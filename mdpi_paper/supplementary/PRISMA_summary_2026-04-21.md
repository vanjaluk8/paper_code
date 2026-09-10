# PRISMA Process Summary

**Generated:** 2026-05-12 19:42 UTC  
**Search executed:** 2026-04-21  
**Databases:** ACL, SS, SCOPUS, IEEE  
**Candidates file:** `01_raw_2026-04-21.csv`  
**SHA-256:** `6dae981905ba20d3ad06bd21eacd4b929a7a216ac1ae578782c4e3ebe76ba758`  
**Screening timestamp:** 2026-04-21T06:12:22.498212+00:00  
**Term set version:** 1.0  

---

## Inclusion and Exclusion Criteria

The following criteria were applied consistently across all screening stages.

| Criterion | Inclusion | Exclusion |
|-----------|-----------|-----------|
| **Publication year** | ≥ 2021 | < 2021 |
| **Language** | English | Other languages |
| **Document type** | Peer-reviewed conference paper, journal article, or arXiv preprint with ≥ 1 citation | Blog posts, grey literature, software documentation, workshop papers without proceedings |
| **Minimum topical relevance** | Addresses ≥ 1 of: (a) parameter-efficient fine-tuning / adapters (PEFT, LoRA, prefix/prompt tuning); (b) distributed / P2P / federated ML systems; (c) multi-task LLM serving or inference | Exclusively covers unrelated domains (CV, audio, RL) with no NLP or LLM systems angle |
| **Tier 1 (highest priority)** | Addresses all three themes jointly (PEFT + distributed/P2P + LLM serving) | — |
| **Abstract availability** | Abstract accessible via API or pre-validated corpus | No accessible metadata and no resolvable DOI |

> **Note on year cutoff:** Pre-2021 foundational works (e.g., Houlsby et al. 2019, Hu et al. 2022) are included via the pre-validated G0–G6 corpora, which were assembled by manual curation and bypass the year filter.

---

## Stage 1 — Identification

Citation snowballing (Wohlin 2014) was conducted across **7 seed papers** in groups G0–G0 (search date: **2026-04-21**) using the following databases/APIs: ACL Anthology; Semantic Scholar Academic Graph API; Scopus (Elsevier); IEEE Xplore API.

| Group | Seeds | Backward examined | Forward examined | New (after dedup) |
|-------|------:|------------------:|-----------------:|------------------:|
| G0 | 7 | 450 | 700 | 972 |
| **Total** | **7** | | | **972** |

- **Records retrieved from API (raw):** 1,150
- **Duplicates removed** (by Semantic Scholar paper ID and DOI): 178
- **Records entering screening:** 972

## Stage 2 — Title Screening

All 972 records were screened by title using a keyword scoring algorithm 
(year cutoff: 2021; term set v1.0).

**Screening rules:**
- Layer 1: Exclude if year < year_cutoff or citation_count < min_citations
- Layer 2: Score title against 4 term sets (peft, llm, systems, distributed)
-   >= 2 sets matched → INCLUDE
-   1 set matched (non-llm) → REVIEW
-   llm-only match → EXCLUDE (precision too low)
-   0 sets matched → EXCLUDE
- Layer 3 (optional): LLM triage of REVIEW rows via Claude API
-   INCLUDE / EXCLUDE resolved; UNCERTAIN rows remain for manual inspection

| Decision | N |
|----------|--:|
| INCLUDE (auto) | 162 |
| REVIEW (manual triage) | 19 |
| EXCLUDE | 791 |
| **Total screened** | **972** |

**Exclusion reasons (title screening):**

| Reason | N |
|--------|--:|
| No keyword match in title | 284 |
| LLM-only match (too broad) | 255 |
| Year 2019 | 41 |
| Year 2020 | 34 |
| Year 2018 | 27 |
| Year 2017 | 24 |
| Year 2016 | 17 |
| Year 2014 | 10 |
| Year 2013 | 9 |
| Year 2015 | 4 |
| Year 2011 | 4 |
| Year 2008 | 3 |
| Year 2005 | 3 |
| Year 2010 | 2 |
| Year 2009 | 2 |
| Year 1995 | 2 |
| Year 1992 | 2 |
| Year 2003 | 1 |
| Year 1999 | 1 |
| Year 1997 | 1 |
| Year 1989 | 1 |
| Year 2007 | 1 |
| Year 2006 | 1 |
| Year 1966 | 1 |
| Year 1994 | 1 |

