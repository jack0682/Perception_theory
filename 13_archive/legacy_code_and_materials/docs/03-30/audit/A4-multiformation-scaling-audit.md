# A4: Multi-Formation and Scaling Audit

**Auditor:** Teammate 4 — Multi-Formation and Scaling Auditor
**Date:** 2026-03-30
**Files reviewed:** I9-multi-formation.md, scc/multi.py, results_multiformation.md, results_sensitivity.md, results-I8.md, results_predictions.md, scc/optimizer.py, scc/energy.py, scc/params.py, Canonical Spec v2.0.md, I8-code-synthesis.md

---

## 1. Why Multi-Formation Currently Fails

### 1.1. The K-Field Energy Is Not Mathematically Sound

**Problem: The simplex barrier breaks analyticity.**

The implementation uses:

```
E_barrier = lambda_bar * sum_x max(0, sum_k u^k(x) - 1)^2
```

The function `max(0, z)^2` is C^1 but not C^2 at z=0 (the second derivative has a jump discontinuity). This directly violates the analyticity requirement for T14 (gradient flow convergence via Łojasiewicz inequality). The entire convergence guarantee of the single-formation theory depends on analyticity (`b_D = 0` was specifically mandated for this reason — see Canonical Spec CN13). The multi-formation extension casually introduces a non-analytic term.

**Severity: CRITICAL.** Without Łojasiewicz convergence, there is no guarantee that the K-field gradient flow converges to a critical point at all. The optimizer may cycle or stall at non-critical configurations. The I9 document claims T14 extends because "the interaction terms u^j(x)·u^k(x) are polynomial, hence analytic" (§5.5), but this statement ignores the barrier term entirely.

**Fix:** Replace the barrier with a smooth penalty, e.g., `sum_x exp(gamma * (S(x) - 1))` or a log-barrier `- sum_x log(1 - S(x))`. Both are analytic on the interior of the feasible set. Alternatively, enforce the simplex constraint via exact projection (as the volume constraint is handled), but this requires projecting onto the simplex intersection with volume constraints — a well-studied but non-trivial problem.

### 1.2. The Repulsion Term Is Ad Hoc

The interaction energy is:

```
E_inter = lambda_rep * sum_x u^j(x) * u^k(x)
```

This is a pointwise inner product — the simplest possible interaction. The I9 document (§4.4) offers an "ontological justification" (cohesive exclusion), but this justification would equally support several alternative interactions:

| Interaction | Formula | What it measures |
|-------------|---------|-----------------|
| Inner product (chosen) | `sum u^j · u^k` | Pointwise overlap |
| Support overlap | `sum min(u^j, u^k)` | Shared territory (non-smooth) |
| Wasserstein distance | `W_1(u^j, u^k)` | Transport cost between formations |
| KL divergence | `sum u^j log(u^j/u^k)` | Information-theoretic asymmetry |
| Boundary interaction | `sum_xy N(x,y) u^j(x) u^k(y)` | Relational proximity (in spec but not implemented) |

The I9 formalization (§3.3) actually specifies **two** interaction terms: pointwise repulsion AND boundary repulsion (`lambda_bdy * sum_xy N(x,y) u^j(x) u^k(y)`). But the implementation (`multi.py`) only implements the pointwise term. The boundary repulsion term is silently dropped. This means the implementation does not match the specification.

**Severity: MODERATE.** The inner product is defensible as the simplest polynomial repulsion, and it is analytic (unlike support overlap). But the spec/implementation mismatch is a concern, and the choice is not uniquely determined by the theory's principles.

### 1.3. T8-Core Does Not Apply Per Formation in the K-Field Setting

The I9 document (§5.5) claims: "T8-Core requires re-examination for the joint energy. The Hessian at the uniform state now includes cross-formation terms. This is an open problem."

This is more serious than acknowledged. The T8-Core argument works by showing the uniform state u ≡ c is a saddle point of E_bd. In the K-field setting, the "uniform state" is (u^1 ≡ c/K, ..., u^K ≡ c/K) (equal distribution of mass). The Hessian of the joint energy at this point is a K×K block matrix:

```
H = diag(H_self^1, ..., H_self^K) + H_inter
```

where `H_inter` has off-diagonal blocks `lambda_rep * I + lambda_bdy * N`. The cross-terms are POSITIVE (repulsion), which **stabilizes** the uniform state — they resist perturbations that would create overlap. So the repulsion actually **opposes** phase separation in the cross-formation directions. The instability condition becomes harder to satisfy, not easier.

