# R1-Q Protocol-Tagged Reformulation

**Date:** 2026-04-11
**Session:** Cycle 67 — protocol-tagged reformulation of R1-Q
**Category:** audit
**Status:** complete
**Depends on:** docs/04-11/theory/SEARCH-AWARE-BRANCH-SELECTION-STATEMENT.md; docs/04-10/audit/GAP-REGISTRY.md; docs/04-10/audit/BRANCH-SELECTION-NOTES.md

---

## 1. CURRENT GAP

The original wording of R1-Q implicitly treated “the selected branch” as if it were a branch-free object. The accumulated Exp73–Exp78 evidence now shows that this is too coarse: branch-threshold claims change when the search protocol changes.

So R1-Q must be reformulated before further theorem-closing work can proceed honestly.

---

## 2. Unsafe Form (Rejected)

Unsafe wording:

> There is a single K=2 branch-selection threshold `lambda_*` at which the selected branch changes type.

Why this is unsafe:

1. it suppresses the search protocol;
2. it conflates discovered branches with selected branches;
3. it confuses persistence of a branch family with protocol-dependent branch selection;
4. it suggests a branch-free scalar invariant that the evidence does not support.

---

## 3. Protocol-Tagged Objects

For fixed graph/configuration `G`, parameter tuple `p`, and search protocol `S`, define:

- `Disc_S(G,p)` = branch set discovered by protocol `S`
- `Sel_S(G,p)` = lowest-energy branch inside `Disc_S(G,p)`
- `Pers_seed(G,p)` = branch obtained by seeded/warm continuation from a named seed family

Examples of protocols `S` used in the current campaign:

- `raw` = raw multistart catalog search
- `upgrade` = direct optimization with an injected continuation seed
- `seed` = warm continuation from a recovered seed family

---

## 4. Corrected R1-Q Split

R1-Q should now be split into three non-equivalent questions.

### R1-Q1 — Persistence Question

Does a named branch family persist under continuation in `lambda_rep`?

This is a question about `Pers_seed(G,p)` and branch-family survival, not about raw selection.

### R1-Q2 — Protocol-Dependent Selection Question

For a fixed search protocol `S`, when does `Sel_S(G,p)` change branch family?

This is a protocol-tagged selected-branch question.

### R1-Q3 — Search Reliability Gap

How different can `Sel_raw(G,p)` and `Sel_upgrade(G,p)` be, and under what conditions do they belong to different branch families or have significantly different energies?

This is the new active obstruction exposed by Exp77–Exp78.

---

## 5. What Is Now Numerically Supported

The campaign currently supports the following **numerical-only** conclusions:

1. there exist configs where `Pers_seed(G,p)` survives to positive `lambda_rep` and even to `lambda_rep=1.0`;
2. there exist configs where `Sel_raw(G,p)` and `Sel_upgrade(G,p)` disagree on the selected branch family;
3. in multiple sentinel configs, `Sel_upgrade(G,p)` has strictly lower energy than both `Sel_raw(G,p)` and the plain warm continuation branch sampled before the upgrade step.

Therefore the next honest theorem-support target is not a branch-free threshold scalar, but a protocol-tagged relation among `Disc_S`, `Sel_S`, and `Pers_seed`.

---

## 6. Immediate Guardrails

Until a search-neutral selection theorem exists, all future branch-threshold wording must obey:

1. never say “the selected branch” without naming the protocol;
2. never identify a persistence threshold with a selected-branch threshold unless protocol invariance is checked;
3. never use raw multistart outcomes alone as evidence of canonical selected-branch structure.

---

## 7. Decision

| Item | Outcome |
|---|---|
| branch-free R1-Q wording | rejected |
| protocol-tagged R1-Q wording | adopted for ongoing audits |
| active subgap | R1-Q3, the search reliability gap |

---

## 8. Next Trigger

Use this reformulation to write the next canonical R1-Q status note:

> state separately what is known about branch persistence, what is known about protocol-dependent branch selection, and what remains open about search-neutral selected-branch inference.
