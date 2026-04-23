# 01 — Exploration: Restatement · Multi-Approach · Primary Selection

**Session:** 2026-04-23
**Target (from plan.md):** Stage 2 Axiom Audit 후속. P0 = {G1 Three-Layer classification of 77 Cat A, G2 SCC transitions의 수학 함수 taxonomy, G3 Single→Multi Formation Quantization 확장}. P1 = {G4 time evolution, G5 thermal softmax}. P2 = {G6 application scoping}.
**This file covers:** 문제 재진술, 각 goal별 3+개 접근 생성, primary 선택 근거.
**Depends on reading:** `canonical.md` §2–§3 (axioms), §11 (fixed commitments), §13 (Cat A/B/C registry), §14 (CN1–CN14); `working/SF/step_cohesion.md` (F1-SSU-v5 Formation Quantization); `working/MF/from_single.md` (§2 RETRACTED, §4–§7 preserved); `logs/daily/2026-04-22/99_summary.md` (R22 synthesis, 4 falsifications, 72 preserved static Cat A).

---

## §1. Session 소관 재진술 (Restatement)

### 1.1 plan.md의 암묵적 가정 표면화

plan.md는 `§1`에서 6개의 병렬 goal (G1–G6)을 나열하고, `§3`에서 우선순위 (P0/P1/P2)를 부여한다. Prompt template의 "단일 target open problem" 기대와 달리, **오늘의 세션은 multi-goal synthesis**이며, 각 goal은 독립적 deliverable을 요구한다. 이 불일치는 prompt §6의 파일명 규약 (`01_exploration / 02_development / 03_integration`)을 수정하게 만든다 — goal 수만큼 본문 파일을 갖되, exploration + integration + summary는 유지.

plan.md가 **암묵적으로 가정하는 것**:

- **A1** (plan §2 G1): 어제 세션에서 산출된 "77 Cat A" 수는 정확하며, 이들 각각이 Layer 1/2/3 중 **정확히 하나**에 할당 가능하다. → 실제 audit이 필요. "mixed" 또는 "layer-bridging" 범주가 불가피할 수 있다 (§1.3 참조).
- **A2** (plan §2 G2): 모든 SCC transition이 유한 개의 수학 함수 클래스 (6–7개) 중 하나로 **깔끔히** 분류된다. → 불명확. Transition이 조건에 따라 형태 변경 (sigmoid → Heaviside as $\sigma \to 0$) 가능성이 있어, taxonomy는 **형태 단일성**보다 **morphological transitions** 관점이 더 정확할 수 있음.
- **A3** (plan §2 G3): Single-formation Formation Quantization (FQ, `step_cohesion.md` §1) framework이 $K \geq 2$로 **자연스럽게** 확장된다. → 확장의 "자연스러움" 기준은 무엇인가? (i) Axiom S1–S4가 그대로 적용되는가, (ii) proof structure가 단순 K-인덱싱으로 확장되는가, (iii) 새 수학적 대상 (moduli, pair interaction)이 기존 프레임워크와 호환되는가 — 세 기준 모두에 관해 답해야 함.
- **A4** (plan §2 G4–G5): Zero-temperature gradient-flow framework을 **finite-T Langevin**으로 그대로 승격 가능하다. → 현재 canonical은 `b_D = 0` (CN13) analyticity commitment에 의존. Noise 추가는 Łojasiewicz convergence 구조를 **근본적으로** 수정함. Metastability의 kinetic 해석 (CN6, CN8)과의 관계도 재검토 필요.
- **A5** (plan §2 G6): Cognitive / segmentation / community detection이 SCC의 단순 application이다. → §12 오류 패턴 주의사항에 의거 **reductive 환원 금지**. "이것은 결국 clustering이다"가 아닌 **contrastive** comparison으로 제한.

### 1.2 성공 / 실패 기준 (내가 부과하는 명시화)

