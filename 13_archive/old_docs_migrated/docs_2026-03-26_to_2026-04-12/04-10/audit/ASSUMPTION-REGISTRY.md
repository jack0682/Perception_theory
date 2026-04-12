# Assumption Registry

**Date:** 2026-04-10
**Session:** Cycle 1 assumptions
**Category:** audit
**Status:** active
**Depends on:** docs/04-10/audit/CURRENT-TARGET.md; scc/multi.py; scc/energy.py

---

## Branch-Selection Analysis Assumptions

| ID | Assumption | Type | Removable? | Notes |
|---|---|---|---|---|
| A1 | G finite connected graph | structural | no | Ensures finite-dimensional compact feasible set |
| A2 | Parameters satisfy SCC admissibility: a_cl < 4, b_D=0, spinodal c | structural | no | Inherited from ParameterRegistry |
| A3 | Feasible set includes box constraints 0 <= u <= 1 and volume constraints | structural | no | Product of compact convex polytopes |
| A4 | Work on a fixed active set for analytic branch theorem | technical/local | yes only by piecewise analysis | Active-set changes are branch event boundaries |
| A5 | Local minimizer is KKT nondegenerate: reduced bordered Hessian invertible/positive definite on tangent cone | theorem hypothesis | no for IFT | Failure is exactly a bifurcation/degeneracy event |
| A6 | Branch-selection rule is specified when claiming selected branch behavior | logical | no | Without this, optimizer dependence is untracked |
| A7 | lambda_bar finite, not hard simplex projection | implementation | possibly | Current scc/multi.py uses penalty; hard constraint would require separate KKT system |
| A8 | Experiments are support only, not proof | proof-quality | no | Required by project rules |

## Hidden Assumptions Exposed

| Hidden assumption | Problem |
|---|---|
| “The K=2 minimizer” is unique | False or unproved; symmetries and local minima create multiple branches |
| Type A/B is a function only of (grid_size, c_ref) | False from exp65 repulsion probe |
| Lambda_coupling alone determines branch type | Insufficient: exp65 has Lambda_coupling = 0 across disjoint but geometrically different branches |
| F''(M/2) is branch-independent | False universalization; F'' is local to selected branch/trajectory |
