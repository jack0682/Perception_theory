# Exp78 Cross-Config Follow-up on 15x15:0.6

**Date:** 2026-04-11
**Session:** Cycle 65 — cross-config search-protocol audit
**Category:** experiment
**Status:** complete
**Depends on:** docs/04-11/experiment/EXP78-SEARCH-PROTOCOL-UPGRADE-20x20_c0.6.md; experiments/results/exp78_search_protocol_upgrade_15x15_0.6.json

---

## 1. CURRENT GAP

Exp78 on `20x20:0.6` suggested that search-protocol sensitivity dominates selected-branch inference. This follow-up asks whether the same effect appears on another sentinel, `15x15:0.6`.

---

## 2. Results

| Lambda | Continued total | Best raw-catalog total | Upgraded-direct best total | direct - continued | direct - catalog | Direct best type |
|---:|---:|---:|---:|---:|---:|---|
| 0.10 | 11.571457 | 13.144003 | 11.061635 | -0.509822 | -2.082368 | Type B candidate |
| 0.50 | 11.072987 | 13.520155 | 10.674284 | -0.398703 | -2.845871 | Type B candidate |
| 1.00 | 10.702254 | 13.960099 | 10.533363 | -0.168891 | -3.426736 | Type B candidate |

---

## 3. Main Findings

1. The same pattern repeats on `15x15:0.6`: upgraded direct optimization beats both the raw catalog and the warm continuation branch at every tested lambda.
2. The improved branch remains `Type B candidate` throughout the tested set.
3. The raw catalog best branch is Type A at all tested lambdas here, so search quality is not merely refining a branch within one family; it changes the inferred selected family.

---

## 4. Interpretation

This strongly suggests that search sensitivity is **not** confined to the hardest sentinel `20x20:0.6`. At least one additional config shows the same qualitative failure mode:

- raw multistart search points toward one selected-family picture,
- seeded/injected optimization finds a different, lower-energy Type B branch.

So the open branch-selection gap is now best understood as a **search-aware theorem/support gap**, not just a branch-existence gap.

---

## 5. Decision

| Claim | Outcome |
|---|---|
| search sensitivity is local to `20x20:0.6` | rejected |
| upgraded direct optimization changes selected-family inference on `15x15:0.6` | numerical support |
| R1-Q closed | no |

---

## 6. Next Trigger

Either widen to `10x10:0.6` for a third config, or start abstracting a search-aware branch-selection statement that explicitly separates discovered branches from optimizer-dependent selected branches.
