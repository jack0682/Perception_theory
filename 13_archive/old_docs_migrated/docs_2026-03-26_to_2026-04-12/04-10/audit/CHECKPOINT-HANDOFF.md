# Checkpoint Handoff — 04-10 Ralph Theorem-Closing Campaign

**Date:** 2026-04-10
**Session:** checkpoint / handoff after exp69 scaffold
**Category:** audit
**Status:** active
**Depends on:** CAMPAIGN-SYNTHESIS.md; THEOREM-STATUS-REGISTRY.md; NEXT-TRIGGER.md

---

## 1. Scope Completed

This checkpoint covers the 04-10 theorem-closing campaign from gap table construction through branch-conditioned spec sync and relaxed-merge communication-height scaffolding.

Major result: all currently listed Category B / Category C formal gaps and current research blockers have a 04-10 proof/audit artifact. No official Canonical Spec theorem counts were changed.

---

## 2. Current Official Counts

```text
35 Category A / 4 Category B / 5 Category C / 5 Retracted
```

Spec wording was synced to make branch/regime/path conditioning explicit, but counts were preserved.

---

## 3. Key Outcomes

| Area | Outcome |
|---|---|
| R1 branch selection | local branch continuation proved; zero-repulsion degeneracy proved; positive-repulsion overlap selection proved; overlap=>centeredness disproved |
| B1/R4 merge/F'' | branch-local `F_B''` meaningful; branch-free `F''` rejected; relaxed manifold `R_M^2` defined |
| B3 d_min | branch-conditioned notation required; coefficients remain empirical |
| B4 Beyond-Weyl | structured theorem split from empirical 33x factor |
| C1/C2 persistence | shifted/deep-core/all-core variants separated |
| C3-C5 K-persistence | regime/selected-branch conditioning clarified |
| R2 near-bifurcation | quartic and cubic normal-form bounds/obstructions recorded |
| R3 kinetics | minimal branch-state variables and Kramers assumptions specified |
| R4 relaxed merge | local barrier proved; global barrier remains path-class/sublevel conditioned |
| exp65-exp69 | branch tracking and relaxed merge path scaffolds implemented with smoke evidence |

---

## 4. Verification Evidence So Far

Recent commands passed:

```bash
git diff --check
python3 -m py_compile \
  experiments/exp65_formation_tracking.py \
  experiments/exp66_branch_selection_sweep.py \
  experiments/exp67_relaxed_merge_paths.py \
  experiments/exp68_relaxed_merge_neb.py \
  experiments/exp69_relaxed_merge_neb_sweep.py \
  experiments/exp_cohesion_scale.py
```

Earlier in the same session:

```text
python3 -m pytest tests/ -q
175 passed
```

Fresh full pytest rerun completed after this checkpoint update:

```text
python3 -m pytest tests/ -q
175 passed in 181.05s (0:03:01)
```

---

## 5. Known Risks

| Risk | Status |
|---|---|
| Many untracked files | expected; campaign generated docs, experiments, results |
| exp68 projection is heuristic | documented; not theorem evidence |
| exp69 numerical scaffold is not MEP proof | documented |
| Canonical Spec sync was wording-only | counts unchanged; should be reviewed before publication |
| `experiments/exp_cohesion_scale.py` had prior partial GPU removal | minimally repaired to CPU mode; not central to proof campaign |

---

## 6. Recommended Next Action

Decision point:

1. **If preparing commit/PR:** review/stage coherent set, use Lore commit protocol, mention no theorem count changes.
2. **If continuing proofs:** run targeted exp69 sweep or start deterministic sublevel separation theorem for a restricted path class.
3. **If cleaning first:** split docs vs experiment artifacts; consider whether all smoke JSON/CSV files should be tracked.

---

## 7. Active Next Trigger

Current next trigger is in:

```text
docs/04-10/audit/NEXT-TRIGGER.md
```

It currently points to checkpoint / commit-handoff decision or targeted exp69 sweep, depending on project lead preference.
