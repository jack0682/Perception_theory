---
type: working/sensing_pipeline/cross_cutting
version: v1
date: 2026-05-25
status: DEFINITION-DRAFT
purpose: |
  Cross-cutting document on end-to-end information accounting.
  Builds the mutual-information chain over the SSKP,
  per-stage channel capacity, Fisher information matrix,
  Bayesian posterior P(scene | spikes),
  efficient coding hypothesis (Laughlin 1981; Atick-Redlich),
  variational / free-energy formulation (cited, not adopted),
  asymptotic capacity scaling, optimal decoder bound,
  σ-coarseness information accounting.
  Registers TC-SP-4.1, TC-SP-4.2, TC-SP-4.3.
register: DEFINITION-DRAFT + THEOREM-CANDIDATE (sketches only)
parent: 01_framework_master
constraint_compliance:
  canonical_theorem_changes: 0
  scc_edits: 0
  new_TC_or_OP_codes: 0  # v1 elaborations stay within existing TC-SP-4.1..4.3
---

> [!nav] Parent: [[00_INDEX]] · Prev: [[05_stage3_ganglion_spike_encoding]] · Next: [[07_omega_sigma_lift]]

# Cross-cutting — End-to-End Information Bound

## 0. 본 문서의 위치

본 문서는 stage 0–3 의 정보를 *통합 회계* 한다. Stage 별 도구는 [[02_stage0_photon_point_process|02]]–[[05_stage3_ganglion_spike_encoding|05]] 에서 등록되었고, 본 문서는:

- DPI chain 의 stage-별 instance (§2, 전체 증명 포함)
- 각 stage 의 channel capacity 의 *정량적* 추정 (§2.2)
- Fisher information chain 의 양의 반정부호 (positive semi-definite, PSD) ordering (§3, 증명 포함)
- Cramér-Rao 한계 로 부터 *contrast detection threshold* 의 유도 (§3.4)
- Bayesian posterior $P(\text{scene} \mid \text{spikes})$ 의 단일 픽셀 분석적 예 (§4.3)
- 자연 광 통계와의 *효율 부호화* — Laughlin (1981) 의 *full derivation*, Atick–Redlich (1990) 의 *full whitening derivation*, 자연 색 spectrum PCA 의 *수치 eigendecomposition* (§5)
- Variational / Free-energy formulation 의 *명시적 변분 부등식* + 채택 거부 이유 + stage 3 decoder 의 *KL minimization 예* (§6)
- SCC 4-energy term 의 stage-2 sub-stage 대응 (§7, suggestive only)
- *Asymptotic capacity* — high-photon / low-contrast scaling laws (§8)
- *Optimal decoder bound* — spike-train Bayesian posterior 의 Wegener–Anderson-type 한계 (§9)
- (Ω, σ) Tier 2 lift 의 정보 보존 정량 — σ-coarseness trade-off (§13)

본 문서가 *수행하지 않는 것*: 단일 stage 의 dynamics (→ 02–05); (Ω, σ) lift 의 *구체 형식* (→ [[07_omega_sigma_lift|07]]).

---

## 1. 정보론적 객체들 — 측도론적 정의

### 1.1 Mutual information — measure-theoretic 정의

**Definition 1.1 (Mutual information, Kullback–Leibler form)**. 측도공간 $(\mathcal{X}, \mathcal{B}_X), (\mathcal{Y}, \mathcal{B}_Y)$ 와 그 곱 위 결합측도 $\mu_{XY}$ (marginals $\mu_X = (\pi_X)_* \mu_{XY}, \mu_Y = (\pi_Y)_* \mu_{XY}$) 에 대해

$$
I(X; Y) := \begin{cases} \displaystyle \int_{\mathcal{X} \times \mathcal{Y}} \log\!\frac{d \mu_{XY}}{d (\mu_X \otimes \mu_Y)} \, d\mu_{XY} & \mu_{XY} \ll \mu_X \otimes \mu_Y \\[4pt] +\infty & \text{otherwise.} \end{cases}
$$

**Properties (Cover–Thomas Ch. 2; Pinsker 1964)**:

1. $I(X; Y) \geq 0$, with equality iff $X, Y$ independent (Gibbs inequality).
2. $I(X; Y) = I(Y; X)$ (symmetric).
3. $I(X; Y) = D_{\text{KL}}(\mu_{XY} \| \mu_X \otimes \mu_Y)$ — KL divergence.

**핵심 관찰**: $I(X; Y)$ 는 *base measure 선택과 무관* — KL divergence 가 base measure 의 Radon–Nikodym 변환 하에서 *불변* 이기 때문 ($\frac{d\mu/d\nu_1}{d\mu/d\nu_2} = d\nu_2/d\nu_1$ 의 log 가 적분에서 상쇄). 이는 sensing pipeline 의 stage 들이 *다른 type 의 공간* (점과정, 함수공간, 다채널 graded, spike train) 에서 작동해도 *동일한 정보 측정* 을 적용 가능하게 함.

### 1.2 Entropy — discrete vs differential vs relative

**세 종류의 entropy 가 sensing pipeline 에서 모두 등장**:

