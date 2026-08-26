---
citation: Federated Adaptive Fine-Tuning of Large Language Models with Heterogeneous Quantization and LoRA. IEEE INFOCOM, 2025.
tags:
  - federated-PEFT
  - heterogeneous
thesis-sections: §6.1, §6.2
tier: 1
paper-key: fed-adaptive-quant
---

## Meta
- **Full citation:** "Federated Adaptive Fine-Tuning of Large Language Models with Heterogeneous Quantization and LoRA," in Proc. IEEE INFOCOM, 2025.
- **Venue:** IEEE INFOCOM 2025
- **Tags:** `federated-PEFT` `heterogeneous-quantization` `resource-heterogeneity`
- **Thesis sections:** §6.1, §6.2

## Key Findings
1. Combines mixed-precision quantization of the base model with LoRA for heterogeneous edge devices.
2. Clients choose per-layer quantization levels based on their capability profiles.
3. Global LoRA adapters aggregated via standard FedAvg over all clients regardless of local quantization choices.
4. Significant communication & memory reduction while maintaining accuracy.

## Methodology
- **Approach:** Each client quantizes the base model heterogeneously (FP32, FP16, INT8), then trains LoRA on the quantized backbone.
- **Base model:** Llama-like model quantized to different precision per client.
- **Aggregation:** Server aggregates only the LoRA parameters (which are always FP32).
- **Personalization:** Each client's quantized backbone(varies) + shared global LoRA.

## Results / Metrics
- Up to 4x memory reduction on constrained devices.
- Accuracy degradation minimal (<1%) compared to unquantized LoRA finetuning.
- Communication volume unaffected by quantization since only LoRA weights are sent.

## Limitations / Gaps
- Requires a coordination server for aggregation.
- No mechanism to share adapters selectively — all global LoRA updated equally.
- Does not consider differential privacy or security.

## Federation / Peer-to-Peer Approach
- Fully centralized — a key mismatch with our P2P marketplace which aims to eliminate the server.
- Heterogeneity in base model capabilities is acknowledged and managed via client-aware quantization assignment.

## Relevance to Thesis
- Shows that heterogeneous clients can be accommodated by varying base-model precision while keeping LoRA standardized.
- Supports the idea that sharing only LoRA weights at reduced frequency could enable decentralized scenarios.
- Suggests adapter-based aggregation methods are practical for cross-device FL.

## Limitations / Gaps (continued)
- P2P decentralized adapter exchange not addressed.
- Limited to supervised text classification datasets.
- No evaluation on ground truth non-IID tasks — manually partitioned.