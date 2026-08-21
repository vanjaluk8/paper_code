# Phase 3 — Part B Proposal: KEEP/DEFER/SKIP reconciliation (REVIEW BEFORE ANY EDIT)

No `.tex` file has been edited for Part B. This is the evidence trail + proposed corrected
tables for your review. Every cell below traces to a literal value-count run on the named
CSV (Python `csv` module, header excluded). Nothing is inferred from prose.

Data source dir: `slr_engine/snowballing/snowball_output/`

---

## B.2 — Raw value-counts (authoritative)

### `S7a_abstract_reviewed_base.csv` — 464 records (pass 1, base corpus)
`abstract_decision`: **`{'KEEP': 202, 'DEFER': 169, 'SKIP': 93}`**  → sums to 464 ✓
- 202 + 169 + 93 = 464

### `08_abstract_reviewed_2026-05-02.csv` — 552 records (pass 2, extended)
`abstract_decision`: **`{'KEEP': 214, 'DEFER': 173, 'SKIP': 165}`**  → sums to 552 ✓
- 214 + 173 + 165 = 552
- Its 88 `G_SNOW_F` (forward-snowball) subset: **`{'SKIP': 72, 'KEEP': 12, 'DEFER': 4}`** → 88 ✓

### `09_fulltext_review_queue_2026-05-02.csv` — 387 records
`abstract_decision`: **`{'KEEP': 214, 'DEFER': 173}`**  → 214 + 173 = 387 ✓
- All 173 DEFER rows: `fulltext_decision = DEFER`, `pdf_downloaded = NO`
- 214 KEEP rows have 2nd-pass annotations: INCLUDE 81, EXCLUDE 7, DEFER 4, blank 122

### `S7b_abstract_reviewed_final.csv` — 552 records (final consolidated)
`abstract_decision`: **`{'KEEP': 214, 'SKIP': 338}`**  → 214 + 338 = 552 ✓ (no DEFER remains)
- Its 88-pool subset = 12 KEEP / 76 SKIP

---

## B.2 — The arithmetic gap, resolved

The prompt flagged that the 88-pool "12 KEEP; 76 SKIP" cannot reconcile 464-pool
(202/169/93) into combined (214/173/165). Full reconciliation with the true 88-pool split:

| Pool (source) | KEEP | DEFER | SKIP | Sum |
|---|---|---|---|---|
| 464-pool (`S7a` / `08` non-G_SNOW_F) | 202 | 169 | 93 | 464 ✓ |
| 88-pool (`08` G_SNOW_F) | **12** | **4** | **72** | 88 ✓ |
| Combined (`08` all / `S7b`) | 214 | 173 | 165 | 552 ✓ |

- 202 + 12 = **214** ✓
- 169 + 4 = **173** ✓
- 93 + 72 = **165** ✓

**Root cause:** the C.1 search-log row for 2026-05-08 reports the 88-pool as
**"12 KEEP; 76 SKIP"** (72 + 4), folding its 4 DEFER into the SKIP column. The true
intermediate split is **12 KEEP / 4 DEFER / 72 SKIP**. That single row is the only error;
every other number in both tables is CSV-correct.

---

## B.3 — Claim 1 vs Claim 2, resolved

- **The 173 DEFER records DO appear in the full-text review queue file** (`09_…` = 214 KEEP +
  173 DEFER = 387). Claim 2's mechanics ("DEFER advance to the queue") is **true**, confirmed
  by a raw count, not prose.
- Within that queue, all 173 keep `fulltext_decision = DEFER` and `pdf_downloaded = NO` →
  **none advanced to data extraction** (0 among the 190 / 224 extraction set).
- In the **final consolidated** classification (`S7b`) all 173 resolve to **SKIP, not KEEP**:
  S7b's 214 KEEP = 202 + 12 (all from records already KEEP in `08`), i.e. **0 former-DEFER
  became KEEP** → all 173 → SKIP.

**Conclusion:** `tab:abstract`'s numbers (214 / 338 / 552; 38.8% / 61.2%) are **correct**.
Only its **caption wording** is misleading — the 173 DEFER resolved to **SKIP only** (not
"KEEP or SKIP"), and although they entered the queue file they did not proceed to extraction.

---

## B.4 — Proposed corrected tables (NOT applied — for your review)

### (a) `sections/12_appendix.tex` — C.1 log, `2026-05-08` row

| | Cell |
|---|---|
| OLD | `88 added & 12 KEEP; 76 SKIP` |
| NEW | `88 added & 12 KEEP; 4 DEFER; 72 SKIP` |

← each value = the exact `G_SNOW_F` value-count in `08_abstract_reviewed_2026-05-02.csv`
(KEEP 12, DEFER 4, SKIP 72).

### (b) `sections/12_appendix.tex` — `tab:abstract` caption (lines ~230–233)

| | Wording |
|---|---|
| OLD | "…the intermediate second pass carried 173 DEFER records that were resolved to KEEP or SKIP." |
| NEW | "…the intermediate second pass carried 173 DEFER records; all were subsequently resolved to SKIP in the final classification and none advanced to data extraction." |

← "all → SKIP, none → KEEP" is traced (S7b KEEP 214 = 202 + 12; 0 ex-DEFER).

---

## Downstream impact check (ground rule 3)

Changing the 88-pool row to 12/4/72 and rewording the caption does **not** change any
dependent number: 552 total, 214/338 split, 387 queue, 190/224 extraction, 123 final all
stay identical and remain mutually consistent. Re-verified, not assumed.

---

**Action:** confirm the two Part B changes above (a) and (b) and I will apply them to
`12_appendix.tex`. I have **not** edited anything for Part B pending your approval.
