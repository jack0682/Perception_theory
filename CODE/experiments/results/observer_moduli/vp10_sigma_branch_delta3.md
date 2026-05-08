# VP-10 — Pseudo-Δ³ Σ_branch Map Summary

**Date:** 2026-05-08  
**Experiment:** vp10_sigma_branch_delta3.py  
**Attack:** OP-OMS-026 — full Σ_branch on Δ³  
**Caveat:** **PSEUDO-Δ³** (static scene; λ_tr-direction degenerate by Prop CW2).  
**Elapsed:** 96.8s  

## Method

Tetrahedral grid on the 3-simplex Δ³ ⊂ R^4 (4 weights summing to 1).
K = 8 → $\binom{K+3}{3} = 165$ grid points per scene.
Per-point `find_formation`, branch identifier $(n_{\mathrm{core}}, n_{\mathrm{high}})$.
Edges = unit moves in tetrahedral lattice (12 directions per interior point).
Transition edges = endpoints with different branch IDs ⇒ Σ_branch crosses the edge.

## Codim-1 evidence criterion

If Σ_branch is codim-1 in 3D Δ³, transition edges should constitute a fraction $\sim 1/K$ of all edges (the surface intersects the 1-skeleton in $O(K^2)$ edges out of $O(K^3)$ total). Fraction within $3 \times 1/K$ is taken as 'codim-1 consistent'.

## Per-scene results

### P12_path

- K = 8 → 165 grid points
- distinct branches: 7
- transition edges: 224 / 720 = 0.311
- expected codim-1 fraction (≤ 3/K): 0.375
- **codim-1 consistent: YES**

| branch (n_core, n_high) | count | fraction |
|---|---|---|
| (3, 4) | 106 | 64.24% |
| (2, 3) | 15 | 9.09% |
| (2, 4) | 15 | 9.09% |
| (0, 0) | 11 | 6.67% |
| (0, 3) | 10 | 6.06% |
| (1, 4) | 4 | 2.42% |
| (0, 4) | 4 | 2.42% |

## Conclusion

**OP-OMS-026 codim-1 part computational support:**
All scenes pass the codim-1 consistency check. Theorem SB11 (B)-(C) is COMPUTATIONALLY SUPPORTED.

**Pseudo-Δ³ caveat acknowledged.** The result tests the codim-1 structure on the simplex with $\lambda_{tr}$ included formally but degenerate. Full temporal Δ³ would require non-degenerate $E_{tr}$, achievable via `scc.multi.transport_k_formations` on a two-time-slice scene; deferred as a sub-OP.
