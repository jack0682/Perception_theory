# New Open Questions from 2026-04-20 Stage 0 Session

**Status:** exploring
**Last touched:** 2026-04-20
**Origin:** `THEORY/logs/daily/2026-04-20/03_integration_and_new_open.md` §9 (NQ-1…NQ-7)
**Purpose:** 2026-04-20 session 에서 드러난 7 개 새 open question 을 topic 별 consolidate. 각 NQ 는 Purpose pin 이후 plan.md Target 후보 또는 reformulation Stage 1–3 의 subtask. **본 문서는 NQ 를 해결하지 않음 — 보존.**

**Relation to `canonical/open_problems.md`:** 본 NQ 들은 아직 canonical open problem 로 승급되지 않음. purpose pin 후 해당 purpose scope 내 NQ 만 canonical/open_problems.md 에 OP-xxxx 로 승급 고려.

---

## NQ-1. Soft-K 정의의 uniqueness / canonical choice

**Question:** `02_development.md` A-S2 에서 제시한 4 개 soft-K 정의 후보가 induce 하는 이론이 동일한가?

- (i) `K_pers(u) = Σᵢ φ(ℓᵢ)` — H₀ persistence bar length 의 weighted sum.
- (ii) `K_Betti(u) = ∫₀¹ β₀({x : u(x) ≥ θ}) dθ` — superlevel set 의 zeroth Betti number threshold 적분.
- (iii) `u : X_t → Δ^{K_max}` — simplex-valued u, `K_eff = exp(H(u))` (entropy 기반 effective number).
- (iv) `u : X_t → P(ℝ≥0)` — measure-valued u, `K = |support|`.

**Sub-questions:**
- (i) 와 (ii) 가 동일 `K_soft` 를 주는가? 각각이 superlevel filtration 의 다른 encoding.
- (iii) 의 `K_max` hyperparameter 는 이론 내부에서 고정 가능한가?
- (iv) 가 가장 일반적이나 computability / Lipschitz 가 문제.

**Purpose 연결:** candidate E 직속 subtask. E-S1 에서 1 개 commit, NQ-1 은 나머지 3 개의 사후 비교로 parked.
**Canonical refs:** `canonical.md` §3.3 (u codomain), §5.5 (transition diagnostics), §12 (K-field 폐기 예고).

---

## NQ-2. CN7 (Dual-Mode) 의 원리적 근거

**Question:** 왜 Cohesion 의 mode 가 2 개 (Closure + Distinction) 이고 Co-belonging 이 energy 진입에서 demotion 되었는가?

**Sub-questions:**
- "Operator mode 의 전수 분류" 가 canonical 에 부재. 무한 mode / 3 mode / 2 mode / 1 mode 중 왜 2 mode 인가 원리적 증명 부재.
- C_t 를 entropy 로 격상 시 (candidate C 의 F-group 공리 하) 3-mode 체계 복원 가능 (P-C 재프레이밍).
- CN7 은 "특정 구조" 를 긍정하나 "왜 이 특정 구조" 는 미결.

**Purpose 연결:** candidate C 의 F-group 작업 내에서 자연스럽게 만남. candidate B 의 CN20 (dual-mode commitment) 초안과 병합 가능.
**Canonical refs:** §3.6 (Co-belonging), §6 Group C, §14 CN7.

---

## NQ-3. Persistence Vineyard 의 T-Persist-K 대체 가능성

**Question:** `02_development.md` E-S2 에서 제안한 "단일 u 의 persistence diagram flow (vineyard) 로 T-Persist-K 삼총사 대체" 가 T-Persist-K-Sep / Weak / Unified 의 모든 conclusion 을 회수하는가, 일부만 회수하는가?

**Sub-questions:**
- Vineyard stability (Cohen-Steiner–Edelsbrunner–Morozov 2006) 이 제공하는 persistence bar 의 time-trajectory 가 per-formation identity 를 보존하는가? (instrumental to T-Persist-K-Sep 의 "per-formation persistence".)
- Well-separated regime 의 "independent per-formation persistence" 가 vineyard 언어에서 어떤 형태로 나타나는가?
- Strongly-interacting regime (T-Persist-K-Unified 의 `Λ > 1/(K-1)`) 이 vineyard 의 "bar merge" 사건 으로 해석 가능한가?

**Purpose 연결:** candidate E 직속 subtask. E-S2 의 §12 재작성 골격 완성의 핵심.
**Canonical refs:** §12 전체.

---

## NQ-4. Q_morph 의 Threshold-Free 화 가능성

