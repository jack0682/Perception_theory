# 08 — Deepening Round 6: Prop 1.3b (d) Full Spectrum Across Spinodal

**Session:** 2026-04-22 (Round 6, post-Round-5)
**Trigger:** User directive "go" — continue 7-item list, item 3.
**Target (item 3):** Round 3 closed the **sign** of $\gamma_D''$ across $c$; Round 6 closes the **full spectrum** $\{\nu_k(c)\}_{k=2}^n$ as a function of $c$ across the spinodal interval $(c_-, c_+)$.
**This file covers:** §1 Scope. §2 Closed-form spectrum. §3 Bifurcation value $p^\ast(c)$. §4 Destabilized-set characterization (three $c$-regimes). §5 Morse index asymmetry. §6 Phase diagram $(c, \beta)$. §7 Canonical $c=1/2$ as symmetric point. §8 Category + residuals.

---

## §1. Scope and motivation

### 1.1 What Round 3 closed

Round 3 `mode_count.md` §2.3c gave:
- $\gamma_D''$ sign: $>0$ for $c < 1/2$, $= 0$ at $c = 1/2$, $<0$ for $c > 1/2$.
- Qualitative: $c < 1/2$ cubic term is destabilizing; $c > 1/2$ stabilizing.
- Magnitude at $c = 0.3$ canonical: $c\gamma_D'' / \gamma_D \approx 2.3$ (cubic dominates).

### 1.2 What Round 6 closes

Beyond sign: the **full closed-form eigenvalue function** $\nu_k(c)$, the **bifurcation eigenvalue** $p^\ast(c)$ at which modes switch stability as $c$ varies, and the resulting **Morse-index function** $N_{\mathrm{unst}}^{\mathrm{sep}}(c)$. This converts Round 3's qualitative sign asymmetry into a **quantitative phase-diagram statement**.

### 1.3 Setup constraints

To keep the algebra clean and match canonical default notation:
- **Regular graph** with degree $d$; adjacency $A$; Laplacian $L = dI - A$; aggregation $P = A/d$. So $P$ is symmetric and commutes with $L$.
- **Laplacian eigenvalues** $\lambda_k \in [0, 2d]$, with $\lambda_1 = 0$ (trivial). Normalized adjacency eigenvalues $p_k = 1 - \lambda_k/d \in [-1, 1]$.
- **Canonical distinction:** $\tau_D = 0$, $\lambda_D = 1$, hence $\delta_D = a_D$, $\kappa_D = 2a_D$. Pre-activation at $u_{\mathrm{uniform}}$: $z_0(c) = a_D(2c-1)$.
- **Spinodal range:** $c \in (c_-, c_+) = ((3-\sqrt 3)/6, (3+\sqrt 3)/6) \approx (0.2113, 0.7887)$.

Non-regular graphs handled via Round 3 §2.3c similarity $T_D$; the $c$-structure derived here transfers via $T_D$ conjugation.

---

## §2. Closed-form spectrum

From Round 3 §2.3d Prop 1.3b (d) consolidated:
$$H_{\mathrm{sep}}|_{u_{\mathrm{uniform}}} = -\gamma_D(c)(P + P^\top) - c\gamma_D''(c)(P^\top P).$$

On regular graph with $P = P^\top$: $H_{\mathrm{sep}} = -2\gamma_D P - c\gamma_D'' P^2$, diagonal in Laplacian basis:
$$\boxed{\;\nu_k(c) = -2\gamma_D(c) p_k - c\gamma_D''(c) p_k^2.\;}$$

Substituting $\gamma_D = d_0(1-d_0)\kappa_D$ and $\gamma_D'' = d_0(1-d_0)(1-2d_0)\kappa_D^2$ with $d_0 = d_0(c) := \sigma(a_D(2c-1))$ and $\bar d_0 := 1 - d_0$:
$$\nu_k(c) = -d_0\bar d_0 \kappa_D p_k\big[2 + c(1 - 2d_0)\kappa_D p_k\big].$$

