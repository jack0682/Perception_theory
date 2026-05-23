---
type: working/main-document
created: 2026-05-07
project: Observer Moduli Space of SCC
status: working (not yet canonical)
version: OMS-0.7
depends_on: definitions.md, toy_models.md, open_problems.md, audit_log.md, readout_map_audit.md, observer_landscape_candidates.md, basin_stratification.md, core_weight_symmetry.md, latent_symmetry.md, rg_relevance_flow.md, stratified_dynamics.md
---

> [!nav] Linked: [[MOC_observer_moduli_OMS]] · [[THEORY_INDEX]]


# SCC Observer Moduli Space

**Version OMS-0.7 — Working Document**

> This document lives in `THEORY/working/observer_moduli/`. It is NOT yet canonical. Promotion to `THEORY/canonical/` requires resolution of blockers OP-OMS-001, OP-OMS-002. ~~OP-OMS-009 RESOLVED 2026-05-07 (VP-1).~~ See `canonical_promotion_checklist.md` for the full promotion pathway.

---

## §1. Introduction and Motivation

The SCC theory (Soft Cognitive Cohesion) defines a formation field $u_t : X_t \to [0,1]$ on a relational support space, governed by an energy functional

$$E = \lambda_{\mathrm{cl}} E_{\mathrm{cl}} + \lambda_{\mathrm{sep}} E_{\mathrm{sep}} + \lambda_{\mathrm{bd}} E_{\mathrm{bd}} + \lambda_{\mathrm{tr}} E_{\mathrm{tr}}$$

The main SCC theory answers: *어떤 차이의 덩어리가 언제부터 하나의 객체가 되는가?* The answer depends on observer parameters: the energy weights $\lambda$, the boundary-separation ratio $q = \beta/\alpha$, and auxiliary hyperparameters $\xi$.

This raises a second-level question:

> **When two observers see the same scene, under what conditions do they share a perceptual core?**

Or equivalently: what is the space of distinct observer configurations, up to perceptual equivalence?

This document formalizes the **SCC Observer Moduli Space** as the answer to that question. It is a Level-2 SCC extension — it lifts the SCC field machinery one level to the space of observer configurations.

**Central object:**

$$\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}} = \mathcal{M}_{\mathrm{obs}} \,/\, G_{\mathrm{SCC}}^{(0)}$$

where $\mathcal{M}_{\mathrm{obs}}$ is the compact observer parameter space and $G_{\mathrm{SCC}}^{(0)}$ is the core-preserving gauge group.

---

## §2. Observer Parameter Space

### §2.1. The Observer Parameter Vector

An observer in the SCC framework is characterized by a triple:

$$\Theta_o = (q,\, \lambda,\, \xi) \in \mathcal{M}_{\mathrm{obs}}$$

**Components:**

| Symbol | Name | Domain | Control |
|---|---|---|---|
| $q = \beta/\alpha$ | Boundary-separation ratio | $[q_{\min}, q_{\max}] \subset \mathbb{R}_{>0}$ | Observer |
| $\lambda = (\lambda_{\mathrm{cl}}, \lambda_{\mathrm{sep}}, \lambda_{\mathrm{bd}}, \lambda_{\mathrm{tr}})$ | Energy weights | $\Delta^3 = \{\lambda \geq 0, \sum \lambda_i = 1\}$ | Observer |
| $\xi = (a_{\mathrm{cl}}, \varepsilon_{\mathrm{OT}}, \theta_{\mathrm{core}}, \theta_{\mathrm{in}})$ | Auxiliary hyperparameters | $B_\xi \subset \mathbb{R}^4$ (polytope) | Observer |

The following are NOT observer parameters: $m$ (scene mass), $\lambda_2$ (Fiedler eigenvalue), $c = m/n$ (mean field), $n$ (graph size), $b_D = 0$ (fixed by analyticity). These are scene-determined or theory-fixed.

### §2.2. The Observer Space

**Definition.** The **observer space** is:

$$\mathcal{M}_{\mathrm{obs}} = [q_{\min}, q_{\max}] \times \Delta^3 \times B_\xi$$

**Proposition 1 (Compactness).** $\mathcal{M}_{\mathrm{obs}}$ is compact.

*Proof.* Each factor is compact: $[q_{\min}, q_{\max}]$ by Heine-Borel; $\Delta^3$ as closed bounded subset of $\mathbb{R}^4$; $B_\xi$ as a closed bounded polytope. The finite product of compact spaces is compact (Tychonoff). $\square$

**Dimension.** $\dim \mathcal{M}_{\mathrm{obs}} = 1 + 3 + 4 = 8$ as a manifold-with-corners (before gauge identification). The dimension 3 for $\Delta^3$ reflects the normalization constraint $\sum \lambda_i = 1$.

### §2.3. The Critical Observer Space

**Criticality hypothesis.** If the observer operates at criticality — the phase transition threshold of T8 — then $q$ is scene-determined:

$$q_c(X_t) = \frac{4\lambda_2}{\lvert W''(c) \rvert} = \frac{4\lambda_2}{2(1 - 6c + 6c^2)}$$

