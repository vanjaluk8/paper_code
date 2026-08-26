## Meta
- **Citation:** Li, T., Sahu, A. K., Zaheer, M., Sanjabi, M., Talwalkar, A., & Smith, V. (2020). Federated Optimization in Heterogeneous Networks. *MLSys*.
- **Venue:** MLSys 2020
- **Tags:** FedProx, Federated Learning, FL, Heterogeneity, Proximal

## Key Findings
1. PDF NOT FOUND: this paper was not in the PDF collection.
2. FedProx extends FedAvg by adding a proximal term to the client objective to handle systems and data heterogeneity.
3. Non-IID: constrains clients to remain close to the global model via L2 regularization (prox term).
4. Partial sharing: allows variable number of local epochs per client (partial work).
5. Aggregation: same averaging as FedAvg but each client can share multiple local updates with FedProx constraint.

## Relevance to Thesis (Specifically Mentioned Thesis Gap: §6.1 FL Foundations)
- FedProx is the key follow-up to FedAvg addressing the critical challenge of system and data heterogeneity.
- For decentralized adapter composition: statistical heterogeneity problem may be reduced via prox-terminology client updates.
- P2P environment: each peer may have non-IID data — FedProx's proximal term could constrain each peer's adapter from deviating too far.

## Key Metrics / Results
- Directly outperforms FedAvg by 1-5% in test accuracy across tasks, ResNet across data distributions.

## Limitations / Gaps
- Still centralized (central aggregator for model averaging).
- Not designed for LoRA adapters (static model-copy).
- Only experiment across my data distribution.

## How to Write for Thesis
- Use for thesis §6.1 FL Foundations: contrast with P2P approach.
- §6.2 discusses FedProx as baseline for non-IID adapter training.

## Relevance to Thesis Sections
- §6.1 Federated Learning Foundations