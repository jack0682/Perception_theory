# Near-Bifurcation Local Theory for Restricted Persistence

**Date:** 2026-03-31
**Session:** Plan_0331 execution — local theory for persistence failure near bifurcation
**Category:** theory
**Status:** complete
**Depends on:** docs/03-31/repair/PERSIST-SYNTHESIS.md, docs/03-31/proof/BASIN-ESCAPE-ANALYSIS.md, docs/03-31/repair/PERSIST-MORSE-ANALYSIS.md, Canonical Spec v2.0.md

---

## 1. Purpose

This document isolates the mathematically honest statement available **near bifurcation**.

The central claim is negative/restricted, not positive:

> Near bifurcation, the full persistence theorem should **not** be stated.  
> What survives is only a **local restricted-persistence principle**: exact-threshold / full-basin persistence fails generically, while weaker continuation statements (shifted-threshold, deep-core remnant, branch-local persistence) may still survive under additional local assumptions.

This reformulation is forced by the current basin analysis and by the existing plan itself, which already lists near-bifurcation basin and near-bifurcation persistence as open problems (`plan/Plan_0331.md:45-46`).

---

## 2. The Structural Mechanism of Failure

The single-formation basin analysis establishes a three-regime picture for escape barriers (`docs/03-31/proof/BASIN-ESCAPE-ANALYSIS.md:203-232`):

1. **away from bifurcation:** boundary barrier remains `O(1)` and basin containment is feasible;
2. **near bifurcation:** the boundary barrier `Δ_bdy` collapses together with the relevant soft spectral gap;
3. **at bifurcation:** no finite basin radius exists in the bifurcating direction.

Thus the basic temporal-persistence mechanism fails for a geometric reason:
\[
\mu \to 0, \qquad \Delta_{\mathrm{bdy}} \to 0,
\]
so the transported perturbation is no longer small relative to the shrinking basin.

The repository already says this in effect:

- `docs/03-31/proof/BASIN-ESCAPE-ANALYSIS.md:224-232`
- `docs/03-31/repair/PERSIST-SYNTHESIS.md:130`
- `Canonical Spec v2.0.md:1001`

The correct conclusion is therefore **not** “persistence theorem still holds with worse constants,” but rather:

> the basic basin-containment hypothesis of full persistence becomes structurally unstable near bifurcation.

---

## 3. What Exactly Fails

Near bifurcation, the following full-strength statements are no longer mathematically honest as general theorems.

### 3.1. Full basin containment

The standard persistence route requires
\[
2\varepsilon_2 + \frac{2\varepsilon_1}{\mu} < r_{\mathrm{basin}}.
\]

But near bifurcation,
- `μ` decreases,
- `2ε_1/μ` blows up,
- `r_basin` shrinks because `Δ_bdy` collapses.

This is exactly the mechanism recorded in the basin analysis (`docs/03-31/proof/BASIN-ESCAPE-ANALYSIS.md:224-232`).

### 3.2. Exact-threshold persistence

Exact-threshold persistence relies on a positive interior margin that dominates the transported displacement. Near bifurcation, the same soft mode that collapses the basin also destroys any robust exact-threshold claim except possibly on a restricted deep-core subset.

### 3.3. Uniform persistence across the whole core

The two-tier structure already shows boundary/shallow-core sites are the first to lose rigidity (`Canonical Spec v2.0.md:972-980`, `996-1001`). Near bifurcation this becomes decisive: the boundary negotiation region becomes the active instability channel.

---

## 4. What Survives

Near bifurcation, the correct surviving statements are **local and tiered**.

### 4.1. Restricted persistence principle

**Principle RP-NB (Restricted Persistence Near Bifurcation).**

Suppose a branch of formation-structured critical points persists up to a shape-transition set where the active-set-aware spectral gap satisfies `μ -> 0`. Then, in a sufficiently small neighborhood of the bifurcation set:

1. the full basin-containment inequality generically fails;
2. exact-threshold persistence is not stable as a uniform theorem;
3. only branch-local continuation / shifted-threshold statements can remain valid;
4. any surviving transport concentration must be formulated on a **deep-core remnant**, not on the entire core.

This is the strongest honest formulation consistent with existing materials.

### 4.2. Shifted-threshold persistence may survive

The existing synthesis already recommends that near bifurcation only the weaker shifted-threshold result should be asserted (`docs/03-31/repair/PERSIST-SYNTHESIS.md:130`).

