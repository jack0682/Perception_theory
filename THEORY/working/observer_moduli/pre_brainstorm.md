---
type: working/brainstorm
created: 2026-05-07
project: Observer Moduli Space of SCC
---

# Pre-Brainstorm — Observer Moduli Space

## Central Question

The main SCC theory answers: "어떤 차이의 덩어리가 언제부터 하나의 객체가 되는가?"

This extension asks a second question:
> **When two observers see the same scene, under what conditions do they share a perceptual core?**

Or equivalently: what is the space of distinct observer configurations, up to perceptual equivalence?

---

## Mathematical Setting

### What varies between observers?

SCC energy:
$$E = \lambda_{cl} E_{cl} + \lambda_{sep} E_{sep} + \lambda_{bd} E_{bd} + \lambda_{tr} E_{tr}$$

Phase transition:
$$\frac{\beta}{\alpha} > \frac{4\lambda_2}{|W''(c)|}$$

Between two observers, the following can differ:
- The ratio $q = \beta/\alpha$ (boundary vs separation balance)
- The energy weights $\lambda = (\lambda_{cl}, \lambda_{sep}, \lambda_{bd}, \lambda_{tr})$
- The auxiliary hyperparameters $\xi = (a_{cl}, \varepsilon_{OT}, \theta_{core}, \theta_{in}, \ldots)$

The following is SCENE-determined (not observer-determined):
- $\lambda_2$ (Fiedler eigenvalue of graph $X_t$)
- $m$ (mass constraint, related to scene content)
- $c = m/n$ (mean field value, determines spinodal position)
- $n$ (graph size)

### What does "same perceptual core" mean?

Options, from coarsest to finest:
1. Same diagnostic vector $d = (\text{Bind, Sep, Inside, Persist}) \in [0,1]^4$
2. Same formation topology (number of connected components, persistence barcode)
3. Same basin structure (same attractor landscape, same transition graph)

We want at least option 2 (topology-including readout).

---

## Key Mathematical Structures

### Why compact gauge group?

The orbit space $\mathcal{M}/G$ is:
- Compact iff $\mathcal{M}$ is compact AND $G$ acts properly
- Hausdorff iff $G$ acts properly (for locally compact $\mathcal{M}$)
- A smooth manifold iff $G$ acts freely and properly (no fixed points)
- An orbifold iff $G$ acts properly but not freely (fixed points allowed)

For finite $G$: properness is automatic. So $\mathcal{M}/G$ is always compact (given compact $\mathcal{M}$) and Hausdorff.

### Why does the gauge group NOT reduce dimension?

For a finite group $G$ acting on an $n$-manifold $M$:
$$\dim(M/G) = n$$

at generic points (where the action is free). Orbifold singularities occur at fixed points but don't change the ambient dimension.

Continuous compact Lie group $G$ of dimension $k$ acting freely:
$$\dim(M/G) = n - k$$

So only continuous groups reduce dimension. Finite groups $S_K$, $\text{Aut}(X)$ are zero-dimensional — no dimension reduction.

### Where does low effective dimension come from?

Three sources:
1. **Normalization constraints**: $\alpha + \beta = 1$ (removes 1 DOF); $\sum \lambda_i = 1$ (removes 1 DOF)
2. **Criticality hypothesis**: $q = q_c(X_t)$ (removes 1 DOF — $q$ becomes scene function)
3. **Relevance/irrelevance flow** (RG-analogy): not all directions in parameter space equally affect perception; irrelevant directions flow to constants

---

## The Double-Well Structure

$W(u) = u^2(1-u)^2$, $W'(u) = 2u(1-u)(1-2u)$

$$W''(u) = 2(1 - 6u + 6u^2)$$

Spinodal zone: $W''(c) < 0$ for $c \in \left(\frac{3-\sqrt{3}}{6}, \frac{3+\sqrt{3}}{6}\right) \approx (0.211, 0.789)$

