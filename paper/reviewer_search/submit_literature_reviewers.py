"""Submit an Edison Scientific LITERATURE task: reviewer suggestions for the
RSI induction-furnace manuscript from the broader literature (not limited to
RSI authors). Companion to submit_analysis_reviewers.py.

Run from paper/reviewer_search/:  python3 submit_literature_reviewers.py
Writes edison_literature_task_id.txt.
"""
import os

from edison_client import EdisonClient, JobNames
from edison_client.models import TaskRequest

QUERY = """\
Suggest peer reviewers for a manuscript submitted to Review of Scientific
Instruments (AIP): 'Retrofitting a commercial RF induction generator into a
computer-controlled, vacuum and gas integrated annealing system for
reactive-metal grain growth.' The paper: a 6 kW solid-state RF induction
generator is retrofitted with LabVIEW/DAQ computer control, a turbopumped
quartz-tube vacuum chamber with argon backfill and mass-flow control, and
closed-loop PID on a two-color (ratio) pyrometer; graphite and tantalum
susceptor assemblies; validation by nickel grain-growth anneals (power-
temperature calibration R^2=0.991, 0.11% soak repeatability, 40 h soaks at
1325 C), preparation-free EBSD of furnace-annealed nickel (high-quality
Kikuchi patterns with zero metallographic preparation), and a
high-temperature extension coarsening YSZ grains at 2500 C in 45 min with a
boron nitride diffusion barrier.

Search the recent literature (roughly 2015-2026) for active researchers who
publish on: (a) laboratory induction-heating instrument design and
susceptor-based furnaces; (b) radiation thermometry / two-color pyrometry /
emissivity metrology in materials processing; (c) vacuum and controlled-
atmosphere annealing furnace design, including open-source or low-cost
scientific hardware; (d) grain growth kinetics and EBSD-based microstructure
characterization in Ni and in zirconia ceramics; (e) ultra-high-temperature
(>2000 C) ceramic processing. Journals to weigh besides RSI: HardwareX,
Measurement Science and Technology, Journal of Instrumentation, Metallurgical
and Materials Transactions, Journal of the European Ceramic Society, Acta
Materialia, Quantitative InfraRed Thermography Journal.

For each suggested reviewer give: name, current institution and country,
2-4 representative publications (year, venue, DOI) demonstrating fit, which
of pillars (a)-(e) they cover, seniority (early-career / mid / senior), and
any conflict-of-interest caution. Exclude: anyone at Brigham Young
University; coauthors or close collaborators of the manuscript authors
(Sterling G. Baird, Ryan Weber, Christopher Nyborg, Ronnie Guymon, Gage
Erickson, Oliver K. Johnson of BYU Mechanical Engineering; Baird was
previously at the University of Utah and the University of Toronto
Acceleration Consortium). Authors whose work the manuscript cites (e.g.,
V. Rudnev on induction heating; K. Daun's group on pyrometry; S. Tekeli,
K. Matsui on YSZ grain growth; T. Duden on in-situ EBSD) may be suggested -
being cited is not a conflict - but flag them as cited-in-manuscript.

Output a ranked list of 10-15 names with the fields above, then 3-5
alternates, ensuring pillars (a)-(e) are each covered by at least two
people. Verify every DOI you list actually belongs to the named person.
"""


def main():
    client = EdisonClient(api_key=os.environ["EDISON_PLATFORM_API_KEY"])
    task_data = TaskRequest(name=JobNames.LITERATURE, query=QUERY)
    resp = client.create_task(task_data)
    task_id = resp if isinstance(resp, str) else str(resp)
    with open("edison_literature_task_id.txt", "w") as f:
        f.write(task_id + "\n")
    print("task:", task_id)


if __name__ == "__main__":
    main()
