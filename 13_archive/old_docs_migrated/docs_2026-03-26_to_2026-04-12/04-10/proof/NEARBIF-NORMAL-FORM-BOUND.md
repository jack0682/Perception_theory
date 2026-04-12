# Near-Bifurcation Normal-Form Displacement Bound

**Date:** 2026-04-10
**Session:** Cycle 14 — R2 normal-form bound
**Category:** proof
**Status:** complete
**Depends on:** docs/04-10/audit/R2-NEAR-BIFURCATION-PERSISTENCE.md

---

## 1. Model

Consider the one-dimensional soft-mode normal form

```text
E_f(a) = 1/2 mu a^2 + 1/4 c4 a^4 - f a
```

with

```text
mu >= 0,   c4 > 0.
```

The perturbation/transition forcing is `f`. Equilibrium satisfies

```text
mu a + c4 a^3 = f.
```

---

## 2. Existence and Uniqueness

The map

```text
T(a)=mu a + c4 a^3
```

is strictly increasing for all `a` when `mu >= 0` and `c4>0`, since

```text
T'(a)=mu + 3 c4 a^2 >= 0
```

and is strictly increasing except for the harmless single point `a=0` when `mu=0`. Therefore for every `f` there is a unique equilibrium `a(f,mu)`.

---

## 3. Displacement Bounds

From

```text
|f| = mu |a| + c4 |a|^3,
```

both terms are nonnegative. Therefore:

### Linear-regime bound (`mu>0`)

```text
|a| <= |f| / mu.
```

### Critical quartic bound

```text
|a| <= (|f| / c4)^(1/3).
```

Thus

```text
|a| <= min( |f|/mu, (|f|/c4)^(1/3) )       for mu>0,
|a| =  (|f|/c4)^(1/3)                      for mu=0.
```

---

## 4. Crossover Scale

The linear and quartic bounds match when

```text
|f|/mu = (|f|/c4)^(1/3).
```

Equivalently:

```text
|f| ~ mu^(3/2) / sqrt(c4).
```

Therefore:

| Forcing regime | Displacement scaling |
|---|---|
| `|f| << mu^(3/2)` | `|a| ~ |f|/mu` |
| `|f| >> mu^(3/2)` | `|a| ~ (|f|/c4)^(1/3)` |
| `mu = 0` | `|a| = (|f|/c4)^(1/3)` |

---

## 5. Persistence Margin Condition

Let `gamma_int` be the available interior threshold margin after projecting the soft-mode displacement into field coordinates. If the soft eigenmode has `||psi||_infty = M_inf`, exact-threshold preservation requires

```text
M_inf |a| < gamma_int.
```

Sufficient conditions are therefore:

### Away from bifurcation

```text
|f| < mu gamma_int / M_inf.
```

### At the critical quartic scale

```text
|f| < c4 (gamma_int / M_inf)^3.
```

The first condition shrinks linearly in `mu`; the second is independent of `mu` only because quartic stabilization is retained at the exact critical point.

---

## 6. Interpretation for R2

The usual IFT estimate `|a| <= |f|/mu` is conservative near `mu=0` because quartic stabilization gives the weaker but finite critical scaling `|a| ~ |f|^(1/3)`.

However, this does **not** restore uniform full persistence. Exact threshold still requires the cubic-root displacement to remain below the interior margin. If `gamma_int` also shrinks near bifurcation, the persistence window still collapses.

Thus near-bifurcation persistence should be stated as:

> shifted/deep-core remnant persistence survives in a shrinking forcing window controlled by `min(mu gamma_int, c4 gamma_int^3)` after eigenmode normalization.

---

## 7. Next Trigger

Continue R2 by adding the cubic/asymmetric normal form

```text
E(a)=1/2 mu a^2 + c3 a^3 + c4 a^4 - f a
```

and determine how branch asymmetry changes the persistence window and branch-selection direction.
