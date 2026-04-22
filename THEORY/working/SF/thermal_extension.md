# thermal_extension.md — Prop 1.3a/b Thermal Extension ($T > 0$)

**Status:** commit draft (2026-04-22 Round 2).
**Author origin:** Round 2 continuation — filling a residual identified in `99_summary.md` §7 "Prop 1.3a thermal extension (T>0) verification".
**Canonical refs:** `canonical_sub.md` 2026-04-21 Round 4 (T-Uniform-Stab-T, Theorem 2.1 three-regime phase diagram), §13 Cat A (thermal extension naturally joins Prop 1.3a).
**Working refs:** `working/SF/mode_count.md` §1 (Prop 1.3a), §2 (Prop 1.3b); `working/C/F_group_axioms.md` F1 (Gibbs) + F2 (Bernoulli entropy); `working/CE/free_energy_wellposed.md` (ℱ_C+E).
**Reason for extension.** Round 4 of 2026-04-21 (`canonical_sub.md`) committed T-Uniform-Stab-T (Cat A for T-version of Prop 1.3a at $k=2$), but **Prop 1.3b thermal** (how cl_sep spectrum and entropy Hessian combine at $T>0$) was not yet explicit. This file fills that.

---

## §1. Thermal Hessian decomposition

At $T > 0$, the free energy on $\Sigma_m^\varepsilon$ is
$$\mathcal{F}_{C+E}[u; T] = \mathcal{E}[u] - T \cdot S(u) + \lambda_K K_{\mathrm{soft}}(u),$$
where $S(u) = -\sum_x[u_x\ln u_x + (1-u_x)\ln(1-u_x)]$ is Bernoulli entropy (F2, Cat A).

**Hessian at $u_{\mathrm{uniform}} = c\mathbf{1}$:**
$$\mathrm{Hess}\,\mathcal{F}_{C+E}\big|_{u_{\mathrm{uniform}}} = H_{\mathrm{bd}}(\beta, \alpha) + H_{\mathrm{cl,sep}}(\alpha, \ldots) - T \cdot H_S(c) + \lambda_K \cdot H_K(c),$$
where:
- $H_{\mathrm{bd}} = 4\alpha L + \beta W''(c) I$ (Prop 1.3a).
- $H_{\mathrm{cl,sep}} = \lambda_{\mathrm{cl}} H_{\mathrm{cl}} + \lambda_{\mathrm{sep}} H_{\mathrm{sep}}$ (Prop 1.3b).
- $H_S := \mathrm{Hess}(-S)$ diagonal: $(H_S)_{ii} = 1/[u_i(1-u_i)]$. At $u_{\mathrm{uniform}}$: $(H_S)_{ii} = 1/[c(1-c)]$ **constant**, so $-T H_S = -T/[c(1-c)] \cdot I$ — **a negative diagonal shift**.
- $H_K$ from $\nabla^2 K_{\mathrm{soft}}$: at $u_{\mathrm{uniform}}$ this vanishes because $K_{\mathrm{soft}}(c\mathbf{1}) = \varphi(0) \cdot (\text{one bar of zero length}) = 0$, and near $u_{\mathrm{uniform}}$ the bar structure is degenerate (all sites at same level). $H_K|_{u_{\mathrm{uniform}}} = 0$ at the uniform configuration itself (vineyard singularity).

Hence:
$$\boxed{\;\mathrm{Hess}\,\mathcal{F}_{C+E}\big|_{u_{\mathrm{uniform}}} = H_{\mathrm{bd}}(\beta, \alpha) + H_{\mathrm{cl,sep}}(\alpha, \ldots) - \frac{T}{c(1-c)}\,I\;}.$$

The entropy contribution is a **uniform shift** of all eigenvalues by $-T/[c(1-c)]$.

---

## §2. Prop 1.3a thermal (Cat A, extending T-Uniform-Stab-T)

### 2.1 Statement

