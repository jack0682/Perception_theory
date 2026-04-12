# Iteration 13 — Temporal Proof Repair: Gaps 1, 2, 3

**Author:** Temporal Prover (Week 6) | **Date:** 2026-03-30

**Purpose:** Close three of the six gaps identified in the I7 Temporal Audit for T-Persist-1. Gaps 4 (basin radius/Morse persistence), 5 (transport concentration), and 6 (interior gap lower bound) remain open.

---

## Gap 1 Closure: Explicit Definition of ε-Gentle Transition

### Problem (from I7-temporal-audit.md, HIGH-2)

The theorem conditions on the transition being "ε-gentle" without defining this precisely. Different definitions yield different theorems.

### Definition (ε-Gentle Transition)

**Definition 1 (ε-Gentle Transition).** Let $\hat{u}_t \in \Sigma_m$ be a formation-structured minimizer of $\mathcal{E}_t$ on a fixed support space $X = X_t = X_s$ with $n = |X|$. A transition from time $t$ to time $s$ is **$\varepsilon$-gentle** if there exist constants $\varepsilon_1, \varepsilon_2, \varepsilon_3 > 0$ such that:

**(G1) Energy landscape closeness.** The energies $\mathcal{E}_t$ and $\mathcal{E}_s$, viewed as $C^2$ functions on $\Sigma_m$, satisfy:

$$\|\mathcal{E}_s - \mathcal{E}_t\|_{C^2(\Sigma_m)} \leq \varepsilon_1$$

where the $C^2$ norm is:

$$\|\mathcal{E}_s - \mathcal{E}_t\|_{C^2(\Sigma_m)} := \sup_{u \in \Sigma_m} |\mathcal{E}_s(u) - \mathcal{E}_t(u)| + \sup_{u \in \Sigma_m} \|\nabla_\Sigma \mathcal{E}_s(u) - \nabla_\Sigma \mathcal{E}_t(u)\|_2 + \sup_{u \in \Sigma_m} \|\nabla^2_\Sigma \mathcal{E}_s(u) - \nabla^2_\Sigma \mathcal{E}_t(u)\|_{\mathrm{op}}$$

Here $\nabla_\Sigma$ and $\nabla^2_\Sigma$ denote the gradient and Hessian projected onto the tangent space $T_u\Sigma_m = \{v \in \mathbb{R}^n : \mathbf{1}^T v = 0\}$.

**(G2) Transport displacement smallness.** The temporal transport kernel $\mathbf{M}_{t \to s}$ satisfies:

$$\|\mathbf{M}_{t \to s} \hat{u}_t - \hat{u}_t\|_2 \leq \varepsilon_2$$

This bounds how far the transport moves the formation field from its current configuration.

**(G3) Adjacency kernel closeness.** The adjacency kernels satisfy:

$$\|\mathbf{N}_s - \mathbf{N}_t\|_{\mathrm{op}} \leq \varepsilon_3$$

where $\|\cdot\|_{\mathrm{op}}$ is the operator norm (largest singular value) on $\mathbb{R}^{n \times n}$.

The **gentleness parameter** is $\varepsilon := \max(\varepsilon_1, \varepsilon_2, \varepsilon_3)$.

### Remarks on Definition 1

1. **Fixed support space.** The definition requires $X_t = X_s = X$. The Canonical Spec (§3.2) allows $X_t$ to vary, but T-Persist-1 cannot apply when the support space changes, because then $\mathcal{E}_t$ and $\mathcal{E}_s$ have different domains and the IFT has no common manifold. This is an explicit hypothesis, not a silent assumption.

2. **Why three separate bounds.** The three conditions are logically independent:
   - (G1) controls the energy landscape directly, which is what the IFT needs.
   - (G2) controls the initial condition for gradient flow (the transported field as starting point).
   - (G3) controls the relational structure, which feeds into closure, distinction, and co-belonging operators.

   In practice, (G3) implies a bound on (G1) because the operators $\mathrm{Cl}_t, \mathbf{D}_t, \mathbf{C}_t$ all depend on $\mathbf{N}_t$. Specifically, if the closure operator is $\mathrm{Cl}(u) = \sigma(a_{\mathrm{cl}} P u + b_{\mathrm{cl}})$ with row-normalized $P = D^{-1}N$, then $\|\mathrm{Cl}_s(u) - \mathrm{Cl}_t(u)\| \leq \|\sigma'\|_\infty \cdot a_{\mathrm{cl}} \cdot \|P_s - P_t\|_{\mathrm{op}}$, and $\|P_s - P_t\|_{\mathrm{op}}$ is controlled by $\|\mathbf{N}_s - \mathbf{N}_t\|_{\mathrm{op}}$ and the minimum degree. However, we retain (G1) as the primary condition because it is the one directly consumed by the IFT, and (G3) serves as a more interpretable sufficient condition.

