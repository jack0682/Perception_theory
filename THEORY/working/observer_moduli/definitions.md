---
type: working/definitions
created: 2026-05-07
project: Observer Moduli Space of SCC
version: 0.7
---

> [!nav] Linked: [[MOC_observer_moduli_OMS]] · [[THEORY_INDEX]]


# Formal Definitions — SCC Observer Moduli Space

Each entry is classified as: **Defined** | **Assumed** | **Hypothesized** | **Open** | **Rejected**

---

## Part I: Observer Parameter Space

### DEF-1. SCC Energy Parameters [Defined]

The SCC energy functional on $\Sigma_m = \{u \in [0,1]^n : \sum_i u_i = m\}$ is:

$$E(u) = \lambda_{cl} E_{cl}(u) + \lambda_{sep} E_{sep}(u) + \lambda_{bd} E_{bd}(u) + \lambda_{tr} E_{tr}(u)$$

The named scalar parameters appearing in $E$ are:

| Parameter | Symbol | Role | Controlled by |
|-----------|--------|------|---------------|
| Boundary smoothness | $\alpha > 0$ | $E_{bd} = 2\alpha \cdot u^\top L u$ | Observer |
| Separation strength | $\beta > 0$ | $E_{sep}$ | Observer |
| Closure gain | $a_{cl} \in (0,4)$ | $E_{cl}$; axiom A3 requires $a_{cl} < 4$ | Observer |
| Distinction bias | $b_D = 0$ | Fixed; required for Łojasiewicz analyticity | Fixed |
| OT regularization | $\varepsilon_{OT} > 0$ | Sinkhorn transport | Observer |
| Core threshold | $\theta_{core} \in (0,1)$ | Reading formation core from $u^*$ | Diagnostic |
| Interior threshold | $\theta_{in} \in (0,1)$ | Reading interior from $u^*$ | Diagnostic |
| Mass | $m \in (0, n)$ | $\sum_i u_i = m$ | Scene-determined |

**Note:** $b_D = 0$ is always fixed. $m$ is scene-determined. The scale of $(\alpha, \beta)$ is gauge-redundant; only the ratio $q = \beta/\alpha$ is physically relevant.

---

### DEF-2. Observer Parameter Vector $\Theta$ [Defined]

$$\Theta = (q,\ \lambda,\ \xi)$$

**Component 1: Phase-transition ratio**
$$q = \frac{\beta}{\alpha} \in [q_{\min}, q_{\max}] \subset \mathbb{R}_{>0}$$

where $q_{\min} > 0$ and $q_{\max} < \infty$ are physical bounds. The scale of $(\alpha, \beta)$ is gauge-fixed by normalization $\alpha + \beta = 1$ (equivalently, $\alpha = 1/(1+q)$, $\beta = q/(1+q)$).

**Component 2: Energy weight vector**
$$\lambda = (\lambda_{cl}, \lambda_{sep}, \lambda_{bd}, \lambda_{tr}) \in \Delta^3$$

where the 3-simplex is:
$$\Delta^3 = \left\{(\lambda_1,\lambda_2,\lambda_3,\lambda_4) \in \mathbb{R}^4 :\ \lambda_i \geq 0,\ \sum_{i=1}^4 \lambda_i = 1\right\}$$

The four weights have distinct semantic roles:
- $\lambda_{cl}$: closure / self-support weight
- $\lambda_{sep}$: separation / contrast weight
- $\lambda_{bd}$: boundary / morphology weight
- $\lambda_{tr}$: transport / temporal continuity weight

These roles are **not interchangeable**; permutation symmetry $S_4$ on $\lambda$ is NOT assumed as gauge (see DEF-8).

**Component 3: Remaining hyperparameters**
$$\xi = (a_{cl},\ \varepsilon_{OT},\ \theta_{core},\ \theta_{in}) \in B_\xi$$

where the box domain is:
$$B_\xi = (0, 4) \times (0, \varepsilon_{\max}] \times (0,1) \times (0,1) \subset \mathbb{R}^4$$

**Extended $\xi$** (for future extension, not yet in minimal model):
$$\xi_{\text{ext}} = (a_{cl},\ \varepsilon_{OT},\ \theta_{core},\ \theta_{in},\ \sigma_K,\ \tau_{\text{persist}},\ \ldots)$$

where $\sigma_K$ is Sinkhorn iteration count and $\tau_{\text{persist}}$ is persistence threshold.

---

### DEF-3. Raw Observer Space $\mathcal{M}_{\text{raw}}$ [Defined]

