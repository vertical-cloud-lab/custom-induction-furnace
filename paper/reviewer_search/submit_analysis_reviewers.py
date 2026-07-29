"""Submit an Edison Scientific ANALYSIS task: suggest peer reviewers for the
RSI induction-furnace manuscript from a wide sweep of RSI authors (2015-2026).

Uploads (text-path only; binary multipart uploads 500 server-side, see
paper/review_spotcheck_query/README.md):
  - paper_text.txt: pdftotext of the compiled manuscript
  - rsi_all_articles_compact.tsv: all 11,869 RSI journal articles 2015-2026
    (doi, year, author family names, title) from Crossref
  - rsi_relevant_articles.jsonl: the 351 articles scoring >= 8 on a
    topical-keyword screen, with abstracts, full author names, affiliations
    (where Crossref has them), scores, and matched keywords
  - rsi_author_ranking.csv: authors ranked by aggregate topical score

Run from paper/reviewer_search/:  python3 submit_analysis_reviewers.py
Writes edison_analysis_task_id.txt.
"""
import os

from edison_client import EdisonClient, JobNames
from edison_client.models import RuntimeConfig, TaskRequest

FILES = [
    ("paper_text.txt", "paper_text.txt",
     "pdftotext extraction of the manuscript under review: 'Retrofitting a "
     "commercial RF induction generator into a computer-controlled, vacuum "
     "and gas integrated annealing system for reactive-metal grain growth', "
     "submitted to Review of Scientific Instruments (AIP). 8 pages."),
    ("rsi_all_articles_compact.tsv", "rsi_all_articles_compact.tsv",
     "All 11,869 Review of Scientific Instruments journal articles published "
     "2015-01-01 to 2026-07-29, from Crossref: doi, year, author family "
     "names + first initial, title. The full-corpus sweep."),
    ("rsi_relevant_articles.jsonl", "rsi_relevant_articles.jsonl",
     "The 351 topically relevant RSI articles (keyword score >= 8) with "
     "title, abstract, year, doi, full author names and affiliations where "
     "Crossref provides them, plus the keyword score and matched patterns."),
    ("rsi_author_ranking.csv", "rsi_author_ranking.csv",
     "RSI authors ranked by aggregate topical score over the relevant "
     "articles: author, score, article count, coauthor-family-name-collision "
     "flag, affiliations seen, top supporting papers."),
]

QUERY = """\
We need suggested peer reviewers for a manuscript being submitted to Review
of Scientific Instruments (RSI, AIP Publishing). The manuscript
(paper_text.txt) describes retrofitting a commercial 6 kW RF induction
generator into an open, computer-controlled, vacuum- and gas-integrated
annealing furnace with ratio-pyrometer feedback (LabVIEW + DAQ), graphite and
tantalum susceptors, validated by nickel grain-growth anneals (calibration,
repeatability, 40 h soaks), preparation-free EBSD of the annealed nickel, and
a 2500 C YSZ grain-growth extension. Its pillars: scientific instrument
design / open hardware; induction heating; optical pyrometry and emissivity;
vacuum and controlled-atmosphere furnace practice; grain growth and EBSD.

Your main task: a wide sweep of RSI's own author pool to find the reviewers
who best fit this manuscript. Files provided:
- rsi_all_articles_compact.tsv: ALL 11,869 RSI journal articles 2015-2026
  (doi, year, authors, title).
- rsi_relevant_articles.jsonl: 351 articles pre-screened as topically
  relevant by a keyword score (with abstracts, full author names, scores).
- rsi_author_ranking.csv: authors pre-ranked by aggregate keyword score.

Do NOT simply accept the pre-screen: it is keyword-based and crude. Please
(1) run your own sweep over the full TSV for candidate authors the keyword
screen may have missed (e.g., titles about levitation processing, containerless
solidification, in situ heating stages, high-temperature mechanical testing
rigs, thermal-analysis instruments, image-furnace or laser-heating systems,
open-source instrument control); (2) critically re-rank: an author is a good
reviewer fit if their RSI work shows they build/publish comparable thermal
instrumentation, not merely if a keyword matched; senior/corresponding-style
authors with a sustained record beat one-off middle authors; (3) for each
candidate, use the corpus (and your own knowledge of the field) to judge
seniority, current activity (favor 2021+ activity), and likely institution.

Conflict-of-interest screen: the manuscript authors are Sterling G. Baird,
Ryan Weber, Christopher Nyborg, Ronnie Guymon, Gage Erickson, and Oliver K.
Johnson, all Department of Mechanical Engineering, Brigham Young University
(BYU), Provo, Utah. Exclude anyone at BYU, any coauthor of these six (note
S. G. Baird previously worked at the University of Utah and the University of
Toronto Acceleration Consortium - flag anyone from those groups), and note
(do not exclude) authors whose work is cited in the manuscript's reference
list. Beware family-name collisions (e.g., other Johnsons are fine if
unrelated).

Output:
1. A ranked table of 12-15 recommended reviewers: name, likely current
   institution (say 'uncertain' if you cannot pin it down), 2-4 supporting
   RSI papers (year + DOI), one-sentence fit rationale, which manuscript
   pillar(s) they cover, and COI status.
2. Make sure the set as a whole covers all five pillars; say which candidates
   cover which.
3. A short list of 3-5 'stretch' alternates (strong fit but some uncertainty).
4. Methods note: how you swept the corpus, what you looked for beyond the
   keyword screen, and known limitations (e.g., Crossref affiliations are
   sparse; author disambiguation by name only).
Be concrete and verifiable: every claim about a candidate's RSI record must
carry DOIs from the provided corpus.
"""


def main():
    client = EdisonClient(api_key=os.environ["EDISON_PLATFORM_API_KEY"])
    uris = []
    for name, path, description in FILES:
        upload = client.store_file_content(name=name, file_path=path, description=description)
        uris.append(f"data_entry:{upload.data_storage.id}")
        print("uploaded", name)
    task_data = TaskRequest(
        name=JobNames.ANALYSIS,
        query=QUERY,
        runtime_config=RuntimeConfig(environment_config={"data_storage_uris": uris}),
    )
    resp = client.create_task(task_data)
    task_id = resp if isinstance(resp, str) else str(resp)
    with open("edison_analysis_task_id.txt", "w") as f:
        f.write(task_id + "\n")
    print("task:", task_id)


if __name__ == "__main__":
    main()
