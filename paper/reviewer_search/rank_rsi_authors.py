"""Score all fetched RSI articles (2015-2026) for topical similarity to the
manuscript (computer-controlled vacuum RF induction annealing furnace;
pyrometer feedback; graphite/tantalum susceptors; Ni + YSZ grain growth;
no-prep EBSD), then rank authors by the summed relevance of their articles.

Outputs:
  rsi_relevant_articles.jsonl : articles with score >= ARTICLE_CUT, ranked
  rsi_author_ranking.csv      : authors ranked by aggregate topical score
  rsi_authors_titles_only.jsonl : full corpus, no abstracts (for Edison upload)

Run from paper/reviewer_search/:  python3 rank_rsi_authors.py
"""
import csv
import json
import re
from collections import defaultdict

# (pattern, weight) applied to title+abstract, title hits count double.
KEYWORDS = [
    (r"induction[- ](?:heat|furnace|generator|melt)", 6),
    (r"\bsusceptor", 6),
    (r"pyromet", 5),
    (r"\bfurnace", 4),
    (r"\banneal", 4),
    (r"grain[- ]growth", 5),
    (r"grain boundar", 3),
    (r"electron backscatter|EBSD|Kikuchi", 4),
    (r"\bemissivity", 3),
    (r"radiation thermometer|radiometric temperature|two-color|ratio pyromet", 5),
    (r"\bcrucible", 4),
    (r"high[- ]temperature", 2),
    (r"heat[- ]treatment", 3),
    (r"\bsinter", 2),
    (r"zirconia|\bYSZ\b|yttria", 3),
    (r"temperature control|PID", 2),
    (r"\bvacuum (?:chamber|furnace|system|anneal)", 3),
    (r"open[- ]source (?:hardware|instrument)|open hardware|LabVIEW", 3),
    (r"\bretrofit", 4),
    (r"radio[- ]?frequency heating|RF heating", 4),
    (r"thermocouple", 1),
    (r"levitation", 2),  # RF levitation furnaces are close cousins
    (r"\bmicrostructur", 2),
]
COMPILED = [(re.compile(p, re.I), w) for p, w in KEYWORDS]
ARTICLE_CUT = 8   # min score to call an article topically relevant

COAUTHOR_FAMILIES = {"baird", "weber", "nyborg", "guymon", "erickson", "johnson"}


def score(title, abstract):
    s = 0
    matched = []
    for rx, w in COMPILED:
        t = len(rx.findall(title or ""))
        a = len(rx.findall(abstract or ""))
        if t or a:
            s += w * (2 * min(t, 2) + min(a, 3))
            matched.append(rx.pattern)
    return s, matched


def main():
    arts = []
    with open("rsi_authors_2015-2026.jsonl") as f, \
         open("rsi_authors_titles_only.jsonl", "w") as g:
        for line in f:
            rec = json.loads(line)
            s, matched = score(rec["title"], rec.get("abstract"))
            rec["score"] = s
            rec["matched"] = matched
            arts.append(rec)
            g.write(json.dumps({k: rec[k] for k in ("doi", "year", "title", "authors")}) + "\n")

    arts.sort(key=lambda r: -r["score"])
    relevant = [r for r in arts if r["score"] >= ARTICLE_CUT]
    with open("rsi_relevant_articles.jsonl", "w") as f:
        for r in relevant:
            f.write(json.dumps(r) + "\n")

    authors = defaultdict(lambda: {"score": 0.0, "n_rel": 0, "papers": [], "affs": set()})
    for r in relevant:
        recency = 1.0 + 0.05 * (r["year"] - 2015 if r["year"] else 0)
        for a in r["authors"]:
            key = f'{a["family"]}, {a["given"]}'.strip(", ")
            d = authors[key]
            d["score"] += r["score"] * recency
            d["n_rel"] += 1
            d["papers"].append((r["score"], r["year"], r["doi"], r["title"]))
            for aff in a.get("affiliation", []):
                d["affs"].add(aff)

    rows = sorted(authors.items(), key=lambda kv: -kv[1]["score"])
    with open("rsi_author_ranking.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["author", "agg_score", "n_relevant_articles", "coauthor_name_collision",
                    "affiliations_seen", "top_papers"])
        for name, d in rows:
            fam = name.split(",")[0].strip().lower()
            top = "; ".join(f"[{s}] {y} doi:{doi} {t[:90]}"
                            for s, y, doi, t in sorted(d["papers"], reverse=True)[:4])
            w.writerow([name, round(d["score"], 1), d["n_rel"],
                        "YES" if fam in COAUTHOR_FAMILIES else "",
                        " | ".join(sorted(d["affs"]))[:200], top])

    print(f"articles total={len(arts)} relevant(score>={ARTICLE_CUT})={len(relevant)}")
    print(f"authors on relevant articles: {len(rows)}")
    for name, d in rows[:25]:
        print(f"{d['score']:7.1f}  n={d['n_rel']}  {name}")


if __name__ == "__main__":
    main()
