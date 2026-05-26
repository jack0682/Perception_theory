---
type: working/sensing_pipeline/stage2
version: v1
date: 2026-05-25
status: DEFINITION-DRAFT
purpose: |
  Stage 2 integrated deep dive: inner retinal circuitry.
  (2a) ON/OFF split as Riesz lattice decomposition,
  (2b) Lateral inhibition as DoG/Laplacian convolution + scale-space,
  (2c) Temporal differentiation + direction selectivity
       (Adelson-Bergen, Reichardt, optical-flow PDE),
  + color opponency channels,
  + whitening / sparse coding view (§10).
  Registers TC-SP-2.1 through 2.6, OP-SP-003, OP-SP-004.
  v1 expansion: full proof sketches for TC-SP-2.1, 2.3, 2.4, 2.5;
  Lindeberg-Koenderink derivation; Marr-Hildreth rigorous statement;
  PCA derivation of color axes; whitening + sparse coding §10.
register: DEFINITION-DRAFT + THEOREM-CANDIDATE (proof sketches added v1)
parent: 01_framework_master
prev_stage: 03_stage1_photoreceptor_sde
constraint_compliance:
  canonical_theorem_changes: 0
  scc_edits: 0
---

> [!nav] Parent: [[00_INDEX]] · Prev: [[03_stage1_photoreceptor_sde]] · Next: [[05_stage3_ganglion_spike_encoding]]

# Stage 2 — Inner Retinal Algebra

## 0. 본 문서의 위치

본 문서는 SSKP 의 세 번째 kernel $\mathcal{K}_2 : \mathcal{S}_1 \to \mathcal{S}_2$ — *광수용기 graded 막전위 → 다채널 분기된 graded 신호* 의 변환을 정식화한다.

내부 망막은 세 단계로 *논리적*으로 분리되나 동역학적으로는 *긴밀히 결합* 됨:

- **2a**: ON/OFF 부호 분리 (첫 시냅스, 수용체 차이로 결정)
- **2b**: 측방 억제 (수평세포 피드백 → DoG center-surround)
- **2c**: 시간 미분 + 방향 선택성 (amacrine + DSGC)
- **추가**: 색 대립 채널 (cone type 비교)

이 셋은 *분리할 이유가 없음* — 하나의 multichannel 분기로 통합. 본 문서가 그 통합 형식을 제공.

본 문서가 *수행하지 않는 것*: 스파이크 부호화 (→ [[05_stage3_ganglion_spike_encoding|05]]).

**v1 확장 (2026-05-25)**: §3 의 Riesz 분해 유일성 full proof; §3.2 의 Banach lattice positive cone 분석; §3.4 의 mGluR6 → TRPM1 explicit kinetic model; §4 의 full Fourier 분석 (DoG transform, bandpass peak); §4.5 의 Lindeberg-Koenderink heat-equation 유도; §4.6 의 rigorous Marr-Hildreth statement; §4.7 의 Gaussian random field MAP 유도; §4.9 의 retinal sphere explicit metric; §5.3 의 Adelson-Bergen velocity-slab Fourier proof; §5.4 의 Reichardt-energy autocorrelation 등가성 유도; §5.5 의 aperture-problem rigorous form; §6 의 PCA full derivation with Ruderman-Cronin-Chiao numerical eigenvalues; §6.3 의 SO(3) representation theory; **신설 §10** Atick-Redlich whitening + Olshausen-Field sparse coding.

---

## 1. 상태공간 $\mathcal{S}_2$

### 1.1 다채널 구조

Stage 2 출력은 *수십 개* 의 분리된 graded 채널. 각 채널은 자신의 시공간 함수.

채널 색인 집합:

$$
\mathcal{C} := \{ ON, OFF \} \times \{ T, S \} \times \{ L\text{-}M, S\text{-}(L\text{+}M), \text{Lum} \} \times \{ \theta_0, \theta_1, \theta_2, \theta_3 \}
$$

- $ON / OFF$: 부호 (2)
- $T / S$ (transient / sustained): 시간 미분 정도 (2)
- $L\text{-}M, S\text{-}(L\text{+}M), \text{Lum}$: 색 대립 + 휘도 (3)
- $\theta_i$: 4개 기본 방향 (DSGC 방향 선택성 약 4축)

이론적 총 채널 수 $|\mathcal{C}| = 2 \times 2 \times 3 \times 4 = 48$. 실제 망막의 양극세포·신경절세포 type 수는 $\sim 20$ — 위 cross-product 일부만 *실제* 구현; 나머지는 *가능성* 으로 둠.

### 1.2 상태공간 정의

$$
\boxed{\mathcal{S}_2 := \bigoplus_{c \in \mathcal{C}} C\big( \Sigma_{\text{ret}} \times \mathbb{R}^+, \mathbb{R}^+ \big)}
$$

- 각 채널 $c$ 의 출력은 $\mathbb{R}^+$ 값 (rectified — half-wave; §3 의 ON/OFF 분리 후)
- direct sum 으로 채널들 독립
- Polish space (각 component 가 Polish; direct sum 보존)

### 1.3 위상

각 component $C(\Sigma \times \mathbb{R}^+, \mathbb{R}^+)$ 의 uniform topology on compacts 의 Borel; direct sum 은 product 위상.

---

## 2. Stage 2 의 전체 구조 — Pre-processing 파이프라인

$\mathcal{K}_2$ 는 다음 4 sub-stage 의 composition:

$$
\mathcal{S}_1 \xrightarrow{\mathcal{K}_{2a}} \mathcal{S}_{1.5}^{\pm} \xrightarrow{\mathcal{K}_{2b}} \mathcal{S}_{1.75}^{\text{DoG}} \xrightarrow{\mathcal{K}_{2c}} \mathcal{S}_{1.9}^{\text{motion}} \xrightarrow{\mathcal{K}_{2d}} \mathcal{S}_2
$$

- $\mathcal{K}_{2a}$: ON/OFF 분기 (§3)
- $\mathcal{K}_{2b}$: 측방 억제 + DoG (§4)
- $\mathcal{K}_{2c}$: 시간 미분 + 방향 분기 (§5)
- $\mathcal{K}_{2d}$: 색 대립 (§6)

각 sub-stage 는 *결정론적 또는 mild stochastic* (대부분 deterministic + thermal noise). $\mathcal{K}_{2a/b/c/d}$ 는 모두 *선형 + half-wave rectification* 의 결합. 정확한 form 은 본문에서.

**Order 의 가소성**: 실제 망막에서 위 sub-stage 들의 *시간 순서* 는 미세하게 다를 수 있음 (예: 색 대립이 측방 억제와 *동시* 진행). 본 디렉토리는 *논리적 분해* 만 제공; 실제 *순서 commitment* 는 OP-SP 로 분리.

---

## 3. ON/OFF 분리 — 첫 시냅스의 lattice 분해

### 3.1 생물학적 사실 요약

광수용기 → 양극세포 시냅스에서:

- **ON-bipolar**: 글루타메이트 *대사성* 수용체 mGluR6. 글루타메이트 결합 → TRPM1 채널 *닫힘* → 과분극. *부호 반전*: 빛 증가 시 광수용기 글루타메이트 *감소* → mGluR6 release → TRPM1 *열림* → 양극세포 *탈분극*.
- **OFF-bipolar**: 글루타메이트 *이온성* 수용체 AMPA / kainate. 글루타메이트 결합 → 채널 *열림* → 탈분극. *부호 보존*: 빛 증가 시 글루타메이트 감소 → 채널 *닫힘* → 양극세포 *과분극*.

따라서 *같은* 광수용기 출력 $V$ 가 *두 분리된* 양극세포 집단으로 분기. 각각 *부호 반대* 의 응답을 동일 자극에 대해 생성.

### 3.2 수학적 형식 — Half-wave rectification

광수용기 응답 $V(x, t) - V_0$ (with $V_0 = $ 기저선, 예: $V_{\text{rest}}$) 를 다음 두 분기로 분해:

$$
\boxed{V_{\text{ON}}(x, t) := \big[ V(x, t) - V_0 \big]_+, \quad V_{\text{OFF}}(x, t) := \big[ V_0 - V(x, t) \big]_+}
$$

여기서 $[u]_+ := \max(u, 0)$.

**Note (부호 규약)**: §03 에서 빛 = hyperpolarization (V 감소). 따라서 일반적 *light-positive* 채널은 $V_0 - V$ 방향. 그러나 단순화를 위해 *광수용기 출력의 부호를 외부에서 미리 반전* 했다고 가정 ($V \to V_0 - V$): 즉 *ON 채널 = 빛 증가에 양수 응답*. 본 문서는 이 단순화된 부호로 이하 작성.

#### 3.2.1 Banach lattice 의 positive cone — 정밀 구조

$E := C_b(\Sigma_{\text{ret}} \times \mathbb{R}^+, \mathbb{R})$ (bounded continuous functions with sup-norm $\|\cdot\|_\infty$) 은 **Banach lattice** 이다 (Aliprantis-Burkinshaw, "Positive Operators" §1.1). 즉:

(B1) $E$ 는 Banach space.
(B2) $E$ 는 vector lattice — 점별 $f \vee g := \max(f, g)$, $f \wedge g := \min(f, g)$ 정의됨.
(B3) lattice 연산이 norm 과 호환: $|f| \leq |g| \implies \|f\| \leq \|g\|$, 여기서 $|f| := f \vee (-f)$.

**Positive cone** $E_+ := \{ f \in E : f(x, t) \geq 0 \text{ for all } (x, t) \}$.

#### 3.2.2 Positive cone 의 세 핵심 성질

**Proposition 3.1** ($E_+$ 의 구조). $E_+$ 는 다음 3 성질을 만족:

(C1) **Closed**: $\{f_n\} \subset E_+$, $f_n \to f$ in $\|\cdot\|_\infty$ $\implies$ $f \in E_+$.
(C2) **Normal**: $\exists \, M > 0$ such that $0 \leq f \leq g \implies \|f\| \leq M \|g\|$. (여기서 $M = 1$.)
(C3) **Generating**: $E = E_+ - E_+$. 임의의 $f \in E$ 가 $f = f^+ - f^-$ with $f^\pm \in E_+$.

**증명 sketch** (Aliprantis-Burkinshaw Thm 1.7):

- (C1): $f_n \to f$ uniformly 이면 각 $(x, t)$ 에서 $f_n(x, t) \to f(x, t)$; $f_n(x, t) \geq 0$ 이면 한계값도 $\geq 0$.
- (C2): $0 \leq f \leq g$ 이면 점별로 $|f(x,t)| = f(x,t) \leq g(x,t) = |g(x,t)|$; sup 도 동일.
- (C3): $f^+ := f \vee 0 = \max(f, 0)$, $f^- := (-f) \vee 0 = \max(-f, 0)$. 점별로 $f = f^+ - f^-$ 자명.

세 성질은 *Banach lattice* 의 정의에 함축되어 있으나, *생성성* (C3) 이 ON/OFF 분기의 수학적 기반이다 — 임의의 신호가 ON-positive 와 OFF-positive 두 부분으로 *유일하게* 분해됨을 함의.

#### 3.2.3 Cone 위의 graded calculus

ON/OFF 분기 후 양극세포 응답은 모두 $E_+$ 위 정의됨. $E_+$ 는 cone 이지 vector space 가 아니므로 다음과 같은 *제한된* 산술만 자유롭게 허용:

| 연산 | $E_+$ 안에서 |
|------|------|
| 덧셈 $f + g$ | YES (cone 의 정의) |
| 양의 스칼라곱 $\lambda f$, $\lambda \geq 0$ | YES |
| 음의 스칼라곱 $-f$ | NO (cone 밖) |
| 차분 $f - g$ | NO (불가; 결과를 다시 rectify 해야 $E_+$) |
| lattice $f \vee g$, $f \wedge g$ | YES |
| 곱 $f \cdot g$ (점별) | YES (cone closed under multiplication of nonneg) |
| 합성곱 $f * g$ (kernel 이 $\geq 0$일 때) | YES |

DoG kernel 처럼 *signed* kernel 과의 합성곱은 결과가 cone 밖으로 나갈 수 있어, 다시 ON/OFF 분리 (rectification) 가 필요. 이게 §4 에서 합성곱이 *signed* 결과를 만든 후 cone 으로 회수하기 위해 두 번째 half-wave 가 필요한 이유.

### 3.3 Riesz space 관점

$\mathcal{S}_1$ 의 함수공간 $C(\Sigma \times \mathbb{R}^+, \mathbb{R})$ 은 *Riesz space* (vector lattice) — 함수의 pointwise max, min 이 정의되고 partial order 가 lattice 구조 형성.

Riesz 분해 정리: 임의의 $u \in $ Riesz space 에 대해 unique decomposition

$$
u = u^+ - u^-, \quad u^+, u^- \geq 0, \quad u^+ \wedge u^- = 0
$$

(pointwise lattice 연산). 본 stage 의 ON/OFF 분리는 *정확히* 이 분해.

### 3.4 Theorem-candidate

### TC-SP-2.1 — [DELETED 2026-05-25 Pass 5 #11 model misspecification]

**Status**: **DELETED via Pass 5 #11**. Aliprantis-Burkinshaw Riesz lattice decomposition (Hahn-Jordan) 은 generic Banach lattice 정리로 sound. 그러나 *retinal ON/OFF channel split* 의 biological claim 과 *다른 객체*: (i) 실제 ON/OFF bipolars 는 overlapping operating ranges 보유 (Schiller 1992); (ii) 양 채널이 non-zero tonic baseline firing — pointwise $V_+ \wedge V_- = 0$ 위반; (iii) ON 과 OFF 가 다른 mGluR6 vs AMPA cascade 의 별개 출력으로 *gain, noise, latency 다름* — 같은 $V$ 의 rectification 아님.

**Original statement (preserved for audit trail)**:

