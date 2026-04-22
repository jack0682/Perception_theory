# 17 — Round 15: $\widehat K(\beta, c, T)$ Full Phase Diagram

**Session:** 2026-04-22 (Round 15, multi-formation synthesis)
**Trigger:** "중기까지" item 5.
**Target:** Combine R5 (Conj 2.1-Bott, Aut volume) + R6 (3-regime $c$-dependence) + thermal extension → 3D phase diagram of $\widehat K$ in $(\beta, c, T)$ space. Explicit regime boundaries.
**This file covers:** §1 Ingredients. §2 3D phase structure. §3 Specific graph classes. §4 Regime boundaries. §5 Dimensional reduction. §6 Category + residuals.

---

## §1. Ingredients from previous rounds

### 1.1 $\beta$-axis (R10)

$\widehat K$ monotonically increases with $\beta$ until saturation:
- $\beta < \beta_{\mathrm{crit}}^{(2)}$: $\widehat K = 0$ (no formation).
- $\beta^{(2)}_{\mathrm{crit}} < \beta < \beta_{\mathrm{crossover}}$: moderate, $\widehat K$ grows per Conj 2.1.
- $\beta > \beta_{\mathrm{crossover}}$: saturation, $\widehat K \to K_{\min-\text{perim}}$ (typically 1 by T11).

### 1.2 $c$-axis (R6)

$N^{\mathrm{sep}}_{\mathrm{unst}}(c)$ has 3 regimes:
- Regime I ($c < c_{\mathrm{bif}}^-$): +bipartite modes → more unstable → higher $\widehat K$.
- Regime II (canonical, central): baseline.
- Regime III ($c > c_{\mathrm{bif}}^+$): -smooth modes → fewer unstable → lower $\widehat K$.

Effect on $\widehat K$ via $N_{\mathrm{unst}}^{\mathrm{full}}(c) \approx N^{\mathrm{bd}}(\beta, c) + N^{\mathrm{sep}}(c)$.

### 1.3 $T$-axis (R2 thermal_extension)

$T > 0$: all mode eigenvalues shifted by $+T/[c(1-c)]$. Modes at $\mu_k < T/[c(1-c)]$ become stable. Effective $N_{\mathrm{unst}}(T) < N_{\mathrm{unst}}(0)$.

**Thermal critical $\beta$-shift:** $\beta^{\mathrm{thermal}}_{\mathrm{crit}}(c, T) = \beta_{\mathrm{crit}}^{(2)}(c) + T\lambda_2 \cdot c(1-c)/[|W''(c)| \cdot c(1-c)] = \beta_{\mathrm{crit}}^{(2)}(c)(1 + T/[|W''(c)|c(1-c)])$.

Higher $T$ → higher critical $\beta$ → more "stable" uniform state.

### 1.4 Graph-topology axis ($G$)

Conj 2.1-Bott (R5): prefactor $\mathrm{Vol}(\mathrm{Iso}_0(M)/\mathrm{Stab})$.
- 2D square: $O(1)$.
- Torus: $O(L)$.
- Cycle: $O(1)$ (after discrete-Aut lock-in).
- $K_n$: $O(1)$ (single threshold structure).

---

## §2. 3D phase structure in $(\beta, c, T)$ at fixed $G$

### 2.1 Master formula (conjectural)

Combining ingredients:
$$\widehat K(\beta, c, T; G) = 1 + \mathrm{Vol}(\mathrm{Iso}_0(M)) \cdot N_{\mathrm{unst}}^{\mathrm{full}}(\beta, c, T)^{1/d_{\mathrm{eff}}(G)} + O(1),$$
where $N_{\mathrm{unst}}^{\mathrm{full}}(\beta, c, T)$ is the full-energy Morse index adjusted for all three parameters.

### 2.2 Near-critical regime

At $\beta$ just above $\beta^{\mathrm{thermal}}_{\mathrm{crit}}(c, T)$: $N_{\mathrm{unst}} = 1$ (Fiedler dominant), $\widehat K \approx 1$.

### 2.3 Moderate regime

$\widehat K$ grows as power of $(N_{\mathrm{unst}})^{1/d_{\mathrm{eff}}}$; specific formula graph- and regime-dependent.

### 2.4 Saturation regime

$\widehat K \to K_{\min-\text{perim}}(c, G) = $ isoperimetric optimum. For mass-fraction $c$ on 2D grid: single disk, $K = 1$.

At $c$ near $1/2$: single disk has max perimeter; at $c$ near $0$ or $1$: small disk, $K \geq 2$ possible (but total mass small).

