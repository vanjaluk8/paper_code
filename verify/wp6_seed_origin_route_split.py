#!/usr/bin/env python3
"""
WP-6 / P1-2 -- Seed-origin attribution in Table 5.

Review finding: Table 5 books only 4 rows as "direct G0 seed" (S-LoRA,
AdapterHub, AdapterFusion, Petals), folding Houlsby (2019) and LoRA/Hu et al.
(2022) into the 105-row "targeted retrieval" (PREVALIDATED) bucket even
though both are G0 seed papers -- and each of the two appears TWICE in
pipeline_unified.csv (once via its arXiv record, once via its Scopus/DOI
record), tagged seed_group=G1 (LoRA) / G2 (Houlsby) rather than G0.

This script recomputes the Table 5 route split directly from
snowball_output/pipeline_unified.csv, treating those 4 Houlsby/LoRA rows as
seed-origin rather than targeted-retrieval, and reports the corrected split.

Usage: python3 verify/wp6_seed_origin_route_split.py
"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PIPELINE = ROOT / "snowball_output" / "pipeline_unified.csv"

# The two G0 seed papers whose final-list rows are bookkept outside G0
# (title match, case-insensitive substring; verified by hand against the
# pipeline file before hardcoding here).
SEED_PAPERS_BOOKKEPT_OUTSIDE_G0 = {
    "lora: low-rank adaptation of large language models",
    "parameter-efficient transfer learning for nlp",
}


def load_final_123():
    with open(PIPELINE, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    final = [r for r in rows if r["in_final_list_123"] == "1"]
    assert len(final) == 123, f"expected 123 final records, got {len(final)}"
    return final


def main():
    final = load_final_123()

    direction_counts = {}
    for r in final:
        direction_counts[r["direction"]] = direction_counts.get(r["direction"], 0) + 1

    print("Raw direction tally over the 123 final records:")
    for k, v in sorted(direction_counts.items()):
        print(f"  {k or '(blank)'}: {v}")
    raw_total = sum(direction_counts.values())
    print(f"  TOTAL: {raw_total}")
    assert raw_total == 123

    seed_direct = direction_counts.get("SEED", 0)
    snowball = direction_counts.get("FORWARD", 0) + direction_counts.get("BACKWARD", 0)
    prevalidated = direction_counts.get("PREVALIDATED", 0)

    # Find the Houlsby/LoRA duplicate rows inside the PREVALIDATED bucket.
    seed_duplicate_rows = [
        r for r in final
        if r["direction"] == "PREVALIDATED"
        and r["title"].strip().lower() in SEED_PAPERS_BOOKKEPT_OUTSIDE_G0
    ]
    print()
    print(f"Houlsby/LoRA rows found inside PREVALIDATED (should be 4: 2 papers x 2 rows each):")
    for r in seed_duplicate_rows:
        print(f"  seed_group={r['seed_group']:<4} arxiv_id={r['arxiv_id']:<12} doi={r['doi']:<20} title={r['title'][:50]}")
    n_seed_dup = len(seed_duplicate_rows)

    print()
    print("=== As currently reported in Table 5 (manuscript) ===")
    print(f"  Direct G0 seed:      {seed_direct}")
    print(f"  Targeted retrieval:  {prevalidated}   <- includes {n_seed_dup} Houlsby/LoRA seed-origin rows")
    print(f"  Snowball descendant: {snowball}")
    print(f"  SUM: {seed_direct + prevalidated + snowball}")

    corrected_seed = seed_direct + n_seed_dup
    corrected_targeted = prevalidated - n_seed_dup

    print()
    print("=== Corrected (seed-origin counted consistently) ===")
    print(f"  Seed-origin (direct + Houlsby/LoRA dup rows): {corrected_seed}")
    print(f"  Targeted retrieval (PREVALIDATED minus seed dups): {corrected_targeted}")
    print(f"  Snowball descendant: {snowball}")
    print(f"  SUM: {corrected_seed + corrected_targeted + snowball}")
    assert corrected_seed + corrected_targeted + snowball == 123

    # Cross-check against Table 2 / Table 3's own claim: "six seeds ... in
    # the final list", "eight seed-origin rows" (4 direct + 2 Houlsby rows +
    # 2 LoRA rows).
    print()
    print("Cross-check against manuscript Table 2/3 note ('six seeds, eight")
    print("seed-origin rows'):")
    print(f"  6 distinct seed papers = 4 direct (S-LoRA, AdapterHub, AdapterFusion,")
    print(f"  Petals) + Houlsby + LoRA  ->  matches" if seed_direct == 4 else "  MISMATCH")
    print(f"  8 seed-origin rows = {seed_direct} direct + {n_seed_dup} Houlsby/LoRA dup rows = {corrected_seed}"
          + ("  -> matches" if corrected_seed == 8 else "  -> MISMATCH"))


if __name__ == "__main__":
    main()
