# 11_nq187_scaling_test_results.md — NQ-187 §8 Numerical Verification

**Date:** 2026-04-30 (W5 Day 4 PM, Wave 3 deep-research)
**Owner:** SF (Single-Formation σ-framework)
**Script:** `CODE/scripts/test_sigma_theorem4_scaling.py`
**Output JSON:** `CODE/scripts/results/sigma_theorem4_scaling.json`
**Working file:** `THEORY/working/SF/sigma_theorem4_higher_order.md` §8

---

## §1. Protocol summary

Per `working/SF/sigma_theorem4_higher_order.md` §8.1:

1. Graph: D_4-symmetric free-BC `L × L` grid for `L ∈ {4, 8, 16}`.
2. `α = 1.0`, `c = 0.5`, double-well `W(u) = u²(1-u)²` ⇒ `|W''(c)| = 1`.
3. `β_crit^(2) = 4α·λ_2^Lap / |W''(c)| = 4·λ_2`.
4. For `ε ∈ {0.001, 0.003, 0.01, 0.03, 0.1}`: set `β = β_crit + ε`.
5. `find_formation` from a Fiedler-perturbed IC `u₀ = c·1 + 0.30·v_2` (large
   amplitude to escape unstable uniform fixed point and converge to the
   bifurcated minimizer; `v_2` normalized to `max|v_2|=1` after sign-fix).
6. **Σ_m-restricted Hessian** at `u^*_ε` via the **analytic** sparse form
   `H_bd(u) = 4α·L_G + β·diag(W''(u_i))` (avoids FD truncation noise that
   would swamp the predicted O(ε²) splitting).
7. Bottom-k eigenvalues via `scipy.sparse.linalg.eigsh(sigma=0, which='LM')`
   shift-invert (Lanczos) for `n ≥ 64`; dense `eigvalsh` for `L = 4`. The
   constant-mode kernel of the Σ_m projector is regularized by adding a
   rank-1 penalty `(ρ/n)·11ᵀ` with `ρ = 10³·β`.
8. Power-law fit `log(μ_1 - μ_0) = p·log(ε) + b` (least-squares).

---

## §2. Results

### 2.1 Critical β

| L  | n   | λ_2^Lap   | β_crit^(2) |
|----|-----|-----------|------------|
| 4  | 16  | 0.5858    | 2.343      |
| 8  | 64  | 0.1522    | 0.609      |
| 16 | 256 | 0.0384    | 0.154      |

(Discrete free-BC grid: `λ_2 = 2(1 - cos(π/L))`.)

### 2.2 Eigenvalue table (μ_0, μ_1)

| L  | ε     | μ_0       | μ_1       | Δμ        | μ_0/ε | μ_1/ε | osc(u) |
|----|-------|-----------|-----------|-----------|-------|-------|--------|
| 4  | 0.001 | 1.98e-03  | 3.47e-03  | 1.49e-03  | 1.98  | 3.47  | 0.0103 |
| 4  | 0.003 | 3.64e-03  | 6.97e-03  | 3.32e-03  | 1.21  | 2.32  | 0.0154 |
| 4  | 0.01  | 1.03e-02  | 2.05e-02  | 1.02e-02  | 1.03  | 2.05  | 0.0269 |
| 4  | 0.03  | 3.00e-02  | 6.02e-02  | 3.02e-02  | 1.00  | 2.01  | 0.0460 |
| 4  | 0.1   | 9.81e-02  | 1.99e-01  | 1.01e-01  | 0.98  | 1.99  | 0.0827 |
| 8  | 0.001 | 1.14e-03  | 2.39e-03  | 1.24e-03  | 1.14  | 2.39  | 0.0174 |
| 8  | 0.003 | 3.08e-03  | 6.18e-03  | 3.09e-03  | 1.03  | 2.06  | 0.0288 |
| 8  | 0.01  | 1.00e-02  | 2.01e-02  | 1.01e-02  | 1.00  | 2.01  | 0.0520 |
| 8  | 0.03  | 2.94e-02  | 5.99e-02  | 3.05e-02  | 0.98  | 2.00  | 0.0886 |
| 8  | 0.1   | 9.31e-02  | 1.98e-01  | 1.05e-01  | 0.93  | 1.99  | 0.154  |
| 16 | 0.001 | 1.04e-03  | 2.08e-03  | 1.04e-03  | 1.04  | 2.08  | 0.0332 |
| 16 | 0.003 | 3.00e-03  | 6.04e-03  | 3.04e-03  | 1.00  | 2.01  | 0.0566 |
| 16 | 0.01  | 9.73e-03  | 1.99e-02  | 1.02e-02  | 0.97  | 1.99  | 0.101  |
| 16 | 0.03  | 2.76e-02  | 5.95e-02  | 3.19e-02  | 0.92  | 1.98  | 0.166  |
| 16 | 0.1   | 7.51e-02  | 1.95e-01  | 1.20e-01  | 0.75  | 1.95  | 0.260  |

### 2.3 Power-law fit per L

| L  | p (slope)    | p_stderr | exp(intercept) | regime  |
|----|--------------|----------|----------------|---------|
| 4  | **0.925**    | 0.031    | 0.521          | small-L |
| 8  | **0.970**    | 0.022    | 0.931          | clean   |
| 16 | **1.028**    | 0.014    | 1.214          | clean   |

---

## §3. Convergence assessment

The fitted exponent **converges to p = 1.0 as L grows** (p_4 = 0.93 → p_8 = 0.97
→ p_16 = 1.03). Inspection of the (μ_0/ε, μ_1/ε) ratios at mid-ε
(`ε ∈ {0.003, 0.01, 0.03}`) confirms

