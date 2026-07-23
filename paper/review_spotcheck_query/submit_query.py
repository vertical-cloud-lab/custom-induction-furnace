"""Submit an Edison Scientific ANALYSIS task: spot-check the AI-edit review
of the manuscript + SI, and give feedback on the review prompt itself.

File-passing pattern (differs from paper/title_survey/submit_edison_task.py
out of necessity): binary uploads via store_file_content route through the
platform's multipart-upload endpoint, which currently 500s server-side (the
initiate call builds a malformed storage URL with no bucket; reproduced 3x on
2026-07-23 for both PDFs). Text-type files (.md/.txt) upload fine via the
text-content path. First attempt (task 72fcebdc...) passed the two PDFs as
store_link entries in data_storage_uris; the task failed instantly with no
failure_reason, matching the known signature of unsupported environment
config, so link entries evidently cannot be used there. This version uploads
only text files (pdftotext extractions of both PDFs, the findings report, and
the prompt) and puts the public PDF URLs in the query text as an optional
download for the agent. All storage ids go into
runtime_config.environment_config.data_storage_uris, which must contain ONLY
data_storage_uris.

Run from paper/review_spotcheck_query/:  python3 submit_query.py
Writes the created task id to edison_task_id.txt.
"""
import os

from edison_client import EdisonClient, JobNames
from edison_client.models import RuntimeConfig, TaskRequest

COMMIT = "c149c59"
RAW = f"https://github.com/vertical-cloud-lab/custom-induction-furnace/raw/{COMMIT}"

PAPER_URL = f"{RAW}/real_person_paper.pdf"
SI_URL = f"{RAW}/paper/SI.pdf"

FILES = [
    (
        "ai_edit_review_prompt.md",
        "../ai_edit_review_prompt.md",
        "The adversarial copy-editing review prompt that was used to produce "
        "the findings report. We want feedback on this prompt itself.",
    ),
    (
        "ai_edit_review_findings.md",
        "ai_edit_review_findings.md",
        "The 43-finding review report produced by running the prompt against "
        "the manuscript and SI LaTeX sources. To be spot-checked against the "
        "two PDFs.",
    ),
    (
        "real_person_paper_text.txt",
        "real_person_paper_text.txt",
        "pdftotext -layout extraction of the compiled manuscript "
        "real_person_paper.pdf (8 pages, Review of Scientific Instruments "
        "submission on a computer-controlled vacuum RF induction annealing "
        "furnace retrofit). Text only; figures absent.",
    ),
    (
        "SI_text.txt",
        "SI_text.txt",
        "pdftotext -layout extraction of the compiled supplementary "
        "information SI.pdf (13 pages): crucible dimensions, coil drawing, "
        "calibration/repeatability/long-soak traces, Kikuchi-pattern survey, "
        "YSZ extension, specimen-run linkage table (Table S1), bill of "
        "materials (Table S2), design-file inventory. Text only; figures "
        "absent.",
    ),
]

QUERY = f"""\
We are finalizing a manuscript for Review of Scientific Instruments (AIP). An
AI reviewing pass was run over the LaTeX sources using the uploaded prompt
(ai_edit_review_prompt.md) and produced the uploaded findings report
(ai_edit_review_findings.md, 43 findings). The manuscript and supplementary
information are provided as pdftotext extractions of the compiled PDFs
(real_person_paper_text.txt = main text, 8 pages; SI_text.txt = supplementary
information, 13 pages). If your environment has internet access, you may also
download the compiled PDFs themselves (public GitHub raw URLs, no auth,
follow redirects): main text {PAPER_URL} and SI {SI_URL} - the PDFs include
the figures, which the text extractions lack. If you cannot download them,
work from the text extractions and mark figure-dependent checks as not
checkable.

Please act as an independent spot check of that review. Note: line numbers in
the findings report refer to the LaTeX sources you do not have; locate each
finding by its verbatim quotes instead.

Task 1 - Verify the findings. For each of the 43 findings (prioritize the
referee-flag items No. 1-11, 20, 21), classify it as: CONFIRMED (the quoted
text and the claimed contradiction/defect are really present in the
documents), NOT CONFIRMED (the quote is absent, misquoted, or the claimed
defect does not hold), OVERSTATED/MISJUDGED (present but the severity or
interpretation is wrong), or NOT CHECKABLE (say what would be needed). Where you
can bring domain knowledge (e.g., NI USB-6000 / NI-9265 / NI-9203 device
specifications, 4-20 mA current loops, Al2O3-C chemistry, EBSD practice,
pyrometry), use it and say what you relied on.

Task 2 - Find what the review missed. Independently sweep both documents for
the same defect classes the prompt targets (garbled sentences, internal numeric
contradictions, claimed-vs-demonstrated gaps, terminology drift, broken or
vague cross-references, physically implausible statements, figure captions
that do not match what the figure shows). Report any defect NOT already in the
findings report, with verbatim quotes and locations (page numbers). This is
the most valuable output: the review is being used as the basis for final
edits, so misses matter more than confirmations.

Task 3 - Critique the prompt. Give concrete feedback on ai_edit_review_prompt.md
as a reusable instrument for catching AI-introduced defects in scientific
manuscripts: (a) what it does well; (b) blind spots - defect classes it does
not ask for, revealed by anything you found in Task 2 or by your own
experience; (c) instructions that are ambiguous, redundant, or likely to cause
false positives; (d) whether the embedded few-shot examples help or overfit it
to this one paper; (e) 3-6 specific, wording-level suggested edits to the
prompt (give the replacement text).

Output format: three sections matching the tasks. In Task 1, a compact table
of finding number -> verdict -> one-line justification, followed by longer
notes only for verdicts other than CONFIRMED. In Task 2, one entry per missed
defect with quote, page, and why it matters. Please be specific and quote
verbatim throughout; do not paraphrase quotes.
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
