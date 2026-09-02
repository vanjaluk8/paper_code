# Reviewer Rebuttal — Working Notes (do not submit as-is)

Status: WORKING NOTES for the Major-Revision rebuttal. Not ready to paste into the portal.
User directive: leave in memory/disk for now — many reviewer questions do not make sense /
appear written without reading the paper. Do NOT edit the tex based on flawed-premise
questions until each is triaged.

Two batches of reviewer feedback exist. This file tracks BOTH.

---

## Batch 1 (already addressed in tex — see git history)

Reviewer's structural complaint: "23+19=42 documented inclusions vs 123 final; 81 records
via untraced supplementary searches." Root cause: the MDPI manuscript had DROPPED the
older manuscript's explicit "Manual additions (Scopus/WoS forward snowball)" disclosure.

Fix (already applied, compiled clean, 69pp no `??`):
- `03_methodology.tex:82-93` funnel narrative now discloses the 88 forward-snowball records
  -> 12 KEEP / 4 DEFER / 72 SKIP at the second abstract pass -> `abstract-2nd-pass` route ->
  53 of the 123 finals trace to it.
- `03_methodology.tex:198-208` origin paragraph: 70 fulltext-queue + 53 abstract-2nd-pass = 123.

Reviewer's Batch-1 numbers (348 / 154 / 139 / 23 seeds / 19 inclusions / "42") **do not exist
anywhere** in the current tex or data. The reviewer appears to be reading an older/other draft.

---

## Batch 2 — the 12 questions currently being triaged (2026-09)

### Q-A. Study-level extraction sheet "not found — provide it. Fields + controlled values."
- **Already answered.** Appendix `tab:extraction_codebook` (12_appendix.tex ~line 197) is a
  full data-extraction codebook: field name / description / allowed values / coverage ratio
  (e.g. `paper_key`, `source`, `arxiv_id`... 223/224, 220/224). The extraction sheet itself
  (`11_data_extraction_2026-05-12.csv`) is the data-availability artifact.
- Action: rebuttal cites `tab:extraction_codebook` + Data Availability. No tex change needed.

### Q-B. Study-level quality / risk-of-bias judgments; how did quality influence the 5 gaps?
- **Partially answered.** The review reports a quality/appraisal rubric
  (12_appendix.tex, Q1-Q6 reporting-completeness 0-10) and singles out single-reviewer as a
  limitation (`03_methodology.tex:160-181`). A **per-study RoB table is NOT present** and the
  explicit "how quality influenced the gaps" mapping is NOT stated in one place.
- Action (optional, defensible): a 2-3 sentence paragraph in Methodology/Threats stating
  that quality appraisal informed inclusion-exclusion and is reported at the rubric level,
  not as a per-study RoB table (consistent with single-author SLR norms). Could add a compact
  per-group quality summary if reviewer insists. Triage: PARTIAL — response can be honest.

### Q-C. "What evidence supports: AdapterFusion requires all source-task training sets simultaneously? Cite original paper's exact section."
- The manuscript says AdapterFusion "needs shared data to learn fusion [weights]"
  (`09_synthesis_gap.tex:47`) and relies on centralised training data
  (`05_adapter_composition.tex:90`). The claim "requires ALL source-task training sets
  SIMULTANEOUSLY" is a STRONGER claim than the paper makes and than the MS asserts.
