# Rung-4 Basin-Access Theorem Outline

**Date:** 2026-04-11
**Session:** Cycle 91 — explicit hypothesis outline for the search-neutral basin-access theorem target
**Category:** proof
**Status:** active
**Depends on:** docs/04-11/audit/NEXT-RUNG-CHOICE.md; docs/04-11/audit/PROOF-ORDER-VERIFICATION-AUDIT.md; docs/04-11/theory/BASIN-ACCESS-CONJECTURE-SUPPORT-LADDER.md; docs/04-11/theory/SEARCH-AWARE-BRANCH-SELECTION-STATEMENT.md

---

## 1. Purpose

This note states the minimum hypothesis families that would be needed before a **search-neutral rung-4 basin-access theorem** could be formulated honestly.

It is **not** a theorem. It is an explicit theorem-target outline.

---

## 2. Desired Theorem Shape

A future theorem should look schematically like:

```text
If H1 + H2 + H3 + H4 (+ optional H5/H6) hold,
then raw-search accessibility to a low-energy branch family can be quantitatively separated
from local persistence once the family is entered.
```

Equivalently, the theorem target is not “Type B is always selected,” but rather:

```text
poor raw accessibility and strong local persistence can coexist,
and the two can be bounded by different structural quantities.
```

---

## 3. Minimum Hypothesis Families

### H1 — Branch-family existence and continuation regularity

There is a named low-energy branch family `B(lambda)` that:

- exists on the lambda interval of interest,
- varies regularly under continuation,
- stays inside a controlled active-stratum / KKT regime,
- and remains identifiable as one family rather than a sequence of unrelated discovered states.

Why needed:
- without H1, the theorem has no stable target family to talk about.

Current status:
- **partially supported / locally available**.
- R1-P and seeded continuation results support local branch-family continuation, but not yet a global search-neutral family theorem.

### H2 — Quantitative local basin robustness

There exists a neighborhood `U_B(lambda)` around the target family such that starts inside `U_B(lambda)` return to the same family with probability or rate bounded below by a strong constant.

Why needed:
- this is the formal version of “easy to keep once entered.”

Current status:
- **numerically well supported**, not proved.
- Exp80 gives strong local return evidence on tested configs.

### H3 — Basin-entry corridor separation

There exists a corridor / barrier / region-separation quantity showing that generic raw starts are unlikely to enter `U_B(lambda)` directly.

This may appear as:
- energy-overlap corridor separation,
- active-set region separation,
- communication bottleneck,
- or another explicit entry obstruction.

Why needed:
- without H3, one cannot distinguish poor entry from mere finite-sample search failure.

Current status:
- **partially supported, still open analytically**.
- Exp82 strongly suggests immediate corridor separation, but there is no theorem yet.

### H4 — Access-volume or access-probability control under a search-neutral protocol

For a named raw-search rule, one needs a protocol-neutralizable quantity bounding how often initialization plus descent enters `U_B(lambda)`.

Examples:
- initialization mass of entry states,
- one-step or finite-step entry probability,
- transition probability across coarse region partitions.

Why needed:
- this is what turns “rare in experiments” into a quantitative theorem statement.

Current status:
- **open**.
- Exp79 gives empirical rarity, but there is no analytic access-volume bound.

---

## 4. Secondary / Refinement Hypotheses

### H5 — Active-stratum or support-pattern coherence

Raw and seeded dynamics should admit a coarse partition into region types where transitions can be controlled well enough to distinguish entry-capable and entry-incapable trajectories.

Why useful:
- provides a route from proxy diagnostics to theorem-level path structure.

Current status:
- **suggestive only**.
- Exp81 is supportive as a proxy, not a proof.

### H6 — Search-rule regularity / protocol comparability

The theorem must either:

1. fix one raw-search protocol precisely, or
2. prove robustness across a controlled class of protocols.

Why needed:
- current branch-selection evidence is explicitly protocol dependent.

Current status:
- **open and essential**.
- The search-aware branch-selection note shows this cannot be ignored.

---

## 5. What Is Already Strong Enough vs Still Missing

### Already strong enough to guide theorem design

- local branch-family continuation as a named object (local form);
- strong numerical local robustness after entry;
- strong numerical evidence that raw and seeded trajectories separate immediately;
- explicit guardrail that selected-branch language must be protocol tagged.

### Still genuinely missing

- a search-neutral access-volume or entry-probability bound;
- an analytic corridor-separation theorem rather than trajectory evidence alone;
- a protocol class on which the theorem is meant to hold;
- a clean argument linking path geometry to quantified accessibility failure.

---

## 6. Recommended Theorem-First Reading

The most honest rung-4 target is currently:

```text
Theorem candidate (schematic):
under H1-H4 and a fixed raw-search rule,
a low-energy branch family may have uniformly strong local persistence
while its raw-access probability is bounded above by a much smaller quantity.
```

This is weaker and safer than any branch-selection theorem claiming a canonical globally selected branch.

---

## 7. Immediate Next Trigger

The next theorem-oriented artifact should refine this outline into:

1. a **named theorem candidate statement**, and
2. a table mapping each hypothesis `H1`–`H6` to current evidence:
   - proved,
   - conditional support,
   - numerical support,
   - open.
