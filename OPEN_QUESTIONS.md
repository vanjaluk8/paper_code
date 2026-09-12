# Open Questions — Author Report (Phase 3)

Per REVISION_PROMPT.md, this file was originally report-only. **Update:** once
primary-source verification produced decisive, verbatim-quoted evidence for a
subset of the E-items, the author explicitly authorised overriding the
report-only rule for those items and applying the corrections directly. Each
such item below is marked **FIXED** (or **PARTIALLY FIXED**, where a
correct-but-unverifiable replacement citation was left as a `%
TODO-AUTHOR` marker rather than invented). Items without a FIXED marker
remain report-only, either because the evidence was judged too soft to act on
without author sign-off, or because the item is inherently a scoping/framing
decision rather than a fact to correct. Each section states the item ID, the
exact file/line, the offending text quoted verbatim, what the review alleges,
what evidence exists in the repo (including primary-source PDFs where
available), the specific question for the author, and — for open items — the
minimal edit that would follow from each possible answer.

**Verification method for the Citation Integrity section below:** every item
marked with a verdict was checked directly against the cited paper's own PDF
(from `materials/writing_materials/pdfs/`) or, where no local PDF existed,
against its arXiv abstract fetched live via the arXiv API. No verdict below
rests on the reviewer's allegation alone, and none rests on prior knowledge of
the literature — every claim is backed by a verbatim quote from the primary
source, cited by page/section where the PDF was used.

---

## Citation integrity

### E-1: Zadouri et al. [102] — O(log N) communication-budget claim — CONTRADICTED — **FIXED**
**Applied:** the Zadouri paragraph (`sections/07_moe_routing.tex`) has been
removed. Its real content (parameter-efficient MoE for instruction tuning)
did not belong in the "Distributed and Crowdsourced MoE" subsection once the
fabricated communication-constraint framing was removed.

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
  result of any kind.
- **Status check (this pass):** confirmed §9.1's SQ4 answer no longer
  mentions Zadouri or any O(log N)-communication-degradation bridge claim
  — it was already rewritten to rest only on the routing-mechanisms point
  and the catalogue-construction gap, neither of which needs this
  citation. `ZadouriPushMoE2024` is not cited anywhere in `sections/*.tex`
  (an orphaned `bibliography.bib` entry only). Nothing further to do.

### E-2: Zeng et al. [65] miscited; Aghajanyan 2021 absent from corpus — CONTRADICTED — **FIXED**
**Applied:** removed the false attribution to Zeng et al. in both §4.1 and
§4.3 (`sections/04_peft.tex`). Author confirmed Aghajanyan et al. 2021 as
the intended source; network-verified (arXiv 2012.13255 / ACL Anthology
2021.acl-long.568 — abstract states pre-trained models have very low
intrinsic dimension, matching the manuscript's claim) and added as
`Aghajanyan2021Intrinsic` in `bibliography.bib`, cited at §4.1. §4.3's
occurrence (the "established earlier" paragraph) stays removed with no
replacement claim, per the TODO-AUTHOR marker's own guidance that the
surrounding prose already flows without it once §4.1 carries the citation.

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

### E-4: MOELoRA [62, Liu et al.] — two attributed claims, both — CONTRADICTED — **FIXED**
**Applied:** §7.3 rewritten to describe the actual task-identity-gate
mechanism instead of a fabricated per-attention-head, per-token top-k
description. §7.4's redundant, incorrect re-description of the same paper as
a "comprehensive analysis of when MoE routing benefits fine-tuning" was
removed (the paper is already correctly described once, at its first
mention).

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

### E-5: MAD-X Table 7 row — dataset claim — CONTRADICTED — **FIXED**
**Applied:** Table 7's MAD-X row (`sections/03_methodology.tex`) now reads
"NER, causal commonsense reasoning, QA (typologically diverse langs)" instead
of "GLUE (6 langs)," matching the paper's own abstract. Metric changed to
"Accuracy/F1" since the exact per-task metric wasn't independently confirmed
beyond the abstract-level dataset check.

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

### E-6: Ormándi et al. [23] — O(log N) epidemic-spreading claim — CONTRADICTED — **FIXED**
**Applied:** removed the incorrect citation at both occurrences (§2.3,
`sections/02_background.tex`; §9.4, `sections/09_synthesis_gap.tex`).
Author chose Karp et al. 2000 ("Randomized Rumor Spreading," FOCS) over
the alternative candidate (Pittel 1987) after both were network-verified —
Karp et al.'s own result is stated in near-identical terms to the
manuscript's claim ("...rounds ... with high probability"; verified
result: log₃n + Θ(log log n) rounds w.h.p.). Added as `KarpRumor2000`
(DOI `10.1109/SFCS.2000.892324`, verified against Crossref) to
`bibliography.bib`, cited at both occurrences.

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