where $\lambda_2$ is the Fiedler eigenvalue of $X_t$ and $c = m/n$ is in the spinodal zone.

**Definition.** The **critical observer space** is:

$$\mathcal{M}_{\mathrm{obs}}^{\mathrm{crit}} = \{\Theta \in \mathcal{M}_{\mathrm{obs}} : q = q_c(X_t)\}$$

**Proposition 2.** $\mathcal{M}_{\mathrm{obs}}^{\mathrm{crit}} \cong \Delta^3 \times B_\xi$.

*Proof.* Setting $q = q_c(X_t)$ fixes the first factor of $\mathcal{M}_{\mathrm{obs}}$ to a single point, leaving the product $\Delta^3 \times B_\xi$. $\square$

**Note.** The criticality hypothesis is a physical claim, not a mathematical axiom. Two versions exist: the unconstrained $\mathcal{M}_{\mathrm{obs}}$ and the constrained $\mathcal{M}_{\mathrm{obs}}^{\mathrm{crit}}$. See AUDIT-004.

### §2.4. Rejected Gauge Candidates

**U(1) action.** The proposal $(\alpha, \beta) \mapsto (e^{i\varphi}\alpha, e^{i\varphi}\beta)$ is **rejected**: $U(1)$ rotations exit the real positive domain $\mathbb{R}_{>0}^2$ for $\varphi \neq 0$. See AUDIT-001 for the complete rejection record.

**Correct scale symmetry.** The actual symmetry is $(\alpha, \beta) \mapsto (r\alpha, r\beta)$ for $r \in \mathbb{R}_{>0}$, a non-compact group. Compactification is achieved by fixing $\alpha + \beta = 1$, leaving $q = \beta/\alpha$ as the free parameter.

---

## §3. Gauge Group

### §3.1. Definition

**Definition.** The **SCC core-preserving gauge group** is:

$$G_{\mathrm{SCC}}^{(0)} = S_K \times \mathrm{Aut}_{\mathrm{task}}(X_t, \mathcal{N}_t, K, \mathcal{A})$$

with $G_{\mathrm{core\text{-}weight}} = \{e\}$ as the default assumption (see AUDIT-003).

**Components:**

**$S_K$ (formation label permutations).** The symmetric group on $K$ formation labels. Acts by permuting $(u^{(1)}, \ldots, u^{(K)}) \mapsto (u^{(\sigma(1))}, \ldots, u^{(\sigma(K))})$ for $\sigma \in S_K$. The labels $1, \ldots, K$ are physically arbitrary — two observers using different label assignments perceive the same formation set.

**$\mathrm{Aut}_{\mathrm{task}}$ (task-anchored graph automorphisms).** The subgroup of the graph automorphism group $\mathrm{Aut}(X_t)$ satisfying three task anchors:
1. Preserves the task-relevant neighborhood structure $\mathcal{N}_t$
2. Fixes the formation count $K$
3. Fixes the attention mask $\mathcal{A}$ setwise

**$G_{\mathrm{core\text{-}weight}} = \{e\}$ (default).** No assumed symmetry on energy weights $\lambda$. This is a conservative default pending resolution of OP-OMS-001.

### §3.2. The Gauge Action

$G_{\mathrm{SCC}}^{(0)}$ acts on the extended space $\mathcal{M}_{\mathrm{obs}} \times \mathcal{U}_K$ where $\mathcal{U}_K = ([0,1]^n)^K$ is the space of formation field configurations.

**Key subtlety.** The global parameters $(q, \lambda, \xi)$ are graph-global scalars. $S_K$ and $\mathrm{Aut}_{\mathrm{task}}$ do not act on them directly. They act on field configurations $(u^{(1)}, \ldots, u^{(K)})$.

The induced equivalence on $\mathcal{M}_{\mathrm{obs}}$ is:
$$\Theta \sim \Theta' \iff \exists g \in G_{\mathrm{SCC}}^{(0)}: P(g \cdot \Theta) = P(\Theta')$$

where $P$ is the readout map (§4).

### §3.3. Order and Structure

| Group | Order | Type |
|---|---|---|
| $S_K$ | $K!$ | Symmetric group; acts on $K$ labels |
| $\mathrm{Aut}_{\mathrm{task}}$ | Divides $|\mathrm{Aut}(X_t)|$ | Subgroup of graph automorphisms |
| $G_{\mathrm{SCC}}^{(0)}$ | $K! \cdot |\mathrm{Aut}_{\mathrm{task}}|$ | Direct product (both finite) |

Both components are finite groups, hence $G_{\mathrm{SCC}}^{(0)}$ is a finite group.

---

## §4. Moduli Space Definition

### §4.1. The Moduli Space

**Definition (Main).** The **SCC Observer Moduli Space** is the orbit space:

$$\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}} = \mathcal{M}_{\mathrm{obs}} \,/\, G_{\mathrm{SCC}}^{(0)}$$

with the quotient topology: $U \subset \mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$ is open iff $\pi^{-1}(U)$ is open in $\mathcal{M}_{\mathrm{obs}}$, where $\pi : \mathcal{M}_{\mathrm{obs}} \to \mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$ is the quotient map.