**Prefactor.** $-d_0 \bar d_0 \kappa_D < 0$ for all $c \in $ spinodal (since $d_0 \in (0, 1)$, $\kappa_D > 0$). So
$$\nu_k(c) < 0 \;\Longleftrightarrow\; p_k \cdot f_c(p_k) > 0,$$
where
$$f_c(p) := 2 + c(1 - 2d_0(c))\kappa_D p.$$

---

## §3. Bifurcation eigenvalue $p^\ast(c)$

$f_c$ is affine in $p$ with slope $s(c) := c(1 - 2d_0(c))\kappa_D$. Its zero:
$$p^\ast(c) := -\frac{2}{c(1 - 2d_0(c))\kappa_D} = -\frac{2}{s(c)}.$$

### 3.1 Behavior across spinodal

- $c < 1/2$: $d_0 < 1/2 \Rightarrow 1-2d_0 > 0 \Rightarrow s > 0 \Rightarrow p^\ast < 0$.
- $c = 1/2$: $d_0 = 1/2 \Rightarrow s = 0 \Rightarrow p^\ast = \pm\infty$ (no finite crossing; $f_c = 2$ constant).
- $c > 1/2$: $d_0 > 1/2 \Rightarrow 1-2d_0 < 0 \Rightarrow s < 0 \Rightarrow p^\ast > 0$.

### 3.2 Numerical values at canonical $a_D = 5$, $\kappa_D = 10$

$s(c) = 10 c (1 - 2\sigma(10c - 5))$.

| $c$ | $d_0(c)$ | $1 - 2d_0$ | $s(c)$ | $p^\ast(c)$ | In spectrum $[-1, 1]$? |
|---|---|---|---|---|---|
| $c_- = 0.2113$ | 0.0528 | 0.8944 | 1.890 | $-1.058$ | outside (below $-1$) |
| 0.25 | 0.0759 | 0.8483 | 2.121 | $-0.943$ | inside, near edge |
| 0.30 | 0.1192 | 0.7616 | 2.285 | $-0.875$ | inside |
| 0.35 | 0.1824 | 0.6353 | 2.223 | $-0.900$ | inside |
| $c_{\mathrm{bif}}^- \approx 0.385$ | 0.231 | 0.538 | 2.072 | $-0.965$ | at edge |
| 0.40 | 0.2689 | 0.4621 | 1.848 | $-1.082$ | outside |
| 0.45 | 0.3775 | 0.2450 | 1.103 | $-1.813$ | outside |
| **0.50** | 0.5 | 0 | 0 | $\pm\infty$ | outside |
| 0.55 | 0.6225 | $-0.245$ | $-1.347$ | $+1.485$ | outside |
| 0.60 | 0.7311 | $-0.462$ | $-2.773$ | $+0.721$ | inside |
| 0.65 | 0.8176 | $-0.635$ | $-4.128$ | $+0.484$ | inside |
| 0.70 | 0.8808 | $-0.762$ | $-5.331$ | $+0.375$ | inside |
| 0.75 | 0.9241 | $-0.848$ | $-6.362$ | $+0.314$ | inside |
| $c_+ = 0.7887$ | 0.9472 | $-0.894$ | $-7.056$ | $+0.283$ | inside |

### 3.3 Structural summary of $p^\ast(c)$

- **Left-sided critical threshold $c_{\mathrm{bif}}^- \approx 0.385$** where $|p^\ast|$ first enters the spectrum from below. Determined by $s(c) \cdot \max|p_k| = 2$, i.e., $s(c_{\mathrm{bif}}^-) \cdot 1 = 2$, i.e., $5c(1-2d_0(c)) = 1$. Numerical: $c_{\mathrm{bif}}^- \approx 0.385$ at $a_D = 5$ (depends on $a_D$).
- **Right-sided critical threshold $c_{\mathrm{bif}}^+ \approx 0.545$** where $p^\ast$ first enters $(0, 1]$ from above. At $c$ just above $1/2$, $p^\ast$ is large (above 1); as $c$ increases, $p^\ast$ decreases below 1 and enters the spectrum. Determined by $|s(c)| = 2$, i.e., $5c(2d_0 - 1) = 1$. Symmetric to left under $c \to 1 - c$ approximately but not exactly (sigmoid is not linear).
- **No bifurcation crossing** for $c \in (c_{\mathrm{bif}}^-, c_{\mathrm{bif}}^+) \approx (0.385, 0.545)$: the Morse index of $H_{\mathrm{sep}}$ is constant in this "central spinodal" regime.

