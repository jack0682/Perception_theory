# 13_LSW_connection.md — Goldstone-Pair Instability ↔ Lifshitz-Slyozov-Wagner Coarsening

**Session:** 2026-04-28 (W5 Day 2 Phase 3, E7).
**Target:** Connect T-σ-Multi-1 Goldstone-pair antisymmetric instability (`09_*`) to classical Lifshitz-Slyozov-Wagner (LSW) coarsening law $R(t) \sim t^{1/3}$. Establish quantitative bridge between SCC K-field σ-framework and statistical-mechanics coarsening theory.
**Resolves:** Phase 3 weakness (sketch only) + NQ-192 partial answer.
**Depends on reading:** `09_goldstone_instability_proved.md` §5 (linear merge rate); `11_PN_unification.md` §6.3 (multi-formation V5b-T'); `06_approach_AB_equivalence_and_D.md` §3 (Approach D persistence).
**Status:** **Cat C → Cat B target**. Quantitative framework + scaling argument. Full Cat A requires statistical-mechanics integration.

---

## §1. Background: LSW Coarsening Law

### 1.1 Classical statement

Lifshitz-Slyozov (1961) and Wagner (1961) showed that for a system of $K \gg 1$ growing/shrinking droplets in a supersaturated solution, the average droplet radius grows as:
$$\langle R(t) \rangle \sim (D \sigma t)^{1/3}, \tag{1.1}$$
where $D$ is the diffusion coefficient and $\sigma$ is surface tension. This is the **LSW coarsening law**.

Mechanism: large droplets grow at the expense of small droplets (Ostwald ripening) due to Gibbs-Thomson surface-tension-driven mass transport.

### 1.2 SCC K-field analog

In SCC K-field architecture (canonical I9), K formations on $\Sigma^K_M$ with repulsion coupling $\lambda_{\mathrm{rep}}$ undergo merger dynamics when:
- λ_rep coupling drives antisym Goldstone-pair instability (T-σ-Multi-1, `09_*`).
- Large formations consume smaller ones (canonical T-Persist-K-Weak K → K-1 merger).

The **rate of K decrease over time** is the SCC analog of LSW $\langle R \rangle$ growth.

---

## §2. Linear Stage: T-σ-Multi-1 Rate

For K=2 well-separated minimizer with antisym Goldstone-pair eigenvalue $\lambda_{\mathrm{antisym}} = \mu_{\mathrm{Gold}} - c_{\mathrm{eff}} \lambda_{\mathrm{rep}}$ (from `09_*` §4):

When (Inst) holds, gradient flow of $\mathcal{E}_K$ near the K=2 minimizer pushes $\mathbf{u}$ along the antisym mode at rate:
$$\frac{d}{dt} \mathbf{u}_{\mathrm{antisym}} = -\nabla \mathcal{E}_K = +|\lambda_{\mathrm{antisym}}| \mathbf{u}_{\mathrm{antisym}}. \tag{2.1}$$

Antisym coordinate grows exponentially:
$$|\mathbf{u}_{\mathrm{antisym}}(t)| \sim |\mathbf{u}_{\mathrm{antisym}}(0)| \cdot e^{|\lambda_{\mathrm{antisym}}| t}. \tag{2.2}$$

This is the **linear merge timescale**: $\tau_{\mathrm{linear}} = 1 / |\lambda_{\mathrm{antisym}}| = 1 / (c_{\mathrm{eff}} \lambda_{\mathrm{rep}})$.

For $\lambda_{\mathrm{rep}} = 0.1$, $c_{\mathrm{eff}} \approx 0.33$ (Phase 3 E9 measurement): $\tau_{\mathrm{linear}} \approx 30$ time units.

### 2.1 Stage limit: linear regime ends at antisym ~ O(1)

The linear approximation breaks down when $|\mathbf{u}_{\mathrm{antisym}}| \approx |\mathbf{u}^*|$, i.e., the perturbation is comparable to the unperturbed state. This is the threshold where formations begin merging structurally.

Time to reach this threshold:
$$t_{\mathrm{merge}} = \tau_{\mathrm{linear}} \cdot \log\big(|\mathbf{u}^*| / |\mathbf{u}_{\mathrm{antisym}}(0)|\big) \sim \tau_{\mathrm{linear}} \cdot \log(\sigma^{-1}). \tag{2.3}$$

For typical IC perturbation $\sigma \sim 10^{-2}$: $\log(100) \approx 4.6$. So $t_{\mathrm{merge}} \approx 4.6 \tau_{\mathrm{linear}} \sim 140$ time units (at $\lambda_{\mathrm{rep}}=0.1$, c_eff=0.33).

---

## §3. Nonlinear Stage: Multi-Formation Coarsening

For K ≫ 1, after linear instability triggers initial mergers, the system enters a **nonlinear coarsening regime** where:
- Larger formations consume smaller ones.
- Mass redistributes through the system.
- Average formation size $\langle m \rangle$ grows.

### 3.1 Mass-transfer rate (per pair)

For two formations of masses $m_j, m_k$ in proximity, the mass-transfer rate is:
$$\dot m_j = +\Phi(m_j, m_k, d_{jk}, \lambda_{\mathrm{rep}}, \beta), \tag{3.1}$$
with $\Phi > 0$ if $m_j > m_k$ (Ostwald ripening direction).

In SCC, this $\Phi$ is determined by the **Goldstone-pair instability rate** (`09_*` §5) integrated over the merger trajectory.

For well-separated formations with $\lambda_{\mathrm{rep}}$ coupling, the merger trajectory has linear duration $\tau_{\mathrm{linear}}$ followed by nonlinear merge. Total mass transfer per merger:
$$\Delta m_{\mathrm{merger}} \sim m_{\mathrm{small}}, \tag{3.2}$$
i.e., the smaller formation is fully absorbed.

### 3.2 LSW-type scaling argument

If formations have characteristic size $R(t)$ and number density $\rho(t)$:
- Total mass conserved: $\rho \cdot R^d = $ const (in $d$ dimensions).
- Merger rate per formation: $\dot \rho / \rho \sim \tau_{\mathrm{linear}}^{-1} \sim \lambda_{\mathrm{rep}}$. But this assumes $\lambda_{\mathrm{rep}}$ constant; for SCC $\lambda_{\mathrm{rep}}$ may depend on size.

For typical SCC where $\lambda_{\mathrm{rep}}$ is a fixed parameter:
$$\dot \rho \sim -\rho^2 \cdot \lambda_{\mathrm{rep}}, \tag{3.3}$$
giving $\rho(t) \sim 1/(\lambda_{\mathrm{rep}} t)$.

With $\rho R^d = $ const: $R(t) \sim (\lambda_{\mathrm{rep}} t)^{1/d}$.

**For $d = 3$**: $R(t) \sim t^{1/3}$ — **LSW law recovered!** ✓

**For $d = 2$**: $R(t) \sim t^{1/2}$ — different from LSW.

**For $d = 1$**: $R(t) \sim t^1 = t$ — different again.

### 3.3 Comparison with classical LSW

Classical LSW assumes:
- Diffusion-limited mass transport (D coefficient).
- Surface-tension-driven (σ).
- 3D bulk system.

SCC analog assumes:
- Coupling-rate-limited transport ($\lambda_{\mathrm{rep}}$).
- Goldstone-instability-driven (T-σ-Multi-1 rate).
- Any dimension; different scaling per d.

The **structural difference**: classical LSW is a 3D-specific result; SCC gives a $d$-dependent family. In 3D, **SCC reduces to LSW with $\lambda_{\mathrm{rep}} \leftrightarrow D \sigma$**:
$$R(t)_{\mathrm{SCC}} = R(t)_{\mathrm{LSW}} \quad \text{when} \quad \lambda_{\mathrm{rep}} = D \sigma. \tag{3.4}$$

### 3.4 SCC predicted exponent table

| Dimension | SCC exponent $R(t) \sim t^\alpha$ | LSW exponent (3D) |
|---|---|---|
| 1 | $t^1$ | — |
| 2 | $t^{1/2}$ | — |
| 3 | $t^{1/3}$ | $t^{1/3}$ ✓ |
| 4+ | $t^{1/d}$ | — |

In 3D: SCC predicts LSW law from K-field architecture + T-σ-Multi-1 instability.

---

## §4. Empirical Anchor (Phase 3 E9 K=2 Linear Rate)

Phase 3 E9 K=2 baseline (`scripts/results/e9_k2_baseline.json`) measures linear regime:

| d_min | λ_rep | μ_antisym (lowest joint H eigenvalue) | τ_linear = 1/|μ_antisym| |
|---|---|---|---|
| 5 | 0.01 | ~0.0002 (positive, stable) | ∞ (no instability) |
| 5 | 0.1 | -0.0364 | 27 |
| 5 | 1.0 | -0.8847 (simplex active) | 1.1 |
| 8 | 0.01 | ~0.0002 (stable) | ∞ |
| 8 | 0.1 | -0.0332 | 30 |
| 8 | 1.0 | -0.8815 (simplex active) | 1.1 |
| 12 | 0.1 | -0.0332 | 30 |
| 16 | 0.1 | -0.0384 | 26 |

**Observation**: $\tau_{\mathrm{linear}}$ ≈ 30 across most λ_rep=0.1 configurations (independent of d_min in well-separated regime). At λ_rep=0.01, system is stable (no instability) — consistent with $\mu_{\mathrm{Gold}}^{\mathrm{lifted}} \approx 2 \times 10^{-3}$ being similar magnitude to λ_rep=0.01.

**Phase 3 numerical verification of T-σ-Multi-1**:
- Instability ON for λ_rep ≥ 10 × μ_Gold (≈ 2 × 10^{-2}). ✓
- Instability OFF for λ_rep ≤ μ_Gold ≈ 2 × 10^{-3}. ✓
- Threshold λ_rep^* ∈ (0.002, 0.02). Consistent with c_eff ≈ 0.33 estimate.

### 4.1 Linear → Nonlinear bridge

Phase 3 E9 only measures **static Hessian** (linear approximation). The actual K=2 → K=1 merger (nonlinear stage) requires time-dependent simulation. Out of E9 scope; possible follow-up.

NQ-209 (Phase 3 E7 NEW, W6+): Time-dependent K=2 simulation to measure $t_{\mathrm{merge}}$ + verify $\tau_{\mathrm{linear}}$ matches predicted $1/|\mu_{\mathrm{antisym}}|$.

NQ-210 (Phase 3 E7 NEW, W7+): K=10 or K=100 simulation to measure $R(t) \sim t^{1/d}$ scaling. SCC numerical verification of LSW analog.

---

## §5. Theoretical Bridge: Modica-Mortola Γ-Convergence

The classical LSW law arises in the limit $\beta \to \infty$ of the Allen-Cahn equation (sharp interface limit). SCC's K-field has $\beta$-dependent dynamics governed by $\mathcal{E}_K$.

**Modica-Mortola Γ-convergence** (canonical T11): in the limit $\xi_0 \to 0$ (super-thin interface), pure $\mathcal{E}_{\mathrm{bd}}$ Γ-converges to perimeter functional. K-formation minimizers become K disjoint phases with sharp interfaces.

In this limit, SCC K-field becomes formally equivalent to **mean-curvature flow** on the interface — and LSW law emerges from interface energetics.

The **σ-framework T-σ-Multi-1** instability rate $|\lambda_{\mathrm{antisym}}| = c_{\mathrm{eff}} \lambda_{\mathrm{rep}}$ provides the **first-order finite-ξ_0 correction** to the sharp-interface limit. The corrections arise from:
1. PN-barrier ($\xi_0$-dependent, per `11_*` §2.1).
2. Coupling Bound Lemma exponentially-small corrections.
3. Mode-mixing factor $c_{\mathrm{eff}}$ (Phase 3 E3 finding).

### 5.1 Γ-convergence + T-σ-Multi-1 = full LSW

Combined statement:
> In SCC K-field architecture at sharp-interface limit ($\xi_0 \to 0$, equivalently $\beta \to \infty$):
> - Modica-Mortola: minimizers are K disjoint phases with sharp interfaces.
> - T-σ-Multi-1: K-phase configurations are saddles (always); merge dynamics → K decreases over time.
> - Coarsening law: $R(t) \sim (\lambda_{\mathrm{rep}} t)^{1/d}$, recovering LSW $t^{1/3}$ in $d=3$.
>
> SCC predicts LSW law as a consequence of T-σ-Multi-1 + Γ-convergence.

**Cat status**: Cat B target. Full Cat A would require:
- Rigorous derivation of $\dot \rho \sim -\rho^2 \lambda_{\mathrm{rep}}$ from K-field gradient flow (not just heuristic).
- Numerical verification at K ≥ 100 (Phase 3 E9 only K=2).
- Connection to Modica-Mortola convergence rate (NQ partial).

---

## §6. Implications

### 6.1 SCC as a self-contained coarsening framework

Standard LSW theory uses external phenomenology (D, σ). SCC derives the analog from canonical primitives ($\alpha, \beta, c, \lambda_{\mathrm{rep}}, $ graph).

This positions SCC as a **first-principles** coarsening framework for graph-based discrete systems.

### 6.2 Multi-formation σ-framework completeness

After Phase 3 E1-E10, the σ-framework now covers:
- Single-formation σ (Commitment 14, T-σ-Lemma-1/2/3, T-σ-Theorem-3/4) — canonical W5 Day 1.
- Multi-formation σ_multi^(A) (`05_*`, `08_*`, `09_*`) — Phase 2 + Phase 3.
- Multi-formation σ_multi^(D) (`06_*`, `10_*`) — Phase 3.
- A vs D complementarity (`12_*`) — Phase 3.
- Goldstone-pair instability T-σ-Multi-1 (`09_*`) — Phase 3.
- Connection to LSW coarsening (this file) — Phase 3.

The framework is **near-complete** for paper §4 exposition. Remaining gaps (NQ-200..NQ-210) are W6+ refinements.

---

## §7. Cross-References

- T-σ-Multi-1 Cat A: `09_goldstone_instability_proved.md`.
- σ_multi^(A) (operational σ): `05_sigma_multi_concrete_T2_K2.md`.
- σ_multi^(D) (topological σ): `10_sigma_multi_D_concrete.md`, `12_D_to_A_reduction.md`.
- PN-barrier formula: `11_PN_unification.md`.
- LSW classical: Lifshitz-Slyozov 1961 *J. Phys. Chem. Solids* 19:35; Wagner 1961 *Z. Elektrochem.* 65:581.
- Modica-Mortola: canonical T11 (Γ-convergence); Modica-Mortola 1977 *Boll. Un. Mat. Ital.* 14:285.
- Mean-curvature flow: Allen-Cahn dynamics in sharp-interface limit.

---

---

## §8. **PHASE 6+7 REFUTATION** (2026-04-28 EOD update)

### §8.1 Phase 6 Q1 + Q2 numerical evidence

After completing Phase 6 elevations (Q1 volume-projected dynamic + Q2 below-spinodal LSW), the LSW connection sketch above is **REFUTED for the current SCC K-field architecture**:

**Q1 finding** (`27_*` Phase 6): even with properly volume-projected joint Hessian eigvec (sums = 0 per formation), perturbation along the unstable eigvec **decays at rate -0.0195** under volume + simplex-constrained gradient flow. Static instability does NOT translate to dynamic merger.

**Q2 finding** (`27_*` Phase 6): K=5, K=10 below-spinodal (c_per=0.05, λ_rep=0.5) on T²_{40} are STABLE for t=80; K=20 simplex-saturates immediately. **No coarsening observed** in any tested regime.

**Phase 7 R1.1, R1.2, R1.3 follow-ups**: investigate which constraint (simplex barrier, box clipping, per-formation volume) stabilizes the dynamics; test alternative architecture (shared volume pool).

### §8.2 What remains valid

- **§2 Linear stage T-σ-Multi-1 rate**: STATIC Hessian eigenvalue analysis remains Cat A (per `09_*`). Joint H has negative eigenvalues, so K=2 is a saddle in the static-Hessian sense.
- **§5 Modica-Mortola Γ-convergence**: connection to perimeter functional remains valid as a theoretical limit. Doesn't depend on dynamics.

### §8.3 What is REFUTED

- **§3.2 Mass-transfer rate (3.1)** $\dot m_j \sim \Phi(...)$: empirically NOT observed under standard K-field gradient flow. Mass redistribution between formations is BLOCKED by per-formation volume constraint.
- **§3.3 LSW scaling argument** R(t) ~ (λ_rep t)^(1/d): NOT recovered numerically. SCC K-field gradient flow doesn't realize this scaling.
- **§3.4 Predicted exponent table** (R(t) ~ t^α for d-dim): all entries are theoretical; none confirmed empirically.
- **§4.1 τ_linear measurement matching prediction**: Phase 5 P1.1 + Phase 6 Q1 show τ_linear is OPPOSITE-SIGN of prediction (decay rather than growth) under standard dynamics.

### §8.4 Conditional re-interpretation

The LSW correspondence may be RECOVERED under one of:
1. **Alternative K-field formulation** with shared volume pool (NQ-223, R1.3). Testing in progress.
2. **Different optimizer**: simulated annealing, stochastic gradient with noise, or barrier-crossing methods (NQ-224).
3. **Relaxed simplex barrier**: λ_bar = 0 (NQ-221, R1.1) testing in progress.
4. **No box constraint clipping**: u allowed outside [0,1] (NQ-222, R1.2) testing in progress.

If any of these recovers LSW dynamics, this file's framework can be re-instated as conditional theorem.

### §8.5 Cat status revision

**Original §6 claim**: "SCC K-field coarsening law R(t) ~ (λ_rep t)^(1/d), Cat B sketched."

**Revised claim (Phase 6+7)**: "SCC K-field coarsening law is **conditional Cat C** (refuted under current K-field architecture; unverified under alternatives). Static T-σ-Multi-1 saddle-point structure remains Cat A."

### §8.6 Implications for paper

- §4.5 LSW section needs REWRITE (`26_*` Q4 paper §4.5 deferred → Phase 7 R1.5 will rewrite as conditional).
- σ-framework's PRIMARY value remains static Hessian analysis (`09_*` Cat A) and topological orbit-type label (`10_*`, `12_*`, `25_*` Cat A).
- **Dynamic predictions must be carefully separated from static structural results in any future presentation**.

---

**End of 13_LSW_connection.md.**
**Status (REVISED Phase 6+7)**: Original SCC-LSW connection sketch was Phase 3 Cat B; **REFUTED at current K-field architecture per Phase 6 Q1+Q2**. Static T-σ-Multi-1 Cat A retained. LSW correspondence is conditional pending alternative-formulation tests (Phase 7 R1.1-R1.3 in progress).
