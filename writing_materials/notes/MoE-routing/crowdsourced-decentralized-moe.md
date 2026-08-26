## Meta
- **Citation:** Belchior, R., et al. (2022). Towards Crowdsourced Training of Large Neural Networks using Decentralized Mixture-of-Experts. *ICDCS*.
- **Venue:** ICDCS
- **Tags:** Decentralized MoE, Crowdsourced Training, P2P, Split Computing
- **Thesis sections:** §6 Federated Learning & Collaborative Training, §3.2 Distributed Training, §7.1 MoE

## Key Findings
1. Proposes a decentralized system where peers contribute computation (not just data) to train large neural networks using MoE splitting.
2. Model is partitioned across peers: a shared (frozen) encoder is replicated to all clients; expert sub-modules are distributed to and trained by individual peers.
3. Peers are assigned to expert training via a dynamic, task-driven assignment protocol — peers train only the expert assigned to them.
4. Uses a DHT-indexed registry to track which peer holds which expert, with topology-aware assignment to reduce communication overhead.
5. Evaluated up to 16 peers with 160M parameter model; demonstrates bandwidth efficiency improvements over centralized alternatives, though with some loss of model quality at high peer counts.
6. Each peer trains a classifier on top of its assigned expert, creating a personalized classification head.

## Relevance to Thesis
- The closest prior work to the decentralized adapter vision: using P2P to distribute expert modules across peers.
- DHT-based registry for expert assignment provides a template for adapter discovery in a P2P adapter marketplace.
- Shows real-world implementation challenges (bandwidth, staleness, peer churn) directly applicable to adapter sharing networks.
- Identifies a proof-of-concept architecture: frozen shared backbone + distributed experts = personalized inference.

## Limitations / Gaps
- Only classification tasks evaluated (CIFAR-10, CIFAR-100, MNIST) — not LLM/NLP tasks.
- Relies on centralized index for peer-expert mapping (DHT registry) which is a single point of coordination if not fully decentralized.
- No privacy analysis — expert weight sharing leaks information about the training data.
- Only 16 peers evaluated; scaling to hundreds of peers likely hits communication bottlenecks.
- Adapters are 2-layer MLPs; not PEFT methods like LoRA.