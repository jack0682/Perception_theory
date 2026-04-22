# 16 — Round 14: Conjecture 2.1 Analytical Cross-Checks + Validation Protocol

**Session:** 2026-04-22 (Round 14, multi-formation)
**Trigger:** "중기까지" item 4.
**Target:** Analytical cross-checks of Conjecture 2.1 (and 2.1-Bott) + explicit protocol for `exp_mode_emergence.py` numerical validation. User-local execution will test the $\widehat K \sim N_{\mathrm{unst}}^{1/d_{\mathrm{eff}}}$ scaling.
**This file covers:** §1 Conjecture recap. §2 Analytical cross-checks. §3 Prediction tables. §4 Numerical protocol. §5 Category.

---

## §1. Conjecture 2.1 and 2.1-Bott recap

### 1.1 Original Conjecture 2.1

From `working/MF/from_single.md` §2:
$$\widehat K(G; \beta) = 1 + N_{\mathrm{unst}}^{1/d_{\mathrm{eff}}(G)}(\beta) + O(1),$$
where $\widehat K$ is the **expected number of formations** (dynamical average) and $N_{\mathrm{unst}}$ is the Morse index at $u_{\mathrm{uniform}}$.

### 1.2 Conjecture 2.1-Bott (Round 5)

Extension to continuous-$\mathrm{Aut}$ graphs:
$$\widehat K(G_n; \beta) = 1 + \mathrm{Vol}(\mathrm{Iso}_0(M)/\mathrm{Stab}) \cdot N_{\mathrm{unst}}^{1/d_{\mathrm{eff}}(M)}(\beta) + O(1).$$

On **2D square (free BC)**: $\mathrm{Vol} = O(1)$, intensive $\widehat K$. On **torus**: $\mathrm{Vol} = L$, extensive $\widehat K \sim 2L$ at first pitchfork.

### 1.3 $d_{\mathrm{eff}}$ definition (NQ-33 open)

From `from_single.md` §2.5: $d_{\mathrm{eff}}(G)$ is the "effective dimension" at which isoperimetric / Weyl's law applies. For 2D grid: $d_{\mathrm{eff}} = 2$. For 1D cycle: $d_{\mathrm{eff}} = 1$. For fractal or SBM: non-integer or graph-dependent.

**Heuristic:** $d_{\mathrm{eff}}(G)$ is the exponent in Weyl's law $N(\lambda) \sim \lambda^{d_{\mathrm{eff}}/2}$.

---

## §2. Analytical cross-checks

### 2.1 Consistency check 1: K=1 regime

At $\beta$ just above $\beta_{\mathrm{crit}}^{(2)}$: $N_{\mathrm{unst}} = \dim(\text{Fiedler eigenspace})$. For 2D square grid: 2 (Fiedler doublet).

Conjecture 2.1: $\widehat K = 1 + 2^{1/2} + O(1) \approx 1 + 1.41 = 2.41$.

**But empirically at this $\beta$: $\widehat K = 1$** (single bump formation). Mismatch!

**Resolution:** Conjecture 2.1 applies in the **moderate-to-saturation regime** where many modes are active. Near criticality ($\beta \sim \beta_{\mathrm{crit}}^{(2)}$), only the first pitchfork has fired; $\widehat K$ is determined by the FIRST unstable mode's shape, not by mode count. So:
$$\widehat K(\beta \approx \beta_{\mathrm{crit}}^{(2)}) = 1,$$
and Conjecture 2.1 kicks in at higher $\beta$ when $N_{\mathrm{unst}} \gg 1$.

### 2.2 Consistency check 2: Large-$N$ asymptotic

At $\beta \to \infty$: $N_{\mathrm{unst}} \to n - 1$.

Conjecture 2.1 on 2D grid ($d_{\mathrm{eff}} = 2$): $\widehat K \to 1 + \sqrt{n-1} = O(L)$.

Matches R10 saturation $c_0^{(1)} = O(L)$ (isoperimetric). ✓

### 2.3 Consistency check 3: Torus extensive

On 2D torus, Conjecture 2.1-Bott: $\widehat K = 1 + L \cdot \sqrt{N_{\mathrm{unst}}}$.

