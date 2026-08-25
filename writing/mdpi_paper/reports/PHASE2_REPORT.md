# Phase 2 — Figure Pipeline Refresh & Reproducible Ground-Truth Report

Companion to `PHASE0_REPORT.md` and `PHASE1_REPORT.md`. Phase 2 scope: (1) make the
pipeline emit **vector PDF** figures (the paper uses `.pdf`, not `.png`), (2) refresh the
four pipeline figures the paper actually includes, and (3) fix one off-by-one in
`make_visuals.py`. Everything below was independently re-verified against the CSVs with a
proper CSV parser (not `wc -l`) before writing this report.

Project root (all paths relative to it): `writing/mdpi_paper/`. SLR engine home:
`slr_engine/snowballing/`.

---

## A. Applied (confirmed by inspection + regeneration)

### 1. `app/visualise.py` now emits vector PDF for every pipeline figure — `slr_engine/snowballing/app/visualise.py`

Each of the 8 figure blocks in `main()` that previously wrote only a `.png` now writes a
matching `.pdf` immediately after it, from the **same inputs** (matplotlib infers format
from the output extension; `matplotlib.use("Agg")` still produces vector PDF). Figures
covered: `fig_slr1_prisma_flow`, `fig_slr2_wave_productivity`, `fig_slr3_year_distribution`,
`fig_slr4_screening_funnel`, `fig_slr5_venues`, `fig_slr6_tier_breakdown`,
`fig_slr7_abstract_review`, `fig_slr9_final_breakdown`. The `.pdf` out-paths are at
`app/visualise.py:1485–1540`.

**How to reproduce:** from `slr_engine/snowballing/`, run `python -m app.visualise`. Output
goes to `slr_engine/assets/figures/`. After the change, that directory contains **PNG + PDF
for all 8** figures (verified present in `slr_engine/assets/figures/`, all dated
2026-08-21 12:37).

### 2. The four PDFs the paper uses are refreshed — `writing/mdpi_paper/figures/`

The paper references exactly 4 of the pipeline figures (verified via
`\includegraphics{figures/fig_*.pdf}` in `sections/` + `main.tex`):

| Figure | Paper ref | PDF size | Header |
|---|---|---|---|
| `fig_slr1_prisma_flow.pdf` | yes | 39,178 B | `%PDF-` |
| `fig_slr3_year_distribution.pdf` | yes | 29,215 B | `%PDF-` |
| `fig_slr5_venues.pdf` | yes | 32,777 B | `%PDF-` |
| `fig_slr6_tier_breakdown.pdf` | yes | 28,332 B | `%PDF-` |

All four are genuine vector PDFs (valid `%PDF-` magic header), regenerated 2026-08-21 12:37,
replacing the stale 2026-08-20 08:42 versions. Every included figure is present in
`writing/mdpi_paper/figures/` and referenced by an active `\includegraphics`. Content was
visually confirmed via rendered thumbnails (PRISMA flow, year chart, venue chart, tier
chart all render correctly).

`fig_slr2`, `fig_slr4`, `fig_slr7`, `fig_slr9` are **not** referenced by the paper, so they
were **not** copied in — they exist as PDFs in `slr_engine/assets/figures/` for future use.

### 3. Off-by-one fix — `slr_engine/snowballing/make_visuals.py`

The "Preprint separation & source tagging" PRISMA-stage row and the file-inventory row both
hard-coded **42** for the arXiv manual-follow-up count. Corrected to **43** in two places
(`make_visuals.py` line 39 and line 151).

**Ground truth:** `slr_engine/snowballing/snowball_output/12_arxiv_for_manual_search.csv`
contains **43 data rows** (verified with the `csv` module, i.e. minus the 1 header row). The
stage row now reads `224 → n_out 181 → n_drop 43` (224 − 181 = 43, internally consistent).

**Scope note:** the user's rule was "align with the paper; if it isn't cited, remove it."
This number is **not cited anywhere in the paper's `.tex`**, so **no `.tex` text changed** —
only the script's hard-coded literals were aligned to the authoritative 43-row CSV.

---

## B. Flagged for review (NOT changed — outside approved scope)

These were surfaced while re-verifying the ground truth for this report. None were edited.

### B1. PRISMA figure content vs. methodology caption describe different funnels — `sections/03_methodology.tex`

The **figure caption** (lines 75–80) and the **methodology prose** (lines 28–36) narrate the
S-shaped funnel `1,150 → 972 → 502 → 464 → 552 → 387 → 224 → 123`, naming stages **502, 387,
and 224**. But the **rendered `fig_slr1_prisma_flow.pdf`** shows a different top-of-funnel
branch and **does not draw the 502 / 387 / 224 boxes at all**:

