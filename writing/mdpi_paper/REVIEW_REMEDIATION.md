# REVIEW_REMEDIATION.md

Remediation plan for **"Decentralised Adapter-Based LLM Inference: A Systematic Literature
Review"** (MDPI *AI*, Systematic Review article type), derived from a simulated MDPI desk-check
+ peer-review audit of `main2.pdf` (71 pp., 9 Sep 2026 build).

This file is the **single source of truth** for the revision. It is written to be executed by
Claude Code against the `paper_code` and `slr_engine` repositories, with the author (Vanja Luk)
acting as validator at every `GATE` marker.

---

## 0. How to use this file

### 0.1 Operating contract for the agent

```
ROLE:   You are revising a manuscript, not writing one. The synthesis, argument,
        and conclusions are the author's. You fix reporting defects.

SCOPE:  Only tasks listed in this file. If you notice something else, add it to
        §9 (Observations backlog). Do not fix it silently.

ORDER:  Work phase by phase. Do not start Phase N+1 until every task in Phase N
        is either DONE or explicitly DEFERRED by the author.

GATES:  A task marked GATE:AUTHOR cannot be completed by you. Prepare the change,
        show the diff, state exactly what input you need, and STOP.
        Do not guess. Do not use a placeholder that could survive to submission.
```

### 0.2 Absolute prohibitions

1. **Never invent a number.** Every count, percentage, date, citation, score, or
   identifier must come from a file in `slr_engine`, a file in `paper_code`, or the
   author. If you cannot source it, mark the task `BLOCKED:NEEDS-DATA` and stop.
2. **Never alter a verified count.** See §1 (Frozen values). Those reconcile. If a
   fix appears to require changing one, you have misread the task — stop and ask.
3. **Never soften a limitation into a strength.** Several tasks below make the paper
   *more* exposed (e.g. B4, M11). That is intentional and correct.
4. **Never add a citation you have not verified exists** with matching author, year,
   venue, and DOI. Fabricated references are the one defect that ends a submission
   permanently rather than temporarily.
5. **Never leave a `TODO`, `XXX`, `FIXME`, placeholder, or non-English note** in the
   compiled manuscript. See B1 for why.

### 0.3 Status legend

| Marker | Meaning |
|---|---|
| `[ ]` | Not started |
| `[~]` | In progress / diff prepared, awaiting author |
| `[x]` | Done and validated by author |
| `[-]` | Deferred by author (record reason inline) |
| `GATE:AUTHOR` | Requires author input, judgment, or new measurement. Agent prepares, author decides. |
| `AGENT-OK` | Agent may complete unaided; author reviews the diff. |

### 0.4 Definition of done, per task

A task is `[x]` only when: the change is in the LaTeX source, the PDF recompiles
without new warnings, the acceptance criteria in that task are met, and the author
has seen the diff.

---

## 1. Frozen values — DO NOT MODIFY

These reconcile exactly and were verified by independent recomputation. If any edit
would change one of these, the edit is wrong.

```
Snowball candidates identified ............ 1,150
Duplicates removed ........................    178
Unique records title-screened .............    972   (= 111 + 130 + 731, Table A1)
Title screening: INCLUDE / UNCERTAIN / EXCL   162 / 19 / 791
Per-seed new records (Table 2) sum .........   972   (157+136+128+125+131+163+132)
Merge: 162 + 352 - 12 .....................    502
Enrichment: 502 - 6 - 32 ..................    464
Abstract pool: 464 + 88 ...................    552
Abstract KEEP / DEFER / SKIP ..............   214 / 173 / 165
Forward-snowball increment ................    12 / 4 / 72   (sums to 88)
Forward snowball sources ..................   74 Scopus + 14 WoS = 88
Full-text queue: 214 + 173 ................    387
Queue exclusions: 24 + 173 ................    197
Extraction: 190 + 34 ......................    224
Eligibility exclusions: 34 + 53 + 14 ......    101
INCLUDED ..................................    123 records / 120 distinct papers
Group partition (Table 3) .................    18+17+17+14+16+11+30 = 123
Pre-validated group sizes .................    9+59+37+95+51+35+66 = 352
Tier partition (Fig. A1) ..................    48 + 42 + 33 = 123
Quality bands (Fig. 6) ....................    13 + 61 + 47 + 2 = 123
Year distribution (Table A4) ..............    sums to 123
```

**Regression guard:** after every phase, run
`python scripts/verify_prisma_counts.py` and `python scripts/verify_quality_appraisal.py`
in `slr_engine`. Any change in their output is a regression unless a task explicitly
called for it.

---

## PHASE 1 — Desk-check blockers

**Rationale:** these are the items that cause MDPI to return the manuscript before it
reaches a reviewer. All are mechanical except B2. Do these first; they are cheap and
they change the manuscript's status from "unsubmittable" to "reviewable."

---

### `[ ]` **B1 — Remove the mentor consultation note** `AGENT-OK`

- **Severity:** BLOCKING. Submission-ending.
- **Location:** §3.2 (Screening Reviewer Configuration), p. 9, manuscript margin lines
  **297–317**.
- **Current state:** the body text contains a bracketed working note beginning
  `[MENTOR CONSULTATION NEEDED — REMOVE BEFORE SUBMISSION:] OVAJ DIO TREBA POGLEDATI
  I ODLUČITI KAKO PRISTUPITI:` followed by ~20 lines of mixed Croatian/English notes
  proposing remedies (A) and (B) for the absent inter-rater statistic, and referencing
  "an external audit of this manuscript."
- **Action:**
  1. Delete the entire block, including its surrounding whitespace and any
     `\textbf{}` / environment wrapper introduced for it.
  2. Grep the whole source tree for other survivors:
     `grep -rniE "TODO|FIXME|XXX|TREBA|OVAJ|POGLEDATI|ODLUČITI|MENTOR|REMOVE BEFORE" *.tex`
  3. Report every hit. Do not delete hits outside this block without asking.
- **Do not:** delete the *surrounding* legitimate paragraphs (lines 282–296 on
  PRISMA Item 8 and single-reviewer practice, and 318–328 on the complementary
  risks). Those stay.
