#!/usr/bin/env python3
"""Ask an Edison Scientific Analysis job whether the *existing* induction-furnace
data (no new experiments) supports a traditional peer-reviewed journal contribution,
and if so which journals, the likely reviewer feedback, and which editors to contact.

This is the "side endeavour" companion to ``run_edison_review.py`` (which reviews the
HardwareX hardware paper). It bundles the manuscript, the data inventory, the
extracted context, and the available microstructure characterization (SEM student
report) and submits a single ``JobNames.ANALYSIS`` job.

Usage::

    pip install edison-client
    python paper/build_data_inventory.py        # refresh DATA_INVENTORY.md first
    python paper/assess_traditional_journal.py

The API key is read from ``EDISON_PLATFORM_API_KEY`` (falling back to ``EDISON_API_KEY``).
Output is written to ``paper/journal-assessment/``.
"""
from __future__ import annotations

import json
import os
import shutil
import time
from pathlib import Path

from edison_client import EdisonClient, JobNames, TaskRequest

HERE = Path(__file__).resolve().parent
OUT = HERE / "journal-assessment"

QUERY = """You are a senior materials-science / physical-metallurgy advisor who also
serves as a journal editor. The attached collection describes a custom vacuum
induction annealing furnace (a HardwareX hardware manuscript: paper.tex / paper.pdf)
together with the COMPLETE existing experimental record from years of use:

- DATA_INVENTORY.md: ~100 logged anneal runs (IFrun001-100), mostly Ni200 and Ni4N5
  (a 99.95% Ni-base alloy) plus some Pd thermal-evaporation and YSZ/crucible runs.
  Soak temperatures span ~900-1400 C and soak times from minutes to ~40 h, each with
  pyrometer temperature-vs-time traces (.xlsx/.txt/.lvm/.tdms).
- extracted-context/*.md: the SOP, parts list, schematics, and coil-geometry context.
- RyanWeber.pdf: a student characterization report that contains microstructure
  (SEM / optical / grain-size) results on annealed samples from this furnace.
- The lab also has SEM and optical micrograph image sets (well-labeled by sample ID)
  that can be correlated with the run logs, but NO NEW EXPERIMENTS will be collected.

Critically assess, assuming **no additional experiments are run** (only analysis of
already-collected data is allowed):

1. **Is there enough for a traditional (non-HardwareX) peer-reviewed contribution?**
   Give a clear yes / qualified-yes / no with the reasoning. State the strongest
   defensible scientific thesis the existing data can support (e.g. grain-growth
   kinetics of Ni/Ni4N5 vs. temperature and time; an Arrhenius/grain-growth-exponent
   analysis; reproducibility of vacuum-induction annealing), and exactly which
   existing data/figures would carry it.

2. **If yes, which journals?** Rank concrete candidate journals (with their scope and
   why they fit), distinguishing (a) full research papers, (b) short/technical notes
   or "method"/measurement journals, and (c) data-descriptor journals. Consider that
   the dataset is observational/retrospective and may lack designed replicates.

3. **What would the paper actually claim and show?** Propose a title, a 3-5 figure
   plan built ONLY from existing data, and the key quantitative analyses (with the
   statistical caveats of using retrospective, non-DOE data).

4. **Likely reviewer feedback / major concerns**, and how to preempt each one
   (e.g. emissivity/pyrometer calibration, missing replicates, single-operator data,
   grain-size measurement methodology, lack of as-received baselines, vacuum-level
   documentation).

5. **Which editors to reach out to in advance** and how: the type of handling/
   associate editor to target (research area), what a good pre-submission inquiry
   email should contain, and whether a registered report / data descriptor route is
   preferable.

Be concrete and decision-oriented. Return a well-structured markdown report.
"""


def build_bundle(dest: Path) -> Path:
    if dest.exists():
        shutil.rmtree(dest)
    (dest / "extracted-context").mkdir(parents=True)
    for name in ("paper.tex", "paper.pdf", "PLAN.md"):
        src = HERE / name
        if src.exists():
            shutil.copy(src, dest / name)
    inv = OUT / "DATA_INVENTORY.md"
    if inv.exists():
        shutil.copy(inv, dest / "DATA_INVENTORY.md")
    for md in (HERE / "extracted-context").glob("*.md"):
        shutil.copy(md, dest / "extracted-context" / md.name)
    sem = HERE.parent / "docs" / "student-work" / "RyanWeber.pdf"
    if sem.exists():
        shutil.copy(sem, dest / "RyanWeber_microstructure_report.pdf")
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
    api_key = os.environ.get("EDISON_PLATFORM_API_KEY") or os.environ.get("EDISON_API_KEY")
    if not api_key:
        raise SystemExit("Set EDISON_PLATFORM_API_KEY (or EDISON_API_KEY).")

    OUT.mkdir(parents=True, exist_ok=True)
    client = EdisonClient(api_key=api_key)
    bundle = build_bundle(Path("/tmp/edison_journal_bundle"))

    resp = client.store_file_content(
        name="induction_furnace_journal_assessment_bundle",
        file_path=bundle,
        as_collection=True,
        description="Induction furnace manuscript + full data inventory + microstructure report",
    )
    uri = f"data_entry:{resp.data_storage.id}"
    print("uploaded:", uri, flush=True)

    task_id = str(client.create_task(
        TaskRequest(name=JobNames.ANALYSIS, query=QUERY),
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
        header = f"<!-- Edison ANALYSIS task {task_id} (traditional-journal assessment) -->\n\n"
        (OUT / "assessment.md").write_text(header + answer)
        print("wrote assessment.md", len(answer), "chars", flush=True)
    nb = dump.get("notebook")
    if nb:
        with (OUT / "assessment.ipynb").open("w") as fh:
            json.dump(nb, fh, indent=1)
        print("wrote assessment.ipynb", flush=True)
    (OUT / "last_task_id.txt").write_text(task_id + "\n")


if __name__ == "__main__":
    main()
