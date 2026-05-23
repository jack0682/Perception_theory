---
type: log/daily/confrontation
date: 2026-05-15
session_label: W7-Day6 Stage 3 — Confrontation
canonical_version: CV-1.16 (sealed 2026-05-14, untouched)
prerequisite: 02_canonical_inventory.md, 03_insight_decomposition.md 완료
mode: 대조 — 새 수학 생성 금지
stage: 3 of 6
---

> [!nav] Linked: [[02_canonical_inventory]] · [[03_insight_decomposition]] · [[01b_user_proposal_zfield]]


# 04 — Confrontation (Stage 3)

**Session:** 2026-05-15 (W7-Day6)
**Target:** Stage 2 의 12 명제 (P-1 ~ P-12) 를 Stage 1 의 canonical inventory 와 *대조*. 각 명제에 4-way 상태 분류: *이미 담김 / canonical 외부 / 부분 / 새 명제*.
**This file covers:** Stage 3 — confrontation 표 + 새 명제 후보의 *수학명제 정식 형태* 작성.
**Depends on reading:** Stage 1, Stage 2 출력 + `01b §3, §8`.

---

## §1. Stage 3 의 위치

Stage 1 = canonical 측정. Stage 2 = 통찰 측정. Stage 3 = *대조*.

대조의 *4-way 상태*:
- **이미 담김** (= 새 수학 아님, 결정 C 증거)
- **canonical 외부** (= 범위 밖, 결정 C 또는 A 증거 — DECL-1.0 변경 필요시 A)
- **부분적** (= 약간 새로움, 결정 B 의심 또는 A 부분 증거)
- **새 명제** (= 결정 A 증거; *구체 명제로 적어둠*)

자기 강제: 새 명제 후보는 §8 에서 *quantifier 와 부호 명확한 정식 수학 형태* 로 적는다. Stage 4 의 verification 대상.

---

## §2. Confrontation 표 (P-1 ~ P-12 × canonical)

각 행: 명제 → canonical 대응 → 위치 (구체 §) → 4-way 상태 → 비고.

| # | 명제 | canonical 대응 | 위치 | 상태 | 비고 |
|---|---|---|---|---|---|
| **P-1** | 다채널 약한 차이 *존재* | (해당 primitive 없음) | §3.2 modeling layer note | **canonical 외부** | DECL-1.0 화살표 시작점 위 — *명시적 외부* |
| **P-2** | 상호 지지 응집 (closure) | A1'/A2/A3 contraction | §6 Group A | **이미 담김 (Cat A)** | $a_{\mathrm{cl}}<4$ 강제 |
| **P-3** | 응집 → 경계 선명 | T8-Core/Full + T-OP6-B | §13 (Cat A) | **이미 담김 (Cat A)** | DECL-1.0 의 "심장" |
| **P-4** | 분해 한계 (사과 융합) | T8 collapse: $\beta/\alpha \leq 4\lambda_2/\lVert W''(c) \rVert$ | §13 + DECL-1.0 | **이미 담김 (Cat A)** | $\lambda_2 \to 0$ 의 직접적 결과 |
| **P-5** | 셈 = 응집 결과 readout | $K_{\mathrm{act}} = \#\mathrm{PersComp}(u^*)$ + Comm.16 (ii) | §3.11 + §11.1 | **이미 담김 (Def + Cat A 조건부)** | T-L1-F/T-L1-M Cat A 가 $K_{\mathrm{soft}}=K_{\mathrm{act}}$ 다리 |
| **P-6** | $S_0(u^*)$ 내부 데이터 | $\sigma_{\mathrm{rich}} = (\mathrm{centroid}, \mathrm{orient}, \sigma_{\mathrm{std}}, \mathrm{wigner})$ derived | derived diagnostic + OP-0008 | **부분적** | centroid/orient Cat B; σ_std MERGE/SPLIT Cat C |
| **P-7** | $u^* \to S_0 \to K$ 방향성 | function composition + CN10 one-way | §3.11 + §14 CN10 | **이미 담김** | trivial 정의 + 메타 commitment |
| **P-8** | D_0/D_1/D_2 삼층 | D_1 (§3.3 u_t) + D_2 (§3.11) ; D_0 부재 | (D_0 부재) | **부분적** | D_1, D_2 담김; D_0 명시적 외부 |
| **P-9** | SCC 가 D_0→D_1 *설명해야* | DECL-1.0 화살표 시작점 정책 | DECL-1.0 §"태초의 장면" | **DECL-1.0 변경 제안** | 수학 명제 아님 — scope 변경 |
| **P-10** | $z_t \to K_{z_t} \to u^*$ | N_t (§3.5) 가 K_{z_t} 의 *상위 추상* | §3.5 + B1-B4 | **이미 담김 (parametrization)** | §3 에서 정량화 — *형태적 동일* |
| **P-11** | T-D0D1-Existence | Weierstrass on compact $\Sigma_m$ + T-PF-A1-AR (Cat A) | §13 (T-PF-A1-AR) | **이미 담김 (trivial)** | $\Sigma_m$ compact convex; $E$ continuous → minimizer 존재. canonical 의 P-F-A1 Package I 의 부분 |
| **P-12** | T-D0D1-Nonuniformity | T8 의 reformulation 후보 | §13 T8-Core/Full | **부분적 / 의심** | T8 너머 인지 검증 — Stage 4 핵심 |

