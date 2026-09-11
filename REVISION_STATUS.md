# REVISION_STATUS.md

Task-by-task status tracker for the `REVIEW_REMEDIATION.md` revision of the MDPI
*AI* systematic-review manuscript.

- **Session date:** 2026-09-10
- **Legend:** `DONE` = change in LaTeX source, author to review diff · `SKIPPED` =
  deliberately not done (reason inline) · `DEFERRED` = blocked on external data,
  instruction file written · `PARTIAL` = fallback applied, decision still open ·
  `TODO` = not started, needs author
- Fill in the **"What was done"** line under each task as you work / review.

---

## Summary

| Phase | Done | Skipped/Deferred | Partial | TODO (author) |
|---|---|---|---|---|
| 1 — Blockers (B1–B9) | B1, B2, B3, B4, B5, B6, B7, B8, B9 | — | — | — |
| 2 — Major (M10–M21) | M11, M12, M13, M14, M15, M16, M17, M18, M19, M20, M21 | M10 (skip — not mandatory) | — | — |
| 3 — Minor (N22–N49) | N22, N23, N24, N25, N26, N27, N29, N30, N31, N32, N33, N34, N35, N36, N37, N38, N39, N40, N43, N44, N46, N47, N49 | N28 (skip); N41, N42, N45, N48 (deferred — author) | — | — |

---

# PHASE 1 — Desk-check blockers

## B1 — Remove the mentor consultation note — `AGENT-OK` — **DONE (neutralised as comment, via M12)**
Croatian/English `\mentornote{...}` block at `03_methodology.tex` (macro
`main.tex:30`).
- **What was done (2026-09-10):** per author, not deleted but converted to a
  plain-English `%` source comment (see M12). It no longer renders and no
  longer contains any trigger word. **Residual:** the `\newcommand{\mentornote}`
  macro at `main.tex:30` is now unused — harmless, can be left or removed at
  submission. A tree grep for the other keywords
  (`TODO|FIXME|XXX|POGLEDATI|REMOVE BEFORE|placeholder`) is part of the Phase 4
  pre-submission pass.

## B2 — Add corresponding-author ORCID — `GATE:AUTHOR` — **DONE**
Already implemented: `main.tex:34` `\orcidauthorA{0009-0009-8142-6890}`,
`main.tex:46` `\Author{Vanja Luk $^{1,}$*\orcidA{}}`. Verified the iD resolves at
`pub.orcid.org` and belongs to "Vanja Luk". No change made.
- **What was done:**

## B3 — Cite the three orphaned float items — `AGENT-OK` — **DONE**
- Table 1 (`tab:g0_seeds`): added `Table~\ref` at `03_methodology.tex:38`.
- Figure 10 (`fig:peft_paradigm`): already had a `\ref` at
  `06_inference_systems.tex:6` — no change needed.
- Table A5 (`tab:abstract`): added `Table~\ref` at `12_appendix.tex` (§A.7 prose
  before the table).
- First-mention order verified ascending in main text and appendix.
- **What was done:**

## B4 — Reconcile Table 7 evidence base with claim scope — `GATE:AUTHOR` — **DONE (Option B)**
Author chose **Option B** (narrow the claim). Changes:
- Abstract (`main.tex`): "no reviewed system simultaneously addresses…" →
  "Across the 17 systems compared in the review's concept matrix…none
  simultaneously addresses…". Abstract now ~192 words (limit 200).
- §10.2 (`11_conclusion.tex:64`): "none of the 123 reviewed records…" → scoped
  to "the 17 systems it scores… (selection rule in §9.2)".
- §9.2 (`09_synthesis_gap.tex`): new **"System selection for the matrix"**
  paragraph documenting how the 17 were chosen (mandatory sub-task).
- Table 7 caption: now "17 selected systems… illustrative cross-section… not an
  exhaustive scoring".
- §9.2 combined-profile line: "No reviewed system…" → "None of the 17 systems
  scored…".
- §10.4 Limitations: new paragraph disclosing 17-vs-123 scope + naming
  full-corpus scoring as future work.
- Left as-is: per-dimension "no reviewed work does X" statements in §9.3 (rest on
  narrative synthesis, no count cited).
- **What was done:**

## B5 — Rebuild Figure 5 as two-column PRISMA 2020 — `AGENT-OK`/`GATE` — **DONE (converging two-column)**
Author approved the **converging two-column** layout (strict two-column not
possible — needs the per-discovery-route split of the 123, which is task N38).
- `figures/prisma.html` rewritten; `figures/fig_slr1_prisma_flow.pdf` regenerated
  (headless Chrome), old version replaced (recoverable via git).
- §3 caption (`03_methodology.tex:450`) rewritten: describes both columns, all
  junctions, and the 70/53 split.
- **Folds in:** N29 (19 UNCERTAIN excluded: 972 = 810 + 162), N30 (reports
  sought / not-retrieved boxes; 24 not retrieved; 173 DEFER not carried
  forward), N32 (38 at enrichment = 6 off-topic + 32 rescue-file "later confirmed
  excluded"), N33 (no "MERGE" band), M19 (INCLUDED splits 70 full-text-queue +
  53 abstract-2nd-pass).
- **Open:** figure is landscape-ish; may want `figure[p]` / sideways float —
  judge on compile.
- **What was done:**

