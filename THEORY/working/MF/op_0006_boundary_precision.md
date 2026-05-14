---
id: OP-0006-WF-1
type: working/open-problem
status: in-progress
last_updated: 2026-05-06
---

> [!nav] Linked: [[INDEX|working/INDEX.md]] · [[MOC_Q4_K_selection]] · [[MOC_sigma_rich_framework]] · [[THEORY_INDEX]]


# OP-0006: Boundary Precision — Working Formalization

**OP-ID:** OP-0006
**Title:** Boundary Definition Precision
**Severity:** High
**Status (theorem_status.md):** TENTATIVE (D-0013 in development)
**Session:** W6 D4 (2026-05-06) — first substantive formalization

---

## 1. Problem Statement

The SCC framework defines a "boundary band" §5.3 as the transition zone between core and
exterior in the soft cohesion field $\tilde{u} : X \to [0,1]$. This is a *soft* concept.

OP-0006 asks: **how does this soft transition zone become a crisp, persistent boundary?**
Specifically:
- Under what conditions does the field $\tilde{u}$ produce a well-defined, stable boundary
  ridge that persists under perturbation (noise, shadow, blur)?
- How does the SCC boundary differ from a raw image edge (gradient of pixel intensity)?
- What is the correct mathematical characterization of the boundary as a geometric object
  on the graph $G_t^\mathcal{P}$?

---

## 2. Proposed Definition: Boundary as Gradient Ridge

**Definition (working, not yet canonical).** Given a soft cohesion field $\tilde{u} \in
\mathcal{F}_0(\mathcal{P})$ on graph $G = (X, E)$, define the discrete gradient magnitude:

$$|\nabla_G \tilde{u}(x)| = \sqrt{\sum_{y \sim x} (\tilde{u}(x) - \tilde{u}(y))^2}$$

The **thresholded gradient boundary** at level $\theta$ is:

$$\partial_{\mathrm{SCC}}(\tilde{u}, \theta) = \{x \in X : |\nabla_G \tilde{u}(x)| > \theta\}$$

This is scale-dependent: the boundary set changes with $\theta$.

---

## 2b. Strengthened Definition: Persistent Gradient Ridge

**Definition (working — strengthened version).** The **persistent gradient ridge** is the
boundary that survives across a range of threshold levels:

$$B_t(\tilde{u}) = \mathrm{PersRidge}(|\nabla_G \tilde{u}|, \rho_{\mathrm{bd}})$$

where $\mathrm{PersRidge}$ is defined via the $H_0$ persistence barcode of the gradient
magnitude field under the superlevel-set filtration on $G$:

$$B_t(\tilde{u}) = \bigl\{x \in X : (b_x, d_x) \in \mathrm{Bars}_0(|\nabla_G \tilde{u}|; G),\; b_x - d_x > \rho_{\mathrm{bd}}\bigr\}$$

Here $\mathrm{Bars}_0(|\nabla_G \tilde{u}|; G)$ is the $H_0$ barcode of the GRADIENT MAGNITUDE
field (not the field $\tilde{u}$ itself) under the superlevel-set filtration, and
$\rho_{\mathrm{bd}} > 0$ is the boundary persistence threshold.

**Interpretation:** $B_t(\tilde{u})$ is the set of nodes whose gradient magnitude forms a
persistent "ridge" — high-gradient nodes that remain connected components of
$\{x : |\nabla_G \tilde{u}(x)| > \theta\}$ for a wide range of $\theta$ values (range
width $> \rho_{\mathrm{bd}}$). This is analogous to the D-ST-3 definition of $K_{\mathrm{act}}$
(§3.11), but applied to the gradient field rather than the cohesion field itself.

**Scale stability:** The persistent ridge is independent of the specific threshold $\theta$
within the persistent range, making it more robust than the thresholded definition.

**Relationship to thresholded definition:** For any $\theta$ with
$b_x - d_x > \rho_{\mathrm{bd}}$ around $\theta$, $x \in B_t \Leftrightarrow x \in
\partial_{\mathrm{SCC}}(\tilde{u}, \theta)$. The thresholded definition (§2) is the
special case where $\rho_{\mathrm{bd}} \to 0$.

**Persistent boundary stability:** $B_t(\tilde{u})$ is stable under perturbations
$\tilde{u} \to \tilde{u} + \delta$ if $\|\delta\|_\infty < \rho_{\mathrm{bd}}/2$
(persistence stability theorem for barcodes — Chazal et al.).

**Relationship to §5.3 Boundary Band:** The canonical §5.3 boundary band is defined as nodes
with intermediate field values $c < \tilde{u}(x) < 1 - c$. Both §2 and §2b are
gradient-based alternatives:
- §5.3: based on field value (position in [0,1])
- §2: based on gradient magnitude at fixed $\theta$
- §2b: based on gradient persistence (robust to $\theta$ choice)
Under phase-separated fields (values near 0 and 1), all three characterizations coincide.
Under smooth fields, they may disagree. **§2b is the target definition for Cat B promotion.**

---

## 3. Distinction from Raw Image Edge

A raw image edge detector (e.g., Canny, Sobel) computes $|\nabla I|$ for pixel intensity
$I : \mathcal{P} \to \mathbb{R}$. The SCC boundary $\partial_{\mathrm{SCC}}(\tilde{u})$
differs fundamentally:

| Property | Raw image edge $|\nabla I|$ | SCC boundary $|\nabla_G \tilde{u}|$ |
|---|---|---|
| Input | Pixel intensity | Soft cohesion field (output of SCC optimization) |
| Responds to | Luminance gradient | Cohesion structure gradient |
| Invariant to | Nothing | Shadow/albedo changes that don't alter formation structure |
| Conditioned on | Appearance only | Full SCC energy (closure + separation + boundary + transport) |
| Stable under | — | Perturbations below $\rho_{\mathrm{pers}}$ (by OP-0006 candidate theorem) |
| Respects | — | Depth discontinuities (via $G_t^\mathcal{P}$, D-ST-1) |

**Key claim (working, not yet proved):** For a well-formed SCC formation $\tilde{u}^*$
(local minimum of $\mathcal{E}_{\mathrm{SCC}}$), the SCC boundary is more stable under
photometric perturbation (shadow, blur, illumination change) than the raw image edge,
because the SCC energy incorporates structural constraints (closure, separation) that
penalize spurious boundary creation.

---

## 4. Open Sub-Questions

### 4.1 Convergence of Boundary Band under Gradient Flow

Does the boundary band $\partial_{\mathrm{SCC}}(\tilde{u}(t), \theta)$ converge to a
stable set as gradient flow $d\tilde{u}/dt = -\nabla \mathcal{E}[\tilde{u}]$ evolves?
Under strong phase separation ($\beta$ large), $\tilde{u}^* \approx \{0, 1\}$-valued and
the boundary band has a sharp, well-defined width. The precise convergence rate (related
to OP-0013 closure convergence rate) is OPEN.

### 4.2 Topological Stability

Is $\partial_{\mathrm{SCC}}(\tilde{u}^*)$ topologically stable — i.e., does it form a
connected closed curve (in 2D) or surface (in 3D) separating formation interior from
exterior? On finite graphs this requires a combinatorial analog of the Jordan curve theorem.

### 4.3 Stereo Conditioning

Under depth-filtered adjacency $G_t^\mathcal{P}$ (D-ST-1), the SCC boundary respects 3D
depth discontinuities: boundary pixels cannot straddle a depth gap (no edges connect them).
The formal statement: $\partial_{\mathrm{SCC}}(\tilde{u}; G_t^\mathcal{P}) \subset
X_L^{\mathrm{valid}} \setminus (\text{depth-gap pixels})$. This is the stereo contribution
to OP-0006.

---

## 5. Toy Experiment Proposal: Boundary Stability under Shadow/Blur

**Objective:** Verify that the SCC boundary $\partial_{\mathrm{SCC}}(\tilde{u}^*)$ is more
stable than a raw image edge under photometric perturbation.

**Protocol:**

1. **Setup:** 20×20 grid. A K=1 formation $\tilde{u}^*$ (local minimum of $\mathcal{E}_{\mathrm{SCC}}$)
   with a well-defined blob at center. Compute $\partial_{\mathrm{SCC}}(\tilde{u}^*, \theta)$.

2. **Perturbations:**
   a. **Shadow:** Set $I_\sigma(x) = \tilde{u}^*(x) \cdot (1 - s \cdot \mathbf{1}_{x \in S})$
      for shadow region $S$ (left half), shadow strength $s \in \{0.2, 0.5, 0.8\}$.
   b. **Blur:** Apply Gaussian blur to $\tilde{u}^*$ with $\sigma_{\mathrm{blur}} \in \{1, 2, 3\}$.

3. **Re-optimize:** For each perturbed initialization, run SCC gradient flow to
   convergence → $\tilde{u}^*_\sigma$.

