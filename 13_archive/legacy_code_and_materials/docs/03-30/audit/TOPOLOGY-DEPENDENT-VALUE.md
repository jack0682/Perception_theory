# Self-Referential Terms: Topology-Dependent Value

**Date:** 2026-03-30
**Finding:** The value of self-referential operators (Cl_t, D_t) is strongly topology-dependent.

## Key Result

| Graph Type | Sep Improvement (SCC - BD-only) |
|------------|-------------------------------|
| Grid 20×20 | +0.007 |
| Grid 10×10 | +0.029 |
| Community p_inter=0.01 | +0.035 |
| Community p_inter=0.02 | +0.075 |
| Community p_inter=0.05 | +0.099 |
| Community p_inter=0.10 | +0.173 |

## Interpretation

On grid graphs (clean spatial structure), Allen-Cahn alone creates sharp boundaries because the Laplacian naturally separates spatial regions. The self-referential distinction operator D_t adds marginal value.

On community graphs (fuzzy inter-community boundaries), Allen-Cahn struggles because the Laplacian cannot cleanly distinguish interior from exterior when connections cross community boundaries. The self-referential D_t excels here: it compares aggregated interior support against exterior support, effectively "reading" the community structure that the Laplacian misses.

**The value of self-referential structure increases with boundary complexity.**

This is the correct response to the reviewer critique: "SCC's novelty matters most where Allen-Cahn matters least — on graphs with complex, non-spatial boundary structure."

## Implication for Papers

Both papers should add a "topology-dependent value" subsection showing that self-referential terms are essential for non-grid graphs, even though they are supplementary on grids. This transforms the weakness (marginal on grids) into a strength (essential on realistic graphs).
