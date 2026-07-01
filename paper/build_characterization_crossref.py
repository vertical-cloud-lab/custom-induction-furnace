#!/usr/bin/env python3
"""Correlate the committed SEM / EBSD / optical characterization data with the
archived furnace runs and build manuscript-ready microstructure figures.

The characterization folders under ``docs/SEM/`` and ``docs/optical/`` are named
by date and specimen (e.g. ``200507_Ni4N5_081``); the ``Ni4N5_###`` /
``Ni200_###`` specimen IDs map back to the annealing runs parsed into
``docs/data_log/processed/run_summary.csv``. This script:

1. Parses the run summary into a specimen -> thermal-history index.
2. Walks the committed characterization files, classifies each by technique
   (SEM imaging, EBSD/OIM, EDS, or optical), and extracts its specimen ID(s).
3. Joins the two on specimen ID and writes a reproducible cross-reference
   (``paper/characterization-crossref.csv`` + ``.md``) flagging which specimens
   have a matched run log.
4. Renders real micrographs/maps into labeled manuscript panels in
   ``paper/figures/`` (EBSD IPF maps and a multimodal SEM+EBSD+optical figure for
   the best-correlated specimen).

Usage::

    python3 paper/build_characterization_crossref.py
"""
from __future__ import annotations

import csv
import re
from collections import defaultdict
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SUMMARY = ROOT / "docs" / "data_log" / "processed" / "run_summary.csv"
SEM_DIR = ROOT / "docs" / "SEM"
OPT_DIR = ROOT / "docs" / "optical"
FIG_DIR = Path(__file__).resolve().parent / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)
OUT_CSV = Path(__file__).resolve().parent / "characterization-crossref.csv"
OUT_MD = Path(__file__).resolve().parent / "characterization-crossref.md"

# Specimen-ID pattern: a material prefix + a zero-padded number, e.g. Ni4N5_081,
# Ni200_015, NiCube_001, Ni_003b2.
SPEC_RE = re.compile(r"(Ni4N5|Ni200|NiCube|Ni)_(\d{3}[a-z0-9]*)", re.IGNORECASE)

# Image extensions we can render.
IMG_EXT = {".tif", ".tiff", ".bmp", ".png", ".jpg", ".jpeg"}

# Keywords that mark a file as EBSD/OIM rather than a plain SEM micrograph.
EBSD_KW = ("ipf", "iq", "oim", "boxscan", "ebsd", "misorient", "step", "scan")
EBSD_EXT = {".ang", ".oim", ".osc", ".ctf", ".cpr", ".crc"}
EDS_KW = ("eds", "spectrum")


def norm_spec(prefix: str, num: str) -> str:
    """Canonical specimen key, e.g. ('Ni4N5','081') -> 'Ni4N5_081'."""
    prefix = {"ni4n5": "Ni4N5", "ni200": "Ni200", "nicube": "NiCube", "ni": "Ni"}[
        prefix.lower()
    ]
    return f"{prefix}_{num}"


def specimens_in(text: str) -> set[str]:
    out = set()
    for m in SPEC_RE.finditer(text):
        out.add(norm_spec(m.group(1), m.group(2)))
    return out


def specimens_for_file(rel: Path) -> set[str]:
    """Attribute a file to the deepest path component that names a specimen.

    Folders like ``200616_Ni4N5_007,081_Ni_003b2`` hold per-specimen subfolders,
    so a file is credited only to the most specific component (its own name, then
    nearest parent) that contains a specimen ID -- not to every ancestor."""
    for part in (rel.name, *[p for p in reversed(rel.parent.parts)]):
        specs = specimens_in(part)
        if specs:
            return specs
    return set()


def classify(path: Path) -> str:
    name = path.name.lower()
    ext = path.suffix.lower()
    parts = [p.lower() for p in path.parts]
    if "optical" in parts:
        return "optical"
    if any(k in name for k in EDS_KW) or "eds" in parts:
        return "EDS"
    if ext in EBSD_EXT or any(k in name for k in EBSD_KW):
        return "EBSD"
    return "SEM"


