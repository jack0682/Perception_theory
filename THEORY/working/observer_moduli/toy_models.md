---
type: working/toy-models
created: 2026-05-07
project: Observer Moduli Space of SCC
depends_on: definitions.md
---

> [!nav] Linked: [[MOC_observer_moduli_OMS]] · [[THEORY_INDEX]]


# Toy Models — Observer Moduli Space

Two fully computed examples of $\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$ under simplifying assumptions.

---

## Toy Model A: Minimal Case ($K = 1$, $\xi$ fixed, strict criticality)

### Setup

Impose the following simplifying assumptions:

| Assumption | Meaning |
|---|---|
| $K = 1$ | Exactly one formation |
| $S_K = S_1 = \{e\}$ | Trivial permutation group |
| $\mathrm{Aut}_{task} = \{e\}$ | No task symmetry |
| $\xi$ fixed | Auxiliary hyperparameters held constant |
| Strict criticality | $q = q_c(X_t)$, so $q$ is scene-determined |

Under these assumptions:
- $G_{\mathrm{SCC}}^{(0)} = S_1 \times \{e\} = \{e\}$ (trivial gauge group)
- Criticality eliminates $q$ from the free observer parameters
- $\xi$ fixed eliminates $B_\xi$

The observer space reduces to:

$$\mathcal{M}_{\mathrm{obs}}^{\min} = \Delta^3$$

where $\Delta^3 = \{(\lambda_1, \lambda_2, \lambda_3, \lambda_4) \in \mathbb{R}^4 : \lambda_i \geq 0,\ \sum_i \lambda_i = 1\}$ is the energy-weight simplex.

The moduli space (trivial quotient) is:

$$\mathfrak{M}_{\min} = \Delta^3 / \{e\} \cong \Delta^3$$

### Topology of $\Delta^3$

**Definition (standard 3-simplex).** The standard 3-simplex in $\mathbb{R}^4$:

$$\Delta^3 = \left\{ (\lambda_1, \lambda_2, \lambda_3, \lambda_4) \in \mathbb{R}^4 : \lambda_i \geq 0,\ \sum_{i=1}^4 \lambda_i = 1 \right\}$$

This is the convex hull of the four standard basis vectors $\{e_1, e_2, e_3, e_4\} \subset \mathbb{R}^4$.

**Proposition A1 (Compactness).** $\Delta^3$ is compact.

*Proof.* $\Delta^3$ is closed (defined by equality + inequality constraints on a Euclidean space) and bounded ($\lVert \lambda \rVert_1 = 1$ implies $\lVert \lambda \rVert_2 \leq 1$). By Heine–Borel, compact. $\square$

**Proposition A2 (Convexity).** $\Delta^3$ is convex.

*Proof.* For $\lambda, \mu \in \Delta^3$ and $t \in [0,1]$: the components of $t\lambda + (1-t)\mu$ are non-negative (convex combination of non-negatives) and sum to 1 (linearity of sum). $\square$

**Proposition A3 (Contractibility).** $\Delta^3$ is contractible.

*Proof.* For any fixed point $p \in \Delta^3$ (e.g., $p = (1/4, 1/4, 1/4, 1/4)$), the map

$$H : \Delta^3 \times [0,1] \to \Delta^3, \quad H(\lambda, t) = (1-t)\lambda + t \cdot p$$

is continuous (linear in both arguments), satisfies $H(\lambda, 0) = \lambda$ (identity) and $H(\lambda, 1) = p$ (constant). By convexity (Prop A2), $H(\lambda, t) \in \Delta^3$ for all $(\lambda, t)$. This is a deformation retract to $p$. $\square$

**Corollary A4 (Homotopy groups).** $\pi_k(\Delta^3) = 0$ for all $k \geq 0$.

*Proof.* Contractible spaces have trivial homotopy groups. In particular:
- $\pi_0(\Delta^3) = 0$: $\Delta^3$ is path-connected (Prop A3 gives a path from any point to $p$)
- $\pi_1(\Delta^3) = 0$: simply connected
- $\pi_k(\Delta^3) = 0$ for $k \geq 2$: by contractibility $\square$

