# Snowballed Papers — Extracted Notes

> Generated 2026-05-27
> 116 PDFs extracted across 10+ categories
> All notes follow a consistent schema: `Meta` · `Key Findings` · `Methodology` · `Relevance to Thesis` · `Limitations/Gaps`

## Categories

| Category | # PDFs | # Notes | Key Topics |
|---|---|---|---|
| `adapter-serving` | 20 | 20 | LoRA batching, tiered memory, CPU/GPU orchestration |
| `federated-PEFT` | 22 | 22 | LoRA in FL, weight aggregation, DP |
| `adapter-composition` | 16 | 16 | AdapterFusion, hypernetworks, retrieval-based composition |
| `MoE-adapter-routing` | 12 | 12 | Gating, expert selection, sparsity, load balancing |
| `P2P-DL` | 4 | 4 | Gossip, collaborative inference, DHT-based discovery |
| `P2P-FL` | 7 | 7 | P2P consensus, unreliable network, serverless FL |
| `PEFT-method` | 7 | 7 | Individual PEFT methods assessed in detail |
| `distributed-inference` | 7 | 7 | KV-cache management, P2P edge inference, tiered memory |
| `survey` | 9 | 9 | Surveys of PEFT, FL+LoRA, P2P DL |
| Other (MoE-routing, gossip, distributed-PEFT, federated-PEFT+routing, foundational-P2P) | 10 | 10 | MoE gating, gossip alternatives |
| **Total** | **116** | **> 100** | |

## Cross-Reference: Papers → Thesis Sections

### §3.x — Parameter-Efficient Fine-Tuning
Covers original PEFT methods (LoRA, adapters, prefix-tuning) and their surveys.

**Papers:** `PEFT-method/lora.md` · `PEFT-method/qlora.md` · `PEFT-method/prefix-tuning.md` · `PEFT-method/adapter-tuning-effectiveness.md` · `PEFT-method/prefix-prompt-tuning.md` · `survey/peft-survey.md` · `survey/lora-survey.md` · `survey/bitfit.md`

### §4.x — Adapter Sharing and Composition
Covers composition methods: AdapterFusion, hypernetworks, gated composition.

**Papers:** `adapter-composition/adapterfusion-pfeiffer2020.md` · `adapter-composition/hyperpelt-karimi2022.md` · `adapter-composition/mad-g-pfeiffer2021.md` · `adapter-composition/unipelt-mao2022.md` · `adapter-composition/mad-x-pfeiffer2020.md` · `adapter-composition/adapters-library-2023.md` · `adapter-composition/lora-retriever-2024.md` · `MoE-adapter-routing/MixLoRA.md` · `MoE-adapter-routing/Mixture_of_LoRA_Experts.md`

### §5.x — Inference Serving Systems
Adapter inference serving: multi-tenant batching, CPU/GPU management, tiered memory.

**Papers:** `adapter-serving/S-LoRA.md` · `adapter-serving/Punica.md` · `adapter-serving/CaraServe.md` · `adapter-serving/EdgeLoRA.md` · `adapter-serving/Compress-then-Serve.md` · `adapter-serving/FLashServe.md` · `adapter-serving/Heterogeneous-LoRA-Serving.md` · `adapter-serving/Chameleon.md` · `adapter-serving/Predictive-LoRA.md` · `distributed-inference/edgeshard.md` · `distributed-inference/pagedattention.md` · `survey/orca.md`

### §6.x — P2P and Decentralized Learning
Covers P2P topology, FL, federation with privacy, distributed fine-tuning.

**Papers:** `P2P-DL/petals.md` · `P2P-DL/collaborative-deep-learning-fixed-topology.md` · `P2P-DL/decentralized-collaborative-learning-personalized.md` · `P2P-FL/decentralized-fl-unreliable.md` · `P2P-FL/p2p-federated-learning.md` · `P2P-FL/federated-split-learning.md` · `P2P-FL/federated-learning-cooperating-devices.md` · `federated-PEFT/flora.md` · `federated-PEFT/slora.md` · `federated-PEFT/fedex-lora.md` · `federated-PEFT/fedlora-wireless.md` · `federated-PEFT/dp-fedlora.md` · `gossip-learning/gossip-learning-alternative.md` · `foundational-P2P/kademlia.md`

### §7.x — MoE and Adapter Routing
Covers gating mechanisms, expert selection, routing strategies.

**Papers:** `MoE-adapter-routing/LoRAMoE.md` · `MoE-adapter-routing/MOELoRA.md` · `MoE-adapter-routing/MiLoRA.md` · `MoE-adapter-routing/Mixture-of-LoRAs.md` · `MoE-adapter-routing/When_MoE_Meets_LLMs.md` · `MoE-routing/switch-transformers.md` · `MoE-routing/crowdsourced-decentralized-moe.md`

### §9.x — PoC: NL-to-SQL
No papers directly mapping to this yet — these are foundational instead.

### §10.x — Conclusion / Synthesis
Covered by surveys and the thesis's own gap analysis.

## Cross-Reference: Papers → Contribution Codes

| Contribution Code | Supporting Papers |
|---|---|
| **★A1** (DHT-based discovery) | `foundational-P2P/kademlia.md` · `P2P-DL/decentralized-lora-llm.md` · `survey/p2p-deep-learning-connection-establishment.md` |
| **★S1** (P2P adapter marketplace) | `adapter-composition/lora-retriever-2024.md` · `federated-PEFT/fedbiot.md` · `adapter-serving/adapterhub.md` |
| **★R1** (capability embeddings) | `MoE-adapter-routing/LoRAMoE.md` · `adapter-composition/mad-g-pfeiffer2021.md` |
| **★M2** (decentralized composition) | `adapter-composition/adapterfusion-pfeiffer2020.md` · `federated-PEFT/fedmcp.md` |
| **★T2** (theoretical bounds) | `adapter-composition/expressive-power-lora-2023.md` |
| **Privacy / security** | `federated-PEFT/dp-fedlora.md` · `federated-PEFT/improving-lora-privacy.md` · `P2P-FL/federated-split-learning.md` |

## Key Cross-Cutting Gaps

For all 116 papers, the following gap is consistent across the entire literature:

1. **No P2P adapter discovery** — every paper assumes centralized orchestration
2. **No peer scoring** — no reputation or trust mechanism for adapter quality
3. **No cross-node retrieval** — adapters are assumed to be co-located with the frozen backbone
4. **Static configurations** — no dynamic composition based on task embeddings
5. **No incentive mechanisms** — no token or credit-based exchange
6. **Synchronous aggregation** — in both FL and P2P scenarios, updates are synchronous