So the correct local statement is:

- **full persistence:** not available,
- **shifted-threshold persistence:** still locally plausible if one stays on the same branch,
- **deep-core remnant persistence:** plausible only where `δ(x) >= 2` and the local interior gap remains positive.

### 4.3. Deep-core remnant principle

Even near bifurcation, instability is boundary-dominated, not core-dominated (`docs/03-31/proof/BASIN-ESCAPE-ANALYSIS.md:86-123`). Therefore, if a non-empty deep core remains and the branch has not yet crossed the bifurcation set, it is reasonable to expect a **restricted remnant theorem** of the form:

> sites sufficiently deep in the core continue to satisfy a shifted-threshold inclusion for sufficiently gentle perturbations,

provided the local interior margin still dominates the transported displacement on those sites.

This is not yet a proved theorem in full generality, but it is the correct direction for a local replacement theory.

---

## 5. Local Non-Persistence Principle

### 5.1. Statement

**Principle NP-NB (Local Non-Persistence Near Bifurcation).**

Let `u_t` lie on a branch of formation-structured local minimizers approaching a shape-transition parameter set. If along this branch
\[
\mu \to 0
\quad\text{and}\quad
\Delta_{\mathrm{bdy}} \to 0,
\]
then the full temporal-persistence package cannot remain uniformly valid. In particular, at sufficiently small spectral gap:

- the transported perturbation budget is no longer dominated by basin radius,
- the boundary layer becomes the first instability channel,
- exact-threshold persistence fails before shifted-threshold persistence,
- and the correct theory is one of **local restricted persistence plus bifurcation-sensitive failure**, not global persistence.

### 5.2. Why this is stronger than a heuristic

This principle is not merely intuitive. It synthesizes three independent internal results:

1. **boundary-dominated soft modes** (`docs/03-31/proof/BASIN-ESCAPE-ANALYSIS.md:86-123`),
2. **three-regime basin theorem** (`docs/03-31/proof/BASIN-ESCAPE-ANALYSIS.md:203-232`),
3. **explicit synthesis warning** that the theorem should exclude a neighborhood of bifurcation points (`docs/03-31/repair/PERSIST-SYNTHESIS.md:130`).

So the local non-persistence principle is a mathematically organized synthesis of what the repository already knows.

---

## 6. A Replacement Theorem Ladder

Near bifurcation, the correct theorem ladder is:

### Level 1 — no longer honest

- full persistence theorem with basin containment,
- universal `r >= const` statement,
- exact-threshold preservation on the whole core.

### Level 2 — still defensible locally

- branch-local continuation while the active-set-aware Hessian remains positive,
- shifted-threshold inclusion,
- deep-core remnant persistence on sites with positive local interior margin.

### Level 3 — bifurcation crossing

Once the branch actually crosses the bifurcation set (`μ = 0` in the relevant direction), the right description is no longer persistence but **branch selection / formation transition**.

This is where merge/split/birth/death theory begins.

---

## 7. Consequence for T-Persist Writing

The practical consequence is simple:

1. **Do not state a positive near-bifurcation persistence theorem.**
2. **Do state a restricted-persistence/local-non-persistence principle.**
3. **Treat bifurcation neighborhoods as an excluded or separately analyzed regime.**

This is fully consistent with the canonical status line:

- full temporal persistence remains conditional on `(NB)` away from shape transitions (`Canonical Spec v2.0.md:993-1001`),
- near-bifurcation persistence remains open (`plan/Plan_0331.md:46`).

---

## 8. Open Problems Created by the Local Theory

The restricted-persistence reformulation exposes three concrete next theorems:

1. **Directional basin theorem near bifurcation** — replacing isotropic radius by direction-dependent control;
2. **Deep-core remnant theorem** — proving shifted-threshold persistence on a locally protected subset;
3. **Bifurcation selection theorem** — describing which post-bifurcation branch is selected by transport + gradient flow.

These are the mathematically correct successors to the failed universal persistence claim.

---

## 9. Final Assessment

The correct near-bifurcation message is not:

> persistence theorem with weaker constants.

It is:

> **near bifurcation, full persistence ceases to be the right theorem shape**.  
> What remains is a local theory of branch continuation, deep-core remnants, shifted thresholds, and instability-driven branch change.

That is the mathematically honest way to continue Plan_0331 without silently overstating what the current proofs can bear.