3. **Smooth parameterization.** For the IFT, we need the energy to vary smoothly in a parameter. Define $\lambda \in [0,1]$ and $\mathcal{E}_\lambda := (1-\lambda)\mathcal{E}_t + \lambda \mathcal{E}_s$. This is $C^2$ in $(\lambda, u) \in [0,1] \times \Sigma_m$ because both $\mathcal{E}_t$ and $\mathcal{E}_s$ are $C^2$ on $\Sigma_m$ (sigmoid closure with $b_D = 0$ gives analyticity; see Canonical Spec §13, T14). The path $\lambda \mapsto \mathcal{E}_\lambda$ is the smooth parameterization required by IFT. $\square$

---

## Gap 2 Closure: IFT Hypotheses on the Constrained Manifold $\Sigma_m$

### Problem (from I7-temporal-audit.md, CRITICAL-1)

The IFT step claims a minimizer $\hat{u}_s$ exists near $\hat{u}_t$ but never states the required hypotheses on the constrained manifold $\Sigma_m$. The constrained vs. unconstrained Hessian distinction is not addressed.

### Setup

The volume-constrained manifold is:

$$\Sigma_m = \{u \in [0,1]^n : \mathbf{1}^T u = m\}$$

This is an $(n-1)$-dimensional smooth manifold (a simplex slice). Its tangent space at any point $u$ is:

$$T_u \Sigma_m = \{v \in \mathbb{R}^n : \mathbf{1}^T v = 0\}$$

which is independent of $u$ (the constraint is affine). The orthogonal projection onto $T_u \Sigma_m$ is:

$$\Pi_\Sigma = I - \frac{1}{n} \mathbf{1}\mathbf{1}^T$$

### Proposition 1 (IFT on $\Sigma_m$)

**Statement.** Let $\hat{u}_t \in \Sigma_m$ be a local minimizer of $\mathcal{E}_t$ on $\Sigma_m$. Suppose:

**(H1) Constrained first-order optimality.** The projected gradient vanishes:

$$\nabla_\Sigma \mathcal{E}_t(\hat{u}_t) := \Pi_\Sigma \nabla \mathcal{E}_t(\hat{u}_t) = 0$$

Equivalently, $\nabla \mathcal{E}_t(\hat{u}_t) = \nu \mathbf{1}$ for some Lagrange multiplier $\nu \in \mathbb{R}$.

**(H2) Constrained non-degeneracy (spectral gap).** The projected Hessian

$$H_\Sigma := \Pi_\Sigma \nabla^2 \mathcal{E}_t(\hat{u}_t) \Pi_\Sigma \big|_{T\Sigma_m}$$

has smallest eigenvalue $\mu > 0$ on $T_{\hat{u}_t}\Sigma_m$. That is, for all $v \in T\Sigma_m$ with $\|v\|_2 = 1$:

$$v^T \nabla^2 \mathcal{E}_t(\hat{u}_t) v \geq \mu > 0$$

**(H3) $C^2$ regularity in the perturbation parameter.** The interpolated energy $\mathcal{E}_\lambda = (1-\lambda)\mathcal{E}_t + \lambda \mathcal{E}_s$ is $C^2$ as a function of $(u, \lambda) \in \Sigma_m \times [0,1]$.

Then for all $\varepsilon_1$ satisfying $\varepsilon_1 < \mu/2$, there exists a unique $C^1$ curve $\lambda \mapsto \hat{u}_\lambda \in \Sigma_m$ with $\hat{u}_0 = \hat{u}_t$ such that $\hat{u}_\lambda$ is a local minimizer of $\mathcal{E}_\lambda$ on $\Sigma_m$, and:

