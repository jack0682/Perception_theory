# 05_orbital_essence.md — Orbital-as-Emergence: Reframing N-1

**Session:** 2026-04-24 (late afternoon)
**Origin:** 사용자 관찰 — "연속장에서 이산을 찾을 수 있음이 주요한 오비탈의 성질로 볼 수 있음. 확률분포적에서 이산적 구분으로 나뉠 수 있으니."
**This file covers:** 이 관찰을 σ-framework 와 N-1 의 lens 로 정형화. Conceptual addendum, not new theorems.
**Depends on reading:** 본 세션 `02_development.md` §2 (σ definition), `04_orbital_proofs.md` §3 (Lemma 3); `working/open_problems_reframing_2026-04-19.md` (N-1 framing).

---

## §1. The observation, formalized

> **Observation (User, 2026-04-24).** "Orbital" 의 정의적 본질은 atomic spectrum 의 구체적 형태가 아니라 **연속 장에서 이산 구조가 emerge** 하는 phenomenon 자체이다. Atomic 의 (n, ℓ, m) 은 한 instance 에 불과하다.

이 관찰을 SCC framework 안에서 명제로 정리:

> **Principle (Continuous-to-Discrete as Orbital Essence).** A theory $\mathcal{T}$ over a continuous primitive $\Psi$ exhibits *orbital character* if and only if there exists a derived map $\sigma_\mathcal{T} : \{\text{stable configurations of }\Psi\} \to \mathcal{D}$ where $\mathcal{D}$ is a discrete set, and $\sigma_\mathcal{T}$ classifies stable configurations up to equivalence relevant to the theory.

이 원리 하에서:
- Atom: $\Psi$ = wavefunction (continuous), $\sigma$ = $(n, \ell, m)$, $\mathcal{D} = \mathbb{Z}_{\geq 1} \times \mathbb{Z}_{\geq 0} \times \mathbb{Z}$.
- Phonon: $\Psi$ = lattice displacement field, $\sigma$ = Bloch wavevector $\mathbf{k}$, $\mathcal{D}$ = first Brillouin zone (discrete in finite lattice).
- Modica-Mortola: $\Psi$ = phase field, $\sigma$ = sharp-interface partition $\{A_k\}$, $\mathcal{D}$ = topological partition type.
- TDA: $\Psi$ = filtration function, $\sigma$ = persistence diagram, $\mathcal{D}$ = barcode poset.
- **SCC**: $\Psi$ = $u_t$ (cohesion field), $\sigma$ = cohesion signature $(\mathcal{F}; \{(n_k, [\rho_k], \lambda_k)\})$, $\mathcal{D}$ = $\mathbb{Z} \times (\mathbb{Z} \times \widehat{S} \times \mathbb{R}_{\geq 0})^K$.

→ orbital 성 은 SCC 만의 특이성이 아니라 **continuous-primitive 이론의 일반 phenomenon**. SCC 는 한 instance.

---

## §2. SCC 의 distinguishing characteristic — multi-source discreteness

위 instance 들 중 SCC 가 specific 한 점: **이산성의 source 가 셋 동시 작동**.

| Framework | Discrete source(s) | 개수 |
|---|---|---|
| Atom | bound-state Schrödinger spectrum (boundary condition) | **1** |
| Phonon | lattice periodicity (Bloch) | **1** |
| Modica-Mortola | Γ-limit (sharp interface) | **1** |
| TDA | filtration sweep (parameter discretization) | **1** |
| **SCC** | (a) topological + (b) spectral-combinatorial + (c) group-theoretic | **3** |

SCC 의 σ-framework 의 세 component 는 각각 다른 source 의 이산성:

### 2.1 Topological source — $\mathcal{F}(u^*)$

$\mathcal{F}(u^*) = |\{i : u^*(i) > u^*(j) \forall j \sim i\}|$ ∈ $\mathbb{Z}_{\geq 0}$.

- **연속 입력** $u^*$ 으로부터 **이산 출력** (정수)
- 메커니즘: 그래프 위의 strict-max 비교 (combinatorial)
- 외부 parameter 무관 (threshold, β 모두 무관 → CN17 의 핵심)
- TDA 의 0-th persistence 와 평행하나, $u^*$ 자체가 dynamical 산물 (TDA 처럼 외부 filter 가 아님)

### 2.2 Spectral-combinatorial source — $n_k$

$n_k = \mathcal{N}(\phi_k)$ = $k$-th Hessian eigenvector 의 nodal domain count.

