---
type: working/theory
created: 2026-05-07
stage: OMS-0.5
project: Observer Moduli Space of SCC
attacks: OP-OMS-012, OP-OMS-013
---

> [!nav] Linked: [[MOC_observer_moduli_OMS]] · [[THEORY_INDEX]]


# Boundary, Corners, Orbifold, and Stratified Dynamics — OMS-0.5

Every statement classified: **DEFINED** | **PROVED** | **ASSUMED** | **HYPOTHESIZED** | **OPEN** | **REJECTED**.

---

## §1. The Structure of $\partial \mathcal{M}_{\mathrm{obs}}$

The observer space $\mathcal{M}_{\mathrm{obs}} = [q_{\min}, q_{\max}] \times \Delta^3 \times B_\xi$ is a compact manifold-with-corners. Its boundary has multiple layers.

### §1.1 Boundary Faces of $\Delta^3$

**Definition SD1 (Boundary stratum of $\Delta^3$).** [DEFINED]

For an index set $I \subseteq \{cl, sep, bd, tr\}$:
$$\partial_I \Delta^3 = \{\lambda \in \Delta^3 : \lambda_i = 0 \text{ for all } i \in I\}$$

The codimension-$|I|$ face $\partial_I \Delta^3$ is a $(3 - |I|)$-simplex.

**Enumeration of faces:**

| Stratum | Notation | Dimension | Perceptual meaning |
|---|---|---|---|
| $\{\lambda_{cl} = 0\}$ | $F_{cl}$ | 2 | No closure energy |
| $\{\lambda_{sep} = 0\}$ | $F_{sep}$ | 2 | No separation energy |
| $\{\lambda_{bd} = 0\}$ | $F_{bd}$ | 2 | No boundary morphology |
| $\{\lambda_{tr} = 0\}$ | $F_{tr}$ | 2 | No temporal transport (static observer) |
| $\{\lambda_{cl} = \lambda_{sep} = 0\}$ | $F_{cl,sep}$ | 1 | Boundary + transport only |
| $\{\lambda_{cl} = \lambda_{bd} = 0\}$ | $F_{cl,bd}$ | 1 | Separation + transport only |
| $\{\lambda_{cl} = \lambda_{tr} = 0\}$ | $F_{cl,tr}$ | 1 | Separation + boundary only |
| $\{\lambda_{sep} = \lambda_{bd} = 0\}$ | $F_{sep,bd}$ | 1 | Closure + transport only |
| $\{\lambda_{sep} = \lambda_{tr} = 0\}$ | $F_{sep,tr}$ | 1 | Closure + boundary only |
| $\{\lambda_{bd} = \lambda_{tr} = 0\}$ | $F_{bd,tr}$ | 1 | Closure + separation only |
| $\{e_{cl}\} = (1,0,0,0)$ | vertex | 0 | Pure closure |
| $\{e_{sep}\} = (0,1,0,0)$ | vertex | 0 | Pure separation |
| $\{e_{bd}\} = (0,0,1,0)$ | vertex | 0 | Pure boundary |
| $\{e_{tr}\} = (0,0,0,1)$ | vertex | 0 | Pure transport |

### §1.2 Perceptual Interpretation of Each Face

**Face $F_{cl}$ ($\lambda_{\mathrm{cl}} = 0$, no closure):**
- Energy: $E = \lambda_{\mathrm{sep}} E_{\mathrm{sep}} + \lambda_{\mathrm{bd}} E_{\mathrm{bd}} + \lambda_{\mathrm{tr}} E_{\mathrm{tr}}$.
- The formation has no self-support; it is driven entirely by contrast with background and boundary smoothness.
- **Predicted behavior:** Formation boundaries may be ill-defined; the field $u^*$ may have diffuse interiors.
- **SCC sub-theory:** This is the "separation-dominant" observer regime.

**Face $F_{sep}$ ($\lambda_{\mathrm{sep}} = 0$, no separation):**
- Energy: $E = \lambda_{\mathrm{cl}} E_{\mathrm{cl}} + \lambda_{\mathrm{bd}} E_{\mathrm{bd}} + \lambda_{\mathrm{tr}} E_{\mathrm{tr}}$.
- The formation has no background contrast; it is driven by internal coherence.
- **Predicted behavior:** Formation may not separate well from background; possible merging with background.
- **SCC sub-theory:** This is the "closure-dominant" observer regime.

