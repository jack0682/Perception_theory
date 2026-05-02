# SCC / Multi-Formation 이론 전체 해설  
## 무엇으로부터 시작했고, 어떤 과정을 거쳐, 지금 무엇이 증명되었는가

2026-05-03 기준 — CV-1.5.2 / T-L1-F 이후 상태 정리

> 문서 상태: working-grade 한국어 해설 문서.  
> 이 문서는 canonical theorem 파일이 아니며, `THEORY/canonical/`의 정리 지위를 변경하지 않는다.

---

## 0. 문서 목적

이 문서는 SCC / Multi-Formation 이론을 “현재 어떤 파일이 있는가”가 아니라, “이 이론이 무엇으로부터 시작했고, 어떤 실패와 정리 과정을 거쳐 지금 어디에 도달했는가”라는 관점에서 재구성한다.

따라서 이 문서는 다섯 층위를 구분한다.

1. 역사적 동기: 왜 이런 이론을 시작했는가.
2. 철학적 핵심: 왜 객체가 아니라 field가 먼저인가.
3. 수학적 구조: 어떤 공간, 함수, count, theorem package가 도입되었는가.
4. 실험과 실패: 어떤 실험이 어떤 기대를 실패시켰고, 그 실패가 어떤 새 정의를 낳았는가.
5. 현재 증명 상태: 무엇이 canonical theorem이고, 무엇이 working candidate이며, 무엇이 empirical evidence이고, 무엇이 아직 open problem인가.

특히 이 문서는 다음 질문에 답하기 위해 작성되었다.

> SCC / Multi-Formation 이론은 무엇이고, 어디서 시작했으며, 어떤 실패와 정리를 거쳐 지금 무엇을 증명한 상태인가?

이 문서는 저자의 향후 연구를 위한 장문 설명서다. canonical claim을 새로 추가하지 않으며, `CV-1.5.2`와 `T-L1-F` 이후 상태를 해석하고 연결하는 역할만 한다.

---

## 1. 이 이론은 한마디로 무엇인가

SCC는 객체를 먼저 가정하지 않는 형성 이론이다. 출발점은 “이미 객체들이 있고, field는 그 객체들을 묘사한다”가 아니다. 출발점은 관계 그래프 위에 놓인 soft cohesion field다. 이 field가 closure, distinction, boundary, morphology, persistence 같은 조건을 만족하며 안정화될 때, 우리는 사후적으로 그것을 object-like formation이라고 부른다.

가장 기본적인 형식은 다음과 같다.

$$
u:X_t\to[0,1].
$$

여기서 $X_t$는 이미 individuated object들의 집합이 아니라 relational loci의 substrate다. $u_t$는 class label, probability mask, object indicator가 아니다. $u_t$ 자체가 primitive SCC field다.

Multi-Formation은 이 생각을 여러 formation이 동시에 상호작용하는 상황으로 확장한다. 그러나 Multi-Formation의 핵심 질문은 단순히 “객체가 여러 개일 때 어떻게 하는가”가 아니다. 진짜 질문은 다음이다.

> 여러 formation이 있을 때, “몇 개가 있다”는 말은 무엇을 세는가?

이 질문이 네 개의 count 언어를 낳았다.

$$
K_{\mathrm{field}},\quad
K_{\mathrm{act}},\quad
K_{\mathrm{bar}},\quad
K_{\mathrm{soft}}.
$$

이 네 기호는 같은 $K$의 네 표기법이 아니다. 서로 다른 층위의 count다.

- $K_{\mathrm{field}}$: 모델링 chart가 허용하는 labelled field slot의 수.
- $K_{\mathrm{act}}^\varepsilon$: mass threshold를 넘는 active labelled slot의 수.
- $K_{\mathrm{bar}}^{\ell_{\min}}$: aggregate field $U=\sum_j u^{(j)}$의 dominant $H_0$ persistence bar 수.
- $K_{\mathrm{soft}}^\phi$: persistence bar lengths에 envelope $\phi$를 적용해 얻는 smooth count.

따라서 SCC / Multi-Formation은 한 문장으로 다음처럼 요약할 수 있다.

> 관계 그래프 위의 soft cohesion field가 object-like formation을 낳는다는 field-first 이론이며, Multi-Formation은 여러 formation 상황에서 labelled slot count, active count, topological count, soft count가 언제 일치하고 언제 갈라지는지를 연구하는 확장이다.

---

## 2. 최초의 문제의식: “객체가 먼저인가, 형성이 먼저인가?”

초기의 문제의식은 철학적이면서 동시에 수학적이었다.

표준적인 관점에서는 객체가 먼저 있다. 예컨대 “세 개의 물체가 있고, field는 각 물체의 위치나 속성을 나타낸다”고 생각한다. 이 관점에서는 segmentation, classification, tracking 모두 이미 어떤 objecthood를 암묵적으로 전제한다.

SCC의 관점은 반대다.

객체는 처음부터 주어지지 않는다. 먼저 있는 것은 관계, 접촉, 응집, 구분, 경계, 지속성의 field다. 이 field가 안정적인 응집 구조를 만들 때, 그 안정화된 응집을 object라고 해석할 수 있다. 즉 object는 primitive가 아니라 derivative다.

canonical SCC에서 $u_t$가 primitive로 선언되는 이유가 여기에 있다.

$$
u_t:X_t\to[0,1]
$$

는 이미 객체를 가리키는 mask가 아니다. $u_t(x)$는 “점 $x$가 어떤 이미 주어진 object에 속할 확률”이 아니라, $x$가 현재 형성 중인 cohesion에 어느 정도 참여하는지를 나타내는 graded field다.

이 철학적 이동은 수학적으로 매우 엄격한 부담을 만든다. 객체가 primitive가 아니라면, 정리 안에 object label을 몰래 들여오면 안 된다. “두 object가 merge한다”는 말을 쓰려면, 실제로는 어떤 field 구조, 어떤 topology, 어떤 persistence event, 어떤 labelled slot dynamics를 말하는지 분리해야 한다.

비유하자면, 고전적 object-first 관점은 바다 위에 이미 섬들이 있다고 보고 지도를 그리는 방식이다. SCC의 field-first 관점은 안개와 물결의 밀도 분포가 먼저 있고, 특정 조건 아래 안정된 island-like landmass가 드러난다고 보는 방식이다. 이때 지도 위의 섬 개수와 실제 지형의 응집 구조는 항상 같은 것이 아니다.

이 비유는 이후 $K$ 문제와도 직접 연결된다.

- 지도에 그린 이름표의 수가 $K_{\mathrm{field}}$일 수 있다.
- 실제로 표시가 살아 있는 이름표 수가 $K_{\mathrm{act}}$일 수 있다.
- 물 위에 드러난 큰 섬 덩어리 수가 $K_{\mathrm{bar}}$일 수 있다.
- 안개 속 밀도 분포를 부드럽게 세는 값이 $K_{\mathrm{soft}}$일 수 있다.

처음부터 객체를 놓지 않는다는 결정은, 나중에 “몇 개인가”라는 질문을 네 갈래로 분해하게 만든 가장 깊은 원인이다.

### 2.1 아주 처음의 실제 연구 상황: F-1 / M-1 / MO-1의 막힘

이 이론의 실제 연구사는 처음부터 깔끔한 $K_{\mathrm{field}}$, $K_{\mathrm{act}}$, $K_{\mathrm{bar}}$, $K_{\mathrm{soft}}$ 분리로 시작하지 않았다. 초기에는 오히려 세 개의 오래된 난점이 이론을 붙잡고 있었다.

| 초기 난점 | 대략적 질문 | 왜 어려웠는가 | 나중의 재해석 |
|---|---|---|---|
| F-1 | $K=2$ 같은 multi-formation이 공허한가 | single formation이 항상 더 자연스러워 보이는 상황이 있었음 | full SCC에서는 single-disk가 primitive attractor가 아님 |
| M-1 | $K=1$이 항상 선호되는가 | energy ordering만 보면 merge/single mode가 유리해 보임 | pure boundary-energy theorem과 full SCC formation 문제를 분리해야 함 |
| MO-1 | Morse theory가 corner 때문에 무효인가 | $\Sigma_M^K$ 같은 labelled multi-field 공간에는 corner와 stratification이 생김 | single-field $\Sigma_m$ 위에서는 smooth theorem domain을 회복할 수 있음 |

이 세 문제는 처음에는 서로 다른 문제처럼 보였다. 하나는 $K=2$의 vacuity 문제, 하나는 $K=1$ preference 문제, 하나는 Morse-theoretic invalidity 문제처럼 보였다.

그러나 2026-04-19 전후의 재분석에서 더 깊은 공통 원인이 드러났다. 그것이 N-1, 즉 Soft-Hard Switching Asymmetry였다.

핵심은 다음이었다.

> 이론은 soft field를 원시로 두면서, 중요한 순간마다 hard integer $K$, hard threshold, hard axiom switch를 몰래 사용하고 있었다.

이것이 “처음부터 객체를 놓지 않는다”는 철학적 명제가 수학적 문제로 바뀐 지점이다. object-first를 거부하려면, integer count도 처음부터 primitive로 두면 안 된다. 그렇다면 formation count는 어떻게 나오는가?

### 2.2 single-field로 되돌아간 이유

이 난점들 때문에 연구는 한 번 Multi-Formation을 곧바로 밀고 가는 대신, single-field domain으로 되돌아갔다. 이 후퇴는 보수적인 후퇴가 아니라 이론의 기초를 다시 세우기 위한 전략적 이동이었다.

질문은 다음처럼 바뀌었다.

> $K$개의 formation을 먼저 놓지 말고, 하나의 soft field 안에서 formation count나 multi-peak 구조가 어떻게 나타나는지 보자.

그래서 핵심 domain은 다시 다음 공간이 되었다.

$$
\Sigma_m(G)=\{u:X\to[0,1]\mid \sum_x u(x)=m\}.
$$

이 공간은 labelled $K$가 없다. 오직 하나의 field $u$만 있다. 따라서 이 공간에서 multi-peak, multi-mode, persistence count가 나온다면, 그것은 external object labels에서 온 것이 아니라 field 자체에서 나온 것이다.

이 시기에 중요한 정의가 $K_{\mathrm{soft}}$였다.

$$
K_{\mathrm{soft}}(u)=\sum_i \phi(\ell_i(u)).
$$

여기서 $\ell_i(u)$는 $u$의 superlevel $H_0$ persistence bar length다. 초기의 생각은 다음과 같았다.

> integer $K$를 primitive로 두지 말고, field가 만들어내는 persistence bars를 통해 formation count를 soft하게 읽자.

이것은 나중에 WQ-LAT-1.B에서 수정된다. arbitrary $\phi$가 안전하지 않다는 사실이 드러나기 때문이다. 그러나 역사적으로 $K_{\mathrm{soft}}$는 매우 중요한 역할을 했다. 그것은 integer $K$를 field-derived statistic으로 바꾸려는 첫 번째 본격 시도였다.

### 2.3 single-formation 단계의 핵심 발견: 하나의 field가 이미 multi-peak일 수 있다

single-field로 돌아간 뒤 가장 중요한 발견은 다음이다.

> full SCC에서는 단순한 $F=1$ single-disk 형태가 primitive ground truth가 아닐 수 있다.

초기의 object-like 상상에서는 하나의 formation이라면 하나의 둥근 덩어리, 하나의 disk, 하나의 connected blob이 가장 자연스러워 보인다. 그러나 full SCC functional은 단순한 boundary energy만 보지 않는다. closure, separation, distinction, entropy, morphology, persistence 같은 여러 요구가 함께 작동한다.

그 결과 하나의 field 안에서도 multi-peak formation이 안정적으로 나타날 수 있다. 이것이 pre-objective mechanism의 핵심이다.

T-PreObj-1의 철학적 의미는 바로 여기에 있다.

> object 이전의 field가 이미 내부 구조를 갖는다. 따라서 object는 원시 단위가 아니라 field가 만들어낸 안정 패턴의 해석이다.

이 발견은 F-1 / M-1 / MO-1을 다시 해석하게 만들었다.

- F-1은 “$K=2$가 공허한가?”라는 문제가 아니라, full SCC에서 single-disk가 왜 primitive answer가 아닌가의 문제로 바뀌었다.
- M-1은 “$K=1$이 항상 옳은가?”가 아니라, pure boundary-energy theorem과 full SCC formation theorem을 구분해야 하는 문제로 바뀌었다.
- MO-1은 labelled multi-field corner 문제를 single-field theorem domain과 분리하는 문제로 바뀌었다.

### 2.4 single-formation 발전의 정리 사다리

초기 single-formation 발전은 다음 사다리로 이해할 수 있다.

| 단계 | 핵심 질문 | 결과 / 정리 성격 | 이후에 남긴 것 |
|---|---|---|---|
| 재분석 | F-1/M-1/MO-1이 정말 독립 난점인가 | N-1 Soft-Hard Switching Asymmetry로 공통 원인 발견 | hard $K$를 primitive로 두면 안 됨 |
| single-field 복귀 | labelled $K$ 없이 formation count를 읽을 수 있는가 | $\Sigma_m(G)$ 위의 field-derived morphology 재정렬 | theorem-grade domain 확보 |
| $K_{\mathrm{soft}}$ 도입 | integer count를 soft persistence statistic으로 바꿀 수 있는가 | $H_0$ bar length weighted sum으로 soft count 정의 | 나중의 $\Phi_{\mathrm{res}}$ 문제의 전신 |
| $\mathcal F_{C+E}$ / thermal reading | field formation을 energy만이 아니라 entropy/count와 함께 볼 수 있는가 | free-energy style functional과 metastability reading | formation count를 distribution / regime으로 읽는 길 |
| T-PreObj-1 | full SCC에서 single disk가 primitive인가 | $F=1$ single-disk non-criticality와 multi-peak attractor | pre-objective formation이 slogan이 아니라 theorem-grade mechanism이 됨 |
| T-PreObj-1G | graph class에 의존하는가 | finite connected graph class로 일반화되는 방향 확보 | SCC가 특정 grid artifact가 아님을 강화 |
| $\sigma$-framework | formation의 구조를 count보다 풍부하게 기록할 수 있는가 | irrep / nodal / Goldstone / orbital signatures | Multi-Formation $\sigma$로 넘어갈 언어 제공 |