**Points.** A point in $\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$ is an orbit $[\Theta] = \{g \cdot \Theta : g \in G_{\mathrm{SCC}}^{(0)}\}$ — an equivalence class of observer configurations related by gauge transformations.

**Interpretation.** $[\Theta]$ is a **perceptual equivalence class**: all observer configurations that produce the same perceptual core.

### §4.2. The Critical Moduli Space

$$\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{crit}} = \mathcal{M}_{\mathrm{obs}}^{\mathrm{crit}} \,/\, G_{\mathrm{SCC}}^{(0)}$$

Under strict criticality, $q$ is eliminated, yielding a reduced moduli space of dimension 7 (at generic points).

---

## §5. Topology of the Moduli Space

### §5.1. Compactness

**Proposition 3 (Compactness of moduli space).** $\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$ is compact.

*Proof.* $\mathcal{M}_{\mathrm{obs}}$ is compact (Prop 1). The quotient map $\pi : \mathcal{M}_{\mathrm{obs}} \to \mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$ is continuous and surjective. The continuous image of a compact space is compact. $\square$

### §5.2. Hausdorff Property

**Proposition 4 (Hausdorff).** $\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$ is Hausdorff.

*Proof.* A finite group acting on a Hausdorff space $X$ gives a Hausdorff quotient $X/G$. (The orbit equivalence relation is closed: for finite $G$, the set $\{(x, gx) : g \in G\}$ is closed in $X \times X$ since each map $x \mapsto gx$ is continuous.) $\mathcal{M}_{\mathrm{obs}}$ is Hausdorff (metric space); hence the quotient is Hausdorff. $\square$

### §5.3. Dimension

**Proposition 5 (Dimension preservation).** At generic points (free orbits), $\dim \mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}} = \dim \mathcal{M}_{\mathrm{obs}} = 8$.

*Proof.* For a finite group $G$ acting on an $n$-manifold $M$, the quotient $M/G$ has dimension $n$ at points with trivial stabilizer. Only at fixed points (stabilizer $\neq \{e\}$) does the local structure differ — but the ambient dimension remains $n$. $\square$

**Corollary.** Finite gauge groups do NOT reduce the effective observer dimension. The reduction from 8 dimensions to an estimated 1–3 effective DOF must come from other sources (see §5.4).

### §5.4. Sources of Effective Dimension Reduction

The effective degrees of freedom are lower than 8 due to:

1. **Normalization constraint** ($\sum \lambda_i = 1$): already applied in DEF-4; reduces raw energy-weight DOF from 4 to 3. (The 8-dimensional $\mathcal{M}_{\mathrm{obs}}$ already accounts for this.)

2. **Criticality hypothesis** ($q = q_c(X_t)$): if applied, removes 1 more DOF. Reduces $\mathcal{M}_{\mathrm{obs}}$ from dimension 8 to $\mathcal{M}_{\mathrm{obs}}^{\mathrm{crit}}$ of dimension 7.

3. **Relevance flow** (RG analogy): in the energy landscape $V(\Theta)$, not all directions in $\mathcal{M}_{\mathrm{obs}}$ equally affect perceptual output. Directions along which $\partial P / \partial \Theta$ is small flow to fixed values — these are irrelevant directions. The number of relevant directions = effective DOF. Estimated at 1–3 (see OP-OMS-005).

### §5.5. Connectedness

**Proposition 6 (Connectedness).** $\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$ is connected.

*Proof.* $\mathcal{M}_{\mathrm{obs}}$ is connected (product of connected sets: $[q_{\min}, q_{\max}]$, $\Delta^3$, $B_\xi$ are all connected). The quotient of a connected space is connected (continuous image of connected set under $\pi$). $\square$

**Note.** This resolves OP-OMS-003 in the affirmative. There are no disconnected observer types: any observer can be continuously deformed into any other, within the moduli space.

---

## §6. Orbifold Structure

### §6.1. Stabilizer Stratification

**Definition.** For $\Theta \in \mathcal{M}_{\mathrm{obs}}$, the **stabilizer** is:

$$G_\Theta = \{g \in G_{\mathrm{SCC}}^{(0)} : g \cdot \Theta = \Theta\}$$

$G_\Theta$ is a subgroup of $G_{\mathrm{SCC}}^{(0)}$.

**Stratification.** The moduli space decomposes into strata by stabilizer conjugacy class:

$$\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}} = \bigsqcup_{[H] \in \mathrm{conj}(G)} \mathfrak{M}_{[H]}$$

where $\mathfrak{M}_{[H]} = \{[\Theta] : G_\Theta \in [H]\}$ and $[H]$ denotes the conjugacy class of $H \leq G_{\mathrm{SCC}}^{(0)}$.

**Principal stratum.** $\mathfrak{M}_{\{e\}} = \{[\Theta] : G_\Theta = \{e\}\}$ — the open dense stratum of generic observer states. Here the action is free and the quotient is locally a smooth manifold.

