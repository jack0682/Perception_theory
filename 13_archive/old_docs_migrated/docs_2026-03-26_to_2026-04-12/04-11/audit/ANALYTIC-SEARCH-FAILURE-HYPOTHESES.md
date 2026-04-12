# Analytic Search-Failure Hypotheses for R1-Q

**Date:** 2026-04-11
**Session:** Cycle 72 — analytic obstruction note for raw-search failure
**Category:** audit
**Status:** complete
**Depends on:** docs/04-11/proof/SEL-UPGRADE-BRANCH-SELECTION-SUPPORT-STATEMENT.md; docs/04-11/proof/SEARCH-PROTOCOL-DEPENDENCE-SUPPORT-PROPOSITION.md

---

## 1. Problem

The protocol-fixed support lane is now stable: under `Sel_upgrade`, tested sentinel configurations prefer lower-energy Type B branches. The remaining question is explanatory:

> why does raw multistart search `Sel_raw` systematically miss these branches?

This note records the strongest current analytic hypotheses.

---

## 2. Hypothesis A — Basin-Volume Asymmetry

The Type B branches may occupy narrower but deeper attraction basins, while broader Type A basins capture most random initializations.

If true, then:

- raw multistart search is biased toward Type A discovery even when Type B has lower final energy;
- seeded continuation can reach Type B because it starts inside the narrow basin;
- injected optimization improves results because it bypasses the basin-entry problem.

This is currently the leading geometric explanation.

---

## 3. Hypothesis B — Active-Set Trapping

The optimizer may cross into an active-set regime early and become trapped on a face/stratum that favors Type A-like geometry.

If true, then:

- random starts hit the wrong active-set pattern before the deeper Type B valley is accessed;
- seeded branches preserve a better active-set path;
- the search gap is partly a stratified KKT accessibility issue, not just a smooth nonconvex landscape issue.

This is especially plausible because branch continuation results already depend on fixed or piecewise-fixed active strata.

---

## 4. Hypothesis C — Continuation-Accessible Valleys

Some lower-energy valleys may be easy to follow once a nearby branch point is known, but hard to discover from independent random starts.

If true, then:

- `Pers_seed` and `Sel_upgrade` can consistently access a valley that `Sel_raw` rarely enters;
- the relevant difference is not final local optimality but **path access** through parameter space;
- branch continuation is not just a convenience, but part of the branch-selection mechanism itself.

This hypothesis fits the current Exp75–Exp78 evidence particularly well.

---

## 5. Non-Hypotheses (What We Should Not Yet Claim)

The current data do **not** justify any of the following stronger claims:

- a theorem that raw multistart always misses Type B;
- a theorem that Type B is always globally optimal in the tested configs;
- a theorem that basin-volume asymmetry is the unique mechanism.

So these remain explanatory hypotheses, not proved mechanisms.

---

## 6. Working Priority Order

1. **Continuation-accessible valleys** — best match to current evidence.
2. **Basin-volume asymmetry** — strong geometric candidate.
3. **Active-set trapping** — plausible stratified mechanism needing more explicit diagnostics.

This ordering is provisional and should be re-evaluated if new diagnostics are added.

---

## 7. Consequence for the Campaign

The theorem-closing campaign should now treat raw-search failure as a structured research blocker, not as mere experimental noise.

The next honest deliverable is therefore not another branch-free threshold claim, but either:

- an experiment/theory bridge that distinguishes basin access from final energy ordering, or
- a protocol-dependent theorem-support statement plus an explicit analytic conjecture on search failure.

---

## 8. Next Trigger

Either add diagnostics aimed at basin access / active-set transitions, or promote the current hypotheses into a compact “analytic conjecture register” for R1-Q3.
