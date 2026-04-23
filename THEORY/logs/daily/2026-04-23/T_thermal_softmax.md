# T_thermal_softmax.md — Thermal / Stochastic Extension Scoping

**Session:** 2026-04-23 (G5 deliverable; intended promotion target: `working/T/thermal_softmax.md`)
**Target (from plan.md §2 G5):** Finite-T dynamics + Layer 1 softmax at selector transitions. 2+ Cat C hypotheses.
**This file covers:** (a) Langevin dynamics framework; (b) Gibbs invariant measure; (c) basin occupation softmax (post-V7 P1 refutation); (d) Layer 1 selector smoothing; (e) Kramers escape between basins.
**Depends on reading:** `01_exploration.md` §5.2 (E1-E4 approach candidates), `T_time_evolution.md` §4 (H-T3 Kramers nucleation), `canonical.md` §13 T14 (Łojasiewicz with $b_D = 0$), `logs/daily/2026-04-22/99_summary.md` §18.2-18.3 (F1-SSU evolution, V7 P1 softmax refutation).

---

## §1. Scope

### 1.1 What is added relative to zero-T

Current canonical (v1.2): **zero-T deterministic gradient flow** on $\Sigma_m$. T14 Cat A guarantees convergence via Łojasiewicz with $b_D = 0$ (CN13).

This session's scoping: **finite-T Langevin noise** and its consequences at Layer 1 (protocol selector smoothing) and Layer 2 (barrier crossing rates).

### 1.2 Critical constraints

Per Hard Constraint #9 (prompt §8): **zero-T metastability claims must be flagged as requiring P-F (thermal framework) for full rigor**. This file explicitly develops P-F scoping.

V7 P1 empirical refutation of basic softmax (logs 2026-04-22 R22 §18.2): restricts form of thermal framework. Cannot assume naive Boltzmann $P(\mathcal{B}_k) \propto e^{-E_k/T}$.

---

## §2. Hypothesis H-Th1: Langevin dynamics framework

### 2.1 Statement

> **Hypothesis H-Th1 (SCC Langevin)**. Finite-temperature SCC dynamics is:
> $$du = -\Pi_{\Sigma_m}\nabla\mathcal{E}(u)\,dt + \sqrt{2T} \Pi_{\Sigma_m}\,dW_t,$$
> where $W_t$ is site-wise independent Brownian motion, and $\Pi_{\Sigma_m}$ projects onto tangent $T_u\Sigma_m = \{v : \sum v_i = 0\}$.

### 2.2 Invariant measure

Under H-Th1, the invariant measure on $\Sigma_m$ is:
$$\mu_T(u) = \frac{1}{Z(T)} \exp(-\mathcal{E}(u)/T) \cdot \delta(\sum_i u_i - m).$$

This is **Gibbs with volume constraint** — standard for SDE on constraint manifold.

### 2.3 Category

- **H-Th1 statement**: Cat B structural (standard SDE construction).
- **Gibbs invariant measure**: Cat B (requires $\mathcal{E}$ smoothness; $b_D = 0$ from CN13 preserves analyticity).
- **Positivity constraint $u \in [0,1]^n$**: Open issue — Langevin noise can push $u_i$ outside $[0, 1]$. Requires **reflected Brownian motion** or truncation. **NQ-67 (new)**: boundary treatment of Langevin on $[0,1]^n \cap \Sigma_m$.

### 2.4 Relation to T14 (zero-T)

H-Th1 at $T \to 0$ limit:
$$du = -\Pi_{\Sigma_m}\nabla\mathcal{E}(u)\,dt,$$
which is T14 gradient flow. Consistent.

### 2.5 Relation to canonical §11 CN6 (K kinetically determined)

Canonical CN6: K is kinetic, not thermodynamic. Under H-Th1 at slow annealing (T → 0 slowly), system reaches Gibbs equilibrium → lowest-$E$ basin selected = K=1 (T-Merge (b)). This is **thermodynamic** K selection, contradicting CN6.

**Resolution**: CN6 is about **actual physical timescales** on which K is observed. Annealing to Gibbs equilibrium requires **asymptotically slow** T reduction — not physical in finite-time observation. H-Th1 with **finite T > 0 and finite time** preserves kinetic K behavior.

---

## §3. Hypothesis H-Th2: Basin occupation (modified softmax, post-V7 P1)