- **Downstream:** the note's content is superseded by **M12**. Do not lose the
  substance — M12 is where it lands.
- **Acceptance:** grep returns zero hits in compiled source; no non-ASCII Croatian
  text outside the Šajina author names and the standard diacritics in references.

---

### `[ ]` **B2 — Add corresponding-author ORCID** `GATE:AUTHOR`

- **Severity:** BLOCKING (MDPI submission requirement).
- **Location:** title block, p. 1.
- **Current state:** name, affiliation, and `vluk@uniri.hr` present. No ORCID iD.
- **Action:** insert into the MDPI author macro, e.g.
  `\author{Vanja Luk \orcidA{}}` with `\orcidauthorA{0000-0000-0000-0000}`
  per the `mdpi.cls` convention already in use.
- **GATE:** the agent cannot know the iD. **Author: supply your ORCID iD.**
  If you do not have one, register at orcid.org — takes ~3 minutes.
- **Acceptance:** ORCID renders in the title block of the compiled PDF.

---

### `[ ]` **B3 — Cite the three orphaned float items** `AGENT-OK`

- **Severity:** BLOCKING (technical pre-check: all floats must be cited, in order).
- **Findings:** three floats have captions but **no in-text callout anywhere**:

  | Float | Caption location | Where the callout belongs |
  |---|---|---|
  | **Table 1** (nine G0 seeds) | p. 10 | §3.1, at the sentence "The search was anchored on nine foundational seed papers (Group G0)…" (line ~208) |
  | **Figure 10** (PEFT serving paradigm) | p. 26 | §6.1, in the multi-tenant serving challenge discussion |
  | **Table A5** (abstract-review disposition) | p. 62 | §A.7, at the paragraph describing the KEEP/DEFER/SKIP split |

- **Action:** add a natural `Table~\ref{}` / `Figure~\ref{}` callout at each location.
  Do not manufacture a sentence — attach the reference to the existing sentence that
  already discusses that content.
- **Verify after:** first-citation order must be monotonic. Recheck by extracting
  first in-text mention order for all floats; Table 1 must precede Table 2, Figure 10
  must fall between Figure 9 and Figure 11.
- **Acceptance:** every `Table`/`Figure` label in the source has ≥1 `\ref` in body text,
  and first-mention order is ascending within main text and within appendices.

---

### `[ ]` **B4 — Reconcile Table 7's evidence base with the claim scope** `GATE:AUTHOR`

- **Severity:** BLOCKING. This is the substantive core of the review.
- **The defect:** Table 7 scores **17 systems**. But:
  - Abstract: "no reviewed system simultaneously addresses…"
  - §10.2: "the concept matrix (Table 7) shows that **none of the 123 reviewed
    records** simultaneously satisfies all seven design dimensions"

  Table 7 cannot support a claim over 123 records. The gap claim — the paper's entire
  contribution — currently overreaches its own evidence sevenfold.
- **Two remedies. The author must choose. They are not mutually exclusive and doing
  both is the strongest outcome.**

  **Option A — widen the evidence (preferred).**
  Score all **123** records, or at minimum the **48 Tier-1** records, on the seven
  dimensions. Publish the full matrix as Supplementary S3. Keep Table 7 in the main
  text as an illustrative extract, with a caption stating it is an extract and
  pointing to S3.
  - Implementation: add seven boolean/ternary columns to the final reading list;
    write `scripts/score_concept_matrix.py`; emit `concept_matrix_full.csv`.
  - Cost: this is a full-text re-read pass. Realistically the largest single item
    in this plan.

  **Option B — narrow the claim (minimum viable).**
  Rewrite the abstract and §10.2 to claim only over the 17 systems in Table 7, and
  **state in §9.3 how those 17 were selected** — this selection rule is currently
  nowhere in the manuscript, which is a separate defect regardless of which option
  is taken.
  - Suggested framing: "none of the 17 systems in Table 7, selected as the most
    advanced published exemplar in each of the five pillars, satisfies…"

- **GATE:** **Author: choose A, B, or A+B.** If A, the agent needs the scoring rubric
  (what makes a `✓` vs `(✓)` vs `×` vs `−` operationally, per dimension) before it
  can help build the script.
- **Regardless of choice — this sub-task is mandatory:** document the Table 7 row
  selection rule in §9.3.
- **Acceptance:** no claim anywhere in the manuscript quantifies over a population
  larger than the population actually scored.

---

### `[ ]` **B5 — Rebuild Figure 5 as the two-column PRISMA 2020 flow diagram** `AGENT-OK` (structure) / `GATE:AUTHOR` (approval)

- **Severity:** BLOCKING for PRISMA conformance.
- **The defect:** the IDENTIFICATION band contains only "1,150 snowball candidates."
  Three further retrieval streams enter mid-funnel:

  | Stream | n | Currently enters at |
  |---|---|---|
  | Pre-validated G0–G6 corpus | 352 | MERGE band |
  | Forward-citation snowball (Scopus+WoS) | 88 | abstract review |
  | Manual Scopus/WoS cross-validation top-up | 34 | data extraction |

  PRISMA 2020 Item 16a and the official flow diagram require all identification
  sources declared at identification. The **two-column variant** (left: databases and
  registers; right: other methods) exists for exactly this topology.
- **Action:**
  1. Redraw using the official PRISMA 2020 two-column template.
     - Left column: snowball retrieval via Semantic Scholar API (1,150 → 972 → 162).
     - Right column ("Identification of studies via other methods"): pre-validated
       corpus (352), forward snowball (88), manual top-up (34).
  2. Remove the nonstandard `MERGE WITH PRE-VALIDATED CORPUS` band (**N29**); fold it
     into Identification/Screening.
  3. Incorporate **N25** (19 UNCERTAIN → excluded), **N26** (sought/not-retrieved
     boxes), **M18** (abstract-2nd-pass path), **N28** (rescue-file labelling).
- **Note:** this task is the assembly point for five smaller tasks. Do them as one
  redraw, not five patches.
- **GATE:** author approves the redrawn figure before it replaces the current one.
- **Acceptance:** every one of the 123 final records can be traced from a box in the
  Identification band to the Included box without leaving the diagram.

