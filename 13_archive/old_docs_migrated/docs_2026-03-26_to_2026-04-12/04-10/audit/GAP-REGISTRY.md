# Gap Registry

**Date:** 2026-04-10
**Session:** SCC theorem-closing campaign registry
**Category:** audit
**Status:** active
**Depends on:** docs/04-10/audit/LATEST-GAP-TABLE.md; Canonical Spec v2.1.md §13-15

---

## Formal Gap Buckets

| ID | Canonical item | Bucket | Current campaign status |
|---|---|---|---|
| B1 | Barrier exponent gamma_eff ≈ 0.89 | Category B | Active, downstream of R1 branch conditioning |
| B2 | General-graph birth supercriticality | Category B | Active |
| B3 | Quantitative d_min* formula | Category B | Active, downstream of R1 branch conditioning |
| B4 | Beyond-Weyl 33x quantification | Category B | Active |
| C1 | T-Persist-1(d) exact threshold preservation | Category C | Active |
| C2 | T-Persist-Full | Category C | Active, chained through C1 |
| C3 | T-Persist-K-Sep | Category C | Active, regime theorem |
| C4 | T-Persist-K-Weak | Category C | Active, regime theorem |
| C5 | T-Persist-K-Unified | Category C | Active, regime theorem |

## Research Blockers

| ID | Research blocker | Current status | Relation to formal gaps |
|---|---|---|---|
| R1 | K=2 branch-selection bifurcation | Split in Cycle 1 into R1-P and R1-Q | Blocks B1/B3 and merge-barrier wording |
| R2 | Near-bifurcation persistence mu -> 0 | Active | Related to C1/C2 |
| R3 | Multi-formation kinetic dynamics | Active | Related to C3-C5 |
| R4 | Merge barrier on relaxed manifold | Active | Related to B1 and R1 |

## Cycle 1 Registry Delta

| Delta | Status |
|---|---|
| R1 universal scalar Type A/B classification | Rejected as too strong |
| R1-P finite-dimensional branch-continuation theorem | REFORMULATED AND PROVED under explicit nondegenerate active-set hypotheses |
| R1-Q quantitative branch-selection threshold | OPEN-CONDITIONAL; requires lambda_rep sweep and branch-conditioned endpoint specification |
| Canonical Spec theorem category changes | None |


## Cycle 56 Registry Delta

| Delta | Status |
|---|---|
| R1-Q frozen candidate catalog threshold | NUMERICAL SUPPORT ONLY: smoke catalog gives `lambda_cross ≈ 9.09e-4` |
| Exp72 candidate discovery bottleneck | partially resolved by multi-start catalog; still non-exhaustive |
| global/universal branch threshold | remains OPEN-CONDITIONAL |


## Cycle 57 Registry Delta

| Delta | Status |
|---|---|
| Exp73 tiny-positive smoke threshold | reclassified as unstable small-catalog artifact |
| source-0 anchored first-crossing scale | numerical range observed: `0.092` to `4.605` across five configs |
| R1-Q | remains OPEN-CONDITIONAL; needs family-matched / larger-catalog analysis |


## Cycle 58 Registry Delta

| Delta | Status |
|---|---|
| global crossing vs within-family crossing | separated numerically by Exp74 |
| early/moderate crossings in R1-Q | often family-switch events in current catalog |
| R1-Q | remains OPEN-CONDITIONAL; next step is budget/threshold robustness |


## Cycle 59 Registry Delta

| Delta | Status |
|---|---|
| family-switch diagnosis | robust for hard configs but not universal |
| catalog-budget effect | confirmed numerically |
| R1-Q | remains OPEN-CONDITIONAL; hardest active survivor is `20x20:0.6` |


## Cycle 61 Registry Delta

| Delta | Status |
|---|---|
| hardest-sentinel catalog absence | reclassified as search/discovery failure, not physical absence |
| seeded Type B continuation on `20x20:0.6` | numerically supported up to `lambda=0.2` with later mixed-label drift |
| R1-Q | remains OPEN-CONDITIONAL; next gap is branch-label loss vs true family loss |


## Cycle 62 Registry Delta

| Delta | Status |
|---|---|
| hardest-sentinel Type B existence | strengthened to persistence through `lambda=1.0` under warm continuation |
| branch-label loss before `lambda=1.0` | not supported on current fine grid |
| R1-Q | narrowed to selection-vs-persistence comparison |


## Cycle 63 Registry Delta

| Delta | Status |
|---|---|
| persistence-vs-selection on `20x20:0.6` | persistent Type B branch beats all discovered raw-catalog competitors on tested grid |
| main R1-Q bottleneck | shifted to optimizer/search reliability |
| R1-Q | remains OPEN-CONDITIONAL; next step is search-protocol upgrade |


## Cycle 64 Registry Delta

| Delta | Status |
|---|---|
| selected-branch inference on `20x20:0.6` | highly search-protocol dependent |
| injected-seed upgraded optimization | returns lower-energy Type B branches at `0.1, 0.5, 1.0` |
| R1-Q | remains OPEN-CONDITIONAL; next step is generalization beyond the hardest sentinel |


## Cycle 69 Registry Delta

| Delta | Status |
|---|---|
| R1-Q3 search reliability gap | upgraded to an explicit numerical-support proposition |
| selected-branch threshold wording | now explicitly protocol-tagged by campaign rule |
| search-neutral selected-branch theorem | remains open |