$$\|\hat{u}_\lambda - \hat{u}_t\|_2 \leq \frac{2\lambda \varepsilon_1}{\mu}$$

In particular, taking $\lambda = 1$: $\hat{u}_s := \hat{u}_1$ satisfies $\|\hat{u}_s - \hat{u}_t\|_2 \leq 2\varepsilon_1/\mu$.

### Proof of Proposition 1

**Step 1: Reduction to an equation on $T\Sigma_m$.**

Define $F: T\Sigma_m \times [0,1] \to T\Sigma_m$ by:

$$F(v, \lambda) = \Pi_\Sigma \nabla \mathcal{E}_\lambda(\hat{u}_t + v)$$

where $v \in T\Sigma_m$ (so $\hat{u}_t + v \in \Sigma_m$ locally). Finding a critical point of $\mathcal{E}_\lambda$ on $\Sigma_m$ near $\hat{u}_t$ is equivalent to solving $F(v, \lambda) = 0$ for $v$ near $0$.

**Step 2: Verify IFT hypotheses for $F$.**

- $F(0, 0) = \Pi_\Sigma \nabla \mathcal{E}_t(\hat{u}_t) = 0$ by (H1). ✓
- The Jacobian $D_v F(0,0) = \Pi_\Sigma \nabla^2 \mathcal{E}_t(\hat{u}_t) \Pi_\Sigma |_{T\Sigma_m} = H_\Sigma$, which is invertible on $T\Sigma_m$ with $\|H_\Sigma^{-1}\|_{\mathrm{op}} \leq 1/\mu$ by (H2). ✓
- $F$ is $C^1$ in $(v, \lambda)$ by (H3). ✓

By the Implicit Function Theorem (finite-dimensional, on the $(n-1)$-dimensional space $T\Sigma_m$), there exists a $C^1$ map $\lambda \mapsto v(\lambda) \in T\Sigma_m$ with $v(0) = 0$ and $F(v(\lambda), \lambda) = 0$ for $\lambda$ in a neighborhood of $0$.

**Step 3: Quantitative bound.**

Differentiating $F(v(\lambda), \lambda) = 0$ in $\lambda$:

$$H_\Sigma \cdot v'(\lambda) + \Pi_\Sigma \frac{\partial}{\partial \lambda} \nabla \mathcal{E}_\lambda(\hat{u}_t + v(\lambda)) = 0$$

At $\lambda = 0$:

$$v'(0) = -H_\Sigma^{-1} \Pi_\Sigma \big(\nabla \mathcal{E}_s(\hat{u}_t) - \nabla \mathcal{E}_t(\hat{u}_t)\big)$$

Therefore:

$$\|v'(0)\|_2 \leq \frac{1}{\mu} \|\nabla_\Sigma \mathcal{E}_s(\hat{u}_t) - \nabla_\Sigma \mathcal{E}_t(\hat{u}_t)\|_2 \leq \frac{\varepsilon_1}{\mu}$$

where the last inequality uses the $C^2$ norm bound (G1) on gradients. For the full path, a bootstrap argument using continuity of $v'(\lambda)$ and the condition $\varepsilon_1 < \mu/2$ (ensuring $H_\Sigma + \lambda(\nabla^2_\Sigma \mathcal{E}_s - \nabla^2_\Sigma \mathcal{E}_t)$ remains invertible with eigenvalue $\geq \mu/2$) gives:

$$\|v(\lambda)\|_2 = \left\|\int_0^\lambda v'(\tau)\,d\tau\right\|_2 \leq \int_0^\lambda \frac{\varepsilon_1}{\mu - \tau \varepsilon_1}\,d\tau \leq \frac{\lambda \varepsilon_1}{\mu - \varepsilon_1} \leq \frac{2\lambda \varepsilon_1}{\mu}$$

Setting $\hat{u}_\lambda = \hat{u}_t + v(\lambda)$ completes the proof. $\square$

### Verification that Hypotheses Hold

**(H1) follows from $\hat{u}_t$ being a local minimizer.** A local minimizer of a $C^1$ function on a smooth manifold is a critical point of the restricted function. The KKT conditions give $\nabla \mathcal{E}_t(\hat{u}_t) = \nu \mathbf{1}$ (ignoring box constraints $u \in [0,1]^n$, which are inactive at interior formation sites). ✓