At $c = 1/2$: $W''(1/2) = 2(1 - 3 + 3/2) = -1$, so $|W''(1/2)| = 1$.

Phase transition ratio:
$$q_c = \frac{4\lambda_2}{|W''(c)|} = \frac{4\lambda_2}{2(6c - 6c^2 - 1)}$$

---

## Gauge Action: What Exactly Does G Act On?

**Critical subtlety:** The global parameters $(q, \lambda, \xi)$ are scalar-valued. Neither $S_K$ nor $\text{Aut}_{task}$ acts on them directly (since they're graph-global).

The gauge action acts on:
- Formation labelings: $S_K$ permutes $(u^{(1)}, \ldots, u^{(K)})$
- Spatial coordinates: $\text{Aut}_{task}$ permutes graph nodes

So the gauge acts on **field configurations**, not directly on parameter space.

**Consequence:** The observer moduli space has two layers:
1. **Parameter layer**: $(q, \lambda, \xi)$ — no gauge action directly
2. **Formation layer**: $(u^{(1)}, \ldots, u^{(K)})$ — $S_K \times \text{Aut}_{task}$ acts

For the moduli space, we quotient the COMBINED space:
$$\mathcal{M}_{\text{obs}} \times \mathcal{U}_K / (G \text{ acting on } \mathcal{U}_K)$$

or we define equivalence on $\mathcal{M}_{\text{obs}}$ via induced equivalence from field outputs.

**Conservative approach:** Model the observer moduli space as the quotient of the **extended parameter space** where per-formation parameters are included.

---

## Attractor Basin Structure (Seed Model)

From the conversation: $\Theta_o(t) = F^t(s_o)$ (observer as dynamical system).

For the moduli space, we DON'T formalize $F$ — that's a separate Level-3 extension. Instead:
- We fix $\Theta_o$ as a static observer configuration
- The moduli space classifies static observer types
- Dynamics are treated as a separate question (OP-OMS-008)

---

## Topology of Δ³ (Minimal Case)

The 3-simplex $\Delta^3$ in $\mathbb{R}^4$:
$$\Delta^3 = \{(\lambda_1, \lambda_2, \lambda_3, \lambda_4) : \lambda_i \geq 0, \sum_i \lambda_i = 1\}$$

Properties:
- Homeomorphic to the closed 3-ball $B^3$
- Compact: closed and bounded in $\mathbb{R}^4$
- Convex: affine convex hull of 4 vertices
- Contractible: deformation retract to any point
- $\pi_k(\Delta^3) = 0$ for all $k \geq 0$
- $\chi(\Delta^3) = 1$ (Euler characteristic via CW decomposition: 4 vertices - 6 edges + 4 faces - 1 interior = 1)

**Key implication:** In the minimal model, no topological barrier exists between observer states. Perceptual discontinuity must come from $V(\Theta)$ basin structure, not from $\mathcal{M}$ topology.

---

## Symmetric Product Sym²(A)

For $A = [a, b]$ (interval), $S_2$ acts on $A^2$ by swapping coordinates:
$$\text{Sym}^2(A) = A^2 / S_2 \cong \{(x,y) \in A^2 : x \leq y\}$$

This is a closed triangular region — homeomorphic to $A^2$ (still a square, topologically).

Singular set: $\{(x,x) : x \in A\}$ — the diagonal, where stabilizer $= S_2$.

For $A = \Delta^3$: $\text{Sym}^2(\Delta^3) = (\Delta^3 \times \Delta^3)/S_2$. More complex, but still compact.

---

## Key Assumptions to State Explicitly

1. Observers are STATIC (no dynamics)
2. Scene is FIXED ($X_t$ given)
3. Mass $m$ is scene-determined
4. Criticality hypothesis is optional (two versions: with/without)
5. $G_{\text{core-weight}} = \{e\}$ (default, not proved)
6. $\text{Aut}_{task}$ is task-specific (not purely mathematical)
