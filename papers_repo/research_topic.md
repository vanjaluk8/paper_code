## PhD Research Topics

## Decentralized Adapter-based LLM Systems

### P2P Adapter Marketplace for LLMs

**Related work:** G0, G3, G4 | **Datasets:** D4 (domain), D7 (language), D1 (department)

#### Motivation
Large models are expensive to train, but small task-specific adapters are cheap. Today adapters are centralised (HF Hub, OpenAI tools). A decentralised network could allow users to share adapters directly.

#### Research Contribution
Design a peer-to-peer network where nodes exchange LoRA/adapters dynamically during inference.

#### Core Ideas
- Base model replicated across peers
- Adapters stored locally on nodes
- During inference, missing adapters are fetched via P2P
- Caching + routing policies

#### Possible Novelty
- Adapter discovery protocol
- Latency-aware adapter routing
- Adapter trust scoring

#### Adapter Discovery Approaches

1. **Capability embeddings** â€” each adapter publishes a vector encoding its behaviour; peers find adapters via nearest-neighbour search in this space
2. **DHT metadata registry** â€” structured metadata (task, domain, base model) stored in a distributed hash table; queried by filters
3. **Adapter fingerprinting** â€” run adapters on a standardised probe set, compare output distribution shifts to find similar adapters without task labels
4. **Gossip-based** â€” nodes periodically share adapter catalogs with neighbours; "wanted" broadcasts for missing capabilities
5. **Query-driven probing** â€” on cache miss, forward query to peers who respond with confidence scores (e.g., perplexity under their adapter)
6. **Layered hybrid** â€” DHT for coarse filtering â†’ embedding/fingerprint matching â†’ query-driven final selection

#### Why Better than Existing Solutions
- No formal framework exists for adapter discovery and composition across distributed nodes â€” existing PEFT research (G0) assumes a single-node, centralised setting.
- The question of how to represent, search, and match adapters by capability (not just task label) is an open research problem â€” requires new adapter embedding/similarity methods beyond what AdapterHub (G0) provides.
- Introduces a novel research question at the intersection of distributed systems (G3) and PEFT (G0, G1): what are the theoretical bounds on adapter reuse and transfer when nodes have heterogeneous data distributions?

#### Scientific Contributions

1. **â˜…A1 â˜…S2** â€” A formal adapter discovery protocol combining capability embeddings with DHT-based routing for decentralised PEFT component retrieval
2. **â˜…V1 â˜…R2** â€” An adapter similarity metric based on behavioural fingerprinting that enables task-agnostic matching without shared label spaces
3. **â˜…T2** â€” Theoretical analysis of adapter reuse bounds under heterogeneous data distributions in P2P networks

#### Expected Outcomes
- Open-source P2P adapter exchange framework with discovery, caching, and routing modules
- Empirical comparison of discovery strategies (DHT, embedding, fingerprint, gossip) across latency, precision, and bandwidth
- Published adapter similarity benchmark on D4/D7 showing reuse rates and transfer quality across domains

#### Evaluation Metrics
- Inference latency vs centralised hub
- Bandwidth cost
- Adapter reuse rate

---

## Datasets

Foundation datasets for all topics. Each dataset has a natural partition key that enables P2P / federated simulation â€” the split determines which node holds which data.

### Available Datasets

#### D1. MIMIC-IV (Medical)
De-identified EHR data â€” diagnoses, procedures, lab results, prescriptions, clinical notes.  
**Split keys:** hospital department, diagnosis group (ICD chapter), admission year, patient demographic.  
**Strength:** Real-world heterogeneity across departments mirrors natural institutional P2P setting.

| Code | Variant | Task | Split key |
|------|---------|------|-----------|
| D1-sql | NL2SQL | LLM-generated NL questions paired with SQL queries over MIMIC schema | department |
| D1-ner | Clinical NER | Entity extraction from clinical notes (medications, conditions, procedures) | specialty |
| D1-sum | Discharge summarisation | Structured EHR data to discharge summary text | diagnosis group |
| D1-qa | Clinical QA | LLM-generated QA pairs from clinical notes | department |
| D1-icd | ICD code prediction | Time-series of clinical events to diagnosis codes | admission year |
| D1-mort | Mortality/readmission | Binary classification from patient trajectories | demographic group |

#### D2. Synthetic Online Shopping
Generated e-commerce data â€” user behaviour, product catalogs, transactions.  
**Split keys:** user segment, product category, store/region.  
**Strength:** Controllable heterogeneity â€” can tune how different each node's distribution is for ablation studies.

| Code | Variant | Task | Split key |
|------|---------|------|-----------|
| D2-rec | Recommendation explanations | LLM-generated NL explanations for product recommendations | user segment |
| D2-intent | Customer intent classification | User query to intent label (browse, compare, buy, complain) | product category |
| D2-desc | Product description generation | Structured product attributes to marketing description | category |
| D2-fraud | Fraud detection | Transaction sequences to anomaly labels | region |

