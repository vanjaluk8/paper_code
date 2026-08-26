## Meta
- **Citation:** Wang, Z., et al. (2024). FederatedScope-LLM: A Comprehensive Package for Fine-tuning Large Language Models in Federated Learning. *SIGMOD*.
- **Venue:** SIGMOD
- **Tags:** Federated Learning, LLM, PEFT, System, Framework
- **Thesis sections:** §6.1 Federated Learning, §7.2 FL+LLM Systems

## Key Findings
1. FederatedScope-LLM is a modular framework that integrates PEFT with FL — supports LoRA, adapters, prompt tuning as trainable modules.
2. Communication: adapters (LoRA weights) sent wire-format compressed — 10-100x reduction vs full gradient/weight uploads.
3. Integration shows that PEFT+FL yields near-centralized performance.
4. Plug-and-play design enables different PEFT methods and optimization strategies.

## Relevance to Thesis
- System design of PEFT modules in FL directly maps to adapter distribution: each adapter treated as discrete modules.
- Communication compression similar to the need for low-bandwidth adapter transfer in P2P marketplace.
- Modular design pattern applicable to a decentralized adapter serving awareness.

## Limitations / Gaps
- Central aggregator design: not P2P or decentralized.
- The focus is on standardized training/fine-tuning, not on serving inference requests.
- No support for runtime adapter switching or peer-to-peer exchange of adapter modules.
- All participants assumed trusted and stable — no Byzantine or churn tolerance.