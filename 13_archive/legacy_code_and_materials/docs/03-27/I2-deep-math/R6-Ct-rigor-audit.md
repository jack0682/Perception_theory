# C_t Formalization — Rigor Auditor Complete Audit

**Author:** Rigor Auditor
**Date:** 2026-03-27
**Iteration:** 2, Round 6

---

## Audit Verdicts

| Item | Verdict |
|------|---------|
| C3 monotonicity proof | **VALID** — u(x) cancels from outgoing, increases incoming |
| Cesàro as C_t form | **AXIOM-COMPLIANT but STRUCTURALLY DEFICIENT** |
| Sep reformulation | **STRUCTURAL IMPROVEMENT** — threshold arbitrary |
| C2 witnesses | **SUFFICIENT** — minimal existence proofs |

## CRITICAL FINDING: Cesàro Degeneration

Within connected components: P̄(x,y) → π(y) regardless of source x.
C_t(x,y) = u(x)·π(y)·u(y) — x-dependence only through u(x), no path structure.

**Consequence:** Same-component pairs all get same rank ordering. Within-formation distance information DESTROYED.

- Cross-formation discrimination: ✓ (different components → zero)
- Within-formation pairwise info: ✗ (degenerate)
- Sep reformulation: ✓ (only uses C_t(x,x) = u(x)²π(x), which is meaningful)
- Multi-formation decomposition (T12): ✗ (reduces to connected component detection)

## RECOMMENDATION: Switch to Resolvent

$$G_\alpha = \alpha(I - (1-\alpha)P)^{-1}$$

- Preserves distance sensitivity via geometric decay (1-α)^k
- α = co-belonging scale (natural parameter)
- C3 monotonicity carries over (same cancellation argument)
- Symmetrize via similarity transform: Ĝ = Π^{-1/2} G_α Π^{1/2}

## C3 Second Amendment Needed

Current: "C_t(x,x) = f(u(x)) for monotone f"
Problem: C_t(x,x) depends on ENTIRE field, not just u(x)
Amended: "C_t(x,x) is monotone increasing in u(x) with other values fixed, satisfying αu(x)² ≤ C_t(x,x) ≤ u(x)²"

## Symmetry Issue

‖C_t - C_tᵀ‖ = 0.058. No axiom explicitly requires symmetry. But co-belonging should be symmetric conceptually. Resolvent similarity transform fixes this. Post-hoc symmetrization also viable.