---

### `[ ]` **B6 — Report the identification funnel for the G1–G6 Undermind route** `GATE:AUTHOR` / `BLOCKED:NEEDS-DATA`

- **Severity:** BLOCKING. This is the largest reporting gap in the review.
- **The defect:** the G1–G6 groups supply **105 of 123 final records (85.4%)**. §3.1
  says only that they were "assembled by manual curation of leading venues." There is
  **no candidates-returned count, no screened count, no rejection count** for the route
  that produced the overwhelming majority of the corpus. Appendix B gives the prompts;
  it gives no numbers.
- **Action:**
  1. Recover per-group counts from the Undermind exports / `slr_engine` retrieval logs:
     `candidates returned → screened → retained`.
  2. Add these as columns to **Table 3** (which currently has `n pre-val.` and `n final`).
  3. Add a short §3.1 paragraph describing the screening applied to this route
     (criteria, who screened, what was rejected and why).
  4. Feed the totals into the right-hand column of the redrawn Figure 5 (**B5**).
- **GATE / NEEDS-DATA:** **Author: do the Undermind exports retain candidate counts
  per query?** If yes, point the agent at the files. If the raw returns were not
  preserved, say so — the fallback is an explicit statement in §3.1 and §10.3 that
  candidate-level counts for this route were not retained, which is far better than
  silence but should be a deliberate choice.
- **Acceptance:** a reader can reconstruct 352 from a reported candidate pool, or is
  told explicitly that they cannot and why.

---

### `[ ]` **B7 — Source or delete the "5–13%" miss-rate estimate** `GATE:AUTHOR`

- **Severity:** BLOCKING (evidence integrity).
- **Location:** §10.3, Internal validity, margin line **1560**.
- **Current text:** "Single-reviewer screening has been estimated elsewhere to miss on
  the order of 5–13% of eligible studies relative to dual independent screening."
- **The defect:** "estimated elsewhere" with **no citation**. This is a specific numeric
  claim doing defensive work in the validity section. Note that the deleted mentor
  note (B1) itself referred to it as the "cited 5–13% miss-rate estimate" — so a
  citation was intended and lost.
- **Action:** either (a) locate the source in the systematic-review methodology
  literature, verify author/year/venue/DOI, and cite it; or (b) delete the numbers and
  rewrite as a qualitative statement.
- **GATE:** **Author: do you know which source this came from?** If yes, supply it.
  The agent must not select a plausible-looking citation on your behalf — see §0.2(4).
- **Acceptance:** no unsourced quantitative claim remains in §10.3.

---

### `[ ]` **B8 — Fix the Model Soups attribution in §10.1** `AGENT-OK`

- **Severity:** BLOCKING (miscitation).
- **Location:** §10.1, Finding 2, margin lines **1510–1515**.
- **Current text:** "LoraHub [37], Model Soups [74], and LoraRetriever [38] all
  demonstrate that independently trained adapters can be composed effectively using
  weight averaging or retrieval-based combination, without access to any task's
  original training data."
- **The defect:** Wortsman et al. [74] demonstrates nothing about adapters. It averages
  **full fine-tuned model weights**, from a **common initialisation**, on the **same
  task**, across hyperparameter configurations. In a numbered findings list this reads
  as primary evidence for a claim the source does not support.
- **Note the inconsistency:** §5.6 (lines 771–779) handles this *correctly*, with an
  explicit parenthetical that Model Soups was demonstrated on vision models and that
  the extension to LoRA is the author's own by-construction argument. §10.1 drops
  every caveat. The fix is to make §10.1 match §5.6, not the reverse.
- **Action:** rewrite Finding 2 to rest on LoraHub [37] and LoraRetriever [38]. Cite
  Model Soups [74] separately as the weight-averaging precedent, with the vision-domain
  and same-task qualifications intact.
- **Acceptance:** no claim about adapter composition cites [74] as demonstrating it.

---

### `[ ]` **B9 — Resolve the Data Availability contradiction** `GATE:AUTHOR`

- **Severity:** BLOCKING (research-integrity).
- **The defect:** the DAS states that "intermediate pipeline artefacts — the
  consolidated `pipeline_unified.csv`, retrieval/screening logs, and the per-record
  data-extraction spreadsheet — are regenerable local outputs of the pipeline and are
  **not separately version-controlled**."

  But those are exactly the files the manuscript offers as its audit trail:

  | Claim | Location | File named |
  |---|---|---|
  | "every per-record decision is logged in audit files for reproducibility" | §10.3 | — |
  | "per-record decisions are recorded in the audit log" | §A.4 | `log_screening_2026-04-21.json` |
  | "logged per record… to support reproducibility checks" | §A.7 | `S7b_abstract_reviewed_final.csv` |
  | "Every record and its per-stage membership are traceable" | §A.7 | `pipeline_unified.csv` |
  | "per-record codings are published in the accompanying data-availability record" | Table 4 | `14_final_curation_reasons` |

  A reader following these pointers reaches files the DAS says are unpublished.
  Because single-reviewer screening is the acknowledged principal internal-validity
  threat, and the per-record log is the **only** compensating control offered, this
  removes the mitigation.
- **Action — choose one:**
  - **B9-a (strongly preferred):** commit the five artefacts to `slr_engine`, update
    the DAS to list them, and keep every claim as written.
  - **B9-b:** remove or qualify every claim in §3, §10.3, §A.4, §A.7, and Table 4 that
    per-record decisions are available.
- **GATE:** **Author: is there any reason not to publish these files?** (Size, licensing,
  third-party metadata redistribution under Scopus/WoS terms — the last is a real
  constraint worth checking.) If Scopus/WoS terms block redistribution of retrieved
  metadata, publish the *decision columns* keyed by DOI without the licensed metadata,
  and say so.
- **Acceptance:** every file named in the manuscript as an audit artefact is either
  publicly resolvable or explicitly stated to be unavailable, with a reason.

---

## PHASE 2 — Major methodological issues

**Rationale:** these will not stop desk check but will drive a reviewer toward Major
Revision or Reject. M10 is the highest-value item in this phase.

---

### `[ ]` **M10 — Strengthen the quality assessment toward risk-of-bias** `GATE:AUTHOR`

