#!/usr/bin/env python3
"""Build fig_microstructure.png: the optical grain map of Ni4N5_081 after its
1300 C / 20 h anneal (run IFrun081-100 series; see SI Table S1).

Per S. Baird (PR #12, 2026-07-22) the figure is the optical panel only (the
SEM grain-boundary detail panel was removed), cropped to the bottom-right
quadrant of the source micrograph so the overlapping yellow grain-size
measurement text is excluded. The microscope's 200 um scale-bar box is cut
from the source's bottom-left corner and pasted onto the crop at native pixel
scale --- the crop is never resampled, so the calibration still holds.

Source: docs/optical/CB121/2005##_Ni200_Ni4N5/200506_Ni4N5_081/
im_sclbr_measure_1.jpg (2048x1536).

Usage::

    python3 paper/build_microstructure_figure.py
"""
from __future__ import annotations

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SRC = (ROOT / "docs" / "optical" / "CB121" / "2005##_Ni200_Ni4N5"
       / "200506_Ni4N5_081" / "im_sclbr_measure_1.jpg")
OUT = Path(__file__).resolve().parent / "figures" / "fig_microstructure.png"

# Bottom-right quadrant of the 2048x1536 source; the yellow measurement
# overlay ends near (1010, 806), so the quadrant is overlay-free.
CROP = (1024, 768, 2048, 1536)
# The microscope's scale-bar box (black background, "200.0 um" text + bar)
# in the source's bottom-left corner.
SCALEBAR = (10, 1408, 240, 1530)
MARGIN = 12  # inset of the pasted scale-bar box from the crop's corner


def main() -> None:
    im = Image.open(SRC).convert("RGB")
    scalebar = im.crop(SCALEBAR)
    out = im.crop(CROP)
    out.paste(scalebar, (MARGIN, out.height - scalebar.height - MARGIN))
    out.save(OUT)
    print(f"wrote {OUT} ({out.width}x{out.height})")


if __name__ == "__main__":
    main()