**성공 (at session close)**:
- G1: 77 Cat A claim 전원에 Layer 1/2/3/mixed/ambiguous 할당 완료. "mixed" 또는 "ambiguous"도 정당한 할당으로 인정 (silent resolution 회피).
- G2: 최소 6개 함수 클래스 × SCC transition 매핑 + 각 class의 정의역·공역·regularity·asymptotic characterization.
- G3: FQ framework의 K-sector 분해 + multi-K 확장의 **세 가지 수학적 구조** 중 최소 두 개 제시 (basin stratification / moduli space / pair interaction / Landau free energy) + 확장의 **자연성 기준 평가**.
- G4, G5: 최소 2개 Cat C hypothesis + 각 hypothesis의 검증 가능 조건.
- G6: 구체적 실험 설계 3개 (입력 데이터 · 기대 출력 · 성공 기준 명시).

**실패 (trigger premature termination)**:
- canonical §2 commitment (u-primitive, 4-term energy, closure non-idempotence) 중 하나라도 silent하게 위반됨.
- K=1 global min을 "문제"로 재주장 (§12 예상 오류 1).
- Open problem (F-1, M-1, MO-1, N-1) 중 today의 target이 아닌 것을 silent resolve.

### 1.3 "Layer 할당"의 엄밀화 (G1 기반)

plan.md G1은 "77 Cat A를 Layer 1/2/3으로 정확히 분류"를 요구하지만, Three-Layer Hierarchy (`step_cohesion.md` §3)는 **기술적 정의보다 개념적 organizational device**에 가깝다. 엄밀한 할당 기준을 여기서 정립:

> **정의 (Layer assignment, this session)**:
> claim $P$에 대해 Layer $\ell \in \{1, 2, 3\}$ 할당:
>
> - **Layer 1 (topology)**: $P$의 statement가 **정수 $K$, basin label, connected component count, topological invariant** (Euler characteristic, Morse index 부호만) 만 다룬다. $P$는 protocol-selection 또는 basin structure에 관한 **discrete** 주장이다.
> - **Layer 2 (geometry)**: $P$의 statement가 **smooth real-valued quantity** ($r_0, \xi_0, d_{\min}, \mu_k$, 에너지 값, scaling exponent)를 다룬다. Layer 1에 해당하는 discrete 구조는 고정되어 있다고 가정하고 within-basin or within-K-sector properties만 진술한다.
> - **Layer 3 (field)**: $P$의 statement가 **continuous field $u(x) \in [0,1]$의 pointwise 또는 Sobolev-type property** (profile $\phi_k^*$의 형태, Allen-Cahn equation, Γ-convergence, analyticity)를 다룬다.
> - **Mixed $(\ell_1, \ell_2)$**: $P$의 statement가 **두 layer의 quantity 간 bridge**이다 (예: "Layer 2의 $\xi_0 = \sqrt{\alpha/\beta}$가 Layer 3의 tanh profile 폭을 결정한다").
> - **Ambiguous**: $P$의 statement가 고전 canonical (v1.2) 어휘로만 기술되어, Three-Layer로 재분류 시 추가 조건 없이는 할당 불가.

이 정의 하에 "mixed" 및 "ambiguous" 항목은 **정당한** 결과이며, 이들의 존재 자체가 Stage 2 Axiom Audit의 산출물이다.

### 1.4 "함수 taxonomy"의 단일성 한계 (G2 기반)

G2의 "함수 class × SCC 현상 매핑"은 **class가 disjoint이며 fit이 unique함**을 암묵적으로 가정한다. 하지만 실제로는 (i) 하나의 transition이 다른 regime에서 다른 class로 나타나고 (예: basin escape rate는 T > 0에서 log-divergent, T = 0에서 step), (ii) 하나의 class가 여러 transition에 동시에 맞는다 (tanh는 interface profile과 logistic 근사 모두에 해당). 따라서 taxonomy는 **함수 class → SCC 현상의 many-to-many 매핑**으로 설계해야 하며, **mapping의 conditionality**를 명시해야 한다.

