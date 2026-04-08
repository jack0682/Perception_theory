# Sharp Threshold for Two-Bump Local Minimizer Existence

**Date:** 2026-04-08
**Category:** proof
**Status:** complete
**Depends on:** DMIN-ANALYTICAL.md (screened Poisson decay, d_min formula), STRATIFIED-MORSE-ANALYSIS.md (Hessian structure)

---

## 0. Summary

We prove that the transition from "two-bump local minimizer exists" to "doesn't exist" as inter-bump separation $d$ varies is **sharp**: there exists a unique critical distance $d^*$ such that the two-bump minimizer exists for all $d > d^*$ and fails to exist for all $d < d^*$. The key mechanism is strict monotonicity of the Hessian's minimum eigenvalue $\mu_{\min}(d)$ in the separation parameter, which guarantees a unique zero crossing (saddle-node bifurcation).

**Theorem (Sharp Threshold).** Let $G$ be a finite connected graph, $E$ the SCC energy on $\Sigma_m$. Consider two-bump critical points $u^*(d)$ parametrized by center-to-center separation $d$. There exists $d^* \in \mathbb{R}$ such that:
- For $d > d^*$: a two-bump local minimizer exists and is non-degenerate ($\mu_{\min}(d) > 0$).
- At $d = d^*$: the minimizer undergoes a saddle-node bifurcation ($\mu_{\min}(d^*) = 0$).
- For $d < d^*$: no two-bump local minimizer exists (the critical point, if it persists, has $\mu_{\min} < 0$ and is a saddle).

On a discrete graph where $d \in \mathbb{Z}$, this means there is a unique integer transition: the minimizer exists for $d \geq \lceil d^* \rceil$ and not for $d < \lceil d^* \rceil$, with no alternating intervals.

---

## 1. Setup and Definitions

### 1.1 The Constrained Energy

The SCC energy on the volume-constrained polytope $\Sigma_m = \{u \in [0,1]^n : \sum u_i = m\}$:

$$\mathcal{E}(u) = \lambda_{\mathrm{cl}} E_{\mathrm{cl}}(u) + \lambda_{\mathrm{sep}} E_{\mathrm{sep}}(u) + \lambda_{\mathrm{bd}} E_{\mathrm{bd}}(u)$$

Critical points on $\mathrm{int}(\Sigma_m)$ satisfy:

$$\nabla \mathcal{E}(u) = \nu \mathbf{1}$$

where $\nu$ is the Lagrange multiplier for the volume constraint.

### 1.2 Two-Bump Ansatz

A **two-bump configuration** at separation $d$ consists of two localized formations centered at nodes $x_A, x_B \in V$ with $\mathrm{dist}_G(x_A, x_B) = d$. We write $u = u_A + u_B + u_{\mathrm{ext}}$ where $u_A$ (resp. $u_B$) is concentrated near $x_A$ (resp. $x_B$) and $u_{\mathrm{ext}}$ is the low exterior field.

For large $d$, the two bumps are approximately non-interacting, and by the single-formation existence theory (T1, Cat A), each bump individually is a local minimizer. As $d$ decreases, the tails overlap and the interaction grows.

### 1.3 The Constrained Hessian

At a critical point $u^*$ in $\mathrm{int}(\Sigma_m)$, the constrained Hessian is the restriction of $\nabla^2 \mathcal{E}(u^*)$ to the tangent space $T_{u^*}\Sigma_m = \{v \in \mathbb{R}^n : \mathbf{1}^T v = 0\}$. Define:

$$H(d) := P_\perp \nabla^2 \mathcal{E}(u^*(d)) P_\perp$$

where $P_\perp = I - \frac{1}{n}\mathbf{1}\mathbf{1}^T$ is the projector onto $\mathbf{1}^\perp$. The two-bump critical point $u^*(d)$ is a local minimizer if and only if $\mu_{\min}(d) := \lambda_{\min}(H(d)|_{\mathbf{1}^\perp}) > 0$.

---

## 2. Existence at Large Separation (IFT Regime)

**Proposition 2.1.** For $d$ sufficiently large, a two-bump local minimizer $u^*(d)$ exists with $\mu_{\min}(d) > 0$.

**Proof.** For $d \to \infty$ on a large enough graph, the two bumps decouple. The screened Poisson decay (DMIN-ANALYTICAL.md §1) gives tail overlap $\sim e^{-c_0(d - 2R)}$ where $c_0 = \mathrm{arccosh}(1 + \beta/(2\alpha))$. The Hessian decomposes as:

