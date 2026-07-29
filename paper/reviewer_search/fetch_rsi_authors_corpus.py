"""Fetch DOI, title, abstract, authors (with affiliations where present) for
Review of Scientific Instruments journal articles from Crossref, 2015-01-01
through 2026-07-29, and write rsi_authors_2015-2026.jsonl.

Wide sweep for the reviewer-suggestion analysis (PR #12, 2026-07-29).
Run from paper/reviewer_search/:  python3 fetch_rsi_authors_corpus.py
"""
import html
import json
import re
import time

import requests

ISSN = "0034-6748"
BASE = f"https://api.crossref.org/journals/{ISSN}/works"
PARAMS = {
    "filter": "from-pub-date:2015-01-01,until-pub-date:2026-07-29,type:journal-article",
    "select": "DOI,title,abstract,published,author",
    "rows": "1000",
    "mailto": "sgbaird@byu.edu",
}
OUT = "rsi_authors_2015-2026.jsonl"
TAG_RE = re.compile(r"<[^>]+>")


def clean(text):
    text = TAG_RE.sub(" ", text)
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def main():
    cursor = "*"
    n = 0
    with open(OUT, "w") as f:
        while True:
            params = dict(PARAMS, cursor=cursor)
            for attempt in range(5):
                try:
                    r = requests.get(BASE, params=params, timeout=60)
                    r.raise_for_status()
                    break
                except Exception as e:
                    print(f"retry {attempt}: {e}")
                    time.sleep(5 * (attempt + 1))
            else:
                raise SystemExit("Crossref unreachable")
            msg = r.json()["message"]
            items = msg.get("items", [])
            if not items:
                break
            for it in items:
                year = None
                pub = it.get("published") or {}
                parts = pub.get("date-parts") or [[None]]
                if parts and parts[0]:
                    year = parts[0][0]
                authors = []
                for a in it.get("author", []) or []:
                    authors.append({
                        "given": a.get("given", ""),
                        "family": a.get("family", ""),
                        "affiliation": [aff.get("name", "") for aff in a.get("affiliation", []) if aff.get("name")],
                    })
                rec = {
                    "doi": it.get("DOI"),
                    "year": year,
                    "title": clean((it.get("title") or [""])[0]),
                    "abstract": clean(it.get("abstract", "")) or None,
                    "authors": authors,
                }
                f.write(json.dumps(rec) + "\n")
                n += 1
            print(f"{n} records...", flush=True)
            cursor = msg.get("next-cursor")
            if not cursor:
                break
            time.sleep(1)
    print(f"done: {n} records -> {OUT}")


if __name__ == "__main__":
    main()
