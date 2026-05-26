---
type: working/sensing_pipeline/framework
version: v1
date: 2026-05-25
status: DEFINITION-DRAFT
purpose: |
  Master architecture for the sensing pipeline.
  Defines the Stratified Stochastic Kernel Pipeline,
  surveys the full mathematical toolkit deployed across stages,
  states three abstract theorem-candidates (TC-SP-1.1, 1.2, 1.3)
  with proof sketches at the DEFINITION-DRAFT register.
  All subsequent documents (02–07) inherit the types and notation defined here.
register: DEFINITION-DRAFT (objects) + THEOREM-CANDIDATE (propositions with proof sketches; no canonical proofs)
constraint_compliance:
  canonical_theorem_changes: 0
  claim_count: 102 (unchanged)
  CV_version: CV-1.20 (unchanged)
  scc_edits: 0
  pai_canonical_edits: 0
---

> [!nav] Parent: [[00_INDEX]] · Next: [[02_stage0_photon_point_process]] · Substrate: [[canonical|canonical.md (CV-1.20)]] · Parallel: [[perception_action_interpretation_pivot_2026_05_21|PAI Pivot]]

# Framework Master — Stratified Stochastic Kernel Pipeline

## 0. 본 문서의 위치

본 문서는 sensing pipeline 디렉토리의 *마스터 골격*이다. 02~07 의 모든 stage / cross-cutting 문서는 본 문서에서 정의한 **타입**, **표기**, **추상 객체** 를 직접 인용한다. 본 문서 단독으로 자기-완결 (stage-agnostic) 이어야 한다.

본 문서가 *수행하는 것*:
- 5단계 pipeline 의 측도론적 골격 확립
- 각 단계 사이를 잇는 Markov kernel 의 정의·합성 규칙
- 단계별로 deploy 될 모든 수학 도구의 카탈로그
- 추상 수준 (stage-agnostic) 의 theorem-candidates (+ DEFINITION-DRAFT 등록 수준의 proof sketch)
- 대안 형식주의와의 비교 (왜 SSKP 가 적합한가)

본 문서가 *수행하지 않는 것*:
- 어느 stage 의 구체 동역학도 적지 않음 (02~05 의 역할)
- 어느 candidate 도 *canonical-register proof* 를 시도하지 않음 (proof sketch 만; full proof 는 별도 plan)
- (Ω, σ) Tier 2 lift 의 구체 형식은 07 로 미룸

---

## 1. 측도론적 기초

### 1.1 상태공간의 일반 형태

각 stage $i \in \{0, 1, 2, 3, 4\}$ 의 상태공간 $\mathcal{S}_i$ 는 다음 중 하나의 표준 클래스:

- **(P)**: 점과정 공간 $\mathcal{N}(\mathcal{X})$ — locally finite counting measures on Polish space $\mathcal{X}$
- **(F)**: 함수공간 $C(\mathcal{X} \times \mathbb{R}^+, \mathbb{R}^d)$ 또는 $L^p(\mathcal{X} \times \mathbb{R}^+, \mathbb{R}^d)$
- **(M)**: 측도공간 $\mathcal{M}^+(\mathcal{X})$ — locally finite positive measures
- **(D)**: 분포공간 $\mathcal{D}'(\mathcal{X})$ — Schwartz distributions (필요 시)

각 클래스는 표준적 σ-algebra 와 함께:

- (P) → vague topology 의 Borel σ-algebra (Daley-Vere-Jones §A2)
- (F) → uniform / Skorokhod / weak σ-algebra
- (M) → vague topology 의 Borel σ-algebra
- (D) → weak* σ-algebra

**가정 (G1, Polish)**: 모든 $\mathcal{S}_i$ 는 *Polish space* (완비 가분 거리화 가능). 이는 disintegration theorem, regular conditional probability, Kolmogorov extension 등을 무료로 사용하기 위함.

**가정 (G2, Borel)**: 모든 σ-algebra 는 Polish topology 의 Borel σ-algebra.

이 두 가정은 본 디렉토리 전체에서 *공통* 으로 가정. 명시적으로 약화하는 stage 가 있으면 그 stage 문서에서 표시.

### 1.1.1 Regular Conditional Probability 와 Disintegration

본 framework 가 의존하는 가장 중요한 측도론적 결과는 *disintegration theorem* 이다. 모든 conditioning 연산 (예: $\mathcal{K}_i(x, \cdot)$ 가 "주어진 입력 $x$ 에 대한 출력 분포") 가 이 정리로 정당화된다.

**Definition 1.1 (Regular Conditional Probability)**. 확률공간 $(\Omega, \mathcal{F}, \mathbb{P})$, 가측공간 $(\mathcal{Y}, \mathcal{B}_Y)$, 그리고 가측사상 $Y : \Omega \to \mathcal{Y}$ 와 sub-σ-algebra $\mathcal{G} \subseteq \mathcal{F}$ 가 주어졌을 때, **regular conditional probability** 는 함수 $\kappa : \Omega \times \mathcal{B}_Y \to [0, 1]$ 로:
1. 각 $\omega$ 마다 $\kappa(\omega, \cdot)$ 는 $(\mathcal{Y}, \mathcal{B}_Y)$ 위 확률측도.
2. 각 $B \in \mathcal{B}_Y$ 마다 $\kappa(\cdot, B)$ 는 $\mathcal{G}$-가측.
3. 모든 $B \in \mathcal{B}_Y$ 와 $G \in \mathcal{G}$ 에 대해
$$
\int_G \kappa(\omega, B) \, \mathbb{P}(d\omega) = \mathbb{P}(\{Y \in B\} \cap G).
$$

**Theorem 1.2 (Disintegration; Kallenberg "Foundations of Modern Probability" 3rd ed. Theorem 8.5 / §6.3)**. $\mathcal{Y}$ 가 Polish 이고 $\mathcal{B}_Y$ 가 그 Borel σ-algebra 라면, regular conditional probability $\kappa$ 가 **존재한다**. 또한 $\mathbb{P}$-a.s. 유일.

**Corollary 1.3 (Disintegration of joint measures)**. $\mathcal{X}, \mathcal{Y}$ 가 Polish 이고 $\pi$ 가 $\mathcal{X} \times \mathcal{Y}$ 위의 결합측도 (marginal $\pi_X$ on $\mathcal{X}$) 라면, kernel $\mathcal{K} : \mathcal{X} \to \mathcal{Y}$ 가 존재하여
$$
\pi(A \times B) = \int_A \mathcal{K}(x, B) \, \pi_X(dx), \quad A \in \mathcal{B}_X, B \in \mathcal{B}_Y.
$$

이 corollary 가 본 framework 의 *원동력*: 어느 두 인접 stage 의 결합분포 $\pi_{i-1, i}$ 가 주어지면 자동으로 kernel $\mathcal{K}_i$ 가 추출됨. 따라서 "kernel cascade" 모델은 *Polish-Borel 결합분포의 자연스러운 직조화* 와 동치이다 (Bayesian network 의 측도론적 base).

### 1.1.2 왜 Polish 가 필요한가 — 비-Polish 의 반례

Polish 가정 (G1) 은 *우연한 편의* 가 아니다. 비-Polish 공간에서는 disintegration 이 실패하는 *명시적 반례* 가 존재한다.

**반례 (Halmos)**: $\mathcal{Y} = [0, 1]$ 에 *non-Borel* 집합을 측정 가능 집합으로 추가하면 (즉, σ-algebra 가 Borel 보다 strictly larger), regular conditional probability 의 존재가 실패할 수 있다. Kallenberg §6 의 주석 참조.

**반례 (Dieudonné, 1948)**: 모든 분리가능 metric 공간이 Polish 인 것은 아니다 (완비성 결여). 비-완비 공간에서 정의된 random variable 의 disintegration 이 *어떤 versions of σ-algebra* 에서 실패.

**반례 (Banach-Kuratowski 가정 하)**: Continuum hypothesis 의 어떤 모델에서는 *$2^{\aleph_0}$-cardinality 의 unitary 측도공간* 위에 regular conditional probability 가 존재하지 않는다 (Pachl 1978; Faden 1985).

**교훈**: Polish-Borel 은 "측도론적 conditioning 이 안전한 *최대* 자연 클래스" 이다. 본 framework 가 이 클래스 내부에 머무는 한, *모든 stage 사이의 kernel 추출과 합성이 무조건 가능* 함이 보장된다. Polish 를 약화하면 (예: G_δ Lusin space, Suslin space) disintegration 이 *조건부로만* 가능 — 본 framework 는 이런 약화를 시도하지 않는다.

### 1.1.3 $\mathcal{N}(\mathcal{X})$ 위의 σ-algebra — 명시적 구성

점과정 stage (Stage 0, 3, 4) 의 상태공간 $\mathcal{N}(\mathcal{X})$ 는 Polish 임을 *명시적으로 확인* 해야 한다 (Daley-Vere-Jones Vol. I §9 / Vol. II §A2).

**Definition 1.4 (Locally finite counting measure)**. $\mathcal{X}$ Polish 위 측도 $N$ 이 **locally finite counting measure** 라 함은:
1. $N(B) \in \{0, 1, 2, \ldots, \infty\}$ for all $B \in \mathcal{B}_X$ (정수값).
2. $N(B) < \infty$ for all compact $B \subset \mathcal{X}$ (locally finite).

집합 $\mathcal{N}(\mathcal{X})$ 는 모든 locally finite counting measures 의 집합.

**Definition 1.5 (Evaluation maps)**. 각 Borel $B \in \mathcal{B}_X$ 에 대해 evaluation map
$$
\mathrm{ev}_B : \mathcal{N}(\mathcal{X}) \to \overline{\mathbb{N}}, \quad N \mapsto N(B).
$$

**Definition 1.6 (Counting measure σ-algebra)**. $\mathcal{N}(\mathcal{X})$ 위의 σ-algebra $\mathcal{B}_{\mathcal{N}}$ 는 *evaluation maps 의 family* $\{\mathrm{ev}_B : B \in \mathcal{B}_X \text{ compact}\}$ 가 가측이 되도록 하는 *최소* σ-algebra.

**Proposition 1.7**. $\mathcal{B}_{\mathcal{N}}$ 는 다음과 동치:
- $\mathcal{N}(\mathcal{X})$ 위 vague topology 의 Borel σ-algebra (vague convergence: $\int f \, dN_n \to \int f \, dN$ for compactly supported continuous $f$).
- $\mathcal{N}(\mathcal{X})$ 위 *weak topology* 의 Borel σ-algebra (Polish 한 경우 일치).

증명 스케치: vague topology 의 sub-base 가 $\{N : N(B) > a\}$ 형태이며 이는 정확히 $\mathrm{ev}_B^{-1}((a, \infty])$. 따라서 두 σ-algebra 는 일치 (Kallenberg §4.1).

**Proposition 1.8 ($\mathcal{N}(\mathcal{X})$ 의 Polish 성)**. $\mathcal{X}$ 가 Polish 이고 locally compact 이면 $\mathcal{N}(\mathcal{X})$ 는 vague topology 에서 Polish.

증명 스케치: $\mathcal{N}(\mathcal{X})$ 가 measurable map 의 image 로서 Polish (Kallenberg Theorem A2.3). Locally compact 조건은 *vague 와 weak 의 동치* 와 *separability* 를 보장.

**본 framework 에의 함의**: Stage 0 의 $\mathcal{X} = \Sigma_{\text{ret}} \times \mathbb{R}^+ \times \Lambda$ 가 Polish + locally compact (Euclidean compact × Polish × compact interval) 이므로 $\mathcal{N}(\Sigma_{\text{ret}} \times \mathbb{R}^+ \times \Lambda)$ 가 Polish. Stage 3, 4 도 유사. 따라서 *모든 stage 가 G1 만족*.

### 1.2 구체적 stage 공간 (preview, 자세한 정의는 02~05)

| Stage | 공간 형태 | 표기 | 의미 |
|-------|----------|------|------|
| 0 | (P) | $\mathcal{S}_0 = \mathcal{N}(\Sigma_{\text{ret}} \times \mathbb{R}^+ \times \Lambda)$ | 광자 marked point process |
| 1 | (F) | $\mathcal{S}_1 = C(\Sigma_{\text{ret}} \times \mathbb{R}^+, \mathbb{R})$ | 광수용기 graded 막전위 |
| 2 | (F) | $\mathcal{S}_2 = \bigoplus_{c \in \mathcal{C}} C(\Sigma_{\text{ret}} \times \mathbb{R}^+, \mathbb{R}^+)$ | 다채널 graded (ON/OFF, transient/sustained, 색, 방향) |
| 3 | (P) | $\mathcal{S}_3 = \prod_{c \in \mathcal{C}_g} \mathcal{N}(\mathbb{R}^+)$ | 신경절세포 평행 스파이크 트레인 |
| 4 | (P) | $\mathcal{S}_4 = \mathcal{S}_3$ + 채널-별 지연 | 시신경 도착 시점의 스파이크 트레인 |

