# docs/04-01 — Index

**Date:** 2026-04-01
**Session:** Open problems — directional basin bounds, β threshold refinement, a₃ decomposition

---

## proof/

| File | Status | Description |
|------|--------|-------------|
| [DIRECTIONAL-BASIN-BOUNDS.md](proof/DIRECTIONAL-BASIN-BOUNDS.md) | complete | Theorem PSM (perturbation–soft mode misalignment), Theorem EBC (ellipsoidal basin containment), Theorem TP (transverse persistence). Proves f₁_grad ≤ √(n_bdy/n_F) for gradient perturbation direction; clarifies distinction from IFT displacement direction. |

## theory/

| File | Status | Description |
|------|--------|-------------|
| [TRANSPORT-SELECTION-ANALYSIS.md](theory/TRANSPORT-SELECTION-ANALYSIS.md) | complete | A1: Degree theory / continuation analysis for transport fixed-point selection. |
| [MERGE-DICHOTOMY-ANALYSIS.md](theory/MERGE-DICHOTOMY-ANALYSIS.md) | complete | A2: Merge dichotomy analysis — K=2 is local min (not saddle), barrier model replaces saddle descent conjecture. Isoperimetric energy ordering, revised K-Strong status. |
| [NEARBIF-DIRECTIONAL-EXTENSION.md](theory/NEARBIF-DIRECTIONAL-EXTENSION.md) | complete | Phase 3: Directional basin extends Tier 1 persistence 2.5-4.3× into near-bif regime. Universal isoperimetric ordering (24 topologies). Boundary instability channel verified. |
| [ISOPERIMETRIC-TRANSPORT-PROOFS.md](theory/ISOPERIMETRIC-TRANSPORT-PROOFS.md) | complete | Phase 4: Isoperimetric energy ordering proved (test function + isoperimetric inequality). Transport confinement bound proved (C_conf = O(σ√(ε_OT log n)), u_s-independent). |
| [R-BAR-BOUND.md](theory/R-BAR-BOUND.md) | complete | Phase 6: Analytical bound on r̄₀ (mean KKT residual). Three approaches: Cauchy–Schwarz, binary mass-balance, KKT contraction. Main result: r̄₀ = O(n^{-1/d}) for τ=1/2 via sharp-interface cancellation. Upgrades T-Bind to Category A. |

## synthesis/

| File | Status | Description |
|------|--------|-------------|
| [UNIFIED-THEORY-STATUS.md](synthesis/UNIFIED-THEORY-STATUS.md) | complete | Phase 5: Comprehensive synthesis of all Phase 1-4 results. 24 fully proved, 6 structural, 6 conditional, 2 retracted, 5 open. Dependency graph, gap register, publication readiness assessment. |
