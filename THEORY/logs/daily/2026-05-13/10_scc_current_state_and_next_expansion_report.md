> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]

# Soft Cognitive Cohesion(SCC) 이론 — 현황 분석 및 다음 확장 설계 보고서

**기준 버전:** CV-1.13 (2026-05-10 봉인, W7-CV1.13 UltraQA 종료감사 직후)
**작성일 기준:** 2026-05-13
**카운트:** 59 Cat A / 14 Cat B / 5 Cat C / 5 Retracted = **83 claims (~71% 완전 증명)**

---

## 0. 이 보고서를 읽는 법

이 이론은 “사람이 사과를 보기 전에, 시야 안에서 어떤 ‘무엇인가의 덩어리’가 먼저 생기는 순간”을 수학화한다. 곧, **객체가 먼저 있고 인식이 따라오는 것이 아니라**, 인식이 진행되는 동안 점차 객체 후보가 응결되어 나온다는 관점이다.

비유 한 줄로 요약하면 — **시야는 안개로 시작하고, 안개 어느 부분이 갑자기 진해져 “여기 무언가 있다”고 말할 수 있게 되는 순간**, 그 순간을 수학적으로 잡으려는 이론이다.

---

## 1. 이론의 발전 흐름 (맥락 복원)

### 1.1 최초 문제의식 — “왜 응집이 먼저인가?”

**비유부터.** 우리가 책상 위에 놓인 사과를 “인식한다”고 말할 때, 실제로는 다음과 같은 일이 일어난다:

1. 시야의 어느 부분에 빨간색이 모여 있다.
2. 그 빨간색 무리에 둥근 윤곽이 있다.
3. 그 둥근 윤곽 안쪽이 바깥쪽과 다르게 행동한다.
4. 그 덩어리가 시간이 지나도 흩어지지 않는다.
5. **그 덩어리가 “하나의 무언가”로 굳어진다.** ← 여기까지가 SCC가 다루는 구간
6. 거기에 “사과”라는 이름이 붙는다. ← SCC 범위 밖

기존 인식 이론들이 가지는 한계는 대부분 **5번 이전 단계를 건너뛴다**는 것이다.

- **객체 검출(object detection):** 객체가 이미 존재한다고 가정하고 어디 있는지를 찾는다. “이미 만들어진 것 중 하나”라는 전제가 깔린다.
- **Segmentation:** 픽셀을 어느 분할에 속한다고 라벨링한다. 라벨이 미리 있다.
- **Gestalt 법칙:** 응집의 “결과 패턴”(근접·유사·연속·폐쇄)을 기술하지만, **응집의 발생 메커니즘 자체를 식별하지는 않는다**.
- **Bayesian / Predictive Processing:** 객체 후보의 사전분포가 이미 정의되어 있다. 사전분포 자체가 어디서 오는지는 묻지 않는다.

SCC는 이 모든 접근이 “이미 만들어진 객체를 다루는 일”이지, **“객체가 만들어지는 일”을 다루는 일이 아니라고 본다.** 만들어지기 직전 단계 — 즉 “경계가 칼로 자른 선이 아니라 안개처럼 번지는 단계” — 를 SCC는 **pre-objective cohesion**이라 부른다.

**근거 파일:** `THEORY/canonical/DECLARATION.md` (DECL-1.0); `canonical.md §2 Foundational Orientation`.

### 1.2 초기 공리계 (crisp 단계의 흔적)

비유: 처음에는 시야를 “점들의 집합”이라고 보고, 어느 점이 어느 점과 손을 잡는지, 어느 점이 어느 무리에 속하는지, 어느 무리가 시간이 지나도 같은 무리인지를 “집합 멤버십”과 “관계 술어”로만 기술하려 했다.

이 초기 단계에서 다음 객체들이 등장한다.

| 기호 | 비유 | 수학적 의미 |
|---|---|---|
| $X_t$ | 사진을 확대하면 보이는 작은 픽셀 세계 | 시각 $t$의 감각 요소 집합 |
| $R_t$ | 점들 사이의 “관계 그물망” | 일반 관계 구조 |
| $\mathrm{Cl}_t$ | 흩어진 점들이 “서로를 지지해서 덩어리로 닫혀가는” 작용 | closure operator |
| $\mathbf{N}_t$ | “가까운 사람끼리 손을 잡을 수 있다” | 인접성 kernel |
| $\mathbf{C}_t$ | “같은 동네에 속한다는 느낌” | co-belonging |
| $\mathbf{D}_t$ | “나는 바깥과 얼마나 다르게 서 있나” | distinction |
| $\mathbf{M}_{t\to s}$ | 어제와 오늘을 잇는 다리 | 시간 transport |
| Bind / Sep / Inside / Persist | “단단한가 / 분리되었나 / 안인가 / 이어졌나”의 네 가지 통과 시험 | proto-cohesion 진단 벡터 |

**이 단계의 한계.** crisp(딱 자른) 집합 $A \subseteq X_t$ 만으로는 “경계가 안개처럼 번지는 구간”, “중간 정도로만 속하는 점”, “closure가 부분적으로만 일어난 상태” 같은 **객체화 직전의 회색지대**를 표현할 수 없다. 종이가 칼로 자르듯이 잘리면, “물감이 번진 띠”를 그릴 수가 없다.

**근거:** `canonical.md §3 Formal Universe`, `§4 Why the Soft Form Is Primary`.

### 1.3 soft field로의 전환 — 안개로서의 응집장

**비유.** 시야 위에 “끈적한 응집 안개”가 깔려 있다고 상상하자. 각 위치마다 그 안개의 진하기가 0(없음)과 1(꽉 참) 사이의 값을 가진다. 이 진하기가 곧 **응집 참여 강도** $u_t(x)$이다.

$$u_t : X_t \to [0,1]$$

핵심은 다음 세 가지다.

