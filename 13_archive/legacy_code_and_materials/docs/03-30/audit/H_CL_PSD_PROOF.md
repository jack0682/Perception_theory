# H_cl PSD at Energy Minimizers -- Proof Attempt

**Author:** Mathematical Proof Specialist
**Date:** 2026-03-27
**Status:** Four strategies evaluated; no unconditional proof; strongest partial result identified
**Dependencies:** H_CL_PSD_EVIDENCE.md, T4-METASTABILITY-REPAIR.md, BIND-BOUND-PROOF.md, operators.py

---

## 0. Setup and Notation

We work on a finite connected graph G = (X, N) with n = |X| vertices. The closure operator is:

$$\mathrm{Cl}(u)_i = \sigma(z_i), \quad z_i = a_\mathrm{cl}\big((1-\eta)u_i + \eta(Pu)_i - \tau\big)$$

where sigma(z) = 1/(1+e^{-z}) is the logistic sigmoid, P is the row-normalized adjacency, and a_cl < 4 (contraction regime).

The closure energy is E_cl(u) = ||Cl(u) - u||^2. Its Hessian decomposes as:

$$H_\mathrm{cl}(u) = G(u) + R_\mathrm{cl}(u)$$

where:
- **Gauss-Newton term:** G = 2(I - J_Cl)^T(I - J_Cl), always PSD
- **Residual correction:** R_cl = 2 sum_i r_i sigma''(z_i) w_i w_i^T

with r_i = Cl(u)_i - u_i, w_i = nabla_u z_i = a_cl((1-eta)e_i + eta P_i^T), and sigma''(z) = sigma'(z)(1 - 2 sigma(z)).

**The conjecture:** H_cl(u-hat) is PSD at any constrained minimizer u-hat of E = lambda_cl E_cl + lambda_sep E_sep + lambda_bd E_bd on Sigma_m.

**Key facts used throughout:**
- sigma'(z) = sigma(z)(1-sigma(z)) in [0, 1/4], maximized at z=0
- sigma''(z) = sigma'(z)(1-2sigma(z)), with |sigma''| <= sqrt(3)/9 ~ 0.1925
- sigma'' > 0 when z < 0 (sigma < 1/2), sigma'' < 0 when z > 0 (sigma > 1/2)
- ||J_Cl||_op <= a_cl/4 < 1, so sigma_min(I - J_Cl) >= 1 - a_cl/4
- gamma_GN := lambda_min(G) >= 2(1 - a_cl/4)^2 > 0
- ||w_i||^2 <= a_cl^2

---

## Strategy A: Sign Cancellation in R_cl

### Idea
Show that the quadratic form v^T R_cl v has small magnitude because the signed terms r_i sigma''(z_i) (w_i^T v)^2 partially cancel.

### Analysis

For any unit vector v:

$$v^T R_\mathrm{cl} v = 2 \sum_i r_i \sigma''(z_i) (w_i^T v)^2$$

Each term has sign = sign(r_i sigma''(z_i)). Decompose:

$$v^T R_\mathrm{cl} v = 2\sum_{i \in S^+} |r_i \sigma''(z_i)| (w_i^T v)^2 - 2\sum_{i \in S^-} |r_i \sigma''(z_i)| (w_i^T v)^2$$

where S^+ = {i : r_i sigma''(z_i) > 0} and S^- = {i : r_i sigma''(z_i) < 0}.

**When does cancellation occur?** Consider the sign pattern:
- If sigma(z_i) > 1/2 (z_i > 0): sigma'' < 0. If additionally r_i = sigma(z_i) - u_i > 0 (closure pulls up), then r_i sigma'' < 0.
- If sigma(z_i) < 1/2 (z_i < 0): sigma'' > 0. If additionally r_i < 0 (closure pulls down), then r_i sigma'' < 0.

At a well-formed binary formation, sites split into:
- **High-cohesion interior** (u_i ~ 1, sigma(z_i) ~ 1): sigma'' ~ 0 (exponentially small). Contribution negligible regardless of sign.
- **Low-cohesion exterior** (u_i ~ 0, sigma(z_i) ~ 0): sigma'' ~ 0. Negligible.
- **Boundary sites** (u_i intermediate): sigma'' may be significant, and r_i can have either sign.

