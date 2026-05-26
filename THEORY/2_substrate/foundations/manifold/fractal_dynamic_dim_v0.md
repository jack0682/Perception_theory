---
type: working/foundation/proof-derivation
date: 2026-05-20
session_label: W8-Day3 (continued) — Type F Dynamic Fractal Dimension Framework + 4 Theorem Derivation
canonical_version: CV-1.18 (sealed 2026-05-19, untouched)
parent: manifold_topology_attempt_v0.md
status: Cat C synthesis with 2 Cat B-target concrete claims
---

> [!nav] Linked: [[manifold_topology_attempt_v0]] · [[_SUMMARY_v0.2]] · [[canonical]] · [[CV-1.18_SEAL]]

# Type F (Dynamic Fractal Dimension) — 4 Theorem Derivation + Master Synthesis

## §0. Context

본 file 의 위치: `manifold_topology_attempt_v0.md` 의 *Type F (Fractal/Dynamic)* 차원 종류 확장. 이전 5-tier synthesis (Bakry-Émery + Whitney + Surgery + Assembly) 에 **interfacial-growth universality framework** 를 접목해 *4개 정리* 도출.

**핵심 메타-인사이트** (사용자 직관):
> H5 의 Goldstone 깨짐은 *통상 정리 차원* 에서는 obstruction 이지만, *동적 프랙탈 차원 (Type F)* 의 관점에서는 *측정 가능한 anomalous scaling* — KPZ universality 의 SCC 유비. H5 를 *수학적 무거움* 이 아닌 *물리적으로 측정 가능한 객체* 로 변환.

4 개 병렬 scientist 에이전트 (Opus tier) 가 도출한 결과:
1. **Theorem F1**: SCC dynamic universality class identification (Edwards-Wilkinson + stratified breakdown)
2. **Theorem F2**: Distance-controlled crossover (mixing-crossover identity)
3. **Theorem F3**: Static fractal dim formula on Σ_T8^(k) stratum
4. **Theorem F4** (protocol): Falsifiable numerical experiment design

본 file 은 4 정리를 통합하고, *cross-theorem consistency* 를 명시하며, 기존 5-tier synthesis 와 *수평적으로* 합쳐 *6-Type Master Statement* 형성.

---

## §1. Master Statement (4 Theorem 통합)

**SCC Dynamic Universality Theorem (Cat C synthesis)**:

Given $(G, \Theta, T_*)$ with $G$ finite connected, $\Theta$ admissible (canonical Cat A), $T_* > 0$. Let $d := \mathrm{dist}(\Theta, \Sigma_{T8})$ be the parameter-space distance to the spinodal critical surface. The reflected Langevin SDE
$$dU_t = -\nabla \mathcal{E}_\Theta(U_t)\,dt + \sqrt{2T_*}\,P_{T\Sigma_m}\,dB_t + dK_t$$
exhibits the following universality structure:

**(F1) Bulk (d > 0)**: SCC dynamics fall in the **massive Edwards-Wilkinson universality class** with:
- effective viscosity $\nu_{\mathrm{eff}} = 4\alpha$
- effective mass $m_{\mathrm{eff}} = \beta W''(c) \geq c_G d$ (Lemma 1.1, distance-controlled)
- dynamic exponent $z = 2$
- Family-Vicsek $(\alpha_{FV}, \beta_{FV}) = ((2-d)/2, (2-d)/4)_{\text{massive limit}}$

**(F2) Crossover regime**: Goldstone-direction mean-square displacement satisfies:
$$\sigma_{\mathrm{Gold}}^2(t) = \frac{T_*}{c_G d}(1 - e^{-2 c_G d \cdot t})$$
with universal scaling collapse $\tilde\sigma^2(\tilde t) = 1 - e^{-\tilde t}$ under $\tilde t = t/\tau_d$, $\tau_d = 1/(2 c_G d)$. Crossover time $\tau_d \to \infty$ as $d \to 0$.

**(F3) Stratified at $\Sigma_{T8}^{(k)}$**: At $d = 0$ on stratum $\Sigma_{T8}^{(k)}$ with kernel dim $k$:
- Goldstone subspace $V_k$ (dim $k$): pure Brownian motion, $\sigma_{\mathrm{Gold}}^2(t) = 2T_* k t$, **no saturation**
- Transverse $V_k^\perp$: massive EW, gapped
- Static fractal dim of typical configuration: $D_f^{(k)} = (n-1) - k$
- Roughness exponent: $\alpha_k = k/(n-1)$

**(F4) Mixing-crossover identity**: For $d > 0$:
$$\tau_{\mathrm{mix}}(\Theta) \asymp \tau_d = \frac{1}{2 c_G d}$$
(equivalence up to $O(1)$ constants; both controlled by the soft Goldstone mode).

**핵심 통찰**:
> H5 의 *수학적 본질* 은 SCC 가 Edwards-Wilkinson universality 의 *경계* 에 있다는 것 — bulk 에서는 EW 가 *작동* 하지만 (Cat A canonical 도구들 사용 가능), $\Sigma_{T8}$ 에서는 EW 가 *부분적으로 깨짐* (Goldstone direction 만 anomalous). 이게 codim-1 박막에 *완전히 localized*.

---

## §2. Theorem F1 — SCC Dynamic Universality Class (Agent 1 결과)

### F1.1 Statement

**Theorem (Cat B linearized, 후보)**:
Under hypotheses (H1)-(H5) [(H1) torus graph, (H2) admissible Θ, (H3) critical point u*, (H4) F3 axiom, (H5) linearization regime $\lVert \xi_t \rVert \leq \delta_0$]:

**(A) Bulk** ($u^* = c\mathbf{1}$ strictly off $\Sigma_{T8}$): Linearized SCC is discrete EW
$$\partial_t \xi = -\nu_{\mathrm{eff}} L \xi - m_{\mathrm{eff}} \xi + \sqrt{2T_*} \eta$$
with $\nu_{\mathrm{eff}} = 4\alpha$, $m_{\mathrm{eff}} = \beta W''(c)$.