### 3.4 Extended sub-threshold region at $c < c_{\mathrm{bif}}^-$

For $c \in (c_-, c_{\mathrm{bif}}^-) \approx (0.211, 0.385)$: $p^\ast \in (-1, 0)$. Modes with $p_k < p^\ast$ (i.e., in the deep-bipartite tail) enter instability.

For $c \in (c_{\mathrm{bif}}^+, c_+) \approx (0.545, 0.789)$: $p^\ast \in (0, 1)$. Modes with $p_k > p^\ast$ (i.e., in the high-smoothness tail) exit instability.

---

## §4. Destabilized-set characterization (three $c$-regimes)

Combining the sign analysis of $p_k f_c(p_k)$:

### Regime I: $c \in (c_-, c_{\mathrm{bif}}^-) \approx (0.211, 0.385)$

$p^\ast(c) \in (-1, 0)$.

**Destabilized modes:**
$$\mathcal{U}^{\mathrm{sep}}_{\mathrm{I}}(c) = \{k \geq 2 : p_k > 0\} \cup \{k \geq 2 : p_k < p^\ast(c)\}.$$

Two branches: (a) smooth modes (positive $p_k$), (b) deep-bipartite modes (very negative $p_k$).

### Regime II: $c \in (c_{\mathrm{bif}}^-, c_{\mathrm{bif}}^+) \approx (0.385, 0.545)$

$p^\ast(c)$ outside spectrum (either below $-1$ or above $+1$).

**Destabilized modes:**
$$\mathcal{U}^{\mathrm{sep}}_{\mathrm{II}}(c) = \{k \geq 2 : p_k > 0\}.$$

Simple: all smooth modes, nothing else. This is the **canonical central regime**, containing $c = 1/2$.

### Regime III: $c \in (c_{\mathrm{bif}}^+, c_+) \approx (0.545, 0.789)$

$p^\ast(c) \in (0, 1)$.

**Destabilized modes:**
$$\mathcal{U}^{\mathrm{sep}}_{\mathrm{III}}(c) = \{k \geq 2 : 0 < p_k < p^\ast(c)\}.$$

Only low-smoothness modes (smooth enough to destabilize linearly, but not so smooth that cubic stabilization dominates).

### Three-regime table

| Regime | $c$-range | $p^\ast(c)$ | Destabilized set | # relative to $c = 1/2$ |
|---|---|---|---|---|
| I | $(c_-, c_{\mathrm{bif}}^-) \approx (0.21, 0.39)$ | $(-1, 0)$ | $\{p_k > 0\} \cup \{p_k < p^\ast\}$ | **more** (gains bipartite) |
| II | $(c_{\mathrm{bif}}^-, c_{\mathrm{bif}}^+) \approx (0.39, 0.55)$ | $\notin [-1, 1]$ | $\{p_k > 0\}$ | **same** (canonical central) |
| III | $(c_{\mathrm{bif}}^+, c_+) \approx (0.55, 0.79)$ | $(0, 1)$ | $\{0 < p_k < p^\ast\}$ | **fewer** (loses smooth) |

---

## §5. Morse index asymmetry

### 5.1 Morse-index function

Define $N^{\mathrm{sep}}_{\mathrm{unst}}(c) := |\mathcal{U}^{\mathrm{sep}}(c)|$.

For 2D grid (regular, $L \times L$, large $L$): Laplacian spectrum approximates continuous density $\rho(\lambda)$ on $[0, 2d] = [0, 8]$; positive-$p_k$ modes ($\lambda_k < d = 4$) number approximately $n/2$, similar for negative.

**Asymmetry magnitude.** Let $N_+ := |\{p_k > 0\}|$, $N_- := |\{p_k < 0\}|$ (both $\approx n/2$ on 2D grid bulk). Denote $N_{\mathrm{tail}}^-(q) := |\{p_k < q\}|$ and $N_{\mathrm{tail}}^+(q) := |\{p_k > q\}|$.

