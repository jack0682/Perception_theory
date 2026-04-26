# 03_V5b_status_update.md — Theorem 1 V5b Status (post-NQ-170, post-W5 Day 1)

**Session:** 2026-04-26 (W5 Day 1)
**Target (from plan.md G1):** NQ-170 결과에 따라 Theorem 1 V5b의 Cat 등급 재평가
**This file covers:** V5b 7 iterations 통합 history + post-NQ-170 honest reassessment + canonical 승급 path 재평가
**Depends on reading:** `01_exploration.md`, `02_NQ170_zeta_scan.md`, W4 04-24 V5b deep dive (`27_deep_dive_results.md`)

---

## §1. V5b 7 iterations 통합 history

| V | Date | Claim | 근거 | Status |
|---|------|-------|------|--------|
| V1 | W4 04-24 morning | Goldstone universal | initial intuition | Falsified by G1 |
| V2 | W4 04-24 (G1) | 3-geometry (T/T_off/O) | L=16 center disk test | Incomplete |
| V3 | W4 04-24 (C3-T) | Regime-based (sub/super-lattice) | torus null result | Misinterpreted via dual-regime |
| V4 | W4 04-24 (24_*) | Dual-regime sharp transition ζ≈1 | 4-point ζ scan | **Retracted in-session (premature)** |
| V5a | W4 04-24 (25_*) | Falsification via critical slowing | Single-mode + L-increase | **Retracted in-session (partially wrong)** |
| **V5b** | W4 04-24 (27_*) | Refined dual-regime + 2D doublet commensurability splitting | Eigenvector projection + L=40 decoupled test | "Current best" through 04-25 |
| **V5b'** | W5 04-26 (this session) | **V5b super-lattice branch Cat A 에 의문 제기** | NQ-170 negative result + NQ-172 reproducibility crisis | **Conditional, pending NQ-172** |

**핵심 update**: V5b가 W4 close 시점에 "Cat A super-lattice + Cat A sub-lattice + Cat A commensurability split"로 평가됐으나, W5 Day 1 NQ-170 ζ=1.0 L=20 결과 (3 seeds 모두 max_overlap=0.000)가 NQ-168 04-25 ζ=1.0 L=20 결과 (5 seeds 모두 max_overlap > 98%)와 **정면 모순** — V5b super-lattice branch의 robustness가 *empirically uncertain*.

---

## §2. V5b 각 sub-statement의 현재 Cat 평가

### (V5-a) Sub-lattice (ζ < 0.3): no Goldstone, orbital only

**Status**: **Cat A 유지** (변동 없음).

**증거**:
- W4 04-25 NQ-128: R23 dataset (L=32, β=30, ζ=0.183), 56 stable Morse-0 minimizer.
  - λ_0/λ_1 ratio: median 0.869, 0% < 0.1, 1.8% < 0.3.
  - Mode 1이 translation Goldstone이 아닌 orbital character — Cat A 직접 확인.
- 90 random IC × 3 IC modes (eigmode_combo + fiedler_random + random) — robust against IC choice.

**NQ-170 contribution**: ζ=0.1, 0.2, 0.3, 0.4에서 F=1 minimizer search 실패 (random IC + n_restarts=1). **새 정보 없음**, sub-lattice prediction 검증 미달성. (V5-a)는 R23 NQ-128 단독으로 Cat A 유지.

### (V5-b) Super-lattice (ζ > 0.5): translation Goldstone existence

**Status**: **Cat A → 의문 제기 (Cat B로 잠정 강등)**.

**04-25 시점 증거 (NQ-168, Cat A 평가)**:
- L=20, 30, 40 × 5 seeds, ζ=1.0, β=1.0 → 15/15 confirmations
- Mode 1 max_overlap > 98% (translation Goldstone)
- Direction (x vs y) seed-dependent flip → commensurability split mechanism 직접 관측
- L=40 β/β_crit=10.15 decoupled test: 99% overlap (criticality-independent)

**04-26 시점 의문 (NQ-170)**:
- 동일 setup (L=20, ζ=1.0, β=1.0, pure E_bd) 3 seeds 모두 max_overlap = 0.000
- λ_1 = numerical zero (-7e-15), 즉 *수치적으로 zero mode이지만 translation 방향 아님*
- 다른 seed function (`seed * 41 + 11` vs NQ-168의 `seed * 37 + 7`)이 결과를 뒤집음

