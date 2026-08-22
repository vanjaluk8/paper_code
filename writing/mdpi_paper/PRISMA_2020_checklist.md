# PRISMA 2020 Checklist

**Manuscript:** *Decentralised Adapter-Based LLM Inference: A Systematic Literature Review—Mapping the Research Gap at the Intersection of PEFT, P2P Systems, and Multi-Task Serving*
**Journal target:** MDPI — *AI*
**Reporting guideline:** PRISMA 2020 (Page et al., 2021, *BMJ* 372:n71)
**Completed:** 21.08.2026.

This checklist maps each of the 27 PRISMA 2020 items to the section, table, figure, or appendix subsection of the manuscript where it is reported. All funnel counts follow the **single authoritative funnel table in `PRISMA_NUMBERS_VALIDATION.md`** (the reconciled, CSV-verified master table) and are traceable record-by-record (Appendix A, `sec:appendix:corpus_pipeline`).

---

## Section and Topic | Item | Checklist item | Location where item is reported

### TITLE

| Section | # | Checklist item | Where the item is reported |
|---|---|---|---|
| **Title** | 1 | Identify the report as a systematic review. | Title page ("...A Systematic Literature Review of..."); §1 Introduction (`sec:introduction`) |

### ABSTRACT

| Section | # | Checklist item | Where the item is reported |
|---|---|---|---|
| **Abstract** | 2 | See the PRISMA 2020 for Abstracts checklist. | Abstract (structured, includes background, methods, results, conclusions) |

### INTRODUCTION

| Section | # | Checklist item | Where the item is reported |
|---|---|---|---|
| **Rationale** | 3 | Describe the rationale for the review in the context of existing knowledge. | §1 Introduction (`sec:introduction`) |
| **Objectives** | 4 | Provide an explicit statement of the objective(s) or question(s) the review addresses. | §1.1 Review Structure; §9 Synthesis (`sec:synthesis_gap`) — research questions answered in §9.1 |

### METHODS

| Section | # | Checklist item | Where the item is reported |
|---|---|---|---|
| **Eligibility criteria** | 5 | Specify the inclusion and exclusion criteria for the review and how studies were grouped for the syntheses. | §3.1 Search Strategy and Corpus (`sec:methodology:search`); §3 Materials and Methods (`sec:methodology`); **Appendix A.3** (Inclusion and Exclusion Criteria); Table C.1 |
| **Information sources** | 6 | Specify all databases, registers, websites, organisations, reference lists, and other sources searched or consulted to identify studies. Specify the date when each source was last searched or consulted. | §3.1 (`sec:methodology:search`); **Appendix A.2** (Citation Snowballing) and **Appendix C.2** (search date 2026-04-21); databases: Semantic Scholar API, Scopus, Web of Science, IEEE Xplore, ACL Anthology (see `PRISMA_summary_2026-04-21.md`, §Stage 1) |
| **Search strategy** | 7 | Present the full search strategies for all databases, registers, and websites, including any filters and limits used. | **Appendix B** (Manual Database Search Queries — full Scopus and WoS query strings); **Appendix C.3** (Forward citation snowballing) |
| **Selection process** | 8 | Specify the methods used to decide whether a study met the inclusion criteria of the review, including how many reviewers screened each record and each report retrieved, whether they worked independently, and, if applicable, details of automation tools used. | §3.1 (`sec:methodology:search`); **Appendix A.4** (Screening Procedure — two-layer title screening, LLM triage, abstract review); **Appendix A.7** (Abstract-Level Review). Single-reviewer screening with AI in strictly advisory capacity (§3.1); all decisions author-made. Reliability: an automated calibration re-screen of a 10% sample (n=55) yielded 58.2% agreement / Cohen's κ=0.17 (slight), disclosed as a limitation (§11.3), not as independent human validation |
| **Data collection process** | 9 | Specify the methods used to collect data from reports, including how many reviewers collected data from each report, whether they worked independently, any processes for obtaining or confirming data from study investigators, and, if applicable, details of automation tools used. | §3.1 (`sec:methodology:search`); **Appendix A.5** (Enrichment and Tier Classification); extraction spreadsheet `11_data_extraction_2026-05-12.csv` (224 rows) |
| **Data items** | 10a | List and define all outcomes for which data were sought. Specify whether all results compatible with each outcome domain in each study were sought, and, in the long run, how any missing information was handled. | The manuscript is a thematic synthesis; outcome = study contribution categories (§4–§8); **Appendix A.6** (Bibliometric Overview) |
| | 10b | List and define all other variables for which data were sought (e.g., participant/intervention characteristics, funding sources). Describe any assumptions made about any missing or unclear information. | Extraction schema (tier, PEFT technique, distribution mechanism, contribution codes) — see extraction spreadsheet columns and §3; **Appendix A.5** |
| **Study risk-of-bias assessment** | 11 | Specify the methods used to assess risk of bias in the included studies, including details of the tool(s) used, how many reviewers assessed each study, and whether they worked independently. | **§3.3 Quality Assessment (`sec:methodology:quality`)** — six-dimension rubric (publication & venue quality, record resolvability, methods specificity, evaluation-claim specificity, contribution clarity, synthesis relevance), each scored 0–2 from a grounded pipeline field (`tab:quality_rubric`). Single-reviewer appraisal with LLM in strictly advisory capacity (§3.1). SLR-specific adaptation (no comparative participant-level intervention, so clinical risk-of-bias instruments do not apply directly) |
| **Effect measures** | 12 | Specify, for each outcome, the effect measure(s) used in the synthesis or presentation of results. | Not applicable — qualitative/thematic synthesis; no pooled quantitative effect measures |
| **Synthesis methods** | 13a | Describe the processes used to decide which studies were eligible for each synthesis. | §3.1 (`sec:methodology:search`); **Appendix A.5** (Enrichment and Tier Classification); tier breakdown (Tab. 48 / 42 / 33) |
| | 13b | Describe any methods required to prepare the data for presentation or synthesis, such as handling of missing summary statistics or data conversions. | Extraction + harmonisation across sources (arXiv/Scopus/WoS duplicates reconciled); §3 |
| | 13c | Describe any methods used to tabulate or visually display results of individual studies and syntheses. | Figures and tables throughout (§4–§9); bibliometric figures Fig. venues / bibliometric; tier figures |
| | 13d | Describe any methods used to synthesise results and provide a rationale for the choice(s). If meta-analysis was performed, describe the model, methods to identify statistical heterogeneity and methods of handling heterogeneity. | Narrative thematic synthesis (§9); no meta-analysis performed |
| | 13e | Describe any methods used to explore possible causes of heterogeneity among study results. | Not applicable (no meta-analysis); heterogeneity handled thematically across five bodies of literature (§9) |
| | 13f | Describe any sensitivity analyses conducted to assess robustness of the synthesised results. | Funnel cross-validation and per-stage reconciliation (`PRISMA_NUMBERS_VALIDATION.md`); §3.1 |
| **Reporting bias assessment** | 14 | Describe any methods used to assess risk of bias due to missing results in a synthesis. | Citation-snowballing + Scopus/WoS forward pass reduces missing-result risk (**Appendix C.3**, **C.4** manual cross-validation); stated in §3.1 |
| **Certainty assessment** | 15 | Describe any methods used to assess certainty (or confidence) in the body of evidence for an outcome. | Not applicable — qualitative synthesis; quality/venue assessment at full-text stage substitutes for GRADE-style certainty |

