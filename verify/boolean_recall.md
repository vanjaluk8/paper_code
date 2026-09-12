# Boolean Recall of the Final 123-Record Corpus

WP-12 / Major #10. Computed by `verify/boolean_recall.py` from:
- `snowball_output/13_final_reading_list_2026-05-12.csv` (123 final records)
- `snowball_output/11_MANUAL_SCOPUS_export_1105.csv` (172 records, Appendix C's 10 Scopus queries, run 2026-05-11)
- `snowball_output/11_MANUAL_WOS_export_1105.txt` (125 records, Appendix C's 10 WoS queries, run 2026-05-11)

Match rule: DOI match first (normalised, case-insensitive, `doi.org/` prefix stripped); falling back to normalised-title match (lowercased, punctuation/whitespace stripped) only when no DOI match is found.

## Headline result

**104 of 123 final records (84.6%)** are returned by at least one of the 20 Scopus/WoS Boolean queries.

- Matched by DOI: 59
- Matched by title only (no DOI match): 45
- Not matched by either export: 19

## Records NOT returned by any Boolean query

| paper_key | title | doi | arxiv_id |
|---|---|---|---|
| 2603.02885 | MuxTune: Efficient Multi-Task LLM Fine-Tuning in Multi-Tenant Datacenters via Spatial-Temporal Backbone Multiplexing |  | 2603.02885 |
| 2511.22880 | Serving Heterogeneous LoRA Adapters in Distributed LLM Inference Systems | 10.48550/arXiv.2511.22880 | 2511.22880 |
| 2311.03285 | S-LoRA: Serving Thousands of Concurrent LoRA Adapters |  | 2311.03285 |
| 2401.11240 | CaraServe: CPU-Assisted and Rank-Aware LoRA Serving for Generative LLM Inference | 10.48550/arXiv.2401.11240 | 2401.11240 |
| 2310.18547 | Punica: Multi-Tenant LoRA Serving | 10.48550/arXiv.2310.18547 | 2310.18547 |
| 2501.15361 | Decentralized Low-Rank Fine-Tuning of Large Language Models | 10.48550/arXiv.2501.15361 | 2501.15361 |
| 2503.11880 | FedALT: Federated Fine-Tuning through Adaptive Local Training with Rest-of-the-World LoRA | 10.48550/arXiv.2503.11880 | 2503.11880 |
| 2407.00952 | SplitLoRA: A Split Parameter-Efficient Fine-Tuning Framework for Large Language Models | 10.48550/arXiv.2407.00952 | 2407.00952 |
| 2404.18848 | FeDeRA: Efficient Fine-tuning of Language Models in Federated Learning Leveraging Weight Decomposition | 10.48550/arXiv.2404.18848 | 2404.18848 |
| 2308.06522 | SLoRA: Federated Parameter Efficient Fine-Tuning of Language Models | 10.48550/arXiv.2308.06522 | 2308.06522 |
| d96aa291c0c56b9522cd7c901f1acd43818f1db3 | FedAdapter: Efficient Federated Learning for Modern NLP |  |  |
| 2404.15159 | MixLoRA: Enhancing Large Language Models Fine-Tuning with LoRA based Mixture of Experts | 10.48550/arXiv.2404.15159 | 2404.15159 |
| 2307.13269 | LoraHub: Efficient Cross-Task Generalization via Dynamic LoRA Composition | 10.48550/arXiv.2307.13269 | 2307.13269 |
| 2402.12851 | MoELoRA: Contrastive Learning Guided Mixture of Experts on Parameter-Efficient Fine-Tuning for Large Language Models | 10.48550/arXiv.2402.12851 | 2402.12851 |
| 2403.03432 | Mixture-of-LoRAs: An Efficient Multitask Tuning Method for Large Language Models | 10.48550/arXiv.2403.03432 | 2403.03432 |
| 2310.18339 | MOELoRA: An MOE-based Parameter Efficient Fine-Tuning Method for Multi-task Medical Applications | 10.48550/arXiv.2310.18339 | 2310.18339 |
| 2510.12178 | Evolution of meta's llama models and parameter-efficient fine-tuning of large language models: a survey | 10.48550/arXiv.2510.12178 | 2510.12178 |
| ecf8cb103a07e78cb3d88944691ed39e48e6cd07 | SLoRA: Scalable Serving of Thousands of LoRA Adapters |  |  |
| 10.54097/6w0gxa44 | Low Rank Adaptation Enables Efficient Domain Transfer in Billion Parameter Language Models | 10.54097/6w0gxa44 |  |

## Full per-record table

| paper_key | title | recalled | match type | matched in |
|---|---|---|---|---|
| 2603.02885 | MuxTune: Efficient Multi-Task LLM Fine-Tuning in Multi-Tenant Datacenters via Spatial-Temporal Backbone Multiplexing | No | - | - |
| 2512.20210 | Predictive-LoRA: A Proactive and Fragmentation-Aware Serverless Inference System for LLMs | Yes | DOI | Scopus |
| 10.1145/3711875.3729141 | EdgeLoRA: An Efficient Multi-Tenant LLM Serving System on Edge Devices | Yes | DOI | Scopus+WoS |
| 2511.22880 | Serving Heterogeneous LoRA Adapters in Distributed LLM Inference Systems | No | - | - |
| 10.1109/TPDS.2025.3590014 | Cannikin: No Lagger of SLO in Concurrent Multiple LoRA LLM Serving | Yes | DOI | Scopus |
| 10.1109/ICCD65941.2025.00046 | AuLoRA: Fine-Grained Loading and Computation Orchestration for Efficient LoRA LLM Serving | Yes | DOI | Scopus+WoS |
| 10.1145/3772052.3772230 | Symbiosis: Multi-Adapter Inference and Fine-Tuning | Yes | DOI | Scopus+WoS |
| 2311.03285 | S-LoRA: Serving Thousands of Concurrent LoRA Adapters | No | - | - |
| 10.1109/ICWS62655.2024.00099 | Edge-LLM: A Collaborative Framework for Large Language Model Serving in Edge Computing | Yes | DOI | Scopus+WoS |
| 2401.11240 | CaraServe: CPU-Assisted and Rank-Aware LoRA Serving for Generative LLM Inference | No | - | - |
| 2407.00066 | Compress then Serve: Serving Thousands of LoRA Adapters with Little Overhead | Yes | title | Scopus+WoS |
| 10.1145/3704440.3704777 | Comparative Analysis and Optimization of LoRA Adapter Co-serving for Large Language Models | Yes | DOI | Scopus |
| 2310.18547 | Punica: Multi-Tenant LoRA Serving | No | - | - |
| 2501.15361 | Decentralized Low-Rank Fine-Tuning of Large Language Models | No | - | - |
| 2404.05182 | DLoRA: Distributed Parameter-Efficient Fine-Tuning Solution for Large Language Model | Yes | title | Scopus |
| 2503.11880 | FedALT: Federated Fine-Tuning through Adaptive Local Training with Rest-of-the-World LoRA | No | - | - |
| 10.1109/INFOCOM55648.2025.11044641 | Federated Adaptive Fine-Tuning of Large Language Models with Heterogeneous Quantization and LoRA | Yes | DOI | Scopus+WoS |
| 10.18653/v1/2025.acl-long.67 | FedEx-LoRA: Exact Aggregation for Federated and Efficient Fine-Tuning of Large Language Models | Yes | DOI | Scopus+WoS |
| 10.1109/ICDM65498.2025.00089 | DP-FedLoRA: Privacy-Enhanced Federated Fine-Tuning for On-Device Large Language Models | Yes | DOI | Scopus |
| 2403.12313 | Improving LoRA in Privacy-preserving Federated Learning | Yes | title | Scopus |
| 2409.05976 | FLoRA: Federated Fine-Tuning Large Language Models with Heterogeneous Low-Rank Adaptations | Yes | title | Scopus+WoS |
| 10.1145/3637528.3671897 | FedBiOT: LLM Local Fine-tuning in Federated Learning without Full Model | Yes | DOI | Scopus+WoS |
| 10.52202/079017-0461 | Federated Fine-tuning of Large Language Models under Heterogeneous Tasks and Client Resources | Yes | title | Scopus+WoS |
| 2407.00952 | SplitLoRA: A Split Parameter-Efficient Fine-Tuning Framework for Large Language Models | No | - | - |
| 2410.01463 | Selective Aggregation for Low-Rank Adaptation in Federated Learning | Yes | title | Scopus |
| 2404.18848 | FeDeRA: Efficient Fine-tuning of Language Models in Federated Learning Leveraging Weight Decomposition | No | - | - |
| 2410.22815 | Towards Robust and Efficient Federated Low-Rank Adaptation with Heterogeneous Clients | Yes | title | Scopus+WoS |
| 10.18653/v1/2025.naacl-short.30 | Towards Federated Low-Rank Adaptation of Language Models with Rank Heterogeneity | Yes | DOI | Scopus+WoS |
| 10.1109/GLOBECOM52923.2024.10901572 | Federated Low-Rank Adaptation for Large Language Model Fine-Tuning Over Wireless Networks | Yes | DOI | Scopus+WoS |
| 10.1109/TMC.2025.3586644 | Adaptive Parameter-Efficient Federated Fine-Tuning on Heterogeneous Devices | Yes | DOI | Scopus+WoS |
| 10.1109/FLTA63145.2024.10840125 | Aggregating Low Rank Adapters in Federated Fine-Tuning | Yes | DOI | Scopus+WoS |
| 10.1109/ICPADS63350.2024.00040 | FedMCP: Parameter-Efficient Federated Learning with Model-Contrastive Personalization | Yes | DOI | Scopus+WoS |
| 2308.06522 | SLoRA: Federated Parameter Efficient Fine-Tuning of Language Models | No | - | - |
| 10.1145/3682068 | Differentially Private Low-Rank Adaptation of Large Language Model Using Federated Learning | Yes | DOI | Scopus+WoS |
| 10.18653/v1/2023.findings-acl.632 | FedPETuning: When Federated Learning Meets the Parameter-Efficient Tuning Methods of Pre-trained Language Models | Yes | DOI | Scopus+WoS |
| d96aa291c0c56b9522cd7c901f1acd43818f1db3 | FedAdapter: Efficient Federated Learning for Modern NLP | No | - | - |
| 10.1109/FLTA67013.2025.11336447 | FedLoRASwitch: Efficient Federated Learning via LoRA Expert Hotswapping and Routing | Yes | DOI | Scopus |
| 10.18653/v1/2025.naacl-long.201 | Sparser Mixture-of-Adapters with Cross-Layer Generalization | Yes | DOI | Scopus |
| 2404.15159 | MixLoRA: Enhancing Large Language Models Fine-Tuning with LoRA based Mixture of Experts | No | - | - |
| 2410.18035 | MiLoRA: Efficient Mixture of Low-Rank Adaptation for Large Language Models Fine-tuning | Yes | title | Scopus |
| 2405.11157 | Towards Modular LLMs by Building and Reusing a Library of LoRAs | Yes | title | Scopus |
| 2307.13269 | LoraHub: Efficient Cross-Task Generalization via Dynamic LoRA Composition | No | - | - |
| 2402.09997 | LoraRetriever: Input-Aware LoRA Retrieval and Composition for Mixed Tasks in the Wild | Yes | title | Scopus+WoS |
| 10.18653/v1/2023.findings-acl.75 | Client-Customized Adaptation for Parameter-Efficient Federated Learning | Yes | DOI | Scopus+WoS |
| 2503.12016 | A Survey on Federated Fine-tuning of Large Language Models | Yes | title | Scopus |
| 10.1145/3637528.3671573 | FederatedScope-LLM: A Comprehensive Package for Fine-tuning Large Language Models in Federated Learning | Yes | DOI | Scopus+WoS |
| 69d631b3875149050ab3088501cfc9d5cbea9e99 | Toppings: CPU-Assisted, Rank-Aware Adapter Serving for LLM Inference | Yes | title | Scopus+WoS |
| 10.1145/3795154.3795363 | FlashServe: Cost-Efficient Serverless Inference Scheduling for Large Language Models via Tiered Memory Management and Predictive Autoscaling | Yes | DOI | Scopus |
| 10.1145/3725843.3756083 | Chameleon: Adaptive Caching and Scheduling for Many-Adapter LLM Inference Environments | Yes | DOI | Scopus+WoS |
| 2007.07779 | AdapterHub: A Framework for Adapting Transformers | Yes | title | Scopus+WoS |
| 2404.13628 | Mixture of LoRA Experts | Yes | title | Scopus |
| 10.18653/v1/2024.acl-long.106 | LoRAMoE: Alleviating World Knowledge Forgetting in Large Language Models via MoE-Style Plugin | Yes | DOI | Scopus |
| 2402.12851 | MoELoRA: Contrastive Learning Guided Mixture of Experts on Parameter-Efficient Fine-Tuning for Large Language Models | No | - | - |
| 2403.03432 | Mixture-of-LoRAs: An Efficient Multitask Tuning Method for Large Language Models | No | - | - |
| 2309.05444 | Pushing Mixture of Experts to the Limit: Extremely Parameter Efficient MoE for Instruction Tuning | Yes | title | Scopus |
| 2310.18339 | MOELoRA: An MOE-based Parameter Efficient Fine-Tuning Method for Multi-task Medical Applications | No | - | - |
| 10.1145/3626772.3657722 | When MOE Meets LLMs: Parameter Efficient Fine-tuning for Multi-task Medical Applications | Yes | DOI | Scopus+WoS |
| 2306.05406 | Mixture-of-Domain-Adapters: Decoupling and Injecting Domain Knowledge to Pre-trained Language Models’ Memories | Yes | title | Scopus+WoS |
| 2210.17451 | AdaMix: Mixture-of-Adaptations for Parameter-efficient Model Tuning | Yes | title | Scopus+WoS |
| 2402.05859 | Learning to Route Among Specialized Experts for Zero-Shot Generalization | Yes | title | Scopus |
| 10.18653/v1/2021.emnlp-main.495 | Single-dataset Experts for Multi-dataset Question Answering | Yes | DOI | Scopus+WoS |
| 2402.09353 | DoRA: Weight-Decomposed Low-Rank Adaptation | Yes | title | Scopus |
| 2310.17513 | The Expressive Power of Low-Rank Adaptation | Yes | title | Scopus |
| 2311.11077 | Adapters: A Unified Library for Parameter-Efficient and Modular Transfer Learning | Yes | title | Scopus |
| 2310.11670 | Prototype-based HyperAdapter for Sample-Efficient Multi-task Tuning | Yes | title | Scopus |
| 10.52202/068431-0772 | Memory Efficient Continual Learning with Transformers | Yes | title | Scopus+WoS |
| 2205.10835 | Multilingual Machine Translation with Hyper-Adapters | Yes | title | Scopus+WoS |
| 2203.08304 | Hyperdecoders: Instance-specific decoders for multi-task NLP | Yes | title | Scopus |
| 2203.03878 | HyperPELT: Unified Parameter-Efficient Language Model Tuning for Both Language and Vision-and-Language Tasks | Yes | title | Scopus+WoS |
| 10.18653/v1/2021.acl-long.47 | Parameter-efficient Multi-task Fine-tuning for Transformers via Shared Hypernetworks | Yes | DOI | Scopus+WoS |
| 10.18653/v1/2022.acl-long.433 | UniPELT: A Unified Framework for Parameter-Efficient Language Model Tuning | Yes | DOI | Scopus+WoS |
| 10.18653/v1/2021.findings-emnlp.410 | MAD-G: Multilingual Adapter Generation for Efficient Cross-Lingual Transfer | Yes | DOI | Scopus+WoS |
| 10.18653/v1/2020.emnlp-main.617 | MAD-X: An Adapter-based Framework for Multi-task Cross-lingual Transfer | Yes | title | Scopus+WoS |
| 10.18653/v1/2021.acl-long.172 | On the Effectiveness of Adapter-based Tuning for Pretrained Language Model Adaptation | Yes | DOI | Scopus+WoS |
| 2510.12178 | Evolution of meta's llama models and parameter-efficient fine-tuning of large language models: a survey | No | - | - |
| 10.1109/CLUSTER59342.2025.11186463 | Rock: Serving Multimodal Models in Cloud with Heterogeneous-Aware Resource Orchestration for Thousands of LoRA Adapters | Yes | DOI | Scopus+WoS |
| ecf8cb103a07e78cb3d88944691ed39e48e6cd07 | SLoRA: Scalable Serving of Thousands of LoRA Adapters | No | - | - |
| 2209.01188 | Petals: Collaborative Inference and Fine-tuning of Large Models | Yes | title | Scopus+WoS |
| 2504.17449 | HMI: hierarchical knowledge management for efficient multi-tenant inference in pretrained language models | Yes | DOI | Scopus+WoS |
| 10.1145/3605573.3605585 | ITIF: Integrated Transformers Inference Framework for Multiple Tenants on GPU | Yes | DOI | Scopus+WoS |
| 10.18653/v1/2024.emnlp-main.717 | Heterogeneous LoRA for Federated Fine-tuning of On-Device Foundation Models | Yes | DOI | Scopus |
| 10.1145/3543507.3583212 | Beyond Fine-Tuning: Efficient and Effective Fed-Tuning for Mobile/Web Users | Yes | DOI | Scopus |
| 10.52202/075280-2488 | Multi-Head Adapter Routing for Cross-Task Generalization | Yes | title | Scopus+WoS |
| 10.1016/j.neunet.2026.108912 | SEA: Hierarchically searching efficient adapters for pre-trained models | Yes | DOI | Scopus+WoS |
| 2005.00247 | AdapterFusion: Non-Destructive Task Composition for Transfer Learning | Yes | DOI | Scopus+WoS |
| 10.18653/v1/2021.emnlp-main.626 | AdapterDrop: On the Efficiency of Adapters in Transformers | Yes | DOI | Scopus+WoS |
| 10.24963/ijcai.2025/1196 | Federated Low-Rank Adaptation for Foundation Models: A Survey | Yes | DOI | Scopus+WoS |
| 10.1109/ACCESS.2024.3442014 | An Overview of Autonomous Connection Establishment Methods in Peer-to-Peer Deep Learning | Yes | DOI | Scopus+WoS |
| 10.1007/3-540-45748-8_5 | Kademlia: A Peer-to-Peer Information System Based on the XOR Metric | Yes | DOI | Scopus+WoS |
| 2305.14314 | QLoRA: Efficient Finetuning of Quantized LLMs | Yes | title | Scopus+WoS |
| 10.1007/s11704-024-40663-9 | A survey on LoRA of large language models | Yes | DOI | Scopus+WoS |
| 10.54097/6w0gxa44 | Low Rank Adaptation Enables Efficient Domain Transfer in Billion Parameter Language Models | No | - | - |
| 0d2adcddccd72de47c263b6e4e0aab3dd0582a52 | ReLoRA: High-Rank Training Through Low-Rank Updates | Yes | title | Scopus |
| 2106.09685 | LoRA: Low-Rank Adaptation of Large Language Models | Yes | title | Scopus |
| a8ca46b171467ceb2d7652fbfb67fe701ad86092 | LoRA: Low-Rank Adaptation of Large Language Models | Yes | title | Scopus |
| 10.18653/v1/2021.acl-long.353 | Prefix-Tuning: Optimizing Continuous Prompts for Generation | Yes | DOI | Scopus+WoS |
| 10.18653/v1/2021.emnlp-main.243 | The Power of Scale for Parameter-Efficient Prompt Tuning | Yes | DOI | Scopus+WoS |
| 43a87867fe6bf4eb920f97fc753be4b727308923 | Towards a Unified View of Parameter-Efficient Transfer Learning | Yes | title | Scopus |
| 656ed155c2d345c19d9bff4b50f2ae00db8407cc | Compacter: Efficient Low-Rank Hypercomplex Adapter Layers | Yes | title | Scopus+WoS |
| 29ddc1f43f28af7c846515e32cc167bc66886d0c | Parameter-Efficient Transfer Learning for NLP | Yes | title | Scopus+WoS |
| 1902.00751 | Parameter-Efficient Transfer Learning for NLP | Yes | title | Scopus+WoS |
| 10.1007/s10462-025-11236-4 | Parameter-efficient fine-tuning in large language models: a survey of methodologies | Yes | DOI | Scopus+WoS |
| 10.1038/s42256-023-00626-4 | Parameter-efficient fine-tuning of large-scale pre-trained language models | Yes | DOI | Scopus+WoS |
| 10.18653/v1/2022.acl-short.1 | BitFit: Simple Parameter-efficient Fine-tuning for Transformer-based Masked Language-models | Yes | DOI | Scopus+WoS |
| 4d886c571c0849fda73a2d24e944d59fd37bcf9c | Collaborative Deep Learning in Fixed Topology Networks | Yes | title | Scopus+WoS |
| aaf4cec6c0ec0f195fc7aa3b0b175c73204fb575 | Decentralized Collaborative Learning of Personalized Models over Networks | Yes | title | Scopus+WoS |
| 10.1109/TBDATA.2023.3280405 | Privacy and Efficiency of Communications in Federated Split Learning | Yes | DOI | Scopus+WoS |
| 10.1109/jstsp.2022.3152445 | Decentralized Federated Learning With Unreliable Communications | Yes | DOI | Scopus+WoS |
| 10.18653/v1/2022.findings-naacl.13 | FedNLP: Benchmarking Federated Learning Methods for Natural Language Processing Tasks | Yes | DOI | Scopus |
| 10.1145/3429252 | Decentralised Learning in Federated Deployment Environments | Yes | DOI | Scopus+WoS |
| 10.1109/DSN-W52860.2021.00034 | An Approach for Peer-to-Peer Federated Learning | Yes | DOI | Scopus+WoS |
| 10.18653/v1/2020.emnlp-main.165 | FedED: Federated Learning via Ensemble Distillation for Medical Relation Extraction | Yes | title | Scopus+WoS |
| 10.1109/JIOT.2020.2964162 | Federated Learning With Cooperating Devices: A Consensus Approach for Massive IoT Networks | Yes | DOI | Scopus+WoS |
| 10.1109/JIOT.2024.3524255 | EdgeShard: Efficient LLM Inference via Collaborative Edge Computing | Yes | DOI | Scopus+WoS |
| 717bc487c987470e063ae92771e910da29ad77c2 | ServerlessLLM: Low-Latency Serverless Inference for Large Language Models | Yes | title | Scopus+WoS |
| 10.1145/3600006.3613165 | Efficient Memory Management for Large Language Model Serving with PagedAttention | Yes | DOI | Scopus+WoS |
| 9d7a75601e0e50dd68d40cfb8ef0e891dad797a6 | Orca: A Distributed Serving System for Transformer-Based Generative Models | Yes | title | Scopus+WoS |
| 10.1109/INFOCOM48880.2022.9796896 | Distributed Inference with Deep Learning Models across Heterogeneous Edge Devices | Yes | DOI | Scopus+WoS |
| 7d1e512888a2fa4e838c12a02ae7fce867d322a8 | DeepSpeed-MoE: Advancing Mixture-of-Experts Inference and Training to Power Next-Generation AI Scale | Yes | title | Scopus+WoS |
| fdacf2a732f55befdc410ea927091cad3b791f13 | Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity | Yes | title | Scopus+WoS |
| 19eaa4ac17550fab2917d3f6121ed25e6d857a58 | Towards Crowdsourced Training of Large Neural Networks using Decentralized Mixture-of-Experts | Yes | title | Scopus+WoS |
| 10.1007/978-3-030-22496-7_5 | Gossip Learning as a Decentralized Alternative to Federated Learning | Yes | DOI | Scopus+WoS |
| 10.1002/cpe.2858 | Gossip learning with linear models on fully distributed data | Yes | DOI | Scopus+WoS |