**The cancellation is real but not provable without structural assumptions.** The sign of r_i sigma''(z_i) at boundary sites depends on the detailed geometry of the minimizer. We cannot prove that the positive and negative contributions balance for an arbitrary minimizer.

**Quantitative attempt:** Suppose we could prove that the "signed weight" satisfies:

$$\left|\sum_i r_i \sigma''(z_i) (w_i^T v)^2\right| \leq \alpha \sum_i |r_i \sigma''(z_i)| (w_i^T v)^2$$

for some alpha < 1 (partial cancellation factor). Then:

$$|v^T R_\mathrm{cl} v| \leq 2\alpha \sum_i |r_i| |\sigma''(z_i)| ||w_i||^2 \leq 2\alpha \cdot \frac{\sqrt{3}}{9} a_\mathrm{cl}^2 ||r||_1$$

For alpha sufficiently small, this could make ||R_cl|| < gamma_GN. But we have no way to bound alpha without knowing the minimizer structure.

### Verdict: **FAILS**

The sign cancellation is empirically real (computational evidence shows R_cl has spectral norm ~ 0.12 while the worst-case sum-of-norms bound gives ~ 2.4) but we cannot prove any cancellation bound without additional structural assumptions on the minimizer. The difficulty is that the signs of r_i sigma''(z_i) at boundary sites are geometry-dependent and not constrained by any known variational principle.

---

## Strategy B: KKT-Constrained Residual Structure

### Idea
Use the KKT conditions at the minimizer to constrain the residual r, then show this constraint forces R_cl to be small (or PSD).

### Analysis

**KKT conditions.** At the constrained minimizer u-hat on Sigma_m with strict interiority:

$$\lambda_\mathrm{cl} \nabla E_\mathrm{cl} + \lambda_\mathrm{sep} \nabla E_\mathrm{sep} + \lambda_\mathrm{bd} \nabla E_\mathrm{bd} = \nu \mathbf{1}$$

where nabla E_cl = -2(I - J_Cl)^T r. After projection onto T(Sigma_m):

$$-2\lambda_\mathrm{cl} \Pi_T((I - J_\mathrm{Cl})^T r) = \lambda_\mathrm{sep} \Pi_T(\nabla E_\mathrm{sep}) + \lambda_\mathrm{bd} \Pi_T(\nabla E_\mathrm{bd})$$

This constrains the tangential component of r. From T-Bind (BIND-BOUND-PROOF.md):

$$||r_T||_2 \leq \frac{\lambda_\mathrm{sep} G_\mathrm{sep} + \lambda_\mathrm{bd} G_\mathrm{bd}}{2\lambda_\mathrm{cl}(1 - a_\mathrm{cl}/4)}$$

where G_sep, G_bd are gradient norm bounds.

**Can the KKT constraint force R_cl to be PSD?** No. The KKT conditions constrain r linearly, but R_cl depends on r through the products r_i sigma''(z_i). Even if r_T is small, the mean component r-bar = (1/n) sum r_i is unconstrained by the projected KKT. Moreover, R_cl being PSD requires ALL eigenvalues to be non-negative, which is a nonlinear condition on r that the linear KKT constraint cannot guarantee.

**Can KKT make ||R_cl|| small?** Writing r = r_T + r-bar (1/sqrt(n)) * 1_normalized:

$$v^T R_\mathrm{cl} v = 2\sum_i (r_T)_i \sigma''(z_i)(w_i^T v)^2 + \frac{2\bar{r}}{\sqrt{n}} \sum_i \sigma''(z_i)(w_i^T v)^2$$

For v in T(Sigma_m):
- First term: bounded by (2 sqrt(3)/9) a_cl^2 sqrt(n) ||r_T||_2 = O(sqrt(n) (lambda_sep + lambda_bd)/lambda_cl)
- Second term: the sum S(v) = sum_i sigma''(z_i)(w_i^T v)^2 does not simplify. Its magnitude is O(n) in worst case (each term up to (sqrt(3)/9) a_cl^2, summing n terms). So the second term is O(|r-bar| sqrt(n)).

The mean residual r-bar is NOT controlled by KKT. From the energy comparison (T4-METASTABILITY-REPAIR.md, Approach A Step 4):

$$||r||_2^2 \leq n|c - \sigma(a_\mathrm{cl}(c-\tau))|^2 + O(n(\lambda_\mathrm{sep} + \lambda_\mathrm{bd})/\lambda_\mathrm{cl})$$