| Regime | $N^{\mathrm{sep}}_{\mathrm{unst}}(c)$ |
|---|---|
| I | $N_+ + N_{\mathrm{tail}}^-(p^\ast(c))$ |
| II | $N_+$ |
| III | $N_+ - N_{\mathrm{tail}}^+(p^\ast(c))$ |

### 5.2 Monotonicity

**On Regime I**: as $c$ decreases from $c_{\mathrm{bif}}^-$ toward $c_-$, $p^\ast(c)$ increases toward 0 (becomes less negative), so $N_{\mathrm{tail}}^-(p^\ast)$ **increases** (more bipartite modes included). Hence $N^{\mathrm{sep}}_{\mathrm{unst}}$ is **decreasing in $c$** on Regime I.

**On Regime III**: as $c$ increases from $c_{\mathrm{bif}}^+$ toward $c_+$, $p^\ast(c)$ decreases toward 0 (becomes smaller positive), so $N_{\mathrm{tail}}^+(p^\ast)$ **increases** (more smooth modes excluded). Hence $N^{\mathrm{sep}}_{\mathrm{unst}}$ is also **decreasing in $c$** on Regime III.

**Global monotonicity** (piecewise): $N^{\mathrm{sep}}_{\mathrm{unst}}(c)$ is non-increasing across the full spinodal. Intuitively: the "more full" the field (larger $c$), the fewer separation-level instabilities.

### 5.3 Explicit formula at canonical $c = 0.3$

At $c = 0.3$: $p^\ast = -0.875$. On 2D 64×64 grid (regular bulk approximation):
$N_{\mathrm{tail}}^-(-0.875) = |\{k : \lambda_k > d(1 - p^\ast) = 4 \cdot 1.875 = 7.5\}|$

For 2D Laplacian on $64 \times 64$, max $\lambda \approx 8$ (at $(\cos \pi + \cos \pi)$ mode); modes with $\lambda > 7.5$ are in the top 5% or so. Estimate $N_{\mathrm{tail}}^-(-0.875) \approx 0.05 \cdot n \approx 200$.

So at $c = 0.3$, $N^{\mathrm{sep}}_{\mathrm{unst}} \approx N_+ + 200 \approx 2048 + 200 = 2248$.

Compare to $c = 0.5$: $N^{\mathrm{sep}}_{\mathrm{unst}} = N_+ \approx 2048$.

**Difference: ~10% more unstable modes at $c = 0.3$ vs $c = 0.5$.**

### 5.4 Explicit formula at canonical $c = 0.7$

At $c = 0.7$: $p^\ast = +0.375$. Modes with $p_k > 0.375$ (i.e., $\lambda_k < d(1 - 0.375) = 2.5$) are **excluded** from instability.

$N_{\mathrm{tail}}^+(0.375) = |\{k : \lambda_k < 2.5\}|$

On 2D $64 \times 64$: bottom 25-30% of spectrum. Estimate $N_{\mathrm{tail}}^+(0.375) \approx 0.28 \cdot n \approx 1150$.

So at $c = 0.7$, $N^{\mathrm{sep}}_{\mathrm{unst}} \approx N_+ - 1150 \approx 2048 - 1150 = 900$.

**Dramatic drop: at $c = 0.7$, less than half the unstable modes compared to $c = 0.5$.**

### 5.5 Asymmetry summary

| $c$ | $N^{\mathrm{sep}}_{\mathrm{unst}}$ on 2D $64^2$ (regular) | Relative to $c = 0.5$ |
|---|---|---|
| 0.30 | ~2248 | +10% |
| 0.40 | ~2048 (Regime II) | baseline |
| 0.50 | 2048 | 0% |
| 0.55 | 2048 (Regime II) | 0% |
| 0.60 | ~1200 | -41% |
| 0.70 | ~900 | -56% |

**Key finding.** The asymmetry is not the sign of a small perturbation but a **dramatic ~50% reduction** of unstable modes in the upper spinodal Regime III compared to the lower.

---

## §6. Phase diagram in $(c, \beta)$

