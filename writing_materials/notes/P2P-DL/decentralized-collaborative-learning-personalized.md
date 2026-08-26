## Meta
- **Citation:** Vanhaesebrouck, P., Bellet, A., & Tommasi, M. (2017). Decentralized Collaborative Learning of Personalized Models over Networks. *AISTATS*.
- **Venue:** AISTATS
- **Tags:** Decentralized Collaborative Learning, Personalized Models, P2P, Consensus
- **Thesis sections:** §6.2 Decentralized FL, §5.3 Personalized Models

## Key Findings
1. Formulates decentralized collaborative learning as a decentralized optimization problem over a graph: each peer minimizes its own empirical loss + regularization term that encourages similarity to neighbor models.
2. Proximal penalty: local model weights are penalized if they diverge too far from neighbor averages, balancing personalization against collaboration.
3. Convergence guarantees for convex models; experiments on synthetic and real data show that carefully tuned regularization outperforms both fully independent training and full-network averaging.
4. Communication efficiency trades off computation for communication rounds: fewer exchanges require more local training steps.
5. Peer selection for neighbor topology significantly affects system accuracy and convergence.

## Relevance to Thesis
- Personalized model learning over P2P networks — each peer learns a unique model but collaborates to improve via neighbor weight penalties.
- Can be interpreted as adapter-level training: each peer training its own adapter, with consensus penalties to peer sharing of similar adapters.
- Proximal penalty idea is relevant to adapter diversity (non-IID problem) in the marketplace.

## Limitations / Gaps
- Convex optimizations only — no analysis for deep networks or transformers.
- Proximal penalty requires careful tuning of regularization strength for each user.
- All nodes assumed honest — no Byzantine tolerance.
- Local computation assumed free compared to communication cost.
- Scale: evaluation with small models on small data only (200 dimensions, 5-50 peers).