### E-7: Internal contradiction on gossip-learning convergence — CONTRADICTED (claim oversimplified) — **FIXED**
**Applied:** §8.2 (`sections/08_p2p_federated.tex`) rewritten to state the
actual, compression-rate-dependent finding instead of a flat "faster... per
communication round" claim. Table 7's "20–50% slower" cell
(`sections/03_methodology.tex`) — which could not be traced to explicit text
in the cited paper — replaced with a qualitative description matching what
was actually verified (compression-rate-dependent).

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

### E-8: S-LoRA [Sheng2024] — second mechanism mis-described — CONTRADICTED — **FIXED**
**Applied:** §6.2 (`sections/06_inference_systems.tex`) rewritten to describe
the actual second mechanism (tensor parallelism + custom CUDA kernels for
heterogeneous batching) instead of the fabricated popularity/queue-depth
prefetch scheduler.

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

### E-9: Switch Transformers — "equivalent parameter count" — CONTRADICTED — **FIXED**
**Applied:** `sections/07_moe_routing.tex` now reads "at equal computational
cost" instead of "at equivalent parameter count."

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

### E-11: Houlsby LayerNorm claim; duplicate equations — CONTRADICTED, decisively — **FIXED**
**Applied:** removed `LayerNorm(h)` from the bottleneck-adapter equation
(`sections/02_background.tex`); rewrote the explanatory prose in
`sections/04_peft.tex` to correctly describe layer normalisation as external
to the adapter (the transformer's own, per-task-retrained LayerNorm, applied
after the adapter+skip connection). Also merged the two duplicate equations
into one (`eq:bottleneck`), with `04_peft.tex` now referencing it instead of
restating it under a second label.

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

### E-14: Šajina thesis year — 2021 vs 2025 — RESOLVED — **FIXED (annotated, not silently altered)**
**Applied:** the "2021" occurs inside a verbatim-quoted Undermind search
prompt (Appendix B), which the manuscript elsewhere states is reproduced
verbatim. Rather than silently changing quoted historical text, added an
editorial `[sic; ... actual defence year is 2025 ...]` annotation inline,
preserving the verbatim-reproduction claim's integrity while flagging the
discrepancy for the reader.

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

### E-15: CaraServe — 1.4× vs 1.7×, and "≤99% SLO attainment" — RESOLVED — **FIXED**
**Applied:** Table 7's "1.4× on average" (`sections/03_methodology.tex`)
changed to "up to 1.7×", matching §6.3/Table 9 and the published Toppings
paper. "≤99% SLO attainment" (Table 9, `sections/06_inference_systems.tex`)
changed to "up to 99% SLO attainment," matching the paper's own wording.

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

### N-3: Petals "only deployed" superlative — **FIXED**
- **Manuscript location:** Table 1 (`sections/03_methodology.tex`)
- **Applied:** "Only deployed P2P frozen-backbone LLM inference system." →
  "Only peer-reviewed, deployed P2P frozen-backbone LLM inference system."
  — the manuscript's own adversarial search (Appendix C.4) names
  PlanetServe and Platformless AI as decentralised serving projects that
  are not peer-reviewed academic systems, so this scoping is accurate and
  grounded in evidence already in the manuscript, not new research.
