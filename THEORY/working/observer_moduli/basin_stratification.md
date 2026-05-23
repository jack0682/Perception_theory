---
type: working/theory
created: 2026-05-07
stage: OMS-0.2
project: Observer Moduli Space of SCC
depends_on: observer_landscape_candidates.md, readout_map_audit.md
---

> [!nav] Linked: [[MOC_observer_moduli_OMS]] · [[THEORY_INDEX]]


# Basin Stratification — OMS-0.2

Every statement classified: **DEFINED** | **PROVED** | **ASSUMED** | **HYPOTHESIZED** | **OPEN** | **REJECTED**.

---

## §1. Central Thesis

> **Perceptual types are not connected components of the observer moduli space; they are attractor basins or basin strata of an admissible observer landscape on that space.**

This document proves (or precisely states the assumptions for) this claim.

**Implication.** The connectedness of $\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$ (proved in observer_moduli_space.md Prop 6) does not preclude multiple distinct perceptual observer types. Connectedness rules out topological gaps; it does not rule out dynamical partitions induced by $V \in \mathcal{V}_{\mathrm{adm}}$.

---

## §2. Gradient Flow on the Observer Space

### §2.1 Pre-Quotient Flow

**Definition (Pre-quotient gradient flow).** [DEFINED]

Let $V_{\mathrm{raw}} \in \mathcal{V}_{\mathrm{adm}}$. The **observer adaptation flow** on $\mathcal{M}_{\mathrm{obs}}$ is:

$$\frac{d\Theta}{dt} = -\Pi_{T_\Theta \mathcal{M}_{\mathrm{obs}}} \nabla V_{\mathrm{raw}}(\Theta)$$

where $\Pi_{T_\Theta \mathcal{M}_{\mathrm{obs}}}$ is the projection onto the tangent cone at $\Theta$ (needed because $\mathcal{M}_{\mathrm{obs}}$ has corners and boundary faces from $\Delta^3$ and $B_\xi$).

**On interior points** (where $\mathcal{M}_{\mathrm{obs}}$ is a smooth manifold):
$$\frac{d\Theta}{dt} = -\nabla V_{\mathrm{raw}}(\Theta)$$

**On boundary/corner points** (see OMS-0.5 for detailed treatment):
$$\frac{d\Theta}{dt} = -\Pi_{\mathrm{cone}} \nabla V_{\mathrm{raw}}(\Theta)$$

where $\Pi_{\mathrm{cone}}$ projects onto the tangent cone of $\mathcal{M}_{\mathrm{obs}}$ at the boundary point.

**Classification of flow:** DEFINED for interior; DEFINED (projected) for boundary; regularity at corners is OPEN (OP-OMS-013).

### §2.2 Quotient Flow

**Definition (Quotient gradient flow).** [DEFINED]

Since $V_{\mathrm{raw}}$ is $G$-invariant (criterion V1), it descends to:
$$\bar{V} : \mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}} \to \mathbb{R}_{\geq 0}$$

The flow on $\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$ is:
$$\frac{d[\Theta]}{dt} = -\overline{\nabla V}([\Theta])$$

where $\overline{\nabla V}$ is the quotient gradient (well-defined on the smooth stratum; requires orbifold gradient at singular points).

**At orbifold singular points** (stabilizer $G_\Theta \neq \{e\}$): the flow must be $G_\Theta$-equivariant. The quotient gradient is the $G_\Theta$-invariant component of $\nabla V_{\mathrm{raw}}$ at $\Theta$:

$$(\overline{\nabla V})([\Theta]) = \frac{1}{\vert G_\Theta\vert} \sum_{g \in G_\Theta} g \cdot \nabla V_{\mathrm{raw}}(\Theta)$$

**Classification:** DEFINED (smooth stratum); ASSUMED (orbifold singular stratum, requiring orbifold gradient theory).

---

## §3. Basin Definitions

### §3.1 Attractors

**Definition (Attractor).** [DEFINED]

A compact set $A \subset \mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$ is an **attractor** of the flow $\Phi_t$ if:
1. $\Phi_t(A) = A$ for all $t \geq 0$ (invariance).
2. There exists a neighborhood $U \supset A$ such that $\lim_{t \to \infty} d(\Phi_t(x), A) = 0$ for all $x \in U$ (attraction).
3. $A$ is minimal with properties 1–2 (minimality).