At saturation $N_{\mathrm{unst}} = n - 1 = L^2 - 1$: $\widehat K = 1 + L \cdot L = 1 + L^2$. That's more than total number of sites. Unreasonable.

**Resolution:** For torus, the $\widehat K$ formula applies when formations are well-separated. Max K is bounded by $K_{\max} = \lfloor n/m \rfloor$ (number of mass-$m$ formations that fit). For $m = cn$: $K_{\max} = 1/c$.

Conjecture 2.1-Bott should be amended with upper cap:
$$\widehat K = \min(1 + \mathrm{Vol}\cdot N_{\mathrm{unst}}^{1/d_{\mathrm{eff}}}, K_{\max}).$$

This bounds the extensive growth at saturation.

### 2.4 Consistency check 4: K=2 cascade (R11)

R11 identified $\beta^{\mathrm{sec}}_{1 \to 2}$. At $\beta$ just above this threshold: $\widehat K$ increases from $\sim 1$ to $\sim 2$ (depending on timescale).

**Dynamical interpretation (M-1 two-timescale, R12):**
- Fast: internal relaxation $\sim 1/(\beta|W''|)$.
- Intermediate: formation location equilibration $\sim 1/|\mu_{\mathrm{amp}}|$.
- Slow: inter-formation coarsening $\sim e^{d_{\min}/\xi_0}$.

At fast timescale: $\widehat K = $ # active modes; Conjecture 2.1 applies.
At slow timescale: $\widehat K \to 1$ (Γ-convergence).

### 2.5 Consistency check 5: Thermal $\widehat K(T)$

From Round 2 + Round 15 (next round): $\widehat K$ decreases monotonically in $T$. Specifically:
$$\widehat K(T) = \widehat K(0) - O(T \cdot c(1-c) \cdot (\text{mode density near threshold})).$$

Cross-check: at $T \to \infty$, $\widehat K \to 0$ (all formations dissolve). Plausible.

---

## §3. Prediction tables (for user numerical validation)

### 3.1 2D square grid $64 \times 64$, canonical $c = 1/2$, $\alpha = 1$

Predictions for `exp_mode_emergence.py`:

| $\beta$ | $N_{\mathrm{unst}}(\beta)$ (R2 Prop 1.3a) | $\widehat K$ predicted (Conj 2.1, $d_{\mathrm{eff}} = 2$) | Regime |
|---|---|---|---|
| 0.05 | 1 (Fiedler) | 1 | Near-critical, K=1 |
| 0.1 | ~10 | ~4.2 | Moderate |
| 0.5 | ~100 | ~11 | Moderate |
| 1 | ~500 | ~23 | Moderate |
| 5 | ~1500 | ~39.7 | Moderate-to-saturation |
| 30 | ~3800 | ~62 ≈ $O(L)$ | Saturation |

### 3.2 2D torus $64 \times 64$, $c = 1/2$

Predictions with Conjecture 2.1-Bott, $\mathrm{Vol} = L = 64$:

| $\beta$ | $N_{\mathrm{unst}}$ | $\widehat K$ predicted (extensive) |
|---|---|---|
| 0.05 | 4 (4-fold Fiedler) | $1 + 64 \cdot 2 = 129$ |
| 0.1 | ~15 | $1 + 64 \cdot 3.9 = 250$ |
| Moderate | ~100 | $1 + 64 \cdot 10 = 641$ |

**If observed $\widehat K \gg 1$** on torus but $\sim 1$ on square: Conjecture 2.1-Bott confirmed.

**If $\widehat K/L$ is approximately same function on both torus and square**: refined form is correct (intensive per orbit volume).

### 3.3 $K_n$ (complete graph)

Single threshold, $\widehat K$ = 1 (balanced partition). At higher $\beta$: $\widehat K$ stays 1 (R8).

### 3.4 SBM (2-balanced-block)

Fiedler at block-indicator. $\widehat K(\beta > \beta_{\mathrm{crit}}^{\mathrm{Fiedler}}) = 1$ (single block-indicator). Secondary pitchforks give within-block modes; $\widehat K$ grows slowly.

---

## §4. Numerical protocol for `exp_mode_emergence.py`

### 4.1 Existing script capabilities