- $\Sigma_{\text{ret}} \subset \mathbb{R}^2$: 망막 표면 (compact, $\partial \Sigma_{\text{ret}}$ smooth)
- $\Lambda \subset \mathbb{R}^+$: 파장 영역 (대략 380–780 nm)
- $\mathcal{C}$: stage 2 채널 색인 집합 (~$10^2$ 종류)
- $\mathcal{C}_g$: 신경절세포 채널 색인 집합 (~$10^6$ 개)

### 1.3 시간

본 디렉토리는 단일 연속 시간축 $t \in \mathbb{R}^+$ 을 default 로 사용. 단, **M / P / K 경로 latency 차이** (TC-SP-3.2 의 동기) 는 채널별 시간축 reparameterization 으로 다룬다. 추상 수준에서는 $\mathbb{R}^+$ 하나로 충분.

이산 시간 모델 (예: 프레임 기반 CMOS) 은 $\mathbb{R}^+ \to \{0, \Delta, 2\Delta, \ldots\}$ 의 sampling 연산으로 추가 stage 처럼 다룬다.

### 1.4 Filtration 과 predictable σ-algebra

연속 시간 stage 에서 *인과성* 을 형식화하려면 filtration 이 필요. 본 절은 §3.3 (인과 kernel) 과 §8.5 (인과 kernel 의 합성) 의 기반.

**Definition 1.9 (Filtration on a Polish state space)**. $\mathcal{S}$ 가 시간-인덱싱 가능한 Polish 공간 (예: $C(\mathbb{R}^+, \mathbb{R}^d)$ 또는 $\mathcal{N}(\mathcal{X} \times \mathbb{R}^+)$) 일 때, *natural filtration* 은
$$
\mathcal{F}^{\mathcal{S}}_t := \sigma\big( s \mapsto s|_{[0, t]} \big) \subseteq \mathcal{B}_{\mathcal{S}}, \quad t \geq 0.
$$
즉, $\mathcal{F}^{\mathcal{S}}_t$ 는 *시각 $t$ 까지의 사건만 결정하는* sub-σ-algebra.

**Definition 1.10 (Predictable σ-algebra)**. Stochastic process $X = \{X_t\}_{t \geq 0}$ 가 $\mathcal{F}_t$-adapted 일 때, *predictable σ-algebra* $\mathcal{P}$ 는 $\mathbb{R}^+ \times \Omega$ 위 left-continuous $\mathcal{F}_t$-adapted process 들에 의해 생성된 σ-algebra (Protter "Stochastic Integration and Differential Equations" Ch.4).

**의미**: predictable σ-algebra 는 "지금 *직전* 까지의 정보만 사용" 이라는 인과성의 가장 강한 형식. 본 framework 의 모든 kernel 은 *최소한 adapted*, 가능하면 *predictable* 이어야 함.

### 1.5 모니카-가산 합성 (Monotone class theorem) — 후속 lemma 의 도구

Lemma 2.3 의 증명에 사용되는 측도론적 *boilerplate*. 명시적으로 진술해둔다.

**Theorem 1.11 (Monotone Class Theorem; Kallenberg Theorem 1.1)**. $\mathcal{H}$ 가 함수의 집합으로:
1. 1 ∈ $\mathcal{H}$
2. $\mathcal{H}$ 는 선형
3. $\mathcal{H}$ 는 비음 단조수렴에 닫힘 ($0 \leq f_n \uparrow f, f_n \in \mathcal{H}, f \text{ bounded} \Rightarrow f \in \mathcal{H}$)

라면, $\mathcal{H}$ 가 어떤 π-system $\mathcal{C}$ 의 indicator 들을 모두 포함하면 $\sigma(\mathcal{C})$-가측한 모든 bounded 함수를 포함한다.

이 정리가 *kernel 합성의 measurability* 증명의 표준 도구.

---

## 2. Stochastic Kernel — 정의와 합성

### 2.1 정의

**Definition 2.1 (Markov / Stochastic Kernel)**. 측도공간 $(\mathcal{X}, \mathcal{B}_X)$ 와 $(\mathcal{Y}, \mathcal{B}_Y)$ 사이의 **stochastic kernel** $\mathcal{K} : \mathcal{X} \times \mathcal{B}_Y \to [0, 1]$ 은:

1. 모든 $x \in \mathcal{X}$ 에 대해 $\mathcal{K}(x, \cdot)$ 은 $(\mathcal{Y}, \mathcal{B}_Y)$ 위 확률측도.
2. 모든 $B \in \mathcal{B}_Y$ 에 대해 $\mathcal{K}(\cdot, B)$ 은 $\mathcal{B}_X$-가측.

**해석**: 입력 상태 $x$ 가 주어지면 출력 상태의 분포 $\mathcal{K}(x, \cdot)$ 가 결정됨.

### 2.1.1 결정론적 vs 진정한 stochastic kernel

**Definition 2.1a (Deterministic kernel)**. Kernel $\mathcal{K}$ 가 *결정론적* (또는 *Dirac*) 이라 함은: 어떤 가측사상 $f : \mathcal{X} \to \mathcal{Y}$ 가 존재하여 모든 $x$ 에 대해 $\mathcal{K}(x, \cdot) = \delta_{f(x)}$.

**Definition 2.1b (Strictly stochastic kernel)**. Kernel $\mathcal{K}$ 가 *strictly stochastic* 이라 함은 결정론적이지 않을 때 — 즉 어떤 $x$ 에 대해 $\mathcal{K}(x, \cdot)$ 가 한 점에 집중되지 않을 때.

**판별**. $\mathcal{K}(x, \cdot)$ 가 Dirac 인지 여부는 가측 — 결정론적 kernel 들의 집합은 strictly stochastic 들의 집합과 *측정 가능하게 분리됨* (Polish-Borel 환경에서). 본 framework 의 각 stage:

| Stage | Kernel type | 이유 |
|-------|-------------|------|
| 0 (입력 $\mu_0$ → 광자 도래) | strictly stochastic | Poisson sampling |
| 1 (광자 → 막전위) | strictly stochastic | 열적 noise (Wiener) |
| 2a (ON/OFF 분리) | deterministic | Riesz 분해는 함수 |
| 2b (DoG) | deterministic | linear convolution |
| 2c (운동 검출) | deterministic 또는 weakly stochastic | quadrature/Reichardt 의 noise 처리 방식 |
| 3 (LIF spiking) | strictly stochastic | Cox/Hawkes; spiking variability |
| 4 (latency shift) | deterministic | 시간 평행이동 |

**중요**: Stage 2 의 *내부 단계* (a, b, c) 들은 deterministic 이지만 *합성 $\mathcal{K}_2$* 는 *그 이전 stage 의 stochasticity 를 inherit* 하므로 효과적으로 stochastic. Deterministic kernel 의 카테고리적 위치: Markov category 의 *부분 카테고리* 로 임베딩 (객체 동일, 화살표는 deterministic 만).

### 2.2 표기

본 디렉토리에서 $\mathcal{K}_i : \mathcal{S}_{i-1} \to \mathcal{S}_i$ 는 stage $i-1 \to i$ 의 kernel. 통상 다음 세 표기 모두 사용:

- $\mathcal{K}_i(x, B) = \Pr[\text{stage } i \text{ output} \in B \mid \text{stage } i-1 \text{ input} = x]$
- $x \xrightarrow{\mathcal{K}_i} y \sim \mathcal{K}_i(x, \cdot)$
- $\mu \mapsto \mathcal{K}_i \mu := \int \mathcal{K}_i(x, \cdot) \mu(dx)$ (좌-작용; 측도 변환)

### 2.3 합성

**Definition 2.2 (Composition)**. 두 kernel $\mathcal{K}_1 : \mathcal{X} \to \mathcal{Y}$, $\mathcal{K}_2 : \mathcal{Y} \to \mathcal{Z}$ 의 합성:

$$
(\mathcal{K}_2 \circ \mathcal{K}_1)(x, C) := \int_\mathcal{Y} \mathcal{K}_2(y, C) \, \mathcal{K}_1(x, dy), \quad C \in \mathcal{B}_Z.
$$

**Lemma 2.3 (Composition is again a kernel)**. $\mathcal{K}_2 \circ \mathcal{K}_1$ 은 $\mathcal{X} \to \mathcal{Z}$ stochastic kernel.

**증명 (full sketch)**. 두 성질을 차례로 확인.

**(i) 확률측도성**. 고정된 $x \in \mathcal{X}$. $C \mapsto (\mathcal{K}_2 \circ \mathcal{K}_1)(x, C)$ 가 $\mathcal{B}_Z$ 위 확률측도임을 보인다.
- *비음성*: 피적분 $\mathcal{K}_2(y, C) \geq 0$.
- *공집합*: $\mathcal{K}_2(y, \emptyset) = 0 \Rightarrow$ 적분 0.
- *가산가법성*: $C_n \in \mathcal{B}_Z$ disjoint. $\mathcal{K}_2(y, \bigsqcup C_n) = \sum_n \mathcal{K}_2(y, C_n)$ (확률측도). 단조수렴 정리 (또는 Tonelli):
$$
\int \mathcal{K}_2(y, \bigsqcup C_n) \mathcal{K}_1(x, dy) = \int \sum_n \mathcal{K}_2(y, C_n) \mathcal{K}_1(x, dy) = \sum_n \int \mathcal{K}_2(y, C_n) \mathcal{K}_1(x, dy).
$$
- *정규화*: $\mathcal{K}_2(y, \mathcal{Z}) = 1$ for all $y$ (Dirac 또는 strictly stochastic 모두), 따라서 $\int 1 \cdot \mathcal{K}_1(x, dy) = \mathcal{K}_1(x, \mathcal{Y}) = 1$.

**(ii) 가측성**. 고정된 $C \in \mathcal{B}_Z$. $x \mapsto (\mathcal{K}_2 \circ \mathcal{K}_1)(x, C)$ 가 $\mathcal{B}_X$-가측임을 보인다.

함수 $g_C(y) := \mathcal{K}_2(y, C)$ 는 정의 (Def 2.1 의 2번) 에 의해 $\mathcal{B}_Y$-가측. 그러면
$$
h(x) := \int g_C(y) \, \mathcal{K}_1(x, dy)
$$
가 $\mathcal{B}_X$-가측임을 보여야 한다.

*Step 1*: $g_C = \mathbf{1}_B$ for $B \in \mathcal{B}_Y$ 인 경우. 이때 $h(x) = \mathcal{K}_1(x, B)$, 정의 (Def 2.1 의 2번) 에 의해 가측.

*Step 2*: $g_C$ 가 비음 단순함수 $\sum_k \alpha_k \mathbf{1}_{B_k}$ 일 때, $h(x) = \sum_k \alpha_k \mathcal{K}_1(x, B_k)$, 가측 함수의 유한합 — 가측.

*Step 3*: $g_C$ 가 비음 가측 — 단순함수 열 $g_n \uparrow g_C$ (Beppo-Levi 정리). 단조수렴
$$
h_n(x) = \int g_n(y) \mathcal{K}_1(x, dy) \uparrow h(x).
$$
가측 함수의 점별 극한 — 가측.

*Step 4*: 일반 $g_C$ 는 $g_C = g_C^+ - g_C^-$ 로 분해. 단, $\mathcal{K}_2(y, C) \in [0, 1]$ 이므로 비음만으로 충분.

**(iii) 응용 — Monotone Class**: 위 Step 1-3 을 monotone class theorem (Theorem 1.11) 으로 정리하면, "각 $g \in \mathcal{H}_{\mathrm{kernel}} \Rightarrow x \mapsto \int g \, d\mathcal{K}_1(x, \cdot) \in \mathcal{B}_X$-가측" 인 함수족 $\mathcal{H}_{\mathrm{kernel}}$ 가 모든 indicator 를 포함하므로 모든 $\mathcal{B}_Y$-가측 bounded 함수를 포함. $\square$

**Remark 2.3a (σ-finiteness)**. 위 증명에서 $\mathcal{K}_1(x, \cdot)$ 가 확률측도 (총질량 1) 이므로 σ-finite 자명. Sub-probability kernel (총질량 ≤ 1) 로 일반화해도 본 증명 그대로. *Non-finite* kernel (예: Lévy measure) 로는 일반화 불가 — Tonelli 의 σ-finiteness 가 필요.