**By retrieval direction:**

| Direction | INCLUDE | REVIEW | EXCLUDE |
|-----------|--------:|-------:|--------:|
| BACKWARD | 20 | 30 | 287 |
| FORWARD | 91 | 100 | 444 |

## Stage 3 — LLM Triage (REVIEW queue)

The 130 REVIEW-queue records (single non-LLM keyword match) were submitted to **claude-haiku-4-5-20251001** for title- and venue-level classification. UNCERTAIN records were retained for manual inspection.

| Outcome | N |
|---------|--:|
| Promoted to INCLUDE | 51 |
| Confirmed EXCLUDE | 60 |
| UNCERTAIN (manual inspection) | 19 |
| **Total triaged** | **130** |

## Stage 4 — Eligibility (Full-text Assessment & Data Extraction)

Records passing abstract review (214 KEEP + 173 DEFER = **387**) advanced to the full-text
review queue. Full texts were sought and assessed for eligibility, then the eligible subset
proceeded through data extraction.

| Outcome | N |
|---------|--:|
| Full-text review queue (KEEP 214 + DEFER 173) | 387 |
| PDF retrieved | 122 |
| PDF not retrieved | 265 |
| Preliminary data extraction | 190 |
| Data extraction top-up (manual) | 224 |
| **Included in review (final reading list)** | **123 (120 distinct papers)** |

> **Distinct-paper note:** the 123 final records correspond to **120 distinct papers**:
> two arXiv↔Scopus duplicate key-pairs (LoRA, arXiv 2106.09685 + Scopus a8ca… ; Houlsby,
> arXiv 1902.00751 + Scopus 29ddc1…) each appear twice in the reading list, and a third
> work (CaraServe, arXiv 2401.11240) was retrieved twice — once as its arXiv preprint,
> once as its USENIX ATC 2025 publication, renamed "Toppings" (ACM DOI
> 10.5555/3768039.3768076) — for three duplicate key-pairs total.

## Stage 5 — Enrichment & Tier Classification

All records from the merged corpus were enriched via the Semantic Scholar batch API 
and OpenAlex (abstracts + field keywords), then filtered for topical relevance.

| Outcome | N |
|---------|--:|
| Kept (relevance filter passed) | 464 |
| Deprioritised (arXiv preprint, low citation, no Tier-1 signal) | 32 |
| Excluded (off-topic / malformed) | 6 |

**Exclusion reasons (enrichment filter):**

| Reason | N |
|--------|--:|
| off_topic_domain | 6 |

**Tier classification** (title + abstract + keyword signal matching):

| Tier | Criteria | N |
|------|----------|--:|
| Tier 1 | PEFT + Systems/Distributed + LLM (all three signals) | 90 |
| Tier 2 | PEFT + LLM, or PEFT + Systems (two signals) | 141 |
| Tier 3 | Other (foundational / tangential) | 233 |
| **Total included** | | **464** |

**Discovery direction of kept papers:**

| Direction | N |
|-----------|--:|
| Prevalidated | 343 |
| Forward | 86 |
| Backward | 26 |
| Seed | 9 |

**Venue quality of kept papers:**

| Venue quality | N | % |
|---------------|--:|--:|
| Top-tier venue (CORE A\* / Scopus Q1) | 166 | 35.8% |
| Peer-reviewed (other conference / journal) | 189 | 40.7% |
| Preprint (arXiv, no published venue) | 91 | 19.6% |
| Unknown / missing venue | 18 | 3.9% |

> **Reading guidance:** Start with Tier 1 papers (full read), Tier 2 (selective read), 
> Tier 3 (abstract skim). Papers are sorted by tier then citation count in `S6_enriched_reading_pool.csv`.

## Stage 6 — Abstract Review

