#!/usr/bin/env python3
"""
Major #19 -- recover abstracts for the 93 consolidated candidates, for
abstract-level topical-relevance screening.

Abstracts were dropped from the trimmed/merged files to cut size; this
script pulls them back from the raw per-query exports (still on disk,
gitignored) by title match, and from the arXiv summaries already saved.

Usage: python3 verify/major19_recover_abstracts.py
Output: verify/major19_topup_with_abstracts.csv
"""
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def norm_title(t: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", (t or "").strip().lower())


def load_scopus_abstracts() -> dict[str, str]:
    out = {}
    for path in (ROOT / "verify" / "db_results" / "scopus").glob("Q*_scopus.csv"):
        if "trimmed" in path.name:
            continue
        with open(path, encoding="utf-8-sig") as f:
            for r in csv.DictReader(f):
                key = norm_title(r.get("Title", ""))
                if key and r.get("Abstract"):
                    out[key] = r["Abstract"]
    return out


def load_wos_abstracts() -> dict[str, str]:
    out = {}
    for path in (ROOT / "verify" / "db_results" / "wos").glob("Q*_wos.txt"):
        if "trimmed" in path.name:
            continue
        with open(path, encoding="utf-8-sig") as f:
            for r in csv.DictReader(f, delimiter="\t"):
                key = norm_title(r.get("TI", ""))
                if key and r.get("AB"):
                    out[key] = r["AB"]
    return out


def load_arxiv_summaries() -> dict[str, str]:
    out = {}
    with open(ROOT / "verify" / "major19_topup_arxiv_candidates.csv", encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            key = norm_title(r.get("title", ""))
            if key and r.get("summary"):
                out[key] = r["summary"]
    return out


def main():
    scopus_ab = load_scopus_abstracts()
    wos_ab = load_wos_abstracts()
    arxiv_ab = load_arxiv_summaries()
    print(f"Loaded abstracts: Scopus={len(scopus_ab)}, WoS={len(wos_ab)}, arXiv={len(arxiv_ab)}")

    with open(ROOT / "verify" / "major19_topup_all_sources_consolidated.csv",
              encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    print(f"Consolidated candidates: {len(rows)}")

    out_rows = []
    n_found = 0
    for r in rows:
        key = norm_title(r["title"])
        ab = scopus_ab.get(key) or wos_ab.get(key) or arxiv_ab.get(key) or ""
        if ab:
            n_found += 1
        out_rows.append({**r, "abstract": ab})

    print(f"Abstracts recovered: {n_found} / {len(rows)}")
    missing = [r["title"] for r in out_rows if not r["abstract"]]
    if missing:
        print(f"Missing abstracts for {len(missing)}:")
        for t in missing:
            print(f"    {t}")

    out_path = ROOT / "verify" / "major19_topup_with_abstracts.csv"
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["title", "year", "sources", "venue_or_id", "abstract"])
        w.writeheader()
        for r in out_rows:
            w.writerow(r)
    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    main()