**중요**: Markov kernel 의 합성은 결합법칙 성립 ($\mathcal{K}_3 \circ (\mathcal{K}_2 \circ \mathcal{K}_1) = (\mathcal{K}_3 \circ \mathcal{K}_2) \circ \mathcal{K}_1$). 증명은 Fubini 의 직접 적용. 따라서 5단계 pipeline 전체의 합성은 well-defined.

### 2.4 통상 표기법 일치성

함수해석 / 작용소 표기와의 일치:

- $\mathcal{K} f(x) := \int f(y) \mathcal{K}(x, dy)$ — kernel 의 함수 위 우-작용
- $\mathcal{K}^* \mu(A) := \int \mathcal{K}(x, A) \mu(dx)$ — kernel 의 측도 위 좌-작용 (adjoint convention)
- 우리는 통일성을 위해 측도 작용을 $\mathcal{K}\mu$ 로 표기 (위 §2.2 의 셋째 항)

### 2.5 결정론적 case

결정론적 변환 $f : \mathcal{X} \to \mathcal{Y}$ 는 Dirac kernel $\mathcal{K}_f(x, B) = \delta_{f(x)}(B)$ 로 embedding. 따라서 결정론 / 확률론 변환을 같은 framework 에서 다룸.

### 2.6 Markov Category — synthetic 추상화 (Fritz 2020)

Stochastic kernel 들이 형성하는 카테고리의 *synthetic* 정식은 본 framework 에 결정적인 어휘를 제공. Fritz 의 "A synthetic approach to Markov kernels" (Advances in Mathematics 370 (2020) 107239) 의 정의를 명시적으로 도입한다.

**Definition 2.4 (Markov category $\mathbf{BorelStoch}$)**. 
- **Objects**: Polish 측도공간 $(\mathcal{X}, \mathcal{B}_X)$.
- **Morphisms**: $\mathcal{X} \to \mathcal{Y}$ 는 stochastic kernel $\mathcal{K}$ (Def 2.1).
- **Composition**: §2.3 (Def 2.2). Lemma 2.3 이 이를 well-defined morphism 으로 만든다.
- **Identity**: $\mathrm{id}_{\mathcal{X}}(x, B) = \delta_x(B) = \mathbf{1}_B(x)$.

**Monoidal structure**:
- $\otimes$ on objects: product space $\mathcal{X} \otimes \mathcal{Y} = \mathcal{X} \times \mathcal{Y}$ (Borel product σ-algebra).
- $\otimes$ on morphisms: $(\mathcal{K} \otimes \mathcal{L})((x, y), A \times B) = \mathcal{K}(x, A) \cdot \mathcal{L}(y, B)$ + product measure extension.
- Monoidal unit: 한 점 공간 $I = \{*\}$ (자명한 σ-algebra).

**Copy/Discard structure (commutative comonoid)**:
- **Copy**: $\Delta_{\mathcal{X}} : \mathcal{X} \to \mathcal{X} \otimes \mathcal{X}$, $\Delta_{\mathcal{X}}(x, \cdot) = \delta_{(x, x)}$. 결정론적 — diagonal embedding.
- **Discard**: $!_{\mathcal{X}} : \mathcal{X} \to I$, $!_{\mathcal{X}}(x, \{*\}) = 1$. 결정론적 — terminal map.

**Axioms** (Fritz 2020, §2):
- (Cocommutativity) $\tau \circ \Delta = \Delta$ (swap 후 copy = copy).
- (Coassociativity) $(\Delta \otimes \mathrm{id}) \circ \Delta = (\mathrm{id} \otimes \Delta) \circ \Delta$.
- (Counit) $(\mathrm{id} \otimes !) \circ \Delta = \mathrm{id}$.

**Determinism 의 카테고리적 특징화 (Fritz Prop 10.1)**. Kernel $\mathcal{K}$ 가 결정론적 ⟺ $\mathcal{K} \otimes \mathcal{K}) \circ \Delta = \Delta \circ \mathcal{K}$ — 즉 *Copy 와 commute*.

**해석**: Strictly stochastic kernel 은 "복사가 가능하지 않음" — 한 입력의 두 *독립 sample* 은 같은 random state 의 *두 복사본* 과 다름 (no-cloning).

**본 framework 의 SSKP 의 위치**: SSKP 는 $\mathbf{BorelStoch}$ 의 *5-객체 cascade* (length 4 의 순차 morphism 합성):
$$
\mathcal{S}_0 \xrightarrow{\mathcal{K}_1} \mathcal{S}_1 \xrightarrow{\mathcal{K}_2} \mathcal{S}_2 \xrightarrow{\mathcal{K}_3} \mathcal{S}_3 \xrightarrow{\mathcal{K}_4} \mathcal{S}_4
$$
이는 Markov category 의 *linear diagram* — branching, copy, discard 가 없는 가장 단순한 형태. Top-down feedback, attention 같은 nonlinear interaction 을 도입하려면 *acyclic directed graph* 로 일반화해야 하며, 이는 Bayesian network 의 카테고리적 정식과 일치 (Fong 2013).

**Conditional 의 정의 (Cho-Jacobs 2019)**. $\pi : I \to \mathcal{X} \otimes \mathcal{Y}$ 가 결합분포일 때, *conditional* $\mathcal{K} : \mathcal{X} \to \mathcal{Y}$ 는 $\pi = (\mathrm{id} \otimes \mathcal{K}) \circ \Delta_{\mathcal{X}} \circ \pi_{\mathcal{X}}$ ($\pi_{\mathcal{X}}$ 는 marginal). Disintegration theorem (Theorem 1.2) 의 카테고리적 진술.

**Forgetful functor 의 존재**. $\mathbf{Meas} \hookrightarrow \mathbf{BorelStoch}$: 가측사상 $f$ → Dirac kernel $\delta_f$. 이 임베딩이 *카테고리의 부분* 으로서 결정론적 시스템을 stochastic 시스템 안에 자연스럽게 포함시킴.

---

## 3. 마스터 객체 — 5단계 파이프라인

### 3.1 정의

**Definition 3.1 (Stratified Stochastic Kernel Pipeline, SSKP)**. SSKP 는 tuple

$$
\mathbb{P} = \left( \{\mathcal{S}_i\}_{i=0}^4, \; \{\mathcal{K}_i\}_{i=1}^4 \right)
$$

여기서:
- $\mathcal{S}_i$ 는 §1.1 의 가정 (G1, G2) 만족하는 Polish-Borel 공간
- $\mathcal{K}_i : \mathcal{S}_{i-1} \to \mathcal{S}_i$ 는 §2.1 의 stochastic kernel

### 3.2 도식

$$
\mathcal{S}_0 \xrightarrow{\mathcal{K}_1} \mathcal{S}_1 \xrightarrow{\mathcal{K}_2} \mathcal{S}_2 \xrightarrow{\mathcal{K}_3} \mathcal{S}_3 \xrightarrow{\mathcal{K}_4} \mathcal{S}_4
$$

또는 합성 형태:

$$
\Phi_{0 \to 4} := \mathcal{K}_4 \circ \mathcal{K}_3 \circ \mathcal{K}_2 \circ \mathcal{K}_1 : \mathcal{S}_0 \to \mathcal{S}_4
$$

### 3.3 인과성 (causality via filtration)

각 $\mathcal{K}_i$ 는 시간에 대해 **인과적 (causal)**: stage $i$ 의 시각 $t$ 출력은 stage $i-1$ 의 시각 $\leq t$ 입력에만 의존.

