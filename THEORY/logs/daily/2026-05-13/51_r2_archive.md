---
type: log/daily
date: 2026-05-13
session_label: R-2 archive after C2 sub-threshold merger demonstration failed
canonical_version: CV-1.13 (untouched throughout)
afd_version: AFD-0 v0.1 (untouched throughout)
v_afd_status: ARCHIVED 2026-05-12 → _archive/v_afd_2026-05-12/
r2_status: ARCHIVED 2026-05-13 → _archive/r2_dcr_2026-05-13/
canonical_edits: 0
afd_0_edits: 0
hypothesis_tree_edits: 0
theorem_status_edits: 0
---

# 51 — R-2 archive 결정 (C2 sub-threshold merger demonstration 실패)

## 1. 결정

`exp_r2_subthreshold_merger.py` 실행 결과 R-2 의 load-bearing scope extension 이 numerical demonstration 실패. 사용자 정책 ("C2 실패 시 즉시 archive — K-tuple 도 표현 가능하거나, R-2 form 이 수치적으로 잘못된 예측을 내는 경우") 적용. R-2 working folder 전체를 `_archive/r2_dcr_2026-05-13/` 로 이동.

8개 파일, ~3,800 줄, ~140 KB 가 archive 로 이동. 원래 위치 `THEORY/working/R2_DCR/` 디렉터리 제거. AFD-0 부모, canonical, 모든 다른 working content 는 무영향.

## 2. 폐기 이유 (요약)

이 세션의 *3 단계* 검증:

### Step 1: 내부 self-audit (이전 round)
- R2_audit.md: 10/10 PASS.
- self-audit 만으로는 framing 오류 검출 불가.

### Step 2: 외부 3-critic audit (이전 round)
- 3 opus critics (DECL-1.0 alignment / 수학적 정확성 / V-AFD 실패 모드) 모두 PARTIAL verdict.
- 공통 진단: R-2 가 V-AFD 의 "Cat-A-but-by-construction" 실패를 더 정교한 형태로 반복.

### Step 3: Canonical alignment Explore audit (이번 라운드)
- R-2 Lemmas B2 (centroid mass-weighted) 와 B3 (orientation parallel-axis) 가 canonical `MF/sigma_inherit_k_jump.md` §3.3 와 **수학적으로 동일**.
- R-2 는 새 수식 생산 아님. 단지 K-tuple identity → PD_0 bar identity 라벨 변경.

### Step 4: Decisive test (Phase C2)
- §12: sub-threshold merger 이론 구성 (7-vertex path, ρ_pers=0.5, u_t parametrization).
- C2b: `exp_r2_subthreshold_merger.py` 실행.

**결과:**

| 검증 항목 | 예측 | 측정 | 결과 |
|---|---|---|---|
| K_read^{0.5}(u_t) 불변 | YES | YES (all = 1) | ✓ |
| n_bars 전이 (2→1) | t≈0.5 | t = 0.500 | ✓ |
| R-2 absorbing-centroid jump | |Δc| ≈ 0.36–0.52 | **|Δc| = 0.0000** | ✗ |
| K-tuple centroid smooth | YES | YES (max step 0.001) | ✓ |
| R-2 > K-tuple (10× ratio) | YES | NO | ✗ |

**Verdict: R-2 LOAD-BEARING SCOPE EXTENSION NOT CONFIRMED.**

이유: 내 §12 construction 이 mass-conserving merger 가 아님. `v_4` 의 mass 가 `b_1` 의 absorbing component 로 *전달되지 않고* 그냥 saddle 아래로 erode. 따라서 R-2 Lemma B2 가 적용 안 됨. K-tuple AFD-0 의 K_act=1 trajectory 와 측정 차이 없음.

## 3. 영향 범위 (clean boundary)

- `canonical.md`: 영향 없음. R-2 가 canonical 을 수정한 적 없음.
- `theorem_status.md`: 영향 없음.
- `hypothesis_tree.md`: 영향 없음.
- `AFD-0` working folder (`THEORY/working/AFD_0/`): 영향 없음, intact.
- `MF/`, `SF/`, `temporal/`, `observer_moduli/`, `CV114_*`, `CV115_*`: 영향 없음.
- CV-1.13 봉인 유지, 59A/14B/5C/5R = 83 claims 불변.

R-2 폐기는 V-AFD 폐기 (2026-05-12) 와 *동일한 패턴* 으로 clean.

## 4. 잃은 것 / 잃지 않은 것

### 잃은 것 (의도적)

- D-R2-1 .. D-R2-7 (5+2 정의)
- R2-1 .. R2-6 (6 정리/명제/추측)
- R2-OP9 Lemmas B2/B3/B4 (centroid + orientation + Wigner σ_standard)
- OP-R2-1 .. OP-R2-10 (10 OP)
- OP-R2-9-NONTRANSV, SADDLE-BOUND, MULTIBAR-TRACK, WIGNER-CATA, SPLIT, GOLDSTONE-DEG (6 sub-OPs)
- R2_DISCIPLINE.md (6 rules + compliance checklist)
- exp_r2_sigma_inheritance.py 의 canonical 15×15 numerical results (2.78% / 7.20%)
- exp_r2_subthreshold_merger.py 의 failed scope demonstration

### 잃지 않은 것

