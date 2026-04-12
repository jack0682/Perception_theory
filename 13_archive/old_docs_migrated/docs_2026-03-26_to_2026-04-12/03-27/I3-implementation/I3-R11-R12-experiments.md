# Iteration 3 R11-R12 — Experiment Designer: Benchmarks + Scalability

**Author:** Experiment Designer | **Iteration:** 3, Rounds 11-12

## R11: Benchmarks (SCC vs Standard Methods)
4 test fields × 5 methods (SCC, Allen-Cahn, spectral, fuzzy C-means, level-set) × 3 seeds = 60 runs.

**Key prediction:** SCC uniquely satisfies ALL FOUR proto-cohesion components. Each competitor fails ≥1: AC fails Sep, spectral fails Bind, FCM fails Inside, level-set fails Persist.

Budget: ~2 hours.

## R12: Scalability
N from 100 to 1M. Profile per-term costs.

**Key predictions:**
- E_bd, E_cl: O(N·deg) — linear, fine
- C_t exact: O(N³) — bottleneck > N=1K. Neumann K=5: O(N·deg·K) — linear
- Neumann K=5 gives <5% Sep error up to N=100K
- Convergence steps roughly constant in N
- **Bottleneck at N=1M: E_sep if naive (O(N²) pairwise)**

Targets: N=10K in <1min/step, N=100K in <10min/step.

Budget: ~4 hours.