Family-Vicsek exponents:
- Massive case ($m_{\mathrm{eff}} \neq 0$): $(\alpha_{FV}, \beta_{FV}, z) = (0, 0, 2)_{\text{massive}}$, exponential approach to finite saturation
- Massless limit ($m_{\mathrm{eff}} \to 0^-$): standard EW $(\alpha_{FV}, \beta_{FV}, z) = ((2-d)/2, (2-d)/4, 2)$

**(B) Stratified at $\Sigma_{T8}^{(k)}$**:
$$z = 2 \text{ on } V_k = \ker H, \quad z = \infty^{\mathrm{eff}} \text{ on } V_k^\perp$$

**(C) Cubic stability**: $W'''(c) = 12(2c-1) \neq 0$ generically. The trilinear vertex is **RG-irrelevant in $d \leq 4$** by power-counting at Gaussian fixed point. At $c = 1/2$ vanishes identically (restoring $\mathbb{Z}_2$ symmetry).

### F1.2 Verdict

**SCC ∈ massive Edwards-Wilkinson class** in bulk. **NOT KPZ** (no $(\nabla u)^2$ vertex — SCC is *potential* flow, not convective).

**SCC ≠ stochastic Allen-Cahn** (Bertini-Brassesco-Buttà 2009) due to simplex constraint, but linearized fluctuation theory coincides (constraint removes only $\phi_1$).

**SCC vs Funaki-Spohn 1997 (∇φ interface)**: SCC has bounded $u \in [0,1]$ (compact polytope), while ∇φ is unbounded. Linearized theories coincide near critical points; nonlinear regimes differ due to compactness.

### F1.3 Connection to canonical Cat A

- **T-PF-A1-SDE Cat A**: provides well-posedness (Lions-Sznitman). F1 layers dynamic-statistical content on top.
- **T-PF-A1-PE Cat A**: spectral gap $\mu_2 = 4\alpha\lambda_2 + \beta W''(c)$ controlling EW relaxation **is** the SCC Poincaré constant on $T\Sigma_m$.
- **T-V5b-T Cat A**: identifies $\Sigma_{T8}$ where $\mu_2 = 0$. F1 shows universality class changes *exactly there*.
- **T-Temporal-Identity Cat A (CV-1.13)**: Goldstone diffusion $\sigma^2_{Gold}(t) = 2T_* k t$ is the microscopic origin of identity drift along soft transport.

### F1.4 Gaps (5 open issues)

1. **Nonlinear EW** (OP-NEW-1): prove $w^2/t \to 2T_*$ in full nonlinear SDE on $\Sigma_{T8}^{(1)}$. Tools: Dirichlet form + Mosco convergence (Funaki 2005).
2. **Cubic RG rigorous** (OP-NEW-2): Wilsonian RG with $\epsilon$-expansion at $d=4-\epsilon$; regularity structures (Hairer 2014) for $\Phi^4$-type vertex.
3. **Reflection** (OP-NEW-3): show boundary local time $dK_t$ contribution negligible in $T_* \to 0$ at rate $\exp(-c/T_*)$ (Freidlin-Wentzell).
4. **Kramers escape match** (OP-NEW-4): connect $z = 2$ to canonical OP-0005 Kramers rate, prefactor renormalization.
5. **Multi-stratum coupling** (OP-NEW-5): $\Sigma_{T8}^{(k)}$ with $k \geq 2$ kernel modes can couple at cubic resonance order. Non-resonance condition on $G$ implicit; needs proof.

---

## §3. Theorem F2 — Distance-Controlled Crossover (Agent 2 결과)

### F2.1 Setup

From Tier 1 synthesis (Lemma 2.4): $\mu_2(\Theta, c) \geq c_G \cdot d$ where $d := \mathrm{dist}(\Theta, \Sigma_{T8})$.

Projecting Langevin trajectory onto Fiedler eigenvector $\phi_2$:
$$a_2(t) := \langle U_t - u^*, \phi_2 \rangle$$
satisfies 1-dim OU SDE:
$$da_2 = -\mu_2 a_2\,dt + \sqrt{2T_*}\,dW$$

Exact solution (Uhlenbeck-Ornstein 1930):
$$\boxed{\;\sigma_{\mathrm{Gold}}^2(t) = \frac{T_*}{\mu_2}(1 - e^{-2\mu_2 t})\;}$$

### F2.2 Three regimes

| Regime | $t$ | $\sigma_{\mathrm{Gold}}^2$ | $z$ |
|---|---|---|---|
| Diffusive | $t \ll \tau_d$ | $2T_* t$ | 2 |
| Crossover | $t \sim \tau_d$ | $T_*/(c_G d)(1 - e^{-1})$ | non-universal |
| Saturated | $t \gg \tau_d$ | $T_*/(c_G d)$ | $\infty$ |

with crossover time $\tau_d := 1/(2 c_G d)$.

### F2.3 Three theorems

**Theorem F2.A (Crossover Time)**: $\tau_d = 1/(2 c_G d) \to \infty$ as $d \to 0$. This is the rigorous statement of **anomalous scaling at $\Sigma_{T8}$**.

**Theorem F2.B (Universal Scaling Collapse)**: With $\tilde t := t/\tau_d$, $\tilde\sigma^2 := \sigma_{\mathrm{Gold}}^2 \cdot \mu_2/T_*$:
$$\tilde\sigma^2(\tilde t) = 1 - e^{-\tilde t}$$
*Independent of $(G, m, \Theta, T_*)$*. All distance-dependence absorbed into $\tau_d$ and saturation amplitude.

**Theorem F2.C (Mixing-Crossover Identity)**: Under Cor. 7.1 ($\lambda_1 \geq c_G d$):
$$\tau_{\mathrm{mix}} \leq 1/(c_G d) = 2\tau_d$$
*Goldstone is the slowest mode*; controls both Poincaré gap and crossover.

### F2.4 Sharpening of canonical Cat A

Canonical T-PF-A1-PE: $\lambda_1 \geq (\pi^2/n) e^{-\mathrm{osc}(\mathcal{E})/T_*}$.

With $\mathrm{osc}(\mathcal{E}) = O(\beta n)$, RHS $\sim (\pi^2/n) e^{-\beta n/T_*}$ — *exponentially small* in formation regime.

**Sharpening criterion**: $c_G d > (\pi^2/n) e^{-\beta n/T_*}$, equivalently $\beta n/T_* > \log(n^2/(c_G d \pi^2))$. **Holds for any $d > 0$ in typical SCC** ($\beta \gg T_*$).

### F2.5 Gaps

1. **Reflection rigor**: OU reduction exact modulo Skorokhod $K_t$. Cat A requires $\mathbb{P}[\tau_\partial < \tau_d] \to 0$.
2. **$c_G$ explicit form**: Lemma 1.1 existence only; sharp $c_G(G, m)$ in $\lambda_2(L), \lVert \phi_2 \rVert_\infty$, spinodal width.
3. **Mixing lower bound**: BGL gives upper $\tau_{\mathrm{mix}} \leq 1/\lambda_1$; matching $\tau_{\mathrm{mix}} \geq c \tau_d$ needs spectral two-sided.
4. **Nonlinear corrections**: $W'''(c)$ at $O(a_2^3)$ renormalizes $\tau_d$ but preserves $d^{-1}$ scaling (Freidlin-Wentzell perturbative).

