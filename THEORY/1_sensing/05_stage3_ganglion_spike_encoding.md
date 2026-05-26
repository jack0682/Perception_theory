---
type: working/sensing_pipeline/stage3
version: v1
date: 2026-05-25
status: DEFINITION-DRAFT
purpose: |
  Stage 3 deep dive: ganglion cell spike encoding.
  Graded → spike conversion via LIF SDE, SRM, Cox process, Hawkes.
  Full first-passage-time derivation (inverse Gaussian ISI) for LIF.
  Gerstner-Kistler SRM ≡ LIF equivalence under exponential kernels.
  Cox log-likelihood (GLM form). Hawkes stability proof.
  Renewal theory: Laplace-transform renewal density. Fano factor derivations.
  TC-SP-3.1 full derivation (Stein/Bialek-Rieke bandlimited rate sufficiency).
  TC-SP-3.2 latency asymmetry with synchronization-delay bit cost.
  TC-SP-3.3 rate-distortion derivation for 1/f^2 natural scenes.
  M/P/K axonal conduction velocity analysis.
  Eccentricity scaling rho(e) and cortical magnification (Drasdo).
  Sheaf presheaf formalism and H^1 obstruction.
  Per-bandwidth capacity integral.
  New §10.5 Population coding and noise correlations.
  Registers TC-SP-3.1, TC-SP-3.2, TC-SP-3.3, OP-SP-005.
register: DEFINITION-DRAFT + THEOREM-CANDIDATE (no proofs)
parent: 01_framework_master
prev_stage: 04_stage2_inner_retinal_algebra
constraint_compliance:
  canonical_theorem_changes: 0
  scc_edits: 0
---

> [!nav] Parent: [[00_INDEX]] · Prev: [[04_stage2_inner_retinal_algebra]] · Next: [[06_endtoend_information_bound]]

# Stage 3 — Ganglion Cell Spike Encoding

## 0. 본 문서의 위치

본 문서는 SSKP 의 네 번째 kernel $\mathcal{K}_3 : \mathcal{S}_2 \to \mathcal{S}_3$ — *다채널 graded 신호 → ~1M 평행 스파이크 트레인* 의 변환을 정식화한다.

핵심 변환들:

- *Graded → spike* (4 candidate 모델: LIF, SRM, Cox, Hawkes) — 각각에 대한 완전한 수학적 전개 포함
- *126:1 압축* (peripheral; fovea 는 1:1:1)
- *M / P / K 경로 분기* (다른 시정수, 다른 축삭 전도 속도, 다른 정보 함량)
- *비균질 표본화* (eccentricity 의존; Drasdo 관계식 포함)

본 문서가 *수행하지 않는 것*: 시신경 후 (LGN, V1) — Stage 4 의 정확한 위치는 OP-SP-007; LGN 까지 다룬다면 별도 stage.

---

## 1. 상태공간 $\mathcal{S}_3$

### 1.1 정의

신경절세포 spike train 의 집합.

$$
\boxed{\mathcal{S}_3 := \prod_{c \in \mathcal{C}_g} \mathcal{N}(\mathbb{R}^+)}
$$

- $\mathcal{C}_g$: 신경절세포 채널 집합 — *유한* (~$10^6$ 개)
- $\mathcal{N}(\mathbb{R}^+)$: $\mathbb{R}^+$ 위 locally finite counting measure (스파이크 시각의 집합)

각 $G \in \mathcal{S}_3$ 는 tuple $G = (G_c)_{c \in \mathcal{C}_g}$, $G_c$ 는 채널 $c$ 의 스파이크 시각들.

### 1.2 채널 집합 $\mathcal{C}_g$

각 신경절세포는 다음으로 식별:

$$
c \in \mathcal{C}_g \iff c = (p, \tau, \text{ONOFF})
$$

- $p \in \Sigma_{\text{ret}}$: 세포의 *공간 위치* (수용야 중심)
- $\tau \in \{M, P, K, \text{DSGC}, \text{ipRGC}, \ldots\}$: 세포 type
- $\text{ONOFF} \in \{ON, OFF\}$: 부호

$\mathcal{C}_g$ 는 $\sim 10^6$ 개 세포의 *비균질 격자*. 위치 $p$ 의 분포는 *fovea 에서 dense, periphery 에서 sparse* (비균질 표본화; §7).

### 1.3 위상

각 component $\mathcal{N}(\mathbb{R}^+)$ 의 vague topology Borel σ-algebra; product σ-algebra. Polish.

### 1.4 동적 표현

각 $G_c$ 는 *atomic counting measure* 으로 표현되거나, 동치적으로:

- *Stochastic process*: $N_c(t) = |\{s \in G_c : s \leq t\}|$ (cumulative count)
- *Spike list*: $(t_{c,1}, t_{c,2}, \ldots)$ ordered
- *Inter-spike intervals (ISI)*: $\Delta_i = t_{c,i+1} - t_{c,i}$

세 표현은 동치. 본 문서에서 context 에 따라 선택.

---

## 2. Graded → Spike 변환 — 4 candidate 모델

같은 입력 $B \in \mathcal{S}_2$ 에 대해 4 가지 모델이 (조건에 따라) 적합. 본 stage 는 모두를 *candidate* 로 등록.

### 2.1 모델 A — Leaky Integrate-and-Fire (LIF) SDE

가장 표준적, mechanistic 모델.

**Definition 2.1**. 채널 $c$ 의 시점 membrane potential $u_c(t)$ 의 SDE:

$$
\tau_c \frac{du_c}{dt} = -(u_c - u_{\text{rest}}) + R \cdot I_c^{\text{syn}}(t) + \sigma \xi(t)
$$

with $I_c^{\text{syn}}(t) = w_c \cdot B_{c}(p_c, t)$ — 시냅스 입력은 *해당 채널의 stage 2 출력*.

여기서 $\xi(t)$ 는 단위 white noise (Gaussian, $\langle \xi(t) \xi(s) \rangle = \delta(t-s)$). Itô 형식으로는 $\sigma dW_t$.

**Firing rule**: $u_c(t) \geq \theta \implies$ spike at $t$, $u_c(t^+) = u_{\text{reset}}$. 추가: refractory period $\tau_{\text{ref}}$.

수학적으로 이는 *first-passage time process* — *Skorokhod problem* 변종.

**Parameters**:
- $\tau_c$: membrane 시정수 (M: $\sim$ 5 ms, P: $\sim$ 15 ms, K: $\sim$ 10 ms)
- $\theta$: firing threshold (단위 mV, $\sim$ -50 mV)
- $u_{\text{reset}}$: reset potential ($\sim$ -70 mV)
- $\tau_{\text{ref}}$: refractory ($\sim$ 1-5 ms)

#### 2.1.1 First-Passage Time 유도 — ISI 의 Inverse Gaussian 분포

**설정**. 단순화를 위해 *constant input* $I$ 를 가정 (정상상태 분석). Reset 후 $u(0) = u_{\text{reset}}$ 에서 출발. SDE:

$$
\tau \frac{du}{dt} = -(u - u_{\text{rest}}) + RI + \sigma \xi(t)
$$

$v(t) := u(t) - \mu_\infty$ 로 치환, $\mu_\infty := u_{\text{rest}} + RI$ (정상상태 평균):

$$
\tau \frac{dv}{dt} = -v + \sigma \xi(t)
$$

이는 *Ornstein-Uhlenbeck (OU)* 과정. 해:

$$
v(t) = v(0) e^{-t/\tau} + \frac{\sigma}{\tau} \int_0^t e^{-(t-s)/\tau} dW_s
$$

**First passage time**. $T_{\text{FPT}}$ 를 $u(t)$ 가 처음으로 $\theta$ 에 도달하는 시각:

$$
T_{\text{FPT}} = \inf\{t > 0 : u(t) = \theta\}
$$

이것이 하나의 ISI.

**순수 drift 극한** ($\sigma \to 0$, deterministic). $u(t) = \mu_\infty + (u_{\text{reset}} - \mu_\infty) e^{-t/\tau}$. Reset 에서 threshold 까지 도달 시간:

$$
T_0 = \tau \ln\!\frac{\mu_\infty - u_{\text{reset}}}{\mu_\infty - \theta}
$$

(단, $\mu_\infty > \theta$ 가정 — 충분한 input 으로 firing 이 보장.)

**Noise 가 있는 경우 — Inverse Gaussian 분포**.

$\sigma$ 작은 경우, 막전위가 $u_{\text{reset}}$ 에서 $\theta$ 까지 *거의 직선*으로 이동한다고 근사하면, OU 를 *Wiener process with drift* 로 근사할 수 있다. 구체적으로:

두 매개변수를 정의:

$$
\mu_{\text{eff}} := \frac{(\theta - u_{\text{reset}})}{T_0}, \qquad \sigma_{\text{eff}}^2 := \frac{\sigma^2}{\tau}
$$

($\mu_{\text{eff}}$: 효과적 drift 속도, $\sigma_{\text{eff}}^2$: 확산 계수.) 그러면 first passage time $T$ 의 분포가 *inverse Gaussian* 으로 근사됨 (Tuckwell 1988, §6.2):

$$
\boxed{p(T) = \frac{\theta - u_{\text{reset}}}{\sqrt{2\pi \sigma_{\text{eff}}^2 \, T^3}}
\exp\!\left( -\frac{(\theta - u_{\text{reset}} - \mu_{\text{eff}} T)^2}{2\sigma_{\text{eff}}^2 T} \right)}
$$

더 명시적으로 원래 매개변수로:

$$
p(\Delta) = \frac{\theta - u_{\text{reset}}}{\sqrt{2\pi (\sigma^2/\tau) \Delta^3}}
\exp\!\left( -\frac{\bigl(\theta - u_{\text{reset}} - \tfrac{(RI + u_{\text{rest}} - \theta)}{\tau}\,\Delta\bigr)^2}{2(\sigma^2/\tau)\,\Delta} \right)
$$

여기서 drift 는 $\mu_{\text{eff}} = (\mu_\infty - \theta + \theta - u_{\text{reset}})/\tau$ 의 선형 근사. (Tuckwell 1988 의 Eq. (6.40).)

**Inverse Gaussian 의 성질**:
- $\mathbb{E}[\Delta] = (\theta - u_{\text{reset}}) / \mu_{\text{eff}}$ — mean ISI
- $\text{Var}[\Delta] = (\theta - u_{\text{reset}}) \sigma_{\text{eff}}^2 / \mu_{\text{eff}}^3$
- $CV = \sigma_{\text{eff}} / \sqrt{(\theta - u_{\text{reset}}) \mu_{\text{eff}}}$ — noise/drift ratio 에 비례