### RESULTS

| Section | # | Checklist item | Where the item is reported |
|---|---|---|---|
| **Study selection** | 16a | Describe the results of the search and selection process, from the number of records identified in the search to the number of studies included in the review, ideally using a flow diagram. | **Figure 5 (PRISMA flow diagram, `fig:prisma`)** — 1,150 raw → 972 dedup → 502 merged → 464 enriched → 552 abstract-reviewed → 387 full-text queue → 224 extraction → 123 final (121 distinct). Table C.1; `PRISMA_summary_2026-04-21.md` |
| | 16b | Cite studies that might appear to have met the inclusion criteria, but which were excluded, and explain why they were excluded. | **Appendix A.4** (two-layer screening exclusion reasons: year 192, no-keyword 284, LLM-only 255 = 731); abstract-review SKIP 338 with reasons (Appendix A.7) |
| **Study characteristics** | 17 | Cite each included study and present its characteristics. | Final reading list (123 papers) — see references/BiBTeX and `13_final_reading_list_2026-05-12.csv`; Appendix A.6 bibliometric overview |
| **Risk of bias in studies** | 18 | Present assessments of risk of bias for each included study. | **§3.3 Quality Assessment** (`sec:methodology:quality`) + **Fig. 6** (`fig:quality_bands`) — score distribution across all 123 records (mean 7.17/12; bands 18/57/46/2); full record-by-record scores in accompanying material (Fig. 6) |
| **Results of individual studies** | 19 | For all outcomes, present, for each study, summary statistics for each group, and an effect estimate and its precision. | Not applicable — thematic synthesis; per-study contributions described in §4–§8 |
| **Results of syntheses** | 20a | For each synthesis, briefly summarise the characteristics and risk of bias among contributing studies. | §9 Synthesis and Research Gap Analysis (`sec:synthesis_gap`) |
| | 20b | Present results of all statistical syntheses conducted. | Not applicable (no meta-analysis) |
| | 20c | Present results of all investigations of possible causes of heterogeneity among study results. | Not applicable; thematic treatment of heterogeneity (§9) |
| | 20d | Present results of all sensitivity analyses conducted to assess the robustness of the synthesised results. | Funnel reconciliation and per-stage counts (`PRISMA_NUMBERS_VALIDATION.md`) |
| **Reporting biases** | 21 | Present assessments of risk of bias due to missing results arising from reporting biases. | §3.1; Appendix C.3/C.4 (forward snowball + manual cross-validation) |
| **Certainty of evidence** | 22 | Present assessments of certainty (or confidence) in the body of evidence for each outcome assessed. | Not applicable — qualitative synthesis; see Item 15 |

