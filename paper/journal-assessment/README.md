# Traditional-journal feasibility assessment

Can the induction-furnace project yield a contribution in a **traditional
(non-HardwareX) journal with no additional experiments**? This folder holds the
data inventory and an Edison Scientific Analysis review that answers that question.

## Files

| File | Purpose |
|------|---------|
| [`DATA_INVENTORY.md`](DATA_INVENTORY.md) | Auto-generated summary of the existing data (~100 anneal runs; materials, soak T/time, file types) — produced by [`../build_data_inventory.py`](../build_data_inventory.py). |
| [`assessment.md`](assessment.md) | Edison Analysis report: feasibility verdict, candidate journals, figure/claim plan, likely reviewer concerns, and editor-outreach guidance. |
| [`assessment.ipynb`](assessment.ipynb) | The analysis notebook returned by the Edison job. |
| [`last_task_id.txt`](last_task_id.txt) | The Edison task id (for chaining a follow-up). |

## Bottom line (from `assessment.md`)

**Qualified yes.** The existing record supports a peer-reviewed paper framed as a
**retrospective study of thermal-history reproducibility and microstructural
outcomes** in a custom vacuum induction annealing furnace — *not* a definitive
grain-growth-kinetics study (the archive is broad but unbalanced, mostly single
runs per condition, with replicate-rich cells at Ni4N5 1200 °C/12 h (n=9) and
1300 °C/20 h (n=4)).

- **Highest-odds targets (no new experiments):** *Review of Scientific Instruments*,
  *Measurement Science and Technology*, *Journal of Materials Engineering and
  Performance*; then *Metallography, Microstructure, and Analysis* / *Journal of
  Materials Science*. **Fallback / companion:** *Data in Brief*.
- **A full kinetics paper** is only defensible if the archived SEM/optical
  micrographs can be cleanly linked to run IDs, measured with one consistent
  grain-size method, and have as-received baselines.
- **Top reviewer concerns to preempt:** retrospective (non-DOE) design,
  pyrometer/emissivity calibration, specimen↔run provenance, missing baselines,
  grain-size methodology, hardware drift over years, per-run vacuum logging.
- **Editors:** target handling/associate editors in high-temperature
  instrumentation / pyrometry (for RSI/MST) or heat-treatment / process metallurgy
  / grain growth (for the metallurgy journals); a short pre-submission inquiry email
  skeleton is included. A **registered report is not appropriate** (retrospective
  data); a **data descriptor** is a good fallback.

## Reproduce

```bash
pip install edison-client
python paper/build_data_inventory.py        # refresh DATA_INVENTORY.md
python paper/assess_traditional_journal.py  # re-run the Edison assessment
```
