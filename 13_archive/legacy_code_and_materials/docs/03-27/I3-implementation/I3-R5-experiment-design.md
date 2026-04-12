# Iteration 3 R5 — Experiment Designer: C_t Scalability

**Author:** Experiment Designer
**Date:** 2026-03-27
**Iteration:** 3, Round 5

---

## POTENTIALLY GAME-CHANGING FINDING: P-C3

**C_t may be diagnostic-only.** The Canonical Spec energy E_sep = Σ u(x)(1-D(x;1-u)) does NOT contain C_t. C_t appears only in the Sep PREDICATE, not in the energy. If confirmed, C_t computation is NOT needed during optimization — only for post-hoc diagnostic evaluation. This reduces C_t from "bottleneck" to "negligible."

## 5 SUB-EXPERIMENTS (2,570 total runs)

| Sub-Exp | Objective | Configurations |
|---------|-----------|---------------|
| 2A | Scalability ceiling per method | 1,800 runs |
| 2B | Neumann K* tradeoff | 480 runs |
| 2C | Integration test (C_t in optimizer) | 120 runs |
| 2D | Gradient test (is C_t in ∂E/∂u?) | 20 runs |
| 2E | α sensitivity | 150 runs |

## KEY PREDICTIONS

- P-C1: Neumann K=10-15 suffices for α/α_max ≤ 0.7
- P-C2: Diagonal-only enables 100×100 grids
- P-C3: C_t is diagnostic-only (NOT in ∂E/∂u)
- P-C6: 1000× discrimination survives K≥10 truncation
- P-C7: α=0.5-0.7 is optimal operating range

## RECOMMENDED PRODUCTION CONFIG

| Grid | Method | K | α/α_max | Update | Sep Error |
|------|--------|---|---------|--------|-----------|
| ≤20² | Exact sparse | — | 0.7 | Every 50 steps | <0.1% |
| 20-50 | Neumann | 15 | 0.7 | Lazy Δu=0.01 | <1% |
| 50-100 | Neumann diag | 15 | 0.5 | Lazy Δu=0.01 | <2% |
| >100 | Neumann diag | 10 | 0.5 | Every 100 steps | <5% |
