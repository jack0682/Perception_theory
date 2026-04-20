# Canonical Sub — 주간 누적 Buffer

**Status:** accumulating (next weekly merge → `canonical.md`)
**Purpose:** canonical 에 반영될 가치가 있는 변경사항을 매일 append 누적. **주 1 회** user 리뷰 후 `canonical.md` 에 merge, 본 파일 reset.
**Last reset:** 2026-04-20 (initial creation)
**Last entry:** 2026-04-20

---

## 사용 규칙

1. **Append-only:** 매일 새 섹션을 상단에 insert (최신순). 수정·제거는 주간 merge 시 user 결정에만.
2. **날짜별 섹션:** `## YYYY-MM-DD` 헤더, 그 안에 타입 라벨 구분.
3. **타입 라벨:** 다음 5 종만 사용.
   - `### Added` — 새 정리·공리·정의·CN·OP (증명/검증 완료).
   - `### Modified` — 기존 canonical 줄의 statement 또는 조건 수정.
   - `### Retired` — 기존 정리/주장의 retraction.
   - `### Clarified` — canonical 에 암묵적이던 것의 명시화 (metadata level, 내용 무변화).
   - `### Pending` — 다음 주 이상 carry-forward (아직 merge 불가).
4. **working reference 필수:** 각 entry 는 `working/<topic>.md` 또는 `logs/daily/YYYY-MM-DD/...` 를 출처로 명시. 출처 없는 entry 는 merge 대상 아님.
5. **주간 merge 절차:**
   - user 가 본 파일 섹션별 검토.
   - Added → `canonical.md` 해당 섹션 insert + `theorem_status.md` 행 추가 + `CHANGELOG.md` 주간 entry.
   - Modified → `canonical.md` 해당 줄 수정.
   - Retired → `canonical.md` Retracted 섹션 이동.
   - Clarified → `canonical.md` inline annotation 또는 §14 CN 추가.
   - Pending → 본 파일에 잔존, 다음 주로 carry.
   - merge 완료 후 본 파일 reset (모든 날짜 섹션 제거, Merge History 한 줄 append, `Last reset` 갱신).
6. **증명 없는 statement 금지:** Added 는 반드시 working 단계에서 증명 완료된 것만. 미완 결과는 Pending 으로.

## Promotion pipeline (개정)

```
logs/daily/YYYY-MM-DD/<artifacts>.md      (날것, chronological)
    ↓ topic 별 정리
working/<topic>.md                         (주제별 개발, 검증 대상)
    ↓ daily (증명/검증 완료분만)
canonical/canonical_sub.md                 (주간 merge buffer, 본 파일)
    ↓ weekly (user 리뷰)
canonical/canonical.md                     (main, 주 1회 update)
canonical/theorem_status.md                (main 동기 update)
```

Canonical.md 가 단일 spec 역할은 유지. 본 파일은 **pre-merge staging area**.

---

## 2026-04-20

**Session type:** Stage 0 (Purpose Declaration) 의사결정 재료 생산 — 이론 작업 Non-goal.
**Origin:** `logs/daily/2026-04-20/` (plan.md + 01_exploration.md + 02_development.md + 03_integration_and_new_open.md + 99_summary.md).
**Canonical-relevant 산출물:** Clarified 1 항목 (9+1 정리 integer-K 의존), Pending 2 항목 (theorem_status ↔ canonical §13 inconsistency), Added 1 항목 (NQ-1~7 pending OP 승급).
**Canonical-irrelevant (meta, 본 파일 대상 아님):** Matrix-1/Matrix-2, 15 세션 스케치, Pareto frontier {B, B+C, E, C+E}, Decision Tree, Sensitivity CS-1~4, 권고 E — 전부 purpose decision 재료이며 canonical 의 theorem/axiom 수정이 아님.

---

### Clarified

#### C-2026-04-20-01. Integer-K Load-Bearing 정리 10 개 목록

**출처:** `working/integer_K_dependency_map.md` §2; 기원 `logs/daily/2026-04-20/01_exploration.md` §5.2–§5.3 (3rd audit).
**변경 유형:** Metadata (category 유지). canonical.md line 의 statement 변경 없음.
**주간 merge 시 적용 방식:** canonical.md §13 의 해당 10 개 정리 라인 옆 inline annotation `*(Integer-K precondition: working/integer_K_dependency_map.md §2)*` 추가 여부는 user decision.