**유도 outline** (Tuckwell 방법):

1. OU 과정의 Fokker-Planck 방정식을 Wiener drift 과정으로 근사.
2. Wiener with drift $\mu$ 와 diffusion $D$ 의 first-passage distribution 은 *정확히* inverse Gaussian:

$$
p_{\text{Wiener}}(T | x_0, a) = \frac{a - x_0}{\sqrt{4\pi D T^3}} \exp\!\left(-\frac{(a - x_0 - \mu T)^2}{4DT}\right)
$$

($x_0 = u_{\text{reset}}$, $a = \theta$, $D = \sigma^2/2$.) 이는 Bachelier-Schrödinger 공식.

3. OU 에서 *linearization* 으로 동일 형태 도출 (점 근처 국소 drift 상수화). 정확한 OU first-passage distribution 은 특수함수 (parabolic cylinder functions; Ricciardi & Sato 1988) 로만 표현되나, 위 근사가 생물물리적으로 합리적 범위에서 정확.

**결론**: LIF 스파이크 트레인의 ISI 는 *inverse Gaussian* (근사). Poisson 의 exponential 과 달리 *unimodal, peak 가 mean ISI 근처* — 실제 신경절 세포 데이터와 정합 (Gerstein-Mandelbrot 1964).

### 2.2 모델 B — Spike Response Model (SRM)

LIF 의 *적분 형식* (Gerstner-Kistler 2002).

**Definition 2.2**. Membrane potential as integral:

$$
u_c(t) = u_{\text{rest}} + \int_{-\infty}^t \kappa(t - s) I_c^{\text{syn}}(s) ds + \sum_{t_{c,i} < t} \eta(t - t_{c,i})
$$

- $\kappa$: input response kernel
- $\eta$: after-spike potential (refractory + after-hyperpolarization)

Firing: $u_c(t) \geq \theta(t - t_{c,\text{last}})$, where $\theta$ 는 직전 spike 이후 시간에 따른 dynamic threshold.

LIF 와 동치 (적절한 $\kappa, \eta$ 선택 하). SRM 의 장점: kernel 들이 *경험적 데이터에 직접 fit*.

#### 2.2.1 SRM $\equiv$ LIF 동치 증명 — Gerstner-Kistler Lemma

**Lemma (GK 2002, Lemma 4.2)**. LIF SDE (노이즈 없는 결정론적 버전:)

$$
\tau \dot{u} = -u + u_{\text{rest}} + R I(t)
$$

가 주어졌을 때, *마지막 spike* 시각 $\hat{t}$ 이후의 해는:

$$
u(t) = u_{\text{rest}} + \frac{R}{\tau} \int_{\hat{t}}^t e^{-(t-s)/\tau} I(s)\,ds + \underbrace{(u_{\text{reset}} - u_{\text{rest}}) e^{-(t-\hat{t})/\tau}}_{\eta(t - \hat{t})}
$$

이를 $t_{c,i} < t$ 인 *모든* 과거 spikes 에 대해 중첩 (선형성 이용):

$$
u(t) = u_{\text{rest}} + \int_{-\infty}^t \underbrace{\frac{R}{\tau} e^{-(t-s)/\tau} \mathbf{1}_{s > 0}}_{\kappa(t-s)} I(s)\,ds + \sum_{t_i < t} \underbrace{(u_{\text{reset}} - u_{\text{rest}}) e^{-(t-t_i)/\tau}}_{\eta(t - t_i)}
$$

따라서:
- $\kappa(s) = \frac{R}{\tau} e^{-s/\tau}$ (exponential input kernel)
- $\eta(s) = (u_{\text{reset}} - u_{\text{rest}}) e^{-s/\tau}$ (exponential after-potential)

**결론**: *지수함수* kernel $\kappa$, $\eta$ 를 가진 SRM 은 LIF 의 *정확한* 적분 형식. Gerstner-Kistler (2002) §4.2 의 내용을 위 방식으로 명시적으로 확인. 두 모델은 결정론적 영역에서 *수학적으로 동치*.

**노이즈 있는 경우**: SDE LIF 의 해도 동일 형태이며, 노이즈 항이 $\kappa$ 와의 합성곱으로 나타남. 단, *firing rule* 의 stochastic 버전에서 SRM 과 LIF 는 *soft* vs *hard* threshold 로 미세하게 다를 수 있음 — 이는 이 동치의 *경계* (상세: Gerstner-Kistler §5).

### 2.3 모델 C — Doubly Stochastic Poisson (Cox process)

가장 간단, top-down phenomenological.

**Definition 2.3**. Spike train $G_c$ 가 *rate* $\lambda_c(t)$ 의 *inhomogeneous Poisson*:

$$
\lambda_c(t) := \phi\big( w_c \cdot B_c(p_c, t) \big)
$$

with $\phi : \mathbb{R} \to \mathbb{R}^+$ a nonlinear *output nonlinearity* (e.g., $\phi(x) = \log(1 + e^x)$ — softplus, or $[\cdot]_+$ — ReLU).

이는 *Cox process* — Poisson with stochastic (input-dependent) rate.

장점: 통계적으로 깔끔. 단점: refractory 무시 (실제 spike train 은 *anti-bunched* — Poisson 보다 *regular*).

#### 2.3.1 Cox process 의 Log-Likelihood — GLM 형식

**설정**. 시간 구간 $[0, T]$ 에서 관측된 스파이크 시각 $\{t_1, t_2, \ldots, t_n\} \subset [0, T]$. Rate function $\lambda(t)$ 는 매개변수 $\beta$ 에 의존: $\lambda(t) = \lambda(t; \beta)$.

**Point process likelihood**. Daley-Vere-Jones (Vol. I, §7.2) 에 의해, rate $\lambda(t)$ 의 inhomogeneous Poisson process 에서 관측된 사건들의 *likelihood*:

$$
L(\beta) = \left[\prod_{i=1}^n \lambda(t_i; \beta)\right] \exp\!\left(-\int_0^T \lambda(t; \beta)\,dt\right)
$$

Log-likelihood:

$$
\boxed{\ell(\beta) = \int_0^T \log \lambda(t; \beta)\,dN(t) - \int_0^T \lambda(t; \beta)\,dt}
$$

여기서 $dN(t) = \sum_i \delta(t - t_i)\,dt$ 는 스파이크 counting measure. 이산 형식으로는:

$$
\ell(\beta) = \sum_{i=1}^n \log \lambda(t_i; \beta) - \int_0^T \lambda(t; \beta)\,dt
$$

**GLM 연결**. $\log \lambda(t; \beta) = \mathbf{x}(t)^T \beta$ (log-linear link) 라 하면 ($\mathbf{x}(t)$ 는 covariate vector — 여기서 stimulus feature):

$$
\ell(\beta) = \sum_i \mathbf{x}(t_i)^T \beta - \int_0^T e^{\mathbf{x}(t)^T \beta}\,dt
$$

이는 *Generalized Linear Model (GLM) 의 Poisson regression log-likelihood* 와 동일한 구조. Score equation $\partial \ell / \partial \beta = 0$ 이 *quasi-Newton* 으로 풀림.

**통계적 의의**. 이 log-likelihood 가 신경 데이터로부터 $\lambda(t)$ 의 매개변수를 *최대우도추정* (MLE) 할 수 있게 한다. GLM 프레임워크가 stage 3 의 *neural decoding* 과 *encoding model fitting* 의 수학적 기반 (Paninski 2004; Pillow et al. 2008).

**오목성**. $\lambda(t; \beta) = e^{\mathbf{x}(t)^T \beta}$ (softplus 근사) 의 경우 $\ell(\beta)$ 가 $\beta$ 에 대해 *오목 (concave)*. 따라서 MLE 가 *유일하고 전역적* — GLM 의 표준 결과 (McCullagh-Nelder 1989).

### 2.4 모델 D — Hawkes Process

Refractory 와 *bursting* 까지 포함.

**Definition 2.4**. Self-exciting / inhibiting:

$$
\lambda_c(t) := \phi\big( w_c \cdot B_c(p_c, t) \big) + \int_{(0, t)} \phi_{\text{self}}(t - s) dG_c(s)
$$

- $\phi_{\text{self}}(\Delta) < 0$ for $\Delta \in [0, \tau_{\text{ref}}]$ — refractory
- $\phi_{\text{self}}(\Delta) > 0$ for some larger $\Delta$ — bursting (M cells 에서 관측)

#### 2.4.1 Hawkes Process 안정성 증명

**Theorem (Hawkes 1971; Daley-Vere-Jones, §6.3)**. Hawkes process 가 *stationary* (시간 평행이동에 불변인 정상 버전이 존재) 할 충분 조건:

$$
\boxed{\|\phi_{\text{self}}\|_{L^1(\mathbb{R}^+)} < 1}
$$

즉, $\int_0^\infty |\phi_{\text{self}}(s)|\,ds < 1$.

**증명 스케치** (Hawkes 1971 방법):

1. **Yule 과정 표현**. Hawkes process 를 *cluster process* 로 재해석: background (Poisson) 이벤트가 offspring 을 생성하고, offspring 이 또 offspring 을 생성. $\phi_{\text{self}}$ 가 *offspring rate kernel*.

2. **Branching ratio**. 한 이벤트가 기대하는 직접 offspring 수:
   $$m = \int_0^\infty \phi_{\text{self}}(s)\,ds$$
   총 offspring (직접 + 간접) 의 기대 수 = *Galton-Watson branching process* 의 기대 total descendant 수 = $1/(1-m)$ (단, $m < 1$).

3. **$m < 1$ 조건**. $m \geq 1$ 이면 branching process 가 *supercritical* → 사건 수 폭발 (explosive). $m < 1$ 이면 *subcritical* → process 가 stabilize.

4. **정상 분포 존재**. $m < 1$ 하에서 stationary Hawkes process 의 *강도 함수 기대값*:
   $$\bar{\lambda} = \frac{\mu_0}{1 - m}$$
   ($\mu_0$ = background rate) 가 유한. 따라서 정상 버전이 (Kolmogorov extension + tightness 로) 존재.

