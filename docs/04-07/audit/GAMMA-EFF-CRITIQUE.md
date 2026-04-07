# Critique: Barrier Exponent Derivation (BARRIER-EXPONENT.md)

**Date:** 2026-04-07
**Session:** Pre-derivation adversarial audit
**Category:** audit
**Status:** complete
**Depends on:** docs/04-02/proof/BARRIER-EXPONENT.md, experiments/exp38_barrier_height.py, docs/04-06/MERGE-CRITIQUE.md

---

## Issue 1: The Two-Term Model ΔE = Aβ + B√β Is Under-Justified

**Problem.** The derivation posits exactly two β-dependent terms — bulk O(β) and interface O(√β) — with no argument that these are the only contributions. Several mechanisms could introduce intermediate powers:

- **β^{3/4} from interface curvature corrections.** The O(√β) interface term assumes a flat interface with constant curvature. On a discrete 2D grid, interface curvature varies with β (sharper profiles have tighter corners). The curvature correction to surface tension in Ginzburg-Landau is O(ε·κ) where ε = √(2α/β) and κ depends on the formation shape. For a circular formation, this gives a correction O(√β · 1/R) that is O(√β) only if R is β-independent. But R depends on the optimization outcome, which may have weak β-dependence.

- **log(β) from discrete lattice effects.** The continuum Γ-convergence (T11) applies in the limit n → ∞. For fixed n = 225, lattice discretization creates corrections that scale as O(ε²/a²) where a is the lattice spacing. Since ε ~ β^{-1/2}, this gives O(1/β) — negligible at large β but non-trivial in the crossover regime.

- **β-dependent |R_∞|.** The derivation treats |R_∞| as a constant (the sharp-limit reorganization volume). But for finite β, the formation positions and shapes change. The optimizer may place K=2 formations differently at β=20 vs β=100, changing the reorganization geometry. This would make A = A(β), invalidating the two-term decomposition.

**Evidence.** The fitted model (§5.2) systematically underpredicts at intermediate β by 11–18%. A pure two-term model fitted at endpoints should be concave between them (since √β is concave), yet the actual data curves the OTHER way. This is strong evidence for a missing convex contribution.

**Severity:** MODERATE. The two-term model is a reasonable leading-order approximation, but it should not be treated as exact. The 18% error at β=30 is not "noise" — it is systematic and diagnostic.

**Fix:** Either (a) add a β^{3/4} or log(β) term and fit to all four data points, or (b) explicitly state that the two-term model is a leading-order expansion with O(β^{3/4}) remainder, or (c) verify numerically whether the K=2 minimizer positions shift with β (which would make A(β) β-dependent).

---

## Issue 2: Linear-Interpolation Barrier vs. MEP Barrier — Which Matters?

**Problem.** The document itself acknowledges (§4.4) that the true saddle barrier is Θ(√β), while the LI barrier is Θ(β). The effective exponent γ ≈ 0.89 characterizes the LI barrier, which is:

1. **Not an upper bound on escape time.** Kramers-type escape rates depend on the MEP barrier (saddle height), not the LI barrier. A formation at temperature T escapes at rate ~ exp(−ΔE_saddle/T), not exp(−ΔE_LI/T). So γ ≈ 0.89 is irrelevant to metastability timescales.

2. **Not a geometric invariant.** The LI path depends on the parameterization of u₂ and u₁. A different interpolation scheme (geodesic on Σ_m, string method, NEB) would give a different barrier and different γ. The exponent is an artifact of choosing linear interpolation.

3. **exp60 (NEB) exists but is not referenced.** The codebase contains `exp60_neb_barrier.py` which computes barriers via the Nudged Elastic Band method — a much better approximation to the MEP. The derivation should be compared to NEB results, not just LI.

**Severity:** CRITICAL for interpretation, MODERATE for the math. The derivation is internally consistent for the LI barrier, but presenting γ ≈ 0.89 as "the merge barrier exponent" (title, summary) is misleading. The physically meaningful exponent is γ_saddle = 1/2.

**Fix:** Either (a) re-derive for the MEP barrier (harder but more meaningful), or (b) clearly scope the result: "LI barrier exponent" throughout, with a prominent warning that this does NOT control escape rates. The NEB data from exp60 should be compared.

---

## Issue 3: |R_∞| Is Not Well-Defined