##### (a) Category A Retire — 5 개

soft-K 재공식화 하에서 statement 자체가 의미 소실. statement 의 per-formation index `j ∈ {1,…,K}` · per-formation mass `Σ^K_M` · `(K-1)` coupling factor 가 integer K 를 본질적으로 요구.

| # | 정리 | canonical.md 위치 | Statement 요약 | Integer-K Load-Bearing 지점 | 운명 근거 |
|---|---|---|---|---|---|
| 1 | **T-Merge (a)** K-Formation Local Minimality | §13 line 979 | Well-separated K-formations 가 K-field energy 의 local minima on `Σ^K_M`. Hessian 은 `μ_1 μ_2 > λ_rep^2` 조건 하 positive definite. | `Σ^K_M` manifold · per-formation Hessian PD · `μ_1 μ_2` product. soft-K distribution 하에서 "K-formation" 이라는 discrete 대상 부재. | Retire — "K 개의 formation" 개념 해체 |
| 2 | **Topological Lock** Merge Impossible on `Σ^K_M` | §13 line 988 | Per-formation mass constrained manifold 위에서 merge endpoint `(u_merged, 0) ∉ Σ^K_M` because `0 ∉ Σ_{m_2}` for `m_2 > 0`. | `Σ_{m_2}` 정의 자체가 per-formation mass 분할 필요. soft-K 에서 per-formation mass 부재. | Retire — `Σ_{m_2}` 라는 객체 부재 |
| 3 | **Coupling Bound Lemma** K-Formation Hessian | §13 line 820 | (SR: `min_k μ_k > (K-1)λ_rep`) 하 K-formation joint Hessian 의 Weyl spectral gap bound. | `(K-1)` factor — 정수 K 에서 pairwise coupling 수. | Retire — `(K-1)` pair count 는 integer K 특유 |
| 4 | **Proposition 1.2** Fiber Dimension | §13 line 1026 | Stratified Morse Analysis 의 `Σ²_M` fiber 의 차원 계산. | `Σ²_M` (K=2 constrained manifold) 자체가 per-formation mass 분할의 대상. | Retire — stratified Morse 대상 해체 |
| 5 | **Theorem 3.1(a,b,d)** Landscape at Symmetric Point | §13 line 1031 | K=2 대칭점 `(m_1 = m_2 = M/2)` 주변의 energy landscape curvature 분석. | K=2 symmetric point 는 정수 K 에서만 의미. | Retire — symmetric point 개념 소멸 |

##### (b) Category A Re-prove (retain) — 1 개

statement 는 재작성되지만 증명 핵심이 soft-K 하에서도 거의 그대로 재활용 가능.

| # | 정리 | canonical.md 위치 | Statement 요약 | 재활용 가능한 증명 핵심 | 재작성 방향 |
|---|---|---|---|---|---|
| 6 | **T-Merge (b)** Energy Ordering (Isoperimetric) | §13 line 984 | K=1 이 K=2 보다 낮은 energy on connected graph. Isoperimetric consequence. | Γ-convergence + perimeter minimization. Soft-K 로 전환해도 "single-mode vs multi-mode" energy 비교가 perimeter argument 로 보존. | "Single-mode (집중된 distribution) 이 multi-mode (분산된 distribution) 보다 low energy" 로 rewrite |

##### (c) Category B Retire — 1 개

empirical fit 이나 대상 개념이 integer K 전제.

| # | Result | canonical.md 위치 | Statement 요약 | Integer-K Load-Bearing 지점 | 운명 근거 |
|---|---|---|---|---|---|
| 7 | **γ_eff ≈ 0.89** empirical K-merge barrier exponent | §13 line 992 (erratum 2026-04-07) | K-merge barrier 가 `β^{0.89}` 로 scaling. exp55 empirical fit. | "K-merge" 개념 자체가 integer K 에서 정의. soft-K distribution 의 "mode unification" 은 barrier 개념이 재정의 필요. | Retire — empirical 대상 재정의 후 재측정 |

