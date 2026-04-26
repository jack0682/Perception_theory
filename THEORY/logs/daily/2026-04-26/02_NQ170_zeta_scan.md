# 02_NQ170_zeta_scan.md — W5 Day 1: NQ-170 Results — Method-Level Crisis + V5b Reproducibility Issue

**Session:** 2026-04-26 (W5 Day 1)
**Target (from plan.md):** ζ-scan crossover quantification (Theorem 1 V5b 검증)
**This file covers:** Numerical results + honest interpretation + NQ-170 protocol limitation + NQ-172 reproducibility crisis
**Depends on reading:** `01_exploration.md` (approach), `04-25/02_NQ168_commensurability.md` (super-lattice confirmation), `04-24/27_deep_dive_results.md` (V5b state)

---

## §1. 결과 요약 (raw)

### 1.1 ζ별 F=1 minimizer search outcome

| ζ | β | F=1 found / 3 seeds | Mode 1 max_overlap (per seed) |
|---|---|---------------------|-------------------------------|
| **0.1** | 100.0 | **0/3** (all F=0) | — |
| **0.2** | 25.0 | **0/3** (all F=0) | — |
| **0.3** | 11.1 | **0/3** (all FAILED, no convergence) | — |
| **0.4** | 6.25 | **0/3** (all FAILED, no convergence) | — |
| **0.5** | 4.0 | **1/3** (seed 0; seeds 1,2 → F=4) | 0.944 (one F=1 found) |
| **0.7** | 2.04 | **2/3** (seed 0 FAILED; seeds 1,2 found) | **0.000, 0.000** |
| **1.0** | 1.0 | **3/3** (all found) | **0.000, 0.000, 0.000** |

### 1.2 Eigenvalue magnitudes (Mode 1, lowest non-tangent)

- ζ=0.5 seed=0: λ_1 = 1.47e-1 (orbital scale)
- ζ=0.7 seed=1,2: λ_1 = -6.0e-15, -1.2e-14 (**numerical zero**)
- ζ=1.0 all seeds: λ_1 = -7.8e-15, -7.0e-15, +1.0e-14 (**numerical zero**)

### 1.3 자동 crossover detection 결과

스크립트는 ζ_* ≈ 0.735 (linear interpolation between ζ=1.0 [overlap=0] and ζ=0.5 [overlap=0.944])를 보고하지만, **이는 잘못된 해석**이다 — ζ=1.0의 overlap=0이 V5b prediction (NQ-168 04-25 결과: 5 seeds 모두 overlap > 98%)과 정면 모순.

---

## §2. 정직한 진단: 두 가지 분리된 문제

### 2.1 Problem A: Sub-lattice 영역에서 F=1 minimizer search 실패

**Observation**: ζ ≤ 0.4 (β ≥ 6.25)에서 random tanh IC + n_restarts=1로 F=1 minimizer 도달 0/12.

**Cause analysis**:
- High β regime: ξ_0 작음 (sharp interface). Random IC tanh disk가 *부드러워서* (ic_width ≥ 0.2), gradient flow가 multi-peak 또는 uniform 으로 collapse.
- W4 04-23 R23 dataset의 sub-lattice (ζ=0.183) F=1 minimizer는 **R23의 90-run × 3 IC modes** (eigmode_combo + fiedler_random + random)로 찾았음 — single-attempt random IC가 아님.

**Diagnosis**: 본 protocol (random tanh IC + n_restarts=1)은 **sub-lattice 영역에서 F=1 minimizer search에 부적합**. Adaptive IC (Fiedler eigenmode) 필요.

**Implication for V5b**:
- NQ-170로 ζ ≤ 0.4 영역에서 V5b sub-lattice prediction (Mode 1 max_overlap < 0.5) 직접 검증 불가.
- 그러나 W4 04-25 NQ-128 (R23 ζ=0.183, 56 minimizer median λ_0/λ_1=0.87)이 sub-lattice prediction을 이미 Cat A 확인. **간접적 보존**.

### 2.2 Problem B: Super-lattice 영역에서 NQ-168과 결과 불일치

**Observation**: ζ=1.0, L=20에서:
- **NQ-168 (04-25)**: 5 seeds 모두 Mode 1 = near-zero Goldstone, max_overlap > 98%
- **NQ-170 (오늘)**: 3 seeds 모두 Mode 1 = numerical zero, max_overlap = 0.000

