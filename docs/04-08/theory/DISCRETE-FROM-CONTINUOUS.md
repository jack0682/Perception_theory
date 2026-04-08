# Discrete Objecthood from Continuous Cohesion: The d_crit = d_min Principle

**Date:** 2026-04-08
**Category:** theory
**Status:** active — central theoretical development
**Depends on:** DMIN-AS-RESOLUTION.md, BEYOND-WEYL-CATA-UPGRADE.md, BEYOND-WEYL-SINGULARITY.md

---

## 0. The Central Claim of SCC

> "The soft cohesion field u_t : X_t → [0,1] is the primitive entity.
>  Crisp objects are always derivative — never invert this."
>  — Agent Instructions §1

This document shows how this claim is realized mathematically: the number of discrete formations (proto-objects) emerges as a sharp, integer-valued quantity from the continuous field u, through the KKT complementarity structure of the constrained energy landscape.

---

## 1. The Principle

**d_crit = d_min Principle.** On a single soft cohesion field with volume constraint, the following three thresholds coincide:

1. **d_crit** (coupling threshold): the distance at which the overlap of two formations first intersects a free variable of the constrained Hessian (KKT complementarity transition)

2. **d_min** (stability threshold): the distance below which no two-bump local minimizer exists (saddle-node bifurcation)

3. **d_res** (resolution threshold): the distance below which the closure operator cannot distinguish two separate entities

Their coincidence means: **the moment two formations begin to "see" each other (through any channel), they merge.** There is no intermediate regime of "aware but separate."

---

## 2. Mechanism: KKT Complementarity as Object Individuation

At a formation minimizer û on Σ_m = {u : Σu = m, u ∈ [0,1]^n}:

**Box-constrained sites** (û_x = 0): the constraint u_x ≥ 0 is active. These sites are "frozen" — they don't participate in the Hessian eigenvalue problem. They form an **information barrier** between formations.

**Free sites** (0 < û_x < 1): these participate in the Hessian. They are the "degrees of freedom" of each formation.

**The transition at d_crit:** a site x* in the inter-formation gap transitions from box-constrained (û(x*) = 0) to free (û(x*) > 0). This:
- Creates a new degree of freedom connecting the two formation Hessians
- Introduces coupling between the two formation's soft modes
- Destroys the block-diagonal structure of the joint Hessian

**The coupling is not perturbative.** The 3×3 model analysis shows that even at u(x*) → 0⁺, the Laplacian coupling 4α between x* and its neighbors is O(1) — comparable to the per-formation spectral gap μ₁. This means the coupling is in the strong-mixing regime from the start.

---

## 3. Why This Makes the Theory Stronger

### 3.1 Binary Prediction

The theory predicts: K formations exist as local minimizers if and only if they are mutually well-separated (d > d_crit for all pairs). The number K is:
- An INTEGER (not continuous)
- SHARPLY determined (not gradually)
- BINARY at each pair level (coupled or decoupled)

This matches the phenomenology of object perception: you see 1 or 2 objects, not 1.5.

### 3.2 No Ambiguous Intermediate

Unlike theories with "soft clustering" (where membership is gradual), SCC predicts a SHARP boundary between "one object" and "two objects." The transition is controlled by the KKT complementarity condition, which is inherently binary (active or inactive).

### 3.3 Resolution as Ontological Boundary

The resolution limit d_min is not an engineering limitation — it is the boundary at which discrete objecthood BEGINS. Below d_min, there is only one entity. Above d_min, there are two. The cohesion field "decides" the number of objects through its energy landscape.

### 3.4 Self-Referential Resolution

The closure operator determines d_min through its parameters (a_cl, τ). Higher closure gain → smaller d_min → finer resolution → more objects distinguishable. The cohesion field's ability to individuate objects is a property of its self-referential structure.

---

## 4. Mathematical Framework

### 4.1 Object Count Function

Define the **formation count** at parameters θ = (α, β, a_cl, τ, m):

$$K^*(\theta) = \max\{K : \exists \text{ K-bump local minimizer on } \Sigma_m\}$$

This is an integer-valued function of continuous parameters. By the d_crit = d_min principle, K* changes only at codimension-1 surfaces in parameter space (where d between some pair of formations crosses d_crit).

### 4.2 Stratification of the Energy Landscape

The constrained energy landscape has a natural stratification by formation count:

$$\mathcal{L}_K = \{\theta : K^*(\theta) = K\}$$

Each stratum is an open set (by structural stability of non-degenerate local minima). The boundaries between strata are the singularity set S where KKT complementarity transitions occur.

### 4.3 The "Phase Diagram" of Objecthood

In the (β, d) plane for fixed other parameters:

```
β
|  K=2 (two objects)     K=1 (one object)
|  ┌──────────────────┐
|  │                  │
|  │   STABLE         │   MERGED
|  │   TWO-BUMP       │   SINGLE BUMP
|  │                  │
|  └──────────────────┘
|  ←────── d_crit(β) ──────→
0 ────────────────────────────── d
```

The boundary curve d_crit(β) is a phase boundary. Crossing it changes the object count. This is a genuine phase transition in the statistical mechanics sense.

---

## 5. Predictions

### P6 (Closure-Resolution Correlation)
Individuals with stronger self-referential cohesion (higher a_cl) exhibit finer spatial resolution in perceptual grouping.

### P7 (Binary Perception)
Perceptual grouping near the resolution threshold is BISTABLE (1 or 2, no intermediate), with the transition being a sharp flip, not a gradual change.

### P8 (Object Count as Phase Transition)
The number of perceived objects changes discontinuously with spatial parameters (distance, size, contrast), analogous to a first-order phase transition.

### P9 (KKT Complementarity in Neural Implementation)
The neural mechanism implementing object individuation involves a threshold-like gating (analogous to KKT active/inactive), not a continuous blending.

---

## 6. Connection to the Theory's Architecture

| SCC Concept | Mathematical Realization |
|-------------|------------------------|
| "Soft cohesion is primitive" | u ∈ [0,1]^n, continuous field |
| "Crisp objects are derivative" | K* ∈ ℤ, derived from landscape topology |
| "Closure creates self-coherent entities" | Each bump is near a closure fixed point |
| "Distinction separates entities" | D(u) → d_min → inter-object boundary |
| "Resolution limit" | d_crit = d_min, KKT complementarity |
| "Object count" | K* = max K with K-bump local min |
| "Pre-objective → objective" | Continuous u → integer K* via sharp transition |

---

## 7. What Remains to Prove

1. **d_crit = d_min (exactly):** The 3×3 model suggests this but a full proof on the graph Hessian is needed. Key: show that coupling strength at u(x*) → 0⁺ exceeds the spectral gap μ₁ in the merge direction.

2. **K* is well-defined:** Show that the maximum K with a K-bump local minimizer is finite and integer-valued for generic parameters.

3. **Phase diagram structure:** Characterize d_crit(β, a_cl) as a function — monotone in β and a_cl (partly proved: ∂d_min/∂β < 0, ∂d_min/∂a_cl < 0).

4. **Predictions P7-P9:** Connect to psychophysical experiments.