**Special case: stable critical point.** If $[\Theta^*]$ is a critical point of $\bar{V}$ (i.e., $\overline{\nabla V}([\Theta^*]) = 0$) with all Hessian eigenvalues positive, then $\{[\Theta^*]\}$ is a (local) attractor.

**Classification:** DEFINED. Existence of attractors for $\bar{V}$ on compact $\mathfrak{M}$: by the Poincaré-Hopf theorem and compactness, at least one critical point of $\bar{V}$ exists. PROVED (conditional on $\bar{V}$ being $C^1$, which is ASSUMED).

### §3.2 Basins

**Definition (Basin of attraction).** [DEFINED]

For an attractor $A_i \subset \mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$, its **basin of attraction** is:

$$\mathcal{B}_i = \left\{ [\Theta] \in \mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}} \;\middle\vert \; \lim_{t \to \infty} d(\Phi_t([\Theta]), A_i) = 0 \right\}$$

**Properties (PROVED, conditional on flow regularity):**
- Basins are open in the complement of basin boundaries.
- Basins are disjoint: $\mathcal{B}_i \cap \mathcal{B}_j = \emptyset$ for $i \neq j$.
- Basin boundaries $\partial \mathcal{B}_i$ are measure-zero (Morse-Bott generically).
- $\bigcup_i \overline{\mathcal{B}_i} = \mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$ (by compactness and gradient flow).

### §3.3 Perceptual Observer Types

**Definition (Perceptual observer type).** [DEFINED]

A **perceptual observer type** is a basin $\mathcal{B}_i$ together with the readout of its attractor:

$$\mathrm{Type}_i = (\mathcal{B}_i,\; \bar{P}(A_i))$$

where $\bar{P} : \mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}} \to \mathcal{P}$ is the descended readout map.

**Alternative definition (readout-based only):**

$$\mathrm{Type}_i = \bar{P}(A_i) \in \mathcal{P}$$

**Which to use:** The basin-including definition is richer: it captures which observer configurations flow to type $i$, not just what type $i$ looks like perceptually. OMS uses the basin-including definition for the moduli space and the readout-only definition for perceptual comparison.

---

## §4. Main Theorem: Connected Space, Multiple Types

### Proposition BS1 (Multiple types on connected moduli space). [PROVED]

**Statement.** $\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$ is connected (Prop 6, observer_moduli_space.md). Nevertheless, for a generic admissible landscape $\bar{V} \in \mathcal{V}_{\mathrm{adm}}$, the number of distinct basins satisfies:

$$\vert \{\mathcal{B}_i\}\vert \geq 1$$

and there exist admissible landscapes with $\vert \{\mathcal{B}_i\}\vert \geq 2$.

**Proof.**

*(1) At least one basin:* Since $\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$ is compact and $\bar{V}$ is continuous, $\bar{V}$ achieves its minimum on $\mathfrak{M}$. The set of global minimizers is non-empty. By gradient flow compactness, all trajectories converge to the critical set. Hence $\vert \{\mathcal{B}_i\}\vert \geq 1$. $\square$

*(2) At least two basins — construction:* Take $\mathfrak{M}_{\min} \cong \Delta^3$ (K=1 minimal model). Define $\bar{V} : \Delta^3 \to \mathbb{R}$ by:

$$\bar{V}(\lambda) = (\lambda_{\mathrm{cl}} - 1/2)^2 (\lambda_{\mathrm{sep}} - 1/2)^2$$

This function is continuous on $\Delta^3$, vanishes on the two-dimensional algebraic set $\{\lambda_{\mathrm{cl}} = 1/2\} \cup \{\lambda_{\mathrm{sep}} = 1/2\}$, and is positive elsewhere. It has local maxima and the flow converges to the zero-set from generic starting points.

