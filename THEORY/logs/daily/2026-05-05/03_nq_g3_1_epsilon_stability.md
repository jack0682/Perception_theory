# 03_nq_g3_1_epsilon_stability.md — NQ-G3-1 ε-Stability Sweep (W6 D2 G2.3 fill-in, Silver target)

**Session:** 2026-05-05 (W6 Day 2, post-G2.2-Option-B-capture; G2.3 fill-in per `plan.md` §G2.3)
**Target (from `plan.md` §G2.3 + `op_resolution.md` §11):** Close NQ-G3-1 — verify the L1-I FEASIBLE_WITH_BUDGET = 439/1920 = 22.9% anchor's stability under ε perturbations across the relevant range. Per `op_resolution.md` §11.3 theoretical pre-analysis, expected outcome is **piecewise-constant**: f(ε) ≈ 22.9% on ε ∈ (0, 30); drops to 0 at ε = 30.
**This file covers:** §1 Phase A theoretical pre-analysis (carry from `op_resolution.md` §11.3); §2 Phase B numerical execution (14-ε sweep × 1920 configs = 26,880 total runs); §3 Findings (deeper-than-trivial: §11.3 prediction confirmed for wq1 state_mode; raw_gaussian state_mode revealed as structurally ε-independent); §4 Implication for T-L1-F empirical anchor + Commitment 16; §5 NQ-G3-1 closure verdict; §6 New open question surfaced; §7 Hard-constraint sweep.
**Depends on reading:** `2026-05-04/op_resolution.md` §11 (NQ-G3-1 question + §11.3 pre-analysis + §11.5 execution plan); `CODE/scripts/l1i_constants_feasibility.py` lines 232–283 (compute_feasibility + active-set logic) + lines 503–537 (make_full_sweep state_mode dichotomy); `CODE/scripts/results/l1i_constants_feasibility.json` (baseline 439/1920); `CODE/scripts/op_resolution_nq_g3_1_epsilon_stability.py` (this session's wrapper); `CODE/scripts/results/op_resolution_nq_g3_1_epsilon_stability.json` (this session's output).

---

## §1. Phase A — Theoretical Pre-Analysis (carry from `op_resolution.md` §11.3)

### §1.1 ε's role in l1i

ε determines the active set $A^\varepsilon = \{j : \|u^{(j)}\|_1 > \varepsilon\}$ when state_mode = `wq1` (per `l1i_constants_feasibility.py` line 279: `A = [j for j, m in enumerate(masses) if m > epsilon]`). For state_mode = `raw_gaussian`, the active set is ε-independent (line 281: `A = [j for j in range(K) if initial_masses[j] > 0]`).

### §1.2 Predicted f(ε) for wq1 state_mode

For `initial_masses = (30, 30, 30, 0)` under wq1 mass-projection:
- ε ∈ (0, 30): n_active = 3 (3 active slots, 1 inactive) → identical active set across ε → identical feasibility chain → identical FEASIBLE_WITH_BUDGET count.
- ε ≥ 30: n_active = 0 → all configs INCONCLUSIVE.

**Predicted f^{wq1}(ε)** = piecewise-constant: $c$ on (0, 30); 0 on [30, ∞).

### §1.3 Predicted f(ε) for raw_gaussian state_mode

raw_gaussian active set is determined by `initial_mass > 0`, NOT by ε threshold. Therefore f^{raw_gaussian}(ε) is **structurally ε-independent**: constant in ε across the entire (0, ∞) range. *(This was implicit in §11.3 but not made explicit; Phase B surfaces it.)*

### §1.4 Total f(ε) on the 1920-config baseline

The baseline 1920 configs comprise 960 wq1 + 960 raw_gaussian (verified `Counter(c.state_mode for c in make_full_sweep()) = {'wq1': 960, 'raw_gaussian': 960}`). Therefore:

$$
f(\varepsilon) = \frac{f^{\mathrm{wq1}}(\varepsilon) \cdot 960 + f^{\mathrm{raw\_gaussian}} \cdot 960}{1920} = \frac{f^{\mathrm{wq1}}(\varepsilon) + f^{\mathrm{raw\_gaussian}}}{2}.
$$

So total f(ε) is **piecewise-constant only in the wq1 component**; the raw_gaussian component is constant.

---

## §2. Phase B — Numerical Execution (14-ε sweep × 1920 configs)

### §2.1 Wrapper script

