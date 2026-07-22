#!/usr/bin/env python3
"""Ask an Edison Scientific Analysis job for *specific, actionable* suggestions on
how to incorporate the existing furnace data and empirical results into the
HardwareX manuscript.

This bundles the current manuscript (``paper.tex`` + the recompiled ``paper.pdf``),
the reproducible per-run data products (``run_summary.csv`` + a representative set
of per-run temperature/power plots), the data inventory, the extracted binary
context, the validated master bibliography, and the previous Edison analysis
results about the data (the traditional-journal assessment), and submits a single
``JobNames.ANALYSIS`` job. When a prior analysis task id is available
(``journal-assessment/last_task_id.txt``) the job is chained via
``continued_job_id`` so the reviewer builds on the earlier data assessment.

Usage::

    pip install edison-client
    python paper/edison_data_incorporation.py

The API key is read from ``EDISON_PLATFORM_API_KEY`` (falling back to
``EDISON_API_KEY``). Output is written to ``paper/edison-feedback/``.
"""
from __future__ import annotations

import json
import os
import shutil
import time
from pathlib import Path
from uuid import UUID

from edison_client import EdisonClient, JobNames, TaskRequest

try:
    from edison_client.models.app import RuntimeConfig
except Exception:  # pragma: no cover - older clients
    RuntimeConfig = None

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
OUT = HERE / "edison-feedback"
JA = HERE / "journal-assessment"

# Representative runs spanning materials, soak temperatures, and durations.
REPRESENTATIVE_RUNS = [
    "IFrun039_Ni4N5_026_1200C_6h",
    "IFrun040_Ni4N5_027_1250C_6h",
    "IFrun049_Ni4N5_034_1200C_12h",
    "IFrun072_Ni4N5_079,080_1400C_12h",
    "IFrun079_Ni4N5_084_1300C_12h",
    "IFrun080_Ni200_017_1325C_40h",
    "IFrun081_Ni200_015_1325C_20h",
    "IFrun038_Ni4N5_025_1300C_1h",
    "IFrun032_Ni4N5_022_1400C_10min",
]

QUERY = """You are a senior materials-science / instrumentation reviewer helping
finalize a HardwareX hardware paper (paper.tex / paper.pdf) about a custom,
generator-agnostic vacuum induction annealing furnace (LabVIEW/DAQ power control +
ratio-pyrometer feedback + high-vacuum quartz chamber + machined graphite
crucible/susceptor). The lab has YEARS of already-collected empirical data and
wants to fold the strongest, most credible empirical results into the manuscript
WITHOUT running new experiments.

Attached:
- paper.tex / paper.pdf: the current draft (specifications table, hardware
  description, BOM, build, operation, validation plan, safety). The validation
  section currently describes 5 *planned* figures and has TODO placeholders for
  the specimen<->thermal-history linkage table and real micrographs.
- run_summary.csv: machine-parsed summary of ~49 logged anneal runs (peak/soak
  temperature, soak time, duration, point count) derived from the raw .xlsx/.lvm
  logs.
- run-plots/*.png: representative reproducible temperature+power-vs-time plots
  generated from the raw logs (e.g. Ni4N5/Ni200 anneals at 1200-1400 C, soaks of
  minutes to 40 h).
- DATA_INVENTORY.md: the full inventory of ~100 runs + characterization assets.
- extracted-context/*.md: SOP, parts list, schematics, coil geometry.
- references.bib + bibliography-validation.md: the validated master bibliography.
- journal-assessment/assessment.md: the previous Edison analysis of whether this
  data supports a traditional journal paper (for continuity).
- The lab also has large, well-labeled SEM and optical micrograph sets keyed by
  sample ID (Ni4N5_###, Ni200_###) that can be correlated with these runs.

Give CONCRETE, ACTIONABLE guidance, organized by manuscript section, on how to
incorporate the existing data and empirical results:

1. **Validation figures (highest priority).** For each of the 5 planned figures,
   say exactly which existing runs/plots to use and what to compute. Specifically:
   (a) the power-command -> steady-state-temperature calibration: which runs give
   usable steady-state points, and how to honestly report scatter given
   retrospective non-DOE data; (b) a representative ramp/soak with quantitative
   control metrics (rise time, overshoot, settling, soak mean/SD, max deviation) -
   which run(s) and how to compute each from run_summary.csv / the per-run CSVs;
   (c) repeatability across runs - which run groups are genuinely same
   profile/material/geometry (e.g. the 1200 C 12 h Ni4N5 series IFrun052-060) and
   what repeatability statistics to report; (d) long-soak stability (e.g. the 20-40 h
   Ni200 runs); (e) microstructure: how to tie SEM/EBSD/optical images to specific
   run IDs and present grain-size vs. soak T/time using only existing samples.

2. **Specimen <-> thermal-history linkage table.** Propose how to populate the
   currently-empty table (which columns, how to derive soak T/time/atmosphere from
   the filenames + run_summary.csv), and which canonical run IDs to feature.

3. **Honest treatment of limitations** (single operator, retrospective data,
   emissivity/pyrometer calibration, missing as-received baselines, sparse
   replicates) and the exact caveat sentences to add so reviewers trust the data.

4. **Which empirical results strengthen the hardware claims** (reproducibility,
   accuracy, long-term stability, broad material range incl. susceptor-coupled
   YSZ) and where in the text to cite them.

5. **A concrete, ordered to-do list** of the specific data-processing and figure
   steps to go from the current draft to a submission-ready validation section,
   noting which can be done now from the attached data vs. which need the
   SEM/optical image sets pulled and registered to run IDs.

Be specific (name run IDs and numbers). Return a well-structured markdown report.
"""


