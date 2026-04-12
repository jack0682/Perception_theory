# Near-Bifurcation Cubic Normal-Form Obstruction

**Date:** 2026-04-10
**Session:** Cycle 15 — R2 cubic/asymmetric normal form
**Category:** proof
**Status:** complete
**Depends on:** NEARBIF-NORMAL-FORM-BOUND.md

---

## 1. Model

Consider

```text
E_f(a)=1/2 mu a^2 + c3 a^3 + c4 a^4 - f a,
```

with `c4>0`. The equilibrium equation is

```text
mu a + 3 c3 a^2 + 4 c4 a^3 = f.
```

---

## 2. Cubic Term Breaks Symmetric Critical Persistence

If `mu=0`, `f=0`, and `c3 != 0`, then near `a=0`,

```text
E(a)=c3 a^3 + c4 a^4.
```

For sufficiently small `a` of opposite signs, the cubic term changes sign. Therefore `a=0` is not a two-sided local minimum in the unconstrained center direction.

Thus a nonzero cubic coefficient encodes an asymmetric / imperfect bifurcation. Uniform persistence through the bifurcation cannot be stated as symmetric pitchfork persistence.

---

## 3. Branch Selection Direction

For small `mu>0`, `f=0`, nonzero equilibria satisfy

```text
a (mu + 3 c3 a + 4 c4 a^2)=0.
```

The nonzero roots are

```text
a = [-3 c3 ± sqrt(9 c3^2 - 16 c4 mu)] / (8 c4),
```

when the discriminant is nonnegative.

Thus branch existence and side are controlled by `sign(c3)` and the discriminant. This is qualitatively different from the symmetric quartic model.

---

## 4. Forced Displacement Bound Near a Stable Branch

If one works not at `a=0` but at a stable branch point `a_*` with local curvature

```text
kappa_* = E''(a_*) = mu + 6 c3 a_* + 12 c4 a_*^2 > 0,
```

then the same local IFT logic gives

```text
|delta a| <= |f| / kappa_*
```

for sufficiently small forcing, with higher-order corrections controlled by local third/fourth derivatives.

As `kappa_* -> 0`, the persistence window again collapses.

---

## 5. Consequence for R2

Near bifurcation, the correct theorem cannot be universal and symmetric. It must specify one of:

1. symmetric quartic case (`c3=0`, `c4>0`), where critical displacement scales as `f^(1/3)`;
2. asymmetric cubic case (`c3 != 0`), where branch side and existence are controlled by normal-form coefficients;
3. stable branch case, where persistence window scales with local curvature `kappa_*`.

---

## 6. R2 Decision Update

R2 is not “remove near-bifurcation gap.” It is:

> classify persistence by normal-form type and derive shrinking forcing windows for each branch.

The cubic term is an obstruction to a universal pitchfork-style persistence theorem.

---

## 7. Next Trigger

Proceed to R3 — multi-formation kinetic dynamics.

First move:

> Use the branch-conditioned results to define the minimal Markov/transition-rate state variables for kinetic coarsening: branch id, barrier height, overlap/separation, noise scale, and birth/death event type.