Created `CODE/scripts/op_resolution_nq_g3_1_epsilon_stability.py` (~6 KB; imports `compute_feasibility`, `make_full_sweep`, `aggregate_results`, `feas_result_to_dict` from `l1i_constants_feasibility`). The wrapper iterates ε over a 14-value grid covering below-baseline / baseline / interior / boundary-transition / above-boundary regimes, calls `compute_feasibility` per config per ε (no JSON post-processing because changing ε changes the active set, which changes the entire feasibility chain — distinct from NQ-G1-2's budget post-processing).

### §2.2 Sweep grid

ε ∈ {0.001, 0.05, 0.10, 0.15, **0.225 (baseline)**, 0.30, 0.50, 1.0, 5.0, 25.0, 29.99, 30.0, 30.01, 35.0}.

### §2.3 Results

| ε | n_active distribution | FEASIBLE_WITH_BUDGET | f(ε) | Wall (s) |
|---:|---|---:|---:|---:|
| 0.001 | {3: 1920} | 439 / 1920 | 22.86% | 14.4 |
| 0.05 | {3: 1920} | 439 / 1920 | 22.86% | 14.4 |
| 0.10 | {3: 1920} | 439 / 1920 | 22.86% | 14.6 |
| 0.15 | {3: 1920} | 439 / 1920 | 22.86% | 14.6 |
| **0.225 (baseline)** | {3: 1920} | **439 / 1920** | **22.86%** | 14.6 |
| 0.30 | {3: 1920} | 439 / 1920 | 22.86% | 14.6 |
| 0.50 | {3: 1920} | 439 / 1920 | 22.86% | 14.6 |
| 1.0 | {3: 1920} | 439 / 1920 | 22.86% | 14.6 |
| 5.0 | {3: 1920} | 439 / 1920 | 22.86% | 14.6 |
| 25.0 | {3: 1920} | 439 / 1920 | 22.86% | 14.6 |
| 29.99 | {3: 1920} | 439 / 1920 | 22.86% | 14.6 |
| **30.0** | {3: 1280, 1: 240, 0: 400} | **404 / 1920** | **21.04%** | 11.1 |
| 30.01 | {0: 960, 3: 960} | 389 / 1920 | 20.26% | 8.8 |
| 35.0 | {0: 960, 3: 960} | 389 / 1920 | 20.26% | 8.8 |

**Total wall-clock: 188.9s** (14 ε × ~14.6s including a transition-region speedup as more configs short-circuit on n_active=0).

Output JSON: `CODE/scripts/results/op_resolution_nq_g3_1_epsilon_stability.json`.

### §2.4 Baseline decomposition (independent verification)

Re-classifying the existing baseline `l1i_constants_feasibility.json` (ε = 0.225) by state_mode (using `make_full_sweep()` ordering):
- **raw_gaussian (960 configs)**: 389 FEASIBLE_WITH_BUDGET / 148 RAW_FEASIBLE / 416 INFEASIBLE / 7 MARGINAL.
- **wq1 (960 configs)**: 50 FEASIBLE_WITH_BUDGET / 80 RAW_FEASIBLE / 817 INFEASIBLE / 13 MARGINAL.

**Total FEASIBLE_WITH_BUDGET: 389 + 50 = 439 ✓** (matches baseline anchor).

This decomposition is the key to interpreting §2.3:
- **At any ε ∈ (0, 30):** wq1 contributes 50; raw_gaussian contributes 389; total = 439 ✓.
- **At ε ≥ 30:** wq1 contributes 0 (all n_active=0); raw_gaussian contributes 389 (structurally ε-independent); total = 389 ✓.
- **At ε = 30.0 (boundary):** partial wq1 transition (240 configs with n_active=1, 400 with n_active=0, 320 with n_active=3 due to numerical mass variance around 30); wq1 contributes 15 (= 404 - 389); raw_gaussian contributes 389; total = 404.

The boundary spread at ε=30 (29.99 → 30.0 → 30.01: wq1 FEASIBLE goes 50 → 15 → 0) is consistent with sub-percent numerical variance in wq1's `build_initial_state` post-projection masses around the nominal 30.

---

## §3. Findings

### §3.1 Below-30 prediction CONFIRMED (load-bearing finding)

**f(ε) is piecewise-constant on ε ∈ (0, 30) at 439/1920 = 22.86%**, exactly as predicted by `op_resolution.md` §11.3. This holds across **11 sampled ε values** spanning 4 orders of magnitude (0.001 → 25.0): no variation observed.

This is the **load-bearing finding for T-L1-F's empirical anchor**: the 439/1920 = 22.9% feasibility claim is empirically stable under ε perturbations within the production regime. The W6 strategic plan G3 finding "production scripts use ε = 0.225 = 0.01·m̄ for $\bar m = M / K_{\mathrm{field}} = 90/4 = 22.5$" is now empirically anchored as **regime-stable**: any production ε in (0, 30) gives the same FEASIBLE_WITH_BUDGET count.

### §3.2 Above-30 prediction PARTIALLY CONFIRMED (with structural reason)

For ε ≥ 30, the predicted "drops to 0" applies **only to the wq1 state_mode component**. The raw_gaussian state_mode component remains constant at 389/960 = 40.5% feasibility because raw_gaussian active-set is determined by `initial_mass > 0` (line 281 of l1i), not by post-projection mass > ε.

**This is by-design dual state_mode behavior**, not a deviation from theory. The §11.3 pre-analysis implicitly assumed wq1 only; Phase B surfaces the dichotomy.

### §3.3 At-30 boundary transition spread

The numerical transition is spread across ε ∈ {29.99, 30.0, 30.01}:
- ε = 29.99: 50 wq1 FEASIBLE_WITH_BUDGET (full).
- ε = 30.0: 15 wq1 FEASIBLE_WITH_BUDGET (partial; 240 configs at n_active=1, 320 at n_active=3 due to wq1 build numerical variance around 30).
- ε = 30.01: 0 wq1 FEASIBLE_WITH_BUDGET (all configs at n_active=0).

The spread is consistent with the wq1 mass-projection introducing sub-percent numerical variance in the post-projection masses around the nominal 30. This is **not a structural feature** of the SCC theory — it's an artifact of how `build_initial_state` constructs fields.

### §3.4 Total f(ε) profile

Plotting f(ε) on the 1920-config baseline: **monotonically non-increasing piecewise-constant in three steps**:
- ε ∈ (0, 30): f = 22.86% (439/1920).
- ε = 30: f = 21.04% (404/1920) — narrow boundary transition.
- ε ≥ 30: f = 20.26% (389/1920) — raw_gaussian-only regime.

The drop from 22.86% to 20.26% over the boundary transition (~0.01 wide) is 50/1920 = 2.6 percentage points. **Below 30, stability is exact.** This is the production-relevant finding.

---

## §4. Implication for T-L1-F Empirical Anchor + Commitment 16

### §4.1 T-L1-F empirical anchor (CV-1.5.2)

T-L1-F's "439/1920 = 22.9% feasible on $T^2_{20}$" empirical claim is the **load-bearing non-vacuity demonstration** for the L1-J regime $(P0)$–$(P11)$. This claim assumes ε = 0.225 (per Commitment 16, R1 reading $\bar m = M/K_{\mathrm{field}}$).

**Phase B confirms:** the 22.9% number is **stable across any ε ∈ (0, 30)**. T-L1-F's empirical anchor does NOT depend sensitively on the precise ε choice within the production regime. This sharpens the Cat A conditional status of T-L1-F (and by inheritance T-L1-M): the regime is structurally robust to small ε perturbations.

### §4.2 Commitment 16 ε-convention (CV-1.5.2 amendment per G3 deep-dive)

The G3 deep-dive (W6 D1 mid-day, R1 reading $\bar m = M/K_{\mathrm{field}}$) made ε = 0.01·M/K_field explicit in Commitment 16 line 810. NQ-G3-1's ε-stability finding **strengthens** this convention: any reasonable ε in (0, 30) gives the same regime characterization, so the 0.225 default is one of many equivalent choices. The convention ratchets up from "default" to "robust default" — but no canonical edit is required (the existing ε = 0.01·m̄ convention already achieves this).

### §4.3 No theorem-level claim modification

NQ-G3-1's empirical confirmation is **regime characterization**, not theorem modification. T-L1-F Cat A conditional status: **unchanged**. T-L1-M Cat A conditional status: **unchanged**. (P0)–(P11) regime hypothesis package: **unchanged**.

---

## §5. NQ-G3-1 Closure Verdict

**✅ EXECUTED** (W6 D2 G2.3 fill-in; ~30 min wrapper authoring + 188.9s wall-clock + ~30 min finding documentation).

**Empirical verdict per `plan.md` §G2.3 success criterion:** "NQ-G3-1 ✅ EXECUTED with prediction confirmed (or deviation documented)."
- **Prediction confirmed for wq1 state_mode** (the production-relevant mode): piecewise-constant on (0, 30); drops to 0 at ε = 30.
- **Deviation documented**: raw_gaussian state_mode is structurally ε-independent (by-design), so f(ε ≥ 30) does NOT drop to 0 on the full 1920-config baseline; it drops to the raw_gaussian-only floor of 389/1920 = 20.26%.
- **Boundary transition spread** at ε = 30 is consistent with sub-percent numerical variance in wq1 build_initial_state.

**Status update target (per `plan.md` §G2.3 success criterion):** `op_resolution.md` §0 row 10 + §11.5 + §11.6 + §13.1 row 10 + §13.4 item 4 — all need updating from `📋 DEFERRED` → `✅ EXECUTED W6 D2 (this session)`. Erratum proposals in §6 below; updates to be applied in same supervised-edit pass as the closure-rigor §7.1 erratum proposal.

---

## §6. New Open Question Surfaced

### NQ-G3-1-ext (Low priority, W7+) — wq1 build_initial_state mass-preservation precision

**Question.** Phase B revealed that `wq1.build_initial_state(rc, list(centers), positions)` produces post-projection masses with sub-percent variance around the nominal `initial_masses` value — at ε = 30 (boundary), 240 of 960 wq1 configs have exactly 1 slot mass > 30 and 400 have all masses ≤ 30 (i.e., the actual masses cluster within ~0.01 of 30 for most configs but not all). Does the wq1 mass projection enforce `‖u^j‖_1 = m_j` exactly, or does it permit small deviations under the simplex constraint $\sum_j u^j(x) \le 1$?

**Severity.** Low. Does not affect any canonical claim or T-L1-F/T-L1-M Cat A conditional status. Production ε regime (0.05 – 1.0) is far from the 30-boundary, so this nuance is purely a boundary-precision question.

**Connection.** Inspect `CODE/scc/wq1.py` `build_initial_state` for the mass-projection algorithm (clipping vs. exact rescaling); compare to the simplex-feasibility of the resulting fields. Estimated effort ~30 min reading + ~30 min targeted experiment if a precise behavior is needed. **NOT a CV-1.6 release blocker.**

### Other NQs not surfaced

No new theorem-level open questions. The empirical anchor stability finding (§3.1) is positive (closure-style), not generative of new questions at the theory level.

---

## §7. Hard-Constraint Sweep

Per `plan.md` §7 hard-constraint sweep target (this Day 2 G2.3 fill-in session):

- [x] **canonical.md / theorem_status.md / scc/**: 0 edits. T-L1-F / T-L1-M Cat A conditional status: unchanged. Tests not re-run (0 scc/ edits; baseline 215 passed + 1 xfailed verified W6 D1 EOD).
- [x] **working/MF/**: 0 edits.
- [x] **THEORY/logs/daily/2026-05-04/op_resolution.md**: 0 edits THIS session (status row updates queued for user-supervised application alongside §7.1 erratum proposal from `01_closure_rigor_audit.md`). Out-of-session writeup queue documented in §5 above.
- [x] **CODE/scripts/**: 1 NEW file (`op_resolution_nq_g3_1_epsilon_stability.py`); 0 modifications to existing scripts. Pattern matches NQ-G1-2 wrapper precedent (CHANGELOG 13th addendum).
- [x] **CODE/scripts/results/**: 1 NEW JSON output (`op_resolution_nq_g3_1_epsilon_stability.json`).
- [x] **Silent OP resolution**: 0. NQ-G3-1 was a deferred-numerical NQ; closure does NOT affect any OP catalog row. T-L1-F / T-L1-M Cat A conditional status preserved.
- [x] **N-1 / CN5 / CN6 / CN7 / CN10 / CN15 / u_t primitive**: all preserved.
- [x] **No Research OS resurrection.** No numbered directories or 5-role daily logs. File-naming follows `plan.md` §8 spec (`03_nq_g3_1_epsilon_stability.md`).
- [x] **No OMC pool / external agent dispatch.** Single-thread.
- [x] **No external framework reduction.** No Yang-Mills / OT / clustering reductive claim made.
- [x] **No metastability claim w/o P-F flag.**

**All 11 hard-constraint items ✓ satisfied.**

---

## §8. CHANGELOG entry proposal (W6 D2 NQ-G3-1 EXECUTED)

For user to apply at Day 2 EOD wrap-up — proposal text:

```markdown
## 2026-05-05 (W6 Day 2 EOD) — NQ-G3-1 EXECUTED (Silver target met): ε-stability sweep of 439/1920 anchor confirms §11.3 piecewise-constant prediction for wq1 mode + reveals raw_gaussian ε-independence

**Trigger:** plan.md §G2.3 fill-in after G2.2 Decision Point 4 = Option B captured. NQ-G3-1 was the only remaining 📋 DEFERRED row in op_resolution.md §13.1 from W6 D1 batch.

### What was done
- Created CODE/scripts/op_resolution_nq_g3_1_epsilon_stability.py wrapper (~6 KB; imports compute_feasibility, make_full_sweep from l1i_constants_feasibility).
- Sweep ε ∈ {0.001, 0.05, 0.10, 0.15, 0.225 baseline, 0.30, 0.50, 1.0, 5.0, 25.0, 29.99, 30.0, 30.01, 35.0} × 1920 configs = 26,880 total runs.
- Wall-clock: 188.9s.
- Output: CODE/scripts/results/op_resolution_nq_g3_1_epsilon_stability.json.

### Findings
- f(ε) = 439/1920 (constant) for ε ∈ (0, 30) — confirms §11.3 piecewise-constant prediction. 11 sampled ε values across 4 orders of magnitude (0.001 → 25.0): zero variation.
- f(ε) drops to 389/1920 (constant) for ε ≥ 30 — raw_gaussian state_mode (960 of 1920 configs) is structurally ε-independent (active set determined by initial_mass > 0, not post-projection mass > ε).
- Boundary transition at ε = 30 is spread across ~0.01 ε-window: f(29.99)=22.86%, f(30.0)=21.04%, f(30.01)=20.26%. Spread reflects sub-percent numerical variance in wq1 build_initial_state.
- Baseline 439 decomposes as 50 wq1 + 389 raw_gaussian (independently verified).

### T-L1-F empirical anchor implication
22.9% feasibility claim is robust under ε perturbations within the production regime (0.05 – 1.0); the 0.225 default is one of many equivalent choices. T-L1-F / T-L1-M Cat A conditional status: unchanged.

### Hard-constraint sweep
- canonical.md / theorem_status.md / scc/ / working/MF/: 0 edits.
- THEORY/logs/daily/2026-05-04/op_resolution.md: status row updates queued for supervised application (§5 of 03_nq_g3_1_epsilon_stability.md).
- CODE/scripts/: 1 new wrapper + 1 new JSON output. No edits to l1i_constants_feasibility.py.
- N-1 hard constraint: 0 silent OP resolution.

### Files modified / created
1. CODE/scripts/op_resolution_nq_g3_1_epsilon_stability.py (NEW)
2. CODE/scripts/results/op_resolution_nq_g3_1_epsilon_stability.json (NEW)
3. THEORY/logs/daily/2026-05-05/03_nq_g3_1_epsilon_stability.md (NEW)

### NQ-G3-1-ext (W7+ low priority)
wq1 build_initial_state mass-preservation precision: at ε = 30 (boundary), 240 wq1 configs have 1 active slot and 400 have 0 active, indicating sub-percent variance around nominal mass 30. Investigate whether mass projection is exact rescaling vs. simplex-constrained clipping. Not a CV-1.6 blocker.

### Lesson logged
A cheap (~30 min wrapper) numerical sweep can simultaneously (a) confirm a theoretical prediction and (b) surface a deeper structural distinction (here: dual state_mode dichotomy, where wq1 is ε-dependent and raw_gaussian is ε-independent by design). Pattern reaffirms: even when §11.3-style theoretical pre-analysis suggests a "trivial" outcome, the actual sweep can produce a non-trivial finding — but in the load-bearing direction (the production regime is robust). Run the sweep cheaply rather than relying on theoretical pre-analysis alone.
```

---

**End of `03_nq_g3_1_epsilon_stability.md`. NQ-G3-1 ✅ EXECUTED. Last 📋 DEFERRED row from W6 D1 op_resolution.md §13.1 closed. Silver target ✅ MET. T-L1-F empirical anchor 22.9% robustness confirmed across production-regime ε. raw_gaussian state_mode ε-independence revealed as new structural finding (low-priority NQ-G3-1-ext W7+). Tests preserved (215 passed + 1 xfailed). Hard-constraint sweep 11/11 ✓.**
