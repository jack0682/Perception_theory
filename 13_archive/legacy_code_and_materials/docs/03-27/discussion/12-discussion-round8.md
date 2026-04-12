# Discussion Phase — Round 8: Multi-Formation Theory — Competition, Coexistence, and Interaction

**Date:** 2026-03-27
**Phase:** Extended discussion — the hardest extension

---

## Foundational Theorist — Round 8

### I. How Deep the Single-Formation Assumption Runs

The multi-formation problem is not a bolt-on extension. It reaches into the theory's primitive architecture.

**Distinction is the critical casualty.** With multiple formations $u_t^{(1)}, u_t^{(2)}, \ldots, u_t^{(K)}$, the complement $1 - u_t^{(i)}$ is no longer "the exterior of formation $i$." It is the union of the background *and every other formation*. The distinction operator conflates two structurally different conditions: being distinguished from background and being distinguished from other formations.

**Co-belonging is also affected.** With multiple formations, co-belonging must do genuinely discriminative work: $x$ and $y$ might both be highly cohesive but belong to *different* formations.

**The energy is implicitly single-formation.** The four-term structure must be re-examined for multi-formation behavior.

**Transport inherits the problem.** Which formation does $\mathbf{M}_{t \to s}$ transport?

### II. Three Candidate Architectures

#### Architecture A: Soft Partition Constraint

$K$ fields with $\sum_k u_t^{(k)}(x) \leq 1$. **Rejected as foundational** — treats formations as competing class labels, smuggling in mutual-exclusion assumptions that the soft ontology was designed to avoid. Acceptable as implementation-level simplification only.

#### Architecture B: Independent Fields with Competition Energy (Advocated)

$K$ independent fields $\{u_t^{(k)}\}$, each in $[0,1]$, without hard partition constraint. Interaction via coupling terms:

**Competition (soft exclusion):**
$$\mathcal{E}_{\mathrm{comp}}(u^{(i)}, u^{(j)}) = \lambda_{\mathrm{comp}} \sum_{x} u^{(i)}(x) \cdot u^{(j)}(x)$$

Soft penalty for overlap. At $\lambda_{\mathrm{comp}} = 0$, fully independent. As $\lambda_{\mathrm{comp}} \to \infty$, recovers hard partition.

**Cross-distinction:**
$$\mathcal{E}_{\mathrm{cross}}(u^{(i)}, u^{(j)}) = \lambda_{\mathrm{cross}} \sum_{x} u^{(i)}(x) \cdot (1 - \mathbf{D}_t(x; u^{(j)}))$$

Distinction no longer against $1 - u^{(i)}$ but against *each other formation specifically*.

#### Architecture C: Vector-Valued Field

$U_t : X_t \to [0,1]^K$. Notationally equivalent to B but obscures per-formation structure.

### III. Three-Level Distinction Structure

**Level 1: Background distinction.** $\mathbf{D}_t^{\mathrm{bg}}(x; u^{(i)}) = \mathbf{D}_t(x; 1 - \sum_k u^{(k)})$

**Level 2: Inter-formation distinction.** $\mathbf{D}_t^{(i \leftarrow j)}(x) = \mathbf{D}_t(x; u^{(j)})$

**Level 3: Total distinction.** $\mathbf{D}_t^{\mathrm{total}}(x; u^{(i)}) = \mathbf{D}_t^{\mathrm{bg}}(x; u^{(i)}) \cdot \prod_{j \neq i} \mathbf{D}_t^{(i \leftarrow j)}(x)$

Multiplicative: a formation is distinguished only if distinguished from background *and* every competitor.

### IV. Generalizing Co-Belonging

**Within-formation:** $W_t^{(k)}(x,y) = \mathbf{N}_t(x,y) \cdot u_t^{(k)}(x) \cdot u_t^{(k)}(y)$ — diffusion stays within formation $k$.

**Cross-formation:** $W_t^{(i,j)}(x,y) = \mathbf{N}_t(x,y) \cdot u_t^{(i)}(x) \cdot u_t^{(j)}(y)$ — diagnostics for merging, splitting, poor separation.

$\mathbf{C}_t$ becomes the **individuation operator** for multi-formation systems.

### V. The Energy Landscape Argument

The single-formation SCC energy is non-convex with multiple basins. **Sequential extraction:**

$$u^{(k+1)*} = \arg\min_u \mathcal{E}(u) + \lambda_{\mathrm{comp}} \sum_{j=1}^{k} \sum_x u(x) \cdot u^{(j)*}(x)$$

