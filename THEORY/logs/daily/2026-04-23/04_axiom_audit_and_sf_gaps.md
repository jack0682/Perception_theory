# 04 — Axiom Audit + Single-Formation Gap Deep Analysis

**Session:** 2026-04-23 (continuation). User instruction: "axiom 검토하고 Single formation gap 분석."
**Target:** (Part A) canonical §6 Groups A-E 각 axiom × Three-Layer 의존성 + proposed S1-S4 self-consistency + redundancy/tension audit. (Part B) `SF_layer_classification.md` §8.1의 G-miss-1..4 단일-formation gap 심화 분석 + 해결 경로 제안.
**Depends on:** `canonical.md` §6, §11, §13 (axiom definitions + fixed commitments); `SF_layer_classification.md` (layer assignment); `step_cohesion.md` §10.1 (S1-S4 proposals); `working/SF/{cardinality_open, profile_deviation, symmetry_moduli, interface_scale, mode_count, thermal_extension}.md` (existing single-formation working theory).

---

# Part A — Axiom Audit (Groups A-E + proposed S1-S4)

## §A.1 Principle: axiom vs layer

An axiom **primarily constrains** a layer if it directly specifies the behavior of that layer's primitive. An axiom **secondarily constrains** another layer if its application shapes theorem-level statements there.

- **Layer 1 (topology)**: discrete $K$, basins, components, Morse index.
- **Layer 2 (geometry)**: smooth real quantities ($r_0, \xi_0, d_{\min}, \mu_k$).
- **Layer 3 (field)**: continuous $u: X \to [0,1]$.

Each axiom gets a **layer-primary classification** and a list of **derived consequences** per layer.

---

## §A.2 Group A — Soft Closure

### A.2.1 A1' (Conditional Extensivity, canonical §6)

**Statement**: For $u(x) \leq c^*$ and $(P_t u)(x) \geq u(x)$, $\mathrm{Cl}_t(u)(x) \geq u(x)$.

**Primary layer**: **L3** — direct constraint on the field-valued closure operator.

**Derived consequences**:
- **L2**: Defines scalar FP $c^* = \sigma(a_{\mathrm{cl}}(c^* - \tau_{\mathrm{cl}}))$ as real-valued geometric quantity determined by two parameters $(a_{\mathrm{cl}}, \tau_{\mathrm{cl}})$; $c^*$ unique iff $a_{\mathrm{cl}} < 4$.
- **L1**: Zero direct consequence (no $K$ statement).

**Tension / redundancy check**:
- With A3 (contraction): resolved — A1' was designed to coexist with $a_{\mathrm{cl}} < 4$.
- With CN1 (non-idempotence): consistent — extensivity below $c^*$ is compatible with non-idempotent behavior above.
- **No redundancy** with A2/A3/A4.

**Status in current theory**: **Essential**. Removing A1' eliminates self-regulation feature.

### A.2.2 A2 (Monotonicity)

**Statement**: $u \leq v$ pointwise $\Rightarrow \mathrm{Cl}_t(u) \leq \mathrm{Cl}_t(v)$.

**Primary layer**: **L3**.

**Derived consequences**:
- **L2**: With A1' gives $\mathrm{Cl}$ as monotone self-map with unique FP.
- **L1**: Guarantees basin structure is order-preserving — two basins cannot "cross" under $\mathrm{Cl}$ iteration.

**Tension check**:
- With A3 (contraction): both monotonicity + contraction → Perron-Frobenius-like structure, coherent.
- **No tension**.

**Status**: **Essential**. Monotonicity is core to sigmoid realization.

### A.2.3 A3 (Stabilization / Contraction)

**Statement**: Cauchy iteration $\|\mathrm{Cl}^{(n+1)} - \mathrm{Cl}^{(n)}\| \to 0$; for sigmoid, contraction rate $a_{\mathrm{cl}}/4$ when $a_{\mathrm{cl}} < 4$.

**Primary layer**: **L3**.

**Derived consequences**:
- **L2**: Establishes contraction rate (L2 real-valued) = $a_{\mathrm{cl}}/4$.
- **L1**: Unique FP means **closure does not generate multi-basin structure by itself**. Multi-basin structure comes from **energy landscape**, not closure (CN9 "two-landscape structure").

**Tension check**:
- With CN1 (non-idempotence): A3 is the **weaker** form replacing idempotence. By construction compatible.
- With A1' (extensivity): coexistent via $a_{\mathrm{cl}} < 4$ constraint.
- With MO-1 (Morse inapplicability on $\Sigma^K_M$): not relevant — A3 is on single $\mathrm{Cl}$, not manifold structure.
- **Clarity point**: A3 says "closure has unique FP"; does NOT say "energy has unique minimum". This distinction is CN9.

**Status**: **Essential** + central.

### A.2.4 A4 (Continuity)

**Statement**: $\mathrm{Cl}$ is continuous on $[0,1]^{X_t}$.

**Primary layer**: **L3** (regularity of field operator).

**Derived consequences**:
- Required for **T14 Łojasiewicz** convergence (combined with $b_D = 0$ from CN13).
- **L2**: Gradient of $\mathcal{E}_{\mathrm{cl}}$ is well-defined everywhere.
- **L1**: Standard Brouwer-type FP arguments (T6a) are applicable.

**Tension check**:
- **No tension**. Continuity is weakest possible regularity; strengthens to $C^\infty$ for sigmoid realization (stronger than axiom requires).

**Status**: **Essential foundational**.

### A.2.5 Group A synthesis

All four axioms are **L3-primary** with significant L2 / L1 derived consequences. **No redundancy, no tension**. A1' is the only axiom specific to closure's SCC character (self-regulation); A2/A3/A4 could appear in generic operator theory.

**Gap identification**: None identified in single-formation setting. Multi-formation K-field extensions (scc/multi.py) use A1'-A4 per formation — naturality ✅.

---

## §A.3 Group B — Soft Adjacency

### A.3.1 B1 (Nonnegativity), B2 (Symmetry), B3 (Locality), B4 (Non-Transitivity)