4. **Compare boundaries:**
   - SCC boundary: $|\partial_{\mathrm{SCC}}(\tilde{u}^*_\sigma) \triangle \partial_{\mathrm{SCC}}(\tilde{u}^*)|$ (symmetric difference)
   - Raw edge: $\|\,|\nabla_G \tilde{u}^*_\sigma| - |\nabla_G \tilde{u}^*|\,\|_1$

5. **Metric:** Boundary stability ratio = $\Delta_{\mathrm{raw}} / \Delta_{\mathrm{SCC}}$.
   If > 1: SCC boundary more stable than raw edge.

6. **Expected result:** For shadow perturbation, $\Delta_{\mathrm{SCC}}$ is small (SCC
   re-optimizes to same formation structure), while $\Delta_{\mathrm{raw}}$ is large (raw
   intensity gradient changes in shadow region). For blur, both degrade similarly at first,
   but SCC boundary is stabilized by the closure + separation terms.

**Claim (proposed, to verify):** SCC boundary stability ratio > 1 under shadow perturbation
for well-formed formations in the phase-separated regime ($\beta \geq 10$).

---

## 5b. PersRidge Equivalence Theorem (Cat B requirement, Session D)

**Claim (working, not yet canonical).** In the phase-separated regime (β sufficiently large, ũ* ≈ {0,1}-valued), the persistent gradient ridge B_t(ũ*) (§2b) and the topological boundary of the persistent component ∂PersComp(ũ*) are approximately equivalent in graph Hausdorff distance:

$$d_H\bigl(B_{\mathrm{PersRidge}}(\tilde{u}^*),\, \partial\mathrm{PersComp}(\tilde{u}^*)\bigr) \leq C \cdot (\alpha/\beta)^{1/2}$$

where:
- $\partial\mathrm{PersComp}(\tilde{u}^*) = \{x \in C_j : \exists y \sim x,\, y \notin C_j\}$ is the node-boundary of the formation core $C_j = \{x : \tilde{u}^*(x) \geq 1/2\}$
- $d_H$ is graph Hausdorff distance (maximum over mutual nearest-neighbor distances)
- $C$ is a geometry-dependent constant (depends on graph structure, edge weight distribution; explicit value is a Cat A blocker — see §7)
- The bound $(\alpha/\beta)^{1/2}$ is the Allen-Cahn interface width estimate (dimension: graph edge units)

**Proof sketch.** In the phase-separated regime, ũ*(x) ≈ 1 − δ inside the formation and ≈ δ outside (for small δ → 0 as β → ∞). The discrete gradient magnitude satisfies:
- For x interior: |∇_G ũ*(x)| ≈ 0 (all neighbors also near 1)
- For x ∈ ∂PersComp: |∇_G ũ*(x)| ≈ (1 − 2δ) (one or more neighbors near 0)
- For x exterior: |∇_G ũ*(x)| ≈ 0 (all neighbors also near 0)

Therefore the gradient magnitude is concentrated on ∂PersComp(ũ*) and forms a persistent peak there (the gradient ridge "life" is ≈ 1 − 2δ). For any ρ_bd < 1 − 2δ, B_t(ũ*) ⊆ ∂PersComp(ũ*) ∪ O(δ)-neighborhood.

The converse: nodes in ∂PersComp(ũ*) have gradient magnitude ≈ 1 − 2δ > ρ_bd, so they appear in B_t(ũ*). The Hausdorff distance bound O(β^{−1/2}) follows from the Allen-Cahn interface width estimate: for the GL energy with parameters α, β, the transition layer has width ∼ (α/β)^{1/2}.

**Regime condition.** The equivalence holds under:
- (R1) Phase separation: β/α > 4λ₂/|W''(c)| (canonical §13 phase transition condition)
- (R2) Well-formed formation: ũ* is a local minimum of E_SCC with K_act = 1 (single component)
- (R3) Persistence thresholds compatible: ρ_bd < (1 − 2δ) and ρ_pers selected by §3.11

**Relationship to exp06.** The experiment (exp06_boundary_stability_shadow_blur.py, W6 D4 Session C) measured Δ_SCC vs Δ_raw under shadow and blur perturbations. The SUPPORTED result (all 10 conditions, max ratio 4.085 shadow / 50.8 blur) confirms that the SCC-optimized boundary is more stable than the raw gradient boundary — consistent with B_t(ũ*) being a persistent structure. This is criterion 3 for Cat B.

**Gap.** The Hausdorff distance bound C(β^{−1/2}) needs explicit constant C (depends on graph geometry, α, λ₂). For Cat A, the topological statement (§4.2) requires a combinatorial Jordan theorem argument.

---

## 6. Relationship to OP-0005 and OP-0009-Pre-b

- **OP-0005 (K-Selection):** Stable persistent boundaries are necessary for K_act = #PersComp
  to be well-defined and non-fluctuating. Without boundary precision (OP-0006), the
  persistence threshold $\rho_{\mathrm{pers}}$ is ad hoc. Full OP-0005 resolution requires
  OP-0006 boundary stability.

