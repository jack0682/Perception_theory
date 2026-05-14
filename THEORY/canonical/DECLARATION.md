---
id: DECL-1.0
type: canonical/declaration
created: 2026-05-07
status: authoritative
description: SCC 이론 중심축 선언문. canonical.md의 모든 수학보다 먼저 읽어야 할 문서. 이론이 무엇을 위해 존재하는가를 기술한다.
---

> [!nav] Theory Navigation
> Parent: [[THEORY_INDEX]] · [[MOC_canonical_authority]]
> Pairs with: [[00_manifest]] (SCC-CT v0.1 구조적 권위)
> Next: [[canonical]] §2 Foundational Orientation → [[hypothesis_tree]] → [[theorem_status]]
> Q-MOCs: [[MOC_Q1_boundary_T8]] · [[MOC_Q2_multi_formation]] · [[MOC_Q3_stochastic_dynamics]] · [[MOC_Q4_K_selection]] · [[MOC_Q5_temporal_identity]] · [[MOC_Q6_sigma_inherit]]
> Status: Canonical (DECL-1.0)

# Soft Cognitive Cohesion — 이론 선언문

---

## 출발 질문

이 이론은 '사물이 존재한다'에서 시작하지 않는다.

이 이론의 출발 질문은 하나다:

> **어떤 차이의 덩어리가 언제부터 하나의 객체가 되는가?**

---

## 태초의 장면

태초에 이름은 없었다. 클래스도 없었다.

있는 것은:

```
색의 차이  밝기의 차이  경계의 흔적  깊이의 변화  형태의 응집
```

그리고 인식이 시작된다. 인식은 클래스를 받아들이는 것이 아니다 — 이 차이들이 하나의 단위로 응집되는 과정 자체가 인식이다. 객체는 이 과정의 출력이지 입력이 아니다. 클래스명은 객체 형성이 완료된 이후에 온다 — 이 이론의 범위 밖이다.

더 정확한 순서:

```
감각장면
  → 차이의 발생
  → 경계 후보
  → 형태 응집
  → 깊이 일관성
  → 하나의 단위로 묶임    ← 이 이론이 다루는 구간
  → 객체 후보
  → 이름 / 클래스 부여    ← 이 이론의 범위 밖
```

---

## Primitive

$$u_t : X_t \to [0,1]$$

이름 없는 연속 장. 값은 **응집 참여 강도**다 — 어느 위치가 얼마나 강하게 응집 구조에 참여하는가.

클래스 소속 확률이 아니다. 레이블이 아니다. 사전에 정의된 객체에 대한 신뢰도도 아니다.

$u_t$는 객체를 기술하는 도구가 아니다. **객체화 이전의 상태 자체다.** 객체는 $u_t$의 에너지 최솟값 구조에서 사후적으로 출현하는 해석이다.

---

## 중심 정리 — T8 (위상전이)

$$\frac{\beta}{\alpha} > \frac{4\lambda_2}{|W''(c)|}$$

이 임계조건이 **성립할 때**:
장은 비균일 최솟값을 가진다. 경계가 출현한다. 객체성이 발생한다.

이 임계조건이 **붕괴할 때**:
장은 균일하게 퍼진다. 경계가 사라진다. 덩어리가 하나로 융합된다.

**$\lambda_2$는 그래프의 해상도다.** 거리가 멀수록, 시야가 흐릴수록, 해상도가 낮을수록 $\lambda_2$가 작아진다. 임계조건이 붕괴한다. 두 객체가 하나로 보인다.

멀리 있는 두 사과가 하나로 보이는 것은 오류가 아니다. 그 해상도에서 임계조건이 붕괴한 결과 — **그 조건에서의 유효한 인식이다.**

이것이 이 이론의 심장이다.

---

## 여섯 가지 질문

이론은 다음 여섯 가지 질문에 수학적으로 답한다:

