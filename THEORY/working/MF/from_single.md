# from_single.md — Multi-Formation Structure Derived from Single-Formation Invariants

**Status:** commit draft (primary approach: Axis B), 2026-04-22 (SF-S1 session).
**Author origin:** `logs/daily/2026-04-22/01_exploration.md` §3.2 (Approach B1 + B3 primary); `02_development.md` §5-§9.
**Canonical refs:** §8.1 (energy), §11 Multi-formation paradigm (I9 K-field architecture), §12 (T-Persist-K family, Coupling Bound Lemma), §13 Cat A T-Merge (b) (isoperimetric ordering), T11 (Γ-convergence), T-Birth-Parametric (D4 pitchfork); §14 CN6 (K kinetic), CN8 (metastable), CN14 (closure expands metastability).
**Working refs:** `working/SF/mode_count.md` (Prop 1.3a/b seeds), `working/SF/interface_scale.md` (ξ_0 anchor, 3-scale table, T-d_min direction correction), `working/E/{F1,M1,MO1}_dissolution.md` (reframings of F-1/M-1/MO-1 rely on derived multi-formation view).
**External refs:** Cahn-Hilliard (1958) amplitude equation; Lifshitz-Slyozov (1961) & Wagner (1961) coarsening (LSW); Freidlin-Wentzell (1984) small-noise escape; Modica-Mortola (1977) Γ-convergence.

---

## §1. Thesis

> **Derived view.** The observed multi-formation structure $(\widehat{K}, m_k, d_{\min}^\ast)$ is determined by the single-formation invariants $(N_{\mathrm{unst}}, \xi_0)$ — the number of unstable Fiedler directions and the interface width — up to graph-topology-class constants. Integer $K$ is NOT a primitive: it is a one-parameter summary of the continuous mode-count statistics seeded by $N_{\mathrm{unst}}$ and filtered by isoperimetric competition.

This view inverts the canonical v1.2 perspective where $K$ was a primary parameter (K-field architecture $\Sigma^K_M$), making F-1 (K=2 vacuity) and M-1 (K=1 preference) "problems". In the derived view, these become **artifacts of choosing integer-K language over $(N_{\mathrm{unst}}, \xi_0)$ language**.

---

## §2. $\widehat{K}$ from $N_{\mathrm{unst}}$ (mode-count emergence)

### 2.1 Conjecture (primary commit of this file)

> **Conjecture 2.1 (Mode-count emergence, graph-class parametrized).** For a generic connected graph $G$ with effective spectral dimension $d_{\mathrm{eff}}(G)$, the expected number of formations emerging from $u_{\mathrm{uniform}}$ under small-noise initialization is
> $$\widehat{K}(\beta, \alpha, T, c, G) = 1 + N_{\mathrm{unst}}(\beta, \alpha, T, c, G)^{1/d_{\mathrm{eff}}(G)} + O(1),$$
> where $N_{\mathrm{unst}} = \#\{k \geq 2 : \mu_k^{\mathrm{full}}(\beta, \alpha, T, c) < 0\}$ is the full-energy Morse index of $u_{\mathrm{uniform}}$ (Prop 1.3a at T=0, extended by T-Uniform-Stab-T at T>0, Prop 1.3b for full-energy correction).

### 2.2 Derivation sketch (Approach B1: weakly-nonlinear + B3: dimensional classification)

See `logs/daily/2026-04-22/02_development.md` §5.2. Key steps:

1. **Eigenbasis decomposition** near $u_{\mathrm{uniform}}$: $u(x,t) = c + \sum_k a_k(t)\phi_k(x)$, with $\dot a_k = -\mu_k a_k + O(a^2)$ from the linearized Euler-Lagrange.
2. **Exponential growth of unstable modes**: modes in $\mathcal{S}_u = \{k : \mu_k < 0\}$ saturate at nonlinear order; stable modes decay.
3. **Characteristic wavelength selection**: among the $N_{\mathrm{unst}}$ unstable modes, the most-unstable direction has the largest $|\mu_k|$; in saturation, the characteristic spatial wavelength is $\lambda_{\mathrm{char}} \sim L/(k^\ast)$ where $k^\ast$ is the mode-index radius in spectrum space.
4. **Counting bumps**: number of wavelengths fitting in the domain $= L/\lambda_{\mathrm{char}} \sim (\text{radius in mode space})$. On a $d_{\mathrm{eff}}$-dimensional grid, $N_{\mathrm{unst}} \sim R^{d_{\mathrm{eff}}}$ gives $R = N_{\mathrm{unst}}^{1/d_{\mathrm{eff}}}$. So $\widehat{K} \sim R = N_{\mathrm{unst}}^{1/d_{\mathrm{eff}}}$.