### DISCUSSION

| Section | # | Checklist item | Where the item is reported |
|---|---|---|---|
| **Discussion** | 23a | Provide a general interpretation of the results in the context of other evidence. | §10 Conclusion — Summary of Findings (`sec:conclusion` / `sec:conclusion:summary`) |
| | 23b | Discuss any limitations of the evidence included in the review. | §10 Conclusion — Limitations and Future Work (`sec:conclusion:limitations`) |
| | 23c | Discuss any limitations of the review processes used. | §10 Conclusion — Threats to Validity (`sec:conclusion:threats`) and Limitations (`sec:conclusion:limitations`) |
| | 23d | Discuss implications of the results for practice, policy, and future research. | §9.6 Research Directions and Open Problems (`sec:synthesis_gap:directions`); §10 Conclusion — Future Work |

### OTHER INFORMATION

| Section | # | Checklist item | Where the item is reported |
|---|---|---|---|
| **Registration and protocol** | 24a | Provide registration information for the review, including register name and registration number, or state that the review was not registered. | **§3 Materials and Methods (`sec:methodology`)** — states the review was **not prospectively registered**, with justification (CS/AI SLRs not commonly eligible for clinical registries such as PROSPERO; no suitable AI-specific registry available at commencement). Not registered in any registry. |
| | 24b | Indicate where the review protocol can be accessed, or state that a protocol was not prepared. | Protocol embedded in Methods (§3) and Appendix A; not separately registered. |
| | 24c | Describe and explain any amendments to information provided at registration or in the protocol. | Not applicable (no registration). |
| **Support** | 25 | Describe sources of financial or non-financial support for the review and the role of the funders or sponsors. | Funding/acknowledgement statement (see manuscript acknowledgment/funding field). |
| **Competing interests** | 26 | Declare any competing interests of review authors. | Competing-interest statement (see manuscript) — no conflicts declared. |
| **Availability of data, code, and other materials** | 27 | Report which of the following are publicly available and where they can be found: template data collection forms; data extracted from included studies; data used for all analyses; analytic code; any other materials used in the review. | Held in two repositories (see Data Availability statement): `papers_code` (this manuscript, curated corpus `papers_repo/G0–G6`, PRISMA package; private) and `slr_engine` (snowballing/retrieval/screening/extraction pipeline source, incl. `app/visualise.py`, `app/prisma.py`), publicly available at <https://github.com/vanjaluk8/slr_engine>. Version-controlled deliverables: `13_final_reading_list_2026-05-12.csv`, `PRISMA_summary_2026-04-21.md`. Intermediate pipeline outputs (`pipeline_unified.csv`, retrieval/screening logs, per-record extraction spreadsheet) are regenerable local artefacts, not separately version-controlled; available on request. `papers_code` is private; public release deferred until after thesis examination. |

---

## Key funnel counts (for auditor cross-check)

| Stage | Count | Source |
|---|---|---|
| G0 seed papers in corpus | 9 | `S1_prevalidated_corpus.csv`, `G0_seed_papers.md`, §3.1 |
| Seeds submitted to retrieval API | 7 (of 9) | `log_retrieval_2026-04-21.json` `_meta.n_seeds`, §3.1 |
| Records retrieved (raw) | 1,150 | `log_retrieval` (450 backward + 700 forward examined) |
| After dedup (unique) | 972 | `log_screening` (dup = 178) |
| Merged (pre-validated G1–G6) | 502 | `S5_merged_corpus.csv` |
| Enriched (post-eligibility) | 464 | `S6_enriched_reading_pool.csv` (tiers 90/141/233) |
| Abstract reviewed | 552 | `S7b_abstract_reviewed_final.csv` (KEEP 214 / SKIP 338) |
| Full-text queue | 387 | `09_fulltext_review_queue_*.csv` |
| Data extraction | 224 | `11_data_extraction_2026-05-12.csv` |
| Final reading list | 123 (121 distinct) | `13_final_reading_list_2026-05-12.csv` (tiers 48/42/33) |

---

*This checklist was generated to accompany the manuscript as Supplementary Material and to support the MDPI editorial audit. Items marked "Not applicable" reflect the qualitative, thematic nature of this SLR of methods/systems literature, in accordance with the PRISMA 2020 guidance that reporting should be adapted to the review type.*
