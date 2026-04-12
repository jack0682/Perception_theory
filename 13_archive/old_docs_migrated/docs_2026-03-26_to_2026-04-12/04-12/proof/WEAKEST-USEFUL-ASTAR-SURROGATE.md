# Weakest Useful A_* Surrogate

**Date:** 2026-04-12
**Session:** Cycle 105 — minimal theorem-usable accessibility surrogate for the fixed-protocol lane
**Category:** proof
**Status:** active
**Depends on:** docs/04-12/audit/BRANCHDISTANCE-VS-ASTAR-DECISION.md; docs/04-12/proof/FIXED-PROTOCOL-ACCESSIBILITY-GAP-STATEMENT.md; docs/04-12/proof/CONSOLIDATED-LOCAL-NEIGHBORHOOD-STATEMENT.md

---

## 1. Purpose

This note identifies the weakest useful theorem-usable accessibility surrogate `A_*` for the fixed-protocol basin-access lane.

---

## 2. Desired Properties

The surrogate should be:

1. **protocol-tagged** — different search rules may give different accessibility values;
2. **target-neighborhood based** — accessibility must mean accessibility to `U_B(lambda)`;
3. **compatible with finite computation / finite descent** — because the experiments observe actual optimization trajectories;
4. **comparable across protocols** — so `Gap_{raw,seed}` is meaningful.

---

## 3. Weakest Useful Choice

The weakest currently useful choice is:

```text
A_S(G, lambda; U_B)
:= probability that protocol S enters the target local neighborhood U_B(lambda)
within the fixed optimization horizon used to define the protocol.
```

In words:
- run the protocol from its stated initialization rule,
- observe whether the trajectory enters `U_B(lambda)` within the prescribed run,
- record that event probability as the accessibility surrogate.

This is weaker than a fully asymptotic basin-measure object, but stronger than vague qualitative language.

---

## 4. Why This Choice Is Enough Right Now

### It matches Exp79

Exp79 is already very close to this form:
- raw starts are launched at the target lambda,
- closeness to the continued target branch is checked,
- practical access failure is recorded.

### It matches Exp80 indirectly

Exp80 supports the local side by showing that, once near the target family, return/capture is strong.
So `A_*` can remain focused on **entry**, while Exp80 anchors the separate local return quantity.

### It matches the protocol-gap theorem lane

The fixed-protocol gap only needs a usable comparison object:

```text
Gap_{raw,seed}(G, lambda; U_B) = A_seed - A_raw.
```

The entry-probability surrogate is the smallest natural object that already supports this comparison.

---

## 5. What This Surrogate Does Not Try To Solve

This choice does **not** yet provide:
- a global basin-volume theorem,
- an infinite-time accessibility limit,
- or a search-neutral measure on the whole branch landscape.

It is intentionally modest.

---

## 6. Safe Current Reading

The safest current reading is:

> accessibility means probability of entering the theorem-facing local neighborhood `U_B(lambda)` under a named protocol within its stated optimization horizon.

This is enough for the fixed-protocol theorem lane because it lets us compare raw and seeded access without pretending to solve the full search-neutral problem.

---

## 7. What Remains Open

- whether the horizon should be fixed by iteration count, convergence rule, or another stopping condition;
- how to pass from empirical entry rates to theorem-level upper/lower bounds;
- how to separate true entry from transient near-misses.

---

## 8. Next Trigger

The next refinement should decide whether to formalize first:

1. the event “enter `U_B(lambda)`”, or
2. the protocol horizon / stopping rule that defines the accessibility probability.