**Proposition A5 (Euler characteristic).** $\chi(\Delta^3) = 1$.

*Proof (CW decomposition).* $\Delta^3$ has a natural CW structure:
- 0-cells (vertices): 4 (the $e_i$)
- 1-cells (edges): $\binom{4}{2} = 6$
- 2-cells (faces): $\binom{4}{3} = 4$ (triangular faces)
- 3-cells (interior): 1

$$\chi = 4 - 6 + 4 - 1 = 1 \quad \square$$

**Proposition A6 (Homeomorphism to 3-ball).** $\Delta^3 \cong B^3$ (closed 3-ball).

*Proof (sketch).* Both are compact, convex, 3-dimensional manifolds-with-boundary in their respective ambient spaces. Any such space is homeomorphic to the closed ball (by e.g. radial projection from an interior point). $\square$

### Vertices of $\Delta^3$ and Their Perceptual Meaning

The four vertices of $\mathfrak{M}_{\min} \cong \Delta^3$ correspond to pure perceptual strategies:

| Vertex | $\lambda$ | Dominant energy | Perceptual emphasis |
|---|---|---|---|
| $v_1 = e_1$ | $(1,0,0,0)$ | $E_{\mathrm{cl}}$ only | Pure closure (shape integrity) |
| $v_2 = e_2$ | $(0,1,0,0)$ | $E_{\mathrm{sep}}$ only | Pure separation (background contrast) |
| $v_3 = e_3$ | $(0,0,1,0)$ | $E_{\mathrm{bd}}$ only | Pure boundary smoothness |
| $v_4 = e_4$ | $(0,0,0,1)$ | $E_{\mathrm{tr}}$ only | Pure temporal transport |
| centroid | $(1/4, 1/4, 1/4, 1/4)$ | All equal | Balanced observer |

The edges, faces, and interior of $\Delta^3$ represent mixed strategies.

### Key Implication

In the minimal model, there is **no topological barrier** between observer states. Any observer $\lambda \in \Delta^3$ can be continuously deformed into any other. 

Perceptual discontinuity must therefore arise from the structure of $V(\Theta)$ (the perception-generating potential) — specifically from its basin structure — not from the topology of the moduli space itself.

**Consequence for OP-OMS-003:** The connectedness question is trivially resolved in the minimal model ($\Delta^3$ is connected). Non-trivial topology, if it exists, must emerge from: (a) non-trivial $G$-action, (b) non-trivial $B_\xi$ topology, or (c) non-constant $q$ (criticality not imposed).

---

## Toy Model B: Two-Formation Case ($K = 2$, $S_2$-action)

### Setup

Impose:

| Assumption | Meaning |
|---|---|
| $K = 2$ | Two formations |
| $S_K = S_2$ | Non-trivial permutation group |
| $\mathrm{Aut}_{task} = \{e\}$ | No task symmetry |
| $\xi$ fixed | Auxiliary hyperparameters held constant |
| Strict criticality | $q$ scene-determined |

Now each formation carries its own energy-weight vector:

$$\theta^{(k)} = (\lambda^{(k)}_{\mathrm{cl}}, \lambda^{(k)}_{\mathrm{sep}}, \lambda^{(k)}_{\mathrm{bd}}, \lambda^{(k)}_{\mathrm{tr}}) \in \Delta^3, \quad k = 1, 2$$

The joint observer state for two formations is:

$$\Theta = (\theta^{(1)}, \theta^{(2)}) \in \Delta^3 \times \Delta^3 = A \times A$$

where $A = \Delta^3$.

### The $S_2$-Action

The gauge group $S_2 = \{e, \tau\}$ acts by swapping formation labels:

$$\tau \cdot (\theta^{(1)}, \theta^{(2)}) = (\theta^{(2)}, \theta^{(1)})$$

This is well-defined since the formations are physically unlabeled (labels are redundant).

The moduli space is:

$$\mathfrak{M}_2 = (A \times A) / S_2 = \mathrm{Sym}^2(A)$$

### Explicit Computation

