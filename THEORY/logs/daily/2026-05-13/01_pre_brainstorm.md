---
type: log/brainstorm
date: 2026-05-13
session: CV-1.15 promotion 전 rough notes
---

> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]


# Pre-Brainstorm — 2026-05-13

Promotion application 직전 탐색적 메모. 증명되지 않은 것은 쓰지 않는다.

---

## Core intuition

> "SCC temporal identity is low-action historical succession, not endpoint similarity."

단일 formation이 시간 $t$에서 $r$로 계승되는 것은, 중간 경로 위에 action이 작은 역사가 존재한다는 것이다. Endpoint가 가깝다는 것이 아니다. 이것이 CV-1.15의 핵심 이동이다.

이것은 기존 T-Temporal-Identity (CV-1.13, Cat A)를 invalidate하지 않는다. 두 개의 보완적 관점이다:
- T-Temporal-Identity: score matrix $S^0_{ij}$ 기반, composition-compatible 부분 구조 확인.
- CV-1.15: action cost 기반, composition을 위한 canonical cost structure 제안.

---

## Q1. 승인 후 CV-1.15를 canonical에 넣을 때 action cost를 refinement로 표현하는 최선의 문장은?

**현재 draft (10_patch_plan.md §1)**:
> "이것은 기존 temporal identity cost의 **대체가 아니라 composition-compatible refinement**이다. T-Temporal-Identity (§8.5)는 독립적으로 유효하다."

**더 나은 후보**:
> "CV-1.15의 action cost는 temporal composition 분석을 위한 layer를 추가한다. 기존 T-Temporal-Identity (§8.5)는 score matrix $S^0_{ij}$ 기반이며 이 layer와 독립적으로 유효하다. Action cost는 composition-compatible한 alternative formulation을 제공하여, 두 layer가 상호 보완적으로 작동한다."

**판단**: 현재 draft로 충분하다. "대체가 아니라 refinement" + "T-Temporal-Identity 독립 유효" 두 문장이면 canonical 독자 혼란 방지에 충분. 과도한 설명은 canonical 분량을 늘린다.

---

## Q2. raw Gibbs kernel K_{i→k}, admissible temporal kernel M_{t→s}, Sinkhorn plan Π_{t→s}를 어떻게 명확히 구분할 것인가?

**세 개체의 차이**:

| 기호 | 수식 | 특징 | 사용처 |
|---|---|---|---|
| $\mathbf{K}_{i\to k}$ | $\exp(-a_i/\varepsilon)$ 행렬 곱 | raw, unnormalized | CV-1.15 T-ACT-GIBBS |
| $M_{t\to s}$ | E1–E4-admissible 수송 계획 | marginal constraints 있음 | canonical §8.5 일반 |
| $M^\mathrm{sink}_{t\to s}$ | $\mathrm{Sinkhorn}(u_t,u_s,c)$ | doubly-stochastic (scaled) | OP-0012-SINK |

**구분 전략**:
- canonical §13.Y 서두에 1문장 주석: "이 섹션에서 $\mathbf{K}_{i\to k}$ (볼드체)는 Gibbs kernel; $K$ (이탤릭 스칼라)는 formation 수."
- $\Pi_{t\to s}$는 Sinkhorn plan의 alternative 기호로 향후 도입 고려. 이번 CV에서는 $M^\mathrm{sink}$로 유지.

**위험**: 기호 변경이 많아질수록 canonical 독자 부담 증가. 최소한의 주석으로 해결.

---

## Q3. exp89 결과는 논문/보고서에서 어느 정도 강도로 주장할 수 있는가?

**허용 표현**:
- "numerically confirms the hierarchy"
- "sanity check consistent with T-ACT-DP and T-ACT-GIBBS"
- "computational validation"
- "numerical evidence for the composition residual hierarchy"

**금지 표현**:
- "exp89 proves T-ACT-DP" (exp89는 proof가 아님)
- "experiments confirm Cat A status" (Cat A는 수학 증명 기반)
- "numerical verification completes the proof"

**강도 판단**: exp89 결과는 1–2문장 각주 수준으로 canonical에 포함 가능. 메인 클레임의 근거는 항상 01–04 파일의 수학 증명이다.

---

## Q4. OP-0012-SINK를 "Sinkhorn Temporal Scaling Compatibility Problem"으로 재명명할 것인가?

**현재 이름**: OP-0012-SINK (Sinkhorn plan composition)

**제안 이름**: "Sinkhorn Temporal Scaling Compatibility Problem"

**장점**: 문제의 핵심 ($b_1 \odot a_2 \neq c \cdot \mathbf{1}$, scaling vector 비호환성)을 이름이 직접 담음.

**단점**: 기존 문서 전체에서 "OP-0012-SINK" 검색 결과가 많음 → 이름 변경 시 문서 일관성 비용 발생.

**결론**: 이번 CV에서는 "OP-0012-SINK" 유지. CV-1.16 혹은 다음 major revision 때 재명명 논의.

---

## Q5. Sinkhorn scaling gap은 marginal mismatch 문제인가, normalization gauge 문제인가, OT geometry 문제인가?

**세 관점 분석**:

**A. Marginal mismatch**:
$M_1 M_2$의 marginal은 $u_t$, $u_r$ (OK)이지만 내부 marginal $\sum_x M_1(x,y) = u_s(y)$와 $\sum_z M_2(y,z) = u_s(y)$가 동시에 만족돼야 함. 그런데 $M_1 M_2$의 중간 marginal은 $\sum_x (M_1 M_2)(x,z) / \sum_z$ 형태로 보존되지 않을 수 있음 → marginal mismatch는 문제 현상이지 원인이 아님.