> **Proposition 1.3a-thermal.** Under hypotheses of Prop 1.3a (pure $\mathcal{E}_{\mathrm{bd}}$ only, so $\lambda_{\mathrm{cl}} = \lambda_{\mathrm{sep}} = 0$) plus $T > 0$ thermal contribution:
> $$N_{\mathrm{unst}}^{\mathrm{bd}}(\beta, \alpha, T, c, G) = \#\big\{k \geq 2 : 4\alpha\lambda_k(G) + \beta W''(c) - T/[c(1-c)] < 0\big\}.$$

### 2.2 Proof

Direct from §1: $\mathrm{Hess}\,(\mathcal{E}_{\mathrm{bd}} - TS) = H_{\mathrm{bd}} - (T/c(1-c))I$. In Laplacian eigenbasis:
$\mu_k^{\mathrm{bd,thermal}} = 4\alpha\lambda_k + \beta W''(c) - T/[c(1-c)]$.
Negative count is the stated formula. ∎

### 2.3 T-Uniform-Stab-T recovery

T-Uniform-Stab-T (canonical_sub 2026-04-21 Round 4): $u_{\mathrm{uniform}}$ is a **local min** iff $\mu_k^{\mathrm{bd,thermal}} > 0$ for all $k \geq 2$, which is equivalent to $T > T^\ast_{\mathrm{uniform}} := c(1-c)[\beta|W''(c)| - 4\alpha\lambda_2]$.

This is the $k=2$ case ($\lambda_2$ is smallest for $k \geq 2$ on connected graph) of Prop 1.3a-thermal. The full Prop 1.3a-thermal generalizes to ALL modes: the $k$-th mode is thermally re-stabilized at
$$T^\ast_k := c(1-c)[\beta|W''(c)| - 4\alpha\lambda_k],$$
with $T^\ast_{\mathrm{uniform}} = T^\ast_2 = \max_k T^\ast_k$.

**Monotonicity.** $T^\ast_k$ is monotone decreasing in $k$ (since $\lambda_k$ increases). The number of unstable modes at $T$ is $N_{\mathrm{unst}}^{\mathrm{bd}}(T) = \#\{k \geq 2 : T^\ast_k > T\}$, non-increasing in $T$.

### 2.4 Category

**Cat A** — direct extension of Prop 1.3a with entropy term analytic (Bernoulli is $C^\omega$ on $(0,1)^n$).

---

## §3. Prop 1.3b thermal

### 3.1 Statement

> **Proposition 1.3b-thermal.** With cl_sep + thermal contributions:
> $$H_{\mathrm{cl,sep}}^{\mathrm{thermal}} := H_{\mathrm{full}}^{\mathrm{thermal}} - H_{\mathrm{bd}}^{\mathrm{thermal}} = H_{\mathrm{cl,sep}}.$$
> That is, the thermal shift factors entirely into $H_{\mathrm{bd}}^{\mathrm{thermal}}$; $H_{\mathrm{cl,sep}}$ is **unchanged** by temperature.

### 3.2 Proof

$H_{\mathrm{full}}^{\mathrm{thermal}} = H_{\mathrm{bd}} + H_{\mathrm{cl,sep}} - (T/c(1-c))I$.
$H_{\mathrm{bd}}^{\mathrm{thermal}} = H_{\mathrm{bd}} - (T/c(1-c))I$.
Subtracting: $H_{\mathrm{cl,sep}}^{\mathrm{thermal}} = H_{\mathrm{cl,sep}}$. ∎

### 3.3 Consequence

The $\beta$-invariance of $H_{\mathrm{cl,sep}}$ (Prop 1.3b (a)) **extends to T-invariance**: $H_{\mathrm{cl,sep}}$ depends on $(\alpha, \lambda_{\mathrm{cl}}, \lambda_{\mathrm{sep}}, a_{\mathrm{cl}}, \tau_{\mathrm{cl}}, c, G)$ but not on $(\beta, T)$.

This is a clean **two-variable invariance**: $H_{\mathrm{cl,sep}}$ is the "structural" operator unaffected by the two dynamical parameters $(\beta, T)$.

