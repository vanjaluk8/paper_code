# SLR Revision Guide — Decentralised Adapter-Based LLM Inference (MDPI *AI*)

> **How to use this file.** Drop it at the root of the manuscript repo (`papers_code/`) as
> `SLR_REVISION_GUIDE.md`, and either rename it `CLAUDE.md` or add this line to your existing
> `CLAUDE.md`:
> `Before any manuscript edit, read SLR_REVISION_GUIDE.md in full. It is authoritative.`
>
> Work **one task at a time**. After each task, run the verification harness (§10) and commit.
> Do not batch tasks across phases.

---

## 1. What this project is

A single-author PRISMA 2020 systematic literature review submitted to MDPI *AI* (ISSN 2673-2688),
article type **Systematic Review**. 69 pp., ~28k words, 128 references, 15 main figures + 3 appendix
figures, 7 main tables + 6 appendix tables. Corpus: **123 included records / 120 distinct papers**
across five pillars (PEFT, adapter composition, inference serving, MoE routing, P2P/federated).

The paper's entire contribution is a synthesis bounded by that corpus. **The integrity of the corpus
description is therefore the contribution.** A reader who cannot reconstruct how 123 records were
arrived at cannot rely on a single gap claim. Treat every count as load-bearing.

A pre-submission peer review returned **Major Revision** with **7 blocking**, **11 major**, and
**22 minor** issues. This guide is the remediation plan.

### Repos and artefacts

| Thing | Where | Role |
|---|---|---|
| LaTeX source | `papers_code/` (this repo) | The manuscript. MDPI LaTeX template. |
| Pipeline + data | `slr_engine/` | Retrieval, screening, extraction; the source of truth for every number. |
| Final reading list | `slr_engine/.../13_final_reading_list_2026-05-12.csv` | **Authoritative** 123-record list. |
| Unified pipeline | `pipeline_unified.csv` | Per-record, per-stage membership. |
| Extraction table | `11_data_extraction_2026-05-12.csv` | 224 rows, schema in Appendix A Table A3. |
| Screening log | `log_screening_2026-04-21.json` | Title-screen decisions. |
| Retrieval log | `log_retrieval_2026-04-21.json` | Per-seed counts. |
| Abstract review | `S7b_abstract_reviewed_final.csv` | KEEP/DEFER/SKIP dispositions. |
| Verifiers | `slr_engine/scripts/verify_prisma_counts.py`, `verify_quality_appraisal.py` | Recompute reported stats. |
| Quality scores | `figures/quality_appraisal_scored.csv` | 123 rows; Tier-1 rows carry `code_released`, `evaluated_vs_baseline`, `threats_reported`. |

**First action of any session:** confirm which of these files actually exist and are readable.
Several were described in the Data Availability statement as "regenerable local outputs … not
separately version-controlled." If they are missing, **stop and tell the user** — most of Phase 1
is impossible without them.

---

## 2. Non-negotiable rules

These override any instinct to be helpful.

**R1 — Numbers come from data, never from reconciliation-by-editing.**
When two numbers in the manuscript disagree, the fix is to query the pipeline and find out which is
right. It is *never* to pick one and overwrite the other so the text reads consistently. If you
cannot resolve a disagreement from the data, leave both, add a `% FIXME:` comment, and report it.

**R2 — Never invent a fact that belongs in the evidence base.**
No invented exclusion reasons, no invented survey rows, no invented citation counts, no invented
DOIs, no invented artifact-availability codings. If a value is unknown, write `\todo{not found —
provide}` and surface it.

**R3 — Do not soften the paper's candour.** See §3. The honest disclosures are the manuscript's
strongest asset and a reviewer specifically credited them. Removing them to make the paper "look
better" would be a serious regression.

**R4 — No `sed`-style global replaces on prose.** Every wording change is a targeted edit with the
surrounding sentence read first. Global replaces will corrupt quoted titles, reference entries,
and figure captions.

**R5 — One task, one commit.** Commit message format: `fix(B1): reconcile 53-record provenance claim`.
Task IDs come from §11.

