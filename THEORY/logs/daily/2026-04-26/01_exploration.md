# 01_exploration.md — W5 Day 1: NQ-170 ζ-scan Exploration

**Session:** 2026-04-26 (W5 Day 1)
**Target (from plan.md):** Theorem 1 V5b의 sub-lattice ↔ super-lattice crossover 경계 ζ-scan으로 정량화
**This file covers:** Restatement (§1) + Multi-approach (§2) + Primary selection (§3)
**Depends on reading:** `04-24/27_deep_dive_results.md` (V5b state), `04-25/02_NQ168_commensurability.md` (super-lattice 확인), `04-25/01_sigma_numerical.md` (sub-lattice 확인 NQ-128)

---

## §1. Restatement (target 재진술)

### 1.1 plan.md의 표면 statement

> "Theorem 1 V5b의 sub-lattice (ζ < 0.3) ↔ super-lattice (ζ > 0.5) crossover 경계를 ζ-scan으로 정량화. ζ_* ≈ 0.3-0.4 추정의 수치 확정 또는 falsification."

### 1.2 무엇이 진짜 물음인가

**기본 사실 (W4에서 확정)**:
- W4 04-24 V5b는 6 iteration (V1→V5b)을 거쳐 도달한 *current best* state. V4, V5a는 in-session retracted.
- Sub-lattice ζ ≈ 0.18 (R23 NQ-128, L=32 β=30): 56 stable minimizer, λ_0/λ_1 median 0.87, 0% Goldstone evidence → *sub-lattice prediction confirmed*.
- Super-lattice ζ = 1.0 (NQ-168, L=20-40 β=1): 15 F=1 minimizers 전부에서 Mode 1 translation overlap > 98% → *super-lattice prediction confirmed*.
- **잔존 ambiguity**: ζ ∈ (0.18, 1.0) 사이 어디서 sub → super transition이 일어나는가? 04-24 27_*.md는 "ζ_* ≈ 0.3-0.4"로 추정만.

### 1.3 success/failure 정의 (명시화)

**Success**:
- ζ scan에서 max(overlap_x, overlap_y)가 ζ에 대해 monotone으로 증가
- 함수 형태가 sigmoidal (smooth crossover) 또는 sharp transition (둘 다 V5b의 부분적 confirmation)
- crossover 경계 ζ_* (예: max_overlap = 0.5 위치) 정의 가능

**Partial success**:
- monotone이지만 V5b 추정 (0.3-0.4)을 벗어남 → V5b refinement (좁은 의미 falsification)
- Sub-lattice/super-lattice prediction이 일부 ζ에서 fail → V5b의 일부 statement만 holds

**Failure (V5b crossover 가설 falsification)**:
- max_overlap이 non-monotone (예: 중간 ζ에서 spike 또는 dip)
- Region-dependent (특정 seed/L에서만 transition 발생)
- V5b의 "smooth crossover" framing 자체가 잘못됨

### 1.4 plan.md의 암묵 가정 surfacing

1. **Smooth crossover 가정**: V5b는 0.3-0.4 사이가 smooth. 그러나 실제 spectral crossover는 first-order (sharp) 일 가능성 — Goldstone existence는 PN barrier scaling에 따라 thresholdic 일 수 있음.
2. **L=20 단일 시스템**: 04-25 NQ-168은 L=20, 30, 40에서 모두 Goldstone 지속 확인. L=20 단독으로 결론 도출 가능 가정.
3. **β = 1/ζ² 변환의 정당성**: ξ_0 = √(α/β), α=1, lattice spacing a=1 → ζ = ξ_0/a = √(1/β). 이 관계 하에서 ζ만 변경 = β만 변경.
4. **Pure E_bd 이외에는 별도 동역학 없음**: Closure (λ_cl) 효과는 04-25 NQ-168 Hypothesis C에서 약하다 확인 (ratio 1.2). Pure E_bd로 충분.

---

## §2. Multi-approach (4 candidate)

