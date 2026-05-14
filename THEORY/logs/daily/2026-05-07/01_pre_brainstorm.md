> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]

# 01_pre_brainstorm.md — W6 D5 Pre-Brainstorm

**Date:** 2026-05-07 (Thu, W6 Day 5)
**Prepared:** EOD 2026-05-06 closeout session
**Topic:** Temporal Identity / Sigma Inheritance / Perception Stack

---

## 1. Temporal Identity — Key Questions

### 1.1 What is the narrowest Cat B theorem for R_{t→s}?

**Current working claim:** Given u_t, u_s ∈ F_M(P), PersComp sets, and admissible transport plan M_{t→s} (E1–E4), there exists a component-level correspondence R_{t→s} obtained by thresholding score matrix S. For K_t = K_s and margin condition Δ_sep > 0, R_{t→s} is a unique bijection.

**Narrowest Cat B scope:**
- Part (a): existence always (constructive from score matrix — no assumptions beyond E1–E4).
- Part (b): uniqueness requires: (1) K_t = K_s, (2) Δ_sep > 0 (margin condition), (3) finite graph.
- Part (d): K=1 reduction is direct algebra.
- Part (c): kernel independence requires OP-0011 (not Cat B yet).

**Key question:** Is the margin condition Δ_sep an explicit computable formula, or does it require additional structure?

### 1.2 Which assumptions are necessary for Cat B?

**Needed:**
- E1: transport plan M_{t→s} with finite total mass.
- E2: PersComp(u_t) and PersComp(u_s) non-empty (thresholded CC).
- E3 (reclassified as solution constraint): Monge-style admissibility.
- E4: finite graph X_t, X_s.
- Margin: Δ_sep = min diagonal score - max off-diagonal score > 0.

**Not needed for Cat B (a,b,d):** kernel independence (→ Cat C), full OP-0011 resolution.

### 1.3 What remains Cat C?

- Part (c): kernel independence — depends on whether score S_{ij} changes under different transport kernels. Requires OP-0011 component confinement proof: that high-mass transport stays within PersComp neighborhoods.
- Stochastic case: transport plan M_{t→s} from Langevin SDE path — requires Package II + T_* registration.

### 1.4 exp83 scope confirmation

exp83 validates:
- Scenario A (translation): CONT correctly detected.
- Scenario B (merge): MERGE correctly detected.
- Scenario C (split): SPLIT correctly detected.
- Scenario D (birth+continuation): BIRTH+CONT correctly detected.

exp83 does NOT validate: kernel independence, stochastic landing distribution, global continuity in T_*.

---

## 2. Sigma Inheritance — Key Questions

### 2.1 Which parts of T-σ-Inherit are Cat B after exp84?

**Cat B path (exp84 validates):**
- (a) σ(C_i) existence and formula: mass, centroid, inertia tensor — well-defined on finite graph.
- (b) CONT: σ inheritance is σ(C_j^s) ≈ transport-weighted σ(C_i^t). Centroid residual < 0.5 units.
- (d-direction): split principal-axis direction inherits elongation direction (cos(θ) > 0.90).
- (e) BIRTH: σ initialized fresh; no inheritance. Well-defined.

**Cat B formula (MERGE centroid):** Φ_MERGE: centroid = mass-weighted average (parallel-axis theorem). exp84 Scenario B residual < 0.05. Scenario C Frobenius < 2%.

### 2.2 Which parts remain Cat C?

- (c): σ_standard = σ(C_i) relative to Wigner/Fiedler eigenvector basis → depends on spectral decomposition under merge/split. This is OP-0008-MERGE/SPLIT. W9+.
- (d)-σ_standard: stochastic landing distribution under σ_standard — requires P-F-A1 Package II (Eyring-Kramers) + OP-0021 T_*. W9+.
- Full orientation inheritance under arbitrary graph topology: requires OP-0008 resolution.

### 2.3 How should σ(C_i) avoid K-field slot dependence?