### 3.1 Preceding refutation

**V7 P1 empirical (logs 2026-04-22 R22 §18.2)**: P(K=1) ≈ 0.02 constant across β=8.5-9.5 (50 seeds). Not sigmoidal. Basic Boltzmann $P(\mathcal{B}_k) \propto e^{-E_k^*/T}$ **refuted**.

**V7 P3**: β=9 × 200 seeds → Gaussian around K=13, not bimodal.

### 3.2 Refined statement

> **Hypothesis H-Th2 (modified basin occupation)**. Under H-Th1 Langevin at finite T, the **marginal distribution over K-sectors** is:
> $$P_T(\widehat K = k) = \sum_{u^* \in \mathcal{M}_k} w(u^*) \exp(-E(u^*)/T) \cdot V_k(T),$$
> where:
> - $\mathcal{M}_k$ is the moduli of $k$-formation minimizers,
> - $w(u^*)$ is a basin-volume weight (log of basin size in $\Sigma_m$),
> - $V_k(T)$ is a $T$-dependent entropy correction.
>
> At short-time (non-equilibrium), this reduces to the protocol's basin-selection distribution (Class N of function taxonomy).

### 3.3 Key departure from basic softmax

Basic: $P \propto e^{-E/T}$ sums over **individual minimizer energies**.

Modified: sum over **moduli points** with **basin-volume weight**. A K-sector with many minimizers of similar energy + large basin has higher probability than K-sector with single deep minimum.

### 3.4 Why V7 P1 refuted basic

For 1D cycle c=0.7 at β=9: $E(\mathcal{B}_1) < E(\mathcal{B}_K)$ for $K \geq 2$ (isoperimetric), so basic softmax predicts P(K=1) → 1 as $T \to 0$. But observed P(K=1) ≈ 0.02 independent of anything.

**Resolution via basin volume**: $V_1(T) \ll V_K(T)$ for K ≈ 13 in the protocol's effective initial distribution. Even though $\mathcal{B}_1$ is deeper, its volume is tiny, so **total probability** is dominated by the large-volume K-sector.

### 3.5 Category

- **H-Th2 statement**: Cat C (requires P-F + basin volume theory).
- **Reconciliation with V7 P1**: Cat C (plausible mechanism, not proved).
- **Gaussian marginal (V7 P3)**: Class N functional form; open parameters.

### 3.6 Failure modes

- Basin volume $V_k(T)$ may not be well-defined (if basin boundaries are fractal or stratified).
- Protocol's short-time distribution ≠ Gibbs equilibrium. H-Th2 conflates two distributions.

---

## §4. Hypothesis H-Th3: Layer 1 selector sigmoid-smoothing

### 4.1 Statement

> **Hypothesis H-Th3 (Selector smoothing)**. At $T = 0$, Layer 1 protocol selector $s_\pi(\beta)$ is a **Heaviside step function** (Class H). At $T > 0$, it becomes **sigmoid-smeared** (Class L):
> $$s_\pi(\beta; T) = \sigma(\kappa(T)(\beta - \beta_\pi^*))$$
> with sharpness $\kappa(T) \propto 1/T^\gamma$ for some exponent $\gamma > 0$.

### 4.2 Mechanism

Near basin boundary $\beta = \beta_\pi^*$, two nearby basins $\mathcal{B}_K$ and $\mathcal{B}_{K+1}$ exist. At T=0, protocol deterministically lands in one. At T>0, thermal fluctuation gives finite probability for either.

For Gaussian barrier $\Delta\mathcal{F}(\beta - \beta_\pi^*) \sim (\beta - \beta_\pi^*)^2$ (smooth approach), Kramers rate gives:
$$P(\mathcal{B}_K | \beta, T) \approx \sigma((\beta - \beta_\pi^*) \cdot \Delta / T)$$

where $\Delta$ is barrier height scale. Sharpness $\kappa(T) = \Delta/T$, so $\gamma = 1$ (linear in 1/T).

### 4.3 Empirical context

R20 β=9 bistable region observation: std/mean of $\widehat K$ ≈ 0.4 at β=9 (1D cycle c=0.7) suggests non-zero effective T from initial-condition noise.

Identifying T_eff from σ_init:
$$T_{\mathrm{eff}} \sim \sigma_{\mathrm{init}}^2 \cdot (\text{scaling factor}).$$

