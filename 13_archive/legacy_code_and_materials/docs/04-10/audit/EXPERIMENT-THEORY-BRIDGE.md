# Experiment-Theory Bridge

**Date:** 2026-04-10
**Session:** Cycle 1 experiment-to-theory bridge
**Category:** audit
**Status:** active
**Depends on:** experiments/exp65_formation_tracking.py; experiments/results/exp65_formation_tracking.json; experiments/results/exp65_lambda_rep0_20x20_c06.json; experiments/results/exp65_lambda_rep1_20x20_c06.json

---

## What exp65 Supports

| Observation | Honest theoretical use |
|---|---|
| Default `lambda_rep=10` branches show no label swaps | Supports that swap mechanism is not the default explanation |
| Default branches are mostly centered/stable | Supports Type A candidate classification for default branch |
| `20x20_c0.6` becomes off-center at `lambda_rep=0` | Shows branch type is repulsion/selection dependent |
| Lambda_coupling is zero for disjoint branches | Shows Lambda alone is insufficient as branch descriptor |

## What exp65 Does Not Prove

| Non-proof | Reason |
|---|---|
| Exact lambda_rep bifurcation threshold | Only tested 0, 1, 10 for one config |
| Uniqueness of Type A/Type B branches | Multi-start may miss branches |
| Analytic branch transition law | Experiments identify candidates, not proof |
| Canonical theorem category upgrade/downgrade | Requires proof-level statement and registry synchronization |

## Minimal Next Experiment

Run a continuation-style sweep, not isolated multi-start only:

```text
lambda_rep values: 0, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10
configs: 15x15:c0.5, 15x15:c0.6, 20x20:c0.5, 20x20:c0.6
selection modes: warm-start increasing, warm-start decreasing, multi-start best
```

Required output:

1. branch label,
2. center_offset_norm,
3. separation,
4. active supports / overlap,
5. Hessian or proxy degeneracy marker if available,
6. energy crossing evidence between branches.

## Sweep Result Integrated

The first sweep shows `20x20_c0.6` switches from Type B at `lambda_rep=0` to Type A at every tested positive value `lambda_rep >= 0.05`. The honest theory bridge is therefore a zero-repulsion degeneracy / positive-repulsion perturbation problem, not yet an exact finite-positive bifurcation threshold.

Numerical evidence still cannot prove the positive-repulsion theorem, but it identifies the next proof route: perturb the degenerate zero-repulsion branch family and show the first-order correction is the overlap term.


## Exp73 Catalog Integration

### What exp73 supports

| Observation | Honest theoretical use |
|---|---|
| finite frozen catalog contains a strongly-interacting low-`E0` branch and a weakly-interacting zero-overlap near-degenerate branch | supports candidate-conditioned branch reselection by `E0 + lambda_rep * overlap` |
| first lower-envelope replacement occurs at `lambda_cross ≈ 9.09e-4` in the smoke catalog | supports that the relevant threshold may be tiny-positive rather than exactly zero **for this finite catalog** |
| crossing occurs between two Type A candidates | shows branch selection is not reducible to a naive Type A/Type B dichotomy |

### What exp73 still does not prove

| Non-proof | Reason |
|---|---|
| exhaustive global branch threshold | catalog is finite and initialization dependent |
| universal threshold law in grid size / volume fraction | only one smoke config tested |
| uniqueness of selected branch | multiple representatives remain near the lower envelope |
| theorem-category upgrade | experiment gives candidate-conditioned support only |


## Exp73 Grid Expansion Update

The expanded source-0 anchored catalog changes the honest interpretation again: the smoke-scale crossing near `9e-4` is not stable. Across five configs, the first anchored frozen crossing ranges from roughly `9.2e-2` to `4.6`, so the only safe bridge statement is that **finite-catalog branch replacement exists but is configuration/catalog dependent**.


## Exp74 Family-Match Update

A stricter family-matched comparison weakens the raw Exp73 lower-envelope interpretation further: in multiple configs the earliest global replacement is much earlier than the nearest same-type matched-family crossing, and in some configs the matched family has no lower-overlap crossing at all. The safe bridge statement is therefore that **global replacement is often a family-switch effect**.


## Exp74 High-Budget Update

The higher-budget sentinel reruns show that family-switch is not a universal explanation: `10x10:0.6` admits a same-family crossing once the catalog is enlarged, while `15x15:0.6` and `20x20:0.6` still do not. The safe bridge statement is therefore that **branch-threshold interpretation is highly budget/config dependent**.


## Exp75 Seeded-Continuation Update

The hardest-sentinel case `20x20:0.6` now has a direct counterweight to the catalog-only interpretation: when the best zero-lambda Type B branch is reused as the initializer, Type B-like positive-lambda continuations appear up to at least `lambda=0.2`. So catalog failure must not be read as physical nonexistence.


## Exp76 Fine-Continuation Update

The `20x20:0.6` hardest-sentinel story is now much narrower: a seeded Type B branch can be warm-continued to `lambda=1.0` without losing its Type B label on the tested grid. The open issue is therefore not branch existence, but branch selection versus persistence.


## Exp77 Selection-vs-Persistence Update

On `20x20:0.6`, the persistent seeded Type B branch currently beats every discovered raw-catalog competitor on the tested lambda grid. So the experimental bottleneck is now clearly branch discovery quality rather than simple persistence failure.


## Exp78 Search-Upgrade Update

On `20x20:0.6`, once the recovered continuation branch is injected into direct optimization, the optimizer finds an even lower-energy Type B branch than either the raw catalog or the plain continuation branch. This makes search protocol sensitivity the dominant experimental caveat for R1-Q.
