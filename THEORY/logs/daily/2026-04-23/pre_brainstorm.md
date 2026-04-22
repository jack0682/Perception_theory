# pre_brainstorm.md — 2026-04-23 Session Pre-brainstorm

**Purpose:** Open-ended mathematical hypothesis exploration before plan execution.
**Reference state:** 2026-04-22 R22 post-session — F1-SSU-v5, Formation Quantization, Three-Layer Hierarchy established.
**Thinking mode:** Wide exploration, multiple perspectives, no premature convergence.

---

## §1. 수학적 함수 관점 (G2 preparation)

### 1.1 SCC에 나타나는 transition 현상들

**목록**:
1. K-sector selector (Heaviside-like step at protocol-transition β)
2. Within-basin K̂ shift (smooth gradient flow outcome)
3. Energy E(β) within each branch (monotone smooth)
4. Basin escape rate at T > 0 (exponential in inverse temperature)
5. Bistable region width (stochastic flicker near transition)
6. Shape profile transition (p 1 → 5+ across α threshold)
7. Cubic term sign flip (algebraic, 1st order in c-1/2)

### 1.2 Function classes 후보

#### A. 급격한 logarithm — **divergent behavior**

$$f(\beta) = \log\!\left(\frac{\beta^* - \beta}{\beta^* - \beta_0}\right)$$

- Divergent as β → β*
- Natural for **escape time / nucleation barrier**: $\tau \sim \exp(\Delta\mathcal{F}/T) \sim \exp\!\log(\ldots)$
- Connection: Kramers rate $\ln \tau$ = linear in $\Delta\mathcal{F}/T$
- **가설 (H-log-1)**: Basin escape time in SCC at finite T follows $\tau_{K \to K+1}(\beta, c, T) \sim \exp\!\left[\Delta\mathcal{F}(\beta, c)/T\right]$ — standard Kramers form

#### B. Logistic sigmoid — **bounded crossover**

$$f(\beta) = \sigma(\kappa(\beta - \beta^*)) = \frac{1}{1 + e^{-\kappa(\beta - \beta^*)}}$$

- Bounded $\in [0, 1]$
- Smooth S-curve
- **가설 (H-log-2)**: Transition probability $P(K=k+1 | \beta)$ at protocol-bistable region is logistic:
$$P(\text{escape to } k+1 | \beta) = \sigma\!\left(\kappa(\beta - \beta_{K \to K+1}^*)\right)$$
- $\kappa$ sharpness = function of noise $\sigma$ and basin geometry

#### C. Tanh with asymptotes — **bounded with saturation**

$$f(s) = \tanh(s/\xi)$$

- $|f| \to 1$ as $|s| \to \infty$
- **Spatial profile** of formation: $\phi_k^*(r) = \frac{1}{2}(1 - \tanh((r - r_0)/\xi_0))$ — 이미 Cat A (Cor 2.2)
- **가설 (H-tanh-1)**: Step decomposition의 $\phi_k^*$는 **universal tanh** in supra-lattice regime (α ≥ 20) per X2 D1 — 이미 확인됨

#### D. Heaviside step — **discrete**

$$f(\beta) = H(\beta - \beta^*)$$

- Discrete jump
- **가설 (H-step-1)**: Protocol selector $s_\pi(\beta)$는 **piecewise constant integer** with discrete jumps at protocol-specific transitions. 이는 landscape 자체가 아니라 protocol's basin-selection의 property.
- X1 V5 hysteresis에서 확증됨

#### E. Softmax — **stochastic basin distribution**

$$P_k(\beta) \propto e^{-E_k^*(\beta)/T_{\mathrm{eff}}}$$

- **가설 (H-softmax-1)**: 유한 noise에서 protocol이 bistable region (selector transition 근처)에 있으면, basin $k$ 선택 probability가 **effective thermal softmax**:
$$P_\pi(\widehat K = k | \beta) = \frac{e^{-E_k^*(\beta)/T_{\mathrm{eff}}(\pi, \sigma)}}{\sum_j e^{-E_j^*(\beta)/T_{\mathrm{eff}}(\pi, \sigma)}}$$
- Noise $\sigma \to 0$에서 deterministic 극한 (Heaviside); $\sigma$ 증가하면 softmax spread 증가
- **R20 β=9 range 1-7 bistable**은 이 framework의 empirical signature일 수 있음 — 단, V7 P1에서 basic softmax는 refuted, more careful formulation 필요