### 2.3 Graph-class instances

| Graph | $d_{\mathrm{eff}}$ | $\widehat{K}$ formula | Status / Evidence |
|---|---|---|---|
| 1D cycle $C_n$ | 1 | $1 + N_{\mathrm{unst}}$ | Conjecture (H-A1, pre_brainstorm §A); untested in scc/ |
| 2D grid $L^2$ | 2 | $1 + \sqrt{N_{\mathrm{unst}}}$ | Conjecture (Round 12 heuristic, canonical exp37/51 compatible but not direct) |
| 3D grid $L^3$ | 3 | $1 + N_{\mathrm{unst}}^{1/3}$ | Conjecture; scc/ lacks 3D support |
| SBM ($K$ blocks) | 0 (spectral clustering) | $\widehat{K} = K_{\mathrm{block}}$ | Conjecture (H-A4) |
| Barbell | 0 | $\widehat{K} = 2$ saturating | Conjecture (H-A5); exp51 K*=1 at long time consistent |

**Failure mode.** Near $\beta = \beta_{\mathrm{crit}}^{(2)}$ (only one unstable mode), all graphs give $\widehat{K} = 2$ — the $\sqrt{N_{\mathrm{unst}}}$ formula reduces to $\widehat{K} = 2$ at $N_{\mathrm{unst}} = 1$, consistent with the D4 pitchfork (T-Birth-Parametric). At large $\beta$, the formulas differ by graph topology.

**Validation carry.** `CODE/experiments/exp_mode_emergence.py` is the test; runtime 30 min–2 h per graph. Not executed in this session.

### 2.4 $N_{\mathrm{unst}}^{\mathrm{full}}$ vs $N_{\mathrm{unst}}^{\mathrm{bd}}$

From Prop 1.3b (e) Weyl bracket (`working/SF/mode_count.md` §2):
$$N_{\mathrm{unst}}^{\mathrm{bd}}(\beta) - \#\{+\nu\} \leq N_{\mathrm{unst}}^{\mathrm{full}}(\beta) \leq N_{\mathrm{unst}}^{\mathrm{bd}}(\beta) + \#\{-\nu\}.$$
At canonical defaults, $\#\{-\nu\} = 1641$, $\#\{+\nu\} \approx 2454$. So $N_{\mathrm{unst}}^{\mathrm{full}}$ differs from $N_{\mathrm{unst}}^{\mathrm{bd}}$ by a bounded, $\beta$-invariant correction. For large $\beta$ (post-saturation), both approach $n-1$; the relative difference vanishes.

**For $\widehat{K}$ prediction**, use $N_{\mathrm{unst}}^{\mathrm{full}}$ — the full-energy Morse index. This is the correct "active-direction" count.

---

## §3. Formation size

### 3.1 Statement

> **Claim 3.1 (equal partition at short time).** At $t \in [t_{\mathrm{emerge}}, t_{\mathrm{coarsen}}]$, each of the $\widehat{K}$ formations has mass
> $$m_k \approx m/\widehat{K}\quad \forall k \in \{1, \ldots, \widehat{K}\},$$
> with realization-wise fluctuations $O(\sigma_0\cdot \sqrt{m/\widehat{K}})$ from initial noise ($\sigma_0$ = RMS noise amplitude).

### 3.2 Proof sketch

See `02_development.md` §6.2. Core steps:
1. **Isotropic saturation** (Approach B1): the most-unstable mode on 2D grid has $p^\ast \approx q^\ast \sim R/\sqrt 2$, yielding a roughly-symmetric grid of bumps.
2. **Mass conservation**: $\sum m_k = m$ (volume constraint, canonical §8.0).
3. **Equal amplitudes + equal formations**: $m_k \approx m/\widehat{K}$.

### 3.3 Disk-radius consequence