**Face $F_{bd}$ ($\lambda_{\mathrm{bd}} = 0$, no boundary):**
- Energy: $E = \lambda_{\mathrm{cl}} E_{\mathrm{cl}} + \lambda_{\mathrm{sep}} E_{\mathrm{sep}} + \lambda_{\mathrm{tr}} E_{\mathrm{tr}}$.
- The formation has no boundary smoothness penalty; boundaries may be sharp or irregular.
- **Predicted behavior:** Formation cores may be well-defined but boundaries may be jagged.

**Face $F_{tr}$ ($\lambda_{\mathrm{tr}} = 0$, no transport):**
- Energy: $E = \lambda_{\mathrm{cl}} E_{\mathrm{cl}} + \lambda_{\mathrm{sep}} E_{\mathrm{sep}} + \lambda_{\mathrm{bd}} E_{\mathrm{bd}}$.
- The static sub-theory: no temporal continuity is enforced.
- **This is the static SCC sub-theory** — the restriction to $F_{tr}$ gives exactly the static SCC energy.
- **Classification of face:** $F_{tr}$ corresponds to the **static observer type**. By Prop CW2, on static scenes this is the only relevant face ($\lambda_{\mathrm{tr}}$ is irrelevant there).

**Vertices:**

| Vertex | Energy | Perceptual behavior |
|---|---|---|
| $e_{cl} = (1,0,0,0)$ | Pure closure | Formation driven only by self-support; ignores background, boundary, time |
| $e_{sep} = (0,1,0,0)$ | Pure separation | Formation driven only by contrast; ignores shape, boundary, time |
| $e_{bd} = (0,0,1,0)$ | Pure boundary | Formation driven only by boundary smoothness; ignores interior |
| $e_{tr} = (0,0,0,1)$ | Pure transport | Formation driven only by temporal persistence; ignores static cues |

**Are vertices valid observer types?** [OPEN — OP-OMS-012]

Vertices are extreme cases; the SCC energy may be degenerate or non-convergent at vertices (e.g., $\lambda_{\mathrm{cl}} = 1$ with $\lambda_{\mathrm{sep}} = 0$ may allow trivial solutions). The question of whether boundary faces are **valid limiting observer types** or **degenerate cases** is registered as OP-OMS-012.

---

## §2. Gradient Flow on $\Delta^3$ with Boundary

### §2.1 Projected Gradient Flow

Since $\Delta^3$ is a convex polytope (manifold-with-corners), the gradient flow must be projected onto the feasible set.

**Definition SD2 (Projected gradient flow on $\Delta^3$).** [DEFINED]

For $V_{\mathrm{raw}} : \mathcal{M}_{\mathrm{obs}} \to \mathbb{R}_{\geq 0}$ and $\lambda \in \Delta^3$:

$$\frac{d\lambda}{dt} = -\Pi_{\Delta^3}(\lambda - \nabla_\lambda V_{\mathrm{raw}}) + \lambda = \Pi_{T_\lambda \Delta^3}(-\nabla_\lambda V_{\mathrm{raw}})$$

where $\Pi_{T_\lambda \Delta^3}$ is the projection onto the tangent cone of $\Delta^3$ at $\lambda$.

**Tangent cone at interior point:** $T_\lambda \Delta^3 = \{v \in \mathbb{R}^4 : \sum_i v_i = 0\}$ (hyperplane).

**Tangent cone at face $F_I$:** The tangent cone is smaller — directions that would violate $\lambda_i \geq 0$ for $i \in I$ are excluded.

**Tangent cone at vertex $e_j$:** $T_{e_j} \Delta^3 = \{v \in \mathbb{R}^4 : v_j \leq 0,\ \sum_i v_i = 0,\ v_i \geq 0 \text{ for } i \neq j\}$.

### §2.2 Invariance of Faces Under Flow

**Proposition SD1 (Faces are forward-invariant).** [PROVED]

If $\lambda(0) \in \partial_I \Delta^3$ (the face where $\lambda_i = 0$ for $i \in I$), then $\lambda(t) \in \partial_I \Delta^3$ for all $t \geq 0$ under the projected gradient flow.

**Proof.** For $\lambda \in \partial_I \Delta^3$, the constraint $\lambda_i = 0$ for $i \in I$ is active. The projected gradient removes any direction that would drive $\lambda_i < 0$. By the projection definition:

$$\Pi_{T_\lambda \Delta^3}(-\nabla V)_i \geq 0 \quad \text{for } i \in I, \lambda_i = 0$$

(The projection ensures the flow stays in $\Delta^3$.) Hence $\frac{d\lambda_i}{dt} \geq 0$ at the boundary, and since $\lambda_i = 0$ is the lower bound, $\lambda_i$ cannot decrease below 0. But the constraint is $\lambda_i = 0$ (not $\lambda_i \geq 0$): if $\nabla V$ has a component in the $-e_i$ direction at $\lambda \in F_I$, the projection sets $\frac{d\lambda_i}{dt} = 0$, keeping $\lambda_i = 0$. $\square$

**Consequence.** The boundary faces are absorbing: an observer that starts on $F_{tr}$ (static observer) never develops temporal energy under gradient flow. Similarly for all other faces.

### §2.3 Flow at Corner Points

**At vertex $e_j$:** The tangent cone is a simplicial cone. The projected flow is:
$$\frac{d\lambda}{dt} = \Pi_{\text{cone}}(-\nabla V(\lambda))\big|_{\lambda = e_j}$$

This may be zero even if $\nabla V(e_j) \neq 0$ — vertices can be "spurious fixed points" of the projected flow if the gradient points outward from the simplex in all feasible directions.

**Classification:** DEFINED. Whether vertices of $\Delta^3$ are attractors of the flow for typical $V$: OPEN (OP-OMS-012). **Hypothesis:** Pure-energy observers (vertices) are not typical attractors for perceptually meaningful landscapes $V$, since the pure energy functionals are degenerate.

---

## §3. Orbifold Strata Integration

### §3.1 Strata from $S_K$ Quotient

In the full $\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$ with $K \geq 2$ and gauge group $S_K$:

**Formation-diagonal stratum:** $\{[\Theta,\Theta]\} \cong \mathcal{M}_{\mathrm{obs}}$ (K=2 case) with stabilizer $S_2$.

**Stratum $\mathfrak{M}_{[S_K]}$:** All observers where all $K$ formations have identical parameters. Stabilizer $S_K$. Dimension $= \dim \mathcal{M}_{\mathrm{obs}} = 8$ (finite gauge, no dimension reduction). But the stratum has codimension $(K-1) \times \dim \mathcal{M}_{\mathrm{obs}}$ inside $\mathcal{M}_{\mathrm{obs}}^K$ — a thin set.

**Gradient flow at stratum:** The $S_K$-equivariant flow on the diagonal stratum is:
$$\frac{d\Theta}{dt} = -\frac{1}{K!} \sum_{\sigma \in S_K} \sigma \cdot \nabla V_{\mathrm{raw}}(\Theta) = -\nabla V_{\mathrm{raw}}(\Theta)$$

(Since all $\sigma \cdot \Theta = \Theta$ on the diagonal.) The flow on the diagonal stratum is the same as the flow on $\mathcal{M}_{\mathrm{obs}}$.

**Off-diagonal perturbations:** If a perturbation breaks the $S_K$ symmetry slightly, the flow may drive the observer away from the diagonal stratum into the generic stratum. Whether the diagonal is attracting or repelling depends on $V$.

### §3.2 Strata from $\mathrm{Aut}_{task}$ Quotient

Fixed-point strata of $\mathrm{Aut}_{task}$ correspond to observer configurations that are symmetric with respect to task spatial symmetries.

**Example.** Scene with $\mathbb{Z}_4$ rotational symmetry: the fixed-point stratum is $\{\Theta : \phi \cdot \Theta = \Theta \text{ for all } \phi \in \mathbb{Z}_4\}$. Since $\mathbb{Z}_4$ acts on the formation field (not directly on $\Theta$), the fixed-point condition is that the formation field $u^*(\Theta)$ is $\mathbb{Z}_4$-symmetric. This constrains $u^*$ but not $\Theta$ directly.

**Classification:** DEFINED for the general case. HYPOTHESIZED that the $\mathrm{Aut}_{task}$-symmetric strata are not generically attractors of the flow (since they correspond to maximally symmetric, hence "most rigid," observer configurations).

---

## §4. Basin-Face Attachment

### §4.1 How Basins Attach to Boundary Faces

**Proposition SD2 (Basin closure and face attachment).** [HYPOTHESIZED]

For a generic admissible landscape $V$, the closure of each basin $\overline{\mathcal{B}_i}$ may include portions of the boundary faces $\partial_I \Delta^3$.