### A1: Mode 1 translation overlap scaling (primary candidate)

**Idea**: Lowest non-tangent eigenmode (Mode 1)의 translation 방향 (δu_x, δu_y) overlap을 ζ scan으로 측정. max(overlap_x, overlap_y) > 0.5 가 V5b super-lattice 정의에 가까움.

**Math tool**: Hessian eigendecomposition + tangent projection.

**Success form**: ζ vs max_overlap의 monotone 함수, sigmoid fit. ζ_* = arg(max_overlap = 0.5).

**Failure mode**: Non-monotone (V5b falsification) 또는 모든 ζ에서 max_overlap > 0.5 (orbital 영역 부정 — 불가능, NQ-128로 sub-lattice 확인됨).

**Interaction with V5b**: V5b의 (V5-a, V5-b, V5-e) 모두 직접 검증. Crossover 정량화 = V5b 강화 또는 falsification.

### A2: Eigenvalue scaling λ_1(ζ)

**Idea**: Mode 1 eigenvalue λ_1을 ζ scan으로 측정. V5b 예측: ζ ≤ 0.3에서 λ_1 = O(β) = O(1/ζ²) (orbital scale); ζ ≥ 0.5에서 λ_1 → 0 (PN barrier-suppressed Goldstone).

**Math tool**: λ_1 vs ζ log-log plot. Slope -2 (sub) → 급격한 drop (super) crossover.

**Success form**: λ_1(ζ) crossover scaling exponent + ζ_* ≈ 0.3-0.4 confirmation.

**Failure mode**: λ_1이 monotonic decrease (no crossover signature) 또는 step-function (sharp transition, smooth 가정 부정).

**A1과의 독립성**: A1은 mode "성격"을, A2는 "energy scale"을 측정. 둘 다 supports V5b 시 strong evidence; A1 supports + A2 contradicts 시 mode mixing 발생.

### A3: Goldstone doublet existence test

**Idea**: 4 modes 중 *몇 개*가 translation overlap > 0.9 인지 카운트. V5b 예측: super-lattice에서 2-fold Goldstone doublet (단, commensurability split으로 한쪽 near-zero, 한쪽 orbital scale).

**Math tool**: 각 mode에서 max(overlap_x, overlap_y) 측정. doublet count = #{k : max_overlap_k > 0.9}.

**Success form**: ζ ≥ 0.5에서 doublet count = 2 (또는 split-aware: 1 near-zero + 1 orbital-scale x-trans). ζ ≤ 0.2에서 doublet count = 0.

**Failure mode**: doublet count가 ζ에 무관하게 0이나 1.

**A1과의 차이**: A1은 lowest mode만, A3은 lowest 4 modes 전체. Commensurability split (NQ-168 발견)이 A3에서 더 명확히 보임.

### A4: ζ-scan with multiple L (graph-class extension proxy)

**Idea**: ζ ∈ {0.2, 0.4, 0.7} × L ∈ {16, 20, 30}. ζ_* 가 L-independent임을 확인 — 이것이 V5b crossover의 universal 성격을 시사.

**Math tool**: ζ-L 2D scan. 각 (ζ, L)에서 max_overlap.

**Success form**: ζ_* (overlap=0.5 crossing)가 L에 무관 (Δζ_* / ζ_* < 0.1). 또는 L-dependent라면 V5b가 finite-size effect 가능성.

**Failure mode**: ζ_*(L)이 systematic L-dependence — V5b가 thermodynamic limit에서 bounded vs L→∞에서 sub/super 구분 사라짐.

**비용**: 3 ζ × 3 L × 3 seeds = 27 minimizers. NQ-170 primary scan 외 추가 1 day 작업 분량.

### Mathematical 독립성 점검

| 접근 | Probe quantity | Success criterion | V5b implication |
|------|---------------|-------------------|----------------|
| A1 | Mode 1 max overlap | sigmoid fit ζ_* | Direct V5b smooth crossover test |
| A2 | Mode 1 eigenvalue | log-log scaling crossover | Energy-scale corroboration |
| A3 | Doublet count | binary indicator transition | Multi-mode structure check |
| A4 | ζ-L 2D scan | L-independence of ζ_* | Universality (graph-size invariance) |

