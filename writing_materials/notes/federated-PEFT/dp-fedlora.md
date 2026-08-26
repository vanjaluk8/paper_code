---
citation: Li et al. "DP-FedLoRA: Privacy-Enhanced Federated Fine-Tuning for On-Device Large Language Models." IEEE ICDM, 2025.
tags:
  - federated-PEFT
  - differential-privacy
thesis-sections: §6.2, §6.3
tier: 1
paper-key: dp-fedlora
---

## Meta
- **Full citation:** J. Li et al., "DP-FedLoRA: Privacy-Enhanced Federated Fine-Tuning for On-Device Large Language Models," in Proc. IEEE ICDM, Washington, DC, USA, 2025, pp. 1–8.
- **Venue:** IEEE ICDM 2025
- **Tags:** `federated-PEFT` `differential-privacy` `on-device`
- **Thesis sections:** §6.2, §6.3

## Key Findings
1. Combines LoRA with differential privacy guarantees for federated LLM fine-tuning.
2. Proposes DP-FedLoRA that adds Gaussian noise to local LoRA gradients before sharing.
3. Shows that DP-FedLoRA provides comparable privacy-utility trade-offs to full-model DP-FedAvg with significantly lower communication cost.
4. Demonstrates feasibility of DP-SGD style training at the adapter granularity.

## Methodology
- **Base model:** GPT-2 / LLAMA-like small models
- **Personalization:** MoE-like per-device router selecting among shared LoRA experts
- **Aggregation:** Secure aggregation of LoRA modules with differential privacy guarantees
- **Federated optimization:** FEDAvg aggregated LoRA updates combined with per-client DP mechanism

## Results / Metrics
- Comparable accuracy to non-DP federated methods across text classification tasks.
- Achieves (epsilon, delta = 8) privacy guarantee with small degradation (~1-2%).
- Model communication size reduced by >90% compared to full parameter exchange.

## Limitations / Gaps
- Limited evaluation scale (moderately sized models only).
- Only considers centralized DP aggregation — no decentralized aggregator.
- Guarantees degrade under low participation rates.

## Federation / Peer-to-Peer Approach
- Centralized FL with server-side aggregation.

## Relevance to Thesis
- Directly relevant — shows PEFT + DP is feasible in federated setting.
- Suggests a path towards private adapter exchange in P2P by disaggregating DP from the server (local DP mechanisms could be added before sharing adapters peer-to-peer).

## Limitations / Gaps (continued)
- Only investigates DP at the aggregated level, not P2P privacy.
- Heterogeneous client participation not addressed.
- No energy or latency profiling on mobile devices.