### 1.5 "자연스러운 확장"의 기준 (G3 기반)

Single → Multi 확장의 "자연스러움"을 다음 세 기준으로 decompose:

- **Axiomatic naturality (AN)**: Axiom S1–S4 (step_cohesion.md §10.1)이 K-indexed 형태로 수정 없이 적용되는가.
- **Proof-structural naturality (PSN)**: Single-formation proof가 "$\sum_k$"를 추가하는 것 외의 새 수학적 도구 없이 K로 확장되는가.
- **Observable naturality (ON)**: Single-formation의 observable (e.g. $\widehat K = 1$ K̂ counter)가 multi에서 $\widehat K \geq 2$의 counter로 직접 재사용되는가.

세 기준 전부 만족 시 "완전 자연스러운", 두 개 만족 시 "부분 자연스러운", 한 개 이하 시 "불연속 확장" (new framework required).

---

## §2. Goal 1 (Layer classification) — Multi-approach

### 2.1 Approach A1: Statement-syntactic classification

**Core idea**: 각 Cat A claim의 **statement 본문에 등장하는 quantity의 type**으로 할당 결정. ($K \in \mathbb{Z} \Rightarrow$ Layer 1; $r_0, \xi_0, \mu_k \in \mathbb{R} \Rightarrow$ Layer 2; $u(x) \in [0,1]^n \Rightarrow$ Layer 3.)

- **성공 결과물**: 깔끔한 1:1 테이블, 77 × 1 column ($\ell$).
- **실패 모드**: Claim이 여러 type의 quantity를 혼합할 때 (e.g., T-Birth-Parametric: "$\beta_{\mathrm{crit}}$에서 $K=1 \to 3$ pitchfork", $K$ topological + $\beta$ real + amplitude $\propto (\beta-\beta_c)^{1/2}$ field-level). "Mixed" 할당 남용 위험.
- **canonical 상호작용**: canonical §13의 기술이 어떤 layer 구분도 명시하지 않으므로, 이 접근은 retrofitting이다. §2의 axiom formulation과 상호작용 적음.

### 2.2 Approach A2: Proof-dependency classification

**Core idea**: 각 claim의 **proof tool**로 할당. Topological proof (connectedness, Euler, Morse index) $\Rightarrow$ Layer 1; geometric/scaling argument $\Rightarrow$ Layer 2; PDE / Γ-convergence / analyticity $\Rightarrow$ Layer 3.

- **성공 결과물**: 각 claim에 "proof tool" + "layer" 두 컬럼 테이블. Stage 2 Axiom Audit에서 각 layer가 의존하는 공리 집합 추출 가능.
- **실패 모드**: 하나의 proof이 여러 도구를 섞는 경우 (e.g., T8-Core: spectral + variational + Γ-convergence). Proof이 reformulation 가능하면 layer도 바뀔 수 있어 불안정.
- **canonical 상호작용**: canonical §13에 proof sketch가 이미 서술되어 있어 이 접근은 실행 가능. 단, 일부 claim은 proof이 축약되어 있어 dependency 추론이 애매.

### 2.3 Approach A3: Observable-role classification

**Core idea**: claim이 궁극적으로 어떤 **observable**를 특성화하는가로 할당. $K$-counting observable에 관여 $\Rightarrow$ L1; $(r_0, \xi_0, d_{\min})$ measurement에 관여 $\Rightarrow$ L2; $u$-field reconstruction에 관여 $\Rightarrow$ L3.

- **성공 결과물**: observable-centric view. 각 layer의 "what do we measure"가 명확.
- **실패 모드**: observable이 명시적이지 않은 claim (존재정리, 일관성 정리)에 할당 애매. 예: T20 (Axiom Consistency)은 observable이 없음 → "meta-layer" 필요할 수 있음.
- **canonical 상호작용**: canonical §5 (Derived Geometric and Morphological Notions)의 observable 정의와 연결됨.

