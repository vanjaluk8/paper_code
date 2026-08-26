---
citation: "SplitLoRA: A Split Parameter-Efficient Fine-Tuning Framework." ArXiv, 2024.
tags:
  - federated-PEFT
  - split-learning
thesis-sections: §6.2
tier: 2
paper-key: splitlora
---

## Meta
- **Full citation:** "SplitLoRA: A Split Parameter-Efficient Fine-Tuning Framework," arXiv preprint arXiv:2407.00952, 2024.
- **Venue:** ArXiv 2024
- **Tags:** `federated-PEFT` `split-learning` `LoRA`
- **Thesis sections:** §6.2

## Key Findings
1. Proposes SplitLoRA — combines split learning with LoRA for FL.
2. Clients compute intermediate representations only and send activations.
3. Reduces client-side computation.

## Methodology
- **Approach:** Base model layers split: first few on client (small), last on server (large).
- **Base model:** ResNet, BERT.

## Results / Metrics
- Reduces client memory and computation vs full LoRA training locally.
- Slightly slower convergence due to communication per batch.

## Limitations / Gaps
- P2P not addressed.

## Federation / Peer-to-Peer Approach
- Centralized (server holds the second half). Not P2P.

## Relevance to Thesis
- Indirect: PEFT + split learning reduces on-device compute.
- LoRA as split vector -> adapters have more prominent role.
- Insight: P2P nodes could share hidden representations to reduce their compute.
- However, this approach relies on a central server hosting base model, which is different from our peer-only setting.

## Limitations / Gaps
- Relies on strong server with base model activation.