# plan.md — 2026-04-25 Session Plan

**Session type:** W4 Weekly Close (MUST) + NQ-168 Goldstone Commensurability Mechanism + σ-Framework Numerical Verification.
**Prerequisite:** 2026-04-24 세션 완료 상태 — C2 ~100% (Theorem 2 Cat A, F-1 resolved), C3 ~100% sub-lattice + super-lattice Goldstone V5b, σ-framework definitional, ~29 Cat A, 2 in-session retractions, ~40 new NQ (NQ-125..171), weekly_draft_storming.md에 2026-04-24 entry 기록완료.
**Session working directory:** `THEORY/logs/daily/2026-04-25/`.
**Weekly buffer target:** `logs/weekly/2026-04-W4/weekly_draft_storming.md`에 end-of-session entry (이후 `weekly_summary.md` 작성).

---

## §1. 세션 목표

**"W4를 정직하게 닫고, 어제의 hot discovery (V5b commensurability splitting)를 수치로 고정하며, σ-framework의 정의적 Cat A를 최소 1건의 empirical 확인으로 뒷받침한다."**

어제 세션은 ~29 Cat A를 기록했으나 Tier 1 (canonically promotable)은 2건 (Theorem 2 family, F-1 resolution)뿐. 나머지 T2/T3는 추가 검증 없이 누적 중. 오늘은 **새로운 결과 추가보다 어제 결과의 검증 + 주간 정리**가 최우선.

---

## §2. Deliverables (P0/P1/P2)

### G0 — W4 Weekly Summary (P0 MUST)

**목표**: `THEORY/logs/weekly/2026-04-W4/weekly_summary.md` 작성. W4 (Apr 19–25) 전체 산출물의 정제된 요약 — canonical merge 권고안 포함.

**필수 섹션**:
1. **Entry → Exit 비교**: Entry state (78 NQ, 4 Cat A empirical) → Exit state 정량 비교
2. **Tier 분류 (필수)**: T1 / T2 / T3 / T4 엄밀 분류
   - T1 (canonically promotable): Theorem 2 family (Cat A, graph-class independent) + F-1 resolution
   - T2 (conditional/regime): Theorem 1 V5b + Lemma 1/2/3 + σ-definitional
   - T3 (sketch): G4 continuum limit, C3 super-lattice qualitative
   - T4 (retracted in-session): V4, V5a
3. **Canonical merge 권고안**: T1만 권고 — F-1 resolution → theorem_status.md 갱신, Theorem 2 → canonical.md §13
4. **W5 carry-forward**: G2 irrep / G3 nodal / NQ-168 / NQ-128/137/141 / canonical_drafts 파일들
5. **Self-assessment**: "C2/C3 100% conquered" claim의 과장 위험 명시, Tier 분류에서 honest

**Anti-pattern**: weekly_summary에서 T2를 T1으로 격상하는 "성과 정리 압박" 금지.

**Outputs**: `logs/weekly/2026-04-W4/weekly_summary.md` (~4-6 pages)

**Success criterion**: 이 파일을 읽은 사용자가 "어느 결과가 canonical merge 가능, 어느 결과가 추가 검증 필요" 즉각 파악 가능.

---

### G1 — NQ-168 Goldstone Commensurability Splitting Mechanism (P1)

**목표**: 어제 super-lattice (ζ > 0.5)에서 발견된 **2D Goldstone doublet commensurability splitting**의 수치 특성화.

**배경 (V5b 현재 상태)**:
- ζ = ξ₀/a < 0.3: sub-lattice, genuine orbital only, Cat A
- ζ > 0.5: super-lattice, translation Goldstone doublet + commensurability splitting
- L=40 β/β_crit=10.15: 99% Goldstone overlap 확인
- **오늘 target**: splitting Δλ = λ₁ - λ₀ 의 mechanism 확인

**오늘 수행할 구체 작업**:
1. L=40 ζ=1.0 torus disk를 N≥5 random seed에서 생성 → (λ₀, λ₁) 측정
2. Δλ vs center position (x_c mod 1) 정량화
3. Δλ vs L (L=20, 30, 40) scaling → 가설 D (finite-size artifact) 기각/지지 결정

**4가지 가설 (falsification 우선순위: D → A → B/C)**:
- 가설 D: L → ∞ 에서 Δλ → 0 (artifact) → torus periodic BC 로 빠른 확인
- 가설 A (FK-PN): Δλ ∝ center-lattice misalignment
- 가설 B (격자 고조파): Δλ ∝ ζ (선형)
- 가설 C (SCC closure): Δλ ∝ λ_cl → λ_cl=0 test

**스크립트**: `deep_dive_eigenvector_analysis.py` 수정 또는 신규 `nq168_commensurability.py`

**Outputs**: `02_NQ168_commensurability.md` + `CODE/scripts/results/nq168_*.json`