##### (d) Category C Re-prove — 3 개

statement 의 per-formation index 를 soft-K distribution 의 mode 로 재해석. 결과 (persistence) 는 유지 가능하나 증명 재작성 필요.

| # | 정리 | canonical.md 위치 | Statement 요약 | 재해석 방향 | 재증명 필요 지점 |
|---|---|---|---|---|---|
| 8 | **T-Persist-K-Sep** Well-Separated | §13 line 1065 | `(u^1_t, …, u^K_t)` well-separated joint minimizer (H1-K, WS, SR) 의 transition-preserving persistence. | "K 개의 독립 formation" → "soft-K distribution 의 K 개의 well-separated mode". | per-formation T-Persist-1 의 mode-wise 일반화, `d_min(j,k) ≥ D_sep` 는 mode pair 거리로 재정의 |
| 9 | **T-Persist-K-Weak** Weakly-Interacting | §13 line 1110 | Joint Hessian spectral gap via Weyl bound under (SR). Post-hoc correction within basin radius. | `(K-1)λ_rep` factor 는 mode pair 수 × repulsion 으로 재해석. | Weyl bound 가 soft-K mode basis 에서도 성립하는지 재증명 |
| 10 | **T-Persist-K-Unified** Parametric | §13 line 1115 | `Λ_coupling = λ_rep · ω_{jk} / min(μ_j, μ_k)` 로 Sep/Weak/Strong regime 을 통일. 100% geometric-Λ agreement in exp46-47. | pair index `(j,k)` → mode pair index. `ω_{jk}` (soft overlap) 은 이미 distribution-friendly. | Λ 의 정의가 soft-K 하에서도 잘 작동함 확인; Corollary I/II 증명 재편성 |

##### (e) Survive — Single-Formation 정리 19~20 개

soft-K 재공식화 하에서 statement 무변화. 증명 재활용 가능. **canonical 에 명시 annotation 불필요** (변화 없음이 default).

- **Cat A (19~20 survive):** T-1, T-3, T-6a/b/Stability, T-7, T-8-Core/Full, T-11 (Γ-Convergence), T-14, T-20, C-Axioms, QM-1/2/3/4, Predicate-Energy Bridge, T-Bind-Proj (τ=1/2), Deep Core Dominance 2b, T-Persist-1(b)/(e), T-A2.
- **Cat B (3 survive):** T-Bind-Proj (single formation, τ=1/2).
- **Cat C (K=1 survive):** T-Bind-Full (general τ, single formation), T-Persist-1(a)/(d)/Full.

---

### Pending

canonical.md 보수 대상. 오늘 수정 없음; 주간 merge 에서 user 확정.

#### P-2026-04-20-01. T-Persist-K-Sep Category Inconsistency

**출처:** `working/integer_K_dependency_map.md` §6.1.

**증상:**
- `canonical.md` §13 line 1043 erratum (2026-04-07) 은 T-Persist-K-Sep 을 **Category C** 로 이동 ("regime conditions are non-removable structural hypotheses, making it conditional").
- `theorem_status.md` CV-1.2 (last_updated 2026-04-12) 은 **Category B** 로 기록 (line 47: "T-Persist-K-Sep | accepted | B | C-0500 | P-0500 | E-0076, E-0077 | Conditional: on well-separated regime + per-formation persist").
- `canonical.md` §13 line 1063 Cat C 섹션 헤더에 "(Erratum 2026-04-07: T-Persist-K-Sep moved to Category C...)" 명시.

**해결 후보:**
- (i) **Sync theorem_status.md → Cat C** (canonical.md §13 기준). 이것이 자연.
- (ii) Sync canonical.md → Cat B (theorem_status 기준, erratum 원복).

**권고:** (i). `canonical.md` §13 이 THE spec (CLAUDE.md 원칙).

**Affected files on merge:** `theorem_status.md` line 47 — Category B → C, Notes 업데이트.

#### P-2026-04-20-02. Cat C Count Header Mismatch

**출처:** `working/integer_K_dependency_map.md` §6.2.