이 사다리의 핵심은 다음이다.

> Single-Formation은 “하나의 객체 이론”이 아니라, object 이전의 field가 어떻게 내부 구조와 count-like morphology를 만들어내는지 보인 단계였다.

### 2.5 T-PreObj-1이 왜 Multi-Formation의 전제인가

T-PreObj-1은 Multi-Formation과 직접 같은 정리는 아니다. 그러나 역사적으로는 Multi-Formation을 가능하게 한 전제다.

왜냐하면 Multi-Formation을 바로 시작하면 labelled slot을 object처럼 읽는 위험이 생긴다. 반면 single-field 단계에서 이미 다음을 확인하면 상황이 달라진다.

1. 하나의 field 안에서도 multi-peak structure가 생긴다.
2. formation count는 external $K$가 아니라 field morphology에서 읽을 수 있다.
3. object-like unit은 나중에 나온다.
4. count와 signature는 field-derived diagnostic이어야 한다.

이 네 가지가 확보된 뒤에야 Multi-Formation으로 돌아갈 수 있었다. 즉 Multi-Formation은 object labels를 추가하는 작업이 아니라, single-field에서 발견된 formation structure를 여러 interacting fields와 shared pool 위로 조심스럽게 lift하는 작업이 되었다.

이것이 이후 $K$-confusion을 처리하는 기준이 된다. 만약 Multi-Formation이 single-field pre-objective discovery 없이 시작되었다면, $K_{\mathrm{field}}$는 쉽게 primitive object count로 오해되었을 것이다. 그러나 single-field 단계가 먼저 있었기 때문에, $K_{\mathrm{field}}$는 chart cap이고, $K_{\mathrm{act}}$는 diagnostic이며, $K_{\mathrm{bar}}$는 aggregate topology라는 분리가 가능해졌다.

### 2.6 쉬운 비유: 국물, 기름방울, 그리고 그릇

Single-Formation의 발견을 가장 쉽게 비유하면, 물 위에 뜬 기름방울을 떠올릴 수 있다.

처음에는 이렇게 생각하기 쉽다.

> 기름방울 하나가 object 하나다.  
> 기름방울이 두 개면 object 두 개다.

하지만 SCC가 보는 것은 기름방울의 이름표가 아니다. SCC가 보는 것은 물 표면 전체에 퍼진 농도 field다. 어떤 곳은 기름 농도가 높고, 어떤 곳은 낮다. 높은 부분들이 서로 연결되어 있으면 하나의 덩어리처럼 보이고, 떨어져 있으면 여러 덩어리처럼 보인다.

여기서 중요한 점은 다음이다.

- 기름방울이라는 object가 먼저 있는 것이 아니다.
- 표면 전체의 농도 field가 먼저 있다.
- 우리가 “방울”이라고 부르는 것은 농도 field가 안정적으로 뭉친 뒤의 해석이다.

이 비유에서 $\Sigma_m(G)$는 “총 기름 양이 정해진 물 표면”이다. 총량 $m$은 고정되어 있고, 그 기름이 어디에 퍼지고 어디에 뭉치는지가 문제다.

T-PreObj-1의 발견은 다음과 비슷하다.

> 총 기름 양이 하나의 둥근 방울을 만드는 것이 가장 자연스러울 줄 알았는데, 실제 full SCC 조건을 넣어 보니 하나의 넓은 방울보다 여러 봉우리로 갈라진 안정 패턴이 더 자연스럽게 나타났다.

이것은 “방울이 여러 개니까 처음부터 object가 여러 개 있었다”는 뜻이 아니다. 오히려 반대다. 하나의 field가 object 이전 단계에서 이미 내부 구조를 만든다는 뜻이다.

### 2.7 쉬운 비유: 사진 속 사물 vs 열화상 지도

object-first 관점은 보통 사진과 비슷하다. 사진을 보면 컵, 책, 손, 테이블 같은 사물이 먼저 보인다. 그 다음에 각 사물의 색, 경계, 위치를 분석한다.

SCC의 관점은 열화상 지도에 더 가깝다. 처음에는 “컵”이나 “책”이라는 label이 없다. 대신 각 위치마다 열의 세기, 연결성, 주변과의 차이가 있다. 어떤 뜨거운 영역이 충분히 응집되고 주변과 구분되며 시간이 지나도 유지되면, 우리는 그것을 하나의 물체처럼 해석할 수 있다.

이 차이를 표로 쓰면 다음과 같다.

| 관점 | 먼저 있는 것 | object의 지위 | count의 의미 |
|---|---|---|---|
| 사진식 object-first | 컵, 책, 사람 같은 사물 | 원시 단위 | 사물 label을 세면 됨 |
| SCC field-first | 관계 그래프 위의 soft field | 안정화 뒤의 해석 | 어떤 count를 세는지 먼저 정해야 함 |

이 비유는 왜 SCC에서 count가 어려운지 잘 보여 준다. 사진에서는 “몇 개냐”가 비교적 쉽다. 컵 두 개, 책 세 권처럼 세면 된다. 그러나 열화상 지도에서는 “뜨거운 영역이 몇 개냐”가 scale, threshold, 연결성, 지속성에 따라 달라질 수 있다.

SCC의 $K$ 문제가 바로 이것이다.

---

## 2.8 Single-Formation 발전사를 더 자세히 풀어쓴 버전

이 절은 앞의 2.1-2.7을 더 느린 서사로 다시 설명한다.

### 2.8.1 첫 직관: 객체를 세고 싶지만, 객체를 먼저 놓고 싶지는 않다

처음 연구 동기는 “여러 formation이 생기는 현상을 설명하고 싶다”에 가까웠다. 그러나 바로 여기서 모순이 생긴다. 여러 formation을 설명하려면 “몇 개”인지 말해야 하는데, “몇 개”라고 말하는 순간 이미 object-like unit을 놓는 것처럼 보인다.

예를 들어 “두 개의 formation이 있다”고 말하면, 듣는 사람은 자연스럽게 두 개의 object가 이미 있다고 생각한다. 하지만 SCC는 바로 그 생각을 피하려고 시작한 이론이다.

따라서 초기의 진짜 문제는 다음이었다.

> object를 먼저 놓지 않고도, formation count를 말할 수 있는가?

이 질문이 F-1, M-1, MO-1, N-1, $K_{\mathrm{soft}}$, T-PreObj-1로 이어졌다.

### 2.8.2 F-1의 의미: “두 개”가 공허한가?

F-1은 대략 $K=2$ 같은 multi-formation 설정이 실제 의미를 갖는지 묻는 문제였다. 만약 energy나 stability를 계산할 때 항상 single formation이 더 유리하다면, $K=2$ 이론은 공허해질 수 있다.

쉬운 비유로는 비누막을 생각할 수 있다. 비누막 위에 두 개의 작은 거품이 있다고 하자. 표면장력만 보면 두 거품은 하나로 합쳐지는 것이 자연스럽다. 그러면 “두 거품 상태”는 오래 버티지 못한다.

초기 F-1은 이런 걱정과 닮아 있었다.

> SCC에서도 여러 formation은 결국 하나로 합쳐져 버리는가?

하지만 full SCC는 단순 표면장력만의 이론이 아니다. closure, distinction, separation, morphology, persistence가 함께 작동한다. 그래서 단순히 “합쳐지는 것이 energy상 유리하다”는 말만으로 full SCC의 formation 구조를 판단할 수 없다.

T-PreObj-1 이후 F-1은 이렇게 재해석된다.

> 문제는 $K=2$가 공허한지가 아니라, object-like single disk를 기준으로 삼은 생각 자체가 full SCC에서 맞는가이다.

### 2.8.3 M-1의 의미: 하나로 합쳐지는 것이 항상 답인가?

M-1은 $K=1$이 항상 선호되는 것처럼 보이는 문제였다. 이것은 pure boundary-energy 관점에서는 자연스럽다. 두 덩어리보다 한 덩어리가 boundary를 덜 가질 수 있기 때문이다.

쉬운 비유는 물방울이다. 작은 물방울 두 개가 가까이 있으면 하나로 합쳐지는 것이 자연스럽다. 표면적을 줄이는 방향이기 때문이다.

하지만 SCC의 field는 물방울보다 복잡하다. SCC field는 “경계가 적으면 무조건 좋다”가 아니다. 너무 합쳐지면 distinction이 약해질 수 있고, 내부 구조가 사라질 수 있으며, morphology나 persistence 조건이 바뀔 수 있다.

따라서 M-1은 “$K=1$이 항상 참인가?”에서 다음으로 바뀐다.

> 어떤 functional 층위에서는 merge가 맞고, 어떤 full SCC 층위에서는 multi-peak formation이 맞을 수 있다. 이 둘을 섞지 말아야 한다.

이 분리가 나중에 Layer I / II / III 분리와도 연결된다.

### 2.8.4 MO-1의 의미: labelled multi-field 공간은 모서리가 많다

MO-1은 Morse theory나 smooth analysis를 적용하기 어렵다는 문제였다. 특히 labelled multi-field space는 mass가 0이 되는 slot, active set이 바뀌는 지점, simplex boundary 같은 corner가 많다.

쉬운 비유로는 방이 여러 개 있는 건물을 생각할 수 있다. 각 방에 사람이 몇 명씩 들어갈 수 있는데, 어떤 방은 비고 어떤 방은 꽉 찬다. 사람이 방을 옮기는 순간 “활성 방의 수”가 바뀐다. 이 건물의 상태공간은 매끄러운 평지가 아니라 문턱, 계단, 복도, 막힌 벽이 많은 구조다.

그런 공간에서 바로 smooth theorem을 세우기는 어렵다.

그래서 연구는 single-field $\Sigma_m$로 되돌아갔다. $\Sigma_m$은 labelled rooms가 아니라 하나의 넓은 홀에 mass가 분포하는 공간이다. 여전히 boundary가 있지만, theorem-grade 분석을 하기 훨씬 안정적이다.

이것이 single-field 복귀의 수학적 이유다.

### 2.8.5 $K_{\mathrm{soft}}$의 초기 의미: 숫자를 세지 말고 구조를 읽자

$K_{\mathrm{soft}}$는 “몇 개냐”를 hard integer로 답하지 않으려는 시도였다.

비유하자면, 산맥을 세는 문제와 비슷하다. 지도에서 봉우리가 몇 개인지 세려면 threshold가 필요하다. 작은 언덕까지 봉우리로 볼 것인가? 큰 산만 볼 것인가? 능선으로 연결된 두 봉우리는 하나인가 둘인가?

hard count는 이런 질문에 민감하다. 그래서 초기에는 각 봉우리의 persistence를 가중해서 부드럽게 세는 방식이 자연스러워 보였다.

$$
K_{\mathrm{soft}}(u)=\sum_i\phi(\ell_i(u)).
$$

여기서 긴 bar는 큰 산맥이고, 짧은 bar는 작은 언덕이다. $\phi$는 “얼마나 큰 언덕부터 count에 넣을 것인가”를 정하는 lens다.

나중에 알게 된 점은 이 lens가 매우 중요하다는 것이다. 아무 lens나 쓰면 안 된다. 너무 부드러운 lens는 chart refinement로 생기는 작은 언덕들을 과하게 세어 버릴 수 있다. 이것이 WQ-LAT-1과 WQ-LAT-1.B의 교훈이다.

### 2.8.6 T-PreObj-1의 의미: object 이전에 이미 지형이 있다

T-PreObj-1은 single-formation 단계의 핵심 turning point다.

쉬운 비유로 다시 산맥을 쓰면, object-first 관점은 “산 하나가 있다”고 먼저 말한 뒤 그 산의 모양을 분석한다. SCC의 pre-objective 관점은 고도 지도 전체를 먼저 본다. 그 고도 지도에는 여러 봉우리, 능선, 골짜기가 있을 수 있다. “산 하나”라는 말은 나중에 그 지형을 해석하는 방식이다.

T-PreObj-1은 full SCC에서 단순한 하나의 둥근 산이 항상 자연스러운 primitive가 아니라는 것을 보여 준다. field는 object가 되기 전에 이미 여러 봉우리와 내부 구조를 만들 수 있다.

이 발견 때문에 Multi-Formation은 새 의미를 얻는다.

Multi-Formation은 “이미 여러 object가 있으니 label을 붙이자”가 아니다. 오히려 다음 질문이다.

> 하나의 field에서 이미 나타난 pre-objective multi-peak 구조를, 여러 interacting formation charts와 shared pool 위에서 어떻게 추적할 것인가?

---

## 3. Single-Formation SCC의 출발점

Single-Formation SCC의 theorem-grade 출발점은 finite graph 위의 mass-constrained soft field다.

$$
G_t=(X_t,N_t)
$$