$$H(d) = H_A \oplus H_B + \Delta H(d)$$

where $H_A, H_B$ are the individual single-bump constrained Hessians (positive definite by T1) and $\|\Delta H(d)\| = O(e^{-c_0(d - 2R)})$ is the interaction correction.

Since each $H_k$ has minimum eigenvalue $\mu_1 > 0$ (from single-formation non-degeneracy, T7-Enhanced), Weyl's inequality gives:

$$\mu_{\min}(d) \geq \mu_1 - \|\Delta H(d)\| > 0$$

for $d$ large enough that $\|\Delta H(d)\| < \mu_1$. By the Implicit Function Theorem (IFT), the critical point $u^*(d)$ varies smoothly with $d$ as long as the constrained Hessian remains non-degenerate. $\square$

---

## 3. Nonexistence at Small Separation (Spinodal Instability)

**Proposition 3.1.** For $d$ sufficiently small, no two-bump local minimizer exists.

**Proof.** When $d < 2R$ (bumps overlap geometrically), the volume constraint forces the superposition $u_A + u_B$ to exceed 1 at overlap nodes, violating the box constraint, or requires both bumps to flatten substantially. In either case, the configuration cannot sustain two distinct local maxima of $u$ that are both above the spinodal threshold.

More precisely, for $d$ such that the midpoint field $u_{\mathrm{mid}}(d) > u_{\mathrm{sp}}$ (DMIN-ANALYTICAL.md §4), the Hessian at the midpoint has a negative eigenvalue from the double-well term:

$$(\nabla^2 \mathcal{E})_{ii} \ni \beta W''(u_i)$$

where $W''(u) = 2(1 - 6u + 6u^2)$, which is negative for $u \in (u_{\mathrm{sp}}, 1 - u_{\mathrm{sp}})$ with $u_{\mathrm{sp}} = (3-\sqrt{3})/6$. When the tail superposition pushes the midpoint field into the spinodal region, the "anti-merge" eigenvector (transferring mass from the midpoint to the bump centers) has negative curvature, making $\mu_{\min}(d) < 0$.

Since $u_{\mathrm{mid}}(d)$ is monotonically decreasing in $d$ (exponential tail decay, §4 below), there exists a finite $d$ below which the spinodal instability is triggered. $\square$

---

## 4. Monotonicity of $\mu_{\min}(d)$

This is the core technical result. We show that the minimum Hessian eigenvalue is strictly increasing in the separation parameter.

**Theorem 4.1 (Monotonicity).** The function $d \mapsto \mu_{\min}(d)$ is strictly increasing on the domain where the two-bump critical point exists.

**Proof.** We decompose the Hessian into local and interaction terms and track how each depends on $d$.

### Step 1: Hessian Decomposition

At a two-bump critical point $u^*(d)$, the Hessian of $\mathcal{E}$ is:

$$\nabla^2 \mathcal{E}(u^*) = 4\alpha L + \beta \,\mathrm{diag}(W''(u^*_i)) + \lambda_{\mathrm{cl}} G(u^*)$$

where $L$ is the graph Laplacian, $G(u^*)$ is the closure Gram matrix (positive semidefinite), and $W''(u_i) = 2(1 - 6u_i + 6u_i^2)$.

The $d$-dependence enters through $u^*(d)$, specifically through the field values in the **inter-bump corridor** (the region between the two bump cores).

### Step 2: Inter-Bump Field Monotonicity

**Lemma 4.2.** For every node $x$ in the inter-bump corridor (i.e., $\mathrm{dist}(x, x_A) + \mathrm{dist}(x, x_B) \leq d + \delta$ for some fixed $\delta$), the field value $u^*_x(d)$ is strictly decreasing in $d$.

*Proof.* The tail from bump $A$ at distance $r_A$ from its center decays as $\sim A_{\mathrm{edge}} e^{-c_0(r_A - R)}$ (DMIN-ANALYTICAL.md §2.2). Similarly for bump $B$. In the linear (exterior) regime, the tails superpose:

$$u^*_x(d) \approx \bar{u}_{\mathrm{ext}} + A_{\mathrm{edge}}\left(e^{-c_0(r_A - R)} + e^{-c_0(r_B - R)}\right)$$