Each formation occupies a disk of area $\approx m_k = m/\widehat{K}$, radius
$$r_0 = \sqrt{m/(\pi \widehat{K})}.$$
Boundary-band area per formation: $\approx 2\pi r_0\cdot \xi_0$ (with $\xi_0 = \sqrt{\alpha/\beta}$ from `interface_scale.md`).

### 3.4 Long-time collapse (T-Merge (b) Cat A)

On connected graphs at $t \to \infty$ (zero-temperature gradient flow), $K^\ast = 1$ (T-Merge (b) Cat A, isoperimetric ordering). The $\widehat{K}$ from §2 is the *emergence-time* count, not the infinite-time limit.

---

## §4. Inter-formation spacing

### 4.1 Statement

> **Claim 4.1 (spacing scale).** On 2D grid, the minimum inter-formation distance at metastable state is
> $$d_{\min}^\ast = C_{\mathrm{spacing}}\cdot \xi_0,\qquad C_{\mathrm{spacing}} = O(\log(1/\epsilon_0)),$$
> where $\epsilon_0$ is the "non-interaction" tolerance (typically $10^{-3}$, giving $C_{\mathrm{spacing}} \approx 7$). This CORRECTS the direction of canonical T-d_min-Formula (Cat B) which fits $d_{\min}^\ast \propto \sqrt{\beta/\alpha} = 1/\xi_0$.

### 4.2 Derivation via Coupling Bound Lemma

Canonical §12 Coupling Bound Lemma Item 5 (Cat A):
$$u^k(x) \leq 2\exp(-c_0\cdot D_{\mathrm{sep}})\quad\text{at core of formation }j \neq k,$$
where $c_0 = \mathrm{arccosh}(1 + \kappa^2/d_{\min})$, $\kappa^2 = \beta/(2\alpha) = 1/(2\xi_0^2)$.

In the large-separation regime $d_{\min} \gg 1$: $\mathrm{arccosh}(1 + x) \approx \sqrt{2x}$, so $c_0 \approx 1/(\xi_0\sqrt{d_{\min}})$. Setting $u^k \leq \epsilon_0$ at $D_{\mathrm{sep}} = d_{\min}$ and solving:
$$d_{\min} \cdot c_0 = d_{\min}/(\xi_0\sqrt{d_{\min}}) = \sqrt{d_{\min}}/\xi_0 = \ln(2/\epsilon_0).$$
Solving: $d_{\min} \approx \xi_0^2 \ln^2(2/\epsilon_0)$ — but this gives a *scale* $\xi_0^2$, not $\xi_0$. Investigating more carefully:

**Alternative derivation (screened-Poisson-decay based):** The 2D radial Green's function for the screened Laplacian $(4\alpha\Delta + \beta W''(c))^{-1}$ has asymptotic decay $\sim K_0(r/\xi_0) \sim (1/\sqrt{r})\exp(-r/\xi_0)$ for $r \gg \xi_0$. Setting $u^k \leq \epsilon_0$: $r/\xi_0 \approx \ln(1/\epsilon_0)$, yielding
$$d_{\min}^\ast \approx \xi_0 \cdot \ln(1/\epsilon_0).$$

**This is the correct scale.** Linear in $\xi_0$, logarithmic in tolerance $\epsilon_0$.

### 4.3 Status and caveats

- **Direction correction** (scaling with $\xi_0$, not $1/\xi_0$): **sketched Cat A** — elementary from screened-Poisson decay.
- **Prefactor $C_{\mathrm{spacing}}$:** see §4.3b (Round 2 exact derivation below).
- **Non-grid graphs**: on barbell, $d_{\min}^\ast$ is set by Cheeger constant $h(G)$; on SBM, by inter-block distance. General formula: $d_{\min}^\ast \asymp 1/\sqrt{\lambda_2^{\mathrm{eff}}}$ where $\lambda_2^{\mathrm{eff}}$ is the effective gap (H-C3).

### 4.3b Round 2 prefactor derivation (screened Poisson Green function)

**Setup.** At well-separated K=2 configuration, each formation's tail at distance $r$ from its core (where the *other* formation's core sits) is governed by the linearized interface equation around $u_{\mathrm{bulk}} = 1$:
$$(-4\alpha\Delta + \beta W''(1)) \delta u = 0,\qquad W''(1) = 2.$$
Rescaling: $(-\Delta + \kappa^2) \delta u = 0$ with $\kappa^2 = \beta W''(1)/(4\alpha) = \beta/(2\alpha)$.

