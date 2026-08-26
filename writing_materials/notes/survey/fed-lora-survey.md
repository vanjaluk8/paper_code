## Meta
- **Citation:** Shen, H., et al. (2025). Federated Low-Rank Adaptation for Foundation Models: A Survey. *IJCAI*.
- **Venue:** IJCAI
- **Tags:** LoRA, Federated Learning, PEFT, Foundation Models
- **Thesis sections:** §6.1 Federated Learning with LoRA, §8.2 Cross-Model Heterogeneity

## Key Findings
1. Comprehensive survey of FL + LoRA integration.
2. Categorizes methods: global LoRA (shared between clients), personalized LoRA (per-client), hybrid.
3. Key system tradeoffs: aggregation strategies (FedAvg vs personalized vs clustering), communication, compute.
4. FedIT, H2OAgg, FATE, pFL methods.

## Relevance to Thesis
- Direct mapping: FL + LoRA research is the equivalent centralized system of distributed P2P.
- Adapter aggregation and routing methods are relevant for P2P interpretation.

## Limitations / Gaps
- No P2P content; method aggregation strategies assume central coordinator.
- Heterogeneity not addressed.
- Foundation models: only weight LoRA plugged into BERT setting.