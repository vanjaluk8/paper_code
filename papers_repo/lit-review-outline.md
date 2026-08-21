# Literature Review Outline
## Decentralized Adapter-Based LLM Systems

**Author:** [Your Name]
**Institution:** University of Rijeka, Faculty of Informatics and Digital Technologies
**Supervisor / Co-mentor:** [Supervisor Name]
**Date:** April 2026

---

> **Review type:** Integrative + Theoretical (deductive approach)
> **Organisation:** Concept-centric (Webster & Watson, 2002)
> **Citation style:** Harvard numbered — LaTeX `\citep{}` / `\citet{}`
> **Target venues:** ACL / NeurIPS / EMNLP / Future Generation Computer Systems

---

## Abstract *(~250 words)*

- What problem does the thesis solve?
- What three fields does it synthesise? (PEFT · P2P systems · multi-task NLP)
- What is the novel contribution space (the gap)?
- What is the PoC scope?

**Status:** 🟡 Draft — finalised after all sections complete

---

## 1. Introduction *(~800 words)*

**Structure:** Funnel — broad → narrow → gap → thesis

| Sub-section | Content | Status |
|---|---|---|
| 1.1 | The scale problem — LLMs at 100B+ parameters; cost of full fine-tuning; centralised deployment bottleneck | 🟡 Partial |
| 1.2 | The decentralisation opportunity — distributed data, edge devices, privacy constraints; why centralised PEFT hubs are insufficient | 🟡 Partial |
| 1.3 | The three pillars — brief framing of PEFT, multi-task composition, and P2P systems | 🟡 Partial |
| 1.4 | **Research question** — *"How can lightweight task-specific adapters be discovered, fetched, composed, and served across a P2P network of nodes sharing a single frozen transformer backbone, with minimal latency and without centralised orchestration?"* | 🟢 Defined |
| 1.5 | Thesis contribution summary — ★A1, ★S1, ★R1, ★R2, ★T2 (one sentence each) | 🟢 Defined |
| 1.6 | PoC scope — three modular adapters (entity extraction, schema mapping, NL-to-SQL) on D1-sql (MIMIC-III / TREQS); metrics: execution accuracy, consistency, inference cost | 🟢 Defined |
| 1.7 | Paper organisation — one paragraph roadmap of all sections | 🔴 Empty |

**Figure to place here:** Figure 3 — Literature Map (G0–G5 → thesis contributions)
![Literature Map](writing/slr_methodology_paper/latex_folder/figures/fig_literature_map.png)

---

## 2. Background *(~1,200 words)*

*Purpose: introduce foundational concepts — transformers, PEFT primitives, decentralised learning. Assume graduate-level reader.*

| Sub-section | Content | Key papers | Status |
|---|---|---|---|
| 2.1 | Transformer architecture — self-attention; encoder-only vs decoder vs seq2seq; BERT; frozen backbone as unit of sharing | Vaswani 2017; Devlin 2019 | 🟡 Partial |
| 2.2 | The fine-tuning paradigm and its limits — pre-train → fine-tune; full fine-tuning cost; parameter explosion with N tasks | Houlsby 2019; Hu 2021 | 🟢 Drafted |
| 2.3 | Decentralised learning: key concepts — P2P vs FL; non-IID data; gossip averaging; directed vs undirected topology | Sajina 2023; **FedAvg 🔴**; **FedProx 🔴** | 🟡 Partial |

---

## 3. Parameter-Efficient Fine-Tuning (PEFT) *(~2,500 words)*

*Purpose: systematic treatment of PEFT families — establishes adapters and LoRA as the atomic units of knowledge in the proposed system.*

| Sub-section | Content | Key papers | Status |
|---|---|---|---|
| 3.1 | PEFT taxonomy — additive / selective / reparameterised / hybrid; comparative table | Han 2024 | 🟢 Drafted |
| 3.2 | Bottleneck adapters — architecture (down-proj → activation → up-proj + skip); GLUE results; 3.6% overhead; natural P2P unit | Houlsby 2019 | 🟢 Drafted |
| 3.3 | Low-Rank Adaptation (LoRA) — ΔW = BA; zero inference latency via weight merging; 10,000× parameter reduction | Hu 2021 | 🟢 Drafted |
| 3.4 | Advanced PEFT variants — QLoRA, Prefix Tuning, BitFit, HyperFormer, AdaLoRA; concept matrix | **QLoRA 🔴; Prefix 🔴; HyperFormer 🔴; AdaLoRA 🔴** | 🔴 Empty |
| 3.5 | PEFT system design — centralised serving (S-LoRA model); distributed training; evaluation metrics | Han 2024; Sheng 2024 | 🟢 Drafted |

