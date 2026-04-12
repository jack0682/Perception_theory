# Next Rung Choice After the Basin-Access Ladder

**Date:** 2026-04-11
**Session:** Cycle 90 — choose between strengthening rung 3 and outlining rung 4
**Category:** audit
**Status:** complete
**Depends on:** docs/04-11/audit/PROOF-ORDER-VERIFICATION-AUDIT.md; docs/04-11/theory/BASIN-ACCESS-CONJECTURE-SUPPORT-LADDER.md

---

## 1. Options

### Option A — strengthen rung 3

Meaning:

> add one broader numerical-support extension to the continuation-access line.

Pros:
- would widen the tested support base;
- keeps the current evidence chain numerically stronger;
- could sharpen how config-sensitive the access asymmetry is.

Cons:
- does not remove the main theorem blocker;
- risks extending an already well-supported empirical lane without clarifying what a theorem would actually need;
- does not by itself neutralize search-protocol dependence.

### Option B — outline rung 4 hypotheses

Meaning:

> write the explicit structural hypotheses needed for an eventual search-neutral basin-access theorem.

Pros:
- attacks the current bottleneck directly;
- prevents theorem inflation by stating exactly what must be assumed;
- turns the next numerical work into targeted evidence for named hypotheses instead of open-ended replication.

Cons:
- does not immediately broaden the empirical base;
- the first outline may be conservative and still incomplete.

---

## 2. Decision

**Choose Option B first: outline rung 4 hypotheses.**

Reason:

1. the proof-order audit shows the continuation-access line is already strong at rung 3;
2. the open gap is no longer “is there any support?” but “what explicit structure would a theorem require?”;
3. a hypothesis outline makes every later experiment more disciplined, because each diagnostic can be attached to a named assumption.

---

## 3. Immediate Consequence

The next proof lane should aim at a note of the form:

```text
Search-neutral basin-access theorem candidate:
if H1 + H2 + H3 + ... hold,
then raw accessibility and local persistence can be quantitatively separated.
```

Likely hypothesis families include:
- basin-entry corridor separation;
- active-stratum / support-pattern coherence;
- continuation-path regularity;
- protocol-independent access-volume lower/upper bounds.

---

## 4. Guardrail

Until that hypothesis outline exists, do **not** upgrade the continuation-access line beyond rung 3.

---

## 5. Next Trigger

Write a compact theorem-target outline listing the minimum explicit hypotheses needed for a search-neutral basin-access theorem candidate.
