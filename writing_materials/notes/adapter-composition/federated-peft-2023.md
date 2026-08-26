## Meta
- **Citation:** Anonymous (2023). Client-Customized Adaptation for Parameter-Efficient Federated Learning.
- **Venue:** Findings of ACL 2023
- **Tags:** `adapter-composition` `federated-learning` `personalization`
- **Thesis sections:** §5 (federated PEFT), §7.1 (decentralized PEFT)

## Key Findings
1. Proposes pFLAT (personalized Federated Learning with AdapTers): each client fine-tunes adapters on its local data, which are aggregated via federated averaging on the server.
2. Personalization is achieved by balancing a globally shared set of adapter parameters with client-specific adapter layers.
3. Clients can deploy the global aggregation or their own client-specific fine-tuned adapter, achieving state-of-the-art personalization on NLP federated learning benchmarks.
4. The use of adapters drastically reduces per-client communication costs compared to full model fine-tuning.

## Composition Method
- A base Transformer model is shared globally. Local adapters are trained on client data. The server aggregates adapter parameters (via FedAvg) from participating clients.
- Two-level personalization: each client retains its locally trained adapter for inference, but the aggregated global adapter can also be downloaded for cold-start personalization.
- This enables non-conflicting per-client personalization.

## Relevance to Thesis
- Directly relevant to decentralized adapter orchestration -- shows that adapters from heterogeneous clients can be aggregated and composed.
- Provides a model for P2P adapter sharing as a potential server-based 'aggregation' step.
- Relevant to §5 and §7.1.

## Limitations / Gaps
- Requires a centralized server for aggregation -- not fully decentralized.
- Assumes all clients share the same base model; does not cover cross-model adapter composition.
- No exploration of open P2P discovery or routing of adapters.