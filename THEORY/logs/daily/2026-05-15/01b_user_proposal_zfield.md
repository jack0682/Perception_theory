---
type: log/daily/user_proposal
date: 2026-05-15
author: 사용자 (작성: 2026-05-14 저녁)
session_label: W7-Day6 brainstorm input
canonical_version: CV-1.15 (sealed, untouched)
status: 사용자 직접 브레인스토밍 메모 — 검토 입력
working_name: D0D1_Cohesion_Genesis
---

> [!nav] Linked: [[00_plan]] · [[01_pre_brainstorm]] · [[DECLARATION]]


# 01b — 사용자 브레인스토밍 메모: z_t / K_{z_t} / u_t^* 경로

**본 파일은 사용자가 2026-05-14 저녁 직접 작성한 브레인스토밍 메모를 그대로 보존한 것이다. assistant 의 재해석이 아니라 *사용자 자신의* 다음 작업 제안.**

---

## 핵심 한 줄

> 핵심은 *u_t 단일장 가정을 버릴지 말지가 아니라*, *u_t 가 무엇의 장인가를 다시 명확히 하는 것* 이다.

---

## 진단: 왜 V-AFD/R-2 가 language refactoring 으로 끝났는가

SCC canonical 은 기본적으로 $u_t : X_t \to [0,1]$ 에서 *시작* 한다. 즉 *이미 하나의 scalar cohesion field 가 주어져 있다.*

그런데 사용자가 진짜 묻고 있는 질문은 *그보다 앞선다*:

> 색, 밝기, 깊이, 질감, 운동, 방향성 같은 *다채널 차이* 가 어떻게 *하나의 응집장 $u_t$ 로* 굳어지는가?

즉 핵심은 **D_0 → D_1**:
- $D_0$ = 전-응집 감각 미분
- $D_1$ = 응집된 cohesion field

문제는 기존 SCC 가 *이미 D_1 부터 시작* 했다는 점. 그래서 D_0 → D_1 을 설명하려고 하면 canonical 안에는 *도구가 부족*. 그 결과:
- V-AFD = 추상 dynamics vocabulary
- R-2 = K/readout vocabulary refactor

---

## 1. u_t 단일장이 문제인가?

**결론:**

> u_t 단일장 가정 자체는 *문제가 아니다*.

문제는 **u_t 를 raw primitive 처럼 다룬 것**.

더 정확히는:

> $u_t$ 는 *감각 원자료가 아니라*, *응집 참여도 (order parameter)* 여야 한다.

즉 u_t 는 색·밝기·깊이·질감 *자체* 가 아니라, 그것들이 *관계적으로 통합된 뒤* 생기는 "이 지점이 어떤 응집에 얼마나 참여하는가" 의 scalar field.

**단일장 가정 유지 가능.** 다만 이렇게 고침:

| 기존 | 새 후보 |
|---|---|
| $(X_t, u_t)$ | $(X_t, z_t, u_t)$ |

여기서:
- $z_t : X_t \to \mathcal{F}$ — 다채널 감각 미분장
- $\mathcal{F}$ — color, depth, texture, motion, orientation, semantic cue 를 포함하는 feature space
- $u_t : X_t \to [0,1]$ — 그 위에서 형성되는 scalar cohesion order parameter

---

## 2. 새 경로

기존 deadlock:

$$D_0 \to D_1 \text{ 설명 필요}$$

그런데 가용 도구가 saliency, PCA, clustering, learned fusion 같은 *engineering proxy* 뿐 — SCC 가 거부.

**새 경로:**

$$\boxed{D_0 = z_t \to K_{z_t} \to \mathcal{E}(u; z_t) \to u_t^*}$$

즉 $z_t$ 가 *직접* $u_t$ 를 만들지 않음. $z_t$ 는 **관계 커널** $K_{z_t}(x,y)$ 를 만들고, SCC energy 가 그 커널 위에서 u 를 안정화:

$$u_t^* = \arg\min_{u \in \Sigma_m} \mathcal{E}(u; z_t)$$

→ D_0 → D_1 을 *engineering fusion 이 아니라* **variational field stabilization** 으로 설명.

---

## 3. 핵심 수식 후보

전-응집 감각장:

$$z_t : X_t \to \mathcal{F}$$

관계 커널 예시:

$$K_{z_t}(x,y) = \exp\left(-\frac{d_X(x,y)^2}{2\rho^2}\right) \exp\left(-\frac{d_\mathcal{F}(z_t(x), z_t(y))^2}{2\sigma^2}\right)$$

- $d_X$ — 공간/시야상 거리
- $d_\mathcal{F}$ — feature-space 거리

SCC 연산자가 $K_{z_t}$ 에 의존:

- $\mathrm{Cl}_{z_t}(u)$
- $D_{z_t}(x; 1-u)$
- $E_\mathrm{bd}(u; K_{z_t})$

최종 응집장:

$$\boxed{u_t^* = \arg\min_{u \in \Sigma_m} \left[\lambda_\mathrm{cl} E_\mathrm{cl}(u; z_t) + \lambda_\mathrm{sep} E_\mathrm{sep}(u; z_t) + \lambda_\mathrm{bd} E_\mathrm{bd}(u; z_t)\right]}$$

즉 $u_t$ 는 *주어진 것이 아니라*, $z_t$ 위에서 *안정화된 해*.

---

## 4. 이것이 중요한 이유

기존 SCC 의 근본 가정이 *크게 깨지지 않음*.

**유지되는 것:**
- $u_t : X_t \to [0,1]$
- $\Sigma_m$
- $E(u)$
- Bind, Sep, Inside, Persist