- **Note on minor #32:** only one instance of "to the best of the author's
  knowledge" was found by text search across the whole manuscript (§8.4,
  already fixed in WP-3, now reads "within the 123-record corpus"). The
  review states "at least two such hedges" exist; a second instance could
  not be located after two separate exhaustive searches (this session
  re-checked every variant: "to our knowledge," "as far as is known," "not
  aware of," "unaware of," "to my knowledge," plus related superlative
  patterns like "one of the first"/"first to") — zero remaining hits. If
  you know where the reviewer's second instance is, point us at it;
  otherwise this is likely a reviewer overcount or a phrase already fixed
  by an earlier, unrelated edit.

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

### Major 19: Top-up search to the submission month — SEARCH, ABSTRACT SCREEN, AND ELIGIBILITY DECISION DONE
- **All three sources now run.** `verify/major19_scopus_wos_topup_queries.md`
  gave the ready-to-paste Boolean queries (Appendix C's 20, year bound moved
  to the gap window); the author ran all 10 Scopus + all 10 WoS queries live
  via each platform's web Advanced Search (no API access needed or used).
  A parallel free-tier arXiv search was also run as an independent third
  source (this environment has no Scopus/WoS API access, so arXiv was the
  only source directly runnable here).
- **Scopus** (`verify/major19_scopus_trim_and_merge.py`): 9,516 raw rows
  (10 queries) → 8,724 unique after dedup (by EID/DOI/title) → 41 pass the
  title-level PEFT+scope filter → 40 new (1, "Symbiosis: Multi-Adapter
  Inference and Fine-Tuning," already in the 123-record corpus — correct
  hit, not new). Raw exports were 114MB; trimmed to 2.9MB (dropped
  Abstract/References/Funding-Details/etc., kept everything needed for
  citation and screening).
- **WoS** (`verify/major19_wos_trim_and_merge.py`): 5,316 raw rows (Q3 split
  into Q3/Q3b/Q3c by the author due to WoS's 1000-row per-export cap,
  treated as one query) → 4,983 unique after dedup (by UT, WoS's accession
  number) → 43 pass the filter → 43 new (0 already in the corpus).
- **arXiv** (`verify/major19_topup_arxiv_search.py`, 6 thematic queries):
  481 raw → 27 shortlisted, 0 already in the corpus.
- **Cross-source consolidation** (`verify/major19_consolidate_all_sources.py`,
  output `verify/major19_topup_all_sources_consolidated.csv`): **93 distinct
  new titles** across all three sources. 17 were found independently by
  *both* Scopus and WoS — a stronger signal than a single-source hit —
  including FedALT, FedFA, PrivLoRA, pFedLoRA, DyMerge-LoRA, AdaFuse,
  CLARE, MeLoRA. Zero cross-source agreement with arXiv (expected: it
  indexes an almost entirely disjoint preprint set vs. Scopus/WoS's
  peer-reviewed venues). One WoS-only title stands out on relevance grounds:
  **"DeCAF: Decentralized consensus-and-factorization for low-rank
  adaptation of foundation models"** (Neural Networks) — close enough to
  the review's own core P2P/decentralised-LoRA subject that it may bear
  directly on the gap claims, the same way Ryabinin's paper did in S-2.
- **Abstract-level topical screen now done** (`verify/major19_recover_abstracts.py`
  recovered all 93/93 abstracts from the raw Scopus/WoS exports and the
  saved arXiv summaries → `verify/major19_topup_with_abstracts.csv`;
  `verify/major19_screening_decisions.py` applied the same topical-relevance
  read used at the manuscript's own Layer-2 abstract stage → outputs
  `verify/major19_topup_screened.csv` (all 93, with per-item rationale) and
  `verify/major19_topup_kept_after_screening.csv` (the 65 survivors)). This
  is a title-filter-plus-abstract-read pass, **not** a Table A2 eligibility
  or full-text/quality-appraisal decision — treat it as a recommended
  shortlist for the author to confirm, the same status the manuscript's own
  abstract-stage dispositions had before full-text review.
