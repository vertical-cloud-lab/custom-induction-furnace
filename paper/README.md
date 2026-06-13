# HardwareX manuscript workspace

Working materials for a [HardwareX](https://www.sciencedirect.com/journal/hardwarex)
article describing the custom induction furnace — the retrofit of a ~1970 LEPEL
high-frequency induction furnace into a computer-controlled, vacuum-integrated
annealing system.

## Contents

| Path | Purpose |
|------|---------|
| [`PLAN.md`](PLAN.md) | The manuscript plan: contribution framing, draft specifications table, every required HardwareX section mapped to the repository files that feed it, and a pre-submission gap checklist. |
| [`extract_context.py`](extract_context.py) | Reproducible utility that extracts text and embedded figures from the binary documents in [`../docs/`](../docs/) into `extracted-context/`. |
| [`extracted-context/`](extracted-context/) | Machine-readable text extracted from `.pptx`/`.docx`/`.xlsx` source documents (SOP, parts list, schematics, coil corrections). The binaries in `docs/` remain the source of record. |
| [`extracted-context/figures/`](extracted-context/figures/) | Candidate manuscript figures (hardware photos, coil geometry) pulled from the embedded media in the PowerPoint files. |

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
