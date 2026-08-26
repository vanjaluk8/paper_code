---
citation: "Towards Federated Low-Rank Adaptation of Language Models with Heterogeneous Data." NAACL 2025 Short.
tags:
  - federated-PEFT
  - heterogeneous-data
thesis-sections: §6.1, §6.2, §6.3
tier: 1
paper-key: towards-federated-lora
---

## Meta
- **Full citation:** "Towards Federated Low-Rank Adaptation of Language Models with Heterogeneous Data," in Proc. NAACL 2025 (Short).
- **Venue:** NAACL 2025
- **Tags:** `federated-PEFT` `heterogeneous-data` `LoRA`
- **Thesis sections:** §6.1, §6.2, §6.3

## Key Findings
1. Investigates non-IID across clients for PEFT + FL.
2. Shows that direct FedAvg of LoRA yields consistent high error due to misalignment of low-rank matrices across clients.
3. Proposes to align LoRA updates for a more consistent global model (by inducing invariance to reparameterization).
4. Better performance compared to default FedAvg.

## Methodology
- **Approach:** Clients train LoRA locally, then server aggregates with alignment step to reduce inconsistency.
- **Base model:** RoBERTa / Llama.
- **Evaluation:** GLUE.

## Results / Metrics
- 3% accuracy improvement on non-IID splits.

## Limitations / Gaps
- Central server required.
- Alignment steps add overhead.

## Federation / Peer-to-Peer Approach
- Centralized.

## Relevance to Thesis
- Important: LoRA updates are not invariant — different local LoRA directions can diverge — requiring alignment.
- P2P scenarios would need a similar alignment mechanism (via consensus or projection).

## Limitations / Gaps (continued)
- Not evaluated on generative or few-shot tasks.
- Overhead of alignment step not quantified on device.