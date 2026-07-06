# Manuscript workspace (Review of Scientific Instruments)

Working materials for a
[Review of Scientific Instruments](https://pubs.aip.org/aip/rsi) (AIP Publishing)
article describing the custom induction furnace — the retrofit of a bare RF
induction generator into a computer-controlled, vacuum-integrated annealing
system. The manuscript was originally drafted for HardwareX and was retargeted
to RSI on 2026-07-02 (the better venue fit; see the PR #3 discussion) — the
HardwareX version is archived in [`archive/`](archive/).

## Contents

| Path | Purpose |
|------|---------|
| [`paper.tex`](paper.tex) / [`paper.pdf`](paper.pdf) | The RSI manuscript draft (LaTeX, REVTeX 4.2 with the `aip,rsi` options) and its compiled PDF. Build with `make pdf` (pdflatex / MiKTeX). |
| [`template/rsi/`](template/rsi/) | Mirrored REVTeX 4.2 / AIP template files (incl. the `rsi` substyle) and the official author instructions — see the [RSI guide summary](template/rsi/RSI_GUIDE_FOR_AUTHORS.md). |
| [`archive/`](archive/) | The archived HardwareX version of the manuscript (Elsevier `elsarticle` class); [`template/`](template/) retains the `elsarticle` files it builds against, plus the [HardwareX Guide for Authors summary](template/HARDWAREX_GUIDE_FOR_AUTHORS.md). |
| [`paper.md`](paper.md) | Migration note — the manuscript moved from Markdown to LaTeX; kept as a pointer. |
| [`Makefile`](Makefile) | Builds `paper.pdf` from `paper.tex`. |
| [`PLAN.md`](PLAN.md) | The manuscript plan: the RSI migration plan (top), contribution framing, section-by-section mapping to the repository files that feed the manuscript, and a pre-submission gap checklist. |
| [`run_edison_review.py`](run_edison_review.py) | Submits the draft + context to an Edison Scientific Analysis review job and saves the feedback. |
| [`edison-feedback/`](edison-feedback/) | Reviewer feedback on the draft (and the analysis notebook) returned by the Edison Analysis job. |
| [`extract_context.py`](extract_context.py) | Reproducible utility that extracts text and embedded figures from the binary documents in [`../docs/`](../docs/) into `extracted-context/`. |
| [`extracted-context/`](extracted-context/) | Machine-readable text extracted from `.pptx`/`.docx`/`.xlsx` source documents (SOP, parts list, schematics, coil corrections). The binaries in `docs/` remain the source of record. |
| [`extracted-context/figures/`](extracted-context/figures/) | Candidate manuscript figures (hardware photos, coil geometry) pulled from the embedded media in the PowerPoint files. |
| [`build_validation_figures.py`](build_validation_figures.py) | Builds the validation figures + metrics (`figures/fig_calibration.png`, etc.; `validation-metrics.json`) from the per-run CSV traces. |
| [`build_characterization_crossref.py`](build_characterization_crossref.py) | Correlates the committed SEM/EBSD/optical data (`../docs/SEM/`, `../docs/optical/`) with the archived runs by specimen ID, writes the cross-reference (`characterization-crossref.csv`/`.md`), and renders the EBSD and multi-scale microstructure figures (`figures/fig_ebsd.png`, `figures/fig_microstructure.png`). |
| [`characterization-crossref.csv`](characterization-crossref.csv) / [`.md`](characterization-crossref.md) | Per-specimen SEM/EBSD/optical ↔ furnace-run cross-reference. |
| [`build_photo_figures.py`](build_photo_figures.py) | Renders the assembled-furnace photo, the vacuum/gas-handling detail panel, and the YSZ high-temperature configuration figure (`figures/fig_furnace_photo.png`, `fig_vacuum_details.png`, `fig_ysz.png`) from the committed photos in `../docs/furnace-photos/`, `../docs/YSZ/`, and `../docs/optical/`. |
| [`build_data_inventory.py`](build_data_inventory.py) | Generates [`journal-assessment/DATA_INVENTORY.md`](journal-assessment/) — a summary of the ~100 logged anneal runs (materials, soak T/time, file types) from `../docs/data_log/`. |
| [`assess_traditional_journal.py`](assess_traditional_journal.py) | Side endeavour: asks an Edison Analysis job whether the **existing data (no new experiments)** supports a traditional journal paper — which journals, likely reviewer feedback, and which editors to contact. |
| [`journal-assessment/`](journal-assessment/) | The data inventory and the Edison traditional-journal feasibility report (`assessment.md`). |

## Regenerating the extracted context

```bash
pip install python-pptx python-docx openpyxl Pillow
python paper/extract_context.py
```

The script is idempotent — it overwrites the generated files under
`extracted-context/`.

## Regenerating the figures

```bash
pip install matplotlib numpy Pillow openpyxl
make figures   # runs build_validation_figures.py + build_characterization_crossref.py
```

## Next steps

See the gap checklist in [`PLAN.md`](PLAN.md#4-gap-checklist-before-submission)
for the remaining work needed before the manuscript can be drafted and submitted.