**Problem.** The sharp-limit reorganization volume |R_∞| = |S₁ ∪ S₂ △ S| depends on:

1. **K=2 minimizer non-uniqueness.** The K=2 energy landscape has multiple local minima due to the grid's discrete symmetries. Two formations can be placed at any two of the four quadrants. Different K=2 configurations have different S₁, S₂, and thus different R_∞. The exp38 experiment uses `n_restarts=3` — different runs may find different K=2 configurations.

2. **K=1 minimizer near-degeneracy.** On a square grid, the K=1 minimizer is approximately circular and centered. But for volume fractions near 0.5, the optimal shape approaches the entire grid, and corner effects create near-degenerate minimizers. The support S depends on initialization.

3. **β-dependence of optimizer output.** Even if the sharp-limit minimizers are unique (up to symmetry), the actual minimizers at finite β are computed by multi-start gradient descent, which is stochastic. The exp38 data at each β value comes from a DIFFERENT optimization run. The formations found at β=20 and β=100 may not be related by the β→∞ limit in any simple way.

**Implication.** The constant A = |R_∞|/16 in the two-term model is not a well-defined theoretical quantity. It depends on which local minimum the optimizer happened to find.

**Severity:** MODERATE. In practice, on a 15×15 grid with two formations, symmetry constrains the positions sufficiently that |R| doesn't vary much across runs. But this should be verified, not assumed.

**Fix:** Run exp38 multiple times at each β value and report variance of ΔE. If variance is small, |R_∞| is effectively determined by the dominant symmetry class. If large, the entire framework needs revision.

---

## Issue 4: Sign and Magnitude of B

**Problem.** The derivation gives B = (C_∂ − C_s)P√α where C_∂ is the interface conflict coefficient and C_s is the smoothness correction coefficient. The doc says "sign depends on geometry" (§3.5), yet the fitted value is B = +2.27 > 0.

Consider the physical meaning:
- C_∂ > 0: interface nodes ADD to the barrier (they are in the spinodal region, creating mixing penalty)
- C_s > 0: smoothness energy SUBTRACTS from the barrier (parallelogram law gives negative correction, §3.4)

For B > 0, the interface penalty dominates the smoothness correction. But §3.4 derives the smoothness correction as −(α_s/2)‖u₂ − u₁‖²_L, which is ALWAYS negative. The interface penalty (§3.3) is always positive. So the sign of B depends on relative magnitudes.

**The problem:** With B > 0, the γ_eff formula (§4.1) gives γ_eff = (1 + ρ/2)/(1 + ρ) where ρ = B/(A√β) > 0. This yields γ_eff < 1, consistent with the data. BUT: the local exponent at β = 20→30 is γ_local = 1.45 > 1. The two-term model with B > 0 gives γ_local < 1 EVERYWHERE. So the model cannot reproduce the observed γ_local = 1.45 at low β.

The document tries to explain γ_local = 1.45 as "formation restructuring costs" but this is hand-waving that contradicts the fitted model.

**Severity:** MODERATE. The overall OLS fit (γ ≈ 0.89) is reasonable, but the local exponent structure reveals that the two-term model fails qualitatively at low β.

**Fix:** The anomalous γ_local = 1.45 at β ∈ [20, 30] likely signals that the K=2 minimizer CHANGES QUALITATIVELY between β=20 and β=30 (e.g., formations that are diffuse blobs at β=20 become separated droplets at β=30). This is a phase transition in the K=2 landscape, not a smooth crossover. Should be investigated separately.

---

## Issue 5: The 18% Error at β = 30 Is Diagnostic, Not Ignorable

**Problem.** §5.2 fits ΔE = Aβ + B√β to β ∈ {20, 100} and gets 18% underprediction at β = 30. The doc dismisses this as "additional structure" and notes that β^{3/4} might help. But:

1. Four data points are insufficient to distinguish Aβ + B√β from Aβ + Bβ^{3/4} from Cβ^γ. The R² = 0.997 for the power law is uninformative with 4 points and 2 parameters.

2. The systematic underprediction ONLY at intermediate β suggests a non-monotone correction. With the fitted A = 4.77 and B = 2.27, the model is:
   - Exact at β = 20 and β = 100 (by construction)
   - Under at β = 30 by 18%
   - Under at β = 50 by 11%

   A function that is exact at endpoints but too low in between is CONCAVE where the data is CONVEX. This means the actual ΔE(β) has a convex component that Aβ + B√β lacks.

