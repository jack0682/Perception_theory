---
type: log/daily/insight_decomposition
date: 2026-05-15
session_label: W7-Day6 Stage 2 — Insight Decomposition
canonical_version: CV-1.16 (sealed 2026-05-14, untouched)
prerequisite: 02_canonical_inventory.md 완료
mode: 분해 — 새 수학 생성 금지
stage: 2 of 6
---

> [!nav] Linked: [[02_canonical_inventory]] · [[00_plan]] · [[01b_user_proposal_zfield]]


# 03 — Insight Decomposition (Stage 2)

**Session:** 2026-05-15 (W7-Day6)
**Target (from `00_plan.md`):** 통찰을 *최소 명제 단위* 로 분해. 각 문장이 주장하는 바를 원자적 명제로.
**This file covers:** Stage 2 — 통찰 텍스트의 *원자적 분해* + 각 명제의 *수학명제 후보 vs 해석/철학적 주장* 분류.
**Depends on reading:** `01_pre_brainstorm §"원래 통찰"`; `01b §3, §8`; `DECLARATION` §"태초의 장면", §"중심 정리", §"관측 조건"; `02_canonical_inventory.md`.

---

## §1. Stage 2 의 위치

Stage 1 inventory 는 canonical 의 *현재 상태* 를 측정. Stage 2 는 *통찰 자체* 를 측정 — 통찰 본문이 *몇 개의 명제* 로 분해되는가. 큰 문장 하나를 *원자적 주장 N 개* 로.

Stage 3 (confrontation) 의 *행* 단위가 Stage 2 의 산출물.

자기 강제:
- 명제는 *quantifier 와 부호* 명확. ∀, ∃, ≤, ≥, →, ⊂ 등.
- 각 명제는 *증명 가능 또는 반증 가능* (Popper-검증가능성) 인지 자체 분류.
- 명제 number 는 후속 Stage 들이 *§3.k* 형식으로 참조 가능하도록 안정 유지.

---

## §2. 통찰 본문 (재인용, 5/14 저녁 사용자 표현)

```
우리는 "3개" 를 먼저 보는 것이 아니라, "서로 다르게 응집된 장면" 을 먼저 본다.

감각장 → 약한 차이 → 응집 → 구조화된 차이 → 해석 → 셈

개수는 응집의 원인이 아니라, 응집된 구조의 판독 결과다.

u^* → S_0(u^*) → K_read

D_0 (전-응집 미분) → D_1 (응집 중 구조) → D_2 (응집 후 해석)

SCC 가 진짜 설명해야 하는 것은 D_0 → D_1, 즉 약한 차이가 어떻게 응집된 구조가 되는가다.
```

추가로 사용자 메모 `01b §3`, `01b §8` 의 수식화도 분해 대상에 포함.

---

## §3. 원자적 명제 (P-1 ~ P-12)

각 명제: **(P-k) 본문 → 수학 형식화 → 분류 (수학명제 후보 / 해석 / 철학) → Popper 검증가능성**

### P-1: 다채널 약한 차이 *존재* 주장

**본문**: "감각장은 색·밝기·깊이·질감·운동·방향성 같은 약한 차이로 미분되어 있다 (응집 *전*)."

**형식화**: 어떤 *site space* $X$ 와 *feature space* $\mathcal{F}$ 가 있어, 함수 $z : X \to \mathcal{F}$ 가 응집장 $u$ 의 형성 *이전에* 정의되어 있다.

$$\exists\, X,\ \mathcal{F},\ z : X \to \mathcal{F} \text{ 로서 } z \text{ 가 } u\text{-formation 이전 단계에 존재}$$

**분류**: **존재 주장**. 그러나 SCC 내부에서는 "응집 이전" 의 *시간/논리적 순서* 의 의미가 미정 — DECL-1.0 의 화살표가 부분적으로 이를 시간 순서로 부여하나, *수학적* 시간 순서는 canonical 에 없음. 따라서 *해석적 주장* 으로도 분류 가능.

