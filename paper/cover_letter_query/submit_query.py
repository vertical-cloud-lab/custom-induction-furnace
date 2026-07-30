"""Submit an Edison Scientific ANALYSIS task: feedback on the RSI cover
letter draft, focused on flow, conciseness, tone, and readability.

Uses the known-working text-only upload pattern (see
paper/review_spotcheck_query/submit_query.py for why binary uploads are
avoided): text files go up via store_file_content, and the returned storage
ids are passed as data_entry:{id} in
runtime_config.environment_config.data_storage_uris (that dict must contain
ONLY data_storage_uris).

Run from paper/cover_letter_query/:  python3 submit_query.py
Writes the created task id to edison_task_id.txt.
"""
import os

from edison_client import EdisonClient, JobNames
from edison_client.models import RuntimeConfig, TaskRequest

FILES = [
    (
        "cover_letter_draft.md",
        "../cover_letter_draft.md",
        "Draft cover letter for a Review of Scientific Instruments (AIP) "
        "regular contributed article submission. The text between the '---' "
        "rule and 'Sincerely,' block is the letter itself; bracketed items "
        "are placeholders the authors will fill in.",
    ),
    (
        "real_person_paper_text.txt",
        "real_person_paper_text.txt",
        "pdftotext -layout extraction of the compiled manuscript the cover "
        "letter accompanies (8 pages): a computer-controlled, "
        "vacuum-and-gas-integrated RF induction annealing furnace retrofit, "
        "validated with nickel and YSZ grain growth. Text only; figures "
        "absent. Use it to check the letter's claims and emphasis against "
        "the manuscript.",
    ),
]

QUERY = """\
We are about to submit a manuscript to Review of Scientific Instruments (AIP)
and need editorial feedback on the uploaded cover letter draft
(cover_letter_draft.md). The manuscript it accompanies is uploaded as a text
extraction (real_person_paper_text.txt) so you can check the letter against
it.

Context on the letter's structure, which is a deliberate choice by the
corresponding author: the letter leads with the two headline results (no-prep
EBSD on annealed nickel, and YSZ grain coarsening in 45 min at 2500 C vs
228 h in a box furnace) immediately after the opening submission sentence,
before describing the instrument. Keep that ordering; do not suggest moving
the results later.

Please give feedback on, in priority order:

1. Flow - does each paragraph lead into the next? Are there abrupt jumps,
   buried topic sentences, or sentences doing double duty awkwardly?
2. Conciseness - identify every sentence or phrase that can be cut or
   shortened without losing content. Quote it verbatim and give the tighter
   replacement. Flag anything superfluous (throat-clearing, restatement,
   empty intensifiers).
3. Tone - is it appropriately confident without overselling, and does it
   read like a letter from working scientists to an editor rather than
   marketing copy? Quote anything that overshoots or undershoots.
4. Readability and jargon - flag any term a busy editor (not necessarily a
   specialist in induction heating or EBSD) would stumble on, and any
   sentence that needs two reads. Suggest plainer wording. Note: the authors
   explicitly want jargon and superfluous language removed.

Also check, briefly:
5. Accuracy - does every claim in the letter match the manuscript text
   (numbers, materials, capabilities)? Flag any mismatch or any claim
   stated more strongly in the letter than in the manuscript.
6. Conventions - anything unusual versus standard practice for AIP/RSI cover
   letters (length, required statements, things editors expect that are
   missing, things present that are unnecessary).

Output format:
- Section A: a numbered list of specific findings, each with the verbatim
  quote, the problem, and a concrete replacement (or "cut").
- Section B: a complete revised version of the letter body (Dear Editor
  through the closing paragraph) with all your suggestions applied, keeping
  the results-first ordering and all bracketed placeholders exactly as they
  are.
- Section C: two or three sentences on overall assessment - is it ready
  after these edits?

Be specific and quote verbatim; do not pad the report.
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
