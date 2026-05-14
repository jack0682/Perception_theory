> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]

# 03a_pf_framework_axiom_proposal_v0.md — P-F Framework Axiom Set v0

**Session:** 2026-05-06 (W6 Day 3 G3.3, sub-file of `03_pf_framework_escalation_core.md`).
**Goal:** P-F axiom set v0 (8 axioms, Cat C sketch). Substantive starting point for W9 v1 formalism.
**Status:** All axioms are v0 sketches (Cat C). W9 D1 target: v1 with existence proofs.
**Hard constraint:** These are proposals for a *working draft* framework; no canonical claims without P-F are modified. All existing deterministic results remain valid in the $T_* = 0$ limit.

---

## §1. Motivation: The P-F Framework Problem

SCC canonical theory is formulated for *deterministic* gradient flow on $\Sigma_M$:
$$\frac{d\mathbf{u}}{dt} = -\nabla_{\Sigma_M} \mathcal{E}(\mathbf{u})$$
(projected gradient, with simplex projection at each step in the discrete implementation).

The P-F (Probabilistic / Finite-Temperature) framework replaces or augments this with a *stochastic* dynamics that admits:
1. Escape from local minima (non-zero probability even at low noise).
2. K-jumps (formation birth/merger events) as stochastic transitions.
3. A well-defined stationary distribution on $\Sigma_M$ (or $\widetilde{\widetilde\Sigma}^K_M$).
4. Quantitative escape rates (Kramers) connecting energy landscape geometry to kinetic selection.

---

## §2. Axiom Set v0 (P-F-A1 through P-F-A8)

### P-F-A1: Stochastic Perturbation Source (Langevin equation)

The SCC cohesion field dynamics on $\Sigma_M$ are augmented with finite-temperature noise:
$$d\mathbf{u}_t = -\nabla_{\Sigma_M} \mathcal{E}(\mathbf{u}_t)\, dt + \sqrt{2 k_B T_*}\, dW_t^{\Sigma_M}$$
where:
- $T_* > 0$ is the *effective temperature* (noise scale, to be calibrated; $T_* = 0$ recovers deterministic flow).
- $W_t^{\Sigma_M}$ is a Wiener process on $\Sigma_M$ (Brownian motion on the simplex face, with respect to the flat metric).
- $k_B$ is a scaling constant (may be absorbed into $T_*$ without loss of generality; keep for physical analogy).
- The projection onto $\Sigma_M$ is maintained by the constraint structure (Lagrange multiplier or projected Euler-Maruyama).

*v0 status:* Existence and uniqueness of the SDE solution on $\Sigma_M$ (a compact convex polytope) is expected from standard SDE theory on compact manifolds (Hsu 2002; Driver 1992); formal proof deferred to W9 D1.

### P-F-A2: Markov Property

The process $\mathbf{u}_t$ defined by P-F-A1 satisfies the Markov property: the conditional distribution of $\mathbf{u}_{t+s}$ given $\{\mathbf{u}_r : r \leq t\}$ depends only on $\mathbf{u}_t$.

*Justification:* Standard consequence of the Itô SDE structure (P-F-A1).

### P-F-A3: Stationary Distribution (Boltzmann-like)

At long times, $\mathbf{u}_t$ converges in distribution to the Gibbs measure:
$$p_*(\mathbf{u}) \propto \exp\!\left(-\frac{\mathcal{E}(\mathbf{u})}{T_*}\right) \cdot \mathbf{1}_{\Sigma_M}(\mathbf{u})$$
(the Boltzmann distribution on $\Sigma_M$ with energy $\mathcal{E}$ and temperature $T_*$).

*v0 status:* Detailed balance argument: $p_*$ satisfies the Fokker-Planck equation $\partial_t p = \nabla \cdot (p \nabla \mathcal{E}) + T_* \Delta p = 0$ (stationary). Existence of $p_*$ as a probability measure: $\mathcal{E}$ is bounded below (by 0, since all energy terms $\geq 0$) and $\Sigma_M$ is compact, so $\exp(-\mathcal{E}/T_*)$ is integrable. ✓ (rigorous). Convergence to $p_*$: requires spectral gap argument (hypoellipticity on $\Sigma_M$); deferred to W9 D1.

*P-F-A3 connection to CN15 (Static/Dynamic Separation):* Under P-F, long-time $K_{\mathrm{act}}$ distribution is $P_{eq}(K | T_*)$ derived from $p_*$. This gives quantitative meaning to CN15's "protocol-endpoint $K_{\mathrm{act}}$" in the stochastic setting.

### P-F-A4: Arrhenius Escape Rate