**Concept matrix to place in 3.4:** adapter type × composability × P2P transfer cost × rank structure × inference overhead

---

## 4. Adapter Sharing and Composition *(~2,000 words)*

*Purpose: establish how adapters can be shared across tasks and nodes — the "glue" between PEFT and P2P.*

| Sub-section | Content | Key papers | Status |
|---|---|---|---|
| 4.1 | AdapterHub — dynamic stitching-in; per-task encapsulation; intermediate task training; **limitation: centralised registry** | Pfeiffer 2020 | 🟢 Drafted |
| 4.2 | AdapterFusion — two-stage algorithm; attention-based Q/K/V fusion; linear cost scaling → motivates sparse routing | Pfeiffer 2021 | 🟢 Drafted |
| 4.3 | Modular and compositional approaches — latent skill modules, LoRA library, gradient-free composition, weight averaging | **Ponti 2023 🔴; Ostapenko 2024 🔴; LoraHub 🔴; AdapterSoup 🔴** | 🔴 Empty |
| 4.4 | **Concept matrix: Adapter Composition Methods** — composition mechanism × local requirement × inference cost × zero-shot support | All of 4.1–4.3 | 🟡 Partial |

**Figure to place in 4.4:** Figure 1 — Concept Coverage Matrix
![Concept Coverage Matrix](writing/slr_methodology_paper/latex_folder/figures/fig_concept_dimensions.png)

---

## 5. Scalable Adapter Inference Systems *(~1,500 words)*

*Purpose: establish the engineering substrate for serving many adapters — closest existing work to the proposed system.*

| Sub-section | Content | Key papers | Status |
|---|---|---|---|
| 5.1 | S-LoRA — unified paging; heterogeneous batching; tensor parallelism; dynamic fetch from main memory; **gap: centralised store** | Sheng 2024 | 🟢 Drafted |
| 5.2 | Petals — layer sharding; client-owned PEFT; server-hosted backbone; fault tolerance; **gap: shards layers, not adapters** | Borzunov 2023 | 🟢 Drafted |
| 5.3 | Additional inference systems — Punica (SGMV kernels), dLoRA (dynamic orchestration), CaraServe (CPU-assisted) | **Punica 🔴; dLoRA 🔴; CaraServe 🔴** | 🔴 Empty |

---

## 6. Peer-to-Peer and Decentralised Learning *(~2,500 words)*

*Purpose: establish the P2P learning substrate; distinguish P2P from FL; motivate topology-aware multi-task collaboration.*

| Sub-section | Content | Key papers | Status |
|---|---|---|---|
| 6.1 | Federated learning foundations — FedAvg algorithm; FedProx proximal term; convergence under non-IID | **McMahan 2017 🔴; Li 2020 🔴; FLamby 🔴** | 🔴 Empty — **Priority 1** |
| 6.2 | Peer-to-peer deep learning — P2P vs FL; gossip averaging; non-IID; P2P-BN personalisation via BN layers; communication compression | Sajina 2023 | 🟢 Drafted |
| 6.3 | Multi-task P2P learning with transformers — MT-EF; shared encoder + task-specific output; encoder freezing; topology parameter P_T; 11.6% gain; four-task generalisation | Sajina 2024 | 🟢 Drafted |
| 6.4 | Decentralised foundation model training — heterogeneous environments; SWARM parallelism; DeFTA | **Yuan 2022 🔴; SWARM 🔴; DeFTA 🔴** | 🔴 Empty |

---

## 7. Mixture-of-Experts and Adapter Routing *(~1,800 words)*

*Purpose: establish MoE routing as the algorithmic foundation for sparse adapter selection in the proposed system.*

