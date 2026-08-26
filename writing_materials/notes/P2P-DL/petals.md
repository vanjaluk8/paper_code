## Meta
- **Citation:** Borzunov, A., et al. (2023). Petals: Collaborative Inference and Fine-tuning of Large Models. *arXiv:2209.01188*.
- **Venue:** Preprint / MLSys 2023
- **Tags:** P2P Inference, Collaborative Computing, Bittorrent-style, Decentralized Fine-tuning
- **Thesis sections:** §3.2 Distributed Training, §6 Federated Learning, §9 PoC System Design

## Key Findings
1. Petals implements a BitTorrent-style P2P network for large transformer models (~176B parameters) where peers share GPU resources.
2. Model is split into "blocks" (transformer layers); each peer hosts a subset of blocks and serves either inference or fine-tuning requests.
3. Inference: routing with geolocation and throughput-awareness to select optimal peer blocks for a request.
4. Fine-tuning: parameter-efficient fine-tuning across the P2P network, supports LoRA adapters on specific blocks without moving data to a central server.
5. Participants contribute GPU/bandwidth resources to the network to earn "reputation" or access inference capabilities, forming an incentive mechanism.
6. Achieves near-central inference quality with latency benefits from intelligent routing.
7. Uses blockchain for peer identity and reward tracking.
8. Fine-tuning support via gradient checkpointing and pipelining across peers to reduce memory requirements.

## Relevance to Thesis
- **The most directly relevant P2P system** for the adapter marketplace concept — demonstrates a working decentralized training/inference ecosystem.
- Block-level partitioning of a model across peers for collaborative operation is the closest existing paradigm to MoE-style adapter distribution.
- LoRA-in-Petals shows that adapter-based fine-tuning integrates naturally with P2P models.
- Incentive/reputation mechanism essential for understanding economic viability of a P2P adapter marketplace.
- Petals is real: implemented and actively used, demonstrating feasibility of P2P LLM serving.

## Limitations / Gaps
- Tight coupling to a specific model architecture (BLOOM 176B) — not a general-purpose adapter marketplace.
- Performance degrades under high peer churn or low bandwidth (latency vs. centralized with caching at 2-3x slowdown reported).
- Reputation system is centralized on blockchain, not fully P2P.
- Communication bottleneck: every token generation step requires round trips across peer blocks — RTT overhead can be high.
- The adapter fine-tuning operates model-wide rather than per-task; adapters are not independently downloadable or replaceable.