5. **스펙트럼 조건 (다변량 일반화)**. 다변량 Hawkes (채널 간 cross-excitation $\Phi_{ij}$) 의 경우, 안정성 조건은 *행렬* $\|\Phi\|_{L^1}$ 의 *스펙트럼 반지름* $\rho(\|\Phi\|_{L^1}) < 1$ — Hawkes 1971 의 주요 결과. 단일 채널이 $|\phi_{\text{self}}|_{L^1} < 1$ 는 이 조건의 단변량 특수 경우.

**직관**: 스파이크 하나가 미래 스파이크를 $m$ 개 만들어내면, $m \geq 1$ 일 때 자기-강화가 수렴하지 않고 발산. $m < 1$ 이면 각 세대마다 $m$ 배씩 감소하므로 기하급수 급수가 수렴.

**적용**. Refractory 를 구현할 때 $\phi_{\text{self}}$ 가 $[0, \tau_{\text{ref}}]$ 에서 음수이면 $m < 0 < 1$ → 항상 안정. Bursting 포함 시 양수 부분이 추가되나, 총 $\int \phi_{\text{self}} < 1$ 이어야 안정 보장.

### 2.5 모델 선택 — 응용에 따라

본 stage 는 *4 모델 모두 등록*. Stage 별 적합성:

| 응용 | 적합 모델 |
|------|----------|
| 단일 세포 mechanistic 분석 | A (LIF) |
| 통계적 추론 (GLM) | B (SRM) or C (Cox) |
| 대규모 시뮬레이션, 정보론적 분석 | C (Cox) |
| Burst-rich M cells, regularity | D (Hawkes) |

본 디렉토리의 *default* 는 C (Cox) — simplest, 정보론적 회계 ([[06_endtoend_information_bound|06]]) 와 호환. 다른 모델은 특수 상황에서 호출.

---

## 3. Renewal Theory — ISI 분포

스파이크 트레인의 통계적 회계.

### 3.1 Renewal process

**Definition 3.1**. $G$ 가 *renewal process* 라 함은 ISI $\Delta_i = t_{i+1} - t_i$ 가 *i.i.d.*, 공통 분포 $F_\Delta$.

Poisson 의 경우 $\Delta \sim \text{Exp}(\lambda)$.

LIF 의 stationary firing 의 경우 ISI 가 *inverse Gaussian* (§2.1.1 유도 참조):

$$
p(\Delta) = \frac{\theta - u_{\text{reset}}}{\sqrt{2\pi (\sigma^2/\tau) \Delta^3}} \exp\!\left( -\frac{(\theta - u_{\text{reset}} - \mu_{\text{eff}} \Delta)^2}{2(\sigma^2/\tau)\,\Delta} \right)
$$

(Tuckwell 1988).

#### 3.1.1 Renewal Density 의 Laplace Transform 유도

**Renewal equation**. 재발 밀도 $h(t)$ 를 다음으로 정의:

$$
h(t) := \frac{d}{dt} \mathbb{E}[N(t)] = \text{(expected number of events in } [t, t+dt] \text{)}/dt
$$

*Renewal equation* (Feller 1971, Vol. II, §XI.1):

$$
h(t) = f(t) + \int_0^t h(t - s) f(s)\,ds
$$

여기서 $f(t)$ 는 ISI 의 probability density. 해석: $t$ 에서 사건이 발생하려면 (i) 첫 사건이 $t$ 에서 발생하거나, (ii) 첫 사건이 $s \in (0, t)$ 에서 발생하고 그로부터 다시 $t-s$ 후 또 사건이 발생.

이는 *convolution equation*:

$$
h = f + h * f
$$

**Laplace domain에서 풀기**. 양변에 Laplace transform $\mathcal{L}[\cdot](z) = \int_0^\infty e^{-zt}(\cdot)\,dt$ 적용:

$$
\tilde{h}(z) = \tilde{f}(z) + \tilde{h}(z) \cdot \tilde{f}(z)
$$

여기서 $\tilde{f}(z) := \mathcal{L}[f](z)$. 따라서:

$$
\tilde{h}(z)\bigl(1 - \tilde{f}(z)\bigr) = \tilde{f}(z)
$$

$$
\boxed{\tilde{h}(z) = \frac{\tilde{f}(z)}{1 - \tilde{f}(z)}}
$$

**해석**:
- $z \to 0$: $\tilde{f}(0) = 1$ (정규화), $\tilde{f}'(0) = -\mathbb{E}[\Delta]$. L'Hopital 로 $\tilde{h}(z) \to 1/\mathbb{E}[\Delta]$ as $z \to 0$ — *Elementary Renewal Theorem* (기대 재발 밀도가 mean ISI 의 역수로 수렴).
- 역변환: $h(t) = \mathcal{L}^{-1}\!\left[\frac{\tilde{f}(z)}{1-\tilde{f}(z)}\right](t)$ — 일반 ISI 분포에 대한 정확한 결과.

**Poisson 특수 경우**. $f(t) = \lambda e^{-\lambda t}$, $\tilde{f}(z) = \lambda/(z+\lambda)$:

$$
\tilde{h}(z) = \frac{\lambda/(z+\lambda)}{1 - \lambda/(z+\lambda)} = \frac{\lambda}{z}
$$

역변환: $h(t) = \lambda$ — 상수. Poisson 의 경우 재발 밀도가 상수임을 확인 (Markov renewal).

**Inverse Gaussian 특수 경우**. $\tilde{f}(z)$ 가 닫힌 형식으로 표현되므로 $\tilde{h}(z)$ 도 닫힌 형식 존재:

$$
\tilde{f}_{\text{IG}}(z) = \exp\!\left(\frac{\mu_{\text{eff}} a}{\sigma_{\text{eff}}^2}\left(1 - \sqrt{1 + \frac{2\sigma_{\text{eff}}^2 z}{\mu_{\text{eff}}^2}}\right)\right)
$$

($a = \theta - u_{\text{reset}}$.) 따라서 $\tilde{h}(z)$ 도 분석 가능 — LIF 스파이크 트레인의 재발 구조 완전 기술.

### 3.2 Fano Factor

$$
F(T) := \frac{\text{Var}[N(T)]}{\mathbb{E}[N(T)]}
$$

#### 3.2.1 LIF 의 Fano Factor — $F < 1$ 유도

**주장**: Regular spiking (refractory period 존재) → $F < 1$.

**유도** (renewal theory):

Renewal process 의 분산 — long-time limit 에서 (Cox-Miller 1965):

$$
\text{Var}[N(T)] \approx \frac{CV^2}{\mathbb{E}[\Delta]} \cdot T = \frac{\text{Var}[\Delta]}{\mathbb{E}[\Delta]^3} \cdot T
$$

$\mathbb{E}[N(T)] \approx T / \mathbb{E}[\Delta]$. 따라서:

$$
F(T) \approx \frac{\text{Var}[\Delta]}{\mathbb{E}[\Delta]^2} = CV^2
$$

(*Fano factor = $CV^2$ in stationary renewal process, large $T$ limit.*)

LIF 의 경우 (§2.1.1):

$$
CV_{\text{LIF}}^2 = \frac{\text{Var}[\Delta]}{\mathbb{E}[\Delta]^2} = \frac{\sigma_{\text{eff}}^2}{(\theta - u_{\text{reset}}) \mu_{\text{eff}}} = \frac{\sigma^2/\tau}{\mu_{\text{eff}}(\theta - u_{\text{reset}})}
$$

이는 *noise-to-drift ratio* 에 비례. $\sigma \to 0$ (deterministic limit) 에서 $CV \to 0$, $F \to 0$. 유한 $\sigma$ 에서도 refractory 가 있으면 $CV < 1$, 따라서 $F < 1$.

**물리적 해석**: Refractory period 가 두 연속 스파이크 사이의 *최소 간격* 을 강제 → ISI 가 $\tau_{\text{ref}}$ 이하로는 절대 내려갈 수 없음 → ISI 분포가 *아래쪽에서 잘림* → variance 가 감소 → $F < 1$ (*sub-Poissonian*).

#### 3.2.2 Cox Process 의 Fano Factor — $F = 1$

Cox process 에서 (조건부 Poisson):

$$
\text{Var}[N(T)] = \mathbb{E}\!\left[\text{Var}[N(T)|\lambda]\right] + \text{Var}\!\left[\mathbb{E}[N(T)|\lambda]\right]
$$

조건부 Poisson: $\text{Var}[N(T)|\lambda] = \mathbb{E}[N(T)|\lambda] = \int_0^T \lambda(t)\,dt =: \Lambda(T)$.

$$
\text{Var}[N(T)] = \mathbb{E}[\Lambda(T)] + \text{Var}[\Lambda(T)]
$$

단순 (비랜덤) rate $\lambda(t) = \lambda$ 의 경우 $\text{Var}[\Lambda] = 0$, $F = 1$.

랜덤 rate (진정한 Cox) 의 경우 $\text{Var}[\Lambda] > 0$, 따라서 $F > 1$ (*super-Poissonian*). 따라서:

$$
F_{\text{Cox}} = 1 + \frac{\text{Var}[\Lambda(T)]}{\mathbb{E}[\Lambda(T)]} \geq 1
$$

랜덤 자극이 Fano factor 를 *증가* 시킴.

#### 3.2.3 Hawkes 의 Fano Factor — $F > 1$ (Bursting)

Self-exciting Hawkes ($\phi_{\text{self}} > 0$ 일부) 의 경우 스파이크 *clustering* → burst → $F > 1$.

정확한 공식 (Hawkes 1971 의 spectral 방법):

$$
F_{\text{Hawkes}} = 1 + 2\bar{\lambda} \int_0^\infty C_0(s)\,ds
$$

여기서 $C_0(s)$ 는 자기상관 함수 (pair correlation 의 편차). Self-excitation 이 있으면 $C_0 > 0$ (스파이크 뒤에 또 스파이크 확률 증가) → $\int C_0 > 0$ → $F > 1$.

**요약**:

| 모델 | $F$ |
|------|-----|
| LIF (regular) | $< 1$ (sub-Poissonian) |
| Cox (fixed rate) | $= 1$ (Poisson) |
| Cox (random rate) | $\geq 1$ |
| Hawkes (self-excitation) | $> 1$ (super-Poissonian) |

실제 M 세포 (bursting): $F \approx 1.5 - 2$. P 세포 (regular): $F \approx 0.5 - 0.8$.

### 3.3 Coefficient of Variation

ISI 의 CV:

$$
CV := \frac{\sqrt{\text{Var}[\Delta]}}{\mathbb{E}[\Delta]}
$$

