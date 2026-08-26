## Meta
- **Citation:** Pfeiffer, J., Vulic, I., Gurevych, I., & Ruder, S. (2020). MAD-X: An Adapter-based Framework for Multi-task Cross-lingual Transfer.
- **Venue:** EMNLP 2020
- **Tags:** `adapter-composition` `cross-lingual` `adapter-fusion`
- **Thesis sections:** §4.1 (adapter-based cross-lingual transfer)

## Key Findings
1. Proposes MAD-X (Multilingual Adapter-Based Cross-Lingual Transfer): decoupling task and language by using separate language adapters (trained on language identification) and task adapters (trained on task-specific data).
2. Introduces **AdapterFusion** as a mechanism to compose multiple language adapters (source embeddings projected into shared space).
3. Demonstrates zero-shot cross-lingual transfer on GLUE tasks across 6 languages with BERT.
4. The framework does not require joint training on multiple tasks -- adapters can be plugged in modularly.

## Composition Method
- Adapters are injected between Transformer layers. Language adapters capture language-specific information; task adapters capture task-specific knowledge.
- For source tasks: language adapter + task adapter stacked sequentially.
- For cross-lingual transfer (zero-shot): target-language language adapter stacked with source-language task adapter.
- Uses a bottleneck architecture: down-projection → ReLU → up-projection → residual connection.
- Composition is sequential -- the output of the language adapter feeds into the task adapter at each layer.

## Relevance to Thesis
- Demonstrates modular adapter composition for cross-lingual transfer -- a key building block for P2P multi-adapter systems.
- Shows that different adapters can be mixed modularly (language + task) without retraining the full model.
- Directly relevant to §4.1 adapter-based cross-lingual transfer and composition.

## Limitations / Gaps
- Composition is limited to stacking two adapters (language + task); does not explore larger sets of adapters or dynamic composition.
- Does not address distributed/decentralized serving of adapters.
- Evaluated on full fine-tuning setting rather than PEFT release.