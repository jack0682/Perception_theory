# Continuation-Access Cross-Config Follow-up on 15x15:0.6

**Date:** 2026-04-11
**Session:** Cycle 79 — cross-config continuation-access replication
**Category:** experiment
**Status:** complete
**Depends on:** docs/04-11/experiment/EXP79-CONTINUATION-ACCESS-DIAGNOSTIC-20x20_c0.6.md; docs/04-11/experiment/EXP80-LOCAL-BASIN-PROXY-20x20_c0.6.md

---

## 1. Raw-Access Diagnostic

At `15x15:0.6`, `lambda=0.5`:

- continued branch type: `Type B candidate`
- continued total energy: `13.186253`
- raw hit rate at threshold `4.0`: `1 / 16 = 0.0625`

Strict-threshold accessibility summary:

- threshold `2.0`: 0 / 16
- threshold `2.5`: 0 / 16
- threshold `3.0`: 0 / 16
- threshold `4.0`: 1 / 16

Best raw branch is still Type A and does not lie inside the strict family neighborhood.

---

## 2. Local Basin Proxy

At the same config and lambda, local perturbations around the continued branch return with:

- sigma=0.01: 8 / 8 = 1.0000
- sigma=0.02: 8 / 8 = 1.0000
- sigma=0.05: 8 / 8 = 1.0000
- sigma=0.10: 8 / 8 = 1.0000


So the same asymmetric pattern seen on `20x20:0.6` reappears:

```text
hard to enter, easy to keep.
```

---

## 3. Interpretation

This significantly strengthens the continuation-access conjecture.

It is no longer only a hardest-sentinel story. At least two nontrivial configs now show:

1. poor raw access into the continued low-energy family;
2. robust local return once the branch is entered.

---

## 4. Decision

| Claim | Outcome |
|---|---|
| continuation-access pattern is only a `20x20:0.6` artifact | rejected |
| cross-config continuation-access support | numerically strengthened |

---

## 5. Next Trigger

Promote the conjecture into a compact cross-config support proposition.
