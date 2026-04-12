# Basin-Access Asymmetry Mechanism Note

**Date:** 2026-04-11
**Session:** Cycle 81 — analytic mechanism note for continuation access
**Category:** theory
**Status:** complete
**Depends on:** docs/04-11/audit/CONTINUATION-ACCESS-CONJECTURE-REGISTER.md; docs/04-11/proof/CONTINUATION-ACCESS-SUPPORT-PROPOSITION.md; docs/04-11/experiment/EXP79-CONTINUATION-ACCESS-DIAGNOSTIC-20x20_c0.6.md; docs/04-11/experiment/EXP80-LOCAL-BASIN-PROXY-20x20_c0.6.md

---

## 1. Mechanism Picture

The current best explanatory picture for R1-Q3 is:

> the low-energy Type B branch sits inside a robust local basin, but the basin has poor accessibility from independent raw starts.

So the observed search gap is not “the branch is unstable,” but rather:

```text
entry problem >> local stability problem.
```

---

## 2. Minimal Mechanism Decomposition

### Layer A — Local basin robustness

Once the optimizer is started sufficiently near the Type B branch, it returns to that family reliably.

This is the local-stability side of the story.

### Layer B — Poor raw basin access

Independent random initializations almost never land in a state that flows into the same branch family at the target lambda.

This is the access side of the story.

### Layer C — Protocol advantage

Seeded continuation and injected optimization effectively transport the optimizer into the right basin before local descent dominates.

This is why `Sel_upgrade` can systematically outperform `Sel_raw`.

---

## 3. Why This Is Stronger Than a Generic Nonconvexity Story

A generic nonconvexity explanation would only say “there are many local minima.”

The current evidence is sharper:

- one specific family is hard to access from raw starts,
- yet once accessed it is robust,
- and injected-seed optimization repeatedly finds it and improves upon raw search.

So the mechanism is not merely multiplicity of minima, but **asymmetric access to a robust low-energy basin**.

---

## 4. Relation to Alternative Mechanisms

### Compared with active-set trapping

Active-set trapping may still be part of the dynamics, but it now looks secondary:

- it can explain *how* trajectories diverge,
- but the primary empirical asymmetry is already captured at the basin-access level.

### Compared with basin-volume asymmetry

Basin-volume asymmetry can be treated as a geometric refinement of the present mechanism note:

- if the Type B basin occupies less initialization volume but has a lower minimum, then the current observations follow naturally.

So basin-volume asymmetry is best read as one concrete geometric realization of basin-access asymmetry.

---

## 5. Working Consequence

For current SCC branch-selection work, the following methodological rule is now justified:

> raw multistart failure to find a branch family is weak evidence about nonexistence when seeded continuation demonstrates both access and local robustness.

That rule should govern how future numerical branch-selection claims are interpreted.

---

## 6. Next Trigger

If the campaign wants one more explanatory step, the natural follow-up is to make basin-access asymmetry more quantitative — for example by a basin-size proxy scaling study or a more explicit access-path diagnostic.