- DECL-1.0 의 근본 질문 — DECLARATION.md 에 그대로.
- T8, T14, T-Merge(b), T-Persist-1(b), Predicate-Energy Bridge, T-Temporal-Identity 등 모든 Cat A.
- AFD-0 (working layer) — V-AFD 와 R-2 둘 다 AFD-0 를 수정한 적 없음.
- canonical OP-0008-MERGE Cat B 부분 (centroid+orientation) — R-2 와 *동일한 수식*, canonical 에 이미 존재.
- canonical sigma_rich machinery (SigmaRich, sigma_inherit_k_jump.md, sigma_rich_augmentation.md).
- CODE/experiments/exp_r2_*.py 스크립트 — archive 대상 아님, CODE/ 에 보존. 향후 canonical OP-0008-MERGE Cat A 작업 시 numerical reference 로 활용 가능.

## 5. R-2 vs V-AFD 비교 (두 archive 의 공통 패턴)

| 항목 | V-AFD (2026-05-12) | R-2 (2026-05-13) |
|---|---|---|
| 시작 동기 | GPT-5 meta-research 외부 추천 | DECL-1.0 phenomenological reframe |
| Primitive | `Z = (D, K_act, E, τ)` — K_act 가 좌표 | `S_0 = (PD_0, MT)`, K 는 readout |
| Self-audit | 15/15 PASS | 10/10 PASS |
| External audit | (없었음) | 3-critic + Explore alignment |
| Decisive test | (전혀 없었음) | C2 sub-threshold demo |
| 폐기 사유 | V-AFD-T9 information loss, scope creep T13..T47 | C2 demonstration 실패 + B2/B3 canonical 중복 |
| Lifetime | ~24h | ~24h |
| 잃은 lines | ~8000 | ~3800 |
| canonical 영향 | 0 | 0 |
| AFD-0 영향 | 0 | 0 |

**공통 메타-패턴**: 두 reframe 모두 *language refactoring* 으로 fundamental question 을 우회하려 시도했고, 둘 다 load-bearing canonical 내용 생산에 실패. **언어 재조직은 hard math 의 대체가 아님.**

## 6. 다음 방향 (V-AFD archive 와 동일한 권장)

V-AFD archive note 와 R-2 archive note 모두 권장:

> State report `THEORY/logs/daily/2026-05-13/10_scc_current_state_and_next_expansion_report.md` §7.5 Roadmap C 로 복귀.

구체적으로:
1. **H-MORSE Cat A** — canonical critical-point Hessian positivity (Cat B target now).
2. **OP-0021 T_*** — Mori-Zwanzig route 5 gaps 또는 RG fixed-point route.
3. **Package II Eyring-Kramers Γ_K** — post-H-MORSE.
4. **T-σ-Inherit MERGE-σ** — Wigner-projection W9+ → canonical OP-0008-MERGE σ_standard Cat C → Cat B.
5. **T-K-Select-DYN Cat A** — Q4 closure (DECL-1.0 Q4 답).

V-AFD 와 R-2 둘 다 이 *frontal-attack* 경로를 선택하지 않았고, 둘 다 archive. 다음 세션의 합리적 시작점은 H-MORSE 정면 공격.

## 7. 본 세션의 핵심 통찰

세 가지 감사 라운드 (self / external 3-critic / Explore canonical alignment) 가 *순차적으로* 발견한 문제들:

1. **Round 2 self-audit**: 형식적 일관성 확인. 0 violation. (정작 진짜 문제는 못 봄.)
2. **Round 3 external 3-critic**: DECL-1.0 misalignment, 수학적 디테일 오류 (R2-3 factor-of-2), V-AFD 실패 모드 재발 위험. **그러나 canonical 중복은 못 봄.**
3. **Round 4 Explore canonical alignment**: B2/B3 수식이 canonical `sigma_inherit_k_jump.md` §3.3 와 동일함을 1 세션에 발견. **이전 모든 audit 이 놓친 자리.**

**Lesson**: *Cross-reference against existing canonical working content* 는 별도 audit dimension. 내부 self-audit + 외부 framing review + 수학적 정확성 review 가 모두 통과해도 "이 내용이 이미 canonical 에 있는가?" 질문은 별도로 던져야.

이 lesson 은 R-2 archive 와 함께 보존되어 향후 working-layer reframe 시도에 적용 가능.

## 8. 파일 변경

| 파일 | 동작 |
|---|---|
| `THEORY/working/R2_DCR/` | **REMOVED** (디렉터리, 8 .md 파일 모두) |
| `_archive/r2_dcr_2026-05-13/` | **CREATED** (8 archived files + ARCHIVE_NOTE.md) |
| `_archive/r2_dcr_2026-05-13/ARCHIVE_NOTE.md` | **CREATED** (이 archive 의 archive-side note) |
| `THEORY/logs/daily/2026-05-13/51_r2_archive.md` | **CREATED** (이 파일) |
| `THEORY/CHANGELOG.md` | **PREPENDED** (R-2 archive entry, 최상단) |
| `CODE/experiments/exp_r2_sigma_inheritance.py` | NOT moved (numerical reference 보존) |
| `CODE/experiments/exp_r2_subthreshold_merger.py` | NOT moved (numerical reference 보존) |
| `CODE/experiments/results/exp_r2_*.json` | NOT moved |

## 9. 슬로건

> V-AFD 와 R-2 모두 *언어 재조직* 으로 근본 질문을 우회하려 시도했고, 둘 다 load-bearing canonical 내용 생산에 실패했다. 다음 방향은 H-MORSE / Eyring-Kramers / σ_standard Wigner-projection 의 *정면 공격* 이다 — 우회가 아니라.

---

*End of `51_r2_archive.md`. R-2 branch closed by author decision per C2 failure. Archive frozen.*
