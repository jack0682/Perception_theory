# Rung-4 Basin-Access Theorem Candidate

**Date:** 2026-04-11
**Session:** Cycle 92 — named theorem-candidate statement and evidence table
**Category:** proof
**Status:** active
**Depends on:** docs/04-11/proof/RUNG-4-BASIN-ACCESS-THEOREM-OUTLINE.md; docs/04-11/audit/PROOF-ORDER-VERIFICATION-AUDIT.md; docs/04-11/theory/BASIN-ACCESS-CONJECTURE-SUPPORT-LADDER.md

---

## 1. Candidate Name

**Search-Neutral Basin-Access Separation Candidate**

---

## 2. Schematic Candidate Statement

A safe future theorem target is the following.

```text
Fix a configuration G, a lambda interval I, and a precisely defined raw-search rule S_raw.
Assume there exists a low-energy branch family B(lambda) that persists regularly on I,
with a quantitatively robust local basin U_B(lambda), and assume moreover that
entry from S_raw-initialized trajectories into U_B(lambda) is controlled by a
strictly smaller accessibility quantity than the local return quantity inside U_B(lambda).
Then raw-search accessibility to B(lambda) and local persistence of B(lambda)
can be quantitatively separated on I.
```

This candidate is intentionally weaker than any theorem claiming a canonical globally selected branch.

---

## 3. H1–H6 Evidence Table

| Hypothesis | Meaning | Current status | Present support level | Main evidence / blocker |
|---|---|---|---|---|
| H1 | Branch-family existence and continuation regularity | local form available, global theorem missing | **conditional support** | R1-P local continuation; seeded continuation results; still no search-neutral global family theorem |
| H2 | Quantitative local basin robustness | strongly observed on tested configs | **numerical support** | Exp80 / dense Exp80 show 100% return across tested sigma ladder |
| H3 | Basin-entry corridor separation | strongly suggested, not proved | **numerical support** | Exp82 immediate divergence at iter 1; no analytic corridor theorem yet |
| H4 | Access-volume / entry-probability control | not yet formulated analytically | **open** | Exp79 gives empirical rarity only; no theorem-level access bound |
| H5 | Active-stratum / support-pattern coherence | useful refinement, still proxy-level | **numerical support** | Exp81 transition-count asymmetry supports it, but only as proxy diagnostics |
| H6 | Search-rule regularity / protocol comparability | essential and unresolved | **open** | search-aware branch-selection statement shows protocol dependence cannot be ignored |

---

## 4. Immediate Reading

The candidate is currently blocked mainly by **H4** and **H6**, with **H3** also still below theorem level.

So the continuation-access line is now in the following state:

- theorem-target shape exists,
- hypothesis families are named,
- evidence is already strong for H2 and useful for H3/H5,
- but search-neutral accessibility control is still missing.

---

## 5. Practical Consequence

The most theorem-efficient next move is not another generic replication.

Instead, future work should target one of the genuine blockers:

1. an analytic access-volume / entry-probability bound for H4, or
2. a fixed-protocol theorem lane that weakens the need for full H6.

---

## 6. Guardrail

Until H4 and H6 are converted from open blockers into explicit proved or conditionally proved ingredients, the continuation-access line must remain below theorem status.