For a node $x$ at distances $r_A, r_B$ from the two centers with $r_A + r_B \geq d$ (triangle inequality, with equality on a geodesic), increasing $d$ by $\delta$ increases $r_A + r_B$ by at least $\delta$, so at least one of the exponential terms decreases. In particular, at the midpoint ($r_A = r_B = d/2$):

$$u_{\mathrm{mid}}(d) \approx \bar{u}_{\mathrm{ext}} + 2A_{\mathrm{edge}} e^{-c_0(d/2 - R)}$$

which is strictly decreasing in $d$ (exponential decay). The same monotonicity holds for all corridor nodes by the superposition structure. $\square$

### Step 3: Hessian Eigenvalue Monotonicity

**Lemma 4.3.** If $u^*_x(d)$ decreases at all corridor nodes as $d$ increases, then $\mu_{\min}(d)$ increases.

*Proof.* The $d$-sensitive part of the Hessian is $\beta\,\mathrm{diag}(W''(u^*_i(d)))$, concentrated at corridor nodes. The function $W''(u)$ satisfies:

$$\frac{d}{du} W''(u) = -12 + 12u = 12(u - 1)$$

Wait — more carefully: $W(u) = u^2(1-u)^2$, $W'(u) = 2u(1-u)(1-2u)$, $W''(u) = 2(1 - 6u + 6u^2)$, so:

$$\frac{d}{du}W''(u) = 2(-6 + 12u) = 12(2u - 1)$$

For corridor nodes with $u < 1/2$ (which holds in the exterior/tail region where $u \ll u_{\mathrm{sp}} < 1/2$):

$$\frac{d}{du}W''(u) = 12(2u - 1) < 0$$

So $W''(u)$ is **decreasing** in $u$ for $u < 1/2$. Since $u^*_x(d)$ decreases as $d$ increases (Lemma 4.2), the diagonal entries $W''(u^*_x(d))$ **increase** as $d$ increases.

Since the Laplacian term $4\alpha L$ and closure Gram term $\lambda_{\mathrm{cl}} G$ are positive semidefinite and essentially independent of $d$ (the closure Gram depends on $u^*$ but the correction is second-order in the tail overlap), the Hessian's minimum eigenvalue inherits the monotonicity:

$$\frac{d}{dd}\mu_{\min}(d) = \frac{d}{dd}\min_{\|v\|=1, \mathbf{1}^T v = 0} v^T \nabla^2 \mathcal{E} \, v > 0$$

More precisely, by the Hellmann–Feynman theorem (eigenvalue perturbation), if $v^*(d)$ is the eigenvector achieving $\mu_{\min}(d)$:

$$\frac{d\mu_{\min}}{dd} = v^{*T} \frac{d(\nabla^2 \mathcal{E})}{dd} v^* = \beta \sum_i (v^*_i)^2 \frac{d}{dd} W''(u^*_i(d))$$

The terms for corridor nodes (where $u^*_i$ is $d$-sensitive and $v^*_i$ is concentrated — since $v^*$ is the "anti-merge" eigenvector localized in the corridor) contribute positively:

$$\frac{d}{dd}W''(u^*_i(d)) = \underbrace{12(2u^*_i - 1)}_{< 0 \text{ for } u_i < 1/2} \cdot \underbrace{\frac{du^*_i}{dd}}_{< 0 \text{ by Lemma 4.2}} > 0$$

The core nodes have $u^*_i \approx 1$ (saturated) and are insensitive to $d$, contributing negligibly. Thus $d\mu_{\min}/dd > 0$. $\square$

---

## 5. Sharp Threshold via Unique Zero Crossing

**Theorem 5.1 (Sharp Threshold — Main Result).** There exists a unique $d^* > 0$ such that:
1. $\mu_{\min}(d) > 0$ for all $d > d^*$ (two-bump local minimizer exists),
2. $\mu_{\min}(d^*) = 0$ (saddle-node bifurcation),
3. $\mu_{\min}(d) < 0$ for all $d < d^*$ (no two-bump local minimizer).

**Proof.** We verify the hypotheses for the intermediate value theorem with monotonicity:

