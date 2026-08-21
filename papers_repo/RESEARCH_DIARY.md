# Research Diary — Decentralised Adapter-Based LLM Systems SLR

**Author:** Vanja Luk  
**Affiliation:** University of Rijeka, Faculty of Informatics and Digital Technologies  
**Governing framework:** PRISMA 2020 · Wohlin (2014) snowballing · Xiao & Watson (2019) 8-step SLR

---

## 2026-04-14 — Initial corpus import

**Action:** First import of pre-validated G1–G6 corpora into the pipeline.

**What was done:**
- Imported all six thematic groups (G1–G6) assembled via Undermind AI-assisted queries anchored on G0 seed papers
- Generated first version of prevalidated corpus (`00_prevalidated_2026-04-14.csv`)
- G0 seeds: 9 hand-selected foundational papers covering PEFT, P2P inference, and multi-task LLM serving

**Outcome:** Initial pipeline run; corpus import confirmed working. File superseded on 2026-04-17.

---

## 2026-04-17 — Prevalidated corpus update

**Action:** Updated G1–G6 corpora with corrected venue names and citation counts.

**What was done:**
- Re-ran corpus import after correcting venue attribution in G1–G6 CSV files
- Generated `00_prevalidated_2026-04-17.csv` (superseded by 2026-04-21 version)

**Outcome:** Improved metadata quality before the main snowballing run.

---

## 2026-04-21 — Full snowballing pipeline run + abstract review

**Action:** Complete pipeline execution — snowballing, screening, enrichment, and abstract-level review.

**What was done:**
1. **Snowballing** (Wohlin 2014 — backward + forward on G0 seeds):
   - Retrieved candidates via Semantic Scholar, Scopus, and ACL Anthology APIs
   - 1,150 raw records retrieved; 41 unique new records after deduplication
   - Merged with 444 pre-validated papers → 485 entering screening

2. **Title screening** (3-layer: year filter → keyword scoring → LLM triage):
   - 825 excluded; 183 passed (auto-INCLUDE + REVIEW promotions)
   - Merged corpus: 464 papers after enrichment and relevance filtering

3. **Enrichment and tier classification:**
   - Abstracts retrieved via Semantic Scholar batch API and OpenAlex
   - Tier classification applied (Tier 1: PEFT + Systems + LLM; Tier 2: two signals; Tier 3: one signal)
   - Result: 464 papers (T1=90, T2=141, T3=233)

4. **Abstract-level review** (Keshav 2007 first-pass model):
   - All 464 papers reviewed at abstract level using interactive screener with Claude Sonnet suggestions
   - Decisions: KEEP=202, SKIP=93, DEFER=169
   - DEFER = papers requiring closer inspection before final inclusion/exclusion

**Key files produced:**
- `S1_prevalidated_corpus.csv` — 350 pre-validated papers (G0-G6)
- `S2_snowball_raw_candidates.csv` — 974 raw snowball candidates
- `S3_title_screened_all.csv` — full screening decisions
- `S6_enriched_reading_pool.csv` — 464 enriched, tier-classified papers
- `S7a_abstract_reviewed_base.csv` — original abstract review (KEEP=202, DEFER=169, SKIP=93)

**Limitation noted:** DEFER papers (n=169) not yet resolved; saturation assessed manually via G1–G6 overlap rather than iterative snowballing to zero (Wohlin 2014 Lesson 7 limitation).

---

## 2026-05-02 — Full-text review of downloaded papers + DEFER resolution

**Action:** Full-text review using Claude Sonnet on downloaded PDFs; DEFER→SKIP decision.

**What was done:**
- Conducted full-text review on papers where PDFs were available locally
- Reviewed DEFER papers (n=169) with closer attention; decided all DEFER → SKIP (none warranted full inclusion after closer reading)
- Downloaded remaining PDFs not yet available locally (identified gap for next phase)

**Decisions:**
- DEFER resolution: all 169 DEFER → SKIP (confirmed out of scope after closer review)
- Updated abstract review file includes 88 additional papers sourced from initial Scopus forward snowballing run
- Final abstract review state: KEEP=214, SKIP=338, DEFER=0

**Key files produced:**
- `S7b_abstract_reviewed_final.csv` — canonical abstract review (KEEP=214, SKIP=338, DEFER=0)

---

## 2026-05-08 — Manual forward snowballing (Scopus + WoS)

**Action:** Validated forward citation chains on priority seeds via Scopus and Web of Science.

**What was done:**
- Ran forward snowballing on priority G0 seeds (Wohlin 2014 §3.2.2 forward procedure)
- Scopus: searched citing papers for each G0 seed using Scopus Advanced Search (DOI field)
- WoS: used Times Cited links and Cited Reference Search for seeds not indexed in WoS
- Screened results by title and abstract against inclusion criteria

**Databases used:** Scopus (Elsevier), Web of Science Core Collection

