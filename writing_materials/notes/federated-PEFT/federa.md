---
citation: "FeDeRA: Efficient Fine-tuning of Language Models in Federated Settings." ArXiv, 2024.
tags:
  - federated-PEFT
  - FeDeRA
thesis-sections: §6.2, §6.3
tier: 2
paper-key: federa
---

## Meta
- **Full citation:** "FeDeRA: Efficient Fine-tuning of Language Models in Federated Settings," arXiv preprint arXiv:2404.18848, 2024.
- **Venue:** ArXiv 2024
- **Tags:** `federated-PEFT` `FeDeRA` `distribution-aware`
- **Thesis sections:** §6.2, §6.3

## Key Findings
1. Proposes FeDeRA — adapters with distribution-aware FL fine-tuning.
2. Server uses the distribution of client data to better guide adapter aggregation.
3. Weighted aggregation of LoRA adapters based on local distribution.

## Methodology
- **Approach:** Weighted averaging of LoRA updates based on client data distribution (as sample count proxy).
- **Base model:** BERT, RoBERTa.
- **Aggregation:** Weighted aggregated — larger data proportion gets higher weight aggregate.

## Results / Metrics
- Minor accuracy gain vs uniform aggregation.

## Limitations / Gaps
- Client distribution is estimated — overhead.
- Centralized server for aggregation.
- Distorted if clients lie.

## Federation / Peer-to-Peer Approach
- Centralized

## Relevance to Thesis
- Weights are assigned to each LoRA based on proxy distribution -> in P2P, each peer can compute its own weight based on local info.

## Limitations / Gaps (continued)
- Under non-IID, weighted aggregation does not fully solve.

Note: No additional gaps available.