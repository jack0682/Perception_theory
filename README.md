# Relational Field Formation

이 저장소는 **객체를 먼저 가정하지 않고**, 관계 그래프 위의 부드러운 장(field)이 어떻게 안정적인 형성으로 굳어져 객체처럼 보이게 되는지를 연구한다.

한 문장으로 말하면:

> 객체가 먼저 있는 것이 아니라, 관계와 응집장이 먼저 있고 객체는 안정화 이후의 해석이다.

---

## 1. 출발점

시간 $t$의 관계 그래프를 $G_t=(X_t,N_t)$라고 하자. 여기서 $X_t$는 이미 주어진 객체들의 집합이 아니라, 관계가 놓이는 자리들의 집합이다.

원시 상태는 다음과 같은 응집장이다.

$$
u_t:X_t\to[0,1].
$$

$u_t(x)$는 “$x$가 어떤 객체에 속한다”는 뜻이 아니다. $x$가 현재 형성 중인 응집 구조에 얼마나 참여하는지를 나타낸다.

기본 상태공간은 총 응집량이 고정된 장들의 공간이다.

$$
\Sigma_m(G_t)=\{u:X_t\to[0,1]\mid \sum_x u(x)=m\}.
$$

이 공간에서 장은 퍼지고, 모이고, 갈라지고, 안정화된다. 객체는 그 결과를 읽는 방식이다.

---

## 2. 이론의 흐름

### 단일 장

처음에는 하나의 그래프 위에 하나의 장만 놓는다. 이 단계의 질문은 다음이다.

> 객체 이름표 없이도 객체처럼 보이는 형성을 설명할 수 있는가?

이 단계에서 정리된 내용은 다음이다.

- 장은 총량 제약 아래 안정 상태를 가진다.
- closure는 장이 자기 자신을 지지하는 과정을 나타낸다.
- distinction은 주변과의 구분을 나타낸다.
- boundary는 선이 아니라 transition band다.
- gradient flow는 장을 안정 상태로 보낸다.
- persistent homology는 장의 형태와 component 구조를 읽는다.

중요한 발견은 하나의 장이 꼭 하나의 단순한 덩어리로 끝나지 않는다는 점이다. 전체 형성 조건을 넣으면, 객체 이름표가 생기기 전에도 여러 봉우리와 내부 구조를 가진 형성이 나타날 수 있다.

### 여러 장

다음 단계에서는 여러 형성 채널이 같은 그래프 위에서 상호작용한다.

이때 “몇 개가 있는가?”라는 질문은 하나가 아니다.

| 읽는 방식 | 뜻 | 수학적 표현 |
|---|---|---|
| 모델 해상도 | 허용된 labelled field slot 수 | $K_{\mathrm{field}}$ |
| 활성 채널 수 | 실제로 충분한 질량을 가진 slot 수 | $K_{\mathrm{act}}$ |
| 위상적 성분 수 | 합산장에 나타나는 dominant connected components | $K_{\mathrm{bar}}$ |
| 부드러운 형태 수 | persistence bar를 가중합한 연속적 count | $K_{\mathrm{soft}}$ |

핵심은 이 네 가지를 섞지 않는 것이다. 모델이 열어 둔 slot 수와, 실제 활성 slot 수와, 합산장의 위상적 성분 수는 서로 다를 수 있다.

### count bridge

세 개의 조명이 모두 켜져 있어도, 멀리서 보면 빛이 하나의 밝은 영역으로 합쳐질 수 있다. 이와 비슷하게 labelled channel은 셋이지만 합산장은 하나의 dominant component처럼 보일 수 있다.

따라서 먼저 필요한 정리는 다음이다.

> 충분히 분리된 상황에서는 활성 채널 수와 합산장의 dominant topological component 수가 일치하는가?

현재 canonical 결과는 이 질문에 조건부로 답한다.

$$
K_{\mathrm{bar}}^{\ell_{\min}}(U;G)
=
K_{\mathrm{act}}^\varepsilon(\mathbf u),
\qquad
U=\sum_j u^{(j)}.
$$

