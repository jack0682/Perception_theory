# Remaining Gap Analysis After exp62-exp65

**Date:** 2026-04-10
**Session:** Continuation of K=2 landscape and remaining-gap analysis
**Category:** audit
**Status:** complete
**Depends on:** Canonical Spec v2.1.md §13 and §15; docs/04-07/SESSION-04-07-INDEX.md; docs/04-07/synthesis/NEXT-STEPS-FORMATION-TRACKING.md; experiments/exp65_formation_tracking.py

---

## 0. Executive Verdict

The interrupted gap analysis from the prior session has been resumed and sharpened.

**Main result:** exp65 directly tracks K=2 formation centers along the mass-transfer direction. Under the canonical/default K-field setting (`lambda_rep=10`), all four tracked configurations stay spatially stable: no label swaps, no soft overlap, and near-centered formation pairs. The earlier Type B/off-center behavior is therefore **not a universal property of the default K=2 branch**; it is branch- and repulsion-dependent.

**New finding:** On the hardest previously flagged case (`20x20_c0.6`), lowering inter-formation repulsion to `lambda_rep=0` produces a clear Type B/off-center branch (`center_offset_norm ≈ 0.165`), while `lambda_rep=1` and `lambda_rep=10` remain Type A/centered. Thus the unresolved gap is no longer simply “Type A vs Type B exists”; it is:

> Determine the branch-selection bifurcation in the joint space of grid geometry, `lambda_rep`, `lambda_sep`, and optimizer initialization.

No theorem status is changed by this session. The correct action is **not** to upgrade/downgrade Canonical Spec yet, but to record the branch sensitivity and run a targeted exp66/exp65-sweep if this gap is to be closed further.

---

## 1. Recovered Work Queue

The previous 04-07 session ended with this explicit continuation path:

1. Write exp65 formation-tracking code.
2. Run exp65 on the four exp62/exp63 configurations.
3. Compare actual swaps/center motion against the ACF[1] and Type A/B hypotheses.
4. Only then update regime classification in Canonical Spec if the evidence is strong.

This session completed steps 1-3. Step 4 is intentionally deferred because the evidence shows branch sensitivity rather than a stable spec-level classification rule.

---

## 2. Evidence Produced This Session

### 2.1 New experiment implementation

Created:

- `experiments/exp65_formation_tracking.py`

Outputs:

- `experiments/results/exp65_formation_tracking.json`
- `experiments/results/exp65_formation_tracking.csv`
- `experiments/results/exp65_lambda_rep1_20x20_c06.json`
- `experiments/results/exp65_lambda_rep1_20x20_c06.csv`
- `experiments/results/exp65_lambda_rep0_20x20_c06.json`
- `experiments/results/exp65_lambda_rep0_20x20_c06.csv`

Tracked fields per epsilon:

- center of mass for `u1`, `u2`
- pair midpoint and normalized center offset
- separation `d_c`
- orientation `theta` modulo pi
- label-swap detection from previous epsilon
- hard overlap, soft overlap, minimum support distance
- `Lambda_coupling` and geometric/lambda regime labels
- total K-field energy

### 2.2 Default branch results (`lambda_rep=10`)

| Config | Type label | Mean center offset | Mean separation | Swaps | Energy asymmetry E(+)-E(-) | Regime notes |
|---|---:|---:|---:|---:|---:|---|
| `15x15_c0.5` | Type A candidate | 0.032 | 10.43 | 0 | +0.0472 | weakly-interacting by distance threshold |
| `15x15_c0.6` | Mixed/ambiguous | 0.076 | 9.59 | 0 | -0.0052 | well-separated |
| `20x20_c0.5` | Type A candidate | 0.011 | 13.56 | 0 | +0.1116 | boundary between weak/well-separated |
| `20x20_c0.6` | Type A candidate | 0.022 | 13.08 | 0 | -0.0052 | well-separated |

Interpretation:

- **No label-swap mechanism was found** on the default branch.
- `Lambda_coupling = 0` throughout because the optimized formations are support-disjoint at the soft-overlap threshold used by `coupling_strength`.
- The 04-07 ACF[1] proxy is therefore **not validated** by default-branch spatial tracking. It may have been measuring optimizer valley-hopping in exp63 rather than physical label swaps.

### 2.3 Repulsion sensitivity probe (`20x20_c0.6`)

| `lambda_rep` | Type label | Mean center offset | Mean separation | Swaps | Energy asymmetry E(+)-E(-) | Regime |
|---:|---|---:|---:|---:|---:|---|
| 10.0 | Type A candidate | 0.022 | 13.08 | 0 | -0.0052 | well-separated |
| 1.0 | Type A candidate | 0.023 | 13.37 | 0 | +0.0895 | well-separated |
| 0.0 | Type B candidate | 0.165 | 11.55 | 0 | -0.0646 | weakly-interacting |

Interpretation:

- Type B/off-center behavior appears when explicit repulsion is removed.
- The transition is not caused by label swapping; it is a different optimizer-selected spatial branch.
- The next useful experiment is a `lambda_rep` sweep, not another single default-parameter rerun.