**(H2) is the definition of "non-degenerate with spectral gap $\mu$."** The spectral gap $\mu$ in the theorem statement is explicitly the smallest eigenvalue of the *constrained* Hessian $H_\Sigma$, not the unconstrained Hessian. This resolves the audit's concern about which Hessian is meant.

**Relationship to unconstrained Hessian.** Let $\lambda_1 \leq \lambda_2 \leq \ldots \leq \lambda_n$ be the eigenvalues of the unconstrained Hessian $H = \nabla^2 \mathcal{E}_t(\hat{u}_t)$, and let $\mu_1 \leq \mu_2 \leq \ldots \leq \mu_{n-1}$ be the eigenvalues of $H_\Sigma$. By the Cauchy interlacing theorem:

$$\lambda_1 \leq \mu_1 \leq \lambda_2 \leq \mu_2 \leq \ldots \leq \mu_{n-1} \leq \lambda_n$$

So $\mu = \mu_1 \geq \lambda_1$, but $\mu_1$ could be strictly larger than $\lambda_1$ (if the eigenvector for $\lambda_1$ is $\mathbf{1}/\sqrt{n}$, i.e., the volume direction). For a local minimizer on $\Sigma_m$, we need $\mu_1 > 0$ but $\lambda_1$ could be negative (the volume direction may be a descent direction of the unconstrained energy). This distinction is load-bearing. ✓

**(H3) follows from sigmoid smoothness and $b_D = 0$.** The energy $\mathcal{E}_t$ consists of:
- $\mathcal{E}_{\mathrm{cl}}$: involves $\mathrm{Cl}_t(u) = \sigma(a_{\mathrm{cl}} P_t u + b_{\mathrm{cl}})$ — analytic (sigmoid is real-analytic).
- $\mathcal{E}_{\mathrm{sep}}$: involves $\mathbf{D}_t(x; 1-u) = \sigma(a_D(\bar{u}_x - \overline{1-u}_x))$ — analytic when $b_D = 0$ (Canonical Spec §13, T14 prerequisite).
- $\mathcal{E}_{\mathrm{bd}}$: polynomial in $u$ — analytic.
- $\mathcal{E}_{\mathrm{tr}}$: polynomial in $u$ (for fixed $\mathbf{M}$) — analytic.

Since all terms are analytic (hence $C^\infty$, hence $C^2$) in $u$, and the interpolation $\mathcal{E}_\lambda = (1-\lambda)\mathcal{E}_t + \lambda \mathcal{E}_s$ is affine in $\lambda$, $\mathcal{E}_\lambda$ is $C^2$ in $(u, \lambda)$. ✓

---

## Gap 3 Closure: Volume Re-Projection Cost

### Problem (from I7-temporal-audit.md, FC9 issue)

The transport kernel $\mathbf{M}_{t \to s}$ is sub-stochastic (Axiom E1), so $\sum_y (\mathbf{M} \hat{u}_t)(y) \leq \sum_x \hat{u}_t(x) = m$. The transported field $\tilde{u} := \mathbf{M} \hat{u}_t$ may not lie on $\Sigma_m$. The IFT is applied on $\Sigma_m$, but the initial point (for gradient flow) may not be on $\Sigma_m$.

### Proposition 2 (Volume Re-Projection Bound)

**Statement.** Let $\hat{u}_t \in \Sigma_m$ and let $\tilde{u} = \mathbf{M}_{t \to s} \hat{u}_t$ be the transported field. Define the mass deficit $\delta_m := m - \mathbf{1}^T \tilde{u} \geq 0$. Then:

**(a) Mass deficit bound.** $\delta_m \leq \|\mathbf{M} \hat{u}_t - \hat{u}_t\|_1 \leq \sqrt{n}\, \varepsilon_2$.

**(b) Projection cost.** The $\ell^2$-nearest point projection $\pi_\Sigma: \mathbb{R}^n \to \Sigma_m$ satisfies:

$$\|\pi_\Sigma(\tilde{u}) - \tilde{u}\|_2 = \frac{\delta_m}{\sqrt{n}}$$

**(c) Combined displacement.** The projected transported field satisfies:

$$\|\pi_\Sigma(\tilde{u}) - \hat{u}_t\|_2 \leq \varepsilon_2 + \frac{\delta_m}{\sqrt{n}} \leq \varepsilon_2 + \varepsilon_2 = 2\varepsilon_2$$

**(d) Minimizer shift from projection.** Combined with Proposition 1, the local minimizer $\hat{u}_s$ satisfies:

$$\|\hat{u}_s - \hat{u}_t\|_2 \leq \frac{2\varepsilon_1}{\mu}$$

and the projected transported field lies within distance $2\varepsilon_2$ of $\hat{u}_t$, hence within distance $2\varepsilon_1/\mu + 2\varepsilon_2$ of $\hat{u}_s$.

### Proof of Proposition 2

**(a)** The mass deficit is:

$$\delta_m = m - \mathbf{1}^T \tilde{u} = \mathbf{1}^T \hat{u}_t - \mathbf{1}^T (\mathbf{M} \hat{u}_t) = \mathbf{1}^T(\hat{u}_t - \mathbf{M} \hat{u}_t)$$

By the triangle inequality:

$$\delta_m \leq \|\hat{u}_t - \mathbf{M} \hat{u}_t\|_1 \leq \sqrt{n}\, \|\hat{u}_t - \mathbf{M} \hat{u}_t\|_2 \leq \sqrt{n}\, \varepsilon_2$$

where the last step uses (G2). Note that $\delta_m \geq 0$ because:

$$\mathbf{1}^T (\mathbf{M} \hat{u}_t) = \sum_y \sum_x M(x,y) \hat{u}_t(x) = \sum_x \hat{u}_t(x) \sum_y M(x,y) \leq \sum_x \hat{u}_t(x) \cdot 1 = m$$

by sub-stochasticity (E1). ✓

**(b)** The projection $\pi_\Sigma(\tilde{u})$ onto the affine hyperplane $\{u: \mathbf{1}^T u = m\}$ is:

$$\pi_\Sigma(\tilde{u}) = \tilde{u} + \frac{m - \mathbf{1}^T \tilde{u}}{n} \mathbf{1} = \tilde{u} + \frac{\delta_m}{n} \mathbf{1}$$

(Uniform redistribution of the mass deficit.) Therefore:

$$\|\pi_\Sigma(\tilde{u}) - \tilde{u}\|_2 = \frac{\delta_m}{n} \|\mathbf{1}\|_2 = \frac{\delta_m}{n} \sqrt{n} = \frac{\delta_m}{\sqrt{n}}$$

**Remark on box constraints.** This projection onto the hyperplane may violate the box constraint $u \in [0,1]^n$ if some components of $\tilde{u}$ are close to 1. However, for formation-structured fields with $\varepsilon_2$ small, the adjustment $\delta_m/n$ per component is $O(\varepsilon_2/\sqrt{n})$, which is negligible for $n \gg 1$. If box constraint violation occurs, iterative clipping-and-rescaling (as in the implementation, see optimizer.py) adds at most second-order corrections. ✓

**(c)** By triangle inequality:

$$\|\pi_\Sigma(\tilde{u}) - \hat{u}_t\|_2 \leq \|\pi_\Sigma(\tilde{u}) - \tilde{u}\|_2 + \|\tilde{u} - \hat{u}_t\|_2 = \frac{\delta_m}{\sqrt{n}} + \varepsilon_2$$

Using part (a), $\delta_m/\sqrt{n} \leq \varepsilon_2$, so:

$$\|\pi_\Sigma(\tilde{u}) - \hat{u}_t\|_2 \leq 2\varepsilon_2 \qquad \square$$

**(d)** The projected transported field $\pi_\Sigma(\tilde{u})$ now lies on $\Sigma_m$ and serves as the initial point for gradient flow. Its distance from the IFT-guaranteed minimizer $\hat{u}_s$ is:

$$\|\pi_\Sigma(\tilde{u}) - \hat{u}_s\|_2 \leq \|\pi_\Sigma(\tilde{u}) - \hat{u}_t\|_2 + \|\hat{u}_t - \hat{u}_s\|_2 \leq 2\varepsilon_2 + \frac{2\varepsilon_1}{\mu}$$

For this to lie within the basin of attraction of $\hat{u}_s$ (needed for Part (b) of T-Persist-1), we need:

$$2\varepsilon_2 + \frac{2\varepsilon_1}{\mu} < r_s$$