**Definition 3.2 (Causal kernel)**. $\mathcal{K} : \mathcal{S}_{i-1} \to \mathcal{S}_i$ 가 인과적이라 함은: 임의의 $T > 0$ 에 대해 stage $i$ 의 $[0, T]$-restriction 의 분포는 stage $i-1$ 의 $[0, T]$-restriction 에 의해 결정됨. 형식적으로, §1.4 의 filtration $\{\mathcal{F}^{\mathcal{S}_{i-1}}_T\}$, $\{\mathcal{F}^{\mathcal{S}_i}_T\}$ 를 사용하면:
$$
\mathcal{K}(x, B) = \mathcal{K}(x', B) \quad \text{whenever } x|_{[0, T]} = x'|_{[0, T]} \text{ and } B \in \mathcal{F}^{\mathcal{S}_i}_T.
$$
즉, *제한 사상* $r_T : \mathcal{S} \to \mathcal{S}|_{[0, T]}$ 에 대해 다음 가환도가 성립:
$$
\begin{array}{ccc}
\mathcal{S}_{i-1} & \xrightarrow{\mathcal{K}_i} & \mathcal{S}_i \\
\downarrow r_T & & \downarrow r_T \\
\mathcal{S}_{i-1}|_{[0, T]} & \xrightarrow{\mathcal{K}_i^{[0, T]}} & \mathcal{S}_i|_{[0, T]}
\end{array}
$$
어떤 *제한 kernel* $\mathcal{K}_i^{[0, T]}$ 가 존재. (이 가환도가 §8.5 의 lemma 의 골격.)

**Definition 3.2a (Predictable kernel; strictly stronger)**. Kernel 이 $\mathcal{F}_{t-} := \bigvee_{s < t} \mathcal{F}_s$ 에만 의존할 때 *predictable*. 본 framework 의 대부분 stage 는 adapted (current time 의 입력 사용); predictable 는 strict subset.

본 디렉토리의 모든 $\mathcal{K}_i$ 는 인과적 (TC-SP-1.3).

### 3.4 동치류

두 SSKP $\mathbb{P}, \mathbb{P}'$ 가 *관측적으로 동치* 라 함은: 임의의 입력 분포 $\mu_0$ 에 대해 $\Phi_{0\to 4} \mu_0 = \Phi'_{0\to 4} \mu_0$. 즉, $\mathcal{S}_4$ 에서 동일한 분포 생성. (Stage 사이의 internal state 가 달라도 output 이 같으면 동치.)

이 동치류는 본 디렉토리에서는 *주제가 아님*. 우리는 각 stage 의 internal mechanism 도 명시한다 (biological reality 와의 정합 위해).

### 3.5 입력 측도 $\mu_0$ 의 위상

본 framework 의 *입력* 은 $\mathcal{S}_0$ 위의 측도 $\mu_0$. 이는 *물리적 장면* (외부 세계의 광원, 반사, 산란 등) 에 의해 결정. 본 디렉토리는 $\mu_0$ 의 *내부 구조* (장면의 의미, 객체 등) 를 다루지 않는다. $\mu_0$ 는 외부에서 주어진 입력.

이 분리는 본질적: "장면 → 광자분포" 는 광학 / 복사 전달 (radiative transfer) 의 문제이며, "광자분포 → 인식 장" 이 본 디렉토리의 문제다.

### 3.6 결합분포 구성 — Ionescu-Tulcea extension

5단계 pipeline 전체의 *결합분포* (joint law on $\mathcal{S}_0 \times \mathcal{S}_1 \times \cdots \times \mathcal{S}_4$) 가 well-defined 임은 자명하지 않다. 무한 product 측도 의 존재는 Kolmogorov extension 으로 처리되나, 본 framework 는 *유한 stage* 이므로 더 명시적인 *Ionescu-Tulcea* 가 적절.

**Theorem 3.3 (Ionescu-Tulcea Extension; Kallenberg Theorem 8.24)**. $\{(\mathcal{X}_n, \mathcal{B}_n)\}_{n=0}^N$ 이 가측공간 열이고 $\mu_0$ 가 $(\mathcal{X}_0, \mathcal{B}_0)$ 위 확률측도, $\{\mathcal{K}_n : \mathcal{X}_0 \times \cdots \times \mathcal{X}_{n-1} \to \mathcal{X}_n\}_{n=1}^N$ 이 kernel 열일 때, product 공간 $\prod_{n=0}^N \mathcal{X}_n$ 위에 *유일한* 결합분포 $\mathbb{P}$ 가 존재하여
$$
\mathbb{P}(A_0 \times A_1 \times \cdots \times A_N) = \int_{A_0} \mu_0(dx_0) \int_{A_1} \mathcal{K}_1(x_0, dx_1) \cdots \int_{A_N} \mathcal{K}_N(x_0, \ldots, x_{N-1}, dx_N).
$$

**Polish 가정 불필요**: 이 정리는 일반 가측공간에서 성립 (Kolmogorov 와 달리). 이것이 *유한 stage 의 강점*.

**본 framework 의 적용**. $N = 4$, $\mathcal{X}_i = \mathcal{S}_i$, kernel $\mathcal{K}_i$ 가 *마지막 stage 만 의존* (Markov 형태):
$$
\mathcal{K}_i(x_0, \ldots, x_{i-1}, dx_i) = \mathcal{K}_i(x_{i-1}, dx_i).
$$
따라서 결합분포
$$
\mathbb{P}_{0:4}(A_0 \times \cdots \times A_4) = \int_{A_0} \mu_0(dx_0) \int_{A_1} \mathcal{K}_1(x_0, dx_1) \int_{A_2} \mathcal{K}_2(x_1, dx_2) \int_{A_3} \mathcal{K}_3(x_2, dx_3) \int_{A_4} \mathcal{K}_4(x_3, dx_4).
$$

이 결합분포 $\mathbb{P}_{0:4}$ 가 본 framework 의 *완전 객체*. Marginal $\mathbb{P}_4 = \Phi_{0 \to 4} \mu_0$ 는 §3.2 의 합성. Conditional 들은 disintegration (Theorem 1.2) 으로 추출.

**의미**. SSKP 는 단순한 kernel cascade 가 아니라 *Polish-Borel 확률공간 위의 유한길이 Markov chain*. 이는 *Bayesian network* (DAG) 의 가장 단순한 형태 (선형 DAG, length 4).

### 3.7 결정론적 pipeline 의 예 — Embedding 의 명시

물리학 / 신호처리 의 *전통적* sensing 모델 (예: pinhole camera, linear filter cascade) 은 *모두 결정론적*. SSKP framework 가 이를 포함함을 명시.

**Example 3.4 (Deterministic SSKP)**. 가측사상 $f_i : \mathcal{S}_{i-1} \to \mathcal{S}_i$ 열이 주어졌을 때, $\mathcal{K}_i(x, B) := \delta_{f_i(x)}(B)$ 가 deterministic kernel (Def 2.1a).

이 경우 $\Phi_{0 \to 4} = \delta_{f_4 \circ f_3 \circ f_2 \circ f_1}$ — Dirac kernel of the composed map.

결합분포 $\mathbb{P}_{0:4}$ 는 $(x_0, f_1(x_0), f_2(f_1(x_0)), \ldots)$ 가 graph 측도 (deterministic graph $\subset \mathcal{S}_0 \times \cdots \times \mathcal{S}_4$ 위에 집중).

**의미**: 결정론적 신호처리 cascade 는 SSKP 의 *부분 카테고리* (정확히 $\mathbf{Meas} \hookrightarrow \mathbf{BorelStoch}$ 의 이미지). 따라서 SSKP 는 *진정한 확장* — 결정론을 잃지 않으면서 stochasticity 를 추가할 수 있는 framework.

망막 sensing 은 *최소한 stage 0 (Poisson)*, *stage 1 (열적 noise)*, *stage 3 (spiking variability)* 에서 strictly stochastic — 따라서 결정론적 framework 로는 표현 불가능. SSKP 가 필요한 *최소* framework.

---

## 4. 수학적 도구 카탈로그 (포괄 survey)

각 도구가 어느 stage 에서 어떤 객체를 정의하는 데 쓰이는지 cross-reference 형태로 정리.

### 4.1 점과정 / 확률과정 (Probability & Point Processes)

**핵심 객체**:
- *Marked point process* (MPP): Janossy density, intensity measure
- *Inhomogeneous Poisson*: $\Pr[N(A) = n] = e^{-\Lambda(A)} \Lambda(A)^n / n!$
- *Cox process* (doubly stochastic Poisson): rate 자체가 random
- *Hawkes process*: self-exciting, $\lambda(t) = \mu + \int_0^t \phi(t-s) dN(s)$
- *Renewal process*: i.i.d. inter-event intervals

**핵심 정리** (formal statements):

**Theorem (Campbell, Daley-Vere-Jones Prop 9.5.II)**. $N$ 이 강도측도 $\Lambda$ 를 가진 simple point process 이고 $f : \mathcal{X} \to \mathbb{R}$ 가 $\Lambda$-적분가능 가측함수라면
$$
\mathbb{E}\left[\sum_{x_i \in N} f(x_i)\right] = \int_{\mathcal{X}} f(x) \, \Lambda(dx),
$$
또한 2차 모멘트 (Campbell-Mecke):
$$
\mathbb{E}\left[\sum_{i \neq j} f(x_i) g(x_j)\right] = \iint f(x) g(y) \, \mathcal{K}^{(2)}(dx, dy),
$$
$\mathcal{K}^{(2)}$ 은 second-order factorial moment measure. **Stage 0 의 §2 (intensity 정의) 가 직접 사용**.

**Theorem (Slivnyak-Mecke; Last-Penrose "Lectures on the Poisson Process" Thm 4.1)**. $N$ 이 Poisson($\Lambda$) 이고 $x \in N$ 의 reduced Palm distribution 은 $N$ 자체의 분포와 일치 (조건 $x$ 의 *나머지 점들* 이 $\Lambda$-Poisson 으로 분포). **Stage 0 의 §5 (correlation 부재) 의 근거**.

**Theorem (Khinchin-Korolyuk)**. $N$ 이 simple stationary point process 이면 1차 강도 = $\lim_{t \to 0} \Pr[N([0, t]) \geq 1] / t$. **Stage 3 의 firing rate 정의의 기반**.

**사용 단계**:
- Stage 0 → Poisson MPP (광자 도래) — 02 §4 의 main 방정식 directly invokes Campbell.
- Stage 3 → Cox / Hawkes (신경절 스파이크) — 05 §3 의 conditional intensity 가 Hawkes 식.

**자연성 근거**: 광자 도래는 무기억(memoryless) 양자 검출 이벤트의 합 — Poisson 의 가장 자연스러운 한계. 스파이크 발화는 graded input 에 의해 변조되는 rate (Cox), 또는 refractory / bursting 자기-여기 (Hawkes).

**도구 표준 reference**: Daley & Vere-Jones, "An Introduction to the Theory of Point Processes" Vol. I §1-3, Vol. II §9-13; Last & Penrose, "Lectures on the Poisson Process" Ch. 1-4.

### 4.2 확률미분방정식 (SDE) / Master Equation

**핵심 객체**:
- *Itô SDE*: $dX_t = b(X_t, t) dt + \sigma(X_t, t) dW_t$
- *Chemical Langevin equation*: $d X_i / dt = \sum_j a_{ij} (X)$ + diffusion (Gillespie 1976)
- *Master equation*: $\partial_t P(n, t) = \sum_{n'} [W(n|n') P(n', t) - W(n'|n) P(n, t)]$
- *Fokker-Planck*: master equation 의 연속 한계 — $\partial_t p = -\partial_x (b p) + \frac{1}{2} \partial_x^2 (\sigma^2 p)$

**핵심 정리** (formal statements):

**Theorem (Itô existence-uniqueness; Øksendal Theorem 5.2.1)**. $b, \sigma$ 가 Lipschitz + linear growth 조건을 만족하면 SDE $dX_t = b(X_t, t) dt + \sigma(X_t, t) dW_t$ 가 *유일한 strong 해* 가짐. **Stage 1 의 §4 (광수용기 SDE well-posedness) 의 근거**.

**Theorem (Fokker-Planck-Kolmogorov forward)**. SDE 의 transition density $p(t, x | s, y)$ 가
$$
\partial_t p = -\partial_x(b \cdot p) + \tfrac{1}{2} \partial_x^2(\sigma^2 \cdot p)
$$
를 만족. **Stage 1, 3 의 분포 진화의 PDE 표현**.

**사용 단계**:
- Stage 1 → SDE (광수용기 막전위 동역학) + master equation (rhodopsin Markov chain) — 03 §3 의 main 방정식.
- Stage 3 → SDE (LIF 모델), Hawkes 의 한계로서 Fokker-Planck — 05 §4.

**자연성 근거**: 광수용기 응답은 광자 도래 (Poisson 입력) 와 열적 확산 (Wiener 항) 의 결합 → SDE 자연. LIF 도 동일 구조.

**도구 표준 reference**: Øksendal, "Stochastic Differential Equations" §5-7; Gardiner, "Stochastic Methods" Ch. 3-5; Pavliotis, "Stochastic Processes and Applications" Ch. 4.

### 4.3 함수해석 (Functional Analysis)

**핵심 객체**:
- *Positive operators on Riesz space*: $T \geq 0 \Leftrightarrow T(\text{cone}) \subset \text{cone}$
- *Half-wave rectification*: $[\cdot]_+ = \max(\cdot, 0)$, $[\cdot]_- = \max(-\cdot, 0)$
- *Volterra series*: 비선형 시스템의 $f(x) = \sum_n \int k_n(t_1, \ldots, t_n) \prod x(t_i) dt_i$
- *Hilbert space* $L^2$ — 필터 뱅크의 자연 서식지

**핵심 정리**:

**Theorem (Riesz decomposition; Schaefer "Banach Lattices" §I.1)**. $L^p(\mathcal{X}, \mu)$ 가 Banach lattice 일 때, 모든 $f \in L^p$ 는 *유일한* 분해 $f = f^+ - f^-$, $f^\pm \geq 0$, $\inf(f^+, f^-) = 0$. **TC-SP-2.1 (ON/OFF 분리의 uniqueness) 의 직접 근거**.

**Theorem (Volterra series convergence; Boyd-Chua 1985)**. 약한 비선형 시스템 ($\| \nabla^n f \|$ 의 적절한 bound 하) 의 응답은 Volterra 급수로 *일양 수렴*. **Stage 1 의 Naka-Rushton 비선형성의 다항식 근사**.

**사용 단계**:
- Stage 2a → ON/OFF 분리의 Riesz 분해 (TC-SP-2.1) — 04 §2 의 main 정리.
- Stage 1 → Volterra 전개 (Naka-Rushton 비선형성) — 03 §6.
- Cross-cutting → $L^2$ 기반 정보론적 분석 — 06 §3.

**자연성 근거**: ON/OFF 분리는 *부호*가 별개 채널이므로 positive cone 분해가 정확. 비선형 응답은 입력의 다항식 functional → Volterra.

**도구 표준 reference**: Schaefer, "Banach Lattices and Positive Operators" §I-II; Aliprantis-Burkinshaw, "Positive Operators" §1-3.

### 4.4 합성곱 대수 (Convolution Algebras)

**핵심 객체**:
- *Convolution*: $(f * g)(x) = \int f(y) g(x - y) dy$
- *DoG (Difference of Gaussians)*: $K_{\text{DoG}} = G_{\sigma_c} - \alpha G_{\sigma_s}$
- *LoG (Laplacian of Gaussian)*: $\Delta G_\sigma$
- *Distribution theory*: tempered distributions, $\delta$, derivatives
- *Translation-invariant operators* = convolution operators (on $L^2(\mathbb{R}^n)$)

**핵심 정리**:

**Theorem (Translation-invariance ⟺ convolution; Rudin "FA" §5.13 / Hörmander "Linear PDE I" §4.2)**. $T : \mathcal{S}'(\mathbb{R}^n) \to \mathcal{S}'(\mathbb{R}^n)$ 가 translation-invariant 연속 선형 operator 이면 *유일한* tempered distribution $K$ 에 대해 $T f = K * f$. **Stage 2b 의 DoG 도출의 기반**: 망막의 국소 translation invariance + linearity ⟹ convolution.

**사용 단계**:
- Stage 2b → DoG (center-surround 수용야) — 04 §3 의 main 방정식.

**자연성 근거**: 망막의 translation invariance (적어도 작은 패치에서) → translation-invariant linear filter → convolution.

**도구 표준 reference**: Schwartz, "Théorie des Distributions" Ch. I-VI; Rudin, "Functional Analysis" Ch. 5-7; Hörmander, "The Analysis of Linear Partial Differential Operators" Vol. I §4.

### 4.5 Scale-space 이론 & PDE

**핵심 객체**:
- *Heat equation*: $\partial_t u = \Delta u$
- *Gaussian scale-space*: $u(x, \sigma) = (G_\sigma * f)(x)$
- *Perona-Malik diffusion*: $\partial_t u = \text{div}(g(|\nabla u|) \nabla u)$
- *Wavelet decomposition*: $f = \sum_{j, k} \langle f, \psi_{j,k} \rangle \psi_{j,k}$

**핵심 정리**:

**Theorem (Scale-space uniqueness; Koenderink 1984; Lindeberg §3.2)**. *Causal, isotropic, linear, shift-invariant* scale-space 의 유일한 generator 는 Gaussian (heat kernel). 즉, 4 공리를 만족하는 유일한 family 는 $\{G_\sigma * \cdot\}_{\sigma > 0}$. **Stage 2b 의 DoG = scale-derivative 의 정당화**.