| 질문 | 수학적 구조 | 현재 상태 |
|---|---|---|
| **Q1. 경계는 언제 출현하는가?** | T8 위상전이, 에너지 최솟값 구조 | 대부분 Cat A |
| **Q2. 여럿이 공존할 수 있는가?** | Multi-formation, Count bridge | Cat A (조건부) |
| **Q3. 어떻게 변하는가?** | Stochastic dynamics, Gibbs measure | Package I Cat A |
| **Q4. 몇으로 안정화되는가?** | K-selection (EQ/OBS/DYN) | Cat B |
| **Q5. 시간이 지나도 같은 것인가?** | Temporal Identity, OT transport | Cat B |
| **Q6. 분열·합병 후에도 이어지는가?** | σ-Inheritance | 진행 중 |

---

## 관측 조건 의존성

객체의 수, 경계, 동일성은 **관측 조건의 함수**다 — 절대량이 아니다.

$$N_{\text{objects}} = f(\lambda_2,\, \beta/\alpha,\, m,\, \text{distance},\, \text{resolution})$$

두 관측자가 같은 장면을 보고 다르게 인식할 수 있다. 둘 다 맞다. 서로 다른 관측 조건 하에서의 서로 다른 에너지 최솟값이다. 같은 클래스명("컵")을 말한다고 해서 같은 $u_t$ 구조를 공유한다는 뜻이 아니다.

이론은 상대주의가 아니다. **구조화된 조건부성**이다:
- 인식은 관측 조건에 의존한다
- 그러나 아무렇게나 구성되지 않는다
- 에너지 최솟값의 위상 구조가 가능한 인식을 제약한다

---

## 에너지 구조

$$E = \lambda_{\text{cl}} E_{\text{cl}} + \lambda_{\text{sep}} E_{\text{sep}} + \lambda_{\text{bd}} E_{\text{bd}} + \lambda_{\text{tr}} E_{\text{tr}}$$

네 에너지 항은 **개념적으로 독립**이다 (수학적 독립이 아님 — 병합 금지):

| 에너지 | 의미 | 대응하는 인식 현상 |
|---|---|---|
| $E_{\text{cl}}$ (closure) | 형태의 자기 지지 | 경계가 닫힌 덩어리 |
| $E_{\text{sep}}$ (separation) | 외부와의 대조 | 배경과의 분리 |
| $E_{\text{bd}}$ (boundary) | 전이 구간의 매끄러움 | 흐린 경계, 선명한 경계 |
| $E_{\text{tr}}$ (transport) | 시간적 연속성 비용 | 시간이 지나도 같은 것 |

---

## 이 이론이 아닌 것

- **객체 검출 이론이 아니다.** 클래스명 부여는 이 이론의 범위 밖이다.
- **퍼지 세그멘테이션이 아니다.** 공학적 근사가 아닌 이론적 기반이다.
- **클러스터링이 아니다.** 레이블 없이 위상 구조를 다룬다.
- **인식의 주관성 주장이 아니다.** 조건부이지 임의적이지 않다.
- **객체 추적이 아니다.** 시간동일성은 추적 알고리즘이 아닌 수학적 성질이다.
- **공학적 비전 파이프라인이 아니다.** 그 파이프라인의 수학적 정당성을 제공한다.

---

## 이 선언문의 위치

```
DECLARATION.md          ← 지금 이 문서 (중심축, 먼저 읽기)
canonical.md            ← 수학적 정식화 (§2 Foundational Orientation → §13 정리 카탈로그)
theorem_status.md       ← 정리 상태 레지스트리
hypothesis_tree.md      ← 가설 의존성 구조 (HT-3.0)
```

**세션 시작 시 읽기 순서:** DECLARATION.md → canonical.md §2 → hypothesis_tree.md → theorem_status.md → CHANGELOG.md

---

*DECL-1.0, 2026-05-07. 이 선언문은 이론의 방향이 바뀌지 않는 한 수정되지 않는다. 수정 시 CHANGELOG.md에 기록하고 버전을 DECL-2.0으로 올린다.*
