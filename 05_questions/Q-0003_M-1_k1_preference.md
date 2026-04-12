---
id: Q-0003
type: question
category: open_problem
status: under_resolution
priority: critical
date_raised: 2026-04-06
date_status_update: 2026-04-13
related_to: [OP-0002, T-Kinetic-2, A-0024]
---

# Question: Q-0003 — M-1 K=1 Energetic Preference

## Statement

Why is K=1 always energetically preferred (lower E) on every tested graph, even when spatially separated well-formed K=2 configurations exist nearby in configuration space?

---

## Original Problem (v1.2)

**Observation:** Energy function E = λ_cl E_cl + λ_sep E_sep + λ_bd E_bd is **always minimized at K=1** across all parameter regimes:
- E(K=1) < E(K=2) always (exp51–exp65, 10+ configurations)
- No parameter choice makes K=2 energetically lower
- Separation energy λ_sep E_sep always pulls toward K=1

**Issue:**
- Multi-formation is predicted by theory but never energetically favored
- Makes K=2 "always reluctant": requires external constraint to maintain
- Creates dependency on external K-field architecture rather than self-sustaining formation dynamics

**Consequence:** Cannot explain why K=2 persists in biology/cognition without invoking artificial K-field machinery.

---

## Resolution Path: Option C (Kinetic Framework)

**Hypothesis:** K=1 is **globally lower in energy**, K=2 is **locally stable via barriers**. Both facts are true simultaneously.

**Mechanism:**
1. On single field: Energy minimization gives K=1 (this is correct)
2. BUT: K=2 configuration sits in local energy minimum with barrier B separating it from K=1 minimum
3. Escape rate from K=2: Kramers law gives τ ≈ τ₀ exp(B / k_B T)
4. At biological timescales (or low noise), K=2 is **kinetically trapped** despite being energetically unfavored
5. **Kinetic preference** (metastability) can override **energetic preference** (global minimum)

**Why this resolves M-1:**
- ✅ K=1 is globally lower (energy is correct)
- ✅ K=2 persists anyway (kinetic barriers explain why)
- ✅ No external constraint needed (self-organized dynamics)

**Biological motivation:**
- Neural clusters persist despite being thermodynamically unstable (kinetic trapping)
- Perceptual groupings survive even when unbundling would lower energy
- Temporal persistence emerges from barrier heights, not energy preference

---

## Validation Experiments (2026-04-13 to 2026-05-24)

**Key experiment: E-0082 (Kramers law validation)**

Measure escape time τ from K=2 minimum and verify:
```
τ_empirical ≈ τ₀ exp(B / k_B T)
```

Where:
- B = barrier height (from exp81)
- T = effective temperature (noise scale)
- τ₀ = prefactor from system properties (Hessian curvature)

**Success criterion:** τ_empirical / τ_theory ∈ [0.5, 2.0] (factor of 2 agreement in exponential, i.e., log-agreement)

**If exp82 succeeds:** M-1 is resolved; kinetic framework explains persistent K>1

**If exp82 fails:** Alternative escape mechanism (tunneling, non-Kramers dynamics) must be identified

---

## Implications for Multi-Formation

**K-field interpretation:** In K-field architecture (multiple fields coupled), each field can occupy its own K=2 minimum independently. Repulsion between fields prevents energy collapse back to K=1. This is now *understandable* rather than ad-hoc.

**Biological systems:** Explain why neural assemblies, gestalt formations, and perceptual objects persist despite energy barriers — they're kinetically trapped local minima, not global energy minimizers.

---

## Status

🔴 **CRITICAL, Under Active Resolution**

- **Depends on:** A-0024 (metastability definition), Kramers theory applicability
- **Validated by:** E-0082 (Kramers law), E-0083 (temperature scaling)
- **Critical decision:** May 3, 2026 (exp82 results)
- **Expected resolution:** 2026-05-24 (v2.0 publication)

---

**Raised:** 2026-04-06 (Critic deep audit)  
**Status Update:** 2026-04-13 (Option C chosen)  
**Hard Decision Point:** 2026-05-03 (exp82 validation)