- **Result: 65 KEEP / 28 DROP.** All 28 DROPs share one pattern: the paper's
  actual application domain sits outside the review's three pillars even
  though its title matched the PEFT/adapter+scope keyword filter — medical
  imaging/diagnosis (7: BiomedCLIP chest X-ray, ophthalmic diagnosis,
  coronary-artery segmentation, SAM3 segmentation, echocardiography
  translation, TCPA-MedMTL, ultrasound), industrial/IoT (RUL estimation,
  IIoT intrusion detection, IoV energy-constrained personalization),
  vision-only (face-forgery detection, video class-incremental learning,
  domain-incremental learning, ViT pruning), telecom (6G V2X beam
  prediction), bioinformatics (protein classification), robotics (VLA
  continual learning), plus one true false-positive on terminology
  ("Fully decentralized inference for spatial data using low-rank models"
  — geostatistics' "low-rank" is unrelated to LoRA). None of the 65 KEEPs
  were dropped on relevance grounds; all engage PEFT/LoRA, federated or
  decentralised adaptation, or multi-adapter/MoE serving for language
  models specifically.
- **Standout among the 65:** "DeCAF: Decentralized consensus-and-factorization
  for low-rank adaptation of foundation models" (Neural Networks, WoS-only
  hit) remains the strongest candidate for bearing directly on the review's
  P2P/decentralised-LoRA gap claims — see above. "RW-LoRA: Communication-
  Efficient Decentralized LoRA Fine-Tuning via Random Walks" is a second
  P2P-relevant hit worth the same scrutiny.
- **Eligibility decision now done.** The author reviewed all 65 survivors
  interactively (an artifact listing sources, screening rationale, full
  abstract, DOI/arXiv link, and a per-item suggestion keyed to Appendix
  A.3's actual I4 criterion — peer-reviewed venue preferred; arXiv retained
  only with a non-trivial citation count) and made a Keep/Skip call on each.
  Decisions recorded in `verify/major19_eligibility_raw_decisions.json`;
  merged with the screening data by `verify/major19_apply_eligibility_decisions.py`
  → `verify/major19_eligibility_decisions.csv`.
- **Result: 10 KEEP / 55 SKIP.** The author applied I4 strictly: every one
  of the 10 kept candidates is from a peer-reviewed venue (Scopus and/or
  WoS); no arXiv-only candidate was kept, including the two flagged as
  highest topical priority despite arXiv-only status — "RW-LoRA:
  Communication-Efficient Decentralized LoRA Fine-Tuning via Random Walks"
  and "Priority-Aware Learning-Unlearning Correction for Dynamic
  Decentralized LoRA Fine-Tuning" — since neither had a citation count
  checked against I4. The 10 kept:
  - AdaFuse (Scopus;WoS) — multi-adapter inference latency, Pillar 3
  - DyMerge-LoRA (Scopus;WoS) — multi-tenant composite LoRA serving, Pillar 3
  - FedALT (Scopus;WoS) — federated LoRA, Pillar 2
  - PrivLoRA (Scopus;WoS) — federated LoRA privacy, Pillar 2
  - pFedLoRA (Scopus;WoS) — federated LoRA personalisation, Pillar 2
  - Automated Federated Pipeline for PEFT of LLMs (WoS)
  - **DeCAF** (WoS) — decentralised-LoRA convergence theory; the strongest
    candidate for bearing directly on the review's P2P/decentralised-LoRA
    gap claim (§9.4) — the sole eligible hit that is actually about
    decentralisation rather than federation
  - Multi-Adapter LLMs: Dynamic Mixture of LoRAs (Scopus) — Pillar 1/2/3
  - Parameter-Efficient Large Model Transfer, Cloud-Edge Collaborative
    Inference (Scopus) — Pillar 3
  - TailorLLM (Scopus) — end-cloud LoRA serving, Pillar 3