1. **0/1 이분법 폐기.** 안개의 중간 진하기가 본질이다. 0.7은 그냥 “0.7의 가능성”이 아니라 **0.7만큼 응집에 참여하고 있는 실제 상태**다.
2. **객체는 출력이지 입력이 아니다.** 객체는 안개의 에너지 최솟값 구조에서 사후적으로 출현한다.
3. **crisp는 soft에서 잘라낼 수 있지만, 그 반대는 안 된다.** $A_t = \{x : u_t(x) \ge \theta\}$로 thresholding하면 crisp 집합을 얻는다. 반대로 crisp에서 soft를 복원할 수는 없다.

여기서 새로운 유도 개념들이 생긴다.

| 개념 | 비유 | 수학적 의미 |
|---|---|---|
| **Core** ($u \ge \theta_{\mathrm{core}}$) | 안개의 가장 진한 핵 | 깊은 내부 |
| **Interior** ($u \ge \theta_{\mathrm{in}}$) | 안개가 어느 정도 진한 영역 | 내부 |
| **Boundary band** ($\theta_1 < u < \theta_2$) | **물감이 번진 띠** | 전이 구간 (선이 아니라 두꺼운 띠) |
| **Exterior** ($u \le \theta_{\mathrm{ext}}$) | 안개가 거의 없는 바깥 | 외부 |

**근거:** `canonical.md §3.3, §4, §5.1–§5.5`.

### 1.4 self-referential energy — 안개를 평가하는 네 가지 시험

**왜 공리만으로는 부족했는가.** 공리는 “closure가 이런 성질을 가져야 한다”는 정합성만 보장한다. 그러나 “어떤 안개 패턴이 좋은 응집인지”에 대한 **선호 구조(preference)** 가 없다. 그래서 에너지 함수가 필요하다.

SCC의 에너지는 네 항으로 구성된다 — **개념적으로 독립이며 합쳐서는 안 된다**:

$$E = \lambda_{\mathrm{cl}} E_{\mathrm{cl}} + \lambda_{\mathrm{sep}} E_{\mathrm{sep}} + \lambda_{\mathrm{bd}} E_{\mathrm{bd}} + \lambda_{\mathrm{tr}} E_{\mathrm{tr}}$$

**네 시험지 비유.** 이 에너지는 안개 덩어리에게 주는 네 가지 시험지와 같다:

| 시험 | 비유 | 수식 의미 |
|---|---|---|
| **$E_{\mathrm{cl}}$ Closure** | “너는 너 스스로를 지지하니?” — 너 자신의 closure 연산 결과와 너는 얼마나 일치하니? | $\lVert u - \mathrm{Cl}(u) \rVert^2$ 류 |
| **$E_{\mathrm{sep}}$ Separation** | “너는 배경과 충분히 다르니?” | $u$-weighted distinction의 부족분 |
| **$E_{\mathrm{bd}}$ Boundary** | “너의 모양이 너무 거칠지 않고, 핵-경계-외부의 매끄러운 전이가 있니?” | $\alpha\,u^\top L u + \beta\,W(u)$ (Allen–Cahn형) |
| **$E_{\mathrm{tr}}$ Transport** | “시간이 지나도 너의 핵이 이어지니?” | 시간 transport 비용 |

이 네 시험지가 **모두 동시에 잘 통과되는 안개**가 곧 “하나의 객체로 굳어진 형성”이 된다. 다만 이 시험들은 서로 다른 차원의 잘못을 잡아내므로, **합치면 안 된다**(CN5: 4-term independence).

핵심은 “self-referential”이라는 단어다 — 덩어리는 자기 자신이 만든 기준 $\mathrm{Cl}(u)$, $1-u$ 같은 self-induced 외부 등으로 **자기 자신을 평가**한다. 이것이 사전 라벨이나 외부 사전분포 없이 응집이 자생적으로 굳어지게 만드는 메커니즘이다.

**근거:** `canonical.md §7–§9`.

### 1.5 구체 연산자 선택의 진화

비유로 정리하면 “**연장통을 고르는 과정**”이다. 같은 closure라도 종류가 여러 가지인데, 그 중 어느 것을 쓰면 이론이 잘 닫히는지를 반복적으로 골라낸 흔적이다.

- **$\mathrm{Cl}_t$ (closure)** → **sigmoid closure**로 선택. 이유: A1′(Conditional Extensivity, $u(x) \le c^*$에서만 강한 자기지지)과 A3(contraction, $a_{\mathrm{cl}} < 4$, 기하적 수렴)이 동시에 성립한다. **idempotent가 아니다** — 즉 “두 번 적용해도 같다”가 아니라 “여러 번 적용하면 부드럽게 안정화된다”. 이것이 핵심 신호 commitment.
- **$\mathbf{D}_t$ (distinction)** → **외부장 $1-u$에 대한 sigmoid 평가**. 자기 자신의 상대 위치를 정의해 외부 대조를 self-induce.
- **$\mathbf{C}_t$ (co-belonging)** → **resolvent** $(I - \alpha W_{\mathrm{sym}})^{-1}$. 비유: 도시 도로망을 따라 “같은 공동체에 속한 정도”를 멀리까지 전파시키는 함수. **Cesàro형은 폐기됨** — pairwise preservation이 무너짐.
- **$\mathbf{M}_{t\to s}$ (transport)** → 함수가 아니라 **entropic partial OT kernel**. 어제의 핵과 오늘의 핵을 일대다, 다대일, 부분적으로 잇는 유연한 다리. 또한 **C_t는 더 이상 정식 universe 멤버가 아니다** — Sep 술어를 $u$-weighted로 고친 뒤 C_t의 유일한 정식 역할이 사라져 v2.0에서 derived diagnostic으로 강등됨.

**근거:** `canonical.md §3, §6, §9, §6 Group A–E`.

---

## 2. proof / audit / canonical correction 흐름

이론은 매주 자기 자신을 감사해서 잘못된 가지를 retract하거나 강등시켰다. 중요한 사건들:

### 2.1 A1과 A3의 충돌 → A1′로 수정

