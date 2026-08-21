# Phase 3 — G0 Seed-Count & KEEP/DEFER/SKIP Reconciliation (applied)

Fixes two confirmed inconsistencies in `writing/mdpi_paper/`. **Part A (G0 "eight"→"nine",
3 locations) applied & verified. Part B (KEEP/DEFER/SKIP) applied after review, with every
number traced to a literal CSV value.** No fabricated explanation was used — any cell that
could not be traced would have been flagged ⚠️ UNRESOLVED; none remained.

---

## PART A — G0 seed count "eight" → "nine" (APPLIED)

### Ground truth (two independent sources)
- `papers_repo/G0_seed_papers.md`: **9** bullets (`grep -c '^- '` = 9).
- `S7b_abstract_reviewed_final.csv`: `direction == SEED` → **9** rows.
- **G0 (corpus) = 9.** ✅

### Applied edits (before → after)
| File:line | Before | After |
|---|---|---|
| `sections/03_methodology.tex:21` | "anchored on **eight** foundational seed papers (Group G0) selected" | "anchored on **nine** foundational seed papers (Group G0) selected" |
| `sections/11_conclusion.tex:12` | "…assembled from **eight** seed papers and six thematic pre-validated groups." | "…assembled from **nine** seed papers and six thematic pre-validated groups." |
| `sections/12_appendix.tex:669–670` | "The **eight** G0 seed papers were submitted for both backward… and forward… retrieval." | "The G0 corpus comprises **nine** seed papers; **seven** of these were submitted for both backward… and forward… retrieval via the Semantic Scholar API." |

### Full-inventory note (ground rule 2 — checked ALL files)
Only the 3 G0-referring instances changed. Unrelated "eight" left intact:
`03:5` & `11:11` Xiao–Watson "eight-step" (correct), `05_adapter_composition:195`
("all eight [GLUE]"), `09_synthesis_gap:59` ("eight open research questions").
`03:52` table G0 row already 9 — unchanged (verified).

### Why 12:669 distinguishes 9 vs 7
The API retrieval log `log_retrieval_2026-04-21.json` (`_meta.n_seeds`) = **7** (the two
Šajina papers were not in the API run), while the G0 corpus = 9. The reworded sentence
reports both accurately. (The PRISMA figure's "n = 8" is a separate artifact of
`visualise.py` rendering `len(retrieval_log)` = 7 seeds + the `_meta` key; it lives in the
figure/PDF, not the `.tex`, and is out of scope for this .tex-fix.)

### Re-verification (ground rule 2 & 3)
- Zero remaining `eight…seed` matches across `sections/*.tex` + `main.tex` ✅
- Xiao–Watson "eight-step" (03:5, 11:11) intact ✅
- `tab:groups` G0 row = 9; 352 total (9+343) consistent ✅

---

## PART B — KEEP/DEFER/SKIP reconciliation (APPLIED after review)

### Root cause found — the C.1 88-pool row folded its 4 DEFER into SKIP
| Pool (source CSV) | KEEP | DEFER | SKIP | Sum |
|---|---|---|---|---|
| 464-pool (`S7a` / `08` non-G_SNOW_F) | 202 | 169 | 93 | 464 ✓ |
| 88-pool (`08_…_2026-05-02.csv` G_SNOW_F subset) | 12 | **4** | **72** | 88 ✓ |
| Combined (`08` all / `S7b`) | 214 | 173 | 165 | 552 ✓ |

Cross-sums now exact: 202+12=214 ✓ · 169+4=173 ✓ · 93+72=165 ✓.
The old row "12 KEEP; 76 SKIP" (72+4) was the single arithmetic error.

### Claim 1 vs Claim 2 resolution (from data, not prose)
- The 173 DEFER **are present** in `09_fulltext_review_queue_2026-05-02.csv` (387 = 214 KEEP
  + 173 DEFER) → they **did enter the full-text queue** (Claim 2's mechanics true).
- All 173 have `fulltext_decision = DEFER` and `pdf_downloaded = NO` → **none advanced to
  extraction** (0 among the 190/224).
- Final consolidated `S7b`: all 173 → **SKIP** (0 → KEEP; S7b KEEP 214 = 202 + 12).
- → `tab:abstract` numbers (214/338/552; 38.8%/61.2%) were correct; only the **caption
  wording** was misleading.

### Applied edits (before → after), `sections/12_appendix.tex`
**(a) C.1 log `2026-05-08` row (line 650):**
- Before: `88 added & 12 KEEP; 76 SKIP`
- After: `88 added & 12 KEEP; 4 DEFER; 72 SKIP`
  ← = exact G_SNOW_F value-count in `08_abstract_reviewed_2026-05-02.csv`.

**(b) `tab:abstract` caption (lines ~230–233):**
- Before: "…the intermediate second pass carried 173 DEFER records that were resolved to
  KEEP or SKIP."
- After: "…the intermediate second pass carried 173 DEFER records; all were subsequently
  resolved to SKIP in the final classification and none advanced to data extraction."

### Downstream check (ground rule 3)
No dependent number changed: 552 total, 214/338 split, 387 queue, 190→224 extraction, 123
final all remain identical and mutually consistent. Re-verified. All other `DEFER` mentions
(222, 258, 639, 641, 642, 643) remain correct and conflict-free.

---

## Reports produced this phase
- `PHASE3_PARTB_PROPOSAL.md` — the pre-application evidence trail (retained for audit).
- `PHASE3_REPORT.md` (this file).

## Compile note
No local LaTeX toolchain; all checks are structural (refs/includes/percent math + traced
counts). Final Overleaf compile remains the user's step.