**Singular strata.** $\mathfrak{M}_{[H]}$ for $\lvert H \rvert > 1$ — the strata of highly symmetric observers. These correspond to observers for whom the gauge action has non-trivial fixed points (e.g., a two-formation observer with identical weights for both formations).

### §6.2. Orbifold Structure

**Proposition 7 (Orbifold).** $\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$ is a compact Hausdorff orbifold with:
- Underlying topological space: $\mathcal{M}_{\mathrm{obs}} / G_{\mathrm{SCC}}^{(0)}$ (compact, Hausdorff by Props 3, 4)
- Generic stratum: smooth manifold of dimension 8
- Singular strata: indexed by conjugacy classes $[H]$ with $\lvert H \rvert > 1$; local model near each point $[\Theta]$ is $\mathbb{R}^8 / G_\Theta$

*Proof sketch.* $G_{\mathrm{SCC}}^{(0)}$ is finite, acting properly (automatically, since $G$ is finite) on the manifold-with-corners $\mathcal{M}_{\mathrm{obs}}$. The orbit space of a proper finite group action on a manifold is an orbifold. $\square$

### §6.3. Examples of Stabilizer Groups

| Observer configuration | $G_\Theta$ | Perceptual meaning |
|---|---|---|
| $K=1$, generic | $\{e\}$ | Generic single-formation observer |
| $K=2$, $\lambda^{(1)} = \lambda^{(2)}$ | $S_2$ | Symmetric two-formation observer |
| $K=3$, all $\lambda^{(k)}$ equal | $S_3$ | Fully symmetric three-formation observer |
| $K=2$, scene with $\mathbb{Z}_2$ spatial symmetry | $\mathbb{Z}_2 \leq \mathrm{Aut}_{\mathrm{task}}$ | Spatially symmetric observer |

Larger stabilizers correspond to more symmetric (less differentiated) observer states.

---

## §7. Readout Map and Perceptual Core

### §7.1. Readout Levels

**Definition.** The **readout map** $P : \mathcal{M}_{\mathrm{obs}} \to \mathcal{P}$ extracts perceptually relevant information. Three levels:

**$P_{\min}$ (diagnostic readout).** Maps $\Theta$ to the diagnostic vector:

$$P_{\min}(\Theta) = d(\Theta, X_t) = (\mathrm{Bind}, \mathrm{Sep}, \mathrm{Inside}, \mathrm{Persist}) \in [0,1]^4$$

**$P_{\mathrm{top}}$ (topological readout, recommended).** Maps $\Theta$ to:

$$P_{\mathrm{top}}(\Theta) = (d(\Theta, X_t),\, \mathrm{barcode}(\Theta, X_t),\, N_{\mathrm{comp}}(\Theta, X_t)) \in [0,1]^4 \times \mathcal{B} \times \mathbb{Z}_{\geq 0}$$

where $\mathcal{B}$ is the space of persistence barcodes. Recommended because topology-including readout better captures perceptual equivalence (two observers can have similar diagnostics but different component counts).

**$P_{\mathrm{full}}$ (basin readout).** Maps $\Theta$ to the full attractor structure of the SCC energy landscape. Requires $V(\Theta)$ to be defined (see OP-OMS-002). Not yet available.

### §7.2. Gauge-Invariance of Readout

**Proposition 8.** $P_{\mathrm{top}}$ is $G_{\mathrm{SCC}}^{(0)}$-invariant: $P_{\mathrm{top}}(g \cdot \Theta) = P_{\mathrm{top}}(\Theta)$ for all $g \in G_{\mathrm{SCC}}^{(0)}$.

*Proof sketch.*
- $S_K$-invariance: permuting formation labels does not change the formation set, hence leaves barcode, component count, and diagnostics unchanged.
- $\mathrm{Aut}_{\mathrm{task}}$-invariance: spatial automorphisms preserve the graph Laplacian, the energy functional, and all derived quantities. $\square$

**Corollary (Descent).** $P_{\mathrm{top}}$ descends to a well-defined map:

$$\bar{P} : \mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}} \to \mathcal{P}, \quad \bar{P}([\Theta]) = P_{\mathrm{top}}(\Theta)$$

### §7.3. Perceptual Core

**Definition.** The **perceptual core** of an observer configuration $\Theta$ is its equivalence class:

$$[\Theta]_G = \{g \cdot \Theta : g \in G_{\mathrm{SCC}}^{(0)}\} \in \mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$$

Two observer configurations $\Theta, \Theta' \in \mathcal{M}_{\mathrm{obs}}$ share a perceptual core iff they lie in the same orbit: $[\Theta]_G = [\Theta']_G$.

**Fundamental domain.** A fundamental domain $F \subset \mathcal{M}_{\mathrm{obs}}$ is a connected set containing exactly one representative from each orbit in the open dense stratum (one representative from each equivalence class for generic $\Theta$). The moduli space $\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$ is homeomorphic to $F$ modulo identifications on $\partial F$ arising from non-trivial stabilizers.

---

## §8. The Potential $V(\Theta)$

### §8.1. Requirements

A function $V : \mathcal{M}_{\mathrm{obs}} \to \mathbb{R}_{\geq 0}$ is a **valid perceptual potential** if it satisfies:

