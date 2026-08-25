# SLR Workflow — Decentralized Adapter-Based LLM Systems

**Author:** Vanja Luk, University of Rijeka, Faculty of Informatics and Digital Technologies  
**Topic:** P2P multi-task NLP inference using PEFT adapters over a shared frozen transformer backbone  
**Standard:** PRISMA 2020

---

## Overview

The literature review is structured in three sequential phases:

| Phase | Activity | Automation |
|---|---|---|
| 1 | Manual seed curation + pre-validated corpus assembly | None |
| 2 | Automated citation snowballing, screening, enrichment | Fully automated (4 APIs + LLM) |
| 3 | Interactive abstract review + Zotero export | Semi-automated (LLM-assisted) |

---

## Phase 1 — Seed Curation and Pre-Validated Corpus

### 1.1 Seed papers (G0)

Seven foundational papers were hand-selected as snowballing seeds, covering the three core fields of the thesis:

| Paper | Relevance |
|---|---|
| Houlsby et al. (2019) | Adapter layers for NLP |
| Hu et al. (2021) — LoRA | Low-rank adaptation |
| Pfeiffer et al. (2020, 2021) | AdapterFusion, MAD-X |
| Han et al. (2024) | PEFT survey |
| Sheng et al. (2024) — S-LoRA | Batched LoRA inference |
| Borzunov et al. (2023) — Petals | P2P inference over shared backbone |
| Sajina (2023, 2024) | P2P adapter marketplace concept |

These are stored in `G0_seed_papers.md` and are the starting point for citation snowballing in Phase 2.

### 1.2 Pre-validated paper groups (G1–G6)

Beyond the seeds, 343 additional papers were curated manually and organized into six thematic groups:

| Group | Topic | File |
|---|---|---|
| G1 | PEFT methods beyond adapters and LoRA | `papers_repo/G1_*.csv` |
| G2 | Adapter composition for multi-task NLP | `papers_repo/G2_*.csv` |
| G3 | Decentralized and P2P machine learning | `papers_repo/G3_*.csv` |
| G4 | Adapter multiplexing for efficient LLM inference | `papers_repo/G4_*.csv` |
| G5 | Routing and MoE for modular PEFT transformers | `papers_repo/G5_*.csv` |
| G6 | Federated PEFT for transformer NLP | `papers_repo/G6_*.csv` |

Each CSV has columns: title, authors, year, journal/venue, DOI, abstract, citation count, relevance score.

These papers are treated as ground truth — they bypass all automated screening filters in Phase 2.

---

## Phase 2 — Automated Citation Snowballing Pipeline

### Entry point

```bash
cd slr_engine/snowballing/
bash run_pipeline.sh [--engine ss|scopus|acl|ieee|all] [--no-llm]
```

This script executes eight numbered steps in sequence, producing immutable intermediate CSV files. Each step reads from the previous step's output, so the entire pipeline is reproducible and crash-safe.

---

### Step 1 — Venue Resolution (optional pre-processing)

**Script:** `app/resolve_venues.py`  
**Purpose:** For papers in G1–G6 that carry only an arXiv ID, query Semantic Scholar to fill in the journal/conference venue name.  
**When to run:** Before Step 2, when the G*.csv files contain blank venue fields.

---

### Step 2 — Import Pre-Validated Corpus

**Script:** `main.py --import-corpus`  
**Input:** `G0_seed_papers.md` + `papers_repo/G1–G6_*.csv`  
**Output:** `snowball_output/00_prevalidated_YYYY-MM-DD.csv` (343 papers)

All G0–G6 papers are parsed, normalized, and written to a single CSV. This becomes the baseline corpus against which snowball discoveries are deduplicated.

---

### Step 3 — Citation Snowballing

**Script:** `main.py --engine all`  
**Input:** G0 seeds (7 papers)  
**Output:** `snowball_output/01_raw_YYYY-MM-DD.csv` + `log_retrieval_YYYY-MM-DD.json`

For each G0 seed paper, the pipeline performs:
- **Backward snowballing:** retrieves the seed's reference list (papers it cites)
- **Forward snowballing:** retrieves papers that cite the seed

This is executed across four academic search engines:

| Engine | API | Provides |
|---|---|---|
| Semantic Scholar | Free graph API | References + forward citations (uncapped) |
| Scopus | Elsevier API (key required) | References + citations (≤25 per query on Starter tier) |
| ACL Anthology | Free metadata API | ACL paper metadata (pairs with Semantic Scholar for citations) |
| IEEE Xplore | IEEE API (key required) | Metadata + citation count |

All four engines are queried and their results are merged. Duplicates are resolved in priority order: DOI → arXiv ID → Semantic Scholar paper ID. The raw output contains 974 unique candidate papers.

---

### Step 4 — Title Screening

**Script:** `app/screen.py --llm`  
**Input:** `01_raw_YYYY-MM-DD.csv`  
**Output:** `02_screened_*.csv`, `03_review_queue_*.csv`, `04_included_*.csv`, `log_screening_*.json`

Each candidate paper passes through a three-layer filter:

