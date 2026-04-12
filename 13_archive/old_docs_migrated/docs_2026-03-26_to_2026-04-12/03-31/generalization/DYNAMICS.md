# Dynamic Formulation of SCC: From Static Optimization to Temporal Evolution

**Author:** Dynamic Formulation Specialist | **Date:** 2026-03-30
**Input:** Canonical Spec v2.0 (energy, phase transition, gradient flow T14), PERSIST-SYNTHESIS.md (temporal theory), optimizer.py (computational gradient descent)

---

## 0. The Gap: Static Theory vs. Dynamic Perception

The current SCC theory characterizes formations as **energy minimizers** on the constraint manifold $\Sigma_m = \{u \in [0,1]^n : \sum u_i = m\}$. The optimizer (`find_formation`) uses projected gradient descent as a **computational method** to find these minimizers. But perception is fundamentally dynamic: formations emerge, evolve, compete, merge, and split in real time.

The gap is precise:

- **What exists:** $\mathcal{E}(u)$ on $\Sigma_m$ with T1 (existence), T8-Core (non-trivial minimizer), T14 (gradient flow convergence), T7-Enhanced (metastability).
- **What is missing:** A dynamical system governing the **temporal evolution** of $u_t$, with formations as attractors, formation transitions as heteroclinic orbits, and perceptual phenomena (rivalry, switching, hysteresis) as dynamical predictions.

This document develops the dynamics in six layers, from the simplest (deterministic gradient flow) to the most novel (coupled field-transport PDE-OT system).

---

## 1. L$^2$ Gradient Flow as Deterministic Dynamics

### 1.1. From Optimization to Dynamics

The projected gradient flow on $\Sigma_m$ is already implicit in the optimizer (§`optimizer.py:110-194`). We promote it from computational method to dynamical model:

$$
\frac{\partial u}{\partial t} = -\Pi_{\Sigma_m} \nabla \mathcal{E}(u)
\tag{GF}
$$

where $\Pi_{\Sigma_m}$ is the orthogonal projection onto $T_u \Sigma_m \cap T_u [0,1]^n$ (tangent cone of the feasible set). In the interior ($0 < u_i < 1$ for all $i$), this simplifies to:

$$
\frac{\partial u_i}{\partial t} = -\nabla_i \mathcal{E}(u) + \nu(t), \qquad \nu(t) = \frac{1}{n}\sum_j \nabla_j \mathcal{E}(u)
$$

where $\nu(t)$ is the Lagrange multiplier enforcing the volume constraint. This is the **mean-subtracted negative gradient**.

### 1.2. Dynamical Interpretation

Under (GF), the theory acquires standard dynamical-systems structure:

| Static concept | Dynamic interpretation |
|---|---|
| Energy minimizer $\hat{u}$ | Stable fixed point (attractor) |
| Saddle point of $\mathcal{E}$ | Unstable fixed point |
| Hessian eigenvalues at $\hat{u}$ | Linearized decay rates |
| T7-Enhanced metastability | Enhanced basin depth (larger $\lambda_{\min}(H_\Sigma)$) |
| T14 convergence | Global attractor existence within each basin |
| Multi-start optimization | Sampling different basins of attraction |

**Proposition 1.1 (Formation as Attractor).** Let $\hat{u} \in \Sigma_m$ be a strict local minimizer of $\mathcal{E}$ with constrained Hessian spectral gap $\mu > 0$. Then $\hat{u}$ is a locally asymptotically stable fixed point of (GF), with linearized convergence rate $\mu$.

*Proof:* Standard. $V(u) = \mathcal{E}(u) - \mathcal{E}(\hat{u})$ is a Lyapunov function: $\dot{V} = -\|\Pi_{\Sigma_m}\nabla\mathcal{E}\|^2 \leq 0$, with equality only at critical points. The Hessian condition gives $V(u) \geq (\mu/2)\|u - \hat{u}\|^2$ locally, yielding exponential convergence.

### 1.3. Formation Emergence Time

**Definition.** The *formation emergence time* $\tau_{\mathrm{emerge}}$ is the time for the gradient flow from the uniform state $u \equiv c$ to reach an $\epsilon$-neighborhood of the nearest non-trivial minimizer.

**Proposition 1.2 (Emergence Time Estimate).** In the unstable regime ($\beta/\alpha > \beta_{\mathrm{crit}}$, T8-Core), the initial exponential growth rate of the most unstable mode is:

$$
\gamma_{\mathrm{unstable}} = |4\alpha\lambda_2 + \beta W''(c)| = \beta|W''(c)| - 4\alpha\lambda_2
$$