#### F. Power law — **scale invariance**

$$f(\beta) = A \cdot (\beta - \beta^*)^\gamma$$

- Near critical point
- **가설 (H-power-1)**: Near $\beta \to \beta^*_c$ (critical point), formation size $r_0 \sim (\beta - \beta_c)^{-\nu}$ with some exponent $\nu$
- Connection: Landau-Ginzburg mean-field critical exponents

#### G. Rational / algebraic — **static structure**

$$\nu_k(c) = -\gamma_D(c)[2 + c(1-2d_0(c))\kappa_D p_k]$$

- Polynomial in algebraic functions of c
- **가설 (H-alg-1)**: 모든 **static** (Layer 3) observables은 algebraic/rational functions of parameters. **Dynamic** (Layer 1, 2) observables은 sigmoid/step/exponential families.

### 1.3 현상 ↔ 함수 class 매핑

이게 G2 deliverable의 중심 table:

| SCC 현상 | Function class | 대응 Layer |
|---|---|---|
| K-sector selector $s_\pi(\beta)$ | Heaviside step (H-step-1) | Layer 1 |
| Within-basin $\widehat K$ shift | Logistic/tanh (H-log-2) | Layer 2 |
| Energy $E_{\mathrm{branch}}(\beta)$ | Linear/polynomial smooth | Layer 2 |
| Basin escape time $\tau(T)$ | 급격한 log (H-log-1) | Layer 1 → Layer 0 (new?) |
| Bistable region stochastic | Softmax (H-softmax-1) | Layer 1 thermal smoothing |
| Shape profile $\phi_k^*(r)$ | Tanh (H-tanh-1) | Layer 3 |
| $\nu_k(c)$ | Rational (H-alg-1) | Layer 3 static |

---

## §2. Single → Multi Extension (G3 preparation)

### 2.1 핵심 질문

"Formation Quantization이 single-formation (K=1) case에서 확증됨. K≥2의 경우는?"

### 2.2 탐구 경로들

#### Path α — **Direct extension via K-sector basin**

Layer 1 basin structure $\Sigma_m = \bigsqcup_K \mathcal{B}_K$에서 각 $\mathcal{B}_K$ 내부:

$$u^*_K = \sum_{k=1}^K \phi_k^* \quad (k\text{-th formation)}$$

- **가설 (H-multi-1)**: 각 K-sector $\mathcal{B}_K$는 "K-formation manifold"로 자연스럽게 분해. 각 $\phi_k^*$는 single-formation 이론 (tanh soliton)과 **동일한 구조** — 단지 center 위치와 size만 다름.
- K-sector 내에서: geometric parameters $r_0(K), \xi_0, d_{\min}(K)$ 계산 가능
- $K$가 mass conservation $\sum |A_k^*| = m = cn$에 의해 제약됨

#### Path β — **Multi-formation moduli space $\mathcal{M}_K$**

$$\mathcal{M}_K(\beta, c, G) = \{(A_1^*, \ldots, A_K^*) : \sum |A_k^*| = m\} / \mathrm{Aut}(G)$$

- Configuration space of K disjoint subsets modulo graph symmetry
- Dim $\mathcal{M}_K \sim K \cdot \dim(\text{location space}) - \text{constraint}$
- **가설 (H-multi-2)**: On 2D grid with K formations of size $r_0 \sim \sqrt{m/(\pi K)}$, $\mathcal{M}_K$ dimension $\approx 2K - K$ (positions) minus constraints from mass and non-overlap.

#### Path γ — **Inter-sector transitions (K=k → K=k+1)**

- Basin escape via saddle-node or pitchfork
- **가설 (H-multi-3)**: $\mathcal{B}_k \to \mathcal{B}_{k+1}$ transition은 **nucleation of new formation** via barrier crossing. Rate: $\tau^{-1}_{k \to k+1} \sim \exp(-\Delta\mathcal{F}_{\mathrm{nuc}}/T)$
- $\Delta\mathcal{F}_{\mathrm{nuc}}$ = nucleation barrier = energy of critical nucleus configuration
- Classical nucleation theory analog

