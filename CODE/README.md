# CODE/

Executable assets for Soft Cognitive Cohesion (SCC). **Run everything from this directory** (`cd CODE && ...`), since tests and experiments locate `scc` via sys.path relative to `CODE/`.

## Contents

```
scc/          Python package (12 modules)
tests/        pytest suite (175 passing)
experiments/  exp<N>_<name>.py + results/
scripts/      one-off utilities
papers/       LaTeX sources + generate_figures.py
```

## Commands

```bash
# All tests (~3 min)
cd CODE && python3 -m pytest tests/ -v

# Single test file
cd CODE && python3 -m pytest tests/test_energy.py -v

# Smoke
cd CODE && python3 -c "from scc import *; g=GraphState.grid_2d(10,10); p=ParameterRegistry(); r=find_formation(g,p); print(r.diagnostics)"

# Experiments (most auto-set sys.path defensively)
cd CODE && python3 experiments/exp1_lambda_sweep.py

# Paper figures
cd CODE && python3 papers/generate_figures.py

# Compile papers (requires texlive)
cd CODE/papers && pdflatex paper1_math.tex && pdflatex paper1_math.tex
```

## scc/ Modules

- **graph.py** — `GraphState` (Laplacian, Fiedler, row-normalized P, W_sym)
- **params.py** — `ParameterRegistry` with constraint validation
- **operators.py** — `closure`, `distinction`, `aggregation`, `resolvent_diagonal` + JVPs
- **energy.py** — `EnergyComputer` (E_cl, E_sep, E_bd + exact gradients, FD-verified 1e-9)
- **optimizer.py** — `find_formation` (semi-implicit projected gradient, BB step, multi-start)
- **diagnostics.py** — `DiagnosticVector` (Bind, Sep, Inside, Persist)
- **multi.py** — K-field architecture, `transport_k_formations` (3 modes)
- **transport.py** — cohesion fingerprint, Sinkhorn log-domain OT, `persist_transport`
- **predicates.py, resolvent.py, persistence.py** — thin compatibility wrappers

Key API: `find_formation(GraphState, ParameterRegistry) → FormationResult`

## Known Technical Debt

- `scripts/m2_landscape.py:15`, `m2_landscape_v2.py:5` — dead `/home/jack/ex` path
- `experiments/exp25_hessian_diagonal.py:12`, `exp63_hessian_mass_transfer.py:23`, `exp21_gap_structural_analysis.py:13`, `exp33_delta_bdy_formula.py:23`, `exp_cohesion_scale_gpu.py:23` — hardcoded paths (already broken pre-move)

These do not affect the main test/experiment pipeline. Fix on demand.

## Links

- Theory: `../THEORY/canonical/canonical.md`
- Project orientation: `../CLAUDE.md`
- Conventions: `../CONVENTIONS.md`