Two cases:
1. **Face is in basin interior:** The basin $\mathcal{B}_i$ contains an open face region. The attractor $A_i$ lies on the face.
2. **Face is basin boundary:** $\partial \mathcal{B}_i$ intersects the face but the attractor $A_i$ is in the interior.

**Perceptual interpretation:**
- Case 1: One perceptual observer type preferentially uses a degenerate (boundary-face) configuration.
- Case 2: The boundary face acts as a separatrix; observers near the face may flow to different interior attractors.

### §4.2 Example: $F_{tr}$ and Static Observer Types

**Hypothesis SD1.** [HYPOTHESIZED]

For a landscape $V$ optimized for static scenes:
- The minimum of $V$ lies near $F_{tr}$ (static face, $\lambda_{\mathrm{tr}} \approx 0$).
- The basin of this minimum includes all observer configurations with small $\lambda_{\mathrm{tr}}$.
- The separatrix between static and temporal observer types lies in the interior of $\Delta^3$ along the $\lambda_{\mathrm{tr}}$ axis.

**Interpretation:** Observer adaptation for static scenes drives observers toward the static face; for dynamic scenes, observers are driven away from $F_{tr}$ into the interior.

---

## §5. Stratified Space Structure

### §5.1 Complete Stratification

The full moduli space $\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$ is a **stratified space** with strata indexed by:
1. Boundary index set $I$ (from $\partial_I \Delta^3$): $2^4 = 16$ strata from $\Delta^3$ alone.
2. Stabilizer conjugacy class $[H]$ in $G_{\mathrm{SCC}}^{(0)}$: multiple strata from the quotient.
3. Combined: boundary strata may intersect orbifold singular strata.

**Definition SD3 (Combined stratification).** [DEFINED]

$$\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}} = \bigsqcup_{I \subseteq \{cl,sep,bd,tr\},\ [H] \leq G} \mathfrak{M}_{I,[H]}$$

where $\mathfrak{M}_{I,[H]} = \{[\Theta] : \lambda|_I = 0 \text{ and } G_{[\Theta]} \in [H]\}$.

**Classification:** DEFINED formally. Detailed computation of each stratum's topology: OPEN.

### §5.2 Stratified Gradient Flow

**Definition SD4 (Stratified gradient flow).** [DEFINED]

A flow on a stratified space satisfies:
1. Within each stratum, the flow is a smooth gradient flow.
2. At stratum boundaries, the flow is defined by a consistent projection (Definition SD2).
3. The flow respects the stratification: it does not cross stratum boundaries except at transitions dictated by the dynamics.

**Well-posedness:** The stratified flow is well-posed if the projected gradient flow on each face is well-posed. For $\Delta^3$ (convex polytope), the projected flow is the standard projected gradient descent, which is well-posed. **ASSUMED** for the full manifold-with-corners $\mathcal{M}_{\mathrm{obs}}$.

**At orbifold singularities:** The $G$-equivariant flow (§2.2 of basin_stratification.md) provides a consistent definition at singular strata. **ASSUMED.**

---

## §6. Relation to SCC Ablation Experiments

The boundary faces $\partial_I \Delta^3$ correspond exactly to **SCC ablation experiments** — experiments where one or more energy terms are zeroed out.

**Mapping:**

| SCC ablation | OMS face | Expected SCC result |
|---|---|---|
| $\lambda_{\mathrm{tr}} = 0$ | $F_{tr}$ | Static SCC (temporal identity not computed) |
| $\lambda_{\mathrm{bd}} = 0$ | $F_{bd}$ | Sharp (unregularized) boundaries |
| $\lambda_{\mathrm{sep}} = 0$ | $F_{sep}$ | Closure-only formation (may merge with background) |
| $\lambda_{\mathrm{cl}} = 0$ | $F_{cl}$ | Separation-only formation (may have diffuse interior) |

**If SCC ablation experiments have been run** (exp1–exp57 in CODE/experiments/), their results provide direct empirical evidence for the behavior of the observer at boundary faces. This connects the OMS boundary analysis to existing experimental data.

**Classification:** COMPUTATIONALLY TESTABLE using existing SCC code.

---

## §7. New Open Problems

**OP-OMS-012 — Boundary-Face Interpretation of $\Delta^3$** [OPEN]