## B6 — Report the G1–G6 (Undermind) identification funnel — `GATE:AUTHOR` / `BLOCKED:NEEDS-DATA` — **DONE (fallback: exported-list funnel; pre-export pool disclosed as unrecoverable)**
Funnel recovered from the `mdpi_slr_engine` sibling repo. Per group, **Undermind
export → pre-validated (post cross-group dedup) → in final 123**:
G1 62→59→17 · G2 42→37→17 · G3 96→95→14 · G4 56→51→16 · G5 46→35→11 ·
G6 75→66→30. Totals **377 → 343 → 105**; +9 G0 seeds = 352 pre-validated.
Sources: `data/inputs/G*.csv` (exported ranked lists), `S1_prevalidated_corpus.csv`
/ `00_prevalidated_2026-04-21.csv` (`seed_group` counts = Table 3's "n pre-val."),
`pipeline_unified.csv` (`in_final_list_123` × `direction` = 105 PREVALIDATED +
4 SEED + 10 FORWARD + 4 BACKWARD = 123). Undermind searches run **2026-04-14**
(RESEARCH_DIARY; metadata corrected 2026-04-17). `log_retrieval_2026-04-21.json`
covers only the snowball route.
- **Not recoverable:** the pre-export candidate pool Undermind evaluated per
  query. No repo/log/diary retains it. Disclosed as an identification-stage
  audit-granularity limitation (Step-3 fallback from the instruction file),
  parallel to the abstract-review SKIP granularity disclosure.
- **Changes:**
  - §3.1 (`03_methodology.tex`): new funnel paragraph (dates, 377→343→105,
    manual-assessment statement, pre-export-pool disclosure).
  - Table 3 (`tab:groups`): new **U. export** column (62/42/96/56/46/75, total
    377); caption rewritten to explain 377→343→352 and the pre-export-pool gap.
  - Appendix A.1 (`12_appendix.tex`): new **Table `tab:undermind_funnel`**
    (per-group exported/pre-val/final) + two paragraphs (funnel walk-through +
    Step-3 disclosure).
  - §10.3 Threats (`11_conclusion.tex`): second granularity-limitation sentence
    for the Undermind identification stage.
  - Figure 5 (`prisma.html` + regenerated `fig_slr1_prisma_flow.pdf`):
    pre-validated box now "377 exported − 34 cross-group dups = 343; + 9 G0
    seeds = 352"; §3 figure caption updated to match. Also fixed a
    pre-existing (non-B6) error caught during the consistency pass: the
    snowball box + caption said "9 / nine G0 seeds → 1,150" but only 7 were
    submitted (`log_retrieval` n_seeds=7) — now "7 of the 9 G0 seeds".
  - §3.2: "85.4% of the final corpus" → "contribute 105 of the 123 final
    records (85.4%)" (makes the 105 explicit).
  - Appendix D.1 search-log table (`tab:search_log`): three new top rows —
    2026-04-14 Undermind six-query deep search (→ 377 exported), 2026-04-14
    cross-group dedup + G0 join (→ 352), 2026-04-17 metadata correction (no
    record change) — plus footnote (a) on the pre-export-pool gap. The log
    previously started at the 2026-04-21 snowball and never mentioned the
    Undermind route.
  - `supplementary/PRISMA_2020_checklist.md` Item 6: adds 2026-04-14 Undermind
    date + funnel summary.
  - `supplementary/PRISMA_NUMBERS_VALIDATION.md`: §B rebuilt as the funnel
    table (U.export / pre-val / final per group + arithmetic), row 1b updated,
    2026-09-10 changelog entry.
- **Consistency-pass fixes (2026-09-10, follow-on):**
  - §3.1 and Appendix A.1: reworded "of the 343 curated records, 105 retained"
    → "105 of the 123 final records carry a G1--G6 attribution" — the 105 is a
    pipeline group-label count, **not a strict subset of the 343**, because the
    LoRA and Houlsby seed papers are booked under G1/G2 in
    `pipeline_unified.csv` though they entered as G0 seeds.
  - Table 3 footnote[1]: "Houlsby is absent from its group bookkeeping" was
    **factually wrong** vs current `pipeline_unified.csv` (Houlsby's records are
    tagged G2). Rewritten: "the pipeline attributes their records to G1 (LoRA)
    and G2 (Houlsby)… both also returned by those groups' Undermind searches".
  - **Table 3 footnote never rendered** (pre-existing bug, unrelated to B6):
    `\footnotetext[1]{}` after a `\begin{tabular}` inside `table[H]` is silently
    dropped by the MDPI class — the caption's superscript "1" pointed at nothing.
    Converted to an in-tabular `\multicolumn{6}{p{0.95\linewidth}}{\footnotesize
    …}` note row after `\bottomrule` (the pattern Table 4 already uses and that
    renders), and dropped `\protect\footnotemark[1]` from the caption. The
    corrected G0 = 18 explanation is now visible below the table. Verified in
    the compiled PDF.
  - `tab:undermind_funnel` caption: notes the G1/G2 Final cells each include one
    G0 seed paper, so Final sums to 105 by label, not as a subset of Pre-val.
  - §10.3: "which supplied 105 of the 123" → "to which 105 of the 123 … are
    attributed" (neutral wording).
- **Author confirmations received (2026-09-10):** query date 2026-04-14 is
  correct; the six verbatim Undermind prompts in Appendix B are the
  reproducibility record (no separate version string needed); the manual
  keep/drop rule stays as the §\ref{sec:methodology:eligibility} criteria,
  left as-is per author.
- **Instruction file:** `B6_undermind_funnel_TODO.md` (superseded — resolution
  recorded there).
- **What was done:** Executed 2026-09-10 (this session). All edits above are in
  the LaTeX source; `fig_slr1_prisma_flow.pdf` regenerated from the edited
  `prisma.html` (headless Chrome). `latexmk` compiles clean — exit 0, **75 pp**
  (was 74; +1 from the new funnel prose/table), no undefined refs/citations, no
  new overfull boxes (same pre-existing 10). Every number cross-checked against
  `mdpi_slr_engine` data (`data/inputs/G*.csv`, `S1_prevalidated_corpus.csv`,
  `pipeline_unified.csv`, `log_retrieval_2026-04-21.json`) and against
  `supplementary/PRISMA_NUMBERS_VALIDATION.md`. Files touched:
  `sections/03_methodology.tex`, `sections/11_conclusion.tex`,
  `sections/12_appendix.tex`, `figures/prisma.html`,
  `figures/fig_slr1_prisma_flow.pdf`, `supplementary/PRISMA_2020_checklist.md`,
  `supplementary/PRISMA_NUMBERS_VALIDATION.md`. Author to review diff.

## B7 — Source or delete the "5–13%" miss-rate estimate — `GATE:AUTHOR` — **DONE (deleted)**
Author chose to delete. `11_conclusion.tex` §10.3 (Internal validity): removed
"Single-reviewer screening has been estimated elsewhere to miss on the order of
5–13%…" (borrowed clinical-screening statistic, doesn't transfer to a
single-author keyword-assisted CS review). Also rewrote the adjacent sentence
"We consider…" → "The author treats… as the two principal threats… and does not
claim to have eliminated either" (3rd person singular). No citation added.
- **What was done:**

## B8 — Fix the Model Soups attribution in §10.1 — `AGENT-OK` — **DONE**
`11_conclusion.tex` Finding 2: rewritten to rest on LoraHub + LoraRetriever;
Model Soups \cite{Wortsman2022} demoted to "the underlying weight-averaging
precedent… demonstrated on full fine-tuned vision models averaged from a common
initialisation on the same task, not on independently trained adapters" — now
matches the correct treatment in §5.6.
- **What was done:**

## B9 — Resolve the Data Availability contradiction — `GATE:AUTHOR` — **DONE (Option A)**
Author: no blocker, will commit the files. Changes:
- DAS (`main.tex:137`): removed "…not separately version-controlled"; now names
  every per-record artefact as version-controlled in `mdpi_slr_engine`
  (`13_final_reading_list…csv`, `pipeline_unified.csv`,
  `log_retrieval…json`, `log_screening…json`, `S7b_abstract_reviewed_final.csv`,
  `11_data_extraction…csv`, `14_final_curation_reasons.csv`,
  `PRISMA_summary…md`) + verification scripts + S2.
- `03_methodology.tex:427`: `14_final_curation_reasons` → `….csv`.
- `supplementary/PRISMA_2020_checklist.md` Item 27: updated to match; removed
  stale "`papers_code` is private" / "available on request" text.
- **Author action items before submission:** (1) commit those 7 files +
  `verify_*.py` + `snowball_output/verification_runs/` to `mdpi_slr_engine`;
  (2) make `mdpi_paper_slr` public; (3) confirm `14_final_curation_reasons.csv` name
  + extension.
- **What was done:**

**SUPERSEDED (2026-09-11):** the ownership model was revised — `mdpi_slr_engine`
is now **code-only** (the pipeline source + `verify_*.py` scripts), and *all*
per-record artefacts and the `snowball_output/verification_runs/` outputs are
version-controlled in `mdpi_paper_slr`. The Data Availability statement, S1
Item 27, `README.md`, `supplementary/README.md`, and this note were updated to
match. The historical B9 wording above records the earlier decision only.

---

