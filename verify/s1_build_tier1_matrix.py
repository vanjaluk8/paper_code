#!/usr/bin/env python3
"""Blocking 3 / S-1: merge the author's final per-dimension scores
(s1_tier1_author_decisions.json, made interactively against all 48 Tier-1
records) with the corpus metadata into the published concept-matrix
extension, and report the k=1..7 distribution the review asked for."""
import csv
import json
from collections import Counter

SCAFFOLD = "verify/s1_tier1_concept_matrix_scaffold.csv"
DECISIONS = "verify/s1_tier1_author_decisions.json"
OUT = "verify/s1_tier1_concept_matrix_scored.csv"

DIMS = [
    "frozen_backbone", "adapter_exchange", "p2p_topology", "discovery",
    "multi_task_fusion", "privacy_dp", "no_central_coordinator",
]
SYM = {"yes": "✓", "partial": "(✓)", "no": "×", "na": "−"}


def main():
    scaffold = list(csv.DictReader(open(SCAFFOLD, newline="", encoding="utf-8")))
    decisions = json.load(open(DECISIONS))

    rows = []
    dist = Counter()
    for s in scaffold:
        key = s["paper_key"].strip()
        is_excluded = decisions["excluded"].get(key, False)
        score = decisions["scores"].get(key, {})
        row = {
            "paper_key": key,
            "title": s["title"],
            "year": s["year"],
            "excluded_from_matrix": is_excluded,
        }
        k = 0
        k_partial = 0.0
        for d in DIMS:
            v = score.get(d, "no")
            row[d] = SYM[v]
            if v == "yes":
                k += 1
                k_partial += 1
            elif v == "partial":
                k_partial += 0.5
        row["k_strict"] = k
        row["k_with_partial"] = k_partial
        rows.append(row)
        if not is_excluded:
            dist[k] += 1

    with open(OUT, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["paper_key", "title", "year", "excluded_from_matrix"] + DIMS + ["k_strict", "k_with_partial"]
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)

    scored = sum(1 for r in rows if not r["excluded_from_matrix"])
    print(f"{scored} scored ({len(rows) - scored} excluded as survey/framework)")
    for k in range(8):
        print(f"  k={k}: {dist.get(k, 0)}")


if __name__ == "__main__":
    main()