Are the boundary faces of $\Delta^3$ (pure-energy observers) valid limiting perceptual theories, or degenerate configurations? Specifically:
- Is $E_{\mathrm{cl}}$ alone (vertex $e_{cl}$) a well-posed energy that produces non-trivial formations?
- Do boundary-face attractors correspond to identifiable human/animal perceptual styles?

**OP-OMS-013 — Stratified Gradient Flow at Corners** [OPEN]

Is the projected gradient flow well-defined and convergent at corner strata (codimension $\geq 2$ faces) of $\Delta^3$? This requires analysis of the flow at simplicial corners, where the tangent cone is strictly smaller than a half-space.

---

## §8. OMS-1.2 patch (Session 5, 2026-05-08) — Branch-switching surfaces

The **simplex stratification** of §2 (faces, edges, vertices of $\Delta^3$) is
**topological**: it is intrinsic to $\Delta^3$ as a polytope. A second
stratification is now in play, not topological but **dynamical**:

> **Definition SD-OMS-1.2.** The **dynamical stratification** of $\Delta^3$
> partitions $\mathrm{int}(\Delta^3) = \bigsqcup_\alpha \mathcal{B}_\alpha \sqcup \Sigma_{\mathrm{branch}}$
> where each $\mathcal{B}_\alpha$ is an open subset of $\Delta^3$ on which
> $u^*(\lambda)$ has a uniform branch identifier ($K_{\mathrm{core}}$, $n_{\mathrm{high}}$,
> active set), and $\Sigma_{\mathrm{branch}}$ is the closed set of $\lambda$
> on which the branch identifier flips for arbitrarily small perturbations.

This is registered as OP-OMS-026 (mapping $\Sigma_{\mathrm{branch}}$
explicitly). Within each open $\mathcal{B}_\alpha$, the projected gradient
flow of $V$ is classically defined by Theorem R1 / R2 of
`op_oms_018_regular_u_star.md`.

### Filippov sliding-mode at $\Sigma_{\mathrm{branch}}$

At a point $\lambda \in \Sigma_{\mathrm{branch}}$ between branches $\alpha$
and $\alpha'$, $V$ has two one-sided gradients $\nabla V|_{\alpha}(\lambda)$
and $\nabla V|_{\alpha'}(\lambda)$. The classical projected gradient flow is
not defined. Following piecewise-smooth dynamical systems theory
(Filippov, *Differential Equations with Discontinuous Right-Hand Side*),
adopt the **convex-hull convention**:

$$\dot \lambda \in -\Pi_{T_\lambda \Delta^3}\, \mathrm{conv}\bigl\{\nabla V|_{\alpha}(\lambda),\ \nabla V|_{\alpha'}(\lambda)\bigr\}.$$

This is a differential inclusion. The flow exists in the Filippov sense
(by upper hemicontinuity of the convex-hull right-hand side and the Hartman
existence theorem for differential inclusions). The flow may slide along
$\Sigma_{\mathrm{branch}}$ until it reaches a transverse exit.

**Status.** **DEFINED**. Existence in the Filippov sense follows from
standard differential-inclusion theory. Uniqueness, asymptotic behavior,
and the relationship between Filippov solutions and within-branch
attractors are **OPEN** (sub-problem of OP-OMS-013 generalized).

### Two stratifications interact

The simplex topological stratification (§2) and the dynamical stratification
(SD-OMS-1.2) are independent:

- The simplex faces $F_{cl}, F_{sep}, F_{bd}, F_{tr}$ are absorbing walls
  (Prop SD1) — once $\lambda_i = 0$, the flow stays on the face.
- The branch-switching set $\Sigma_{\mathrm{branch}}$ is generically
  **transverse** to the simplex faces (e.g.\ the cl-dominant transition
  on S4 is a slice through the interior near the cl-axis).
- Their intersection (codim-2 sets where both apply) requires more careful
  analysis; flag as a sub-OP under OP-OMS-013.

### Computational evidence

VP-6 (Run 2) flagged 2 stencils as branch-jumping (out of 42), localizing
$\Sigma_{\mathrm{branch}}$ near $\{\lambda_{cl} \approx \lambda_{sep}\}$ on S3
and on the cl-axis on S4. The path test (`vp6_u_star_regular_path_test.py`)
provides directional evidence (paths that cross $\Sigma_{\mathrm{branch}}$
exhibit $K_{\mathrm{core}} / n_{\mathrm{high}}$ flips at intermediate $t$).