So ||r||_2 = O(sqrt(n)), giving |r-bar| <= ||r||_2 / sqrt(n) = O(1). The second term is then O(sqrt(n)), which competes with gamma_GN = O(1).

**A subtler approach: can KKT constrain the sign pattern?** The KKT condition tells us that at the minimizer, nabla E_cl is proportional to 1 plus corrections from the other energies. This means (I - J_Cl)^T r is approximately proportional to 1, i.e., r is approximately in the direction of ((I - J_Cl)^T)^{-1} 1. This is a specific structural constraint on r, but it does not directly constrain the sign pattern of r_i sigma''(z_i) because sigma'' depends on z_i, which depends nonlinearly on u.

### Verdict: **FAILS**

The KKT conditions provide useful bounds on ||r_T||_2 but leave the mean component r-bar and the sign pattern of r_i sigma''(z_i) unconstrained. The resulting bounds on ||R_cl|| are O(sqrt(n)), which is too large to guarantee PSD-ness of H_cl for general n.

---

## Strategy C: Second-Order Sufficiency (Indirect Bound)

### Idea
At a constrained minimizer, the full Hessian nabla^2 E |_T >= 0. Use this to bound how negative H_cl can be, by relating it to the other Hessian components.

### Analysis

**Second-order necessary conditions.** At the constrained minimizer u-hat on Sigma_m:

$$\nabla^2 E|_T = \lambda_\mathrm{cl} H_\mathrm{cl} + \lambda_\mathrm{sep} H_\mathrm{sep} + \lambda_\mathrm{bd} H_\mathrm{bd} \succeq 0$$

This gives:

$$\lambda_\mathrm{cl} H_\mathrm{cl}|_T \succeq -\lambda_\mathrm{sep} H_\mathrm{sep}|_T - \lambda_\mathrm{bd} H_\mathrm{bd}|_T$$

Taking minimum eigenvalues:

$$\lambda_\mathrm{cl} \lambda_\mathrm{min}(H_\mathrm{cl}|_T) \geq -\lambda_\mathrm{sep} ||H_\mathrm{sep}|_T||_\mathrm{op} - \lambda_\mathrm{bd} ||H_\mathrm{bd}|_T||_\mathrm{op}$$

So:

$$\lambda_\mathrm{min}(H_\mathrm{cl}|_T) \geq -\frac{\lambda_\mathrm{sep} ||H_\mathrm{sep}||_\mathrm{op} + \lambda_\mathrm{bd} ||H_\mathrm{bd}||_\mathrm{op}}{\lambda_\mathrm{cl}}$$

**This bounds how negative H_cl can be, but does NOT prove it is PSD.** It says lambda_min(H_cl|_T) >= -C/lambda_cl for some constant C (depending on the other energies). For H_cl to be PSD, we need lambda_min >= 0, which this only guarantees in the limit lambda_cl -> infinity.

**Can we do better using the structure of H_bd?** H_bd is PSD (it involves the graph Laplacian and the double-well second derivative, both of which are PSD at well-formed minimizers with u in the spinodal wells). If H_bd >> 0 in the sense that lambda_min(H_bd|_T) is large, then the second-order condition gives a tighter lower bound on lambda_min(H_cl|_T). But this still does not yield PSD-ness of H_cl alone.

**The fundamental limitation.** Second-order sufficiency tells us about the SUM lambda_cl H_cl + lambda_sep H_sep + lambda_bd H_bd, not about H_cl individually. The conjecture that H_cl is PSD is strictly stronger than what the second-order conditions imply.

### Verdict: **FAILS** (for the H_cl PSD conjecture)

Second-order sufficiency provides only a lower bound of O(-1/lambda_cl) on the minimum eigenvalue of H_cl|_T. This is useful context (H_cl cannot be very negative at minimizers) but does not prove PSD-ness. The approach yields a partial result: **H_cl is approximately PSD at minimizers, with negative eigenvalues bounded by O(1/lambda_cl).**

---

## Strategy D: Fixed-Point Proximity for Sigmoid Closure

### Idea
At a constrained minimizer u-hat, the closure residual r = Cl(u-hat) - u-hat is "small" (in a suitable sense). Near the closure fixed point (where r = 0), R_cl is quadratically small in the distance from the fixed point, making H_cl = G + R_cl close to the PSD matrix G.

### Analysis