- **The defect:** MDPI's review guidelines require "quality assessment, encompassing the
  risk of bias analyses." §3.4 is candid that it is not one, and the reasoning
  (methods-and-systems papers, not comparative interventions) is defensible. But
  examine what the six-dimension rubric actually measures:

  | Dim | Measures | Character |
  |---|---|---|
  | Q1 | venue-quality tag | bibliographic proxy |
  | Q2 | presence of DOI / arXiv ID | bibliographic proxy |
  | Q3 | named PEFT technique | substantive |
  | Q4 | quantified vs qualitative claim | substantive |
  | Q5 | contribution codes | **reported over n=16 of 123 (13%)** |
  | Q6 | your own relevance tier | self-referential |

  Three of six are proxies, one covers 13% of the corpus. A mean of 6.04 on this
  instrument tells a reader almost nothing about the methodological quality of the
  corpus.
- **The opening:** §3.4.1 is the strongest part of the appraisal — a **verified,
  dated, per-row** artifact-availability check across 33 systems that produced a real
  finding (79% release code; the gap concentrated precisely among the P2P/federated
  systems closest to the thesis). §3.4.1 already says baseline adequacy and
  threats-to-validity reporting "remain a candidate for a full-text re-read pass
  before submission."
- **Action:** do that pass. Extend the verified full-text check to **baseline adequacy**
  and **explicit threats-to-validity reporting** across at least the **48 Tier-1**
  records. Report the three dimensions as a distinct appraisal instrument alongside
  the reporting-completeness rubric — not folded into the 0–10 score.
- **GATE:** **Author: confirm scope — 48 Tier-1, or all 123?** And define the coding
  rule for each dimension before extraction begins, so the agent can build the
  scoring sheet.
- **Why this matters most in Phase 2:** it converts the paper's weakest rubric into a
  measured result, and it can be combined with the B4 Option-A pass over the same
  full texts. **Do B4-A and M10 in a single reading pass.**
- **Acceptance:** the manuscript reports at least three substantive (non-proxy)
  appraisal dimensions with stated coding rules and full per-record publication.

---

### `[ ]` **M11 — Qualify or complete the Wohlin snowballing claim** `GATE:AUTHOR`

- **The defect:** §3 and the abstract claim the review follows Wohlin et al. (2014).
  §A.2 discloses that **one wave** was executed and that saturation was "assessed
  qualitatively by inspecting the overlap between newly retrieved candidates and the
  pre-validated G1–G6 corpora," explicitly "not formalised as a quantitative stopping
  criterion." Wohlin's procedure iterates until no new papers are found.
- **Action — choose one:**
  - **M11-a:** run a second wave on the 162 screened-in records; report the marginal
    inclusion rate as the stopping criterion. This is the methodologically complete fix.
  - **M11-b:** restate throughout as "a single-wave adaptation of the snowballing
    procedure of Wohlin et al. [26]" — in the **abstract**, §3, §10.3, and §A.2. Keep
    the existing §A.2 disclosure.
- **GATE:** **Author: is a second wave feasible before your deadline?** The pipeline
  exists; the cost is screening time, not engineering. If not, M11-b is honest and
  sufficient — but it must propagate to the abstract, which currently says "Following
  PRISMA 2020 and Wohlin et al. snowballing" without qualification.
- **Acceptance:** the method named in the abstract is the method executed.

---

### `[ ]` **M12 — Address the inter-rater gap** `GATE:AUTHOR`

- **Context:** this is where the substance of the deleted B1 note lands.
- **Current state:** single reviewer, no IRR statistic. The manuscript's refusal to
  compute a spurious κ against a non-independent automated classifier is **correct
  and should be preserved** — do not let any fix reintroduce a fake reliability number.
- **Options, in descending order of strength:**
  - **M12-a:** recruit a colleague or co-supervisor to blind re-screen a random 5–10%
    sample of the 972 title-screened records; report percent agreement.
  - **M12-b:** author re-screens the same random sample after a time delay, blind to
    their own prior labels; report **intra-rater** agreement, labelled as a weaker
    but single-author-feasible substitute.
  - **M12-c:** no new measurement; strengthen the §10.3 disclosure only.
- **Recommendation:** **M12-b.** It is achievable solo before submission, it is honest
  about what it does and does not measure, and it converts the manuscript's weakest
  methodological point from an absence into a reported measurement.
- **Implementation if M12-b:** sample with a fixed seed from `log_screening_2026-04-21.json`;
  strip prior labels; re-screen; compute percent agreement and Cohen's κ on the
  intra-rater comparison; add a short paragraph to §3.2 and a sentence to §10.3.
  Publish the sample and both label sets.
- **GATE:** **Author: choose a, b, or c.**
- **Acceptance:** §10.3's internal-validity paragraph reports either a measurement or
  an explicit, reasoned statement that none was performed.

---

### `[ ]` **M13 — Make the adversarial search systematic** `GATE:AUTHOR`

- **Location:** §10.3, final paragraphs (lines 1600–1618).
- **The defect:** the review's headline finding is a **negative** claim. A negative
  claim's strength is exactly the strength of the search that failed to falsify it.
  The counter-search is described as **"non-systematic."** It surfaced Bittensor and
  Platformless AI and dismissed both on defensible substantive grounds — but reports
  no queries, no sources, no date, no screening rule.
- **Action:** re-run it systematically and report, in a new §3.5 or an appendix:
  queries, sources (**include grey literature, GitHub, and arXiv without the
  peer-review filter** — the two hits found were both non-academic, which tells you
  where the risk lives), execution date, and the disposition of every candidate.
- **Keep:** the existing substantive analysis of why neither system meets the
  seven-dimension profile. That reasoning is sound. Only the search apparatus is missing.
- **GATE:** author approves the query set before execution.
- **Acceptance:** a reader can re-run the disconfirming search from the manuscript alone.

---

### `[ ]` **M14 — Add a related-surveys search and comparison table** `GATE:AUTHOR`

