---
citation: Zhang et al. "FedPETuning: When Federated Learning Meets the Parameter-Efficient Fine-Tuning of Large Language Models." ACL 2023 Findings.
tags:
  - federated-PEFT
  - FedPETuning
thesis-sections: §6.2, §6.3
tier: 1
paper-key: fedpetuning
---

## Meta
- **Full citation:** Z. Zhang et al., "FedPETuning: When Federated Learning Meets the Parameter-Efficient Fine-Tuning of Large Language Models," in Findings of ACL, 2023, pp. 632–647.
- **Venue:** ACL 2023 Findings
- **Tags:** `federated-PEFT` `FedPETuning` `Seminal`
- **Thesis sections:** §6.2, §6.3

## Key Findings
1. Pioneers combination of FedPETuning (Federated + PEFT + tuning) in cross-silo FL of LLMs.
2. Tests LoRA, prefix tuning, and adapter methods integrated with FedAvg.
3. Shows PEFT performs closer to full fine-tuning under federated scenarios with limited communication budget.
4. Adapters and LoRA outperform prefix tuning in non-IID splitting of text classification datasets.

## Methodology
- **Base model:** RoBERTa-base / GPT-2.
- **PEFT methods:** LoRA, prefix tuning, adapter layers.
- **Non-IID partitions:** Dirichlet distribution across clients.
- **Aggregation:** FedAvg on the small adapter parameters.
- **Communication efficiency:** adapter-only exchange reduces overhead.

## Results / Metrics
- Adapters and LoRA consistently beat FedAvg (full model) on long-tail task distributions.
- 90%+ my communication savings, 1-5% accuracy loss vs centralized PEFT.

## Limitations / Gaps
- Central server aggregator.
- Limited to cross-silo, no cross-device results.
<Extra>Notable as first systematic study of FedPETuning — foundational for all follow-ups.</Extra>

## Federation / Peer-to-Peer Approach
- Centralized server.

## Relevance to Thesis
- FedPETuning is the foundation for RQs about PEFT in FL.
- Directly shows adapters are sufficient for FL — hence decentralized exchange of adapters (rather than raw updates) is promising.

## Limitations / Gaps (continued)
- No privacy mechanism.
- Heterogeneous client resources ignored.