$$
\Sigma_m(G_t)=
\{u:X_t\to[0,1]\mid \sum_{x\in X_t}u(x)=m\}.
$$

여기서 $G_t$는 시간 $t$의 relational graph다. $X_t$는 relational loci이고, $N_t$는 adjacency 또는 neighborhood 구조다. $\Sigma_m(G_t)$는 총 mass $m$을 갖는 soft cohesion field들의 공간이다.

이 공간이 중요한 이유는 다음과 같다.

1. 객체 label을 필요로 하지 않는다.
2. finite graph 위에서 compact하고 theorem-grade로 다룰 수 있다.
3. closure, distinction, boundary, morphology, persistence를 모두 field functional로 정의할 수 있다.
4. crisp object는 이 공간 위의 안정화된 field를 thresholding하거나 collapse한 사후 해석으로만 등장한다.

Single-Formation SCC에서 주요 canonical theorem family는 대략 다음과 같은 역할을 한다.

| 계열 | 역할 | 이론 내 의미 |
|---|---|---|
| existence / minimizer 계열 | 에너지 functional의 minimizer 존재 | field-first 모델이 공허하지 않음 |
| closure fixed point 계열 | closure operator와 안정 상태 | object-like closure의 수학적 조건 |
| distinction / boundary 계열 | 내부와 외부의 분리 | 객체성이 단순 mass가 아니라 구분을 필요로 함 |
| phase transition 계열 | parameter 변화에 따른 형상 전환 | formation은 연속 field에서 구조적으로 바뀜 |
| $\Gamma$-convergence 계열 | discrete-continuum 안정성 | graph model이 단순 discretization artifact가 아님 |
| gradient flow 계열 | 동역학적 수렴과 안정성 | formation이 시간 evolution을 가짐 |
| pre-objective mechanism | object 이전의 multi-peak / formation 발생 | “객체가 먼저”라는 관점을 뒤집는 핵심 |
| $\sigma$-framework | formation의 structural signature | 단순 count보다 풍부한 구조 언어 |

Single-Formation SCC의 핵심은 “하나의 object를 모델링한다”가 아니다. 오히려 하나의 soft field 안에서도 object-like structure가 어떻게 형성되고, 왜 crisp objecthood가 derivative인지 설명하는 것이다.

이 지점이 중요하다. 나중에 Multi-Formation으로 넘어갈 때, 여러 labelled fields를 도입하는 것은 ontology를 바꾸는 일이 아니다. 그것은 field-first 이론을 여러 formation chart로 lift하는 일이다. 이 lift가 조심스럽지 않으면, SCC가 처음 거부했던 object labels를 다시 몰래 들여오게 된다.

---

## 4. 왜 Multi-Formation으로 넘어갔는가

Single-Formation은 field-first ontology를 정립하는 데 충분했지만, 실제 형성 현상은 하나의 안정 덩어리만으로 끝나지 않는다. 하나의 scene, 하나의 relational substrate, 하나의 ambient state 안에서 여러 응집 구조가 동시에 생기고, 가까워지고, 겹치고, 병합되고, 사라지는 상황을 다뤄야 한다.

이 때문에 Multi-Formation이 필요해졌다.

하지만 Multi-Formation은 단순히 $K$개의 field를 나열하는 문제가 아니었다. 처음에는 다음과 같은 자연스러운 생각이 있었다.

$$
\mathbf u=(u^{(1)},\ldots,u^{(K)}).
$$

그러면 $K$개의 formation field를 두면 되는 것처럼 보인다. 그러나 이 순간 SCC의 field-first 원칙과 충돌이 생긴다.

- $K$는 외부에서 고정되는가?
- $K$는 실제 formation 개수인가?
- $K$개의 label은 object label인가?
- formation은 죽을 수 있는가?
- 두 formation이 merge하면 $K$는 줄어드는가?
- aggregate field의 topological component 수와 labelled slot 수는 같은가?
- soft count가 integer count를 대체할 수 있는가?

이 질문들은 모두 하나의 단어 $K$에 묶여 있었지만, 사실 서로 다른 층위의 질문이었다.

Single-Formation에서 Multi-Formation으로 넘어간 이유는 “여러 object를 세고 싶어서”가 아니라, field-first formation theory가 multi-peak, multi-component, multi-slot, multi-scale 현상을 다루기 위해 자기 자신의 count 언어를 정리해야 했기 때문이다.

---

## 5. K-confusion: 네 개의 K가 섞이기 시작한 문제

Multi-Formation의 초기 혼란은 $K$의 값이 어려워서가 아니라, $K$라는 한 글자가 서로 다른 네 가지 것을 동시에 가리켰기 때문에 생겼다.

### Four-K comparison table

| 기호 | 층위 | 무엇을 세는가 | 정수인가 | label 의존성 | 위험한 오해 |
|---|---|---|---|---|---|
| $K_{\mathrm{field}}$ | architecture / chart | 모델이 허용한 labelled field slot 수 | 예 | 강함 | primitive object 수라고 착각 |
| $K_{\mathrm{act}}^\varepsilon$ | lifecycle / active slots | mass가 $\varepsilon$ 이상인 labelled slot 수 | 예 | 강함 | 실제 topological component 수라고 착각 |
| $K_{\mathrm{bar}}^{\ell_{\min}}$ | aggregate topology | $U=\sum_j u^{(j)}$의 dominant $H_0$ bars 수 | 예 | 약함 또는 없음 | label count와 항상 같다고 착각 |
| $K_{\mathrm{soft}}^\phi$ | smooth morphology | bar lengths를 $\phi$로 가중한 soft count | 보통 실수 | 없음 | 아무 $\phi$나 써도 안정적이라고 착각 |

각각의 의미는 다음과 같다.

$$
K_{\mathrm{field}}
$$

는 architectural cap이다. 이것은 finite chart의 해상도다. $K_{\mathrm{field}}=4$라고 해서 “세계에 object가 네 개 있다”는 뜻이 아니다. 단지 모델이 네 개의 labelled formation slot을 허용한다는 뜻이다.

$$
K_{\mathrm{act}}^\varepsilon
$$

는 active labelled slot count다. slot $j$의 mass가 threshold $\varepsilon$을 넘으면 active로 본다. 이것은 lifecycle diagnostic이다.

$$
K_{\mathrm{bar}}^{\ell_{\min}}
$$

는 aggregate field $U$의 hard topological count다. superlevel persistent $H_0$ barcode에서 길이가 $\ell_{\min}$ 이상인 dominant terminal bars를 센다.

$$
K_{\mathrm{soft}}^\phi
$$

는 persistence-weighted soft count다.

$$
K_{\mathrm{soft}}^\phi(U)=\sum_i \phi(\ell_i(U)).
$$

핵심 문제는 이제 “$K$가 무엇인가?”가 아니다.

핵심 문제는 다음이다.

> 지금 말하는 $K$는 어느 층위의 $K$이며, 어떤 조건 아래 서로 일치하는가?

이 질문이 이후 Layered Ambient-State Architecture, WQ failures, reservoir reinterpretation, L1 proof chain을 모두 낳았다.

---

## 6. Layered Ambient-State Architecture가 왜 필요했는가

Layered Ambient-State Architecture는 세 가지를 섞지 않기 위해 도입되었다.

1. single-field theorem domain
2. shared-pool lifecycle domain
3. fixed-mass smooth local slices

이 세 층위를 섞으면, 정리의 domain과 실험의 domain과 count diagnostic의 domain이 뒤엉킨다.

### Layer architecture table

| Layer | 공간 | 주 역할 | 왜 필요한가 | 조심할 점 |
|---|---|---|---|---|
| Layer I | $\Sigma_m(G_t)$ | single-field SCC theorem domain | canonical SCC의 기본 정리들이 사는 곳 | labelled slot 없음 |
| Layer II | $\widetilde{\Sigma}^{K_{\mathrm{field}}}_M(G_t)$ | shared-pool Multi-Formation lifecycle domain | slot mass 변화, activation, extinction, aggregate projection을 다룸 | $K_{\mathrm{field}}$를 object 수로 오해하면 안 됨 |
| Layer III | $\Sigma_M^A(\mathbf m_A;G_t)$ | fixed active-set / fixed-mass smooth slice | jump 사이의 local theorem, stability 분석 | active set이 고정된 local chart일 뿐 |

Layer I:

$$
\Sigma_m(G_t)=\{u:X_t\to[0,1]\mid \sum_xu(x)=m\}.
$$

Layer II:

$$
\widetilde{\Sigma}^{K_{\mathrm{field}}}_M(G_t)
$$

는 shared-pool Multi-Formation 공간이다. 각 labelled slot $u^{(j)}$가 있고 총 mass $M$ 및 pointwise pool constraints가 있다. 여기서 slot mass가 줄거나 늘며 $K_{\mathrm{act}}$가 변할 수 있다.

Layer III:

$$
\Sigma_M^A(\mathbf m_A;G_t)
$$

는 active set $A$와 각 mass $\mathbf m_A$가 고정된 smooth slice다. K-jump 사이의 local theorem을 세우기에 적합하다.

ASCII diagram:

```text
Layer I:    Sigma_m(G_t)
              ^
              | aggregate projection U = sum_j u^(j)
              |
Layer II:   tilde Sigma_M^{K_field}(G_t)
              |
              | choose active set A, fixed masses m_A
              v
Layer III:  Sigma_M^A(m_A; G_t)
```

이 architecture의 도입은 단순한 형식 정리가 아니었다. 그것은 SCC의 field-first 원칙을 Multi-Formation에서 보존하기 위한 안전장치였다.

---

## 7. 처음 시도: NQ-242c / WQ-1에서 무엇을 보려 했는가

NQ-242c / WQ-1의 원래 목표는 OP-0008 계열의 질문을 실험적으로 건드리는 것이었다.

목표는 다음과 같았다.

1. $T^2_{20}$ 같은 finite torus graph에서 $K_{\mathrm{field}}=4$, 총 mass $M=90$인 shared-pool Layer II dynamics를 설정한다.
2. 두 trajectory A/B를 만든다.
3. pre-jump $\sigma$-standard가 같거나 비교 가능하게 만든다.
4. 자연스러운 labelled $K_{\mathrm{act}}$-jump, 예컨대 $3\to2$,가 일어나게 한다.
5. post-jump $\sigma$-standard가 달라지는지 본다.

기대는 다음이었다.

> 같은 pre-jump $\sigma$-standard에서 서로 다른 post-jump $\sigma$-standard가 나오면, $\sigma$-standard만으로는 K-jump inheritance를 결정할 수 없다는 evidence가 된다.

그러나 실제 결과는 실패였다.

NQ-242c / WQ-1은 failure mode F2로 끝났다.

- 14개 trajectory에서 $K_{\mathrm{act}}$-jump가 일어나지 않았다.
- $K_{\mathrm{act}}$는 계속 3이었다.
- 최소 slot mass도 $\varepsilon$보다 훨씬 컸다.
- parameter sweep을 해도 구조적으로 slot extinction이 발생하지 않았다.

이 실패는 $\sigma$-standard의 충분성 또는 불충분성을 증명하지 않았다. 왜냐하면 애초에 테스트하고 싶었던 K-jump event가 발생하지 않았기 때문이다.

중요한 해석은 다음이다.

> WQ-1은 OP-0008을 해결하지 못했다. 그러나 “현재 Layer II dynamics가 labelled slot을 쉽게 죽이지 않는다”는 사실을 보여 주었고, $K_{\mathrm{act}}$와 다른 count를 봐야 한다는 압력을 만들었다.

---

## 8. 실패에서 나온 핵심 발견: WQ-2의 F-B6

WQ-1의 실패 이후 중요한 전환은 WQ-2에서 일어났다.

WQ-2는 labelled slot count가 아니라 aggregate field를 보았다.

$$
U=\sum_j u^{(j)}.
$$

그리고 $U$의 $H_0$ persistent bars를 세었다.

결과는 결정적이었다.

$$
K_{\mathrm{act}}:3\to3
$$

였지만,

$$
K_{\mathrm{bar}}:3\to1
$$

였다.

즉 labelled active slots는 세 개가 계속 살아 있었다. 그러나 그 세 slot의 aggregate topology는 하나의 dominant component처럼 병합되었다.

비유하자면, 세 사람이 여전히 서 있다. 그러나 빛을 비추면 세 사람의 그림자가 하나로 합쳐진다. labelled individual은 셋인데, aggregate shadow는 하나다.

이것이 turning point였다.

이제 질문은 “왜 $K_{\mathrm{act}}$-jump가 안 생겼는가?”에서 다음으로 바뀌었다.

> labelled slot count와 aggregate topological count는 언제 같고, 언제 달라지는가?

이 질문이 L1 proof chain의 직접적인 출발점이다.

---

## 9. Layer I retry와 σ-standard의 한계

WQ-1.C는 Layer I single-field dynamics에서 H0 bar-death를 다시 보려는 시도였다. 목적은 labelled slot extinction이 아니라, single-field aggregate topology에서 bar-death event를 만들고 $\sigma$-standard가 그것을 포착하는지 보는 것이었다.

결과는 다시 단순한 성공이 아니었다.

- compressed B에서는 bar-death가 robust하게 나타났다.
- equilateral A에서는 같은 방식의 event가 나타나지 않았다.
- 따라서 A/B를 symmetric comparison으로 쓰기 어려웠다.