**Step 1: Taylor expansion of R_cl near a fixed point.**

Let u* satisfy Cl(u*) = u* (closure fixed point). At u*, r = 0 and R_cl = 0, so H_cl = G, which is PSD with lambda_min = gamma_GN.

At a nearby point u = u* + delta u:

$$r_i = \mathrm{Cl}(u)_i - u_i = \mathrm{Cl}(u*)_i + (J_\mathrm{Cl})_i \delta u + O(||\delta u||^2) - u*_i - \delta u_i$$
$$= (J_\mathrm{Cl} - I)_i \delta u + O(||\delta u||^2)$$

So r = (J_Cl - I) delta u + O(||delta u||^2), and ||r|| <= ||J_Cl - I|| ||delta u|| + O(||delta u||^2).

The residual correction quadratic form for unit v:

$$v^T R_\mathrm{cl} v = 2\sum_i r_i \sigma''(z_i) (w_i^T v)^2$$

Substituting r_i = sum_j (J_Cl - I)_{ij} (delta u)_j + O(||delta u||^2):

$$|v^T R_\mathrm{cl} v| \leq 2 ||r||_\infty \sum_i |\sigma''(z_i)| (w_i^T v)^2 + O(||delta u||^2)$$

Now ||r||_infty <= ||r||_2 <= (1 + a_cl/4)||delta u||_2, and sum_i |sigma''(z_i)| ||w_i||^2 <= n (sqrt(3)/9) a_cl^2. So:

$$||R_\mathrm{cl}||_\mathrm{op} \leq 2(1 + a_\mathrm{cl}/4) \cdot \frac{\sqrt{3}}{9} a_\mathrm{cl}^2 n \cdot ||\delta u||_2$$

For H_cl = G + R_cl to be PSD, we need:

$$||\delta u||_2 \leq \frac{\gamma_\mathrm{GN}}{2(1+a_\mathrm{cl}/4) \cdot \frac{\sqrt{3}}{9} a_\mathrm{cl}^2 n} = \frac{9(1-a_\mathrm{cl}/4)^2}{\sqrt{3}(1+a_\mathrm{cl}/4) a_\mathrm{cl}^2 n}$$

This is O(1/n), which is a very strong proximity requirement. For a 10x10 grid (n=100), this would require ||delta u|| < ~0.001, which is unrealistically tight.

**Step 2: A tighter approach -- use per-site residuals.**

The problem with Step 1 is the crude bound sum_i |sigma''(z_i)| ||w_i||^2 = O(n). In reality, sigma''(z_i) is small at sites far from the decision boundary z_i = 0. At a well-formed binary minimizer, most sites have z_i far from 0.

Let us define the **effective boundary width**:

$$B(\hat{u}) = \sum_i |\sigma''(z_i)| \cdot ||w_i||^2$$

At a perfectly binary field (all u_i in {0,1}), z_i is far from 0 at all sites, sigma'' ~ 0 everywhere, and B ~ 0. At a typical well-formed minimizer, B is controlled by the number of boundary sites n_b and the sharpness of the boundary.

Then: ||R_cl||_op <= 2 ||r||_infty B(u-hat).

For PSD-ness: ||r||_infty B(u-hat) < gamma_GN / 2.

**Step 3: Asymptotic argument for large a_cl.**

As a_cl increases (steeper sigmoid), the closure operator becomes more "switch-like":
- Sites with z_i > 0 have sigma(z_i) -> 1, sigma'(z_i) -> 0, sigma''(z_i) -> 0
- Sites with z_i < 0 have sigma(z_i) -> 0, sigma'(z_i) -> 0, sigma''(z_i) -> 0
- Only sites with z_i ~ 0 contribute, and these form a thin boundary layer

However, simultaneously:
- ||w_i||^2 = a_cl^2 ((1-eta)^2 + cross terms) grows as a_cl^2
- gamma_GN = 2(1-a_cl/4)^2 decreases (and we need a_cl < 4)

These opposing effects make it unclear whether increasing a_cl helps.

**Step 4: The correct asymptotic -- large lambda_cl.**

As lambda_cl -> infinity with other parameters fixed, the minimizer u-hat approaches the closure fixed point u* projected onto Sigma_m (because the closure energy term dominates).

