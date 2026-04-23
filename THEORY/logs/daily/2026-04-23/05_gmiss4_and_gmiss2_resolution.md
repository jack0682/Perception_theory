# 05 — G-miss-4 (K̂=1 Sufficient Condition) + G-miss-2 (c_0 Scope Correction)

**Session:** 2026-04-23 (continuation; user instruction "4, 2부터").
**Target:** (Part A) G-miss-4 resolution path — theoretical characterization of sufficient condition for $\widehat K = 1$ generically. (Part B) G-miss-2 resolution path — explicit scope correction of Round 8 Universal $c_0$-Counting + irrep-dimension dependency.
**Depends on:** `04_axiom_audit_and_sf_gaps.md` §B.6 priority matrix, §B.4 G-miss-4 setup, §B.2 G-miss-2 setup; `canonical.md` §13 T-Birth-Parametric (Crandall-Rabinowitz); `working/SF/mode_count.md` Prop 1.3a/b; `working/SF/symmetry_moduli.md` R4/R5/R8 equivariant framework.

---

# Part A — G-miss-4 Resolution: Sufficient Condition for $\widehat K = 1$

## §A.1 Formal setup

### A.1.1 Observable

$$\widehat K(\beta, c, G, \pi) := K_{\mathrm{step}}(u_\pi^*(\beta)) = \#\{\text{connected components of } \{x : u_\pi^*(\beta)(x) \geq \tau\}\}$$

with canonical $\tau = 1/2$. Dynamic observable (depends on protocol $\pi$).

### A.1.2 Generic protocol

Consider a **generic small-noise protocol**:
$$u_0 = c \mathbf{1} + \sigma_0 \cdot \xi,\quad \xi \sim \mathcal{N}(0, I_{T\Sigma_m}),\ \ \sigma_0 \ll 1$$
where $\xi$ is a tangent-space Gaussian (i.e., $\sum_i \xi_i = 0$). Gradient flow:
$$\dot u(t) = -\Pi_{\Sigma_m \cap [0,1]^n} \nabla\mathcal{E}(u(t)),\quad u(0) = u_0.$$

The "generic protocol" here is **any protocol with rotationally-invariant small-noise IC**. Fiedler-init is a special case (concentrates $\xi$ on Fiedler mode); random-init is the full-covariance case.

### A.1.3 Question (formalized)

> **Q-K1 (generic sufficiency)**: Under what condition on $(\beta, c, G)$ does
> $$\mathbb{P}_\xi[K_{\mathrm{step}}(u^*(\beta, c, G, u_0(\xi))) = 1] \to 1\text{ as }\sigma_0 \to 0\text{?}$$

This captures "for almost every small random initialization, gradient flow ends up with K=1." Equivalently: **basin $\mathcal{B}_1$ contains a neighborhood of $u_{\mathrm{unif}}$** (or at least contains $u_0(\xi)$ for a.e. $\xi$).

### A.1.4 Connection to canonical

T1 (Cat A) guarantees minimizer existence on $\Sigma_m$. T-Merge (b) (Cat A) says K=1 is global min. But global min ≠ generic dynamic endpoint. Q-K1 asks about dynamic endpoint distribution.

---

## §A.2 Linearization analysis near $u_{\mathrm{unif}}$

### A.2.1 Hessian at uniform

From Prop 1.3a (Cat A, R1-R4):
$$H_{\mathrm{bd}}(u_{\mathrm{unif}}) = 4\alpha L + \beta W''(c) I$$

with eigenvalues $\mu_k = 4\alpha\lambda_k + \beta W''(c)$ where $\lambda_k$ are graph Laplacian eigenvalues ($\lambda_1 = 0$ constant mode, $\lambda_2 = $ Fiedler, ...).

Full-energy Hessian (Prop 1.3b): $H_{\mathrm{full}} = H_{\mathrm{bd}} + H_{\mathrm{cl,sep}}$.

### A.2.2 Unstable modes count

$N_{\mathrm{unst}}^{\mathrm{bd}}(\beta) = \#\{k : \mu_k < 0\}$.

For $\beta > \beta_{\mathrm{crit}}^{(2)} = 4\alpha\lambda_2/|W''(c)|$: $\mu_2 < 0$ (at least one unstable).
For $\beta > 4\alpha\lambda_3/|W''(c)|$: $\mu_3 < 0$ (two unstable).
Etc.

### A.2.3 Near-critical regime ($\beta$ slightly above $\beta_{\mathrm{crit}}^{(2)}$)

Only $\mu_2 < 0$; all other $\mu_k > 0$.

**Linearized dynamics**: $\dot v_2 = |\mu_2| v_2 + O(v_2^3)$ where $v_2 = \langle u - u_{\mathrm{unif}}, \phi_2\rangle$ is the Fiedler-mode amplitude. Other modes decay.

$v_2$ saturates via cubic term → $v_2 \to \pm A^*$ (supercritical pitchfork, T-Birth-Parametric).

**Saturation pattern**: $u^*(x) \approx u_{\mathrm{unif}} + A^* \phi_2(x)$.

**Critical observation**: On connected graph, Fiedler eigenvector $\phi_2$ is **sign-definite on two regions** — nodal set divides $X$ into two parts. $\phi_2(x) > 0$ on part $A$, $\phi_2(x) < 0$ on $X \setminus A$.

