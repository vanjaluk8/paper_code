## Meta
- **Citation:** He, C., et al. (2022). Decentralized Federated Learning With Unreliable Communications. *IEEE Journal of Selected Topics in Signal Processing*.
- **Venue:** IEEE JSTSP
- **Tags:** Decentralized FL, Communication Failures, Unreliable Networks, P2P
- **Thesis sections:** §6.2 Decentralized FL, §5.5 Reliable P2P Communication

## Key Findings
1. D-SGD for decentralized federated learning tolerating unreliable communication channels: dropped packets, delayed updates, peer failures.
2. Mathematical analysis of convergence bounds for D-SGD under unreliable communication: the impact of packet drops on consensus.
3. Peers use gossip averaging with relaxed consistency requirements — they average their model with neighbor updates but accept that some updates may be outdated or lost.
4. Convergence guarantee: if <50% of peers drop updates per round, convergence is still expected, though slower.
5. "Blind" gossipping used along with local SGD to prevent divergence when some peers update slowly.

## Relevance to Thesis
- Relaxed consensus tolerance is critical for P2P adapter marketplace reliability — adapters from peers disappearing or dropping updates are addressed.
- Packet loss analysis and straggler peer handling are directly relevant for the network adversary model for P2P sharing.
- Demonstrates that full consensus is not required for convergence — adaptation to adapter-sharing systems.

## Limitations / Gaps
- Theoretical convergence guarantees under convex objectives only.
- Validated on small-scale models (CNNs and ResNets) — not on large language models.
- Analyzes only degraded performance, not unrecoverable failures (churn) which are more severe.
- Packet drops only part of the adversary model — no Byzantine attacks.