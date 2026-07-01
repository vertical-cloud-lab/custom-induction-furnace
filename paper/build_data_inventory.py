#!/usr/bin/env python3
"""Generate a machine-readable inventory of the experimental data in ``docs/``.

The induction-furnace project accumulated ~100 logged anneal runs plus SEM/optical
characterization. This script summarizes what exists (run IDs, materials, soak
temperature/time parsed from the file names, file types, and characterization
assets) into ``paper/journal-assessment/DATA_INVENTORY.md`` so the question
"is there enough data for a traditional journal paper without new experiments?"
can be answered from version-controlled context.

The script is read-only with respect to ``docs/`` and idempotent.

Usage::

    python paper/build_data_inventory.py
"""
from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
DOCS = REPO / "docs"
OUT = HERE / "journal-assessment" / "DATA_INVENTORY.md"

# e.g. "1200C_12h", "1400C_10min", "1325C_40h"
COND_RE = re.compile(r"(\d{3,4})\s*C[_\- ]*(\d+\.?\d*)\s*(h|min)", re.IGNORECASE)
MATERIALS = ("Ni200", "Ni4N5", "Pd", "YSZ", "crucible", "evap")


def parse_runs() -> list[dict]:
    data_log = DOCS / "data_log"
    rows: list[dict] = []
    if not data_log.exists():
        return rows
    for p in sorted(data_log.rglob("*")):
        if not p.is_file():
            continue
        name = p.name
        mat = next((m for m in MATERIALS if m.lower() in name.lower()), "")
        cond = COND_RE.search(name)
        temp = int(cond.group(1)) if cond else None
        soak = f"{cond.group(2)}{cond.group(3).lower()}" if cond else ""
        rows.append({
            "rel": str(p.relative_to(DOCS)),
            "name": name,
            "material": mat,
            "temp_C": temp,
            "soak": soak,
            "ext": p.suffix.lower().lstrip("."),
        })
    return rows


def fmt_table(rows: list[dict]) -> str:
    keep = [r for r in rows if r["temp_C"] or r["material"]]
    lines = ["| Run / file | Material | Soak T (°C) | Soak time | Type |",
             "|------------|----------|------------:|-----------|------|"]
    for r in sorted(keep, key=lambda r: r["rel"]):
        lines.append(f"| {r['rel']} | {r['material'] or '—'} | "
                     f"{r['temp_C'] or '—'} | {r['soak'] or '—'} | {r['ext']} |")
    return "\n".join(lines)


def characterization_assets() -> list[str]:
    out = []
    for rel in ("student-work/RyanWeber.pdf",
                "equipment-reference",
                "ThermalEvaporation"):
        p = DOCS / rel
        if p.exists():
            if p.is_dir():
                n = sum(1 for _ in p.rglob("*") if _.is_file())
                out.append(f"- `docs/{rel}/` — {n} file(s)")
            else:
                out.append(f"- `docs/{rel}` — {p.stat().st_size // 1024} KB")
    return out


def thermal_traces_section() -> list[str]:
    """Summarize the parsed raw-data thermal traces and validation cohorts."""
    summ = DOCS / "data_log" / "processed" / "run_summary.csv"
    if not summ.exists():
        return []
    rows = list(csv.DictReader(summ.open()))
    n = len(rows)
    peaks = [float(r["peak_temp_C"]) for r in rows if r["peak_temp_C"]]
    soaks = [float(r["soak_temp_C"]) for r in rows if r["soak_temp_C"]]
    durs = [float(r["duration_min"]) for r in rows if r["duration_min"]]
    flow = Counter(r["has_flow"] for r in rows)
    bullets = [f"- **Runs with a parsed trace:** {n}"]
    if peaks:
        bullets.append(f"- **Peak temperature range (°C):** "
                       f"{min(peaks):.0f}–{max(peaks):.0f}")
    if soaks:
        bullets.append(f"- **Soak-mean temperature range (°C):** "
                       f"{min(soaks):.0f}–{max(soaks):.0f}")
    if durs:
        bullets.append(f"- **Soak duration range (min):** "
                       f"{min(durs):.0f}–{max(durs):.0f} (≈{max(durs)/60:.0f} h)")
    bullets.append("- **Gas-flow flag:** "
                   + ", ".join(f"{k}={v}" for k, v in flow.most_common()))
    out = [
        "## Parsed raw-data thermal traces",
        "",
        "The raw `.xlsx`/`.lvm` run logs were parsed into uniform per-run CSV/PNG",
        "traces under `docs/data_log/processed/` by `paper/build_run_traces.py`",
        "(time, analog power command, pyrometer temperature, optional flow).",
        "",
        *bullets,
        "",
    ]
    metrics = HERE / "validation-metrics.json"
    if metrics.exists():
        m = json.loads(metrics.read_text())
        cal = m["calibration"]["fit"]
        rep = m["repeatability"]["stats"]
        out += [
            "### Validation cohorts (computed by `build_validation_figures.py`)",
            "",
            f"- **Power→temperature calibration** (fixed Ni4N5 geometry, "
            f"n={cal['n']}): T = {cal['intercept']:.0f} + {cal['slope']:.0f}·I (mA), "
            f"R² = {cal['r2']:.3f}.",
            f"- **Repeatability** (Ni4N5 1200 °C / 12 h, n={rep['n']}): "
            f"{rep['soak_mean_C']:.1f} ± {rep['soak_sd_C']:.1f} °C "
            f"(CV {rep['cv_pct']:.2f}%).",
            "- **Long-soak stability** (Ni200, 1325 °C): "
            "20 h and 40 h runs held within a few °C of setpoint.",
            "",
        ]
    return out


