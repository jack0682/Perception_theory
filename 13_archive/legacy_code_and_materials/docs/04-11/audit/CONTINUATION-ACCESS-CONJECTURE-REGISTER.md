# Continuation-Access Conjecture Register

**Date:** 2026-04-11
**Session:** Cycle 77 — conjecture register for R1-Q3
**Category:** audit
**Status:** complete
**Depends on:** docs/04-11/audit/R1-Q3-ANALYTIC-LANE-COMPARISON.md; docs/04-11/experiment/EXP79-CONTINUATION-ACCESS-DIAGNOSTIC-20x20_c0.6.md; docs/04-11/experiment/EXP80-LOCAL-BASIN-PROXY-20x20_c0.6.md

---

## 1. Core Conjecture

**Continuation-Access Conjecture.**

For some SCC K=2 configurations and positive repulsion values, there exist lower-energy branch families whose local basins are robust once entered, but which are rarely reached by independent raw multistart search. These families are instead accessed reliably by seeded/warm continuation or by search rules that inject continuation-derived seeds.

This is currently a **conjecture backed by numerical evidence**, not a theorem.

---

## 2. Evidence Currently Supporting It

### Support E1 — Raw-access failure

Exp79 (`20x20:0.6`, `lambda=0.5`) shows zero raw hits into the continued Type B family for all strict family-distance thresholds up to `4.0`.

### Support E2 — Local robustness after entry

Exp80 on the same config shows 100% return to the continued Type B family for perturbation scales `sigma = 0.01, 0.02, 0.05, 0.10`.

### Support E3 — Search-upgraded selection advantage

Exp77/Exp78 show that once continuation-derived seeds are injected back into direct optimization, lower-energy Type B branches are found systematically across multiple sentinels.

Together, E1 + E2 + E3 strongly support the picture:

```text
hard to enter, easy to keep.
```

---

## 3. What Would Strengthen the Conjecture

1. **Basin-size proxy scaling:** estimate return probability as a function of perturbation radius and compare against raw-start discovery probability.
2. **Cross-config replication:** repeat Exp79/Exp80-style diagnostics on `15x15:0.6` and/or `10x10:0.6`.
3. **Access-path diagnostics:** show that seeded paths enter the target basin through routes that raw starts do not reach.
4. **Transition structure correlation:** connect coarse region / active-set transitions to success or failure of entry.

---

## 4. What Would Weaken the Conjecture

1. if broad raw-start sweeps begin discovering the same family at non-negligible rates once budgets are only mildly increased;
2. if local perturbation return rates collapse for modest perturbations, contradicting the robust-basin picture;
3. if active-set transition logging reveals a much cleaner trapping mechanism that explains the gap without requiring a basin-access asymmetry story.

---

## 5. Relationship to Other Hypotheses

- **Basin-volume asymmetry** can be read as a geometric mechanism underlying this conjecture.
- **Active-set trapping** can be read as one possible dynamical route by which raw trajectories fail to access the continuation-favored basin.

So the continuation-access conjecture currently sits one level above those more specific mechanism claims.

---

## 6. Working Status

| Item | Status |
|---|---|
| continuation-access conjecture | active leading hypothesis |
| basin-volume asymmetry | plausible mechanism candidate |
| active-set trapping | secondary mechanism candidate |
| theorem-level proof | open |

---

## 7. Next Trigger

Use this register to design the next follow-up experiment: either a basin-size proxy scaling study or a cross-config continuation-access replication.
