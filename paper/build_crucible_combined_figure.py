#!/usr/bin/env python3
"""Compose the combined graphite-crucible figure (disassembled + assembly).

Merges the former standalone figures fig_crucible.png (fully disassembled
parts) and fig_crucible_assembly.png (three-step loading sequence) into one
figure, per S. Baird's review (PR #12, 2026-07-22). Unlike the previous
fig_crucible_assembly.png, no caption text is baked into the image: panels
carry only their (a)-(d) letters (one font, one size); all descriptive text
lives in the LaTeX caption. The orange part call-outs composited into the
source crops are kept.

Sources (committed):
  docs/graphite-crucible/crucible_disassembled.jpg          -> panel (a)
  docs/graphite-crucible/assembly-crops/step1_*.png          -> panel (b)
  docs/graphite-crucible/assembly-crops/step2_*.png          -> panel (c)
  docs/graphite-crucible/assembly-crops/step3_*.png          -> panel (d)

Output: paper/figures/fig_crucible_combined.png

Usage:  python3 paper/build_crucible_combined_figure.py
Requires matplotlib + Pillow.
"""
from __future__ import annotations

import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(REPO_ROOT, "docs", "graphite-crucible")
FIGURES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")

DPI = 300
LABEL_KW = dict(fontsize=11, fontweight="bold", family="DejaVu Sans",
                va="top", ha="left")

PANELS = [
    ("(a)", os.path.join(SRC, "crucible_disassembled.jpg")),
    ("(b)", os.path.join(SRC, "assembly-crops", "step1_sample_on_alumina.png")),
    ("(c)", os.path.join(SRC, "assembly-crops", "step2_lid_on.png")),
    ("(d)", os.path.join(SRC, "assembly-crops", "step3_sapphire_window.png")),
]


def main() -> None:
    fig = plt.figure(figsize=(6.4, 5.2))
    gs = fig.add_gridspec(2, 3, height_ratios=[1.15, 1.0],
                          hspace=0.06, wspace=0.05)
    axes = [fig.add_subplot(gs[0, :]),
            fig.add_subplot(gs[1, 0]),
            fig.add_subplot(gs[1, 1]),
            fig.add_subplot(gs[1, 2])]
    for ax, (label, path) in zip(axes, PANELS):
        ax.imshow(Image.open(path))
        ax.set_xticks([])
        ax.set_yticks([])
        for s in ax.spines.values():
            s.set_visible(False)
        ax.text(0.02, 0.98, label, transform=ax.transAxes,
                color="white", bbox=dict(facecolor="black", alpha=0.55,
                                         pad=2, edgecolor="none"),
                **LABEL_KW)
    out = os.path.join(FIGURES, "fig_crucible_combined.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print("Wrote", os.path.relpath(out, REPO_ROOT))


if __name__ == "__main__":
    main()
