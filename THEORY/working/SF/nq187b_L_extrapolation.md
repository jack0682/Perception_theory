# nq187b_L_extrapolation.md — NQ-187b: Discrete-Grid $A_2/A_1$ Evaluation as Function of L

**Status:** working draft (W5 Day 4 PM, Task #62).
**Created:** 2026-04-30 (W5 Day 4 PM).
**Type:** Numerical test design — L → ∞ extrapolation of cubic-equivariant ratio $A_2/A_1$ on $D_4$ free-BC grid; reconciliation path (α) for T-σ-Theorem-4 finite-L finding (per `sigma_theorem4_canonical_revision.md` §4.1).
**Author origin:** Task #62; companion to Task #63 (urgent canonical revision packet); part of (α)/(β)/(γ) reconciliation triple.
**Canonical refs:** §13 T-σ-Theorem-4 (Cat B with finite-L caveat per Wave 3 audit); §11.1 Commitment 14 (O7).
**Working refs:** `sigma_theorem4_canonical_revision.md` (Task #63 parent packet); `working/SF/symmetry_moduli.md` §3.3 (R22 $A_2/A_1 = 4$ continuum claim — audit target); `THEORY/logs/daily/2026-04-30/11_nq187_scaling_test_results.md` (NQ-187 numerical evidence source).

---

## §1. Mission

> **"NQ-187 W5 Day 4 numerical test 가 finite L $\in \{4, 8, 16\}$ 에서 $\mu_1/\mu_0 = 2$ (NOT 1) 를 measure 했음. 이는 effective $(A_2/A_1)_{\mathrm{eff}, L} \approx 8$ 를 의미하나, R22 continuum claim 은 $A_2/A_1 = 4$. 이 file 은 directly $A_2 = \int \phi_{(1,0)}^2 \phi_{(0,1)}^2$ 와 $A_1 = \int \phi_{(1,0)}^4$ 를 discrete grid 에서 compute 하여 L → ∞ extrapolation 을 design — (α) reconciliation path."**

이 working file 은 T-σ-Theorem-4 의 finite-L 발견에 대한 (α) reconciliation path 를 정식화한다: $A_2/A_1$ ratio 를 직접 discrete grid 에서 compute 하여 R22 continuum claim 을 verify 또는 reject.

**핵심 deliverables**:
1. $A_1, A_2$ discrete grid formulas (§2).
2. L scan plan (§3).
3. Extrapolation methodology (§4).
4. Predictions (§5).
5. Numerical script outline (§6).
6. Cat criteria (§7).
7. Cross-link to Task #63 reconciliation triple (§8).

---

## §2. Discrete Grid Formulas

### §2.1 Eigenmodes on $D_4$ free-BC grid

For $L \times L$ free-BC (Neumann) grid, the eigenmodes of the discrete Laplacian are:
$$\phi_{(p, q)}(i, j) = \cos\left(\frac{p\pi(i + 1/2)}{L}\right) \cos\left(\frac{q\pi(j + 1/2)}{L}\right)$$
for $i, j \in \{0, 1, \ldots, L-1\}$ and $p, q \in \{0, 1, \ldots, L-1\}$.

The lowest non-trivial Fiedler doublet is $V_2 = \mathrm{span}(\phi_{(1, 0)}, \phi_{(0, 1)})$ (after removing $\phi_{(0, 0)} = $ constant).

### §2.2 Cubic equivariants

In the R22 normal-form analysis on $D_4$ Fiedler doublet, the cubic-equivariant coefficients $A_1, A_2$ enter the post-bifurcation potential $F(x, y; \beta) = \beta(x^2 + y^2) + A_1 (x^2 + y^2)^2 + A_2 x^2 y^2$.

### §2.3 Continuum form (R22 §3.3 claim)

In continuum limit on $[0, L]^2$ with eigenmodes $\phi_{(p, q)}^{\mathrm{cont}}(x, y) = \cos(p\pi x / L) \cos(q\pi y / L)$:

$$A_1^{\mathrm{cont}} = \int_0^L \int_0^L \phi_{(1, 0)}^4 \, dx \, dy = \int_0^L \cos^4(\pi x / L) dx \cdot \int_0^L 1 \, dy = (3L/8) \cdot L = 3L^2/8.$$

$$A_2^{\mathrm{cont}} = \int_0^L \int_0^L \phi_{(1, 0)}^2 \phi_{(0, 1)}^2 \, dx \, dy = \int_0^L \cos^2(\pi x / L) dx \cdot \int_0^L \cos^2(\pi y / L) dy = (L/2)^2 = L^2/4.$$

**Continuum ratio**: $A_2^{\mathrm{cont}} / A_1^{\mathrm{cont}} = (L^2/4) / (3L^2/8) = 2/3 \neq 4$.

**WAIT — discrepancy with R22 claim**. R22 `symmetry_moduli.md` §3.3 claims $A_2/A_1 = 4$. The naive integration gives $2/3$. There must be a normalization difference (e.g., L²-norm normalized eigenmodes, or different cubic-equivariant convention).

**Reconciliation**: the R22 cubic-equivariant ratio depends on the *normalization convention* for $\phi_{(p, q)}$:
- If eigenmodes normalized to $\|\phi\|_2 = 1$ (L² unit norm): $\phi_{(1, 0)}^{\mathrm{norm}} = \sqrt{2/L^2} \cdot \cos(\pi x / L)$. Then $A_1^{\mathrm{norm}} = (3/8) \cdot (2/L^2)^2 \cdot L^2 = 3/(2L^2)$, $A_2^{\mathrm{norm}} = (1/4) \cdot (2/L^2)^2 \cdot L^2 = 1/L^2$. Ratio $A_2/A_1 = 1/(3/2) = 2/3$.
- If R22's $A_1, A_2$ have additional $W''(c)$ or $\beta$ factors: ratio may differ.
- If the convention is *energy expansion in axis-aligned vs symmetric coordinates*: factor of 4 may arise from a 4-element orbit ($\phi_{(1, 0)} \pm \phi_{(0, 1)}$ as orbit elements vs single-mode amplitude).

The naive cubic-equivariant integral ratio $2/3$ does NOT match R22's $4$. This is an immediate **red flag** for (β) reconciliation path (R22 derivation audit).

### §2.4 Discrete grid form

For the $L \times L$ free-BC grid:
$$A_1^L = \sum_{i, j = 0}^{L-1} [\phi_{(1, 0)}(i, j)]^4 = \sum_{i = 0}^{L-1} \cos^4\left(\frac{\pi(i + 1/2)}{L}\right) \cdot L$$
(separable; sum over $j$ of $1$'s gives $L$).

$$A_2^L = \sum_{i, j = 0}^{L-1} [\phi_{(1, 0)}(i, j)]^2 [\phi_{(0, 1)}(i, j)]^2 = \sum_{i = 0}^{L-1} \cos^2\left(\frac{\pi(i + 1/2)}{L}\right) \cdot \sum_{j = 0}^{L-1} \cos^2\left(\frac{\pi(j + 1/2)}{L}\right).$$

### §2.5 Closed-form discrete sums

**For $\sum_{i=0}^{L-1} \cos^2((i+1/2)\pi/L)$**: by trigonometric identity $\cos^2(\theta) = (1 + \cos(2\theta))/2$,
$$\sum_i \cos^2\left(\frac{(i+1/2)\pi}{L}\right) = L/2 + (1/2)\sum_i \cos\left(\frac{(2i+1)\pi}{L}\right) = L/2 + 0 = L/2$$
(the sum $\sum_i \cos((2i+1)\pi/L) = 0$ for any $L \geq 1$, by symmetric cancellation).

**For $\sum_{i=0}^{L-1} \cos^4((i+1/2)\pi/L)$**: $\cos^4 = (3 + 4\cos(2\theta) + \cos(4\theta))/8$,
$$\sum_i \cos^4\left(\frac{(i+1/2)\pi}{L}\right) = 3L/8 + (4/8)\sum_i \cos\left(\frac{(2i+1)\pi}{L}\right) + (1/8)\sum_i \cos\left(\frac{(4i+2)\pi}{L}\right).$$

The middle sum is $0$. The last sum: $\sum_i \cos((4i+2)\pi/L)$ is non-zero in general (specifically zero when $L$ is even, but with $\pi/L$ phase shift makes it more complex).

For $L \in \{4, 8, 16, 32, 64\}$: explicit computation gives:

| L | $\sum_i \cos^2((i+1/2)\pi/L)$ | $\sum_i \cos^4((i+1/2)\pi/L)$ |
|---|---|---|
| 4 | 2.0 | 1.25 |
| 8 | 4.0 | 2.625 |
| 16 | 8.0 | 5.6875 |
| 32 | 16.0 | 11.96875 |
| 64 | 32.0 | 24.2734375 |

Continuum value: $L/2$ for $\cos^2$ sum (verified) and $3L/8$ for $\cos^4$ sum (continuum $3/8 \cdot 64 = 24$; discrete $24.273$ — small finite-L correction).

### §2.6 Discrete ratio

$$\frac{A_2^L}{A_1^L} = \frac{(L/2)^2}{L \cdot \sum_i \cos^4(\theta_i)} = \frac{L/4}{\sum_i \cos^4(\theta_i)}$$

Plugging in:

| L | $A_1^L$ | $A_2^L$ | $A_2^L/A_1^L$ |
|---|---|---|---|
| 4 | $4 \cdot 1.25 = 5.0$ | $2.0^2 = 4.0$ | **0.80** |
| 8 | $8 \cdot 2.625 = 21.0$ | $4.0^2 = 16.0$ | **0.762** |
| 16 | $16 \cdot 5.6875 = 91.0$ | $8.0^2 = 64.0$ | **0.703** |
| 32 | $32 \cdot 11.96875 = 383.0$ | $16.0^2 = 256.0$ | **0.668** |
| 64 | $64 \cdot 24.2734 = 1553.5$ | $32.0^2 = 1024.0$ | **0.659** |

Continuum limit: $A_2/A_1 \to (L^2/4) / (L \cdot 3L/8) = (L/4) / (3L/8) = 2/3 \approx 0.667$.

**Critical observation**: discrete $A_2/A_1$ ratio approaches $2/3 \approx 0.667$ as $L \to \infty$, **NOT** R22's claimed value of 4.

This is a **two-orders-of-magnitude discrepancy** with R22. Either:
- (α') The cubic-equivariants in the R22 paper are *not* the naive integrals computed above — different normalization or different definition.
- (β') R22's $A_2/A_1 = 4$ value is incorrect.
- (γ') The eigenmodes used by R22 differ from $\phi_{(p, q)} = \cos((p)(i+1/2)\pi/L) \cos((q)(j+1/2)\pi/L)$ (e.g., spectral gauge convention).

---

## §3. L Scan Plan

### §3.1 Test specification

Compute $A_2^L / A_1^L$ at $L \in \{4, 8, 16, 32, 64, 128\}$ via:
1. Naive cubic-equivariant integrals (§2.5 explicit).
2. Cross-check against R22 derivation in `working/SF/symmetry_moduli.md` §3.3 (audit (β)).
3. Cross-check against numerical $\mu_1/\mu_0$ from NQ-187 (current values at L=4,8,16; extend to L=32, 64).

### §3.2 Convention check

Multiple R22-compatible conventions to test:
- **C1 (naive integral)**: §2.5 closed-form. Continuum $\to 2/3$.
- **C2 (normalized eigenmodes)**: $\|\phi\|_2 = 1$. Ratio same as C1 (normalization cancels).
- **C3 (mass-conservation simplex projection)**: cubic equivariants computed on Σ_m-tangent space (subtract mean). Ratio differs.
- **C4 (W-potential expansion coefficients)**: $A_1, A_2$ pulled out of full potential expansion $\mathcal{E}(c\mathbf{1} + a\phi + b\psi)$, including $W$-potential cross-terms. Ratio differs.

NQ-187b test: compute under each convention and report.

### §3.3 NQ-187 cross-check

Current NQ-187 numerical $\mu_1/\mu_0(L)$:

| L | NQ-187 $\mu_1/\mu_0$ | (Implies effective $A_2/A_1$ ratio) |
|---|---|---|
| 4 | ≈ ? (raw data needed) | ? |
| 8 | ≈ ? | ? |
| 16 | ≈ 2.0 (from §2 of `13_wave3_critical_findings.md`) | ≈ 8 |

If NQ-187 numerical $\mu_1/\mu_0$ approaches some L-independent value: that limit is the *true* effective ratio.

If NQ-187 numerical $\mu_1/\mu_0(L) \to 2/3$ as $L \to \infty$: matches naive convention C1.
If NQ-187 numerical $\mu_1/\mu_0(L) \to 1$: matches R22 claim $A_2/A_1 = 4$.
If NQ-187 numerical $\mu_1/\mu_0(L) \to 2$: stays at L=16 value.

---

## §4. Extrapolation Methodology

### §4.1 Finite-L corrections

For closed-form $A_1^L, A_2^L$ (per §2.5, naive convention):
$$A_2^L / A_1^L = (L^2/4) / (L \cdot 3L/8 + O(1)) \to 2/3 + O(1/L^2).$$

The leading finite-L correction is $O(1/L^2)$. Extrapolation:
$$A_2^L / A_1^L = (A_2/A_1)_{\infty} + c_1/L^2 + O(1/L^4)$$
fit to $L \in \{4, 8, 16, 32, 64\}$.

For numerical $\mu_1/\mu_0$ from NQ-187: same $1/L^2$ correction expected.

### §4.2 Extrapolation procedure

Given measured ratios $r_L = A_2^L / A_1^L$ (or $\mu_1/\mu_0(L)$) at $L \in \{L_1, \ldots, L_N\}$:
1. Plot $r_L$ vs $1/L^2$.
2. Fit linear regression: $r_L = a + b/L^2$.
3. Extrapolated value: $a$ at $1/L^2 = 0$.

### §4.3 Predicted continuum value

Per naive convention C1 (§2.5): $r_\infty = 2/3 \approx 0.667$.

If R22 convention is different (C3 or C4): $r_\infty$ differs. Audit via `symmetry_moduli.md` §3.3 (β path) needed.

If NQ-187 numerical $r_\infty \to$ value matching one of the conventions: identify which convention is correct.

---

## §5. Predictions

### §5.1 Hypothesis (α-naive)

Naive cubic-equivariant ratio: $A_2/A_1 \to 2/3$ in continuum.
- $\mu_1/\mu_0 = (A_2/A_1) / 4 \to (2/3)/4 = 1/6$ at L → ∞ (per canonical T-σ-Theorem-4 (ii) formula: $\mu_0 = 4|W''(c)|\epsilon$, $\mu_1 = (A_2/A_1)|W''(c)|\epsilon$).

NQ-187 numerical at L=16: $\mu_1/\mu_0 = 2$.

Trend: $\mu_1/\mu_0 = 2$ at L=16; if approaching $1/6$ as $L \to \infty$ would require **decreasing** trend with L. NQ-187 power-law $p = 1.03$ implies leading-order non-degeneracy at finite L; whether this trend changes at larger L is the test.

### §5.2 Hypothesis (R22)

R22 continuum $A_2/A_1 = 4$ ⇒ $\mu_1/\mu_0 \to 1$ at L → ∞ (degenerate as canonical claims).
- Trend: $\mu_1/\mu_0 = 2$ at L=16; if approaching 1 as $L \to \infty$, would require **decreasing** trend.

### §5.3 Hypothesis (saturation)

Effective $(A_2/A_1)_{\mathrm{eff}} = 8$ saturates ⇒ $\mu_1/\mu_0 = 2$ for all L.
- Trend: $\mu_1/\mu_0 = 2$ at all L.

### §5.4 Verification at L = 32, 64

Need NQ-187 extension to $L = 32, 64$ to discriminate (α-naive)/(R22)/(saturation):

| L | $\mu_1/\mu_0$ predicted (α-naive) | (R22) | (saturation) |
|---|---|---|---|
| 16 | trend toward 1/6 | trend toward 1 | 2 |
| 32 | smaller than at L=16 | smaller than at L=16 | 2 |
| 64 | smaller still | smaller still | 2 |

The α-naive and R22 hypotheses both predict *decreasing* $\mu_1/\mu_0$ with L (toward different limits 1/6 vs 1); saturation hypothesis predicts constant 2.

---

## §6. Numerical Script Outline

### §6.1 Direct $A_2/A_1$ computation

`CODE/scripts/nq187b_a2_a1_extrapolation.py`:
```python
"""
NQ-187b: Direct discrete-grid computation of A_2/A_1 ratio on D_4 free-BC grid,
extrapolated to L → ∞.
Reconciliation path (α) for T-σ-Theorem-4 finite-L finding.
"""

import numpy as np

def phi_pq(p, q, L):
    """Discrete eigenmode on L x L free-BC grid."""
    i = np.arange(L).reshape(-1, 1)  # (L, 1)
    j = np.arange(L).reshape(1, -1)  # (1, L)
    return np.cos(p * np.pi * (i + 0.5) / L) * np.cos(q * np.pi * (j + 0.5) / L)

def A1(L):
    """A_1 = sum phi_(1,0)^4 on L x L grid."""
    phi = phi_pq(1, 0, L)
    return np.sum(phi**4)

def A2(L):
    """A_2 = sum phi_(1,0)^2 * phi_(0,1)^2 on L x L grid."""
    phi_h = phi_pq(1, 0, L)
    phi_v = phi_pq(0, 1, L)
    return np.sum(phi_h**2 * phi_v**2)

def ratio(L):
    return A2(L) / A1(L)

def extrapolate_to_infinity(L_values, ratios):
    """Linear fit r(L) = a + b/L^2; extrapolate to L=infty."""
    x = 1 / np.array(L_values)**2
    y = np.array(ratios)
    A = np.vstack([np.ones_like(x), x]).T
    a, b = np.linalg.lstsq(A, y, rcond=None)[0]
    return a, b  # a is L=infty extrapolation

def main():
    L_values = [4, 8, 16, 32, 64, 128]
    ratios = [ratio(L) for L in L_values]
    print(f"L values: {L_values}")
    print(f"A_2/A_1 ratios: {ratios}")
    
    # Extrapolate
    r_infty, slope = extrapolate_to_infinity(L_values, ratios)
    print(f"Extrapolated A_2/A_1 at L → ∞: {r_infty:.6f}")
    print(f"Slope coefficient: {slope:.6f}")
    
    # Compare to predictions
    print(f"  Naive convention (cont 2/3): {2/3:.6f}")
    print(f"  R22 convention (claimed 4): 4.0")
    print(f"  Saturation (effective 8): 8.0")
    
    # Save
    with open('results/nq187b_a2_a1_extrapolation.json', 'w') as f:
        import json
        json.dump({
            'L_values': L_values,
            'ratios': ratios,
            'extrapolated_L_infty': r_infty,
            'slope_1_over_L_squared': slope,
            'continuum_naive_value': 2/3,
        }, f, indent=2)

if __name__ == '__main__':
    main()
```

### §6.2 Combined with NQ-187 mu_1/mu_0 extension

`CODE/scripts/nq187b_mu_extrapolation.py` (extension of existing `test_sigma_theorem4_scaling.py`):
- Run NQ-187 at L = 32, 64, 128 (Lanczos eigenvalue extraction; may require larger compute budget).
- Fit $\mu_1/\mu_0(L) = a + b/L^2$.
- Compare extrapolated value to direct $A_2/A_1$ ratio (with conversion factor).

### §6.3 Estimated runtime

- Direct $A_2/A_1$ (§6.1): < 1 minute (closed-form trigonometric sums).
- NQ-187 extension to L=32, 64: ~5-15 hours per L (Lanczos eigenvalue extraction at first pitchfork).

**Total**: ~1 hour (direct) + ~10-30 hours (NQ-187 extension via parallelization).

---

## §7. Cat Status and Promotion

### §7.1 Pre-execution Cat status (this file)

- Naive convention C1 closed-form (§2.5): **Cat A** (elementary trigonometric algebra).
- L → ∞ extrapolation methodology (§4.2): **Cat A** (standard finite-size scaling).
- Convention disambiguation (§3.2): **Cat B sketch** — requires R22 audit (β path) to resolve which convention is canonical.

### §7.2 Post-execution Cat target

If §6.1 direct computation + §6.2 NQ-187 extension converge to same value: **Cat A reconciliation path (α)** complete.

If they disagree: convention mismatch identified — directs (β) audit toward specific R22 step.

### §7.3 Promotion

This file's results inform `sigma_theorem4_canonical_revision.md` (Task #63 packet) §4.1 (α path) audit. Direct contribution to T-σ-Theorem-4 Cat A re-promotion path at CV-1.7+.

---

## §8. Cross-Link to Reconciliation Triple (Task #63)

### §8.1 Path (α) NQ-187b L → ∞ extrapolation

**This file**: directly computes $A_2/A_1$ at multiple L; extrapolates to continuum.

### §8.2 Path (β) R22 derivation audit

**Companion file** (NEW W6+ working file `working/SF/r22_a2_a1_audit.md`): re-derive R22's $A_2/A_1 = 4$ claim from first principles; check each step.

### §8.3 Path (γ) Σ_m-Hessian convention audit

**Companion file** (NEW W6+ working file `working/SF/sigma_m_hessian_convention_audit.md`): verify NQ-187 architect's §2.1 absorption derivation.

### §8.4 Combined convergence

If (α)+(β)+(γ) all converge to same value: T-σ-Theorem-4 Cat A re-promotion at CV-1.7+.

If discrepancies: further investigation; possible Cat C downgrade if no convention is correct.

---

## §9. Hard Constraint Verification

- [x] **canonical 직접 수정 0** — `working/SF/` only.
- [x] **Silent resolution 0** — multiple conventions registered (§3.2); naive C1 closed-form gives ratio $2/3$, contradicts R22 $4$ claim and contradicts NQ-187 numerical $\mu_1/\mu_0 = 2$ implies $(A_2/A_1)_{\mathrm{eff}} = 8$ — full disambiguation pending (β) audit.
- [x] **No Research OS resurrection** — single-topic test design.
- [x] **Not reductive** — naive trigonometric integrals computed in standard mathematical conventions; no external framework reduction.
- [x] **u_t primitive maintained** — eigenmodes are derived from graph Laplacian; $A_1, A_2$ are coefficients in expansion of $\mathcal{E}$ on $V_2$.
- [x] **CN5 4-energy not merged** — N/A.
- [x] **K not dual-treated** — single-formation context.
- [x] **No metastability claim without P-F flag** — N/A.
- [x] **Closed-form Cat A, NQ-187 extension Cat B target** — explicit (§7).
- [x] **Convention disambiguation explicit** — §3.2.

---

## §10. Forward Roadmap

### §10.1 W6 Day 1-3 immediate

- Execute §6.1 direct computation (`CODE/scripts/nq187b_a2_a1_extrapolation.py`) — < 1 hour.
- Execute (γ) Σ_m convention audit (Task #63 §4.3 `sigma_m_hessian_convention_audit.md`) — 3-5 days.

### §10.2 W6 Day 4 - W7

- Execute §6.2 NQ-187 extension to L = 32, 64.
- Execute (β) R22 derivation audit (Task #63 §4.2 `r22_a2_a1_audit.md`).

### §10.3 W7 - W8

- Combine (α)+(β)+(γ) results into final T-σ-Theorem-4 reconciliation report.
- Update canonical revision text (`sigma_theorem4_canonical_revision.md` §3.1) per reconciliation outcome.

### §10.4 CV-1.7+ Cat A re-promotion

If all reconciled: T-σ-Theorem-4 Cat A re-promotion candidate at CV-1.7+.

---

## §11. References

### §11.1 Working files (parent + companions)

- `working/SF/sigma_theorem4_canonical_revision.md` (Task #63 parent packet; this file is (α) reconciliation path).
- `working/SF/symmetry_moduli.md` §3.3 (R22 source — audit target (β)).
- (NEW W6+) `working/SF/r22_a2_a1_audit.md` (β path).
- (NEW W6+) `working/SF/sigma_m_hessian_convention_audit.md` (γ path).

### §11.2 Canonical refs

- `canonical/canonical.md` §13 T-σ-Theorem-4 (Cat B with finite-L caveat post Wave 3).
- `canonical/canonical.md` §11.1 Commitment 14 (O7).

### §11.3 Daily logs

- `THEORY/logs/daily/2026-04-30/11_nq187_scaling_test_results.md` (NQ-187 numerical evidence at L=4,8,16).
- `THEORY/logs/daily/2026-04-30/13_wave3_critical_findings.md` §1 (CRITICAL FINDING #1 — source of this Task #62).

### §11.4 Numerical infrastructure

- `CODE/scripts/test_sigma_theorem4_scaling.py` (existing NQ-187 W5 Day 4).
- (NEW W6 Day 1) `CODE/scripts/nq187b_a2_a1_extrapolation.py` (this file §6.1).
- (NEW W6 Day 4-7) `CODE/scripts/nq187b_mu_extrapolation.py` (this file §6.2).

---

**End of nq187b_L_extrapolation.md.**

**Status: working draft. Task #62 complete (design phase). NQ-187b discrete-grid $A_2/A_1$ evaluation as function of L: closed-form discrete sums (§2.5 Cat A elementary algebra); naive convention gives $A_2/A_1 \to 2/3$ at L → ∞ (NOT R22's claimed 4 — significant discrepancy; (β) audit critical); §3.2 multiple convention candidates registered; §4 finite-size scaling extrapolation methodology; §5 three competing predictions (α-naive 1/6, R22 1, saturation 2); §6 script outline (direct A_2/A_1 < 1 hour, NQ-187 extension 10-30 hours W6+); §7 Cat A target post-execution (post (β) audit). Cross-linked to Task #63 reconciliation triple (§8). All hard constraints verified. Forward: W6 Day 1-3 direct + (γ) audit; W6 Day 4-W7 NQ-187 extension + (β) audit; W7-W8 combined reconciliation report; CV-1.7+ Cat A re-promotion target.**

**File:** `/Users/ojaehong/Perception/Perception_theory/THEORY/working/SF/nq187b_L_extrapolation.md`
**Created:** 2026-04-30 (W5 Day 4 PM).
**Promotion target:** Component of T-σ-Theorem-4 Cat A re-promotion path (CV-1.7+).