$$\mathcal{M}_{\text{raw}} = \mathbb{R}_{>0}^2 \times \Delta^3 \times B_\xi$$

where $\mathbb{R}_{>0}^2$ contains $(\alpha, \beta)$ before gauge-fixing.

**Gauge redundancy:** $(\alpha, \beta) \mapsto (r\alpha, r\beta)$ for $r \in \mathbb{R}_{>0}$ leaves $q = \beta/\alpha$ unchanged and is physically undetectable. The group $\mathbb{R}_{>0}$ is **non-compact**; it is removed by gauge-fixing, not by compact group quotient.

**Gauge-fixing:** Set $\alpha + \beta = 1$, reducing $\mathbb{R}_{>0}^2$ to the arc $\{(\alpha, \beta) : \alpha + \beta = 1, \alpha > 0, \beta > 0\} \cong (0,1)$, parametrized by $q = \beta/\alpha \in (0,\infty)$.

**Rejected candidate:** $(\alpha, \beta) \mapsto (e^{i\phi}\alpha, e^{i\phi}\beta)$ with $\phi \in [0, 2\pi)$ is a $U(1)$ action, but it takes real positive $(\alpha, \beta)$ out of $\mathbb{R}_{>0}^2$. Not valid for the current real-positive SCC parameter scheme. [Rejected — see audit_log.md AUD-001]

---

### DEF-4. Observer Space $\mathcal{M}_{\text{obs}}$ [Defined]

After gauge-fixing the $(\alpha,\beta)$ scale redundancy and bounding $q$:

$$\mathcal{M}_{\text{obs}} = [q_{\min}, q_{\max}] \times \Delta^3 \times B_\xi$$

**Proposition 1 (Compactness):** $\mathcal{M}_{\text{obs}}$ is compact.

*Proof:* $[q_{\min}, q_{\max}]$ is a compact interval in $\mathbb{R}$. $\Delta^3$ is compact (closed and bounded in $\mathbb{R}^4$). $B_\xi$ is compact (finite product of closed bounded intervals). By Tychonoff's theorem, the finite product is compact. $\square$

**Structure:** $\mathcal{M}_{\text{obs}}$ is a compact manifold with corners. It is not a smooth closed manifold because $\Delta^3$ and $B_\xi$ have boundary faces.

**Dimension:**
$$\dim \mathcal{M}_{\text{obs}} = 1 + 3 + \dim B_\xi = 4 + \dim B_\xi$$

In the minimal model ($\xi$ fixed): $\dim \mathcal{M}_{\text{obs}}^{\text{min}} = 1 + 3 = 4$.

---

### DEF-5. Critical Observer Space $\mathcal{M}_{\text{obs}}^{\text{crit}}$ [Defined, Conditionally]

**The criticality hypothesis** [Hypothesized]:
The observer tracks the phase-transition critical point, so that:

$$q \approx q_c(X_t) := \frac{4\lambda_2(X_t)}{\lvert W''(c) \rvert}$$

where $\lambda_2(X_t)$ is the Fiedler eigenvalue of graph $X_t$, $c = m/n$, and:
$$\lvert W''(c) \rvert = 2(6c - 6c^2 - 1) \quad \text{for } c \in \left(\tfrac{3-\sqrt{3}}{6}, \tfrac{3+\sqrt{3}}{6}\right)$$

**Strict critical observer space:**
$$\mathcal{M}_{\text{obs}}^{\text{crit}} = \{q_c(X_t)\} \times \Delta^3 \times B_\xi \cong \Delta^3 \times B_\xi$$

Under strict criticality, $q$ is entirely scene-determined and drops from the observer's free parameters.

**Proposition 2 (Critical reduction):** Under the criticality hypothesis with fixed scene $X_t$:
$$\mathcal{M}_{\text{obs}}^{\text{crit}} \cong \Delta^3 \times B_\xi$$

*Proof:* The map $(q, \lambda, \xi) \mapsto (\lambda, \xi)$ is a homeomorphism on $\{q_c\} \times \Delta^3 \times B_\xi \cong \Delta^3 \times B_\xi$. $\square$

**Band version** (approximate criticality with tolerance $\varepsilon > 0$):
$$\mathcal{M}_{\text{obs}}^{\text{crit},\varepsilon} = \{(q, \lambda, \xi) \in \mathcal{M}_{\text{obs}} : \lvert q - q_c(X_t) \rvert \leq \varepsilon\}$$

This is a closed subset of $\mathcal{M}_{\text{obs}}$, hence compact.

