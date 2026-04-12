# Exp80 Local Basin Proxy on 20x20:0.6

**Date:** 2026-04-11
**Session:** Cycle 74 — local basin proxy for the continued Type B branch
**Category:** experiment
**Status:** complete
**Depends on:** docs/04-11/experiment/EXP79-CONTINUATION-ACCESS-DIAGNOSTIC-20x20_c0.6.md; experiments/exp80_local_basin_proxy.py

---

## 1. Goal

Complement Exp79 by testing whether the continued Type B branch has a robust local basin once the optimizer is started near it.

This distinguishes two possibilities:

1. the branch is globally hard to access but locally stable;
2. the branch is not even locally robust.

---

## 2. Protocol

- config: `20x20:0.6`
- target lambda: `0.5`
- recover and continue the Type B branch
- perturb that continued branch with Gaussian noise
- re-optimize from the perturbed state
- count returns to the same family under distance threshold `4.0`

---

## 3. Results

| Sigma | Hits | Rate |
|---:|---:|---:|
| 0.01 | 8 / 8 | 1.0000 |
| 0.02 | 8 / 8 | 1.0000 |
| 0.05 | 8 / 8 | 1.0000 |
| 0.10 | 8 / 8 | 1.0000 |

---

## 4. Main Finding

The continued Type B branch shows **100% return rate** for all tested perturbation scales:

- `sigma = 0.01`
- `sigma = 0.02`
- `sigma = 0.05`
- `sigma = 0.10`

So the current picture is highly asymmetric:

- **raw starts**: fail to enter the branch family at practical rates (Exp79),
- **nearby perturbed starts**: return to the family with probability 1 in this test (Exp80).

---

## 5. Interpretation

This strongly favors a continuation-access / basin-access explanation over a “the branch is too fragile to matter” explanation.

The emerging geometry is:

- the Type B branch has a robust local basin,
- but that basin is not reached by independent raw starts,
- so the search gap is about **entry into the basin**, not local instability after entry.

---

## 6. Decision

| Claim | Outcome |
|---|---|
| continued Type B branch is locally unstable at `lambda=0.5` | rejected |
| local basin proxy supports continuation-accessible valleys | strongly supported |
| next analytic follow-up should stay on access mechanics, not local stability | yes |

---

## 7. Next Trigger

Move to the next explanatory layer:

> instrument active-set transition logging or another path-access diagnostic to understand why random starts fail to enter the robust local Type B basin.
