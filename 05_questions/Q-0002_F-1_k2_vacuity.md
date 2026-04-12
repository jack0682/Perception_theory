---
id: Q-0002
type: question
category: open_problem
status: under_resolution
priority: critical
date_raised: 2026-04-06
date_status_update: 2026-04-13
related_to: [OP-0001, T-Kinetic-1, T-Kinetic-2, T-Kinetic-3, A-0023, A-0024, A-0025]
---

# Question: Q-0002 — F-1 K=2 Vacuity

## Statement

Why does K>1 (multiple formations) appear possible in theory but never stable in experiments on single fields? Is K=2 genuinely stable, or is it merely an artifact of incomplete relaxation?

---

## Original Problem (v1.2)

**Observation (exp51–exp65):** Across 10 single-field configurations (grids, random, barbell, SBM), when relaxed to energy-minimizing equilibrium, the system **always** converges to K=1 (single global formation). K>1 never achieves stable equilibrium.

**Issue:** 
- Theory predicts K>1 is possible (no axiom forbids it)
- Energy formulation (E = λ_cl E_cl + λ_sep E_sep + λ_bd E_bd) has no explicit K=2 minimum
- K=1 is always energetically lower
- → K=2 appears **vacuous**: predicted but never realized

**Consequence:** Multi-formation theory (K-field architecture) was motivated but lacks grounding on single field.

---

## Resolution Path: Option C (Kinetic Framework)

**Hypothesis:** K=2 exists as **metastable local minimum**, separated from K=1 by an energy barrier.

**Mechanism:**
1. Energy landscape has TWO minima: K=1 (global) and K=2 (local)
2. Barrier height B > 0 prevents K=2 → K=1 transition at finite time
3. Residence time τ in K=2 well: τ ≈ τ₀ exp(B / k_B T) (Kramers law)
4. K=2 coexists dynamically, not thermodynamically

**Why this resolves F-1:**
- K=2 IS stable (metastably); it's not vacuous
- K=1 is **globally** lower, K=2 is **locally** stable — both true
- Multi-formation dynamics explained by barrier heights, not energy minimization

---

## Validation Experiments (2026-04-13 to 2026-05-24)

**Critical path:**

| Experiment | Validates | Status | Timeline |
|-----------|-----------|--------|----------|
| E-0081 | Barrier exists | Designed | Apr 13–19 |
| E-0082 | Kramers law τ ≈ τ₀ exp(B/T) | Designed | Apr 20–May 3 **CRITICAL** |
| E-0083 | Temperature scaling | Designed | May 4–10 |
| E-0084 | K=2 emergence under noise | Designed | May 4–10 |

**Decision point (May 3):** If exp82 shows τ_empirical ≈ τ_theory (within 2×), F-1 is resolved by kinetic framework. If exp82 fails, framework collapses.

---

## Historical Context

**Why not found earlier?**
- Single-field focus assumed energy was sufficient
- Kinetic barrier effects overlooked
- Stochastic dynamics not central to v1.2

**Why kinetic now?**
- exp62–exp65 failures forced reconsideration
- Barrier landscape structure observed in multi-formation studies (exp38, exp55)
- Kramers theory naturally applies to stochastic systems

---

## Status

🔴 **CRITICAL, Under Active Resolution**

- **Dependencies:** A-0023, A-0024, A-0025 formalized; proofs of T-Kinetic-1/2/3 in progress
- **Blockers:** exp82 validation (must show Kramers law holds)
- **Expected resolution:** 2026-05-24 (v2.0 publication) or May 3 (hard decision if exp82 fails)

---

**Raised:** 2026-04-06 (Critic deep audit)  
**Status Update:** 2026-04-13 (Option C chosen)  
**Expected Resolution:** 2026-05-24 (v2.0 publication)  
**Hard Decision Point:** 2026-05-03 (exp82 results)