**Question:** 현 Q_morph 가 superlevel filtration 을 sweep 하지만 **최종 diagnostic 에서 threshold 선택이 재등장** (Core/Interior 경계). 완전 threshold-free Q_morph 가 기존 공리 QM1–QM4 를 만족하는가?

**Sub-questions:**
- `θ_core, θ_in, θ_1, θ_2, θ_ext` 를 integral-over-θ 로 처리 시 QM1–4 중 어느 공리가 위반되는가?
- integral-over-θ diagnostic 이 Lipschitz 인가? (sweep 은 bar length 에 대해 Lipschitz 이지만 Core/Interior 경계는 u 값의 sharp cutoff.)
- threshold-free QM 이 기존 Cat A QM1/QM2/QM3/QM4 증명을 재활용 가능한가?

**Purpose 연결:** candidate A 의 A-S3 subtask. E 선택 시 parked.
**Canonical refs:** §5 전체, §7.1 (Q_morph).

---

## NQ-5. CN ↔ 공리 Layer 충돌 해결 규칙 부재

**Question:** Commitment Note (CN) 와 공리 (A1′–E4) 간 충돌 시 resolution rule 이 canonical 에 명시되지 않음. 예: B+C 조합에서 CN18 (zero-T) 과 F4 (T > 0 primacy) 직접 충돌.

**Sub-questions:**
- CN 이 공리와 충돌 시 어느 쪽이 precedence 를 갖는가? (현재는 "conservative wording" 수동 해결.)
- CN 은 statement level 인가 meta-commentary 인가? 공리 system 내부인가 외부인가?
- 이는 canonical 의 **구조적** 문제 — `reformulation_plan.md` 에 meta-rule 추가 후보.

**Purpose 연결:** B+C 조합 선택 시 필수. 다른 purpose 에선 lower priority.
**Canonical refs:** §6 (공리 layer), §14 (CN 정의).

---

## NQ-6. Candidate D 의 Partial Variant 의 Well-Posedness

**Question:** D-S3 의 fixed-point obstruction 검토는 `u → N[u] → Cl(u)` 의 Banach contraction 이 `(a_cl / 4) · L_N < 1` 을 요구. `L_N` 의 분석이 미수행.

**Sub-questions:**
- `L_N` (N 이 u 에 얼마나 Lipschitz-민감한가) 의 upper bound 계산.
- D-S3 partial variant (ii) cohesion-weighted adjacency 의 B1–B4 공리 자동 성립 여부.
- fixed-point 존재 조건과 uniqueness.

**Purpose 연결:** candidate D prerequisite. D 선택 시 D-S1 의 핵심 수학 작업.
**Canonical refs:** §3.5 (Soft Adjacency), §6 Group B (B1–B4), §9.1 (Local Relation Kernel).

---

## NQ-7. N-1 의 Axiom-Switching 얼굴 (P-G) 의 정확한 Scope

**Question:** `open_problems_reframing_2026-04-19.md` §8 에서 `N-1 = P-A (integer-K) + P-D (threshold) + P-G (axiom-switching)` 로 분해. **P-G 가 정확히 무엇을 포함하는가?**

**Sub-questions:**
- A1′ (`a_cl < 4` 조건부 연장성) 은 axiom switching 인가 parametric commitment 인가?
- b_D = 0 강제 (D-Ax3 implicit 침해) 는 axiom/구현 괴리로서 P-G 에 속하는가?
- E3 reclassification (공리 → 해답 제약 강등) 은 P-G 인가?
- 각 Group 의 Reclassification Note / Layer-crossing note 가 전부 P-G 인가, 일부만인가?

**Purpose 연결:** candidate A 선택 시 A-S1 audit table 의 core deliverable. E 선택 시 parked.
**Canonical refs:** §3 (formal universe), §6 (각 Group 의 Reclassification Note), §14 CN6/CN14.

---

## 우선순위 및 purpose 매핑

| NQ | 자연 purpose | 우선순위 | E 선택 시 |
|---|---|---|---|
| NQ-1 | E | HIGH | E-S1 직후 |
| NQ-2 | C 또는 A | MEDIUM | parked |
| NQ-3 | E | HIGH | E-S2 core |
| NQ-4 | A | MEDIUM | parked |
| NQ-5 | B+C 조합 / meta | LOW | skip |
| NQ-6 | D | LOW | skip |
| NQ-7 | A | MEDIUM | parked |

**권고 (E 선택 경로):** NQ-1 과 NQ-3 이 E 의 Stage 1–2 에서 직접 다뤄짐. 나머지 5개 NQ 는 E 완료 후 재평가.
