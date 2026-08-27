# PRISMA 2020 — Verified Number Table (single source of truth)

Every number is cross-checked against the pipeline data in
`slr_engine/snowballing/snowball_output/` (counted with the Python `csv`
module, header excluded). Status: ✅ CSV/log-verified · 📌 stated figure
(internally consistent; not a stored CSV row count).

---

## A. Master funnel table (all numbers in one place)

| # | Stage | Number | Ground-truth source | In `.tex` | Status |
|---|---|---|---|---|---|
| 1 | **G0 seed papers in corpus** | **9** | `S1_prevalidated_corpus.csv` direction=SEED → 9; `S1` seed_group G0=9; `G0_seed_papers.md` = 9 bullets | 03:21 "nine", 03:tab:groups "9", 11:12 "nine", 12:682 "nine" | ✅ |
| 1b | **Seeds submitted to retrieval API** | **7** | `log_retrieval_2026-04-21.json` `_meta.n_seeds` = **7** | 12:683 "seven of these", 12:641 (C.1 row "7 seeds") | ✅ |
| 1c | Seeds excluded from API snowball | **2** (of 9) | 9 − 7 = **2** | 12:684–690 (C.2 explanatory sentence: Sajina2025, Sajina2024) | ✅ |
| 2 | **Raw records retrieved (examined)** | **1,150** | `log_retrieval`: backward_examined **450** + forward_examined **700** = **1,150** | 03:75, 12:48, 12:691, 12:tab:search_log | ✅ |
| 3 | **Unique records after dedup** | **972** | `log_retrieval`: backward_new 337 + forward_new 635 = **972** = `S2` rows | 03:28, 12:693, 12:tab:search_log | ✅ |
| 3b | **Duplicates removed** | **178** | 1,150 − 972 = **178** | 03:28, 12:tab:search_log | ✅ |
| 4 | **Title screening — final outcome** | **162 INCL / 791 EXCL / 19 UNCERT = 972** | `S3_title_screened_all.csv` inclusion **162/791/19**; `log_screening` decisions = 162/791/19 | 12:tab:screening (final rows), 12:tab:search_log | ✅ |
| 4a | Title screening — Layer 2 (keyword) | **111 INCL / 130 queue / 731 EXCL = 972** | `log_screening` `by_seed_group.G0` = INCLUDE 111 / REVIEW 130 / EXCLUDE 731 | 12:tab:screening (col L2), 12:74 "130-record" | ✅ |
| 4b | Title screening — Layer 3 (triage of 130) | **+51 INCL / +60 EXCL / 19 UNCERT = 130** | `log_screening` `llm_screening` = resolved_include 51 / resolved_exclude 60 / uncertain_remaining 19 | 12:tab:screening (col L3), 12:79 "19 of 130" | ✅ |
| 4c | UNCERTAIN review queue | **19** | `03_review_queue_2026-04-21.csv` = **19** (inclusion SKIP) | 12:79 | ✅ |
| 5 | **Merge w/ 352 pre-validated** | 514 → **502** | 162 + 352 = 514; `S5_merged_corpus.csv` = **502**; `05_merged` = 502 | 12:tab:search_log "514 → 502", 03:29 | ✅ |
| 6 | **Enrichment + tier filter** | 502 → **464** | `S6_enriched_reading_pool.csv` = **464**; `S6b`=6 excl + `S6c`=32 depri → 464+6+32=502 | 12:tab:search_log, 03:31, 12:124–127 | ✅ |
| 6a | Tier classification (of 464) | **T1 90 / T2 141 / T3 233 = 464** | `S6` tier = **90/141/233** | 12:tab:tiers, fig:tiers | ✅ |
| 7 | Abstract review, pass 1 (464) | **202 KEEP / 169 DEFER / 93 SKIP = 464** | `S7a_abstract_reviewed_base.csv` abstract_decision **202/169/93** | 12:tab:search_log | ✅ |
| 8 | Abstract review, combined (552) | **214 KEEP / 173 DEFER / 165 SKIP = 552** | `08_abstract_reviewed_2026-05-02.csv` abstract_decision **214/173/165** | 12:tab:abstract, 12:tab:search_log | ✅ |
| 8a | 88-pool (forward G_SNOW_F) | **12 KEEP / 4 DEFER / 72 SKIP = 88** | `08_2026-05-02` seed_group=G_SNOW_F → **12/4/72** | 12:tab:search_log "12 KEEP; 4 DEFER; 72 SKIP", 12:C.3 | ✅ |
| 8b | Pool cross-sum | 202+12=**214** · 169+4=**173** · 93+72=**165** | rows 7 + 8a | 12:tab:abstract | ✅ |
| 9 | **Full-text review queue** | **387** (= 214 KEEP + 173 DEFER) | `09_fulltext_review_queue_2026-05-02.csv` = **387**; abstract_decision KEEP 214 / DEFER 173 | 12:tab:search_log "387 queued", 12:249 | ✅ |
| 9a | PDF retrieved (of 387) | **122 YES / 265 NO** | `09` pdf_downloaded YES 122 / NO 265 = 387 | 12:256 "no PDF was downloaded" | ✅ |
| 10 | Preliminary data extraction | 387 → **190** | `10_data_extraction_2026-05-02.csv` = **190** | 12:tab:search_log, 12:252 | ✅ |
| 11 | Forward snowball — Scopus | 106 raw → **74** title-screened in | `M1_forward_scopus_2026-05-08.csv` = **106**; G_SNOW_F scopus = 74 | 12:tab:search_log, 12:C.3 | ✅ |
| 12 | Forward snowball — WoS | 20 raw → **14** title-screened in | `08..._scopus` source_engine wos = **14**; `M2_forward_wos_2026-05-08.txt` = 20 records | 12:tab:search_log, 12:C.3 | ✅ |
| 13 | Forward snowball added (74+14) | **88** | `08` G_SNOW_F = **88**; scopus 94−20=74 + wos 14 = 88 | 12:C.3 "88 records (74 + 14)" | ✅ |
| 14 | Venue validation — Scopus | **172** matched | `M3_scopus_venue_validation_2026-05-11.csv` = **172** = `11_MANUAL_SCOPUS_export_1105.csv` | 12:tab:search_log, 12:C.5 | ✅ |
| 15 | Venue validation — WoS | **125** matched | `M4_wos_venue_validation_2026-05-11.txt` = **125** records (126 lines − 1 header) | 12:tab:search_log, 12:C.5 | ✅ |
| 16 | Data extraction top-up (manual) | 190 → **224** | `11_data_extraction_2026-05-12.csv` = **224** | 12:tab:search_log "190 → 224", 03:35 | ✅ |
| 17 | **Final reading list** | **123** | `13_final_reading_list_2026-05-12.csv` = **123** | 03:36, 03:prisma-caption, 11:12, 12:256 | ✅ |
| 18 | **Distinct papers** | **120** | `13`: 123 rows = **120 unique titles**; LoRA (ARXIV 2106.09685 + SCOPUS a8ca46…) & Houlsby (ARXIV 1902.00751 + SCOPUS 29ddc1…) each appear twice, and CaraServe/Toppings (ARXIV 2401.11240, arXiv preprint + ACM DOI 10.5555/3768039.3768076, USENIX ATC'25 publication renamed "Toppings") appears twice — **found 2026-08-22**, third duplicate pair not previously flagged | 03:37, 03:prisma-caption, 11:12 | ✅ |
| 19 | Final corpus tier | **T1 48 / T2 42 / T3 33 = 123** | `13` tier = **48/42/33** | 03:synthesis, 12:tab:year_dist | ✅ |
| 20 | Final corpus split | **core 89 / background 34 = 123** | `13` corpus = core 89 / background 34 | (synthesis chapters) | ✅ |

**Funnel arithmetic (all hold):**
- 1,150 − 972 = **178** ✓ · 162 + 791 + 19 = **972** ✓
- Layer 2: 111 + 130 + 731 = **972** ✓ · Layer 3: 51 + 60 + 19 = **130** ✓
- 111+51 = **162** ✓ · 731+60 = **791** ✓
- 162 + 352 = 514 → **502** ✓ · 464 + 6 + 32 = 502 ✓
- 202+12 = 214 ✓ · 169+4 = 173 ✓ · 93+72 = 165 ✓ (88 = 12/4/72)
- 214 + 173 = **387** ✓ · 74 + 14 = **88** ✓ · 190 → **224** ✓
- 48 + 42 + 33 = **123** ✓ · 89 + 34 = **123** ✓

---

## B. Groups table (`tab:groups` — pre-validated split) — verified against `S1` seed_group

| Group | n pre-validated | Source | In `.tex` | Status |
|---|---|---|---|---|
| G0 | 9 | 9 | tab:groups G0=9 | ✅ |
| G1 | 59 | 59 | G1=59 | ✅ |
| G2 | 37 | 37 | G2=37 | ✅ |
| G3 | 95 | 95 | G3=95 | ✅ |
| G4 | 51 | 51 | G4=51 | ✅ |
| G5 | 35 | 35 | G5=35 | ✅ |
| G6 | 66 | 66 | G6=66 | ✅ |
| **Total** | **352** | 9+59+37+95+51+35+66 = **352** | Total 352 | ✅ |

> `tab:groups` "n final" per-cell column (G0=18, G1=17, G2=17, G3=14, G4=16, G5=11,
> G6=30; no "Other" row) **sums to 123** ✅ but is a **narrative synthesis-mapping** (each
> paper counted under the chapter where it is discussed), not reproducible from a
> single pipeline column. **Total 123 is CSV-authoritative; treat per-cell finals as 📌 stated.**
> (Corrected 2026-08-21 from a stale earlier snapshot — G0=20/G1=12/G2=15/G3=11/G4=12/G5=9/
> G6=29/Other=15 — to match the current `tab:groups` in `03_methodology.tex`, per S6
> `seed_group` re-tagging; see `REVISION_LOG.md` row 16.)

---

## C. DEFER → SKIP cascade (KEEP / DEFER / SKIP reconciliation)

| Claim | Value | Ground truth | In `.tex` | Status |
|---|---|---|---|---|
| 173 DEFER advanced to full-text queue | **173** of 387 | `09` abstract_decision = DEFER **173**; fulltext_decision DEFER **173** | 12:230–233 caption "carried 173 DEFER" | ✅ |
| All 173 DEFER → SKIP in final | **173** (338−165) | `S7b_abstract_reviewed_final.csv` = **KEEP 214 / SKIP 338** (no DEFER; 338 = 165+173) | 12:230–233 "all subsequently resolved to SKIP" | ✅ |
| No DEFER entered extraction | **0** | `10`/`11` contain no DEFER; 09 fulltext_decision INCLUDE 109 / EXCLUDE 13 / DEFER 173 / blank 92 | 12:233 "none advanced to extraction", 12:256 | ✅ |

---

## D. Screening detail (`log_screening_2026-04-21.json`)

| Metric | Value | Status |
|---|---|---|
| input.total_records | 972 | ✅ |
| decisions.INCLUDE / EXCLUDE / REVIEW | 162 / 791 / 19 | ✅ |
| by_seed_group.G0.INCLUDE / REVIEW / EXCLUDE | 111 / 130 / 731 (=972) | ✅ |
| llm_screening.rows_sent | 130 | ✅ |
| llm_screening.resolved_include / exclude / uncertain_remaining | 51 / 60 / 19 (=130) | ✅ |
| exclusion: pre-2021 years | 192 | ✅ |
| exclusion: no keyword match | 284 | ✅ |
| exclusion: LLM-only (too broad) | 255 | ✅ |
| **Exclusion sub-total** | 192+284+255 = **731** = pre-triage G0.EXCLUDE | ✅ |

---

## E. Venue-quality & abstract-review percentages

**Venue quality of 464** (`S6` venue_quality): top_venue **166** (35.8%) · peer_reviewed **189** (40.7%) · preprint **91** (19.6%) · unknown **18** (3.9%). ✅ (A.5 prose)

**Abstract review** (`tab:abstract`, A.7, from `08_2026-05-02`): KEEP **214** = 38.8% (214/552) · SKIP **338** = 61.2% (338/552) · Total **552**. ✅

**Years 2021–2025 window:** **107 papers = 87%**; most active 2024 **38 (31%)**, then 2025 **20 (16%)**, 2023 **19 (15%)**. ✅ (A.6 prose)

---

## F. Year distribution of the 123 final papers — verified against `13` `year` column

| Year | Papers | % of corpus | Status |
|---|---|---|---|
| 2002 | 1 | 0.8 | ✅ |
| 2011 | 1 | 0.8 | ✅ |
| 2016 | 1 | 0.8 | ✅ |
| 2017 | 1 | 0.8 | ✅ |
| 2019 | 4 | 3.3 | ✅ |
| 2020 | 5 | 4.1 | ✅ |
| 2021 | 17 | 13.8 | ✅ |
| 2022 | 13 | 10.6 | ✅ |
| 2023 | 19 | 15.4 | ✅ |
| 2024 | 38 | 30.9 | ✅ |
| 2025 | 20 | 16.3 | ✅ |
| 2026 | 3 | 2.4 | ✅ |
| **Total** | **123** | 100 | ✅ |

---

## G. Change log

- **2026-08-20**: Rebuilt as a single master table (all numbers in one place). Added the **2 excluded seeds** row (1c) reflecting the new C.2 explanatory sentence and the **7 seeds → 1,150** C.1-row clarification. Newly derived the raw **1,150** and **178** duplicates directly from `log_retrieval` examined-vs-new sums. Confirmed year/tier/venue/group splits, the DEFER→SKIP cascade, all percentages, and the **121 distinct** double-key explanation. No flagged inconsistencies remain.
- **2026-08-22**: Found a third duplicate key-pair not caught by the 2026-08-20 pass — CaraServe (arXiv 2401.11240, row `2401.11240` in `13`) and its own USENIX ATC 2025 publication, renamed "Toppings" (row `69d631b3…` in `13`, ACM DOI `10.5555/3768039.3768076`), are the same paper retrieved twice, one preprint + one renamed camera-ready. Corrected **distinct papers 121 → 120** everywhere (row 18 above, abstract, §3.1 body + footnote, Fig 5 caption, §11 Conclusion ×2, PRISMA checklist ×2, PRISMA summary ×3, this file). Bibliography: merged `LiToppings2025` into `Li2024CaraServe` (now the USENIX ATC 2025 / ACM-DOI record, with a `note` field preserving the original arXiv title); §6 Inference Systems' two separate CaraServe/Toppings paragraphs merged into one. No change to Table 1 / per-group G4 counts — those already total 123 records (not 120/121 distinct), consistent with how the other two duplicate pairs were already handled.