WQ-1.C-R2는 다시 Layer II aggregate $U(t)$로 돌아가 projection된 aggregate $\sigma$를 분석했다. 여기서는 A/B 모두에서 aggregate H0 bar-death가 보였다. 그러나 현재의 $\sigma$-standard cluster structure는 그 event를 제대로 구분하지 못했다.

핵심 결론은 다음이다.

1. aggregate H0 bar-death는 실제로 존재한다.
2. 그러나 현재 $\sigma$-standard는 그 topological transition을 충분히 민감하게 반영하지 못한다.
3. 이것은 OP-0008을 해결한 것이 아니다.
4. $\sigma$-rich로 돌아가기 전에, count/topology baseline이 먼저 필요하다.

즉 WQ-1.C와 R2는 실패했지만, 무엇이 부족한지 명확히 했다. 바로 $K_{\mathrm{act}}$, $K_{\mathrm{bar}}$, $K_{\mathrm{soft}}$의 관계를 먼저 정리해야 한다는 것이다.

---

## 10. Reservoir / Latent Index Space로의 전환

WQ 실패들이 누적되면서 중요한 해석 전환이 생겼다.

사용자의 핵심 통찰은 다음과 같이 요약할 수 있다.

> formation이 무에서 유로 창조되는 것이 아니라, 잠재 index space 안에 있는 reservoir를 finite chart가 어떤 해상도로 잘라내는 것이다.

이 관점에서는 $K_{\mathrm{field}}$가 세계의 object 수가 아니다. 그것은 latent formation reservoir를 finite number of slots로 근사하는 chart resolution이다.

working-grade formal idea는 다음과 같다.

$$
\rho:\mathcal A\times X\to[0,1].
$$

$$
U_\rho(x)=\int_{\mathcal A}\rho(\alpha,x)\,d\nu(\alpha).
$$

여기서 $\mathcal A$는 latent index space이고, $\rho$는 reservoir field다. finite $K_{\mathrm{field}}$는 $\mathcal A$를 $K$개의 chart element 또는 basis-like slot으로 잘라서 보는 truncation이다.

이 해석은 강력하다.

1. $K_{\mathrm{field}}$가 primitive object count가 아니라 chart resolution이 된다.
2. $K_{\mathrm{act}}$는 finite chart 안에서 threshold를 넘은 slot 수가 된다.
3. $K_{\mathrm{bar}}$는 finite chart가 바뀌어도 aggregate morphology가 안정적인지 검사하는 count가 된다.
4. $K_{\mathrm{soft}}$는 reservoir-invariant smooth count가 되려면 envelope $\phi$가 매우 신중해야 한다는 문제가 된다.

그러나 이 reservoir theory는 현재 canonical이 아니다. 그것은 Multi-Formation의 K-selection 문제와 latent formation interpretation을 풀기 위한 working-grade 방향이다.

---

## 11. WQ-LAT-1: reservoir resolution sweep

WQ-LAT-1은 reservoir reinterpretation을 실험적으로 검사했다.

질문은 다음이었다.

> $K_{\mathrm{field}}$를 늘려도 aggregate field와 topological count가 안정적인가?

실험은 $K_{\mathrm{field}}\in\{3,4,6,8,12\}$ 같은 finite chart refinements를 비교했다. 기대는 다음이었다.

- aggregate field $U_K$는 안정화되어야 한다.
- $K_{\mathrm{bar}}$는 chart refinement에 대해 안정적이어야 한다.
- dominant bar profile도 안정적이어야 한다.
- $K_{\mathrm{soft}}$도 가능하면 안정적이어야 한다.

결과는 mixed but productive였다.

- aggregate field는 안정화되었다.
- $K_{\mathrm{bar}}$는 integer morphology level에서 안정적이었다.
- dominant bar profile도 안정적이었다.
- 그러나 default saturating $\phi$를 쓴 $K_{\mathrm{soft}}^\phi$는 drift했다.

해석은 분명하다.

> hard topological count는 reservoir chart refinement 아래에서 안정적인 신호를 보였지만, default smooth envelope는 안정적이지 않았다.

이는 reservoir idea 자체를 무너뜨린 것이 아니라, $K_{\mathrm{soft}}$의 정의에서 $\phi$가 장식이 아니라 구조라는 사실을 드러냈다.

---

## 12. WQ-LAT-1.B: $\phi$는 장식이 아니라 구조다

WQ-LAT-1.B는 바로 이 문제를 겨냥했다.

질문은 다음이었다.

> 어떤 $\phi$를 써야 $K_{\mathrm{soft}}^\phi$가 chart refinement 아래에서 reservoir-stable한 count가 되는가?

결과는 명확했다.

- default $\phi_{\mathrm{sat}}$는 실패했다.
- hard threshold family는 강하게 성공했다.
- high-slope logistic, 특히 $s=100$ 계열은 성공했다.
- shifted-saturating family, 특히 $\beta=20$ 계열도 성공했다.

따라서 결론은 다음이다.

$$
\phi\in\Phi_{\mathrm{res}}
$$

이어야 한다.

즉 arbitrary monotone Lipschitz $\phi$는 안전하지 않다. $\phi$는 단순한 smoothing decoration이 아니라 count identity와 reservoir invariance를 결정하는 구조적 선택이다.

이 결과는 다음 단계인 L1-M을 준비한다.

> L1-M의 자연스러운 목표는 $T$-L1-F의 hard-count bridge 위에 $\Phi_{\mathrm{res}}$ envelope 조건을 얹어 $K_{\mathrm{soft}}$ corollary를 만드는 것이다.

### WQ experiment history table

| 실험 / 진단 | 왜 실행했는가 | 기대한 것 | 실제 결과 | 낳은 개념 / 다음 질문 |
|---|---|---|---|---|
| NQ-242c / WQ-1 | 자연스러운 labelled $K_{\mathrm{act}}$-jump를 만들어 OP-0008형 $\sigma$-inheritance를 테스트 | $K_{\mathrm{act}}:3\to2$ 같은 extinction event | F2: 14개 trajectory에서 $K_{\mathrm{act}}$가 계속 3 | 현재 dynamics는 slot을 쉽게 죽이지 않음. aggregate count를 봐야 함 |
| WQ-2 | WQ-1 failure lineage에서 aggregate topology를 검사 | $K_{\mathrm{act}}$와 다른 count가 움직일 수 있음 | $K_{\mathrm{act}}:3\to3$, $K_{\mathrm{bar}}:3\to1$ | labelled slot과 aggregate topology 분리. L1 질문 탄생 |
| WQ-1.C | Layer I single-field에서 H0 bar-death를 직접 만들기 | A/B 모두 bar-death 후 $\sigma$ 비교 | B compressed만 bar-death, A equilateral은 안정 | symmetric comparison 실패. dynamics asymmetry 확인 |
| WQ-1.C-R2 | Layer II aggregate projection에서 $\sigma$-standard가 H0 transition을 보는지 검사 | aggregate bar-death가 $\sigma$로 포착됨 | bar-death는 보이나 cluster-structure $\sigma$에는 거의 보이지 않음 | 현재 $\sigma$-standard의 blind spot 확인 |
| WQ-LAT-1 | reservoir chart refinement 아래 안정량 확인 | $U$, $K_{\mathrm{bar}}$, $K_{\mathrm{soft}}$ 모두 안정 | $U$, $K_{\mathrm{bar}}$, dominant bars 안정; default $K_{\mathrm{soft}}$ drift | hard topology는 안정, soft envelope는 문제 |
| WQ-LAT-1.B | $\phi$-envelope를 바꿔 $K_{\mathrm{soft}}$ 안정성 회복 | sharp $\phi$가 chart-invariance를 복원 | hard threshold, logistic $s=100$, shifted-sat $\beta=20$ 성공 | $\Phi_{\mathrm{res}}$ 필요. L1-M 준비 |
| L1-G | L1 hypotheses가 실제 diagnostic에서 측정 가능한지 확인 | WQ lineage가 어떤 조건을 깨는지 드러남 | H8 count mismatch 등 확인, H10은 직접 측정 불가 | WQ mismatch는 L1 regime 밖. local-to-global gap이 핵심 |
| L1-I | L1-J 조건이 공허하지 않은지 검사 | 일부 configuration이 feasible | 439/1920 feasible-with-budget | resolved regime nonempty. T-L1-F가 vacuous하지 않음 |
| L1-H2 | boundary leakage 방향을 stress-test | $\ell_{\mathrm{global}}\le\ell_{\mathrm{local}}$ | 5/5 stress tests 통과 | local-to-global upper-bound gap 폐쇄 |
| L1-J | P0-P11 theorem package를 Cat-A 후보로 정리 | count bridge strong candidate | decay-to-cut diagnostics 통과, THEOREM_CANDIDATE_STRONG | audit와 P7 지위 결정 후 T-L1-F 승격 |

---

## 13. L1 proof chain은 왜 시작되었는가

L1 proof chain은 하나의 baseline theorem이 필요했기 때문에 시작되었다.

WQ-2 이후 theory는 다음 사실을 알게 되었다.

$$
K_{\mathrm{act}}\neq K_{\mathrm{bar}}
$$

인 상황이 실제로 나타난다. 그런데 이 mismatch를 의미 있게 해석하려면, 먼저 일치해야 하는 regime이 있어야 한다.

만약 어떤 조건에서도 $K_{\mathrm{act}}$와 $K_{\mathrm{bar}}$가 일치하지 않는다면, mismatch는 그냥 두 count가 서로 무관하다는 뜻일 뿐이다. 반대로, 잘 분리되고 해상도가 충분한 resolved regime에서

$$
K_{\mathrm{bar}}=K_{\mathrm{act}}
$$

가 증명되면, 그 밖에서의 mismatch는 meaningful signal이 된다. overlap, bridge, unresolved merge, K-jump, σ-rich event를 해석할 기준선이 생긴다.

### L1 journey table

| 단계 | 등장한 문제 | 만든 정의/정리 | 결과 |
|---|---|---|---|
| L1 formalization | active slot count와 aggregate bar count가 다른 객체임 | WS-1..WS-8 well-separated package | theorem shape와 failure modes 정리 |
| L1-A merge level | slot 하나가 dominant bar 하나를 낳는 조건이 불명확 | representative peak, birth height, merge level, persistence margin | lower-bound skeleton 형성 |
| L1-B bridge bound | distance alone으로 조기 병합을 막을 수 없음 | separating cut, cut height, bridge bound lemma | cut가 bridge height를 상계한다는 finite-graph fact 확보 |
| L1-C slot-to-bar | active slot과 global bar의 대응이 모호 | terminal-death H0 convention, association map | bijection의 형식 정의 |
| L1-D no extra bar | 한 slot이 여러 dominant bars를 만들 수 있음 | secondary-bar suppression | overcount 방지 조건 |
| L1-E inactive suppression | inactive residual이 fake bar를 만들 수 있음 | $R_{\mathrm{inact}}$, height/persistence suppression | inactive overcount 방지 조건 |
| L1-F synthesis | A-E 조건들이 흩어져 있음 | H1-H10 synthesis package | proof skeleton 완성, local-to-global gap 노출 |
| L1-G diagnostics | 조건들이 측정 가능한지 불명확 | L1Hyp diagnostic scripts | WQ trajectories는 regime 밖임을 확인 |
| L1-H local-to-global | local barcode control이 global로 이전되는지 불명확 | LG conditions, counterexample registry | 핵심 gap을 PO-LH1로 축소 |
| L1-I feasibility | 조건들이 공허할 위험 | constants feasibility sweep | 439/1920 feasible-with-budget로 non-vacuity 확인 |
| L1-H2 boundary leakage | global bar가 local보다 길어질 수 있는지 우려 | $\ell_{\mathrm{global}}\le\ell_{\mathrm{local}}$ lemma | local-to-global upper bound 폐쇄 |
| L1-J Cat-A attempt | theorem package를 canonical 후보로 정리해야 함 | P0-P11 package | THEOREM_CANDIDATE_STRONG |
| L1-K audit | proof hygiene와 circularity 점검 필요 | external audit, contradiction repair | audit passed, substantive blocker 제거 |
| L1-L P7 | decay-to-cut의 지위 불명확 | P7 route analysis | P7은 strong stationarity 아래 유도 가능, 일반적으로는 safe hypothesis |

L1 체인의 의미는 단순히 “정리 하나를 증명했다”가 아니다. 그것은 count language의 기준선을 세웠다.

---

## 14. 핵심 직관: local bar가 global에서 더 길어질 수 있는가?

L1-H2의 핵심은 매우 직관적이다.

어떤 local neighborhood $G_j^r$ 안에서 component가 persistent bar를 만든다고 하자. 이 local graph에는 가능한 경로가 적다. 그런데 global graph $G$로 가면 경로가 더 많아진다.

superlevel filtration에서 경로가 더 많아진다는 것은 component들이 더 일찍 만날 수 있다는 뜻이다. 더 늦게 만나는 것이 아니다. 따라서 local에서 보던 bar가 global에서 더 길어지는 방향은 자연스럽지 않다.

정리의 핵심 부등식은 다음이다.

$$
\ell_{\mathrm{global}}\le\ell_{\mathrm{local}}.
$$

이 부등식은 boundary leakage concern을 뒤집었다. 처음에는 외부 경로가 local component를 이상하게 연장시켜 dominant bar를 만들 수 있다고 걱정했다. 그러나 corrected direction은 global path가 bar를 길게 만드는 것이 아니라, 오히려 더 빨리 merge시켜 bar를 짧게 만들 수 있다는 것이다.

이것이 왜 중요한가?

