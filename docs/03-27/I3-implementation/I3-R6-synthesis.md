# Iteration 3 — Round 6: Parameter Selection Synthesis

**Author:** Implementation Synthesizer
**Date:** 2026-03-27
**Inputs:** Algorithm Designer R6 (primary), Experiment Designer R6, R4/R5 syntheses
**Status:** COMPLETE — Algo + Experiment positions integrated; Sys covered by R4 architecture

---

## I. EXECUTIVE SUMMARY

Parameter selection is the bridge between SCC's mathematics and computation. Two converging results:

1. **R10's 10⁵× separation dominance is a normalization artifact** (Algo Designer). Realistic: O(1) to O(10²). The Experiment Designer predicts it reduces to 1-10× when Hessian-normalized — aligning with the Rigor Auditor's R13 caveats.

2. **Hessian normalization is the principled default** (Algo Designer). Normalizes λ values by spectral norms of per-term Hessians at the uniform state. Energy-value normalization (R4 proposal) is flawed because E_bd's smoothness term vanishes at uniform.

The R10 resolution experiment is designed: 110 runs, ~15 minutes compute, highest-ROI experiment in Iteration 3.

---

## II. NORMALIZATION METHOD: HESSIAN (ADOPTED)

**R4 proposal (superseded):** λ_i = w_i / E_i(c·1). Problem: E_bd smoothness = 0 at uniform.

**R6 proposal (adopted):** λ_i = w_i / ‖H_i(c·1)‖_op. Computed via Lanczos (~30 mat-vecs per term).

| Property | Energy-value | Hessian |
|----------|-------------|---------|
| Captures Laplacian contribution | No (smoothness = 0 at uniform) | Yes |
| Physical meaning of λ ratios | "Equal energy at uniform" | "Equal instability contribution" |
| Cost | O(n) — trivial | O(90·\|E\|) — cheap |
| Relevant to R10 verification | No | **Yes — directly measures per-term instability** |

**User interface:** Relative weights w_cl, w_sep, w_bd ∈ [0, 1]. Internal λ computed automatically. Users never set raw λ values.

---

## III. R10 RESOLUTION: THE EXPERIMENT

**Design (Experiment Designer):** 11 configurations, λ_sep/λ_bd from 0 to 1000, on 10×10 grid, β=10, c=0.5. Plus constrained Hessian decomposition addressing all 3 R13 caveats.

**Predictions (converging across positions):**

| # | Prediction | Source |
|---|-----------|--------|
| P-S1 | Goldilocks range at λ_sep/λ_bd ∈ [10⁻³, 10⁻¹] | Experiment Designer |
| P-S2 | 10⁵× reduces to 1-10× when Hessian-normalized | Experiment Designer + Algo Designer |
| P-S3 | Separation enhances but does not replace double-well | Both |
| P-S5 | Anti-Turing pattern may survive at moderate λ_sep | Experiment Designer |

**The verdict question (Experiment Designer):** Is there a λ_sep/λ_bd range where formations are QUALITATIVELY BETTER than pure Allen-Cahn? If yes → separation is genuine contributor. If no → decorative.

**Budget:** ~15 minutes compute. **Highest-ROI experiment in Iteration 3.**

---

## IV. PARAMETER ADMISSIBILITY CHECKER

Complete validator integrating Algo Designer R6 + R4/R5 constraints:

| Check | Constraint | Source |
|-------|-----------|--------|
| Contraction | a_cl < 4 | A3 (R4, T20) |
| Spinodal range | c ∈ (0.211, 0.789) | W''(c) < 0 required for T8 |
| Phase transition (E_bd only) | β/α > 4λ₂/\|W''(c)\| | T8-Core |
| Phase transition (full energy) | min eigenvalue of H_total < 0 on Σ_m | R6 — goes beyond T8-Core |
| Resolvent convergence | α_C · ρ(W_sym) < 1 | R5 |
| Analyticity | b_D = 0 | T14 (Łojasiewicz) |
| Distinction nontrivial | a_D > τ_D (approx) | D_t must be nonzero |

**Critical R6 addition:** The full-energy Hessian check catches cases where T8-Core's β/α condition is met but E_cl or E_sep stabilize the uniform state. This can happen when λ_cl or λ_sep are large relative to λ_bd.

---

## V. ANNEALING FALLBACK

For difficult regimes where direct optimization converges to trivial:

```
Phase 1 (0-30%):   E = E_bd only             (Allen-Cahn separation)
Phase 2 (30-60%):  E = E_bd + ramp · E_cl    (closure correction)
Phase 3 (60-80%):  E = E_bd + E_cl + ramp · E_sep  (separation)
Phase 4 (80-100%): E = full energy            (final convergence)
```

**When to trigger:** Automatic fallback if direct optimization (all terms from start) shows energy plateau or converges to u ≡ c after 1000 steps.

---

## VI. REVISED DEFAULT PARAMETERS (v2, incorporating R5 + R6)

```python
DEFAULTS_V2 = {
    # Operator (unchanged from R4 except α_resolvent)
    'a_cl': 3.5, 'eta_cl': 0.5, 'tau_cl': 0.5,
    'a_D': 5.0, 'lambda_D': 1.0, 'tau_D': 0.0, 'b_D': 0.0,
    'alpha_resolvent': 0.1,  # α_C·ρ ≈ 0.4 for 2D grid
    'k_neumann': 10,

    # Energy (user-facing relative weights)
    'w_cl': 1.0, 'w_sep': 1.0, 'w_bd': 1.0,
    'normalization': 'hessian',   # NEW: replaces energy-value
    'lanczos_iter': 30,

    # Morphology
    'alpha_bd': 1.0, 'beta_bd': 10.0,
    'volume_fraction': 0.3,

    # Optimization
    'dt_init': 0.01, 'max_iter': 10000, 'n_restarts': 5,
    'eps_energy': 1e-8, 'eps_field': 1e-6, 'eps_grad': 1e-6,
    'k_diag': 100,

    # Annealing
    'use_annealing': False,
    'anneal_phases': [0.3, 0.6, 0.8],

    # C_t (from R5)
    'ct_staleness_threshold': 0.01, 'ct_max_age': 50,
    'ct_method': 'auto',
}
```

---

## VII. INTEGRATION WITH CRITICAL PATH

R6 modifies the R4 critical path:

```
REVISED CRITICAL PATH:
  Operators → Energy → Per-term Hessians
    ├→ Hessian normalization (before optimization)
    ├→ Parameter validator (before optimization)
    └→ R10 verification / E1 experiment (110 runs, ~15 min)
  → Gradient flow → Phase diagram → Sensitivity → Capstone
```

The Hessian module serves triple duty: normalization, validation, and R10 verification.

---

## VIII. DECISIONS

| # | Decision | Rationale |
|---|----------|-----------|
| D1 | Hessian normalization replaces energy-value | E_bd smoothness=0 at uniform makes energy-value unbalanced |
| D2 | R10 dominance expectation: O(1)-O(10²) | Algo + Experiment agree; 10⁵× was normalization artifact |
| D3 | Full-energy Hessian check mandatory | T8-Core (E_bd only) is necessary but not sufficient |
| D4 | Annealing as automatic fallback | Safety net for difficult parameter regimes |
| D5 | User-facing relative weights, not raw λ | Prevents user errors; auto-scaling is internal |
| D6 | R10 experiment: 110 runs, ~15 min | Highest-ROI experiment; determines narrative |

---

*Complete synthesis. Parameter selection is resolved: Hessian normalization default, admissibility checker mandatory, annealing fallback automatic, R10 expectations recalibrated. The 15-minute R10 experiment will settle the theory's computational narrative.*
