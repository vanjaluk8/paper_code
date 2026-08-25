# CLAUDE.md

> **Two-repo split (2026-08-21):** this repo (`papers_code`) holds the manuscripts,
> curated corpus (`papers_repo/`), and PRISMA package. The **`slr_engine/`** pipeline
> code moved to the sibling **`slr_engine`** repository. Paths below that mention
> `slr_engine/...` refer to that sibling checkout, not this repo.

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Research repository for a systematic literature review (SLR) on **Decentralized Adapter-Based LLM Systems** — specifically P2P multi-task NLP inference using PEFT adapters over a shared frozen transformer backbone. Affiliated with University of Rijeka, Faculty of Informatics and Digital Technologies.

The thesis synthesises three fields: **PEFT** (adapters/LoRA) · **P2P systems** · **multi-task NLP**.

## Running the Notebook

The original screening notebook now lives in `slr_engine/archive/main.ipynb` (archived — the active pipeline is the snowballing engine under `slr_engine/snowballing/`).

```bash
# Install dependencies
pip install -r slr_engine/snowballing/requirements.txt

# Launch the archived screening notebook
jupyter notebook slr_engine/archive/main.ipynb
```

The notebook expects WoS raw exports (`*.xls`) in `exports/wos/`. It must be run cell-by-cell in order.

## Repository Structure

| File/Dir | Purpose |
|---|---|
| `papers_repo/` | Paper curation: `lit-review-outline.md`, `G0_seed_papers.md`, `G1–G6_*.csv`, `WORKFLOW.md`, `research_topic.md`, methodology/validation references |
| `slr_engine/snowballing/` | Active automated pipeline: retrieval, screening, merge, enrichment, PRISMA, figures (run via `run_pipeline.sh`) |
| `slr_engine/snowballing/snowball_output/` | Intermediate pipeline CSVs/logs/PRISMA reports |
| `slr_engine/db_queries/` | Scopus and WoS advanced search query strings (`queries.sql`, `refined-queries-scopus-wos.md`) |
| `slr_engine/archive/` | Superseded earlier work (`main.ipynb`, `SLR_kostur.md`, `INTRO.md`, `papers_per_field.md`) |
| `slr_engine/assets/figures/` | Generated SLR figures (fig_slr1–9) |
| `writing/slr_methodology_paper/` | The paper itself: `latex_folder/` (LaTeX source + figures), `validation/`, `writing_materials/`, reference guides |

## Screening Pipeline (archived notebook — `slr_engine/archive/main.ipynb`)

1. **Convert** — `exports/wos/*.xls` → `*.csv`
2. **Load & merge** — all CSVs concatenated into one DataFrame
3. **Deduplicate** — on `Article Title` (~5,429 unique records)
4. **Screen** — keyword match on title + abstract → `screened_in` bool + `exclusion_reason`
5. **Tag** — classify into tiers: Tier 1 (PEFT + systems + LLM), Tier 2 (PEFT + LLM), Tier 3 (other)
6. **Export** — `screened_studies.csv` and `screened_studies_tagged.csv`

> The current, maintained pipeline is the python snowballing engine under `slr_engine/snowballing/`
> (see its `README.md`), not this archived notebook.

## Literature Review Status

Tracked in `papers_repo/lit-review-outline.md`. Critical gaps (🔴 Empty, Priority 1):
- **§6.1** Federated learning foundations (FedAvg, FedProx)
- **§7.1–7.2** MoE routing + adapter routing (SiRA, MoDE, Switch Transformers)
- **§4.3** Modular composition (Ponti 2023, LoraHub, AdapterSoup)
- **§9** PoC section (NL-to-SQL on MIMIC-III)

## Contribution Codes

Used throughout the outline to tag novel contributions:

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
- Snowball log in `papers_repo/lit-review-outline.md` Appendix B tracks G-groups (G0–G6) and read/unread status
- Figures referenced by number in outline; stored in `slr_engine/assets/figures/`