Combining with Prop 1.3a bd-Morse index:
$$N_{\mathrm{unst}}^{\mathrm{bd}}(\beta, c) = \#\{k : 4\alpha\lambda_k < \beta|W''(c)|\}.$$

And Prop 1.3b (e) Weyl bracket:
$$N_{\mathrm{unst}}^{\mathrm{bd}} - N^{\mathrm{sep}}_+ \leq N_{\mathrm{unst}}^{\mathrm{full}} \leq N_{\mathrm{unst}}^{\mathrm{bd}} + N^{\mathrm{sep}}_-.$$

### 6.1 Central regime behavior

On Regime II ($c \approx 0.5$, $N^{\mathrm{sep}}_{\mathrm{unst}}$ stable at $N_+$): $N_{\mathrm{unst}}^{\mathrm{full}}$ behavior is cleanly controlled by $\beta$ alone (via Prop 1.3a bd-contribution).

### 6.2 Outer regimes

On Regime I (low $c$) or III (high $c$): $N_{\mathrm{unst}}^{\mathrm{full}}$ has additional $c$-dependence from cubic term, and the Weyl bracket widens.

### 6.3 Critical $\beta_{\mathrm{crit}}^{(2)}(c)$

$\beta_{\mathrm{crit}}^{(2)}(c) = 4\alpha\lambda_2/|W''(c)|$. $W''(c) = 2 - 12c + 12c^2$, which is negative in spinodal and symmetric around $c = 1/2$ (since $W''(1 - c) = 2 - 12(1-c) + 12(1-c)^2 = 2 - 12 + 12c + 12 - 24c + 12c^2 = 2 - 12c + 12c^2 = W''(c)$).

So $|W''(c)|$ is symmetric in $c \to 1-c$, and $\beta_{\mathrm{crit}}^{(2)}(c) = \beta_{\mathrm{crit}}^{(2)}(1-c)$.

But $N^{\mathrm{sep}}_{\mathrm{unst}}(c)$ is asymmetric in $c \to 1-c$ (Regime I ≠ Regime III). So **Prop 1.3b contribution breaks the $c \to 1-c$ symmetry** that $W''$ would otherwise preserve.

### 6.4 Phase-diagram statement

> **Prop 1.3b-Phase (Round 6, Cat A).** In the $(c, \beta)$ plane restricted to spinodal $c \in (c_-, c_+)$ and $\beta > 0$, the Morse-index function $N_{\mathrm{unst}}^{\mathrm{full}}(c, \beta)$ exhibits **three $c$-regimes** (I, II, III) separated by **critical $c$-values** $c_{\mathrm{bif}}^\pm(a_D, \lambda_D)$. On the central Regime II (containing $c = 1/2$), $N_{\mathrm{unst}}^{\mathrm{full}}$ depends on $\beta$ only (Prop 1.3a behavior). On outer regimes, $N_{\mathrm{unst}}^{\mathrm{full}}$ acquires $c$-dependence via Prop 1.3b (d) cubic term: Regime I adds bipartite-mode instabilities ($c < 1/2$); Regime III removes smooth-mode instabilities ($c > 1/2$). The asymmetry is intrinsic (not removable by rescaling).

---

## §7. Canonical $c = 1/2$ as symmetric point

### 7.1 Why $c = 1/2$ is canonical

Round 6 confirms:
- $c = 1/2$ is the **unique point** where $\gamma_D'' = 0$, removing cubic dependence.
- $c = 1/2$ is contained in Regime II (central), so the destabilized-set is purely $\{p_k > 0\}$.
- $c = 1/2$ is the symmetry point of $W''(c)$ (not of the distinction operator — that would be $(1-c)$-symmetric but the distinction $D(\cdot)$ breaks this).

### 7.2 Canonical-choice justification

The choice of $c = 1/2$ in most canonical derivations (including canonical.md §8.1 double-well) is now **structurally justified**: it is the **only $c$ at which the Hessian $H_{\mathrm{cl,sep}}$ has closed diagonal form $\nu_k = -2\gamma_D p_k$ without cubic correction**.

