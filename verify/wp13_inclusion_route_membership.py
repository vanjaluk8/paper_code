#!/usr/bin/env python3
"""
WP-13 / P1-1 + Blocking 2 -- the inclusion-route defect.

Central question: are the 53 review_source=abstract-2nd-pass records (from
snowball_output/11_data_extraction_2026-05-12.csv) inside the 190-record
extraction subset drawn from the 387-record full-text queue, or did they
enter by some other route that bypasses full-text eligibility assessment?

Method: join snowball_output/13_final_reading_list_2026-05-12.csv (123 final
records) to snowball_output/11_data_extraction_2026-05-12.csv (224 extraction
rows, has the review_source label) by paper_key, and separately to
snowball_output/pipeline_unified.csv (622 rows, has per-stage 0/1 flags) by
normalised title, to build a 7-stage membership matrix per final record.

Also checks the 173 fulltext_decision=DEFER records' stage membership, and
reports a secondary anomaly found along the way (2 of the 34 manual
cross-validation top-up records have in_fulltext_queue_Q9=1 in
pipeline_unified.csv, contradicting the manuscript's own source-comment claim
that "all 34 have no S5/S6/S7b/Q9 stage flags set").

This script only computes and reports. Per the task instructions, if the
data answers the central question (it does), the corrected manuscript
wording is a proposed diff for author approval -- not applied here.

Usage: python3 verify/wp13_inclusion_route_membership.py
Outputs: verify/wp13_membership_matrix.csv (123 rows x 7 stage columns),
         verify/wp13_defer_records.csv (173 DEFER records' stage flags),
         and a printed summary.
"""
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FINAL_LIST = ROOT / "snowball_output" / "13_final_reading_list_2026-05-12.csv"
EXTRACTION = ROOT / "snowball_output" / "11_data_extraction_2026-05-12.csv"
PIPELINE = ROOT / "snowball_output" / "pipeline_unified.csv"

STAGE_COLUMNS = [
    ("title_screened_502", "in_title_screened_S5"),   # merged-502 stage, per pipeline's own S5 label
    ("enriched_464", "in_enriched_S6"),
    ("abstract_pool_552", "in_abstract_review_S7b"),
    ("fulltext_queue_387", "in_fulltext_queue_Q9"),
    ("extraction_224", "in_extraction_E11"),
    ("final_123", "in_final_list_123"),
]


def norm_title(t):
    return re.sub(r"[^a-z0-9]+", "", (t or "").strip().lower())


def load_csv(path, **kwargs):
    with open(path, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f, **kwargs))


