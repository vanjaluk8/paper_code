## Meta
- **Citation:** Li et al. (2023) MOELoRA: An MOE-based Parameter Efficient Fine-Tuning Method
- **Venue:** ArXiv preprint (November 2023)
- **Tags:** `MoE-routing` `LoRA` `MOELoRA` `PEFT`
- **Thesis sections:** §7.x (MoE routing)

## Key Findings
1. MOELoRA introduces a mixture of LoRA-experts architecture where multiple low-rank matrices are combined via routing in Multi-Head Attention (MHA) outputs.
2. Each LoRA expert is assigned to different heads in attention; the router selects which experts to route which head tokens to.
3. Achieves better performance than standard LoRA and full fine-tuning on various NLP tasks.

## Routing / Gating Mechanism
- Gating is computed at the head level within each attention layer.
- The router assigns each input token to the top-k LoRA experts per attention head.
- Sparse top-k gating is used to keep negligible inference overhead.

## Relevance to Thesis
- Shows that LoRA decomposition can be used in an MoE setup with per-head routing.
- Could inspire how multiple adapters are composed per word token in a P2P context.

## Limitations / Gaps
- Routing decisions are centralised and global — not decentralised or peer-based.
- No mention of communication or protocol for distributed routing.