---

## Part II: Readout Map

### DEF-6. Perceptual Readout Map $\mathcal{P}$ [Defined, Three Levels]

The readout map assigns to each observer parameter configuration a perceptual outcome:
$$\mathcal{P} : \mathcal{M}_{\text{obs}} \times \{X_t\} \to \mathcal{Y}$$

**Note:** $\mathcal{P}$ depends on the scene $X_t$. For a fixed scene, we write $\mathcal{P}_{\!X_t}(\Theta)$.

**Level 1 — Diagnostic-only readout** [Defined as minimal]:
$$\mathcal{P}_{\min}(\Theta) = d_\Theta = (\text{Bind}_\Theta, \text{Sep}_\Theta, \text{Inside}_\Theta, \text{Persist}_\Theta) \in [0,1]^4$$

where the diagnostic vector is computed from the energy minimizer $u^*(\Theta, X_t)$.

**Limitation of $\mathcal{P}_{\min}$:** Two field configurations can share identical diagnostic scores while differing in formation topology (e.g., one connected component vs two). The diagnostic-only readout conflates these.

**Level 2 — Topology-including readout** [Defined, Recommended]:
$$\mathcal{P}_{\text{top}}(\Theta) = (d_\Theta,\ \mathcal{T}_\Theta)$$

where $\mathcal{T}_\Theta$ is the topological formation signature, including:
- $K_{\text{act}}$: number of active formations (connected components of the core)
- Persistence barcode $H_0$: birth/death of connected components as threshold varies
- (Optional) $H_1$: loop structure if relevant

**Level 3 — Full readout** [Defined, Not Yet Computationally Grounded]:
$$\mathcal{P}_{\text{full}}(\Theta) = (d_\Theta,\ \mathcal{T}_\Theta,\ \mathcal{B}_\Theta)$$

where $\mathcal{B}_\Theta$ is the basin signature:
- Number of attractor basins in $E(u)$ landscape
- Basin volumes (relative)
- Transition graph between basins
- Metastability barriers (Kramers rates, if available)

**Canonical choice:** $\mathcal{P}_{\text{top}}$ is the recommended first canonical readout. $\mathcal{P}_{\text{full}}$ requires Package II (Eyring-Kramers) from the main SCC theory, which is currently open.

---

### DEF-7. Perceptual Core [Defined]

The perceptual core of an observer configuration $\Theta$ (given scene $X_t$) is the equivalence class under the gauge group:
$$\text{Core}(\Theta) = [\Theta]_{G_{\mathrm{SCC}}^{(0)}} \in \mathcal{M}_{\text{obs}} / G_{\mathrm{SCC}}^{(0)}$$

Two configurations $\Theta, \Theta'$ share the same core if and only if $\exists g \in G$ such that $g \cdot \Theta = \Theta'$.

**Relationship to readout:** If $\mathcal{P}$ is $G$-invariant (DEF-10), then same core implies same perceptual outcome. The converse is not guaranteed — equal readout does not necessarily imply gauge-equivalence (see OP-OMS-001).

---

## Part III: Gauge Group

### DEF-8. Core-Preserving Gauge Group $G_{\mathrm{SCC}}^{(0)}$ [Defined, Conservative]

$$G_{\mathrm{SCC}}^{(0)} = S_K \times \mathrm{Aut}_{\mathrm{task}}(X, N, K, \mathcal{A})$$

**Component 1: Formation label gauge** $S_K$ [Defined]:

For a $K$-formation system, the formation indices $1, 2, \ldots, K$ are representational conventions. The permutation group $S_K$ acts by relabeling:
$$\sigma \cdot (u^{(1)}, \ldots, u^{(K)}) = (u^{(\sigma^{-1}(1))}, \ldots, u^{(\sigma^{-1}(K))})$$

$S_K$ is a finite group, hence compact. It acts on the multi-formation field space, not on the global parameters $(q, \lambda, \xi)$.

**Justification:** Formation 1 and Formation 2 being swapped cannot change the perceptual core. Without this quotient, the multi-formation space overcounts by a factor of $K!$.

**Component 2: Task-respecting graph automorphism gauge** $\mathrm{Aut}_{\mathrm{task}}$ [Defined, with caveat]:

$$\mathrm{Aut}_{\mathrm{task}}(X, N, K, \mathcal{A}) = \{g : X \to X \mid N(gx, gy) = N(x,y),\ K(gx, gy) = K(x,y),\ g \text{ preserves } \mathcal{A}\}$$

