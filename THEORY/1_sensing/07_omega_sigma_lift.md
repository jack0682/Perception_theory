---
type: working/sensing_pipeline/lift
version: v0
date: 2026-05-25
status: DEFINITION-DRAFT
purpose: |
  Lift the entire SSKP to (Ω, σ) Tier 2 framework.
  Define (Ω_i, σ_i) for each stage 0–3.
  Establish σ propagation as a functorial structure.
  Show the point ↔ field ↔ point cycle (Stage 0 point process,
  Stage 1–2 fields, Stage 3 point process again).
  Register TC-SP-5.1, TC-SP-5.2, OP-SP-006.
register: DEFINITION-DRAFT + THEOREM-CANDIDATE (no proofs)
parent: 01_framework_master
prev_doc: 06_endtoend_information_bound
constraint_compliance:
  canonical_theorem_changes: 0
  scc_edits: 0
---

> [!nav] Parent: [[00_INDEX]] · Prev: [[06_endtoend_information_bound]] · Next: [[08_open_problems_sp]] · Conversation origin: 사용자 commit to Tier 2 (Ω, σ) minimal Raw

# (Ω, σ) Tier 2 Lift — Pipeline as Graded Tier 2 Structure

## 0. 본 문서의 위치

본 문서는 sensing pipeline 전체를 (Ω, σ) Tier 2 framework 로 lift 한다. 이 framework 의 commit 은 대화에서 이루어졌으며 ([Tier 2 (Ω, σ) minimal Raw](#)), 본 문서는 그 commitment 가 *각 stage 에서 어떻게 자연스럽게 실현되는지* — 또는 어디서 강제적 extension 이 필요한지 — 를 정확히 추적.

본 문서의 핵심 주장 (모두 candidate):

1. 각 stage 가 (Ω_i, σ_i) 의 한 instance 를 carry
2. Kernel $\mathcal{K}_i$ 가 σ 를 *functorially* propagate
3. 전체 파이프라인이 Tier 2 *위에서 닫혀 있음* — Tier 4 (metric / vector) 구조를 본질적으로 요구하지 않음
4. **Stage 0 와 Stage 3 가 둘 다 점과정** — *point ↔ field ↔ point* 의 순환 구조가 의미론적으로 결정적

본 문서가 *수행하지 않는 것*: SCC 의 $u_t$ 가 어느 stage 에 대응하는가의 *결정* (OP-SP-006 등록만); PAI 와의 다리 (격리).

---

## 1. (Ω, σ) Tier 2 — 정의 (대화에서의 commit 재진술)

### 1.0 Axiomatic definition

**Definition 1.1 (Tier 2 structure / tolerance space)**. **Tier 2 객체** 는 쌍 $(\Omega, \sigma)$ 이며 다음 axioms 를 만족:

- **(Ω0) Carrier**: $\Omega$ 는 집합. 원소들은 *불투명 토큰* — 내부 구조 (component, value, coordinate) 가 *데이터로* 주어지지 않음.
- **(σ1) Reflexivity**: $\forall x \in \Omega,\ \sigma(x, x)$.
- **(σ2) Symmetry**: $\forall x, y \in \Omega,\ \sigma(x, y) \Rightarrow \sigma(y, x)$.
- **(σ3) Non-transitivity**: 일반적으로 $\sigma(x, y) \wedge \sigma(y, z) \not\Rightarrow \sigma(x, z)$. *Transitivity 를 axiom 으로 부과하지 않음*. (이는 *금지* 가 아니라 *비-요구*. 특정 instance 가 우연히 transitive 면 Tier 2 의 *degenerate* case.)

**용어 (Poincaré 1905)**: $(\Omega, \sigma)$ 를 *tolerance space* 라 부른다. $\sigma$ 는 *tolerance relation*. *Equivalence relation 의 약화* — transitivity 만 빠진 것.

**금지된 추가 구조** (Tier 2 commit 의 의미):

- (X1) 거리 함수 $d : \Omega \times \Omega \to \mathbb{R}^+$ — 금지 (Tier 3 에서 도입)
- (X2) 값 mapping $v : \Omega \to V$ for non-trivial value space $V$ — 부속물로는 허용, 본질로는 금지
- (X3) 벡터공간 구조 $+, \cdot$ — 금지 (Tier 4)
- (X4) 확률 분포 $\mu$ on $\Omega$ — 부속물로는 허용, 본질로는 금지 (Markov 가 아님)

### 1.0.1 Equivalence class 비-존재 정리

**Proposition 1.2 (Non-existence of induced equivalence classes)**. 일반적 tolerance space $(\Omega, \sigma)$ 에서, $\sigma$ 로부터 $\Omega$ 의 *분할* (partition into equivalence classes) 을 *canonical* 하게 유도하는 방법은 *존재하지 않는다*.

**증명 sketch (counterexample: Sorites)**. $\Omega := \{0, 1, 2, \ldots, n\}$ (모래알 더미의 알 수), $\sigma(i, j) :\iff |i - j| \leq 1$.

- $\sigma$ 는 반사적 (자명), 대칭적 (자명).
- $\sigma$ 는 *비추이*: $\sigma(0, 1) \wedge \sigma(1, 2)$ 이나 $\neg \sigma(0, 2)$.
- *Transitive closure* $\sigma^*$ 를 취하면 $\sigma^*(0, n)$ — 즉 모든 원소가 단일 class. *정보 zero*.
- *Maximal cliques* (각 원소에 대해 $\sigma$-인접한 모든 원소의 maximal subset) 는 *겹침* — $\{0, 1\}, \{1, 2\}, \ldots$. *분할이 아님*.
- *어떤 canonical 분할도 정의 불가*.

따라서 tolerance space 의 *근본 특징* 은: *유사성 관계는 있으나 깔끔한 카테고리 (equivalence class) 가 없음*. 이게 *Tier 2 의 진정한 표현력* — 사물이 "겹쳐 보이는" 현상을 살림.

**물리적 의미**: 두 광자가 "거의 같은 위치" 라는 관계는 가능하나, "어떤 광자가 어떤 위치-class 에 속하는가" 는 *임의 분할* 없이 결정 불가. Sorites 와 동일 구조.

### 1.1 정의 (대화의 재진술)

**Definition 1.3 (Tier 2 structure, 본 디렉토리 용)**. (Ω, σ) Tier 2 객체는 §1.0 의 axioms 를 만족하며:

- **Ω**: occasion (발생점) 의 집합 — 불투명 토큰, 내부 구조 없음
- **σ ⊆ Ω × Ω**: 유사성 / 인접 관계 — 반사적, 대칭적, **비추이적**

추가 구조 *없음*: 값, 거리, 벡터, 좌표, 확률 분포.

### 1.1.1 Tier 계위 (대화에서의 위계 재진술)

| Tier | 구조 | 가능 | 추가 axiom |
|------|------|------|-----------|
| 0 | 집합만 | 거의 없음 | (없음) |
| 1 | 동일성 (=) | 동등 / 부등 | $\equiv$ reflexive, symmetric, *transitive* |
| **2** | **유사성 σ (비추이)** | **근접 군집화, 그래프** | $\sigma$ reflexive, symmetric, *not transitive* |
| 3 | 의사거리 d | "얼마나 멀리" | $d : \Omega^2 \to \mathbb{R}^+$ with $d(x,x)=0$, $d(x,y)=d(y,x)$, *triangle inequality* |
| 4 | 벡터공간 | 미분, 선형대수 | $(\Omega, +, \cdot)$ a vector space + metric/topology |

본 디렉토리의 commit: **Tier 2 에서 작업**. 더 강한 구조가 *필요할 때* 만 정당화하여 도입.

### 1.1.2 Tier hierarchy comparison theorems

**Theorem 1.4 (Forgetful collapse, Tier k+1 → Tier k)**. 다음 forgetful maps 가 자연스럽게 정의된다:

1. **U_{4→3}**: Tier 4 $(V, +, \cdot, \|\cdot\|)$ → Tier 3 $(V, d)$ with $d(x, y) := \|x - y\|$. ($+, \cdot$ 잊음.)
2. **U_{3→2}**: Tier 3 $(\Omega, d)$ → Tier 2 $(\Omega, \sigma_{\varepsilon})$ with $\sigma_{\varepsilon}(x, y) :\iff d(x, y) < \varepsilon$ for some chosen $\varepsilon > 0$. (Triangle inequality 잊음. 결과 $\sigma_\varepsilon$ 는 반사/대칭/비추이 — Tier 2 axioms 자동 만족.)
3. **U_{2→1}**: Tier 2 $(\Omega, \sigma)$ → Tier 1 $(\Omega, \equiv_{\sigma^*})$ with $\equiv_{\sigma^*}$ = *transitive closure* of $\sigma$. (Trivial 한 경우가 많음; Sorites 식 collapse.)
4. **U_{1→0}**: Tier 1 → Tier 0: $\equiv$ 잊고 carrier $\Omega$ 만 남김.

**Proof sketch**: 각 단계에서 잊는 구조 (vector, triangle, transitivity, equivalence) 가 axiom set 의 *적절한 부분집합*. 잊어진 후 남은 axioms 가 하위 Tier 의 axioms 와 일치.

**Corollary 1.5 (Tier 4 → Tier 2 direct)**. $U_{2→}^{\varepsilon} := U_{2→} \circ U_{3→} \circ U_{4→}$ 는 vector space + metric 구조를 (Ω, σ_ε) 로 압축. 본 디렉토리의 commit 은: *역방향 lift 가 자연스럽지 않음*. Tier 2 → Tier 4 는 *임의의 enrichment* — 정보 *추가*. 반면 4 → 2 forgetful 은 *정보 손실*.

**중요**: 본 pipeline 의 *대상 구조* 는 Tier 2 이지만, *분석 도구* (Fourier, SDE, convolution) 는 종종 Tier 4 위에서 산다. Tier 4 도구로 만든 결과의 *Tier 2 측 reduction* 이 본 디렉토리가 추적하는 것.

### 1.2 (Ω, σ) 와 prolegomena 의 양립 — 상세 검증

[[00_field_conditions_v0|prolegomena conditions catalog]] 의 negative 조건 C1–C5 에 대해 각각 *형식적 정당화*:

**C1 verification — 장은 함수가 아니다**.
함수 $f : A \to B$ 는 *사전에 주어진* domain $A$, codomain $B$, 그리고 각 $a$ 에 *유일한* $f(a)$ 를 요구. Tier 2 $(\Omega, \sigma)$ 에는: (i) 사전에 주어진 codomain 없음 (σ 는 $\Omega \times \Omega \to \{0, 1\}$ 의 *관계* 일 뿐, $\Omega \to V$ 의 mapping 이 아님); (ii) σ 는 *대칭* 이므로 "input → output" 의 방향성 없음; (iii) 각 $x$ 에 대해 σ 가 *어떤 $y$ 와 관계 맺는가* 는 *복수* — 함수의 *single-valued* 조건 위배. 따라서 C1 ✓.

**C2 verification — 장은 공간이 아니다**.
공간 (topological / metric / vector) 은 *거리, 위상, 또는 선형 구조* 를 요구. Tier 2 axioms 는 *오직* 반사·대칭·비추이성만; 거리도 위상도 없음 (위상은 *유도* 가능하지만 *원천* 이 아님: σ 로부터 generated topology 는 σ 보다 약함). C2 ✓.

**C3 verification — 장은 상태가 아니다**.
"상태 (snapshot)" 는 시간 $t$ 에서의 *값* — 함수 $s : T \to S$ 의 $s(t_0)$. Tier 2 는 관계 구조이므로 *snapshot 값* 의 개념 자체가 결여. *작동* (= 관계가 *시간에 따라 변함*) 은 Tier 2 sequence $(\Omega_t, \sigma_t)_t$ 로 표현되지만, *snapshot value* 가 아닌 *관계 패턴* 의 진화. C3 ✓.

**C4 verification — 장은 제3자 환원 불가능**.
$\Omega$ 의 토큰은 *불투명* (axiom Ω0). *외부 관측자가* 토큰에 *내부 구조* (좌표, 라벨, 값) 를 *부여* 하지 *않음* — 토큰의 identity 는 *오직 σ-관계의 패턴* 으로 정의 (categorical / structural identity). 따라서 token 자체가 *제3자 좌표계* 에 의존하지 않음. C4 ✓.

**C5 verification — witness/witnessed 분리 불가능**.
σ 는 *대칭* 관계: $\sigma(x, y) \Leftrightarrow \sigma(y, x)$. 어느 쪽이 "관찰자" 인지, 어느 쪽이 "관찰 대상" 인지 *구조적으로 구분 불가*. *관찰 행위* 자체가 *대칭적 인접* 으로 흡수. C5 ✓.

**총평**: prolegomena C1–C5 (N grade, 즉 *반드시* 만족해야 할 조건) 모두 (Ω, σ) Tier 2 가 *axiom 수준에서 자동* 만족. *추가 검증 불필요*. 본 디렉토리의 sensing pipeline 이 prolegomena 와 정합한다는 것은 §1.0 의 axioms 만으로 이미 보장됨.

---

## 2. 각 Stage 의 (Ω_i, σ_i) — explicit

본 절은 각 stage 에 대해: (a) $\Omega_i$ 의 set-theoretic 정의 (가능하면 sigma-algebra 명시); (b) $\sigma_i$ 의 predicate-logic 정의 (parameter constants 명시); (c) σ_i 가 axioms (Ω0, σ1, σ2, σ3) 를 만족함의 sketch; (d) σ-class analog (graph connected component 가 *없음*) 의 예.

### 2.1 Stage 0 — 광자 점과정

**(a) Ω_0 의 형식 정의**.

$$
\boxed{\Omega_0 := \{ \text{atomic points of } N \} = \{ (x_i, t_i, \nu_i) \in \Sigma_{\text{ret}} \times \mathbb{R}^+ \times \Lambda : i \in \mathbb{N} \}}
$$

각 발생점은 단일 광자 도래. **토큰 불투명성**: 광자는 광자 — 다른 모든 양자수가 marginalize 되어 동일. *Ω_0 자체는 sigma-algebra 를 carry 하지 않음* (axiom Ω0); 단 underlying carrier $\Sigma_{\text{ret}} \times \mathbb{R}^+ \times \Lambda$ 는 §1.2 ([[01_framework_master]]) 의 Borel σ-algebra $\mathcal{B}_\mathcal{X}$ 를 가짐 — 이 sigma-algebra 는 *Markov kernel framework 측* 의 것이지 Tier 2 측 데이터가 아님.

**(b) σ_0 의 predicate**.

$$
\boxed{\sigma_0\big((x_i, t_i, \nu_i), (x_j, t_j, \nu_j)\big) :\iff \|x_i - x_j\| < \delta_x \;\wedge\; |t_i - t_j| < \delta_t}
$$

with parameter constants:
- $\delta_x > 0$: 공간 tolerance (e.g., photoreceptor 의 receptive radius $\sim 1{-}5\,\mu m$)
- $\delta_t > 0$: 시간 tolerance (e.g., integration window $\sim 10\,ms$)

(파장 $\nu$ 는 σ 에 포함시키지 않음 — 단순화. 색 정보는 mark 로 carry-along.)

**(c) Axiom 검증**.
- **(Ω0)** 광자 token 의 양자수 (spin, helicity 등) 가 marginalize → opaque ✓
- **(σ1) reflexivity**: $\|x - x\| = 0 < \delta_x$, $|t - t| = 0 < \delta_t$ — 자동 ✓
- **(σ2) symmetry**: $\|x_i - x_j\| = \|x_j - x_i\|$ (norm 의 대칭) — 자동 ✓
- **(σ3) non-transitivity**: 반례. $(x_A, t_A) = (0, 0), (x_B, t_B) = (\delta_x/2 \cdot \hat{e}, 0), (x_C, t_C) = (\delta_x \cdot \hat{e}, 0)$. 그러면 $\|x_A - x_B\| = \delta_x/2 < \delta_x$, $\|x_B - x_C\| = \delta_x/2 < \delta_x$, *그러나* $\|x_A - x_C\| = \delta_x \not< \delta_x$. 비추이 ✓

**(d) σ-class analog**.
Graph-theoretic connected component 은 *equivalence class* 를 요구 — Tier 2 에서는 일반적으로 *존재하지 않음* (Prop 1.2). 그렇다면 Stage 0 에서 σ-class 의 자연스러운 *대체* 는 무엇인가?

- **σ-neighborhood**: $N_{\sigma_0}(p) := \{q \in \Omega_0 : \sigma_0(p, q)\}$ — *공간시간 ball*.
- **σ-clique (maximal)**: $\sigma_0$-완전 부분집합의 maximal extension — *겹침* (overlap), 즉 한 광자가 *여러 clique* 에 속함.
- **Photon "burst"**: 모든 광자 pair 가 σ_0 로 연결된 *최대 부분집합* — 이게 *clique* 임. *Partition 이 아니라 cover*.

본 디렉토리의 자세는: **Stage 0 에서 σ-cliques 의 cover 가 "객체 발생 직전의 잠재 형성" 의 자연 표현**. 어떤 cover 원소가 *유일한 객체로 응고하는가* 는 sensing pipeline 의 *밖* (formation dynamics; SCC 의 영역).

### 2.2 Stage 1 — 광수용기 응답

**(a) Ω_1 의 형식 정의**.

광수용기 응답은 *graded field*. 그러나 *picosecond-resolved sampling* 을 한다면 다음과 동치:

$$
\boxed{\Omega_1 := \Sigma_{\text{ret}} \times \mathbb{R}^+ \times \{R, L, M, S\}}
$$

(*시공간 × 광수용기 type* 격자.) 형식적으로 $\Omega_1$ 의 원소는 $(x, t, \tau)$ 로 *광수용기 sample point*. Sigma-algebra: $\mathcal{B}(\Sigma_{\text{ret}}) \otimes \mathcal{B}(\mathbb{R}^+) \otimes 2^{\{R, L, M, S\}}$ — product Borel × discrete. (이 sigma-algebra 도 axiom 외 carrier 측 데이터.)

각 sample point 위에 graded value $V(x, t, \tau) \in \mathbb{R}$ *부속됨* — Tier 2 + value attachment. **Value 가 구조적 본질이 아니라 부속**: σ_1 정의에 V 가 들어가지 않음.

**(b) σ_1 의 predicate**.

$$
\boxed{\sigma_1\big((x, t, \tau), (x', t', \tau')\big) :\iff \|x - x'\| < \delta_x \;\wedge\; |t - t'| < \delta_t \;\wedge\; \tau = \tau'}
$$

with $\delta_x, \delta_t$ 같은 parameter (변경 가능). (*같은 type 안에서 시공간 인접*.)

**(c) Axiom 검증**.
- **(Ω0)** sample point token 은 *graded value 가 부속물로* 따라붙으나, token identity 자체는 (x, t, τ) — opaque 처리 ✓
- **(σ1)** $\tau = \tau$ trivial, ball 자명 ✓
- **(σ2)** 모든 조건 (norm, abs, =) 대칭 ✓
- **(σ3)** Stage 0 과 동일 반례 (같은 τ 고정) ✓

**(d) σ-class analog**.
Receptive field overlap 의 cover. Single cone $\tau = L$ 의 σ_1-neighborhood 는 *cell membrane 의 인접 영역 + integration window*. 다른 type ($\tau = M$) 과는 σ_1 로 연결되지 *않음* — type-segregated covers.

이는 *Tier 2 + 1-mark* — Tier 2 의 가벼운 enrichment (type label 이 partition 을 induce, σ 가 partition 내부에서 추가 구조), 본질적 Tier 4 으로의 도약 아님.

### 2.3 Stage 2 — Multichannel inner retinal

**(a) Ω_2 의 형식 정의**.

$$
\boxed{\Omega_2 := \Sigma_{\text{ret}} \times \mathbb{R}^+ \times \mathcal{C}}
$$

(*시공간 × 채널 색인*.) Sigma-algebra: $\mathcal{B}(\Sigma_{\text{ret}}) \otimes \mathcal{B}(\mathbb{R}^+) \otimes 2^\mathcal{C}$.

**(b) σ_2 의 predicate**.

$$
\boxed{\sigma_2\big((x, t, c), (x', t', c')\big) :\iff \underbrace{\Big[\|x - x'\| < \delta_x \;\wedge\; |t - t'| < \delta_t \;\wedge\; c = c'\Big]}_{\text{within-channel locality}} \;\;\vee\;\; \underbrace{\Big[x = x' \;\wedge\; t = t' \;\wedge\; (c, c') \in \mathcal{P}_{\text{opp}}\Big]}_{\text{cross-channel opposition}}}
$$

with:
- $\delta_x, \delta_t$ 시공간 tolerance
- $\mathcal{P}_{\text{opp}} \subseteq \mathcal{C} \times \mathcal{C}$: *대립 채널 쌍의 집합* — biology-given (e.g., ON↔OFF, L↔M, S↔(L+M))

**두 종류의 인접**:
1. *Within-channel 시공간 인접* (기본)
2. *Cross-channel opposing pairs*: ON-OFF, L-M-S 의 *대립 쌍* 들이 같은 시공간 점에서 σ-연결

**(c) Axiom 검증**.
- **(Ω0)** channel token + value attachment (opaque token 처리) ✓
- **(σ1)** within-channel 분기: trivial. (단 cross-channel 분기는 $(c, c) \in \mathcal{P}_{\text{opp}}$ 일 필요 없음 — within-channel 가 reflexivity 를 cover) ✓
- **(σ2)** $\mathcal{P}_{\text{opp}}$ 가 *대칭 관계* 임을 가정 ($(c, c') \in \mathcal{P}_{\text{opp}} \Rightarrow (c', c) \in \mathcal{P}_{\text{opp}}$). 망막 회로의 wiring 이 이를 자연 만족. ✓
- **(σ3)** within-channel: §2.1 반례. Cross-channel: $\sigma_2(\text{ON-A}, \text{OFF-A}) \wedge \sigma_2(\text{OFF-A}, \text{ON-B})$ (만약 ON-A 와 ON-B 가 within-channel 으로 가까움 + OFF-A 와 OFF-B 가 가까움) 인데 $\neg \sigma_2(\text{ON-A}, \text{ON-B})$ 가능 — 다른 위치에서. 비추이 ✓

**(d) σ-class analog**.
σ_2-clique cover 가 매우 복잡: within-channel local patches + cross-channel single-point opposition. **이 이중 σ 구조** 가 stage 2 의 *완전한* 인접 관계. Cross-channel link 가 *biologically primitive* — 회로 wiring 이 이 link 를 직접 구현.

자연스러운 *부분 분할* 은 channel-equivalence $c = c'$ 만으로 — 그러나 이는 σ_2 가 *주는 분할이 아니라* underlying channel label *직접 사용*. σ_2 자체로부터의 canonical partition 은 *없음* (Prop 1.2 의 반복).

### 2.4 Stage 3 — Spike trains (다시 점과정)

**(a) Ω_3 의 형식 정의**.

$$
\boxed{\Omega_3 := \bigsqcup_{c \in \mathcal{C}_g} G_c = \{ (c, t) : c \in \mathcal{C}_g,\ t \in G_c \}}
$$

스파이크 사건들 — *다시 atomic 점들*. Sigma-algebra (carrier 측): $2^{\mathcal{C}_g} \otimes \mathcal{B}(\mathbb{R}^+)$. **Tier 2 토큰 불투명성 회복**: spike 는 spike — 부속 value 없음 (timing 자체가 정보).

**(b) σ_3 의 predicate**.

$$
\boxed{\sigma_3\big((c_i, t_i), (c_j, t_j)\big) :\iff |t_i - t_j| < \tau \;\wedge\; d_{\text{topo}}(c_i, c_j) < \delta_c}
$$

with:
- $\tau > 0$: spike coincidence window (e.g., $\sim 5\,ms$)
- $d_{\text{topo}} : \mathcal{C}_g \times \mathcal{C}_g \to \mathbb{R}^+$: *topological* distance on channel set (e.g., spatial position of corresponding ganglion cells; channel type proximity)
- $\delta_c > 0$: channel topology tolerance

**중요한 미묘함**: $d_{\text{topo}}$ 의 *존재* 가 Tier 3 (의사거리) 처럼 *보일 수 있으나*, σ_3 정의에서는 $d_{\text{topo}}$ 의 *수치* 가 사라지고 *binary threshold* 만 남음. 즉 σ_3 는 *Tier 3 도구로 정의된 Tier 2 관계*. ([[#13. 더 높은 Tier 의 확장|§13]] 의 "Tier 2 contract" 와 정합.)

**(c) Axiom 검증**.
- **(Ω0)** spike token 은 *오직 시각 + 채널 ID* — 진폭 없음, 파형 없음 ✓
- **(σ1)** $(c, t) = (c, t)$ → $0 < \tau$, $d_{\text{topo}}(c, c) = 0 < \delta_c$ ✓
- **(σ2)** $|t_i - t_j| = |t_j - t_i|$, $d_{\text{topo}}$ 가 metric 가정 (symmetric) ✓
- **(σ3)** 시간 ball 반례 + 채널 topology ball 반례 (overlap 한 receptive fields) ✓

**(d) σ-class analog**.
스파이크 *synchrony cluster* (시간 window 내 + 인접 채널 set). 다시 *cover*, *partition 아님*. *Spike volley*, *population burst* 등의 신경과학 용어가 이 cluster 의 직관적 대응.

### 2.5 Stage 4 — 시신경 도착

**(a) Ω_4 의 형식 정의**.

Stage 3 와 동일 형식, 단 *latency 보정* 후의 timing 사용:

$$
\Omega_4 := \Omega_3 \text{ with } t \to t + \tau_{\text{latency}}(c)
$$

with $\tau_{\text{latency}} : \mathcal{C}_g \to \mathbb{R}^+$ a fixed channel-specific delay (M cell ≈ 30 ms, P cell ≈ 60 ms etc.).

**(b) σ_4 의 predicate**.
$\sigma_4$ 는 $\sigma_3$ 와 동일 form (인과적 latency 보정 후 timing 사용).

**(c) Axiom 검증**.
Latency shift 는 *time translation by channel-dependent constant* — σ_3 의 axioms 보존. ✓

**(d) σ-class analog**.
σ_3 와 동일 (latency 가 spike 간 *간격* 을 channel pair 마다 일관되게 shift).

### 2.6 Stage 매핑 요약

| Stage | $\Omega_i$ | 핵심 σ_i 형식 | Carrier sigma-algebra | 토큰 종류 |
|------|-----------|-------------|---------------------|---------|
| 0 | Photon events | 시공간 ball | $\mathcal{B}(\Sigma_{\text{ret}} \times \mathbb{R}^+ \times \Lambda)$ | atomic event |
| 1 | Photoreceptor samples | 시공간 ball + type 동일 | product Borel × discrete | sample + value attach |
| 2 | Channel samples | within-channel ball ∨ cross-opposition | product Borel × discrete | sample + value attach |
| 3 | Spike events | 시간 ball + channel-topology ball | $2^{\mathcal{C}_g} \otimes \mathcal{B}(\mathbb{R}^+)$ | atomic event |
| 4 | Latency-shifted spikes | $\sigma_3$ form on shifted times | (same as 3) | atomic event |

---

## 3. σ Propagation — Kernel 의 functorial 작용

### 3.1 핵심 질문

Stage $i-1$ 의 (Ω_{i-1}, σ_{i-1}) 가 stage $i$ 로 propagate 되는가? Kernel $\mathcal{K}_i$ 가 σ 를 *어떻게* 변환하는가?

### 3.2 σ-pushforward 정의 — Deterministic case

**Definition 3.1 (Deterministic σ-pushforward)**. Source Tier 2 객체 $(\Omega_{i-1}, \sigma_{i-1})$ 와 deterministic map $f_i : \Omega_{i-1} \to \Omega_i$ 가 주어졌을 때 (즉 $\mathcal{K}_i = \delta_{f_i}$), *pushed σ-structure on $\Omega_i$* 는:

$$
\boxed{\sigma_i^{\text{pushed}}(y_1, y_2) :\iff \exists x_1, x_2 \in \Omega_{i-1} : \sigma_{i-1}(x_1, x_2) \;\wedge\; f_i(x_1) = y_1 \;\wedge\; f_i(x_2) = y_2}
$$

**Properties**:
- $\sigma_i^{\text{pushed}}$ 는 자동으로 *symmetric* (σ_{i-1} 의 대칭성에서)
- $\sigma_i^{\text{pushed}}$ 의 reflexivity 는 $f_i$ 가 *surjective* 일 때 자동 (각 $y$ 에 대해 $\exists x : f(x) = y$, 그리고 $\sigma_{i-1}(x, x)$); 일반적으로는 $y \in \text{im}(f)$ 에 한정해야 함
- $\sigma_i^{\text{pushed}}$ 의 non-transitivity 는 *자동으로 유지되지 않음* — pushforward 가 transitive 한 σ 를 만들 수 있음 (예: f 가 constant 이면 모두 σ-연결, transitive)

**Definition 3.2 (σ-confluent map)**. Deterministic $f : (\Omega, \sigma) \to (\Omega', \sigma')$ 가 *σ-confluent* 라 함은:

$$
\sigma(x, y) \Rightarrow \sigma'(f(x), f(y))
$$

(σ 를 *위배하지 않음*: 입력에서 인접하면 출력에서도 인접.)

**Proposition 3.3 (σ-confluent maps form a subcategory)**. 
- *Identity*: $\text{id} : (\Omega, \sigma) \to (\Omega, \sigma)$ 는 σ-confluent (자명).
- *Composition*: $f, g$ σ-confluent → $g \circ f$ σ-confluent.
- 따라서 $(\text{Tier 2 객체}, \text{σ-confluent maps})$ 는 카테고리 — 이를 $\mathbf{Tier2}$ 라 부름 ([[#6. Functorial / Categorical 정식화 (preview)|§6]] 에서 정식).

**Proof sketch**. Composition: $\sigma(x, y) \Rightarrow \sigma'(f(x), f(y)) \Rightarrow \sigma''(g(f(x)), g(f(y))) = \sigma''((g \circ f)(x), (g \circ f)(y))$. ✓

**Note**: $\sigma_i^{\text{pushed}}$ 와 $\sigma_i^{\text{natural}}$ (stage 별로 §2 에서 정의된 자연스러운 σ_i) 의 *관계* 가 functoriality 의 핵심 — §3.3 에서 stage-by-stage.

### 3.2.1 Stochastic case

Deterministic case 의 §3.2 정의가 stochastic 으로 확장:

**Definition 3.4 (Stochastic σ-pushforward)**. Markov kernel $\mathcal{K}_i : \Omega_{i-1} \to \Omega_i$ 와 source $(\Omega_{i-1}, \sigma_{i-1})$ 에 대해:

$$
\sigma_i^{\text{push}, \theta}(y_1, y_2) :\iff \Pr_{(X_1, X_2)} \big[ \sigma_{i-1}(X_1, X_2) \;\big|\; Y_1 = y_1, Y_2 = y_2 \big] > \theta_\sigma
$$

with threshold $\theta_\sigma \in (0, 1)$ (e.g., 0.5). 이는 *probabilistic* σ-extension — Tier 2 의 가벼운 fuzzification.

**Σ propagation 의 의미** (정확히):
- *Deterministic case*: σ 가 *exactly* push 됨 — set-theoretic 정의.
- *Stochastic case*: σ 가 *probabilistically* push 됨 — measure-theoretic 정의, threshold-dependent.

본 디렉토리는 *binary* σ 를 유지 (deterministic). Probabilistic σ 는 [[08_open_problems_sp|08]] 의 별도 OP.

### 3.3 Stage 별 확인

각 transition $i \to i+1$ 에 대해 *세 가지 데이터*: kernel $\mathcal{K}_i$, source σ_{i-1}, computed pushed σ_i. 그리고 *naturally-defined* σ_i 와 비교. *Direction of difference* (expansion / contraction / mismatch) 식별.

#### 3.3.1 Transition 0 → 1 (Photon → Photoreceptor)

- **Kernel** $\mathcal{K}_1$: 광자 → 광수용기 적분. 각 광자 $(x, t, \nu)$ 가 인접 photoreceptor $\tau$ 에 *공간-local + 시간-local* contribution.
- **Source σ_0**: $\|x_i - x_j\| < \delta_x \wedge |t_i - t_j| < \delta_t$ (photon 들 사이).
- **Pushed σ_1^{push}**: 두 photoreceptor sample $(x, t, \tau), (x', t', \tau')$ 가 *광자 한 쌍 ($\sigma_0$-인접) 에 의해 동시에 자극* 된 경우. 광자 ($x_p$, $t_p$) 가 photoreceptor $(x, t)$ 에 contribute 는 *$\|x - x_p\| < r_{\text{rec}}$* 그리고 $0 < t - t_p < r_{\text{int}}$. 합성하면: σ_1^{push}((x, t, τ), (x', t', τ')) 가 $\sigma_0$-pair 에 의해 induced.
- **Natural σ_1**: §2.2 정의.
- **비교**: σ_1^{push} ⊆ σ_1^{natural} (typically; pushed 는 *photon-mediated* 인접만 잡고, σ_1^{natural} 는 *photoreceptor sample grid* 위의 ball). *Direction*: pushed 가 *narrower* — natural 이 expand 함.
- **Functoriality status**: σ-confluent (pushed implies natural for compatible $\delta$ choices) ✓. *Expansion* 정도는 parameter $\delta_x, \delta_t, r_{\text{rec}}, r_{\text{int}}$ 의 관계로 quantify 가능.

#### 3.3.2 Transition 1 → 2 (Photoreceptor → Channel)

- **Kernel** $\mathcal{K}_2$: DoG center-surround + ON/OFF split + chromatic opponency.
- **Source σ_1**: within-type 시공간 ball.
- **Pushed σ_2^{push}**: 두 channel sample 이 *σ_1-인접 photoreceptor pair* 에서 derive. DoG 의 *surround radius* $\sigma_s$ 가 photoreceptor radius 보다 크므로 *공간적 확장*. ON/OFF split 은 *type* 차원에서 *분할* (한 photoreceptor 의 +/- contribution 이 두 다른 channel 로). Opponency 는 *cross-type linkage* 를 만듦.
- **Natural σ_2**: §2.3 정의 — within-channel ball + cross-channel opposition.
- **비교**: σ_2^{push} *fundamentally* expands σ_1 in *two* directions:
  - (i) *공간 expansion*: DoG surround $\sigma_s \gg \delta_x$.
  - (ii) *Cross-channel expansion*: opponency link 가 *없던* 인접을 만듦.
- **Direction of difference**: *strict expansion*. σ_1^{push} ⊊ σ_2^{natural} 와 (조정된 parameter 로) σ_2^{push} ≈ σ_2^{natural}. 본 stage 가 *유일하게 strict-expansion* 인 stage.
- **Functoriality status**: σ-confluent ✓, *non-trivially*. Kernel 의 *biologically primitive cross-channel wiring* 이 σ-expansion 의 원천.

#### 3.3.3 Transition 2 → 3 (Channel field → Spike)

- **Kernel** $\mathcal{K}_3$: pool over channel sample $\to$ rate $\lambda_c(t) \to$ inhomogeneous Poisson (or Cox) sampling.
- **Source σ_2**: within-channel ball + cross-opposition.
- **Pushed σ_3^{push}**: 두 spike $(c_i, t_i), (c_j, t_j)$ 가 *σ_2-인접 channel sample* 에서 derive. *Channel pooling* 이 *공간 평균* — σ_2 의 spatial ball 이 ganglion cell 의 receptive field 로 *projected*. *Cross-opposition* link 가 *동일 receptive field 의 ON/OFF 한 쌍* 으로 mapping — but separate ganglion types.
- **Natural σ_3**: §2.4 정의 — 시간 ball + channel topology ball.
- **비교**: σ_3^{push} ⊆ σ_3^{natural} (approximately):
  - 시간 차원: spike timing 이 channel input 의 시간 profile 을 *delay + jitter* 후 reflect. σ_2 시간 ball ≈ σ_3 시간 ball (with $\tau_{\text{spike}} \approx \delta_t + \tau_{\text{jitter}}$).
  - 채널 차원: σ_2 cross-opposition 이 σ_3 의 *대립 ganglion type 인접* 으로 대응 — *natural 한 d_topo* 에 포함.
- **Direction of difference**: *approximate match*, small expansion from temporal jitter.
- **Functoriality status**: σ-confluent (conditional on parameter compatibility) ✓.

#### 3.3.4 Transition 3 → 4 (Spike → Optic nerve)

- **Kernel** $\mathcal{K}_4$: pure latency shift $t \to t + \tau_{\text{latency}}(c)$.
- **Source σ_3**: 시간 ball + channel topology ball.
- **Pushed σ_4^{push}**: 시간 차이가 보존 (channel-dependent constant shift 는 *상대 시각 차이* 를 동일 channel pair 에서 보존, 다른 channel pair 에서 $\Delta \tau_{\text{latency}}$ 만큼 shift).
- **Natural σ_4**: §2.5 정의.
- **비교**: 동일 channel pair: exact match. 다른 channel pair: timing 이 $\Delta \tau_{\text{latency}}$ 만큼 *uniform shift*; σ_4 가 *cross-channel timing* 을 *재정의* 함으로써 흡수.
- **Direction of difference**: trivial expansion / no expansion.
- **Functoriality status**: σ-confluent ✓ trivially.

#### 3.3.5 요약 table

| 단계 | σ pushforward 가 σ_i 와 일치? | Direction | 메커니즘 | Functoriality |
|------|----|----------|---------|--------------|
| 0→1 | pushed ⊆ natural (expansion in natural) | natural expand | photon-to-receptor pooling | confluent |
| 1→2 | pushed expand significantly | *strict expansion* | DoG surround + opponency | confluent, non-trivial |
| 2→3 | pushed ≈ natural | minor expansion (jitter) | rate-coded Poisson | confluent (conditional) |
| 3→4 | pushed = natural (after re-parameterization) | trivial | latency shift | confluent trivially |

따라서 *대부분 stage 에서 σ 가 naturally propagate*. 단 1→2 가 *expansion* — surround 가 σ 를 확장.

### TC-SP-5.1 — [DELETED 2026-05-25 Pass 3]

**Status**: **DELETED via Pass 3 adversarial verification** (3-pattern HOLE: #18 tautology + #40 too-clean lemma + #5 hypothesis recheck).

**Original statement (preserved for audit trail)**:

> 각 stage 의 σ-pushforward 가 *그 stage 의 자연스러운* σ_i 와 일치 — σ propagation 이 *functorial*: $\mathcal{K}_i^\flat : (\Omega_{i-1}, \sigma_{i-1}) \to (\Omega_i, \sigma_i)$ for all 4 transitions.

**Refute basis** (Pass 3 verifier votes — 3 of 4 HOLE):

- **#18 (tautology)**: $\sigma_i$ 가 pushed σ 를 흡수하도록 *post-hoc 정의* (1→2 transition 에서 σ_2^natural 이 DoG output structure 까지 포함하도록 expanded). "Non-trivial functoriality" label 이 engineering 의 wrapper.
- **#40 (too-clean general lemma)**: General form 의 obvious counterexamples — *constant map* 은 모든 σ-pair 를 diagonal 로 push (pushed σ trivial); *broadly-mixing kernel* 은 pushed σ 가 empty/universal; σ-confluence 는 kernel 과 target tolerance 의 *specific compatibility* 요구 — generic 아님.
- **#5 (hypothesis recheck)**: 5-stage retinal instance 의 verification 이 *case-by-case* + *regularity 가 required 만 stated, not verified* (DoG 는 non-compact support, but compact-support 가정됨).

**Why deleted**: General functoriality 는 *false-as-stated*. 5-stage case-by-case verification 은 정리가 아니라 *case analysis*. 본 directory 본문 의 case analysis (§3.3.1–3.3.4) 자체는 유지하나, "functorial 정리" 로서의 TC-SP-5.1 자격 박탈.

**Replacement (없음)**: σ propagation 의 5-stage case analysis 는 *empirical descriptive observation* 으로 격하 (§3.3 본문 유지; TC 라벨 없음). General functoriality 의 *regularity condition 의 형식화* 는 추후 OP candidate (08 §6 의 OP-SP-(future) 로 등록 deferred).

---

## 4. Tier 2 Closure of the Pipeline

### TC-SP-5.2 — [DELETED 2026-05-25 Pass 3]

**Status**: **DELETED via Pass 3 adversarial verification** (3-pattern HOLE: #18 tautology + #40 too-clean + #5 hypothesis recheck; **저자 본인이 이전 §4 에서 "증명 어려움. '본질적으로 요구하지 않는다' 의 완전 형식화" 라고 meta-OP 임을 명시 admit**).

**Original statement (preserved for audit trail)**:

> 전체 SSKP 가 Tier 2 카테고리 *내부에서 닫혀 있음*: 임의의 stage 가 *Tier 4 metric 또는 vector 구조를 본질적으로 요구하지 않는다*.

**Refute basis** (3 of 4 patterns HOLE — strongest refute in Pass 3):

- **#18 (tautology)**: σ_i 가 *Tier 4 norm 으로 계산되지만 binary threshold 후 Tier 2 label* — definitional fiat. 저자 §4 명시적 admit.
- **#40 (too-clean lemma)**: Stage 1 의 SDE drift $-\tau^{-1}(V - V_{\text{rest}}) dt + \sigma dW$ 가 본질적으로 Tier 4 vector structure 요구; "implementation tool vs. axiom-level data" 의 distinction 이 형식화 안 됨 (조건부 인용에 의해 자명).
- **#5 (hypothesis recheck)**: Tier 2 closure 가 category-theoretic forgetful functor 의 *not-yet-constructed* 형식에 의존; threshold parameter 자체가 Tier 3 datum.

**Why deleted**: Definitional fiat (Tier 4 도구로 계산 후 binary 라고 label 만 함). 저자 본인이 "vague 함을 인정" — 정리 자격 아님.

**Replacement (없음)**: Stage 별 σ_i 의 *operational binary form* 의 descriptive observation 은 §2 본문 유지. *Tier 2 closure 의 formal forgetful functor* 구성은 추후 OP candidate (08 §6 의 OP-SP-(future) 로 등록 deferred). Definition 4.1, 4.2 본문 자체는 *definition* 으로 격하 (TC 라벨 없음).

**증명 어려움**. "본질적으로 요구하지 않는다" 의 *완전 형식화* — Tier 4 구조 (예: 합성곱의 미분 연산) 가 *implementation* 에 사용되나, *output structure* 는 Tier 2. 이 구별의 *category-theoretic* 형식화 (예: "Tier 2 의 axiom data 가 forgetful functor 의 fiber") 는 OP — meta-OP.

**의미**: 이론 자체가 *minimal 구조 위에서 닫혀 있음* — Tier 4 의 강한 구조 (Hilbert space, metric, etc.) 가 *분석 도구* 로는 쓰이나 *대상 구조* 가 아님. 이게 사용자의 *minimal 가공* commit 의 *수학적 보증*. Tier 2 commitment 가 파이프라인 전체에서 유지됨.

---

## 5. 점 ↔ 장 ↔ 점 순환

### 5.1 결정적 관찰

```
Stage 0 (점과정) → Stage 1 (장) → Stage 2 (장) → Stage 3 (점과정) → Stage 4 (점과정)
```

**Stage 0 과 Stage 3 가 *둘 다 점과정***. 위상학적으로 *동일 종류*. 이는 우연이 아닐 수 있음.

### 5.2 형식

Stage 0: 광자 점과정 — *물리적 자극의 원자 사건*
Stage 1-2: graded field — *연속적 표현 / 적분*
Stage 3: 스파이크 점과정 — *생물학적 응답의 원자 사건*

순환의 의미: 자극과 응답이 *같은 위상학적 형식* — *원자적, 시간 indexed, 시공간 locality 가짐*. 둘 사이의 *graded field* 는 *내부 처리의 임시 표현*.

### 5.3 (Ω, σ) 관점에서

Stage 0 의 (Ω_0, σ_0) 와 Stage 3 의 (Ω_3, σ_3) 가:
- 둘 다 *atomic 토큰* (점들)
- 둘 다 *시공간 인접 σ*
- 둘 다 *불투명* (값 없음)

차이:
- Ω_0 = 광자 사건, Ω_3 = 스파이크 사건
- σ_0 의 토폴로지 = 망막 표면 + 시간 + 파장
- σ_3 의 토폴로지 = 신경절세포 set + 시간

**둘 다 Tier 2 의 *순수* 인스턴스**. Stage 1-2 는 Tier 2 + value/channel attachments — *덜 순수*.

### 5.3.1 Category-theoretic view

본 절은 §6 의 정식 카테고리를 *미리 사용* 하여 cycle 의 구조를 분명히 함.

**Definition 5.1 (Tier 2 sub-categories)**.

- $\mathbf{Tier2}_{\text{pt}}$: *point Tier 2* — objects 가 $(\Omega, \sigma)$ with $\Omega$ purely atomic (no value attach), σ a tolerance relation. Examples: $(\Omega_0, \sigma_0)$, $(\Omega_3, \sigma_3)$, $(\Omega_4, \sigma_4)$.
- $\mathbf{Tier2}_{\text{val}}$: *Tier 2 with value attachments* — objects 가 triples $(\Omega, \sigma, V)$ with $V : \Omega \to \mathcal{V}$ a value mapping (V 가 σ 정의에 들어가지 않으나 데이터로 carry). Examples: $(\Omega_1, \sigma_1, V_1)$, $(\Omega_2, \sigma_2, V_2)$.

$\mathbf{Tier2}_{\text{pt}} \hookrightarrow \mathbf{Tier2}_{\text{val}}$ (point objects 는 trivial value, e.g., singleton $\mathcal{V}$).

**Cycle 의 functorial view**:

$$
\underbrace{(\Omega_0, \sigma_0)}_{\mathbf{Tier2}_{\text{pt}}} \xrightarrow{\bar{\mathcal{K}}_1} \underbrace{(\Omega_1, \sigma_1, V_1)}_{\mathbf{Tier2}_{\text{val}}} \xrightarrow{\bar{\mathcal{K}}_2} \underbrace{(\Omega_2, \sigma_2, V_2)}_{\mathbf{Tier2}_{\text{val}}} \xrightarrow{\bar{\mathcal{K}}_3} \underbrace{(\Omega_3, \sigma_3)}_{\mathbf{Tier2}_{\text{pt}}} \xrightarrow{\bar{\mathcal{K}}_4} \underbrace{(\Omega_4, \sigma_4)}_{\mathbf{Tier2}_{\text{pt}}}
$$

각 morphism 은 σ-confluent. *Boundary* (start, end) 는 *pure point subcategory*; *interior* 는 *value-enriched subcategory*. *Forgetful* $\mathbf{Tier2}_{\text{val}} \to \mathbf{Tier2}_{\text{pt}}$ 가 $V$ 잊음.

**Functorial transitions**:
- $\bar{\mathcal{K}}_1$ (point → value): *attachment* — value 가 추가됨 (장 응답).
- $\bar{\mathcal{K}}_2$ (value → value): *value transformation* (DoG 등).
- $\bar{\mathcal{K}}_3$ (value → point): *detachment* — value 가 다시 잊혀짐 (rate → spike).
- $\bar{\mathcal{K}}_4$ (point → point): *trivial* (latency shift).

이 *attachment / transformation / detachment / shift* 의 4-step cycle 이 sensing pipeline 의 *purist categorical 구조*.

### 5.4 정보론적 의미 — Compression bit accounting

- *Atomic-to-atomic* mapping: photon arrival ⟶ spike emission. 정보 손실 + reformulation.
- *Compression ratio*: $10^9$ photons/sec → $10^6$ spikes/sec ≈ $10^3$ 압축.
- *Bandwidth conservation*: 비록 압축이 크나 *모든 양자 사건이 어떻게든 응답에 contribute*.

**Bit-level accounting** (cite [[06_endtoend_information_bound#TC-SP-4.1|TC-SP-4.1]] + [[05_stage3_ganglion_spike_encoding#TC-SP-3.3|TC-SP-3.3]]):

| Quantity | Stage 0 | Stage 3 | Compression |
|----------|---------|---------|-------------|
| Token rate | $\sim 10^9$ photons/sec | $\sim 10^6$ spikes/sec | $\sim 10^3 \times$ |
| Bits per token | $\sim 1$ bit (binary detection) | $\sim 5$ bits (timing + channel) | $\sim 5 \times$ recovery |
| Total bit rate | $\sim 10^9$ bits/sec | $\sim 5 \times 10^6$ bits/sec | $\sim 200 \times$ |
| (Ω, σ) cardinality per sec | $\sim 10^9$ tokens | $\sim 10^6$ tokens | $\sim 10^3 \times$ |

**핵심**: Compression 은 *token rate* 에서 일어남 (10^3×); *bit per token* 은 *증가* (1 → 5 bits) — Stage 3 의 spike timing 이 *더 풍부한 token semantics* 를 담음.

**Tier 2 측면**: |Ω_0| 가 |Ω_3| 보다 $\sim 1000 \times$ 큼 — Tier 2 객체의 *원소 수* 가 줄어듦. 그러나 σ_3 의 *clique 풍부도* 는 *증가* (cross-channel topology, temporal coincidence patterns) — Tier 2 의 *관계 풍부도* 가 token 수 감소를 보상.

**TC-SP-3.3 와의 정합**: Stage 3 의 rate-distortion ($\sim 126:1$ peripheral compression) 가 본 *token 수 압축* 의 *bit-level mirror*.

### 5.5 SCC 의 $u_t$ 와의 관계 (OP-SP-006)

SCC 의 primitive $u_t : X_t \to [0,1]$ 는 *graded field* — 즉 Stage 1 또는 Stage 2 에 대응하는 듯. 그러나:

- $u_t$ 는 *지각 장* — 즉 *주체에 도달한 후* 의 상태
- 위 순환에서 Stage 3 의 출력 (스파이크) 가 *뇌가 받는 입력*
- 그렇다면 $u_t$ 는 *Stage 3 이후 cortical 재구성* 의 결과?

### OP-SP-006 (확장 분석)

**Status**: OPEN. Severity: High.

**문제**: SCC 의 $u_t$ 가 본 sensing pipeline 의 *어디에 위치*?

본 절은 4 candidates 각각에 대해 *심층 분석* (해석 / SCC axiom 호환성 / 경험적 증거):

#### Candidate 1: Pre-Stage 0 ($u_t$ = world cohesion field)

**해석**: $u_t : X_t \to [0,1]$ 가 *물리적 세계의 cohesion* — 광자 도래 *이전*. 세계 자체가 *이미 부분적으로 응고된 형성* 의 장.

**SCC axioms 호환성**:
- *자연*: A3 (closure stabilization tendency) 가 *물리적 안정성* 으로 직관적 — 안정 상태의 객체 (산, 돌) 가 stable formation.
- *자연*: 닫힘 / 분리 / 경계 / 수송 *모두* 물리적 의미 직설.
- *어색*: $X_t$ 가 *세계의 어느 점인가*? 광원? 물체 표면? 산란점? — 세계의 *연속체* 와 *이산 그래프* 의 다리 불명.
- *어색*: SCC 가 *지각 이론* 이라는 framing 과 충돌 — physics 로 환원.

**경험적 증거**:
- 지지: object permanence (Piaget) — 영아가 *세계의 객체* 를 *지각 이전에* 가정함을 보임. *Pre-perceptual object* 의 인지심리학적 후보.
- 반대: physics 가 $u_t$ 같은 *graded cohesion* 을 사용하지 않음 — quantum field 는 *complex amplitude*, classical field 는 *real-valued* scalar/vector. SCC 와 직접 대응 없음.
- 중립: cosmology 의 *structure formation* (matter density field, density contrast) 가 *부분적* 유비 — Zeldovich pancakes, halo formation. 그러나 SCC 의 [0,1] 범위와 다름.

**판정 잠정**: *philosophically attractive, empirically thin*. SCC 를 *physics-of-formation* 으로 재구성해야 함 — 큰 commitment.

#### Candidate 2: Stage 1-2 ($u_t$ = retinal field)

**해석**: $u_t$ 가 *광수용기 + 양극세포 응답 장* — 즉 망막 내부의 graded representation. SCC 가 *retinal dynamics* 이론.

**SCC axioms 호환성**:
- *자연*: 광수용기 응답이 *연속 graded 값* — $u_t \in [0,1]$ 와 형식 호환 (정규화 후).
- *자연*: receptive field overlap → 이웃 픽셀 간 cohesion → closure operator 의 직관적 대응.
- *어색*: A3 stabilization 이 망막에서 *반응 시상수* (~10-50 ms) 와 충돌 — 망막 응답은 *transient*, *not stably stable*.
- *어색*: 경계 / 분리가 *DoG zero-crossing 의 binary edge* 이지 *gradient field* 가 아님 — SCC 의 $E_{\text{bd}}$ 와 형식 불일치.
- *심각*: 망막 dynamics 가 *milliseconds* 인데 SCC formation 이 *cognitive timescale* (~100ms-seconds) 을 implicit 가정.

**경험적 증거**:
- 지지: receptive field linearity (Hartline, Kuffler) — 광수용기-양극세포가 linear filter 이고, SCC 의 $E$ 항이 *quadratic* — first-order Taylor 호환.
- 반대: 망막에서 *형성된 객체* 의 *상관물* (correlate) 부재 — 객체성은 *upstream cortical area* (V2, IT) 에 인코딩.
- 강력 반대: foveal vs peripheral differential — 망막은 *uniform graph 가 아님* — SCC 의 $G$ 가 *균질* 가정과 충돌.

**판정 잠정**: *empirically discordant*. SCC 가 망막 수준이면 receptive field 와 cortical 객체성의 gap 을 SCC 가 *내부* 에 흡수해야 함 — overstretch.

#### Candidate 3: Stage 3 output functional ($u_t$ = spike-derived rate field)

**해석**: $u_t$ 가 *스파이크 trains 의 어떤 functional* — e.g., 시공간-smoothed rate. $u_t(x) = (G_\sigma * \text{rate})(x, t)$.

**SCC axioms 호환성**:
- *자연*: spike rate 가 *graded scalar* — $[0, \lambda_{\max}]$ 정규화 후 $[0, 1]$ 에 mapping.
- *자연*: 각 spike → contribute to rate field → cohesion 의 *additive* 구성 자연.
- *어색*: SCC 의 *graph* $G$ 가 *어떤 자연적 topology* 인가? Ganglion cell array 의 receptive field overlap graph? — 그럴 듯하나 *post-hoc*.
- *어색*: spike Poisson noise 가 SCC 의 *deterministic gradient flow* 와 호환 안 됨 — *expected rate* level 에서만 SCC 적용.
- *문제*: spike → smoothing 의 *time constant* 가 SCC 의 *formation time* 과 일치해야 함 — 검증 필요.

**경험적 증거**:
- 지지: population rate coding (Georgopoulos, Pouget) — population vector / rate field 가 *cortical object representation* 의 표준 모델. SCC 의 $u_t$ 가 이 *population rate* 의 추상화일 수 있음.
- 지지: V1 의 *orientation map* 이 graded scalar field — SCC 와 직접 형식 호환.
- 반대: spike-derived rate 가 *V1 input* 이지 *V1 output* 이 아님 — perceptual 객체성은 *higher visual area* — Candidate 4 와 경쟁.

**판정 잠정**: *empirically supported (cortical input level)*. SCC 가 *V1 input rate field* 이면 receptive field overlap graph 가 *자연 $G$*. 가장 *concrete* 한 candidate.

#### Candidate 4: Post-Stage 4 ($u_t$ = cortical reconstruction)

**해석**: $u_t$ 가 *cortical 재구성* — V1, V2 이후의 perceptual representation. SCC 가 *cortical theory*.

**SCC axioms 호환성**:
- *자연*: A3 (stabilization) ↔ cortical attractor dynamics (Hopfield, Amit) — 매우 잘 맞음.
- *자연*: 객체성 emergence 가 *cognitive* 사건 — SCC 의 *formation* 과 일치.
- *자연*: closure / separation / boundary 가 *perceptual binding / segmentation* 의 cortical correlates 와 일치 (Tononi, Singer).
- *어색*: $G$ 가 *어떤 cortical graph* 인가? V2/V4 의 lateral connectivity? Cross-area? — *덜 명확*.
- *복잡*: cortical 동역학이 *attention*, *top-down*, *prior* 에 의해 modulate — SCC 가 이를 *parameters* 로 흡수해야.

**경험적 증거**:
- 강력 지지: bistable perception (Necker cube, binocular rivalry) — *형성된 객체* 가 *unstable* between two minima — SCC 의 *multiple critical points* 와 일치.
- 지지: Gestalt phenomena (closure, proximity) — *perceptual* 현상이지 *retinal* 현상이 아님.
- 지지: object-based attention — 객체 가 *attention 의 단위* 임을 보여줌. SCC 의 *formation = attention 단위*?
- 중립: cortical area 의 *어떤* level 인지 unclear — V4? IT? prefrontal?

**판정 잠정**: *philosophically most coherent, empirically supported by Gestalt + bistable*. SCC 가 *cortical formation theory*. *Most likely candidate*.

#### Multi-candidate summary table

| Candidate | Naturalness | Awkwardness | Empirical | Verdict |
|-----------|-----------|------------|-----------|---------|
| 1 (Pre-0) | Physics 직설 | Pipeline framing 충돌 | thin | overlay-only |
| 2 (Stage 1-2) | Filter 호환 | Timescale 충돌 | discordant | unlikely |
| 3 (Stage 3 out) | Population rate | Post-hoc graph | supported (V1 input) | viable concrete |
| 4 (Post-4) | Attractor / Gestalt | Graph 정의 모호 | strongly supported | most likely |

**본 디렉토리의 입장**: *결정하지 않음*. 본 sensing pipeline 은 Stage 0-4 만 다루며, $u_t$ 가 어디인지는 후속 작업 (PAI 와의 다리 또는 SCC 의 새 layer). 가장 *경험적으로* 지지 받는 candidate 는 4, 가장 *concretely formalizable* 한 candidate 는 3. 두 candidate 의 *직렬 조합* (Stage 3 → cortical-extended) 도 가능.

---

## 6. Functorial / Categorical 정식화 (확장)

### 6.1 Tier 2 카테고리 — 정식 정의

**Definition 6.1 (The category $\mathbf{Tier2}$)**.

- **Objects**: tolerance spaces $(\Omega, \sigma)$ — pairs satisfying (Ω0, σ1, σ2, σ3) of §1.0.
- **Morphisms**: σ-confluent maps $f : (\Omega, \sigma) \to (\Omega', \sigma')$ — set-functions satisfying
$$\sigma(x, y) \Rightarrow \sigma'(f(x), f(y))$$
for all $x, y \in \Omega$.

**Composition**: ordinary function composition (set-theoretic).

**Identity**: identity function on each $\Omega$.

**Verification of category axioms**:
- *Identity confluent*: $\sigma(x, y) \Rightarrow \sigma(\text{id}(x), \text{id}(y)) = \sigma(x, y)$. ✓
- *Composition confluent* (Prop 3.3): $f, g$ confluent $\Rightarrow g \circ f$ confluent. ✓
- *Associativity*: function composition is associative. ✓
- *Identity laws*: $f \circ \text{id} = f = \text{id} \circ f$. ✓

따라서 $\mathbf{Tier2}$ 는 *well-defined* category. (이는 *그래프 카테고리* $\mathbf{Grph}$ 의 변종 — symmetric, reflexive graph 와 graph homomorphism.)

### 6.2 카테고리 구조의 성질

#### 6.2.1 Products in $\mathbf{Tier2}$

**Proposition 6.2 (Binary product)**. $(\Omega_1, \sigma_1) \times (\Omega_2, \sigma_2) := (\Omega_1 \times \Omega_2, \sigma_\times)$ with
$$\sigma_\times((x_1, x_2), (y_1, y_2)) :\iff \sigma_1(x_1, y_1) \;\wedge\; \sigma_2(x_2, y_2)$$
는 categorical product (universal property: 유일한 mediating map from any third object).

**Proof sketch**: σ_× 가 reflexive (자명), symmetric (componentwise), non-transitive (componentwise inheritance). Projections $\pi_i$ confluent: $\sigma_\times \Rightarrow \sigma_i$ on $i$-th component. Universal property: $f : (\Omega, \sigma) \to (\Omega_1, \sigma_1) \times (\Omega_2, \sigma_2)$ confluent iff both components $f_i$ confluent.

#### 6.2.2 Coproducts in $\mathbf{Tier2}$

**Proposition 6.3 (Binary coproduct)**. $(\Omega_1, \sigma_1) \sqcup (\Omega_2, \sigma_2) := (\Omega_1 \sqcup \Omega_2, \sigma_\sqcup)$ with
$$\sigma_\sqcup(z_1, z_2) :\iff (z_1, z_2 \in \Omega_1 \wedge \sigma_1(z_1, z_2)) \;\vee\; (z_1, z_2 \in \Omega_2 \wedge \sigma_2(z_1, z_2))$$
는 categorical coproduct.

**Proof sketch**: standard from disjoint union construction. *Cross-component* σ 가 *empty* — 다른 component 의 원소는 σ-관계 없음.

#### 6.2.3 Kernels / equalizers

**Proposition 6.4 (Equalizers exist)**. For $f, g : (\Omega, \sigma) \to (\Omega', \sigma')$ both confluent, the equalizer is $(\text{Eq}(f, g), \sigma|_{\text{Eq}})$ where $\text{Eq}(f, g) = \{x : f(x) = g(x)\}$ and σ restricts.

**Proof sketch**: $\sigma|_{\text{Eq}}$ 는 axioms 자동 만족 (restriction). Inclusion is confluent. Universal: standard.

**Note**: *kernels* in the abelian sense 는 $\mathbf{Tier2}$ 에 정의되지 않음 (no zero object). Equalizers 가 가장 가까운 대응.

#### 6.2.4 Finite vs infinite Ω

**Observation 6.5**. 위 propositions (products, coproducts, equalizers) 는 *finite or infinite* $\Omega$ 모두에서 성립. 단 *infinite product* (∞-ary) 에서는 σ_× 의 결정 가능성이 problematic — 본 디렉토리는 finite-arity 만 사용.

### 6.3 Forgetful functor — Markov → Tier2

**Markov category recap** ([[01_framework_master#4.10 범주론|01 §4.10]]). $\mathbf{Markov}$ = monoidal category with:
- Objects: Polish-Borel spaces $(\mathcal{S}, \mathcal{B})$
- Morphisms: stochastic kernels $\mathcal{K} : \mathcal{S}_1 \to \mathcal{S}_2$
- Composition: kernel composition (§2.3 of 01)
- Tensor: product spaces with product kernels

**Definition 6.6 (Forgetful functor $U : \mathbf{Markov} \to \mathbf{Tier2}$)**.

- *On objects*: $U(\mathcal{S}, \mathcal{B}) := (\mathcal{S}, \sigma_\mathcal{B})$ with $\sigma_\mathcal{B}$ = some *canonical σ* on $\mathcal{S}$. 일반적으로 *정확한 정의가 어려움* — Polish space 위 *canonical tolerance* 가 unique 하지 않음.
- *On morphisms*: $U(\mathcal{K}) := \bar{\mathcal{K}}$, the σ-pushforward of §3.2.

**What $U$ forgets**:
- *Distribution data*: $\mathcal{K}(x, \cdot)$ 의 확률 분포 → forgotten. Only kept: *which $y$ are σ-related to which $x$* (binary).
- *Measure-zero distinctions*: P-a.e. 동일한 kernel 들이 $\bar{\mathcal{K}}$ 에서 동일 — coarsening.
- *Quantitative integration*: $\int f d\mathcal{K}$ structure → forgotten.

**Functoriality**: $U(\mathcal{K}_2 \circ \mathcal{K}_1) = U(\mathcal{K}_2) \circ U(\mathcal{K}_1)$? — 정확한 *canonical σ* 정의가 필요. TC-SP-5.1 의 *조건부* (stage 마다 σ choice 가 compatible) 가 functoriality 의 *minimum condition*.

본 디렉토리는 $U$ 의 *정확한* 형식을 *open* 으로 둠 (meta-OP).

### 6.4 Adjunction — Free Markov from Tier 2?

**Question**: $U$ 가 *right adjoint* 인가? 즉, *left adjoint* $F : \mathbf{Tier2} \to \mathbf{Markov}$ — "free Markov category 생성" — 존재하는가?

**Argument against (general)**:
- $F(\Omega, \sigma) =$ "what Markov structure 가 $(\Omega, \sigma)$ 로부터 *자유롭게* 생성되는가?"
- Markov 의 데이터: 확률 분포 + sigma-algebra. Tolerance space 는 이 둘 다 *제공하지 않음* — σ-algebra 는 *generated by σ-balls* 가능하나 *유일하지 않음*; 분포는 *전혀 없음*.
- *Uniform prior on σ-balls* 같은 *canonical choice* 가 가능하지만 *not functorial* (σ-confluent map 이 uniform 을 보존하지 않음).
- 따라서 일반적으로 *left adjoint 없음*.

**Argument for (special)**:
- Finite $\Omega$ 의 경우, *counting measure* 가 *canonical*. Left adjoint candidate: $F(\Omega, \sigma) = (\Omega, 2^\Omega, \text{uniform})$ with $F(f) = $ deterministic kernel (Dirac).
- 그러나 이는 *Markov structure 의 trivialization* — 비-deterministic kernel 을 *생성하지 않음*.
- 따라서 "free" 의 의미가 *불충분* — *no interesting adjunction*.

**Conclusion**: 일반적으로 *left adjoint 없음*. 본 디렉토리의 *Markov → Tier 2 forgetful* 은 *one-way reduction* — *upgrade* 없음. 이게 Tier 2 의 *prior* 위상 (덜한 구조가 더 근본) 과 정합.

### 6.5 Small example — |Ω| = 3 chain

**Setup**: $\Omega = \{a, b, c\}$, σ = chain: $\sigma(a, b) \wedge \sigma(b, c)$ (+ reflexivity, symmetry), 但 $\neg \sigma(a, c)$. Non-trivial Tier 2 (Sorites-toy).

**All σ-confluent endomorphisms $f : \Omega \to \Omega$**:

Total set functions $\Omega \to \Omega$: $3^3 = 27$. σ-confluent 조건 검사:

Constraint: $\sigma(x, y) \Rightarrow \sigma(f(x), f(y))$.
- $\sigma(a, b) \Rightarrow \sigma(f(a), f(b))$: $\{f(a), f(b)\}$ must be σ-related.
- $\sigma(b, c) \Rightarrow \sigma(f(b), f(c))$: $\{f(b), f(c)\}$ must be σ-related.
- $\sigma(x, x)$ 자동.

σ-related pairs in $\Omega$: $\{(a,a), (b,b), (c,c), (a,b), (b,a), (b,c), (c,b)\}$. NOT σ-related: $(a, c), (c, a)$.

**Case analysis**:
- *$f(a) = a$*:
  - $f(b) \in \{a, b\}$ (since σ(a, f(b)) required, only a or b qualify with a; c excluded).
    - $f(b) = a$: $\sigma(a, f(c))$ required. $f(c) \in \{a, b\}$.
      - $f(c) = a$: constant $a$. ✓
      - $f(c) = b$: $f = (a, a, b)$. ✓
    - $f(b) = b$: $\sigma(b, f(c))$ required. $f(c) \in \{a, b, c\}$ all qualify (b is σ-related to all).
      - $f(c) = a$: $f = (a, b, a)$. ✓
      - $f(c) = b$: $f = (a, b, b)$. ✓
      - $f(c) = c$: identity. ✓
- *$f(a) = b$*:
  - $f(b) \in \{a, b, c\}$ (σ(b, f(b)) required, b is σ-related to all).
    - $f(b) = a$: $\sigma(a, f(c))$ required. $f(c) \in \{a, b\}$.
      - $(b, a, a)$, $(b, a, b)$. ✓ ✓
    - $f(b) = b$: $\sigma(b, f(c))$. $f(c) \in \{a, b, c\}$.
      - $(b, b, a)$, $(b, b, b)$, $(b, b, c)$. ✓ ✓ ✓
    - $f(b) = c$: $\sigma(c, f(c))$. $f(c) \in \{b, c\}$.
      - $(b, c, b)$, $(b, c, c)$. ✓ ✓
- *$f(a) = c$*:
  - $f(b) \in \{b, c\}$ (σ(c, f(b)), c is σ-related to b, c only).
    - $f(b) = b$: $\sigma(b, f(c))$. $f(c) \in \{a, b, c\}$.
      - $(c, b, a)$, $(c, b, b)$, $(c, b, c)$. ✓ ✓ ✓
    - $f(b) = c$: $\sigma(c, f(c))$. $f(c) \in \{b, c\}$.
      - $(c, c, b)$, $(c, c, c)$. ✓ ✓

**Total σ-confluent endomorphisms** (listed as triples $(f(a), f(b), f(c))$):

$(a, a, a), (a, a, b), (a, b, a), (a, b, b), (a, b, c),$
$(b, a, a), (b, a, b), (b, b, a), (b, b, b), (b, b, c), (b, c, b), (b, c, c),$
$(c, b, a), (c, b, b), (c, b, c), (c, c, b), (c, c, c).$

**Count**: 5 + 7 + 5 = **17** σ-confluent endomorphisms out of 27 total. 약 63%.

**Among these**:
- *Isomorphisms* (bijective): $(a, b, c)$ (identity), $(c, b, a)$ (reflection). → only 2.
- *Constants*: $(a, a, a), (b, b, b), (c, c, c)$. → 3.
- *Idempotents* ($f \circ f = f$): identity + constants + a few collapse maps.

**Observation**: The endomorphism monoid is *non-commutative* (e.g., $(a, a, b) \circ (b, b, c) = ?$ vs reverse). 이 monoid 의 구조 분석이 Tier 2 객체의 *internal symmetry* 를 reveals.

이 예가 본 디렉토리의 stage-별 σ 의 *combinatorial richness* 의 toy version — sensing pipeline 의 morphism 도 동일 종류 analysis 가 가능 (much larger).

### 6.6 SSKP 의 Tier2-lift (재진술)

SSKP 가 **Tier2** (또는 $\mathbf{Tier2}_{\text{val}}$) 의 5 객체의 sequence + 사이의 morphisms $\bar{\mathcal{K}}_i$:

$$
(\Omega_0, \sigma_0) \xrightarrow{\bar{\mathcal{K}}_1} (\Omega_1, \sigma_1) \xrightarrow{\bar{\mathcal{K}}_2} (\Omega_2, \sigma_2) \xrightarrow{\bar{\mathcal{K}}_3} (\Omega_3, \sigma_3) \xrightarrow{\bar{\mathcal{K}}_4} (\Omega_4, \sigma_4)
$$

각 $\bar{\mathcal{K}}_i$ 는 $\mathcal{K}_i$ 의 *Tier 2 측 reduction* — σ 보존 (또는 확장).

TC-SP-5.1 의 functoriality 가 *$F = U|_{\text{SSKP}}$ 가 well-defined functor* 라는 statement.

### 6.7 Markov category 와의 정합

[[01_framework_master#4.10 범주론|01 §4.10]] 에서 언급한 Markov category (Fritz 2020) — stochastic kernel 들의 monoidal category. 본 디렉토리의 SSKP 가 Markov category 의 한 object cascade.

Tier2 와 Markov category 사이의 *forgetful functor* (§6.3) 가 존재 — Markov 의 *분포 정보* 를 lose 하고 Tier 2 의 *graph 구조* 만 carry. *Left adjoint 없음* (§6.4) — *one-way reduction*.

본 디렉토리는 이 forgetful 의 정확한 형식을 *open* 으로 둠.

---

## 7. Stage 별 *Tier 2 순도* (purity)

각 stage 의 (Ω_i, σ_i) 가 *얼마나 순수한 Tier 2 인가*?

| Stage | 순도 | 이유 |
|------|------|------|
| 0 | **순수 Tier 2** | 토큰 (광자) + σ (시공간 인접). 값 없음. |
| 1 | Tier 2 + value | 각 발생점에 *graded 값* (V) 부속. σ 본질은 Tier 2. |
| 2 | Tier 2 + value + cross-channel | 채널 색인 + 대립 cross-link. σ 가 *이중 구조* (within + cross). |
| 3 | **순수 Tier 2** | 스파이크 (단순 사건) + σ. 값 없음. |
| 4 | 순수 Tier 2 | Stage 3 + latency. |

**순수 Tier 2** 가 *입력 / 출력 양 끝점*. 내부 stage 들은 *기술적 enrichment* 가 있으나 본질은 Tier 2.

이 패턴 (purity at boundaries, enrichment in interior) 이 *우연인지 필연인지* — 본 절에서 두 *논증* (information-theoretic + bio-engineering):

### 7.1 Information-theoretic argument — Bottleneck = purity

**Claim**: 경계 stage (0, 3) 의 *순수성* 은 *bottleneck 조건* 의 자연 결과.

**Argument**:
- [[06_endtoend_information_bound#TC-SP-4.1|TC-SP-4.1]]: end-to-end bound 가 *minimum stage capacity* 에 의해 결정.
- Bottleneck stage 는 *minimum representation* 을 가짐 — 가장 *compressed* 형식.
- Compression 의 한계: *atomic events* (각 token 이 *single bit + timestamp* 이상의 데이터 carry 불가). 이게 *pure Tier 2* 의 정의.
- 따라서 *bottleneck stage = pure Tier 2 stage*.

**Per-stage 검증**:
- *Stage 0* (input bottleneck): photon — *atomic*. *Single quantum event*. 부속 데이터 없이 *발생* 자체가 데이터. ✓
- *Stage 3* (transmission bottleneck — optic nerve $\sim 5$ Mbits/sec): spike — *atomic*. *Single neural event*. 부속 진폭/파형 없이 *timing* 이 데이터. ✓
- *Stage 1, 2* (internal computation, not bottlenecked): graded values OK — bandwidth abundant. → enrichment 가능.

**결론**: *순수 Tier 2 at boundaries* 가 *bandwidth bottleneck 의 필연* — *우연 아님*.

### 7.2 Bio-engineering argument — Sensor/effector atomicity

**Claim**: 생체 시스템의 *sensor* (광자 검출) 와 *effector* (신경 신호 전송) 는 *물리적 atomicity* 에 의해 *pure Tier 2*.

**Argument**:
- *Sensor*: photon detection 은 양자 사건 — *all-or-none* (rhodopsin isomerization). *Graded amplitude 가 불가능* — *single photon* event.
- *Effector*: action potential 은 *all-or-none* — *threshold-crossing* 동역학. *Graded spike 가 불가능* — biological constraint (membrane biophysics).
- *Interior*: dendritic computation, graded potentials, neurotransmitter release — *analog* 가능. *Computation 의 자유*.

따라서 *sensor/effector* 의 *atomicity = biological inevitability*. *Interior* 의 *analog enrichment = biological flexibility*.

**결론**: *순수 Tier 2 at boundaries* 는 *biology 의 ATOMIC physical event* 의 자연. Interior 의 enrichment 는 *생체 정보처리의 자유로운 표상*.

### 7.3 종합

Information-theoretic + bio-engineering 두 논증 *수렴*:
- 경계 stage = *최소 표현 / 물리적 atomicity*
- 내부 stage = *자유로운 enrichment / 정보처리 표상*

**Pattern**: *pure Tier 2 at boundaries, enriched in interior*. 이게 *sensing pipeline 의 universal pattern* 후보. *Conjecture*: 다른 양상의 sensing (auditory, somatosensory) 도 같은 pattern.

이 conjecture 는 *meta-OP* (sensory modality-wide). [[08_open_problems_sp|08]] 의 통합 목록에서.

---

## 8. Theorem-Candidates summary

| 코드 | 명제 | 위치 |
|------|------|------|
| TC-SP-5.1 | σ propagation functorial (case-by-case 확인 + proof sketch) | §3.3 |
| TC-SP-5.2 | SSKP 가 Tier 2 내부에서 closed (per-stage 검증) | §4 |

---

## 9. Open Problems

| 코드 | 문제 | Severity |
|------|------|----------|
| OP-SP-006 | SCC $u_t$ ↔ which stage? (4 candidate 분석) | High |

추가 *meta-OP*:
- σ-pushforward 의 *정확한* 형식 (deterministic vs probabilistic)
- Markov category 와 Tier2 의 forgetful functor 의 정확한 형식
- *순수 Tier 2 boundaries* 의 필연성 (§7 의 패턴)
- *Left adjoint 부재* 의 형식 증명 (§6.4)
- Tier 2 의 *generalized* equivalence (반례 cover 의 universal property)

이들은 본 문서에서 *registered* 만; [[08_open_problems_sp|08]] 의 통합 목록에 추가.

---

## 10. 도구 사용 summary

| 도구 ([[01_framework_master#4. 수학적 도구 카탈로그|01 §4]]) | 사용 |
|------|------|
| 4.9 대수위상 | sheaf / σ-structure (§6) |
| 4.10 범주론 | Tier 2 카테고리, functor (§6); Markov category 의 forgetful (§6.3-6.4) |
| 4.1 점과정 | Ω_0, Ω_3 의 점과정 형식 (§2.1, 2.4) |
| (외부) | tolerance spaces (Poincaré 1905; Zeeman 1962) |
| (외부) | Markov category (Fritz 2020; Cho-Jacobs 2019) |

---

## 11. 본 문서가 *시도하지 않는 것*

- $u_t$ 의 *결정* (OP-SP-006 등록만; §5.5 의 분석은 *후보 평가*, *결정 아님*)
- σ 의 *probabilistic* 일반화 본격 (deterministic σ 만; §3.2.1 의 sketch 만)
- Tier 2 카테고리의 *complete* 정식 — Markov category 와의 다리만 preview
- (Ω, σ) 가 *어떻게 객체를 생성* 하는가의 dynamics — *형성* 이 본 디렉토리 밖
- PAI 의 $\Delta_{\text{interp}}$ 가 (Ω, σ) 위에서 어떻게 보이는가 (격리)
- *Adjunction* 의 일반적 분석 (§6.4 의 negative argument 만)

---

## 12. 한 줄 요약

> SSKP 의 5 stage 모두가 (Ω, σ) Tier 2 객체를 carry; kernel 들이 σ 를 functorially propagate (σ-confluent maps); 전체 파이프라인이 Tier 2 *내부에서 닫혀 있음*. **Stage 0 와 Stage 3 가 둘 다 순수 점과정** — 자극과 응답이 *같은 위상학적 형식*. SCC $u_t$ 의 정확한 위치는 *open* (OP-SP-006; 4 candidates 분석, 가장 강한 후보 = post-Stage 4 cortical).

---

## 13. 더 높은 Tier 의 확장 — Tier-2 contract 의 규율

본 절은 *meta* 논의: 만약 *Tier 3* (pseudo-metric) 또는 *Tier 4* (vector) 을 어떤 stage 에서 *수용* 한다면 무엇이 일어나는가? 언제 *필요* 하고 언제 *sneaky* 한가?

### 13.1 Tier-2 contract — 정식 진술

**The Tier-2 contract**:

> *모든 stage 의 σ_i 정의는 (Ω0, σ1, σ2, σ3) axioms 만 사용한다. Tier 3/4 구조는 도구 (implementation) 로 자유롭게 사용되나, *정의 본체* (σ_i 의 predicate) 에는 들어가지 않는다. 만약 Tier 3/4 구조가 정의 본체에 들어가야 한다면, 그 stage 는 *명시적으로 Tier-2 contract 를 위반*하며 위반의 *이유* 가 문서화되어야 한다.*

이 contract 는 *positive* 규율 — *Tier 2 의 minimality 를 유지* 하기 위해.

### 13.2 Tier 3 (pseudo-metric) 의 도입 — 언제 필요한가

**Tier 3 = $(\Omega, d)$ with $d : \Omega^2 \to \mathbb{R}^+$, $d(x,x)=0$, $d(x,y)=d(y,x)$, triangle inequality**.

**필요할 가능성**:

1. *Geodesic 관계*: 두 점 사이의 *최단 경로* 가 *수치 거리* 를 요구.
   - Sensing pipeline 에서: ganglion cell array 위의 *spike propagation distance* 가 *수치* — Tier 3.
   - 그러나 σ_3 는 이를 *binary threshold* 후 사용 — Tier 2 로 reduce.
2. *Gradient flow*: SCC 의 $u_t$ dynamics 가 *gradient* 를 사용 — 본질적 Tier 4.
   - Sensing pipeline 의 σ 는 이를 *직접* 사용하지 않음.
3. *Optimal transport*: Wasserstein distance 가 *Tier 3* (metric).
   - [[01_framework_master#4.11 최적수송|01 §4.11]] 의 OT 가 *분석 도구* — implementation level. σ 정의에는 들어가지 않음.

**판정**: Tier 3 가 *분석에 필요* 하나 *σ 정의에 들어가는 것 금지* — Tier 2 contract 유지.

### 13.3 Tier 4 (vector) 의 도입 — 언제 sneaky 한가

**Tier 4 = $\Omega = $ vector space + metric/topology**.

**Sneaky 도입의 예** (피해야 할 것):

1. *"σ 가 inner product 의 threshold"* — $\sigma(x, y) :\iff \langle x, y \rangle > \theta$. 
   - **Sneaky**: $\langle, \rangle$ 가 Tier 4. *Threshold* 후 binary 이지만, *axiom-level data* 가 inner product 의 *구조* 를 요구.
   - **수정**: $\sigma$ 를 *primitive* 로 받고, $\langle, \rangle$ 를 *유도된 도구* 로만 사용.
2. *"σ 가 distance < ε"* — 이미 Tier 3 의 직설 사용. 
   - **덜 sneaky**: 거리 가 *binary* threshold 후 사라짐. *최소* 위반.
   - **수정**: ε 의 *물리적 motivation* 명시 (예: receptive field radius) — 그러면 Tier 3 도구가 *justified primitive*.
3. *"σ 가 cosine similarity > θ"* — vector inner product 의 정규화.
   - **Sneaky**: Tier 4 의 inner product structure 가 axiom-level.
   - **수정**: cosine similarity 의 *Tier 2 측 reduction* — *direction-based tolerance*.

**판정**: Tier 4 의 *implementation* 사용은 OK; *axiom-level* 사용은 *위반*.

### 13.4 본 파이프라인의 *명시적 Tier-2 contract 점검*

각 σ_i 정의에 대해 *axiom-level data* 검사:

- **σ_0**: $\|x_i - x_j\| < \delta_x \wedge |t_i - t_j| < \delta_t$.
  - *Tier-level data*: norm + abs + threshold. *Norm* 이 Tier 4 도구. 그러나 *threshold* 후 binary.
  - *Contract 상태*: *경계선*. Norm 의 *수치* 가 사라지면 OK; norm 자체의 *존재* 가 *공간 구조* 를 가정. 망막 표면 $\Sigma_{\text{ret}} \subset \mathbb{R}^2$ 가 *물리적으로 주어진* 공간 — *external given*, *Tier 2 의 axiom 외부*.
  - *판정*: contract 준수 (외부 given 으로 처리).
- **σ_1**: σ_0 form + $\tau = \tau'$. 동일 분석 + finite type set.
  - *판정*: 준수.
- **σ_2**: within-channel ball + cross-opposition (combinatorial set).
  - *Cross-opposition*: pure combinatorial. Tier 0-1 level. ✓
  - *판정*: 준수.
- **σ_3**: timing ball + $d_{\text{topo}}$ ball.
  - *$d_{\text{topo}}$*: Tier 3 도구로 정의되나, threshold 후 binary. **§2.4 의 미묘함**.
  - *판정*: 경계선 — Tier 3 도구가 σ 정의의 *근접* 에 있으나 *binary reduction* 이 finally Tier 2.
- **σ_4**: σ_3 form on shifted times.
  - *판정*: 준수.

**종합**: 본 파이프라인이 *Tier-2 contract 를 일관되게 준수*. *경계선* 인 경우 (σ_0, σ_3) 가 외부 공간 구조 / 채널 topology 의 *물리적 given* 에 의존 — *axiom-level Tier 4 자체* 는 아님.

### 13.5 만약 contract 를 위반한다면 — 수학적 결과

**위반 시 sneaky risk**:

- *Equivalence collapse*: Tier 3+ 의 *metric* 이 자연스럽게 equivalence class 를 induce (uniform partition) — Tier 2 의 *cover 구조* (Sorites 식) 를 잃음.
- *결정성 손실*: *왜* 이 stage 가 Tier 4 를 필요로 하는가의 *내재적 정당화* 부재 시, *임의 도입* 의 trace.
- *Empirical disconnection*: 생체 wiring 이 *combinatorial / topological* 인데 *수치 metric* 을 도입하면 *bio-implausible*.

**위반의 *합리적* 경우**:

- *지각 강도* (perceptual intensity): cognitive 수준에서 *graded confidence* 가 필요할 수 있음 — 본 sensing pipeline 의 *상위* (post-Stage 4) 에서.
- *Bayesian inference*: posterior 분포는 *Tier 4* 본질. *sensing 의 inference 측면* 이 Tier 2 위에 *얹힐 경우* contract 가 *명시적으로 변경*.

본 디렉토리는 위반 *없음*. 후속 작업 (PAI, cortical theory) 이 contract 변경 시 *명시적 변경 로그* 필요.

### 13.6 Tier-2 contract 의 *philosophical* 가치

**Argument**:
- *Minimality*: 가장 적은 구조로 *최대한 멀리* — Occam's razor 의 수학화.
- *Robustness*: 약한 구조는 *더 많은 instance* 를 cover — 다른 sensing modality 에 적용 가능.
- *Honesty*: *가정* 을 명시 — Tier 4 가정이 *숨어 있으면 보이지 않는 commitment*.
- *Prolegomena alignment*: §1.2 의 C1–C5 가 모두 *부정 조건* — Tier 2 의 minimality 와 정합.

**Counter-argument**:
- *Underspecification*: Tier 2 만으로 *dynamics 불완전* — formation 에 Tier 4 가 필요.
- *Practical*: *측정* 이 항상 수치적 — 순수 Tier 2 는 *implementation* 에 어색.

**본 디렉토리의 자세**: contract 를 *대상 구조* 에 적용; *도구* 에는 자유. *대상 / 도구 분리* 가 contract 의 본질.

---

## 14. 본 lift 의 *summary*

본 문서는 다음 작업을 완료:

1. (Ω, σ) Tier 2 의 *axiomatic* 정의 (§1.0) — Poincaré tolerance space.
2. Tier hierarchy 의 *forgetful collapse* 정리 (§1.1.2).
3. Prolegomena C1–C5 의 *per-condition* 검증 (§1.2).
4. 각 stage 의 (Ω_i, σ_i) *완전 정의 + axiom 검증 + σ-class analog* (§2).
5. σ-pushforward 의 *deterministic + stochastic* 정의 (§3.2, §3.2.1).
6. σ-confluent maps 가 *카테고리* 를 형성 (§3.2, §6.1).
7. Stage-별 σ pushforward vs natural σ *비교 + direction 식별* (§3.3).
8. TC-SP-5.1 의 *full proof sketch* (§3.3.5, §3.3 end).
9. Tier 2 closure 의 *rigorous 정의* (Def 4.1, 4.2) + per-stage 검증 (§4).
10. *Point ↔ field ↔ point* cycle 의 *category-theoretic* 표현 (§5.3.1).
11. *Bit-level compression accounting* (§5.4).
12. OP-SP-006 의 *4 candidate 심층 분석* (§5.5).
13. $\mathbf{Tier2}$ 의 products / coproducts / equalizers (§6.2).
14. Forgetful functor $U : \mathbf{Markov} \to \mathbf{Tier2}$ (§6.3).
15. *Left adjoint 부재* 논증 (§6.4).
16. Small example: |Ω|=3 chain endomorphism 17개 enumeration (§6.5).
17. Stage purity 의 *information-theoretic + bio-engineering* 이중 논증 (§7).
18. *Tier-2 contract* 의 정식 진술 + 본 파이프라인 점검 (§13).

총 18 항목 — 본 lift 가 *(Ω, σ) Tier 2 framework 의 sensing pipeline 위 완전한 lift* 의 candidate.

후속: [[08_open_problems_sp]] 의 OP 통합; PAI 와의 다리는 별도.

---

*Lift 07 v0 (확장본 2026-05-25). TC-SP-5.1, TC-SP-5.2 등록 + proof sketch. OP-SP-006 4-candidate 심층 분석. Tier-2 contract 정식 규율 (§13). 사용자의 (Ω, σ) Tier 2 commit 이 본 디렉토리 전체에서 *axiom-level 일관성* 으로 유지됨을 보증.*
