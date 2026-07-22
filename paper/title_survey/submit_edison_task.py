"""Submit an Edison Scientific analysis task: feedback on the manuscript title
against 5 years of Review of Scientific Instruments titles/abstracts.

Run from paper/title_survey/:  python3 submit_edison_task.py
Writes the created task id to edison_task_id.txt.
"""
import os

from edison_client import EdisonClient, JobNames
from edison_client.models import TaskRequest

CURRENT_TITLE = (
    "Retrofitting a commercial RF induction generator into a "
    "computer-controlled, vacuum-integrated annealing system for "
    "reactive-metal grain growth"
)

ABSTRACT = """\
High-temperature vacuum annealing near a metal's melting point drives \
controlled grain growth, but it normally requires an expensive turn-key \
vacuum induction furnace. We describe an open modernization stack (the added \
control, vacuum, and temperature-feedback hardware and software) that \
converts a bare commercial radio-frequency (RF) induction generator into a \
computer-controlled, vacuum-integrated annealing system with pyrometer \
feedback. The modernization stack consists of analog power control through \
LabVIEW and a data-acquisition (DAQ) device, dual-wavelength optical \
temperature feedback, a high-vacuum quartz-tube chamber, and an in-house \
machined graphite crucible that serves as a susceptor (an RF-absorbing \
element that heats the charge it encloses) for metal specimens. The \
modernization stack transfers between generators because its only \
requirement is a monotonic analog power-control input. The reproducible \
build is anchored on a current 6 kW solid-state generator. In operation, \
the system produced a fixed-geometry power-temperature calibration with \
R^2 = 0.991 over 1200-1400 C. Eight nickel anneals at 1200 C for 12 h \
reproduced their soak temperature to 1201.2 +/- 1.3 C, and soaks up to 40 h \
at 1325 C remained stable. The annealed nickel microstructures were \
characterized by optical metallography, scanning electron microscopy (SEM), \
and electron backscatter diffraction (EBSD). A modified sample stack \
extends the furnace to non-coupling ceramics at temperatures up to 2500 C, \
demonstrated with yttria-stabilized zirconia (YSZ) grain growth. Complete \
design files, the bill of materials, the control software, and the data are \
openly available.\
"""

QUERY = f"""\
We are preparing a manuscript for submission to Review of Scientific \
Instruments (RSI, AIP Publishing) and want feedback on our working title.

Current title: "{CURRENT_TITLE}"

Manuscript abstract, for context:
{ABSTRACT}

The uploaded file rsi_titles_abstracts_2021-2026.jsonl contains the titles \
and abstracts of all 4,408 journal articles published in Review of \
Scientific Instruments over the last 5 years (2021-07-22 to 2026-07-22), \
retrieved from Crossref. Each line is a JSON object with keys: doi, year, \
title, abstract (4,324 of the records have a non-empty abstract).

Please analyze this corpus and give feedback on our current title:
1. Characterize RSI title conventions from the corpus: typical length \
(words/characters), structural patterns (e.g., noun-phrase vs. sentence, \
use of colons/subtitles, leading gerunds like "Retrofitting"), and how \
often instrument-development papers name the instrument class, the \
technique, and the application in the title.
2. Compare our title against those conventions: is it typical or an \
outlier in length and structure? Identify the closest comparable papers \
(similar topic: induction heating/furnaces, vacuum annealing, \
open-source/low-cost instrument builds, retrofits/modernizations of \
commercial equipment) and how they titled them.
3. Assess discoverability: does our title contain the terms researchers \
searching this space actually use (based on terms frequent in the corpus)? \
Note any jargon in our title that rarely appears in the corpus, and any \
high-value keywords from our abstract that the title omits.
4. Give concrete recommendations: keep, tweak, or rework, with 3-5 \
specific alternative titles consistent with RSI conventions, each with a \
one-sentence rationale. Note any tension with the fact that the abstract \
already leads with "grain growth" as the motivating application.

Please include quantitative support (counts, distributions, example \
titles with DOIs) from the corpus for your claims.\
"""


def main():
    client = EdisonClient(api_key=os.environ["EDISON_PLATFORM_API_KEY"])
    task_data = TaskRequest(name=JobNames.ANALYSIS, query=QUERY)
    responses = client.create_task(
        task_data, files=["rsi_titles_abstracts_2021-2026.jsonl"]
    )
    task_id = responses if isinstance(responses, str) else str(responses)
    with open("edison_task_id.txt", "w") as f:
        f.write(task_id + "\n")
    print("created task:", task_id)


if __name__ == "__main__":
    main()
