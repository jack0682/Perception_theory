# Predicate-Energy Bridge — Proof Strategist Complete Proof

**Author:** Proof Strategist
**Date:** 2026-03-27
**Iteration:** 2, Round 12

---

## THE BRIDGE THEOREM

Near-minimizers of the SCC energy satisfy proto-cohesion predicates.

### Bind Bridge
$$\mathrm{Bind}(u) \geq 1 - \sqrt{\mathcal{E}_{\mathrm{cl}}(u)/n}$$
Cauchy-Schwarz. Rate: O(√δ). If using ℓ² Bind: exact equality Bind_ℓ² = 1 - E_cl/n.

### Sep Bridge (STRONGEST — exact equality)
$$\boxed{\mathrm{Sep}(u) = 1 - \mathcal{E}_{\mathrm{sep}}(u)/m}$$
Linear. Small E_sep directly implies high Sep. No approximation.

### Inside Bridge
For δ_bd < α·w_min (forces single connected component):
$$\mathrm{Inside}(u) \geq \mathrm{Artic}_{\min}(m,n) > 0$$
Threshold behavior: binary values + spatial coherence → high Q_morph.

## SEPARATION DOMINANCE IS GOOD NEWS

The R10 finding (E_sep dominates by 10⁵×) makes the bridge STRONGER:
- Sep has the tightest control (linear, exact)
- Near-minimizers are primarily near-minimizers of E_sep
- Formations exist because separation demands distinction

## CONVERGENCE RATES

| Predicate | Rate | Type |
|-----------|------|------|
| Bind (ℓ²) | O(δ) | Exact equality |
| Sep | O(δ) | **Exact equality** |
| Inside | Threshold | Step function |
| Persist | O(δ) expected | OPEN |

## WHAT'S NOT PROVED

- Persist bridge (requires transport/two-time analysis)
- Sharpness of Bind_ℓ∞ bound
- Upper bounds on E(û) in terms of parameters
