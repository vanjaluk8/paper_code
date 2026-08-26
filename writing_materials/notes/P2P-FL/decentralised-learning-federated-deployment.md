## Meta
- **Citation:** Miao, Y., et al. (2020). Decentralised Learning in Federated Deployment Environments. *ACM CCSW'20*.
- **Venue:** ACM CCSW
- **Tags:** Decentralized FL, Wireless Networks, Heterogeneous Hardware
- **Thesis sections:** §6.2 Decentralized FL, §5.4 Heterogeneous Hardware and Devices

## Key Findings
1. Proposes a decentralised learning framework for federated environments without central aggregator using P2P model exchange.
2. Peers use wireless protocol to exchange model updates in a round-robin fashion.
3. Heterogeneous hardware support: some peers are slower; system adapts by tolerating updates that do not arrive within a threshold.
4. Uses topology-aware averaging: peer weights are inversely proportional to their communication distance to others.
5. Achieves comparable accuracy to FL with even mild packet loss; reduces energy consumption and latency vs. centralized aggregator.
6. Joint training on CIFAR-10 with 50 mobile RPi nodes.

## Relevance to Thesis
- P2P collaborative model aggregation without central server fits perfectly with the adapter marketplace.
- Heterogeneity tolerance directly addresses how peers with different compute capabilities contribute aggregator roles as "slow nodes."
- Energy/latency analysis applicable: similar model to mobile-edge computing for adapter exchange.

## Limitations / Gaps
- Full models trained, not adapters.
- Only small vision models (2 conv layers) — not applicable in transformer era.
- Peer discovery is assumed fixed and known (network of RPi devices with assigned addresses).
- Limited to 50 small devices, all identical hardware.