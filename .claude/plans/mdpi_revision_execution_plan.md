# MDPI SLR Manuscript & Supplementary Package — Revision Execution Plan

**Date:** 2026-08-21 · **Repo:** `litreview-peft-p2p-adapters` · **Manuscript root:** `writing/mdpi_paper/`
**Prior audit work:** `reports/PHASE0–PHASE3` + `PRISMA_NUMBERS_VALIDATION.md` (already done — **reuse & reconcile**, per user).

---

## 0. Ground rules (bind every edit)

1. **Numbers source of truth = pipeline CSVs** (`slr_engine/snowballing/snowball_output/`), computed with Python `csv`, header excluded. Narrative claims = manuscript. Never pick "which looks right."
2. Headline inclusion unit = **121 distinct papers** (123 included records, 2 arXiv+Scopus duplicate key-pairs: LoRA `2106.09685`/`a8ca…`, Houlsby `1902.00751`/`29ddc1…`). Footnote the 123-vs-121 nuance in data files only. **Decided by user.**
3. Every number appears in **7 places** (Abstract, §3.1, Table 1, Table A3, Fig 5, PRISMA checklist, PRISMA summary). Any edit = grep all 7 for the old value.
4. **Never delete limitations** — reframe/strengthen. Use corpus-bounded phrasing ("within the reviewed corpus"), not absolute claims.
5. No fabricated numbers/DOIs/citations. A missing input is a **blocking dependency**, listed as such, not guessed.
6. Keep `REVISION_LOG.md` mapping every change to issue + file.

---

## PHASE 1 — Critical/Blocking (order matters)

### Blocking dependency (do first, unblocks the rest)
- **Force-push rewritten history** (`git push --force origin main`) and **rotate the leaked `sk-ant-api03…` key** → put in `.env`. Manual (user). *No file edits depend on this*, but reviewers need the public/updated repo for item 1.6 wording.

---

### 1.5 Resolve 123 vs 121 — **decided: 121 distinct headline** · Effort: S
Order: **FIRST among content items** (everything else consumes this decision).
- [ ] Verify the 2 duplicate key-pairs in `13_final_reading_list_2026-05-12.csv` (confirm titles/DOIs).
- [ ] `main.tex` abstract: "surveys **123 papers** across five clusters" → keep 123 as counts of reviewed records, add "…surveying **121 distinct papers** (see Table A3)". Ensure no numeric-only "123" that contradicts.
- [ ] Grep `123` vs `121` across Abstract/§3.1/Table 1/Table A3/Fig 5/checklist/summary; add the footnote once (Appendix A3 / Table A3 caption).
- **Result:** consistent "121 distinct / 123 records" story everywhere.

### 1.1 Reconcile the PRISMA package · Effort: S–M · **Depends on 1.5 + 1.4**
- [ ] `PRISMA_2020_checklist.md` (still stale):
  - Line 3 title → match manuscript title exactly.
  - Line 8: "pipeline_unified.csv (622 records)" → **remove the 622 claim**; point to `PRISMA_NUMBERS_VALIDATION.md` master table (the reconciled file).
  - Item 16a line 59: "Figure 1 (`fig:prisma`)" → **"Figure 5"**.
  - Item 11 (line 44) & item 18 (line 62): "Not applicable" → point to new **§3.3 Quality Assessment** (item 1.3).
  - Item 24a (line 84): "state in cover letter" → point to new **registration sentence in §3** (item 1.8).
- [ ] `PRISMA_summary_2026-04-21.md` (stale, ⚠ several `*to be filled*`), regenerate funnel from validation doc:
  - Stage 4 "to be filled" rows → real counts (387 → 224 → 123).
  - Stage 7 references `S8_final_reading_list.csv` → `13_final_reading_list_2026-05-12.csv`.
  - Add 121-distinct note.
- [ ] Single authoritative funnel = `PRISMA_NUMBERS_VALIDATION.md` (already exists). **Adopt verbatim** into Abstract/§3.1/Fig5 caption/checklist/summary — no independent retyping.