**(a) Discrete entropy** (counting measure $\nu_{\#}$ over countable space):

$$
H(X) := - \sum_{x \in \mathcal{X}} \mu_X(\{x\}) \log \mu_X(\{x\}) \in [0, \infty]
$$

- 항상 $\geq 0$
- $X$ 가 stage 3 spike count, stage 0 photon count 의 finite-window restriction 등에서 등장

**(b) Differential entropy** (Lebesgue base $dx$ over $\mathbb{R}^n$):

$$
h(X) := - \int p(x) \log p(x) \, dx, \quad p = d\mu_X / dx
$$

- *부호 임의* — 좌표 변환 하에서 *Jacobian 만큼 shift*: $X \mapsto AX$ 일 때 $h(AX) = h(X) + \log |\det A|$
- $X$ 가 stage 1 graded membrane potential $V_p(t)$ 의 sampled snapshot 등에서 등장
- *단위 의존* — $X$ 의 단위 (mV vs V) 가 바뀌면 entropy 가 바뀜 → "절대 정보량" 이라 부르기 부적절

**(c) Relative entropy / KL divergence** (base measure $\nu$ unspecified):

$$
D_{\text{KL}}(\mu \| \nu) := \int \log\!\frac{d\mu}{d\nu} \, d\mu, \quad \mu \ll \nu
$$

- *base-measure-free, 항상 $\geq 0$, 좌표 변환 불변* (Radon–Nikodym 의 chain rule)
- Mutual information $I(X; Y) = D_{\text{KL}}(\mu_{XY} \| \mu_X \otimes \mu_Y)$
- *근본적* 정보 측정 — discrete / differential entropy 둘 다 KL 의 특수 경우

**핵심 사실 (Gelfand–Yaglom–Perez 1956–59)**: 가측 분해 $\{B_i\}_{i \in \mathcal{F}}$ 에 의해 $X, Y$ 를 *finite-alphabet quantization* $X_\mathcal{F}, Y_\mathcal{F}$ 로 환원할 때

$$
I(X; Y) = \sup_{\mathcal{F}, \mathcal{G}} I(X_\mathcal{F}; Y_\mathcal{G})
$$

(sup 은 모든 finite 분해 위). 즉, *연속* mutual information 은 *모든 finite 분해의 sup* — discrete 으로 정확히 reduce 가능한 양. 이게 sensing pipeline 의 mixed (continuous + discrete) stage 사이의 mutual information 을 *single 정의* 로 다룰 수 있는 근거.

**참조**: Gelfand & Yaglom (1957), "Calculation of the amount of information about a random function contained in another such function," *Uspekhi Mat. Nauk* 12; Pinsker (1964), *Information and Information Stability of Random Variables and Processes*; Cover–Thomas Thm 8.5.1.

### 1.3 Conditional mutual information

**Definition 1.3**. 확률공간 $(\Omega, \mathcal{F}, P)$ 위 random variables $X, Y, Z$ 에 대해

$$
I(X; Y \mid Z) := \mathbb{E}_Z\big[ I(X; Y \mid Z = z) \big] = \int I(X; Y \mid Z = z) \, dP_Z(z)
$$

with $I(X; Y \mid Z = z)$ 가 *conditional law* $P_{XY|Z=z}$ 에 대한 mutual information.

**Key property** (chain rule of mutual information; Cover–Thomas Thm 2.5.2):

$$
I(X; Y, Z) = I(X; Z) + I(X; Y \mid Z)
$$

이게 §2 의 DPI 증명의 *핵심 도구*.

### 1.4 Channel capacity

**Definition 1.4**. Stochastic kernel $\mathcal{K} : \mathcal{X} \to \mathcal{Y}$ 의 capacity:

$$
C(\mathcal{K}) := \sup_{\mu_X \in \mathcal{P}_{\text{adm}}(\mathcal{X})} I_\mathcal{K}(X; Y)
$$

with $I_\mathcal{K}(X; Y) = I(X; Y)$ when $Y \sim \mathcal{K}(X, \cdot)$, $X \sim \mu_X$. Sup 은 *admissible* 입력 분포 (power constraint, mean constraint, support constraint) 위.

### 1.5 Fisher information

**Definition 1.5**. Parametric family $\{P_\theta\}_{\theta \in \Theta}$ on $\mathcal{X}$, with $\Theta \subset \mathbb{R}^k$ open. Score:

$$
s_\theta(x) := \nabla_\theta \log p(x \mid \theta), \quad p(\cdot \mid \theta) = dP_\theta / d\nu
$$

Fisher information matrix:

$$
\mathcal{I}(\theta) := \mathbb{E}_{P_\theta}\!\big[ s_\theta(X) \, s_\theta(X)^T \big] \in \mathbb{R}^{k \times k}_{\succeq 0}
$$

**Cramér–Rao bound**: 임의 unbiased $\hat{\theta}$ 에 대해 $\text{Cov}[\hat{\theta}] \succeq \mathcal{I}(\theta)^{-1}$ (PSD ordering).

### 1.6 Rate-distortion function

**Definition 1.6**. Source $X$ + distortion $d : \mathcal{X} \times \hat{\mathcal{X}} \to \mathbb{R}^+$:

$$
R(D) := \inf_{P_{\hat{X}|X} : \mathbb{E} d(X, \hat{X}) \leq D} I(X; \hat{X})
$$

압축의 정보론적 하한.

---

## 2. Data Processing Inequality Chain

### 2.1 Stage-별 DPI

[[01_framework_master#TC-SP-1.2|01 TC-SP-1.2]] 의 직접 확장:

$$
\underbrace{H(\mathcal{S}_0)}_{\text{photon stream}} \geq I(\mathcal{S}_0; \mathcal{S}_1) \geq I(\mathcal{S}_0; \mathcal{S}_2) \geq I(\mathcal{S}_0; \mathcal{S}_3) \geq I(\mathcal{S}_0; \mathcal{S}_4)
$$

가정: 각 $\mathcal{K}_i$ 가 *conditional independent from prior stages given $\mathcal{S}_{i-1}$* — Markov property.

### 2.2 TC-SP-1.2 — 전체 증명 (재현)

**Theorem (DPI for SSKP)**. $\mathcal{S}_0 \xrightarrow{\mathcal{K}_1} \mathcal{S}_1 \xrightarrow{\mathcal{K}_2} \mathcal{S}_2 \xrightarrow{\mathcal{K}_3} \mathcal{S}_3 \xrightarrow{\mathcal{K}_4} \mathcal{S}_4$ 가 Markov chain (각 $\mathcal{S}_i$ 가 $\mathcal{S}_{i-1}$ 에 의해 conditionally 독립 from prior) 일 때 임의 입력 분포 $\mu_0$ 에 대해

$$
I(\mathcal{S}_0; \mathcal{S}_1) \geq I(\mathcal{S}_0; \mathcal{S}_2) \geq I(\mathcal{S}_0; \mathcal{S}_3) \geq I(\mathcal{S}_0; \mathcal{S}_4).
$$

**Proof**.

*Step 1 — 3-variable lemma* (Cover–Thomas Thm 2.8.1). $X \to Y \to Z$ Markov chain (즉 $X \perp Z \mid Y$) 라 하자. Chain rule of mutual information (§1.3) 을 두 가지 방식으로 적용:

$$
I(X; Y, Z) = I(X; Y) + I(X; Z \mid Y) \quad (*)
$$
$$
I(X; Y, Z) = I(X; Z) + I(X; Y \mid Z) \quad (**)
$$

Markov 가정 $X \perp Z \mid Y$ 로부터 $I(X; Z \mid Y) = 0$ (conditional MI 는 conditional independence 의 측정). 따라서 $(*)$ 가

$$
I(X; Y, Z) = I(X; Y).
$$

$(**)$ 와 비교:

$$
I(X; Y) = I(X; Z) + I(X; Y \mid Z) \geq I(X; Z)
$$

(왜냐하면 $I(X; Y \mid Z) \geq 0$, conditional MI 가 KL divergence 의 평균이므로 비음). 따라서 $I(X; Z) \leq I(X; Y)$. $\square$

*Step 2 — 4-fold induction*. 위 lemma 를 sensing pipeline 의 4 연속 단계에 반복 적용:

- $(\mathcal{S}_0, \mathcal{S}_1, \mathcal{S}_2)$ Markov 적용 → $I(\mathcal{S}_0; \mathcal{S}_2) \leq I(\mathcal{S}_0; \mathcal{S}_1)$.
- $(\mathcal{S}_0, \mathcal{S}_2, \mathcal{S}_3)$ Markov 적용 → $I(\mathcal{S}_0; \mathcal{S}_3) \leq I(\mathcal{S}_0; \mathcal{S}_2)$.
- $(\mathcal{S}_0, \mathcal{S}_3, \mathcal{S}_4)$ Markov 적용 → $I(\mathcal{S}_0; \mathcal{S}_4) \leq I(\mathcal{S}_0; \mathcal{S}_3)$.

세 부등식을 결합 → 전체 chain. $\blacksquare$

**필요한 Markov 가정의 미세 검증**: SSKP 의 합성 $\Phi_{0 \to i} = \mathcal{K}_i \circ \cdots \circ \mathcal{K}_1$ 가 Markov 임을 보이려면, *$\mathcal{S}_i$ 가 $\mathcal{S}_{i-1}$ 만 보고 출력을 생성* 해야 함 (이전 stage 들의 *추가 메모리 없이*). 이는 [[01_framework_master#3.3 인과성|01 §3.3]] 의 *no-feedback assumption* — top-down feedback 무시 가정. 망막에 실제로는 centrifugal feedback 이 있으나 (OP-SP-010) 본 디렉토리는 *forward-only* 채택. 따라서 DPI 적용 가능.

### 2.3 각 stage 의 손실 — *정량적* 추정

[[06_endtoend_information_bound#2.2|이전 v0]] 의 *qualitative table* 을 다음 *정량 추정* 으로 대체. 단위: bits/photon (per absorbed photon) 또는 bits/sec (rate).

**Stage 0 → 1 (광수용기 적분)**.

광수용기 $V_p(t) = V_{\text{rest}} + \int_{-\infty}^t r_1(t-s) \, dN_p(s) + \text{noise}$ 형태 (single-photon impulse response $r_1$ 의 *시간 적분*).

손실 mechanism: *시간 적분 ${\sim} 100$ ms window* 가 *광자 도래 시각의 정밀도* 를 잃음. 한 photoreceptor 의 단위 시간당 입사 광자수가 $\bar n$ 이라면, integrating window $\tau_{\text{int}}$ 안의 absorbed photon count $K \sim \text{Poisson}(\bar n \tau_{\text{int}})$.

광자 stream $N$ 의 단위시간당 *raw* entropy (timing 포함; *finite-window restriction*):

$$
H_{\text{photon}}(\tau_{\text{int}}) \approx \bar n \tau_{\text{int}} \cdot \log\!\frac{e \cdot \tau_{\text{int}}}{\delta_t}
$$

with $\delta_t$ effective timing 해상도 (예: photoreceptor quantum noise jitter, ${\sim} 1$ ms). Membrane potential 의 finite-bandwidth Gaussian 통신 capacity ([[#1.4 Channel capacity|§1.4]]):

$$
C_{\text{V}}(\tau_{\text{int}}) \approx W_V \cdot \log_2\!\big(1 + V^2 / \sigma_V^2 \big)
$$

with $W_V$ membrane bandwidth (${\sim} 20$ Hz), $\sigma_V$ thermal noise.

**Bound**:

$$
\text{Loss}_{0 \to 1} \gtrsim H_{\text{photon}}(\tau_{\text{int}}) - C_V(\tau_{\text{int}})
$$

전형값: $\bar n \tau_{\text{int}} \sim 100$ photons/100ms × $\log(100 / 0.001) \approx 1150$ bits/sec photon-stream entropy; 광수용기 capacity ${\sim} 20 \log_2(50) \approx 110$ bits/sec. *Loss 약 1 order of magnitude* (~$10^3$ bits/sec at moderate light). 이게 *time integration 으로 인한 정밀 timing 손실*.

**Stage 1 → 2 (DoG bandpass)**.

DoG bandpass 의 DC removal: $\alpha \to 1$ 일 때 ([[04_stage2_inner_retinal_algebra#4.2 DoG kernel|04 §4.2]]) integral $\int K_{\text{DoG}} = 1 - \alpha \to 0$. 입력 신호의 *DC 성분* (mean luminance) 이 *완전 제거*.

손실 bound (rate-distortion form): 입력 $V$ 가 spatial power spectrum $S_V(\xi)$ 라면, DoG transfer function $\hat K(\xi)$ 의 zero crossing 근방의 정보가 손실. 정량:

$$
\text{Loss}_{1 \to 2} \lesssim \int_{\xi : |\hat K(\xi)| < \epsilon} \tfrac{1}{2} \log\!\big(1 + S_V(\xi)/\sigma^2 \big) \, d\xi
$$

전형값: $\sim 1$ bit per spatial frequency band, total ${\sim} 5-10$ bits/sec — *작음*.

**Stage 2 → 3 (ganglion compression, TC-SP-3.3)**.

[[05_stage3_ganglion_spike_encoding#TC-SP-3.3|05 TC-SP-3.3]] 의 explicit bound:

$$
\text{Loss}_{2 \to 3} \leq \sum_{c \in \mathcal{C}_g^{\text{periph}}} \log\!\Big(1 + L_{\text{RF}}^2(c) / L_{\text{corr}}^2 \Big)
$$

전형값: peripheral $L_{\text{RF}} \sim 1-5$ deg, $L_{\text{corr}} \sim 1$ deg → $\sim 1-5$ bits/cell. Total over ${\sim} 10^6$ peripheral cells, after weighting by relative area: $\sim 10^5-10^6$ bits/sec total compression. *Largest loss*.

**Stage 3 → 4 (optic nerve transmission)**.

본질적 손실 0 — 단순 axonal conduction with no compression. *Latency* (M ${\sim} 70$ ms, P ${\sim} 100$ ms) 가 *시간 axis re-parameterization* 만, *information* 손실 없음. (TC-SP-3.2 의 *alignment cost* 는 stage 4 *이후* — V1 에서 발생.)

$$
\text{Loss}_{3 \to 4} \approx 0
$$

**요약 table** (bits/sec, order-of-magnitude, moderate photopic light):

| 단계 | Loss (bits/sec) | 기 mechanism |
|------|-----|-----|
| 0 → 1 | ${\sim} 10^3$ | Photoreceptor 시간 적분 + Naka–Rushton 압축 |
| 1 → 2 | ${\sim} 10$ | DoG DC removal |
| 2 → 3 | ${\sim} 10^5-10^6$ | 126:1 신경절 압축 (peripheral) |
| 3 → 4 | $\approx 0$ | 단순 axonal latency |

Total 입력 (photon stream entropy) ${\sim} 10^9$ bits/sec; total 출력 (optic nerve) ${\sim} 5 \times 10^6$ bits/sec → *factor ${\sim} 200$ 압축*.

### 2.4 합성 capacity bound

### TC-SP-4.1 — [DELETED 2026-05-25 Pass 5 #11 model misspecification]

**Status**: **DELETED via Pass 5 #11**. Shannon channel capacity 가정 — (i) coding over arbitrary long blocks, (ii) optimal encoder/decoder pair, (iii) memoryless or strictly stationary channel, (iv) transmitter freely choosing arbitrary message — *모두 retina 에 적용 안 됨*. 망막은 communication channel 이 아니라 *task-specific lossy transformation for downstream perception/action* (Geisler 2008); 추출하는 정보는 *task-relevant Fisher information about scene parameters*, *Shannon source bits 아님*. Min C(K_i) bound 는 mathematically correct *for idealized Shannon channel*; *retinal perception 의 operational limit 아님*.

**Original statement (preserved for audit trail)**:

> $C(\Phi_{0 \to 4}) \leq \min_{i} C(\mathcal{K}_i)$ — bottleneck stage 가 한계.

**Why DELETED**: 본 TC 의 *Shannon capacity framing* 자체가 retina 에 misspecified. Same fundamental issue 로 *이미* deleted TC-SP-3.1 (rate sufficiency / Cox channel-capacity) — Shannon capacity 는 *wrong object* for biological information processing. 06 본문의 entire information-theoretic framework 가 본 TC 위에 build 됨; 본 TC 박탈 시 framework 자체가 *conjectural*.

**Replacement**: §2.4 의 capacity bound 본문은 *generic Shannon-theoretic fact* 로 유지 — *retinal application* 은 *conjecture* 로 격하. Task-relevant Fisher information bounds (Geisler 2008, Pillow-Simoncelli 2003) 가 더 적절한 framework — 추후 별도 작업. TC 자격 박탈.

### 2.5 Lossy-Stage 회계

### TC-SP-4.2 — [DELETED 2026-05-25 Pass 4]

**Status**: **DELETED via Pass 4** (cumulative 2 HOLE: Pass 3 #5 + Pass 4 #51 — *inherits TC-SP-3.1's Cox violation*; v0→v1 ranking reversal 자체가 *fragility 의 가시화*).

**Original statement (preserved for audit trail)**:

> Natural scene 분포 가정 하: Loss(K_3) > Loss(K_1) > Loss(K_2) > Loss(K_4).

**Why DELETED**:
- Inherits TC-SP-3.1 (Rate Sufficiency, also DELETED) 의 Cox process 가정 위반 — per-stage capacity estimates 자체가 Cox approximation 에 의존.
- v0 → v1 ranking *reversal* (qualitative intuition vs quantitative — direction flipped) 가 estimate 의 *fragility* 직접 보임.
- Strict inequalities at *ties boundary* 미처리 (Pass 4 #46 UNCLEAR): adjacent stage losses 가 order-of-magnitude 추정에서 *tie* 가능.
- Pattern #51 confirms: per-stage loss estimates assume channels are independent contributors — population coding noise correlations 가 ranking 을 재배열 가능.

**Replacement**: §2.3 의 *quantitative bit-rate estimates* 본문 유지 — *order-of-magnitude empirical estimates* 로. *Ranking 정리* 자격 박탈. 진화적 critical points 는 *qualitative claim* 으로 §2.5 본문에 유지.

---

## 3. Fisher Information at Each Stage

### 3.1 Stage-별 Fisher matrix

자극 parameter $\theta$ (예: contrast, orientation, velocity) 에 대한 Fisher information:

$$
\mathcal{I}_i(\theta) := \mathbb{E}_{P_\theta(\mathcal{S}_i)}\!\big[ s_\theta^{(i)} (s_\theta^{(i)})^T \big], \quad s_\theta^{(i)} = \nabla_\theta \log p_i(\mathcal{S}_i | \theta).
$$

### 3.2 Fisher DPI — 증명

**Theorem (Fisher Information DPI; van Trees 1968, Zamir 1998)**. $X \to Y \to Z$ Markov chain with parametric family $\{P_\theta\}$ 일 때

$$
\mathcal{I}_X(\theta) \succeq \mathcal{I}_Y(\theta) \succeq \mathcal{I}_Z(\theta) \quad \text{(PSD ordering)}.
$$

**Proof (sketch)**. 한 단계 (인접 $Y \to Z$) 의 증명:

Markov chain $Y \to Z$ ($Y$ 를 알면 $Z$ 가 conditionally $\theta$-independent: $p(z|y, \theta) = p(z|y)$). Score 의 conditional expectation:

$$
\mathbb{E}[s^{(Y)}_\theta(Y) \mid Z = z] = \frac{\int s^{(Y)}_\theta(y) p(z|y) p(y|\theta) dy}{\int p(z|y) p(y|\theta) dy}
$$

Bayes' formula 로 이를 정리하면 $\mathbb{E}[s^{(Y)}_\theta \mid Z] = s^{(Z)}_\theta(Z)$. 즉, *$Z$ 의 score 가 $Y$ 의 score 의 conditional expectation*.

이제 Jensen / law-of-total-covariance:

$$
\mathcal{I}_Y(\theta) = \text{Cov}(s^{(Y)}_\theta) = \mathbb{E}[\text{Cov}(s^{(Y)}_\theta \mid Z)] + \text{Cov}(\mathbb{E}[s^{(Y)}_\theta \mid Z])
$$

$$
= \mathbb{E}[\text{Cov}(s^{(Y)}_\theta \mid Z)] + \text{Cov}(s^{(Z)}_\theta)
$$

$$
= \underbrace{\mathbb{E}[\text{Cov}(s^{(Y)}_\theta \mid Z)]}_{\succeq 0 \text{ (PSD)}} + \mathcal{I}_Z(\theta)
$$

따라서 $\mathcal{I}_Y(\theta) - \mathcal{I}_Z(\theta) \succeq 0$. 동일 논리를 $X \to Y$ 에 적용 → 전체 chain. $\blacksquare$

**참조**: van Trees (1968), *Detection, Estimation, and Modulation Theory*, Vol. I, §2; Zamir (1998), "A proof of the Fisher information inequality via a data processing argument," *IEEE TIT* 44.

### 3.3 Sensing pipeline Fisher chain

$$
\boxed{\mathcal{I}_0(\theta) \succeq \mathcal{I}_1(\theta) \succeq \mathcal{I}_2(\theta) \succeq \mathcal{I}_3(\theta) \succeq \mathcal{I}_4(\theta)}
$$

각 stage 의 *최적 decoder* 가 도달할 수 있는 *최소 분산*:

$$
\text{Var}[\hat{\theta} | \mathcal{S}_i] \succeq \mathcal{I}_i(\theta)^{-1}
$$

후속 stage 에서 *추정 정확도* 단조 *악화*.

### 3.4 Stage 1 Fisher matrix — *explicit* contrast parameter

설정: spatial 위치 $x$ 의 photoreceptor 의 graded membrane potential

$$
V_p(t) = V_0 + g \cdot \theta + \xi(t), \quad \xi(t) \sim \mathcal{N}(0, \sigma_V^2)
$$

with $\theta$ = scene contrast (about background), $g$ = photoreceptor gain (bits/contrast unit, depends on Naka–Rushton derivative at operating point).

광자 도래 측면도 포함: 입사 광자수 $N \sim \text{Poisson}(\bar n (1 + \theta))$ in integration window $\tau_{\text{int}}$, with $\bar n = $ background rate.

**Joint likelihood** (graded + Poisson photon):

$$
p(V, N \mid \theta) = \underbrace{\frac{1}{\sqrt{2\pi\sigma_V^2}} \exp\!\Big(-\tfrac{(V - V_0 - g\theta)^2}{2\sigma_V^2}\Big)}_{\text{thermal Gaussian}} \cdot \underbrace{\frac{(\bar n (1+\theta) \tau_{\text{int}})^N e^{-\bar n(1+\theta)\tau_{\text{int}}}}{N!}}_{\text{Poisson photon}}
$$

Score:

$$
s_\theta = \partial_\theta \log p = \frac{g(V - V_0 - g\theta)}{\sigma_V^2} + \frac{N - \bar n(1+\theta)\tau_{\text{int}}}{1 + \theta}
$$

Fisher information (단일 channel):

$$
\boxed{\mathcal{I}_1(\theta) = \frac{g^2}{\sigma_V^2} + \frac{\bar n \tau_{\text{int}}}{1 + \theta}}
$$

두 *additive* contributions: *thermal* (Gaussian, $\theta$-independent) + *photon shot* (Poisson, scales with mean light).

### 3.5 Cramér–Rao detection threshold

Detection task: *$\theta > \theta_{\text{thr}}$ 이면 detect, otherwise miss*. Threshold $\theta_{\text{thr}}$ 를 *unbiased estimator 의 표준편차 = $\theta$* 조건 (signal-to-noise = 1) 으로 정의:

$$
\theta_{\text{thr}}^2 = \text{Var}[\hat\theta] = \mathcal{I}_1(\theta)^{-1} = \Big(\frac{g^2}{\sigma_V^2} + \frac{\bar n \tau_{\text{int}}}{1 + \theta}\Big)^{-1}
$$

**Low-light limit** ($\bar n \tau_{\text{int}} \ll g^2/\sigma_V^2$): Poisson shot noise dominates:

$$
\theta_{\text{thr}} \approx \frac{1}{\sqrt{\bar n \tau_{\text{int}}}}
$$

이게 *Rose–de Vries law*: detection threshold $\propto 1/\sqrt{N_{\text{photons}}}$ — *quantum limit*. 망막의 single-photon sensitivity (Baylor 1979) 가 *이 한계에 근접*.

**High-light limit** ($\bar n \tau_{\text{int}} \gg g^2/\sigma_V^2$): thermal noise dominates:

$$
\theta_{\text{thr}} \approx \frac{\sigma_V}{g}
$$

*Photon noise 가 사라지고 thermal 만 남은 regime* — Weber's law 의 정보론적 기원.

**관찰적 의미** ([[02_stage0_photon_point_process#7.2 Photon noise limit|02 §7.2]], Hecht–Shlaer–Pirenne 1942): 어두운 조건의 detection threshold 가 *${\sim} 5-7$ absorbed photons* — 위 $\theta_{\text{thr}} \approx 1/\sqrt{\bar n \tau_{\text{int}}} \approx 1/\sqrt{5} \approx 0.45$ (effective contrast) 와 *일치*. 즉, *psychophysical 한계 = single-photon Cramér–Rao 한계*.

이게 DPI (TC-SP-1.2) + Fisher chain (§3.2) 의 정확한 정량적 implication: 망막의 stage 0 Fisher information 이 *psychophysical detection threshold* 의 absolute floor.

### 3.6 자극의 정확한 인식 가능성

지각 임계가 *어느 stage* 의 $\mathcal{I}^{-1}$ 에 의해 결정되는가?

- *Detection task*: stage 0-1 의 photon Poisson noise (§3.4-5)
- *Discrimination task* (orientation, motion): stage 2-3 의 channel-specific noise — DoG bandwidth, DSGC tuning sharpness
- *Categorization task*: stage 3 이후 cortical noise (out of scope)

망막은 *detection level* 의 한계에 *근접* — *near-quantum-limited*.

---

## 4. Bayesian Posterior — Scene Reconstruction

### 4.1 정의

뇌가 풀어야 하는 inverse problem:

$$
P(\text{scene} | \text{spikes}) = \frac{P(\text{spikes} | \text{scene}) \cdot P(\text{scene})}{P(\text{spikes})}
$$

- $P(\text{spikes} | \text{scene}) = \Phi_{0 \to 4}(\cdot | \text{scene})$
- $P(\text{scene})$: 자연 장면 사전분포
- $P(\text{spikes})$: marginal (intractable in general)

### 4.2 Decoder 의 한계

*Optimal decoder* 는 posterior 의 *mean* (Bayes optimal MSE) 또는 *MAP*. 둘 모두 Cramér-Rao bound $\mathcal{I}^{-1}$ 에 한정. Posterior variance:

$$
\text{Var}[\theta \mid \mathcal{S}_4] \geq \mathcal{I}_4(\theta)^{-1} \geq \mathcal{I}_0(\theta)^{-1}
$$

(Fisher DPI).

### 4.3 단일 픽셀 분석적 예 — *posterior variance scaling*

설정 (가장 단순):

- *Scene*: 단일 픽셀, intensity $\theta \in [0, \theta_{\max}]$
- *Prior*: $P(\theta) = \mathcal{N}(\theta_0, \sigma_\theta^2)$ (truncated to $[0, \theta_{\max}]$; ignore truncation for tractability)
- *Forward model*: photon count $K \sim \text{Poisson}(\eta \theta \tau)$ in window $\tau$, with $\eta$ = quantum efficiency × area
- *Observation*: $K$ photons absorbed in single integration window

**Likelihood**:

$$
P(K \mid \theta) = \frac{(\eta \theta \tau)^K e^{-\eta \theta \tau}}{K!}
$$

**Posterior**:

$$
P(\theta \mid K) \propto \theta^K \exp\!\Big(-\eta\tau \theta - \tfrac{(\theta-\theta_0)^2}{2\sigma_\theta^2}\Big)
$$

**Saddle point / Laplace approximation** (centered at MAP $\hat\theta$):

MAP 조건: $\partial_\theta \log P = K/\theta - \eta\tau - (\theta - \theta_0)/\sigma_\theta^2 = 0$.

For $\sigma_\theta \to \infty$ (uninformative prior): $\hat\theta = K / (\eta\tau)$.

Curvature at $\hat\theta$:

$$
-\partial_\theta^2 \log P \big|_{\hat\theta} = \frac{K}{\hat\theta^2} + \frac{1}{\sigma_\theta^2} = \frac{(\eta\tau)^2}{K} + \frac{1}{\sigma_\theta^2}
$$

**Posterior variance** (Gaussian approx):

$$
\boxed{\text{Var}[\theta \mid K] \approx \Big(\frac{(\eta\tau)^2}{K} + \frac{1}{\sigma_\theta^2}\Big)^{-1}}
$$

**Scaling**:
- *Photon-limited* (small $K$, weak prior $\sigma_\theta \to \infty$): $\text{Var}[\theta \mid K] \approx K / (\eta\tau)^2 \approx \theta / (\eta\tau)$. *Variance $\propto 1/$ photon count*.
- *Prior-limited* (large $\sigma_\theta$, large $K$): $\text{Var}[\theta \mid K] \to 0$ as $K \to \infty$.

**핵심 사실**: posterior *standard deviation* $\propto 1/\sqrt{K}$ — single-photon Cramér–Rao bound (Rose–de Vries) 와 일치. *Bayesian posterior variance scales inversely with photon count*. 이게 *natural prior 가 강하지 않은 한 limit*; strong prior 가 있으면 더 좁은 posterior 가능 (but biased).

### 4.4 Multi-pixel generalization

전체 장면 $\boldsymbol\theta \in \mathbb{R}^N$ 와 spike train $\boldsymbol G$:

$$
P(\boldsymbol\theta \mid \boldsymbol G) \propto P(\boldsymbol G \mid \boldsymbol\theta) \cdot P(\boldsymbol\theta)
$$

with $P(\boldsymbol\theta)$ a natural-scene prior — *Gaussian process* with $1/f^\alpha$ power spectrum (Field 1987). Conjugate inference 가능 → posterior covariance:

$$
\text{Cov}[\boldsymbol\theta \mid \boldsymbol G] = (\mathcal{I}_4(\boldsymbol\theta) + \Sigma_{\text{prior}}^{-1})^{-1}
$$

with $\mathcal{I}_4$ stage-4 Fisher matrix, $\Sigma_{\text{prior}}$ scene covariance.

이는 *추후 work* 의 framework. 본 문서는 *원칙*만 기록.

---

## 5. 효율 부호화 — 자연 통계와의 alignment

### 5.1 Barlow's hypothesis (1961)

> "Sensory systems are adapted to the *statistics of the natural environment*."

원시적 statement: *redundancy reduction* — 자연 신호의 *상관 구조* 를 제거하여 *효율적 부호*.

### 5.2 Laughlin (1981) — Naka-Rushton optimality

**핵심 결과** (Laughlin 1981, *Z. Naturforsch.*): 광수용기의 input-output 변환은 *자연 광 강도 분포의 누적 CDF* 와 일치하면 mutual information 을 *최대화*.

#### 5.2.1 TC-SP-4.3 — *Full derivation*

**Statement**: $I \in \mathbb{R}^+$ random input, distribution $p_I$, CDF $F_I(i) = \int_0^i p_I(t) dt$. $f : \mathbb{R}^+ \to [0, 1]$ monotone with $f(0) = 0, f(\infty) = 1$. Output $R = f(I)$.

> Among all monotone $f$, $f^* = F_I$ uniquely maximizes $I(I; R)$ — i.e., $I(I; R) \leq I(I; F_I(I))$ with equality iff $f = F_I$.

(Single-symbol channel, no added noise.)

**Proof**.

*Step 1 — noiseless deterministic case (degenerate)*. $R = f(I)$ exactly determines $I$ via $I = f^{-1}(R)$ (monotone). Thus $I(I; R) = H(I) = H(R)$ for any monotone $f$. Information is *equal* — not strictly maximized.

*Step 2 — bounded output range with noise* (relevant biological case). 출력 $R$ 가 *bounded support* $[0, R_{\max}]$ + *additive output noise* $\xi$ (bounded variance) — *neural output 의 dynamic range 한계*. 즉,

$$
\tilde R = f(I) + \xi, \quad \xi \in [-\delta/2, \delta/2]
$$

Output entropy bound: $H(\tilde R) \leq \log_2 R_{\max}/\delta$ (*finite dynamic range, finite noise quantization*).

By bounded-range entropy maximization: $H(\tilde R)$ 는 $\tilde R$ 가 *uniform on $[0, R_{\max}]$* 일 때 maximized (KL bound: $D_{\text{KL}}(p_R \| U_{[0, R_{\max}]}) \geq 0$).

*Step 3 — monotone $f$ 와 uniform output 의 동치*. Probability integral transform (Casella–Berger Thm 2.1.10): $R = F_I(I) \implies R \sim U_{[0, 1]}$ exactly. 즉, $f = F_I$ 가 *uniform output* 을 달성하는 유일한 monotone $f$ ($[0, 1]$ normalize).

*Step 4 — mutual information bound*. Noisy output with fixed noise $\xi$:

$$
I(I; \tilde R) = H(\tilde R) - H(\tilde R | I) = H(\tilde R) - H(\xi)
$$

$H(\xi)$ 가 $f$ 와 무관 (noise 가 output 단의 additive). 따라서 $I(I; \tilde R)$ 가 $H(\tilde R)$ 와 monotone — Step 2-3 에 의해 $f = F_I$ 가 *uniquely maximizing*. $\blacksquare$

#### 5.2.2 자연 광 통계와 Naka–Rushton 의 일치

자연 광 강도 $I$ 의 *empirical distribution* (Brady–Field 2000, Frazor–Geisler 2006) 가 log-normal 또는 Weibull 형태. 그 CDF $F_I$ 가 sigmoidal 형태.

**Naka–Rushton response**:

$$
R(I) = R_{\max} \frac{I^n}{I^n + I_{50}^n}
$$

is the *Hill function* — sigmoidal. With $n \approx 1$, this is $R(I) = R_{\max} I/(I + I_{50})$.

CDF of log-normal distribution: $F_I(i) = \Phi(\log i / \sigma)$ where $\Phi$ = standard normal CDF. *Both are sigmoidal, both monotone, similar shape with appropriate $I_{50}$*. Quantitative fit: Laughlin (1981) showed *< 5% deviation* between fly LMC response curve and natural-intensity CDF.

#### 5.2.3 영장류 망막에서의 일치

영장류 cone Naka–Rushton parameters: $n \approx 1, I_{50} \approx 50$ td (trolands) at photopic adaptation level. Natural-intensity log-mean $\approx 70$ td (Frazor–Geisler 2006). 정성적 일치, 정량적 fit *within order-of-magnitude*.

### TC-SP-4.3 — [DELETED 2026-05-25 Pass 4]

**Status**: **DELETED via Pass 4** (cumulative 3 HOLE: Pass 3 #5 + Pass 4 #46 + #51). Verifier #46: additive Gaussian noise on bounded output $R \in [0, R_{\max}]$ 가 *structural incompatibility* 정확히 saturation boundary 에서. Verifier #51: iid sample 가정이 natural light 의 strong temporal correlation 위반.

**Original statement (preserved for audit trail)**:

> Naka-Rushton 변환이 자연 광 CDF 와 (fitting 내에서) 일치 → mutual information 근사적 최대화 (bounded-output + additive-noise 하).

**Why DELETED**:
- Pass 3 #5: Markov adaptation 가정이 multi-timescale 적응 (OP-SP-009) 으로 위반; bounded-range hypothesis 가 Laughlin 1981 원본보다 *추가됨* 으로 verification gap.
- Pass 4 #46 (boundary): *additive Gaussian noise* 가 *bounded output range* 와 *구조적 incompatible* — saturation boundary ($R = 0, R = R_{\max}$) 에서 noise leaks beyond support; Laughlin optimality 가 $O(\sigma_n)$ 이내에서 깨짐 — 미처리.
- Pass 4 #51 (independence): natural light 의 strong temporal correlation ($\tau_c \sim 50-100$ ms) → iid input distribution 가정 위반; derivation 이 *marginal* CDF 만 최적화, *joint* 구조 미활용.
- 3 patterns HOLE + 가장 load-bearing 한 *추가* TC 였음 (§5 Laughlin/Atick-Redlich edifice 의 핵심) → 박탈.

**Replacement**: §5.2 의 *Laughlin 1981 derivation* 본문 유지 — *partial empirical result* (Brady-Field 2000, Frazor-Geisler 2006) 로. *Optimality 정리* 자격 박탈. Naka-Rushton 의 *biological 적정성* 은 *empirical fitting* 으로만 — *first-principle proof* 아님.

### 5.3 Atick-Redlich (1990) — Decorrelation / whitening — *full derivation*

**Setup**: spatially extended input $V(x)$, with $x \in \Sigma_{\text{ret}}$. Natural image second-order statistic:

$$
C_{\text{nat}}(x, x') := \mathbb{E}[V(x) V(x')] - \mathbb{E}[V(x)]\mathbb{E}[V(x')]
$$

Translation-invariant (over small patches): $C_{\text{nat}}(x, x') = c(x - x')$ depends only on offset. Power spectrum:

$$
S_V(\xi) := \int c(\Delta) e^{-i\xi \cdot \Delta} d\Delta
$$

*Natural images*: $S_V(\xi) \propto 1/|\xi|^\alpha$ with $\alpha \approx 2$ (Field 1987; Ruderman–Bialek 1994). I.e., *power-law decay* (1/f² spectrum).

#### 5.3.1 Whitening derivation

**Question**: linear filter $W$ to apply: $\tilde V(x) = (W * V)(x)$ such that $\tilde V$ has *flat* (uniform) power spectrum (= maximally decorrelated, white).

**Constraint**: filter must trade off whitening (high-frequency boost) against output noise (signal/noise at high frequency is bad → don't amplify pure noise).

**Atick–Redlich (1990) optimization**: find $W$ minimizing

$$
\mathcal{L}[W] = D_{\text{KL}}\big(\, p_{\tilde V} \, \big\| \, \mathcal{N}(0, \sigma_{\text{out}}^2 \cdot \mathbb{I}) \,\big) + \lambda \cdot \mathbb{E}[\| W * V \|^2]
$$

Sub. Plancherel/Parseval:

$$
\mathcal{L}[W] = \int \Big[ \frac{|\hat W(\xi)|^2 S_V(\xi) + \hat N(\xi)}{\sigma_{\text{out}}^2} - 1 - \log\frac{|\hat W(\xi)|^2 S_V(\xi) + \hat N(\xi)}{\sigma_{\text{out}}^2} \Big] d\xi + \lambda \int |\hat W|^2 S_V \, d\xi
$$

where $\hat N(\xi)$ is the *input* noise spectrum (sensor/photoreceptor noise).

**Variational condition** $\delta \mathcal{L} / \delta \hat W = 0$:

$$
\hat W^*(\xi)^2 = \frac{\sigma_{\text{out}}^2 - \hat N(\xi)}{S_V(\xi) \cdot (1 + \lambda \sigma_{\text{out}}^2)}
$$

Up to constants, this simplifies (Atick–Redlich 1990, Eq. 25):

$$
\boxed{\hat W^*(\xi) = \big( S_V(\xi) + \sigma_{\text{noise}}^2 \big)^{-1/2}}
$$

(noise-regularized whitening).

#### 5.3.2 DoG matches this filter (approximately)

For $S_V(\xi) = K/|\xi|^2$ (1/f² spectrum) and noise floor $\sigma^2$:

$$
\hat W^*(\xi) = (K/|\xi|^2 + \sigma^2)^{-1/2}
$$

- *Low frequency* ($|\xi|$ small): $\hat W^*(\xi) \approx |\xi|/\sqrt{K}$ — *high-pass* (linear boost). DoG also has high-pass low-frequency response.
- *High frequency* ($|\xi|$ large): $\hat W^*(\xi) \approx 1/\sigma$ — *flat saturation*. DoG also rolls off at high frequency (Gaussian cutoff at $|\xi| \sim 1/\sigma_c$).
- *Crossover* at $|\xi|_* \sim \sqrt{K}/\sigma$ — where noise comparable to signal.

DoG 의 Fourier transform: $\hat K_{\text{DoG}}(\xi) = e^{-\sigma_c^2 |\xi|^2 / 2} - \alpha e^{-\sigma_s^2 |\xi|^2 / 2}$. *Bandpass*: peaks at $|\xi| \sim 1/\sigma_c$, rolls off both sides. *Matches the whitening filter qualitatively*.

따라서 *DoG receptive field 가 natural-image whitening filter 의 근사*.

#### 5.3.3 Predictive coding interpretation

Atick–Redlich 의 또 다른 해석: *predictive coding*. 입력의 *expected value* (predicted from surrounding context via spatial correlation) 를 빼면 *residual* — *prediction error* 만 전송.

수학적 형식: $\tilde V(x) = V(x) - \mathbb{E}[V(x) | V(\text{surround})]$.

Surround 의 Bayesian conditional expectation 가 $C_{\text{nat}}(x, \cdot) C_{\text{nat}}(\cdot, \cdot)^{-1} V(\cdot)$ — *weighted sum of surround* (the *prediction*).

For 1/f² natural images, this weighting equals (approximately) the *DoG surround*. Thus *DoG = (input) - (predicted input from surround)* = *prediction error*. 이게 *predictive coding 의 망막 instance* (Srinivasan–Laughlin 1982; Rao–Ballard 1999 의 cortical 일반화의 원형).

### 5.4 색 대립의 PCA optimality — *explicit eigendecomposition*

[[04_stage2_inner_retinal_algebra#6.3 군론적 정당화|04 §6.3]] 의 TC-SP-2.6 — L-M, S-(L+M), L+M 이 *자연 광원 spectral statistic 의 PCA*. 본 v1 에서 *수치적 eigendecomposition* 추가.

#### 5.4.1 자연 spectrum 의 측정

Ruderman, Cronin, Chiao (1998) — *Statistics of cone responses to natural images*: 자연 장면 의 cone activation $(V_L, V_M, V_S)$ 의 covariance matrix 측정.

*Forested environment*:

$$
C_{\text{LMS}} \approx \begin{pmatrix} 1.000 & 0.989 & 0.788 \\ 0.989 & 1.000 & 0.829 \\ 0.788 & 0.829 & 1.000 \end{pmatrix} \cdot \sigma_{\text{cone}}^2
$$

(*L-M correlation 0.989* — *매우* 큰 redundancy 두 채널 사이.)

#### 5.4.2 Eigendecomposition

이 $3 \times 3$ symmetric matrix 의 eigendecomposition:

**Eigenvalues** (descending):

$$
\lambda_1 \approx 2.776, \quad \lambda_2 \approx 0.207, \quad \lambda_3 \approx 0.017
$$

(Trace = 3, 정확함. $\sigma_{\text{cone}}^2 = 1$ 단위.)

**Ratios**:

$$
\lambda_1 / \lambda_2 \approx 13.4, \quad \lambda_2 / \lambda_3 \approx 12.2
$$

**Eigenvectors**:

- $\mathbf{v}_1 \approx (0.577, 0.585, 0.570)^T$ — *근사적으로 $(L + M + S)/\sqrt{3}$* — *luminance axis*
- $\mathbf{v}_2 \approx (0.402, 0.426, -0.811)^T$ — *근사적으로 $-S + (L+M)/2$* — *blue-yellow axis*
- $\mathbf{v}_3 \approx (0.711, -0.690, 0.135)^T$ — *근사적으로 $L - M$* — *red-green axis*

#### 5.4.3 해석

- *$\lambda_1 \gg \lambda_2 \gg \lambda_3$*: variance dominated by *luminance* (L+M+S). Color information 은 *${\sim} 10\%$* of total variance.
- *Blue-yellow (S vs L+M) 가 red-green (L-M) 보다 ${\sim} 10 \times$ variance*. *자연 광의 spectral 가변성이 short-wavelength 에서 더 큼* — sky vs sunset.
- 망막의 *parvocellular L-M* + *koniocellular S-(L+M)* 회로가 *bottom two PC axes* 와 일치. *Magnocellular luminance* 가 *top PC* (가장 큰 variance) 와 일치.

#### 5.4.4 TC-SP-2.6 의 강화

자연 spectrum covariance 의 PCA 가 *quantitative 단위* (정확한 eigenvalue ratio) 까지 망막의 *3 채널 분리* 와 *일치*. 진화가 *PCA 최적해* 에 정확히 수렴한 형식.

### 5.5 효율 부호화 통합 statement

본 stage 들의 모든 변환이 *하나의 원리* 로 환원:

> **(EC-Principle, candidate)** 망막의 각 변환 $\mathcal{K}_i$ 는 (자연 통계 $\mu_{\text{nat}}$ 와 sensor 한계 하에서) *mutual information* $I(\text{input}; \text{output})$ 를 *근사적으로 maximize* — 또는 동치적으로 *redundancy reduction* 을 수행.

이는 본 문서가 *통합 metaprinciple* 으로 등록하나, *증명 가능 statement* 가 아님 (각 stage 마다 다른 측면의 efficient coding 이 작동).

---

## 6. Variational / Free-Energy Formulation (cited, not adopted)

### 6.1 Friston's variational free energy — *formal statement*

Friston (2010): 인지 시스템이 *generative model* $p(x, y)$ 와 *recognition density* $q(x | y)$ 를 가질 때, *variational free energy*:

$$
\boxed{F[q] := \mathbb{E}_q[\log q(x|y) - \log p(x, y)] = D_{\text{KL}}(q \| p_{x|y}) - \log p(y)}
$$

여기서 $x$ = hidden states (cause), $y$ = sensory observations.

**Key identity** (Jensen / Gibbs):

$$
F[q] = -\log p(y) + D_{\text{KL}}(q \| p_{x|y}) \geq -\log p(y)
$$

(equality iff $q = p_{x|y}$, true posterior).

**Implications**:
- *$\min_q F[q] = -\log p(y)$* — Bayesian evidence (negative log marginal likelihood).
- *$F$ 를 최소화* 하는 것은 동치적으로 *evidence $\log p(y)$ 를 최대화* (free-energy principle 의 *evidence approximation* 측면).
- 추가 가정 (active inference): action 도 $F$ 를 최소화 — i.e., 신경계가 *unsurprising* sensory state 를 추구.

### 6.2 본 디렉토리의 입장 — *왜 채택하지 않는가*

**채택하지 않음**. 이유:

1. **너무 일반적** — Free-energy principle 은 *generative model + recognition density* 만 있으면 거의 모든 시스템에 적용 가능. 따라서 *망막의 특이성* (왜 DoG? 왜 ON/OFF? 왜 126:1 압축?) 을 *predict* 안 함 — 단지 *post-hoc 정리*.

2. **본 디렉토리의 DEFINITION-DRAFT 원칙** — settled 기초 (Shannon mutual information, Cramér–Rao, DPI) 위에서만 작업. FEP 의 *active inference* 측면은 controversial: action selection 의 free-energy 해석은 standard reinforcement learning / Bayesian decision theory 와 *동치인가 다른가* 미해결 (Aitchison–Lengyel 2017, Biehl–Pollock–Kanai 2021).

3. **PAI 호환성 불명확** — Friston 의 action 통합은 PAI (Perception–Action–Interpretation) 의 OP-PAI-002 와 *유사 형식* 이나 *interpretation invariance* 가 FEP framework 에서 어떻게 등장하는지 명확하지 않음. 본 디렉토리는 PAI 와 isolated 작업 (sensing stage 만).

4. **수학적 rigor** — Friston 의 FEP 가 *physics analogy* (statistical mechanics) 에 의존; *exchangeable* 형식으로의 분석적 reduction 이 어떤 가정 하에서 가능한지 *full mathematical proof* 가 controversial.

다만 *reference* 로 등록: future work 에서 connection 시도 가능. 본 디렉토리에서는 *언급* 만.

### 6.3 Variational 형식 예 — Stage 3 spike decoder

본 framework 의 *내부* 에서, 한 stage 의 변환을 *KL minimization* 으로 표현 가능한가? 예: stage 3 의 optimal Bayesian decoder.

**Setup**:
- $B \in \mathcal{S}_2$ = stage 2 input (graded multi-channel signal)
- $G \in \mathcal{S}_3$ = stage 3 output (spike trains)
- $p(G | B)$ = stage 3 kernel ($\mathcal{K}_3$, Cox model)
- Optimal *Bayesian decoder*: $q(B | G) \propto p(G | B) p(B)$ — posterior

**Variational formulation**: approximate posterior $q(B | G) \in \mathcal{Q}$ (some tractable family) by

$$
q^*(B | G) = \arg\min_{q \in \mathcal{Q}} D_{\text{KL}}\big( q(B | G) \, \big\| \, p(B | G) \big)
$$

Expanding KL:

$$
D_{\text{KL}}(q \| p) = \mathbb{E}_q[\log q(B|G)] - \mathbb{E}_q[\log p(B|G)]
$$

$$
= \mathbb{E}_q[\log q(B|G)] - \mathbb{E}_q[\log p(G|B) + \log p(B)] + \log p(G)
$$

$$
= -\underbrace{\mathbb{E}_q[\log p(G|B)]}_{\text{data fit (Cox likelihood)}} + \underbrace{D_{\text{KL}}(q(B|G) \| p(B))}_{\text{prior complexity}} + \log p(G)
$$

Drop the $\log p(G)$ (constant in $q$); minimize the first two terms:

$$
\mathcal{L}_{\text{ELBO}}[q] := \mathbb{E}_q[\log p(G | B)] - D_{\text{KL}}(q(B|G) \| p(B))
$$

This is the *ELBO* (Evidence Lower BOund) of variational inference. Optimal decoder = ELBO maximizer.

**Explicit Cox case**: $\log p(G | B) = \sum_c \int [\log \lambda_c(t) dN_c(t) - \lambda_c(t) dt]$ with $\lambda_c(t) = \phi(w_c B_{\sigma(c)}(p_c, t))$. ELBO becomes a *trace integral* over the spike train, evaluable analytically for Gaussian $q$.

**관찰**: stage 3 의 *decoder* 가 variational form 으로 표현 가능 — 그러나 이는 *general fact about Bayesian inference*, *FEP 의 unique implication 이 아님*. 따라서 FEP 채택 없이도 variational decoding 활용 가능.

---

## 7. SCC 의 $E_{\text{cl}}, E_{\text{sep}}, E_{\text{bd}}, E_{\text{tr}}$ 와의 candidate 연결

본 디렉토리는 *PAI 와의 다리* 시도 안 함 ([[00_INDEX#7. 본 디렉토리가 시도하지 않는 것|00 §7]]). 그러나 *SCC 의 energy framework* 와의 *formal 유사성* 은 등록 가치 있음.

### 7.1 4-term 대응의 정밀화 (v1 추가)

| SCC term | Stage 2 sub-stage 대응 | 정밀 형식 |
|----------|------------------------------------|---|
| $E_{\text{cl}}$ (closure) | $\mathcal{K}_{2b}$ center 적분 | DoG center Gaussian $G_{\sigma_c} * V$ — *국소 cohesion 추출* |
| $E_{\text{sep}}$ (separation) | $\mathcal{K}_{2a}$ Riesz 분해 | ON/OFF half-wave $[V]_+, [V]_-$ — *부호 separation* |
| $E_{\text{bd}}$ (boundary) | $\mathcal{K}_{2b}$ DoG zero-crossing | Marr–Hildreth edge detection — *boundary 추출* |
| $E_{\text{tr}}$ (transport) | $\mathcal{K}_{2c}$ + $\mathcal{K}_3$ spike OT | Adelson–Bergen + Wasserstein on spike train — *time-axis transport* |

### 7.2 Suggestive evidence

1. *SCC 의 4 항이 conceptually 독립* (canonical CV-1.13 §2 axiom) — *stage 2 의 4 sub-stage 도 conceptually 독립* ([[04_stage2_inner_retinal_algebra#2. Stage 2 의 전체 구조|04 §2]]).
2. *Closure 가 stabilization tendency (A3), idempotence 아님* — *DoG center adaptation* 도 *steady-state convergence*, idempotence 아님.
3. *Separation 가 정보 보존 with 부호 분리* — *Riesz lattice 분해의 uniqueness* (TC-SP-2.1) 가 정확히 이 형식.
4. *Boundary 가 zero crossing* (sign change) — *DoG zero-crossing* 이 edge 의 정확한 정의 (TC-SP-2.2).
5. *Transport 가 time evolution along velocity* — *Adelson–Bergen velocity-tuned slab* (TC-SP-2.4) 가 spacetime 의 정확한 transport 추적.

### 7.3 *주의 — Caveats*

이 대응은 *suggestive 형식 유사성*, *증명 가능 isomorphism 아님*. 구체적 caveats:

- *SCC 의 $E_{\text{cl}}, E_{\text{sep}}, E_{\text{bd}}, E_{\text{tr}}$ 는 graph 위 함수의 energy* — *stage 2 의 sub-stage 들은 함수 → 함수 변환*. 두 framework 의 *type 이 다름* (energy vs operator).
- *SCC 는 formation 동역학 (gradient flow on Σ_m)* — *stage 2 는 feedforward kernel*. *Dynamics vs feedforward* 의 본질적 차이.
- *SCC primitive $u_t$ 가 어느 stage 의 객체에 해당하는가* — OP-SP-006 (미해결).

본 디렉토리는 *기록만*; 정합 분석은 후속 plan (PAI bridge work).

---

## 8. 새로운 — Asymptotic Capacity Scaling

[[#TC-SP-4.1|TC-SP-4.1]] 의 극한 거동 분석. 두 자연 극한: *high photon count* (밝은 광) 와 *low contrast* (탐지 임계).

### 8.1 High-photon limit ($\bar n \to \infty$)

$\bar n$ = mean photon flux. Stage 0 의 entropy:

$$
H(\mathcal{S}_0; \tau) \sim \bar n \tau \log(\bar n \tau)
$$

(Poisson entropy at large rate).

Stage 1 의 capacity (Gaussian channel with rate-proportional shot noise):

$$
C_1 \sim W_V \cdot \log_2\!\big(1 + g^2 \bar n / \sigma_V^2 \big) \sim W_V \log_2(\bar n) \quad \text{as } \bar n \to \infty
$$

*Logarithmic* growth with photon count.

Stage 3 의 capacity (Cox model, $\bar\lambda \propto \bar n^{\text{something}}$):

$$
C_3 \sim |\mathcal{C}_g| \cdot \log_2(\bar\lambda / W_c)
$$

*Saturating* — ganglion firing rate has biophysical ceiling ($\bar\lambda_{\max} \sim 200$ Hz).

**End-to-end** (TC-SP-4.1):

$$
C(\Phi_{0 \to 4}) \to C_3^{\text{sat}} \approx 10^6 \cdot \log_2(200) \approx 8 \times 10^6 \text{ bits/sec}
$$

as $\bar n \to \infty$. *Bottleneck 이 stage 3 (ganglion saturation)*.

**Scaling law**: $C(\Phi_{0 \to 4}) \to C_{\max}^{\text{ganglion}}$ exponentially fast in $\bar n$. *효율 부호화가 saturation 한계를 결정* — 진화가 ganglion 의 spike rate ceiling 을 *information-limit* 으로 조정.

### 8.2 Low-contrast limit ($\theta \to 0$)

Contrast $\theta$ → 0 (자극 vs background 의 차이가 작음). Fisher information at $\theta = 0$ (§3.4):

$$
\mathcal{I}_1(0) = g^2/\sigma_V^2 + \bar n \tau_{\text{int}}
$$

*$\theta$-independent at $\theta = 0$* — 즉, *near-threshold sensitivity* 가 $\theta$ 와 무관 한 상수.

*Channel capacity at low contrast* (Gaussian approximation around $\theta = 0$):

$$
C_1(\theta \to 0) \sim \tfrac{1}{2} \log_2\!\big(1 + \theta^2 \mathcal{I}_1(0) \big) \sim \tfrac{\theta^2}{2 \ln 2} \cdot \mathcal{I}_1(0)
$$

*Quadratic* in $\theta$. *Capacity 가 $\theta^2$ 비례로 0 으로 감소*.

Detection threshold (signal/noise = 1):

$$
\theta_{\text{thr}} \sim \mathcal{I}_1(0)^{-1/2} \sim (\bar n \tau_{\text{int}})^{-1/2}
$$

(low-light limit) — *Rose–de Vries* (§3.5). *Quantum-limited*.

### 8.3 Photopic vs scotopic regime crossover

$\bar n \tau_{\text{int}} \approx g^2 / \sigma_V^2$ 에서 *crossover* — *photon noise vs thermal noise* 가 같은 크기.

- $\bar n \tau_{\text{int}} < g^2/\sigma_V^2$: *scotopic* (dark) regime, photon-limited, $\theta_{\text{thr}} \propto 1/\sqrt{\bar n}$
- $\bar n \tau_{\text{int}} > g^2/\sigma_V^2$: *photopic* (bright) regime, thermal-limited, $\theta_{\text{thr}} \approx \sigma_V/g$ (Weber's law)

전형 crossover: $\bar n \tau_{\text{int}} \approx 10^3-10^4$ photons. *어두운 별빛 - 달빛 사이* 의 luminance 범위에서 일어남.

### 8.4 종합 Scaling Table

| Regime | $C(\Phi_{0 \to 4})$ | $\theta_{\text{thr}}$ | Bottleneck |
|--------|---|---|---|
| Scotopic ($\bar n \tau \ll 10^3$) | $\sim W_V \log_2 \bar n$ | $\sim 1/\sqrt{\bar n \tau}$ | Photon shot noise |
| Mesopic ($\bar n \tau \sim 10^3-10^4$) | $\sim 10^4-10^5$ bits/sec | crossover | Mixed |
| Photopic ($\bar n \tau \gg 10^4$) | $\sim 8 \times 10^6$ bits/sec (saturated) | $\sim \sigma_V/g$ | Ganglion saturation |

---

## 9. 새로운 — Optimal Decoder Bound

[[#4.1 정의|§4.1]] 의 posterior $P(\text{scene} | \text{spikes})$ 의 *최적 decoder* 의 한계.

### 9.1 Spike-train Bayesian posterior

Stage 4 출력 $\boldsymbol G \in \mathcal{S}_4 = \mathcal{S}_3$ (latency-shifted spike trains). Scene $\boldsymbol s \in \mathcal{S}_{\text{scene}}$.

Forward model: $\boldsymbol G \sim \Phi_{0 \to 4}(\cdot | \boldsymbol s)$ — full pipeline likelihood. Cox model 가정:

$$
p(\boldsymbol G | \boldsymbol s) = \prod_c \exp\!\Big[\int_0^T \log \lambda_c(t; \boldsymbol s) \, dN_c(t) - \int_0^T \lambda_c(t; \boldsymbol s) \, dt \Big]
$$

with $\lambda_c$ a (deterministic) functional of $\boldsymbol s$ via the cascade $\boldsymbol s \to V \to B \to \lambda$.

### 9.2 Posterior bound — Wegener–Anderson 형식

**Theorem (Posterior concentration; van Trees–Bell 2007, applied)**.

Let $\hat{\boldsymbol s}$ = posterior mean estimator. Then for any prior $p(\boldsymbol s)$ with finite Fisher metric $\mathcal{I}_{\text{prior}}$:

$$
\mathbb{E}_{\boldsymbol s, \boldsymbol G}\big[ (\hat{\boldsymbol s} - \boldsymbol s)(\hat{\boldsymbol s} - \boldsymbol s)^T \big] \succeq \big( \mathcal{I}_4(\boldsymbol s) + \mathcal{I}_{\text{prior}}(\boldsymbol s) \big)^{-1}
$$

*Bayesian Cramér–Rao bound* (van Trees inequality). Posterior covariance bounded below by *combined Fisher* (data + prior).

### 9.3 Asymptotic concentration

장시간 관측 ($T \to \infty$, 또는 *increasing photon count* via $\bar n \to \infty$): Fisher $\mathcal{I}_4 \propto T$ or $\propto \bar n$. Therefore posterior covariance $\propto 1/T$ or $\propto 1/\bar n$ — *concentration around true scene at rate $T^{-1/2}$* (Bayesian central limit theorem).

**조건**: prior $p(\boldsymbol s)$ 가 *non-degenerate* (positive density at true scene), forward model *identifiable* (no fundamental ambiguities).

### 9.4 실용 한계 — Approximate decoders

*Exact* Bayesian decoder 가 *intractable* (high-dimensional posterior, $\boldsymbol s \in \mathbb{R}^{N \gg 10^6}$). Approximate methods:

1. *MAP*: $\arg\max_{\boldsymbol s} p(\boldsymbol s | \boldsymbol G)$ — Laplace approximation, gradient ascent.
2. *Variational*: minimize $D_{\text{KL}}(q \| p)$ over tractable $q$ family (§6.3).
3. *Sampling*: MCMC, particle filters.
4. *Linear Bayesian* (Gaussian assumption): closed-form posterior covariance, biased but fast.

각 approximate decoder 가 *optimal posterior 의 하한* 보다 *위* 의 variance — bounded by van Trees inequality.

### 9.5 Decodability 의 정보론적 분리

$\boldsymbol s$ 의 *어느 측면* 이 decodable? Fisher matrix $\mathcal{I}_4(\boldsymbol s)$ 의 *eigenstructure* 가 답:

- *Top eigenvectors* (large eigenvalues): decoded with high precision — e.g., luminance, large-scale edges
- *Bottom eigenvectors* (small eigenvalues): degraded / lost — e.g., fine spatial detail in periphery, high spatial frequency under low light

*Information geometry*: Fisher matrix induces a Riemannian metric on scene manifold; decodability anisotropy = metric anisotropy.

본 디렉토리는 *원칙*만 기록; explicit decoder design 은 cortical processing (out of scope).

---

## 10. 정보 흐름의 한 줄 요약

```
H(scene) ≫ H(photons hitting retina)            [external optics: lossy]
                  > I(photons; photoreceptor V)        [stage 1 lossy ~ 10^3 bits/sec]
                  > I(photons; bipolar+amacrine B)     [stage 2 mild loss ~ 10 bits/sec]
                  > I(photons; ganglion spikes G)      [stage 3 lossy ~ 10^5-10^6 bits/sec]
                  ≈ I(photons; optic-nerve arrival)    [stage 4 lossless]
```

각 부등호의 *정확한 손실* 이 §2.3 의 회계 대상. 두 lossy stages (1, 3) 가 *진화적 critical points*. *Stage 3 이 dominant* (peripheral compression, v1 correction).

---

## 11. Theorem-Candidates summary

| 코드 | 명제 | 위치 | v1 추가 |
|------|------|------|------|
| TC-SP-4.1 | End-to-end capacity ≤ min stage capacity | §2.4 | Asymptotic bound §8 |
| TC-SP-4.2 | Stage 3 + Stage 1 dominant lossy (v1 corrected order) | §2.5 | Quantitative §2.3 |
| TC-SP-4.3 | Naka-Rushton ≈ natural-intensity CDF (info max) | §5.2 | Full derivation §5.2.1 |

(추가 candidate TC-SP-2.6 은 [[04_stage2_inner_retinal_algebra|04]] 에 등록; §5.4 에서 quantitative eigendecomposition 확장.)

---

## 12. 도구 사용 summary

| 도구 ([[01_framework_master#4. 수학적 도구 카탈로그|01 §4]]) | 사용 |
|------|------|
| 4.8 정보이론 | mutual information (§1.1, measure-theoretic); DPI (§2, full proof); capacity (§1.4); rate-distortion (§1.6); Fisher information chain (§3, full proof); Cramér–Rao (§3.5) |
| 4.13 변분법 | free-energy (§6, cited with full formula); ELBO (§6.3); efficient coding optimization (§5.3.1) |
| 4.11 최적수송 | (preview) Wasserstein for spike train comparison |
| 4.12 군이론 | (cross-reference) symmetry-based redundancy reduction; color PCA eigenstructure |

---

## 13. (Ω, σ) Tier 2 와의 연결 — σ-coarseness 정보 보존

[[07_omega_sigma_lift|07]] 에서 본격 전개. 본 §13 은 *정보론적 정당화* 의 정량적 측면 (v1 확장).

### 13.1 σ-graph 의 정보 표현

$\Omega = $ pipeline 의 *event 집합* (e.g., $\Omega_0 = $ photon events, $\Omega_3 = $ spike events). $\sigma : \Omega \times \Omega \to \{0, 1\}$ = *binary co-belonging relation* (또는 weighted $\sigma : \Omega \times \Omega \to [0, 1]$).

*Information content of σ*: σ-aware encoding (e.g., connected components, persistent homology of σ-graph) 이 추가 정보를 carry. 그러나 *σ 자체의 entropy* 가 *coarseness* 에 의존.

### 13.2 σ-coarseness trade-off — *정량*

**Setup**: σ-relation 의 *threshold* $\tau$ — "두 사건이 시공간 distance $< \tau$" 면 σ-connected.

- $\tau \to 0$ (*fine*): σ trivial — 대부분 사건이 자기 자신만 σ-connected. *No structure carried by σ* — σ 가 *identity relation 에 근접*.
- $\tau \to \infty$ (*coarse*): σ 모든 사건을 연결 — *complete graph*. *No discrimination 가능* — σ 가 *trivial structure*.
- $\tau$ *medium* (e.g., correlation length of natural signal): σ 가 *meaningful clustering* 를 표현 — *maximal σ-information*.

**정보론적 측정**: σ-graph $G_\sigma$ 의 information content (e.g., # of connected components, betti numbers $\beta_0, \beta_1$ of σ-induced complex):

$$
I(\text{scene}; G_\sigma) = f(\tau)
$$

with $f(\tau)$ unimodal, peaking at $\tau^* \sim $ natural correlation length.

### 13.3 σ-aware encoding 의 추가 정보 vs σ-trivial encoding

**σ-aware**: pipeline 출력 = $(B, G_\sigma)$ — graded responses + σ-graph as side information.

**σ-trivial**: pipeline 출력 = $B$ only (σ implicit / lost).

추가 정보:

$$
\Delta I = I(\text{scene}; B, G_\sigma) - I(\text{scene}; B) = I(\text{scene}; G_\sigma | B)
$$

- *Too fine $\tau$*: $G_\sigma$ 가 $B$ 에 의해 *완전 결정* (각 event 의 location + time 만으로 fine σ 계산 가능) → $\Delta I \approx 0$. *σ adds nothing*.
- *Too coarse $\tau$*: $G_\sigma$ 가 *trivial* (constant graph) → $\Delta I \approx 0$. *σ adds nothing*.
- *Optimal $\tau^*$*: $G_\sigma$ 가 $B$ *위의 추가 structure* (clustering at correlation length) → $\Delta I > 0$. *σ adds bits proportional to log of cluster count*.

### 13.4 함의 — σ 선택 기준의 정보론적 정당화

본 문서의 회계가 $\sigma$ 의 *선택 기준* 을 제공:

- *정보 보존*: $\sigma_i$ 가 *high-correlation 사건들을 연결* (clustering 의 information).
- *Redundancy reduction*: $\sigma_i$ 가 *대비 사건들 (ON-OFF) 도 연결* (predictive coding 의 cross-channel).
- *최적 coarseness*: $\tau^* \sim $ stage 의 *natural correlation length* (stage 0 의 mean inter-photon time, stage 3 의 mean inter-spike interval).

본 디렉토리는 *원칙만* 등록; [[07_omega_sigma_lift|07]] 가 정확한 σ-coarseness propagation 을 다룸.

### 13.5 OP — σ 의 optimal coarseness 의 닫힌 형식

본 문서에서는 *open meta-question*: $\tau^*$ 의 닫힌 form 이 *자연 통계* (correlation length) 와 *sensor 한계* (timing resolution) 의 정확한 함수 인가? Empirically $\tau^* \sim L_{\text{corr}}$ 이지만 *분석적 derivation* 미존재. ([[08_open_problems_sp|08]] 에서 추가 등록 검토 — 단 신규 OP code 등록은 본 v1 의 권한 밖.)

---

## 14. Open Problems registered here

본 문서에서 신규 OP code 등록 없음 (디렉토리 정책: 본 v1 elaboration 은 기존 TC-SP-4.1..4.3 만 elaborate). 본 문서의 OP 후보들은 모두 stage 문서 또는 [[08_open_problems_sp|08]] 에서 등록.

다만 *meta-question* 으로 §7 의 SCC-pipeline parallel 의 *수학적 본질* + §13.5 의 σ-coarseness optimal 은 미해결 (등록 보류).

---

## 15. 본 문서가 *시도하지 않는 것*

- *정확한 수치* end-to-end bound (numerical) — §2.3 의 *order-of-magnitude* 만; numerical 정밀 작업은 별도
- *Decoder design* 의 구체적 implementation (§9 는 *bound* 만)
- PAI 와의 연결 — 격리
- *Free-energy principle* 의 채택 — 단지 cited (§6 full formula 추가)
- *Information geometry* — Fisher matrix 의 Riemannian 구조는 §9.5 에서 *언급* 만; 별도 작업
- *Multi-photon coherence* (Bose-Einstein bunching) 의 정보론적 보정 — OP-SP-001 의 영역

---

## 16. 정리 — v1 변경 사항

본 v1 (2026-05-25) 의 v0 대비 추가:

- §1: measure-theoretic Mutual information / KL / Gelfand–Yaglom–Perez 추가
- §2.2: TC-SP-1.2 *full proof* 재현 (chain rule + 4-fold induction)
- §2.3: per-stage loss 의 *quantitative bounds* (qualitative table → numbers)
- §2.5: TC-SP-4.2 ranking *v1 corrected* (stage 3 dominant, not stage 1)
- §3.2: Fisher DPI *full proof* (van Trees / Zamir)
- §3.4-5: stage-1 explicit Fisher matrix + Rose-de Vries Cramér-Rao threshold
- §4.3: single-pixel Bayesian posterior analytic example with $1/\sqrt{K}$ scaling
- §5.2.1: TC-SP-4.3 *full derivation* (probability integral transform + bounded output)
- §5.3.1: Atick-Redlich whitening *full derivation* (noise-regularized $S_V^{-1/2}$)
- §5.3.3: predictive coding interpretation
- §5.4: explicit *eigendecomposition* of Ruderman-Cronin-Chiao spectrum
- §6.1: Friston FEP *formal variational identity*
- §6.3: Stage-3 decoder *ELBO derivation*
- §7: SCC 4-term ↔ stage-2 sub-stage 정밀 대응 + *caveats*
- §8: *new section* — asymptotic capacity scaling (high-photon, low-contrast)
- §9: *new section* — optimal decoder bound (van Trees / Bayesian CR)
- §13: σ-coarseness *정량 trade-off* + information-preservation 정당화

Stage-document 영향 없음 (cross-references only).

---

*Cross-cutting 06 v1. 후속: [[07_omega_sigma_lift]]. TC-SP-4.1, 4.2, 4.3 의 elaboration (신규 code 없음). DPI / Fisher DPI / Cramér-Rao / Laughlin / Atick-Redlich 의 *full derivation* 추가. Free-energy principle 은 formal formula 와 함께 cited but not adopted. SCC parallel 은 형식 유사성만 기록. v0 (390 lines) → v1 (~1500 lines).*
