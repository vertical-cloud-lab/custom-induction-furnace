#!/usr/bin/env python3
"""Open-source Hough indexing of the committed raw Kikuchi patterns.

Requested by S. Baird (PR #12, 2026-07-22): check whether more raw patterns
like the main-text Kikuchi figure exist, and run open-source indexing on
them. The committed representative patterns (see
docs/SEM/raw-kikuchi-patterns/README.md; more than 100,000 further patterns
survive in the Box archives referenced there) are indexed here with
pyebsdindex (https://github.com/USNavalResearchLaboratory/PyEBSDIndex), the
open-source Radon/Hough band-detection indexer.

The patterns are the EBSD detector's 8x8-binned 115x115 px JPEG output,
saved during orientation mapping of furnace-annealed nickel specimens that
received no metallographic preparation. The detector pattern center is not
recorded with the JPEGs, so it is first fitted per acquisition session with
pyebsdindex's pattern-center optimizer (pcopt) from a nominal EDAX-geometry
starting guess, then all patterns are indexed against an FCC (nickel)
phase.

Usage:  python3 paper/kikuchi_indexing/index_raw_patterns.py
Writes results.csv and prints a summary table.
Requires: pip install pyebsdindex pillow numpy
"""
from __future__ import annotations

import csv
import glob
import math
import os

import numpy as np
from PIL import Image
from pyebsdindex import ebsd_index, pcopt

REPO_ROOT = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT_CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "results.csv")

PC0 = [0.5, 0.7, 0.6]  # nominal EDAX-convention pattern-center guess
N_BANDS = 9

# One group per acquisition session (each session has its own detector
# geometry, hence its own fitted pattern center).
GROUPS = {
    "191026_Ni_003b1a (scans reg1a, rega1a1)":
        "docs/SEM/raw-kikuchi-patterns/191026_Ni_003b1a/**/*_x*.jpg",
    "191031_Ni_003b1a (scan reg2)":
        "docs/SEM/raw-kikuchi-patterns/191031_Ni_003b1a/**/*_x*.jpg",
    "200616 Ni_003a1b (boxscan, background-corrected)":
        "docs/SEM/200616_Ni4N5_007,081_Ni_003b2/Ni4N5_007/"
        "boxscan_003a1b_0degRot/*_x*.jpg",
}


def quat_to_bunge(q):
    """Rowenhorst et al. (2015) quaternion -> Bunge Euler angles (deg)."""
    w, x, y, z = (float(v) for v in q)
    q03, q12 = w * w + z * z, x * x + y * y
    chi = math.sqrt(q03 * q12)
    if chi == 0.0:
        if q12 == 0.0:
            return (math.degrees(math.atan2(-2 * w * z, w * w - z * z)),
                    0.0, 0.0)
        return (math.degrees(math.atan2(2 * x * y, x * x - y * y)),
                180.0, 0.0)
    phi1 = math.atan2((x * z - w * y) / chi, (-w * x - y * z) / chi)
    Phi = math.atan2(2 * chi, q03 - q12)
    phi2 = math.atan2((x * z + w * y) / chi, (y * z - w * x) / chi)
    return tuple(math.degrees(a) % 360.0 for a in (phi1, Phi, phi2))


def main() -> None:
    rows = []
    for session, pattern_glob in GROUPS.items():
        paths = sorted(glob.glob(os.path.join(REPO_ROOT, pattern_glob),
                                 recursive=True))
        if not paths:
            print(f"WARNING: no patterns found for {session}")
            continue
        pats = np.stack([np.asarray(Image.open(p).convert("L"),
                                    dtype=np.float32) for p in paths])
        indexer = ebsd_index.EBSDIndexer(
            phaselist=["FCC"], PC=PC0, patDim=pats.shape[1:],
            sampleTilt=70.0, camElev=5.3, vendor="EDAX", nBands=N_BANDS)
        pc = pcopt.optimize(pats, indexer, PC0=PC0, batch=False)
        print(f"\n{session}\n  fitted pattern center (EDAX x*,y*,z*): "
              f"{np.round(pc, 4).tolist()}")
        data, _ = indexer.index_pats(pats, PC=pc)[:2]
        for path, r in zip(paths, data[-1]):
            eulers = quat_to_bunge(np.asarray(r["quat"], float))
            indexed = int(r["phase"]) == 0 and float(r["fit"]) < 2.0
            rows.append({
                "session": session,
                "pattern": os.path.relpath(path, REPO_ROOT),
                "indexed_phase": "FCC (Ni)" if indexed else "unindexed",
                "bands_matched": f"{int(r['nmatch'])}/{N_BANDS}",
                "mean_band_fit_deg": round(float(r["fit"]), 2),
                "confidence_metric": round(float(r["cm"]), 3),
                "phi1_deg": round(eulers[0], 1),
                "Phi_deg": round(eulers[1], 1),
                "phi2_deg": round(eulers[2], 1),
            })
            print("  %-52s %-9s bands %s  fit %.2f deg  CM %.3f" % (
                os.path.basename(path), rows[-1]["indexed_phase"],
                rows[-1]["bands_matched"], rows[-1]["mean_band_fit_deg"],
                rows[-1]["confidence_metric"]))
    with open(OUT_CSV, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"\nWrote {os.path.relpath(OUT_CSV, REPO_ROOT)} "
          f"({len(rows)} patterns)")


if __name__ == "__main__":
    main()