### Candidate Datasets to Add

#### D3. FLamby (Federated Medical Benchmarks)
Pre-partitioned medical datasets (Fed-ISIC, Fed-Camelyon, Fed-Heart, Fed-TCGA, Fed-IXI).  
**Split keys:** already split by institution/hospital.  
**Strength:** Accepted FL benchmark â€” enables direct comparison with FedAvg, FedProx, PerFedAvg baselines.

| Code | Variant | Task | Split key |
|------|---------|------|-----------|
| D3-meta | Cross-institutional meta-features | LLM-generated descriptions of each institution's data characteristics | institution |
| D3-aug | Synthetic augmentation | LLM/diffusion-generated additional samples per site | institution |

#### D4. The Pile (Subsets)
Large-scale language modelling corpus from diverse sources.  
**Split keys:** source domain (Wikipedia, PubMed, GitHub, legal, books, StackExchange, ArXiv).  
**Strength:** Natural domain specialisation â€” each node trains an adapter on its domain.

| Code | Variant | Task | Split key |
|------|---------|------|-----------|
| D4-cls | Domain classification | Text snippet to source domain label (for training adapter routers) | domain |
| D4-xsum | Cross-domain summarisation | Summarise text from one domain in the style of another | domain pair |
| D4-code2doc | Code/Documentation | Code-to-docstring and docstring-to-code pairs (GitHub subset) | programming language |
| D4-qa | Domain QA | LLM-generated QA pairs per domain (medical, scientific, legal) | domain |

#### D5. LEAF / Reddit (FL Benchmark)
Standard federated learning benchmark with Reddit comments.  
**Split keys:** by user (natural non-IID).  
**Strength:** Established in FL literature, extreme user heterogeneity.

| Code | Variant | Task | Split key |
|------|---------|------|-----------|
| D5-sent | Per-user sentiment | Sentiment-labeled comments per user | user |
| D5-style | Writing style transfer | LLM-paraphrased parallel corpus in different user styles | user |
| D5-topic | Subreddit topic classification | Comment to subreddit prediction | user |

#### D6. Amazon Reviews (Multi-domain)
Product reviews across 28+ product categories.  
**Split keys:** product category, reviewer.  
**Strength:** Clean domain boundaries, temporal dimension (review date enables time-based splits).

| Code | Variant | Task | Split key |
|------|---------|------|-----------|
| D6-sent | Category-specific sentiment | Sentiment where "positive" differs per category (durability vs taste) | category |
| D6-aspect | Aspect-based opinion extraction | Extract (aspect, opinion, sentiment) triples from reviews | category |
| D6-summ | Review summarisation | Multiple reviews to consensus summary per product | category |
| D6-xfer | Cross-category transfer pairs | LLM-generated analogous reviews across categories | category pair |

#### D7. Stack Overflow / SOTorrent
Programming Q&A with code, tags, timestamps.  
**Split keys:** programming language, tag cluster, year.  
**Strength:** Natural task specialisation (Python vs Java node), strong temporal drift.

| Code | Variant | Task | Split key |
|------|---------|------|-----------|
| D7-code | Code generation | Question to accepted answer code snippet | language |
| D7-rank | Answer ranking | Given question + multiple answers, rank by quality/votes | tag cluster |
| D7-dup | Duplicate detection | Question pair to duplicate or not | language |
| D7-tag | Tag prediction | Question text to tag set | year |
| D7-migrate | API migration | Old API usage to new API usage pairs (from edit history) | year |

### Splitting Strategies

| Strategy | How | Best for | Example |
|----------|-----|----------|---------|
| Domain/institutional | Each node = different domain or institution | Topics 1, 3, 7 | D1 by department, D4 by source |
| User-based | Each node = one or group of users | Topic 5 | D5 by user, D6 by reviewer |
| Temporal | Each node = different time period | Topic 6 | D1 by admission year, D7 by post year |
| Label Dirichlet (Î±) | Synthetic non-IID via Dirichlet allocation | Controlled ablations | Any classification dataset, tune Î± |
| Category/vertical | Each node = product/task vertical | Topics 2, 4 | D6 by category, D2 by store |

---

## Addendum: Contribution Taxonomy for Decentralized Adapter Systems

Adapted from the unified CS/ML contribution taxonomy (classical CS + NeurIPS/ICML/ACL reviewing conventions). Only categories relevant to this thesis direction are included, with concrete examples from the research topics above.

### Contribution Types

#### 1. Theoretical (T)

| Code | Type | Example from this thesis |
|------|------|--------------------------|
| â˜…T1 | New theorem / proof | Convergence bounds for adapter exchange vs gradient exchange (Topic 3) |
| â˜…T2 | Tightened bound | Adapter reuse bounds under heterogeneous distributions (Topic 1) |
| â˜…T3 | Impossibility result | Conditions under which adapter composition provably degrades (Topic 2) |