- **V1 (Gauge-invariant):** $V(g \cdot \Theta) = V(\Theta)$ for all $g \in G_{\mathrm{SCC}}^{(0)}$
- **V2 (Continuous):** $V \in C^0(\mathcal{M}_{\mathrm{obs}})$
- **V3 (Readout-compatible):** $\nabla V(\Theta) = 0$ iff $P(\Theta)$ is locally stable under perturbations of $\Theta$
- **V4 (Basin-generating):** The level sets of $V$ define a basin decomposition of $\mathcal{M}_{\mathrm{obs}}$
- **V5 (Boundary-aware):** $V(\partial \mathcal{M}_{\mathrm{obs}}) \not\equiv \mathrm{const}$

### §8.2. Status

$V(\Theta)$ is not yet explicitly defined. See OP-OMS-002 for candidate forms and resolution criteria.

The existence of $V$ is anticipated from the physics (observer configurations that produce different perceptual outcomes should be distinguished by an energy barrier in parameter space), but its explicit form requires computation of the readout landscape $P(\Theta)$ over $\mathcal{M}_{\mathrm{obs}}$.

---

## §9. Toy Models

The following are fully computed; see `toy_models.md` for proofs.

### §9.1. Model A: Minimal Case

**Assumptions:** $K = 1$, $G = \{e\}$, $\xi$ fixed, strict criticality.

**Result:** $\mathfrak{M}_{\min} \cong \Delta^3$.

**Topology:** compact, convex, contractible; $\pi_k = 0$ for all $k$; $\chi = 1$; homeomorphic to $B^3$.

**Key implication:** no topological barriers in the minimal model. Perceptual discontinuity must arise from $V(\Theta)$ basin structure, not from moduli space topology.

### §9.2. Model B: Two-Formation Case

**Assumptions:** $K = 2$, $G = S_2$, $\xi$ fixed, strict criticality.

**Result:** $\mathfrak{M}_2 \cong \mathrm{Sym}^2(\Delta^3) = (\Delta^3 \times \Delta^3) / S_2$.

**Topology:** dimension 6 at generic points; orbifold singularity along the diagonal $\Delta_{\Delta^3} \cong \Delta^3$ (dimension 3, stabilizer $S_2$); compact; connected.

**Perceptual meaning of diagonal:** the singular stratum $\{[\theta,\theta]\}$ corresponds to two-formation observers where both formations are governed by identical energy weights — a "symmetric" or "undifferentiated" observer state.

---

## §10. Open Problems

See `open_problems.md` for full statements. Summary:

| ID | Title | Priority | Promotion Blocker? |
|---|---|---|---|
| OP-OMS-001 | Core-Weight Gauge Group | ★★★ | **YES** |
| OP-OMS-002 | Admissible $V$ Existence | ★★★ | **YES** |
| OP-OMS-003 | Connectedness | ★★ | No (RESOLVED: Prop 6) |
| OP-OMS-004 | Contractibility of $\mathrm{Sym}^K(\Delta^3)$ | ★★ | No |
| OP-OMS-005 | Effective DOF / Continuous Gauge | ★★★ | No |
| OP-OMS-006 | Topology for Non-Trivial $\mathrm{Aut}_{task}$ | ★★ | No |
| OP-OMS-007 | Observer Dynamics (Level-3) | ★★ | No (deferred) |
| OP-OMS-008 | Relation to RelationWorld | ★ | No |
| OP-OMS-009 | Readout Resolution + Continuity | ★★★ | **YES** |
| OP-OMS-010 | $V$ Regularity | ★★ | No (subsumed by 002) |
| OP-OMS-011 | Basin Stability | ★★ | No |
| OP-OMS-012 | Boundary Face Interpretation | ★★ | No |
| OP-OMS-013 | Stratified Flow at Corners | ★ | No |
| OP-OMS-014 | Empirical Identifiability | ★★ | No |
| OP-OMS-015 | OMS ↔ Perceptual Styles | ★★ | No |
| OP-OMS-016 | Computational $d_{\mathrm{eff}}$ | ★★ | No |

---

## §11. Relation to Main SCC Theory

### §11.1. Dependence Structure

The Observer Moduli Space is a **Level-2 SCC extension** — it uses the SCC field theory as its foundation without modifying it.

Dependencies:
- T8 (phase transition): provides the criticality condition $q_c(X_t)$, used in $\mathcal{M}_{\mathrm{obs}}^{\mathrm{crit}}$
- Multi-formation framework (K-field): provides the formation count $K$ and label permutation symmetry $S_K$
- Readout framework (DiagnosticVector, persistence): provides the readout map $P$

This document does NOT modify or constrain any theorem in `canonical.md`.

### §11.2. Observer Dependence in SCC

SCC already recognizes observer-dependence (DECLARATION.md §관측 조건 의존성):

> 객체의 수, 경계, 동일성은 관측 조건의 함수다 — 절대량이 아니다.

The Observer Moduli Space makes this dependence mathematically precise: it provides the space of all distinct observer types, equipped with a topology (from $\mathcal{M}_{\mathrm{obs}}$) and an equivalence relation (from $G_{\mathrm{SCC}}^{(0)}$).