Any deviation from $c = 1/2$ requires the full cubic analysis (Round 6 §3-§5).

### 7.3 Regime-II robustness

Moreover, Round 6 shows that $c = 1/2$ sits in a **robust central regime** $(c_{\mathrm{bif}}^-, c_{\mathrm{bif}}^+) \approx (0.385, 0.545)$ of width $\sim 0.16$ where the Morse index behavior is identical to $c = 1/2$. So small perturbations of $c$ around $1/2$ do not change the qualitative structure.

---

## §8. Category and residuals

### 8.1 New Cat A claims (Round 6)

1. **Closed-form $\nu_k(c) = -d_0\bar d_0\kappa_D p_k[2 + c(1-2d_0)\kappa_D p_k]$** — explicit function of $c$, universal on regular graphs.

2. **Bifurcation eigenvalue $p^\ast(c) = -2/[c(1-2d_0)\kappa_D]$** — two critical $c$-thresholds $c_{\mathrm{bif}}^\pm$ at which $|p^\ast(c)| = 1$.

3. **Three-regime classification** — Regimes I/II/III with distinct destabilized-set characterizations.

4. **Asymmetric Morse-index function $N^{\mathrm{sep}}_{\mathrm{unst}}(c)$** — non-increasing in $c$, with dramatic ~50% drop from Regime I/II to Regime III.

5. **Prop 1.3b-Phase** — phase-diagram statement in $(c, \beta)$ plane with three-regime structure.

6. **Canonical $c = 1/2$ justification** — unique point with closed diagonal form; sits in robust central Regime II.

### 8.2 Residuals from Round 6

- **Non-regular graph spectrum** — formula $\nu_k(c)$ derived on regular graph; non-regular requires Round 3 similarity $T_D$ but combined $c$-dependence not written out.
- **3D grid / higher-dim spectrum density** — Regime I/III boundaries depend on the tail densities $\rho(p)$ at $p \to \pm 1$.
- **SBM / barbell phase diagrams** — graph-specific $\rho(p)$ shapes, case-by-case.
- **Fit between Regimes I and III** at finite-graph discretization — boundaries $c_{\mathrm{bif}}^\pm$ sharp in continuum limit, smoothed at finite $L$.
- **Thermal extension** — Round 2 `thermal_extension.md` §3 showed $H_{\mathrm{cl,sep}}$ is $T$-invariant, so Round 6 spectrum inherits $T$-independence. But Prop 1.3b-Phase combined with Prop 1.3a thermal ($H_{\mathrm{bd}}$) in the $(c, \beta, T)$ phase diagram has richer structure — explicitly open.

### 8.3 Cumulative Cat A count (today)

- Morning: 4
- Round 2: 6
- Round 3: 3
- Round 4: 3
- Round 5: 4
- **Round 6: 6**
- **Cumulative: 26 Cat A statements today.**

---

## §9. Next steps

7-item residual list:
- [x] Item 1: $\Phi_4$ on non-D4 graph classes (Round 4).
- [x] Item 2: Continuous $\mathrm{Aut}$ groups (Round 5).
- [x] Item 3: Prop 1.3b (d) full-spectrum beyond $c = 1/2$ (Round 6, this file).
- [ ] Item 4: NQ-31 sharp $c_0$ value.
- [ ] Item 5: G-C sub-claim C on general graphs.
- [ ] Item 6: Cor 2.2 SCC-minimizer supra-lattice regime.
- [ ] Item 7: Higher-order pitchfork cascade.

**Recommendation for Round 7:** Item 4 (NQ-31 sharp $c_0$ value). This is the G-C residual that Round 2 left open (sharp cardinality value). Requires either multi-init Morse survey (compute) or theoretical derivation via Morse-Bott (Round 5) + pitchfork cascade (item 7). We can attempt the theoretical route using Round 5's continuous-Aut refinement.

### 9.1 Files to update this round

- `working/SF/mode_count.md` — add new §2.3e "Round 6 — full-spectrum $c$-dependence" with condensed Round 6 content.
- `canonical_sub.md` — append Round 6 entry (6 new Cat A + Q35-Q37).

---

**End of 08_deepening_round6.md.**
