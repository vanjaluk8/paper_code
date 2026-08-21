# Responses to Reviewers — DRAFT (scaffold — requires verbatim comments)

> **STATUS: DRAFT SCAFFOLD.** This file documents every change made during the
> revision and the reviewer concern each change addresses. It is **not yet a
> complete point-by-point reply**: it must be finalised by pasting the
> **verbatim reviewer comments / decision letter** (not currently available in
> this repository) into each block, and by filling the marked **D2/D3/D4**
> placeholders. No reviewer quote is fabricated herein — every "concern" below
> is reconstructed from the revision plan's stated rationale.

**Manuscript:** *Decentralised Adapter-Based LLM Serving: A Systematic Literature Review of Peer-to-Peer Transferable Knowledge Units*
**Journal:** MDPI *AI* · **Submission:** [TO FILL: manuscript ID]
**Revision:** [TO FILL: major / minor second round]

---

## Cover note

Dear Editor,

We thank the reviewers for their careful reading and constructive comments,
which have materially improved the clarity, methodological rigour, and
reproducibility of the manuscript. [TO FILL: paste the decision letter header,
the reviewers' overall assessments, and any editor-level instructions.]

In this revision we have:

1. **Audited and reconciled every corpus/funnel figure** against the
   underlying pipeline data files (single source of truth: `PRISMA_NUMBERS_VALIDATION.md`), so the
   headline **123 included records / 121 distinct papers** and the full
   PRISMA 2020 chain (1,150 → 972 → 502 → 464 → 552 → 387 → 224 → 123) are
   consistent across the Abstract, §3.1, Table 1, Table A3, Figure 5, the
   PRISMA checklist, and the PRISMA summary.
2. **Added a grounded, auditable six-dimension quality-appraisal instrument
   (§3.3)** with no imputed or fabricated values; dimensions that could not be
   scored from the available data are explicitly scoped out and disclosed.
3. **Grounded every analytical claim in the reviewed corpus**, replacing any
   over-reaching wording with corpus-bounded phrasing.
4. **Improved transparency of the search strategy** (per-group provenance,
   G0 seed justification, full data-extraction codebook, AI-tool disclosure),
   and **corrected all typographical, terminology, reference, and
   reproducibility issues raised**.

A point-by-point response to each comment follows. Quotations of the
reviewers' comments are reproduced verbatim from the decision letter;

---

## Reviewer 1

### R1-1 — [TO FILL: paste reviewer concern / comment]

**Concern (reconstructed):** the manuscript should justify the reproducibility
and provenance of every reported number (corpus counts, funnel stages).

**Response:** We reconciled all reported figures against the authoritative
pipeline records (`PRISMA_NUMBERS_VALIDATION.md`, itself a reconciliation of
the raw `snowball_output/` CSVs). The headline inclusion figure is now
consistently reported as **123 included records / 121 distinct papers** (two
foundational works, LoRA and the original adapter-based transfer-learning
method, each appear under both an arXiv and a Scopus retrieval key). The full
PRISMA 2020 chain is stated once (§3.1 and Figure 5) and reused verbatim in the
Abstract, PRISMA checklist, and summary, so no independent retyping can drift.
> **Plan ref:** 1.5 (123 vs 121), 1.1/1.4 (PRISMA reconciliation), Phase 4
> (7-place consistency check).

### R1-2 — [TO FILL]

**Response:** [TO FILL — see plan items 1.1/1.4 if this concerns the PRISMA
flow figure; 1.7/1.8 if protocol registration.]

---

## Reviewer 2

### R2-1 — Quality/risk-of-bias appraisal ([TO FILL: verbatim comment])

**Concern (reconstructed):** each included study should receive a quality /
risk-of-bias assessment rather than a purely narrative synthesis.

**Response:** We added a dedicated **§3.3 Quality Assessment** with a grounded
six-dimension rubric (Q1 publication/venue, Q2 record resolvability, Q3 methods
specificity, Q4 evaluation-claim specificity, Q5 contribution clarity, Q6
synthesis relevance), each dimension scored 0–2 from real pipeline columns (no
imputation), giving a 0–12 score per record. Over all **123** records: mean
**7.17** (SD 2.09), bands **18 / 57 / 46 / 2**, shown in **Figure 6** and the
scored data available as accompanying material. Four classic dimensions
(code/artifact availability, result reproducibility, baseline adequacy, threat
reporting) could **not** be auto-extracted from the pipeline data; rather than
fabricate scores we **scoped them out and disclosed** this explicitly in §3.3.
> **Plan ref:** 1.3, 1.3-D5. PRISMA checklist items 11 & 18 now point here.

### R2-2 — Over-claiming / novelty framing ([TO FILL: verbatim comment])

**Concern (reconstructed):** some claims read as over-broad or novel-in-absolute
terms; claims should be bounded to the reviewed corpus.

**Response:** We de-escalated over-reaching phrasing throughout: the abstract's
"unprecedented opportunity" → "substantial opportunity"; the synthesis gap's
"primary analytical contribution" → corpus-bounded "its principal analytical
deliverable within the reviewed corpus" and "No prior work frames…" → "Within
the reviewed corpus, no work yet frames…"; the conclusion's "novel research
direction" → "distinct research direction grounded in the reviewed corpus" and
"no existing system" → "none of the 123 reviewed systems (to the best of the
author's knowledge)". We also **added a survey-positioning paragraph (§1)** that
explicitly contrasts the review against prior PEFT/LoRA and decentralised
surveys (Han et al., Wang et al., Mao et al., Ye et al., Wink et al., Šajina et
al.) and states the exact synthesis gap: adapter-level knowledge represented,
discovered, and exchanged in a decentralised, multi-task P2P setting.
> **Plan ref:** 2.6, 2.5, 2.2.

### R2-3 — Search-strategy / provenance ([TO FILL: verbatim comment])

**Concern (reconstructed):** the split between curated groups and citation
snowballing, and the seed-selection criterion, should be explicit and
justified.

**Response:** §3.1 now reports the provenance split explicitly: of the 123
included records, **105 (85.4%)** come from the curated pre-validated groups
G1–G6 and **18 (14.6%)** from forward/backward snowballing around the G0 seeds
(4 direct seeds, 10 forward, 4 backward). Group final counts were corrected to
the authoritative seed-group tagging (G0:18 … G6:30, Table 1). We added
**Table `g0_seeds`** justifying the 9 seeds (venue + role) and a
threat-to-validity paragraph on the ≥300-citation seed-selection bias.
> **Plan ref:** 2.3, 2.2. ⚠ **@user-verify:** confirm the manual-add → G0
> remapping reflected in Table 1 is intended.

---

## Method / reproducibility (all reviewers / editor)

- **AI-tool disclosure (§3):** expanded to MDPI Statement-on-AI style — names
  tools (Undermind, candidate retrieval; Claude, drafting/proofreading +
  advisory abstract-review notes), gives exact roles, and states that the
  author made all inclusion/exclusion/appraisal decisions, verified all numbers
  against the pipeline data, and assumes full responsibility.
> **Plan ref:** 3.3.
- **Data-extraction codebook (§A.5):** documents all 22 extraction columns
  (meaning, allowed values, coverage/224), transparently noting that
  `method_name`/`datasets`/`metrics` are schema-only (0% populated).
> **Plan ref:** 2.7.
- **Reference hygiene (3.2):** verified via the arXiv and Crossref APIs that
  the 55 arXiv-DOI references are the correct canonical resolvers — 0 of the 9
  arXiv-only works have a Crossref-registered published version to upgrade to;
  the 17 Phase-1 DataCite-verified DOIs are retained.
- **Terminology (3.6):** normalised spelling (decentralised); verbatim Scopus/
  WoS query strings and quoted Undermind prompts preserved (altering them would
  misrepresent the documented search).
- **Abstract (3.1):** restructured to Background→Methods→Results→Conclusion and
  now states the validated funnel and the QA instruments.

---

## Open items requiring author input (D2 / D3 / D4) — [TO FILL]

| # | Item | What the author must supply |
|---|---|---|
| D2 | Data-availability section (§1.6) + repository URL references (§3.5) | The two-project repo **names/URLs** and **public-vs-private** status per repo, so we can (a) finalise the data-availability statement and (b) replace bare filenames with stable URLs. |
| D3 | Inter-rater reliability (2.1) | The **2nd reviewer's independent 10% screening decisions**, to report % agreement / Cohen's κ in §3.1 (as requested by the reviewer on single-reviewer bias). |
| D4 | Circular arXiv-inclusion criterion (2.4) | **Current citation counts** for the 123 records (or permission to query the Semantic Scholar API), to replace the circular "cited by ≥1 work in corpus" proxy with a corpus-independent one. |

---

*This scaffold is updated from `REVISION_LOG.md` (rows 1–25) and the execution
plan. When pasting the decision letter, insert each verbatim comment into the
matching block above and remove the `[TO FILL]` markers; delete this footer.*