**Key files produced:**
- `M1_forward_scopus_2026-05-08.csv` — raw Scopus forward snowball export (106 papers)
- `M2_forward_wos_2026-05-08.txt` — raw WoS forward snowball export

**Outcome:** Relevant papers from this search were incorporated into the abstract review pool (reflected in `S7b_abstract_reviewed_final.csv`).

---

## 2026-05-11 — Manual database searches for venue validation (Scopus + WoS)

**Action:** Searched Scopus and WoS by title to confirm database indexing for papers in the reading pool.

**What was done:**
- Ran manual title searches in Scopus and WoS to:
  - Confirm papers are indexed in recognised academic databases (Scopus Q1 / WoS SCIE)
  - Update `source` attribution (Scopus or WoS > arXiv where both exist)
  - Retrieve accurate citation counts and venue metadata
- Scopus export: 208 papers matched and exported with full metadata
- WoS export: matching papers exported for cross-reference

**Rationale:** Mentor guideline — Scopus and WoS take precedence over arXiv as recognised sources; provenance must be documented (PRISMA 2020 Item 7).

**Key files produced:**
- `M3_scopus_venue_validation_2026-05-11.csv` — Scopus title-search export (208 papers)
- `M4_wos_venue_validation_2026-05-11.txt` — WoS title-search export

---

## 2026-05-12 — ArXiv venue validation + final reading list assembled

**Action:** Validated venues for arXiv-only papers; assembled the definitive final reading list.

**What was done:**
1. **ArXiv venue validation:**
   - Identified 43 papers in the reading pool with arXiv as the only source
   - Searched Scopus and WoS by title/DOI to find published versions
   - Updated venue attribution where published conference/journal versions existed
   - Result: arXiv-only papers reduced to ~9% of the final list

2. **Final reading list assembled** (`S8_final_reading_list.csv`):
   - 123 papers confirmed for inclusion
   - Tier breakdown: T1=48 (39%), T2=42 (34%), T3=33 (27%)
   - Corpus role: core=89, background=34
   - Source: SCOPUS=101 (82%), ARXIV=18 (15%), other=4 (3%)
   - G-group attribution: G0=20, G1=12, G2=15, G3=11, G4=12, G5=9, G6=29, Other=15

3. **Pipeline documentation updated:**
   - PRISMA summary regenerated (`PRISMA_summary.md`)
   - All SLR figures regenerated (fig1–fig9)
   - Superfluous intermediate CSV files deleted; remaining files renamed with meaningful names

**Key files produced:**
- `M5_arxiv_venue_validation.csv` — arXiv venue validation decisions (43 papers)
- `S8_final_reading_list.csv` — **definitive 123-paper reading list**
- `PRISMA_summary.md` — updated PRISMA audit trail

**Current status:** Reading phase begins. `read_status` column in `S8_final_reading_list.csv` to be updated as papers are read (values: `read`, `done`, or blank).

---

## Pipeline File Index

| File | Stage | Description |
|------|-------|-------------|
| `S1_prevalidated_corpus.csv` | Stage 1 | G0–G6 pre-validated corpus (350 papers) |
| `S2_snowball_raw_candidates.csv` | Stage 2 | Raw snowball output (974 candidates) |
| `S3_title_screened_all.csv` | Stage 3 | Full title screening decisions |
| `S4_title_screened_included.csv` | Stage 4 | Title-screened inclusions |
| `S5_merged_corpus.csv` | Stage 5 | Pre-validated + snowball merged |
| `S6_enriched_reading_pool.csv` | Stage 6 | Enriched, tier-classified pool (464) |
| `S6b_excluded_offtopic.csv` | Stage 6 | Off-topic exclusions |
| `S6c_deprioritized_lowcite.csv` | Stage 6 | Low-citation preprints (rescue pool) |
| `S7a_abstract_reviewed_base.csv` | Stage 7 | Original manual abstract review (DEFER=169) |
| `S7b_abstract_reviewed_final.csv` | Stage 7 | **Canonical** — DEFER resolved (KEEP=214, SKIP=338) |
| `S8_final_reading_list.csv` | Stage 8 | **Canonical** — 123-paper final reading list |
| `M1_forward_scopus_2026-05-08.csv` | Manual | Scopus forward snowball raw export |
| `M2_forward_wos_2026-05-08.txt` | Manual | WoS forward snowball raw export |
| `M3_scopus_venue_validation_2026-05-11.csv` | Manual | Scopus venue validation export |
| `M4_wos_venue_validation_2026-05-11.txt` | Manual | WoS venue validation export |
| `M5_arxiv_venue_validation.csv` | Manual | ArXiv venue validation decisions |
| `log_retrieval_2026-04-21.json` | Log | Per-seed snowball retrieval counts |
| `log_screening_2026-04-21.json` | Log | Keyword/LLM screening audit log |
| `PRISMA_summary.md` | Report | PRISMA 2020 process summary |
