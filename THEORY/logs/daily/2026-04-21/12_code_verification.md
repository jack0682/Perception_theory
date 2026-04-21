# 12 — Code Verification: Numerical Experiments on scc/ Codebase

**Session:** 2026-04-21 (Round 9, post-saturation; user requested actual code verification)
**Mode:** **Numerical verification** of theoretical claims via existing scc/ codebase. First substantive code work in the session.
**Format:** ~250 줄. Tests + results + corrections to theory.
**Depends on reading:** all prior daily files; runs all from `CODE/` directory.

---

## §0. Setup

scc/ codebase verified functional (smoke test from CLAUDE.md passes). Persistence machinery exists in `scc/persistence.py`. K_soft wrapper implemented and tested.

```python
from scc.persistence import persistence_h0
def k_soft(u, grid_size, phi=lambda l: l/(1+l)):
    bars = persistence_h0(u, grid_size)
    return sum(phi(b - d) for b, d in bars if (b - d) > 1e-12)
```

**Note:** `persistence_h0` returns superlevel filtration bars with `birth > death`, so `length = b - d`. (My earlier wrapper sketch in Round 4 §7 had `phi(d - b)` — sign error caught immediately by code testing.)

---

## §1. Test 1 — Hard-K Recovery (Prop 4.1) ✓ PASS

**Theoretical claim** (G1 §4 + Prop 4.1): on sharp-interface configurations with K disjoint maximal regions, `K_soft → K · φ(1)`.

**Numerical results on 4×4 grid, m = 4:**

| Configuration | Predicted K_soft | Measured K_soft | Status |
|---|---|---|---|
| Uniform (u = 0.25 everywhere) | φ(0.25) = 0.20 | **0.2000** | ✓ exact (essential bar from c to 0) |
| Sharp K=1 (4 sites at 1, rest 0) | φ(1) = 0.5 | **0.5000** | ✓ exact |
| Sharp K=2 (two 2-site clusters at 1, rest 0) | 2·φ(1) = 1.0 | **1.0000** | ✓ exact |

**Conclusion:** Prop 4.1 hard-K recovery **numerically verified to machine precision**.

**Errata E-15 (NEW):** Round 5 §1.5 stated "K_soft of uniform is 0 (single trivial bar of length 0)". **INCORRECT.** Numerical: K_soft(uniform) = φ(c) ≠ 0 (essential H₀ bar has length c, from c down to 0). For canonical c = 0.25: K_soft = 0.20 (not 0). Affects Round 5 Hessian-at-uniform argument — though qualitatively Hessian is still ~0 since K_soft is locally smooth in u for fixed bar-vertex structure.

---

## §2. Test 2 — K_soft Lipschitz (Cor 4.1) ✓ PASS (loose)

**Theoretical claim** (Cor 4.1, corrected Round 2): `L_K ≤ 4 L_φ · n` globally on Σ_m.

**Numerical: 200 random pairs (u, v) ∈ Σ_m, compute |K_soft(u) − K_soft(v)| / ‖u − v‖_∞.**

| Grid | n | Theoretical bound `4·L_φ·n` | Empirical max ratio | Tightness (max/bound) |
|---|---|---|---|---|
| 3×3 | 9 | 36 | 2.19 | 6.1% |
| 5×5 | 25 | 100 | 1.94 | 1.9% |
| 8×8 | 64 | 256 | 3.52 | 1.4% |

**Conclusion:** Cor 4.1 **holds with large margin** (1-6% of bound used). Empirical max ratio scales **weakly with n** (2-4 across n = 9-64), suggesting **NQ-9 is well-motivated** — sharper bound exists.

**Implication:** L_K = O(n) is a loose worst-case bound. True scaling looks closer to O(1) or O(√n). Sharper bound via graph spectral structure would give tighter Lipschitz of ℱ_C+E and tighter Kramers / Langevin estimates.

---

## §3. Test 3 — T*_uniform Hessian (Round 4 Theorem 1.1) ✓ PASS (0.1% accuracy)