---

## §4. Theorem F3 — Static Fractal Dim on $\Sigma_{T8}^{(k)}$ (Agent 3 결과)

### F3.1 Setup — Gibbs decomposition

At $\Theta \in \Sigma_{T8}^{(k)}$, $u^*$ critical with $\mathrm{Hess} H$ having kernel dim $k$. Spectrum:
$$0 = \mu_1 = \cdots = \mu_k < \mu_{k+1} \leq \cdots \leq \mu_{n-1}$$

Decompose $\xi := u - u^* \in T_{u^*}\Sigma_m = V_k \oplus V_k^\perp$:
$$\pi_{T_*}^{\mathrm{lin}}(d\xi) = \rho_{\mathrm{Gold}}(\xi_{Gold})\,d\xi_{Gold} \otimes \mathcal{N}(0, T_* H_\perp^{-1})(d\xi_\perp)$$

Goldstone marginal is **uniform on bounded convex polytope section** $\Omega_k := V_k \cap (\Sigma_m - u^*) \cap ([0,1]^n - u^*)$ — *not* Gaussian!

### F3.2 Main theorem

**Theorem F3 (Static Fractal Dim, Cat C candidate)**:
For $u \sim \pi_{T_*}$ near $u^* \in \Sigma_{T8}^{(k)}$, with probability $1 - o(1)$ as $T_* \downarrow 0$:

**(i)** Level sets $\{u : u(x) = a\}$ (generic $a$) have Hausdorff/box-counting fractal dim
$$\boxed{\;D_f^{(k)} = (n-1) - k\;}$$
$D_f^{(0)} = n-2$ (standard non-degenerate codim-1).

**(ii)** Roughness exponent $\alpha_k = k/(n-1)$.

**(iii) Goldstone-fractal correspondence**:
$$\alpha_k \cdot \dim T\Sigma_m = k = \dim V_k$$

### F3.3 Proof sketch

Gaussian-uniform decomposition $\xi = \xi_{Gold} + \xi_\perp$:
- $\xi_\perp$ (Gaussian, dim $n-1-k$): level set codim-1 contributes $n-2-k$
- $\xi_{Gold}$ (uniform on $\Omega_k$, dim $k$): adds $k-1$ via Goldstone translation, plus $+1$ thickening (level set commutes with Goldstone translation up to relabeling)

Total: $(n-2-k) + (k-1) + 1 = n-1-k$.

### F3.4 Verification per stratum

| $k$ | $D_f^{(k)}$ | $\alpha_k$ | 의미 |
|---|---|---|---|
| 0 | $n-2$ | 0 | Standard codim-1 (no Goldstone) |
| 1 | $n-2$ | $1/(n-1)$ | Generic neck — Goldstone translates levels, no rupture |
| 2 | $n-3$ | $2/(n-1)$ | Cap (Morse-Bott) — 2D fold |
| $n-1$ | $0$ | 1 | Fully degenerate — points only |

### F3.5 Gaps

1. **Cubic regularization rigor**: Goldstone marginal regularized by $D^3\mathcal{E}$ at scale $T_*^{1/4}$. Need quantitative concentration bound.
2. **Persistence equivalence**: $D_f^{\mathrm{pers}}(k) = D_f^{(k)}$ asymptotically? Boissonnat-Pritam 2021 framework, status Cat C.
3. **Hausdorff vs box-counting**: Requires Frostman energy bound; standard for Gaussian (Adler-Taylor), needs mixed Gaussian-uniform verification.
4. **Non-asymptotic regime**: $k = \Theta(n)$ case uncharacterized.
5. **Parameter neighborhood radius**: depends on $\mu_{k+1}$; Whitney regularity qualitative only.

---

## §5. Theorem F4 — Numerical Test Protocol (Agent 4 결과)

### F5.1 Mapping

| Conjecture | 실험 | Primary statistic |
|---|---|---|
| F1 (universality) | exp-Fractal-3 | $(\alpha, \beta)$ vs EW prediction |
| F2 (crossover) | exp-Fractal-2 | $\chi^2$ of scaling collapse |
| F3 (static D_f) | exp-Fractal-1 | $D_f^{(k)}$ jump = 1 ± 0.2 |
| F1 ↔ F3 | exp-Fractal-4 | $\vert D_f - 1/\gamma_k\vert < 0.1$ |

