---
type: working/sensing_pipeline/stage1
version: v1
date: 2026-05-25
status: DEFINITION-DRAFT
purpose: |
  Stage 1 deep dive: photoreceptor transduction as marked-jump SDE.
  Develops the chemical cascade as Markov chain with full van Kampen
  system-size expansion, Pugh-Lamb ODE model with LNK reduction,
  the membrane SDE as Itô jump-diffusion with existence-uniqueness,
  single-photon gamma-function response derivation,
  Naka-Rushton from saturation kinetics with Hill exponents,
  slow-fast SDE adaptation, Weber-Fechner exact derivation,
  Volterra K_2 computation, dark current derivation,
  Poisson thinning proof, Fokker-Planck stationary distribution,
  explicit K_1 conditional law, empirical parameter table.
  Registers TC-SP-1.4, TC-SP-1.5, OP-SP-002.
register: DEFINITION-DRAFT + THEOREM-CANDIDATE (no proofs)
parent: 01_framework_master
prev_stage: 02_stage0_photon_point_process
constraint_compliance:
  canonical_theorem_changes: 0
  scc_edits: 0
---

> [!nav] Parent: [[00_INDEX]] · Prev: [[02_stage0_photon_point_process]] · Next: [[04_stage2_inner_retinal_algebra]]

# Stage 1 — Photoreceptor Transduction (SDE)

## 0. 본 문서의 위치

본 문서는 SSKP 의 두 번째 kernel $\mathcal{K}_1 : \mathcal{S}_0 \to \mathcal{S}_1$ — *광자 도래 점과정 → 광수용기 graded 막전위* 의 변환을 정식화한다. 본 문서가 끝나면:

- 광수용기 막전위 $V_p(t)$ 의 SDE 형식 (jump-diffusion, Itô 의미)
- van Kampen system-size expansion 의 전개 (master equation → Fokker-Planck)
- Pugh-Lamb 활성화 모델의 명시적 ODE + LNK 축약
- 단광자 응답 $r_1(t)$ 의 gamma-function 유도
- Naka-Rushton 비선형 압축의 포화 동역학 유도
- $I_{50}$ 슬라이딩의 slow-fast SDE 분석
- Weber-Fechner 도출의 정확한 계산
- $K_2$ Volterra kernel 의 명시적 계산
- dark current $J_{\text{dark}}$ 의 cGMP 채널 유도
- Poisson thinning 정리의 증명 (type 분기의 수학적 기초)
- Fokker-Planck 정상 분포 계산 (Ornstein-Uhlenbeck 경우)
- $\mathcal{K}_1(N, \cdot)$ 의 조건부 법칙의 명시적 형식
- Rod/cone 실험적 파라미터 표 (rat, monkey, human)

이 다음 문서의 입력으로 노출된다.

본 문서가 *수행하지 않는 것*: ON/OFF 분기, 측방 억제 (→ [[04_stage2_inner_retinal_algebra|04]]); 스파이크 부호화 (→ [[05_stage3_ganglion_spike_encoding|05]]).

---

## 1. 상태공간 $\mathcal{S}_1$

### 1.1 정의

광수용기는 망막 위 *유한 격자* 또는 *연속 배치* 로 modeling 가능. 본 디렉토리는 연속 배치 (Polish space 의 closure 를 유지) 를 default.

$$
\boxed{\mathcal{S}_1 := C\big( \Sigma_{\text{ret}} \times \mathbb{R}^+, \, \mathbb{R} \big)}
$$

$V \in \mathcal{S}_1$ 는 시공간 함수 $V(x, t)$: 위치 $x$ 의 광수용기의 시각 $t$ 막전위.

**Note (이산 vs 연속)**: 실제 망막은 $\sim 1.3 \times 10^8$ 개의 이산 광수용기. 연속 표현은 모델링 편의 — 격자 spacing 보다 큰 스케일의 결과는 동일.

**Note (Type 분리)**: 광수용기는 rod / L-cone / M-cone / S-cone 4 종. 본 문서에서는 단일 type 의 SDE 를 먼저 정의 후 §6 에서 type-specific 일반화.

### 1.2 위상

$\mathcal{S}_1$ 의 σ-algebra 는 *uniform topology on compacts* 의 Borel σ-algebra. 즉, 임의의 compact $K \subset \Sigma_{\text{ret}} \times \mathbb{R}^+$ 에 대해 $\sup_K |V - V'|$ 가 측정 가능.