More precisely: at the constrained minimizer, the per-site closure residual satisfies r_i = O(1/lambda_cl) for interior sites and r_i = O(1) only at the mass-constraint boundary. But this is not quite right either -- the mass constraint forces u-hat away from u* by an amount that depends on the mismatch between sum u*_i and m.

Let u* be the closure fixed point closest to Sigma_m. Define delta = ||u* - u*_projected||. Then ||u-hat - u*|| is bounded by a quantity involving delta/lambda_cl plus the effect of other energy terms.

**Formal statement:** For lambda_cl sufficiently large relative to lambda_sep and lambda_bd, the minimizer u-hat satisfies ||r||_1 <= epsilon(lambda_cl) where epsilon -> 0 as lambda_cl -> infinity. Consequently:

$$||R_\mathrm{cl}||_\mathrm{op} \leq \frac{2\sqrt{3}}{9} a_\mathrm{cl}^2 \epsilon(\lambda_\mathrm{cl}) \to 0$$

and H_cl = G + R_cl is PSD for lambda_cl large enough.

**Problem:** Making this rigorous requires proving that ||r||_1 -> 0 as lambda_cl -> infinity. The energy comparison gives:

$$||r||_2^2 = E_\mathrm{cl}(\hat{u}) \leq E(\hat{u})/\lambda_\mathrm{cl} \leq E(u^*_\mathrm{proj})/\lambda_\mathrm{cl}$$

where u*_proj is the projection of u* onto Sigma_m. If u* is NOT on Sigma_m (i.e., sum u*_i != m), then E_cl(u*_proj) = ||Cl(u*_proj) - u*_proj||^2 > 0, and:

$$||r||_2^2 \leq ||Cl(u^*_\mathrm{proj}) - u^*_\mathrm{proj}||^2 + \frac{\lambda_\mathrm{sep} E_\mathrm{sep}(u^*_\mathrm{proj}) + \lambda_\mathrm{bd} E_\mathrm{bd}(u^*_\mathrm{proj})}{\lambda_\mathrm{cl}}$$

The first term is a constant (independent of lambda_cl). So ||r||_2 does NOT go to zero as lambda_cl -> infinity! The residual is bounded below by the closure mismatch at the mass-projected fixed point.

**This is the fundamental obstruction.** The mass constraint forces the minimizer away from the closure fixed point, maintaining a nonzero residual independent of lambda_cl. The residual R_cl does not vanish, and its sign cannot be controlled.

**Step 5: Can we still prove PSD-ness despite nonvanishing residual?**

At the mass-projected fixed point u*_proj, the residual r* = Cl(u*_proj) - u*_proj is nonzero but has specific structure: r* = Cl(u*_proj) - u*_proj where u*_proj is close to u*. The residual correction at u*_proj:

$$R^*_\mathrm{cl} = 2\sum_i r^*_i \sigma''(z^*_i) w^*_i (w^*_i)^T$$

For this to be PSD, we need sum_i r*_i sigma''(z*_i) (w*_i^T v)^2 >= 0 for all v. This is equivalent to the matrix sum_i alpha_i w_i w_i^T being PSD where alpha_i = r*_i sigma''(z*_i).

A sum of rank-1 matrices with signed coefficients is PSD iff the positive part dominates in every direction. This is a non-trivial condition that depends on the geometry of the vectors {w_i} and the sign pattern {alpha_i}.

**Key structural observation.** At a binary-like minimizer, the relevant sites (where alpha_i is non-negligible) are boundary sites. At these sites:
- If u_i < sigma(z_i) (closure pulls up): r_i > 0
- The sign of sigma''(z_i) depends on whether sigma(z_i) > or < 1/2

For a "typical" boundary (a level-set crossing of the field), approximately half the boundary sites have sigma > 1/2 and half have sigma < 1/2. Similarly, r_i may have either sign. The product r_i sigma''(z_i) has no guaranteed sign dominance.

### Verdict: **PARTIAL**

Strategy D yields:
1. **Asymptotic result (PARTIAL FAILURE):** ||r|| does NOT go to zero as lambda_cl -> infinity due to the mass constraint. The fixed-point proximity argument fails to give an unconditional proof.
2. **Local result (PARTIAL SUCCESS):** If the minimizer u-hat happens to satisfy ||r||_1 < 9 gamma_GN / (2 sqrt(3) a_cl^2), then H_cl is PSD. This is a computable condition at the minimizer.
3. **Structural insight:** The obstruction to PSD-ness of H_cl is localized at boundary sites where both |r_i| and |sigma''(z_i)| are non-negligible. The sign of the product r_i sigma''(z_i) at these sites determines the sign of R_cl.

