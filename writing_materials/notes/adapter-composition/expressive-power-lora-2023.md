## Meta
- **Citation:** (2023). The Expressive Power of Low-Rank Adaptation.
- **Venue:** Pre-print (arXiv:2310.17513)
- **Tags:** `adapter-composition` `loRA` `theoretical`
- **Thesis sections:** §3 (theoretical analysis of PEFT expressivity), §2 (deep learning background)

## Key Findings
1. Formal theoretical analysis comparing the expressive power of LoRA versus full fine-tuning.
2. Proves that LoRA can approximate any weight update achieved by full fine-tuning provided that the rank budget is sufficiently large, with formal bounds on rank requirements.
3. Defines strict separation conditions between full fine-tuning and low-rank adaptation, providing precise rank requirements for task adaptation.
4. Provides theoretical guarantees that low-rank adaptation can simulate fine-tuning at the model level.

## Composition Method
- Not a composition paper; purely theoretical analysis of expressive capabilities of low-rank adaptation.

## Relevance to Thesis
- Theoretical underpinning for why PEFT (LoRA) is as expressive as full FT within enough rank.
- Justifies the choice of adapter approaches in decentralized settings.

## Limitations / Gaps
- Does not propose any composition method or mechanism for combining multiple adapters.
- Theoretical; missing experimental validation of composition in a P2P setting.