# R1-Q Lane Decision After Protocol-Dependence Formalization

**Date:** 2026-04-11
**Session:** Cycle 70 — lane selection after support proposition
**Category:** audit
**Status:** complete
**Depends on:** docs/04-11/proof/SEARCH-PROTOCOL-DEPENDENCE-SUPPORT-PROPOSITION.md; docs/04-11/audit/R1-Q-STATUS-NOTE-PROTOCOL-TAGGED.md

---

## 1. Decision Surface

After formalizing the search-protocol dependence proposition, the campaign has two serious next lanes:

### Lane A — Analytic Search-Failure Explanation

Goal:

> explain why raw multistart search systematically misses lower-energy Type B branches.

Possible tools:
- basin-volume asymmetry,
- Hessian anisotropy,
- continuation-accessible valleys vs random-init inaccessible valleys,
- active-set trapping,
- barrier geometry / simplex-penalty distortion.

### Lane B — Protocol-Fixed Branch-Selection Support Theory

Goal:

> treat `Sel_upgrade` as the operative selection rule and build the strongest honest theorem/support statement under that fixed protocol.

Possible tools:
- protocol-tagged branch selection statements,
- fixed-seed continuation theorems,
- support proposition tying positive repulsion to the upgraded selection rule,
- branch-family persistence + upgraded-selection composite statement.

---

## 2. Evaluation

### Lane A strengths

- goes after the deepest unresolved mechanism;
- could eventually explain when raw search is trustworthy or not;
- directly addresses the newly exposed R1-Q3 reliability gap.

### Lane A weaknesses

- analytically harder;
- likely to consume many cycles before yielding a clean theorem-level result;
- may require new geometric quantities not yet formalized.

### Lane B strengths

- closer to an immediately stabilizable theorem-support artifact;
- uses the protocol-tagged framework already built;
- can convert the numerical campaign into a disciplined conditional statement sooner.

### Lane B weaknesses

- leaves the raw-search failure mechanism unexplained;
- risks overfitting theory to a chosen protocol if not clearly labeled.

---

## 3. Recommended Lane

**Recommended next lane: Lane B first, Lane A second.**

Reason:

1. the campaign already has enough material to formulate a strong protocol-fixed support statement;
2. that will stop future wording drift immediately;
3. once the protocol-fixed lane is stabilized, analytic search-failure work can proceed as a deeper explanatory follow-up without blocking theorem-status hygiene.

So the next concrete objective should be:

> formulate the strongest honest branch-selection support statement under `Sel_upgrade`, explicitly marked as protocol-fixed and not search-neutral.

---

## 4. Decision

| Option | Decision |
|---|---|
| Lane A — analytic search-failure explanation | deferred but retained as next deep-research lane |
| Lane B — protocol-fixed branch-selection support | chosen as immediate next execution lane |

---

## 5. Next Trigger

Write a protocol-fixed R1-Q support artifact centered on `Sel_upgrade`, stating exactly what branch-family selection behavior is numerically supported under that rule and what remains open without protocol fixing.
