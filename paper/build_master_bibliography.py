#!/usr/bin/env python3
"""
Build a master bibliography from every Edison literature query in this repo.

This script collects all BibTeX entries produced by the Edison Scientific
literature searches stored under ``literature-search/`` (the per-query
``references.bib`` files and the ``combined_references.bib`` rollups),
de-duplicates them by DOI (falling back to a normalized title), and validates
that each entry's DOI/URL resolves to a live page (non-404). The validated,
de-duplicated set is written to ``paper/references.bib`` for use by the
manuscript, and a human-readable validation report is written to
``paper/edison-feedback/bibliography-validation.md``.

The script is idempotent and re-runnable; pass ``--no-validate`` to skip the
network checks (e.g. offline) and just rebuild the merged ``references.bib``.

Usage:
    python build_master_bibliography.py [--no-validate] [--workers N]
"""

from __future__ import annotations

import argparse
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

try:
    import requests
except ImportError:  # pragma: no cover - requests is a hard dependency here
    print("❌ 'requests' is required. Install with: pip install requests")
    sys.exit(1)

REPO_ROOT = Path(__file__).resolve().parent.parent
LIT_DIR = REPO_ROOT / "literature-search"
OUT_BIB = REPO_ROOT / "paper" / "references.bib"
REPORT = REPO_ROOT / "paper" / "edison-feedback" / "bibliography-validation.md"

ENTRY_RE = re.compile(r"@(\w+)\s*\{\s*([^,]+),(.*?)\n\}", re.DOTALL)
FIELD_RE = re.compile(r'(\w+)\s*=\s*"(.*?)"\s*,?\s*$', re.MULTILINE)


def parse_bib(text: str) -> list[dict]:
    """Parse a BibTeX string into a list of entry dicts."""
    entries = []
    for m in ENTRY_RE.finditer(text):
        etype, key, body = m.groups()
        fields = {k.lower(): v.strip() for k, v in FIELD_RE.findall(body)}
        fields["__type__"] = etype.lower()
        fields["__key__"] = key.strip()
        entries.append(fields)
    return entries


def clean_doi(doi: str) -> str:
    """Strip LaTeX escaping/whitespace from a DOI string."""
    return doi.replace("\\_", "_").replace("\\", "").strip()


def norm_doi(entry: dict) -> str | None:
    doi = clean_doi(entry.get("doi", "")).lower()
    if doi:
        return doi
    url = entry.get("url", "")
    m = re.search(r"doi\.org/(10\.\S+)", url, re.IGNORECASE)
    return clean_doi(m.group(1)).lower() if m else None


def norm_title(entry: dict) -> str:
    return re.sub(r"[^a-z0-9]+", "", entry.get("title", "").lower())


def collect_entries() -> list[dict]:
    """Collect entries from every per-query references.bib (best field quality)."""
    entries: list[dict] = []
    for bib in sorted(LIT_DIR.rglob("references.bib")):
        text = bib.read_text(encoding="utf-8", errors="replace")
        for e in parse_bib(text):
            e["__source__"] = str(bib.relative_to(REPO_ROOT))
            entries.append(e)
    return entries


def dedupe(entries: list[dict]) -> list[dict]:
    """De-duplicate by DOI, then by normalized title. Prefer richer entries."""
    by_id: dict[str, dict] = {}
    for e in entries:
        doi = norm_doi(e)
        ident = f"doi:{doi}" if doi else f"title:{norm_title(e)}"
        if not ident or ident in ("title:",):
            ident = f"key:{e['__key__']}"
        prev = by_id.get(ident)
        if prev is None or len(e) > len(prev):
            by_id[ident] = e
    return list(by_id.values())