def load_runs() -> dict[str, list[dict]]:
    """specimen-key -> list of run records (deduplicated by run base name)."""
    index: dict[str, list[dict]] = defaultdict(list)
    seen: set[tuple[str, str]] = set()
    if not SUMMARY.exists():
        return index
    with SUMMARY.open(newline="") as fh:
        for row in csv.DictReader(fh):
            run = (row.get("run") or "").strip().strip('"')
            if not run or run in {"run", "checktestdata", "trent_test1"}:
                continue
            specs = specimens_in(run)
            for spec in specs:
                key = (spec, run)
                if key in seen:
                    continue
                seen.add(key)
                index[spec].append(
                    {
                        "run": run,
                        "soak_temp_C": row.get("soak_temp_C", ""),
                        "peak_temp_C": row.get("peak_temp_C", ""),
                        "duration_min": row.get("duration_min", ""),
                        "has_flow": row.get("has_flow", ""),
                    }
                )
    return index


def walk_char(base: Path, source: str) -> dict[str, dict]:
    """specimen-key -> aggregated characterization record for one source tree."""
    recs: dict[str, dict] = {}
    if not base.exists():
        return recs
    for path in sorted(base.rglob("*")):
        if not path.is_file():
            continue
        if path.name in {"CATALOG.csv", "README.md"}:
            continue
        rel = path.relative_to(ROOT)
        # Credit the file to the most specific specimen component in its path.
        specs = specimens_for_file(rel)
        if not specs:
            continue
        technique = classify(path)
        for spec in specs:
            rec = recs.setdefault(
                spec,
                {
                    "source": source,
                    "folders": set(),
                    "n_files": 0,
                    "techniques": set(),
                    "img_files": [],
                },
            )
            rec["folders"].add(str(rel.parent))
            rec["n_files"] += 1
            rec["techniques"].add(technique)
            if path.suffix.lower() in IMG_EXT:
                rec["img_files"].append(str(rel))
    return recs


def build_crossref(runs, sem, opt) -> list[dict]:
    specs = sorted(set(runs) | set(sem) | set(opt))
    rows = []
    for spec in specs:
        run_recs = runs.get(spec, [])
        sem_rec = sem.get(spec)
        opt_rec = opt.get(spec)
        techniques = set()
        if sem_rec:
            techniques |= sem_rec["techniques"]
        if opt_rec:
            techniques |= opt_rec["techniques"]
        # Only emit specimens that actually have characterization data.
        if not sem_rec and not opt_rec:
            continue
        material = spec.split("_")[0]
        run_ids = "; ".join(r["run"] for r in run_recs)
        soaks = "; ".join(
            f"{r['soak_temp_C']}C/{r['duration_min']}min" for r in run_recs if r["soak_temp_C"]
        )
        rows.append(
            {
                "specimen": spec,
                "material": material,
                "matched_runs": run_ids,
                "run_thermal_history": soaks,
                "sem_files": sem_rec["n_files"] if sem_rec else 0,
                "optical_files": opt_rec["n_files"] if opt_rec else 0,
                "techniques": ", ".join(sorted(techniques)),
                "has_ebsd": "yes" if "EBSD" in techniques else "no",
                "has_eds": "yes" if "EDS" in techniques else "no",
                "matched": "yes" if run_recs else "no",
                "sem_folders": "; ".join(sorted(sem_rec["folders"])) if sem_rec else "",
                "optical_folders": "; ".join(sorted(opt_rec["folders"])) if opt_rec else "",
            }
        )
    return rows


def write_csv(rows):
    fields = [
        "specimen",
        "material",
        "matched_runs",
        "run_thermal_history",
        "sem_files",
        "optical_files",
        "techniques",
        "has_ebsd",
        "has_eds",
        "matched",
        "sem_folders",
        "optical_folders",
    ]
    with OUT_CSV.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow(r)


def write_md(rows):
    matched = [r for r in rows if r["matched"] == "yes"]
    lines = [
        "# SEM / EBSD / optical \u2194 furnace-run cross-reference",
        "",
        "Auto-generated by `paper/build_characterization_crossref.py`. Each row is a",
        "characterized specimen; `matched_runs` is the archived furnace run(s) whose",
        "`Ni4N5_###` / `Ni200_###` specimen ID matches the characterization folder, with",
        "the machine-parsed soak temperature/duration from",
        "`docs/data_log/processed/run_summary.csv`.",
        "",
        f"- Characterized specimens with committed data: **{len(rows)}**",
        f"- Of those, specimens with a matched parsed run log: **{len(matched)}**",
        f"- Specimens with committed EBSD/OIM data: "
        f"**{sum(1 for r in rows if r['has_ebsd'] == 'yes')}**",
        f"- Specimens with committed EDS data: "
        f"**{sum(1 for r in rows if r['has_eds'] == 'yes')}**",
        "",
        "| Specimen | Material | Matched run(s) | Soak (parsed) | SEM files | Optical files | Techniques | EBSD | EDS |",
        "|---|---|---|---|---:|---:|---|:--:|:--:|",
    ]
    for r in rows:
        lines.append(
            "| {specimen} | {material} | {runs} | {soak} | {sem} | {opt} | {tech} | {ebsd} | {eds} |".format(
                specimen=r["specimen"],
                material=r["material"],
                runs=r["matched_runs"] or "\u2014",
                soak=r["run_thermal_history"] or "\u2014",
                sem=r["sem_files"],
                opt=r["optical_files"],
                tech=r["techniques"],
                ebsd=r["has_ebsd"],
                eds=r["has_eds"],
            )
        )
    lines.append("")
    OUT_MD.write_text("\n".join(lines))