**Popper**: *부분적*. $z$ 의 *존재* 는 trivial (어떤 feature map 이든 정의 가능). *비-trivial 한 형태* — 즉 *"$u_t$ 가 $z$ 의 *해* 라는 의미에서 $z$ 가 prior"* — 는 사용자 메모 §3 에서 *variational stabilization* 으로 형식화되어야 검증 가능. 본 명제 자체로는 trivial.

### P-2: 약한 차이가 *상호 지지* 로 응집

**본문**: "약한 차이들 중 일부가 서로를 지지하면서 응집한다."

**형식화**: 응집장 $u_t$ 의 closure operator $\mathrm{Cl}_t$ 가 자기-지지 contraction 성질 (A1'/A2/A3, $a_{\mathrm{cl}}<4$).

$$\mathrm{Cl}_t : [0,1]^{X_t} \to [0,1]^{X_t},\ \|\mathrm{Cl}_t(u) - \mathrm{Cl}_t(v)\|_D \leq (a_{\mathrm{cl}}/4) \|u - v\|_D$$

**분류**: **수학명제** (이미 canonical, A3 = Cat A).

**Popper**: 검증 가능. canonical 에서 *증명됨*.

### P-3: 응집 진행 → 경계 *선명* 화

**본문**: "응집이 진행되면 경계가 선명해진다."

**형식화**: T8 임계 충족 시 (β/α > 4λ_2/|W''(c)|), 에너지 최솟값은 비균일 (boundary 출현). 또한 T-OP6-B 가 $d_H(B_{\mathrm{PersRidge}}, \partial\mathrm{PersComp}) \leq 2(\alpha/\beta)^{1/2}$.

**분류**: **수학명제** (T8-Core/Full + T-OP6-B 모두 Cat A).

**Popper**: 검증 가능. canonical 에서 *증명됨*.

### P-4: 분해 한계 — 두 사과가 *하나로* 보일 수 있다

**본문**: "두 사과가 멀리 있으면 *하나로* 보일 수 있다. 해상도가 낮으면 두 객체가 융합한다."

**형식화**: T8 임계 *붕괴* 조건. $\beta/\alpha \leq 4\lambda_2/|W''(c)|$ — 또는 $\lambda_2 \to$ 작음 → 임계 붕괴 → uniform minimum.

**분류**: **수학명제** + **DECL-1.0 의 직접 인용 ("이것이 이 이론의 심장이다")**.

**Popper**: 검증 가능. *증명됨*.

### P-5: 셈 (counting) 은 응집의 *원인* 이 아니라 *결과*

**본문**: "개수는 응집의 원인이 아니라, 응집된 구조의 판독 결과다."

**형식화**: $K_{\mathrm{act}}(u^*) = \#\mathrm{PersComp}(u^*; \rho_{\mathrm{pers}})$ — *$u^*$ 로부터 readout* (역방향 아님).

또는: $K$ 가 *minimizer* 에 들어가는 외부 파라미터가 아니라 *minimizer 의 함수*.

**분류**: **수학명제** + **CN6, CN10 (one-way) 의 메타 commitment**.

**Popper**: 검증 가능. CN10 ("one-way") 은 사용자가 미리 선언한 정책으로서 *수학적* 검증 대상이라기보다 *디자인 결정*. K_act 의 정의 (§3.11) 와 Commitment 16 (ii) 가 이를 구현.

### P-6: 응집 구조의 *내부 데이터* $S_0(u^*)$

**본문**: "응집된 구조는 그 자체로 *데이터* — centroid, orientation, sigma_standard 같은 내부 readout."

**형식화**: $S_0(u^*) := (\mathrm{PersComp}(u^*), \sigma_{\mathrm{rich}}(u^*))$ — derived diagnostic.

**분류**: **수학적 정의** (canonical 에 σ_rich derived diagnostic 으로 존재).

**Popper**: 검증 가능. canonical 의 σ_rich namedtuple + Wigner-projection 등 정의.

### P-7: 화살표의 *방향성* — $u^* \to S_0 \to K_{\mathrm{read}}$

**본문**: "$u^*$ → $S_0(u^*)$ → $K_{\mathrm{read}}$ 의 *순서*. 역방향 금지."

**형식화**: 각 화살표가 *함수* (입력 → 출력), 역화살표는 *자동* 없음 (역함수 일반적으로 부재).

**분류**: **수학적 정의** (function composition) + **메타 commitment** (CN10 one-way).

**Popper**: trivial 한 정의. 비-trivial 한 부분 — 역방향이 *수학적으로* 가능한지 (예: $K$ 로부터 $u^*$ 의 일부 정보 복원) — 는 별도 검증 필요.

### P-8: D_0 → D_1 → D_2 *삼층* 구조

**본문**: "D_0 (전-응집 미분) → D_1 (응집 중 구조) → D_2 (응집 후 해석) 의 세 층."

**형식화**: 세 객체 $D_0, D_1, D_2$ 와 두 화살표 $D_0 \to D_1, D_1 \to D_2$. 각 객체는 *수학적 객체* 의 모음.

- $D_1 = u_t \in [0,1]^{X_t}$ (canonical primitive)
- $D_2 = (K_{\mathrm{act}}, \sigma_{\mathrm{rich}}, ...)$ (canonical derived diagnostics)
- $D_0 = ?$ (**candidate 부재** — Stage 1 §4 참조)

**분류**: **부분 수학명제** (D_1, D_2 부분) + **부분 미정 명제** (D_0 부분).

**Popper**: D_1, D_2 측면은 검증 가능 (이미 canonical). D_0 측면은 *명제 자체로는* 검증 불가 — D_0 의 *수학적 정의* 가 없으면 화살표 $D_0 \to D_1$ 가 *어느 정도 비-trivial* 한지 평가 불가.

### P-9: SCC 가 *진짜 설명해야 할 것* 은 D_0 → D_1

**본문**: "SCC 가 진짜 설명해야 하는 것은 D_0 → D_1, 즉 약한 차이가 어떻게 응집된 구조가 되는가다."

**형식화**: SCC 의 *최소 정당화 범위* 는 $D_0 \to D_1$ 화살표를 *수학화* 하는 것. canonical 의 *현재 범위* (= $D_1$ 만, plus readout $D_1 \to D_2$) 는 *불충분*.

**분류**: **메타 명제** — SCC 의 scope 에 대한 normative 주장. *수학명제가 아니라 *DECL-1.0 의 수정 제안***.

**Popper**: 직접 검증 불가. SCC 의 scope 는 사용자 정의 (DECL-1.0). 이 명제는 *DECL-1.0 변경 제안* 으로서만 의미를 가진다. Stage 5–6 의 결정 대상.

**주의**: P-9 는 사용자 본인의 표현이지만, *DECL-1.0 (2026-05-07) 의 명시적 화살표 외부화* 와 *충돌* 한다. 사용자가 자신의 prior commitment 와 *현재 의도* 사이의 긴장을 표현하고 있는 것 — Stage 6 에서 명시적으로 다룰 점.

### P-10: $z_t$ 가 prior 인 $u_t^*$ 의 *variational* 정식

**본문** (`01b §3`): $u_t^* = \arg\min_{u \in \Sigma_m} \mathcal{E}(u; z_t)$, 여기서 $\mathcal{E}$ 는 SCC energy, $z_t$ 가 $K_{z_t}(x,y) = \exp(-d_X^2/2\rho^2)\exp(-d_\mathcal{F}^2/2\sigma^2)$ 를 통해 SCC 의 adjacency kernel 을 만든다.

**형식화**: $z_t \to K_{z_t} \to (E_{\mathrm{cl}}, E_{\mathrm{sep}}, E_{\mathrm{bd}}, E_{\mathrm{tr}}) \to u_t^*$.

**분류**: **수학명제 후보**. 그러나 *현재 canonical 의 N_t 와의 관계* 에 의존:
- 만약 $K_{z_t}$ = N_t (같은 것의 다른 이름) → trivial — $z_t$ 는 N_t 의 *parametrization* 일 뿐.
- 만약 $K_{z_t} \neq$ N_t 이고 *비-trivial 새 제약* 을 가짐 → 새 수학.
- Stage 3 의 confrontation 표가 이를 결정.

**Popper**: 형식화는 검증 가능. *trivial 인가 non-trivial 인가* 의 판정은 Stage 3/4 에서.

### P-11: T-D0D1-Existence

**본문** (`01b §8` 의 첫 후보 정리): "유한 $X_t$ 에서 $z_t$-conditioned SCC energy 는 $\Sigma_m$ 위의 minimizer $u_t^*$ 를 가진다."

**형식화**: $\forall z_t : X_t \to \mathcal{F}, \forall G$ finite connected, $\exists u_t^* \in \Sigma_m$ such that $u_t^* = \arg\min_{u \in \Sigma_m} E(u; K_{z_t})$.

**분류**: **수학명제**. 그러나 **trivial 임을 우려**: $E$ 가 $u$ 에 대해 continuous, $\Sigma_m$ 이 compact convex (finite-dim simplex) — Weierstrass extreme value theorem 으로 즉시 minimizer 존재. *z_t* 가 새 primitive 라는 사실과 무관하게 *어떤 continuous E 든* minimizer 가짐.

**Popper**: 검증 가능, 그러나 trivial. 사용자 메모도 §8 에서 "*증명은 compactness + continuity 로 가능할 것*" 라고 인정.

**자체 판정**: T-D0D1-Existence 는 *substantive content 없는* 정리. Cat A 로 증명 가능하나, 그것이 *새 수학* 인 것은 아님 — canonical 의 minimization 정리들 (예: §13 T-Persist-1(b)) 의 standard adaptation.

### P-12: T-D0D1-Nonuniformity

**본문** (`01b §8` 의 둘째 후보 정리): "$z_t$ 의 차이가 비균일 $u_t^*$ 를 유도하는 조건."

**형식화**: $\exists$ 조건 $\mathcal{C}$ on $z_t$ such that, if $z_t$ satisfies $\mathcal{C}$, then $u_t^* = \arg\min E(u; K_{z_t})$ is non-uniform on $X_t$.

**분류**: **수학명제 후보** — *비-trivial 가능성 있음*.

**Popper**: 검증 가능. 그러나 의문 점:

1. canonical T8 (Cat A) 이 이미 *N_t 의 spectral 성질 ($\lambda_2$) 이 비균일 minimizer 를 강제* 하는 조건. T8 의 $\lambda_2$ 가 $K_{z_t}$ 의 spectral gap 이라면, T-D0D1-Nonuniformity 는 *T8 의 special case* — *새 수학 아님*.
2. *비-trivial 새 수학* 이 되려면 *$z_t$ 가 $K_{z_t}$ 위에 induce 하는 spectral 구조* 가 *T8 의 가설 너머* 의 어떤 성질을 가져야 함. 어떤 성질인지 사용자 메모 §8 에 명시되어 있지 않음 — 따라서 *현재로서는 명제가 미완*.

**자체 판정**: T-D0D1-Nonuniformity 는 *substantive 일 가능성이 있는 명제 후보*, 그러나 *현재로서는 T8 의 reformulation 으로 환원될 위험 큼*. Stage 4 의 verification 에서 *T8 너머* 인지 *T8 의 동일물* 인지 결정.

---

## §4. 명제 분류 요약표

| # | 명제 (요약) | 형태 | 검증가능성 | Stage 1 inventory 와 관계 |
|---|---|---|---|---|
| **P-1** | 다채널 약한 차이 존재 ($z$ exists) | 존재주장 | trivial | D_0 부재 — canonical 외부 |
| **P-2** | 상호 지지 응집 (closure) | 수학명제 | 증명됨 | D_1 내부 (A3 Cat A) |
| **P-3** | 응집 → 경계 선명 | 수학명제 | 증명됨 | D_1 (T8 + T-OP6-B Cat A) |
| **P-4** | 분해 한계 (사과 융합) | 수학명제 | 증명됨 | D_1 (T8 collapse Cat A) |
| **P-5** | 셈 = 응집 결과 readout | 수학명제 + 메타 | 정의됨 | D_2 (§3.11 + CN10) |
| **P-6** | $S_0(u^*)$ 내부 데이터 | 수학적 정의 | 정의됨 | D_2 (σ_rich derived) |
| **P-7** | $u^* \to S_0 \to K$ 방향성 | 정의 + 메타 | trivial 정의 | D_2 화살표 (canonical) |
| **P-8** | D_0/D_1/D_2 삼층 | 부분 명제 | 부분 검증 | D_1, D_2 담김; D_0 부재 |
| **P-9** | SCC 가 D_0→D_1 설명해야 | **메타 normative** | DECL-1.0 수정 제안 | DECL-1.0 화살표와 *충돌* |
| **P-10** | $z_t \to K_{z_t} \to u^*$ | 수학명제 후보 | Stage 3/4 결정 | N_t parametrization 의심 |
| **P-11** | T-D0D1-Existence | 수학명제 | trivial (Weierstrass) | substantive 없음 |
| **P-12** | T-D0D1-Nonuniformity | 수학명제 후보 | 의문 — T8 reformulation 위험 | Stage 4 핵심 검증 대상 |

---

## §5. 분해의 패턴 — 12 명제의 분포

12 명제 중:

- **이미 canonical 에 담긴 명제 (= D_1 / D_2 내부)**: P-2, P-3, P-4, P-5, P-6, P-7 — **6개**.
- **trivial 또는 substantive 없는 명제**: P-1, P-11 — **2개**.
- **메타 / DECL-1.0 변경 제안**: P-9 — **1개**.
- **부분 수학적 + 부분 미정 (D_0 의 미정에 의존)**: P-8, P-10, P-12 — **3개**.

**비율**:
- 50% (P-2 ~ P-7) = 이미 담김.
- 25% (P-8, P-10, P-12) = 새 수학 후보 *지만* canonical 내부 (N_t, T8) 로 환원 위험.
- ~17% (P-1, P-11) = trivial.
- ~8% (P-9) = scope normative 주장 (수학 명제 아님).

**관찰**: 통찰의 *대부분* (P-2 ~ P-7) 은 *이미 담김*. 통찰의 *새 부분* 후보 (P-8, P-10, P-12) 는 모두 *D_0 의 수학적 지위에 의존*. D_0 의 수학화가 단순 N_t parametrization 인지 (위 §3 P-10 분석) 아니면 *비-trivial 새 primitive* 인지가 결정의 정점.

---

## §6. Stage 2 → Stage 3 연결 메모

Stage 3 (`04_confrontation.md`) 의 confrontation 표는 본 §4 표의 *각 명제 행 × Stage 1 inventory 의 canonical 위치* 의 대조. 각 행에 *"이미 담김 / canonical 외부 / 부분 / 새 명제"* 의 4-way 분류 부여.

**Stage 4 의 핵심 검증 대상** (Stage 3 의 "새 명제" / "부분" 행 들):
- **P-10**: $K_{z_t}$ 가 N_t 와 *형태적으로 다른가* 의 검증 (Gaussian product = 표준 도구 형태 → *§8-5 proxy 검증* 의 정확한 위치).
- **P-12**: T-D0D1-Nonuniformity 가 T8 의 *reformulation* 인가 *strict 확장* 인가 의 검증.

**Stage 5 의 archive 패턴 검증 대상**:
- P-9 (scope 변경 제안) 의 *효과* 가 V-AFD ("vector projection of formations") / R-2 ("PD_0 bar identity = K_act") 와 *동일 구조* 인가. 즉 *DECL-1.0 의 화살표 시작점을 위로 이동* 하는 시도가 (a) 새 수학 (b) language refactoring 중 어느 것인가.

---

*Stage 2 종료. Stage 3 (`04_confrontation.md`) 진입.*