### 1.4 Make Fig 5 fully standard · Effort: M · **Depends on 1.5; feeds 1.1**
- [ ] Known mismatch (Phase 2 §B1): figure draws branch `972→…→162 eligible→464→552→123` but **omits 502 merged / 387 queue / 224 extraction**; caption/prose name `502/387/224`. Left intentionally for this phase.
- [ ] Redraw `fig_slr1_prisma_flow` (TikZ or `app/visualise.py` source) so the figure shows the full standard chain left-to-right/top-to-bottom with **per-stage reasons**: Identified 1,150 (SS 450 back + 700 fwd; + 352 pre-validated G0–G6) → duplicates removed 178 → screened 972 → excluded with reasons (year 192 / no-keyword 284 / LLM-only 255 = 731; + triage 60; 19 uncertain) → enriched 464 (tiers 90/141/233) → abstract reviewed 552 (KEEP 214 / SKIP 338) → full-text queue 387 (PDF retrieved 122 / not retrieved 265) → extraction 224 → **final 123 (121 distinct)**.
- [ ] Source of truth for the figure: `app/prisma.py` + `app/visualise.py` (already emit PDF). Update the generator, regenerate PDF, place in `writing/mdpi_paper/figures/`.
- [ ] After regen, verify figure, caption, §3.1 prose, Appendix A, checklist, summary **all name the same chain**.

### 1.2 Replace placeholder figures (original TikZ) · Effort: M · Independent
- [ ] **Figure 2** = `fig:peft_adapter_types` (`02_background.tex:100–112`): side-by-side (a) bottleneck adapter, (b) LoRA, (c) prefix tuning at module level. Replace `\fbox` placeholder with **TikZ** (`tikz` already required by `mdpi.cls`). Caption text already correct — keep.
- [ ] **Figure 6** = `fig:houlsby_adapter` (`04_peft.tex:55–73`): full bottleneck adapter incl. LayerNorm step per Eq. 6 context. Replace placeholder with TikZ.
- [ ] Bonus (Phase 4 requires *no placeholder anywhere*): also fill the other 4 placeholder frames in `04_peft` (taxonomy), `05_adapter_composition` (AdapterFusion), `07_moe_routing` (Switch Transformer), `08_p2p_federated` (Petals) — at minimum as clean TikZ schematics consistent with captions.
- [ ] Verify captions match rendered content exactly.

### 1.3 Quality-appraisal / risk-of-bias framework · Effort: M · Independent · ✅ DONE
- [x] **Instrument** (§3.3, new): 6 dimensions — publication/peer-review status; venue tier; code/artifact availability; result reproducibility; baseline adequacy; evaluation realism + threats-to-validity reporting. 3-level rubric (0/1/2) per dimension → 0–12 score → aggregate banding table.
  - ⚠ 4 of the literal 6 dimensions (code availability / reproducibility / baseline adequacy / threats) have **no grounded data** anywhere (datasets/metrics/method_name are empty schema columns in `11_data_extraction_*`; no code/repo column exists). Per the no-fabrication rule, these are **scoped out and disclosed** in §3.3 (user-approved: "Scope out, disclose"). Actual rubric is fully grounded → **Q1** publication&venue (S6 `venue_quality`), **Q2** record resolvability (DOI/arXiv union), **Q3** methods specificity, **Q4** evaluation-claim specificity, **Q5** contribution clarity, **Q6** synthesis relevance (tier). N=123, mean 7.17, SD 2.09, bands **18/57/46/2**.
