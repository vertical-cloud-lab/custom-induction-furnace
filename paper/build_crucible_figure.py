#!/usr/bin/env python3
"""Compose the fully-disassembled graphite crucible/susceptor photo.

The source photograph lives under ``docs/graphite-crucible/`` (a lab photo of the
in-house machined two-piece graphite crucible with its alumina spacer discs and
sapphire pyrometer window laid out). This script normalises it to a single clean
300 dpi ``fig_crucible.png`` under ``paper/figures/`` so the manuscript uses an
*actual* photo rather than a placeholder.

The previous four-panel version duplicated the assembly-sequence photos already
shown (with call-outs) in ``fig_crucible_assembly.png``; per review it is reduced
to just this single disassembled overview, whose caption names each laid-out part.

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

# Single disassembled overview: lid (top left), cup body / specimen carrier
# (top middle), sapphire window (far right), two alumina spacer sheets (bottom).
SRC = "crucible_disassembled.jpg"


def main() -> int:
    path = os.path.join(SRC_DIR, SRC)
    if not os.path.exists(path):
        print(f"ERROR: missing source photo {path}", file=sys.stderr)
        return 1
    img = Image.open(path)

    w, h = img.size
    fig, ax = plt.subplots(figsize=(6.0, 6.0 * h / w))
    ax.imshow(img)
    ax.axis("off")

    fig.subplots_adjust(left=0.0, right=1.0, top=1.0, bottom=0.0)
    os.makedirs(FIGURES, exist_ok=True)
    out = os.path.join(FIGURES, "fig_crucible.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight", pad_inches=0.0)
    plt.close(fig)
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