where $\mathcal{A}$ is the task anchor set, which may include:
- Camera frame / body frame reference
- Gravity direction
- Affordance landmarks
- Action-relevant coordinate distinctions

**Critical caveat:** Not all graph symmetries are perceptually gauge. If $g$ corresponds to left-right reflection and the task requires left-right discrimination, then $g \notin \mathrm{Aut}_{\mathrm{task}}$. The set $\mathcal{A}$ is task-specific and must be specified externally. [See OP-OMS-003]

**Component 3: Weight symmetry gauge** $G_{\mathrm{core-weight}}$ [Open, Default = {e}]:

$$G_{\mathrm{core-weight}} = \{e\} \quad \text{(default, conservative)}$$

This is NOT assumed. The energy weights $(\lambda_{cl}, \lambda_{sep}, \lambda_{bd}, \lambda_{tr})$ have distinct semantic roles and their permutation is generally not gauge. The correct $G_{\mathrm{core-weight}}$ must be determined empirically or proven from the energy structure. [See OP-OMS-001]

**Future definition** [Open]:
$$G_{\mathrm{core-weight}}(\mathcal{P}) = \{g \in \mathrm{Diff}(\Delta^3) \mid \mathcal{P}(g \cdot \Theta) = \mathcal{P}(\Theta) \ \forall \Theta\}$$

---

### DEF-9. Stabilizer Subgroup [Defined]

For $\Theta \in \mathcal{M}_{\text{obs}}$ and $G$ acting on the relevant space:
$$G_\Theta = \{g \in G \mid g \cdot \Theta = \Theta\}$$

$G_\Theta$ is a subgroup of $G$ (the stabilizer or isotropy group at $\Theta$).

**Interpretation:**
- $|G_\Theta|$ large $\Rightarrow$ high-symmetry observer configuration (more structurally canonical)
- $G_\Theta = \{e\}$ $\Rightarrow$ generic observer (trivial stabilizer, smooth point in quotient)
- Large stabilizer at $\Theta$ $\Rightarrow$ orbifold singularity at $[\Theta]_G$

---

## Part IV: The Moduli Space

### DEF-10. G-Invariance of Readout [Proposition]

**Proposition 6 (G-invariance):** If $\mathcal{P}$ is $G$-invariant, i.e., $\mathcal{P}(g \cdot \Theta) = \mathcal{P}(\Theta)$ for all $g \in G$ and all $\Theta$, then $\mathcal{P}$ descends to a well-defined map on the quotient:
$$\bar{\mathcal{P}} : \mathcal{M}_{\text{obs}}/G \to \mathcal{Y}$$
such that $\mathcal{P} = \bar{\mathcal{P}} \circ \pi$, where $\pi : \mathcal{M}_{\text{obs}} \to \mathcal{M}_{\text{obs}}/G$ is the quotient projection.

*Proof:* For any $[\Theta]_G \in \mathcal{M}_{\text{obs}}/G$, define $\bar{\mathcal{P}}([\Theta]_G) = \mathcal{P}(\Theta)$. This is well-defined: if $\Theta' = g \cdot \Theta$ for some $g \in G$, then $\mathcal{P}(\Theta') = \mathcal{P}(g \cdot \Theta) = \mathcal{P}(\Theta)$ by $G$-invariance. $\square$

**Note:** The converse direction — that $\mathcal{P}(\Theta) = \mathcal{P}(\Theta')$ implies $\Theta' \in G \cdot \Theta$ — is NOT claimed. This would require surjectivity of the gauge action on the level sets of $\mathcal{P}$.

---

### DEF-11. SCC Observer Moduli Space [Defined]

$$\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}} = \mathcal{M}_{\text{obs}} / G_{\mathrm{SCC}}^{(0)}$$

with the quotient topology: $U \subset \mathfrak{M}$ is open iff $\pi^{-1}(U)$ is open in $\mathcal{M}_{\text{obs}}$.

**Critical version** [Defined, Conditional on criticality hypothesis]:
$$\mathfrak{M}_{\mathrm{SCC,crit}}^{\mathrm{obs}} = \mathcal{M}_{\text{obs}}^{\text{crit}} / G_{\mathrm{SCC}}^{(0)} \cong (\Delta^3 \times B_\xi) / G_{\mathrm{SCC}}^{(0)}$$

**Proposition 3 (Finite gauge and dimension):** Since $G_{\mathrm{SCC}}^{(0)}$ is a finite group, it does not reduce the dimension of the quotient:
$$\dim \mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}} = \dim \mathcal{M}_{\text{obs}}$$