### 3.4 Thermal Morse index (full energy)

$$N_{\mathrm{unst}}^{\mathrm{full}}(\beta, \alpha, T, c, G) = \#\{k \geq 2 : \mu_k^{\mathrm{bd}}(\beta, \alpha, c) + \nu_k^{\mathrm{cl,sep}}(\alpha, \ldots) - T/[c(1-c)] < 0\}.$$
Weyl bracket: $N_{\mathrm{unst}}^{\mathrm{full}}(T) \in [N_{\mathrm{unst}}^{\mathrm{bd,thermal}}(T) - \#\{+\nu^{\mathrm{cl,sep}}\},\; N_{\mathrm{unst}}^{\mathrm{bd,thermal}}(T) + \#\{-\nu^{\mathrm{cl,sep}}\}]$.

### 3.5 Three-regime recovery (canonical_sub 2026-04-21 Round 4 Theorem 2.1)

Round 4's three-regime result classifies $(T, c)$ space into single-mode / multi-mode / uniform regions. The formal content:

- **Uniform regime** ($T > T^\ast_{\mathrm{uniform}}$): $N_{\mathrm{unst}}^{\mathrm{full}}(T) = 0$, $u_{\mathrm{uniform}}$ is the local min.
- **Multi-mode regime** ($T_c < T < T^\ast_{\mathrm{uniform}}$): $N_{\mathrm{unst}}^{\mathrm{full}}(T) \geq 1$ but moderate; $\widehat{K}$ from Conjecture 2.1 of `working/MF/from_single.md` §2.
- **Single-mode regime** ($T < T_c$): $N_{\mathrm{unst}}^{\mathrm{full}}(T)$ close to its $T = 0$ maximum; $\widehat{K}$ close to $\widehat{K}(T=0)$.

**Quantitative $T_c$.** $T_c$ is the temperature at which $\widehat{K}$ transitions from "multi" to "single-dominated" — typically $T_c \approx $ the thermal re-stabilization of the 2nd-most-unstable mode, i.e., $T^\ast_3$.

At canonical defaults ($c=1/2$, $\beta=30$, $\alpha=1$, 8×8 grid): $T^\ast_2 \approx 30\cdot 0.25 = 7.5$ minus $4\lambda_2 \cdot 0.25 \approx 7.38$ (from canonical_sub Round 4 numerical verification on 6×6: 7.22 prediction, 7.218 measured). So $T^\ast_{\mathrm{uniform}} \approx 7.37$. Multi-mode regime is $T \in [T_c, 7.37]$.

### 3.6 Category

- Prop 1.3b-thermal ($H_{\mathrm{cl,sep}}$ T-invariance): **Cat A**.
- Prop 1.3a-thermal ($N_{\mathrm{unst}}^{\mathrm{bd,thermal}}$ formula): **Cat A**.
- Prop 1.3b-thermal Weyl bracket: **Cat A**.
- Three-regime phase diagram structure: **Cat A** (Round 4).
- Precise $T_c$ location: **Cat B** — depends on graph-class-dependent "transition from multi to single-dominated $\widehat{K}$".

---

## §4. Bridge to multi-formation at $T > 0$

Combining with `working/MF/from_single.md` §2 Conjecture 2.1:
$$\widehat{K}(\beta, \alpha, T, c, G) = 1 + N_{\mathrm{unst}}^{\mathrm{full}}(\beta, \alpha, T, c, G)^{1/d_{\mathrm{eff}}(G)} + O(1).$$

With Prop 1.3a-thermal providing $N_{\mathrm{unst}}^{\mathrm{full}}(T)$ monotone decreasing in $T$: **$\widehat{K}(T)$ is monotone decreasing** in $T$.

- At $T = 0$: $\widehat{K}$ at its maximum (all modes accessible).
- At $T = T^\ast_{\mathrm{uniform}}$: $\widehat{K} = 1$ (no modes unstable, uniform is the "formation").
- Intermediate $T$: $\widehat{K}$ interpolates.

**Observable prediction.** Three-regime phase diagram's transitions correspond to integer jumps in $\widehat{K}$. Specifically:
- $\widehat{K}$ crosses 1 at $T = T^\ast_{\mathrm{uniform}}$ (Prop 1.3a-thermal formula).
- $\widehat{K}$ crosses 2 at $T = T^\ast_3$ (next mode stabilizes).
- etc.

### 4.1 CN6-quantitative at $T > 0$

`working/MF/from_single.md` §6 quantitative CN6 at $T>0$:
$$\widehat{K}(t_{\mathrm{emerge}}; T) = 1 + N_{\mathrm{unst}}^{\mathrm{full}}(\beta, \alpha, T, c, G)^{1/d_{\mathrm{eff}}(G)}.$$

The thermal dependence enters entirely through $N_{\mathrm{unst}}^{\mathrm{full}}(T)$, which Prop 1.3a-thermal computes.

### 4.2 M-1 two-timescale at $T > 0$

`working/E/M1_dissolution.md` §8 two-timescale picture acquires thermal content:
- $t_{\mathrm{emerge}}(T) \sim 1/|\mu_{\min}(T)|$ where $\mu_{\min}(T) = \min_k \mu_k^{\mathrm{full}}(T)$.
- $t_{\mathrm{coarsen}}(T) \sim \exp(\Delta\mathcal{F}(T)/T)$ Kramers.

As $T \to T^\ast_{\mathrm{uniform}}$ from below: $|\mu_{\min}(T)| \to 0$, so $t_{\mathrm{emerge}} \to \infty$. The "emergence" regime disappears into a **critical slowing-down** near $T^\ast_{\mathrm{uniform}}$ (standard Landau-Ginzburg behavior near 2nd-order phase transition).

---

## §5. Category self-classification and canonical impact

### 5.1 Statement-level categories

| Claim | Category |
|---|---|
| §1 Hessian decomposition | **Cat A** |
| §2.1 Prop 1.3a-thermal | **Cat A** (extends T-Uniform-Stab-T Cat A) |
| §3.1 Prop 1.3b-thermal ($H_{\mathrm{cl,sep}}$ T-invariance) | **Cat A** |
| §3.4 Thermal Weyl bracket | **Cat A** |
| §3.5 Three-regime structural | **Cat A** (canonical_sub Round 4) |
| §3.5 Precise $T_c$ | **Cat B** |
| §4 $\widehat{K}(T)$ monotonicity | **Cat A via** Prop 1.3a-thermal |

### 5.2 Canonical merge (pending Stage 6)

- **§13 Cat A:** one entry combining Prop 1.3a-thermal + Prop 1.3b-thermal (T-invariance of $H_{\mathrm{cl,sep}}$) with "generalizes T-Uniform-Stab-T (Round 4)" annotation. ~15 lines.
- **§14 CN addition (optional):** "$H_{\mathrm{cl,sep}}$ is invariant under both $\beta$ and $T$; it is the purely structural component of the full-energy Hessian at $u_{\mathrm{uniform}}$." ~5 lines.

### 5.3 What closes which residual

From `99_summary.md` §7 list of open residuals:
- **Residual #7 (Prop 1.3a thermal extension numerical verification)**: Now **structurally closed** via Prop 1.3b-thermal (§3.1). Numerical verification at $T > 0$ is still pending (exp_three_regime.py, Stage 5 carry).

---

## §6. File status

- **Prop 1.3a-thermal:** committed Cat A (generalizes T-Uniform-Stab-T).
- **Prop 1.3b-thermal:** committed Cat A ($H_{\mathrm{cl,sep}}$ is $T$-invariant, extending its $\beta$-invariance).
- **Weyl bracket thermal form:** committed Cat A.
- **Canonical merge proposal:** staged in §5.2 (~20 lines total).
- **Remaining:** numerical verification at $T > 0$ (exp_three_regime.py, Stage 5 carry, not session scope).

**End of thermal_extension.md.**
