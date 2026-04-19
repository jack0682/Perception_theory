# Open Problems — 재프레이밍 (2026-04-19)

**Status:** exploring
**Canonical refs:** `THEORY/canonical/canonical.md` v1.2 §3, §6, §8, §11, §12, §14 (CN5, CN6, CN7)
**Method:** 5-way 병렬 — bottom-up / axiom stress / implicit assumption / top-down ontology / external comparison
**Goal:** F-1 / M-1 / MO-1 언어를 일체 사용하지 않고 현 이론의 실제 미해결 지점을 재명명·재발견. 마지막 §에서 기존 3 문제와 교차 대조.

---

## 0. 고착화의 징후 (왜 기존 관점이 갇혀있었는가)

`THEORY/canonical/open_problems.md` 전체를 다시 읽으면 15+ 문제 중 **critical 3건이 모두 K=1 vs K=2 에너지 비교**에 집중되어 있다. F-1/M-1/MO-1은 서로 다른 세 문제로 보이지만 실제로는 **하나의 깊은 문제의 세 얼굴**이다 (§9에서 전개). 1년 가까이 이 언어에 갇혀있었기 때문에, 이 하나의 깊은 문제를 해소해야 풀리는 다른 층위의 문제들이 안 보였다.

또 하나의 징후: **Category C 5개 중 4개가 K-field 관련** (T-Persist-K-Sep, T-Persist-K-Weak, T-Persist-K-Unified, T-Persist-1(d)). K 문제가 해결되면 조건부 정리들이 연쇄적으로 격상될 수 있다. 그러나 K 문제의 "해결"이 정말 무엇을 의미하는지 명료하지 않다 — 이것 자체가 재프레이밍 대상.

---

## 1. 방법 1: 공리 스트레스 테스트

각 공리를 완화하면 무엇이 깨지나.

### Group A (Closure)
- **A1' (조건부 연장성)**: `a_cl < 4` 조건에 묶여있음. `a_cl ≥ 4`에서 다중 고정점 → "비축약 regime"이 canonical §11.2 item 8에 open으로 명시되어 있으나 **전혀 연구되지 않음**. 다중-형성체를 비축약 regime으로 설명하는 대안 경로가 개봉된 채로 방치.
- **A3 (축약)**: `max σ' = 1/4`라는 sigmoid 특유의 상수에 의존. Sigmoid를 다른 활성화(ReLU-like, smooth step)로 바꾸면 경계값이 달라짐 — sigmoid 의존성은 사실상 load-bearing인데 "provisional"로 라벨됨.

### Group B (Adjacency)
- **B1-B4**: 인접 구조 `N_t`가 **외부 입력**으로 주어진다. 자가참조 이론인데 관계 구조 자체는 자가참조적이지 않다. `N_t`를 `u_t`에서 유도할 수 있는가? — 현 canonical에 일체 언급 없음.

### Group C (Co-belonging)
- **C1-C4**: `C_t`가 v2.0→v1.2에서 **에너지 항에서 강등**됨 (§3.6). 진단 도구로만 잔존. 이 강등은 "Sep이 u-weighted로 바뀌면서 C가 predicate 역할을 잃었기 때문"이라는 설명 — 즉 **수학적 편의로 인한 강등**이었지 원리적 결정이 아니다. §14 CN7이 "세 모드(completion / contrast / integration) 중 integration은 빠져있다"를 공개적으로 인정한다. 이 공백은 open problem으로 등록되지 않음.

### Group D (Distinction)
- **b_D = 0 강제**: §9.3이 명시. `b_D·g_t` 항은 경계 민감도(D-Ax3)의 명시적 수학적 구현이었으나 **에너지 해석성(analyticity)을 위해 제거**됨. 즉 **D-Ax3이 실질적으로 침해된 상태에서 나머지가 작동**. 이것이 정리 T14(Łojasiewicz) 성립을 가능케 했지만, 공리 D-Ax3과 구현의 괴리는 canonical 자체에서는 정면으로 다루어지지 않음.

### Group E (Transport)
- **E3가 공리 → 해답 제약으로 강등** (§3.8 Reclassification Note, §6 Group E "Reclassification Note"). 즉 "공리였으나 증명이 안 되어 '좋은 해답의 속성'으로 지위를 낮춤". 이것은 **완곡하게 표현된 공리 실패**. 또 있는가?
- **E4는 외부 특징 φ에 의존** (§3.8 Honesty Note). 자가참조적 transport는 open. `T-Persist-1(e)`에서 3-component fingerprint로 약진했으나 완전 자가참조는 아님.