- Action: verify against the actual Pfeiffer et al. 2021 paper before repeating the strong
  phrasing. If the original trains on all tasks jointly (it does — AdapterFusion training
  requires the fused task's train set plus the source adapters), cite the exact section
  (AdapterFusion paper §3, fusion-layer training). Triage: LEGITIMATE verification request —
  answer precisely, do not overclaim.

### Q-D. Model Soups: were LoRA A/B factors, full BA deltas, or merged backbone weights averaged? Evidence for applying vision result to independently-init LoRA adapters?
- Manuscript: "Model Soups was demonstrated for vision models" (`05_adapter_composition.tex:188`).
- Action: Model Soups (Wortsman 2022) averages FULL MODEL WEIGHTS (fine-tuned weights of cloned
  runs), NOT LoRA deltas. The reviewer is right that a direct-transfer claim to LoRA A/B factors
  needs support. Triage: LEGITIMATE — the MS already flags it as vision-domain; make explicit
  that Model Soups averages full fine-tuned weights and that its application to LoRA is a
  reasoned extension, not a demonstrated primary result. Add one clarifying clause.

### Q-E. "Does EdgeLoRA actually use structured pruning + quantisation and report 70% memory savings within 2% accuracy?"
- Manuscript states "EdgeLoRA achieves up to 70% memory savings compared to uncompressed
  loading" (`06_inference_systems.tex:137`). The "within 2% accuracy" and "structured pruning +
  quantisation" specific claims are the REVIEWER's framing of the primary source.
- Action: re-verify against Shen et al. 2025 primary source; cite the exact table/figure if we
  repeat 70% / 2%. Triage: LEGITIMATE verification request. Our 70% figure is already present
  and defensible; the 2%-accuracy phrasing should be sourced or dropped.

### Q-F. "Does FlashServe tier adapter weights specifically, or primarily complete model checkpoints?"
- **Already answered** and the reviewer's premise is WRONG vs our text. The MS explicitly says
  FlashServe "tiers adapter weights across GPU" (`06_inference_systems.tex:117`).
- Action: rebuttal quotes our text; the primary source (Chen et al. 2025) should be re-checked
  to confirm where "tier" is scoped (adapter vs checkpoint tiering). Triage: mostly a rebut
  (our text already correct); just re-verify source.

### Q-G. "Which of refs 80-89 and 107-121 have verified DOI resolution and final publication metadata?"
- Data Availability / corpus already records source keys (SCOPUS/ARXIV/WOS) and DOI/arXiv IDs
  per record. A per-reference DOI-verified audit list is not in the MS.
- Action: respond that all included records carry DOI/arXiv and retrieval source in the
  data-availability artifact; offer DOI list. Triage: respond from data, no tex change.

### Q-H. "How many studies support each of G1-G5? How many partial counterexamples?"
- `tab:groups` (03_methodology.tex ~314-328) already gives per-group incl counts (G0=9/18...
  G6=66/30; total 352/123). Support/counterexample breakdown is implicit in synthesis tables
  (09_synthesis_gap.tex has checkbox matrices).
- Action: point to `tab:groups` + synthesis matrices; optionally add a per-gap support/counter
  count sentence. Triage: mostly answered; small optional clarification.

### Q-I. "Why is DHT discovery presented as REQUIRED rather than one candidate among DHT, gossip, federated indexing, replicated registries, hybrid coordination?"
- This is a design-contribution framing question. The thesis positions DHT (its own ★A1/S1
  contribution) as the discovery mechanism. The reviewer wants acknowledgment of alternatives.
- Action: add a sentence in the synthesis/future-work that DHT is one candidate among several
  (gossip, federated indexing, replicated registries, hybrid) and that the open question is
  which scales — partially already echoed in `11_conclusion.tex:160` (gossip open question).
  Triage: reasonable — add a balancing clause. Not a blocker.

### Q-J. "Which searches were explicitly designed to locate competing systematic reviews and surveys?"
- Han et al. 2024 PEFT survey is a seed/positioning reference (in `tab:g0_seeds`).
- Action: honestly state whether a dedicated SR-of-SRs search was run. If not run, say so and
  disclose as a limitation ("we did not run a formal search for competing SLRs; we screened for
  them during snowballing and cite the PEFT survey as positioning"). Triage: answer honestly;
  if no SR-of-SRs search was done, disclose it.

### Q-K. "Will the January 2026 search be updated before submission? How are post-cutoff studies integrated without changing criteria post hoc?"
- The review's search dates are 2026-04-21 (Semantic Scholar) and 2026-05-08 (Scopus/WoS) —
  NOT January 2026. The reviewer's "January 2026" is again a phantom/older date.
- Action: correct the reviewer: searches ran Apr-May 2026. State the search-date/cutoff policy
  and how later works are handled (positioning/future-work cites, not added to corpus post hoc).
  Triage: mostly a correction; add an explicit cutoff-policy sentence if not present.

### Q-L meta (item 12): AI-tool disclosure; AI-generated figures; repo verifiability; prior-publication overlap.
- **AI-tool disclosure: ALREADY PRESENT and MDPI-compliant** (`03_methodology.tex:16-33`):
  Undermind (role + verbatim prompts in Appendix B), Claude/Anthropic Claude Opus 4.5
  (advisory: abstract-review consistency notes, drafting/proofreading). Explicit scope + human
  oversight + author responsibility. Reviewer ask "tool/version/role/human oversight" is fully
  answered. Pure rebut — cite the statement.
  - Sole possible gap: "AI-generated figures/labels" is NOT explicitly called out. Check whether
    any figures were AI-generated; if all are hand/script-built (e.g. TikZ, CSV->plot), say so in
    one line in the rebuttal. The PRISMA figure is hand/authored (prisma.html), not AI-generated.
  - MDPI also requires the same statement near the end (before References). Confirm it appears
    once; if MDPI template wants it in main.tex tail too, that's a formatting check, not content.
- **Repo verifiability (persistent links):** addresses Batch-2 Data Availability concern; offer
  archived DOIs/links. Data Availability statement + exports/scopus,wos archived in slr_engine.
- **Prior-publication overlap:** already disclosed in the same statement
  (`03_methodology.tex:30-33`: derived from doctoral coursework, substantially revised).
  Extend to state thesis/preprint overlap explicitly in rebuttal for completeness.

---

## VERIFICATION RESULT (2026-09-01) — the "small additions" re-checked against real data

I proposed 5 "small defensible additions." grep + data check verdict:

1. **Saturation/stopping criterion** — ALREADY PRESENT and rigorous
   (`11_conclusion.tex:101`, `12_appendix.tex:39-42`): saturation "assessed by overlap
   with pre-validated corpora but NOT formally measured." NOTHING to add.
2. **Primary-study status ("all 123 are primary studies")** — MY DRAFT WAS FACTUALLY
   **WRONG — WITHDRAWN.** The final reading list
   (`writing_materials/13_final_reading_list_2026-05-12.csv`, 123 rows) contains
   **9 rows tagged `contribution_type=survey`** (5 core, 4 background), all with verifiable
   DOIs (e.g. Federated Fine-tuning survey arXiv 2503.12016; FedLoRA survey IJCAI 2025/1196;
   LoRA survey Front.Comput.Sci; meta-llama survey arXiv 2510.12178; P2P-DL overview
   IEEE Access 2024.3442014). So "all 123 are primary studies; no survey counted" would be
   a FALSE assertion. The HONEST statement is a disclosure: "9 of 123 (7.3%) are survey or
   overview contributions retained for field context and taxonomy mapping; the remaining 114
   are primary studies (methods, systems, composition mechanisms); no position or tutorial
   works are included." This directly answers reviewer Q "are all 123 primary studies? If not
   identify reviews separately."
   - NOTE: BitFit and FederatedScope-LLM are MIS-tagged as survey (they are a method and a
     system respectively) — the data's contribution_type tagging is imperfect; if we quote
     "9 surveys" use the recorded field value/7.3% and hedge as "survey-tagged."
3. **DHT as one candidate among alternatives** — GENUINELY NOT PRESENT. Zero balancing
   language in whole paper ("one of several/among/one candidate/not the only" = 0 hits).
   Paper foregrounds DHT as THE mechanism (it is the ★A1/S1 contribution); gossip appears
   only as separate open question. Defensible small clause to add (non-concessive).
4. **SR-of-SRs honesty** — GENUINELY NOT PRESENT. No dedicated search for competing
   reviews/surveys. Honest disclosure: no dedicated SR-of-SRs run; the 9 surveys that
   surfaced during retrieval/snowballing were screened under the SAME eligibility criteria
   and retained as corpus rows (that is how they entered the 123). Defensible one-liner.
5. **Cutoff/post-cutoff policy** — ALREADY PRESENT (`11_conclusion.tex:101`: "papers
   published after the search date (2026-04-21) may address gaps..."). The "January 2026"
   in the reviewer's Q is a PHANTOM — searches ran 2026-04-21 and 2026-05-08. NOTHING to add;
   correct the date in the rebuttal.

ALSO DISCOVERED: `_archive/working/responses_to_reviewers_DRAFT.md` is an EARLIER rebuttal
against a PRIOR simulated review (numbers state "123/121 distinct" before CaraServe
correction). Its R1-4 says the Data Availability names slr_engine public GitHub
(https://github.com/vanjaluk8/slr_engine). DO NOT reuse its funnel numbers verbatim — it
predates the 190/34 correction. main.tex:151 still has a TODO: PLACEHOLDER for papers_code
public URL.

ACTION: apply only clause #3 (DHT-as-one-candidate) and a truthful #4 (SR-of-SRs one-liner)
to tex. Do NOT add #2 as "all primary" — instead optionally add the truthful "9 of 123 are
surveys retained for context" disclosure OR answer it in the rebuttal letter only. #1 and #5
need no tex change.

## Inventory of reviewer numbers vs reality (for spotting phantom premises)

| Reviewer says | Reality in this MS |
|---|---|
| "348 total / IEEE Xplore initial" | 1,150 raw snowball; no 348 anywhere |
| "154 excluded initial" | no such number |
| "139 excluded snowball" | no such number |
| "23 seeds" | 9 foundational seeds, 7 submitted |
| "19 snowballing inclusions" | not a number used in the MS |
| "42 documented inclusions" | 123 (120 distinct) final |
| "81 studies added" | extraction-stage `review_source` abstract-2nd-pass=81; finals=53 |
| "January 2026 search" | searches ran 2026-04-21 and 2026-05-08 |

## Triage summary
- **Pure rebut (reviewer premise wrong vs text):** Q-A, Q-F, Q-K (dates), Batch-1 numbers.
- **Already answered; cite existing text/artifact:** Q-A, Q-H, Q-G.
- **Legitimate verification of a cited primary source (verify then answer, don't overclaim):**
  Q-C (AdapterFusion), Q-D (Model Soups), Q-E (EdgeLoRA), Q-F (FlashServe).
- **Small defensible additions:** Q-B (RoB-how-it-affected-gaps), Q-I (DHT-as-one-candidate),
  Q-J (SR-of-SRs), Q-K (cutoff policy).
- **NOT missing (pure rebut — cite existing text):** Q-L AI-usage statement is already
  MDPI-compliant at `03_methodology.tex:16-33`; false-negative-rate is N/A (no automated
  exclusion); seed set, forward-pass rows, primary-study status already in text/artifacts.
- **User's own clarifications (from prior turn):**
  - Seed set already fully justified (`tab:g0_seeds` + prose); reviewer's "23 seeds" is phantom.
  - Forward-citation service+date already in appendix search log as auditable dated rows
    (12_appendix.tex ~749-754: Scopus 2026-05-08 106->74; WoS 2026-05-08 20->14; G_SNOW_F 88->12K/4D/72S).
  - Saturation stopping criterion: add one explicit sentence.
  - All 123 are primary studies; surveys/background (Han survey, Šajina thesis) already
    segregated as positioning, not counted. State in one place.
  - False-negative rate of automated exclusion: NOT APPLICABLE — no fully-automated exclusion;
    every SKIP/DEFER is a human decision ("AI-assisted, human decision"). Rebut cleanly.

---

## RESOLVED ANCHOR + SINGLE-SOURCE-OF-TRUTH (2026-09-02) — breaks the PRISMA cycle

### Confirmed anchor (user decision, data-verified)
- **123 records = 120 distinct works; 3 works recorded as two entries each.**
- The three duplicate pairs (paper_key): 
  1. LoRA — `2106.09685` ↔ `a8ca46b171467ceb2d7652fbfb67fe701ad86092`
  2. Adapter-based PEFT / Houlsby — `1902.00751` ↔ `29ddc1f43f28af7c846515e32cc167bc66886d0c`
  3. **CaraServe (2024 arXiv) == Toppings (2025 USENIX ATC)** — `2401.11240` ↔ `69d631b3875149050ab3088501cfc9d5cbea9e99`
  - (Caution: earlier "121 distinct" was WRONG — title-only dedup missed the CaraServe→Toppings
    preprint-rename. Treat as ONE work → 120 distinct.)

### Verified non-funnel facts (all now emitted + asserted)
- Final rows 123 · distinct 120 · dup works 3
- **Entry-route split (review_source from 11_data_extraction_2026-05-12.csv):**
  fulltext **70** / abstract-2nd-pass **53**  (all 123 rows carry a value)
- **Group subtotals (tab:groups):** G0=18, G1=17, G2=17, G3=14, G4=16, G5=11, G6=30 → 123 (G1–G6=105)
- **Forward-snowball branch (G_SNOW_F):** 88 added → 12 KEEP / 4 DEFER→SKIP / 72 SKIP.
  This branch is SMALL & contributes few finals — it is NOT the same as the 53 abstract-2nd-pass
  decision-route records (that was Findings 1 & 2 both boiling down to one conflation).
- **Single provenance cross-tab (group × route), all margins = 123:**
  | Grp | fulltext | abs-2nd-pass | total |
  |-----|-----|-----|-----|
  | G0  | 14 | 4  | 18 |
  | G1  | 13 | 4  | 17 |
  | G2  | 13 | 4  | 17 |
  | G3  | 2  | 12 | 14 |
  | G4  | 4  | 12 | 16 |
  | G5  | 7  | 4  | 11 |
  | G6  | 17 | 13 | 30 |
  | Tot | 70 | 53 | 123 |

### New tool: slr_engine/scripts/prisma_facts.py (single source of truth)
- Loads canonical data (13_final list, 11_data_extraction, pipeline_unified, EXPECTED registry).
- Recomputes + asserts the funnel AND the final-list facts above (21 checks, exit 0 = all pass).
- Emits `prisma_facts.json` (single machine-readable number set) + `prisma_numbers.tex`
  (LaTeX \newcommand macros for EVERY number) to `data/snowball_output/generated/`.
- Group closure now inherits the duplicate-partner key so the cross-tab closes on all 123 rows.
- NEXT (Task 3): have main.tex `\input` prisma_numbers.tex, replace the hard-coded prose
  numbers (03_methodology ~88-99 and ~205-218 must stop saying "53 trace to forward snowball"),
  generate the provenance table from the JSON, and gate the build on prisma_facts.py exit 0.