A1과 A2는 mode 1 단독을 다른 측면(성격 vs energy)에서 본다. A3은 4 modes로 확장. A4는 finite-size effect 분리. 4 접근은 mathematically 독립적.

---

## §3. Primary Selection: A1 + A3 (combined)

**Primary**: A1 (Mode 1 translation overlap) — V5b crossover 가설의 가장 직접적 test.

**Supporting**: A3 (doublet count) — multi-mode structure 확인. NQ-168에서 발견한 commensurability split은 A1으로 모드 1만 보면 놓칠 수 있음. A3이 보완.

**Deferred to W5 Day 2+**: A2 (eigenvalue scaling) — primary 결과 해석 후 별도 분석. A4 (L-independence) — 별도 day 작업 (graph-class extension은 W5 Week 마지막 작업).

### 왜 A1 + A3 primary?

1. **A1만 단독**: Mode 1만 보면 commensurability split이 missed (NQ-168 04-25 결과: super-lattice에서 Mode 1 = near-zero Goldstone in *one* direction, x-trans는 orbital scale로 빠짐).
2. **A3만 단독**: doublet count는 binary, smooth crossover 정량 불가.
3. **A1 + A3 결합**: ζ < ζ_* 에서 doublet=0, ζ > ζ_* 에서 doublet=1 (split) or 2 (degenerate). Mode 1 max_overlap이 sigmoidal 변화 → smooth crossover + split mechanism 둘 다 capture.

### 측정 protocol (script `nq170_zeta_scan.py`)

- ζ ∈ {0.1, 0.2, 0.3, 0.4, 0.5, 0.7, 1.0} × N=3 seeds × L=20 torus
- β = 1/ζ² (ξ_0 = ζ)
- Pure E_bd, F=1 minimizer (random tanh IC)
- Hessian lowest 4 modes, projected onto tangent
- Per mode: (eigenvalue, overlap_x, overlap_y, max_overlap)
- Per ζ: aggregate mean ± std of mode 1 max_overlap; identify crossover where mean crosses 0.5

### 예상 outcomes (conditional)

1. **V5b confirmation**: max_overlap ζ-curve가 sigmoidal, ζ_* ∈ [0.3, 0.4] → V5b sub-lattice + super-lattice + smooth crossover all supported. Cat A 강화.
2. **V5b refinement**: ζ_*가 0.3-0.4 외부 (예: 0.45 또는 0.25) → V5b 수치 update, qualitative claim 유지.
3. **V5b partial falsification**: non-monotone or sharp transition → V5b "smooth crossover" 가설 부정. (V5-e) statement 폐기, (V5-a)/(V5-b) 만 유지.
4. **V5b 강한 falsification**: orbital ↔ Goldstone region 분리 자체가 안 보임 → V5b core 가설 (sub/super dichotomy) 부정. 매우 unlikely (NQ-128 + NQ-168이 양 끝 점 이미 확인).

가능성 분포 (사전 추정): outcome 1 ~50%, outcome 2 ~30%, outcome 3 ~15%, outcome 4 ~5%.

---

## §4. Workflow (다음 단계)

1. ✅ `nq170_zeta_scan.py` 작성 + 백그라운드 실행
2. 결과 도착 (`results/nq170_zeta_scan.json`) 후:
   - `02_NQ170_zeta_scan.md` 작성 — A1 + A3 분석 + crossover boundary 정량
3. V5b 상태 update:
   - `03_V5b_status_update.md` — 6 iteration 후 honest assessment + W5+ canonical 승급 path
4. `99_summary.md` + W5 weekly_draft 04-26 entry

---

**End of 01_exploration.md.**
**Next: 결과 대기 → 02_NQ170_zeta_scan.md.**