From a local minimum $\hat{\mathbf{u}} \in \Sigma_M$ with energy $\mathcal{E}(\hat{\mathbf{u}})$, the escape rate over an energy barrier $\Delta E$ is:
$$\Gamma_{\mathrm{esc}} \sim A \cdot \exp\!\left(-\frac{\Delta E}{T_*}\right)$$
where $A > 0$ is a prefactor and $\Delta E = \mathcal{E}(\mathbf{u}_{\mathrm{saddle}}) - \mathcal{E}(\hat{\mathbf{u}})$ is the barrier height (energy difference to the relevant saddle point on $\Sigma_M$).

*v0 status:* This is the Arrhenius law / Kramers (1940) result. Formal derivation requires: (a) existence of a saddle point $\mathbf{u}_{\mathrm{saddle}}$ connecting $\hat{\mathbf{u}}$ to the neighboring basin; (b) non-degeneracy of the Hessian at saddle (one negative eigenvalue); (c) the Eyring-Kramers prefactor formula. These are all computable from the existing energy framework.

### P-F-A5: Mean First Passage Time (MFPT)

The mean time to escape from the basin of $\hat{\mathbf{u}}$ is:
$$\tau_{\mathrm{MFPT}} \approx \frac{2\pi}{|\lambda_-|} \sqrt{\frac{\det H_{\hat{\mathbf{u}}}}{\left|\det' H_{\mathbf{u}_{\mathrm{saddle}}}\right|}} \cdot \exp\!\left(\frac{\Delta E}{T_*}\right)$$
where:
- $H_{\hat{\mathbf{u}}} = \nabla^2 \mathcal{E}|_{\hat{\mathbf{u}}}$ (Hessian at minimum, restricted to $T_{\hat{\mathbf{u}}} \Sigma_M$).
- $H_{\mathbf{u}_{\mathrm{saddle}}}$ = Hessian at saddle; $\det'$ = product of all eigenvalues except the unique negative one; $|\lambda_-|$ = magnitude of the negative eigenvalue.

This is the *Eyring-Kramers formula* (Hänggi-Talkner-Borkovec 1990, Eq. 4.56). All quantities are computable from `scc/energy.py` (energy + gradient + Hessian).

*v0 status:* The formula is correct in the 1D Kramers setting and generalizes to multi-dimensional Langevin under the "harmonic transition state theory" approximation. The extension to $\Sigma_M$ (constrained manifold) requires careful treatment of the constraint geometry; deferred to W9 D2.

### P-F-A6: K-Jump Stochastic Transition Rates

Under P-F dynamics, the active formation count $K_{\mathrm{act}}$ undergoes stochastic jumps. The rate for $K \to K-1$ (merger) and $K \to K+1$ (birth) transitions are:
$$k_{K \to K-1} = A_{K \to K-1} \cdot \exp\!\left(-\frac{\Delta E_{K \to K-1}}{T_*}\right), \qquad k_{K \to K+1} = A_{K \to K+1} \cdot \exp\!\left(-\frac{\Delta E_{K \to K+1}}{T_*}\right)$$
where $\Delta E_{K \to K \pm 1}$ are the energy barriers for the respective transitions on $\Sigma_M$ (passage from K-formation basin to $(K\pm 1)$-formation basin via the separating saddle).

**N-1 Soft-Hard Asymmetry recovery:** $\Delta E_{K \to K+1} > \Delta E_{K \to K-1}$ (birth barrier > merger barrier) → $k_{K \to K+1} \ll k_{K \to K-1}$ at low $T_*$ → merger dominates → $K_{\mathrm{act}}$ is non-increasing on average at low temperature. This recovers N-1 as the $T_* \to 0$ limit of P-F-A6. ✓

*v0 status:* The barriers $\Delta E_{K \to K \pm 1}$ are geometric quantities (energy landscape on $\Sigma_M$); the prefactors $A_{K \to K \pm 1}$ require Eyring-Kramers formula applied to the K-formation regime boundary. Deferred to OP-0005 Layer B (W9 D2).

### P-F-A7: Calibration of $T_*$

The effective temperature $T_*$ proxies the following physical sources in SCC implementations:
- **Gradient noise** $\sigma_{\nabla}$: additive noise on gradient steps in the numerical optimizer.
- **IC distribution width** $\sigma_{\mathrm{IC}}$: variance of the initial cohesion field $u_0$.
- **Numerical solver tolerance** $\delta_{\mathrm{tol}}$: finite-step approximation error.

In the simplest calibration: $T_* \approx \sigma_{\nabla}^2 / (2 \eta)$ where $\eta$ is the learning rate (analogous to the Einstein relation $D = k_B T / \gamma$ with diffusion coefficient $D = \sigma_{\nabla}^2 \eta / 2$ and friction $\gamma = 1$).

*v0 status:* This is an informal calibration sketch. W9 D1 task: derive the precise $T_*$ calibration from the actual numerical scheme in `scc/optimizer.py` (BB step + simplex projection); check whether the noise in the numerical flow is well-modeled by additive Gaussian.

### P-F-A8: Zero-Temperature Reduction

In the limit $T_* \to 0$, the P-F framework recovers the deterministic SCC theory:
- P-F-A1 → deterministic gradient flow $\dot{\mathbf{u}} = -\nabla_{\Sigma_M} \mathcal{E}$.
- P-F-A3 → $p_*$ concentrates on the global minimizers of $\mathcal{E}$ (Laplace approximation).
- P-F-A4, P-F-A5 → escape rates → 0 (barriers infinite relative to $T_*$); metastable basins become permanent.
- P-F-A6 → K-jump rates → 0 for birth ($\Delta E_{K \to K+1} > 0$); merger rates → 0 more slowly (N-1 asymmetry preserved in ratio).

This ensures **backward compatibility**: all canonical deterministic results remain valid in the $T_* = 0$ limit of the P-F framework.

---

## §3. Summary

| Axiom | Content | Status | W9 work |
|---|---|---|---|
| P-F-A1 | Langevin on $\Sigma_M$ with $T_*$ | Cat C sketch | W9 D1 existence proof |
| P-F-A2 | Markov property | Trivial from A1 | — |
| P-F-A3 | Boltzmann stationary distribution | $p_*$ existence rigorous; convergence sketch | W9 D1 spectral gap |
| P-F-A4 | Arrhenius escape rate | Standard Kramers result | W9 D2 $\Sigma_M$ adaptation |
| P-F-A5 | MFPT Eyring-Kramers formula | Standard; $\Sigma_M$ constraint treatment needed | W9 D2 |
| P-F-A6 | K-jump stochastic rates + N-1 recovery | Cat C sketch; asymmetry recovered ✓ | W9 D2 (OP-0005 Layer B) |
| P-F-A7 | $T_*$ calibration from numerical noise | Informal; needs precise derivation | W9 D1 |
| P-F-A8 | Zero-T reduction (backward compatibility) | Trivial from A1-A6 | — |

**P-F Axiom v0 = Cat C target.** W9 D1 refines to v1 (Cat B target with explicit proof sketches for A1, A3 convergence, A5 on $\Sigma_M$).

---

## §4. Addendum: $\mathcal{P}$-Conditioning (2026-05-07)

*Added during Phase 4 file review (Canonical Memo v1.1). No axiom text altered above.*

**Correction note for A4, A5, A6.** In the stereo-SCC setting, the state space $\Sigma_M$ depends
parametrically on the 3D point cloud $\mathcal{P}_t$ (the graph structure $\mathcal{G}^P_t$ changes
with scene/camera motion). The barriers in A4–A6 should be understood as $\mathcal{P}$-conditioned:

- **A4**: $\Delta E = \Delta E(\mathcal{P})$ — barrier height depends on $\mathcal{G}^P$ (depth-filtered
  adjacency raises merger barriers between depth-separated formations).
- **A5**: $H_{\hat{\mathbf{u}}}$ and $H_{\mathbf{u}_\mathrm{saddle}}$ both depend on $\mathcal{P}$ via the
  Laplacian of $\mathcal{G}^P$.
- **A6**: $k_{K \to K-1}(\mathcal{P})$ — rates are $\mathcal{P}$-conditional; the effective Markov
  chain over $K_\mathrm{act}$ has time-varying rates $\Gamma^{K \to K'}(\mathcal{P}_t)$ as $\mathcal{P}_t$
  changes (non-autonomous Markov process, BO-reduced).

The single-field formulation $\Sigma_M$ in A1 is **correct** — this file already uses $\Sigma_M$
(not $\Sigma_M^K$), consistent with Canonical Memo v1.1 §D3. The P-F-A1 Langevin on $\Sigma_M$
should be read as $\Sigma_M(\mathcal{P}_t)$ in the stereo setting (parametrically varying with $\mathcal{P}_t$).

**Forward reference:** `stereo_observation_framework.md` §5–§6 derives the $\mathcal{P}$-conditioned
BO + Kramers structure in detail; `k_selection_b_kramers.md` §3.2 has the barrier definition
$\Delta\mathcal{E}^{(jk)}(\mathcal{P})$.

---

**End of `03a_pf_framework_axiom_proposal_v0.md`. P-F axiom set v0 complete (8 axioms, Cat C). G3.3 sub-file §a done. §4 addendum: P-conditioning for A4/A5/A6 in stereo setting (2026-05-07).**
