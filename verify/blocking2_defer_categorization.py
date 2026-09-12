#!/usr/bin/env python3
"""Blocking 2: categorise the 173 DEFER-origin records dropped without
individual full-text assessment (verify/wp13_defer_records.csv), to support
a grouped PRISMA 2020 Item 16b exclusion reason rather than 173 individual
codes. Joins in abstracts from the 552-record abstract-review pool
(S7b_abstract_reviewed_final.csv) by DOI, then arXiv ID, then title."""
import csv
import json
import re

DEFER = "verify/wp13_defer_records.csv"
ABSTRACTS = "snowball_output/S7b_abstract_reviewed_final.csv"
OUT_JSON = "verify/blocking2_defer_categorized.json"


def load_abstracts():
    rows = list(csv.DictReader(open(ABSTRACTS, newline="", encoding="utf-8")))
    by_doi = {r["doi"].strip().lower(): r for r in rows if r["doi"].strip()}
    by_arxiv = {r["arxiv_id"].strip(): r for r in rows if r["arxiv_id"].strip()}
    by_title = {r["title"].strip().lower(): r for r in rows}
    return by_doi, by_arxiv, by_title


def categorize(title, abstract):
    t = (title + " " + abstract).lower()
    if re.search(r"\bp2p\b|peer-to-peer|decentrali[sz]ed|gossip", t):
        return "p2p-decentralized"
    if re.search(r"federat", t):
        return "federated-peft"
    if re.search(r"multi-tenant|serving|inference (system|latency|serverless)|kv-cache|kernel|throughput|serverless", t):
        return "multi-tenant-serving"
    if re.search(r"mixture.of.expert|\bmoe\b|routing|multi-task", t):
        return "moe-routing-composition"
    return "single-model-peft-variant"


def main():
    by_doi, by_arxiv, by_title = load_abstracts()
    defer_rows = list(csv.DictReader(open(DEFER, newline="", encoding="utf-8")))

    out = []
    for d in defer_rows:
        r = (
            by_doi.get(d["doi"].strip().lower())
            or by_arxiv.get(d["arxiv_id"].strip())
            or by_title.get(d["title"].strip().lower())
        )
        abstract = r.get("abstract", "").strip() if r else ""
        out.append({
            "title": d["title"],
            "doi": d["doi"],
            "arxiv_id": d["arxiv_id"],
            "abstract": abstract,
            "category": categorize(d["title"], abstract),
        })

    json.dump(out, open(OUT_JSON, "w", encoding="utf-8"), indent=1)

    from collections import Counter
    counts = Counter(o["category"] for o in out)
    print(f"{len(out)} DEFER records categorized ({sum(1 for o in out if o['abstract'])} with abstract)")
    for c, n in counts.most_common():
        print(f"  {c}: {n}")


if __name__ == "__main__":
    main()