**Layer 1 — Hard exclusion filters**
- Year < 2021 → EXCLUDE
- Citation count below per-year threshold → EXCLUDE

**Layer 2 — Keyword scoring on title**

The title is checked against four term sets:

| Term set | Example keywords |
|---|---|
| `peft` | adapter, LoRA, fine-tuning, PEFT, prefix-tuning |
| `systems` | P2P, decentralized, federated, distributed, routing |
| `llm` | language model, transformer, BERT, GPT |
| `distributed` | peer-to-peer, gossip, DHT, overlay network |

- Matches in 2+ term sets → **INCLUDE** (automatically)
- Match in 1 term set (systems, peft, or distributed only) → **REVIEW** (borderline)
- LLM-only match → **EXCLUDE** (too broad)
- No match → **EXCLUDE**

**Layer 3 — LLM triage (for REVIEW queue only)**

Papers flagged as REVIEW are sent to `claude-haiku-4-5-20251001` with their title and venue. The model returns one of: `relevant` → INCLUDE, `irrelevant` → EXCLUDE, `uncertain` → placed in manual review queue.

**Screening results:**
- 164 papers → INCLUDE (automatic)
- 27 papers → manual review queue (`03_review_queue_*.csv`)
- 783 papers → EXCLUDE

The review queue CSV is edited by hand: change the `inclusion` column, save, and re-run the screening step to fold manual decisions into `04_included_*.csv`.

---

### Step 5 — Merge Corpora

**Script:** `app/merge.py` (via `main.py --merge`)  
**Input:** `00_prevalidated_*.csv` + `04_included_*.csv`  
**Output:** `05_merged_YYYY-MM-DD.csv` (534 papers)

The pre-validated corpus (343 papers, Phase 1) is combined with the screened snowball discoveries (191 papers). Deduplication is applied again on DOI / arXiv ID / SS paper ID to ensure no paper appears twice.

---

### Step 6 — Abstract Enrichment and Relevance Filtering

**Script:** `enrich_and_filter.py`  
**Input:** `05_merged_*.csv`  
**Output:** `06_enriched_*.csv`, `07_filtered_*.csv`, `07_excluded_*.csv`, `07_deprioritized_*.csv`

**Enrichment:**
- Missing abstracts are fetched in bulk via Semantic Scholar Batch API, with OpenAlex as fallback
- Keywords are retrieved from OpenAlex
- Venue quality is classified: `top_venue` / `peer_reviewed` / `preprint` / `unknown`
- All API results are cached in `.enrich_cache.json` for crash-safe resumability

**Tier classification** (applied to every paper):

| Tier | Condition | Count |
|---|---|---|
| 1 | PEFT + systems/distributed + LLM signals (all three) | 91 |
| 2 | Any two of the three signals | 141 |
| 3 | One or zero signals (foundational / tangential) | 232 |

**Relevance filtering:**
- Papers outside the NLP domain (e.g., pure computer vision or audio) → `07_excluded_*.csv`
- Low-citation arXiv preprints without Tier-1 signals → `07_deprioritized_*.csv` (rescue pool)
- Pre-validated papers (G0–G6) bypass domain filters

**Final reading list:** `07_filtered_*.csv` — 464 papers sorted by tier then citation count.

---

### Step 7 — PRISMA 2020 Summary

**Script:** `app/prisma.py`  
**Input:** All intermediate CSVs from Steps 2–6  
**Output:** `PRISMA_summary_YYYY-MM-DD.md`

Generates a PRISMA 2020-compliant audit report including:
- Six-stage flowchart with record counts at each decision point
- Formal inclusion/exclusion criteria table
- Venue quality breakdown
- Per-seed snowball productivity table
- Exclusion reason histogram

---

### Step 8 — Figure Generation

**Script:** `app/visualise.py` (via `main.py --visualise`)  
**Input:** `07_filtered_*.csv` + `PRISMA_summary_*.md`  
**Output:** `slr_engine/assets/figures/fig_slr{1–8}_*.png`

Eight publication-quality figures (matplotlib, 180 DPI, colorblind-safe palette):

| Figure | Content |
|---|---|
| fig_slr1 | PRISMA 2020 flowchart |
| fig_slr2 | Papers per seed, backward vs. forward breakdown |
| fig_slr3 | Publication year distribution, stacked by G-group |
| fig_slr4 | Exclusion funnel |
| fig_slr5 | Top venues, conference/journal/preprint ratio |
| fig_slr6 | Tier distribution + citation count box plot per tier |
| fig_slr7 | Abstract review decisions per tier (generated after Phase 3) |
| fig_slr8 | Papers per G-group by outlet type |

---

## Phase 3 — Interactive Abstract Review

**Script:** `python -m app.abstract_review --llm`  
**Input:** `07_filtered_*.csv` (464 papers)  
**Output:** `08_abstract_reviewed_*.csv`, `08_zotero_ready_*.ris`

The researcher reads each abstract in a terminal UI. Before each abstract, Claude Sonnet (pre-fetched in background) provides a one-sentence summary and a suggested decision.