이는 Polish ([[01_framework_master#1.1 상태공간의 일반 형태|01 §1.1]] 가정 G1 만족).

---

## 2. 광변환 캐스케이드 (Markov chain layer)

### 2.1 분자 단계 — Pugh-Lamb 활성화 모델

광자 흡수에서 막전위 변화까지의 분자 chain (Pugh & Lamb 1993; Lamb & Pugh 2006 기준):

```
Photon + Rh (rhodopsin)  →  Rh* (active)
Rh* + G_t (transducin)  →  Rh* + G_t* (GTP-형태)
G_t* + PDE (phosphodiesterase)  →  PDE* (active)
PDE* + cGMP  →  5'-GMP  (hydrolysis, rate k_cat)
GTP-cyclase  →  cGMP  (synthesis, rate alpha_dark)
cGMP-gated channel: closed by falling [cGMP]
```

각 단계는 first-order (또는 pseudo-first-order) Markov 전이로 모델 가능. 명시적 coupled ODE 계:

$$
\frac{d[R^*]}{dt} = \nu_R \cdot \phi(t) - k_{R^*}[R^*]
$$

$$
\frac{d[T^*]}{dt} = k_{\text{tr}} [R^*] (G_{T,\text{total}} - [T^*]) - k_{T^*}[T^*]
$$

$$
\frac{d[\text{PDE}^*]}{dt} = k_{\text{act}} [T^*] (\text{PDE}_{\text{total}} - [\text{PDE}^*]) - k_{\text{deact}}[\text{PDE}^*]
$$

$$
\frac{d[\text{cGMP}]}{dt} = \alpha_{\text{dark}} - \beta_{\text{dark}}[\text{cGMP}] - k_{\text{cat}}[\text{PDE}^*][\text{cGMP}]
$$

여기서:
- $\phi(t) = \sum_k \delta(t - t_k)$: 광자 흡수 사건 스트림 (stage 0 의 $dN_x$)
- $\nu_R$: 광자당 rhodopsin 활성화율
- $k_{R^*} \approx 20 \text{ s}^{-1}$: R* 비활성화율 (phosphorylation + arrestin; Lamb-Pugh)
- $k_{\text{tr}} \approx 3 \times 10^3 \text{ M}^{-1}\text{s}^{-1}$: transducin 활성화 2차 속도 상수
- $k_{T^*} \approx 1 \text{ s}^{-1}$: transducin 비활성화율 (GTPase)
- $k_{\text{act}}, k_{\text{deact}}$: PDE 활성화/비활성화 속도 상수
- $\alpha_{\text{dark}} \approx 40 \,\mu\text{M s}^{-1}$: 어둠에서 cGMP 합성율 (guanylate cyclase)
- $\beta_{\text{dark}} \approx 4 \text{ s}^{-1}$: cGMP hydrolysis 기저율
- $k_{\text{cat}} \approx 3000 \text{ s}^{-1}$ (per PDE): activated PDE 의 catalytic rate

**채널 전류**: cGMP-gated 채널은 전류 $J \propto [\text{cGMP}]^n$ (Hill; §4 에서 전개).

### 2.1.1 선형-비선형-동역학 (LNK) 축약

위 4-ODE system 의 quasi-steady-state (QSS) 축약 — transducin 과 PDE 의 활성화가 R* 보다 빠르다고 가정 ($k_{\text{tr}} G_T \gg k_{T^*}$, i.e., transducin 빠르게 saturate):

단계 1. R* 의 QSS: 단광자 사건 ($\phi = \delta(t)$) 에 대해 $[R^*](t) = \nu_R e^{-k_{R^*} t}$ (1차 선형 ODE 해).

단계 2. PDE* 의 선형 convolution: R* 가 T* 를 거쳐 PDE* 를 활성화. 낮은 copy number 극한에서:

$$
[\text{PDE}^*](t) = \nu_R \int_0^t h_{\text{PDE}}(t - s) [R^*](s) \, ds
$$

여기서 $h_{\text{PDE}}$ 는 T*-PDE 연결의 impulse response (지수 감쇠 형태).

단계 3. cGMP 동역학: PDE* 가 충분히 작다고 가정하면 ([cGMP] 의 비선형 term 이 1차):

$$
\frac{d[\text{cGMP}]}{dt} \approx \alpha_{\text{dark}} - \beta_{\text{dark}}[\text{cGMP}] - k_{\text{cat}}[\text{PDE}^*](t)[\text{cGMP}]_{\text{dark}}
$$

결합하면: **LNK 모델** = Linear filter (R* 응답) $\times$ Nonlinear gain (Hill function of cGMP) $\times$ Kinetics (막전류 → 막전위 ODE).

이 축약이 §3.2 의 gamma-function 단광자 응답의 이론적 토대.

### 2.2 Master equation

상태 변수 $\mathbf{n} = (n_{R^*}, n_{T^*}, n_{\text{PDE}^*}, n_{\text{cGMP}}, \ldots)$ 가 each molecular species 의 copy number.

Master equation (Chemical Master Equation, CME):

$$
\partial_t P(\mathbf{n}, t) = \sum_{\mathbf{n}' \neq \mathbf{n}} \left[ W(\mathbf{n} | \mathbf{n}') P(\mathbf{n}', t) - W(\mathbf{n}' | \mathbf{n}) P(\mathbf{n}, t) \right]
$$

여기서 $W(\mathbf{n}'|\mathbf{n})$ 은 단위 시간당 상태 $\mathbf{n} \to \mathbf{n}'$ 전이율. 반응 $\rho$ 의 propensity $a_\rho(\mathbf{n})$ 와 stoichiometry vector $\nu_\rho$ 로:

$$
W(\mathbf{n} + \nu_\rho | \mathbf{n}) = a_\rho(\mathbf{n})
$$

**반응 목록 (명시적)**:

| 반응 | propensity $a_\rho$ | 변화 $\Delta \mathbf{n}$ |
|------|---------------------|--------------------------|
| photon → R* | $\lambda(x, t)$ | $n_{R^*} \to n_{R^*} + 1$ |
| R* + T → R* + T* | $k_{\text{tr}} n_{R^*} n_T$ | $n_{T^*} \to n_{T^*} + 1$ |
| T* → T (GTPase) | $k_{T^*} n_{T^*}$ | $n_{T^*} \to n_{T^*} - 1$ |
| T* + PDE → T* + PDE* | $k_{\text{act}} n_{T^*} n_{\text{PDE}}$ | $n_{\text{PDE}^*} \to n_{\text{PDE}^*} + 1$ |
| PDE* → PDE | $k_{\text{deact}} n_{\text{PDE}^*}$ | $n_{\text{PDE}^*} \to n_{\text{PDE}^*} - 1$ |
| GTP → cGMP (cyclase) | $\alpha_{\text{dark}} \Omega$ | $n_{\text{cGMP}} \to n_{\text{cGMP}} + 1$ |
| cGMP + PDE* → 5'GMP | $k_{\text{cat}} n_{\text{cGMP}} n_{\text{PDE}^*} / \Omega$ | $n_{\text{cGMP}} \to n_{\text{cGMP}} - 1$ |
| R* 비활성화 | $k_{R^*} n_{R^*}$ | $n_{R^*} \to n_{R^*} - 1$ |

여기서 $\Omega$ 는 outer segment 의 *system size* (effective volume; 아래 van Kampen expansion 의 핵심).

### 2.3 van Kampen System-size Expansion — Chemical Langevin 유도

van Kampen (1981) 의 system-size expansion 은 분자 copy number 가 클 때 ($\Omega \gg 1$) CME 를 Fokker-Planck 로 조직적으로 근사하는 방법이다.

**단계 0. 농도 변수 도입**: 정수 copy number $n_i$ 를 *농도* $\phi_i = n_i / \Omega$ 로 치환. $\Omega$ 는 반응 volume (outer segment 의 경우 $\approx 10^{-14}$ L).

**단계 1. Omega expansion**: 각 종 $i$ 에 대해

$$
n_i = \Omega \phi_i + \Omega^{1/2} \xi_i
$$

여기서 $\phi_i(t)$ 는 결정론적 (thermodynamic limit 에서의 농도), $\xi_i(t)$ 는 *fluctuation* 으로 $O(1)$ 크기.

**단계 2. propensity 전개**: 반응 $\rho$ 의 propensity $a_\rho(\mathbf{n})$ 를 $\mathbf{n} = \Omega \boldsymbol{\phi} + \Omega^{1/2} \boldsymbol{\xi}$ 로 대입, Taylor 전개:

$$
a_\rho(\Omega \boldsymbol{\phi} + \Omega^{1/2}\boldsymbol{\xi}) = \Omega f_\rho(\boldsymbol{\phi}) + \Omega^{1/2} \sum_i \frac{\partial f_\rho}{\partial \phi_i} \xi_i + O(1)
$$

여기서 $f_\rho(\boldsymbol{\phi}) := a_\rho(\Omega \boldsymbol{\phi}) / \Omega$ 는 *macroscopic rate function* (propensity 를 volume 으로 나눈 것).

**단계 3. Master equation 에 대입 — leading order**:

$O(\Omega^0)$ 항을 모으면 $\boldsymbol{\phi}(t)$ 의 결정론적 방정식:

$$
\frac{d \phi_i}{dt} = \sum_\rho \nu_{\rho i} f_\rho(\boldsymbol{\phi})
$$

이게 *rate equation* (mass-action ODE). §2.1 의 coupled ODE 가 바로 이 leading order.

**단계 4. $O(\Omega^{-1/2})$ 항 — fluctuation equation**:

Fluctuation $\boldsymbol{\xi}(t)$ 의 방정식은 CME 에서 $O(\Omega^{-1/2})$ 항을 모으면:

$$
\frac{d\xi_i}{dt} = \sum_j A_{ij}(\boldsymbol{\phi}(t)) \xi_j + \eta_i(t)
$$

여기서

$$
A_{ij} = \sum_\rho \nu_{\rho i} \frac{\partial f_\rho}{\partial \phi_j}
$$

는 반응 Jacobian, 그리고 $\eta_i(t)$ 는 *Gaussian white noise* 로:

$$
\langle \eta_i(t) \eta_j(t') \rangle = D_{ij}(\boldsymbol{\phi}(t)) \delta(t - t')
$$

diffusion matrix:

$$
D_{ij}(\boldsymbol{\phi}) = \sum_\rho \nu_{\rho i} \nu_{\rho j} f_\rho(\boldsymbol{\phi})
$$

즉, *noise covariance 가 macroscopic rate 에 비례* — 분자 수가 클수록 (상대) fluctuation 이 작음.

**단계 5. Fokker-Planck 도출**:

위 Langevin equation $d\boldsymbol{\xi}/dt = A \boldsymbol{\xi} + \boldsymbol{\eta}$ 에 대응하는 *확률 분포* $\Pi(\boldsymbol{\xi}, t)$ 는 Fokker-Planck:

$$
\partial_t \Pi(\boldsymbol{\xi}, t) = -\sum_i \partial_{\xi_i} \left[ (A \boldsymbol{\xi})_i \Pi \right] + \frac{1}{2} \sum_{i,j} D_{ij} \partial_{\xi_i} \partial_{\xi_j} \Pi
$$

이것이 *leading-order Fokker-Planck* — CME 의 $\Omega \to \infty$ 극한.

**요약 도식**:

$$
\text{CME} \xrightarrow{\Omega \to \infty, \; n_i = \Omega \phi_i + \Omega^{1/2} \xi_i}
\begin{cases}
O(\Omega^0): & \dot{\boldsymbol{\phi}} = \sum_\rho \nu_\rho f_\rho(\boldsymbol{\phi}) \quad \text{(rate ODE)} \\
O(\Omega^{-1/2}): & d\boldsymbol{\xi} = A \boldsymbol{\xi} \, dt + \sqrt{D(\boldsymbol{\phi})} \, dW_t \quad \text{(Langevin)}
\end{cases}
$$

**Chemical Langevin Equation (CLE)**: 두 항을 합치면 (원래 변수 $\mathbf{n}$ 으로 돌아오면):

$$
\boxed{d n_i = \left(\sum_\rho \nu_{\rho i} a_\rho(\mathbf{n})\right) dt + \sum_\rho \nu_{\rho i} \sqrt{a_\rho(\mathbf{n})} \, dW_t^\rho}
$$

각 반응 $\rho$ 마다 독립 Wiener process $W_t^\rho$. 이게 Gillespie (2000) 의 CLE 의 van Kampen 유도.

**광변환에의 적용**: cGMP ($n_{\text{cGMP}}$) 의 경우, 합성 (rate $\alpha_{\text{dark}} \Omega$) + 가수분해 (rate $k_{\text{cat}} n_{\text{cGMP}} n_{\text{PDE}^*}/\Omega$) 로부터:

$$
d[\text{cGMP}] = \left(\alpha_{\text{dark}} - \beta_{\text{eff}}(t) [\text{cGMP}]\right) dt + \sqrt{\frac{\alpha_{\text{dark}} + \beta_{\text{eff}}(t)[\text{cGMP}]}{\Omega}} \, dW_t
$$

여기서 $\beta_{\text{eff}}(t) = \beta_{\text{dark}} + k_{\text{cat}} [\text{PDE}^*](t)$. 이 SDE 가 막전위 SDE (§3) 의 분자적 기초.

**Applicability condition**: CLE 는 각 종의 copy number 가 $\gtrsim 20–100$ 일 때 정확. cGMP: outer segment 에 $\sim 10^5$ 분자 (조건 만족). PDE: $\sim 10^3$ (경계). R*: 단광자 사건 → 최소 1개 (조건 불만족 → 여전히 jump 항으로 유지).

### 2.4 효과적 축소 — 광자 → 막전위

위 5–6 상태 cascade 의 quasi-steady-state 축약은 다음 effective relation:

$$
\frac{d V(x, t)}{dt} \approx -\frac{1}{\tau_V}(V - V_{\text{dark}}) + g_{\text{ph}} \cdot \lambda_{\text{absorbed}}(x, t) - \text{(nonlinear corrections)}
$$

여기서 $V_{\text{dark}}$ 는 어둠 막전위 ($\approx -40$ mV), $\tau_V$ 는 막 시상수, $g_{\text{ph}}$ 는 광자당 응답 진폭 (음수 — hyperpolarization).

§3 에서 이를 SDE 형태로 정확히.

---

## 3. 광수용기 SDE — Jump-Diffusion 정식화

### 3.1 핵심 SDE

광수용기 막전위 $V(x, t)$ 의 동역학:

$$
\boxed{dV(x, t) = -\frac{1}{\tau} \big( V(x, t) - V_{\text{rest}} \big) dt - g \cdot (r_1 *_t dN_x)(t) - h(V(x, t)) dt + \sigma_V dW_t(x)}
$$

각 항:

- **$-\tau^{-1}(V - V_{\text{rest}}) dt$**: 막 시상수 $\tau$ 로의 *수동적 이완* (passive relaxation) toward $V_{\text{rest}}$.
- **$-g \cdot (r_1 *_t dN_x)(t)$**: 광자 도래 jump 항. $r_1(t)$ 는 *단광자 응답 kernel*, $*_t$ 는 시간 합성곱, $dN_x$ 는 픽셀 $x$ 의 점과정 micro-event. 부호 *음* 임에 주의 — hyperpolarizing.
- **$-h(V) dt$**: Naka-Rushton 비선형 압축 (§4 에서 자세히).
- **$\sigma_V dW_t(x)$**: 열잡음 (Wiener process); 각 픽셀 독립.

이 SDE 는 *jump-diffusion type* — Poisson jump + Brownian diffusion.

### 3.1.1 Itô 의미의 정확한 해석

위 SDE 를 *Itô jump-diffusion* 의 표준 형식으로 적으면:

$$
dV_t = b(V_t) \, dt + \sigma_V \, dW_t + \int_{\mathbb{R}} c(V_{t^-}, z) \, \widetilde{N}(dt, dz)
$$

여기서:
- $b(V) = -\tau^{-1}(V - V_{\text{rest}}) - h(V)$: drift (연속 부분)
- $\sigma_V dW_t$: Wiener diffusion
- $\widetilde{N}(dt, dz) = N(dt, dz) - \Lambda_x(dz) dt$: *compensated* Poisson random measure
- jump 크기 $c(V_{t^-}, z) = -g \cdot r_1(0) \cdot \mathbf{1}_{|z| < \epsilon}(z)$ (단순화; 실제로는 $r_1$ kernel 이 jump 직후부터 convolution 을 시작)

**Itô 의 공식 (jump-diffusion 버전)**: $f(V_t)$ 에 대해

$$
df(V_t) = f'(V_t) b(V_t) dt + f'(V_t) \sigma_V dW_t + \frac{1}{2} f''(V_t) \sigma_V^2 dt + \int_\mathbb{R} [f(V_{t^-} + c(V_{t^-}, z)) - f(V_{t^-})] N(dt, dz)
$$

마지막 항이 *jump 의 비선형 기여*. $f(V) = V$ 의 경우 위 SDE 로 환원.

### 3.1.2 존재-유일성 정리 (Applebaum §6.2)

**Theorem 3.1 (Jump-diffusion 존재-유일성)**. 다음 조건 하에서 SDE (§3.1) 의 강해 (strong solution) 가 *존재*하고 *확률적으로 유일*하다:

**(H1) Linear growth**: $|b(V)| + |\sigma_V| \leq C(1 + |V|)$ for some $C > 0$.

**(H2) Lipschitz**: $|b(V) - b(V')| + |c(V, z) - c(V', z)| \leq L |V - V'|$ for $L$-독립.

**(H3) Square-integrability of jumps**: $\int_\mathbb{R} |c(v, z)|^2 \, \nu(dz) < \infty$ for all $v \in \mathbb{R}$, where $\nu$ is the Lévy measure of $N$.

**(H4) Initial condition**: $V_0$ 가 $\mathcal{F}_0$-가측이고 $\mathbb{E}[V_0^2] < \infty$.

**검증 (photoreceptor SDE 의 경우)**:
- (H1): $b(V) = -\tau^{-1}(V - V_{\text{rest}}) - h(V)$; $h(V)$ 가 bounded (Naka-Rushton 의 saturation) 이므로 linear growth 만족.
- (H2): $h$ 가 smooth 하고 $|h'|$ 가 bounded 이므로 Lipschitz. jump 크기는 $g \cdot r_1(0)$ (상수) → Lipschitz (trivially).
- (H3): Poisson process 의 Lévy measure 는 finite (jump 크기 $g r_1(0)$ 고정), $\int |c|^2 d\nu = \lambda_x \cdot (g r_1(0))^2 < \infty$.
- (H4): $V_0 = V_{\text{rest}}$ (결정론적 초기) → 만족.

**결론**: 조건 (H1)–(H4) 가 광수용기 SDE 에서 만족 → $\mathcal{K}_1$ 이 well-defined stochastic kernel (TC-SP-1.1 의 stage 1 측).

**Reference**: Applebaum, D. (2009). *Lévy Processes and Stochastic Calculus*, 2nd ed., §6.2 Theorem 6.2.3.

### 3.2 Single-Photon Impulse Response $r_1$ — Gamma-function 유도

**목표**: 단일 광자 흡수 후 막전위 응답 $r_1(t)$ 가 왜 gamma-function 형태인가를 n-stage filter cascade 로 유도.

#### 3.2.1 n-stage 지수 filter cascade

광변환 cascade 의 각 단계 (R*, T*, PDE*, cGMP, 막전류, 막전위) 를 *1차 low-pass filter* (RC 회로 아날로그) 로 모델:

$$
\tau_i \frac{d x_i}{dt} = -x_i + x_{i-1}(t), \quad i = 1, \ldots, n
$$

초기: $x_0(t) = \delta(t)$ (단광자 입력). 각 단계의 impulse response:

$$
h_i(t) = \frac{1}{\tau_i} e^{-t/\tau_i} \mathbf{1}_{t \geq 0}
$$

#### 3.2.2 Convolution의 반복 적용

Cascade 의 전체 impulse response 는 각 단계 $h_i$ 의 합성곱:

$$
r_1(t) = (h_1 * h_2 * \cdots * h_n)(t)
$$

**동일 시상수 경우** ($\tau_i = \tau$ for all $i$):

$$
r_1(t) = \left( \frac{1}{\tau} e^{-t/\tau} \right)^{*n} = \frac{1}{\tau^n (n-1)!} t^{n-1} e^{-t/\tau} \mathbf{1}_{t \geq 0}
$$

이는 *Gamma 분포의 pdf* (형상 모수 $n$, 스케일 모수 $\tau$):

$$
\boxed{r_1(t) = \frac{t^{n-1} e^{-t/\tau}}{\tau^n (n-1)!}, \quad t \geq 0}
$$

**유도 (귀납)**:

기저: $n = 1$: $h_1(t) = \tau^{-1} e^{-t/\tau}$. ✓

귀납 단계: $n \to n+1$ 의 합성곱:

$$
h^{*n} * h_1 = \frac{1}{\tau^n (n-1)!} \int_0^t s^{n-1} e^{-s/\tau} \cdot \frac{1}{\tau} e^{-(t-s)/\tau} ds = \frac{e^{-t/\tau}}{\tau^{n+1} (n-1)!} \int_0^t s^{n-1} ds = \frac{t^n e^{-t/\tau}}{\tau^{n+1} n!}
$$

Laplace transform 경유의 대안 증명: $\mathcal{L}\{h_i\}(s) = (1 + \tau s)^{-1}$, cascade 의 전이 함수는 $(1 + \tau s)^{-n}$, 역변환이 위 gamma pdf.

#### 3.2.3 Rod 실험치와의 매칭

Rod $r_1(t)$ 의 실험적 사실 (Baylor 1979; Lamb & Pugh 1992):

- Peak time $t_{\text{peak}} = \tau(n-1)$ (Gamma pdf 의 모드)
- Half-width at half-maximum (HWHM): $\sim 200$ ms (rod)
- $n \approx 4$–$6$ (cascade 단계 수)
- $\tau \approx 30$–$50$ ms

실험치 $t_{\text{peak}} \approx 100$–$200$ ms, $n \approx 5$: $\tau \approx 25$–$40$ ms. 이는 *rhodopsin 비활성화* ($k_{R^*}^{-1} \approx 50$ ms), *transducin 교환* ($k_{T^*}^{-1} \approx 200$ ms), *PDE 비활성화*, *cGMP 시상수*, *막 RC 시상수* 의 합으로 설명 가능.

**이질 시상수 경우** ($\tau_i$ 각각 다름): Laplace domain 에서

$$
\hat{r}_1(s) = \prod_{i=1}^n \frac{1}{1 + \tau_i s}
$$

이는 *partial fraction* 분해 → 각 극점에 exponential. $\tau_i$ 가 가깝지만 같지 않으면 gamma 에 근사; 비슷한 시상수들의 평균으로 $\tau_{\text{eff}}$ 를 정의 가능.

### 3.3 Poisson jump 항의 의미

$dN_x$ 는 stage 0 의 점과정 $N$ 을 픽셀 $x$ 에 *localize* 한 것:

$$
N_x(B) := N\big( (\{x\} \cap \Sigma_p) \times B \times \Lambda \big)
$$

여기서 $\Sigma_p$ 는 픽셀 $p$ 가 차지하는 absorption 영역. $dN_x$ 는 *integer-valued* random measure — 각 atomic 점에서 $+1$.

Jump term 의 정확한 의미: 광자 도래 사건이 일어날 때마다 $V$ 가 *순간적으로* $g \cdot r_1$ 의 형태로 perturb 됨. 사건들이 *겹치면* 합산 (linearity of $r_1$ for small responses).

### 3.4 Wiener 항의 정당화

$\sigma_V dW_t(x)$ 는 *열잡음* — 막 이온 채널의 stochastic gating, 분자 thermal motion. 픽셀 $x$ 마다 독립 Brownian motion (공간 독립; correlation length scale 이 픽셀 크기보다 작음).

크기 추정: $\sigma_V \sim 0.1$ mV per $\sqrt{\text{ms}}$ (single-photon response 진폭의 $\sim$ 10%).

§9.5 의 실험적 추정치 참조.

### 3.5 합성된 SDE — 정리

위 4 항을 합쳐 stage 1 의 *해석학적 마스터 SDE*:

$$
dV(x, t) = \underbrace{- \frac{1}{\tau}(V - V_{\text{rest}}) dt}_{\text{passive relaxation}} \underbrace{- g \, (r_1 *_t dN_x)(t)}_{\text{photon jump (hyperpolarizing)}} \underbrace{- h(V) dt}_{\text{adaptive compression}} \underbrace{+ \sigma_V dW_t(x)}_{\text{thermal noise}}
$$

이 SDE 가 $\mathcal{K}_1$ 의 generative model.

---

## 4. Naka-Rushton 비선형 압축

### 4.1 포화 동역학으로부터의 유도

Naka-Rushton 방정식을 *saturation kinetics* 에서 유도한다. 출발점은 cGMP-gated 채널의 전류.

**단계 1. cGMP-gated 채널 전류**:

cGMP 농도 $c = [\text{cGMP}]$ 에서 채널 전류:

$$
J_{\text{ch}}(c) = J_{\text{max}} \cdot \frac{c^n}{c^n + K_{\text{cG}}^n}
$$

이는 Hill 함수 ($n$ = Hill 지수, $K_{\text{cG}}$ = half-saturation cGMP 농도). Rod 에서 $n \approx 2$–$3$, $K_{\text{cG}} \approx 10$–$30 \,\mu\text{M}$ (Baylor 1987; Yau 1994).

**단계 2. 정상상태 cGMP**:

어둠에서 정상상태: $\alpha_{\text{dark}} = \beta_{\text{eff}} c_{\text{dark}}$, 즉 $c_{\text{dark}} = \alpha_{\text{dark}} / \beta_{\text{dark}}$.

빛 입력 $I$ (광자 flux) 로 인한 PDE* 활성화: $\beta_{\text{eff}} = \beta_{\text{dark}} + k_{\text{cat}}[\text{PDE}^*]$, 여기서 $[\text{PDE}^*] \propto I$ (낮은 intensity 선형 regime). 따라서

$$
c_{\text{ss}}(I) = \frac{\alpha_{\text{dark}}}{\beta_{\text{dark}} + \kappa I}
$$

$\kappa = k_{\text{cat}} \cdot (\text{PDE*-per-photon})$ 상수.

**단계 3. 막전위 응답**:

막전위 $V$ 는 $J_{\text{ch}}$ 에 비례 (ohmic approximation):

$$
V - V_{\text{dark}} = -R_{\text{m}} [J_{\text{dark}} - J_{\text{ch}}(c_{\text{ss}}(I))]
$$

여기서 $R_{\text{m}}$ 은 막 저항. 대입하면 (분자를 정리하면):

$$
R(I) := V_{\text{dark}} - V(I) = R_{\text{max}} \cdot \frac{I^n}{I^n + I_{50}^n}
$$

여기서

$$
I_{50} = \left(\frac{\beta_{\text{dark}}}{\kappa}\right) \cdot K_{\text{cG}}^{n/1} \cdot \frac{1}{c_{\text{dark}}^{n-1}}
$$

(정확한 표현은 $n$ 지수와 cGMP 농도 표현식으로부터).

이게 *Naka-Rushton equation* (Naka & Rushton 1966) — cGMP 포화 동역학의 자연스러운 결과.

### 4.1.1 Hill 지수의 실험적 값

| 측정 | 종 | $n$ | 참고 |
|------|---|-----|------|
| rod, suction electrode | 두꺼비 | 1.0–1.2 | Baylor et al. 1979 |
| rod, peak response | 원숭이 | 0.9–1.1 | Schnapf et al. 1990 |
| cone (L/M), steady state | 인간 | 0.7–1.0 | Schnapf et al. 1987 |
| cGMP-gated channel | 소 | 2.0–3.0 | Haynes & Yau 1985 |
| ganglion cell (P-cell) | 원숭이 | 0.7–0.9 | Kaplan & Shapley 1986 |

**주목**: cGMP 채널 수준의 $n \approx 2$–$3$ 이 막전위 수준에서 $n \approx 1$ 로 줄어드는 이유: 여러 압축 단계 (분자 수준의 여러 비선형성) 가 *연쇄*되면 전체 Hill 지수가 부분 hill 지수들의 비율에 의해 감소. Lamb & Pugh (1992) 참조.

### 4.2 미분 형태 ($h(V)$ 의 정체)

§3.1 의 $h(V)$ 항이 Naka-Rushton 압축을 구현. $V$ 가 $V_{\text{dark}}$ 에서 멀어질수록 $h$ 가 *환원 방향* 으로 작용 — 응답이 saturate.

명시적 형태:

$$
h(V) = \alpha \cdot \frac{(V_{\text{dark}} - V)^{n+1}}{I_{50}^n + (V_{\text{dark}} - V)^n}
$$

(부호 주의 — hyperpolarizing convention 에서 $V_{\text{dark}} - V > 0$ when responding.)

### 4.3 적응 — $I_{50}$ 의 sliding 과 slow-fast SDE 분석

**현상학적 관찰**: $I_{50}$ 은 *상수가 아니다*. 배경 강도 $\bar{I}$ 에 따라 *움직임*:

$$
I_{50}(t) \approx \kappa \cdot \bar{I}(t)
$$

여기서 $\bar{I}(t)$ 는 *최근 입력의 평균* (exponential moving average).

#### 4.3.1 Augmented System

Hidden state augmentation (§0 의 Meta-3 결정):

$$
\mathbf{X}(t) = (V(t), \bar{I}(t)) \in \mathbb{R}^2
$$

Augmented SDE:

$$
dV = \left[-\frac{1}{\tau}(V - V_{\text{rest}}) - h(V, \bar{I})\right] dt - g (r_1 *_t dN_x)(t) + \sigma_V dW_t^{(1)}
$$

$$
d\bar{I} = -\frac{1}{\tau_a}(\bar{I} - I(t)) dt + \sigma_a dW_t^{(2)}
$$

여기서 $I(t) = \int r_1 *_t dN_x$ (광도 추정), $\tau_a \gg \tau$ (slow adaptation).

#### 4.3.2 Slow-fast 분리

$\epsilon := \tau / \tau_a \ll 1$ 로 정의. 시간을 *fast scale* $t$ (membrane) 와 *slow scale* $T = \epsilon t$ (adaptation) 로 분리.

$\epsilon \to 0$ 극한에서 Pavliotis-Stuart §16 의 *averaging / homogenization* 적용:

**Fast equation** ($T$ 고정, $\bar{I} = \bar{I}_0$):

$$
dV = b_0(V, \bar{I}_0) dt + \sigma_V dW_t + \text{(Poisson jump)}
$$

이 방정식은 $\bar{I}_0$ 를 파라미터로 하는 *고정된* SDE → stationary distribution $p_\infty^{(\bar{I}_0)}(V)$ 가 존재 (§7.2 참조).

**Slow effective equation**: $\bar{I}$ 의 effective dynamics 는 $V$ 를 fast equilibrium 으로 평균화:

$$
d\bar{I} = -\frac{1}{\tau_a}\left(\bar{I} - \langle I \rangle_{\bar{I}}\right) dT + \tilde{\sigma}_a dW_T^{(2)}
$$

여기서 $\langle I \rangle_{\bar{I}} = \int I \, p_\infty^{(\bar{I})}(V) dV$ 는 fast stationary distribution 에 대한 평균 광도.

**결론**: 느린 시간 스케일에서 $\bar{I}$ 는 *effective Naka-Rushton 의 setpoint* 로 행동. 빠른 시간에서 $V$ 는 현재의 $\bar{I}$ 를 파라미터로 하는 즉각적인 Naka-Rushton 응답.

이 *sliding setpoint* 메커니즘이 dark adaptation (rod: $\tau_a \sim$ minutes) 와 light adaptation (cone: $\tau_a \sim$ seconds–minutes) 의 수학적 설명.

**Reference**: Pavliotis & Stuart (2008), *Multiscale Methods: Averaging and Homogenization*, §16; Freidlin & Wentzell (2012), *Random Perturbations of Dynamical Systems*.

### 4.4 Weber-Fechner 도출 — 정확한 계산

**목표**: 적응이 완료된 상태에서 *상대 contrast* 에 대한 응답이 logarithmic임을 정확히 계산.

**설정**: $I_{50} = \kappa \bar{I}$ (적응 완료). 입력 $I = \bar{I} + \Delta I$ 로 쓰면.

**단계 1. Naka-Rushton 의 1차 Taylor 전개** (at $I = \bar{I}$, i.e., $\Delta I = 0$):

$$
R(I) = R_{\max} \frac{I^n}{I^n + I_{50}^n}
$$

편미분:

$$
\frac{dR}{dI}\bigg|_{I = \bar{I}} = R_{\max} \cdot \frac{n I^{n-1}}{(I^n + I_{50}^n)} \cdot \frac{I_{50}^n}{I^n + I_{50}^n}\bigg|_{I = \bar{I}}
$$

$I_{50} = \kappa \bar{I}$ 대입 → $I = I_{50}/\kappa$ 로 표현하면:

$$
\frac{dR}{dI}\bigg|_{I = \bar{I}} = R_{\max} \cdot \frac{n \kappa^n}{(\kappa^n + 1)^2} \cdot \frac{1}{\bar{I}}
$$

**단계 2. contrast response**:

$$
\Delta R := R(\bar{I} + \Delta I) - R(\bar{I}) \approx \frac{dR}{dI}\bigg|_{\bar{I}} \cdot \Delta I = C(\kappa, n) \cdot R_{\max} \cdot \frac{\Delta I}{\bar{I}}
$$

여기서 $C(\kappa, n) = n\kappa^n / (1 + \kappa^n)^2$ 는 상수.

**단계 3. Weber-Fechner 형태**:

이를 contrast $c = \Delta I / \bar{I}$ 로 쓰면:

$$
\boxed{\Delta R = C(\kappa, n) \cdot R_{\max} \cdot c}
$$

즉, *응답 변화는 절대 강도에 무관하고 상대 contrast 에만 비례*. 이게 **Weber-Fechner law 의 미분 형태**.

**단계 4. 로그 근사**:

$|I - \bar{I}| / \bar{I} \ll 1$ 이면 $I = \bar{I} e^x$ ($x \ll 1$) 로 parameterize:

$$
R(\bar{I} e^x) - R(\bar{I}) \approx C(\kappa, n) \cdot R_{\max} \cdot x = C(\kappa, n) \cdot R_{\max} \cdot \log(I/\bar{I})
$$

따라서 *응답 차이가 log-ratio 에 비례* — Weber-Fechner 의 적분 형태.

**단계 5. 동적 범위 (per decade)**:

$I$ 가 1 decade ($\times 10$) 변할 때 응답 변화:

$$
\Delta R\big|_{1\text{ decade}} = C(\kappa, n) \cdot R_{\max} \cdot \ln(10) \approx C \cdot R_{\max} \cdot 2.303
$$

이게 TC-SP-1.4 의 구체적 계산.

**단계 6. 전체 동적 범위**:

실제 log-range: 빛 자극은 $10^{10}$ 의 강도 범위. Naka-Rushton 단독으로는 $\sim 1.5$ decades. *적응으로 I_{50} 이 슬라이딩*하면 유효 범위가 훨씬 넓어짐 — 각 *지역적 강도 구간* 에서 선형 동작.

**Laughlin (1981) 의 관계**: 최적 log-compressor 는 input distribution 이 power-law 일 때 Fischer-information maximizing 이다. 광자 intensity 분포가 (자연 장면에서) 거의 log-normal → log-compression 이 locally optimal.

### 4.5 Volterra 전개 — $K_2$ 의 명시적 계산

Naka-Rushton 의 작은 신호 전개 (around $I_0 = \bar{I}$, $R_0 = R(\bar{I})$):

$$
R(I) - R_0 = K_1 * \Delta I + \iint K_2(t_1, t_2) \Delta I(t - t_1) \Delta I(t - t_2) \, dt_1 dt_2 + \ldots
$$

#### 4.5.1 1차 kernel $K_1$

시간 영역에서 $K_1(t) = r_1(t)$ — *단광자 응답 함수*. (정의에 의해.)

주파수 영역: $\hat{K}_1(\omega) = \hat{r}_1(\omega) = \prod_{i=1}^n (1 + i\omega\tau_i)^{-1}$.

#### 4.5.2 2차 kernel $K_2$ 의 유도

Naka-Rushton 의 2차 Taylor 전개:

$$
R(\bar{I} + \Delta I) = R(\bar{I}) + R'(\bar{I}) \Delta I + \frac{1}{2} R''(\bar{I}) (\Delta I)^2 + O((\Delta I)^3)
$$

$R''(\bar{I})$ 계산 (Hill function 의 2차 미분):

$$
R''(I) = R_{\max} \cdot n \cdot \frac{I_{50}^n (n-1 - (n+1) I^n/I_{50}^n) \cdot I^{n-2}}{(I^n + I_{50}^n)^3}
$$

$I = I_{50}$ ($\kappa = 1$ 의 경우 명료함) 에서:

$$
R''(I_{50}) = R_{\max} \cdot \frac{n(n-1 - (n+1))}{4 I_{50}^2} = R_{\max} \cdot \frac{-2n}{4 I_{50}^2} = -\frac{n R_{\max}}{2 I_{50}^2}
$$

따라서 *2차 kernel* (시간 영역, 시간-불변 가정):

$$
K_2(t_1, t_2) = \frac{1}{2} R''(\bar{I}) \cdot K_1(t_1) K_1(t_2)
$$

즉,

$$
\boxed{K_2(t_1, t_2) = -\frac{n R_{\max}}{4 I_{50}^2} \cdot r_1(t_1) r_1(t_2)}
$$

(이는 "product" 형태 — Wiener kernel 의 자기-곱 구조.)

**부호**: $K_2 < 0$ (억제적) — Naka-Rushton 의 *오목성* (saturation) 이 2차 kernel 의 음수 부호로 나타남.

**크기**: $|K_2| / |K_1|^2 \sim n R_{\max} / (4 I_{50}^2)$. $I \approx I_{50}$ 에서 비선형 효과가 strongest.

#### 4.5.3 Wiener kernel vs Volterra kernel

**구별점**: Volterra kernel $K_2$ 는 *symmetric* ($K_2(t_1, t_2) = K_2(t_2, t_1)$) 이고, 임의의 input 에 대해 정의. Wiener kernel $H_2$ 는 *white noise input* 에 대한 cross-correlation 로 정의:

$$
H_2(t_1, t_2) = \frac{\langle y(t) x(t - t_1) x(t - t_2) \rangle}{2! \langle x^2 \rangle^2}
$$

관계: Gaussian white noise input 에서 $H_2 = K_2 / 2$ (symmetric normalization 차이만). 자연 scene stimulus 에서는 Volterra 이, 실험적 reverse-correlation 에서는 Wiener 가 자연스럽다.

**Reference**: Marmarelis & Marmarelis (1978), *Analysis of Physiological Systems*; Simoncelli & Heeger (1998).

---

## 5. Hyperpolarizing Dark Current — 부호 규약과 유도

### 5.1 cGMP-gated 채널의 구조 — Dark current 유도

광수용기 outer segment 의 cGMP-gated 채널 (CNG channel) 의 전류를 미시적으로 유도한다.

**단계 1. 단일 채널 전류** (Ohm's law):

단일 CNG 채널의 전류:

$$
i_{\text{single}} = \gamma_{\text{CNG}} \cdot (V - E_{\text{rev}})
$$

여기서 $\gamma_{\text{CNG}} \approx 20$–$30$ pS 는 단일채널 conductance, $E_{\text{rev}} \approx 0$ mV (Na+/Ca2+ reversal potential).

**단계 2. Open probability**:

채널의 open probability 는 cGMP 에 대한 Hill 함수:

$$
p_{\text{open}}(c) = \frac{c^n}{c^n + K_{\text{cG}}^n}
$$

Rod 에서 $n \approx 2$–$3$, $K_{\text{cG}} \approx 20 \,\mu\text{M}$.

**단계 3. Total dark current**:

채널 밀도 $\rho_{\text{CNG}}$ (개수/membrane area), outer segment 막 면적 $A_{\text{OS}} \approx 500 \,\mu\text{m}^2$:

$$
J_{\text{dark}} = N_{\text{CNG}} \cdot p_{\text{open}}(c_{\text{dark}}) \cdot \gamma_{\text{CNG}} \cdot (V_{\text{dark}} - E_{\text{rev}})
$$

여기서 $N_{\text{CNG}} = \rho_{\text{CNG}} \cdot A_{\text{OS}}$.

**단계 4. 어둠 막전위 $V_{\text{dark}}$ 결정**:

Dark current $J_{\text{dark}}$ (inward, Na+/Ca2+) 가 hyperpolarizing current (outer segment K+ current + inner segment pump) 와 균형:

$$
J_{\text{dark,in}} + J_{\text{K,out}} + J_{\text{pump}} = 0
$$

이 균형으로부터 $V_{\text{dark}} \approx -40$ mV 가 결정됨 (일반 신경세포 $-70$ mV 보다 덜 음수).

**수치 추정**:
- $N_{\text{CNG}} \approx 10^4$–$10^5$ channels
- $p_{\text{open,dark}} \approx 0.02$–$0.05$ (낮은 개방 확률 — 이미 대부분 닫혀 있음)
- 총 dark current: $J_{\text{dark}} \approx 10$–$50$ pA (rod suction electrode 측정 일치)

**왜 $-40$ mV 인가**: 일반 신경세포에서 K+ leak channel 로 $-70$ mV 가 설정. 광수용기는 추가로 *dark current* (inward) 가 항상 흐르므로 membrane 이 *탈분극 방향* 으로 offset. $-40$ mV 는 dark inward current 와 K+ outward current 의 균형점.

### 5.2 빛 → 토닉 감소

빛 → cGMP 가수분해 → 채널 닫힘 → 막 *과분극* → 시냅스 글루타메이트 *감소*.

따라서 *빛 = 신호 증가* 가 *아니라* *빛 = 토닉 감소*. 부호 규약 (sign convention) 이 *반전*.

### 5.3 부호 규약의 SDE 함의

본 문서의 §3.1 SDE 에서 jump 항이 *음수* (-g) 인 이유 — 광자 도래 시 $V$ 가 *감소* (more negative, hyperpolarizing).

후속 stage 에서 다시 부호가 분리됨: bipolar cell 의 ON-type 은 sign-inverting (light → depolarize), OFF-type 은 sign-preserving (light → hyperpolarize). 첫 시냅스의 수용체 차이가 결정 (→ [[04_stage2_inner_retinal_algebra#3. ON OFF 분리|04 §3]]).

### 5.4 정보론적 의미 (preview)

빛 = 토닉 감소의 정보론적 사실:

- *부재* 신호 (negative encoding) 는 *존재* 신호와 같은 정보량을 carry
- 다만 *biological efficiency* 가 다름 — 토닉 spike rate 가 항상 높으면 metabolic cost 가 크다
- → ON/OFF 분리는 이 효율을 회복 (각 채널은 절반 시간만 활성)

상세는 [[04_stage2_inner_retinal_algebra|04]] 와 [[06_endtoend_information_bound|06]].

---

## 6. Type 분리 — Rod vs Cone

### 6.1 Poisson Thinning 정리 — 증명

Type 분기의 수학적 기초는 *Poisson thinning theorem* 이다.

**Theorem 6.1 (Poisson Thinning / Coloring)**. $N \sim \text{Poisson}(\Lambda)$ 는 $\mathcal{X}$ 위 inhomogeneous Poisson point process 라 하자. 각 점 $x \in N$ 을 독립적으로 type $\tau \in \mathcal{T}$ 로 분류하되, 확률

$$
\Pr[\text{type} = \tau \mid x] = p_\tau(x), \quad \sum_{\tau \in \mathcal{T}} p_\tau(x) = 1
$$

로 분류한다. Type $\tau$ 의 점들의 집합 $N_\tau := \{x \in N : \text{type}(x) = \tau\}$ 에 대해:

**(a)** 각 $N_\tau$ 는 강도 $\Lambda_\tau(dx) = p_\tau(x) \Lambda(dx)$ 의 inhomogeneous Poisson point process.

**(b)** $\{N_\tau\}_{\tau \in \mathcal{T}}$ 는 *서로 독립*.

**증명 스케치**:

**(a)의 증명**: 임의의 Borel set $B \subset \mathcal{X}$ 에 대해:

$$
\Pr[N_\tau(B) = k] = ?
$$

원래 과정 $N$ 에서 $B$ 안의 점 수는 $N(B) \sim \text{Poisson}(\Lambda(B))$.

각 점이 독립적으로 type $\tau$ 일 확률 $\bar{p}_\tau(B) := \Lambda_\tau(B) / \Lambda(B)$ (강도로 가중된 평균).

전체 확률 법칙으로:

$$
\Pr[N_\tau(B) = k] = \sum_{m=k}^{\infty} \Pr[N(B) = m] \binom{m}{k} \bar{p}_\tau(B)^k (1 - \bar{p}_\tau(B))^{m-k}
$$

$$
= \sum_{m=k}^{\infty} e^{-\Lambda(B)} \frac{\Lambda(B)^m}{m!} \binom{m}{k} \bar{p}_\tau(B)^k (1 - \bar{p}_\tau(B))^{m-k}
$$

$$
= e^{-\Lambda(B)} \frac{(\Lambda(B) \bar{p}_\tau(B))^k}{k!} \sum_{m=k}^{\infty} \frac{[\Lambda(B)(1-\bar{p}_\tau(B))]^{m-k}}{(m-k)!}
$$

$$
= e^{-\Lambda(B)} \frac{\Lambda_\tau(B)^k}{k!} e^{\Lambda(B)(1 - \bar{p}_\tau(B))} = e^{-\Lambda_\tau(B)} \frac{\Lambda_\tau(B)^k}{k!}
$$

따라서 $N_\tau(B) \sim \text{Poisson}(\Lambda_\tau(B))$.

완전 독립성 (P1) 의 검증: disjoint $B_1, B_2 \subset \mathcal{X}$ 에 대해 $N_\tau(B_1)$ 와 $N_\tau(B_2)$ 의 독립성은 원래 $N$ 의 독립 증분과 각 점의 독립 분류로부터.

**(b)의 증명**: $N_{\tau_1}(B)$ 와 $N_{\tau_2}(B)$ 의 결합 분포 ($\tau_1 \neq \tau_2$):

$$
\Pr[N_{\tau_1}(B) = k_1, N_{\tau_2}(B) = k_2] = \sum_{m \geq k_1 + k_2} \frac{e^{-\Lambda(B)} \Lambda(B)^m}{m!} \frac{m!}{k_1! k_2! (m-k_1-k_2)!} \bar{p}_1^{k_1} \bar{p}_2^{k_2} (1 - \bar{p}_1 - \bar{p}_2)^{m-k_1-k_2}
$$

위와 동일한 계산으로:

$$
= e^{-\Lambda_1(B)} \frac{\Lambda_1(B)^{k_1}}{k_1!} \cdot e^{-\Lambda_2(B)} \frac{\Lambda_2(B)^{k_2}}{k_2!}
$$

즉, **결합 분포 = 주변 분포의 곱** → $N_{\tau_1}(B)$ 와 $N_{\tau_2}(B)$ 가 독립. $\square$

**광변환에의 적용**: Stage 0 의 광자 $N$ 이 파장 $\nu$ 에 따라 type 분류:

$$
p_\tau(\nu) = \eta_\tau(\nu) / \sum_{\tau'} \eta_{\tau'}(\nu)
$$

Thinning theorem → 각 $N_\tau$ 가 독립 Poisson, 강도 $\Lambda_\tau = p_\tau \Lambda$.

$$
N \xrightarrow{\text{thinning by } \eta_\tau} N_\tau \text{ for each } \tau \in \{R, L, M, S\}
$$

### 6.2 4-type SDE

광수용기 type $\tau \in \{R, L, M, S\}$:

- $R$: rod (rhodopsin, peak $\sim 500$ nm, low light)
- $L$: long cone (peak $\sim 564$ nm)
- $M$: medium cone (peak $\sim 534$ nm)
- $S$: short cone (peak $\sim 420$ nm)

각 type 의 SDE 는 동일 form (§3.1) 이나 parameter 가 다름:

| Parameter | Rod | Cone (L/M/S) |
|-----------|------|--------------|
| $\tau$ (membrane) | $\sim 100$ ms | $\sim 10$ ms |
| $g$ (photon gain) | high (single-photon detectable) | low ($\sim 100$ photons needed) |
| $r_1$ peak time | $\sim 200$ ms | $\sim 50$ ms |
| $R_{\max}$ | similar | similar |
| $\eta(\nu)$ profile | peak 500 nm | peak 564/534/420 nm |

### 6.3 4-component 상태공간

Type-분리된 $\mathcal{S}_1$:

$$
\mathcal{S}_1^{\text{full}} := \bigoplus_{\tau \in \{R, L, M, S\}} C(\Sigma_\tau \times \mathbb{R}^+, \mathbb{R})
$$

여기서 $\Sigma_\tau$ 는 type $\tau$ 광수용기의 *서식 영역* — rod 는 주변부 dense, cone 은 fovea dense.

격자 비균질성:
- Rod: foveal pit 에 0, peripheral 에 $\sim 1.6 \times 10^5$ /mm²
- L+M cones: foveal 에 $\sim 2 \times 10^5$ /mm², peripheral 에 $\sim 5 \times 10^3$ /mm²
- S cones: 전반 sparse, $\sim 5-10\%$ of cones

### 6.4 색 정보의 원형

L, M, S cone 의 입력 분리가 *색 정보의 원형*. 그러나 *색 대립* (L-M, S-(L+M)) 은 stage 2 의 inner retinal circuit 에서 일어남 (→ [[04_stage2_inner_retinal_algebra|04 §6]]).

본 stage 의 출력은 *3-tuple* $(V_L, V_M, V_S)$ + $V_R$. 이를 *색 공간으로 재조합* 하는 것은 다음 stage.

---

## 7. Fokker-Planck 대응

### 7.1 분포 방정식

SDE $dV = b(V) dt + \sigma dW$ 의 distribution $p(V, t)$ 는 Fokker-Planck:

$$
\partial_t p(V, t) = -\partial_V [b(V) p(V, t)] + \frac{\sigma^2}{2} \partial_V^2 p(V, t)
$$

§3.1 의 jump term 포함하면 (integro-differential form):

$$
\partial_t p(V, t) = -\partial_V[b(V) p] + \frac{\sigma_V^2}{2} \partial_V^2 p + \int \lambda(\nu) [p(V - g r_1(\nu), t) - p(V, t)] d\nu
$$

여기서 마지막 항이 *Poisson jump* contribution.

### 7.2 Stationary Distribution — Ornstein-Uhlenbeck 기저 사례

Jump 없이 ($g = 0$), 선형 drift $b(V) = -\alpha(V - \mu)$ (Ornstein-Uhlenbeck process), 상수 diffusion $\sigma$ 인 경우의 정상 분포를 계산한다.

**Fokker-Planck (jump 없음)**:

$$
\partial_t p = \alpha \partial_V [(V - \mu) p] + \frac{\sigma^2}{2} \partial_V^2 p
$$

**정상 분포**: $\partial_t p_\infty = 0$ → ODE:

$$
\alpha \frac{d}{dV} [(V - \mu) p_\infty] + \frac{\sigma^2}{2} \frac{d^2 p_\infty}{dV^2} = 0
$$

**적분**: 한 번 적분 (probability current = 0 at boundaries):

$$
\alpha (V - \mu) p_\infty + \frac{\sigma^2}{2} \frac{d p_\infty}{dV} = 0
$$

이는 separable ODE:

$$
\frac{d \ln p_\infty}{dV} = -\frac{2\alpha}{\sigma^2}(V - \mu)
$$

풀면:

$$
\boxed{p_\infty(V) = \mathcal{N}\left(\mu, \frac{\sigma^2}{2\alpha}\right) = \sqrt{\frac{\alpha}{\pi \sigma^2}} \exp\left(-\frac{\alpha}{\sigma^2}(V - \mu)^2\right)}
$$

**해석**: OU process 의 정상 분포는 *Gaussian* — 평균 $\mu$ (= drift 의 목표), 분산 $\sigma^2/(2\alpha)$ (noise 와 restoring force 의 균형).

광수용기 적용 ($\mu = V_{\text{rest}}$, $\alpha = 1/\tau$):

$$
p_\infty^{\text{OU}}(V) = \mathcal{N}\left(V_{\text{rest}}, \frac{\sigma_V^2 \tau}{2}\right)
$$

분산 $\sigma_V^2 \tau / 2$: 노이즈 강도와 막 시상수의 곱. 크기 추정: $\sigma_V \sim 0.1$ mV/$\sqrt{\text{ms}}$, $\tau \sim 100$ ms → 분산 $\sim 0.5$ mV². 이는 dark noise floor 와 일치.

**Jump 포함 경우**: 광자 Poisson jump 는 $p_\infty$ 를 *오른쪽 (더 음수 방향)* 으로 shift 시키고 *비대칭* 하게 만든다. 명시적 계산은 적분-미분 방정식으로 일반 해가 없으나, *소 광자율* 극한에서 OU 결과의 1차 perturbation 으로 처리 가능.

### 7.3 Has'minskii 의 ergodicity 기준

**Theorem 7.1 (Has'minskii)**. SDE $dV = b(V) dt + \sigma dW$ 가 다음 *Lyapunov 조건* 을 만족하면 unique stationary distribution 이 존재하고 분포가 지수적으로 수렴한다:

**(L1) Lyapunov function**: $U : \mathbb{R} \to \mathbb{R}^+$ smooth 이고, compact $K$ 밖에서:

$$
\mathcal{L} U(V) := b(V) U'(V) + \frac{\sigma^2}{2} U''(V) \leq -c U(V) + d \cdot \mathbf{1}_K(V)
$$

for constants $c > 0$, $d < \infty$.

**(L2) Ellipticity**: $\sigma > 0$ (nondegenerate diffusion).

**검증 (photoreceptor SDE)**: $U(V) = (V - V_{\text{rest}})^2$ 로 취하면:

$$
\mathcal{L} U(V) = 2(V - V_{\text{rest}}) b(V) + \sigma_V^2
$$

$b(V) = -\tau^{-1}(V - V_{\text{rest}}) - h(V)$ 이고 $h(V) \geq 0$ (Naka-Rushton), $h(V) \to h_{\max}$ (bounded):

$$
\mathcal{L} U(V) = -\frac{2}{\tau}(V - V_{\text{rest}})^2 - 2(V - V_{\text{rest}}) h(V) + \sigma_V^2 \leq -\frac{2}{\tau} U(V) + \sigma_V^2 + 2 h_{\max}^2 \tau / 2
$$

즉, $K = \{V : U(V) \leq R\}$ for 충분히 큰 $R$ 에서 (L1) 만족.

**결론**: Has'minskii 기준 → 광수용기 SDE 의 unique stationary distribution + 지수 수렴.

**Reference**: Has'minskii (1980), *Stochastic Stability of Differential Equations*, §3.3.

---

## 8. $\mathcal{K}_1$ — Explicit Form

### 8.1 정의

$\mathcal{K}_1 : \mathcal{S}_0 \to \mathcal{S}_1$ 의 정의:

> $N \in \mathcal{S}_0$ (광자 configuration) 이 주어졌을 때, $\mathcal{K}_1(N, \cdot)$ 는 §3.1 의 SDE 의 *path 분포* (모든 픽셀 $x$ 위에서, 시간 $\mathbb{R}^+$ 위에서) 의 law.

### 8.2 Conditional Distribution $\mathcal{K}_1(N, \cdot)$ — Explicit Form

광자 configuration $N = \sum_k \delta_{(x_k, t_k, \nu_k)}$ (stage 0 의 atomic 표현) 가 주어졌을 때, $\mathcal{K}_1(N, \cdot)$ 는 각 픽셀 $x$ 에 대해 다음 SDE 의 law:

$$
dV_t^{(x)} = b(V_t^{(x)}) dt + \sigma_V dW_t^{(x)} - g \sum_{k: x_k = x} r_1(t - t_k) \mathbf{1}_{t > t_k}
$$

더 정확히 — stochastic integration 으로:

$$
V_t^{(x)} = V_0 + \int_0^t b(V_s^{(x)}) ds + \sigma_V W_t^{(x)} - g \int_{(0, t]} r_1(t - s) N_x(ds)
$$

여기서:
- $W_t^{(x)}$: pixel $x$ 의 독립 Brownian motion
- $N_x(ds) = \sum_{k: x_k = x} \delta_{t_k}(ds)$: pixel $x$ 의 photon arrival times
- $\int_{(0,t]} r_1(t-s) N_x(ds) = \sum_{k: x_k = x, t_k < t} r_1(t - t_k)$: 누적 단광자 응답

**Markov property**: 위 표현에서 $V_t^{(x)}$ 는 $N$ (고정) 에 대해 drift 가 결정론적 (시간 의존) 이므로 *driven Langevin* process. $N$ 이 random 이면 다시 Markov.

**Law of $V_t$ given $N$**: $\mathcal{K}_1(N, \cdot) = \text{Law}(V^{(x)}, x \in \Sigma_{\text{ret}})$ where $V^{(x)}$ 는 위 SDE 의 solution. 이는 $C(\Sigma_{\text{ret}} \times \mathbb{R}^+, \mathbb{R})$ 위 *Gaussian process* (jump term 을 고정하면 나머지 SDE 가 linear → Gaussian). 즉:

$$
\mathcal{K}_1(N, \cdot) = \text{Gaussian process} \left( \text{mean: } \mu_{V}^{(N)}(x, t), \text{ covariance: } C_V(x, t; x', t') \right)
$$

where

$$
\mu_V^{(N)}(x, t) = V_{\text{rest}} + (V_0 - V_{\text{rest}}) e^{-t/\tau} - g \sum_{k: x_k = x, t_k < t} r_1(t - t_k) e^{-(t - t_k)/\tau}
$$

(OU semigroup 로부터 closed form; 비선형 $h(V)$ 를 무시한 선형 근사).

**Cross-pixel independence**: 서로 다른 픽셀 $x \neq x'$ 의 SDE 는 독립 Brownian motion $W^{(x)}, W^{(x')}$ 를 가지므로, *jump term 이 독립* (Poisson thinning → 픽셀별 독립 Poisson) 이면 $V^{(x)}$ 와 $V^{(x')}$ 도 conditional on $N$ 에 대해 *독립*.

### 8.3 well-definedness

**TC-SP-1.1 (Stage 1 보장)** ([[01_framework_master#TC-SP-1.1|01 §5]] 의 stage 1 측 보강):

> 다음 조건 하에서 $\mathcal{K}_1$ 는 well-defined stochastic kernel:
> (a) $\sigma_V > 0$ (positive diffusion)
> (b) $h, b$ 가 Lipschitz on bounded sets
> (c) jump kernel $r_1$ 이 integrable
> (d) 초기 분포 $V(\cdot, 0)$ 가 $\mathcal{S}_1$ 위 well-defined measure

**증명 가능성**: Theorem 3.1 (§3.1.2) 의 직접 적용.

### 8.4 인과성

SDE 가 *Itô* 의 standard form → 인과적 (현재의 $V$ 변화율은 현재까지의 history 에만 의존). [[01_framework_master#TC-SP-1.3|01 TC-SP-1.3]] 의 stage 1 측 보장.

### 8.5 평균 회계 (Campbell-Mecke application)

Stage 0 의 [[02_stage0_photon_point_process#5. Palm Calculus|02 §5]] 의 Campbell-Mecke 를 §3.1 SDE 에 적용:

$$
\mathbb{E}[V(x, t)] = V_{\text{rest}} - g \int_{-\infty}^t \int_{\Sigma_p \times \Lambda} r_1(t - s) \cdot \eta_\tau(\nu) \, \Lambda(dx', ds, d\nu) - O(\text{nonlinear})
$$

여기서 적분 영역의 $\Sigma_p$ 는 픽셀 $p$ 의 absorption 영역. 이 표현이 *평균 응답* — linear (LN) 해석.

비선형 corrections (Volterra $K_2, K_3, \ldots$) 가 Naka-Rushton 의 saturation 으로부터. $K_2$ 의 explicit form 은 §4.5.2.

---

## 9. Theorem-Candidates

### TC-SP-1.4 — [DELETED 2026-05-25 Pass 4 (escalated from Pass 3 WEAKENED)]

**Status**: **DELETED via Pass 4 — weakening insufficient**. Pass 4 의 #46 (boundary: sub-threshold $\bar I \to 0$ + saturation $\bar I \to \infty$ 미처리; Q1-Q3 qualifier 가 working region 을 pin 하지 못함) + #51 (Pavliotis-Stuart conditional ergodicity 가 jump-diffusion 의 cross-window independence 깸) 가 추가 HOLE → cumulative 4 patterns → 박탈.

**Original statement**: Naka-Rushton 압축 후 dynamic range ∝ log(input).

**Weakening attempt (Pass 3, also DELETED)**: Q1-Q3 (adaptive sliding + log-normal + ergodicity) 추가했으나 boundary 와 averaging 의 underlying independence 가 fundamental 결함.

**Why DELETED**: Logarithmic compression 은 *Hill function + adaptation + 자연 광 분포* 의 *결합 결과* — 어느 하나라도 본 정리의 *load-bearing assumption*. 일반 정리 자격 없음.

**Replacement**: §4.4 의 Weber-Fechner derivation 본문 유지 — *quantitative observation* 으로. *Empirical fitting* (Laughlin 1981 fly LMC, Brady-Field 2000) 만 reference. 정리 자격 없음.

### TC-SP-1.5 — [DELETED 2026-05-25 Pass 3]

**Status**: **DELETED via Pass 3 adversarial verification** (2-pattern HOLE: #18 tautology + #5 hypothesis recheck).

**Original statement (preserved for audit trail)**:

> 적절한 SNR 조건 (rod 의 dark current 노이즈 floor $\sigma_V$ vs 단광자 응답 진폭 $g \cdot \max r_1$) 하에서 $\text{SNR} \gtrsim 1$ → 단일 광자 응답이 통계적으로 *검출 가능*.

**Refute basis**:

- **#18 (tautology)**: "Detectable" 가 SNR ≥ 1 로 *operationally 정의됨*; 정리가 SNR ≥ 1 → detectable 주장 — *pure self-reference*. 저자 본문 "SNR 정의로부터 자명" 명시 admit.
- **#5 (hypothesis)**: CLE 의 copy number ≳ 20-100 가정이 R* (copy number = 1) 에 대해 *명시적으로* 위반; 광수용기 noise 는 *discrete bumps* (non-Gaussian) 이나 SNR 정리는 Gaussian noise 가정.

**Why deleted**: Tautological self-reference + hypothesis violation. *Empirical observation* (Baylor 1979 의 rod 단광자 검출) 은 사실; 그러나 *theorem* 으로 다루지 않는다.

**Replacement**: Baylor-Lamb-Yau (1979) empirical 사실 은 §3.4 본문 (single-photon impulse response) 에 *empirical reference* 로만 유지. SNR ≥ 1 의 statistical detection criterion (Neyman-Pearson, ROC) 의 *non-Gaussian* (discrete-bump) decision theory 형식은 추후 OP candidate.

---

## 10. Open Problems

### OP-SP-002: Naka-Rushton 적응 동역학의 형식화

**Status**: OPEN. Severity: Medium.

**문제**: §4.3 의 $I_{50}(t)$ sliding 은 phenomenological — 실제 적응은 multiple time scales (수 ms ~ 수 시간; OP-SP-009) 의 hierarchy.

**Candidate 방향**:

1. **Slow-fast SDE**: §4.3.2 에서 skeleton 분석 완료. 남은 문제: (a) averaging 오차의 정량화 ($O(\epsilon)$); (b) 실제 $\tau_a$ 가 $\tau$ 의 몇 배인지 정확한 생물학적 추정.
2. **Hidden Markov 적응**: $I_{50}$ 가 discrete *adaptation state* 들 사이의 Markov chain.
3. **Adaptive Wiener filter**: $\mathcal{K}_1$ 가 *time-varying* kernel 로, optimal filtering 이론 (Wiener-Hopf) 에서.
4. **Variational adaptation**: 적응이 어떤 *free energy* 또는 *KL divergence* 의 최소화.

**Lyapunov 함수의 존재**: 적응이 어떤 functional 의 gradient descent 인가? Candidate: information-theoretic objective (mutual info; Laughlin 1981, TC-SP-4.3).

**본 디렉토리의 입장**: 적응을 hidden state augmentation 으로 처리 (§4.3). 정확한 동역학은 별도 추후 작업.

---

## 11. (Ω, σ) Tier 2 mapping (preview)

[[07_omega_sigma_lift|07]] 에서 본격. Stage 1 의 직접 매핑:

- $\Omega_1 = \Sigma_{\text{ret}} \times \mathbb{R}^+ \times \{R, L, M, S\}$ — type-마크된 시공간 격자
- $\sigma_1((x_i, t_i, \tau_i), (x_j, t_j, \tau_j)) \iff$ $|x_i - x_j| < \delta_x$ AND $|t_i - t_j| < \delta_t$ AND $\tau_i = \tau_j$ (같은 type 안에서 시공간 인접)

여기에 "응답 값" $V(x, t, \tau)$ 가 attached — Tier 2 + 부속 graded value. 사용자가 commit 한 *minimal 가공* 의 일관성 — 값이 *부속*되어 있지 *구조에 본질적* 이지 않음.

---

## 12. 도구 사용 summary

본 stage 에서 사용된 도구 ([[01_framework_master#4. 수학적 도구 카탈로그|01 §4]] reference):

| 도구 | 사용 |
|------|------|
| 4.1 점과정 | Poisson thinning (type 분기, §6.1 증명); Campbell-Mecke (§8.5) |
| 4.2 SDE | jump-diffusion SDE (§3.1); Fokker-Planck (§7); CLE van Kampen (§2.3) |
| 4.3 함수해석 | Volterra series K_2 (§4.5); Lipschitz 조건 (§3.1.2); coercivity (§7.3) |
| 4.4 합성곱 | single-photon kernel $r_1 *$ (§3.1); gamma-function 유도 (§3.2) |
| 4.8 정보이론 | TC-SP-1.4 의 DPI 관계; Weber-Fechner (§4.4) |
| 4.13 변분법 | OP-SP-002 의 free-energy candidate; Has'minskii Lyapunov (§7.3) |

---

## 9.5 실험적 파라미터 표 — Rod/Cone (Rat, Monkey, Human)

아래 표는 §3.1 의 SDE 파라미터를 실험 문헌으로부터 수집한 것이다. 모든 값은 개략적 (order-of-magnitude) 이며 실험 조건 (온도, 개체, 연령) 에 따라 변동.

### 9.5.1 Single-Photon Response 파라미터

| 파라미터 | Rat Rod | Monkey Rod | Human Rod | Monkey Cone | Human Cone (L/M) | Reference |
|---------|---------|-----------|-----------|------------|-----------------|-----------|
| Peak amplitude $\max r_1$ (pA) | 0.9–1.5 | 0.7–1.2 | 1.0–1.8 | 0.01–0.05 | ~ 0.03 | Baylor et al. 1979, 1984 |
| Peak time $t_{\text{peak}}$ (ms) | 200–400 | 100–200 | 120–250 | 20–60 | 30–70 | Schnapf et al. 1987, 1990 |
| Halfwidth HWHM (ms) | 400–700 | 200–400 | 250–500 | 30–80 | 40–100 | Baylor et al. 1984 |
| Cascade stages $n$ | 4–6 | 4–6 | 4–6 | 3–4 | 3–4 | (fit to gamma) |
| Filter time const $\tau$ (ms) | 40–80 | 25–50 | 30–60 | 8–20 | 10–25 | Lamb & Pugh 1992 |

### 9.5.2 Membrane 파라미터

| 파라미터 | Rat Rod | Monkey Rod | Human Rod | Cone (est.) | Reference |
|---------|---------|-----------|-----------|------------|-----------|
| Membrane time const $\tau_V$ (ms) | 80–150 | 60–120 | 70–130 | 5–15 | Baylor & Nunn 1986 |
| Dark potential $V_{\text{dark}}$ (mV) | $-38$ to $-42$ | $-38$ to $-42$ | $\approx -40$ | $-40$ to $-45$ | Baylor et al. 1979 |
| Dark current $J_{\text{dark}}$ (pA) | 15–30 | 10–25 | 10–25 | 20–60 | Schnapf et al. 1990 |
| Thermal noise $\sigma_V$ (mV/$\sqrt{\text{ms}}$) | 0.05–0.15 | 0.05–0.12 | ~0.10 | 0.2–0.5 | (estimated from SNR) |

### 9.5.3 Naka-Rushton 파라미터

| 파라미터 | Rat Rod | Monkey Rod | Human Rod | L-cone | M-cone | S-cone | Reference |
|---------|---------|-----------|-----------|--------|--------|--------|-----------|
| Hill exponent $n$ | 0.9–1.1 | 0.9–1.0 | 1.0 | 0.7–1.0 | 0.7–1.0 | ~0.8 | Schnapf et al. 1987 |
| Half-sat $I_{50}$ (photons/s/$\mu$m²) | 50–200 | 80–300 | ~100 | $10^3$–$10^4$ | $10^3$–$10^4$ | ~$10^4$ | Baylor et al. 1984 |
| Adaptation $\tau_a$ (s) | 10–100 | 5–60 | 5–60 | 0.1–5 | 0.1–5 | ~1 | Fain et al. 2001 |

### 9.5.4 Cascade 분자 파라미터 (Pugh-Lamb)

| 파라미터 | 값 (Amphibia/Mammal) | 의미 | Reference |
|---------|---------------------|-----|-----------|
| $k_{R^*}$ | 10–50 s$^{-1}$ | Rhodopsin 비활성화율 | Lamb & Pugh 1992 |
| $k_{\text{tr}}$ | $10^3$–$10^4$ M$^{-1}$s$^{-1}$ | Transducin 활성화 속도 | Pugh & Lamb 1993 |
| $k_{T^*}$ | 1–3 s$^{-1}$ | Transducin GTPase | Lamb 1996 |
| $k_{\text{cat}}$ (PDE) | $1000$–$4000$ s$^{-1}$ | cGMP 가수분해율 | Rieke & Baylor 1998 |
| $\alpha_{\text{dark}}$ | 20–80 $\mu$M s$^{-1}$ | cGMP 합성율 | Burns & Baylor 2001 |
| $K_{\text{cG}}$ (Hill) | 10–30 $\mu$M | cGMP channel half-sat | Yau & Nakatani 1985 |
| $n_{\text{cG}}$ (Hill) | 2–3 | cGMP channel cooperativity | Haynes & Yau 1985 |

**온도 의존성**: 위 값들은 대부분 $37°$C (포유류 체온) 기준. $25°$C (냉혈동물) 에서는 $k$ 들이 $\sim 3$–$5\times$ 느림 (Q10 $\approx 2$–$3$).

**개체 변동**: Rod 파라미터는 개체 간 변동이 $\sim 30$–$50\%$ (geometric std). Cone 파라미터는 색각 이상자 (dichromat, anomalous trichromat) 에서 크게 다를 수 있음.

---

*Stage 1 v1. 후속: [[04_stage2_inner_retinal_algebra]]. 노출 type: $V(x, t, \tau) \in \mathcal{S}_1^{\text{full}}$, type-tagged graded 막전위. TC-SP-1.4, TC-SP-1.5 등록. OP-SP-002 등록.*
