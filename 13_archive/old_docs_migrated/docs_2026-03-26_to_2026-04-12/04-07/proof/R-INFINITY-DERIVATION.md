# Sharp-Limit Reorganization Volume |R_∞|: Analytical Derivation

**Date:** 2026-04-07
**Category:** proof
**Status:** complete
**Depends on:** BARRIER-EXPONENT.md (§3.2), Canonical Spec v2.1 §8 (Γ-convergence), multi.py K-field architecture
**Purpose:** Derive closed-form expression for A = |R_∞|/16 in the merge barrier ΔE = Aβ + B√β + O(1)

---

## 0. Summary

The merge barrier between K=2 and K=1 configurations has leading term (β/16)·|R_∞| where R_∞ = (S₁ ∪ S₂) △ S is the symmetric difference of supports in the sharp-interface limit. We derive:

$$|\mathcal{R}_\infty|(d_c) = 2m\bigl(1 - f(\rho)\bigr)$$

where m is total mass, ρ = d_c/r₁ is the normalized center-to-center distance, and f(ρ) is an explicit overlap fraction given by circle-circle intersection geometry.

**Critical observation (exp64):** |R_∞| is NOT a fixed geometric constant — it depends on which K=2 minimizer the optimizer converges to, specifically the separation d between the two formation centers. Poorly separated K=2 formations (d_c small) give |R_∞| ≈ 0 and barrier ≈ 0. Well-separated formations (d_c large) give |R_∞| ≈ 2m and maximum barrier. The formula below parameterizes this dependence explicitly.

**Energy decomposition (exp64):** The barrier at the interpolation midpoint (α ≈ 0.5) is dominated by the boundary-morphology energy E_bd (80–100% of total), with E_cl contributing a negative correction (−5 to −7, roughly −5%) and E_sep also negative (−3 to −6, roughly −5%). The net effect is a ~10–15% reduction from the pure E_bd prediction. See §10 for the corrected formula.

---

## 1. Setup

### 1.1 Sharp-Interface Formations on L×L Grid

On an L×L grid with n = L² nodes, total mass m = cL² (volume fraction c ∈ (0,1)):

**K=1 configuration:** Single formation, sharp-interface limit → characteristic function of a disk.
- Area: πr₁² = m, so **r₁ = √(m/π)**
- Center: grid center O = (L/2, L/2)

**K=2 configuration:** Two formations, each with mass m/2, sharp-interface → two disjoint disks.
- Area of each: πr₂² = m/2, so **r₂ = √(m/(2π)) = r₁/√2**
- Centers: p₁, p₂ placed symmetrically about O along the grid diagonal, at distance d_c from O
- Separation: d = 2d_c (by symmetry, |p₁ − O| = |p₂ − O| = d_c)

### 1.2 Symmetric Difference

$$\mathcal{R}_\infty = (S_1 \cup S_2)\;\triangle\; S$$

Since S₁, S₂ are well-separated (disjoint), |S₁ ∪ S₂| = |S₁| + |S₂| = m/2 + m/2 = m, and |S| = m. Therefore:

$$|\mathcal{R}_\infty| = |S_1 \cup S_2| + |S| - 2|S \cap (S_1 \cup S_2)| = 2m - 2\bigl(|S \cap S_1| + |S \cap S_2|\bigr)$$

By symmetry of placement, |S ∩ S₁| = |S ∩ S₂|. Define the **overlap area** I = |S ∩ S₁|. Then:

$$\boxed{|\mathcal{R}_\infty| = 2m - 4I}$$

The problem reduces to computing I = I(r₁, r₂, d_c): the intersection area of two circles with radii r₁ (K=1, centered at O) and r₂ (one K=2 formation, centered at distance d_c from O).

---

## 2. Circle-Circle Intersection

### 2.1 Standard Formula

For two circles with radii r, R and center separation d, the intersection area is:

$$A_{\cap}(r, R, d) = r^2 \cos^{-1}\!\left(\frac{d^2 + r^2 - R^2}{2dr}\right) + R^2 \cos^{-1}\!\left(\frac{d^2 + R^2 - r^2}{2dR}\right) - \frac{1}{2}\sqrt{(-d+r+R)(d+r-R)(d-r+R)(d+r+R)}$$

valid when |r − R| < d < r + R (partial overlap). The boundary cases:
- d ≤ |r − R|: smaller circle contained, A_∩ = π·min(r,R)²
- d ≥ r + R: disjoint, A_∩ = 0

### 2.2 Specialization to Our Geometry

Substituting r = r₁, R = r₂ = r₁/√2, d = d_c:

$$I(d_c) = r_1^2 \cos^{-1}\!\left(\frac{d_c^2 + r_1^2 - r_1^2/2}{2d_c r_1}\right) + \frac{r_1^2}{2}\cos^{-1}\!\left(\frac{d_c^2 + r_1^2/2 - r_1^2}{2d_c \cdot r_1/\sqrt{2}}\right) - \frac{1}{2}\sqrt{\Delta}$$

Simplifying the arguments:

$$\cos^{-1}\text{ arg 1} = \frac{d_c^2 + r_1^2/2}{2d_c r_1} = \frac{\rho^2 + 1/2}{2\rho}$$

$$\cos^{-1}\text{ arg 2} = \frac{d_c^2 - r_1^2/2}{2d_c \cdot r_1/\sqrt{2}} = \frac{\rho^2 - 1/2}{\rho\sqrt{2}}$$

where **ρ = d_c / r₁** is the dimensionless distance parameter.

### 2.3 Normalized Overlap Fraction

Define **f(ρ) = 2I(d_c)/m**, so that |R_∞| = 2m(1 − f(ρ)). Since I/m = I/(πr₁²), we have f = 2I/(πr₁²) = 4I/(2m). Expressing in terms of ρ:

$$f(\rho) = \frac{2}{\pi}\left[\cos^{-1}\!\left(\frac{\rho^2 + 1/2}{2\rho}\right) + \frac{1}{2}\cos^{-1}\!\left(\frac{\rho^2 - 1/2}{\rho\sqrt{2}}\right) - \frac{1}{2}\sqrt{\Delta'(\rho)}\right]$$

where:
$$\Delta'(\rho) = (-\rho + 1 + 1/\sqrt{2})(\rho + 1 - 1/\sqrt{2})(\rho - 1 + 1/\sqrt{2})(\rho + 1 + 1/\sqrt{2})$$

$$= \bigl[(1+1/\sqrt{2})^2 - \rho^2\bigr]\bigl[\rho^2 - (1-1/\sqrt{2})^2\bigr]$$

This is valid for the **partial overlap regime**: $(1 - 1/\sqrt{2}) < \rho < (1 + 1/\sqrt{2})$, i.e., **0.293 < ρ < 1.707**.

### 2.4 Boundary Cases

| Regime | Condition | f(ρ) | \|R_∞\| |
|--------|-----------|-------|----------|
| Containment | ρ ≤ 1 − 1/√2 ≈ 0.293 | f = 1 (K=2 disks inside K=1) | 0 |
| Partial overlap | 0.293 < ρ < 1.707 | f(ρ) via §2.3 | 2m(1−f) |
| Disjoint | ρ ≥ 1 + 1/√2 ≈ 1.707 | f = 0 | 2m |

---

## 3. The Reorganization Volume Formula

### 3.1 Master Formula

$$\boxed{|\mathcal{R}_\infty|(m, d_c) = 2m\bigl(1 - f(d_c / \sqrt{m/\pi})\bigr)}$$

or equivalently, with ρ = d_c√(π/m):

$$|\mathcal{R}_\infty| = 2m\left[1 - \frac{2}{\pi}\left(\cos^{-1}\!\left(\frac{\rho^2 + 1/2}{2\rho}\right) + \frac{1}{2}\cos^{-1}\!\left(\frac{\rho^2 - 1/2}{\rho\sqrt{2}}\right) - \frac{1}{2}\sqrt{\Delta'(\rho)}\right)\right]$$

### 3.2 The Merge Barrier Constant

$$A = \frac{|\mathcal{R}_\infty|}{16} = \frac{m}{8}\bigl(1 - f(\rho)\bigr)$$

This determines the leading coefficient of the merge barrier ΔE = Aβ + B√β + O(1).

---

## 4. Well-Separated Limit

When d_c >> r₁ + r₂, i.e., ρ >> 1 + 1/√2 ≈ 1.707:

$$f(\rho) = 0, \qquad |\mathcal{R}_\infty| = 2m, \qquad A = \frac{m}{8}$$

This is the **maximum barrier** configuration: the K=2 formations have zero overlap with the K=1 formation, so the entire mass must reorganize during a merge. The barrier is:

$$\Delta E_{\mathrm{merge}}^{\mathrm{max}} = \frac{m\beta}{8} + O(\sqrt{\beta})$$

---

## 5. Equilibrium Separation d_c*

The actual separation d_c* is determined by the energy balance between inter-formation repulsion (pushing K=2 formations apart) and boundary effects (penalizing proximity to grid edges). On an L×L grid:

### 5.1 Repulsion-Boundary Balance

The K=2 formations are placed along the grid diagonal at positions:
$$p_1 = (L/2 - \delta, L/2 - \delta), \quad p_2 = (L/2 + \delta, L/2 + \delta)$$

with d_c = δ√2. The formations must fit within the grid: the center of each K=2 disk is at least r₂ from the boundary, giving the constraint:

$$\delta \leq L/2 - r_2/\sqrt{2}$$

The maximum possible separation (corner-to-corner along diagonal):

$$d_c^{\max} = \frac{L - r_2\sqrt{2}}{\sqrt{2}} = \frac{L}{\sqrt{2}} - r_2$$

### 5.2 Practical Estimate

For strong repulsion λ_rep, the formations are pushed to the grid margins. The effective center-to-center distance is:

$$d_c^* \approx \frac{L}{\sqrt{2}} - r_2 - \varepsilon_{\mathrm{bd}}$$

where ε_bd is a small boundary correction (formations pulled inward to avoid energy cost of truncation against grid boundary). For the default parameters and moderate grid sizes, ε_bd ≈ 0.5–1.5r₂.

---

## 6. Numerical Verification: L = 15, c = 0.3

### 6.1 Parameters

- L = 15, n = 225, m = cL² = 0.3 × 225 = 67.5
- r₁ = √(67.5/π) = √(21.486) ≈ 4.636
- r₂ = r₁/√2 ≈ 3.278

### 6.2 Maximum Separation (Corner Placement)

$$d_c^{\max} = \frac{15}{\sqrt{2}} - 3.278 \approx 10.607 - 3.278 = 7.329$$

At this separation: ρ = 7.329/4.636 = 1.581. Since ρ < 1.707, this is still in the partial overlap regime!

$$\rho^2 = 2.499, \quad \frac{\rho^2 + 1/2}{2\rho} = \frac{2.999}{3.162} = 0.9485$$

$$\cos^{-1}(0.9485) = 0.3219 \text{ rad}$$

$$\frac{\rho^2 - 1/2}{\rho\sqrt{2}} = \frac{1.999}{2.236} = 0.8940$$

$$\cos^{-1}(0.8940) = 0.4671 \text{ rad}$$

$$\Delta' = [(1.707)^2 - (1.581)^2][(1.581)^2 - (0.293)^2] = [2.914 - 2.499][2.499 - 0.086] = 0.415 \times 2.413 = 1.001$$

$$f = \frac{2}{\pi}\left[0.3219 + 0.5 \times 0.4671 - 0.5\sqrt{1.001}\right] = \frac{2}{\pi}[0.3219 + 0.2336 - 0.5003] = \frac{2}{\pi}(0.0552) = 0.0351$$

$$|\mathcal{R}_\infty| = 2 \times 67.5 \times (1 - 0.0351) = 135 \times 0.965 = \mathbf{130.2}$$

This is **above** the 40–80 range, meaning the formations are NOT at maximum separation in practice.

### 6.3 Moderate Separation (Realistic Case)

The empirical range |R_∞| ≈ 40–80 requires f(ρ) ≈ 0.41–0.70. Solving numerically:

| d_c | ρ = d_c/r₁ | f(ρ) | \|R_∞\| | A = \|R_∞\|/16 |
|-----|------------|-------|----------|-----------------|
| 3.0 | 0.647 | 0.736 | 35.7 | 2.23 |
| 3.5 | 0.755 | 0.639 | 48.8 | 3.05 |
| 4.0 | 0.863 | 0.542 | 61.8 | 3.86 |
| 4.5 | 0.971 | 0.449 | 74.4 | 4.65 |
| 5.0 | 1.079 | 0.359 | 86.5 | 5.41 |
| 5.5 | 1.187 | 0.274 | 98.0 | 6.12 |
| 6.0 | 1.294 | 0.196 | 108.5 | 6.78 |

The **empirical range |R_∞| ≈ 40–80** corresponds to **d_c ≈ 3.5–4.5**, i.e., **ρ ≈ 0.75–0.97**.

This makes physical sense: the K=2 formation centers are at distance 0.75–0.97 times r₁ from the grid center, meaning the K=2 disks significantly overlap the K=1 disk (45–64% overlap fraction).

### 6.4 Detailed Computation at d_c = 4.0

Using the circle-circle intersection formula with r₁ = 4.636, r₂ = 3.278, d_c = 4.0:

$$I = r_1^2\,\theta_1 + r_2^2\,\theta_2 - \tfrac{1}{2}\sqrt{(-d_c + r_1 + r_2)(d_c + r_1 - r_2)(d_c - r_1 + r_2)(d_c + r_1 + r_2)}$$

| Quantity | Value |
|----------|-------|
| arg₁ = (d² + r₁² − r₂²)/(2dr₁) | 26.75/37.09 = 0.7210 |
| θ₁ = arccos(0.7210) | 0.7656 rad |
| arg₂ = (d² + r₂² − r₁²)/(2dr₂) | 5.25/26.22 = 0.2003 |
| θ₂ = arccos(0.2003) | 1.3688 rad |
| Triangle term | ½√(3.914 × 4.358 × 2.642 × 11.914) = 11.59 |
| **I** = 21.49(0.766) + 10.74(1.369) − 11.59 | **18.31** |

Per-disk overlap I = 18.31. Total: 4I = 73.22. (Python-verified.)

$$|\mathcal{R}_\infty| = 2(67.5) - 73.22 = \mathbf{61.8}$$

✓ **Within the empirical range of 40–80.**  Overlap fraction f = 73.22/135 = 0.542.

---

## 7. Closed-Form for Default Parameters

### 7.1 Default Configuration

For the SCC default parameters (λ_rep = 10.0, 15×15 grid, c = 0.3), the optimizer typically places K=2 formations with d_c ≈ 4.0 ± 0.5. Taking **d_c = 4.0** as the reference:

$$|\mathcal{R}_\infty| \approx 62 \text{ nodes}, \qquad A = \frac{62}{16} \approx 3.9$$

### 7.2 Sensitivity

The function |R_∞|(d_c) varies approximately linearly in the relevant range:

$$\frac{d|\mathcal{R}_\infty|}{dd_c} \approx 25 \text{ nodes per unit distance}$$

(computed from the table: (86.5 − 48.8)/(5.0 − 3.5) = 25.1). So a ±0.5 uncertainty in d_c translates to ±13 nodes in |R_∞|, consistent with the spread 40–80.

---

## 8. Scaling with Grid Size

### 8.1 Fixed Volume Fraction c

For fixed c (so m = cL²), as L → ∞:

- r₁ = √(cL²/π) = L√(c/π) — scales linearly with L
- d_c ∝ L (formations separate proportionally to grid size)
- ρ = d_c/r₁ → constant (determined by λ_rep and boundary conditions)

Therefore **|R_∞| ∝ m ∝ L²** and **A ∝ L²** — the merge barrier constant grows with system size.

### 8.2 Fixed Total Mass m

For fixed m as L → ∞:

- r₁, r₂ are fixed
- d_c → ∞ (repulsion pushes formations apart on the larger grid)
- ρ → ∞, so f → 0

Therefore |R_∞| → 2m and A → m/8 — the barrier saturates at the maximum value.

---

## 9. Summary

### Main Result

The sharp-limit reorganization volume is:

$$|\mathcal{R}_\infty| = 2m\left(1 - f\!\left(\frac{d_c}{\sqrt{m/\pi}}\right)\right)$$

where f(ρ) is the normalized overlap fraction from circle-circle intersection (§2.3), valid for 0.293 < ρ < 1.707, with f = 1 for ρ ≤ 0.293 and f = 0 for ρ ≥ 1.707.

### Key Values

| Quantity | Formula | L=15, c=0.3 value |
|----------|---------|-------------------|
| r₁ | √(m/π) | 4.64 |
| r₂ | r₁/√2 | 3.28 |
| d_c (typical) | ≈ L/(√2·κ) | ≈ 4.0 |
| ρ | d_c/r₁ | ≈ 0.86 |
| f(ρ) | §2.3 | ≈ 0.54 |
| \|R_∞\| | 2m(1−f) | ≈ 62 |
| A | \|R_∞\|/16 | ≈ 3.9 |
| ΔE_merge (leading) | Aβ | 3.9β |

### Limiting Cases

| Case | ρ | f | \|R_∞\| | A | Physical meaning |
|------|---|---|----------|---|------------------|
| Contained | < 0.29 | 1 | 0 | 0 | K=2 inside K=1, no reorganization |
| Typical | ≈ 0.86 | 0.54 | 62 | 3.9 | Partial overlap, moderate barrier |
| Well-separated | > 1.71 | 0 | 2m | m/8 | No overlap, maximum barrier |

### Merge Barrier (Complete)

$$\Delta E_{\mathrm{merge}} = \frac{\beta}{16}\cdot 2m(1 - f(\rho)) + B\sqrt{\beta} + O(1)$$

where B = (C_∂ − C_s)P√α is the net interface/smoothness correction from BARRIER-EXPONENT.md §3.5.

---

## 10. Multi-Energy Corrections (from exp64)

### 10.1 Barrier Decomposition

The merge barrier ΔE decomposes across energy terms at the interpolation midpoint α = 0.5:

$$\Delta E_{\mathrm{merge}} = \Delta E_{\mathrm{bd}} + \Delta E_{\mathrm{cl}} + \Delta E_{\mathrm{sep}}$$

Experiment exp64 reveals the following structure for well-separated K=2 formations:

| Term | Contribution | Sign | Fraction |
|------|-------------|------|----------|
| ΔE_bd (boundary/morphology) | +Aβ + B√β + ... | positive | 80–100% |
| ΔE_cl (closure) | −5 to −7 | **negative** | −5% |
| ΔE_sep (separation) | −3 to −6 | **negative** | −5 to −10% |

**Physical interpretation:** At the interpolation midpoint, the field is a superposition of K=2 and K=1 profiles. The boundary energy increases (mixing penalty from double-well), but:
- **Closure energy decreases** because the merged field has a more connected, cohesive support than two separated formations — the closure operator rewards spatial continuity.
- **Separation energy decreases** because the interpolated field has a broader, more diffuse profile that reduces the self-separation diagnostic.

### 10.2 Corrected Barrier Formula

Including the multi-energy corrections:

$$\Delta E_{\mathrm{merge}} = \underbrace{\frac{\beta}{16}\cdot 2m(1 - f(\rho))}_{\text{E_bd leading}} + \underbrace{B\sqrt{\beta}}_{\text{E_bd interface}} + \underbrace{\Delta E_{\mathrm{cl}} + \Delta E_{\mathrm{sep}}}_{\text{negative corrections}} + O(1)$$

The correction terms are approximately:

$$\Delta E_{\mathrm{cl}} + \Delta E_{\mathrm{sep}} \approx -\eta \cdot \Delta E_{\mathrm{bd}}$$

where η ≈ 0.10–0.15 is the **correction fraction**. Therefore:

$$\boxed{\Delta E_{\mathrm{merge}} \approx (1 - \eta)\left[\frac{\beta}{16}\cdot 2m(1 - f(\rho)) + B\sqrt{\beta}\right], \qquad \eta \approx 0.10\text{--}0.15}$$

### 10.3 Dependence on K=2 Formation Quality

**Key finding from exp64:** The barrier magnitude depends critically on the quality of the K=2 minimizer found by the optimizer. Specifically:

- **Well-separated K=2** (d_c ≈ 3.5–5.0, ρ ≈ 0.75–1.08): Full barrier, ΔE ~ 100–465 for β ∈ [20, 100]. The geometric derivation in §§1–6 applies.
- **Poorly separated K=2** (d_c < 2, ρ < 0.4): The two formations overlap significantly with each other and with the K=1 support. |R_∞| → 0 and barrier → 0. The K=2 configuration is essentially already near the K=1 basin.
- **Degenerate K=2** (one formation much smaller): The "K=2" minimizer is not truly two-formation; the mass is concentrated in one component. Barrier is near zero.

This means |R_∞| should be understood as a **function of the K=2 minimizer quality**, not a fixed geometric constant. The formula |R_∞|(d_c) = 2m(1 − f(d_c/r₁)) captures this dependence exactly.

---

## 11. Upper Bound on |R_∞|

### 11.1 Maximum Separation on L×L Grid

The maximum possible separation occurs when K=2 formations are at opposite corners of the grid diagonal, constrained to fit within the boundary:

$$d_c^{\max} = \frac{L}{\sqrt{2}} - r_2 = \frac{L}{\sqrt{2}} - \sqrt{\frac{m}{2\pi}}$$

The corresponding normalized distance:

$$\rho^{\max} = \frac{d_c^{\max}}{r_1} = \frac{L/\sqrt{2} - r_1/\sqrt{2}}{r_1} = \frac{L - r_1}{r_1\sqrt{2}} = \frac{1}{\sqrt{2}}\left(\frac{L}{r_1} - 1\right) = \frac{1}{\sqrt{2}}\left(\sqrt{\frac{\pi}{c}} - 1\right)$$

### 11.2 Upper Bound Formula

$$|\mathcal{R}_\infty|^{\max} = 2m\bigl(1 - f(\rho^{\max})\bigr)$$

For L = 15, c = 0.3: ρ^max = 1.581, which gives f(1.581) = 0.034, so:

$$|\mathcal{R}_\infty|^{\max} = 2(67.5)(1 - 0.034) = 130.4$$

$$A^{\max} = 130.4/16 = 8.15$$

### 11.3 Absolute Upper Bound

In the limit L → ∞ (or equivalently c → 0), ρ^max → ∞ and f → 0:

$$|\mathcal{R}_\infty|^{\mathrm{abs}} = 2m, \qquad A^{\mathrm{abs}} = \frac{m}{8}$$

This is the **absolute upper bound**: no geometric configuration can produce a larger reorganization volume than 2m, since |S₁ ∪ S₂| = m and |S| = m.

### 11.4 Summary of Bounds

For L = 15, c = 0.3 (m = 67.5):

| Configuration | d_c | ρ | \|R_∞\| | A | ΔE_merge/β |
|--------------|-----|---|----------|---|------------|
| Degenerate | < 1.4 | < 0.29 | 0 | 0 | 0 |
| Typical (optimizer) | 4.0 | 0.86 | 62 | 3.9 | 3.3–3.5 (with η) |
| Maximum (corner) | 7.3 | 1.58 | 130 | 8.2 | 6.9–7.3 (with η) |
| Absolute limit | ∞ | ∞ | 135 | 8.4 | 7.2–7.6 (with η) |

The "with η" column applies the 10–15% E_cl + E_sep correction.