**Keymap:**
- `k` / Enter → KEEP
- `s` → SKIP
- `d` → DEFER (revisit later)
- `b` → Undo last decision
- `q` → Quit and save

All KEEP + DEFER papers are exported as a `.ris` file, which is imported directly into Zotero (File → Import → select the `.ris` file).

After Phase 3, steps 7 and 8 are re-run to update the PRISMA flowchart and fig_slr7 with abstract-level decision counts.

---

## Data Flow Summary

```
papers_repo/
  G0_seed_papers.md              7 seed papers (hand-curated)
  G1–G6_*.csv                    343 pre-validated papers

          │
          ▼  Step 2: import
00_prevalidated_*.csv            350 papers

          │
          ▼  Step 3: snowball (4 engines × 2 directions)
01_raw_*.csv                     974 candidate papers

          │
          ▼  Step 4: keyword screening + LLM triage
02_screened_*.csv                974 papers with inclusion decision
03_review_queue_*.csv            27 borderline papers (manual edit)
04_included_*.csv                191 papers passing screening

          │
          ▼  Step 5: merge with pre-validated corpus
05_merged_*.csv                  534 unique papers

          │
          ▼  Step 6: enrich abstracts + tier classification
06_enriched_*.csv                534 papers with abstracts + keywords
07_filtered_*.csv                464 papers (final reading list, tier-sorted)
07_deprioritized_*.csv           32 low-signal preprints (rescue pool)
07_excluded_*.csv                7 off-topic exclusions (audit trail)

          │
          ▼  Steps 7–8: reporting
PRISMA_summary_*.md              PRISMA 2020 audit report
slr_engine/assets/figures/       SLR figures (fig_slr1–8)

          │
          ▼  Phase 3: abstract review
08_abstract_reviewed_*.csv       464 papers with KEEP/SKIP/DEFER decisions
08_zotero_ready_*.ris            Final corpus for Zotero
```

---

## Key Design Decisions

**Immutable intermediate files** — each step writes a new dated CSV and never modifies prior outputs. Any step can be re-run independently without corrupting earlier results.

**Crash-safe API caching** — enrichment and LLM suggestion results are cached to disk. Interrupting and restarting any API-heavy step continues from where it left off.

**Pre-validated papers bypass screening** — G0–G6 papers were curated with expert judgment. Subjecting them to automated keyword filters would risk excluding foundational works with unusual terminology (e.g., "Petals" for P2P inference).

**LLM triage is bounded** — Claude is invoked only for the 27-paper REVIEW queue in Step 4 and for generating reading suggestions in Phase 3. It does not make final inclusion decisions; those are either deterministic (keyword rules) or human (abstract review).

**Four-engine search reduces engine bias** — Semantic Scholar and Scopus have different citation graph coverage. ACL Anthology provides authoritative metadata for NLP papers. IEEE Xplore covers hardware-adjacent systems work. Using all four increases recall.

---

## Repository Structure

```
litreview-peft-p2p-adapters/
├── CLAUDE.md                      # Project instructions
├── papers_repo/
│   ├── lit-review-outline.md      # Thesis outline with section status
│   ├── G0_seed_papers.md
│   └── G1–G6_*.csv
└── slr_engine/
    └── snowballing/
        ├── run_pipeline.sh        # Master pipeline script
        ├── main.py                # CLI entry point
        ├── enrich_and_filter.py   # Step 6 standalone script
        ├── app/
        │   ├── seeds.py           # Parse G0 from markdown
        │   ├── core.py            # Snowball orchestration
        │   ├── screen.py          # Title screening + LLM triage
        │   ├── merge.py           # Step 5 merge + dedup
        │   ├── corpus_loader.py   # G0–G6 loader + tier classification
        │   ├── abstract_review.py # Phase 3 interactive tool
        │   ├── resolve_venues.py  # Venue label enrichment
        │   ├── visualise.py       # SLR figures (matplotlib)
        │   ├── prisma.py          # PRISMA 2020 report
        │   ├── enrich_wos.py      # Optional WoS enrichment
        │   ├── models.py          # Paper dataclass
        │   ├── storage.py         # CSV I/O + dedup logic
        │   ├── config.py          # Environment + config loading
        │   ├── .env               # API keys (gitignored)
        │   └── engines/
        │       ├── semantic_scholar.py
        │       ├── scopus.py
        │       ├── acl_anthology.py
        │       ├── ieee_xplore.py
        │       └── wos.py
        └── snowball_output/
            ├── 00_prevalidated_*.csv
            ├── 01_raw_*.csv
            ├── 02_screened_*.csv
            ├── 03_review_queue_*.csv
            ├── 04_included_*.csv
            ├── 05_merged_*.csv
            ├── 06_enriched_*.csv
            ├── 07_filtered_*.csv
            ├── 07_deprioritized_*.csv
            ├── 07_excluded_*.csv
            ├── log_retrieval_*.json
            ├── log_screening_*.json
            ├── PRISMA_summary_*.md
            └── .enrich_cache.json
```
