# D3 — Inter-rater reliability calibration (AI second reviewer)

**Date:** 2026-08-21
**Input relied on:** `S7b_abstract_reviewed_final.csv` (abstract-review pool, 552 records)
**Sample:** deterministic 10% subset, n = 55, drawn with `random.seed(42)` from the abstract pool.
Keyed by **title** (verified unique in pool; `ss_paper_id` is empty for 302/552 rows, so it is NOT a usable key).

## Design
- A spawned AI agent acted as an independent second reviewer.
- **Blind:** the agent received only title/venue/year/abstract + the verbatim screening rubric
  (from `abstract_review.py` `_SUGGEST_SYSTEM`); it did NOT see the original `abstract_decision`.
- Ground truth = the author single-reviewer `abstract_decision` from S7b.

## Results (n = 55; GT 27 KEEP / 28 SKIP; agent 46 KEEP / 8 SKIP / 1 DEFER)

| Metric | 3-way (KEEP/SKIP/DEFER) | Binary (KEEP vs non-KEEP) |
|---|---|---|
| % observed agreement | 56.4% | 58.2% |
| Cohen's κ | 0.153 | 0.174 |
| Landis & Koch | Slight | Slight |

KEEP-positive contingency (binary): TP=25, TN=7, FP=21, FN=2.
Recall on ground-truth KEEPs: 25/27 = 92.6%. Precision (of agent KEEPs): 25/46 = 54.3%.

## Directional bias identified
The AI reviewer was systematically **over-inclusive**: it KEPT 21 of 28 records the single
reviewer had SKIPped (only 2 false negatives), i.e. a broader inclusion threshold. This is a
known failure mode of LLM-assisted screening and must be disclosed, not hidden.

## Validity caveat
This is an **automated reproducibility/calibration check**, NOT a substitute for a genuine
second human rater. The agent shares model-family priming with the author's own LLM-assisted
screening, so the apparent agreement is not a human--human κ, and a low κ here may partly
reflect threshold differences rather than arbitrary screening. Reporting it as an automated
calibration aid is defensible; presenting it as evidence of reliable human double-screening would
not be.

## Decision for manuscript
NOT yet written into the manuscript. A low κ (slight/sometimes 'fair' in other SLRs) is not a
validation to highlight; the honest framing options are discussed with the user before editing
§3.1 / PRISMA item 8 / response letter R1-3.