비유: 건물을 짓고 보니 기둥 둘이 같은 자리를 점유하고 있었다. A1(weak extensivity)은 $u(x) = 0.9$에서도 $\mathrm{Cl}(u)(x) \ge u(x)$를 요구하는데, sigmoid에서 이것을 만족시키려면 $a_{\mathrm{cl}} \ge 5.49$가 필요하다. 그런데 A3(contraction)은 $a_{\mathrm{cl}} < 4$를 요구한다. **양립 불가**.

해법: A1을 **conditional extensivity A1′**로 약화. “$u(x) \le c^*$ (self-support threshold) 아래에서만” 강한 closure 작용을 요구. 위에서는 closure가 **상쇄·교정 작용**을 한다(self-regulation). 이로써 A1′는 A1보다 강한 동시에 A3과 정합한다.

### 2.2 Volume constraint $\sum u = m$의 의무화

비유: 비행기를 띄우려면 양력만 있어선 안 되고 활주로(베이스)가 있어야 한다. 변분 문제 $\min E(u)$가 자명한 답($u\equiv 0$ 등)으로 무너지지 않도록 만들기 위해 **질량 보존 제약**이 구조 공리로 승격됨. 이로써 작동 공간이 simplex $\Sigma_m$로 고정.

### 2.3 Q_morph / Inside 정의 문제

원래의 $\mathcal{Q}_{\mathrm{morph}} = \ell_{\max} \cdot \mathrm{Artic}$는 균일장에서도 0이 되지 않는 버그가 있었다. **normalized form** $\mathcal{Q} = (\ell_{\max} - c)/(1-c) \cdot \mathrm{Artic}$로 교정 (QM1 axiom satisfaction).

### 2.4 T8 / 위상전이 — **이론의 심장**

$$\frac{\beta}{\alpha} > \frac{4\lambda_2}{\lvert W''(c) \rvert}$$

비유로 한 줄 — **시야의 해상도가 충분히 높을 때만 두 사물이 둘로 보인다**. 멀어서 $\lambda_2$(스펙트럼 간격, 즉 해상도)가 작아지면 두 사과가 하나로 융합되어 보인다. 이것은 오류가 아니라 **그 해상도에서의 유효한 인식**.

여기서 **2λ₂ vs 4λ₂ 혼선** 사건이 있었다. 원인은 합 표기 관행 — ordered pair vs unordered pair. canonical.md §0의 **summation convention**(모든 합은 ordered pair)을 명시함으로써 해소되어 현재 **4λ₂가 정답**.

### 2.5 비-idempotent closure의 안정성 이점

증명됨(T3 / T6-Stability, Cat A): 비-idempotent fixed point에서 closure Hessian $2(I-J_{\mathrm{Cl}})^\top(I-J_{\mathrm{Cl}})$는 **strictly positive definite** ($n/n$ 양의 고유값). idempotent였다면 range 방향에서 영고유값이 생겨 약함. 즉 idempotence를 “포기”한 결과 **더 강한** 안정성이 나옴.

### 2.6 Gradient flow convergence — T14 Cat A

$\dot u = -\Pi_{\Sigma_m}\nabla E(u)$. analytic energy + compact constraint → Łojasiewicz inequality로 critical point 수렴 보장. $b_D = 0$ 또는 ε-smoothing이 analyticity의 전제.

### 2.7 Γ-convergence — T11 Cat A

$\varepsilon = \alpha/\beta \to 0$일 때 $E_{\mathrm{bd}}$가 perimeter functional로 Γ-수렴. 즉 “안개 띠”가 “sharp interface”로 수렴. 단, **self-referential correction term이 effective surface tension을 수정**하므로 Allen–Cahn의 그대로가 아님.

### 2.8 Sep/Bind bridge — Cat A (Predicate-Energy Bridge)

$\mathsf{Sep} = 1 - E_{\mathrm{sep}}/m$ (정확한 양방향 등식, $u$-weighted Sep에서 성립). $\mathsf{Bind} \ge 1 - \sqrt{E_{\mathrm{cl}}/n}$ (정방향), 최소점에서는 KKT를 통한 역방향. 둘 다 Cat A로 격상됨.

### 2.9 C_t 관련 — 정식 universe에서 강등

Sep을 $u$-weighted로 고친 후 C_t는 어느 술어·에너지에도 들어가지 않게 됨. 그래서 v2.0 cycle 2에서 **derived diagnostic으로 강등**. 여전히 진단 도구로는 쓰임. 공리 C1–C5는 well-defined 상태로 남아 있음.

### 2.10 시간 정리 — 일찍 주장되었다가 강등되었던 부분

원래는 “temporal theorem proved”라거나 “Brouwer로 self-referential OT가 완전 해결됨” 같은 주장이 있었다. **모두 강등됨**. 진짜 해결은 W7에 다음 형태로 이루어졌다:
- **H-SINK** (Sinkhorn-Lipschitz 안정성) **Cat A 완전 종료** (W7-FINAL, 2026-05-10).
- **Theorem Partial-H-SINK** Cat A — SCC E1이 one-sided row-normalized이라는 사실을 이용해 row-softmax Lipschitz로 직접 증명. Séjourné 등의 unbalanced OT 결과가 **필요 없게** 됨.
- **T-Temporal-Identity (a,b,c,d) 전 파트 Cat A** (W7-CV1.13, 2026-05-10). 단 (c)는 conditional — margin condition $\Delta_{\mathrm{sep}} \ge \Delta_{\mathrm{sep}}^* + 2\epsilon_{\mathrm{kernel}}$ 하. (이 보고서 작성 시점에 막 봉인된 결과.)

**근거:** `canonical/CV-1.13_SEAL.md`, `CHANGELOG.md 2026-05-10 (W7-CV1.13)`.

---

## 3. 현재 현황 판정 (CV-1.13 기준, 4구획)

전체 통계: **59A / 14B / 5C / 5R = 83 claims, ~71% fully proved.**

### 3.1 확정된 핵심 (Cat A — “이미 단단한 기둥”)