**Setup 비교**:
- 둘 다 L=20, c=0.5, β=1.0, pure E_bd (w_cl=0, w_sep=0, w_bd=1)
- NQ-168 seed function: `seed * 37 + 7` (NQ-168 script)
- NQ-170 seed function: `seed * 41 + 11` (NQ-170 script)
- 외에 모든 파라미터 동일

**가능한 원인**:
1. **다른 IC seed → 다른 minimizer convergence**: NQ-170에서 도달한 minimizer가 NQ-168과 *질적으로 다른* basin (uniform-like or saddle).
2. **Numerical precision artifact**: max_overlap = 0.000 정확히는 *eigenvector가 translation 공간과 완전 orthogonal* 의미. Hessian near-singular한 경우 (mode 1, mode 2가 모두 numerical zero) eigenspace가 ill-defined.
3. **Translation_modes 함수 issue**: u가 거의 uniform이면 du_x, du_y ≈ 0 vector → norm=1e-14로 div → noise.

**Test**: ζ=1.0 NQ-170 결과의 minimizer u가 실제로 disk-shaped인지 (NQ-168) vs uniform-like인지 (suspected) 확인 필요. 본 세션에서는 미수행 (W5 Day 2 작업).

### 2.3 단일 data point: ζ=0.5 seed=0

**Single F=1 minimizer at ζ=0.5**: max_overlap = 0.944 (overlap_x = 0.944, overlap_y = 0.000), λ_1 = 0.147.

**해석**: 
- λ_1 = 0.147 = orbital scale (NOT near-zero) — 즉 *PN-barrier가 finite하게 lifted Goldstone*
- 98.5% x-translation overlap — Goldstone character는 retained
- This is **V5b super-lattice (ζ ≥ 0.5) Goldstone existence prediction과 일치**

이 1 data point는 V5b의 super-lattice branch lower boundary (ζ ≈ 0.5)를 시사하는 단일 지지 evidence이지만, 통계적 의미 없음 (n=1).

---

## §3. NQ-172 reproducibility crisis 등록

**새 NQ-172**: NQ-168 (04-25) 과 NQ-170 (04-26) 의 ζ=1.0 L=20 결과가 정반대. 동일 setup에서 결과 양극화.

**Falsification candidates**:
1. **NQ-168이 잘못 측정**: 04-25 결과의 98% overlap이 random luck or implementation artifact. (5 seeds 모두 confirmation이 통계적으로 약함)
2. **NQ-170이 잘못 측정**: 본 세션의 max_overlap=0.000 결과가 uniform-collapsed minimizer 측정. Eigenvector projection이 ill-defined된 경우 정확히 0이 나올 수 있음.
3. **Both partial**: V5b super-lattice branch가 *seed-sensitive* — 일부 IC에서는 Goldstone, 일부에서는 collapse. Basin structure 자체가 multi-modal.

**다음 step (W5 Day 2)**:
1. ζ=1.0 L=20에서 minimizer u의 *직접 visualization* — disk shape 확인
2. NQ-168 seed=0 setup을 정확히 재실행 (`seed * 37 + 7`)하여 04-25 결과 재현
3. NQ-170 seed=0 setup으로 NQ-168과 같은 측정 — 두 결과의 차이 source 분리

이를 NQ-172로 등록.

---

## §4. V5b prediction check (revised)

**원래 V5b predictions**:
- (V5-a) ζ ≤ 0.3: orbital only, no Goldstone — **NQ-128 (R23 ζ=0.183)에서 Cat A 확인 (04-25)**, NQ-170로 직접 ζ=0.1, 0.2 검증 *불가능* (F=1 search 실패).
- (V5-b) ζ ≥ 0.5: Goldstone existence — **NQ-168 (ζ=1.0)에서 Cat A 확인 (04-25)** but **NQ-170 (ζ=1.0)에서 negative result** ⚠ NQ-172 reproducibility issue.
- (V5-c) commensurability splitting: Cat A (NQ-168 04-25 15 seeds).
- (V5-e) crossover ζ_* ≈ 0.3-0.4 smooth: **NQ-170에서 검증 불가** (sub-lattice region search 실패 + super-lattice region NQ-168과 모순).