#### Path δ — **Pair interaction (K=2 starting point)**

$H_{\mathrm{Hessian}}$ at $u_K^* = \phi_1^* + \phi_2^*$:
- Block-diagonal structure (per-formation internal modes)
- Off-diagonal $\mu_{\mathrm{sep}}$ coupling (screened Poisson, $\sim e^{-d_{\min}/\xi_0}$)
- **가설 (H-multi-4)**: K=2 case에서 $\mu_{\mathrm{sep}} > 0$ condition이 metastability 결정 (이미 R12 Cat A). 확장: K≥3에서 K·K pair matrix의 positivity condition.

#### Path ε — **Landau free energy F(K, β, c)**

$$F(K; \beta, c, G) = K \cdot F_{\mathrm{single}}(r_0(K), \xi_0) + \binom{K}{2} \cdot F_{\mathrm{pair}}(d_{\min}(K))$$

- **가설 (H-multi-5)**: Effective landscape over K is Landau-like:
  - $F_{\mathrm{single}}$: single formation's isoperimetric cost, $\sim \xi_0 \cdot \mathrm{Per}(A_1^*) \sim \xi_0 \sqrt{m/K}$
  - $F_{\mathrm{pair}}$: inter-formation repulsion, $\sim e^{-d_{\min}/\xi_0}$
  - Optimal $K^*$ minimizes $F(K)$ → gives natural prediction of $\widehat K$

이건 **Conjecture 2.1의 refined version** — Landau-level, not naive Weyl-count.

### 2.3 Connection between Single-formation and Multi-formation

Formation Quantization이 이미 **bridge**:
$$u^*(x) = \sum_{k=1}^{K(u^*)} \phi_k^*(x) + r(u^*)$$

- Single formation ⇔ K=1 sector
- Multi-formation ⇔ K≥2 sectors
- 각 sector의 internal structure는 **single-formation theory로 다룸** (per-basin analysis)
- Inter-sector relationships는 **graph geometry + pair interaction**

이건 "multi-formation as family of single-formation theories" 관점.

---

## §3. Time Evolution Theory (G4)

### 3.1 기본 질문

"Static landscape는 알았는데, gradient flow dynamics는 어떻게 되는가?"

### 3.2 Sharp interface dynamics (step limit)

#### Motion by curvature

$\beta \to \infty$에서 formations become sharp ($\phi_k^* \to \chi_{A_k^*}$). Dynamics: boundary $\partial A_k$가 curvature-driven motion:
$$v_n(x) = \alpha \kappa(x)$$

- $v_n$: normal velocity of boundary
- $\kappa$: signed mean curvature
- Standard mean-curvature flow (MCF) on graph analog

**가설 (H-time-1)**: Sharp-interface limit of SCC는 graph-MCF와 일치. Continuous limit이 standard MCF 재현.

#### Coarsening (LSW)

Multi-formation의 대규모 t → ∞ behavior:
- Small formations shrink (boundary tension driven)
- Large formations grow
- Characteristic scale $\langle r \rangle \sim t^{1/3}$ (Ostwald ripening)

**가설 (H-time-2)**: SCC long-time behavior는 Lifshitz-Slyozov-Wagner (LSW) coarsening을 graph-adapted form으로 따름. $\widehat K(t) \sim t^{-\alpha}$ for some graph-topology-dependent exponent α.

### 3.3 Allen-Cahn PDE (finite $\beta$)

$$\partial_t u = -\frac{\delta \mathcal{E}}{\delta u}\bigg|_{\Sigma_m}$$

- Gradient flow on constrained simplex
- Linear stability around $u_{\mathrm{uniform}}$ → Prop 1.3a/b (already Cat A)
- Saturation: $u \to u^*$ in basin of attraction

**가설 (H-time-3)**: Gradient flow의 attractor는 K-sector determined by Fiedler cone's alignment (X1 V5 주제). Flow trajectories이 고차원 phase space에서 어떤 geometry를 형성하는가는 open.

### 3.4 Nucleation rate (K=0 → K=1 transition)

- Barrier height: critical nucleus energy $\Delta\mathcal{F}_c$
- Saddle point of $\mathcal{E}$ on path from $u_{\mathrm{uniform}}$ to $u^*_{K=1}$
- Kramers rate: $\tau^{-1} \sim \exp(-\Delta\mathcal{F}_c/T)$

