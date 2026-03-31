# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains the formal specification, Python implementation, and publication drafts for **Soft Cognitive Cohesion (SCC)** — a mathematical theory of how coherent formations emerge prior to discrete objecthood.

### Session Start — MANDATORY
**Every new session must read `CONVENTIONS.md` and the last entry of `CHANGELOG.md` before any file creation or modification.** These files define naming rules, directory structure, and carry-forward items from the previous session.

### Agent Teams — DEFAULT WORKFLOW
This project runs in **tmux**. For any non-trivial task (research, proof writing, experiments, multi-file edits), **spawn agent teams with tmux split panes by default**:
- Use `TeamCreate` to create a team, `TaskCreate` for task breakdown, then spawn teammates via `Agent` with `team_name` parameter.
- Each teammate runs in its own tmux pane for visibility.
- Typical team: 2-4 teammates working in parallel (e.g., proof-writer + experiment-runner + auditor).
- Task #5-style "integration" tasks should be blocked on prerequisite tasks and handled by the team lead.
- Always use `bypassPermissions` mode for teammates to avoid blocking on approvals.
- After all teammates finish, the lead integrates results, updates Canonical Spec/CHANGELOG, and cleans up the team.

### Authoritative Documents
- **Canonical Spec v2.0.md** — The authoritative formal specification (865 lines). Supersedes the original `Canonical Spec.md`.
- **Agent Instructions.md** — Binding operational protocol. Must be read before any formalization work.
- **CONVENTIONS.md** — File management rules, naming conventions, logging protocol. **Read every session.**
- **CHANGELOG.md** — Session-level change log. **Append after every session that modifies files.**

### Python Package (`scc/`)
Working implementation with 174 passing tests. Core pipeline: field → operators → energy → optimization → diagnostics.

### Papers (`papers/`)
Two LaTeX drafts (IEEEtran format): `paper1_math.tex` (math, 11 pages) and `paper2_cogsci.tex` (cognitive science, 14 pages).

### Development Record (`docs/`)
148 documents from 12 structured iterations (I1-I12), organized by date then category:
- `docs/03-26/` — Day 1: Brainstorming (I1)
- `docs/03-27/` — Day 2: Deep math through papers (I2-I10)
- `docs/03-30/` — Day 3: Comprehensive audit & repair
- `docs/03-31/` — Day 4: Transport, multi-temporal, persist analysis

Each date folder has an `INDEX.md`. Start with `docs/00-overview.md`.

## Test Fixtures

`tests/conftest.py` provides shared fixtures: `rng` (seed 42), `grid_5x5`, `grid_10x10`, `grid_20x20`, `default_params`, `bump_field_10x10` (Gaussian bump projected to Σ_m), `two_region_field` (sharp left/right). Helper `make_params(**overrides)` for custom parameter sets.

## Build & Test Commands

```bash
# Run all tests (174 tests, ~2min)
python3 -m pytest tests/ -v

# Run a single test file
python3 -m pytest tests/test_energy.py -v

# Run a specific test
python3 -m pytest tests/test_operators.py::TestA3Contraction -v

# Quick smoke test (find a formation on 10x10 grid)
python3 -c "from scc import *; g=GraphState.grid_2d(10,10); p=ParameterRegistry(); r=find_formation(g,p); print(r.diagnostics)"

# Run all experiments
python3 experiments/run_all.py

# Run individual experiments (17 total, exp1-exp17)
python3 experiments/exp1_lambda_sweep.py
python3 experiments/exp2_phase_transition.py
python3 experiments/exp3_ablation.py
python3 experiments/exp14_multi_persist.py

# Generate paper figures
python3 papers/generate_figures.py

# Compile papers (requires texlive)
cd papers && pdflatex paper1_math.tex && pdflatex paper1_math.tex
cd papers && pdflatex paper2_cogsci.tex && pdflatex paper2_cogsci.tex
```

## Code Architecture

The `scc/` package follows the theory's pipeline: `graph → params → operators → energy → optimizer → diagnostics`.

