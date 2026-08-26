## Meta
- **Citation:** Savazzi, S., Nicoli, M., & Rampa, V. (2020). Federated Learning With Cooperating Devices: A Consensus Approach. *IEEE Internet of Things Journal*.
- **Venue:** IEEE IoT
- **Tags:** P2P Federated Learning, Consensus, Edge Collaboration, IoT
- **Thesis sections:** §6.1 Federated Learning, §5.3 Consensus

## Key Findings
1. Federated learning through device-to-device cooperation only — no central server.
2. ADMM-based consensus: devices alternately perform local optimization and then solve local consensus problems with neighbors.
3. Provides convergence and privacy bounds even when nodes do not trust each other — each device only sees neighbor aggregated model differences (not individual data).
4. Bandwidth analysis: P2P communication overhead is linear in number of nodes, not all-to-all.
5. Tested on image classification (MNIST, CIFAR-10) with 10-50 edge devices with limited training rounds.

## Relevance to Thesis
- ADMM-based consensus optimization could be transferred to adapter sharing: each peer agrees on global adapter base weight but retains local dataset-specific adaptation.
- No central aggregator means fully decentralized adapter storage and policy — mirrors the P2P adapter marketplace.
- Privacy bound is highly relevant: assures that sharing adapter weights does not leak training data.
- Device-to-device edge collaboration maps to heterogeneous edge devices sharing adapters (laptop, phone, server).

## Limitations / Gaps
- Model sizes: up to few MB parameter models only (small CNNs).
- ADMM introduces hyper-parameter overhead: penalty factor influences data privacy and convergence speed.
- Assumes fixed network topology; no mobility or dynamic connection handling.
- All devices have homogeneous compute capability assumed.
- 3x more local training rounds required vs. centralized SGD.