| 항목 | 쉬운 설명 | 수학적 의미 | 근거 |
|---|---|---|---|
| **정적 single-formation SCC core** | 안개가 하나의 덩어리로 굳어지는 메커니즘 전반 | T1(존재), T-A2(monotone), T14(수렴), T11(Γ-수렴), T20(공리 정합성) | canonical §13 Cat A |
| **Volume-constrained variational backbone** | $\Sigma_m$ 위의 에너지 최소화 골격 | $E$ analytic on $\Sigma_m$, $\Pi_{\Sigma_m}$ projection | §7–§9 |
| **Non-idempotent closure 안정성** | closure를 idempotent로 두지 않은 덕분에 안정성이 더 강해짐 | $2(I-J_{\mathrm{Cl}})^\top(I-J_{\mathrm{Cl}}) \succ 0$ | T3/T6-Stability |
| **T8-Core / T8-Full 위상전이** | 해상도가 충분할 때만 경계가 출현 | $\beta/\alpha > 4\lambda_2/\lvert W''(c) \rvert$ | T8-Core/Full Cat A |
| **Gradient flow convergence** | 경사하강이 임계점에 안전하게 도달 | Łojasiewicz–Simon | T14 |
| **Diagnostic vector 계산 가능성** | (Bind, Sep, Inside, Persist)을 실제로 계산할 수 있음 | Predicate-Energy Bridge Cat A | T-Bind-Proj/Full |
| **Deep Core Dominance 2b** | 핵 안의 핵이 이만큼 크다는 isoperimetric 부등식 | $\vert {\rm Core}^2\vert /\vert {\rm Core}\vert \ge 1 - 4C/\sqrt m$ | canonical §13 |
| **T-OP6-B Persistent Gradient Ridge Boundary** | 경계가 “물감 띠”이지만 그 띠와 위상적 경계의 거리는 $\le 2\sqrt{\alpha/\beta}$ | $d_H \le 2(\alpha/\beta)^{1/2}$, H1–H5 하 | T-OP6-B (Session K) |
| **σ-framework supporting (Lemma 1/2/3, Theorem 3)** | 응집 핵심에 어떤 “지문(signature)” 구조가 있는지에 대한 표준 토대 | irrep decomposition + nodal count + Goldstone-ℓ=1 | T-σ-Lemma-1/2/3, T-σ-Theorem-3 |
| **P-F-A1 Package I 완전 Cat A** | 잡음 속에서 안개가 어떻게 흐르고 어떤 분포에 도달하는지 | reflected Langevin SDE on polytope + Gibbs 유일 불변 + Poincaré ergodic | T-PF-A1-AR / SDE / GI / PE |
| **T-L1-F, T-L1-M (multi-formation Cat A conditional)** | K-field slot 카운트와 persistent bar 카운트가 같다는 다리 | $(P0)$–$(P11)$ 하에서 $K_{\mathrm{bar}}=K_{\mathrm{act}}$ | W5–W6 |
| **T-Temporal-Identity (a,b,c,d) — NEW Cat A** | 어제의 덩어리와 오늘의 덩어리를 잇는 정체성 대응이 존재·유일·kernel-독립 | partial OT + score matrix + margin condition | CV-1.13 SEALED |
| **Stereo extension (T-ST-5a Cat A)** | 깊이가 다른 두 영역은 topologically locked | 비연결 그래프 → K=2 강제 | CV-1.6 |
| **OMS-2.0 Accepted Full** | 관측자 구성공간을 한 단계 위로 들어 올린 moduli space | Static (Sessions 4–7) + Temporal (Session 8) | canonical Appendix OMS |
| **구현 + 테스트** | 모두 215 + 1 xfailed 통과 (~4분), exp01–exp88 다수 SUPPORTED | `CODE/scc/`, `CODE/tests/` | — |

**다음 확장에 주는 의미.** 단단한 기둥이 매우 많다. 정적 single-formation은 사실상 종결. 핵심 추론 도구(Γ-convergence, Łojasiewicz, isoperimetric, Schur/Maschke, Lions-Sznitman, Payne-Weinberger, partial OT)가 모두 검증됨. **이론은 더 이상 “버그 잡기 단계”가 아니라, 새로운 영역을 두드릴 준비가 됨.**

### 3.2 조건부로 강한 부분 (Cat B / Cat A conditional)

| 항목 | 어디까지 와 있나 | 어디가 안 닫혔나 | 다음 확장에 쓸 때 caveat |
|---|---|---|---|
| **Resolvent $C_t$** | 공리 C1–C5 만족, $C3''$ Schur complement로 닫힘 | universe 멤버에서 강등됨 — 디아그노스틱 용도만 | 정식 술어로 다시 끌어올리지 말 것 |
| **Q_morph / Inside** | normalized form Cat A | $\theta_{\mathrm{in}}$ 의존성이 명시적으로 남음 | threshold-기반 진단은 OP-0006 후속 결과(T-OP6-B) 쪽이 더 신뢰적 |
| **T-K-Select-PF / T-K-Select-OBS (Cat B)** | 평형 분포에서 K* 선택 + 관측 조건부 K* 선택 | $T_*$ 미공리화(OP-0021), Kramers rate 미증명(OP-0005-DYN) | $T_*$ 사용 시 axiomatic 주의 |
| **T-σ-Theorem-4** | continuum-limit 예측 Cat A였다가 Cat B로 retroactive 강등 | 이산 격자에서 measured $\mu_1/\mu_0 \approx 2$ vs 예측 $1$(degeneracy) | 이산 결과는 NQ-187 audit 후 |
| **Enhanced metastability (T7-Enhanced)** | closure가 Hessian eigenvalue를 올린다는 사실 Cat A | Hessian–energy barrier 간 간극은 Morse 해석 필요 | 정량 barrier에 직접 쓰지 말 것 |
| **Sep/Bind bridge** | 양방향 Cat A | 다중 응집 regime에선 conditional | multi-formation으로 끌고 갈 때 conditioning 명시 |
| **S-B1-SYM Cat B (symbolic 0.84)** | 분석적으로 유도된 $\rho_{\mathrm{deep}} \ge \theta_{\mathrm{core}}(1 - 4C_{\mathrm{iso}}/\sqrt m)$ | HWF-1 (iso_ratio ≤ C_iso) 조건부; 길쭉한 형성은 반례 | 둥근(well-formed) 형성에만 |
| **Partial-H-SINK** | one-sided row-stochastic case Cat A | balanced/double-stochastic 영역은 별도 | 현재 SCC E1엔 충분 |