### F5.2 Specifications

**exp-Fractal-1** (Static D_f): 2D torus 16×16 + 32×32, $\beta/\alpha$ scan, 10^4 samples per Θ, box-counting at ε=1,2,4,8. **Cost: 30 CPU-hours**.

**exp-Fractal-2** (Crossover): 16×16 torus, $d \in \{0.01,0.03,0.1,0.3,1.0\}$, 100 runs per $d$, Fiedler projection. **Cost: 2 CPU-hours**.

**exp-Fractal-3** (Universality): 4 graphs (2D/3D torus, random-regular, K_16). Flat-interface IC, vary $L$, extract $(\alpha, \beta)$. **Cost: 8 CPU-hours**.

**exp-Fractal-4** (Persistence): Re-use exp-1 reservoir, PH₀ via k_soft.py, power-law tail fit (Clauset et al. 2009). **Cost: 3 CPU-hours**.

**Sanity (exp-Fractal-90)**: Pure GFF baseline. Expected $D_f^{GFF} = 1$ (continuum), known $\gamma_{GFF} = 2$ analytic (Bobrowski-Skraba 2020).

### F5.3 Falsification criteria

- F1 refuted: $D_f^{(1)} - D_f^{(2)}$ CI excludes $1 \pm 0.2$
- F2 refuted: scaling collapse $\chi^2 p < 0.01$ or $c_G$ varies > 30%
- F3 refuted: $(\alpha, \beta)$ deviates from EW by 3σ in $d \to \infty$ limit
- F4 refuted: $\vert D_f^{box} - 1/\gamma_k\vert > 0.2$ non-overlapping CI

### F5.4 Total budget

**~43 CPU-hours, parallelizable to ~6 wall-hours on 8 cores**. Existing scc/ + k_soft.py infrastructure sufficient; only new graph constructors needed (no scc/ edits — W8 anti-goal preserved).

---

## §6. Cross-Theorem Consistency Check

### §6.1 Theorem 1 vs Theorem 2 (anticipated critic issue)

**Critical conceptual point**: "Goldstone direction" has two distinct meanings:

- **On $\Sigma_{T8}$**: $\mu_2 = 0$ exactly. Fiedler mode is *true* Goldstone (zero-eigenvalue direction). Pure Brownian motion in this direction (Theorem 1B linear growth).
- **Near $\Sigma_{T8}$ (bulk, $d > 0$)**: $\mu_2 = c_G d > 0$. Fiedler mode is *almost-Goldstone* (small but positive curvature). OU process with rate $\mu_2$ (Theorem 2 crossover).

**Consistency**: As $d \to 0$, $\mu_2 \to 0$, OU rate $\to 0$, crossover time $\tau_d \to \infty$, OU reduces to Brownian motion. **Smooth limit**.

The two theorems describe the same Fiedler-mode dynamics in different parameter regimes. **Not inconsistent**.

### §6.2 Theorem 1 vs Theorem 3 (universality vs fractal dim)

Theorem 1 (dynamic): $z = 2$ on Goldstone subspace.
Theorem 3 (static): $D_f^{(k)} = (n-1) - k$ for typical configuration.

Connection (anticipated): Static fractal dim from typical Gibbs sample $\sim \pi_{T_*}$. Gibbs is the *stationary distribution* of Langevin dynamics (T-PF-A1-GI Cat A). Time-averaged trajectory has same fractal properties as space-averaged Gibbs.

**Static-dynamic identity** (Hohenberg-Halperin 1977 + Family-Vicsek 1985): At stationarity, time-averaged trajectory dim $= D_f^{trajectory}$, related to static $D_f^{(k)}$ by Family-Vicsek $D_f^{traj} = 2/z + D_f^{(k)}$ or similar (needs explicit derivation).

This connection is **structural but not yet rigorous** — Cat C.

### §6.3 Anticipated critic concerns

Based on critic experience (W8-Day3 first pass):

1. **Cubic RG irrelevance**: Allen-Cahn coarsening $L(t) \sim t^{1/2}$ contradicts pure EW universality! Resolution: SCC's polytope constraint + simplex mass conservation removes the *symmetry-breaking* mode that drives Allen-Cahn coarsening. The coarsening would happen *if* mass could rearrange, but $\sum u_i = m$ constraint blocks it. So bulk SCC is EW, NOT Allen-Cahn coarsening regime.

2. **z = ∞ on transverse**: This means *no growth in time*, which is correct for massive directions (immediately saturated). But "z = ∞" is loose notation — should say *no power-law growth*, exponential approach to saturation.

3. **D_f^(0) = n-2 vs D_f^(1) = n-2 — no jump**: Theorem 3 predicts no jump at k=0 vs k=1, only between k=1 and k=2. This is the **proper falsification target**: experiments must check k=1 → k=2 transition, not k=0 → k=1.

---

## §7. Master Synthesis — 6-Type Statement

### §7.1 6-Type Taxonomy (확장된)

| Type | 성격 | 예시 | $\Sigma_{T8}^{(k)}$ 에서의 behavior |
|---|---|---|---|
| A. 양자화 | 정수 | $k$, $K_{act}$, $\mathrm{mult}(\lambda_2)$ | jumps |
| B. 연속 | 실수 | $q$, $\lambda$, $T_*$ | smooth |
| C. 확장 | $n$-dependent | $\dim \Sigma_m$ | scaling |
| D. 함수적 | $\infty$-dim | $T$ | external |
| E. 대수적 | rank | $R(\mathrm{Aut})$ | discrete |
| **F. Fractal/Dynamic** | **non-integer** | $z, \alpha_k, D_f^{(k)}$ | **stratum-parameterized** |

### §7.2 Master Theorem (W8-Day3 final, Cat C synthesis)

