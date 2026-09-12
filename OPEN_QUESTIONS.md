# Open Questions — Author Report (Phase 3)

Per REVISION_PROMPT.md: this file makes no manuscript edits. Each section states
the item ID, the exact file/line, the offending text quoted verbatim, what the
review alleges, what evidence exists in the repo (including primary-source PDFs
where available), the specific question for the author, and the minimal edit
that would follow from each possible answer.

**Verification method for the Citation Integrity section below:** every item
marked with a verdict was checked directly against the cited paper's own PDF
(from `materials/writing_materials/pdfs/`) or, where no local PDF existed,
against its arXiv abstract fetched live via the arXiv API. No verdict below
rests on the reviewer's allegation alone, and none rests on prior knowledge of
the literature — every claim is backed by a verbatim quote from the primary
source, cited by page/section where the PDF was used.

---

## Citation integrity

### E-1: Zadouri et al. [102] — O(log N) communication-budget claim — CONTRADICTED
- **Manuscript location:** `sections/03_methodology.tex` line ~230 (§7.2 area is
  now cross-referenced from methodology; original claim text lives in
  `sections/07_moe_routing.tex`), cited as `ZadouriPushMoE2024`
- **Manuscript claim (verbatim):** "demonstrating that MoE routing quality
  degrades gracefully when all-to-all communication is limited to O(log N)
  messages per batch — a communication budget consistent with DHT-based
  lookup" (§9.1 SQ4 leans on this bridge)
- **Cited work:** Zadouri, Üstün, Ahmadian, Ermiş, Locatelli, Hooker,
  "Pushing Mixture of Experts to the Limit: Extremely Parameter Efficient MoE
  for Instruction Tuning" (arXiv 2309.05444)
- **Primary-source evidence:** Read the paper's abstract and introduction
  (page 1) and ran a full-text search for "communicat", "O(log", "dht", and
  "message" across the entire PDF — **zero matches for any of the four
  terms**. The paper's actual subject, per its own abstract: "we push MoE to
  the limit. We propose extremely parameter-efficient MoE by uniquely
  combining MoE architecture with lightweight experts... showcasing its
  ability to deliver robust performance even when subjected to rigorous
  parameter constraints." This is about memory/parameter efficiency, not
  communication cost, message complexity, or network topology.
- **Verdict: CONTRADICTED.** The paper contains no O(log N) communication
  result of any kind. §9.1's SQ4 answer, which leans on this citation to
  bridge MoE routing literature to DHT-based lookup, needs to drop this
  citation or find a different source for the claim.
- **Minimal edit:** delete the sentence and its dependent claim in SQ4, or
  replace the citation if you have a different source in mind for a
  genuine MoE-communication-budget result.

### E-2: Zeng et al. [65] miscited; Aghajanyan 2021 absent from corpus — CONTRADICTED
- **Manuscript location:** `sections/04_peft.tex` §4.1 and §4.3, cited as
  `ZengExpressive2024`
- **Manuscript claim (verbatim, §4.3):** "The theoretical basis for LoRA's
  effectiveness was established earlier by work on intrinsic dimensionality …
  Zeng et al. [65] showed that the gradient signal during fine-tuning lies
  near a low-rank manifold, and that models pre-trained at scale are already
  close to the optimum."
- **Cited work:** Zeng & Lee, "The Expressive Power of Low-Rank Adaptation"
  (arXiv 2310.17513, published ICLR 2024)
- **Primary-source evidence (page 1, abstract + intro):** "This paper takes
  the first step to bridge this gap by theoretically analyzing the expressive
  power of LoRA. We prove that, for fully connected neural networks, LoRA can
  adapt any model f to accurately represent any smaller target model f̄ if
  LoRA-rank ≥ (width of f) × (depth of f̄ / depth of f)... Our work focuses
  solely on the expressive power of the model with low-rank adapters, i.e.,
  we show that under which conditions effective low-rank adapters exist for
  the given adaptation task. **This excludes other aspects such as
  optimization and generalisation.**" The paper's own related-work paragraph
  cites Hu et al. 2022a (LoRA) as a predecessor it builds on.
- **Verdict: CONTRADICTED**, on two independent grounds: (a) the paper is
  explicitly about representational capacity/expressivity theory (can a
  rank-r adapter exactly represent a target model), and explicitly disclaims
  any optimization/gradient-dynamics claim — it does not contain a
  "gradient signal lies near a low-rank manifold" result; (b) the paper is
  from 2024 and cites LoRA (2021/2022) as prior work, so it cannot have
  "established earlier" LoRA's theoretical basis — this is chronologically
  impossible on the paper's own terms, independent of point (a).
