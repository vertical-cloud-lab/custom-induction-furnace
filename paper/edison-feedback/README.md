# Edison Scientific feedback on the HardwareX draft

This folder holds the feedback returned by [Edison Scientific](https://www.edisonscientific.com/)
**Analysis** jobs that reviewed the HardwareX manuscript draft against the journal's
requirements. The review is run **iteratively**: each round's feedback is implemented in
`paper.md`, then the revised draft is re-submitted (chained via `continued_job_id`) for the
next round. Numbered `feedback-N.md` files preserve every round; `feedback.md` mirrors the
latest.

## Review rounds

| Round | Task ID | Chained from | Feedback | Status |
|------:|---------|--------------|----------|--------|
| 1 | `e7eacd4f-739c-4cb3-a6f8-e9b6a5b9130f` | — | (folded into earlier commits) | success |
| 2 | `6f4d2804-3c2d-4d53-b3b2-13bb0483bd5a` | — | [`feedback-2.md`](feedback-2.md) | success |
| 3 | `f10579bb-4cbc-45bb-9761-373dbd7754d9` | round 2 | [`feedback-3.md`](feedback-3.md) | success |
| 4 | `d6b87bcc-813a-45e6-8405-f05dc7a72398` | round 3 | [`feedback-4.md`](feedback-4.md) | success |

Each uploaded bundle contains `paper.md`, the compiled `paper.pdf`, `PLAN.md`, all
`extracted-context/` text + candidate figures, and the East Coast Induction heater notes.

## What each round changed

- **Round 2** → single 7-column BOM expanded with part detail/costing conventions;
  reproducibility-boundary, prior-art, generator-compatibility and LEPEL→CEIA migration
  tables; control signal-flow + vacuum-stack detail; operation restructured into
  preflight/startup/run/shutdown/emergency; safety hazard table; validation metrics +
  specimen-linkage table; References section.
- **Round 3** → resolved the DAQ vs. 4–20 mA control-chain inconsistency (explicit
  0–5 V → V→I conditioner → 4–20 mA, new BOM row); unified the canonical pyrometer
  (LumaSense IMPAC ISR 6); fixed BOM arithmetic/SKU errors; softened the cost claim;
  monotonic (not linear) compatibility; defined the open→closed-loop handoff criterion;
  PPE/shielding line.

## Remaining blockers (require lab assets/decisions, not text edits)

1. Fill GEN/DAQ/pump/chiller **pricing** from the East Coast Induction quote and exact models.
2. Declare final **licenses** (proposed CERN-OHL-S hardware / MIT code) and mint a **Zenodo DOI**.
3. Replace the validation **plan with real figures** (calibration, ramp/soak, repeatability,
   SEM + EBSD) and populate the specimen ↔ run-ID table.
4. Add the **graphite crucible machining drawing** and **LabVIEW `.vi` block-diagram exports**.

These items are reflected in the gap checklist in [`../PLAN.md`](../PLAN.md).

## Files

- `feedback-N.md` — each round's reviewer report; `feedback.md` mirrors the latest round.
- [`analysis.ipynb`](analysis.ipynb) — the most recent analysis notebook (kept for provenance).
- `last_task_id.txt` — the latest task id, used to chain the next round.

## Reproducing

```bash
pip install edison-client
python paper/run_edison_review.py                              # new review round
python paper/run_edison_review.py --continued-job-id <task-id> # chained follow-up round
```