**SCC Energy Landscape Dimension-Universality Structure Theorem**:

For $(G, \Theta)$ in post-bifurcation regime, the energy landscape $(\Sigma_m, \mathcal{E}_\Theta)$ is characterized by:

**(Part 1) Static structure** (from W8-Day3 manifold_topology_attempt_v0):
- Bulk: CD$(c_G d, \infty)$ holds, $W_{SCC}$ monotone, Poincaré gap $\lambda_1 \geq c_G d$
- Critical: $\Sigma_{T8} = \bigsqcup_k \Sigma_{T8}^{(k)}$ Whitney stratification, codim $k(k+1)/2 - 1$
- Assembly: $\mu: \mathcal{D}\otimes\mathcal{A}\otimes\mathcal{P} \twoheadrightarrow \mathrm{Inv}_{SCC} \setminus \{H5\}$

**(Part 2) Dynamic structure** (Type F, this file):
- Universality: SCC ∈ Edwards-Wilkinson class (bulk), stratified at $\Sigma_{T8}^{(k)}$
- Crossover: $\tau_d = 1/(2 c_G d)$, universal scaling collapse $1 - e^{-\tilde t}$
- Fractal dim: $D_f^{(k)} = (n-1) - k$, roughness $\alpha_k = k/(n-1)$
- Mixing: $\tau_{\mathrm{mix}} \asymp \tau_d$, controlled by Goldstone mode

**(Part 3) Cross-identity** (static-dynamic bridge):
- Goldstone direction is **both** the Hessian kernel **and** the slowest dynamic mode **and** the fractal-dim-reducing direction.
- $\dim \ker \mathrm{Hess} = k$ ⟺ $\dim V_{\mathrm{slow}} = k$ ⟺ $D_f$ reduction = $k$.

**(Part 4) H5 localization** (정면 돌파의 답):
> H5 = CD curvature degeneracy on Σ_T8 = Slowest mode (Goldstone) wandering = Fractal-dim reduction. *세 가지 표현, 한 가지 현상*.

### §7.3 *가장 leveraged* concrete new content

**Single Cat B-target claim** (post W8-Day3 work):
$$\boxed{\;\lambda_1(\Sigma_m, \mathcal{E}_\Theta, T_*) \geq c_G \cdot \mathrm{dist}(\Theta, \Sigma_{T8})\;}$$

**Second Cat C-target claim** (this session):
$$\boxed{\;D_f^{(k)} = (n-1) - k, \quad \alpha_k \cdot \dim T\Sigma_m = k\;}$$

**Third Cat C-target claim** (universal scaling):
$$\boxed{\;\tilde\sigma^2_{Gold}(\tilde t) = 1 - e^{-\tilde t}, \quad \tilde t = t \cdot c_G d\;}$$

These are *physically measurable* and *numerically testable* — turning H5 from obstruction into observable.

---

## §8. Cat Status Assessment (정직)

| Claim | Status | 비고 |
|---|---|---|
| F1 — SCC = massive EW class (bulk) | Cat B linearized (Agent 1) | Conditional on linearization regime H5 |
| F1 — Stratified at Σ_T8^(k) | Cat B linearized | Same |
| F1 — Cubic RG irrelevance | Cat C heuristic | Needs Hairer regularity structures |
| F2 — $\tau_d = 1/(2 c_G d)$ crossover | Cat B target | Lemma 1.1 + OU exact |
| F2 — Universal scaling collapse $1 - e^{-\tilde t}$ | Cat B target | Direct from OU |
| F2 — Mixing-crossover identity | Cat C | Two-sided spectral bound needed |
| F3 — $D_f^{(k)} = (n-1) - k$ | Cat C candidate | Cubic regularization gap |
| F3 — Goldstone-fractal correspondence | Cat C | Heuristic mode-counting |
| Master Theorem (Part 1+2+3+4) | Cat C synthesis | 4 components Cat B-C |

**Total**: 2 Cat B-target + multiple Cat C candidates + 1 Cat C synthesis. **No Cat A claimed**; all Cat A references are *to canonical theorems used as inputs*.

---

## §9. Next Steps (Priority Order)

### §9.1 Priority 1 (가장 leveraged, 3 sessions)

**Lemma 1.1 explicit $c_G$ Łojasiewicz calculation** → Theorem F2.A,B Cat B 확정.

Łojasiewicz constant 의 explicit form:
$$c_G = \min_{(\Theta,c) \in \Sigma_{T8}} \vert \nabla_\Theta \mu_2(\Theta, c)\vert / (4\alpha\lambda_2(L) + \beta \lvert W''(c) \rvert)$$

이게 계산되면 distance-controlled Poincaré gap Cat B 승급 + Theorem F2.A-B 자동 Cat B.

### §9.2 Priority 2 (병렬, ~2 weeks 수치 작업)

**Implement exp-Fractal-1 ~ 4** (Agent 4 protocol) — ~43 CPU-hours, falsification 가능.

가장 큰 가치: **F1, F2, F3 의 *수치 검증*** — 만약 통과하면 Cat C → Cat B 후보로 강력한 evidence.

특히 **exp-Fractal-2 (crossover)** 가 가장 결정적 — 단 2 CPU-hours, 직접 $c_G$ 측정 + scaling collapse 검증.

### §9.3 Priority 3 (장기, W9-W10)

1. **OP-NEW-1 nonlinear EW**: Funaki 2005 Dirichlet form approach → F1 Cat A 후보
2. **OP-NEW-2 cubic RG rigorous**: Hairer regularity structures → cubic vertex 통제
3. **OP-NEW-3 reflection rigor**: Freidlin-Wentzell exponential decay → boundary term 제어

### §9.4 Priority 4 (장기, W11+)

**Conjecture F1 의 새 OP 등록**: OP-FRACTAL-DYN-1,2,3 정식 OP 후보 (canonical OP catalog 의 *frontal H5 attack* 항목).

---

