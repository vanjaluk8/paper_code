---
citation: "FLoRA: Federated Fine-Tuning Large Language Models with Heterogeneous Resources." ArXiv, 2024.
tags:
  - federated-PEFT
  - FLoRA
thesis-sections: §6.2, §6.3
tier: 1
paper-key: flora
---

## Meta
- **Full citation:** "FLoRA: Federated Fine-Tuning Large Language Models with Heterogeneous Resources," arXiv preprint arXiv:2409.05976, 2024.
- **Venue:** ArXiv 2024
- **Tags:** `federated-PEFT` `FLoRA` `heterogeneous-resources`
- **Thesis sections:** §6.2, §6.3

## Key Findings
1. Proposes FLoRA — FedAvg on heterogeneous sizes of LoRA using weight truncation and padding to unify LoRA matrices across clients.
2. Based on SLoRA but uses rank-truncation mapping.
3. Each client exports a LoRA matrix of its resource-dependent size.
4. Global LoRA with fixed max rank is maintained.

## Methodology
- **Approach:** Server maintains a global matrix of max possible rank — each client's LoRA of different rank is broadcast / truncated to map to global for aggregation.
- **Base model:** Llama, evaluated on few-shot natural language tasks.
- **Aggregation:** FedAvg with dimension padding.

## Results / Metrics
- Outperforms homogeneous LoRA on non-IID.
- Convergence robust to different ranks.

## Limitations / Gaps
- Central server needed to manage global matrix.
- Communication volume high for high-ranked clients.

## Federation / Peer-to-Peer Approach
- Centralized.

## Relevance to Thesis
- Direct: PEFT communicates only LoRA -> P2P can exchange LoRA of varying ranks.
- Important if we want to implement cross-device P2P marketplace with rank-heterogeneous LoRA modules.
- Adapt to top-k selection of peers based on their LoRA "capabilities" or "compatibility score".

## Limitations / Gaps (continued)
- No Byzantine resilience or privacy layer.
- Heterogeneity limited to rank, ignoring base model quantization or non-linearities.