---

## 3. Updated Gap Register

### 3.1 Category B items in Canonical Spec v2.1

| Item | Current status | This-session assessment | Next closure route |
|---|---|---|---|
| Barrier exponent `gamma_eff ≈ 0.89` | Cat B | Leave Cat B. 04-07 audit already showed the exponent is optimizer/path/range dependent. | Only make optimizer-conditioned claims, or replace exponent with asymptotic `Theta(beta)` + branch-conditioned constants. |
| General-graph birth supercriticality | Cat B | Not touched. Still needs proof beyond D4/simple cases. | Cheeger/spectral-clustering or equivariant bifurcation argument for non-D4 degenerate eigenspaces. |
| `d_min*` quantitative formula | Cat B | Not touched directly. exp65 supports branch dependence of spatial separation. | Replace single regression formula with branch-conditioned bounds; validate across `lambda_rep` and grid-size sweep. |
| Beyond-Weyl 33x quantification | Cat B | exp65 shows `Lambda_coupling` can collapse to zero on disjoint branches, so fixed “33x” remains too configuration-specific. | Wider grid/overlap validation; report interval rather than point factor. |

### 3.2 Category C items in Canonical Spec v2.1

| Item | Current status | This-session assessment | Next action |
|---|---|---|---|
| T-Persist-1(d) exact threshold | Cat C due structural `beta > 7 alpha` condition | Leave as Cat C unless the structural condition is reframed as regime definition. | Do not silently remove condition; maybe split theorem into unconditional shifted-threshold part and structural exact-threshold corollary. |
| T-Persist-Full | Cat C because it chains through T-Persist-1(d) | Leave Cat C. | Same as above. |
| T-Persist-K-Sep | Cat C due WS/SR structural regime hypotheses | Leave Cat C. Conditions are definitions, not accidental gaps. | Consider relabeling as “regime theorem” rather than trying to erase conditions. |
| T-Persist-K-Weak | Cat C due WI/SR/NB-K | Leave Cat C. exp65 suggests branch selection matters before persistence claims. | Validate under branch-sensitive initialization and overlap sweep. |
| T-Persist-K-Unified | Cat C due five structural hypotheses | Leave Cat C. exp65 exposes that `Lambda_coupling` alone can be zero on disjoint branches while geometry/repulsion still matters. | Extend unified parameterization with branch-selection state or repulsion/history variable. |

### 3.3 Research extensions from §15

| Extension | Updated status |
|---|---|
| Near-bifurcation persistence (`mu -> 0`) | Still open; unrelated to exp65 except that branch selection may create near-bifurcation windows. |
| Multi-formation kinetic dynamics | Still central. exp65 supports kinetic/branch framing: K=2 type is selected by optimizer path and repulsion, not only by thermodynamic energy. |
| Merge barrier on relaxed manifold | Still open. exp65 indicates relaxed-manifold `F''(M/2)` must be branch-conditioned; a single scalar sign is not well-defined without specifying branch selection. |

---

## 4. What exp65 Resolves vs. What It Does Not

### Resolved for the default branch

- Default `lambda_rep=10` trajectories do **not** show label swaps across the tested epsilon range.
- The default tracked branch is spatially stable and mostly centered.
- The 04-07 “swap” hypothesis is not supported as the explanation for exp62/exp63 divergence on the default branch.

### Not resolved

- Whether multiple local K=2 branches coexist at the same parameter values.
- The bifurcation threshold in `lambda_rep` between centered and off-center branches.
- Whether `lambda_sep`, grid size, and Fiedler structure alter that threshold.
- Whether exp63’s F'' sign flips arise from branch jumps, optimizer restarts, or sparse finite-difference sampling.

---

## 5. Recommended Next Experiment

Create an exp66 or extend exp65 with a sweep mode:

```bash
python3 experiments/exp65_formation_tracking.py \
  --configs 15x15:0.5 15x15:0.6 20x20:0.5 20x20:0.6 \
  --lambda-rep <sweep value> \
  --n-restarts 4 --max-iter 1500
```

Minimum useful sweep:

```text
lambda_rep ∈ {0, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10}
```

Decision criteria:

- Type B if `mean_center_offset_norm >= 0.12` or stable off-center branch persists over epsilons.
- Type A if `max_center_offset_norm < 0.08`, no swaps, and orientation drift `< 0.35 rad`.
- Ambiguous if thresholds conflict.

Expected closure target:

> A branch-selection diagram in `(grid_size, c_ref, lambda_rep)` space, with `lambda_sep` and Fiedler asymmetry as explanatory covariates.

Only after that diagram exists should Canonical Spec §12/§13 be amended.

---

## 6. Carry-Forward Items

1. Do **not** change theorem categories from this session alone.
2. Treat K=2 type as branch-conditioned, not a scalar property of `(grid_size, c_ref)`.
3. Run a `lambda_rep` sweep before attempting any spec update.
4. The unrelated dirty file `experiments/exp_cohesion_scale.py` was minimally repaired by replacing the stale GPU-mode expression with `mode = "CPU"`; no experiment was rerun for that script.
