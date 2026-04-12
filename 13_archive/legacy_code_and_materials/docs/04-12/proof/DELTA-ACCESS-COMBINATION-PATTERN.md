# Delta_access Combination Pattern

**Date:** 2026-04-12
**Session:** Cycle 115 — combining one-sided accessibility bounds into a direct protocol-gap lower bound
**Category:** proof
**Status:** active
**Depends on:** docs/04-12/proof/ARAW-UPPER-BOUND-TEMPLATE.md; docs/04-12/proof/ASEED-LOWER-BOUND-TEMPLATE.md; docs/04-12/proof/DIRECT-PROTOCOL-GAP-BOUND-TEMPLATE.md

---

## 1. Purpose

This note shows the weakest useful combination pattern from the one-sided bounds

```text
A_raw(G, lambda; U_B) <= eps_raw(G, lambda; U_B)
A_seed(G, lambda; U_B) >= eta_seed(G, lambda; U_B)
```

to a theorem-facing lower bound on the direct protocol-gap quantity.

---

## 2. Combination Rule

If both one-sided statements hold, then the direct protocol-gap quantity satisfies the schematic lower bound

```text
A_seed(G, lambda; U_B) - A_raw(G, lambda; U_B)
>= eta_seed(G, lambda; U_B) - eps_raw(G, lambda; U_B).
```

So the natural candidate is

```text
Delta_access(G, lambda; U_B) := eta_seed(G, lambda; U_B) - eps_raw(G, lambda; U_B).
```

This is the weakest useful direct-lower-bound pattern currently available.

---

## 3. Why This Pattern Is Right

This combination does not add any extra theorem ambition beyond what the one-sided routes already promise.
It simply preserves the intended asymmetry:

- the seeded protocol contributes a positive accessibility floor,
- the raw protocol contributes a small accessibility ceiling,
- and their difference yields the comparison quantity.

So the direct gap is not a separate mysterious object; it is the difference between the positive side and the obstruction side.

---

## 4. When the Gap Is Actually Positive

The comparison becomes genuinely informative once

```text
eta_seed(G, lambda; U_B) > eps_raw(G, lambda; U_B).
```

That is the real theorem-facing positivity condition.

So the next layer of analysis is no longer “how do we combine the two sides?” but:

> **under what structural conditions is the seeded-access floor strictly larger than the raw-access ceiling?**

---

## 5. Relation to Existing Evidence

The current experiments already support this qualitative pattern:

- Exp79 suggests `eps_raw` is small under strict target-neighborhood thresholds;
- Exp80 suggests `eta_seed` is positive and plausibly large on the local side.

So the positivity condition

```text
eta_seed > eps_raw
```

is already the natural way to express the current continuation-access asymmetry.

---

## 6. Safe Current Reading

The strongest current theorem-support reading is:

> if raw accessibility is bounded above by a small quantity and seeded accessibility is bounded below by a larger one, then the direct protocol gap inherits a positive lower bound by subtraction.

This is still a theorem-facing scaffold, not a completed theorem.

---

## 7. What Remains Open

- how to control `eps_raw` and `eta_seed` by comparable structural quantities;
- whether positivity should be shown by shrinking `eps_raw`, enlarging `eta_seed`, or both;
- how robust the inequality is across configs and lambdas.

---

## 8. Next Trigger

The next step should ask which positivity route is more proof-feasible:

1. make `eps_raw` small enough first, or
2. make `eta_seed` robustly positive enough first.
