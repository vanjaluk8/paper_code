#!/usr/bin/env python3
"""Generate `fig_slr1_prisma_flow.pdf` — a PRISMA 2020 flow diagram.

Single source of truth for every number is `PRISMA_NUMBERS_VALIDATION.md`
(which cross-checks each value against the pipeline CSVs). This script is a
small, self-contained reporting tool that produces the standard PRISMA 2020
flow figure used as Figure~5 in `writing/mdpi_paper`. The centre chain is drawn
exactly as the manuscript prose and caption describe it:

    1,150 -> 972 -> 502 -> 464 -> 552 -> 387 -> 224 -> 123 (120 distinct)

Standard PRISMA 2020 exclusion-reason boxes are attached to every junction for
which a validated count exists.

Output: <repo>/writing/mdpi_paper/figures/fig_slr1_prisma_flow.pdf
"""

import matplotlib
matplotlib.use("PDF")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "figures" / "fig_slr1_prisma_flow.pdf"

# ---------------------------------------------------------------------------
# Verified numbers (see PRISMA_NUMBERS_VALIDATION.md, section A)
# ---------------------------------------------------------------------------
N_RAW        = "1,150"   # databases/registers (450 backward + 700 forward)
N_OTHER      = "352"     # other methods: pre-validated G0-G6 curation
N_DUP        = "178"     # duplicates removed before screening
N_SCREEN     = "972"     # records screened (title level)
N_TITLE_EXCL = "791"     # 731 (Layer-2 keyword) + 60 (LLM triage)
N_TITLE_731  = "731"
N_TITLE_60   = "60"
N_MERGE      = "502"     # merged w/ pre-validated + title screening (514->502)
N_MERGE_DUP  = "12"      # removed in cross-dedup during merge
N_ENRICH     = "464"     # enrichment + tier filter
N_ENRICH_EXCL= "38"      # 6 off-topic + 32 deprioritised
N_ENRICH_6   = "6"
N_ENRICH_32  = "32"
N_ABS        = "552"     # abstract review (two passes + forward snowball)
N_ABS_SKIP   = "165"     # abstract-level SKIP
N_FULLTEXT   = "387"     # reports sought for retrieval (full-text queue)
N_NORETR     = "265"     # reports not retrieved (no PDF); 122 yes / 265 no
N_EXTRACT    = "224"     # reports assessed for eligibility (data extraction)
N_FINAL      = "123"     # studies included in review
N_DISTINCT   = "120"     # distinct papers

# ---------------------------------------------------------------------------
# Layout constants
# ---------------------------------------------------------------------------
COL_MAIN   = "#e3ecf6"   # main-flow fill
COL_HEAD   = "#cfe0f2"   # identification / highlighted
COL_EXCL   = "#f4e8da"   # exclusion / side boxes
COL_EDGE   = "#2f4f72"
COL_TEXT   = "#1c2b3a"
COL_EXCLT  = "#7a4f1d"

CX = 0.34           # centre-column x
SX = 0.80           # side (exclusion) column x
W  = 0.46           # main box width
SW = 0.34           # side box width
SPACING = 0.112     # vertical pitch between box centres (~9 rows in 0..1)
FS  = 9.0
FSX = 8.0
FS_STAGE = 9.0

# box titles (bold first line) and optional sub-lines, one entry per stage
STAGES = [
    # (stage-label, title, sub, n, colour)
    ("Identification",
     "Records identified from databases & registers",
     "backward 450 + forward 700", N_RAW, COL_HEAD),
    (None,
     "Records identified via other methods",
     "pre-validated G0-G6 curation", N_OTHER, COL_HEAD),
    ("Screening",
     "Records screened (title level)",
     None, N_SCREEN, COL_MAIN),
    (None,
     "Records after merge with pre-validated corpus",
     "title screening (514→502)", N_MERGE, COL_MAIN),
    (None,
     "Records after enrichment + tier filter",
     None, N_ENRICH, COL_MAIN),
    ("Eligibility (abstract)",
     "Records after abstract review",
     "two passes + forward snowball", N_ABS, COL_MAIN),
    ("Eligibility (full-text)",
     "Reports sought for retrieval",
     "full-text queue (KEEP 214 + DEFER 173)", N_FULLTEXT, COL_MAIN),
    (None,
     "Reports assessed for eligibility",
     "data extraction (190 auto + top-up)", N_EXTRACT, COL_MAIN),
    ("Included",
     "Studies included in review",
     "{0} distinct papers".format(N_DISTINCT), "{0} ({1})".format(N_FINAL, N_DISTINCT),
     "#d9ead8"),
]

