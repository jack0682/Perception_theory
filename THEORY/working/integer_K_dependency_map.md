# Integer-K Dependency Map

**Status:** developing
**Last touched:** 2026-04-20
**Canonical refs:** `canonical.md` §12 (K-field), §13 Cat A (T-Merge (a), Topological Lock, Coupling Bound Lemma, Prop 1.2, Thm 3.1), §13 Cat B (γ_eff ≈ 0.89), §13 Cat C (T-Persist-K-Sep/Weak/Unified)
**Origin:** `THEORY/logs/daily/2026-04-20/01_exploration.md` §5.2–§5.3 (3rd audit: A–E K-dissolution 대칭성)
**Purpose:** canonical 에 분산되어 있던 "integer K 의 load-bearing 지점" 을 단일 목록으로 consolidation. candidate E (soft-K) 또는 A (N-1 전체) 가 건드릴 정리의 **명시적 목록** 제공.

---

## 1. 왜 지금 명시화하는가

canonical v1.2 는 이미 "fixed K, fixed m" 외부 가정 하에 K-field 정리들을 증명 (`theorem_status.md` CV-1.2 notes). 그러나 **어떤 정리가 K 의 정수성 (integer structure) 자체에 의존** 하고 어떤 정리는 단순히 "K=1 에서 성립" 인지가 `canonical.md` inline 으로 분산되어 있어, 재공식화시 건드릴 범위의 정확한 지도가 없었다.

2026-04-20 session 3rd audit (`logs/daily/2026-04-20/99_summary.md` Error-7) 에서 candidate A 의 K-soft 작업이 candidate E 와 동일 효과를 만듦이 발견되었고, 이 동치의 근거는 **같은 9개 정리 집합** 에 대한 공통 공격 이다. 본 문서는 그 9개를 목록화.

## 2. Integer-K Load-Bearing 정리 9개

### 2.1 Category A — Retire (5개)

statement 자체가 per-formation mass `Σ^K_M` · K-formation index · (K-1) coupling factor 를 사용하므로 soft-K 하에서 의미 소실.

| # | 정리 | canonical.md 위치 | integer-K 의존 지점 |
|---|---|---|---|
| 1 | **T-Merge (a)** — K-Formation Local Minimality | §13, line 979 | `Σ^K_M` manifold 위의 per-formation Hessian PD |
| 2 | **Topological Lock** — Merge Impossible on `Σ^K_M` | §13, line 988 | `0 ∉ Σ_{m_2}` 의 per-formation mass 정의 |
| 3 | **Coupling Bound Lemma** — K-Formation Hessian | §13, line 820 | Weyl bound 의 `(SR): min_k μ_k > (K-1)λ_rep` — `(K-1)` factor 는 integer K 특유 |
| 4 | **Proposition 1.2** — Fiber Dimension | §13, line 1026 | Stratified Morse 의 `Σ²_M` fiber 구조 |
| 5 | **Theorem 3.1(a,b,d)** — Landscape at Symmetric Point | §13, line 1031 | K=2 대칭점 (m_1 = m_2 = M/2) 의 landscape |

**주:** T-Merge (b) Energy Ordering (Isoperimetric, line 984) 는 Cat A 이나 증명 핵심이 Γ-convergence isoperimetric — soft-K 하에서 "single-mode vs multi-mode energy ordering" 로 statement 재작성 + 증명 재활용 가능. **Re-prove (retain)** 으로 분류, Retire 아님.

### 2.2 Category B — Retire (1개)

| # | Result | canonical.md 위치 | integer-K 의존 지점 |
|---|---|---|---|
| 6 | **γ_eff ≈ 0.89** (empirical K-merge barrier exponent) | §13, line 992 (erratum 2026-04-07) | "K=2 → K=1 merge" barrier 의 scaling — "merge" 개념이 soft-K distribution 의 mode unification 으로 대체되면 barrier exponent 는 재측정 대상 |

### 2.3 Category C — Re-prove (3개)

statement 의 per-formation index `j ∈ {1,…,K}` 를 soft-K distribution 의 mode 로 재해석 가능. 결과 (persistence) 는 유지 가능하나 증명 재작성 필요.

| # | 정리 | canonical.md 위치 | integer-K 의존 지점 |
|---|---|---|---|
| 7 | **T-Persist-K-Sep** (Well-Separated) | §13, line 1065 (erratum-moved to Cat C 2026-04-07) | per-formation T-Persist 를 K 번 independent 적용; `d_min(j,k) ≥ D_sep` |
| 8 | **T-Persist-K-Weak** (Weakly-Interacting) | §13, line 1110 | joint Hessian `(SR): min_k μ_k > (K-1)λ_rep` |
| 9 | **T-Persist-K-Unified** | §13, line 1115 | pair index `(j,k)` 의 $\Lambda_{coupling} = \lambda_{rep} \omega_{jk} / \min(μ_j, μ_k)$ |

### 2.4 총계

- **Retire 6** (Cat A 5 + Cat B 1) — soft-K 하에서 statement 의미 소실.
- **Re-prove 3** (Cat C) — statement 재작성 + 증명 재작성.
- **Re-prove (retain) 1** (T-Merge (b), Cat A) — 증명 핵심 유지.

이 **9 + 1 = 10 개** 가 candidate E (또는 A) 의 K-얼굴 작업의 정확한 대상.

## 3. Integer-K 에 load-bearing 이 **아닌** 정리들 (Soft-K 하 Survive)

