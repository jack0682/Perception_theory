# Beyond-Weyl Singularity Structure: The ω_soft = 0 → ω_soft > 0 Transition

**Date:** 2026-04-08
**Category:** theory
**Status:** active
**Depends on:** BEYOND-WEYL-CATA-UPGRADE.md, KKT theory

---

## 1. The Singularity

The Beyond-Weyl improvement factor 1/ω_soft has a singularity:

$$\omega^{\text{soft}} = \begin{cases} 0 & d > d_{\text{crit}} \text{ (well-separated)} \\ >0 & d < d_{\text{crit}} \text{ (overlapping)} \end{cases}$$

At d = d_crit, ω_soft transitions from exactly 0 to positive. The improvement factor 1/ω_soft diverges:

$$\frac{1}{\omega^{\text{soft}}} \to \infty \quad \text{as } d \to d_{\text{crit}}^-$$

This is NOT a removable singularity — it reflects a genuine structural change in the coupling.

## 2. KKT Complementarity Structure

The singularity is a **KKT complementarity transition**. At formation minimizer û:

- For each site x: either û(x) > 0 (free, ν_x = 0) or û(x) = 0 (box-constrained, ν_x ≥ 0)
- ν_x is the KKT multiplier enforcing u_x ≥ 0

The **active set** A = {x : û(x) = 0} defines the box-constrained exterior.

As formations approach (d decreases):
- Tails of formation 1 reach sites in the support of formation 2
- At d = d_crit: a site x* in the overlap transitions from A (û(x*) = 0) to free (û(x*) > 0)
- At this transition: ν_{x*} = 0 AND û(x*) = 0 simultaneously — **strict complementarity fails**

This is a **degenerate KKT point** — the standard regularity theory (LICQ, strict complementarity) breaks down.

## 3. Singularity Set in Parameter Space

Define the singularity set:
$$\mathcal{S} = \{(d, \beta, \alpha, \lambda_{\text{rep}}, a_{\text{cl}}) : \exists x \in O_{12} \text{ with } \hat{u}_k(x) = 0,\; \nu_x = 0\}$$

This is a **codimension-1 hypersurface** in parameter space (one equation: the complementarity condition at the critical site).

On one side of S (d > d_crit):
- O ∩ F = ∅
- ω_soft = 0 (exactly)
- Coupling vanishes on soft modes
- μ_joint = min_k μ_k (no penalty)

On the other side (d < d_crit):
- O ∩ F ≠ ∅
- ω_soft > 0 (grows continuously from 0)
- Coupling begins to affect soft modes
- μ_joint < min_k μ_k

## 4. Continuity at the Transition

**ω_soft is continuous but not smooth at S:**

As d → d_crit from below:
- The critical site x* has û(x*) → 0⁺
- The soft mode weight on x*: |ψ_soft(x*)|² → 0 continuously
- Therefore ω_soft → 0 continuously

But the DERIVATIVE dω_soft/dd has a jump:
- d > d_crit: dω_soft/dd = 0 (identically zero)
- d < d_crit: dω_soft/dd < 0 (grows as tail penetrates)

**This is a "kink" — C⁰ but not C¹ at the transition.** Like a relu function.

## 5. Rate of Growth Below d_crit

For d slightly below d_crit, the critical site has:
$$\hat{u}(x^*) \sim (d_{\text{crit}} - d)^{1/2} \quad \text{(saddle-node scaling)}$$

or more precisely, from the screened Poisson tail:
$$\hat{u}(x^*) \sim A \cdot e^{-c_0 d} \cdot (d_{\text{crit}} - d)$$

The soft mode weight on the newly-freed site:
$$|\psi_{\text{soft}}(x^*)|^2 \sim \hat{u}(x^*)^2 / \|\psi_{\text{soft}}\|^2 \sim (d_{\text{crit}} - d)^2$$

Therefore near the transition:
$$\omega^{\text{soft}}(d) \sim C \cdot (d_{\text{crit}} - d)^2 \quad \text{for } d < d_{\text{crit}}$$

The improvement factor:
$$\frac{1}{\omega^{\text{soft}}} \sim \frac{1}{C(d_{\text{crit}} - d)^2} \to \infty$$

**Quadratic approach to the singularity.** The coupling penalty vanishes quadratically as formations separate.

## 6. Physical Interpretation

The singularity at d_crit represents a **phase transition in the coupling structure**:

| d > d_crit | d < d_crit |
|------------|------------|
| Formations are "invisible" to each other's Hessian | Formations "feel" each other via overlap |
| Coupling = 0 (exact decoupling) | Coupling > 0 (grows with overlap) |
| K-formation stability = per-formation stability | K-formation stability < per-formation stability |
| Repulsion λ_rep is irrelevant | Repulsion λ_rep affects stability |

This is the **perceptual analogue of resolution limit**: at d > d_crit, the two formations are completely independent "objects." At d < d_crit, they begin to interact and potentially merge.

**d_crit ≈ d_min** — the singularity in the Beyond-Weyl coupling coincides with the d_min resolution threshold. This is not a coincidence: both are determined by the same tail-overlap condition.

## 7. Connection to d_min

From the d_min existence proof:
- d_min is where the two-bump minimizer loses stability (Hessian zero eigenvalue)
- d_crit is where the coupling begins to affect the soft mode

These are the SAME threshold:
$$d_{\text{crit}} = d_{\min}$$

because the coupling vanishes on the reduced Hessian for d > d_crit, and the reduced Hessian is identical to two independent single-formation Hessians, which are positive definite (T7-Enhanced). So stability can only be lost when d ≤ d_crit, i.e., when coupling appears.

## 8. Stratified Structure

The parameter space has a natural stratification by the number of overlap-free-variable intersections:

$$\mathcal{M}_0 = \{O \cap F = \varnothing\} \quad \text{(generic stratum, open, ω = 0)}$$
$$\mathcal{S}_1 = \{|O \cap F| = 1\} \quad \text{(codim-1, first site enters)}$$
$$\mathcal{S}_2 = \{|O \cap F| = 2\} \quad \text{(codim-2, two sites)}$$
$$\vdots$$

This is a Whitney stratification of the parameter space, analogous to the M₂ stratification from the Stratified Morse Analysis (04-06).

The improvement factor:
- On M₀: 1/ω = ∞
- On S₁: 1/ω ~ 1/(d_crit - d)²
- Deep in the overlap: 1/ω ~ 1/ε_BMD ~ β (BMD theorem)