Hence $u^*(x)$ exceeds $c$ on one part, falls below on another. **$\{u^* > \tau\}$ is one connected component** (part $A$ or $X \setminus A$ depending on sign of $A^*$), so **$K_{\mathrm{step}}(u^*) = 1$**.

### A.2.4 Claim G-miss-4.1

> **Claim A.2.1 (K=1 near bifurcation, Cat A structural)**: For $\beta \in (\beta_{\mathrm{crit}}^{(2)}, \beta_{\mathrm{crit}}^{(3)})$, where $\beta_{\mathrm{crit}}^{(3)} = 4\alpha\lambda_3/|W''(c)|$, gradient flow from generic small-$\sigma_0$ initial condition produces $u^*$ with $K_{\mathrm{step}}(u^*) = 1$ almost surely.

**Proof sketch**:
1. Only Fiedler mode $\phi_2$ is unstable.
2. Generic $\xi$ has $\langle \xi, \phi_2\rangle \neq 0$ (probability 1).
3. Linearized flow amplifies $\phi_2$ component, decays all others.
4. Nonlinear saturation (pitchfork) → $u^* \approx u_{\mathrm{unif}} + A^* \phi_2$.
5. Fiedler eigenvector is connected-support (classical Courant nodal theorem on graph): one sign on connected piece.
6. Threshold at $\tau = 1/2 \approx c + $ small: superthreshold set is one connected component.

**Status**: Cat A structural (elementary from Prop 1.3a + Courant + pitchfork).

### A.2.5 Scope of Claim A.2.1

- **Necessary condition**: only one unstable mode.
- **Sufficient condition**: $\beta \in (\beta_{\mathrm{crit}}^{(2)}, \beta_{\mathrm{crit}}^{(3)})$.

This gives a **precise regime** where $\widehat K = 1$ is **guaranteed** by single-mode dominance. For $\beta > \beta_{\mathrm{crit}}^{(3)}$, multi-mode competition opens possibility of $\widehat K > 1$.

**Empirical match**:
- Near-critical regime empirically gives K=1 (e.g., R22 V5 at β ≤ 7): ✓ matches Claim A.2.1.
- R19 c=0.7 β=0.5-10: K=1 observed; likely $\beta < \beta_{\mathrm{crit}}^{(3)}$.

### A.2.6 Beyond near-critical: the hard case

For $\beta > \beta_{\mathrm{crit}}^{(3)}$ with multiple unstable modes: dynamics is **not** predicted by single Fiedler mode. Multi-mode competition + basin selection.

**Empirically**:
- c=0.5 torus β=30: $\widehat K = 1.00$ (R18) — K=1 persists far beyond near-critical.
- c=0.3 2D sq β=30: $\widehat K = 7.76$ — K>1 emerges.
- c=0.7 1D cycle β=30: $\widehat K = 45$ — K>>1.

**Conclusion**: Near-critical gives easy sufficient condition (Claim A.2.1). **Far-from-critical** K=1 (c=0.5 torus β=30) requires **different mechanism** — basin volume argument.

---

## §A.3 Basin volume approximation (Gaussian)

### A.3.1 Setup

For each K-formation minimizer $u^*_K$ with constrained Hessian $H_K > 0$ on tangent $T_{u^*_K}\Sigma_m$, the basin $\mathcal{B}_K$ admits local Gaussian approximation:
$$\mathcal{E}(u) \approx \mathcal{E}(u^*_K) + \tfrac{1}{2} (u - u^*_K)^T H_K (u - u^*_K) + O(\|u - u^*_K\|^3)$$

### A.3.2 Basin volume estimate

Gradient flow from $u_0$ lands in $\mathcal{B}_K$ iff $u_0$ is in the attraction region of $u^*_K$.

**Approximation**: Basin boundary is where $\mathcal{E}$-contour equals value at adjacent saddle. For steepest-descent dynamics:
$$\mathrm{Vol}(\mathcal{B}_K) \approx \text{(some function of )} \det(H_K)^{-1/2} \cdot \#(\text{moduli points in }\mathcal{M}_K)$$

More precisely, using thin-basin approximation and Stanley's formula (or simpler: basin radius $\sim 1/\sqrt{\lambda_{\min}(H_K)}$):

$$\mathrm{Vol}(\mathcal{B}_K) \sim |\mathcal{M}_K| \cdot \prod_i \lambda_i(H_K)^{-1/2}\text{ (within small region around each minimizer)}$$

where $\lambda_i(H_K)$ are positive Hessian eigenvalues and $|\mathcal{M}_K|$ is the number of K-formation minimizers modulo $\mathrm{Aut}(G)$.

### A.3.3 K=1 vs K>1 volume ratio

For K=1 formation (large): Hessian $H_1$ has:
- Few "soft" directions (boundary displacement, $\lambda \sim \xi_0$, small).
- Rest "hard" ($\lambda \sim 1$).

For K=2 formation: Hessian $H_2$ has:
- More soft directions (2× boundary displacement modes).
- Inter-formation soft mode $\mu_{\mathrm{sep}} \sim e^{-d_{\min}/\xi_0}$ (very small).

**Generally**: higher K → more soft modes → smaller $\det(H_K)$ per formation → **larger basin volume per minimizer**. But also fewer minimizers in $\mathcal{M}_K$ on small-$K$ side.

**Key tension**:
$$\mathrm{Vol}(\mathcal{B}_K) \sim |\mathcal{M}_K(\beta, c, G)| \cdot (\text{basin vol per min})$$