$K$ is not a parameter but a property of the energy landscape. Formations individuate *themselves* through the dynamics.

### VI. Transport in Multi-Formation

A **matrix of kernels:**

$$\mathbf{M}_{t \to s} = \begin{pmatrix} \mathbf{M}^{(1 \to 1)} & \mathbf{M}^{(1 \to 2)} & \cdots \\ \mathbf{M}^{(2 \to 1)} & \mathbf{M}^{(2 \to 2)} & \cdots \\ \vdots & \vdots & \ddots \end{pmatrix}$$

Diagonal: within-formation persistence. Off-diagonal: merging, splitting, switching.

### VII. Multi-Formation Proto-Cohesion

**Per-formation:** Each $k$ satisfies $\mathsf{ProtoCoh}^{(k)}$ with $\mathsf{Sep}^{(k)}_{\mathrm{total}}$ using three-level distinction.

**System-level:** (1) Each formation individually proto-cohesive. (2) Cross-formation co-belonging bounded. (3) Non-trivial background exists.

---

## Formal Systems Architect — Round 8

### 1. Option (b) Is Architecturally Correct

**The formal universe remains unchanged.** Multi-formation is DERIVED, not primitive.

A field with two separated high-cohesion regions is already handled: $\mathbf{C}_t$ identifies clusters, $\mathbf{D}_t$ measures distinction, the energy evaluates each region. C_t extraction is ontologically consistent: formations emerge from the field.

### 2. The Architectural Explosion Under Option (a)

| Component | Single-formation | Multi-formation (a) |
|-----------|-----------------|-------------------|
| Primitive fields | 1 | K |
| Operators | ~7 | ~7K + O(K²) cross-terms |
| Derived notions | 5 | 5K |
| Energy terms | 4 | 4K + 2 cross-terms |
| **Total entities** | ~20 | ~20K + O(K²) |

For K=5: ~130 entities. For K=20: ~500. Not manageable.

### 3. Formation Count via Persistence Diagram

$K_t = |\{\text{bars in } PD_0(u_t) \text{ with persistence} > \varepsilon_{\mathrm{form}}\}|$

**Formation lifecycle as topological events:**
- BIRTH: new bar appears in $PD_0$
- MERGER: two bars merge
- SPLIT: one bar bifurcates
- DEATH: bar ends

Every event detectable by existing machinery. No new operators required.

### 4. C_t Upgraded to Essential

C_t is no longer merely the co-belonging operator — it is the **formation individuation mechanism**. Status upgraded from OPEN to ESSENTIAL-OPEN.

### 5. Energy Structure Unchanged

Competition is implicit: the single-field constraint ($u_t(x) \in [0,1]$) combined with the double-well and separation terms creates implicit competition. No explicit $\mathcal{E}_{\mathrm{comp}}$ needed.

### 6. Multi-Formation Derived Layer

```
7.5.1  FORMATION EXTRACTION: C_t clusters {S_k}
7.5.2  PER-FORMATION RESTRICTION: u_t^(k) = u_t · 1_{S_k}
7.5.3  PER-FORMATION PREDICATES: ProtoCoh^(k)(u_t)
7.5.4  FORMATION RANKING: by diagnostic vector or persistence
7.5.5  LIFECYCLE EVENTS: topological events in PD_0
```

### 7. Decision Matrix

| Criterion | Option (a) | Option (b) |
|-----------|-----------|-----------|
| Ontological consistency | Violates | **Preserves** |
| Formal universe change | Major | **None** |
| Entity count | O(K²) | **O(1)** |
| Formation count | Fixed/circular | **Emergent** |
| Overlapping formations | Handles | Cannot (deferred) |
| Formation lifecycle | Requires operators | **Automatic** |

**Recommendation:** Option (b) canonical. Option (a) deferred for overlapping formations.

---

## Critical Skeptic — Round 8

### 1. D_t Is Fundamentally Broken

Two formations adjacent on $X_t$. From formation 1's perspective, $1 - u^{(1)}$ is high on sites belonging to formation 2. But formation 2's sites are not "exterior" — they are *another coherent formation*. D_t treats the second formation identically to empty background.

**What's needed:** Relative distinction $\mathbf{D}_t(x; u^{(k)}, u^{(j)})$ — new type signature, new axioms. Current D-Ax1 through D-Ax3 do not address inter-formation distinction.

