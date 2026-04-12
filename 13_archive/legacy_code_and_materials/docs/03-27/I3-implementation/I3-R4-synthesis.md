# Iteration 3 — Round 4: Implementation Synthesis

**Author:** Implementation Synthesizer
**Date:** 2026-03-27
**Inputs:** Algorithm Designer R4, Systems Engineer R4, Experiment Designer R4
**Scope:** Unified implementation roadmap for computational realization of SCC

---

## I. EXECUTIVE SUMMARY

Three independent positions converge on a feasible computational realization of SCC's static theory. The core algorithm (projected semi-implicit gradient flow on Σ_m), the architecture (3-layer, 6-module), and the validation plan (7 experiments with statistical protocol) are broadly compatible. One structural tension — monolithic pipeline vs. modular decomposition — is resolved below through a **facade pattern**: modular internals with a pipeline-level orchestrator.

**The single most important implementation outcome for Iteration 3:** Rigorous verification or falsification of the R10 separation-dominance hypothesis. Everything else — phase diagrams, scalability, parameter sensitivity — is downstream of knowing whether the theory's instability structure is separation-driven or Allen-Cahn-driven. This determines the parameter regime, the narrative, and the computational priorities.

---

## II. CROSS-POSITION AGREEMENT REGISTRY

All three positions independently converged on these decisions. These are **settled** for implementation.

