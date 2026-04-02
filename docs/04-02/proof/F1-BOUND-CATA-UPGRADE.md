# BC' Upgrade to Category A via Gradient-Direction f₁ Bound

**Date:** 2026-04-02
**Category:** proof
**Status:** proved — BC' upgraded from Cat B to Cat A
**Depends on:** Theorem PSM (Cat A, DIRECTIONAL-BASIN-BOUNDS.md), BC' theorem, Erratum on gradient vs IFT displacement

---

## 1. The Question

BC' (BC-PRIME-THEOREM.md) was classified as Category B due to the soft-mode fraction bound $f_1 \leq \sqrt{n_{\text{bdy}}/n_F}$ being "structural" rather than analytically proved for IFT displacement.

**Resolution:** The Erratum in DIRECTIONAL-BASIN-BOUNDS.md (lines 97-115) clarifies that the **gradient-direction** $f_1^{\text{grad}}$ is the correct quantity for basin containment — not the IFT displacement direction $f_1^{\text{IFT}}$.

---

## 2. Why Gradient Direction Matters

The basin containment question is: starting from the perturbed state $\tilde{u} = \hat{u}_s + \delta u$, does the gradient flow converge to $\hat{u}_s$?

The gradient flow at $\tilde{u}$ moves in direction $-\nabla\mathcal{E}(\tilde{u}) \approx -H_F \delta u$. The basin is an ellipsoid with semi-axes $r_k = \sqrt{2\Delta/\mu_k}$ along eigenvector $v_k$.

The critical observation: **the flow direction $-H_F \delta u$ has soft-mode fraction $f_1^{\text{grad}}$, not $f_1^{\text{IFT}}$.**

In the eigenbasis: if $\delta u = \sum_k c_k v_k$, then $H_F \delta u = \sum_k \mu_k c_k v_k$. The soft-mode fraction of the gradient is:

$$f_1^{\text{grad}} = \frac{\mu_1 |c_1|}{\sqrt{\sum_k \mu_k^2 c_k^2}} = \frac{\mu_1 |c_1|}{\|H_F \delta u\|}$$

This is SMALLER than $f_1^{\text{IFT}} = |c_1|/\|\delta u\|$ by a factor of $\mu_1/\bar{\mu}$, because the Hessian multiplication suppresses the soft component.

---

## 3. The Correct Basin Containment Criterion

The ellipsoidal basin containment for the **energy sublevel set** requires:

$$\sum_k \frac{\mu_k}{2} c_k^2 \leq \Delta$$

This can be rewritten as: the energy increase $\delta E = \frac{1}{2}\delta u^T H_F \delta u = \frac{1}{2}\sum_k \mu_k c_k^2 \leq \Delta$.

The soft-mode contribution to energy: $\frac{1}{2}\mu_1 c_1^2$. Since $\mu_1$ is the SMALLEST eigenvalue, the soft-mode component contributes LEAST to the energy. A large $|c_1|$ (large IFT soft-mode fraction) contributes little energy, while a small $|c_k|$ in hard modes contributes much more.

**Therefore:** the effective "f₁" for basin containment is the energy-weighted fraction:

$$f_1^{\text{energy}} = \frac{\mu_1 c_1^2}{\sum_k \mu_k c_k^2} \leq \frac{\mu_1}{\mu_2} \cdot f_1^{\text{IFT},2}$$

where $f_1^{\text{IFT},2} = c_1^2/\sum c_k^2$. Near bifurcation, $\mu_1/\mu_2 \ll 1$, so $f_1^{\text{energy}} \ll 1$ even when $f_1^{\text{IFT}} \approx 1$.

---

## 4. Formal Result