**Consequence:** There is no guarantee that the K-field energy has a non-trivial minimizer with K active formations. The I9 phase transition sketch (§3.6) argues informally that "for sufficiently large lambda_rep and M," splitting is favorable, but this argument assumes the split formations are well-separated — which is the conclusion, not a premise. The argument is circular.

### 1.4. K Is an Irreducible External Parameter

The I9 document acknowledges this (§1, Option B weaknesses) and proposes "formation death" as a mitigation: start with K_max formations and let unnecessary ones die (u^k → 0). However:

1. **No sparsity penalty is implemented.** The implementation (`multi.py`) has no mechanism to drive formations to zero mass. The volume is fixed per formation (`m_per_formation`).
2. **Volume is pre-allocated.** Each formation gets `volume_fraction * n` mass by default. A dying formation would need to transfer its mass to surviving formations, requiring a variable-mass formulation not present in the code.
3. **No criterion for choosing K_max.** Even if formation death worked, K_max must be chosen. Setting K_max = 100 on a 20×20 grid is computationally infeasible (400 × 100 = 40,000-dimensional optimization).

**Severity: HIGH.** K-selection is genuinely unsolved. The "formation death" proposal is aspirational, not implemented or implementable with the current architecture.

---

## 2. K=2 Experimental Results: Critical Analysis

### 2.1. The Two Formations Are Real but Fragile

At **weak repulsion (lambda_rep=1)**, both formations achieve strong diagnostics (Bind > 0.88, Sep > 0.79, Inside > 0.74). This is the one genuinely positive result. The formations are spatially separated (CoM distance 12.4) with small overlap (0.075). This demonstrates that K-field can work when repulsion is gentle.

However, the question "are these two independent structures or two halves of one?" is relevant. With overlap = 0.075 and the Fiedler-based initialization deliberately placing formations in different spatial regions, the optimizer may simply be finding two single-formation solutions that happen to coexist peacefully because the repulsion is too weak to matter.

**Test needed but not performed:** Run K=1 with volume_fraction = 0.5 (same total mass as K=2). If K=1 produces a single formation with comparable or better diagnostics, the K=2 result is not demonstrating multi-formation behavior — just splitting a single formation for cosmetic reasons.

### 2.2. Strong Repulsion Destroys Formations — This IS Reported Honestly

At **strong repulsion (lambda_rep=100)**: Bind=0.84, Sep=0.21, Inside=0.01. The results_multiformation.md correctly states: "Very strong repulsion flattens formations to near-uniform ~0.25 within their support, destroying phase separation (Inside ~ 0)."

This is honest reporting. But the implication is severe: **the repulsion-quality tradeoff has no good regime for strong separation.** The weak regime (lambda_rep=1) gives high quality but allows overlap. The strong regime (lambda_rep=100) eliminates overlap but destroys formation quality. The moderate regime (lambda_rep=10) is a compromise with mediocre results (Sep=0.45, Inside=0.12).

**Root cause:** The pointwise repulsion `sum u^j · u^k` penalizes ANY co-occurrence, including at low field values. When lambda_rep is large, the gradient `lambda_rep * sum_{j≠k} u^j` dominates the self-energy gradient everywhere, flattening the fields. A thresholded repulsion (only penalize overlap above some threshold) would avoid this, but would sacrifice analyticity.

### 2.3. Is K=2 Ever Better Than K=1?

The experiments do not answer this directly. The K=2 results use volume_fraction = 0.25 per formation (total 0.50). There are no K=1 results at volume_fraction = 0.50 for comparison. Without this baseline, the claim "K-field architecture works" is incomplete. Working means doing better than the alternative, not just producing two fields.

---

## 3. Scaling Analysis

### 3.1. Computational Scaling

**Claim: O(n) per gradient step.**

Let's verify. Each gradient step computes:
- `grad_bd`: sparse matrix-vector product L·u → O(nnz(L)). For grid graphs, nnz ≈ 4n, so O(n). ✓
- `grad_cl`: closure operator (sigmoid of weighted average) → O(nnz(L)). Then Jacobian-transpose-vector → O(nnz(L)). Total O(n). ✓
- `grad_sep`: distinction operator → O(nnz(L)). Jacobian-transpose-vector → O(nnz(L)). Total O(n). ✓
- Semi-implicit step: `spsolve(A_imp, u_react)`. This is NOT O(n) in general. For banded matrices (grid graphs), it's O(n) with appropriate solvers. For general sparse matrices, it's O(n^{1.5}) or worse. ✓ for grids, ✗ in general.
- Hessian normalization: `eigsh(L, k=1)` → O(n·nnz(L)/n) ≈ O(n) for sparse, but with a large constant. Called once, not per step.