- [x] **Score all 123** from **existing fields** (user choice). `slr_engine/snowballing/quality_appraisal.py`; outputs `writing/mdpi_paper/figures/quality_appraisal_scored.csv` + `fig_slr_quality_bands.pdf` (both local, regenerable — only the script is tracked).
- [x] New `\subsection{Quality Assessment}` in `03_methodology.tex` (**§3.3**, after §3.2) — instrument, rubric (`tab:quality_rubric`), aggregate distribution, scoped-out dims disclosure. Added `\newcommand{\textstar}` to `main.tex` preamble.
- [x] Update checklist item 11 & 18 → point to §3.3 (`sec:methodology:quality`) + Fig. 6 (`fig:quality_bands`).
- [x] **Data need:** confirmed `S6_enriched_reading_pool.csv` `venue_quality` covers all 123 (top_venue 63 / peer_reviewed 47 / preprint 11 / unknown 2); join via paper_key→arxiv/doi + title crosswalk, all 123 join. ✅

### 1.6 Data Availability → two-project split (user's design) · Effort: M · User-driven
Per user: **split into two projects**: (1) snowballing **code** in one repo; (2) clean **literature sources + materials** in another.
- [ ] Decide repo locations/names with user (suggest: repo A = existing `litreview-peft-p2p-adapters` (code+engine); repo B = new, private, for `papers_repo/`, CSVs, PRISMA/figures sources, validation docs). Both **private/internal**, shared with reviewers — compliant with security policy (no public publish via my actions).
- [ ] Rewrite `\dataavailability{…}` in `main.tex` from "available from the author upon reasonable request" → concrete, specific statement listing both repos (or "available at [private repo URL] shared with reviewers; public release/DOI deferred until after thesis examination" — concrete reason, not a generic clause).
- [ ] Update checklist item 27 to name the two repos + stable refs.
- [ ] **Blocking dependency on user:** exact repo names/URLs and the public-vs-private decision per repo.

### 1.7 Back matter · Effort: S · ✅ DONE
- [x] Added `\acknowledgments{None.}` (class defines but does NOT auto-emit the heading; placed before `\conflictsofinterest` per mdpi.cls order). ⚠ Note: `Author Contributions` and `Funding` are also absent from back matter — out of this task's scope; flag for reviewer compliance check.
- [x] ORCID confirmed correctly encoded: `\orcidauthorA{0009-0009-8142-6890}` (main.tex:27) + `\orcidA{}` (main.tex:39) → `\href{https://orcid.org/0009-0009-8142-6890}{\orcidicon}`. **Dep: `Definitions/logo-orcid.pdf` missing locally** → `\orcidicon` would fail to compile until restored from official MDPI template (icon asset; cannot fabricate).

### 1.8 Protocol registration statement · Effort: S · Independent · ✅ DONE
- [x] Added sentence at start of §3 Methods: review not prospectively registered; CS/AI SLRs not commonly PROSPERO-eligible; no suitable AI-specific registry at commencement. (No OSF/protocols.io claim — no evidence.)
- [x] Checklist item 24a updated → points to §3 (`sec:methodology`); 24b already pointed to §3/Appendix A (left); 24c remains "Not applicable (no registration)" (correct).

---

## PHASE 2 — Major methodological fixes

| Item | Effort | Notes |
|---|---|---|
| **2.1 Single-reviewer bias mitigation** | M | Add calibration: 10% random sample independently screened by 2nd reviewer → report % agreement / Cohen's κ in §3.1/Appendix A; reference in checklist item 8. **Needs the 2nd reviewer's actual decisions** (blocking data — ask user/supervisor). |
| **2.2 G0 seed justification table** | S–M | ✅ DONE — added `tab:g0_seeds` (9 seeds, venue, one-line role; citation column omitted — 6/9 S1 counts NaN) + threat-to-validity para on ≥300-cite bias. |
| **2.3 Search-strategy provenance split** | S | ✅ DONE — §3.1: 123 = **105 curated G1–G6 + 18 snowballing**; corrected Table 1 per-group counts to S6 seed_group truth (G0:18,G1:17,G2:17,G3:14,G4:16,G5:11,G6:30; dropped stale "Other:15"). ⚠ verify G0 remap. |
| **2.4 Fix circular arXiv criterion** | S–M | Replace "arXiv cited by ≥1 work in corpus" (circular) with corpus-independent proxy — Semantic Scholar ≥N citations, or resubmission/official status. Document trade-off in A.3. **Needs current citation counts** via API (network) or a supplied snapshot. |
| **2.5 Positioning vs existing surveys** | S | New short subsection (end of Intro or start §9) vs Han2024/Wang2024/Mao2024, MoE, FL/decentralised surveys — state the exact synthesis gap this review closes. |
| **2.6 De-escalate overclaiming** | S | Grep §9/§10 for "no existing system / no prior work / novel / primary analytical contribution" → corpus-bounded phrasing. |
| **2.7 Data-extraction codebook** | M | Table/appendix defining every column of `11_data_extraction_2026-05-12.csv` (columns confirmed: `contribution_type, method_name, peft_technique, distribution_mechanism, contribution_codes, datasets, metrics, key_finding`, etc.): meaning, allowed values, consistency check. |

