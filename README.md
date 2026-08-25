# papers_code — Decentralised Adapter-Based LLM SLR (manuscripts, curated corpus & evidence)

The **literature / manuscript half** of a two-repo split for the SLR on
**decentralised adapter-based LLM inference**:

- **This repo (`papers_code`)** — manuscripts (MDPI paper + thesis), the curated
  corpus & methodology materials (`papers_repo/`), and the PRISMA package
  (checklist, summary, verified-numbers table, audit reports).
- **`slr_engine`** (sibling repo) — the snowballing/search/screening/extraction/PRISMA/figures pipeline that generates the numbers and figures this manuscript reports.

## Layout

| Path | Purpose |
|---|---|
| `papers_repo/` | Curated literature: G0–G6 seed/corpus CSVs, `G0_seed_papers.md`, methodology outlines, `WORKFLOW.md`, reference notes |
| `writing/mdpi_paper/` | The MDPI *AI* journal article: `main.tex`, `sections/`, `bibliography.bib`, PRISMA checklist/summary, `PRISMA_NUMBERS_VALIDATION.md`, audit `reports/` |
| `writing/slr_methodology_paper/` | The thesis / SLR-progress LaTeX version + writing materials |

> **Provenance:** the funnel numbers and figure PDFs in the manuscript are produced
> by `slr_engine` (its `data/` snapshot mirrors the canonical `papers_repo/G*-*` CSV
> here). The extraction spreadsheet (`11_data_extraction_*.csv`) is pipeline-derived
> and kept local, not versioned.

## The PRISMA package
- `writing/mdpi_paper/PRISMA_2020_checklist.md` — 27-item checklist mapping.
- `writing/mdpi_paper/PRISMA_summary_2026-04-21.md` — per-stage pipeline summary.
- `writing/mdpi_paper/PRISMA_NUMBERS_VALIDATION.md` — **single authoritative funnel
  table** (all numbers cross-checked against `slr_engine/snowball_output/`).

## Compile note
No local LaTeX toolchain is committed here; the PDFs are compiled on Overleaf. The
manuscript figure PDFs are regenerable from `slr_engine` (`python -m app.visualise`)
and kept locally (gitignored).
