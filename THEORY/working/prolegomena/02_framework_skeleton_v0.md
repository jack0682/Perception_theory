---
type: working/prolegomena/framework-skeleton
version: v0
date: 2026-05-23
status: Stage 1.0 — 4-layer architecture scaffold (no formalization, no proofs)
purpose: |
  00 (perception-side 44 조건) 과 01 (math-side 44 조건 평행 번역) 위에
  *어떤 수학적 객체가 어느 layer 에 거주하는지* 명시한 framework skeleton.
  2026-05-22 광범위 리서치 (5 영역: 작용소대수 / 범주론 / 동역학 / 이산-관계론 / 정보-인지)
  의 수렴 결과를 4-layer hybrid 로 정착.
companions:
  - 00_field_conditions_v0.md (perception-side conditions catalog)
  - 01_mathematical_conditions_v0.md (math-side conditions catalog, parallel translation)
constraint_compliance:
  canonical_theorem_changes: 0
  claim_count: 102 (unchanged)
  CV_version: CV-1.20 (unchanged)
  scc_edits: 0
  new_OPs_registered: 0 (5 OP-NEW identified inside §6 only; not registered to theorem_status.md)
  formalization: 0
  proofs: 0
---

> [!nav] Parent: [[../INDEX|working/INDEX.md]] · Companions: [[00_field_conditions_v0.md]] · [[01_mathematical_conditions_v0.md]] · PAI: [[../../canonical/perception_action_interpretation_pivot_2026_05_21|PAI Pivot]] · [[../../canonical/PAI_ROADMAP|PAI Roadmap]]

# Framework Skeleton — 4-Layer Architecture v0

## §0 — 문서 위치

00 (perception-side) 와 01 (math-side) 의 *조건 catalog* 를 받아, *각 조건 클러스터가 어느 수학 layer 에 거주하는지* 명시한다. *조건 catalog* (00, 01) → *layer 분담* (본 문서) → *각 layer 의 형식화* (별도 문서, 미작성).

**Hard constraints**:
- canonical 무수정 (CV-1.20 그대로). 102 claims (71A / 20B / 6C / 5R) 그대로.
- scc/ Python 코드 무수정.
- 증명 0. 형식화 0. 새 vocabulary 0. 새 OP 등록 0.
- M_k 등급 변경 0. 00/01 의 표 무수정.

**Status**: Stage 1.0 — *architecture scaffold only*. 어느 layer 도 *internal formalization* 되지 않았다. 각 layer 의 후보 framework 들은 *기존 수학·물리 이론의 이름 표시* 일 뿐 *채택* 이 아니다.

---

## §1 — 4-layer architecture (overview)

| Layer | 역할 | Primitive | Derived | 후보 framework | 담당 M_k 클러스터 |
|---|---|---|---|---|---|
| **L0** | cohesion field dynamics | flow `μ_t ∈ Prob(X_t)` | trajectory, transport | McKean-Vlasov on Wasserstein, rough path | M3, M40, M44 (부분), SCC 자체의 격상 경로 |
| **L1** | derived carrier + correlation metric | algebra `A`, 측도 `ρ` 또는 spectral data | `X = spec(A)` 또는 `supp(ρ)`, metric `d ~ -log\|C\|`, 위상 | Connes NCG (spectral triple), Causal Fermion Systems (Finster), tensor network / AdS-MERA | M2, M5, M31, M33, M34, M41 (부분) |
| **L2** | algebraic state + autonomous dynamics + time | `ω: A → ℂ` (positive linear), `L\|_{h=0} ≠ 0`, modular flow `σ_t^ω` | KMS condition, linear response | BFV locally covariant AQFT + Tomita-Takesaki + Connes-Rovelli thermal time | M3, M10, M12-M17, M23-M24, M32, M38, M42 |
| **L3** | frame / observer / no global section | context category `O` (partial morphisms), bundle `π: E → O`, frame-indexed family `{ω_o}` | local sections, comparison morphisms | Doering-Isham Topos (spectral presheaf, Kochen-Specker), Rovelli RQM, Oreshkov-Costa-Brukner process matrices, QBism | M4, M6, M7, M9, M24, M37 |
| **L4** | self-reference scaffold | cartesian closed category 내부의 Lawvere fixed point theorem | (scaffold only) | Lawvere 1969, Yanofsky 2003 unification (Gödel/Tarski/Cantor) | M39 (formal status open) |

