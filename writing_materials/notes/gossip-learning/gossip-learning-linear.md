## Meta
- **Citation:** Hegedus, I., Jelasity, M. (2020). Gossip Learning with Linear Models on Fully Distributed Data. *Concurrency and Computation: Practice and Experience*.
- **Venue**: Concurrency and Computation
- **Tags:** Gossip Learning, Linear Models, Decentralized ML, Fully Distributed
- **Thesis sections:** §5.4 Gossip Learning, §6.3 Peer Sampling

## Key Findings
1. Gossip learning using peer sampling: each peer periodically selects a random peer, averaging local model parameters.
2. Linear model (SGD) validation on 1000 peers with non-IID data; converges to centralized baseline.
3. Key metric tracking: time-to-accuracy expressed as function of rounds.
4. Multiplicative pairwise averaging vs. uniform with decreasing step size.

## Relevance to Thesis
- Core algorithim for model adaptation exchange: peers averaging adapters expands to P2P averaging.
- Asynchronous content equivalence equivalent: node communication by averaging.

## Limitations / Gaps
- No deep learning (linear models only) — adding adapters to DL would test communication constraints.
- Peer union only highly uniform gossip.
- Little analysis of convergence under high churn.