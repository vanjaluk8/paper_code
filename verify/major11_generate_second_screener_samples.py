#!/usr/bin/env python3
"""
Major #11 -- generate the two blind second-screener samples.

Draws a fixed-seed 10% random sample from (a) the 552-record abstract-review
pool and (b) the 387-record full-text queue, for an independent second
screener to blindly re-screen. Produces, per sample: a blind sheet (no prior
decision visible) and a separate original-decisions file (kept apart so the
blind sheet can actually be sent to a screener without leaking the original
disposition).

Usage: python3 verify/major11_generate_second_screener_samples.py
"""
import csv
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SEED = 20260912  # fixed, recorded here for reproducibility


def write_blind_sheet(path, rows):
    fieldnames = ["blind_id", "title", "authors", "year", "venue", "abstract",
                  "second_screener_decision", "second_screener_notes"]
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for i, r in enumerate(rows, 1):
            w.writerow({
                "blind_id": f"S{i:03d}",
                "title": r.get("title", ""),
                "authors": r.get("authors", ""),
                "year": r.get("year", ""),
                "venue": r.get("venue", ""),
                "abstract": r.get("abstract", ""),
                "second_screener_decision": "",
                "second_screener_notes": "",
            })


def write_original_decisions(path, rows, decision_field):
    fieldnames = ["blind_id", "title", "doi", "arxiv_id", "first_screener_decision"]
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for i, r in enumerate(rows, 1):
            w.writerow({
                "blind_id": f"S{i:03d}",
                "title": r.get("title", ""),
                "doi": r.get("doi", ""),
                "arxiv_id": r.get("arxiv_id", ""),
                "first_screener_decision": r.get(decision_field, ""),
            })


def main():
    with open(ROOT / "snowball_output" / "S7b_abstract_reviewed_final.csv", encoding="utf-8-sig") as f:
        abstract_pool = list(csv.DictReader(f))
    assert len(abstract_pool) == 552

    with open(ROOT / "snowball_output" / "pipeline_unified.csv", encoding="utf-8-sig") as f:
        pipe = list(csv.DictReader(f))
    fulltext_queue = [r for r in pipe if r.get("in_fulltext_queue_Q9") == "1"]
    assert len(fulltext_queue) == 387

    rng1 = random.Random(SEED)
    sample_abstract = rng1.sample(abstract_pool, 55)

    rng2 = random.Random(SEED)
    sample_fulltext = rng2.sample(fulltext_queue, 39)

    v = ROOT / "verify"
    write_blind_sheet(v / "major11_second_screener_abstract_sample_blind.csv", sample_abstract)
    write_blind_sheet(v / "major11_second_screener_fulltext_sample_blind.csv", sample_fulltext)
    write_original_decisions(v / "major11_second_screener_abstract_sample_original_decisions.csv",
                              sample_abstract, "inclusion")
    write_original_decisions(v / "major11_second_screener_fulltext_sample_original_decisions.csv",
                              sample_fulltext, "fulltext_decision")

    print(f"Seed used: {SEED}")
    print(f"Abstract-pool sample: {len(sample_abstract)} of {len(abstract_pool)} (10.0%)")
    print(f"Full-text-queue sample: {len(sample_fulltext)} of {len(fulltext_queue)} (10.1%)")


if __name__ == "__main__":
    main()
