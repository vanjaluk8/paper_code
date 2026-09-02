# PRISMA validation table — single source of truth (`prisma_facts.json`)

Auto-generated; every value is recomputed from the pipeline files, not typed. Open this next to the manuscript: every funnel number you read should match a row here.

> Anchor the funnel on **123 rows = 120 distinct works** (3 works kept as two rows each). **70/53** is the entry-*decision-route* split; the *forward-snowball* branch (**G_SNOW_F**) is the small 88→12/4/72 block in stage 8 — these are two different axes and must never be conflated.

## Funnel

| # | Stage | Quantity | Value | Source / arithmetic |
|---|-------|----------|------:|---------------------|
| 1 | Identification | raw records retrieved | 1150 |
|  |  | duplicates removed | 178 |
|  |  | unique after dedup (screen pool) | 972 |
| 2 | Title screening | INCLUDE | 162 |
|  |  | UNCERTAIN / REVIEW | 19 |
|  |  | EXCLUDE | 791 |
|  |  | sum = pool ✓ | 972 |
| 2b | LLM triage | rows sent | 130 |
|  |  | promoted to INCLUDE | 51 |
|  |  | EXCLUDE | 60 |
|  |  | UNCERTAIN remaining | 19 |
| 3 | Merge | pre-validated corpus (G0-G6) | 352 |
|  |  | merge duplicates removed | 12 |
|  |  | merged corpus | 502 |
| 4 | Enrichment | retained (enriched) | 464 |
|  |  | deprioritized low-cite | 32 |
|  |  | off-topic excluded | 6 |
| 5 | Abstract review | abstract-review pool | 552 |
|  |  | KEEP | 214 |
|  |  | DEFER | 173 |
|  |  | SKIP (final) | 165 |
|  |  | sum = pool ✓ | 552 |
| 6 | Full-text / extraction | full-text queue | 387 |
|  |  | extraction from queue | 190 |
|  |  | manual cross-val top-up | 34 |
|  |  | extraction total | 224 |

## Final list — anchors

| Quantity | Value | Source |
|----------|------:|--------|
| final rows | 123 | 13_final_reading_list (N=123) |
| **distinct works** | **120** | 123 − 3 dup-works (ANCHOR) |
| duplicate works (2 rows each) | 3 | LoRA · Houlsby · CaraServe≡Toppings |
| entry route: fulltext | 70 | 11_data_extraction `review_source` |
| entry route: abstract-2nd-pass | 53 | 11_data_extraction `review_source` |
| route sum = 123 ✓ | 123 | 70+53 |
| tiers 1 / 2 / 3 | 48 / 42 / 33 | 13_final `tier` (48/42/33=123) |
| core / background | 89 / 34 | 13_final `corpus` (89/34=123) |

## Forward-snowball branch (G_SNOW_F) — its own block, NOT the 53

| Quantity | Value | Source |
|----------|------:|--------|
| records added | 88 | Appendix C.3 |
| KEEP | 12 | Appendix C.3 |
| DEFER → resolved SKIP | 4 | Appendix C.3 |
| SKIP | 72 | Appendix C.3 |
| 12+4+72 = 88 ✓ | 88 | consistency |

## Provenance cross-tab (originating group × entry route), all margins = 123

| Group | fulltext | abstract-2nd-pass | total |
|-------|--------:|------------------:|------:|
| G0 | 14 | 4 | 18 |
| G1 | 13 | 4 | 17 |
| G2 | 13 | 4 | 17 |
| G3 | 2 | 12 | 14 |
| G4 | 4 | 12 | 16 |
| G5 | 7 | 4 | 11 |
| G6 | 17 | 13 | 30 |
| **TOT** | **70** | **53** | **123** |

Group subtotals: G0=18, G1=17, G2=17, G3=14, G4=16, G5=11, G6=30 (G1–G6 = 105, total 123)

## Duplicate works (kept as two rows each, counted once)

- `2106.09685` ≡ `a8ca46b171467ceb2d7652fbfb67fe701ad86092`
- `1902.00751` ≡ `29ddc1f43f28af7c846515e32cc167bc66886d0c`
- `2401.11240` ≡ `69d631b3875149050ab3088501cfc9d5cbea9e99`

---
Consistency: 21 checks pass (see `prisma_facts.py` / `verify_common.py`).