**Verdict: O(n) per step for grid graphs, but the semi-implicit solve is the bottleneck for general graphs.** The claim needs qualification.

### 3.2. Quality Scaling

From results-I8.md Experiment 4:

| Grid | n | Bind | Sep | Inside |
|------|---|------|-----|--------|
| 5×5 | 25 | 0.846 | 0.506 | 0.986 |
| 10×10 | 100 | 0.852 | 0.504 | 0.990 |
| 20×20 | 400 | 0.855 | 0.507 | 0.986 |

Quality is remarkably stable across grid sizes. But these are all TINY grids. On a 100×100 grid (n=10,000), the Fiedler eigenvalue λ₂ ≈ π²/100² ≈ 0.001. This means:

- β_crit = 4αλ₂/|W''(c)| ≈ 4 × 1.0 × 0.001 / 0.667 ≈ 0.006
- β/β_crit = 10/0.006 ≈ 1,667

The theory ALWAYS predicts phase separation on large grids (β_crit → 0 as grid size increases). **This means the phase transition becomes trivially satisfied — it is not a meaningful constraint on large graphs.** Any β > 0 will produce formations.

### 3.3. The Phase Transition Is Vacuous on Large Graphs

This is a fundamental issue. The T8-Core condition β/α > 4λ₂/|W''(c)| becomes trivially satisfied as the graph grows, because λ₂ → 0 for grid-like graphs (λ₂ ~ 1/diameter²). This means:

1. The phase transition criterion provides no information about whether formations are "real" or artifacts.
2. On a 1000×1000 grid, β_crit ≈ 4 × 10^{-6}. Even β = 0.001 (practically zero double-well) would produce "formations."
3. The theory cannot distinguish "the system undergoes phase separation because the parameters favor it" from "the system is so large that any perturbation grows."

**This is not just a calibration issue — it undermines the theoretical claim that formations emerge from a genuine phase transition.** On large graphs, formations emerge because the flat state is unstable to ANY perturbation, not because the parameters encode a meaningful physical tendency.

**Possible fix:** The phase transition criterion should be expressed in terms of intensive quantities (per-site energies) rather than extensive quantities (total energy). Alternatively, scale α with n to keep β_crit O(1).

### 3.4. Parameter Scaling

The sensitivity experiment (results_sensitivity.md) tests on a 15×15 grid only. Key question: do the "sweet spot" parameters transfer to larger graphs?

The Hessian normalization (`normalize_weights`) is graph-dependent — it computes spectral norms at the uniform state. On different graph sizes, the spectral norms change:
- `sigma_bd` depends on `lambda_max(L)`, which is O(1) for bounded-degree graphs (max eigenvalue of grid Laplacian ≈ 8 for 2D grid).
- `sigma_cl` and `sigma_sep` are estimated by finite-difference power iteration, which also depends on graph structure.

So the normalized weights `lambda_i = w_i / sigma_i` will change with graph size, but in a predictable way. The normalization is specifically designed to handle this. **This is one area where the design is sound.**

However: the Hessian norms are computed at the uniform state u ≡ c. The actual optimization proceeds far from this state. There is no guarantee that the normalization remains appropriate at the minimizer. On larger graphs with more complex energy landscapes, the local Hessian structure could differ dramatically from the initial point.

---

## 4. Parameter Interaction Analysis

### 4.1. What the Sensitivity Experiment Misses

The sensitivity experiment sweeps **one parameter at a time** while holding all others at defaults. This tests marginal sensitivity but completely misses:

1. **Pairwise interactions.** Does the effect of a_cl depend on eta_cl? The closure operator is `sigma(a_cl * ((1-eta_cl) * u + eta_cl * Pu - tau_cl))`. The a_cl and eta_cl parameters multiply — a_cl amplifies the nonlinearity while eta_cl controls the aggregation/self balance. At extreme (a_cl=3.9, eta_cl=0.1), the closure is nearly self-referential with maximum nonlinearity. This combination is never tested.

2. **Energy weight interactions.** The sweep tests w_cl, w_sep, w_bd independently. But the quality depends on their RATIOS (after Hessian normalization). Setting w_cl=5 with w_sep=1 is very different from w_cl=5 with w_sep=5. The experiment cannot distinguish "w_cl=5 is bad" from "w_cl/w_sep=5 is bad."

3. **Volume-parameter interactions.** Volume_fraction = 0.75 (near spinodal boundary) with beta_bd = 5 (low double-well) might fail catastrophically, while each independently is fine.