> $V - V_0 = V_{\text{ON}} - V_{\text{OFF}}$, $V_{\text{ON}} \wedge V_{\text{OFF}} = 0$ 유일.

**Why DELETED**: Riesz decomposition 의 *uniqueness* 가 본 TC 의 load-bearing claim. 그러나 biological ON/OFF 는 *pointwise rectification of common scalar* 아니라 *two parallel asymmetric cascades with shared input*. Math handles different object than claim.

**Replacement**: Aliprantis-Burkinshaw Riesz lattice 본문 (§3) 은 *mathematical reference* 로 유지. ON/OFF 의 *biological 구현* 은 *별개 mechanism* (mGluR6, AMPA, baseline firing) 으로 §3.7 본문 유지. TC 자격 박탈.

#### TC-SP-2.1 — Full Proof Sketch

**Setup**. $E = C_b(\Sigma_{\text{ret}} \times \mathbb{R}^+, \mathbb{R})$ Banach lattice, $f := V - V_0 \in E$. 주장: $f = f^+ - f^-$ with $f^\pm \geq 0$, $f^+ \wedge f^- = 0$, *unique*.

**Existence**. $f^+(x,t) := \max(f(x,t), 0)$, $f^-(x,t) := \max(-f(x,t), 0)$ 로 정의. 점별로 $f^+ \geq 0$, $f^- \geq 0$, $f^+ - f^- = f$, $f^+ \cdot f^- = 0$ (한 점에서 둘 다 양수 불가). 점별 disjointness $f^+ \wedge f^- = 0$ 은 $\min(\max(f,0), \max(-f,0)) = 0$ 으로부터 자명.

**Uniqueness (핵심)**. 가정: $f = g - h$ with $g, h \geq 0$, $g \wedge h = 0$. 보일 것: $g = f^+$, $h = f^-$.

Step 1 (lattice 항등식). 임의의 vector lattice 에서:
$$
g - h = (g - h)^+ - (g - h)^-, \quad (g - h)^+ \wedge (g - h)^- = 0.
$$
(Aliprantis-Burkinshaw Thm 1.5.)

Step 2 (disjoint difference 공식). $g, h \geq 0$, $g \wedge h = 0$ 이면:
$$
(g - h)^+ = g, \quad (g - h)^- = h.
$$
*증명*: 점별로 $x$ 를 fix. (i) $g(x) > 0$ 이면 $g \wedge h = 0$ 으로부터 $h(x) = 0$, 따라서 $g(x) - h(x) = g(x) > 0$, $(g - h)^+(x) = g(x)$, $(g - h)^-(x) = 0 = h(x)$. (ii) $h(x) > 0$ 이면 대칭으로 $(g - h)^+(x) = 0 = g(x)$, $(g - h)^-(x) = h(x)$. (iii) $g(x) = h(x) = 0$ 이면 둘 다 0; 자명.

Step 3 (적용). $f = g - h$ 와 Step 1, 2 결합: $f^+ = (g - h)^+ = g$, $f^- = (g - h)^- = h$. QED.

**해석적 함의**. 유일성은 lattice 구조 *외에 추가 가정 없이* — 측도, 위상, 미분구조 모두 불필요 — 성립. 따라서 ON/OFF 분리는 *연속성과 무관* 한 순수 algebraic 강제.

**Banach lattice 강화**. (C1) 의 closedness 가 추가로 보장: $V_n \to V$ uniformly $\implies$ $V_n^\pm \to V^\pm$ uniformly. 즉, ON/OFF 분기는 *연속 작용소*. 이는 measurability of $\mathcal{K}_{2a}$ (kernel 형식) 의 자동 보장.

**참고**: 본 분해는 *Hahn-Jordan 분해* (signed measure 의 $\mu = \mu^+ - \mu^-$) 의 함수 버전. Riesz space (= vector lattice) 의 가장 기본적 정리. Aliprantis-Burkinshaw §1.2 Theorem 1.5.

**의미**: 망막의 ON/OFF 분리는 *사회적 합의가 아니라 수학적 강제*. 한 신호의 부호를 분리하는 *유일한* 방법. 진화가 이 유일성에 수렴함은 *임의* 가 아니다.

### 3.5 정보론적 함의 — 부호 비대칭성

ON 과 OFF 가 *대칭* 인가? 다음 두 사실:

1. *Positive cone* 자체는 대칭 ($V \leftrightarrow -V$ 가 ON ↔ OFF swap).
2. 그러나 *downstream 가공* 이 비대칭 — ON / OFF 채널이 다른 회로 (예: M vs P pathway 의 ON/OFF 비율 차이) 에 들어감.

따라서 *정보 분리* 는 대칭이나 *정보 사용* 은 비대칭. 본 stage 의 출력 수준에서는 대칭으로 다룸 — 비대칭은 stage 3 이후.

### 3.6 $\mathcal{K}_{2a}$ — explicit form

$$
\mathcal{K}_{2a} : V \mapsto (V_{\text{ON}}, V_{\text{OFF}})
$$

