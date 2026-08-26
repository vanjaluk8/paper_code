## Meta
- **Citation:** Comparative Analysis and Optimization of LoRA Adapter Co-serving for Large Language Models (2025)
- **Venue:** ACM CF 2025
- **Tags:** `adapter-serving` `lora` `comparative-analysis`
- **Thesis sections:** §5.x

## Key Findings
1. Provides a comparative analysis of existing LoRA co-serving systems (S-LoRA, Punica, CaraServe, Cannikin).
2. Proposes optimizations such as adaptive batch sizing and speculative scheduling to improve LoRA adapter serving throughput.
3. The study finds that adapter co-serving is bottlenecked by I/O bandwidth rather than compute for most LoRA ranks.
4. Tested across multiple hardware configurations (A100, V100, RTX 3090).
5. Suggests that system-level heterogeneity support (GPU-diverse nodes) is missing in all current LoRA serving systems.

## Relevance to Thesis
- The comparative analysis provides useful insights for thesis survey — benchmarking Punica, S-LoRA, Cannikin.
- The "bottleneck is I/O, not compute" finding impacts P2P design: in a networked setting, network I/O is even more constrained than memory I/O.
- Concludes that heterogeneous hardware handling is not addressed by any existing serving system — gap the thesis can fill.

## Limitations / Gaps
- Lacks any distributed or P2P component entirely.
- Analysis limited to single-node, single-cluster deployments.
- Unable to match all workload patterns typical of P2P environments across the internet.
- Optimization suggestions assume all adapters in local memory — no network transfer modeled.