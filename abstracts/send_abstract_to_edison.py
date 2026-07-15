#!/usr/bin/env python3
"""Send the TMS 2027 abstract draft to an Edison Scientific Analysis job for feedback.

Bundles the abstract draft (``tms2027-fullwood-symposium.md``), the compiled
manuscript it distills (``real_person_paper.pdf`` from PR #3), and the TMS 2027
call-for-abstracts flyer, then submits a ``JobNames.ANALYSIS`` job chained (via
``continued_job_id``) to the last manuscript review round so the reviewer has
the full manuscript-history context.

Usage::

    pip install edison-client
    python abstracts/send_abstract_to_edison.py [--paper-pdf PATH] [--no-chain]

The API key is read from ``EDISON_PLATFORM_API_KEY`` (falling back to
``EDISON_API_KEY``). Output is written to ``abstracts/edison-feedback.md`` and
the task id to ``abstracts/edison_task_id.txt``.
"""
from __future__ import annotations

import argparse
import os
import shutil
import time
import urllib.request
from pathlib import Path
from uuid import UUID

from edison_client import EdisonClient, JobNames, TaskRequest
from edison_client.models.app import RuntimeConfig

HERE = Path(__file__).resolve().parent

# Last Edison manuscript-review round on PR #3 (paper/edison-feedback/last_task_id.txt).
PREVIOUS_TASK_ID = "d6b87bcc-813a-45e6-8405-f05dc7a72398"

FLYER_URL = "https://www.tms.org/tms2027/downloads/flyers/TMS2027-CFA-Flyer-086.pdf"

QUERY = """You previously reviewed (over four chained rounds) a manuscript about a custom,
generator-agnostic vacuum induction annealing furnace (LabVIEW/DAQ power control,
ratio-pyrometer feedback, high-vacuum quartz chamber, machined graphite susceptor),
now drafted for Review of Scientific Instruments (attached as real_person_paper.pdf).

NEW TASK: the team wants to present this work at TMS 2027 (156th Annual Meeting,
March 14-18, 2027, Orlando) in the symposium "Microstructure-Sensitive Design and
Advanced Characterization: An MPMD/SMD Symposium Honoring David T. Fullwood"
(call-for-abstracts flyer attached). The draft title and 150-word abstract are in
tms2027-fullwood-symposium.md.

Please give concise, prioritized feedback on the conference abstract ONLY:
1. Fit: does the title/abstract speak to this symposium's scope (microstructure-
   sensitive design, EBSD/HR-EBSD advanced characterization, honoring David T.
   Fullwood's legacy)? How could the framing better match the audience?
2. Accuracy: is every claim in the abstract supported by the attached manuscript?
   Flag anything overstated or understated.
3. Impact: is the title compelling for a TMS talk? Offer 2-3 alternative titles.
4. Mechanics: the abstract must stay at or under 150 words; suggest tightened
   wording if any recommended addition would exceed that.
5. Any red flags for a TMS technical-program reviewer.

Return a clear, well-structured markdown report with a suggested revised title and
revised <=150-word abstract."""


def build_bundle(dest: Path, paper_pdf: Path | None) -> Path:
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    shutil.copy(HERE / "tms2027-fullwood-symposium.md", dest)
    if paper_pdf and paper_pdf.exists():
        shutil.copy(paper_pdf, dest / "real_person_paper.pdf")
    try:
        req = urllib.request.Request(FLYER_URL, headers={"User-Agent": "Mozilla/5.0"})
        (dest / "TMS2027-CFA-Flyer-086.pdf").write_bytes(
            urllib.request.urlopen(req, timeout=60).read())
    except Exception as exc:  # noqa: BLE001 - flyer is nice-to-have context
        print("flyer download failed (continuing without it):", exc, flush=True)
    return dest


def extract_answer(dump: dict) -> str | None:
    ef = dump.get("environment_frame") or {}
    try:
        ans = ef.get("state", {}).get("state", {}).get("answer")
        if ans:
            return ans
    except AttributeError:
        pass
    return dump.get("answer") or dump.get("formatted_answer")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--paper-pdf", type=Path, default=None,
                    help="Path to real_person_paper.pdf (from the PR #3 branch).")
    ap.add_argument("--no-chain", action="store_true",
                    help="Do not chain to the previous manuscript-review task.")
    ap.add_argument("--poll-minutes", type=int, default=20,
                    help="How long to wait for the result before exiting (task id "
                         "is saved either way).")
    args = ap.parse_args()

    api_key = os.environ.get("EDISON_PLATFORM_API_KEY") or os.environ.get("EDISON_API_KEY")
    if not api_key:
        raise SystemExit("Set EDISON_PLATFORM_API_KEY (or EDISON_API_KEY).")

    client = EdisonClient(api_key=api_key)
    bundle = build_bundle(Path("/tmp/edison_abstract_bundle"), args.paper_pdf)

    resp = client.store_file_content(
        name="induction_furnace_tms2027_abstract_bundle",
        file_path=bundle,
        as_collection=True,
        description="TMS 2027 abstract draft + RSI manuscript + CFA flyer",
    )
    uri = f"data_entry:{resp.data_storage.id}"
    print("uploaded:", uri, flush=True)

    runtime_config = None
    if not args.no_chain:
        runtime_config = RuntimeConfig(continued_job_id=UUID(PREVIOUS_TASK_ID))

    task_id = str(client.create_task(
        TaskRequest(name=JobNames.ANALYSIS, query=QUERY, runtime_config=runtime_config),
        files=[uri],
    ))
    print("task:", task_id, flush=True)
    (HERE / "edison_task_id.txt").write_text(task_id + "\n")

    deadline = time.time() + 60 * args.poll_minutes
    status = ""
    while time.time() < deadline:
        status = str(getattr(client.get_task(task_id), "status", "")).lower()
        print("status:", status, flush=True)
        if any(k in status for k in ("success", "fail", "cancel", "complete", "truncat")):
            break
        time.sleep(60)

    dump = client.get_task(task_id).model_dump()
    answer = extract_answer(dump)
    if answer:
        header = f"<!-- Edison ANALYSIS task {task_id} (TMS 2027 abstract review) -->\n\n"
        (HERE / "edison-feedback.md").write_text(header + answer)
        print("wrote edison-feedback.md", len(answer), "chars", flush=True)
    else:
        print("no answer yet; retrieve later with task id", task_id, flush=True)


if __name__ == "__main__":
    main()
