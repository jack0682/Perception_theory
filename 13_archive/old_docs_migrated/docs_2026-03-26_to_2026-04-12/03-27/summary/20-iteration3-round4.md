# Iteration 3 — Round 4: Core Algorithm and Software Architecture

**Date:** 2026-03-27
**Iteration:** 3 (Implementation)
**Theme:** Projected gradient flow on Ω_m + complete module design

---

## Key Decisions (from Synthesis)

1. **Facade pattern:** FindFormation orchestrator over 6 pure-function modules
2. **R10 verification is Priority 1** — determines narrative and parameter strategy
3. **C_t is diagnostic only, NOT in energy gradient** — Sep_new monitors but doesn't drive gradient
4. **Sep_new only needs resolvent diagonal** — O(k·n) not O(k·n²)
5. **Three-phase roadmap:** Foundation → Optimization → Exploration

## Algorithm (Algo Designer)

Semi-implicit gradient flow: (I + Δτ·4αλ_bd·L)u^{k+1} = u^k - Δτ·[explicit terms]
- Fiedler eigenvector initialization seeds dominant instability mode
- Armijo backtracking line search
- Convergence: gradient norm + diagnostic vector dual criterion
- Scaling: n=10⁶ feasible in ~20s

## Architecture (Systems Engineer)

9 modules: ParameterRegistry → Aggregation → Closure → Distinction → CoBelonging → EnergyComputer → Projector → Optimizer → DiagnosticVector

All data types specified: GraphState, OperatorOutputs, EnergyResult, DiagnosticResult, ParameterSet. Complete YAML config schema. Gradient formulas verified:
- ∇E_cl = 2·(I - J_Cl)ᵀ · (u - Cl(u))
- ∇E_sep = (1 - D) - J_Dᵀ · u
- ∇E_bd = 4α·Lu + β·W'(u)

## Experiments (Experiment Designer)

7 experiments designed with 2,240 total runs. Critical ablation (6 energy configs) resolves R10. Phase transition verification at β* = 4λ₂/|W''(c)|. Statistical protocol: 10 seeds, Wilcoxon, Bonferroni.

## Files

- `I3-R4-algo-designer.md` — Complete algorithm pseudocode
- `I3-R4-sys-engineer.md` — Full module architecture with code
- `I3-R4-experiment-design.md` — 7 experiments with predictions
- `I3-R4-synthesis.md` — Integration synthesis
