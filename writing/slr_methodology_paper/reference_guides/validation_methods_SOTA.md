
# How to Validate Your SOTA Papers & Justify Seed Selection

## A.1 What your professor needs to see

Your supervisor requires two things for the literature review chapter:

1. **Provenance**: where did each paper come from? (database, search string, date)
2. **Inclusion justification**: why is each paper a seed? (selection criteria satisfied)

This maps to Items 6, 7, 8 of the PRISMA 2020 checklist (Information sources, Search
strategy, Selection process), which is the standard your faculty uses.

## A.2 The three legitimate sources for a seed paper

Each paper in `SEED_PAPERS.py` should be traceable to exactly one of these origins:

| Source code | Meaning | How to document it |
|-------------|---------|-------------------|
| `DB-WOS` | Found by keyword search in WoS | Record the exact query string + date + result set ID |
| `DB-ACL` | Found in ACL Anthology search | Record query + anthology collection name + date |
| `DB-SS` | Found in Semantic Scholar | Record query + date |
| `SNOW-B` | Found by backward snowballing from another seed | Record: "In reference list of [seed X], iteration N" |
| `SNOW-F` | Found by forward snowballing | Record: "Cited by [seed X] in WoS forward search, iteration N" |
| `PRIOR` | Known to you before search (expert knowledge / supervisor suggestion) | Must be explicitly stated and justified — *not* a problem, but must be declared |

## A.3 Seed selection criteria (for each paper, tick all that apply)

A paper qualifies as a seed if it meets **at least 2 of the 5 criteria** below.
Document your answer in the seed justification table (Section A.4).

| Criterion | Code | Description |
|-----------|------|-------------|
| Highly cited | **C1** | ≥ 100 citations OR ≥ 20 citations if published after 2022 |
| Venue quality | **C2** | Published in CCF-A/B venue, Q1 journal (SJR/JCR), or equivalent |
| Direct topic match | **C3** | Paper's main contribution intersects ≥ 2 of your 3 research pillars |
| Definitional/foundational | **C4** | Introduces or defines a core concept used in your thesis |
| Cited by supervisor | **C5** | Supervisor or thesis committee explicitly mentioned it |

## A.4 Seed Justification Table (fill this into your thesis appendix)

This is the table to present to your professor. One row per seed paper.

| # | Key | Title (short) | Venue | Year | Source | C1 | C2 | C3 | C4 | C5 | Notes |
|---|-----|--------------|-------|------|--------|----|----|----|----|----|-------|
| 1 | Houlsby 2019 | Parameter-Efficient Transfer Learning for NLP | ICML | 2019 | PRIOR | ✓ | ✓ | ✓ | ✓ | — | Foundational adapter paper; >5,700 citations |
| 2 | Hu 2022 LoRA | LoRA: Low-Rank Adaptation | ICLR | 2022 | PRIOR | ✓ | ✓ | ✓ | ✓ | — | >15,000 citations; defines LoRA used throughout |
| 3 | Pfeiffer 2020 Hub | AdapterHub | EMNLP | 2020 | PRIOR | ✓ | ✓ | ✓ | ✓ | — | Defines centralized adapter repo; P2P analog |
| 4 | Pfeiffer 2021 Fusion | AdapterFusion | EACL | 2021 | PRIOR | ✓ | ✓ | ✓ | ✓ | — | Core composition mechanism for MoA |
| 5 | Han 2024 Survey | PEFT Survey | TMLR | 2024 | DB-SS | ✓ | ✓ | ✓ | — | — | Positions thesis in PEFT landscape; 370+ refs |
| 6 | Borzunov 2022 Petals | Petals | NeurIPS | 2023 | PRIOR | ✓ | ✓ | ✓ | ✓ | — | Only deployed P2P LLM inference system |
| 7 | Sheng 2024 SLoRA | S-LoRA | MLSys | 2024 | DB-WOS | ✓ | ✓ | ✓ | — | — | Centralized serving baseline for comparison |
| 8 | Sajina 2024 P2P | Multi-task P2P NLP | FGCS | 2024 | PRIOR | — | ✓ | ✓ | ✓ | ✓ | Most closely related prior work; supervisor co-author |
| ... | | | | | | | | | | | |

> **Tip for your thesis chapter**: Write this paragraph once and reference the table:
> *"Seed papers were selected from the following sources: (1) papers known to the
> researcher through prior domain expertise (PRIOR); (2) papers retrieved by systematic
> keyword search in WoS Core Collection, ACL Anthology, and Semantic Scholar (DB-*);
> (3) papers identified through citation snowballing (SNOW-*). Each candidate seed
> was evaluated against five inclusion criteria (C1–C5). Papers satisfying ≥ 2 criteria
> were included. The full justification table is presented in Appendix X."*

## A.5 Search Strings to Document (Reproducibility)

Record these verbatim in your thesis methodology section.

**WoS Core Collection** — searched April 2026:
```
TS=("parameter-efficient fine-tuning" OR "adapter module" OR "LoRA") AND
TS=("peer-to-peer" OR "decentralized" OR "distributed inference") AND PY=(2019-2026)

TS=("adapter fusion" OR "mixture of adapters" OR "adapter composition") AND
TS=("multi-task" OR "task routing") AND PY=(2019-2026)

TS=("LoRA serving" OR "multi-tenant adapter" OR "adapter inference") AND PY=(2022-2026)
```

**ACL Anthology** (aclanthology.org) — full-text search, April 2026:
```
adapter composition multi-task
adapter routing inference
federated LoRA adapter
```

**Semantic Scholar** — April 2026:
```
"decentralized adapter inference"
"P2P fine-tuning transformer"
"mixture of LoRA adapters serving"
```

---