at generic points where the action is free. The quotient may however produce orbifold singularities at fixed points of the action.

*Proof sketch:* A finite group acts with finite orbits. At a generic point $[\Theta]$ with trivial stabilizer, a neighborhood is homeomorphic to a neighborhood in $\mathcal{M}_{\text{obs}}$. Dimension is a local invariant. $\square$

**Corollary:** The primary sources of effective dimension reduction are:
1. Normalization constraints ($\alpha + \beta = 1$: $-1$ DOF; $\sum \lambda_i = 1$: $-1$ DOF)
2. Criticality hypothesis ($q = q_c(X_t)$: $-1$ DOF)
3. Relevance/irrelevance flow in $B_\xi$ (RG-analogy: TBD, OP-OMS-006)

Not from finite gauge quotient.

---

### DEF-12. Fundamental Domain [Defined, for Finite G]

A fundamental domain $\mathcal{F} \subset \mathcal{M}_{\text{obs}}$ for the $G$-action is a closed subset such that:
1. Every $G$-orbit intersects $\mathcal{F}$: $\mathcal{M}_{\text{obs}} = G \cdot \mathcal{F}$
2. The restriction $\pi|_\mathcal{F} : \mathcal{F} \to \mathfrak{M}$ is surjective

The interior of $\mathcal{F}$ contains exactly one representative from each generic (trivial-stabilizer) orbit.

**Example for $S_K$ on $\mathcal{A}^K$:** Choose an ordering functional $h : \mathcal{A} \to \mathbb{R}$ and define:
$$\mathcal{F} = \{(\theta_1, \ldots, \theta_K) \in \mathcal{A}^K : h(\theta_1) \leq h(\theta_2) \leq \cdots \leq h(\theta_K)\}$$

The boundary $h(\theta_i) = h(\theta_j)$ for $i \neq j$ is the stabilizer stratum.

---

### DEF-13. Observer Adaptation Landscape $V$ [Requirements only; not defined]

[**Status: Requirements stated; definition is open (OP-OMS-002)**]

$V : \mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}} \to \mathbb{R}$ must satisfy:

**V1. Gauge invariance:** $V(g \cdot \Theta) = V(\Theta)$ for all $g \in G$. (Automatic since $V$ is defined on the quotient.)

**V2. Continuity:** $V \in C^0(\mathfrak{M})$ at minimum; $V \in C^2$ where smooth structure permits (for gradient flow). Since $\mathfrak{M}$ may be an orbifold with corners, smoothness must be defined carefully.

**V3. Diagnostic compatibility:** $V$ should be monotone-compatible with $\mathcal{P}$ in some partial-order sense. Full specification requires scalarization of the vector-valued readout.

**V4. Basin-generating:** The gradient flow $-\nabla V$ (where defined) should generate attractor basins corresponding to stable observer types.

**V5. Boundary awareness:** Since $\mathcal{M}_{\text{obs}}$ has corners, gradient flow must use projected or constrained dynamics near the boundary.

Possible candidates for $V$ (not selected; see OP-OMS-002):
- Expected formation energy over scenes
- Negative diagnostic quality
- Task loss over perception-action episodes
- Free-energy-like adaptation cost
- Population-level perceptual style potential

---

### DEF-14. Orbifold Structure of $\mathfrak{M}$ [Hypothesized]

**Hypothesis:** $\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$ is generically an orbifold (rather than a smooth manifold), due to fixed points of the $G$-action.

The stabilizer stratification:
$$\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}} = \bigsqcup_{[H] \leq G} \mathfrak{M}_{(H)}$$

where $\mathfrak{M}_{(H)} = \{[\Theta] : G_\Theta \text{ is conjugate to } H\}$ is the stratum of observers with stabilizer type $[H]$.

**Interpretation** [Hypothesis, not theorem]:
The stratum with maximum stabilizer $|G_\Theta| = \lvert G \rvert$ (fixed points of full $G$) may correspond to highly canonical or "species-typical" observer configurations. This is an interpretation, not a proved claim.

---

## Part V: Extended Definitions (OMS-0.2 through OMS-0.7)

### DEF-15. Topological Signature $T_\Theta$ [Defined]

The topological signature of an observer configuration $\Theta$ on scene $X_t$ is:

$$T_\Theta = (N_0,\ \mathrm{Bar}_0,\ \ell_1,\ \ell_2,\ A,\ K^*,\ C_{bd})$$