Each paper in the enriched reading list was reviewed at abstract level using an interactive screener (`app.abstract_review`) with AI-assisted suggestions (Claude Sonnet). The reviewer made final KEEP / SKIP / DEFER decisions; the AI suggestion was advisory only.

| Decision | N | % of reviewed |
|----------|--:|--------------:|
| KEEP (included in Zotero corpus) | 214 | 38.8% |
| SKIP (excluded after abstract) | 338 | 61.2% |
| DEFER (requires closer reading) | 0 | 0.0% |
| **Total** | **552** | |

**Decision breakdown by tier:**

| Tier | KEEP | SKIP | DEFER | Undecided |
|------|-----:|-----:|------:|----------:|
| 1 | 49 | 41 | 0 | 0 |
| 2 | 68 | 73 | 0 | 0 |
| 3 | 85 | 148 | 0 | 0 |
| ? | 12 | 76 | 0 | 0 |

> **DEFER → SKIP cascade (reconciliation):** at the abstract-review *stage* the split was
> **KEEP 214 / DEFER 173 / SKIP 165 = 552** (`08_abstract_reviewed_2026-05-02.csv`). The
> 173 DEFER records were carried to the full-text queue (Stage 4, 387 = 214 + 173) but none
> advanced to data extraction; all 173 subsequently resolved to **SKIP** in the final corpus,
> giving the final view **KEEP 214 / SKIP 338** (338 = 165 + 173). The two views are consistent
> (`PRISMA_NUMBERS_VALIDATION.md` §C).
>
> **Zotero import:** Run `python -m app.abstract_review --export-ris` to generate the RIS file.

## Stage 7 — Final Included Studies

After all screening and abstract review stages, **123 papers** were confirmed for inclusion in the systematic review and assembled into the final reading list (`13_final_reading_list_2026-05-12.csv`). These correspond to **120 distinct papers** (three duplicate key-pairs — see Stage 4 note).

**By tier:**

| Tier | Criteria | N |
|------|----------|--:|
| Tier 1 | PEFT + Systems/Distributed + LLM (all three signals) | 48 |
| Tier 2 | PEFT + LLM, or PEFT + Systems (two signals) | 42 |
| Tier 3 | Foundational / tangential | 33 |
| **Total** | | **123** |

**By corpus role:**

| Role | N |
|------|--:|
| Core | 89 |
| Background | 34 |

**By discovery source:**

| Source | N |
|--------|--:|
| SCOPUS | 101 |
| ARXIV | 18 |
| ? | 4 |

> **Reading progress:** 0 / 123 papers read.

---

## File Inventory

| File | Role | Modifiable? |
|------|------|-------------|
| `01_raw_2026-04-21.csv` | Original candidates — **source of truth** | No — never edited |
| `02_screened_2026-04-21.csv` | Full list with screening decisions | No — regenerated by screener |
| `03_review_queue_2026-04-21.csv` | Manual triage queue | **Yes** — edit `inclusion` column |
| `04_included_*.csv` | Snowball candidates after screening | No — regenerated by screener |
| `05_merged_*.csv` | Merged prevalidated + screened candidates | No — regenerated by merge step |
| `06_enriched_*.csv` | All records with abstract + keywords filled | No — regenerated by enrich_and_filter.py |
| `07_filtered_*.csv` | Enriched reading list (tier-classified, sorted) | No — regenerated by enrich_and_filter.py |
| `07_deprioritized_*.csv` | Low-citation arXiv preprints (rescue if needed) | No |
| `07_excluded_*.csv` | Off-topic / malformed records (audit) | No |
| `08_abstract_reviewed_*.csv` | Abstract review decisions (KEEP/SKIP/DEFER) | No — written by abstract_review.py |
| `08_zotero_ready_*.ris` | **Zotero import file** (KEEP papers only) | No — regenerated by abstract_review.py |
| `13_final_reading_list_*.csv` | **Final included studies** (thesis reading material) | **Yes** — fill `read_status`, `key_finding`, etc. |
| `log_screening_*.json` | Keyword/LLM screening audit log | No — written by screener |
| `log_retrieval_*.json` | Per-seed retrieval counts | No — written by snowballer |
| `PRISMA_summary_*.md` | This file | No — regenerated by prisma.py |
