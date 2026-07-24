"""Submit an Edison Scientific ANALYSIS task: a fresh full review of the
current manuscript + SI (commit aa23a90) using paper/ai_edit_review_prompt.md
as the review instrument.

Requested by R. Guymon on PR #12 (2026-07-24): "using the previously-used
Edison analysis, do another review of the manuscript."

File-passing pattern follows paper/review_spotcheck_query/submit_query.py
(the known-working pattern): binary uploads through store_file_content 500
server-side, so only text files are uploaded, and the public GitHub raw URLs
of the compiled PDFs are placed in the query text for the agent to download
itself if its sandbox has internet. All storage ids go into
runtime_config.environment_config.data_storage_uris (only that key).

Run from paper/manuscript_review_query/:  python3 submit_query.py
Writes the created task id to edison_task_id.txt.
"""
import os

from edison_client import EdisonClient, JobNames
from edison_client.models import RuntimeConfig, TaskRequest

COMMIT = "aa23a90"
RAW = f"https://github.com/vertical-cloud-lab/custom-induction-furnace/raw/{COMMIT}"

PAPER_URL = f"{RAW}/real_person_paper.pdf"
SI_URL = f"{RAW}/paper/SI.pdf"

FILES = [
    (
        "ai_edit_review_prompt.md",
        "../ai_edit_review_prompt.md",
        "The adversarial copy-editing review prompt to apply. Follow its "
        "three passes and output format.",
    ),
    (
        "real_person_paper_text.txt",
        "real_person_paper_text.txt",
        "pdftotext -layout extraction of the CURRENT compiled manuscript "
        "real_person_paper.pdf (8 pages, Review of Scientific Instruments "
        "submission on a computer-controlled vacuum RF induction annealing "
        "furnace retrofit), commit aa23a90. Text only; figures absent.",
    ),
    (
        "SI_text.txt",
        "SI_text.txt",
        "pdftotext -layout extraction of the CURRENT compiled supplementary "
        "information SI.pdf (13 pages): crucible dimensions, coil drawing, "
        "calibration/repeatability/long-soak traces, Kikuchi-pattern survey, "
        "YSZ extension, specimen-run linkage table (Table S1), bill of "
        "materials (Table S2), design-file inventory. Text only.",
    ),
    (
        "previous_review_findings.md",
        "../review_spotcheck_query/ai_edit_review_findings.md",
        "The 43-finding review produced by the same prompt against an OLDER "
        "revision (commit c149c59). Many findings have since been fixed. Use "
        "it only to label your findings NEW vs STILL-OPEN; do not assume any "
        "finding still applies without re-verifying against the current text.",
    ),
    (
        "previous_spotcheck_report.md",
        "../review_spotcheck_query/edison_spotcheck_report.md",
        "An earlier Edison spot-check of that 43-finding review, including "
        "nine additional defects it found. Same usage: context for NEW vs "
        "STILL-OPEN labeling only; re-verify everything against current text.",
    ),
]

QUERY = f"""\
We are finalizing a manuscript for Review of Scientific Instruments (AIP).
Since the last review, many edits have been applied by the authors and by AI
editing passes. Please perform a FRESH, full review of the CURRENT documents
by applying the uploaded review prompt (ai_edit_review_prompt.md) - all three
passes, exactly as it instructs - to the current manuscript
(real_person_paper_text.txt, 8 pages) and supplementary information
(SI_text.txt, 13 pages).

If your environment has internet access, also download the compiled PDFs
(public GitHub raw URLs, no auth, follow redirects): main text {PAPER_URL}
and SI {SI_URL} - the PDFs include the figures, which the text extractions
lack, so figure-caption-vs-content checks need them. If you cannot download
them, work from the text extractions and mark figure-dependent checks as not
checkable.

Two adjustments to the prompt's instructions for this run:

1. Locations: you have compiled documents, not LaTeX sources, so give
   locations as page number + section/caption, with verbatim quotes.

2. NEW vs STILL-OPEN labeling: two context files are provided
   (previous_review_findings.md - a 43-finding review of an older revision;
   previous_spotcheck_report.md - a spot-check of that review that added nine
   more defects). After you complete your own independent review, label each
   of your findings as NEW (not in either context file) or STILL-OPEN (a
   previously reported defect that survives, verbatim-verified, in the
   current text). Do NOT let the context files steer your search: several of
   their findings have been fixed, and the spot-check warned that the
   prompt's few-shot examples can overfit a reviewer toward re-finding known
   motifs. Findings you re-verify as fixed need not be listed except in a
   short closing list of confirmed-fixed items.

The authors will use your report for the final editing pass before
submission, so misses matter more than confirmations, and NEW findings are
the most valuable output. Quote verbatim throughout; do not paraphrase
quotes. End with the completeness note the prompt requires (documents swept,
checks not performable and why).
"""


def main():
    client = EdisonClient(api_key=os.environ["EDISON_PLATFORM_API_KEY"])
    uris = []
    for name, path, description in FILES:
        upload = client.store_file_content(
            name=name, file_path=path, description=description
        )
        storage_id = upload.data_storage.id
        uris.append(f"data_entry:{storage_id}")
        print("uploaded", name, "->", storage_id)

    task_data = TaskRequest(
        name=JobNames.ANALYSIS,
        query=QUERY,
        runtime_config=RuntimeConfig(
            environment_config={"data_storage_uris": uris},
        ),
    )
    responses = client.create_task(task_data)
    task_id = responses if isinstance(responses, str) else str(responses)
    with open("edison_task_id.txt", "w") as f:
        f.write(task_id + "\n")
    print("created task:", task_id)


if __name__ == "__main__":
    main()
