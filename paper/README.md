# HardwareX manuscript workspace

Working materials for a [HardwareX](https://www.sciencedirect.com/journal/hardwarex)
article describing the custom induction furnace — the retrofit of a ~1970 LEPEL
high-frequency induction furnace into a computer-controlled, vacuum-integrated
annealing system.

## Contents

| Path | Purpose |
|------|---------|
| [`paper.tex`](paper.tex) / [`paper.pdf`](paper.pdf) | The HardwareX manuscript draft (LaTeX, Elsevier `elsarticle` class) and its compiled PDF. Build with `make pdf` (pdflatex / MiKTeX). |
| [`template/`](template/) | Mirrored Elsevier `elsarticle` class/template files and a summary of the [HardwareX Guide for Authors](template/HARDWAREX_GUIDE_FOR_AUTHORS.md). |
| [`paper.md`](paper.md) | Migration note — the manuscript moved from Markdown to LaTeX; kept as a pointer. |
| [`Makefile`](Makefile) | Builds `paper.pdf` from `paper.tex`. |
| [`PLAN.md`](PLAN.md) | The manuscript plan: contribution framing, draft specifications table, every required HardwareX section mapped to the repository files that feed it, and a pre-submission gap checklist. |
| [`run_edison_review.py`](run_edison_review.py) | Submits the draft + context to an Edison Scientific Analysis review job and saves the feedback. |
| [`edison-feedback/`](edison-feedback/) | Reviewer feedback on the draft (and the analysis notebook) returned by the Edison Analysis job. |
| [`extract_context.py`](extract_context.py) | Reproducible utility that extracts text and embedded figures from the binary documents in [`../docs/`](../docs/) into `extracted-context/`. |
| [`extracted-context/`](extracted-context/) | Machine-readable text extracted from `.pptx`/`.docx`/`.xlsx` source documents (SOP, parts list, schematics, coil corrections). The binaries in `docs/` remain the source of record. |
| [`extracted-context/figures/`](extracted-context/figures/) | Candidate manuscript figures (hardware photos, coil geometry) pulled from the embedded media in the PowerPoint files. |
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

## Next steps

See the gap checklist in [`PLAN.md`](PLAN.md#4-gap-checklist-before-submission)
for the remaining work needed before the manuscript can be drafted and submitted.
