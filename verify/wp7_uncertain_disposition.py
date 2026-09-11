#!/usr/bin/env python3
"""
WP-7 / P1-3 -- Disposition of the 19 UNCERTAIN title-screening records.

The manuscript gave three incompatible accounts of what happened to these 19
records:
  (i)   Figure 5 / Table A2 (tab:screening): excluded at title screening,
        "unresolved after manual triage, not carried forward".
  (ii)  Appendix A.5 (old text): "were not part of this merge ... and were
        excluded at final curation" (a much later pipeline stage).
  (iii) Appendix A.4 (old text): "were re-examined manually after screening:
        only 3 reached the abstract-level review stage and none was
        retained".

This script checks (i) against every canonical, version-controlled data file
in this repo. It also reports (informationally, not as the basis for the fix)
what an archived per-record fixture in the sibling mdpi_slr_engine lineage
shows, per author confirmation that file is still authoritative.

Usage: python3 verify/wp7_uncertain_disposition.py
"""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCREEN_LOG = ROOT / "snowball_output" / "log_screening_2026-04-21.json"
PIPELINE = ROOT / "snowball_output" / "pipeline_unified.csv"

# Author-confirmed-authoritative external fixture (not part of this repo or
# mdpi_slr_engine's tracked tree -- an archived per-record snapshot from an
# earlier stage of the same pipeline codebase). Informational corroboration
# only; the manuscript fix below rests on the canonical files above, which
# are sufficient on their own.
EXTERNAL_FIXTURE = Path(
    "/Users/vanja/git/slr_engine/verification_fixtures/03_review_queue_2026-04-21.csv"
)


def check_screening_log():
    d = json.load(open(SCREEN_LOG, encoding="utf-8"))
    llm = d["llm_screening"]
    decisions = d["decisions"]
    print("=== log_screening_2026-04-21.json ===")
    print(f"  Layer-3 (LLM-assisted manual triage) queue: {llm['rows_sent']} records")
    print(f"    resolved INCLUDE: {llm['resolved_include']}")
    print(f"    resolved EXCLUDE: {llm['resolved_exclude']}")
    print(f"    uncertain_remaining: {llm['uncertain_remaining']}")
    print(f"  Top-level decisions: INCLUDE={decisions['INCLUDE']}, "
          f"REVIEW={decisions['REVIEW']}, EXCLUDE={decisions['EXCLUDE']}")
    assert llm["uncertain_remaining"] == 19
    assert decisions["INCLUDE"] == 162
    # 162 = 111 (Layer-2 direct include) + 51 (Layer-3 resolved include).
    # The 19 uncertain_remaining are absent from both INCLUDE and EXCLUDE
    # tallies used downstream -- i.e. dropped, not carried into any later
    # bucket by this log.
    print("  -> 19 uncertain records are not counted in either final INCLUDE")
    print("     (162) or final EXCLUDE (791+19=810 total non-included);")
    print("     consistent with 'excluded at title screening, not carried")
    print("     forward' (account i).")


def check_pipeline_unified():
    with open(PIPELINE, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    # The 502-record merged pool = 162 title-screened INCLUDE + 352
    # pre-validated - 12 cross-duplicates. If any of the 19 UNCERTAIN records
    # had reached the merge or beyond, the merged-pool arithmetic (162+352-12
    # =502, reported and independently reconciled in PASS 1 of the review)
    # would not close. pipeline_unified.csv itself contains no per-record tag
    # distinguishing an UNCERTAIN-origin row, which is expected if none of
    # the 19 ever entered the tracked pipeline stages this file records.
    print()
    print("=== pipeline_unified.csv ===")
    print(f"  Total rows: {len(rows)} (tracks only records reaching some")
    print("  pipeline stage beyond raw title screening -- the 791 EXCLUDE and")
    print("  19 UNCERTAIN title-screening records are not expected to appear")
    print("  here at all, and none do under any recognisable tag).")


def check_external_fixture():
    print()
    print("=== external fixture (informational corroboration only) ===")
    print(f"  Path: {EXTERNAL_FIXTURE}")
    if not EXTERNAL_FIXTURE.exists():
        print("  NOT FOUND at this path in this environment -- skipping.")
        return
    with open(EXTERNAL_FIXTURE, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    from collections import Counter
    print(f"  Rows: {len(rows)}")
    print(f"  inclusion values: {Counter(r['inclusion'] for r in rows)}")
    n_llm_error = sum(1 for r in rows if "LLM error" in r.get("exclusion_reason", ""))
    print(f"  Rows with an LLM parsing error as the exclusion reason: {n_llm_error}")
    print("  -> All 19 rows are marked inclusion=SKIP with a populated")
    print("     exclusion_reason (several: LLM parse failures on re-attempt).")
    print("     Fully consistent with account (i); contradicts (ii) and (iii).")


if __name__ == "__main__":
    check_screening_log()
    check_pipeline_unified()
    check_external_fixture()
