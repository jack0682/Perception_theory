# 04_nq174_setup.md — G2 NQ-174 ζ_*(graph) Precise Script Setup (Day 2 Morning Run)

**Session:** 2026-04-27 (W5 Day 1, G2 Block 5)
**Target (from plan.md §3 Block 5 21:30-22:00):** NQ-174 ζ_*(graph) precise script ready for Day 2 09:00 run.
**This file covers:** Script overview, sweep design, expected runtime, Day 2 execution checklist.
**Depends on reading:** `04-26/04_NQ170c_graph_extension_nodal.md` §2.1 + §2.3 (V5b-T crossover bracketing); W5 strategic plan §0.3 G2; `CODE/scripts/nq174_zeta_star_precise.py` (this session's script).
**Status:** Script written + syntax + import verified. Day 2 morning execution ready.

---

## §1. Question

W4-04-26 NQ-170c bracketed:
- ζ_*(2D torus L=20) ∈ **[0.2, 0.5]** (overlap 0.49 at 0.2 vs 0.97 at 0.5).
- ζ_*(1D cycle L=40) **< 0.2** (overlap 0.76 at 0.2 already super-lattice).

This bracketing is *3-decimal precision insufficient* for canonical statement of the V5b-T crossover. NQ-174 narrows.

**Question (NQ-174):** What is ζ_* (V5b-T sub/super-lattice crossover) to 2-decimal precision on:
- 2D torus L=20
- 1D cycle L=40

---

## §2. Sweep Design

### 2D torus L=20

ζ ∈ {0.25, 0.30, 0.35, 0.40, 0.45} × N=5 seeds = **25 minimizers**.

Bracket coverage: fills the [0.2, 0.5] gap with 5 points at 0.05 resolution.

**Crossover detection:** smallest ζ where mean(max_overlap across 5 seeds) > 0.9.

### 1D cycle L=40

ζ ∈ {0.05, 0.10, 0.15} × N=5 seeds = **15 minimizers**.

Bracket coverage: NQ-170c showed super-lattice at ζ=0.2 already; need finer resolution below to find true crossover. Minimum ζ=0.05 chosen for $\xi_0 = 0.05a$ (very thin interface; sub-lattice extreme).

**Total:** 25 + 15 = **40 minimizers** across two graph classes.

---

## §3. Mode-Agnostic Detection (from W4-04-26 NQ-172 Lesson)

The script (`analyze_minimizer` function) iterates over **all 6 lowest non-tangent eigenmodes** and records the maximum mode-agnostic Goldstone overlap (vs translation modes per axis). **No** hardcoded mode index (e.g., `mode_overlaps[1]`).

This was the critical lesson from W4-04-26 NQ-172: NQ-170 morning's reproducibility crisis was caused by the analysis script hardcoding `mode_overlaps[1]` while the Goldstone could appear at mode 0, 5, or any other index. Mode-agnostic detection resolves this.

---

## §4. Multi-IC Strategy (from NQ-170c reuse)

For each (ζ, seed) attempt:
- 3 IC widths: $\xi_0$, $\xi_0/2$, $\xi_0 \cdot 2$.
- IC center randomized within [0.5, L-0.5] (avoid exact lattice positions).
- Best F=1 minimizer (lowest energy) selected per (ζ, seed) tuple.

This strategy improves F=1 success rate from ~40-60% to >90% per (ζ, seed) per NQ-170c.

---

## §5. Expected Runtime

Per minimizer attempt (3 IC × find_formation + Hessian + mode analysis): ~30-50s on standard CPU.

Total: 40 minimizer attempts × ~40s ≈ **27 minutes**.

For 2D torus alone: 25 × 40s ≈ 17 min.
For 1D cycle alone: 15 × 25s ≈ 6 min (smaller n).

---

## §6. Day 2 Execution Checklist

**08:55 (PRE-RUN sanity test, recommended per `91_critical_review.md` §6.G):** Verify scc API matches script assumptions before launching long-running sweep:
```bash
cd /Users/ojaehong/Perception/Perception_theory/CODE
python3 -c "
from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation
import scipy.sparse as sp
import numpy as np
n = 16
rows = list(range(n-1)) + list(range(1, n))
cols = list(range(1, n)) + list(range(n-1))
g = GraphState(sp.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(n, n)))
p = ParameterRegistry(alpha_bd=1.0, beta_bd=4.0, volume_fraction=0.1, a_cl=3.5, a_D=5.0, lambda_D=1.0, b_D=0.0, w_cl=0.0, w_sep=0.0, w_bd=1.0, n_restarts=1, max_iter=100)
res = find_formation(g, p, normalize=False, verbose=False, u_init=np.full(n, 0.1))
print('OK', res.converged, res.energy)
"
```
Expected: `OK True <number>`. If errors (e.g., `find_formation()` doesn't accept `normalize=`, or `ParameterRegistry` missing field), fix script kwargs before sweep.

**09:00:** Start NQ-174 sweep:
```bash
cd /Users/ojaehong/Perception/Perception_theory/CODE
python3 scripts/nq174_zeta_star_precise.py
```

**09:30 (estimated):** Sweep complete. Inspect output:
```bash
cat scripts/results/nq174_zeta_star.json | head -100
```

**Then:**
1. Extract per-(ζ, seed) overlap from JSON.
2. Compute per-ζ mean overlap.
3. Find ζ_* (smallest ζ where mean > 0.9) per graph class.
4. Compare to W4-04-26 NQ-170c brackets — does ζ_*(2D torus) fall in [0.2, 0.5]? Does ζ_*(1D cycle) fall below 0.2 confirmed?
5. Write Day 2 analysis file `01_NQ174_zeta_star_results.md`.
6. Determine canonical impact: T-V5b-T-(d) entry's ζ_*(G) line currently states bracketed values only — NQ-174 result enables 2-decimal precision update.

---

## §7. Canonical Impact (post-NQ-174, Day 2+)

T-V5b-T entry §13 line 1129 currently:
> $\zeta_*(2D \text{ torus}) \in [0.2, 0.5]$ (bracketed by $\zeta=0.2$ overlap 0.49, $\zeta=0.5$ overlap 0.97).
> $\zeta_*(1D \text{ cycle}) < 0.2$ (sub-lattice overlap already 0.76 at $\zeta=0.2$).

**Post-NQ-174 expected update:**
> $\zeta_*(2D \text{ torus L=20}) \approx [\text{measured value, e.g., 0.35}]$ (NQ-174 W5 Day 2).
> $\zeta_*(1D \text{ cycle L=40}) \approx [\text{measured value, e.g., 0.10}]$ (NQ-174 W5 Day 2).

**Cat A target:** quantitative ζ_* values registered in canonical with experimental support.

**Out of NQ-174 scope (W6+ candidate):** ζ_*(graph) as analytic function of dimensionality d and graph topology — would advance to closed-form derivation. NQ-175 V5b 3D extension may inform this.

---

## §8. Plan.md Block 5 Status

Per plan.md §3 Block 5:
- [x] 21:30-22:00 (30min): G2 NQ-174 script `nq174_zeta_star_precise.py` written. ✓ Written.
- [x] 22:00-22:30 (30min): Day 1 review + W5 weekly_draft 04-27 entry. → Next file: `99_summary.md`.

**Plan.md §6 hard constraint:** "G2 NQ-174 script ready for Day 2 09:00 run." → ✓ Met.

**Status:** Script + setup notes ready. Day 2 morning user runs script + writes Day 2 analysis.

---

**End of 04_nq174_setup.md.**