- **연속 입력** $\phi_k$ (Hessian 의 eigenmode, $\mathbb{R}^X$ 위 함수) 로부터 **이산 출력**
- 메커니즘: sign + connected component (combinatorial on graph)
- Courant 부등식 $n_k \leq k+1$ — 정수 vs 정수 inequality
- atom 의 radial quantum number $n$ 과 평행하나 그래프-intrinsic

### 2.3 Group-theoretic source — $[\rho_k]$

$[\rho_k]$ = $V_k = \ker(H - \lambda_k I)$ 의 $S(u^*)$-irrep 분해의 dominant component.

- **연속 입력** $V_k$ (벡터공간) 로부터 **이산 출력** (irrep class $\in \widehat{S(u^*)}$)
- 메커니즘: 유한군 representation theory (Maschke + isotypic projector)
- $\widehat{S}$ 는 항상 **유한 집합** (S 가 finite group 이므로) — 이산성의 hard guarantee
- atom 의 angular quantum number $\ell, m$ 과 평행 (그러나 atom 은 무한군 SO(3) 의 irreps; SCC 는 유한 finite stabilizer)

### 2.4 세 source 의 독립성

세 source 는 동일한 $u^*$ 에서 추출되지만 **수학적 도구가 독립**:
- $\mathcal{F}$: combinatorial graph 분석 (Hessian 무관)
- $n_k$: spectral 분석 (group 무관)
- $[\rho_k]$: representation theory (nodal 구조 무관)

서로 무관한 세 도구가 같은 $u^*$ 에 적용되어 **서로 다른 이산 정보**를 추출. 각각 독립적으로 fail 가능 (e.g., trivial stabilizer 면 $[\rho_k]$ 가 vacuous; nodal sign 모호하면 $n_k$ 가 ill-defined). 그러나 셋 모두 fail 하는 case 는 codim ≥ 3 → **generic configuration 에서 σ 는 강건한 이산 라벨**.

---

## §3. N-1 의 reframing

`working/open_problems_reframing_2026-04-19.md` 의 N-1:

> **N-1 (Soft-Hard Switching Asymmetry).** 이론 ontology 는 continuous (graded $u$) 이지만 operations 는 discrete (integer K, threshold, axiom-carved category) 에 의존. 단일 root cause 가 F-1, M-1, MO-1 등의 표면 증상.

### 3.1 기존 frame: "bug to fix"

지금까지 N-1 은 다음으로 다뤄짐:
- "Soft 와 hard 를 어떻게 smooth 하게 연결할 것인가?"
- "Integer K 를 continuous 양으로 보내거나, $u$ 를 discrete 화할 mechanism 이 필요"
- 답을 못 찾으면 이론의 fundamental tension 으로 잔존

### 3.2 새 frame (사용자 관찰 기반): "feature to characterize"

위 §1 Principle 적용:
- 모든 continuous-primitive 이론이 orbital character 를 가지려면 reqiure 하는 것이 **continuous → discrete map** $\sigma$.
- "Soft 와 hard 의 smooth 연결" 은 잘못된 목표. **연결은 본질상 not smooth** — 그것이 emergence 자체.
- 답해야 할 질문이 바뀜: "이 emergence 의 mechanism 은 무엇인가?" (what generates discreteness from continuity?)

### 3.3 σ-framework 가 이 새 frame 의 답이다

σ 의 정의 자체가 emergence 의 mathematical embodiment:
- **입력**: continuous $u^* \in \Sigma_m$
- **출력**: discrete $\sigma \in \mathbb{Z} \times (\mathbb{Z} \times \widehat{S} \times \mathbb{R}_{\geq 0})^K$
- **연결**: 세 독립 메커니즘 ($\mathcal{F}$, $n_k$, $[\rho_k]$) 의 결합

따라서:

> **N-1 의 partial answer (sharpened, 2026-04-24):** 연속 $u$ 와 이산 분류 사이의 asymmetry 는 SCC 의 본질적 orbital character 의 표현이다. σ-signature 가 이 asymmetry 를 명시적으로 정형화: σ 는 연속 입력에서 이산 출력을 산출하는 well-defined 함수이며, 그 메커니즘은 (topological) ⊕ (spectral) ⊕ (group-theoretic) 의 세 독립 source 의 결합이다. "Smooth connection" 의 부재는 결함이 아니라 phenomenon 이다.

### 3.4 N-1 의 잔존 부분