**사용 단계**:
- Stage 2b → DoG 가 scale-normalized Laplacian 의 근사 ($\partial_\sigma G * f \approx \sigma \Delta G * f$) — 04 §3.

**자연성 근거**: 망막의 다중-cell-size (foveal 작은 cell, peripheral 큰 cell) → 자연스러운 scale 계층.

**도구 표준 reference**: Koenderink (Biological Cybernetics 1984); Lindeberg, "Scale-Space Theory in Computer Vision" §3-4; Sapiro, "Geometric PDEs and Image Analysis" Ch. 1-3.

### 4.6 미분기하 (Differential Geometry)

**핵심 객체**:
- *Riemann manifold* $(M, g)$
- *Laplace-Beltrami operator* $\Delta_M$
- *Fiber bundle* $E \to B$ with fiber $F$
- *Vector field / Tangent bundle* $TM$

**핵심 정리**:

**Theorem (Hodge decomposition on compact Riemann manifolds; Warner "Foundations of Differentiable Manifolds and Lie Groups" §6.8)**. Compact orientable $(M, g)$ 위의 $k$-form 공간은 $\Omega^k = d\Omega^{k-1} \oplus d^* \Omega^{k+1} \oplus \mathcal{H}^k$, $\mathcal{H}^k = \ker \Delta$. **Stage 2c 의 motion field 의 곡률 분해의 잠재 도구** (OP).

**사용 단계**:
- Stage 2b → 망막을 2-manifold 로 다룰 때 $\Delta_M$ (foveal eccentricity 처리) — 04 §3.4.
- Stage 2c → motion 을 $TM$ 위 vector field 로 표현 — 04 §4.
- Stage 4 → 채널 다발을 fiber bundle 로 (각 픽셀 위에 채널 fiber) — 05 §6.

**자연성 근거**: 망막은 평평하지 않음 (안구 곡률); foveal eccentricity 가 metric 을 흔든다. 평행 채널은 fiber bundle 의 typical example.

**도구 표준 reference**: do Carmo, "Riemannian Geometry"; Warner, "Foundations of Differentiable Manifolds and Lie Groups" §1-6; Kobayashi-Nomizu, "Foundations of Differential Geometry" Vol. I (bundles).

### 4.7 시공간 분석 (Spatiotemporal Analysis)

**핵심 객체**:
- *Spatiotemporal Fourier*: $\hat{f}(\xi, \omega) = \iint f(x, t) e^{-i(\xi \cdot x + \omega t)} dx \, dt$
- *Velocity-tuned filter*: $\hat{f}$ 의 $\omega = -\xi \cdot v$ slab 에 energy
- *Adelson-Bergen motion energy*: quadrature pair $(G^{\sin}, G^{\cos})$ → $E = (G^{\sin} * f)^2 + (G^{\cos} * f)^2$
- *Reichardt detector*: $R = f(x, t) f(x + \delta, t + \tau) - f(x, t) f(x - \delta, t + \tau)$
- *Optical flow PDE*: $\nabla I \cdot v + I_t = 0$

**핵심 정리**:

**Theorem (Adelson-Bergen equivalence; JOSA-A 1985)**. Quadrature pair motion energy = $|\hat{f}(\xi, -\xi v)|^2$ — Fourier slab energy. **TC-SP-2.4 의 정확한 진술**.

**Theorem (Reichardt ↔ motion energy equivalence under normalization; Adelson-Bergen 1985 §4)**. 적절한 normalization 하에서 Reichardt detector $R$ 와 motion energy $E$ 가 동등 — 둘 다 Fourier slab 의 에너지를 다른 방식으로 측정. **TC-SP-2.5 의 직접 근거**.

**사용 단계**:
- Stage 2c → DSGC 방향 선택성, amacrine 시간 미분 — 04 §4 의 main 방정식.

**자연성 근거**: 움직임은 spacetime 의 "기울어진 줄무늬" — Fourier domain 의 slab. Reichardt 와 motion energy 는 이 slab 의 energy 를 두 다른 방식으로 추출.

**도구 표준 reference**: Adelson-Bergen (JOSA-A 1985); Watson-Ahumada (JOSA-A 1985); Simoncelli-Heeger (Vision Research 1998).

### 4.8 정보이론 (Information Theory)

**핵심 객체**:
- *Mutual information*: $I(X; Y) = H(X) - H(X|Y)$
- *Channel capacity*: $C = \sup_{P_X} I(X; Y)$
- *Rate-distortion*: $R(D) = \inf_{P_{Y|X} : \mathbb{E} d(X,Y) \leq D} I(X; Y)$
- *Fisher information*: $\mathcal{I}(\theta) = \mathbb{E}\left[(\partial_\theta \log p(X|\theta))^2\right]$
- *Data processing inequality*: Markov chain $X \to Y \to Z \Rightarrow I(X; Z) \leq I(X; Y)$

**핵심 정리**:

**Theorem (Data Processing Inequality; Cover-Thomas Thm 2.8.1, 2nd ed.)**. $X \to Y \to Z$ 가 Markov chain (즉 $p(z | x, y) = p(z | y)$) 이면 $I(X; Z) \leq I(X; Y)$, 또한 $I(X; Z) \leq I(Y; Z)$. 등호 조건: $X \to Z \to Y$ 도 Markov.

**Theorem (Chain rule; Cover-Thomas Thm 2.5.2)**. $I(X; Y, Z) = I(X; Y) + I(X; Z | Y)$.

**Theorem (Channel coding; Shannon 1948)**. Memoryless channel $\mathcal{K}$ 의 capacity $C = \sup_{P_X} I(X; Y)$ 가 reliable transmission 의 sharp threshold. **06 의 end-to-end bound 의 기반**.

**사용 단계**:
- Cross-cutting (06) → end-to-end bound, 각 stage 의 channel capacity — 06 §2-4 의 main 방정식.
- TC-SP-1.2, TC-SP-4.1-4.3 의 기반.

**자연성 근거**: pipeline 은 본질적으로 noisy channel cascade; data processing inequality 가 직접 적용.

**도구 표준 reference**: Cover & Thomas, "Elements of Information Theory" Ch. 2, 7, 10; MacKay, "Information Theory, Inference, and Learning Algorithms" Ch. 2, 8.

### 4.9 대수위상 / 지속 호몰로지 (Algebraic Topology)

**핵심 객체**:
- *Simplicial / cubical complex*
- *Homology* $H_k(X)$
- *Persistent homology*: filtration $X_0 \subset X_1 \subset \ldots$ 의 $H_k(X_t)$ 추적; bar code
- *Sheaf* $\mathcal{F}$ on topological space — local-to-global structure

**핵심 정리**:

**Theorem (Stability of persistence diagrams; Cohen-Steiner-Edelsbrunner-Harer 2007)**. 두 filtration 의 persistence diagram 사이의 bottleneck distance ≤ $\| f - g \|_\infty$. **Stage 3 의 spike pattern 분석의 robustness 근거**.

**사용 단계**:
- Stage 3 출력 분석 → 스파이크 패턴의 위상학적 motif — 05 §7.
- (Ω, σ) lift (07) → sheaf 가 patch-wise σ 의 자연스러운 ambient — 07 §6.

**자연성 근거**: Receptive field 들이 overlap 하며 patch 를 형성 → local-to-global 의 전형. SCC 의 `k_soft.py` 가 persistent homology 인프라 제공.

**도구 표준 reference**: Edelsbrunner & Harer, "Computational Topology" Ch. VII; Hatcher, "Algebraic Topology" Ch. 2; Carlsson, "Topology and Data" (BAMS 2009).

### 4.10 범주론 (Category Theory)

**핵심 객체**:
- *Category* $\mathbf{C}$ — objects + morphisms with composition
- *Functor* $F : \mathbf{C} \to \mathbf{D}$ — composition / identity 보존
- *Natural transformation* $\eta : F \Rightarrow G$
- *Markov category* — stochastic kernel 들의 monoidal category (Fritz 2020); 본 문서 §2.6 에서 명시적 정의

**핵심 정리**:

**Theorem (Coherence; Mac Lane Ch. XI)**. Monoidal category 의 모든 associator/unitor 다이어그램이 commute — 따라서 우리는 괄호를 신경쓰지 않고 합성 가능. **§3.2 의 $\Phi_{0 \to 4}$ 의 well-definedness 의 카테고리 측 근거**.

**사용 단계**:
- Master level → SSKP 자체가 Markov category 의 화살표 cascade — §2.6 + §3.
- (Ω, σ) lift → σ 의 propagation 이 functor 인지 (TC-SP-5.1) — 07 §3, 6.

**자연성 근거**: Stochastic kernel cascade 는 monoidal category 의 자연 example. Markov category framework (Cho-Jacobs, Fritz) 가 disintegration / conditioning 의 깔끔한 추상화 제공.

**도구 표준 reference**: Mac Lane, "Categories for the Working Mathematician" §VII, XI; Fritz, "A synthetic approach to Markov kernels" (Adv. Math. 370, 2020) §2-4; Cho-Jacobs, "Disintegration and Bayesian inversion via string diagrams" (Math. Struct. Comp. Sci. 2019).

### 4.11 최적수송 (Optimal Transport)

**핵심 객체**:
- *Wasserstein distance* $W_p(\mu, \nu)$
- *Kantorovich duality*: $W_1(\mu, \nu) = \sup_{f \in 1\text{-Lip}} \int f \, d(\mu - \nu)$
- *Sinkhorn algorithm* (entropic regularization)
- *Monge-Kantorovich problem*: $\inf_\pi \int c(x, y) d\pi(x, y)$

**핵심 정리**:

**Theorem (Kantorovich duality; Villani Thm 5.10)**. $W_p^p(\mu, \nu) = \sup_{\phi, \psi : \phi(x) + \psi(y) \leq c(x, y)} \int \phi \, d\mu + \int \psi \, d\nu$. **06 의 OT-based stage distance 의 dual 형식**.

**사용 단계**:
- Cross-cutting → stage 간 분포 거리 비교; spike train 의 OT 매칭 — 06 §5.
- SCC 의 `transport.py` Sinkhorn 인프라 재사용 가능.

**자연성 근거**: 두 distinct spike train 또는 두 다른 retinal 출력을 비교할 때 OT 가 자연 — pointwise difference 가 무의미한 random process 의 경우.

**도구 표준 reference**: Villani, "Optimal Transport: Old and New" §5-6; Peyré & Cuturi, "Computational Optimal Transport" §2-4; Santambrogio, "Optimal Transport for Applied Mathematicians" Ch. 1-3.

### 4.12 군이론 / 표현론 (Group Theory)

**핵심 객체**:
- *Translation group* $\mathbb{R}^2$ — 망막 위 평면 평행이동
- *Rotation group* $SO(2)$ — 잘 정의되지 않음 (fovea 가 깸)
- *Scale group* $\mathbb{R}^+$ — 적응
- *Equivariance*: $f(g \cdot x) = g \cdot f(x)$ for $g \in G$

**핵심 정리**:

**Theorem (Equivariance theorem for convolutional layers; Cohen-Welling 2016, ICML)**. $G$-equivariant linear layer 는 *generalized convolution* with $G$-invariant kernel. **Stage 2 의 모든 *translation-equivariant* 처리의 일반화**.

**사용 단계**:
- Cross-cutting → DoG 가 translation-equivariant; orientation column 이 $SO(2)$ 의 부분군 — 04 §3, 06 §6.
- OP-SP-004 → 색 대립의 군론적 해석 가능성 — 04 §5.

**자연성 근거**: 망막의 *국소* translation invariance 가 모든 convolutional 처리의 정당화. Rotation invariance 는 *전역적으로는* 깨짐 — fovea 가 origin 을 fix.

**도구 표준 reference**: Fulton-Harris, "Representation Theory" §1-3; Cohen-Welling (ICML 2016); Folland, "A Course in Abstract Harmonic Analysis" Ch. 2-3.

### 4.13 변분법 / 자유에너지 (Variational Calculus)

**핵심 객체**:
- *Energy functional* $E[u] = \int L(u, \nabla u) dx$
- *Euler-Lagrange*: $\delta E / \delta u = 0$
- *Free energy*: $F = E - T S$
- *Variational Bayesian inference*: $\log P(y) \geq \mathbb{E}_q[\log P(y, x) - \log q(x)]$
- *Friston free-energy principle* (cite, not adopt)