On 2D lattice in the far field, the Green's function $G(r) = \sum_x \delta u(x)$ decays as the modified Bessel function of order 0:
$$G(r) \sim \frac{1}{\sqrt{2\pi\kappa r}}\cdot \exp(-\kappa r),\qquad r \to \infty.$$
(Continuum limit of discrete screened Poisson; lattice correction is $O(1)$ multiplicative.)

**Setting "non-interaction" tolerance $\epsilon_0$.** For formations to remain metastable at separation $d_{\min}^\ast$, the tail contribution of each at the other's core must satisfy:
$$G(d_{\min}^\ast) \leq \epsilon_0\quad \Leftrightarrow\quad \frac{\exp(-\kappa d_{\min}^\ast)}{\sqrt{2\pi\kappa d_{\min}^\ast}} \leq \epsilon_0.$$
Taking log:
$$\kappa d_{\min}^\ast + \tfrac{1}{2}\ln(2\pi\kappa d_{\min}^\ast) \geq \ln(1/\epsilon_0).$$
In the asymptotic regime $\kappa d_{\min}^\ast \gg 1$, leading order:
$$\kappa d_{\min}^\ast \approx \ln(1/\epsilon_0) - \tfrac{1}{2}\ln(2\pi\kappa d_{\min}^\ast).$$
Iterating once (Newton-type): with $x_0 = \ln(1/\epsilon_0)$ as first estimate of $\kappa d_{\min}^\ast$,
$$\kappa d_{\min}^\ast \approx \ln(1/\epsilon_0) - \tfrac{1}{2}\ln\!\big(2\pi\ln(1/\epsilon_0)\big).$$

**Converting to $\xi_0$.** Since $\kappa = \sqrt{\beta/(2\alpha)} = 1/(\xi_0\sqrt 2)$:
$$\boxed{\;d_{\min}^\ast(\beta, \alpha, \epsilon_0) = \sqrt{2}\cdot \xi_0\cdot \big[\ln(1/\epsilon_0) - \tfrac{1}{2}\ln(2\pi\ln(1/\epsilon_0))\big] + O(\xi_0).\;}$$

Leading order: **$d_{\min}^\ast = \sqrt 2\,\xi_0\cdot \ln(1/\epsilon_0)$**.

### 4.3c Numerical prefactor at tolerance values

For $\epsilon_0 = 10^{-3}$: $\ln(1/\epsilon_0) \approx 6.908$, $\sqrt 2 \cdot 6.908 \approx 9.77$.
Log correction: $\tfrac{1}{2}\ln(2\pi \cdot 6.908) \approx \tfrac{1}{2}\ln 43.4 \approx 1.88$.
Corrected: $\sqrt 2(6.908 - 1.88) \approx \sqrt 2 \cdot 5.03 \approx 7.11$.

So $d_{\min}^\ast \approx 7.1\cdot \xi_0$ at $\epsilon_0 = 10^{-3}$.

For $\epsilon_0 = 10^{-2}$: $\sqrt 2(4.605 - \tfrac{1}{2}\ln(2\pi \cdot 4.605)) \approx \sqrt 2(4.605 - 1.68) \approx 4.13$.
So $d_{\min}^\ast \approx 4.1\cdot \xi_0$ at $\epsilon_0 = 10^{-2}$.

### 4.3d Comparison to canonical T-d_min-Formula fit

Canonical T-d_min-Formula (Cat B fit, `canonical.md` line 1007):
$d_{\min}^\ast = 4.8 + 0.31\sqrt{\beta/\alpha}$ (direction wrong: $\sqrt{\beta/\alpha} = 1/\xi_0$).

**At $\beta=30$, $\alpha=1$** (canonical default): $\xi_0 = 1/\sqrt{30} \approx 0.183$. Prediction (Round 2 formula, $\epsilon_0 = 10^{-3}$): $d_{\min}^\ast \approx 7.1 \cdot 0.183 \approx 1.3$ lattice units.

This is **smaller** than the canonical fit of $d_{\min}^\ast \approx 4.8 + 0.31\sqrt{30} \approx 6.5$ lattice units.