# (source-stage-index, [side-box lines...]) for the exclusion boxes
EXCLUSIONS = [
    (1, ["Records removed before screening:",
         "duplicates (n = {0})".format(N_DUP)]),
    (2, ["Records excluded (title screening):",
         "keyword/year (n = {0})".format(N_TITLE_731),
         "LLM triage (n = {0})".format(N_TITLE_60)]),
    (3, ["Records removed (cross-dedup during merge):",
         "n = {0}".format(N_MERGE_DUP)]),
    (4, ["Records excluded (enrichment / tier filter):",
         "off-topic (n = {0})".format(N_ENRICH_6),
         "deprioritised (n = {0})".format(N_ENRICH_32)]),
    (5, ["Records excluded (abstract SKIP):",
         "n = {0}".format(N_ABS_SKIP)]),
    (6, ["Reports not retrieved (no PDF):",
         "n = {0} not retrieved / {1} retrieved".format(N_NORETR, "122")]),
]

fig, ax = plt.subplots(figsize=(11.5, 8.8))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

# centre y of each of the 9 main boxes
cy = [0.96 - i * SPACING for i in range(9)]   # 0.96 .. 0.064


def h_of(lines):
    return 0.096 + 0.030 * max(lines - 1, 0)


def arrow(x1, y1, x2, y2):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>",
                                 mutation_scale=13, linewidth=1.2,
                                 color=COL_EDGE, zorder=1))


# ---------------------------------------------------------------------------
# Main column boxes + vertical connectors
# ---------------------------------------------------------------------------
for i, (stage, title, sub, n, color) in enumerate(STAGES):
    x = CX
    y = cy[i]
    nlines = 2 if sub else 1
    h = h_of(nlines)
    ax.add_patch(FancyBboxPatch((x - W / 2, y - h / 2), W, h,
                                boxstyle="round,pad=0.010,rounding_size=0.016",
                                linewidth=1.2, edgecolor=COL_EDGE,
                                facecolor=color, zorder=2))
    ax.text(x, y + (0.028 if sub else 0.0), title, ha="center", va="center",
            fontsize=FS, fontweight="bold", color=COL_TEXT, zorder=3)
    # count on the right inside the box
    ax.text(x + W / 2 - 0.012, y, "n = " + n, ha="right", va="center",
            fontsize=FS, color=COL_TEXT, zorder=3, fontweight="bold")
    if sub:
        ax.text(x, y - h / 2 + 0.020, sub, ha="center", va="bottom",
                fontsize=FS - 0.8, color=COL_TEXT, zorder=3, style="italic")
    # vertical connector into this box (skip the very first)
    if i > 0:
        arrow(x, cy[i - 1] - h_of(2 if STAGES[i - 1][2] else 1) / 2,
              x, y + h / 2)

# stage labels on the left margin
for i, (stage, *_rest) in enumerate(STAGES):
    if stage is None:
        continue
    ax.text(0.045, cy[i], stage, ha="center", va="center",
            fontsize=FS_STAGE, fontweight="bold", color="#5a7590", zorder=1)

# ---------------------------------------------------------------------------
# Exclusion boxes on the right
# ---------------------------------------------------------------------------
for src_idx, lines in EXCLUSIONS:
    y = cy[src_idx]
    n = len(lines)
    h = h_of(n)
    ax.add_patch(FancyBboxPatch((SX - SW / 2, y - h / 2), SW, h,
                                boxstyle="round,pad=0.010,rounding_size=0.014",
                                linewidth=1.0, edgecolor=COL_EXCLT,
                                facecolor=COL_EXCL, zorder=2))
    for j, ln in enumerate(lines):
        yy = y + h / 2 - 0.022 - j * 0.026
        ax.text(SX, yy, ln, ha="center", va="center", fontsize=FSX,
                color=COL_EXCLT, zorder=3)
    # connector from main box to exclusion box
    arrow(CX + W / 2, y, SX - SW / 2, y)

fig.tight_layout()
fig.savefig(OUT, bbox_inches="tight")
print("wrote", OUT)