Rendered in the PDF: `1,150 raw → 972 (178 dup removed) → 972 title-screen → 791 excluded →
181 LLM-triage → 60 excluded → 162 eligible → 464 enriched (T1 90 / T2 141 / T3 233) → 552
abstract review (214 KEEP / 338 SKIP / 0 DEFER) → 123 final (T1 48 / T2 42 / T3 33)`.

The appendix (`sections/12_appendix.tex` §C.2, lines 630–634) is consistent with the
**figure's** branch (`972 → 162 INCL / 791 EXCL / 19 UNCERT`; `cross-dedup 514 → 502`), but the
**caption** names 502/387/224 which the figure never shows. **Recommendation:** either redesign
`fig1_prisma` to draw the full 502→387→224 chain (matching the caption), or trim the caption to
the stages the figure actually renders (464→552→123). Left untouched because it changes figure
content, not just its file format.

### B2. G0 count inconsistent across paper — "eight" vs "9"

- `sections/03_methodology.tex:21` — "anchored on **eight** foundational seed papers (G0)"
- `sections/03_methodology.tex:52` (Table) — "**G0 & 9**"
- `fig_slr1_prisma_flow.pdf` — "Citation snowballing on G0 seeds (**n = 8**)"

PHASE0/PHASE1 established the ground truth **G0 = 9** (`G0_seed_papers.md` and the S7b SEED
pool both = 9). So line 21 "eight" and the figure's "n = 8" disagree with the table (9).
**Recommendation:** change line 21 "eight" → "nine", and fix the figure's G0 box to `n = 9`.
Left untouched (figure G0 label is baked into `fig1_prisma`; text line is a prose edit).

### B3. Commented-out dead figure reference — `sections/02_background.tex:168–174`

A fully commented-out figure block (`\begin{figure}[H]` … `\end{figure}`, every line prefixed
`%`) references `figures/fig_concept_marketplace.png`, which is **absent** from
`writing/mdpi_paper/figures/`. Because it is commented out it is **not compiled** and does
**not** break the build (verified: the only occurrence is inside the comment). The file exists
at `slr_engine/assets/figures/fig_concept_marketplace.png` if the author wants to re-enable it.
Clean-up only; no compile impact.

---

## C. Ground-truth reconciled (CSV-parser verified, header row excluded)

These are the authoritative numbers backing the applied changes and the flags above,
computed with Python's `csv` module across `slr_engine/snowballing/snowball_output/`:

| File | Data rows | Stage it maps to |
|---|---|---|
| `S2_snowball_raw_candidates.csv` | **972** | 972 after dedup |
| `S3_title_screened_all.csv` | **972** | 972 title-screened |
| `S4_title_screened_included.csv` | **162** | 162 eligible (fig branch) |
| `S5_merged_corpus.csv` | **502** | 502 merged (caption/prose) |
| `S6_enriched_reading_pool.csv` | **464** | 464 enriched |
| `S7b_abstract_reviewed_final.csv` | **552** | 552 abstract-reviewed |
| `13_final_reading_list_2026-05-12.csv` | **123** | 123 final list |
| `12_arxiv_for_manual_search.csv` | **43** | 43 → arXiv follow-up |

Notes for the validator:
- `1,150` pre-dedup is **not** a CSV row count — it is the figure's own stated raw-retrieval
  number (PRISMA 2020 requires reporting it). The CSV-verifiable chain is
  `972 → 502 → 464 → 552 → 123`, all of which the CSVs confirm.
- The **43** in `make_visuals.py` is confirmed against the 43-row CSV (this validates the
  application in §A.3).
- The figure's tier sub-totals (T1 90 / T2 141 / T3 233 for 464; T1 48 / T2 42 / T3 33 for
  123) were read from the rendered PDF and are reported here as observed, not independently
  re-derived in this phase.

---

## D. Final structural verification

- All 4 used figures present in `writing/mdpi_paper/figures/` and referenced by an **active**
  (non-commented) `\includegraphics` — **0 missing active includes**.
- `app/visualise.py` re-runs cleanly (`python -m app.visualise`) and regenerates PNG+PDF for
  all figures in `slr_engine/assets/figures/`.
- Pipeline figure-wide verification ends: the authoritative funnel numbers [Included 464 |
  Reviewed 552 | Final 123] hold in the regenerated corpus.
- **Compile note:** no local LaTeX toolchain; "compiles" is verified structurally
  (refs/includes/envs) rather than via pdflatex. Final Overleaf compile must still be run by
  the user to pick up the refreshed figure PDFs.

**Consistency caveat carried from Phase 1:** the PRISMA narrative has two live branches — the
caption/prose S-funnel (`502/387/224`) and the figure branch (`791/181/162`) — plus the G0
8-vs-9 wrinkle. These are itemised in §B and deliberately left for review; resolving them
(so figure, caption, prose, and appendix all tell one funnel) is the recommended Phase 3.