- **Aghajanyan et al. 2021 ("Intrinsic Dimensionality Explains the
  Effectiveness of Language Model Fine-Tuning", ACL 2021):** confirmed absent
  from `bibliography.bib` (no "Aghajanyan" or "intrinsic dimensionality"
  match) and from the local PDF corpus. This is the seminal antecedent the
  reviewer alleges is the actual paper being described, and it is genuinely
  missing from the 135-reference list.
- **Minimal edit:** correct the §4.3 attribution (the "established earlier"
  clause needs a different, earlier citation — Aghajanyan et al. 2021 is the
  reviewer's candidate, but adding it is your call, not mine, per the rule
  against introducing citations from my own literature knowledge), and
  either delete or re-source the "gradient signal... low-rank manifold"
  claim, since Zeng et al. does not support it.

### E-3: Ponti et al. [76] vs Pfeiffer [29] — modular-taxonomy attribution — CONTRADICTED (swap indicated)
- **Manuscript location:** `sections/05_adapter_composition.tex` §5.1
- **Manuscript claim (verbatim):** credits ref [76] with "a systematic
  taxonomy of modular deep learning" organising "modular architectures across
  four dimensions of variation"
- **Cited work [76]:** `Ponti2023` = Ponti, Sordoni, Bengio, Reddy, "Combining
  Modular Skills in Multitask Learning" (arXiv 2202.13914)
- **Primary-source evidence (arXiv abstract, fetched live):** "In this work,
  we assume that each task is associated with a subset of latent discrete
  skills from a (potentially small) inventory. In turn, skills correspond to
  parameter-efficient (sparse/low-rank) model parameterisations. By jointly
  learning these and a task-skill allocation matrix, the network for each
  task is instantiated as the average of the parameters of active skills...
  We evaluate our latent-skill model on... multitask reinforcement learning
  [BabyAI]... and few-shot adaptation... [CrossFit]." This is a specific
  latent-skill/skill-allocation method paper (the Polytropon line) with no
  taxonomy or four-dimension framework of any kind.
- **Cited work [29]:** `PfeifferModular2023` = Pfeiffer, Ruder, Vulić, Ponti,
  "Modular Deep Learning" (arXiv 2302.11529) — already correctly used
  elsewhere in the manuscript, in Table 4.
- **Primary-source evidence (arXiv abstract, fetched live):** "We offer a
  survey of modular architectures, providing a unified view over several
  threads of research that evolved independently in the scientific
  literature." This is unambiguously the survey/taxonomy paper the
  manuscript's claim describes (its title is literally "Modular Deep
  Learning").
- **Verdict: CONTRADICTED** for [76] (wrong paper — no taxonomy claim exists
  in Ponti2023); strong title/abstract-level evidence that [29] is the
  correct reference, though the exact "four dimensions of variation" framing
  was not independently confirmed word-for-word (no PDF of PfeifferModular2023
  was available locally; only the abstract was checked).
- **Minimal edit:** swap the citation from `Ponti2023` to `PfeifferModular2023`
  in §5.1, or cite both with the specific contribution attributed to each
  (Ponti2023 for the skill-matrix method it actually proposes, elsewhere in
  the text where that's relevant).

### E-4: MOELoRA [62, Liu et al.] — two attributed claims, both — CONTRADICTED
- **Manuscript location:** `sections/07_moe_routing.tex` §7.3 (line ~98) and
  §7.4 (line ~144), cited as `LiuWhenMOE2024`
- **Manuscript claims (verbatim):**
  - §7.3: "MOELoRA (Liu et al.) attaches separate LoRA experts per attention
    head and routes each token to its top-$k$ experts at the head level"
  - §7.4: "Liu et al. provided a comprehensive analysis of when MoE routing
    benefits LLM fine-tuning, identifying task diversity and data
    heterogeneity as the primary drivers"
- **Cited work:** Liu, Wu, Zhao, Zhu, Xu, Tian, Zheng, "When MOE Meets LLMs:
  Parameter Efficient Fine-tuning for Multi-task Medical Applications"
  (SIGIR 2024)
- **Primary-source evidence (pages 1, 4, 5):**
  - Abstract: "we devise multiple experts as the trainable parameters, where
    each expert consists of a pair of low-rank matrices... Then, a
    **task-motivated gate function** for all MOELoRA layers is proposed,
    which can control the contributions of each expert and produce distinct
    parameters for **various tasks**."
  - Page 5 (§3.3, the routing mechanism itself): "we exclusively input the
    **task identity** into the gate function... If the gate function is
    driven by the input vector x, the weight vector would differ across
    samples, leading to a sample-specific fine-tuned parameter matrix...
    **Our approach diverges**" [from per-sample/per-token routing — they
    deliberately route by task ID instead].
  - Page 5 (§4, Research Questions): RQ1–RQ4 are all about evaluating their
    own proposed MOELoRA method against baselines (performance, ablations,
    hyperparameter sensitivity, efficiency) — not a general empirical
    analysis of "when MoE routing benefits fine-tuning" across settings.
- **Verdict: CONTRADICTED, both claims.** §7.3: the paper's gate function is
  explicitly task-identity-driven, not per-token top-k at the attention-head
  level — the paper's own text contrasts its design against exactly the kind
  of per-sample/token routing the manuscript describes. §7.4: this is a
  single-method proposal paper benchmarked against baselines, not "a
  comprehensive analysis of when MoE routing benefits fine-tuning" — that
  framing does not match the paper's actual structure or stated contribution.
- **Minimal edit:** rewrite or remove both sentences; if a different paper
  actually contains the head-level/top-k routing description or the
  routing-benefits analysis, that citation would need to be identified and
  added (not something I can do from my own knowledge of the literature).

### E-5: MAD-X Table 7 row — dataset claim — CONTRADICTED
- **Manuscript location:** `sections/03_methodology.tex` Table 7
  (`tab:datasets`), MAD-X row
- **Manuscript claim (verbatim):** "GLUE (6 langs), cross-lingual transfer,
  Accuracy, zero-shot transfer"
- **Cited work:** `PfeifferMADX2020` = Pfeiffer, Vulić, Gurevych, Ruder,
  "MAD-X: An Adapter-Based Framework for Multi-Task Cross-Lingual Transfer"
  (EMNLP 2020)
- **Primary-source evidence (page 1, abstract):** "MAD-X outperforms the
  state of the art in cross-lingual transfer across a representative set of
  typologically diverse languages on **named entity recognition** and
  **causal commonsense reasoning**, and achieves competitive results on
  **question answering**." No mention of GLUE anywhere in the abstract; GLUE
  is a monolingual English benchmark and has no six-language variant.
- **Verdict: CONTRADICTED.** Actual datasets per the paper's own abstract:
  NER, causal commonsense reasoning (this is XCOPA, per the paper's task
  description), and QA.
- **Minimal edit:** replace "GLUE (6 langs)" with the correct dataset names
  (NER, XCOPA, QA — confirm exact benchmark names from the paper's
  experiments section if you want dataset-level precision beyond what the
  abstract states) in Table 7's Dataset and Task Type columns.

### E-6: Ormándi et al. [23] — O(log N) epidemic-spreading claim — CONTRADICTED
- **Manuscript location:** `sections/02_background.tex` line ~138 (§2.3) and
  `sections/09_synthesis_gap.tex` (§9.4), cited as `OrmandyGossip2013`
- **Manuscript claim (verbatim, §2.3):** "information spreads across the
  network in $O(\log N)$ rounds with high probability \cite{OrmandyGossip2013}"
- **Cited work:** Ormándi, Hegedűs, Jelasity, "Gossip Learning with Linear
  Models on Fully Distributed Data" (Concurrency and Computation: Practice
  and Experience, 2013)