### 2.5 Thermal dissolution regime

At $T$ above some $T_{\mathrm{dis}}(c, G)$: all formations dissolve, $\widehat K \to 0$. Thermal critical $T$: when $\beta^{\mathrm{thermal}}_{\mathrm{crit}} \to \infty$ at given $\beta$, i.e., $T_{\mathrm{dis}} \sim \beta \cdot c(1-c)/\lambda_2$.

### 2.6 Phase diagram sketch

In $(\beta, c, T)$ space:
- **Uniform phase:** $\beta < \beta^{\mathrm{thermal}}_{\mathrm{crit}}(c, T)$.
- **Single-formation phase:** $\beta^{\mathrm{thermal}}_{\mathrm{crit}} < \beta < \beta^{\mathrm{sec}}_{1 \to 2}(c, T)$.
- **K ≥ 2 metastable phase:** $\beta > \beta^{\mathrm{sec}}_{1 \to 2}$; ergodic $\widehat K$ grows with $\beta$.
- **Saturation phase:** $\beta > \beta_{\mathrm{crossover}}$; $\widehat K$ stabilizes.

Each phase boundary is a 2D surface in $(\beta, c, T)$.

---

## §3. Specific graph classes

### 3.1 2D square grid (free BC, $D_4$)

$\mathrm{Vol} = O(1)$, $d_{\mathrm{eff}} = 2$. At canonical $c = 1/2$ (Regime II):
$$\widehat K(\beta, 1/2, 0; \text{2D square}) = \begin{cases} 1 & \beta < \beta_{\mathrm{crit}}^{(2)} \\ 1 + \sqrt{N_{\mathrm{unst}}(\beta)} & \text{moderate} \\ O(L) = O(\sqrt n) & \text{saturation} \end{cases}$$

At Regime I ($c = 0.3$): $N_{\mathrm{unst}}^{\mathrm{full}}$ increased by ~10% (R6); $\widehat K$ increases by ~5% (square root scaling).

At Regime III ($c = 0.7$): $N_{\mathrm{unst}}^{\mathrm{full}}$ decreased by ~50%; $\widehat K$ decreases by ~29%.

Thermal: $\widehat K(T)$ decreases monotonically.

### 3.2 2D torus $T^2$

$\mathrm{Vol} = L$, $d_{\mathrm{eff}} = 2$:
$$\widehat K(\beta, c, T; T^2) = 1 + L \cdot \sqrt{N_{\mathrm{unst}}(\beta, c, T)} + O(1) \quad (\text{capped at }K_{\max}).$$

Extensive in $L$ at moderate $\beta$. Intensive $\widehat K/L$ is a universal function of $(\beta, c, T)$.

### 3.3 1D cycle $C_n$

$\mathrm{Vol} = O(1)$ (after $D_n$-quotient), $d_{\mathrm{eff}} = 1$:
$$\widehat K(\beta, c, T; C_n) = 1 + N_{\mathrm{unst}}(\beta, c, T) + O(1).$$

Linear in $N_{\mathrm{unst}}$ (vs square root on 2D). Reflects 1D bubble density.

### 3.4 Complete graph $K_n$

Single threshold → $\widehat K = 1$ for all $\beta > \beta_{\mathrm{crit}}$. Very simple phase structure; $c$ and $T$ don't qualitatively change the picture (just shift $\beta_{\mathrm{crit}}$).

---

## §4. Regime boundaries explicit

### 4.1 Critical $\beta_{\mathrm{crit}}^{(2)}(c, T; G)$

Thermal-extended Prop 1.3a:
$$\beta_{\mathrm{crit}}^{(2)}(c, T) = \frac{4\alpha\lambda_2(G)}{|W''(c)| - T/[c(1-c)]}.$$

Diverges when $|W''(c)| = T/[c(1-c)]$, i.e., at the thermal dissolution line.

**Locus of dissolution:** $T_{\mathrm{dis}}(c) = c(1-c)|W''(c)| = c(1-c)(2 - 12c + 12c^2)$.

$c \in (c_-, c_+)$, $|W''|$ max at $c = 1/2$ ($|W''(1/2)| = 1$), so $T_{\mathrm{dis}}(1/2) = 1/4$. Decreasing away from $c = 1/2$.

### 4.2 Saturation boundary $\beta_{\mathrm{crossover}}(c, G)$

