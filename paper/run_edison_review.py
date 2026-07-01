#!/usr/bin/env python3
"""Submit the HardwareX draft + supporting context to an Edison Scientific Analysis job
and save the returned feedback.

Bundles the manuscript draft (``paper.tex``/``paper.pdf``), the plan, and the extracted
context, uploads them as a single collection, runs a ``JobNames.ANALYSIS`` review job,
and writes the feedback to ``paper/edison-feedback/``.

The script supports an iterative review loop: each invocation writes a numbered
``feedback-<N>.md`` (and updates ``feedback.md`` to the latest), so successive
review → implement → re-review cycles are preserved as version-controlled history.
Pass ``--continued-job-id`` with the previous task's UUID to chain the follow-up query
so the reviewer is aware of the prior round's context.

Usage::

    pip install edison-client
    python paper/run_edison_review.py                       # one review round
    python paper/run_edison_review.py --continued-job-id <uuid>  # follow-up round

The API key is read from ``EDISON_PLATFORM_API_KEY`` (falling back to ``EDISON_API_KEY``).
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import time
from pathlib import Path
from uuid import UUID

from edison_client import EdisonClient, JobNames, TaskRequest
from edison_client.models.app import RuntimeConfig

HERE = Path(__file__).resolve().parent
OUT = HERE / "edison-feedback"

QUERY = """You are reviewing a draft manuscript for the journal HardwareX (open-source
scientific hardware). The attached collection contains the draft manuscript (paper.tex and
the compiled paper.pdf), a detailed plan (PLAN.md), and supporting extracted context (SOP,
parts list, schematics, coil geometry corrections, candidate figures, and hardware notes).

The hardware is a retrofit that turns a commercial RF induction generator into a
computer-controlled (LabVIEW/DAQ analog power setpoint), vacuum-integrated, pyrometer-
feedback annealing system for reactive-metal grain growth, using an in-house machined
graphite crucible/susceptor. The reproducible build is anchored on the lab's current
USA-sourced generator (CEIA Power Cube 6 kW via East Coast Induction); a ~1970 LEPEL
furnace was the prototype.

Give thorough, actionable feedback to finish this HardwareX submission:
1. Completeness/quality vs. HardwareX's required sections (specifications table, hardware
   in context, hardware description, design files, bill of materials, build, operation,
   validation & characterization, safety, declarations). Identify missing/weak sections.
2. Is the retrofit/modernization framing and generator-agnostic reproducibility argument
   convincing? How to strengthen it?
3. Is the bill of materials reproducible (it has [TODO] price/source items)? What is
   essential to fill in?
4. Validation: plan is power->temperature calibration, ramp/soak profiles, and real SEM +
   EBSD microstructure/grain-size results. What analyses, figures, and controls make this
   publishable?
5. Highest-priority gaps and an ordered pre-submission checklist, plus any HardwareX policy
   requirements (license, design-file formats, DOI) not yet satisfied.

Return the feedback as a clear, well-structured markdown report."""


def build_bundle(dest: Path) -> Path:
    if dest.exists():
        shutil.rmtree(dest)
    (dest / "extracted-context" / "figures").mkdir(parents=True)
    for name in ("paper.tex", "paper.pdf", "paper.md", "PLAN.md"):
        src = HERE / name
        if src.exists():
            shutil.copy(src, dest / name)
    ec = HERE / "extracted-context"
    for md in ec.glob("*.md"):
        shutil.copy(md, dest / "extracted-context" / md.name)
    for img in (ec / "figures").glob("*"):
        if img.suffix.lower() in (".png", ".jpg", ".jpeg"):
            shutil.copy(img, dest / "extracted-context" / "figures" / img.name)
    notes = HERE.parent / "docs" / "east-coast-induction" / "heater-notes.txt"
    if notes.exists():
        shutil.copy(notes, dest / "east-coast-induction-heater-notes.txt")
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


def next_iteration(out: Path) -> int:
    existing = sorted(int(p.stem.split("-")[1]) for p in out.glob("feedback-*.md")
                      if p.stem.split("-")[1].isdigit())
    return (existing[-1] + 1) if existing else 1


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--continued-job-id", default=None,
                    help="UUID of the previous Edison task to chain this review onto.")
    ap.add_argument("--iteration", type=int, default=None,
                    help="Override the iteration number (defaults to auto-increment).")
    args = ap.parse_args()

    api_key = os.environ.get("EDISON_PLATFORM_API_KEY") or os.environ.get("EDISON_API_KEY")
    if not api_key:
        raise SystemExit("Set EDISON_PLATFORM_API_KEY (or EDISON_API_KEY).")

    OUT.mkdir(parents=True, exist_ok=True)
    iteration = args.iteration if args.iteration is not None else next_iteration(OUT)
    print("iteration:", iteration, flush=True)

    client = EdisonClient(api_key=api_key)
    bundle = build_bundle(Path("/tmp/edison_bundle"))

    resp = client.store_file_content(
        name="induction_furnace_hardwarex_bundle",
        file_path=bundle,
        as_collection=True,
        description="HardwareX induction furnace manuscript draft + supporting context",
    )
    uri = f"data_entry:{resp.data_storage.id}"
    print("uploaded:", uri, flush=True)

    runtime_config = None
    query = QUERY
    if args.continued_job_id:
        runtime_config = RuntimeConfig(continued_job_id=UUID(args.continued_job_id))
        query = (QUERY + "\n\nThis is a FOLLOW-UP review round. The draft has been revised "
                 "to address your previous feedback (single 7-column BOM, ethics section, "
                 "graphite susceptor framing, analog-input requirement, references, etc.). "
                 "Focus on (a) verifying the previous issues are resolved, (b) any NEW "
                 "weaknesses introduced, and (c) the next most important changes to reach "
                 "submission quality. Be concise and prioritized; avoid repeating advice "
                 "already implemented.")

    task_id = str(client.create_task(
        TaskRequest(name=JobNames.ANALYSIS, query=query, runtime_config=runtime_config),
        files=[uri],
    ))
    print("task:", task_id, flush=True)

    deadline = time.time() + 60 * 60
    while time.time() < deadline:
        status = str(getattr(client.get_task(task_id), "status", "")).lower()
        print("status:", status, flush=True)
        if any(k in status for k in ("success", "fail", "cancel", "complete", "truncat")):
            break
        time.sleep(60)

    dump = client.get_task(task_id).model_dump()
    answer = extract_answer(dump)
    if answer:
        header = f"<!-- Edison ANALYSIS task {task_id} (iteration {iteration}) -->\n\n"
        (OUT / f"feedback-{iteration}.md").write_text(header + answer)
        (OUT / "feedback.md").write_text(header + answer)
        print("wrote feedback-%d.md" % iteration, len(answer), "chars", flush=True)
    nb = dump.get("notebook")
    if nb:
        with (OUT / "analysis.ipynb").open("w") as fh:
            json.dump(nb, fh, indent=1)
        print("wrote analysis.ipynb", flush=True)
    # Record the task id so follow-up rounds can chain via --continued-job-id.
    (OUT / "last_task_id.txt").write_text(task_id + "\n")


if __name__ == "__main__":
    main()