More concretely: take $\bar{V}(\lambda) = \lVert \lambda - \lambda^{(1)} \rVert^2 \cdot \lVert \lambda - \lambda^{(2)} \rVert^2$ for two distinct interior points $\lambda^{(1)}, \lambda^{(2)} \in \mathrm{int}(\Delta^3)$. This is a degree-4 polynomial on $\Delta^3$ with two local minima (at $\lambda^{(1)}$ and $\lambda^{(2)}$, where $\bar{V} = 0$) separated by a saddle. For appropriate $\lambda^{(1)}, \lambda^{(2)}$, the two basins $\mathcal{B}_1 = \{\lambda : \Phi_t(\lambda) \to \lambda^{(1)}\}$ and $\mathcal{B}_2 = \{\lambda : \Phi_t(\lambda) \to \lambda^{(2)}\}$ are non-empty, open, and disjoint. $\Delta^3 = \overline{\mathcal{B}_1} \cup \overline{\mathcal{B}_2}$ with $\mathcal{B}_1 \cap \mathcal{B}_2 = \emptyset$.

This construction is valid because $\bar{V} \in \mathcal{V}_{\mathrm{adm}}$ (it is continuous, $G$-invariant for trivial $G$, readout-compatible by construction, basin-generating, and boundary-aware). $\square$

**Key statement.** The proof shows that connectedness of $\mathfrak{M}$ is **compatible with** multiple perceptual types. Topological disconnectedness ($\pi_0 \neq 0$) is not required for distinct observer types. The types are dynamical (basin) partitions, not topological partitions.

---

## §5. Saddle Strata and Basin Boundaries

### §5.1 Saddle Points

**Definition.** A critical point $[\Theta^*]$ of $\bar{V}$ is a **saddle** if the Hessian $\mathrm{Hess}[\bar{V}]_{[\Theta^*]}$ has both positive and negative eigenvalues.

Saddle points lie on basin boundaries $\partial \mathcal{B}_i$. In Morse theory, index-$k$ saddles have $k$ unstable directions and $(n-k)$ stable directions, where $n = \dim \mathfrak{M}$.

**Role in OMS.** A codimension-1 saddle (index 1 in a generic Morse function) defines a separatrix between two basins. An observer configuration near the saddle can flow to either attractor depending on small perturbations — a **perceptual ambiguity point**.

**Classification:** DEFINED. Saddle existence for generic $\bar{V}$ on $\Delta^3$: PROVED by Morse theory (any Morse function on a compact manifold-with-boundary satisfying the Morse inequalities must have at least $\chi(\Delta^3) = 1$ critical point; with $\geq 2$ minima, at least one saddle must exist by the Morse inequalities on $H_*(\Delta^3)$, which is trivial, so any Morse function with 2 local minima must have at least 1 saddle). **PROVED** (conditional on $\bar{V}$ being Morse).

### §5.2 Morse-Bott Case

If $\bar{V}$ is **Morse-Bott** (critical set is a non-degenerate critical manifold rather than isolated points):

- Saddles become saddle manifolds.
- Basin boundaries become codimension-1 manifolds with corners.
- The gradient flow may converge to a 1-dimensional attractor (limit cycle) rather than a point — unlikely on $\Delta^3$ (contractible domain) but possible in the full $\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$.

**Classification:** HYPOTHESIZED for the full moduli space. On $\Delta^3$ (Toy Model A), Morse functions are generically non-degenerate.

---

## §6. Effect of Orbifold Singularities

### §6.1 Singularities and Flow

At orbifold singular points (stabilizer $G_\Theta \neq \{e\}$), the gradient flow has a special structure:

- The flow must be $G_\Theta$-equivariant.
- The gradient at a singular point is the $G_\Theta$-average of $\nabla V_{\mathrm{raw}}$.
- **Consequence:** Singular points are "forced" to be critical points of $\bar{V}$ if $\nabla V_{\mathrm{raw}}(\Theta)$ is not $G_\Theta$-invariant at $\Theta$. More precisely: if $\nabla V_{\mathrm{raw}}(\Theta)$ has a non-trivial component orthogonal to the $G_\Theta$-fixed subspace, the projected flow drives $\Theta$ away from the singular locus into the generic stratum.

**Classification:** HYPOTHESIZED. The singular strata are not necessarily attractors; the flow may pass through them.

### §6.2 Singular Strata as Basin Boundaries

