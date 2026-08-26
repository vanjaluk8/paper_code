---
citation: Wei et al. "Federated Low-Rank Adaptation for Large Models Fine-Tuning Over Wireless Networks." IEEE GLOBECOM, 2024.
tags:
  - federated-PEFT
  - wireless-federated
thesis-sections: §6.1, §6.2
tier: 2
paper-key: fedlora-wireless
---

## Meta
- **Full citation:** W. Wei et al., "Federated Low-Rank Adaptation for Large Models Fine-Tuning Over Wireless Networks," in Proc. IEEE GLOBECOM, Cape Town, South Africa, 2024, pp. 1–6.
- **Venue:** IEEE GLOBECOM 2024
- **Tags:** `federated-PEFT` `wireless` `resource-constraint`
- **Thesis sections:** §6.1, §6.2

## Key Findings
1. Proposes FedLoRA — a scheme combining LoRA with over-the-air (OTA) aggregation over wireless networks.
2. Designs a specific power allocation strategy for wireless transmission of LoRA adapters.
3. Shows that transmitting only LoRA adapters (rather than full model weights) saves bandwidth in the uplink.
4. Achieves ~95% of the accuracy of centralized fine-tuning while significantly reducing communication overhead.

## Methodology
- **Base model:** RoBERTa-base (with LoRA for GLUE tasks)
- **Aggregation:** Federated averaging of LoRA *gradients* over the wireless channel using analog aggregation (OTA computation).
- **Wireless model:** Simulates Rayleigh fading channels; considers signal and noise in transmission.
- **Communication budget:** LoRA reduces uplink transmission per round compared to full fine-tuning.

## Results / Metrics
- Accuracy close to centralized fine-tuning on several GLUE tasks.
- Communication overhead is O(1) per device per round.
- Performance mildly degrades under poor channel conditions (low SNR).

## Limitations / Gaps
- Only evaluated on RoBERTa-base — not on larger (LLM-scale) models.
- Wireless simulation only, not real deployment on resource-constrained edge devices.
- Does not consider heterogeneous client capabilities (all clients run identical LoRA rank).

## Federation / Peer-to-Peer Approach
- Standard server-aggregator federated architecture.
- LoRA adapters are communicated via the aggregation server (not P2P).
- Over-the-air computation merges communication and computation steps.

## Relevance to Thesis
- Demonstrates a concrete bandwidth advantage of sending only LoRA adapters over full models.
- Highlights how wireless-specific challenges (fading, noise) impact communication.
- Still relies on a central parameter server — not P2P.

## Limitations / Gaps (continued)
- No privacy analysis beyond implicit LoRA gradient compression.
- Does not consider multi-task heterogeneity.
- Client selection under channel dynamics is not explored.
- No evaluation of system-level energy consumption on devices.