#### 2. Algorithmic (A)

| Code | Type | Example from this thesis |
|------|------|--------------------------|
| â˜…A1 | New algorithm | Adapter discovery protocol with DHT + capability embeddings (Topic 1) |
| â˜…A2 | Algorithmic improvement | Selective adapter propagation reducing negative transfer (Topic 3) |
| â˜…A3 | Online / adaptive algorithm | Temporal adapter router with drift-aware selection (Topic 6); bandit-based cache eviction (Topic 4) |

#### 3. Representation (R)

| Code | Type | Example from this thesis |
|------|------|--------------------------|
| â˜…R1 | Representation learning | Adapter capability embeddings for task-agnostic similarity (Topic 1) |
| â˜…R2 | Feature representation | Adapter behavioural fingerprints from probe-set outputs (Topic 1) |

#### 4. Model / Architecture (M)

| Code | Type | Example from this thesis |
|------|------|--------------------------|
| â˜…M1 | New architecture | Mixture-of-Adapters with token-level routing (Topic 2) |
| â˜…M2 | Architectural modification | Decentralised AdapterFusion without central coordinator (Topic 3) |

#### 5. Systems (S)

| Code | Type | Example from this thesis |
|------|------|--------------------------|
| â˜…S1 | System architecture | P2P adapter marketplace framework (Topic 1) |
| â˜…S2 | Distributed protocol | Adapter gossip protocol (Topic 3); adapter exchange protocol (Topic 1) |
| â˜…S3 | Infrastructure framework | Open-source P2P adapter exchange platform (Topic 1) |

#### 6. Empirical (E)

| Code | Type | Example from this thesis |
|------|------|--------------------------|
| â˜…E1 | Benchmark suite | Adapter similarity benchmark on D4/D7 (Topic 1) |
| â˜…E2 | Large-scale empirical study | Adapter interpolation in time (Topic 6); privacy leakage comparison (Topic 5) |
| â˜…E3 | Empirical discovery | Scaling behaviour of adapter reuse across domains; adapter composition failure modes |

#### 7. Measurement (V)

| Code | Type | Example from this thesis |
|------|------|--------------------------|
| â˜…V1 | New metric | Adapter similarity metric via behavioural fingerprinting (Topic 1); multi-dimensional trust score (Topic 7) |
| â˜…V2 | Diagnostic evaluation | Adapter poisoning detection rates (Topic 7); negative transfer analysis (Topic 3) |

#### 8. Conceptual (C)

| Code | Type | Example from this thesis |
|------|------|--------------------------|
| â˜…C1 | Problem formalisation | Adapter lifecycle as formal model (Topic 6); adapter poisoning threat model (Topic 7) |
| â˜…C2 | Conceptual framework | Adapters as atomic units of knowledge exchange in P2P systems (thesis-wide) |
| â˜…C3 | Taxonomy | Adapter discovery strategies taxonomy (Topic 1); adapter poisoning attack taxonomy (Topic 7) |

### Topicâ€“Contribution Mapping

| Topic | Primary Contributions | Types |
|-------|-----------------------|-------|
| 1. P2P Adapter Marketplace | Discovery protocol; similarity metric; reuse bounds | â˜…A1, â˜…R1, â˜…R2, â˜…V1, â˜…S1, â˜…T2 |
| 2. Adapter MoE | Token-level MoA architecture; routing stability analysis; continual insertion | â˜…M1, â˜…T1, â˜…A2 |
| 3. Decentralised Multi-Task | Convergence analysis; decentralised fusion; selective propagation | â˜…T1, â˜…M2, â˜…A2, â˜…S2 |
| 4. Edge Adapter Streaming | Prefetching meta-model; bandit cache eviction; adapter compression | â˜…A3, â˜…A1, â˜…M2 |
| 5. Federated Personalisation | Optimal rank theory; aggregation strategies; privacy bounds | â˜…T1, â˜…A2, â˜…T2 |
| 6. Temporal Routing | Lifecycle framework; temporal router; interpolation analysis | â˜…C1, â˜…A3, â˜…E2 |
| 7. Trust & Reputation | Threat model; reputation protocol; certification testing | â˜…C1, â˜…S2, â˜…V1, â˜…V2 |

### What Makes a Contribution Strong (Conference-Grade)

A contribution should satisfy:

1. **Generality** â€” not a one-off trick; applicable beyond the specific experimental setup
2. **Verifiability** â€” reproducible results with clear experimental protocol
3. **Metric-moving** â€” improves measurable quantities (accuracy, latency, bandwidth, robustness, scalability, communication cost, privacy leakage)
4. **Extensibility** â€” others can build on it (open protocol, modular design, formal framework)