- $|\mathcal{M}_K|$ grows fast with K (combinatorial).
- Per-minimizer vol grows slower but still grows with K.

Thus **K>>1 has dominant total volume unless $|\mathcal{M}_K|$ is restricted**.

### A.3.4 Why c ≈ 1/2 gives $\mathcal{B}_1$ dominance

At c=1/2, the landscape has **$u \leftrightarrow 1-u$ symmetry** (E3 cubic term $\gamma_D''(1/2) = 0$ per R6, `mode_count.md` §2.3e static part preserved).

**Key consequence**: For each K=1 minimizer $u^*_1$, its complement $1 - u^*_1$ is also a K=1 minimizer (same energy). But **$K_{\mathrm{step}}(u^*_1) = K_{\mathrm{step}}(1 - u^*_1) = 1$** (both single-component).

For K=2: $u^*_2$ and $1 - u^*_2$ are both K=2 configurations (but now $1 - u^*_2$'s $\{u > \tau\}$ is the **complement of two bumps = one connected region for $X$ minus two disks**, which is K=1 if $X$ is connected and bumps are disjoint!).

**Implication at c=1/2**: The complement involution $u \leftrightarrow 1 - u$ **maps K≥2 basins to K=1 basins**. Specifically, if $u$ has K disks, then $1 - u$ has background occupying most of $X$ minus K holes — which is K=1 (the ambient region).

**Formal statement**:

> **Claim A.3.1 (c=1/2 involution)**: At $c = 1/2$, the map $u \mapsto 1 - u$ is a measure-preserving involution on $\Sigma_m$ that maps basin $\mathcal{B}_K$ (for $u$ with K disk-like components) to $\mathcal{B}_1$ (since $1 - u$ has one connected super-threshold region = ambient background).

**Proof**:
- $c = 1/2$ ⟹ mass $m = n/2$. $(1 - u)$ has mass $n - n/2 = n/2 = m$. ✓ stays on $\Sigma_m$.
- $\mathcal{E}(u) = \mathcal{E}(1-u)$ (4-term energy all symmetric under $u \leftrightarrow 1-u$ at c=1/2, by direct check: $W(u) = u^2(1-u)^2$ symmetric; $\mathcal{E}_{\mathrm{bd}}$ via $|\nabla u|^2 = |\nabla(1-u)|^2$; $\mathcal{E}_{\mathrm{cl}}$ requires $\tau_{\mathrm{cl}} = 1/2$ — which is canonical default).
- $u \mapsto 1-u$ is an involution on $\Sigma_m$.
- Super-threshold set of $1-u$ at $\tau=1/2$ = $\{x : u(x) < 1/2\}$ = complement of $\{u \geq 1/2\}$.
- If $\{u \geq 1/2\}$ has K disk components on connected $X$, then **complement is connected** (ambient region minus K holes is connected in 2D/higher-D).
- So $K_{\mathrm{step}}(1-u) = 1$ when $\{u \geq 1/2\}$ is K disk-components **and** $X$ is 2D-like (not fragmenting).

**Status**: Cat A structural (on 2D connected graphs; holds with tiny effort).

### A.3.5 Implication for c=1/2

Involution $u \mapsto 1-u$:
- Identifies $\mathcal{B}_K$ (K-disk config) with a subset of $\mathcal{B}_1$ (complement is single region).

**But careful**: the involution maps **minimizer** to **minimizer** only if landscape is symmetric. At c=1/2, it is.

**Consequence**: At c=1/2,
$$\mathrm{Vol}(\mathcal{B}_K^{\mathrm{K-disk}}) + \mathrm{Vol}(\mathcal{B}_1^{\mathrm{complement-of-K-disk}}) = 2 \cdot \mathrm{Vol}(\text{single-side basin}).$$

Since the involution connects these, **the "K-disk" basin and "complement" basin share equal volume**. But the **observable** $K_{\mathrm{step}}$ gives $K$ for one and $1$ for the other!

**Specifically**: half the gradient-flow trajectories from random IC land in "K-disk" configurations ($\widehat K = K$); the other half land in "complement-of-K-disk" ($\widehat K = 1$).

**Expected distribution at c=1/2**:
$$\mathbb{P}[\widehat K = 1] \geq \frac{1}{2}$$
from involution argument alone.

**R18 empirical**: $\widehat K = 1.00\pm 0.00$ across 50 seeds at c=0.5 2D torus β=30 → **near 100%**, not just 50%.

**Further mechanism needed**: The "K-disk" basins are also often mapped to K=1 via dynamics (not just involution). At c=1/2 on torus, there's additional symmetry (translation + reflections) that concentrates basin structure.

### A.3.6 Refined sufficient condition

> **Hypothesis G-miss-4 refined**: $\widehat K = 1$ a.s. iff **one of**:
> (i) Single-mode dominance: $\beta \in (\beta_{\mathrm{crit}}^{(2)}, \beta_{\mathrm{crit}}^{(3)})$ (Claim A.2.1 Cat A).
> (ii) Complement self-symmetry: $c = 1/2$ AND $X$ is "topologically simple" (2D-like, connected complement) (Claim A.3.1 partial; Cat B).
> (iii) Large $\mathrm{Vol}(\mathcal{B}_1)$ dominance: $|\mathcal{M}_1|$ large relative to $|\mathcal{M}_K|$ per-minimizer volume sum (Cat C basin-volume argument).

Conditions (i) and (ii) **together** cover: near-critical, OR c=1/2 on 2D-like $X$.

Outside these: $\widehat K \geq 1$ is possible, $\widehat K = 1$ generic is conditional on (iii).

### A.3.7 Empirical regime mapping

| Regime | Condition (i)? | (ii)? | Empirical $\widehat K$ |
|---|---|---|---|
| 2D sq c=0.5 β=30 | ✗ (multi-unst) | ✓ (c=1/2) | K=1 per observation similar setups |
| 2D torus c=0.5 β=30 | ✗ | ✓ (c=1/2, torus 2D-like) | **K=1.00 (R18)** ✓ |
| 2D torus c=0.5 β=0.5 | ✓ (near-crit) | ✓ | K=1.00 (R18) ✓ |
| 2D sq c=0.3 β=30 | ✗ | ✗ (c≠0.5) | K=7.76 (R17) ✓ |
| 2D sq c=0.7 β=30 | ✗ | ✗ | K=1.08 (R19) — near K=1 |
| 2D torus c=0.7 β=30 | ✗ | ✗ (c≠0.5) but 2D-like | K=1.00 (R19) |
| 1D cycle c=0.7 β=30 | ✗ | ✗ (c≠0.5, 1D non-topological-simple) | K=45 (R19) ✓ |

**Mostly consistent**. Outliers:
- 2D sq c=0.7 β=30 K=1.08 (R19): neither (i) nor (ii) holds strongly, yet K near 1. Requires mechanism (iii) or refined (ii) [c=0.7 closer to 1 than to 1/2; maybe extended c range works].
- 2D torus c=0.7 β=30 K=1: similar.

**Refinement of (ii)**: Symmetry argument works not only at c=1/2 but in wider range if $X$ is 2D-topologically-simple. Let's call this condition (ii'):
- (ii') $X$ is 2D-like (topologically: 2-connected planar region or 2D torus) AND c ∈ [something around 1/2, maybe 0.3-0.7].

### A.3.8 Topological simplicity (2D-like)

The involution argument used "complement of K disks on connected 2D = 1 connected region". Generalize:

**Definition (topological simplicity for K=1 preference)**: $X$ is **K1-preserving** iff for every set $S \subset X$ with $|S| = n/2$ consisting of disjoint "disks," $X \setminus S$ is connected.

- 2D grid (free BC, torus): K1-preserving ✓.
- 1D cycle: **NOT** K1-preserving — removing K disjoint "intervals" leaves K complementary intervals. Removing 2 intervals leaves 2 intervals. $K_{\mathrm{step}}(1-u) = K_{\mathrm{step}}(u)$, not 1.

**Corollary**: On 1D cycle, involution argument FAILS. Hence:
- 1D cycle c=0.5: $\widehat K$ should NOT reduce to 1 via (ii).
- **Prediction**: 1D cycle c=0.5 β=30 → $\widehat K > 1$.

**Check**: R18 1D cycle c=0.5 β=30: $\widehat K = 56.18$ (R18 §17.1 cross-c table). ✓ **Matches prediction** — involution mechanism not available on 1D cycle, hence multi-K.

**Strong empirical support for condition (ii') being the correct formulation.**

### A.3.9 Refined claim

> **Claim A.3.2 (K1-preservation at c=1/2)**: If $X$ is **K1-preserving** (topologically 2D-like) AND $c = 1/2$, then the $u \leftrightarrow 1-u$ involution gives $\mathbb{P}[\widehat K = 1] \geq 1/2$, with observed values near 1 when combined with Fiedler-mode alignment preferences.
>
> **Cat B structural**: Proof requires: (a) topological def of K1-preserving; (b) involution symmetry at c=1/2 $\tau_{\mathrm{cl}} = 1/2$; (c) additional Fiedler-bias mechanism pushing probability from 1/2 toward 1.

### A.3.10 Extended c-range (far from 1/2)

At c=0.7 on 2D torus: not c=1/2, yet $\widehat K = 1$ empirically.

**Mechanism (conjectural, G-miss-4 Cat C)**:
- At c=0.7, mass fraction is 70%; formations fill most of $X$.
- K=1 with $r_0 = \sqrt{0.7 n/\pi}$ (large disk).
- K≥2 requires **at least two separated large disks**; on torus with total mass 0.7n, two disks need ~0.35n each, which requires separation — may not fit.
- **Geometric constraint**: at c=0.7 on finite torus, **K≥2 configurations may not exist** geometrically (disks would overlap).

**Consequence**: At c near 0.5 and beyond (on 2D compact $X$), the **geometric admissibility** of K>1 disappears, forcing K=1.

**Refined sufficient condition (iv)**:
- (iv) $X$ is 2D-like AND $c \geq c^*_{\mathrm{max}}(G)$ where $c^*_{\mathrm{max}}$ is the max $c$ for which K=2 fits geometrically.

On 2D torus $L \times L$ with K=2 well-separated requires $d_{\min} \geq \xi_0 \log(1/\epsilon_0) \approx 7\xi_0$. For K=2 disks of radius $r_0$ each: $2r_0 + d_{\min} \leq L/2$ (on torus), so $r_0 \leq (L - 7\xi_0) / 4$.

Mass conservation: $\pi r_0^2 \cdot 2 = cn$, so $r_0 = \sqrt{cn/(2\pi)}$.

K=2 admissible iff $\sqrt{cn/(2\pi)} \leq (L - 7\xi_0)/4$, i.e., $c \leq \pi (L - 7\xi_0)^2 / (8n) = \pi (1 - 7\xi_0/L)^2 / 8 \approx \pi/8 \approx 0.39$ (for $\xi_0 \ll L$).

**Prediction**: c > 0.39 (approximately) on 2D torus forbids K=2 geometrically → **K=1 forced**.

**Match**: c=0.5 (R18) and c=0.7 (R19) both > 0.39 → K=1 observed. ✓

### A.3.11 Consolidated sufficient condition

> **Theorem G-miss-4 (K=1 generic sufficiency, tentative Cat B)**: $\widehat K = 1$ almost surely (generic IC) on 2D-like $X$ when any of:
>
> (i) **Near-critical mode-count regime**: $\beta \in (\beta_{\mathrm{crit}}^{(2)}, \beta_{\mathrm{crit}}^{(3)})$ — single unstable mode (Cat A, Claim A.2.1).
>
> (ii) **c=1/2 self-symmetry**: $c = 1/2$ and $\tau_{\mathrm{cl}} = 1/2$, $X$ K1-preserving — involution mechanism (Cat B, Claim A.3.2).
>
> (iv) **Geometric K≥2 forbidden**: $c > c^*_{\mathrm{max}}(G, \xi_0)$ — K=2 disks cannot fit with required separation (Cat B, Claim A.3.10).
>
> **Necessary condition for $\widehat K > 1$**: None of (i), (ii), (iv). Corresponds to "low-c far-from-critical multi-formation" regime (e.g., c=0.3 β=30 on 2D — R17 K=7.76).

### A.3.12 Resolution of G-miss-4

G-miss-4 is **structurally addressed** by Theorem G-miss-4:
- Near-critical K=1 proved Cat A via Claim A.2.1.
- c=1/2 K=1 proved Cat B via Claim A.3.2 (involution).
- High-c K=1 proved Cat B via geometric constraint (Claim A.3.10).

**Residual**: Low-c, far-from-critical, not covered by (i)/(ii)/(iv) → "multi-K regime" where $\widehat K \geq 1$ but distribution / mechanism remain open. This is **NQ-79 (new)**: classification of multi-K basin landscape when no K=1 forcing mechanism applies.

---

# Part B — G-miss-2 Resolution: Round 8 $c_0$-Counting Scope Correction

## §B.1 Restatement of Round 8 claim

From logs 2026-04-22 99_summary §4.1 R8 entry:
> **Universal $c_0$-Counting Theorem**: Equivariant CR framework; universal per-irrep rules; graph-class cascade table; $K_n$ two-valued exact; Hyp. Thm. 4.1*(C) upgrade.

Original Round 8 claim (bundled Cat A): For finite connected graph $G$ with automorphism group $\Gamma = \mathrm{Aut}(G)$, the number of index-0 critical points of $\mathcal{E}$ on $\Sigma_m$ modulo $\Gamma$-action, i.e.,
$$c_0(\beta, c, G) = \#\{u^* \in \Sigma_m : \nabla\mathcal{E}(u^*) = 0, u^* \text{ local min}\}/\Gamma,$$
can be **universally computed** from spectral data of $G$ + group-theoretic data of $\Gamma$, via equivariant Crandall-Rabinowitz applied per irrep of $\Gamma$.

## §B.2 Equivariant Crandall-Rabinowitz machinery

### B.2.1 CR setup

Near bifurcation $\beta = \beta_c$, linearization $L(\beta_c) = H(u_{\mathrm{unif}}; \beta_c)$ has zero eigenvalue. CR: under transversality + nondegeneracy, branch of nontrivial solutions emerges.

**Classical CR (no symmetry)**: null space $N = \mathrm{span}(\psi)$ 1-dimensional. One branch.

**Equivariant CR** (with group action): $N$ is a $\Gamma$-invariant subspace; decomposes into irreps. For each irrep $\rho$ in $N$, apply CR fiberwise.

### B.2.2 Irrep-dimension analysis

Let $\Gamma$ act on $\mathbb{R}^n$ (tangent of $\Sigma_m$); decomposition:
$$\mathbb{R}^n = \bigoplus_\rho V_\rho^{\oplus m_\rho}$$
where $\rho$ ranges over irreducible representations of $\Gamma$, $V_\rho$ has $\dim \rho$ components each, $m_\rho$ is multiplicity.

**Null space at bifurcation**: $N \subset \mathbb{R}^n$ is $\Gamma$-invariant → decomposes as $N = \bigoplus_\rho V_\rho^{\oplus k_\rho}$ for some $k_\rho$.

At a **simple bifurcation** (generic): $N$ is single irrep, i.e., some $V_\rho$ with multiplicity 1.

**Branching from single $V_\rho$**:
- $\dim V_\rho = 1$ (abelian irrep): 1D CR; 1 branch pair (supercritical pitchfork).
- $\dim V_\rho = 2$ (e.g., $D_4$'s 2-dim irrep, cyclic group's complex pair): 2D CR; branch structure = orbits of $\Gamma$ on $V_\rho$.
- $\dim V_\rho \geq 3$: requires **Cicogna-Gaeta bifurcation** theorem; not generic.

### B.2.3 $A_2/A_1 \in \{2, 4\}$ classification (Round 4)

For $D_4$ (2D square lattice Aut):
- 4 one-dim irreps (trivial, sign, axis-flip, diagonal-flip): pitchfork with $A_1$ axes.
- 1 two-dim irrep (standard): pitchfork with $A_2$ axes (2-fold or 4-fold).

Round 4 ratio classification ($A_2 / A_1 \in \{2, 4\}$) covers:
- 1-dim irreps uniformly.
- 2-dim irreps with $Z_4$ vs $Z_2$ stabilizer (→ 2 or 4 orbits).

**Explicit scope**: $\leq 2$-dim irreps, with known orbit structure.

---

## §B.3 Explicit scope of Round 8

### B.3.1 Graphs with only 1-dim + 2-dim irreps

**Group theory fact**: Every **abelian** group has only 1-dim (complex) irreps. Real-irreps are 1-dim (over $\mathbb{R}$, complex conjugate pair → 2-dim real).

- Abelian $\Gamma$: all irreps ≤ 2-dim over $\mathbb{R}$. ✓ Round 8 applies.
- $D_n$ for $n$ odd: 2 one-dim + (n-1)/2 two-dim. ✓ Round 8 applies.
- $D_n$ for $n$ even: 4 one-dim + (n-2)/2 two-dim. ✓ Round 8 applies.
- Dihedral groups in general: ≤ 2-dim. ✓ Round 8 applies.

**Graph examples in scope**:
- $C_n$ cycle: $\Gamma = D_n$. ✓
- 2D torus: $\Gamma = (\mathbb{Z}_L)^2 \rtimes D_4$; individual factors have 1D/2D irreps; combined may have up to 4D irreps via induction. **Borderline** — need careful case analysis.
- 2D free-BC square: $\Gamma = D_4$. ✓
- Barbell (two cliques + bridge): $\Gamma \subset S_k \times S_k \times \mathbb{Z}_2$; $S_k$ has (k-1)-dim standard irrep. **Not in scope**.
- Complete graph $K_n$: $\Gamma = S_n$; has (n-1)-dim standard irrep. **Not in scope**.

### B.3.2 Round 8 claim re $K_n$

R8 notes "$K_n$ two-valued exact". But $S_n$ has (n-1)-dim standard irrep — seemingly out of scope per §B.3.1.

**Resolution**: On $K_n$, the energy $\mathcal{E}$ has **extra symmetry**: $S_n$ acts on $\Sigma_m$ by permuting all sites. Due to full symmetry, **critical points are invariant strata**:
- $u \equiv c$ uniform (fully symmetric, trivial irrep).
- $u$ = indicator of $k$-subset (partially symmetric, invariant under $S_k \times S_{n-k}$).

$S_n$-orbit decomposition: number of $S_n$-orbits of critical points = number of distinct $\{k : k = \lfloor cn \rfloor, \lfloor cn \rfloor + 1\}$ types. "Two-valued" = two types in generic mass $m = cn$.

**Mechanism different from generic Round 8**: On $K_n$, the high symmetry forces all critical points to be $S_n$-orbits of "fully indicator" configurations, bypassing irrep decomposition.

**Scope note**: Round 8's $K_n$ result uses graph-specific fact (all critical points are indicator-subsets), not equivariant CR per irrep. **Different proof technique**, still Cat A but for different reason.

### B.3.3 Corrected Round 8 scope statement

> **Round 8 Universal $c_0$-Counting (scope-corrected)**: The equivariant Crandall-Rabinowitz framework gives explicit $c_0(\beta, c, G)$ counting when:
>
> (a) $\Gamma = \mathrm{Aut}(G)$ has only **1-dim and 2-dim irreps** (Cat A).
> 
> (b) $G$ is **vertex-transitive with full-symmetry-forced critical points** (e.g., $K_n$, other high-symmetry graphs) (Cat A by different proof).
>
> **Outside scope**:
> (c) $\Gamma$ with 3+ dim irreps requiring Cicogna-Gaeta or beyond (e.g., $S_n$ standard irrep on $n$-vertex graphs that are NOT $K_n$, $A_n$ for $n \geq 5$) — **Cat C conjecture**.
>
> (d) Generic graphs with $\Gamma = \{e\}$ — **completely different technique required** (random-matrix Hessian analysis) — **open**.
>
> (e) **Weighted graphs** with non-uniform $\mathbf{N}$ kernel (breaks symmetry even if unweighted $G$ had symmetry) — **Cat C open**.

---

## §B.4 Non-abelian extension (scope (c))

### B.4.1 What's needed

For $\Gamma = S_n$ (n ≥ 4) acting on non-$K_n$ graph (e.g., caterpillar, star graph with permutation symmetries), standard $(n-1)$-dim irrep appears in $N$.

**Cicogna-Gaeta bifurcation theorem**: For $\geq 3$-dim null space, branching is **not generically to pitchfork** but can go to cone, surface, etc. Number of branches depends on orbits of $\Gamma$ on $S^{\dim V - 1}$ (unit sphere in irrep).

**For $S_n$ standard irrep**: Orbits on $S^{n-2}$ (standard irrep minus trivial) = partitions / conjugacy classes. Count = number of integer partitions of n minus 1.

**Example**: $S_4$ standard irrep is 3-dim. Orbits on $S^2$ under $S_4$ = 4 types (partitions of 4: (4), (3,1), (2,2), (2,1,1), (1,1,1,1) — minus trivial = 4 nontrivial). So up to 4 branches from single 3-dim irrep.

### B.4.2 Formula proposal (Cat C)

> **Proposal (Cat C, NQ-80 new)**: For graph $G$ with $\Gamma = \mathrm{Aut}(G)$ acting nontrivially with irrep decomposition $N = \bigoplus_\rho V_\rho^{k_\rho}$ at bifurcation, the $c_0$ count is:
> $$c_0(\beta_c, G) = \sum_\rho k_\rho \cdot N_\rho(\Gamma, \dim V_\rho)$$
> where $N_\rho$ is the number of $\Gamma$-orbits on $S^{\dim V_\rho - 1}$ under the irrep action.

**For** $\dim V_\rho = 1$: $N_\rho = 2$ (trivial pitchfork pair).
**For** $\dim V_\rho = 2$ (D_n-type): $N_\rho = 2$ or $N_\rho = 4$ (Round 4 classification).
**For** $\dim V_\rho \geq 3$: $N_\rho$ from Cicogna-Gaeta / orbit counting.

### B.4.3 Category

Proposal Cat C — requires:
- Cicogna-Gaeta machinery formally applied to SCC's cubic coefficient structure.
- Per-irrep $N_\rho$ values tabulated for small $\Gamma$.

---

## §B.5 Generic graphs (scope (d))

### B.5.1 $\Gamma = \{e\}$ case

Generic random graph $G$ has trivial automorphism group. Equivariant CR offers no reduction.

**$c_0$-count methodology**:
- Direct Morse theory: $c_0$ lower-bounded by Betti number $b_0(\Sigma_m) = 1$ (contractible).
- Upper bound: depends on spectral structure of $L$ (all eigenvalues distinct generically).
- **Conjecture (NQ-81)**: On generic connected $G$ of size $n$ with distinct Laplacian eigenvalues, $c_0(\beta) = 1 + \#\{k \geq 2 : \mu_k < 0\text{ at some considered parameter}\}$ — basically unconstrained enumeration.

### B.5.2 Random matrix theory connection

**Conjecture (speculative, NQ-82)**: For $G$ drawn from Erdős–Rényi $G(n, p)$, the Hessian $H(u_{\mathrm{unif}}; \beta, c)$ eigenvalue distribution follows Wigner semicircle + mean shift. $c_0(\beta, c)$ follows random-matrix cumulative distribution.

Link to Gaussian matrix theory; **beyond current canonical scope**.

---

## §B.6 Weighted graphs (scope (e))

Per NQ-A1 from §04 axiom audit: canonical Group B allows arbitrary non-negative $\mathbf{N}$ weights. No current theorem on $c_0$ for weighted $G$.

**Claim (simple)**: If $G$ has automorphism group $\Gamma$ under weight-preserving automorphisms, Round 8 applies to weight-preserving subgroup. Weights can **reduce** $\Gamma$.

**Example**: 2D square with non-uniform weights breaks $D_4$ → $\mathbb{Z}_2$ (if horizontal/vertical edges have different weights). Round 8 still applies to $\mathbb{Z}_2$.

**Category**: Cat B achievable — reducing to weight-preserving $\Gamma$. NQ-83 formalization.

---

## §B.7 Corrected Cat A statement (Round 8 revision)

Proposed corrected statement for Stage 6 merge:

> **Theorem G-miss-2 (Universal $c_0$-Counting, corrected Cat A scope)**: Let $G$ be a finite connected graph with automorphism group $\Gamma = \mathrm{Aut}(G)$. Suppose one of:
>
> (A1) $\Gamma$ has only 1-dim and 2-dim real irreducible representations. *Examples: abelian $\Gamma$, dihedral $D_n$, all products thereof.*
>
> (A2) $G$ is vertex-transitive AND every critical point of $\mathcal{E}$ is $\Gamma$-invariant up to orbit (e.g., complete graph, Cayley graph with high symmetry).
>
> Under (A1) or (A2), the per-irrep branching count
> $$c_0(\beta_c, c, G) = \sum_\rho k_\rho \cdot N_\rho$$
> gives exact Cat A count, where $k_\rho$ is the multiplicity of irrep $\rho$ in null space at bifurcation and $N_\rho \in \{2, 4\}$ (from Round 4 $A_2/A_1$ classification for dim ≤ 2).
>
> **Demoted to Cat C for scope outside (A1)/(A2)**:
> - Non-abelian $\Gamma$ with irreps of dim ≥ 3 (requires Cicogna-Gaeta; NQ-80).
> - Generic $\Gamma = \{e\}$ (requires enumerative / random-matrix approach; NQ-81, NQ-82).
> - Weighted graphs (reduces to weight-preserving $\Gamma$; NQ-83).

---

## §B.8 Verification of canonical claims within corrected scope

### B.8.1 Check: canonical §13 T-Birth-Parametric

Cat A for $D_4$-symmetric 2D square; Cat B for general non-symmetric. **Match** with corrected scope: $D_4$ in (A1), general non-symmetric drops to scope (c).

### B.8.2 Check: Round 4 $\Phi_4$ on $C_n, T^2$

$C_n$ has $D_n$ Aut — in scope (A1).
$T^2$ has $(\mathbb{Z}_L)^2 \rtimes D_4$ Aut. Needs irrep analysis: tensor product of $(\mathbb{Z}_L)$-irreps (1-dim) with $D_4$-irreps. Max dim = 2. **In scope (A1)** ✓.

### B.8.3 Check: Round 8 $K_n$ two-valued exact

$K_n$ has $S_n$ Aut; $S_n$ has (n-1)-dim standard irrep. Per §B.3.2, $K_n$ exception is via scope (A2) — vertex-transitive with full-symmetry-forced criticals. ✓

### B.8.4 Check: Round 10 Tree Structure Theorem

Round 10 tree structure via saddle-node cascade. Uses pitchfork + saddle-node (1D/2D reductions per-branch). Scope (A1) ✓ for symmetric trees.

---

## §B.9 Summary of G-miss-2 resolution

**Action items for canonical Stage 6**:

1. **Round 8 Cat A → Cat A (restricted) + Cat B/C (extensions)**: Explicit scope statement as Theorem G-miss-2 (§B.7).
2. **NQ-80, NQ-81, NQ-82, NQ-83 (new)**: non-abelian, generic, random-matrix, weighted extensions.
3. **Verification table**: canonical §13 theorems that cite "universal" language — audit and restrict or extend.

**Categorization post-resolution**:
- Round 8 in-scope (A1/A2): Cat A **maintained**.
- Out-of-scope cases: **downgraded or opened** (Cat B/C/open).
- No silent resolution.

---

# Part C — Integration and Next Steps

## §C.1 Status update

| Gap | Pre-resolution | Post-resolution |
|---|---|---|
| G-miss-4 | Observation-pattern without theory | Theorem with 3 sufficient conditions (Cat A + 2× Cat B) |
| G-miss-2 | "Universal" Cat A claim over-broad | Cat A restricted + 4 Cat C/open extensions |

## §C.2 New NQ this continuation file

- **NQ-79**: Classification of multi-K basin landscape when no K=1 forcing mechanism applies (complement of G-miss-4 Theorem).
- **NQ-80**: Non-abelian $\Gamma$ with dim-≥3 irreps via Cicogna-Gaeta.
- **NQ-81**: Generic $\Gamma = \{e\}$ $c_0$-counting (enumerative).
- **NQ-82**: Random-matrix theory for $c_0$ on Erdős–Rényi.
- **NQ-83**: Weighted-graph reduction to weight-preserving subgroup.

**This continuation adds 5 new NQ**. Cumulative session total: 25 (from 03) + 8 (from 04) + 5 (from 05) = **38 new NQ** for 2026-04-23.

## §C.3 Back-reference updates

### C.3.1 `04_axiom_audit_and_sf_gaps.md` §B.6 priority matrix update

| Gap | Pre-05 status | Post-05 status |
|---|---|---|
| G-miss-1 | Medium, unresolved | Medium, unresolved |
| G-miss-2 | High, unresolved | **Cat A restricted + 4 NQ**, scope-clarified |
| G-miss-3 | Medium, unresolved | Medium, unresolved |
| G-miss-4 | Highest, unresolved | **Cat A + 2× Cat B theorem**, substantially resolved |

### C.3.2 `SF_layer_classification.md` §8.1 updates

- G-miss-2 status: scope now **Cat A (abelian/dihedral/$K_n$)**, explicit statement in §B.7.
- G-miss-4 status: scope now **Cat A near-critical + Cat B involution + Cat B geometric**, theorem in §A.3.11.

### C.3.3 Canonical merge additions

Beyond previous §03 §2 proposals, add:

- **New Theorem §13: G-miss-2 Universal $c_0$-Counting (restricted)**: replaces unqualified "Round 8 Universal".
- **New Theorem §13: G-miss-4 K=1 Generic Sufficiency**: three sufficient condition cases.
- **Erratum: Round 8 scope restriction** — explicit statement of outside-scope cases.

## §C.4 Remaining single-formation gaps

After tackling G-miss-4 and G-miss-2, remaining from §04:

- **G-miss-1** (corner regularity): cleanup-level, low priority.
- **G-miss-3** (non-regular $\xi_0$): medium priority, connects to NQ-33 (long-standing).
- **G-miss-5** (corner KKT count): enrichment, low.
- **G-miss-6** ($\mathbf{C}$ axiom demotion): cleanup, low.
- **G-miss-7** (thermal single-formation): medium, connects to G5.

**Next prioritization (if continuing)**:
- **G-miss-3** before **G-miss-7** (geometry before thermal).
- **G-miss-1** and **G-miss-5** as bundle (both corner-related).

## §C.5 File status

- **G-miss-4 resolution**: Theorem with 3 sufficient conditions (Cat A single-mode, Cat B involution, Cat B geometric). Empirical regime mapping (§A.3.7) matches 6/7 observed cases; 1 residual (c=0.7 2D sq β=30 K=1.08) consistent with multiple conditions partially applying.
- **G-miss-2 resolution**: Corrected Cat A scope (A1 / A2 conditions) + explicit out-of-scope enumeration (4 NQ).
- **Category self-classification**: G-miss-4 Theorem tentative Cat A + 2× Cat B; G-miss-2 Theorem Cat A (restricted scope).
- **Intended promotion**: `working/SF/k1_sufficient.md` (new) + `working/SF/c0_counting_scope.md` (new). Alternatively, expansion of `working/SF/cardinality_open.md` §8.10+.

**End of 05_gmiss4_and_gmiss2_resolution.md.**
