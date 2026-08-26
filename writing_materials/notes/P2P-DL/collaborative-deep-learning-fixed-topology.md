## Meta
- **Citation:** Hegedus, I., Jelasity, M., Kertesz, A., Kocsis, M., & Vincze, B. (2020). Collaborative Deep Learning in Fixed Topology Networks. *Annals of Telecommunications*.
- **Venue:** Annals of Telecommunications
- **Tags:** P2P Collaborative Deep Learning, Fixed Topology, Decentralized DL, Node Failure
- **Thesis sections:** §6 Federated Learning & Collaborative Training, §5.2 P2P Communication Topologies

## Key Findings
1. Decentralized collaborative deep learning executed over fixed-topology P2P networks: each peer trains its own model using SGD on local data and periodically averages weights with neighbors.
2. Gossip protocol (peer sampling, distributed averaging) used for weight exchange — no central server required.
3. Experiments on MNIST and CIFAR-10 with 50 peers, measuring convergence time vs. gossip frequency.
4. Converges to comparable accuracy with centralized SGD, but requires specific parameter-tuning for gossip interval vs. model quality trade-offs.
5. Topology matters: regular random graphs converge faster than rings or highly clustered topologies.
6. Bandwidth bottleneck: each modality update cycle shares the full model weights — a significant bottleneck for large models.

## Relevance to Thesis
- Demonstrates model weight sharing as p2p gossip, not gradient sharing — relates to sharing trained adapters rather than training signal.
- Topology-aware experiments suggest DHT-based routing for adapter discovery could improve efficiency.
- Collaborative training over P2P shows feasibility but at bandwidth cost prohibitive for large models.

## Limitations / Gaps
- Full-model averaging, not adapter-level parameter sharing — extremely bandwidth intensive for LLM scales (communication of millions of parameters, not millions-of-billions).
- Homogeneous model assumption: all peers train identical model same architecture — target use-case does not allow specialization.
- Fixed-topology inherent peer availability — evaluates node failures only, not churn.
- Small models: MLPs and small CNNs (2-3 layers) not LLMs — scaling evaluation to transformer architectures is not completed.