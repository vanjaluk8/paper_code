## Meta
- **Citation:** Zhou, Y., et al. (2022). Expert Choice in Mixture-of-Experts. *NeurIPS*.
- **Venue:** NeurIPS 2022
- **Tags:** Expert Choice, MoE, Routing, Mixture of Experts

## Key Findings
1. PDF NOT FOUND: this paper was not in the PDF collection.
2. Expert Choice removes token-drop and improves expert load balance.
3. Instead of "top-k experts per token", Expert Choice does "top-k tokens per expert".
4. Each expert selects its top-k tokens, then processes the tokens assigned to it.
5. This eliminates tokens dropped due to over confluction of routing.

## Relevance to Thesis (Specifically Mentioned Thesis Gap: §7.1 MoE Routing)
- Expert Choice introduces an alternative architecture to token-choice MoE.
- When routing adapters across peers: adapters can be "pulled" by peer-based workloads OR "pushed" using Expert Choice chooses.
- Relevant to §7.1 Router routing approaches.

## How to Write for Thesis
- Position under MoE routing methods: can inform how to route adapters in a p2p scenario where each peer is the target per acting as an "expert".

## Limitations / Gaps
- Not validated for adapters (MoE dense layers).
- Centralized switch: still relies on all-to-all.

## Relevance to Thesis Sections
- §7.1 MoE Routing