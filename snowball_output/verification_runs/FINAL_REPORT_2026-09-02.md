# Final Verification Report — slr_engine vs the manuscript

Every number below is **recomputed from the pipeline's own data files**, never read from the manuscript text. Two independent paths are checked:

1. **Fixtures** — recomputed from the frozen, committed snapshots in `verification_fixtures/` (what ships in this repository), and
2. **Live run** — recomputed from a fresh pipeline run in `data/snowball_output/` (or the `SLR_OUTPUT_DIR` tree), proving the *actual* pipeline reproduces the same numbers, not just curated fixtures.

- Suites run: multiple; checks executed: **78**, passed: **78**, failed: **0**

## Verified values (committed fixtures)

| # | Suite | Figure / check | Recomputed | Manuscript ref | Verdict |
|---|-------|----------------|-----------|----------------|---------|
| 1 | PRISMA funnel | n_seeds submitted | 7 |  | ✅ pass |
| 2 | PRISMA funnel | raw records retrieved | 1150 |  | ✅ pass |
| 3 | PRISMA funnel | unique records after dedup (log_retrieval total_new) | 972 |  | ✅ pass |
| 4 | PRISMA funnel | duplicates removed (1150-972) | 178 |  | ✅ pass |
| 5 | PRISMA funnel | screening-pool total (log_screening input.total_records) | 972 |  | ✅ pass |
| 6 | PRISMA funnel | title INCLUDE | 162 |  | ✅ pass |
| 7 | PRISMA funnel | title REVIEW/UNCERTAIN | 19 |  | ✅ pass |
| 8 | PRISMA funnel | title EXCLUDE | 791 |  | ✅ pass |
| 9 | PRISMA funnel | title screen sums to pool (162+19+791) | 972 |  | ✅ pass |
| 10 | PRISMA funnel | S3_title_screened_all rows | 972 |  | ✅ pass |
| 11 | PRISMA funnel | S4_title_screened_included rows (INCLUDE set) | 162 |  | ✅ pass |
| 12 | PRISMA funnel | 03_review_queue rows (UNCERTAIN set) | 19 |  | ✅ pass |
| 13 | PRISMA funnel | llm rows sent | 130 |  | ✅ pass |
| 14 | PRISMA funnel | llm promoted to INCLUDE | 51 |  | ✅ pass |
| 15 | PRISMA funnel | llm confirmed EXCLUDE | 60 |  | ✅ pass |
| 16 | PRISMA funnel | llm UNCERTAIN remaining | 19 |  | ✅ pass |
| 17 | PRISMA funnel | title INCLUDE = rule-based + llm (111 + 51 = 162) | 162 |  | ✅ pass |
| 18 | PRISMA funnel | pre-validated corpus (S1 rows) | 352 |  | ✅ pass |
| 19 | PRISMA funnel | merged corpus (S5 rows) | 502 |  | ✅ pass |
| 20 | PRISMA funnel | merge duplicates removed (514-502) | 12 |  | ✅ pass |
| 21 | PRISMA funnel | enriched retained (S6 rows) | 464 |  | ✅ pass |
| 22 | PRISMA funnel | deprioritized (S6c rows) | 32 |  | ✅ pass |
| 23 | PRISMA funnel | off-topic excluded (S6b rows) | 6 |  | ✅ pass |
| 24 | PRISMA funnel | S6 + S6b + S6c = merged | 502 |  | ✅ pass |
| 25 | PRISMA funnel | abstract-review pool (S7b rows = 464+88) | 552 |  | ✅ pass |
| 26 | PRISMA funnel | forward-added records (S7b - S7a = 88) | 88 |  | ✅ pass |
| 27 | PRISMA funnel | KEEP | 214 |  | ✅ pass |
| 28 | PRISMA funnel | DEFER (from 09 queue) | 173 |  | ✅ pass |
| 29 | PRISMA funnel | SKIP (abstract 338 - DEFER 173 = 165) | 165 |  | ✅ pass |
| 30 | PRISMA funnel | keep + defer + skip = pool | 552 |  | ✅ pass |
| 31 | PRISMA funnel | full-text queue (09 rows = 214+173) | 387 |  | ✅ pass |
| 32 | PRISMA funnel | queue KEEP + DEFER = 387 | 387 |  | ✅ pass |
| 33 | PRISMA funnel | preliminary extraction (10_data_extraction rows) | 190 |  | ✅ pass |
| 34 | PRISMA funnel | final extraction (11_data_extraction rows) | 224 |  | ✅ pass |
| 35 | PRISMA funnel | top-up (224 - 190) | 34 |  | ✅ pass |
| 36 | PRISMA funnel | final reading list rows (13) | 123 |  | ✅ pass |
| 37 | PRISMA funnel | duplicate works present in final list | 3 |  | ✅ pass |
| 38 | PRISMA funnel | distinct papers (123 - 3 extra rows) | 120 |  | ✅ pass |
| 39 | PRISMA funnel | final tiers 1/2/3 | (48, 42, 33) |  | ✅ pass |
| 40 | PRISMA funnel | final corpus core/background | (89, 34) |  | ✅ pass |
| 41 | Quality appraisal | enriched pool size | 464 |  | ✅ pass |
| 42 | Quality appraisal | venue_quality top_venue | 166 |  | ✅ pass |
| 43 | Quality appraisal | venue_quality peer_reviewed | 189 |  | ✅ pass |
| 44 | Quality appraisal | venue_quality preprint | 91 |  | ✅ pass |
| 45 | Quality appraisal | venue_quality unknown | 18 |  | ✅ pass |
| 46 | Quality appraisal | venue-quality sums to 464 | 464 |  | ✅ pass |
| 47 | Quality appraisal | enriched tier 1 | 90 |  | ✅ pass |
| 48 | Quality appraisal | enriched tier 2 | 141 |  | ✅ pass |
| 49 | Quality appraisal | enriched tier 3 | 233 |  | ✅ pass |
| 50 | Quality appraisal | tier sums to 464 | 464 |  | ✅ pass |
| 51 | Quality appraisal | abstract pool size | 552 |  | ✅ pass |
| 52 | Quality appraisal | KEEP | 214 |  | ✅ pass |
| 53 | Quality appraisal | SKIP | 338 |  | ✅ pass |
| 54 | Quality appraisal | KEEP + SKIP = 552 | 552 |  | ✅ pass |
| 55 | Quality appraisal | final list size | 123 |  | ✅ pass |
| 56 | Quality appraisal | year distribution matches manuscript | {'2002': 1, '2011': 1, '2016': 1, '2017': 1, '2019': 4, '2020': 5, '2021': 17, '2022': 13, '2023': 19, '2024': 38, '2025': 20, '2026': 3} |  | ✅ pass |
| 57 | Quality appraisal | most active year 2024 = 38 | 38 |  | ✅ pass |
| 58 | Quality appraisal | year distribution sums to 123 | 123 |  | ✅ pass |
| 59 | Quality appraisal | full year range present (2002..2026) | 2002 |  | ✅ pass |
| 60 | Live run | n_seeds submitted (live) | 7 | Fig. 1 / §3.1 | ✅ pass |
| 61 | Live run | raw records retrieved (live) | 1150 | Fig. 1 | ✅ pass |
| 62 | Live run | unique records after dedup (live) | 972 | Fig. 1 | ✅ pass |
| 63 | Live run | duplicates removed (live) | 178 | Fig. 1 | ✅ pass |
| 64 | Live run | screening pool (live) | 972 | Fig. 1 | ✅ pass |
| 65 | Live run | title INCLUDE (live) | 162 | Fig. 1 | ✅ pass |
| 66 | Live run | title REVIEW/UNCERTAIN (live) | 19 | Fig. 1 | ✅ pass |
| 67 | Live run | title EXCLUDE (live) | 791 | Fig. 1 | ✅ pass |
| 68 | Live run | title screen sums to pool (live) | 972 | Fig. 1 | ✅ pass |
| 69 | Live run | llm promoted to INCLUDE (live) | 51 | Fig. 1 | ✅ pass |
| 70 | Live run | llm UNCERTAIN remaining (live) | 19 | Fig. 1 | ✅ pass |
| 71 | Live run | pre-validated corpus (live) | 352 | Fig. 1 | ✅ pass |
| 72 | Live run | merged corpus (live) | 502 | Fig. 1 | ✅ pass |
| 73 | Live run | enriched retained (live) | 464 | Fig. 1 | ✅ pass |
| 74 | Live run | abstract-review pool (live) | 552 | Fig. 1 | ✅ pass |
| 75 | Live run | abstract KEEP (live) | 214 | Fig. 1 | ✅ pass |
| 76 | Live run | final reading list rows (live) | 123 | Fig. 1 | ✅ pass |
| 77 | Live run | distinct papers (live) | 120 | Fig. 1 + §3.4 | ✅ pass |
| 78 | Live run | PRISMA_summary.md consistent with funnel (values in summary) | 0 | PRISMA_summary.md | ✅ pass |

## Reproducibility statement

**ALL CHECKS PASS** — 78/78 verifications matched the manuscript (reproducible from committed fixtures.)

> The values quoted in the PRISMA funnel and quality-appraisal tables of the manuscript are exactly reproduced here from the pipeline artifacts committed to `verification_fixtures/`. Run `python3 scripts/verify.py` to regenerate this report on any fresh clone.