**→ 공리계 전체가 "편의로 조정된 곳"이 공리-구현 괴리의 형태로 다수 존재.** 이것들이 모두 명시적 공리로 등록되어있지 않은 **암묵적 구현 제약**이다.

---

## 2. 방법 2: 암묵 가정 탐지

canonical이 "당연시"하는 것들.

1. **`X_t`는 유한**. 증명은 전부 유한 그래프 위에서. 연속 극한은 OP-0022 "LOW"로 분류. 그러나 pre-objective 이론이 본질적으로 이산 집합에 의존한다면 철학적 주장과 수학적 토대가 어긋난다 (§2 "On the status of $X_t$"가 방어하지만 논증 자체는 짧은 주석).
2. **`X_t`는 t에 대해 고정 (site 생성/소멸 없음)**. 즉 OP-0020 "Dynamic topology"로 분리. 그러나 pre-objective cohesion은 세계 구조 자체가 변하는 층위를 지칭해야 하는데 sites는 고정이라 가정됨.
3. **T는 주어진 이산 순서집합** (§3.1). 시간 자체가 pre-theoretic. "temporal inheritance"를 논하는 이론이 시간 자체를 주어진 것으로 전제.
4. **Volume m은 외부 파라미터**. §8.0에서 "구조적 공리"로 격상 시도하지만 ontological justification ("finite capacity")은 수학적 필연이 아니라 선택된 commitment.
5. **Double-well W(u) = u²(1-u)²는 특정 형태**. Allen-Cahn의 유산. 왜 이 형태여야 하는지 이론 내부에서 도출되지 않음.
6. **σ sigmoid, 평균장 P_t**, 각종 파라미터 `(a_cl, η_cl, τ_cl, a_D, λ_D, τ_D, α, β, λ_*, σ_M, γ_M, γ_rep, μ_floor, ...)` — 모두 **외부 지정**. 원리적 선택법 없음 (OP-0005 "K 선택 메커니즘"보다 근본적인 파라미터 전체의 origin 문제).
7. **4개 에너지 가중치 `λ_{cl,sep,bd,tr}`는 모두 > 0**이고 선택 자유. `λ_sep/λ_bd ≈ 10⁻⁵`는 Hessian normalization에서 암시되지만 (§11.2 item 9) framework로 통합 안 됨.
8. **Core/Interior/Boundary 임계값 `θ_{core,in,1,2,ext}`는 전부 free parameter** (§5). "threshold-free" 대안이 없고, threshold는 이론에 영속적으로 내재됨. Q_morph조차 superlevel filtration의 sweep을 사용하나 최종 diagnostic에서 threshold 선택 재등장.

**→ 이론은 '파라미터-의존 platform' 위에 building됨.** canonical-level에서 "파라미터의 원천"이 다루어지지 않음.

---

## 3. 방법 3: 최상위 ontology로부터 downward

§3의 formal universe `C^soft = (T, {X_t}, {u_t}, {Cl_t}, {N_t, D_t}, {M_{t→s}})` 를 "가장 상위 물음"으로 추궁.

### 물음 1 — u_t는 진짜로 primitive인가?
`u_t : X_t → [0,1]`가 primitive라 선언되지만, 그 domain인 `X_t`는 primitive가 아니다 (그저 "relational support"). 따라서 **진짜 primitive는 (X_t, u_t) 쌍**이다. X_t 자체의 정당화가 없으면 u_t의 "pre-objective" 지위는 X_t의 pre-theoretic 지위에 기생한다.

### 물음 2 — K는 어떤 층위의 개념인가?
`u_t`는 실수값 연속장이다. 그러나 "formation"과 "K 개의 formation"은 정수값이다. K는 언제, 어떻게, 무엇으로부터 추출되는가? 현 canonical에서 K는:
- Phase I (Nucleation): 스펙트럼의 eigenvector에서 emerge
- K-field 구조 (§12): K 개의 coupled field가 **구조적으로 선 given**
- 진단 레벨: connected components of superlevel set

**셋이 일치한다는 보장 없음.** K는 soft-level에서 integer가 아닐 수 있다. K가 그래디언트 연속으로 정의되는 "soft count" (예: persistent H_0 total bars weighted by length)로 대치되어야 할 가능성이 canonical에 전혀 반영되지 않음.