**문제 진단**:
- 가능성 1: NQ-168이 우연히 *favorable basin*에 도달한 5 seeds. NQ-170의 다른 seed가 *uniform-collapsed basin*. **V5b가 IC-sensitive임을 시사**.
- 가능성 2: NQ-170 minimizer가 실제로는 F=1이 아닌 collapsed state (count_local_maxima_torus가 numerical noise로 false positive). **V5b는 robust지만 NQ-170 protocol 결함**.
- 가능성 3: NQ-168 자체가 implementation artifact였고, V5b super-lattice Goldstone existence 자체가 confirmed되지 않은 상태였음. **V5b가 falsified 되었거나 partial**.

**조치**: V5b 의 (V5-b) sub-statement를 *Cat A 잠정 강등 → Cat B with reproducibility caveat*. NQ-172 (W5 Day 2)에서 결정.

### (V5-c) 2D doublet commensurability splitting

**Status**: **Cat A → 의문 제기 (Cat B로 잠정 강등)**.

**04-25 시점 증거 (NQ-168, Cat A 평가)**:
- 15 seeds × 3 L 모두에서 near-zero direction (x vs y) flip 관측
- seed=0: y near-zero (fx=0.049), seed=1: x near-zero (fy=0.491)
- Position-dependent mechanism 직접 관측

**04-26 시점**: NQ-170에서 ζ=1.0 super-lattice 영역 자체가 reproduce 안 됨 → commensurability splitting도 함께 의문. (V5-c)가 (V5-b)에 의존.

**조치**: NQ-172와 함께 W5 Day 2에서 재검증.

### (V5-d) β-scaling ν=5.8

**Status**: Cat B 유지 (NQ-170 미측정, 변동 없음).

### (V5-e) Crossover smooth ζ_* ≈ 0.3-0.4

**Status**: **검증 미달성**. NQ-170 protocol이 sub-lattice 영역에서 F=1 search 실패로 ζ-scan 자체 미실행.

**미달성 이유**:
1. ζ ≤ 0.4에서 random tanh IC + n_restarts=1로 F=1 minimizer 도달 0/12.
2. 따라서 ζ-scan crossover boundary 정량 불가능.

**조치**: W5 Day 2+에서 *adaptive IC* (Fiedler eigenmode) ζ-scan 재시도.

---

## §3. V5b 전체 (Theorem 1)의 canonical 승급 path

### 3.1 W4 close 시점 (2026-04-25)

W4 weekly_summary §3.2에서 Theorem 1 V5b를 **T2** (conditional/regime, canonical 승급 후보)로 분류. 사유:
- 6 iterations + 2 in-session retraction → process trust 우려
- ζ-scan crossover 미정량
- Graph-class extension (free BC, barbell, T³) 미수행
- Nodal count (n_k) explicit verification 미수행

### 3.2 W5 Day 1 후 (2026-04-26)

NQ-170 결과로 status 후퇴:
- (V5-a) sub-lattice Cat A 유지 (NQ-128 단독)
- (V5-b) super-lattice **Cat A → Cat B (의문 제기)**
- (V5-c) commensurability split **Cat A → Cat B (의존성으로 함께)**
- (V5-d) β-scaling Cat B 유지
- (V5-e) crossover ζ_* 미달성

**T-classification**: T2 → **T2-prime (conditional, with reproducibility crisis)**. canonical 승급 보류 + W5 Day 2에서 NQ-172 결정 후 재평가.

### 3.3 향후 canonical 승급 조건 (revised)

V5b가 canonical T1로 승격되려면:

1. **NQ-172 reproducibility resolved**: NQ-168 결과가 reproduce 됨 (또는 NQ-170 결과의 artifact 원인 식별).
2. **ζ-scan crossover quantification**: adaptive IC로 ζ_* boundary 정량.
3. **Graph-class extension**: torus T² 외 free BC + barbell + T³ 중 ≥ 2 graph class에서 super-lattice Goldstone 확인.
4. **Nodal count explicit**: σ-framework의 (n_k, [ρ_k]) Cat A로 V5b mode들 분류.

이 4 조건이 모두 충족되어야 V5b canonical 승급. 현재 (W5 Day 1 후): **0/4** (NQ-128로 sub-lattice Cat A만 단단함).

**예상 timeline**: W5+W6 (2 weeks) ~ 1 month, 빠른 progress 시.

### 3.4 만약 NQ-172에서 NQ-168 falsified될 경우

가능성 (사전 추정): ~30%. 이 경우:
- V5b super-lattice branch (Cat A → Cat C 또는 retracted) 격하
- W4 weekly_summary §3.2의 T2-1 entry retraction
- W4 V5b "current best"가 W5에서 *retracted* — 04-24 V4/V5a 패턴이 한 단계 더 (V5b → V5c 시도) 진행되는 셈
- V5c (post-V5b) 작성 필요: super-lattice 영역의 진짜 spectral structure가 무엇인지 재정립