**Components:**
- $N_0 = K^*$: number of connected components of the formation core $\{i : u^*_i \geq \theta_{\mathrm{core}}\}$
- $\mathrm{Bar}_0$: persistence barcode of $H_0$ (birth-death pairs as threshold varies from 0 to 1)
- $\ell_1$: perimeter of the union of active formation cells (boundary length)
- $\ell_2$: square root of the area (or volume in 3D analog) of active formation
- $A = \ell_2^2$: area of active formation region
- $K^* = $ total number of active formations after thresholding
- $C_{bd}$: boundary component count (number of connected components of the formation boundary)

**Classification:** DEFINED. The full topological signature $T_\Theta$ can be computed from $u^*(\Theta, X_t)$ using standard persistent homology and geometric measures.

**Distinction from $P_{\min}$.** The diagnostic $d_\Theta$ is a scalar summary; $T_\Theta$ is a richer multi-component topological descriptor. Together they form $P_{\mathrm{top}}(\Theta) = (d_\Theta, T_\Theta)$.

**Filed in.** `readout_map_audit.md` DEF-R2.

---

### DEF-16. Admissible Observer Landscape Class $\mathcal{V}_{\mathrm{adm}}$ [Defined]

The admissible observer landscape class is the set of functions $V : \mathcal{M}_{\mathrm{obs}} \to \mathbb{R}_{\geq 0}$ satisfying:

**V1. Continuity:** $V \in C^0(\mathcal{M}_{\mathrm{obs}})$.

**V2. Morse-like genericity:** The critical point set $\mathrm{Crit}(V) = \{\Theta : \nabla V(\Theta) = 0\}$ is finite and non-degenerate (all eigenvalues of the Hessian at critical points are nonzero).

**V3. Bounded below:** $\inf_{\Theta \in \mathcal{M}_{\mathrm{obs}}} V(\Theta) > -\infty$ (automatically satisfied since $\mathcal{M}_{\mathrm{obs}}$ is compact and $V$ is continuous).

**V4. SCC-derived:** $V$ is determined by the SCC energy and readout structure — it is not an arbitrary function on $\mathcal{M}_{\mathrm{obs}}$.

**V5. Gauge-invariant:** $V(g \cdot \Theta) = V(\Theta)$ for all $g \in G_{\mathrm{SCC}}^{(0)}$, so that $V$ descends to a well-defined function on $\mathfrak{M}$.

$$\mathcal{V}_{\mathrm{adm}} = \{V : \mathcal{M}_{\mathrm{obs}} \to \mathbb{R}_{\geq 0} \mid \text{V1--V5 hold}\}$$

**OMS-1.0 position:** OMS-1.0 defines the class $\mathcal{V}_{\mathrm{adm}}$; it does NOT designate a unique canonical $V$. This is by design — different applications (computational vs. empirical vs. theoretical) call for different elements of $\mathcal{V}_{\mathrm{adm}}$.

**Open.** Existence of $V \in \mathcal{V}_{\mathrm{adm}}$ is asserted but not proved. OP-OMS-002 registers this as a blocker.

**Filed in.** `observer_landscape_candidates.md` §1.

---

### DEF-17. Attractor Basin and Perceptual Type [Defined]

**Gradient flow on $\mathcal{M}_{\mathrm{obs}}$:** For $V \in \mathcal{V}_{\mathrm{adm}}$ and $\Theta \in \mathcal{M}_{\mathrm{obs}}$:
$$\dot{\Theta}(t) = -\Pi_{T_\Theta \mathcal{M}_{\mathrm{obs}}} \nabla V(\Theta(t))$$
where $\Pi$ denotes projection onto the tangent space of $\mathcal{M}_{\mathrm{obs}}$ (needed because $\mathcal{M}_{\mathrm{obs}}$ has boundary faces).

**Attractor basin:** For a local minimum $\Theta^* \in \mathcal{M}_{\mathrm{obs}}$ of $V$:
$$\mathcal{B}(\Theta^*) = \{\Theta_0 \in \mathcal{M}_{\mathrm{obs}} : \lim_{t \to \infty} \Theta(t; \Theta_0) = \Theta^*\}$$

**Perceptual type:** The equivalence class $[V, \Theta^*]$ consisting of all observers that flow to $\Theta^*$ under the gradient flow of $V$. Equivalently, $\mathcal{B}(\Theta^*) / G$ on the quotient.