### 물음 3 — 4개 에너지는 진짜로 독립인가?
CN5: "독립은 개념적, 수학적이지 않음". 이것은 조심스러운 자기 비판이자 동시에 숨은 열린 문제다. **수학적 의존 구조를 정량화**하지 않았다. 예: `∂E_sep/∂u`가 `∂E_cl/∂u`와 얼마나 정렬(aligned)되는가? Fisher 정보 행렬의 off-diagonal? 만약 세 항의 gradient가 근사 평행하면 "4개 독립 요구"는 환상.

### 물음 4 — 자가참조성의 구체성 (CN7)
Cl은 self-completion, D는 self-contrast, C는 self-integration. 셋 중 둘만 에너지에. 왜 **완료 2모드 체계**인가? 3모드, 1모드, 무한모드 중 2모드가 선택된 것은 uniqueness/completeness 주장이 아니라 **경험적 균형**. 진짜 "operator 모드의 전수 분류"가 canonical에 없다.

---

## 4. 방법 4: 외부 이론과의 비교 — SCC가 놓치는 것

| 비교 이론 | 이론의 특징 | SCC의 대응 | SCC의 공백 |
|---|---|---|---|
| Allen-Cahn | `E = ∫(ε∇u² + W(u))`, double-well, Γ-conv → mean curvature | `E_bd`로 포함 | 자가참조 closure는 AC에 없음 → 이 novelty가 결정적 |
| Optimal Transport (OT) | 거리·cost 기반 | Transport `M_{t→s}`, Sinkhorn | Self-referential cost의 **uniqueness** 미결 |
| Persistent Homology | H_k, 다중 스케일 | Q_morph의 H_0 bar | H_1 이상 안 씀 — hole / void 구조는 전혀 다루지 않음 |
| Graph gauge theory | 평행 이송, holonomy | 없음 | SCC에서 "**연결(connection)**" 개념 부재. C_t가 그 공백의 유령 |
| Renormalization Group | 스케일 변환 flow | §12 "RG analysis"가 open으로 언급만 | 어느 스케일에서 `u_t`가 정의되는지 공리 수준에 없음 |
| Mean-field theory / statistical mechanics | 분배함수 Z, free energy F=E-TS | §8.1의 E | **엔트로피 항 없음.** 온도 없음. 비결정론 없음 |
| Stochastic PDE / fluctuation | 노이즈 항, escape rate | OP-0021 "LOW" | metastability는 noise가 본질인데 noise theory 부재 |

**→ 가장 눈에 띄는 두 공백:**
- **연결(connection) 개념 부재.** Gauge 구조가 SCC에 필요한지는 separate question이지만, `C_t` 강등 이후 "어떻게 cohesion이 공간 간 전달되는가"를 다루는 구조가 오로지 Laplacian(scalar)만 남아있다. Vector-valued transport가 없다.
- **엔트로피 / 온도 / 노이즈의 부재.** metastability 주장이 가능하려면 thermal escape의 정량화가 있어야 함. §12에서 "Kramers" 언급하나 프레임워크에 통합되지 않음. 사실상 이론이 **zero-temperature 결정론**으로 작동.

---

## 5. 방법 5: Bottom-up 섹션별 "이 안의 진짜 미해결"

| 섹션 | 내부의 실제 미해결 |
|---|---|
| §2 foundational orientation | `X_t`의 pre-theoretic 지위 vs 이론의 pre-objective 주장 간 긴장 (§2 마지막 단락이 defense하나 짧음) |
| §3 formal universe | `C_t`가 formal universe에서 demote된 이후 세 모드의 자가참조 → 두 모드로 축소 정당화 부재 |
| §4 "why soft is primary" | 전부 철학적 논증. 수학적 필연성 proof 없음 |
| §5 derived morphology | 모든 정의가 임계값 `θ`에 의존. threshold-free 대안 없음 |
| §6 axiom groups | A1', b_D=0, E3 demotion은 수학적 편의로 공리 약화 |
| §7 proto-cohesion vector | 4 컴포넌트는 각각 척도가 다른데 `[0,1]^4` 단일 space에 넣고 대등 취급. "가중평균"이 diagnostic에 없음 — 의도적 선택 |
| §8 energy principle | 4 term은 linear 합. 곱/결합 형태 가능성 miss |
| §9 provisional operators | sigmoid, resolvent — 전부 particular choice. "general class 내에서 canonical choice" 이론 없음 |
| §11 fixed/open | 13개 fixed commitment는 전부 post-hoc 합리화. 여기서 "fixed"는 "지금까지 흔들리지 않은"이지 "증명된 불가결성"이 아님 |
| §12 open problems | Self-referential transport가 거의 해결됨을 빠르게 주장하지만, **transport 자체가 self-referential이 돼야 한다는 motivation도 실은 ad-hoc** |
| §14 CN들 | CN1/CN2/CN5/CN6/CN9는 **논쟁 여지가 있는 선언을 commitment로 고정**한 것. 비판 가능한 지점을 "commitment"로 보호함 |