### 2.4 Approach A4: Static/dynamic-bifurcated classification

**Core idea**: R22 (§17.6) Static/Dynamic Separation Principle을 주 축으로 삼고, **static claim**과 **dynamic claim**을 먼저 분리한 후 각 그룹 내에서 sub-layer 할당.

- **성공 결과물**: 2 × 3 grid (static/dynamic × L1/L2/L3), 그리고 "mixed", "meta"는 off-grid. R22의 empirical decoupling 발견을 classification에 반영.
- **실패 모드**: Static vs dynamic 기준이 자체로 논쟁적 ("existence of minimizer"는 static, "gradient flow convergence"는 dynamic — 하지만 Łojasiewicz는 analytic property이므로 static의 결과).
- **canonical 상호작용**: canonical §13의 erratum이 이미 "static vs kinetic" 구분을 일부 도입 (CN6, CN8). 이 접근은 그 구분을 classification axis로 **승격**.

### 2.5 Primary selection (G1)

**선택: A2 × A4의 하이브리드.**

- A2 (proof-dependency)는 객관성·검증가능성 측면에서 우수 (canonical §13의 proof sketch가 일차 자료).
- A4 (static/dynamic bifurcation)는 R22의 empirical finding과 정합성이 가장 높음.
- A1 (syntactic)는 빠르지만 claim의 의미를 소실시킴 — 보조로 사용.
- A3 (observable)은 observable-absent claim 처리에 취약함 — 제외.

**Hybrid 적용 규칙**:
1. 먼저 static/dynamic 구분 ($\exists$ gradient-flow / time / stochastic → dynamic; else static).
2. Static 그룹 내에서 proof tool 기반 L1/L2/L3.
3. Dynamic 그룹 내에서 동일.
4. Bridge claim (layer간 연결 주장)은 "mixed $(\ell_1, \ell_2)$".
5. Meta (axiom consistency, existence 결과 without observable)는 "meta".

Fallback 대안: A2 단독 (static/dynamic 구분이 애매한 경우). A1은 disambiguation용으로만.

**Primary가 실패하면**: A1으로 전환하여 syntactic assignment로 대체. "Mixed" 비율이 30%를 초과하면 Three-Layer framework 자체의 충분성 재검토 (이는 NQ-49의 확장).

---

## §3. Goal 2 (Function taxonomy) — Multi-approach

### 3.1 Approach B1: Forward (class → SCC 현상)

**Core idea**: 6–7개 함수 클래스를 먼저 정하고, 각 class에 대해 SCC 내에서 **instance**를 찾는다.

후보 class: {Heaviside step, logistic sigmoid, tanh soliton, log-divergent, softmax, rational/algebraic, power-law}.

- **성공 결과물**: class-centric 카탈로그. 각 class의 수학적 property (regularity, asymptotic, 유도함수)를 일관되게 서술.
- **실패 모드**: Class가 overlap (tanh는 logistic의 scaled version) 또는 class가 빈 instance를 가질 때 (power-law는 finite-size lattice에서 pure power-law 없음).
- **canonical 상호작용**: canonical §13의 이미 확정된 scaling (T8-Core의 phase transition, T11 Γ-convergence)을 class 인스턴스로 사용.

### 3.2 Approach B2: Reverse (SCC 현상 → class)

**Core idea**: SCC의 주요 transition (pre_brainstorm §1.1의 7개 항목) 각각에 대해 **best-fit class**를 empirically/analytically 선택.

- **성공 결과물**: 현상-centric 카탈로그. 각 현상에 대해 유일한 best-fit class와 근거.
- **실패 모드**: 같은 현상이 다른 parameter regime에서 다른 class를 보인다 (R20 β=9 bistable region: deterministic이면 Heaviside, noisy면 softmax). 단일 class 고정은 부정확.
- **canonical 상호작용**: canonical에 "현상 → class" 식 매핑이 명시적이지 않아 새로운 perspective 제공.