**Definition (Symmetric product).** For a topological space $A$:
$$\mathrm{Sym}^2(A) = (A \times A) / S_2$$
where $S_2$ acts by $(\theta^{(1)}, \theta^{(2)}) \mapsto (\theta^{(2)}, \theta^{(1)})$.

**Proposition B1 (Fundamental domain).** A fundamental domain for the $S_2$-action on $A \times A$ is:

$$F = \{(\theta^{(1)}, \theta^{(2)}) \in A \times A : \theta^{(1)} \leq \theta^{(2)}\}$$

where $\leq$ is any total order on $A$ (e.g., lexicographic on $\Delta^3 \subset \mathbb{R}^4$).

*Proof.* Each orbit $\{\theta^{(1)}, \theta^{(2)}\}$ (as an unordered pair) has a unique representative with $\theta^{(1)} \leq \theta^{(2)}$, except on the diagonal $\Delta_A = \{(\theta, \theta) : \theta \in A\}$ where both orders coincide. $\square$

**Simplified case: $A = [a, b]$ (interval).**

If each formation has a single scalar parameter (e.g., only $\lambda_{\mathrm{cl}}$ varies), then $A = [a, b]$ and:

$$\mathrm{Sym}^2([a,b]) = \{(\theta^{(1)}, \theta^{(2)}) \in [a,b]^2 : \theta^{(1)} \leq \theta^{(2)}\}$$

This is a **closed triangular region** in $[a,b]^2$ — bounded by:
- The diagonal $\theta^{(1)} = \theta^{(2)}$ (above)
- The bottom edge $\theta^{(1)} = a$ (left)
- The right edge $\theta^{(2)} = b$ (top)

**Proposition B2 (Topology of $\mathrm{Sym}^2([a,b])$).** The triangular region is homeomorphic to $[a,b]^2$, hence to the closed square — it is compact, connected, and contractible.

*Proof.* The map $(\theta^{(1)}, \theta^{(2)}) \mapsto (\theta^{(1)}/(\theta^{(1)}+\theta^{(2)}), \theta^{(1)}+\theta^{(2)})$ gives a homeomorphism to a rectangle. $\square$

### Orbifold Singularity: The Diagonal

**Definition (Diagonal).** $\Delta_A = \{(\theta, \theta) : \theta \in A\} \subset A \times A$.

On $\Delta_A$, the stabilizer is full:

$$G_{(\theta,\theta)} = S_2 \quad \text{(the swap acts trivially at } (\theta,\theta)\text{)}$$

Off $\Delta_A$, for $\theta^{(1)} \neq \theta^{(2)}$:

$$G_{(\theta^{(1)}, \theta^{(2)})} = \{e\}$$

**Proposition B3 (Orbifold singularity).** The image of $\Delta_A$ in $\mathrm{Sym}^2(A)$ is the singular stratum of the orbifold structure. Locally at a point $[\theta,\theta]$, the moduli space looks like:

$$(\mathbb{R}^d \times \mathbb{R}^d) / S_2 \cong (\mathbb{R}^d)^+ \times \mathbb{R}^d$$

where $d = \dim A = 3$ (for $A = \Delta^3$), reflecting the cone structure of the quotient near the diagonal.

### Perceptual Meaning of the Diagonal

The diagonal $\Delta_A$ in $\mathrm{Sym}^2(\Delta^3)$ corresponds to **identical formation observers**: an observer where both formations are governed by the same energy weights $\lambda^{(1)} = \lambda^{(2)}$.

- **Generic point** (off diagonal): the two formations are perceptually asymmetric (different closure/separation emphases).
- **Diagonal point**: both formations are treated identically — a "symmetric" or "undifferentiated" observer state.

The orbifold singularity at the diagonal is **not a pathology**: it reflects the genuine physical degeneracy when formation labels are interchangeable.

### Sym²(Δ³): Full Case

For $A = \Delta^3$:

$$\mathfrak{M}_2 = \mathrm{Sym}^2(\Delta^3) = (\Delta^3 \times \Delta^3) / S_2$$

