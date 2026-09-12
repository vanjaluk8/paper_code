# RESPONSE_TO_REVIEWER.md

Skeleton per Phase 4 of `REVISION_PROMPT.md`. One row per item ID.
**Status**: `done` / `needs author` / `disputed`. **Where to look**: file(s)
in the revised manuscript, or the relevant section of `OPEN_QUESTIONS.md`.
Prose response cells are intentionally left blank — the author writes these.

## Desk-check and PRISMA reconciliation (D-*, P1-*)

| Item | Status | Where to look | Response |
|---|---|---|---|
| D-1 | done | `sections/02_background.tex`, `06_inference_systems.tex`, `08_p2p_federated.tex` (WP-2) | |
| D-2 | done | `sections/12_appendix.tex` (WP-11) | |
| P1-1 | done | `sections/03_methodology.tex` §3.2, `figures/prisma.html` (WP-13); membership matrix `verify/wp13_membership_matrix.csv` | |
| P1-2 | done | `sections/03_methodology.tex` Table 5 (WP-6) | |
| P1-3 | done | `sections/12_appendix.tex` §A.4/A.5 (WP-7) | |
| P1-4 | done | `sections/03_methodology.tex` Table 7 (WP-8) | |
| P1-5 | done | `sections/03_methodology.tex` §3.4, Figure 6 (WP-9) | |
| P1-6 | needs author | review's own text; not addressed in Phase 1/2 — no WP covered PRISMA Item 16b re-application | |
| P1-7 | done | `sections/03_methodology.tex` §3.1 (WP-9) | |

## Blocking issues

| Item | Status | Where to look | Response |
|---|---|---|---|
| Blocking 1 (Undermind reproducibility) | needs author | disclosed as a limitation pre-revision; not re-addressed here | |
| Blocking 2 (173 DEFER, no assessment) | done (data) / needs author (judgement) | `verify/wp13_defer_records.csv`; author must decide whether to assess or justify dropping | |
| Blocking 3 (extend concept matrix) | needs author | `OPEN_QUESTIONS.md` S-1; scaffold at `verify/s1_tier1_concept_matrix_scaffold.csv` | |
| Blocking 4 (add Dec-LoRA/MoE rows) | needs author | `OPEN_QUESTIONS.md` S-2 | |
| Blocking 5 (appraisal instrument) | needs author | `OPEN_QUESTIONS.md` Blocking 5; scaffold at `verify/blocking5_appraisal_scoring_template.csv` | |
| Blocking 6 (E-1, Zadouri O(log N)) | needs author | `OPEN_QUESTIONS.md` E-1 — CONTRADICTED | |
| Blocking 7 (E-2, Zeng/Aghajanyan) | needs author | `OPEN_QUESTIONS.md` E-2 — CONTRADICTED | |
| Blocking 8 (Figure A3) | done | `sections/12_appendix.tex` (WP-11) | |
| Blocking 9 (Supplementary S1/S2) | done | files exist in `supplementary/`; confirm attached at submission | |

## Major issues

| Item | Status | Where to look | Response |
|---|---|---|---|
| Major 10 (Boolean recall) | done (data) / needs author (prose) | `verify/boolean_recall.md` — 84.6% | |
| Major 11 (second screener) | needs author | `verify/major11_*` blind samples, seed 20260912 | |
| Major 12 / P1-2 (Table 5/2) | done | see P1-2 above | |
| Major 13 / P1-3 (UNCERTAIN) | done | see P1-3 above | |
| Major 14 (§6.4/6.7/8.5/4.4 → tables) | disputed | author judgement: existing prose already covers this content adequately; tables judged not mandatory | |
| Major 15 / S-4 ("Combined reference profile") | done | `sections/09_synthesis_gap.tex` — renamed "Requirement profile implied by RQ" | |
| Major 16 / N-1 (survey sets) | needs author | `OPEN_QUESTIONS.md` N-1 | |
| Major 17 (inclusion-rule / I-E table) | done (table) / needs author (rule-tightening decision) | `sections/12_appendix.tex` Table A2 (Appendix A.3) | |
| Major 18 (E-3–E-8 verify/correct) | needs author | `OPEN_QUESTIONS.md` E-3, E-4, E-5, E-6, E-8 — all resolved with verdicts | |
| Major 19 (top-up search) | needs author | `verify/major20_topup_search_queries.md` — drafted, not run | |
| Major 20 (citation-verification pass) | done (DOI pass) / needs author (full pass) | `OPEN_QUESTIONS.md` Major 21 — 125/128 DOIs resolve, 3 fixed | |
| Major 21 (§9.3 dimension provenance) | needs author | not addressed — requires new synthesis prose | |

## Minor issues

