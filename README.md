# mdpi_paper_slr — Decentralised Adapter-Based LLM Inference: An SLR (manuscript + curated corpus)

The **manuscript & curated-corpus half** of a two-repo split for the systematic
literature review on **decentralised adapter-based LLM inference**:

- **This repo (`mdpi_paper_slr`)** — the MDPI *AI* manuscript (`main.tex`, `sections/`,
  `bibliography.bib`), the curated literature corpus (`papers_repo/`), the PRISMA
  package (`supplementary/`), and the MDPI class files (`Definitions/`).
- **`mdpi_slr_engine`** (sibling repo, `../mdpi_slr_engine`, github.com/vanjaluk8/mdpi_slr_engine) — the
  snowballing/search/screening/extraction/PRISMA/figures pipeline that generates
  the numbers and figures this manuscript reports.

> **Provenance:** the funnel numbers and figure PDFs in the manuscript are
> produced by `mdpi_slr_engine`. Its `data/` snapshot mirrors the canonical
> `papers_repo/G*-*` CSVs here. The extraction spreadsheet (`11_data_extraction_*.csv`)
> is pipeline-derived and kept local, not versioned.

## Layout

| Path | Purpose |
|---|---|
| `main.tex` | The MDPI *AI* manuscript root — document class, title/author/abstract, data-availability & supplementary statements, bibliography, appendices. Includes `sections/*.tex`. |
| `sections/` | The manuscript body: `01_introduction` … `09_synthesis_gap`, `11_conclusion`, `12_appendix`. |
| `bibliography.bib` | The manuscript bibliography (MDPI numbered style). |
| `Definitions/` | The MDPI LaTeX class and assets (`mdpi.cls`, `*.bst`, `*.sty`, logos). |
| `figures/` | Figure sources (HTML/CSV) referenced by the manuscript; the compiled **PDFs are regenerable from `mdpi_slr_engine` and gitignored** (see `.gitignore`). |
| `supplementary/` | The MDPI submission bundle — S1 (PRISMA 2020 checklist), S2 (quality-appraisal scores), supporting data, search exports, and the cover letter. See `supplementary/README.md`. |
| `build/` | Build tooling: `compile_mdpi.sh`. |
| `papers_repo/` | **Curated literature corpus** — G0–G6 seed/corpus CSVs (the 352-paper pre-validated corpus). Promised publicly by the manuscript's Data Availability statement. Author working/draft notes (methodology outlines, `lit-review-outline.md`, workflow/research notes) were removed in the reorg — recoverable from git history. |
| `REVISION_STATUS.md` | Working log of manuscript revisions (author-side; not part of the submission package). |
| `VALIDATION_NOTE.md` | Working note on number/figure validation (author-side; not part of the submission package). |
| `supplementary/queries.sql` | Scopus / WoS advanced search query strings. |

## The PRISMA package (in `supplementary/`)
- `supplementary/S1_PRISMA_2020_checklist.md` — 27-item checklist mapping.
- `supplementary/PRISMA_summary_2026-04-21.md` — per-stage pipeline summary.
- `supplementary/S2_quality_appraisal_scored.csv` — per-study quality-appraisal
  scores underlying §3.4. The **authoritative funnel/validation numbers** are
  produced by the `mdpi_slr_engine` scripts `verify_prisma_counts.py` /
  `verify_quality_appraisal.py` and their outputs are version-controlled in
  `mdpi_paper_slr` under `snowball_output/` (see the manuscript's Data Availability
  statement).

## Submission package
To build a LaTeX submission, zip the repo root **excluding** `papers_repo/`,
`REVISION_STATUS.md`, `VALIDATION_NOTE.md`, `build/`, and anything under
`_archive/` — i.e. `main.tex`, `sections/*.tex`, `figures/*.pdf`,
`Definitions/`, `bibliography.bib`, and the `supplementary/` bundle. See
`supplementary/README.md` for the full submission checklist.

## Compile note
No local LaTeX toolchain is committed here; the PDFs are compiled on Overleaf. The
manuscript figure PDFs are regenerable from `mdpi_slr_engine` and kept local (gitignored).
