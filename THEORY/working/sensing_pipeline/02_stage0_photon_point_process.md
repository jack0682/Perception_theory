---
type: working/sensing_pipeline/stage0
version: v1
date: 2026-05-25
status: DEFINITION-DRAFT
purpose: |
  Stage 0 deep dive: photon arrival as marked Poisson point process
  on Σ_ret × ℝ⁺ × Λ. Develops the full point-process apparatus
  (intensity measure, Campbell, Slivnyak-Mecke, Janossy, Palm,
  cumulants, pair correlation, Doob-Meyer, Cox, photon-number
  uncertainty) and registers TC-SP-0.1, TC-SP-0.2, TC-SP-0.3.
  Deepened version: Janossy equivalence proof, Mandel-Wolf coherence
  primer, radiative transfer derivation, full variance computation,
  Campbell-Mecke proof sketch, Slivnyak proof, explicit Palm example,
  Doob-Meyer decomposition, sub/super-Poissonian regimes, Mandel Q,
  two-point peripheral correlations.
register: DEFINITION-DRAFT + THEOREM-CANDIDATE (no proofs)
parent: 01_framework_master
constraint_compliance:
  canonical_theorem_changes: 0
  scc_edits: 0
---

> [!nav] Parent: [[00_INDEX]] · Prev: [[01_framework_master]] · Next: [[03_stage1_photoreceptor_sde]]

# Stage 0 — Photon Arrival as Marked Point Process

## 0. 본 문서의 위치

