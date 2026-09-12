#!/usr/bin/env python3
"""
Major #19 -- trim and merge the 10 per-query Scopus top-up exports.

Input: verify/db_results/Q{1..10}_scopus.csv (raw Scopus exports, one per
Appendix-C query, re-run with the year bound moved to 2026-onward).

Output:
  - verify/db_results/Q{1..10}_scopus_trimmed.csv -- same rows, columns cut
    down to what's actually useful for screening (Scopus exports carry ~45
    columns; most, e.g. Funding Details, Molecular Sequence Numbers, are
    irrelevant here).
  - verify/major19_scopus_topup_merged.csv -- all 10 files combined,
    deduplicated by EID (Scopus's own unique record identifier), with a
    matched_queries column recording every Qn that returned each record.

No screening or relevance judgement is applied -- this is a mechanical
column-trim and duplicate-merge, nothing else.

Usage: python3 verify/major19_scopus_trim_and_merge.py
"""
import csv
import re
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent
DB_RESULTS = ROOT / "verify" / "db_results" / "scopus"

KEEP_COLUMNS = [
    "Authors", "Title", "Year", "Source title", "Cited by", "DOI",
    "Document Type", "Open Access", "EID",
]

QUERY_FILES = [f"Q{i}_scopus.csv" for i in range(1, 11)]

# Same title-level filter used for the arXiv partial search
# (verify/major19_topup_arxiv_search.py) and at the same precision level as
# the manuscript's own Layer-2 title screening: require PEFT/adapter
# terminology to co-occur with a P2P/federated/MoE/serving term IN THE
# TITLE, not just anywhere in the record, to cut a broad OR-heavy Boolean
# search down to something reviewable. This is mechanical keyword
# filtering, not an eligibility/inclusion judgement.
PEFT_TERMS = r"\b(adapter|adapters|lora|peft|parameter-efficient|low-rank)\b"
SCOPE_TERMS = (r"\b(federated|decentrali[sz]ed|peer-to-peer|p2p|multi-task|multitask|"
               r"multi-adapter|serving|inference|routing|mixture-of-experts|moe)\b")


def title_level_filter(title: str) -> bool:
    t = (title or "").lower()
    return bool(re.search(PEFT_TERMS, t)) and bool(re.search(SCOPE_TERMS, t))


def norm_title(t: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", (t or "").strip().lower())


def load_corpus_titles() -> set[str]:
    with open(ROOT / "snowball_output" / "13_final_reading_list_2026-05-12.csv",
              encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    return {norm_title(r["title"]) for r in rows}


def main():
    merged: dict[str, dict] = {}  # keyed by EID (falls back to DOI, then Title)

    for qfile in QUERY_FILES:
        path = DB_RESULTS / qfile
        if not path.exists():
            print(f"  SKIP (not found): {qfile}")
            continue
        qlabel = qfile.replace("_scopus.csv", "")
        with open(path, encoding="utf-8-sig") as f:
            rows = list(csv.DictReader(f))
        print(f"{qfile}: {len(rows)} rows")

        # Write the trimmed per-query file.
        trimmed_path = DB_RESULTS / qfile.replace(".csv", "_trimmed.csv")
        with open(trimmed_path, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=KEEP_COLUMNS)
            w.writeheader()
            for r in rows:
                w.writerow({k: r.get(k, "") for k in KEEP_COLUMNS})

        # Fold into the merged, deduplicated master.
        for r in rows:
            key = (r.get("EID") or r.get("DOI") or r.get("Title", "")).strip().lower()
            if not key:
                continue
            if key not in merged:
                entry = {k: r.get(k, "") for k in KEEP_COLUMNS}
                entry["matched_queries"] = [qlabel]
                merged[key] = entry
            else:
                merged[key]["matched_queries"].append(qlabel)

    print(f"\nTotal raw rows across all 10 files (before dedup): "
          f"{sum(len(v['matched_queries']) for v in merged.values())}")
    print(f"Unique records after EID/DOI/Title dedup: {len(merged)}")

    from collections import Counter
    year_counts = Counter(v.get("Year", "") for v in merged.values())
    print(f"Year distribution (unique records): {dict(year_counts)}")

    out_path = ROOT / "verify" / "major19_scopus_topup_merged.csv"
    fieldnames = KEEP_COLUMNS + ["matched_queries"]
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for entry in sorted(merged.values(), key=lambda x: x.get("Title", "")):
            row = {k: entry.get(k, "") for k in KEEP_COLUMNS}
            row["matched_queries"] = ";".join(entry["matched_queries"])
            w.writerow(row)
    print(f"\nWrote {len(merged)} unique merged records to {out_path}")

    # Title-level shortlist.
    shortlisted = [e for e in merged.values() if title_level_filter(e.get("Title", ""))]
    print(f"Title-level PEFT+scope co-occurrence (reviewable shortlist): {len(shortlisted)}")

    # Exclude records already in the 123-record final corpus (mechanical
    # title match, not a relevance judgement -- these are correct hits, just
    # not new).
    corpus_titles = load_corpus_titles()
    already_in_corpus = [e for e in shortlisted if norm_title(e.get("Title", "")) in corpus_titles]
    new_candidates = [e for e in shortlisted if norm_title(e.get("Title", "")) not in corpus_titles]
    print(f"Of these, already in the 123-record corpus: {len(already_in_corpus)}")
    for e in already_in_corpus:
        print(f"    {e.get('Title')}")
    print(f"Genuinely new candidates: {len(new_candidates)}")

    shortlist_path = ROOT / "verify" / "major19_scopus_topup_shortlist.csv"
    with open(shortlist_path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for entry in sorted(new_candidates, key=lambda x: x.get("Title", "")):
            row = {k: entry.get(k, "") for k in KEEP_COLUMNS}
            row["matched_queries"] = ";".join(entry["matched_queries"])
            w.writerow(row)
    print(f"Wrote {len(new_candidates)} new, shortlisted candidates to {shortlist_path}")
    print("No eligibility/inclusion judgement applied -- shortlist only, for human screening.")


if __name__ == "__main__":
    main()
