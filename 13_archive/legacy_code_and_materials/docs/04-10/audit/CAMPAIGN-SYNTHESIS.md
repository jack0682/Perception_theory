# Campaign Synthesis — SCC Remaining Gap Closure Pass

**Date:** 2026-04-10
**Session:** Cycle 18 — theorem-status synchronization proposal
**Category:** audit
**Status:** complete
**Depends on:** docs/04-10/audit/THEOREM-STATUS-REGISTRY.md; docs/04-10/audit/LATEST-GAP-TABLE.md

---

## 1. Campaign Scope

This pass processed every active Category B, Category C, and research-blocker item from `LATEST-GAP-TABLE.md`.

No Canonical Spec theorem category was changed. The campaign produced proof/audit artifacts that clarify what is proved, conditional, false, or structurally open.

---

## 2. Formal Category B Outcomes

| ID | Item | Outcome | File |
|---|---|---|---|
| B1 | `gamma_eff` / merge barrier | branch-local `F_B''` proved meaningful; branch-free `F''` rejected; exponent remains empirical | `B1-R4-BRANCH-CONDITIONED-MERGE.md` |
| B2 | general-graph birth supercriticality | existence/instability proved; D4 and sufficient-gap supercriticality proved; narrow-gap/non-D4 degeneracy remains Cat B | `B2-GENERAL-BIRTH-SUPERCRITICALITY.md` |
| B3 | `d_min*` formula | qualitative threshold retained; coefficients remain empirical; branch-free scalar rejected | `B3-DMIN-BRANCH-CONDITIONED.md` |
| B4 | Beyond-Weyl 33x | structured perturbation theorem separated from empirical `33x`; universal factor rejected | `B4-BEYOND-WEYL-QUANTIFICATION.md` |

---

## 3. Formal Category C Outcomes

| ID | Item | Outcome | File |
|---|---|---|---|
| C1 | T-Persist-1(d) | exact-threshold preservation condition is structural; shifted threshold is proved; all-core exact is too strong | `C1-TPERSIST-EXACT-THRESHOLD.md` |
| C2 | T-Persist-Full | should be tiered into shifted, deep-exact, and invalid all-core-exact variants | `C2-TPERSIST-FULL-COMPOSITION.md` |
| C3 | T-Persist-K-Sep | proved as Sep-regime theorem; Category C globally because WS/SR are regime definitions | `C3-TPERSIST-K-SEP-REGIME.md` |
| C4 | T-Persist-K-Weak | conditionally proved as Weak-regime theorem; WI/SR/NB-K non-removable | `C4-TPERSIST-K-WEAK-REGIME.md` |
| C5 | T-Persist-K-Unified | selected-branch conditional theorem; `Lambda` alone cannot classify branch identity | `C5-TPERSIST-K-UNIFIED-REGIME.md` |

---

## 4. Research Blocker Outcomes

| ID | Item | Outcome | File |
|---|---|---|---|
| R1 | K=2 branch selection | local branch continuation proved; zero-repulsion degeneracy proved; positive-repulsion overlap selection proved; overlap⇒centeredness disproved | `PROOF-ATTEMPTS.md`, `ZERO-REPULSION-BRANCH-DEGENERACY.md`, `POSITIVE-REPULSION-SELECTION.md`, `OVERLAP-TO-CENTEREDNESS-COUNTEREXAMPLE.md` |
| R2 | near-bifurcation persistence | uniform persistence rejected; quartic normal-form scaling proved; cubic asymmetry obstruction recorded | `R2-NEAR-BIFURCATION-PERSISTENCE.md`, `NEARBIF-NORMAL-FORM-BOUND.md`, `NEARBIF-CUBIC-NORMAL-FORM.md` |
| R3 | kinetic dynamics | minimal branch-aware kinetic state specified; Kramers-rate assumptions separated from theorem claims | `R3-KINETIC-DYNAMICS-STATE.md`, `R3-KRAMERS-RATE-FORMULATION.md` |
| R4 | relaxed merge barrier | valid relaxed manifold defined; finite-image minimax existence proved; universal positive lower bound rejected; local quadratic basin barrier proved; target-outside-basin condition proved under mass/radius assumptions | `R4-RELAXED-MERGE-MANIFOLD.md`, `RELAXED-MERGE-BARRIER-LOWER-BOUND.md`, `RELAXED-LOCAL-BASIN-BARRIER.md`, `RELAXED-MERGE-GLOBAL-PATH-CONDITION.md` |

