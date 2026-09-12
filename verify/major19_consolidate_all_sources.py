#!/usr/bin/env python3
"""
Major #19 -- consolidate the three top-up search sources (arXiv, Scopus, WoS)
into one cross-referenced shortlist.

Inputs:
  - verify/major19_topup_arxiv_candidates.csv
  - verify/major19_scopus_topup_shortlist.csv
  - verify/major19_wos_topup_shortlist.csv

Output: verify/major19_topup_all_sources_consolidated.csv -- one row per
distinct title, with a `sources` column recording which of the three
searches found it (multi-source agreement is a stronger relevance signal
than any single source, though still not a screening/inclusion decision).

No eligibility/inclusion judgement applied. Usage:
    python3 verify/major19_consolidate_all_sources.py
"""
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def norm_title(t: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", (t or "").strip().lower())


def main():
    consolidated: dict[str, dict] = {}

    with open(ROOT / "verify" / "major19_topup_arxiv_candidates.csv", encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            key = norm_title(r["title"])
            consolidated.setdefault(key, {"title": r["title"], "sources": [],
                                           "venue_or_id": [], "year": r["published"][:4]})
            consolidated[key]["sources"].append("arXiv")
            consolidated[key]["venue_or_id"].append(f"arXiv:{r['arxiv_id']}")

    with open(ROOT / "verify" / "major19_scopus_topup_shortlist.csv", encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            key = norm_title(r["Title"])
            consolidated.setdefault(key, {"title": r["Title"], "sources": [],
                                           "venue_or_id": [], "year": r["Year"]})
            consolidated[key]["sources"].append("Scopus")
            consolidated[key]["venue_or_id"].append(r.get("Source title", ""))

    with open(ROOT / "verify" / "major19_wos_topup_shortlist.csv", encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            key = norm_title(r["Title"])
            consolidated.setdefault(key, {"title": r["Title"], "sources": [],
                                           "venue_or_id": [], "year": r["Year"]})
            consolidated[key]["sources"].append("WoS")
            consolidated[key]["venue_or_id"].append(r.get("Source title", ""))

    print(f"Total distinct titles across all three sources: {len(consolidated)}")
    from collections import Counter
    n_sources_dist = Counter(len(v["sources"]) for v in consolidated.values())
    print(f"By number of sources agreeing: {dict(sorted(n_sources_dist.items()))}")

    multi_source = [v for v in consolidated.values() if len(v["sources"]) >= 2]
    print(f"\nFound by 2+ independent sources ({len(multi_source)}):")
    for v in sorted(multi_source, key=lambda x: -len(x["sources"])):
        print(f"  [{'+'.join(v['sources'])}] {v['title']}")

    out_path = ROOT / "verify" / "major19_topup_all_sources_consolidated.csv"
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["title", "year", "sources", "venue_or_id"])
        w.writeheader()
        for v in sorted(consolidated.values(), key=lambda x: (-len(x["sources"]), x["title"])):
            w.writerow({
                "title": v["title"], "year": v["year"],
                "sources": ";".join(v["sources"]),
                "venue_or_id": ";".join(x for x in v["venue_or_id"] if x),
            })
    print(f"\nWrote {len(consolidated)} consolidated rows to {out_path}")


if __name__ == "__main__":
    main()