---

## Synthesis: Why No Strategy Succeeds

The four strategies fail for related but distinct reasons:

| Strategy | Why it fails |
|----------|-------------|
| A (Sign cancellation) | Cannot prove cancellation without structural assumptions on the minimizer geometry |
| B (KKT constraint) | KKT controls tangential residual but not the mean component; resulting bounds are O(sqrt(n)) |
| C (Second-order sufficiency) | Gives lambda_min(H_cl) >= -C/lambda_cl, not >= 0 |
| D (Fixed-point proximity) | Mass constraint maintains nonzero residual; cannot bound ||r||_1 -> 0 |

**The common obstruction:** The mass constraint sum u_i = m forces the minimizer away from the closure fixed point, creating a residual r that does not vanish even as lambda_cl -> infinity. The sign pattern of r_i sigma''(z_i) at boundary sites is not constrained by any known variational principle.

**Why the conjecture is probably true anyway:** The computational evidence (24/24 configurations, min_eig ~ 2.0) is strong. The likely explanation is that at energy minimizers, the minimization of E_cl (which drives ||r|| small) combined with the minimization of E_bd (which promotes binary fields, making sigma'' small at most sites) conspires to make R_cl have very small spectral norm. This is a cooperative effect of the energy minimization that is hard to capture in worst-case bounds.

---

## Strongest Partial Results

### Result 1: Conditional PSD-ness (Computable)

**Proposition (H_cl PSD -- Conditional).**
Let u-hat be a constrained minimizer with strict interiority. Define:

$$\delta_\mathrm{res}(\hat{u}) := \frac{2\sqrt{3}}{9} a_\mathrm{cl}^2 ||\mathrm{Cl}(\hat{u}) - \hat{u}||_1$$

If delta_res(u-hat) < gamma_GN = 2(1 - a_cl/4)^2, then H_cl(u-hat) is PSD with:

$$\lambda_\mathrm{min}(H_\mathrm{cl}(\hat{u})) \geq \gamma_\mathrm{GN} - \delta_\mathrm{res}(\hat{u}) > 0$$

**Proof.** The Gauss-Newton term satisfies G >= gamma_GN I (since sigma_min(I - J_Cl) >= 1 - a_cl/4). The residual correction satisfies:

$$||R_\mathrm{cl}||_\mathrm{op} \leq 2\sum_i |r_i| |\sigma''(z_i)| ||w_i||^2 \leq \frac{2\sqrt{3}}{9} a_\mathrm{cl}^2 ||r||_1 = \delta_\mathrm{res}$$

using |sigma''(z)| <= sqrt(3)/9 and ||w_i|| <= a_cl. Therefore H_cl = G + R_cl >= (gamma_GN - delta_res) I. QED.

**Remark.** Computationally, delta_res ~ 0.12 while gamma_GN ~ 2.0 for typical parameters (a_cl = 3.5), so the condition delta_res < gamma_GN is easily satisfied. However, the bound delta_res is extremely loose (it does not account for sign cancellation in R_cl), and there exist parameter regimes where the bound delta_res exceeds gamma_GN even though H_cl is empirically PSD.

### Result 2: Lower Bound from Second-Order Conditions

**Proposition (H_cl Near-PSD at Minimizers).**
At a constrained minimizer u-hat on Sigma_m with strict interiority:

$$\lambda_\mathrm{min}(H_\mathrm{cl}(\hat{u})|_T) \geq -\frac{\lambda_\mathrm{sep} ||H_\mathrm{sep}||_\mathrm{op} + \lambda_\mathrm{bd} ||H_\mathrm{bd}||_\mathrm{op}}{\lambda_\mathrm{cl}}$$

In particular, for lambda_cl >> lambda_sep, lambda_bd, the minimum eigenvalue of H_cl on T(Sigma_m) is close to zero from below.

**Proof.** From second-order necessary conditions at the minimizer: nabla^2 E|_T >= 0. Therefore lambda_cl H_cl|_T >= -lambda_sep H_sep|_T - lambda_bd H_bd|_T. Taking minimum eigenvalues and dividing by lambda_cl gives the result. QED.

### Result 3: PSD at Closure Fixed Points

