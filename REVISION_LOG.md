# Revision Log — Decentralised Adapter-Based LLM Inference (SLR, MDPI *AI*)

Mapping every change made during the MDPI revision to the execution-plan item and
the file(s) touched. One row per change, newest first. Drives the
response-to-reviewers letter (Phase 4).

| # | Plan item | What changed | Files / commits | Status |
|---|---|---|---|---|
| 15 | **1.7** | Back matter: added `\acknowledgments{None.}` before `\conflictsofinterest`. ORCID encoding confirmed correct (`\orcidA{}` → orcid.org link). ⚠ Dep: `Definitions/logo-orcid.pdf` missing locally (template asset — restore or icon won't render/compile). | `main.tex` | ✅ Done (ORCID logo ⚠ dep) |
| 14 | **1.8** | Protocol-registration statement added at start of §3 (not prospectively registered; CS/AI SLRs not PROSPERO-eligible; no AI registry at commencement). Checklist 24a updated → §3. | `sections/03_methodology.tex`, `PRISMA_2020_checklist.md` (item 24a) | ✅ Done |
| 13 | **1.3** | Quality-appraisal rubric: added `§3.3 Quality Assessment` (6-dimension grounded rubric, 0–12, N=123, mean 7.17, bands 18/57/46/2); scoped-out & disclosed code-availability/baseline/threats (no grounded data → user-approved "Scope out, disclose"); new `\textstar` macro. | `sections/03_methodology.tex`, `main.tex`, `PRISMA_2020_checklist.md` (items 11 & 18), `slr_engine/snowballing/quality_appraisal.py` (new), figures `fig_slr_quality_bands.pdf` + `quality_appraisal_scored.csv` (local, regenerable) | ✅ Done |
| 12 | **1.1/1.4** | PRISMA funnel reconciled to single authoritative source (`PRISMA_NUMBERS_VALIDATION.md`); checklist/summary cleaned of stale refs. | `PRISMA_2020_checklist.md`, `PRISMA_summary_2026-04-21.md` | ✅ Done |
| 11 | **1.4** | Rebuilt full PRISMA 2020 flow figure (1,150→972→502→464→552→387→224→123/121 distinct) with per-stage exclusions. | `generate_prisma_figure.py`, `figures/fig_slr1_prisma_flow.pdf` (local) | ✅ Done |
| 10 | **1.3 (D5)** | Confirmed `S6_enriched_reading_pool.csv` `venue_quality` covers all 123 final records (63/47/11/2); full join via paper_key→arxiv/doi + title crosswalk. | data verification | ✅ Done |

## Number-consistency rule

The headline inclusion figure is **123 included records / 121 distinct papers**
(2 arXiv+Scopus duplicate key-pairs). Every funnel count appears in 7 places
(Abstract, §3.1, Table 1, Table A3, Fig 5 PRISMA, PRISMA checklist, PRISMA
summary) and must agree with the authoritative `PRISMA_NUMBERS_VALIDATION.md`.