### 3.3 Approach B3: Morphological transition graph

**Core idea**: 각 현상이 parameter regime에 따라 class를 **변경**한다는 점을 그래프로 구조화. Nodes = 함수 class, edges = regime transitions. 하나의 현상은 edge sequence.

- **성공 결과물**: 현상별 "morphological trajectory" — 예: basin escape at $T \to 0$은 log-divergent → step (finite $T$에서는 log); Layer 1 selector는 Heaviside → sigmoid with $\sigma > 0$.
- **실패 모드**: Graph 구성이 artistic하고 자의적일 수 있음. Regime transition points가 canonical에 명시되지 않은 경우 empirical anchor 부족.
- **canonical 상호작용**: R20 $N_{\mathrm{unst}}$ saturation 발견, R22 V5 hysteresis에 의해 transition points 일부 empirical 확인 가능.

### 3.4 Approach B4: Asymptotic scaling classification

**Core idea**: SCC의 모든 transition을 asymptotic scaling exponent (e.g., $p$, $\gamma$, $\nu$)로만 서술. Class는 scaling 패턴 (폴리노미얼, 지수, 로그)으로 정의.

- **성공 결과물**: Landau-Ginzburg 스타일의 exponent table.
- **실패 모드**: 많은 SCC 현상이 finite-size, non-universal (R21 $p = 5.0$ saturated 관측). Pure scaling은 large-system limit 가정.
- **canonical 상호작용**: canonical T8-Core의 $\beta_{\mathrm{crit}} = 4\alpha\lambda_2/|W''(c)|$는 scaling 형태로 해석 가능. 대부분의 다른 Cat A는 constant-level statement.

### 3.5 Primary selection (G2)

**선택: B3 (morphological transition graph)을 primary, B1 (forward class catalog)을 secondary로.**

- B3은 pre_brainstorm §1.3의 "SCC 현상 ↔ class" 매핑이 parameter-regime-dependent라는 관찰을 **그래프 형태로 정식화**. R17/R19/R20/V7 P1의 falsification cascade가 "단일 class를 현상에 고정하면 reality와 불일치"를 보였음 — 이 실패를 구조적으로 피하는 설계.
- B1은 각 class의 수학적 property를 깔끔히 서술하는 reference 카탈로그로 B3의 보조.
- B2 (reverse)는 B3의 node lookup으로 흡수.
- B4 (asymptotic)은 finite-size artifact 때문에 SCC에는 부적합.

**Primary가 실패하면**: B1 + B2의 단순 table로 회귀. "Morphological transition"이 너무 복잡하면 각 현상을 **primary class + fallback classes** 형태로 단순화.

---

## §4. Goal 3 (Single → Multi extension) — Multi-approach

### 4.1 Approach C1: K-sector basin stratification

**Core idea**: $\Sigma_m = \bigsqcup_{K \geq 0} \mathcal{B}_K$ (basin decomposition by K). 각 $\mathcal{B}_K$ 내부에서 single-formation 이론을 K-copy한다.

- **성공 결과물**: K-sector 내부 구조는 single-formation theory × K. Basin boundary는 Layer 1 protocol-selector. Axiom S1–S4가 직접 K-인덱싱으로 확장.
- **실패 모드**: Basin stratification의 수학적 well-posedness — $\mathcal{B}_K$가 open/connected/manifold-like인가? Boundary는 측도 0인가? (MO-1과 재충돌 가능성).
- **canonical 상호작용**: canonical §11 Multi-formation paradigm과 정합. T-Persist-K-Sep (Cat A)가 $\mathcal{B}_K$ 간 mapping으로 해석 가능.

### 4.2 Approach C2: Configuration moduli space $\mathcal{M}_K$

**Core idea**: K-formation configuration space $\mathcal{M}_K = \{(A_1^*, \ldots, A_K^*) : \sum |A_k^*| = m\} / \mathrm{Aut}(G)$. Multi-formation structure = moduli space structure.