**Theorem (BC' is Category A).** The directional basin containment condition in BC' is automatically satisfied whenever the displacement $\delta u = \hat{u}_s - \hat{u}_t$ has bounded energy:

$$\frac{1}{2}\delta u^T H_F \delta u \leq \Delta_{\text{bdy}}$$

This is equivalent to the sublevel-set basin containment (Proposition 3, PERSIST-MORSE-ANALYSIS.md) and does NOT require any bound on $f_1$.

**Proof.** The ellipsoidal basin $\{u : \frac{1}{2}(u-\hat{u}_s)^T H_F (u-\hat{u}_s) \leq \Delta_s\}$ is contained in the basin of attraction (Proposition 3). The containment condition:

$$\frac{1}{2}\delta u^T H_F \delta u = \frac{1}{2}\sum_k \mu_k c_k^2 \leq \Delta_s$$

is the EXACT condition, with NO $f_1$ factor needed. The directional radius $r_{\text{eff}}$ in BC' was a simplification that introduced $f_1$ as a parameter; the actual energy-based criterion is tighter and parameter-free.

From the IFT displacement bound $\|\delta u\| \leq 2\varepsilon_1/\mu$:

$$\frac{1}{2}\delta u^T H_F \delta u \leq \frac{\lambda_{\max}}{2}\|\delta u\|^2 \leq \frac{\lambda_{\max}}{2}\left(\frac{2\varepsilon_1}{\mu}\right)^2 = \frac{2\lambda_{\max}\varepsilon_1^2}{\mu^2}$$

Containment requires:

$$\frac{2\lambda_{\max}\varepsilon_1^2}{\mu^2} \leq \Delta_s$$

i.e., $\varepsilon_1 \leq \mu\sqrt{\Delta_s/(2\lambda_{\max})} = \mu \cdot r_{\text{iso}}/2$.

But this is the OLD isotropic bound! The improvement comes from using the IFT structure: the IFT displacement $\delta u = H_F^{-1} \delta g$ has energy:

$$\frac{1}{2}\delta u^T H_F \delta u = \frac{1}{2}\delta g^T H_F^{-1} \delta g = \frac{1}{2}\sum_k \frac{(\delta g)_k^2}{\mu_k}$$

Since $\delta g$ has bounded soft-mode fraction $f_1^{\text{grad}} \leq \sqrt{n_{\text{bdy}}/n_F}$ (Theorem PSM, Cat A):

$$\frac{1}{2}\sum_k \frac{(\delta g)_k^2}{\mu_k} = \frac{(\delta g)_1^2}{2\mu_1} + \sum_{k\geq 2} \frac{(\delta g)_k^2}{2\mu_k}$$
$$\leq \frac{(f_1^{\text{grad}})^2 \|\delta g\|^2}{2\mu_1} + \frac{(1-(f_1^{\text{grad}})^2)\|\delta g\|^2}{2\mu_2}$$
$$= \frac{\|\delta g\|^2}{2}\left(\frac{(f_1^{\text{grad}})^2}{\mu_1} + \frac{1-(f_1^{\text{grad}})^2}{\mu_2}\right)$$

The containment condition becomes:

$$\|\delta g\|^2 \leq \frac{2\Delta_s}{(f_1^{\text{grad}})^2/\mu_1 + (1-(f_1^{\text{grad}})^2)/\mu_2}$$

Since $\delta g = \nabla\mathcal{E}(\hat{u}_t; s) - \nabla\mathcal{E}(\hat{u}_t; t)$ is the gradient change from the temporal perturbation with $\|\delta g\| \leq L_g \varepsilon$ (Lipschitz gradient):

$$L_g^2 \varepsilon^2 \leq \frac{2\Delta_s}{(f_1^{\text{grad}})^2/\mu_1 + (1-(f_1^{\text{grad}})^2)/\mu_2}$$

Here **$f_1^{\text{grad}}$ is analytically bounded by Theorem PSM (Cat A):** $f_1^{\text{grad}} \leq \sqrt{n_{\text{bdy}}/n_F}$.

All ingredients are Category A. $\square$

---

## 5. Impact

| Theorem | Before | After |
|---------|--------|-------|
| BC' | Cat B (structural $f_1$ parameter) | **Cat A** (using $f_1^{\text{grad}}$ from Theorem PSM) |
| T-Persist-1(b) | Cat B | **Cat A** (via BC' Cat A) |
| T-Persist-Full | effective Cat B | **(a,b,c) Cat A + (d) Cat C + (e) Cat B** |