- **Primary-source evidence:** confirmed the bib entry matches this exact PDF
  (title, authors, journal, DOI all match). Read the abstract (page 1): the
  paper's contribution is "an ensemble learning method, which — through the
  continuous combination of the models in the network — implements a virtual
  weighted voting mechanism over an exponential number of models... We prove
  the convergence of the method theoretically." Ran a full-text search across
  the entire PDF for "O(log", "log N", and "rounds with high probability" —
  **zero matches for any of the three**.
- **Verdict: CONTRADICTED.** The paper contains no O(log N) round-complexity
  or epidemic-spreading result. This is very likely the uncited classical
  rumour-spreading result (Demers/Karp/Pittel-type bound), misattributed here
  to a specific empirical gossip-learning paper that doesn't contain it. The
  same citation is reused for the same claim in §9.4, where it underwrites a
  gap-analysis claim.
- **Minimal edit:** cite the actual source of the O(log N) bound (a classical
  epidemic/rumour-spreading paper — identifying which one is your call, not
  mine), or delete the specific complexity claim and keep only the
  qualitative "gossip protocols disseminate information efficiently" framing
  in both locations.

### E-7: Internal contradiction on gossip-learning convergence — CONTRADICTED (claim oversimplified)
- **Manuscript location:** `sections/08_p2p_federated.tex` line 59 (§8.2) vs
  `sections/03_methodology.tex` line 762 (Table 7, Gossip Learning row)
- **Manuscript claims (verbatim):**
  - §8.2: "Convergence is faster than FL per communication round due to the
    direct peer-to-peer exchange"
  - Table 7: "≈ FL quality (20–50% slower)"
- **Cited work (both):** `HegeduisGossip2019` = Hegedűs, Danner, Jelasity,
  "Gossip Learning as a Decentralized Alternative to Federated Learning"
  (DAIS 2019)
- **Primary-source evidence (page 84, §4.5 Results):** "Most importantly,
  gossip learning clearly **outperforms** federated learning in the case of
  **high compression rates** (low sampling probability) over two of the
  three datasets, and it is competitive on the remaining dataset as well...
  Indeed, **with no compression, federated learning performs better**.
  However, with high compression rates, slower aggregation is compensated
  by a higher communication efficiency." The paper's comparisons throughout
  (Figures 2–4) are plotted against wall-clock time (hours), not
  communication rounds.
- **Verdict: CONTRADICTED as a flat, unconditional claim.** The paper's own
  finding is compression-rate- and dataset-dependent: gossip learning is
  *slower* than FL with no compression, and only *outperforms* FL under high
  compression — the opposite of a simple "faster... due to direct
  peer-to-peer exchange" statement, and the comparison axis in the paper is
  wall-clock time, not per-round. I could not locate a verbatim "20–50%
  slower" figure anywhere in the paper (read in full); Table 7's specific
  number may come from a different source or may be an approximation not
  traceable to explicit text in this citation.
- **Minimal edit:** rewrite §8.2 to state the actual, conditional finding
  (compression-rate-dependent, wall-clock time, not "per round"); verify
  Table 7's specific "20–50% slower" figure against wherever it actually
  originates, or replace it with a qualitative description matching what
  the cited paper supports.

### E-8: S-LoRA [Sheng2024] — second mechanism mis-described — CONTRADICTED
- **Manuscript location:** `sections/06_inference_systems.tex` §6.2
- **Manuscript claim (verbatim):** "S-LoRA introduced two key mechanisms:
  Unified Paging … and a stateless scheduler that selects which adapters to
  prefetch into GPU memory based on request queue depth and adapter
  popularity."
- **Cited work:** Sheng et al., "S-LoRA: Serving Thousands of Concurrent LoRA
  Adapters" (arXiv 2311.03285, MLSys 2024)
- **Primary-source evidence (page 1, abstract):** "S-LoRA stores all adapters
  in the main memory and fetches the adapters used by the currently running
  queries to the GPU memory. To efficiently use the GPU memory and reduce
  fragmentation, S-LoRA proposes Unified Paging... Additionally, S-LoRA
  employs **a novel tensor parallelism strategy and highly optimized custom
  CUDA kernels for heterogeneous batching of LoRA computation**." No mention
  of "popularity," "queue depth," or a "prefetch scheduler" anywhere in the
  abstract.
