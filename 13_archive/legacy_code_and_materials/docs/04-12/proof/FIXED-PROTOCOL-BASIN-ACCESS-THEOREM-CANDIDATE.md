# Fixed-Protocol Basin-Access Theorem Candidate

**Date:** 2026-04-12
**Session:** Cycle 94 — fixed-protocol theorem candidate for protocol-tagged basin-access separation
**Category:** proof
**Status:** active
**Depends on:** docs/04-11/audit/H4-VS-FIXED-PROTOCOL-LANE-DECISION.md; docs/04-11/proof/RUNG-4-BASIN-ACCESS-THEOREM-CANDIDATE.md; docs/04-11/theory/SEARCH-AWARE-BRANCH-SELECTION-STATEMENT.md

---

## 1. Candidate Name

**Fixed-Protocol Basin-Access Separation Candidate**

---

## 2. Statement Shape

A realistic near-term theorem target is:

```text
Fix a configuration G, a lambda interval I, a raw-search protocol S_raw,
and a seeded/upgrade protocol S_seed.
Assume there exists a named branch family B(lambda) on I such that:

1. B(lambda) persists regularly under the seeded protocol,
2. starts sufficiently near B(lambda) return to B(lambda) with a uniform lower bound,
3. S_raw enters a B(lambda)-capturing neighborhood with a much smaller upper bound,
4. S_seed enters that same neighborhood with a much larger lower bound.

Then the accessibility of B(lambda) under S_raw and S_seed can be quantitatively separated,
even though local persistence of B(lambda) remains strong once entry occurs.
```

This candidate is protocol-tagged on purpose. It does **not** claim protocol-neutral branch selection.

---

## 3. Minimal Quantities To Bound

### Q1 — Local return quantity

A lower bound for return to the target family once initialized in a neighborhood `U_B(lambda)`:

```text
P(return to B(lambda) | x0 in U_B(lambda)) >= c_ret
```

Role:
- formalizes local persistence.

Current evidence:
- strong numerical support from Exp80.

### Q2 — Raw-entry quantity

An upper bound for how often the raw protocol enters `U_B(lambda)`:

```text
P_{S_raw}(entry into U_B(lambda)) <= c_raw
```

Role:
- formalizes poor accessibility under raw search.

Current evidence:
- numerical rarity from Exp79, but no theorem-level bound yet.

### Q3 — Seeded-entry quantity

A lower bound for how often the seeded protocol reaches `U_B(lambda)` or stays inside it under continuation:

```text
P_{S_seed}(entry or persistence in U_B(lambda)) >= c_seed
```

Role:
- captures the protocol advantage.

Current evidence:
- seeded continuation / persistence line strongly suggests this, but theorem form is still open.

### Q4 — Protocol-comparison gap

A quantitative separation between raw and seeded accessibility:

```text
c_raw << c_seed
```

Role:
- expresses the core protocol-level asymmetry.

Current evidence:
- qualitatively strong; not yet sharpened into a proved inequality.

---

## 4. Hypothesis Mapping

| Quantity / ingredient | Closest previous hypothesis | Current level |
|---|---|---|
| Q1 local return bound | H2 | numerical support |
| Q2 raw-entry upper bound | H4 | open / empirical only |
| Q3 seeded-entry lower bound | H1 + H2 + protocol-tagged persistence | conditional + numerical support |
| Q4 protocol-comparison gap | H6 + protocol-tagged selection language | open theorem ingredient |

---

## 5. Why This Lane Is Better Right Now

Compared with the search-neutral rung-4 target, this candidate:

- uses the protocol-tagged vocabulary already forced by the evidence;
- avoids pretending that H6 has been neutralized;
- gives a theorem-shaped object whose missing pieces are clearer and smaller.

In particular, the candidate can advance even if the final theorem only applies to one fixed pair `(S_raw, S_seed)`.

---

## 6. Main Remaining Blockers

The candidate is still blocked by two quantitative gaps:

1. a credible upper bound or surrogate bound for `Q2` under `S_raw`, and
2. a theorem-usable comparison statement for `Q4`.

So this lane is narrower than the full H4 problem, but it is not trivialized.

---

## 7. Next Trigger

The next natural artifact is a blocker-focused note asking which quantity should be attacked first:

- `Q2` raw-entry upper bound, or
- `Q4` protocol-comparison inequality.
