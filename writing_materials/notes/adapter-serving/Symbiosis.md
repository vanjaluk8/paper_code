## Meta
- **Citation:** Symbiosis: Multi-Adapter Inference and Fine-Tuning (2025)
- **Venue:** ASPLOS 2025
- **Tags:** `adapter-serving` `lora` `fine-tuning` `multi-adapter`
- **Thesis sections:** §5.x

## Key Findings
1. Symbiosis is a unified framework for both multi-adapter inference and fine-tuning simultaneously.
2. Allows fine-tuning on new adapter while serving inference on other different adapters.
3. Introduces a "gradient-aware" offloading: the GPU memory is shared between training forward/backward passes and inference compute.
4. Proposes a gradient-aware scheduler that assigns adapters with heavy gradients to dedicated training slots.
5. Achieves 2x throughput improvement over completely separate serving and fine-tuning.

## Relevance to Thesis
- Symbiosis combines centralized adapter serving and fine-tuning under one roof — serving the marketplace dimension where both training and inference for adapters is done by the platform.
- The framework could evolve into a P2P version (peer A trains adapter for task T, peer B serves inference using that adapter).
- Gradient allocation memory sharing suggests that a P2P marketplace would need to handle both training and inference compute across peers.
- Relevance to P2P dimensioning: adapters could be trained on one peer and then transferred for inference on another peer.

## Limitations / Gaps
- All adapters, serving and training demands within same GPU cluster.
- Centralized orchestrator dictates GPU allocation.
- No mention of decentralized identity or trust framework.
- The gradient calculation assumes co-located GPUs — unrealistic for P2P.