# Changelog — PRISMA number/text edits (all in writing/mdpi_paper/mdpi_submission/)

Format: file | location | old → new | source file / row count

## Funnel numbers — VERDICT: fully reconcilable; no bold funnel value had to change.
Every manuscript funnel number was confirmed correct against pipeline files. The
two "contradictions" are explained, not typos.

| # | Location | Change | Source |
|---|----------|--------|--------|
| 1 | 03_methodology funnel ¶ | Clarified 387 composition: 214 KEEP + 173 DEFER (was: "full-text queue selection narrowed this pool to 387"). No value changed. | 09_fulltext_review_queue.csv (387 rows; abstract_decision KEEP 214 + DEFER 173); 10_data_extraction.csv (190); 11_data_extraction.csv (224) |
| 2 | 12_appendix Table tab:abstract caption | Rewrote caption (was: "173 DEFER all resolved to SKIP ... none advanced to data extraction"). Now: DEFERs subsumed into SKIP in final classification, BUT carried into queue (214+173=387) and a subset reached extraction. Fixes factual contradiction (2b). | queue file row counts |
| 3 | 12_appendix prose after table | Clarified 387 = 214 KEEP + 173 DEFER; 190 (KEEP-origin) extracted; DEFER subset read but excluded at final curation. No value changed. | queue + 10_/11_ extraction |
| 4 | 12_appendix §A.4 | "19 UNCERTAIN records are carried forward and resolved during abstract-level review" → "re-examined manually; only 3 reached abstract level, none in final list; not part of 502 pool." Fixes data contradiction. | 03_review_queue.csv (19); pipeline_unified trace (3 in S7b, 0 final) |
| 5 | 12_appendix §A.5 | Added: "On merge, 162+352=514, 12 records already present in pre-validated corpus removed as duplicates → 502 (reproducible by re-running app.merge.py); 19 UNCERTAIN not part of merge." Confirms 2a. | re-ran app.merge.py → deduped=12, prevalidated=352, new=150, total=502 |
| 6 | 12_appendix §A.7 | "464 enriched corpus records after rescues were resolved" → "32 deprioritised ... confirmed excluded and not reinstated". Fixes misleading "resolved" phrasing (2c). | 07_deprioritized.csv (32); pipeline in_final_list=0 for all 32 |

## Non-funnel edits
| # | File | Change |
|---|------|--------|
| 7 | 03_methodology | AI-disclosure sentence: added "Claude Opus 4.5" model (user-supplied; screening model claude-haiku-4-5-20251001 already in appendix) |
| 8 | 03_methodology | NEW "Eligibility Criteria" subsection (summarises appendix A.3–A.4: English-only, year≥2021 for snowballed, arXiv citation-count proxy) + forward pointer |
| 9 | 03_methodology | tab:groups caption footnote: G0 n final=18 = 4 directly-seeded + 14 snowball descendants (10 fwd + 4 bwd), not 18 of 9 seeds |
| 10 | 03_methodology | Tier-1 appraisal: added "no" % for code release (24/48 = 50.0%) and baseline (2/48 = 4.2%), matching existing threats "none" 39.6% |
| 11 | main.tex | Abstract trimmed 212 → ~177 words (≤200), structure preserved |
| 12 | main.tex | Author Contributions rewritten in CRediT single-author format, ending "The author has read and agreed to the published version of the manuscript." |
| 13 | main.tex | \acknowledgments{None.} → Not applicable. |

## FLAGS for author (not silently edited)
- **FLAG E8**: 101 records excluded between the 224-row extraction set and the
  123-paper final list (224−123=101). **pipeline_unified.csv has NO structured
  exclusion-reason / notes column** for these records (columns available:
  fulltext_decision INCLUDE 39 / '' 61 / DEFER 1; abstract_decision KEEP 67 /
  SKIP 1 / '' 33). Reason categories would need to be reconstructed by
  re-reading the excluded records — bigger than a text fix. Left unedited.
- **FLAG 5 no-DOI bib entries** (for A.8 crosswalk): KitchenhamCharters2007
  (techreport, no DOI/URL), Sajina2025 (phdthesis, no DOI — author confirmed
  this key is current; updated from Sajina2021), YuOrca2022
  (inproceedings, no DOI BUT has USENIX URL), RadfordGPT22019 (techreport, no
  DOI/URL), CohenBitTorrent2003 (inproceedings, no DOI BUT has bittorrent URL).
  URLs can be added for the 4 that have a resolvable source.
- **FLAG BIB-GAP (larger than expected)**: crosswalk of `13_final_reading_list`
  (123 rows) against all 128 bib entries finds **29 corpus papers with NO bib
  entry** (e.g. MuxTune, LoraServe, Symbiosis, Compress-then-Serve, DLoRA,
  FedBiOT, FedLoRASwitch, FederatedScope-LLM, Chameleon, MOELoRA-medical,
  MADE, PHA, HMI, ITIF, Fed-Tuning, SEA, FedNLP, FedED, + more). Proven three
  ways: (1) exact DOI/arXiv-ID absence in .bib, (2) normalized-title absence,
  (3) cardinality — the .bib has 128 entries, 38 are methodology/foundation,
  leaving 90 corpus entries, structurally < ~119 distinct corpus papers.
  Author to decide: add 29 entries vs. de-list.
- **Duplicate-pairs note**: reading list has 4 duplicate pairs (LoRA 95/96,
  Houlsby 101/102, CaraServe/Toppings 11/48, S-LoRA 9/78) ⇒ ~119 distinct, not
  120. `Sheng2024` covers line 9 (S-LoRA, MLSys); line 78 ("SLoRA: Scalable
  Serving") is that same paper, not missing. Line 57 (MOELoRA-medical, arXiv
  2310.18339) IS genuinely missing (distinct from line 58 → LiuWhenMOE2024).

## PRISMA funnel — verification COMPLETE (2026-08-28)
Re-counted every funnel stage with a proper CSV reader (headers excluded):
01_raw=972, 02_screened=972, 03_review_queue=19, 04_included=162,
00_prevalidated=352, 05_merged=502, 07_deprioritized=32, 07_excluded=6,
07_filtered=464, S7b/abstract=552, 09_fulltext_queue=387, 10_extraction(0502)=190,
11_extraction(0512)=224, 13_final=123. Derived identities verified:
162+352−12=502; 387=214 KEEP+173 DEFER (RIS=214); 224=190+34 top-up;
464+88=552 (88 not independently isolable by column — source col blank;
arithmetically consistent). All bold funnel values in the manuscript are
DATA-BACKED; no funnel total needed to change.

## Pending
- PRISMA reconciliation: COMPLETE (all funnel totals data-backed; see above).
- Bibliography crosswalk / A.8 section: PAUSED at author's request (2026-08-28)
  — author focused the session on PRISMA number consistency only. The 29-paper
  bib-gap and duplicate-pairs flags above remain recorded for future resolution.
