# Stochastic Extension of Soft Cognitive Cohesion

**Author:** Stochastic Extension Specialist
**Date:** 2026-03-30
**Status:** Theoretical development
**Dependencies:** Canonical Spec v2.0 (energy functional §8), T4-METASTABILITY-REPAIR.md (Hessian analysis), H_CL_PSD_EVIDENCE.md (curvature data), continuum-ext (SPDE connection)

---

## 0. Motivation

The deterministic SCC theory (T = 0) characterizes formations as energy minimizers on $\Sigma_m$. But real perception operates in the presence of noise — neural fluctuations, sensory variability, attentional modulation. The stochastic extension asks: what happens to SCC formations at finite temperature?

This is not merely a technical add-on. Three of the theory's empirical predictions (P3: enhanced dwell times, P4: path dependence, P5: noise-induced formation) are inherently stochastic phenomena that *require* a finite-temperature framework. The deterministic theory can identify metastable states but cannot predict transition rates, dwell time distributions, or noise-dependent nucleation.

**Scope.** This document develops the stochastic SCC framework for the static (single-time) energy $\mathcal{E}(u) = \lambda_{\mathrm{cl}}\mathcal{E}_{\mathrm{cl}} + \lambda_{\mathrm{sep}}\mathcal{E}_{\mathrm{sep}} + \lambda_{\mathrm{bd}}\mathcal{E}_{\mathrm{bd}}$ on $\Sigma_m$. The temporal transport term $\mathcal{E}_{\mathrm{tr}}$ is excluded because its operator $\mathbf{M}_{t \to s}$ lacks a concrete self-referential realization (Canonical Spec §12, Open Problem 1).

---

## 1. Gibbs Measure on the Formation Manifold

### 1.1. Definition

Define the Gibbs (Boltzmann) probability measure on the constraint manifold $\Sigma_m = \{u \in [0,1]^n : \sum_i u_i = m\}$:

$$
\mathrm{d}\mu_T(u) = \frac{1}{Z(T)} \exp\!\left(-\frac{\mathcal{E}(u)}{T}\right) \mathrm{d}\sigma_{\Sigma}(u)
$$

where $T > 0$ is the temperature (noise intensity), $\mathrm{d}\sigma_{\Sigma}$ is the $(n-1)$-dimensional Hausdorff measure on $\Sigma_m \cap [0,1]^n$ (restricted to the box), and $Z(T)$ is the partition function.

**Interpretation.** $T$ parameterizes the noise level in the perceptual system. It is not literal thermodynamic temperature but a control parameter measuring the strength of fluctuations relative to energetic preferences. In neural terms, $T$ correlates with internal noise, attentional variability, or sensory uncertainty.

### 1.2. Limiting Behavior

- **$T \to 0^+$ (deterministic limit):** $\mu_T$ concentrates on the set of global energy minimizers. By Laplace's method, $\mu_T \to \sum_k w_k \delta_{\hat{u}_k}$ where $\hat{u}_k$ are the global minimizers and $w_k$ depends on the Hessian determinant at each minimizer. This recovers the deterministic theory.

- **$T \to \infty$ (maximal noise):** $\mu_T \to$ uniform measure on $\Sigma_m \cap [0,1]^n$. All field configurations are equally probable; no formation is preferred. This is the "perceptual white-out" regime.

- **Intermediate $T$:** $\mu_T$ concentrates near local minimizers with weights depending on both depth and curvature of the energy basins. Multiple metastable formations coexist as peaks of the Gibbs measure.

### 1.3. Self-Referential Structure

The Gibbs measure inherits the self-referential structure of SCC. The energy $\mathcal{E}(u)$ contains the closure term $\mathcal{E}_{\mathrm{cl}} = \|u - \mathrm{Cl}(u)\|^2$ and the separation term $\mathcal{E}_{\mathrm{sep}} = \sum_i u_i(1 - D_i(u))$, both of which involve operators that depend on $u$ itself. This makes $\mu_T$ a non-standard Gibbs measure: the "Hamiltonian" is self-referential, not a fixed external potential.

**Consequence.** Standard results from equilibrium statistical mechanics (e.g., equivalence of ensembles, Lee-Yang theory of phase transitions) apply only with caution. The self-referential terms modify the effective interaction structure in a field-dependent way.

---

## 2. Partition Function and Free Energy

### 2.1. Partition Function

$$
Z(T) = \int_{\Sigma_m \cap [0,1]^n} \exp\!\left(-\frac{\mathcal{E}(u)}{T}\right) \mathrm{d}\sigma_{\Sigma}(u)
$$