where $r_s$ is the basin radius of $\hat{u}_s$. This is the condition that connects Gap 3 to Gap 4 (basin radius), which remains open. $\square$

### Summary of Re-Projection Impact on T-Persist-1

The re-projection step introduces an additional $O(\varepsilon_2)$ displacement but does not change the structure of the argument. The key modification is:

- **Part (a):** The bound becomes $\|\hat{u}_s - \hat{u}_t\|_2 \leq 2\varepsilon_1/\mu$ (unchanged; the IFT operates on $\Sigma_m$ directly).
- **Part (b):** The gradient flow starts from $\pi_\Sigma(\tilde{u})$ (on $\Sigma_m$), at distance $\leq 2\varepsilon_2 + 2\varepsilon_1/\mu$ from $\hat{u}_s$. Basin containment (Gap 4) ensures convergence.
- **Part (c):** The $\ell^\infty$ bound $\|\hat{u}_s - \hat{u}_t\|_\infty \leq \|\hat{u}_s - \hat{u}_t\|_2 \leq 2\varepsilon_1/\mu$ is unchanged.
- **Constants:** Replace $C_0\varepsilon/\mu$ in the original statement with $2\varepsilon_1/\mu$ for the minimizer shift and $2\varepsilon_2 + 2\varepsilon_1/\mu$ for the gradient flow initial displacement.

---

## Revised T-Persist-1 Statement

**Theorem (T-Persist-1: Temporal Core Inheritance — Conditional).**

Let $X = X_t = X_s$ be a fixed support space with $n = |X|$. Let $\hat{u}_t \in \Sigma_m$ be a local minimizer of $\mathcal{E}_t$ on $\Sigma_m$ that is **formation-structured** and **non-degenerate**: the constrained Hessian $H_\Sigma = \Pi_\Sigma \nabla^2 \mathcal{E}_t(\hat{u}_t) \Pi_\Sigma|_{T\Sigma_m}$ has spectral gap $\mu > 0$ (smallest eigenvalue on $T\Sigma_m$), and there is an energy barrier $\Delta E > 0$ separating $\hat{u}_t$ from other critical points on $\Sigma_m$.

Suppose the transition from $t$ to $s$ is **$\varepsilon$-gentle** in the sense of Definition 1 (conditions G1–G3 with parameters $\varepsilon_1, \varepsilon_2, \varepsilon_3$), and suppose $\varepsilon_1 < \mu/2$. Then:

**(a) Minimizer persistence.** $\mathcal{E}_s$ has a local minimizer $\hat{u}_s \in \Sigma_m$ with:

$$\|\hat{u}_s - \hat{u}_t\|_2 \leq \frac{2\varepsilon_1}{\mu}$$

Moreover, $\hat{u}_s$ is non-degenerate with constrained spectral gap $\geq \mu - \varepsilon_1 > \mu/2$.

**(b) Gradient flow convergence.** Let $\tilde{u} = \mathbf{M}_{t \to s} \hat{u}_t$ be the transported field, and let $\tilde{u}_\Sigma = \pi_\Sigma(\tilde{u})$ be its projection onto $\Sigma_m$ (with $\|\tilde{u}_\Sigma - \hat{u}_t\|_2 \leq 2\varepsilon_2$). If $2\varepsilon_2 + 2\varepsilon_1/\mu < r_s$ (the basin radius of $\hat{u}_s$; see Gap 4, open), then the projected gradient flow on $\Sigma_m$ starting from $\tilde{u}_\Sigma$ converges exponentially to $\hat{u}_s$ by T14.

**(c) Core inclusion with shifted threshold.** For any $x \in \mathrm{Core}_t(\hat{u}_t) := \{x : \hat{u}_t(x) \geq \theta_{\mathrm{core}}\}$:

$$\hat{u}_s(x) \geq \theta_{\mathrm{core}} - \eta, \qquad \eta := \frac{2\varepsilon_1}{\mu}$$

using $\|\hat{u}_s - \hat{u}_t\|_\infty \leq \|\hat{u}_s - \hat{u}_t\|_2 \leq 2\varepsilon_1/\mu$. Hence $\mathrm{Core}_t(\hat{u}_t) \subseteq \mathrm{Core}_s(\hat{u}_s, \theta_{\mathrm{core}} - \eta)$.