4. **The cliff at eta_cl = 0.1.** The experiment shows eta_cl=0.1 gives min_diag=0.700 (exactly at the threshold). What happens at eta_cl=0.05? 0.01? The one-dimensional sweep has 5 points across [0.1, 0.9] — there are no points below 0.1. The parameter space below 0.1 is unexplored. If eta_cl=0.01 gives min_diag=0.3, there is a cliff that the experiment misses entirely.

### 4.2. Hidden Fragility: The Hessian Normalization

The Hessian normalization divides energy weights by spectral norms: `lambda_i = w_i / (sigma_i + eps)`. On grid graphs, the spectral norms are well-behaved. But on other graph topologies:

- **Scale-free graphs:** The maximum Laplacian eigenvalue can be O(n) (hub nodes). sigma_bd would be very large, making lambda_bd very small. The double-well (the dominant formation driver) would be effectively turned off.
- **Disconnected or nearly-disconnected graphs:** λ₂ ≈ 0, so β_crit ≈ 0, and sigma_bd could be dominated by the W''(c) term, which is negative in the spinodal range. The spectral norm computation takes `abs(4α·lambda_max_L + 2β·W''(c))`, which could be near zero if the two terms cancel — creating numerical instability in the normalization.
- **Random geometric graphs:** Spectral properties vary with realization. The normalization would produce different effective weights for each random instance, making results non-reproducible across graph instances.

**Severity: MODERATE for current scope (grid graphs only), HIGH for any claim of generality.**

### 4.3. The 44/45 Robustness Claim

The sensitivity report claims "44/45 configurations have min_diag > 0.7" and concludes "the theory is NOT hand-tuned." This is misleading for several reasons:

1. **Threshold is arbitrary.** Why 0.7? If the threshold were 0.85, only ~25/45 would pass. The choice of 0.7 is itself a form of parameter tuning.
2. **One-at-a-time sweep is weak.** A full factorial design (5^9 = ~2M configs) or even a Latin hypercube sample (100 configs) would provide much stronger evidence.
3. **Grid graphs are easy.** 2D grids are the most regular, symmetric graphs possible. Robustness on grids says little about robustness on irregular graphs, trees, or real-world networks.
4. **Formation quality is dominated by E_bd.** The ablation experiment (Experiment 3) shows BD-only gives Inside=1.0 and Bind=0.85. The closure and separation terms provide marginal refinements. So the "robustness" is really the robustness of the Allen-Cahn double-well on grid graphs — which is well-known and not a novel finding.

---

## 5. The Single-Formation Assumption is Pervasive

### 5.1. Inventory of Single-Formation Dependencies

| Component | Single-formation assumption | Multi-formation status |
|-----------|---------------------------|----------------------|
| Energy E(u) | Single field u | K-field extension specified, partially implemented |
| Gradient flow (T14) | Analyticity of E(u) | BROKEN by simplex barrier (max(0,·)²) |
| Phase transition (T8-Core) | Hessian at u ≡ c for single field | NOT re-derived for K-field |
| Diagnostic vector d | Single formation | Per-formation diagnostics defined but use SINGLE-FORMATION operators |
| Closure Cl_t | Single field aggregation | Formation-specific aggregation specified but NOT implemented |
| Distinction D_t | 1-u as exterior | 1-u^k as exterior — includes other formations, which is correct per spec |
| Optimizer | Single field on Σ_m | K-field optimizer implemented but WITHOUT semi-implicit stepping |
| Hessian normalization | Spectral norms for single-field energy | Applied per-formation independently; cross-terms ignored |

### 5.2. The Implementation Gap

The I9 specification describes formation-specific operators (§3.2): closure with available-capacity modulation (ω^k_t(y) = 1 - sum_{j≠k} u^j_t(y)), formation-specific co-belonging, etc. **None of this is implemented.** The `multi.py` code reuses the single-formation `EnergyComputer` unchanged:

```python
# Intra-formation gradient
g_intra = ec.gradient(fields[k])
```

This means each formation's gradient is computed as if the other formations don't exist. The only interaction is through the repulsion and barrier terms. The closure operator does not see other formations' presence. The distinction operator computes against `1 - u^k`, not against the refined decomposition into "other-formation" and "true exterior."

**Consequence:** The current K=2 implementation is not K-field theory as specified in I9. It is K independent single-formation optimizations coupled only by a pointwise repulsion penalty. The formation-specific operator modifications (which are the theoretical innovation) are entirely absent from the code.

---

## 6. Cleanest Extension Path