# PHASE 2 — Major methodological issues

## M10 — Strengthen quality assessment toward risk-of-bias — `GATE:AUTHOR` — **SKIPPED (not mandatory)**
Would extend the verified §3.4.1 full-text check to baseline adequacy +
threats-to-validity reporting across ≥48 Tier-1 records, reported as a distinct
instrument.
- **Author (2026-09-10): skip — not mandatory.** Rationale: MDPI will not
  desk-reject; PRISMA Item 11 is satisfied in form by §3.4 (0–10 reporting
  rubric) + §3.4.1 (verified, dated, per-row artifact-availability check over 33
  systems — a real finding), and §3.4 is candid that a formal risk-of-bias tool
  (RoB 2 / ROBINS-I) does not apply to CS methods/systems papers. It is a
  hardening item, not a blocker.
- **If a referee later asks:** the fix is a reading pass over the 48 Tier-1
  records scoring (a) baseline adequacy and (b) explicit threats-to-validity
  reporting, published per-record. Do it in the same pass as any future B4-A
  full-text re-read. Instructions to build the scoring sheet can be prepared
  then.
- **What was done:** status → SKIPPED per author; no source change.

## M11 — Qualify the Wohlin snowballing claim — `AGENT-OK` — **DONE (Option B)**
Author chose (b): restate as single-wave, no 2nd wave.
- **What was done (2026-09-10):** reworded in all five spots —
  `main.tex` abstract ("a single-wave Wohlin et al.\ snowballing pass";
  abstract now 197 words, still < 200), `03_methodology.tex:6` ("a single-wave
  adaptation of the citation-snowballing procedure of Wohlin et al.\ … not
  iterated to saturation"), `11_conclusion.tex:12` (§10.2 lead), `12_appendix.tex`
  §A.2 (adds "the procedure as published is iterated until no new studies are
  found, whereas this review executed one forward/backward wave only") and §D.2.
  §10.3 already carried the one-wave / no-stopping-criterion disclosure. Compiles
  clean.

## M12 — Inter-rater gap — `AGENT-OK` — **DONE (Option C: disclosure only)**
Author: single-user SLR; keep the disclosure, and keep the mentor note as a
source comment so it neither renders nor trips validation.
- **What was done (2026-09-10):**
  - The single-reviewer disclosure + the (correct) refusal to compute κ against
    the non-independent classifier is already the full text of the "Screening
    Reviewer Configuration" paragraph in §3.2 — no change needed there.
  - `\mentornote{OVAJ DIO TREBA … MENTOR …}` block at `03_methodology.tex:250`
    replaced with a plain English `%` comment (records the A/B/C options and the
    "C, disclosure-only" decision). It no longer renders **and** no longer
    contains any Phase-4 trigger word (`TREBA/OVAJ/ODLUČITI/MENTOR/REMOVE
    BEFORE`) — so the pre-submission keyword grep is now clean here.
  - This also closes **B1** in substance (mentor note neutralised, not deleted,
    per author).

## M13 — Make the adversarial search systematic — `AGENT-OK` — **DONE (Option A: documented grey-lit search)**
The disconfirming counter-search (Bittensor, Platformless AI) was non-systematic.
Author chose Option A — document it rather than demote it.
- **Search run 2026-09-10 (agent, via web/arXiv/GitHub search):** 8 queries, no
  venue/peer-review filter, following Garousi et al.\ 2019 (`Garousi2019`,
  added to bib) grey-literature / MLR guidelines. Screening criterion: a
  system/protocol/project combining (i) adapters/LoRA as the exchange unit over
  a frozen shared backbone with (ii) a coordinator-free P2P topology; noted also
  discovery + composition.
- **Result: 0 matching artefacts.** Near-misses catalogued by category (each
  covers one facet): decentralised whole-model serving (Platformless AI,
  PlanetServe `arXiv:2504.20101`, `arXiv:2606.17059`); decentralised
  model-training market (Bittensor finetuning-subnet, `arXiv:2506.07940`);
  decentralised co-training of a *single* adapter (Dec-LoRA `Ghiasvand2025`,
  `arXiv:2511.18291`, `arXiv:2606.22878`); centralised retrieval+composition
  (LoraRetriever `ZhaoLoraRetriever2024`, `arXiv:2605.01429`, `arXiv:2602.21222`);
  registry hubs (AdapterHub `Pfeiffer2020hub`, HuggingFace); DHT capability
  discovery for *agents* (`arXiv:2601.14567`). PlanetServe + Dec-LoRA verified
  via arXiv (title/abstract); all 10 arXiv IDs return HTTP 200.
- **What was done:**
  - **§3.1**: short `\paragraph{Disconfirming (adversarial) search.}` — method,
    Garousi cite, negative result, pointer to appendix; states it supersedes the
    informal §10.3 counter-search.
  - **Appendix C**: new `\subsection*{Disconfirming (Adversarial) Search}`
    (`app:db_queries:adversarial`) — the 8 query strings, screening rule,
    result, + **Table A7** (`tab:adversarial_search`, 6 category rows ×
    Unit/P2P/Disc./Comp., + a representative-artefact note row with arXiv IDs).
  - **Appendix D.1** search-log: new 2026-09-10 row (8 queries → 0 matching).
  - **§10.3**: "a non-systematic adversarial search" → "a structured
    disconfirming search (method … Appendix~\ref{app:db_queries:adversarial};
    grey-literature methodology after Garousi et al.)"; Bittensor/Platformless
    substance kept, footnote URLs kept.
  - `Garousi2019` added to `bibliography.bib` (DOI 10.1016/j.infsof.2018.09.006,
    curl-verified); now 135 entries.
  - Compiles clean: `latexmk` exit 0, **78 pp**, no undefined citations/refs,
    11 overfull boxes (10 pre-existing + 1 × 5.4 pt in §3.1 prose).

## M14 — Add a related-surveys search + comparison table — `AGENT-OK` — **DONE**
- **Author ran** the WoS + Scopus searches on **2026-09-10** (ScienceDirect not
  run separately — same Elsevier content as Scopus) and supplied the exports
  (`wos_survey_search.csv` = 50 records; `scopus_survey_search.csv` = 19
  records, all doctype `re`) + the corrected query strings.
- **Agent screening (2026-09-10):** against the inclusion rule (secondary study,
  ≥2 of the 5 pillars; exclude single-pillar and application-domain). The
  queries are heavily polluted by `LoRa` (radio) / generic `adapter`/`modular` —
  after removing false positives, **6 competing surveys** retained:
  Pfeiffer et al. 2023 (`PfeifferModular2023`, TMLR — added separately, not in
  either index; verified via OpenReview `z9EkXfvxta` / arXiv 2302.11529),
  Woisetschläger et al. 2024 (`WoisetschlagerFLsurvey2024`, IJCAI, DOI
  10.24963/ijcai.2024/919), Yang et al. 2025 FedLoRA survey
  (`YangFedLoRAsurvey2025`, IJCAI, DOI 10.24963/ijcai.2025/1196), Dib 2026
  (`DibAgenticEdge2026`, Information Fusion, DOI 10.1016/j.inffus.2026.104577),
  Jiang et al. 2026 (`JiangEdgeLLM2026`, CCF TPCI, DOI 10.1007/s42486-025-00227-7),
  Lukáč et al. 2026 (`LukacLLMsurvey2026`, Applied Sci., DOI 10.3390/app16157849).
  **All DOIs curl-verified (302).**
- **What was done:**
  - 6 new bib entries appended to `bibliography.bib` (now 134 entries).
  - §3.1: the "No search was dedicated..." admission replaced with a pointer;
    new **"Related reviews and surveys"** paragraph (search method, 50/19 yield,
    screening, the 6+1, the finding that none covers the 5 pillars jointly or
    takes coordinator-free adapter exchange as its subject).
  - New **Table 5** (`tab:related_surveys`, placed after `tab:discovery_route`):
    rows = 6 surveys + This review; cols = PEFT · Comp. · Serve · MoE · P2P ·
    Exch. (✓ / ◦ / blank). Only "This review" fills the *Exch.* column and all 5
    pillars.
  - Appendix C: new **"Related-Reviews Search"** subsection
    (`app:db_queries:related`) with both verbatim query strings + the
    ScienceDirect note.
  - Appendix D.1 search-log table: new 2026-09-10 row (50 + 19 → 6 retained).
  - `supplementary/PRISMA_2020_checklist.md` Items 6 and 7 updated.
  - Renumbering: `tab:related_surveys` = Table 5; `tab:final_exclusions` 5→6,
    `tab:datasets` 6→7, `tab:serving_comparison` 8→9, etc. All `\ref`; build
    settles clean.
  - Compiles clean: `latexmk` exit 0, **77 pp**, no undefined citations/refs,
    11 overfull boxes (10 pre-existing + 1 new 5 pt in the §3.1 funnel prose).

## M15 — State honestly what the extraction sheet contains — `AGENT-OK` — **DONE**
`03_methodology.tex`: new **"Scope of the coded extraction"** paragraph after the
funnel — lists the coded fields, states `method_name`/`datasets`/`metrics` are
uniformly empty, and that §§4–8 synthesis was narrative full-text reading (via
`key_finding`/`notes_raw` + Table 5), not machine-derived from coded fields.
- **What was done:**

## M16 — Name the automated screening classifier in-text — `AGENT-OK` — **DONE**
§A.4 / §A.7 said the model ID is "in the audit log"; §3 GenAI disclosure named
Undermind + Claude Opus 4.5 but not this classifier.
- **What was done (2026-09-10):**
  - **§3 GenAI disclosure** rewritten: Undermind now "(accessed 2026-04-14)";
    two pipeline models named — **Claude Haiku 4.5**
    (`claude-haiku-4-5-20251001`, term-set v1.0) for the 130-record title-triage
    queue, **Claude Sonnet** (`claude-sonnet-4-6`) for abstract-review advisory
    notes; drafting/proofreading attributed to "Claude Sonnet models … via the
    Claude Code interface".
  - **§A.4** (×2 spots): classifier named as Claude Haiku 4.5
    (`claude-haiku-4-5-20251001`), term-set version 1.0, log
    `log_screening_2026-04-21.json`.
  - **§A.7**: advisory notes attributed to Claude Sonnet (`claude-sonnet-4-6`);
    **corrected a false claim** — the old text said "the model identifier, the
    automated suggestion, and the author's final decision are logged per record
    in `S7b_…csv`"; that CSV has neither a model nor a suggestion column, only
    `abstract_decision`. Now states the notes were shown in the screener and not
    exported; only the final decision is logged.
  - **`\bAI` disclosure error fixed:** the manuscript named **Claude Opus 4.5**
    for abstract-review notes + drafting. Author: "I have not used Opus in any
    iteration." Git co-author trailers are all "Claude Sonnet" / "Claude Sonnet
    5". All Opus references removed from the `.tex`. Saved to memory
    (`project_ai_disclosure.md`).
- **Sourcing note:** Haiku title-triage ID is CSV/log-verified
  (`log_screening_2026-04-21.json` `llm_screening.model`, and `app/config.py`
  `LLM_SCREEN_MODEL`). Sonnet abstract ID (`claude-sonnet-4-6`) rests on the
  `app/abstract_review.py` code default + RESEARCH_DIARY "Claude Sonnet" — **no
  per-run log pins the exact build**; author to confirm before submission.
- **Reviewer's "Opus versioned / Undermind not" inconsistency (REMEDIATION
  §M16):** now moot — Opus gone; Undermind carries an access date.
- Compiles clean (exit 0, 75 pp).

## M17 — Fix Acknowledgments and disclose relationships — `AGENT-OK` — **DONE**
- **Author (2026-09-10):**
  - **Acknowledgments:** nothing to acknowledge — pure SLR, no new discovery,
    all work done by the author alone. `\acknowledgments{Not applicable.}` stays
    (accurate; MDPI permits this). The coursework professor relates to M18, not
    an acknowledgment.
  - **Šajina relationship:** none — the only tie is having studied at the same
    university (University of Rijeka). No collaboration, no shared supervision,
    no co-authored work.
- **What was done:** `\conflictsofinterest{}` in `main.tex` extended with a
  transparency sentence: the author and R.\ Šajina (whose thesis is the closest
  published predecessor) are both affiliated with the University of Rijeka but
  have no collaboration / shared supervision / co-authored work, and the thesis
  is cited solely on its scholarly merits. Pre-empts the referee question
  without inventing a conflict. Compiles clean.

## M18 — Declare the coursework self-overlap (iThenticate) — `AGENT-OK` — **DONE**
- **Author (2026-09-10):** the coursework version was **not deposited** — only
  submitted to the professor as a course-assessment obligation. No institutional
  repository, no publication.
- **Consequence:** low iThenticate risk (nothing for it to match against). No
  formal reference to cite (unpublished).
- **What was done:** the existing §3 disclosure sentence was tightened —
  "developed as coursework for a doctoral Research Methodology course at the
  University of Rijeka" now continues: "That version was submitted only for
  course assessment and was not deposited in an institutional repository or
  otherwise published; the present manuscript has been substantially revised
  and expanded from it." Compiles clean.
- **Optional for author:** a one-line mention in the cover letter ("an early
  protocol draft was prepared for a doctoral methods course; not deposited or
  published") pre-empts any question, but is not required.

## M19 — Show the abstract-2nd-pass route in the flow diagram — `AGENT-OK` — **DONE**
Folded into B5: the INCLUDED box splits into "70 via full-text-queue assessment
(`review_source = fulltext`)" + "53 via second abstract-review pass
(`review_source = abstract-2nd-pass`)"; caption states 70 + 53 = 123.
- **What was done:**

## M20 — Reconsider protocol registration — `AGENT-OK` — **DONE (Option B, pending author read)**
The old §3 text ("systematic reviews of CS/AI systems literature are not
commonly eligible for clinical registries such as PROSPERO, and no suitable
AI-specific registry was available") was factually too narrow.
- **What was done (2026-09-10):** §3 opening paragraph rewritten (same edit as
  M11's first spot). New text: PROSPERO restricts to health-related outcomes,
  which this review lacks; **OSF Registries and protocols.io do accept CS /
  engineering review protocols but were not used** — the protocol evolved
  iteratively rather than being fixed in advance, and every search string,
  screening rule and per-record decision is documented in Appendices A–D + the
  public pipeline repo instead; retrospective registration was considered and
  judged to add little beyond that. Accurate about what was available, per the
  M20 acceptance criterion. Compiles clean.
- **If the author prefers Option A** (actually register retrospectively on OSF):
  create the OSF entry, then I swap the "were not used … judged to add little"
  clause for "were registered retrospectively on OSF (DOI/date), disclosed here
  as a retrospective registration."

## M21 — Add per-pillar synthesis to §§4–8 — `GATE:AUTHOR` — **DONE (table added; synthesis per author)**
- **Serving-systems comparison table — DONE (2026-09-10):** new
  **Table `tab:serving_comparison`** in §6 (after §6.3), rows = **Punica /
  S-LoRA / CaraServe / EdgeLoRA** (dLoRA is *not* in the corpus, so it cannot be
  a row — substituted EdgeLoRA for the edge/constrained contrast). Columns:
  adapter residence · multi-adapter batching · tier beyond GPU HBM · headline
  result vs.\ own baseline. Every cell backed by §6 prose or the primary PDF;
  the three throughput/latency figures (12×, 4×, 1.7×) were re-checked against
  the Punica / S-LoRA / CaraServe PDFs and are correct (unlike the N25 rows).
  Caption states all four assume a single operator / centralised scheduler /
  co-located compute and none addresses peer discovery, bandwidth variance, or
  churn — the P2P hook.
- **Per-pillar synthesis paragraphs:** **author's own** — the author states
  these are already written (each of §§4–8 carries per-subsection "what this
  leaves open for P2P" observations, and §6 has an explicit cross-system
  synthesis paragraph, "Across these systems, a consistent architectural
  pattern emerges…"). A draft pass adding `%` prompt comments to the section
  ends was reverted at the author's request. If a referee flags a *specific*
  pillar as lacking a demarcated synthesis, that is a targeted fix at that time.
- Compiles clean (exit 0, 75 pp; one new 2.5 pt overfull in a table cell —
  negligible, well inside existing tolerance).
- **What was done:** table added + verified; synthesis left to the author per
  their statement that it is done.

---

# PHASE 3 — Minor issues

## N22 — §5.6 "same initialisation point" claim — `AGENT-OK` — **DONE**
`05_adapter_composition.tex` — independently trained LoRAs do not share an
initialisation point in the model-soup sense (A random per run, B zero-init).
- **What was done (2026-09-10):** Model Soups paragraph in §5.6 rewritten.
  Removed "the weight-averaging principle extends **by construction** to …
  LoRA adapter matrices, provided the adapters share the same initialisation
  point" and "this result implies that adapter weight averaging is a **viable**
  zero-shot composition strategy". New text: Model Soups was on full vision
  models from a *shared* init on the *same* task (common low-loss region);
  independently trained LoRA adapters fail that precondition ($A$ random per
  run, $B$ zero-init → no shared init point, no guaranteed common basin);
  mean-averaging their matrices is therefore a *"plausible but empirically
  unvalidated"* zero-shot strategy and "among the open questions this review
  identifies (§9)". Consistent with the B8 §10.1 Finding 2 demotion of Model
  Soups. Compiles clean.

## N23 — §10.1 Finding 1 "2–10 MB for r = 4–8 at GPT-2 scale" — `AGENT-OK` — **DONE (derivation stated)**
No source.
- **What was done (2026-09-10):** chose the "state the derivation" option.
  §10.1 Finding 1: "2--10~MB" → "of order 2--10~MB" + a new footnote giving the
  back-of-envelope: LoRA on query+value projections adds $2rd$ params per
  projection; for GPT-2 medium–XL ($d\approx1024$–$1600$, 24–48 layers) at
  $r=4$–$8$ that is $\approx0.4$–$2.5$\,M params $\approx$ 1–10\,MB in single
  precision; explicitly labelled "order-of-magnitude estimate … not a measured
  file size". No external citation added (keeps it self-contained; consistent
  with the citation-integrity rule). Compiles clean (footnote renders in §11
  body text, same mechanism as the UniPELT footnote).

## N24 — §10.1 Finding 3: cite specific papers not "G6" — `AGENT-OK` — **DONE**
`11_conclusion.tex` Finding 3: "the G6 group in Table…" →
`\cite{ZhangFedPETuning2023}` (the paper §8.4 already uses for the 90–99% range)
+ pointer to §`sec:p2p_federated:fed_peft`.
- **What was done:**

## N25 — Table 5: re-verify score rows — `AGENT-OK` — **DONE (4 rows fixed; broader re-check flagged)**
Verified against the primary-paper PDFs in
`writing_materials/pdfs/` (2026-09-10).
- **The two reviewer-named rows were both wrong:**
  - **LoRA "87.8 (GLUE avg.)"** → **87.2 (GLUE avg., RoBERTa-base)**. LoRA
    Table 2: RoBERTa-base LoRA = 87.2, RoBERTa-large = 89.0, DeBERTa-XXL = 91.3.
    **87.8 is the `RoBlarge (AdptH)† 6.0M` Houlsby-adapter baseline row**, not a
    LoRA result.
  - **Li & Liang "34.9 (XSUM ROUGE-L)"** → **36.05 (XSUM, BART-large, 2\%
    params)**. Prefix-Tuning Table 3: Prefix(2\%) R-L = 36.05, Prefix(0.1\%) =
    35.05, FT-full = 37.25. No 34.9 anywhere.
- **Spot-check found two more wrong rows, now also fixed:**
  - **Houlsby "91.1 (SciTail)"** → **80.0 (GLUE overall, BERT-large)**. Houlsby
    et al.\ 2019 **has no SciTail experiment** (their extra-tasks table is 20
    newsgroups / Crowdflower / SMS spam / …); GLUE overall is 80.0 (adapters)
    vs 80.4 (full FT). Dataset cell changed "GLUE, SciTail" → "GLUE, 17 add'l
    classification tasks".
  - **AdapterFusion "96.6 (SciTail)"** → **94.8 (SciTail, Fusion w/ MT-A)**.
    AdapterFusion Table 2 SciTail row tops out at 94.79; no 96.6. Dataset cell
    changed to "16-task suite (incl.\ MNLI, SciTail, MRPC, CB)".
- **Checked OK:** LoraHub "34.7 avg per task (BBH)" — matches LoraHub Table
  (LoraHub\_avg = 34.7). QLoRA "99.3\% of ChatGPT" — genuine Guanaco/Vicuna
  claim.
- **⚠ Recommendation:** 4 of 5 checkable numeric rows in Pillars 1–2 were
  misattributed. The Pillar 3–5 rows are mostly qualitative directional claims
  ("up to 4× throughput", "10–100× comm. saving") not individually verified
  here. A **full author re-verification of every numeric "Score" cell in
  Table 5 against its cited primary is strongly advised** before submission.
- Compiles clean (exit 0, 75 pp).

## N26 — Replace Table 8's Evidence column — `AGENT-OK` — **DONE**
`09_synthesis_gap.tex` Table 8 (`tab:gap_map`): "Evidence" (G-group labels) →
"Closest prior work checked", each row now cites the specific works named in the
matching §9.3 gap paragraph (e.g. Kademlia/LoraRetriever/Ostapenko for
discovery; OrmandyGossip/HegeduisGossip for gossip; Pfeiffer2021fusion/
TaskArithmetic/TIES for fusion). Caption updated; header column widths adjusted.
- **What was done:**

## N27 — Verify corpus coverage of adjacent recent work — `AGENT-OK` — **DONE**
- **Verification (2026-09-10, against `13_final_reading_list_2026-05-12.csv`,
  `pipeline_unified.csv`, `bibliography.bib`):**
  - **Heterogeneous-rank federated LoRA — covered.** In the final 123:
    HetLoRA (`ChoHeteroLoRA2024`), FFA-LoRA (`SunImprovingLoRA2024`), FLoRA
    (`WangFLoRA2024`), "Serving Heterogeneous LoRA Adapters…", "Federated
    Adaptive Fine-Tuning… Heterogeneous Quantization and LoRA", DP-FedLoRA,
    `KooBai2025` (bib). **FlexLoRA** specifically: screened (in
    `pipeline_unified.csv`) but **not retained** in the final 123 — topic
    nonetheless well represented, so no gap.
  - **Adapter retrieval beyond LoraRetriever — covered.** In the final 123:
    LoraRetriever (`ZhaoLoraRetriever2024`), PHATGOOSE (`Muqeeth2024`),
    Ostapenko "Library of LoRAs"/Arrow (`Ostapenko2024`). RAMoLE
    ("Retrieval-Augmented Mixture of LoRA Experts…") screened but not retained.
  - **Decentralised training beyond Petals (DiLoCo, SWARM) — not in corpus,
    by scope.** Neither DiLoCo nor SWARM Parallelism is in the corpus; these
    concern decentralised training of a *full* model, outside this review's
    frozen-shared-backbone adapter-exchange scope. Petals (`Borzunov2023`,
    P2P *inference*) is the in-scope exemplar and is included.
- **What was done:** added a scope-boundary sentence to §10.3 *External
  validity* (`11_conclusion.tex`): states DiLoCo / SWARM Parallelism were not
  sought (full-model training is out of scope; Petals is the in-scope P2P
  exemplar), and that heterogeneous-rank federated LoRA (HetLoRA, FLoRA,
  FFA-LoRA) and adapter retrieval beyond LoraRetriever (PHATGOOSE, Ostapenko's
  LoRA library) are all represented in the final corpus. Compiles clean.

## N28 — Replace arXiv DOIs with publisher DOIs — `AGENT-OK` — **DONE (review list, no source change)**
Author: leave the .bib as-is, build a list. `N28_doi_review_list.md` written:
52 arXiv-DOI refs (most venues — NeurIPS, PMLR/ICML, MLSys — have no publisher
DOI at all), 7 refs with no DOI (incl. ref [7] Toppings; candidate DOI found is
dead), 2 pre-existing `10.5555/` DOIs verified as 404.
- **What was done:**

## N29 — Report 19 UNCERTAIN as excluded — folded into B5 — **DONE**
Figure 5: 972 = 810 excluded (791 + 19 UNCERTAIN unresolved) + 162.
- **What was done:**

## N30 — Add "Reports sought / not retrieved" boxes — folded into B5 — **DONE**
Figure 5: 387 reports sought for retrieval; 24 not retrieved (full text
unavailable); 173 DEFER not carried forward to eligibility assessment.
- **What was done:**

## N31 — Retro-code the 165 abstract SKIPs OR state 16b-at-eligibility — `GATE:AUTHOR` — **DONE (author accepted the fallback)**
- **Author decision (2026-09-10): accept the fallback.** No retro-coding of the
  165 SKIP records. The fallback is already stated in the manuscript in three
  places and needs no further edit:
  - Figure 5 exclusion box: "165 records excluded at abstract review (SKIP) —
    individual exclusion reasons not coded at this stage (disposition reported
    per PRISMA 2020 Item 16b)".
  - §3.1 body: "The abstract-review pipeline records only a coarse KEEP/SKIP
    disposition and does not retain an individually coded exclusion reason for
    SKIP records; this gap is disclosed as a named limitation in §10.3".
  - §10.3 (Threats): the "granularity of the audit trail at that specific
    stage, consistent with PRISMA 2020 Item 16b" sentence; PRISMA 16b is
    satisfied at the eligibility stage via Table 4 (the 101 read-in-full
    exclusions, all per-record categorised).
- **What was done:** status flipped PARTIAL → DONE; no source change required.

## N32 — Reconcile "38 excluded in enrichment" — folded into B5 — **DONE**
Figure 5: 38 removed at enrichment = 6 off-topic + 32 low-citation preprints
moved to rescue file, "later confirmed excluded at abstract review".
- **What was done:**

## N33 — Remove the nonstandard MERGE band — folded into B5 — **DONE**
Figure 5: no "MERGE WITH PRE-VALIDATED CORPUS" band; the 162 + 352 − 12 = 502
merge is a normal box inside SCREENING.
- **What was done:**

## N34 — Table 5 / §3.4.1 category mismatch — `AGENT-OK` — **DONE**
`03_methodology.tex` §3.4.1 prose now matches the Table 5 caption's four
categories: 26 (79%) release; 1 (3%) `Partial` (FedAvg); 2 (6%) `No` (Expert
Choice, MT-EF); 4 (12%) `Unknown` (Ostapenko, DP-FedLoRA, SLoRA, Gossip
Learning) — no longer collapses `No` + `Unknown`.
- **What was done:**

## N35 — Standardise tier labels — `AGENT-OK` — **DONE (captions)**
`12_appendix.tex` Table A2 wording ("PEFT + distributed/P2P + LLM (all three)" /
"two of the three themes" / "foundational or tangential (one theme)") adopted in
the Figure A1 caption.
- **Residual:** axis/legend text baked into `fig_slr6_tier_breakdown.pdf` etc.
  comes from plotting scripts in `mdpi_slr_engine` — update there.
- **What was done:**

## N36 — Study-type split over 120 distinct papers — `AGENT-OK` — **DONE**
`03_methodology.tex`: split reported over the 120 distinct papers (111 primary /
9 survey), with the 123-row basis (114 / 9) noted alongside.
- **What was done:**

## N37 — Fix the DEFER contradiction in §3.1 — `AGENT-OK` — **DONE**
`03_methodology.tex:88`: "173 were classified SKIP but re-flagged DEFER" →
"173 were classified DEFER and carried into the full-text queue". Matches Table
A5's canonical three-way split.
- **What was done:**

## N38 — Clarify Table 3's attribution rule / report by discovery route — `AGENT-OK` — **DONE**
Table 3's G-group labels record the corpus a paper landed in, not how it was
discovered (G0's n-final=18 folds in 14 snowball descendants) — yet §3.2 used
"G1–G6 = 105" as evidence of "85.4% via targeted retrieval rather than blind
snowball screening", conflating label and route.
- **What was done (2026-09-10):**
  - **B6 groundwork:** verified the 105 against `pipeline_unified.csv`
    `direction` — 105 are `direction = PREVALIDATED` / `source_engine =
    undermind` exactly; corrected the "not a strict subset of 343" wording in
    §3.1 / App. A.1 / `tab:undermind_funnel`; fixed the Table 3 footnote
    ("Houlsby absent" → attributed to G2).
  - **This pass — the by-route table:** new **Table 4** (`tab:discovery_route`,
    placed right after `tab:groups`) breaks the 123 down by the unified
    pipeline's `direction` field, independent of group label:
    **105 targeted retrieval** (85.4%) · **4 direct G0 seed** (3.3%) ·
    **14 citation snowballing** on G0 = 10 forward + 4 backward (11.4%) ·
    **0** supplementary Scopus/WoS forward-snowball pass · **0** manual
    cross-validation top-up. Verified against `pipeline_unified.csv`
    (`in_final_list_123` × `direction`; `G_SNOW_F` in final = 0).
  - §3.2 paragraph reworded to say the group label records placement not
    discovery, and to point at Table 4; the "85.4% via targeted retrieval, not
    blind snowballing" claim now rests on the route field, with only 14/123
    from snowballing.
  - Renumbering: `tab:discovery_route` = Table 4; `tab:final_exclusions` 4→5,
    `tab:datasets` 5→6, etc. All refs are `\ref` (no hardcoded numbers); build
    settles clean, first-mention order preserved.
- Compiles clean (latexmk exit 0, 75 pp, no undefined refs).

## N39 — Table A4 rounding note — `AGENT-OK` — **DONE**
`12_appendix.tex`: caption now notes the % column sums to 100.1 due to rounding.
- **What was done:**

## N40 — Expand "MT-EF" at first use — `AGENT-OK` — **DONE**
`03_methodology.tex` Table 5: "MT-EF" → "MT-EF (Multi-Task Encoder Fusion)" at
first use (p. 14), before the §8.4 heading.
- **What was done:**

## N41 — Figures 3 and 14 near-duplicates — `GATE:AUTHOR` — **DEFERRED (author: all figures later)**
Both illustrate Kademlia XOR-metric lookup. Cut one, or make Figure 14 show
adapter-capability keys in the DHT (would also strengthen §8.6).
- **Author (2026-09-10):** figures will be tackled later as a batch. Parked.
  (Note: Fig 3 and Fig 14 are literally the same PDF `fig_p2p_dht_lookup.pdf`;
  connects to N42.)
- **What was done:** nothing yet — deferred.

## N42 — "(own figure)" attribution inconsistent — `GATE:AUTHOR` — **DEFERRED (audit done; author: all figures later)**
- **Author (2026-09-10):** figures will be tackled later as a batch. Audit
  table (below) is ready; no source edits until the author answers the
  attribution questions.
- **Full audit (2026-09-10) — three attribution styles in use:**

  | Fig | Label | PDF | Caption attribution |
  |---|---|---|---|
  | 1 | `fig:concept_peft_paradigm` §2 | `fig_concept_peft_paradigm.pdf` | **none** |
  | 2 | `fig:peft_adapter_types` §2 | `fig_peft_adapter_types.pdf` | "(own figure)" |
  | 3 | `fig:p2p_dht_lookup` §2 | `fig_p2p_dht_lookup.pdf` | **none** |
  | 4 | `fig:p2p_gossip` §2 | `fig_p2p_gossip.pdf` | **none** |
  | 5 | `fig:prisma` §3 | `fig_slr1_prisma_flow.pdf` | **none** |
  | 6 | `fig:quality_bands` §3 | `fig_slr_quality_bands.pdf` | **none** |
  | 7 | `fig:houlsby_adapter` §4 | `fig_houlsby_adapter_figure.pdf` | "(own figure)" |
  | 8 | `fig:peft_types` §4 | `fig_peft_taxonomy.pdf` | "(own figure)" |
  | 9 | `fig:adapterfusion` §5 | `fig_adapterfusion.pdf` | "(own figure)" |
  | 10 | `fig:peft_paradigm` §6 | **`fig_concept_peft_paradigm.pdf`** (same as Fig 1) | **"Adapted from \cite{Sheng2024}"** |
  | 11 | `fig:switch_transformer` §7 | `fig_switch_transformer.pdf` | "(own figure)" |
  | 12 | `fig:gossip` §8 | **`fig_p2p_gossip.pdf`** (same as Fig 4) | "(own figure)" |
  | 13 | `fig:petals` §8 | `fig_petals.pdf` | "(own figure)" |
  | 14 | `fig:dht_lookup` §8 | **`fig_p2p_dht_lookup.pdf`** (same as Fig 3) | "(own figure)" |
  | 15 | `fig:fig_gap_quadrant` §9 | `fig_gap_quadrant.pdf` | **none** |
  | A1 | `fig:tiers` §A | `fig_slr6_tier_breakdown.pdf` | **none** |
  | A2 | `fig:bibliometric` §A | `fig_slr3_year_distribution.pdf` | **none** |
  | A3 | `fig:venues` §A | `fig_slr5_venues.pdf` | **none** |

- **Two live contradictions to resolve first:**
  1. **Fig 1 vs Fig 10** — identical PDF (`fig_concept_peft_paradigm.pdf`), but
     Fig 10 says "Adapted from \cite{Sheng2024}" and Fig 1 says nothing. Must be
     the same attribution in both places.
  2. **Fig 3/14** (same PDF) and **Fig 4/12** (same PDF) — the §8 instance says
     "(own figure)", the §2 instance says nothing. (N41 also wants Fig 3 or 14
     cut.)
- **Needs from author (cannot be inferred):**
  - Is `fig_concept_peft_paradigm.pdf` your own drawing (→ "(own figure); concept
    after \cite{Sheng2024}") or an adaptation of S-LoRA's figure (→ "Adapted
    from \cite{Sheng2024}", + permission)?
  - Figs 7, 9, 11, 13 (Houlsby adapter, AdapterFusion, Switch Transformer,
    Petals) currently say "(own figure)". Confirm each is an original redraw and
    does **not** trace/adapt the source paper's own figure. Any that do need
    "Adapted from \cite{…}" + a permission line.
  - The 8 unmarked figures (1, 3, 4, 5, 6, 15, A1–A3): confirm all author-made
    (the SLR data plots and PRISMA/gap diagrams evidently are) → I add
    "(own figure)".
- **What was done:** audit table above; no source edits yet (stamping
  "(own figure)" on an adapted figure is a copyright risk — needs the answers).

## N43 — Swap Figure A2/A3 numbering; Table A3 before A4 — `AGENT-OK` — **DONE**
`12_appendix.tex`: year-distribution figure (`fig:bibliometric`) moved ahead of
the venues figure (`fig:venues`) to match citation order. Tables A3/A4 were
already in correct order.
- **What was done:**

## N44 — Typos + missing-space scan — `AGENT-OK` — **DONE**
Fixed `contribution.Forward` (`03_methodology.tex:70`) and `),with`
(`12_appendix.tex:245`). Full-source scan for `[a-z]\.[A-Z]` and `,[a-z]`
returned only math-mode false positives.
- **What was done:**

## N45 — page count is long for *AI* — `GATE:AUTHOR` — **DEFERRED (author: waiting for mentor)**
Consider moving parts of §§4–8 to supplementary.
- **Author (2026-09-10):** leave as is; will decide with the mentor. Parked.
- **Note:** now **75 pp** (was 71 at first triage; +B4/B5/B6 prose, tables and
  the two-column PRISMA figure). Trimming pressure has increased, not decreased.
- **What was done:**

## N46 — §1 "closes" → "identifies" — `AGENT-OK` — **DONE**
`01_introduction.tex:100`: "The specific synthesis gap this review closes" →
"…identifies".
- **What was done:**

## N47 — §10.2 restore corpus bound — `AGENT-OK` — **DONE**
`11_conclusion.tex`: "From the literature that has been reviewed, no prior
finding has examined this intersection" → "Within the reviewed corpus, no prior
finding…".
- **What was done:**

## N48 — Archive both repos to Zenodo, cite DOIs — `GATE:AUTHOR` — **DEFERRED (author: keep GitHub for now)**
GitHub URLs are not persistent identifiers; MDPI prefers PIDs. Archive
`mdpi_paper_slr` and `mdpi_slr_engine` to Zenodo, cite the DOIs in the DAS.
- **Author (2026-09-10):** leave GitHub for now; revisit at submission. Parked.
  (MDPI reviewers may still request a PID; low effort to add later once the
  Zenodo deposit exists.)
- **What was done:** nothing — deferred.

## N49 — Supply the ten Web of Science search strings — `AGENT-OK` — **DONE (already in Appendix C)**
- **Finding (2026-09-10):** the WoS strings were **already present** — Appendix C
  has a "Web of Science Advanced Search Queries" subsection with all ten
  (`app:db_queries:wos`, Q1–Q10), and they match `supplementary/queries.sql` (repo root)
  verbatim. A prior session added them; only this tracker was stale.
- **What was done:** verified the 10 appendix WoS queries against
  `/Users/vanja/git/papers_code/queries.sql` (exact match). Tightened the
  Appendix C intro sentence: "In WoS, Topic-field (TS=) queries were used with
  equivalent year filters" → notes all 20 strings are reproduced below and that
  Scopus `PUBYEAR > y` vs WoS `PY >= y` differ by one boundary year. Compiles
  clean.

---

# PHASE 4 — Pre-submission verification (batch A run 2026-09-10)

- [x] **grep source for `TODO|FIXME|XXX|TREBA|OVAJ|POGLEDATI|ODLUČITI|MENTOR|REMOVE BEFORE|placeholder`** — clean. Removed 4 `% [PROPOSED C1 - Vanja review before removing]` marker pairs in §6/§7/§8 (kept the prose they wrapped: Mixtral, GShard/GLaM, Chord/BitTorrent, FlexGen/AlpaServe sentences).
- [ ] `verify_prisma_counts.py` + `verify_quality_appraisal.py` unchanged — **author to run in `mdpi_slr_engine`** (no pipeline number changed this session; low risk).
- [x] **every float cited, ascending first-mention order** — MAIN: figures 1–15 ✓, tables 1–11 ✓ (fixed: `tab:serving_comparison` was uncited → added §6 `\ref`; `tab:related_surveys`↔`tab:discovery_route` swapped + an early §3.1 `\ref` to `tab:discovery_route` so mentions ascend). APPENDIX tables are numbered by position within the appendix (A1–A8) and first-mentioned from the main text in a different order — standard for appendix floats; **accepted, not reshuffled**.
- [x] **every reference cited; every citation resolves; contiguous** — 135 bib entries, **135 cited, 0 uncited, 0 cited-but-missing**; `main.bbl` has 135 contiguous bibitems.
- [ ] every DOI resolves (HTTP 200 via doi.org) — **known/accepted state** per `N28_doi_review_list.md` (52 arXiv-DOI refs, 7 no-DOI, 2 dead `10.5555/`); the 7 M13/M14 additions are all curl-verified.
- [ ] no unsourced quantitative claim (§10.1, §10.3, §3.4, Table 5) — **needs a human read** (partly swept: N23 sourced "2–10 MB", N25 fixed 4 Table 5 rows, B7 deleted "5–13%").
- [x] **ORCID in title block** — **present and correct**: the green iD icon renders next to "Vanja Luk", hyperlinking to `https://orcid.org/0009-0009-8142-6890` (verified in the PDF's link targets). An external reviewer using text extraction won't "see" it (icon + annotation, not text) — that is standard MDPI rendering. *Optional:* add "ORCID: 0009-…" as plain text to the corr.-author line for belt-and-suspenders.
- [x] **abstract ≤ 200 words** — 197 ✓
- [x] **keywords 3–10** — 9 ✓
- [ ] PRISMA 2020 27-item checklist attached as S1 — **author packaging** (`supplementary/PRISMA_2020_checklist.md` exists + updated; referenced in Methods).
- [ ] Supplementary S2 (`quality_appraisal_scored.csv`) attached — **author packaging**.
- [x] **back matter complete** — all 9 commands present with real content: `\authorcontributions` (CRediT), `\funding` (none), `\institutionalreview`/`\informedconsent` (N/A), `\dataavailability` (populated), `\acknowledgments` (N/A per author), `\conflictsofinterest` (M17 transparency note), `\abbreviations` (table), `\reftitle`.
- [ ] cover letter declares coursework overlap (M18), verbatim search strings, PRISMA boilerplate — **author writes**.
- [ ] iThenticate pre-check run — **submission system**.
- [x] every claim quantifies only over the population scored (B4 ✓) — new text (§3.1 disconfirming "No located artefact…", Table 5 "None of the seven…") is correctly scoped.
- [x] **method named in abstract = method executed** — abstract says "a single-wave Wohlin et al.\ snowballing pass"; execution was one forward/backward wave (M11). Consistent.

**Batch A summary (7 mechanical checks + back-matter):** all pass or fixed. Still open: `verify_*.py` re-run (author, in `mdpi_slr_engine`), DOI resolution (known/accepted per N28 list), **unsourced-number read of §10.1/§10.3/§3.4** (needs human), S1/S2 attachment + cover letter + iThenticate (author packaging).

---

# Auxiliary files produced this session

| File | Purpose |
|---|---|
| `N28_doi_review_list.md` | Manual DOI-check list for the 52 arXiv-DOI + 7 no-DOI + 2 dead-DOI references |
| `B6_undermind_funnel_TODO.md` | Recovery steps + fallback wording for the G1–G6 identification funnel (now marked RESOLVED — records the B6 outcome) |
| `figures/prisma.html` | Rewritten source for the two-column PRISMA figure; B6 pass added the funnel to the pre-validated box and fixed the "9 → 7 of 9 G0 seeds" snowball label |
| `supplementary/PRISMA_NUMBERS_VALIDATION.md` | Master number table — §B rebuilt as the identification funnel (U.export/pre-val/final), row 1b + changelog updated in the B6 pass |
| `M13_M14_search_materials.md` | Runnable search package for M13 (competing systems, grey-lit queries) + M14 (competing surveys, WoS/ScienceDirect/Scopus queries) — strings, screening rules, candidate lists, tables to fill; author executes |

## B6 follow-on (2026-09-10) — files modified

- `sections/03_methodology.tex` — §3.1 funnel para, Table 3 U.export column + caption + footnote[1], §3.2 "105 of 123 (85.4%)", §3 PRISMA fig caption, "7 of the 9 G0 seeds"
- `sections/12_appendix.tex` — new `tab:undermind_funnel` + A.1 prose, 3 new rows + fn(a) in `tab:search_log` (D.1)
- `sections/11_conclusion.tex` — §10.3 Undermind identification-granularity sentence
- `figures/fig_slr1_prisma_flow.pdf` — regenerated (gitignored build artefact)
- `supplementary/PRISMA_2020_checklist.md` — Item 6
- Compiles clean: `latexmk` exit 0, 75 pp, no undefined refs, no new overfull boxes