---

## 6. 재명명된 Open Problem 목록 (P-A ~ P-H)

**기존 F/M/MO 언어 일체 사용 금지.** 새 이름은 의도적으로 K=1/K=2 비교에서 멀어지게 만듦.

### P-A. 이산 K와 연속 u의 층위 불일치 (Integer-K / Continuous-u Mismatch)

**무엇이 문제인가.** `u_t`는 연속 실수값장. 그러나 "formation의 개수 K"는 정수. 두 층위를 매끄럽게 잇는 수학이 없다. K-field 아키텍처(§12)는 K를 **외부에서 정수로 고정**하고 소프트 장을 구축하는 방식 — 이 자체가 층위 도약의 임시방편.

**어디서 보이는가.** §12 K-field, §14 CN6, K-field 관련 모든 정리의 "fixed K" 가정, isoperimetric 비교 (`E(u*_{2c}) < 2·E(u*_c)`)는 K 위치를 사전 고정.

**왜 지금까지 잘 안 보였는가.** F-1/M-1 언어가 "K=1 vs K=2 에너지 비교"로 프레임을 좁혔기 때문. 진짜 물음은 "K가 무엇인지, 어디서 오는지, 정수여야 하는지"인데 언어가 이미 정수 K를 전제하고 있었다.

**가능한 재프레이밍 방향 (method-open).**
- Soft-count: H_0 persistence total weighted bar length처럼 K 자체를 실수화
- K를 외부 파라미터로 명시 유지하되 이를 "regularization scale"로 재해석
- u를 vector-valued로 격상 (u: X_t → Δ^K simplex) — K-field와 다른 조형

### P-B. 외부 제공 substrate (X_t, N_t) 의존성

**무엇이 문제인가.** `X_t`(sites)와 `N_t`(adjacency)는 pre-theoretic 입력. 즉 이론은 "관계 구조가 이미 주어진 세계"에서 시작한다. 그러나 이론의 ontological ambition은 "objecthood 이전 층위"이며, 이 층위에서 관계 자체가 이미 개별화되어 주어진 것은 수행적 모순(performative contradiction).

**어디서 보이는가.** §3.2, 3.5의 "given". B-group 공리 전부 `N_t`를 input. §2 마지막 단락의 방어는 짧은 주석.

**왜 안 보였는가.** "graph 위 이론"이라는 배경 합의에 가려져 substrate 자체의 지위 물음은 수학 작업 목록에 안 올라왔음.

**재프레이밍 방향.**
- `N_t`를 `u_t`에서 유도하는 메커니즘 (self-generating adjacency)
- 관계 primitive를 점이 아닌 엣지로 재설정
- 또는 이 가정을 의식적 scope 제한으로 canonical에 명시 (honesty 승급)

### P-C. 자가참조 세 모드 중 한 모드의 실종 (Missing Third Mode)

**무엇이 문제인가.** Closure(self-completion)와 Distinction(self-contrast)는 에너지에 진입. Co-belonging(self-integration, C_t)는 강등되어 진단 전용. CN7이 "dual-mode"를 자랑스럽게 선언하지만, 실은 **세 모드 ontology를 두 모드로 축소한 암묵적 결정**이다. 축소의 정당성은 "C_t-weighted Sep이 0.5로 degenerate됨"이라는 수학적 부작용이지 원리적 이유가 아니다.

**어디서 보이는가.** §3.6, §9.4, CN7.

**왜 안 보였는가.** 개발 과정에서 C 강등이 "문제 해결"로 기록되었기 때문에 그 결정 자체를 재검토 대상으로 보지 않게 됨.