## §10. Hard-Constraint 자가 점검

- canonical 0 edits ✓
- DECLARATION 0 edits ✓
- scc/ 0 edits ✓
- 새 framework letter 0 ✓ (EW, KPZ, $D_f$, $z$, $\alpha_k$ 모두 표준 statistical physics 표기)
- silent OP resolution 0 ✓ (OP-NEW-1~5 모두 *명시 reference*)
- CN10 disclosure 준수 ✓ (universality class = *analogy*, not *instantiation*; SCC is its own object)
- pytest baseline 유지 ✓ (코드 변경 부재; 수치 작업은 Priority 2 별도 세션)

---

## §11. References

### §11.1 SCC Canonical (CV-1.18)
- T-PF-A1-SDE Cat A: reflected Langevin (canonical §6.3)
- T-PF-A1-GI Cat A: Gibbs invariance
- T-PF-A1-PE Cat A: Poincaré exponential ergodicity
- T8-Core Cat A: phase transition
- SB7 Cat A (L2495): Σ_Hess = Σ_T8 codim-1
- T-V5b-T / V5b-T-zero Cat A (L1328): Goldstone exact zero
- T-Temporal-Identity Cat A (CV-1.13)
- Lemma 2.4 (W8-Day3 synthesis): distance-controlled $\mu_2 \geq c_G d$
- Corollary 7.1 (W8-Day3): distance-controlled Poincaré $\lambda_1 \geq c_G d$
- AUX-1.5 §7 CN-COB, §8 D/A/P classification
- CV-1.18 §N: T_* ξ resident formal entry

### §11.2 External Literature
- **Edwards, Wilkinson** (1982) *Proc. R. Soc. A* 381 — surface roughening universality
- **Kardar, Parisi, Zhang** (1986) *PRL* 56 — KPZ universality
- **Funaki, Spohn** (1997) *Commun. Math. Phys.* 185 — ∇φ interface model
- **Bertini, Brassesco, Buttà** (2009) *Stoch. Proc. Appl.* 119 — stochastic Allen-Cahn
- **Hohenberg, Halperin** (1977) *Rev. Mod. Phys.* 49 — dynamic critical phenomena
- **Family, Vicsek** (1985) — Family-Vicsek dynamic scaling
- **Bakry, Gentil, Ledoux** (2014) — Markov diffusion + Γ_2 framework
- **Uhlenbeck, Ornstein** (1930) — OU process
- **Lions, Sznitman** (1984) — reflected SDE
- **Markowich, Villani** (1999) — entropy methods
- **Adler, Taylor** (1981/2007) — Random fields and geometry
- **Falconer** (2003) — Fractal Geometry
- **Sheffield** (2007) — Gaussian Free Field
- **Boissonnat, Pritam** (2021) — persistence-fractal equivalence
- **Hairer** (2014) *Invent. Math.* — regularity structures
- **Mourrat, Weber** (2017) — $\Phi^4_3$ rigorous
- **Freidlin, Wentzell** (1998) — random perturbations of dynamical systems
- **Clauset, Shalizi, Newman** (2009) *SIAM Review* — power-law tail MLE
- **Bobrowski, Skraba** (2020) — persistent homology of random fields

---

## §12. Closing

### §12.1 본 session 의 *진짜 산출물*

1. **6-Type taxonomy** 확장 (Type F = Fractal/Dynamic 추가)
2. **4 정리 도출** (F1 universality, F2 crossover, F3 fractal dim, F4 protocol) — 4 병렬 Opus 에이전트
3. **Master Synthesis Theorem** (Part 1+2+3+4) 통합
4. **3 concrete Cat B/C-target claims** (distance-Poincaré, fractal dim formula, scaling collapse)
5. **Cross-theorem consistency check** — anticipated critic concerns resolved
6. **Falsifiable numerical protocol** — 43 CPU-hours, ready for implementation

### §12.2 H5 정면 돌파의 *진짜 모양*

> H5 의 본질 = **SCC 가 Edwards-Wilkinson universality 의 경계** 에 있음 + **codim-1 박막 Σ_T8 에 완전 localized** + **stratum 차원 k 에 의해 정확히 매개변수화**.
>
> 정면 돌파의 의미 변화:
> - **이전 (W8-Day3 manifold_topology_attempt_v0)**: H5 위치 + 차원 + algebraic obstruction class 명시
> - **현재 (이 session)**: H5 의 *dynamic universality structure* 명시 + *수치적 falsifiability* 부여
> - **누적**: H5 가 *수학적 잔류* 에서 *물리적 측정 대상* 으로 전환됨

### §12.3 Slogan

