#!/usr/bin/env python3
"""Compose the graphite crucible component-dimensions figure.

Ronnie Guymon contributed a slide deck (``docs/graphite-crucible/
Induction-Furnace-images-with-callouts.pdf``) that photographs every individual
piece of the two-piece graphite crucible/susceptor stack and annotates each with
colour-coded diameter call-outs. Several slides carry *two* photographs of the
same view --- one with the measurement lines drawn on, one clean --- and this
builder deliberately uses the *dimensioned* copy so the reader sees where each
number was taken.

The seven dimensioned crops are committed under
``docs/graphite-crucible/callout-crops/`` (rendered from the source PDF). If
PyMuPDF (``fitz``) is installed the crops are regenerated from the committed PDF
so the figure is fully reproducible from source; otherwise the committed crops
are used directly (so ``make figures`` works without PyMuPDF).

Output: ``paper/figures/fig_crucible_dimensions.png`` --- a labelled seven-panel
figure with each part's diameters printed beneath it, colour-matched to the
call-out lines in the photograph.

Usage::

    python paper/build_crucible_dimensions_figure.py

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
CROP_DIR = os.path.join(SRC_DIR, "callout-crops")
PDF = os.path.join(SRC_DIR, "Induction-Furnace-images-with-callouts.pdf")
FIGURES = os.path.join(REPO_ROOT, "paper", "figures")

DPI = 300  # HardwareX requires >=300 dpi raster figures.

# Call-out colours copied from the source slides so the printed measurements
# colour-match the lines drawn on each photograph.
TEAL = "#0097a6"
ORANGE = "#ff9a3d"
YELLOW = "#c9a800"  # darkened from the slide yellow so it reads on white
RED = "#e00000"
GREEN = "#12b012"
GREY = "#404040"

# (0-based PDF page, crop filename stem, page-fraction crop box) for the
# dimensioned photo on each measurement slide.
CROPS = [
    (0, "01_alumina", (0.02, 0.16, 0.49, 0.71)),
    (1, "02_sapphire", (0.15, 0.12, 0.42, 0.67)),
    (2, "03_body_top", (0.0, 0.15, 0.45, 0.75)),
    (3, "04_body_bottom", (0.03, 0.16, 0.59, 0.78)),
    (4, "05_lid_oblique", (0.01, 0.21, 0.41, 0.80)),
    (5, "06_lid_top", (0.50, 0.0, 0.91, 1.0)),
    (6, "07_lid_bottom", (0.0, 0.12, 0.37, 0.66)),
]

# Panel definitions: (crop stem, label, title, [(text, colour), ...] measurements).
PANELS = [
    ("01_alumina", "(a)", "Alumina disc",
     [("14 mm dia.", GREY)]),
    ("02_sapphire", "(b)", "Sapphire window",
     [("9.5 mm dia.", GREY)]),
    ("03_body_top", "(c)", "Crucible body, top",
     [("inner 14.55 mm", TEAL), ("outer 20.30 mm", ORANGE)]),
    ("04_body_bottom", "(d)", "Crucible body, bottom",
     [("20.30 mm dia.", GREY)]),
    ("05_lid_oblique", "(e)", "Crucible lid, oblique",
     [("upper 13.70 mm", TEAL), ("lower 14.55 mm", ORANGE)]),
    ("06_lid_top", "(f)", "Crucible lid, top",
     [("outer 13.70 mm", YELLOW), ("2nd 9.75 mm", TEAL),
      ("3rd 5 mm", RED), ("bore 3.5 mm", GREEN)]),
    ("07_lid_bottom", "(g)", "Crucible lid, bottom",
     [("outer 14.55 mm", GREEN), ("bore 3.5 mm", ORANGE)]),
]


def _regenerate_crops_from_pdf() -> bool:
    """Re-render the dimensioned crops from the committed source PDF.

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


def _pad_to_canvas(img: Image.Image, aspect: float = 1.4) -> Image.Image:
    """Letterbox ``img`` (preserving its own aspect) onto a uniform white canvas.

    Uniform panel sizes keep the grid tidy and the measurement captions aligned
    regardless of whether a given photo is portrait or landscape.
    """
    img = img.convert("RGB")
    w, h = img.size
    # Canvas sized so the image fits with margin, aspect = width/height.
    cw = int(max(w, h * aspect) * 1.06)
    ch = int(round(cw / aspect))
    canvas = Image.new("RGB", (cw, ch), "white")
    canvas.paste(img, ((cw - w) // 2, (ch - h) // 2))
    return canvas


def main() -> int:
    if _regenerate_crops_from_pdf():
        print("regenerated call-out crops from source PDF")
    else:
        print("PyMuPDF/PDF unavailable; using committed crops")

    images = []
    for stem, label, title, meas in PANELS:
        path = os.path.join(CROP_DIR, f"{stem}.png")
        if not os.path.exists(path):
            print(f"ERROR: missing crop {path}", file=sys.stderr)
            return 1
        images.append((_pad_to_canvas(Image.open(path)), label, title, meas))

    # 7 panels on a 4-wide x 2-tall grid; the last cell is left blank.
    ncols, nrows = 4, 2
    fig, axes = plt.subplots(nrows, ncols, figsize=(9.0, 5.6))
    flat = axes.ravel()

    for ax, (img, label, title, meas) in zip(flat, images):
        ax.imshow(img)
        ax.axis("off")
        ax.set_title(f"{label} {title}", fontsize=8.5, fontweight="bold", pad=3)
        # Colour-matched measurement tokens beneath the photo (two per line).
        if len(meas) == 1:
            ax.text(0.5, -0.05, meas[0][0], transform=ax.transAxes,
                    fontsize=8.0, color=meas[0][1], ha="center", va="top")
        else:
            positions = [(0.27, -0.05), (0.73, -0.05),
                         (0.27, -0.17), (0.73, -0.17)]
            for (t, c), (x, y) in zip(meas, positions):
                ax.text(x, y, t, transform=ax.transAxes, fontsize=7.5,
                        color=c, ha="center", va="top")

    # Hide any unused cells (the 8th).
    for ax in flat[len(images):]:
        ax.axis("off")

    fig.subplots_adjust(left=0.01, right=0.99, top=0.95, bottom=0.02,
                        wspace=0.05, hspace=0.45)
    os.makedirs(FIGURES, exist_ok=True)
    out = os.path.join(FIGURES, "fig_crucible_dimensions.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight", pad_inches=0.03)
    plt.close(fig)
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