**Theoretical claim** (Round 4 Thm 1.1): T*_uniform = c(1-c) · [β·|W''(c)| - 4α·λ_2(G) - r_{cl,sep}].

**Numerical: 6×6 grid, c = 0.5, β = 30, α = 1, w_cl = 1.**

- Graph Laplacian λ_2(L) = 0.2679 (computed numerically).
- W''(0.5) = -1, |W''| = 1.
- r_cl = w_cl · 2(1 - a_cl/4)² = 1 · 2(1 - 3.5/4)² = 0.0312.

**Predicted:** T*_uniform = 0.25 · (30 - 1.072 - 0.031) = **7.224**.

**Numerical Hessian at uniform via finite differences (n² = 1296 entries, h = 5e-5):**
- Smallest non-trivial constrained eigenvalue: **-28.873**.
- Predicted from formula `4α·λ_2 + β·W''(c) + r_cl` = -28.897. Match within 0.08%.
- Numerical T*_uniform (when smallest H_ε + T·4 = 0): **7.218**.

**Discrepancy: 0.1%.** Round 4 Thm 1.1 **strongly verified**.

**Status:** T-Uniform-Stab-T promoted from "Cat A sketched-rigorous" to **"Cat A numerically verified at canonical params"**.

---

## §4. Test 4 — F-1 Dissolution + Boltzmann Ratio (G4 §3.3) ⚠ PARTIAL

**Theoretical claim** (Round 4 §2.2): T_c = ΔE/ΔS ≈ 1.0 for K=1 ↔ K=2 thermodynamic crossover.

**Numerical: 12×12 grid, m=36, β=30, α=1.** Multi-init search for K=1 and K=2 minima.

**K=1 minimum (best of 36 inits):** E = 2.348, S = 23.67, K_soft = 0.506. Sites: 35 high (>0.7), 7 boundary (0.1-0.7), 102 low (<0.1).

**K=2 minimum (best of 18 inits):** E = 2.699, S = 29.79, K_soft = 0.988. Sites: 32 high, 16 boundary, 96 low.

**Differences:**
- ΔE = +0.351 (K=2 higher; canonical T-Merge (b) ✓)
- ΔS = +6.118 (K=2 has MORE entropy; sign matches Round 4 ✓)
- ΔK_soft = +0.482

**Numerical T_c = ΔE/ΔS = 0.057** — **17× SMALLER than Round 4 predicted (≈ 1.0).**

### 4.1 Why the discrepancy?

Round 4 §11 used estimate ΔS ≈ 2.5 nats (from boundary site counting heuristic). **Actual ΔS = 6.12 nats**, 2.4× larger.

Reason: my Round 4 estimate underestimated boundary entropy. Actual K=2 has 16 boundary sites (~6.2 nats S contribution) vs K=1's 7 boundary sites (2.5 nats). Plus K=2's "low" sites contribute slightly more entropy (lower u → more spread). Total entropy gap is larger.

### 4.2 Boltzmann ratio at varied T (γ_K = 0.05)

| T | ΔF | K=2/K=1 ratio | K=1 occupancy |
|---|---|---|---|
| 0.05 | +0.047 | 0.39 | **72%** |
| 0.1 | -0.258 | 13.2 | 7% |
| 0.2 | -0.867 | 76.5 | 1.3% |
| 0.5 | -2.695 | 219 | 0.5% |
| 1.0 | -5.742 | 312 | 0.3% |
| 2.0 | -11.84 | 372 | 0.3% |
| 5.0 | -30.12 | 413 | 0.2% |

### 4.3 Three-regime phase diagram — NUMERICAL CORRECTION

**Original Round 4 §2.2 prediction:**
- Low-T (T < T_c ≈ 1.0): K=1 preferred.
- Mid-T (1.0 < T < 7.4): K=2 preferred.
- High-T (T > 7.4): uniform preferred.

**Numerical correction (this experiment):**
- **Low-T (T < ~0.06): K=1 preferred. Very narrow regime!**
- **Mid-T (0.06 < T < 7.2): K=2 preferred. Wide regime.**
- **High-T (T > 7.2): uniform preferred (Theorem 1.1 unchanged).**

