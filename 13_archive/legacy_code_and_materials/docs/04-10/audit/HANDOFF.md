# Handoff

**Date:** 2026-04-10
**Session:** Cycle 1 handoff
**Category:** audit
**Status:** active
**Depends on:** docs/04-10/audit/PROOF-ATTEMPTS.md; docs/04-10/audit/THEOREM-STATUS-REGISTRY.md

---

## What Was Proved

A local analytic branch-continuation theorem (R1-P) was formulated and proved under explicit hypotheses: finite graph, admissible analytic SCC parameters, fixed active set/penalty region, strict KKT nondegeneracy, and specified branch/selection context.

Two R1 support lemmas were also added:

1. zero-repulsion automorphism degeneracy: at `lambda_rep=0`, automorphism-related barrier-feasible branch pairs can be energy-degenerate;
2. positive-repulsion first-order selection: among equal-energy zero-barrier candidates, positive repulsion orders branches by overlap, and smooth branch energy satisfies `F'(lambda_rep)=<u_1,u_2>`.

## What Failed

The universal scalar branch-selection claim failed. Type A/B cannot be treated as a function only of `(grid_size,c_ref)` or a branch-free regime scalar.

## What Remains Open

R1-Q was sharpened by the `20x20_c0.6` sweep: Type B appears at `lambda_rep=0`, while every tested positive value `lambda_rep >= 0.05` selects Type A under the exp65 protocol. The remaining open target is now R1-G: a graph-geometric overlap-to-centeredness lemma. Positive repulsion selects minimum-overlap branches, but it is not yet proved that minimum overlap implies the Type A/centered descriptor under square-grid hypotheses.

## Files Changed in This Cycle

- docs/04-10/audit/SESSION-INDEX.md
- docs/04-10/audit/GAP-REGISTRY.md
- docs/04-10/audit/CURRENT-TARGET.md
- docs/04-10/audit/ASSUMPTION-REGISTRY.md
- docs/04-10/audit/METHOD-LEDGER.md
- docs/04-10/audit/PROOF-ATTEMPTS.md
- docs/04-10/audit/COUNTEREXAMPLES.md
- docs/04-10/audit/BRANCH-SELECTION-NOTES.md
- docs/04-10/audit/EXPERIMENT-THEORY-BRIDGE.md
- docs/04-10/audit/THEOREM-STATUS-REGISTRY.md
- docs/04-10/audit/HANDOFF.md
- docs/04-10/audit/NEXT-TRIGGER.md
- docs/04-10/audit/SWEEP-ANALYSIS-R1.md
- docs/04-10/proof/ZERO-REPULSION-BRANCH-DEGENERACY.md
- docs/04-10/proof/POSITIVE-REPULSION-SELECTION.md

## Exact Next Subproblem

Attack the graph-geometric overlap-to-centeredness lemma: determine whether minimum-overlap feasible K=2 placements on square grids imply Type A/centered placement, or produce a counterexample and reformulate Type A as minimum-overlap rather than geometric centeredness.

## R1-G Addendum

R1-G was closed negatively: overlap minimization does not imply centeredness. The universal centeredness implication is disproved by the square-grid corner-placement counterexample. The corrected branch-selection target is now a tie-breaker theorem: minimum overlap plus maximum separation / symmetry rule.

## Final continuation addendum

The loop continued beyond the first R4 definition. Added relaxed merge lower-bound artifacts and Kramers-rate formulation:

- `RELAXED-MERGE-BARRIER-LOWER-BOUND.md`
- `RELAXED-LOCAL-BASIN-BARRIER.md`
- `RELAXED-MERGE-GLOBAL-PATH-CONDITION.md`
- `R3-KRAMERS-RATE-FORMULATION.md`

Current next hard target is no longer definitional; it is the global MEP after local basin escape, plus a rigorous constrained Langevin/Kramers theorem if stochastic rates are to be claimed.

## Post-local-basin continuation addendum

The loop continued through post-local-basin relaxed merge analysis:

- `RELAXED-MERGE-MEP-AFTER-ESCAPE.md`: additional barrier beyond local escape is conditional on sublevel-set separation.
- `RELAXED-MERGE-SUBLEVEL-SEPARATION.md`: dissolve-spread-transfer-reconcentrate is a real obstruction; direct interpolation is not an MEP lower bound.
- `RELAXED-MERGE-CORE-PRESERVING-PATHS.md`: core-preserving path class is meaningful for identity-preserving merge but artificial for unrestricted coarsening.
- `CORE-DISSOLUTION-LOWER-BOUND.md`: single-site threshold crossing lower bound `beta W(theta)` proved.
- `CORE-DISSOLUTION-NO-PEELING.md`: q-site band bound proved; mass-scaled bound requires collective/no-peeling restriction.

Next hard target: decide whether to formalize a physically justified collective-dissolution path class, or pivot to stochastic constrained Langevin/Kramers theorem assumptions.