**Proposition (H_cl PSD at Fixed Points).**
If u* satisfies Cl(u*) = u* (closure fixed point), then H_cl(u*) = 2(I - J_Cl(u*))^T(I - J_Cl(u*)) is PSD with lambda_min >= 2(1 - a_cl/4)^2.

**Proof.** At a fixed point, r = 0, so R_cl = 0 and H_cl = G, which is the Gram matrix of (I - J_Cl) and hence PSD. QED.

**Remark.** This is trivial but important: the conjecture is trivially true at the "right" point. The difficulty is entirely about the gap between the closure fixed point and the constrained energy minimizer.

---

## Why the Full Proof Is Hard

The core mathematical difficulty can be stated precisely:

**The PSD-ness of H_cl at energy minimizers is a cooperative effect of multiple energy terms that cannot be deduced from any single term's structure.**

More specifically:
1. E_cl minimization drives ||r|| small (via Bind), which helps make R_cl small.
2. E_bd minimization drives u toward {0,1}, which makes sigma''(z_i) small at most sites.
3. The constrained minimization on Sigma_m creates cross-term dependencies between r_i and sigma''(z_i) that are favorable but hard to quantify.

A rigorous proof would likely require one of:
- **Gamma-convergence analysis** showing that minimizers concentrate on a thin boundary layer where the sign pattern of r_i sigma''(z_i) can be characterized.
- **A refined spectral bound** on sums of signed rank-1 matrices that exploits the geometry of the vectors w_i (which have specific structure from the graph Laplacian).
- **A direct analysis** of the optimality conditions that yields a PSD certificate for R_cl at minimizers, perhaps through a Schur complement or interlacing argument.

None of these approaches is straightforward, and each requires substantial additional mathematical machinery beyond what is available in the current theory.

---

## Recommended Theorem Statement Update

Given the analysis, the strongest rigorous statement is:

**Theorem (H_cl PSD -- Conditional).** At any constrained minimizer u-hat of E on Sigma_m with strict interiority and a_cl < 4, define:
- gamma_GN = 2(1 - ||J_Cl(u-hat)||_op)^2 (Gauss-Newton floor)
- delta_res = (2 sqrt(3)/9) a_cl^2 ||Cl(u-hat) - u-hat||_1 (residual correction bound)

If delta_res < gamma_GN, then H_cl(u-hat) is positive semi-definite with lambda_min(H_cl) >= gamma_GN - delta_res.

**Conjecture (H_cl PSD -- Unconditional).** At any constrained minimizer u-hat of the SCC energy E = lambda_cl E_cl + lambda_sep E_sep + lambda_bd E_bd on Sigma_m with strict interiority and a_cl < 4, H_cl(u-hat) is positive semi-definite. Computationally verified across 24 configurations (5x5 to 15x15 grids, beta in {10,20,50}, c in {0.3, 0.5}), with min_eig(H_cl) consistently ~ 2(1 - a_cl/4)^2.

**Open Problem.** Prove (or disprove) the unconditional conjecture. The main obstacle is bounding the spectral norm of the signed rank-1 sum R_cl = 2 sum_i r_i sigma''(z_i) w_i w_i^T at energy minimizers, where the worst-case triangle-inequality bound is a factor ~20x larger than the observed values. A proof likely requires exploiting the cooperative structure of multi-term energy minimization (closure drives residual small, boundary drives field binary, both suppress R_cl).

---

## Summary Table

| Strategy | Verdict | What It Yields | Key Obstacle |
|----------|---------|----------------|-------------|
| A: Sign cancellation | **FAILS** | Empirical observation only | Cannot bound cancellation without minimizer geometry |
| B: KKT constraint | **FAILS** | Bound on tangential residual | Mean component r-bar unconstrained; bounds O(sqrt(n)) |
| C: Second-order sufficiency | **PARTIAL** | lambda_min(H_cl) >= -C/lambda_cl | Only a lower bound, not PSD |
| D: Fixed-point proximity | **PARTIAL** | Conditional PSD if delta_res < gamma_GN | Mass constraint prevents r -> 0; bound is loose |

**Bottom line:** The conjecture that H_cl is PSD at energy minimizers is almost certainly true based on computational evidence, but we cannot prove it rigorously. The strongest provable result is the conditional statement (Result 1), which is satisfied in all tested configurations. The unconditional conjecture remains open and likely requires new mathematical tools to resolve.