**증상:**
- `canonical.md` §13 line 1061 header: "### Category C: Conditional (**5 theorems**)".
- 실제 Cat C 섹션 나열 (line 1061-1147 사이):
  1. T-Bind-Full (line 미확인, grep 필요)
  2. T-Persist-1(a)
  3. T-Persist-1(d)
  4. T-Persist-Full
  5. T-Persist-K-Sep (erratum-moved in)
  6. T-Persist-K-Weak
  7. T-Persist-K-Unified

  → 6 또는 7 개 (T-Persist-K-Sep 의 Cat C 편입 시점에 따라).

**해결안:** header 의 `(5 theorems)` 를 실제 count (P-2026-04-20-01 해결 후 6 or 7) 로 수정.

**Affected files on merge:** `canonical.md` line 1061 header 수정.

---

### Added — Pending OP 승급

본 주에는 `canonical/open_problems.md` 에 OP-xxxx 로 승급하지 않음. **승급 조건:** reformulation purpose pin 후 해당 purpose scope 내 NQ 만.

**출처:** `working/new_open_questions_2026-04-20.md` (topic-consolidated); 기원 `logs/daily/2026-04-20/03_integration_and_new_open.md` §9.

#### NQ-1. Soft-K 정의의 Uniqueness / Canonical Choice — HIGH (E 직속)

- **Question:** 4 개 soft-K 정의 후보가 induce 하는 이론이 동일한가?
  - (i) `K_pers(u) = Σᵢ φ(ℓᵢ)` — H₀ persistence bar length weighted sum
  - (ii) `K_Betti(u) = ∫₀¹ β₀({x: u(x) ≥ θ}) dθ`
  - (iii) `u: X_t → Δ^{K_max}` simplex-valued, `K_eff = exp(H(u))`
  - (iv) `u: X_t → P(ℝ≥0)` measure-valued, K = support size
- **Canonical 연결:** §3.3 (u codomain), §5.5 (transition diagnostics), §12 (K-field 폐기 예고).
- **승급 조건:** purpose = E 또는 C+E. E-S1 에서 1 개 commit, NQ-1 은 사후 비교.

#### NQ-2. CN7 (Dual-Mode) 의 원리적 근거 — MEDIUM (C 연결)

- **Question:** 왜 Cohesion mode 가 2 개 (Closure + Distinction) 이고 Co-belonging 이 energy 진입에서 demotion 되었는가? "operator mode 전수 분류" 가 canonical 에 부재.
- **Canonical 연결:** §3.6 (Co-belonging), §6 Group C, §14 CN7, CN20 초안 (B-S1).
- **승급 조건:** purpose = C 또는 B+C. C 의 F-group 공리에서 C_t 가 entropy 로 격상되면 3-mode 복원 가능 (P-C 재프레이밍).

#### NQ-3. Persistence Vineyard 의 T-Persist-K 대체 가능성 — HIGH (E 직속)

- **Question:** 단일 u 의 persistence diagram flow (vineyard, Cohen-Steiner-Edelsbrunner-Morozov 2006) 가 T-Persist-K-Sep/Weak/Unified 의 conclusion 을 얼마나 회수하는가?
- **Sub-questions:** (a) vineyard stability 이 per-formation identity 를 보존? (b) well-separated regime 의 independent persistence 가 vineyard 언어에서 어떤 형태? (c) strongly-interacting regime (`Λ > 1/(K-1)`) 이 vineyard bar merge 로 해석 가능?
- **Canonical 연결:** §12 Multi-formation 전면 재작성의 수학적 핵심.
- **승급 조건:** purpose = E 또는 C+E. E-S2 의 §12 재작성 골격 완성의 core.

#### NQ-4. Q_morph 의 Threshold-Free 화 가능성 — MEDIUM (A 연결)

- **Question:** 현 Q_morph 가 superlevel filtration 을 sweep 하지만 최종 diagnostic 에서 threshold 선택이 재등장 (Core/Interior 경계). 완전 threshold-free Q_morph 가 QM1-4 를 만족하는가?
- **Sub-questions:** (a) integral-over-θ 로 처리 시 QM1-4 중 어느 공리 위반? (b) Lipschitz 성 (sweep 은 bar length 에 Lipschitz 지만 Core/Interior 는 sharp cutoff)? (c) 기존 Cat A QM 증명 재활용 가능?
- **Canonical 연결:** §5 전체, §7.1 (Q_morph), 공리 QM1-QM4.
- **승급 조건:** purpose = A. E 선택 시 parked.

