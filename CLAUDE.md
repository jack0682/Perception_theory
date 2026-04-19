# CLAUDE.md

Guidance for Claude Code working on **Soft Cognitive Cohesion (SCC)** — a mathematical theory of how coherent formations emerge prior to discrete objecthood.

## Session Start

Read in order:
1. **`THEORY/canonical/canonical.md`** — authoritative specification (v1.2, 2026-04-12). Single source of truth for the theory.
2. **`THEORY/canonical/open_problems.md`** — currently unresolved: F-1 (K=2 vacuity), M-1 (K=1 preference), MO-1 (Morse inapplicability).
3. **`THEORY/CHANGELOG.md`** — theory-side session log; last entry defines carry-forward.

For the reorganization history (what was tried and abandoned), see `AUDIT_2026-04-18.md`.

## Repository Layout

```
Perception_theory/
├── CLAUDE.md / README.md / CONVENTIONS.md / AUDIT_2026-04-18.md
│
├── CODE/                           executable assets — run from this dir
│   ├── scc/                        Python package (12 modules)
│   ├── tests/                      pytest suite (175 passing)
│   ├── experiments/                exp<N>_<name>.py + results/
│   ├── scripts/                    one-off utilities
│   ├── papers/                     LaTeX + generate_figures.py
│   └── README.md
│
├── THEORY/                         theory documents — read-oriented
│   ├── CHANGELOG.md                theory state-change log
│   ├── canonical/                  authoritative (no contamination)
│   │   ├── canonical.md            ← THE spec (v1.2)
│   │   ├── theorem_status.md       proved / conditional / open index
│   │   └── open_problems.md        F-1 / M-1 / MO-1
│   ├── working/                    in-progress theory (one file = one topic)
│   └── logs/                       chronological research journal
│       ├── daily/  YYYY-MM-DD.md
│       ├── weekly/ YYYY-Www.md
│       └── monthly/ YYYY-MM.md
│
├── private_brainstorm/             personal exploratory notes
└── _archive/                       frozen material — do not edit
    └── research_os_2026-04-12/     abandoned Research OS scaffolding
```

## Promotion Pipeline (Contamination Barrier)

```
THEORY/logs/daily/YYYY-MM-DD.md   (raw chronological record)
         ↓ reorganize by topic
THEORY/working/<topic>.md          (active theory development)
         ↓ proof + review + tests
THEORY/canonical/canonical.md      (authoritative — one-way only)
```

**canonical/ accepts only promoted content.** No reverse flow. Retractions stay explicit (inline `*(Retracted YYYY-MM-DD: reason)*`) and are logged in `THEORY/CHANGELOG.md`.

## Policy

- **Do not re-introduce Research OS structure** (numbered 00–99 dirs, 5-role daily logs, D/S/T/A/E/Q/C/P/X registry files). It was tried 2026-04-12, collapsed 2026-04-16, archived 2026-04-18.
- **`THEORY/canonical/canonical.md` is the single authoritative spec.** Any theorem-status change edits it + `theorem_status.md` + appends to `THEORY/CHANGELOG.md`.
- **No per-item registry files.** Proofs live inside canonical.md sections; theorem index lives in theorem_status.md (single file).
- **Experiments**: keep `experiments/exp<N>_*.py` numbering stable. No E-xxxx renaming.
- **Run everything from `CODE/`.** Tests and experiments locate `scc` via sys.path relative to `CODE/`.

## Test & Build

```bash
# All tests (175, ~3min)
cd CODE && python3 -m pytest tests/ -v

# Single file
cd CODE && python3 -m pytest tests/test_energy.py -v

# Smoke
cd CODE && python3 -c "from scc import *; g=GraphState.grid_2d(10,10); p=ParameterRegistry(); r=find_formation(g,p); print(r.diagnostics)"

# Experiments
cd CODE && python3 experiments/exp1_lambda_sweep.py

# Paper figures
cd CODE && python3 papers/generate_figures.py
```

## Code Architecture (scc/)

Pipeline: `graph → params → operators → energy → optimizer → diagnostics`.

- **graph.py** — `GraphState` (Laplacian, Fiedler, row-normalized P, cohesion-weighted W_sym)
- **params.py** — `ParameterRegistry` (a_cl<4, spinodal, β_crit validation)
- **operators.py** — `closure`, `distinction`, `aggregation`, `resolvent_diagonal` + exact JVPs
- **energy.py** — `EnergyComputer` (E_cl, E_sep, E_bd + exact gradients, FD-verified 1e-9)
- **optimizer.py** — `find_formation` (semi-implicit projected gradient, BB step, multi-start)
- **diagnostics.py** — `DiagnosticVector` (Bind, Sep, Inside, Persist)
- **multi.py** — K-field, `transport_k_formations` (independent/correction/reoptimize)
- **transport.py** — cohesion fingerprint, Sinkhorn log-domain OT, `persist_transport`
- **predicates.py, resolvent.py, persistence.py** — thin compatibility wrappers

### Critical Implementation Details

- E_bd smoothness: `2α·uᵀLu` → gradient `4α·Lu` (factor 4, ordered-pair sum)
- Double-well: `W'(u) = 2u(1-u)(1-2u)` (factor 2, I6 correction)
- Sep predicate: u-weighted (`Σuᵢ·Dᵢ / Σuᵢ`), NOT C_t-weighted (degenerate)
- `b_D = 0` required for analyticity (Łojasiewicz convergence)
- Persist: core-overlap (`diagnostics.py`) + transport-based `persist_transport` (`transport.py`)

## Ontological Constraints (non-negotiable)

1. **Soft cohesion field `u_t : X_t → [0,1]` is the primitive.** Crisp objects are derivative.
2. **Four energy terms (closure, separation, boundary, transport) are conceptually independent.** Do not merge.
3. **Closure has stabilization tendency (A3), not idempotence.** Deliberately omitted.
4. **Not fuzzy segmentation, not clustering, not tracking.** No engineering proxies.
5. **Never silently resolve open problems** (F-1, M-1, MO-1, co-belonging form, transition operator, crisp recovery). Keep explicit until deliberately resolved via promotion pipeline.

## Theory Sketch (v1.2)

Formal universe: `C^soft = (T, {X_t}, {u_t}, {Cl_t}, {N_t, D_t}, {M_{t→s}})`

Energy on `Σ_m = {u ∈ [0,1]^n : Σuᵢ = m}`:
`E = λ_cl·E_cl + λ_sep·E_sep + λ_bd·E_bd + λ_tr·E_tr`

Diagnostic: `d = (Bind, Sep, Inside, Persist) ∈ [0,1]⁴`

Phase transition: `β/α > 4λ₂ / |W''(c)|` with c in spinodal `((3-√3)/6, (3+√3)/6)`.

Full theorem catalog: `THEORY/canonical/canonical.md` §13.