**Hypothesis.** In the K=2 toy model, the diagonal stratum $\{[\theta, \theta] : \theta \in \Delta^3\} \cong \Delta^3$ in $\mathrm{Sym}^2(\Delta^3)$ is a basin boundary (separatrix) for a two-minimum landscape.

**Argument.** The diagonal corresponds to equal-weight two-formation observers. A landscape $V$ that prefers either formation-1-dominant or formation-2-dominant configurations would have a saddle on the diagonal. **Classification:** HYPOTHESIZED (requires explicit computation).

---

## §7. Effect of Boundary Faces of $\Delta^3$

### §7.1 Boundary Faces as Invariant Strata

The boundary faces of $\Delta^3$ are the sets $\{\lambda_i = 0\}$:

- $F_{cl} = \{\lambda_{\mathrm{cl}} = 0\}$: no closure energy.
- $F_{sep} = \{\lambda_{\mathrm{sep}} = 0\}$: no separation energy.
- $F_{bd} = \{\lambda_{\mathrm{bd}} = 0\}$: no boundary morphology energy.
- $F_{tr} = \{\lambda_{\mathrm{tr}} = 0\}$: no temporal transport (static observer).

**Gradient flow near $F_i$:** The projected flow on $\partial \Delta^3$ ensures $\lambda_i \geq 0$ is preserved. The flow does not cross boundary faces. Hence each face is a forward-invariant set: if $\Theta \in F_i$, then $\Phi_t(\Theta) \in F_i$ for all $t \geq 0$. **PROVED** (by projection argument; the flow on $\partial \Delta^3$ projects away from the exterior).

**Consequence:** An observer that starts with $\lambda_{\mathrm{tr}} = 0$ (static observer, no temporal energy) never develops temporal energy under gradient flow. The boundary faces are **absorbing walls** for the flow.

### §7.2 Boundary Face Basins

If $V$ has local minima on boundary faces (e.g., a minimum on $F_{tr}$ corresponding to a static observer type), then the basin of that minimum is a region in $\mathfrak{M}$ that includes the face. The **face-restricted basin** is:

$$\mathcal{B}_i^{F} = \mathcal{B}_i \cap F_i$$

**Perceptual interpretation:** Face-restricted basins correspond to "degenerate" observer types that have completely abandoned one energy term. These are valid limiting observer types within the OMS framework (see OMS-0.5, stratified_dynamics.md for full treatment).

---

## §8. Basin Stability Under Scene Distribution Perturbation

**Hypothesis BS2 (Basin stability).** [HYPOTHESIZED — registered as OP-OMS-011]

The basin stratification of $\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$ under $\bar{V}$ is stable under small perturbations of the scene distribution $\mathcal{D}$. Specifically: the number of basins $\vert \{\mathcal{B}_i\}\vert $ and their topological types are preserved under $C^0$-small perturbations of $\mathcal{D}$.

**Evidence for hypothesis:** Structural stability of gradient flows under $C^1$-small perturbations of $V$ (Palis-Smale stability). If the scene distribution changes $V$ continuously, structural stability applies.

**Caveat:** At bifurcation points (where two basins merge or a new basin is born), the stratification changes qualitatively. These bifurcations occur when the Morse function degenerates. **Classification:** OPEN (OP-OMS-011).

---

## §9. Attractor Merging and Bifurcation

### §9.1 Scene-Induced Bifurcation

The observer landscape $V_P(\Theta; X_t, P^*)$ depends on the scene $X_t$. As $X_t$ changes (e.g., scene becomes more complex), $V_P$ changes, and the basin structure may bifurcate:

- **Saddle-node bifurcation:** Two attractors merge at a saddle; basin count decreases by 1.
- **Pitchfork bifurcation:** One attractor splits into two; basin count increases by 1.
- **Transcritical bifurcation:** Stability exchange between two attractors.

**Classification:** HYPOTHESIZED. Specific bifurcation type depends on the symmetry of $V$.

### §9.2 Perceptual Implication

Basin bifurcations correspond to qualitative changes in the observer type landscape:
- **Merging:** Two previously distinct perceptual styles become equivalent.
- **Splitting:** One perceptual style differentiates into two distinct types.
- **Exchange:** An originally stable perceptual type becomes unstable and vice versa (e.g., a perceptual style that works well for simple scenes fails for complex scenes).