### 3.3 미완 / Open

| 항목 | 현재 위치 | 막힌 곳 | 확장 후보? | 필요한 선행 |
|---|---|---|---|---|
| **OP-0005-DYN (Kramers rates)** | OPEN | Package II (Eyring-Kramers) + H-MORSE + OP-0021 | **예 — Q4 완성용** | H-MORSE Cat A + $T_*$ 정규 등록 |
| **OP-0008 σ-Inheritance (MERGE/SPLIT)** | sub-problem 4개 PARTIALLY STRUCTURED, σ_standard Cat C | Wigner-projection W9+ | **예 — Q6** | T-Temporal-Identity Cat A (이미 확보!) |
| **OP-0009 Multi-formation foundations** | 7개 sub-item 중 1/7 RESOLVED, 6/7 PARTIALLY | K-field vs shared-pool 양립, λ_rep ontology, $C_t$-multi | 부분 | OAT-2..7 통합 |
| **H-MORSE (Morse 안정성)** | OPEN, 수치적으로 $\mu_{\min} \in [0.96, 60.2]$ | 임의 임계점에서 spectrum 양성 일반 증명 부재 | **최상 우선** | T7-Enhanced + Allen-Cahn Morse 전이 |
| **H-T* ($T_*$ 정규 등록, OP-0021)** | OPEN, 5 gap (Mori-Zwanzig route) + RG route 스케치 | NOP-F / NOP-J 안 닫힘 | 중요 | Package II 진입 조건 |
| **H-SR (spectral repulsion)** | OPEN | $\min_k \mu_k > (K-1)\lambda_{\mathrm{rep}}$의 명시적 하한 | 보조 | Weyl 부등식 + 에너지 장벽 |
| **H-WS (well-separation)** | OPEN | $d_{\min}^*(\beta,\alpha,K)$ 명시 공식 | 보조 | 에너지 장벽 분석 |
| **H-σ4** | PARTIALLY OPEN | continuum vs 이산 격자 합치 (NQ-187) | 중 | 세 경로 α/β/γ 중 하나 |
| **H-P7 (decay-to-cut)** | PARTIALLY STRUCTURED | Combes–Thomas / Agmon 일반화 | 보조 | T-L1-F 조건 감소 |
| **H-κ (곡률 조건)** | OPEN | T-OP6-B의 H4 ($\kappa_{\max}\xi \le 0.1$) 에너지로부터 유도 | 보조 | — |
| **H-μ0 (μ₀ > 0 일반)** | OPEN, 수치 OK | 일반 그래프 이론 증명 부재 | 후순위 | — |
| **OP-0012 Persistence Composition** | PARTIALLY STRUCTURED | 3+-step composition formula | 중 | margin condition + Markov 형식 |
| **Empirical validation full-pipeline** | exp01–exp88 진행 중 | RGB-D / real perception 연결 미흡 | 별개 후보(D) | perception linking framework |

### 3.4 폐기 / 강등된 부분 (Retracted = 5)

| 과거 주장 | 문제 | 현재 상태 |
|---|---|---|
| **원래 A1 (weak extensivity)** | A3와 양립 불가 | **A1′로 대체** |
| **Unconstrained mountain pass / T-Merge (c)(d)(e)** | merge path가 $\Sigma_M^K$에 존재하지 않음 → MP theorem 부적용 | **RETRACTED** (2026-04-07 Erratum) |
| **Cesàro $C_t$ pairwise preservation** | 보존성 무너짐 | **resolvent $C_t$로 대체** |
| **“temporal theorem proved”(W3)** | proof strategy를 proof로 착각 | **재구성** → T-Temporal-Identity (CV-1.12 Cat B → CV-1.13 Cat A) |
| **“Brouwer로 self-referential OT 완전 해결”** | fixed-point existence ≠ uniqueness/stability | **재구성** → partial OT + S-B3 |
| **Sep_new global diagnostic ($C_t$-weighted)** | 형성 품질에 무관하게 0.5 근처 | **$u$-weighted Sep로 대체** |
| **2λ₂ critical ratio** | unordered-pair sum 표기 오류 | **4λ₂ 정정** (§0 summation convention) |
| **Theorem 3.3 ($\bar r_0 = O(n^{-1/d})$ for general τ)** | exp falsified — $\bar r_0$ is $O(1)$ for $\tau \neq 1/2$ | **RETRACTED** |
| **D-5 V5b-T′ Goldstone**(2D torus PN-barrier) | NQ-198f phantom — μ=0 exact | **V5b-T-zero (Cat A def)로 대체** |
| **T-σ-Theorem-4 Cat A**(continuum 예측) | 이산 격자에서 numerically mismatched | **Cat B로 retroactive 강등** |
| **literal $\rho_{\mathrm{deep}} \ge 0.84$ 무조건** | 길쭉한 형성에서 반례 | **S-B1-SYM Cat B (조건부)** + **Lemma S-B1-Weak Cat A** (positivity threshold 정정) |

**재사용 가능성.** 폐기된 명제는 대부분 “약화된 형태”로 재사용된다. 예: Cesàro $C_t$는 derived diagnostic으로, mountain pass는 K-field 위상고정으로, “0.84”는 symbolic identity로. **그러나 원형 그대로 끌어오지 말 것.**

---

## 4. 다음 확장 후보 분석

### 후보 1 — Temporal Persistence (Q5 deepening)

**비유.** 책상 위 물방울이 살짝 움직였다. 우리는 “같은 물방울”이라 말한다. 하지만 물방울이 갈라지거나 합쳐지면 동일성을 말하기 어렵다. Temporal Persistence는 **변형·이동·일부 손실에도 같은 응집이라고 말할 수 있는 조건**을 찾는 문제.

