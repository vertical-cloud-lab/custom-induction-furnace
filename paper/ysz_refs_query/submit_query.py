"""Submit an Edison Scientific literature task: citable references for two
manuscript statements in the YSZ / high-temperature extension section.

Requested by S. Baird (PR #12, 2026-07-22): (1) a real reference for
"grain growth in refractory ceramics follows Arrhenius kinetics", and
(2) a real reference for the graphite-alumina "eutectic reaction" claim
(with a wording check, in case "eutectic" is not what the literature
supports).

No file upload is needed, so this uses the LITERATURE job type (per
CLAUDE.md, ANALYSIS is only required when uploading files).

Run from paper/ysz_refs_query/:  python3 submit_query.py
Writes the created task id to edison_task_id.txt.
"""
import os

from edison_client import EdisonClient, JobNames
from edison_client.models import TaskRequest

QUERY = """\
We are finalizing a Review of Scientific Instruments manuscript on a custom
vacuum induction annealing furnace. We need authoritative, citable
references (with DOIs) for two specific statements in the section on
extending the furnace to refractory ceramics (8 mol% yttria-stabilized
zirconia, YSZ):

1. The statement: "Grain growth in refractory ceramics follows Arrhenius
   kinetics and is therefore highly sensitive to annealing temperature."
   Context: we compare grain coarsening of 8YSZ from roughly 10-20 um to
   roughly 90 um, which took 228 h at 1600 C in a conventional box furnace
   but only 45 min at 2500 C in our induction furnace. Please identify the
   best one to three references establishing that grain growth in ceramics
   is thermally activated with Arrhenius temperature dependence, ideally
   including measured grain-growth kinetics and activation energies for
   YSZ / cubic zirconia specifically (textbook treatments such as
   Rahaman's "Ceramic Processing and Sintering" or classic papers are
   fine, but journal articles with DOIs are preferred).

2. The statement: "Direct contact between graphite and alumina was
   eliminated because they undergo a eutectic reaction that lowers the
   interface melting temperature to approximately 1800 C." Please check
   this claim against the Al2O3-C literature: carbothermal reduction of
   alumina, the Al2O3-Al4C3 phase diagram and its eutectics, and
   alumina-graphite interface reactions at high temperature. Provide the
   best one to three citable references with DOIs. IMPORTANT: if the
   "eutectic" wording or the approximately-1800-C figure is not what the
   literature supports, say exactly what wording would be supported (for
   example, carbothermal reduction beginning near 1700-1900 C under
   vacuum, forming Al4C3 and CO, degrading the interface) and give the
   references for that corrected wording instead.

For each statement, give full bibliographic details (authors, title,
journal, year, volume, pages, DOI) and a one-sentence rationale for why it
is the right citation to attach to that sentence.\
"""


def main():
    client = EdisonClient(api_key=os.environ["EDISON_PLATFORM_API_KEY"])
    task_data = TaskRequest(name=JobNames.LITERATURE, query=QUERY)
    responses = client.create_task(task_data)
    task_id = responses if isinstance(responses, str) else str(responses)
    with open("edison_task_id.txt", "w") as f:
        f.write(task_id + "\n")
    print("created task:", task_id)


if __name__ == "__main__":
    main()