> **"SCC 에너지장의 형태" 는, Edwards-Wilkinson universality 의 *부분적 깨짐* 으로 특성화된다. 깨짐은 *codim-1 박막 Σ_T8 위에서만*, *Goldstone direction 만*, *fractal dim $(n-1)-k$ 만큼* 발생. 이 3 가지 정확한 양화 (codim + direction + dim drop) 가 H5 의 *수학적 본질*. 우회 (H5') = 박막 제거. 정면 돌파 = 박막을 *분류 + 측정 + 시뮬레이션*. 본 session 의 *진짜 첫 시뮬레이션 가능한 정리* = $\tilde\sigma^2(\tilde t) = 1 - e^{-\tilde t}$.**

---

*End of working file. Session 2026-05-20 (W8-Day3 continued). Companion to manifold_topology_attempt_v0.md. Next session entry: §9.1 Priority 1 — Lemma 1.1 explicit $c_G$ Łojasiewicz calculation OR §9.2 Priority 2 — exp-Fractal-2 (crossover, 2 CPU-hours, most decisive).*

---

## §13. Critic Adversarial Pass — 4 Critical Findings + Corrections Required

본 file 작성 후 (Opus tier) critic adversarial agent 가 **4 critical + 4 major findings** 발견. 이전 §1-§12 의 *상당 부분이 잘못된 statement* 임을 확정.

### §13.1 Critical Finding C1 — "Goldstone confusion" (HIGH confidence)

**문제**: Theorem F1 ($z=2$ "Brownian on Goldstone $V_k$", linear growth $\mathbb{E}\lVert P_k\xi_t \rVert^2 = 2T_*kt$) 와 Theorem F2 ($\mu_2 \geq c_G d > 0$, OU crossover) 가 *동일 모드를 가리키는 것처럼* 작성됨. 이는 **잘못**:

- **On $\Sigma_{T8}^{(k)}$** ($d=0$): $\mu = 0$ exact. *True Goldstone*. Pure Brownian, linear unbounded growth (a measure-zero stratum 위에서만).
- **Near $\Sigma_{T8}$** ($d > 0$): $\mu_2 > 0$ small but positive. *Near-soft Fiedler mode*, **NOT Goldstone**. OU process, variance saturates at $T_*/\mu_2$.

두 statement 는 *coexist 불가* — different parameter regimes. **Correction**: §3 (F2) statement 에 "Fiedler mode" 또는 "near-soft mode" 로 명시 (NOT "Goldstone"). §2 (F1B) statement 는 *strict on-stratum* (measure-zero) 한정.

### §13.2 Critical Finding C2 — Dimensional/Scaling Error in $c_G$ (HIGH confidence)

**문제**: Lemma 2.4 statement "$\mu_2 \geq c_G \cdot d$" assumes **linear** scaling. Morse-Bott normal form near non-degenerate critical submanifold typically gives **quadratic** scaling:
$$\mu_2 \asymp d^2$$
(Hessian eigenvalue ~ $d^2$, not $d$, near a generic Morse-Bott manifold).

**결과**: $\tau_d = 1/(2 c_G \mu_2) \asymp 1/d^2$, NOT $1/d$. **Theorem F4 의 falsification threshold 변경 필요**: $d \in \{0.01, 0.03, 0.1, 0.3, 1.0\}$ scan 에서 $\tau_d$ ratio 가 $1/d^2$ scaling 으로 검증.

**Correction**: §3.1 Lemma 1.1 statement 수정 — explicit Morse-Bott normal form 계산 필요. 결과가 $d^2$ scaling 이면 *Cor. 7.1 (distance-Poincaré gap)* 도 $\lambda_1 \geq c_G d^2$ 으로 정정.

### §13.3 Critical Finding C3 — Universality Class Misclassification (HIGH confidence)

**문제**: SCC 에너지 = double-well $W(u) = u^2(1-u)^2$. 이는 **Allen-Cahn / Model A** (Hohenberg-Halperin classification), **NOT** Edwards-Wilkinson:

- Spinodal interior $c \in I_{sp}$: $W''(c) < 0$ — **unstable linearization** (mass NOT positive). Calling "massive EW" with $m_{eff} = \beta W''(c) > 0$ is **wrong direction**.
- 안정 well ($u \to 0$ 또는 $u \to 1$): $W''(0) = W''(1) = 2 > 0$. *Stable linearization*, EW-like.
- 장기 거동 in spinodal: **coarsening** $L(t) \sim t^{1/2}$ (Model A), driven precisely by $W'''$ which Agent 1 dismissed as "RG-irrelevant".

**Cubic RG argument 오류**: cubic vertex $u^3$ 의 upper critical dim is $d_c = 6$ (not 4). For Model A (quartic stable potential), upper critical dim is $d_c = 4$. Naive power-counting at Gaussian fixed point misses the **Wilson-Fisher fixed point** controlling Ising-class transition. $W'''(c) = 12(2c-1) \neq 0$ is **relevant** in $d \leq 6$, selects symmetry-breaking.

**Correction**: §2 (F1) universality assignment downgrade:
- Stable-well linearization (near $u = 0, 1$): EW class ✓
- Spinodal interior (near $u = c$): **Model A / Allen-Cahn coarsening** class
- Long-time SCC dynamics in spinodal regime: $L(t) \sim t^{1/2}$ coarsening, NOT pure diffusion

### §13.4 Critical Finding C4 — Skorokhod Reflection Ignored (HIGH confidence)

**문제**: 4 theorems 전부 boundary local time $K_t$ on $\partial(\Sigma_m \cap [0,1]^n)$ 무시. 결과적으로:
- Goldstone linear-in-$t$ variance $2T_*kt$ **bounded by polytope diameter** $\to$ statement **wrong for large $t$**.
- T-PF-A1-SDE Cat A 에는 reflection 포함 (Lions-Sznitman 1984), 본 file 의 OU reduction 은 reflection 무시한 *approximation*.

**Correction**: 모든 statement 에 *interior regime* hypothesis 추가 ($u_i \in (\epsilon, 1-\epsilon)$ for all $i$, with $\epsilon$ uniform). exit time bound $\mathbb{P}[\tau_\partial < \tau_d]$ 의 explicit 처리 필요 — 현재 sketch level only.

### §13.5 Major Findings (M1-M4)

- **M1 (Codim arithmetic)**: $D_f^{(k)} = (n-1) - k$ for $k=0$ gives $n-1$ = whole ambient, *clearly wrong*. **Correction**: distinguish $\dim(\text{level set})$ vs. $\dim(\text{singular locus})$ vs. $\dim(\Sigma_{T8}^{(k)})$. Need explicit Morse-Bott normal form re-derivation.
- **M2 ($z=\infty$ abuse)**: Massive transverse mode has finite correlation length, $z$ *undefined* (no diverging scale). **Correction**: replace with "exponential approach to saturation" not "$z = \infty$".
- **M3 (Mixing-crossover identity)**: only valid in convex-well; multi-well metastability gives exponentially larger $\tau_{\mathrm{mix}}$. **Correction**: restrict claim to single-basin regime.
- **M4 (Protocol basin-hopping)**: Langevin at $T_* > 0$ crosses saddles; exp-Fractal-2 must avoid contamination via short-time observation (Lyapunov time of basin).

### §13.6 *Strongest Surviving Synthesis Statement* (Cat B honest)

> *In the interior linearized regime near a non-degenerate critical point $u^*$ of $\mathcal{E}$ on $\Sigma_m$, away from $\partial(\Sigma_m \cap [0,1]^n)$ and **outside the spinodal interval** (i.e., at stable wells $u^* \approx 0$ or $u^* \approx 1$), SCC reflected Langevin dynamics is approximated by a finite-dimensional Ornstein-Uhlenbeck process with covariance matrix determined by $\mathrm{Hess}\,\mathcal{E}(u^*)\vert _{T_{u^*}\Sigma_m}$.*
>
> *Variance of each mode $k$ saturates at $T_*/\mu_k$ on timescale $1/\mu_k$. Off-stratum soft modes (near but not on $\Sigma_{T8}^{(k)}$) inherit small positive curvature; their crossover time diverges as the stratum is approached, with scaling exponent determined by the Morse-Bott normal form (to be computed — likely $\mu_2 \asymp d^2$ giving $\tau_d \asymp 1/d^2$).*

이 statement 가 **honest Cat B** — 4 critical findings 모두 회피, surviving content 만 보존.

### §13.7 Cat Status 재평가 (정직)

| Claim | 이전 (낙관) | 정정 (정직) |
|---|---|---|
| F1 — SCC = massive EW (bulk) | Cat B linearized | **Cat C, restrict to stable wells only** |
| F1 — Allen-Cahn coarsening 부재 | (가정) | **잘못, 명시적으로 인정** |
| F1 — cubic RG-irrelevant | Cat C heuristic | **잘못, Wilson-Fisher fixed point 작동** |
| F2 — $\tau_d = 1/(2 c_G d)$ | Cat B target | **Cat C, Morse-Bott $d^2$ scaling 재도출 필요** |
| F2 — universal collapse | Cat B target | Cat B (form is right, just need correct $\mu_2(d)$) |
| F3 — $D_f^{(k)} = (n-1)-k$ | Cat C | **Cat D, codim 산수 잘못 — 재도출 필요** |
| F4 — protocol | Cat B | Cat B (protocol structure OK, but **falsification thresholds 정정 필요**) |
| Master Theorem | Cat C synthesis | **Cat D, 4 critical findings 통합 후 재작성 필요** |

**Total downgrade**: 모든 claim 1-2 등급 하향. *진짜 Cat B-survivable 1개* (F2 universal collapse with corrected $\mu_2$).

### §13.8 Next Mathematical Work (정정된 priority)

**Priority 1A (긴급)** — Morse-Bott normal form 계산:
$\mu_2(d)$ 의 *correct* scaling 도출. $\mu_2 \asymp d$ 인지 $d^2$ 인지 결정 — 이게 모든 distance-controlled statement 의 결정자.

**Priority 1B** — Allen-Cahn coarsening vs Edwards-Wilkinson 의 SCC 에서의 *정확한 regime* 식별:
- *어디서* 단순 diffusion (EW)
- *어디서* coarsening (Allen-Cahn)
- 둘 사이 crossover scale

**Priority 1C** — Skorokhod reflection 처리:
- interior regime hypothesis 명시 + exit time bound
- 또는 Tanaka formula 로 boundary local time 포함

**Priority 2** — 정정된 numerical protocol:
- exp-Fractal-2 with $\mu_2 \asymp d^2$ scaling hypothesis
- exp-Fractal-1 with corrected $D_f$ formula
- exp-Fractal-3 distinguish EW vs Allen-Cahn vs Model B regime

### §13.9 본 critic pass 의 *의미*

> **Critic 가 발견한 4 critical findings 가 보여주는 것**:
> 1. *Naive analogy import 의 위험* — manifold topology 의 universality class machinery 를 SCC 에 직접 적용 시 SCC 의 *특수한 구조* (compact polytope, double-well, simplex constraint) 무시 가능성.
> 2. *CN10 disclosure 의 중요성* — analogies vs instantiations 의 구분.
> 3. *Adversarial verification 의 필수성* — 4 specialist agents 의 *수렴된 결과* 도 critic pass 없이는 *systematically biased* 가능.
>
> 본 critic pass 가 *production canonical* 진입 전에 *진짜 잘못* 들 (Wilson-Fisher 무시, Allen-Cahn vs EW 혼동, Goldstone 의미 conflation) 을 catch 했음. **이게 working layer 의 존재 이유** — canonical 보호 barrier 가 작동.

### §13.10 *진짜 진전* 의 재정의

본 session 의 *진짜 산출물* (critic 후):

1. **6-Type taxonomy** 의 *프레임* (Type F 추가 자체는 유효, 단 statements 는 재작성)
2. **Theorem F2 universal collapse $\tilde\sigma^2 = 1 - e^{-\tilde t}$** — form 은 Cat B-survivable (correct $\mu_2(d)$ 후)
3. **4 critical findings 자체** — *진짜로 catch 한 잘못들* 이 향후 작업의 *반드시 수정 항목* 으로 명시됨
4. **Critic + 4-agent 의 *systematic pipeline* 작동 확인** — adversarial verification 이 *production canonical 보호* 의 결정적 단계임 증명

본 file 의 §1-§12 는 ***잘못된 statements 의 archive*** 로 retain (silent OP resolution 회피, 실수의 명시적 기록). 정정 작업 = 별도 next-session.

---

*End of working file v0. Critic pass complete; 4 critical findings catalogued in §13. Status: working draft, requires major revision (Priority 1A-C) before any promotion attempt. Companion: manifold_topology_attempt_v0.md (W8-Day3 prior synthesis). Next session entry: §13.8 Priority 1A — Morse-Bott normal form for $\mu_2(d)$.*
