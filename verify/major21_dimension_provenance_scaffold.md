# Major-21 scaffold: dimension provenance for §9.3's concept matrix

Review's ask (line 171): *"Demonstrate the inductive derivation: for each
dimension, cite the two or three corpus papers whose design commitments
forced it into the list. Right now the reader is asked to take 'derived
inductively' on trust, and the seven dimensions happen to be exactly the
seven properties of a P2P adapter marketplace."*

This is not a data-derivation task (no script produces a number) and not a
citation-verification task (no misattribution to check) — it's an
evidentiary-grounding task for an argument only the author can make. What
follows is **not draft prose** for §9.3: it is, per dimension, the
candidate systems and the manuscript's own already-cited evidence about
each, so the connecting sentence is a selection-and-phrasing job rather
than a from-scratch literature search.

**Method:** for each dimension, the candidates below are systems already
scored ✓ or (✓) on that dimension in Table~10 (`tab:concept_matrix`) —
i.e., evidence already inside the paper, not new sources. Quotes are
pulled verbatim from the manuscript's own descriptions of each system
(`sections/*.tex`), so nothing here introduces a claim not already
verified and cited in this revision.

**A note on the reviewer's deeper suspicion**, which citing matrix rows
alone doesn't fully answer: the author both defined the dimensions *and*
built the table using those same dimensions, so pointing at checkmarks in
a table the author constructed is somewhat circular as a rebuttal. The
strongest version of each paragraph below therefore also names the
*design problem* each cited paper says it is solving in its own terms —
independent of whether the matrix exists at all — since a problem a paper
states for itself is harder to accuse of being reverse-engineered from the
target architecture.

---

## 1. Frozen backbone

**Matrix evidence:** ✓ for 15 of 17 systems (all but Gossip Learning).

**Candidates:**
- **Houlsby et al. 2019** (bottleneck adapters) and **Hu et al. 2022**
  (LoRA) — the entire premise of both foundational PEFT methods is
  freezing the backbone and training a small delta; per
  `sections/04_peft.tex`, LoRA's frozen-backbone design lets "adapted and
  base-model inference share exactly the same computation graph with zero
  added latency" once merged. These two papers alone establish the
  commitment as foundational, not derived from the target architecture.
- **S-LoRA / Punica / CaraServe** (multi-tenant serving systems, §6) — a
  second, independent line of evidence: frozen backbone is not just a
  training-time convenience here, it is the *structural precondition*
  that makes multi-tenant serving of many task-adapters on shared GPU
  infrastructure possible at all (one resident backbone, many swappable
  adapters).

**Suggested framing:** two independent bodies of work converge on this
commitment for different reasons — PEFT methods need it to avoid storing
a full model copy per task; serving systems need it to amortise one
backbone across many tenants — which is stronger provenance than either
alone.

---

## 2. Adapter exchange

**Matrix evidence:** ✓ for AdapterHub, LoraHub, LoraRetriever, S-LoRA,
Punica, CaraServe, FedPETuning, DP-FedLoRA, FLoRA, MixLoRA, MiLoRA (11 of
17).

**Candidates:**
- **Pfeiffer et al. 2020** (AdapterHub) — built explicitly as "a
  centralised repository and ecosystem for sharing trained adapter
  modules across the community" (`sections/05_adapter_composition.tex`).
  Exchange is not incidental here, it is the paper's stated contribution.
- **Huang et al. 2023** (LoraHub) — "composes a pool of pre-existing LoRA
  adapters" for cross-task generalisation; the whole mechanism depends on
  adapters already being exchangeable, reusable artefacts.
- **Zhao et al. 2024** (LoraRetriever) — selects from "a library" of
  adapters per incoming request; exchange (which adapter answers which
  request) is structural to the design, not optional.

**Suggested framing:** three independent systems, spanning centralised
repositories (AdapterHub), ad hoc composition (LoraHub), and per-request
retrieval (LoraRetriever), all treat the adapter as a portable,
exchangeable unit — the commitment recurs across designs that don't cite
each other's exchange mechanism, suggesting it's a property of the
adapter abstraction itself, not an import from the target architecture.

