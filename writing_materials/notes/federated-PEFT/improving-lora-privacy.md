---
citation: "Improving LoRA in Privacy-preserving Federated Learning." ArXiv, 2024.
tags:
  - federated-PEFT
  - privacy-preserving
thesis-sections: §6.2, §6.3
tier: 2
paper-key: improving-lora-privacy
---

## Meta
- **Full citation:** "Improving LoRA in Privacy-preserving Federated Learning," arXiv preprint arXiv:2403.12313, 2024.
- **Venue:** ArXiv 2024
- **Tags:** `federated-PEFT` `privacy-preserving` `LoRA`
- **Thesis sections:** §6.2, §6.3

## Key Findings
1. Investigates whether LoRA is privacy-preserving enough for FL.
2. Shows that naive LoRA+FL leaks membership information (gradient leakage).
3. Proposes adding calibrated noise (DP) to local LoRA updates.
4. Demonstrates improved defense against gradient inversion attacks.

## Methodology
- **Approach:** Apply Gaussian noise to LoRA gradients directly.
- **Base model:** GPT-2 / RoBERTa, text classification datasets.
- **Privacy mechanism:** DP with Matrix-Variate Gaussian noise over LoRA updates.

## Results / Metrics
- Privacy-utility trade-off: lower rank helps privacy but hurts accuracy.

## Limitations / Gaps
- Privacy guarantee relies on DP noise + central server honesty.

## Federation / Peer-to-Peer Approach
- Centralized — server would aggregate with added noise.

## Relevance to Thesis
- Important reference — shows naive LoRA does not guarantee privacy, but can be enhanced.
- Relevant to the P2P marketplace: peers exchanging adapters locally would need DP guarantees per exchange.

## Limitations / Gaps (continued)
- No decentralized aggregation with DP.
- Only BERT-size models considered.