---

## 5. Proposed Future Canonical Spec Edits

Do **not** apply automatically without a dedicated spec-sync pass.

| Spec area | Proposed edit |
|---|---|
| theorem registry counts | keep current 35A/4B/5C/5R |
| B1 | explicitly say `gamma_eff` is branch/path/manifold conditioned |
| B3 | write `d_min*(B, rule, params, graph)` rather than branch-free `d_min*` |
| B4 | split structured perturbation theorem from empirical `33x` factor |
| C1/C2 | distinguish shifted-threshold, deep-core exact, and all-core exact persistence |
| C3/C4/C5 | label as regime/selected-branch theorems rather than global unconditional theorems |
| R1 additions | add branch-selection note: overlap minimization does not imply centeredness without tie-breaker |
| R4 additions | define relaxed merge manifold `R_M^2` before any future merge-barrier theorem |

---

## 6. Remaining Proof Targets

| Priority | Target | First proof move |
|---:|---|---|
| 1 | global relaxed merge MEP after local escape | bound/compute the minimum-energy path outside the local basin and rule out dissolve-spread-transfer shortcuts |
| 2 | Kramers theorem for SCC constrained dynamics | choose reflected/projected Langevin model and prove or cite finite-dimensional constrained Kramers asymptotics |
| 3 | branch-conditioned `d_min*` bounds | derive bounds after tie-breaker rule is fixed |
| 4 | narrow-gap birth supercriticality | analyze finite-dimensional normal form coefficients |
| 5 | full branch-state transition graph | define event graph over `(K, branch_id, geometry, barrier)` states |

---

## 7. Verification / Safety

No official theorem category was upgraded. Several universal claims were rejected or reformulated instead:

- branch-free Type A/B classification,
- minimum-overlap implies centeredness,
- branch-free `F''(M/2)`,
- universal `gamma_eff`,
- universal `d_min*`,
- universal `33x` Beyond-Weyl factor,
- all-core exact-threshold persistence.

---

## 8. Next Trigger

Proceed to a dedicated spec-sync planning pass, not direct spec editing.

First move:

> Create a patch plan for Canonical Spec v2.1 that lists exact sections/lines to update, with no theorem category changes unless explicitly justified.

---

## 9. Cycle 21-24 Addendum

After the initial synthesis, the campaign continued through relaxed merge and kinetic-rate support targets:

| Artifact | Outcome |
|---|---|
| `RELAXED-MERGE-BARRIER-LOWER-BOUND.md` | finite-image minimax existence proved; universal positive lower bound rejected; vanishing second-formation degeneration proved |
| `RELAXED-LOCAL-BASIN-BARRIER.md` | quadratic local escape barrier proved from relaxed Hessian gap under stratified SOSC |
| `RELAXED-MERGE-GLOBAL-PATH-CONDITION.md` | target-outside-local-basin condition proved under mass lower bound and basin-radius inequality |
| `R3-KRAMERS-RATE-FORMULATION.md` | stochastic model assumptions required before Kramers-rate claims specified |

No Canonical Spec category counts changed.

---

## 10. Cycle 25-29 Addendum

The campaign continued through post-local-basin relaxed merge analysis and event-specific core dissolution bounds:

| Artifact | Outcome |
|---|---|
| `RELAXED-MERGE-MEP-AFTER-ESCAPE.md` | post-escape separation criterion proved conditionally; no automatic additional barrier beyond local escape |
| `RELAXED-MERGE-SUBLEVEL-SEPARATION.md` | direct interpolation rejected as MEP lower bound; diffuse shortcut identified as real obstruction class |
| `RELAXED-MERGE-CORE-PRESERVING-PATHS.md` | core-preserving path class defined; meaningful for identity-preserving merge but artificial for unrestricted MEP |
| `CORE-DISSOLUTION-LOWER-BOUND.md` | single-site threshold crossing cost `beta W(theta)` proved; mass-scaled bound rejected without synchronization/no-peeling assumptions |
| `CORE-DISSOLUTION-NO-PEELING.md` | q-site threshold-band lower bound proved; exact simultaneous all-core crossing rejected as nongeneric/artificial |

No Canonical Spec category counts changed. The relaxed merge barrier program is now narrowed to path-class-specific morphology bottlenecks and stochastic-rate modeling assumptions.