# ----------------------------------------------------------------------------
# Figure rendering
# ----------------------------------------------------------------------------
def load_img(rel: str) -> np.ndarray:
    """Load an image (relative to repo root) as an 8-bit display array."""
    im = Image.open(ROOT / rel)
    if im.mode == "I;16" or im.mode == "I":
        arr = np.asarray(im, dtype=np.float64)
        lo, hi = np.percentile(arr, (1, 99))
        if hi <= lo:
            hi = lo + 1
        arr = np.clip((arr - lo) / (hi - lo), 0, 1)
        return arr  # grayscale float
    if im.mode == "RGBA":
        im = im.convert("RGB")
    if im.mode == "L":
        return np.asarray(im, dtype=np.float64) / 255.0
    return np.asarray(im.convert("RGB"))


def show(ax, rel: str, title: str):
    arr = load_img(rel)
    if arr.ndim == 2:
        ax.imshow(arr, cmap="gray")
    else:
        ax.imshow(arr)
    ax.set_title(title, fontsize=9)
    ax.set_xticks([])
    ax.set_yticks([])


def fig_ebsd():
    """EBSD inverse-pole-figure orientation maps of two annealed specimens."""
    panels = [
        (
            "docs/SEM/200303_Ni4N5_034_specialHolder1stTry/reg1_IPF.bmp",
            "(a) Ni4N5_034 IPF map\nIFrun049, 1200 C / 12 h",
        ),
        (
            "docs/SEM/200423_Ni4N5_069/IPF.png",
            "(b) Ni4N5_069 IPF map\n(annealed, EBSD)",
        ),
    ]
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.8))
    for ax, (rel, title) in zip(axes, panels):
        show(ax, rel, title)
    fig.tight_layout()
    out = FIG_DIR / "fig_ebsd.png"
    fig.savefig(out, dpi=200, bbox_inches="tight")
    plt.close(fig)
    return out


def fig_multimodal():
    """Multi-scale microstructure of the best-correlated specimen (Ni4N5_081,
    IFrun082, 1300 C / 20 h): optical grain map -> SEM survey -> SEM GB detail."""
    panels = [
        (
            "docs/optical/CB121/2005##_Ni200_Ni4N5/200506_Ni4N5_081/im_sclbr_measure_1.jpg",
            "(a) Optical, grain structure\n(scale bar + grain-size measurements)",
        ),
        (
            "docs/SEM/200616_Ni4N5_007,081_Ni_003b2/Ni4N5_081/im_003.tif",
            "(b) SEM survey",
        ),
        (
            "docs/SEM/200511_Ni4N5_081_postEP/GB.tif",
            "(c) SEM grain-boundary detail",
        ),
    ]
    fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.6))
    for ax, (rel, title) in zip(axes, panels):
        show(ax, rel, title)
    fig.suptitle(
        "Ni4N5_081 microstructure after IFrun082 (1300 \u00b0C / 20 h, flow)",
        fontsize=10,
    )
    fig.tight_layout(rect=(0, 0, 1, 0.93))
    out = FIG_DIR / "fig_microstructure.png"
    fig.savefig(out, dpi=200, bbox_inches="tight")
    plt.close(fig)
    return out


def main():
    runs = load_runs()
    sem = walk_char(SEM_DIR, "SEM")
    opt = walk_char(OPT_DIR, "optical")
    rows = build_crossref(runs, sem, opt)
    write_csv(rows)
    write_md(rows)
    print(f"Wrote {OUT_CSV.relative_to(ROOT)} ({len(rows)} specimens)")
    print(f"Wrote {OUT_MD.relative_to(ROOT)}")
    for fn in (fig_ebsd, fig_multimodal):
        out = fn()
        print(f"Wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