L1-F까지는 local secondary-bar suppression이 global에서도 유지되는지 불분명했다. L1-H2는 local에서 $\ell_{\min}$ 아래로 눌린 secondary bar가 global에서 갑자기 $\ell_{\min}$ 이상 dominant bar로 승격되는 것을 막는 핵심 근거를 제공했다.

---

## 15. L1-I가 왜 중요했는가: 조건이 공허하지 않은가?

조건부 정리의 가장 흔한 위험은 조건이 너무 강해서 아무 상태도 만족하지 않는 것이다.

L1-J의 P0-P11 package는 강하다. disjoint active neighborhoods, low boundary collar, background suppression, birth height margin, decay-to-cut, local secondary suppression, inactive residual suppression 등을 요구한다.

따라서 반드시 물어야 했다.

> 이 조건들을 동시에 만족하는 상태가 실제로 존재하는가?

L1-I는 이 질문에 empirical answer를 주었다.

- 총 1920개 configuration을 sweep했다.
- 그중 439개가 `FEASIBLE_WITH_BUDGET`이었다.
- raw Gaussian mode에서는 feasibility가 더 높았다.
- WQ-1 default production normalization은 대체로 infeasible이었다.

해석은 다음이다.

1. L1-J resolved regime은 공허하지 않다.
2. 그러나 WQ-1 default dynamics는 그 regime에 잘 들어가지 않는다.
3. 따라서 WQ-1의 mismatch는 T-L1-F의 반례가 아니라, unresolved / overlap / bridge regime의 예다.

이 점은 T-L1-F의 지위를 이해하는 데 매우 중요하다. T-L1-F는 모든 Multi-Formation state를 다루는 정리가 아니다. resolved regime이 실제로 비어 있지 않다는 것을 확인한 뒤, 그 regime 안에서 count bridge를 증명한 정리다.

---

## 16. P7는 무엇이고 왜 조심해야 하는가

P7은 decay-to-cut condition이다. 직관적으로는 active field들이 자기 support 밖으로 충분히 decay해서, 서로 다른 active regions 사이의 bridge height가 낮게 유지되어야 한다는 조건이다.

P7이 필요한 이유는 명확하다. active regions 사이의 corridor가 너무 높으면, aggregate field $U$에서 서로 다른 slot들이 일찍 merge한다. 그러면 $K_{\mathrm{bar}}$가 $K_{\mathrm{act}}$보다 작아질 수 있다.

그러나 P7은 조심해야 한다.

L1-L은 P7의 가능한 derivation routes를 검토했다. 결론은 다음과 같다.

- strong stationarity / source-cancellation / Agmon-type decay 같은 강한 추가 조건 아래에서는 P7을 유도할 수 있다.
- Gaussian model class에서는 P7이 자연스럽게 성립할 수 있다.
- 하지만 일반 SCC state 전체에서 P7이 자동으로 성립한다고 말할 수는 없다.
- 특히 mass multiplier, uniform offset, shared-pool projection 등은 decay-to-cut를 깨뜨릴 수 있다.

따라서 canonical T-L1-F에서 P7의 지위는 다음이다.

> P7은 resolved-regime의 safe technical hypothesis이지, 모든 SCC 상태에 대한 global theorem이 아니다.

이 distinction을 지키는 것이 과대주장을 막는다.

---

## 17. 최종 정리: T-L1-F

T-L1-F의 이름은 다음과 같다.

> T-L1-F — Hard-Bar / Active-Count Bridge under the L1-J Regime.

정리의 핵심 statement는 다음이다.

finite graph $G$ 위의 shared-pool Multi-Formation state $\mathbf u\in\widetilde{\Sigma}^{K_{\mathrm{field}}}_M(G)$를 생각하자. aggregate field를

$$
U(\mathbf u)=\sum_j u^{(j)}
$$

로 둔다. active set을 $A^\varepsilon(\mathbf u)$, active count를

$$
K_{\mathrm{act}}^\varepsilon(\mathbf u)=|A^\varepsilon(\mathbf u)|
$$

로 둔다. aggregate field의 dominant hard-bar count를

$$
K_{\mathrm{bar}}^{\ell_{\min}}(U(\mathbf u);G)
$$

로 둔다.

P0-P11 조건 아래에서,

$$
K_{\mathrm{bar}}^{\ell_{\min}}(U(\mathbf u);G)
=
K_{\mathrm{act}}^\varepsilon(\mathbf u).
$$

또한 active slots와 dominant terminal $H_0$ bars 사이의 association

$$
\mathcal A_{\mathrm{bar}}
$$

는 bijection이다.

### T-L1-F P0-P11 table

| 조건 | 이름 | 역할 | 왜 필요한가 |
|---|---|---|---|
| P0 | terminal-death $H_0$ convention | persistence convention 고정 | bar count의 의미를 고정 |
| P1 | deterministic tie convention | tie / plateau 처리 | association ambiguity 제거 |
| P2 | active mass + connected $\delta$-support | active slot의 실질성 | empty label을 active로 세지 않음 |
| P3 | disjoint active neighborhoods | resolved separation | overlap으로 인한 조기 병합 방지 |
| P4 | low boundary collar | boundary height control | local component가 외부와 높게 연결되는 것 방지 |
| P5 | background suppression on $U$ | aggregate background 제어 | fake bars와 high bridges 억제 |
| P6 | birth height lower bound | dominant birth 보장 | slot마다 bar birth가 충분히 높음 |
| P7 | decay-to-cut | bridge height decay | slot 사이 corridor가 낮게 유지됨 |
| P8 | tightened H6 on $G_j^r$ | local secondary-bar suppression | 한 slot이 여러 dominant bars를 만들지 않음 |
| P9 | local perturbation control | local-to-aggregate 안정성 | 개별 field와 aggregate의 차이 제어 |
| P10 | inactive residual suppression | inactive noise 억제 | inactive slot이 fake dominant bar 생성 방지 |
| P11 | margin ledger | 모든 margin의 동시 호환 | $\ell_{\min}$, cut, birth, residual 조건을 함께 묶음 |

T-L1-F의 의미는 매우 구체적이다.

이 정리는 Multi-Formation 전체를 해결하지 않는다. OP-0005도 해결하지 않고, OP-0008도 해결하지 않는다. $K_{\mathrm{soft}}=K_{\mathrm{act}}$를 말하지도 않는다.

그러나 이 정리는 최초의 canonical resolved-regime count bridge다.

이제 theory는 다음 baseline을 갖는다.

> 충분히 분리되고, background가 낮고, decay-to-cut가 성립하고, local secondary bars가 억제되는 regime에서는 labelled active slot count와 aggregate hard topological count가 정확히 일치한다.

이 baseline이 있기 때문에, 앞으로의 overlap, K-jump, $\sigma$-rich, soft-count 연구가 의미를 얻는다.

---

## 18. 현재까지 증명된 것

### Proved / empirical / open status table

| 명제 | 상태 | 설명 |
|---|---|---|
| Single-field SCC core | canonical foundation | $\Sigma_m(G_t)$ 위의 field-first SCC 정리 체계. object는 derivative라는 구조가 canonical core에 반영됨 |
| $u_t$ primitive / object derivative | canonical commitment | $u_t$는 class/mask가 아니라 primitive cohesion field |
| $K_{\mathrm{field}}$ vs $K_{\mathrm{act}}$ 분리 | canonical commitment | CV-1.5.1에서 K-status가 정리되어 $K_{\mathrm{field}}$는 cap, $K_{\mathrm{act}}$는 diagnostic으로 분리됨 |
| T-L1-F | Cat-A conditional theorem | P0-P11 resolved regime 아래 $K_{\mathrm{bar}}^{\ell_{\min}}=K_{\mathrm{act}}^\varepsilon$ 및 association bijection |
| L1-H2 local-to-global inequality | proof-grade working chain, absorbed into T-L1-F provenance | $\ell_{\mathrm{global}}\le\ell_{\mathrm{local}}$ 방향으로 boundary leakage concern 폐쇄 |
| L1-I feasibility | empirical support | 439/1920 feasible-with-budget; resolved regime이 공허하지 않음을 지지 |
| WQ-2 F-B6 | empirical discovery | $K_{\mathrm{act}}$는 3 유지, $K_{\mathrm{bar}}$는 3에서 1로 collapse 가능 |
| WQ-LAT-1 | empirical reservoir support | aggregate $U$, hard $K_{\mathrm{bar}}$, dominant bars는 chart refinement 아래 안정적 |
| WQ-LAT-1.B | empirical $\Phi_{\mathrm{res}}$ evidence | default $\phi$는 실패, hard/logistic/shifted-sat 계열은 안정적 |
| L1-L P7 route | conditional derivation / safe hypothesis | strong stationarity 아래 derivable; 일반 SCC global theorem은 아님 |

정리하면, 현재 실제로 canonical하게 증명된 Multi-Formation bridge는 T-L1-F다. 그것은 conditional theorem이다. working evidence와 experiments는 그 조건이 의미 있고 비공허하며, 다음 soft-count 단계로 갈 수 있음을 보여 준다.

---

## 19. 아직 증명되지 않은 것

다음은 아직 증명되지 않았다.

| 항목 | 현재 상태 | 왜 아직 중요한가 |
|---|---|---|
| global $K_{\mathrm{bar}}=K_{\mathrm{act}}$ | false / forbidden overclaim | WQ-2 같은 mismatch가 실제로 있음 |
| global $K_{\mathrm{soft}}=K_{\mathrm{act}}$ | open / forbidden overclaim | $\phi$ 선택에 민감함 |
| L1-M | not yet written as standalone theorem file | $\Phi_{\mathrm{res}}$ 아래 soft-count corollary 필요 |
| OP-0005 K-selection | open | $K_{\mathrm{field}}$의 선택 mechanism은 아직 canonical하게 해결되지 않음 |
| OP-0008 σ-inheritance | open / tentative | K-jump 후 $\sigma$-standard inheritance non-determinism은 아직 Cat-A 아님 |
| $\sigma$-rich sufficiency | open | 현재 $\sigma$-standard는 H0 bar-death를 충분히 포착하지 못함 |
| reservoir canonicalization | working-grade | latent index space는 강력한 해석이나 canonical commitment는 아님 |
| P7 for all SCC states | not proved | P7은 strong stationarity 아래 가능하지만 일반 SCC 전체에서는 아님 |
| dynamic persistence bridge | open | T-L1-F는 static resolved-regime bridge이며 full dynamics theorem은 아님 |
| graph-family generalization | open | finite graph 조건을 넘는 family-level theorem 필요 |
| weak-overlap approximation | open | resolved regime 밖에서 approximate bridge가 필요 |

특히 중요한 non-claim은 다음이다.

> T-L1-F는 OP-0008을 해결하지 않는다.  
> T-L1-F는 $K_{\mathrm{soft}}$ identity를 증명하지 않는다.  
> T-L1-F는 reservoir theory를 canonical로 만들지 않는다.  
> T-L1-F는 P7을 모든 SCC state에서 유도하지 않는다.

---

## 20. 이론의 방향성 평가

현재 방향은 강하다. 이유는 네 가지다.

첫째, SCC는 field-first ontology를 유지하고 있다. Multi-Formation이 label machinery를 도입했지만, $K_{\mathrm{field}}$를 primitive object count로 격상시키지 않고 chart cap으로 낮추었다.

둘째, theory는 실패를 숨기지 않고 구조로 바꿨다. WQ-1의 F2는 단순한 실패가 아니라 $K_{\mathrm{act}}$-jump가 현재 dynamics에서 잘 생기지 않는다는 발견이었다. WQ-2의 F-B6는 labelled count와 aggregate topology가 갈라질 수 있음을 보여 주었다. WQ-LAT-1의 $K_{\mathrm{soft}}$ drift는 $\phi$가 구조적 선택이라는 사실을 드러냈다.

셋째, Layer I / II / III architecture가 theorem domain과 lifecycle domain과 local slice를 분리했다. 이 분리가 없으면 어떤 정리가 어느 공간에서 성립하는지 계속 혼동된다.

넷째, T-L1-F는 resolved-regime baseline을 제공했다. 이제 mismatch는 단순 혼란이 아니라 regime failure, overlap, bridge, unresolved merge, dynamic event로 해석될 수 있다.

그러나 위험도 분명하다.

| 위험 | 설명 | 방지책 |
|---|---|---|
| 조건 과다 | P0-P11이 강해 보일 수 있음 | L1-I non-vacuity와 이후 weak-overlap theorem으로 보완 |
| overclaim | resolved theorem을 global identity처럼 말할 위험 | non-claims를 항상 명시 |
| P7 dependence | decay-to-cut가 일반 SCC theorem이 아님 | P7을 safe hypothesis로 유지하고 별도 derivation 연구 |
| soft-count sensitivity | $K_{\mathrm{soft}}$가 $\phi$에 민감 | $\Phi_{\mathrm{res}}$ 제한 |
| premature OP-0008 return | count baseline 없이 $\sigma$-rich로 바로 가면 반복 실패 가능 | L1-M, L1-N 이후 OP-0008 re-entry |

---

## 21. 앞으로의 로드맵

현재 가장 안전한 순서는 $\sigma$-rich로 바로 뛰어드는 것이 아니라, count bridge를 hard에서 soft, static에서 dynamic, resolved에서 weak-overlap으로 확장하는 것이다.

### Future roadmap table