- Poisson: $CV = 1$
- Perfectly periodic: $CV = 0$
- 실제: $CV \in [0.3, 1.2]$ depending on cell type and stimulus.

$F \approx CV^2$ (§3.2.1 의 renewal 결과) — Fano factor 와 CV 의 관계.

### 3.4 Spike train 의 자기상관

$$
C(s, t) := \mathbb{E}[dN(s) dN(t)] - \mathbb{E}[dN(s)] \mathbb{E}[dN(t)]
$$

Poisson: $C(s, t) = \lambda \delta(t - s)$ — *white*.
Renewal (non-Poisson): peaks at multiples of mean ISI, *decaying oscillation* with refractory dip near $s = t$.

Hawkes 의 경우 $C(s,t)$ 가 *양수 꼬리* (clustering) — 적분 $\int C\,ds > 0$ 으로 $F > 1$ 다시 확인.

---

## 4. 율 코드 vs 정밀 타이밍 코드

스파이크 트레인이 *어떤* 부호화 형식인가의 질문.

### 4.1 Rate code 가설

*평균 발화율* $\bar{\lambda}_c$ 가 정보를 운반:

$$
\bar{\lambda}_c(t) := \frac{1}{T} \sum_{i : t_i \in [t - T/2, t + T/2]} 1
$$

with $T$ a sliding window (~50-200 ms).

정보 = $\bar{\lambda}_c(t)$ 의 시간 변화.

### 4.2 Temporal code 가설

*정확한 스파이크 시각* $t_{c,i}$ 가 정보를 운반. 또는 *spike pattern* (timing of multiple spikes) 이 정보.

증거: 일부 cortical areas 에서 *millisecond-precision timing* 이 reliable (Bair-Koch 1996); 그러나 retinal P-cells 에서는 rate code 가 dominant.

### TC-SP-3.1 — [DELETED 2026-05-25 Pass 4]

