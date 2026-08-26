## Meta
- **Citation:** Hegedus, I., Jelasity, M., Kocsis, M., & Vincze, B. (2019). Gossip Learning as a Decentralized Alternative to Federated Learning. *Euro-Par*.
- **Venue:** Euro-Par
- **Tags:** Gossip Learning, Federated Learning, Decentralized Learning, Adaptive Gossip
- **Thesis sections:** §5.4 Gossip Learning, §7.1 Decentralized Federated Learning

## Key Findings
1. Gossip Learning (GL): each node initiates peer sampling, averages parameters with selected neighbor — fully distributed.
2. Convergence 20-50% slower than FL in simulation, but due to communication constraints, GL benefits linearly with number of peers.
3. Scalable: adding peers does not validate performance by centralizing updates (no central server bottleneck).
4. Adaptive sampling: selecting peers by high estimated bandwidth improves convergence.
5. Low latency: each step only requires single message exchange with one peer.

## Relevance to Thesis
- GL represents the key approach for adapter sharing and averaging across fully distributed peers without central aggregator.
- Adaptive peer selection: select neighbors with "adapter storage" via DHT discovery.
- Scalable convergence for many peers in the adapter marketplace.

## Limitations / Gaps
- Parameter averaging only works if adapters share backbone architecture — loosely homogeneous.
- Peer departure during averaging iteration leads to training data loss.
- Limited evaluation scale — only simulation of 1000 processes, not real P2P network environment.