**B. Normalization gauge**:
$b_1 \odot a_2 \neq c \cdot \mathbf{1}$은 두 개의 독립 transport 문제에서 결정된 scaling vector가 서로 다른 normalization gauge를 가진다는 것. 각 Sinkhorn은 자기 자신의 marginal constraints를 만족하는 최소 entropically-regularized plan을 구하지만, 합성에서는 중간 계층 ($s$)의 scaling이 호환되지 않음.

**C. OT geometry**:
두 independent OT problems의 optimal plans를 합성할 때, 합성 plan이 $u_t$–$u_r$ OT optimal과 같아질 이유가 없음. OT geometry 관점에서 이것은 geodesic non-composability: $W_2$-geodesic이 일반적으로 중간점을 통해 합성 가능하지 않음.

**종합 판단**: 세 관점이 동일 현상의 다른 단면. 가장 수학적으로 정확한 표현은 B (normalization gauge) → $b_1 \odot a_2$ 비호환성. L-δ_eff-SINK는 A (marginal mismatch) 관점에서 bound를 구함. 실제 L-Eff-Sinkhorn은 B + C 관점 모두 필요.

---

## Q6. continuous-time action limit은 CV-1.16/OP-0022 후보인가?

**질문**: discrete-time action $\mathcal{A}_{i:k}(P) = \sum_\ell a_\ell(x_\ell, x_{\ell+1})$을 $\Delta t \to 0$ 극한으로 보내면 어떤 continuous-time functional이 나오는가?

**예상 답변**:
$a_\ell(x,y) = d(x,y)^2/\Delta t + \gamma \lVert \Delta\varphi \rVert^2/\Delta t$에서 $\Delta t \to 0$ 극한은 Lagrangian $L(x, \dot{x}, \varphi, \dot{\varphi}) = \vert \dot{x}\vert ^2 + \gamma\vert \dot{\varphi}\vert ^2$를 가진 action integral 형태. 이것은 Riemannian manifold 위의 geodesic energy와 유사한 구조.

**CV-1.16/OP-0022 후보**:
- Γ-수렴 분석: $\mathcal{A}^h \to \mathcal{A}$ as $h = \Delta t \to 0$.
- Viscosity solution PDE (HJB equation for hard-min cost).
- 연속 시간 Gibbs kernel 극한.

**결론**: CV-1.16 이후 별도 OP로 등록. 이번 CV에서는 "continuous-time limit은 OPEN" 명시로 충분.

---

## Q7. action cost는 K-jump 이전 stable-K temporal theory의 canonical cost가 될 수 있는가?

**현재 상황**: canonical §8.5 temporal cost는 Sinkhorn-based score matrix $S^0_{ij}$. CV-1.15 action cost는 composition-compatible alternative.

**가능한 경로**:
- stable-K temporal theory (K-jump 없는 경우): action cost가 composition property를 갖는다 (T-ACT-DP, T-ACT-GIBBS, Cat A). 이 범위에서 canonical cost 후보.
- K-jump 포함 경우: action cost를 K-jump 전후로 어떻게 정의할지 불명확. OP-0008 (σ-inherit) 범위.

**결론**: stable-K temporal theory (K_t=K_s=K_r=K)에 한정하여 action cost를 canonical cost 후보로 등록하는 것이 적절. K-jump 포함 확장은 CV-1.16+ 이후.

canonical §8.5 M_{t→s} 정의 변경 여부 결정은 T-ACT-KERNEL-COMP→REL의 (GK) 조건 채택 여부와 연결되므로, CV-1.16 때 함께 결정.

---

## Q8. path inheritance 관점에서 SCC temporal identity 선언문을 어떻게 정리할 것인가?

**현재 canonical 선언 (T-Temporal-Identity, §8.5)**:
> Formation $F_t$ is temporally identical to $F_s$ if the OT-induced relation $R_{t→s}[M_{t→s}]$ is a bijection on persistent components.

**CV-1.15 추가 관점 (P-ACTION-PATH-INHERITANCE)**:
> $F_t$ is temporally identical to $F_r$ if there exists a low-action historical path $P: x_t \to x_r$ with small $\mathcal{A}_{t:r}(P)$.

**두 관점의 관계**:
- T-Temporal-Identity: 현 시점 snapshot 비교 (OT-based matching).
- P-ACTION-PATH-INHERITANCE: 역사적 경로 기반 (dynamics-based).

T-Temporal-Identity는 snapshot이 일치하는지를 묻고, P-ACTION-PATH-INHERITANCE는 그 일치가 '어떤 종류의 역사'에 의해 지지되는지를 묻는다.

**canonical 선언문 제안**:
> "SCC temporal identity는 두 층위에서 작동한다: (1) snapshot layer — OT-induced persistent component bijection (T-Temporal-Identity); (2) historical layer — low-action path existence (P-ACTION-PATH-INHERITANCE, CV-1.15). 두 층위는 독립적으로 정의되며 stable-K 조건 하에서 상호 보완적으로 해석된다."

이것은 오늘 canonical 삽입 블록의 배경 섹션에 포함할 수 있다.

---

## 오늘의 리스크

| 리스크 | 확률 | 완화 방법 |
|---|---|---|
| K symbol 주석이 canonical에서 누락 | 낮음 | 10_patch_plan.md §1 첫 줄에 이미 포함 |
| "refinement" 표현 모호 | 낮음 | Q1 최선 문장 사용 |
| OP-0012-SINK OPEN 상태 canonical에서 모호 | 낮음 | Warning block + OP 등록으로 명시 |
| post-promotion audit에서 표현 충돌 발견 | 중간 | Block D grep 체크리스트 실행 |
| exp89를 proof로 표현하는 실수 | 낮음 | 모든 언급에 "numerical validation" 명시 |

---

*작성: 2026-05-13. CV-1.15 promotion application 직전 brainstorm.*