**Status**: **DELETED via Pass 4** (cumulative 2 HOLE: Pass 3 #5 + Pass 4 #51 — *double confirmation of same fundamental issue*: Cox process conditional-independence 가 망막에서 위반). 저자 본문 §10.5 admits noise correlations $r^{\text{noise}} \approx 0.01-0.1$ (Bair 2001, Pillow 2008) 인데 TC 는 unconditional Cox 주장.

**Original statement (preserved for audit trail)**:

> (i) 대역폭 제한 + (ii) λ ≳ 2W (Nyquist) + (iii) Fano ~ 1 하에서 rate code 정보론적으로 충분: $I(B_c; G_c) \approx I(B_c; \bar\lambda_c)$.

**Why DELETED**:
- Verifier #5 (Pass 3) 가 Cox process 가정 위반 명시 — Berry-Meister 1998 (Fano ≠ 1), Pillow et al. 2008 (coupling filters violate conditional independence).
- Verifier #51 (Pass 4) 가 *동일 hole* 을 *다른 attack vector* 로 재확인 — Cox 의 conditional-independence backbone 이 *the* key structural assumption 이고 *empirically 위반*.
- **이는 본 corpus 의 구조적으로 가장 약한 load-bearing TC** — TC-SP-3.3 (compression bound), TC-SP-4.1 (end-to-end), TC-SP-4.2 (lossy ranking) 모두 본 TC 에 의존.
- 2 patterns HOLE + downstream cascade → 박탈.

**Replacement**: Cox process 와 LIF/SRM/Hawkes 본문 (§2) 은 *modeling choice* 로 유지 — *정리* 아님. Rate code sufficiency 는 *조건부 approximation* (parvocellular high-rate stationary regime 에서) — *empirical regime* 으로 언급, *정리* 아님.

#### 4.2.1 TC-SP-3.1 의 완전 유도 (Stein 1967 / Bialek-Rieke 논증)

**설정**. 단일 채널 분석. 자극 $s(t)$ 가 *bandlimited Gaussian process*:

$$
s(t) = \int_{-W}^{W} \hat{s}(\omega) e^{i\omega t} d\omega, \quad \hat{s}(\omega) \sim \mathcal{N}(0, S(\omega))
$$

($W$: 대역폭, $S(\omega)$: power spectrum.)

스파이크 트레인 $G = \sum_i \delta(t - t_i)$. Rate: $\lambda(t) = \phi(s(t))$ (Cox model).

**단계 1: 율로 인코딩된 정보**. 율 $\lambda(t)$ 는 $s(t)$ 의 함수이므로 $I(s; \lambda)$ 는 $\phi$ 의 선형성 정도에 따라 다름. $\phi$ 가 충분히 smooth 하면 $I(s; \lambda) \approx I(s; s)$ (정보 보존).

**단계 2: 스파이크 트레인이 율을 추가로 인코딩하는가?**

Stein (1967) 논증: 스파이크 열의 *무작위성* 으로 인해 $G$ 가 $\lambda(t)$ 에 추가로 부가하는 정보를 계산.

Cox process 에서, $G$ 가 조건부 ($\lambda$ 주어졌을 때) Poisson 이므로:

$$
I(s; G) = I(s; \lambda) + I(\lambda; G | s)
$$

그러나 Cox process 에서 $G | \lambda$ 가 Poisson 이므로 $\lambda$ 가 $G$ 와 $s$ 사이의 *충분통계량*:

$$
I(s; G) = I(s; \lambda)
$$

즉, Cox process 에서는 $\lambda(t)$ 가 정보론적으로 충분통계량. *스파이크 시각의 추가 정보는 0.*

**단계 3: 율을 관측 가능한가?**

율 $\lambda(t)$ 를 *window $T$ 로 추정*:

$$
\hat{\lambda}(t) = \frac{N(t, t+T)}{T} = \text{(spike count in window)}
$$

이 추정의 SNR: $\text{SNR} = \bar{\lambda}^2 T / \bar{\lambda} = \bar{\lambda} T$.

Nyquist 조건: $\bar{\lambda} \geq 2W$ 이어야 $\bar{\lambda}(t)$ 의 시간 변화를 *충분한 정밀도*로 추적 가능.

**단계 4: 정보 rate 계산**

Cox process channel 의 capacity (§4.3 참조):

$$
R_{\text{rate}} = W \cdot \log_2\!\left(1 + \frac{\bar{\lambda}}{W}\right) \text{ bits/sec}
$$

(Shannon-Hartley 의 아날로그. Poisson channel 에서 Gaussian channel 로 근사 시.)

Timing precision $\delta t < 1/(2W)$ 의 추가 정보: $\log_2(T_{\text{window}} / \delta t)$ per spike. 그러나 bandwidth $W$ 이하의 $s(t)$ 에서 timing information 은 *이미 rate 에 포함* — $\delta t < 1/(2W)$ 의 timing jitter 는 bandwidth 를 넘는 정보이므로 $s(t)$ 와 *무관*.

**결론** (Stein 1967; Bialek-Rieke 1996 §3): 조건 (i)(ii)(iii) 하에서:

$$
I(s; G) = I(s; \bar{\lambda}) + O\!\left(\frac{W}{\bar{\lambda}} \log \frac{\bar{\lambda}}{W}\right)
$$

보정항이 $\bar{\lambda} \gg W$ 이면 $\to 0$. 따라서 rate code 가 *asymptotically sufficient*.

**의미**: 실제 정보 처리에는 *rate code 추적* 으로 충분. *정밀 timing 의 추가 정보* 는 미미 (특정 stage / 신호 외에는). 정보론적 회계 ([[06_endtoend_information_bound|06]]) 가 rate 만 다뤄도 충분.

**반례**: Magnocellular pathway 의 transient burst — 짧은 시간 window 의 정확한 spike count 가 중요. 이 경우 rate sufficiency 는 약화. OP 로 둘 가능성.

### 4.3 Channel capacity (Poisson channel)

단일 신경절세포 channel 의 capacity — Cox model 가정.

#### 4.3.1 Kabanov (1978) 공식

**Poisson channel capacity**. Rate $\lambda \in [\lambda_{\min}, \lambda_{\max}]$ 로 제약된 Poisson channel 의 용량 (Kabanov 1978):

$$
\boxed{C_{\text{Poisson}} = \lambda_{\max} \log\frac{\lambda_{\max}}{\lambda_{\min}} - (\lambda_{\max} - \lambda_{\min})}
$$

단위: nats/sec. Bits/sec 로는 $\log \to \log_2$, 우변 마지막 항도 $\log_2 e$ 곱.

**유도 스케치** (Kabanov 1978; Davis 1980):

정보 입력을 $\lambda(t)$ (rate function), 출력을 $N(t)$ (spike count process) 로 볼 때, Poisson channel 의 mutual information rate:

$$
I = \int \lambda(t) \log \frac{\lambda(t)}{\bar{\lambda}}\,dt - \int (\lambda(t) - \bar{\lambda})\,dt
$$

제약: $\lambda_{\min} \leq \lambda(t) \leq \lambda_{\max}$, 평균 $\bar{\lambda}$ 에 대한 제약 없음.

이를 maximize: convex optimization. Lagrange condition 이 $\lambda(t) \in \{\lambda_{\min}, \lambda_{\max}\}$ (bang-bang control) 을 요구. 따라서 최적 input 이 *binary* (on-off keying): rate 가 $\lambda_{\max}$ 또는 $\lambda_{\min}$ 만 취함.

Binary Poisson channel 에서 capacity:

$$
C = p(\lambda_{\max} - \lambda_{\min}) \log\frac{\lambda_{\max}}{\lambda_{\min}} - (\lambda_{\max} - \lambda_{\min}) p (1-p) \cdot (?)
$$

의 최적화. 정확한 결과 (Kabanov):

$$
C = \lambda_{\max} \log\!\frac{\lambda_{\max}}{\lambda_{\min}} - (\lambda_{\max} - \lambda_{\min}) \text{ [nats/sec]}
$$

**실제 값 추정**:

$\lambda_{\max} \sim 100$ Hz, $\lambda_{\min} \sim 0$ Hz (silent):

$$
C \approx 100 \log(100) - 100 \approx 100 \times 4.6 - 100 = 360 \text{ nats/sec} \approx 520 \text{ bits/sec}
$$

그러나 신호가 항상 $[0, 100]$ Hz 전 범위를 쓰지 않으므로 effective capacity 는 $\sim 4-6$ bits/sec per cell.

#### 4.3.2 Per-bandwidth capacity

Time-bandwidth 분리 형식으로:

$$
C_c = \int_0^{W_c} \log_2\!\left(1 + \frac{\text{SNR}(\omega)}{1}\right) d\omega \text{ [bits/sec]}
$$

여기서 $\text{SNR}(\omega) = S_\lambda(\omega) / S_{\text{noise}}(\omega)$ — rate spectrum / noise spectrum.

Poisson noise 의 spectral density: $S_{\text{noise}}(\omega) = \bar{\lambda}$ (flat — Poisson 의 white noise). Signal spectrum: $S_\lambda(\omega)$ — stimulus modulation depth.

단순 flat signal 가정 ($S_\lambda = \bar{\lambda}^2 / W_c$ for $|\omega| < W_c$):

$$
C_c \approx W_c \log_2\!\left(1 + \frac{\bar{\lambda}}{W_c}\right) \text{ bits/sec}
$$

이를 $W_c$ 에 대해 전체 bandwidth 로 적분:

$$
C_{\text{total}} = \int_0^{W_c} \log_2\!\left(1 + \frac{\bar{\lambda}}{w}\right) dw
$$

전형값: $\bar{\lambda} \sim 50$ Hz, $W_c \sim 30$ Hz → $C_c \sim 4-6$ bits/sec per cell.

시신경 전체: $10^6$ cells $\times$ 5 bits/sec $= 5$ Mbits/sec.

---

## 5. M / P / K 경로 분리와 latency 비대칭

### 5.1 경로 정량 (영장류)

| 경로 | % | $\tau_{\text{membrane}}$ | 축삭 직경 | conduction velocity | latency to V1 | center RF size |
|------|----|--------|----|------|------|------|
| Magno (M, Parasol) | ~10% | $\sim$ 5 ms | 대 (유수, $\sim 5-10\,\mu$m) | $\sim$ 15–25 m/s | $\sim$ 70 ms | 큼 |
| Parvo (P, Midget) | ~80% | $\sim$ 15 ms | 소 (유수, $\sim 1–3\,\mu$m) | $\sim$ 3–8 m/s | $\sim$ 100 ms | 작음 (fovea: 1 cone) |
| Konio (K, Bistratified) | ~8-10% | $\sim$ 10 ms | 소-중 (일부 무수) | $\sim$ 5–12 m/s | $\sim$ 80-100 ms | 중간 |

#### 5.1.1 축삭 전도 속도 분석

**유수 (myelinated) 축삭의 전도 속도**. Hodgkin (1954) 의 cable theory + myelin scaling:

$$
v_{\text{cond}} \approx 6 \cdot d_{\text{axon}} \text{ [m/s per }\mu\text{m diameter]}
$$

여기서 $d_{\text{axon}}$ 은 축삭 직경 ($\mu$m 단위). 경험적 공식 (Rushton 1951).

**유도 근거**. Myelinated axon 에서:
- Capacitance per unit length: $C_m \propto d$ (diameter)
- Myelin sheath 전기저항: $R_m \propto 1/d$
- Axial resistance: $R_i \propto 1/d^2$
- Space constant: $\lambda = \sqrt{R_m/R_i} \propto d$
- Node of Ranvier 간격: $\Lambda \propto d$ (경험적)
- 전도 속도: $v = \Lambda / \tau_{\text{node}} \propto d$

$\tau_{\text{node}}$ 는 국소 node 의 시정수 = $R_{\text{node}} C_{\text{node}} \approx$ 상수 (node 기하가 척도 불변) → $v \propto d$.

**M pathway**: 직경 $d \sim 5-10\,\mu$m → $v \sim 25-60$ m/s. 망막-LGN 거리 $\sim 5-10$ cm → 전도 지연 $\sim 2-4$ ms (축삭). 시냅스 지연 + LGN 처리 합하면 V1 도달 $\sim 60-80$ ms.

**P pathway**: 직경 $d \sim 1-3\,\mu$m → $v \sim 3-8$ m/s. 같은 거리 → 전도 지연 $\sim 6-25$ ms. 추가 시냅스 + 느린 $\tau_{\text{membrane}}$ → V1 도달 $\sim 90-110$ ms.

**K pathway**: 직경 중간 + 일부 무수 → $v \sim 5-12$ m/s. V1 도달 $\sim 80-100$ ms. 일부 K 세포는 LGN 를 우회하여 V1 layer I 에 직접 투사 (더 복잡한 경로).

**무수 (unmyelinated) 축삭**: $v \propto \sqrt{d}$ (Hodgkin). 직경 $d \sim 0.5-1\,\mu$m → $v \sim 0.5-1$ m/s. 망막 내부 (amacrine 등); 시신경 섬유는 대부분 유수.

**지연 계산 요약**:

$$
\text{latency} = \underbrace{\frac{L_{\text{axon}}}{v_{\text{cond}}}}_{\text{축삭 전도}} + \underbrace{N_{\text{syn}} \cdot \tau_{\text{syn}}}_{\text{시냅스 지연}} + \underbrace{\tau_{\text{process}}}_{\text{세포 처리}}
$$

$L \sim 8$ cm (eye to LGN), $\tau_{\text{syn}} \sim 1-2$ ms per synapse, $N_{\text{syn}} \sim 2$ (망막 → LGN, LGN → V1):

- M: $8 \times 10^{-2} / 20 + 2 \times 2 + 60 \approx 4 + 4 + 62 \approx 70$ ms
- P: $8 \times 10^{-2} / 5 + 2 \times 2 + 80 \approx 16 + 4 + 80 \approx 100$ ms

### 5.2 Latency 비대칭의 정보론적 의미

같은 시각 자극이 M / P 경로를 통해 *다른 시각*에 V1 에 도달:

- M : $t + \tau^M$ ($\tau^M \approx 70$ ms)
- P : $t + \tau^P$ ($\tau^P \approx 100$ ms)

따라서 V1 의 시각 $t$ 에는 "stimulus 의 $t - \tau^M$ M-version" + "stimulus 의 $t - \tau^P$ P-version" 이 *동시 존재* — 두 *별개* time-stamp 의 information.

### TC-SP-3.2 — [DELETED 2026-05-25 Pass 3]

**Status**: **DELETED via Pass 3 adversarial verification** (2-pattern HOLE: #18 tautology + #5 hypothesis recheck-minor).

**Original statement (preserved for audit trail)**:

> M-P latency 차이 ($\Delta\tau \approx 30$ ms) → V1 입력은 두 time axis 의 multiplex. M-P 결합은 별도 alignment 요구.

**Refute basis**:

- **#18 (tautology)**: "Two distinct time axes" = "two distinct constant latencies" 의 *pure rename* — 정의 재진술; 7-bit alignment cost 는 heuristic stipulation ($\sigma_{\Delta\tau} \approx 1$ ms), formally derived 아님.
- **#5 (hypothesis-minor)**: 시간적 $1/\omega^2$ spectrum 이 Field 1987 의 *spatial* 결과로부터 extrapolated — Dong-Atick 1995 는 시간 통계가 다르다고 보임. Cramér-Rao alignment bound 의 핵심 empirical input 이 unverified.

**Why deleted**: "Two distinct latencies require alignment" 는 *trivial definitional fact* — 정리 자격 없음. Alignment bit cost 계산은 unverified empirical assumption 의존.

**Replacement**: §5.2.1 의 *quantitative bit cost estimate* 는 본문 유지 (*empirical estimate* 로 표기), 그러나 TC 라벨 박탈. M-P latency 차이의 존재 사실은 §5.1 본문 (M/P 경로 정량) 에 *empirical fact* 로 유지.

#### 5.2.1 동기화 지연의 bit cost

**상대 시프트 분석**. 자극 $s(t)$ 가 bandlimited (bandwidth $W$). M-pathway 가 $s(t - \tau^M)$ 를, P-pathway 가 $s(t - \tau^P)$ 를 전달. 상대 지연 $\Delta\tau = \tau^P - \tau^M$.

**두 신호의 cross-correlation**: $R_{MP}(\tau) = \mathbb{E}[s(t) s(t + \tau)]$. 자연 장면의 시간 상관이 $|R_{MP}(\Delta\tau)|$ 를 결정.

자연 장면의 시간 스펙트럼 $\sim 1/\omega^2$ (Field 1987 의 시간 버전) → 상관 함수 $R(\tau) \propto e^{-|\tau|/\tau_c}$ with $\tau_c \sim 50-100$ ms. $\Delta\tau \approx 30$ ms with $\tau_c \sim 50$ ms:

$$
R_{MP}(\Delta\tau) / R(0) \approx e^{-30/50} \approx 0.55
$$

따라서 두 경로가 전달하는 정보 사이의 *공유 부분*이 55% — 나머지 45%는 *서로 다른 시각*의 독립 정보.

**Alignment cost**. 두 스트림을 *동일한 physical time* 에 정렬하기 위해서는 alignment 매개변수 $\Delta\tau$ 를 *추정*해야 함. Cramér-Rao bound 으로 추정 정밀도:

$$
\sigma_{\Delta\tau}^2 \geq \frac{1}{\mathcal{I}(\Delta\tau)}
$$

$\mathcal{I}(\Delta\tau)$ 는 cross-channel Fisher information on timing. 이 추정 과정에서 *소비되는 정보* (bits):

$$
\text{Cost}_{\text{bits}} = \log_2\!\frac{\Delta\tau_{\text{max}}}{\sigma_{\Delta\tau}} \approx \log_2\!\frac{100 \text{ ms}}{1 \text{ ms}} \approx 7 \text{ bits}
$$

($\sigma_{\Delta\tau} \sim 1$ ms 의 추정 정밀도 가정; physiologically: inter-pathway latency 가 $\sim 1$ ms 정밀도로 tune 됨.)

**증명 가능성**: 정의의 직접 결과. *Alignment* 의 정보 비용은 *temporal binding problem* 의 한 instance.

**의미**: 신경계는 *동시성* 의 *허구* 를 유지하기 위해 추가 처리. 본 디렉토리는 이 처리를 *stage 4 이후* 의 미해결 문제로 둠 (OP-SP-007).

### 5.3 정보 종류의 분리

- M : *언제, 어디서* (where, when) — motion, transient, low spatial freq, high temporal freq
- P : *무엇* (what) — fine detail, color (L-M), sustained, high spatial freq
- K : *부가적 색 정보* (S vs L+M)

이 *기능적 분리*가 *해부학적 경로 분리*에 대응. Cortical processing 에서도 별도 stream 유지 (V1 4Cα/β, V2 stripe 등).

### 5.4 채널-병렬 kernel

$\mathcal{K}_3$ 가 각 신경절세포 type 마다 *다른 변환 kernel*:

$$
\mathcal{K}_3 = \bigsqcup_{\tau \in \{M, P, K\}} \mathcal{K}_3^\tau \otimes \text{type-specific routing}
$$

여기서 *routing* 은 stage 2 의 다채널 출력에서 *어느 채널이 어느 ganglion type 에 가는지* 의 mapping.

---

## 6. ON-center / OFF-center 수용야 상속

### 6.1 양극세포 → 신경절세포

신경절세포의 수용야는 *직접 연결된 양극세포들의 수용야의 합* — 그리고 양극세포는 이미 ON / OFF + DoG ([[04_stage2_inner_retinal_algebra|04]]).

따라서 신경절세포는 *자동* 으로 ON-center 또는 OFF-center 의 center-surround 수용야 보유.

### 6.2 채널 곱

| Bipolar type → | Ganglion type → |
|----|----|
| ON-bipolar DoG | ON-center ganglion |
| OFF-bipolar DoG | OFF-center ganglion |

각 ganglion (M / P / K) 가 ON 과 OFF 두 변종으로 또 분리 — 따라서 총 *최소 6 종* (M-ON, M-OFF, P-ON, P-OFF, K-ON, K-OFF).

### 6.3 수용야의 정확한 형식

$$
\text{RF}_c(x) = \int K_{\text{DoG}}^{c}(x - x') \cdot w_c(x') dx'
$$

with $K_{\text{DoG}}^{c}$ inherited from bipolar, $w_c$ a *pooling weight*.

---

## 7. 비균질 표본화 — Fovea vs Periphery

### 7.1 격자 비균질성

신경절세포 *밀도* 와 입력 *convergence* 가 망막 위치에 따라 dramatically 다름:

| Eccentricity | 신경절세포 밀도 (cells/mm²) | Photoreceptor : ganglion |
|-----|-----|-----|
| Fovea (0°) | $\sim 35000$ | $\sim 1 : 1 : 1$ (cone : midget bipolar : midget ganglion) |
| 5° eccentricity | $\sim 4000$ | $\sim 5 : 1$ |
| 20° eccentricity | $\sim 500$ | $\sim 50 : 1$ |
| 60° eccentricity | $\sim 50$ | $\sim 500 : 1$ |

전체 평균: $\sim 126:1$ — 광수용기 $1.26 \times 10^8$ → 신경절세포 $\sim 10^6$.

### 7.2 비균질 표본화의 수학적 형식 — Eccentricity Scaling

신경절세포 *밀도* $\rho$ 의 eccentricity $e$ (시각도 단위, degrees of visual angle) 의존성:

$$
\boxed{\rho(e) \propto \left(e + e_0\right)^{-2}}
$$

여기서 $e_0 \approx 0.9°$ (foveal scale factor; 단, 다양한 species 에서 $0.5° - 2°$ 범위). Drasdo (1977) 의 인간 망막 측정 결과 및 Curcio-Allen (1990) 의 조직학적 데이터에서.

**유도 근거**: 망막 표면 넓이가 eccentricity 에 따라 증가 (망막 = 구면 일부; 넓이 $\propto e$), 반면 신경절세포 총 수 (고정) → 밀도 $\propto 1/e$ 이 첫 근사. $e_0$ 의 추가로 foveal singularity 완화 → $\rho \propto (e + e_0)^{-2}$ 가 전체 범위에서 좋은 fitting.

**Receptive field size** 는 역비례:

$$
L_{\text{RF}}(e) \propto \rho(e)^{-1/2} \propto (e + e_0)
$$

선형 scaling: periphery 에서 RF size 가 eccentricity 에 비례하여 증가.

#### 7.2.1 피질 확대 인수 (Cortical Magnification Factor) — Drasdo 관계

*Cortical Magnification Factor (CMF)*: V1 에서 시각 공간의 단위 각도 당 피질 mm.

**Drasdo (1977) 관계**:

$$
\text{CMF}(e) \approx \frac{a}{e + e_0} \text{ [mm/deg]}
$$

$a \approx 7.99$ mm/deg (인간 V1; Daniel-Whitteridge 1961 데이터를 Drasdo 가 fitting).

**망막-피질 대응**: $\text{CMF} \propto 1/(e + e_0)$ 이고 $\rho \propto 1/(e + e_0)^2$ → $\text{CMF} \propto \sqrt{\rho}$.

**해석**: V1 에서의 *공간 해상도* $\propto \text{CMF}$. 이것이 망막 표본화와 *일치* — 망막 ganglion cell 밀도의 square root 가 피질 확대에 비례.

따라서:
- Fovea ($e = 0$): CMF $\approx a/e_0 \approx 8$ mm/deg → 고해상도
- $e = 10°$: CMF $\approx 8/11 \approx 0.7$ mm/deg
- $e = 40°$: CMF $\approx 8/41 \approx 0.2$ mm/deg

**Nyquist 한계**: 망막 격자가 공간 주파수 $f_{\text{Nyq}}(e) = \rho(e)^{1/2}/2$ cycles/mm (2D Nyquist) 까지의 세부 정보를 표본화 가능. Fovea: $\sim 50$ cycles/deg, periphery 60°: $\sim 1$ cycle/deg.

### 7.3 압축의 정보론적 한계

### TC-SP-3.3 — [DELETED 2026-05-25 Pass 4 (escalated from Pass 3 WEAKENED)]

**Status**: **DELETED via Pass 4 — weakening insufficient**. Pass 4 의 #46 (W_max → ∞ boundary 가 weakening 의 (Q1) 을 무효화 → divergence 회귀; para-foveal rapid ρ(e) 미처리) + #51 (overlapping RF 의 correlated samples 가 independent-pixel pooling 가정 위반) → cumulative 4 patterns → 박탈.

**Original statement**: $L_{\text{corr}} > L_{\text{RF}}$ 이면 126:1 압축 lossless.

**Weakening attempt (Pass 3, also DELETED)**: (Q1) bandlimited patch + (Q2) finite $L_{\text{corr}}^{\text{eff}}$ + (Q3) sparse edges. Pass 4 가 새 hole 발견 — qualifier (Q2) 가 *hypothesis-by-stipulation*, derivation 아님.

**Why DELETED**: 126:1 는 *anatomical fact* (영장류 photoreceptor:ganglion 평균 비율) — 정리 자격 없음. Information-theoretic bound 자체는 자연 이미지 1/f² 의 IR 발산 + overlapping RF correlation 에 의해 *constructed only by hypothesis circular reasoning*. 정리 자격 박탈.

**Replacement**: 126:1 anatomical fact 는 §7 본문 유지. *Bandlimited natural patch 위 rate-distortion* 의 정확한 derivation 은 추후 OP candidate. 정리 라벨 없음.

#### 7.3.1 Rate-Distortion 유도 — $1/|\xi|^2$ Natural Scene Spectrum

**자연 장면의 공간 스펙트럼**. Field (1987) 의 자연 이미지 통계 (2D):

$$
P(\xi) \propto \frac{1}{|\xi|^2}, \quad \xi \in \mathbb{R}^2 \setminus \{0\}
$$

이는 *scale-invariant (fractal)* 공간 통계. 이미지를 Gaussian process 로 모델링:

$$
s(x) \sim \mathcal{GP}(0, K), \quad \hat{K}(\xi) = P(\xi) \propto |\xi|^{-2}
$$

**Rate-distortion for Gaussian source with spectral constraint**.

이미지 $s(x)$ 를 spatial frequency 영역에서 독립적 Gaussian 채널로 분해 (Karhunen-Loève). 각 주파수 $\xi$ 에서:

$$
R(\xi, D_\xi) = \frac{1}{2} \log_2^+ \frac{P(\xi)}{D_\xi} := \frac{1}{2} \max\!\left(0, \log_2 \frac{P(\xi)}{D_\xi}\right)
$$

(Shannon 1948 의 rate-distortion for Gaussian source.)

전체 rate-distortion: water-filling 원리로

$$
R(D) = \int_{|\xi| < \xi_{\text{cut}}} \frac{1}{2} \log_2 \frac{P(\xi)}{\theta}\,d\xi
$$

($\theta$ = water level; $D = \int_{|\xi| > \xi_{\text{cut}}} P(\xi)\,d\xi + \theta \cdot \text{Area}(\xi < \xi_{\text{cut}})$.)

**압축 bound 유도**:

주변시 신경절세포의 수용야 크기 $L_{\text{RF}} \sim 5°$ at eccentricity 30°. 이에 대응하는 공간 주파수 cutoff $f_{\text{cut}} = 1/L_{\text{RF}} \sim 0.2$ cycles/deg. 이보다 *높은 주파수* 의 정보는 *표본화 불가* (aliasing).

손실되는 정보:

$$
\Delta I = \int_{|\xi| > f_{\text{cut}}} \frac{1}{2} \log_2 \frac{P(\xi)}{\theta_{\min}}\,d\xi
$$

$P(\xi) \propto |\xi|^{-2}$ 으로 고주파 에너지가 *급격히 작음* (power-law decay). 2D 적분:

$$
\int_{|\xi| > f_{\text{cut}}} |\xi|^{-2}\,d^2\xi = 2\pi \int_{f_{\text{cut}}}^\infty r^{-2} r\,dr = 2\pi \int_{f_{\text{cut}}}^\infty r^{-1}\,dr
$$

발산! 그러나 *distortion* 은 자연 상관 길이 $L_{\text{corr}}$ 로 인해 고주파 에너지가 실제로는 $1/|\xi|^\alpha$ with $\alpha > 2$ 로 더 가파름 (Field 1987: $\alpha \approx 2.1-2.4$). 따라서:

$$
\Delta I \lesssim \int_{f_{\text{cut}}}^\infty \frac{1}{2}\log_2\!\frac{P(f)}{\theta_{\min}} 2\pi f\,df
$$

이는 수렴하고, 정보 손실이 *finite*.

**정량적 bound**:

$$
\text{Info loss} \lesssim \log_2\!\left(1 + \frac{L_{\text{RF}}^2}{L_{\text{corr}}^2}\right) \text{ [bits/cell]}
$$

$L_{\text{corr}} \sim 1°$ (자연 장면의 coherence scale; field 1987), $L_{\text{RF}} \sim 1-5°$ at periphery:

- $L_{\text{RF}} = 1°$: $\log_2(1 + 1) = 1$ bit/cell
- $L_{\text{RF}} = 5°$: $\log_2(1 + 25) \approx 4.7$ bits/cell (그러나 이 경우 자연 장면의 상관이 커서 주변 세포들이 중복 커버 — 실제 정보 손실은 더 작음)

**의미**: 진화는 *공간 상관이 큰 영역* (주변시) 에서 압축을 진행. *공간 상관이 작은 영역* (중심시) 에서는 1:1 보존. 이는 *자연 이미지 통계에 최적화된 retinal sampling* 의 rate-distortion 표현.

### 7.4 OP-SP-005 — 비균질 표본화의 Sheaf 처리

**Status**: OPEN. Severity: Medium.

**문제**: §7 의 비균질 표본화는 단순 *density variation* 으로 보이나, 더 자연스러운 수학적 객체는 *sheaf*.

#### 7.4.1 Presheaf 정의

망막 표면 $\Sigma_{\text{ret}}$ 을 위상공간으로 보자. 열린 집합 $U \subset \Sigma_{\text{ret}}$ 에 대해:

**Presheaf** $\mathcal{F}$ 를 다음으로 정의:

$$
\mathcal{F}(U) := \{ \text{ganglion cell responses on } U \} = \prod_{c : p_c \in U} \mathcal{N}(\mathbb{R}^+)
$$

즉 $U$ 에 속하는 모든 신경절세포 위치 $p_c$ 의 스파이크 트레인 공간.

**Restriction maps**. $V \subset U$ 에 대해:

$$
\rho_{UV} : \mathcal{F}(U) \to \mathcal{F}(V), \quad (G_c)_{p_c \in U} \mapsto (G_c)_{p_c \in V}
$$

단순히 $V$ 바깥 세포를 *잊음*. 이것이 restriction map.

**Gluing axiom (Sheaf 조건)**. 열린 덮개 $U = \bigcup_\alpha U_\alpha$ 와 각 $U_\alpha$ 위 section $s_\alpha \in \mathcal{F}(U_\alpha)$ 가 *compatible* ($\rho_{U_\alpha, U_\alpha \cap U_\beta}(s_\alpha) = \rho_{U_\beta, U_\alpha \cap U_\beta}(s_\beta)$) 이면 유일한 $s \in \mathcal{F}(U)$ 가 존재하여 $\rho_{U, U_\alpha}(s) = s_\alpha$.

**문제**: 이 presheaf 가 sheaf 가 되려면 restriction map 이 *일관성* 을 가져야 한다. 신경절세포의 receptive field 가 *겹치므로* ($U_\alpha \cap U_\beta$ 의 세포가 $U_\alpha$ 와 $U_\beta$ 응답에 동시 포함), gluing 이 *자명하게 consistent*.

그러나 *reconstruction* (spikes → scene) 의 관점에서는 다름 — 다른 region 의 response 가 *compatible* 하려면 *noise* 와 *RV correlation* 의 일관성도 필요 → sheaf condition 이 *non-trivial*.

#### 7.4.2 Obstruction Cohomology $H^1(\mathcal{F})$

**Cech cohomology**. 덮개 $\{U_\alpha\}$ 에 대해:

$$
H^1(\mathcal{F}) := Z^1(\mathcal{F}) / B^1(\mathcal{F})
$$

- $Z^1$: 1-cocycles (compatible 하지만 global section 에서 오지 않는 local sections 의 집합)
- $B^1$: 1-coboundaries (global section 의 제한)

**$H^1 = 0 \Leftrightarrow$ Sheaf** (gluing이 항상 uniquely 가능).

**$H^1 \neq 0$의 의미**: 국소적으로 compatible 한 응답들이 *전역적으로 consistent 하지 않음* — 즉 망막 전체 응답을 국소 응답의 gluing 으로 재구성할 수 없는 *위상학적 장애물*.

**물리적 해석**: $H^1(\mathcal{F}) \neq 0$ 이면 망막 응답의 *전역 재구성* 이 원리적으로 불가 (국소 patch 들이 서로 모순). 이는 *non-uniform sampling + noise correlation* 의 상호작용에서 발생 가능.

**해결 방향**: 이 $H^1$ 의 계산이 OP-SP-005 의 핵심. Candidate 도구: persistent sheaf cohomology (Curry 2014); Robinson (2014), "Topological Signal Processing".

---

## 8. Information-Theoretic 회계

### 8.1 단일 채널 capacity

§4.3 의 추정 — Cox model 로:

$$
C_c = \int_0^{W_c} \log_2\!\left(1 + \text{SNR}(\omega)\right) d\omega \text{ [bits/sec]}
$$

Poisson noise 의 경우 $\text{SNR}(\omega) = \bar{\lambda} / (W_c \cdot \sigma_{\text{shot}}^2)$ where $\sigma_{\text{shot}}^2 = 1$ (normalized Poisson). 이를 이용하면:

$$
C_c = W_c \cdot \log_2\!\left(1 + \frac{\bar{\lambda}}{W_c}\right) \text{ bits/sec}
$$

단순화: 전형값 $\bar{\lambda} \sim 50$ Hz, $W \sim 30$ Hz:

$$
C_c = 30 \cdot \log_2\!\left(1 + \frac{50}{30}\right) = 30 \cdot \log_2(2.67) \approx 30 \times 1.42 \approx 42 \text{ bits/sec}
$$

그러나 이는 상한 (optimal encoding 가정). 실제 ganglion cell 의 유효 capacity 는 sub-optimal encoding 으로 인해 $\sim 5-15$ bits/sec per cell (Reinagel-Reid 2000; Strong et al. 1998).

### 8.2 Per-bandwidth 적분

**Rate-dependent SNR**. Poisson channel 에서 SNR 은 주파수 $\omega$ 에 독립 (white noise). 그러나 자극 스펙트럼 $S_s(\omega) \propto 1/\omega^2$ (1/f² scene) 이면:

$$
\text{SNR}(\omega) = \frac{|H(\omega)|^2 S_s(\omega)}{S_{\text{noise}}(\omega)} = \frac{|H(\omega)|^2 / \omega^2}{\bar{\lambda}}
$$

($H(\omega)$ = 세포의 시간 전달 함수 — bandpass for M, lowpass for P.)

비균질 SNR 로 per-bandwidth capacity:

$$
C_c = \int_0^{W_c} \log_2\!\left(1 + \frac{|H(\omega)|^2 S_s(\omega)}{\bar{\lambda}}\right) d\omega
$$

M cell ($H$ bandpass, peak $\sim 20$ Hz):

$$
C_M \approx \int_5^{50} \log_2\!\left(1 + \frac{A_M / \omega^2}{\bar{\lambda}}\right) d\omega \approx 15-30 \text{ bits/sec}
$$

P cell ($H$ lowpass, peak $\sim 5$ Hz):

$$
C_P \approx \int_0^{20} \log_2\!\left(1 + \frac{A_P / \omega^2}{\bar{\lambda}}\right) d\omega \approx 3-8 \text{ bits/sec}
$$

M 이 더 높은 capacity per cell (빠른 반응, 높은 bandwidth) — 그러나 M 세포 수가 ~10%이므로 전체 기여는 P 와 비슷.

### 8.3 통합 capacity

$\sim 10^6$ 채널 × $\sim 5$ bits/sec = $\sim 5 \times 10^6$ bits/sec = $\sim 5$ Mbit/sec of optic nerve bandwidth.

(실제 추정 다소 변동; 이는 order-of-magnitude.)

### 8.4 손실의 정량

Stage 0 의 광자율 ($\sim 10^9$ photons/sec at moderate light) 와 비교:
- Each photon $\sim 1$ bit (existence + location/wavelength info)
- 그러나 광수용기 적분 + Naka-Rushton 압축 + DoG + 채널 분기 + 압축 후 → $\sim 5$ Mbit/sec
- 따라서 *수백 배 압축*

이게 [[06_endtoend_information_bound|06]] 의 정확한 회계 대상.

---

## 9. $\mathcal{K}_3$ — explicit form

### 9.1 정의 (모델 C / Cox 채택)

$\mathcal{K}_3 : \mathcal{S}_2 \to \mathcal{S}_3$ 의 정의:

> 입력 $B \in \mathcal{S}_2$ 가 주어졌을 때, 각 채널 $c \in \mathcal{C}_g$ 에 대해
> $$\lambda_c(t) := \phi_c\!\big( w_c \cdot B_{\sigma(c)}(p_c, t) \big)$$
> with $\sigma(c)$ a fixed *routing* (stage 2 channel → ganglion type), $\phi_c$ a channel-specific output nonlinearity (softplus or ReLU), $w_c$ pooling weight. 그 후 $G_c$ 가 *inhomogeneous Poisson with rate $\lambda_c$*, 서로 다른 채널은 *조건부 독립* (given $B$).

### 9.2 well-definedness

채널 수가 *유한* 이고 각 채널이 Poisson → 표준. [[01_framework_master#TC-SP-1.1|01 TC-SP-1.1]] 의 stage 3 측 보장.

### 9.3 인과성

$\lambda_c(t)$ 는 $B_{\sigma(c)}(p_c, s)$ for $s \leq t$ 에만 의존 (해당 채널의 stage 2 합성곱이 인과적). 따라서 stage 3 도 인과적. [[01_framework_master#TC-SP-1.3|01 TC-SP-1.3]] 보장.

### 9.4 다른 모델 (A, B, D) 의 인과성

- A (LIF): SDE 자체가 인과적
- B (SRM): kernel $\kappa$ supported on $\mathbb{R}^+$ — 인과적
- D (Hawkes): self-history 만 사용 — 인과적

모든 모델 변종이 인과성 유지.

---

## 10. Theorem-Candidates summary

| 코드 | 명제 |
|------|------|
| TC-SP-3.1 | Rate sufficiency under bandlimited + sufficient rate + Poisson noise (§4.2.1 유도) |
| TC-SP-3.2 | M / P latency asymmetry → two time axes; synchronization-delay bit cost $\sim 7$ bits (§5.2.1) |
| TC-SP-3.3 | Peripheral compression bound from $1/|\xi|^2$ natural scene rate-distortion (§7.3.1) |

### 10.1 TC-SP-3.1 정확한 진술 (재확인)

**조건**: (i) $B_c$ bandlimited with bandwidth $W_c$; (ii) $\bar{\lambda}_c \geq 2W_c$; (iii) Cox process model (Fano $= 1$).

**결론**: $I(B_c; G_c) = I(B_c; \bar{\lambda}_c) + O(W_c/\bar{\lambda}_c \cdot \log(\bar{\lambda}_c/W_c))$.

**증명 스케치 핵심**: Cox process 에서 $\bar{\lambda}_c$ 가 sufficient statistic (§4.2.1 단계 2). Correction term 은 finite $\bar{\lambda}/W$ 의 Nyquist 초과 timing fluctuation 의 기여.

### 10.2 TC-SP-3.2 정확한 진술 (재확인)

**설정**: $\tau^M \approx 70$ ms, $\tau^P \approx 100$ ms, $\Delta\tau = 30$ ms. 자극 bandwidth $W$.

**결론 1**: V1 에서 M-P 동기화 없이는 $I(s; G^M, G^P) < I(s; G^M) + I(s; G^P)$ (두 경로의 공유 정보를 활용하지 못함).

**결론 2**: Alignment cost $\sim \log_2(\Delta\tau_{\text{max}} / \sigma_{\Delta\tau}) \approx 7$ bits (§5.2.1).

### 10.3 TC-SP-3.3 정확한 진술 (재확인)

**자연 장면 모델**: $P(\xi) \propto |\xi|^{-2}$, Gaussian source.

**결론**: Peripheral ganglion cell (RF size $L_{\text{RF}}$) 의 정보 손실 상한:

$$
\text{Info loss} \lesssim \log_2\!\left(1 + \frac{L_{\text{RF}}^2}{L_{\text{corr}}^2}\right) \text{ bits/cell}
$$

**적용 조건**: $L_{\text{corr}} > 0$; scene statistics follow $1/|\xi|^2$ (Field 1987 empirical).

---

## 10.5 Population Coding 과 Noise Correlation

### 10.5.1 단순 Cox 모델의 가정

본 문서 §9 의 Cox 기반 $\mathcal{K}_3$ 는 조건부 독립 채널을 가정:

$$
P(G_1, G_2, \ldots | B) = \prod_{c} P(G_c | B)
$$

즉, $B$ 가 주어졌을 때 신경절세포들의 스파이크가 *서로 독립*. 이는 수학적으로 편리하지만 생물학적으로는 *근사*다.

### 10.5.2 실제 Population 의 Noise Correlation

실제 신경절세포 population 에서는 **noise correlation** 이 존재:

$$
\text{Cov}[G_i(t), G_j(t) | s(t)] \neq 0 \text{ for } |p_i - p_j| < d_{\text{corr}}
$$

두 종류의 상관을 구분해야 함:

**Signal correlation** $r^{\text{signal}}_{ij}$: 자극 $s$ 의 변화에 대한 두 세포의 응답이 비슷한 정도.

$$
r^{\text{signal}}_{ij} := \text{Corr}\!\left[\mathbb{E}[G_i | s], \mathbb{E}[G_j | s]\right]
$$

공간적으로 인접하고 같은 type 의 세포는 비슷한 RF → $r^{\text{signal}} \approx 1$ at $|p_i - p_j| < L_{\text{RF}}$.

**Noise correlation** $r^{\text{noise}}_{ij}$: 자극을 고정했을 때 두 세포 응답의 공변동.

$$
r^{\text{noise}}_{ij} := \text{Corr}\!\left[G_i - \mathbb{E}[G_i | s], G_j - \mathbb{E}[G_j | s]\right]
$$

실험적으로 $r^{\text{noise}} \approx 0.01 - 0.1$ (약하나 0 이 아님; Bair et al. 2001; Pillow et al. 2008).

### 10.5.3 Noise Correlation 이 정보에 미치는 영향

Schnitzer-Meister (2003) 및 Averbeck et al. (2006) 의 결과:

**정보 감소 조건**: signal correlation 과 noise correlation 이 *같은 방향* 이면:

$$
I_{\text{population}} < \sum_c I_c \text{ (independent channels)}
$$

즉, 양의 noise correlation 이 *정보를 감소*시킨다 — 세포들이 같은 노이즈를 공유하므로 독립 채널이 아님.

**정보 증가 조건**: signal correlation 과 noise correlation 이 *반대 방향* 이면:

$$
I_{\text{population}} > \sum_c I_c
$$

이른바 *differential coding*: 반대 방향 노이즈 상관이 정보를 *증가*시킴.

**수식**. 선형 Gaussian 근사에서 (Averbeck-Lee 2006):

$$
I_{\text{pop}} \approx \frac{1}{2} \log\frac{|\Sigma_{\text{noise}} + \Sigma_{\text{signal}}|}{|\Sigma_{\text{noise}}|}
$$

독립 가정 ($\Sigma_{\text{noise}} = \sigma^2 I$) 이면 $I_{\text{pop}} = \sum I_c$. Noise correlation 이 있으면 상황에 따라 증감.

### 10.5.4 단순 Cox 모델이 놓치는 것

1. **Noise correlation 의 존재**: 공유 내부 노이즈 (기계적 진동, 네트워크 진동) 가 만드는 correlations.

2. **Network effects**: Horizontal cell 과 amacrine 을 통한 측방 상호작용이 *조건부 독립*을 깸.

3. **Adaptive gain control**: 강도에 따라 세포들이 동시에 response gain 을 조절 → 공통 fluctuation → noise correlation.

4. **Gap junctions**: 인접 신경절세포들 사이의 전기적 결합 → 직접 noise 전파.

### 10.5.5 Population Code 의 유효 차원성

실제 population 의 noise covariance $\Sigma_{\text{noise}}$ 가 low-rank 이면 (공유 noise 원천이 적음), 유효 정보는:

$$
\dim_{\text{eff}} = \text{rank}(\Sigma_{\text{noise}})^{-1} \cdot n_{\text{cells}}
$$

보다 적은 차원에 해당. Dimensionality reduction 으로 실제 정보 운반 방향을 파악 가능.

### 10.5.6 본 디렉토리에서의 처리

본 stage 문서는 *조건부 독립 가정* 을 유지 (Cox model default). 다음 이유:

1. Noise correlation 의 크기 (0.01-0.1) 이 signal variation 대비 작음 → 1차 근사에서 무시 가능.
2. 정보론적 bound (TC-SP-3.1~3.3) 가 *독립 채널 가정*에서 *보수적 (conservative)* — 실제 정보는 더 작거나 더 클 수 있음.
3. Noise correlation 의 정밀한 처리는 별도 단계 (OP-SP-008 후보) 로.

**함의**: §8 의 capacity 추정 $\sim 5$ Mbit/sec 은 *noise correlation 무시한 독립 채널 상한*. 실제 population 정보는 noise correlation 방향에 따라 다를 수 있음.

---

## 11. Open Problems

| 코드 | 문제 | Severity |
|------|------|----------|
| OP-SP-005 | 비균질 표본화의 sheaf 처리; $H^1(\mathcal{F})$ 계산 (§7.4) | Medium |
| OP-SP-007 | Stage 4 cut location (시신경 후, LGN, V1?) | Medium |

OP-SP-007 는 본 stage 의 *경계* 문제. 본 디렉토리는 *Stage 4 ≡ 시신경 도착 직후* 채택 (LGN 은 별도 후속 작업).

---

## 12. 도구 사용 summary

| 도구 | 사용 |
|------|------|
| 4.1 점과정 | Cox process, Hawkes (§2.3, §2.4); renewal theory (§3); Laplace transform (§3.1.1) |
| 4.2 SDE | LIF SDE (§2.1); Fokker-Planck (§2.1.1 FPT 유도) |
| 4.3 함수해석 | output nonlinearity $\phi$; GLM likelihood (§2.3.1) |
| 4.8 정보이론 | rate sufficiency (TC-SP-3.1; §4.2.1); Poisson channel capacity Kabanov (§4.3.1); compression bound (TC-SP-3.3; §7.3.1) |
| 4.9 대수위상 | sheaf (OP-SP-005; §7.4); $H^1$ obstruction |
| 4.5 Scale-space | Drasdo CMF scaling (§7.2.1) |

---

## 13. (Ω, σ) Tier 2 mapping (preview)

[[07_omega_sigma_lift|07]] 에서. Stage 3 의 직접 매핑:

- $\Omega_3 = \bigcup_c \{(c, t) : t \in G_c\}$ — 스파이크 사건들 (다시 점과정)
- $\sigma_3((c_i, t_i), (c_j, t_j)) \iff |t_i - t_j| < \tau \text{ AND } d(p_{c_i}, p_{c_j}) < \delta$ (시공간 인접; cell type 무관)

흥미: $\mathcal{S}_3$ 가 *다시* 점과정 형태 → **Stage 0 과 Stage 3 가 위상학적으로 동일 종류**. 이게 [[07_omega_sigma_lift#5. 점 ↔ 장 ↔ 점 순환|07 §5]] 의 *point ↔ field ↔ point* 순환의 직접 사례.

---

## 14. 본 stage 가 *시도하지 않는 것*

- 시신경 이후 (LGN, V1) — Stage 4 의 정의 (OP-SP-007)
- *Precise timing* code 의 정량적 limits beyond §4.2.1 (rate-only sufficient 의 정확한 한계)
- *Adaptation* (gain control, light adaptation) — OP-SP-009
- *Top-down feedback* 영향 — OP-SP-010
- *Population coding* 의 exact noise correlation structure (§10.5 에서 개요만; 정량 처리는 OP 후보)

---

*Stage 3 v1. 후속: [[06_endtoend_information_bound]]. 노출 type: $G \in \mathcal{S}_3$, ~1M 평행 스파이크 트레인. TC-SP-3.1 ~ 3.3 등록 + 완전 유도 포함. OP-SP-005 등록 (OP-SP-007 은 §11 에서 preview). 신규: §2.1.1 FPT/inverse-Gaussian 유도, §2.2.1 SRM≡LIF 동치, §2.3.1 GLM log-likelihood, §2.4.1 Hawkes 안정성 증명, §3.1.1 Laplace renewal density, §3.2.1-3 Fano factor 유도 3종, §4.2.1 TC-SP-3.1 완전 유도, §4.3.1 Kabanov capacity, §5.1.1 축삭 전도 속도 유도, §5.2.1 synchronization-delay bit cost, §7.2.1 Drasdo CMF, §7.3.1 rate-distortion 유도, §7.4.1-2 sheaf+H^1, §8.2 per-bandwidth integral, §10.5 population coding.*