**현재 위치.** **상당 부분 이미 닫혔다.** CV-1.13에서 T-Temporal-Identity 네 파트(a,b,c,d) 모두 Cat A. (a) Lemma 1 constructive existence, (b) S-A1 + S-B1-Weak 양수성, (c) Lemma 11 kernel independence ($\Delta_{\mathrm{sep}} \ge \Delta_{\mathrm{sep}}^* + 2\epsilon_{\mathrm{kernel}}$), (d) K=1 reduction. 모두 single-formation 경우.

**남은 빈 자리.**
- **Multi-formation** temporal identity (CV-1.13의 non-overclaim에 명시).
- **3-step composition** (OP-0012; OP-0012-CC만 Cat B 후보).
- **ε-gentle transition** 일반화.
- **Basin stability** under transport.

**닫으려면 필요한 lemma.** S-A2 류의 multi-formation correspondence matrix 분석, partial OT의 component-level 형식화 확장, Kramers escape rate(Q3와 결합)로 transport-driven escape 통제.

**위험도 / 기대효과.** **낮은 위험·낮은 기대효과.** 단일 형성 정체성은 이미 Cat A이므로 추가 보강은 incremental. 정작 깊은 통찰은 multi-formation에서 나옴 → 후보 3과 합쳐서 추진하는 게 자연.

---

### 후보 2 — Self-Referential Optimal Transport (Q5 closure)

**비유.** 어제 물방울과 오늘 물방울을 잇는 다리. 그런데 다리의 비용이 물방울 모양에 따라 달라지고, 그 모양은 다리에 의해 다시 바뀐다 → **자기참조 고정점 문제**.

**현재 위치.** **H-SINK 완전 종료(Cat A)**, **Partial-H-SINK Cat A**, **OP-0011 PARTIALLY RESOLVED**. 즉 “고정 cost 하의 OT”와 “cost perturbation에 대한 안정성”은 이미 해결.

**남은 빈 자리.** 진정한 self-referential 단계 — cost 자체가 $u_t, u_s$에 의존하는 경우 (entropic regularization과 핵 fingerprint cost를 동시에 자기참조적으로). Brouwer fixed-point는 존재성만 주고 uniqueness/stability는 별개.

**판단.** Q5는 이미 충분히 닫혔으므로, self-referential OT는 **단독 후보로 추진할 매력이 약하다**. 후보 1 / 후보 3에 흡수해서 “multi-formation 자기참조 OT”로 묶는 것이 효율적.

---

### 후보 3 — Multi-Formation / K-Selection (Q4 + Q6 통합) ⭐

**비유.** 시야 안에 물방울 여러 개. 어떤 건 거의 붙어 있고, 어떤 건 곧 합쳐질 듯하고, 어떤 건 명확히 따로다. “지금 몇 개인가?”를 결정하는 문제.

**현재 위치.**
- **T-K-Select-PF (평형) Cat B** ✓
- **T-K-Select-OBS (관측조건부) Cat B** ✓
- **T-K-Select-DYN (Kramers) OPEN** ← 막힘
- **OP-0008 σ-Inheritance** (MERGE / SPLIT) 4 sub-problem PARTIALLY STRUCTURED
- **OP-0009 Multi-formation 7 ontological foundations** PARTIALLY RESOLVED

**single → multi에서 깨지는 것.**
- 단일 cost analyticity 단순함 → multi-block Hessian의 inter-block 결합 항.
- $\Sigma_m$ → $\Sigma_M^K$ 또는 $\mathcal{B}_K(\mathcal{P}) \subset \mathcal{F}_M(\mathcal{P})$ topological sector.
- K-field architecture(I9) vs shared-pool(I9′) 두 가지 옵션 공존.

