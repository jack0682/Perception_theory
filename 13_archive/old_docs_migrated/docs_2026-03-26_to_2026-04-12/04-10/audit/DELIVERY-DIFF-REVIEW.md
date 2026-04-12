# Delivery Diff Review — 04-10 SCC Gap Campaign

**Date:** 2026-04-10
**Session:** Ralph delivery / commit-prep review
**Category:** audit
**Status:** complete
**Depends on:** FINAL-RALPH-HANDOFF.md; CHECKPOINT-HANDOFF.md; CHANGELOG.md

---

## 1. Current Git Scope

Tracked files modified:

| File | Reason |
|---|---|
| `CHANGELOG.md` | Session log for theorem-closing campaign and verification |
| `Canonical Spec v2.1.md` | Branch/regime/path-conditioned wording sync; theorem counts unchanged |
| `experiments/exp_cohesion_scale.py` | Minimal repair of stale `args.gpu` reference after prior partial GPU removal |

New files:

- `docs/04-10/` campaign docs/proofs/audits/index
- `experiments/exp65_formation_tracking.py`
- `experiments/exp66_branch_selection_sweep.py`
- `experiments/exp67_relaxed_merge_paths.py`
- `experiments/exp68_relaxed_merge_neb.py`
- `experiments/exp69_relaxed_merge_neb_sweep.py`
- cited JSON/CSV result artifacts under `experiments/results/`

---

## 2. Result Artifact Tracking Recommendation

Track JSON/CSV result artifacts that are explicitly cited by 04-10 docs. Do not track transient `.log` files.

Already removed from working tree:

```text
experiments/results/exp65_sweep_20x20_c06_lrep_*.log
experiments/results/exp68_*_smoke.log
```

Recommended to track:

| Result group | Reason |
|---|---|
| exp65 tracking and lambda probes | cited by branch-selection analysis |
| exp65 sweep 20x20_c06 lrep CSV/JSON | supports singular zero-repulsion transition analysis |
| exp66 tail sweep | supports positive-lambda Type A continuation at higher repulsion |
| exp67 smoke | baseline direct-vs-diffuse path scaffold evidence |
| exp68 smoke configs | NEB-lite path improvement evidence with constraints |
| exp69 smoke/lrep sweeps | reusable aggregator evidence and repulsion scaling |

---

## 3. Suggested Commit Split

### Commit 1 — docs/spec theorem audit

Scope:

- `docs/04-10/**`
- `Canonical Spec v2.1.md`
- `CHANGELOG.md`

Intent:

```text
Document branch-conditioned SCC gap closure decisions
```

### Commit 2 — experiment scaffolds/results

Scope:

- `experiments/exp65_formation_tracking.py`
- `experiments/exp66_branch_selection_sweep.py`
- `experiments/exp67_relaxed_merge_paths.py`
- `experiments/exp68_relaxed_merge_neb.py`
- `experiments/exp69_relaxed_merge_neb_sweep.py`
- `experiments/results/exp65*`, `exp66*`, `exp67*`, `exp68*`, `exp69*` JSON/CSV cited by docs
- `experiments/exp_cohesion_scale.py`

Intent:

```text
Add branch and relaxed-merge communication-height experiment scaffolds
```

### Alternative: one broad commit

```text
Document and scaffold SCC branch-conditioned gap closure campaign
```

This is simpler but large.

---

## 4. Lore Commit Drafts

### Commit 1 draft

```text
Document branch-conditioned SCC gap closure decisions

The 04-10 campaign audits the remaining Category B/C and research-blocker gaps,
then records branch-, regime-, and path-conditioned theorem formulations without
changing official theorem counts.

Constraint: Canonical Spec theorem counts must remain 35A/4B/5C/5R
Rejected: Upgrade B/C items directly | evidence supports conditioning/reformulation, not count changes
Confidence: high
Scope-risk: moderate
Directive: Do not treat branch-conditioned scalar quantities as branch-free invariants
Tested: docs grep review; git diff --check
Not-tested: independent mathematical referee review
```

### Commit 2 draft

```text
Add SCC branch and relaxed-merge communication-height scaffolds

The experiment scripts track K=2 branch geometry and compare relaxed merge path
classes, including NEB-lite path relaxation and sweep aggregation for numerical
support of communication-height questions.

Constraint: Experiments are numerical scaffolds, not theorem evidence
Rejected: Treat direct interpolation as MEP | NEB-lite lowers direct path proxy in smoke tests
Confidence: medium
Scope-risk: moderate
Directive: Do not cite exp68/exp69 as proof of true MEP without convergence/path-class analysis
Tested: py_compile for exp65-exp69; exp67/exp68/exp69 smoke runs; pytest 175 passed
Not-tested: large-grid runtime, NEB convergence, exact relaxed-manifold projection
```

---

## 5. Verification Evidence

Latest known verification:

```text
git diff --check — passed
python3 -m py_compile exp65-exp69 + exp_cohesion_scale — passed
python3 -m pytest tests/ -q — 175 passed in 181.05s
```

---

## 6. Next Trigger

If committing:

1. run `git status --short`;
2. review staged scope;
3. commit with Lore protocol.

If continuing theorem work:

1. use exp69 for a targeted sweep tied to a specific path-class question;
2. avoid open-ended numerical exploration without theorem target.
