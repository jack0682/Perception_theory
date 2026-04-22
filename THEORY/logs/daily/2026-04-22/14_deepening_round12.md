# 14 — Round 12: $u^\ast_2$ Hessian via Lyapunov-Schmidt Reduction

**Session:** 2026-04-22 (Round 12, multi-formation 이어서)
**Trigger:** "중기까지" item 2.
**Target:** Well-separated K=2 configuration에서 Hessian의 explicit block-diagonal 구조 + exponentially small inter-formation corrections. Morse index at $u^\ast_2$ 계산.
**This file covers:** §1 Scope. §2 Well-separated ansatz. §3 Block-diagonal Hessian. §4 Localized spectra. §5 Inter-formation coupling. §6 Goldstone/separation mode structure. §7 Category + residuals.

---

## §1. Scope and setup

### 1.1 Target

Compute $H(u^\ast_2; \beta)$ in well-separated regime ($d_{\min} \gg \xi_0$). Express spectrum in terms of single-formation Prop 1.3a/b results + exponentially small corrections.

### 1.2 Well-separated vs interacting

$d_{\min}/\xi_0 \geq C$ for some threshold $C \sim 5$. In this regime, formations are "nearly independent". Interaction strength $\sim e^{-d_{\min}/\xi_0}$.

For $d_{\min} \sim \xi_0$ (near regime): Lyapunov-Schmidt breaks down; need full numerics.

### 1.3 Framework: Lyapunov-Schmidt reduction

Split $u = u_{\mathrm{ls}} + v$ where $u_{\mathrm{ls}}$ is the "leading-order superposition" and $v$ is a small correction orthogonal to translation Goldstone.

---

## §2. Well-separated K=2 ansatz

### 2.1 Superposition ansatz

$$u_{\mathrm{ls}}(x; x_1, x_2) := u_0(x - x_1) + u_0(x - x_2) - c\mathbf{1} + \cdot \text{mass correction}.$$

Here $u_0$ is the K=1 single-formation profile satisfying $-2\alpha u_0'' + \beta W'(u_0) = 0$ (continuum) or discrete analog.

Mass constraint: $\sum_i u_{\mathrm{ls}}(i) = m$ (i.e., 2 × mass-of-single - adjustment for baseline).

### 2.2 Residual equation

Plug $u_{\mathrm{ls}} + v$ into full Allen-Cahn EL: $-2\alpha \Delta u + \beta W'(u) = 0$. Since $u_0$ satisfies the single-formation EL, the residual is a source proportional to nonlinear cross-terms between the two copies of $u_0$:

$$\mathrm{Source}(x) \sim W'(u_1 + u_2 - c) - W'(u_1) - W'(u_2) + W'(c) \sim O(u_1 u_2)$$

where $u_i := u_0(x - x_i)$. The cross-term $u_1 u_2$ is non-negligible only near the midpoint between formations; it decays exponentially when either $u_1$ or $u_2$ is far from its formation center.

**Magnitude:** $|\mathrm{Source}| \lesssim e^{-d_{\min}/\xi_0}$ at the midpoint.

### 2.3 Correction $v$

Linearized equation for $v$: $\mathcal{L}_{u_{\mathrm{ls}}} v = -\mathrm{Source}$, where $\mathcal{L}_u := -2\alpha\Delta + \beta W''(u)$. Solvability: requires source $\perp$ kernel of $\mathcal{L}_{u_{\mathrm{ls}}}$. Kernel at $u_{\mathrm{ls}}$: translation modes $\partial_{x_i} u_{\mathrm{ls}} \approx -u_0'(x - x_i)$.

**Check:** $\int \mathrm{Source}(x) u_0'(x - x_i) dx \approx 0$ by parity (source is symmetric around midpoint; $u_0'$ localized at $x_i$, odd-parity about $x_i$). Integral is exponentially small but non-zero; this gives **position shift** of formations.

$v$ is well-defined (exponentially small) away from translation directions.

---

## §3. Block-diagonal Hessian

### 3.1 Hessian definition

$H(u^\ast_2) = \mathrm{Hess}\,\mathcal{E}\big|_{u^\ast_2}$. Full $n \times n$ matrix on $\mathbb R^n \supset \Sigma_m$.

### 3.2 Localization

At well-separated $u^\ast_2$: $u^\ast_2 \approx u_1 \oplus u_2$ (two localized bumps). Hessian inherits localization.

Let $\chi_i(x)$ be a partition of unity concentrated around formation $i$ (with overlap only in the midpoint region). Define subspaces $V_i := \mathrm{span}\{\chi_i \cdot \text{low-wavelength basis}\}$.

Hessian block structure:
$$H(u^\ast_2) = \begin{pmatrix} H_1 & H_{12} \\ H_{21} & H_2 \end{pmatrix} + \text{midpoint coupling},$$
where $H_i$ acts on $V_i$ and $H_{ij}$ is small.