**Central distinction (mandatory):** Perceptual types are NOT connected components of $\mathfrak{M}$. They are attractor basins of $V \in \mathcal{V}_{\mathrm{adm}}$. Since $\mathfrak{M}$ is connected (Prop 6), all perceptual types are part of a single connected space. The basin boundaries (saddle-point level sets) divide the space functionally, not topologically.

**Classification:** DEFINED. Existence of multiple perceptual types depends on the choice of $V$.

**Filed in.** `basin_stratification.md` §2.

---

### DEF-18. Relevant and Irrelevant Observer Directions [Defined]

For observer $\Theta \in \mathcal{M}_{\mathrm{obs}}$, let $J_P(\Theta)$ be the Jacobian of the readout map $P_{\mathrm{top}} : \mathcal{M}_{\mathrm{obs}} \to \mathcal{Y}$ (see DEF-22).

**Relevant direction at $\Theta$:** A unit tangent vector $v \in T_\Theta \mathcal{M}_{\mathrm{obs}}$ is $\varepsilon$-relevant if:
$$\lVert J_P(\Theta) \cdot v \rVert \geq \varepsilon$$

i.e., small perturbations in direction $v$ produce changes of magnitude $\geq \varepsilon$ in the readout.

**Irrelevant direction at $\Theta$:** A unit vector $v$ is $\varepsilon$-irrelevant if:
$$\lVert J_P(\Theta) \cdot v \rVert < \varepsilon$$

**Relevant subspace:** $V_{\mathrm{rel}}(\Theta; \varepsilon) = \mathrm{span}\{v_i : \sigma_i(J_P(\Theta)) \geq \varepsilon\}$ where $\sigma_i$ are singular values of $J_P(\Theta)$ and $v_i$ are corresponding right singular vectors.

**Irrelevant subspace:** $V_{\mathrm{irr}}(\Theta; \varepsilon) = V_{\mathrm{rel}}(\Theta; \varepsilon)^\perp$ in $T_\Theta \mathcal{M}_{\mathrm{obs}}$.

**Classification:** DEFINED. The decomposition is $\varepsilon$-dependent and observer-location-dependent.

**Filed in.** `rg_relevance_flow.md` §2, RG3–RG5.

---

### DEF-19. Local Effective Dimension $d_{\mathrm{eff}}$ [Defined, Hypothesized Value]

$$d_{\mathrm{eff}}(\Theta; \varepsilon) = \#\{\sigma_i(J_P(\Theta)) \geq \varepsilon\}$$

i.e., the number of singular values of the readout Jacobian exceeding the threshold $\varepsilon$.

**Interpretation:** $d_{\mathrm{eff}}(\Theta; \varepsilon)$ is the number of independently discriminable observer directions at $\Theta$ at resolution $\varepsilon$. Directions in $V_{\mathrm{irr}}(\Theta; \varepsilon)$ are perceptually indistinguishable at resolution $\varepsilon$.

**Global effective dimension:**
$$d_{\mathrm{eff}}^{\mathrm{glob}}(\varepsilon) = \max_{\Theta \in \mathcal{M}_{\mathrm{obs}}} d_{\mathrm{eff}}(\Theta; \varepsilon)$$

**Hypothesis RG1** [HYPOTHESIZED]: For typical observers and $\varepsilon = 0.05$:
$$d_{\mathrm{eff}}^{\mathrm{typical}}(0.05) \in [2, 4]$$

This hypothesis must be tested by VP-6 (Jacobian singular spectrum computation).

**Warning.** The discrete component $K^*$ of $P_{\mathrm{top}}$ is not differentiable. $d_{\mathrm{eff}}$ should be computed using only the smooth components of $P_{\mathrm{top}}$ (diagnostic vector + continuous topological summaries $\ell_1, \ell_2, A$).

**Filed in.** `rg_relevance_flow.md` §3, DEF RG5.

---

### DEF-20. Boundary Strata of $\Delta^3$ [Defined]

For index set $I \subseteq \{cl, sep, bd, tr\}$, the $I$-face of $\Delta^3$ is:
$$\partial_I \Delta^3 = \{\lambda \in \Delta^3 : \lambda_i = 0\ \forall i \in I\}$$

**Dimension of stratum:** $\dim(\partial_I \Delta^3) = 3 - \lvert I \rvert$ (number of surviving active coordinates minus normalization constraint).

**Full stratification of $\Delta^3$:** There are $2^4 = 16$ faces (including the interior and the four vertices):