본 문서는 SSKP (Stratified Stochastic Kernel Pipeline; [[01_framework_master#3. 마스터 객체 — 5단계 파이프라인|01 §3]]) 의 *입력 stage* $\mathcal{S}_0$ 와 그 위 측도 $\mu_0$ 를 점과정 이론으로 형식화한다. 본 문서가 끝나면:

- $\mathcal{S}_0$ 의 정확한 측도론적 구조
- $\mu_0$ 의 생성 (장면 radiance + 광학 + 양자효율) 의 합성 규칙
- Poisson 가정의 자연성 — Mandel-Wolf coherence 이론으로 정당화
- Poisson 의 등가 정의 및 Janossy density 형태와의 동치 증명 스케치
- 1차/2차 모멘트 measure, 분산, 모든 cumulant 의 명시적 계산
- Pair correlation $g^{(2)}$: Poisson, Neyman-Scott, Matérn, Gibbs 비교
- Campbell, Campbell-Mecke, Slivnyak-Mecke 의 완전한 증명 스케치
- Palm distribution 의 명시적 1D 예제
- 보상측도 (compensator), Doob-Meyer 분해, Cox process 연결
- Sub-Poissonian / super-Poissonian regime, Mandel Q, 시각에서의 위치
- 말초 시야에서의 two-point 광자 상관 구조
- $\mathcal{K}_1 : \mathcal{S}_0 \to \mathcal{S}_1$ 의 입력 type 의 엄밀한 해명

이 다음 문서에서 사용할 수 있는 형태로 노출된다.

본 문서가 *수행하지 않는 것*: stage 1 의 광수용기 변환 ($\mathcal{K}_1$ 의 정확한 형태; [[03_stage1_photoreceptor_sde|03]] 의 역할).

---

## 1. 측도론적 골격

### 1.1 Ground space

광자 1개의 *발생점* 은 다음 세 정보로 식별:

- *위치*: $x \in \Sigma_{\text{ret}} \subset \mathbb{R}^2$ (망막 표면)
- *시각*: $t \in \mathbb{R}^+$
- *파장*: $\nu \in \Lambda \subset \mathbb{R}^+$ (대략 380–780 nm)

따라서 단일 광자 발생점은 ground space

$$
\mathcal{X} := \Sigma_{\text{ret}} \times \mathbb{R}^+ \times \Lambda
$$

의 원소. 본 디렉토리 전체에서 $\Sigma_{\text{ret}}$ 은 compact ($\partial \Sigma_{\text{ret}}$ smooth), $\Lambda$ 는 compact interval (bounded wavelength band). 따라서 $\mathcal{X}$ 는 locally compact Polish space.

**Note (편광)**: 광자에는 편광 자유도도 있으나 망막 수용기는 (이론적으로) 편광 비-감지 — 본 디렉토리는 편광 자유도를 marginalize 하여 무시. 명시적 mark 로 추가하려면 $\mathcal{X} \times S^2$ 로 확장.

**Note (방향)**: 광자의 입사 방향 (k-vector) 은 광수용기에 따라 응답이 다른 *Stiles-Crawford 효과* 가 있음. 이론적 단순화를 위해 본 문서는 입사 방향을 marginalize (광학 transfer 가 이를 처리한다고 가정).

### 1.2 Counting measure 공간

$\mathcal{X}$ 위 *locally finite counting measure* 공간:

$$
\mathcal{N}(\mathcal{X}) := \left\{ N = \sum_{i} \delta_{x_i} : x_i \in \mathcal{X}, \; N(K) < \infty \text{ for all compact } K \subset \mathcal{X} \right\}
$$

각 $N \in \mathcal{N}(\mathcal{X})$ 는 (가능하면 무한히 많은) 광자 발생점들의 집합을 atomic Dirac 측도의 합으로 표현. **Borel σ-algebra** $\mathcal{B}_{\mathcal{N}}$ 는 *vague topology* 에서 유도 — 즉, 모든 compact $K \subset \mathcal{X}$ 와 $n \in \mathbb{N}$ 에 대해

$$
\{ N : N(K) = n \} \in \mathcal{B}_{\mathcal{N}}
$$

가 가측집합. (Daley-Vere-Jones §A2; Last-Penrose §6.)

### 1.3 Stage 0 상태공간

$$
\boxed{\mathcal{S}_0 := \mathcal{N}(\mathcal{X}) \text{ with Borel σ-algebra } \mathcal{B}_{\mathcal{N}}.}
$$

이는 Polish space (Last-Penrose Lemma 6.4) — [[01_framework_master#1.1 상태공간의 일반 형태|01 §1.1]] 의 가정 (G1, G2) 만족.

---

## 2. Inhomogeneous Poisson Point Process

### 2.1 강도 측도 (Intensity Measure)

**Definition 2.1**. $\mathcal{X}$ 위 σ-finite measure $\Lambda \in \mathcal{M}^+(\mathcal{X})$ 가 *강도측도* (intensity measure) 라 함은:

$$
\mathbb{E}[N(B)] = \Lambda(B) \quad \forall B \in \mathcal{B}_\mathcal{X}.
$$

본 디렉토리에서 $\Lambda$ 는 density 를 가진다고 가정:

$$
\Lambda(dx \, dt \, d\nu) = \lambda(x, t, \nu) \, dx \, dt \, d\nu
$$

여기서 $\lambda : \mathcal{X} \to \mathbb{R}^+$ 는 *강도밀도* (intensity density). $\lambda$ 의 단위: photons / (area × time × wavelength).

### 2.2 Inhomogeneous Poisson 정의

**Definition 2.2 (Inhomogeneous Poisson)**. $N \in \mathcal{N}(\mathcal{X})$ 가 강도 $\Lambda$ 의 *inhomogeneous Poisson point process* 라 함은:

1. **(P1)** 임의의 disjoint Borel sets $B_1, \ldots, B_k \subset \mathcal{X}$ 에 대해 $N(B_1), \ldots, N(B_k)$ 가 *독립*.
2. **(P2)** 임의의 Borel set $B$, $n \in \mathbb{N}$ 에 대해:
   $$\Pr[N(B) = n] = e^{-\Lambda(B)} \frac{\Lambda(B)^n}{n!}.$$

조건 (P1) 은 *완전 독립 증분* (complete independence), (P2) 는 *Poisson marginal*.

**Note**: $\Lambda$ 가 atomic 이 아니라 absolutely continuous (∝ density) 인 경우 process 는 *simple* — 두 광자가 정확히 같은 점에 있을 확률 0.

### 2.3 정의 등가형 — Janossy density 와 (P1)+(P2) 의 동치

**Definition 2.3 (Janossy density)**. Compact window $W \subset \mathcal{X}$ 위 $n$-차 Janossy density:

$$
j_n^W(x_1, \ldots, x_n) = e^{-\Lambda(W)} \prod_{i=1}^n \lambda(x_i), \quad x_1, \ldots, x_n \in W.
$$

이는 "$N(W) = n$ 이고 그 점들이 $(x_1, \ldots, x_n)$ 일 확률밀도" 의 symmetrized 버전.

**명제 2.3.1 (동치)**. $N$ 이 Definition 2.3 의 Janossy density 를 가짐은 $N$ 이 (P1)+(P2) 를 만족함과 동치이다.

**증명 스케치** (양방향):

**(P1)+(P2) → Janossy)**. Compact $W$ 를 고정. $B_1, \ldots, B_n \subset W$ 가 disjoint 라 하자. (P2) 로부터 각 $B_i$ 에서의 점 개수는 독립 Poisson($\Lambda(B_i)$) 이다. 이를 통합하면: $N(W) = n$ 조건 하에 $n$ 개의 점은 $W$ 위에 *i.i.d.* $\lambda(x)/\Lambda(W)$ 분포를 가진다. 따라서 $N(W) = n$ 의 결합 밀도는

$$
\Pr[N(W) = n] \cdot \frac{n! \prod_i \lambda(x_i)}{\Lambda(W)^n} = e^{-\Lambda(W)} \frac{\Lambda(W)^n}{n!} \cdot \frac{\prod_i \lambda(x_i)}{\Lambda(W)^n} \cdot n! = e^{-\Lambda(W)} \prod_{i=1}^n \lambda(x_i).
$$

(마지막 $n!$ 은 symmetrization 에서 상쇄.) 이것이 정확히 $j_n^W$.

**(Janossy → (P1)+(P2))**. 역방향: Janossy density 가 product 형태 $e^{-\Lambda(W)} \prod_i \lambda(x_i)$ 이면, $W$ 안의 점들이 i.i.d. $\lambda/\Lambda(W)$ 이고 개수가 Poisson($\Lambda(W)$) 임을 Janossy density 의 generating function 을 통해 확인할 수 있다. 생성함수:

$$
G^W(h) := \sum_{n=0}^\infty \frac{1}{n!} \int_{W^n} j_n^W(x_1, \ldots, x_n) \prod_{i=1}^n h(x_i) \, d x_1 \cdots d x_n
$$

에 $j_n^W = e^{-\Lambda(W)} \prod \lambda(x_i)$ 를 대입하면

$$
G^W(h) = e^{-\Lambda(W)} \sum_{n=0}^\infty \frac{1}{n!} \left( \int_W \lambda(x) h(x) \, dx \right)^n = \exp\!\left( -\Lambda(W) + \int_W \lambda(x) h(x) \, dx \right) = \exp\!\left( \int_W (h(x) - 1) \Lambda(dx) \right).
$$

이것이 inhomogeneous Poisson 의 probability generating functional (PGF) 이다 (Last-Penrose §3). PGF 가 일치하면 분포가 일치하므로 (P2) 가 복원된다. Disjoint windows 위에서의 PGF 의 곱 인수분해

$$
G^{W_1 \cup W_2}(h) = G^{W_1}(h) \cdot G^{W_2}(h)
$$

가 $W_1, W_2$ disjoint 일 때 성립하므로 (P1) 도 복원된다. $\square$

**핵심 관찰**: Poisson 의 Janossy density 가 *곱* 형태인 것이 전 이론의 기초. 일반 점과정에서는 $j_n^W$ 가 $n$ 개의 점 사이에 임의의 상관을 허용한다.

### 2.4 광자 도래의 Poisson 가정 — Mandel-Wolf coherence 이론

**물리적 핵심 문제**: 왜 자연광 아래에서의 광자 도래가 Poisson 인가? 단순히 "양자역학이 그렇다"는 답은 불충분하다. 광원의 *통계적 성질* — coherent vs. thermal vs. Fock state — 이 다른 광자 통계를 준다. Mandel-Wolf 의 표준 광학 coherence 이론이 이 질문에 답한다.

#### 2.4.1 Coherence 시간과 Coherence 면적

**Coherence 시간** $\tau_c$ 는 전자기장의 *자기-상관 함수* $\Gamma^{(1)}(\tau) := \langle E^*(t) E(t+\tau) \rangle$ 가 decay 하는 시간 스케일:

$$
\tau_c := \int_{-\infty}^\infty |\gamma^{(1)}(\tau)|^2 \, d\tau, \quad \gamma^{(1)}(\tau) := \frac{\Gamma^{(1)}(\tau)}{\Gamma^{(1)}(0)}.
$$

(Mandel-Wolf §4.3, eq. 4.3-19.) 단색광 (좁은 대역폭 $\Delta\nu$) 의 경우 $\tau_c \sim 1/\Delta\nu$. 태양광의 경우 $\Delta\nu \sim 10^{14}$ Hz 이므로 $\tau_c \sim 10^{-14}$ 초.

**Coherence 면적** $A_c$ 는 횡단 방향 (transverse) 에서의 상관 길이의 제곱:

$$
A_c := \left( \int |\mu^{(1)}(\mathbf{r}_1, \mathbf{r}_2)|^2 \, d^2\mathbf{r}_{12} \right)
$$

여기서 $\mu^{(1)}$ 은 공간 coherence degree. 확장 광원 (태양) 의 경우 van Cittert-Zernike 정리에 의해 망막에서의 coherence 면적은

$$
A_c^{\text{ret}} \approx \frac{(\lambda_{\text{opt}} f)^2}{A_{\text{source}}}
$$

($f$: 눈의 초점거리, $A_{\text{source}}$: 광원의 시야 입체각에 대응하는 면적). 태양의 경우 이것이 단일 망막 수용기 면적 ($\sim 1 \, \mu\text{m}^2$) 보다 *훨씬 작아* coherence 효과가 무시된다.

#### 2.4.2 Bose-Einstein vs. Poisson 통계

단일 모드 열광원 (blackbody) 의 광자 수 분포는 **Bose-Einstein** (기하분포):

$$
\Pr[n \text{ photons}] = \frac{\bar{n}^n}{(1 + \bar{n})^{n+1}}, \quad \bar{n} = \frac{1}{e^{h\nu/kT} - 1}.
$$

(Mandel-Wolf §12.10, eq. 12.10-6.) 이 분포는 분산이 $\text{Var}[n] = \bar{n}(1 + \bar{n}) > \bar{n}$ — *super-Poissonian*.

그러나 이는 *단일 모드, 단일 coherence cell* 에서의 통계. 검출기가 *많은 독립 모드* 를 합산할 때 중심극한정리의 효과로 Poisson 으로 수렴한다. 구체적으로: 검출 시간 $\Delta t$ 와 검출 면적 $A$ 에 대해 모드 수는

$$
M \approx \frac{\Delta t}{\tau_c} \cdot \frac{A}{A_c}
$$

이다. $M$ 개의 독립 Bose-Einstein 모드의 합 $n = \sum_{i=1}^M n_i$ 의 분산은

$$
\text{Var}[n] = \bar{n} + \frac{\bar{n}^2}{M}.
$$

(Mandel-Wolf §9.7, eq. 9.7-29.) $M \gg \bar{n}$ 이면 $\text{Var}[n] \approx \bar{n}$ — Poisson 한계.

망막의 경우: $\Delta t \sim 1 \text{ ms}$ (rod 통합 시간), $\tau_c \sim 10^{-14}$ s → $\Delta t / \tau_c \sim 10^{11}$ 모드. $A \sim 1 \, \mu\text{m}^2$, $A_c^{\text{ret}} \ll 1 \, \mu\text{m}^2$ → 수백~수천 공간 모드. 따라서 $M \gg 1$ 이고 Poisson 근사는 *극도로 정확하다* — Bose-Einstein 보정항 $\bar{n}^2/M$ 이 완전히 무시 가능.

#### 2.4.3 Coherent (laser) 광원의 경우

Ideal single-mode laser (coherent state $|\alpha\rangle$) 는 *정확한* Poisson 통계를 가진다:

$$
\Pr[n] = e^{-|\alpha|^2} \frac{|\alpha|^{2n}}{n!}, \quad \bar{n} = |\alpha|^2, \quad \text{Var}[n] = \bar{n}.
$$

(Mandel-Wolf §11.3.) 즉, coherent 광원은 Poisson 을 *정확히* 실현한다 (Bose-Einstein 으로의 보정 없음). 이런 의미에서 "자연광 = Poisson" 은 다양한 경로로 정당화된다: (a) 열광원의 다중-모드 한계, (b) coherent 광원의 정확한 결과.

#### 2.4.4 자연 광원의 Poisson 환원 — 명시적 정리 형태

**Proposition 2.4 (Mandel의 자연광 Poisson 환원)**. 검출 시간 $\Delta t$ 와 검출 면적 $A$ 에서의 광자 수 $n$이 $M = (\Delta t / \tau_c)(A / A_c)$ 개의 독립 thermal 모드의 합일 때, $M \to \infty$ 와 함께 $\bar{n} = M\bar{n}_{\text{mode}}$ 고정이면:

$$
\Pr[n] \to e^{-\bar{n}} \frac{\bar{n}^n}{n!}.
$$

*증명 스케치*: $n$ 의 특성함수 $\phi_n(\xi) = (\mathbb{E}[e^{i\xi n_{\text{mode}}}])^M$. 단일 Bose-Einstein 모드의 특성함수는 $\phi_{\text{BE}}(\xi) = (1 - \bar{n}_{\text{mode}}(e^{i\xi} - 1))^{-1}$. 따라서 $\phi_n(\xi) = (1 - \bar{n}_{\text{mode}}(e^{i\xi}-1))^{-M}$. $M \to \infty$, $\bar{n}_{\text{mode}} = \bar{n}/M \to 0$:

$$
(1 - \tfrac{\bar{n}}{M}(e^{i\xi}-1))^{-M} \to e^{\bar{n}(e^{i\xi} - 1)},
$$

이것이 Poisson($\bar{n}$) 의 특성함수이다. $\square$

#### 2.4.5 무시되는 경우 (→ OP-SP-001)

아래 경우들에서 Poisson 가정이 깨진다:

- **광자 bunching** (Hanbury Brown-Twiss 효과): 좁은 검출 시간 $\Delta t < \tau_c$ 에서 super-Poissonian.
- **광자 antibunching**: 단일 emitter (단일 형광 분자, quantum dot) 의 경우 sub-Poissonian, $g^{(2)}(0) < 1$.
- **Squeezed light**: 특정 양자광학 상태에서 임의의 sub-Poissonian 분포 가능.
- **레이저 강도 변조**: modulated laser 는 super-Poissonian intensity noise.

일상 자연 시각의 맥락에서 이 모든 경우는 무시 가능하다 (OP-SP-001).

### 2.5 광자율의 유래 — 복사 전달 방정식과 광학 transfer

강도 밀도 $\lambda(x, t, \nu)$ 의 합성 공식:

$$
\boxed{\lambda(x, t, \nu) = L_{\text{ret}}(x, t, \nu) \cdot T_{\text{optics}}(x, \nu) \cdot \eta(\nu) \cdot \frac{1}{h \nu}}
$$

- $L_{\text{ret}}(x, t, \nu)$: 망막 표면에 도달하는 *방사조도* (irradiance), 단위 W/(m² · Hz)
- $T_{\text{optics}}(x, \nu)$: 안구 광학의 *투과도* ∈ [0, 1]
- $\eta(\nu)$: 광수용기 단위면적당 *흡수 효율*
- $1 / (h \nu)$: 광자 에너지의 역수

#### 2.5.1 복사 전달 방정식 (Radiative Transfer Equation)

장면에서 $L_{\text{ret}}$ 까지의 변환은 *복사 전달 방정식* (RTE) 에 의해 지배된다. 산란 없는 대기 + 반사면의 단순화 버전:

$$
\frac{dL(\mathbf{r}, \hat{\omega}, \nu)}{ds} = -\kappa(\mathbf{r}, \nu) L(\mathbf{r}, \hat{\omega}, \nu) + j(\mathbf{r}, \hat{\omega}, \nu)
$$

여기서 $\mathbf{r}$ 은 공간 위치, $\hat{\omega}$ 는 전파 방향, $s$ 는 경로 길이, $\kappa$ 는 소멸 계수, $j$ 는 방출 + 산란 소스. 산란이 없고 $\kappa \approx 0$ (투명 대기) 이면 $L$ 은 경로를 따라 보존된다 (Radiometry의 기본 법칙).

**장면 표면의 BRDF 기여**: 장면 점 $\xi$ 에서 망막 점 $x$ 로의 radiance 기여:

$$
L_{\text{ret}}(x, t, \nu) = \int_{\text{scene}} \rho(\xi; \hat{\omega}_i(\xi) \to \hat{\omega}_o(\xi, x)) \cdot E_i(\xi, t, \nu) \cdot \cos\theta_i(\xi) \, d\xi
$$

여기서:
- $\rho(\xi; \cdot \to \cdot)$: 위치 $\xi$ 에서의 BRDF (Bidirectional Reflectance Distribution Function), 단위 sr$^{-1}$
- $E_i(\xi, t, \nu)$: 장면 점 $\xi$ 에서의 입사 irradiance
- $\hat{\omega}_i$: 입사 방향, $\hat{\omega}_o(\xi, x)$: 망막 점 $x$ 로의 출사 방향
- $\theta_i$: 입사 zenith angle

#### 2.5.2 광자율 도출 — 단위 추적

방사조도 $L_{\text{ret}}$ 의 단위는 W/(m² · sr · Hz). 안구 pupil 면적 $A_p$, 전체 광학 solid angle $\Omega$ 를 통해 망막 위 단위 면적당 도달 power flux 는

$$
E_{\text{ret}}(\nu) = \int_\Omega L_{\text{ret}}(\hat{\omega}, \nu) \cos\theta \, d\Omega \quad [\text{W} \cdot \text{m}^{-2} \cdot \text{Hz}^{-1}]
$$

이를 광자 에너지 $h\nu$ 로 나누면 광자 flux (photons / m² / s / Hz):

$$
\Phi_{\text{photon}}(\nu) = \frac{E_{\text{ret}}(\nu)}{h\nu}.
$$

전체 스펙트럼 통합 광자율:

$$
\Phi_{\text{total}} = \int_\Lambda \Phi_{\text{photon}}(\nu) \, d\nu = \int_\Lambda \frac{E_{\text{ret}}(\nu)}{h\nu} \, d\nu.
$$

이것이 $\lambda(x, t)$ 의 스펙트럼-marginalized 버전. 스펙트럼 분해를 유지하면 위 §2.5 의 $\lambda(x, t, \nu) = L_{\text{ret}}(x, t, \nu) \cdot T_{\text{optics}} \cdot \eta(\nu) / (h\nu)$ 가 복원된다.

#### 2.5.3 기하광학 근사 — 점광원과 원거리 광원

**점광원 조명**: 거리 $d$ 에 있는 점광원 (power $P$ [W]) 의 경우 입사 irradiance 는

$$
E_i = \frac{P}{4\pi d^2} \quad [\text{W/m}^2]
$$

(역제곱 법칙). 따라서 광자율은 $\propto 1/d^2$.

**원거리 광원 (태양) 근사**: 태양은 실질적으로 평행광 (plane wave). 단위 면적당 irradiance $E_\odot \approx 1361 \text{ W/m}^2$ (Solar constant). 이 경우 거리 의존성이 사라지고 $L_{\text{ret}}$ 는 태양 고도각과 대기 흡수에 의해서만 결정된다.

**망막에서의 결과적 광자수**: 낮 환경 ($E_{\text{ret}} \sim 10^{-3}$ W/m² 전후, wavelength 통합)에서

$$
\lambda_{\text{typical}} \sim 10^5 \text{ photons / (mm}^2 \cdot \text{s)}
$$

로드 (rod) 는 $\sim 1 \, \mu\text{m}^2$ 면적이므로 단일 로드에서 $\sim 10^5 \times 10^{-6} = 0.1$ photon/s in daylight (bleaching saturation level) 부터 deep dark-adapted 상태에서 $10^{-3}$ photon/rod/s 까지.

**Definition 2.4 (Scene-derived intensity)**. 장면 $\mathcal{W}$ 가 BRDF $\rho$, 조명 $E$ 를 가질 때, 스펙트럼 분해 유지 강도 밀도:

$$
\lambda(x, t, \nu) = \left[ \int_{\text{scene}} \rho(\xi; \hat\omega_i(\xi) \to \hat\omega_o(\xi,x)) E_i(\xi, t, \nu) \cos\theta_i \, d\xi \right] \cdot T_{\text{optics}}(x, \nu) \cdot \eta(\nu) \cdot (h\nu)^{-1}.
$$

본 디렉토리는 $L_{\text{ret}}$ 를 *주어진 것* 으로 취급. 장면 → $L_{\text{ret}}$ 의 복사 전달은 외부 문제.

### 2.6 입력 측도 $\mu_0$

[[01_framework_master#3.5 입력 측도|01 §3.5]] 의 $\mu_0$ 는 본 stage 에서 *Poisson 분포* 로 specific:

$$
\mu_0 := \text{Law}(N) \text{ where } N \sim \text{Poisson}(\Lambda).
$$

즉, $\mu_0$ 는 $\mathcal{S}_0$ 위의 *분포* — 광자 발생점들의 random configuration 의 확률법칙. 본 디렉토리에서 $\mu_0$ 가 등장할 때 항상 이 Poisson 분포를 의미한다.

---

## 3. 모멘트 측도 (Moment Measures) 와 Cumulant

Point process 의 통계를 정량화하는 핵심 도구. Poisson 의 *결정적 단순성* 이 여기서 드러난다.

### 3.1 1차 모멘트 (Intensity Measure)

**Definition 3.1**. 1차 모멘트 측도:

$$
M_1(B) := \mathbb{E}[N(B)], \quad B \in \mathcal{B}_\mathcal{X}.
$$

Inhomogeneous Poisson 의 경우 $M_1 = \Lambda$ — definition 으로부터 직접.

### 3.2 2차 factorial 모멘트

**Definition 3.2 (2nd factorial moment measure)**. 

$$
M_2^{[2]}(B_1 \times B_2) := \mathbb{E}\left[ \sum_{x \neq y \in N} \mathbf{1}_{B_1}(x) \mathbf{1}_{B_2}(y) \right]
$$

여기서 합은 $N$ 안의 *서로 다른* 점쌍 위.

**Lemma 3.3 (Poisson factorization)**. Inhomogeneous Poisson 의 경우:

$$
M_2^{[2]}(B_1 \times B_2) = \Lambda(B_1) \Lambda(B_2).
$$

즉, *factorial 모멘트가 1차 모멘트의 곱으로 분해됨*. 이는 *완전 독립성* (P1) 의 직접 결과.

*증명 스케치*: $B_1, B_2$ 가 disjoint 이면 (P1) 에 의해 $N(B_1)$ 과 $N(B_2)$ 는 독립 Poisson 이므로 $\mathbb{E}[N(B_1) N(B_2)] = \mathbb{E}[N(B_1)] \cdot \mathbb{E}[N(B_2)] = \Lambda(B_1)\Lambda(B_2)$. $B_1 = B_2 = B$ 이면 $M_2^{[2]}(B \times B) = \mathbb{E}[N(B)(N(B)-1)] = \Lambda(B)^2$ (Poisson 의 factorial moment 공식). 일반 경우는 두 케이스의 linearity 로 처리.

### 3.3 $k$-차 factorial 모멘트

일반화:

$$
M_k^{[k]}(B_1 \times \cdots \times B_k) = \prod_{i=1}^k \Lambda(B_i) \quad \text{(Poisson)}.
$$

이는 Poisson 의 *기억-free 성질* 의 정확한 표현 — 임의 개수의 distinct 점들이 통계적으로 독립.

### 3.4 분산 계산 — 완전한 도출

**Proposition 3.4 (Shot noise 분산)**. Inhomogeneous Poisson 의 $N(B)$ 의 분산:

$$
\text{Var}[N(B)] = \mathbb{E}[N(B)] = \Lambda(B).
$$

**완전한 증명**: Poisson($m$) 분포 ($m = \Lambda(B)$) 에 대해 분산을 factorial moment 로 계산한다. $N(B) = n$ 분포에서:

$$
\mathbb{E}[N(B)] = \sum_{n=0}^\infty n \cdot e^{-m} \frac{m^n}{n!} = e^{-m} \sum_{n=1}^\infty \frac{m^n}{(n-1)!} = m e^{-m} \sum_{k=0}^\infty \frac{m^k}{k!} = m.
$$

2차 factorial moment:

$$
\mathbb{E}[N(B)(N(B)-1)] = \sum_{n=0}^\infty n(n-1) e^{-m} \frac{m^n}{n!} = m^2 e^{-m} \sum_{n=2}^\infty \frac{m^{n-2}}{(n-2)!} = m^2.
$$

따라서 $\mathbb{E}[N(B)^2] = \mathbb{E}[N(B)(N(B)-1)] + \mathbb{E}[N(B)] = m^2 + m$, 그리고

$$
\text{Var}[N(B)] = \mathbb{E}[N(B)^2] - (\mathbb{E}[N(B)])^2 = (m^2 + m) - m^2 = m = \Lambda(B). \quad \square
$$

**Covariance between disjoint sets**: $B_1 \cap B_2 = \emptyset$ 이면 (P1) 에 의해 $N(B_1), N(B_2)$ 독립, 따라서

$$
\text{Cov}[N(B_1), N(B_2)] = 0.
$$

이는 일반 점과정에서는 성립하지 않는다. Poisson 은 *disjoint regions 간 covariance 가 0* 이다.

이 두 사실을 합치면: $N(B)$ 의 covariance kernel 은

$$
\text{Cov}[N(B_1), N(B_2)] = \Lambda(B_1 \cap B_2).
$$

(Intersection 에 비례 — Poisson 의 covariance 구조의 완전한 표현.)

**관찰적 의미**: 어두운 장면 (작은 $\Lambda$) 일수록 *상대* 광자 잡음 $\sqrt{\text{Var}}/\mathbb{E} = 1/\sqrt{\Lambda(B)}$ 는 크다. 이게 *low-light vision* 이 *intrinsically noisy* 한 물리적 이유 — 정보 손실은 망막 회로의 결함이 아니라 양자물리의 한계.

### 3.5 Cumulant 분석 — 모든 cumulant 가 $\Lambda(B)$ 와 일치

**Definition 3.5 (Cumulant generating function)**. 확률변수 $X$ 의 *cumulant generating function (CGF)*:

$$
K_X(\xi) := \log \mathbb{E}[e^{\xi X}].
$$

$m$-차 cumulant 는 $\kappa_m = K_X^{(m)}(0) = \frac{d^m}{d\xi^m} K_X(\xi) \big|_{\xi=0}$.

**Proposition 3.6 (Poisson 의 cumulant)**. $X \sim \text{Poisson}(m)$ 에 대해:

$$
K_X(\xi) = m(e^\xi - 1), \quad \frac{d^k}{d\xi^k} K_X(\xi)\big|_{\xi=0} = m \quad \forall k \geq 1.
$$

즉, *모든 cumulant 가 $m = \Lambda(B)$ 로 동일하다.*

**증명**:

$$
\mathbb{E}[e^{\xi X}] = \sum_{n=0}^\infty e^{\xi n} e^{-m} \frac{m^n}{n!} = e^{-m} \sum_{n=0}^\infty \frac{(me^\xi)^n}{n!} = e^{-m} e^{m e^\xi} = e^{m(e^\xi - 1)}.
$$

따라서 $K_X(\xi) = m(e^\xi - 1)$. $k$-차 미분: $(d^k/d\xi^k)(e^\xi - 1) \big|_{\xi=0} = 1$ for all $k \geq 1$. 따라서 $\kappa_k = m$ for all $k \geq 1$. $\square$

**의미**: 1차 cumulant = 평균 $m$, 2차 cumulant = 분산 $m$ (§3.4 와 일치), 3차 cumulant = skewness source $m$, ... 모두 동일. 이는 Poisson 분포가 단 하나의 매개변수 $m$ 으로 완전히 결정됨의 cumulant 측 표현.

**점과정으로의 일반화**: 임의의 Borel set $B$ 에 대해 $N(B)$ 의 $k$-차 cumulant 측도:

$$
C_k^{\text{Poisson}}(B_1 \times \cdots \times B_k) = \Lambda(B_1 \cap B_2 \cap \cdots \cap B_k) \quad \text{(Poisson)}.
$$

일반 점과정의 경우 $k$-차 cumulant 측도는 diagonalonly form (Poisson) 이 아니라 off-diagonal 성분을 가진다 — 이것이 clustering / inhibition 의 cumulant 표현.

### 3.6 $g$-함수 (Pair correlation function) — 구체 예시 4가지

**Definition 3.7 (Pair correlation)**. 2차 intensity density $m_2(x_1, x_2)$ 와 1차 intensity $m_1(x) = \lambda(x)$ 에 대해:

$$
g^{(2)}(x_1, x_2) := \frac{m_2(x_1, x_2)}{m_1(x_1) m_1(x_2)}
$$

여기서 $m_2(x_1, x_2)$ 는 $M_2^{[2]}$ 의 density. 물리학 표기로는 $g^{(2)}(\mathbf{r}_1, \mathbf{r}_2)$ (second-order intensity correlation; Mandel-Wolf §9.2).

Poisson: $g^{(2)} \equiv 1$ (no correlation).

#### 3.6.1 Poisson: $g^{(2)} \equiv 1$

Lemma 3.3 으로부터 $m_2(x_1, x_2) = \lambda(x_1)\lambda(x_2)$, 따라서:

$$
g^{(2)}_{\text{Poisson}}(x_1, x_2) = 1 \quad \forall x_1 \neq x_2.
$$

완전 무상관. 임의의 두 광자의 위치는 독립적으로 분포.

#### 3.6.2 Neyman-Scott 군집 과정: $g^{(2)} > 1$

**Neyman-Scott process**: 모 점과정 (intensity $\kappa$ Poisson) 의 각 점 주위에 offspring 들이 i.i.d. 분포로 군집. 모 점 위치 $c$, offspring 분포 $h(\cdot - c)$ (예: $\mathcal{N}(0, \sigma^2)$), 클러스터당 평균 $\mu$ offspring.

이 과정의 intensity: $\lambda = \kappa \mu$. Pair correlation:

$$
g^{(2)}_{\text{NS}}(r) = 1 + \frac{1}{\kappa \mu^2} h^{(2)}(r)
$$

여기서 $h^{(2)}(r) = \int h(\mathbf{u}) h(\mathbf{u} + \mathbf{r}) \, d\mathbf{u}$ 는 offspring 분포의 자기-합성곱 (isotropic 가정 하 $r = \|x_1 - x_2\|$). $g^{(2)} > 1$ — 군집 (clustering).

**광학적 해석**: 반사 표면의 specular spot (정반사 점) 이 공간적으로 군집된 광자를 생성하면 Neyman-Scott 구조가 자연스럽다.

#### 3.6.3 Matérn 억제 과정: $g^{(2)} < 1$

**Matérn Type II**: Poisson 과정으로 "후보 점" 들을 생성, 그 중 어떤 점 $x$ 는 기준 거리 $r_0$ 내에 *먼저 생성된* 다른 점이 있으면 제거.

결과 과정의 intensity 는 $\lambda_{\text{Mat}} = \lambda_0 (1 - e^{-\lambda_0 \pi r_0^2}) / (\lambda_0 \pi r_0^2)$. Pair correlation:

$$
g^{(2)}_{\text{Mat}}(r) = 0 \text{ for } r < r_0, \quad g^{(2)}_{\text{Mat}}(r) \to 1 \text{ as } r \to \infty.
$$

$g^{(2)} < 1$ for $r < r_0$ — *hard-core inhibition*. 어떤 두 점도 거리 $r_0$ 이내에 올 수 없음.

**광학적 해석**: 광수용기의 물리적 배제 부피 (수용기 간 간격 $\sim 2 \, \mu\text{m}$ in fovea) 가 Matérn 구조를 *흡수* 한다. 그러나 이는 검출 단계 (stage 1) 의 효과지 광자 도래 자체의 성질이 아님.

#### 3.6.4 Gibbs 과정: 페어 포텐셜

**Gibbs process**: 쌍 상호작용 에너지 $\phi(r)$ 로 정의:

$$
p(x_1, \ldots, x_n) \propto e^{-\sum_{i < j} \phi(\|x_i - x_j\|)}.
$$

- $\phi(r) > 0$ (repulsion): $g^{(2)}(r) < 1$ for small $r$ (inhibition)
- $\phi(r) < 0$ (attraction): $g^{(2)}(r) > 1$ for small $r$ (clustering)

Pair correlation 은 Ornstein-Zernike 적분 방정식으로 계산 (closed form 없음; numerical):

$$
h(r) = c(r) + \lambda \int h(r') c(|r - r'|) \, dr'
$$

여기서 $h = g^{(2)} - 1$ (total correlation), $c$ (direct correlation).

**비교 요약**:

| 과정 | $g^{(2)}(0)$ | $g^{(2)}(\infty)$ | 의미 |
|------|-------------|------------------|------|
| Poisson | 1 | 1 | 무상관 |
| Neyman-Scott | $> 1$ | 1 | 군집 |
| Matérn Type II | 0 | 1 | hard-core 배제 |
| Gibbs (repulsion) | $< 1$ | 1 | soft 배제 |
| Gibbs (attraction) | $> 1$ | 1 | soft 군집 |

---

## 4. Campbell-type 정리들 — 증명 스케치

### 4.1 Campbell's theorem (1차) — 완전한 증명 스케치

**Theorem 4.1 (Campbell)**. 가측 $f : \mathcal{X} \to \mathbb{R}^+$ 에 대해:

$$
\mathbb{E}\left[ \sum_{x \in N} f(x) \right] = \int_\mathcal{X} f(x) \, \Lambda(dx).
$$

**증명 스케치** (monotone class argument):

*Step 1 (지시함수)*. $f = \mathbf{1}_B$ 이면

$$
\mathbb{E}\left[\sum_{x \in N} \mathbf{1}_B(x)\right] = \mathbb{E}[N(B)] = \Lambda(B) = \int \mathbf{1}_B \, d\Lambda.
$$

*Step 2 (단순함수)*. $f = \sum_{k=1}^m a_k \mathbf{1}_{B_k}$ ($a_k \geq 0$, $B_k$ disjoint) 이면 선형성:

$$
\mathbb{E}\left[\sum_{x \in N} f(x)\right] = \sum_k a_k \mathbb{E}[N(B_k)] = \sum_k a_k \Lambda(B_k) = \int f \, d\Lambda.
$$

*Step 3 (단조 수렴)*. 임의의 $f \geq 0$ 에 대해 단순함수 증가열 $f_n \nearrow f$. 각 $f_n$ 에 대해 등호 성립. 단조수렴정리를 양변에 적용:

$$
\mathbb{E}\left[\lim_{n\to\infty} \sum_{x\in N} f_n(x)\right] = \lim_{n\to\infty} \int f_n \, d\Lambda.
$$

좌변: $\sum_{x\in N} f_n(x) \nearrow \sum_{x\in N} f(x)$ pointwise, MCT 적용. 우변: $\int f_n \, d\Lambda \nearrow \int f \, d\Lambda$. 따라서 등호. $\square$

**일반 $f$ (양수/음수)**. $f = f^+ - f^-$ 로 분해 후 각각 적용.

**해석**: random configuration 위 합의 평균은 강도에 대한 적분. 광자 점과정의 *first-order statistic* 의 핵심.

### 4.2 Campbell's theorem (2차, distinct pairs)

**Theorem 4.2**. 가측 $f : \mathcal{X}^2 \to \mathbb{R}^+$ 에 대해:

$$
\mathbb{E}\left[ \sum_{x \neq y \in N} f(x, y) \right] = \int \int f(x_1, x_2) \, M_2^{[2]}(dx_1, dx_2).
$$

Poisson 의 경우 (Lemma 3.3):

$$
\mathbb{E}\left[ \sum_{x \neq y \in N} f(x, y) \right] = \int \int f(x_1, x_2) \Lambda(dx_1) \Lambda(dx_2).
$$

**증명 스케치**: Theorem 4.1 과 동일한 monotone class argument 를 $\mathcal{X}^2$ 위의 함수에 적용. $f = \mathbf{1}_{B_1 \times B_2}$ 이면 $\mathbb{E}[\sum_{x\neq y} \mathbf{1}_{B_1}(x)\mathbf{1}_{B_2}(y)] = M_2^{[2]}(B_1 \times B_2)$ 가 정의로부터, 나머지는 동일.

### 4.3 Campbell-Mecke 공식 — 깊은 정리

**Theorem 4.3 (Campbell-Mecke)**. $g : \mathcal{X} \times \mathcal{N}(\mathcal{X}) \to \mathbb{R}^+$ 가측이면:

$$
\mathbb{E}\left[ \sum_{x \in N} g(x, N) \right] = \int_\mathcal{X} \mathbb{E}\left[ g(x, N \cup \delta_x) \right] \Lambda(dx).
$$

여기서 우변의 기댓값은 $N \sim \text{Poisson}(\Lambda)$ 에 대해 — 점 $x$ 가 *추가된* configuration 에서의 $g$ 의 기댓값.

**증명 스케치** (Last-Penrose §4 의 접근):

*Step 1 (단순 $g$)*. $g(x, N) = \mathbf{1}_B(x) h(N)$ ($B \in \mathcal{B}_\mathcal{X}$, $h : \mathcal{N}(\mathcal{X}) \to \mathbb{R}^+$) 으로 취하면:

$$
\text{LHS} = \mathbb{E}\left[ \sum_{x \in N} \mathbf{1}_B(x) h(N) \right] = \mathbb{E}\left[ N(B) h(N) \right].
$$

$N(B)$ 와 $h(N)$ 의 관계를 다루기 위해, $N$ 을 $B$ 안의 부분 $N_B := N|_B$ 와 $B$ 밖의 부분 $N_{B^c}$ 로 분리. Poisson 의 (P1) 에 의해 $N_B \sim \text{Poisson}(\Lambda|_B)$ 와 $N_{B^c} \sim \text{Poisson}(\Lambda|_{B^c})$ 는 독립.

$N_B$ 에 대한 조건부 기댓값 계산: $N_B = \sum_{i} \delta_{y_i}$ ($y_i \in B$) 라 하면

$$
\mathbb{E}[N(B) h(N)] = \mathbb{E}\left[\left(\sum_i \mathbf{1}_B(y_i)\right) h\!\left(\sum_i \delta_{y_i} + N_{B^c}\right)\right].
$$

Poisson 과정에서 $N_B$ 의 $n$-th factorial moment 를 이용, 이를

$$
\int_B \mathbb{E}\left[h(N \cup \delta_x)\right] \Lambda(dx)
$$

의 형태로 재정리할 수 있다 (Mecke's formula 의 핵심 계산; 자세한 전개는 Last-Penrose §4.4). 이것이 Theorem 의 RHS (단순 $g$ 경우).

*Step 2 (일반화)*. 단순 $g$ 로부터 monotone class theorem 적용 — $g$ 들의 π-system (product functions) 이 위 등호를 만족하고, Dynkin 의 λ-π theorem 으로 모든 가측 $g$ 로 확장. $\square$

**핵심 의미**: Campbell-Mecke 는 "$x$ 에 점을 놓은 뒤 나머지 과정을 어떻게 보는가" 의 도구. 광자 수용기 응답 계산의 핵심: 각 광자 $x$ 의 기여 $g(x, N)$ 은 그 광자가 *어떤 configuration* $N$ 에 속해 있는지에 의존할 수 있다 — 이를 다루는 공식.

### 4.4 Slivnyak-Mecke 정리 — 증명 스케치

**Theorem 4.4 (Slivnyak-Mecke)**. Inhomogeneous Poisson ($N \sim \text{Poisson}(\Lambda)$) 의 경우, reduced Palm distribution $P^!_x$ 는:

$$
P^!_x = \text{Law}(N) = P \quad \forall x \in \mathcal{X}.
$$

**증명 스케치** (Janossy density 를 이용):

*Setup*. Compact window $W \subset \mathcal{X}$, $x \in W$. Campbell-Mecke (Theorem 4.3) 을 $g(x, N) = \mathbf{1}_B(x) \cdot h(N \setminus \{x\})$ ($h$ 가측, $B$ neighborhood) 으로 취하면:

$$
\mathbb{E}\left[\sum_{y \in N \cap B} h(N \setminus \{y\})\right] = \int_B \mathbb{E}[h(N)] \, \Lambda(dy).
$$

좌변은 Palm distribution $P^!_x$ 에 대한 정의 (§5.1) 로 재표현할 수 있다:

$$
= \int_B \mathbb{E}_{P^!_y}[h(N)] \, \Lambda(dy).
$$

$\Lambda$-a.e. $y$ 에 대해 피적분 함수를 비교하면 $\mathbb{E}_{P^!_y}[h(N)] = \mathbb{E}[h(N)]$ for all $h$. 이것이 $P^!_y = P$ 임을 의미한다.

*Alternative (Janossy)*. Janossy density 가 product form $j_n^W = e^{-\Lambda(W)} \prod \lambda(x_i)$ 이면 "$x_j$ 가 점과정의 일원이라 조건 후 나머지 점들의 Janossy density" 는 여전히 동일 product form:

$$
j_{n-1}^{W \setminus \{x_j\}}(x_1, \ldots, \hat x_j, \ldots, x_n) = e^{-\Lambda(W \setminus \{x_j\})} \prod_{i \neq j} \lambda(x_i).
$$

이는 정확히 $\text{Poisson}(\Lambda|_{W \setminus \{x_j\}})$ 의 Janossy density — $x_j$ 자신을 제거한 뒤의 Poisson 과정. $\square$

**핵심 직관**: Poisson 의 (P1) 이 말하는 것은 "어떤 점이 존재함" 이 *다른 점들의 분포에 영향을 미치지 않는다" 이다. Slivnyak-Mecke 는 이 직관을 Palm 이론의 언어로 정확하게 표현한다. Clustering 과정 (Neyman-Scott) 에서는 $P^!_x \neq P$ — 한 점이 존재한다는 것이 근방에 다른 점이 있을 확률을 높인다.

**광자 물리**: 두 광원의 합산 (광자들이 서로 간섭하지 않을 때). 광원 A 의 광자 $x$ 가 검출되었다고 해서 광원 B 의 다른 광자의 분포가 변하지 않는다 — 이것이 바로 $P^!_x = P$. 이 사실은 TC-SP-0.3 의 내용이다.

---

## 5. Palm Calculus — 광자 관점의 통계

Palm distribution 은 "조건부 분포" 이지만 *random measure* 의 atomic 점 위에서 조건. 광자 점과정에서 "광자 한 개의 관점에서" 보는 통계.

### 5.1 Palm distribution

**Definition 5.1**. $\mathcal{X}$ 의 점 $x$ 에서의 Palm distribution $P_x$:

$$
\int_\mathcal{X} \mathbb{E}_{P_x}[h(N)] \, \Lambda(dx) = \mathbb{E}\left[ \sum_{x \in N} h(N) \right]
$$

여기서 $h$ 는 $\mathcal{N}(\mathcal{X})$ 위의 가측 함수.

해석: $P_x$ 는 "$x$ 에 점이 있다는 조건 하에서 전체 configuration 의 분포".

### 5.2 Reduced Palm

$P^!_x := $ "$x$ 에 점이 있다 조건 후 $x$ 자신을 제거한 나머지 configuration 의 분포".

Poisson (Slivnyak-Mecke): $P^!_x = P$ 이지만 $P_x \neq P$ — 구체적으로

$$
P_x = \text{Law}(N + \delta_x) \text{ with } N \sim P = \text{Poisson}(\Lambda).
$$

즉, Poisson 의 Palm distribution 은 "원래 Poisson 에 $x$ 에서 Dirac 을 추가한 것".

### 5.3 명시적 1D 예시 — 율 $\lambda$ 의 동차 Poisson

**예시**: $\mathcal{X} = \mathbb{R}^+$, $N \sim \text{Poisson}(\lambda \cdot \ell)$ (Lebesgue measure × constant $\lambda$). 이 1D 과정에서 Palm distribution $P_0$ ("원점에 점이 있다" 조건) 는?

**계산**: Slivnyak-Mecke 에 의해 $P^!_0 = P = \text{Poisson}(\lambda \cdot \ell)$. 따라서

$$
P_0 = P^!_0 + \delta_0 = \text{Poisson}(\lambda \cdot \ell) + \text{ (a point at 0)}.
$$

즉, $N$ 의 Palm distribution 은 *원점에 점을 하나 추가한* 과정의 분포이다.

이를 더 명확히: Palm distribution 하에서 샘플 경로를 보면:
- 원점 0 에는 반드시 점이 있다 ($\delta_0$ 기여).
- 나머지 점들은 독립적으로 율 $\lambda$ 의 Poisson 분포를 따른다.

**보조 결과 — 1D Poisson 의 Palm 통계**:

(i) Palm distribution 하에서 0 다음 점까지의 거리 $D_0$: $D_0 \sim \text{Exp}(\lambda)$ (나머지 Poisson 의 첫 번째 점이므로).

(ii) Stationary case 에서 Palm distribution 은 *renewal theory* 의 *length-biased* 관점과 연결됨: 임의 시점 $t$ 에서 가장 가까운 이전 점까지의 거리 $A$ 와 다음 점까지의 거리 $B$ 는 독립 Exp($\lambda$) (Poisson 의 memoryless 성질).

**광학적 해석**: 시간 축 1D 예시가 *단일 광수용기* 에 도달하는 광자 스트림. Rate $\lambda$ 의 시간적 Poisson 과정. Palm distribution 하에서 "방금 광자가 도달했다" 조건이면 다음 광자는 Exp($\lambda$) 로 도달 — memoryless. 이것이 rod 의 연속적 광자 응답 이론의 기초이다.

**일반화**: 공간-시간 $(\Sigma_{\text{ret}} \times \mathbb{R}^+)$ 위 비동차 과정에서 Palm distribution 은 $\Lambda$-weighted 적분 평균 — Campbell-Mecke 가 이를 컨트롤.

### 5.4 광자-중심 관점

Palm calculus 가 광자 stage 에서 자연스러운 이유: **광수용기는 "광자 1개" 를 unit 으로 응답** (Baylor 1979). 따라서 광수용기 응답을 "전체 광자 configuration" 보다 "광자 하나의 관점" 에서 회계하는 것이 자연.

Campbell-Mecke (Thm 4.3) 가 이 회계의 정확한 도구를 제공:

$$
\mathbb{E}[\text{rod response}] = \mathbb{E}\!\left[\sum_{x \in N} r_1(t - t_x, x, \nu_x)\right] = \int r_1(t - s, x, \nu) \, \Lambda(dx, ds, d\nu)
$$

이는 [[03_stage1_photoreceptor_sde|03]] 의 $\mathcal{K}_1$ 정의에서 직접 사용.

---

## 6. 조건화와 filtration

### 6.1 History σ-algebra

시간 $t$ 까지의 history:

$$
\mathcal{F}_t := \sigma\left( \{ N(B) : B \in \mathcal{B}_\mathcal{X}, B \subset \mathcal{X}_{\leq t} \} \right)
$$

여기서 $\mathcal{X}_{\leq t} := \Sigma_{\text{ret}} \times [0, t] \times \Lambda$.

**Lemma 6.1 (Causality of Poisson)**. Inhomogeneous Poisson 은 *시간 increment 가 독립*: $t_1 < t_2$ 에 대해 $N(\mathcal{X}_{\leq t_2}) - N(\mathcal{X}_{\leq t_1})$ 는 $\mathcal{F}_{t_1}$ 와 독립.

이는 (P1) 의 시간-disjoint 적용. Pipeline 의 인과성 (TC-SP-1.3) 의 stage 0 측 보장.

### 6.2 Doob-Meyer 분해와 보상측도

**Theorem 6.2 (Doob-Meyer for counting processes)**. $N_t := N(\mathcal{X}_{\leq t})$ 는 $(\mathcal{F}_t)$-submartingale. Doob-Meyer 분해에 의해 고유한 예측가능 (predictable) 증가 과정 $A_t$ (보상측도, compensator) 가 존재하여:

$$
M_t := N_t - A_t \text{ 는 } (\mathcal{F}_t)\text{-local martingale.}
$$

Inhomogeneous Poisson 의 경우 보상측도는 결정론적:

$$
A_t = \Lambda(\mathcal{X}_{\leq t}) = \int_0^t \int_{\Sigma_{\text{ret}} \times \Lambda} \lambda(x, s, \nu) \, dx \, d\nu \, ds.
$$

따라서 $M_t = N_t - \Lambda(\mathcal{X}_{\leq t})$ 는 *martingale* (단순히 local 이 아님 — $\Lambda(t)$ 가 locally integrable 이므로).

**증명 스케치**: $N_t$ 가 submartingale 임을 확인: $\mathbb{E}[N_t | \mathcal{F}_s] = N_s + \mathbb{E}[N_t - N_s | \mathcal{F}_s] = N_s + \Lambda_s^t$ (독립 증분). 이를 재정렬하면 $N_t - \Lambda_t = N_s - \Lambda_s + (N_s^t - \Lambda_s^t)$. 후자의 $\mathcal{F}_s$-조건부 기댓값이 0 이면 (독립 증분으로부터) $M_t$ 가 martingale. $\square$

**강도 과정 (predictable)**. 일반 점과정 이론 (비-Poisson) 에서 보상측도는 예측가능한 확률적 강도 과정 $\tilde\lambda_t$ 로 표현될 수 있다:

$$
A_t = \int_0^t \tilde\lambda(s) \, ds.
$$

$\tilde\lambda$ 가 존재하면 점과정을 "stochastic intensity $\tilde\lambda$" 로 완전히 characterize 할 수 있다. Poisson 의 경우 $\tilde\lambda(x, t, \nu) = \lambda(x, t, \nu)$ (결정론적).

**SDE 연결**: $M_t = N_t - A_t$ 를 미분 형태로 쓰면:

$$
dN_t = dA_t + dM_t = \lambda(x, t, \nu) \, dt + dM_t.
$$

이것이 [[03_stage1_photoreceptor_sde|03]] 의 막전위 SDE 에서 $dN$ 항의 정확한 형태 — $\lambda \, dt$ 는 예측가능 부분, $dM_t$ 는 martingale 잡음 부분.

### 6.3 Cox process (이중 확률 Poisson) 와의 연결

**Definition 6.3 (Cox process / Doubly stochastic Poisson)**. 강도 측도 $\Lambda$ 자체가 확률적인 경우: $\Lambda(\omega)$ 가 확률변수 (random measure), 그 조건부로 $N | \Lambda \sim \text{Poisson}(\Lambda)$. 이를 *Cox process* (doubly stochastic Poisson) 라 한다.

Cox process 의 marginal 통계:

$$
\mathbb{E}[N(B)] = \mathbb{E}[\Lambda(B)], \quad \text{Var}[N(B)] = \mathbb{E}[\Lambda(B)] + \text{Var}[\Lambda(B)].
$$

분산이 평균보다 크다 — *super-Poissonian*. 이것이 coherence 효과 (§2.4.4) 를 흡수하는 자연스러운 방법 (OP-SP-001 의 해법 후보 (B)).

**광학에서의 Cox process**: 조명 자체가 fluctuate 하는 경우 (예: 구름 뒤 태양, 깜빡이는 광원). $\Lambda(\omega)$ 가 조명 fluctuation 을 반영. 이 경우 photon statistics 는 super-Poissonian 이고 추가 "photon noise beyond shot noise" 가 생긴다.

**Predictable intensity connection**: Cox process 의 강도 과정 $\tilde\lambda$ 는 random (condition on $\Lambda$). Doob-Meyer 보상측도가 random 이 된다. 이것이 일반 강도 과정 (predictable 강도) 이론과 Cox process 의 연결 지점.

---

## 7. Photoreceptor 측 — Stage 0 의 한계

본 stage 의 출력은 광자 발생점 configuration. 광수용기의 응답은 [[03_stage1_photoreceptor_sde|03]] 의 $\mathcal{K}_1$ 이 정의. 그러나 *Stage 0 단의 사실들* 이 03 의 입력을 제약함:

### 7.1 Single-photon resolution (Rod 의 SPAD-like 측면)

**Empirical fact** (Baylor, Lamb, Yau 1979): 어두운 조건의 rod 는 단일 광자 흡수에 대해 *측정 가능한* 응답을 생성.

수학적 함의: $\mathcal{K}_1$ 의 입력은 *광자 단위* configuration 으로 충분 해상. 적분된 intensity 만 받는 모델 (CMOS-like) 은 *상실된* 정보가 있음.

### 7.2 Photon noise limit

식별 가능한 시각 자극의 *최소 광자 수* (psychophysical Hecht-Shlaer-Pirenne 1942):

- 5–7 개의 흡수된 광자가 검출 임계
- 각 광자는 *독립* (Poisson 가정)

이는 Stage 0 의 정보 한계를 직접 결정. 어떤 후속 stage 도 이 한계 *밑* 으로는 갈 수 없음 (TC-SP-1.2, DPI).

### 7.3 Photon number-phase uncertainty — Sub-Poissonian 과 Super-Poissonian 정권

#### 7.3.1 Mandel Q 매개변수

광자 수 통계의 비-Poissonian 정도를 정량화하는 표준 척도는 **Mandel Q parameter** (Mandel 1979):

$$
Q := \frac{\text{Var}[N] - \overline{N}}{\overline{N}} = \frac{\text{Var}[N]}{\overline{N}} - 1.
$$

(Mandel-Wolf §9.8, eq. 9.8-4.) 해석:

- $Q = 0$: Poisson (shot noise limit)
- $Q > 0$: super-Poissonian (over-dispersed, 예: thermal, bunched)
- $Q < 0$: sub-Poissonian (under-dispersed, 예: antibunched, Fock state)

$Q$ 의 Fano factor 와의 관계: Fano factor $F = \text{Var}[N]/\overline{N} = 1 + Q$.

#### 7.3.2 Number-Phase 불확정성 관계

양자광학에서 광자 수 $\hat n$ 과 위상 $\hat\phi$ 는 정준 켤레 관계:

$$
\Delta n \cdot \Delta \phi \geq \frac{1}{2}.
$$

(이것은 Robertson-Schrödinger 불확정성 원리의 $(\hat n, \hat\phi)$ 버전; Mandel-Wolf §11.6.) 결과:

- **Coherent state** ($|\alpha\rangle$): $\Delta n = |\alpha|$, $\Delta\phi = 1/(2|\alpha|)$ — Poisson, $Q = 0$.
- **Fock state** ($|n\rangle$): $\Delta n = 0$, $\Delta\phi = \infty$ — perfect photon number, sub-Poissonian, $Q = -1$.
- **Thermal state**: $\Delta n = \bar n \sqrt{1 + 1/\bar n} > \sqrt{\bar n}$ — super-Poissonian, $Q = \bar n$.
- **Squeezed number state**: $\Delta n < \sqrt{\bar n}$ — sub-Poissonian, $Q < 0$.

#### 7.3.3 Sub-Poissonian 광원의 예시

**단일 quantum emitter (single-photon source)**: 두 광자를 동시에 방출할 수 없으므로 $g^{(2)}(0) = 0$ — perfect antibunching. 이를 달성하려면 단일 원자/분자/quantum dot 를 cavity 안에서 excite.

**Resonance fluorescence**: 강한 laser 로 구동되는 단일 원자는 antibunching 보임 (Kimble, Dagenais, Mandel 1977 — 최초 실험적 antibunching 관측).

#### 7.3.4 인간 시각에서의 위치 — Poisson 한계

인간 시각에서 $Q \approx 0$ 의 이유:

1. **광원 통계**: 자연광은 §2.4 의 다중-모드 분석으로 Poisson 으로 수렴.
2. **rod 의 내재적 잡음**: 열적 이성질화 (thermal isomerization) 에 의한 *dark noise* 자체가 Poisson 과정 — 따라서 실제 신호 + 잡음의 합도 Poisson.
3. **측정 한계**: Hecht-Shlaer-Pirenne (1942) 의 역치 측정이 Poisson 통계를 가정하면 완벽히 설명됨 — $Q \neq 0$ 이면 역치 값이 달라질 것이다.
4. **자연 환경에서의 quantum 효과의 크기**: 일상 조명 아래 $\bar n \sim 10^4$-$10^6$ photons per rod per second, $Q = \bar n_{\text{mode}} \cdot (M^{-1}) \approx 10^{-10}$ — 완전 무시 가능.

**결론**: 인간 시각은 *Poisson 한계* (shot noise limit) 에 있다. 이는 생물학적 성취가 아니라 물리적 필연 — quantum 광학적 최적 설계가 Poisson 을 선택하는 것이다.

---

## 8. Theorem-Candidates

### TC-SP-0.1a — [DELETED 2026-05-25 Pass 8]

**Status**: **DELETED via Pass 8** (2 patterns HOLE — original 9-pattern survivor finally cracks).

- **#7 implicit regularity smuggle**: "Density of Λ w.r.t. reference measure" silently assumes Radon-Nikodym absolute continuity ($\Lambda \ll \mu_{\text{ref}}$). 정리 자체의 hypothesis 가 아닌 *명사구 안에 hidden*. PGF/Tonelli interchange 도 verify 안 됨.
- **#28 subset support (mild)**: Stated "all Poisson PP" iff product Janossy 이나, atomic Λ excluded silently (§2.2 Note 의 "simple — atomless" 가정 우회). Subset 이 stated full domain 보다 좁음.

**Original statement (preserved for audit trail)**:

> Stage 0 의 Poisson 점과정 $N \sim \text{Poisson}(\Lambda)$ 의 모든 finite-dimensional 통계는 강도 측도 $\Lambda$ 만으로 결정된다.

**Why DELETED**: 본 TC 가 sensing pipeline corpus 의 *마지막 9-pattern survivor* 였으나 Pass 8 의 *meta-mathematical attacks* (#7 regularity, #28 subset support) 에서 *load-bearing 가정이 statement 밖에 hidden* 임이 노출. Radon-Nikodym 과 simple-process 가정의 *명시화* 가 fix 의 길이나, *현재 형식* 으로는 자격 박탈.

**Replacement**: §3-§5 본문의 Poisson + Janossy 도구 reference 는 *generic mathematical reference* 로 유지. *Theorem-candidate* 자격 박탈. TC-SP-R-1 (with explicit Radon-Nikodym hypothesis) 가 후속 version.

> Stage 0 의 점과정 $N \sim \text{Poisson}(\Lambda)$ 의 모든 finite-dimensional 통계는 강도 측도 $\Lambda$ 만으로 결정된다.

**증명 가능성**: Poisson 분포의 정의로부터 직접. Janossy density (Defn 2.3) 가 이미 product 형태이므로 finite-dimensional distribution 도 모두 $\Lambda$ 에 의해 결정.

**의미**: Stage 0 의 모든 통계적 행동은 Λ 로 환원.

### TC-SP-0.1b (Factorization formula) — [DELETED 2026-05-25 Pass 3]

**Status**: **DELETED via Pass 3 adversarial verification** (2-pattern HOLE: #18 tautology + #5 hypothesis recheck).

**Original statement (preserved for audit trail)**:

> Λ 는 $L_{\text{ret}} \cdot T_{\text{optics}} \cdot \eta \cdot (h\nu)^{-1}$ 의 곱 (장면 광휘 × 광학 투과 × 양자 효율 × 광자 에너지^{-1}).

**Refute basis**:

- **#18 (tautology)**: $\Lambda = L \cdot T \cdot \eta \cdot (h\nu)^{-1}$ 는 §2.5 Defn 2.4 의 *정의* — 정리가 정의 재진술.
- **#5 (hypothesis)**: Stiles-Crawford 효과 (cone 의 입사 방향 의존성) 가 "marginalize-direction" 가정 위반; intraocular scatter (aging lens) 가 $T_{\text{optics}}$ 의 pure-transmittance 가정 위반.

**Why deleted**: Factorization 은 *radiative transfer 의 단순 책기록* 이지 정리 아님. Physical hypothesis (no Stiles-Crawford, no scatter) 가 generic 아님.

**Replacement (없음)**: §2.5 의 Definition 2.4 (radiative-transfer 분해) 본문 유지 — *정의* 로서. TC 자격 박탈. 외부 3-tuple 입력 자체는 framework 의 *premise* 로 유지.

### TC-SP-0.2 — [DELETED 2026-05-25 Pass 5 #11 model misspecification]

**Status**: **DELETED via Pass 5 #11 (model misspecification)**. Math (Poisson Taylor expansion at Λ→0) is sound but proof handles *photon arrival* order statistics, while the biological claim is about *rod detection* (hidden Markov rhodopsin cascade with single-quantum amplification + thermal isomerization noise). Same fundamental conflation as deleted TC-SP-1.5 (single-photon detectability).

**Original statement (preserved for audit trail)**:

> $\Lambda(B) \to 0$ 극한에서 $\Pr[N(B)=1] \approx \Lambda(B) - O(\Lambda^2)$, $\Pr[N(B)=2] = O(\Lambda^2)$ → 1차 사건 dominate.

**Why DELETED**: Photon arrival Poisson Taylor expansion 이 *abstract* 으로 자명하나, "어두운 조건에서 망막은 1차 사건만 본다" 의 *biological claim* 은 rod 의 stochastic 증폭 cascade + threshold detection 의 별도 분석 필요. Math 와 biology 가 *다른 객체*. TC 라벨 박탈.

**Replacement**: Mathematical observation (Poisson Taylor expansion) 은 §3 본문 유지 — *technical fact* 로. Baylor 1979 단광자 검출 은 *empirical observation* (§7.1 본문) 으로 유지. *Theorem-candidate* 자격 박탈.

이 TC-SP 는 [[03_stage1_photoreceptor_sde|03]] 의 *single-photon impulse response* $r_1(t)$ 개념의 정당화.

### TC-SP-0.3 (보조 candidate: Slivnyak 기반 합성 독립성)

> 강도 측도들이 $\Lambda = \Lambda_A + \Lambda_B$ 인 두 독립 광원 A, B 의 합산 Poisson 과정 $N = N_A + N_B$ 에서, Slivnyak-Mecke (Theorem 4.4) 에 의해: $N_A$ 의 한 점의 존재는 $N_B$ 의 분포에 영향을 주지 않는다.

**증명 가능성**: Poisson superposition theorem (두 독립 Poisson 의 합은 Poisson) + Slivnyak-Mecke 의 직접 적용.

**의미**: 독립 광원들의 광자들은 *서로의 통계에 영향을 주지 않는다* — 양자물리적 사실 (photon independence) 의 정확한 수학적 표현.

---

## 9. Open Problems

### OP-SP-001: 양자 coherence 무시의 정당화 한계

**Status**: OPEN. Severity: Low.

**문제**: Poisson 가정 (§2.4) 은 *incoherent 광원* 에 대해 정당화됨. 그러나 다음 경우들에서는 부정확:

1. *형광/인광 emission*: photon bunching (super-Poissonian)
2. *Laser*: ideal laser 는 Poisson, 그러나 modulated laser 는 sub-Poissonian
3. *Quantum imaging / parametric down-conversion*: pair-correlated photons, $g^{(2)}(0) < 1$
4. *지각 한계 실험*: ROC at threshold 에서 quantum correlation 이 양식적 효과를 줄 수 있음

**자연 환경에서의 실제 영향**:
- 대부분의 일상 광원 (태양, 백열, 형광등의 평균) 은 Poisson 정확
- 산란 광 (cloud, fog) 도 Poisson 정확
- 단, 특정 인공 환경 (laser pointer, single-photon source) 에서는 deviation
- 망막 통합 시간 ($\sim$ ms) 동안 평균화되면 대부분 무시 가능

**candidate 해법**: 
- (A) 광원 클래스를 *Poisson 가정이 정확한 부류로 제한* 하고 명시
- (B) Poisson 을 *Cox process* 로 일반화 (rate 자체가 random) — coherence 효과를 stochastic intensity 로 흡수 (§6.3 참조)
- (C) Mandel-Wolf coherence 이론을 직접 도입 — 이론 비용 크지만 정확

본 디렉토리는 (A) 를 default 로. 확장 시 (B).

---

## 10. $\mathcal{K}_1$ 의 입력 type — 엄밀한 해명

[[03_stage1_photoreceptor_sde|03]] 는 stage 0 의 출력을 받아 stage 1 (광수용기 graded 전위) 로 보내는 kernel $\mathcal{K}_1 : \mathcal{S}_0 \to \mathcal{S}_1$ 을 정의한다. *무엇이 실제로 전달되는가?*

### 10.1 세 가지 동치 표현

Stage 0 의 출력은 다음 세 표현 중 어느 것으로도 볼 수 있다:

**표현 A (Counting measure)**:
$$N = \sum_i \delta_{(x_i, t_i, \nu_i)} \in \mathcal{N}(\mathcal{X}).$$

이것이 $\mathcal{S}_0$ 의 *canonical* 표현. 가측 공간은 최대한 추상적.

**표현 B (Time-ordered stream)**:
$$((x_1, \nu_1), t_1), ((x_2, \nu_2), t_2), \ldots \quad t_1 < t_2 < \ldots$$

각 광자를 시각으로 정렬한 무한 (또는 유한) 수열. 광수용기 응답은 이 스트림을 인과적으로 처리.

**표현 C (Intensity measure)**:
$$\Lambda(dx \, dt \, d\nu) = \lambda(x, t, \nu) \, dx \, dt \, d\nu.$$

이것은 $N$ 의 *평균* 이지 random realization 이 아니다. $\Lambda$ 만 받는 stage 1 모델은 *shot noise 를 무시한 mean-field 근사*.

세 표현은 동치: A ↔ B (atomic list 의 다른 view), A ↔ C (A 의 기댓값이 C). 그러나 통계적으로는 A 와 C 가 *다른 정보*를 전달한다.

### 10.2 Shot noise 포함 여부 — 결정적 구별

$\mathcal{K}_1$ 이 *counting measure* (표현 A) 를 입력으로 받으면: 각 실현 $N$ 마다 discrete jump 들이 막전위 SDE 에 입력됨 — shot noise 완전 포함.

$\mathcal{K}_1$ 이 *intensity measure* (표현 C) 만 받으면: $dN \approx \lambda \, dt$ 의 결정론적 근사 — shot noise 상실. 이는 mean-field 또는 diffusion 근사.

**본 framework 의 선택**: $\mathcal{K}_1$ 은 counting measure (표현 A) 를 받는다. [[03_stage1_photoreceptor_sde|03]] 의 SDE 가 $dN$ 항을 *discrete jump* 로 다루는 이유가 여기에 있다:

$$
dV_p(t) = [f(V_p) + I_{\text{dark}}(t)] \, dt + r_1 \cdot dN_p(t) + \sigma_V \, dW_t
$$

여기서 $dN_p(t) = \sum_i \delta(t - t_i^{(p)})$ 가 픽셀 $p$ 에서의 counting measure 의 미분.

### 10.3 평균 응답의 Campbell 표현

*평균* 막전위를 계산할 때는 Campbell (Theorem 4.1) 이 자동으로 counting measure → intensity 로 환원:

$$
\mathbb{E}[V_p(t)] = V_{\text{rest}} + \int_{-\infty}^{t} \int_{\Sigma_p \times \Lambda} r_1(x, t - s, \nu) \, \Lambda(dx, ds, d\nu)
$$

여기서 $\Sigma_p$ 는 픽셀 $p$ 의 absorption 영역. 이 공식은 shot noise 를 평균화해버리지만 mean response 는 정확하다.

**요약**:

| 무엇을 받는가 | shot noise | 적합 모델 |
|------------|-----------|---------|
| Counting measure $N$ | 포함 | 완전 확률적 SDE |
| Intensity $\Lambda$ | 무시 | Mean-field / rate-code 근사 |

본 framework 는 전자 — stage 0 는 counting measure 를 stage 1 에 넘긴다.

---

## 11. Stage 0 의 (Ω, σ) Tier 2 mapping (preview)

[[07_omega_sigma_lift|07]] 에서 본격 전개. 본 stage 의 직접 매핑:

- $\Omega_0 = N$ 의 atomic 점들 = 광자 발생 사건 집합
- $\sigma_0(x_i, x_j) \iff \|t_i - t_j\| < \tau \text{ AND } |x_i - x_j| < \delta$ (시공간 인접; $\beta$ 옵션)

따라서 Stage 0 자체가 이미 $(Ω_0, \sigma_0)$ 형태의 Tier 2 객체를 제공. 이게 *최소 가공 Raw* 의 물리적 실현 ([[../prolegomena/00_field_conditions_v0|prolegomena C1–C5]] 가 요구한 *비-함수*, *비-공간*, *비-상태* 조건과 정합).

### 11.5 Two-point correlation in the visual periphery

**경험적 사실**: 자연 장면 (natural scene) 은 픽셀 수준에서 *통계적으로 구조화된* 상관을 가진다. 특히 1/f 스펙트럼 — spatial power spectrum $S(f) \propto 1/f^2$ — 이 자연 이미지의 표준 통계 (Field 1987; Ruderman & Bialek 1994).

이것이 stage 0 의 광자 도래 *공간* 상관에 어떤 영향을 주는가?

**광자 도래 공간 상관**: 장면 radiance $L(x, \nu)$ 가 공간 상관

$$
C_L(x_1, x_2) := \mathbb{E}[L(x_1, \nu) L(x_2, \nu)] - \mathbb{E}[L(x_1, \nu)] \mathbb{E}[L(x_2, \nu)]
$$

을 가질 때, 광자 도래의 *조건부 Poisson 통계* (즉 Cox process, §6.3) 의 two-point correlation 은:

$$
\text{Cov}[N(B_1), N(B_2)] = \underbrace{\Lambda(B_1 \cap B_2)}_{\text{Poisson 기여 (diag 만)}} + \underbrace{\int_{B_1 \times B_2} C_\lambda(x_1, x_2) \, dx_1 \, dx_2}_{\text{장면 통계 기여}}.
$$

첫째 항은 §3.4 의 Poisson covariance ($B_1 \cap B_2 = \emptyset$ 이면 0). 둘째 항이 *장면 구조* 에 의한 추가 상관이다.

**말초 시야에서의 구체적 구조**: 말초 시야 (eccentricity $e > 5°$) 에서:

- 광수용기 spacing $\sim 5$–$30 \, \mu\text{m}$ (eccentricity 증가와 함께 증가)
- 수용야 크기 $\sim 1$–$5°$ (시각도)
- 인접 수용기들의 spatial correlation $C_L(x_1, x_2)$: 자연 이미지의 1/f 통계로부터

$$
C_L(r) \approx \sigma_L^2 \cdot \exp\!\left(-\frac{r}{r_c}\right), \quad r_c \sim 0.5°\text{–}2° \text{ (자연 장면 correlation length)}.
$$

(Field 1987; Simoncelli & Olshausen 2001.)

**수용기 쌍 간의 공분산**: 거리 $r = \|x_1 - x_2\|$ 의 수용기 쌍에서 광자수 공분산:

$$
\text{Cov}[N_1, N_2] \approx \eta^2 \cdot C_L(r) \cdot (\Delta t)^2 / (h\nu)^2 \cdot A_{\text{rec}}^2
$$

여기서 $A_{\text{rec}}$ 은 수용기 면적, $\Delta t$ 는 통합 시간.

**단계 2 (inner retina) 와의 연결**: 이 two-point correlation 이 stage 2 의 *center-surround 수용야* 의 설계에 반영된다 — DoG 필터 (§4.4 of 01) 의 최적 매개변수는 이 correlation length $r_c$ 에 맞춰 조율됨 (Srinivasan, Laughlin, Dubs 1982 의 efficient coding 원리). Stage 0 의 공간 상관이 이미 stage 2 의 구조를 *예측*한다.

**말초 특화**: 중심와 (fovea) 에서는 수용기 밀도가 높고 수용기 크기가 작아 sampling limit 이 지배적. 말초에서는 수용기 크기가 커서 각 수용기 내부의 공간 평균 효과가 크다 — 말초 수용기는 넓은 영역의 광자를 통합하므로 이웃 수용기와의 상관이 더 강하다. 이 비등방성 상관 구조가 stage 2 의 peripheral vs. foveal 처리 비대칭성의 stage 0 측 물리적 원인이다.

---

## 12. 본 문서가 *시도하지 않는 것*

- Single-photon impulse response $r_1$ 의 정확한 형태 (→ 03)
- 광수용기 SDE 의 동역학 (→ 03)
- Pre-retinal 산란/회절 (→ 외부 광학 모델)
- Coherence 효과의 정확한 처리 (→ OP-SP-001)
- 분광 (color) 의 *지각* 측면 (이는 stage 1 의 cone 종류 분리에서 시작; 이 stage 는 spectral mark $\nu$ 만 carry)

---

## 13. 도구 사용 summary (cross-reference to [[01_framework_master#4. 수학적 도구 카탈로그|01 §4]])

본 stage 에서 *실제로* 사용된 도구:

| 도구 (§4.X) | 사용 객체 |
|------------|----------|
| 4.1 점과정 | Inhomogeneous Poisson MPP, Janossy, Campbell, Slivnyak-Mecke, Palm, cumulant, $g^{(2)}$, Doob-Meyer, Cox |
| 4.8 정보이론 | TC-SP-0.2 의 단광자 한계; §7.3 Mandel Q |

다른 도구들 (SDE, convolution, scale-space 등) 은 stage 0 에서 *직접* 사용되지 않음. 적분된 결과 ($\mathcal{K}_1$ 통과 후) 에서 등장.

---

*Stage 0 v1. 후속: [[03_stage1_photoreceptor_sde]]. TC-SP-0.1, TC-SP-0.2, TC-SP-0.3 등록. OP-SP-001 등록. 심화: Janossy 동치 증명, Mandel-Wolf coherence primer (§2.4.1–2.4.5), RTE 광자율 도출 (§2.5.1–2.5.3), 분산 완전 도출 (§3.4), 모든 cumulant (§3.5), $g^{(2)}$ 4가지 비교 (§3.6), Campbell-Mecke 증명 스케치 (§4.3), Slivnyak 증명 스케치 (§4.4), Palm 1D 예시 (§5.3), Doob-Meyer + Cox (§6.2–6.3), Mandel Q + number-phase (§7.3), K₁ 입력 type 해명 (§10), peripheral two-point correlation (§11.5).*
