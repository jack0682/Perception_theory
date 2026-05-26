---
type: working/sensing_pipeline/open_problems
version: v1
date: 2026-05-25
status: DEFINITION-DRAFT
purpose: |
  Consolidated registry of all OP-SP-N open problems from stages 02–07.
  Each entry: full mathematical statement, severity, location of origin,
  literature pointers, candidate directions, candidate experiments,
  cross-references to relevant TC-SPs, PAI cross-links, and explicit
  non-resolution flag (no OP is moved to RESOLVED within this directory).
register: DEFINITION-DRAFT (open problems only; no resolution)
parent: 01_framework_master
constraint_compliance:
  canonical_theorem_changes: 0
  scc_edits: 0
  open_problems_resolved: 0
---

> [!nav] Parent: [[00_INDEX]] · Prev: [[07_omega_sigma_lift]]

# Open Problems — Sensing Pipeline (OP-SP-*)

## 0. 본 문서의 위치

본 문서는 [[02_stage0_photon_point_process|02]]~[[07_omega_sigma_lift|07]] 본문에서 등록한 모든 OP-SP-N 의 *통합 registry*. 본 디렉토리 안에서 어떤 OP 도 **RESOLVED 로 이동시키지 않음** ([[00_INDEX#0. 본 working subdirectory 의 위치|00 §0]] 의 discipline).

본 문서가 *수행하는 것*:
- 각 OP 의 *완전 수학적 statement* + severity + 출처 location
- 문헌 지표 (저자, 연도, 핵심 결과)
- 후보 실험 / 수치 검증 항목
- 각 OP 가 advancement 시 어떤 TC-SP 를 강화하는지의 cross-link
- Candidate 방향 (heuristic; binding 아님)
- 의존성 그래프 — OP 사이의 *blockage* 관계
- PAI OP 와의 cross-link (격리된 관계 명시)

본 문서가 *수행하지 않는 것*:
- 어떤 OP 의 *해결 시도* (모두 OPEN 으로 끝)
- OP 의 priority 결정 (severity rating 만; *어느 것을 먼저* 는 후속 plan)
- PAI 의 OP-PAI 와의 *연결 시도* (격리; future bridge work)
- 새 OP-SP 코드의 등록 (14개 고정)

---

## 1. OP-SP 통합 목록 (요약)

| 코드 | 제목 | Severity | 출처 stage | 영향받는 TC-SP |
|------|------|----------|-----------|----------------|
| OP-SP-001 | 양자 coherence 무시의 정당화 한계 | Low | [[02_stage0_photon_point_process#9.|02 §9]] | TC-SP-0.1, 0.2 |
| OP-SP-002 | Naka-Rushton 적응 동역학의 형식화 | Medium | [[03_stage1_photoreceptor_sde#10.|03 §10]] | TC-SP-1.4, 4.3 |
| OP-SP-003 | 다채널 분기의 fiber bundle 형식 | Medium | [[04_stage2_inner_retinal_algebra#6.5|04 §6.5]] | TC-SP-2.1, 5.2 |
| OP-SP-004 | 색 대립의 군론적 정당화 | High | [[04_stage2_inner_retinal_algebra#6.4|04 §6.4]] | TC-SP-2.6 |
| OP-SP-005 | 비균질 표본화의 sheaf 처리 | Medium | [[05_stage3_ganglion_spike_encoding#7.4|05 §7.4]] | TC-SP-3.3 |
| OP-SP-006 | SCC $u_t$ ↔ which stage? | High | [[07_omega_sigma_lift#5.5|07 §5.5]] | TC-SP-5.1, 5.2 |
| OP-SP-007 | Stage 4 cut location | Medium | [[05_stage3_ganglion_spike_encoding#11.|05 §11]] | TC-SP-3.2 |
| OP-SP-008 | Orientation 채널 (4 방향) 군론적 정당화 | Medium | [[04_stage2_inner_retinal_algebra#4.10|04 §4.10]] | TC-SP-2.4, 2.5 |
| OP-SP-009 | 적응 시상수 hierarchy | Medium | [[03_stage1_photoreceptor_sde#4.3|03 §4.3]] | TC-SP-1.4 |
| OP-SP-010 | Top-down feedback 무시 정당화 | Low | [[01_framework_master#TC-SP-1.3|01 TC-SP-1.3]] | TC-SP-1.3 |
| OP-SP-M1 | 순수 Tier 2 boundaries 의 필연성 | Low | [[07_omega_sigma_lift#7.|07 §7]] | TC-SP-5.2 |
| OP-SP-M2 | σ-pushforward 의 deterministic vs probabilistic | Low | [[07_omega_sigma_lift#3.4|07 §3.4]] | TC-SP-5.1 |
| OP-SP-M3 | SCC parallel (E_cl/sep/bd/tr ↔ stage 2 측면) 의 본질 | Medium | [[06_endtoend_information_bound#7.|06 §7]] | TC-SP-5.1, 5.2 |
| OP-SP-M4 | Free-energy principle 의 채택 / 거부 기준 | Low | [[06_endtoend_information_bound#6.2|06 §6.2]] | TC-SP-4.3 |

**총 14 OP**: core 10 (OP-SP-001 ~ 010) + meta 4 (OP-SP-M1 ~ M4). High severity 2; Medium 7; Low 5.

---

## 2. 개별 OP 의 완전 statement

### OP-SP-001 — 양자 coherence 무시의 정당화 한계

**Status**: OPEN. Severity: Low.

#### 2.1.1 완전 수학적 statement

[[02_stage0_photon_point_process#2.4 광자 도래의 Poisson 가정 — 정당화|02 §2.4]] 의 Poisson 가정은 *incoherent 광원* 에 대해서만 정밀하다. 형식적으로:

Poisson 점과정 $N$ 은 임의 서로소 Borel 집합 $A_1, \ldots, A_k \subset \mathcal{X}$ 에 대해

$$
P\big(N(A_1) = n_1, \ldots, N(A_k) = n_k\big) = \prod_{j=1}^{k} \frac{e^{-\mu(A_j)} \mu(A_j)^{n_j}}{n_j!}
$$

이 성립하는 점과정이며, 이는 *2차 moment measure 가 factorize* 됨을 등치적으로 함의:

$$
\mu^{(2)}(A \times B) = \mu(A) \cdot \mu(B), \quad A \cap B = \emptyset
$$

그러나 실제 광원의 2차 coherence 함수 $g^{(2)}(\tau)$ (Glauber, 1963) 는:

$$
g^{(2)}(\tau) := \frac{\langle \hat{a}^\dagger(t)\hat{a}^\dagger(t+\tau)\hat{a}(t+\tau)\hat{a}(t) \rangle}{\langle \hat{a}^\dagger(t)\hat{a}(t)\rangle^2}
$$

- *Coherent (laser)* state: $g^{(2)}(0) = 1$ — Poisson 정확.
- *Thermal (incoherent) state*: $g^{(2)}(0) = 2$ — super-Poissonian (photon bunching). 그러나 *단일 모드 탐지 시간* $\Delta t$ 가 광원 coherence time $\tau_c$ 보다 훨씬 크면: $g^{(2)}(0) \to 1$ (Poisson limit). 태양광 $\tau_c \approx 10^{-15}$ s, 탐지 시간 $\Delta t \sim 10^{-3}$ s 이므로 $\Delta t \gg \tau_c$ — Poisson approximation 극히 정밀.
- *Single-photon source* (parametric down-conversion): $g^{(2)}(0) = 0$ — sub-Poissonian (photon anti-bunching).
- *형광 표식 (FLIM)*: $g^{(2)}(0)$ 가 emitter 간 간격, 수명 등에 의존.

따라서 정확한 statement 는:

> **Claim (candidate)**: 자연 광 환경에서 감각 임계값 이상의 조도 $I \gg I_{\min}$ 에서, 시간 평균 $\Delta t \gg \tau_c$ 조건 하에, Poisson 근사의 오차는 $O\!\left( \tau_c / \Delta t \right)$ 로 억제된다.

이 claim 이 정확히 형식화되지 않은 것이 OP-SP-001 의 핵심.

#### 2.1.2 문헌 지표

- **Glauber, R.J. (1963)**. "The quantum theory of optical coherence." *Physical Review* 130(6), 2529–2539. — $g^{(2)}$ 정의와 coherent / thermal / sub-Poissonian 분류. 노벨상 (2005) 수상.
- **Hanbury Brown, R. & Twiss, R.Q. (1956)**. "Correlation between photons in two coherent beams of light." *Nature* 177, 27–29. — photon bunching 의 첫 관측 (intensity interferometry).
- **Mandel, L. & Wolf, E. (1995)**. *Optical Coherence and Quantum Optics*. Cambridge. — §10 에서 광원 클래스별 counting statistics 의 완전 처리. Cox process 가 super-Poissonian 의 자연 확률론적 extension.
- **Daley-Vere-Jones (2003)**. *An Introduction to the Theory of Point Processes*, Vol. I. — Poisson 점과정의 측도론적 정의 (§2).
- **Rieke, F. et al. (1997)**. *Spikes: Exploring the Neural Code*. MIT Press. — §2 에서 광수용기 photon-counting 의 Poisson 가정 실증적 정당화.

#### 2.1.3 후보 실험 / 수치 검증

A. **Coherence regime simulation**: Poisson 과 Cox process (rate 자체를 Gamma 분포) 로 photon counting 시뮬레이션. 두 경우의 세포 응답 분산 비교 — $\tau_c / \Delta t$ 의 함수로 오차 quantify.

B. **$g^{(2)}$ 문턱값 탐색**: 광수용기 SNR 을 Poisson vs super-Poissonian 입력으로 계산. $g^{(2)}(0)$ 가 어느 임계값 이상에서 TC-SP-0.1 의 factorization 이 실질적으로 깨지는지 수치 확인.

C. **임계 자극에서의 quantum noise**: 절대 임계 (dark-adapted, ~5–7 quanta) 에서의 Poisson 통계 vs. 실측 psychophysics (Hecht-Shlaer-Pirenne 1942 데이터와 재분석).

#### 2.1.4 영향받는 TC-SP

- TC-SP-0.1 (Stage 0 statistics factorization) — Poisson 가정에 직접 의존
- TC-SP-0.2 (Photon limit) — 단광자 검출의 *통계* 가 Poisson 일 때만 자명한 1차 사건

#### 2.1.5 후보 방향

A. *Restriction*: 광원 클래스를 *Poisson 정확한 부류로 명시* — incoherent natural light 만 다룸. 본 디렉토리 default.

B. *Cox 확장*: Poisson 을 *Cox process* (rate 자체 random) 로 일반화 — coherence 효과를 stochastic intensity 로 흡수. 추가 cost 작음.

C. *Mandel-Wolf 도입*: 광 coherence 이론 (Mandel-Wolf §10) 을 직접 도입 — 정확하지만 이론 부피 大.

#### 2.1.6 PAI cross-link

직접 PAI cross-link 없음. OP-SP-001 은 pipeline 의 물리적 입력 통계에 대한 질문으로, PAI 의 formation-level OP-PAI-001..006 과 독립적이다.

**Blocking**: 본 OP 가 OPEN 으로 남아도 후속 stages 작업 가능 (Stage 0 의 Poisson 을 working hypothesis 로).

---

### OP-SP-002 — Naka-Rushton 적응 동역학의 형식화

**Status**: OPEN. Severity: Medium.

#### 2.2.1 완전 수학적 statement

[[03_stage1_photoreceptor_sde#4.3 적응 — I_{50} 의 sliding|03 §4.3]] 의 $I_{50}(t)$ sliding 은 *phenomenological*:

$$
\frac{d I_{50}}{dt} = -\frac{1}{\tau_a}\bigl(I_{50}(t) - \kappa \bar{I}(t)\bigr)
$$

with $\bar{I}(t) = \int_0^\infty h_a(s) I(t-s)\, ds$ (exponential kernel, $h_a(s) = \tau_a^{-1} e^{-s/\tau_a}$), and $\kappa > 0$ 는 gain constant.

이 식이 정확히 *한 개* 의 적응 시상수 $\tau_a$ 를 가정한다. 그러나 광수용기 적응은 최소 4 개의 독립 시상수를 가진 계층 과정:

$$
\tau_{\text{channel}} \sim 10\text{ ms}, \quad \tau_{\text{Ca}} \sim 1\text{ s}, \quad \tau_{\text{rhodopsin}} \sim 5\text{ min}, \quad \tau_{\text{circadian}} \sim 10\text{ h}
$$

각각 다음 생화학 메커니즘에 대응:
- $\tau_{\text{channel}}$: cGMP-gated channel 의 직접 gain 변화
- $\tau_{\text{Ca}}$: guanylyl cyclase-activating protein (GCAP) 를 통한 Ca$^{2+}$ 피드백
- $\tau_{\text{rhodopsin}}$: opsin regeneration (11-cis-retinal 재합성)
- $\tau_{\text{circadian}}$: 망막 내 circadian clock 에 의한 gene expression 변화

*단일 $\tau_a$ 모델의 형식적 부정확성*: 현재 형식의 Naka-Rushton SDE

$$
R(I; t) = R_{\max} \cdot \frac{I^n}{I^n + I_{50}(t)^n}
$$

에서 $n$ 과 $I_{50}(t)$ 모두 *시간-불변 파라미터로 근사* — 여러 시상수 regime 에서의 정확도가 보장되지 않는다.

정확한 multi-scale 형식은 *연립 slow-fast SDE 계* 를 요구:

$$
\begin{cases}
dV = f(V, I_{50}^{(1)}, I_{50}^{(2)}, I) \,dt + \sigma_V \,dW_t \\
dI_{50}^{(1)} = -\frac{1}{\tau_1}(I_{50}^{(1)} - \kappa_1 \bar{I}_1) \,dt \\
dI_{50}^{(2)} = -\frac{1}{\tau_2}(I_{50}^{(2)} - \kappa_2 \bar{I}_2) \,dt \\
\vdots
\end{cases}
$$

*OP 의 핵심 질문*: 이 계층이 *독립 병렬 변수들의 합* 인가, *nested 종속 구조* 인가, 또는 *연속 스펙트럼* ($1/f$ kernel) 으로 대체 가능한가?

#### 2.2.2 문헌 지표

- **Naka, K.I. & Rushton, W.A.H. (1966)**. "S-potentials from luminosity units in the retina of fish." *J. Physiology* 185, 587–599. — Hill function 형태의 원전.
- **Pugh, E.N. & Lamb, T.D. (1993)**. "Amplification and kinetics of the activation steps in phototransduction." *Biochimica et Biophysica Acta* 1141, 111–149. — cascade 의 분자 시상수 정량화.
- **Smirnakis, S.M. et al. (1997)**. "Adaptation of retinal processing abolishes stable colour appearance." *Nature* 386, 671–674. — 다중 시상수 가설의 실증 (수초 vs 수분 적응).
- **Wark, B., Lundstrom, B.N. & Fairhall, A. (2007)**. "Sensory adaptation." *Current Opinion in Neurobiology* 17, 423–429. — multi-timescale 적응의 리뷰; $1/f$ power-law kernel 가설.
- **Pavliotis, G.A. & Stuart, A.M. (2008)**. *Multiscale Methods: Averaging and Homogenization*. Springer. — slow-fast SDE 의 singular perturbation 이론.
- **Torre, V. & Ashmore, J.F. (2000)**. *Molecular and Cellular Physiology of Neurons*. — calcium dynamics 의 time constants.

#### 2.2.3 후보 실험 / 수치 검증

A. **다중 시상수 fitting**: 실측 ERG (electroretinogram) adaptation curve 를 단일 $\tau_a$ 모델 vs. 2-시상수 모델 vs. power-law kernel 로 fit. AIC/BIC 로 모델 선택.

B. **Slow-fast 분리 검증**: $\epsilon = \tau_{\text{channel}} / \tau_{\text{Ca}} \approx 10^{-2}$ — 이 $\epsilon$ 에서의 averaging theorem (Pavliotis-Stuart §3) 이 실제 SDE 와 얼마나 가까운지 수치 ODE 적분으로 확인.

C. **정보-이론적 비교**: 단일 $\tau_a$ vs. 2-scale 모델에서의 Fisher information $\mathcal{I}(\theta)$ (intensity discrimination) 차이를 natural scene statistics (van Hateren database) 에서 계산.

#### 2.2.4 영향받는 TC-SP

- TC-SP-1.4 (Compression) — 정확한 $I_{50}$ dynamics 가 logarithmic compression 의 *시간 형식* 결정
- TC-SP-4.3 (Naka-Rushton optimality) — 적응이 mutual info 최대화의 *시간 변동 측면*

#### 2.2.5 PAI cross-link

간접 연결: OP-PAI-002 ($\mathcal{A}(u)$ 정의) 가 *시간 축 행동 해석* 을 포함할 경우, 적응의 시간 구조가 action-readiness 의 temporal window 를 결정할 수 있다. 그러나 이 연결은 현재 추측 수준이며 공식적으로 분리되어 있다.

**Blocking**: OP-SP-002 의 partial 해결 (slow-fast 분해) 이 TC-SP-1.4 의 *정량적* 강화. OP-SP-002 해결 없이 후속 stage 진행 가능.

---

### OP-SP-003 — 다채널 분기의 fiber bundle 형식

**Status**: OPEN. Severity: Medium.

#### 2.3.1 완전 수학적 statement

[[04_stage2_inner_retinal_algebra#1.2 상태공간 정의|04 §1.2]] 의 $\mathcal{S}_2 = \bigoplus_{c \in \mathcal{C}} C(\Sigma \times \mathbb{R}^+, \mathbb{R}^+)$ 는 채널들을 *독립 좌표축* 으로 취급한다.

정확히: 현재 모델에서는 채널 $c, c' \in \mathcal{C}$ 가 서로 다른 위치 $(x, t)$ 에서의 응답에 대해 어떤 *fiber-wise 구조* 도 없다. 채널 응답이 단순히 $\mathbb{R}^+$ 값을 가진 독립 함수들이다.

그러나 실제 구조는:

1. 모든 채널이 *동일 photoreceptor input* $V(x, t)$ 에서 분기 — 즉, 공통 base 를 가짐
2. 채널 $|\mathcal{C}| = 48$ 이 실제 위치 $x \in \Sigma_{\text{ret}}$ 마다 *다름* — fovea 에서는 cone-driven ON/OFF/color 가 풍부하나 rod-driven 채널 희소; periphery 에서는 반대

더 자연스러운 대상:

$$
\pi : E \longrightarrow \Sigma_{\text{ret}} \times \mathbb{R}^+, \quad \pi^{-1}(x, t) = F_{(x,t)}
$$

여기서 fiber $F_{(x,t)}$ 는 위치 $(x,t)$ 에서 *실제로 활성화된 채널들의 공간*. $F_{(x,t)}$ 는 위치마다 다름 (비균질 fiber). 각 kernel $\mathcal{K}_{2a/b/c/d}$ 는 *bundle morphism* (fiber-wise 작동).

*OP 의 핵심 질문*: 이 bundle 이 *trivial* ($E \cong \Sigma \times \mathcal{C}$) 인가, non-trivial 인가? Non-trivial 이라면 어떤 *transition function / structure group* 을 가지는가?

#### 2.3.2 문헌 지표

- **Husemoller, D. (1994)**. *Fibre Bundles*, 3rd ed. Springer. — fiber bundle 의 표준 정의 (§1–§3).
- **Massey, W.S. (1991)**. *A Basic Course in Algebraic Topology*. Springer. — associated bundle 구성.
- **Sternberg, S. (1964)**. *Lectures on Differential Geometry*. Prentice-Hall. — Lie group 의 representation 과 principal bundle.
- **Spillmann, L. & Werner, J.S. (eds., 1990)**. *Visual Perception: The Neurophysiological Foundations*. Academic Press. — 망막 채널의 위치 의존성 (fovea vs. periphery anatomy).
- **Dacey, D.M. (2004)**. "Origins of perception." *Trends in Neurosciences* 27, 401–406. — 망막 RGC type 의 공간 분포와 채널 mapping.

#### 2.3.3 후보 실험 / 수치 검증

A. **Triviality 검증**: $\Sigma_{\text{ret}}$ 을 적도-극 grid 로 이산화. 각 격자점의 fiber (활성 채널 집합) 를 해부학 데이터로 구성. transition map 의 *non-trivial holonomy* 계산.

B. **Morphism 호환성**: 현재 $\mathcal{K}_{2a}$ (ON/OFF split) 가 fiber-wise 로 작동하는지 확인 — 즉, $\mathcal{K}_{2a}$ 가 $\pi$ 와 commute 하는지 수치 구성.

C. **Sheaf cohomology 시험**: §2.3.1 의 bundle 을 sheaf 로 대체하고 $H^1$ 계산. 비자명 cohomology 가 *reconstruction obstruction* 을 주는지 확인 (→ OP-SP-005 와 연결).

#### 2.3.4 영향받는 TC-SP

- TC-SP-2.1 (Riesz 분해) — fiber 안의 lattice 구조
- TC-SP-5.2 (Tier 2 closure) — bundle 구조가 Tier 2 안에 머무는지

#### 2.3.5 의존성

- 영향: TC-SP-2.1 의 fiber-wise statement; OP-SP-005 (sheaf 가 비균질 표본화의 자연 도구)
- 의존: OP-SP-004 (색 대립의 group 이 fiber group 후보)

#### 2.3.6 PAI cross-link

간접: bundle 구조가 확립되면 $\mathcal{I}_{\text{perception}}(F)$ (PAI OP-PAI-001) 의 *domain* 이 bundle section 으로 자연스럽게 정의될 수 있다. 그러나 이 연결은 OP-SP-006 해결 이후의 문제이다.

**Blocking**: 본 OP 의 해결이 §4 의 형식적 깔끔함을 크게 개선. 후속 stage 진행에 *필수* 아님.

---

### OP-SP-004 — 색 대립의 군론적 정당화

**Status**: OPEN. Severity: **High**.

#### 2.4.1 완전 수학적 statement

[[04_stage2_inner_retinal_algebra#6.4|04 §6.4]] — 색 대립축 $L-M$, $S-(L+M)$, $L+M$ 이 *왜* 자연 축인가?

현재 설명의 형식적 구조: 색 응답 벡터 $\mathbf{r} = (r_L, r_M, r_S) \in \mathbb{R}^3$ 에 대해, opponent matrix

$$
A = \begin{pmatrix} 1 & -1 & 0 \\ 0 & -1 & 1 \\ 1 & 1 & 0 \end{pmatrix}
$$

(approximate; normalization 생략) 를 정의하면 대립 응답 $\mathbf{o} = A \mathbf{r}$ 가 된다. 그러나 *왜 이 $A$ 인가* 가 미결.

후보 정당화 1 — **통계적 (PCA)**:

자연 장면 스펙트럼 $s(\lambda)$ 의 공분산 행렬 $\Sigma_s$ 의 eigenvectors 가 시각 시스템의 대립 축과 정렬하는가? 즉:

$$
\Sigma_s \mathbf{v}_i = \lambda_i \mathbf{v}_i, \quad \mathbf{v}_i \approx \text{(luminance, R-G, B-Y axes)}
$$

Buchsbaum-Gottschalk (1983) 의 결과: 첫 3 PC 가 근사적으로 일치. 그러나 PCA 는 *선형 최적화* 이지 *필연적 수학적 구조* 가 아님.

후보 정당화 2 — **Decorrelation (정보 효율)**:

$L$ 과 $M$ cone 응답은 $\text{corr}(r_L, r_M) \approx 0.97$ (Atick-Redlich, 1990). 이 고상관을 제거하면 $L-M$ channel 이 자연스럽게 나타남:

$$
\text{If } \Sigma = \begin{pmatrix} \sigma^2 & \rho \sigma^2 \\ \rho \sigma^2 & \sigma^2 \end{pmatrix}, \quad \text{PCA eigenvectors} = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix}, \frac{1}{\sqrt{2}}\begin{pmatrix}1\\-1\end{pmatrix}
$$

이것이 $L+M$ (luminance) 와 $L-M$ (chrominance) 의 자연 도출.

후보 정당화 3 — **Lie group representation**:

색 공간이 $G$-symmetric ($G$ = some Lie group) 이고, 대립 채널이 $G$ 의 *irreducible representations* 로 분해? 후보:
- $G = SO(3)$: $\mathbf{r} \in \mathbb{R}^3$ 을 벡터 representation; 대립 = weight decomposition
- $G = SU(2)$: 2-cone system 의 경우; 3-cone 은 더 복잡
- $G = \mathbb{Z}_2 \times \mathbb{Z}_2$: ON/OFF × L-M 의 이산 군

*OP 의 핵심 질문*: PCA-기반 통계적 정당화를 *Lie group / representation theory 로 승격* 할 수 있는가? 또는 통계적 정당화가 원리적으로 충분한가?

#### 2.4.2 문헌 지표

- **Buchsbaum, G. & Gottschalk, A. (1983)**. "Trichromacy, opponent colours coding and optimum colour information transmission in the retina." *Proc. R. Soc. Lond. B* 220, 89–113. — 자연 광 PCA 와 trichromacy 의 첫 연결.
- **Atick, J.J. & Redlich, A.N. (1990)**. "Towards a theory of early visual processing." *Neural Computation* 2, 308–320. — decorrelation 가설; redundancy reduction.
- **Ruderman, D.L., Cronin, T.W. & Chiao, C.-C. (1998)**. "Statistics of cone responses to natural images: implications for visual coding." *J. Opt. Soc. Am. A* 15, 2036–2045. — LMS 응답의 자연 통계 empirical 분석.
- **Wyszecki, G. & Stiles, W.S. (1982)**. *Color Science*, 2nd ed. Wiley. — 색 공간의 수학적 기초; CIE, Munsell; color opponent mechanisms §7.
- **Webster, M.A. & Mollon, J.D. (1997)**. "Adaptation and the color statistics of natural images." *Vision Research* 37, 3283–3298. — 적응과 색 통계의 관계.
- **Maloney, L.T. (1986)**. "Evaluation of linear models of surface spectral reflectance with small numbers of parameters." *J. Opt. Soc. Am. A* 3, 1673–1683. — surface reflectance 의 basis decomposition.

#### 2.4.3 후보 실험 / 수치 검증

A. **PCA 정밀 정합도**: van Hateren (1997) natural image database 의 hyperspectral 데이터에서 LMS 공분산 행렬의 eigenvectors 를 계산. 대립 matrix $A$ 의 columns 와의 cosine similarity 수치 확인.

B. **대안 basis 비교**: 자연 통계에서 ICA (independent component analysis), NMF (nonneg. matrix factorization), sparse coding 으로 도출한 basis 가 PCA basis 와 얼마나 다른지 비교.

C. **Lie group 검정**: $SO(3)$ 의 표준 basis $(e_1, e_2, e_3)$ 와 색 대립 matrix $A$ 의 columns 의 *group-theoretic 관계* 계산. 색 공간 변환이 $SO(3)$ orbit 위에서 닫혀 있는지 확인.

D. **4-cone → 3-cone 대칭 파괴**: Tetrachromat (조류, 어류) 의 대립 구조 비교 — 3-cone 시스템의 $A$ 가 4-cone 의 *symmetry breaking projection* 으로 도출되는가?

#### 2.4.4 영향받는 TC-SP

- TC-SP-2.6 (Decorrelation optimality) — 본 OP 해결이 최적성 statement 의 강도 결정

#### 2.4.5 PAI cross-link

간접: 색 대립 구조의 군론적 정당화가 확립되면, 이 구조 위에서 $\mathcal{I}_{\text{perception}}(F)$ (PAI OP-PAI-001) 를 *색 공간의 표현론* 으로 정의할 가능성이 열린다. 그러나 현재는 OP-SP-006 해결이 선행 조건.

**Blocking**: 본 OP 가 High severity 이나 후속 stage 들에는 *영향 없음* — 색 채널을 *given* 으로 받고 진행 가능.

---

### OP-SP-005 — 비균질 표본화의 sheaf 처리

**Status**: OPEN. Severity: Medium.

#### 2.5.1 완전 수학적 statement

[[05_stage3_ganglion_spike_encoding#7.4|05 §7.4]] — 신경절세포 밀도 $\rho(p)$ 가 비균질:

$$
\rho(p) = \rho_0 \cdot \left(1 + \frac{e}{\varepsilon_{\frac{1}{2}}}\right)^{-2}, \quad e = \text{eccentricity}, \quad \rho_0 \approx 35{,}000 \text{ cells/mm}^2
$$

(Watson, 1992 의 근사식). Fovea ($e \approx 0$): $\rho \approx \rho_0$; periphery ($e = 50°$): $\rho \approx \rho_0 / 100$.

단순 density variation 모델: 각 위치 $p$ 에서의 *sampling coverage* 가 $\rho(p)$ 에 반비례. 이는 *재구성 한계* 를 Nyquist-like bound 로 정량화한다:

$$
\Delta_{\min}(p) \sim \frac{1}{\sqrt{\rho(p)}} \quad (\text{effective spatial resolution at } p)
$$

더 자연스러운 형식은 sheaf $\mathcal{F}$ 를 다음으로 정의:

$$
\mathcal{F}(U) := \{ \text{ganglion response configurations on } U \subset \Sigma_{\text{ret}} \}
$$

restriction maps $\rho_{UV} : \mathcal{F}(U) \to \mathcal{F}(V)$ (for $V \subset U$), gluing axiom.

*핵심 질문*: 이 sheaf 의 cohomology $H^0(\mathcal{F}), H^1(\mathcal{F})$ 가 어떤 *재구성 한계* 를 encode 하는가?

$H^1(\mathcal{F}) \neq 0$ 이면 *globally consistent section 이 존재하지 않을 수 있음* — 즉, 비균질 표본화로 인해 *전역적으로 일관된 perceptual reconstruction* 이 불가능한 영역이 존재.

#### 2.5.2 문헌 지표

- **Curry, J. (2014)**. *Sheaves, Cosheaves and Applications*. PhD Thesis, University of Pennsylvania. — discretized sheaves 의 topological signal processing 응용.
- **Robinson, M. (2014)**. *Topological Signal Processing*. Springer. — sheaf theory 의 신호 처리 응용; §4 에서 sampling lattice 의 sheaf model.
- **Ghrist, R. (2014)**. *Elementary Applied Topology*. Createspace. — constructible sheaves 와 Euler characteristic.
- **Watson, A.B. (1992)**. "A formula for the mean human optical modulation transfer function as a function of pupil size." *J. Opt. Soc. Am. A* 9, 1579–1597. — ganglion cell density formula.
- **Curcio, C.A. & Allen, K.A. (1990)**. "Topography of ganglion cells in human retina." *J. Comparative Neurology* 300, 5–25. — 상세 해부학적 density map.
- **Bredies, K. & Lorenz, D. (2018)**. *Mathematical Image Processing*. Springer. — non-uniform sampling 과 reconstruction bounds.

#### 2.5.3 후보 실험 / 수치 검증

A. **Nerve complex 구성**: Curcio-Allen (1990) 의 RGC density data 로 Vietoris-Rips complex 구성. 서로 다른 eccentricity band 에서의 $H^0, H^1$ 계산.

B. **Reconstruction bound 비교**: 단순 Nyquist bound ($\Delta_{\min}(p)$) vs. sheaf cohomology $H^1$ 가 주는 bound 의 수치 비교.

C. **Constructible sheaf**: $\Sigma_{\text{ret}}$ 를 eccentricity stratum (fovea / paracentral / periphery) 으로 stratify. 각 stratum 에서 constant sheaf, gluing map 에서의 restriction 호환성 확인.

#### 2.5.4 영향받는 TC-SP

- TC-SP-3.3 (Peripheral compression bound) — sheaf cohomology 가 재구성 가능성의 정량
- TC-SP-5.1 (σ propagation) — sheaf 구조가 σ 의 자연 ambient

#### 2.5.5 PAI cross-link

OP-SP-005 는 PAI 의 core OP 들과 직접 연결되지 않는다. 단, 재구성 한계의 sheaf-theoretic 정량화가 확립되면, PAI OP-PAI-001 ($\Delta_{\text{interp}}$ 의 domain) 를 *sheaf section 공간* 으로 잡는 것이 자연스러울 수 있다. 현재는 격리.

**Blocking**: 단순 density model 로도 working 가능. 해결이 *재구성 한계* 의 정확한 statement 를 가능케 함.

---

### OP-SP-006 — SCC $u_t$ ↔ which stage?

**Status**: OPEN. Severity: **High**.

#### 2.6.1 완전 수학적 statement

[[07_omega_sigma_lift#5.5|07 §5.5]] — SCC 의 primitive $u_t : X_t \to [0,1]$ 가 본 sensing pipeline 의 *어느 단계의 어떤 대상* 으로 식별되는가?

각 후보의 *형식적 명세*:

**후보 1 — Pre-Stage 0 (physical world cohesion)**:

$$
u_t : \Sigma_{\text{world}} \to [0,1], \quad u_t(x) = \text{(cohesion of scene at point } x \text{ at time } t)
$$

$X_t = \Sigma_{\text{world}}$ 는 장면의 물리적 공간. SCC = 세계 구조 이론. 감각 pipeline 은 $u_t$ 를 *추출하는 계산* 으로 해석.

**후보 2 — Stage 1–2 (retinal graded field)**:

$$
u_t(x) = \phi\bigl(V_p(x, t)\bigr) \in [0,1], \quad \phi : \mathbb{R} \to [0,1] \text{ (sigmoid normalization)}
$$

또는 특정 채널 $c^*$ 의 응답:

$$
u_t(x) = \frac{s_{c^*}(x, t)}{\sup_{x'} s_{c^*}(x', t)}, \quad s_{c^*} \in \mathcal{S}_2
$$

$X_t = \Sigma_{\text{ret}}$. SCC = retinal graded dynamics 이론.

**후보 3 — Stage 3 출력의 functional (post-encoding)**:

$$
u_t(x) = \phi\!\left( \sum_{c \in \mathcal{C}_g : p_c \approx x} \int_{t-\delta}^{t} dG_c(s) \cdot h(t-s)\right), \quad h : \mathbb{R}^+ \to \mathbb{R}^+ \text{ (smoothing kernel)}
$$

즉, spike train 의 spatially-smoothed rate field, normalize. SCC = post-encoding perceptual theory.

**후보 4 — Multi-instance (colimit)**:

$u_t^{(i)}$ 가 stage $i$ ($i = 1,2,3$) 각각에서 독립적으로 정의되고, 이들이 *homotopy / colimit* 구조를 통해 연결:

$$
u_t = \varinjlim_{i} u_t^{(i)}, \quad \text{via transition maps } \phi_i : u_t^{(i)} \to u_t^{(i+1)}
$$

*핵심 질문*: 이 네 후보 중 어느 것이 SCC 의 102 claims 와 *해석론적으로 가장 일관성 있는가*? 특히 4 energy term

$$
E = \lambda_{\text{cl}} E_{\text{cl}} + \lambda_{\text{sep}} E_{\text{sep}} + \lambda_{\text{bd}} E_{\text{bd}} + \lambda_{\text{tr}} E_{\text{tr}}
$$

이 어느 stage 의 물리량으로 *잘 정의* 되는가?

검증 수단 (후보 실험 §2.6.3 참조): 각 stage 의 시뮬레이션 출력에서 $u_t$ 를 구성하고, SCC diagnostic vector $d = (\text{Bind, Sep, Inside, Persist})$ 를 계산하여 어느 stage 에서 *가장 semantically meaningful* 한 값이 나오는지 비교.

#### 2.6.2 문헌 지표

- **SCC canonical.md (CV-1.13)**. `THEORY/2_substrate/canonical/canonical.md`. — $u_t$ 의 공리적 정의 (Axioms A1-A3), 4 energy term, diagnostic vector.
- **DECLARATION.md (DECL-1.0, 2026-05-07)**. `THEORY/0_axis/DECLARATION.md`. — "어떤 차이의 덩어리가 언제부터 하나의 객체가 되는가?" 의 원점. $u_t$ = primitive.
- **Koenderink, J.J. & van Doorn, A.J. (1992)**. "Generic neighborhood operators." *IEEE TPAMI* 14, 597–605. — graded saliency field 의 retinal basis 논의.
- **Marr, D. (1982)**. *Vision*. Freeman. — primal sketch, 2.5D sketch — Stage 2 출력 수준에서의 형식; SCC 와의 대조.
- **Grossberg, S. (1994)**. "3-D vision and figure-ground separation by visual cortex." *Perception & Psychophysics* 55, 48–121. — cortical filling-in 과 graded field 의 동역학.

#### 2.6.3 후보 실험 / 수치 검증

A. **Stage-wise $u_t$ 구성 및 diagnostic 비교**: 단순 장면 (원형 patch on uniform background) 을 시뮬레이션. Stage 1, 2, 3 출력 각각에서 $u_t$ 를 후보 1–3 의 방식으로 구성. 각 $u_t$ 에 대해 $\text{Bind}, \text{Sep}, \text{Inside}, \text{Persist}$ 계산. 어느 stage 에서 가장 sensible (high Bind, reasonable Sep) 한 값이 나오는가?

B. **Phase transition 검증**: 각 stage 의 $u_t$ 에서 *spinodal condition* $\beta/\alpha > 4\lambda_2 / |W''(c)|$ 가 성립하는가? Stage 에 따라 phase transition 여부가 다른가?

C. **Transport term 유의미성**: $E_{\text{tr}}$ (Wasserstein transport) 가 어느 stage 에서 가장 자연스럽게 정의되는가 — Stage 2 의 graded field 간 Wasserstein, vs. Stage 3 의 spike train 간 optimal transport (Thorpe 2019).

#### 2.6.4 영향받는 TC-SP

- TC-SP-5.1 (σ propagation) — $u_t$ 가 어느 stage 에 있는가에 따라 σ 흐름의 해석 다름
- TC-SP-5.2 (Tier 2 closure) — $u_t$ 가 만약 outside pipeline 이면 closure 가 enriched
- SCC 의 전체 framework 의 위상 결정

#### 2.6.5 PAI cross-link (핵심)

**직접 연결 — 가장 강한 PAI cross-link**:

- **OP-PAI-001** ($\Delta_{\text{interp}}$ 의 수학적 정의) 은 $\mathcal{I}_{\text{perception}}(F)$ 를 요구한다. $\mathcal{I}_{\text{perception}}(F)$ 는 "F 의 perceptual individuation" — 이것이 정확히 $u_t$ 로부터 파생되는 형식이다. 따라서 **OP-SP-006 의 해결이 OP-PAI-001 의 필요 전제**:

$$
\text{OP-SP-006 RESOLVED} \implies \mathcal{I}_{\text{perception}}(F) \text{ 정의 가능} \implies \text{OP-PAI-001 진척 가능}
$$

- **OP-PAI-002** ($\mathcal{A}(u)$ — action interpretation map): $\mathcal{A}(u)$ 의 domain 이 $u_t$ 이다. $u_t$ 가 어느 stage 에 있는가에 따라 $\mathcal{A}(u)$ 의 구체적 형태 (retinal field level vs. spike rate level vs. cortical level) 가 완전히 달라진다.

*순서*: **OP-SP-006 → OP-PAI-001 → OP-PAI-002** 가 critical dependency chain.

**Blocking**: 본 OP 의 해결 없이 PAI 와의 다리 구축 *불가능*. 본 디렉토리의 가장 중요한 OP.

---

### OP-SP-007 — Stage 4 cut location

**Status**: OPEN. Severity: Medium.

#### 2.7.1 완전 수학적 statement

[[05_stage3_ganglion_spike_encoding#11.|05 §11]] — 본 디렉토리는 Stage 4 를 *시신경 optic nerve head 도착 직후* 로 default 설정:

$$
\Omega_4 = \Omega_3 \text{ with } t \to t + \tau_{\text{latency}}(c)
$$

이 cut 은 *임의적*이다. 두 자연스러운 대안:

**대안 A — LGN (외측슬상핵) 까지 포함**:

LGN relay 에서 추가되는 가공:
- *M/P/K pathway 의 thalamic gate*: 각 layer 의 gain control
- *Attentional modulation*: corticothalamic feedback 에 의한 gain (Sherman-Guillery, 2002)
- *Push-pull RF*: LGN 의 center-surround 가 retinal RF 를 refinement

추가 kernel $\mathcal{K}_4^{\text{LGN}} : \mathcal{S}_3 \to \mathcal{S}_4^{\text{LGN}}$ 이 필요:

$$
\mathcal{S}_4^{\text{LGN}} := \prod_{l \in \{M_p, M_m, P_p, P_m, K\}} \mathcal{N}(\mathbb{R}^+) \times \text{(gain state)}
$$

**대안 B — V1 입력까지 포함**:

V1 simple cells 의 orientation tuning, ocular dominance columns 까지 포함:

$$
\mathcal{S}_4^{\text{V1}} := C(\Sigma_{\text{V1}} \times \mathbb{R}^+ \times S^1 \times \{L, R\}, \mathbb{R}^+)
$$

$S^1$: orientation. $\{L, R\}$: eye of origin.

*OP 의 핵심 질문*: cut location 이 TC-SP 의 *정량적 예측* 에 어떤 영향을 주는가? 특히 TC-SP-3.2 (latency asymmetry) 의 수치가 LGN delay (약 10ms 추가) 포함 시 얼마나 변하는가?

#### 2.7.2 문헌 지표

- **Sherman, S.M. & Guillery, R.W. (2001)**. *Exploring the Thalamus*. Academic Press. — LGN relay 의 기능적 구조; thalamic gate 메커니즘.
- **Bear, M.F., Connors, B.W. & Paradiso, M.A. (2015)**. *Neuroscience: Exploring the Brain*, 4th ed. — LGN 의 M/P/K layer anatomy 와 cortical projections (§12).
- **Hubel, D.H. & Wiesel, T.N. (1962)**. "Receptive fields, binocular interaction and functional architecture in the cat's visual cortex." *J. Physiology* 160, 106–154. — V1 의 첫 체계적 기술; simple/complex cell 정의.
- **Maunsell, J.H.R. & Gibson, J.R. (1992)**. "Visual response latencies in striate cortex of the macaque monkey." *J. Neurophysiology* 68, 1332–1344. — M/P 경로 latency 수치 ($M \approx 30\text{ ms}$, $P \approx 50\text{ ms}$ from retina to V1).
- **Dacey, D.M. (2000)**. "Parallel pathways for spectral coding in primate retina." *Annual Review of Neuroscience* 23, 743–775. — M/P/K pathway 의 retina-to-LGN connectivity.

#### 2.7.3 후보 실험 / 수치 검증

A. **Latency 재계산**: LGN delay (약 4–8 ms 추가) 포함 시 TC-SP-3.2 의 M-P latency asymmetry 수치가 얼마나 변하는지 계산.

B. **Information bound 재계산**: LGN 의 corticothalamic feedback 이 채널 capacity $C(\mathcal{K}_4)$ 에 미치는 영향 추정 (feedback 의 이론적 gain 범위 사용).

C. **Modular decomposition 타당성**: LGN 을 독립 stage 로 분리하면 *현재 TC-SP 들의 statement 가 변경 없이 유지되는가* 확인.

#### 2.7.4 영향받는 TC-SP

- TC-SP-3.2 (latency asymmetry) — LGN 의 추가 지연이 alignment 문제의 정량 변경
- TC-SP-4.1 (end-to-end bound) — 어디까지를 receiver 로 보는가에 따라 bound 다름

#### 2.7.5 PAI cross-link

**중간 강도 연결**: PAI 는 "perception 이 action-addressable unit 을 생성한다"고 가정한다. 이 unit 의 *신경 기질* 이 어디에 있는가 — retinal spikes, LGN relayed spikes, V1 orientation map — 가 PAI Phase 5 (구체적 action connection; `PAI_ROADMAP.md` 참조) 의 시작점을 결정한다.

- LGN cut → action-addressable unit 이 LGN output spike stream
- V1 cut → action-addressable unit 이 orientation-tuned cortical response

*순서*: **OP-SP-007 → PAI Phase 5 시작점** 이 자연스러운 progression.

**Blocking**: 본 OP 의 해결이 PAI 와의 다리 작업의 시작점 결정. PAI 가 가정하는 "perceptual unit" 의 신경 substrate 확정.

---

### OP-SP-008 — Orientation 채널 (4 방향) 군론적 정당화

**Status**: OPEN. Severity: Medium.

#### 2.8.1 완전 수학적 statement

[[04_stage2_inner_retinal_algebra#4.10|04 §4.10]] — DSGC 의 4 기본 방향 $\theta_k = k\pi/4$ ($k = 0,1,2,3$) 이 *왜 4* 이고 *왜 이 각도들* 인가?

형식적으로: motion 에너지 표현에서 orientation selectivity 는

$$
R_\theta(x, t) = \left| \int \! g_e(x', t') s(x - x'\cos\theta, t - t') \,dx'\,dt' + i \int \! g_o(x', t') s(x - x'\cos\theta, t - t') \,dx'\,dt' \right|^2
$$

($g_e, g_o$: even/odd Gabor filter pair; Adelson-Bergen, 1985). 실제 pipeline 에서는 $\theta$ 가 이산적으로 선택됨.

**군론적 틀**: $SO(2)$ 의 *유한 부분군* $C_n$ ($n$-fold rotation) 중 $n = 4$ (즉 $C_4$) 를 망막이 선택한 것으로 볼 수 있는가?

$C_4$ 는 $SO(2)$ 의 실 representation:

$$
\rho : C_4 \to GL(2, \mathbb{R}), \quad \rho(k) = \begin{pmatrix} \cos(k\pi/2) & -\sin(k\pi/2) \\ \sin(k\pi/2) & \cos(k\pi/2) \end{pmatrix}
$$

이 representation 의 *복소 eigenspace* 는 $e^{i \cdot 0}, e^{i\pi/2}, e^{i\pi}, e^{i3\pi/2}$ — 즉 4 방향.

**cortical boost 질문**: V1 은 *continuous orientation map* (pinwheel structure) 를 가진다. Retinal $C_4$ (4-fold discrete) 에서 V1 $SO(2)$ (continuous) 로의 *전이* 가 어떤 수학적 메커니즘으로 일어나는가?

후보: 
- *Interpolation*: $C_4$ 의 4 채널이 선형 보간으로 continuous coverage 제공
- *Cortical completion*: V1 의 recurrent dynamics 가 $C_4$ input 을 $SO(2)$ map 으로 확장
- *Evolutionary bootstrap*: $C_4$ 가 V1 pinwheel 의 초기 scaffold

#### 2.8.2 문헌 지표

- **Hubel, D.H. & Wiesel, T.N. (1962)**. "Receptive fields, binocular interaction and functional architecture in the cat's visual cortex." *J. Physiology* 160, 106–154. — orientation selectivity 의 최초 기술; 4축 구조 언급.
- **Adelson, E.H. & Bergen, J.R. (1985)**. "Spatiotemporal energy models for the perception of motion." *J. Opt. Soc. Am. A* 2, 284–299. — motion energy model; even/odd filter pair.
- **Reichardt, W. (1961)**. "Autocorrelation, a principle for the evaluation of sensory information by the central nervous system." In: *Sensory Communication*, MIT Press. — motion detection model.
- **Blasdel, G.G. (1992)**. "Orientation selectivity, preference, and continuity in monkey striate cortex." *J. Neuroscience* 12, 3139–3161. — V1 pinwheel map 의 optical imaging.
- **Petitot, J. (2008)**. *Neurogéométrie de la vision*. Editions de l'Ecole Polytechnique. — V1 의 orientation map 의 differential geometry; contact structure.
- **Serres, M. (1990)**. *Le contrat naturel*. — 진화적 contingency 의 철학적 논의 (참조용).

#### 2.8.3 후보 실험 / 수치 검증

A. **$C_4$ vs $C_8$ sampling**: 4 방향 vs. 8 방향 orientation sampling 으로 자연 image 의 motion energy 를 계산. Reconstruction error 비교 — $n = 4$ 가 *충분* 한가?

B. **Cortical interpolation 시뮬레이션**: $C_4$ input 을 V1 recurrent network (rate model, 2D ring attractor) 에 투영. continuous orientation tuning curve 가 emergence 하는지 시뮬레이션.

C. **Starburst amacrine geometry**: 실제 starburst amacrine 의 dendritic tree 기하학 (4-fold 대칭 보고 다수) 에서 $C_4$ 구조가 anatomical 하게 필연적인지 확인.

#### 2.8.4 영향받는 TC-SP

- TC-SP-2.4 (velocity-tuned slab) — 4 방향 sampling 의 Nyquist-like 조건
- TC-SP-2.5 (Reichardt ≡ energy)

#### 2.8.5 PAI cross-link

간접: orientation tuning 의 군론적 정당화가 확립되면, 행동 공간 (grasping, reaching) 의 방향 구조와 retinal orientation 채널의 대응이 PAI OP-PAI-003 (interpretation invariance criterion) 의 *구체 사례* 로 분석될 수 있다. 현재는 격리.

**Blocking**: 본 OP 의 해결이 V1 의 cortical orientation column 으로의 연결을 정당화. 본 디렉토리 진행에는 필수 아님.

---

### OP-SP-009 — 적응 시상수 hierarchy

**Status**: OPEN. Severity: Medium.

#### 2.9.1 완전 수학적 statement

[[03_stage1_photoreceptor_sde#4.3|03 §4.3]] — 적응이 *multiple* time scales 로 이루어짐. OP-SP-002 (Naka-Rushton 단일 시상수) 의 *자연 확장*이자 독립 OP.

다중 시상수의 스펙트럼을 *측도* 로 표현하면:

$$
I_{50}^{\text{eff}}(t) = \int_0^\infty k(\tau) \left[ \int_0^\infty e^{-s/\tau} I(t-s)\,ds \right] d\tau
$$

$k(\tau) \geq 0$: 시상수 스펙트럼 (weight distribution over timescales).

- *단일 시상수* (OP-SP-002): $k(\tau) = \delta(\tau - \tau_a)$
- *유한 몇 개의 시상수*: $k(\tau) = \sum_j w_j \delta(\tau - \tau_j)$
- *연속 스펙트럼*: $k(\tau) = c \cdot \tau^{-\alpha}$ (power-law; $1/f$-like)

*OP 의 핵심 질문*: 실제 망막 적응의 $k(\tau)$ 가 *이산 합* 인가 *연속 power-law* 인가? 그리고 각 시상수가 *독립 상태변수* 인가, *공통 dynamical variable 의 different time projections* 인가?

#### 2.9.2 문헌 지표

- **Smirnakis, S.M. et al. (1997)**. "Adaptation of retinal processing abolishes stable colour appearance." *Nature* 386, 671–674. — 수초-수분 multi-timescale 적응의 실증.
- **Wark, B., Lundstrom, B.N. & Fairhall, A. (2007)**. "Sensory adaptation." *Current Opinion in Neurobiology* 17, 423–429. — multi-timescale 적응의 리뷰; $1/f$ kernel 제안.
- **Drew, P.J. & Abbott, L.F. (2006)**. "Models and properties of power-law adaptation in neural systems." *J. Neurophysiology* 96, 826–833. — power-law adaptation 의 computational model.
- **Fain, G.L. et al. (2001)**. "Adaptation in vertebrate photoreceptors." *Physiological Reviews* 81, 117–151. — 분자 레벨의 adaptation mechanism 총람.
- **Baccus, S.A. & Meister, M. (2002)**. "Fast and slow contrast adaptation in retinal circuitry." *Neuron* 36, 909–919. — 빠른(50 ms)·느린(8 s) 적응의 구별; 두 시상수 모델.

#### 2.9.3 후보 실험 / 수치 검증

A. **ERG/retinal recording fitting**: 4 시상수 모델 vs. power-law $k(\tau) \propto \tau^{-0.5}$ 를 실측 adaptation curve (예: Baccus-Meister 2002 data) 에 fit. 잔차 비교.

B. **Information 최적 시상수**: natural scene temporal statistics (van Hateren 1997) 에서 *mutual information 최대화* 관점에서 optimal $k(\tau)$ 를 analytic 또는 numeric 으로 도출. 실제 시상수 spectrum 과 비교.

C. **Self-organized criticality 검정**: 적응 power spectrum 이 $1/f$ 형태인지 long-duration retinal recording data 분석.

#### 2.9.4 영향받는 TC-SP

- TC-SP-1.4 (compression) — 다중 시상수가 contrast adaptation 의 시간 형식
- TC-SP-4.3 (Naka-Rushton optimality) — multi-scale adaptation 이 어떤 시간 windows 에서 정보 최대화

#### 2.9.5 PAI cross-link

간접: multi-timescale adaptation 이 *action-relevant* timescale 에서 지각 단위의 안정성을 결정할 수 있다. PAI OP-PAI-002 ($\mathcal{A}(u)$) 가 시간 축 action (순간적 grasp vs. sustained navigation) 을 포함할 경우, 적응 timescale hierarchy 가 action-relevant temporal window 를 설정한다. 그러나 현재는 격리.

**Blocking**: 해결이 *long-term plasticity / learning* 과의 연결을 가능케 함. 본 디렉토리에는 필수 아님.

---

### OP-SP-010 — Top-down feedback 무시 정당화

**Status**: OPEN. Severity: Low.

#### 2.10.1 완전 수학적 statement

[[01_framework_master#TC-SP-1.3|01 TC-SP-1.3]] — 본 디렉토리의 kernel chain $\mathcal{K}_1 \circ \mathcal{K}_2 \circ \mathcal{K}_3$ 가 *strictly causal (forward)* 임을 가정:

$$
\mathcal{S}_0 \xrightarrow{\mathcal{K}_1} \mathcal{S}_1 \xrightarrow{\mathcal{K}_2} \mathcal{S}_2 \xrightarrow{\mathcal{K}_3} \mathcal{S}_3
$$

feedback 없음. 그러나 실제 시각 시스템은 *역방향 연결* 을 가진다:

- *Corticothalamic feedback* (V1 → LGN): 약 $10^8$ 개 synapses — LGN 의 $10^7$ 개 thalamocortical 보다 10배 많음 (Sherman-Guillery)
- *Centrifugal fibers* (brain → retina): 수 천 개 (조류에서 풍부; 포유류에서 제한적)
- *Lateral inhibition* (amacrine, horizontal cells): stage 2 내부의 *같은 stage* feedback

형식적으로: feedback 있는 pipeline 은

$$
\mathcal{S}_0 \rightleftharpoons \mathcal{S}_1 \rightleftharpoons \mathcal{S}_2 \rightleftharpoons \mathcal{S}_3
$$

이 되어 *bidirectional kernel* $(\mathcal{K}_i, \mathcal{K}_i^{\text{back}})$ 의 쌍이 필요하고, steady-state 가 *fixed point* 조건을 만족해야 한다:

$$
\mathcal{S}_i^* = \mathcal{K}_i\!\left(\mathcal{S}_{i-1}^*\right) \circ \mathcal{K}_i^{\text{back}}\!\left(\mathcal{S}_{i+1}^*\right)
$$

이 조건을 무시하는 것이 TC-SP-1.3 의 가정. 정당화 요건:

$$
\|\mathcal{K}_i^{\text{back}}\| \ll \|\mathcal{K}_i^{\text{fwd}}\| \quad \text{(feedback strength negligible)}
$$

또는 feedback 이 *slow* 여서 pipeline 의 fast forward pass 에 영향 없음.

#### 2.10.2 문헌 지표

- **Sherman, S.M. & Guillery, R.W. (2002)**. "The role of the thalamus in the flow of information to the cortex." *Phil. Trans. R. Soc. Lond. B* 357, 1695–1708. — corticothalamic feedback 의 anatomical scale; V1→LGN 연결의 정량.
- **Reynolds, J.H. & Heeger, D.J. (2009)**. "The normalization model of attention." *Neuron* 61, 168–185. — top-down attention 의 normalization model; pipeline 의 gain control 로 흡수 가능.
- **Bastos, A.M. et al. (2012)**. "Canonical microcircuits for predictive coding." *Neuron* 76, 695–711. — predictive coding framework; feedback = prediction signal.
- **Rao, R.P. & Ballard, D.H. (1999)**. "Predictive coding in the visual cortex." *Nature Neuroscience* 2, 79–87. — V1 에서의 predictive coding; top-down = prior; bottom-up = prediction error.
- **Carandini, M. & Heeger, D.J. (2012)**. "Normalization as a canonical neural computation." *Nature Reviews Neuroscience* 13, 51–62. — divisive normalization 이 feedback 효과를 흡수하는 메커니즘.

#### 2.10.3 후보 실험 / 수치 검증

A. **Feedback strength 정량화**: LGN 에서의 corticothalamic synaptic weight 비율 (형태학 데이터) 로부터 feedback 의 effective gain estimate. 이 값이 "무시 가능" 기준 ($< 5\%$) 이하인지 확인.

B. **Normalization 흡수**: Reynolds-Heeger (2009) normalization model 에서 top-down gain 을 OP-SP-009 의 *slow adaptation* 으로 reparametrize 가능한지 형식적 확인.

C. **Predictive coding 프레임 비교**: Rao-Ballard (1999) 모델을 현재 SSKP 에 적용. feedback = prediction, forward = error 프레임이 TC-SP 들과 *모순 없이* 병존 가능한지 확인.

#### 2.10.4 영향받는 TC-SP

- TC-SP-1.3 (causal time-ordering) — feedback 이 strictly forward 가정을 기술적으로 위반

#### 2.10.5 PAI cross-link

PAI 의 §2 (Core Thesis) 는 "perception must produce the same unit that action can act upon" 을 가정한다. Top-down feedback (attention, expectation) 이 이 unit 의 형성에 *action-relevant context* 를 제공하는 경우, OP-SP-010 의 해결이 PAI OP-PAI-006 (Formation-to-affordance bridge) 의 *context dependency* 측면과 연결될 수 있다. 그러나 현재는 격리.

**Blocking**: negative 해결 (feedback 무시 정당화) 이면 본 디렉토리 작업 안전. positive 해결 이면 SSKP 형식 자체의 non-causal extension 필요.

---

## 3. Meta Open Problems (본 문서에서 등록)

### OP-SP-M1 — 순수 Tier 2 boundaries 의 필연성

**Status**: OPEN. Severity: Low (technical, philosophical).

#### 3.1.1 완전 수학적 statement

[[07_omega_sigma_lift#7. Stage 별 Tier 2 순도|07 §7]] 에서 관찰:

| Stage | (Ω, σ) type | Tier 2 순도 |
|-------|------------|------------|
| 0 | 점과정 (atomic) | 순수 Tier 2 |
| 1 | graded field + type mark | Tier 2 + 1-mark |
| 2 | multichannel graded | Tier 2 + value attachment + cross-channel σ |
| 3 | 점과정 (spike) | 순수 Tier 2 회복 |

패턴: 입력 boundary (Stage 0) 와 출력 boundary (Stage 3) 가 *순수 Tier 2*; 내부 processing (Stage 1-2) 가 *enriched*.

*핵심 질문*: 이 boundary-purity, interior-enrichment 패턴이 *필연적* 인가?

형식화 후보: 임의의 multi-stage Markovian pipeline $\mathcal{S}_0 \to \mathcal{S}_1 \to \cdots \to \mathcal{S}_n$ 에서, 다음이 성립하는가?

$$
\text{If } \mathcal{S}_0, \mathcal{S}_n \text{ are pure Tier 2, and DPI holds, then } \mathcal{S}_1, \ldots, \mathcal{S}_{n-1} \text{ require enrichment.}
$$

이 주장이 참이면 *정보론적 필연* (enrichment = information capacity); 거짓이면 *진화적 우연*.

#### 3.1.2 문헌 지표

- **Tishby, N., Pereira, F.C. & Bialek, W. (1999)**. "The information bottleneck method." *arXiv:physics/0004057*. — information bottleneck; 중간 representation 이 DPI 를 만족하며 enrichment 를 요구하는 조건.
- **Cover, T.M. & Thomas, J.A. (2006)**. *Elements of Information Theory*, 2nd ed. — DPI theorem (§2.8).

#### 3.1.3 PAI cross-link

직접 연결 없음. 단, PAI 의 substrate-canonical 구조 (SCC 가 Tier 2 이상의 enrichment 를 가지는 기초) 와 철학적으로 연결.

---

### OP-SP-M2 — σ-pushforward 의 deterministic vs probabilistic

**Status**: OPEN. Severity: Low.

#### 3.2.1 완전 수학적 statement

[[07_omega_sigma_lift#3.4|07 §3.4]] — 본 디렉토리는 σ 를 *binary* (deterministic) 로 유지:

$$
\sigma_i(y_1, y_2) \in \{0, 1\}
$$

그러나 kernel $\mathcal{K}_i$ 가 *stochastic* 이라면 pushforward σ 가 자연스럽게 *probabilistic* 이 된다:

$$
\sigma_i^{\text{prob}}(y_1, y_2) := P\!\big(\exists x_1, x_2 \in \Omega_{i-1} : \sigma_{i-1}(x_1, x_2) = 1 \text{ AND } y_1 \sim \mathcal{K}_i(x_1), y_2 \sim \mathcal{K}_i(x_2)\big)
$$

이 *graded similarity* 는 "Tier 2.5" — Tier 2 (binary) 와 Tier 3 (metric) 사이의 hybrid.

*핵심 질문*: binary σ 고수가 이론적으로 올바른가, 또는 probabilistic σ 로의 전환이 더 자연스러운가? 전환 시 어떤 구조가 추가되는가?

#### 3.2.2 문헌 지표

- **Chung, F.R.K. (1997)**. *Spectral Graph Theory*. AMS. — 그래프 σ 의 spectral 표현; 가중 그래프로의 자연 일반화.
- **Zadeh, L.A. (1965)**. "Fuzzy sets." *Information and Control* 8, 338–353. — fuzzy membership function; [0,1]-valued σ 의 선구.

#### 3.2.3 PAI cross-link

간접: probabilistic σ 가 도입되면 $\Delta_{\text{interp}}(F)$ (PAI OP-PAI-001) 의 정의가 *expected discrepancy* 형태로 자연화된다. 현재는 격리.

---

### OP-SP-M3 — SCC parallel (E_cl/sep/bd/tr ↔ stage 2 측면) 의 본질

**Status**: OPEN. Severity: Medium.

#### 3.3.1 완전 수학적 statement

[[06_endtoend_information_bound#7. SCC 의 E_cl, E_sep, E_bd 와의 candidate 연결|06 §7]] — SCC 의 4 energy term 과 stage 2 의 4 computational 측면 사이의 형식적 유사:

| SCC term | Stage 2 측면 | 형식 |
|----------|------------|------|
| $E_{\text{cl}}(u) = \frac{\lambda_{\text{cl}}}{2} u^\top L u$ (closure) | DoG center-surround integration | Laplacian smoothing |
| $E_{\text{sep}}(u) = \lambda_{\text{sep}} \sum_i W'(u_i)$ (separation) | ON/OFF Riesz lattice 분해 | double-well potential |
| $E_{\text{bd}}(u) = \lambda_{\text{bd}} \sum_{ij} |u_i - u_j|^2$ (boundary) | DoG zero-crossing edge detection | gradient-based |
| $E_{\text{tr}}(u, v) = \lambda_{\text{tr}} W_2(u, v)$ (transport) | spike train Wasserstein distance | optimal transport |

이 매핑이 형식적으로 더 강한 주장으로 승격될 수 있는가?

후보 주장 (unverified):
$$
\exists \Phi : \mathcal{S}_2 \to \Sigma_m, \quad E_{\text{SCC}}(\Phi(s)) = f\!\big(E_{\text{stage2}}(s)\big) \quad \forall s \in \mathcal{S}_2
$$

즉, stage 2 의 computational object 가 SCC energy landscape 와 *isomorphic* 인 공간으로 map 되는가?

이것이 OP-SP-006 (SCC u_t 위치) 의 *evidence* 를 제공할 수 있다: 만약 SCC energy 가 stage 2 에서 자연스럽게 정의된다면, $u_t$ = stage 2 의 graded field 가 강력한 후보.

#### 3.3.2 문헌 지표

- **SCC canonical.md (CV-1.13)**. 4 energy term 의 정확한 정의.
- **Koenderink, J.J. (1984)**. "The structure of images." *Biological Cybernetics* 50, 363–370. — scale-space theory; Laplacian as diffusion = closure energy 유사.
- **Villani, C. (2009)**. *Optimal Transport: Old and New*. Springer. — $W_2$ 의 정확한 정의; transport energy 의 수학.

#### 3.3.3 PAI cross-link

**직접 연결 (중간 강도)**: OP-SP-M3 의 해결 (SCC energy = stage 2 의 어떤 functional) 이 확립되면, PAI OP-PAI-002 ($\mathcal{A}(u)$ 정의) 의 domain 을 stage 2 graded field 로 구체화하는 경로가 열린다. 즉:

$$
\text{OP-SP-M3 RESOLVED} + \text{OP-SP-006 RESOLVED} \implies \mathcal{A}(u) \text{ 의 Stage 2 anchoring 가능}
$$

---

### OP-SP-M4 — Free-energy principle 의 채택 / 거부 기준

**Status**: OPEN. Severity: Low (philosophical / methodological).

#### 3.4.1 완전 수학적 statement

[[06_endtoend_information_bound#6.2 본 디렉토리의 입장|06 §6.2]] — 본 디렉토리는 FEP 를 *cited but not adopted*. FEP 의 핵심:

$$
\mathcal{F}[q] := \underbrace{\mathbb{E}_q[\log q(\phi) - \log p(\phi, o)]}_{\text{variational free energy}} = \underbrace{\mathbb{E}_q[\log q(\phi)] - \mathbb{E}_q[\log p(\phi|o)]}_{\text{KL}} - \log p(o)
$$

$\phi$: internal state (causes), $o$: observations. FEP 는 "$\mathcal{F}$ 를 minimize 하는 것이 perception 이다" 를 주장.

*채택 기준 후보*:

1. FEP 의 $\mathcal{F}$ 가 SCC 의 $E = \lambda_{\text{cl}} E_{\text{cl}} + \lambda_{\text{sep}} E_{\text{sep}} + \lambda_{\text{bd}} E_{\text{bd}} + \lambda_{\text{tr}} E_{\text{tr}}$ 와 *동치 또는 dominant* 임이 입증될 때.

2. FEP 가 PAI OP-PAI-002 ($\mathcal{A}(u)$) 의 *자연해* — 즉, $\mathcal{A}(u)$ 가 free energy 의 action component 로 정의될 때.

3. FEP 가 TC-SP-4.3 (Naka-Rushton optimality) 의 *제일 원리 도출* 을 가능케 할 때.

*거부 기준*:

1. SCC 의 4 energy term 이 FEP 의 $\mathcal{F}$ 로 환원되지 않음 — 독립적 구조 유지.

2. FEP 가 망막 수준 ($\mathcal{S}_0 \to \mathcal{S}_3$) 에서 *테스트 가능한 예측* 을 내놓지 못할 때.

#### 3.4.2 문헌 지표

- **Friston, K. (2010)**. "The free-energy principle: a unified brain theory?" *Nature Reviews Neuroscience* 11, 127–138. — FEP 의 주요 리뷰.
- **Bogacz, R. (2017)**. "A tutorial on the free-energy framework for modelling perception and learning." *J. Mathematical Psychology* 76, 198–211. — FEP 의 수학적 구현.
- **Biehl, M. et al. (2021)**. "Expanding the active inference landscape: more intrinsic motivations in the perception-action loop." *Frontiers in Neurorobotics* 15. — FEP 비판과 한계 분석.

#### 3.4.3 PAI cross-link

중간 강도: FEP 가 채택되면 PAI OP-PAI-003 (interpretation invariance criterion) 의 *candidate form 2* (commutativity: $\mathcal{A} \circ \mathcal{P} = \mathcal{P} \circ \mathcal{A}'$) 가 active inference 의 자연 언어로 번역된다. 그러나 채택 전에는 격리.

---

## 4. 의존성 그래프 (확장)

OP 사이의 *blockage / advancement* 관계 (상세 버전):

```
OP-SP-001 (coherence / Poisson)
    ─── isolated: affects only TC-SP-0.1, 0.2
    ─── no downstream blockage

OP-SP-002 (Naka-Rushton adaptation, single τ)
    ──→ TC-SP-1.4 (compression)
    ──→ TC-SP-4.3 (optimality)
    ──→ OP-SP-009 (extension: adaptation hierarchy)
         ──→ TC-SP-1.4, TC-SP-4.3 (quantitative refinement)
         ──→ OP-SP-010 (slow feedback absorbed in adaptation)

OP-SP-003 (fiber bundle formalism)
    ←── OP-SP-004 (color group = fiber structure group candidate)
    ──→ OP-SP-005 (sheaf as natural tool for non-uniform fibers)
    ──→ TC-SP-2.1 (fiber-wise Riesz)
    ──→ TC-SP-5.2 (Tier 2 closure with bundle)

OP-SP-004 (color opponency group-theoretic)
    ─── inputs to: OP-SP-003 (fiber group)
    ──→ TC-SP-2.6 (decorrelation optimality strength)

OP-SP-005 (sheaf for non-uniform sampling)
    ←── OP-SP-003 (fiber compatibility)
    ──→ TC-SP-3.3 (peripheral compression bound)
    ──→ TC-SP-5.1 (σ propagation ambient)

OP-SP-006 (SCC u_t stage identification) ═══ CRITICAL
    ──→ PAI OP-PAI-001 (Δ_interp definition; u_t = I_perception substrate)
    ──→ PAI OP-PAI-002 (A(u) domain specification)
    ──→ OP-SP-M3 (SCC parallel as evidence)
    ──→ TC-SP-5.1 (σ interpretation)
    ──→ TC-SP-5.2 (Tier 2 closure enrichment)
    Evidence from: OP-SP-M3, OP-SP-007

OP-SP-007 (Stage 4 cut location)
    ←── OP-SP-006 (u_t location changes what Stage 4 means)
    ──→ PAI Phase 5 (action connection starting point)
    ──→ TC-SP-3.2 (latency asymmetry numerical value)
    ──→ TC-SP-4.1 (end-to-end bound with/without LGN)

OP-SP-008 (orientation 4 channels, group-theoretic)
    ←── OP-SP-004 (parallel question; both ask "why these axes?")
    ──→ TC-SP-2.4 (velocity-tuned slab, Nyquist condition)
    ──→ TC-SP-2.5 (Reichardt ≡ energy model)

OP-SP-009 (adaptation timescale hierarchy)
    ←── OP-SP-002 (extension)
    ──→ OP-SP-010 (slow feedback can be reparametrized as slow adaptation)
    ──→ TC-SP-1.4, TC-SP-4.3

OP-SP-010 (top-down feedback justification)
    ─── affected by: OP-SP-009 (if feedback is slow, it's adaptation)
    ──→ TC-SP-1.3 (causal ordering preserved or violated)

OP-SP-M1 (Tier 2 boundary purity necessity)
    ─── isolated (philosophical; depends on DPI + information theory)

OP-SP-M2 (σ-pushforward deterministic vs probabilistic)
    ─── affects: TC-SP-5.1 (σ propagation formalism)
    ─── isolated otherwise

OP-SP-M3 (SCC energy parallel to stage 2)
    ←── OP-SP-006 (if u_t = stage 2 graded field, M3 becomes evidence)
    ──→ PAI OP-PAI-002 (anchors A(u) to stage 2)

OP-SP-M4 (FEP adoption/rejection)
    ─── affects: TC-SP-4.3 (if adopted: first-principle derivation)
    ─── affects: PAI OP-PAI-003 (if adopted: active inference language)
```

**Critical path** (PAI bridge 까지):

```
OP-SP-006 → OP-SP-007 → PAI Phase 5 (action connection)
    └──→ OP-PAI-001 → OP-PAI-002 → OP-PAI-003
```

**Independent paths** (병렬 진행 가능):
- OP-SP-001 (완전 독립)
- OP-SP-004 (OP-SP-003 에만 영향)
- OP-SP-008 (OP-SP-004 와 병렬)
- OP-SP-M1, OP-SP-M2 (거의 독립)

**Coupled pairs**:
- OP-SP-002 ↔ OP-SP-009 (같은 메커니즘의 scope 차이)
- OP-SP-003 ↔ OP-SP-005 (fiber bundle ↔ sheaf)
- OP-SP-004 ↔ OP-SP-008 (parallel "why these axes?" questions)
- OP-SP-006 ↔ OP-SP-M3 (mutual evidence)

---

## 5. Severity 분포

| Severity | 개수 | 코드 |
|----------|------|------|
| **High** | 2 | OP-SP-004, OP-SP-006 |
| **Medium** | 7 | OP-SP-002, 003, 005, 007, 008, 009, M3 |
| **Low** | 5 | OP-SP-001, 010, M1, M2, M4 |

**총 14 OP** (10 core + 4 meta).

High severity 둘 — OP-SP-004 (색 대립 군론) 와 OP-SP-006 (SCC u_t 위치) — 이 *결정적 다음 작업*. OP-SP-006 이 본 디렉토리의 PAI bridge 가능성을 결정; OP-SP-004 가 색 채널의 제일 원리 정당화.

---

## 6. 본 디렉토리에서 *resolved* 된 OP 목록

```
RESOLVED OPs in this directory: NONE
```

본 디렉토리의 discipline ([[00_INDEX#4. 정합성 ledger|00 §4]]): 어떤 OP 도 *RESOLVED 로 이동시키지 않음*. 모든 OP 가 후속 plan 의 작업 대상.

---

## 7. PAI OP 와의 *공식적* 격리 및 cross-link 요약

[[perception_action_interpretation_pivot_2026_05_21#OP-PAI-001|PAI 의 OP-PAI-001 ~ 006]] 과 본 디렉토리의 OP-SP-001 ~ 010 + M1-M4 는 *공식적으로 분리됨*:

- 본 디렉토리는 PAI OP 를 *advance 시도하지 않음*
- PAI 작업은 본 디렉토리의 OP-SP 를 *advance 시도하지 않음*

단, 다음 *단방향 의존* 은 공식 등록:

| OP-SP | PAI OP | 관계 | 방향 |
|-------|--------|------|------|
| OP-SP-006 | OP-PAI-001 | $u_t$ 식별이 $\mathcal{I}_{\text{perception}}(F)$ 의 전제 | OP-SP-006 → OP-PAI-001 |
| OP-SP-006 | OP-PAI-002 | $u_t$ 의 stage 가 $\mathcal{A}(u)$ 의 domain 결정 | OP-SP-006 → OP-PAI-002 |
| OP-SP-007 | PAI Phase 5 | Stage 4 cut 이 action connection substrate 결정 | OP-SP-007 → Phase 5 |
| OP-SP-M3 | OP-PAI-002 | SCC energy = stage 2 functional 이면 $\mathcal{A}(u)$ anchoring | OP-SP-M3 → OP-PAI-002 |
| OP-SP-M4 | OP-PAI-003 | FEP 채택 시 active inference 언어로 번역 | OP-SP-M4 → OP-PAI-003 |
| OP-SP-002, 009 | OP-PAI-002 | Adaptation timescale = action temporal window (간접) | weak, isolated |

**Critical chain**: OP-SP-006 → OP-PAI-001 → OP-PAI-002 가 PAI bridge 의 *최소 필요 체인*. OP-SP-007 은 Phase 5 의 *시작점* 을 결정.

---

## 8. 본 문서가 *시도하지 않는 것*

- 어떤 OP 의 *해결 시도*
- OP 사이 *우선순위 결정* (severity rating 만 제공)
- 14개 OP-SP 코드 외 *새 OP 등록* (14개 고정)
- PAI OP 와의 *통합* 시도 (격리 + cross-link 등록만)
- SCC 와의 *수정 제안* (preservation 만)
- OP 의 *부분 해결 시도* (heuristic candidate 방향만)

---

## 9. 한 줄 요약

> Sensing pipeline 의 OP 총 14: core 10 (OP-SP-001 ~ 010) + meta 4 (OP-SP-M1 ~ M4). High severity 2 (OP-SP-004, 006); Medium 7; Low 5. Critical path = OP-SP-006 → OP-SP-007 → PAI bridge; critical dependency chain = OP-SP-006 → OP-PAI-001 → OP-PAI-002. 본 디렉토리에서 **resolved = 0**.

---

## 10. Path to PAI Bridge — 로드맵 스케치

본 섹션은 OP-SP-006 → OP-SP-007 → PAI bridge 가 *어떻게 진행될 것인지* 의 단계별 스케치다. 이것은 *계획 제안* 이 아니라 *구조의 서술* — 현재 작업하지 않는다.

### Phase I — OP-SP-006 의 진척 (전제)

**목표**: SCC $u_t$ 의 stage 식별.

필요 작업:
1. Stage 1, 2, 3 각각에서 $u_t^{(i)}$ 를 수치 구성 (§2.6.3 실험 A)
2. 각 $u_t^{(i)}$ 에서 SCC diagnostic $d = (\text{Bind, Sep, Inside, Persist})$ 계산
3. 어느 stage 에서 phase transition ($\beta/\alpha > 4\lambda_2 / |W''(c)|$) 이 적절히 발생하는가 확인
4. OP-SP-M3 검증 — SCC energy 가 stage 2 functional 과 일치하는가의 수치 확인

*예상 결론* (현재 미결): stage 2 graded field 가 $u_t$ 의 가장 자연스러운 후보일 가능성 높음 (SCC energy 의 4 term 이 stage 2 의 4 computational 측면과 형식적으로 유사하기 때문). 그러나 이것은 추측이며 OP 임.

### Phase II — OP-SP-007 의 진척

**목표**: Stage 4 cut location 확정 (LGN / V1 중 어느 것이 PAI 의 "perceptual unit" 을 carry 하는가).

필요 작업:
1. LGN output 과 V1 input 에서의 *action-addressable information* 비교 — 어느 쪽이 PAI §2 의 "action unit" 기준 더 잘 만족하는가?
2. TC-SP-3.2 (latency) 와 TC-SP-4.1 (end-to-end bound) 의 LGN 포함 / 미포함 수치 비교

*예상 결론* (현재 미결): LGN cut 이 spike-level action connection 에 충분할 가능성; V1 cut 은 *orientation-based action* (manipulation, grasping direction) 에 필요.

### Phase III — PAI OP-PAI-001 진척 (bridge 시작)

**전제**: OP-SP-006 RESOLVED.

**목표**: $\mathcal{I}_{\text{perception}}(F)$ 의 수학적 정의.

OP-SP-006 이 "stage 2 graded field" 로 해결된다면:

$$
\mathcal{I}_{\text{perception}}(F) := \text{(equivalence class of } u_t^{(2)} \text{ restricted to } \Omega(F)\text{)}
$$

$\Omega(F)$: formation $F$ 의 support set. $u_t^{(2)}$: stage 2 graded field.

이 정의가 *구조적 거리* $d$ 의 정의 (OP-PAI-001 의 나머지 절반) 를 가능케 하는가?

### Phase IV — PAI OP-PAI-002 진척

**전제**: OP-PAI-001 진척.

**목표**: $\mathcal{A}(u)$ 의 action-level 정의.

OP-SP-006 의 stage 결정에 따라:
- Stage 2: $\mathcal{A}(u)$ = affordance map over retinal-graded field (Gibsonian candidate)
- Stage 3: $\mathcal{A}(u)$ = action-saliency over spike rate field

두 후보 중 PAI §4.2 (IPF 정의) 와 *더 잘 호환되는* 것을 선택.

### Phase V — Invariance criterion 선택 (OP-PAI-003)

**전제**: OP-PAI-001 + OP-PAI-002 진척.

**목표**: PAI §4.4 의 세 candidate form 중 선택:
- Candidate 1 (equivariance): $\mathcal{P}(g \cdot x) = g \cdot \mathcal{P}(x)$
- Candidate 2 (commutativity): $\mathcal{A} \circ \mathcal{P} = \mathcal{P} \circ \mathcal{A}'$
- Candidate 3 (low-distortion): $\Delta_{\text{interp}}(F) \leq \epsilon$

OP-SP-006 의 결과와 OP-SP-007 의 LGN/V1 결정이 함께 어느 form 이 자연스러운가를 제약.

**Bridge complete condition**: Phase I–V 가 모두 partially resolved 되고, $\Delta_{\text{interp}}(F)$ 가 수치 계산 가능한 object 가 될 때.

---

## 11. Verification of OP Non-Resolution — 개별 확인 ledger

본 섹션은 §6 의 "RESOLVED = 0" 을 *항목별로* 검증하는 explicit ledger.

본 디렉토리의 discipline: 어떤 OP 도 이 디렉토리 안에서 RESOLVED 로 이동하지 않음. 아래는 각 OP 의 *non-resolution 이유* 를 명시.

| 코드 | Non-resolution 이유 | 상태 확인 |
|------|---------------------|----------|
| OP-SP-001 | Poisson 근사의 정확한 오차 bound 미계산; Cox 확장 선택 미결 | OPEN |
| OP-SP-002 | 단일 $\tau_a$ 의 다중 시상수로의 교체 형식 미결정 | OPEN |
| OP-SP-003 | Fiber bundle 이 trivial vs non-trivial 미결; structure group 미확인 | OPEN |
| OP-SP-004 | Lie group 정당화 vs PCA 통계 정당화 사이 선택 미결 | OPEN |
| OP-SP-005 | Sheaf cohomology $H^1$ 계산 미수행; reconstruction bound 미수치화 | OPEN |
| OP-SP-006 | $u_t$ 가 stage 1 / 2 / 3 / pre-0 중 어느 것인지 수치 검증 미수행 | OPEN |
| OP-SP-007 | LGN vs V1 cut 의 PAI 관련성 미분석; TC-SP 수치 재계산 미수행 | OPEN |
| OP-SP-008 | $C_4 \subset SO(2)$ 의 retinal 필연성 미증명; cortical boost 메커니즘 미결 | OPEN |
| OP-SP-009 | $k(\tau)$ 스펙트럼 형태 (이산 vs power-law) 미결; 실측 fitting 미수행 | OPEN |
| OP-SP-010 | Feedback strength 정량화 미수행; feedback 이 TC-SP-1.3 을 깨는지 미확인 | OPEN |
| OP-SP-M1 | DPI 기반 boundary-purity 필연성 증명 미시도 | OPEN |
| OP-SP-M2 | Probabilistic σ 의 추가 구조 분석 미수행 | OPEN |
| OP-SP-M3 | SCC energy = stage 2 functional 의 수치 동치 확인 미수행 | OPEN |
| OP-SP-M4 | FEP 채택 기준 (§3.4.1) 의 실증 확인 없음; SCC 4-term 과의 관계 미분석 | OPEN |

**결론**: 총 14 OP 전부 OPEN. RESOLVED = 0. §6 의 statement 확인됨.

---

## 12. Severity 루브릭 — 명시적 정의

본 섹션은 High / Medium / Low severity 의 *정확한 판정 기준* 을 정의.

### 12.1 High Severity

다음 중 *하나 이상* 에 해당:

1. **PAI bridge block**: 이 OP 의 OPEN 상태가 PAI bridge (OP-PAI-001 → OP-PAI-002 chain) 의 시작을 *직접 막음*.
2. **TC-SP invalidation risk**: 이 OP 가 *잘못 해결될 경우* 기존 TC-SP 하나 이상의 statement 가 형식적으로 틀리게 됨.
3. **SCC framework reorientation**: 이 OP 의 해결이 SCC 의 *전체 해석 방향* (substrate 가 어디에 있는가) 을 결정.

**현재 High**: OP-SP-004, OP-SP-006.
- OP-SP-004: TC-SP-2.6 의 *최적성 statement 의 강도* 를 결정 (잘못 해결되면 statement 약화). 색 채널의 제일 원리가 없으면 전체 색 opponency framework 가 statistically motivated 에 그침.
- OP-SP-006: PAI bridge 의 직접 전제 (§10 Phase I). SCC framework 의 substrate 위치 결정.

### 12.2 Medium Severity

다음 중 *하나 이상*, 그러나 High 기준 미달:

1. **TC-SP quantitative scope**: 이 OP 의 해결이 기존 TC-SP 의 *정량적 statement* 를 강화하거나 약화하나 invalidate 하지는 않음.
2. **Formal elegance**: 이 OP 의 해결이 본 문서의 형식적 완결성을 크게 개선하나 후속 증명에 *필수* 는 아님.
3. **Downstream scope limitation**: 이 OP 가 OPEN 으로 남으면 특정 방향의 *확장이 제한* 되나 현재 scope 는 유지.

**현재 Medium**: OP-SP-002, 003, 005, 007, 008, 009, M3.

### 12.3 Low Severity

다음 *모두* 에 해당:

1. TC-SP 들이 이 OP 해결 없이도 *현재 형태* 로 유지됨.
2. PAI bridge 에 직접 영향 없음.
3. 이 OP 가 해결되어도 본 디렉토리의 *핵심 theorem candidates* 의 statement 는 변경 없음.
4. 주로 *curiosity, formal cleanup, philosophical clarification* 수준.

**현재 Low**: OP-SP-001, 010, M1, M2, M4.

### 12.4 Severity 재평가 조건

다음 이벤트 발생 시 severity 재평가 필요:
- 새 TC-SP 가 등록되어 기존 OP 에 *새 dependency* 생길 때
- PAI 작업 진척으로 *bridge dependency* 가 명확해질 때
- 실험 결과가 어떤 OP 의 *해결 불가능성* 을 보여줄 때 (이 경우 severity 변경이 아닌 *retraction 고려*)

---

## 13. OP-SP Timeline — 등록 이력

본 섹션은 각 OP 의 *최초 등록 시점* 과 *출처* 를 기록하는 이력 ledger.

모든 OP 는 2026-05-25 에 본 sensing_pipeline 디렉토리 작업 중 등록됨 (sensing pipeline 문서들의 v0 작성 세션).

| 코드 | 등록일 | 출처 문서 | 출처 섹션 | 비고 |
|------|--------|----------|----------|------|
| OP-SP-001 | 2026-05-25 | 02_stage0_photon_point_process.md | §9 | Poisson 가정 한계 인식 |
| OP-SP-002 | 2026-05-25 | 03_stage1_photoreceptor_sde.md | §10 | Naka-Rushton 단일 τ 한계 |
| OP-SP-003 | 2026-05-25 | 04_stage2_inner_retinal_algebra.md | §6.5 | direct sum 의 부자연성 인식 |
| OP-SP-004 | 2026-05-25 | 04_stage2_inner_retinal_algebra.md | §6.4 | 색 대립 군론 미결 |
| OP-SP-005 | 2026-05-25 | 05_stage3_ganglion_spike_encoding.md | §7.4 | 비균질 표본화 sheaf |
| OP-SP-006 | 2026-05-25 | 07_omega_sigma_lift.md | §5.5 | SCC u_t stage 식별 — PAI critical |
| OP-SP-007 | 2026-05-25 | 05_stage3_ganglion_spike_encoding.md | §11 | Stage 4 cut location |
| OP-SP-008 | 2026-05-25 | 04_stage2_inner_retinal_algebra.md | §4.10 | Orientation 4축 군론 |
| OP-SP-009 | 2026-05-25 | 03_stage1_photoreceptor_sde.md | §4.3 | 적응 시상수 hierarchy |
| OP-SP-010 | 2026-05-25 | 01_framework_master.md | TC-SP-1.3 | Top-down feedback 무시 |
| OP-SP-M1 | 2026-05-25 | 07_omega_sigma_lift.md | §7 | Tier 2 boundary 패턴 |
| OP-SP-M2 | 2026-05-25 | 07_omega_sigma_lift.md | §3.4 | σ deterministic vs probabilistic |
| OP-SP-M3 | 2026-05-25 | 06_endtoend_information_bound.md | §7 | SCC energy / stage 2 parallel |
| OP-SP-M4 | 2026-05-25 | 06_endtoend_information_bound.md | §6.2 | FEP 채택 기준 |

**등록 baseline**: 2026-05-25. 이 날짜가 OP 진척 추적의 기준점.

**향후 갱신 규칙**:
- 어떤 OP 가 *partially advanced* 되면: 해당 OP 항목 (§2 또는 §3) 에 날짜 + 내용 *append*. 본 ledger 의 등록일은 *변경하지 않음* (immutable baseline).
- 어떤 OP 가 RESOLVED 로 이동할 준비가 되면: sensing_pipeline 디렉토리 discipline 에 의해 *이 디렉토리 안에서는 RESOLVED 로 이동하지 않음*. 후속 plan 문서에서 처리.

---

## 14. 본 문서가 *시도하지 않는 것* (재확인)

- 어떤 OP 의 *해결 시도*
- OP 사이 *우선순위 결정* (severity rating 만 제공)
- 새 OP-SP 코드 14개 외 *등록* 금지
- PAI OP 와의 *통합* 시도 (격리 + cross-link 등록만)
- SCC 와의 *수정 제안* (preservation 만)

---

*Open Problems registry v1. 2026-05-25. 총 14 OP 전부 OPEN. Resolved = 0. 후속 plan 에서 high-severity OP 들 (특히 OP-SP-006) 의 진척이 본 디렉토리의 다음 단계 자연스러운 entry.*