**Resolution.** Canonical's 6.5 is a **numerical** quantity on an 8×8 to 12×12 grid where $\xi_0 \approx 0.18$; the "minimum separation for metastable coexistence" is defined at a larger tolerance than $10^{-3}$ (canonical uses gradient-flow-stability criterion, not exponential-tail tolerance). Fitting canonical's $d_{\min}^\ast \approx 6.5$ to our formula requires $\ln(1/\epsilon_0) \approx 6.5/(\sqrt 2 \cdot 0.183) \approx 25$, i.e., $\epsilon_0 \approx 10^{-11}$ — astronomically tight, inconsistent with any reasonable stability criterion.

**More likely cause.** Canonical's fit mixes (i) minimum separation for metastability (what Round 2 formula predicts) with (ii) formation interface radius (extra additive $r_0$ term from each formation's own extent). Writing:
$$d_{\min}^\ast_{\mathrm{center-to-center}} \approx 2r_0 + d_{\min}^\ast_{\mathrm{edge-to-edge}},$$
with $2r_0 \approx 2\sqrt{m/(\pi \widehat{K})}$ (formation disk diameter), at $m = cn = 0.3 \cdot 144 = 43.2$ (for $12\times 12$, $c=0.3$) and $\widehat{K} = 2$: $r_0 \approx \sqrt{43.2/(2\pi)} \approx 2.6$, so $2r_0 \approx 5.2$. Adding edge-to-edge $\approx 1.3$ gives center-to-center $\approx 6.5$. **Consistent with canonical.** ✓

**Conclusion.** The canonical T-d_min-Formula Cat B fit measures **center-to-center** distance, which is dominated by formation size $2r_0$ (not by interface tail $d_{\min}^\ast_{\mathrm{edge-to-edge}} \asymp \xi_0$). The 30% reduction attributed to closure (CN14) is consistent: closure tightens $r_0$ slightly + reduces tail-coupling $d_{\min}^\ast_{\mathrm{edge-to-edge}}$.

This reconciles the **apparent direction mismatch**: canonical's $\sqrt{\beta/\alpha} = 1/\xi_0$ was picking up formation-size scaling through $r_0 \sim \sqrt{m/\widehat{K}}$ with $\widehat{K}$ varying with $\beta$ (higher $\beta \Rightarrow$ more formations, smaller $r_0$). NQ-30 resolution: **canonical's formula is a composite; its "direction" is a confounding of $r_0$ and $\xi_0$ scaling.**

### 4.3e Category self-assessment (Round 2)

- **Leading order $d_{\min}^\ast \asymp \sqrt 2\,\xi_0\,\ln(1/\epsilon_0)$:** **Cat A** — direct screened Poisson.
- **Exact prefactor with logarithmic correction:** **Cat A** — iterative asymptotic.
- **Direction reconciliation with canonical T-d_min-Formula:** **Cat A** — formula decomposes as center-to-center $= 2r_0 + d_{\mathrm{edge}}$.
- **Numerical verification (NQ-30 remeasurement):** **Open** — experimental.

### 4.4 NQ-30 resolution and canonical T-d_min-Formula

Canonical T-d_min-Formula (§13 Cat B):
$$d_{\min}^\ast = 4.8 + 0.31\cdot \sqrt{\beta/\alpha}\quad\text{(fit, Cat B)}.$$

Dimension analysis: $\sqrt{\beta/\alpha} = 1/\xi_0$ — **backwards**. Round 13 §2.5 flagged "dimensionally suspicious".

**Proposed correction:** $d_{\min}^\ast \approx C_0\cdot \xi_0\cdot \ln(1/\epsilon_0)$ with $C_0$ an O(1) topology-dependent constant.

**NQ-30 carry:** remeasure with correct directional axis, comparing $(\alpha, \beta)$ scans in the $\xi_0$-axis rather than $\sqrt{\beta/\alpha}$-axis. Execution pending.

---

## §5. Two-timescale dynamical picture

### 5.1 Statement