$Z(T)$ is finite and positive for all $T > 0$ because $\Sigma_m \cap [0,1]^n$ is compact and the integrand is continuous and strictly positive.

### 2.2. Free Energy

$$
F(T) = -T \log Z(T)
$$

The free energy governs the thermodynamics of formation fluctuations:

- **Entropy:** $S(T) = -\partial F / \partial T = \log Z + \langle \mathcal{E} \rangle_T / T$, measuring the log-volume of thermally accessible configurations.
- **Specific heat:** $C(T) = T \, \partial S / \partial T = \langle (\mathcal{E} - \langle \mathcal{E} \rangle)^2 \rangle_T / T^2$, measuring energy fluctuations. A peak in $C(T)$ signals a crossover or phase transition in the Gibbs measure.

### 2.3. Formation Thermodynamic Stability

A formation $\hat{u}$ is **thermodynamically favored** at temperature $T$ if the local free energy $F_{\mathrm{loc}}(\hat{u}, T)$ (computed from the Laplace approximation around $\hat{u}$) satisfies:

$$
F_{\mathrm{loc}}(\hat{u}, T) < F_{\mathrm{loc}}(c\mathbf{1}, T)
$$

where $c\mathbf{1}$ is the uniform field. By the Laplace approximation (§2.4):

$$
F_{\mathrm{loc}}(\hat{u}, T) \approx \mathcal{E}(\hat{u}) + \frac{T}{2} \log \det\!\left(\frac{H(\hat{u})|_T}{2\pi T}\right)
$$

The entropic correction $\frac{T}{2} \log \det H|_T$ penalizes states with large Hessian eigenvalues (stiff basins). The SCC Hessian enhancement (T7-Enhanced) makes formation basins stiffer than Allen-Cahn basins, so the entropic penalty is larger — partially offsetting the energetic advantage at high $T$.

### 2.4. Laplace Approximation

For small $T$, the partition function decomposes over critical points:

$$
Z(T) \approx \sum_k \frac{(2\pi T)^{(n-1)/2}}{\sqrt{\det H_k|_T}} \exp\!\left(-\frac{\mathcal{E}(\hat{u}_k)}{T}\right)
$$

where the sum runs over minimizers $\hat{u}_k$ and $H_k|_T$ is the constrained Hessian at $\hat{u}_k$ restricted to $T_{\hat{u}_k}\Sigma_m$. This is an $(n-1)$-dimensional Laplace integral on $\Sigma_m$.

---

## 3. Metastable Lifetime: Kramers Theory for SCC

### 3.1. Setup

SCC formations are metastable (T4, T7-Enhanced): they sit in local energy minima separated by saddle points. At finite $T$, thermal fluctuations drive transitions between metastable states. Kramers theory gives the mean escape time.

### 3.2. Kramers Formula on $\Sigma_m$

Let $\hat{u}$ be a metastable minimizer and $u_{\mathrm{sad}}$ the lowest saddle point on $\Sigma_m$ separating $\hat{u}$ from another basin. The mean first-passage time (Kramers escape time) is:

$$
\tau_{\mathrm{escape}} = \frac{2\pi}{|\lambda_{\mathrm{sad}}^{-}|} \cdot \sqrt{\frac{\det H(\hat{u})|_T}{|\det H(u_{\mathrm{sad}})|_T|}} \cdot \exp\!\left(\frac{\Delta}{T}\right)
$$

where:
- $\Delta = \mathcal{E}(u_{\mathrm{sad}}) - \mathcal{E}(\hat{u})$ is the **energy barrier height**
- $\lambda_{\mathrm{sad}}^{-}$ is the unique negative eigenvalue of $H(u_{\mathrm{sad}})|_T$ (the unstable direction at the saddle)
- The determinant ratio is a **prefactor** depending on basin geometry

The dominant factor is exponential: $\tau_{\mathrm{escape}} \sim \exp(\Delta / T)$.

### 3.3. SCC vs. Allen-Cahn Barrier Heights

**Critical distinction.** The T4/T7-Enhanced results concern Hessian eigenvalues (local curvature), not barrier heights (global energy landscape). The Hessian enhancement affects the prefactor in Kramers formula, not the exponential:

- **Hessian effect (prefactor):** The SCC Hessian has larger minimum eigenvalue than AC at minimizers. This increases $\det H(\hat{u})|_T$, which *increases* the prefactor — a modest contribution to longer escape times.