def validate_url(entry: dict, timeout: int = 25) -> tuple[bool, str]:
    """Return (ok, note). ok is True if the DOI/URL resolves (non-404).

    Many publishers (ACS, Wiley, SAGE, ASM, SciELO, IET, ...) reject automated
    HEAD/GET requests with 401/403/429 even though the DOI is perfectly valid.
    We therefore treat those bot-blocking statuses as "reachable" and only flag
    genuine 404/410 (not found / gone) or connection failures as broken. When a
    DOI is present we validate the canonical ``https://doi.org/<doi>`` form
    rather than a publisher-specific URL that may itself be stale.
    """
    doi = norm_doi(entry)
    if doi:
        url = f"https://doi.org/{doi}"
    else:
        url = entry.get("url", "")
    if not url:
        return True, "no-url (kept; no link to validate)"
    headers = {"User-Agent": "Mozilla/5.0 (bibliography-validator)"}
    bot_blocked = {401, 403, 429}
    try:
        r = requests.head(url, allow_redirects=True, timeout=timeout, headers=headers)
        if r.status_code >= 400 and r.status_code not in bot_blocked:
            # Some servers reject HEAD; retry with a lightweight GET.
            r = requests.get(
                url, allow_redirects=True, timeout=timeout, headers=headers, stream=True
            )
        if r.status_code in bot_blocked:
            return True, f"HTTP {r.status_code} (reachable; bot-blocked) -> {r.url}"
        ok = r.status_code < 400
        return ok, f"HTTP {r.status_code} -> {r.url}"
    except Exception as exc:  # noqa: BLE001 - report and continue
        return False, f"error: {exc}"


def render_entry(e: dict) -> str:
    skip = {"__type__", "__key__", "__source__"}
    # Normalize DOI/URL so the emitted .bib has clean, resolvable links.
    doi = norm_doi(e)
    if doi:
        e["doi"] = doi
        e["url"] = f"https://doi.org/{doi}"
    lines = [f"@{e['__type__']}{{{e['__key__']},"]
    order = ["author", "title", "journal", "volume", "number", "pages",
             "year", "month", "publisher", "doi", "url"]
    keys = [k for k in order if k in e] + [k for k in e if k not in skip and k not in order]
    for k in keys:
        lines.append(f'    {k} = "{e[k]}",')
    if len(lines) > 1:
        lines[-1] = lines[-1].rstrip(",")
    lines.append("}")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--no-validate", action="store_true",
                    help="Skip network URL/DOI validation.")
    ap.add_argument("--workers", type=int, default=8,
                    help="Concurrent validation workers (default: 8).")
    args = ap.parse_args()

    raw = collect_entries()
    entries = dedupe(raw)
    entries.sort(key=lambda e: e["__key__"].lower())
    print(f"Collected {len(raw)} entries; {len(entries)} unique after de-dup.")

    results: dict[str, tuple[bool, str]] = {}
    if not args.no_validate:
        print("Validating DOIs/URLs (non-404 check)...")
        with ThreadPoolExecutor(max_workers=args.workers) as ex:
            for e, (ok, note) in zip(entries, ex.map(validate_url, entries)):
                results[e["__key__"]] = (ok, note)
                flag = "✓" if ok else "✗"
                print(f"  {flag} {e['__key__']}: {note}")

    # Write the master bibliography (all unique entries are kept; broken links
    # are flagged in the report rather than silently dropped).
    header = (
        "% Master bibliography for the HardwareX manuscript.\n"
        "% Auto-generated by paper/build_master_bibliography.py from the Edison\n"
        "% literature queries under literature-search/. Do not edit by hand;\n"
        "% re-run the builder to regenerate. See edison-feedback/\n"
        "% bibliography-validation.md for the URL/DOI validation report.\n\n"
    )
    OUT_BIB.write_text(header + "\n\n".join(render_entry(e) for e in entries) + "\n",
                       encoding="utf-8")
    print(f"Wrote {OUT_BIB.relative_to(REPO_ROOT)} ({len(entries)} entries).")

    if not args.no_validate:
        n_ok = sum(1 for ok, _ in results.values() if ok)
        n_bad = len(results) - n_ok
        lines = [
            "# Master bibliography validation report",
            "",
            "Generated by `paper/build_master_bibliography.py`. Each entry's DOI/URL "
            "was checked for a non-404 (HTTP < 400) response.",
            "",
            f"- Unique references: **{len(entries)}**",
            f"- Resolving (non-404): **{n_ok}**",
            f"- Broken / unreachable: **{n_bad}**",
            "",
            "| Key | Status | Detail |",
            "|-----|--------|--------|",
        ]
        for e in entries:
            ok, note = results.get(e["__key__"], (True, "not validated"))
            status = "✅ ok" if ok else "❌ broken"
            lines.append(f"| `{e['__key__']}` | {status} | {note} |")
        REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"Wrote {REPORT.relative_to(REPO_ROOT)} "
              f"({n_ok} ok, {n_bad} broken).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