**가설 (H-time-4)**: Near $\beta_{\mathrm{crit}}^{(2)}$, nucleation rate exponent:
$$\ln \tau^{-1} \sim -(\beta - \beta_{\mathrm{crit}}^{(2)})^{\gamma}$$
with $\gamma$ depending on spatial dimension.

---

## §4. Stochastic / Thermal Extensions (G5)

### 4.1 Langevin dynamics

$$du_x = -\nabla \mathcal{E}(u)_x\, dt + \sqrt{2T}\, dW_x$$

- Standard thermal fluctuation around gradient flow
- Invariant measure: $\mu(u) \propto e^{-\mathcal{E}(u)/T}$ (Gibbs) — but on constrained $\Sigma_m$
- **가설 (H-therm-1)**: At $T > 0$, invariant measure over $\Sigma_m$:
$$\mu_T(u) = \frac{1}{Z(T)} e^{-\mathcal{E}(u)/T} \cdot \delta(\Sigma u - m)$$

### 4.2 Basin occupation probability at equilibrium

$$P_T(\mathcal{B}_k) = \int_{\mathcal{B}_k} \mu_T(u)\, du \approx e^{-E_k^*/T} / \sum_j e^{-E_j^*/T}$$

- **Boltzmann softmax** at equilibrium
- Protocol의 gradient-flow endpoint는 **non-equilibrium** distribution; finite T Langevin equilibrium은 다름

**가설 (H-therm-2)**: Under slow annealing protocol (slowly decreasing T), SCC reaches Boltzmann equilibrium → lowest-energy basin selected. 이건 **annealed protocol**의 characterization.

### 4.3 Kramers escape time between basins

$$\tau_{k \to k'} = \tau_0 \cdot e^{\Delta\mathcal{F}_{kk'}/T}$$