아래 정리들은 K 개념을 사용하지 않거나 K=1 의 single formation 만 다룸. soft-K 재공식화에서 **survive**.

**Cat A (19개 survive):** T-1 (Existence), T-3 (Interior Stability), T-6a/b/Stability (Closure FP), T-7 (Enhanced Metastability), T-8-Core/Full (Phase Transition), T-11 (Γ-Convergence), T-14 (Gradient Flow), T-20 (Consistency), C-Axioms, QM-1/2/3/4, Predicate-Energy Bridge, T-Bind-Proj, Deep Core Dominance 2b, T-Persist-1(b)/(e), T-A2.

**Cat B (3개 survive):** T-Bind-Proj (single formation), T-Persist-K-Sep/Unified (theorem_status.md 기준, 하지만 canonical §13 는 Cat C 로 erratum-이동 — 6.1 inconsistency 참조).

**Cat C (2개 survive under K=1):** T-Bind-Full (general τ, single formation), T-Persist-1(a)/(d)/Full.

## 4. Candidate A 와 E 의 coverage 동치의 근거

Matrix-1 의 OP 5-level coding 에서 A 와 E 가 indistinguishable 함의 원인: 두 후보 모두 위 **9개 정리를 공통 공격**. A 는 추가로 threshold (Core/Interior 경계, §5) 와 axiom-switching (A1' `a_cl<4`, b_D=0, E3 reclassification) 을 별도 phase 에서 다루나, 이는 **위 9개 정리 목록 밖의 작업** 이며 Matrix-2 (정리 survival) 에 반영되지 않음.

결론: A ⊋ E 의 scope 포함은 sustained, 그러나 Matrix-2 coarse 코딩에서 drop out. 실질 구분 축은 세션 수 (A 18 vs E 12) 와 qualitative depth 뿐.

## 5. "Retire" vs "Re-prove" 구분 기준

- **Retire:** statement 자체가 soft-K 이후 의미를 잃음. Topological Lock 의 `0 ∉ Σ_{m_2}` 는 per-formation mass 가 integer K 를 전제하므로 soft-K 에서 `Σ_{m_2}` 라는 객체 자체가 부재.
- **Re-prove:** statement 의 내용이 soft-K 언어로 rewrite 가능. T-Persist-K-Sep 의 "per-formation persistence" 를 "per-mode persistence of soft-K distribution" 로 재작성, 결과 (persistence 유지) 는 동일.
- **Re-prove (retain):** 증명 핵심 (예: Γ-convergence) 이 statement 언어 재작성 후에도 거의 그대로 재활용 가능. T-Merge (b) 가 유일 예.

## 6. 기존 canonical 과의 inconsistency (incidental finding)

### 6.1 T-Persist-K-Sep 의 Category

- `canonical.md` §13 line 1043 erratum (2026-04-07): "T-Persist-K-Sep moved to Category C".
- `theorem_status.md` (last_updated 2026-04-12): Cat B.

두 파일이 불일치. 본 dependency map 은 **canonical.md §13 을 우선** (CLAUDE.md 의 "canonical.md 는 THE spec" 원칙). 이 inconsistency 자체가 별도 작업: `theorem_status.md` 를 §13 에 맞춰 sync 해야.

### 6.2 Cat C 개수

- `canonical.md` §13 line 1061 header: "Cat C: Conditional (5 theorems)".
- 그러나 line 1065+ 에 T-Persist-K-Sep, T-Persist-K-Weak, T-Persist-K-Unified + T-Persist-1(a)/(d)/Full + T-Bind-Full 가 나열 — 6~7개.

header 와 내용 불일치. 본 문서는 header 숫자 대신 내용 목록 기준.

## 7. Next Actions

- [ ] 본 문서 user 검토 (2026-04-21).
- [ ] 위 §2 의 "Retire 6 / Re-prove 3 / Re-prove (retain) 1" 분류가 정확한지 각 정리 증명을 reread 하여 검증. 특히 **T-Merge (b) Γ-conv 재증명 sketch** 를 soft-K 언어로 pre-draft.
- [ ] Soft-K 정의가 commit 된 후 (purpose = E 선택 + E-S1 완료) 본 목록이 완전한지 cross-check. §3–§7 의 K 를 간접 사용하는 predicate 가 누락되어 있는지 audit.
- [ ] §6 inconsistency (T-Persist-K-Sep category · Cat C count) 별도 보수 세션 — `theorem_status.md` 를 `canonical.md` §13 에 sync.
- [ ] (optional) `canonical.md` §13 의 위 9개 정리 옆에 inline marker `*(Integer-K precondition: working/integer_K_dependency_map.md)*` 추가 여부 user decision. 이는 category 변경 아님 (metadata).

## 8. 2026-04-20 session 과의 관계

본 문서는 `logs/daily/2026-04-20/01_exploration.md` §5.2–§5.3 의 3rd audit 발견을 topic 기반으로 consolidate. Matrix-2 cell 판정의 근거를 독립 reference 문서화 — 향후 재공식화 세션 이 Matrix-2 를 재생성하지 않고 본 문서만 참조하면 됨.

9 integer-K load-bearing 정리 + 1 re-provable 정리 목록은 reformulation Stage 2 (Axiom Audit) 의 **pre-deliverable**. Stage 2 본 작업은 각 정리의 수정 상세와 공리 수준 합의.