| 순서 | 작업 | 목표 | 왜 이 순서인가 |
|---|---|---|---|
| 1 | L1-M | $\Phi_{\mathrm{res}}$ 아래 soft-count corollary | T-L1-F hard bridge를 $K_{\mathrm{soft}}$로 확장 |
| 2 | L1-N | dynamics-compatible resolved regime | static bridge를 flow segment에 연결 |
| 3 | L1-O | graph-family generalization | finite graph proof를 graph family / scaling으로 확장 |
| 4 | L1-P | weak-overlap approximate bridge | resolved regime 밖 mismatch를 정량화 |
| 5 | OP-0008 re-entry | K-jump / $\sigma$-inheritance 재진입 | count baseline과 soft bridge 이후에야 안전 |
| 6 | $\sigma$-rich minimal packet | H0/topology-sensitive signature 보강 | 기존 $\sigma$-standard의 blind spot 해결 |
| 7 | K-selection / reservoir effective rank | $K_{\mathrm{field}}$ selection mechanism | latent reservoir와 OP-0005 연결 |

이 순서가 안전한 이유는 간단하다.

OP-0008은 K-jump와 $\sigma$-inheritance의 문제다. 그런데 지금까지의 실패가 보여 준 것은, K-jump 자체가 어떤 count에서 일어나는지 명확히 해야 한다는 점이다. $K_{\mathrm{act}}$-jump인지, $K_{\mathrm{bar}}$-collapse인지, $K_{\mathrm{soft}}$-drift인지, reservoir chart refinement artifact인지 구분하지 않으면 $\sigma$-rich도 같은 혼란에 빠진다.

따라서 다음 직접 작업은 L1-M이다.

$$
\Phi_{\mathrm{res}}
$$

아래에서

$$
K_{\mathrm{soft}}^\phi
$$

가 $K_{\mathrm{bar}}$, 그리고 T-L1-F를 통해 $K_{\mathrm{act}}$와 어떤 오차범위로 연결되는지 정리해야 한다.

---

## 22. 결론: 이 이론은 지금 어디에 있는가

SCC는 객체를 먼저 가정하지 않겠다는 거부에서 시작했다. 이 거부는 철학적 선언에 그치지 않았다. 관계 그래프 위의 soft cohesion field

$$
u_t:X_t\to[0,1]
$$

를 primitive로 두고, object를 안정화된 formation의 사후 해석으로 만드는 수학적 프로그램으로 발전했다.

Single-Formation SCC는 $\Sigma_m(G_t)$ 위에서 closure, distinction, boundary, energy, persistence, pre-objective mechanism을 정리했다. 그 과정에서 “하나의 field 안에서도 object-like structure는 나중에 생긴다”는 핵심이 분명해졌다.

Multi-Formation으로 넘어가자 $K$ 문제가 폭발했다. $K$는 하나가 아니었다. $K_{\mathrm{field}}$, $K_{\mathrm{act}}$, $K_{\mathrm{bar}}$, $K_{\mathrm{soft}}$가 서로 다른 층위에서 서로 다른 것을 세고 있었다. WQ-1은 labelled $K_{\mathrm{act}}$-jump를 만들지 못했다. 그러나 WQ-2는 더 중요한 것을 보여 주었다. labelled slots는 셋으로 남아 있어도 aggregate topology는 하나로 합쳐질 수 있다.

이 실패들은 theory를 약화시키지 않았다. 오히려 무엇을 정의해야 하는지 알려 주었다. Layered Ambient-State Architecture는 theorem domain과 lifecycle domain을 분리했고, reservoir / latent index space 해석은 $K_{\mathrm{field}}$를 object count가 아니라 chart resolution으로 재해석했다. WQ-LAT-1과 WQ-LAT-1.B는 hard topological count가 chart refinement 아래 안정적일 수 있지만, soft count는 $\phi$ 선택에 구조적으로 의존한다는 사실을 보여 주었다.

그 결과 L1 proof chain이 시작되었다. L1-A부터 L1-L까지의 작업은 “resolved regime에서는 labelled active slots와 aggregate dominant bars가 정확히 대응한다”는 baseline을 만들기 위해 필요한 모든 장애물을 하나씩 처리했다. merge level, bridge cut, slot-to-bar association, no-extra-bar, inactive suppression, local-to-global transfer, constants feasibility, boundary leakage, P7 decay-to-cut의 지위가 순서대로 정리되었다.

현재 canonical하게 도달한 핵심은 T-L1-F다.

$$
K_{\mathrm{bar}}^{\ell_{\min}}(U(\mathbf u);G)
=
K_{\mathrm{act}}^\varepsilon(\mathbf u)
$$

는 P0-P11 resolved regime 아래에서 성립한다. 또한 active slots와 dominant terminal $H_0$ bars 사이의 association은 bijection이다.

이것은 final theory가 아니다. 그러나 매우 중요한 기준선이다.

이제 theory는 “언제 count들이 일치하는가”를 하나는 증명했다. 다음 단계는 “언제, 어떻게, 얼마나 깨지는가”를 연구하는 것이다. 그 첫 단계는 L1-M, 즉 $\Phi_{\mathrm{res}}$ 아래 soft-count corollary다. 그 뒤에야 dynamic resolved regime, weak-overlap approximation, $\sigma$-rich, OP-0008, OP-0005로 안전하게 돌아갈 수 있다.

결론적으로, SCC / Multi-Formation은 지금 다음 위치에 있다.

> 객체를 먼저 놓지 않는 field-first 이론에서 출발해, single-field SCC의 정리 체계를 만들었고, Multi-Formation에서 $K$의 네 의미를 분리했으며, 실패한 WQ 실험들을 통해 labelled count와 aggregate topology의 차이를 발견했고, L1 proof chain을 통해 resolved regime의 첫 canonical count bridge를 증명한 상태다. 앞으로의 과제는 이 bridge를 soft count, dynamics, overlap, reservoir, $\sigma$-rich로 확장하는 것이다.

---

## 부록 A. 핵심 수식과 개념을 더 천천히 읽기

이 문서의 본문은 역사적 흐름을 중심으로 작성되었다. 그러나 SCC / Multi-Formation의 핵심은 몇 개의 수식이 어떤 철학적 결정을 담고 있는지 이해하는 데 있다. 이 부록은 그 수식들을 더 천천히 풀어 쓴다.

### A.1 $X_t$는 object set이 아니다

가장 먼저 오해하면 안 되는 것은 $X_t$의 의미다. 많은 모델에서는 domain의 원소를 이미 object, particle, agent, pixel-object 같은 것으로 읽는다. SCC에서는 그렇게 읽으면 안 된다.

SCC에서 $X_t$는 relational loci의 집합이다. 즉 어떤 관계, adjacency, influence, contact, neighborhood가 정의될 수 있는 자리들의 집합이다. 이 자리들이 이미 object라는 뜻은 아니다. object는 $X_t$ 위에서 정의된 field가 안정화된 뒤에 나오는 해석이다.

따라서 다음 수식은 단순한 함수 표기가 아니라 ontology의 선언이다.

$$
u_t:X_t\to[0,1].
$$

$u_t(x)$는 “$x$가 어떤 object에 속하는가”가 아니다. 그것은 $x$가 현재의 cohesion field에 어느 정도 참여하는가를 나타낸다. 이 차이가 작아 보이지만, 이론 전체를 바꾼다.

object-first 관점이라면 먼저 object label이 있고, 그 label에 따라 membership function을 만든다. SCC 관점에서는 membership-like field가 먼저 있고, object label은 나중에 안정적인 pattern을 설명하기 위해 붙인다.

### A.2 $\Sigma_m(G_t)$는 왜 theorem-grade domain인가

Single-Formation의 기본 공간은 다음이다.

$$
\Sigma_m(G_t)=
\{u:X_t\to[0,1]\mid \sum_{x\in X_t}u(x)=m\}.
$$

이 공간은 세 가지 점에서 중요하다.

첫째, mass가 고정되어 있다. field가 전부 0으로 사라지거나 무한히 커지는 trivial case를 막는다. 총량 $m$ 안에서 field가 어디에 모이고, 어디에서 퍼지고, 어디에서 경계를 만드는지가 문제가 된다.

둘째, 값이 $[0,1]$에 제한된다. 이것은 crisp set indicator로 collapse될 수 있는 가능성을 남기면서도, 처음부터 crisp membership을 요구하지 않는다. $u(x)=0.3$ 같은 값은 모호함이나 noise가 아니라 이론의 primitive graded state다.

셋째, graph $G_t=(X_t,N_t)$가 들어간다. field는 단순히 점마다 독립적인 값이 아니라, neighborhood relation 위에서 closure, boundary, distinction을 형성한다. 두 점의 값이 같아도 graph relation이 다르면 formation의 의미가 달라진다.

### A.3 object는 언제 등장하는가

SCC에서 object는 다음 조건들이 충분히 안정화될 때 등장하는 사후 해석이다.

| 조건 | 직관 | objecthood와의 관계 |
|---|---|---|
| closure | field가 자기 안으로 닫히는 경향 | 내부 응집이 있어야 함 |
| distinction | 주변과 구분되는 contrast | 외부와 달라야 함 |
| boundary | 내부/외부 전이대 | 단순 blob이 아니라 경계가 있어야 함 |
| morphology | shape 또는 structural pattern | 임의의 mass cloud가 아니어야 함 |
| persistence | 시간 또는 parameter 아래 지속 | 순간적 fluctuation이 아니어야 함 |

따라서 SCC의 object는 “있다/없다”의 원시 이분법이 아니다. field가 위 조건들을 어느 정도 만족하는가에 따라 object-like formation의 강도가 달라진다.

이것이 Multi-Formation에서 count 문제가 어려워지는 이유다. object가 원시적으로 주어져 있지 않다면, “몇 개인가”라는 질문도 원시적으로 주어지지 않는다.

---

## 부록 B. 왜 네 개의 $K$를 반드시 분리해야 하는가

본문에서는 네 개의 $K$를 표로 정리했다. 여기서는 왜 이 분리가 피할 수 없었는지 더 자세히 설명한다.

### B.1 $K_{\mathrm{field}}$는 해상도다

$K_{\mathrm{field}}$는 모델이 몇 개의 labelled slot을 허용하는지를 말한다.

$$
\mathbf u=(u^{(1)},\ldots,u^{(K_{\mathrm{field}})}).
$$

이것은 카메라의 해상도나 coordinate chart의 차원에 가깝다. 해상도가 12라고 해서 실제 object가 12개라는 뜻은 아니다. 해상도가 3이면 볼 수 없는 latent variation이 있을 수 있고, 해상도가 12이면 하나의 formation이 여러 slots로 split되어 표현될 수도 있다.

따라서 $K_{\mathrm{field}}$를 object count로 읽으면 theory가 다시 object-first로 퇴행한다.

### B.2 $K_{\mathrm{act}}$는 살아 있는 label 수다

$K_{\mathrm{act}}^\varepsilon$는 mass threshold를 넘는 labelled slot의 수다.

$$
K_{\mathrm{act}}^\varepsilon(\mathbf u)
=
\#\{j:\sum_x u^{(j)}(x)\ge \varepsilon\}.
$$

이 count는 lifecycle을 추적하는 데 유용하다. slot이 birth, activation, weakening, extinction을 겪는지 볼 수 있다. 그러나 이것도 topological object count는 아니다.

WQ-2가 바로 이 점을 보여 주었다. labelled slots는 셋 다 살아 있었지만, aggregate topology는 하나로 합쳐졌다. 즉 $K_{\mathrm{act}}=3$이더라도 field-native morphology는 하나의 dominant component일 수 있다.

### B.3 $K_{\mathrm{bar}}$는 aggregate field의 hard topology다

$K_{\mathrm{bar}}^{\ell_{\min}}$는 label을 보지 않고 aggregate field를 본다.

$$
U=\sum_j u^{(j)}.
$$

그리고 $U$의 superlevel persistent $H_0$ bars 중 길이가 $\ell_{\min}$ 이상인 것들을 센다.

이 count는 field-first ontology와 더 잘 맞는다. 왜냐하면 labelled chart가 아니라 실제 aggregate cohesion morphology를 보기 때문이다. 그러나 hard threshold $\ell_{\min}$가 필요하므로 여전히 regime과 scale 선택이 들어간다.

### B.4 $K_{\mathrm{soft}}$는 부드럽지만 더 위험하다

$K_{\mathrm{soft}}^\phi$는 hard threshold 대신 smooth envelope를 쓴다.

$$
K_{\mathrm{soft}}^\phi(U)=\sum_i\phi(\ell_i(U)).
$$

처음에는 이것이 더 SCC답게 보였다. SCC는 soft field 이론이므로 count도 soft하게 만드는 것이 자연스러워 보였기 때문이다. 그러나 WQ-LAT-1은 default saturating envelope가 reservoir chart refinement 아래 drift할 수 있음을 보여 주었다.

여기서 중요한 교훈은 다음이다.

> smooth하다는 것만으로 좋은 SCC quantity가 되지 않는다.

field-first 이론이라고 해서 모든 smooth observable이 안전한 것은 아니다. 어떤 smooth observable은 chart artifacts에 더 민감할 수 있다. 따라서 $\phi$는 admissible family $\Phi_{\mathrm{res}}$로 제한되어야 한다.

---

## 부록 C. 실패가 정의를 만든 방식

이 이론의 발전 과정에서 실패는 단순한 부정적 결과가 아니었다. 실패는 잘못된 질문을 고쳐 주었다.

### C.1 WQ-1의 F2: 질문이 실행되지 않았다

WQ-1은 OP-0008형 질문을 실험하려 했다. 그러나 OP-0008형 질문이 성립하려면 최소한 labelled $K_{\mathrm{act}}$-jump가 일어나야 한다. 예컨대 다음과 같은 event가 필요했다.

