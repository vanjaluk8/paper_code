#!/usr/bin/env python3
"""
WP-11 / D-2 -- Figure A3 (fig:venues) caption/content population mismatch.

The manuscript's caption claimed the figure plots the 464-record enriched
pool, "not the final 123-paper corpus" -- but the rendered figure's own
embedded pie chart reads "123 total" (Conference 83 / Journal 21 / Preprint
11 / Other 8), and its per-venue bars (EMNLP 13, ACL 12, arXiv 11, ICLR 8,
ICML 6, NeurIPS 5, ...) match the 123-record final reading list exactly, not
some larger 464-record population.

This script recomputes the per-venue counts directly from
snowball_output/13_final_reading_list_2026-05-12.csv to confirm the figure's
actual population and to derive the correct caption numbers.

Usage: python3 verify/wp11_figure_a3_venue_population.py
"""
import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
READING_LIST = ROOT / "snowball_output" / "13_final_reading_list_2026-05-12.csv"


def main():
    with open(READING_LIST, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 123
    venues = Counter(r["venue"].strip() for r in rows)

    emnlp = venues["Conference on Empirical Methods in Natural Language Processing"]
    acl = venues["Annual Meeting of the Association for Computational Linguistics"]
    arxiv = sum(c for v, c in venues.items() if "arxiv" in v.lower())
    iclr = venues["International Conference on Learning Representations"]
    icml = venues["International Conference on Machine Learning"]
    mlsys = sum(c for v, c in venues.items()
                if "machine learning and systems" in v.lower() or "mlsys" in v.lower())
    neurips = venues["Neural Information Processing Systems"]

    print("Computed directly from the 123-record final reading list:")
    print(f"  ACL + EMNLP combined: {acl} + {emnlp} = {acl + emnlp}")
    print(f"  arXiv (all spellings): {arxiv}")
    print(f"  ICLR: {iclr}")
    print(f"  ICML + MLSys combined: {icml} + {mlsys} = {icml + mlsys}")
    print(f"  NeurIPS: {neurips}")
    print()
    print("These exactly match the bars rendered in figures/fig_slr5_venues.pdf")
    print("(verified by visual inspection) and its embedded pie chart's")
    print("'123 total' label -- confirming the figure plots the 123-record")
    print("final corpus, not the 464-record enriched pool the old caption")
    print("claimed. The old caption's own per-venue numbers (arXiv 9, NeurIPS")
    print("8, ICML/MLSys 7) also did not match the rendered bars under either")
    print("population reading.")

    assert acl + emnlp == 25
    assert arxiv == 11
    assert iclr == 8
    assert icml + mlsys == 9
    assert neurips == 5


if __name__ == "__main__":
    main()