**Dimension:** $\dim(\Delta^3 \times \Delta^3) = 6$; gauge group $S_2$ has order 2 but is discrete (0-dimensional); hence $\dim \mathfrak{M}_2 = 6$ at generic points.

**Topology:** $\mathrm{Sym}^2(\Delta^3)$ is:
- Compact (quotient of compact by compact)
- Connected (quotient of connected by connected)
- Has an orbifold singularity along $\mathrm{Sym}^2(\partial\Delta^3) \cup \{$diagonal$\}$
- Generic stratum (off diagonal): smooth 6-manifold
- Diagonal stratum: $\Delta^3$ (3-dimensional singular locus with stabilizer $S_2$)

**Stratification:**
$$\mathfrak{M}_2 = \mathfrak{M}_2^{\mathrm{gen}} \cup \mathfrak{M}_2^{\mathrm{sing}}$$

where:
- $\mathfrak{M}_2^{\mathrm{gen}} = \{[\theta^{(1)}, \theta^{(2)}] : \theta^{(1)} \neq \theta^{(2)}\}$ — open dense stratum, dimension 6
- $\mathfrak{M}_2^{\mathrm{sing}} = \{[\theta, \theta] : \theta \in \Delta^3\} \cong \Delta^3$ — singular stratum, dimension 3

---

## Comparison of Toy Models

| Feature | Model A ($K=1$) | Model B ($K=2$) |
|---|---|---|
| Gauge group | $\{e\}$ | $S_2$ |
| Moduli space | $\Delta^3$ | $\mathrm{Sym}^2(\Delta^3)$ |
| Dimension | 3 | 6 |
| Compact | Yes | Yes |
| Connected | Yes | Yes |
| Contractible | Yes | ? (open problem) |
| Singular strata | None | $\Delta_A \cong \Delta^3$ |
| Orbifold type | Smooth manifold-with-boundary | Orbifold with codim-3 singularity |
| $\pi_1$ | $0$ | ? |
| $\chi$ | 1 | ? |

---

## Open Questions from Toy Models

These observations generate specific open problems (see `open_problems.md`):

1. **OP-OMS-003 (connectivity):** Is $\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$ connected for general $(K, G)$? Toy Model A: yes. Toy Model B: yes (quotient of connected). General case: unclear when $\mathrm{Aut}_{task}$ acts non-trivially.

2. **OP-OMS-004 (contractibility of $\mathrm{Sym}^2(\Delta^3)$):** Is $\mathrm{Sym}^2(\Delta^3)$ contractible? If yes, the same implication as Model A holds (no topological barriers). Note: $\mathrm{Sym}^2(X)$ is contractible when $X$ is contractible (since $\mathrm{Sym}^2$ preserves contractibility — use join construction or Steenrod argument). Requires verification for manifolds-with-boundary.

3. **OP-OMS-005 (orbifold volume):** What is the volume ratio $\mathrm{Vol}(\mathfrak{M}_2^{\mathrm{sing}}) / \mathrm{Vol}(\mathfrak{M}_2)$ in appropriate measure? This quantifies how often real observers sit at the singular (symmetric) stratum.

4. **OP-OMS-006 ($K \geq 3$):** For $K \geq 3$, $\mathrm{Sym}^K(\Delta^3) = (\Delta^3)^K / S_K$. The singular structure becomes a stratified space with multiple strata indexed by partition types of $\{1,\ldots,K\}$. Explicit computation needed.

---

## Notes for Future Development

- Model A establishes the **baseline** for perceptual indistinguishability within a single-formation observer.
- Model B establishes the **formation-symmetry singularity** — the first non-trivial quotient structure.
- Both models support the claim that **topological barriers are absent** in $\mathfrak{M}$ (assuming $\mathrm{Sym}^K$ of contractible spaces remains contractible), so perceptual discreteness must arise from $V(\Theta)$ basin structure.
- The critical case ($q$ scene-determined) gives a much smaller moduli space: Model A reduces $\dim$ by 1 (from 4 to 3), Model B reduces $\dim$ by 1 (from 7 to 6).