- **Verdict: CONTRADICTED.** The paper's own stated second contribution is
  tensor parallelism + custom CUDA kernels for heterogeneous batching (this
  matches the reviewer's alleged correct answer, MBGMM/MBGMV-style batching),
  not a popularity/queue-depth-based prefetch scheduler.
- **Minimal edit:** rewrite the §6.2 sentence to describe the actual second
  mechanism; check whether this also affects the P2P-analogy argument drawn
  immediately after it in §6.2, and Table 9's S-LoRA row description.

### E-9: Switch Transformers — "equivalent parameter count" — CONTRADICTED
- **Manuscript location:** `sections/07_moe_routing.tex`, line ~1031 area
- **Manuscript claim (verbatim):** "achieved a 7× pre-training speedup over
  dense T5 at equivalent parameter count"
- **Cited work:** `Fedus2022` = Fedus, Zoph, Shazeer, "Switch Transformers:
  Scaling to Trillion Parameter Models with Simple and Efficient Sparsity"
  (JMLR 23, 2022)
- **Primary-source evidence (page 1, abstract):** "We design models based off
  T5-Base and T5-Large... to obtain up to 7x increases in pre-training speed
  with **the same computational resources**."
- **Verdict: CONTRADICTED.** The comparison axis is explicitly equal
  computational cost (FLOPs/resources), not equal parameter count — MoE
  models have far more parameters than their dense comparison point at equal
  compute, which is the entire premise of sparse MoE scaling.
- **Minimal edit:** "at equivalent parameter count" → "at equal computational
  cost" (or "with the same computational resources," matching the paper's own
  wording).

### E-10: AdaMix [58] — homogeneous vs heterogeneous module mixing — CONTRADICTED
- **Manuscript location:** `sections/07_moe_routing.tex` §7.4
- **Manuscript claim (verbatim):** "routes between multiple heterogeneous PEFT
  modules (combining bottleneck adapters and LoRA matrices within the same
  layer)"
- **Cited work:** `WangAdaMix2022` = Wang, Agarwal, Mukherjee, Liu, Gao,
  Awadallah, Gao, "AdaMix: Mixture-of-Adaptations for Parameter-efficient
  Model Tuning" (EMNLP 2022)
- **Primary-source evidence (page 1, abstract):** "We propose AdaMix as a
  general PEFT method that tunes a mixture of adaptation modules — given the
  underlying PEFT method of choice — introduced in each Transformer layer...
  For instance, AdaMix can leverage a mixture of adapters like Houlsby (2019)
  **or** a mixture of low rank decomposition matrices like LoRA (2021) to
  improve downstream task performance." A full-text search of the paper for
  "heterogeneous" and "homogeneous" returned no matches at all.
- **Verdict: CONTRADICTED**, on consistent-framing evidence (the paper
  never states this explicitly as a denial, but every description of its
  mechanism is "choose one PEFT method type, then mix multiple instances of
  that type" — the abstract's own phrasing, "a mixture of adapters... **or**
  a mixture of... LoRA," directly rules out combining both within one
  configuration). This is a slightly softer verdict than the others above,
  since there is no single sentence that explicitly denies heterogeneous
  mixing — the case rests on the paper's total silence on
  heterogeneous/mixed-type composition, plus the "or" framing throughout.
- **Minimal edit:** correct to describe homogeneous mixing (multiple
  instances of one adapter type, stochastically routed); consider whether
  this claim was conflated with §5.7's UniPELT, which the reviewer notes is
  the genuinely heterogeneous-composition system in this corpus.

### E-11: Houlsby LayerNorm claim; duplicate equations — CONTRADICTED, decisively
- **Manuscript location:** `sections/04_peft.tex` lines 50–54 (prose) and
  Equation `eq:bottleneck_intro` (line 44); a second version of the same
  equation, `eq:bottleneck` in `sections/02_background.tex` line 74, includes
  a `LayerNorm(h)` term the first does not
- **Manuscript claim (verbatim, `04_peft.tex`):** "The original Houlsby et
  al. architecture additionally applies layer normalisation to the adapter
  input before the down-projection, which is abstracted away in Equation
  (eq:bottleneck_intro) for clarity. Figure~\ref{fig:houlsby_adapter} shows
  the full architecture, including this normalisation step."
- **Cited work:** Houlsby, Giurgiu, Jastrzebski, Morrone, De Laroussilhe,
  Gesmundo, Attariyan, Gelly, "Parameter-Efficient Transfer Learning for NLP"
  (ICML 2019)
- **Primary-source evidence (page 3, Figure 2 and surrounding text):**
  Houlsby's Figure 2 (right panel, "Adapter Layer") shows the module itself
  containing exactly three elements in sequence — feedforward down-project,
  nonlinearity, feedforward up-project — plus a skip connection. **No
  LayerNorm block appears inside the Adapter Layer box.** The left panel
  ("Transformer Layer") shows LayerNorm applied to the *output* of the
  attention/FFN sub-layer, *after* the adapter and its skip-connection are
  already combined — i.e. LayerNorm is external to the adapter, part of the
  transformer's pre-existing normalisation, applied after the adapter's
  output is added back in. The paper's own text confirms this explicitly:
  "The output of the adapter is then passed directly into the following
  layer normalization," and separately, "Alongside the layers in the adapter
  module, **we also train new layer normalization parameters per task**" —
  meaning the transformer's *existing* LayerNorm parameters are fine-tuned
  per task, not that a LayerNorm module lives inside the adapter.