**새로 추가되는 것:**
- $z_t : X_t \to \mathcal{F}$
- $K_{z_t}$
- $u_t^* = \arg\min \mathcal{E}(u; z_t)$

즉 SCC 는 더 이상 "*$u_t$ 가 있다고 치자*" 에서 멈추지 않고:

> 다채널 감각 미분이 어떻게 scalar cohesion field 로 안정화되는가

를 다룰 수 있다. **이것이 진짜 D_0 → D_1 문제.**

---

## 5. 단일장 vs 다중장 — 내일 따져볼 논점

**Q1.** $u_t$ 는 정말 scalar 하나로 충분한가?

| 가능성 | 형태 | 평가 |
|---|---|---|
| 1 | $u_t : X_t \to [0,1]$ — 단일 scalar cohesion participation field | 안전, 기존 유지 |
| 2 | $U_t : X_t \to [0,1]^r$ — 다중 aspect cohesion field | r 이 K 처럼 행동할 위험; r 은 object count 가 아니라 feature-aspect dimension 이어야 |

예: $U_t = (u^\text{color}, u^\text{depth}, u^\text{motion}, u^\text{texture})$ — 그러나 이 경우에도 $U_t \to u_t$ 통합 문제 발생.

**우선 단일장 유지가 더 안전:**

> $z_t$ 는 다채널, $u_t$ 는 단일 order parameter.

이 구도가 가장 덜 파괴적.

---

## 6. 내일의 핵심 질문

> $u_t$ 를 *primitive* 로 둘 것인가, 아니면 $z_t$ 위의 *variational solution* 으로 둘 것인가?

| 선택 | 형태 | 장점 | 단점 |
|---|---|---|---|
| **A** | $u_t$ primitive (기존) | canonical 안정 | D_0 → D_1 설명 불가; H-MORSE 내부로 후퇴 |
| **B** | $z_t \to K_{z_t} \to u_t^*$ | 진짜 미분→응집 문제 열림 | canonical primitive 확장 필요; 근본부 수정 |

사용자 직감: **B 가 더 정직.** 단 canonical 즉시 수정 금지 — *working-layer 에서 먼저*.

---

## 7. 작업 이름 후보

| 후보 | 평가 |
|---|---|
| `D0_to_D1_Cohesion_Genesis` | 명확 |
| `PreCohesive_Differentiation_to_Cohesion_Field` | 길지만 정확 |
| `Feature_Grounded_Cohesion_Order_Parameter` | 한 측면 강조 |
| **`D0D1_Cohesion_Genesis`** | **채택 후보** |

---

## 8. 내일의 첫 목표

**증명 시도 금지. 먼저 명확히 할 것:**

1. $z_t$ 의 정의
2. $K_{z_t}$ 의 정의
3. $K_{z_t}$ 가 기존 SCC 연산자에 *들어가는 방식*
4. $u_t^* = \arg\min \mathcal{E}(u; z_t)$ 의 *존재 정리*
5. **이게 saliency/PCA/segmentation proxy 가 아닌 이유** ← 핵심
6. 단일장 $u_t$ 가정이 어떻게 *보존* 되는지
7. 기존 canonical 과 *충돌하는 지점*

**가장 작은 첫 정리:**

$$\boxed{\text{T-D0D1-Existence: 유한 } X_t \text{ 에서 } z_t\text{-conditioned SCC energy 는 } \Sigma_m \text{ 위의 minimizer } u_t^* \text{ 를 가진다.}}$$

증명은 compactness + continuity 로 가능할 것.

**하지만 진짜 어려운 것은 *존재가 아니라*:**

$$\boxed{\text{T-D0D1-Nonuniformity: } z_t \text{ 의 차이가 비균일 } u_t^* \text{ 를 유도하는 조건}}$$

---

## 9. 한 줄 요약

> $u_t$ 단일장은 *버릴 필요 없다*. 다만 $u_t$ 는 *raw primitive 가 아니라* $z_t$ 라는 *전-응집 미분장 위에서 안정화되는 scalar order parameter* 로 재해석해야 한다.

**전체 화살표:**

$$\boxed{D_0 = z_t \to K_{z_t} \to \mathcal{E}(u; z_t) \to u_t^* \to S_0(u_t^*) \to I(S_0(u_t^*))}$$

---

## 본 메모의 위치

- **assistant 의 P1-P4 framework 와 무관.** 사용자 직접 사고.
- **새 어휘 도입 *유의*:** $z_t$, $K_{z_t}$, $\mathcal{F}$, $D_0 D_1$ — 정의가 *수학적으로 구체* 이므로 vocabulary refactoring 와 다름 (단, *§8 작업 5번* 이 그 차이를 *증명* 해야 함).
- **검증 책무:** 본 메모의 §3 커널 형태 $K_{z_t}(x,y) = \exp(-d_X^2/2\rho^2)\exp(-d_\mathcal{F}^2/2\sigma^2)$ 는 *Gaussian similarity kernel* — diffusion maps, spectral clustering, mean-shift 와 형태적으로 동일. **§8-5 ("proxy 아닌 이유") 의 응답이 본 메모의 *진정성* 의 검증 게이트.**
- **결정 위치:** 본 메모는 *결정 B (z_t 도입)* 의 사용자 측 제안. 00_plan 의 6 stage 검토를 *통과하면* 진행. 통과 못하면 메모 자체가 *셋째 archive 후보*.

---

*5/14 저녁 사용자 메모 보존. 검토는 5/15.*