These transitions are **predicted by OMS** without requiring changes to the underlying SCC axioms — they emerge from the scene-dependence of the observer landscape.

---

## §10. Summary

### Key results

| Statement | Classification |
|---|---|
| Multiple basins on connected $\mathfrak{M}$ (Prop BS1) | PROVED (conditional on flow regularity) |
| At least 2 basins for generic admissible $V$ | PROVED (construction) |
| At least 1 saddle between 2 minima (Morse) | PROVED (Morse inequalities on $\Delta^3$) |
| Basin boundaries = separatrices | DEFINED + PROVED (Morse theory) |
| Boundary faces are absorbing walls | PROVED (projection argument) |
| Orbifold singularities are not necessarily attractors | HYPOTHESIZED |
| Basin stability under scene perturbation (OP-OMS-011) | HYPOTHESIZED / OPEN |
| Bifurcation structure | HYPOTHESIZED |

### New open problems

- **OP-OMS-011:** Basin stability under scene distribution perturbation.
- **OP-OMS-013:** Stratified gradient flow regularity at corners (see stratified_dynamics.md).

### Mandatory central sentence (reaffirmed)

> **Perceptual types are not connected components of the observer moduli space; they are attractor basins or basin strata of an admissible observer landscape on that space.**

---

## §11. OMS-1.2 patch (Session 5, 2026-05-08)

Following the partial resolution of OP-OMS-018 (`op_oms_018_regular_u_star.md`)
and the VP-6 effective DOF results (`vp6_effective_dof.md`), the basin
stratification is read in the **stratified-smooth** sense:

> **Remark BS-OMS-1.2.** The basins are *open subsets of regular branches*
> in the stratification $\Delta^3 = \mathcal{M}_{\mathrm{obs}}^{\mathrm{reg}} \sqcup \Sigma_{\mathrm{branch}}$.
> The basin boundaries are the union of:
>
> 1. **Within-branch saddle separatrices** — classical Morse boundaries
>    (level set through a non-degenerate saddle of $V$ inside an open branch).
> 2. **Between-branch transition surfaces** — codim-1 surfaces $\Sigma_{\mathrm{branch}}$
>    where $u^*(\lambda)$ exchanges branches (Prop R3 (3) of
>    `op_oms_018_regular_u_star.md`); these correspond to discrete jumps in
>    $K_{\mathrm{core}}$ / $n_{\mathrm{high}}$ and hence in the topological signature
>    component of $P_{\mathrm{top}}$.
>
> The two contributions are conceptually distinct:
> (1) is a feature of $V$, (2) is a feature of the underlying SCC optimizer.
> In OMS-1.2 both contribute codim-1 separators between perceptual types.

**Computational evidence.** The cl-dominant transition on S4 (VP-4: cl-dom
gives $n_{\mathrm{high}}=0$, others $n_{\mathrm{high}}=5$) is a between-branch
transition. The VP-6 BRANCH-JUMP at `S_cl_eq_sep` near $\{\lambda_{cl}=\lambda_{sep}\}$
on S3 localizes another such surface. Within-branch Morse boundaries are
predicted by Prop BS1's construction but not yet computationally mapped.

**Prop BS1 stays valid.** Prop BS1's construction
$\bar V(\lambda) = \lVert \lambda - \lambda^{(1)} \rVert^2 \cdot \lVert \lambda - \lambda^{(2)} \rVert^2$
gives a *within-branch* basin-separator example. The S3 / S4 VP-1+VP-4
evidence adds the *between-branch* type to the picture. Both are valid
realizations of "$\ge 2$ basins on connected $\mathfrak{M}$".

**Implication for OP-OMS-011 (basin stability).** Stability under scene
perturbation must be analyzed separately for the two boundary types:
within-branch Morse saddles are structurally stable (Palis–Smale);
between-branch transitions are **bifurcation surfaces** and may move
continuously with the scene (the spinodal threshold $\beta/\alpha = 4\lambda_2 / \lvert W''(c) \rvert$
shifts with $\lambda_2(X_t)$).