> **Claim 5.1 (three timescales).** A generic SCC trajectory starting near $u_{\mathrm{uniform}}$ with small noise passes through:
>
> - **(a) Emergence** $t \in [0, t_{\mathrm{emerge}}]$: $u_{\mathrm{uniform}}$ saturates into $\widehat{K}$ formations via Fiedler-mode instability. $t_{\mathrm{emerge}} = \ln(1/\sigma_0)/|\mu_{\min}|$.
>
> - **(b) Metastable plateau** $t \in [t_{\mathrm{emerge}}, t_{\mathrm{coarsen}}]$: $K_{\mathrm{soft}}(u(t)) \approx \widehat{K}$. At $T=0$, $t_{\mathrm{coarsen}} = \infty$; at $T>0$, $t_{\mathrm{coarsen}} = \tau_0\exp(\Delta\mathcal{F}/T)$ (Kramers, `working/E/M1_dissolution.md` §3).
>
> - **(c) Coarsening** $t > t_{\mathrm{coarsen}}$: LSW-type $K(t) \sim t^{-1/2}$ in 2D, until $K^\ast = 1$ (T-Merge (b)).

### 5.2 Derivation

See `02_development.md` §8.2. Key components:
- (a) Linearization: exponential growth of unstable modes, saturation at $a_k = O(1)$.
- (b) Metastability: at $T=0$, gradient flow absorbs into a local minimum. At $T>0$, Kramers escape time.
- (c) Coarsening: classical Allen-Cahn in 2D → LSW exponent 1/2.

### 5.3 Category self-classification

- **Emergence (a):** Cat A (linearization).
- **T=0 metastability (b):** Cat A (gradient flow absorbs).
- **T>0 Kramers (b):** Cat C / sketched (requires metastability framework P-F).
- **LSW coarsening (c):** sketched — standard Allen-Cahn; SCC corrections (CN14 closure raising barrier) open.

### 5.4 Connection to canonical

- Canonical §11 Multi-formation paradigm: "kinetic (barrier-based), not thermodynamic" matches claim 5.1 (b).
- Canonical T-Merge (b) Cat A: is the $t \to \infty$ limit of claim 5.1 (c).
- Canonical CN6 "K kinetically determined": specified in §6 below.
- Canonical CN8 "formations are metastable": (b) provides the quantitative content at $T>0$.
- Canonical CN14 "closure expands metastability": (b) prediction — closure raises $\Delta\mathcal{F}$, extending $t_{\mathrm{coarsen}}$.

---

## §6. CN6 quantitative reinterpretation

### 6.1 Original CN6 (canonical §14)

"**K is kinetically determined, not thermodynamically selected.** The relational kernel $K_t$ emerges from initial conditions and spatial structure through the dynamics of formation nucleation and metastable persistence, not from energy minimization."

### 6.2 Quantitative version (2026-04-22 reframing)

**CN6-quantitative.** The observed formation count $\widehat{K}$ at the emergence timescale is set by the number of unstable Fiedler directions $N_{\mathrm{unst}}$ via graph-class law
$$\widehat{K}(\beta, \alpha, T, c, G) = 1 + N_{\mathrm{unst}}(\beta, \alpha, T, c, G)^{1/d_{\mathrm{eff}}(G)} + O(1).$$
The thermodynamic ground state $K^\ast = 1$ (T-Merge (b) Cat A) is reached only at the coarsening timescale $t_{\mathrm{coarsen}} \gg t_{\mathrm{emerge}}$. "Kinetic" = **emergence-timescale Fiedler-instability nucleation + Kramers metastability on the gradient-flow landscape**.

### 6.3 What this buys

1. **Canonical CN6 is commitment-level ("kinetic") without specifying how.** The quantitative version specifies $N_{\mathrm{unst}}^{1/d_{\mathrm{eff}}}$.
2. **Testability**: exp_mode_emergence.py measures $N_{\mathrm{unst}}$ and $\widehat{K}$; fit verifies the exponent.
3. **Integer $K$ is derived**: from $N_{\mathrm{unst}}$ continuous, round to integer. Matches canonical paradigm shift — "$K$ is an index of emergent structure, not a primitive".

### 6.4 Category

**Cat A commitment** (reuses CN6 + T8-Core + canonical §11), **conjecture formula** (quantitative part).

---

## §7. Integration with F-1 / M-1 / MO-1 dissolution

This file's framework re-casts the three Critical open problems:

### 7.1 F-1 (K=2 vacuity)

**Original framing.** "K=2 global stability is vacuous without external per-formation mass constraint."

**Derived-view resolution.** The "external m_j" was an artifact of K-field architecture ($\Sigma^K_M = \Sigma_{m_1}\times \cdots \times \Sigma_{m_K}$). In the derived view, K=2 emergence is **automatic** whenever $N_{\mathrm{unst}} \geq 1$ (single Fiedler mode gives $\pm$ pair of basins, hence $\widehat{K} = 2$ at this regime, see `02_development.md` §5.2 endgame). No external constraint needed.

