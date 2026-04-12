# Iteration 3 — Round 5: C_t Resolvent Synthesis

**Author:** Implementation Synthesizer
**Date:** 2026-03-27
**Inputs:** Algorithm Designer R5, Systems Engineer R5, Experiment Designer R5
**Status:** COMPLETE — all 3 positions integrated

---

## I. EXECUTIVE SUMMARY

**C_t is diagnostic only.** All three positions independently converge on this: the Canonical Spec's E_sep = Σ u(x)(1−D_t(x;1−u)) contains NO C_t. The resolvent enters the Sep *predicate* but not the *energy*. This is the round's decisive finding — it transforms C_t from "optimization bottleneck" to "negligible diagnostic cost."

With C_t out of the gradient loop, the remaining questions are: (1) how accurately must we compute C_t for Sep monitoring, (2) which backend at which scale, and (3) how to validate C_t axiom satisfaction. All three positions provide compatible answers.

---

## II. THE DECISIVE FINDING: C_t DIAGNOSTIC-ONLY

| Source | Statement |
|--------|-----------|
| Algo Designer | "Sep gradient through C_t" is the hard part — but only needed if C_t enters energy |
| Sys Engineer | "If E_sep = Σu(1−D), then C_t computation is only needed for Sep PREDICATE evaluation" |
| Experiment Designer | "P-C3: C_t is diagnostic-only (NOT in ∂E/∂u)" — calls this "potentially game-changing" |
| R4 Synthesis | Decision D8: "C_t is diagnostic only, not in energy gradient" |
| Canonical Spec §8.2 | E_sep(u_t) = Σ_{x∈X_t} u_t(x)(1 − D_t(x; 1−u_t)) — confirmed: no C_t |

**Status: CONFIRMED.** C_t is evaluated only at diagnostic checkpoints (every k_diag = 50-100 gradient steps), not during optimization. The adjoint method for ∂Sep/∂u through C_t is deferred indefinitely.

**Implication for computation budget:**

| Scenario | C_t evaluations per run | Cost fraction |
|----------|------------------------|---------------|
| C_t in gradient (old assumption) | 10,000 (every step) | 30-80% of total |
| C_t diagnostic-only (confirmed) | 100-200 (every k_diag) | <2% of total |

---

## III. UNIFIED BACKEND SELECTION

All three positions agree on a tiered approach. Harmonized table:

| n | Backend | Cost per eval | Accuracy | Source |
|---|---------|--------------|----------|--------|
| ≤ 400 (20²) | Exact sparse LU | O(n·nnz) | Machine ε | Sys, Exp |
| 400-2,500 (20²-50²) | Neumann K=15 | O(15·\|E\|) | <1% Sep error | Algo, Exp |
| 2,500-10,000 (50²-100²) | Neumann K=15, diagonal only | O(15·\|E\|) per probe | <2% Sep error | Algo, Exp |
| >10,000 (>100²) | Hutchinson+CG, S=50 probes | O(50·nnz) | <5% Sep error | Sys, Algo |

**Key parameters:**
- α_C operating range: 0.5-0.7 of α_max = 1/ρ(W_sym) (Experiment Designer P-C7)
- Neumann convergence: at α_C·ρ = 0.4, K=10 gives error < 7×10⁻⁵ (Algo Designer)
- Discrimination survival: 1000× within/cross-boundary separation survives K≥10 truncation (Experiment Designer P-C6)

### Minor disagreements resolved

