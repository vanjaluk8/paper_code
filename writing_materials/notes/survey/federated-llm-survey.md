## Meta
- **Citation:** Wu, X., et al. (2025). A Survey on Federated Fine-tuning of Large Language Models. *arXiv:2503.12016*.
- **Venue:** Preprint
- **Tags:** Federated Fine-tuning, FL, LLM, PEFT
- **Thesis sections:** §6.1 Federated Learning, §7.2 PEFT Fine-tuning

## Key Findings
1. Exhaustive survey of fine-tuning LLMs in FL through taxonomizing methods: prompt tuning, adapters, PEFT hybrids (local training, aggregation, personalization).
2. Categorizes by FL scenario: standalone fine-tuning, collaborative prompt/adapter training.
3. Communication efficiency: federated PEFT reduces communication overhead by 10-100x compared to full fine-tuning, since only small adapter weights need transfer.
4. Categorizes methods: FedAdapter, FedPrompt, FedBasis (parameter decomposition), personalized methods.
5. Discusses security vulnerabilities: gradient leakage, backdoor attacks in federated PEFT.
6. Identifies open problems: cross-device heterogeneity, non-IID data distribution, incentive mechanisms for participation.

## Relevance to Thesis
- Comprehensive categorization of FL+PEFT methods serves as reference for selecting PEFT method in decentralized setting.
- Identifies adapter-based FL methods like FedAdapter that directly parallel the adapter marketplace concept.
- Non-IID and heterogeneity insights are directly applicable to P2P adapter marketplace diversity.
- Attacker model analysis informs security considerations for the adapter marketplace.

## Limitations / Gaps
- System purely federated, not P2P; assumes central aggregation server.
- No analysis of decentralized model among peers.
- Focus on training (fine-tuning) rather than inference/query serving.
- Does not cover runtime selection or routing of adapters (ad-hoc decision) important for marketplace.