- **The defect (two parts):**
  1. §3.1 states outright: "No search was dedicated specifically to locating competing
     systematic reviews or umbrella surveys of this exact scope." For a review whose
     contribution is "no prior survey addresses this intersection," this is directly
     load-bearing.
  2. There is no related-surveys comparison table. §1 differentiates against six works
     ([10,11,12] PEFT/LoRA surveys; [13,14] decentralised FL; [15] P2P connection
     establishment) in a single prose paragraph. The corpus holds 9 survey records.
     Nothing shows which survey covers which pillar and where each stops.
- **Action:**
  1. Run a dedicated search for reviews/surveys/SLRs across the five pillars; report
     strings and dates in §3.
  2. Build **Table 9 (new)**: rows = existing surveys; columns = the five pillars +
     the seven design dimensions. Let the empty cells carry the argument.
- **Why this is high-value:** for a review whose contribution is organisational, this
  table *is* the contribution's evidence. It is also the single most likely thing a
  referee asks for.
- **GATE:** author approves the survey set before the table is built.
- **Acceptance:** the positioning claim in §1 rests on a reported search, not an assertion.

---

### `[ ]` **M15 — State honestly what the extraction sheet contains** `AGENT-OK`

- **The defect:** Table A3 records that `method_name`, `datasets`, and `metrics` are
  **uniformly empty** across all 224 extraction rows. Those are the three fields that
  would make an extraction table an extraction table rather than a bibliographic
  register. What remains populated: `paper_key`, `doi`, `title`, `authors`, `year`,
  `venue`, `citation_count`, `tier`, `review_source`.
- **The implication:** the synthesis in §§4–8 was drawn from full-text reading, not
  from the coded extraction sheet. That is entirely legitimate — but the Methods
  currently imply a structured extraction that did not occur.
- **Action:** add a short, plain statement in §3.1 or §3.4 distinguishing (a) what was
  coded in the extraction sheet from (b) what was read and synthesised narratively.
  Table A3's existing note is a good starting point — promote it to the main text.
- **Do not:** retro-populate the empty fields. That would be fabrication.
- **Acceptance:** no reader can infer from the Methods that the synthesis was
  machine-derived from coded fields.

---

### `[ ]` **M16 — Name the automated screening classifier in-text** `GATE:AUTHOR`

- **Locations:** §A.4 (Layer-3 triage over 130 records) and §A.7 (advisory KEEP/SKIP/
  DEFER notes across 552 abstracts).
- **Current state:** both say the model identifier is "recorded in the audit log."
  §3's GenAI disclosure names Undermind and Claude Opus 4.5 but not this classifier.
- **The defect:** in a submission to *AI*, about an AI-assisted review, read by
  AI-literate referees, burying the classifier identity in a log invites exactly the
  suspicion the rest of §3 works to avoid.
- **Action:** name the model and version in §3's disclosure paragraph and at both
  appendix locations. Also add a version or access date for Undermind (currently
  unversioned while Claude Opus 4.5 is versioned — an inconsistency).
- **GATE:** **Author: supply the classifier model ID + version from
  `log_screening_2026-04-21.json`, and the Undermind access date.**
- **Acceptance:** every AI tool used at any decision-adjacent stage is named with a
  version in the main text.

---

### `[ ]` **M17 — Fix Acknowledgments and disclose relationships** `GATE:AUTHOR`

- **The defect:** `Acknowledgments: Not applicable.` is almost certainly wrong. Evidence
  in the manuscript itself: p. 9 contains a note addressed to a mentor (B1); §3
  discloses that the search strategy originated as doctoral coursework at Rijeka;
  §10.3 refers to "an external audit of this manuscript."
- **Related — the Šajina question.** Šajina et al. [9] is a G0 seed, the "closest
  published predecessor," a row in Table 5, a row in Table 7, and a recurring anchor
  in §8.4 and §10.1. Šajina 2025 is a **University of Rijeka doctoral thesis** — your
  own institution, cited from the institutional repository (`infri:1394`). Meanwhile
  Conflicts of Interest reads "none" and Acknowledgments reads "Not applicable."
- **Action:**
  1. Write a real Acknowledgments statement naming supervisors, advisors, and anyone
     who reviewed drafts.
  2. If Šajina is your supervisor, co-supervisor, or group colleague, **state the
     relationship**. One sentence. It costs nothing and pre-empts the question.
- **GATE:** **Author: who should be acknowledged, and what is your relationship to
  Šajina?** The agent cannot know this.
- **Acceptance:** no reader can discover an undisclosed relationship that the
  manuscript's own text hints at.

---

### `[ ]` **M18 — Declare the coursework self-overlap (iThenticate)** `GATE:AUTHOR`

- **Context:** §3 discloses that "an earlier version of the search strategy and
  screening protocol described in this section was developed as coursework for a
  doctoral Research Methodology course at the University of Rijeka; the review has been
  substantially revised for this submission."
- **The risk:** if that coursework was deposited in the Rijeka institutional repository
  — as Šajina's thesis was — iThenticate will match it at high similarity against your
  entire Methods section. Undisclosed self-overlap with a repository-deposited document
  surfaces at production rather than at review, which is a much worse place to find it.
- **Other predictable hits, both benign but worth pre-empting in the cover letter:**
  - PRISMA boilerplate in §3 / §3.4 — normal and tolerated.
  - Appendix B's verbatim Undermind prompts and Appendix C's verbatim Scopus strings —
    intentionally verbatim for reproducibility; say so.
- **Action:**
  1. **Author: check whether the coursework version is deposited.**
  2. If yes, cite it as a formal reference rather than mentioning it narratively, and
     declare the overlap in the cover letter.
  3. Draft the cover-letter paragraph covering all three overlap sources.
- **GATE:** author confirms deposit status.
- **Acceptance:** every known source of similarity is either cited or declared.

---

### `[ ]` **M19 — Show the abstract-2nd-pass route in the flow diagram** `AGENT-OK`

- **The defect:** §3.2 reports that **53 of the 123 final records (43.1%)** carry
  `review_source = abstract-2nd-pass`. Figure 5 places all 190 extraction inputs inside
  "190 from full-text queue," implying a full-text eligibility assessment that, by the
  manuscript's own account, 53 records did not receive at that point.
