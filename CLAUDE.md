# CLAUDE.md

> **Two-repo split (2026-08-21):** this repo (`mdpi_paper_slr`) holds the MDPI
> manuscript (`main.tex`, `sections/`, `Definitions/`, `bibliography.bib`), the
> curated corpus (`papers_repo/`), and the PRISMA/supplementary package
> (`supplementary/`). The **`slr_engine/`** pipeline code lives in the sibling
> **`slr_engine`** repository (`../slr_engine`), not this repo. Paths below that
> mention `slr_engine/...` refer to that sibling checkout unless stated otherwise.

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Research repository for a systematic literature review (SLR) on **Decentralized Adapter-Based LLM Systems** — specifically P2P multi-task NLP inference using PEFT adapters over a shared frozen transformer backbone, reported as a manuscript for the MDPI *AI* journal. Affiliated with University of Rijeka, Faculty of Informatics and Digital Technologies.

The review synthesises three fields: **PEFT** (adapters/LoRA) · **P2P systems** · **multi-task NLP**.

> **Note.** All pipeline/screening code lives in the sibling **`slr_engine`** repo
> (`../slr_engine`). This repo is the manuscript + curated corpus + submission
> package only; it contains no runnable screening code.

## Repository Structure (this repo)

| File/Dir | Purpose |
|---|---|
| `main.tex` | MDPI `AI` manuscript root (class, title/abstract, DAS, supplementary, bibliography, appendices); `\input`s `sections/*`. |
| `sections/` | Manuscript body: `01_introduction` … `09_synthesis_gap`, `11_conclusion`, `12_appendix`. |
| `Definitions/` | MDPI LaTeX class + assets (`mdpi.cls`, `*.bst`, `*.sty`, logos). |
| `bibliography.bib` | Manuscript bibliography. |
| `figures/` | Figure sources (HTML + source CSVs). Compiled PDFs are regenerable from `slr_engine` and gitignored. |
| `supplementary/` | Submission bundle: S1 (PRISMA 2020 checklist), S2 (quality-appraisal scores CSV), supporting data, search exports, cover letter. See `supplementary/README.md`. |
| `papers_repo/` | **Curated literature corpus** — G0–G6 seed/corpus CSVs (352-paper pre-validated corpus) + `G0_seed_papers.md`. Promised publicly in the manuscript DAS. Author working/draft notes (`lit-review-outline.md`, methodology outlines, workflow/research notes) were removed in the reorg — recoverable from git history. |
| `build/` | Bundle/compile tooling (`compile_mdpi.sh`). |
| `supplementary/queries.sql` | Scopus / WoS advanced search query strings (mirrored from `slr_engine/db_queries/`). |
| `REVISION_STATUS.md`, `VALIDATION_NOTE.md` | Author-side working docs (excluded from the submission package; see `supplementary/README.md`). |

## Related work in the sibling `slr_engine` repo

| Path (in `../slr_engine`) | Purpose |
|---|---|
| `snowballing/` | Active automated pipeline: retrieval, screening, merge, enrichment, PRISMA, figures (run via `run_pipeline.sh`). |
| `snowballing/snowball_output/` | Intermediate pipeline CSVs / logs / PRISMA reports (authoritative funnel numbers). |
| `db_queries/` | Scopus and WoS advanced search query strings (`supplementary/queries.sql`, `refined-queries-scopus-wos.md`). |
| `archive/` | Superseded earlier work (`main.ipynb`, `SLR_kostur.md`, `INTRO.md`, `papers_per_field.md`). |
| `assets/figures/` | Generated SLR figures (fig_slr1–9). |
| `scripts/` | Verification scripts (`verify_prisma_counts.py`, `verify_quality_appraisal.py`). |

## Literature Review Status

The working literature-review outline (`lit-review-outline.md`) that tracked
section status and gaps was **removed in the reorg** (recoverable from git
history) — the review's live content now lives in the manuscript itself
(`sections/*.tex`). Earlier tracked critical gaps (🔴 Empty, Priority 1) for
reference:
- **§6.1** Federated learning foundations (FedAvg, FedProx)
- **§7.1–7.2** MoE routing + adapter routing (SiRA, MoDE, Switch Transformers)
- **§4.3** Modular composition (Ponti 2023, LoraHub, AdapterSoup)
- **§9** PoC section (NL-to-SQL on MIMIC-III)

## Contribution Codes

Novel contributions, consistently tagged in the outline and referenced in the manuscript's §3.3 Quality Assessment:

| Code | Description |
|---|---|
| ★A1 | Adapter discovery protocol (DHT + capability embeddings) |
| ★S1 | P2P adapter marketplace framework |
| ★R1/★R2 | Adapter capability/behavioural embeddings |
| ★T2 | Reuse bounds under non-IID distributions |
| ★M2 | Decentralised AdapterFusion without central coordinator |

## Key Conventions

- Citation style: Harvard numbered — LaTeX `\citep{}` / `\citet{}`
- Section status emoji: 🟢 Drafted · 🟡 Partial · 🔴 Empty
- The G0–G6 snowball groups (with read/unread status) were logged in the now-removed `lit-review-outline.md` Appendix B (git history); group data lives in the `papers_repo/G*-*` CSVs here and `slr_engine`.
- Figures: compiled PDFs referenced in `sections/*.tex` are regenerated from `slr_engine`; their sources live in `figures/` here. The outline's figure numbering maps to `slr_engine/assets/figures/`.
