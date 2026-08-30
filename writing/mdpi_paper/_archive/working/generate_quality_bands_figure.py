#!/usr/bin/env python3
"""Regenerate `fig_slr_quality_bands.pdf` from ground truth.

Fix for Blocking Issue #4b/#5 (MDPI AI resubmission audit, 2026-08-30):
the previous fig_slr_quality_bands.pdf plotted an 18/57/46/2 distribution
under an invalid 0-12-scale banding (10-12/7-9/4-6/0-3), which does not
match the 0-10 rubric defined in Table 4 (Q1-Q4+Q6, Q5 scored separately)
and does not match the Section 3.4 prose (13/61/47/2, mean 6.04, SD 2.00,
bands 9-10/6-8/3-5/0-2). The prose was independently verified correct via
slr_engine/slr_engine/snowballing/scripts/verify_quality_appraisal.py; this
script regenerates the figure to match it exactly rather than hand-editing
the chart.

Output: <repo>/writing/mdpi_paper/figures/fig_slr_quality_bands.pdf
"""
import csv
import statistics
from pathlib import Path

import matplotlib
matplotlib.use("PDF")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
FIGURES = HERE.parent.parent / "figures"
CSV_PATH = FIGURES / "quality_appraisal_scored.csv"
OUT = FIGURES / "fig_slr_quality_bands.pdf"

BAND_ORDER = ["High (9-10)", "Upper-mid (6-8)", "Lower-mid (3-5)", "Low (0-2)"]
BAND_COLORS = {
    "High (9-10)": "#2e7d32",
    "Upper-mid (6-8)": "#8bc34a",
    "Lower-mid (3-5)": "#f0ad2c",
    "Low (0-2)": "#c62828",
}


def band(total):
    if 9 <= total <= 10:
        return "High (9-10)"
    if 6 <= total <= 8:
        return "Upper-mid (6-8)"
    if 3 <= total <= 5:
        return "Lower-mid (3-5)"
    return "Low (0-2)"


def main():
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    scores = [int(r["q1"]) + int(r["q2"]) + int(r["q3"]) + int(r["q4"]) + int(r["q6"]) for r in rows]
    n = len(scores)
    mean = statistics.mean(scores)
    sd = statistics.stdev(scores)

    counts = {b: 0 for b in BAND_ORDER}
    for s in scores:
        counts[band(s)] += 1

    assert counts == {"High (9-10)": 13, "Upper-mid (6-8)": 61, "Lower-mid (3-5)": 47, "Low (0-2)": 2}, counts
    print("Verified band counts:", counts, f"(N={n}, mean={mean:.2f}, SD={sd:.2f})")

    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    xs = list(range(len(BAND_ORDER)))
    heights = [counts[b] for b in BAND_ORDER]
    colors = [BAND_COLORS[b] for b in BAND_ORDER]
    bars = ax.bar(xs, heights, color=colors, width=0.6, edgecolor="none")

    for x, h in zip(xs, heights):
        ax.text(x, h + 1.2, str(h), ha="center", va="bottom", fontsize=11, fontweight="bold")

    ax.set_xticks(xs)
    ax.set_xticklabels(BAND_ORDER, fontsize=9.5)
    ax.set_ylabel("Papers", fontsize=10)
    ax.set_title(f"Reporting-completeness score distribution (N = {n}, score 0–10)",
                 fontsize=11, fontweight="bold")
    ax.set_ylim(0, max(heights) * 1.22)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    fig.savefig(OUT, bbox_inches="tight", pad_inches=0.05)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