**수정된 V5b 상태 (post-NQ-170)**:
| Sub-statement | 상태 |
|--------------|------|
| (V5-a) Sub-lattice no Goldstone | **Cat A** (NQ-128 confirmed). NQ-170로 추가 검증 미달성. |
| (V5-b) Super-lattice Goldstone existence | **Cat A → 의문 제기** (NQ-168 vs NQ-170 모순). NQ-172 reproducibility 검증 필요. |
| (V5-c) 2D doublet commensurability split | **Cat A** (NQ-168 04-25). NQ-170에서 단일 ζ=0.5 seed에서 partial 일치 (1 mode at orbital scale). |
| (V5-d) β-scaling ν=5.8 | Cat B 유지 (NQ-170 미측정). |
| (V5-e) Crossover smooth ζ_* ≈ 0.3-0.4 | **검증 미달성**. NQ-170 protocol 부적합. |

---

## §5. 본 세션의 honest contribution

**Negative results는 진전이다**. 본 세션이 보여준 것:

1. **Method-level limit**: Random tanh IC + single-attempt F=1 search는 ζ-scan crossover quantification에 *부적합*. Sub-lattice 영역에서 minimizer search 실패. **W5 Day 2 protocol에 Fiedler eigenmode IC 도입 필요**.

2. **NQ-172 reproducibility crisis 발견**: 04-25 NQ-168 (positive)과 04-26 NQ-170 (negative)의 ζ=1.0 L=20 결과 모순. V5b super-lattice branch가 *robust*인지 *seed-sensitive*인지 W5 Day 2에서 결정.

3. **단일 ζ=0.5 data point**: max_overlap=0.944는 V5b super-lattice lower boundary가 ζ ≈ 0.5 근처일 가능성을 단일 example로 시사. n=1이므로 통계적 의미 없음.

**Healthy process**: V5b 6 iteration (V1→V5b in W4) + 본 세션 W5 Day 1의 method-failure 식별이 **검증 우선** 정신의 직접적 실현. 04-24 V4/V5a in-session retraction과 동일한 pattern — 결과가 기대와 다르면 정직히 기록 + 재검토.

---

## §6. W5 Day 2 priority (revised after NQ-170)

**Original W5 Day 1 plan**: G0 NQ-170 ζ-scan + G1 V5b status update.
**Actual W5 Day 1 outcome**: G0 *attempted*, method limitation 발견 + NQ-172 reproducibility crisis.

**W5 Day 2 (2026-04-27) revised priority**:
1. **P0: NQ-172 reproducibility check** — NQ-168 seed=0 (`seed * 37 + 7`) 재실행 + NQ-170 seed=0 (`seed * 41 + 11`) 재실행, 두 minimizer를 visualization + Hessian eigenstructure 직접 비교.
2. **P0 (조건부)**: NQ-172 결과가 NQ-168 reproducible 확인 시 → NQ-170b (adaptive IC ζ-scan) 실행. NQ-168 falsified 시 → V5b super-lattice branch Cat A → Cat B 격하 + 더 깊은 조사.
3. **P1: NQ-170 results의 partial 정보 활용**: ζ=0.5 seed=0의 0.944 overlap 단일 data point가 V5b super-lattice lower boundary 후보 ζ_* ≈ 0.5를 시사 — W5 후반 multi-seed scan으로 통계 확보.

---

## §7. 결론

**NQ-170 자체는 crossover quantification 미달성**. 그러나 두 가지 substantive contribution:

1. **Method limitation 명시화**: ζ-scan은 adaptive IC 필요 (random IC 부적합).
2. **NQ-172 reproducibility crisis 발견**: V5b super-lattice branch (Cat A) 의 robustness 의문 제기. 04-25 NQ-168 결과를 *맹목적으로 trust 하지 말 것* — W5 Day 2에서 직접 reproduction 검증.

**V5b 상태 (post-NQ-170, 2026-04-26)**:
- Sub-lattice (V5-a): Cat A 유지 (NQ-128 04-25 기반).
- Super-lattice (V5-b): **Cat A 의문** — NQ-172 결과 대기.
- Commensurability split (V5-c): Cat A 유지 (NQ-168 04-25 기반).
- Crossover (V5-e): 미검증, 미falsified.

**Canonical impact**: 본 세션 결과로 V5b의 canonical 승급은 *지연*. T2 유지 (W5+ 추가 검증 후 결정). canonical.md / theorem_status.md 직접 수정 없음 (hard constraint).

---

**End of 02_NQ170_zeta_scan.md.**
**Honest verdict: NQ-170 method failed for crossover quantification. NQ-172 reproducibility crisis discovered. V5b super-lattice branch Cat A → 의문 제기.**