위 reframing 후에도 여전히 open:
- **(NQ-A)** σ 가 parameter 변동 (β, c) 하에서 어떻게 jump 하는가? — orbital phase transition 의 정형화. (Cf. NQ-127.)
- **(NQ-B)** 두 다른 σ-class 사이의 transition path (saddle, NEB) 의 dynamics. — emergence 의 동역학적 측면.
- **(NQ-C)** σ 의 universality — 다른 graph (random, SBM 등) 에서 동일 σ-framework 가 작동하는가, 아니면 graph-class-specific?

이 셋이 N-1 의 "characterize" 측면의 후속 작업.

---

## §4. SCC vs other instances — what's specific

위 §1 의 5 instance 비교 표를 더 자세히:

| Instance | $\Psi$ (primitive) | $\sigma$ (discrete output) | Discrete sources | Self-referential? | Pre-objective? |
|---|---|---|---|---|---|
| Atom | wavefunction | $(n, \ell, m)$ | spectral (Schrödinger) | No (linear) | No (objects are atoms) |
| Phonon | displacement | $\mathbf{k}$ | lattice translation | No (linear) | No (lattice given) |
| Modica-Mortola | phase field | partition $\{A_k\}$ | Γ-limit | No (linear in limit) | partial (Allen-Cahn) |
| TDA | filtration $f$ | persistence diagram | filtration sweep | No (filtration external) | No (filter is given) |
| **SCC** | $u_t$ | $(\mathcal{F}; \{(n_k, [\rho_k], \lambda_k)\})$ | **3 source** | **Yes** (Cl, D dual-mode) | **Yes** |

SCC 가 가지는 **두 가지 distinguishing 특성**:

### 4.1 Multi-source discreteness (위 §2)

3 sources of discreteness 가 동시 작동 → σ 가 풍부한 이산 라벨. 다른 instance 들은 single source. 이것은 SCC 의 "orbital character 의 multi-channel 성".

### 4.2 Self-reference 가 emergence 자체에 진입

다른 instance 들은 모두 **linear** (Schrödinger, harmonic phonon, Allen-Cahn 의 leading order, filtration). Linear 한 시스템에서 spectrum 의 이산성은 boundary condition 의 결과.

SCC 는 nonlinear 그리고 **self-referential** (CN7 의 dual-mode). $\mathcal{E}_\text{cl}$ 가 $\text{Cl}(u)$ 에 의존, $\mathcal{E}_\text{sep}$ 가 $D(u)$ 에 의존 — 두 operator 모두 $u$ 자체로부터 정의됨.

따라서 SCC 의 σ 의 이산성은 **자기참조의 결과**:
- $\mathcal{F}$ 가 정수인 것은 $u$ 자신의 spatial 구조 자체가 결정 (외부 grid 가 아니라)
- $\lambda_k$ 의 spectrum 이 $H(u^*)$ 에서, $H$ 자체가 $u^*$ 에 의존
- $S(u^*)$ 가 $u^*$ 의 함수 → $\widehat{S}$ 도 $u^*$-dependent

→ **SCC 의 orbital 은 self-referential emergence**. Atom 의 orbital 은 fixed external structure (Coulomb potential, nucleus position) 위에서의 emergence. 이것이 "atom 과의 평행을 인정하면서도 reduction 을 거부" 의 가장 mathematical 한 표현 (CN10).

### 4.3 Pre-objective ontology

다른 instance 들은 모두 "이미 있는 객체 (atom, lattice site, phase domain, simplex)" 위에서 emergence. SCC 는 객체 자체가 emergence 의 결과 (응집의 stabilized configuration).

→ SCC 의 orbital 은 **pre-objective layer 의 orbital character**. 이 layer 자체가 다른 framework 에 부재.

---

## §5. σ-framework 의 위상학적 위치

위 분석을 종합:

> **σ-framework 의 정체**: continuous primitive $u_t$ 위에서 작동하는 self-referential pre-objective 이론에서, **orbital character 의 multi-source 이산 emergence 를 mathematical 으로 정형화하는 single object**.

이 정의 하에:
- σ 가 **단순 라벨** 이 아니라 **이론의 ontological 두 layer (continuous primitive, discrete derivative) 의 mathematical bridge**.
- σ 가 ontologically necessary — 이 두 layer 둘 다 존재한다는 SCC 의 commitment 가 σ 같은 객체를 강제.

### 5.1 Diagnostic vector $\mathbf{d}$ 와 σ 의 분업

| 객체 | 답하는 질문 | Layer |
|---|---|---|
| $\mathbf{d} \in [0,1]^4$ | "이것이 응집인가?" (proto-cohesion 의 질적 평가) | continuous → continuous |
| $\sigma$ | "이 응집의 정체는 무엇인가?" (formation 의 이산 분류) | continuous → discrete |

