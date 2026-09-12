#!/usr/bin/env python3
"""
S-1 -- generate the empty concept-matrix scoring scaffold for the 48 Tier-1
final-corpus records, keyed by record ID with the seven Table 10 dimension
columns, ready for the author to fill in.

Usage: python3 verify/s1_generate_tier1_scaffold.py
"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIMENSIONS = [
    "frozen_backbone", "adapter_exchange", "p2p_topology", "discovery",
    "multi_task_fusion", "privacy_dp", "no_central_coordinator",
]


def main():
    with open(ROOT / "snowball_output" / "13_final_reading_list_2026-05-12.csv",
              encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    tier1 = [r for r in rows if r["tier"] == "1"]
    assert len(tier1) == 48

    out_path = ROOT / "verify" / "s1_tier1_concept_matrix_scaffold.csv"
    fieldnames = ["paper_key", "title", "authors", "year", "venue", "doi", "arxiv_id"] \
        + DIMENSIONS + ["notes"]
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in tier1:
            row = {k: r[k] for k in ["paper_key", "title", "authors", "year", "venue", "doi", "arxiv_id"]}
            for d in DIMENSIONS:
                row[d] = ""
            row["notes"] = ""
            w.writerow(row)

    print(f"Wrote {out_path}: {len(tier1)} rows x {len(fieldnames)} columns")


if __name__ == "__main__":
    main()
