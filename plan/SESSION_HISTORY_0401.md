# Session History — 2026-04-01

## 세션 개요
T-Persist-1 Gap 4/5/6 감사, 수리, 보강, Phase 1 실행까지 완료.

---

## 타임라인

### 1. 초기 상태 확인
- Git 연동: `git@github.com:jack0682/Perception_theory.git` ← 로컬 `/home/jack/ex` 연결
- Plan_0331.md, Plan_0401.md 확인
- 이전 세션에서 이미 strong-regime theorem ladder, near-bifurcation local theory, 3-regime synthesis 작성 완료

### 2. 감사 (Audit) — 6개 문서 점검
3개 Explore 에이전트 병렬로 6개 문서 감사:

| 문서 | 점수 | 치명적 문제 |
|------|------|------------|
| CORE-DEPTH-ISOPERIMETRIC.md (Gap 6) | 5.5/10 | Prop 3 공식 14× 오류, Γ→finite-β 미증명, Thm 2 15% 위반 |
| BASIN-ESCAPE-ANALYSIS.md (Gap 4) | 5/10 | Boundary-mode 미증명, r≥0.210 대체 없음 |
| TRANSPORT-CONCENTRATION-STRENGTHENED.md (Gap 5) | 4/10 | 해석적 bound 오류, Schauder Step 7 불완전 |
| T-PERSIST-K-STRONG-MORSE-ATTEMPT.md | 8/10 | Selection hypothesis 미정의 |
| THREE-REGIME-SYNTHESIS.md | 7/10 | 조직적 문서 |
| NEAR-BIFURCATION-LOCAL-THEORY.md | 6/10 | 비정식 원리만 |

### 3. 수리 (Repair) — 6건 결함 수정
4-agent 팀 (`formula-fixer`, `gamma-prover`, `schauder-fixer`, `boundary-prover`):

| 결함 | 수정 |
|------|------|
| Prop 3 공식 14× | C₂ 서술 = 유도 = 2.875 |
| Γ→finite-β Step 4 | Markov + EL bootstrap 3단계 증명 |
| Thm 2 위반 | 2a (무조건 항등식) + 2b (조건부) split |
| ‖∂φ/∂u‖ bound | P doubly stochastic 증명 + vertical-stack norm |
| Schauder Step 7 | Finite-time flow truncation (IFT 불필요) |
| Boundary-mode 미증명 | Prop BMD: Hessian diagonal gap, core fraction O(1/β) |

커밋: `f6bdd3a` → 푸시 완료

### 4. 심화 (Deep Strengthen) — 3-agent
`basin-agent`, `chain-agent`, `theory-agent`:

| 결과 | 내용 |
|------|------|
| exp24 | Sublevel estimate 3-12× 보수적 |
| exp26 | T-Persist chain (a)(c)(e) 100% 통과, (b)(d) basin-switching 문제 |
| ‖J_φ‖ ≤ 1.75 | Formation-conditional bound |
| NB-1/NB-2 | 분기점 정량 정리, 3-tier ladder |

### 5. 최종 보강 (Final Strengthen) — 3-agent
`code-agent`, `synthesis-agent`, `stress-agent`:

| 결과 | 내용 |
|------|------|
| transport.py | 3-component fingerprint default, 175 tests |
| **exp27** | **5/5 parts × 5/5 configs = 100% PASS** (warm-start) |
| exp28 | 84/100 stress test, n≥64 β≥20 전부 통과 |
| T-PERSIST-FULL-PROOF.md | 450줄 통합 증명 문서 |

커밋: `46dd9a3` → 푸시 완료

### 6. Phase 1 (B1 + B2 + C3) — Round 1 + Round 2

**Round 1** (3-agent: `beta-agent`, `basin-dir-agent`, `delta-agent`):

| Task | 결과 |
|------|------|
| B1 β_crit | 58α → 20α (discrete max principle, C₂ 우회) |
| B2 Directional basin | Ellipsoidal 1.5-3.3×, PSM/EBC/TP 3 theorems |
| C3 Δ_bdy formula | μ³/(216β²λ²S₃²), S₃ = boundary asymmetry invariant |