### §11.3. Connection to Open Problems in SCC

- **OP-0005** (K-selection): the K-selection problem determines $K$ as a function of the scene. For the moduli space, $K$ is a parameter — different values of $K$ give different moduli spaces $\mathfrak{M}_{\mathrm{SCC}}^{(K)}$. The moduli space over all $K$ would be $\bigsqcup_{K \geq 1} \mathfrak{M}_{\mathrm{SCC}}^{(K)}$.
- **OP-0008** (temporal identity): the transport energy $E_{\mathrm{tr}}$ enters the moduli space via $\lambda_{\mathrm{tr}} \in \Delta^3$. Different observers weight temporal identity differently.
- **OP-0009** (σ-inheritance): inheritance maps may carry symmetries that contribute to $\mathrm{Aut}_{\mathrm{task}}$.

---

## §12. Relation to RelationWorld Theory

See OP-OMS-008 for the open problem. Brief note:

RelationWorld Theory develops discrete gauge structure on finite graphs, including analogues of Yang–Mills gauge groups. The SCC gauge group $G_{\mathrm{SCC}}^{(0)}$ also acts on finite graph structures ($X_t$). The subgroup $\mathrm{Aut}_{\mathrm{task}} \leq \mathrm{Aut}(X_t)$ is a task-anchored restriction of the full graph automorphism group.

A potential unified framework: both theories are special cases of gauge theory on finite graphs, with different fields (RelationWorld: combinatorial gauge fields; SCC: cohesion fields $u_t$) and different gauge groups (RelationWorld: general discrete gauge groups; SCC: $S_K \times \mathrm{Aut}_{\mathrm{task}}$).

---

## §13. Status and Promotion Criteria

### §13.1. Current Status

**Version OMS-0.7** (2026-05-07)

| Component | Status |
|---|---|
| $\mathcal{M}_{\mathrm{obs}}$ defined | Complete (definitions.md DEF-4) |
| $\mathcal{M}_{\mathrm{obs}}^{\mathrm{crit}}$ defined | Complete (definitions.md DEF-5) |
| $G_{\mathrm{SCC}}^{(0)}$ defined | Complete (definitions.md DEF-8) |
| $\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$ defined | Complete (§4 this document) |
| Compactness proved | Complete (Prop 3) |
| Hausdorff proved | Complete (Prop 4) |
| Connectedness proved | Complete (Prop 6) |
| Orbifold structure stated | Complete (§6) |
| Gauge-invariance of $P$ verified | Complete (Prop 8, conditional) |
| $K=1$ toy model | Complete (toy_models.md Prop A1–A6) |
| $K=2$ toy model | Complete (toy_models.md Prop B1–B3) |
| Readout hierarchy $P_{\min} / P_{\mathrm{top}} / P_{\mathrm{full}}$ | Complete (readout_map_audit.md) |
| Admissible landscape class $\mathcal{V}_{\mathrm{adm}}$ | Complete (observer_landscape_candidates.md) |
| Basin stratification framework | Complete (basin_stratification.md) |
| $S_4$ weight symmetry rejected | Complete (core_weight_symmetry.md CW1) |
| Transport invariance on static scenes | Complete (core_weight_symmetry.md CW2, conditional) |
| No continuous vertex-preserving symmetry | Complete (latent_symmetry.md LS1) |
| RG relevance flow framework | Complete (rg_relevance_flow.md, program status) |
| Boundary faces as absorbing walls | Complete (stratified_dynamics.md Prop SD1) |
| Full $\Delta^3$ stratification (16 strata) | Complete (stratified_dynamics.md §2) |
| Integration with SCC layers | Complete (integration_with_scc.md) |
| Validation protocols VP-1 through VP-6 | VP-1 COMPLETE (exp86, 2026-05-07); VP-2–VP-6 not yet run |
| $\mathcal{V}_{\mathrm{adm}}$ existence proved | **OPEN BLOCKER (OP-OMS-002)** |
| $G_{\mathrm{core\text{-}weight}}$ determined | **OPEN BLOCKER (OP-OMS-001)** |
| $u^*(\Theta)$ continuity proved | OPEN (OP-OMS-009 residual — not a canonical blocker) |
| Effective DOF quantified | OPEN (OP-OMS-005, VP-6 needed) |

### §13.2. Promotion Criteria

For promotion to `THEORY/canonical/canonical.md`, the three blockers must be resolved:

1. **OP-OMS-001** (core-weight gauge): either prove $G_{\mathrm{core\text{-}weight}} = \{e\}$ or identify the correct non-trivial group. VP-3 can partially constrain.
2. **OP-OMS-002** (admissible $V$): prove existence of $V \in \mathcal{V}_{\mathrm{adm}}$ satisfying V1–V5. VP-2 can demonstrate a concrete instance.
3. **OP-OMS-009** (readout resolution + continuity): prove $u^*(\Theta)$ continuous in $\Theta$ (or prove $P_{\mathrm{top}}$ directly). VP-1 provides computational evidence for Prop R1.