The emergence time scales as $\tau_{\mathrm{emerge}} \sim \gamma_{\mathrm{unstable}}^{-1} \ln(1/\epsilon_0)$ where $\epsilon_0$ is the initial perturbation amplitude.

*Derivation:* Linearize (GF) at $u \equiv c$. The constrained Hessian on $T_{c\mathbf{1}}\Sigma_m$ has eigenvectors $v_k$ (Laplacian eigenvectors orthogonal to $\mathbf{1}$) with eigenvalues $4\alpha\lambda_k + \beta W''(c)$. The Fiedler mode $v_2$ is the most unstable when $4\alpha\lambda_2 + \beta W''(c) < 0$, giving exponential growth $\|v_2(t)\| \sim e^{\gamma_{\mathrm{unstable}} t}$.

**SCC prediction:** Formations aligned with the Fiedler vector emerge first. On grids, this means the first split follows the graph's largest-scale geometric mode. The self-referential terms ($\mathcal{E}_{\mathrm{cl}}, \mathcal{E}_{\mathrm{sep}}$) modify the mode selection but not the leading-order timescale (since they are perturbative at small amplitude per T8-Full).

### 1.4. Continuum Consistency (Integration with CONTINUUM.md)

The discrete gradient flow (GF) must reduce to the continuum PDE in the limit $|X| \to \infty$ with mesh spacing $h \to 0$ and $\alpha = \alpha_0/h^2$ (finite-element rescaling, Spec Section 13). The continuum gradient flow is (per continuum-ext):

$$
\frac{\partial u}{\partial t} = 2\alpha_0 \Delta u - \beta W'(u) - \lambda_{\mathrm{cl}} \nabla_u \mathcal{E}_{\mathrm{cl}}[u] - \lambda_{\mathrm{sep}} \nabla_u \mathcal{E}_{\mathrm{sep}}[u]
\tag{GF-cont}
$$

