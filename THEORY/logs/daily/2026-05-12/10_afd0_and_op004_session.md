---
type: log/session
date: 2026-05-12
session_label: W7-Day2-AFD0-OP004
canonical_version: CV-1.13 (unchanged, read-only)
files_created:
  - THEORY/working/AFD_0/op_afd_004_proof.md
files_modified:
  - THEORY/working/AFD_0/afd_theorem_registry.md (pending: AFD-T7 Cat B upgrade)
  - THEORY/logs/weekly/2026-05-W2/weekly_draft_storming.md (pending: Day 2)
---

# 10 — AFD-0 Session + OP-AFD-004 Proof (2026-05-12)

이 파일은 2026-05-12 W7 Day 2 세션을 기록한다.
canonical/theorem_status/changelog 등은 수정하지 않았다 (working 단계).

---

## 세션 시작 상태

| 항목 | 값 |
|---|---|
| Canonical version | CV-1.13 (sealed 2026-05-10) |
| Claim count | 59A / 14B / 5C / 5R = 83 claims |
| AFD-0 package | `THEORY/working/AFD_0/` — 11파일 완성 (전날 세션) |
| 오늘 주요 목표 | OP-AFD-004 증명 시도 (positive merge barrier analytic lower bound) |

---

## 작업 1: exp38 재실행 — 최신 barrier 수치 획득

**파일:** `CODE/experiments/exp38_barrier_height.py`
**실행 결과 (2026-05-12):**

| β | Linear barrier | Refined barrier | c_low = 0.0221β |
|---|---------------|-----------------|-----------------|
| 20 | 86.5 | — | 0.44 |
| 30 | 193.9 | — | 0.66 |
| 50 | 279.6 | **23.5** | **1.1** |
| 100 | 680.5 | — | 2.2 |

- 선형 경로 log-log 기울기: **γ_linear = 1.216** (linear interpolation 경로는 비물리적 고에너지 구역 통과)
- Refined 경로 (10 gradient steps per α): β=50에서 23.5 (NEB의 37.2보다 낮음 — refinement 부족)
- 실제 MEP 장벽: NEB exp60 기준 ~37.2 (β=50)
- canonical이 인용하는 O(β^0.89)는 exp38/exp55 이전 실행 기반 — 오늘 linear 결과(γ=1.216)와 상이할 수 있음

**결론:** c_low = 0.0221β는 실제 장벽보다 ~21배 작은 보수적 하한. 유효하고 양수.

---

## 작업 2: OP-AFD-004 증명 — `op_afd_004_proof.md` 작성

**출력:** `THEORY/working/AFD_0/op_afd_004_proof.md`

### 핵심 판정: Cat B Resolved (qualitative positivity)

**Strategy A (정성적 양수성, H-MORSE 불필요):**

1. u*_K는 strict local minimizer (T8-Core Cat A + AFD-D1)
2. Basin B(F_K)는 non-trivial (T14 Cat A + AFD-D2)
3. u*_{K-1} ∉ B(F_K): u*_{K-1}은 다른 critical point이므로 자신으로 수렴 → B(F_K)에 속할 수 없음
4. 모든 admissible path γ ∈ Adm(F_K, F_{K-1})는 ∂B(F_K)를 횡단해야 함
5. ∂B(F_K) 횡단 시: E(γ(s₀)) ≥ E(u*_K) + Δ_min(F_K) > E(u*_K)
6. **따라서: Bar(F_K, F_{K-1}) ≥ Δ_min(F_K) > 0** □

**Strategy B (정량적 하한, T-Persist-1(b) 사용):**

- T-Persist-1(b) (Cat A, canonical line 1804): Δ_core ≥ 0.0441β
- K=2 joint basin depth: Δ_min(F_K2) ≥ 0.0441β/2 = 0.0221β (H1-H4, WS, SR 조건 하)
- **c_low(β) = 0.0221β > 0** (명시적 하한)

### 사용한 canonical 입력 (모두 Cat A)

| 정리 | 역할 |
|---|---|
| T8-Core (Cat A) | u*_K는 strict local minimizer |
| T14 gradient flow convergence (Cat A) | Basin B(F_K) well-defined |
| T-Merge(b) (Cat A) | u*_{K-1}은 global minimum, u*_K ≠ u*_{K-1} |
| T-Persist-1(b) (Cat A) | Δ_core ≥ 0.0441β |

### H-MORSE 불필요 여부

