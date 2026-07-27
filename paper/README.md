# Manuscript workspace (Review of Scientific Instruments)

Working materials for a
[Review of Scientific Instruments](https://pubs.aip.org/aip/rsi) (AIP Publishing)
article describing the custom induction furnace — the retrofit of a bare RF
induction generator into a computer-controlled, vacuum-integrated annealing
system. The manuscript was originally drafted for HardwareX and was retargeted
to RSI on 2026-07-02 (see the PR #3 discussion).

This branch carries only the files needed to edit and build the submitted
manuscript and its supplementary material. The full drafting workspace —
`paper.tex`, the HardwareX `archive/`, `PLAN.md`, the `supplementary/*.md`
sources, the extraction utilities, and the remaining `build_*.py` figure
scripts (with the large source decks and raw data they read) — lives on
PR #3's branch (`copilot/vertical-cloud-labattempt-download-docs`). Figures
whose build scripts are not on this branch are committed as pre-built PNGs
under `figures/`.

## Contents

| Path | Purpose |
|------|---------|
| [`real_person_paper.tex`](real_person_paper.tex) | The RSI manuscript (LaTeX, REVTeX 4.2 with the `aip,rsi` options). Build with `make real`; the deliverable PDF is copied to the repository root. |
| [`SI.tex`](SI.tex) / [`SI.pdf`](SI.pdf) | The supplementary material — a single separate PDF named `SI.pdf` per the AIP author instructions, with S-numbered figures/tables and alt text under each caption. Build with `make si`. |
| [`references.bib`](references.bib) | Bibliography for the manuscript. |
| [`template/rsi/`](template/rsi/) | Mirrored REVTeX 4.2 / AIP template files (incl. the `rsi` substyle) and the official author instructions — see the [RSI guide summary](template/rsi/RSI_GUIDE_FOR_AUTHORS.md). |
| [`figures/`](figures/) | Manuscript and SI figures. Regenerable ones are rebuilt by the scripts below; the rest are pre-built on PR #3's branch. |
| [`build_power_figures_volts.py`](build_power_figures_volts.py) | Rebuilds `fig_calibration.png` and `fig_representative.png` from the per-run CSV traces in [`../docs/data_log/processed/csv/`](../docs/data_log/processed/csv/), with the power command in volts on the DAQ's 0–5 V scale. |
| [`build_crucible_combined_figure.py`](build_crucible_combined_figure.py) | Composes `fig_crucible_combined.png` from the crucible photos in `../docs/graphite-crucible/`. |
| [`build_crucible_dimensions_figure.py`](build_crucible_dimensions_figure.py) | Composes the SI's `fig_crucible_dimensions.png` from the dimensioned crops in `../docs/graphite-crucible/callout-crops/` (bare panel letters; descriptions live in the SI caption). |
| [`build_ebsd_figure.py`](build_ebsd_figure.py) | Composes `fig_ebsd.png` from the committed EBSD maps in `../docs/SEM/`. |
| [`build_microstructure_figure.py`](build_microstructure_figure.py) | Crops `fig_microstructure.png` from the committed optical micrograph in `../docs/optical/`. |
| [`build_grooving_figure.py`](build_grooving_figure.py) | Rebuilds `fig_grooving.png` — requires `../docs/student-work/W2020_Sprint6.pptx` and SEM images that exist only on PR #3's branch. |
| [`make_ysz_stack_schematic.py`](make_ysz_stack_schematic.py) | Regenerates `../docs/ysz-stack-schematic.pptx` and renders `fig_ysz_stack.png` (requires LibreOffice). |
| [`add_chamber_stand_schematic.py`](add_chamber_stand_schematic.py) | Adds the vacuum-chamber support stand to `../docs/induction-furnace-schematic-v2.pptx` and renders `fig_system_overview_v2.png` (requires LibreOffice). |
| [`kikuchi_indexing/`](kikuchi_indexing/) | Open-source (PyEBSDIndex) indexing of the nine committed raw Kikuchi patterns. |
| [`ai_edit_review_prompt.md`](ai_edit_review_prompt.md) | Reusable adversarial review prompt for catching AI-introduced defects. |
| [`ysz_survey_table_draft.tex`](ysz_survey_table_draft.tex) | Draft of the YSZ extreme-temperature configuration-survey table (not yet inserted into the SI). |
| `*_query/`, [`title_survey/`](title_survey/) | Edison Scientific task submissions, reports, and trajectory artifacts (EBSD no-prep mechanism, YSZ references, title survey, manuscript reviews). |
| [`Makefile`](Makefile) | Builds `real_person_paper.pdf` and `SI.pdf`; `make figures` regenerates the figures whose inputs are on this branch. |

## Building

```bash
make real   # real_person_paper.pdf (pdflatex + bibtex, REVTeX 4.2)
make si     # SI.pdf
```

## Regenerating the figures

```bash
pip install matplotlib numpy Pillow
make figures   # only the figures whose inputs are committed on this branch
```