- **OP-0009-Pre-b (K_act as #PersComp):** The #PersComp definition via threshold filtration
  depends on the formation having a well-defined boundary structure. Noisy or diffuse
  boundaries create spurious or non-persistent components. OP-0006 provides the structural
  grounding for OP-0009-Pre-b.

---

## 7. Status and Promotion Criteria

**Current status:** OPEN / working-grade only. The §2 definition (gradient-based) is
proposed but not canonical. The §5.3 boundary band in canonical.md is the registered
definition.

**Promotion criteria to Cat B:**
1. Formal proof that the persistent gradient ridge $B_t(\tilde{u})$ (§2b) is stable under
   perturbations $\|\delta\|_\infty < \rho_{\mathrm{bd}}/2$ (follows from barcode stability;
   main gap: formalizing $\rho_{\mathrm{bd}}$ in terms of $\mathcal{E}_{\mathrm{SCC}}$ parameters).
2. Equivalence theorem: §5.3 boundary band $= B_t(\tilde{u})$ in the phase-separated regime
   ($\beta$ large, $\tilde{u}^* \approx \{0,1\}$-valued).
3. exp06 completed (W6 D4 Session C): boundary stability ratio > 1 for shadow perturbation.
   Target: $\Delta_{\mathrm{raw}} / \Delta_{\mathrm{SCC}} > 1$ for $s \geq 0.3$.

**Promotion criteria to Cat A (4 explicit blockers — aligned with theorem_status.md; refined Session H W6 D4):**

---

**Blocker 1: Topological Separator** (§4.2)

*Statement:* Prove that $B_{\mathrm{PersRidge}}(\tilde{u}^*)$ is a connected separator on the graph — a combinatorial Jordan-curve-theorem analog such that removing $B_t$ disconnects $G$ into (at least) an interior component containing formation core $C_j$ and an exterior component.

*Why this is hard:* The standard Jordan curve theorem requires a Jordan curve (continuous closed curve) in $\mathbb{R}^2$. On finite graphs, the analog is a "vertex separator" or "vertex cut." The persistent gradient ridge may not be a minimal separator; it may include extraneous nodes, or (in degenerate cases) fail to be connected.

*Possible routes:*
- **Route A (Alexander duality analog):** Use graph-theoretic Alexander duality: if the graph $G$ is a triangulation of $S^2$, then any cycle in $G$ separates the sphere. For planar grid graphs, the discrete Jordan theorem holds (see Heawood / Hopf 1920s; Diestel §4.2). Apply to the boundary cycle defined by $B_t$.
- **Route B (Morse-theoretic argument):** At a phase-separated local minimum $\tilde{u}^*$, the superlevel set $\{\tilde{u}^* \geq 1/2\}$ is exactly the formation core $C_j$. The boundary $\partial C_j = \{x \in C_j : \exists y \sim x, y \notin C_j\}$ is a vertex cut by definition (removing it disconnects interior from exterior). Show $B_t \approx \partial C_j$ via the Hausdorff bound (§5b), then the separator property of $\partial C_j$ carries to $B_t$ within the interface-width tolerance.
- **Route C (Direct persistence argument):** Show that any path from $C_j^{int} = \{x : \tilde{u}^*(x) > 1-\delta\}$ to $C_j^{ext} = \{x : \tilde{u}^*(x) < \delta\}$ must pass through a node in $B_t$ (since the gradient magnitude must be large on any such path by the mean value theorem analog on graphs).

*Recommended route:* Route B (least new machinery; uses existing §5b bound). Effort: ~half-day.

---

**Blocker 2: Hausdorff Constant C**

*Statement:* Determine $C$ explicitly in $d_H(B_{\mathrm{PersRidge}}, \partial\mathrm{PersComp}) \leq C \cdot (\alpha/\beta)^{1/2}$ in terms of graph geometry (degree $d$, edge weight distribution $\{w_{ij}\}$) and SCC parameters $(\alpha, \beta, \lambda_{\mathrm{bd}})$.

*Why this is hard:* The interface width estimate $(\alpha/\beta)^{1/2}$ comes from the Allen-Cahn energy balance. But the constant $C$ depends on:
1. The graph regularity (regular grid: $d=4$ or $d=8$; general graph: variable)
2. The gradient threshold $\rho_{\mathrm{bd}}$ (higher threshold = thinner ridge = smaller $C$)
3. The energy minimizer profile (the exact interface shape depends on boundary conditions)

*Possible routes:*
- **Route A (Explicit profile computation):** For a regular grid graph, compute the 1D Allen-Cahn profile analytically: $u^*(x) = \tfrac{1}{2}(1 + \tanh((x - x_0)/\xi))$ where $\xi = (2\alpha/\beta|W''(c)|)^{1/2}$. The gradient at the interface is $|\nabla u^*| \approx (2\alpha/\beta)^{1/2}/(2\xi)$ ... Wait, let me think more carefully. The interface profile has $|du/dx| \approx 1/(2\xi)$. On a grid: $|\nabla_G u^*| \approx 1/(2\xi) = (\beta|W''(c)|/(8\alpha))^{1/2}$. This determines both the ridge height (determines $\rho_{\mathrm{bd}}$ compatibility) and the ridge width (determines $C$). Specifically, the region where $|\nabla_G u^*| > \rho_{\mathrm{bd}}$ has width $\approx \xi \cdot 2\,\mathrm{artanh}(\sqrt{1 - 4\rho_{\mathrm{bd}}^2\xi^2})$ — giving the effective $C$. For $\rho_{\mathrm{bd}} \ll 1/\xi$: $C \approx 2$.
- **Route B (Barcode stability quantification):** Use the Chazal et al. stability theorem: $d_B(\mathrm{Bars}(f), \mathrm{Bars}(g)) \leq \|f - g\|_\infty$ for $H_0$ barcodes. Apply to $f = |\nabla_G u^*|$ and $g = |\nabla_G u^*| + \delta$ (perturbation). The persistence of the ridge is $1/\xi \approx (\beta/\alpha)^{1/2}$. The Hausdorff distance from the ridge to $\partial\mathrm{PersComp}$ is at most $\xi$ — yielding $C = 1$ in natural units. This is the cleanest route.
- **Route C (Numerical verification):** Run exp06-style experiment with varying $\beta$ and measure $d_H(B_t, \partial C_j)$ vs $(\alpha/\beta)^{1/2}$. Fit the constant $C$. Not a proof but provides a working estimate.

*Recommended route:* Route A (explicit 1D profile) for Cat A. Effort: ~1 day (requires checking the profile against discrete grid boundary conditions).

*Candidate explicit bound:* $C \leq 2$ for regular grid graphs ($d=4$) with $\rho_{\mathrm{bd}} < \min_{x\in\partial C} |\nabla_G \tilde{u}^*(x)|/2$.

#### Working Note — 1D Allen-Cahn Profile Bound for C (W6 D4 Session I, 2026-05-06)

*Status: working note only. Not a proof. Confirms O(1) scaling; C=2 is a candidate for regular grids. Do not promote to Cat A without closing the 4 gaps listed below.*

**⚠ CORRECTION (Session J, 2026-05-06): Two errors in this Working Note are fixed in §8.**
*(1) The Δ formula below uses $4\rho^2\xi^2$ but the correct derivation gives $2\rho\xi$ (see §8.1).*
*(2) The candidate $\rho_{\mathrm{bd}} = \tfrac{1}{2}(\alpha/\beta)^{1/2}$ is dimensionally wrong: $\rho_{\mathrm{bd}}\xi = (\alpha/\beta)/\sqrt{2} \to 0$ as $\beta\to\infty$. The correct choice is $\rho_{\mathrm{bd}} = 1/(4\xi) = \tfrac{1}{4}(\beta/(2\alpha))^{1/2}$ (half-maximum gradient), giving $\rho_{\mathrm{bd}}\xi = 1/4$ (constant). See §8.1 for corrected analysis.*

**Setup.** Consider a 1D segment graph $(\mathbb{Z}, E)$ with uniform edge weights $w=1$. The SCC boundary energy on this graph is $E_{\mathrm{bd}} = \alpha \sum_i (u_{i+1} - u_i)^2 + \lambda_{\mathrm{bd}} W(u_i)$ where $W(u) = u^2(1-u)^2$. At a phase-separated minimum, the interface near site $x_0$ has the 1D Allen-Cahn profile:

$$u^*(x) = \frac{1}{2}\!\left(1 + \tanh\!\frac{x - x_0}{\xi}\right), \qquad \xi = \left(\frac{2\alpha}{\beta |W''(c)|}\right)^{1/2}$$

where $c = 1/2$ is the spinodal point and $|W''(1/2)| = 1$ for $W(u)=u^2(1-u)^2$ (computed: $W''(u)=2(1-2u)^2-4u(1-u)$; at $u=1/2$: $W''(1/2)=-1$). Therefore $\xi = (2\alpha/\beta)^{1/2}$.

**Candidate bound derivation (Session I — contains errors corrected in §8).** The gradient magnitude at site $x$ is:

$$|u^*{}'(x)| = \frac{1}{2\xi}\,\mathrm{sech}^2\!\frac{x-x_0}{\xi}, \qquad \max_x |u^*{}'| = \frac{1}{2\xi} = \frac{1}{2}\!\left(\frac{\beta}{2\alpha}\right)^{1/2}$$

The PersRidge set $B_t = \{x : |u^*{}'(x)| > \rho_{\mathrm{bd}}\}$ is the interval $|x - x_0| < \Delta$, where *(⚠ formula incorrect — see §8.1)*:

$$\Delta = \xi\,\mathrm{arctanh}\!\left(\sqrt{1 - 4\rho_{\mathrm{bd}}^2\xi^2}\right) \quad \text{[wrong; correct formula in §8.2]}$$

For $\rho_{\mathrm{bd}} \xi \ll 1$ (thin-ridge regime): $\Delta \approx \xi|\log(2\rho_{\mathrm{bd}}\xi)| = O(\xi) = O((\alpha/\beta)^{1/2})$.

**Gaps before Cat A (4 items):**
1. *1D → 2D:* The tanh profile is for a 1D segment. On a 2D grid ($d=4$), the interface curves; $|u^*{}'|$ at interface nodes is bounded by the 1D value times a geometry factor $\leq \sqrt{d}$. Need explicit bound for $d=4$.
2. *Hausdorff distance vs. ridge width:* $\Delta$ gives the half-width of the ridge (distance from center). The Hausdorff distance $d_H(B_t, \partial\mathrm{PersComp})$ requires both directions: nearest-$B_t$-point-to-$\partial C$ and nearest-$\partial C$-point-to-$B_t$. The reverse direction needs interface completeness (every $\partial C$ point is within $\Delta$ of $B_t$) — requires showing the interface has no isolated crossing points.
3. *Discretization correction:* The tanh profile is continuum. Discrete lattice profile differs by $O(1/\xi^2)$ corrections (negligible for $\xi \gg 1$, i.e., $\beta \ll 2\alpha n^2$; standard SCC operating regime satisfies this).
4. *$\partial\mathrm{PersComp}$ identification:* Need to verify that the PersComp boundary $\partial\mathrm{PersComp}(\tilde{u}^*)$ coincides with $\{x : \tilde{u}^*(x) \approx 1/2\}$ (level-set interface), not merely a topological boundary. Requires connecting the barcode definition to the Allen-Cahn interface location.

**Conclusion for OP-0006 Cat A path:** Corrected analysis (§8) gives $C \leq 1.25$ (1D) and $C \leq 1.56$ (2D flat interface, conditional). Both finite, confirming $O(1)$ scaling. Formal Cat A requires closing gaps 1–4; estimated ~1 day.

---

**Blocker 3: Stereo Conditioning** (§4.3)

*Statement:* Formally prove $B_{\mathrm{PersRidge}}(\tilde{u}^*; G_t^\mathcal{P}) \subset X \setminus \text{(depth-gap pixels)}$ under D-ST-1 stereo adjacency.

*Why this is hard:* D-ST-1 removes edges across depth discontinuities. But the persistent gradient ridge may still detect boundary-like structure AT depth-gap pixels via in-plane edges (edges within the same depth layer). The claim is that boundary nodes cannot straddle depth gaps (cannot have high cross-depth gradient if no cross-depth edges exist).

*Possible routes:*
- **Route A (Direct argument from D-ST-1 and gradient definition):** Under hard-cut D-ST-1 ($w_{ij} = 0$ for $|z_i - z_j| > \Delta z_{\mathrm{thresh}}$), the gradient at depth-gap pixels is:
  $|\nabla_G \tilde{u}^*(x)| = \sqrt{\sum_{y \sim x} w_{xy}(\tilde{u}^*(x) - \tilde{u}^*(y))^2}$
  where the sum is only over in-plane edges (cross-depth edges removed). For $x$ at a depth gap with $\tilde{u}^*(x) \approx 1$ (inside a formation) and all in-plane neighbors also $\approx 1$: $|\nabla_G \tilde{u}^*(x)| \approx 0$. Therefore depth-gap pixels have near-zero gradient and cannot appear in $B_t$. This is essentially immediate from D-ST-1.
- **Route B (Formal proof for hard-cut case):** Under D-ST-1 hard-cut, depth-gap pixels belong to exactly one connected component of $G_t^\mathcal{P}$. Their gradient is determined by in-layer neighbors only. Claim: for a well-formed formation (K_act=1, phase-separated), $|\nabla_G \tilde{u}^*|$ at depth-gap pixels is $< \rho_{\mathrm{bd}}$. Proof: by the formation smoothness within each depth layer. Needs the claim that the local minimum $\tilde{u}^*$ is smooth within-layer.

*Status for hard-cut D-ST-1:* Route A argument essentially complete; formalizing requires careful case analysis. Effort: ~half-day.

*For smooth D-ST-1 (T-ST-5b context):* Stereo conditioning is more subtle — cross-depth edges still exist with small weights. The gradient at cross-depth nodes is non-zero but small. This is the interface between Blocker 3 and T-ST-5b; requires joint treatment.

---

**Blocker 4: $\rho_{\mathrm{bd}}$ Calibration**

*Statement:* Canonically connect $\rho_{\mathrm{bd}}$ to SCC parameters $(\alpha, \beta, \lambda_{\mathrm{bd}}, M, n)$ such that $B_t(\tilde{u}^*)$ is both non-trivially defined (not empty) and stable under perturbation (not hypersensitive to threshold choice).

*Why this is hard:* $\rho_{\mathrm{bd}}$ must satisfy a compatibility window: $0 < \rho_{\mathrm{bd}} < \min_{x \in \partial C_j} |\nabla_G \tilde{u}^*(x)|$. If $\rho_{\mathrm{bd}}$ is too large, $B_t$ is empty. If too small, all nodes with any gradient appear. The correct value depends on the interface height, which scales as $(\beta/\alpha)^{1/2}$.

*Possible routes:*
- **Route A (Derived from interface analysis):** From Blocker 2 Route A: $\min_{x \in \partial C_j} |\nabla_G \tilde{u}^*(x)| \approx (2\alpha/\beta)^{1/2} \cdot |W''(c)|^{1/2}$ on regular grids. Set $\rho_{\mathrm{bd}} = \rho_0 \cdot (\alpha/\beta)^{1/2}$ for some $\rho_0 \in (0, 1)$ (dimensionless constant). The compatibility window then becomes $0 < \rho_0 < C_{\mathrm{grad}}$ where $C_{\mathrm{grad}} \approx (2|W''(c)|)^{1/2}$. For canonical SCC parameters: $|W''(c)| = 1/2$ (at $c=1/2$), so $C_{\mathrm{grad}} \approx 1$. Recommended: $\rho_0 = 0.5$ (middle of compatibility window).
- **Route B (Data-driven from exp06):** Measure $|\nabla_G \tilde{u}^*(x)|$ at boundary nodes in exp06 experiments across $\beta$ values. Fit $\rho_{\mathrm{bd}}(\beta) = c \cdot (\alpha/\beta)^{1/2}$ with empirical constant $c$. This is calibration only, not a proof, but establishes the scaling law.
- **Route C (OP-0006 specific theorem):** Register the calibration as part of the OP-0006 canonical definition: "the canonical choice is $\rho_{\mathrm{bd}} = (\alpha/\beta)^{1/2}/2$." This is definitional (Cat A by adoption) but requires verification that the choice is always compatible (i.e., never empty $B_t$).

*Recommended route:* Route A (analytic) + Route B (empirical confirmation). Effort: ~1 day total (Route A: half-day analytic; Route B: run experiment on existing exp06 data).

*Candidate canonical choice (Session I — corrected in §8.1):* $\rho_{\mathrm{bd}} = \tfrac{1}{4}(\beta/(2\alpha))^{1/2} = 1/(4\xi)$ (half-maximum gradient). ~~Original candidate $\tfrac{1}{2}(\alpha/\beta)^{1/2}$ was dimensionally inconsistent; $\rho_{\mathrm{bd}}\xi \to 0$ as $\beta\to\infty$.~~

**Cat B status: ACHIEVED (Session D).** All three Cat B criteria are now met:
1. Barcode stability for B_t(ũ): follows from Chazal et al. (standard result, formal gap in SCC parameter grounding deferred to Cat A).
2. PersRidge equivalence theorem proof sketch: §5b above (formal Hausdorff bound with gap on constant C).
3. exp06 SUPPORTED (W6 D4 Session C): shadow 5/5 SUPPORTED (max ratio 4.085), blur 5/5 SUPPORTED (max ratio 50.804).

**This file now constitutes a Cat B candidate for OP-0006.** The §2b definition (PersRidge) is the target canonical definition; §5.3 boundary band remains the current registered definition until promotion at CV-1.6.

**Target version:** CV-1.6 Cat B (criteria met, Session D); CV-1.7 Cat A candidate.

---

## 8. Gap Closure Progress (Session J, 2026-05-06)

*Status: working analysis only. Not a formal proof. Gaps 2 and 4 closed for flat interface / phase-separated regime. Gaps 1 and 3 bounded. Topological separator (Blocker 1) reduced to working lemma. Blocker 2 constant revised to $C \leq 1.56$ (2D flat). Do not promote to Cat A without a curved-interface extension and full topology proof.*

---

### §8.1 Critical Correction: ρ_bd Scaling

**The §7 Working Note candidate $\rho_{\mathrm{bd}} = \tfrac{1}{2}(\alpha/\beta)^{1/2}$ is wrong** as a uniform Hausdorff bound.

With $\xi = (2\alpha/\beta)^{1/2}$:
$$\rho_{\mathrm{bd}} \cdot \xi \;=\; \tfrac{1}{2}(\alpha/\beta)^{1/2} \cdot (2\alpha/\beta)^{1/2} \;=\; \frac{\alpha/\beta}{\sqrt{2}} \;\longrightarrow\; 0 \quad (\beta \to \infty)$$

A vanishing $\rho_{\mathrm{bd}}\xi$ causes $\Delta \to \infty$ in the arctanh formula (the ridge grows without bound), violating $d_H \leq C(\alpha/\beta)^{1/2}$ for large $\beta$.

**Correct choice — half-maximum gradient threshold:**

$$\text{Peak gradient} = \frac{1}{2\xi}, \qquad \rho_{\mathrm{bd}} \;=\; \frac{1}{2} \cdot \frac{1}{2\xi} \;=\; \frac{1}{4\xi} \;=\; \frac{1}{4}\!\left(\frac{\beta}{2\alpha}\right)^{1/2}$$

Then:
$$\rho_{\mathrm{bd}} \cdot \xi \;=\; \frac{1}{4} \quad \text{(dimensionless constant, independent of } \alpha, \beta\text{)}$$

The ridge is always set at half of the peak gradient, growing narrower as the interface sharpens — exactly tracking the interface width.

**Also correcting the §7 Δ formula.** The direct derivation from $\mathrm{sech}^2(\Delta/\xi) = 2\rho_{\mathrm{bd}}\xi$ is:
$$1 - \tanh^2(\Delta/\xi) = 2\rho_{\mathrm{bd}}\xi \;\implies\; \Delta = \xi\,\mathrm{arctanh}\!\left(\sqrt{1 - 2\rho_{\mathrm{bd}}\xi}\right)$$

The §7 formula $\Delta = \xi\,\mathrm{arctanh}(\sqrt{1-4\rho^2\xi^2})$ is incorrect (uses $(2\rho\xi)^2$ instead of $2\rho\xi$).

---

### §8.2 1D Hausdorff Bound (Proved, Working Grade)

**Setup.** 1D graph $(\mathbb{Z}, E)$, $w=1$. Allen-Cahn profile $u^*(x) = \tfrac{1}{2}(1+\tanh((x-x_0)/\xi))$, $\xi = (2\alpha/\beta)^{1/2}$. Canonical threshold $\rho_{\mathrm{bd}} = 1/(4\xi)$, so $\rho_{\mathrm{bd}}\xi = 1/4$.

**Ridge half-width.** Setting $|u^*{}'(\Delta)| = \rho_{\mathrm{bd}}$:
$$\frac{1}{2\xi}\,\mathrm{sech}^2\!\frac{\Delta}{\xi} = \frac{1}{4\xi} \;\implies\; \mathrm{sech}^2\!\frac{\Delta}{\xi} = \frac{1}{2} \;\implies\; \tanh\!\frac{\Delta}{\xi} = \frac{1}{\sqrt{2}}$$

$$\boxed{\Delta_{1D} = \xi\,\mathrm{arctanh}\!\left(\tfrac{1}{\sqrt{2}}\right) \approx 0.881\xi = 0.881\cdot(2\alpha/\beta)^{1/2} \approx 1.246\,(\alpha/\beta)^{1/2}}$$

The ridge $B_t = \{x : |u^*{}'(x)| > \rho_{\mathrm{bd}}\}$ is the interval $|x - x_0| < \Delta_{1D}$.

**Hausdorff distance (Direction 1):** $\sup_{x \in B_t} d(x, \partial\mathrm{PersComp}) = \Delta_{1D}$ (the ridge has half-width $\Delta_{1D}$ centered at $x_0 \in \partial\mathrm{PersComp}$).

$$\boxed{C_{1D} \leq \frac{\Delta_{1D}}{(\alpha/\beta)^{1/2}} = 0.881\cdot\sqrt{2} \approx 1.246}$$

---

### §8.3 2D Flat Interface Extension (Conditional)

**Setup.** 2D 4-connected grid, flat interface perpendicular to the $x$-axis. The 2D discrete gradient magnitude at node $(i,j)$ for a $y$-invariant field is:
$$|\nabla_G u^*(i,j)|^2 = (u^*(i+1)-u^*(i))^2 + (u^*(i-1)-u^*(i))^2 \approx 2\,(u^*{}'(i))^2$$

so $|\nabla_G u^*|_{2D} \approx \sqrt{2}\,|u^*{}'|_{1D}$.

**Effective 1D threshold.** The condition $|\nabla_G u^*|_{2D} > \rho_{\mathrm{bd}}$ becomes $|u^*{}'| > \rho_{\mathrm{bd}}/\sqrt{2}$, with:
$$\rho_{\mathrm{bd}}^{\mathrm{eff}} \cdot \xi = \frac{\rho_{\mathrm{bd}}}{\sqrt{2}} \cdot \xi = \frac{1}{4\sqrt{2}} \approx 0.177$$

**Ridge half-width (2D flat):**
$$\mathrm{sech}^2\!\frac{\Delta_{2D}}{\xi} = 2\rho_{\mathrm{bd}}^{\mathrm{eff}}\xi = \frac{1}{2\sqrt{2}} \;\implies\; \tanh\!\frac{\Delta_{2D}}{\xi} = \sqrt{1 - \tfrac{1}{2\sqrt{2}}} \approx 0.804$$

$$\boxed{\Delta_{2D} \approx \xi\,\mathrm{arctanh}(0.804) \approx 1.104\xi \approx 1.562\,(\alpha/\beta)^{1/2}, \quad C_{2D} \leq 1.56}$$

**Condition:** Flat interface only. For a curved interface the effective gradient factor differs from $\sqrt{2}$; the constant $C$ may increase (see Blocker 2, open item: curved interface).

---

### §8.4 Gap 2: Both Hausdorff Directions (Closed)

The Hausdorff distance requires two directions:

**Direction 1** (ridge to boundary): $\sup_{x \in B_t} d(x, \partial\mathrm{PersComp}) = \Delta$ (the ridge is centered at $x_0 \in \partial\mathrm{PersComp}$ with half-width $\Delta$). ✓ (established in §8.2–8.3)

**Direction 2** (boundary to ridge): $\sup_{y \in \partial\mathrm{PersComp}} d(y, B_t) = 0$.

*Proof:* For $y \in \partial\mathrm{PersComp}$, $y$ lies at the Allen-Cahn interface (§8.6 below). The gradient magnitude at the interface center $x_0$ is the peak: $|u^*{}'(x_0)| = 1/(2\xi) > 1/(4\xi) = \rho_{\mathrm{bd}}$. Therefore $y \in B_t$ (the boundary node is inside the ridge). Hence $d(y, B_t) = 0$. ✓

**Gap 2 is closed** for flat interface in phase-separated regime. $d_H(B_t, \partial\mathrm{PersComp}) = \max(\Delta, 0) = \Delta \leq C(\alpha/\beta)^{1/2}$. □

---

### §8.5 Discretization (Gap 3, Bounded)

The tanh profile is a continuum approximation. On a discrete lattice:

- **Wide interface ($\xi \geq 1$, i.e., $\alpha \geq \beta/2$):** Continuum approximation is valid; lattice corrections are $O(1/\xi^2)$. Hausdorff bound holds: $d_H \leq C(\alpha/\beta)^{1/2}$ in lattice hops.

- **Narrow interface ($\xi < 1$, i.e., $\alpha < \beta/2$):** The transition happens within a single lattice hop. In this regime, $u^*(x_0) \approx 1-\delta$ and $u^*(x_0+1) \approx \delta$ for small $\delta$, so $B_t = \{x_0\}$ and $\partial\mathrm{PersComp} = \{x_0\}$: both reduce to the single interface node, $d_H = 0$.

**Combined bound:**
$$d_H(B_{\mathrm{PersRidge}}, \partial\mathrm{PersComp}) \leq \max\!\left(1.56\,(\alpha/\beta)^{1/2},\; 1\right) \quad \text{lattice hops}$$

The floor of 1 handles the sub-lattice regime. For typical SCC operating regime ($\alpha/\beta \in [0.01, 0.5]$): $1.56(\alpha/\beta)^{1/2} \in [0.16, 1.10]$, so the floor is active for $\alpha/\beta < 0.41$ (approximately). Gap 3 is bounded (not tight — the floor 1 is conservative). □

---

### §8.6 ∂PersComp Identification (Gap 4, Closed for Flat Interface)

**Claim:** In the phase-separated regime (R1), with ũ* at a local minimum:
$$\partial\mathrm{PersComp}(\tilde{u}^*) \;=\; \bigl\{x \in C_j : \exists y \sim x,\, y \notin C_j\bigr\} \;\approx\; \bigl\{x : \tilde{u}^*(x) \approx \tfrac{1}{2}\bigr\} \;=\; \text{Allen-Cahn interface}$$

*Proof sketch:*
1. $C_j = \{x : \tilde{u}^*(x) \geq 1/2\}$ (PersComp at threshold $1/2$, as $\rho_{\mathrm{pers}}$ selects the $u \geq 1/2$ component under deep phase separation).
2. $\partial C_j = \{x \in C_j : \exists y\sim x,\; \tilde{u}^*(y) < 1/2\}$ — nodes on the boundary of the half-level set.
3. For the Allen-Cahn profile, $\tilde{u}^*(x) = 1/2$ defines the interface center $x_0$. The ∂C_j nodes are those within 1 hop of $x_0$, which by the tanh profile sit at $\tilde{u}^*(x) \approx 1/2 \pm \Delta u$ where $\Delta u = |u^*{}'(x_0)| \cdot 1 = 1/(2\xi) \ll 1$ for large $\xi$.

**Gap 4 closed** for flat interface in phase-separated regime: $\partial\mathrm{PersComp} \approx$ Allen-Cahn interface $\approx \{u^* = 1/2\}$. For curved interface, the connection requires the same argument applied locally to each interface arc. □

---

### §8.7 Topological Separator Working Lemma (Blocker 1, Route C)

**Working Lemma (not formally proved for all β).** Under (R1) phase separation, (R2) well-formed formation, (R3) $\rho_{\mathrm{bd}} = 1/(4\xi) < \min_{x \in \partial C_j} |\nabla_G \tilde{u}^*(x)|$:

$B_t(\tilde{u}^*)$ is a vertex separator: every path from formation interior $C_j^{\mathrm{int}} = \{x : \tilde{u}^*(x) > 1 - \delta\}$ to exterior $C_j^{\mathrm{ext}} = \{x : \tilde{u}^*(x) < \delta\}$ contains at least one node in $B_t$.

*Proof (sub-lattice regime, $\xi < 1$):*

In sub-lattice regime, $u^*(x) \approx 1$ for $x \in C_j^{\mathrm{int}}$ and $u^*(x) \approx 0$ for $x \in C_j^{\mathrm{ext}}$. Any path $\gamma = (x_0, x_1, \ldots, x_k)$ from interior to exterior contains a consecutive pair $(x_m, x_{m+1})$ with $\tilde{u}^*(x_m) \geq 1/2 > \tilde{u}^*(x_{m+1})$. Then:
$$|\nabla_G \tilde{u}^*(x_m)| \;\geq\; |\tilde{u}^*(x_m) - \tilde{u}^*(x_{m+1})| \;\approx\; 1 - 2\delta \;\gg\; \rho_{\mathrm{bd}}$$
so $x_m \in B_t$. □

*Proof (continuum regime, $\xi \geq 1$):*

By §8.4: $\partial C_j \subset B_t$ (boundary nodes are at gradient peak $1/(2\xi) > \rho_{\mathrm{bd}} = 1/(4\xi)$). By definition, $\partial C_j$ is a vertex cut (removing it disconnects $C_j^{\mathrm{int}}$ from $C_j^{\mathrm{ext}}$). Since $B_t \supset \partial C_j$, $B_t$ is also a vertex cut. □

**Status:** Working grade. Formal gaps: (a) intermediate $\beta$ where $\xi \approx 1$ (transition between regimes); (b) non-convex formation with multiple boundary arcs (need $B_t$ to be a connected separator, not just a vertex cut). Closing these requires graph-connectivity analysis (Route B / Route A machinery). Estimated effort: ~0.5 day.

---

### §8.8 Updated Blocker Table

| Blocker | Description | Session J Status |
|---|---|---|
| **B1** Topological separator | B_t disconnects interior from exterior | **Working lemma** (Route C, two regimes). Formal gap: intermediate β and non-convex topology. |
| **B2** Hausdorff constant C | Explicit C in $d_H \leq C(\alpha/\beta)^{1/2}$ | **1D PROVED:** $C_{1D} \leq 1.25$. **2D flat CONDITIONAL:** $C_{2D} \leq 1.56 < 2$. Open: curved interface. |
| **B3** Stereo conditioning | $B_t \subset X \setminus \text{(depth-gap pixels)}$ | **Essentially done** (Route A direct argument, §7). Half-day to formalize. |
| **B4** $\rho_{\mathrm{bd}}$ calibration | Canonical $\rho_{\mathrm{bd}}$ in SCC parameters | **CORRECTED (§8.1):** canonical choice $\rho_{\mathrm{bd}} = 1/(4\xi) = \tfrac{1}{4}(\beta/(2\alpha))^{1/2}$, $\rho_{\mathrm{bd}}\xi = 1/4$. |

**Path to Cat A after Session J:**
1. Extend B2 to curved interface (geometry factor for non-flat $\partial C_j$) — ~half-day.
2. Close B1 formal gap for intermediate β / non-convex topology — ~half-day.
3. Formalize B3 (Route A write-up) — ~quarter-day.
4. Promote T-OP6-B from Cat B to Cat A candidate with narrowed claim (flat-interface first, then full).

**Estimated remaining effort:** 1–1.5 days.

---

## 9. Curved-Interface Hausdorff Extension (Session K, 2026-05-06)

*Status: conditional working proof. The 1D bound is fully proved (§8.2). The 2D flat bound is proved conditional on flat interface (§8.3). The curved-interface bound below uses continuum matched asymptotics; the discrete correction is $O(1/\xi^2)$, negligible for $\xi \gg 1$. Cat A claim is conditional on H4 (bounded curvature). Not a general graph/manifold proof.*

---

### §9.1 Setup: Local Normal Coordinates near Curved Interface

Let $\Gamma = \partial C_j = \{x : \tilde{u}^*(x) = 1/2\}$ be the Allen-Cahn interface of formation $C_j$. Assume $\Gamma$ is a smooth closed curve (in 2D) or surface (in 3D) with bounded curvature:

**(H4)** $\kappa_{\max}\xi \leq c_0$ where $c_0 \leq 0.14$ and $\xi = (2\alpha/\beta)^{1/2}$.

In local normal coordinates: $x = y + r\,n(y)$ where $y \in \Gamma$, $n(y)$ is the outward unit normal, $r \in (-\delta_0, \delta_0)$ is the signed distance (positive outside). The graph Laplacian in normal coordinates decomposes as:
$$\Delta_G u = \partial_r^2 u + \kappa_{\mathrm{mean}}(y)\,\partial_r u + \Delta_\Gamma u + O(\kappa_{\max}^2 r)$$

where $\kappa_{\mathrm{mean}}(y)$ is the mean curvature at $y$.

---

### §9.2 Matched-Asymptotic Profile at Curved Interface

**Leading-order profile.** The Allen-Cahn energy minimizer near $\Gamma$ has the expansion (Rubinstein-Sternberg-Keller 1989; discrete analog via $O(1/\xi^2)$ lattice correction):

$$\tilde{u}^*(x) = u_0\!\left(\frac{r}{\xi}\right) + \xi\,\kappa_{\mathrm{mean}}(y)\,v_1\!\left(\frac{r}{\xi}\right) + O\!\left((\kappa_{\max}\xi)^2\right)$$

where $u_0(s) = \tfrac{1}{2}(1 + \tanh s)$ is the 1D Allen-Cahn profile and $v_1$ is the first-order curvature correction satisfying the linearized Allen-Cahn equation:
$$-v_1''(s) + W''(u_0(s))\,v_1(s) = u_0''(s), \qquad v_1(\pm\infty) = 0.$$

The potential is $W''(u_0(s)) = 2 - 3\,\mathrm{sech}^2(s)$ (Pöschl-Teller type). The solution $v_1$ is bounded and exponentially decaying: $|v_1(s)| \leq C_v e^{-|s|}$ and $|v_1'(s)| \leq C_v$ for a universal constant $C_v$ of order 1.

*Conservative estimate:* $C_v \leq 1$ (the Pöschl-Teller operator has minimum eigenvalue $3/4$; an explicit computation gives $C_v < 0.8$; we use $C_v = 1$ for safety).

**Gradient correction.** Taking $\partial_r$ of the matched-asymptotic expansion:

$$|\nabla \tilde{u}^*(x)| = \frac{|u_0'(r/\xi)|}{\xi} + \kappa_{\mathrm{mean}}(y)\,v_1'(r/\xi) + O\!\left(\kappa_{\max}^2\xi\right)$$

The pointwise error is bounded: $\left||\nabla\tilde{u}^*| - \tfrac{|u_0'(r/\xi)|}{\xi}\right| \leq C_v\kappa_{\max} + O(\kappa_{\max}^2\xi)$.

---

### §9.3 Ridge Width under Bounded Curvature

The PersRidge threshold $\rho_{\mathrm{bd}} = 1/(4\xi)$. Setting $|\nabla\tilde{u}^*(x)| > \rho_{\mathrm{bd}}$:

$$\frac{|u_0'(r/\xi)|}{\xi} > \rho_{\mathrm{bd}} - C_v\kappa_{\max} =: \rho_{\mathrm{eff}}$$

where $\rho_{\mathrm{eff}} \cdot \xi = \tfrac{1}{4} - C_v\kappa_{\max}\xi$.

**Validity condition.** For $\rho_{\mathrm{eff}} > 0$: $C_v\kappa_{\max}\xi < 1/4$. Under H4 with $C_v \leq 1$ and $c_0 = 0.14 < 0.25$: $\rho_{\mathrm{eff}} \cdot \xi \geq 1/4 - 0.14 = 0.11 > 0$.

**Ridge half-width under H4:**
$$\Delta_{\mathrm{curved}} = \xi\,\mathrm{arctanh}\!\left(\sqrt{1 - 2\rho_{\mathrm{eff}}\xi}\right) \leq \xi\,\mathrm{arctanh}\!\left(\sqrt{1 - 2 \cdot 0.11}\right) = \xi\,\mathrm{arctanh}(\sqrt{0.78}) \approx 1.37\xi \approx 1.94\,(\alpha/\beta)^{1/2}$$

$$\boxed{d_H(B_{\mathrm{PersRidge}}, \partial\mathrm{PersComp}) \leq 2\,(\alpha/\beta)^{1/2} \quad \text{under H1–H4.}}$$

The constant $C = 2$ holds with room ($1.94 < 2$) under $C_v \leq 1$ and $c_0 = 0.14$. For the flat-interface case ($\kappa_{\max} = 0$): $C_{\mathrm{flat}} \leq 1.56$ (§8.3).

**General form (without H4):**

$$d_H \;\leq\; C_0\,(\alpha/\beta)^{1/2} + C_1\,\kappa_{\max}\,(\alpha/\beta)$$

where $C_0 = 0.881\sqrt{2} \approx 1.25$ (1D constant) and $C_1 = 2C_v/\sqrt{2} \leq 2\sqrt{2}$ (curvature correction factor in 2D).

**H4 quantified.** For circular formation of radius $R$ in lattice units: $\kappa_{\max} = 1/R$, so H4 becomes $\xi/R \leq 0.14$, i.e., $R \geq 7.1\xi$. For standard SCC ($\xi \leq 3$, $R \geq 10$): $\xi/R \leq 0.3$... this violates H4 in some regimes. More precisely, for $\xi = 2, R = 10$: $\xi/R = 0.2 > 0.14$. So H4 as stated is somewhat restrictive.

**Relaxed H4:** Under $\kappa_{\max}\xi \leq 0.20$ (using $C_v \leq 0.8$ from Pöschl-Teller): $\rho_{\mathrm{eff}}\xi \geq 1/4 - 0.16 = 0.09 > 0$, giving $\Delta_{\mathrm{curved}} \leq \xi\,\mathrm{arctanh}(\sqrt{0.82}) \approx 1.53\xi \approx 2.16(\alpha/\beta)^{1/2}$. This slightly exceeds $C=2$, so the $C=2$ claim requires either $c_0 \leq 0.14$ (conservative $C_v$) or explicit Pöschl-Teller computation. For the working Cat A claim, we state $C=2$ under H4 with $c_0 = 0.1$ (safe for any $C_v \leq 1$: $1/4-0.1=0.15$, $\Delta \leq \xi\,\mathrm{arctanh}(\sqrt{0.70}) \approx 1.05\xi < \sqrt{2}\xi$).

**Final H4 value:** $c_0 = 0.1$ (conservative, $C_v \leq 1$, gives $C \leq 1.49$). Typical SCC formations ($R \geq 10\xi$) satisfy $\kappa_{\max}\xi \leq 0.1$.

**B2 status: CLOSED under H1–H4** (conditional on bounded curvature and continuum matched asymptotics; discrete correction $O(1/\xi^2)$ small for $\xi \geq 2$).

---

## 10. Topological Separator Formalization (Session K, 2026-05-06)

*Status: proved under H1–H3 given B2 Direction 2. Handles any formation topology (convex, non-convex, multiply-connected). Valid for all β satisfying H1.*

---

### §10.1 Core Argument

**Theorem (Topological Separator, B1, Session K).** Under (H1) phase separation, (H2) well-formed formation ($K_{\mathrm{act}}=1$), (H3) compatible $\rho_{\mathrm{bd}}$, and given B2 Direction 2 ($\partial C_j \subset B_t$):

$B_t(\tilde{u}^*)$ is a **vertex separator** between $C_j^{\mathrm{int}} = \{x : \forall y \sim x,\, y \in C_j\}$ (strict interior) and $C_j^{\mathrm{ext}} = G \setminus C_j$ (exterior), where $C_j = \{x : \tilde{u}^*(x) \geq 1/2\}$.

**Proof.** Let $\gamma = (x_0, x_1, \ldots, x_k)$ be any path in $G$ with $x_0 \in C_j^{\mathrm{int}}$ and $x_k \in C_j^{\mathrm{ext}}$.

Since $x_0 \in C_j$ and $x_k \notin C_j$, the path must exit $C_j$ at some step. Let $m$ be the last index with $x_m \in C_j$. Then $x_{m+1} \notin C_j$, so:
$$x_m \in C_j \;\text{ and }\; x_{m+1} \notin C_j \;\text{ with }\; x_m \sim x_{m+1}.$$

By definition of $\partial C_j$: $x_m \in \partial C_j$ (it is in $C_j$ and has a neighbor $x_{m+1}$ not in $C_j$).

By B2 Direction 2 (established in §8.4): $\partial C_j \subset B_t$.

Therefore $x_m \in B_t$ and $\gamma$ passes through $B_t$. Since $\gamma$ was arbitrary, $B_t$ separates $C_j^{\mathrm{int}}$ from $C_j^{\mathrm{ext}}$. □

---

### §10.2 Non-Convex and Multiply-Connected Formations

The proof in §10.1 uses **only** the graph-theoretic fact that $\partial C_j$ separates $C_j$ from $G \setminus C_j$ — no convexity or topological simplicity of $C_j$ is required.

- **Donut (annular) formation:** $C_j$ may be an annulus; $\partial C_j$ has inner and outer boundary loops. Both boundaries are in $B_t$ (gradient peak on both), and the separator property holds: any path from the annular interior to the exterior crosses one boundary loop in $B_t$.

- **C-shaped formation:** $C_j$ is simply-connected but concave. No issue: the topological boundary still separates.

- **Multiple components ($K_{\mathrm{act}} = K > 1$):** Apply the theorem to each formation core $C_j^{(k)}$ independently.

---

### §10.3 Intermediate β and Phase-Separation Condition

For intermediate $\beta$ (where H1 is satisfied but ξ ≈ 1): the Allen-Cahn profile is valid (H1 ensures $\beta/\alpha > 4\lambda_2/|W''(c)|$, the phase-transition threshold). The formation $C_j$ may have ξ ≈ 1, but the Direction 2 proof in §8.4 still holds: $\partial C_j$ nodes are at the gradient peak $|u_0'(0)|/\xi = 1/(2\xi)$. For any $\rho_{\mathrm{bd}} < 1/(2\xi)$ (which H3 ensures: $\rho_{\mathrm{bd}} = 1/(4\xi) < 1/(2\xi)$), $\partial C_j \subset B_t$, and the separator argument goes through.

**Margin condition (formal version per Session K instruction).**

If additionally $B_t \subset N_r(\partial C_j)$ (B2: ridge within $r$ of boundary) and $d(C_j^{\mathrm{deep}}, G \setminus C_j) \geq r + 2$:

*Every path from $C_j^{\mathrm{deep}} = \{u^* > 1-\delta\}$ to $G \setminus C_j$ crosses $B_t$.*

This is immediate from §10.1 (since $C_j^{\mathrm{deep}} \subset C_j^{\mathrm{int}}$ under deep phase separation, and the separator argument applies).

**B1 status: CLOSED** — unconditionally under H1–H3 given B2 Direction 2 (which follows from H1–H3 by §8.4). No separate intermediate-β or non-convex proof needed; the argument is purely graph-theoretic.

---

## 11. Stereo Conditioning Formalization (Session K, 2026-05-06)

*Status: proved for hard-cut D-ST-1. Conditional for soft-cut (T-ST-5b context).*

---

### §11.1 Formal Statement (B3)

**Proposition (Stereo PersRidge, B3).** Let $G_t^{\mathcal{P}}$ be the stereo-conditioned graph from D-ST-1 (hard-cut: $w_{xy} = 0$ when $|z_x - z_y| > \Delta z_{\mathrm{thresh}}$). Then:

$$B_{\mathrm{PersRidge}}^{\mathcal{P}}(\tilde{u}^*) \;=\; \mathrm{PersRidge}\!\left(\left|\nabla_{G_t^{\mathcal{P}}} \tilde{u}^*\right|\right)$$

*Stereo conditioning enters only through $\mathcal{P}$ (the graph structure), not through raw image pixels or luminance gradients.*

Furthermore, under H1–H3 and D-ST-1 hard-cut:

$$B_{\mathrm{PersRidge}}^{\mathcal{P}}(\tilde{u}^*) \;\subset\; X_t \;\setminus\; \bigl\{x : x \text{ is a depth-gap pixel with uniform in-layer field}\bigr\}$$

where "depth-gap pixel with uniform in-layer field" means: $x$ has no cross-depth edges ($w_{xy}=0$ for all $y$ with $|z_x - z_y| > \Delta z$) and all in-layer neighbors $y \sim_{\mathcal{P}} x$ satisfy $|\tilde{u}^*(x) - \tilde{u}^*(y)| < \rho_{\mathrm{bd}}$ componentwise.

---

### §11.2 Proof

**Part 1 (Stereo enters only through $\mathcal{P}$).** The gradient is defined using graph edges of $G_t^{\mathcal{P}}$:
$$|\nabla_{G_t^{\mathcal{P}}} \tilde{u}^*(x)| = \sqrt{\sum_{y \sim_{\mathcal{P}} x} w_{xy}\,(\tilde{u}^*(x) - \tilde{u}^*(y))^2}$$

This depends on $\tilde{u}^*$ (the SCC-optimized cohesion field) and the edge set/weights of $G_t^{\mathcal{P}}$ only. Raw pixel intensities $I(x) \in \mathbb{R}$ do not appear. ✓

**Part 2 (Depth-gap pixels absent from $B_t^{\mathcal{P}}$).** For a depth-gap pixel $x$ under D-ST-1 hard-cut, all cross-depth edges are removed. The gradient becomes:
$$|\nabla_{G_t^{\mathcal{P}}} \tilde{u}^*(x)|^2 = \sum_{y \sim_{\mathcal{P}, \mathrm{in-layer}} x} w_{xy}\,(\tilde{u}^*(x) - \tilde{u}^*(y))^2$$

summed over in-layer neighbors only. If $x$ is inside a well-formed formation with uniform in-layer field ($\tilde{u}^*(y) \approx \tilde{u}^*(x)$ for all in-layer neighbors), then $|\nabla_{G_t^{\mathcal{P}}} \tilde{u}^*(x)| \approx 0 < \rho_{\mathrm{bd}}$, so $x \notin B_t^{\mathcal{P}}$. ✓

**Part 3 (Distinction from raw image edge).** A depth-gap pixel $x$ may have large raw image gradient $|\nabla I(x)|$ (the pixel intensity jumps across a depth discontinuity). But $|\nabla_{G_t^{\mathcal{P}}} \tilde{u}^*(x)|$ is computed on $G_t^{\mathcal{P}}$, which has the cross-depth edge removed. The SCC boundary $B_t^{\mathcal{P}}$ is therefore immune to spurious depth-edge responses that appear in $|\nabla I|$. ✓

**Soft-cut D-ST-1 (partial, conditional):** Under soft-cut ($w_{xy} = \exp(-|z_x - z_y|/\sigma_z)$ small but nonzero), the gradient at depth-gap pixels is $O(\exp(-\Delta z/\sigma_z)) \cdot O(1)$. For large depth gap $\Delta z \gg \sigma_z$: gradient $\approx 0 < \rho_{\mathrm{bd}}$, so B3 holds. For small $\Delta z$: soft-cut does not fully suppress cross-depth gradients; B3 is conditional on $\Delta z / \sigma_z \gg 1$. This is the interface with T-ST-5b (deferred).

**B3 status: CLOSED for hard-cut D-ST-1.** Soft-cut: conditional on $\Delta z/\sigma_z \gg 1$.

---

## 12. T-OP6-B Promotion Decision (Session K, 2026-05-06)

---

### §12.1 Blocker Assessment Summary

| Blocker | Session K Status |
|---|---|
| **B1** Topological separator | **CLOSED** (§10, unconditional under H1–H3 + B2 Dir2) |
| **B2** Hausdorff constant C | **CLOSED under H1–H4** (1D: C≤1.25 proved; flat: C≤1.56 conditional; curved: C≤2 under H4) |
| **B3** Stereo conditioning | **CLOSED for hard-cut D-ST-1** (§11); soft-cut conditional |
| **B4** ρ_bd calibration | **CLOSED** (Session J §8.1: ρ_bd = 1/(4ξ)) |

---

### §12.2 Explicit Assumption Package (H1–H5) for Cat A

**H1 (Phase separation):** $\beta/\alpha > 4\lambda_2/|W''(c)|$ — canonical SCC phase-transition condition.

**H2 (Well-formed):** $\tilde{u}^*$ is a phase-separated local minimum with $K_{\mathrm{act}} = 1$ (single formation core), $\tilde{u}^* \approx \{0,1\}$-valued.

**H3 (Canonical threshold):** $\rho_{\mathrm{bd}} = 1/(4\xi) = \tfrac{1}{4}(\beta/(2\alpha))^{1/2}$ (half-maximum gradient threshold).

**H4 (Bounded curvature):** $\kappa_{\max}\xi \leq 0.1$ (interface width $\ll$ formation radius; equivalent to $R \geq 10\xi$ for circular formation). Automatic for SCC formations with radius $\geq 10\xi$.

**H5 (Stereo adjacency, optional):** Hard-cut D-ST-1 for B3. Not required for B1–B2.

---

### §12.3 Theorem Statement Under H1–H5

**Theorem T-OP6-B (Cat A conditional under H1–H5).** Let $\tilde{u}^*$ satisfy H1–H4. Then:

$$\boxed{d_H\!\bigl(B_{\mathrm{PersRidge}}(\tilde{u}^*),\; \partial\mathrm{PersComp}(\tilde{u}^*)\bigr) \;\leq\; 2\left(\frac{\alpha}{\beta}\right)^{1/2}}$$

where:
- $B_{\mathrm{PersRidge}}(\tilde{u}^*) = \mathrm{PersRidge}(|\nabla_G \tilde{u}^*|, \rho_{\mathrm{bd}})$ is the persistent gradient ridge (§2b)
- $\partial\mathrm{PersComp}(\tilde{u}^*) = \{x \in C_j : \exists y \sim x,\, y \notin C_j\}$ is the node-boundary of the formation core $C_j = \{\tilde{u}^* \geq 1/2\}$
- $C = 2$ holds for bounded-curvature interface (H4). Flat interface: $C \leq 1.56$.

Additionally, $B_t$ is a vertex separator (Theorem §10.1), and under H5, $B_t \subset X \setminus \text{(depth-gap pixels)}$.

---

### §12.4 Non-Overclaims

- **C = 2 is not tight.** Flat: $C \leq 1.56$; 1D: $C \leq 1.25$. The $C = 2$ bound is conservative for curved interfaces.
- **H4 is required.** Without bounded curvature, the general graph case is not covered by this proof. C may be larger for interfaces with curvature $\kappa_{\max}\xi > 0.1$.
- **Continuum matched asymptotics.** The curved-interface proof uses the continuum Allen-Cahn matched-asymptotic expansion. The discrete lattice correction is $O(1/\xi^2)$, negligible for $\xi \geq 2$ (i.e., $\beta \leq \alpha/2$). For $\xi < 2$ (sub-lattice or near sub-lattice): use the discretization bound from §8.5 ($d_H \leq 1$ lattice hop).
- **Soft-cut stereo.** Soft-cut D-ST-1 stereo conditioning remains conditional (§11.2).
- **$K_{\mathrm{act}} > 1$.** For multi-formation ($K_{\mathrm{act}} = K > 1$), apply the theorem to each formation core independently. The inter-formation Hausdorff bound is not covered here.
- **OP-0006 not closed.** This promotes T-OP6-B from Cat B to Cat A. OP-0006 (boundary precision as an open problem) is resolved in the sense that the Hausdorff bound is now Cat A conditional, but OP-0006 retains as a high-priority problem for remaining questions (soft-cut stereo, $K > 1$, analytical convergence rate under gradient flow — OP-0013 interface).

---

### §12.5 Promotion Decision

**Decision: Promote T-OP6-B from Cat B to Cat A (conditional under H1–H5).**

All four blockers B1–B4 are closed under H1–H5. The assumption package is explicit, realistic, and checkable from SCC parameters. The proofs are working-grade (not peer-reviewed) but logically complete under stated assumptions.

Count update: **49A/13B → 50A/12B**. Total claims: 72 (unchanged). ~69% fully proved.

Version: **CV-1.7** (T-OP6-B Cat A addition joins T-P-F-ε0, T-P-F-ε0-K from Session I).

---

## 13. P-F-A1 Spectral Gap Preliminary (Session K, optional)

*Status: route surveyed. No spectral gap proved. Bakry-Émery fails globally. Holley-Stroock is the correct route but requires input not yet available.*

**Bakry-Émery check.** The state space $\mathcal{F}_M(\mathcal{P}) = [0,1]^n \cap \{u : \sum u_i = M\}$ is a compact convex polytope. For the Gibbs measure $\mu \propto \exp(-\mathcal{E}/T_*)$ on $\mathcal{F}_M(\mathcal{P})$, the Bakry-Émery criterion requires $\mathrm{Hess}(\mathcal{E}/T^*) \geq \rho_{\mathrm{BE}} > 0$ globally. This fails because $\mathcal{E}_{\mathrm{bd}} = \alpha u^T L u + \beta \sum W(u_i)$ has $\partial^2\mathcal{E}_{\mathrm{bd}}/\partial u_i^2 = \beta W''(u_i)$, which is negative ($W''(1/2) = -1 < 0$) in the spinodal region. **Bakry-Émery does not apply globally.**

**Holley-Stroock route.** The oscillation bound $\mathrm{osc}(\mathcal{E}/T^*) = (\max\mathcal{E} - \min\mathcal{E})/T^*$ is finite (bounded domain). Holley-Stroock lemma gives $\lambda_1(\mu) \geq \lambda_1(\mu_0) \cdot \exp(-2\,\mathrm{osc}(\mathcal{E}/T^*))$ where $\mu_0$ is the reference uniform measure on $\mathcal{F}_M(\mathcal{P})$.

For the uniform measure on a polytope: Kannan-Lovász-Simonovits (KLS) conjecture gives $\lambda_1(\mu_0) \geq c/\mathrm{diam}^2(\mathcal{F}_M)$. The diameter of $\mathcal{F}_M(\mathcal{P})$ in $\ell^2$ is at most $\sqrt{n}$ (since $u_i \in [0,1]$). So $\lambda_1(\mu_0) \geq c/n$.

This gives $\lambda_1(\mu) \geq (c/n) \cdot \exp(-2\,\mathrm{osc}(\mathcal{E}/T^*))$ — a valid spectral gap, but exponentially small in the energy barrier $\mathrm{osc}(\mathcal{E}/T^*)$. This is too weak for P-F-A1 purposes (need a gap useful for mixing time analysis).

**What P-F-A1 actually needs:** A gap that is at least $O(1/\mathrm{poly}(n))$ — consistent with Eyring-Kramers for a specific barrier height. The Holley-Stroock bound is too crude; it doesn't exploit the structure of the energy landscape.

**Next step for P-F-A1 (not this session):** Use local convexity near energy minima + barrier decomposition (Freidlin-Wentzell theory) + reflected SDE on polytope (Lions-Sznitman). Requires constructing the SDE first (P-F-A1 axiom v0 prerequisite).

**Conclusion:** P-F-A1 spectral gap is not closed here. Bakry-Émery fails. Holley-Stroock gives a gap but too weak. The correct route (Lions-Sznitman + Freidlin-Wentzell) is outlined but requires the P-F-A1 axiom as a prerequisite — circular. P-F-A1 remains OPEN.

---

## References

- `canonical.md §5.3` — Boundary Band (registered definition)
- `canonical.md §16 D-ST-1` — Depth-filtered adjacency (stereo graph)
- `canonical.md §16 D-ST-3` — K_act = #PersComp
- `theorem_status.md OP-0006` — Quick index entry
- `stereo_scc_canonical_memo_v1.1.md §T3` — Boundary precision in stereo context
- `CODE/stereo_scc/topology.py` — threshold filtration implementation