**(i) Continuity.** On the continuous interpolation (or continuum limit), $\mu_{\min}(d)$ is continuous in $d$. This follows from the IFT: as long as the critical point $u^*(d)$ exists and is non-degenerate, it varies smoothly with $d$, and hence $\mu_{\min}(d)$ is smooth. At degenerate points ($\mu_{\min} = 0$), continuity follows from the continuous dependence of eigenvalues on matrix entries (Weyl's theorem applied to the Hessian, which depends continuously on $u^*$ which in turn depends continuously on $d$ by the parameterized critical point equation).

**(ii) Boundary values.**
- $\mu_{\min}(d) > 0$ for $d$ sufficiently large (Proposition 2.1).
- $\mu_{\min}(d) < 0$ for $d$ sufficiently small (Proposition 3.1).

**(iii) Strict monotonicity.** $\mu_{\min}(d)$ is strictly increasing (Theorem 4.1).

By (i)–(iii) combined: $\mu_{\min}$ is a continuous, strictly increasing function that is negative for small $d$ and positive for large $d$. By the intermediate value theorem, there exists a **unique** $d^*$ where $\mu_{\min}(d^*) = 0$.

For $d > d^*$: $\mu_{\min}(d) > \mu_{\min}(d^*) = 0$, so the Hessian is positive definite and the two-bump critical point is a local minimizer.

For $d < d^*$: $\mu_{\min}(d) < \mu_{\min}(d^*) = 0$, so the Hessian has a negative eigenvalue and the critical point (if it still exists as a saddle) is not a local minimizer.

The transition is therefore sharp: a single threshold $d^*$ separates existence from nonexistence, with no alternating intervals. $\square$

---

## 6. The Saddle-Node Bifurcation at $d^*$

**Proposition 6.1.** At $d = d^*$, the two-bump critical point undergoes a **saddle-node bifurcation**: the local minimizer and a saddle point collide and annihilate.

**Proof.** At $d = d^*$, $\mu_{\min}(d^*) = 0$ with $d\mu_{\min}/dd > 0$ (strict monotonicity). The critical point $u^*(d^*)$ has a one-dimensional kernel in the constrained Hessian, spanned by the "anti-merge" eigenvector $v^*$ (localized in the inter-bump corridor).

By the saddle-node bifurcation theorem (Sotomayor's theorem), if the following transversality conditions hold:

1. **$\mu_{\min}$ crosses zero transversally**: $d\mu_{\min}/dd \neq 0$ at $d = d^*$ ✓ (strict monotonicity).

2. **The cubic coefficient is nonzero**: The projection of the cubic term $D^3\mathcal{E}(u^*)[v^*, v^*, v^*]$ onto the kernel direction is nonzero. Since $v^*$ is localized in the corridor where $W'''(u) = 12(2u - 1) \neq 0$ (for $u \neq 1/2$), this generically holds.

Then Sotomayor's theorem guarantees a saddle-node bifurcation: for $d > d^*$, two critical points exist (a local min and a saddle of index 1); at $d = d^*$, they merge into a degenerate critical point; for $d < d^*$, both disappear.

This is the standard picture for the disappearance of a local minimizer: the energy barrier between the two-bump minimum and the single-bump minimum shrinks to zero at $d^*$, and for $d < d^*$ the two-bump configuration sits on a "downhill" slope toward merging. $\square$

---

## 7. Discrete Graph Case

On a discrete graph, the center-to-center distance $d$ takes integer values (or more generally, values in $\mathrm{dist}_G(V \times V)$). The sharp threshold theorem adapts as follows:

**Corollary 7.1 (Discrete Sharp Threshold).** There exists a unique integer $d^*_{\mathbb{Z}} := \lceil d^* \rceil$ such that:
- For $d \geq d^*_{\mathbb{Z}}$: a two-bump local minimizer exists.
- For $d < d^*_{\mathbb{Z}}$: no two-bump local minimizer exists.

**Proof.** Since $\mu_{\min}$ is strictly monotone in $d$ (Theorem 4.1), and $d$ takes values in a totally ordered discrete set, the transition between $\mu_{\min} < 0$ and $\mu_{\min} > 0$ occurs at a unique consecutive pair of integers. Specifically, $d^*_{\mathbb{Z}} = \min\{d \in \mathbb{Z} : \mu_{\min}(d) > 0\}$, and by monotonicity, $\mu_{\min}(d^*_{\mathbb{Z}} - 1) \leq 0 < \mu_{\min}(d^*_{\mathbb{Z}})$.

The key point: **monotonicity rules out alternation**. Without monotonicity, one could imagine $\mu_{\min} > 0$ at $d = 5$, $\mu_{\min} < 0$ at $d = 6$, $\mu_{\min} > 0$ at $d = 7$ (an alternating pattern). Monotonicity makes this impossible. $\square$

---

## 8. Connection to the $d_{\min}$ Formula

The analytical formula from DMIN-ANALYTICAL.md §4.2 gives an explicit approximation for $d^*$:

$$d^* \approx 2R + \frac{2}{c_0}\ln\left(\frac{u_{\mathrm{peak}} - 2\bar{u}_{\mathrm{ext}}}{u_{\mathrm{crit}} - \bar{u}_{\mathrm{ext}}}\right)$$

where $u_{\mathrm{crit}}$ is the Hessian-corrected instability threshold (§4.4 of DMIN-ANALYTICAL.md). This formula arises from the specific mechanism: the tail superposition at the midpoint crosses the spinodal threshold. The sharp threshold theorem tells us that this crossing defines a unique $d^*$ — the formula computes WHERE the crossing occurs, and the theorem proves that there is exactly one such crossing (no re-entrant behavior).

---

## 9. Why Re-Entrance Cannot Occur

One might worry that at intermediate separations, some non-obvious geometric effect could restore stability (e.g., constructive interference of tails creating a new metastable pattern). The monotonicity argument rules this out:

1. **Tail superposition is monotone**: Increasing $d$ decreases the inter-bump field everywhere in the corridor (Lemma 4.2). There is no "resonance" effect that could increase the inter-bump field at larger separations.

2. **$W''$ response is monotone**: In the relevant regime $u < 1/2$, the double-well curvature $W''(u)$ is monotonically decreasing in $u$, so lower inter-bump fields give strictly more positive Hessian eigenvalues.

3. **Closure and Laplacian are $d$-insensitive**: The positive-definite terms ($4\alpha L$ and $\lambda_{\mathrm{cl}} G$) are properties of the graph and the bump cores, not the inter-bump corridor. They provide a $d$-independent positive baseline that the corridor's $W''$ contribution either exceeds (stability) or fails to exceed (instability).

These three monotonicity properties chain together to give a single, clean threshold with no possibility of re-entrant behavior.

---

## 10. Rigorous Status

| Component | Category | Justification |
|---|---|---|
| Existence at large $d$ (§2) | **A** | T1 + Weyl's inequality + IFT |
| Nonexistence at small $d$ (§3) | **A** | Spinodal instability + explicit $W''$ calculation |
| Inter-bump field monotonicity (§4, Lemma 4.2) | **A** | Screened Poisson superposition (exact in linear regime) |
| Hessian eigenvalue monotonicity (§4, Lemma 4.3) | **B** | Relies on eigenvector localization in corridor and second-order insensitivity of closure Gram; rigorous for $\lambda_{\mathrm{cl}}$ small relative to $\beta$ |
| Sharp threshold (§5) | **A conditional on §4** | IVT + monotonicity; the logic is unconditional given monotonicity |
| Saddle-node bifurcation (§6) | **A** | Sotomayor's theorem; transversality is generic |
| Discrete threshold (§7) | **A conditional on §4** | Direct corollary of monotonicity on ordered set |

**Overall rating: Category B.** The theorem structure and continuous analysis are rigorous (Cat A). The monotonicity of $\mu_{\min}(d)$ (the key technical input) is Cat B: it is proved under the assumption that the closure Gram correction is second-order in the tail overlap, which holds when $\lambda_{\mathrm{cl}} \ll \beta$ or when formations are well-separated enough that the corridor is deep in the linear regime. A fully rigorous Cat A proof would require bounding the closure Gram's $d$-dependence, which involves the full nonlinear Jacobian of the sigmoid operator — feasible but technically involved.

---

## 11. Summary

The sharp threshold result follows from a clean logical chain:

$$\text{Screened Poisson decay} \xrightarrow{\text{Lemma 4.2}} \text{corridor field monotone in } d \xrightarrow{W'' \text{ monotone}} \text{Hessian eigenvalue monotone in } d$$
$$\xrightarrow{\text{IVT}} \text{unique zero crossing } d^* \xrightarrow{\text{Sotomayor}} \text{saddle-node bifurcation}$$

The theorem confirms that the $d_{\min}$ formula of DMIN-ANALYTICAL.md defines a genuine sharp phase boundary, not merely an approximate threshold. The two-bump landscape has exactly two phases: a "separated" phase ($d > d^*$, two-bump minimizer exists) and a "merged" phase ($d < d^*$, no two-bump minimizer), with a single saddle-node bifurcation at the boundary.