| # | Agreement | Algo | Sys | Exp | Mathematical Basis |
|---|-----------|------|-----|-----|-------------------|
| 1 | Volume constraint mandatory | ✓ | ✓ | ✓ | T8-Core requires Σ_m; without it, u≡0 is global min (R4-R5) |
| 2 | Automatic λ normalization | ✓ | ✓ | ✓ | R10 caveat 1: quantitative claims are parameter-dependent |
| 3 | Resolvent C_t, never Cesàro | ✓ | ✓ | ✓ | Cesàro destroys pairwise info (R6, FALSE claim #4) |
| 4 | b_D = 0 for energy analyticity | ✓ | ✓ | ✓ | Łojasiewicz (T14) requires analytic energy |
| 5 | R10 verification is Priority 1 | ✓ | ✓ | ✓ | R13 caveats: normalization, volume constraint, sign conventions |
| 6 | Single-formation, 2D grid first | ✓ | ✓ | ✓ | Multi-formation blocked by contraction regime |
| 7 | Semi-implicit time stepping | ✓ | ✓ | — | Stiff Laplacian in E_bd requires implicit treatment |
| 8 | Python + NumPy/SciPy stack | — | ✓ | ✓ | Research code; no premature optimization |
| 9 | Property-based testing from axioms | — | ✓ | ✓ | A1'-A4, C1-C4, D-Ax1-4 as test oracles |
| 10 | 10 seeds per configuration | — | — | ✓ | Wilcoxon signed-rank + Bonferroni correction |

---

## III. TENSION RESOLUTION: PIPELINE vs. MODULES

**The tension:** Algorithm Designer specifies `FindFormation` as a monolithic pipeline (normalize → initialize → iterate → extract). Systems Engineer specifies 6 independent modules with clean interfaces. These are not contradictory — they operate at different abstraction levels.

**Resolution: Facade over modules.**

```
┌─────────────────────────────────────────────────────┐
│  FindFormation (orchestrator / facade)               │
│  ─ owns iteration loop, convergence check, logging  │
│                                                      │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐            │
│  │ Operators │ │ Energy   │ │ Gradient │            │
│  │ Module    │ │ Module   │ │ Module   │            │
│  └──────────┘ └──────────┘ └──────────┘            │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐            │
│  │ Predicate│ │ Parameter│ │ Recovery │            │
│  │ Module   │ │ Module   │ │ Module   │            │
│  └──────────┘ └──────────┘ └──────────┘            │
└─────────────────────────────────────────────────────┘
```

**Rules:**
1. Each module has a pure-function interface: inputs → outputs, no shared mutable state.
2. `FindFormation` is the *only* thing that orchestrates module calls and manages iteration state.
3. Experiments call `FindFormation` for end-to-end runs, but can call individual modules for ablation studies (e.g., computing energy with one term zeroed out).
4. No module imports another module. All inter-module data flows through the orchestrator or through explicit data structures (field arrays, parameter dicts).

This gives the Algorithm Designer's clean pipeline semantics *and* the Systems Engineer's testability and composability.

---

## IV. UNIFIED ARCHITECTURE

### Layer 1: Static Evaluation (no iteration)

**Module 1: Operators** — Computes operator outputs from field u and parameters.

| Operator | Realization | Complexity | Key Constraint |
|----------|-------------|------------|----------------|
| Cl_t(u) | σ(a_cl · ((1-η)u + η·P_t·u − τ_cl)) | O(\|E\|) | a_cl < 4 (contraction) |
| N_t | Kernel (given as graph adjacency) | O(1) lookup | Symmetric, sparse |
| C_t(u) | (I − αW_sym)^{-1} via Neumann series, k=5-10 | O(k·\|E\|) | α < 1/ρ(W_sym); resolvent only |
| D_t(x; 1−u) | σ(a_D·(P_t·u − λ_D·P_t·(1−u)) − τ_D) | O(\|E\|) | b_D = 0 (mandatory) |
| T_t | — | — | OPEN — not implemented in Iteration 3 |
| M_{t→s} | — | — | Deferred (temporal theory unaddressed) |

**Implementation note on C_t:** The Neumann series $(I - \alpha W_{\mathrm{sym}})^{-1} \approx \sum_{j=0}^{k} (\alpha W_{\mathrm{sym}})^j$ is computed as iterated sparse matrix-vector products. For the full matrix (needed for Sep computation), compute column-by-column or use the diagonal-only shortcut for Sep_new when only $C_t(x,x)$ is needed.

**Critical optimization:** Sep_new = $\frac{\sum_x C_t(x,x) \cdot D_t(x; 1-u)}{\sum_x C_t(x,x)}$ requires only the diagonal of the resolvent. The diagonal of $(I - \alpha W)^{-1}$ can be computed in O(k·n) via the Neumann series without forming the full matrix: $[(I - \alpha W)^{-1}]_{xx} = \sum_{j=0}^{k} [\alpha^j W^j]_{xx}$. This is the return-probability of a length-j walk — computable by k rounds of sparse matrix-vector multiplication with indicator vectors, or more efficiently by tracking the diagonal of the running product.

**Module 2: Energy** — Computes energy terms from field u and operator outputs.

| Term | Formula | Dependencies |
|------|---------|-------------|
| E_cl(u) | Σ_x (u(x) − Cl_t(u)(x))² | Operators.Cl_t |
| E_sep(u) | Σ_x u(x)·(1 − D_t(x; 1−u)) | Operators.D_t |
| E_bd(u) | α·Σ_{x,y} N_t(x,y)·(u(x)−u(y))² + β·Σ_x u(x)²(1−u(x))² | Operators.N_t |
| E_tr | — (deferred) | — |
| E_total | λ_cl·E_cl + λ_sep·E_sep + λ_bd·E_bd | All above |

**Automatic λ normalization (MANDATORY):** Before optimization, evaluate each energy term at u ≡ c (uniform on Σ_m, c = m/n). Set:

$$\lambda_i^{\mathrm{norm}} = \frac{\lambda_i^{\mathrm{raw}}}{\mathcal{E}_i(c\mathbf{1}) + \varepsilon_{\mathrm{norm}}}$$

where ε_norm ~ 10⁻¹⁰ prevents division by zero. This ensures each term has comparable magnitude at the uniform state, making the λ ratios interpretable and R10 verification meaningful. The normalization must happen once at initialization, then λ^norm values are frozen for the entire optimization run.

**Module 3: Predicates** — Computes diagnostic vector from field u and operator outputs.

| Predicate | Formula | Output |
|-----------|---------|--------|
| Bind(u) | 1 − ‖u − Cl_t(u)‖₂ / √n | [0, 1] |
| Sep(u) | Σ_x C_t(x,x)·D_t(x;1−u) / Σ_x C_t(x,x) | [0, 1] |
| Inside(u) | ℓ_max(u) · Artic(u) | [0, 1] |
| Persist | — (deferred) | — |
| ProtoCoh | [Bind, Sep, Inside, —] | [0,1]³ (static) |

**ℓ_max and Artic definitions:**
- ℓ_max(u): length of the longest bar in the 0-dimensional persistence diagram of the superlevel filtration of u. Normalized by diameter or max possible. Requires a persistence computation library (e.g., `gudhi`, `ripser`, or a simple union-find for 0-dim on grids).
- Artic(u): articulation index — measures how well-separated the longest bar is from the rest. Ratio of longest bar to sum of all bars, or gap between longest and second-longest.

**Implementation note:** For 0-dimensional persistence on a grid graph, the superlevel filtration is computed by sorting vertices by decreasing u-value and using union-find. This is O(n log n) — fast and standard.

### Layer 2: Within-Time Optimization

**Module 4: Gradient + Projection** — Core optimization loop.

**Algorithm: Projected Semi-Implicit Gradient Flow on Σ_m**

```
Input: graph G = (V, E, N_t), parameters θ, volume m, tolerance ε_conv
Output: optimized field u* ∈ Σ_m

1. NORMALIZE: compute λ^norm from E_i(c·1) where c = m/|V|
2. INITIALIZE: u ← random perturbation of c·1 on Σ_m
   (uniform Dirichlet on simplex, or Gaussian perturbation + project)
3. ITERATE:
   For τ = 1, 2, ... until convergence:
     a. g ← ∇E_total(u)                    // full gradient (Module 2 + autodiff or analytic)
     b. g_Σ ← g − mean(g)·1               // project gradient onto Σ_m tangent space
     c. dt ← adaptive_step(g_Σ, u)         // backtracking line search or Barzilai-Borwein
     d. u_half ← u − dt · g_Σ^{react}     // explicit step: reaction terms (E_cl, E_sep, double-well)
     e. u_new ← (I + dt·α·L)^{-1} u_half  // implicit step: diffusion (Laplacian of E_bd)
     f. u_new ← clip(u_new, 0, 1)          // enforce [0,1] box
     g. u_new ← u_new · (m / sum(u_new))   // re-project onto Σ_m
     h. CONVERGE CHECK:
        - |E(u_new) − E(u)| / (|E(u)| + ε) < ε_energy
        - ‖u_new − u‖₂ / √n < ε_field
        - ‖g_Σ‖₂ / √n < ε_grad
        If all three: STOP
     i. u ← u_new
     j. EVERY k_diag STEPS: compute and log diagnostic vector [Bind, Sep, Inside]
4. MULTI-START: repeat with R independent initializations, return lowest-energy solution
5. OUTPUT: u*, E(u*), diagnostic vector, convergence history
```

**Semi-implicit splitting rationale:** The Laplacian term 2α·L in E_bd has eigenvalues up to 2α·λ_max(L), which for a 2D grid of side N is O(αN²). Explicit stepping requires dt < 1/(2αλ_max) ~ O(1/N²) — prohibitively small. The implicit step (I + dt·α·L)⁻¹ is unconditionally stable for the diffusion part and costs one sparse linear solve per step (tridiagonal on regular grids, or sparse Cholesky via `scipy.sparse.linalg.spsolve`).

**Gradient computation:** Two options, both viable:
- **Analytic gradients** for each energy term. E_cl and E_sep require the Jacobian of Cl_t and D_t w.r.t. u (chain rule through sigmoid and P_t — straightforward). E_bd gradient is 4αLu + β·∇W(u) where W is the double-well.
- **Automatic differentiation** via JAX or PyTorch. Cleaner but adds a framework dependency.

**Recommendation:** Start with analytic gradients for E_bd (trivial) and E_cl (one Jacobian). Use finite differences to validate. Only bring in autodiff if E_sep gradients through the resolvent C_t become unwieldy.

**Step size:** Barzilai-Borwein with backtracking Armijo line search. Initial dt from 1/(Lipschitz estimate of ∇E). Adaptive: if energy increases, halve dt and retry.

### Layer 3: Between-Time Evolution (DEFERRED)

Not implemented in Iteration 3. The temporal theory (Persist, M_{t→s}, between-time handoff) is the largest open gap in the mathematics. Implementation would be premature.

**Stub interface only:** Define the data structure for a temporal sequence of fields {u_t}_{t∈T} and the transport kernel M_{t→s}, but do not implement optimization or persistence evaluation.

### Module 5: Parameters

**Three-tier parameter organization:**

| Tier | Parameters | How Set |
|------|-----------|---------|
| **Structural** (fixed by theory) | Volume constraint m, box [0,1], Σ_m projection | Not tunable |
| **Operator** (set once per problem) | a_cl, η_cl, τ_cl, a_D, λ_D, τ_D, α_resolvent, k_Neumann | See defaults below |
| **Optimization** (tunable per run) | dt_init, ε_conv, max_iter, n_restarts, k_diag | See defaults below |

**Default parameter values (initial):**

```python
DEFAULTS = {
    # Operator parameters
    'a_cl': 3.5,          # < 4 for contraction (A3). Close to boundary for expressiveness
    'eta_cl': 0.5,        # balance self-retention and neighborhood
    'tau_cl': 0.5,        # threshold at midpoint
    'a_D': 5.0,           # distinction sensitivity
    'lambda_D': 1.0,      # equal weighting of interior/exterior support
    'tau_D': 0.0,         # no offset
    'b_D': 0.0,           # MANDATORY: zero for analyticity
    'alpha_resolvent': 0.5,  # < 1/ρ(W_sym); safe default for bounded-degree graphs
    'k_neumann': 8,       # Neumann series truncation

    # Energy parameters (raw, before normalization)
    'lambda_cl': 1.0,
    'lambda_sep': 1.0,
    'lambda_bd': 1.0,
    'alpha_bd': 1.0,      # smoothness weight in E_bd
    'beta_bd': 10.0,      # double-well weight; must satisfy β/α > 4λ₂/|W''(c)| for T8

    # Optimization parameters
    'dt_init': 0.01,
    'eps_energy': 1e-8,
    'eps_field': 1e-6,
    'eps_grad': 1e-6,
    'max_iter': 10000,
    'n_restarts': 5,
    'k_diag': 100,        # diagnostic evaluation interval
}
```

**Phase transition computation:** For a given graph, compute λ₂ (Fiedler eigenvalue) and evaluate β*/α = 4λ₂/|W''(c)| where W''(c) = 2(1-6c+6c²). This gives the critical ratio above which non-trivial minimizers exist (T8-Core). The implementation must compute and report this threshold before any optimization run.

### Module 6: Recovery (Group F interface)

Computes derived crisp notions from optimized soft field:

| Output | Method |
|--------|--------|
| Core_t | {x : u(x) ≥ θ_core}, θ_core = 0.9 default |
| Int_t | {x : u(x) ≥ θ_in}, θ_in = 0.5 default |
| Bd_t | {x : θ₁ < u(x) < θ₂}, θ₁ = 0.2, θ₂ = 0.8 |
| Ext_t | {x : u(x) ≤ θ_ext}, θ_ext = 0.1 default |
| Persistence diagram | 0-dim superlevel filtration (union-find) |

---

## V. R10 VERIFICATION PROTOCOL (PRIORITY 1)

This is the single most important experiment. It determines the theory's mathematical narrative.

### What must be verified

The R10 claim: "Separation energy dominates instability by 10⁵×" has three methodological caveats (R13):
1. **Parameter normalization** — was the dominance computed with arbitrary λ = 1?
2. **Volume constraint** — was the analysis done on Σ_m or on unconstrained [0,1]^n?
3. **Sign conventions** — were stabilizing/destabilizing contributions correctly attributed?

### Verification experiment design

**Setup:** 2D grid graph, N×N, N ∈ {10, 20, 50}. Volume fraction c = 0.5 (centered in spinodal). Evaluate at u ≡ c·1 on Σ_m.

**Step 1: Compute constrained Hessian.** The Hessian of E_total on Σ_m is:

$$H_{\Sigma} = \Pi_{\Sigma} \cdot H \cdot \Pi_{\Sigma}$$

where $\Pi_\Sigma = I - \frac{1}{n}\mathbf{1}\mathbf{1}^T$ is the projection onto the tangent space of Σ_m, and H is the unconstrained Hessian. This projection removes the constant mode (which is constrained).

**Step 2: Decompose by energy term.**

$$H_{\Sigma} = \lambda_{\mathrm{cl}}^{\mathrm{norm}} H_{\mathrm{cl}} + \lambda_{\mathrm{sep}}^{\mathrm{norm}} H_{\mathrm{sep}} + \lambda_{\mathrm{bd}}^{\mathrm{norm}} H_{\mathrm{bd}}$$

Each H_i is the constrained Hessian of the corresponding energy term, computed with the **normalized** λ values.

**Step 3: Eigendecomposition.** For each H_i, compute eigenvalues. Count negative eigenvalues (destabilizing directions). Sum negative eigenvalues (total destabilizing magnitude).

**Step 4: Sweep λ ratios.** Repeat with λ_sep/λ_bd ∈ {0.01, 0.1, 1, 10, 100} while keeping λ_cl fixed. Report:
- Number of negative eigenvalues per term
- Sum of negative eigenvalues per term
- Most negative eigenvalue per term
- Whether the dominance ratio changes qualitatively or only quantitatively

**Step 5: Sign verification.** For each eigenvector v with negative eigenvalue in H_total: compute v^T H_i v for each energy term. Verify that the signs are consistent (negative = destabilizing, positive = stabilizing). Report any eigenvector where the decomposition is ambiguous.

**Step 6: Six energy configurations** (from Experiment Designer):
1. E_bd only (pure Allen-Cahn baseline)
2. E_bd + E_cl (closure correction)
3. E_bd + E_sep (separation correction)
4. E_bd + E_cl + E_sep (full static energy)
5. E_sep only (pure separation — does it produce formations alone?)
6. E_cl + E_sep (no Allen-Cahn — does morphology emerge from self-referential terms alone?)

For each: run gradient flow from perturbed uniform, record convergence, final energy, diagnostic vector, and visualize the field.

### Success criteria

| Outcome | Implication |
|---------|-------------|
| Separation dominates across all λ ratios and grid sizes | R10 confirmed; separation-driven narrative adopted |
| Separation dominates only for specific λ ratios | R10 partially confirmed; dominance is parameter-dependent, not intrinsic |
| Separation contributes but does not dominate | R10 weakened; "Allen-Cahn + self-referential corrections" narrative retained |
| Separation does not contribute to instability on Σ_m | R10 falsified; re-examine the unconstrained analysis |

---

## VI. EXPERIMENT SCHEDULE (PRIORITY ORDER)

| # | Experiment | Depends On | Purpose | Est. Compute |
|---|-----------|------------|---------|-------------|
| **E1** | **R10 Verification** | Modules 1-2, Hessian code | Settle the narrative | Hours (small grids, eigendecomposition) |
| **E2** | Phase diagram | Module 4 (gradient flow) | Map (β/α, c) → formation/uniform | Hours-days (grid sweep) |
| **E3** | Axiom property tests | Module 1 | Verify A1'-A4, C1-C4, D-Ax1-4 computationally | Minutes |
| **E4** | Convergence validation | Module 4 | Verify T14 (gradient flow convergence) numerically | Hours |
| **E5** | C_t scalability | Module 1 (resolvent) | Neumann series k vs. accuracy vs. time | Minutes |
| **E6** | Parameter sensitivity | Modules 4-5 | Which parameters most affect diagnostic vector | Days (high-dimensional sweep) |
| **E7** | Non-idempotence advantage | Module 4 | Compare Cl_t fixed points: contraction vs. projection | Hours |

**Critical path:** Module 1 (Operators) → Module 2 (Energy) → E1 (R10 verification) → E3 (axiom tests) → Module 4 (Gradient flow) → E2 (phase diagram) → E4 (convergence) → E6 (sensitivity) → E7 (non-idempotence).

E1 and E3 can be done *before* the full gradient flow is implemented — they only need static evaluation and Hessian computation.

---

## VII. IMPLEMENTATION ROADMAP

### Phase 1: Foundation (Modules 1-2 + E1/E3)

**Goal:** Static evaluation layer complete. R10 verified or falsified. Axioms tested.

**Deliverables:**
- `operators.py`: All operator realizations (Cl_t, N_t, C_t, D_t). Pure functions. Property-tested.
- `energy.py`: All energy terms + automatic λ normalization. Gradient computation (analytic for E_bd; analytic or finite-diff for E_cl, E_sep).
- `predicates.py`: Diagnostic vector computation. Persistence via union-find for ℓ_max.
- `parameters.py`: Default parameter dict. Phase transition threshold computation.
- `hessian.py`: Per-term Hessian computation on Σ_m. Eigendecomposition.
- `test_axioms.py`: Property-based tests for A1'-A4, C1-C4, D-Ax1-4.
- **E1 results document.**

**Estimated effort:** This is the highest-value phase. Everything downstream depends on it.

### Phase 2: Optimization (Module 4 + E2/E4)

**Goal:** Gradient flow working. Phase diagram computed. Convergence validated.

**Deliverables:**
- `optimizer.py`: Semi-implicit projected gradient flow. Multi-start. Convergence diagnostics.
- `find_formation.py`: Orchestrator facade. End-to-end pipeline.
- `recovery.py`: Crisp readout (Core, Int, Bd, Ext, persistence diagram).
- `test_convergence.py`: Validate T14 numerically (energy monotone decrease, rate estimation).
- **E2 phase diagram document.**

### Phase 3: Exploration (E5-E7)

**Goal:** Parameter sensitivity understood. Non-idempotence advantage quantified. Scalability characterized.

**Deliverables:**
- Parameter sensitivity report
- Non-idempotence comparison document
- C_t scalability analysis
- Scaling benchmarks (n = 10², 10³, 10⁴, 10⁵, 10⁶)

### Phase 4: Documentation

**Goal:** Iteration 3 capstone integrating all results.

**Deliverables:**
- Revised Operator Status Table (with computational validation status)
- Updated parameter recommendations
- R10 narrative resolution
- Gaps identified for Iteration 4 (temporal theory, multi-formation)

---

## VIII. SCALING ANALYSIS

Algorithm Designer's estimate: n = 10⁶ feasible in ~20s per gradient step. Let's verify.

**Per-step cost breakdown (n = |V|, m_E = |E|):**

| Operation | Cost | For 2D grid (n = N²) |
|-----------|------|-----------------------|
| P_t·u (sparse mat-vec) | O(m_E) | O(4n) = O(n) |
| Cl_t(u) (sigmoid + P_t) | O(n + m_E) | O(n) |
| D_t(x; 1−u) (sigmoid + 2×P_t) | O(n + 2m_E) | O(n) |
| C_t diagonal (k Neumann rounds) | O(k·m_E) | O(8kn) for k=8 |
| E_cl (pointwise) | O(n) | O(n) |
| E_sep (pointwise) | O(n) | O(n) |
| E_bd (sparse quadratic form) | O(n + m_E) | O(n) |
| ∇E_bd = 4αLu + β∇W | O(n + m_E) | O(n) |
| ∇E_cl (through Cl_t Jacobian) | O(n + m_E) | O(n) — J_Cl is sparse |
| ∇E_sep (through D_t Jacobian) | O(n + m_E) | O(n) |
| Implicit solve (I + dt·αL)⁻¹ | O(n) for 2D grid (FFT or tridiagonal) | O(n log n) via FFT |
| Projection onto Σ_m | O(n) | O(n) |
| **Total per step** | **O(k·m_E)** | **~100n** for k=8 |

For n = 10⁶: ~10⁸ flops per step ≈ 0.1s in NumPy. With 200-1000 steps to convergence: **20-100s total.** Feasible for research.

**Memory:** Field u (n floats) + sparse adjacency (4n entries for grid) + Cl_t, D_t outputs (n each) + gradient (n). Total: ~30n floats = 240 MB for n = 10⁶. Fits in RAM.

**Bottleneck:** The C_t diagonal computation (k sparse mat-vecs) dominates. If full C_t matrix is needed (for validation, not for Sep_new), it's O(k·n·m_E) — infeasible for large n. **Use diagonal-only for production; full matrix only for small-n validation.**

---

## IX. GAPS AND RISKS

### Gaps in the current plan

| # | Gap | Severity | Mitigation |
|---|-----|----------|------------|
| G1 | ∇E_sep through resolvent C_t | Medium | C_t enters Sep but Sep is a predicate, not directly in the energy. E_sep only uses D_t, not C_t. The resolvent affects Sep *monitoring* but not the gradient flow. **Clarify:** does the energy use C_t? If Sep_new enters the energy, the resolvent Jacobian is needed. If Sep_new is diagnostic only, it isn't. The Canonical Spec's E_sep = Σ u(x)·(1−D_t(x;1−u)) does NOT contain C_t. **Resolution: C_t is diagnostic only; gradient flow uses E_cl + E_sep + E_bd, none of which contain C_t.** |
| G2 | Persistence computation for Inside | Low | 0-dim persistence on grid is O(n log n) via union-find. Well-understood. Library dependency (gudhi) or simple custom implementation. |
| G3 | ∇E_cl requires J_{Cl_t} (Jacobian of closure) | Medium | For sigmoid closure, J = diag(σ'(·)) · (diag(1−η) + η·P_t). This is a sparse matrix. Computing J^T·(u − Cl_t(u)) is O(n + m_E). Straightforward but must be implemented correctly. |
| G4 | ∇E_sep requires J_{D_t} (Jacobian of distinction) | Medium | Similar to G3. D_t is a sigmoid of affine functions of P_t·u and P_t·(1−u). Jacobian is sparse. Must be derived and implemented. |
| G5 | Implicit solve for non-grid graphs | Low (for Iteration 3) | On regular grids, (I + dt·αL)⁻¹ can use FFT or ADI splitting. On general graphs, use `scipy.sparse.linalg.spsolve` (sparse Cholesky). For Iteration 3, grids only. |
| G6 | Multi-start doesn't guarantee global minimum | Inherent | Non-convex landscape. Multi-start with R = 5-10 restarts. Report all local minima found. Compare energies. |
| G7 | No T_t implementation | By design | T_t is mathematically OPEN. Do not implement a placeholder. |

### Risks

| # | Risk | Probability | Impact | Mitigation |
|---|------|-------------|--------|------------|
| R1 | R10 falsified — separation doesn't drive instability | Medium | High (narrative change) | The theory still works; only the "separation-driven" narrative is lost. Formations still exist (T8-Core). |
| R2 | Gradient flow converges to trivial minimizer despite volume constraint | Low | High | Volume constraint + T8-Core should prevent this for supercritical β/α. Monitor. |
| R3 | Resolvent C_t is numerically unstable for α near spectral radius | Medium | Medium | Monitor condition number. Reduce α or increase ε stabilization if needed. |
| R4 | Semi-implicit splitting introduces artifacts | Low | Medium | Validate against fully explicit (small dt) on small grids. Energy should still decrease monotonically. |
| R5 | A1' not satisfied by sigmoid in practice | Medium | Low (known from R4) | A1' is conditional. Monitor and report violations. |

---

## X. WHAT WE ARE NOT DOING IN ITERATION 3

Explicitly deferred to Iteration 4 or later:

1. **Temporal theory (Persist, M_{t→s}, between-time evolution)** — mathematics not ready.
2. **Multi-formation** — blocked by contraction regime; requires architectural decisions.
3. **T_t implementation** — operator mathematically OPEN.
4. **JAX/GPU optimization** — premature; NumPy/SciPy first.
5. **3D or non-grid domains** — 2D grid is sufficient for all Iteration 3 experiments.
6. **Category-theoretic formulation** — pure mathematics, not implementation.
7. **Cognitive science connections** — downstream of computational validation.

---

## XI. DECISION RECORD

| # | Decision | Rationale | Status |
|---|----------|-----------|--------|
| D1 | Facade pattern resolves pipeline/module tension | Algo gets clean pipeline; Sys gets testable modules | **SETTLED** |
| D2 | Analytic gradients first, autodiff only if needed | Minimize dependencies; E_bd gradient is trivial; E_cl/E_sep manageable | **SETTLED** |
| D3 | Diagonal-only C_t for production | Full resolvent is O(k·n²); diagonal is O(k·n) | **SETTLED** |
| D4 | R10 verification before phase diagram | Narrative determines parameter priorities | **SETTLED** |
| D5 | Union-find for 0-dim persistence | Standard, fast, no heavy library needed | **SETTLED** |
| D6 | Barzilai-Borwein step size | Superlinear convergence without Hessian cost | **SETTLED** |
| D7 | 10 seeds, Wilcoxon, Bonferroni for statistics | Experiment Designer's protocol is sound | **SETTLED** |
| D8 | C_t is diagnostic only, not in energy gradient | Canonical Spec E_sep uses D_t, not C_t | **SETTLED** (verify with theory) |

---

## XII. SUMMARY

**What we're building:** A Python implementation of SCC's static theory — operators, energy, predicates, gradient flow optimizer — sufficient to verify the R10 hypothesis, compute phase diagrams, and validate the first 12 theorems computationally.

**What we're deciding first:** Whether separation energy drives instability (R10). This single experiment determines the parameter regime, the mathematical narrative, and the priorities for everything that follows.

**What we're deferring:** Temporal theory, multi-formation, T_t, GPU, 3D. All are premature given the current mathematical status.

**Architecture:** Six modules behind a `FindFormation` facade. Pure-function interfaces. Property-based testing from axioms. Automatic λ normalization. Semi-implicit gradient flow. Multi-start for non-convexity.

**Critical path:** Operators → Energy → Hessian → R10 verification → Axiom tests → Gradient flow → Phase diagram → Parameter sensitivity → Capstone.

---

*This synthesis integrates the Algorithm Designer's computational specifications, the Systems Engineer's architectural design, and the Experiment Designer's validation protocol into a single coherent implementation roadmap. Conflicts are resolved, gaps are identified, and priorities are established. The theory enters computational realization.*