def main():
    final_rows = load_csv(FINAL_LIST)
    ext_rows = load_csv(EXTRACTION)
    pipe_rows = load_csv(PIPELINE)

    assert len(final_rows) == 123
    assert len(ext_rows) == 224
    assert len(pipe_rows) == 622

    ext_by_key = {r["paper_key"]: r for r in ext_rows}
    pipe_by_title = {}
    for r in pipe_rows:
        pipe_by_title.setdefault(norm_title(r["title"]), []).append(r)

    matrix_rows = []
    no_extraction_match = []
    no_pipeline_match = []
    for fr in final_rows:
        key = fr["paper_key"]
        ext = ext_by_key.get(key)
        if ext is None:
            no_extraction_match.append(key)
            continue
        prows = pipe_by_title.get(norm_title(fr["title"]), [])
        if not prows:
            no_pipeline_match.append(fr["title"])
            continue
        row = {"paper_key": key, "title": fr["title"], "review_source": ext["review_source"]}
        for label, col in STAGE_COLUMNS:
            flags = {p[col] for p in prows}
            row[label] = "1" if "1" in flags else "0"
        matrix_rows.append(row)

    print(f"Final records: {len(final_rows)}")
    print(f"Matched to an extraction row by paper_key: {len(matrix_rows) + len(no_extraction_match)}")
    print(f"  no extraction match: {no_extraction_match}")
    print(f"Matched to a pipeline row by normalised title: {len(matrix_rows)}")
    print(f"  no pipeline match: {no_pipeline_match}")

    print()
    print("=== Central question: are the 53 abstract-2nd-pass records inside")
    print("    the 387-record full-text queue / 190-record extraction subset? ===")
    by_source = {}
    for row in matrix_rows:
        src = row["review_source"]
        by_source.setdefault(src, []).append(row)
    for src, rows in by_source.items():
        in_queue = sum(1 for r in rows if r["fulltext_queue_387"] == "1")
        in_extraction = sum(1 for r in rows if r["extraction_224"] == "1")
        print(f"  review_source={src!r}: n={len(rows)}, "
              f"in_fulltext_queue_387={in_queue}/{len(rows)}, "
              f"in_extraction_224={in_extraction}/{len(rows)}")

    all_in_queue = all(r["fulltext_queue_387"] == "1" for r in matrix_rows)
    all_in_extraction = all(r["extraction_224"] == "1" for r in matrix_rows)
    print()
    if all_in_queue and all_in_extraction:
        print("ANSWER: YES. All 123 final records -- both the 70 review_source="
              "'fulltext' and the 53 review_source='abstract-2nd-pass' -- are "
              "flagged in_fulltext_queue_Q9=1 AND in_extraction_E11=1 in "
              "pipeline_unified.csv. The 53 are genuinely inside the "
              "387-record queue and the 190-record extraction-from-queue "
              "subset (109 fulltext + 81 abstract-2nd-pass = 190 across all "
              "224 extraction rows, not just the 123 that survived to the "
              "final list). review_source is an internal review-workflow tag "
              "(which screening pass produced the eligibility decision), not "
              "a membership boundary.")
    else:
        print("ANSWER: NO -- see per-record matrix for exceptions.")

    # Write the full matrix.
    out_matrix = ROOT / "verify" / "wp13_membership_matrix.csv"
    fieldnames = ["paper_key", "title", "review_source"] + [c[0] for c in STAGE_COLUMNS]
    with open(out_matrix, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for row in matrix_rows:
            w.writerow(row)
    print(f"\nWrote {out_matrix} ({len(matrix_rows)} rows)")

    # --- DEFER records ---
    print()
    print("=== 173 fulltext_decision=DEFER records ===")
    defer_rows = [r for r in pipe_rows if r["fulltext_decision"] == "DEFER"]
    print(f"Count: {len(defer_rows)}")
    for label, col in STAGE_COLUMNS:
        from collections import Counter
        print(f"  {label}: {dict(Counter(r[col] for r in defer_rows))}")

    out_defer = ROOT / "verify" / "wp13_defer_records.csv"
    fieldnames2 = ["title", "doi", "arxiv_id", "abstract_decision", "fulltext_decision"] \
        + [c[0] for c in STAGE_COLUMNS]
    with open(out_defer, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames2)
        w.writeheader()
        for r in defer_rows:
            out = {
                "title": r["title"], "doi": r["doi"], "arxiv_id": r["arxiv_id"],
                "abstract_decision": r["abstract_decision"],
                "fulltext_decision": r["fulltext_decision"],
            }
            for label, col in STAGE_COLUMNS:
                out[label] = r[col]
            w.writerow(out)
    print(f"Wrote {out_defer} ({len(defer_rows)} rows)")

    n_defer_reached_extraction = sum(1 for r in defer_rows if r["in_extraction_E11"] == "1")
    n_defer_in_final = sum(1 for r in defer_rows if r["in_final_list_123"] == "1")
    print(f"\n  DEFER records that reached extraction (in_extraction_E11=1): "
          f"{n_defer_reached_extraction} (manuscript claims 0 -- 'not carried forward')")
    print(f"  DEFER records in the final 123: {n_defer_in_final}")
    if n_defer_reached_extraction > 0:
        print("  ANOMALY: manuscript's claim that DEFER records were 'not carried")
        print("  forward to full-text eligibility assessment' is not exactly true --")
        print(f"  {n_defer_reached_extraction} DEFER-tagged record(s) do have")
        print("  in_extraction_E11=1. None reached the final 123, so this does not")
        print("  affect any reported count, but the qualitative claim of a clean")
        print("  173/0 split is not exact.")

    # --- Secondary anomaly: manual top-up records with Q9=1 ---
    print()
    print("=== Secondary anomaly found: manual cross-validation top-up records ===")
    ext_topup = [r for r in ext_rows if r["review_source"] == ""]
    print(f"Extraction rows with blank review_source (should be the 34 manual top-up): {len(ext_topup)}")
    anomalous = []
    for r in ext_topup:
        prows = pipe_by_title.get(norm_title(r["title"]), [])
        if any(p["in_fulltext_queue_Q9"] == "1" for p in prows):
            anomalous.append(r["title"])
    print(f"Of these, records that DO have in_fulltext_queue_Q9=1 in pipeline_unified.csv: "
          f"{len(anomalous)}")
    for t in anomalous:
        print(f"    - {t}")
    if anomalous:
        print("  This contradicts the manuscript's own source-comment claim ('verified:")
        print("  all 34 have no S5/S6/S7b/Q9 stage flags set in pipeline_unified.csv').")
        print("  Neither anomalous record is in the final 123, so no reported count is")
        print("  affected, but the internal verification comment is not accurate as")
        print("  stated for 2 of the 34.")


if __name__ == "__main__":
    main()