**$K_{\mathrm{field}}$ vs $K_{\mathrm{act}}$.** Commitment 16에서 명시화됨. $K_{\mathrm{field}}$ = 구조적 슬롯 상한, $K_{\mathrm{act}}$ = 실제 활성 형성 수 (= #PersComp). T-L1-F가 이 둘의 등식을 (P0)-(P11) regime에서 보장.

**필요한 선행 구조.**
1. **H-MORSE Cat A** — 임의 critical point의 Hessian 양성성.
2. **H-T* (OP-0021)** — $T_*$ 정규 등록.
3. **Disjointness penalty / competition term** — λ_rep 형식화.
4. **K-jump dynamics** (split/merge 이벤트의 무한소 생성).
5. **σ-rich augmentation** (centroid + orientation + Wigner) — 이미 working/sigma_rich_*에 다수.
6. **Admissible $V_P$** — observer landscape (OMS-2.0에서 이미 다룸).

**위험도.** **중간.** H-MORSE는 numerically 잘 받쳐지지만 일반 증명이 까다롭다. 단 Allen–Cahn Morse 전이 결과의 SCC 변형으로 접근 경로가 보임.

**기대효과.** **매우 큼.** Q4 + Q6 두 인식론적 질문을 동시에 닫는다. Eyring-Kramers Γ_K, K→K-1 barrier crossing이 정량화되면 Q4-DYN까지 도달 → **대목표가 사실상 종결**.

---

### 후보 4 — Observer / Perception Link (응용 확장)

**비유.** 수학적으로 물방울이 정의되었지만, 실제 카메라/눈은 그것을 어떻게 보나? 이론을 RGB-D, stereo, image graph에 연결해야 한다.

**현재 위치.**
- **Stereo extension (D-ST-1..5, T-ST-5a/b)** 이미 CV-1.6에 포함.
- **OMS-2.0 Accepted Full** — observer moduli space 자체가 별도 layer로 canonicalized됨.
- **Stereo-SCC topology.py** 구현.

**남은 빈 자리.**
- 실제 image gradient → SCC field로 가는 **observation likelihood** 캐노니컬화 (LM1–LM3가 일부 있음).
- Psychophysics 예측 (예: 두 사물이 멀어질 때 1로 보이는 임계 거리)을 T8 위상전이로 정량 매핑.
- Predictive Processing 기존 패러다임과의 비교 실험.

**판단.** **수학 이론 확장이 아니라 응용/해석 확장.** 추진 가치는 매우 높지만, **수학적으로 “닫히는” 문제가 아니다.** 따라서 단독 우선 추진보다는 후보 3 다음 단계의 paper-level 검증 경로로 자연스럽게 따라옴.

---

### 후보 5 — Computational / Experimental Consolidation

**비유.** 설계도는 있지만 실제 모형 자동차를 굴려서 바퀴가 빠지나 확인. 약한 나사를 찾는 작업.

**현재 위치.** 215 + 1 xfailed 테스트 통과. exp01–exp88까지 다수.

**가장 먼저 보강할 것.**
- **R10 / separation dominance 판정** — λ_sep 우위 영역 정량화.
- **Energy ablation** — full SCC vs BD-only, full SCC vs CL+SEP-only.
- **Full SCC의 BD-only 대비 고유 기여** — multi-peak attractor (T-PreObj-1)에서 closure가 만든 차이.
- **Random vs adaptive IC 격차** — $L^{2.8}$ exponent.
- **H-MORSE numerical extension** — $\mu_{\min}$ 분포의 더 넓은 sweep.

**판단.** **낮은 위험·중간 기대효과.** 실험 보강은 항상 가치 있지만, 새로운 정리를 닫지는 않음. **후보 3을 추진할 때 동시에 진행할 baseline 작업**으로 적합.

---

## 5. 확장 우선순위 평가표

각 후보 1~5점, 종합 판정.

| 확장 후보 | 자연성 | 닫힘 가능성 | 논문화 가치 | 위험도(↓좋음) | 구현 가능성 | 선행 의존성(↓좋음) | 설명 가능성 | 종합 판정 |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| **1. Temporal Persistence 보강** | 4 | 5 | 3 | 1 | 5 | 1 | 4 | 보수적 마무리 |
| **2. Self-Ref OT 단독** | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 보류 (후보3에 흡수) |
| **3. Multi-Formation + K-Sel ⭐** | 5 | 4 | 5 | 3 | 4 | 3 | 5 | **즉시 추진 / 선행 lemma 후 본격화** |
| **4. Perception / OMS link** | 4 | 2(수학) / 5(응용) | 5 | 2 | 4 | 2 | 5 | 후보3 후 추진 |
| **5. Experimental consolidation** | 5 | 5 | 2 | 1 | 5 | 1 | 4 | 후보3 baseline로 병행 |

종합 판정:

- 후보 1: **선행 lemma 후 추진 (multi-formation case)** — 단일 formation은 이미 종결.
- 후보 2: **open problem으로 보류** — 후보 3에 자연 흡수.
- 후보 3: **즉시 추진** (H-MORSE Cat A 먼저).
- 후보 4: **후보 3 후 추진 / 동시 paper-track 가능**.
- 후보 5: **상시 병행** (특히 H-MORSE numerical 확장).

---

## 6. 추천 확장 로드맵

### Roadmap A — 보수적 논문화 경로

**비유.** 이미 다 자란 나무에서 잘 익은 열매들을 따서 시장에 내놓는다.

- **목적.** 단일 formation SCC 정적 이론 + temporal identity (CV-1.13 Cat A 결과) + Package I + T-K-Select를 paper 1편으로 정식 publication.
- **선행 조건.** 없음 — 이미 충분.
- **작업.**
  1. `papers/paper1_math.tex` 재작성 (2026-05-04 삭제된 draft).
  2. `papers/paper2_cogsci.tex` 재작성 (perception interpretation).
  3. Figure script (generate_figures.py)와 일관성 맞춤.
- **산출물.** Math paper (canonical CV-1.13 기준), CogSci paper (DECLARATION.md 해석 + T8 + diagnostic vector).
- **실패 시 fallback.** 거의 없음. 단지 reviewer가 perception link를 요구하면 후보 4를 일부 흡수.
- **예상 OP.** 없음.

### Roadmap B — Temporal 확장 경로 (이미 거의 종료)

**비유.** 물방울 하나의 시간 정체성은 “이미 봉인된 상자”. multi-formation으로 확장하는 일이 남았다.

- **목적.** T-Temporal-Identity multi-formation 확장.
- **선행 조건.** H-MORSE 일부 + T-σ-Inherit (OP-0008) MERGE/SPLIT 진전.
- **작업.**
  1. component-level OT의 multi-formation 확장.
  2. K-jump 이벤트 (birth/death) 대응표 형식화.
  3. OP-0012 composition formula.
- **산출물.** T-Temporal-Identity-Multi Cat B → Cat A.
- **실패 시 fallback.** Cat B 유지 + Cat A는 별도 paper로.
- **예상 OP.** OP-0012-3step, OP-0008-DIST.

### Roadmap C — Multi-Formation + K-Selection 확장 경로 ⭐

**비유.** 여러 물방울이 동시에 살아가는 도시의 인구 동태를 수학화한다.

- **목적.** Package II 진입 → Eyring-Kramers Γ_K → Q4-DYN 완성 → 대목표 종결.
- **선행 조건.**
  - **H-MORSE Cat A** (가장 중요).
  - **H-T* / OP-0021** (T_* 정규 등록, NOP-F or NOP-J 경로).
  - **σ-rich Lipschitz** (이미 working에 있음).
- **작업 순서.**
  1. **H-MORSE 단독 attack.** working/SF/sigma_m_hessian_convention_audit.md를 기반으로 임의 critical point의 spectrum 양성 증명. Allen-Cahn Morse 전이 문헌 + T7-Enhanced 결합.
  2. **OP-0021 attack.** Mori-Zwanzig 경로 5 gap 닫기 또는 RG 고정점 경로(T_*^{Fisher} = T_*^{RG}).
  3. **Package II 정식 작성** — Eyring-Kramers Γ_K = (rate prefactor) × exp(-ΔE/T_*).
  4. **T-σ-Inherit MERGE/SPLIT** — Wigner-projection을 σ-standard에 정식 적용.
  5. **T-K-Select-DYN Cat A 격상**.
- **산출물.** CV-1.14 sealed: T-σ-Inherit Cat B + Package II Cat B; CV-1.15 target: K-Select-DYN Cat A.
- **실패 시 fallback.** Package II는 Cat B로 유지, T_*는 axiomatic 유지. 그래도 σ-Inherit 진전은 가능.
- **예상 OP.** OP-MORSE-residual, OP-T*-RG.

### Roadmap D — Perception / Cognitive Science 연결 경로

**비유.** 수학적으로 잘 닦아 둔 도구를 실제 카메라·눈·시각피질 모델에 꽂아본다.

- **목적.** Stereo-SCC + OMS-2.0를 실험적 perception 예측에 연결.
- **선행 조건.** Roadmap A 종료 + 실험 인프라.
- **작업.**
  1. RGB-D 데이터셋(YCB, NYU)에서 stereo-SCC pipeline 검증.
  2. Psychophysics 데이터(2-AFC 실험)와 T8 phase transition 예측 매핑.
  3. ONN/ORTSF perception stack 연계 — `scc_relation_onn_ortsf_perception_stack.md` 활용.
- **산출물.** Empirical paper (퍼셉션 예측 + 데이터 검증).
- **실패 시 fallback.** 수학 이론 자체는 변하지 않음. 검증 실패 시 “모델링 layer mismatch”라는 분리 명시.
- **예상 OP.** Observation likelihood canonicalization.

---

## 7. 최종 결론

### 7.1 현재 SCC는 어디까지 와 있는가?

**71%가 완전히 증명된 상태이며, 단일 formation 정적 이론은 사실상 종결되었다.** Q1(경계 출현), Q3(잡음 속 동역학 Package I), Q5(시간 정체성)이 모두 Cat A로 닫혔다. Q2(공존), Q4(K-선택), Q6(분열·합병)이 Cat B로 부분 닫혔다.

### 7.2 다음 확장으로 가장 적절한 것은?

**Roadmap C (Multi-Formation + K-Selection)이다.** 구체적으로는 **H-MORSE를 먼저 Cat A로 닫고, 그 다음 Package II(Eyring–Kramers)로 진입**하는 경로다. 이것이 “대목표” — “어떤 차이의 덩어리가 언제부터 하나의 객체가 되는가?” — 의 마지막 큰 조각이다.

### 7.3 왜 그것이 가장 적절한가?

- **선행 의존성이 안에서 닫혀 있다.** P-F-A1 Package I 전체가 Cat A이므로 Package II 진입에 필요한 토대(SDE 존재 + Gibbs 불변 + Poincaré 부등식)가 이미 마련됨.
- **수치 증거가 H-MORSE를 강하게 받친다.** $\mu_{\min} \in [0.96, 60.2]$ 모든 tested config — 증명만 더 단단히 하면 됨.
- **하나의 정리로 Q4 + Q6 두 인식론적 질문을 동시 닫는다.**
- **논문화 가치가 최상위.** 응집 형성의 “수, 동역학, 위상전이” 삼중주가 한 framework에 들어옴.

### 7.4 지금 하면 위험한 확장은?

- **Self-referential OT 단독 추진** (후보 2) — H-SINK가 이미 닫혔기 때문에 단독 노벨티가 약하다.
- **Perception 연결을 너무 일찍** (후보 4 단독) — 수학적 closure가 끝나지 않은 상태에서 응용 paper를 내면 reviewer가 “수학적 정당성”을 다시 묻게 된다.
- **T-σ-Theorem-4 continuum 재격상 시도** — NQ-187에서 이산 격자 mismatch가 있는 상태, γ/β/α 감사 종료 전까지 보류.
- **Mountain pass 재도입** — $\Sigma_M^K$에 merge path가 없다는 사실은 구조적이므로, 옛 형태로 끌어오면 안 됨.

### 7.5 다음 작업의 첫 번째 파일·정리·실험

**첫 번째 정리.** **H-MORSE Cat A 증명 시도.**
**첫 번째 파일.** `THEORY/working/SF/sigma_m_hessian_convention_audit.md` (H-MORSE prerequisite).
**첫 번째 실험.** `CODE/experiments/` 신규 — H-MORSE numerical extension: 더 넓은 graph 클래스(SBM, barbell, 작은-월드)에서 $\mu_{\min}$ 분포 sweep + 임의 critical point에서 spectrum 확인.

---

## 8. 마지막 다섯 문장 — 수학 모르는 사람도 알 수 있게

1. SCC는 “사과가 보이기 직전, 시야 위에 어떤 안개 같은 덩어리가 진해지는 순간”을 수학으로 잡으려는 이론이다.
2. 지금까지 이 이론은 “안개 한 덩어리”에 대해서는 거의 완벽하게 풀어냈고, “어제와 오늘의 안개가 같은 것이라 말할 조건”도 막 풀어냈다.
3. 남은 큰 문제는 “안개 덩어리가 두 개일 때, 그리고 그 두 개가 합쳐지거나 갈라질 때 어떻게 다루느냐”다.
4. 이 문제를 풀기 위해 가장 먼저 해야 할 일은, “안개 덩어리의 모양이 약간 흔들려도 무너지지 않는다는 것”을 일반적으로 증명하는 일(H-MORSE)이다.
5. 그게 풀리면, “시야 안에 안개가 몇 덩이 있는지, 어느 순간 합쳐지는지”까지 수학으로 자연스럽게 따라 나오게 되어, 이 이론은 자신의 출발 질문 — *어떤 차이의 덩어리가 언제부터 하나의 객체가 되는가?* — 에 거의 완전한 답을 가질 수 있게 된다.

---

**보고서 종료. 작성 기준: CV-1.13 (sealed 2026-05-10, 83 claims).**
**다음 실행 시 권장:** `THEORY/working/SF/sigma_m_hessian_convention_audit.md`를 열어 H-MORSE attack을 시작.