---

## 3. P2P topology

**Matrix evidence:** ✓ for Petals, MT-EF/Šajina, Gossip Learning (only 3
of 17 — the tightest, most selective dimension in the matrix, which is
itself worth stating: this dimension is rare in the corpus, not padding).

**Candidates:**
- **Borzunov et al. 2023** (Petals) — "geographically distributed
  volunteers contribute GPU resources" in a P2P topology
  (`sections/06_inference_systems.tex`).
- **Šajina et al. 2024** (MT-EF) — peers "collaboratively train and serve
  task-specific modules over a shared encoder backbone"
  (`sections/08_p2p_federated.tex`).
- **Hegedűs et al. 2019** (Gossip Learning) — peer-to-peer gossip exchange
  of model parameters with no server, "eliminating the central
  aggregator."

**Suggested framing:** this is the dimension with the fewest ✓s in the
whole matrix (3 of 17) — worth stating explicitly, since it undercuts the
"reverse-engineered to flatter the target" reading: if the dimensions were
picked to make the target look achievable, the rarest one would be an odd
choice to keep.

---

## 4. Discovery

**Matrix evidence:** ✓ for Petals only; (✓) for AdapterHub and
LoraRetriever.

**Candidates:**
- **Petals** — needs a DHT-based routing table mapping *block indices* to
  peer addresses (`sections/07_moe_routing.tex`: "a DHT-based routing
  table mapping block indices to peer addresses"). This is a genuine
  discovery mechanism, but at the **layer/shard level**, not the
  **adapter-capability level** — which is exactly the distinction the
  review's own gap claim in §9.4 rests on. This is the single strongest
  piece of evidence available: a real system needed *some* discovery
  mechanism, and its granularity mismatch with what a P2P adapter
  marketplace would need is a finding, not an assumption.
- **LoraRetriever** — "matches input embeddings against adapter
  descriptions using a shared embedding space, enabling dynamic routing"
  (`sections/05_adapter_composition.tex`) — a discovery mechanism, but
  explicitly centralised: "LoraRetriever assumes a central retriever with
  a pre-indexed catalogue of all accessible adapters," which is exactly
  why it scores (✓) partial, not ✓.
- **AdapterHub** — a central repository is itself a (centralised)
  discovery mechanism: users find adapters by browsing/searching the hub
  rather than a peer-level lookup.

**Suggested framing:** all three systems that engage this dimension at
all solve discovery by *centralising* it (a hub, a pre-indexed catalogue)
or by operating at the wrong granularity (Petals' layer-level DHT) — none
solves adapter-level discovery without a central index, which is precisely
the gap the review identifies. This dimension's provenance argument is the
strongest of the seven because the corpus evidence and the gap claim are
the same observation stated twice.

---

## 5. Multi-task fusion (composition)

**Matrix evidence:** ✓ for AdapterFusion, LoraHub, LoraRetriever,
MT-EF/Šajina, MixLoRA, MiLoRA (6 of 17).

**Candidates:**
- **Pfeiffer et al. 2021** (AdapterFusion) — "a two-stage approach to
  multi-task" composition (`sections/05_adapter_composition.tex`); this is
  the foundational, most-cited fusion method in the corpus.
- **Huang et al. 2023** (LoraHub) — composes multiple existing LoRA
  adapters for cross-task generalisation on BIG-Bench Hard.
- **Li et al. 2024 / Zhang et al. 2024** (MixLoRA / MiLoRA) — MoE-style
  routing among multiple LoRA experts, a second, independently-arrived-at
  mechanism for the same underlying need (combining more than one
  adapter's contribution per query).

**Suggested framing:** three structurally different composition
mechanisms (two-stage attention fusion, ad hoc hub composition, MoE-style
routing) converge on the same functional need — combining multiple
adapters per query — independently of each other, which is the kind of
convergent-evolution evidence the reviewer is asking for.

---

## 6. Privacy/DP

**Matrix evidence:** ✓ for DP-FedLoRA only; (✓) for FedPETuning (2 of 17
— the second-tightest dimension, alongside P2P topology).

**Candidates:**
- **Xu et al. 2025** (DP-FedLoRA) — "an end-to-end framework combining
  per-sample gradient clipping with low-rank adapter exchange, achieving
  formal DP guarantees" on clinical NLP benchmarks
  (`sections/08_p2p_federated.tex`) — privacy is not incidental here, it's
  a hard requirement of the application domain (clinical data).
- **Zhang et al. 2023** (FedPETuning) — federated learning's foundational
  motivation is avoiding centralised raw data, an implicit privacy
  concern, but FedPETuning itself adds no *formal* DP mechanism — which is
  exactly why it scores (✓) partial rather than ✓, and is itself evidence
  the scoring is principled rather than inflated.
- Two further corpus papers not in the 17-system matrix but already cited
  in `sections/08_p2p_federated.tex` reinforce the same point: **Liu et
  al. 2023** (DP mechanisms for federated adapters) and **Sun et al.
  2024** (privacy-utility tradeoff for federated LoRA, showing low-rank
  adapters need smaller DP noise than full gradients).

**Suggested framing:** this dimension is rare in the matrix (2 of 17) for
a specific, statable reason — privacy becomes an explicit design
commitment only when the application domain demands it (clinical data,
here), not as a general property of adapter systems — which argues for
inclusion as a *recognised but underserved* requirement, not padding.

---

## 7. Absence of a central coordinator

**Matrix evidence:** ✓ for Petals, MT-EF/Šajina, Gossip Learning; (✓) for
LoraHub (4 of 17).

**Candidates:**
- **Petals** — no operator; volunteers alone constitute the serving
  infrastructure.
- **Hegedűs et al. 2019** (Gossip Learning) — by construction, "gossip
  learning matches or outperforms FL quality in simulation **while
  eliminating the central aggregator**" (`sections/08_p2p_federated.tex`)
  — the elimination of a coordinator is the paper's own explicit framing
  of its contribution, not an inference.
- **Šajina et al. 2024 / Šajina 2025** — the doctoral thesis (§8.4)
  describes "one of the first systems for multi-task P2P learning... over
  a shared encoder backbone," explicitly without a central server.

**Suggested framing:** note the overlap with dimension 3 (P2P topology) —
the same three systems dominate both, and the manuscript's own Table 10
footnote already distinguishes them conceptually ("a system could in
principle adopt a P2P topology while still depending on a central
coordinator"). Worth stating in §9.3's justification prose that these two
dimensions are empirically correlated in the current literature but
conceptually separable, which is itself evidence they weren't collapsed
into one dimension for convenience.

---

## Summary table for quick reference

| Dimension | ✓/(✓) count in matrix | Strongest 2-3 candidates |
|---|---|---|
| Frozen backbone | 15/17 | Houlsby 2019, Hu 2022 (LoRA), S-LoRA/Punica/CaraServe |
| Adapter exchange | 11/17 | AdapterHub, LoraHub, LoraRetriever |
| P2P topology | 3/17 | Petals, MT-EF/Šajina, Gossip Learning |
| Discovery | 3/17 (1 full + 2 partial) | Petals (layer-level DHT), LoraRetriever (centralised), AdapterHub (centralised) |
| Multi-task fusion | 6/17 | AdapterFusion, LoraHub, MixLoRA/MiLoRA |
| Privacy/DP | 2/17 | DP-FedLoRA, FedPETuning (+ Liu2023, Sun2024 outside the matrix) |
| No central coordinator | 4/17 | Petals, Gossip Learning, MT-EF/Šajina |

Note the pattern: the three dimensions the review's gap claim actually
hinges on (P2P topology, discovery, no central coordinator) are also the
three rarest in the matrix (3–4 of 17 each). That is itself a datum worth
stating explicitly in §9.3 — the dimensions central to the gap claim are
not the ones every system already satisfies; they're the ones almost none
do, which is a different and stronger claim than "the dimensions were
picked to describe a target that doesn't exist yet."
