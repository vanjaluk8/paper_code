#!/usr/bin/env python3
"""
Major #19 -- trim and merge the per-query WoS top-up exports.

Input: verify/db_results/wos/Q{1..10}[b/c]_wos.txt (raw WoS tab-delimited
exports, one per Appendix-C query, re-run with the year bound moved to
2026-onward). Q3 was split into Q3/Q3b/Q3c by the author because it hit
WoS's per-export row cap (1000) -- all three are treated as one query
("Q3") for provenance-tracking purposes.

Output:
  - verify/db_results/wos/Q*_wos_trimmed.csv -- same rows, columns cut down
    (WoS's raw export carries all ~70 field tags; most, e.g. CR = cited
    references, FU = funding, are irrelevant here).
  - verify/major19_wos_topup_merged.csv -- all files combined, deduplicated
    by UT (WoS's own unique accession number), with a matched_queries
    column recording every Qn that returned each record.
  - verify/major19_wos_topup_shortlist.csv -- title-level PEFT+scope filter
    applied (same precision as the arXiv/Scopus passes), cross-checked
    against the 123-record corpus.

No screening or relevance judgement is applied beyond the mechanical title
keyword filter -- nothing here is an eligibility/inclusion decision.

Usage: python3 verify/major19_wos_trim_and_merge.py
"""
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WOS_DIR = ROOT / "verify" / "db_results" / "wos"

# WoS field tags -> friendly names for the trimmed output.
KEEP_FIELDS = {
    "AU": "Authors",
    "TI": "Title",
    "PY": "Year",
    "SO": "Source title",
    "TC": "Cited by",
    "DI": "DOI",
    "DT": "Document Type",
    "OA": "Open Access",
    "UT": "UT (Accession Number)",
}
OUT_COLUMNS = list(KEEP_FIELDS.values())

# Query files -> query label (Q3/Q3b/Q3c collapse to one label: they're the
# same query, split across exports only because of WoS's per-export cap).
QUERY_FILES = {
    "Q1_wos.txt": "Q1",
    "Q2_wos.txt": "Q2",
    "Q3_wos.txt": "Q3",
    "Q3b_wos.txt": "Q3",
    "Q3c_wos.txt": "Q3",
    "Q4_wos.txt": "Q4",
    "Q5_wos.txt": "Q5",
    "Q6_wos.txt": "Q6",
    "Q7_wos.txt": "Q7",
    "Q8_wos.txt": "Q8",
    "Q9_wos.txt": "Q9",
    "Q10_wos.txt": "Q10",
}

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
    merged: dict[str, dict] = {}  # keyed by UT, falling back to DOI then title

    for fname, qlabel in QUERY_FILES.items():
        path = WOS_DIR / fname
        if not path.exists():
            print(f"  SKIP (not found): {fname}")
            continue
        with open(path, encoding="utf-8-sig") as f:
            rows = list(csv.DictReader(f, delimiter="\t"))
        print(f"{fname} ({qlabel}): {len(rows)} rows")

        # Write the trimmed per-file output.
        trimmed_path = WOS_DIR / fname.replace(".txt", "_trimmed.csv")
        with open(trimmed_path, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=OUT_COLUMNS)
            w.writeheader()
            for r in rows:
                w.writerow({KEEP_FIELDS[k]: r.get(k, "") for k in KEEP_FIELDS})

        for r in rows:
            key = (r.get("UT") or r.get("DI") or r.get("TI", "")).strip().lower()
            if not key:
                continue
            if key not in merged:
                entry = {KEEP_FIELDS[k]: r.get(k, "") for k in KEEP_FIELDS}
                entry["matched_queries"] = [qlabel]
                merged[key] = entry
            elif qlabel not in merged[key]["matched_queries"]:
                merged[key]["matched_queries"].append(qlabel)

    total_raw = sum(len(v["matched_queries"]) for v in merged.values())
    print(f"\nTotal raw rows across all files (before dedup, query-collapsed): {total_raw}")
    print(f"Unique records after UT/DOI/Title dedup: {len(merged)}")

    from collections import Counter
    year_counts = Counter(v.get("Year", "") for v in merged.values())
    print(f"Year distribution (unique records): {dict(year_counts)}")

    fieldnames = OUT_COLUMNS + ["matched_queries"]
    out_path = ROOT / "verify" / "major19_wos_topup_merged.csv"
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for entry in sorted(merged.values(), key=lambda x: x.get("Title", "")):
            row = {k: entry.get(k, "") for k in OUT_COLUMNS}
            row["matched_queries"] = ";".join(entry["matched_queries"])
            w.writerow(row)
    print(f"\nWrote {len(merged)} unique merged records to {out_path}")

    shortlisted = [e for e in merged.values() if title_level_filter(e.get("Title", ""))]
    print(f"Title-level PEFT+scope co-occurrence (reviewable shortlist): {len(shortlisted)}")

    corpus_titles = load_corpus_titles()
    already_in_corpus = [e for e in shortlisted if norm_title(e.get("Title", "")) in corpus_titles]
    new_candidates = [e for e in shortlisted if norm_title(e.get("Title", "")) not in corpus_titles]
    print(f"Of these, already in the 123-record corpus: {len(already_in_corpus)}")
    for e in already_in_corpus:
        print(f"    {e.get('Title')}")
    print(f"Genuinely new candidates: {len(new_candidates)}")

    shortlist_path = ROOT / "verify" / "major19_wos_topup_shortlist.csv"
    with open(shortlist_path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for entry in sorted(new_candidates, key=lambda x: x.get("Title", "")):
            row = {k: entry.get(k, "") for k in OUT_COLUMNS}
            row["matched_queries"] = ";".join(entry["matched_queries"])
            w.writerow(row)
    print(f"Wrote {len(new_candidates)} new, shortlisted candidates to {shortlist_path}")
    print("No eligibility/inclusion judgement applied -- shortlist only, for human screening.")


if __name__ == "__main__":
    main()