3. The most likely source: A is not constant. If A(β) is increasing in β (because the reorganization volume grows as formations sharpen and separate), then A(30) < A(100) and the model fitted at β=100 overestimates A for β=30. But this means the slope A(β) → A_∞ from below, which would make the model OVER-predict at β=30, not under. So this doesn't explain it.

4. More likely: there is a β-dependent correction to the per-node mixing penalty. At intermediate β, the field values in R are not yet binary (0 or 1) but diffuse, so Φ_i(1/2) > W(1/2) = 1/16 for some nodes. (Yes, GREATER than 1/16 — this can happen when both u_{2,i} and u_{1,i} are in the spinodal region, not at 0 or 1.) This would add a positive bump at intermediate β.

**Severity:** MODERATE. The two-term model is a poor fit to the actual data — it just happens to look OK because R² is inflated by only having 4 points.

**Fix:** Compute ΔE at 10+ β values in [10, 200]. Fit a three-term model. Examine per-node Φ_i contributions at each β to identify the source of the convex correction.

---

## Issue 6: E_cl and E_sep Are Ignored in the Derivation

**Problem.** The entire derivation analyzes only E_bd (boundary/morphology energy). But exp38 computes the FULL energy via `EnergyComputer.energy()`, which includes:

- E_cl = ‖Cl(u) − u‖² (closure energy, weight w_cl = 1.0)
- E_sep = Σ u_i(1 − D_i) (separation energy, weight w_sep = 1.0)
- E_bd = 2α u^T L u + β Σ W(u_i) (boundary energy, weight w_bd = 1.0)

All three terms are computed with equal weight (default w_cl = w_sep = w_bd = 1.0). However, after `normalize_weights()` is called in the optimizer, the effective weights are rescaled by the spectral norm of each term's Hessian.

**Impact on the barrier:**
- E_cl involves the closure operator Cl(u), which depends on the resolvent of the adjacency matrix. Along the interpolation path, Cl(u(α)) varies nonlinearly with α. The closure energy barrier could be non-trivial.
- E_sep involves the distinction operator D(1−u), which also varies nonlinearly. The separation energy may contribute positively or negatively to the barrier.

The derivation's implicit assumption is that E_cl and E_sep contribute O(1) corrections or track E_bd proportionally. This is not justified anywhere.

**Severity:** CRITICAL. If E_cl or E_sep contribute O(β) or O(√β) to the barrier, the constants A and B in the derivation are wrong. The theoretical analysis of E_bd alone may be correct for E_bd, but the experimental validation uses the full energy. The comparison is apples-to-oranges.

**Fix:** Either (a) decompose the exp38 barrier into per-term contributions (the `terms_list` output is already available — just analyze `E_cl`, `E_sep`, `E_bd` separately along the path), or (b) re-derive the barrier for the full energy functional, or (c) verify experimentally that E_cl and E_sep barriers are negligible compared to E_bd.

---

## Issue 7: The Merge Theorem Framework Was Retracted

**Problem.** The BARRIER-EXPONENT.md document depends on "Proposition 1, MERGE-DICHOTOMY-ANALYSIS.md" (K=2 is a local minimum) and "Proposition 2" (K=1 is the global minimum). However, the 04-06 session (MERGE-CRITIQUE.md) identified fatal flaws in the Merge Theorem:

1. The merge endpoint doesn't exist on Σ^K_M (the zero vector has wrong mass)
2. The Mountain Pass theorem was applied to a manifold with boundary
3. Part (a) metastability proof has gaps

The current project status (CHANGELOG.md 04-06) retracted the Merge Theorem.

**Impact on the barrier exponent:** The barrier exponent derivation is EMPIRICAL (fitted to exp38 data) and the two-term decomposition is a physical argument, not a rigorous proof. So it doesn't strictly depend on the Merge Theorem's formal claims. However, the document references Merge Theorem propositions as established facts. These references should be removed or replaced with direct arguments.

**Severity:** MINOR for the mathematics (the scaling analysis stands on its own), MODERATE for the document's credibility (citing retracted results).

**Fix:** Remove references to Merge Theorem propositions. Replace with: (a) direct verification that K=2 minimizers exist (empirical, from exp38), (b) direct verification that K=1 has lower energy (empirical), (c) no formal claim about global minimality.