- **Action:** in the **B5** redraw, give the second abstract-review pass its own path
  into extraction, or state the sub-counts explicitly in the Figure 5 caption
  (70 via full-text queue + 53 via abstract-2nd-pass = 123).
- **Depends on:** B5. Execute together.
- **Acceptance:** the diagram does not imply an assessment stage that 43% of the corpus
  bypassed.

---

### `[ ]` **M20 — Reconsider protocol registration** `GATE:AUTHOR`

- **Current justification (§3):** "systematic reviews of computer-science and AI systems
  literature are not commonly eligible for clinical registries such as PROSPERO, and no
  suitable AI-specific registry was available at the time of commencement."
- **The defect:** PROSPERO's health-relatedness restriction is real. But **OSF
  Registries and protocols.io accept CS and engineering review protocols and are not
  clinical registries.** The justification as written is factually too narrow and a
  methodologist referee will say so.
- **Action — choose one:**
  - **M20-a:** register retrospectively on OSF, disclose the registration date and
    that it is retrospective. Retrospective registration is weaker than prospective
    but far better than none.
  - **M20-b:** revise the §3 justification to acknowledge OSF/protocols.io explicitly
    and explain why they were not used.
- **GATE:** **Author: a or b?**
- **Acceptance:** the justification is accurate about what was available.

---

### `[ ]` **M21 — Add per-pillar synthesis to §§4–8** `GATE:AUTHOR`

- **The defect:** §§4–8 follow a subsection-per-method pattern ("X et al. showed Y"),
  and each closes with a single pointer sentence — e.g. "The composition findings of
  this section are consolidated, alongside the other four sub-questions, in the
  centralised discussion in Section 9.1." Deferring all synthesis to §9 leaves ~25
  pages reading as descriptive survey.
- **Note:** §9 itself is genuinely strong interpretive synthesis. This task is about
  §§4–8 only.
- **Action:**
  1. Add a closing synthesis paragraph to each of §§4–8: what the pillar collectively
     establishes, where its members disagree, and which of its assumptions breaks in a
     P2P setting.
  2. Add a per-pillar comparison table. **§6 most urgently** — S-LoRA / Punica /
     CaraServe / dLoRA differ on batching strategy, memory management, and rank
     handling in ways a table makes legible at a glance and prose does not.
- **GATE:** these paragraphs are argument, not reporting. **The author writes them.**
  The agent may prepare the comparison-table scaffolds from existing text.
- **Acceptance:** no review section ends without stating what it collectively shows.

---

## PHASE 3 — Minor issues

Batch these. Most are `AGENT-OK`. Group the LaTeX-mechanical ones into one commit and
the prose ones into another.

### Evidence and citation

- `[ ]` **N22** `GATE:AUTHOR` — §5.6, line 775: "provided the adapters share the same
  initialisation point." This does not hold as written. Independently trained LoRAs do
  not share an initialisation point in the sense model-soup averaging requires: A is
  randomly initialised per run and B is zero-initialised, so two adapters trained by
  different peers occupy arbitrarily rotated subspaces — which is *why* LoraHub learns
  combination coefficients rather than mean-averaging. Since the SQ2 answer leans on
  this, tighten to: adapter weight averaging is a **plausible but unvalidated**
  zero-shot strategy — which is itself one of your own empirical gaps.
- `[ ]` **N23** `GATE:AUTHOR` — §10.1 Finding 1: "2–10 MB for r = 4–8 at GPT-2 scale"
  has no source. Either cite a paper reporting adapter sizes, or state the derivation
  with the assumed hidden dimension and layer count.
- `[ ]` **N24** `AGENT-OK` — §10.1 Finding 3: cite the specific papers reporting the
  endpoints of the "90–99%" communication-reduction range at the point of claim, not
  the group label "G6".
- `[ ]` **N25** `GATE:AUTHOR` — Table 5, two score rows need re-verification against
  primaries, with backbone/config stated: **LoRA "87.8 (GLUE avg.)"** (the LoRA paper
  reports different GLUE averages for RoBERTa-base / RoBERTa-large / DeBERTa-XXL — which
  row?) and **Li & Liang "34.9 (XSUM ROUGE-L)"**. Table 5's caption already promises
  every score is traceable to a cited primary — make each traceable to a table and row.
- `[ ]` **N26** `AGENT-OK` — Replace Table 8's Evidence column. It currently cites
  retrieval groups ("G0–G6", "G3, G4", "G2, G5"). A gap evidenced by a retrieval group
  is not evidenced. Use specific record IDs or citations that were checked.
- `[ ]` **N27** `GATE:AUTHOR` — Verify corpus coverage of adjacent recent work before a
  referee does. Confirm presence or explain exclusion for: heterogeneous-rank federated
  LoRA (FlexLoRA / HetLoRA / FFA-LoRA); decentralised training beyond Petals (DiLoCo,
  SWARM); adapter-retrieval beyond LoraRetriever. *(Ostapenko [39] and PHATGOOSE/Muqeeth
  [99] are already present.)* Absence is not asserted here — verify.
- `[ ]` **N28** `AGENT-OK` — Replace the 49 arXiv DOIs (`10.48550/…`) with publisher DOIs
  where a published venue is cited: [1] Vaswani (NeurIPS), [3] Houlsby (PMLR/ICML),
  [4] Hu (ICLR), [5] Sheng (MLSys), [6] Chen (MLSys), and the rest. Add a DOI to
  **reference [7]** (Toppings, USENIX ATC 2025), which currently has none.

### PRISMA reporting detail *(fold into B5 where marked)*

- `[ ]` **N29** — Report the 19 UNCERTAIN title-screening records as **excluded**
  (n = 19, unresolved after triage), so 972 = 810 excluded + 162 sought. → fold into B5.
- `[ ]` **N30** — Add PRISMA "Reports sought for retrieval" / "Reports not retrieved"
  boxes; move the 24 full-text-unavailable records into *not retrieved*, out of the
  combined "197 excluded from queue". → fold into B5.
- `[ ]` **N31** `GATE:AUTHOR` — Retro-code exclusion reasons for the 165 abstract-review
  SKIPs from `S7b_abstract_reviewed_final.csv`, **or** state explicitly in §3 that
  PRISMA Item 16b is satisfied at the eligibility stage (Table 4, fully categorised) and
  **not** at abstract review.
