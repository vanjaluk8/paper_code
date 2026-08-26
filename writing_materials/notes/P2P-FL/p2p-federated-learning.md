## Meta
- **Citation:** Bellet, A., Guerraoui, R., Taziki, M., & Tommasi, M. (2021). An Approach for Peer-to-Peer Federated Learning. *DSN Workshops*.
- **Venue:** DSN Workshops
- **Tags:** P2P Federated Learning, Decentralized FL, Personalized Models
- **Thesis sections:** §6.1 Federated Learning, §6.2 Decentralized FL

## Key Findings
1. Proposes a fully P2P FL approach: no central server; peers cooperate in a decentralized manner to learn models through gossip protocol.
2. Each peer local model: baseline model + optional personalized tuning layer, informing local vs global performance trade-off.
3. Two-phase approach: first, use SGD-SMPC (secure multi-party computation) without revealing individual data to neighbors; second, choose between local model (personalized) or neighbor-shared models (collaboratively trained).
4. Communication of model parameters gradient updates via secure aggregation across the P2P network.
5. Achieves comparable accuracy to centralized FL (FedAvg) on benchmarks.

## Relevance to Thesis
- P2P FL replaces central FL aggregator — directly relevant for adapter-based P2P sharing without central authority.
- Personalized (two-phase) approach directly supports the diversity in the marketplace.

## Limitations / Gaps
- Assumes all peers have identical architecture: full-model-level FL — adapters not applicable.
- No support for heterogeneous model weights much larger P2P sharing market.
- Not measured for large-scale transformer models.
- Relies on two-phase approach that requires additional communication rounds by majority.