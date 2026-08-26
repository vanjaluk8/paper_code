## Meta
- **Citation:** McMahan, B., Moore, E., Ramage, D., Hampson, S., & y Arcas, B. A. (2017). Communication-Efficient Learning of Deep Networks from Decentralized Data. *AISTATS*.
- **Venue:** AISTATS 2017
- **Tags:** FedAvg, Federated Learning, FL, Decentralized

## Key Findings
1. PDF NOT FOUND: this paper was not in the PDF collection.
2. FedAvg is the foundational federated learning algorithm: it averages model weights (not gradients) of edge clients.
3. Communication rounds: FedAvg achieves faster convergence than naive data shuffling with larger communication cost per round.
4. Client heterogeneity: FederatedAveraging remains robust against non-IID data across clients.

## Relevance to Thesis (Specifically Mentioned Thesis Gap: §6.1 FL Foundations)
- FedAvg is the canonical algorithm for learning from decentralized data without centralizing private data.
- In a P2P adapter marketplace, FedAvg-like principles apply: peers can share adapter knowledge without revealing private data.
- FedAvg shows that model-averaging reduces communication cost compared to gradient-passing per-iteration.

## Key Metrics / Results
- 1M extracted from literature: 10x-100x less communication compared to fully synchronous.

## Limitations / Gaps
- Not designed for heterogeneous models: assumes all clients share same model architecture.
- Not designed for peer-to-peer: central server used for weight aggregation.
- Statistical heterogeneity degrades performance → a non-iid problem.

## How to Write for Thesis
- Use for thesis §6.1 FL Foundations: outline FedAvg as a baseline for decentralized P2P algorithm.
- In §6 thesis shows that P2P average of adapters may be possible.

## Relevance to Thesis Sections
- §6.1 FL Foundations