- **Barrier height effect (exponential):** Whether $\Delta_{\mathrm{SCC}} > \Delta_{\mathrm{AC}}$ is not controlled by the Hessian analysis alone. It requires knowing the saddle-point energy, which is a global property of the landscape.

**Conjecture (SCC-Barrier).** At well-formed formations on community-structured graphs, $\Delta_{\mathrm{SCC}} > \Delta_{\mathrm{AC}}$. The self-referential closure and separation terms create additional energetic penalties at the saddle point (where the field is poorly self-supporting and poorly distinguished), raising the barrier.

**Evidence.**

1. *Hessian curvature (local).* On a $10 \times 10$ grid with default parameters, the minimum Hessian eigenvalue at SCC minimizers is $\sim 2.0$ (H_CL_PSD_EVIDENCE.md), compared to $0$ for pure AC. This gives a quadratic lower bound on the barrier: $\Delta \geq \frac{1}{2}\mu_{\min} \cdot d^2$ where $d$ is the distance to the saddle.

2. *Saddle-point energy (heuristic).* The self-referential terms add $\lambda_{\mathrm{cl}} \|r_{\mathrm{sad}}\|^2 + \lambda_{\mathrm{sep}} \mathcal{E}_{\mathrm{sep}}(u_{\mathrm{sad}})$ to the saddle energy, where $r_{\mathrm{sad}} = \mathrm{Cl}(u_{\mathrm{sad}}) - u_{\mathrm{sad}}$ is the closure residual at the saddle. At saddle points, closure residuals are large (the field is poorly self-supporting), so this contribution is positive and likely significant.

3. *Sharp-interface limit (perturbative, from continuum-ext).* In the sharp-interface regime ($\varepsilon = \alpha/\beta \to 0$), the nucleation barrier scales as $\Delta \sim \sigma_{\mathrm{eff}}^d / (\Delta\mu)^{d-1}$ in $d$ dimensions. The effective surface tension satisfies $\sigma_{\mathrm{eff}} = \sigma_{\mathrm{AC}} + O(\varepsilon)$ with *positive* $O(\varepsilon)$ correction from the self-referential terms (CONTINUUM.md §7.4). This confirms SCC-Barrier for nucleation barriers in the near-sharp-interface regime, but the effect is perturbatively small — $O(\varepsilon)$ correction to $\sigma_{\mathrm{eff}}$ gives $O(\varepsilon)$ relative correction to $\Delta$.

**Regime analysis.** The sharp-interface confirmation (evidence 3) is rigorous but perturbative. The more interesting regime for SCC-Barrier is *moderate* $\varepsilon$ (finite interface width), where the self-referential terms are not perturbatively small relative to $\mathcal{E}_{\mathrm{bd}}$. In this regime, the Hessian lower bound (evidence 1) gives a floor but the actual barrier could be much larger. Resolving SCC-Barrier at moderate $\varepsilon$ requires numerical Morse theory.

**Required computation.** Finding saddle points on $\Sigma_m$ (e.g., via the dimer method or gentlest ascent dynamics) and comparing $\Delta_{\mathrm{SCC}}$ vs. $\Delta_{\mathrm{AC}}$ is a concrete numerical experiment. Priority should be on moderate-$\varepsilon$ configurations on community-structured graphs, where the self-referential corrections are largest.

### 3.4. Escape Time Ratio

For the prediction P3 (enhanced dwell times):

$$
\frac{\tau_{\mathrm{SCC}}}{\tau_{\mathrm{AC}}} = \underbrace{\frac{|\lambda_{\mathrm{sad,AC}}^{-}|}{|\lambda_{\mathrm{sad,SCC}}^{-}|}}_{\text{saddle curvature}} \cdot \underbrace{\sqrt{\frac{\det H_{\mathrm{SCC}}^{\min}}{|\det H_{\mathrm{SCC}}^{\mathrm{sad}}|} \cdot \frac{|\det H_{\mathrm{AC}}^{\mathrm{sad}}|}{\det H_{\mathrm{AC}}^{\min}}}}_{\text{geometry ratio}} \cdot \underbrace{\exp\!\left(\frac{\Delta_{\mathrm{SCC}} - \Delta_{\mathrm{AC}}}{T}\right)}_{\text{barrier enhancement}}
$$

If $\Delta_{\mathrm{SCC}} > \Delta_{\mathrm{AC}}$ (SCC-Barrier conjecture), the exponential factor dominates and SCC predicts *exponentially* longer dwell times at low noise — a strong, testable prediction.

---

## 4. Formation Fluctuation Spectrum