---

## §3. P-10 의 정밀 검사 — $K_{z_t}$ 가 N_t 의 parametrization 인가

**사용자 제안의 kernel 형태** (`01b §3`):

$$K_{z_t}(x,y) = \exp\left(-\frac{d_X(x,y)^2}{2\rho^2}\right) \cdot \exp\left(-\frac{d_\mathcal{F}(z_t(x), z_t(y))^2}{2\sigma^2}\right)$$

**canonical 의 N_t 공리 (B1-B4)** 의 manifest:

- **B1 (Non-negativity)**: $\mathbf{N}_t(x,y) \geq 0$ — $K_{z_t}$ exponential product 이므로 자동 만족.
- **B2 (Symmetry)**: $\mathbf{N}_t(x,y) = \mathbf{N}_t(y,x)$ — $d_X, d_\mathcal{F}$ 가 *metric* 인 한 자동.
- **B3 (Locality)**: $\mathbf{N}_t(x,y)$ decays as $d_X(x,y) \to \infty$ — Gaussian decay → 만족.
- **B4 (Non-Transitivity)**: 명시적으로 transitivity 가정 안 함 — Gaussian product 는 transitive 아님 (counter-example: $K(x,y) = K(y,z) = e^{-1}$ 이지만 $K(x,z)$ 일반적으로 $\neq e^{-1}$).

**판정**: $K_{z_t}$ 는 **N_t 의 *valid realization***. canonical Group B 공리를 *모두* 만족.

**역방향**: canonical N_t 는 $K_{z_t}$ 의 *추상화*. 어떤 N_t 든 *적절한 $z_t, d_\mathcal{F}, \rho, \sigma$* 가 있으면 $K_{z_t}$ 형태로 표현 가능 — 즉 $K_{z_t}$ family 는 *N_t family 안* 의 *parametrized sub-family*.

**결론**: P-10 의 화살표 $z_t \to K_{z_t} \to u^*$ 는 canonical 화살표 $N_t \to u^*$ 의 *parametrization*. 새 수학이 아니라 *N_t 의 출처에 대한 한 가지 명시적 모델*.

**중요 따름결과**: 이 사실 자체가 *§8-5 ("proxy 아닌 이유") 의 응답을 어렵게* 만든다. $K_{z_t}$ 가 표준 도구 (bilateral filter / diffusion maps / mean-shift) 와 *수식 형태로 동일* 일 뿐 아니라 *canonical N_t 의 parametrized realization* 이므로 — *N_t = 표준 도구의 추상* 이라는 등식이 자동으로 성립. 이는 SCC 가 *외부 도구의 추상* 이 아님을 옹호하는 어떤 주장이든 *N_t 가 표준 도구의 추상이 아니다* 라는 별도 주장을 필요로 한다는 의미. 그러나 canonical 자체는 N_t 의 출처를 *modeling layer 외부* 로 위임 (§3.2) — 따라서 "N_t 가 표준 도구 *아님*" 의 어떤 주장도 SCC 외부 진술이다.