From Round 7: $\beta_{\mathrm{crossover}} \sim 16\pi^2/L$ on 2D grid. Weakly $c$-dependent (via $|W''(c)|$ in $\beta^{(k)}_{\mathrm{crit}}$).

Not strongly $T$-dependent (since $H_{\mathrm{cl,sep}}$ is $T$-invariant, only $H_{\mathrm{bd}}$ thermal; shift rescales $\beta$).

### 4.3 K=2 emergence $\beta^{\mathrm{sec}}_{1 \to 2}(c, T; G)$

From R11: $\beta^{\mathrm{sec}}_{1 \to 2} \approx \beta_{\mathrm{crit}}^{(4)}(c, T)$ on 2D grid. Thermal shift via same formula as §4.1.

### 4.4 Regime I/II/III $c$-boundaries

$c_{\mathrm{bif}}^\pm$ (R6): $\approx 0.385, 0.545$ at $a_D = 5$ canonical. Weakly $T$-dependent via thermal effect on distinction operator (but $H_{\mathrm{cl,sep}}$ is $T$-invariant, so $c_{\mathrm{bif}}^\pm$ are $T$-independent).

**Net:** $c_{\mathrm{bif}}^\pm$ is a constant independent of $\beta, T$ for fixed $a_D$.

---

## §5. Dimensional reduction

### 5.1 2D slice: $\widehat K(\beta, c)$ at $T = 0$

At $T = 0$: drop thermal axis. 2D diagram with $\beta$ (horizontal) and $c$ (vertical). Three vertical bands (Regimes I/II/III) separated by $c_{\mathrm{bif}}^\pm$. Each band has monotone $\widehat K(\beta)$.

### 5.2 2D slice: $\widehat K(c, T)$ at fixed $\beta$

At $\beta$ moderate: $\widehat K$ depends on $c$ (Regime-dependent) and $T$ (linear decrease).

Dissolution line $T_{\mathrm{dis}}(c)$ caps the diagram from above.

### 5.3 2D slice: $\widehat K(\beta, T)$ at $c = 1/2$

Canonical slice. $\widehat K$ increases with $\beta$, decreases with $T$. Saturation at high $\beta$.

### 5.4 1D slice: $\widehat K(\beta)$ at $c = 1/2, T = 0$

Classical Conjecture 2.1 curve: $\widehat K \sim 1 + \sqrt{N_{\mathrm{unst}}(\beta)}$ on 2D grid.

---

## §6. Category + residuals

### 6.1 New Cat A claims (Round 15)

1. **Master formula** $\widehat K = 1 + \mathrm{Vol} \cdot N_{\mathrm{unst}}^{1/d_{\mathrm{eff}}} + O(1)$ with all three $(\beta, c, T)$ dependencies.

2. **Thermal dissolution line** $T_{\mathrm{dis}}(c) = c(1-c)|W''(c)|$; max at $c = 1/2$ giving $T_{\mathrm{dis}}(1/2) = 1/4$.

3. **3-phase structure** in $(\beta, c, T)$: uniform / single-formation / multi-formation / saturation, each a 3D region bounded by 2D surfaces.

4. **Regime-I/II/III $c$-boundaries are $T$-independent** — $c_{\mathrm{bif}}^\pm$ depends only on $a_D$.

5. **Graph-class $\widehat K$ scaling** — intensive on 2D grid, extensive on torus, linear on cycle, constant on $K_n$.

6. **Dimensional slices** — 2D and 1D reductions of full phase diagram.

### 6.2 Residuals from Round 15

- **Explicit $K_{\max}$ for capping** at each $c, T$ — depends on mass fraction.
- **Phase boundaries in physically realistic parameter scan** — at canonical $(\alpha, a_D, \lambda_D, \tau_D)$, the regime widths may shrink/grow.
- **Thermal regime in $\mathcal{M}_K$** — multi-formation phase diagram depends on $T$ via single-formation thermal, but inter-formation interactions also thermally modified (exponential barrier $\sim e^{-\Delta F/T}$).
- **Co-belonging/aggregation in phase diagram** — energy decomposition beyond $\mathcal{E}_{\mathrm{bd}} + \mathcal{E}_{\mathrm{cl,sep}}$ may open new regimes.

### 6.3 Cumulative Cat A

- R1-14: 73
- **R15: 6**
- **Cumulative: 79.**

### 6.4 Next: Round 16 (FINAL medium-term round)

Item 6: F-1 multi verification. Apply R11-15 framework to explicitly confirm K=2 dissolution of F-1 "K=2 vacuity" original concern.

---

**End of 17_deepening_round15.md.**