- `μ_0 = ε·|W''(c)| + O(ε²)`  (asymptotic ratio ≈ 1)
- `μ_1 = 2·ε·|W''(c)| + O(ε²)` (asymptotic ratio ≈ 2)

so the two eigenvalues are **non-degenerate at leading order** with
asymptotic ratio `μ_1/μ_0 = 2`, and the splitting is

> **Δμ = μ_1 - μ_0 = ε·|W''(c)| + O(ε²)** — slope **p = 1**.

The exponent does *not* converge toward 2 (the §3.2 polynomial-equivariant
prediction) or 3/2 (the §5 alternative); it converges toward 1.

---

## §4. Falsifiability verdict

| Hypothesis (NQ-187 §8.2)                                          | Predicted p | Observed | Status      |
|-------------------------------------------------------------------|-------------|----------|-------------|
| §3.2 polynomial-equivariant (Cat A re-promotion path)             | 2           | 1.0      | **REJECTED** |
| §5 alternative (5th-equivariant non-zero, non-poly correction)    | 3/2         | 1.0      | **REJECTED** |
| Leading-order non-degeneracy (cubic-equivariant ratio ≠ canonical)| 1           | **1.0**  | **CONFIRMED**|

**Verdict: `inconsistent` — observed p ≈ 1 contradicts both NQ-187 §8.2
predictions; data shows leading-order non-degeneracy μ_0 = ε|W''(c)|,
μ_1 = 2ε|W''(c)| consistent with R22 working convention §2 (line 45) but
inconsistent with the Σ_m convention map of §2.1.5 (which predicts
μ_0 = μ_1 = 4ε|W''(c)|).**

---

## §5. Interpretation — what NQ-187 needs to revise

The §3.2 derivation in `working/SF/sigma_theorem4_higher_order.md` predicts
`μ_1 - μ_0 = O(ε²)` *conditional on* the leading-order degeneracy
`μ_0 = μ_1 = 4ε|W''(c)|`, which itself depends on the cubic-equivariant
ratio `A_2/A_1 = 4` (R22 Cat A, `working/SF/symmetry_moduli.md` §3.3).

The data is consistent with `μ_0 = ε`, `μ_1 = 2ε` (in units of `|W''(c)|`).
Reading the R22 normal form Hessian eigenvalues directly (working file §2
line 45 in **R22 working convention**):

- `F_xx^R22(a_ε, 0) = -2μ = 2ε|W''(c)|`
- `F_yy^R22(a_ε, 0) = -μ·(A_2/A_1) = (A_2/A_1)·ε|W''(c)|`

For these to match the observed ascending eigenvalues `μ_0 = ε`, `μ_1 = 2ε`,
we need `A_2/A_1 = 1` (and the smaller eigenvalue is the y-direction).
This is *not* `A_2/A_1 = 4` as claimed in `working/SF/symmetry_moduli.md` §3.3.

Two implications for the working file (no canonical edits per task scope):

1. **§2.1 convention map (sub-subsections 2.1.1–2.1.7)** appears off:
   the empirical Σ_m-restricted Hessian eigenvalues at the bifurcated
   minimizer match the R22 working convention values directly, with no
   factor-of-2 re-absorption needed. The boxed claim `μ_0 = μ_1 = 4ε|W''(c)|`
   (line 108) is *not* supported by the numerical Hessian on `L ∈ {4, 8, 16}`.
2. **§3.2 conclusion `μ_1 - μ_0 = O(ε²)`** is conditional on the leading-order
   degeneracy, which the data falsifies on these grids. Until either (a) the
   continuum-limit `A_2/A_1 = 4` claim is verified at much larger L (with
   explicit `L → ∞` extrapolation showing convergence), or (b) the discrete
   `A_2/A_1` value is re-derived for L ≤ 16 and shown to differ from the
   continuum, the §3.2 splitting prediction has no operational test on the
   `L ∈ {4, 8, 16}` regime specified by §8.

The §8 protocol as written **cannot test** the §3.2 prediction in its
intended falsifiability form on small grids; either much larger L
(continuum extrapolation) or explicit subtraction of the leading-order
O(ε) non-degeneracy is required to isolate the predicted O(ε²) signal.

---

## §6. Compute envelope

| L  | per-ε opt time | per-ε eig time | total |
|----|----------------|----------------|-------|
| 4  | 0.4–1.9 s      | <0.01 s        | 5 s   |
| 8  | 0.2–3.8 s      | <0.01 s        | 8 s   |
| 16 | 0.7–9.7 s      | 0.01 s         | 20 s  |

**Total runtime:** 33 seconds (well within the 60-min budget). The Lanczos
shift-invert eigsh is essentially free (≤ 10 ms for `n = 256` sparse
Hessian); the bottleneck is `find_formation` at small ε on L = 16.

---

## §7. Carry-forward

- **NQ-187:** §3.2 conclusion (p=2) and §2.1 convention map both need
  revision in light of the empirical p=1 observation. Recommend spawning
  `NQ-187b`: discrete-grid `A_2/A_1` evaluation as a function of L,
  verifying whether continuum `A_2/A_1 = 4` is recovered as `L → ∞`.
- **Cross-link to canonical:** T-σ-Theorem-4 (Cat B as of CV-1.5.1) cannot
  be re-promoted to Cat A via the §7 path until the leading-order
  non-degeneracy `μ_0 ≠ μ_1` at finite L is reconciled with the canonical
  claim `K_0 = K_1 = 4ε|W''(c)|`.
- **Working-only this round** — no canonical edits per task constraints.

---

**File status:** Result log (executor numerical verification, 2026-04-30 PM,
Wave 3 W5 Day 4).