*Cluster coverage 자체 점검*: 00/01 의 10개 카테고리 (M1-M5 부정 / M6-M9 frame / M10-M14 world limit / M15-M18 autonomy / M19-M22 1차-2차 / M23-M26 algebraic / M27-M30 invariance / M31-M34 derived / M35-M39 accessibility / M40-M44 continuity) 중 **M27-M30 invariance 클러스터** 는 어느 단일 layer 에도 자연 거주하지 않는다 — §6 OP-NEW-C 로 분리.

---

## §2 — Layer 1: Derived carrier + correlation metric

**Primitive**: state functional 또는 operator algebra `A` (가환 또는 비가환), 측도 `ρ` (Causal Fermion 의 경우 유계 연산자 집합 위의 양의 Borel 측도).

**Derived**:
- carrier `X = spec(A)` (Gelfand spectrum) 또는 `X = supp(ρ)` (Finster CFS).
- metric `d(x,y) ~ -log\|C(x,y)\|` — Connes 공식 `d(x,y) = sup{|f(x)-f(y)| : ‖[D,f]‖ ≤ 1}` 의 일반화.
- 위상, 부피 형식 (Dixmier trace), K-이론 짝.

**후보 frameworks**:
- **Connes Noncommutative Geometry** — spectral triple `(A, H, D)`. M2, M31, M33, M34 의 정밀 구현.
- **Causal Fermion Systems (Finster 2025)** — 시공간 `M = supp(ρ)` 가 완전 derived. 인과 구조가 연산자 곱 `xy` 의 스펙트럼에서 정의. M31+M33 동시 만족의 가장 진보된 단일 후보.
- **Tensor network / AdS-MERA** — Ryu-Takayanagi `d ~ -log I(A:B)` 가 M31 의 가장 직접적 수식 구현. 단 배경 CFT 가정 (M33 부분).

**담당 M_k**: M2, M5, M31, M33, M34, M41 (부분).

**Gap**: M5 + M41 *동시* 의 axiom 수준 강제. 어느 후보도 *공리적 비분해성* 을 강제하지 않음. → §6 OP-NEW-E.

---

## §3 — Layer 2: Algebraic state + autonomous dynamics + time

**Primitive**: 상태 `ω: A → ℂ` (양의 정규화 선형 범함수), 자율 생성원 `L|_{h=0} ≠ 0`, 모듈 자기동형군 `σ_t^ω` (Tomita-Takesaki).

**Derived**:
- KMS 조건 `ω(ab) = ω(b σ_{iβ}(a))` → 시간 매개변수 `t` 가 *상태로부터 유도*.
- 선형 응답 `χ_{AB}(τ) = δω(A) / δh_B` (Kubo).
- 귀납적 극한 `W = lim→ A(O)` (world limit, M10).

**후보 frameworks**:
- **Brunetti-Fredenhagen-Verch locally covariant AQFT** — 함자 `A: Loc → Alg` 가 M7, M8 (정신), M10, M29, M36 의 가장 정밀한 범주적 구현. canonical/모범 예시.
- **Tomita-Takesaki modular theory + Connes 분류 (Type II_∞, III_λ)** — M3, M15-M17, M32, M42 의 동시 만족. 시간 유도의 *단일* 후보.
- **Connes-Rovelli thermal time hypothesis** — KMS 상태가 물리적 시간을 *선택*. M8 의 *부분* (시간 방향만; 공간은 미해결).

**담당 M_k**: M3, M10, M12-M17, M23-M24, M32, M38, M42.

**Gap**:
- M13 (multiplicative coupling) + M16 (non-trivial invariant measure) *동시* — 결정론적 rough path 만으로는 invariant measure 정의 불가. → §6 OP-NEW-D.
- M44 (interval / germ primitive) strict — KMS 조건이 *부분* 만족; *완전* 한 jet-level primitive 미해결.

---

## §4 — Layer 3: Frame / observer / no global section

**Primitive**: context category `O` (partial morphisms 만 허용), 번들 `π: E → O`, frame-indexed 상태 family `{ω_o}_{o ∈ O}`.

**Derived**:
- local sections `X^o = π^{-1}(o)`.
- frame 간 비교 사상 (있는 경우, 부분 동형).
- 부분 함자 `F: S → {Top, Prob, Cat}` (전역 임베딩 부재).