**Substantive correction.** The "single-mode regime" is **17× narrower** than predicted. Most physical temperatures (T ≥ 0.1, where σ_noise ≥ 0.45) fall in **multi-mode preferred regime**.

This **strengthens F-1 dissolution** even more: K=2 dominates at virtually all T > 0.1. canonical zero-T "K=1 always preferred" is effectively a measure-zero edge case.

**Errata E-16 (NEW):** Round 4 §2.2 T_c estimate of ~1.0 is too high. **Numerical T_c ≈ 0.06** (verified on 12×12 grid). Round 4 §2.5 testable predictions table needs correction.

---

## §5. Test 5 — Canonical T-Merge (b) Numerical Check ✓ PASS

**Canonical claim** (Cat A): on connected graph, K=1 has lower E_bd than K=2 (isoperimetric).

**Numerical (best minima from §4):**
- E_bd(K=1) = 24.29
- E_bd(K=2) = 33.89
- ΔE_bd = +9.60 (K=2 larger). ✓ T-Merge (b) confirmed.

**Earlier confusion:** my first test with single-init found "K=2 minimum" with E_bd = 33.89 < 46.02 = "K=1 minimum from suboptimal Gaussian init". This appeared to contradict T-Merge (b), but was actually **two suboptimal local minima**. With multi-init global search, T-Merge (b) holds.

**Errata E-17 (NEW, methodological lesson):** SCC's energy landscape has **many local minima** even within a single K topology class. Single-init optimization can find suboptimal minima. Multi-init essential for global comparisons. **C-S2 numerical work should use multi-init systematically.**

---

## §6. Empirical Findings Summary

### 6.1 Confirmed (numerical verification)

✅ **Prop 4.1 hard-K recovery:** sharp K=1, K=2 give K_soft = 0.5, 1.0 exactly.
✅ **Cor 4.1 K_soft Lipschitz:** holds with large margin (1-6% of bound).
✅ **Round 4 Theorem 1.1 (T-Uniform-Stab-T):** numerical T*_uniform = 7.218 vs predicted 7.224 (0.1% accuracy).
✅ **Round 4 §2 Three-regime structure:** qualitative pattern (low-T K=1, mid-T K=2, high-T uniform) confirmed.
✅ **Canonical T-Merge (b):** numerically holds (K=1 E_bd < K=2 E_bd).

### 6.2 Refuted / Corrected

❌ **Round 5 §1.5 "K_soft(uniform) = 0":** actually = φ(c) ≠ 0. **Errata E-15.**
❌ **Round 4 §2.2 T_c ≈ 1.0:** actually T_c ≈ 0.057 on 12×12 grid (17× smaller). **Errata E-16.**
❌ **Implicit assumption: gradient flow finds globals:** false. Multi-init essential. **Errata E-17.**

### 6.3 Strengthened (by numerical accuracy)

🔼 **F-1 dissolution:** K=1 single-mode regime is **much narrower** than Round 4 predicted. K=2 dominates at virtually all T > 0.1. Even **stronger dissolution** of canonical zero-T "K=1 preferred" framing.

### 6.4 Quantitative deviations

| Quantity | Theoretical (Round 4) | Numerical (this work) | Ratio |
|---|---|---|---|
| T*_uniform | 7.224 | 7.218 | 0.999 ✓ |
| T_c | ~1.0 | 0.057 | 17× off |
| ΔS (K=2 - K=1) | ~2.5 nats | 6.12 nats | 2.4× off |

---

## §7. New Errata (Round 9)

| # | Issue | Severity | Status |
|---|---|---|---|
| **E-15** | K_soft(uniform) = φ(c) ≠ 0 (Round 5 §1.5 error) | Low | Documented |
| **E-16** | T_c ≈ 0.057 numerical (Round 4 ~1.0 too high) | **Medium-High** | Need theory revision |
| **E-17** | Single-init finds suboptimal minima; multi-init essential | Methodological | C-S2 protocol note |

