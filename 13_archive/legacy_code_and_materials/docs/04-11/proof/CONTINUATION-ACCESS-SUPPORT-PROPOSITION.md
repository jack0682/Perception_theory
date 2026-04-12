# Continuation-Access Support Proposition

**Date:** 2026-04-11
**Session:** Cycle 79 — compact support proposition for continuation access
**Category:** proof
**Status:** complete
**Depends on:** docs/04-11/audit/CONTINUATION-ACCESS-CONJECTURE-REGISTER.md; docs/04-11/experiment/CONTINUATION-ACCESS-CROSS-CONFIG-15x15_c0.6.md

---

## 1. Proposition (Numerical Support Only)

There exist tested SCC K=2 configurations and positive repulsion values for which:

1. a low-energy Type B branch family is difficult to discover from independent raw starts at the target lambda, yet
2. the same branch family is robust under local perturbations once reached by seeded/warm continuation.

Equivalently, the current experiments support a cross-config pattern of the form:

```text
raw access is rare, local persistence is strong.
```

This is not yet a theorem. It is a numerical-support proposition for the continuation-access explanation of R1-Q3.

---

## 2. Supported Instances

- `20x20:0.6`, `lambda=0.5`
- `15x15:0.6`, `lambda=0.5`

In both cases:

- strict-threshold raw access is absent or extremely rare,
- local perturbation return is 100% on the tested sigma set.

---

## 3. Consequence

The continuation-access story should now be treated as more than a one-off anecdote. It is a cross-config support proposition that can organize the next analytic diagnostics.

---

## 4. Next Trigger

Decide whether to replicate once more on `10x10:0.6` or to shift toward an analytic mechanism note explaining why this access asymmetry occurs.