- **graph.py**: `GraphState` — wraps sparse adjacency, computes Laplacian, Fiedler eigenvalue, row-normalized P, cohesion-weighted W_sym
- **params.py**: `ParameterRegistry` — all parameters with constraint validation (a_cl < 4, spinodal range, β_crit)
- **operators.py**: `closure()`, `distinction()`, `aggregation()`, `resolvent_diagonal()` — the operator triad + exact Jacobian-transpose-vector products for gradient computation
- **energy.py**: `EnergyComputer` — E_cl, E_sep, E_bd with exact gradients (verified to FD 1e-9), Hessian spectral normalization
- **optimizer.py**: `find_formation()` — semi-implicit projected gradient descent on Σ_m with BB step size, multi-start
- **diagnostics.py**: `DiagnosticVector` — Bind (ℓ²/√n), Sep (u-weighted), Inside (H0 persistence Q_morph), Persist
- **multi.py**: K-field architecture (I9) — K coupled soft cohesion fields with simplex participation constraint, inter-formation repulsion, and `transport_k_formations` for multi-formation temporal transport (three modes: independent/correction/reoptimize; coupled transport cost with repulsion-aware OT). `inter_formation_distances`, `classify_regime`, `formation_overlap` for regime classification. T-Persist-K-Sep (well-separated) and T-Persist-K-Weak (weakly-interacting) proved.
- **transport.py**: Temporal transport kernel — cohesion fingerprint, self-referential cost, entropy-regularized partial OT (Sinkhorn log-domain), transport field application, self-referential fixed-point iteration, transport-based `persist_transport` predicate
- **predicates.py**, **resolvent.py**, **persistence.py**: Thin compatibility wrappers for tests (accept raw matrices/dicts instead of typed objects)

Key API: `find_formation(GraphState, ParameterRegistry) → FormationResult`

No `setup.py` or `pyproject.toml` — run from repo root via `python3 -m pytest` or direct imports. No install step needed.

### Critical Implementation Details
- **Ordered-pair summation**: E_bd smoothness = 2α·u^T·L·u, gradient = 4α·L·u (factor 4, not 2)
- **Double-well gradient**: W'(u) = 2u(1-u)(1-2u) — factor of 2 (I6 correction)
- **Sep predicate**: Uses u-weighted average (Σ u_i·D_i / Σ u_i), matching spec §7.1 (corrected from original C_t-weighted version in I8, which gives ~0.5 regardless)
- **Persist**: Two implementations available: (1) Core-overlap approximation in `diagnostics.py`: Σ min(u_curr, u_prev) / max(Σ u_curr, Σ u_prev) — genuine soft-field overlap measure, no transport needed. (2) Transport-based `persist_transport` in `transport.py`: core-to-core inheritance via transport kernel M_{t→s}, implementing the spec's §7.1 formula. Uses self-referential cost via cohesion fingerprint; weak-regime fixed-point converges via Banach contraction.
- **b_D = 0**: Required for energy analyticity (Łojasiewicz convergence)

## Critical Constraints

Before doing any work on this theory, read **Agent Instructions.md** in full. Key rules:

1. **Ontological priority**: The soft cohesion field `u_t : X_t -> [0,1]` is the primitive entity. Crisp objects are always derivative — never invert this.
2. **Never collapse layers**: Maintain strict separation between ontology, axiomatics, provisional operator realizations, and implementation.
3. **Never silently resolve open problems**: If the theory leaves something open (co-belonging operator form, transition operator form, crisp recovery protocol, dynamic update laws), it must stay explicitly open unless deliberately resolved.
4. **Never reduce to familiar frameworks**: The theory is not fuzzy segmentation, not clustering, not tracking. Do not substitute engineering proxies (edge detection for distinction, morphological dilation for closure, tracking IDs for persistence).
5. **Four-term energy independence**: The four energy terms (closure, separation, boundary/morphology, transport) are conceptually independent and must not be merged or collapsed.
6. **Idempotence is deliberately omitted**: Closure has a stabilization tendency (A3), not primitive idempotence. This is a foundational commitment.

## Required Work Order

Per Agent Instructions Section 5, work must proceed in this sequence:
1. Internalize conceptual motivation (why pre-objective cohesion, not objects)
2. Read and preserve the Canonical Spec
3. Normalize notation without altering concepts
4. Separate primitives from derived notions
5. Distinguish axioms from provisional operator realizations
6. Clarify energy structure
7. Record unresolved issues explicitly
8. Only then proceed to implementation-oriented work

## Theory Structure Quick Reference (v2.0)