def sem_optical_section() -> list[str]:
    """Summarize the SEM/optical catalogs (full archive vs committed subset)."""
    out = ["## SEM / optical characterization catalog", ""]
    any_found = False
    for top, label in (("SEM", "SEM / EBSD"), ("optical", "Optical microscopy")):
        cat = DOCS / top / "CATALOG.csv"
        if not cat.exists():
            continue
        any_found = True
        rows = list(csv.DictReader(cat.open()))
        nfull = len(rows)
        sfull = sum(int(r["size_bytes"]) for r in rows)
        comm = [r for r in rows if r["committed"] == "yes"]
        scomm = sum(int(r["size_bytes"]) for r in comm)
        exts = Counter(r["ext"] for r in rows)
        out += [
            f"- **{label}** (`docs/{top}/`): full archive {nfull} files, "
            f"{sfull/1e9:.2f} GB; representative subset committed here "
            f"{len(comm)} files, {scomm/1e6:.0f} MB. Top file types: "
            + ", ".join(f"{k} ({v})" for k, v in exts.most_common(6)) + ".",
        ]
    if not any_found:
        return []
    out += [
        "",
        "Full per-file inventories are in `docs/SEM/CATALOG.csv` and",
        "`docs/optical/CATALOG.csv`; the complete multi-gigabyte raster/EBSD",
        "archives remain on the lab's Box share (see each folder's README).",
        "",
    ]
    return out


def main() -> None:
    rows = parse_runs()
    mats = Counter(r["material"] for r in rows if r["material"])
    temps = sorted({r["temp_C"] for r in rows if r["temp_C"]})
    by_ext = Counter(r["ext"] for r in rows)
    # group run IDs by material
    runs_by_mat: dict[str, set[str]] = defaultdict(set)
    for r in rows:
        m = re.search(r"IFrun\d+", r["name"], re.IGNORECASE)
        if m and r["material"]:
            runs_by_mat[r["material"]].add(m.group(0))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    md = ["# Experimental data inventory (auto-generated)",
          "",
          "Generated by `paper/build_data_inventory.py` from the binary data files in",
          "`docs/`. This summarizes what already exists **without any new experiments**,",
          "to assess feasibility of a traditional (non-HardwareX) journal contribution.",
          "",
          "## Summary",
          "",
          f"- **Total files under `docs/data_log/`:** "
          f"{sum(1 for _ in (DOCS / 'data_log').rglob('*') if _.is_file())}",
          f"- **Files with a parseable material/condition label:** {len(rows)}",
          f"- **Materials (by labeled file count):** "
          + ", ".join(f"{k} ({v})" for k, v in mats.most_common()),
          f"- **Soak temperatures observed (°C):** "
          + ", ".join(str(t) for t in temps),
          f"- **Data file types:** "
          + ", ".join(f"{k or 'none'} ({v})" for k, v in by_ext.most_common()),
          "",
          "### Distinct run IDs by material",
          ""]
    for mat, ids in sorted(runs_by_mat.items()):
        md.append(f"- **{mat}:** {len(ids)} runs — "
                  + ", ".join(sorted(ids)))
    md += ["",
           *thermal_traces_section(),
           "## Characterization / supporting assets",
           "",
           *characterization_assets(),
           "",
           *sem_optical_section(),
           "## Labeled runs (material + soak condition parsed from filename)",
           "",
           fmt_table(rows),
           ""]
    OUT.write_text("\n".join(md))
    print(f"wrote {OUT.relative_to(REPO)} ({len(rows)} labeled files)")


if __name__ == "__main__":
    main()
