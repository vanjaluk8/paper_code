## Meta
- **Citation:** Zhou et al. (2023) Mixture-of-Domain-Adapters: Decoupling and Injecting Domain Knowledge into LMs
- **Venue:** ArXiv preprint (June 2023)
- **Tags:** `MoE-routing` `domain-adaptation` `adapterfusion`
- **Thesis sections:** §7.x (MoE routing)

## Key Findings
1. Proposes a set of domain adapters combined via a learned mixing gating that adaptively weights them depending on input token.
2. Demonstrates that domain-specific adapters can be separated and mixed at inference time, enabling flexible composition across domains.
3. The learned router weights contributions from multiple domains, achieving strong cross-task and cross-domain generalisation.

## Routing / Gating Mechanism
- Each domain adapter is trained independently on domain-specific data.
- At test time, a lightweight gating network combines the outputs of all domain adapters weighted by learned probabilities.
- Different masking of the gating can allow sparse selection of domain experts.

## Relevance to Thesis
- The concept of composing domain experts wwith a router is highly relevant to P2P adapter composition.
- Suggests how adapters from different peers (domains) can be combined at inference.

## Limitations / Gaps
- Routing network is centralised; no discussion of decentralised routing protocols.
- Domain experts are fixed after pretraining — no mechanism for on-the-fly addition of new experts.