- **성공 결과물**: $\mathcal{M}_K$의 dimension·topology·singular locus를 명시. K=2의 $\mathcal{M}_2$는 R11에서 parameterized됨 (position + size).
- **실패 모드**: $\mathcal{M}_K$의 정확한 정의가 formation support $A_k^*$의 discrete/soft 구분에 민감. Soft formation이면 $\mathcal{M}_K$는 $\Sigma_m$의 submanifold로 embedded, "configuration space"가 아니라 continuous orbit.
- **canonical 상호작용**: canonical §13 Theorem 3.1 Stratified Morse와 연결. G-D symmetry_moduli (R4/R5) 확장.

### 4.3 Approach C3: Pair interaction + Landau free energy

**Core idea**: K≥2 landscape를 **effective Landau energy** $F(K; \beta, c, G) = K \cdot F_{\mathrm{single}} + \binom{K}{2} F_{\mathrm{pair}}$로 근사. Pair interaction은 screened Poisson decay $\sim e^{-d/\xi_0}$.

- **성공 결과물**: $F(K)$의 minimizer $K^*$가 자연스러운 $\widehat K$ 예측. R12 Cat A Hessian block-diagonal + $\mu_{\mathrm{sep}}$ 결과와 직접 연결. 수학적 단순성 우수.
- **실패 모드**: Pair-only 근사가 triple/multi-body coupling을 놓침 (pre_brainstorm §7 위험). R17/R19/R20이 "K 예측 공식"을 반증했으므로, $F(K)$가 **observed** $\widehat K$와 반드시 일치하지 않음 (protocol-dependence).
- **canonical 상호작용**: canonical §12 Coupling Bound Lemma (Cat A)와 직접 연결. T-Merge (b) isoperimetric ordering은 $F_{\mathrm{single}}$ 부분.

### 4.4 Approach C4: Inter-sector transition dynamics

**Core idea**: $\mathcal{B}_K \to \mathcal{B}_{K+1}$ transition (nucleation) 및 $\mathcal{B}_K \to \mathcal{B}_{K-1}$ (merger)의 rate를 Kramers-type으로 계산. Multi-formation structure를 **static landscape + transition rates** 쌍으로 기술.

- **성공 결과물**: 각 K-sector가 "어떻게 떠나고 어떻게 들어오는가"를 수량화. Time-evolution G4와 자연스럽게 연결.
- **실패 모드**: Zero-T deterministic setup에서는 rate = 0 또는 ∞만 존재. Finite T framework (P-F, 여전히 open)가 전제됨 — metastability with escape rate는 P-F 부재 하에 엄밀히 주장 불가.
- **canonical 상호작용**: canonical §11 Three Pillars of Kinetic Multi-Formation (Pillars II/III)과 직접 연결. T-Persist-K-Sep이 "Sector 안에서의 persistence"를 다룸, C4는 "sector 간 transition"을 보완.

### 4.5 Approach C5: Group-theoretic K-reduction

**Core idea**: Multi-formation을 single-formation on the quotient graph $G/\sim$ (where $\sim$는 K-formation support symmetry)로 환원. $\mathrm{Aut}(G)$가 non-trivial 할 때만 유효.

- **성공 결과물**: K가 $\mathrm{Aut}(G)$-orbit 크기로 결정. G-D 확장 (R4, R5, R8)의 자연스러운 일반화.
- **실패 모드**: Generic graph는 $\mathrm{Aut}(G) = \{e\}$ → K 축소 불가. Regular lattice에만 적용 가능해 일반성 제약.
- **canonical 상호작용**: canonical §13 Proposition 1.1 / Theorem 3.1 Stratified Morse의 G-D 성분과 연결.

### 4.6 Primary selection (G3)

**선택: C1 (basin stratification) primary, C3 (pair + Landau) secondary.**

