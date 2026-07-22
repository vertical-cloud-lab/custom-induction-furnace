"""Fetch titles and abstracts of Review of Scientific Instruments articles
published in the last 5 years (2021-07-22 to 2026-07-22) from the Crossref
REST API, and write them to rsi_titles_abstracts_2021-2026.jsonl.

Run from paper/title_survey/:  python3 fetch_rsi_corpus.py
"""
import html
import json
import re
import sys
import time

import requests

ISSN = "0034-6748"  # Review of Scientific Instruments (print ISSN)
BASE = f"https://api.crossref.org/journals/{ISSN}/works"
PARAMS = {
    "filter": "from-pub-date:2021-07-22,until-pub-date:2026-07-22,type:journal-article",
    "select": "DOI,title,abstract,published",
    "rows": "1000",
    "mailto": "sgbaird@byu.edu",
}
OUT = "rsi_titles_abstracts_2021-2026.jsonl"

TAG_RE = re.compile(r"<[^>]+>")


def clean(text):
    """Strip JATS/XML tags and collapse whitespace in Crossref abstract text."""
    text = TAG_RE.sub(" ", text)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def main():
    cursor = "*"
    n_total = None
    rows = []
    while True:
        params = dict(PARAMS, cursor=cursor)
        for attempt in range(5):
            try:
                r = requests.get(BASE, params=params, timeout=120)
                r.raise_for_status()
                break
            except Exception as e:  # noqa: BLE001 — retry any transient failure
                print(f"retry {attempt + 1}: {e}", file=sys.stderr)
                time.sleep(5 * (attempt + 1))
        else:
            sys.exit("Crossref request failed after 5 attempts")
        msg = r.json()["message"]
        if n_total is None:
            n_total = msg["total-results"]
            print(f"total results reported: {n_total}")
        items = msg["items"]
        if not items:
            break
        for it in items:
            title = clean(" ".join(it.get("title") or []))
            abstract = clean(it.get("abstract") or "")
            # Crossref abstracts open with a section label such as "Abstract".
            abstract = re.sub(r"^(Abstract|ABSTRACT)[.:\s]*", "", abstract)
            year = (it.get("published", {}).get("date-parts") or [[None]])[0][0]
            rows.append(
                {"doi": it.get("DOI"), "year": year, "title": title, "abstract": abstract}
            )
        print(f"fetched {len(rows)}/{n_total}")
        cursor = msg["next-cursor"]
        time.sleep(1)

    rows.sort(key=lambda x: (x["year"] or 0, x["doi"] or ""))
    with open(OUT, "w") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    n_abs = sum(1 for x in rows if x["abstract"])
    print(f"wrote {len(rows)} records to {OUT}; {n_abs} have abstracts")


if __name__ == "__main__":
    main()
