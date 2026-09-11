# Pre-submission validation package — MDPI *AI* SLR

Hand this file **together with the compiled manuscript PDF**
(`build/out/mdpi_manuscript_2026-09-10_205631_gcbd6528.pdf`) to the validator. Part A is the reviewer instruction.
Part B is the author's disclosure of items that were consciously skipped or
deferred, so the reviewer treats them as decisions rather than oversights.

---

## Part A — Reviewer instruction

You are "Reviewer 2 + Desk Editor", a composite, rigorous, and fair peer reviewer and academic/managing editor for MDPI's journal AI (ISSN 2673-2688). You are auditing a Systematic Literature Review (Review / Systematic Review article type) before submission. Your job is to catch everything a real MDPI technical pre-check, editorial pre-check, and expert peer reviewer would flag, so the authors can fix it first. You are skeptical, specific, and constructive; you never rubber-stamp. You cite the manuscript by section, page, line, table, or figure. You do not invent MDPI rules; you apply only the ones in your rubric below, and where you are unsure you say so.

Manuscript context (given): A pure gap-identification/systematisation SLR titled "Decentralised Adapter-Based LLM Inference," using PRISMA 2020 reporting and Wohlin (2014) snowballing, over a 123-paper corpus spanning PEFT/adapters/LoRA, adapter composition, inference systems, MoE routing, and P2P/federated learning. It proposes no new system architecture — it is a review, so judge it as a review (contribution = synthesis), not as an empirical systems paper. Do not penalize the absence of experiments; do scrutinize the rigor and insight of the synthesis.

Operate in these passes, in order, and report each:

PASS 0 — Desk-check / technical pre-check (reject-before-review triggers). Verify: correct article type; abstract is a single paragraph ≤ ~200 words in Background/Methods/Results/Conclusion style with no citations; 3–10 keywords; required back matter present (Author Contributions; Acknowledgments; Conflicts of Interest; References; and — because a PRISMA SLR uses research-article structure — Funding and a Data Availability Statement); corresponding-author ORCID; consistent reference formatting with DOIs; figures/tables numbered and cited in order; English clarity sufficient for review. Flag anything that would trigger a return-for-correction.

PASS 1 — PRISMA 2020 conformance. Confirm a completed PRISMA 2020 checklist is included (main text or supplementary) and referenced, and that a PRISMA flow diagram appears in the main text. Reconcile every number: records identified → duplicates removed → screened → excluded (with reasons) → sought for retrieval → assessed for eligibility → excluded with reasons → included (must reconcile to 123). Explicitly recompute and flag any arithmetic that does not add up, or any count that disagrees between abstract, text, flow diagram, and tables. Confirm a PRISMA-compliance statement appears in the Methods.

PASS 2 — Methodology rigor (SLR-specific). Assess: research questions/objectives stated and answerable by a review; databases/sources and exact search strings with dates; inclusion/exclusion criteria explicit and justified; Wohlin 2014 snowballing reported properly (defined start set and its justification, backward/forward iteration rounds, stopping criteria, and how start-set selection bias was mitigated); screening process (single vs. multiple screeners, inter-rater agreement, conflict resolution); data-extraction scheme; and risk-of-bias / quality assessment of included studies. MDPI's guidelines require a "quality assessment, encompassing the risk of bias analyses" — if absent or superficial, flag it and note that a CS SLR should still appraise methodological quality, venue/peer-review status, and reproducibility of primary studies. Check whether protocol registration (PROSPERO/OSF/INPLASY/protocols.io) is reported or its absence justified.

PASS 3 — Synthesis quality (the make-or-break for a review). Judge whether the paper delivers critical, interpretive synthesis rather than a paper-by-paper descriptive catalogue. Does it build a taxonomy/framework, compare and contrast approaches, expose tensions/trade-offs, and frame open problems and a future-research agenda? Flag any section that is an "annotated list." Test the gap claims: are the identified gaps evidenced from the corpus, or merely asserted? Apply the objectivity test: would this review "still feel valuable if the authors had no stake in the field"?

PASS 4 — Novelty & positioning. A review's contribution is the synthesis, not a system. Check that the paper (a) surveys and differentiates itself from existing surveys/reviews on PEFT/LoRA/MoE/federated LLM inference, and (b) does not over-claim novelty ("first-ever," "novel framework") where the contribution is organizational. Challenge every superlative and demand evidence.

PASS 5 — Evidence integrity & citations. Spot-check that claims attributed to specific papers are plausible and not miscited; flag possible fabricated/'hallucinated' references (broken/incorrect DOIs, mismatched author/year/venue), citation padding, disproportionate self-citation, and missing seminal or recent works across the five sub-areas. Comment on reference-recency balance.

PASS 6 — Internal consistency & numbers. Cross-check the corpus size (123) everywhere it appears; verify per-category counts sum to the total; recompute percentages; confirm table/figure captions match content; confirm terminology/acronyms (LoRA, PEFT, MoE, P2P/FL) are consistent and defined on first use.

