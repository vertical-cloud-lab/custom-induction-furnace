#!/usr/bin/env python3
"""Compose the graphite crucible assembly-sequence figure.

Ronnie Guymon's slide deck (``docs/graphite-crucible/
Induction-Furnace-images-with-callouts.pdf``) closes with three photographs that
walk through loading a specimen into the two-piece graphite crucible/susceptor in
the correct order. Each photo carries orange call-out labels naming the visible
parts. This builder renders those three slides (compositing the call-out text and
arrows over the photo) into a single left-to-right assembly sequence with a short
caption beneath each step.

The three assembly steps are the *last three* slides of the deck:

    step 1 (page 8)  -- specimen on the alumina sheet in the crucible body
    step 2 (page 9)  -- the lid placed on the alumina/sample stack
    step 3 (page 10) -- the sapphire window placed on the lid (pyrometer sighting)

If PyMuPDF (``fitz``) is installed the crops are regenerated from the committed
PDF so the figure is fully reproducible from source; otherwise the committed
crops under ``docs/graphite-crucible/assembly-crops/`` are used directly (so
``make figures`` works without PyMuPDF).

Output: ``paper/figures/fig_crucible_assembly.png``.

Usage::

    python paper/build_crucible_assembly_figure.py

Requires matplotlib + Pillow (PyMuPDF optional).
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
CROP_DIR = os.path.join(SRC_DIR, "assembly-crops")
PDF = os.path.join(SRC_DIR, "Induction-Furnace-images-with-callouts.pdf")
FIGURES = os.path.join(REPO_ROOT, "paper", "figures")

DPI = 300  # HardwareX requires >=300 dpi raster figures.

# (0-based PDF page, crop stem, page-fraction crop box) for the photo (with its
# orange call-out labels) on each of the three assembly-sequence slides. The
# boxes are set just outside each embedded photo so the overlaid labels/arrows
# are captured but the white caption margin is excluded.
CROPS = [
    (8, "step1_sample_on_alumina", (0.015, 0.015, 0.545, 0.985)),
    (9, "step2_lid_on", (0.005, 0.100, 0.555, 0.890)),
    (10, "step3_sapphire_window", (0.005, 0.035, 0.525, 0.885)),
]

# Panel definitions: (crop stem, label, title, caption beneath the photo).
PANELS = [
    ("step1_sample_on_alumina", "(a)", "Load specimen",
     "Specimen placed on an alumina sheet in the crucible body,\n"
     "then covered with a second alumina sheet."),
    ("step2_lid_on", "(b)", "Cap with lid",
     "The graphite lid is placed on top of the\nalumina/specimen stack."),
    ("step3_sapphire_window", "(c)", "Seat sapphire window",
     "The sapphire window is placed on the lid so the\n"
     "pyrometer can sight the specimen temperature."),
]


def _regenerate_crops_from_pdf() -> bool:
    """Re-render the assembly-step crops from the committed source PDF.

    Returns True on success, False if PyMuPDF is unavailable or the PDF is
    missing (in which case the committed crops are used as-is).
    """
    try:
        import fitz  # PyMuPDF
    except Exception:
        return False
    if not os.path.exists(PDF):
        return False
    os.makedirs(CROP_DIR, exist_ok=True)
    doc = fitz.open(PDF)
    for page_idx, stem, (x0, y0, x1, y1) in CROPS:
        page = doc[page_idx]
        w, h = page.rect.width, page.rect.height
        clip = fitz.Rect(x0 * w, y0 * h, x1 * w, y1 * h)
        pix = page.get_pixmap(dpi=150, clip=clip)
        pix.save(os.path.join(CROP_DIR, f"{stem}.png"))
    doc.close()
    return True


def _pad_to_canvas(img: Image.Image, aspect: float = 1.0) -> Image.Image:
    """Letterbox ``img`` (preserving its own aspect) onto a uniform white canvas.

    Uniform panel sizes keep the three steps the same height so the row reads as
    a clean left-to-right sequence.
    """
    img = img.convert("RGB")
    w, h = img.size
    cw = int(max(w, h * aspect) * 1.04)
    ch = int(round(cw / aspect))
    canvas = Image.new("RGB", (cw, ch), "white")
    canvas.paste(img, ((cw - w) // 2, (ch - h) // 2))
    return canvas


def main() -> int:
    if _regenerate_crops_from_pdf():
        print("regenerated assembly crops from source PDF")
    else:
        print("PyMuPDF/PDF unavailable; using committed crops")

    images = []
    for stem, label, title, caption in PANELS:
        path = os.path.join(CROP_DIR, f"{stem}.png")
        if not os.path.exists(path):
            print(f"ERROR: missing crop {path}", file=sys.stderr)
            return 1
        images.append((_pad_to_canvas(Image.open(path)), label, title, caption))

    fig, axes = plt.subplots(1, 3, figsize=(9.0, 3.7))
    for ax, (img, label, title, caption) in zip(axes, images):
        ax.imshow(img)
        ax.axis("off")
        ax.set_title(f"{label} {title}", fontsize=9.5, fontweight="bold", pad=4)
        ax.text(0.5, -0.04, caption, transform=ax.transAxes, fontsize=7.6,
                color="#222222", ha="center", va="top", linespacing=1.25)

    fig.subplots_adjust(left=0.01, right=0.99, top=0.93, bottom=0.14,
                        wspace=0.06)
    os.makedirs(FIGURES, exist_ok=True)
    out = os.path.join(FIGURES, "fig_crucible_assembly.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight", pad_inches=0.03)
    plt.close(fig)
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