### 4.1. Gaussian Fluctuations Around a Minimizer

Near a minimizer $\hat{u}$, expand $u = \hat{u} + \delta u$ with $\delta u \in T_{\hat{u}}\Sigma_m$ (tangent space, i.e., $\sum_i \delta u_i = 0$). To quadratic order:

$$
\mathcal{E}(\hat{u} + \delta u) \approx \mathcal{E}(\hat{u}) + \frac{1}{2} \delta u^T H|_T \, \delta u
$$

where $H|_T = \Pi_T \nabla^2\mathcal{E}(\hat{u}) \Pi_T$ is the constrained Hessian on the tangent space. The Gibbs measure near $\hat{u}$ is approximately Gaussian:

$$
\delta u \sim \mathcal{N}\!\left(0,\; T \cdot (H|_T)^{-1}\right)
$$

The **fluctuation covariance** is $\Sigma_{\mathrm{fluct}} = T \cdot (H|_T)^{-1}$.

### 4.2. Eigenmode Decomposition

Let $\{(\mu_k, v_k)\}_{k=1}^{n-1}$ be the eigendecomposition of $H|_T$ on $T_{\hat{u}}\Sigma_m$, with $\mu_1 \leq \mu_2 \leq \cdots \leq \mu_{n-1}$. Then:

$$
\delta u = \sum_{k=1}^{n-1} a_k v_k, \qquad a_k \sim \mathcal{N}(0, T/\mu_k)
$$

- **Stiff modes** (large $\mu_k$): small fluctuations, $\mathrm{Var}(a_k) = T/\mu_k \ll 1$. These preserve the formation shape.
- **Soft modes** (small $\mu_k$): large fluctuations, $\mathrm{Var}(a_k) = T/\mu_k \gg 1$. These deform the formation.
- **Near-critical modes** ($\mu_k \to 0$): divergent fluctuations. These correspond to incipient instabilities — directions along which the formation shape is about to bifurcate.

### 4.3. SCC-Specific Spectral Structure

The SCC Hessian has three contributions:

$$
H|_T = \lambda_{\mathrm{cl}} \underbrace{[G + R_{\mathrm{cl}}]}_{\text{closure}} + \lambda_{\mathrm{sep}} \underbrace{H_{\mathrm{sep}}}_{\text{separation}} + \lambda_{\mathrm{bd}} \underbrace{H_{\mathrm{bd}}}_{\text{morphology}}
$$

where $G = 2(I - J_{\mathrm{Cl}})^T(I - J_{\mathrm{Cl}})$ is the Gauss-Newton term (PSD, minimum eigenvalue $\geq 2(1 - a_{\mathrm{cl}}/4)^2$) and $H_{\mathrm{bd}} = 4\alpha L + \beta \, \mathrm{diag}(W''(\hat{u}))$ is the Allen-Cahn Hessian.

**Key spectral difference from Allen-Cahn.** The soft modes of pure $H_{\mathrm{bd}}$ (eigenvectors of $L$ with small eigenvalue) receive a uniform positive shift from the closure Gauss-Newton term. This raises the *floor* of the fluctuation spectrum:

$$
\mu_k^{\mathrm{SCC}} \geq \mu_k^{\mathrm{AC}} + \lambda_{\mathrm{cl}} \cdot 2(1 - a_{\mathrm{cl}}/4)^2 - \lambda_{\mathrm{cl}} \delta_{\mathrm{res}} - \lambda_{\mathrm{sep}} \delta_{\mathrm{sep}}
$$

(using the notation from T4-METASTABILITY-REPAIR, Approach C). When the metastability condition $\lambda_{\mathrm{cl}}(\gamma_{\mathrm{GN}} - \delta_{\mathrm{res}}) > \lambda_{\mathrm{sep}} \delta_{\mathrm{sep}}$ holds, all SCC eigenvalues exceed their AC counterparts. This means:

1. **Reduced fluctuation amplitude**: $\mathrm{Var}(a_k)_{\mathrm{SCC}} < \mathrm{Var}(a_k)_{\mathrm{AC}}$ for all modes.
2. **Sharper formation boundaries**: the soft modes that blur formation boundaries are stiffened.
3. **Higher critical temperature**: the temperature at which $\mu_1 \to 0$ (formation instability) is higher for SCC.

### 4.4. Observable Predictions

The fluctuation spectrum generates measurable predictions:

**Fluctuation correlation function.** The spatial correlator of field fluctuations is:

$$
\langle \delta u(x) \, \delta u(y) \rangle_T = T \sum_k \frac{v_k(x) v_k(y)}{\mu_k}
$$

The dominant contribution comes from the softest mode ($k = 1$). For SCC, this mode is stiffer, so fluctuation correlations are shorter-ranged and smaller-amplitude than for AC. In perceptual terms: SCC formations have *less noisy boundaries* than equivalent AC formations at the same temperature.

**Participation ratio.** The fraction of sites significantly affected by fluctuations:

$$
\mathrm{PR} = \frac{\left(\sum_x \langle \delta u(x)^2 \rangle\right)^2}{n \sum_x \langle \delta u(x)^2 \rangle^2}
$$

Low PR indicates fluctuations are concentrated at the boundary (localized soft modes); high PR indicates diffuse fluctuations. For well-formed SCC formations, PR should be lower than AC (fluctuations more boundary-localized) because closure stiffens the interior.

---

## 5. Stochastic Formation Dynamics

### 5.1. Langevin Equation on $\Sigma_m$

The natural stochastic dynamics is a constrained Langevin equation (overdamped limit):

$$
\mathrm{d}u = -\Pi_{\Sigma}(\nabla \mathcal{E}(u)) \, \mathrm{d}t + \sqrt{2T} \, \Pi_{\Sigma} \, \mathrm{d}W_t
$$

where:
- $\Pi_{\Sigma}(v) = v - \bar{v}\mathbf{1}$ is the projection onto $T\Sigma_m$ (subtract mean), ensuring $\sum_i \mathrm{d}u_i = 0$
- $W_t$ is $n$-dimensional standard Brownian motion
- The projection $\Pi_{\Sigma}$ applied to both drift and noise ensures the dynamics stays on $\Sigma_m$

**Box constraint.** The constraint $u \in [0,1]^n$ requires reflection or projection at the boundary of the box. In practice, the double-well term drives $u$ toward $\{0, 1\}$, so box violations are rare for moderate $T$.

### 5.2. Detailed Balance and Reversibility

The Langevin dynamics satisfies detailed balance with respect to the Gibbs measure $\mu_T$:

$$
\mu_T(u) \, p(u \to v, \mathrm{d}t) = \mu_T(v) \, p(v \to u, \mathrm{d}t)
$$

This ensures that $\mu_T$ is the unique invariant measure (ergodicity on the compact domain $\Sigma_m \cap [0,1]^n$), and that time averages converge to Gibbs expectations.

### 5.3. Connection to Continuum SPDE

On a spatial domain $\Omega$ with mesh spacing $h$, the discrete Langevin equation converges (formally, as $h \to 0$) to the stochastic PDE provided by continuum-ext:

$$
\mathrm{d}u = \left[2\alpha \Delta u - \beta W'(u) - \lambda_{\mathrm{cl}} \frac{\delta \mathcal{E}_{\mathrm{cl}}}{\delta u} - \lambda_{\mathrm{sep}} \frac{\delta \mathcal{E}_{\mathrm{sep}}}{\delta u}\right] \mathrm{d}t + \sqrt{2T} \, \mathrm{d}\mathcal{W}_t
$$

where $\mathcal{W}_t$ is space-time white noise projected onto the volume constraint. This is a **stochastic Allen-Cahn equation with self-referential drift corrections** — a novel SPDE whose well-posedness (in the Da Prato-Zabczyk framework) is an open problem.

**Key question for well-posedness.** The self-referential terms $\delta\mathcal{E}_{\mathrm{cl}}/\delta u$ and $\delta\mathcal{E}_{\mathrm{sep}}/\delta u$ involve the sigmoid $\sigma(\cdot)$, which is globally Lipschitz and bounded. This regularity should suffice for local existence via standard semigroup methods, but the global existence and uniqueness of the SPDE is unproved.

### 5.4. Perceptual Switching as Noise-Driven Transitions

At moderate $T$, the stochastic dynamics produces transitions between metastable formations. This gives a model of **perceptual switching** (e.g., binocular rivalry, ambiguous figures):

- The system dwells near one formation for a random time $\sim \mathrm{Exp}(1/\tau_{\mathrm{escape}})$
- Then transitions rapidly through a saddle to an alternative formation
- Then dwells near the new formation, and so on

The dwell time distribution is approximately exponential at low $T$ (Kramers regime), with deviations toward gamma distribution at higher $T$ (multiple barrier-crossing attempts).

### 5.5. Noise-Induced Formation (Stochastic Resonance)

At intermediate $T$, noise can *assist* formation by helping the system cross the nucleation barrier from the uniform state $c\mathbf{1}$ to a structured formation. This is relevant when:

- $\beta/\alpha$ is near (but below) the phase transition threshold $4\lambda_2/|W''(c)|$
- The uniform state is the global minimizer, but structured formations exist as metastable states

Noise can push the system over the nucleation barrier, creating a *transient* formation that persists for a time $\sim \tau_{\mathrm{escape}}$ before dissolving. This is the stochastic analogue of perceptual organization in noisy, ambiguous stimuli.

---

## 6. Phase Transition in the Gibbs Measure

### 6.1. Order Parameter

Define the **formation order parameter** as the $\ell^2$ distance of the Gibbs-averaged field from the uniform state:

$$
\Phi(T) = \sqrt{\langle \|u - c\mathbf{1}\|^2 \rangle_T / n}
$$

- $\Phi = 0$: the Gibbs measure concentrates on the uniform field (disordered phase)
- $\Phi > 0$: the Gibbs measure has weight on structured formations (ordered phase)

### 6.2. Critical Temperature

The system undergoes a **disorder-to-order transition** as $T$ decreases below a critical temperature $T_c$. By analogy with the Ginzburg-Landau theory:

$$
T_c \approx \frac{\beta |W''(c)| - 4\alpha \lambda_2}{C_{\mathrm{eff}}}
$$

where $C_{\mathrm{eff}}$ is a constant depending on the geometry and the self-referential corrections. This connects to T8-Core: the phase transition condition $\beta/\alpha > 4\lambda_2/|W''(c)|$ ensures $T_c > 0$ (the ordered phase exists at some positive temperature).

### 6.3. Effect of Self-Referential Terms

The self-referential SCC terms modify $T_c$ relative to pure Allen-Cahn:

- **Closure term $\mathcal{E}_{\mathrm{cl}}$:** At the uniform field, $\mathrm{Cl}(c\mathbf{1}) = \sigma(a_{\mathrm{cl}}(c - \tau)) \cdot \mathbf{1} \neq c\mathbf{1}$ (unless $c$ is the closure fixed point $c^*$). So $\mathcal{E}_{\mathrm{cl}}(c\mathbf{1}) > 0$, which raises the energy of the disordered state and *lowers* $T_c$ (makes formation *easier*).

- **Separation term $\mathcal{E}_{\mathrm{sep}}$:** At the uniform field, $D(c\mathbf{1}) \approx 0.5$ (no asymmetry), so $\mathcal{E}_{\mathrm{sep}}(c\mathbf{1}) = c \cdot n \cdot 0.5 > 0$. This also penalizes the disordered state. At well-formed formations, $\mathcal{E}_{\mathrm{sep}}$ is smaller (high distinction). So the separation term also *lowers* $T_c$.

**Net effect.** Both self-referential terms penalize the disordered state more than the ordered state, lowering $T_c$ and expanding the regime where formations are thermodynamically favored. SCC formations survive to *higher temperatures* than AC formations on the same graph.

---

## 7. Large Deviation Theory

### 7.1. Rate Function

The large deviation principle governs rare fluctuations. As $T \to 0$:

$$
\mu_T(u \in B) \asymp \exp\left(-\frac{1}{T} \inf_{u \in B} I(u)\right)
$$

where the **rate function** is:

$$
I(u) = \mathcal{E}(u) - \mathcal{E}(\hat{u})
$$

relative to the global minimizer $\hat{u}$. The rate function measures the "cost" of observing the system at configuration $u$ rather than at the minimizer.

### 7.2. Formation Basin at Temperature $T$

The **thermal basin** of a metastable formation $\hat{u}$ at temperature $T$ is the set of configurations that are "thermally accessible":

$$
\mathcal{B}_T(\hat{u}) = \{u \in \Sigma_m : I(u) \leq T \cdot (n-1) \cdot C\}
$$

where $C$ is a constant (formally $C = \frac{1}{2} + \varepsilon$ for any $\varepsilon > 0$, from concentration of measure). The thermal basin is larger than the deterministic basin (the Morse-theoretic basin of attraction of $\hat{u}$ under gradient flow); it includes configurations that the system can reach via thermal fluctuations.

**SCC thermal basins are more confined.** The enhanced Hessian curvature (T7-Enhanced) makes the energy grow faster away from $\hat{u}$, so $\mathcal{B}_T(\hat{u})$ is smaller for SCC than for AC at the same $T$. The formation stays "closer to its ideal shape" under thermal perturbation.

### 7.3. Transition Paths

The most probable transition path from $\hat{u}_1$ to $\hat{u}_2$ (two metastable formations) minimizes the Freidlin-Wentzell action functional:

$$
S[\gamma] = \frac{1}{2} \int_0^1 \left\|\dot{\gamma}(s) + \Pi_\Sigma \nabla\mathcal{E}(\gamma(s))\right\|^2 \mathrm{d}s
$$

over paths $\gamma : [0,1] \to \Sigma_m$ with $\gamma(0) = \hat{u}_1$, $\gamma(1) = \hat{u}_2$. The minimizing path passes through the lowest saddle point and follows the gradient flow in reverse on the exit side.

The self-referential terms modify the action landscape: because $\nabla\mathcal{E}_{\mathrm{cl}}$ and $\nabla\mathcal{E}_{\mathrm{sep}}$ are nonlinear and field-dependent, the optimal transition path is not a simple interpolation between formations. The closure term penalizes paths that pass through poorly self-supporting intermediate states, channeling transitions through configurations that maintain some degree of closure even at the saddle.

---

## 8. Connection to Empirical Predictions

### 8.1. P3: Enhanced Dwell Times in Binocular Rivalry

**Prediction.** SCC predicts longer dwell times than Allen-Cahn in bistable perception tasks.

**Mechanism.** From Kramers theory (§3.4):

$$
\frac{\tau_{\mathrm{SCC}}}{\tau_{\mathrm{AC}}} = (\text{prefactor ratio}) \cdot \exp\!\left(\frac{\Delta_{\mathrm{SCC}} - \Delta_{\mathrm{AC}}}{T}\right)
$$

The prefactor ratio is $O(1)$ and depends on Hessian determinants. The exponential factor depends on the barrier height difference. If SCC-Barrier conjecture holds ($\Delta_{\mathrm{SCC}} > \Delta_{\mathrm{AC}}$), the ratio grows exponentially as $T$ decreases.

**Testable form.** Plot $\log(\tau_{\mathrm{dwell}})$ vs. $1/T_{\mathrm{noise}}$ for SCC and AC models. SCC should have a steeper slope (larger effective $\Delta$). The slope difference estimates $\Delta_{\mathrm{SCC}} - \Delta_{\mathrm{AC}}$.

### 8.2. P4: Path Dependence

**Prediction.** Different noise histories lead to different metastable formations, with the distribution of outcomes reflecting the basin landscape.

**Mechanism.** The non-idempotent closure creates a more complex energy landscape with more metastable minima than AC. Different noise realizations in the Langevin dynamics explore different basins. The distribution of final formations at time $t$ samples the Gibbs measure weighted by basin areas:

$$
P(\text{formation } k) \approx \frac{\mathrm{Vol}(\mathcal{B}(\hat{u}_k))}{\sum_j \mathrm{Vol}(\mathcal{B}(\hat{u}_j))} + O(e^{-\Delta_{\min}/T})
$$

at moderate $T$, where $\Delta_{\min}$ is the smallest barrier height.

**Testable form.** Run many independent Langevin trajectories from the same initial condition. Measure the variance of the final formation across realizations. SCC should show *greater* variance (more basins) than AC.

### 8.3. P5: Noise-Assisted Formation

**Prediction.** At intermediate noise levels, noise *helps* formation nucleation.

**Mechanism.** From §5.5: when the system is near the phase transition threshold but the uniform state is energetically preferred, noise can push the system over the nucleation barrier. The optimal noise level for formation is:

$$
T_{\mathrm{opt}} \sim \Delta_{\mathrm{nuc}} / \log(n)
$$

where $\Delta_{\mathrm{nuc}}$ is the nucleation barrier. Below $T_{\mathrm{opt}}$, formation is too slow; above $T_{\mathrm{opt}}$, the formation dissolves too quickly. This non-monotonic dependence on noise is a signature of stochastic resonance.

---

## 9. Open Problems

### 9.1. Computational

1. **Saddle-point computation.** Find saddle points on $\Sigma_m$ via dimer method or gentlest ascent dynamics. Compare $\Delta_{\mathrm{SCC}}$ vs. $\Delta_{\mathrm{AC}}$ on test graphs. This resolves the SCC-Barrier conjecture.

2. **Langevin simulation.** Implement the constrained Langevin dynamics and measure dwell time distributions. Verify the exponential dependence $\log \tau \sim \Delta/T$.

3. **Fluctuation spectrum measurement.** Compute Hessian eigenvalues at formation minimizers. Compare the soft-mode structure between SCC and AC.

### 9.2. Theoretical

4. **SPDE well-posedness.** Prove existence and uniqueness of the continuum stochastic SCC equation (§5.3) in the Da Prato-Zabczyk framework.

5. **Critical temperature computation.** Derive $T_c$ for the order-disorder transition on specific graph families (grids, community graphs). Prove that $T_c^{\mathrm{SCC}} > T_c^{\mathrm{AC}}$.

6. **Barrier height bounds.** Prove (or disprove) $\Delta_{\mathrm{SCC}} > \Delta_{\mathrm{AC}}$ under natural parameter conditions. This may require Morse-theoretic analysis of the energy landscape.

7. **Non-equilibrium extensions.** The Gibbs measure assumes equilibrium. Time-dependent perceptual stimuli require a non-equilibrium treatment (e.g., Jarzynski equality for driven formation transitions).

### 9.3. Connections to Other Extensions

8. **Block-spin RG requires stochastic theory (multiscale-ext).** The block-spin renormalization group transformation (MULTISCALE.md §8.2) integrates out intra-block fluctuations, producing a coarse-grained energy $\mathcal{E}_{\mathrm{coarse}} = \mathcal{E}_{\mathrm{mean\text{-}field}} - T \cdot S_{\mathrm{intra}}$. The deterministic SCC ($T = 0$) captures only the mean-field part; the entropic correction $T \cdot S_{\mathrm{intra}}$ from intra-block thermal fluctuations is exactly what the stochastic extension provides. Two specific consequences:

   - **Effective double-well weakening.** Intra-block fluctuations reduce the effective double-well depth: $\beta_{\mathrm{eff}} < \beta$. This is the standard Wilson-Fisher mechanism — thermal fluctuations soften the phase transition. For SCC, the enhanced Hessian stiffness (T7-Enhanced) means intra-block fluctuations are *smaller* than for AC (§4.3), so $\beta_{\mathrm{eff}}^{\mathrm{SCC}} > \beta_{\mathrm{eff}}^{\mathrm{AC}}$. SCC formations are more robust to coarse-graining.

   - **Rigorous coarse-graining.** The Gibbs measure $\mu_T$ (§1) provides the proper probability space for computing block-spin averages. The marginal of $\mu_T$ over intra-block degrees of freedom defines the coarse-grained Gibbs measure $\mu_T^{\mathrm{coarse}}$, which is the starting point for RG flow analysis. Without the stochastic extension, this construction is unavailable.

9. **Scale-dependent temperature.** The temperature $T$ may vary across spatial scales (multiscale-ext). A hierarchical stochastic model with scale-dependent noise $T(\ell)$ at scale $\ell$ would connect to the multiscale extension, with the RG flow determining how $T(\ell)$ evolves under coarse-graining.

10. **Dynamics coupling.** The Langevin dynamics interfaces with the temporal dynamics (dynamics-ext) through the transport term. At finite $T$, noise-induced formation changes could trigger transport kernel updates — a stochastic generalization of the temporal persistence framework.

---

## 10. Summary of Key Results

| Result | Status | Reference |
|--------|--------|-----------|
| Gibbs measure $\mu_T \propto \exp(-\mathcal{E}/T)$ on $\Sigma_m$ | Defined | §1 |
| Free energy $F(T)$ and Laplace approximation | Derived | §2 |
| Kramers escape time for SCC formations | Derived (modulo SCC-Barrier) | §3 |
| SCC fluctuation spectrum stiffer than AC | Conditional on T4 metastability condition | §4 |
| Constrained Langevin dynamics on $\Sigma_m$ | Formulated | §5 |
| Order-disorder transition at $T_c$ | Identified, not quantified | §6 |
| Large deviation rate function $I(u) = \mathcal{E}(u) - \mathcal{E}(\hat{u})$ | Standard | §7 |
| Enhanced dwell time prediction (P3) | Conditional on SCC-Barrier conjecture | §8.1 |
| Path dependence prediction (P4) | Qualitative | §8.2 |
| Noise-assisted formation prediction (P5) | Qualitative | §8.3 |
| Block-spin RG entropic corrections | Framework identified | §9.3 |

**Central open conjecture.** SCC-Barrier: $\Delta_{\mathrm{SCC}} > \Delta_{\mathrm{AC}}$ at well-formed formations on structured graphs. This is the load-bearing conjecture for the stochastic extension's quantitative predictions. If false, SCC and AC have similar escape times and the theory loses its strongest stochastic signature.
