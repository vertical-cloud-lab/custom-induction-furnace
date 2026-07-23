# Edison spot-check of the AI-edit review

Edison Scientific ANALYSIS task `86c61cd1-4bc8-4cbe-9a32-c493f4433563`
(submitted 2026-07-23, completed successfully). It independently verified the
43-finding AI-edit review (`ai_edit_review_findings.md`), hunted for defects
the review missed, and critiqued `../ai_edit_review_prompt.md`.

## Contents

- `edison_spotcheck_report.md` — Edison's full report (Tasks 1–3).
- `edison_task_response.json` — full task response for provenance.
- `submit_query.py` / `fetch_results.py` — submission and retrieval scripts.
- `ai_edit_review_findings.md`, `real_person_paper_text.txt`, `SI_text.txt` —
  the uploaded inputs (findings report and pdftotext extractions).
- `artifacts/` — all trajectory artifacts: the agent's analysis notebook
  (`*.ipynb`), its memory log (`*.jsonl`), the page renders it made of both
  PDFs (`page_*.png`), and the figure crops it inspected (`step007_*.png`).

Two trajectory artifacts are **not** committed here: the agent downloaded the
compiled PDFs itself from the public GitHub raw URLs, and those downloads are
byte-identical to the files already in this repository at the reviewed state —
`real_person_paper.pdf` (md5 `b01d721315b1016c5b6440d0ec3b6f2a`, repo root)
and `SI.pdf` (md5 `5e9dbcbffd287b4ec57a40be85c879fe`, `paper/SI.pdf`).
Because the agent had the real PDFs, the figure-dependent checks in the
report were performed on the actual compiled figures, not just the text
extractions.

## Why the PDFs were not uploaded directly (status as of 2026-07-23)

The officially documented upload path
(<https://docs.edisonscientific.com/edison-client/file-management#upload>) is
`store_file_content(name=..., file_path=..., description=...)` with the
returned ids passed as `data_entry:{id}` in
`runtime_config.environment_config.data_storage_uris`. That is what
`submit_query.py` does. However, in `edison-client` 0.16.1 binary files are
routed through the platform's multipart-upload endpoint
(`/v0.1/data-storage/data-entries/{id}/multipart-upload/initiate`), which
currently fails **server-side**: the initiate call constructs a Google Cloud
Storage URL with no bucket in the path
(`https://storage.googleapis.com/<name>%20-%20<uuid>?uploads`), so GCS
returns 400 and the platform surfaces a 500. Reproduced three consecutive
times on 2026-07-23 for an 8 MB PDF; `client.upload_file()` is a thin wrapper
over the same code path, so it fails identically. Text-type files are sent as
JSON text content through a different path and upload fine — hence the
text-extraction fallback plus public PDF URLs in the query, which the agent
used successfully. Retry binary uploads once the platform fixes the multipart
initiate; nothing on the client side needs to change.
