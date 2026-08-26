---
citation: "Aggregating Low Rank Adapters in Federated Fine-Tuning." IEEE FLTA, 2024.
tags:
  - federated-PEFT
  - adapter-aggregation
thesis-sections: §6.3
tier: 2
paper-key: aggregating-lora
---

## Meta
- **Full citation:** "Aggregating Low Rank Adapters in Federated Fine-Tuning," in Proc. IEEE FLTA (Federated Learning Technologies and Applications), 2024.
- **Venue:** IEEE FLTA 2024
- **Tags:** `federated-PEFT` `adapter-aggregation` `low-rank`
- **Thesis sections:** §6.3

## Key Findings
1. Investigates different aggregation strategies for LoRA adapters when aggregated through a server.
2. Evaluates average-vs-weighted-vs-selective aggregation of LoRA modules.
3. Demonstrates that weighted adaptive aggregation of LoRA matrices outperforms simple averaging of LoRA.

## Methodology
- **Approach:** Standard FL with LoRA, varying aggregation function.
- **Base model:** RoBERTa-base, fine-tuned on GLUE.
- **Aggregation strategies tested:** FedAvg, weighted fedavg, selective mask aggregation.
- **Evaluation:** Accuracy, convergence speed, communication volume.

## Results / Metrics
- Selective aggregation (only updated clients contribute) converges faster.
- Weighted fedavg reduces variance in non-IID settings.

## Limitations / Gaps
- Only centralized.
- No Byzantine resilience.

## Federation / Peer-to-Peer Approach
- Centralized — methodological insights apply.

## Relevance to Thesis
- Direct methodological comparison: in a P2P setting, we could selectively aggregate adapters from certain peers using importance/relevance weighting.
- Relevance weighting (similar to weighted LoRA aggregation) could be key in P2P marketplace (e.g., weighted adapter fusion based on peer reputation).

## Limitations / Gaps
- No security analysis.
- Small model scale.