See `canonical_promotion_checklist.md` for the complete criterion-by-criterion checklist (Criteria A–E).

### §13.3. What Must NOT Change

The following are permanent decisions regardless of promotion:
- $\mathcal{M}_{\mathrm{obs}}$ is compact (Tychonoff)
- Finite gauge groups do not reduce dimension
- U(1) on $(\alpha, \beta)$ is rejected
- $\mathcal{M}_{\mathrm{obs}}$ is connected
- The minimal model is $\Delta^3$

---

## §14. Summary

The SCC Observer Moduli Space $\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}} = \mathcal{M}_{\mathrm{obs}} / G_{\mathrm{SCC}}^{(0)}$ is:

1. A **compact Hausdorff orbifold** of dimension 8 (generic stratum)
2. **Connected** — no disconnected observer types exist
3. **Finite-group quotient** — gauge identifications introduce orbifold singularities but preserve dimension
4. **Stratified** — by stabilizer conjugacy class; singular strata correspond to highly-symmetric observers
5. **Contractible in the minimal case** ($\Delta^3$ for $K=1$, $\xi$ fixed, strict criticality)
6. A **topologically non-trivial orbifold** for $K \geq 2$ (orbifold singularity at $\mathrm{Sym}^K(\Delta^3)$ diagonals)

The central result (Prop 6) is that **no topological barrier** separates observer types — perceptual discontinuity must arise from the basin structure of a potential $V(\Theta)$, not from the topology of $\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$.

The principal open problem (OP-OMS-002) is the explicit construction of $V(\Theta)$.

---

---

## §15. Readout Map Audit (OMS-0.2)

### §15.1. The Three-Level Hierarchy

The readout map admits three informationally distinct levels (see `readout_map_audit.md` for full proofs):

**Level 1 — $P_{\min}$:** Diagnostic vector only. $P_{\min}(\Theta) = d_\Theta \in [0,1]^4$.
- Too coarse: two observers with equal $d_\Theta$ can differ in topological signature (Prop R1 — **PROVED**, VP-1, exp86, 2026-05-07; 4 explicit counterexamples).
- Used in: SCC static theory, ablation experiments exp1–exp57.

**Level 2 — $P_{\mathrm{top}}$:** Adds topological formation signature $T_\Theta = (N_0, \mathrm{Bar}_0, \ell_1, \ell_2, A, K^*, C_{bd})$.
$$P_{\mathrm{top}}(\Theta) = (d_\Theta,\ T_\Theta)$$
- Recommended readout: discriminates topologically distinct formations.
- Descends to quotient (Prop R3 — PROVED conditional on $u^*$ continuity, OP-OMS-009).

**Level 3 — $P_{\mathrm{full}}$:** Adds basin signature $\mathcal{B}_\Theta$. Requires $V \in \mathcal{V}_{\mathrm{adm}}$ (OP-OMS-002, open blocker). Deferred.

**Warning R1.** Using $P_{\min}$ as the sole readout conflates topologically distinct observer configurations. For OMS purposes, always use $P_{\mathrm{top}}$ or acknowledge the coarseness explicitly.

### §15.2. Descent to Quotient

**Proposition R3** [PROVED, conditional on $u^*$ continuity]: $P_{\mathrm{top}}$ is gauge-invariant and descends to $\bar{P}_{\mathrm{top}} : \mathfrak{M} \to \mathcal{P}_{\mathrm{top}}$.

*Condition.* The descent requires $u^*(\Theta, X_t)$ to be continuous in $\Theta$ (or at least measurable). Continuity of $u^*$ is an open sub-question of OP-OMS-009; the resolution sub-question (P_min coarseness) was RESOLVED-NEGATIVE by VP-1 (2026-05-07), but continuity itself remains unproved.

---

## §16. Basin Stratification (OMS-0.2)

### §16.1. Gradient Flow on $\mathcal{M}_{\mathrm{obs}}$

For $V \in \mathcal{V}_{\mathrm{adm}}$, the observer gradient flow is:
$$\dot{\Theta}(t) = -\Pi_{T_\Theta \mathcal{M}_{\mathrm{obs}}} \nabla V(\Theta(t))$$

where $\Pi$ projects onto the tangent space (required because $\mathcal{M}_{\mathrm{obs}}$ has boundary faces). The projection is the projected gradient descent standard in constrained optimization.

### §16.2. Multiple Basins on Connected Space

**Proposition BS1** [PROVED]: For any $V \in \mathcal{V}_{\mathrm{adm}}$ with more than one local minimum on $\Delta^3$, the moduli space $\mathfrak{M}$ supports multiple distinct attractor basins even though $\mathfrak{M}$ is connected.

*Proof.* Explicit 2-minimum construction: $V(\lambda) = \lambda_{cl}^2(1 - \lambda_{cl})^2$ on $\Delta^3$. This has local minima at $\lambda_{cl} = 0$ and $\lambda_{cl} = 1$ (both in $\partial \Delta^3$), separated by a saddle at $\lambda_{cl} = 1/2$. $\mathfrak{M}$ remains connected (Prop 6), but two distinct basins exist. $\square$

