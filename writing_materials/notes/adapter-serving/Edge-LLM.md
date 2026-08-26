## Meta
- **Citation:** Edge-LLM: A Collaborative Framework for Large Language Model Serving in Edge Computing (ICWS 2024)
- **Venue:** IEEE ICWS 2024
- **Tags:** `adapter-serving` `edge-computing` `collaborative-inference` `distributed`
- **Thesis sections:** §5.x, §6.x

## Key Findings
1. Proposes a collaborative edge framework for LLM serving across edge devices with heterogeneous hardware.
2. Uses a centralized orchestrator that dispatches inference tasks to edge nodes, splitting layers across devices.
3. Adapts model parallelism to available edge device resources — splits transformer layers across multiple edge nodes.
4. Achieves latency reduction compared to local inference on resource-constrained devices.
5. Handles dynamic network conditions with adaptive task offloading strategies.

## Relevance to Thesis
- Highly relevant to P2P perspective: addresses distributed LLM inference across resource-heterogeneous devices.
- However, the architecture is _orchestrator-centric_ — a central controller assigns workloads, rather than autonomous P2P discovery and negotiation.
- The collaborative layer-splitting approach could inform the "P2P cooperation" dimension in our proposed marketplace.
- Edge latency constraints directly relate to fetching adapters from peers in a P2P adapter marketplace — network conditions matter.

## Limitations / Gaps
- Centralized orchestrator is the single point of control and failure — opposite of a decentralized architecture.
- Assumes all devices trust the central orchestrator and each other — no adversarial model.
- Layer splitting across edge nodes introduces inter-node communication overhead that grows with model size — not evaluated for 7B+ models.
- No adapter sharing or specialization — each edge node runs the same base model and inference, losing the benefit of P2P adapter diversity.
- Limited to collaborative _inference_ only — does not handle adapter or model fine-tuning.