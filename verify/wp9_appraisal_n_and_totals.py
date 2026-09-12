#!/usr/bin/env python3
"""
WP-9 / P1-5 + P1-7.

P1-5: Sec 3.4/Figure 6 report the reporting-completeness appraisal (mean,
SD, band counts) over all 123 records, but Figure 5's INCLUDED box already
distinguishes "123 records; 120 distinct papers" -- three works (LoRA,
Houlsby, CaraServe/Toppings) are each scored twice under two identities.
Sec 3.4's own footnote (Sec 3.1, line ~165) asserts the manuscript's count
is 120 distinct papers; this script checks whether the three duplicate pairs
were in fact scored identically (as an "unaffected mean" defence would
require) and reports the mean/SD/median computed both ways.

P1-7: sums the gross records identified across all four discovery routes
and checks it against the only number the abstract currently cites (1,150).

Usage: python3 verify/wp9_appraisal_n_and_totals.py
"""
import csv
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APPRAISAL = ROOT / "figures" / "quality_appraisal_scored.csv"

DUPLICATE_TITLE_PAIRS = [
    ("lora: low-rank adaptation of large language models",
     "lora: low-rank adaptation of large language models"),
    ("parameter-efficient transfer learning for nlp",
     "parameter-efficient transfer learning for nlp"),
]
# CaraServe/Toppings share no title text -- matched by DOI/arxiv_id instead.
CARASERVE_ARXIV = "2401.11240"


def load_rows():
    with open(APPRAISAL, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 123
    return rows


def find_duplicate_rows(rows):
    by_title = {}
    for r in rows:
        by_title.setdefault(r["title"].strip().lower(), []).append(r)
    dup_groups = []
    for title in {"lora: low-rank adaptation of large language models",
                  "parameter-efficient transfer learning for nlp"}:
        group = by_title[title]
        assert len(group) == 2, f"expected 2 rows for {title!r}, got {len(group)}"
        dup_groups.append(group)
    caraserve_group = [r for r in rows if "caraserve" in r["title"].strip().lower()
                        or "toppings" in r["title"].strip().lower()]
    assert len(caraserve_group) == 2, f"expected 2 CaraServe/Toppings rows, got {len(caraserve_group)}"
    dup_groups.append(caraserve_group)
    return dup_groups


def summarize(scores, label):
    print(f"  {label}: n={len(scores)}, mean={statistics.mean(scores):.4f}, "
          f"sd={statistics.stdev(scores):.4f}, median={statistics.median(scores)}")


def main():
    rows = load_rows()
    dup_groups = find_duplicate_rows(rows)

    print("=== Duplicate-pair scores (reporting_completeness_score) ===")
    identical_count = 0
    for group in dup_groups:
        scores = [int(r["reporting_completeness_score"]) for r in group]
        titles = [r["title"][:45] for r in group]
        same = scores[0] == scores[1]
        identical_count += same
        print(f"  {titles[0]!r}: {scores} {'(identical)' if same else '(DIFFERENT)'}")
    print(f"  {identical_count} of {len(dup_groups)} duplicate pairs are scored identically.")
    if identical_count < len(dup_groups):
        print("  -> The manuscript CANNOT claim duplicates were scored identically")
        print("     and the mean is therefore unaffected. That escape hatch is closed")
        print("     by the data; the two counting methods must be compared directly.")

    all_scores = [int(r["reporting_completeness_score"]) for r in rows]
    print()
    print("=== Mean/SD/median, both ways ===")
    summarize(all_scores, "Over all 123 records (current manuscript basis)")

    # 120-distinct-studies basis: drop one row from each duplicate pair.
    # Rule: keep the row with the higher score is NOT used (that would bias
    # the mean upward); instead keep the row that represents the record's
    # PUBLISHED/canonical identity per how the review's own found_type
    # question would resolve it -- for LoRA and Houlsby, drop the row without
    # an arxiv_id (the Scopus-only duplicate row, arbitrary but consistent);
    # for CaraServe/Toppings, keep the published Toppings/USENIX version
    # (the citable, peer-reviewed identity) and drop the arXiv preprint row.
    drop_ids = set()
    for group in dup_groups:
        if any("toppings" in r["title"].strip().lower() for r in group):
            drop = next(r for r in group if "toppings" not in r["title"].strip().lower())
        else:
            drop = next((r for r in group if not r.get("arxiv_id", "").strip()), group[1])
        drop_ids.add(id(drop))
    scores_120 = [int(r["reporting_completeness_score"]) for r in rows if id(r) not in drop_ids]
    assert len(scores_120) == 120
    summarize(scores_120, "Over 120 distinct studies (one row per duplicate pair dropped)")

    diff = statistics.mean(all_scores) - statistics.mean(scores_120)
    print(f"  Difference in mean: {diff:+.4f}")
    print(f"  Reported manuscript mean is 6.04 -- 123-record mean computed here is "
          f"{statistics.mean(all_scores):.4f}")

    print()
    print("=== 120-distinct-study band tally ===")
    bands_120 = []
    for r in rows:
        if id(r) in drop_ids:
            continue
        bands_120.append(r["reporting_completeness_band"])
    from collections import Counter
    band_order = ["High (9-10)", "Upper-mid (6-8)", "Lower-mid (3-5)", "Low (0-2)"]
    tally = Counter(bands_120)
    for b in band_order:
        pct = 100 * tally[b] / len(bands_120)
        print(f"  {b}: {tally[b]} ({pct:.1f}%)")
    print(f"  TOTAL: {sum(tally.values())}")

    # Write the corrected 120-row CSV (author-approved rule: keep each pair's
    # published/canonical identity -- arXiv-keyed row for LoRA/Houlsby,
    # Toppings/USENIX row over the CaraServe preprint).
    out_path = ROOT / "verify" / "wp9_quality_appraisal_120_studies.csv"
    fieldnames = list(rows[0].keys())
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            if id(r) not in drop_ids:
                w.writerow(r)
    print()
    print(f"Wrote corrected 120-row appraisal CSV to {out_path}")

    print()
    print("=== P1-7: gross records identified across all four discovery routes ===")
    routes = {
        "Snowball (Semantic Scholar/Scopus/ACL, 2026-04-21)": 1150,
        "Undermind G1-G6 exports (2026-04-14)": 377,
        "G0 direct seeds": 9,
        "Forward-citation snowball, Scopus+WoS (2026-05-08)": 88,
        "Manual Scopus/WoS cross-validation top-up": 34,
    }
    for k, v in routes.items():
        print(f"  {k}: {v}")
    total = sum(routes.values())
    print(f"  TOTAL gross records identified: {total}")


if __name__ == "__main__":
    main()