| Sub-section | Content | Key papers | Status |
|---|---|---|---|
| 7.1 | Sparse Mixture-of-Experts — sparsely-gated MoE; Switch Transformers top-1 routing; Expert Choice routing | **Shazeer 2017 🔴; Fedus 2022 🔴; Zhou 2022 🔴** | 🔴 Empty — **Priority 1** |
| 7.2 | MoE applied to adapter routing — SiRA, MoDE, Adapter-X | **Li 2024 🔴; SiRA 🔴; MoDE 🔴** | 🔴 Empty — **Priority 1** |
| 7.3 | Routing mechanisms and zero-shot generalisation — Arrow (zero-shot routing in LoRA library); query-driven probing | **Ostapenko 2024 🔴; Muqeeth 2024 🔴** | 🔴 Empty |

---

## 8. Synthesis: The Decentralised Adapter Marketplace *(~1,500 words)*

*Purpose: integrate all prior sections; prove the contribution space as the precise intersection of all gaps.*

| Sub-section | Content | Status |
|---|---|---|
| 8.1 | Unified problem formulation — formal definitions: frozen backbone, adapter, node, discovery, fetch, fusion, serve; ★C2 contribution | 🟡 Partial |
| 8.2 | **Concept matrix: All Related Systems** — frozen backbone × adapter-level exchange × P2P × discovery × multi-task fusion | 🟡 Partial |
| 8.3 | Gap analysis — Conceptual (★T), Algorithmic (★A), Systems (★S), Empirical (★E) | 🟢 Drafted |

**Figure to place in 8.1:** Figure 2 — System Architecture Diagram
![System Architecture](writing/slr_methodology_paper/latex_folder/figures/fig_p2p_adapter_types.png)

### Concept Matrix: All Related Systems (Section 8.2)

| System | Frozen Backbone | Adapter Exchange | P2P Topology | Adapter Discovery | Multi-task Fusion |
|---|---|---|---|---|---|
| AdapterHub (Pfeiffer 2020) | ✓ | ✓ centralised | ✗ | Label-based | ✗ |
| AdapterFusion (Pfeiffer 2021) | ✓ | ✓ local | ✗ | None | ✓ attention |
| S-LoRA (Sheng 2024) | ✓ | ✓ centralised | ✗ | None | ✗ |
| Petals (Borzunov 2023) | ✗ sharded | ✗ | ✓ | None | ✗ |
| Sajina 2024 (MT-EF) | ✓ shared enc. | ✗ full model | ✓ | None | ✓ encoder avg. |
| **Proposed system** | **✓** | **✓ P2P** | **✓** | **✓ ★A1 ★R1** | **✓ ★M2** |

---

## 9. Proof-of-Concept: NL-to-SQL on MIMIC-III *(~1,200 words)*

*Purpose: instantiate the proposed framework on a concrete, bounded problem.*

| Sub-section | Content | Status |
|---|---|---|
| 9.1 | Task definition — three modular adapters (entity extraction → schema mapping → NL-to-SQL); D1-sql dataset; frozen T5 / BERT | 🔴 Empty |
| 9.2 | Experimental design — baselines; evaluation metrics (execution accuracy, consistency, inference cost); ablation on fetch latency | 🔴 Empty |
| 9.3 | Expected results and limitations — what the PoC proves vs what is deferred (privacy, production P2P, orchestration) | 🔴 Empty |

---

## 10. Conclusion *(~600 words)*

- Restatement of research question and contribution codes (★A1, ★S1, ★R1, ★R2, ★T2)
- Summary of what the literature establishes (what is known)
- What remains unknown → motivates the thesis
- Future work directions beyond PoC scope

**Status:** 🔴 Empty — written last

---

## Appendix A — Concept Matrix (Full)

Following Webster & Watson (2002) concept-centric framework.
Rows = papers | Columns = concepts (adapter type · composability · P2P · routing · privacy · latency · dataset)

**Status:** 🟡 Populated incrementally as papers are added

---

## Appendix B — Snowball Log

