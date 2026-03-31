# Soft Cognitive Cohesion (SCC)

A mathematical theory of how coherent formations emerge **prior to discrete objecthood** — before the world is parsed into separately-identified things.

The central claim: cohesive formation is a graded, self-referentially evaluated structural state that is formally richer than, and not reducible to, discrete objecthood. Objects are a distinguished limit of the formation space, not its starting point.

---

## Theory in One Page

The primitive entity is a **soft cohesion field** $u_t : X_t \to [0,1]$ over a relational support space. The value $u_t(x)$ is the degree to which site $x$ participates in a cohesive formation — not a probability, not a segmentation mask.

**Formal universe:**

$$\mathfrak{C}^{\mathrm{soft}} = \Big( T,\ \{X_t\},\ \{u_t\},\ \{\mathrm{Cl}_t\},\ \{\mathbf{N}_t, \mathbf{D}_t\},\ \{\mathbf{M}_{t \to s}\} \Big)$$

**Operator triad** (variational):
- $\mathrm{Cl}_t$ — Self-completion (closure): spreads cohesion along relational support
- $\mathbf{D}_t$ — Self-contrast (distinction): suppresses cohesion where the field contrasts with its exterior
- $\mathbf{C}_t$ — Self-integration (co-belonging resolvent): derived diagnostic, not a primitive

**Energy** on volume-constrained simplex $\Sigma_m = \{u \in [0,1]^n : \sum u_i = m\}$:

$$E = \lambda_{\mathrm{cl}} E_{\mathrm{cl}} + \lambda_{\mathrm{sep}} E_{\mathrm{sep}} + \lambda_{\mathrm{bd}} E_{\mathrm{bd}} + \lambda_{\mathrm{tr}} E_{\mathrm{tr}}$$

**Proto-cohesion diagnostic vector** $\mathbf{d} = (\mathrm{Bind},\ \mathrm{Sep},\ \mathrm{Inside},\ \mathrm{Persist}) \in [0,1]^4$

**Phase transition condition:**

$$\frac{\beta}{\alpha} > \frac{4\lambda_2}{|W''(c)|}$$

with $c$ in the spinodal range $\left(\frac{3-\sqrt{3}}{6},\ \frac{3+\sqrt{3}}{6}\right)$.

---

## Repository Structure

```
Canonical Spec v2.0.md   # Authoritative formal specification (865 lines)
Agent Instructions.md    # Binding operational protocol
CONVENTIONS.md           # File management & naming rules
CHANGELOG.md             # Session-level change log

scc/                     # Python implementation
  graph.py               # GraphState — Laplacian, Fiedler, row-normalized P
  params.py              # ParameterRegistry — constraint validation
  operators.py           # closure(), distinction(), aggregation(), resolvent_diagonal()
  energy.py              # EnergyComputer — E_cl, E_sep, E_bd with exact gradients
  optimizer.py           # find_formation() — semi-implicit projected gradient descent
  diagnostics.py         # DiagnosticVector — Bind, Sep, Inside, Persist
  multi.py               # K-field architecture for multi-formation
  transport.py           # Temporal transport kernel, Sinkhorn OT, persist_transport

tests/                   # 174 tests
experiments/             # exp1–exp24 (exp24 unfinished)
papers/                  # paper1_math.tex (math, ~11p), paper2_cogsci.tex (cogsci, ~14p)
docs/                    # 148+ development documents, 12 iterations (I1–I12)
  03-26/                 # Day 1: Brainstorming (I1)
  03-27/                 # Day 2: Deep math through papers (I2–I10)
  03-30/                 # Day 3: Comprehensive audit & repair
  03-31/                 # Day 4: Transport, multi-temporal, persist analysis
```

---

## Quickstart

No install step. Run from repo root.

```bash
# Quick smoke test
python3 -c "from scc import *; g=GraphState.grid_2d(10,10); p=ParameterRegistry(); r=find_formation(g,p); print(r.diagnostics)"

# Run all tests (~2 min)
python3 -m pytest tests/ -v

# Run a single test file
python3 -m pytest tests/test_energy.py -v

# Run all experiments
python3 experiments/run_all.py

# Generate paper figures
python3 papers/generate_figures.py

# Compile papers (requires texlive)
cd papers && pdflatex paper1_math.tex && pdflatex paper1_math.tex
cd papers && pdflatex paper2_cogsci.tex && pdflatex paper2_cogsci.tex
```

---

## Theorem Status (as of 2026-03-31)

**Category A — Fully proved:** T1 (existence), T6a/T6b (closure fixed point), T-A2 (monotonicity), T8-Core (phase transition), T20 (axiom consistency), T14 (gradient flow), T3/T6-Stability, T7 (enhanced metastability), T11 (Γ-convergence), C-Axioms, QM1–4.

**Category B — Proved with structural parameter:** $\mathrm{Sep} = 1 - E_{\mathrm{sep}}/m$ (exact equality), Predicate-Energy Bridge, T8-Full (IFT, conditional on generic non-degeneracy), T-Bind (projected form), T-Persist-K-Sep (well-separated multi-formation persistence).

**Conditional:** T-Persist-1 (subcomponents a,c proved; b corrected to away-from-bifurcation; e proved via Schauder), T-Persist-K-Weak (weakly-interacting regime).

**Open:** Near-bifurcation persistence, strong-regime fixed-point uniqueness, T-Persist-K-Strong (conjectured), barrier scaling exponent $\Delta_{\mathrm{soft}} \sim \mu^{0.32}$.

**Predictions verified:** P1–P5 (single-formation), P1-K/P2-K/P3-K (multi-formation). P4-K retracted after experiments showed incorrect Hessian assumption.

---

## Critical Implementation Notes

- **Factor 4 in $E_{\mathrm{bd}}$ gradient:** $\nabla E_{\mathrm{bd}} = 4\alpha L u$ (ordered-pair summation convention, not factor 2)
- **Double-well gradient:** $W'(u) = 2u(1-u)(1-2u)$ — factor of 2 (I6 correction)
- **Sep predicate:** $u$-weighted average $\sum u_i D_i \,/\, \sum u_i$ — $\mathbf{C}_t$-weighted form gives $\approx 0.5$ regardless (degenerate)
- **$b_D = 0$:** Required for energy analyticity (Łojasiewicz convergence)
- **Persist:** Two implementations — core-overlap approximation in `diagnostics.py`, transport-based `persist_transport` in `transport.py`

---

## What This Is Not

The theory is not fuzzy segmentation, not clustering, not tracking. Substituting engineering proxies (edge detection for distinction, morphological dilation for closure, tracking IDs for persistence) would dissolve the ontological commitments that give the theory its content. The four energy terms are conceptually independent and must not be merged. Idempotence of closure is deliberately omitted — closure has a stabilization tendency (A3), not primitive idempotence.