- C1은 Axiom S1–S4를 직접 K-인덱싱으로 확장 가능한 **구조적 뼈대**. 성공/실패가 axiomatic framework 평가에 즉시 반영.
- C3는 C1의 **quantitative instantiation** — $F(K)$가 K-sector 내부 구조에 값을 부여. R22 Cat A 중 C-FQ가 C1, T-Merge + Coupling Bound가 C3의 핵심 재료.
- C4 (transition dynamics)는 G4/G5와 중복, 거기서 다룸.
- C2 (moduli)는 C1의 한 구성요소로 흡수 (basin $\mathcal{B}_K$의 interior parameterization).
- C5 (group-theoretic)은 special case로, primary development의 subsection으로 편입.

**Primary가 실패하면**: C3 단독 Landau 접근으로 회귀. Basin structure가 너무 수학적으로 무거우면 $F(K)$ minimization만으로 "K-selection"을 다룸 (그러나 R20 decoupling과 충돌 가능성 주의).

---

## §5. Goal 4/5 (Time evolution, Thermal) — Multi-approach (compact)

시간 제약상 간략히. G4, G5는 plan.md에서 P1 (scoping level, Cat C hypothesis generation)이므로 multi-approach는 exploration depth를 의도적으로 줄임.

### 5.1 G4 approach candidates

- **D1 (Sharp interface + MCF)**: $\beta \to \infty$ limit에서 formation boundary의 motion by curvature. Γ-convergence (T11 Cat A) 자연 확장.
- **D2 (Allen-Cahn gradient flow)**: Finite $\beta$, $\partial_t u = -\Pi_{\Sigma_m} \nabla \mathcal{E}$. T14 Cat A의 long-time 확장.
- **D3 (LSW coarsening)**: Large-time multi-formation의 scaling. 2D에서 $\langle r \rangle \sim t^{1/3}$ classical. SCC corrections는 CN14 closure-barrier에 의존.
- **D4 (Nucleation via Kramers)**: Zero → one formation transition. Critical nucleus energy + Kramers rate. 그러나 zero-T 엄밀.

**Primary**: D1 (MCF)를 Γ-convergence 확장 + D3 (LSW) scoping. D4는 thermal G5에서 다룸.

### 5.2 G5 approach candidates