- `[ ]` **N32** — Reconcile Figure 5's "38 excluded in enrichment" with §A.5/§A.7, which
  describe 32 as "deprioritised to a rescue file" and only confirmed excluded later at
  abstract review. → fold into B5.
- `[ ]` **N33** — Remove the nonstandard `MERGE WITH PRE-VALIDATED CORPUS` band. → fold
  into B5.

### Internal consistency

- `[ ]` **N34** `AGENT-OK` — Table 5 / §3.4.1 category mismatch. The caption defines four
  values (Yes / Partial / **No** = "no artifact released" / **Unknown** = "no public
  artifact could be located"). §3.4.1 then says *"For 6 systems (18%)… no public artifact
  could be located,"* collapsing the 2 `No` and 4 `Unknown` rows into the `Unknown`
  definition. Counts are right (26+1+2+4 = 33); categories are not. Also the `Partial`
  row (FedAvg) is never assigned in the prose totals — 79% + 18% = 97%.
- `[ ]` **N35** `AGENT-OK` — Standardise tier labels. Three variants currently coexist:
  Table A2 ("PEFT + distributed/P2P + LLM" / "two of the three themes" / "one theme"),
  Figure A1 axis ("PEFT+Systems+LLM" / "PEFT+LLM" / "Other"), Figure A3 legend
  ("PEFT + LLM / PEFT + Systems" / "Other / foundational"). Adopt Table A2's wording
  everywhere.
- `[ ]` **N36** `AGENT-OK` — §3.2: report the study-type split (114 primary / 9 survey)
  over the **120 distinct papers**, not the 123 rows, which include 3 duplicates. Note
  the row-vs-paper basis.
- `[ ]` **N37** `AGENT-OK` — Fix the DEFER contradiction. §3.1: "173 were classified SKIP
  but re-flagged DEFER." Table A5 caption: "DEFER records were not disposed of as SKIP."
  A5's three-way canonical split is correct; fix §3.1.
- `[ ]` **N38** `GATE:AUTHOR` — Clarify Table 3's attribution rule. The caption says each
  final record is attributed to "the single pre-validated group recorded by the unified
  pipeline," and that G0's n=18 includes "14 snowball descendants" — so snowball-
  discovered records can carry a G-group label. But §3.2 uses the 105 records in G1–G6
  as evidence that "85.4% of the final corpus… were assembled via targeted,
  framing-informed retrieval rather than blind snowball screening." If G1–G6 also absorb
  snowball descendants, 85.4% overstates the curated share. **Report the split by
  discovery route, not by group label.**
- `[ ]` **N39** `AGENT-OK` — Table A4: note the rounding in the caption (% column sums to
  100.1).
- `[ ]` **N40** `AGENT-OK` — Expand "MT-EF" (Multi-Task Encoder Fusion) at first use in
  Table 5, p. 14. It is currently first expanded in the §8.4 heading, p. 32.

### Figures, floats, typography

- `[ ]` **N41** `GATE:AUTHOR` — Figures 3 and 14 are near-duplicates (both illustrate
  Kademlia XOR-metric lookup). Cut one, or make Figure 14 do different work — e.g. show
  **adapter-capability keys** in the DHT rather than a generic lookup, which would also
  strengthen §8.6.
- `[ ]` **N42** `GATE:AUTHOR` — "(own figure)" attribution is inconsistent: present on
  Figures 2, 7, 8, 9, 11, 12, 13, 14; absent on 1, 3, 4, 5, 6, 10, 15. If all are
  original, mark all. If any is adapted, MDPI requires the source and a permission
  statement.
- `[ ]` **N43** `AGENT-OK` — Swap Figure A2/A3 numbering (A3 is currently cited before
  A2 in §A.6); move Table A3 before Table A4 (A3 is cited first but placed second).
- `[ ]` **N44** `AGENT-OK` — Typos: `contribution.Forward` (§3.1, missing space);
  `(Table A4; Figure A3),with` (§A.6, missing space). Then run a full-source scan for
  `[a-z]\.[A-Z]` and `,[a-z]` outside URLs/filenames.
- `[ ]` **N45** `GATE:AUTHOR` — 71 pages is long for *AI*. Consider moving parts of
  §§4–8 to supplementary. Judgment call; not required.

### Claims and framing

- `[ ]` **N46** `AGENT-OK` — §1: "The specific synthesis gap this review **closes**" →
  "**identifies**." The review identifies and characterises the gap; it does not close it.
- `[ ]` **N47** `AGENT-OK` — §10.2: "no prior finding has examined this intersection"
  drops the corpus bound that §9 carefully establishes ("All gap claims in this section
  are bounded by the 123-paper corpus"). Restore: "within the reviewed corpus."

### Repository and availability

- `[ ]` **N48** `GATE:AUTHOR` — Archive both `paper_code` and `slr_engine` to **Zenodo**
  and cite the DOIs in the DAS. GitHub URLs are not persistent identifiers and MDPI
  prefers PIDs.
- `[ ]` **N49** `GATE:AUTHOR` — Supply the **ten Web of Science search strings** for
  Appendix C. Currently only the ten Scopus queries are reproduced verbatim; WoS is
  described only as "Topic-field (TS=) queries… with equivalent year filters."
  *Not found in the manuscript — provide.*

---

## PHASE 4 — Pre-submission verification

Run in order. All must pass.

```bash
# 1. No leftover working notes anywhere in source
grep -rniE "TODO|FIXME|XXX|TREBA|OVAJ|POGLEDATI|ODLUČITI|MENTOR|REMOVE BEFORE|placeholder" *.tex

# 2. Counts unchanged (see §1 Frozen values)
python slr_engine/scripts/verify_prisma_counts.py
python slr_engine/scripts/verify_quality_appraisal.py

# 3. Every float cited, in ascending first-mention order
#    (main text and appendix sequences checked separately)

# 4. Every reference cited; every citation resolves
#    Expect 128 refs, contiguous 1..128, no gaps, none uncited

# 5. Every DOI resolves (HTTP 200 via doi.org)

# 6. No unsourced quantitative claim
#    Manual pass over §10.1, §10.3, §3.4, Table 5
```

**Manual checklist before upload:**

- `[ ]` ORCID present in title block (B2)
- `[ ]` Abstract ≤ 200 words, single paragraph, no citations *(currently 179 — recheck
      after any edit to it, especially from B4 and M11)*
- `[ ]` Keywords 3–10 *(currently 9)*
- `[ ]` PRISMA 2020 27-item checklist attached as S1 — **not present in the audited PDF;
      confirm it is uploaded**
- `[ ]` Supplementary S2 (`quality_appraisal_scored.csv`) attached; S3 added if B4-A taken
- `[ ]` Back matter complete: Author Contributions, Funding, IRB, Informed Consent, Data
      Availability, Supplementary Materials, Acknowledgments (M17), Conflicts of Interest,
      Abbreviations
- `[ ]` Cover letter declares: coursework overlap (M18), verbatim search strings in
      Appendices B/C, PRISMA boilerplate
- `[ ]` iThenticate pre-check run and reviewed
- `[ ]` Every claim quantifies only over the population actually scored (B4)
- `[ ]` The method named in the abstract is the method executed (M11)

---

## 5. Suggested execution order

Phases are ordered by gating dependency, not by severity alone.

```
Sprint 1 (mechanical — 1 sitting)
  B1, B3, B8  ............................ agent, unaided
  N28, N34, N35, N36, N37, N39, N40,
  N43, N44, N46, N47  ................... agent, batched
  → author reviews two commits

Sprint 2 (author inputs — collect in one pass)
  B2  (ORCID)
  B7  (5–13% source)
  M16 (classifier ID + Undermind date)
  M17 (acknowledgments + Šajina relationship)
  M18 (coursework deposit status)
  B9  (publish audit files? any blocker?)
  N49 (WoS strings)
  → these are all "look it up and paste it" tasks; do them together

Sprint 3 (decisions — author chooses, agent implements)
  B4  (A / B / A+B)      ← highest impact
  M10 (scope of appraisal pass)
  M11 (second wave or requalify)
  M12 (a / b / c — recommend b)
  M20 (a / b)
  → B4-A and M10 share one full-text reading pass. Plan them together.

Sprint 4 (new work)
  B6  (Undermind funnel)
  M13 (systematic adversarial search)
  M14 (survey search + Table 9)
  M21 (per-pillar synthesis — author writes)

Sprint 5 (assembly)
  B5 + M19 + N29 + N30 + N32 + N33  ..... one Figure 5 redraw
  N31, N38, N41, N42, N45, N48
  Phase 4 verification
```

**Critical path:** B4 → M10 (shared reading pass) → B5 redraw → verification.
Everything else can run in parallel.

---

## 6. What is already good — do not "fix" it

The agent should be told this explicitly, because several of these look like defects
to a naive pass and are not.

1. **All PRISMA arithmetic reconciles.** Seventeen stage transitions plus the per-seed
   retrieval counts were independently recomputed. Zero errors. Do not "correct" any
   frozen value.
2. **The 123 vs 120 distinction is correct and well-footnoted.** Three works appear
   twice (LoRA arXiv+Scopus; Houlsby arXiv+Scopus; CaraServe preprint + Toppings ATC).
   Leave the footnote intact.
3. **The refusal to report a κ against a non-independent classifier is methodologically
   right.** Do not let M12 reintroduce a fake reliability statistic.
4. **The GenAI disclosure in §3 is close to fully compliant** — tools named, roles
   stated, no decision authority delegated, responsibility statement present, AI not an
   author. M16 refines it; it does not need rewriting.
5. **§9 is genuine interpretive synthesis**, not a catalogue: a defended
   seven-dimension framework, dimensions explicitly considered *and rejected* with
   reasons, a four-quadrant taxonomy on a principled axis choice, and eight open
   questions mapped to unaddressed dimensions. M21 targets §§4–8 only. **Do not touch §9's
   argument.**
6. **The hedging discipline is above average** — "to the author's knowledge," "within the
   reviewed corpus," "bounded by the 123-paper corpus." Preserve it. B4 and N47 tighten
   the two places where it slipped; they do not license loosening it elsewhere.
7. **§3.4.1's artifact-availability check is the strongest appraisal element** —
   verified, dated, per-row, and it produced a real finding. M10 extends this method; it
   does not replace it.
8. **The disclosure culture throughout is unusually honest** (single-reviewer limitation,
   start-set bias, uncoded SKIP reasons, non-formalised saturation, coursework origin).
   Several tasks above make the paper *more* exposed. That is the correct direction.
9. **Table A6 is a real chronological search log.** Most SLRs have nothing like it.
10. **Two verification scripts recompute the funnel from source data.** Almost no
    submission ships these. Consider mentioning them in the cover letter.

---

## 7. Assessment at time of writing

| Criterion | Score (1–5) | Note |
|---|---|---|
| Novelty | 4 | Gap map + seven-dimension framework are a real organisational contribution |
| Scope | 4 | Five pillars well-bounded; missing survey-of-surveys (M14) |
| Significance | 4 | Contingent on B4 |
| Quality of presentation | 2 | B1, B3, N41–N44 |
| Scientific soundness | 3 | M10, M11, M12, M15 |
| Interest to readers | 4 | — |
| Overall merit | 3 | Strong core, fixable shell |
| English | 4 | Two typos + one non-English block (B1) |

**Simulated recommendation: Major Revision (reconsider after major revision).**

Nothing in this plan requires re-running the review. The desk-check items are
mechanical; the identification gap is a reporting fix plus one count per Undermind
group; the Table 7 scope problem is a rewrite or a scoring pass; the data-availability
contradiction is a `git add`. The only item requiring substantial new effort is the
full-text appraisal pass — and B4-A and M10 share it.

---

## 8. Change log

| Date | Phase | Tasks completed | Validated by |
|---|---|---|---|
| | | | |

---

## 9. Observations backlog

Anything the agent notices that is not in this file. Do not act on these; log them.

| # | Location | Observation | Author decision |
|---|---|---|---|
| | | | |