| Point | Algo | Sys | Exp | Resolution |
|-------|------|-----|-----|------------|
| Neumann K default | 5-10 | — | 10-15 | **K=10** (sufficient at α·ρ ≤ 0.5; increase to 15 for α·ρ > 0.5) |
| Stochastic probes S | — | 50 | — | **S=50** (Sys's recommendation; <1% error) |
| Hutchinson threshold | n > 100K (Algo) | n > 2500 (Sys) | n > 100² (Exp) | **n > 2500 for full matrix; diagonal Neumann up to 10K** |
| Caching threshold | ε_C = 0.01 (Algo) | adaptive age+norm (Sys) | Δu = 0.01 (Exp) | **Dual criterion: recompute when ‖Δu‖/√n > 0.01 OR age > 50 steps** |

---

## IV. DIAGONAL-ONLY OPTIMIZATION FOR Sep_new

Sep_new = Σ C_t(x,x)·D_t(x;1−u) / Σ C_t(x,x) requires only the diagonal of the resolvent.

**Computing the diagonal efficiently:**

1. **Exact (n ≤ 2500):** Factor (I − α_C W_sym) via sparse LU. Extract diagonal of inverse by solving n unit-vector systems. Or: sparse Cholesky → direct diagonal extraction.

2. **Hutchinson estimator (n > 2500):**
   $$\mathrm{diag}((I - \alpha W)^{-1}) \approx \frac{1}{S}\sum_{i=1}^{S} z_i \odot ((I - \alpha W)^{-1} z_i)$$
   with S=50 Rademacher probes, each solved by CG (~10 iterations). Cost: O(50·10·|E|) = O(500|E|). Error < 1%.

3. **Neumann diagonal (approximate):** The diagonal of Σ_{j=0}^K (αW)^j is the sum of return-probabilities. For the diagonal *only*, this is computable by tracking e_x^T (αW)^j e_x for each x — but this is O(K·n) individual propagations, i.e., O(K·n·|E|). **NOT efficient.** Hutchinson is better for large n.

**Decision:** Use exact for n ≤ 2500, Hutchinson for n > 2500. Neumann is useful for the full Sep computation on small-to-medium grids but not for diagonal-only on large grids.

---

## V. MODULE SPECIFICATION

### resolvent.py (dedicated module per R4 architecture)

```python
class CoBelongingOperator:
    """C_t = (I - α_C · W_sym)^{-1}. Diagnostic only."""

    def __init__(self, config):
        # config: alpha_C, method ('auto'|'exact'|'neumann'|'hutchinson'),
        #         k_neumann, n_probes, staleness_threshold, max_age
        self.backend = auto_select(config, n)  # per tiered table

    def diagonal(self, W_sym, u) -> np.ndarray:
        """Returns [C_t(x,x)] for x in V. Cached with staleness check."""

    def sep_new(self, W_sym, u, D_values) -> float:
        """Sep_new = Σ diag·D / Σ diag. Primary interface for predicates."""

    def full_matrix(self, W_sym, u) -> np.ndarray:
        """Full C_t. Validation only, n ≤ 2500."""

    def validate_axioms(self, W_sym, u, N_t) -> dict:
        """Test C1-C4 on current field. Returns pass/fail per axiom."""
```

### Axiom test suite (from Sys Engineer)

| Axiom | Test | Criterion |
|-------|------|-----------|
| C1 (dependence) | Perturb u, check C_t changes | ‖ΔC_t‖ > 0 when ‖Δu‖ > 0 |
| C2 (discrimination) | Compare C_t(x,y) for within-formation vs cross-boundary pairs | Ratio ≥ 1000× |
| C3'' (monotonicity) | Increase u(x), check C_t(x,x) increases | ΔC_t(x,x) > 0 |
| C4 (symmetry) | Check C_t(x,y) = C_t(y,x) | ‖C_t − C_t^T‖ < ε |

---

## VI. EXPERIMENT PLAN (from Experiment Designer, integrated)

**2,570 total runs across 5 sub-experiments:**

| # | Experiment | Runs | Key Question |
|---|-----------|------|-------------|
| 2A | Scalability ceiling per backend | 1,800 | Where does each method fail? |
| 2B | Neumann K* tradeoff | 480 | Minimum K for <1% Sep error? |
| 2C | C_t in optimizer integration | 120 | Does lazy C_t affect convergence? |
| 2D | Gradient verification (C_t ∉ ∂E/∂u) | 20 | **Confirm P-C3 empirically** |
| 2E | α sensitivity | 150 | Optimal α_C operating range? |

**Sub-experiment 2D is critical:** Compute ∂E/∂u numerically (finite differences) with and without C_t dependence. If the two gradients agree → C_t diagnostic-only confirmed computationally. If they disagree → we have a theory error to resolve.

---

## VII. SUMMARY OF DECISIONS

| # | Decision | Rationale |
|---|----------|-----------|
| D1 | C_t is diagnostic-only — not in gradient loop | Canonical Spec E_sep has no C_t; confirmed by all 3 positions |
| D2 | Evaluate C_t every k_diag = 50-100 steps | Sufficient for monitoring; 50-100× cheaper than every step |
| D3 | Backend: exact ≤2500, Hutchinson >2500 | Sys Engineer + Algo Designer agree on thresholds |
| D4 | Neumann K=10 default, α_C·ρ ≈ 0.4 | Algo error bound + Experiment prediction |
| D5 | Dual caching criterion (norm + age) | Harmonizes Algo/Sys/Exp staleness proposals |
| D6 | Separate resolvent.py module | Own method selection, caching, evaluation schedule |
| D7 | Sub-experiment 2D must run first | Empirically confirms the diagnostic-only finding before building on it |

---

*Complete synthesis. The C_t question is settled: diagnostic-only, evaluated at checkpoints, with tiered backend selection. The adjoint gradient method is deferred indefinitely. Total C_t cost: <2% of optimization budget.*
