# Edison manuscript review (2026-07-24)

Fresh full review of the current manuscript + SI (commit `aa23a90`) by an
Edison Scientific ANALYSIS task, applying `paper/ai_edit_review_prompt.md`
as the review instrument. Requested by R. Guymon on PR #12.

- Task id: `e68a88da-6e7a-4089-bcbc-232768394d2b` (see `edison_task_id.txt`)
- `submit_query.py` — submission script (text-upload pattern from
  `paper/review_spotcheck_query/`, since binary uploads still 500
  server-side). Uploads: the review prompt, pdftotext extractions of both
  compiled PDFs, and the two prior reports (findings + spot-check) for
  NEW/STILL-OPEN labeling only.
- `poll_until_done.py` — foreground-blocking poller (per CLAUDE.md, no
  background polling on Actions runners). The task took ~22 min.
- `edison_review_report.md` — the task's answer (a summary; the full
  report was delivered as a trajectory artifact).
- `edison_review_full_report.md` — the full 40-finding report (copy of
  `artifacts/fresh_full_manuscript_review.md`): 8 NEW findings, 32
  STILL-OPEN, a confirmed-fixed list, and the completeness note.
- `edison_task_response.json` — full task response for provenance
  (fetched with `history=False`; the `history=True` payload repeatedly
  failed with read timeouts / truncated JSON server-side).
- `artifacts/` — all trajectory artifacts: the agent's notebook, memory
  log, figure crops it rendered while checking captions, and the full
  report. The agent's downloaded copies of `main_pdf.pdf` / `si_pdf.pdf`
  were md5-verified byte-identical to the repo's `real_person_paper.pdf`
  (b1b41130502c05253c035ce306b7ac53) and `paper/SI.pdf`
  (5e9dbcbffd287b4ec57a40be85c879fe) at `aa23a90` and are therefore not
  duplicated here.
