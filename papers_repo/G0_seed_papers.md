# Group 0 — SEED Papers (Foundational — Read First)

**Theme:** Core foundational works that define your thesis scope

- [x] **Parameter-Efficient Transfer Learning for NLP** — Houlsby et al., 2019
  - **Venue**: ICML 2019
  - **Core Contribution**: Introduced bottleneck adapter modules inserted into frozen transformer layers; near-SOTA on 26 GLUE tasks adding only 3.6% parameters per task
  - **Relevance**: Foundational definition of the adapter paradigm; architectural baseline for PoC modular adapters
  - **URL**: https://arxiv.org/abs/1902.00751 | https://proceedings.mlr.press/v97/houlsby19a.html

- [x] **LoRA: Low-Rank Adaptation of Large Language Models** — Hu et al., 2022
  - **Venue**: ICLR 2022
  - **Core Contribution**: Freezes pre-trained weights; injects trainable rank-decomposition matrices per layer; reduces trainable parameters by 10,000× with no inference latency
  - **Relevance**: Primary PEFT method for the decentralized adapter framework; P2P nodes exchange LoRA matrices
  - **URL**: https://arxiv.org/abs/2106.09685 | https://openreview.net/forum?id=nZeVKeeFYf9

- [x] **AdapterHub: A Framework for Adapting Transformers** — Pfeiffer et al., 2020
  - **Venue**: EMNLP 2020
  - **Core Contribution**: Framework for dynamic stitching-in of pre-trained adapters for different tasks and languages; modular sharing infrastructure built on HuggingFace
  - **Relevance**: Conceptual precursor to the P2P adapter marketplace; centralized analog of the DHT-based system
  - **URL**: https://arxiv.org/abs/2007.07779 | https://aclanthology.org/2020.emnlp-demos.7/

- [x] **AdapterFusion: Non-Destructive Task Composition for Transfer Learning** — Pfeiffer et al., 2021
  - **Venue**: EACL 2021
  - **Core Contribution**: Two-stage algorithm: knowledge extraction (per-task adapters) + knowledge composition (attention-based fusion); evaluated on 16 NLU tasks
  - **Relevance**: Core composition mechanism for MoA (Mixture-of-Adapters) in the thesis framework
  - **URL**: https://arxiv.org/abs/2005.00247 | https://aclanthology.org/2021.eacl-main.39/

- [x] **Multi-task Peer-to-Peer Learning using Encoder-only Transformers** — Šajina et al., 2024
  - **Venue**: Future Generation Computer Systems (Elsevier Q1, Vol. 141, 2023)
  - **Core Contribution**: P2P collaboration on distinct NLP tasks (MLM + NER) with shared BERT encoder across nodes
  - **Relevance**: Most closely related published work — direct predecessor to this thesis
  - **URL**: https://www.sciencedirect.com/science/article/abs/pii/S0167739X23004053

- [ ] **Peer-to-Peer Deep Learning** — Šajina, 2021
  - **Venue**: University of Rijeka Doctoral Thesis 2021
  - **Core Contribution**: Foundations of P2P collaborative training without centralized server
  - **Relevance**: Theoretical foundation for decentralized learning paradigm; direct ancestor work
  - **URL**: https://www.inf.uniri.hr/images/studiji/poslijediplomski/kvalifikacijski/Robert_Sajina.pdf

- [x] **Petals: Collaborative Inference and Fine-tuning of Large Models** — Borzunov et al., 2022/2023
  - **Venue**: ACL 2023 Demo / NeurIPS 2023
  - **Core Contribution**: BitTorrent-style P2P inference with fault tolerance; BLOOM-176B at 1 step/second on consumer GPUs; exposes hidden states for PEFT
  - **Relevance**: Direct architectural inspiration; the only deployed P2P system for frozen-backbone LLM inference
  - **URL**: https://arxiv.org/abs/2209.01188

- [ ] **Parameter-Efficient Fine-Tuning for Large Models: A Comprehensive Survey** — Han et al., 2024
  - **Venue**: Transactions on Machine Learning Research (TMLR 2024)  ← corrected from arXiv
  - **Core Contribution**: Surveys all PEFT families (adapters, LoRA, prefix, prompt) with system-level implementation analysis; 370+ citations
  - **Relevance**: Primary positioning reference for the thesis literature review
  - **URL**: https://arxiv.org/abs/2403.14608 | https://openreview.net/forum?id=PkAzIOcEE9

- [x] **S-LoRA: Serving Thousands of Concurrent LoRA Adapters** — Sheng et al., 2024
  - **Venue**: Conference on Machine Learning and Systems (MLSys 2024)
  - **Core Contribution**: Unified paging for adapter weights, heterogeneous batching, tensor parallelism; 4× throughput over vLLM
  - **Relevance**: State-of-the-art multi-tenant LoRA serving baseline; centralized system the P2P framework compares against
  - **URL**: https://arxiv.org/abs/2311.03285 | https://proceedings.mlsys.org/paper_files/paper/2024/hash/35b72b6c8def4b6a5ecb68ab12e48f3a-Abstract-Conference.html