#### NQ-5. CN ↔ 공리 Layer 충돌 해결 규칙 부재 — LOW (meta)

- **Question:** CN 과 공리 간 충돌 시 resolution rule 이 canonical 에 명시되지 않음. 예: B+C 조합에서 CN18 (zero-T) 과 F4 (T > 0 primacy) 직접 충돌.
- **Sub-questions:** (a) precedence 규칙? (b) CN 은 statement-level 인가 meta-commentary 인가? 공리 system 내부인가 외부인가?
- **Canonical 연결:** §6 (공리 layer), §14 (CN 정의).
- **승급 조건:** purpose = B+C 조합 시 필수. 다른 purpose 에서 conservative wording 으로 회피 가능.

#### NQ-6. Candidate D Partial Variant 의 Well-Posedness — LOW (D 연결)

- **Question:** `u → N[u] → Cl(u)` 의 Banach contraction 이 `(a_cl / 4) · L_N < 1` 요구. `L_N` 분석 미수행.
- **Sub-questions:** (a) `L_N` (N 의 u-Lipschitz 민감도) upper bound? (b) partial variant (ii) cohesion-weighted adjacency 의 B1-B4 공리 자동 성립? (c) fixed-point existence/uniqueness?
- **Canonical 연결:** §3.5 (Soft Adjacency), §6 Group B (B1-B4), §9.1 (Local Relation Kernel).
- **승급 조건:** purpose = D. D 후순위일 때 long-term carry.

#### NQ-7. N-1 의 Axiom-Switching 얼굴 (P-G) 정확한 Scope — MEDIUM (A 연결)

- **Question:** `N-1 = P-A + P-D + P-G` 분해에서 P-G 가 정확히 무엇을 포함?
- **Sub-questions:** (a) A1' (`a_cl < 4` 조건부 연장성) 은 axiom switching 인가 parametric commitment 인가? (b) b_D = 0 강제 (D-Ax3 implicit 침해) 는 P-G? (c) E3 reclassification (공리 → 해답 제약 강등) 은 P-G? (d) 각 Group 의 Reclassification Note 전부 P-G, 일부만?
- **Canonical 연결:** §3 (formal universe), §6 (각 Group 의 Reclassification Note), §14 CN6/CN14.
- **승급 조건:** purpose = A. A 의 A-S1 audit table core deliverable. E 선택 시 parked.

---

### 본 entry 의 canonical 변경 규모 (주간 merge 예상)

주간 merge 시 `canonical.md` 실제 수정:

1. **§13 inline annotation** — 10 개 정리 라인 옆 `*(Integer-K precondition: working/integer_K_dependency_map.md §2)*` 추가 (10 줄, metadata). user 수락 시만.
2. **§13 line 1061 header** — `(5 theorems)` → `(6 or 7 theorems)` — P-2026-04-20-02 해결 후.
3. **theorem_status.md line 47** — T-Persist-K-Sep Category B → C — P-2026-04-20-01 해결 후.
4. **open_problems.md** — NQ-1~7 은 본 주 변경 없음 (pending).

총 변경 ≤ 12 줄 (inline annotation 10 + header 1 + theorem_status 1). 새 정리/공리/CN 추가 없음. canonical.md 의 major 구조 변경 없음.

**주간 merge 에서 user 가 결정할 4 가지:**
- Q1. Inline annotation 10 개 추가할지 여부.
- Q2. theorem_status.md sync 방향 (Cat C 로 ← canonical §13 기준 / Cat B 유지 ← canonical erratum 원복).
- Q3. Cat C count header 수정값 (6 or 7, T-Persist-K-Sep 편입 여부에 따라).
- Q4. NQ-1~7 중 어느 것이든 본 주 내에 OP-xxxx 로 승급할지 (권고: purpose pin 후까지 대기).

---

## Merge History

(empty — 본 파일은 2026-04-20 첫 생성, 아직 weekly merge 수행 없음.)
