---
citation: "Heterogeneous LoRA for Federated Fine-tuning of On-Device Foundation Models." EMNLP 2024.
tags:
  - federated-PEFT
  - heterogeneous-lora
thesis-sections: §6.1, §6.2
tier: 1
paper-key: hetero-lora-ondevice
---

## Meta
- **Full citation:** "Heterogeneous LoRA for Federated Fine-tuning of On-Device Foundation Models," in Proc. EMNLP 2024.
- **Venue:** EMNLP 2024
- **Tags:** `federated-PEFT` `heterogeneous-loRA` `on-device`
- **Thesis sections:** §6.1, §6.2

## Key Findings
1. Proposes HetLoRA — allows clients to use different LoRA ranks based on local resource availability.
2. Server-side "tensor completion" step reconstructs full low-rank structure from partial LoRA updates.
3. Non-IID performance gains via heterogeneous rank.

## Methodology
- **Approach:** Clients with high resources (more compute/memory) use higher LoRA rank, lower resource clients use smaller rank.
- **Server side:** Server reconstructs LoRA weight, using masking or low-rank completion.
- **Aggregation:** Weighted aggregation where rank contributes to weight.
- **Base model:** Llama/LLaMA.

## Results / Metrics
- HetLoRA outperforms homogeneous single-rank baselines on GLUE / few-shot.
- Memory usage per client reduced up to 50% compared to full fine-tuning.

## Limitations / Gaps
- Central server required.
- Reconstruction of LoRA from clients expensive.

## Federation / Peer-to-Peer Approach
- Centralized FL — knowledge transferred via server aggregation and tensor completion.

## Relevance to Thesis
- Important: demonstrates that heterogeneous adapter structure is viable across clients.
- In P2P, adapters with different ranks can be exchanged and re-weighted.
- Completion / weighting necessary when aggregating from heterogeneous sources.

## Limitations / Gaps (continued)
- Aggregation complexity.
- Does not consider P2P.