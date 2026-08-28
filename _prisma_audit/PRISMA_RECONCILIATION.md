# PRISMA Funnel Reconciliation — Ground Truth (Phase 1 + Phase 2)

Data source root:
`/Users/vluk/PycharmProjects/slr_engine/slr_engine/snowballing/snowball_output/`
Manuscript target (to edit):
`writing/mdpi_paper/mdpi_submission/`

Every number below was recomputed from row counts in the pipeline files, NOT from the .tex.

## Stage-by-stage: recomputed vs. manuscript

| Stage | Manuscript states | Recomputed from data | Source file / method | Verdict |
|---|---|---|---|---|
| Raw snowball candidates | 1,150 | 1,150 | PRISMA_summary; log_retrieval | ✓ |
| After dedup → title-screening pool | 972 | 972 | 01_raw_2026-04-21.csv (972 rows); audit `input.total_records=972` | ✓ |
| Title INCLUDE | 162 | 162 | 04_included_2026-04-21.csv (162 rows); audit decisions.INCLUDE | ✓ |
| Title UNCERTAIN (post-triage) | 19 | 19 | 03_review_queue_2026-04-21.csv (19 rows); audit llm_screening.uncertain_remaining | ✓ |
| Title EXCLUDE | 791 | 791 | audit decisions.EXCLUDE (162+19+791=972) | ✓ |
| Merge: 162+352=514 − 12 = 502 | 502 | 502 | 05_merged (502 rows); **re-ran app.merge.py → prevalidated 352, new 150, deduped 12, total 502** | ✓ RESOLVED (2a) |
| Enrichment retained | 464 | 464 | pipeline in_enriched_S6=464 | ✓ |
| Enrichment deprioritised (rescues) | 32 | 32 | 07_deprioritized (32); S6c (32) | ✓ |
| Enrichment off-topic excluded | 6 | 6 | S6b_excluded_offtopic (6) | ✓ |
| Abstract-review pool | 552 | 552 | S7b (552 rows); pipeline in_abstract_review_S7b=552 | ✓ |
| Abstract KEEP | 214 | 214 | S7b abstract_decision KEEP; RIS entries=214 | ✓ |
| Abstract SKIP (final) | 338 | 338 | S7b abstract_decision SKIP (214+338=552) | ✓ |
| Full-text review queue | 387 | 387 | 09_fulltext_review_queue (387 rows); pipeline in_fulltext_queue_Q9=387; queue `abstract_decision`= KEEP 214 + DEFER 173 | ✓ RESOLVED (2b) |
| Preliminary data extraction (from queue) | 190 | 190 | 10_data_extraction (190 rows); pipeline KEEP-origin extraction=190 | ✓ |
| Data extraction (final) | 224 | 224 | 11_data_extraction (224 rows); review_source 109+81=190 + 34 top-up | ✓ |
| Final reading list | 123 (120 distinct) | 123 / 120 | 13_final_reading_list (123 rows; 120 distinct; 3 works duplicated) | ✓ |

## 2a — 502 vs 514 (RESOLVED)
- 04_included (162 INCLUDE) + 00_prevalidated (352) = 514 raw.
- Re-ran `app.merge.py` dedup logic (DOI / arxiv / ss_paper_id): **12 snowball records already present in the pre-validated corpus were dropped** → new=150, total=502.
- The 12 deduped records are enumerated (LoRA arXiv 2106.09685, GLaM 2112.06905, Compacter 2106.04647, Orca, SEA, EfficientLoRA, HCInfer, RTT/Bandwidth, Birds in Cages, Prompt Inversion Attack, Indic BLOOMZ, Empirical PEFT-in-Code).
- **502 is correct.** Manuscript already states "12 removed as duplicates" — confirmed accurate.
- **19 UNCERTAIN** were NOT part of the merge (merge used only the 162 INCLUDE). See ambiguity note below.

## 2b — 214 vs 387 (RESOLVED)
- The full-text queue file `09_fulltext_review_queue_2026-05-02.csv` has **387 rows**, and ITS OWN `abstract_decision` column = **KEEP 214 + DEFER 173 = 387**.
- pipeline_unified `in_fulltext_queue_Q9` = 387. → **387 is the full-text queue size** = 214 KEEP + 173 borderline-DEFER.
- 214 = the KEEP subset (also = RIS export entries = 214).
- EXT RACTED: 190 preliminary (10_data_extraction) = the KEEP-origin subset + 34 top-up = 224 final. The manuscript's chain "387 → 190 → 224 → 123" is arithmetically consistent.
- **CONTRADICTION in Table tab:abstract caption**: it claims "all 173 DEFER records were resolved to SKIP in the final classification and none advanced to data extraction." DATA CONTRADICTS: the queue (387) is explicitly built from KEEP + DEFER, and DEFER-origin records reached extraction (extraction includes non-KEEP rows; pipeline extraction has fulltext_decision=DEFER=1 and abstract_decision=SKIP=1). The C.1 search log itself already documents "Fulltext review queue compiled from KEEP and borderline-DEFER records" and treats 387 queued → 190 extracted.
- → The caption must be rewritten so it does not claim DEFERs never entered the queue / never reached extraction. 387 stays as the queue size (already consistent in methodology + prose + Figure 2).

## 2c — 32 rescued records
- All 32 deprioritised (07_deprioritized) records are in the S5/502 pool only.
- **NONE reached abstract review (0), extraction (0), or the final list (0).** They were NOT reinstated.
- → 464 and the abstract 552 are correct. The phrase "after rescues were resolved" (§A.7) must NOT imply reinstatement.

## Flags for the author (data contradictions to report, not silently fix)
1. **19 UNCERTAIN records (§A.4 claim "carried forward and resolved during abstract-level review").** By ss-id and title matching in `pipeline_unified.csv`, only **3 of 19** UNCERTAIN records appear in the abstract-review pool (`in_abstract_review_S7b`), and **0** reach the final list; the other **16** appear nowhere in the pipeline file. This contradicts the appendix claim. Recommend the text be corrected to say the UNCERTAIN records were manually re-checked post-screen and effectively excluded (none reached the final corpus) — pending author confirmation.

## Files consulted (counts)
- 01_raw 972 · 02_screened 972 · 03_review_queue 19 · 04_included 162 · 05_merged 502
- 07_deprioritized 32 · S6b_excluded_offtopic 6 · S7b 552 · 08_zotero_ready.ris 214 entries
- 09_fulltext_review_queue 387 · 10_data_extraction 190 · 11_data_extraction 224 · 13_final_reading_list 123