H-Th3 with $T_{\mathrm{eff}}$ reproduces R20 bistable width qualitatively.

### 4.4 Category

- **H-Th3 sigmoid smoothing**: Cat B sketched (Kramers + barrier structure).
- **Exponent $\gamma = 1$**: Cat C (dependent on barrier form; $\gamma = 1/2$ also possible for inverse-cusp).
- **$T_{\mathrm{eff}}$ from initial noise**: Cat C (plausible but not rigorously derived).

### 4.5 Critical clarification (Hard Constraint #9)

H-Th3 uses term "metastable" in that $\mathcal{B}_K, \mathcal{B}_{K+1}$ are metastable local minima with finite escape rates at T>0. This requires **P-F** (thermal framework). At T=0, escape rate is zero, and "metastable" is only **static** Hessian positive-definite.

---

## §5. Hypothesis H-Th4: Kramers escape between basins

### 5.1 Statement

> **Hypothesis H-Th4 (Inter-basin Kramers rate)**. Escape time from $\mathcal{B}_K$ to $\mathcal{B}_{K'}$ at finite T:
> $$\tau_{K \to K'}(T, \beta) = \tau_0 \cdot \exp(\Delta\mathcal{F}_{K \to K'}(\beta)/T),$$
> where:
> - $\tau_0$ = attempt frequency ($\tau_0 \sim 1/\lambda_{\max}$ spectral scale).
> - $\Delta\mathcal{F}_{K \to K'}$ = barrier height on minimum-energy path between basins.

### 5.2 Two types of transitions

- **$K \to K+1$ (nucleation of new formation)**: Small formation spontaneously nucleates. Barrier is critical-nucleus energy.
- **$K \to K-1$ (merger)**: Two formations merge. Barrier is merger saddle energy.

Different scales: typically $\Delta\mathcal{F}_{\mathrm{nucleation}}$ large (far from K=1 basin), $\Delta\mathcal{F}_{\mathrm{merger}}$ depends on separation.

### 5.3 Relation to canonical barrier exponent

Canonical §13 Cat B: "Barrier exponent $\gamma_{\mathrm{eff}} \approx 0.89$". $\Delta\mathcal{F}_{\mathrm{merger}} \propto \beta^{0.89}$ empirically.

Under H-Th4, merger timescale:
$$\tau_{K \to K-1} \propto \exp(A \beta^{0.89}/T).$$

At canonical $\beta = 30, T = 1$: $\exp(A \cdot 30^{0.89}) = \exp(A \cdot 17.3)$. For $A \sim 1$: $\tau \sim e^{17} \sim 10^7$. Large timescale separation — consistent with M-1 dissolution ("K=1 reached only in astronomically long time at zero $\tilde T$").

### 5.4 Category

- **H-Th4 Kramers form**: Cat C (requires P-F).
- **Merger barrier $\propto \beta^{0.89}$**: Cat B canonical (empirical fit from exp38).
- **Nucleation barrier form**: Open.

### 5.5 Failure modes

- At $T = 0$, $\tau = \infty$ formally; not observable. Zero-T dynamics is freeze.
- At very high T, $\tau \to \tau_0$ (system thermalizes rapidly). Not in physical regime.
- Barrier exponent 0.89 is branch/protocol-specific (canonical erratum 2026-04-10).

---

## §6. P-F (thermal framework) status

### 6.1 What P-F would provide

- Rigorous Langevin dynamics on constraint manifold $\Sigma_m$.
- Boundary treatment ($u \in [0,1]^n$): reflected Brownian motion or penalization.
- Gibbs invariant measure proof.
- Ergodicity / mixing time bounds.
- Freidlin-Wentzell small-noise large deviation theory (for Kramers justification).

### 6.2 What is currently missing

- Canonical has **no P-F section**. Section 11.2 "dynamic update laws" is open choice.
- No formal SDE for SCC defined.

### 6.3 Recommendation for Stage 2/3

- **P-F as new section in canonical v2.0**: define H-Th1 as canonical axiom for thermal extension.
- **Boundary treatment specification**: reflected Brownian motion on $[0,1]^n \cap \Sigma_m$.
- **Open design choice** (11.2) → thermal framework selection.

---

## §7. Layer 1 softmax revised (after V7 P1)

Per G2 function taxonomy §5.3: basic softmax (Class S) is **refuted**. Replacement:

### 7.1 Class N (spectral Gaussian) — tentative

$P(\widehat K | \beta, T, \pi) \approx \mathcal{N}(\widehat K; \bar K(\beta, T, G, \pi), \sigma_K^2(\beta, T, G, \pi))$.

Variance $\sigma_K^2$ depends on spectral structure of initial perturbation and basin geometry.

### 7.2 Relationship

- Class N at $T \to 0$: variance collapses, mean peaks at protocol's deterministic K. Reduces to deterministic step (Class H).
- Class N at $T \to \infty$: variance grows, distribution uniform. Approaches "everything equally likely".

### 7.3 Protocol's role

Protocol $\pi$ changes **both** $\bar K$ and $\sigma_K^2$:
- Fiedler-init: narrow $\sigma_K^2$ (concentrated near spectral mode).
- Random-init: broader $\sigma_K^2$.

---

## §8. Connection to G4 time evolution

H-T3 (Kramers nucleation) is the $\mathcal{B}_0 \to \mathcal{B}_1$ case of H-Th4.
H-T2 (LSW coarsening) is long-time evolution driven by repeated $\mathcal{B}_K \to \mathcal{B}_{K-1}$ events.

At finite T, whole G4 + G5 scoping interconnect:
- Gradient flow (R-GF) is T=0 limit of Langevin (H-Th1).
- Sharp interface MCF (R-SI) is $\beta \to \infty$ limit, orthogonal to T.
- LSW coarsening (R-LSW) requires T > 0 for barrier crossing.
- Nucleation rates (H-T3) = specific case of Kramers (H-Th4).

---

## §9. Hypothesis summary

| ID | Hypothesis | Cat | Dep |
|---|---|---|---|
| H-Th1 | Langevin SDE on $\Sigma_m$ (P-F framework) | Cat B sketched | boundary treatment NQ-67 |
| H-Th2 | Basin-volume-weighted occupation (not basic softmax) | Cat C | P-F + basin volume theory |
| H-Th3 | Layer 1 selector sigmoid-smoothing at T>0 | Cat B sketched | Kramers + barrier shape |
| H-Th4 | Inter-basin Kramers escape rate | Cat C | P-F |

---

## §10. Open questions

### 10.1 NQ-67 — Langevin boundary treatment on $[0,1]^n \cap \Sigma_m$

Reflected BM? Penalization? Both preserve Gibbs. Choice affects **short-time statistics near boundary**.

### 10.2 NQ-68 — Basin volume $V_K(T)$ for SCC

Computationally: measure of $\mathcal{B}_K$ in $\Sigma_m$. Analytically: related to Gaussian width around each minimizer.

### 10.3 NQ-69 — T_eff from protocol noise

Quantitative relation $T_{\mathrm{eff}}(\sigma_{\mathrm{init}}, \beta, G, \pi)$?

### 10.4 NQ-70 — Kramers prefactor $\tau_0$ for SCC

Standard Kramers gives $\tau_0 \sim 1/\sqrt{-\lambda_{\mathrm{saddle}}}$. For SCC with closure contribution, what's the saddle's negative eigenvalue?

### 10.5 NQ-71 — Class N parameter laws

Gaussian $\bar K, \sigma_K^2$의 $(β, c, T, G, π)$ 의존성. V7 P3 empirical fit point (β=9, c=0.7, 1D cycle, 200 seeds → $\bar K ≈ 13, \sigma_K \approx 1.5$) is **one data point**; full scaling law open.

---

## §11. Canonical merge targets (Stage 6 pending)

- **New Section 11.3 (or §12 extension): P-F Thermal Framework**. H-Th1 Langevin SDE + Gibbs invariant measure.
- **Modification of CN6**: explicit finite-time vs slow-annealing distinction.
- **New Class N**: formalize as empirically-motivated Layer 1 stochastic selector distribution.
- **Erratum on V7 P1**: softmax refutation documented.

---

## §12. File status

- **Primary deliverable**: 4 hypotheses (H-Th1, H-Th2, H-Th3, H-Th4) + P-F framework scoping.
- **V7 P1 post-refutation treatment**: Class N replacement proposed (§7).
- **Hard Constraint #9 compliance**: "metastability" usage flagged with P-F dependence.
- **Intended promotion**: `working/T/thermal_softmax.md` (신규).

**End of T_thermal_softmax.md.**