**핵심 정리**:

**Theorem (Euler-Lagrange; Evans "Partial Differential Equations" §8.1)**. Functional $E[u] = \int L(u, \nabla u) dx$ 의 critical point 는 $\partial_u L - \nabla \cdot \partial_{\nabla u} L = 0$. **06 의 각 stage 의 functional 해석의 가능성**.

**사용 단계**:
- Cross-cutting (06) → 각 stage 를 어떤 functional 의 critical point 로 해석 가능? — 06 §7.
- 본 디렉토리는 free-energy principle 을 *채택하지 않음* (단지 reference).

**자연성 근거**: SCC 자체가 energy minimization framework — `scc/energy.py` 와 직접 호환.

**도구 표준 reference**: Evans, "Partial Differential Equations" §8; Giaquinta-Hildebrandt, "Calculus of Variations" Vol. I.

### 4.14 확률기하 (Stochastic Geometry)

**핵심 객체**:
- *Random closed set* (RACS): $\mathcal{X}$ 의 닫힌 부분집합 위의 random element (Matheron 1975)
- *Choquet capacity functional*: $T_\Xi(K) := \Pr[\Xi \cap K \neq \emptyset]$ for compact $K$ — random set 의 분포를 *유일하게* 결정 (Choquet's theorem)
- *Boolean model*: $\Xi = \bigcup_i (X_i + Z_i)$ where $\{X_i\}$ Poisson, $\{Z_i\}$ i.i.d. random shapes
- *Germ-grain model*: 일반화된 Boolean
- *Coverage probability*: $\Pr[x \in \Xi]$
- *Contact distribution*: 한 점에서 random set 까지의 distance distribution

**핵심 정리**:

**Theorem (Choquet; Matheron 1975 Thm 2-2-1)**. RACS $\Xi$ 의 분포는 $T_\Xi(K) = \Pr[\Xi \cap K \neq \emptyset]$ 에 의해 *유일하게* 결정. (단, $T_\Xi$ 는 upper semi-continuous + alternating of infinite order.) **Receptive field overlap 의 확률 구조의 base**.

**Theorem (Boolean model coverage; Stoyan-Kendall-Mecke §3.1)**. $\Xi$ 가 강도 $\lambda$ Poisson germ + 평균 부피 $\bar{v}$ random grain 의 Boolean 이면
$$
\Pr[x \in \Xi] = 1 - \exp(-\lambda \bar{v}).
$$
**Stage 2-3 의 RF overlap 의 ganglion coverage 분석의 정량적 도구**.

**사용 단계**:
- Stage 3 → 신경절세포 receptive field 들이 retinal surface 를 *부분적으로 cover* 하는 구조 — 05 §5.
- Stage 2 → DoG center/surround 의 disk 들이 random Boolean 모형으로 해석 가능 — 04 §3.5.
- (Ω, σ) lift → §2.3 의 *cross-channel σ* 가 RF overlap 그래프의 통계적 구조와 연결 — 07 §2.3.

**자연성 근거**: Receptive field 들은 *지점이 아닌 확장된 영역* — 점이 아닌 *closed set*. 그들의 공간 분포가 (대략) Poisson 이고 모양이 random (cell type, eccentricity 의존) — 정확히 Boolean / germ-grain 모형. Receptive field overlap 의 σ 그래프가 Choquet capacity 의 *graph realization*.

**도구 표준 reference**: Matheron, "Random Sets and Integral Geometry" (1975) Ch. 2; Stoyan-Kendall-Mecke, "Stochastic Geometry and Its Applications" (2nd ed.) Ch. 3-4; Chiu-Stoyan-Kendall-Mecke (3rd ed.) Ch. 6-9; Schneider-Weil, "Stochastic and Integral Geometry" Ch. 9-12.

---

## 5. 추상 Theorem-Candidates

세 명제 모두 *DEFINITION-DRAFT register*. 본 §5 의 proof sketch 는 *full canonical proof 가 아님* — 단지 proof strategy 의 명료성을 보장하기 위함. Full proof 는 후속 plan 의 PROVED register 에서.

### TC-SP-1.1 — [DELETED 2026-05-25 Pass 4]

**Status**: **DELETED via Pass 4** (cumulative 2 HOLE: Pass 3 #5 + Pass 4 #51). Composition lemma 자체 (Lemma 2.3) 는 mathematically sound 이나, *retinal pipeline 에의 적용* 이 Markov property 가정에 의존; 실제 망막은 adaptation (sliding $I_{50}$, calcium dynamics, slow conductances) 으로 *non-Markov*. State augmentation 없이는 TC-SP-1.1 의 *applicability* 가 깨짐.

**Original statement (preserved for audit trail)**:

> 가정 (G1, G2) 하에서, $\Phi_{0 \to 4} = \mathcal{K}_4 \circ \mathcal{K}_3 \circ \mathcal{K}_2 \circ \mathcal{K}_1$ 은 $\mathcal{S}_0 \to \mathcal{S}_4$ 의 stochastic kernel.

**Why DELETED**: 
- *Composition lemma* 자체 (Lemma 2.3, §2.3) 는 *진짜 mathematical content* — Polish-Borel 가정 하 well-defined. 본 lemma 는 §2 본문 유지.
- 그러나 *TC-SP-1.1 의 form* 은 "5-stage retinal pipeline 에 적용" 을 claim — Markov 가정이 *암묵적*이며, adaptation 으로 *위반*.
- Verifier #51 (Pass 4): "TC-SP-1.1's statement does not articulate this requirement [hidden-state augmentation for adaptation]."
- "If pipeline is not Markov, the entire DPI chain needs hidden-state augmentation to recover" — TC-SP-1.1 의 strong form 정리 자격 박탈.

**Replacement**: Lemma 2.3 본문 (composition of Markov kernels is again Markov) 은 *유지* — *generic* mathematical lemma. 본 lemma 의 *retinal pipeline applicability* 는 *augmented state* (hidden adaptation variables 포함) 가정 하 *empirical observation* — 정리 자격 없음.

### TC-SP-1.2 — [DELETED 2026-05-25 Pass 5 #11 model misspecification]

**Status**: **DELETED via Pass 5 #11**. Abstract Markov DPI (Cover-Thomas Thm 2.8.1) is sound, but the *retinal pipeline application* requires retina to *be Markov* — empirically false (centrifugal feedback, gap-junction lateral coupling, dopaminergic neuromodulation, adaptation hidden states). 06 §2.2 본문이 이미 "forward-only 채택" 명시 (가정이지 사실 아님). 본 TC-SP-1.2 의 *generic Markov DPI* 정리 자격이 *retinal context 에서* 다른 객체.

**Original statement (preserved for audit trail)**:

> $I(\mathcal{S}_0; \mathcal{S}_0) \geq I(\mathcal{S}_0; \mathcal{S}_1) \geq \cdots \geq I(\mathcal{S}_0; \mathcal{S}_4)$.

**Why DELETED**: Cover-Thomas Thm 2.8.1 *그대로* 는 generic Markov 체인 정리 — *retinal-specific 내용* 없음. Retinal applicability 의 Markov 가정이 *empirically false* (TC-SP-1.1 과 동일 fundamental issue). 정리는 일반 정리집에 속하지 본 sensing pipeline 의 *originally-stated TC-candidate* 자격 아님.

**Replacement**: §5 본문의 Cover-Thomas DPI 인용은 *generic information-theoretic fact* 로 유지 (도구로). *Retinal pipeline 적용* 은 augmented-state assumption 하 *conjecture* 로 격하. TC 자격 박탈.

**Proof sketch (DEFINITION-DRAFT register)**.

*핵심 도구*:
- Cover-Thomas Theorem 2.8.1 (Data Processing Inequality): Markov chain $X \to Y \to Z$ 에서 $I(X; Z) \leq I(X; Y)$.
- Cover-Thomas Theorem 2.5.2 (Chain rule of mutual information): $I(X; Y, Z) = I(X; Y) + I(X; Z | Y)$.

*Step 1: Markov property 확인*. 각 stage $i \geq 1$ 에 대해 다음의 Markov chain 이 성립함을 보인다:
$$
\mathcal{S}_0 \to \mathcal{S}_{i-1} \to \mathcal{S}_i.
$$
즉, $\mathcal{S}_i$ 의 조건부분포가 $\mathcal{S}_{i-1}$ 만에 의존 ($\mathcal{S}_0$ 의 정보가 $\mathcal{S}_{i-1}$ 를 거치지 않고 $\mathcal{S}_i$ 로 흐르지 않음).

이는 §3.6 의 Ionescu-Tulcea construction 의 직접 결과: 결합분포 $\mathbb{P}_{0:i}$ 의 disintegration 에서 $\mathbb{P}(\mathcal{S}_i \in B | \mathcal{S}_0, \mathcal{S}_1, \ldots, \mathcal{S}_{i-1}) = \mathcal{K}_i(\mathcal{S}_{i-1}, B)$ — $\mathcal{S}_{i-1}$ 외 변수에 *의존하지 않음*. 정확히 Markov property.

*Step 2: DPI 의 stage-wise 적용*. 각 인접 쌍 $(i-1, i)$ 에 대해 Cover-Thomas Thm 2.8.1 의 적용:
$$
\text{Markov chain } \mathcal{S}_0 \to \mathcal{S}_{i-1} \to \mathcal{S}_i \quad \Rightarrow \quad I(\mathcal{S}_0; \mathcal{S}_i) \leq I(\mathcal{S}_0; \mathcal{S}_{i-1}).
$$

*Step 3: 사슬화*. $i = 1, 2, 3, 4$ 의 부등식을 연결:
$$
I(\mathcal{S}_0; \mathcal{S}_4) \leq I(\mathcal{S}_0; \mathcal{S}_3) \leq I(\mathcal{S}_0; \mathcal{S}_2) \leq I(\mathcal{S}_0; \mathcal{S}_1) \leq I(\mathcal{S}_0; \mathcal{S}_0) = H(\mathcal{S}_0).
$$

마지막 등호: $I(X; X) = H(X)$ (자신과의 mutual information = entropy). 단, $\mathcal{S}_0$ 가 continuous-valued point process 이면 $H$ 가 *differential entropy* 로 발산할 수 있음 — 그러나 *부등식 chain* 은 여전히 유효 (relative entropy 의 좋은 정의 하).

*Step 4: 일반 $i < j$*. 위 사슬을 잘라 사용: $I(\mathcal{S}_0; \mathcal{S}_j) \leq I(\mathcal{S}_0; \mathcal{S}_{j-1}) \leq \cdots \leq I(\mathcal{S}_0; \mathcal{S}_i)$. $\square$

*기술적 verification 필요사항*:
- Mutual information 의 *측도론적 정의* (Csiszár-Körner §2.3, Cover-Thomas §8) 가 Polish-Borel 환경에서 well-defined — 본 framework 의 G1 으로 자동 충족.
- DPI 의 등호 조건: $I(\mathcal{S}_0; \mathcal{S}_i) = I(\mathcal{S}_0; \mathcal{S}_{i-1})$ ⟺ $\mathcal{S}_0$ 와 $\mathcal{S}_i$ 의 모든 정보가 $\mathcal{S}_{i-1}$ 을 통해 흐름 ⟺ $\mathcal{K}_i$ 가 $\mathcal{S}_0$-관점에서 *sufficient*. 본 framework 의 어느 stage 도 이를 만족하지 않음 (각 stage 가 information loss).
- 광자 vs 스파이크 entropy 의 *finite 정의역* 분석 — Stage 0 의 finite local mean intensity 가정 하에 모두 finite mutual info.

**의미**: 정보가 단조 감소함. 어떤 stage 도 정보를 *증가*시킬 수 없음. 모든 후속 정보론적 bound 의 뿌리.

**주의**: 이는 *Shannon mutual information* 의 단조성. *유용한 정보* 의 단조성이 아님. Stage 가 진행될수록 정보는 줄지만 *접근 가능성* 은 증가할 수 있음 (압축 + 구조화). 이 구별이 TC-SP-4.3 (Naka-Rushton 의 mutual information 최대화) 의 미묘함.

### TC-SP-1.3 — [DELETED 2026-05-25 Pass 4 (escalated from Pass 3 WEAKENED)]

**Status**: **DELETED via Pass 4 — weakening insufficient**. Pass 3 weakening 후에도 Pass 4 의 #46 (boundary: T=0/T→∞ 미처리) + #51 (channel-independence in causal kernel 위반: lateral inhibition) 가 추가 HOLE 발견 → cumulative 4 patterns HOLE → 박탈.

**Original statement (preserved for audit trail)**: $\mathcal{K}_i$ 의 $[0, T]$-restriction 의 분포는 $\mathcal{S}_{i-1}$ 의 $[0, T]$-restriction 에 의해서만 결정.

**Weakening attempt (Pass 3, also DELETED)**: Q1 (no-feedback) + Q2 (causal Gabor) qualifier 추가했으나, Pass 4 가 새 hole 발견.

**Why DELETED**: 인과성은 *각 $K_i$ 의 by-construction property* (정의적 사실) + qualifier (Q1, Q2) 가 *trivial restriction* 으로 reduced; (Q3) T=0/∞ boundary 미처리; (Q4) channel-causal-independence 가 horizontal cell lateral 결합 위반. 정리 자격 박탈.

**Replacement**: 인과성은 본 디렉토리의 *axiomatic assumption* — "본 디렉토리는 인과적 파이프라인을 가정한다 (top-down feedback 무시)" — 정리 아님. §3.3 본문의 case analysis 는 *descriptive observation* 으로 유지.

**Filtration 언어로의 정밀 진술**. §1.4 의 natural filtration $\{\mathcal{F}^{\mathcal{S}_i}_T\}_{T \geq 0}$ 를 사용하면, kernel $\mathcal{K}_i : \mathcal{S}_{i-1} \to \mathcal{S}_i$ 가 *인과적* 이라 함은:

(C1) 모든 $T > 0$ 와 $B \in \mathcal{F}^{\mathcal{S}_i}_T$ 에 대해,
$$
\mathcal{K}_i(\cdot, B) : \mathcal{S}_{i-1} \to [0, 1] \text{ is } \mathcal{F}^{\mathcal{S}_{i-1}}_T\text{-measurable}.
$$

(C2) 동치로, 모든 $T > 0$ 와 $x, x' \in \mathcal{S}_{i-1}$ 가 $x|_{[0, T]} = x'|_{[0, T]}$ 를 만족하면 (즉, $\mathcal{F}^{\mathcal{S}_{i-1}}_T$ 동등),
$$
\mathcal{K}_i(x, B) = \mathcal{K}_i(x', B) \quad \text{for all } B \in \mathcal{F}^{\mathcal{S}_i}_T.
$$

(C3) Kernel 의 measurable restriction 관점: 어떤 *restriction kernel*
$$
\mathcal{K}_i^{[0, T]} : \mathcal{S}_{i-1}^{[0, T]} \to \mathcal{S}_i^{[0, T]}
$$
가 존재하여 §3.3 의 가환도가 성립.

위 세 진술 (C1), (C2), (C3) 의 동치는 §1.4 의 natural filtration 의 정의 (cylinder σ-algebra 형성) 에서 직접 follows.

**증명 가능성**: 각 $\mathcal{K}_i$ 의 구체적 형태에 의존. Stage 0 (Poisson), Stage 1 (인과 SDE), Stage 2 (인과 합성곱), Stage 3 (인과 LIF/Cox/Hawkes), Stage 4 (지연만) — 모두 인과적. 따라서 합성도 인과적 (§8.5 의 lemma).

**Proof sketch (DEFINITION-DRAFT register)**.

각 stage 의 인과성을 separately 확인:

*Stage 0 $\to$ 1*: 광수용기 SDE $dV_t = b(V_t, N_t([0, t])) dt + \sigma dW_t$. Drift $b$ 가 시각 $t$ 의 입력 (현재까지의 광자 count) 에만 의존; Wiener 항도 forward-적분. (C1) 자명히 성립 — SDE 해의 표준 인과성.

*Stage 1 $\to$ 2*: ON/OFF 분리는 *pointwise in (x, t)*; DoG 와 motion energy 는 *과거에 대한 합성곱* (causal kernel 형태로 표현 가능). 즉, $f * K$ 에서 $K(\tau) = 0$ for $\tau < 0$ — temporal kernel 이 nonnegative-time 에서만 nonzero. (C1) 성립.

*Stage 2 $\to$ 3*: LIF 모델은 ODE/SDE 형태로 입력 (graded current) 의 시간 적분 — 인과적 SDE. Cox process 의 conditional intensity $\lambda(t | \mathcal{F}_{t-})$ 가 *과거에만 의존* (predictable). Hawkes 의 자기-여기도 과거 stamp 에만 의존. (C1) 성립.

*Stage 3 $\to$ 4*: 단순한 latency shift $t \mapsto t + \tau$ ($\tau > 0$). 시각 $T$ 의 출력 = 시각 $T - \tau$ 의 입력 — *과거에만 의존*. (C1) 자명.

각 stage 의 (C1) 성립. §8.5 의 Lemma (causal kernel 의 합성도 causal) 에 의해 전체 $\Phi_{0 \to 4}$ 도 causal. $\square$

**의미**: Pipeline 은 시간 비역행. *현재의 출력이 미래의 입력에 의존하지 않음.* 이는 *진실로 자명한* 가정이 아님 — 망막에는 top-down feedback 이 존재 (OP-SP-010); 본 디렉토리는 이를 *무시* 함으로써 인과성을 보장.

---

## 6. 후속 문서 (02~07) 의 inheritance

본 문서가 정의한 다음 객체들이 02~07 에서 *그대로* 사용됨:

| 객체 | 정의 위치 | 사용처 |
|------|----------|-------|
| $\mathcal{S}_i$, $\mathcal{K}_i$ | §1, §2 | 02–05 의 stage 동역학 |
| $\Sigma_{\text{ret}}$, $\Lambda$, $\mathcal{C}$, $\mathcal{C}_g$ | §1.2 | 02–05 의 공간 정의 |
| Causal kernel | §3.3 + §1.4 | 모든 stage |
| Composition $\Phi_{0 \to i}$ | §3.2 | 06 의 end-to-end bound |
| Ionescu-Tulcea joint $\mathbb{P}_{0:4}$ | §3.6 | 06 의 mutual info chain |
| 4.1–4.14 의 도구들 | §4 | 각 stage 의 deep dive |
| TC-SP-1.1–1.3 | §5 | 06 의 추상 backbone, 07 의 lift |

각 후속 문서가 본 문서의 어느 부분을 어떻게 활용하는지 명시:

### 6.1 02 (Stage 0 — Photon point process) 의 inheritance

- $\mathcal{S}_0 = \mathcal{N}(\Sigma_{\text{ret}} \times \mathbb{R}^+ \times \Lambda)$ (§1.2) 의 *구체적 강도측도* $\Lambda$ 정의.
- §1.1.3 의 $\mathcal{N}(\mathcal{X})$ σ-algebra 의 명시적 사용 — Stage 0 의 sample space 의 well-defined-ness.
- §4.1 의 Campbell theorem 의 *직접 적용* — Stage 0 §4 의 평균 광자수 계산.
- §4.14 의 stochastic geometry 의 *future use* — Stage 0 의 spatial coverage 통계.
- $\mu_0$ 의 위상 (§3.5) — Stage 0 가 *radiative transfer 의 출력* 을 입력으로 받음.

### 6.2 03 (Stage 1 — Photoreceptor SDE) 의 inheritance

- $\mathcal{S}_1 = C(\Sigma_{\text{ret}} \times \mathbb{R}^+, \mathbb{R})$ (§1.2) 의 함수공간 구조.
- §4.2 의 Itô SDE existence-uniqueness — Stage 1 §4 의 광수용기 model 의 well-posedness.
- §4.3 의 Volterra series — Naka-Rushton 비선형성의 다항식 근사 (Stage 1 §6).
- §3.3 의 causal kernel 정의 — Stage 1 의 인과성 (TC-SP-1.3 의 instance).

### 6.3 04 (Stage 2 — Inner retinal algebra) 의 inheritance

- $\mathcal{S}_2 = \bigoplus_c C(\Sigma_{\text{ret}} \times \mathbb{R}^+, \mathbb{R}^+)$ (§1.2) 의 *direct sum* 다채널 구조.
- §4.3 의 Riesz decomposition theorem — TC-SP-2.1 (ON/OFF uniqueness) 의 직접 결과.
- §4.4 의 translation-invariance $\Rightarrow$ convolution theorem — DoG 의 도출 (Stage 2 §3).
- §4.5 의 scale-space uniqueness — DoG ≈ scale-normalized Laplacian (Stage 2 §3.3).
- §4.7 의 Adelson-Bergen + Reichardt 정리 — TC-SP-2.4, 2.5 (Stage 2 §4).
- §4.6 의 fiber bundle — 다채널이 *각 retinal 위치 위의 fiber* 로 (Stage 2 §6).

### 6.4 05 (Stage 3 — Ganglion spike encoding) 의 inheritance

- $\mathcal{S}_3 = \prod_c \mathcal{N}(\mathbb{R}^+)$ (§1.2) 의 평행 점과정 구조.
- §4.1 의 Cox / Hawkes process 정의 — Stage 3 §3 의 conditional intensity.
- §4.2 의 LIF SDE — Stage 3 §4 의 membrane dynamics.
- §4.14 의 Boolean model — Stage 3 §5 의 RF coverage.
- §4.9 의 persistent homology — Stage 3 §7 의 spike pattern motif.

### 6.5 06 (End-to-end information bound) 의 inheritance

- $\Phi_{0 \to 4}$ (§3.2) 의 합성 — *end-to-end* channel.
- TC-SP-1.1, 1.2 의 직접 인용 — 06 §2-3 의 main 부등식.
- §4.8 의 capacity, rate-distortion — 06 §4 의 channel capacity 계산.
- §4.11 의 OT — 06 §5 의 stage 간 분포 거리.
- §4.13 의 variational — 06 §7 의 functional 해석.
- §3.6 의 Ionescu-Tulcea $\mathbb{P}_{0:4}$ — 06 의 mutual info chain 의 measure-theoretic base.

### 6.6 07 ((Ω, σ) Tier 2 lift) 의 inheritance

- 모든 $\mathcal{S}_i$ (§1.2) 의 (Ω_i, σ_i) 추출 (07 §2).
- 각 $\mathcal{K}_i$ (§2.1) 의 σ-pushforward 정의 (07 §3).
- §4.9 의 sheaf — patch-wise σ 의 자연스러운 환경 (07 §6).
- §4.10 의 Markov category — Tier 2 카테고리와의 forgetful functor (07 §6.4).
- TC-SP-1.1 (composition) — Tier 2 functoriality (TC-SP-5.1) 의 prerequisite.

### 6.7 08 (Open problems) 의 inheritance

- §7 의 메타 문제들 — OP-SP 등록부에 추가 후보.
- §4 의 각 도구의 *open extension* — Markov category 의 forgetful 의 정확한 형식 등.

---

## 7. Open Meta-Questions

본 문서 수준에서 등록되는 메타 문제 (구체 OP-SP-N 은 stage 문서에서):

- **(Meta-1)** 입력 측도 $\mu_0$ 의 *클래스* 는 어떻게 제한되어야 하는가? 임의의 Polish 측도? 또는 finite total mass 조건? 또는 ergodicity 가정?
- **(Meta-2)** Kernel 의 *time-homogeneity* — $\mathcal{K}_i$ 가 시간 평행이동에 불변인가? 일부 stage 만 그러한가?
- **(Meta-3)** *Adaptation* 은 kernel 의 시간 변동으로 다룰 것인가, 또는 hidden state 로 augment 할 것인가?
- **(Meta-4)** Stage 4 의 정확한 위치 — 시신경 도착인가, LGN 출구인가, V1 입력인가? (OP-SP-007)
- **(Meta-5)** Markov category $\mathbf{BorelStoch}$ 와 (Ω, σ) Tier 2 카테고리 사이의 forgetful functor 의 정확한 형식.
- **(Meta-6)** Ionescu-Tulcea 결합분포 $\mathbb{P}_{0:4}$ 위의 *time-reversal* 의 의미 — 결정론적 case 에서는 자명하나 stochastic case 에서는 *Bayesian inversion* 으로 처리.

이 메타 문제들은 본 문서에서 결정하지 않는다. Stage 문서에서 stage-specific 결정을 한 뒤 후속 plan 에서 회수.

---

## 8. Glossary of Types (요약)

| 표기 | 의미 |
|------|------|
| $\mathcal{S}_i$ | stage $i$ 의 상태공간 (Polish-Borel) |
| $\mathcal{K}_i : \mathcal{S}_{i-1} \to \mathcal{S}_i$ | stage $i-1 \to i$ stochastic kernel |
| $\Phi_{a \to b}$ | $\mathcal{K}_b \circ \cdots \circ \mathcal{K}_{a+1}$ |
| $\mu_0$ | $\mathcal{S}_0$ 위 입력 측도 |
| $\mathbb{P}_{0:4}$ | $\prod \mathcal{S}_i$ 위 Ionescu-Tulcea 결합분포 |
| $\Sigma_{\text{ret}}$ | 망막 표면 $\subset \mathbb{R}^2$ |
| $\Lambda$ | 파장 영역 $\subset \mathbb{R}^+$ |
| $\mathcal{C}$ | stage 2 채널 색인 |
| $\mathcal{C}_g$ | 신경절세포 채널 색인 |
| $\mathcal{N}(\mathcal{X})$ | $\mathcal{X}$ 위 locally finite counting measure 공간 |
| $\mathcal{M}^+(\mathcal{X})$ | $\mathcal{X}$ 위 locally finite positive measure 공간 |
| $\mathcal{B}_X$ | $\mathcal{X}$ 의 Borel σ-algebra |
| $\mathcal{F}^{\mathcal{S}}_t$ | $\mathcal{S}$ 위 natural filtration 의 $t$-component |
| $\mathbf{BorelStoch}$ | Polish-Borel 측도공간 + stochastic kernel 의 Markov category |
| $I(X; Y)$ | mutual information |
| $\mathcal{I}(\theta)$ | Fisher information |
| $W_p(\mu, \nu)$ | Wasserstein-$p$ distance |
| $\Delta_M$ | $M$ 위 Laplace-Beltrami operator |
| $\delta_x$ | $x$ 에서의 Dirac 측도 |
| $T_\Xi(K)$ | random closed set $\Xi$ 의 Choquet capacity |
| $[\cdot]_+, [\cdot]_-$ | positive / negative half-wave rectification |

---

## 8.5 Lemma — 인과 Kernel 의 합성

§3.3 의 인과성 (Def 3.2 / TC-SP-1.3) 이 합성에 의해 보존됨을 별도 lemma 로 분리. 이는 TC-SP-1.3 의 *full statement* (전체 $\Phi_{0 \to 4}$ 가 인과) 의 기술적 기둥.

**Lemma 8.5 (Causality is preserved by composition)**. $\mathcal{K}_1 : \mathcal{X} \to \mathcal{Y}$, $\mathcal{K}_2 : \mathcal{Y} \to \mathcal{Z}$ 가 §1.4 의 natural filtration $\{\mathcal{F}^{\mathcal{X}}_t\}, \{\mathcal{F}^{\mathcal{Y}}_t\}, \{\mathcal{F}^{\mathcal{Z}}_t\}$ 에 대해 인과적 (§5 의 TC-SP-1.3 (C1) 의미) 이라 하자. 그러면 합성 $\mathcal{K}_2 \circ \mathcal{K}_1 : \mathcal{X} \to \mathcal{Z}$ 도 같은 의미에서 인과적.

**Proof sketch (DEFINITION-DRAFT register)**.

고정된 $T > 0$ 와 $C \in \mathcal{F}^{\mathcal{Z}}_T$.

$\mathcal{K}_2$ 의 인과성 (가정): $y \mapsto \mathcal{K}_2(y, C)$ 는 $\mathcal{F}^{\mathcal{Y}}_T$-가측.

따라서 $\mathcal{K}_2(\cdot, C)$ 가 $\mathcal{F}^{\mathcal{Y}}_T$-가측 함수 $g_C$ 와 동일.

합성 정의:
$$
(\mathcal{K}_2 \circ \mathcal{K}_1)(x, C) = \int_{\mathcal{Y}} g_C(y) \, \mathcal{K}_1(x, dy).
$$

$\mathcal{K}_1$ 의 인과성 (가정): 임의의 $\mathcal{F}^{\mathcal{Y}}_T$-가측 함수 $h$ 에 대해 $x \mapsto \int h(y) \mathcal{K}_1(x, dy)$ 는 $\mathcal{F}^{\mathcal{X}}_T$-가측.

증명: indicator $h = \mathbf{1}_B, B \in \mathcal{F}^{\mathcal{Y}}_T$ 의 경우 $\int \mathbf{1}_B \mathcal{K}_1(x, \cdot) = \mathcal{K}_1(x, B)$ 가 (가정 (C1) 의 $\mathcal{K}_1$-인과성) $\mathcal{F}^{\mathcal{X}}_T$-가측. Monotone class theorem (Theorem 1.11) 으로 일반 $\mathcal{F}^{\mathcal{Y}}_T$-가측 $h$ 로 확장.

$g_C$ 가 $\mathcal{F}^{\mathcal{Y}}_T$-가측이므로 $\int g_C(y) \mathcal{K}_1(x, dy)$ 가 $\mathcal{F}^{\mathcal{X}}_T$-가측 — 정확히 합성의 인과성 (C1).

따라서 $(\mathcal{K}_2 \circ \mathcal{K}_1)(\cdot, C)$ 가 $\mathcal{F}^{\mathcal{X}}_T$-가측 for all $C \in \mathcal{F}^{\mathcal{Z}}_T$. $\square$

**Corollary 8.5a**. $\mathcal{K}_1, \ldots, \mathcal{K}_4$ 가 인과적이면 $\Phi_{0 \to 4} = \mathcal{K}_4 \circ \cdots \circ \mathcal{K}_1$ 도 인과적. (Lemma 8.5 의 3회 반복.)

**의미**. 인과성은 합성의 *local 성질* — 각 단계만 확인하면 전체가 자동으로 보장. 이는 §5 의 TC-SP-1.3 의 진술이 *stage-wise 확인으로 충분* 한 이유.

---

## 9. 본 문서가 *시도하지 않는 것* (재확인)

- 어떤 stage 의 *구체적 dynamics* 도 적지 않음 (02–05 에서)
- 어떤 candidate 도 *canonical-register proof* 를 시도하지 않음 (별도 후속 plan; 본 §5 의 proof sketch 는 DEFINITION-DRAFT 수준)
- (Ω, σ) Tier 2 의 *구체적 매핑* 은 07 로 미룸
- PAI 와의 다리 (interpretation invariance) 시도 없음
- SCC 의 $u_t$ 가 어느 stage 에 해당하는지 결정하지 않음 (OP-SP-006)
- biological reality 의 *완전성* 주장 없음 (top-down feedback, LGN, attention 등은 OP-SP)

---

## 10. Discussion — Why SSKP vs Alternative Formalisms

본 framework 의 선택을 정당화하기 위해, 세 대안 formalism 과의 비교 + SSKP 가 망막 sensing 에 *적합* 한 이유.

### 10.1 대안 (a): 무한차원 결정론적 흐름 (Deterministic flow on infinite-dimensional state)

**Formalism**. 전체 sensing 상태를 하나의 *infinite-dimensional state* $\Psi(t)$ 로 모으고 결정론적 PDE $\partial_t \Psi = F[\Psi]$ 로 진화. 모든 stage 가 $\Psi$ 의 *coordinate projection* 으로 추출.

**예시 분야**. 고전 광학의 wavefront propagation; deterministic neural field theory (Wilson-Cowan).

**SSKP 와의 비교**:

| 항목 | Deterministic flow | SSKP |
|------|---------------------|------|
| Stochasticity | 외부 perturbation 으로만 | 내장 (kernel 자체가 stochastic) |
| Stage 분리 | 인공적 (한 PDE 의 projection) | 본질적 (kernel 사이) |
| 비선형 noise (Poisson, spiking) | 외삽 어려움 | 자연 |
| 계산적 추상화 | nonlocal global | 각 단계 독립 |

**판정**: 결정론적 흐름은 *최선의 경우 stage 0 → stage 1 의 deterministic 부분* (ray optics) 만 다룸. Stage 0 자체가 *Poisson* (광자의 quantum 본질) 이므로 결정론적 framework 는 *부적합*. Stage 3 의 spiking variability 도 동일.

### 10.2 대안 (b): 단일 시간축의 확률과정 (Stochastic process, single time axis, no stages)

**Formalism**. 모든 망막 변수를 하나의 *vector-valued stochastic process* $X(t) \in \mathbb{R}^d$ 로 모으고 SDE / master equation 으로 진화. *Stage 구분이 없음*.

**예시 분야**. Mean-field neural network theory; Wilson-Cowan stochastic.

**SSKP 와의 비교**:

| 항목 | Single-process | SSKP |
|------|----------------|------|
| 정보 흐름 | 양방향 (변수 간 coupling) | 단방향 (stage 정렬) |
| Causality | 시간만 (변수 간은 instant coupling) | 시간 + stage 정렬 |
| Mutual info 분석 | $I(X_i(t); X_j(t))$ — 모든 쌍 | $I(\mathcal{S}_i; \mathcal{S}_j)$ — stage-ordered |
| DPI 의 명시성 | 부재 (variable order 가 분명치 않음) | 자명 (stage order = info-flow order) |
| Bayesian network 의 정합성 | 약함 (DAG 가 자명치 않음) | 강함 (linear DAG) |

**판정**: 단일 process formalism 은 *neural population dynamics* (서로 영향) 에 적합하나 *sensing cascade* (입력 → 출력 의 unidirectional flow) 에는 부자연. 망막은 *근사적으로 unidirectional* (feedforward; top-down feedback 은 OP-SP-010 로 분리) 이므로 stage-ordered SSKP 가 정확.

### 10.3 대안 (c): 일반 그래프 모형 (Graphical model, general DAG / Bayesian network)

**Formalism**. 일반 DAG (또는 undirected graph) 위의 conditional probability table / kernel. 각 node 가 한 변수, edge 가 conditional dependency.

**예시 분야**. Bayesian networks (Pearl); probabilistic graphical models (Koller-Friedman).

**SSKP 와의 비교**:

| 항목 | 일반 DAG | SSKP |
|------|----------|------|
| Topology | 임의 | linear (chain) |
| 일반화 가능성 | 모든 generative model 포함 | sensing cascade 만 |
| 추상 분석 도구 | belief propagation, junction tree | composition algebra |
| 본 framework 적합성 | overkill (구조의 일부만 사용) | minimal 적합 |

**판정**: SSKP 는 일반 DAG 의 *부분 카테고리* (linear chain). 본 framework 의 모든 정리는 *일반 DAG 로 확장 가능* — 단, 망막 sensing 의 구조는 linear (5 stage cascade) 이므로 linear chain 으로 충분. *Top-down feedback* (OP-SP-010) 이 도입되면 DAG cycle 이 생기며 *Bayesian network* (acyclic 일 때) 또는 *factor graph* (cycle 허용) 로 일반화 필요.

### 10.4 SSKP 의 적합성 근거 (요약)

망막 sensing 에 SSKP 가 *최소 적합* framework 인 세 이유:

1. **Stochasticity 의 본질성**: 광자 Poisson, thermal noise, spike variability — 세 단계가 *strictly stochastic*. 결정론적 framework (10.1) 는 표현 불가.

2. **Stage-ordered information flow**: sensing 은 *입력 → 출력* 의 unidirectional cascade. 양방향 coupling 의 process formalism (10.2) 는 *과잉* 표현.

3. **Linear chain structure**: 5 stage 가 명확히 linear DAG. 일반 graphical model (10.3) 의 power 는 필요하지 않음 — *cleaner specialization* 이 본 framework.

추가로, **Markov category 와의 정합** (§2.6) 이 SSKP 를 *synthetic 카테고리 이론* 의 어휘 안에 자연스럽게 임베딩 — 이는 (Ω, σ) Tier 2 lift (07) 의 categorical 정식 (functor 의 존재) 의 기반.

**결론**: SSKP 는 망막 sensing 의 *수학적 정식* 으로서 *적합 + 최소 + 확장 가능* — 본 framework 가 채택되는 정당성.

---

*Framework Master v1 (deepened). 후속: [[02_stage0_photon_point_process]]. 본 문서의 객체·표기·candidate 는 모든 후속 문서가 inherit. 수정 시 후속 문서 일괄 갱신 필요. v1 변경사항: §1.1.1-1.1.3 (Polish / disintegration / counting σ-algebra), §1.4-1.5 (filtration / monotone class), §2.1.1 (deterministic vs stochastic), Lemma 2.3 full sketch, §2.6 (Markov category formal), §3.6 (Ionescu-Tulcea), §3.7 (deterministic embedding), §4.x formal theorem statements + chapter refs, §4.14 stochastic geometry, §5 TC-SP-1.1/1.2/1.3 proof sketches (DEFINITION-DRAFT register), §6.1-6.7 per-doc inheritance, §7 Meta-5, Meta-6 추가, §8.5 causal kernel composition lemma, §10 (a)(b)(c) alternative formalism 비교.*