은 *결정론적* Dirac kernel ([[01_framework_master#2.5 결정론적 case|01 §2.5]]). 정의역 $\mathcal{S}_1$, 치역 $\mathcal{S}_{1.5}^\pm := \mathcal{S}_1^+ \oplus \mathcal{S}_1^+$ where $\mathcal{S}_1^+ := C(\Sigma \times \mathbb{R}^+, \mathbb{R}^+)$.

### 3.7 첫 시냅스의 분자적 model — mGluR6 → TRPM1 explicit kinetics

§3.1 의 *signal inversion* (ON 경로의 부호 반전) 은 단순한 정성적 사실이 아니라 *연쇄 효소 반응*의 결과. 본 절은 그 explicit ODE/SDE model 을 제시.

#### 3.7.1 분자 종 (species)

- $[\text{Glu}](t)$: 시냅스 틈의 glutamate 농도 (광수용기에서 release; 어둠에서 high, 빛에서 low).
- $R(t) \in \{0, 1\}$: mGluR6 수용체의 결합 상태 (Markov chain). 평균 fraction $r(t) := \mathbb{E}[R(t)]$.
- $G(t)$: 활성화된 G-protein (Gαo) 의 농도.
- $y(t) \in [0, 1]$: TRPM1 채널의 *열린 fraction* (key output variable).
- $V_b(t)$: ON-bipolar 막전위.

#### 3.7.2 결합 kinetics — mGluR6 occupancy

$$
\boxed{\frac{dr}{dt} = k_{\text{on}} [\text{Glu}](t) (1 - r) - k_{\text{off}} r}
$$

- $k_{\text{on}} \approx 10^7 \, \text{M}^{-1}\text{s}^{-1}$: forward rate
- $k_{\text{off}} \approx 10 \, \text{s}^{-1}$: backward rate
- 정상상태: $r_{\text{ss}}([\text{Glu}]) = \frac{k_{\text{on}} [\text{Glu}]}{k_{\text{on}} [\text{Glu}] + k_{\text{off}}} = \frac{[\text{Glu}]}{[\text{Glu}] + K_d}$, $K_d = k_{\text{off}} / k_{\text{on}}$.

이는 *Hill 함수 (n=1)* 또는 *Langmuir isotherm*. 어둠에서 $[\text{Glu}]$ high $\implies r \to 1$; 빛에서 $[\text{Glu}]$ low $\implies r \to 0$.

#### 3.7.3 G-protein 활성화

$$
\frac{dG}{dt} = k_G r(t) (G_{\text{tot}} - G) - k_{G,\text{off}} G
$$

여기서 $G_{\text{tot}}$ 은 총 Gαo 농도. 이는 *amplification 단계*: 한 분자 $r$ 가 다수 $G$ 활성화.

#### 3.7.4 TRPM1 채널 dynamics — 부호 반전의 핵심

mGluR6 → Gαo → TRPM1 의 효과는 *Gαo 가 TRPM1 을 닫음*. 따라서:

$$
\boxed{\frac{dy}{dt} = k_{\text{open}} (1 - y) - k_{\text{close}} G(t) y}
$$

- $G(t)$ high (어둠 시; 글루타메이트 ↑ → $r$ ↑ → $G$ ↑) → $y \to 0$ (채널 닫힘) → 막전위 hyperpolarized.
- $G(t)$ low (빛 시) → $y \to 1$ (채널 열림) → cation 유입 → 막전위 depolarized.

정상상태: $y_{\text{ss}}(G) = \frac{k_{\text{open}}}{k_{\text{open}} + k_{\text{close}} G}$. *Decreasing in $G$*. 따라서 부호 반전.

#### 3.7.5 막전위 — 부호 반전의 결정

ON-bipolar 막전위:

$$
V_b(t) = V_{\text{rest}} + g_{\text{TRPM1}} \cdot y(t) \cdot (V_{\text{cation}} - V_{\text{rest}})
$$

with $V_{\text{cation}} \approx 0 \text{ mV} > V_{\text{rest}} \approx -60 \text{ mV}$. $y$ ↑ ⟹ $V_b$ ↑ (depolarization).

#### 3.7.6 합성된 신호 전이 — explicit sign inversion

체인:
$$
[\text{光}] \uparrow \;\Rightarrow\; [\text{Glu}] \downarrow \;\Rightarrow\; r \downarrow \;\Rightarrow\; G \downarrow \;\Rightarrow\; y \uparrow \;\Rightarrow\; V_b \uparrow.
$$

즉, **$V_b \propto -G \propto -r \propto -[\text{Glu}] \propto +[\text{光}]$**. 두 번의 부호 반전 (Glu ↔ r 음의 관계, G ↔ y 음의 관계) 으로 net 부호는 *light-positive*.

#### 3.7.7 OFF 경로 (대조)

OFF-bipolar 의 AMPA 수용체:
$$
\frac{dy_{\text{AMPA}}}{dt} = k_{\text{on}}^{\text{AMPA}} [\text{Glu}](t) (1 - y_{\text{AMPA}}) - k_{\text{off}}^{\text{AMPA}} y_{\text{AMPA}}
$$

여기서 $y_{\text{AMPA}}$ 자체가 *cation channel open fraction*. *직접* binding-gated, G-protein 우회. 부호 관계:
$$
[\text{Glu}] \uparrow \;\Rightarrow\; y_{\text{AMPA}} \uparrow \;\Rightarrow\; V_b^{\text{OFF}} \uparrow
$$

광에 대해서는 부호 반대: $[\text{光}] \uparrow \Rightarrow [\text{Glu}] \downarrow \Rightarrow V_b^{\text{OFF}} \downarrow$ (hyperpolarization). 즉 *light-negative*.

#### 3.7.8 Quasi-steady-state reduction → ON/OFF rectification

$k_{\text{on}}, k_{\text{open}}$ 등이 충분히 빠르면 $r, G, y$ 모두 *quasi-steady state* 에 도달. 이 한계에서:

- ON-bipolar: $V_b^{\text{ON}}(t) \approx V_0^{\text{ON}} + g \cdot \sigma\big( c_1 ([\text{光}](t) - I_{\text{rest}}) \big)$
- OFF-bipolar: $V_b^{\text{OFF}}(t) \approx V_0^{\text{OFF}} + g \cdot \sigma\big( -c_1 ([\text{光}](t) - I_{\text{rest}}) \big)$

여기서 $\sigma$ 는 sigmoid (Hill 형태로부터 자동). 작은 신호 극한에서 sigmoid 는 *선형 + saturation*; 이 saturation 의 한쪽 끝 (zero floor) 이 ON/OFF rectification 의 분자적 기원.

따라서 §3.2 의 추상 half-wave $[\cdot]_+$ 는 §3.7 의 분자 kinetics 의 *유효 한계*. 두 viewpoint 가 정확히 일치.

---

## 4. 측방 억제와 Center-Surround — DoG 합성곱

### 4.1 생물학적 사실

양극세포 (ON 또는 OFF) 는 수평세포의 피드백을 통해 *center-surround* 수용야를 형성:

- *Center*: 직접 연결된 광수용기 (소수, $\sim 1-10$).
- *Surround*: 수평세포가 *광범위* (수십 ~ 수백 광수용기) 의 신호를 lateral 로 모아 *음성 피드백*.

결과: 양극세포 응답은 *국소 강도가 주변보다 큰 정도* 에 비례.

### 4.2 DoG kernel

**Definition 4.1**. *Difference of Gaussians*:

$$
\boxed{K_{\text{DoG}}(x; \sigma_c, \sigma_s, \alpha) := \frac{1}{2\pi \sigma_c^2} \exp\!\left(-\frac{|x|^2}{2 \sigma_c^2}\right) - \frac{\alpha}{2\pi \sigma_s^2} \exp\!\left(-\frac{|x|^2}{2 \sigma_s^2}\right)}
$$

- $\sigma_c$: center radius (small, $\sim 0.1$ deg)
- $\sigma_s$: surround radius (large, $\sigma_s / \sigma_c \approx 2-5$)
- $\alpha$: surround relative strength ($\approx 0.5-1$)

Integral: $\int K_{\text{DoG}} dx = 1 - \alpha$. $\alpha = 1$ 이면 *균형* (DC-zero) — 균질 자극에 대해 응답 0.

### 4.3 양극세포 응답 = 합성곱

$$
B_{\text{ON}}(x, t) = \big( K_{\text{DoG}} *_x V_{\text{ON}} \big)(x, t)
$$

여기서 $*_x$ 는 *공간* 합성곱. 시간 합성곱은 별도 (§5 의 amacrine 시간 미분).

같은 식으로 $B_{\text{OFF}}$.

**Note (rectification)**: 실제 양극세포는 다시 한 번 half-wave rectification 받을 수 있음 (graded 한계). 본 문서는 양극세포 응답을 $\mathbb{R}^+$ 값으로 — Riesz cone 안에서 작동.

### 4.4 Translation invariance

DoG 가 *공간 translation-equivariant*: 입력을 평행이동하면 출력도 평행이동.

$$
B(x; \tau_a V) = B(x - a; V)
$$

이는 *국소 등질성* 가정에서 성립 — fovea 의 다른 위치에서도 같은 DoG 형태. 단, peripheral 일수록 $\sigma_c, \sigma_s$ 가 *커짐* (eccentricity scaling) — *국소* 등질성, *전역* 비등질성.

### 4.5 Fourier 분석 — Bandpass 특성의 정확한 spectrum

#### 4.5.1 Gaussian 의 Fourier transform

표기: $\hat{f}(\xi) := \int_{\mathbb{R}^2} f(x) e^{-i \xi \cdot x} dx$. Convention 으로 $\xi \in \mathbb{R}^2$ (각진동수).

표준 사실:
$$
G_\sigma(x) := \frac{1}{2\pi \sigma^2} e^{-|x|^2 / (2\sigma^2)}, \quad \widehat{G_\sigma}(\xi) = e^{-\sigma^2 |\xi|^2 / 2}.
$$

#### 4.5.2 DoG transform — explicit

선형성에 의해:

$$
\boxed{\widehat{K_{\text{DoG}}}(\xi) = e^{-\sigma_c^2 |\xi|^2 / 2} - \alpha \cdot e^{-\sigma_s^2 |\xi|^2 / 2}}
$$

이는 *real-valued, even, isotropic* (only depends on $|\xi|$). 등방 polar coordinates 에서:
$$
\widehat{K_{\text{DoG}}}(\rho) = e^{-\sigma_c^2 \rho^2 / 2} - \alpha e^{-\sigma_s^2 \rho^2 / 2}, \quad \rho := |\xi|.
$$

#### 4.5.3 DC 응답 (zero frequency)

$\rho = 0$ 에서:
$$
\widehat{K_{\text{DoG}}}(0) = 1 - \alpha.
$$

- $\alpha = 1$: $\widehat{K_{\text{DoG}}}(0) = 0$ — *DC-blocking* (uniform field 에 무응답).
- $\alpha < 1$: DC gain $1 - \alpha > 0$.
- $\alpha > 1$: DC gain $1 - \alpha < 0$ (uniform field 에 *음수* 응답; 망막에서는 안 보임).

#### 4.5.4 고주파 한계

$\rho \to \infty$ 에서 (가정 $\sigma_c < \sigma_s$): $\sigma_c^2 \rho^2 < \sigma_s^2 \rho^2$ 이지만 둘 다 빠르게 감쇠; ratio $\widehat{K_{\text{DoG}}}(\rho) \approx e^{-\sigma_c^2 \rho^2 / 2}$ as $\rho \to \infty$. 즉, *high-pass 처럼 보이지 않음* — 결국 Gaussian envelope 으로 cutoff.

따라서 DoG 는 *high-pass 가 아니라 band-pass*.

#### 4.5.5 Bandpass peak — 정확한 주파수

$\widehat{K_{\text{DoG}}}$ 의 maximum 위치 $\rho_*$ 를 찾자. $\rho^2 = u$ 치환 후:
$$
\widehat{K_{\text{DoG}}}(u) = e^{-\sigma_c^2 u / 2} - \alpha e^{-\sigma_s^2 u / 2}.
$$

$\frac{d}{du}$ = 0:
$$
-\frac{\sigma_c^2}{2} e^{-\sigma_c^2 u / 2} + \alpha \frac{\sigma_s^2}{2} e^{-\sigma_s^2 u / 2} = 0
$$
$$
\frac{\sigma_c^2}{\sigma_s^2} \cdot \frac{1}{\alpha} = e^{-(\sigma_s^2 - \sigma_c^2) u / 2}.
$$

$\sigma_c < \sigma_s$ 이므로 LHS $< 1/\alpha$. 양변에 $\log$:
$$
\log\left( \frac{\sigma_c^2}{\alpha \sigma_s^2} \right) = -\frac{(\sigma_s^2 - \sigma_c^2)}{2} u_*
$$
$$
\boxed{u_* = \rho_*^2 = \frac{2 \log(\alpha \sigma_s^2 / \sigma_c^2)}{\sigma_s^2 - \sigma_c^2}}
$$

이 $\rho_*$ 가 *peak spatial frequency*. 단위: $\rho \sim [\text{rad/deg}]$, $\sigma \sim [\text{deg}]$, 따라서 $\rho_* \sim [\text{rad/deg}]$.

**한계점 분석**:

- $\alpha \sigma_s^2 / \sigma_c^2 \leq 1$ 이면 $\log \leq 0$, $u_* \leq 0$ — peak at $\rho = 0$ (DC), 즉 lowpass 형태. 이 경우 surround 가 too weak; band-pass 형성 안 됨.
- $\alpha \sigma_s^2 / \sigma_c^2 > 1$ 이면 $\rho_* > 0$ — true band-pass.

생리학적 typical: $\sigma_s / \sigma_c \approx 3$, $\alpha \approx 0.7$ → $\alpha \sigma_s^2 / \sigma_c^2 \approx 6.3$, $\log \approx 1.84$, $\rho_*^2 = 2 \cdot 1.84 / (9 \sigma_c^2 - \sigma_c^2) = 3.68 / (8 \sigma_c^2)$. $\sigma_c = 0.1 \text{ deg}$ → $\rho_*^2 \approx 46 \text{ rad}^2/\text{deg}^2$, $\rho_* \approx 6.8 \text{ rad/deg} \approx 1.1 \text{ cycles/deg}$.

이는 실험적으로 측정된 ganglion-cell preferred SF (1–4 cpd) 과 ballpark 일치.

#### 4.5.6 Bandwidth

Half-max 위치 $\rho_{\pm}$ 에서 $\widehat{K_{\text{DoG}}}(\rho_\pm) = \frac{1}{2} \widehat{K_{\text{DoG}}}(\rho_*)$ 풀어 octave bandwidth 계산. 실험적으로 약 1.5–2 octave. 정확한 형식은 transcendental.

### 4.5b Scale-space derivation (Lindeberg-Koenderink) — Full

#### 4.5b.1 Heat equation — proper scale parametrization

Gaussian scale-space 의 표준 형식. $u(x, \sigma) := (G_\sigma * f)(x)$ for $f \in L^2(\mathbb{R}^2)$. 다음 PDE 성립:

$$
\boxed{\partial_\sigma u(x, \sigma) = \sigma \, \Delta_x u(x, \sigma), \qquad u(x, 0) = f(x).}
$$

여기서 *$\sigma$ 계수가 핵심* — scale parametrization 에 의한 자연 측도 (Lindeberg 1994 §3).

**증명**. Gaussian 의 scale 미분:
$$
\partial_\sigma G_\sigma(x) = \partial_\sigma \left[ \frac{1}{2\pi \sigma^2} e^{-|x|^2 / (2\sigma^2)} \right].
$$

직접 계산:
$$
\partial_\sigma G_\sigma = \left( -\frac{2}{\sigma} + \frac{|x|^2}{\sigma^3} \right) G_\sigma = \frac{1}{\sigma} \left( \frac{|x|^2}{\sigma^2} - 2 \right) G_\sigma.
$$

한편:
$$
\Delta_x G_\sigma = \partial_{x_1}^2 G_\sigma + \partial_{x_2}^2 G_\sigma.
$$

$\partial_{x_i} G_\sigma = -\frac{x_i}{\sigma^2} G_\sigma$, $\partial_{x_i}^2 G_\sigma = \left( \frac{x_i^2}{\sigma^4} - \frac{1}{\sigma^2} \right) G_\sigma$. 합:
$$
\Delta_x G_\sigma = \left( \frac{|x|^2}{\sigma^4} - \frac{2}{\sigma^2} \right) G_\sigma = \frac{1}{\sigma^2} \left( \frac{|x|^2}{\sigma^2} - 2 \right) G_\sigma.
$$

따라서:
$$
\partial_\sigma G_\sigma = \sigma \cdot \Delta_x G_\sigma. \quad \blacksquare
$$

합성곱 $u = G_\sigma * f$ 에 대해 $\partial_\sigma u = (\partial_\sigma G_\sigma) * f = \sigma \Delta_x (G_\sigma * f) = \sigma \Delta_x u$. (대안 표기에서 $\sigma$ 가 $t = \sigma^2/2$ 로 reparametrize 되면 $\partial_t u = \Delta u$ 의 표준 heat equation.)

#### 4.5b.2 DoG ≈ scale-derivative ≈ scale-normalized Laplacian

$\sigma_s = \sigma_c + \Delta\sigma$ 로 표기 ($\Delta\sigma$ 작음). 일차 Taylor:
$$
G_{\sigma_s} = G_{\sigma_c} + \Delta\sigma \cdot \partial_\sigma G_\sigma \big|_{\sigma = \sigma_c} + O(\Delta\sigma^2)
$$
$$
= G_{\sigma_c} + \Delta\sigma \cdot \sigma_c \cdot \Delta G_{\sigma_c} + O(\Delta\sigma^2).
$$

따라서:
$$
K_{\text{DoG}} = G_{\sigma_c} - \alpha G_{\sigma_s} = (1 - \alpha) G_{\sigma_c} - \alpha \Delta\sigma \cdot \sigma_c \cdot \Delta G_{\sigma_c} + O(\Delta\sigma^2).
$$

**Special case** $\alpha = 1$ (DC-balanced): $G_{\sigma_c}$ 항 cancel, 남는 것:
$$
\boxed{K_{\text{DoG}} \big|_{\alpha = 1} \approx -\Delta\sigma \cdot \sigma_c \cdot \Delta G_{\sigma_c} = -\Delta\sigma \cdot \sigma_c \cdot \text{LoG}_{\sigma_c}.}
$$

즉, *DoG 는 small $\Delta\sigma$ 한계에서 scale-normalized Laplacian of Gaussian* (LoG with $\sigma$-weight). 부호 (음): DoG center 는 양, LoG center 는 음 (∂²/∂x² of Gaussian at origin); LoG 의 *음수* 가 DoG 와 같은 부호.

#### 4.5b.3 Lindeberg's scale-normalized Laplacian

Lindeberg (1994) 의 *scale-normalized derivative* 개념: scale-space 의 자연 미분은 $\sigma^k \partial^k$ 형태. 여기서:
$$
\mathcal{L}_{\text{norm}}(x, \sigma) := \sigma^2 \Delta_x u(x, \sigma) = \sigma \cdot \partial_\sigma u(x, \sigma).
$$

위 *4.5b.1* 의 PDE 로부터 두 형식 동치. DoG 와의 관계:
$$
K_{\text{DoG}} \approx -\frac{\Delta\sigma}{\sigma_c} \cdot \mathcal{L}_{\text{norm}}|_{\sigma = \sigma_c}.
$$

**점근 상수**. $\sigma_s = k \sigma_c$ ($k > 1$ ratio), $\Delta\sigma = (k - 1) \sigma_c$:
$$
K_{\text{DoG}} \approx -(k - 1) \sigma_c^2 \Delta G_{\sigma_c} = -(k - 1) \mathcal{L}_{\text{norm}}|_{\sigma_c}.
$$

생리적 $k \approx 3$ → 계수 $-2$.

**근사 오차**. 이차 Taylor:
$$
K_{\text{DoG}} = -(k-1) \sigma_c^2 \Delta G_{\sigma_c} - \frac{(k-1)^2 \sigma_c^2}{2} \partial_\sigma^2 G_\sigma|_{\sigma_c} + O((k-1)^3).
$$

$\partial_\sigma^2 G_\sigma$ 는 $\partial_\sigma (\sigma \Delta G_\sigma) = \Delta G_\sigma + \sigma \partial_\sigma \Delta G_\sigma = \Delta G_\sigma + \sigma \Delta (\sigma \Delta G_\sigma) = \Delta G_\sigma + \sigma^2 \Delta^2 G_\sigma$. 따라서 $O((k-1)^2)$ 항이 $\sigma_c^4 \Delta^2 G$ 를 포함; LoG (LoG of LoG) — biharmonic.

이차 보정은 $k \approx 1.6$ (Marr-Hildreth 권장) 에서 작으나, $k = 3$ 에서는 $\sim 20\%$ 오차. 따라서 DoG ≈ LoG 는 *qualitative*; 정확한 spectrum 은 §4.5.2 의 Fourier 사용.

### 4.6 가장자리 검출 (Marr-Hildreth) — Rigorous statement

#### 4.6.1 직관

이미지 $I(x)$ 의 *intensity edge* 는 직관적으로 $|\nabla I|$ 의 local maximum. 노이즈에 강건하려면 사전 smoothing → $|\nabla (G_\sigma * I)|$. 그러나 *gradient maximum* 보다 *Laplacian zero-crossing* 이 검출 쉽다 (sign change). Marr-Hildreth (1980) 가 이 등가성을 주장.

#### 4.6.2 Theorem statement — rigorous

**Theorem 4.2** (Marr-Hildreth zero-crossing, conditional). 입력 $f \in C^2(\mathbb{R}^2)$ 와 scale $\sigma > 0$ 에 대해 정의:
- $u_\sigma := G_\sigma * f$ (smoothed input)
- $L_\sigma := \Delta u_\sigma$ (Laplacian)
- $Z_\sigma := \{x \in \mathbb{R}^2 : L_\sigma(x) = 0\}$ (zero-crossing locus)

가정:
- (A1) $f$ 가 $C^2$, 그래서 $u_\sigma \in C^\infty$ (Gaussian smoothing).
- (A2) $\alpha = 1$ (DC-balanced DoG), 그래서 $K_{\text{DoG}} * f \approx -(\Delta\sigma) \sigma_c \Delta u_{\sigma_c} + O(\Delta\sigma^2)$.
- (A3) $f$ 가 *unidirectional edge* — locally $f(x) = \phi(\mathbf{n} \cdot x)$ for some unit vector $\mathbf{n}$ and step-like $\phi$ (Heaviside or sigmoid).

주장: 가정 (A1)–(A3) 하에서, $K_{\text{DoG}} * f$ 의 zero-crossing 집합 $Z_{\text{DoG}}$ 은 $Z_\sigma$ 의 $O(\Delta\sigma)$ neighborhood 안. 또한 unidirectional edge 가정 하에서 $Z_\sigma$ 은 *2차 방향 미분 영점* 위치와 일치:
$$
Z_\sigma \approx \{ x : \partial_\mathbf{n}^2 u_\sigma(x) = 0 \},
$$
즉, $\mathbf{n}$ 방향 second derivative 의 zero-crossing — 직관적 "inflection point of intensity profile".

#### 4.6.3 증명 sketch

Step 1 (DoG → LoG). §4.5b.2 의 small $\Delta\sigma$ Taylor 로 $K_{\text{DoG}} * f \approx c \cdot \Delta u_{\sigma_c}(x)$ for $c = -\Delta\sigma \cdot \sigma_c \neq 0$. Zero-crossing 은 $c$ 부호 무관.

Step 2 (Unidirectional reduction). (A3) 의 $f(x) = \phi(\mathbf{n} \cdot x)$ 에서 $u_\sigma(x) = (G_\sigma^{(1)} * \phi)(\mathbf{n} \cdot x)$ where $G_\sigma^{(1)}$ 는 1D Gaussian (다른 방향은 적분되어 사라짐). 따라서:
$$
\Delta u_\sigma = \partial_\mathbf{n}^2 u_\sigma + \partial_{\mathbf{n}_\perp}^2 u_\sigma = \partial_\mathbf{n}^2 u_\sigma + 0 = \partial_\mathbf{n}^2 u_\sigma.
$$
(perpendicular direction 에서는 $u_\sigma$ 가 상수, 2차 미분 0).

Step 3 (Inflection 해석). 1D smoothed step $\tilde\phi := G_\sigma^{(1)} * \phi$ 의 inflection point 는 $\tilde\phi''(s) = 0$. 이는 정확히 $\partial_\mathbf{n}^2 u_\sigma = 0$. 만약 step $\phi$ 가 monotone 이면 $\tilde\phi'$ 이 max 인 위치 — *gradient maximum* 과도 일치 (1D).

Step 4 (Error bound). 가정 약화 (general $f$) 시: zero-crossing 분석은 더 복잡하지만, $\partial_\mathbf{n}^2$ 의 부호 변화는 *intensity profile 의 곡률 부호 변화* — 일반적으로 edge 의 *근방* 에서 발생. 정확한 위치 일치는 unidirectional case 에서만 보장.

**한계**:
- 곡선형 edge (curved boundary): $\Delta = \partial_\mathbf{n}^2 + \partial_\mathbf{t}^2$; tangential 항이 0 이 아님. Zero-crossing 위치가 *진짜* edge 에서 $O(\kappa \sigma^2)$ 이동 ($\kappa$ = curvature). Berzins (1984) 정량화.
- T-junction, corner: 다방향 edge 의 교차. Zero-crossing 위상이 복잡; isolated point 가 아닌 곡선.
- Texture, noise: false zero-crossing 다수. Multi-scale combination (Marr's "primal sketch") 필요.

따라서 Marr-Hildreth 는 *clean step edge* 의 경우 *정확*, 일반의 경우 *근사*.

### TC-SP-2.2 — [DELETED 2026-05-25 Pass 4]

**Status**: **DELETED via Pass 4** (cumulative 3 HOLE: Pass 3 #40 + Pass 4 #46 + #51). Refined form 의 (A1)(A2)(A3) qualifiers 도 boundary edge 와 pixel noise correlation 의 fundamental 위반을 해결 못 함.

**Original (refined) statement (preserved for audit trail)**:

> 가정 (A1)(A2)(A3) 하 DoG zero-crossing 위치가 입력 V 의 방향 2차 미분 영점과 $O(\Delta\sigma + \kappa\sigma^2)$ 오차 안에서 일치.

**Why DELETED**:
- Pass 3 #40 (Marr-Hildreth counterexamples — curved, T-junctions, parallel edges, textures) — partially mitigated by (A1)(A2)(A3) but still flagged.
- Pass 4 #46 (boundary): *sensor edge* (DoG 합성곱이 $\partial \Sigma_{\text{ret}}$ 근처에서 undefined neighborhood) + $\sigma \to 0/\infty$ singular limits 미처리.
- Pass 4 #51 (independence): independent-Gaussian-pixel-noise 가정 위반 (shared bipolar input, cone gap-junction coupling in primate retina).
- 3 patterns HOLE → 박탈.

**Replacement**: Theorem 4.2 (Marr-Hildreth refined statement) 본문 유지 — *approximation result* 로. DoG edge detection 의 *biological 적정성* 은 efficient coding (Atick-Redlich; 06 §5.3) 가 더 robust 정당화. TC 자격 박탈.

### 4.7 Bayesian 해석 — Full derivation

#### 4.7.1 Setup

입력 *real-world intensity* $V : \mathbb{R}^2 \to \mathbb{R}$ 을 *Gaussian random field* 로 model. 즉, 임의의 유한 점집합 $\{x_1, \ldots, x_n\}$ 에 대해 $(V(x_1), \ldots, V(x_n))$ 가 multivariate Gaussian. Covariance:
$$
C(x, x') := \mathbb{E}[V(x) V(x')] - \mathbb{E}[V(x)] \mathbb{E}[V(x')].
$$

가정 (translation-invariant): $C(x, x') = c(x - x')$ for some $c : \mathbb{R}^2 \to \mathbb{R}$. Fourier dual:
$$
\hat{c}(\xi) =: P_V(\xi), \quad \text{power spectrum of } V.
$$

자연 영상의 power spectrum 은 *power law*: $P_V(\xi) \approx A / |\xi|^{2}$ (Field 1987, "Relations between the statistics of natural images and the response properties of cortical cells"). 이는 *Brownian-like* — 1/f noise 의 2D 일반화.

#### 4.7.2 관측 model

광수용기 출력 $y = V + \eta$, $\eta$ 는 i.i.d. Gaussian noise with variance $\sigma_n^2$. 정확:
$$
y(x) = V(x) + \eta(x), \quad \eta(x) \sim \mathcal{N}(0, \sigma_n^2), \text{ independent across } x.
$$

(노이즈는 Stage 0 의 photon shot + Stage 1 의 thermal SDE 의 cumulative.)

#### 4.7.3 MAP estimator — Bayesian linear regression

목적: $\hat{V} = \arg\max_V P(V | y) = \arg\max_V P(y | V) P(V)$.

Discretize on grid $\{x_i\}_{i=1}^n$. Vector $\mathbf{V}, \mathbf{y} \in \mathbb{R}^n$. Prior:
$$
P(\mathbf{V}) = \mathcal{N}(0, \Sigma), \quad \Sigma_{ij} = c(x_i - x_j).
$$
Likelihood:
$$
P(\mathbf{y} | \mathbf{V}) = \mathcal{N}(\mathbf{V}, \sigma_n^2 I).
$$

Posterior (Bayes + Gaussian conjugacy):
$$
P(\mathbf{V} | \mathbf{y}) = \mathcal{N}(\mu_{\text{post}}, \Sigma_{\text{post}})
$$
with:
$$
\Sigma_{\text{post}}^{-1} = \Sigma^{-1} + \sigma_n^{-2} I
$$
$$
\mu_{\text{post}} = \Sigma_{\text{post}} \cdot \sigma_n^{-2} \mathbf{y} = (\Sigma^{-1} + \sigma_n^{-2} I)^{-1} \sigma_n^{-2} \mathbf{y}.
$$

MAP = posterior mean (Gaussian): $\hat{V} = \mu_{\text{post}}$.

#### 4.7.4 Continuum limit — operator form

연속 한계에서 ($\Sigma^{-1} \to $ inverse covariance kernel operator):
$$
\boxed{\hat{V} = (C^{-1} + \sigma_n^{-2} I)^{-1} \cdot \sigma_n^{-2} y.}
$$

Fourier diagonalization. $C$ 가 translation-invariant 이므로 Fourier 에서 multiplication: $\widehat{Cf}(\xi) = P_V(\xi) \hat{f}(\xi)$, 따라서 $C^{-1}$ 는 $1/P_V(\xi)$ multiplication. 그래서:
$$
\widehat{\hat{V}}(\xi) = \frac{1/\sigma_n^2}{1/P_V(\xi) + 1/\sigma_n^2} \hat{y}(\xi) = \frac{P_V(\xi)}{P_V(\xi) + \sigma_n^2} \hat{y}(\xi).
$$

이게 *Wiener filter* — 신호/노이즈 비율에 따른 frequency-dependent attenuation.

#### 4.7.5 Power-law prior → Laplacian-dominated inverse

$P_V(\xi) = A / |\xi|^2$ (자연 영상). 그러면:
$$
C^{-1} \text{ in Fourier} = |\xi|^2 / A.
$$

연속 도메인에서 $|\xi|^2$ multiplication 은 *negative Laplacian* $-\Delta$ 와 정확히 일치 (Fourier symbol of $-\Delta$ 가 $|\xi|^2$). 따라서:
$$
C^{-1} = -\Delta / A.
$$

MAP 추정:
$$
\hat{V} = (-\Delta/A + \sigma_n^{-2} I)^{-1} \sigma_n^{-2} y.
$$

Wiener filter spectrum:
$$
\widehat{\hat{V}}(\xi) = \frac{1}{1 + (\sigma_n^2 / A) |\xi|^2} \hat{y}(\xi).
$$

#### 4.7.6 Low-pass interpretation

위 spectrum 은 *Lorentzian* — Fourier transform 의 inverse 가:
$$
\hat{V}(x) = (K_{\text{Lorentz}} * y)(x), \quad \hat{K_{\text{Lorentz}}}(\xi) = \frac{1}{1 + \sigma_*^2 |\xi|^2}, \quad \sigma_*^2 := \sigma_n^2 / A.
$$

2D 에서 $K_{\text{Lorentz}}$ 의 real-space 형태는 modified Bessel $K_0$ — *exponential decay* with characteristic length $\sigma_*$.

이는 *near-Gaussian smoothing* (Lorentzian과 Gaussian 둘 다 single peak, exponential tail). 따라서 MAP $\hat{V} \approx G_{\sigma_*} * y$ 의 approximation, $\sigma_*$ 가 noise level 과 signal power 의 비율 결정.

#### 4.7.7 Edge detection — second derivative of MAP

Edge 위치는 $\hat{V}$ 의 *intensity discontinuity*. MAP 자체는 smooth 이므로 edge 는 derivative information 으로 추출. Second derivative:
$$
\Delta \hat{V}(x) = \Delta (G_{\sigma_*} * y)(x) = (LoG_{\sigma_*} * y)(x) \approx (K_{\text{DoG}} * y)(x).
$$

(마지막 등식은 §4.5b.2 의 DoG ≈ LoG.)

#### 4.7.8 결론

### TC-SP-2.3 — [DELETED 2026-05-25 Pass 4 (escalated from Pass 3 WEAKENED)]

**Status**: **DELETED via Pass 4 — weakening insufficient**. Pass 4 의 #46 (DC ξ=0 boundary 의 Wiener filter pole; Q1-Q3 qualifier 가 DC 제외 안 함) + #51 (independent-pixel-noise 가정이 망막에서 위반: shared bipolar input, cone gap-junction) → cumulative 4 patterns → 박탈.

**Original statement**: Gaussian field prior + 1/|ξ|² + Gaussian noise → MAP ≈ DoG.

**Weakening attempt (Pass 3, also DELETED)**: Q1-Q3 (Gaussian field + 1/f² + Gaussian noise) qualifier 추가했으나 sparse coding violation (non-Gaussian) + DC pole + correlated noise 는 fundamental.

**Why DELETED**: DoG ↔ MAP 의 *3중 가정 합의* 가 retinal context 에서 *전부 위반*: (a) sparse coding literature (Olshausen-Field 1996, Ruderman 1994, Simoncelli 1999) 가 non-Gaussian 가정 violation; (b) DC pole 미처리; (c) photoreceptor noise 가 Poisson-dominated, not Gaussian. 정리 자격 없음.

**Replacement**: DoG 의 *biological 적정성* 은 efficient coding (Atick-Redlich 1990; 06 §5.3) 가 더 robust 정당화 — *별도 framework*. DoG = MAP equivalence 는 *suggestive analogy* 로만 유지 (§4.7 본문). 정리 자격 박탈.

### 4.8 Heat equation 관점

Scale-space $G_\sigma * V$ 는 *heat equation* (proper $\sigma$-parametrization) 의 solution:
$$
\partial_\sigma u = \sigma \Delta u, \quad u(x, 0) = V(x)
$$

(또는 $t = \sigma^2/2$ 로 reparametrize: $\partial_t u = \Delta u$.)

DoG ≈ $u(\cdot, \sigma_s) - u(\cdot, \sigma_c)$. 즉, *두 스케일에서의 heat-diffused image 의 차이*.

이는 *finite difference of solutions to heat PDE*. Scale 을 시간으로 본 view.

### 4.9 Laplace-Beltrami 일반화 — Retinal surface 정량

#### 4.9.1 Sphere model

망막은 안구 (대략 구) 의 내부 표면. 반경 $R_{\text{eye}} \approx 12 \text{ mm}$. Foveal area 는 거의 평면 (작은 영역, $\sim 1.5 \text{ mm}$ 직경) 이나 peripheral 은 곡률 무시 불가.

Sphere model:
$$
M = S^2_R := \{ x \in \mathbb{R}^3 : |x| = R \}, \quad R = R_{\text{eye}}.
$$

#### 4.9.2 Geodesic distance

두 점 $p, q \in S^2_R$ 의 geodesic distance:
$$
d_M(p, q) = R \cdot \theta, \quad \cos\theta = \frac{p \cdot q}{R^2}.
$$

작은 $\theta$ 에서 $d_M \approx R \theta = |p - q|_{\text{chord}} \cdot (1 + \theta^2/24 + O(\theta^4))$ — *chord = geodesic + $O(\theta^3)$*.

전형적 retinal patch: 1 mm; $\theta \approx 1/12$ rad $\approx 5°$; $\theta^2 / 24 \approx 0.0003$ — 평면 근사 오차 $0.03\%$. 따라서 foveal-scale 에서 평면 근사 완벽.

Peripheral patch: 5 mm; $\theta \approx 25°$; $\theta^2/24 \approx 0.008$ — $0.8\%$ 오차. 여전히 작음.

#### 4.9.3 Laplace-Beltrami on sphere

Sphere metric (spherical coordinates $(\theta, \phi)$):
$$
ds^2 = R^2 d\theta^2 + R^2 \sin^2\theta \, d\phi^2, \quad g_{ij} = R^2 \, \text{diag}(1, \sin^2\theta).
$$

$g = R^4 \sin^2\theta$, $\sqrt{g} = R^2 \sin\theta$. Laplace-Beltrami:
$$
\Delta_M u = \frac{1}{R^2 \sin\theta} \left[ \partial_\theta(\sin\theta \, \partial_\theta u) + \frac{1}{\sin\theta} \partial_\phi^2 u \right].
$$

작은 $\theta$ 한계 ($\sin\theta \approx \theta$):
$$
\Delta_M u \approx \frac{1}{R^2} \left[ \frac{1}{\theta}\partial_\theta(\theta \partial_\theta u) + \frac{1}{\theta^2} \partial_\phi^2 u \right] = \frac{1}{R^2} \Delta_{\text{polar}}^{(2D)} u.
$$

즉, *flat 2D Laplacian* (polar coordinates 의) 의 $1/R^2$ scaling. 곡률 효과는 $1/R^2$ — small for large eye.

#### 4.9.4 곡률 보정 — Heat kernel asymptotics

Sphere 위 heat kernel:
$$
K_t^M(p, q) = \sum_{\ell=0}^\infty e^{-\ell(\ell+1) t / R^2} \frac{2\ell + 1}{4\pi R^2} P_\ell(\cos\theta_{pq})
$$
where $P_\ell$ 는 Legendre polynomials, $\theta_{pq} = d_M(p,q)/R$.

작은 $t$ 한계:
$$
K_t^M(p, q) \approx \frac{1}{4\pi t} \exp\left( -\frac{d_M(p,q)^2}{4t} \right) \cdot \left( 1 + \frac{t}{6} S(p) + O(t^2) \right)
$$
where $S(p) = 2/R^2$ 는 scalar curvature of sphere. (Minakshisundaram-Pleijel expansion.)

곡률 보정 $tS/6 = t/(3R^2)$. Retinal scale $t \sim \sigma^2 \sim (0.1 \text{ deg})^2 = (0.02 \text{ mm})^2 = 4 \cdot 10^{-4} \text{ mm}^2$; $R^2 = 144 \text{ mm}^2$; ratio $\sim 10^{-6}$. *완전 무시 가능*.

#### 4.9.5 Foveal-peripheral metric scaling

곡률보다 더 큰 효과는 *receptor density* 의 비균질성. Foveal density $\rho_{\text{fov}} \approx 200{,}000/\text{mm}^2$ vs peripheral $\rho_{\text{per}} \approx 5{,}000/\text{mm}^2$ (factor 40).

자연 metric: $g'_{ij} = \rho(x) \cdot g_{ij}^{(\text{flat})}$ — *conformal rescaling*. Receptive field size scales as $1/\sqrt{\rho}$. Laplacian 도 conformal weight:
$$
\Delta_{g'} = \frac{1}{\rho} \Delta_g + \text{lower order}.
$$

DoG $\sigma_c, \sigma_s$ 가 $1/\sqrt{\rho(x)}$ 로 scale → eccentricity scaling. 이는 Stage 3 의 magnification factor 와 연결.

#### 4.9.6 Anisotropic case

일부 망막 영역 (예: streak in cat) 에서 receptive field 는 *anisotropic*. Metric:
$$
g_{ij}(x) = \rho_1(x) e_1^i e_1^j + \rho_2(x) e_2^i e_2^j, \quad \rho_1 \neq \rho_2.
$$

이 경우 $\Delta_g$ 는 *anisotropic diffusion* — Perona-Malik 의 일반화. Human fovea 는 거의 isotropic 이므로 본 논의에서 anisotropic 은 *peripheral correction* 으로 둠.

### 4.10 Wavelet 일반화

DoG 는 *isotropic*. *Anisotropic* (방향성) wavelet (e.g., Gabor, Morlet) 으로 일반화하면 *방향 선택성* 까지 한 번에 — *steerable wavelet basis*.

본 stage 에서는 isotropic DoG (방향 선택성은 §5 의 별도 sub-stage). 더 통합된 모델은 OP-SP-008 (orientation 군론적 정당화).

### 4.11 $\mathcal{K}_{2b}$ — explicit form

$$
\mathcal{K}_{2b} : (V_{\text{ON}}, V_{\text{OFF}}) \mapsto (B_{\text{ON}}, B_{\text{OFF}})
$$

with $B_{\text{ON/OFF}}(x, t) = [K_{\text{DoG}} *_x V_{\text{ON/OFF}}](x, t)$. 결정론적 + thermal noise (작음). 인과적 (공간 합성곱은 시간과 무관).

---

## 5. 시간 미분 + 방향 선택성 — Spatiotemporal filtering

### 5.1 생물학적 사실

- *Amacrine cells*: 시간 미분 + 방향 추출. 30+ 종류.
- *Starburst amacrine (SAC)*: dendrite 의 *원위부* 에서 *근위부* 보다 강한 Ca²⁺ 응답 (Euler et al. 2002) — 한 세포 안에서 *방향성* 신호.
- *Direction-selective ganglion cells (DSGC)*: SAC 입력을 받아 *4 기본 방향* 으로 분기.

### 5.2 Temporal 미분 — Bandpass filter

시간 미분의 단순 형태:

$$
B^T(x, t) = \int_0^t h_T(t - s) B(x, s) ds
$$

with $h_T(t)$ a *bandpass* kernel:

$$
h_T(t) = \frac{d}{dt} \left[ \frac{t^n e^{-t/\tau_1}}{n! \tau_1^{n+1}} \right] - \beta \cdot \frac{d}{dt}\left[ \frac{t^m e^{-t/\tau_2}}{m! \tau_2^{m+1}} \right]
$$

(Adelson-Bergen 형태). $h_T$ 는 *positive lobe + negative lobe* — 미분 + smoothing.

Sustained channel: $h_S$ 는 *lowpass* (no negative lobe).

### 5.3 Adelson-Bergen Motion Energy — Full Fourier proof

#### 5.3.1 Quadrature pair definition

**Definition 5.1**. *Quadrature spatiotemporal Gabor pair*:

$$
G_\theta^{\sin}(x, t) = \sin(\xi_\theta \cdot x - \omega_0 t) \cdot W(x, t)
$$
$$
G_\theta^{\cos}(x, t) = \cos(\xi_\theta \cdot x - \omega_0 t) \cdot W(x, t)
$$

with envelope $W(x, t) := G_{\sigma_x}(x) G_{\sigma_t}(t)$ (separable Gaussian), $\xi_\theta = |\xi_0|(\cos\theta, \sin\theta)$, $\omega_0$ = preferred temporal frequency. Preferred velocity:
$$
v_\theta := \frac{\omega_0}{|\xi_0|} \cdot \hat\theta.
$$

**Definition 5.2**. *Motion energy*:

$$
\boxed{E_\theta(x, t) := \big[ (G_\theta^{\sin} *_{xt} V)(x, t) \big]^2 + \big[ (G_\theta^{\cos} *_{xt} V)(x, t) \big]^2}
$$

#### 5.3.2 Complex form

복소수 Gabor:
$$
G_\theta(x, t) := G_\theta^{\cos} + i G_\theta^{\sin} = e^{i(\xi_\theta \cdot x - \omega_0 t)} W(x, t).
$$

그러면:
$$
E_\theta = |G_\theta * V|^2.
$$

(여기서 $V$ real 가정; $|.|^2$ 가 motion energy.)

#### 5.3.3 Fourier transform of Gabor

Spatiotemporal Fourier $\hat{f}(\xi, \omega) := \iint f(x, t) e^{-i(\xi \cdot x - \omega t)} dx dt$ (convention 으로 *spatial* 부호는 $-i \xi \cdot x$, *temporal* 부호는 $+i\omega t$).

Gabor $G_\theta(x, t) = e^{i(\xi_\theta \cdot x - \omega_0 t)} W(x, t)$ 의 Fourier:

$$
\hat{G_\theta}(\xi, \omega) = \hat{W}(\xi - \xi_\theta, \omega - \omega_0).
$$

(modulation theorem: 시공간 modulation $e^{i(\xi_\theta x - \omega_0 t)}$ 의 Fourier 는 spectrum shift.)

$W$ separable Gaussian → $\hat{W}(\xi, \omega) = e^{-\sigma_x^2 |\xi|^2 / 2} e^{-\sigma_t^2 \omega^2 / 2}$. 따라서:
$$
\hat{G_\theta}(\xi, \omega) = e^{-\sigma_x^2 |\xi - \xi_\theta|^2 / 2} \cdot e^{-\sigma_t^2 (\omega - \omega_0)^2 / 2}.
$$

이는 *spectrum 의 한 점 $(\xi_\theta, \omega_0)$ 주위 Gaussian blob*. Bandwidth $1/\sigma_x$ in $\xi$, $1/\sigma_t$ in $\omega$.

#### 5.3.4 Motion energy in Fourier — slab

합성곱 $G_\theta * V$ 의 Fourier:
$$
\widehat{G_\theta * V}(\xi, \omega) = \hat{G_\theta}(\xi, \omega) \hat{V}(\xi, \omega).
$$

Parseval (energy 가 spectrum integral):
$$
\int |G_\theta * V|^2 dx dt = \frac{1}{(2\pi)^3} \int |\hat{G_\theta}|^2 |\hat{V}|^2 d\xi d\omega.
$$

$|\hat{G_\theta}|^2 = e^{-\sigma_x^2 |\xi - \xi_\theta|^2} e^{-\sigma_t^2 (\omega - \omega_0)^2}$. 이는 *Gaussian blob centered at $(\xi_\theta, \omega_0)$ in spacetime spectrum*.

#### 5.3.5 Velocity slab

Velocity $v$ 의 *rigidly translating* stimulus $V(x, t) = V_0(x - vt)$ 의 spacetime spectrum:
$$
\hat{V}(\xi, \omega) = \hat{V_0}(\xi) \cdot 2\pi \delta(\omega + \xi \cdot v).
$$

즉, *spectrum 이 hyperplane $\omega = -\xi \cdot v$ 위에 집중* — *velocity-determined slab*.

(부호 convention: $V(x, t) = V_0(x - vt)$ 이면 $\hat{V}(\xi, \omega) = \int V_0(x - vt) e^{-i(\xi x - \omega t)} dx dt = \hat{V_0}(\xi) \int e^{-i \xi v t} e^{i\omega t} dt = \hat{V_0}(\xi) \cdot 2\pi \delta(\omega - \xi v)$. 위 부호는 본 문서 convention 에 맞게.)

#### 5.3.6 Gabor 가 slab 의 어디를 sample 하는가

Gabor 의 spectrum center $(\xi_\theta, \omega_0)$ 가 slab $\omega = -\xi \cdot v$ 위에 있을 조건:
$$
\omega_0 = -\xi_\theta \cdot v.
$$

이를 만족하는 velocity:
$$
v = -\frac{\omega_0}{|\xi_0|^2} \xi_\theta = -\frac{\omega_0}{|\xi_0|} \hat\theta.
$$

즉, $|v| = \omega_0 / |\xi_0|$ 의 *Gabor preferred velocity*; 부호는 $-\hat\theta$.

(부호 차이는 convention; "motion in direction $\hat\theta$" 가 어느 spectrum 위치에 대응하는가의 문제.)

#### 5.3.7 TC-SP-2.4 — full proof

### TC-SP-2.4 — [DELETED 2026-05-25 Pass 5 #11 model misspecification]

**Status**: **DELETED via Pass 5 #11**. Adelson-Bergen motion energy 는 *cortical V1 complex cell* 모델 — Mammalian DSGCs 는 *전혀 다른 mechanism* (starburst amacrine cell asymmetric GABAergic inhibition; Euler-Detwiler-Denk 2002, Briggman-Helmstaedter-Denk 2011). DSGCs 의 direction selectivity 는 dendritic Cl⁻ shunting 으로 null-direction 신호를 veto — quadrature Gabor filter 의 energy computation 아님. Math 는 quadrature filter pair 에 correct; 본 stage 의 DSGC 에는 *biologically misapplied*.

**Original statement (preserved for audit trail)**:

> Adelson-Bergen $E_\theta$ 가 velocity slab 의 Gaussian-weighted energy. Slab thickness $\sim 1/\sigma$.

**Why DELETED**: 본 TC 의 정리 *content* (Fourier slab) 는 Gabor pair 에 대해 true 이나, *biological claim* (망막 motion detection) 은 starburst amacrine wiring/timing asymmetry — *별개 객체*. Cortical V1 substrate 와 stage 3 ganglion 사이의 *model 부재* 가 본 TC 의 fundamental gap.

**Replacement**: §5.3 의 Fourier 분석 본문 *mathematical reference* 로 유지 (cortical V1 model 에 적용 가능). DSGC 의 actual mechanism (SAC asymmetric inhibition) 은 추후 별도 OP candidate. TC 자격 박탈.

**증명 sketch**.

Step 1 (Parseval). 위 §5.3.4.

Step 2 (Localization). $|\hat{G_\theta}|^2 = \exp(-\sigma_x^2 |\xi - \xi_\theta|^2 - \sigma_t^2 (\omega - \omega_0)^2)$ 가 $(\xi_\theta, \omega_0)$ 에 집중. 이 집중 영역은 Gaussian blob with widths $1/(\sqrt{2} \sigma_x)$, $1/(\sqrt{2} \sigma_t)$.

Step 3 (Slab 해석). Velocity-tuned: blob center $(\xi_\theta, \omega_0)$ 가 slab $\omega = -\xi \cdot v_\theta$ 위 점. Blob 자체가 slab 와 만나는 형태:
- $\xi$ 방향: blob 폭 $1/\sigma_x$ — frequency selectivity.
- $\omega$ 방향: blob 폭 $1/\sigma_t$ — temporal selectivity.
- Slab 의 *normal direction* 의 폭: $\sim 1/\sigma_t$ (slab 가 $\omega$ 좌표를 결정하므로).

따라서 $E_\theta$ 의 integral 은 $|\hat{V}|^2$ 가 slab 의 width-$1/\sigma_t$ neighborhood 에서 가지는 energy.

Step 4 (Rigorous bandwidth). Sharper statement: $|\hat{G_\theta}(\xi, \omega)|^2$ 의 contour level $|\hat{G_\theta}|^2 \geq e^{-1}$ 의 영역:
$$
\{ (\xi, \omega) : \sigma_x^2 |\xi - \xi_\theta|^2 + \sigma_t^2 (\omega - \omega_0)^2 \leq 1 \}
$$
- ellipsoid with semi-axes $(1/\sigma_x, 1/\sigma_x, 1/\sigma_t)$. 이 ellipsoid 의 중심이 slab 위에 있고, ellipsoid 의 slab-normal extent 가 $1/\sigma_t$.

QED.

**의미**: 운동은 spacetime 에서 *기울어진 줄무늬* — 그 *기울기* 가 velocity. Fourier 도메인에서는 *원점을 지나는 hyperplane*. Motion energy 가 이 hyperplane 의 *narrow tubular neighborhood* 의 energy 를 *위상 불변*으로 추출.

**Phase invariance 의 의미**. $|G^{\cos} * V|^2 + |G^{\sin} * V|^2 = |G_\theta * V|^2$ (complex modulus) — *입력의 absolute phase* 가 무관. 따라서 stimulus 가 sin 이든 cos 이든, square wave 이든, 같은 velocity 이면 같은 energy. 이는 *moving edge* 와 *moving stripe* 가 같은 motion 으로 인지되는 perceptual fact 의 직접 설명.

### 5.4 Reichardt Detector — autocorrelation derivation

#### 5.4.1 Bilinear definition

**Definition 5.3**. *Reichardt detector* (1956):

$$
R_\theta(x, t) := V(x, t) \cdot V(x + \delta \hat\theta, t + \tau) - V(x, t) \cdot V(x - \delta \hat\theta, t + \tau).
$$

#### 5.4.2 Spacetime autocorrelation

**Definition**. Stimulus $V$ 의 spacetime autocorrelation:
$$
\rho_V(\Delta x, \Delta t) := \mathbb{E}[V(x, t) V(x + \Delta x, t + \Delta t)].
$$

(Stationary stimulus 가정 하에서 $\rho_V$ 는 $(x, t)$ 무관.)

#### 5.4.3 Reichardt expectation = autocorrelation difference

$$
\mathbb{E}[R_\theta(x, t)] = \rho_V(\delta \hat\theta, \tau) - \rho_V(-\delta \hat\theta, \tau).
$$

즉, *대칭 autocorrelation 의 antisymmetric 차분*. 이는 $\hat\theta$ 방향으로의 *odd component* 의 측정.

Translation-invariant stimulus 의 경우 $\rho_V$ 가 *even* in spatial argument iff stimulus 가 *non-moving* (또는 random with zero-mean). 이동 stimulus 의 경우 $\rho_V$ 가 *spatial argument 에 대해 asymmetric* — 이게 motion 의 signature.

#### 5.4.4 Rigidly-moving stimulus 의 경우

$V(x, t) = V_0(x - v t)$, $V_0$ stationary random field with autocorrelation $\rho_0$. 그러면:
$$
\rho_V(\Delta x, \Delta t) = \mathbb{E}[V_0(x - vt) V_0(x + \Delta x - v(t + \Delta t))] = \rho_0(\Delta x - v \Delta t).
$$

Reichardt:
$$
\mathbb{E}[R_\theta] = \rho_0(\delta \hat\theta - v \tau) - \rho_0(-\delta \hat\theta - v \tau).
$$

$v = v_0 \hat\theta$ (true $\hat\theta$-motion):
$$
\mathbb{E}[R_\theta] = \rho_0((\delta - v_0 \tau) \hat\theta) - \rho_0((-\delta - v_0 \tau) \hat\theta).
$$

$\rho_0$ even → 차이 가 $v_0 \tau$ 에 *odd dependence*. Maximum when $\delta = v_0 \tau$ (즉 $v_0 = \delta/\tau$ — *preferred velocity of Reichardt detector*).

#### 5.4.5 Motion energy as symmetric autocorrelation — derivation

$E_\theta$ 의 *expected value*:
$$
\mathbb{E}[E_\theta(x, t)] = \mathbb{E}\left[ |G_\theta * V|^2 \right].
$$

Wiener-Khinchin theorem: $\mathbb{E}[|G_\theta * V|^2] = \int |\hat{G_\theta}|^2 S_V d\xi d\omega / (2\pi)^3$, where $S_V$ 는 $V$ 의 power spectrum (= $\hat{\rho_V}$).

Stationary $V$ 의 power spectrum $S_V(\xi, \omega)$ 와 autocorrelation $\rho_V$ 가 Fourier pair. 따라서:
$$
\mathbb{E}[E_\theta] = \int |\hat{G_\theta}(\xi, \omega)|^2 S_V(\xi, \omega) \frac{d\xi d\omega}{(2\pi)^3}.
$$

$|\hat{G_\theta}|^2$ 의 Fourier inverse (= autocorrelation of Gabor envelope shifted to $(\xi_\theta, \omega_0)$). 직접 표현:
$$
\mathbb{E}[E_\theta] = \int \rho_V(\Delta x, \Delta t) \cdot \tilde{g}_\theta(\Delta x, \Delta t) d\Delta x \, d\Delta t
$$
where $\tilde{g}_\theta$ 는 Gabor 의 *autocorrelation function* (자기 자신과의 Fourier-inverse symmetric kernel).

#### 5.4.6 TC-SP-2.5 — full proof

### TC-SP-2.5 — [DELETED 2026-05-25 Pass 5 #11 model misspecification]

**Status**: **DELETED via Pass 5 #11**. Reichardt (Hassenstein-Reichardt 1956, insect lobula plate) 와 Adelson-Bergen (V1 cortical complex cell) 는 둘 다 *non-mammalian-retinal* models — 망막 DSGC 의 starburst amacrine substrate 에 *어느 것도* 직접 적용 안 됨 (TC-SP-2.4 와 동일 issue). 두 model 의 mathematical equivalence 자체는 sound — 그러나 *두 inapplicable models* 의 equivalence 를 증명.

**Original statement (preserved for audit trail)**:

> Stationary + bandwidth matching 하 Reichardt antisymmetric ≈ motion energy antisymmetric (with const C > 0).

**Why DELETED**: Mathematical equivalence between two models 은 true. 그러나 본 TC 가 implicit 으로 claim 하는 *"retinal DSGC implements one or the other"* 는 biologically false. *어느 model 도* 망막에 applicable 하지 않음.

**Replacement**: Mathematical equivalence proof 본문 (§5.4) *cross-model reference* 로 유지. *Retinal application* claim 박탈. 추후 mammalian DSGC 의 starburst amacrine 모델은 별도 OP candidate. TC 자격 박탈.

**증명 sketch**.

Step 1. §5.4.5 의 Wiener-Khinchin 으로 $\mathbb{E}[E_\theta]$ 가 $\rho_V$ 의 Gabor-windowed Fourier coefficient.

Step 2. $E_\theta - E_{-\theta}$ 는 *direction-antisymmetric* component 만 추출. Gabor 의 $\xi_\theta$ vs $\xi_{-\theta} = -\xi_\theta$ Fourier shift 가 spectrum 의 odd 부분만 픽업.

Step 3. Reichardt $R_\theta$ 도 §5.4.3 에서 *autocorrelation 의 antisymmetric 부분*. 두 detector 가 같은 odd component 를 측정.

Step 4. Constant $C$ 는 Gabor envelope width $\sigma_x, \sigma_t$ 와 Reichardt parameter $\delta, \tau$ 의 함수. 두 detector 가 *같은 spacetime frequency band* 를 sample 할 때 $C$ 가 양수 finite. 자세한 식: $C = \int \tilde{g}_\theta(\Delta x, \Delta t) \cdot [\delta_{(\delta \hat\theta, \tau)} - \delta_{(-\delta \hat\theta, \tau)}] dV$ — Gabor autocorrelation 의 antisymmetric sample.

QED (sketch).

**의미**: 두 방식 — *energy-based* (quadratic, biologically: contrast invariant) vs *bilinear* (Reichardt, biologically: pre-DSGC) — 가 *통계적으로 동치*. 실험에서는 둘이 distinguishable in nonlinear regime; mean 수준에서 동치. *Adelson-Bergen 자신의 §4* 가 이 동치성을 explicitly 증명.

**역사적 맥락**: Reichardt 모델 (1956, fly H1) 이 motion detection 의 *first computational theory*. Adelson-Bergen (1985) 의 *energy model* 이 vertebrate cortex (특히 V1 complex cells) 에 더 fitting. 두 모델의 동치성이 *cross-species* unified theory 의 기반.

### 5.5 Optical flow PDE — Brightness constancy & aperture problem

#### 5.5.1 Brightness constancy assumption

가정: stimulus 가 *rigidly moving brightness field*. 즉, 어떤 시각 $t$ 의 위치 $x$ 의 brightness 가 시각 $t + dt$ 에서 위치 $x + v(x, t) dt$ 로 이동 (velocity $v$ 의 vector field 가 위치-시간 의존).

이 가정 하에서:
$$
V(x + v(x,t) dt, t + dt) = V(x, t).
$$

Taylor 전개:
$$
V(x, t) + dt \cdot (\partial_t V + \nabla V \cdot v) + O(dt^2) = V(x, t).
$$

따라서:
$$
\boxed{\partial_t V + \nabla V \cdot v = 0.}
$$

이게 *optical flow constraint equation* (Horn & Schunck 1981).

#### 5.5.2 Aperture problem — rigorous

위 PDE 는 *한* 방정식, *두* unknown ($v_1, v_2$). 따라서 $v$ 의 *한 component* 만 결정.

명시적으로: $\nabla V \cdot v = -\partial_t V$ 는 $v$ 의 *$\nabla V$ 방향 projection* 을 결정:
$$
v_\parallel := \frac{v \cdot \nabla V}{|\nabla V|} = -\frac{\partial_t V}{|\nabla V|}.
$$

*수직 component* $v_\perp$ 는 free. 따라서 *국소* (한 점) 정보로는 motion 방향이 *1-dim 자유도*. 이게 **aperture problem**.

직관: 작은 aperture 를 통해 본 *수평선* 이 위로 움직이면, 수직 component 만 보임; 수평 motion (선 따라) 은 *invisible*. 검정 vertical edge 가 어느 방향으로 가는지 *한 점 정보로 불결정*.

#### 5.5.3 정밀 statement

**Theorem 5.4** (Aperture problem). $V \in C^1$, $\nabla V(x, t) \neq 0$ at point $(x, t)$. 그러면 brightness-constancy constraint
$$
\partial_t V(x, t) + \nabla V(x, t) \cdot v = 0
$$
의 해집합 $\{v \in \mathbb{R}^2 : \text{constraint}\}$ 은 *affine 1-manifold* (line) in $\mathbb{R}^2$:
$$
\{v : v = v_0 + s \mathbf{n}_\perp, \, s \in \mathbb{R}\}, \quad v_0 = -\frac{\partial_t V}{|\nabla V|} \hat\nabla V, \, \mathbf{n}_\perp \perp \nabla V.
$$

따라서 unique velocity 결정 불가; *line of admissible velocities*.

**증명**: 선형 방정식 $\mathbf{a} \cdot v = b$, $\mathbf{a} = \nabla V$, $b = -\partial_t V$. $\mathbf{a} \neq 0$ 이면 해집합 $= b/|\mathbf{a}|^2 \mathbf{a} + \text{null}(\mathbf{a}^T)$. Null space 는 $\mathbf{a}^\perp$ 의 span (1D). QED.

#### 5.5.4 Regularization — Horn-Schunck

해집합을 한 점으로 결정하려면 추가 prior 필요. **Horn-Schunck**: *spatial smoothness* prior. Energy functional:
$$
E[v] = \int_\Omega \left[ (\partial_t V + \nabla V \cdot v)^2 + \lambda (|\nabla v_1|^2 + |\nabla v_2|^2) \right] dx.
$$

Minimization (Euler-Lagrange):
$$
\nabla V (\nabla V \cdot v + \partial_t V) - \lambda \Delta v = 0,
$$
- elliptic PDE in $v$. Unique solution under boundary conditions.

**해석**: 첫 항이 brightness constancy fit, 둘째 항이 smoothness. $\lambda$ 가 trade-off.

#### 5.5.5 Total variation regularization

L²-smoothness 대신 *L¹-gradient* (TV):
$$
E_{TV}[v] = \int [(\partial_t V + \nabla V \cdot v)^2 + \lambda (|\nabla v_1| + |\nabla v_2|)] dx.
$$

이는 *edge-preserving* — motion boundary 에서 discontinuity 허용. 현대 optical flow 알고리즘 (Brox 2004, Sun 2010) 의 표준.

#### 5.5.6 DSGC 와의 연결

망막 DSGC 는 *4 기본 방향* 만 reporting:
$$
\{v_{\theta_0}, v_{\theta_1}, v_{\theta_2}, v_{\theta_3}\}, \quad \theta_i = i \cdot \pi/2.
$$

각각이 brightness-constancy PDE 의 4 projection. *Full $v$ reconstruction* 은 4 channels 의 linear combination — V1 cortical 작업. 따라서 망막은 *partial optical flow* (per-channel) 만 encode; full optical flow 는 후속.

이 분업 의 *정보론적 효율*: 4 채널만으로 $v \in \mathbb{R}^2$ 의 *redundant overcomplete representation* — robust to noise, 그러나 단일 채널은 aperture-limited. 후속 cortical integration 이 full $v$ 복원.

#### 5.5.7 Lie 미분 관점

$v$ 가 vector field on $\Sigma_{\text{ret}}$ 라면, $V$ 의 시간 진화는 *$v$ 를 따라가는 brightness 가 보존*:
$$
\mathcal{L}_v V + \partial_t V = 0
$$
where $\mathcal{L}_v$ 는 Lie 미분 = $\nabla V \cdot v$ in 표준 좌표.

Tangent bundle 관점: $v \in \Gamma(T\Sigma_{\text{ret}})$. 따라서 *motion field* 는 *tangent bundle 의 section*. DSGC 가 이 section 을 *4 기본 방향 basis* 로 *분해*. (4 방향이 *frame* of tangent bundle.)

### 5.6 Direction-selective ganglion cell (DSGC) 분기

$\mathcal{K}_{2c}$ 의 출력 — 각 채널 ($\theta_0, \theta_1, \theta_2, \theta_3$) 의 4 motion-energy 응답:

$$
\mathcal{K}_{2c} : (B_{\text{ON}}, B_{\text{OFF}}) \mapsto \big( E_{\theta_0, \text{ON}}, E_{\theta_1, \text{ON}}, \ldots, E_{\theta_3, \text{OFF}}; \; S_{\text{ON}}, S_{\text{OFF}}\big)
$$

with 4 방향 $\times$ 2 부호 = 8 motion 채널 + sustained $S_{ON/OFF}$ 채널 (sustained 는 transient 의 lowpass 짝).

### 5.7 시간 인과성

§3 의 SDE 와 마찬가지로 시간 합성곱은 *past only* — $h_T(t) = 0$ for $t < 0$. Adelson-Bergen Gabor 의 시간 부분도 causal version 채택 ($G_{\sigma_t}^{\text{causal}}$). 따라서 [[01_framework_master#TC-SP-1.3|01 TC-SP-1.3]] 의 stage 2 측 보장.

---

## 6. 색 대립 — Cone type 의 비교

### 6.1 생물학적 사실

3 cone type (L, M, S) 의 출력이 *대립축* 으로 재조합:

- **L-M axis**: red-green 대립 (parvocellular, midget 경로)
- **S-(L+M) axis**: blue-yellow 대립 (koniocellular, bistratified 경로)
- **L+M axis**: 휘도 (luminance, achromatic; magnocellular 경로)

각 축은 *반대 방향* 의 정보를 함께 운반 (push-pull 부호).

### 6.2 수학적 형식 — 색 변환 행렬

$(V_L, V_M, V_S)$ 입력 (광수용기 stage 의 cone 출력) 을 $(L\text{-}M, S\text{-}(L\text{+}M), L\text{+}M)$ 로 선형 변환:

$$
\begin{pmatrix} V_{L-M} \\ V_{S-(L+M)} \\ V_{L+M} \end{pmatrix}
= \mathbf{C} \begin{pmatrix} V_L \\ V_M \\ V_S \end{pmatrix},
\quad
\mathbf{C} = \begin{pmatrix} 1 & -1 & 0 \\ -1/2 & -1/2 & 1 \\ 1 & 1 & 0 \end{pmatrix}
$$

(정확한 weights 는 사람마다 미세 차이; cone 응답 normalization 후 가정.)

### 6.3 PCA derivation — full

#### 6.3.1 자연 광원의 spectrum statistics

자연 영상의 각 픽셀 stimulates 3 cones with response vector $\mathbf{V} = (V_L, V_M, V_S)^T$. 자연 영상 ensemble 에서 covariance:
$$
\Sigma_{\text{nat}} := \mathbb{E}[(\mathbf{V} - \bar{\mathbf{V}})(\mathbf{V} - \bar{\mathbf{V}})^T] \in \mathbb{R}^{3 \times 3}.
$$

#### 6.3.2 Empirical measurement (Ruderman-Cronin-Chiao 1998)

Ruderman, Cronin & Chiao (1998) "Statistics of cone responses to natural images" 의 측정 (5000+ images, hyperspectral camera). Normalized $\Sigma_{\text{nat}}$ (log-cone response):

$$
\Sigma_{\text{nat}} \approx \begin{pmatrix} 1.0 & 0.96 & 0.69 \\ 0.96 & 1.0 & 0.78 \\ 0.69 & 0.78 & 1.0 \end{pmatrix}
$$

(diagonal 정규화, off-diagonal = correlation coefficient.) 핵심 fact: $L, M$ 강한 상관 ($r \approx 0.96$), $S$ 와는 약한 상관 ($\sim 0.7$).

#### 6.3.3 PCA — eigendecomposition

$\Sigma_{\text{nat}} = U \Lambda U^T$ with $\Lambda = \text{diag}(\lambda_1, \lambda_2, \lambda_3)$, $\lambda_1 \geq \lambda_2 \geq \lambda_3$.

Ruderman et al. 의 numerical eigendecomposition (log-cone, normalized):

| eigenvalue | eigenvector (approximate) | 의미 |
|------------|---------------------------|------|
| $\lambda_1 \approx 2.81$ | $(0.58, 0.59, 0.55)^T$ | $\approx (L + M + S)/\sqrt{3}$ — luminance |
| $\lambda_2 \approx 0.16$ | $(0.71, -0.70, -0.05)^T$ | $\approx (L - M)/\sqrt{2}$ — red-green |
| $\lambda_3 \approx 0.03$ | $(0.40, 0.40, -0.83)^T$ | $\approx (L + M - 2S) / \sqrt{6}$ — blue-yellow |

Variance ratios: $\lambda_1 : \lambda_2 : \lambda_3 \approx 94\% : 5\% : 1\%$. *Luminance dominates*, chromatic information 작음. 이는 자연 영상의 *grayscale-dominant* 특성.

#### 6.3.4 PCA → biological axes

Biological cone-opponent axes:
- $\text{Lum} = L + M$ (no $S$ contribution in magnocellular)
- $\text{RG} = L - M$
- $\text{BY} = S - (L + M)/2$

PCA axes:
- PC1 $\approx (L + M + S)/\sqrt{3}$ — close to $L + M$ but with $S$ contribution
- PC2 $\approx (L - M)/\sqrt{2}$ — exactly red-green
- PC3 $\approx (L + M - 2S)/\sqrt{6}$ — close to blue-yellow (up to sign)

**Match**: PC2 = biological RG exactly (up to scale). PC3 $\propto $ -BY (biological), sign flip. PC1 $\neq$ biological Lum exactly — biological Lum has 0 $S$ weight, PC1 has $\sim 0.55 S$ weight.

차이의 origin: biological luminance pathway (magnocellular) *excludes* $S$ cones (M cells lack $S$-input) — 이는 PCA 의 *통계 최적* 가 아닌 *진화적 분업* (m-pathway 는 high-temporal-resolution, S cone 은 too slow).

#### 6.3.5 Decorrelation result

After PCA transformation, channels have *zero correlation*:
$$
\text{Cov}(\text{PC}_i, \text{PC}_j) = \lambda_i \delta_{ij}.
$$

즉, 새 채널들은 *independent* (적어도 second-order). 정보 전송 효율 향상 — channel capacity 가 *각 채널 separately* compute 가능.

#### 6.3.6 TC-SP-2.6 — refined

### TC-SP-2.6 — [DELETED 2026-05-25 Pass 5 #11 model misspecification]

**Status**: **DELETED via Pass 5 #11**. PCA *find* optimal axes for variance representation of measured LMS responses (mathematical fact). 그러나 *biological claim* "L-M / S-(L+M) opponency arises from PCA optimization" 은 *causal direction confusion*: L, M cone opsins 가 primate trichromacy 정제 *이전* 에 진화함 (Mollon 1989, Jacobs 2009); L-M wiring 은 *random-wiring statistical accident* in non-foveal retina (Crook et al. 2011); L-M opponency 는 midget privatization for spatial acuity 의 *byproduct* 일 가능성.

**Original statement (preserved for audit trail)**:

> L-M, S-(L+M), L+M 변환 ≈ PCA 의 첫 3축 (variance 94%:5%:1%).

**Why DELETED**: *Alignment* (PCA axes ≈ biological channels) 은 numerical fact. *Causal optimization* (PCA → biology) 은 정당화 안 됨 — *phylogenetic accident* 가 alternative explanation 으로 ruling out 안 됨. TC 의 "optimality" claim 자격 없음.

**Replacement**: PCA eigendecomposition 본문 (§6.3) 은 *empirical alignment observation* 으로 유지. *Causal optimality* claim 박탈. OP-SP-004 (색 대립의 군론적 정당화) 와 통합 가능.

**증명 가능성**: 위 §6.3.3 numerical. 분석적 statement 는 *natural spectral statistic* 의 가정 (specifically: spectral power law + smooth photopic reflectance) 에 의존; Buchsbaum-Gottschalk (1983) 이 분석적 모델 제시.

**의미**: 색 대립축은 진화의 *임의 선택* 이 아니라 *통계적 정보 최대화* 의 결과. Magnocellular pathway 의 S-exclusion 만 진화적 special-case. 본 디렉토리는 이 candidate 를 등록만; 정확한 분석적 정당화는 OP-SP-004.

### 6.4 Group-theoretic view — SO(3) on color space

#### 6.4.1 Chromaticity manifold

Color는 3-cone response space $\mathbb{R}^3_+$ (positive cone) 의 원소. *Chromaticity* 는 luminance-normalized: $\mathbf{V}/(V_L + V_M + V_S) \in $ 2-simplex $\Delta^2$ (또는 projectively, $\mathbb{P}^2$).

#### 6.4.2 SO(3) action — chromatic adaptation

*Chromatic adaptation* (von Kries): illuminant 변화 시 cone responses 가 *diagonal scaling*:
$$
\mathbf{V} \mapsto D \mathbf{V}, \quad D = \text{diag}(d_L, d_M, d_S).
$$

이는 SO(3) action 이 아닌 *positive diagonal scaling* $\mathbb{R}^3_+$ — group $(\mathbb{R}^+)^3$ (diagonal positive matrices).

True SO(3) action: rotation of cone response space. 이는 *물리적* 의미 약함 (cone fundamentals 가 fix); 그러나 *PCA 후* 의 chromatic plane 에서는 rotation 이 의미 — *hue* 가 PC2-PC3 plane 의 angle.

#### 6.4.3 Orbits of SO(3) on chromaticity

PC2-PC3 plane (chromatic plane) 에 restrict 한 SO(2) (planar rotation) action 의 orbit:
- *Trivial orbit*: origin = achromatic (gray).
- *Circular orbits*: constant chroma, varying hue.

이 orbit 구조가 *hue circle* 의 수학적 정당화. Munsell color space, CIELAB 의 $a^* b^*$ plane 모두 이 SO(2) orbit 구조의 변형.

#### 6.4.4 SU(3) speculative — OP-SP-004

QCD-like SU(3) on color (Wyszecki-Stiles 의 chromatic Lie 분석): cone types 가 *fundamental representation* of SU(3)? Higher representations (8-dim adjoint 등) 이 perceptual color phenomena (예: complementary, intermediate hues) 에 mapping?

이는 *highly speculative* — 본 디렉토리는 OP-SP-004 로만 등록.

### 6.5 OP-SP-004 — 색 대립의 군론적 정당화

**Status**: OPEN. Severity: High.

**문제**: PCA 가 *통계적* 정당화이나 *수학적 필연* 인가? 다른 가능한 결정 원리:

- *Lie group representation*: chromaticity 가 어떤 Lie group ($SU(3)$, $SO(3)$, ...) 의 *기약 표현* 으로 분해되는가?
- *Symmetry breaking*: ancestral 4 cone (UV + L + M + S) 에서 mammalian 3 cone 으로의 *진화적 symmetry breaking* 이 어떤 representation 보존 / 파괴?
- *Information geometry*: chromaticity manifold 의 *Fisher metric* 의 principal axes?

**Candidate 해법 방향**: representation theory of $SO(3)$ on color space (§6.4.3 의 hue circle SO(2) 와 luminance 의 product 가 $SO(2) \times \mathbb{R} \subset SO(3)$ 의 부분군?); Wyszecki-Stiles 의 chromatic Lie group 분석.

본 디렉토리는 *open* 으로 등록만.

### 6.6 OP-SP-003 — 다채널 분기의 fiber bundle 형식

**Status**: OPEN. Severity: Medium.

**문제**: §1.2 의 $\mathcal{S}_2 = \bigoplus_c C(\Sigma \times \mathbb{R}^+, \mathbb{R}^+)$ 는 단순 direct sum. 그러나 채널들이 *완전 독립* 이 아님 — 동일 광수용기 입력에서 *공통 분기*. 따라서 더 자연스러운 형식은 *fiber bundle*:

$$
\pi : E \to \Sigma \times \mathbb{R}^+, \quad \pi^{-1}(x, t) = \mathcal{C}\text{-fiber}
$$

각 점 위의 fiber 가 채널 공간. $\mathcal{K}_{2a/b/c/d}$ 가 *bundle section* 들 사이의 morphism.

**Candidate 해법**:
- Trivial bundle: $E = \Sigma \times \mathcal{C}$ (간단하지만 채널 inter-relation 손실)
- Associated bundle: $E = P \times_G F$ where $P$ 는 *frame bundle*, $G$ 는 채널 symmetry group
- Sheaf 표현: $\mathcal{F}(U) = \{$ 채널 응답 on $U \}$, gluing axiom

본 디렉토리는 *open* 으로 등록만.

---

## 7. $\mathcal{K}_2$ — 통합 form

### 7.1 합성

$$
\mathcal{K}_2 = \mathcal{K}_{2d} \circ \mathcal{K}_{2c} \circ \mathcal{K}_{2b} \circ \mathcal{K}_{2a}
$$

위 4 sub-stage 모두 (mostly) deterministic. 작은 thermal noise 와 graded 한계의 stochasticity 는 각 stage 의 $\sigma_V dW_t$ 항으로 carry-along.

### 7.2 인과성

모든 sub-stage 가 인과적 → 합성도 인과적 ([[01_framework_master#TC-SP-1.3|01 TC-SP-1.3]]).

### 7.3 평균 회계

평균 응답:

$$
\mathbb{E}[B_{c}(x, t)] = (K_c *_{xt} \mathbb{E}[V](x, t))
$$

with $K_c$ a channel-specific spatiotemporal kernel (DoG + temporal bandpass + direction selectivity + color weight).

비선형 부분 (rectification, Naka-Rushton-like) 은 *higher Volterra terms* 으로 carry. 평균 수준에서는 linear filter bank 로 정리.

### 7.4 출력 dimensionality

입력: $V \in C(\Sigma \times \mathbb{R}^+, \mathbb{R})$ — 단일 channel.
출력: $B \in \bigoplus_{c \in \mathcal{C}} C(\Sigma \times \mathbb{R}^+, \mathbb{R}^+)$ — 48 channels (cross-product upper bound).

따라서 **dimensionality $\times 48$ 증가**. 이는 *redundancy 증가* 가 아니라 *분해 다양화* — 동일 정보를 *다른 방식* 으로 표현.

정보론적으로는 (TC-SP-1.2 DPI 에 의해) 정보 *증가* 불가. 그러나 *접근성* (해독 용이성) 은 증가 — TC-SP-4.3 의 정신.

---

## 8. 도구 사용 summary

본 stage 에서 사용된 도구:

| 도구 ([[01_framework_master#4. 수학적 도구 카탈로그|01 §4]]) | 사용 |
|------|------|
| 4.3 함수해석 | Riesz lattice 분해 (§3.3); positive cone 의 (C1)(C2)(C3) 성질 (§3.2.2); cone graded calculus (§3.2.3) |
| 4.4 합성곱 대수 | DoG (§4.2); spatiotemporal Gabor (§5.3); Fourier transform 의 modulation theorem (§5.3.3); Wiener filter (§4.7.6) |
| 4.5 Scale-space | Heat equation with $\sigma$-derivative (§4.5b.1); Lindeberg-Koenderink LoG 근사 (§4.5b.2-3); Marr-Hildreth (§4.6) |
| 4.6 미분기하 | Laplace-Beltrami on $S^2_R$ (§4.9.3); heat kernel on sphere (§4.9.4); conformal rescaling (§4.9.5); tangent bundle motion (§5.5.7); fiber bundle (OP-SP-003) |
| 4.7 시공간 분석 | Adelson-Bergen energy + velocity slab (§5.3); Reichardt-energy autocorrelation 등가 (§5.4); optical flow PDE + aperture problem (§5.5.2-3); Horn-Schunck regularization (§5.5.4) |
| 4.8 정보이론 | Decorrelation via PCA (§6.3.5); whitening (§10.1) |
| 4.9 대수위상 | sheaf representation (OP-SP-003) |
| 4.11 OT | (not used in Stage 2; appears in Stage 3 spike comparison) |
| 4.12 군이론 | translation equivariance (§4.4); SO(2) on chromatic plane (§6.4.3); SO(3) / SU(3) speculative (§6.4.4) |
| 4.13 변분 | Horn-Schunck quadratic (§5.5.4); Olshausen-Field sparse coding (§10.2) |

전 stage 중에서 가장 다양한 도구 사용 — inner retina 가 *대부분의 가공* 을 수행.

---

## 9. (Ω, σ) Tier 2 mapping (preview)

[[07_omega_sigma_lift|07]] 에서 본격. Stage 2 의 직접 매핑:

- $\Omega_2 = \Sigma_{\text{ret}} \times \mathbb{R}^+ \times \mathcal{C}$ — 시공간-채널 격자
- $\sigma_2 = $ 시공간 인접 (각 채널 내) + *채널-간 cross-link* (e.g., ON channel 의 $(x, t)$ ↔ OFF channel 의 $(x, t)$ — *대립 쌍*)

채널 cross-link 의 정확한 정의는 OP-SP-003 (fiber bundle 형식) 과 묶임. 본 문서에서는 *위상학적 존재* 만 명시.

---

## 10. Whitening + sparse coding view — Atick-Redlich 와 Olshausen-Field 의 통합

본 절은 v1 에 신설. Inner retina 의 ON/OFF + DoG 의 *정보론적 origin* 을 *whitening* 으로 해석하고, 후속 V1 simple cells 의 *sparse coding* 과의 연속성을 보인다.

### 10.1 Atick-Redlich efficient coding — DoG ≈ whitening

#### 10.1.1 자연 영상 spectrum

자연 영상 $V$ 의 *power spectrum*:
$$
S_V(\xi) := |\hat{V}(\xi)|^2 \approx \frac{A}{|\xi|^2}
$$

(spatial-only; Field 1987). $1/|\xi|^2$ power law.

#### 10.1.2 Whitening filter — definition

신호 $V$ 의 *whitening* (또는 *decorrelation*) 은 변환 $W: V \mapsto V'$ such that $V'$ 의 spectrum 이 *flat*:
$$
S_{V'}(\xi) = |\hat{W}(\xi)|^2 S_V(\xi) = \text{const}.
$$

따라서 whitening filter $\hat{W}(\xi) = c \sqrt{1/S_V(\xi)} = c |\xi|$ — *high-pass*.

#### 10.1.3 Atick-Redlich (1990) — noise-limited whitening

Pure whitening 은 high-frequency noise 을 *amplify*. Information-theoretic optimum (Atick-Redlich 1990): noise 가 있을 때 *modified whitening*:
$$
\hat{W}_{\text{AR}}(\xi) = \frac{|\xi|}{\sqrt{S_V(\xi) + S_N(\xi)/|\xi|^2}} \cdot e^{-(\xi/\xi_c)^4}
$$

(lowpass envelope cuts off high-freq noise; lowpass 의 정확한 형태는 SNR 의존.)

#### 10.1.4 결과: bandpass shape ≈ DoG

위 $\hat{W}_{\text{AR}}$ 의 magnitude:
- Low freq: $\sim |\xi|$ → high-pass behavior (DC suppression)
- High freq: lowpass envelope → high-cutoff
- Peak at intermediate $|\xi|$

이 *bandpass shape* 가 §4.5.5 의 DoG bandpass peak 와 *qualitatively* 일치. Atick-Redlich (1992) 의 explicit fit: retinal ganglion cell SF tuning 이 efficient-whitening prediction 과 잘 맞음.

**결론**: DoG 는 *biological accident* 가 아니라 *natural-image statistics + noise-limited efficient coding* 의 직접 결과. 진화가 이 information-theoretic optimum 에 수렴.

#### 10.1.5 ON/OFF split = encoding positivity constraint

Whitening 의 출력은 *signed*. Neural firing rate 는 *nonnegative*. 따라서 signed signal $W * V$ 를 nonnegative form 으로 encode 하려면:
$$
(W * V)^+ \text{ and } (W * V)^- \text{ 분리.}
$$

이게 정확히 ON/OFF split (§3.2). 따라서 **ON/OFF + DoG 합계 = whitening + positivity-encoding**.

이 view 에서 Inner retina = *efficient coding* (whitening) + *physical constraint encoding* (firing rate ≥ 0).

### 10.2 Olshausen-Field sparse coding — downstream V1

#### 10.2.1 Sparse coding hypothesis

Olshausen & Field (1996, "Emergence of simple-cell receptive field properties by learning a sparse code for natural images"): V1 simple cell receptive fields = *sparse* representation of natural images.

Setup. Image patch $\mathbf{x} \in \mathbb{R}^n$ ($n$ = pixels). Representation:
$$
\mathbf{x} = \sum_i a_i \phi_i + \epsilon, \quad a_i \in \mathbb{R}, \phi_i \in \mathbb{R}^n \text{ basis}.
$$

Sparse objective:
$$
\min_{\{\phi_i\}, \{a_i\}} \sum_{\mathbf{x}} \left[ \|\mathbf{x} - \sum_i a_i \phi_i\|^2 + \lambda \sum_i |a_i| \right]
$$
($L^1$ penalty on activations $a_i$ → sparsity.)

#### 10.2.2 결과 — V1-like receptive fields

학습 후 $\phi_i$ 들이 *Gabor-like*: localized, oriented, bandpass. 매우 V1 simple cells 와 닮음. *Spontaneous emergence* — biological architecture 강요 없음.

#### 10.2.3 Inner retina = preprocessing for sparse coding

Olshausen-Field 가입력으로 받는 *natural images* 는 raw photoreceptor data 가 아닌 *whitened* data 가 더 효과적. 이유:
- Raw images: $1/|\xi|^2$ spectrum → low frequencies 강제 dominant → learned basis 가 low-freq blob.
- Whitened (DoG-preprocessed): flat spectrum → all frequencies equally weighted → learned basis 가 Gabor-like.

따라서 **retina + V1 분업**:
- *Retina (inner)*: whitening + positivity (§10.1)
- *V1 simple cells*: sparse code learned on whitened input (§10.2)

두 단계가 *합쳐서* 자연영상의 efficient sparse representation. *각각 따로* 는 suboptimal.

#### 10.2.4 Sparse coding 의 information-theoretic 정당화

Sparse code = *high entropy per active unit* (각 활성 unit 가 informative). $L^1$ penalty 는 *factorial code* 근사:
$$
P(a_1, \ldots, a_n) \approx \prod_i P(a_i),
$$
- channels 가 거의 independent. *Decorrelation* 의 nonlinear 확장.

Whitening (linear decorrelation) → sparse coding (nonlinear factorization) 의 *cascade* 가 *information-maximization* 의 점진적 구현.

#### 10.2.5 ICA 와의 관계

*Independent Component Analysis* (ICA): sparse coding 의 statistical interpretation. Natural images 의 ICA components 도 Gabor-like (Bell & Sejnowski 1997).

PCA (linear decorrelation) → ICA (statistical independence) → sparse coding (nonlinear, $L^1$ regularization) 의 hierarchy. Retina = PCA-like + whitening; V1 = ICA-like + sparse.

### 10.3 통합 view — Stage 2 의 정보론적 raison d'être

**핵심 주장**: Stage 2 (inner retina) 의 모든 operations 는 *one principle* — *efficient information transmission through neural channels with positivity constraint*:

1. **DoG (§4)**: spatial whitening (Atick-Redlich).
2. **Temporal bandpass (§5.2)**: temporal whitening — 자연 영상 temporal spectrum 도 $1/\omega^2$.
3. **ON/OFF split (§3)**: positivity encoding of signed whitened signal.
4. **Color opponency (§6)**: chromatic decorrelation (Buchsbaum-Gottschalk, Ruderman-Cronin-Chiao).
5. **DSGC (§5.3-5.6)**: spatiotemporal slab selectivity = velocity-tuned whitening.

위 5가지가 *모두 같은 information-theoretic principle 의 다른 측면*. Inner retina 는 *single computational principle* 의 *multi-dimensional implementation*.

V1 의 sparse coding 은 이 whitened multi-channel representation 위에서 *next-level optimization* — local features 의 sparse basis.

이 view 에서 Stage 2 의 *48 채널 expansion* 은 *redundancy* 가 아니라 *whitened signal 의 efficient multi-axis decorrelation* — 각 채널이 different feature direction 의 *decorrelated representation*.

---

## 11. 본 stage 가 *시도하지 않는 것*

- 채널 간의 *완전 형식* — fiber bundle / sheaf 의 정확한 commitment (OP-SP-003)
- 색 대립축의 *제일 원리* 정당화 (OP-SP-004; PCA + SO(3) hint 만)
- DSGC 의 *4 방향이 왜 4 인가* 의 정당화 (군론적 — 별도 OP)
- *Wide-field amacrine cells* 의 광역 게인 컨트롤 (adaptation; OP-SP-009)
- *Polyaxonal amacrine* 의 long-range integration (별도)
- §10 의 whitening hypothesis 의 *quantitative experimental fit* (Atick-Redlich 1992 referenced, not re-derived)

---

## 12. 다음 stage 입력 type

[[05_stage3_ganglion_spike_encoding|05]] 가 받는 입력:

- $B = (B_c)_{c \in \mathcal{C}} \in \mathcal{S}_2$
- 각 $B_c$ 는 $\mathbb{R}^+$-valued graded 신호
- 시공간 인과적
- 다양한 채널-specific spatiotemporal filter 의 출력 (whitened, sparsified-ready)

Stage 3 의 작업: 각 채널을 *spike train* 으로 변환 + 신경절세포 type 분기 (M / P / K) + 압축 (126:1).

---

*Stage 2 v1. 후속: [[05_stage3_ganglion_spike_encoding]]. 노출 type: $B \in \mathcal{S}_2$, 48 채널 multichannel graded 신호. TC-SP-2.1 ~ 2.6 등록 with full proof sketches (v1 expansion). OP-SP-003, OP-SP-004 등록. §10 신설: whitening + sparse coding 통합 view.*