### 6.1. Minimum Viable Multi-Formation

To make multi-formation mathematically sound, the following are required (in order of priority):

1. **Replace simplex barrier with smooth penalty.** Use `sum_x phi(S(x))` where `phi` is analytic and `phi(z) → ∞` as `z → 1^+`. The log-barrier `phi(z) = -log(1-z)` for z < 1 is standard. This restores analyticity and T14 applicability.

2. **Implement formation-specific aggregation.** The closure operator for formation k must use `omega^k_t(y) = 1 - sum_{j≠k} u^j_t(y)` in its aggregation weights. This is the core theoretical contribution of I9 and currently has zero implementation.

3. **Add boundary repulsion term.** The spec defines `lambda_bdy * sum_xy N(x,y) u^j(x) u^k(y)` but the code omits it. This term provides relational-topology-aware repulsion rather than just pointwise, and is needed for the theory to be self-consistent.

4. **Re-derive T8-Core for K-field.** The Hessian of the K-field energy at the uniform state must be explicitly computed, including cross-formation blocks. The instability condition will depend on both lambda_rep and the graph spectrum.

### 6.2. Minimal New Mathematics Required

1. **K-field Hessian analysis.** Compute the full nK × nK Hessian at (c/K, ..., c/K) and find conditions on lambda_rep such that a negative eigenvalue exists. This is a block matrix eigenvalue problem — tractable.

2. **Analyticity proof for smooth barrier.** Verify that the chosen smooth barrier preserves analyticity of the total energy on the interior of the feasible set.

3. **Formation-specific contraction.** Prove that Cl^k_t with omega-modulated aggregation remains a contraction. The key question: does other-formation presence reduce the contraction constant (good) or violate it (fatal)?

4. **K-selection theory.** This is the hardest unsolved problem. A principled approach might use information-theoretic criteria (BIC/AIC on the energy landscape) to select K from data, analogous to model selection in mixture models.

---

## 7. Summary of Findings

### Critical Issues (theory-breaking)

| # | Issue | Location | Impact |
|---|-------|----------|--------|
| C1 | Simplex barrier breaks analyticity, invalidating T14 for K-field | multi.py:153-154 | Convergence guarantee lost |
| C2 | T8-Core not re-derived for K-field; instability may be harder to achieve | I9 §5.5 | Non-trivial K-formation existence unproved |
| C3 | Phase transition vacuous on large graphs (β_crit → 0 as n → ∞) | General | Theory's central prediction meaningless at scale |

### Significant Issues (spec/implementation mismatch, missing features)

| # | Issue | Location | Impact |
|---|-------|----------|--------|
| S1 | Boundary repulsion term in spec but not implemented | multi.py vs I9 §3.3 | Code does not match theory |
| S2 | Formation-specific operators not implemented | multi.py:140 | K-field is just K×(single-field) + repulsion |
| S3 | No formation death mechanism (K fixed) | multi.py:53-58 | K is irreducible external parameter |
| S4 | Strong repulsion destroys formation quality | results_multiformation.md | No good operating regime for strict separation |
| S5 | No K=1 baseline comparison for K=2 results | results_multiformation.md | Cannot assess whether K=2 adds value |

### Moderate Issues (testing gaps, generality concerns)

| # | Issue | Location | Impact |
|---|-------|----------|--------|
| M1 | Sensitivity tests one-at-a-time only; no interaction effects | results_sensitivity.md | Robustness claim overstated |
| M2 | All experiments on grid graphs only | results-I8.md | No evidence for non-grid topologies |
| M3 | Semi-implicit solve is not O(n) for general graphs | optimizer.py:116 | Scaling claim needs qualification |
| M4 | Hessian normalization at uniform state may not represent minimizer | energy.py:169-205 | Normalization could be inappropriate |
| M5 | Cliff behavior at eta_cl < 0.1 unexplored | results_sensitivity.md | Potential hidden fragility |

### What Works

1. **Single-formation theory on grid graphs is solid.** 100% success rate, consistent across grid sizes 5×5 to 20×20, robust to one-at-a-time parameter variation.
2. **K=2 at weak repulsion produces plausible results.** Two spatially separated formations with reasonable diagnostics.
3. **The I9 architecture decision is well-reasoned.** The four-option evaluation is thorough, and K-field is the right choice. The problem is execution, not architecture.
4. **Hessian normalization is a sound design.** It provides graph-adaptive energy weight scaling.
5. **SCC basins are deeper than Allen-Cahn (4-17×).** This is a genuine, experimentally confirmed advantage of the self-referential terms.