**Key principle (CN5 analogue):** σ(C_i) must be defined relative to the induced subgraph G_{C_i} with one-hop buffer, NOT relative to slot index in K-field. σ(C_i) = σ_rich(u_i; G_{C_i}, P_C).

**Why this matters:** K-field is a local chart convenience. If σ(C_i) is slot-indexed, it would make σ-inheritance depend on slot assignment, which is arbitrary (S_K permutation symmetry). The quotient formalism from W6 D3 resolves this: σ should be defined on the S_K-quotient, not on the indexed product.

---

## 3. Perception Stack — Open Questions

### 3.1 SCC creates perceptual objecthood

- Primitive: u_t : X_t → [0,1] soft cohesion field.
- Output: formations (cohesion regions) — pre-objective.
- Key: formations are not yet objects; objecthood is derivative.

### 3.2 RelationWorld organizes SCC formations into world grammar

- Input: SCC formations (detected via K_act, PersComp).
- Layer: assigns relation structure (closure, distinction, co-belonging) between formations.
- Output: world-state (which formations are in relation, what their structure is).
- Note: RelationWorld theory may be ontologically broader than SCC (it handles any relational primitive), but in the perceptual pipeline it receives SCC output.

### 3.3 ONN gives semantic/ontological placement

- Input: relational world-state from RelationWorld.
- Layer: constraint-based fixed-point solver; maps relational structure to ontological categories.
- Output: semantic labels, ontological commitments.

### 3.4 ORTSF stabilizes action, attention, memory, and delayed control

- Input: ONN outputs + temporal identity (T-Temporal-Identity).
- Layer: ORTSF framework — delay-robust control stabilization, attention allocation, memory formation.
- Output: action commands, updated attention, memory updates.

### 3.5 Formal inter-layer links (open questions)

1. **SCC → RelationWorld**: How does the SCC energy E determine which formations become RelationWorld primitives? Do formation boundaries (T-OP6-B, d_H ≤ 2(α/β)^{1/2}) map cleanly to RelationWorld node boundaries?
2. **RelationWorld → ONN**: Is the relational grammar produced by RelationWorld already in the constraint form needed by ONN? Or is there a translation step?
3. **T-Temporal-Identity as ORTSF input**: How does the σ-inheritance (T-σ-Inherit) map to ORTSF memory formation?

---

## 4. Open Risks for W7

### 4.1 Overpromoting working candidates

Risk: T-Temporal-Identity has exp83 numerical support but not a proof. Canonical promotion requires full statement with proved assumptions — not just "exp passes."

Mitigation: Any Cat B canonical promotion must have (a) explicit assumptions listed, (b) narrow claim not exceeding exp83 scope, (c) parts (c) kept Cat C.

### 4.2 Treating toy experiments as proofs

exp83 uses 15×15 grid, Gaussian blobs, threshold PersComp proxy. This is NOT the full PersComp definition. Any Cat B theorem must explicitly state "PersComp proxy via threshold superlevel-set CC" or use the actual persistence-diagram definition.

### 4.3 Mixing Package I equilibrium with Package II dynamics

Package I (T-PF-A1-AR/SDE/GI/PE) proves: Gibbs invariant measure exists, is unique, Poincaré inequality holds for any T_* > 0.

Package I does NOT prove: Eyring-Kramers rates, T_* has a natural definition, inter-sector transition rates, T_* > 0 is canonical.

Any claim about "dynamics of K over time" requires Package II + OP-0021. Do not blur this line.

### 4.4 K-field local chart leaking into foundation

K-field (K-indexed product manifold Σ_M^K) is a modeling artifact for multi-formation analysis. It is NOT the foundational state space. The foundational state space is F_M(G) = {u ∈ [0,1]^n : Σu_i = M}.

If any new theorem uses "slot k of K-field" as a primitive, flag it immediately and route through the quotient formalism (W6 D3 G3.2).

---

*End of W6 D5 pre-brainstorm. Prepared EOD 2026-05-06 closeout.*