**후보 frameworks**:
- **Doering-Isham Topos** — von Neumann 대수 `A` 위의 context 범주 `V(A)` 와 spectral presheaf. Kochen-Specker 가 *전역 단면 부재 (M4)* 의 가장 강력한 수학적 실현. M4, M6, M7, M37, M39 동시 만족의 *유일* 후보.
- **Rovelli RQM** — 관측량이 *다른 물리 시스템* 에 상대적. M6, M7, M8 (부분), M24 의 자연 만족.
- **Oreshkov-Costa-Brukner process matrices** — 인과 구조 자체가 superposition. M9 의 native 만족. M4 강함.
- **QBism (Fuchs-Schack)** — agent-relative belief. M4 + M7 + M24 의 가장 직접적 실현 (단 dynamics 부재).

**담당 M_k**: M4, M6, M7, M9, M24, M37.

**Gap**: M8 *internal frame derivation* — context 범주가 이론 *외부* 에서 주어짐. Connes-Rovelli thermal time 이 시간 방향만 frame 으로 선택; *공간 방향* 의 상태-의존 파생은 미해결. → §6 OP-NEW-B.

---

## §5 — Layer 4: Self-reference scaffold

**Primitive**: cartesian closed category (CCC) 내부의 Lawvere 고정점 정리.

**Lawvere 1969**: CCC 에서 점-전사 사상 `φ: A → B^A` 가 존재하면 모든 자기사상 `f: B → B` 가 고정점을 가짐. *그 부정* — 고정점이 없는 `f` 가 존재하면 `φ` 가 점-전사일 수 없다 — 이 Gödel 불완전성, Cantor 대각, Tarski 정의불가능성을 통일 (Yanofsky 2003, arXiv:math/0305282).

**S 의 자기기술에 적용**: `S` 의 내부 언어가 자기 자신을 완전히 기술하는 점-전사 함자 `φ_S` 를 갖지 못한다는 조건이 M39 의 *형식 후보*.

**담당 M_k**: M39 (formal status open).

**Status**: **scaffold only** — 가장 약한 layer. IIT (intrinsicality axiom), autopoiesis (organizational closure) 는 *의미론적 선조* 일 뿐 formal encoding 미확립. *오늘 진입하지 않음*.

---

## §6 — Inter-layer adhesion: 5 미해결 수학 과제

본 문서에서 *명시만* 한다. *해결 시도 0*. *theorem_status.md 의 Open Problems Catalog 에 등록하지 않는다*. (등록 권유 카테고리: OP-FW; user 결정 보류.)

### OP-NEW-A — `σ_t`-공변 spectral triple 의 완전 특성화
**위치**: Layer 1 ↔ Layer 2.
**문제**: 일-매개변수 자기동형군 `σ_t` 를 갖는 C*-동력학계 `(A, σ_t)` 에서 spectral triple `(A, H, D)` 를 `σ_t`-공변하게 구성할 조건의 완전 특성화.
**기존 결과**: Bellissard-van Elst-Schulz-Baldes 1994 (J. Math. Phys. 35) — 준결정 경우. 일반 미해결.

### OP-NEW-B — M8 의 작용소대수적 내부 파생
**위치**: Layer 2 ↔ Layer 3.
**문제**: Connes-Rovelli thermal time 이 시간 방향만 선택. *공간 slicing* 의 상태-의존 파생 — 완전한 시공간 구조의 `ω`-의존 파생 — 미해결.
**기존 결과**: Connes-Rovelli (1994, Class. Quantum Grav. 11), Martinetti-Rovelli (2003, CQG 20). 이후 진전 없음.

### OP-NEW-C — M29 cross-fiber groupoid invariance 의 native model (PAI 핵심)
**위치**: Layer 3 ↔ Layer 4.
**문제**: 서로 다른 fiber (예: 시각 / 촉각) 사이의 부분 동형 하의 *불변량* 으로서의 객체 정체성. *PAI 의 진짜 독창적 요구* 이며, 5개 영역 어디에도 *기본 구조 수준* 에서 존재하지 않음.
**기존 후보 (모두 부분)**: cohesive ∞-topos (Schreiber) — categorical scaffold 만; BFV locally covariant — 함자 수준만; QBism — cross-fiber 자체 없음.
**전망**: *PAI 수학화의 first real entry point*. Phase 1 의 핵심 작업이 결국 여기로 환원될 가능성.

### OP-NEW-D — M13 + M16 동시 만족
**위치**: Layer 2 내부 (혹은 Layer 0 으로 격상).
**문제**: multiplicative coupling 형 `dS_t = L(S_t)dt + g(S_t)dh_t` 가 결정론적 `h` 에서는 invariant measure 정의 불가. Stochastic rough path 또는 McKean-Vlasov on Wasserstein 으로 가야 함.
**기존 후보**: Cardaliaguet-Delarue-Lasry-Lions (2019) lifted SDE on `Prob(R^d)`. 적용 검토 필요.

