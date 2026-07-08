#!/usr/bin/env python3
"""Extract the manuscript's real data figures from the lab's uploaded records.

Requested by R. Guymon (PR #3, 2026-07-08): the manuscript must not carry
self-generated data figures — it uses the actual graphs/datasets uploaded by
the lab, verbatim. This script only *extracts or copies* those records; it
draws nothing.

Outputs (into ``paper/figures/``):

* ``fig_grain_growth.png`` — the as-recorded optical micrograph of the YSZ
  specimen after the first successful 2500 degC / 45 min tantalum-susceptor
  anneal (grain growth 20 um -> 90 um), extracted verbatim from page 14 of
  ``Grain Growth Summary.pdf`` (repo root, uploaded by S. Baird). The red
  measurement traces and the 100 um scale bar are part of the original
  microscope record.

* ``fig_kikuchi_raw.jpg`` — the clearest of the saved raw electron-backscatter
  (Kikuchi) patterns, copied byte-for-byte from
  ``docs/SEM/200616_Ni4N5_007,081_Ni_003b2/Ni4N5_007/boxscan_003a1b_0degRot/``
  (specimen ``Ni_003a1b``; the detector's 8x8-binned 115x115 px output, saved
  by OIM Data Collection during mapping — see
  ``docs/SEM/raw-kikuchi-patterns/README.md`` for provenance).

Usage::

    python3 paper/extract_uploaded_figures.py

Requires PyMuPDF (``pip install pymupdf``) for the PDF extraction.
"""
from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FIG_DIR = Path(__file__).resolve().parent / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

GRAIN_GROWTH_PDF = ROOT / "Grain Growth Summary.pdf"
# Page 14 (0-indexed 13): "2500C For 45 min ... Grain Growth: 20um - 90um".
GRAIN_GROWTH_PAGE = 13

KIKUCHI_SRC = (
    ROOT
    / "docs/SEM/200616_Ni4N5_007,081_Ni_003b2/Ni4N5_007"
    / "boxscan_003a1b_0degRot/boxscan_003a1b_0degRot_x255y268.jpg"
)


def extract_grain_growth_micrograph() -> None:
    import fitz  # PyMuPDF

    doc = fitz.open(GRAIN_GROWTH_PDF)
    page = doc[GRAIN_GROWTH_PAGE]
    images = page.get_images(full=True)
    assert len(images) == 1, f"expected 1 image on p{GRAIN_GROWTH_PAGE + 1}"
    info = doc.extract_image(images[0][0])
    out = FIG_DIR / "fig_grain_growth.png"
    assert info["ext"] == "png", info["ext"]
    out.write_bytes(info["image"])
    print(f"extracted {out} ({info['width']}x{info['height']}) "
          f"from '{GRAIN_GROWTH_PDF.name}' p{GRAIN_GROWTH_PAGE + 1}")


def copy_raw_kikuchi_pattern() -> None:
    out = FIG_DIR / "fig_kikuchi_raw.jpg"
    shutil.copyfile(KIKUCHI_SRC, out)
    print(f"copied {out} verbatim from {KIKUCHI_SRC.relative_to(ROOT)}")


if __name__ == "__main__":
    extract_grain_growth_micrograph()
    copy_raw_kikuchi_pattern()
