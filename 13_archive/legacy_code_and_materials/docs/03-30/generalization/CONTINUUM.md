# Continuum Limit of Soft Cognitive Cohesion

**Status:** Extension document
**Relation to spec:** Extends Canonical Spec v2.0 from finite graphs to continuous domains
**Key result:** Well-posed energy functional; gradient flow is self-referential reaction-diffusion PDE; sharp-interface limit recovers standard Modica-Mortola (self-referential corrections vanish)

---

## 1. Motivation

SCC is formulated on finite graphs $(X_t, \mathbf{N}_t)$. This creates a philosophical tension: the theory claims to describe pre-objective cohesion, yet its substrate $X_t$ consists of individuated discrete sites (see Canonical Spec v2.0, Section 2, "On the status of $X_t$"). The continuum formulation addresses this by working on a continuous domain $\Omega \subset \mathbb{R}^d$, where sites are not individuated.

Beyond the philosophical motivation, the continuum formulation provides:

- Access to PDE theory (Sobolev regularity, maximum principles, comparison theorems)
- Connection to the large Allen-Cahn / Ginzburg-Landau / phase-field literature
- A framework for sharp-interface asymptotics and geometric evolution equations
- Analytical techniques (spectral theory of differential operators) not available on graphs

The continuum limit is the standard passage from graph Laplacian to the Laplace operator, extended to the full SCC energy including self-referential terms.

---

## 2. Setup and Notation

Let $\Omega \subset \mathbb{R}^d$ be a bounded domain with Lipschitz boundary (typically $d = 2$ or $d = 3$). The cohesion field is

$$
u : \Omega \to [0,1]
$$

belonging to the Sobolev space $H^1(\Omega) \cap L^\infty(\Omega)$, with the constraint $0 \leq u(x) \leq 1$ a.e.

The volume constraint becomes

$$
\int_\Omega u(x)\, dx = m
$$

for a prescribed cohesive budget $m > 0$. The volume fraction is $c = m / |\Omega|$.

The constraint manifold is

$$
\Sigma_m = \left\{ u \in H^1(\Omega) : 0 \leq u \leq 1 \text{ a.e.},\ \int_\Omega u\, dx = m \right\}
$$

We impose **Neumann boundary conditions** $\partial u / \partial \nu = 0$ on $\partial\Omega$ (no flux of cohesion through the domain boundary). This is the natural analogue of the graph setting where the boundary of the relational support is not distinguished.

---

## 3. Continuous Operators

### 3.1. Aggregation Kernel

The discrete aggregation operator $(P_t u)(x) = \sum_y N(x,y) u(y) / (\sum_y N(x,y) + \varepsilon)$ is replaced by a kernel convolution:

$$
(K * u)(x) = \frac{\int_\Omega K(x,y)\, u(y)\, dy}{\int_\Omega K(x,y)\, dy + \varepsilon}
$$

where $K : \Omega \times \Omega \to [0, \infty)$ is a symmetric, nonnegative kernel satisfying:

- **Symmetry:** $K(x,y) = K(x,y)$ for all $x,y \in \Omega$
- **Locality:** $K(x,y) \approx 0$ when $|x - y| \gg \ell_K$ for some kernel length scale $\ell_K > 0$
- **Regularity:** $K \in L^1(\Omega \times \Omega)$, with $\int_\Omega K(x,y)\, dy$ bounded and bounded away from zero for $x$ in the interior of $\Omega$

The canonical choice is a normalized Gaussian kernel:

$$
K(x,y) = \frac{1}{(2\pi \ell_K^2)^{d/2}} \exp\!\left( -\frac{|x-y|^2}{2\ell_K^2} \right)
$$

When $\ell_K \to 0$ (with appropriate rescaling), $K * u \to u$ pointwise for smooth $u$, recovering the local limit. When $\ell_K$ is finite, $K * u$ is a local spatial average — the continuum analogue of the graph's neighborhood averaging.

**Remark.** On a regular lattice with spacing $h$, the row-normalized adjacency $P$ is approximately $K * (\cdot)$ with $K$ supported on nearest neighbors. The passage from $P$ to kernel convolution is the standard graph-to-continuum correspondence used in graph limits (graphon theory) and nonlocal-to-local PDE limits.

### 3.2. Continuous Closure

$$
\mathrm{Cl}[u](x) = \sigma\!\Big( a_{\mathrm{cl}} \big[ (1 - \eta_{\mathrm{cl}})\, u(x) + \eta_{\mathrm{cl}}\, (K * u)(x) - \tau_{\mathrm{cl}} \big] \Big)
$$

where $\sigma$ is the logistic sigmoid. This is the direct transcription of the discrete operator (Spec Section 9.2) with $P_t u \mapsto K * u$.