**Central distinction (mandatory):** Perceptual types are NOT connected components of $\mathfrak{M}$. They are attractor basins of $V$. Connectedness of $\mathfrak{M}$ and multiplicity of perceptual types are compatible.

### §16.3. Basin Count Dependence on $V$

**Warning:** The number of perceptual types (basins) depends on $V \in \mathcal{V}_{\mathrm{adm}}$. OMS-1.0 does not assert a universal basin count. Any claim "there are exactly $N$ observer types" requires specifying $V$.

VP-2 (basin discovery protocol) can empirically estimate the basin count for the specific landscape $V_D^0(\lambda) = \lVert d_\lambda - d^* \rVert^2$.

---

## §17. Stratified Dynamics and RG Relevance (OMS-0.5 / OMS-0.4)

### §17.1. Stratification of $\Delta^3$

The simplex $\Delta^3$ has $2^4 = 16$ faces indexed by which weights are zero:

$$\Delta^3 = \bigsqcup_{I \subseteq \{cl,sep,bd,tr\}} \mathrm{int}(\partial_I \Delta^3)$$

**Boundary face dimensions:**

| $\lvert I \rvert$ | Count | Dimension | Observer type |
|---|---|---|---|
| 0 | 1 | 3 | Generic interior (all weights active) |
| 1 | 4 | 2 | One-weight-ablated face |
| 2 | 6 | 1 | Two-weight-ablated edge |
| 3 | 4 | 0 | Vertex (single dominant weight) |

**Four canonical vertices:**
- $e_{cl} = (1,0,0,0)$: pure closure — maximal compactness drive
- $e_{sep} = (0,1,0,0)$: pure separation — maximal contrast drive
- $e_{bd} = (0,0,1,0)$: pure boundary — morphological observer
- $e_{tr} = (0,0,0,1)$: pure transport — temporal continuity observer

### §17.2. Absorbing Wall Property

**Proposition SD1** [PROVED, conditional on $V \in C^1$]: Each face $\partial_I \Delta^3$ is forward-invariant under projected gradient flow. Once $\lambda_i = 0$ for $i \in I$, the flow cannot increase $\lambda_i$.

*Proof.* The projection $\Pi_{T_\lambda \Delta^3}$ satisfies $(\Pi \nabla V)_i \leq 0$ when $\lambda_i = 0$ and the interior normal is outward-pointing. Hence $\dot{\lambda}_i \geq 0$ is not possible for $\lambda_i = 0$, maintaining the face. $\square$

*Corollary.* An observer who has "turned off" an energy term cannot spontaneously reactivate it under gradient flow alone. Reactivation requires external perturbation.

### §17.3. RG Relevance: Effective Dimension

The **perceptual Jacobian** $J_P(\Theta) = D_\Theta P_{\mathrm{top}}$ encodes which observer directions produce detectable readout changes.

**Effective dimension:** $d_{\mathrm{eff}}(\Theta; \varepsilon) = \#\{\sigma_i(J_P(\Theta)) \geq \varepsilon\}$.

**Hypothesis RG1** [HYPOTHESIZED]: $d_{\mathrm{eff}}^{\mathrm{typical}}(0.05) \in [2,4]$.

**Warning RG1.** This is a research program, not a theorem. VP-6 (RG Jacobian protocol) must be run to test Hypothesis RG1.

**Mandatory distinction (three separate mechanisms):**
1. Normalization constraints reduce raw DOF (already in $\dim \mathcal{M}_{\mathrm{obs}} = 8$)
2. Finite gauge quotient identifies orbits (does NOT reduce dimension, AUDIT-002)
3. RG relevance flow: irrelevant directions become perceptually flat (HYPOTHESIZED)

These three are conceptually distinct and must never be conflated.

---

*OMS-0.7, 2026-05-07. Working document — superseded by `THEORY/canonical/canonical.md` Appendix OMS as of Session 7 (2026-05-08). Static OMS-2.0 Accepted. Full Temporal Conditional on OP-OMS-034.*

---

## §18. OMS-2.0 Promotion Trajectory (Session 4 → Session 7, 2026-05-08)

| Session | Classification | Key advance |
|---|---|---|
| Session 4 (morning) | OMS-1.1 — Computationally Grounded Canonical Candidate | VP-3/VP-2/VP-4 complete |
| Session 5 | OMS-1.2 — w/ Local Regularity Theorem | OP-OMS-018 partially resolved (R1–R5 PROVED) |
| Session 5 cont. | OMS-1.2+ | OP-OMS-028 PROVED (Lipschitz); OP-OMS-029 PROVED (continuous-component triviality) |
| Session 6 | OMS-2.0 Conditional Accepted | All three hard blockers resolved at theorem + witness level |
| **Session 7** | **OMS-2.0 Accepted — Static, Full Temporal Conditional on OP-OMS-034** | **Gap C1 theorem package consolidated; sub-OPs 032/033/034 resolved/separated; Appendix OMS added to canonical.md** |

**Authoritative status at end of Session 7:** see `THEORY/canonical/canonical.md` **Appendix OMS** and `oms_2_0_accepted_audit.md`.
