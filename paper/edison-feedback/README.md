# Edison Scientific feedback on the HardwareX draft

This folder holds the feedback returned by an [Edison Scientific](https://www.edisonscientific.com/)
**Analysis** job that reviewed the HardwareX manuscript draft against the journal's
requirements.

| | |
|---|---|
| Job type | `JobNames.ANALYSIS` (`job-futurehouse-data-analysis-crow-high`) |
| Task ID | `e7eacd4f-739c-4cb3-a6f8-e9b6a5b9130f` |
| Uploaded bundle | `paper.md`, `paper.pdf`, `PLAN.md`, all `extracted-context/` text + candidate figures, the East Coast Induction heater notes, and the code README |
| Status | success |

## Files

- [`feedback.md`](feedback.md) — the reviewer report (completeness vs. HardwareX
  sections, framing, BOM, validation/SEM+EBSD, and an ordered pre-submission checklist).
- [`analysis.ipynb`](analysis.ipynb) — the analysis notebook produced by the job
  (kept for provenance).

## Highest-priority actions extracted from the feedback

1. Fill BOM gaps for the **CEIA Power Cube generator + Master Controller v3+**, the
   recirculating chiller, and the exact **NI DAQ** model (with currency + year).
2. Merge the BOM into a **single 7-column table** with grouped designators
   (GEN-/RETRO-/CONS-). *(applied in `paper.md`)*
3. Add the mandatory **"Source file repository (DOI)"** specifications row and an
   **Ethics statements** section. *(applied in `paper.md`)*
4. Declare an **OSHWA-approved hardware license** (e.g. CERN-OHL-S) and an OSI-approved
   **software license** (e.g. MIT); mint a permanent DOI (Zenodo) — GitHub URLs are not
   accepted as the primary file location.
5. **Export the LabVIEW `.vi` block diagrams to PDF/PNG** and add a 2D/3D drawing of the
   machined graphite crucible to the design files.
6. Generate the validation figures: power→temperature calibration, open- vs. closed-loop
   stability (via `plotheatcurve.m`), and **SEM micrographs + EBSD grain-size histograms**
   (as-received vs. annealed), plus a photo of the assembled system. Prefer the CAD-render
   coil figures over informal workshop photos.

These items are reflected in the gap checklist in [`../PLAN.md`](../PLAN.md).

## Reproducing

```bash
pip install edison-client
python paper/run_edison_review.py   # re-uploads paper/ context and submits a new job
```