---

## §4. P-12 의 정밀 검사 — T-D0D1-Nonuniformity 가 T8 의 reformulation 인가

**사용자 제안 (`01b §8`)**: "$z_t$ 의 차이가 비균일 $u_t^*$ 를 유도하는 조건."

**canonical T8-Core (Cat A)**: 임계 $\beta/\alpha > 4\lambda_2(L)/\lvert W''(c) \rvert$ 충족 시, $E$ 의 minimizer 는 *uniform field 가 critical 이지만 unstable*, 따라서 *비균일 minimizer 가 존재*. $\lambda_2(L)$ 은 그래프 Laplacian $L = D - W$ 의 spectral gap, $W$ 는 *N_t 로부터 유도된 weight matrix*.

**비교**:
- T8 가설: $N_t$ 의 *spectral 성질 ($\lambda_2$)* 와 double-well curvature ($\lvert W''(c) \rvert$) 의 비교.
- T-D0D1-Nonuniformity 가설: $z_t$ 의 *feature variation* 이 *비균일 $u^*$ 유도*.

**관계**:

만약 T-D0D1-Nonuniformity 가 다음 형태로 형식화되면:

$$\text{(T-D0D1-NU)}: \exists \theta_z \text{ such that, if } \mathrm{Var}_X(z_t) \geq \theta_z, \text{ then } u^*(z_t) \text{ is non-uniform}$$

이는 T8 의 *반대 방향* — T8 은 *graph spectral 조건* 으로부터 비균일성 도출. T-D0D1-NU 는 *feature variation* 으로부터 도출. 두 조건의 관계:

- $z_t$ 의 feature variation 이 *어떻게 $K_{z_t}$ 의 spectral gap 에 영향* — 정량 분석이 필요. 일반적으로 *작은 feature variation* → $K_{z_t}$ 가 *blocky 가 적음* → *$\lambda_2$ 가 작음* → T8 임계 *충족 어려워짐* → *uniform minimizer*.
- 따라서 직관적으로: $\mathrm{Var}_X(z_t) \uparrow \Rightarrow \lambda_2(L_{K_{z_t}}) \uparrow \Rightarrow$ T8 임계 충족 가능 $\Rightarrow$ 비균일 $u^*$.

**판정**: T-D0D1-NU 는 *T8 의 입력층 (feature variation → spectral) 정량화* 형식. 본질적 *수학 내용* 은 T8 의 *전제 조건* 의 한 가지 *명시적 source 모델*. 즉 *T8 의 hypothesis 영역 내 추가 정보* — 새 정리 후보로서는 *T8 의 corollary* 에 가까움.

**비-trivial 가능성**: 만약 *$z_t$ 가 special 한 구조* — 예를 들어 *piecewise constant* (sharp feature boundary) 또는 *power-law spectrum* — 를 가질 때 $u^*$ 의 비균일성에 *quantitative* 한계 (예: cluster 개수의 *상한* 또는 *하한*) 를 줄 수 있다면, 이는 T8 의 *순수 spectral* 조건 너머의 *feature-aware* 정리. 그러나 사용자 메모는 이런 specific 구조를 명시하지 않는다.

**결론**: T-D0D1-NU 는 *현재 형태로는* T8 의 *입력 모델 보강 corollary* — substantive 새 수학 *후보 자격은 있으나* 사용자 메모의 형태로는 미완.

---

## §5. P-9 의 정밀 검사 — DECL-1.0 화살표 시작점 변경 제안

**사용자 표현**: "SCC 가 *진짜* 설명해야 할 것은 D_0 → D_1."

**DECL-1.0 (2026-05-07)** 의 명시적 화살표:

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

이 화살표는 SCC 의 *self-declared scope*:
- *상한*: "감각장면 → 차이의 발생" (D_0 의 발생) 은 *위쪽 외부*.
- *하한*: "이름 / 클래스 부여" (객체 분류) 는 *아래쪽 외부*.

