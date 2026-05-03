# Soft Cognitive Cohesion (SCC)

A mathematical theory of how coherent formations emerge **prior to discrete objecthood** — before the world is parsed into separately-identified things.

**Central claim**: cohesive formation is a graded, self-referentially evaluated structural state that is formally richer than, and not reducible to, discrete objecthood. Objects are a distinguished limit of the formation space, not its starting point.

---

## Theory in One Page

The primitive entity is a **soft cohesion field** $u_t : X_t \to [0,1]$ over a relational support space. $u_t(x)$ is the degree to which site $x$ participates in a cohesive formation — not a probability, not a segmentation mask.

**Formal universe:**

$$\mathfrak{C}^{\mathrm{soft}} = \Big( T,\ \{X_t\},\ \{u_t\},\ \{\mathrm{Cl}_t\},\ \{\mathbf{N}_t, \mathbf{D}_t\},\ \{\mathbf{M}_{t \to s}\} \Big)$$

**Operator triad** (variational):
- $\mathrm{Cl}_t$ — self-completion (closure)
- $\mathbf{D}_t$ — self-contrast (distinction)
- $\mathbf{C}_t$ — self-integration (co-belonging resolvent): **derived diagnostic, not primitive**

**Energy** on volume-constrained simplex $\Sigma_m = \{u \in [0,1]^n : \sum u_i = m\}$:

$$E = \lambda_{\mathrm{cl}} E_{\mathrm{cl}} + \lambda_{\mathrm{sep}} E_{\mathrm{sep}} + \lambda_{\mathrm{bd}} E_{\mathrm{bd}} + \lambda_{\mathrm{tr}} E_{\mathrm{tr}}$$

**Proto-cohesion diagnostic** $\mathbf{d} = (\mathrm{Bind},\ \mathrm{Sep},\ \mathrm{Inside},\ \mathrm{Persist}) \in [0,1]^4$

**Phase transition:** $\beta/\alpha > 4\lambda_2 / |W''(c)|$ with $c$ in spinodal $((3-\sqrt{3})/6,\ (3+\sqrt{3})/6)$.

Full formal specification: **`THEORY/canonical/canonical.md`** (v1.2).

---

## Repository Layout

```
CLAUDE.md / README.md / CONVENTIONS.md / AUDIT_2026-04-18.md

CODE/                  executable — run everything from here
├── scc/               Python package (12 modules, 3198 LOC)
├── tests/             175 passing tests
├── experiments/       exp1 ~ exp82 + results/
├── scripts/           utilities
├── papers/            LaTeX sources + generate_figures.py
└── README.md

THEORY/                theory documents
├── CHANGELOG.md       theory state-change log
├── canonical/         authoritative — promoted content only
│   ├── canonical.md   ← THE spec (v1.2, 1216 lines)
│   ├── theorem_status.md
│   └── theorem_status.md
├── working/           in-progress theory (one file = one topic)
└── logs/              chronological journal
    ├── daily/ weekly/ monthly/

private_brainstorm/    personal notes
_archive/              frozen material (includes abandoned Research OS)
```

### Promotion Pipeline (one-way flow)

```
logs/daily/  →  working/<topic>.md  →  canonical/canonical.md
(raw journal)    (active work)          (authoritative — no return)
```

canonical/ is protected from contamination by this unidirectional flow. Retractions remain explicit, never silent.

---

## Quickstart

```bash
# Smoke
cd CODE && python3 -c "from scc import *; g=GraphState.grid_2d(10,10); p=ParameterRegistry(); r=find_formation(g,p); print(r.diagnostics)"

# All tests (175, ~3min)
cd CODE && python3 -m pytest tests/ -v

# Single experiment
cd CODE && python3 experiments/exp1_lambda_sweep.py

# Paper figures
cd CODE && python3 papers/generate_figures.py

# Compile papers (requires texlive)
cd CODE/papers && pdflatex paper1_math.tex && pdflatex paper1_math.tex
```

---

## Current Status (v1.2, 2026-04-12)

**Proved (Category A):** T1 existence, T6a/T6b closure FP, T-A2 monotonicity, T8-Core & T8-Full phase transition, T20 axiom consistency, T14 gradient flow, T3/T6-Stability, T7 metastability, T11 Γ-convergence, C-Axioms, QM1–4, Predicate-Energy Bridge, Deep Core Dom. 2b, auxiliary results.

**Proved structural (Category B):** T-Bind-Proj/Full, T-Persist-K-Sep.

**Conditional (Category C):** T-Persist-1 subcomponents, T-Persist-K-Weak, T-Persist-K-Unified.

**Retracted:** K-Saddle Conjecture, Theorem 3.3 (r̄₀ general τ), **Type A/B classification** (exp65: 0/4 configs observed as Type B).

**Open critical:** F-1 (K=2 vacuity), M-1 (K=1 always preferred), MO-1 (Morse inapplicable under fixed-K). See `THEORY/canonical/theorem_status.md`.

**Predictions verified:** P1–P5 (single-formation), P1-K/P2-K/P3-K (multi-formation). P4-K retracted.

---

## Critical Implementation Notes

- **Factor 4 in ∇E_bd:** `4α·Lu` (ordered-pair summation, not 2)
- **Double-well gradient:** `W'(u) = 2u(1-u)(1-2u)` (factor 2, I6 correction)
- **Sep predicate:** u-weighted `Σuᵢ·Dᵢ / Σuᵢ` — C_t-weighted form gives ≈0.5 regardless
- **b_D = 0:** required for analyticity (Łojasiewicz convergence)
- **Persist:** core-overlap in `diagnostics.py` + transport-based `persist_transport` in `transport.py`

---

## What This Is Not

Not fuzzy segmentation, not clustering, not tracking. Substituting engineering proxies (edge detection for distinction, morphological dilation for closure, tracking IDs for persistence) dissolves the ontological commitments that give the theory its content. The four energy terms are conceptually independent and must not be merged. Idempotence of closure is deliberately omitted — closure has a stabilization tendency (A3), not primitive idempotence.
