# C_t Formalization — Rigor Auditor Pre-Audit: Cesàro vs Resolvent

**Author:** Rigor Auditor
**Date:** 2026-03-27
**Iteration:** 2, Round 6

---

## CRITICAL FINDING: Cesàro Form Is Fatally Flawed

For ergodic Markov chain on finite state space:

$$\frac{1}{N}\sum_{k=0}^{N-1} P^k(x,y) \to \pi(y) \text{ for all } x$$

This means C_t^Cesàro(x,y) = u(x)·π(y)·u(y) — the x-dependence factors through u(x) alone. All source points within a component yield the same ranking of targets. **Pairwise character destroyed.**

## RECOMMENDATION: Resolvent Form

$$G_\alpha = \alpha(I - (1-\alpha)P)^{-1} = \alpha\sum_{k=0}^{\infty} (1-\alpha)^k P^k$$

**Advantages:**
- Geometric decay preserves distance sensitivity
- α = walk termination probability (natural scale parameter)
- Spectral decomposition: upweights slow-mixing modes = formation structure
- Closed-form via matrix inversion

**Symmetry fix needed:** Use similarity transform $\hat{G}_\alpha = \Pi^{-1/2} G_\alpha \Pi^{1/2}$ (symmetric for reversible chains).

**C3 issue:** $C_t(x,x) = u(x)^2 G_\alpha(x,x)$ is bounded between $\alpha u(x)^2$ and $u(x)^2$ but not a pure function of u(x). C3 needs "local monotonicity" amendment.

## Candidate Comparison

| Candidate | Pairwise Info | Symmetry | C1 | C2 | C3 | Recommendation |
|-----------|--------------|----------|----|----|----|----|
| Cesàro | **LOST** | ✓ | ✓ | Technically | ✓ | **REJECT** |
| Resolvent | Preserved | Needs fix | ✓ | ✓ | Needs amendment | **ADOPT** |
| Finite-step | Preserved | Needs fix | ✓ | ✓ | Same issue | Viable alt |
