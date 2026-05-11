---
type: working/afd
status: AFD-0 Draft (2026-05-12)
---

# Framework Comparison for AFD

Comparison of 15 candidate mathematical frameworks that AFD-0 might draw on, build with, or be compared against. Ranked roughly by relevance to AFD-0 (Layer 2). Each row notes the framework's degeneracy tolerance, H-MORSE dependence, fit with AFD-0, risks, and priority for AFD development.

## Summary Table

| # | Framework | SCC role | Handles degeneracy? | Needs H-MORSE? | Best use in AFD | Risk | Priority |
|---|---|---|---|---|---|---|---|
| 1 | Łojasiewicz gradient flow | Layer 1 (T14 Cat A) | Yes (handles analytic E) | No | Basin AFD-D2 definition | None | Already used |
| 2 | Freidlin-Wentzell large deviations | Layer 2 ↔ 3 bridge | Partial (needs gradient SDE) | No (for exponent) | Bar(F_i, F_j) ≡ quasipotential | OP-AFD-005 | **High** |
| 3 | Eyring-Kramers (Bovier-Eckhoff-Gayrard) | Layer 3 | **No** (requires Morse) | **Yes** | EK refinement of AFD edges | H-MORSE Cat B target | **High** (Layer 3) |
| 4 | Conley index theory | Layer 2 extension | **Yes** (intrinsically) | No | AFD-1 / AFD-Conley replacement of reps by isolated invariant sets | Heavy machinery; specialist knowledge | Medium (deferred) |
| 5 | Persistence stability (CSEH 2007) | Layer 1 (QM3) | Yes (vineyard set codim-1) | No | τ stability AFD-D11 | None (Cat A external) | Already used |
| 6 | Whitney / Thom stratifications | Layer 2 regularity question | Yes if applied carefully | No | Upgrade S_K to proper stratum | OP-AFD-002 | Medium |
| 7 | Morse-Bott theory | Layer 3 generalization | Yes (allows degenerate sub-manifolds) | Partial (requires Bott-nondeg along orbit) | Goldstone family Layer-3 treatment | Adapts EK to symmetric cases | Medium |
| 8 | Reflected Langevin / Lions-Sznitman | Layer 1 (Pkg I Cat A) | Yes (convex polytope) | No | AFD-D2' stochastic basin | None (Cat A) | Already used |
| 9 | Quasi-stationary distributions | Layer 2 ↔ 3 | Partial | No (for existence); yes (for asymptotics) | AFD-D2' basin definition | Asymptotic identification needs Layer 3 | Medium |
| 10 | Łojasiewicz inequality (analytic-set theoretic) | Layer 1 (via T14) | Yes (general analytic case) | No | Convergence rate refinement | Constants graph-dependent | Low |
| 11 | Cheeger-type spectral / isoperimetric inequalities | Layer 1 ⊕ 2 quantitative input | Yes | No | Quantitative lower bounds on Bar | Constants are loose for SCC | Low |
| 12 | Cluster expansion / sector decomposition | Layer 2 (D-ST-4) | Yes (set-theoretic) | No | K-stratum / sector formalization | Already in stereo-SCC | Already partially used |
| 13 | Bovier-den Hollander metastability framework | Layer 3 quantitative | Partial | Yes (for sharp prefactor) | Sharp EK formula | Same risks as #3 | High (Layer 3) |
| 14 | Hamilton-Jacobi / viscosity-solution methods | Layer 2 alternative cost theory | Yes | No | Alternative formulation of C_AFD via value function | Heavy PDE machinery on graphs | Low |
| 15 | Markov chain lumpability / coarse-graining | Layer 3 → Layer 2 reduction | Partial | Yes (for asymptotic rate Markov) | OP-AFD-006 Markov chain on V_form | Lumpability is non-trivial without strong gaps | Medium |

## Prose analysis (per framework)

### 1. Łojasiewicz gradient flow

Already canonical in SCC as T14 (Cat A). Provides gradient-flow convergence to a critical point for any analytic E on a compact analytic manifold, including degenerate critical points. This is exactly what AFD-D2 needs to make B_det well-defined. There is no degeneracy obstruction.

### 2. Freidlin-Wentzell large deviations

The natural Layer-2 ↔ Layer-3 bridge. For gradient SDEs, FW quasipotential V(u_F_i^*, u_F_j^*) = Bar(F_i, F_j) — this identification is the technical heart of AFD-T8. FW theory itself is standard for SDEs on Euclidean space; the reflected-Langevin case on convex polytopes requires the literature gap noted in `CV114_H_MORSE_PACKAGEII/06_packageII_dependency_map.md` §2.5. Critical for AFD-0 OP-AFD-005.

### 3. Eyring-Kramers (Bovier-Eckhoff-Gayrard)

The Layer-3 prefactor theory. Bovier-Eckhoff 2003 + Bovier-Gayrard-Klein 2005 establish the sharp prefactor for reflected diffusions on appropriate domains. The H-MORSE-Local + H-MORSE-Saddle hypotheses are intrinsic to this framework (the prefactor is a Hessian-determinant ratio). When H-MORSE holds, EK exactly recovers the AFD ordering and supplies the prefactor; when H-MORSE fails, EK is not applicable and AFD-T10 strategies kick in.

### 4. Conley index theory