- **Manuscript integration now done, abstract-level only — no full-text read.**
  Author instinct on reviewing the 10 was correct: most are incremental
  instances of a pattern the manuscript already documents from its own
  corpus. Reading all 10 abstracts against the specific subsections that
  already cover their topic gave a redundant/non-redundant split:
  - **Redundant (6), logged here, not cited in the manuscript:** FedALT
    (same category as `ZhaoFedMCP2024`'s model-contrastive personalisation),
    PrivLoRA (same category as `LiuDP2023`'s DP federated adapters, adds HE
    on top — not a new mechanism this review discusses), pFedLoRA (same
    category as the already-cited `Liu2024`/`Koo2025` heterogeneity work),
    Automated Federated Pipeline/FedPipe (same category as
    `Wang(Globecom2024)`'s adaptive-quantisation federated LoRA),
    Multi-Adapter LLMs: Dynamic Mixture of LoRAs (generic abstract, no named
    mechanism beyond "mixture of LoRAs", already covered at length by the
    adapter-composition/MoE-LoRA literature in §5/§7), Parameter-Efficient
    Large Model Transfer/Cloud-Edge (same category as `Cai(EdgeLLM2024)`,
    weaker evidence — BERT-scale classification, not LLM-scale).
  - **Non-redundant (4), added to the manuscript as narrative citations**
    (`sections/03_methodology.tex` §3.1 "Post-review top-up search"; cited
    in §6/§7/§8; bibliography entries added with network-verified DOIs;
    documented in Appendix C.5/D.7): DyMerge-LoRA (composite multi-adapter
    serving — an axis none of Table 9's four systems address, by the
    manuscript's own account), AdaFuse (a specific fused-kernel fix for
    MoE-adapter routing latency, more precise than §7's general
    DeepSpeed-MoE dispatch-latency discussion), TailorLLM (a named
    imitation-learning adapter-library manager, distinct from the already-
    cited `Cai2024`/`ZhangEdgeShard2025` mechanisms), and DeCAF (a second,
    independent decentralised-LoRA convergence-theory result alongside the
    already-cited `Ghiasvand2025`/Dec-LoRA — corroborates rather than closes
    the §9.4 P2P gap, since both address co-training one shared adapter,
    not the task-differentiated-adapter-exchange gap this review identifies).
  - **Deliberately not done:** none of the four was put through Wohlin
    snowballing, quality appraisal, or discovery-route classification, and
    none was merged into the 123-record corpus, the PRISMA flow diagram, or
    any corpus-derived statistic (Table~4/5, the concept matrix, the
    Boolean-recall check) — precedent is the manuscript's own existing
    "related reviews" search (§3.1), whose 7 finds are cited but likewise
    excluded from the corpus. Full-text reading of the 4 was also not
    done (abstract-only, per author instruction); if a full-text read later
    surfaces something the abstract didn't, revisit.

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

**Fixes applied directly (author-authorised, see above):** E-1, E-4, E-5,
E-7, E-8, E-9, E-11, E-14, E-15 (fully fixed); E-2, E-6 (partially fixed —
the false attribution was removed, but the correct replacement citation is
left as a `% TODO-AUTHOR` marker since inventing one would violate the rule
against introducing citations from the agent's own literature knowledge).
**Left as report-only, author judgement required:** E-3 (evidence rests on
arXiv abstracts only, no full paper read), E-10 (inferred from consistent
framing, not an explicit denial), E-12 (no citation exists to check), E-13
(already handled in WP-3, not a fact-check item). S-1 through S-4, N-1, N-3,
and the Methodology-section items remain entirely report-only as originally
scoped — none of those are simple factual corrections the way the fixed
E-items were.