**Sep becomes meaningless** in multi-formation: a formation distinguished from background but undistinguished from its neighbor scores high — a false positive.

### 2. Occlusion Destroys the Soft Partition

A hand in front of a face: both formations present at occluded sites. $\sum u^{(k)}(x) > 1$. The soft partition constraint cannot handle this. Three responses — amodal completion (violates constraint), layered fields (introduces depth ordering), deny the problem (limits applicability). **No good answer yet.**

### 3. Only Emergent K Is Ontologically Consistent — And It's Unformalized

Fixed K = segmentation labels = prohibited. Optimized K = model selection = engineering. Emergent K = from energy landscape = consistent but requires nonparametric formulation, basin counting, and "deep enough" criteria. **Commitment-apparatus mismatch:** the ontology requires emergence, the apparatus supports only pre-specification.

### 4. Multiple Basins ≠ Coexisting Formations

A gradient flow from one initial condition reaches ONE basin. "Multiple basins exist" is about the energy landscape. "Multiple formations coexist" is about a field configuration. Different things. A field realizes one basin, not multiple simultaneously.

### 5. C_t Clusters: Promising but Incomplete

**Works** for non-overlapping formations with zero-cohesion gaps. **Partially works** for soft gaps (low but nonzero cohesion — requires thresholding C_t graph). **Doesn't work** for: overlapping formations, preventing energy from preferring merged formations, fixing D_t's blindness.

### 6. The Deepest Ontological Worry

**Single-field approach:** Ontologically consistent (field primary, formations derived) but structurally limited.

**Multi-field approach:** Structurally capable but ontologically problematic (formations become primitive inputs).

**This is a genuine dilemma.** The ontologically consistent approach cannot handle the full range of phenomena. The capable approach betrays the theory's commitments.

**Recommendation:** State the dilemma explicitly. Develop single-field + C_t for non-overlapping cases. Develop multi-field as pragmatic supplement for overlapping cases with explicit ontological tension acknowledgment.

---

## Synthesis Moderator — Round 8

### 1. The Fundamental Disagreement

The sharpest genuine disagreement since the discussion began:
- **Theorist:** Multi-field Architecture B
- **Architect:** Single-field + C_t extraction
- **Skeptic:** Neither is satisfactory; genuine dilemma

The Skeptic is right that this is a dilemma, not a design choice.

### 2. Three-Phase Resolution

1. **Complete single-formation theory first.** C_t, T_t, Group F, dynamics.
2. **Single-field multi-formation (Option b)** for non-overlapping case. C_t extraction, PD_0, emergent K.
3. **Multi-field theory (Architecture B)** as generalization for overlapping formations. New primitives clearly labeled.

### 3. D_t Is the Technical Bottleneck

Cannot distinguish formation-background from formation-formation boundaries. Must be resolved before multi-formation ProtoCoh can be defined.

### 4. K-Emergence: Two Distinct Concepts

- **Coexisting formations:** Multiple formations in one field → C_t clusters
- **Alternative formations:** Different possible formations from same substrate → energy basins

Different concepts requiring different apparatus.

### 5. Convergence/Divergence Table

**SETTLED:**

| # | Item |
|---|------|
| S33 | K must be emergent, not externally specified |
| S34 | D_t structurally inadequate for multi-formation |
| S35 | Single-field C_t extraction handles non-overlapping case |
| S36 | Overlapping formations require multi-field extension |
| S37 | Multi-formation is a genuine extension, not trivial |
| S38 | Coexisting vs. alternative formations are distinct concepts |

**CONTESTED:**

| # | Issue | Options |
|---|-------|---------|
| C16 | Single-field vs. multi-field as primary approach | Architect: single / Theorist: multi / Skeptic: dilemma |
| C17 | D_t reformulation strategy | Three-level (Theorist) vs. unspecified |
| C18 | Competition energy vs. implicit competition | Explicit vs. emergent |
| C19 | Formation identity across time | Transport matrix vs. derived |

### 6. Recommended Phasing

- Phase 2: Complete single-formation
- Phase 3: Dynamics, sharp-interface, existence theorems
- Phase 4: Single-field multi-formation (non-overlapping)
- Phase 5: Multi-field theory (overlapping)

### 7. Meta-Observation

Round 8 is the first round with genuine unresolved disagreement. This is appropriate — multi-formation IS harder. The Skeptic's identification of the single-field / multi-field dilemma is the round's most important contribution. The theory cannot avoid this choice forever, but it can defer it responsibly.