---

## Issue 8: The Asymptotic Prediction γ → 1 Contradicts the Data Trend

**Problem.** §4.4 proves that γ_eff → 1 as β → ∞ for the LI barrier. But the local exponents from exp38 show a DECREASING trend: 1.45, 0.81, 0.70. Extrapolating, γ_local appears to approach ~0.5 or lower, not 1.

The resolution offered in §4.3 — that γ_eff increases back toward 1 at very high β — requires that:
1. The local exponents first decrease (observed)
2. Then reach a minimum
3. Then increase back toward 1

This is a non-monotone trajectory for γ_local(β), which is possible for ΔE = Aβ + B√β (since the local exponent formula gives γ_local → 1 as β → ∞). But the observed decrease from 0.81 to 0.70 between β ∈ [30,50] and [50,100] shows no sign of the turnaround. The minimum may be at β >> 100.

**The concern:** If the minimum of γ_local is at β ~ 1000, then for all practically relevant β values (20–200), γ_eff is DECREASING, and the asymptotic result γ → 1 is irrelevant. The document creates a misleading impression that γ ≈ 0.89 is a crossover en route to γ = 1, when in fact the crossover may not complete until β is unrealistically large.

**Severity:** MINOR. The asymptotic result is mathematically correct. But the claim that β ∈ [20, 100] is a "crossover regime" (§4.3) is speculative without data at β > 100.

**Fix:** Compute ΔE at β ∈ {200, 500, 1000} to verify the turnaround. If γ_local is still decreasing at β = 1000, reconsider the two-term model.

---

## Issue 9: Volume Projection Along the Interpolation Path

**Problem.** In exp38 (line 91), the interpolated field is clipped and projected:

```python
u_interp = project_volume(np.clip(u_interp, 0.0, 1.0), m_total)
```

The clip-then-project operation is NOT linear interpolation. For fields where (1−α)u₂ + αu₁ exits [0,1] at some nodes, the clipping and re-projection introduces a nonlinear distortion. The actual path through state space is:

u(α) = Π_Σ(clip((1−α)u₂ + αu₁))

where Π_Σ is the volume projection. This is a piecewise-linear path in field space, not a smooth one.

The derivation's analysis (§2, §3) assumes pure linear interpolation. The clipping/projection creates additional curvature in the energy landscape that is not accounted for in the two-term model.

**Severity:** MINOR for large β (where fields are nearly binary and clipping is rarely triggered), MODERATE for small β (where diffuse fields can have values summing to more than m_total after interpolation).

**Fix:** Verify that clipping is rarely triggered at the exp38 parameter values. If it is, the derivation needs to account for the nonlinear correction from projection.

---

## Summary Table

| # | Issue | Severity | Impact on γ ≈ 0.89 |
|---|-------|----------|---------------------|
| 1 | Two-term model unjustified | Moderate | Missing terms explain 18% error |
| 2 | LI barrier vs MEP barrier | Critical (interpretation) | γ_eff is for wrong quantity |
| 3 | |R_∞| non-unique | Moderate | A is not well-defined |
| 4 | B sign vs local exponents | Moderate | Model fails qualitatively at low β |
| 5 | 18% error is diagnostic | Moderate | Model is a poor fit |
| 6 | E_cl, E_sep ignored | Critical | Theory ≠ experiment |
| 7 | Merge Theorem retracted | Minor–Moderate | Citations invalid |
| 8 | γ → 1 contradicts trend | Minor | Asymptotic claim unverified |
| 9 | Volume projection nonlinear | Minor–Moderate | Path ≠ linear interpolation |

**Bottom line:** The derivation has two critical issues (#2 and #6) that undermine the comparison between theory and experiment. Issue #2 means the physically meaningful quantity is γ_saddle = 1/2, not γ_eff = 0.89. Issue #6 means even the LI barrier analysis is incomplete because it ignores E_cl and E_sep, while the experiment measures the full energy. The remaining issues are moderate — the two-term model is a reasonable approximation but not rigorous, and the fitted constants are not well-determined.

Before attempting a new derivation, the minimum necessary steps are:
1. Decompose exp38 barriers by energy term (E_bd vs E_cl vs E_sep)
2. Verify |R_∞| stability across multiple optimizer runs
3. Decide whether to derive for LI barrier (easier, less meaningful) or MEP barrier (harder, physically correct)