### OP-NEW-E — M5 + M41 의 코호몰로지 장애물
**위치**: Layer 1 내부.
**문제**: 비자명 Čech 1-코사이클 (M10 + M7 긴장에서 등장) 이 global tensor decomposition 을 *금지* 하는가? 이 연결이 확립되면 M5, M7, M10, M41 을 *통합* 코호몰로지 장애물 이론으로 처리 가능.
**기존 후보**: Abramsky-Brandenburger (arXiv:1102.0264) sheaf-theoretic contextuality + Abramsky et al. (arXiv:1111.3620) cohomology of non-locality.

---

## §7 — PAI thesis 정합 표

| PAI commitment (2026-05-21) | 4-layer 위치 |
|---|---|
| α (세계 하나, 인식 무한, 관측자 의존) | L3 frame indexing + L0 cohesion field |
| β (인식의 장 = 세계와 관측자의 접면; 접면은 관측자의 것) | L3 + L1 (carrier 가 ρ-의존 derived) |
| γ (장이 먼저 자기 질서; 세계는 나중 압력) | L2 autonomous generator `L|_{h=0} ≠ 0` |
| δ (객체화 1차, 출처 분류 2차) | L1 (substructure as G-invariant) + L3 (labeling functor `Λ`) |
| Interpretation invariance (PAI thesis 핵심) | **OP-NEW-C (L3 ↔ L4)** |
| Shared Unit Principle | L0 + L2 (readout observable `A ∈ A` 가 perception unit 과 action unit 모두) |
| Modal cross-invariance (Lorentz analogue) | OP-NEW-C 의 구체 instance |

**2026-05-21 commit (`inspection` action class)** → L2 의 readout observable `A ∈ A` 의 *first instance*. `A_inspection` 의 명시적 정의는 PAI roadmap Phase 2 의 대상.

**SCC substrate (102 claims) 위치**: L0 + L1 의 *현재 그래프 기반 구현*. L1 의 *비가환 격상* (Connes NCG / CFS) 은 substrate 의 *재해석* 이지 *대체* 가 아님 — 102 claims 보존.

---

## §8 — 본 문서가 *하지 않는* 것

- 어떤 layer 의 *내부 형식화*. 모든 layer 는 *후보 framework 의 이름표* 만.
- 새 vocabulary 도입. 기존 PAI 6 vocabulary 외 추가 없음.
- 새 정리/명제 제시. 증명 0.
- 새 OP 의 *공식 등록* (theorem_status.md). 5 OP-NEW 는 §6 *문서 내부 언급만*.
- canonical 수정. scc/ 수정. 102 claim 수정.
- M_k 등급/분포 변경. 00/01 무수정.
- PAI roadmap Phase 1 의 *해결*. 본 문서는 Phase 1 의 *기술 substrate* 일 뿐.
- 4-layer 의 *유일성* 주장. 다른 layer 분담도 가능; 본 안은 5/22 리서치 수렴의 한 정착.

---

## §9 — Next entry points

01 §10 의 4 진입점 (A_math / B_math / C_math / D_math) 을 layer 별로 *재배치*:

| 진입점 | 본 문서 layer | 비고 |
|---|---|---|
| A_math — controlled DE setting | L0 또는 L2 | rough path + autonomous generator |
| B_math — modal cross-invariance toy | L3 + OP-NEW-C | PAI 핵심 OP 의 minimal example |
| C_math — translation functor sketch | L3 | partial natural transformation between frame-restricted observables |
| D_math — SCC inheritance audit | 모든 layer 에 분산 | 102 claims 의 layer 별 위치 점검 |

*우선순위 명시하지 않음*. 다음 세션에서 user 결정.

---

## §10 — Changelog

- **v0 (2026-05-23)**: initial 4-layer skeleton. 2026-05-22 5-영역 광범위 리서치 (작용소대수 / 범주론 / 동역학 / 이산-관계론 / 정보-인지) 의 수렴 결과 정착. 5 OP-NEW 식별 (등록하지 않음, 본 문서 §6 내부 언급만). PAI roadmap Phase 1 의 기술 substrate 로 등록.

---

*Framework Skeleton v0 — 2026-05-23. 정리 0. 명제 0. 새 OP 등록 0. 4-layer architecture scaffold 만. canonical / scc / theorem_status 무수정. CV-1.20 그대로. 102 claims 그대로.*