$$
K_{\mathrm{act}}:3\to2.
$$

실제로는 그런 event가 없었다.

$$
K_{\mathrm{act}}:3\to3.
$$

따라서 WQ-1의 실패는 $\sigma$-standard의 충분성에 대한 반례도 아니고, 충분성의 증거도 아니다. 그것은 precondition failure다. 질문을 실행하려 했지만, 질문을 실행시키는 event가 발생하지 않았다.

이 실패가 낳은 교훈은 다음이다.

> labelled lifecycle event와 aggregate morphological event를 구분해야 한다.

### C.2 WQ-2의 F-B6: 같은 상태를 다른 count가 다르게 본다

WQ-2는 WQ-1의 같은 lineage를 aggregate topology로 다시 보았다. 여기서 결정적 분리가 나타났다.

$$
K_{\mathrm{act}}:3\to3,
\qquad
K_{\mathrm{bar}}:3\to1.
$$

이것은 “하나는 맞고 하나는 틀렸다”가 아니다. 두 count가 서로 다른 것을 세고 있다는 뜻이다.

$K_{\mathrm{act}}$는 labelled slot lifecycle을 본다. slot mass가 threshold 아래로 떨어지지 않았으므로 세 slot은 살아 있다.

$K_{\mathrm{bar}}$는 aggregate field의 dominant connected morphology를 본다. 세 slot의 fields가 서로 overlap하거나 bridge를 형성하면 aggregate superlevel topology는 하나의 component처럼 행동할 수 있다.

따라서 F-B6는 다음 정의적 요구를 만들었다.

> resolved regime에서는 두 count가 같아야 한다. unresolved / overlap regime에서는 달라질 수 있다. 그러면 먼저 resolved regime의 equality theorem이 필요하다.

이 요구가 L1 proof chain으로 이어졌다.

### C.3 WQ-LAT-1의 soft failure: 부드러움이 불변성을 보장하지 않는다

reservoir reinterpretation 이후 자연스러운 기대는 $K_{\mathrm{field}}$를 늘려도 field-native quantities가 안정된다는 것이었다. 실제로 hard topology는 안정적이었다. 그런데 default $K_{\mathrm{soft}}$는 drift했다.

이 실패는 soft count를 버리라는 뜻이 아니다. 오히려 soft count를 제대로 정의하라는 뜻이다.

WQ-LAT-1.B는 sharp threshold-like $\phi$들이 chart invariance를 회복한다는 evidence를 주었다. 따라서 soft-count problem은 다음처럼 바뀌었다.

> $K_{\mathrm{soft}}$를 정의할 수 있는가?  
> 가 아니라, 어떤 $\phi$ family가 reservoir-stable한가?

이것이 $\Phi_{\mathrm{res}}$와 L1-M의 이유다.

---

## 부록 D. T-L1-F의 증명 직관

T-L1-F는 복잡한 조건 P0-P11을 갖지만, 증명 직관은 두 방향으로 나눌 수 있다.

### D.1 lower bound: active slot마다 적어도 하나의 bar가 있다

먼저 보여야 하는 것은 다음이다.

$$
K_{\mathrm{bar}}\ge K_{\mathrm{act}}.
$$

이를 위해서는 active slot 하나가 aggregate field $U$ 안에서 충분히 높은 birth를 가진 component를 만들어야 한다. 이것이 P2, P6, P9와 관련된다.

직관은 다음이다.

1. active slot $j$는 충분한 mass를 가진다.
2. 그 support는 connected하게 집중되어 있다.
3. representative peak 또는 birth region이 충분히 높다.
4. aggregate perturbation이 그 peak를 없애지 않는다.
5. 따라서 slot $j$는 적어도 하나의 terminal $H_0$ bar를 만든다.

이 방향은 “slot 하나가 사라지지 않는다”는 주장이다.

### D.2 upper bound: active slot보다 많은 dominant bar는 없다

반대 방향은 더 어렵다.

$$
K_{\mathrm{bar}}\le K_{\mathrm{act}}.
$$

왜 더 어려운가? active slot 하나가 여러 개의 peaks를 만들 수 있고, inactive residual이 fake peak를 만들 수 있고, local에서 작아 보인 secondary bar가 global에서 커질 수 있다는 걱정이 있기 때문이다.

이 문제를 막기 위해 L1-D, L1-E, L1-H2가 필요했다.

- L1-D: active slot 내부 secondary bars를 억제한다.
- L1-E: inactive residual이 dominant bar를 만들지 못하게 한다.
- L1-H2: local에서 억제된 secondary bar가 global에서 더 길어지지 않음을 보인다.

핵심 부등식은 다음이다.

$$
\ell_{\mathrm{global}}\le \ell_{\mathrm{local}}.
$$

이 부등식 덕분에 local secondary-bar suppression이 global overcount 방지로 이전될 수 있다.

### D.3 equality와 bijection

lower bound와 upper bound가 함께 성립하면 count equality가 나온다.

$$
K_{\mathrm{bar}}=K_{\mathrm{act}}.
$$

하지만 T-L1-F는 단순한 숫자 equality만 말하지 않는다. active slots와 dominant terminal bars 사이의 association map도 bijection이라고 말한다.

이 점이 중요하다. 숫자만 같으면 우연히 개수가 같은 것일 수도 있다. bijection은 더 강하다. 각 active slot이 어떤 dominant bar와 대응되는지 추적할 수 있다는 뜻이다. 이것이 resolved regime에서 “ordinary counting이 작동한다”는 정확한 의미다.

---

## 부록 E. L1-M은 무엇을 해야 하는가

L1-M은 아직 standalone theorem file로 존재하지 않는다. 그러나 현재 이론 흐름상 가장 자연스러운 다음 단계다.

T-L1-F는 hard count bridge다.

$$
K_{\mathrm{bar}}^{\ell_{\min}}(U)=K_{\mathrm{act}}^\varepsilon(\mathbf u).
$$

L1-M은 이 위에 soft count를 얹어야 한다.

목표는 다음 형태일 가능성이 높다.

$$
\left|
K_{\mathrm{soft}}^\phi(U)
-
K_{\mathrm{bar}}^{\ell_{\min}}(U)
\right|
\le
\text{controlled error}(\phi,\ell_{\min},\text{bar margins}).
$$

그리고 T-L1-F를 대입하면 다음과 같은 corollary가 된다.

$$
\left|
K_{\mathrm{soft}}^\phi(U)
-
K_{\mathrm{act}}^\varepsilon(\mathbf u)
\right|
\le
\text{controlled error}.
$$

그러나 이것은 arbitrary $\phi$에 대해 성립하면 안 된다. WQ-LAT-1이 이미 default saturating $\phi$의 위험을 보여 주었기 때문이다. 따라서 L1-M의 핵심은 다음이 될 것이다.

1. admissible envelope family $\Phi_{\mathrm{res}}$를 정의한다.
2. dominant bars와 subdominant bars 사이의 margin을 가정한다.
3. $\phi$가 dominant bars에는 거의 1, subthreshold bars에는 거의 0처럼 작동함을 요구한다.
4. 그 결과 soft count가 hard count를 controlled error 안에서 근사함을 보인다.

이 순서가 중요한 이유는, soft count를 너무 빨리 canonical로 올리면 WQ-LAT-1의 실패를 반복하기 때문이다. L1-M은 “soft count도 된다”를 말하는 정리가 아니라, “어떤 soft count만 된다”를 말하는 정리가 되어야 한다.

---

## 부록 F. 2026-05-03 기준 canonical 정의와 정리 상태 전체 정리

이 부록은 현재 canonical layer를 한 번에 읽기 위한 정리표다. authoritative source는 `THEORY/canonical/theorem_status.md`와 `THEORY/canonical/canonical.md`이며, version authority는 `theorem_status.md`의 CV-1.5.2 항목이다. `canonical.md` 상단과 closing summary 일부에는 CV-1.5.1 기준 숫자가 남아 있으므로, 현재 수치와 T-L1-F 지위는 `theorem_status.md`를 우선한다.

현재 canonical headline은 다음이다.

| 항목 | 현재 상태 |
|---|---|
| 현재 canonical version | CV-1.5.2, 2026-05-02 |
| 최신 canonical addition | T-L1-F |
| 총 formal claims | 61 |
| Category A | 46, 그중 T-L1-F는 conditional Cat-A |
| Category B | 5 |
| Category C | 5 |
| Retracted | 5 |
| fully proved 비율 | 약 75% |
| 핵심 non-claim | global $K_{\mathrm{bar}}=K_{\mathrm{act}}$, global $K_{\mathrm{soft}}=K_{\mathrm{act}}$, OP-0005 해결, OP-0008 해결은 모두 주장하지 않음 |

### F.1 canonical primitive / formal universe

canonical SCC의 primitive layer는 다음과 같이 읽으면 된다.

| 항목 | canonical 의미 | 쉬운 설명 |
|---|---|---|
| $T$ | 시간 index 또는 evolution parameter | field가 변하는 축 |
| $X_t$ | relational loci substrate | object들의 집합이 아니라 관계가 놓이는 자리 |
| $u_t:X_t\to[0,1]$ | primitive soft cohesion field | “무엇이 object인가” 이전의 응집 강도 |
| $N_t$ | soft adjacency / neighborhood | 어떤 위치들이 서로 관계를 갖는가 |
| $\mathrm{Cl}_t$ | closure operator | field가 자기 자신을 지지하며 닫히는 경향 |
| $D_t$ | distinction / exterior asymmetry | field가 외부와 얼마나 구분되는가 |
| $M_{t\to s}$ | temporal transport | 시간 사이의 structural inheritance |
| $C_t$ | co-belonging diagnostic | primitive energy/predicate가 아니라 derived diagnostic |

가장 중요한 commitment는 다음이다.

> $u_t$가 primitive이고, crisp object는 derivative다.

즉 canonical SCC는 object set theory가 아니라 field formation theory다.

### F.2 canonical theorem-grade domain

Single-Formation canonical theorem domain은 다음이다.

$$
\Sigma_m(G_t)
=
\{u:X_t\to[0,1]\mid \sum_{x\in X_t}u(x)=m\}.
$$

이 공간의 의미는 다음과 같다.

| 구조 | 역할 |
|---|---|
| $u:X_t\to[0,1]$ | soft field |
| $\sum_x u(x)=m$ | finite cohesive budget |
| $G_t=(X_t,N_t)$ | relation graph |
| compactness | existence theorem의 기반 |
| no object label | field-first ontology 보존 |

Multi-Formation canonical / working interface는 현재 다음 기호들을 사용한다.

| 공간 / 기호 | 상태 | 의미 |
|---|---|---|
| $\widetilde{\Sigma}^{K_{\mathrm{field}}}_M(G_t)$ | canonical T-L1-F와 working MF에서 사용 | shared-pool finite K-field state space |
| $K_{\mathrm{field}}$ | Commitment 16 canonical | architectural cap / modelling-layer commitment |
| $K_{\mathrm{act}}^\varepsilon$ | Commitment 16 + T-L1-F canonical | active labelled slot count |
| $U=\sum_j u^{(j)}$ | T-L1-F canonical | aggregate field |
| $K_{\mathrm{bar}}^{\ell_{\min}}(U;G)$ | T-L1-F canonical | aggregate hard-bar count |
| $K_{\mathrm{soft}}^\phi$ | working / pre-canonical for MF bridge | soft persistence-weighted count; L1-M 대상 |

### F.3 derived geometric and morphological notions

canonical SCC는 primitive field로부터 다음 derived geometry를 만든다.

| notion | canonical form | 의미 |
|---|---|---|
| Core | $\mathrm{Core}_t(u_t)=\{x:u_t(x)\ge\theta_{\mathrm{core}}\}$ | 강하게 응집된 핵 |
| Interior | $\mathrm{Int}_t(u_t)=\{x:u_t(x)\ge\theta_{\mathrm{in}}\}$ | core를 포함하는 내부 영역 |
| Boundary band | $\mathrm{Bd}_t(u_t)=\{x:\theta_1<u_t(x)<\theta_2\}$ | sharp line이 아니라 transition band |
| Exterior | $\mathrm{Ext}_t(u_t)=\{x:u_t(x)\le\theta_{\mathrm{ext}}\}$ | distinction을 측정하는 외부 |
| gradient indicator | $g_t(x;u)=\sum_y N_t(x,y)|u_t(x)-u_t(y)|$ | boundary / transition intensity |
| morphology quality | $\mathcal Q_{\mathrm{morph}}$ | persistence-based morphology diagnostic |

쉬운 말로 하면, canonical SCC는 “object boundary”를 선으로 먼저 긋지 않는다. field의 core, interior, boundary band, exterior가 먼저 정의되고, object-like boundary는 그 뒤의 해석이다.

### F.4 axiom groups

canonical axioms는 다섯 그룹으로 정리된다.

| 그룹 | 이름 | 무엇을 통제하는가 | 핵심 의미 |
|---|---|---|---|
| A | Soft Closure | $\mathrm{Cl}_t$ | field가 자기 자신을 지지하고 안정화되는 방식 |
| B | Soft Adjacency | $N_t$ / relation kernel | 어떤 loci가 서로 관계를 갖는가 |
| C | Soft Co-belonging | $C_t$ diagnostic | non-local integration의 분석 도구 |
| D | Distinction | $D_t$ | 외부와의 asymmetry / separation |
| E | Temporal Transport and Persistence | $M_{t\to s}$ | 시간이 지나도 같은 formation이라고 말할 조건 |