**Round 2** (`round2-agent`):
- B1: 2× safety → 정확한 source bound (19.55α exact)
- B2: gradient vs IFT soft-mode fraction 구분
- C3: 12×12 outlier 비재현성 확인 + 보정항
- docs/04-01/INDEX.md 생성

**Round 3 (리드 직접 검증)**:
- S_x가 grid/β dependent (2.1-6.9) → β_crit도 config-dependent (15-33α)
- Canonical Spec 업데이트: β_crit = "config-dependent 15-33α"

커밋: `40f6493` → 푸시 완료

---

## 현재 Git 상태
```
master @ 40f6493
origin: git@github.com:jack0682/Perception_theory.git
175 tests passing
```

## 현재 파일 현황
- 증명 문서: docs/03-31/proof/ (6개), docs/04-01/proof/ (1개)
- 이론 문서: docs/03-31/theory/ (3개)
- 통합 문서: docs/03-31/synthesis/T-PERSIST-FULL-PROOF.md
- 실험: exp18-33 (16개)
- 계획: plan/Plan_0331.md, Plan_0401.md, Plan_0401_revised.md, Plan_0401_open_problems.md

## 미해결 문제 (우선순위순)

### A급 (필수)
- **A1. Strong-regime transport selection** — Schauder 존재 증명됨, 유일성/선택 미증명
- **A2. K-Strong merge dichotomy** — instability 증명됨, (K-1) descent 미증명

### B급 (완료됨)
- ~~B1. β_crit~~ → 19.55α (config-dependent 15-33α) ✅
- ~~B2. Directional basin~~ → Ellipsoidal 1.5-3.3× ✅
- **B3. Near-bif boundary-layer dynamics** — NB-1/NB-2 증명됨, boundary node 운명 미해결

### C급 (장기)
- ~~C3. Δ_bdy formula~~ → S₃ invariant ✅
- **C1. Product-manifold basin on Σ^K_M** — A2 필요
- **C2. Formation birth/death** — 미탐색

## 다음 세션에서 할 일
- Phase 1 검증 결과 최종 확인
- A1 (strong-regime selection) 수치 실험 시작 (exp29: λ_tr sweep)
- A2 (K-Strong merge) 2-formation 구체적 예시 시도
- 또는 사용자 지시에 따라 다른 방향

## 주요 실험 결과 요약

| 실험 | 핵심 결과 |
|------|----------|
| exp18 | Deep core: 62/62 존재 (|Core|≥25) |
| exp19 | Soft mode: 90%+ boundary |
| exp21-23 | r_soft < 0.210 in 21/32 configs (r≥0.210 반증) |
| exp24 | 실제 basin 3-12× > sublevel estimate |
| exp25 | Hessian diagonal: boundary 최소 확인 |
| exp26 | Chain: (a)(c)(e) universal, (b)(d) basin-switching |
| **exp27** | **Warm-start: 5/5 × 5/5 = 100% PASS** |
| exp28 | Stress: 84/100, n≥64 β≥20 전부 통과 |
| exp31 | β threshold scan |
| exp32 | Directional basin: ellipsoidal 1.5-3.3× |
| exp33 | Δ_bdy S₃ formula: 6/7 configs 1-7% |

## 핵심 정리 상태

| 정리 | 상태 |
|------|------|
| T-Persist-1(a) IFT | **Proved** |
| T-Persist-1(b) Basin | **Conditional** (GT+NB, boundary-mode bottleneck) |
| T-Persist-1(c) Shifted | **Proved** |
| T-Persist-1(d) Exact | **Conditional** (H2'+H3, β≥20α) |
| T-Persist-1(e) Transport | **Conditional** (fixed-point: Schauder ✅, selection: WR') |
| Schauder fixed-point | **Proved** (finite-time flow) |
| Deep core existence H2' | **Proved** (Γ + isoperimetric + max principle) |
| Boundary-mode dominance | **Proved** (Prop BMD) |
| NB-1 Basin collapse | **Proved** (Δ = O(μ³)) |
| NB-2 Deep-core remnant | **Proved** |
| K-Sep | **Proved** |
| K-Weak | **Conditional** |
| K-Strong | **Conjectured** (theorem ladder) |