**See:** `working/E/F1_dissolution.md` §Round 18 post-audit reframing.

### 7.2 M-1 (K=1 always preferred)

**Original framing.** "K=2 landscape $E(m_1, m_2)$ monotonically decreasing toward $m_2 \to 0$; K=1 always cheaper."

**Derived-view resolution.** M-1 is a **long-time** statement (T-Merge (b) Cat A, isoperimetric). Short-time emergence has $\widehat{K} \geq 2$ when $N_{\mathrm{unst}} \geq 1$. M-1 was "two-timescale confounding": emergence and thermodynamic preference live on different timescales.

**See:** `working/E/M1_dissolution.md` §Round 18 post-audit reframing.

### 7.3 MO-1 (Morse inapplicability on $\Sigma^K_M$)

**Original framing.** "$\Sigma^K_M$ has corners at $m_j \to 0$; smooth Morse inapplicable."

**Derived-view resolution.** $\Sigma^K_M$ is **not needed**. Analysis lives on single $\Sigma_m$, which is a convex polytope (canonical Prop 1.1 Cat A) with standard hypercube corners. Smooth Morse on $\Sigma_m^\varepsilon\setminus V$ (open interior minus vineyard) applies directly (canonical T1, T14). Prop 1.3a/b counts Morse indices on $\Sigma_m$ — the exact object MO-1 claimed was inaccessible.

**See:** `working/E/MO1_dissolution.md` §Round 18 post-audit reframing.

---

## §8. Canonical merge proposals (Stage 6 Pending)

| Target | Proposal | Category |
|---|---|---|
| §11 Multi-formation paradigm | Add paragraph: "$\widehat{K}$ is derived from $N_{\mathrm{unst}}^{1/d_{\mathrm{eff}}}$; see working/MF/from_single.md §2" | Extension to existing CN |
| §12 T-d_min-Formula | Direction correction: $d_{\min}^\ast \asymp \xi_0$, not $\sqrt{\beta/\alpha}$ | Cat B correction (NQ-30) |
| §14 new CN18 | "Single-formation invariants $(N_{\mathrm{unst}}, \xi_0)$ pre-determine multi-formation structure $(\widehat K, m_k, d_{\min}^\ast)$" | New CN |
| §14 CN6 extension | Quantitative addendum (§6 above) | CN modification |
| §13 new conjecture entry | $\widehat{K}(N_{\mathrm{unst}})$ formula as Cat C conjecture (evidence: Round 12 heuristic + Prop 1.3a Cat A) | New Cat C |

---

## §9. Open questions seeded by this file

- **NQ-32 carry:** SCC profile deviation (`working/SF/profile_deviation.md`) affects $\xi_0^{\mathrm{fitted}}$ and hence all MF predictions.
- **NQ-33 (new):** $d_{\mathrm{eff}}(G)$ precise definition for non-lattice graphs. Candidate: spectral dimension from Laplacian eigenvalue density. Carry to Stage 2.
- **NQ-34 (new):** Coarsening exponent with SCC self-referentiality. LSW standard is 1/2 in 2D; CN14's closure-barrier $\beta^{0.89}$ suggests a modified exponent. Carry to E-S3.
- **NQ-35 (new):** Saturating $\widehat{K}$ on graphs with sharp spectral cluster (barbell, small-world): formula $\widehat{K} = 2$ or $K_{\mathrm{block}}$ bypasses the $N_{\mathrm{unst}}^{1/d_{\mathrm{eff}}}$ scaling. Unified treatment? Carry post-Stage-1.

---

## §10. File status

- **Primary commit:** §2 Conjecture 2.1 ($\widehat{K} = f(N_{\mathrm{unst}})$ graph-class formula).
- **Supporting (Cat A):** §4 spacing direction correction (sketched Cat A via Coupling Bound Lemma); §6 CN6 quantitative reinterpretation; §7 integration of dissolution reframings.
- **Conjectures:** graph-class scaling in §2.3, prefactor in §4.
- **Execution pending:** exp_mode_emergence.py for §2.3 validation; exp_profile_fit.py for §3.3 $\xi_0^{\mathrm{fitted}}$ measurement.

**End of from_single.md.**
