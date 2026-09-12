#!/usr/bin/env python3
"""Major-17: compute the core/background split of the final 123-record corpus,
to formalise the inclusion rule's discriminating stratification per the
review's suggested fix (use the corpus: core/background field already in the
extraction data, Table 6 / tab:extraction_codebook)."""
import csv
from collections import Counter

SRC = "snowball_output/13_final_reading_list_2026-05-12.csv"


def main():
    with open(SRC, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    counts = Counter(r["corpus"].strip() for r in rows)
    total = len(rows)
    print(f"{total} final records")
    for label, n in counts.items():
        print(f"  {label}: {n} ({n / total * 100:.1f}%)")


if __name__ == "__main__":
    main()