def build_bundle(dest: Path) -> Path:
    if dest.exists():
        shutil.rmtree(dest)
    (dest / "extracted-context").mkdir(parents=True)
    (dest / "run-plots").mkdir(parents=True)

    for name in ("paper.tex", "paper.pdf", "PLAN.md", "references.bib"):
        src = HERE / name
        if src.exists():
            shutil.copy(src, dest / name)
    for src in (JA / "DATA_INVENTORY.md", JA / "assessment.md",
                OUT / "bibliography-validation.md"):
        if src.exists():
            shutil.copy(src, dest / src.name)
    for md in (HERE / "extracted-context").glob("*.md"):
        shutil.copy(md, dest / "extracted-context" / md.name)

    processed = REPO / "docs" / "data_log" / "processed"
    summary = processed / "run_summary.csv"
    if summary.exists():
        shutil.copy(summary, dest / "run_summary.csv")
    for run in REPRESENTATIVE_RUNS:
        png = processed / "png" / f"{run}.png"
        if png.exists():
            shutil.copy(png, dest / "run-plots" / png.name)
        csvf = processed / "csv" / f"{run}.csv"
        if csvf.exists():
            shutil.copy(csvf, dest / "run-plots" / csvf.name)
    sem = REPO / "docs" / "student-work" / "RyanWeber.pdf"
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
    api_key = (os.environ.get("EDISON_PLATFORM_API_KEY")
               or os.environ.get("EDISON_API_KEY"))
    if not api_key:
        raise SystemExit("Set EDISON_PLATFORM_API_KEY (or EDISON_API_KEY).")
    api_key = api_key.strip()

    OUT.mkdir(parents=True, exist_ok=True)
    client = EdisonClient(api_key=api_key)
    bundle = build_bundle(Path("/tmp/edison_data_incorporation_bundle"))

    resp = client.store_file_content(
        name="induction_furnace_data_incorporation_bundle",
        file_path=bundle,
        as_collection=True,
        description="Manuscript + reproducible run data/plots + inventory + bibliography",
    )
    uri = f"data_entry:{resp.data_storage.id}"
    print("uploaded:", uri, flush=True)

    runtime_config = None
    prior = JA / "last_task_id.txt"
    if RuntimeConfig is not None and prior.exists():
        try:
            runtime_config = RuntimeConfig(continued_job_id=UUID(prior.read_text().strip()))
            print("chaining from prior task", prior.read_text().strip(), flush=True)
        except Exception as exc:  # noqa: BLE001
            print("could not chain prior task:", exc, flush=True)

    task_kwargs = dict(name=JobNames.ANALYSIS, query=QUERY)
    if runtime_config is not None:
        task_kwargs["runtime_config"] = runtime_config
    task_id = str(client.create_task(TaskRequest(**task_kwargs), files=[uri]))
    print("task:", task_id, flush=True)
    (OUT / "data_incorporation_task_id.txt").write_text(task_id + "\n")

    deadline = time.time() + 60 * 55
    while time.time() < deadline:
        status = str(getattr(client.get_task(task_id), "status", "")).lower()
        print("status:", status, flush=True)
        if any(k in status for k in ("success", "fail", "cancel", "complete", "truncat")):
            break
        time.sleep(60)

    dump = client.get_task(task_id).model_dump()
    answer = extract_answer(dump)
    if answer:
        header = (f"<!-- Edison ANALYSIS task {task_id} "
                  f"(data-incorporation suggestions) -->\n\n")
        (OUT / "data-incorporation-suggestions.md").write_text(header + answer)
        print("wrote data-incorporation-suggestions.md", len(answer), "chars", flush=True)
    else:
        print("NO ANSWER; dump keys:", list(dump.keys()), flush=True)
    nb = dump.get("notebook")
    if nb:
        with (OUT / "data-incorporation-suggestions.ipynb").open("w") as fh:
            json.dump(nb, fh, indent=1)
        print("wrote data-incorporation-suggestions.ipynb", flush=True)


if __name__ == "__main__":
    main()