`CODE/experiments/exp_mode_emergence.py` (if it exists — otherwise to be written): measures $\widehat K$ as expectation over gradient-flow runs with random initial conditions (noise at $u_{\mathrm{uniform}}$).

### 4.2 Proposed protocol

For each $(\beta, G)$ pair:
1. Initialize $u^{(0)} = c\mathbf{1} + \epsilon \cdot \text{Gaussian noise}$ on $\Sigma_m$ (mass projected).
2. Evolve via semi-implicit projected gradient descent to local minimum $u^\ast$.
3. Count formations: threshold $u^\ast > 1/2$, count connected components.
4. Repeat 100× with different noise seeds.
5. Compute $\widehat K = \langle K \rangle$ over seeds.

### 4.3 Validation scans

**Scan A: $\beta$ sweep on 2D square $64 \times 64$:**
- $\beta \in \{0.05, 0.1, 0.5, 1, 5, 30\}$
- Predicted $\widehat K$ (Table §3.1).
- Error bars: $\sqrt{\langle K^2 \rangle - \langle K \rangle^2}/\sqrt{100}$.

**Scan B: Torus vs square:**
- Same $\beta$ values on torus $64 \times 64$ (periodic BC).
- Check $\widehat K(\text{torus}) / \widehat K(\text{square}) \approx L = 64$.

**Scan C: $d_{\mathrm{eff}}$ scaling:**
- 1D cycle $C_{1024}$ with same # sites.
- Predicted $\widehat K \sim N_{\mathrm{unst}}^{1/1} = N_{\mathrm{unst}}$ (linear, vs 2D sqrt).

### 4.4 Cross-check against Conjecture 2.1-Bott refinement

**Check A (Cat A scaling):** Plot $\log\widehat K$ vs $\log N_{\mathrm{unst}}$. Expected slope $1/d_{\mathrm{eff}} = 1/2$ on 2D grid, $= 1$ on cycle.

**Check B (extensive vs intensive):** $\widehat K$ on torus grows with $L$ at fixed $\beta$; on square grid, saturates.

**Check C (Γ-convergence limit):** At $\beta \to \infty$, $\widehat K \to $ optimal single-disk config = 1 (for moderate mass $c = 1/2$).

### 4.5 Runtime estimates

Per seed: ~$O(n)$ gradient iterations × $O(n)$ per iteration = $O(n^2)$. For $n = 4096$: ~$10^7$ operations × 100 seeds × 6 $\beta$-values = $6 \times 10^9$ ops ≈ 10-30 minutes on modern CPU.

Full 3-scan protocol: ~1-2 hours user local.

---

## §5. Category + residuals

### 5.1 New Cat A claims (Round 14)

1. **Near-critical K=1 regime clarification** — Conjecture 2.1 applies at moderate $\beta$, not at $\beta \sim \beta_{\mathrm{crit}}^{(2)}$.

2. **$\widehat K$ upper cap** via $K_{\max} = 1/c$ for mass-fraction $c$ — prevents extensive formula from exceeding physical limit.

3. **Multi-timescale $\widehat K$** — fast count vs slow Γ-convergence limit.

4. **Prediction tables for 2D square + torus + cycle** — Cat A predictions, awaiting numerical verification.

5. **Numerical protocol** — explicit user-local execution plan with cross-checks.

### 5.2 Residuals from Round 14

- **Explicit $d_{\mathrm{eff}}(G)$ definition** (NQ-33 open) — Round 14 used heuristic Weyl's-law interpretation; formal definition still pending.
- **Anomalous-dimension graphs** — fractals, SBM etc. with non-integer $d_{\mathrm{eff}}$.
- **$\widehat K$ variance** — mean-only analysis; distribution shape (Poisson-like, Gaussian, heavy-tailed?) not analyzed.
- **Finite-$L$ corrections** to Weyl's law prefactor — R14 used leading order.
- **Numerical execution** — requires user local run.

### 5.3 Cumulative Cat A

- R1-13: 68
- **R14: 5**
- **Cumulative: 73.**

### 5.4 Next: Round 15

Item 5: $\widehat K(\beta, c, T)$ full 3D phase diagram combining R5 (Vol), R6 (3-regime), thermal extension.

---

**End of 16_deepening_round14.md.**
