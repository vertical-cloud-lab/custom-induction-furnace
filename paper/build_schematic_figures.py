#!/usr/bin/env python3
"""Render the real hardware schematics/photos used as manuscript figures.

The system-overview schematics live as editable PowerPoint drawings in ``docs/``
(native shapes, not embedded raster), and the LabVIEW control front panel is a
committed screenshot. This script renders the schematic slides to high-resolution
PNG via LibreOffice and stages the front-panel screenshot, writing canonical
``fig_*.png`` files into ``paper/figures/`` so the manuscript uses *actual* figures
rather than placeholders.

Usage::

    sudo apt-get install -y libreoffice-impress poppler-utils   # soffice + pdftoppm
    python paper/build_schematic_figures.py

Re-running is idempotent. If LibreOffice is unavailable the schematic renders are
skipped (with a warning) and any previously committed PNGs are kept.
"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(REPO_ROOT, "docs")
FIGURES = os.path.join(REPO_ROOT, "paper", "figures")

DPI = "300"  # HardwareX requires >=300 dpi raster figures.

# (source .pptx relative to docs/, slide page number, output figure name).
SCHEMATIC_RENDERS = [
    ("induction-furnace-schematic.pptx", 1, "fig_system_overview.png"),
    ("schematic.pptx", 1, "fig_system_overview_alt.png"),
]

# Committed raster screenshots copied verbatim (source relative to docs/, output).
PHOTO_COPIES = [
    ("equipment-reference/frontPanel_200219.PNG", "fig_control_panel.png"),
]


def _have(cmd: str) -> bool:
    return shutil.which(cmd) is not None


def render_schematics() -> None:
    if not (_have("soffice") and _have("pdftoppm")):
        print("WARNING: soffice/pdftoppm not found; skipping schematic renders "
              "(install libreoffice-impress + poppler-utils to regenerate).",
              file=sys.stderr)
        return
    for src, page, out_name in SCHEMATIC_RENDERS:
        src_path = os.path.join(DOCS, src)
        if not os.path.exists(src_path):
            print(f"WARNING: missing {src_path}; skipping", file=sys.stderr)
            continue
        with tempfile.TemporaryDirectory() as tmp:
            subprocess.run(
                ["soffice", "--headless", "--convert-to", "pdf",
                 "--outdir", tmp, src_path],
                check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            )
            pdf = os.path.join(tmp, os.path.splitext(src)[0] + ".pdf")
            prefix = os.path.join(tmp, "page")
            subprocess.run(
                ["pdftoppm", "-png", "-r", DPI, "-f", str(page), "-l", str(page),
                 pdf, prefix],
                check=True,
            )
            # pdftoppm names files like page-1.png / page-01.png depending on count.
            rendered = next(
                (os.path.join(tmp, f) for f in sorted(os.listdir(tmp))
                 if f.startswith("page") and f.endswith(".png")),
                None,
            )
            if rendered is None:
                print(f"WARNING: render produced no PNG for {src}", file=sys.stderr)
                continue
            shutil.copyfile(rendered, os.path.join(FIGURES, out_name))
            print(f"wrote figures/{out_name}  (from docs/{src} slide {page})")


def copy_photos() -> None:
    for src, out_name in PHOTO_COPIES:
        src_path = os.path.join(DOCS, src)
        if not os.path.exists(src_path):
            print(f"WARNING: missing {src_path}; skipping", file=sys.stderr)
            continue
        shutil.copyfile(src_path, os.path.join(FIGURES, out_name))
        print(f"wrote figures/{out_name}  (from docs/{src})")


def main() -> None:
    os.makedirs(FIGURES, exist_ok=True)
    render_schematics()
    copy_photos()


if __name__ == "__main__":
    main()