where the self-referential corrections involve Fréchet derivatives of the continuous closure and distinction operators (kernel convolutions composed with sigmoid). The Allen-Cahn part ($2\alpha_0 \Delta u - \beta W'(u)$) is standard; the self-referential terms are the SCC-specific content.

**Consistency check.** In the discrete setting, the smoothness gradient is $4\alpha L u$ (ordered-pair convention, Spec §0). With $\alpha = \alpha_0/h^2$ and the standard graph Laplacian approximation $L \approx -h^{-2}\Delta + O(h^0)$, this gives $4\alpha_0 h^{-2} \cdot (-h^{-2}\Delta u) \cdot h^d = 2\alpha_0 \Delta u$ after accounting for the volume element and ordered-pair double-counting. The factor matches (GF-cont).

**Sharp-interface limit.** As $\varepsilon = \alpha/\beta \to 0$, the continuum flow (GF-cont) converges to mean curvature flow with $O(\varepsilon)$ self-referential corrections to the interface velocity and profile. Per continuum-ext, these corrections vanish in the $\Gamma$-limit (consistent with T11) but modify the dynamics at finite $\varepsilon$. The interface velocity becomes:

$$
v_n = \kappa + \varepsilon \cdot v_{\mathrm{SCC}}(\text{local field structure}) + O(\varepsilon^2)
$$

where $\kappa$ is the mean curvature and $v_{\mathrm{SCC}}$ encodes the self-referential operator contributions. This is the dynamic counterpart of T11 ($\Gamma$-convergence).

**Spectral correspondence.** The Fiedler eigenvalue $\lambda_2$ of the graph Laplacian corresponds to the first Dirichlet eigenvalue $\lambda_1(-\Delta)$ of $-\Delta$ on the domain $\Omega$ in the continuum. The phase transition criterion $\beta/\alpha > 4\lambda_2/|W''(c)|$ becomes the standard Allen-Cahn instability condition $\beta/\alpha_0 > 4\lambda_1(-\Delta)/|W''(c)|$ in the continuum. This confirms that the discrete T8-Core is the correct finite-dimensional truncation of the continuum instability.

### 1.5. Scale-Dependent Convergence Rates (Integration with MULTISCALE.md)

The convergence rate of the gradient flow (GF) depends on the spatial scale of the perturbation. Per multiscale-ext, the relaxation time for a perturbation at length scale $L$ scales as:

$$
\tau_{\mathrm{relax}}(L) \sim L^z
$$

where $z$ is the **dynamic exponent**. For pure Allen-Cahn, $z = 2$ (diffusive scaling). The SCC self-referential corrections may modify $z$ at scales comparable to the formation size.

**Proposition 1.3 (Scale-dependent Hessian spectral gap).** The constrained Hessian $H_\Sigma$ restricted to eigenmodes at scale $L$ has eigenvalue:

$$
\mu(L) \approx 4\alpha / L^2 + \beta |W''(\hat{u})| + \lambda_{\mathrm{cl}} \mu_{\mathrm{cl}}(L) + \lambda_{\mathrm{sep}} \mu_{\mathrm{sep}}(L)
$$

where $\mu_{\mathrm{cl}}(L), \mu_{\mathrm{sep}}(L)$ are the scale-dependent contributions of the closure and separation Hessians. The convergence rate at scale $L$ is $\sim 1/\mu(L)$.

- **Fine scales** ($L \ll$ formation size): Dominated by $4\alpha/L^2$. Relaxation is fast, diffusive ($z = 2$). Self-referential corrections are negligible.
- **Formation scale** ($L \sim$ formation size): The self-referential terms $\mu_{\mathrm{cl}}, \mu_{\mathrm{sep}}$ become comparable to the diffusive term. The effective $z$ may deviate from 2 at this scale -- this is where the SCC dynamics is most distinct from Allen-Cahn.
- **Coarse scales** ($L \gg$ formation size): Dominated by the double-well curvature $\beta|W''|$. Relaxation is fast and scale-independent.

The T14 convergence rate (gradient flow to critical point) is determined by the *slowest* mode, which is typically at the formation scale. This explains why the optimizer's convergence (§`optimizer.py:172-178`) is controlled by the constrained Hessian spectral gap $\mu$ -- this is $\mu(L_{\mathrm{formation}})$.

### 1.6. Connection to Existing Code

The optimizer's semi-implicit scheme (§`optimizer.py:131-140`) is a time discretization of (GF):

- The diffusion part ($4\alpha Lu$) is treated implicitly (unconditionally stable).
- The reaction part (double-well + closure + separation gradients) is treated explicitly.
- The Barzilai-Borwein step size (§`optimizer.py:156-164`) is an adaptive time step.

Reinterpreting the optimizer as a dynamical simulator requires: (i) fixed time step $\Delta t$ (not adaptive), (ii) recording the full trajectory $u(t)$, not just the endpoint, (iii) interpreting convergence failure as metastable trapping, not optimization failure.

---

## 2. Stochastic Gradient Flow (Langevin Dynamics on $\Sigma_m$)

### 2.1. Motivation

Deterministic gradient flow converges to a single minimizer determined by initial conditions. Perception, however, involves:
- **Bistable perception** (Necker cube, Rubin vase): spontaneous switching between formations.
- **Binocular rivalry**: alternating dominance of competing formations.
- **Perceptual noise**: stochastic fluctuations in perceived structure.

These require stochastic dynamics.

### 2.2. Constrained Langevin Equation

The stochastic gradient flow on $\Sigma_m$ is:

$$
du = -\Pi_{\Sigma_m}\nabla\mathcal{E}(u)\,dt + \sqrt{2T}\,\Pi_{\Sigma_m}\,dW_t
\tag{SL}
$$

where:
- $T > 0$ is the **noise temperature** (not physical temperature; a parameter controlling stochastic exploration),
- $W_t$ is standard Brownian motion in $\mathbb{R}^n$,
- $\Pi_{\Sigma_m}$ projects both drift and diffusion onto the constraint manifold.

The projection of the noise term ensures $\sum du_i = 0$ (volume preservation) and $u_i \in [0,1]$ (box constraint, enforced by reflection at boundaries).

### 2.3. Stationary Distribution

**Proposition 2.1.** The stationary distribution of (SL) restricted to the interior of $\Sigma_m$ is the Gibbs measure:

$$
\pi_T(u) \propto \exp\left(-\frac{\mathcal{E}(u)}{T}\right) \cdot \mathbf{1}_{\Sigma_m}(u)
$$

At low temperature ($T \to 0$), the measure concentrates on global energy minimizers. At intermediate $T$, it samples metastable states with probability proportional to their basin volumes weighted by $\exp(-\mathcal{E}/T)$.

*Proof:* Standard detailed balance for gradient-flow Langevin dynamics with quadratic (Euclidean) kinetic energy on the constraint manifold.

### 2.4. Kramers Escape Theory: Formation Switching

**Theorem 2.2 (Kramers Rate for Formation Transitions).** Let $\hat{u}_a, \hat{u}_b$ be two local minimizers of $\mathcal{E}$ on $\Sigma_m$, separated by a saddle point $u^*$ with energy barrier $\Delta E = \mathcal{E}(u^*) - \mathcal{E}(\hat{u}_a)$. The mean escape time from the basin of $\hat{u}_a$ satisfies:

$$
\tau_{\mathrm{escape}} \sim \frac{2\pi}{\gamma_{\mathrm{unstable}}(u^*)} \sqrt{\frac{\det H_\Sigma(\hat{u}_a)}{|\det H_\Sigma(u^*)|}} \exp\left(\frac{\Delta E}{T}\right)
\tag{Kramers}
$$

where $\gamma_{\mathrm{unstable}}(u^*)$ is the absolute value of the single negative eigenvalue of the constrained Hessian at $u^*$, and $H_\Sigma$ denotes the constrained Hessian restricted to $T\Sigma_m$.

**SCC enhancement via T7-Enhanced.** The closure term's positive-definite Hessian contribution increases $\Delta E$ relative to pure Allen-Cahn (AC). For SCC vs. AC at the same $(\alpha, \beta)$:

$$
\Delta E^{\mathrm{SCC}} = \Delta E^{\mathrm{AC}} + \lambda_{\mathrm{cl}} \Delta E_{\mathrm{cl}} + \lambda_{\mathrm{sep}} \Delta E_{\mathrm{sep}}
$$

where $\Delta E_{\mathrm{cl}} = \mathcal{E}_{\mathrm{cl}}(u^*) - \mathcal{E}_{\mathrm{cl}}(\hat{u}_a) \geq 0$ (the saddle point is further from the closure fixed point than the minimizer). Therefore:

$$
\frac{\tau_{\mathrm{escape}}^{\mathrm{SCC}}}{\tau_{\mathrm{escape}}^{\mathrm{AC}}} \sim \exp\left(\frac{\lambda_{\mathrm{cl}}\Delta E_{\mathrm{cl}} + \lambda_{\mathrm{sep}}\Delta E_{\mathrm{sep}}}{T}\right) \gg 1
$$

**Prediction (SCC-specific):** Self-referential formations dwell longer than non-self-referential formations with the same morphology. The enhancement is exponential in the closure and separation barrier contributions. This is the dynamical signature of T7-Enhanced metastability.

### 2.5. Dwell Time Distribution

**Prediction 2.3 (Dwell Time Statistics).** For a bistable stimulus (two competing formations $\hat{u}_a, \hat{u}_b$), the dwell time in each percept follows an approximate exponential distribution:

$$
P(\tau > t) \approx \exp\left(-t / \bar{\tau}\right), \qquad \bar{\tau} = \tau_{\mathrm{escape}}(\text{Kramers})
$$

with corrections from:
1. **Non-Arrhenius prefactor:** The prefactor in (Kramers) depends on basin geometry, modulated by SCC's self-referential operators.
2. **Multiple escape paths:** If the saddle point is degenerate or multiple saddles have similar barrier heights.
3. **Noise-induced transitions:** At high $T$, the Kramers approximation breaks down and transitions become diffusive.

This is directly testable against binocular rivalry data, where dwell times are empirically close to gamma-distributed (approximately exponential with shape parameter near 1).

---

## 3. Multi-Formation Dynamics

### 3.1. $K$-Field Competition Dynamics

For $K$ coexisting formations with fields $u^1, \ldots, u^K \in [0,1]^n$ subject to simplex constraint $\sum_k u^k(x) \leq 1$ for all $x$, the coupled gradient flow is:

$$
\frac{\partial u^k}{\partial t} = -\Pi_{\Sigma}\nabla_{u^k} \mathcal{E}_K(u^1, \ldots, u^K)
\tag{KF}
$$

where $\Pi_\Sigma$ projects onto the joint constraint $\{\sum_k u^k_i \leq 1,\; \sum_i u^k_i = m_k\}$ and the total energy is:

$$
\mathcal{E}_K = \sum_{k=1}^K \mathcal{E}(u^k) + \lambda_{\mathrm{rep}} \sum_{j \neq k} \mathcal{E}_{\mathrm{rep}}(u^j, u^k)
$$

The repulsion term prevents formation overlap:

$$
\mathcal{E}_{\mathrm{rep}}(u^j, u^k) = \sum_{x \in X} u^j(x) \cdot u^k(x)
$$

### 3.2. Competition and Selection

The $K$-field dynamics exhibit three regimes:

**Regime I: Weak competition** ($\lambda_{\mathrm{rep}}$ small, formations spatially separated). Each $u^k$ evolves approximately independently. Fixed points are products of single-formation minimizers.

**Regime II: Strong competition** ($\lambda_{\mathrm{rep}}$ large, formations overlap). Competition suppresses weaker formations. Winner-take-all dynamics emerge:

$$
\frac{d}{dt}\left(\sum_i u^k_i\right) \approx -\lambda_{\mathrm{rep}} \sum_i u^k_i \sum_{j \neq k} u^j_i + \text{(self-energy terms)}
$$

A formation with less spatial overlap with competitors grows at the expense of those with more overlap.

**Regime III: Critical** (near bifurcation). Formation birth/death events occur. See Section 3.3.

### 3.3. Formation Birth and Death

**Birth (nucleation).** A new formation nucleates when the background field (complement of existing formations) becomes unstable. The instability criterion is a $K$-field generalization of T8-Core:

$$
\beta / \alpha > \frac{4\lambda_2^{\mathrm{comp}}}{|W''(c^{\mathrm{comp}})|}
$$

where $\lambda_2^{\mathrm{comp}}$ is the Fiedler eigenvalue of the Laplacian restricted to the complement of existing formation supports, and $c^{\mathrm{comp}}$ is the mean field value in the complement.

**Death (collapse).** A formation dies when its energy barrier vanishes: $\Delta E^k \to 0$. This occurs when:
1. Its volume $m_k$ drops below a critical threshold (the formation becomes too small to sustain itself).
2. Competition from neighboring formations erodes its basin of attraction.
3. The spectral gap $\mu^k \to 0$ (approaching a shape bifurcation; cf. PERSIST-SYNTHESIS.md Section 2.3).

**Prediction 3.1 (Formation Number Scaling).** On a graph with $n$ sites, the equilibrium number of formations scales as $K^* \sim n / n_{\mathrm{crit}}$ where $n_{\mathrm{crit}}$ is the minimum graph size supporting a single formation (determined by T8-Core phase transition). This is analogous to the number of domains in a ferromagnet below the Curie temperature.

### 3.4. Open Problem: Simplex vs. Independent Volume Constraints

Two constraint architectures are possible:

**(A) Global simplex:** $\sum_k u^k(x) \leq 1$ for all $x$, with $\sum_i u^k_i = m_k$ for each $k$. This enforces that formations partition the space. Computationally tractable via alternating projection.

**(B) Independent volumes:** Each $u^k \in \Sigma_{m_k}$ independently, with overlap penalized only through $\mathcal{E}_{\mathrm{rep}}$. This allows partial overlap (e.g., transparent surfaces, auditory streaming with shared features).

The choice between (A) and (B) is an **open design decision** (Canonical Spec Section 11.2, item 6). Architecture (A) is simpler but prohibits legitimate overlap phenomena; (B) is more general but requires careful tuning of $\lambda_{\mathrm{rep}}$.

---

## 4. Coupled Field-Transport Dynamics

### 4.1. The Self-Referential PDE-OT System

The most novel dynamical structure arises when field evolution and transport are coupled. At each time $t$, two processes operate simultaneously:

**Field evolution** (reaction-diffusion on $X_t$):
$$
\frac{\partial u_t}{\partial \tau} = -\Pi_{\Sigma_m}\nabla_u \mathcal{E}_t(u_t)
\tag{FE}
$$

**Transport evolution** (optimal transport between times):
$$
M_{t \to s}^* = \arg\min_{M \in \mathcal{M}} \sum_{x,y} M(x,y) \cdot c(x,y; u_t, u_s) + \varepsilon_{\mathrm{OT}} \cdot \mathrm{KL}(M \| \kappa)
\tag{TE}
$$

where $c(x,y; u_t, u_s)$ is the **self-referential transport cost** (depending on the fields that transport connects), $\mathcal{M}$ is the set of sub-stochastic couplings (Spec E1), and the KL term provides entropic regularization.

The coupling is bidirectional:
- $M_{t \to s}$ depends on $u_t, u_s$ through the cost function (fingerprint-based; PERSIST-SYNTHESIS.md Section 1.2).
- $u_s$ depends on $M_{t \to s}$ through the transport energy $\mathcal{E}_{\mathrm{tr}}$ and the initialization $u_s^{(0)} = \pi_{\Sigma}(M_{t \to s} u_t)$.

### 4.2. Formal Structure: Fixed-Point Iteration

**Definition 4.1.** The *self-referential field-transport fixed point* is a pair $(\hat{u}_s, \hat{M}_{t \to s})$ satisfying:

1. $\hat{u}_s$ minimizes $\mathcal{E}_s(u) + \lambda_{\mathrm{tr}} \mathcal{E}_{\mathrm{tr}}(u, \hat{u}_t; \hat{M}_{t \to s})$ on $\Sigma_m$.
2. $\hat{M}_{t \to s}$ minimizes the regularized transport cost with $c(x,y; \hat{u}_t, \hat{u}_s)$.

This is the object whose existence is the "self-referential transport fixed-point" open problem (Canonical Spec Section 12, PERSIST-SYNTHESIS.md Section 4.1 item 1).

**Proposition 4.2 (Alternating Minimization).** The alternating scheme:

$$
u_s^{(\ell+1)} = \arg\min_u \mathcal{E}_s(u) + \lambda_{\mathrm{tr}} \mathcal{E}_{\mathrm{tr}}(u, u_t; M^{(\ell)}), \qquad M^{(\ell+1)} = \arg\min_M \mathrm{cost}(M; u_t, u_s^{(\ell+1)})
$$

decreases the joint objective at each step (since each sub-problem is a minimization with the other variable fixed). Convergence to a fixed point follows if the joint objective is bounded below and the sub-problems have unique solutions (guaranteed for the transport sub-problem by strict convexity of KL when $\varepsilon_{\mathrm{OT}} > 0$).

*Status:* The alternating minimization converges to *a* fixed point but not necessarily to the *global* minimizer of the joint problem (which is non-convex). This aligns with PERSIST-SYNTHESIS.md Section 4.1: "The Brouwer argument fails at Maxwell points."

### 4.3. Timescale Separation

The coupled system has **two natural timescales**:

- **Fast ($\tau$):** Within-time field evolution by gradient flow. Timescale: $1/\mu$ where $\mu$ is the Hessian spectral gap.
- **Slow ($t$):** Between-time transport. Timescale: $\Delta t$ (the physical time between successive frames/inputs).

When $\mu \Delta t \gg 1$ (the field equilibrates much faster than the input changes), the dynamics reduce to:

$$
\hat{u}_{t+\Delta t} \approx \hat{u}_t - \frac{\Delta t}{\mu} \nabla_{\mathrm{param}} \mathcal{E}(\hat{u}_t; \theta(t)) + O(\Delta t^2)
$$

where $\theta(t)$ represents slowly varying external parameters (adjacency structure, stimulus). This is the **adiabatic approximation**: the formation tracks the slowly moving energy landscape.

When $\mu \Delta t \sim O(1)$ (the field cannot fully equilibrate), the dynamics become genuinely non-equilibrium. Formation-tracking lag produces **perceptual hysteresis**: the perceived formation persists beyond the parameter range where it is the global minimizer.

### 4.4. Hysteresis and Path-Dependence

**Prediction 4.3 (Hysteresis Width).** Consider a parameter $\theta$ that is swept slowly through a bifurcation at $\theta = \theta_c$ where formation $\hat{u}_a$ loses stability and formation $\hat{u}_b$ becomes the global minimizer. Under deterministic dynamics:

- Forward sweep: $\hat{u}_a$ persists until $\theta = \theta_c + \delta_+$ where $\delta_+$ is the basin collapse point.
- Backward sweep: $\hat{u}_b$ persists until $\theta = \theta_c - \delta_-$.
- Hysteresis width: $\delta_+ + \delta_-$.

Under stochastic dynamics (SL), the hysteresis narrows:
$$
\delta_\pm^{\mathrm{stochastic}} \approx \delta_\pm^{\mathrm{det}} - T \cdot f(\text{barrier shape})
$$

where $f$ captures how noise facilitates early escape. The **SCC-specific prediction** is that self-referential formations have wider hysteresis than Allen-Cahn formations (because T7-Enhanced increases the barrier, requiring larger $\delta$ to collapse the basin or more noise to escape).

---

## 5. Neural Dynamics Interpretation

### 5.1. Mapping to Neural Activity

If $u_t(x)$ represents the firing rate or activation level of a neural population at cortical site $x$, the gradient flow (GF) maps to a neural dynamics model:

| SCC quantity | Neural interpretation |
|---|---|
| $u_t(x)$ | Population firing rate at site $x$ |
| $\mathbf{N}_t(x,y)$ | Lateral connection strength |
| $\mathrm{Cl}_t(u)$ | Recurrent excitation (self-amplification) |
| $\mathbf{D}_t(x; 1-u)$ | Lateral inhibition (surround suppression) |
| $\mathcal{E}_{\mathrm{bd}}$ smoothness | Spatial integration (smoothing by lateral connections) |
| $\mathcal{E}_{\mathrm{bd}}$ double-well | Winner-take-all nonlinearity |
| Temperature $T$ | Neural noise / spontaneous firing |
| Volume constraint $\sum u_i = m$ | Global normalization (divisive inhibition) |

### 5.2. Relation to Existing Neural Models

**Hopfield networks:** The energy $\mathcal{E}$ plays the role of the Hopfield energy, with formations as stored patterns (attractors). SCC extends Hopfield by: (i) continuous-valued fields on graphs (not binary neurons on complete graphs), (ii) self-referential operators (not fixed weight matrices), (iii) volume constraint (not unconstrained).

**Wilson-Cowan dynamics:** The gradient flow $\partial u/\partial t = -\nabla\mathcal{E}$ can be written as:

$$
\frac{\partial u_i}{\partial t} = -u_i + \sigma\left(\sum_j W_{ij}^{\mathrm{eff}}(u) u_j - \theta_i^{\mathrm{eff}}(u)\right) + \text{correction terms}
$$

where $W^{\mathrm{eff}}(u)$ and $\theta^{\mathrm{eff}}(u)$ are field-dependent effective weights and thresholds derived from the closure and distinction operators. The field-dependence of the effective connectivity is the SCC-specific feature: lateral connections are **modulated by the activity pattern they produce**, creating a self-referential loop.

**Remark (CN10 compliance).** These mappings are **contrastive comparisons**, not reductive identifications. SCC dynamics is not "just" a Hopfield network or "just" Wilson-Cowan; the self-referential operator structure and the ontological commitments (graded cohesion prior to objecthood) are distinctive. The mapping illuminates structural parallels while preserving theoretical independence.

### 5.3. Neural Predictions

**P5.1 (Enhanced stability of coherent percepts).** Neural representations that achieve high Bind and Sep scores should exhibit longer dwell times and stronger resistance to perturbation than representations with similar energy but lower self-referential scores. This is the neural correlate of T7-Enhanced metastability.

**P5.2 (Volume-constrained competition).** Enhancing one formation's activity should suppress competing formations globally (not just locally), mediated by the volume constraint. This maps to divisive normalization in visual cortex.

**P5.3 (Mode-dependent switching).** Transitions between competing percepts should follow the Fiedler-mode pathway (the minimum-energy saddle), producing characteristic intermediate states where the field is partially decomposed along the graph's principal geometric axis.

---

## 6. Summary of Predictions from Dynamics

### 6.1. Quantitative Predictions

| Prediction | Formula | Testable against |
|---|---|---|
| **Dwell time** | $\bar{\tau} \propto \exp(\Delta E / T)$ with $\Delta E$ from SCC energy | Binocular rivalry data |
| **SCC vs. AC dwell ratio** | $\bar{\tau}^{\mathrm{SCC}}/\bar{\tau}^{\mathrm{AC}} \sim \exp((\lambda_{\mathrm{cl}}\Delta E_{\mathrm{cl}} + \lambda_{\mathrm{sep}}\Delta E_{\mathrm{sep}})/T)$ | Comparative simulation |
| **Emergence time** | $\tau_{\mathrm{emerge}} \sim (\beta|W''(c)| - 4\alpha\lambda_2)^{-1} \ln(1/\epsilon_0)$ | Reaction time data |
| **Hysteresis width** | $\delta \propto r_{\mathrm{basin}}$ (basin radius from PERSIST-SYNTHESIS.md: $r \geq 0.210$) | Perceptual hysteresis experiments |
| **Formation count** | $K^* \sim n/n_{\mathrm{crit}}$ | Multi-object displays |

### 6.2. Qualitative Predictions

1. **Switching dynamics are formation-to-formation, not random.** Transitions follow minimum-energy paths (heteroclinic orbits) through specific saddle points, producing structured intermediate states.

2. **Self-referential formations are stickier.** Higher Bind and Sep scores predict longer dwell times, even controlling for energy depth. This is the unique dynamical signature of SCC's operator structure.

3. **Emergence from homogeneity follows spectral modes.** The initial symmetry-breaking of the uniform state $u \equiv c$ is dominated by the Fiedler eigenvector, predicting that the first perceived structure aligns with the stimulus's principal geometric axis.

4. **Hysteresis is wider for SCC than AC.** Formation persistence under parameter change extends further because the self-referential operators deepen the energy well.

5. **Near-bifurcation fragility is real.** When $\mu \to 0$ (PERSIST-SYNTHESIS.md Section 2.3), formations become maximally sensitive to perturbation. This predicts that stimuli near perceptual bifurcations should show maximum rivalry rate and minimum dwell time.

---

## 7. Mathematical Status and Open Problems

### 7.1. What Is Proved (or Follows from Existing Results)

| Claim | Status | Depends on |
|---|---|---|
| Formation = stable fixed point of (GF) | **Proved** | T14 + Lyapunov argument (standard) |
| Exponential convergence within basin | **Proved** | Hessian spectral gap $\mu > 0$ (T7-Enhanced) |
| Gibbs stationary distribution for (SL) | **Proved** | Standard Langevin theory on compact manifold |
| Kramers rate formula | **Conditional** | Requires saddle-point analysis on $\Sigma_m$ (partially done: PERSIST-SYNTHESIS.md Section 1.3) |
| Enhanced dwell time (SCC > AC) | **Conditional** | Requires $\Delta E_{\mathrm{cl}}(u^*) > 0$ at saddle points (plausible but unproved) |

### 7.2. Open Problems Specific to Dynamics

1. **Saddle-point classification on $\Sigma_m$.** The Kramers formula requires identifying all index-1 saddle points of $\mathcal{E}$ on $\Sigma_m$ and their energies. This is a computational problem for specific graphs and a Morse-theoretic problem in general. Related to PERSIST-SYNTHESIS.md Section 4.1 item 3 ("basin escape paths bypassing core").

2. **Stochastic dynamics on $\Sigma_m$ with box constraints.** The reflected Langevin process on the polytope $\Sigma_m \cap [0,1]^n$ has technical subtleties (corner behavior, non-smoothness of the constraint boundary). Existence and uniqueness of the process require verification, though the compact convex setting is well-studied.

3. **$K$-field dynamics: well-posedness.** The coupled system (KF) with simplex constraint $\sum_k u^k \leq 1$ requires careful analysis of the projection operator and its differentiability.

4. **Self-referential PDE-OT coupling: existence.** The coupled field-transport fixed point (Definition 4.1) is the dynamics version of the foundational open problem (Canonical Spec Section 12). The alternating minimization (Proposition 4.2) provides a constructive approach but does not resolve the uniqueness question.

5. **Sharp-interface dynamics limit.** As $\varepsilon = \alpha/\beta \to 0$, the gradient flow (GF) should converge to a modified mean curvature flow with self-referential surface tension (Canonical Spec Section 12, "Sharp-interface dynamics"). Connecting the SCC dynamics to geometric evolution equations is mathematically novel.

6. **Quantitative barrier computation.** Computing $\Delta E_{\mathrm{cl}}$ and $\Delta E_{\mathrm{sep}}$ at saddle points to verify the enhanced-dwell-time prediction. This requires finding saddle points numerically (e.g., via the nudged elastic band method on $\Sigma_m$).

### 7.3. Relation to Canonical Spec Open Design Choices

The dynamics developed here addresses **Open Design Choice 4** from the Canonical Spec (Section 11.2): "Dynamic update laws." We propose:

- The L$^2$ gradient flow (GF) as the **canonical deterministic dynamics**.
- The constrained Langevin equation (SL) as the **canonical stochastic dynamics**.
- The coupled field-transport system (FE)+(TE) as the **canonical temporal dynamics**.

These are proposed as **provisional dynamical realizations**, at the same architectural layer as the provisional operator forms in Spec Section 9. They are constrained by the canonical commitments (especially the four-term energy independence, CN5) but not uniquely determined by them.

---

## 8. Coordination Notes

### For continuum-ext teammate
**Integrated:** Section 1.4 now incorporates the continuum PDE form, sharp-interface limit with $O(\varepsilon)$ self-referential corrections, and spectral correspondence ($\lambda_2 \leftrightarrow \lambda_1(-\Delta)$). Remaining question: the stochastic version (SL) becomes an SPDE in the continuum. The sharp-interface limit ($\varepsilon \to 0$) of the *stochastic* dynamics gives a stochastic mean curvature flow with self-referential surface tension -- this is the dynamics counterpart of T11 ($\Gamma$-convergence). Does the noise survive the sharp-interface limit, or does it concentrate on the interface as in stochastic Allen-Cahn (Funaki, 1995)?

### For multiscale-ext teammate
**Integrated:** Section 1.5 now incorporates the scale-dependent relaxation $\tau(L) \sim L^z$ and the possibility that SCC modifies the dynamic exponent $z$ at the formation scale. Remaining questions: (i) What is the explicit form of $\mu_{\mathrm{cl}}(L)$ and $\mu_{\mathrm{sep}}(L)$ (the scale-dependent self-referential Hessian contributions)? These depend on the Fourier/spectral structure of the closure and distinction Jacobians. (ii) Does the RG flow on the energy landscape commute with the dynamics on the state? That is, does coarse-graining the energy and then flowing give the same result as flowing and then coarse-graining? This is a dynamical RG question. (iii) The adiabatic approximation (Section 4.3) reduces the dynamics to ODE on the slow manifold. Non-adiabatic corrections produce hysteresis and formation-tracking lag.

### For stochastic-ext teammate
The Langevin dynamics (SL) is the starting point for your work. Key extensions: (i) spatially correlated noise (not white noise), modeling structured neural fluctuations; (ii) multiplicative noise ($\sqrt{T \cdot f(u)}\,dW$), modeling state-dependent neural variability; (iii) non-equilibrium steady states when external driving breaks detailed balance. The Kramers escape theory (Section 2.4) needs your expertise for: computing prefactors, handling degenerate saddles (multiple escape paths with similar barriers), and extending to the $K$-field setting.