| Round | Paper | Direction | Status | G-group | Decision |
|---|---|---|---|---|---|
| 1 | Houlsby 2019 | Seed | ✅ Included | G0 | Core |
| 1 | Hu 2021 (LoRA) | Seed | ✅ Included | G0 | Core |
| 1 | Pfeiffer 2020 (AdapterHub) | Seed | ✅ Included | G0 | Core |
| 1 | Pfeiffer 2021 (AdapterFusion) | Seed | ✅ Included | G2 | Core |
| 1 | Han 2024 (PEFT Survey) | Seed | ✅ Included | G0 | Core |
| 1 | Sheng 2024 (S-LoRA) | Seed | ✅ Included | G4 | Core |
| 1 | Borzunov 2023 (Petals) | Seed | ✅ Included | G3/G4 | Core |
| 1 | Sajina 2023 (P2P-BN) | Seed | ✅ Included | G3 | Core |
| 1 | Sajina 2024 (MT-EF) | Seed | ✅ Included | G3/G2 | Core |
| 2 | McMahan 2017 (FedAvg) | Backward | 🔴 To read | G3/G6 | Priority 1 |
| 2 | Li 2020 (FedProx) | Backward | 🔴 To read | G3/G6 | Priority 1 |
| 2 | Fedus 2022 (Switch Trans.) | Backward | 🔴 To read | G5 | Priority 1 |
| 2 | Ponti 2023 (Modular Skills) | Forward | 🔴 To read | G2/G5 | Priority 1 |
| 2 | Dettmers 2023 (QLoRA) | Backward | 🔴 To read | G1 | Priority 2 |
| 2 | Mahabadi 2021 (HyperFormer) | Backward | 🔴 To read | G1/G2 | Priority 2 |
| 2 | Li & Liang 2021 (Prefix Tuning) | Backward | 🔴 To read | G1 | Priority 2 |
| 2 | Ostapenko 2024 (LoRA Library) | Forward | 🔴 To read | G2/G4 | Priority 2 |
| 2 | Shazeer 2017 (MoE Layer) | Backward | 🔴 To read | G5 | Priority 2 |
| 2 | Zhou 2022 (Expert Choice) | Backward | 🔴 To read | G5 | Priority 2 |

---

## Coverage Dashboard

| Group | Papers in | Section(s) | Priority |
|---|---|---|---|
| **G0** Foundational PEFT | 5 | 3.1 · 3.2 · 3.3 · 3.5 | 🟢 Strong |
| **G1** Advanced PEFT | 0 | 3.4 (empty) | 🔴 Critical |
| **G2** Multi-task composition | 1 | 4.1 · 4.2 (partial) | 🔴 Critical |
| **G3** P2P / Federated | 3 | 6.2 · 6.3 (partial) | 🔴 Critical |
| **G4** Inference systems | 2 | 5.1 · 5.2 | 🟡 Medium |
| **G5** MoE / Routing | 0 | 7.x (all empty) | 🔴 Critical |
| **G6** Federated privacy | 0 | — | 🟡 Lower |

---

## Figures

| # | Title | Location in paper | Status |
|---|---|---|---|
| Fig 1 | Concept Coverage Matrix — Seed Papers vs Key Dimensions | Section 4.4 / Appendix A | ✅ Ready |
| Fig 2 | Proposed P2P Adapter Inference Architecture | Section 8.1 | ✅ Ready |
| Fig 3 | Literature Map — G0–G5 Groups and Thesis Contributions | Section 1 (Introduction) | ✅ Ready |
| Fig 4 | Relevance tree (snowball structure) | Section 1 or Appendix B | 🔴 Planned |
| Fig 5 | PoC pipeline diagram (NL→SQL 3-adapter chain) | Section 9.1 | 🔴 Planned |

---

## Thesis Contribution Map

| Code | Type | Description |
|---|---|---|
| ★A1 | Algorithmic | Adapter discovery protocol — DHT + capability embeddings |
| ★R1 | Representation | Adapter capability embeddings for task-agnostic similarity |
| ★R2 | Representation | Adapter behavioural fingerprints from probe-set outputs |
| ★S1 | Systems | P2P adapter marketplace framework architecture |
| ★S2 | Systems | Adapter gossip / exchange protocol |
| ★T2 | Theoretical | Reuse bounds under heterogeneous data distributions (non-IID) |
| ★M2 | Architecture | Decentralised AdapterFusion without central coordinator |
| ★V1 | Measurement | Adapter similarity metric via behavioural fingerprinting |
| ★C2 | Conceptual | Adapters as atomic units of knowledge exchange in P2P systems |

---

*Last updated: April 2026 — v0.2 (foundational seed layer complete)*