**Statement**: $\mathbf{N}(x,y) \geq 0$, $\mathbf{N}(x,y) = \mathbf{N}(y,x)$, $\mathbf{N}$ locally supported, $\mathbf{N}$ not transitive-preserving.

**Primary layer**: All four **L3** — direct constraints on kernel $\mathbf{N}: X \times X \to \mathbb{R}_{\geq 0}$.

**Derived consequences**:
- **L2**: Graph Laplacian $L = D - \mathbf{N}$ is symmetric PSD; Fiedler eigenvalue $\lambda_2 \geq 0$ (geometric quantity).
- **L1**: Connectedness of $G$ (from B3 locality + B1) gives graph connectivity property — L1 topological.

**Tension check**:
- **Directedness**: B2 adopts symmetry as default; extensions may relax. No current tension.
- With E2 (transport non-injectivity): both acknowledge asymmetric temporal behavior is distinct from instantaneous symmetry.

**Status**: **Essential**. Define the substrate.

**Gap identification**: 
- **Weighted graph**: B1-B4 allow arbitrary nonnegative weights. Canonical $\mathbf{N}$ is typically 0/1 (unweighted); no axiom on whether/how weights enter.
- **Graph-class specification**: SCC works on arbitrary graph; but theorems (Cor 2.2, Prop 1.3b(d) Φ_4) depend on D_4 symmetry. No axiom bridging generic B-axioms to D_4-specific theorems.

**New gap candidate NQ**:
- **NQ-A1 (new)**: Canonical axiom for **weight structure** on $\mathbf{N}$ (unweighted / integer-weighted / real-weighted). Currently ambiguous.

---

## §A.4 Group C — Soft Co-belonging

### A.4.1 C1 (Dependence on cohesion and adjacency)

**Statement**: $\mathbf{C}_t(x,y)$ depends on $u_t$ and $\mathbf{N}_t$.

**Primary layer**: **L3** (operator dependence).

**Status**: **Essential definitional** — excludes standalone $\mathbf{C}$.

### A.4.2 C2 (Distinction from adjacency)

**Statement**: $\mathbf{C}$ not reducible to $\mathbf{N}$; captures global joint-participation.