이 등식은 전역적으로 항상 참이라는 뜻이 아니다. 활성 영역이 분리되어 있고, 영역 사이 bridge가 낮으며, 작은 잔여 성분이 억제되는 resolved regime에서 참이다.

즉 이 정리는 “언제 ordinary counting이 작동하는가”를 정한다.

---

## 3. 사용되는 수학적 도구

| 도구 | 역할 |
|---|---|
| 유한 그래프 | 관계가 놓이는 기초 공간 |
| 제약 변분법 | 총량이 고정된 장의 안정 상태 분석 |
| fixed point theory | closure와 self-support 분석 |
| gradient flow | 안정화 과정 분석 |
| spectral graph theory | 불안정성, 분기, Hessian mode 분석 |
| persistent homology | 장의 connected component와 형태 count |
| representation theory | 그래프 대칭 아래 구조적 signature |
| layered state spaces | labelled slot 변화와 경계 처리 |

이 도구들은 각각 다른 혼동을 막는다. 변분법은 안정 상태를, 위상적 지속성은 형태를, spectral theory는 분기와 불안정성을, layered state spaces는 모델 label과 실제 morphology의 차이를 다룬다.

---

## 4. 현재 상태

현재 formal status는 `THEORY/canonical/theorem_status.md`가 기준이다.

요약하면:

| 항목 | 상태 |
|---|---|
| 단일 장 기반 이론 | canonical |
| 객체 이전의 multi-peak 형성 | proved |
| 그래프 class 확장 | proved |
| 여러 장의 static structural signature | canonical definitional layer |
| hard topological count와 active count의 bridge | proved under explicit conditions |
| soft count bridge | open |
| field capacity 선택 원리 | open |
| dynamic count-jump inheritance | open |

---

## 5. 주장하지 않는 것

이 이론은 다음을 주장하지 않는다.

- 객체가 원시적이라는 주장
- 모델 slot 수가 실제 객체 수라는 주장
- 모든 상황에서 active count와 topological count가 같다는 주장
- 모든 smooth count가 안정적이라는 주장
- field capacity 선택 문제가 해결되었다는 주장
- dynamic merge/split 이후의 구조 상속이 해결되었다는 주장

이 구분이 이론의 핵심이다. 같은 현상을 여러 방식으로 셀 수 있고, 그 count들은 조건에 따라 일치하거나 갈라진다.

---

## 6. 저장소 구조

```text
CODE/
  scc/           Python package
  tests/         pytest tests
  experiments/   research experiments
  scripts/       diagnostics and result generation

THEORY/
  canonical/     settled definitions, theorem registry, open problems
  working/       active notes and explanatory documents
  logs/          research history
```

주요 문서:

- `THEORY/canonical/theorem_status.md` — 현재 정리 상태
- `THEORY/canonical/canonical.md` — 승급된 이론 본문
- `THEORY/canonical/open_problems.md` — 열린 문제
- `THEORY/working/MF/scc_multiformation_origin_to_current_korean_explanation_2026-05-03.md` — 긴 한국어 해설

---

## 7. 실행

```bash
cd CODE
python3 -m pytest tests/ -v
```

간단한 smoke check:

```bash
cd CODE
python3 -c "from scc import *; g=GraphState.grid_2d(10,10); p=ParameterRegistry(); r=find_formation(g,p); print(r.diagnostics)"
```

---

## 8. 다음 방향

다음 핵심 과제는 hard count에서 soft count로 넘어가는 것이다.

현재 조건부 정리는 resolved regime에서 다음을 보장한다.

$$
K_{\mathrm{bar}}=K_{\mathrm{act}}.
$$

다음 단계는 어떤 가중 함수 $\phi$에 대해

$$
K_{\mathrm{soft}}^\phi\approx K_{\mathrm{bar}}
$$

가 안정적으로 성립하는지 밝히는 것이다. 모든 smooth weighting이 좋은 것은 아니므로, 안정적인 envelope class와 오차 bound가 필요하다.

