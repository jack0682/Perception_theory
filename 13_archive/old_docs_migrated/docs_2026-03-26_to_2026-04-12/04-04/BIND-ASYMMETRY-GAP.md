# Binary Approximation Gap Analysis: Why $\bar{r}_0$ is O(1) at τ = 1/2

**Date:** 2026-04-04  
**Phase:** 13 — T-Bind-Proj General τ  
**Author:** Perturbation Analyst  
**Status:** REVISED (post-Task #1 validation)  
**Dependencies:** R-BAR-BOUND.md (Phase 6), BIND-PERTURBATION-THEORY.md (this phase)  
**Revision Note:** Original version assumed the cancellation mechanism works at τ=1/2 for all c. Task #1 data disproves this. This revision explains the correct picture.

---

## 1. Purpose

This document explains the structure of the mean closure residual $\bar{r}_0(\tau)$:
- Why $\bar{r}_0$ is $O(1)$ for generic $(\tau, c)$ pairs
- Why $\bar{r}_0 = O(n^{-1/d})$ only at the volume-compatible threshold $\tau = \tau^*$
- Why R-BAR-BOUND Theorem 6.1 incorrectly claimed $O(n^{-1/d})$ at $\tau = 1/2$
- The correct decomposition of the residual into bulk and boundary terms

---

## 2. The Two Sources of Mass Imbalance

### 2.1 Source 1: Operator asymmetry ($\delta_+ \neq \delta_-$)

The closure operator maps:
- Core ($u \approx 1$) downward by $\delta_+ = 1 - \sigma(a(1-\tau))$ per site
- Exterior ($u \approx 0$) upward by $\delta_- = 1 - \sigma(a\tau)$ per site

At $\tau = 1/2$: $\delta_+ = \delta_-$ (sigmoid symmetry). The operator treats core and exterior symmetrically.

At $\tau \neq 1/2$: $\delta_+ \neq \delta_-$. The operator has different pull strengths on core vs exterior.

### 2.2 Source 2: Population asymmetry ($c \neq 1/2$)

Even when the operator is symmetric ($\delta_+ = \delta_-$), the net mass transfer is:

$$\text{Net mass} = -(cn)\delta_+ + ((1-c)n)\delta_- = n\delta_{\text{sym}}(1 - 2c)$$

This is nonzero whenever $c \neq 1/2$: there are more exterior sites than core sites, so the net mass transfer (closure pushing exterior up) exceeds the reverse transfer (closure pulling core down).

### 2.3 The two-dimensional symmetry requirement

$\bar{r}_0 = O(n^{-1/d})$ requires BOTH symmetries simultaneously:
- Operator symmetry: $\delta_+ = \delta_-$ (requires $\tau = 1/2$)
- Population symmetry: $c = 1/2$ (requires balanced volume)

OR: the single condition that the two asymmetries cancel:
- $(1-c)\delta_- = c\delta_+$ (requires $\tau = \tau^*(c)$)

This is the key insight that R-BAR-BOUND missed: sigmoid symmetry at τ = 1/2 eliminates source 1 but NOT source 2.

---

## 3. The Correct Cancellation Mechanism

### 3.1 Bulk mass-balance identity

At a near-binary minimizer (R-BAR-BOUND Proposition 4.1):

$$n\bar{r}_0 = \left|-(cn)\delta_+ + ((1-c)n)\delta_- + \sum_{i \in \mathcal{T}} r_i\right|$$

The bulk term: $B(\tau, c) = (1-c)\delta_-(\tau) - c\,\delta_+(\tau)$

The transition correction: $T_n = \frac{1}{n}\sum_{i \in \mathcal{T}} r_i = O(|\partial\text{Core}|/n) = O(n^{-1/d})$

$$\bar{r}_0(\tau) = |B(\tau, c)| + O(n^{-1/d})$$

### 3.2 When the bulk term vanishes

$B(\tau, c) = 0$ requires:

$$(1-c)(1-\sigma(a\tau)) = c(1-\sigma(a(1-\tau)))$$

This defines the curve $\tau = \tau^*(c)$ in the $(\tau, c)$ plane. On this curve (and only on it), the bulk contribution vanishes and $\bar{r}_0 = O(n^{-1/d})$.

### 3.3 The τ = 1/2 case

At $\tau = 1/2$: $\delta_+ = \delta_- \equiv \delta$, so $B(1/2, c) = \delta(1-2c)$.

- If $c = 1/2$: $B = 0$ ✓ (both symmetries satisfied)
- If $c \neq 1/2$: $B = \delta|1-2c| > 0$ ✗ (population asymmetry persists)

For $c = 0.3$, $a = 3.5$: $B(1/2, 0.3) = 0.148 \times 0.4 = 0.059$ — exactly matching exp58.

---

## 4. Where R-BAR-BOUND Goes Wrong

### 4.1 The faulty cancellation claim

R-BAR-BOUND §5.6 states: *"The critical observation is that in (⋆), the dominant O(1) terms in ν and the energy gradient sums cancel when combined through the identity, leaving only O(n^{-1/d}) residuals."*

This is wrong. The KKT identity (Prop 5.1) is exact:

$$\bar{r}_0 = \frac{|F|}{2\lambda_{\mathrm{cl}}(1-\overline{a_{\mathrm{cl}} s})}$$

where $F$ involves $\nu$, sep/bd gradient means, and $\operatorname{Cov}(s,r)$.

### 4.2 The actual structure of F

$F$ can be rewritten as:

$$F = \underbrace{\frac{1}{n}\bigl[\lambda_{\mathrm{sep}}\mathbf{1}^T\nabla\mathcal{E}_{\mathrm{sep}} + \lambda_{\mathrm{bd}}\mathbf{1}^T\nabla\mathcal{E}_{\mathrm{bd}}\bigr]}_{\text{non-closure gradient mean}} \underbrace{- \nu}_{\text{Lagrange mult.}} + \underbrace{\frac{2\lambda_{\mathrm{cl}} a_{\mathrm{cl}}}{n}\operatorname{Cov}(s,r)}_{\text{covariance correction}}$$

Wait — from KKT: $\nu = \frac{1}{n}[\lambda_{\mathrm{cl}}\mathbf{1}^T\nabla\mathcal{E}_{\mathrm{cl}} + \lambda_{\mathrm{sep}}\mathbf{1}^T\nabla\mathcal{E}_{\mathrm{sep}} + \lambda_{\mathrm{bd}}\mathbf{1}^T\nabla\mathcal{E}_{\mathrm{bd}}]$

Substituting $\mathbf{1}^T\nabla\mathcal{E}_{\mathrm{cl}} = 2[(\overline{a_{\mathrm{cl}} s}-1)n\bar{r}_0\cdot\text{sgn} + a_{\mathrm{cl}}\operatorname{Cov}(s,r)]$:

The $\nu$ in $F$ already contains the closure gradient contribution, which is itself proportional to $\bar{r}_0$. When you solve the self-consistency equation, the $\bar{r}_0$-dependent parts cancel (this is correct — Prop 5.1 is an identity, not a bound).

**The remaining terms** are the non-closure gradient means minus their projection through the covariance structure. These are O(1) generically and do NOT cancel unless specific parameter conditions are met.

### 4.3 The specific error

R-BAR-BOUND §5.6 implicitly assumed that at $\tau = 1/2$:
1. The covariance $\operatorname{Cov}(s,r)/n = O(n^{-1/d})$ ← **TRUE** (sigmoid symmetry gives $s_+ = s_-$)
2. The remaining non-closure gradient means cancel ← **FALSE** for $c \neq 1/2$

The non-closure gradient means don't cancel because:
- $\mathbf{1}^T\nabla\mathcal{E}_{\mathrm{sep}}/n$ depends on the sep energy landscape, which is asymmetric in c
- $\mathbf{1}^T\nabla\mathcal{E}_{\mathrm{bd}}/n = \beta S_W/n$ is small for near-binary profiles
- But the combination of all terms, after solving the self-consistency, yields $|F|$ proportional to the bulk mass-balance $|B(\tau, c)|$

**In short:** The Proposition 5.1 identity is correct. The bound on $|F|$ claimed in Theorem 6.1 is wrong. The actual $|F|$ encodes the bulk mass imbalance and is $O(1)$ when $B \neq 0$.

---

## 5. Corrected Residual Decomposition

### 5.1 The clean decomposition

$$\bar{r}_0(\tau) = \underbrace{\Phi(\tau; a, c)}_{\text{bulk mass-balance (O(1))}} + \underbrace{O(n^{-1/d})}_{\text{transition layer}}$$

where $\Phi(\tau; a, c) = |(1-c)(1-\sigma(a\tau)) - c(1-\sigma(a(1-\tau)))|$.

**There is no "perfect cancellation + asymmetry correction" structure** for generic τ. The O(1) bulk term is always present unless $\tau = \tau^*$.

### 5.2 Interpretation by source

| Condition | Source 1 (operator) | Source 2 (population) | $\bar{r}_0$ |
|-----------|--------------------|-----------------------|---|
| $\tau = 1/2, c = 1/2$ | ✓ symmetric | ✓ balanced | $O(n^{-1/d})$ |
| $\tau = 1/2, c \neq 1/2$ | ✓ symmetric | ✗ unbalanced | $O(1)$ |
| $\tau = \tau^*, c$ any | ✗ asymmetric | ✗ unbalanced | $O(n^{-1/d})$* |
| generic $\tau, c$ | ✗ asymmetric | ✗ unbalanced | $O(1)$ |

*At τ = τ\*, the two asymmetries cancel: $(1-c)\delta_- = c\delta_+$.

### 5.3 Why the asymmetry correction is irreducible

The bulk mass-balance is a **structural property** of the closure operator and volume constraint, not a consequence of the field shape. No field adjustment within $\Sigma_m$ can eliminate it:

**Proposition.** For any field $u \in \Sigma_m$ (not necessarily a minimizer) with a core-exterior partition satisfying $\sum_{i \in \mathcal{C}} 1 = cn + O(\sqrt{n})$ and $|\mathcal{T}| = O(n^{(d-1)/d})$:

$$\bar{r}_0(u) \geq |B(\tau, c)| - O(n^{-1/d}) - O(\text{max field deviation from binary})$$

The field deviation from binary is bounded by the competition between $\mathcal{E}_{\mathrm{cl}}$ (favoring closure fixed point) and $\mathcal{E}_{\mathrm{bd}}$ (favoring sharp interfaces). At energy minimizers, this deviation is small ($O(\lambda_{\mathrm{cl}}/\lambda_{\mathrm{bd}})$), and the bulk mass-balance dominates.

---

## 6. Consistency with Perturbation Theory (Task #2)

### 6.1 Cross-check

The revised BIND-PERTURBATION-THEORY.md now correctly identifies:
- $\bar{r}_0(\tau) = \Phi(\tau; a, c) + O(n^{-1/d})$
- The perturbation expansion around $\tau^*$ gives linear growth $|\Phi'(\tau^*)| \cdot |\tau - \tau^*|$
- The expansion around $\tau = 1/2$ starts from a nonzero baseline $\Phi(1/2) = \delta_{\rm sym}|1-2c|$

Both documents are now consistent.

### 6.2 Growth rate

The growth rate away from $\tau^*$ is linear: $\bar{r}_0 \approx |\Phi'(\tau^*)| \cdot |\tau - \tau^*|$ near $\tau^*$.

Away from $\tau^*$, the growth follows the nonlinear sigmoid structure of $\Phi$. The function $\Phi(\tau)$ is smooth, bounded by $\max(c, 1-c)$ (since $\delta_\pm \leq 1$), and vanishes only at $\tau = \tau^*$.

---

## 7. Summary

### The correct picture:

1. **$\bar{r}_0$ is O(1) at ALL generic parameter values**, including τ = 1/2 with c ≠ 1/2.
2. **$\bar{r}_0 = O(n^{-1/d})$ only at the volume-compatible threshold** $\tau = \tau^*(c)$.
3. **The binary mass-balance formula** $\Phi(\tau; a, c)$ captures the O(1) bulk term with R² ≈ 0.995.
4. **R-BAR-BOUND Theorem 6.1 has a gap:** it incorrectly claimed O(n^{-1/d}) at τ=1/2 for all c.
5. **T-Bind can still be Category A** because $\bar{r}_0$ is now an explicit, computable function of parameters.

### What was wrong in the original analysis:

The original (pre-revision) gap analysis assumed τ = 1/2 as the center of symmetry and analyzed how the cancellation "breaks down" at τ ≠ 1/2. This framing was incorrect: the cancellation was never present at τ = 1/2 for c ≠ 1/2 in the first place. The sigmoid derivative symmetry ($s_+ = s_-$) at τ = 1/2 is real but irrelevant — it affects the covariance term but not the dominant bulk mass-balance.

### The correct framing:

The cancellation mechanism operates at $\tau^*$, where the two sources of mass imbalance (operator asymmetry and population asymmetry) exactly offset. The special point τ = 1/2 only coincides with τ\* when $c = 1/2$. For the default $c = 0.3$, the correct special point is $\tau^* \approx 0.643$.

### Quantitative results (defaults: $a = 3.5, c = 0.3$):

| τ | $\Phi(\tau)$ | $\bar{r}_0$ (exp58, 20×20) | Status |
|---|---|---|---|
| 0.50 | 0.059 | 0.060 | O(1) — NOT special |
| 0.643 (τ\*) | 0.000 | ~0.005 | O(n^{-1/d}) — special |
| 0.30 | 0.158 | 0.163 | O(1) |
| 0.70 | 0.022 | 0.027 | O(1) but small |