- **Verdict: CONTRADICTED, decisively.** LayerNorm is not inside the adapter
  module and does not sit before the down-projection; it is the surrounding
  transformer layer's own normalisation, applied after the adapter's skip
  connection, whose *parameters* (not architecture) are additionally
  fine-tuned per task.
- **Minimal edit:** correct the prose and Equation (`eq:bottleneck` in
  `02_background.tex`) to remove `LayerNorm(h)` from inside the adapter
  formula, and reword the explanatory sentence to describe the actual
  mechanism (trainable existing LayerNorm parameters, not an internal
  normalisation step). Independent of this fix: merge the two versions of
  the bottleneck-adapter equation (`eq:bottleneck` and `eq:bottleneck_intro`)
  into one, since having two slightly different forms in two sections is a
  MECHANICAL duplication issue regardless of which one is correct.

### E-12: Uncited claim doing real work — flagged, no PDF check possible
- **Manuscript location:** `sections/04_peft.tex` §4.3
- **Manuscript claim (verbatim):** "subsequent studies demonstrate that
  applying LoRA to all projection matrices including Wk, Wo, and FFN layers
  is required to match full fine-tuning performance"
- **Evidence:** no `\cite{}` attached to this sentence (confirmed by
  inspection); it sits immediately after a claim that LoRA on Wq/Wv alone
  matches full fine-tuning, creating an internal tension the sentence never
  resolves.
- **Question for the author:** which specific paper(s) support this claim?
  There is no PDF to check since no citation is given.
- **Minimal edit:** add the citation, or delete the sentence — no in-between
  fix is possible without knowing the intended source.

### E-13: Author-count errors — already fixed
Status unchanged from WP-3: "Wohlin et al."→"Wohlin" (5 instances), "Chen et
al."→"Chen" (1 instance, the single-authored `ChenFlashServe2025`),
"Mahabadi et al."→"Karimi Mahabadi et al." (both occurrences, plus the
underlying bib `author` fields corrected). Nothing further needed unless you
know of additional instances not caught by text search.

### E-14: Šajina thesis year — 2021 vs 2025 — RESOLVED
- **Manuscript location:** Table 1 and ref `Sajina2025` say 2025;
  `sections/12_appendix.tex` Appendix B, Group 3 Undermind prompt says
  "Šajina (2021, University of Rijeka doctoral thesis)"
- **Primary-source evidence:** located and opened the actual thesis PDF
  (`materials/writing_materials/pdfs/seed/Robert Šajina - Deep Learning
  Personalization Methods in Peer-to-peer Heterogeneous Systems.pdf` — note:
  there is a *different* "Šajina" thesis in the same folder by "Romeo
  Šajina," on an unrelated pose-forecasting topic; do not confuse the two).
  Robert Šajina's title page reads: "University of Rijeka, Faculty of
  Informatics and Digital Technologies... Doctoral Thesis... **Rijeka,
  2025**." The bib entry (`Sajina2025`, `school = University of Rijeka...`,
  `year = 2025`) matches this exactly.
- **Verdict: RESOLVED.** 2025 is correct (Table 1, ref `Sajina2025`); the
  "2021" in Appendix B's Group 3 prompt is the error.
- **Minimal edit:** change "Šajina (2021, ...)" to "Šajina (2025, ...)" in
  Appendix B — this is now a MECHANICAL fix, not a judgement call, since the
  correct year is independently confirmed from the primary source. Left
  unedited here per the rule that citation corrections go through the author
  report, but it is fully resolved and safe to apply as-is.

### E-15: CaraServe — 1.4× vs 1.7×, and "≤99% SLO attainment" — RESOLVED
- **Manuscript location:** `sections/06_inference_systems.tex` §6.3 and
  Table 9 say "up to 1.7× lower serving latency"; Table 7
  (`sections/03_methodology.tex`) says "1.4× on average"
- **Primary-source evidence, arXiv v1 preprint (page 1, abstract):** "Our
  results demonstrate that CaraServe can speed up the average request serving
  latency by up to **1.4×** and achieve an SLO attainment of up to 99%."
- **Primary-source evidence, published USENIX ATC 2025 version ("Toppings"):**
  "TOPPINGS improves the average request serving latency by up to **1.7×**
  and achieves an SLO attainment of up to 99%."
- **Verdict: RESOLVED.** The number changed between the preprint (1.4×) and
  the peer-reviewed published version (1.7×) — both figures are real, they
  just come from different versions of the same underlying work. Since the
  citation resolves to the published Toppings paper, 1.7× is the
  version-consistent number, and Table 7's "1.4×" is the stale one to
  update. Both sources confirm "up to 99%," not "≤99%" — "≤99%" is indeed a
  vacuous phrasing (as the reviewer notes, everything is trivially ≤99%);
  the paper's own wording is "up to 99%."
- **Minimal edit:** change Table 7's "1.4× on average" to "1.7× on average"
  (or however you want to phrase the reconciled figure), and change "≤99%
  SLO attainment" to "up to 99% SLO attainment" in Table 9. Both are now
  MECHANICAL fixes with a decisive primary-source basis, left for you to
  apply since E-items go through this report per the task's rules.

---

## Scoping and analysis