The most principled handling of degenerate dynamics. Replaces the notion of "critical point" by "isolated invariant set" and "Morse decomposition" by "Conley-Morse digraph." Conley index is invariant under continuous deformation and handles symmetric/degenerate critical sets gracefully. Recommended for AFD-1 / AFD-Conley as the natural foundation for OP-AFD-009 and as the principled answer to the degeneracy catalogue in `CV114_H_MORSE_PACKAGEII/04_degeneracy_catalogue.md`.

### 5. Persistence stability (CSEH 2007)

External Cat A input. Bottleneck stability d_B(τ(u), τ(v)) ≤ ‖u − v‖_∞ is the unique reason AFD-D11 / AFD-T2 work without ad-hoc smoothing. Already used; no risk.

### 6. Whitney / Thom stratifications

The natural framework for OP-AFD-002. To call S_K a "stratum" in any sense beyond set-theoretic, we need either Whitney regularity (Whitney's conditions A and B at stratum boundaries) or Thom transversality. The vineyard set V is semi-algebraic; under definability hypotheses, a Whitney stratification exists. The proof would upgrade AFD-D12 from "set-theoretic decomposition" to "Whitney-stratified decomposition," sharpening AFD-T3.

### 7. Morse-Bott theory

Generalizes Morse to nondegenerate critical sub-manifolds. Bott-nondegeneracy: the Hessian is nondegenerate on the normal bundle of the critical sub-manifold. This handles Goldstone-like degeneracies (the zero eigenvalues are exactly along the orbit). For SCC, when the Aut(G)-orbit of a minimizer is the critical set, Morse-Bott gives the natural Layer-3 treatment: the EK prefactor becomes an integral over the orbit weighted by the normal Hessian. Best fit for Example 7 (D_4 symmetric formations) at Layer 3.

### 8. Reflected Langevin / Lions-Sznitman

Already Cat A as Package I (CV-1.8–1.9). T-PF-A1-SDE provides the well-posed reflected SDE on the convex polytope Σ_m. T-PF-A1-GI + PE provide Gibbs invariance and Poincaré ergodicity. This is the canonical stochastic substrate for AFD-D2' and §11. No degeneracy issue.

### 9. Quasi-stationary distributions

A QSD on a basin is the unique nonneg measure that decays exponentially in time under the killed-on-exit dynamics. Used in AFD-D2' as the rigorous definition of stochastic basin. Existence holds under mild conditions (Champagnat-Villemonais). Asymptotic identification with the Gibbs restricted measure requires Layer 3 (small-noise / metastability).

### 10. Łojasiewicz inequality

Provides the analytic-set-theoretic backbone of T14. Could give quantitative convergence rates under additional analytic-class hypotheses on E. Low priority because T14 already gives qualitative convergence (which is what AFD needs).

### 11. Cheeger / spectral / isoperimetric inequalities

Provides quantitative lower bounds on energy barriers via spectral gap arguments. The Cheeger constant of (Σ_m, E) lower-bounds the rate of mixing and, indirectly, barriers. Could feed into OP-AFD-004 as an alternative analytic route to positive merge barriers. Constants are typically loose; T7-Enhanced is sharper for SCC.

### 12. Cluster expansion / sector decomposition

The stereo-SCC framework (D-ST-1..D-ST-5) already uses sector decomposition: each (K, α)-sector B_K(P) is a topological + energy basin. AFD-D12 is the non-stereo analogue. Cluster expansion (statistical-mechanics style) could provide quantitative low-temperature expansion of the Gibbs measure π_{T_*} that refines AFD-T8.

### 13. Bovier-den Hollander metastability framework

The complete sharp-asymptotic metastability framework (capacity / Dirichlet-form / potential-theoretic approach). Provides sharp constants for mean exit times and refined EK formulae. Subsumes #3 with cleaner proofs. Same H-MORSE dependence. Recommended Layer-3 reference for the AFD-T8 full proof (OP-AFD-005).

### 14. Hamilton-Jacobi / viscosity solutions

An alternative formulation of C_AFD as the viscosity solution of a Hamilton-Jacobi equation on Σ_m. On graphs, this becomes a discrete Hamilton-Jacobi / monotone scheme. Heavy machinery, low priority unless OP-AFD-003 (attainment of the inf) is approached via this route.

### 15. Markov chain lumpability / coarse-graining

The coarse-grained process Π_t = F_i (basin assignment) is Markov when the underlying microscopic process satisfies lumpability conditions (Kemeny-Snell). In the small-noise limit + H-MORSE, Bovier metastability proves Π_t is asymptotically Markov on V_form with rates given by EK (= refined AFD-T8). This is OP-AFD-006. Without H-MORSE, lumpability is delicate.

## Recommendations for AFD-0

- **Immediate use (Layer 1 Cat A, no new framework):** #1 (Łojasiewicz), #5 (CSEH), #8 (reflected Langevin). All already canonical, no architectural risk.
- **Critical Layer-2 ↔ 3 bridge:** #2 (FW). Drive OP-AFD-005.
- **Reserve for AFD-1:** #4 (Conley). Required for OP-AFD-009 and the AFD-T10 Design Principle's full execution.
- **Regularity upgrade for AFD-T3 / AFD-D12:** #6 (Whitney stratification). Drive OP-AFD-002.
- **Layer-3 prefactor (when CV-1.14 H-MORSE-Local lands):** #3, #7, #13. Combined Morse + Morse-Bott + Bovier-den Hollander treatment of EK on Σ_m.
- **Low priority / optional:** #10, #11, #14.
- **Medium priority post AFD-0:** #9, #12, #15.