P-9 는 이 화살표의 *상한을 위쪽으로 이동* 하라는 요청 — D_0 의 *발생 자체* 를 SCC 내부로.

**충돌 분석**:

1. DECL-1.0 자체가 사용자가 *2026-05-07 에 명시적으로 결정* 한 self-limitation. P-9 는 그 결정의 *retraction 제안*.
2. DECL-1.0 의 의도된 self-limitation 의 이유 (DECL-1.0 §"이 이론이 아닌 것"):
   - "객체 검출 이론이 아니다" — 즉 sensory pipeline 의 *전반부와 후반부* 모두 *명시적으로 외부화*.
   - "공학적 비전 파이프라인이 아니다. *그 파이프라인의 수학적 정당성을 제공* 한다."
3. P-9 가 채택되면:
   - SCC 는 *공학적 비전 파이프라인* 의 *전반부* (= sensory differentiation) 도 다뤄야 함.
   - 그러나 D_0 의 *수학적 정당화* 는 (a) saliency / PCA / learned fusion 같은 공학 도구 (= CLAUDE.md Constraint #4 위반), 또는 (b) 사용자 메모 §3 의 Gaussian similarity kernel (= 표준 도구의 동일 형태, §8-5 proxy 검증 실패) — 둘 중 하나로 귀결될 가능성 높음.
   - 어느 쪽이든 DECL-1.0 의 self-limitation 의 *설계 이유* 와 정면 충돌.

**판정**: P-9 는 *수학 명제가 아니라 DECL-1.0 의 정책 변경 제안*. 이 변경의 *수학적 결과* 가 (Decision A 가 되려면) 새 수학을 산출해야 하나, P-1, P-10, P-11, P-12 의 분석에 따르면 *그 수학은 N_t parametrization + T8 corollary* 로 환원 — *DECL-1.0 변경의 정당화에는 부족*.

---

## §6. 새 명제 후보의 *정식 수학 형태* (Stage 4 검증 입력)

Stage 4 의 verification 대상 — 본 §6 가 *그 verification 의 입력* 이 됨. 각 후보를 quantifier / 부호 명확한 형태로:

### §6.1 후보 NP-A: T-D0D1-Existence (P-11 의 정식)

> **(NP-A)** 임의의 finite connected graph $G = (X, E)$, 임의의 measurable feature space $(\mathcal{F}, d_\mathcal{F})$, 임의의 함수 $z : X \to \mathcal{F}$, 임의의 mass $m \in (0, \lvert X \rvert)$, 임의의 parameters $\rho, \sigma > 0$, 임의의 SCC parameters $(\lambda_{\mathrm{cl}}, \lambda_{\mathrm{sep}}, \lambda_{\mathrm{bd}}, a_{\mathrm{cl}} \in (0,4), \beta, \alpha)$:
>
> $$E(u; K_z) := \lambda_{\mathrm{cl}} E_{\mathrm{cl}}(u; K_z) + \lambda_{\mathrm{sep}} E_{\mathrm{sep}}(u; K_z) + \lambda_{\mathrm{bd}} E_{\mathrm{bd}}(u; K_z)$$
>
> *(transport 항은 single-time 분석에서 제외)*
>
> attains its infimum on $\Sigma_m = \{u \in [0,1]^X : \sum_x u(x) = m\}$, i.e. $\exists u^* \in \Sigma_m, E(u^*; K_z) = \inf_{u \in \Sigma_m} E(u; K_z)$.

**자체 판정**: NP-A = **trivial Cat A**. 증명: $\Sigma_m$ 은 $[0,1]^X$ 의 hyperplane intersection — finite-dim 에서 compact (closed bounded). $E(u; K_z)$ 는 $u \mapsto E$ 가 polynomial / smooth in $u$ 로 continuous (canonical §7 의 4 항 모두 polynomial in $u$). Weierstrass extreme value theorem 으로 minimum attained. **이는 canonical T-PF-A1-AR (Cat A, CV-1.8) 의 *부분 진술* — 추가 정리 아님.**

### §6.2 후보 NP-B: T-D0D1-Nonuniformity (P-12 의 정식)

> **(NP-B)** Above setting. 정의:
>
> $$\mathrm{Var}_X(z) := \frac{1}{\lvert X \rvert} \sum_x d_\mathcal{F}(z(x), \bar{z})^2, \quad \bar{z} := \arg\min_{w \in \mathcal{F}} \sum_x d_\mathcal{F}(z(x), w)^2$$
>
> Then there exists a function $\Theta: \mathbb{R}^+ \to \mathbb{R}^+$ such that:
>
> $$\mathrm{Var}_X(z) \geq \Theta(\rho, \sigma, \beta/\alpha, \lvert X \rvert) \quad \Longrightarrow \quad u^*(z) \in \arg\min_{\Sigma_m} E(\cdot; K_z) \text{ is non-uniform}$$
>
> i.e. $u^*$ 가 constant 가 아님 (∃ $x, y \in X, u^*(x) \neq u^*(y)$).

**자체 판정**: NP-B = **부분적**.

분석:
1. $\mathrm{Var}_X(z) \uparrow \Rightarrow K_{z}(x,y)$ matrix 가 *block structure* 강해짐 → $L = D - W$ 의 *Fiedler value $\lambda_2$ 증가*.
2. $\lambda_2 \uparrow$ → T8 임계 $\beta/\alpha > 4\lambda_2/\lvert W''(c) \rvert$ *충족 어려워짐* — 따라서 직관 *역방향*: 강한 feature variation 이 비균일 $u^*$ 을 *방해* 할 수 있음.
3. 또는 *반대로*: $K_{z}$ 가 disconnected 에 가까워지면 (예: $\sigma \to 0$ 으로 cross-cluster edge weight $\to 0$) → *T8 와 무관한 분리* — 그래프가 *실질적으로 multiple component*. 이 regime 에서 비균일 $u^*$ 자명 (각 component 에 mass 분배).

**판정 1 (분석 1+2)**: T8 hypothesis 영역 내에서 NP-B 는 T8 의 corollary — 새 수학 아님.

**판정 2 (분석 3)**: $K_z$ 가 disconnected approach → graph theoretic trivial — 새 수학 아님.

**둘 다 새 수학 아님**. 단지 T8 의 입력 데이터에 대한 *모델 dependent* 정량화. NP-B 의 substantive 새 내용은 *현재 형태로 부재*.

**Cat 자기 분류**: Conjecture (증명 시도 안 했으나 trivial corollary 의심).

### §6.3 후보 NP-C: $K_{z_t}$ 가 N_t 와 *수학적으로 구별* 됨 (P-10 + §8-5 응답)

> **(NP-C)** $K_{z_t}$ 의 어떤 *수학적 성질* $P$ 가 존재하여, 일반 $\mathbf{N}_t$ 가 (B1-B4 만 만족) $P$ 를 일반적으로 만족하지 못함. 그래서 $K_{z_t}$ 가 SCC 의 *진정한 새 primitive* 임.

**자체 판정**: NP-C = **반증** (Stage 3 §3 의 결과). $K_{z_t}$ 는 B1-B4 를 만족하는 *N_t 의 한 family*; B1-B4 외에 *추가 성질* 이 명시되지 않음. 따라서 $K_{z_t}$ family 는 N_t family 의 *parametrized subset*. $P$ 의 후보가 사용자 메모에 없는 한 NP-C 는 *vacuous*.

### §6.4 후보 NP-D: $\mathcal{E}(u; K_z) \neq E_{\mathrm{spectral-clustering}}(u; K_z)$ — *§8-5 의 변형*

> **(NP-D)** SCC 의 energy $\mathcal{E}(u; K_z)$ 가 spectral clustering / mean-shift / bilateral filter 의 *어떤* 표준 objective 와도 *수학적으로 구별*.

**분석**:
- Spectral clustering objective: $\min_{u \in \{0,1\}^X, \lvert u \rvert=k} u^T L u$ — *Boolean indicator + Ncut style*. SCC 의 $u \in [0,1]^X$ continuous + 4 항 energy 와 *명백히 다름*.
- Bilateral filter: *non-variational* — direct iterative update $u_{t+1}(x) = \sum_y K_z(x,y) u_t(y) / \sum_y K_z(x,y)$. SCC 의 *energy gradient flow* 와 다름.
- Mean-shift: *mode finding* on density $p(z) = \sum K_z(x, \cdot)$. SCC 의 $u$-field 와 *카테고리 다름* (mean-shift 는 site 가 아니라 mode 을 반환).
- Diffusion maps: spectral *embedding*, not clustering. SCC 와 *목적 다름*.

**판정**: NP-D = **TRUE Cat A**. 즉 *energy + closure + boundary + transport* 의 SCC 4-항 구조는 *kernel 만 공유하는 표준 도구와 명백히 다른 수학*. 그러나 — 이 사실은 **canonical CV-1.16 의 §7 (Energy) 와 §6 (Axiomatic Groups) 의 자동 결과**. 즉 NP-D 는 *이미 canonical 에 의해 (간접적으로) 보장됨* — 별도 정리로 등재할 필요 없음.

**중요**: NP-D 가 TRUE 라는 사실은 *SCC 의 정체성을 보존* 한다. 그러나 이는 *$z_t$ 도입과 무관* — *N_t 가 어디서 오든* SCC 의 energy 가 표준 도구와 다른 한 SCC 는 SCC. 따라서 NP-D 는 *$z_t$ 가 새 primitive 임의 정당화* 가 아니라 *canonical SCC 의 정체성의 정당화*.

### §6.5 새 명제 후보 요약

| 후보 | 형태 | 새 수학 여부 | Stage 4 verification 필요 |
|---|---|---|---|
| **NP-A** (T-D0D1-Existence) | trivial Weierstrass | ❌ 새 수학 아님 | 검증 불필요 (자명) |
| **NP-B** (T-D0D1-Nonuniformity) | T8 corollary 후보 | ❌ T8 의 input 모델 — 부분 새로움 가능성 미명시 | Stage 4: T8 와 *strict* 다름인지 검증 |
| **NP-C** ($K_{z_t}$ 가 N_t 와 구별) | vacuous | ❌ B1-B4 를 모두 만족 — 구별 없음 | 검증 결과 부정적 (이미) |
| **NP-D** (SCC ≠ 표준 도구) | canonical 자동 결과 | ❌ 이미 canonical (간접) | 별도 정리 불필요 |

**Stage 3 의 결정적 사실**: 새 명제 후보 NP-A ~ NP-D 중 *어느 하나도* canonical CV-1.16 외부의 *substantive 새 수학* 을 산출하지 못함.

---

## §7. Stage 3 → Stage 4 연결 메모

Stage 3 confrontation 표 (§2) 의 12 명제 중:
- **6개 (P-2 ~ P-7)**: 이미 담김.
- **2개 (P-1, P-8)**: canonical 외부 (DECL-1.0 의 명시적 self-limitation).
- **3개 (P-6, P-10, P-12)**: 부분적 — 그러나 §3, §4, §6 정밀 분석에서 모두 *새 수학 아님 / parametrization / corollary* 로 환원.
- **1개 (P-9)**: DECL-1.0 변경 *제안* (수학 명제 아님).

**Stage 4 (`05_verification_question.md`) 의 작업**:

Stage 3 §6 의 새 명제 후보 NP-A ~ NP-D 의 *최종 검증*:
- NP-A: trivial 확인 (자체 sketch 증명).
- NP-B: T8 와의 관계 *수치 또는 분석적* 정밀 비교 — *T8 너머 인지*.
- NP-C: vacuous 확인 (이미).
- NP-D: canonical 의 자동 결과 확인.

추가로: **archive (V-AFD, R-2) 의 명제와의 동일성 비교**. NP-A ~ NP-D 가 V-AFD 의 어떤 정리 또는 R-2 의 어떤 lemma 와 *동일* 한지.

---

*Stage 3 종료. Stage 4 (`05_verification_question.md`) 진입.*
