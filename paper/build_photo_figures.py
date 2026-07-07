#!/usr/bin/env python3
"""Compose the assembled-furnace photo figures and the YSZ configuration figure.

Sources (all committed):

* ``docs/furnace-photos/`` -- photographs of the assembled, operating furnace
  contributed by R. Guymon (PR #3): the full assembly at temperature with
  part call-outs (cropped from ``assembled-furnace-callouts.pdf``), the
  chamber-bottom relief valve, the Sierra Smart-Trak mass flow controller, and
  the vibration-isolated roughing-pump support.
* ``docs/YSZ/ysz-stack-schematic.png`` -- hand schematic of the
  tantalum-susceptor / MgO-crucible stack used for high-temperature ceramic
  (YSZ) anneals.
* ``docs/optical/.../190823_YSZ/YSZ_1700C_10h.JPG`` and
  ``docs/optical/.../190909_YSZ/YSZ_induction1_multiplyScaleBy2_.JPG`` --
  committed YSZ optical micrographs.

Outputs (paper/figures/):

* ``fig_furnace_photo.jpg``  -- labeled photo of the assembled system at power.
* ``fig_vacuum_details.jpg`` -- 3-panel vacuum/gas-handling detail photos.
* ``fig_ysz.png``            -- YSZ stack schematic + optical micrographs.

The two pure-photograph figures are written as JPEG (photographic content
compresses ~10x better than PNG, keeping the compiled PDF a reasonable size);
the YSZ figure stays PNG for the line-art schematic panel.

Usage::

    python paper/build_photo_figures.py

Requires matplotlib + Pillow.
"""
from __future__ import annotations

import os
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PHOTOS = os.path.join(REPO_ROOT, "docs", "furnace-photos")
YSZ_DIR = os.path.join(REPO_ROOT, "docs", "YSZ")
OPTICAL = os.path.join(REPO_ROOT, "docs", "optical")
FIGURES = os.path.join(REPO_ROOT, "paper", "figures")

DPI = 300

YSZ_1700 = os.path.join(
    OPTICAL, "CB121", "1908##_SS_etc", "190823_YSZ", "YSZ_1700C_10h.JPG")
YSZ_INDUCTION = os.path.join(
    OPTICAL, "CB121", "1909##_Ni_YSZ_Pd", "190909_YSZ",
    "YSZ_induction1_multiplyScaleBy2_.JPG")


def _load(path: str, max_px: int = 1600) -> Image.Image:
    """Load an image, downscaling so the long edge is at most ``max_px``."""
    img = Image.open(path).convert("RGB")
    w, h = img.size
    scale = max_px / max(w, h)
    if scale < 1.0:
        img = img.resize((int(w * scale), int(h * scale)), Image.LANCZOS)
    return img


def build_furnace_photo() -> str:
    """Labeled photo of the assembled system at operating power."""
    img = _load(os.path.join(PHOTOS, "furnace-assembled-callouts.png"),
                max_px=2000)
    fig, ax = plt.subplots(figsize=(4.6, 4.6 * img.size[1] / img.size[0]))
    ax.imshow(img)
    ax.axis("off")
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
    out = os.path.join(FIGURES, "fig_furnace_photo.jpg")
    fig.savefig(out, dpi=DPI, bbox_inches="tight", pad_inches=0.02,
                pil_kwargs={"quality": 88})
    plt.close(fig)
    return out


def build_vacuum_details() -> str:
    """Two vacuum detail photos as one row (the MFC photo was dropped from the
    manuscript per PR #3 review -- the MFC is described as optional in prose)."""
    panels = [
        ("roughing-pump-isolation.png", "(a)",
         "Pumping station: roughing pump on a\nseparate support (vibration isolation)"),
        ("relief-valve.png", "(b)",
         "Overpressure relief valve at the\nbottom of the chamber stack"),
    ]
    fig, axes = plt.subplots(1, 2, figsize=(6.2, 4.2))
    for ax, (fname, label, caption) in zip(axes, panels):
        img = _load(os.path.join(PHOTOS, fname), max_px=1100)
        ax.imshow(img)
        ax.axis("off")
        ax.set_title(label, fontsize=10, fontweight="bold", loc="left", pad=4)
        ax.text(0.5, -0.03, caption, transform=ax.transAxes, fontsize=7.6,
                color="#222222", ha="center", va="top", linespacing=1.25)
    fig.subplots_adjust(left=0.01, right=0.99, top=0.94, bottom=0.12,
                        wspace=0.05)
    out = os.path.join(FIGURES, "fig_vacuum_details.jpg")
    fig.savefig(out, dpi=DPI, bbox_inches="tight", pad_inches=0.03,
                pil_kwargs={"quality": 88})
    plt.close(fig)
    return out


def build_ysz() -> str:
    """YSZ high-temperature stack schematic + optical micrographs."""
    fig = plt.figure(figsize=(9.0, 4.6))
    gs = fig.add_gridspec(2, 2, width_ratios=[0.9, 1.5], hspace=0.16,
                          wspace=0.05)

    ax_schem = fig.add_subplot(gs[:, 0])
    # Panel (a) uses the redrawn stack schematic (make_ysz_stack_schematic.py ->
    # build_schematic_figures.py), not the original hand sketch.
    ax_schem.imshow(_load(os.path.join(FIGURES, "fig_ysz_stack.png"), max_px=2000))
    ax_schem.axis("off")
    ax_schem.set_title("(a)", fontsize=10, fontweight="bold", loc="left",
                       pad=4)

    ax_b = fig.add_subplot(gs[0, 1])
    ax_b.imshow(_load(YSZ_1700))
    ax_b.axis("off")
    ax_b.set_title("(b)", fontsize=10, fontweight="bold", loc="left", pad=4)

    ax_c = fig.add_subplot(gs[1, 1])
    ax_c.imshow(_load(YSZ_INDUCTION))
    ax_c.axis("off")
    ax_c.set_title("(c)", fontsize=10, fontweight="bold", loc="left", pad=4)

    fig.subplots_adjust(left=0.01, right=0.99, top=0.95, bottom=0.02)
    out = os.path.join(FIGURES, "fig_ysz.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight", pad_inches=0.03)
    plt.close(fig)
    return out


def main() -> int:
    for path in (os.path.join(PHOTOS, "furnace-assembled-callouts.png"),
                 os.path.join(FIGURES, "fig_ysz_stack.png"),
                 YSZ_1700, YSZ_INDUCTION):
        if not os.path.exists(path):
            print(f"ERROR: missing source image {path}", file=sys.stderr)
            return 1
    os.makedirs(FIGURES, exist_ok=True)
    for builder in (build_furnace_photo, build_vacuum_details, build_ysz):
        print(f"wrote {builder()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