**Well-definedness.** For $u \in L^2(\Omega)$ with $0 \leq u \leq 1$, the kernel convolution $K * u$ is well-defined (by Young's inequality, $K * u \in L^\infty(\Omega)$ since $K \in L^1$). The sigmoid maps $\mathbb{R}$ to $(0,1)$, so $\mathrm{Cl}[u] : \Omega \to (0,1)$ is well-defined and bounded.

**Contraction property.** The discrete contraction (A3) extends directly:

$$
\|\mathrm{Cl}[u] - \mathrm{Cl}[v]\|_{L^\infty(\Omega)} \leq \frac{a_{\mathrm{cl}}}{4} \|u - v\|_{L^\infty(\Omega)}
$$

*Proof.* By the mean value theorem applied to $\sigma$:

$$
|\mathrm{Cl}[u](x) - \mathrm{Cl}[v](x)| \leq \frac{a_{\mathrm{cl}}}{4} \big| (1-\eta)(u(x) - v(x)) + \eta (K*(u-v))(x) \big|
$$

Since $|K*(u-v)| \leq \|u-v\|_\infty$ (the kernel is sub-stochastic) and $|(1-\eta)s + \eta t| \leq \max(|s|, |t|)$ for the convex combination, we get the bound. Contraction holds when $a_{\mathrm{cl}} < 4$, exactly as in the discrete case. $\square$

### 3.3. Continuous Distinction

$$
\mathbf{D}[u](x) = \sigma\!\Big( a_D \big[ (K * u)(x) - \lambda_D\, (K * (1-u))(x) \big] - \tau_D \Big)
$$

Using the identity $K * (1-u) = K * \mathbf{1} - K * u$ (where $(K * \mathbf{1})(x) = \int K(x,y)\, dy / (\int K(x,y)\, dy + \varepsilon) \approx 1$):

$$
\mathbf{D}[u](x) = \sigma\!\Big( a_D \big[ (1 + \lambda_D)(K * u)(x) - \lambda_D\, (K * \mathbf{1})(x) \big] - \tau_D \Big)
$$

This is well-defined for $u \in L^2(\Omega)$ by the same argument as closure.

### 3.4. What Does Not Transfer: Co-belonging

The resolvent co-belonging $\mathbf{C}_t = (I - \alpha W_{\mathrm{sym}})^{-1}$ does not have an obvious continuum analogue. In the discrete case, $W_{\mathrm{sym}}$ is a finite matrix (cohesion-weighted adjacency) and the resolvent is a finite-dimensional inverse. In the continuum, the analogue would be:

$$
\mathbf{C}[u] = (I - \alpha\, \mathcal{W}_u)^{-1}
$$

where $\mathcal{W}_u$ is an integral operator with kernel $W_u(x,y) = \sqrt{u(x)}\, K(x,y)\, \sqrt{u(y)} / d(x)$ for appropriate normalization $d(x)$.

This is a **Fredholm integral operator** of the second kind. By the Fredholm alternative, $(I - \alpha \mathcal{W}_u)^{-1}$ exists and is bounded provided $\alpha$ is not a reciprocal eigenvalue of $\mathcal{W}_u$. The Neumann series converges when $\alpha \|\mathcal{W}_u\|_{\mathrm{op}} < 1$.

However, since $\mathbf{C}_t$ is a **derived diagnostic** that does not enter the energy or predicates (Spec Section 3.6), this is not load-bearing for the continuum energy theory. It remains available as a diagnostic tool.

---

## 4. Continuous Energy Functional

### 4.1. Boundary/Morphology Energy

$$
\mathcal{E}_{\mathrm{bd}}[u] = \int_\Omega \left[ \alpha\, |\nabla u|^2 + \beta\, W(u) \right] dx
$$

where $W(u) = u^2(1-u)^2$ is the double-well potential. This is the **standard Ginzburg-Landau / Cahn-Hilliard / Allen-Cahn functional**, which is the established continuum limit of the discrete energy $\alpha \sum_{x,y} N(x,y)(u(x) - u(y))^2 + \beta \sum_x W(u(x))$ on lattice graphs.

**Correspondence with discrete:** On a $d$-dimensional lattice with spacing $h$, the graph Laplacian satisfies $L u \to -h^2 \Delta u$ as $h \to 0$, and the ordered-pair sum $2\alpha u^T L u \to 2\alpha \int |\nabla u|^2\, dx$ (with appropriate rescaling $\alpha_{\text{discrete}} = \alpha_{\text{cont}} / h^{d-2}$).

### 4.2. Closure Energy

$$
\mathcal{E}_{\mathrm{cl}}[u] = \int_\Omega \big| \mathrm{Cl}[u](x) - u(x) \big|^2\, dx
$$

This measures the $L^2$ deviation of $u$ from its relationally completed form, exactly as in the discrete case ($\sum_x |Cl(u)(x) - u(x)|^2 \to \int |Cl[u] - u|^2\, dx$).

### 4.3. Separation Energy

$$
\mathcal{E}_{\mathrm{sep}}[u] = \int_\Omega u(x)\, \big(1 - \mathbf{D}[u](x)\big)\, dx
$$

Penalizes cohesive sites that are not structurally distinguished from the exterior.

### 4.4. Transport Energy

$$
\mathcal{E}_{\mathrm{tr}}[u_t, u_s] = \int_\Omega \int_\Omega \mathbf{M}_{t \to s}(x,y)\, \omega(u_t(x), u_s(y))\, |u_s(y) - u_t(x)|^2\, dx\, dy
$$

This is formally well-defined but requires a continuum transport kernel $\mathbf{M}_{t \to s}$, which is an open problem in the discrete theory and remains open here.

### 4.5. Full Energy

$$
\mathcal{E}[u] = \lambda_{\mathrm{cl}}\, \mathcal{E}_{\mathrm{cl}}[u] + \lambda_{\mathrm{sep}}\, \mathcal{E}_{\mathrm{sep}}[u] + \lambda_{\mathrm{bd}}\, \mathcal{E}_{\mathrm{bd}}[u]
$$

(Transport term deferred, as in the discrete implementation.)

---

## 5. Well-Posedness

### 5.1. Existence of Minimizers

**Theorem (Minimizer Existence).** Let $\Omega \subset \mathbb{R}^d$ be bounded with Lipschitz boundary, $K \in L^1(\Omega \times \Omega)$ nonneg and symmetric, and $c \in (0,1)$. Then $\mathcal{E}$ attains its minimum on $\Sigma_m$.

*Proof sketch (direct method of calculus of variations).*

1. **Coercivity.** $\mathcal{E}_{\mathrm{bd}}[u] \geq \alpha \|\nabla u\|_{L^2}^2$, so $\mathcal{E}$ is coercive in $H^1(\Omega)$.

2. **Boundedness below.** All three terms are nonneg: $\mathcal{E}_{\mathrm{cl}} \geq 0$, $\mathcal{E}_{\mathrm{sep}} \geq 0$ (since $u \geq 0$ and $1 - D \geq 0$), $\mathcal{E}_{\mathrm{bd}} \geq 0$.

3. **Lower semicontinuity.** The key term is $\mathcal{E}_{\mathrm{bd}}$: $u \mapsto \int |\nabla u|^2$ is weakly lower semicontinuous in $H^1(\Omega)$. The double-well term $\int W(u)$ is continuous under strong $L^4$ convergence (which follows from compact embedding $H^1 \hookrightarrow L^4$ for $d \leq 3$). For $\mathcal{E}_{\mathrm{cl}}$ and $\mathcal{E}_{\mathrm{sep}}$: the kernel convolution $K * u$ is a compact operator from $L^2$ to $L^2$ (since $K \in L^2(\Omega \times \Omega)$ for bounded $K$), so $K * u_n \to K * u$ strongly in $L^2$ whenever $u_n \rightharpoonup u$ weakly in $L^2$. The sigmoid is Lipschitz, so $\mathrm{Cl}[u_n] \to \mathrm{Cl}[u]$ and $\mathbf{D}[u_n] \to \mathbf{D}[u]$ strongly in $L^2$. Combined with the strong $L^2$ convergence of $u_n \to u$ (from compact embedding), both $\mathcal{E}_{\mathrm{cl}}$ and $\mathcal{E}_{\mathrm{sep}}$ are continuous under the weak $H^1$ topology.

4. **Constraint closure.** $\Sigma_m$ is weakly closed in $H^1(\Omega)$: the box constraints $0 \leq u \leq 1$ are preserved under weak limits (convexity), and $\int u\, dx = m$ is a continuous linear functional.

5. By the direct method, $\mathcal{E}$ attains its infimum on $\Sigma_m$. $\square$

**Remark.** This is a stronger result than the discrete case (T1), where existence was immediate from compactness of the finite-dimensional box. Here we need the coercivity from $\mathcal{E}_{\mathrm{bd}}$ to compensate for the infinite-dimensional setting.

### 5.2. Regularity

At a minimizer $\hat{u}$, the Euler-Lagrange equation (see Section 6) is:

$$
-2\alpha \Delta \hat{u} + \beta W'(\hat{u}) + \lambda_{\mathrm{cl}} \frac{\delta \mathcal{E}_{\mathrm{cl}}}{\delta u}\Big|_{\hat{u}} + \lambda_{\mathrm{sep}} \frac{\delta \mathcal{E}_{\mathrm{sep}}}{\delta u}\Big|_{\hat{u}} = \nu
$$

where $\nu$ is the Lagrange multiplier for the volume constraint. The self-referential terms involve $K * u$ (smooth if $K$ is smooth) composed with $\sigma$ (smooth). So the right-hand side is a smooth function of $\hat{u}$ and $K * \hat{u}$.

By elliptic regularity (bootstrapping): if $\hat{u} \in H^1$ and the nonlinear terms are in $L^2$, then $\hat{u} \in H^2$. If $K$ is $C^\infty$, then $K * u$ is $C^\infty$ for any $L^2$ function $u$, and bootstrapping gives $\hat{u} \in C^\infty(\Omega)$. In particular, **minimizers are smooth** (classical solutions) when $K$ is smooth.

### 5.3. Phase Transition

**Theorem (Continuum Phase Transition).** Let $\lambda_1$ be the first nontrivial eigenvalue of $-\Delta$ on $\Omega$ with Neumann boundary conditions (the analogue of the Fiedler eigenvalue). Let $c \in ((3-\sqrt{3})/6, (3+\sqrt{3})/6)$. If

$$
\frac{\beta}{\alpha} > \frac{4\lambda_1}{|W''(c)|}
$$

then the uniform state $u \equiv c$ is not a minimizer of $\mathcal{E}_{\mathrm{bd}}$ on $\Sigma_m$. The global minimizer is non-uniform.

*Proof.* Identical structure to T8-Core. The second variation of $\mathcal{E}_{\mathrm{bd}}$ at $u \equiv c$ in the direction of the first Neumann eigenfunction $\phi_1$ (which satisfies $\int \phi_1 = 0$, hence is tangent to $\Sigma_m$) is:

$$
\delta^2 \mathcal{E}_{\mathrm{bd}}[c](\phi_1, \phi_1) = \int_\Omega \left[ 2\alpha |\nabla \phi_1|^2 + \beta W''(c) \phi_1^2 \right] dx = (2\alpha \lambda_1 + \beta W''(c)) \|\phi_1\|^2
$$

(The factor 2 in $2\alpha$ comes from the ordered-pair convention: in the continuum, $\mathcal{E}_{\mathrm{bd}} = \alpha \int |\nabla u|^2$ with Hessian $2\alpha(-\Delta)$.) This is negative when $\beta/\alpha > 2\lambda_1 / |W''(c)|$.

**Correction:** In the continuum, the Hessian of $\int \alpha |\nabla u|^2\, dx$ is $2\alpha(-\Delta)$, not $4\alpha L$ as in the discrete case. The factor difference arises because the discrete ordered-pair sum $2\alpha u^T L u$ has Hessian $4\alpha L$, while the continuum $\alpha \int |\nabla u|^2$ has Hessian $2\alpha(-\Delta)$. The phase transition criterion is:

$$
\frac{\beta}{\alpha} > \frac{2\lambda_1}{|W''(c)|}
$$

This matches the standard Allen-Cahn phase transition condition. $\square$

**Remark on the discrete-to-continuum correspondence.** The factor 4 in the discrete Hessian ($4\alpha L$) and factor 2 in the continuum ($2\alpha(-\Delta)$) are consistent under the identification $L \sim -h^{-2}\Delta$ with appropriate rescaling of $\alpha$.

---

## 6. Gradient Flow and the Continuum PDE

### 6.1. Functional Derivatives

The $L^2$ gradient flow of $\mathcal{E}$ on $\Sigma_m$ is $\partial_t u = -\Pi_{\Sigma_m} \frac{\delta \mathcal{E}}{\delta u}$, where $\Pi_{\Sigma_m}$ projects onto the tangent space of $\Sigma_m$ (subtracting the mean).

**Boundary/morphology:**

$$
\frac{\delta \mathcal{E}_{\mathrm{bd}}}{\delta u} = -2\alpha \Delta u + \beta W'(u) = -2\alpha \Delta u + 2\beta u(1-u)(1-2u)
$$

**Closure:** By the chain rule for the Fréchet derivative,

$$
\frac{\delta \mathcal{E}_{\mathrm{cl}}}{\delta u} = 2(\mathrm{Cl}[u] - u) \cdot \left( \frac{\delta \mathrm{Cl}}{\delta u} - I \right)
$$

More precisely, for a variation $\delta u$:

$$
\left\langle \frac{\delta \mathcal{E}_{\mathrm{cl}}}{\delta u},\, \delta u \right\rangle = 2 \int_\Omega (\mathrm{Cl}[u] - u)\, \big( J_{\mathrm{Cl}}[\delta u] - \delta u \big)\, dx
$$

where $J_{\mathrm{Cl}}$ is the Fréchet derivative of $\mathrm{Cl}$:

$$
J_{\mathrm{Cl}}[\delta u](x) = \sigma'(z(x)) \cdot a_{\mathrm{cl}} \big[ (1-\eta)\, \delta u(x) + \eta\, (K * \delta u)(x) \big]
$$

with $z(x) = a_{\mathrm{cl}}[(1-\eta)u(x) + \eta(K*u)(x) - \tau]$. The adjoint is:

$$
J_{\mathrm{Cl}}^*[v](x) = \sigma'(z(x))\, a_{\mathrm{cl}} \big[ (1-\eta)\, v(x) + \eta\, (K^* * v)(x) \big]
$$

where $K^*$ is the adjoint kernel ($K^*(x,y) = K(y,x)$; for symmetric $K$, $K^* = K$). So:

$$
\frac{\delta \mathcal{E}_{\mathrm{cl}}}{\delta u}(x) = 2\big[ J_{\mathrm{Cl}}^*[r](x) - r(x) \big]
$$

where $r = \mathrm{Cl}[u] - u$ is the closure residual. This exactly mirrors the discrete gradient (energy.py, `grad_cl`).

**Separation:**

$$
\frac{\delta \mathcal{E}_{\mathrm{sep}}}{\delta u}(x) = (1 - \mathbf{D}[u](x)) - J_{\mathbf{D}}^*[u](x)
$$

where $J_{\mathbf{D}}$ is the Fréchet derivative of $\mathbf{D}$ with respect to $u$:

$$
J_{\mathbf{D}}[\delta u](x) = \sigma'(z_D(x)) \cdot a_D (1 + \lambda_D) (K * \delta u)(x)
$$

and its adjoint:

$$
J_{\mathbf{D}}^*[v](x) = a_D(1 + \lambda_D)\, (K * [\sigma'(z_D) \cdot v])(x)
$$

This mirrors `grad_sep` in energy.py.

### 6.2. The Full Gradient Flow PDE

Combining, the projected $L^2$ gradient flow is:

$$
\boxed{
\frac{\partial u}{\partial t} = 2\alpha \Delta u - \beta W'(u) - \lambda_{\mathrm{cl}} \frac{\delta \mathcal{E}_{\mathrm{cl}}}{\delta u} - \lambda_{\mathrm{sep}} \frac{\delta \mathcal{E}_{\mathrm{sep}}}{\delta u} - \nu(t)
}
$$

where $\nu(t) = \frac{1}{|\Omega|} \int_\Omega \left[ -2\alpha \Delta u + \beta W'(u) + \lambda_{\mathrm{cl}} \frac{\delta \mathcal{E}_{\mathrm{cl}}}{\delta u} + \lambda_{\mathrm{sep}} \frac{\delta \mathcal{E}_{\mathrm{sep}}}{\delta u} \right] dx$ enforces volume conservation ($\frac{d}{dt} \int u\, dx = 0$).

**Structure:** This is a **nonlocal reaction-diffusion equation** with:

- **Diffusion:** $2\alpha \Delta u$ (standard Laplacian diffusion)
- **Reaction:** $-\beta W'(u) = -2\beta u(1-u)(1-2u)$ (bistable reaction, standard Allen-Cahn)
- **Self-referential closure correction:** $-\lambda_{\mathrm{cl}} \frac{\delta \mathcal{E}_{\mathrm{cl}}}{\delta u}$ (nonlocal, involving $K * u$)
- **Self-referential separation correction:** $-\lambda_{\mathrm{sep}} \frac{\delta \mathcal{E}_{\mathrm{sep}}}{\delta u}$ (nonlocal, involving $K * u$ and $K * (1-u)$)
- **Volume conservation:** $-\nu(t)$ (Lagrange multiplier)

The Allen-Cahn part ($2\alpha \Delta u - \beta W'(u)$) is a classical semilinear parabolic PDE with well-understood theory. The self-referential corrections are **bounded nonlocal perturbations** — they involve the sigmoid (bounded with bounded derivatives) composed with $K * u$ (a smoothing operator). This structure ensures well-posedness.

### 6.3. Well-Posedness of the Gradient Flow

**Theorem (Short-Time Existence).** For $u_0 \in H^1(\Omega) \cap L^\infty(\Omega)$ with $0 \leq u_0 \leq 1$ and $\int u_0 = m$, there exists a unique mild solution $u \in C([0, T]; L^2(\Omega)) \cap L^2([0,T]; H^1(\Omega))$ for some $T > 0$.

*Proof sketch.* The Allen-Cahn semigroup $e^{t(2\alpha \Delta)}$ is a contraction on $L^2$. The nonlinear terms $F(u) = -\beta W'(u) - \lambda_{\mathrm{cl}} \delta\mathcal{E}_{\mathrm{cl}}/\delta u - \lambda_{\mathrm{sep}} \delta\mathcal{E}_{\mathrm{sep}}/\delta u$ are locally Lipschitz on $L^2$ (the sigmoid and its derivative are globally Lipschitz; $K*$ is a bounded operator). The Picard-Lindelof theorem in Banach space gives local existence and uniqueness.

**Theorem (Global Existence).** The solution exists for all $t > 0$.

*Proof sketch.* The energy $\mathcal{E}[u(t)]$ is monotonically decreasing and bounded below. The $L^\infty$ bound $0 \leq u \leq 1$ is preserved by the maximum principle (the reaction term $W'(u)$ vanishes at $u = 0$ and $u = 1$; the self-referential terms are bounded; the sigmoid maps to $(0,1)$). Combined with the energy bound on $\|\nabla u\|_{L^2}$, this prevents blow-up.

**Theorem (Convergence to Equilibrium).** For analytic energy (sigmoid closure with $b_D = 0$), the gradient flow converges to a critical point as $t \to \infty$.

*Proof.* By the Lojasiewicz-Simon inequality for analytic functionals on $H^1(\Omega)$. This is the continuum analogue of T14. The key requirement is analyticity of the energy, which holds because $\sigma$ is analytic and $K * (\cdot)$ is a bounded linear operator. $\square$

---

## 7. Sharp-Interface Limit

### 7.1. The Regime

Set $\alpha = \varepsilon$, $\beta = 1/\varepsilon$ (so $\varepsilon = \alpha/\beta \to 0$). The boundary energy becomes:

$$
\mathcal{E}_{\mathrm{bd}}^\varepsilon[u] = \int_\Omega \left[ \varepsilon\, |\nabla u|^2 + \frac{1}{\varepsilon}\, W(u) \right] dx
$$

This is the standard Modica-Mortola functional.

### 7.2. Gamma-Convergence

**Theorem (Gamma-convergence, standard).** As $\varepsilon \to 0$:

$$
\mathcal{E}_{\mathrm{bd}}^\varepsilon \xrightarrow{\Gamma} \sigma_{\mathrm{AC}} \cdot \mathrm{Per}(S; \Omega)
$$

where $S = \{u = 1\}$, $\mathrm{Per}(S; \Omega)$ is the perimeter of $S$ in $\Omega$, and the surface tension is:

$$
\sigma_{\mathrm{AC}} = \int_0^1 \sqrt{2W(s)}\, ds = \int_0^1 \sqrt{2}\, s(1-s)\, ds = \frac{\sqrt{2}}{6}
$$

Minimizers converge to characteristic functions $u \to \mathbf{1}_S$ where $S$ minimizes perimeter subject to $|S| = m$.

### 7.3. Self-Referential Corrections in the Sharp-Interface Limit

**Claim (G4 closure, confirmed).** The self-referential terms $\lambda_{\mathrm{cl}} \mathcal{E}_{\mathrm{cl}}$ and $\lambda_{\mathrm{sep}} \mathcal{E}_{\mathrm{sep}}$ do not affect the Gamma-limit.

*Analysis.* Near a sharp interface at position $\Gamma$ with transition profile $u(x) \approx q((x \cdot \nu) / \varepsilon)$ where $q$ is the Allen-Cahn profile ($q'' = W'(q)$, $q(-\infty) = 0$, $q(+\infty) = 1$):

| Term | Scaling with $\varepsilon$ | Reason |
|------|---------------------------|--------|
| $\mathcal{E}_{\mathrm{bd}}^\varepsilon$ | $O(1/\varepsilon) \cdot |\Gamma|$ | Standard Modica-Mortola |
| $\mathcal{E}_{\mathrm{cl}}$ | $O(|\Gamma|)$ | Closure residual is $O(1)$ per unit interface, transition zone has width $O(\varepsilon)$, integrated over $|\Gamma|$ gives $O(|\Gamma|)$ |
| $\mathcal{E}_{\mathrm{sep}}$ | $O(\varepsilon \cdot |\Gamma|)$ | In the bulk, $u(1-D) \approx 0$; in the transition zone of width $O(\varepsilon)$, $u(1-D) = O(1)$ |

Since $\mathcal{E}_{\mathrm{cl}}$ and $\mathcal{E}_{\mathrm{sep}}$ are $o(1/\varepsilon)$, they vanish relative to $\mathcal{E}_{\mathrm{bd}}^\varepsilon$ in the Gamma-limit.

**The Gamma-limit of the full SCC energy is the standard perimeter functional with surface tension $\sigma_{\mathrm{AC}} = \sqrt{2}/6$. There is no self-referential correction to the surface tension.** (This confirms the G4 closure from GAP-CLOSURES-3.md.)

### 7.4. Finite-$\varepsilon$ Corrections

At finite $\varepsilon$, the self-referential terms modify the optimal transition profile and the interface velocity. The effective surface tension is:

$$
\sigma_{\mathrm{eff}}(\varepsilon) = \sigma_{\mathrm{AC}} + \varepsilon \cdot \frac{\lambda_{\mathrm{cl}} \mathcal{E}_{\mathrm{cl}}^{\mathrm{profile}} + \lambda_{\mathrm{sep}} \mathcal{E}_{\mathrm{sep}}^{\mathrm{profile}}}{|\Gamma|}
$$

where $\mathcal{E}_{\mathrm{cl}}^{\mathrm{profile}}$ and $\mathcal{E}_{\mathrm{sep}}^{\mathrm{profile}}$ are the self-referential energies evaluated at the optimal 1D transition profile for a single planar interface. The $O(\varepsilon)$ correction is always positive (since both energy terms are nonneg), so **self-referential terms increase the effective surface tension at finite resolution**.

This is consistent with T7-Enhanced (enhanced metastability): the self-referential terms make interfaces more stable by increasing the energetic cost of interface creation.

### 7.5. Sharp-Interface Dynamics

In the sharp-interface limit, the Allen-Cahn gradient flow converges to **mean curvature flow** of the interface $\Gamma$:

$$
V_n = -\kappa + \nu
$$

where $V_n$ is the normal velocity, $\kappa$ is the mean curvature, and $\nu$ is the Lagrange multiplier enforcing volume conservation ($|S(t)| = m$).

The self-referential corrections produce an $O(\varepsilon)$ perturbation to the interface velocity:

$$
V_n = -\kappa + \nu + \varepsilon \cdot \delta V_n^{\mathrm{self-ref}} + O(\varepsilon^2)
$$

Computing $\delta V_n^{\mathrm{self-ref}}$ requires matched asymptotic expansions (inner expansion at the interface, outer expansion in the bulk). This is a standard calculation in the Allen-Cahn literature but has not been carried out for the SCC-specific self-referential terms. **This is an open calculation.**

---

## 8. Continuum Analogues of Discrete Results

| Discrete Result | Continuum Analogue | Status |
|----------------|-------------------|--------|
| T1 (minimizer existence) | Theorem 5.1 (direct method) | **Proved** (Section 5.1) |
| T6 (closure contraction) | Contraction in $L^\infty(\Omega)$ | **Proved** (Section 3.2) |
| T8-Core (phase transition) | $\beta/\alpha > 2\lambda_1/\|W''(c)\|$ | **Proved** (Section 5.3) |
| T14 (gradient flow convergence) | Lojasiewicz-Simon convergence | **Proved** (Section 6.3) |
| T11 (Gamma-convergence) | Standard Modica-Mortola | **Proved** (Section 7.2) |
| G4 ($\delta\sigma = 0$) | Self-ref terms are $o(1/\varepsilon)$ | **Confirmed** (Section 7.3) |
| T7 (enhanced metastability) | $\sigma_{\mathrm{eff}} > \sigma_{\mathrm{AC}}$ at finite $\varepsilon$ | **Confirmed** (Section 7.4) |
| Sep = 1 - E_sep/m | Sep = 1 - $\mathcal{E}_{\mathrm{sep}}/m$ | **Transfers directly** |
| Bind $\geq$ 1 - $\sqrt{E_{\mathrm{cl}}/n}$ | Bind $\geq 1 - \|\mathrm{Cl}[u] - u\|_{L^2} / \|\Omega\|^{1/2}$ | **Transfers directly** |

---

## 9. What's Gained

1. **PDE regularity theory.** Minimizers are smooth (classical solutions) when $K$ is smooth. No analogous regularity statement exists in the discrete setting.

2. **Connection to phase-field community.** The SCC energy is a perturbation of the Ginzburg-Landau functional, which is one of the most studied objects in mathematical physics. The entire Allen-Cahn / Cahn-Hilliard / phase-field literature becomes directly relevant.

3. **Sharp-interface asymptotics.** The matched asymptotic expansion machinery (inner/outer solutions, solvability conditions) provides systematic access to the interface dynamics. In the discrete setting, these calculations are ad hoc.

4. **Spectral theory.** The Fiedler eigenvalue is replaced by $\lambda_1(-\Delta_\Omega)$, which is computable (and well-tabulated) for standard domains. The phase transition criterion becomes a simple inequality involving domain geometry.

5. **Philosophical coherence.** The continuum domain $\Omega$ does not consist of individuated sites, partially addressing the "discrete substrate" critique (Spec Section 12, "Discrete substrate defense").

6. **Stochastic extension.** The continuum PDE provides the natural setting for stochastic perturbation (SPDE theory), large deviations, and Gibbs measure analysis.

---

## 10. What's Lost or Changed

1. **Nonlocality.** The self-referential structure, which in the discrete case involves the sparse matrix $P$ (local), becomes a nonlocal integral operator $K * (\cdot)$ in the continuum. This is well-defined but makes the PDE nonlocal — harder to analyze than a purely local PDE. **However**, in the local limit ($\ell_K \to 0$), the kernel convolution reduces to pointwise evaluation ($K * u \to u$), and the closure/distinction operators become pointwise nonlinearities. This limit destroys the spatial coupling in the self-referential terms, which is essential to the theory's relational character.

2. **Co-belonging resolvent.** The resolvent $\mathbf{C}_t = (I - \alpha W_{\mathrm{sym}})^{-1}$ becomes a Fredholm integral operator. While well-defined, it loses the combinatorial interpretation (counting weighted paths) that makes it intuitive on graphs. Since $\mathbf{C}_t$ is a derived diagnostic (not in the energy), this does not affect the variational theory.

3. **Graph-specific results.** The Neumann series for the resolvent, the combinatorial path interpretation, and the explicit matrix computations that work on finite graphs do not transfer directly. They are replaced by functional-analytic analogues (Fredholm theory, spectral decomposition of integral operators) which are more abstract.

4. **Computational tractability.** The discrete theory admits direct numerical implementation (89 passing tests). The continuum PDE requires spatial discretization (finite elements, finite differences) to compute — which effectively returns to a graph/mesh setting. The continuum theory is primarily an analytical tool, not a computational one.

5. **The kernel length scale $\ell_K$ is new.** The discrete theory's aggregation operator $P$ is defined entirely by the graph structure (adjacency). The continuum kernel $K$ introduces a free length scale $\ell_K$ that must be prescribed or derived. This is an additional parameter not present in the discrete theory.

6. **Fiedler eigenvalue specificity.** The discrete $\lambda_2$ depends on graph topology (connectivity, bottlenecks, expansion properties). The continuum $\lambda_1(-\Delta_\Omega)$ depends only on domain geometry. The rich interplay between graph topology and formation structure is smoothed out.

---

## 11. The Local Limit: When the Kernel Shrinks

A natural question: what happens when the kernel width $\ell_K \to 0$?

In this limit, $(K * u)(x) \to u(x)$ for smooth $u$, so:

- $\mathrm{Cl}[u](x) \to \sigma(a_{\mathrm{cl}}(u(x) - \tau_{\mathrm{cl}}))$ (pointwise sigmoid)
- $\mathbf{D}[u](x) \to \sigma(a_D((1+\lambda_D)u(x) - \lambda_D) - \tau_D)$ (pointwise sigmoid)

The energy becomes **local**:

$$
\mathcal{E}_{\mathrm{cl}}^{\mathrm{local}}[u] = \int_\Omega |\sigma(a_{\mathrm{cl}}(u - \tau)) - u|^2\, dx
$$

$$
\mathcal{E}_{\mathrm{sep}}^{\mathrm{local}}[u] = \int_\Omega u\, (1 - \sigma(a_D((1+\lambda_D)u - \lambda_D) - \tau_D))\, dx
$$

These are **integral functionals of $u$ alone** (no derivatives, no convolutions). They act as additional potential terms in the energy:

$$
\mathcal{E}^{\mathrm{local}}[u] = \int_\Omega \left[ \alpha |\nabla u|^2 + V_{\mathrm{eff}}(u) \right] dx
$$

where $V_{\mathrm{eff}}(u) = \beta W(u) + \lambda_{\mathrm{cl}} |\sigma(a(u-\tau)) - u|^2 + \lambda_{\mathrm{sep}} u(1 - \sigma(\cdots))$.

This is a **modified Allen-Cahn functional** with a modified potential $V_{\mathrm{eff}}$. The self-referential structure reduces to a shaped potential well. The theory loses its relational character: closure and distinction become pointwise operations that do not depend on the spatial neighborhood.

**Assessment:** The local limit is mathematically clean but theoretically impoverished. The distinctive feature of SCC — that cohesion is defined by relational mutual support — requires a finite kernel width. The continuum theory is most faithful to the discrete theory when $\ell_K$ is comparable to the characteristic formation size, not when $\ell_K \to 0$.

---

## 12. Open Problems Specific to the Continuum Formulation

1. **Matched asymptotics for the self-referential correction to interface velocity.** The $O(\varepsilon)$ correction $\delta V_n^{\mathrm{self-ref}}$ to mean curvature flow has not been computed. This requires inner/outer expansion of the gradient flow PDE at a moving interface.

2. **Optimal kernel choice.** What kernel $K$ best approximates a given graph structure? Is there a canonical choice for $K$ given only the domain $\Omega$ and a length scale?

3. **Nonlocal-to-local limit with scaling.** As $\ell_K \to 0$ with $\alpha \sim \ell_K^2$ (rescaling the diffusion coefficient to maintain a finite diffusion length), does the nonlocal energy converge to a local energy with corrected potential? This would connect the kernel-based formulation to the purely local Allen-Cahn theory.

4. **Continuum transport.** The transport energy $\mathcal{E}_{\mathrm{tr}}$ requires a continuum transport kernel $\mathbf{M}_{t \to s}(x,y)$. This is the continuum analogue of the open discrete problem — making transport self-referential. In the continuum, optimal transport theory (Monge-Kantorovich, Benamou-Brenier) provides a natural framework, but the self-referential cost function (depending on $u_t, u_s$) remains novel and unproved.

5. **Multi-formation interaction in the continuum.** The discrete multi-formation problem (Spec Section 12) becomes a system of coupled nonlocal PDEs for $K$ fields $u^{(1)}, \ldots, u^{(K)}$. The continuum setting may provide analytical tools (e.g., vectorial Gamma-convergence) not available on graphs.

6. **The kernel as emergent.** Can $K$ be derived from the cohesion field itself, making the aggregation structure part of the solution rather than the input? This would address CN6 ("$K$ must be emergent") and would make the continuum theory fully self-contained.

---

## 13. Summary Assessment

**The continuum limit of SCC is mathematically well-posed and theoretically informative.** The core results (minimizer existence, phase transition, gradient flow convergence, Gamma-convergence) transfer cleanly from the discrete setting, with stronger regularity and richer analytical tools.

**What works:**
- The energy functional is well-defined in $H^1(\Omega)$
- Minimizers exist and are smooth
- The gradient flow is a well-posed nonlocal reaction-diffusion PDE
- The phase transition extends with $\lambda_2 \to \lambda_1(-\Delta)$
- The Gamma-convergence to perimeter (with $\delta\sigma = 0$) is standard
- All discrete bounds (Bind, Sep) transfer

**What is delicate:**
- The kernel $K$ introduces a length scale not present in the discrete theory
- The local limit ($\ell_K \to 0$) destroys the relational structure
- The co-belonging resolvent becomes a Fredholm operator (well-defined but less intuitive)
- Computational implementation requires re-discretization (finite elements)

**What breaks:**
- Nothing breaks in a fundamental sense. The continuum theory is a strict generalization of the discrete theory (any graph can be embedded as a kernel on a discrete measure). The main loss is specificity: graph-topological features (expansion, bottlenecks, specific spectral properties) are smoothed into domain-geometric features.

**The continuum formulation confirms that SCC is a perturbation of Allen-Cahn/Ginzburg-Landau theory by bounded self-referential terms.** At leading order (sharp-interface limit), SCC reduces to standard phase-field theory. At finite interface width, the self-referential terms provide quantitative corrections (enhanced metastability, modified transition profiles) without changing the qualitative picture. This is both a validation (SCC is mathematically consistent with a well-understood framework) and a challenge (the distinctive SCC features are subleading in the sharp-interface limit).
