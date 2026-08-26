## Meta
- **Citation:** Ryabinin, M., et al. (2025). Decentralized Low-Rank Fine-Tuning of Large Language Models. *arXiv:2501.15361*.
- **Venue:** Preprint
- **Tags:** P2P Fine-tuning, Decentralized LoRA, LLM, DHT
- **Thesis sections:** §6.2 Decentralized LoRA Fine-tuning, §9 PoC

## Key Findings
1. Extends Petals to support decentralized LoRA fine-tuning over a P2P network without any central coordinator.
2. Uses DHT for discovering model blocks and coordinating fine-tuning and inference across peers.
3. LoRA adapters are learned collaboratively across distributed peer resources — each peer trains on its data but contributes to shared adapter weights through aggregating updates via peer-to-peer averaging.
4. Peers maintain connection information with Kademlia-like DHT; adapters are identified by task type (e.g. text classification job).
5. Convergence is robust even with 10-20% random peer dropouts per round.
6. Experiments on BLOOM structure, fine-tuning classification tasks (IMDB sentiment, natural language inference).
7. Accuracy within 2-3% of centralized LoRA fine-tuning on GLUE-like tasks; latency scales as O(log N) for peer discovery using DHT.

## Relevance to Thesis
- **Core reference for the decentralized adapter marketplace thesis**: LoRA adapters discovered and shared exclusively through P2P network.
- DHT-based adapter discovery is the direct predecessor to the proposed decentralized adapter hub.
- Robustness to peer dropout directly addresses the real-world P2P failure challenge.
- Collaborative adapter weight aggregation across peers demonstrates feasibility of shared adapters implemented via P2P averaging.

## Limitations / Gaps
- Operates at the "model block" level for fine-tuning — still requires full visibility of the model structure across peers.
- Adapters aggregated network-wide, not independent per-cohort.
- Task-based routing only (e.g., "sentiment analysis") — no flexible routing per-user-request.
- Requires significant peer bandwidth for model block distribution during fine-tuning.
- No explicit adapter versioning or quality assurance mechanism.