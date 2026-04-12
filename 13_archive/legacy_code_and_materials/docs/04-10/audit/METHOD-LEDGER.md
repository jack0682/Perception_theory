# Method Ledger

**Date:** 2026-04-10
**Session:** Cycle 1 method ledger for R1
**Category:** audit
**Status:** active
**Depends on:** docs/04-10/audit/CURRENT-TARGET.md; docs/04-10/audit/ASSUMPTION-REGISTRY.md

---

## Target

R1 — K=2 branch-selection bifurcation.

## 20-Method Attack Ledger

| # | Method | Why it might work | Execution summary | Result | Failure / lesson |
|---:|---|---|---|---|---|
| 1 | Compactness + extreme value theorem | Product simplices are compact | Energy continuous on compact feasible set | Proves global minimizers exist | Does not prove uniqueness or selected branch |
| 2 | Berge maximum theorem | Parameterized compact optimization has stable minimizer sets | Apply to lambda_rep, masses, beta | Gives upper hemicontinuity of argmin set | Set-valued; branch jumps remain possible |
| 3 | Fixed-active-set KKT + IFT | Local minimizers satisfying strict complementarity solve analytic equations | Write KKT system on fixed active set and apply IFT | Proves local analytic continuation | Ends at Hessian degeneracy or active-set change |
| 4 | Reduced Hessian / second variation | Branch bifurcation is detected by loss of positive definiteness | Analyze Hessian on tangent cone | Identifies bifurcation event criterion | Requires computing/evaluating branch Hessian |
| 5 | Energy-crossing analysis | Selected branch can change by lower-energy crossing | Compare two local branch energy functions | Shows selection changes can occur without local degeneracy | Requires identifying competing branches |
| 6 | Symmetry / equivariant bifurcation | Square grids have symmetry-related branches | Treat D4 orbit of minimizers | Explains non-uniqueness under symmetry | Does not handle asymmetric graphs/general thresholds |
| 7 | Explicit low-dimensional toy model | Counterexample to universal scalar Type A/B may be small | Two-mode or two-site reduced energy can exhibit branch dependence | Supports rejection of universal classification | Toy model must be linked carefully to SCC energy |
| 8 | Fiedler-mode reduction | Branches may align with low graph modes | Reduce field to first few Laplacian eigenmodes | Promising for branch diagram | Nonlinear closure/boundary terms make closure incomplete |
| 9 | Cheeger / graph-cut relaxation | Type selection may be cut geometry | Relate separated supports to cut/isoperimetry | Useful for d_min downstream | Too coarse for branch threshold |
| 10 | Gamma-convergence / sharp interface | Large beta shapes approximate sets | Reduce to two-droplet geometry and interaction | Gives asymptotic branch geometry | Does not determine finite-beta optimizer branch alone |
| 11 | Perturbation in lambda_rep | R1 is explicitly repulsion-sensitive | Differentiate KKT branch w.r.t. lambda_rep | Gives local sensitivity formula under nondegeneracy | Cannot cross branch events |
| 12 | Mass-transfer epsilon IFT | F'' is local along a branch | Continue local minimizer in epsilon | Proves branch-local F'' is well-defined | Does not make F'' branch-independent |
| 13 | Transversality / genericity | Degenerate events may be codim-1 | Apply generic nondegenerate crossing logic | Plausible event stratification | Needs full proof for nonsmooth active-set boundaries |
| 14 | Numerical continuation | Could trace actual branches | Warm-start along lambda_rep sweep | Best practical next step | Experimental support only, not proof |
| 15 | Normal form near branch event | Branch selection often pitchfork/saddle-node | Expand reduced energy near Hessian zero | Would classify transition type | Requires locating event and eigenvector |
| 16 | Barrier construction | Branch stability may be kinetic | Estimate energy barrier between branches | Useful for kinetic theory | Depends on branch endpoints; not first closure step |
| 17 | Topological degree | Existence of critical points under continuation | Degree persists absent boundary escape | Proves some branch survives | Does not select optimizer branch |
| 18 | Convex relaxation | Could simplify selection | Relax nonconvex double-well/K-field energy | Fails to preserve branch physics | Shows nonconvexity is essential |
| 19 | Comparison principle | Might order centered/off-center states | Try monotone field comparison | Not applicable globally due nonlocal closure and volume constraints | No lattice order theorem available |
| 20 | Computational falsification / validation | Can identify false universal statements | exp65 lambda_rep probes | Falsifies scalar (grid,c_ref)-only classification | Cannot alone prove analytic thresholds |

## Ledger Conclusion

Methods 1-3 and 11-12 close the local analytic branch-continuation part R1-P. Methods 4-5 identify the only honest branch-transition mechanisms. Methods 6-20 show why the original universal scalar branch-selection claim is too strong and why quantitative closure requires continuation/sweep data.