**Expected Cat 업그레이드**: 가설 D 기각 + mechanism 확인 → Theorem 1 V5b Cat A 조건 달성.

**Success criterion**: Δλ vs center position 정량 관계 (R² > 0.8) 또는 falsification 명시.

---

### G2 — σ-Framework Numerical Verification (P1)

**목표**: σ(u*) = (F; {(n_k, [ρ_k], λ_k)})의 정의적 Cat A를 최소 1건 empirical 확인.

**우선 순서: NQ-128 → NQ-137 → NQ-141**

**NQ-128** (λ₀/λ₁ ratio 분포, Theorem 1 직접 검증):
- R23 exp_orbital_fullscale.json의 56 stable minimizer 각각의 ζ = ξ₀/a 계산
- Sub-lattice (ζ<0.3): λ₀/λ₁ ≈ O(1) 예측 (genuine orbital)
- Super-lattice (ζ>0.5): λ₀/λ₁ << 1 예측 (near-zero Goldstone)
- 스크립트: `G1_analyze_R23.py` 재사용

**NQ-137** (nodal × irrep cross-check):
- 각 minimizer의 lowest 20 mode → (n_k, [ρ_k]) 계산
- D₄ irrep projection 8 symmetry operations

**NQ-141** (σ ↔ orbital taxonomy):
- R23 angular multipole (ℓ=0,1,2) vs σ-irrep label 비교
- Lemma 3 numerical verify: Mode 0 ↔ ℓ=1 Goldstone saturation

**Success criterion**: NQ-128 최소 1건 완료 + σ-framework "definitional + numerically grounded" 상태 달성.

---

### G3 — D₄ Irrep Classification 결정 (P2)

**목표**: 어제 plan.md G2 (원래 P0, 미실행)의 오늘 처리 방향 결정.

**세션 시작 30분 내 3-way 결정 (명시적 commit 필요)**:
- Option A: 오늘 실행 — `orbital_irrep_classify.py` 작성, 90-run × 20 modes
- Option B: W5 연기 — 사유: "G2 σ-numerical이 NQ-137로 대체"
- Option C: Drop — 사유: "σ-framework의 [ρ_k]가 D₄ irrep을 완전히 포괄"

**결정 기준**: σ-framework가 D₄ irrep 분류를 포괄하는가? 포괄하면 C (drop), 추가 정보를 제공하면 A 또는 B.

**Outputs**: 결정문 in `99_summary.md` §G3 + (실행 시) `working/orbital/M1_irrep_classification.md`

---

### G4 — working/canonical_drafts/ 실제 파일 작성 (P2)

**목표**: weekly_draft_storming.md Pending 항목의 실제 파일 생성.
- `working/canonical_drafts/axiom_S1_prime_v1.md`
- `working/canonical_drafts/CN15_static_dynamic.md`
- `working/canonical_drafts/CN16_protocol_parameterized.md`
- `working/canonical_drafts/CN17_sigma_labeled.md`

**Priority**: G0/G1/G2 완료 후 시간 허용 시. 이 파일들이 없으면 weekly_summary의 "merge 권고" 에 실체 없는 reference가 됨.

---

## §3. 우선순위 표

| 우선순위 | 작업 | Skip 시 결과 |
|---------|------|------------|
| **P0 (MUST)** | G0 weekly_summary.md | W4 미마감, W5 진입 무결성 훼손 |
| **P1** | G1 NQ-168 numerical | V5b hot discovery 검증 없이 식음 |
| **P1** | G2 σ-numerical (NQ-128 최소) | σ-framework "정의만 있고 검증 없음" 누적 |
| **P2** | G3 D₄ irrep 결정 | 어제 deferred debt 지속 |
| **P2** | G4 canonical_drafts 파일 | weekly merge 시 reference 없는 상태 |

---

## §4. Non-goals (명시적 제외)

- **Theorem 1 V5c 시도** — 6회 개정 history. 오늘은 V5b 검증만.
- **Canonical.md 직접 수정** — T1 결과도 weekly_summary → user 리뷰 → merge 파이프라인.
- **C1' cluster 새 attack** — 11 NQ 신규 공략 없음. W5 이후.
- **Multi-formation σ (Phase 5)** — 단일 formation σ 검증도 미완.
- **새 large 실험** — 어제 생성 스크립트 결과 분석만.
- **Theorem 2 (C5) 재오픈** — Cat B 확정, 오늘 out of scope.
- **G2/G3 미실행 사유를 추측으로 채우기** — 먼저 사유 명시, 추측 금지.

---

## §5. 작업 흐름

**Morning (09:00–12:00, 3h)**:
- 09:00–09:30: G3 결정 (D₄ irrep: A/B/C, 사유 commit)
- 09:30–12:00: G2 σ-numerical (NQ-128 먼저, 결과 대기 중 NQ-137 준비)
- 산출물: `01_sigma_numerical.md` + `CODE/scripts/results/nq128_*.json`

