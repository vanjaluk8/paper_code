## Meta
- **Citation:** Mao, Y. et al. (2022). UniPELT: A Unified Framework for Parameter-Efficient Language Model Tuning.
- **Venue:** ACL 2022 (long)
- **Tags:** `adapter-composition` `PEFT-framework` `unified`
- **Thesis sections:** §4.3 (unified PEFT framework)

## Key Findings
1. UniPELT provides a unified framework integrating multiple PEFT methods (adapters, prefix tuning, LoRA) in a single model.
2. Each PEFT module is controlled by a gating mechanism that learns to activate the most suitable method for each task at each layer.
3. UniPELT outperforms individual PEFT methods on GLUE benchmarks and shows consistent improvements across text classification, QA, and NER tasks.
4. The gating mechanism learns to adaptively combine the outputs of adapters, prefix tuning, and LoRA, dynamically allocating capacity per task.

## Composition Method
- For each PEFT module (adapter, prefix, LoRA), a small linear gating unit decides how much each contributes to the output at each layer.
- The final hidden representation is a weighted combination: `h_layer_output = h_layer_input + lambda_prefix * h_prefix + lambda_adapter * h_adapter + lambda_lora * h_lora`, where the lambdas are learned scalars per layer.
- Gating parameters are task-specific and trained jointly with the PEFT modules.

## Relevance to Thesis
- Demonstrates dynamic composition of multiple PEFT methods -- directly relevant to a P2P system where the best adapter architecture must be selected per task.
- The gating/weighting concept can be extended to composing independently trained adapters in a P2P setting.
- Relevant to §4.3 on adapter composition frameworks.

## Limitations / Gaps
- Gating mechanism is trained jointly for each task -- not suitable for post-hoc addition of new adapters.
- Focused on method composition at the PEFT-type level (adapter vs prefix vs LoRA), not composition of multiple task-specific adapters.
- Does not consider federated or decentralized scenarios.