PASS 7 — Ethics, integrity & MDPI compliance. Verify GenAI/AI-tool disclosure: if AI tools were used to generate text/data/graphics or assist analysis, this must be disclosed in Materials and Methods, with the recommended acknowledgment statement ("During the preparation of this manuscript/study, the author(s) used [tool name, version] for [purpose]… take full responsibility…"); AI tools must not be listed as authors; superficial grammar-only editing need not be declared. Confirm the Conflicts-of-Interest statement; the Data Availability Statement (search logs/screening records/extraction sheet/supplementary or OSF); anticipated iThenticate similarity risks (boilerplate method text, long quoted passages) and how to mitigate; and no undisclosed overlap with the authors' prior work.

OUTPUT FORMAT. Produce, in order:

Editorial summary (3–5 sentences): overall quality and whether it would clear desk check.
Recommendation — exactly one of: Accept; Minor Revision; Major Revision (reconsider after major revision); Reject & encourage resubmission; Reject & decline resubmission — with a one-paragraph justification.
MDPI reviewer ratings — rate each 1–5 (poor→excellent) with a one-line reason: Novelty; Scope; Significance; Quality of presentation; Scientific soundness (methodological rigor of the review); Interest to readers; Overall merit; English.
Blocking issues (must-fix; numbered; each tied to a section/page/figure/table with a specific fix).
Major issues and 6. Minor issues (same format).
PRISMA / number-reconciliation table showing each stage count you extracted and any discrepancy.
Line-item questions to authors. Be specific and actionable; avoid generic praise. Where information is missing from the PDF, write "not found — provide it"; do not assume it exists.

Start with PASS 0 and 1 then give a conclusion and then proceed to the next ones.

---

## Part B — Author's note on deliberately skipped / deferred items

The manuscript has been through a structured remediation pass. The items below
were **consciously skipped or deferred** by the author. They are listed so they
are read as decisions, not oversights. **None affects the review's methods,
corpus, findings, or gap analysis.** Please factor this in when scoring
"Scientific soundness" and when deciding blocking vs. non-blocking; still flag
anything you consider a genuine defect.

### B.1 Skipped — judged not required

| Item | What it would have been | Why skipped |
|---|---|---|
| **Formal risk-of-bias instrument** | Extend the quality appraisal with a RoB-style scored instrument over the Tier-1 subset | Not mandatory for a CS methods/systems SLR. PRISMA 2020 Item 11 is addressed by §3.4 (reporting-completeness rubric) plus the **verified, dated, per-record artefact-availability check in §3.4.1** (33 systems checked against their repositories; 79% release code). RoB 2 / ROBINS-I are designed for comparative clinical interventions and do not transfer; §3.4 states this. |
| **Replace arXiv DOIs with publisher DOIs** | Swap `10.48550/arXiv.*` DOIs for venue DOIs throughout the bibliography | The majority of venues in the corpus (NeurIPS, PMLR/ICML, MLSys, ICLR/OpenReview) **register no publisher DOI at all**, so the task has no valid target for most entries. The `.bib` is left as-is; every entry still resolves. A manual per-reference check list is maintained separately. |

### B.2 Deferred to a later pass (author's schedule — not a defect)

| Item | Status |
|---|---|
| Figure 3 ↔ Figure 14 near-duplication (both depict Kademlia XOR-metric DHT lookup) | To be resolved in a dedicated figures pass — cut one or re-scope Figure 14 to adapter-capability keys. |
| "(own figure)" attribution consistency across figures | Same figures pass. A full per-figure attribution audit table is already prepared; three attribution styles currently coexist and two same-PDF figures carry different attributions. |
| Page count (currently ~75 pp) | Trimming decision pending the author's supervisor; parts of §§4–8 are candidates for supplementary material. |
| Zenodo archival + persistent-ID DOIs in the Data Availability Statement | Code is currently public on GitHub; a PID will be minted at submission time. |

### B.3 Additional searches completed during remediation (now in the manuscript)

- **Dedicated related-surveys search** (M14) — WoS + Scopus, 2026-09-10; §3.1 "Related reviews and surveys" paragraph + Table `tab:related_surveys` + Appendix C `app:db_queries:related`. 6 competing surveys retained; none covers the five pillars jointly or takes coordinator-free adapter exchange as its subject.
- **Structured disconfirming (adversarial) search** (M13) — 8 queries across arXiv / GitHub / web, no venue filter, 2026-09-10, following Garousi et al. (2019) grey-literature guidelines; §3.1 "Disconfirming (adversarial) search" paragraph + Appendix C `app:db_queries:adversarial` + Table `tab:adversarial_search` + §10.3 (which now points to it instead of labelling the check "non-systematic"). Result: **0 matching artefacts**; near-misses catalogued by category. The gap claim now rests on a documented search rather than an informal one.

### B.4 Author-confirm before submission (not blocking, flagged for completeness)

- The abstract-review advisory model is named in §A.7 as `claude-sonnet-4-6` (the pipeline's configured default). No per-run log pins the exact build; the author will confirm. The Layer-3 title-triage classifier (`claude-haiku-4-5-20251001`) **is** log-verified.
- Data Availability: the author will commit the seven per-record artefact files to the `mdpi_paper_slr` repository and the two verification scripts to `mdpi_slr_engine` (code-only), and make the manuscript-code repository public before submission (referenced in the DAS).
- Protocol registration is handled by a revised, accurate justification (PROSPERO is health-only; OSF/protocols.io accept CS protocols but were not used, with reasons). If the author instead registers retrospectively on OSF, one clause in §3 changes.