**R6 — Compile after every phase.** `latexmk -pdf` (or the project's build command) must succeed and
the page count must not change unexpectedly. A silently broken `\ref` renders as `??`.

**R7 — Stop and ask the user** in the situations listed in §12. Do not guess.

---

## 3. Protected content — do NOT remove or soften

These passages were explicitly praised in review. Preserving them is a requirement, not a preference.

- **§3.2 single-reviewer disclosure** — the argument that PRISMA Item 8 requires *reporting* the
  number of reviewers, not dual screening; and the refusal to report a κ computed against a
  non-independent artefact. Keep the reasoning intact. You will *add* a calibration measure (M3);
  you will not delete the disclosure.
- **§3.2 confirmation-bias paragraph** — "Both risks are therefore acknowledged as complementary,
  not mutually mitigating." Keep verbatim.
- **§3.1 / §10.3 abstract-review reporting gap** — the admission that 165 SKIP records carry no
  individually coded exclusion reason. Keep.
- **§10.3 adversarial search** — Bittensor and Platformless AI, including the reasoning about why
  neither qualifies. Keep in full.
- **§3 AI-tool disclosure** — Undermind and Claude Opus 4.5, with roles and the responsibility
  statement. Keep; you will only *add* the model identifier for the screening classifier and
  optionally mirror it in Acknowledgments.
- **§3 coursework-lineage disclosure** — "An earlier version of the search strategy … was developed
  as coursework for a doctoral Research Methodology course." Keep. This protects against a
  similarity-report surprise.
- **Footnote on 123 vs 120 distinct papers** — the three double-counted retrieval keys. Keep.
- **§3.4 scope caveat** — that the rubric measures reporting completeness, not intrinsic merit, and
  that classic quality dimensions were "scoped out here and disclosed rather than estimated." Keep
  the disclosure even as you extend the appraisal (M2).

---

## 4. Known failure modes for this specific task

Read these before starting. Each has been observed on work of this shape.

| # | Failure | Why it happens | Guard |
|---|---|---|---|
| F1 | Editing "53" → "12" to make §3.2 agree with §C.3 | Both numbers are in the text; the agent treats it as a typo | R1. The 53 may be a *correct* count of `review_source = abstract-2nd-pass` records mis-*attributed* to the 88-record branch. Query first. |
| F2 | Writing plausible-sounding exclusion reasons for the 101 | The table has an empty column and the agent fills it | R2. Reasons must be derived from the extraction/curation data or coded by the human. |
| F3 | Deleting the "no inter-rater statistic" paragraph as a weakness | Agent optimises for reviewer approval | R3 + §3. |
| F4 | Populating the survey-comparison table (M1) from memory | Agent knows PEFT surveys exist | R2. Only rows retrieved by the documented search, with DOIs. |
| F5 | Regenerating Figure A1 from the final-list dataframe again | The plotting script defaults to the 123-record CSV | Assert `len(df) == 464` before plotting. |
| F6 | `sed 's/chapter/section/g'` | Fast and tempting | R4. 18 occurrences; several are inside sentences that need rewording, and reference titles may contain "Chapter". |
| F7 | Replacing "we/our" inside the abstract's hedge "To our knowledge" without checking whether the hedge should survive | Voice sweep | Rewrite as "To the author's knowledge" — keep the hedge, change the pronoun. |
| F8 | Fixing `\ref{}` targets by renumbering rather than by correcting the label | Cross-ref errors look like numbering errors | The §3.3/§3.4 and Appendix B/C errors are *wrong targets*, not wrong numbers. |
| F9 | Adding `\cite`-style in-text callouts for Figures 8–14 in the wrong place | Agent inserts "(see Figure 8)" mechanically at the caption | The callout belongs at the point of first *discussion*, which is usually 1–3 paragraphs above the float. |
| F10 | Cutting §§4–8 by deleting whole subsections | "Cut 4,000 words" read as "delete content" | Compress prose into the new comparison tables (M6); no pillar loses coverage. |
| F11 | Trusting `pdftotext` output for numbers inside two-column or rotated tables | Extraction garbles some table cells | Cross-check any table number against the `.tex` source, not the PDF text. |

---

## 5. Phase 0 — Discovery (do this first, every session)

```bash
# 1. Manuscript structure
find . -name '*.tex' | head -50
wc -l $(find . -name '*.tex')
grep -rn '\\input\|\\include' --include='*.tex' . | head -30

# 2. Build works?
latexmk -pdf -interaction=nonstopmode <main>.tex && pdfinfo <main>.pdf | grep Pages

# 3. Which data files are actually present?
for f in 13_final_reading_list_2026-05-12.csv pipeline_unified.csv \
         11_data_extraction_2026-05-12.csv log_screening_2026-04-21.json \
         log_retrieval_2026-04-21.json S7b_abstract_reviewed_final.csv \
         figures/quality_appraisal_scored.csv; do
  find .. -name "$(basename $f)" -print 2>/dev/null | head -1 | \
    xargs -r -I{} sh -c 'echo "FOUND {}"' || echo "MISSING $f"
done

# 4. Baseline verification snapshot
python3 tools/check_manuscript.py <main>.pdf > reports/baseline.txt
```

Report to the user: file inventory, build status, and the baseline check output. **Do not start
editing until the user confirms the data files you found are the right ones.**

---

## 6. Phase 1 — Data-truth fixes (require querying the pipeline)

Do not attempt these without the data files. Each produces a *finding* first, then an edit.

### B1 — The 53-record provenance contradiction ⛔ BLOCKING

**Symptom.** §3.2 (p. 9): *"the remaining 53 (43.1%) were added by the supplementary
forward-citation snowball … and 53 of the 123 final records trace to this supplementary branch."*
But §3.1, Appendix D §C.3 and Table A6 all state the 88 forward-snowball records resolved to
**12 KEEP, 4 DEFER, 72 SKIP**, and §C.3 adds the 4 DEFER "were resolved to SKIP in the final
consolidation." Table A6's pass-1→final delta confirms it exactly: 202→214 (+12), 169→173 (+4),
93→165 (+72), summing to 88.

**Hypothesis to test (do not assume).** The 53 is probably a correct count of final records whose
`review_source` field equals `abstract-2nd-pass`, drawn from the **464-record pool** reviewed in the
second abstract pass — *not* from the 88 forward-snowball additions. If so, the number is right and
the **attribution sentence is wrong**.

**Query.**
```python
import pandas as pd
final = pd.read_csv('13_final_reading_list_2026-05-12.csv')
ext   = pd.read_csv('11_data_extraction_2026-05-12.csv')
uni   = pd.read_csv('pipeline_unified.csv')

print(len(final))                                   # expect 123
m = final.merge(ext, on='paper_key', how='left')
print(m['review_source'].value_counts(dropna=False)) # expect fulltext / abstract-2nd-pass split
# Which of the 123 carry the forward-snowball source group?
for col in uni.columns:
    if 'group' in col.lower() or 'source' in col.lower():
        print(col, uni[col].dropna().unique()[:20])
# G_SNOW_F is the forward-snowball group label per §C.3
```

**Then produce**, and paste into the revision letter:
- N final records with `review_source == 'abstract-2nd-pass'`
- N final records whose source group is `G_SNOW_F`
- N final records on the primary full-text-queue path

**Edit.** Rewrite the §3.2 sentence to state the *actual* rule that defines each cohort. Example
shape only — use your real numbers:
> "Of the 123 included records, X entered via the primary full-text queue and Y were adjudicated in
> the second abstract-review pass (`review_source = abstract-2nd-pass`), of which Z originate from
> the supplementary Scopus/WoS forward snowball (source group `G_SNOW_F`)."

Then reconcile §3.1, §C.3 and Table A6 to the same three numbers.

**Done when.** §3.1, §3.2, §C.3, Table A6 and Figure 5 all use one consistent cohort vocabulary and
one set of counts, and the guide's check script reports no residual `53`-vs-`12` mismatch.

---

### B2 — Table 3 assigns 18 final records to a 9-paper group ⛔ BLOCKING

**Symptom.** Table 3 (p. 11): G0 `n pre-val. = 9`, `n final = 18`. Table 2 (p. 10) independently
documents that only **six of nine** G0 seeds are in the final list, occupying **eight rows**
(Houlsby ×2, LoRA ×2, AdapterHub, AdapterFusion, Petals, S-LoRA). Column totals (352, 123) do sum
correctly, so the error is in the **row-level allocation rule**, which the manuscript never states.

**Query.**
```python
# How is a final record assigned to a group when retrieved by multiple routes?
grp = [c for c in uni.columns if 'group' in c.lower()]
print(uni[grp].head(20))
# Cross-tab: group membership × in-final-123
uni['in_final'] = uni['paper_key'].isin(final['paper_key'])
print(uni.groupby(<group_col>)['in_final'].sum())
```

**Likely causes** (test each): records are assigned to *every* group that retrieved them, so counts
double-count; or "n final" means "records this group contributed to, by section coverage" rather
than "records originating in this group."

**Edit.** Add the allocation rule to the Table 3 caption in one sentence, and correct the row(s).
If a record can belong to multiple groups, say so and either report first-retrieval attribution or
label the column "records covered" and note that the column may exceed group size — but then the
column can no longer sum to 123 without explanation. Pick one and be explicit.

**Done when.** Table 3's caption states the rule, every row is consistent with Table 2, and the
totals still reconcile to 352 and 123.

---

### B3 — Figure A1 plots the wrong dataset ⛔ BLOCKING

**Symptom.** Figure A1 (p. 57) is captioned "Tier breakdown of the **464-paper** relevant corpus …
90, 141, 233" and sits directly under Table A2 giving those numbers. The chart plots bars of
**48 / 42 / 33** — the tier counts of the **123-record final list**. The legend
("Prevalidated / Backward / Forward / Seed") also implies a stacked breakdown that is not rendered.

**Fix.**
```python
enriched = pd.read_csv(<464-record enriched pool file>)
assert len(enriched) == 464, f"wrong dataframe: {len(enriched)} rows"
counts = enriched['tier'].value_counts().sort_index()
assert list(counts) == [90, 141, 233], counts
```
Regenerate the left panel from the 464 pool **with the stacked discovery-direction breakdown the
legend promises**, or drop the legend. Confirm what the right panel ("Citation Count Distribution by
Tier", medians 26 / 113 / 118) is computed over and state it in the caption.

**Alternative** (acceptable): recaption the existing figure as the final-list tiering and move it
beside §3.2 where 48/42/33 are introduced. Then Appendix A needs a *new* 464-pool figure or none.

**Done when.** The plotted values, the caption, and Table A2 agree, and the plotting script asserts
its input row count.

---

### B6 — No exclusion reasons for the 101 records dropped at eligibility ⛔ BLOCKING (PRISMA 16b)

**Symptom.** Figure 5's final transition: "224 in data extraction → 123 included / **101 excluded in
final QA**." The string "101" appears **nowhere else** in the manuscript. These records were read in
full; PRISMA 2020 Item 16b requires reasons at this stage.

**Query.**
```python
extracted = ext['paper_key'].unique()          # expect 224
included  = set(final['paper_key'])            # expect 123
excluded  = [k for k in extracted if k not in included]
print(len(excluded))                            # expect 101
# Look for any curation/decision/exclusion column
print([c for c in ext.columns])
sub = ext[ext['paper_key'].isin(excluded)]
for c in ['corpus','tier','contribution_type','peft_technique','distribution_mechanism','notes_raw']:
    if c in sub: print(c, sub[c].value_counts(dropna=False).head(15))
```

**Two outcomes:**
1. **A reason field exists** (even implicitly — e.g. `corpus == 'background'`, or the 34 manual
   top-up records which the text says contributed 0). Derive categories and counts. Note that 34 of
   the 101 are already accounted for: the entire manual Scopus/WoS top-up was excluded.
2. **No reason field exists.** Then **stop and tell the user.** The human must code them. Do not
   invent categories. A defensible fallback the user can execute: code the 101 against a short
   scheme — *out of scope on full reading / no adapter or PEFT component / duplicate or superseded
   version / insufficient methodological detail / manual cross-validation top-up, not retained* —
   and record it in a new `14_final_curation_reasons.csv`.

**Edit.** Add a new table in §3.1 (e.g. Table 4, renumbering downstream) giving category × count
summing to 101, add the category tallies to the Figure 5 exclusion box, and cross-reference from
§10.3.

**Done when.** 101 decomposes into named categories that sum to 101, in both the text and Figure 5.

---

### M7 — Table 4 "Public" column is undefined and internally contradictory

**Symptom.** The column is never defined in the caption or §3.3. Rows whose Dataset column names
GLUE, SuperGLUE, WMT or C4 are marked "No" (Expert Choice, DeepSpeed-MoE, Switch Transformers,
Ostapenko et al.). Under the alternative reading (code availability), S-LoRA, Punica and
DeepSpeed-MoE are marked "No" while having public repositories. **Either reading yields errors.**

This matters beyond Table 4: the same coding judgement underpins §3.4.1's headline finding
("only 20 of 48 Tier-1 papers (41.7%) release usable code").

**Fix.** Decide what the column encodes, define it in the caption, re-derive every value, and
publish the operational rule plus the check date. Then spot-check the Tier-1 `code_released == no`
set in `quality_appraisal_scored.csv` against the actual repositories. Report any corrections to the
41.7% figure to the user before editing §3.4.1.

---

### Minor data checks in this phase

- **11 vs 18 arXiv records.** §10.3/§A.3 say 11 of 123 are arXiv preprints without a peer-reviewed
  venue; §C.6 says 18 "retained an arXiv source" plus 4 unannotated. Determine whether these are
  different constructs (venue status vs. retrieval source). If so, add one clarifying sentence to
  §C.6. If not, correct.
- **Layer 1 title-screening outcome.** §A.4 says Layer 1 excluded pre-2021 records; Table A1 shows
  all 972 entering Layer 2. Either Layer 1 excluded zero (state it) or a count is missing.
- **Table 2 per-seed counts.** They sum to 972, not 1,150, because they are incremental
  post-deduplication counts. Verify against `log_retrieval_2026-04-21.json` and add one sentence to
  the caption saying so — currently it reads as an error.

---

## 7. Phase 2 — Mechanical and text fixes (no data needed)

Safe to do in one pass, but still one commit per group.

### B7 — Desk-check triggers ⛔ BLOCKING

1. **Missing `References` heading.** The bibliography starts mid-p.47 with no heading. Almost
   certainly the MDPI template's `\bibliography`/`thebibliography` block is being emitted without
   `\section*{References}` or `\reftitle{References}`. In the MDPI class the macro is typically
   `\reftitle{References}` immediately before the bibliography. Locate and restore. Verify in the
   compiled PDF, not just the source.
2. **Figures 8–14 never cited in text.** Confirmed: the strings "Figure 8" … "Figure 14" each occur
   exactly once, in their caption. Add `\ref{}` callouts at the point of first *discussion*
   (see F9):
   - Fig. 8 — PEFT taxonomy → §4.6/end of §4
   - Fig. 9 — AdapterFusion fusion layer → §5.3
   - Fig. 10 — PEFT serving paradigm → §6.1
   - Fig. 11 — Switch Transformer routing → §7.1
   - Fig. 12 — Gossip learning → §8.2
   - Fig. 13 — Petals → §8.4
   - Fig. 14 — Kademlia lookup → §8.6
   Also add callouts for Table A2, Figure A1, Figure A3, Table A5.
3. **Table 2 cited before Table 1.** §3.1: *"The full disposition of all nine seeds is given in
   Table 2, immediately following Table 1."* Reorder so Table 1 is cited first, e.g. "Table 1 lists
   the nine seeds and their role; Table 2 records the disposition of each."

### B5 — Truncated sentence in §10.3 ⛔ BLOCKING

p. 45 currently reads: *"Single-reviewer screening has been estimated elsewhere to miss on the order
of **5–13screening**."* The `%` sign, the clause ending, and the citation are all missing — likely a
lost `\%` and a dropped `\cite{}`. **Do not guess the figure.** Ask the user for the intended source
(single- vs dual-screening error-rate literature) and restore both the number and the citation. If
the user cannot supply it, delete the sentence rather than leave a fabricated statistic.

### Cross-reference errors

| Location | Says | Should say |
|---|---|---|
| Data Availability | quality-appraisal scores "reported in §3.3" | **§3.4** |
| Supplementary Materials | S2 "underlying §3.3" | **§3.4** |
| §C.4 | queries "documented in Appendix B" | **Appendix C** (B holds the Undermind prompts) |
| Appendix D subsections | `C.1`–`C.6` | `D.1`–`D.6` |

These are wrong *targets*, not wrong numbers (F8). Fix the `\label`/`\ref` pairs.

### Typography and consistency

- **§9.3** — "The seven dimensions as shown in **table 6**, were selected" → capitalise `Table~\ref{}`
  and remove the comma splice.
- **§9.3** — missing full stop after "discussed in Section 10.4".
- **§3.2** — duplicated sentence; the final-stage tier counts (48/42/33) are stated three times in
  five lines, twice near-verbatim. Keep one.
- **§A.7** — broken sentence: "of these, 190 (all KEEP-origin; …) and 197 were excluded" — missing
  verb. Rewrite: "…of these, 190 proceeded to data extraction (all KEEP-origin) and 197 were
  excluded."
- **Table 6** — the `†` footnote has no anchor in the table body. Attach it to the cell it explains
  (the Privacy/DP column of the combined reference profile row).
- **Acronyms** — `MoE` first appears in Table 3 (p. 11) and Table 4 (p. 13), pages before
  "Mixture-of-Experts" is expanded in §7. Expand at first use. **`MT-EF` is never expanded
  anywhere** — expand it at its first occurrence (Table 4 / §8.4 heading).
- **Voice** — "our"/"we" appears in the abstract ("To our knowledge"), §8.4 ("to the best of our
  knowledge") and §10.3 ("we treat this as…"). Convert to "the author" / "To the author's knowledge"
  — keeping the hedge (F7). Single-author paper; be consistent.
- **Register** — "chapter" appears 18× for what are Sections. Also §3.2: "No second independent human
  reviewer was available **for this thesis**" and "biasing the corpus toward **the thesis
  narrative**". Neutralise for a journal submission (targeted edits only — F6). Keep the *coursework
  lineage disclosure* itself (§3).
- **Title page** — no `* Correspondence:` line; the `*` is on the author name and the email sits only
  in the affiliation footnote. Add the correspondence line per the MDPI template.
- **Reference fixes** — ref 26 (Wohlin) has duplicated "Proceedings of the Proceedings of"; ref 19
  (LLaMA) has a stray bracketed `[2302.13971]`; ref 7 (Toppings) uses DOI prefix `10.5555/…` —
  verify it resolves, and if not, cite the USENIX ATC page without a DOI.
- **Table 1** — Petals' venue is given as "ACL 2023 / NeurIPS 2023", conflating the ACL System
  Demonstrations paper (which is reference [8]) with the separate NeurIPS 2023 paper on distributed
  inference over the Internet. Fix the venue field or cite both papers.
- **§3.1** — "Petals … has accumulated over 100 citations in three years" materially understates and
  will date badly. Drop the figure or verify and update.

---

## 8. Phase 3 — Statement and compliance fixes

### B4 — Data Availability contradicts itself ⛔ BLOCKING

Two problems in one statement:
1. `papers_code` is described as "**private**" and, four sentences later, as "**publicly available**
   at github.com/vanjaluk8/papers_code." Resolve.
2. It says the screening logs, `pipeline_unified.csv` and the extraction spreadsheet "are **not
   separately version-controlled**", while also claiming `verify_prisma_counts.py` and
   `verify_quality_appraisal.py` "recompute every PRISMA-stage count … **directly from the underlying
   pipeline files**." Scripts whose inputs are not archived cannot be run by anyone else.

**Fix.** Deposit the pipeline CSV/JSON artefacts in a citable archive (**Zenodo or OSF with a DOI**
— preferable to GitHub for citability and permanence). They are modest in size and contain no
personal data. Then rewrite the statement so that: the public/private status of each repo is
unambiguous; the archived dataset has a DOI; and the verification scripts' inputs are named and
reachable.

This single fix converts the paper's biggest liability — unverifiable single-reviewer screening —
into a manageable one, because a sceptical reader could re-derive the decisions.

### Conflicts of Interest

Two G0 seeds are by an author at the same faculty (Šajina et al., FGCS 2024) and one is a University
of Rijeka doctoral thesis (Šajina 2025, repository object `infri:1394`); Šajina is cited three times
([9], [15], [106]) and MT-EF/Šajina is scored as a row in the concept matrix. Add one line:

> "The author is affiliated with the same faculty as the authors of [9,15,106]; these works were
> identified through the standard search protocol and appraised under the same criteria."

### GenAI disclosure

Already good and located correctly in Materials and Methods. Two additions:
- **Name the screening classifier model and version in the manuscript**, not only in the audit log.
  A reader assessing screening reliability needs to know whether the Layer-3 and abstract-review
  advisory notes came from the same model family as the drafting assistant.
- Consider mirroring a one-sentence statement in **Acknowledgments** (currently "Not applicable") in
  MDPI's recommended form: *"During the preparation of this manuscript, the author used [tool,
  version] for [purpose]. The author has reviewed and edited the output and takes full
  responsibility for the content of the publication."*

### Protocol registration

The §3 justification ("no suitable AI-specific registry was available") is inaccurate — **OSF
Registries, INPLASY and protocols.io all accept CS/AI review protocols**, and OSF is now routine for
software-engineering SLRs. Either register retrospectively with a clear timestamp note, or restate
honestly: "the protocol was not prospectively registered; OSF Registries and protocols.io would have
been available, and this is a limitation."

### Terminology consistency around automation

Figure 5 says "60 LLM triage"; Table A6 calls Layer 3 "LLM triage"; §A.4 says the author "reviewed
all 130 records individually" with the classifier providing "preliminary sorting suggestions." The
labels imply automation, the prose implies human adjudication. **Pick one description and use it in
all three places** — this matters because the AI-use disclosure depends on it.

### Cover letter (draft for the user, do not submit)

Must state: (a) the manuscript derives from unpublished doctoral coursework/thesis material and is
not published elsewhere; (b) **whether the doctoral thesis containing this material has been or will
be publicly deposited, and when**. A publicly deposited thesis chapter is the most common cause of an
unexpected iThenticate score in exactly this situation. Also flag the verbatim Scopus/WoS query
strings and Undermind prompts in the appendices as expected similarity sources.

---

## 9. Phase 4 — Substantive additions (largest effort; do last)

These change the paper's standing as a review. Each needs user sign-off before drafting.

### M1 — Survey-of-surveys search + comparison table (highest value)

§3.1 currently concedes: *"No search was dedicated specifically to locating competing systematic
reviews or umbrella surveys of this exact scope."* For a Review article this is a hole in the middle
of the contribution.

Run and document:
```
("survey" OR "systematic review" OR "literature review")
AND (PEFT OR LoRA OR adapter OR "mixture-of-experts" OR "federated LLM"
     OR "parameter-efficient fine-tuning")
```
2021–2026, across Scopus, WoS, **ACM DL, IEEE Xplore**, arXiv. Add the queries to Appendix C and the
execution to Table A6.

Then add a **Comparison with related surveys** table (10–15 rows): survey · year · venue · scope ·
#papers · PEFT? · composition? · serving? · MoE? · P2P/FL? · gap-analysis method · what this review
adds. **Rows come only from the search, with DOIs (F4).**

### M2 — Promote §3.4.1 to the primary quality instrument

§3.4's all-corpus rubric is largely bibliographic: Q2 (presence of a DOI/arXiv ID) measures retrieval
bookkeeping, not quality; Q1 and Q6 are prestige/relevance proxies. §3.4.1 — artifact availability,
baseline adequacy, threats reporting, hand-coded yes/partial/no — *is* a risk-of-bias appraisal, but
covers only the 48 Tier-1 records.

Extend those three dimensions to all 123 records (or at minimum every record cited as evidence in
§§4–9), report risk of bias as the primary appraisal, and demote Q1–Q6 to a corpus-description
instrument. Also: **drop Q5 or report its coverage failure honestly** — it is scored on 16 of 123
records and all 16 score the maximum, which is uninformative.

Then fix the abstract: "a six-dimension rubric" applied to "each study" is inaccurate on both halves
(the total is Q1–Q4+Q6, and the sixth applies to 16 records).

### M3 — Add a screening calibration measure

The disclosure is exemplary; the remedy is absent. Cheapest defensible option: a **blinded intra-rater
re-screen of a random 10% sample after a washout interval**, reporting agreement. Alternatives: a
documented pilot-calibration round on ~50 records with criteria refinement; or a colleague screening
a 5–10% sample. Add whichever the user can actually execute — **do not report one that was not
performed.**

### M4 — Database coverage

Add ACM Digital Library, IEEE Xplore and DBLP passes, or justify their omission explicitly. Given the
corpus is dominated by MLSys/USENIX/NeurIPS/ICML/ACL, the absence of ACM DL and IEEE Xplore is
material. Separately, **rewrite §C.4's conclusion**: "zero new candidates from the WoS manual search"
supports a claim about *database overlap*, not about *coverage completeness*.

### M5 — Bound the concept-matrix claim

Table 6 scores **17 systems**. §10.2 claims "**none of the 123 reviewed records** simultaneously
satisfies all seven design dimensions" and the abstract makes the same move. A 17-row matrix cannot
support a 123-record claim. Either:
- score all 123 (or all 48 Tier-1) on the seven dimensions and report the distribution; or
- restate as: "none of the 17 systems in Table 6, selected as the most complete representatives of
  each pillar."

Also: **state the row-selection rule for Table 6**, and flag that MT-EF/Šajina [9] is *not* in the
123-record corpus (Table 2 records it as background/motivation only) yet is scored as a row.

### M6 — Per-pillar comparison tables

§§4–8 contain **zero comparison tables** across ~30 pages reviewing five literatures. Add one per
pillar. Example for §6: system · adapter residency · memory strategy · batching kernel · reported
speedup · **what exactly is centralised**. This converts five catalogues into five syntheses and
lets you cut ~3,000–4,000 words of prose (F10 — compress, don't delete coverage).

### M8, M9, and Figure 15

- **M8** — one-wave snowballing with no formal stopping criterion is a deviation from the cited
  Wohlin protocol. Name it in §3, not only in §10.3.
- **M9** — Table 7's "Evidence" column reads "G0–G6", "G3, G4". Replace group labels with **reference
  numbers** so each negative claim is checkable.
- **Figure 15** — the "Empirical Gaps" quadrant sits bottom-**left**, on an axis whose left side is
  defined as "calls for new theory". Rename the quadrant (e.g. "Theoretical/Analytical Gaps") or
  move it.
- **§3.3 placement** — Table 4 is extraction *output*, not method. Move it to §4 or an appendix, or
  reframe §3.3 as "extraction targets".

---

## 10. Verification harness

Save as `tools/check_manuscript.py`. Run after every phase.

```python
#!/usr/bin/env python3
"""Structural checks for the SLR manuscript. Usage: python3 tools/check_manuscript.py main.pdf"""
import re, subprocess, sys, collections

def text(pdf):
    return subprocess.run(['pdftotext', '-layout', pdf, '-'],
                          capture_output=True, text=True, check=True).stdout

def check_float_citations(t):
    """Every Figure/Table must be referenced somewhere other than its own caption."""
    bad = []
    lines = t.split('\n')
    caption_of = collections.defaultdict(list)
    ref_of = collections.defaultdict(list)
    for i, ln in enumerate(lines):
        s = ln.strip()
        cap = re.match(r'^(Figure|Table)\s+(A?\d+)\.', s)
        for m in re.finditer(r'\b(Figure|Table)s?\s+(A?\d+)', s):
            key = f"{m.group(1)} {m.group(2)}"
            if cap and cap.group(0).startswith(key):
                caption_of[key].append(i)
            else:
                ref_of[key].append(i)
    for key in sorted(caption_of, key=lambda k: (k.split()[0], k.split()[1])):
        if not ref_of[key]:
            bad.append(f"UNCITED: {key} appears only as a caption")
    # first-citation ordering, per kind
    for kind in ('Figure', 'Table'):
        firsts = [(min(ref_of[k]), k) for k in ref_of if k.startswith(kind)
                  and not k.split()[1].startswith('A')]
        order = [k for _, k in sorted(firsts)]
        nums = [int(k.split()[1]) for k in order]
        if nums != sorted(nums):
            bad.append(f"OUT OF ORDER ({kind}): first citations run {order}")
    return bad

def check_headings(t):
    bad = []
    if not re.search(r'^\s*References\s*$', t, re.M):
        bad.append("MISSING: 'References' heading")
    for h in ['Author Contributions', 'Funding', 'Data Availability',
              'Conflicts of Interest', 'Acknowledgments']:
        if h not in t:
            bad.append(f"MISSING: '{h}' statement")
    return bad

def check_prisma(t):
    """Recompute the funnel from the numbers the manuscript states."""
    bad, chain = [], [
        ("identified - duplicates = screened", 1150 - 178, 972),
        ("title outcomes sum to screened",      162 + 791 + 19, 972),
        ("merge minus cross-dupes",             162 + 352 - 12, 502),
        ("enrichment",                          502 - 38, 464),
        ("abstract pool",                       464 + 88, 552),
        ("abstract outcomes",                   214 + 173 + 165, 552),
        ("full-text queue",                     214 + 173, 387),
        ("queue exclusions",                    24 + 173, 197),
        ("extraction",                          190 + 34, 224),
        ("final",                               224 - 101, 123),
        ("tiers of final list",                 48 + 42 + 33, 123),
        ("tiers of enriched pool",              90 + 141 + 233, 464),
        ("quality bands",                       13 + 61 + 47 + 2, 123),
    ]
    for label, got, want in chain:
        if got != want:
            bad.append(f"ARITHMETIC: {label}: {got} != {want}")
    if '101' not in re.sub(r'\s+', ' ', t).replace('10.1', ''):
        bad.append("PRISMA 16b: no discussion of the 101 eligibility-stage exclusions")
    return bad

def check_prose(t):
    bad = []
    if re.search(r'5[–-]13screening', t):
        bad.append("BROKEN SENTENCE: '5-13screening' in Threats to Validity (B5)")
    n = len(re.findall(r'\bchapters?\b', t, re.I))
    if n:
        bad.append(f"REGISTER: 'chapter' appears {n}x — should be 'Section'")
    for pat, why in [(r'\bfor this thesis\b', 'thesis register'),
                     (r'\bthe thesis narrative\b', 'thesis register'),
                     (r'\bwe treat this\b', 'first person'),
                     (r'\bto our knowledge\b', 'first person'),
                     (r'\bto the best of our knowledge\b', 'first person')]:
        if re.search(pat, t, re.I):
            bad.append(f"VOICE/{why}: {pat}")
    if re.search(r'Proceedings of the Proceedings of', t):
        bad.append("REF 26: duplicated 'Proceedings of the'")
    if 'MT-EF' in t and not re.search(r'Multi-?Task.{0,40}MT-?EF|MT-?EF\s*\(', t):
        bad.append("ACRONYM: MT-EF never expanded")
    moe = t.find('MoE'); full = t.lower().find('mixture-of-experts')
    if 0 <= moe < full:
        bad.append("ACRONYM: 'MoE' used before 'Mixture-of-Experts' is expanded")
    return bad

def check_crossrefs(t):
    bad = []
    if re.search(r'quality[- ]appraisal[^.]{0,80}§?\s*3\.3', t, re.I):
        bad.append("XREF: quality appraisal cited as §3.3 (is §3.4)")
    if re.search(r'documented in Appendix B', t):
        bad.append("XREF: Scopus/WoS queries cited as Appendix B (are Appendix C)")
    if re.search(r'^\s*C\.\d', t, re.M) and 'Appendix D' in t:
        bad.append("XREF: Appendix D subsections numbered C.x")
    if '??' in t:
        bad.append("LATEX: unresolved reference '??' in output")
    return bad

if __name__ == '__main__':
    t = text(sys.argv[1])
    issues = (check_headings(t) + check_float_citations(t) + check_prisma(t)
              + check_crossrefs(t) + check_prose(t))
    for i in issues:
        print(i)
    print(f"\n{len(issues)} issue(s).")
    sys.exit(1 if issues else 0)
```

**Baseline expectation on the current PDF:** ~20 issues, dominated by seven uncited figures, the
missing References heading, the broken sentence, and the register/voice flags. The arithmetic block
should pass — the funnel already reconciles; the failures are attribution and reasons, which no
script can catch. **A green run does not mean Phase 1 is done.**

---

## 11. Issue register

Copy into the repo as `TODO.md` and tick as you go.

### Blocking
- [ ] **B1** §3.2 / §3.1 / §C.3 / Table A6 — 53-record provenance contradicted by 12-KEEP branch
- [ ] **B2** Table 3 — G0: 18 final records from a 9-paper group; no allocation rule stated
- [ ] **B3** Figure A1 — plots 48/42/33 under a caption claiming 90/141/233
- [ ] **B4** Data Availability — `papers_code` both private and public; verification inputs not archived
- [ ] **B5** §10.3 — truncated sentence "5–13screening", missing `%` and citation
- [ ] **B6** Figure 5 — 101 eligibility-stage exclusions with no reasons (PRISMA 16b)
- [ ] **B7** Missing References heading; Figures 8–14 uncited; Table 2 cited before Table 1

### Major
- [ ] **M1** No search for competing surveys; add search + comparison table
- [ ] **M2** All-corpus rubric is not a risk-of-bias appraisal; promote §3.4.1
- [ ] **M3** Single-reviewer screening with no calibration; add intra-rater re-screen
- [ ] **M4** No ACM DL / IEEE Xplore / DBLP; §C.4 over-claims coverage from a null result
- [ ] **M5** 17-row concept matrix used to support a 123-record claim; non-corpus row included
- [ ] **M6** No comparison tables in §§4–8; add one per pillar
- [ ] **M7** Table 4 "Public" column undefined and contradictory; affects §3.4.1 statistic
- [ ] **M8** One-wave snowballing deviation not named in §3
- [ ] **M9** Table 7 evidence at group granularity, not paper granularity
- [ ] **M10** Protocol-registration justification inaccurate (OSF/INPLASY/protocols.io exist)
- [ ] **M11** Same-faculty relationship to [9,15,106] not disclosed in CoI

### Minor
- [ ] 11 vs 18 arXiv records unreconciled
- [ ] Fig. 5 (165) vs Table A5 (338) — add reconciling pointer
- [ ] Table 2 per-seed counts sum to 972 — say they are incremental post-dedup
- [ ] §3.2 duplicated tiering sentence
- [ ] §A.7 broken sentence (missing verb)
- [ ] Layer 1 title-screening outcome unreported
- [ ] "LLM triage" vs "author reviewed individually" — inconsistent
- [ ] Four cross-reference errors (§3.3→§3.4 ×2, App. B→C, App. D subsections C.x)
- [ ] Table 6 `†` footnote has no anchor
- [ ] MoE used before expansion; MT-EF never expanded
- [ ] First person inconsistent (abstract, §8.4, §10.3)
- [ ] "Chapter" ×18; "for this thesis"; "the thesis narrative"
- [ ] §9.3 lowercase "table 6" + comma splice; missing full stop after "Section 10.4"
- [ ] Ref 26 duplicated words; ref 19 stray `[2302.13971]`; ref 7 DOI `10.5555/` unverified
- [ ] Table 1 conflates Petals ACL 2023 / NeurIPS 2023
- [ ] Petals citation count understated and will date
- [ ] Fig. 15 "Empirical Gaps" on the theoretical axis
- [ ] No `* Correspondence:` line
- [ ] §3.3 (Table 4) is extraction output placed in Methods
- [ ] Verify Houlsby SciTail 91.1; Prefix-tuning XSUM ROUGE-L 34.9; Crowdsourced MoE datasets
- [ ] Name the screening classifier model/version in the manuscript
- [ ] Mirror GenAI disclosure in Acknowledgments

---

## 12. Stop and ask the user

Do not proceed on your own judgement in these cases:

1. **Any pipeline data file is missing or ambiguous.** Most of Phase 1 depends on them.
2. **B1 resolves to "the 53 is wrong"** rather than "the attribution is wrong." Changing a corpus
   count is the user's call, not yours.
3. **B6 finds no reason field.** The 101 must be coded by a human.
4. **B5** — the intended source for the 5–13% figure.
5. **M7** — if re-deriving the artifact coding would change the 41.7% headline statistic.
6. **M3** — which calibration measure the user can actually perform. Never report an unperformed one.
7. **Any edit that would remove or weaken §3 content.**
8. **Anything requiring a factual claim you cannot source from the repo.**

---

## 13. Suggested session shape

```
Session 1  Phase 0 discovery + baseline check + file inventory report
Session 2  B1, B2 (queries first, findings reported, then edits)
Session 3  B3, B6, M7 (figure regen + exclusion reasons + coding rule)
Session 4  Phase 2 in full (B5, B7, cross-refs, typography, acronyms, voice, register)
Session 5  Phase 3 (B4 + Zenodo/OSF deposit, CoI, GenAI, protocol, cover letter draft)
Session 6+ Phase 4, one major item per session, user sign-off before drafting each
Final      Full rebuild, check_manuscript.py green, response-to-reviewers letter
```

**Response-to-reviewers letter:** maintain it incrementally in `RESPONSE.md` as you go — one entry
per issue ID with what changed and where. Writing it at the end from memory produces vague entries
that reviewers dislike.

---

## 14. What "done" looks like

- `check_manuscript.py` exits 0.
- Every count in the manuscript is reproducible by running the verification scripts against archived,
  DOI-citable pipeline files.
- The 101 eligibility-stage exclusions decompose into named categories summing to 101.
- One consistent cohort vocabulary across §3.1, §3.2, §C.3, Table A6, and Figure 5.
- A survey-comparison table exists and every row has a DOI.
- Risk of bias is reported for the evidence base, not just for 48 Tier-1 records.
- Every claim of the form "no reviewed work does X" is bounded to a stated population and points at
  reference numbers.
- Every protected passage in §3 is still there.