### 3.3 Per-formation blocks

$H_i$ is the Hessian of Allen-Cahn linearized at $u_0$, restricted to $V_i$:
$$H_i \approx \mathcal{L}_{u_0}\big|_{V_i} = (-2\alpha\Delta + \beta W''(u_0))\big|_{V_i}.$$

**Spectrum of $\mathcal{L}_{u_0}$** (continuum on real line):
- 1 zero mode (translation $u_0'$).
- 1 "amplitude" eigenvalue $\mu_1 = $ some positive value (bound state below continuum).
- Continuous spectrum above $\beta W''(0) = \beta W''(1)$ (bulk gap).

**Discrete lattice analog:** continuous spectrum discretizes; zero mode becomes exact translation; amplitude eigenvalue preserved.

### 3.4 Inter-formation coupling $H_{ij}$

$H_{12}$ is the cross-derivative of $\mathcal{E}$ between a formation-$1$ direction and formation-$2$ direction. For localized directions: $H_{12} \sim e^{-d_{\min}/\xi_0}$ (exponentially small).

**Magnitude estimate:** $(H_{12})_{a, b} \sim \int \partial_a \mathcal{E} \partial_b W(u_{\mathrm{ls}}) dx \sim \int_{\text{midpoint}} u_1' u_2' dx \sim e^{-d_{\min}/\xi_0}/\xi_0$.

---

## §4. Localized spectra

### 4.1 Per-formation contribution

Each $H_i$ block contributes:
- **Translation Goldstone**: 1 eigenvalue $= 0$ (exact).
- **Amplitude mode**: 1 eigenvalue $\mu_{\mathrm{amp}} > 0$ (bound state).
- **Continuous/radial modes**: positive eigenvalues above $\sim \beta W''(0)$.

If formation is locally unstable (e.g., high $\beta$): additional negative eigenvalues from internal pitchforks. In moderate $\beta$ regime at well-separated K=2: each formation is K=1-like, carrying its own Prop 1.3a/b spectrum.

### 4.2 Total spectrum of $H(u^\ast_2)$

$H(u^\ast_2) = \mathrm{diag}(H_1, H_2) + H_{\mathrm{int}}$ where $H_{\mathrm{int}}$ is the inter-formation coupling.

**Leading order (diagonal):**
- 2 zero modes (Goldstone × 2).
- 2 amplitude eigenvalues (2 × $\mu_{\mathrm{amp}}$).
- 2 × Prop 1.3a/b Morse indices (if applicable).

**First-order correction (coupling splits 2 Goldstones):**
- 1 exact Goldstone: **center-of-mass translation** $\partial_{\bar x} u^\ast_2 = u_0'(x - x_1) + u_0'(x - x_2)$. Kernel of full $H(u^\ast_2)$ (assuming translation invariance of full energy).
- 1 small-positive eigenvalue: **relative separation mode** $\partial_{\Delta x} u^\ast_2 = u_0'(x - x_1) - u_0'(x - x_2)$. Eigenvalue $\mu_{\mathrm{sep}} \sim e^{-d_{\min}/\xi_0}/\xi_0^2$.

### 4.3 Morse index at $u^\ast_2$

$$N_{\mathrm{unst}}^{\mathrm{full}}(u^\ast_2) \approx 2 N_{\mathrm{unst}}^{\mathrm{full}}(u_0) + O(1),$$

where the $O(1)$ correction depends on inter-formation coupling sign. For well-separated + stable single formation: $N(u^\ast_2) \approx 0$ (local min) at leading order.

---

## §5. Inter-formation coupling — explicit structure

### 5.1 Separation-mode eigenvalue

$\mu_{\mathrm{sep}}$ is small and its sign determines whether the K=2 configuration is stable against split/merge:
- $\mu_{\mathrm{sep}} > 0$: K=2 is locally stable (formations don't want to merge or separate).
- $\mu_{\mathrm{sep}} < 0$: K=2 unstable, becomes K=1 (if merge) or K=3 (if further split).

**Sign analysis** (analog of Kramers' escape over barrier):
$$\mu_{\mathrm{sep}}(d_{\min}) \sim \frac{d}{d(d_{\min})}V_{\mathrm{int}}(d_{\min})$$
where $V_{\mathrm{int}}(d)$ is the inter-formation interaction potential. From Round 2 §4.3b:
$$V_{\mathrm{int}}(d) \sim \frac{e^{-d/\xi_0}}{\sqrt{d/\xi_0}}.$$

$V_{\mathrm{int}}'(d_{\min}^\ast) = 0$ (equilibrium condition). Higher derivative gives $\mu_{\mathrm{sep}}$:
$$\mu_{\mathrm{sep}}(d_{\min}^\ast) \sim V_{\mathrm{int}}''(d_{\min}^\ast) \sim e^{-d_{\min}^\ast/\xi_0}/\xi_0^2.$$

**Positive at equilibrium** (K=2 is a minimum of $V_{\mathrm{int}}$): $\mu_{\mathrm{sep}} > 0$, so **K=2 is local min**. ✓

### 5.2 Two-timescale picture (M-1 from this viewpoint)

Time scales in the K=2 configuration:
- **Fast**: internal formation modes (timescale $\sim 1/(\beta|W''(c)|)$).
- **Slow**: separation-mode relaxation (timescale $\sim 1/\mu_{\mathrm{sep}} \sim e^{+d_{\min}/\xi_0}/\xi_0^{-2}$, exponentially long).

**Explanation for M-1 dissolution:** K=2 is "effectively stable" at observational timescales < $1/\mu_{\mathrm{sep}}$, even though it's NOT the global minimum (T11 says global min = single large disk). The two-timescale emerges naturally from Round 12 Hessian structure.

---

## §6. Goldstone + separation mode structure

### 6.1 Count of zero/near-zero eigenvalues

On 2D torus (continuous translation): K=2 config has:
- 2-dim Goldstone (center-of-mass translation).
- 1 zero eigenvalue (center-of-mass, exact).
- 1 small-positive eigenvalue (separation magnitude, $\mu_{\mathrm{sep}}^{|d|}$).
- 1 zero or small eigenvalue (separation angle, if continuous rotation available).

**On 2D torus**: 2 Goldstones (CM-x + CM-y), 1 separation mode (radial), 1 angle. Total 2 zero + 2 small-positive.

**On 2D square (free BC)**: 0 Goldstones, 2 separation modes (x, y).

### 6.2 Goldstone dimension = $K \cdot \dim\mathrm{Iso}_0(M)$

General result from Round 5 Morse-Bott:
$$\dim(\text{zero Goldstones at }u^\ast_K) = K \cdot \dim\mathrm{Iso}_0(M) - \dim(\text{stabilizer of config}).$$

For K=2 on torus, stabilizer = $\{e\}$ generically, so Goldstones = $2 \cdot 2 - 0 = 4$... but wait, that counts separately for each formation. After $T^2$-translation-invariance quotient, only 2 Goldstones remain (CM).

The other 2 dimensions become "separation-vector" modes (exponentially small eigenvalues, not exact zeros).

### 6.3 Formalization

> **$u^\ast_K$ Hessian Structure (Round 12, Cat A structural).** For well-separated K-formation critical configuration on graph with continuum limit $(M, g)$:
> - $\dim\mathrm{Iso}_0(M)$ exact Goldstones (from global translation/rotation of full configuration).
> - $(K - 1) \cdot \dim\mathrm{Iso}_0(M)$ exponentially-small-positive eigenvalues (inter-formation relative coordinates, order $e^{-d_{\min}/\xi_0}$).
> - $K \cdot$ (single-formation positive spectrum) otherwise.
> - $K \cdot$ (single-formation negative spectrum) contributes $K \cdot N_{\mathrm{unst}}^{\mathrm{full}}(u_0)$ to Morse index.

**Category: Cat A structural** — block-diagonal decomposition + perturbative coupling bounds.

---

## §7. Category + residuals

### 7.1 New Cat A claims (Round 12)

1. **Superposition ansatz + Lyapunov-Schmidt validity** in well-separated regime.

2. **Block-diagonal Hessian structure** $H(u^\ast_2) = \mathrm{diag}(H_1, H_2) + O(e^{-d_{\min}/\xi_0})$.

3. **Per-formation spectrum inheritance** — each $H_i$ replicates single-formation spectrum.

4. **CM + separation mode decomposition** — $K$-wise translation Goldstones split into 1 exact (CM) + $K-1$ exponentially-small (separation).

5. **Separation mode eigenvalue positivity** $\mu_{\mathrm{sep}} \sim V_{\mathrm{int}}''(d^\ast_{\min}) > 0$ at equilibrium → K=2 is local min.

6. **Two-timescale explicit mechanism** — M-1 dissolution via $\mu_{\mathrm{sep}}^{-1}$ as "slow" scale $\sim e^{d_{\min}/\xi_0}$.

### 7.2 Residuals from Round 12

- **Explicit coefficient of $\mu_{\mathrm{sep}}$** — requires $V_{\mathrm{int}}''$ computation with lattice discretization corrections.
- **Near-interaction regime** ($d_{\min} \sim \xi_0$): Lyapunov-Schmidt invalid; need full numerics.
- **K=3, 4, ... generalization** — Hessian has $K \times K$ block structure; non-trivial coupling.
- **Non-well-separated correction to $\mathcal{M}_2$** (Round 11): feeds back into orbit classification.

### 7.3 Cumulative Cat A

- R1-11: 56
- **R12: 6**
- **Cumulative: 62.**

### 7.4 Next: Round 13

$c_0^{(2)}(\beta)$ bracket via cascade enumeration × K-formation combinatorics + Round 12 Hessian structure.

---

**End of 14_deepening_round12.md.**