**Formal universe**: `C^soft = (T, {X_t}, {u_t}, {Cl_t}, {N_t, C_t, D_t}, {M_{t->s}})` (T_t demoted to derived diagnostic)

**Axiomatic groups**: A (closure, A1' conditional extensivity), B (adjacency), C (co-belonging, resolvent), D (distinction, b_D=0), E (temporal transport)

**Operator pair** (variational): Self-completion (Cl_t), Self-contrast (D_t vs 1-u). **Derived diagnostic**: Self-integration (C_t resolvent, demoted from formal universe)

**Energy**: E = λ_cl·E_cl + λ_sep·E_sep + λ_bd·E_bd + λ_tr·E_tr on volume-constrained Σ_m

**Proto-cohesion diagnostic vector**: d = (Bind, Sep, Inside, Persist) ∈ [0,1]^4

**Phase transition**: β/α > 4λ₂/|W''(c)| with c in spinodal ((3-√3)/6, (3+√3)/6)

**12 fully proved results** in Canonical Spec §13 Category A (T1 existence, T6a/T6b closure fixed point, T-A2 monotonicity, T8-Core phase transition, T20 axiom consistency, T14 gradient flow, T3/T6-Stability, T7-Enhanced metastability, T11 Γ-convergence, C-Axioms, QM1–4). **Category B (proved with structural parameter):** Sep=1-E_sep/m (exact equality), Predicate-Energy Bridge (forward direction + exact equalities), T8-Full (IFT proof complete, conditional on generic non-degeneracy), T-Bind (projected form proved — tangential residual fully controlled as O((λ_bd+λ_sep)/λ_cl), mean residual r̄₀ is an explicit parameter, empirically <0.02 but not analytically bounded by KKT), T-Persist-K-Sep (well-separated multi-formation persistence, proved conditional on per-formation T-Persist-1 + well-separation WS + spectral-repulsion compatibility SR; Coupling Bound Lemma with Weyl spectral gap bound). **Conditional:** T-Persist (conditional, 5 subcomponents: a,c proved; b,d conditional; e numerically verified), T-Persist-K-Weak (weakly-interacting multi-formation persistence, conditional on joint spectral gap NB-K + overlap bound WI), C3'' (first-order, symmetrization gap). 5/5 single-formation predictions verified (P1 contraction, P2 independence, P3 enhanced dwell p=0.037, P4 path dependence, P5 Sep-before-Inside) + 3 multi-formation predictions (P1-K deep core decoupling, P2-K violation scaling, P3-K reoptimize boundary). P4-K (repulsion increases spectral gap) was retracted — experiments showed the incorrect Hessian (R_k ≠ 0 claim); revised theory uses Weyl bound μ_joint ≥ min_k(μ_k) - (K-1)λ_rep instead. See Canonical Spec §13 and `/docs/03-30/generalization/PREDICTION-VERIFICATION-COMPREHENSIVE.md`.

## Development Record (docs/)

87+ documents from 12 structured iterations. Start with `docs/00-overview.md`.

| Iter | Focus | Key Output | Score |
|------|-------|-----------|-------|
| I1 | Brainstorming (10 rounds) | 44 settled points | 6/10 |
| I2 | Deep mathematics | 12 theorems proved | 7/10 |
| I3 | Implementation design | Algorithm + module specs | 7/10 |
| I4 | Extensions | Gestalt mapping, 10 predictions | 7/10 |
| I5 | Vulnerability audit | 17 vulnerabilities found | 6.5/10 |
| I6 | Spec rewrite | Canonical Spec v2.0 | 7.5/10 |
| I7 | Temporal theory | T-Persist-1, Sep identity | 8/10 |
| I8 | Code + experiments | scc/ package, 89 tests | 8.5/10 |
| I9 | Multi-formation | K-field architecture decided | 9/10 |
| I10 | Publication | 2 paper outlines + drafts | 9/10 |
| I11 | Transport implementation | transport.py, 3 experiments, T-Persist verified, multi-formation temporal (well-separated) | 8.5/10 |
| I12 | Multi-temporal | T-Persist-K-Sep/Weak, regime classification, coupled transport | - |

## Required Deliverables (when formalizing)

Any formalization work must produce: notation-consistent formal spec, primitive/derived concept registry, operator catalogue, energy-term explanation sheet, unresolved-issues register. Implementation specs are downstream and must be clearly labeled as such.
