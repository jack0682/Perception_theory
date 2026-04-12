# Iteration 3 R4 — Experiment Designer: Core Algorithm Validation

**Author:** Experiment Designer
**Date:** 2026-03-27
**Iteration:** 3 (Implementation), Round 4

---

## Experiment 1: Does the Optimizer Find Formations?

### Setup
- Grids: 5×5, 10×10, 20×20, 50×50
- β sweep: 0.5, 1, 2, 5, 10, 20, 50, 100 (α=1)
- Volume: c = 0.3, 0.4, 0.5, 0.6, 0.7
- Initializations: random uniform, perturbed uniform, structured (Gaussian bump)
- 10 random seeds per configuration

### Critical Ablation: Energy Term Contribution (Resolves R10)

| Experiment | λ_cl | λ_sep | λ_bd | Purpose |
|-----------|------|-------|------|---------|
| BD-only | 0 | 0 | 1 | Pure Allen-Cahn |
| BD+CL | 1 | 0 | 1 | AC + closure |
| BD+SEP | 0 | 1 | 1 | AC + separation |
| Full-SCC | 1 | 1 | 1 | Complete |
| SEP-dominant | 0 | 10 | 1 | Test R10 |
| SEP-only | 0 | 1 | 0 | Separation alone |

### Success Criteria
- Minimum: 10×10, β=10, c=0.5 → Bind≥0.9, Sep≥0.8, Inside≥0.5 (8/10 seeds)
- Strong: Phase transition at β* matches 4λ₂/|W''(c)| ± 20%
- Breakthrough: Consistent formations on 50×50

## Experiment 2: C_t Scalability

- Methods: exact resolvent, sparse solve, CG, Neumann K={5,10,20,50,100}
- Grids: 5×5 to 100×100
- Accuracy: <1% diagonal error, discrimination ratio preserved
- Integration: approximate C_t in optimization loop

## 7 Total Experiments Designed (Ranked Priority)

1. Ablation study (resolves R10)
2. Basic optimizer validation
3. C_t scalability
4. R10 verification on Σ_m
5. C_t integration test
6. Phase transition verification
7. SCC vs Allen-Cahn head-to-head