**재프레이밍 방향.**
- C_t가 에너지에 들어가는 대안 (entropy-like 항?)
- 세 모드를 symmetric하게 배치하는 공리계
- 또는 "왜 두 모드여야 하는지" 를 증명 (어려움)

### P-D. Threshold의 비원리적 내재성

**무엇이 문제인가.** Core, Interior, Boundary band 전부 `θ_core, θ_in, θ_1, θ_2, θ_ext` 임의 선택에 의존 (§5). Q_morph는 superlevel filtration으로 threshold를 sweep하지만 Bind/Sep/Persist predicate은 threshold로 잘라낸 set을 재사용한다. 이론의 "graded" 주장은 predicate-level에서 다시 임계값에 의해 이산화된다.

**어디서 보이는가.** §5, §7.1 (특히 Persist의 `Core_t` 참조), §12의 `D_{sep}` 같은 모든 geometric 임계.

**왜 안 보였는가.** "임계값은 구현 디테일"이라는 관행. 그러나 threshold 선택은 예측 결과(특히 metastability 구간)에 직접 영향.

**재프레이밍 방향.**
- Threshold-free diagnostic (integral over all θ → 단일 스칼라)
- Threshold-parametrized family로 공식 인정
- Promotion pipeline에서 "threshold 선택은 명시하라" 규약

### P-E. 파라미터 origin problem (Full Parameter Genealogy)

**무엇이 문제인가.** OP-0005 "K selection"은 `K` 한 파라미터만 문제시한다. 그러나 `(a_cl, η_cl, τ_cl, a_D, λ_D, τ_D, α, β, λ_cl, λ_sep, λ_bd, λ_tr, σ_M, γ_M, λ_rep, m, c, θ_core, θ_in, θ_1, θ_2, θ_ext, ε, ε_OT, σ, γ, θ_supp, ...)` **25개 이상의 파라미터**가 외부 지정. 원리적 값도 없고 dimensional analysis만 partial.

**어디서 보이는가.** §9 전체, §11.2 items 5/9.

**왜 안 보였는가.** 파라미터 개별 조정은 일상 작업이라 "파라미터 origin"이라는 공통 프레임으로 묶이지 않음.

**재프레이밍 방향.**
- 파라미터를 dimensional group으로 분류 → 무차원 비만 관찰
- RG flow가 고정점을 제공한다면 파라미터는 emergent
- 각 파라미터를 "ontological / structural / computational" 범주로 분류 → computational만 free로 인정

### P-F. Zero-Temperature 결정론 위의 metastability 주장

**무엇이 문제인가.** Metastability는 본질적으로 **finite temperature 현상** (barrier vs kBT). 그러나 SCC 이론에 온도도 엔트로피도 노이즈도 없다. 그럼에도 §12, §13, CN6/CN8/CN14가 "metastable" 표현을 반복 사용. exp38의 `β^{0.89}` 같은 scaling도 temperature가 없는 세계에서는 시간척도를 가질 수 없다.

**어디서 보이는가.** §12 multi-formation 전체, CN6, CN8, CN14, T7-Enhanced 해석.

**왜 안 보였는가.** "noise / temperature는 추후 extension"으로 미루어둠. 그러나 metastability 주장을 현재 시점에 쓰고 있음 — 주장과 framework의 표준 불일치.

**재프레이밍 방향.**
- Thermal SCC: Langevin noise, partition function, free energy
- Kinetic SCC (Option C는 폐기됐지만 이 프레임은 살아있음) 을 **independent working topic**으로 재설정
- Metastability 주장을 "zero-temperature local minimum" 언어로 downgrade

### P-G. 공리-구현 괴리 (Axiom/Implementation Divorce)

**무엇이 문제인가.** 세 가지 공리가 수학적 편의로 수정 또는 강등됨:
- A1 → A1' (conditional)
- D-Ax3의 gradient 항 `b_D·g_t` → `b_D = 0`
- E3: 공리 → solution constraint

이 모두 "공리는 유지하되 구현에서는 완화"라는 이중 표시. Canonical 내부에서 "공리/구현 층위 분리"가 명시되나, 실제로 공리계가 무엇을 보장하는지는 **구현 선택에 달려있다**.

**어디서 보이는가.** §6 각 Group의 "Layer-crossing note" 및 "Reclassification Note".