- Basin $k \to k'$ escape time
- $\Delta\mathcal{F}_{kk'}$: barrier height on minimum-energy path
- $\tau_0$: attempt frequency (microscopic timescale)

**가설 (H-therm-3)**: $\Delta\mathcal{F}_{kk'}$는 K=k → K=k+1 transition에서 **nucleation barrier**; K=k → K=k-1에서 **merger barrier**; 서로 다른 scale.

### 4.4 Layer 1 selector smoothing

**가설 (H-therm-4)**: Heaviside selector $s_\pi(\beta)$ is **sharp at T=0**; at T>0, it becomes **sigmoid-smeared** with effective width $\propto T^\gamma$ (some exponent γ). 이게 R20 β=9 bistable observations의 설명.

### 4.5 Stochastic softmax formalization

각 β에서 basin $k$ 선택 확률:
$$P_\pi(\widehat K = k | \beta) = \frac{e^{-E_k^*(\beta)/T_{\mathrm{eff}}(\pi)}}{\sum_j e^{-E_j^*(\beta)/T_{\mathrm{eff}}(\pi)}}$$

- $T_{\mathrm{eff}}(\pi)$ = protocol's effective temperature
- Fiedler-init at small $\sigma$: $T_{\mathrm{eff}} \to 0$ (deterministic)
- Random-init at large $\sigma$: $T_{\mathrm{eff}}$ large (thermalized)

**가설 (H-therm-5)**: $T_{\mathrm{eff}}(\pi)$는 protocol-specific quantity, measurable via bistable region width.

---

## §5. Application Layer (G6)

### 5.1 Cognitive perception

SCC를 knowing/perception theory로 해석:

- **Object formation**: 연속 감각 input에서 discrete object 추출 = Formation Quantization
- **K = number of objects observed** — integer quantum
- **Protocol = attention state** (어느 level of detail, 어느 spatial focus)
- **Thermal extension**: attention noise, distraction
- **Coarsening**: gestalt grouping (small groups merge into larger)

**가설 (H-app-1)**: Cognitive perception의 "object count" (e.g., Miller's 7±2) is SCC's $\widehat K$ observable under specific protocol.

### 5.2 Image segmentation

SCC gradient flow on pixel graph:
- Input: image = cohesion values per pixel
- Output: segmented regions = K formations
- **Connection to established methods**: Chan-Vese (level set), Mumford-Shah (piecewise constant)

**가설 (H-app-2)**: SCC outperforms classical segmentation on graph-based (non-grid) domains where Allen-Cahn PDE framework breaks down.

### 5.3 Community detection

Social network / biological network:
- Graph G = network
- Cohesion field = community membership
- **K = number of communities**

**가설 (H-app-3)**: SCC with SBM graphs shows $\widehat K = K_{\mathrm{block}}$ (exact community recovery) under specific protocol.

### 5.4 Chemical / biological pattern formation

- **Turing patterns**: reaction-diffusion
- **Cahn-Hilliard phase separation**: block copolymers
- SCC with two-component (closure + separation) 결합 = hybrid

**가설 (H-app-4)**: SCC theory는 기존 pattern formation theories의 graph generalization. Bio-inspired neural network applications 가능.

---

## §6. 근본적 질문들 (deep)

### Q-D1: 왜 formation K는 integer인가?

**답 후보**:
- Topological (basin 구조의 connected components)
- Combinatorial (mass constraint의 integer-partition nature)
- **Emergence**: continuous field → discrete observable via **spontaneous symmetry breaking**

### Q-D2: 왜 SCC의 energy는 **3개 components** (cl, sep, bd)를 가지는가?

- Closure: stabilization tendency
- Separation: inter-formation repulsion
- Boundary: Allen-Cahn interface regularization
- 세 개 독립적이라는 canonical 공리가 SCC만의 특성. 다른 2-component theories (Cahn-Hilliard)와의 차이.

**가설 (H-D-1)**: 3-component energy structure이 Formation Quantization의 **필요조건**. 2-component theory는 discrete K 생성 못함.

### Q-D3: Protocol-dependence는 bug인가 feature인가?

오늘 관점: **feature**. Protocol-specific observable이 canonical의 richness.

**가설 (H-D-2)**: Protocol-dependence는 "observer effect"의 classical analog. 다른 observer (protocol)가 다른 observations (basin selection). 이는 SCC의 quasi-quantum character의 일부.

### Q-D4: F1-SSU-v5와 양자역학의 유사성?

- Discrete K = quantum number
- Protocol = measurement basis
- Basin selection = measurement outcome
- Noise / T > 0 = measurement uncertainty

**가설 (H-D-3)**: SCC는 "classical field theory with quantum-like discrete observables". Entirely classical dynamics이지만 observables의 structure가 quantum-like. Novel category.

---

## §7. 위험/주의사항

### Over-extrapolation 경계

- Formation Quantization은 C_1024 + 2D sq L=32,48에서 empirically 확증
- 다른 graph classes (torus, SBM, barbell, random)에서는 **미검증**
- Canonical에 얹기 전에 graph-class generalization 필요

### 함수 class overgeneralization

- "All transitions are sigmoidal" — **refuted** (오늘)
- 단순히 "sigmoidal and Heaviside" 대체 — 너무 단순
- **Each transition type has specific function class** — taxonomy 필요

### Multi-formation 확장의 complexity

- Pair interactions만 있을 줄 알았는데 triple/multi-body coupling 있을 가능성
- K=3 case에서 pair matrix가 entire landscape 결정하지 못할 수 있음

---

## §8. 내일 세션에서 explore할 핵심 hypothesis 요약

**우선순위 1 (G2)**:
- H-tanh-1, H-step-1 (이미 empirically 지원됨)
- H-log-2 (logistic for bistable transitions)
- H-softmax-1 (careful formulation after V7 P1 lesson)

**우선순위 2 (G3)**:
- H-multi-1 (K-sector basin decomposition)
- H-multi-5 (Landau free energy F(K))
- H-multi-3 (nucleation rate K→K+1)

**우선순위 3 (G4, G5, G6)**:
- H-time-1, H-time-2 (MCF + LSW)
- H-therm-4, H-therm-5 (Layer 1 smoothing at T > 0)
- H-app-1 (cognitive perception connection)

**Deep questions (수시로 돌아볼)**:
- Q-D1 (왜 K integer?)
- Q-D3 (protocol-dependence의 본질)
- Q-D4 (양자역학 유사성)

---

**End of pre_brainstorm.md for 2026-04-23.**
**Target: 수학적 다양성 + multi-extension + time/stochastic/application scoping을 단일 framework 아래로 수렴.**
