#!/usr/bin/env python3
"""Compose the custom-machined graphite crucible/susceptor photo panel.

The four source photographs live under ``docs/graphite-crucible/`` (lab photos of
the in-house machined two-piece graphite crucible, contributed on the PR). This
script lays them out as a labelled four-panel figure (a)--(d) and writes the
canonical ``fig_crucible.png`` into ``paper/figures/`` so the manuscript uses an
*actual* figure rather than a placeholder.

Usage::

    python paper/build_crucible_figure.py

Re-running is idempotent. Requires Pillow + matplotlib.
"""
from __future__ import annotations

import os
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(REPO_ROOT, "docs", "graphite-crucible")
FIGURES = os.path.join(REPO_ROOT, "paper", "figures")

DPI = 300  # HardwareX requires >=300 dpi raster figures.

# (filename relative to SRC_DIR, panel sub-caption label). Ordered as a
# disassembled -> nested -> assembled (oblique) -> assembled (top) narrative.
PANELS = [
    ("crucible_disassembled.jpg", "(a)"),
    ("crucible_stacked.jpg", "(b)"),
    ("crucible_assembled_oblique.jpg", "(c)"),
    ("crucible_assembled.jpg", "(d)"),
]


def main() -> int:
    images = []
    for fname, label in PANELS:
        path = os.path.join(SRC_DIR, fname)
        if not os.path.exists(path):
            print(f"ERROR: missing source photo {path}", file=sys.stderr)
            return 1
        images.append((Image.open(path), label))

    fig, axes = plt.subplots(2, 2, figsize=(7.0, 5.6))
    for ax, (img, label) in zip(axes.flat, images):
        ax.imshow(img)
        ax.axis("off")
        ax.text(
            0.02, 0.97, label, transform=ax.transAxes,
            fontsize=12, fontweight="bold", color="white",
            va="top", ha="left",
            bbox=dict(boxstyle="round,pad=0.2", fc="black", ec="none", alpha=0.6),
        )

    fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01,
                        wspace=0.03, hspace=0.03)
    os.makedirs(FIGURES, exist_ok=True)
    out = os.path.join(FIGURES, "fig_crucible.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight", pad_inches=0.02)
    plt.close(fig)
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