**왜 안 보였는가.** 각 수정이 개별 iteration에서 "gap closure"로 기록되어 누적 효과가 drift로 인식되지 않음.

**재프레이밍 방향.**
- 공리-구현 정합성 표(audit table) 작성
- "공리가 이렇게 약화되었을 때 어떤 정리가 무효가 되는가" 체크
- 또는 공리를 구현에 맞춰 재기술 (공리가 거짓말 안 하도록)

### P-H. 시간 T의 pre-theoretic 성격

**무엇이 문제인가.** T는 "linearly ordered set"으로 주어진다 (§3.1). 그러나 이 이론의 가장 강력한 개념 중 하나가 **temporal persistence**이다. 시간 자체를 pre-theoretic으로 두면 "persistence"가 무엇을 연결하는지가 substrate-dependent.

**어디서 보이는가.** §3.1, §6 Group E, §7.1 (Persist 정의의 window W).

**왜 안 보였는가.** "시간은 당연히 주어진다"는 배경 가정.

**재프레이밍 방향.**
- 시간 자체가 cohesion 의 emergent property인가? ("시간은 변화가 있는 곳에서만 있다")
- 또는 명시적으로 "SCC는 주어진 시간 위에서의 공간적 cohesion 이론이다"로 scope 제한
- 연속 시간 극한 (T → ℝ)을 별도 working으로

---

## 7. 더 작은, 그러나 동일하게 안 보였던 것들 (요약)

- **H_1 이상의 persistence 부재** — `u_t`의 hole/void 구조는 전혀 사용 안 됨. Q_morph가 H_0로 제한. 고리 있는 formation은 이론에 언어 없음.
- **에너지 항 선형 결합의 임의성** — 4 term은 `λ · E` 형태로 합쳐짐. Multiplicative/modal 결합 가능성 미탐.
- **관찰자 / 측정의 부재** — 이론은 `u_t`가 존재함을 가정. 어떻게 관찰되는가, 어떤 관측 가능량과 대응하는가는 open.
- **학습 / 적응 메커니즘 부재** — 이론은 정적. 파라미터가 경험/데이터로부터 조정되는 메커니즘 없음.
- **다중 스케일 내재성 부재** — RG와 coarse-graining은 §12에 open으로 언급만. 현재 이론은 단일 스케일.

이들은 P-A~P-H보다 덜 시급하나, 향후 개별 working topic로 분화될 후보.

---

## 8. 재분류: "진짜 하나의 깊은 문제"

위 P-A~P-H 중 **P-A, P-D, P-G가 모두 동일한 근본 긴장에서 파생**된다:

> **이론의 ontology는 continuous (graded, soft)인데, 작동은 discrete (integer K, threshold, axiom-carved category)에 의존한다.**

즉 "**소프트-하드 스위칭(soft-hard switching)의 비원리성**"이 단일 원천.

- P-A는 K에서의 스위칭
- P-D는 threshold에서의 스위칭
- P-G는 공리 가정의 강-약 스위칭

이 관점에서 F-1/M-1/MO-1도 같은 원천의 증상이다 (§9 참조).

이 하나의 깊은 문제를 **N-1: Soft-Hard Switching Asymmetry** 라고 임시 명명. 다음 연구 세션에서 이 문제를 별도 working topic (`THEORY/working/N-1_soft_hard_switching.md`)으로 분화할 후보.

---

## 9. 기존 F-1 / M-1 / MO-1과의 교차 대조