**Honest acknowledgment**: 이 가능성은 04-25 NQ-168 5-seed confirmation을 *strong evidence*로 받아들였던 W4 close evaluation이 *premature*였을 가능성을 의미. V5b가 V4/V5a 패턴을 한번 더 반복하는 것 — 이번에는 W4 close 직후에.

---

## §4. 본 update의 process implication

### 4.1 W4 weekly_summary 정직성 점검

W4 weekly_summary.md §7.2 ("V5b는 T2 유지, ζ-scan + graph-class 검증 후 결정")가 *boundary 위에서 일하는 자세*로 적절했음. T1으로 격상시키지 않은 것은 옳은 결정.

W4 §3.2의 V5b sub-component Cat 평가 ("super-lattice Cat A existence + commensurability split Cat A")는 W5 Day 1 결과에 비추어 보면 **다소 strong**. 더 cautious한 wording이 적절했을 수 있음. 이는 lesson learned for W5 weekly_summary.

### 4.2 04-24 7 iteration의 honest pattern

V1 → V5b까지 6 iteration이 W4 single day에 일어남. 이것이 W5 Day 1에서 *7th iteration potential* (V5b → V5b' or V5c)을 보임. 즉:

- W4 04-24 V1 (universal Goldstone) → V5b (refined dual-regime + commensurability split)
- W5 04-26 V5b → ?

**Question**: V5b의 "current best" 평가가 W4 close에서 너무 빨리 굳어졌나? Or NQ-168의 5-seed evidence가 *충분*이라 평가했던 것이 합리적이었으나 W5 NQ-170이 *예상치 못한* reproducibility issue를 드러낸 것인가?

후자가 맞다면, V5b의 current 상태는 *learning event*이지 *retraction*이 아님. 더 신중한 검증으로 전진.

### 4.3 ZK process: "검증 우선" 정신

본 세션 (W5 Day 1) 결과가 W4 weekly_summary의 진보 narrative와 *일부 모순*. 그러나 이것을 정직히 기록하는 것이 SCC project의 consistent 정신:
- W4 04-24: "사용자의 3차 skepticism이 V5b 도달 강제"
- W5 04-26: "method-failure 발견 + NQ-172 reproducibility crisis 등록"

**Pattern**: 매 step이 *추가 검증을 요구*. canonical 승급은 multiple independent verifications 후에만.

---

## §5. 결정 사항

### 5.1 V5b 상태 (현재, 2026-04-26 EOD)

| Component | Pre-NQ-170 (04-25) | Post-NQ-170 (04-26) |
|-----------|-------------------|-------------------|
| (V5-a) Sub-lattice no Goldstone | Cat A | **Cat A** (NQ-128 단독, 안정) |
| (V5-b) Super-lattice existence | Cat A | **Cat B (Cat A 의문)** |
| (V5-c) Commensurability split | Cat A | **Cat B (Cat A 의문)** |
| (V5-d) β-scaling ν=5.8 | Cat B | Cat B (변동 없음) |
| (V5-e) Crossover ζ_* ≈ 0.3-0.4 | Cat C | **검증 미달성** |
| Theorem 1 V5b overall | T2 | **T2 with reproducibility crisis** |

### 5.2 Canonical impact

**현재 canonical 변경 없음** (hard constraint 준수). V5b는 W5+에서 NQ-172 등 추가 검증 후 결정.

### 5.3 W5 Day 2 우선순위 (확정)

**P0**: NQ-172 reproducibility test
- NQ-168 seed=0 setup (`seed * 37 + 7`, L=20, ζ=1.0, β=1.0) 정확히 재실행
- NQ-170 seed=0 setup (`seed * 41 + 11`, 같은 params) 정확히 재실행
- 두 minimizer u의 visualization (heatmap + cross-section)
- Hessian eigenstructure 직접 비교 (lowest 6 modes)
- Goldstone overlap 차이의 source 식별

**P1 (조건부)**: NQ-172 결과
- NQ-168 reproducible → V5b super-lattice Cat A 회복 + NQ-170b (adaptive IC ζ-scan) 진행
- NQ-168 falsified → V5b super-lattice (Cat A → Cat C/retracted) + V5c iteration 시작

---

**End of 03_V5b_status_update.md.**
**Verdict: V5b T2 → T2 with reproducibility crisis. (V5-b) + (V5-c) Cat A 의문 제기. NQ-172 (W5 Day 2)이 V5b future를 결정.**