**Primary layer**: **L3** (operator's structural character).

**Tension**: CN12 "$\mathbf{C}_t$ is derived diagnostic" demoted $\mathbf{C}$ from energy term. Does C2 still have force?

**Answer**: Yes — C2 still characterizes what diagnostic $\mathbf{C}$ should do (capture joint-participation), even though $\mathbf{C}$ doesn't enter energy.

**Status**: **Retained despite demotion** (still gives content to the diagnostic).

### A.4.3 C3'' (Local Monotonicity)

**Statement**: $\mathbf{C}_t(x,x)$ monotone increasing in $u_t(x)$.

**Primary layer**: **L3** (pointwise property).

**Derived consequences**:
- **L2**: No direct consequence.
- **L1**: No direct consequence.

**Status**: **Weakened from C3 (=u(x))** to admit more realizations. Proved for resolvent.

### A.4.4 C4 (Symmetry)

**Statement**: $\mathbf{C}_t(x,y) = \mathbf{C}_t(y,x)$.

**Primary layer**: **L3**.

**Status**: **Implicit in v1.0, explicit in v1.2**. Automatic for resolvent construction.

### A.4.5 Group C synthesis

All four **L3-primary**. C3'' is the only axiom with weak (monotone) rather than specific functional content.

**Gap identification**: 
- **Since $\mathbf{C}_t$ is derived diagnostic (CN12)**, axioms C1-C4 are **under-utilized**. No theorem in canonical §13 invokes C1-C4 directly (only $\mathbf{C}$-free claims).
- **Possible redundancy**: If $\mathbf{C}$ is never required for a theorem, its axioms are **decorative** — documentation of what a good $\mathbf{C}$-diagnostic realization should satisfy, not load-bearing on framework.

**New gap candidate**:
- **NQ-A2 (new)**: **Formal status of Group C axioms**. Should Group C be demoted from "axioms" to "diagnostic specification"? Same demotion as $\mathbf{C}_t$ itself (CN12). Under current arrangement, Group C has axiom-level solemnity without axiom-level role.

---

## §A.5 Group D — Distinction

### A.5.1 D-Ax1 (Exterior Sensitivity)

**Statement**: $\mathbf{D}_t(x; 1-u_t)$ depends on relational configuration of $1-u$, not just $u_t(x)$.

**Primary layer**: **L3**.

**Derived consequences**:
- **L2**: Non-local dependence → gradient of $\mathcal{E}_{\mathrm{sep}}$ extends beyond local neighborhood.
- **L1**: No direct.

### A.5.2 D-Ax2 (Asymmetry)

**Statement**: High distinction when interior support ≫ exterior support at $x$.

**Primary layer**: **L3**.

### A.5.3 D-Ax3 (Boundary Sensitivity)

**Statement**: Structural awareness via spatial structure of $P_t(1-u)$; explicit gradient $b_D \cdot g_t$ set to zero (or $\varepsilon$-smoothed) for **analyticity**.

**Primary layer**: **L3** (direct field-level).

**Derived consequences**:
- **L2**: Enables T14 Łojasiewicz via analyticity.
- **L1**: No direct; **but** L1 depends on T14 convergence to well-defined critical point.

**Tension check**:
- **$b_D = 0$ vs "boundary sensitivity"**: tension at face value. Resolved by "boundary sensitivity is preserved through $P_t(1-u)$ structure" (relocate sensitivity from gradient to aggregator).
- **CN13 commitment**: "$b_D = 0$ for distinction" makes D-Ax3 a structural choice, not a derivation.

**Status**: **Load-bearing but conditionally** — $b_D = 0$ is a commitment that **rules out** certain sharper distinction realizations (hard-boundary discriminators) in favor of smooth theory.

### A.5.4 Group D synthesis

All three **L3-primary**. D-Ax3 has CN13 dependence ($b_D = 0$).

**Gap identification**:
- **D-Ax3 is the fragile axiom**: depends on CN13 commitment which is itself at-risk if thermal extension (H-Th1 Langevin) breaks analyticity via noise.
- **At thermal extension**: analyticity survives (Gaussian noise on smooth function gives smooth process), so D-Ax3 preserved. But **multiplicative noise** or **Lévy processes** would break it.

**New gap**:
- **NQ-A3 (new)**: **Distinction at finite T**: does D-Ax3 survive H-Th1 Langevin? Conjectural yes, needs confirmation.

---

## §A.6 Group E — Temporal Transport and Persistence

### A.6.1 E1 (Sub-Stochasticity)

**Statement**: $\sum_y \mathbf{M}_{t \to s}(x, y) \leq 1$.

**Primary layer**: **L3** (kernel-level constraint). **Dynamic** (temporal).

**Derived consequences**:
- **L2**: Transport moves mass with sub-conservation.
- **L1**: Allows formation disappearance (mass → 0 → no K counter).

### A.6.2 E2 (Non-Injectivity)

**Statement**: $\mathbf{M}$ may be many-to-many.

**Primary layer**: **L3** + **L1** (multi-to-multi bridges K-sectors across time).

**Derived consequences**:
- K-changes (merge/split) are permitted by E2.

### A.6.3 E3 (Core Inheritance — solution constraint)

**Statement**: For persistent formations, $\sum_y \mathbf{M}(x,y) u_s(y) \geq \delta$ for $x \in \mathrm{Core}_t$.

**Primary layer**: **L2 × L1** (bridge: L2 core-mass measure, L1 persistence).

**Reclassification note (v2.0)**: E3 is **solution constraint**, not operator axiom. Characterizes good solutions, not valid kernels.

**Tension check**:
- **E3 vs E1**: E1 says $\sum \mathbf{M} \leq 1$; E3 says $\sum \mathbf{M} \cdot u_s \geq \delta$. Compatible since $u_s \leq 1$ and $\delta$ is small.

### A.6.4 E4 (Structural Sensitivity)

**Statement**: $\mathbf{M}(x, y)$ depends on structural features beyond spatial proximity.

**Primary layer**: **L3**.

**Honesty note (canonical)**: Provisional transport breaks self-referential loop. Open problem (§12) to make transport fully self-referential.

### A.6.5 Group E synthesis

**L3-primary, Dynamic**. E3 is the only axiom explicitly **layer-crossing** (reclassified v2.0).

**Gap identification**:
- **Self-referential transport (OP-0011)**: existing open problem.
- **E3 as solution constraint**: elegant but leaves kernel under-constrained.

**Status**: Transport axioms are **active development area** (`working/SF/thermal_extension.md` + OP-0011 + §T_thermal H-Th4).

---

## §A.7 Proposed S1-S4 (step_cohesion.md §10.1)

### A.7.1 S1 (Step-Cohesion Decomposition)

**Statement**: Every well-separated $u^* \in \Sigma_m$ local minimizer admits unique $u^* = \sum_k \phi_k^* + r$ with $K \in \mathbb{Z}_{\geq 0}$ topological invariant.

**Primary layer**: **L1** (integer $K$, topological invariant).

**Derived consequences**:
- **L3**: Each $\phi_k^*$ is L3 tanh soliton (Cor 2.2).
- **L2**: Per-formation $(r_k, \xi_0)$ are L2 geometric.

**Redundancy check**:
- **Overlap with T-Merge (a)** (canonical Cat A): T-Merge (a) says well-separated K-formations are local minima. S1 says decomposition exists + unique.
- **These are complementary**: T-Merge (a) is **existence of local min within K-sector**; S1 is **decomposition at such a min**. S1 strictly strengthens T-Merge (a) by adding uniqueness of decomposition.
- **No redundancy**.

**Tension check**:
- **With T-Merge (b)** (K=1 < K=2 isoperimetric): T-Merge (b) is about energy ordering of global min; S1 is about any local min structure. Compatible.
- **With T1 (existence)**: T1 gives minimizer existence on $\Sigma_m$; S1 characterizes those that are well-separated. S1 does **not claim** that all minimizers are well-separated — hence non-conflict.
- **"Well-separated" condition**: requires precise meaning. In §MF §3.6 proof, $d_{\min} \geq d_{\mathrm{sep}}$ with $\exp(-d_{\mathrm{sep}}/\xi_0) < \eta$. Quantitative; not conceptually problematic.

**Gap**:
- **Non-well-separated minimizers**: S1 doesn't address. In strongly-overlapping regime, decomposition non-unique. **NQ-A4 (new)**: canonical treatment of overlap regime.

**Status**: **Proposal robust for well-separated**; overlap extension open.

### A.7.2 S2 (Three-Layer Hierarchy)

**Statement**: Layer 1 (topology, $K$), Layer 2 (geometry, real-valued), Layer 3 (field, $u$).

**Primary layer**: **Meta-organizational** (not a single-layer axiom).

**Role**: Organizational framework across all claims.

**Redundancy check**:
- **Overlap with existing axioms?**: No existing axiom declares the layer structure. S2 introduces new organizational vocabulary.

**Tension check**:
- **27% "Mixed" claims** (§SF_layer_classification §7.3): strict 3-partition doesn't hold. S2 needs to admit Mixed as first-class, not as residual.
- **Proposal**: S2 should say "layers with explicit bridge-claim allowance".

**Gap**:
- **Formal definition of "bridge claim"**: informal in current framing. Need formal typing.
- **NQ-A5 (new)**: Formal type theory of SCC claims (Layer 1 / Layer 2 / Layer 3 / bridge-set / meta).

**Status**: **Organizational; needs formalization**. Currently under-specified.

### A.7.3 S3 (Protocol-Parameterized Observable)

**Statement**: $O_{\mathrm{obs}}(\beta, \pi)$ factors via protocol $\pi$; dynamic observables require $\pi$.

**Primary layer**: **Dynamic + L1** (protocol selects basin = L1).

**Redundancy check**:
- **Overlap with existing axioms**: None — no existing axiom formalizes protocol dependence. CN6 "K kinetically determined" is closest but weaker.

**Tension check**:
- **Vs E4 (Structural Sensitivity)**: E4 is about transport kernel's dependence on features; S3 is about protocol dependence. Orthogonal concerns.
- **Vs CN6 (K kinetic)**: S3 strengthens CN6 with explicit $\pi$-dependence.

**Gap**:
- **Protocol space $\Pi$**: what is the set of admissible protocols? Currently informal (Fiedler-init, random-init, warm-start).
- **NQ-50 (existing)**: Protocol specification language — a canonical observable should always state $(\beta, c, G, \pi)$.

**Status**: **Strong proposal; needs protocol formalization (NQ-50)**.

### A.7.4 S4 (Static/Dynamic Decomposition)

**Statement**: Static invariants describe landscape; dynamic observables require protocol.

**Primary layer**: **Meta**.

**Role**: Formalizes Static/Dynamic Separation Principle (R22 §17.6).

**Redundancy check**:
- **Overlap with S3**: S4 is generalization; S3 is the specific case for dynamic observables.
- **Overlap with CN15 (proposed)**: CN15 = S4 essentially. Either keep both (CN for commitment, S4 for axiom) or merge.

**Tension check**:
- **4 falsifications (R17/R19/R20/V7 P1)**: S4 is the **axiomatic correction** that those falsifications demand. No tension; S4 is **inductive conclusion** from falsifications.

**Status**: **Empirically supported; formally proposed**. Should merge with CN15 or clearly differentiate.

### A.7.5 S1-S4 synthesis

- **S1**: L1-primary theorem-like axiom (existence + uniqueness of decomposition).
- **S2**: meta-organizational.
- **S3**: L1 + dynamic primary.
- **S4**: meta-organizational (overlaps CN15).

**Redundancy issue**: S2 and S4 are both meta; may consolidate to single "Organizational Axiom" pair.
**Tension issue**: S2 needs "Bridge" layer formalization (27% Mixed).

---

## §A.8 Cross-axiom tension and redundancy audit

### A.8.1 Cross-group tensions identified

| Pair | Tension | Resolution status |
|---|---|---|
| A1' × A3 | Historical: A1 vs A3 incompatible for sigmoid | Resolved by A1' reformulation |
| D-Ax3 × CN13 | $b_D = 0$ weakens D-Ax3 | Resolved (CN13 commitment) |
| E3 × E1 | Upper and lower bounds on mass flow | Compatible via $\delta$ small |
| C1-C4 × CN12 | Axioms for demoted diagnostic | **Unresolved** (NQ-A2) |
| S2 × observed Mixed 27% | Strict 3-partition | **Unresolved** (NQ-A5) |
| S3 × protocol space | Informal $\pi$ | **Unresolved** (NQ-50 existing) |

### A.8.2 Redundancy

**Load-bearing axioms**:
- A1', A2, A3, A4 (all essential for closure FP theory).
- B1-B4 (substrate).
- D-Ax1-Ax3 (+ CN13).
- E1, E2, E4 (transport kernel constraints); E3 (solution constraint, reclassified).
- S1 (Formation Quantization structural).

**Potentially redundant or decorative**:
- **C1-C4**: No theorem in canonical §13 invokes directly (except in the proof of C-Axioms which is self-referential). **Demotion candidate** to "Diagnostic Specification" (NQ-A2).
- **S4**: Overlaps CN15. Consolidation candidate.

### A.8.3 Missing axiom candidates

From layer analysis + session deliverables:

- **Axiom (proposed) for Graph Class Specification** (NQ-A1): Weighted/unweighted $\mathbf{N}$, symmetry group commitments.
- **Axiom (proposed) for Protocol Space** (NQ-50): Formal $\pi \in \Pi$.
- **Axiom (proposed) for Bridge Layer** (NQ-A5): Handle 27% Mixed as first-class.
- **Axiom (proposed) for Thermal Framework** (P-F existing, now SP-F structured): Langevin SDE choice + boundary treatment (NQ-67).

---

## §A.9 Axiom audit summary

| Axiom | Layer primary | Essential? | Tension | Status post-audit |
|---|---|---|---|---|
| A1' | L3 | Y | None | Active |
| A2 | L3 | Y | None | Active |
| A3 | L3 | Y | None | Active |
| A4 | L3 | Y | None | Active |
| B1 | L3 | Y | None | Active (weights NQ-A1 open) |
| B2 | L3 | Y | Default; extensible | Active |
| B3 | L3 | Y | None | Active |
| B4 | L3 | Y | None | Active |
| C1 | L3 | ? | CN12 tension | Demotion candidate NQ-A2 |
| C2 | L3 | ? | CN12 tension | Demotion candidate |
| C3'' | L3 | ? | CN12 tension | Demotion candidate |
| C4 | L3 | ? | CN12 tension | Demotion candidate |
| D-Ax1 | L3 | Y | None | Active |
| D-Ax2 | L3 | Y | None | Active |
| D-Ax3 | L3 | Y | CN13 $b_D=0$ | Active, thermal extension NQ-A3 |
| E1 | L3 dyn | Y | None | Active |
| E2 | L3 dyn | Y | None | Active |
| E3 | L2×L1 dyn | Y (as solution constraint) | Reclassified v2.0 | Active |
| E4 | L3 dyn | Y | None | Active (OP-0011) |
| S1 | L1 | Y | Overlap regime undefined | Proposed; well-separated ready |
| S2 | Meta | Y | Mixed 27%, Bridge NQ-A5 | Proposed; needs refinement |
| S3 | L1+dyn | Y | Protocol space NQ-50 | Proposed; needs $\Pi$ definition |
| S4 | Meta | Y | Overlaps CN15 | Proposed; consolidation needed |

**Audit result**: 15 essential axioms + 4 proposed + 4 demotion candidates (C1-C4) + 4 new axiom candidates (NQ-A1..A3 + weighted graph, protocol space, bridge layer, thermal framework).

---

# Part B — Single-Formation Gap Deep Analysis

From `SF_layer_classification.md` §8.1, four gaps were flagged:

- **G-miss-1**: L3 corner behavior (Σ_m manifold-with-corners energy/regularity).
- **G-miss-2**: $c_0$-Counting universality across graph classes.
- **G-miss-3**: $\xi_0$ / profile for non-regular graphs.
- **G-miss-4**: Observed-$\widehat K = 1$ sufficient condition (protocol-independence).

Each analyzed below.

---

## §B.1 G-miss-1: L3 corner behavior on $\Sigma_m$

### B.1.1 Setup

Canonical Prop 1.1 (Cat A): $\Sigma_m = \{u \in [0,1]^n : \sum u_i = m\}$ is convex polytope, **manifold with corners**. Corners occur where $u_i = 0$ or $u_i = 1$ for some site.

Prop 1.2 (Cat A): Fiber dimension $2n-2$ for interior splits; **cone singularity at $m_j \in \{0, M\}$** (in K-field architecture $\Sigma^K_M$).

### B.1.2 What's established (L3 at interior)

- **Interior** ($0 < u_i < 1$ all $i$): smooth manifold, Łojasiewicz works (T14).
- **Convergence** of gradient flow from interior to interior: Cat A.

### B.1.3 What's missing (L3 at corner)

Three questions:

**Q-B.1.a**: Is $\mathcal{E}(u)$ **differentiable** at $u \in \partial \Sigma_m$ (boundary sites with $u_i \in \{0, 1\}$)?

**Analysis**:
- $\mathcal{E}_{\mathrm{bd}} = \sum_i W(u_i) + 2\alpha \sum_{(i,j)} (u_i - u_j)^2$ — smooth as polynomial/double-well; differentiable.
- $\mathcal{E}_{\mathrm{cl}} = \sum_i (u_i - \mathrm{Cl}(u)_i)^2$ — sigmoid closure is $C^\infty$ inside $[0,1]$; at boundary, sigmoid evaluated at $\pm\infty$ pre-image is $\{0, 1\}$ — **still smooth as function of $u$** because sigmoid input $P_t u$ is bounded.
- $\mathcal{E}_{\mathrm{sep}}$ — polynomial.
- $\mathcal{E}_{\mathrm{tr}}$ — depends on transport kernel; smooth for entropy-regularized OT (canonical §9.5).

**Conclusion Q-B.1.a**: $\mathcal{E}$ is $C^\infty$ on closed $[0,1]^n$, including $\partial \Sigma_m$. **Differentiable**. No singularity.

**Q-B.1.b**: Does gradient flow $\dot u = -\Pi_{\Sigma_m}\nabla\mathcal{E}$ **respect the boundary** (i.e., $u_i \in [0,1]$ preserved)?

**Analysis**:
- At $u_i = 0$ with $\partial_i \mathcal{E} > 0$: projection $\Pi_{\Sigma_m}$ onto tangent $\sum v_i = 0$ doesn't automatically preserve $u_i \geq 0$.
- **Reality**: need **bound-constrained gradient flow** — projection onto $\Sigma_m \cap [0,1]^n$ (polytope), not just $\Sigma_m$.
- In `CODE/scc/optimizer.py` (based on CLAUDE.md): uses "semi-implicit projected gradient, BB step" — i.e., projected onto the constraint polytope.

**Conclusion Q-B.1.b**: Gradient flow **does** respect boundary via projection; **canonical T14 statement uses $\Pi_{\Sigma_m}$ but implementation uses $\Pi_{\Sigma_m \cap [0,1]^n}$**. There's a **latent gap** between stated theorem (simple $\Pi_{\Sigma_m}$) and needed operation.

**Q-B.1.c**: Does **Łojasiewicz inequality** hold at corner critical points?

**Analysis**:
- Interior critical points: Łojasiewicz works (analytic + compact + interior).
- Boundary critical points: Łojasiewicz on semi-algebraic sets includes polytope with corners — **theorem still applies** (Kurdyka-Łojasiewicz extended to semi-algebraic).
- **But**: with bound constraints, the KKT conditions include **complementarity** $u_i \cdot \partial_i\mathcal{E} = 0$. Critical points satisfy KKT, not $\nabla\mathcal{E} = 0$.

**Conclusion Q-B.1.c**: Łojasiewicz extends, but **convergence-to-KKT-points** is the correct statement, not "convergence to $\nabla\mathcal{E} = 0$".

### B.1.4 G-miss-1 structured statement

> **G-miss-1 (single-formation corner regularity)**: Canonical T14 states convergence to "critical point" under gradient flow. For bounded $[0,1]^n$ constraint, the correct endpoint is **KKT point** (including boundary strata). Canonical §13 does not:
> (a) state which projection operator is used ($\Pi_{\Sigma_m}$ vs $\Pi_{\Sigma_m \cap [0,1]^n}$);
> (b) characterize KKT points vs interior criticals;
> (c) prove Łojasiewicz on semi-algebraic extension.
>
> Implementation-level correctness (scc/optimizer.py) is **ahead of** theorem-level statement.

### B.1.5 Resolution path

**Short (canonical errata)**:
- Add remark to T14: "Gradient flow uses $\Pi_{\Sigma_m \cap [0,1]^n}$; convergence is to KKT critical point".
- Cite Kurdyka-Łojasiewicz extension (Bolte-Daniilidis-Lewis 2007) for semi-algebraic functions.

**Long (research)**:
- Characterize KKT structure at $[0,1]^n$ boundary; how many boundary-KKT points? (Related to Morse index at corners.)
- Formal statement of "corner critical point" + inclusion in $c_0$-count (g-miss-2).

### B.1.6 Category

**Resolution**: Cat A achievable with errata (existing Bolte-Daniilidis-Lewis framework). **Promote priority**: medium (implementation is correct; only theorem statement needs cleanup).

---

## §B.2 G-miss-2: $c_0$-Counting universality

### B.2.1 Setup

Round 8 Universal $c_0$-Counting Theorem (logs 2026-04-22): claims universal counting formula across graph classes via equivariant Crandall-Rabinowitz. Listed as Cat A.

Round 8 bundled: specific count for {cycle $C_n$, torus $T^2$, 2D square free BC, complete $K_n$, regular lattice}. Claimed "universal" via equivariant CR machinery.

### B.2.2 What's established

- **D_4 symmetric 2D square**: explicit $c_0$ values (Round 4 $\Phi_4$ axis selection, Round 8).
- **$C_n$**: Round 4 first-pitchfork, Round 5 Lock-In.
- **$T^2$**: Round 4 + Round 5 moduli.
- **$K_n$**: Round 8 "two-valued exact".
- **Regular lattice (general $d$)**: Round 8 framework via irrep rules.

### B.2.3 What's missing

**Q-B.2.a**: **Non-regular but symmetric** graphs (e.g., bipartite $K_{m,n}$, Petersen graph, Cayley graph of non-abelian group).

- Equivariant CR requires irreducible representation analysis. For non-abelian Aut(G), irreps are higher-dimensional, and $\Phi_4$-type ratio $(A_2/A_1)$ may not be $\{2, 4\}$.
- **Gap**: Universal $c_0$-Counting of Round 8 proved the $\{2, 4\}$ classification for abelian / $D_4$ cases; general classification for all finite groups open.

**Q-B.2.b**: **Generic random graphs** ($\mathrm{Aut}(G) = \{e\}$).

- No symmetry → no equivariant CR.
- $c_0$ count is fully enumerative; hard to derive universal formula.
- **Gap**: Hole in Round 8's "universal" claim — universal only for **non-trivially-symmetric** graphs.

**Q-B.2.c**: **Weighted graphs**.

- Canonical axiom Group B allows arbitrary weights (NQ-A1).
- Different weight structures induce different Hessian spectra → different $c_0$.
- **Gap**: Weight-sensitivity formula for $c_0$.

### B.2.4 G-miss-2 structured statement

> **G-miss-2 (c_0-Counting scope)**: Round 8 Universal $c_0$-Counting Theorem is proved for abelian-Aut-group or $D_4$-symmetric graphs. Three open sub-regimes:
> (a) non-abelian Aut(G) with higher-dim irreps,
> (b) generic graphs ($\mathrm{Aut}(G) = \{e\}$),
> (c) weighted graph variants.

### B.2.5 Resolution path

**Short (restrict claim scope)**:
- Reclassify Round 8 "universal" from Cat A to Cat A (abelian/D_4 only). Non-abelian → Cat B, generic → Cat C, weighted → open.

**Medium (non-abelian extension)**:
- Equivariant Morse theory (Wasserman 1969) for compact group action.
- Specific representations: $S_n$, $A_n$, higher dihedral.
- Paper target: 2-3 months.

**Long (generic graph)**:
- Likely requires **random matrix theory** (Hessian spectrum distribution).
- Beyond canonical framework scope; application paper.

### B.2.6 Category

**Current**: Cat A misleading (restricted to abelian/D_4).
**Post-refinement**: Cat A (abelian/D_4) + Cat B/C/open (other sub-regimes). Explicit scope statement.

---

## §B.3 G-miss-3: $\xi_0$ / profile for non-regular graphs

### B.3.1 Setup

Cor 2.2 (Cat A, 2D D_4 lattice): $\phi^*(x) \approx \frac{1}{2}(1 - \tanh(d/\xi_0))$ with $\xi_0 = \sqrt{\alpha/\beta}$.

`profile_deviation.md` (NQ-32): Full-energy SCC minimizer deviates from pure tanh; shape exponent $p$ varies.

R21 (logs 2026-04-22 §17.10-17.13): Two Shape Regimes (A = sharp p≥3.5; B = near-tanh p≈1.2). Regime boundary = **absolute α** (X2 D1), NOT $\xi_0/a$.

### B.3.2 What's established

- $\xi_0 = \sqrt{\alpha/\beta}$ for 2D D_4 lattice (Cor 2.2).
- Regime A/B on D_4 lattice with α threshold ≈ 10 (X2).
- $C_n$ (1D cycle) — tanh profile assumed but not explicitly verified at scale (NQ-39).

### B.3.3 What's missing

**Q-B.3.a**: **Non-regular lattices**: SBM, barbell, random geometric.

- For non-regular, "interface" is ill-defined (no natural boundary between blocks).
- Block-to-block boundary on SBM: what's $\xi_0$?
- **Gap**: Cor 2.2 inapplicable to non-regular.

**Q-B.3.b**: **Hierarchical graphs**: small-world, scale-free.

- Different spectral dimension $d_{\mathrm{eff}}$ → different Allen-Cahn scaling.
- $\xi_0 = \sqrt{\alpha/\beta}$ is 2D-specific. On hierarchical, $\xi_0$ may scale differently with $\beta$.
- **Gap**: graph-spectral-dim-aware $\xi_0$ formula.

**Q-B.3.c**: **Weighted lattices**: continuous lattice with weight function $w(x, y)$.

- $L = D - W$ spectrum changes; $\xi_0$ scales via $\lambda_2(L)$.
- **Gap**: weight-dependent $\xi_0$ formula.

### B.3.4 G-miss-3 structured statement

> **G-miss-3 (profile for non-regular graphs)**: Cor 2.2's $\xi_0 = \sqrt{\alpha/\beta}$ is 2D D_4 lattice-specific. Extension to (a) non-regular (SBM, barbell), (b) hierarchical (small-world, scale-free), (c) weighted lattices is open. Current working treatment: NQ-33 "$d_{\mathrm{eff}}$ precise definition" carries this.

### B.3.5 Resolution path

**Short (NQ-33 formal)**:
- Define $d_{\mathrm{eff}}(G) = 2\cdot(\text{slope of log-log spectral density at low end})$ or similar spectral-dim definition.
- Re-derive $\xi_0 = \sqrt{\alpha/\beta} \cdot f(d_{\mathrm{eff}})$ for abstract $d_{\mathrm{eff}}$.

**Medium (graph-class specific)**:
- SBM: $\xi_0$ governed by block-interface Hessian eigenvector.
- Barbell: Cheeger constant $h(G)$ as proxy — $\xi_0 \sim 1/\sqrt{h(G)}$.
- Random geometric: $\xi_0 \sim r_c$ (connection radius).

**Long (unified framework)**:
- Integral spectral formula: $\xi_0^{-2} \sim \int \rho(\lambda) \cdot \lambda\, d\lambda$ (weighted by spectral density).

### B.3.6 Category

- **Short**: Cat B achievable via NQ-33 formalization.
- **Medium**: Cat B per graph class; union Cat C.
- **Long**: Open research direction.

---

## §B.4 G-miss-4: Observed-$\widehat K = 1$ sufficient condition

### B.4.1 Setup

R17 c=0.3 2D square β=30: $\widehat K = 7.76$ (gradient flow, 50 seeds).
R18 c=0.5 2D torus: $\widehat K = 1.00$ (50 seeds, perfect).
R19 c=0.7 2D square: $\widehat K = 1.00$ (perfect at β=0.5-10), 1.08 at β=30 (mostly 1).

**Observation**: Some regimes give $\widehat K = 1$ with **near-zero variance**; others give $\widehat K \gg 1$ with spread.

**Gap**: Canonical has no theorem saying "under condition $X$, gradient flow from any random init lands in $\mathcal{B}_1$ almost surely."

### B.4.2 What's established

- **T-Merge (b)** (Cat A): K=1 is **global** energy minimum. But global min doesn't imply gradient-flow destination from arbitrary IC (landscape has metastable local mins).
- **R22 V5 (C-X1V5)**: Protocol-dependent basin selection. Same (β, c, G) can give K=1 or K=HIGH depending on protocol.
- **R18 empirical**: c=0.5 torus shows K=1 nearly universally across protocols (Cat A empirical).

### B.4.3 What's missing

**Q-B.4.a**: For which $(β, c, G)$ is **$\mathcal{B}_1$ the attracting basin for almost every initial condition**?

**Hypothesis** (tentative): 
> **G-miss-4 Hypothesis**: $\widehat K = 1$ almost surely iff the **basin volume** $\mathrm{Vol}(\mathcal{B}_1) / \mathrm{Vol}(\Sigma_m) \to 1$.

For c=0.5 torus: high symmetry → $\mathcal{B}_1$ is the "radially symmetric" configuration which has large basin volume.
For c=0.3 2D square: low symmetry for K=1 config (off-center); small $\mathcal{B}_1$ basin, larger other basins.

**Q-B.4.b**: **Quantitative condition**: What spectral/structural feature of $(β, c, G)$ gives large $\mathrm{Vol}(\mathcal{B}_1)$?

- Fiedler eigenvalue: strong $\lambda_2 \gg \lambda_3$ → K=1 basin dominates (single mode dominates at critical regime).
- $c$ regime: $c = 1/2$ is **Regime II** (R6 classification); has $\gamma_D(c) = 0$ cubic term zero, suggesting symmetric bifurcation structure.
- **Hypothesis sub-form**: $\widehat K = 1$ generically iff (i) $\lambda_2(L)/\lambda_3(L) \gg 1$ (spectral gap), AND (ii) $c \approx 1/2$ (Regime II).

### B.4.4 G-miss-4 structured statement

> **G-miss-4 (sufficient condition for $\widehat K = 1$)**: Empirically, certain $(β, c, G)$ regimes give $\widehat K = 1$ with near-zero variance across initialization protocols (e.g., c=0.5 torus). No theorem characterizes **which regimes** have this property. Hypothesis: $\widehat K = 1$ a.s. iff (i) $\lambda_2/\lambda_3 \gg 1$ and (ii) $c \approx 1/2$. NOT yet proved.

### B.4.5 Resolution path

**Short (empirical verification)**:
- Run $\widehat K$ measurement across ($c, G$) grid at fixed β.
- Correlate with $(\lambda_2/\lambda_3, |c - 1/2|)$.
- If hypothesis holds, tentative Cat C empirical.

**Medium (theoretical)**:
- **Basin volume estimate** for $\mathcal{B}_1$ via Gaussian integration around K=1 minimizer.
- $\mathrm{Vol}(\mathcal{B}_1) \sim \det(H_1)^{-1/2}$ where $H_1$ is K=1 Hessian.
- Compare to $\mathcal{B}_K$ for K≥2.

**Long (rigorous)**:
- Large-deviation principle for gradient flow — for a.e. initial condition, descent direction aligns with steepest mode (Fiedler). If Fiedler mode is K=1, $\mathcal{B}_1$ dominates.
- Freidlin-Wentzell-type theory at zero T.

### B.4.6 Category

- **Empirical characterization (short)**: Cat B achievable.
- **Basin volume (medium)**: Cat C requires Gaussian approximation.
- **Rigorous (long)**: Open; connects to H-Th2 (basin-volume-weighted occupation).

---

## §B.5 New single-formation gap candidates from axiom audit (Part A feedback)

Axiom audit (Part A) revealed additional single-formation gaps:

### B.5.1 G-miss-5 (new): Corner KKT critical point count

From §B.1 Q-B.1.c: Corner KKT points vs interior critical points in $c_0$-count.

**Question**: Round 8 $c_0$-Counting covers interior critical points only (implicitly). Does SCC have KKT critical points at corners (boundary strata)?

**Analysis**:
- At corner $u_i = 0$ with $\partial_i \mathcal{E} > 0$: complementarity $u_i \partial_i \mathcal{E} = 0$ automatically satisfied.
- These **boundary KKT points** exist generically.
- **Gap**: $c_0$-count should include them — ** effectively $c_0^{\mathrm{total}} = c_0^{\mathrm{interior}} + c_0^{\mathrm{boundary}}$**.
- Empirically untouched; theoretically under-specified.

**Resolution path**: Extend $c_0$-Counting framework to stratified Morse (Goresky-MacPherson 1988). Cat B achievable; writing commitment needed.

### B.5.2 G-miss-6 (new): $\mathbf{C}_t$ diagnostic role (axiom demotion question)

From §A.4.5 NQ-A2: Group C axioms (C1-C4) are decorative if no theorem invokes $\mathbf{C}$. Are there **single-formation facts** that **need** $\mathbf{C}$?

**Analysis**:
- $\mathbf{C}$ is demoted to diagnostic (CN12).
- No energy term uses $\mathbf{C}$.
- **But**: `scc/predicates.py` + canonical §5.5 use $\mathbf{C}$ for "Inside" predicate and Bind diagnostic.
- **Gap**: Check if $\mathbf{C}$-based diagnostics for single formation require C1-C4 OR if any weaker property suffices.

**Resolution path**: Per-diagnostic analysis (Bind, Sep, Inside, Persist) to see which C axioms are load-bearing. Likely outcome: C3'' (monotonicity) is sufficient; C4 (symmetry) for resolvent realization. Cat A achievable with careful reading.

### B.5.3 G-miss-7 (new): Thermal extension of single-formation theory

From §A.5.4 NQ-A3: Does single-formation Cor 2.2 tanh profile survive at T > 0?

**Analysis**:
- Zero-T: Cor 2.2 Cat A.
- Finite-T under H-Th1 Langevin: noise blurs interface; expected $\xi_0^{\mathrm{T}} > \xi_0^{0}$.
- **Gap**: quantitative law $\xi_0(T) = \xi_0 \sqrt{1 + T/T_0}$ or similar; no current derivation.

**Resolution path**: Direct Langevin perturbation around Cor 2.2 tanh profile. Cat C achievable. Connects to `working/SF/thermal_extension.md`.

---

## §B.6 Priority + resolution matrix

| Gap | Severity | Resolution cost | Priority for Stage 2/3 |
|---|---|---|---|
| G-miss-1 (corner regularity) | Low | Short (errata) | Medium — cleanup |
| G-miss-2 (c_0 universality scope) | Medium | Short-Medium | High — impacts Round 8 claim |
| G-miss-3 (non-regular $\xi_0$) | Medium | Medium-Long | Medium — NQ-33 long-standing |
| G-miss-4 ($\widehat K = 1$ sufficiency) | High | Short empirical / Medium theoretical | **Highest** — empirically observed phenomenon undescribed |
| G-miss-5 (corner KKT count) | Low | Medium | Low — enrichment |
| G-miss-6 ($\mathbf{C}$ axiom demotion) | Low | Short (analysis) | Low — cleanup |
| G-miss-7 (thermal single-formation) | Medium | Medium | Medium — G5 scope connection |

**Top priority**: G-miss-4 (empirical phenomenon of $\widehat K = 1$ regimes demands theoretical explanation).

---

## §C. Consolidated output

### §C.1 Axiom audit deliverable

- **4 proposed new axiom candidates** (NQ-A1 weight structure, NQ-A2 Group C demotion, NQ-A3 D-Ax3 thermal, NQ-A5 Bridge layer).
- **C1-C4 demotion proposal** to "Diagnostic Specification" (parallel with $\mathbf{C}_t$'s CN12 demotion).
- **S2 refinement**: formalize Bridge layer for Mixed category (27%).
- **S3 / NQ-50**: Protocol space $\Pi$ formal definition.
- **S4 / CN15**: consolidation recommendation.

### §C.2 Single-formation gap deliverable

- **4 original gaps re-analyzed** (G-miss-1..4) with structured statements + resolution paths + Cat projections.
- **3 new gaps** identified from axiom audit (G-miss-5..7).
- **Priority matrix** (§B.6): G-miss-4 highest.

### §C.3 New NQ consolidated (this file adds to session)

- **NQ-A1**: Canonical axiom for $\mathbf{N}$ weight structure.
- **NQ-A2**: Formal status of Group C axioms (demotion decision).
- **NQ-A3**: D-Ax3 under finite-T.
- **NQ-A4**: Canonical treatment of strongly-overlapping formations (beyond S1 well-separated).
- **NQ-A5**: Bridge layer formalization.
- **NQ-76 (from G-miss-5)**: Corner KKT critical point count.
- **NQ-77 (from G-miss-6)**: Per-diagnostic $\mathbf{C}$ axiom dependency.
- **NQ-78 (from G-miss-7)**: Cor 2.2 at finite T, Langevin perturbation.

**Note on numbering**: NQ-A1..A5 are axiom-audit tagged. NQ-76..78 continue from §03's NQ-75.

---

## §D. Integration with this session's earlier deliverables

### D.1 Back-reference to `SF_layer_classification.md`

- §8.1 G-miss-1..4 are fleshed out in §B.1..B.4 here.
- §9 axiom-layer dependency summary: refined in §A with primary/derived distinction.
- **Update candidate**: Promote this analysis into `SF_layer_classification.md` §8 expansion.

### D.2 Back-reference to `MF_multi_quantization.md`

- §2.3 Axiom naturality audit AN ✅ across S1-S4: this file §A.7 confirms with tension points.
- §3.6 Formation Quantization Uniqueness: this file §A.7.1 shows it overlaps with T-Merge (a) complementarily.

### D.3 Back-reference to `03_integration_and_new_open.md`

- §2.2 proposed CN15/16/17: this file §A.7.4 notes S4 ↔ CN15 overlap; consolidation proposed.
- §5 new NQ: this file adds 8 more (NQ-A1..A5 + NQ-76..78).

---

## §E. Recommended Stage 2 Axiom Audit next steps

Based on this audit:

1. **Formalize canonical §6 revision**:
   - Add "Group S" with S1-S4 axioms.
   - Demote Group C axioms to "§6.C Diagnostic Specification" (NQ-A2).
   - Add layer annotation to each axiom.
2. **Address NQ-A5 (Bridge layer)**:
   - 27% Mixed is high; refine Three-Layer to Four-Layer or allow Bridge as first-class.
3. **NQ-50 Protocol language**:
   - Formal $\pi \in \Pi = $ {Fiedler-init, random-init, warm-start, ...} with signature specification.
4. **G-miss-4 empirical investigation**:
   - $\widehat K = 1$ sufficient condition is the single highest-leverage open.
   - Run $(\beta, c, G, \pi)$ grid measurement to characterize.
5. **G-miss-2 c_0 scope correction**:
   - Reclassify Round 8 Cat A to "abelian/D_4 only"; non-abelian/generic as separate Cat B/C.

---

## §F. File status

- **Part A Axiom Audit**: 5 essential group (A-E) axiom sets audited + 4 proposed S1-S4 + 4 demotion candidates (C1-C4) + 5 new axiom candidates (NQ-A1..A5).
- **Part B Single-Formation Gap**: G-miss-1..4 deep-analyzed; 3 new gaps identified; priority matrix.
- **New NQ total**: 8 (A-tagged 5 + numbered 3).
- **Intended promotion**: `working/SF/axiom_audit.md` + `working/SF/layer_classification.md` §8 expansion.

**End of 04_axiom_audit_and_sf_gaps.md.**
