## Meta
- **Citation:** Yi, L., et al. (2024). DLoRA: Distributed Parameter-Efficient Fine-Tuning Solution. *arXiv:2404.05182*.
- **Venue:** Preprint
- **Tags:** Distributed LoRA, Distributed PEFT, Model Parallelism, Adapter Synchronization
- **Thesis sections:** §4.2 LoRA, §3.2 Distributed Training

## Key Findings
1. DLoRA distributes LoRA fine-tuning across multiple GPUs: each GPU hosts a full base model shared across all tasks but holds a unique shard across both base blocks and LoRA.
2. Two-phase: forward pass shared across layers then swapped; reduce all average partial updates into final adapter/weights.
3. Communication: all-reduce across GPUs for LoRA gradient parameters (2*rank*small) not full weight — approximately 10x less than full gradient exchange.
4. Single node multi-GPU only design.

## Relevance to Thesis
- Distributes adapter fine-tuning across compute nodes directly — each GPU trains its LoRA and shares gradients.
- LoRA gradients are communication efficient.
- Viable for coordinating multi-peer training of shared adaptive parameters.

## Limitations / Gaps
- Multi-GPU single node only — no P2P coordination over the network.
- Requires high-bandwidth interconnects (NVLink).
- Not designed for heterogeneous environments or peer churn.