---

## PHASE 3 — Minor polish & compliance

| Item | Effort | Notes |
|---|---|---|
| **3.1 Abstract restructuring** | S | Background→Methods→Results→Conclusion signal via sentence sequence (no subheads). |
| **3.2 Reference hygiene** | M | Replace arXiv-DOI refs where a peer-reviewed version exists; spot-check 2025–26 entries. **Some already done in Phase 1.** Needs care not to break the 17 verified DataCite DOIs. |
| **3.3 AI-tool disclosure** | S | Expand Methods AI disclosure → MDPI-style: tool+version, exact purpose, explicit authorial-responsibility sentence. |
| **3.4 Table/figure cleanup** | S | Simplify Fig 5 caption to PRISMA-standard terms only; consider splitting dense Table 2 per pillar. |
| **3.5 Repository references** | S | Replace bare filenames (`log_screening_…json`) with stable URL/DOI refs in text. |
| **3.6 Terminology pass** | S | Grep decentralised/peer-to-peer/distributed/serverless; consistent first-use definitions. |

---

## PHASE 4 — Final verification pass

1. **Recompute entire funnel** from raw CSVs independently (Script 1.3 / validation script); confirm matches the 7 places.
2. **Grep all stale values**: `622`, "Figure 1"→PRISMA, "123 papers vs 121 distinct", "eight … seed", `S8_final_reading_list`, `*to be filled*`.
3. **Grep for placeholder text**: `create original figure here`, `to be filled`, `\fbox (create…`.
4. **Similarity focus pass** on background/method boilerplate.
5. Produce **`REVISION_LOG.md`** mapping each Phase 1–3 item → diff/commit, for the response-to-reviewers letter.

---

## Summary of blocking dependencies (cannot fabricate — need from user / external)

| # | Dependency | Why |
|---|---|---|
| D1 | **Force-push + key rotation** (manual) | Repo hygiene, reviewers need updated root for 1.6 |
| D2 | **Two-project repo names/URLs** + public-vs-private per repo | 1.6 wording |
| D3 | **2nd reviewer's 10% calibration decisions** | 2.1 κ/agreement |
| D4 | **Current citation counts** for 123 (or permission to hit Semantic Scholar API) | 2.4 external proxy |
| D5 | Confirm `S6` venue_quality covers all 123 | 1.3 auto-scoring |

## Effort summary
- **S:** 1.5, 1.7, 1.8, 2.2, 2.3, 2.5, 2.6, 3.1, 3.3, 3.4, 3.5, 3.6
- **M:** 1.1, 1.2, 1.3, 1.4, 1.6, 2.4, 2.7, 3.2
- **L:** none (split finely enough to avoid single large risky diffs)

## Suggested order of operations
D1(manual) → **1.5** → **1.4** (figure) → **1.1** (checklist/summary, consumes 1.5+1.4) → **1.3** (quality; independent, but wire checklist 11/18 here) → **1.2** (figures, independent) → **1.8** → **1.7** → **1.6** (needs D2) → then Phase 2 (2.4 needs D4; 2.1 needs D3) → Phase 3 → Phase 4 verification + REVISION_LOG.
