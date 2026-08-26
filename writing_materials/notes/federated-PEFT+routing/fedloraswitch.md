## Meta
- **Citation:** Chen, Z., et al. (2025). FedLoRASwitch: Efficient Federated Learning via LoRA Expert Hotswapping and Routing. *IEEE FLTA*.
- **Venue:** IEEE FLTA
- **Tags:** Federated LoRA, Expert Routing, Hotswapping, PEFT, FL
- **Thesis sections:** §6.2 Decentralized LoRA Fine-tuning, §7.2 Routing Adapters

## Key Findings
1. FedLoRASwitch: each FL client fine-tunes a set of LoRA "experts" on local data, then uploads to central server.
2. Server aggregates and routes experts for inference tasks using dynamic routing (choose best expert/model for each query).
3. Hotswapping: routers can replace experts on the fly without affecting other deployed experts — modular, plug-and-play.
4. Communication: send only LoRA weight updates (few MBs), not full model.
5. Evaluated across text and conversational tasks — matches performance of centralized LoRA with lower communication overhead.
6. Adds "expert routing layer" to assign query to the best expert (adapter) based on embedding similarity.

## Relevance to Thesis
- Adapter-level expert selection directly analogous to P2P adapter marketplace: each client is a potential seller, server routes buyers.
- Hotswapping: the idea of enabling and disabling adapters without downtime — critical for dynamic market switching between adapters.
- Routing layer selects expert: adapter marketplace can use this (similar to classifier routing) to direct inference request to the best peer.

## Limitations / Gaps
- Server-based system with central router, not P2P.
- Expert aggregation only on server; no model sharing between non-server nodes.
- Evaluated only with LoRA adapters on BERT-based models — not very large LLMs.