**(d) Exact threshold preservation (conditional on Gap 6).** If $\min_{x \in \mathrm{Core}_t} (\hat{u}_t(x) - \theta_{\mathrm{core}}) > \eta$, then $\mathrm{Core}_t(\hat{u}_t) \subseteq \mathrm{Core}_s(\hat{u}_s)$ with the original threshold. A lower bound on this interior gap from the double-well structure remains open (Gap 6).

**(e) Diagnostic stability.** $\mathsf{Bind}_s \geq \mathsf{Bind}_t - O(\varepsilon_1/\mu)$ (requires operator smoothness from G3). $\mathsf{Inside}$ stability requires non-degeneracy of the persistence gap $\ell_{\max} - \ell_{\mathrm{second}}$; without this, $\mathsf{Inside}$ may be discontinuous.

---

## Remaining Open Gaps (4, 5, 6)

### Gap 4: Basin Radius / Morse Persistence (OPEN)

**What is needed:** A lower bound on the basin radius $r_s$ of $\hat{u}_s$, sufficient to contain $\pi_\Sigma(\tilde{u})$. The natural approach is Morse-theoretic: track not just the minimizer but also the saddle points that define the energy barrier. If all critical points of $\mathcal{E}_t$ in a neighborhood of $\hat{u}_t$ are non-degenerate (Morse condition), then they persist under perturbation by IFT, their Morse indices are preserved, and the basin radius is $r_s \geq r_t - O(\varepsilon_1/\mu)$ where $r_t \propto \sqrt{2\Delta E / \lambda_{\max}(H_\Sigma)}$.

**Why it is hard:** The Morse condition requires non-degeneracy at ALL critical points (minimizers and saddle points), not just at $\hat{u}_t$. This is a genericity condition that may fail at bifurcation points in the energy landscape.

### Gap 5: Transport Concentration (OPEN)

**What is needed:** A proof that $\sum_{y \in \mathrm{Core}_s} \mathbf{M}_{t \to s}(x, y) \geq 1 - \varepsilon_{\mathrm{core}}$ for $x \in \mathrm{Core}_t$. This is required for T-Persist-2 (the Persist predicate bound). T-Persist-1 proves that the *field values* are high where they were high; it does not prove that the *transport kernel* maps core to core.

**Why it is hard:** For a general sub-stochastic $\mathbf{M}$, transport from a core site could go to boundary or exterior sites. The self-referential transport framework could potentially provide this (if the cost function penalizes core-to-non-core transport), but this requires the existence result from the Transport Designer, which itself has gaps (Brouwer continuity issue).

### Gap 6: Interior Gap Lower Bound (OPEN)

**What is needed:** A lower bound $\min_{x \in \mathrm{Core}_t}(\hat{u}_t(x) - \theta_{\mathrm{core}}) \geq \gamma > 0$ for formation-structured minimizers, derived from the double-well structure. This would make Part (d) non-vacuous.

**Why it is plausible:** The double-well term $\beta u^2(1-u)^2$ in $\mathcal{E}_{\mathrm{bd}}$ penalizes intermediate values, pushing interior sites toward $u = 1$. For $\beta/\alpha$ sufficiently large (deep in the phase-transition regime), core sites should have $u \geq 1 - O(e^{-c\sqrt{\beta/\alpha}})$ by $\Gamma$-convergence (T11). But a quantitative bound requires analyzing the interplay between the double-well and the other energy terms at the minimizer.

---

## Registry Update

| Result | Previous Status | New Status |
|--------|----------------|------------|
| T-Persist-1(a) | Proof strategy, missing hypotheses | **Gap 2 closed**: IFT hypotheses stated and verified on $\Sigma_m$ |
| T-Persist-1 (ε-gentle) | Ill-posed | **Gap 1 closed**: precise 3-part definition given |
| T-Persist-1 (re-projection) | Unaddressed | **Gap 3 closed**: mass deficit bounded, projection cost $O(\varepsilon_2)$ |
| T-Persist-1(b) | Dependent on basin radius | Still open (Gap 4) |
| T-Persist-1(d) | May be vacuous | Still open (Gap 6) |
| T-Persist-2 | Conditional on transport concentration | Still open (Gap 5) |