| $\lvert I \rvert$ | Count | Dimension | Interpretation |
|---|---|---|---|
| 0 | 1 | 3 | Interior: full observer (all terms active) |
| 1 | 4 | 2 | Faces: one term ablated |
| 2 | 6 | 1 | Edges: two terms ablated |
| 3 | 4 | 0 | Vertices: three terms ablated, one dominant |
| 4 | 1 | — | Empty set ($\lambda = 0$ violates normalization) |

**Four vertices** (one term dominant):
- $e_{cl} = (1,0,0,0)$: pure closure observer
- $e_{sep} = (0,1,0,0)$: pure separation observer
- $e_{bd} = (0,0,1,0)$: pure boundary observer
- $e_{tr} = (0,0,0,1)$: pure transport observer

**Absorbing wall property (Prop SD1):** Each face $\partial_I \Delta^3$ is forward-invariant under the projected gradient flow of any $V \in \mathcal{V}_{\mathrm{adm}}$. Once $\lambda_i = 0$, the flow cannot increase $\lambda_i$ without external perturbation.

**Filed in.** `stratified_dynamics.md` §2–§5.

---

### DEF-21. Latent Generator Framework [Defined, OMS-Gen Extension]

A latent generator for $\mathcal{M}_{\mathrm{obs}}$ is a pair $(Z, \Gamma)$ where:
- $Z$ is a latent parameter space (typically $\mathbb{R}^r$ or a compact manifold)
- $\Gamma : Z \to \Delta^3$ is a smooth surjection (the generator map)

**Latent symmetry group:** A compact group $H$ is a latent symmetry of $(Z, \Gamma)$ if $H$ acts continuously on $Z$ and:
$$\Gamma(h \cdot z) = \Gamma(z) \quad \forall h \in H, z \in Z$$

In this case, $\Gamma$ factors through the orbit space: $\Gamma = \tilde{\Gamma} \circ \pi_H$ where $\pi_H : Z \to Z/H$ and $\tilde{\Gamma} : Z/H \to \Delta^3$.

**Dimension reduction from latent symmetry:** If $H$ has dimension $k$ and acts freely on $Z$, then:
$$\dim_{\mathrm{eff}}(\Delta^3 \text{ via } Z/H) = \dim(Z) - k$$

**Classification:** DEFINED. This framework is part of OMS-Gen (generalization extension), not OMS core. OMS core requires no latent space.

**Prop LS1 (proved):** No continuous group $H$ acts faithfully on $\Delta^3$ preserving all four vertices $\{e_{cl}, e_{sep}, e_{bd}, e_{tr}\}$. Hence the only relevant latent symmetries arise from non-trivial generators $\Gamma$ that do not span all vertices.

**Filed in.** `latent_symmetry.md` §1–§4.

---

### DEF-22. Perceptual Jacobian [Defined]

For observer $\Theta \in \mathcal{M}_{\mathrm{obs}}$ and smooth readout map $P_{\mathrm{top}} : \mathcal{M}_{\mathrm{obs}} \to \mathcal{Y}_{\mathrm{smooth}}$ (smooth components only):

$$J_P(\Theta) = D_\Theta P_{\mathrm{top}} \in \mathbb{R}^{p \times n_\Theta}$$

where $p = \dim(\mathcal{Y}_{\mathrm{smooth}})$ (smooth readout dimension) and $n_\Theta = \dim(T_\Theta \mathcal{M}_{\mathrm{obs}})$ (local tangent space dimension).

**Singular value decomposition:**
$$J_P(\Theta) = U \Sigma V^\top, \quad \sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_{\min(p,n_\Theta)} \geq 0$$

**Interpretations of singular values:**
- $\sigma_i$ large: direction $v_i$ (right singular vector) in $T_\Theta \mathcal{M}_{\mathrm{obs}}$ is perceptually sensitive
- $\sigma_i \approx 0$: direction $v_i$ is perceptually flat (irrelevant at the given resolution)

**Numerical computation:** Use centered finite differences:
$$J_P^{jk}(\Theta) \approx \frac{P_{\mathrm{top},j}(\Theta + \varepsilon e_k) - P_{\mathrm{top},j}(\Theta - \varepsilon e_k)}{2\varepsilon}$$
with $\varepsilon = 10^{-3}$ (consistent with VP-6 protocol).

**Classification:** DEFINED. The Jacobian is well-defined wherever $P_{\mathrm{top}}$ is $C^1$, which requires continuity of $u^*(\Theta)$ (OP-OMS-009 residual sub-question — open, but no longer a canonical promotion blocker).

**Filed in.** `rg_relevance_flow.md` §2, DEF RG2.