**Afternoon (13:00–16:30, 3.5h)**:
- 13:00–13:30: NQ-168 스크립트 작성 `nq168_commensurability.py`
- 13:30–15:00: 실행 (N=5 × L=20,30,40 = ~1h)
- 15:00–16:30: 결과 분석 + Theorem 1 V5b upgrade 판단
- 산출물: `02_NQ168_commensurability.md` + JSON results

**Evening (17:00–20:00, 3h RESERVED for G0)**:
- G0 weekly_summary.md 작성 (Apr 19-25 통합, Tier 분류 표 작성, canonical merge 권고안)
- G4 (시간 허용 시): canonical_drafts 파일 초안

**Late buffer (20:00–21:00)**:
- 세션 summary `99_summary.md` + weekly_draft_storming.md 에 2026-04-25 entry
- W5 디렉토리 준비: `logs/weekly/2026-04-W5/weekly_draft_storming.md` skeleton

**총 예상 세션 길이: 8–10시간**

---

## §6. R23 Carry-forward (어제 미완 항목 처리 매트릭스)

| 항목 | 어제 상태 | 오늘 처리 |
|------|---------|---------|
| G2 D₄ irrep (90-run) | P0 → 미실행 (사유 미기록) | G3에서 A/B/C 결정 |
| G3 nodal count | P0 → 미실행 | G3와 함께 결정 |
| G4 continuum limit | P1 → sketch | Cat C 유지, W5 이후 |
| Axiom S1' v1 파일 | 03_integration 내 draft만 | G4에서 canonical_drafts/ 파일 작성 |
| CN15/16/17 파일 | weekly_draft pending에만 | G4에서 파일 생성 |
| NQ-128 | 미실행 | G2 P1 |
| NQ-137 | 미실행 | G2 P1 |
| NQ-141 | 미실행 | G2 P1 |
| NQ-168 | 새 발견, 미검증 | G1 P1 |
| σ-framework 위치 감사 | 미수행 | G0 작성 전 확인 |

---

## §7. 성공 기준

**P0 (반드시 달성)**:
- [ ] `THEORY/logs/weekly/2026-04-W4/weekly_summary.md` 완성 + commit
- [ ] Tier 1/2/3/4 분류 표 포함 (T1 = 2건 정직하게)
- [ ] F-1 resolution (T1) 명시 + theorem_status.md 갱신 권고
- [ ] V5b (T2) vs Theorem 2 (T1) 구분 명시
- [ ] W5 carry-forward 항목 명시

**P1**:
- [ ] NQ-168: Δλ vs L scaling → 가설 D 기각/지지 결론
- [ ] NQ-128: 56 minimizer λ₀/λ₁ ratio 분포 + ζ crossover
- [ ] G3 결정: A/B/C 중 하나 + 사유 commit

**P2**:
- [ ] NQ-137 또는 NQ-141 결과 1건
- [ ] canonical_drafts/ 파일 1건 이상

**Hard constraints (무조건)**:
- [ ] Canonical.md 직접 수정 없음
- [ ] Silent resolution 없음
- [ ] V5b 이번 세션 canonical 승격 없음

---

## §8. 종료 기준

**정상 종료**: G0 완료 + G1 + G2 중 1건 이상 완료 + 세션 summary

**Minimal 종료**: G0 완료만 (G1/G2 → W5)

**Blocker 종료**: V5b 오늘 falsified → G0에서 정직하게 기록 후 종료

**금지된 종료 패턴**:
- G0 미완성 종료 (W4 close 의무 위반)
- V5b 검증 없이 Theorem 1 Cat A 승급 선언
- NQ-168 "mechanism 이해" = "V5b Cat A 완성" 혼동

---

## §9. Stage 가이드라인

**Analyst 지적 반영** (2026-04-25 사전 분석 기반):
- 29 Cat A 중 T1 확정은 2건. weekly_summary에서 정직한 Tier 분류 필수.
- In-session retraction (V4, V5a): V4 = 4-point 추외라 premature (process failure 측면), V5a = single-mode test 오해석 (partial process failure). **개선안**: T2 이상 claim 전 최소 sanity check 1건 필수화 (다른 seed 또는 그래프 클래스).
- G2/G3 미실행 사유: 어제 로그에 명시 없음 → 오늘 G3 결정 시 사유 문서화 필수.

**Silent resolution 금지**:
- F-1 (Cat A resolved) / M-1 (layer-clarified) / MO-1 (sidestepped) — 세 가지가 다른 상태임. weekly_summary에서 혼동 금지.
- NQ-168 mechanism 이해 != Theorem 1 Cat A 자동 승급.

**Promotion pipeline 준수**:
- weekly_summary.md → user 리뷰 → canonical.md merge (T1만)
- V5b는 working/에 최소 W5 종료까지 동결

---

**End of plan.md for 2026-04-25.**
**Target: Verify over discover. Honest W4 close. V5b numerically pinned or honestly retracted.**
