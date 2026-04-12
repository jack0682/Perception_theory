# Relaxed Merge Barrier: Conditional Definition and No-Universal-Lower-Bound Result

**Date:** 2026-04-10
**Session:** Cycle 21 — relaxed merge barrier lower-bound attack
**Category:** proof
**Status:** complete
**Depends on:** docs/04-10/audit/R4-RELAXED-MERGE-MANIFOLD.md; docs/04-10/audit/NEXT-TRIGGER.md; docs/04-06/MERGE-CRITIQUE.md

---

## 1. CURRENT GAP

**Target:** R4 relaxed-manifold merge barrier lower bound.

The relaxed manifold was defined as

```text
R_M^2 = { (u1,u2): 0 <= u_k <= 1,
          sum_x (u1+u2)=M,
          u1+u2 <= 1 }.
```

The merge endpoint is valid here:

```text
Embed(u_merged) = (u_merged, 0),     sum_x u_merged = M.
```

The question is whether one can prove a positive merge barrier from a K=2 source branch `B` to a K=1 embedded target.

---

## 2. Barrier Functional

For a source branch state `B in R_M^2`, target `T=Embed(u_merged)`, energy `E_R`, and path class `P(B,T)`, define

```text
DeltaE_R(B,T,P) = inf_{gamma in P(B,T)} [ max_{t in [0,1]} E_R(gamma(t)) - E_R(B) ].
```

This is meaningful only after specifying:

- source branch `B`,
- relaxed energy `E_R`,
- endpoint `T`,
- path class `P`.

---

## 3. Direct Method: What Can Be Proved

### Proposition 1 — Existence for finite-dimensional discretized path classes

Fix an integer `N >= 2`. Let `P_N(B,T)` be the class of piecewise-linear paths in `R_M^2` determined by `N+1` nodes

```text
z_0 = B, z_N = T, z_i in R_M^2.
```

Define the discrete barrier

```text
DeltaE_N(B,T) = min_{z_1,...,z_{N-1} in R_M^2}
                [ max_i E_R(z_i) - E_R(B) ].
```

Because `R_M^2` is a closed bounded polytope in finite dimension, it is compact. The product `(R_M^2)^{N-1}` is compact. If `E_R` is continuous, the map

```text
(z_1,...,z_{N-1}) -> max_i E_R(z_i)
```

is continuous. Therefore the minimum exists.

**Status:** PROVED for finite-image / discretized path classes.

### Limitation

This proves existence of a discrete minimax path, not a positive lower bound. It also does not prove existence of an optimal path in the unrestricted space of all continuous paths without additional compactness/equicontinuity assumptions.

---

## 4. No Universal Positive Lower Bound

### Proposition 2 — Positive lower bound requires source stability in the relaxed manifold

If the source `B` is not a strict local minimizer of `E_R` on `R_M^2`, then there need not be any positive barrier. In particular, if there exists a continuous path `gamma` from `B` to `T` such that

```text
E_R(gamma(t)) <= E_R(B)       for all t,
```

then

```text
DeltaE_R(B,T,P) <= 0.
```

Since the constant lower bound convention clips barriers at zero, the effective barrier is zero.

**Proof.** Direct from the definition of `DeltaE_R`: the maximum along such a path is at most `E_R(B)`, so the max-minus-source quantity is nonpositive. ∎

### Consequence

A positive relaxed merge barrier cannot be inferred merely from the fact that K=2 is locally stable on the fixed per-formation manifold `Sigma_{m1} x Sigma_{m2}`. The relaxed manifold adds mass-transfer directions. Stability must be rechecked on `R_M^2`.

---

## 5. Explicit Degeneration: Small Second Formation

Even if some branches have positive barriers, no uniform positive lower bound can hold over all source branches.

Let `B_epsilon=(u_M-epsilon, v_epsilon)` be a family of K=2 states in `R_M^2` with

```text
sum v_epsilon = epsilon,
||v_epsilon|| -> 0,
u_M-epsilon -> u_M,
```

where `T=(u_M,0)` is the embedded K=1 target.

If `E_R` is continuous, then

```text
E_R(B_epsilon) -> E_R(T).
```

The straight path from `B_epsilon` to `T` has image shrinking to `T`. By uniform continuity of `E_R` on compact `R_M^2`, its energy oscillation tends to zero. Hence

```text
DeltaE_R(B_epsilon,T,P_linear) -> 0.
```

**Status:** PROVED degeneration. Therefore no branch-uniform positive lower bound exists without lower-bounding the disappearing formation mass and imposing a source-stability condition.

---

## 6. Path-Class Counterexample Mechanism

For finite equal-mass branches, a positive barrier may still fail if the path class permits “dissolve-spread-transfer-reconcentrate” moves:

1. flatten `u2` toward a low-amplitude diffuse field,
2. transfer total mass into `u1` through low-overlap states,
3. reconcentrate into `u_merged`,
4. avoid core-core overlap that a direct interpolation path would force.

This does not prove zero barrier for every SCC branch, but it shows why a direct linear-path lower bound is not a minimax lower bound. A lower-bound theorem must restrict path class or prove that every such avoidance route incurs a boundary/morphology cost.

---

## 7. Corrected Theorem Schema

A valid positive-barrier theorem must have the form:

> Let `B` be a specified K=2 branch that is a strict local minimizer of the relaxed energy `E_R` on `R_M^2`, with relaxed Hessian gap `mu_R > 0`, formation masses bounded below, and admissible paths restricted to a class `P` that cannot dissolve/spread a formation without paying a quantified boundary/morphology cost. Then `DeltaE_R(B,T,P) > 0`, with a lower bound depending on `mu_R`, the basin radius, mass lower bound, and path-class restrictions.

Without these hypotheses, the universal positive relaxed merge barrier is false.

---

## 8. Decision

| Claim | Outcome |
|---|---|
| relaxed merge barrier functional | well-defined once branch/endpoint/path class specified |
| minimax existence for finite-image path classes | PROVED |
| positive lower bound for all relaxed paths/source branches | FALSE / unsupported |
| positive lower bound under relaxed local stability + path restrictions | plausible conditional theorem, not yet proved |
| direct interpolation barrier as true barrier | false unless path class is explicitly linear/direct |

---

## 9. Registry Delta

R4 remains structurally open, but with a sharper classification:

> OPEN-CONDITIONAL. The object is now well-defined; universal positive lower bound is false. A positive theorem requires relaxed local stability, mass lower bound, and path-class restrictions.

---

## 10. Next Trigger

Proceed to the conditional positive-barrier theorem:

> Prove a local basin barrier: if `B` is a strict local minimizer of `E_R` with relaxed Hessian gap `mu_R`, then every path from `B` to outside a radius `rho` must cross energy at least `E_R(B)+c mu_R rho^2` up to higher-order terms.

This will give a local barrier component independent of global merge endpoint details.