✓ Strategy A: H-MORSE 사용 없음. Hessian nondegeneracy 없음. Morse saddle 없음.
✓ Strategy B: H-MORSE 사용 없음. Weyl spectral gap argument만 사용.
✓ AFD-T9 (H-MORSE is Layer 3)와 일관.

### 남은 격차 (개방 문제)

| 격차 | OP 등록 | Layer |
|---|---|---|
| 실제 지수 β^0.89 (또는 β^1.2) analytic 도출 | OP-AFD-004a | **Layer 3** (H-MORSE-Saddle + Modica) |
| 일반 K에 대한 WS/SR 없는 양수성 | OP-AFD-004b | Layer 2 |
| 분기점 근방 (μ→0) 하한 | OP-AFD-004c | Layer 2+ |

### AFD-T7 상태 변경 (권장)

- **이전:** "Proposition + Lemma Candidate" (C_K(K,K-1) > 0은 Lemma Candidate)
- **이후:** "Proposition + **Cat B Proposition** (C_K(K,K-1) > 0)" (H1-H4, WS, SR 조건부)
- `afd_theorem_registry.md` 업데이트 필요

---

## 작업 3: 전략적 검토 — CV-1.14 Track A 상태

W7 strategic plan의 Track A (H-MORSE-Local Cat B):
- **오늘 Track B(AFD)에 집중**하여 OP-AFD-004 Cat B 달성
- Track A (M-A2 수치 검증)는 내일(Day 3) 착수 예정
- `CV114_H_MORSE_PACKAGEII/09_CV114_recommendation.md` 확인 완료

**M-A2 블로커 상태:** canonical 15×15 minimizer의 Stab_{Aut(G)}(u*)가 {e}인지 미확인.
- 이 검증이 Track A의 1번 블로커
- W7 Day 3 세션에서 수치 검증 실행 계획

---

## 오늘 세션 종합

| 항목 | 결과 |
|---|---|
| Canonical 상태 변경 | 없음 (CV-1.13 그대로) |
| 파일 생성 | `THEORY/working/AFD_0/op_afd_004_proof.md` (1개) |
| 파일 수정 | 이 파일 + weekly draft (Day 2) |
| AFD-T7 상태 | Lemma Candidate → Cat B 권장 (registry 업데이트 필요) |
| OP-AFD-004 해결 수준 | **Cat B Resolved** (Strategy A: qualitative; Strategy B: c_low = 0.0221β) |
| 다음 목표 | AFD-T7 registry 업데이트 + M-A2 수치 검증 (Track A) |

---

## Session Close — OP-AFD-004 Pull (ultrawork consolidation)

### OP-AFD-004 status at session close

| Item | Status |
|---|---|
| OP-AFD-004 Cat B sealed | YES — `op_afd_004_proof.md` finalized |
| Strategy A (qualitative basin-exit) | COMPLETE — depends only on T8-Core + T14 + T-Merge(b) Cat A |
| Strategy B (quantitative c_low = 0.0221β) | COMPLETE — conditional on H1-H4+WS+SR |
| exp38 validation (β=50, barrier=23.5, c_low=1.1) | CONFIRMED — factor ~21 conservative |
| Tight exponent β^0.89/β^1.2 | OPEN — OP-AFD-004a, Layer 3 only |
| AFD-T7 registry | UPDATED — Lemma Candidate → Cat B Proposition |
| AFD-0 blocker resolved | YES — OP-AFD-004 no longer blocks AFD-0 |

### Files touched in this session

| File | Action |
|---|---|
| `AFD_0/op_afd_004_proof.md` | Created + Phase 2 wording strengthened |
| `AFD_0/afd_theorem_registry.md` | AFD-T7 row + promotion section updated |
| `AFD_0/afd_open_problems.md` | OP-AFD-004 resolved; 004a/b/c registered |
| `AFD_0/afd_log.md` | Session 2 appended |
| `AFD_0/afd_summary_for_next_agent.md` | UPDATE 2026-05-12 section prepended |
| `logs/daily/2026-05-12/10_afd0_and_op004_session.md` | This file |
| `logs/weekly/2026-05-W2/weekly_draft_storming.md` | Day 2 filled + close note |
| `logs/daily/2026-05-13/00_plan.md` | Created (Day 3 plan) |
| `logs/daily/2026-05-13/01_pre_brainstorm.md` | Created (Day 3 brainstorm) |

### Day 3 handoff

Primary: M-A2 numeric verification (Track A, CV-1.14).
Parallel: AFD-0 external audit (3 agents), OP-AFD-003 infimum attainment.
No new theory branches today. Consolidation complete.