| 기존 이름 | 기존 정식화 | 재프레이밍 매핑 | 차이 |
|---|---|---|---|
| **F-1** (K=2 vacuity) | K=2 global stability이 external m 제약 없이는 공허 | **P-A + P-E**: K는 정수-스위칭 스케일, m은 외부 파라미터 genealogy | F-1은 "증상". 더 일반화된 문제의 단면. |
| **M-1** (K=1 always preferred) | E(u*_M) < E(u*_{M/2}) (isoperimetric) | **P-A**: K가 외부에서 정수로 고정되기 때문에 단사 비교가 가능 | M-1 자체는 수학적으로 **참 정리** (isoperimetric). "문제"가 아니라 **기존 프레이밍이 문제로 해석한 정리**. |
| **MO-1** (Morse inapplicable) | Σ²_M이 corners 있는 manifold → smooth Morse 불가 | **P-A + P-D**: m₂ = 0 코너는 정수-K 스위칭이 만든 stratification. threshold-free formulation에서는 corner가 사라질 수 있음. | MO-1은 "smooth Morse가 안 되는" 기술적 한계. 대안 framework(stratified Morse, discrete Morse)가 있음에도 smooth Morse만 기본 도구로 쓴 선택의 결과. |
| **OP-0004** Type A/B 기각 | exp65에서 0/4 Type B 관찰 → 분류 기각 | 분류 실패 자체가 P-A 증상 — "정수 타입"으로 configs를 강제 분류하려 했음 | 재평가: Type A/B 의 정수 분류 대신 continuous classifier가 가능한가? |
| **OP-0005** K-선택 메커니즘 | K는 어디서 오는가 | **P-A**: 근본. K를 integer로 전제한 채 "선택"하려 하기 때문에 막힘. | K 를 선택하는 게 아니라, K 자체를 emergent/gradable 하게 재정의하면 문제가 사라질 가능성. |
| **OP-0006** 경계 정의 정밀도 | B_t = {D_t > θ} 불명확 | **P-D**: threshold 의존 | 경계 자체를 smooth family로 정의 (threshold-free). |

**핵심 교체:**
- **F-1** → "K가 정수여야 하는가" + "m의 origin은 무엇인가"
- **M-1** → 이것은 문제가 아니라 proved theorem. K를 soft로 만들면 isoperimetric 비교의 의미가 바뀐다.
- **MO-1** → "왜 smooth Morse만 쓰는가" + "stratified alternative 사용은?"

**증발한 것:**
- **"K=2가 살 수 있어야 한다"는 요구** — 이 요구 자체가 framework에 의한 편향. K를 soft로 만들면 "K=2가 안정인가"가 물음이 아니라 "K-soft 분포가 어떤 모습인가"가 물음이 됨.

**새롭게 드러난 것:**
- **N-1 Soft-Hard Switching Asymmetry** (§8): 이 단일 원천이 F-1/M-1/MO-1/OP-0004/OP-0005/OP-0006/P-A/P-D/P-G를 모두 설명.
- **P-F Zero-Temperature Metastability Claim**: 현 이론의 가장 큰 주장 중 하나가 framework 불일치 위에 서있다.
- **P-B External Substrate**: ontological 선언과 수학적 입력의 괴리 — 전혀 open problem list에 없던 것.
- **P-H Time Pre-theoretic**: persistence 주장의 근거 층위가 미검토.

---

## 10. 다음 단계 제안 (본 reframing의 deliverable로서)

이 문서는 재프레이밍 **결과**이지 해결이 아니다. 어느 줄기부터 붙을지는 별개 의사결정.

가장 강한 후보 세 줄기 (method-flexible):

1. **N-1 (Soft-Hard Switching Asymmetry) 을 working topic으로 분화** → `working/N-1_soft_hard_switching.md` — F-1/M-1/MO-1/OP-0005/OP-0006 을 통합 framing으로 다룸.
2. **P-B (External Substrate) 방어 심화** → `working/substrate_genealogy.md` — X_t/N_t의 pre-theoretic 지위를 공식 scope 제한 혹은 self-generating 메커니즘으로 다룸.
3. **P-F (Temperature-less metastability) 을 honest scope note로 승급** → canonical §14에 새 CN 추가 혹은 working에서 full thermal reformulation.

각 줄기는 single-session scale 작업 단위로 쪼개 가능.

---

## 11. 문서 메타

- **작성**: 2026-04-19
- **Method scorecard**: 5 방법 중 5 적용 — 공리 스트레스(§1), 암묵 가정(§2), top-down(§3), 외부 비교(§4), bottom-up(§5) 모두 기여.
- **Fresh eye 성공 지표**: F/M/MO 언어 §1~§7에서 0회 사용 (§9에서만 대조 목적으로 등장). 새 problem label (P-A~P-H, N-1) 9개 생성.
- **증발한 기존 문제**: 없음 (M-1은 "정리로 재분류", 삭제 아님).
- **새로 드러난 문제**: P-B, P-F, P-H 및 단일 원천 N-1.
- **위치**: `THEORY/working/open_problems_reframing_2026-04-19.md`
- **승급 경로**: 이 문서는 working 단계. canonical로 승급하려면 `THEORY/canonical/open_problems.md` 에 반영 — 단, canonical 수정 전에 주요 재명명을 CHANGELOG에 기록하고 공개적 erratum 형식 유지.