- **E1 (Langevin dynamics)**: $du = -\nabla \mathcal{E}\,dt + \sqrt{2T}\,dW$. Gibbs invariant measure $\mu_T \propto e^{-\mathcal{E}/T}$.
- **E2 (Basin occupation softmax)**: 평형에서 $P(\mathcal{B}_k) \propto e^{-E_k^*/T}$. 단, R22 V7 P1 refutation 고려.
- **E3 (Kramers escape rate)**: $\tau_{k \to k'} \sim \exp(\Delta\mathcal{F}/T)$. Nucleation barrier와 merger barrier의 구분.
- **E4 (Selector sigmoid-smoothing)**: Layer 1 Heaviside가 $T > 0$에서 sigmoid로 smoothed. Width $\propto T^\gamma$.

**Primary**: E1 (framework) + E4 (concrete prediction). E2는 V7 P1 refutation이 basic softmax를 배제했으므로 **제한적**으로만 (landscape가 Layer-1 quantized이지 Layer-3 Gibbs가 직접 $P(K)$를 주지 않음).

---

## §6. Goal 6 (Application scoping) — Multi-approach (brief)

- **F1 (Cognitive perception)**: SCC $\widehat K$ ↔ "number of objects observed" (Miller 7±2). Contrastive, not reductive.
- **F2 (Image segmentation)**: SCC gradient flow on pixel graph. Mumford-Shah / Chan-Vese와의 **구조적** 대조 (무엇이 다른가).
- **F3 (Community detection)**: SBM graph에서 $\widehat K = K_{\mathrm{block}}$ 검증. Empirical testable.
- **F4 (Pattern formation analog)**: Turing / Cahn-Hilliard와의 대조. 단순 환원 금지.

**Primary**: F2 + F3 (구체적 empirical 실험 설계 가능). F1, F4는 interpretive contextualization만.

---

## §7. Primary approach summary table

| Goal | Primary | Secondary | Deferred/Absorbed |
|---|---|---|---|
| G1 | Proof-dependency × Static/Dynamic (A2 × A4) | Syntactic (A1) as disambiguation | Observable-role (A3) |
| G2 | Morphological transition graph (B3) | Forward class catalog (B1) | Reverse (B2, absorbed), Asymptotic (B4, inadequate) |
| G3 | K-sector basin stratification (C1) | Pair + Landau free energy (C3) | Moduli (C2, absorbed), Group-theoretic (C5, subsection) |
| G4 | Sharp interface MCF (D1) + LSW scoping (D3) | Allen-Cahn (D2) | Nucleation Kramers (D4, moved to G5) |
| G5 | Langevin (E1) + Selector smoothing (E4) | Kramers rate (E3) | Basin softmax (E2, restricted after V7 P1) |
| G6 | Segmentation contrast (F2) + SBM community (F3) | Cognitive analogy (F1, interpretive) | Pattern formation analogy (F4, contrastive only) |

---

## §8. Alternatives preserved (not discarded)

후속 세션에서 primary 실패 시 재활성화 가능:

- **G1의 A3 (Observable-role)**: Observable layer를 3rd axis로 추가해 3D classification으로 확장할 수 있음.
- **G2의 B4 (Asymptotic scaling)**: Large-graph limit이 실험적으로 가능한 세션에서 재활성.
- **G3의 C4 (Inter-sector transitions)**: G4 time evolution과 merge할 때 재활성.
- **G3의 C5 (Group-theoretic K-reduction)**: Regular lattice 전용 결과가 필요할 때.
- **G5의 E2 (Basin softmax)**: Protocol이 equilibrium에 도달 (slow annealing) 시 여전히 유효.

---

## §9. 본 세션의 non-trivial 가정 (surface-level)

Primary approach 실행에 앞서 다음 가정을 명시:

1. **72 "preserved static Cat A" + 5 R22 new = 77 수**는 R22 session의 자가 집계값이므로 정확성 재검증 필요. 실제 실행 중 sanity check 수행.
2. **R22의 Three-Layer Hierarchy는 "true" framework**이라는 가정은 잠정적. Stage 2 Axiom Audit의 출발점이지 최종 구조가 아님. 분류 중 framework 자체의 수정 제안이 나올 수 있음.
3. **canonical v1.2는 frozen state** (수정 금지, 제안만). 그러나 현재 canonical과 working/logs 사이 괴리 (F-1/M-1/MO-1 dissolution이 canonical에 반영 안 됨)가 있으므로, 이 세션의 classification은 **working state 기준** (R22 + canonical 최선의 synthesis).
4. **Protocol specification language (NQ-50)**이 아직 canonical에 없으므로, dynamic claim 분류 시 "protocol $\pi = $ Fiedler/random/warm-start" 정보를 inline으로 기입.

---

## §10. 이후 파일 계획

- `SF_layer_classification.md` — G1 deliverable (77 Cat A table + layer assignment rationale).
- `SF_function_taxonomy.md` — G2 deliverable (6+ function classes + morphological transition graph).
- `MF_multi_quantization.md` — G3 deliverable (K-sector basin + Landau $F(K)$ + axiom naturality audit).
- `T_time_evolution.md` — G4 deliverable (MCF + LSW hypotheses, Cat C).
- `T_thermal_softmax.md` — G5 deliverable (Langevin + selector smoothing, Cat C).
- `A_application_scoping.md` — G6 deliverable (segmentation + SBM + 3 experiment designs).
- `03_integration_and_new_open.md` — canonical integration + silent-resolution audit + new open questions.
- `99_summary.md` — 세션 요약 + 내일 plan 권고.

**End of 01_exploration.md.**
