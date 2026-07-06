#!/usr/bin/env python3
"""Build the grain-boundary thermal-grooving figure (fig_grooving.png).

The source micrographs are edge-on SEM views of specimen Ni4N5_053 recorded on
2020-03-05 (the same microscope session as the committed
``docs/SEM/200305_Ni4N5_033,053_sharpie_grooving/Ni4N5_053_grooves`` files,
verified against the FEI databar timestamps), after the IFrun059 anneal
(1200 C / 12 h) with no metallographic preparation. They are archived as
embedded media in ``docs/student-work/W2020_Sprint6.pptx`` (slides 8 and 10)
and are extracted directly from the deck here so the figure regenerates
reproducibly.

Usage::

    python3 paper/build_grooving_figure.py
"""
from __future__ import annotations

import io
import zipfile
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
PPTX = ROOT / "docs" / "student-work" / "W2020_Sprint6.pptx"
FIG_DIR = Path(__file__).resolve().parent / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

# Slide-8 media inside the deck: (media path, panel title). All are 3072x2188
# FEI exports with the databar (scale bar, mag, date) preserved.
PANELS = [
    ("ppt/media/image8.tif", "(a) Edge view, 350x"),
    ("ppt/media/image7.tif", "(b) Edge view, 800x"),
    ("ppt/media/image9.tif", "(c) Grooved boundary, 12,000x"),
]


def main() -> None:
    fig, axes = plt.subplots(1, 3, figsize=(7.5, 2.35))
    with zipfile.ZipFile(PPTX) as zf:
        for ax, (media, title) in zip(axes, PANELS):
            im = Image.open(io.BytesIO(zf.read(media)))
            ax.imshow(np.asarray(im.convert("L")), cmap="gray")
            ax.set_title(title, fontsize=9)
            ax.set_xticks([])
            ax.set_yticks([])
    fig.tight_layout()
    out = FIG_DIR / "fig_grooving.png"
    fig.savefig(out, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