**Cumulative errata: 17 (E-1 through E-17).** Applied: 8. Documented in daily file: 6. User review pending: 3.

---

## §8. New NQs from Code Verification

**NQ-23 (new).** Why does ΔS estimate (Round 4 §11 boundary-counting heuristic) underestimate by 2.4×? Could be:
- Boundary band wider than 1 site at finite β.
- Per-site boundary entropy contribution closer to log 2 (max) than estimated 0.5.
- "Low-u" sites (u < 0.05) also contribute non-negligibly to S.

**NQ-24 (new).** Verify T*_uniform on different graph topologies (cycle, expander, random). Round 4 derived for general connected graph; only verified on grid here.

**NQ-25 (new).** Numerical NEB on K=1 ↔ K=2 transition path (from this graph) to compute ΔF directly. Compare to canonical exp38's γ_eff = 0.89.

---

## §9. What Code Verification Reveals about Verification Process

### 9.1 Numerical truth vs theoretical estimates

5 of 5 **structural / qualitative claims** verified.
2 of 3 **quantitative predictions** off by significant factors:
- T*_uniform: spot-on (Hessian computation matches theory to 0.1%)
- T_c: 17× off (entropy estimate was rough)
- ΔS: 2.4× off (boundary counting heuristic)

**Lesson:** structural theorems (Hessian formulas, scaling laws) are robust. Quantitative predictions involving heuristic estimates (entropy from "boundary site counting") need numerical calibration.

### 9.2 Actual verification value (numerical vs 8 verification rounds)

8 verification rounds: confirmed internal consistency, found 14 errata.
1 numerical experiment session: found 3 NEW errata, **strengthened F-1 dissolution numerically**, **refuted one quantitative claim** (T_c estimate).

**One numerical session ≈ value of 4-5 verification rounds.** For substantive new claims, **code is more powerful than self-verification**.

### 9.3 Implication for tomorrow's plan

**C-S2 should be primarily numerical:**
1. Implement permanent `scc/k_soft.py` (5 lines per Round 4 §7).
2. NEB on K=1 ↔ K=2 transition for canonical exp62/63 setup → ΔF (NQ-25, resolves NQ-15 protocol-specifically).
3. Verify T*_uniform on cycle / expander graphs (NQ-24).
4. Re-derive T_c from explicit entropy + energy on calibrated SCC (closes E-16).
5. Hessian decomposition at K_soft critical points (Round 3 §1) — verify numerical eigenvalues.

These are **concrete numerical tasks**, much more substantive than additional verification rounds.

---

## §10. Final Status (Truly)

8 verification rounds + 1 numerical session = **9 rounds total**.

**Numerical verification of Stage 1 first session:**
- Cat A claims: 19 (no new from numerical, but 3 numerically verified).
- Errata: 17 (E-1 to E-17), 11 actionable.
- New NQs: 27 (24 + 3 from code).
- Substantive corrections: T_c ≈ 0.057 (not 1.0); K_soft(uniform) ≠ 0; multi-init essential.

**Bottom line.** The C+E framework is:
- **Mathematically consistent** (verified 5 rounds).
- **Self-critically aware** (4 critique-mode rounds → 4 errata).
- **Numerically validated where tested** (Hessian + Lipschitz + T*_uniform spot-on; T_c off by 17×).

The numerical T_c ≈ 0.06 finding is **the most consequential single result** of this entire session — it shifts the F-1 dissolution narrative from "balanced low-T preference" to "K=1 only at deeply-zero-T edge case". The thermal multi-mode regime is **nearly all of phase space**.

**This is what code verification adds that pure theory cannot:** quantitative reality-check that catches O(10×) estimate errors invisible to self-verification.

---

**End of Code Verification (Round 9).**

**Session 2026-04-21 truly truly concludes.** Tomorrow's C-S2 should be primarily numerical (NEB, Hessian eigenvalue analysis at saddle, multi-init Boltzmann calibration).