### S-1: Extend concept matrix to the 48 Tier-1 records
- **Scaffolding prepared:** `verify/s1_tier1_concept_matrix_scaffold.csv` — 48
  rows (one per Tier-1 record, confirmed count via
  `snowball_output/13_final_reading_list_2026-05-12.csv`'s `tier` column),
  columns: `paper_key`, `title`, `authors`, `year`, `venue`, `doi`,
  `arxiv_id`, then the seven concept-matrix dimensions
  (`frozen_backbone`, `adapter_exchange`, `p2p_topology`, `discovery`,
  `multi_task_fusion`, `privacy_dp`, `no_central_coordinator`), all empty,
  plus a `notes` column. Ready for you to fill in ✓/(✓)/✗/− per the same
  scoring convention already used in Table 10.
- **Not done here:** the actual scoring (requires reading each of the 48
  papers and making an architectural judgement call per dimension —
  AUTHOR work).
- **Minimal edit once scored:** publish the filled sheet as Supplementary
  Material, and add the k=1…7 distribution as a new sentence/figure in §9.3,
  per the review's Blocking-item request. That sentence is new synthesis and
  must be written by you.

### S-2: Table 10 omits decentralised MoE [63] (Ryabinin) and Dec-LoRA [36] (Ghiasvand)
- **Manuscript location:** `tab:concept_matrix` (`sections/09_synthesis_gap.tex`),
  and the "first algorithmic gap" statement (§9.4): "can DHT-based
  infrastructure, proven at scale in systems such as Kademlia, support
  adapter discovery at the capability level rather than the identifier
  level?"
- **Dec-LoRA:** already distinguished in prose (`sections/08_p2p_federated.tex`
  line ~225, WP-2) as decentralised co-training of a single shared adapter
  via gossip-averaged updates on private data — a different problem from
  independently pre-trained adapter exchange. Still not a scored Table 10
  row. **No PDF available** for Ghiasvand et al.'s Dec-LoRA in this repo's
  materials — could not independently verify beyond the existing prose note.
- **Ryabinin's mechanism — primary-source evidence** (Ryabinin & Gusev,
  "Towards Crowdsourced Training of Large Neural Networks using Decentralized
  Mixture-of-Experts," NeurIPS 2020): the paper explicitly uses Kademlia DHT
  for expert bookkeeping and lookup. Key quotes: "Workers within the DMoE
  layer interact using Kademlia DHT protocol... Each runtime periodically
  announces its experts to the DHT, associating their identifiers with the
  runtime." The actual routing procedure (page 5, Figure 2 description) is
  **two separate steps**: (1) "Choose experts **with gating function**" — a
  jointly-trained, learned sub-network selects which expert IDs are relevant
  to a given input, based on the input's content; (2) "**locate workers
  using DHT**" — once specific expert IDs are already chosen, the DHT
  resolves those IDs to network addresses. The paper states this takes "at
  most O(k log N) DHT queries to **locate** the chosen experts."
- **What this means for the gap claim:** the DHT step in Ryabinin's system is
  identifier-level lookup only (given a known expert ID, find its host) —
  the capability-level decision (which expert is relevant to this input) is
  made by a centrally/jointly-trained gating network operating over a fixed,
  closed set of experts known at training time. This is a genuinely
  different problem from discovering the right *adapter* among independently
  trained, previously-unknown adapters in an open decentralised system — the
  manuscript's own phrase "capability level rather than the identifier
  level" appears to already precisely anticipate and correctly scope around
  this distinction, rather than being falsified by it.
- **Question for the author:** given this reading, do you agree the gap
  statement's existing "identifier level" framing already accounts for
  Ryabinin's mechanism, or do you read the evidence differently? Either way,
  the review's specific ask — score [63] and Dec-LoRA as Table 10 rows — is
  independent of this question and can proceed once you decide the ✓/✗/−
  values per dimension (Dec-LoRA's values cannot be verified here for lack
  of a PDF).
- **Minimal edit:** add both as scored rows (mechanical once you decide
  values); revise the §9.4 gap sentence only if you conclude the existing
  phrasing needs sharpening in light of this evidence (new prose, yours to
  write).

### S-3: Redundant matrix rows collapse the effective sample size
- **Evidence (verified programmatically by parsing the concept-matrix table
  directly from `sections/09_synthesis_gap.tex`, not by hand-transcription):**
  of the 17 scored systems, there are exactly **12 distinct profiles**:
  - Houlsby adapters = LoRA (identical: ✓✗✗✗✗✗−)
  - **S-LoRA = Punica = CaraServe = FLoRA** (identical: ✓✓✗✗✗✗✗) — a
    **4-way** match, one more than the review's own estimate of 3
    (S-LoRA/Punica/CaraServe); FLoRA has the exact same profile too and was
    not flagged by the review.
  - MixLoRA = MiLoRA (identical: ✓✓✗✗✓✗✗)
  - The remaining 8 systems (AdapterHub, AdapterFusion, LoraHub,
    LoraRetriever, Petals, MT-EF, FedPETuning, DP-FedLoRA, Gossip Learning —
    that's actually 9, since Gossip Learning is also distinct) each have a
    unique profile.
- **Question for the author:** should redundant rows be collapsed to one
  representative each (the §9.3 "representation-by-predecessor" rule already
  used for other incremental variants), reducing the visible n from 17 to 12
  distinct profiles? Or should the manuscript instead explicitly state the
  effective n alongside the nominal 17?
- **Minimal edit once answered:** restructure Table 10 to 12 rows with a
  footnote listing which predecessor each collapsed row represents, or add
  one sentence after the table stating the effective distinct-profile count
  (12, not the ~8 a rough visual read might suggest, and not the 3-way tie
  the review itself estimated for the serving-systems group — it's 4-way).

### S-4: "Combined reference profile" row reads as a proposed system
- **Manuscript location:** `sections/09_synthesis_gap.tex` line 174 (table
  row) and lines 183–184 (surrounding text)
- **Current text (verbatim):** "The final row of Table~\ref{tab:concept_matrix}
  defines a combined reference profile that aggregates the dimensions
  addressed individually by different bodies of work. It does not represent
  a proposed system or architecture."
- **Review's proposed fix:** rename the row "Requirement profile implied by
  RQ" and add: "this row states the conjunction the review was constructed
  to test; it is a restatement of the research question, not a finding."
- **Question for the author:** do you want this exact rename and sentence, a
  variant, or do you disagree with the review's characterisation and want to
  keep the current framing? This is a naming/framing decision, not a factual
  correction.
- **Minimal edit once answered:** a one-line table-header rename plus a
  one-sentence addition — mechanical once you approve the exact wording.

### N-1: §1 and Table 4 present two disjoint sets of prior surveys
- **Evidence (verified directly from the .tex sources and bibliography.bib,
  no PDF needed):**
  - §1 (`sections/01_introduction.tex` lines 91–97) cites: `Han2024`,
    `WangAIReview2024`, `MaoLoraSurvey2024` (PEFT/LoRA surveys),
    `YeDecentralizedFL2022`, `WinkP2PFL2021` (called "surveys and position
    papers on decentralised federated learning"), `SajinaP2PConnection2024`.
  - Table 4 (`sections/03_methodology.tex`, `tab:related_surveys`) cites a
    completely disjoint set: `PfeifferModular2023`, `WoisetschlagerFLsurvey2024`,
    `YangFedLoRAsurvey2025`, `DibAgenticEdge2026`, `JiangEdgeLLM2026`,
    `LukacLLMsurvey2026`. **Zero overlap** between the two lists.
  - Bib-entry titles confirm: `WinkP2PFL2021` = "An Approach for Peer-to-Peer
    Federated Learning" (a specific system, published at DSN-W 2021 — I have
    the PDF and confirmed it presents one concrete P2P FL protocol, not a
    review); `YeDecentralizedFL2022` = "Decentralized Federated Learning
    with Unreliable Communications" (a specific algorithm/study, IEEE JSTSP
    2022). Neither title describes a review or survey — §1's characterisation
    of these two as "surveys and position papers" does not match what they
    actually are.
- **Question for the author:** was Table 4 meant to supersede §1's list
  entirely (i.e., §1's citations were never updated after the dedicated
  related-reviews search in Appendix C.3 was run), or are these genuinely two
  different literatures that both belong in the manuscript, under different
  framing?
- **Minimal edit once answered:** consolidate into one table covering all
  named prior reviews, reduce §1's prose to point at it; separately, correct
  §1's characterisation of `YeDecentralizedFL2022` and `WinkP2PFL2021` as
  "surveys and position papers" to something accurate (e.g. "system papers
  addressing decentralised FL protocols") — this second part could be done
  as a MECHANICAL fix in isolation, but is left here since it's entangled
  with the larger restructuring question.

### N-3: Petals "only deployed" superlative
- **Manuscript location:** Table 1 (`sections/03_methodology.tex`)
- **Manuscript claim (verbatim):** "Only deployed P2P frozen-backbone LLM
  inference system."
- **Tension:** §10.3's own adversarial search (Appendix C.4) names
  PlanetServe and Platformless AI as decentralised serving projects the
  review itself found and scoped out as operating at the whole-model level
  rather than the adapter level.
- **Question for the author:** do you want "Only deployed" softened to "the
  only peer-reviewed, deployed…" (consistent with the manuscript's own
  adversarial-search findings), or is there a substantive reason
  PlanetServe/Platformless AI don't count as counterexamples to this
  specific claim that should be stated instead?
- **Minimal edit once answered:** one-word/one-clause change to Table 1's
  cell.
- **Note on minor #32:** only one instance of "to the best of the author's
  knowledge" was found by text search across the whole manuscript (§8.3,
  already fixed in WP-3). The review states "at least two such hedges"
  exist; a second instance could not be located by searching for that
  phrase or close variants ("to our knowledge," "as far as is known," "to
  the author's knowledge"). If you know where the second one is, point me
  at it.

---

## Methodology

### Blocking 5: Appraisal instrument — baseline adequacy, threats reporting, peer-review status
- **Scaffolding prepared:** `verify/blocking5_appraisal_scoring_template.csv`
  — **33 rows** (parsed directly from Table 7's LaTeX body, not
  hand-transcribed — confirmed the 17 concept-matrix systems are a strict
  subset of these 33), columns `system`, `bib_key`, `in_concept_matrix_17`,
  `in_table7_33`, `baseline_adequacy`, `threats_to_validity_reporting`,
  `peer_reviewed_status`, `notes`, all empty except the membership flags.
- **Not done here:** the actual scoring — requires reading each system's
  paper and making a judgement call on baseline adequacy and
  threats-reporting quality (AUTHOR work).
- **Q5 deletion:** per the review, Q5 (contribution clarity) is scored on
  only 16/123 records (13%) and all 16 hit the maximum — delete only on your
  say-so, per REVISION_PROMPT.md's own instruction. Not deleted here.

### Major 11: Second-screener 10% sample
- **Scaffolding prepared and seeded (fixed seed `20260912`, recorded in the
  generating script for reproducibility):**
  - `verify/major11_second_screener_abstract_sample_blind.csv` — 55 of the
    552 abstract-review records, blind sheet (title/authors/year/venue/
    abstract only, no prior decision visible).
  - `verify/major11_second_screener_fulltext_sample_blind.csv` — 39 of the
    387 full-text-queue records, same blind format.
  - `verify/major11_second_screener_abstract_sample_original_decisions.csv` and
    `verify/major11_second_screener_fulltext_sample_original_decisions.csv` — the
    original decisions for both samples, kept in separate files specifically
    so the blind sheets can actually be sent to a second screener without
    leaking the disposition.
- **Not done here:** recruiting a second screener, having them fill in
  `second_screener_decision`, computing raw agreement and Cohen's κ, and
  adjudicating disagreements — all AUTHOR/external work.

### Major 18: Inclusion/exclusion criteria table
- **Evidence assembled from the pipeline data (not written up as a formal
  table file — the underlying facts, for you to format):**
  - Title-screening exclusions (`log_screening_2026-04-21.json`,
    `exclusion_breakdown`): a hard year cutoff (varies by layer; the
    ≥2021-for-snowballed rule stated in §3.2 is the operative one for the
    final corpus), "No keyword match in title" (284 records), and
    "LLM-only match (too broad)" (255 records) are the three actually-coded
    reasons.
  - Eligibility-stage exclusions (`14_final_curation_reasons.csv`, 101
    rows): coarse `category` field only — `background` (53), `topup` (34),
    `core` (14). **No finer per-record reason exists** in this file beyond
    these three category labels.
  - English-language and preprint-citation-proxy criteria are stated in
    manuscript prose (§3.2/Appendix A.3) but have **no corresponding
    exclusion code anywhere in the data** — i.e. they may have been applied
    but were never logged as a distinguishable reason.
- **Gap found, not silently smoothed over:** a genuine Kitchenham/Charters-
  style I/E table with a distinct reason per excluded record (rather than
  three coarse categories) would require a fresh full-text re-read of the
  67 background+core exclusions — that is new empirical work, not something
  derivable from existing data.
- **What I have not done:** written the actual I/E criteria table — that
  requires you to decide the criterion wording and rationale column, which
  is a presentation/scoping choice, not a data-extraction one.

### Major 20: Top-up search to the submission month
- **Prepared:** `verify/major20_topup_search_queries.md` — reuses the
  existing 20 Boolean queries from Appendix C verbatim, changing only the
  date filter to cover the gap between the last search (2026-05-12) and
  submission (~September 2026), plus an execution checklist.
- **Not done here (explicitly, per instruction):** running the queries or
  screening/judging the results.

### Major 21: Systematic citation-verification pass (DOI resolution)
- **Network-verified all 128 DOI'd references** (of 135 total; 7 have no DOI
  field, all individually reviewed and defensible — a doctoral-course
  reference, an API-docs page, two theses, a serving-system report, a
  language-model report, and a BitTorrent incentives paper): checked each
  DOI against `doi.org` directly via `curl`, cross-referencing any failure
  against Crossref's search API and, for arXiv identifiers, arXiv's own
  query API.
- **Result: 125 of 128 resolve correctly.** Three did not, and all three
  have now been corrected directly in `bibliography.bib` (this is a
  mechanical, network-verified identifier correction, not a citation-content
  judgement call — the author/title/venue fields were already correct in all
  three cases; only the DOI digits were wrong):
  - `MahabadiCompacter2021` cited arXiv 2110.16277, which does not exist
    (arXiv API confirms zero results for that ID). arXiv's own title search
    for "Compacter: Efficient Low-Rank Hypercomplex Adapter Layers" finds
    the real paper at **2106.04647**. Corrected.
  - `Ostapenko2024` cited DOI `10.5555/3692070.3693646`, which 404s on
    doi.org and has no Crossref record under any title search. This is a
    PMLR-hosted ICML paper, a class that frequently lacks a registered DOI
    at all. Its arXiv preprint (**2405.11157**, confirmed via arXiv API,
    same title verbatim) does exist and resolves. Corrected to the arXiv
    DOI, consistent with the bibliography's documented convention.
  - `Fedus2022` (Switch Transformers) cited DOI `10.5555/3648699.3648751`,
    which also 404s and has no Crossref record. Its arXiv preprint
    (**2101.03961**, confirmed via arXiv API) exists and resolves. Corrected
    to the arXiv DOI. (The existing `url` field pointing to jmlr.org was left
    in place — it resolves fine — this fix only touches the `doi` field.)
- **Not done here:** (a) author/venue/year metadata matching for all 135
  entries beyond the specific E-1…E-15 items above, and (b) a full
  per-reference "does every attributed claim appear in the source" pass
  beyond E-1 through E-15 — both are much larger passes than this session's
  scope, left as explicit gaps rather than partially attempted and presented
  as complete.

---

## Process note

This report's citation-integrity verification was initially attempted via a
background research agent, which stalled partway through and, before
stalling, took two actions worth disclosing: it wrote a duplicate set of
scaffolding files (since discarded in favour of the versions referenced
above, which were built by parsing the manuscript's LaTeX directly rather
than by hand-transcription, and are more accurate — e.g. it undercounted
Table 7's system list at 50 rows where the correct, parsed count is 33, and
missed one of four redundant rows in the S-3 analysis), and it made one
unreviewed git commit (correcting the same Compacter DOI error independently
re-derived above). That fix was verified correct and left in place; see
`CHANGELOG.md` for the disclosure. All of the E-1 through E-15 and S-2
primary-source verification above was completed directly, by reading the
cited papers' own PDFs or fetching their abstracts from arXiv's API.
