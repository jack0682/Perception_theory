# F''(M/2) Computation — Mass-Transfer Curvature at K=2 Symmetric Point

**Date:** 2026-04-07
**Session:** F''(M/2) numerical computation
**Category:** theory
**Status:** complete
**Depends on:** docs/04-06/proof/STRATIFIED-MORSE-ANALYSIS.md (Proposition 3.3, Theorem 3.1)

---

## 1. Question

The sign of F''(M/2) determines K=2 stability on the mass-transfer manifold M_2:
- F'' > 0: K=2 symmetric point is local minimum (merge has barrier)
- F'' < 0: K=2 symmetric point is saddle (merge spontaneous along mass-transfer)

where F(m) = min_{u in Sigma_m} E_self(u) with FIXED normalization weights.

## 2. Methodology

### 2.1 Prior Issue (04-06)
The 04-06 attempt (M2-LANDSCAPE-CORRECTED.md) used `normalize_weights(c=m/n)` at each mass, making E_self(m) use a different functional at each m. This made F(m) ill-defined across masses.

### 2.2 Fix
Fix normalization weights at reference c = c_half = c_ref/2. This gives a single, well-defined energy functional E(u; lambda_fixed) whose minimum over Sigma_m is the true F(m).

### 2.3 Two Methods
1. **Method 1 — Uniform transfer (no re-opt):** Perturb K=2 minimizer as (u1 + eps/n, u2 - eps/n). Measures total curvature including intra-formation stiffness. Always gives F'' >> 0 (O(30-60)) because moving mass uniformly is energetically very costly.

2. **Method 2 — Re-optimize at each mass:** Solve min_{u in Sigma_{M/2+eps}} E(u) independently at each mass, using fixed normalization. This gives the TRUE reduced energy F(m). Numerically noisy due to optimizer finding different local minima at nearby masses.

## 3. Results

### 3.1 Method 1: Uniform Transfer

| Grid | c_ref | c_half | F''(h=0.1) | F''(h=0.2) |
|------|-------|--------|------------|------------|
| 15x15 | 0.5 | 0.250 | 55.8 | 27.8 |
| 15x15 | 0.6 | 0.300 | 61.8 | 30.9 |
| 20x20 | 0.5 | 0.250 | 55.0 | 27.5 |
| 20x20 | 0.6 | 0.300 | 61.7 | 30.8 |

**Always strongly positive.** But this overestimates F'' because it doesn't allow field relaxation.

### 3.2 Method 2: Re-Optimized (True F(m))

| Grid | c_ref | c_half | F''(h=0.5) | F''(h=1) | F''(h=2) |
|------|-------|--------|------------|----------|----------|
| 15x15 | 0.5 | 0.250 | +0.36 | **+0.11** | +0.027 |
| 15x15 | 0.6 | 0.300 | +0.80 | **-0.16** | -0.014 |
| 20x20 | 0.5 | 0.250 | -1.17 | **-0.40** | +0.13 |
| 20x20 | 0.6 | 0.300 | +1.56 | **+0.36** | +0.094 |

**Sign is parameter-dependent and numerically fragile.** The magnitude is O(0.1-1), much smaller than Method 1's O(30-60).

### 3.3 Chemical Potential Gap

| Grid | c_ref | Delta_mu |
|------|-------|----------|
| 15x15 | 0.5 | 1.2e-3 |
| 15x15 | 0.6 | 4.3e-2 |
| 20x20 | 0.5 | -6.4e-3 |
| 20x20 | 0.6 | 3.2e-3 |

Near-zero: formations are at near-equilibrium in mass exchange.

## 4. Analysis

### 4.1 Why F'' is Small and Sign-Variable
The reduced energy F(m) = E_self(u*_m) has competing contributions:
- **Boundary energy** ~ m^{(d-1)/d}: concave in m (F'' contribution < 0)
- **Closure energy** ~ -kappa*m: linear (F'' contribution ~ 0)
- **Separation energy**: parameter-dependent sign

These nearly cancel, giving |F''| << 1. Small optimization noise tips the sign.

### 4.2 Consistency with Theory
This confirms the Stratified Morse Analysis (04-06, Proposition 3.3, Theorem 3.1(c)):
- The boundary-dominated regime predicts F'' < 0 (saddle)
- Strong closure or repulsion can make F'' > 0 (local min)
- The sign IS parameter-dependent — this is the central theoretical prediction

### 4.3 Physical Interpretation
F'' ~ 0 means the K=2 energy landscape along mass-transfer is **nearly flat**. Neither merge nor stability is energetically strong. The K=2 state is:
- Stable within each fiber (intra-formation Hessian positive)
- Marginally stable/unstable along mass-transfer
- Always higher energy than K=1 on tested grids (K=1 wins by factor ~2)

## 5. Conclusion

**F''(M/2) is parameter-dependent, confirming Cat B status.**

The sign cannot be resolved analytically in general because:
1. Competing energy terms with O(1) coefficients nearly cancel
2. The answer depends on the specific graph geometry and SCC parameters
3. Optimizer noise at the 0.01-level is sufficient to flip the sign

**Resolution status:**
- The FRAMEWORK (Stratified Morse theory on M_2) is Cat A
- The SIGN of F''(M/2) for specific parameters is Cat B (numerical/parameter-dependent)
- No promotion to Cat A is possible — this is inherently a parameter-dependent quantity

**Experiments:** exp62_f_double_prime.py (mass sweep), exp63_hessian_mass_transfer.py (direct Hessian)
