#!/usr/bin/env python3
"""Rebuild fig_ebsd.png without in-image anneal-condition titles.

The previous fig_ebsd.png (from build_characterization_crossref.py on the
PR #3 branch) titled panel (a) with its anneal condition (1200 C / 12 h)
while panel (b)'s condition is unrecorded (specimen Ni4N5_069 has no run-log
linkage in the parsed set). Per S. Baird's review (PR #12, 2026-07-22) the
recipe should appear for both panels or neither, so the panels now carry
only their (a)/(b) letters and Table S1 in the SI holds the linkage.

Sources (committed):
  docs/SEM/200303_Ni4N5_034_specialHolder1stTry/reg1_IPF.bmp  -> (a) Ni4N5_034
  docs/SEM/200423_Ni4N5_069/IPF.png                           -> (b) Ni4N5_069

Output: paper/figures/fig_ebsd.png

Usage:  python3 paper/build_ebsd_figure.py
Requires matplotlib + Pillow.
"""
from __future__ import annotations

import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIGURES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")

PANELS = [
    ("(a)", os.path.join(REPO_ROOT, "docs", "SEM",
                         "200303_Ni4N5_034_specialHolder1stTry",
                         "reg1_IPF.bmp")),
    ("(b)", os.path.join(REPO_ROOT, "docs", "SEM", "200423_Ni4N5_069",
                         "IPF.png")),
]


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.6))
    for ax, (label, path) in zip(axes, PANELS):
        ax.imshow(Image.open(path))
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title(label, fontsize=11, fontweight="bold",
                     family="DejaVu Sans", loc="left")
    fig.tight_layout()
    out = os.path.join(FIGURES, "fig_ebsd.png")
    fig.savefig(out, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print("Wrote", os.path.relpath(out, REPO_ROOT))


if __name__ == "__main__":
    main()