두 객체 모두 $u^*$ 에서 derived 이지만 **다른 ontological work** 를 수행:
- $\mathbf{d}$ 는 응집 자체의 척도 (proto-cohesion 의 4 qualitative axes)
- $\sigma$ 는 응집의 종류의 라벨 (formation identity 의 discrete encoding)

→ 두 객체는 **complementary**, 서로 대체 안 됨. canonical Item 11 ($\mathbf{d}$ primary) + S1' v1 (σ as formation identity) 가 양립.

---

## §6. 작은 정리 — the formal statement

위 분석을 명제로:

> **Proposition (Orbital Emergence in SCC, conceptual).** Let $\mathcal{T}_\text{SCC}$ denote the SCC theory with primitive $u_t : X_t \to [0,1]$ over finite graph $X_t$. Then $\mathcal{T}_\text{SCC}$ admits orbital character (in the sense of §1 Principle), and the corresponding emergence map $\sigma$ satisfies:
> (i) $\sigma$ is well-defined for Morse-0 local minimizers (Def 2.2 of `02_development.md`).
> (ii) $\sigma$ admits three independent sources of discreteness: topological ($\mathcal{F}$), spectral-combinatorial ($n_k$), group-theoretic ($[\rho_k]$).
> (iii) The discreteness of $\sigma$ is not externally imposed but **internally generated** via the dual-mode self-referentiality $(\text{Cl}, D)$ of CN7, distinguishing SCC from linear instances (atom, phonon, Modica-Mortola, TDA).
> (iv) $\sigma$ provides the **partial answer to N-1**: the soft-hard switching asymmetry is the orbital emergence, not a defect.

**Status: Cat A conceptual** (not a new theorem; consolidation of σ-definition + Lemma 1, 2, 3).

---

## §7. Implications for plan

### 7.1 새 NQ

- **NQ-147**: σ 의 multi-source discreteness 의 "depth" 정량화 — 어느 source 가 어느 regime 에서 dominant 인가? (e.g., trivial-stabilizer 영역에서 $[\rho_k]$ 가 vacuous → $n_k$ 와 $\mathcal{F}$ 가 dominant)
- **NQ-148**: §3 의 "characterize the emergence" 후속으로, σ-jump (orbital phase transition) 의 정형화.
- **NQ-149**: §4.2 의 "self-referential emergence" 와 atomic "external-structure emergence" 의 mathematical 차이의 정량적 statement (e.g., σ 의 sensitivity to $\lambda_\text{cl}, \lambda_\text{sep}$ vs atomic insensitivity to nuclear potential normalization).
- **NQ-150**: 다른 graph 에서 σ-framework 의 universality (NQ-C 와 일관).

### 7.2 다음 세션 권고 보강

99_summary.md §6 의 권고: σ-numerical 검증 (NQ-128, 137, 141). **추가**: 본 §6 Proposition 의 (iii) 를 정량 check — atom 과 SCC 의 σ 의 parameter sensitivity 비교.

### 7.3 Canonical 방향 시사

S1' v1 (in `03_integration_and_new_open.md` §1.1) 의 상위 framing 으로 본 §1 Principle 추가 가능: "SCC is an instance of continuous-to-discrete orbital emergence; Axiom S1' encodes the SCC-specific instance of this emergence."

이것이 canonical §11 commitment 의 14번째 항목 후보:
> **Commitment 14 (proposal, 2026-04-24).** Orbital character — the emergence of discrete formation identity (cohesion signature σ) from the continuous cohesion field $u_t$ — is **constitutive** of SCC's ontology, not a derived secondary phenomenon. The asymmetry between continuous primitive and discrete derivative is the orbital emergence, not a defect to be resolved.

---

## §8. 닫는 한 문장

사용자의 한 문장 ("연속에서 이산 emerge 가 orbital 본질") 이 σ-framework 를 단순한 분류 도구에서 **SCC 의 ontological 두 layer 의 mathematical bridge** 로 격상시켰다. 이 reframing 으로 N-1 의 "asymmetry 를 해소하라" 가 "emergence 를 characterize 하라" 로 바뀌고, σ 의 multi-source discreteness 가 SCC 를 다른 continuous-primitive 이론들 (atom, phonon, M-M, TDA) 과 distinguish 시키는 self-referential pre-objective 한 instance 로 만든다.

**End of 05_orbital_essence.md.**