| Item | Status | Where to look | Response |
|---|---|---|---|
| Minor 22 (abstract ≤200 words + route split) | done | `main.tex` (WP-5, WP-6) — 193 words | |
| Minor 23 (D-1 dupes, C-5) | done | see D-1 above | |
| Minor 24 (C-1, Appendix C labels) | done | `sections/12_appendix.tex` (WP-1) | |
| Minor 25 (C-3, C-4) | done | see WP-2 above | |
| Minor 26 (C-2, abbreviations) | done | see WP-3 above | |
| Minor 27 (Eq. 4/6, Houlsby LayerNorm) | needs author | `OPEN_QUESTIONS.md` E-11 — CONTRADICTED, decisively; equation merge is mechanical once content is corrected | |
| Minor 28 (author-count errors) | done | see WP-3 above | |
| Minor 29 (CaraServe 1.4/1.7, SLO) | needs author | `OPEN_QUESTIONS.md` E-15 — RESOLVED (1.7× is correct) | |
| Minor 30 (E-9, Switch parameter count) | needs author | `OPEN_QUESTIONS.md` E-9 — CONTRADICTED | |
| Minor 31 (unbalanced parenthesis) | done | see WP-1 above | |
| Minor 32 ("to the best of the author's knowledge", N-3) | done (first hedge) / needs author (superlative + possible 2nd hedge) | see WP-3 above; `OPEN_QUESTIONS.md` N-3 | |
| Minor 33 (E-14, Šajina thesis year) | needs author | `OPEN_QUESTIONS.md` E-14 — RESOLVED (2025 is correct) | |
| Minor 34 (C-8, Pillar-4 denominator) | done | see P1-4/WP-8 above | |
| Minor 35 (C-6, latency cross-ref) | done | see WP-1 above | |
| Minor 36 (S-5, Figure 15) | needs author | not addressed — a figure/table redesign decision | |
| Minor 37 (P1-5, N=120 vs 123) | done | see P1-5 above | |
| Minor 38 (P1-6, Item 16b) | needs author | see P1-6 above | |
| Minor 39 (P1-7, total records) | done | see P1-7 above | |
| Minor 40 (ref [29]/[7] formatting, DOI convention) | done | see WP-4 above | |
| Minor 41 (Appendices B–D → Supplementary) | needs author | a submission-structure decision, not attempted | |

## Citation integrity (E-*)

| Item | Status | Where to look | Response |
|---|---|---|---|
| E-1 | done | `sections/07_moe_routing.tex` — fabricated paragraph removed | |
| E-2 | done (partial — TODO-AUTHOR marker for the replacement citation) | `sections/04_peft.tex` §4.1, §4.3 | |
| E-3 | needs author | `OPEN_QUESTIONS.md` E-3 — CONTRADICTED, swap indicated (evidence: arXiv abstracts only) | |
| E-4 | done | `sections/07_moe_routing.tex` §7.3, §7.4 — both claims corrected/removed | |
| E-5 | done | `sections/03_methodology.tex` Table 7, MAD-X row | |
| E-6 | done (partial — TODO-AUTHOR marker for the replacement citation) | `sections/02_background.tex` §2.3, `sections/09_synthesis_gap.tex` §9.4 | |
| E-7 | done | `sections/08_p2p_federated.tex` §8.2, `sections/03_methodology.tex` Table 7 | |
| E-8 | done | `sections/06_inference_systems.tex` §6.2 | |
| E-9 | done | `sections/07_moe_routing.tex` | |
| E-10 | needs author | `OPEN_QUESTIONS.md` E-10 — CONTRADICTED (inferred from framing, not an explicit denial) | |
| E-11 | done | `sections/02_background.tex`, `sections/04_peft.tex` — equation + prose corrected, duplicate equations merged | |
| E-12 | needs author | `OPEN_QUESTIONS.md` E-12 — no citation exists to check | |
| E-13 | done | see WP-3 above | |
| E-14 | done (annotated, not silently altered — see OPEN_QUESTIONS.md) | `sections/12_appendix.tex` Appendix B | |
| E-15 | done | `sections/03_methodology.tex` Table 7, `sections/06_inference_systems.tex` Table 9 | |

## Scoping and analysis (S-*, N-*)

| Item | Status | Where to look | Response |
|---|---|---|---|
| S-1 | needs author | `OPEN_QUESTIONS.md` S-1; scaffold ready | |
| S-2 | needs author | `OPEN_QUESTIONS.md` S-2 — Ryabinin DHT mechanism checked (identifier-level only); Dec-LoRA no PDF available | |
| S-3 | needs author | `OPEN_QUESTIONS.md` S-3 — 12 distinct profiles (not ~8), 4-way tie found (not 3-way) | |
| S-4 | done | `sections/09_synthesis_gap.tex` — renamed "Requirement profile implied by RQ" | |
| S-5 | needs author | not addressed — a figure/table design decision | |
| N-1 | needs author | `OPEN_QUESTIONS.md` N-1 | |
| N-2 | needs author | not addressed — new search work | |
| N-3 | needs author | `OPEN_QUESTIONS.md` N-3 | |
| N-4 | no action needed | reviewer notes this in the author's favour; no fix required | |

## Consistency and terminology (C-*)

| Item | Status | Where to look | Response |
|---|---|---|---|
| C-1 | done | see WP-1 above | |
| C-2 | done | see WP-3 above | |
| C-3 | done | see WP-2 above | |
| C-4 | done | see WP-2 above | |
| C-5 | done | see WP-2 above | |
| C-6 | done | see WP-1 above | |
| C-7 | needs author | terminology-discipline pass across Sections 6–8 not attempted — a prose-consistency judgement call | |
| C-8 | done | see WP-8 above | |

## Ethics, integrity, MDPI compliance

| Item | Status | Where to look | Response |
|---|---|---|---|
| GenAI disclosure model/date range | needs author | review asks for the Claude Code drafting model + date range, not currently stated | |
| Undermind framing in §3.1 as method | needs author | a scope/emphasis decision | |
| Acknowledgments sentence | needs author | requires confirming with the editorial office | |
| Prior-work overlap (text carryover disclosure) | needs author | requires the author's own knowledge of what was carried over | |
| iThenticate exposure (Appendices B/C to Supplementary) | needs author | same as Minor 41 | |
| Data Availability — verify DOIs/repos resolve | needs author | requires checking live GitHub/Zenodo links, not done in this pass | |