특히 Group A의 closure commitment는 중요하다. canonical SCC는 closure를 idempotent projection으로 두지 않는다. closure는 contraction / stabilization tendency다.

| closure axiom | 의미 |
|---|---|
| A1' conditional extensivity | $u(x)$가 self-support threshold 아래이고 local aggregation이 지지할 때 closure가 값을 키움 |
| A2 monotonicity | 더 큰 field의 closure는 더 작아지지 않음 |
| A3 stabilization / contraction | $a_{\mathrm{cl}}<4$에서 반복 closure가 fixed point로 수렴 |
| A4 continuity | closure operator는 continuous |

이것은 “object를 한 번에 닫힌 집합으로 만드는” 이론이 아니라, “field가 점진적으로 self-support를 형성하는” 이론이라는 뜻이다.

### F.5 fixed commitments

canonical fixed commitments는 이론의 해석을 제한하는 meta-theoretical commitments다. 아래 표는 현재 문서에서 필요한 수준으로 전체를 요약한 것이다.

| 번호 | commitment | 요약 |
|---|---|---|
| 1 | Primacy of soft cohesion fields | primitive는 $u_t:X_t\to[0,1]$ |
| 2 | Relational priority | object보다 relation이 먼저 |
| 3 | Non-primitive crisp objects | crisp object는 threshold/stabilization 이후의 derivative |
| 4 | Non-primitive idempotence | closure는 primitive idempotent projection이 아님 |
| 5 | Four-term minimal energy | closure, separation, boundary/morphology, transport term은 구분되어야 함 |
| 6 | Structural persistence | temporal identity는 pointwise sameness가 아니라 structural core inheritance |
| 7 | Boundary as transition band | boundary는 sharp frontier가 아니라 graded band |
| 8 | Distinction as exterior asymmetry | distinction은 local contrast가 아니라 exterior field와의 asymmetry |
| 9 | Volume constraint | finite cohesive budget은 구조적 axiom |
| 10 | A1' conditional extensivity | closure는 self-regulating |
| 11 | Diagnostic vector primary | proto-cohesion은 Boolean이 아니라 $[0,1]^4$ vector |
| 12 | $C_t$ derived diagnostic | co-belonging은 energy/predicate primitive가 아님 |
| 13 | $b_D=0$ | analyticity와 T14 convergence를 위해 distinction operator의 gradient term 제거 |
| 14 | Orbital character constitutive | $\sigma$-signature는 analogy가 아니라 formation character의 일부 |
| 15 | Pre-objective commitment theorem-grounded | pre-objective claim은 T-PreObj-1/T-PreObj-1G로 theorem-grounded |
| 16 | K-status two-tier decomposition | $K_{\mathrm{field}}$는 cap, $K_{\mathrm{act}}$는 derived active count |

Commitment 16은 Multi-Formation의 해석에서 특히 중요하다.

$$
K_{\mathrm{act}}(t)\le K_{\mathrm{field}}.
$$

$K_{\mathrm{field}}$는 모델이 허용한 slot 수이고, $K_{\mathrm{act}}$는 그중 실제 active한 slot 수다. CN6의 “K is kinetically determined”는 CV-1.5.1 이후 $K_{\mathrm{act}}$에 관한 말로 refined되었다.

### F.6 canonical theorem registry: Category A

아래 표는 현재 canonical Category A의 핵심 항목들을 기능별로 정리한 것이다. 원문 registry는 theorem ID별로 길게 서술되어 있으므로, 여기서는 “현재 이 이론이 무엇을 증명한 상태인가”를 읽기 쉽게 재배열한다.

| theorem / family | canonical 상태 | 무엇을 보장하는가 |
|---|---|---|
| T1 Energy Minimizer Existence | Cat A | $\Sigma_m$ 위에서 energy minimizer 존재 |
| T6a Closure Fixed Point Existence | Cat A | closure fixed point 존재 |
| T6b Closure Fixed Point Uniqueness | Cat A in contraction regime | $a_{\mathrm{cl}}<4$에서 unique fixed point와 geometric convergence |
| T20 Axiom Consistency | Cat A | sigmoid closure가 A1', A2, A3, A4를 만족 |
| T-A2 Monotonicity | Cat A | $u\le v\Rightarrow \mathrm{Cl}(u)\le\mathrm{Cl}(v)$ |
| T8-Core | Cat A | spectral phase condition 아래 non-uniform minimizer 존재 |
| T8-Full | Cat A | full energy perturbation 아래 non-trivial minimizer 유지 |
| T14 Gradient Flow | Cat A | projected gradient flow가 critical point로 수렴 |
| T3/T6-Stability | Cat A | non-idempotent closure fixed point가 stability advantage를 가짐 |
| T7-Enhanced | Cat A | closure correction이 local Hessian curvature를 강화 |
| T11 $\Gamma$-Convergence | Cat A | sharp-interface limit에서 perimeter functional로 수렴 |
| C-Axioms | Cat A | co-belonging resolvent realization이 C axioms 만족 |
| QM1-4 | Cat A | normalized $\mathcal Q_{\mathrm{morph}}$가 morphology axioms 만족 |
| Predicate-Energy Bridge | Cat A | energy minimization과 diagnostic alignment 연결 |
| Deep Core Dominance 2b | Cat A | deep core dominance bound |
| T-Merge (a) | Cat A | well-separated K-formations are local minima on $\Sigma_M^K$ |
| T-Merge (b) | Cat A | pure boundary-energy layer에서 K=1 energy ordering |
| Topological Lock | Cat A but vacuous as barrier | $\Sigma_M^K$에서는 merge endpoint가 domain 밖 |
| T-PreObj-1 | Cat A | full SCC에서 $F=1$ single-disk non-criticality와 multi-peak attractor |
| T-PreObj-1G | Cat A | pre-objective mechanism의 finite connected graph generality |
| F-1 Resolution Corollary | Cat A corollary | F-1 split-resolved via T-Merge(b) + T-PreObj-1 |
| T-V5b-T | Cat A | translation-invariant graph에서 pre-objective Goldstone structure |
| T-σ-Lemma-1 | Cat A | $\sigma$ irrep decomposition well-defined |
| T-σ-Lemma-2 | Cat A plus C riders | nodal count properties; 일부 subclaim은 conditional |
| T-σ-Lemma-3 | Cat A in continuum | Goldstone–$\ell=1$ angular saturation |
| T-σ-Theorem-3 | Cat A | uniform $D_4$ grid에서 $\sigma$ closed form |
| T-Commitment-14-Multi-Static | Cat A definitional | static Multi-Formation $\sigma_{\mathrm{multi}}$ 정의 |
| T-σ-multi-A-Static | Cat A well-separated | within-formation $\sigma$ tuple multiset invariance |
| T-σ-multi-D-Static | Cat A definitional | between-formation cohomology pull-back |
| V5b-T-zero | Cat A definitional | sub-spinodal translation-invariant regime의 zero Goldstone mass |
| T-L1-F | Cat A conditional | P0-P11 아래 $K_{\mathrm{bar}}=K_{\mathrm{act}}$와 bar-slot bijection |

주의할 점은 T-L1-F가 Category A이지만 “conditional Cat-A”라는 점이다. 이것은 proof가 약하다는 뜻이 아니라, theorem statement 자체가 P0-P11 regime theorem이라는 뜻이다.

### F.7 Category B / Category C / tentative / retracted

Category B와 C는 실패가 아니라 정확한 status control이다. canonical registry는 어떤 결과가 fully proved인지, structural parameter에 의존하는지, regime condition에 의존하는지를 분리한다.

| 항목 | 상태 | 의미 |
|---|---|---|
| T-Bind-Proj | Category B | $\tau=1/2$ 등 explicit structural condition 아래 bind projection |
| $\gamma_{\mathrm{eff}}\approx0.89$ barrier exponent | Category B | empirical / branch-conditioned barrier exponent |
| general-graph birth supercriticality | Category B | narrow-gap / non-$D_4$ cases에서 structural parameter 의존 |
| $d_{\min}$ formula | Category B | branch-conditioned regression fit |
| Beyond-Weyl quantification | Category B | grid/branch-specific improvement factor |
| T-σ-Theorem-4 | downgraded to Category B in $\epsilon$-small regime | first pitchfork $\sigma$ leading-order statement은 critic 이후 격하 |
| T-σ-Multi-1 | tentative / B target | Multi-Formation Goldstone-pair instability candidate |
| V5b-F empirical | B target | boundary-modified graph partial Goldstone mass scaling |
| T-Bind-Full | Category C | general $\tau$ dependence conditional |
| T-Persist-1(a) | Category C in v1.2 table / component-level proved | minimizer persistence via IFT; composition status 유의 |
| T-Persist-1(d) | Category C | exact threshold preservation은 structural condition 필요 |
| T-Persist-Full | Category C | full persistence composition은 multiple regime conditions 필요 |
| T-Persist-K-Sep | Category C | well-separated + spectral-repulsion hypotheses |
| T-Persist-K-Weak | Category C | weakly interacting regime hypotheses |
| T-Persist-K-Unified | Category C | selected branch + five structural hypotheses |

Retracted claims는 다음과 같다.

| retracted item | 왜 retracted 되었는가 |
|---|---|
| Theorem 3.3 general $\tau$ | general $\tau$에서 $\bar r_0=O(n^{-1/d})$ claim falsified |
| T-Merge (c) | merge endpoint가 $\Sigma_M^K$ domain 밖이라 Mountain Pass path 없음 |
| T-Merge (d) | T-Merge (c)에 의존 |
| T-Merge (e) | T-Merge (c)에 의존 |
| K-Saddle Conjecture | 이전에 retracted |

이 retraction들은 이론의 약점만을 의미하지 않는다. 오히려 domain을 잘못 잡으면 그럴듯한 theorem이 무효가 된다는 중요한 교훈을 남겼다. 이 교훈이 나중에 Layer I / II / III architecture의 필요성과 직접 연결된다.

### F.8 현재 canonical open problems

현재 open problems registry는 다음처럼 읽을 수 있다.

| OP | 상태 | 의미 |
|---|---|---|
| OP-0001 F-1 | split-resolved | pure $E_{\mathrm{bd}}$는 T-Merge(b), full SCC는 T-PreObj-1로 분리 해결 |
| OP-0002 M-1 | layer-clarified | “K=1 preference”는 pure layer theorem을 full SCC 문제로 오독한 것 |
| OP-0003 MO-1 | sidestepped / conditional reactivation | single-field $\Sigma_m$에서는 sidestepped; Multi-Formation stratified Morse로 재활성 가능 |
| OP-0004 Type A/B Classification | high / retracted classification | Type A/B classification invalidated |
| OP-0005 K Selection Mechanism | open | $K_{\mathrm{field}}$ selection / effective rank mechanism 미해결 |
| OP-0006 Boundary Definition Precision | high | boundary definition precision 문제 |
| OP-0008 $\sigma^A$ K-jump inheritance | open / tentative | K-jump 이후 $\sigma$ inheritance non-determinism 미해결 |
| OP-0009 Multi-Formation Ontological Foundations | partially addressed | K-status만 Commitment 16으로 resolved; 나머지 subitems partially addressed |
| OP-0010 Bind Generalization | medium | bind generalization |
| OP-0011 Transport Kernel Uniqueness | medium | transport kernel uniqueness |
| OP-0012 Persistence Composition | medium | persistence composition |
| OP-0013 Closure Operator Convergence Rate | medium | closure convergence rate |
| OP-0020 Dynamic Topology | low / out of scope | dynamic topology |
| OP-0021 Stochastic Dynamics | low | stochastic dynamics |
| OP-0022 Continuous-Time Limit | low | continuous-time limit |

현재 Multi-Formation 문맥에서 가장 중요한 open trio는 다음이다.

1. OP-0005: $K_{\mathrm{field}}$는 어떻게 선택되는가?
2. OP-0008: K-jump 이후 $\sigma$ inheritance는 무엇으로 결정되는가?
3. OP-0009: Multi-Formation ontology는 Commitment 16 이후에도 무엇이 남았는가?

T-L1-F는 이 셋을 해결하지 않는다. 대신 이 셋을 다루기 위한 resolved-count baseline을 제공한다.

### F.9 canonical status를 읽는 법

이론을 읽을 때 가장 중요한 습관은 “증명됨”이라는 말을 하나로 읽지 않는 것이다.

| 표현 | 읽는 법 |
|---|---|
| Cat A | theorem statement가 명시한 domain에서 fully proved |
| Cat A definitional | 정의나 invariant가 well-defined임이 증명/확정됨 |
| Cat A conditional | 조건부 theorem 자체가 fully proved; 조건이 빠지면 주장하지 않음 |
| Cat B | structural parameter, empirical fit, branch condition, limited quantification이 있음 |
| Cat C | regime hypotheses가 본질적이고 제거되지 않음 |
| tentative / B target | working direction이나 partial evidence가 있으나 canonical proof 아님 |
| retracted | 현재 이론에서 사용하면 안 됨 |
| open | 해결되지 않음 |
| partially addressed | 일부 subproblem만 닫힘 |

따라서 T-L1-F는 다음처럼 읽어야 한다.

> “$K_{\mathrm{bar}}=K_{\mathrm{act}}$가 항상 참이다”가 아니라,  
> “P0-P11 resolved regime에서는 $K_{\mathrm{bar}}=K_{\mathrm{act}}$가 theorem-grade로 참이다.”

이것이 canonical status를 정확히 읽는 방식이다.
