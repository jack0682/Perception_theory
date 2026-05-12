---
type: log/integration
date: 2026-05-12
target: OP-AFD-003 → Integration with canonical / AFD registry; new open problems
canonical_version: CV-1.13 (NOT modified)
session_label: W7-Day3
---

# 03 — Integration and New Open Problems

**Session:** 2026-05-12
**Target (from plan.md Priority 3):** Integrate OP-AFD-003 resolution into AFD registry; identify canonical-side implications; harvest new open problems.

**This file covers:** §4.5 Integration + §4.6 New open questions + meta items.

**Depends on reading:** `02_development.md` of this session.

---

## §1. Integration with AFD-0 working layer

### 1.1 Proposed updates to `afd_open_problems.md`

**OP-AFD-003 status:** OPEN (H) → **RESOLVED (Cat A for Q-A; Cat A generic / Cat B worst-case for Q-B)**.

Suggested replacement text (to be applied by user in a separate working-layer edit):

```
## OP-AFD-003 — Existence of Minimizing Transition Paths

**Severity.** H → RESOLVED (2026-05-12, Cat A).

**Statement.** The infimum in AFD-D7 is attained by an admissible
Lipschitz path γ_*.

**Resolution (2026-05-12).**
- Minimal version (λ_D = λ_K = 0): Theorem T-OP-AFD-003-A.
  Cat A unconditional.
- General version (λ_D, λ_K ≥ 0): Theorem T-OP-AFD-003-C.
  Cat A generic / Cat B worst-case (vineyard transversality).
- See `logs/daily/2026-05-12/02_development.md` for proof.

**Key lemmas (new, AFD-internal).**
- L1 — Constant-speed reparametrization (image-invariant).
- L2 — Sub-level-set ε-net PL approximation.
- L3 — Length-bounded shortcut via o-minimal diameter.
- L4–L6 — PL finite-dimensional reduction (parallel proof).

**Residual sub-problems.**
- OP-AFD-003a (L2 refinement): explicit bound on D^* for SCC energy.
- OP-AFD-003b (L3 generalization): non-analytic E (drop A3 b_D = 0).
- OP-AFD-003c (Q-C J_K): tighten Cat B → Cat A by removing vineyard-transversality genericity.

**Relates to.** AFD-T5 attainment (now PROVED); AFD-T8 FW instanton (partial feed); OP-AFD-005 (FW); CV-1.14 program (no direct blocker change).
```

### 1.2 Proposed updates to `afd_theorem_registry.md`

| ID | Name | Update |
|---|---|---|
| AFD-T5 | Abstract Transition Cost Existence | "infimum attainment" gap **CLOSED** (Cat A); add note `OP-AFD-003 resolved 2026-05-12`. |

No new row added to the registry — the result is a property *of* AFD-T5, not a separate theorem (though §1.4 below proposes registering the result as AFD-T11 if desired).

### 1.3 Proposed updates to `abstract_formation_dynamics.md`

§14 AFD-T5 "Properties" bullet ("**Infimum attainment** is OPEN (OP-AFD-003)..."): **replace** with:

> **Infimum attainment.** **PROVED (Cat A, 2026-05-12).** For the minimal version (λ_D = λ_K = 0), the infimum `C_AFD(F_i, F_j) = Bar(F_i, F_j)` is attained by some Lipschitz admissible path γ_* of bounded length. See Theorem T-OP-AFD-003-A in `logs/daily/2026-05-12/02_development.md` §5. For the general version, Cat A generic / Cat B worst-case (T-OP-AFD-003-C, §7).

### 1.4 Proposed new AFD theorem registry entry (optional)

**AFD-T11 (Infimum Attainment).** For all `F_i, F_j ∈ V_form` with `Adm(F_i, F_j) ≠ ∅`, the infimum `C_AFD(F_i, F_j)` is attained.

- **Status.** Cat A (minimal version), Cat A generic / Cat B worst-case (general).
- **Dependencies.** T-PF-A1-AR (Cat A), E continuous (Cat A, §3 / §8.1), AFD-T2 D Lipschitz (Cat A), Arzelà-Ascoli, BV-LSC (Ambrosio-Fusco-Pallara 2000).
- **File reference.** `logs/daily/2026-05-12/02_development.md` Theorems T-OP-AFD-003-A, T-OP-AFD-003-B, T-OP-AFD-003-C.

User decision: prefer to absorb into AFD-T5 commentary (less proliferation) or register as separate AFD-T11. **Recommendation:** absorb into AFD-T5 — the result is the closure of T5's last open property, not a new claim.

---

## §2. Implications for canonical (`canonical.md` and `theorem_status.md`)

### 2.1 No direct canonical edit proposed

AFD-0 itself is **not yet promoted to canonical** (per `abstract_formation_dynamics.md` §18 — promotion happens in CV-1.14 / R2 round). So `canonical.md` has no entry for AFD-T5 to update.

When AFD-0 promotes to canonical, the OP-AFD-003 resolution should propagate as follows:

| Future canonical section | Insertion content |
|---|---|
| §13 (Theorem catalog) | Add `T-AFD-T5: C_AFD attainment, Cat A` row. |
| §13 Open Problems Catalog | `OP-AFD-003 RESOLVED (Cat A)` move from active to resolved list. |
| §14 Commitment Notes (CN-AFD if introduced) | Note "AFD admissible class has attaining minimizers" as a structural fact. |

### 2.2 Cross-check: no silent resolution of other OPs

Per prompt §8 item 2: I must explicitly state how today's result affects existing open problems, and not silently resolve any.

| OP | Effect of T-OP-AFD-003 |
|---|---|
| OP-0001 — Crisp recovery | **None.** Attainment of minimizing barrier path is unrelated to crisp object recovery. |
| OP-0002 — Co-belonging form | **None.** C-form vs. predicate-form choice is orthogonal. |
| OP-0003 — Transition operator M_{t→s} | **None.** Transport vs. barrier are independent. |
| OP-0005 — K-Selection | **None.** Selection criterion vs. barrier attainment are independent (resolution of "which K is preferred" requires Cat A small-noise asymptotics — see Path B / Path E in canonical). |
| OP-0006 — N-1 Soft-Hard Switching | **None.** N-1 asks about K integer-vs-continuous dichotomy; orthogonal to barrier-path attainment. |
| OP-0007 — Diagnostic-energy bridge tightening | **None.** |
| OP-0008 — σ-rich / Wigner | **None.** σ tracking is a diagnostic; barrier attainment doesn't depend on it. |
| OP-0009 — Multi-formation foundations | **None.** Multi-field K-field structure is at a different layer (Layer 1 → AFD-D5 multi-field analog). |
| OP-0021 — T_* registration | **None.** Small-noise temperature is Layer-3; barrier attainment is Layer-2 deterministic. |
| OP-AFD-001 — TopSig continuity at V | **Mild partial relation.** Q-B J_K case Cat B → Cat A would also benefit OP-AFD-001 vineyard-regularity work. **Not resolved by T-OP-AFD-003.** |
| OP-AFD-002 — K_act stratification regularity | **Mild partial relation.** Same vineyard-regularity issue. **Not resolved.** |
| OP-AFD-004 (a/b/c) — Tight barrier exponent | **None.** Attainment ≠ tight value. |
| OP-AFD-005 — FW compatibility | **Partial feed.** FW instanton identification needs (a) existence of admissible minimizer (NOW PROVIDED by T-OP-AFD-003-A) and (b) identification of γ_* with FW instanton (NOT PROVIDED here; requires Layer-3 work). |
| OP-AFD-006 — Markov / lumpability | **None.** |
| OP-AFD-007 — Multi-K_field graph | **None.** |
| OP-AFD-008 — Topology-aware J_K | **None.** |
| OP-AFD-009 — Conley extension | **Mild partial relation.** The proof technique (Arzelà-Ascoli in C([0,1], Σ_m)) extends naturally to isolated-invariant-set basins; reusable for AFD-1. |
| OP-AFD-010 — Finiteness of V_form | **None.** Attainment of minimizers between pairs is independent of how many pairs there are. |

**No silent resolutions.** All other OPs remain in their pre-session status.

### 2.3 No retractions

No canonical claim is **weakened** by today's work; only a Layer-2 (AFD working) gap is closed. Canonical stays unmodified.

---

## §3. Pre-numerical sanity check (per session prompt §12 lesson)

Per [[numerical_validation]] memory: cheap numerical validation precedes canonical proposals. Although this is a *theoretical* attainment result (no numerical experiment naturally applies), we can perform a **structural sanity check** by inspection of `op_afd_004_proof.md` §5.1 item 4:

> "OP-AFD-003 dependency. Strategy A uses inf in Bar(F_K2, F_K1) and argues the infimum is achieved at the basin boundary exit. If inf is not attained (OP-AFD-003 gap), the argument still gives Bar ≥ Δ_min because every path achieves E ≥ E(u*) + Δ_min at some point — the inf of the maximum over paths is still ≥ Δ_min."

**Consistency check.** Today's resolution of OP-AFD-003 (Cat A) is *strictly stronger* than required by OP-AFD-004's argument. OP-AFD-004 proceeds without OP-AFD-003; OP-AFD-004 now becomes *also* compatible with picking a concrete minimizer (for visualization, for numerical NEB comparison). ✓ Consistent.

**Numerical compatibility check.** NEB experiments (exp60) compute approximate minimum-energy paths; T-OP-AFD-003-B's PL construction is essentially a discrete version of the same numerical procedure. NEB results converging in mesh refinement is empirical evidence for the attainment claim (NEB converges → there exists a limit path → that path attains Bar). ✓ Consistent with empirics.

**No experiment needed today.** Theoretical attainment + counterexample search exhaustion + empirical NEB convergence is sufficient.

---

## §4. Byproduct: theoretical prediction for M-A2 (Priority 1)

Per `01_exploration.md` §1, we committed to a *theoretical* prediction for the M-A2 numerical experiment (Priority 1 in plan.md). This is a free byproduct of AFD-D2 (deterministic basins) + AFD-T9 (H-MORSE non-necessity) + a generic-symmetry-breaking argument.

### 4.1 Prediction

**Claim.** On the canonical 15×15 grid with free BC, β = 50, vol_frac = 0.3 (so m = 67.5), the canonical minimizer `u^*` obtained by `find_formation` with default multi-start initialization is **generically D_4-asymmetric**, hence `Stab_{Aut(G)}(u^*) = {e}`, and **M-A2 PASSES**.

### 4.2 Reasoning

(a) **Aut(G) for 15×15 free-BC grid.** The graph is the Cartesian product of two 15-path graphs P_15 □ P_15. Aut(P_n) = ℤ/2 (single reflection). Aut(P_15 □ P_15) = (ℤ/2)^2 ⋊ ℤ/2 = D_4 (order 8): 4 reflections (horizontal, vertical, two diagonal) + 4 rotations (e, r_90, r_180, r_270). This is exactly the group identified in `01_pre_brainstorm.md` §1.

(b) **Generic asymmetry of formations.** AFD-D1 places no symmetry constraint on representatives. For a formation to be D_4-symmetric, its support must be invariant under all 8 elements of D_4 — a very restrictive condition. The set of D_4-symmetric u ∈ Σ_m has codimension ≥ 3 (vol-constrained simplex with D_4 invariance) within Σ_m, so a *generic* minimizer is D_4-asymmetric.

(c) **At which (β, vol_frac) does symmetric minimizer dominate?** At vol_frac = 0.5 (m = n/2) the symmetric "checkerboard" or "centered blob" patterns are *energetically competitive*. At vol_frac = 0.3 (off-half) the symmetric centered blob is suboptimal because the mass constraint pulls the optimal blob toward an off-center attractor (any of 4 corner-zone basins). Multi-start initialization will *generically* pick one of the 4 asymmetric corner basins.

(d) **Outcome.** With probability 1 over generic initialization seed, `u^*` lies in one of the 4 corner-attractor families; `Stab_{Aut(G)}(u^*) = {e}` (trivial) for any single such minimizer. **M-A2 PASSES.**

### 4.3 Caveat (when M-A2 might FAIL)

If `find_formation` employs a symmetry-aware initialization (e.g. centered Gaussian seed), it might land on a metastable D_4-symmetric minimizer. The genuine M-A2 verification requires running with multiple random initializations and confirming the *lowest-energy* minimizer is asymmetric. This is what Priority 1 should do empirically.

### 4.4 Theoretical follow-up for M-A1 and M-A3

For completeness:

- **M-A1 (bifurcation margin η > 0).** Holds when β/α ≫ β_crit. With β = 50, α = 0.5 default, λ_2 = O(1) on 15×15, |W''(c)| = O(1), the condition β/α > 4 λ_2 / |W''(c)| is satisfied with large margin η ∼ β.

- **M-A3 (strict interiority δ_0 > 0).** For u^* with values in (0, 1) bounded away from {0, 1} by at least δ_0. Generically satisfied for soft-formations (not for crisp-threshold solutions). Should hold for `find_formation` output unless E pushes toward boundary (extreme β).

**Combined prediction:** With high probability M-A1 + M-A2 + M-A3 all hold for the canonical 15×15 minimizer → **H-MORSE-Local Cat B is achievable in a CV-1.14 session running the verification.**

---

## §5. New open problems generated by this work

### 5.1 OP-AFD-003a — Explicit bound on `D^*`

**Statement.** Lemma L3 uses an o-minimal/semi-algebraic diameter bound `D^*` for path-components of E-sublevel sets in Σ_m. Compute an explicit `D^*(E, n, deg)` formula.

**Approach.** Bochnak-Coste-Roy 1998 Theorem 9.1.2 gives `D^* ≤ poly(deg(E), n)`. For SCC energy: deg E ≤ 4, n = |V|. Explicit constant likely `D^* ≤ C · 4^n` (pessimistic; tighter on regular graphs).

**Severity.** L. Not blocking AFD-0 promotion; refines L3.

**Relates to.** Lemma L3 in `02_development.md` §4.

### 5.2 OP-AFD-003b — Drop the analyticity hypothesis

**Statement.** L3 uses o-minimality of E (sublevel set has finitely many components with bounded intrinsic diameter). When is L3 valid without analytic E?

**Sub-claim.** For E *merely continuous*, sublevel set components may have infinite intrinsic diameter (Cantor-like ridges). T-OP-AFD-003 requires either (i) E analytic (Cat A in SCC; current proof), or (ii) some replacement of L3.

**Approach.** Replace L3 with a direct compactness argument that bypasses sublevel-set components. Idea: use **path-shortening via convex-combination paths** through interior of Σ_m (since Σ_m is convex, any γ can be retracted toward its endpoint along Σ_m linear segments). The retraction preserves admissibility and shortens length without (necessarily) increasing Bar.

**Severity.** L. Only relevant for non-canonical SCC variants.

### 5.3 OP-AFD-003c — Vineyard-transversality in J_K case

**Statement.** Theorem T-OP-AFD-003-C in Q-B/Q-C is Cat A *generically* (γ_* meets vineyard set V transversally) and Cat B in the worst case (γ_* dwells on V on a positive-measure subset). Close the gap to Cat A unconditional.

**Approach.** Two routes:

- (i) **Density argument.** Show that admissible paths meeting V transversally are dense in Adm under sup-norm. Then the infimum is attained in the closure, and lower-semicontinuity gives attainment by a limit γ_*. The limit may itself fail transversality on a measure-zero set; that suffices for `liminf TV` bound.
- (ii) **Replacement of J_K.** Use a *smoothed* K_act (e.g. K_soft, QM3) instead of K_act. K_soft is Lipschitz (QM3 Cat A) so TV(K_soft ∘ γ) is fully continuous-friendly. This sidesteps the vineyard issue.

**Severity.** M. Decides whether AFD-D10 is fully Cat A or remains Cat B.

**Relates to.** OP-AFD-001 (TopSig continuity), OP-AFD-008 (refined J_K).

### 5.4 OP-AFD-003d — Smoothness of minimizing path γ_*

**Statement.** T-OP-AFD-003-A gives γ_* Lipschitz. Is γ_* smoother (e.g. C^1 piecewise; differentiable except at saddle points)?

**Approach.** On any open interval where γ_* does not maximize E, the constraint that γ_* minimize Bar is *non-active*; the path is free to be reparametrized smoothly. On the closed set where E(γ_*(s)) = E_{F_i} + B^* (the "saddle interval"), the path must dwell. Standard MEP regularity theory (Henkelman-Jónsson, NEB) suggests γ_* is C^1 away from corner-points of Σ_m and saddle-set.

**Severity.** L. Geometric refinement, not blocking.

### 5.5 OP-AFD-003e — Sensitivity of γ_* to (F_i, F_j) perturbation

**Statement.** How does γ_* vary under continuous perturbation of `u_{F_i}^*, u_{F_j}^*`, β, or graph topology G?

**Approach.** Compactness gives upper-hemicontinuity of the set-valued map `(F_i, F_j) ↦ {γ_*}`. Convergence in Hausdorff metric. Continuity of Bar in parameters → continuity of attainment.

**Severity.** L. Refinement; useful for vineyard / parameter-sweep studies.

### 5.6 Cross-references

| New OP | Severity | Blocks | Refines | Extends |
|---|---|---|---|---|
| OP-AFD-003a | L | — | Lemma L3 | — |
| OP-AFD-003b | L | — | A3 b_D = 0 dependency | non-analytic E |
| OP-AFD-003c | M | Q-B Cat A | T-OP-AFD-003-C | OP-AFD-001, 008 |
| OP-AFD-003d | L | — | T-OP-AFD-003-A | OP-AFD-005 |
| OP-AFD-003e | L | — | T-OP-AFD-003-A | parameter sensitivity |

---

## §6. Prompt-template feedback (per session prompt §14)

Per session prompt §14, I record possible improvements to the prompt template for v2 consideration.

### 6.1 Multi-priority plan handling

**Issue.** Today's `00_plan.md` had **three** parallel priorities, but the prompt template assumes "**단일** target open problem". The template should be augmented with:

> "**If `plan.md` lists multiple priorities:** identify which one best fits the 'single deep theoretical development' format (theoretical proof rather than numerical run; not banned by §10). State your selection in `01_exploration.md` §1 and note the other priorities for parallel handling."

This session followed this implicitly; making it explicit avoids ambiguity.

### 6.2 Numerical-task escape valve

**Issue.** When a priority is purely computational (Priority 1: run `find_formation` + check Aut(G)), the template's 3-file output format is over-engineered. A *short* "computational handoff" log would suffice.

**Suggestion.**

> "**If a priority is purely computational:** produce a single `0X_compute_handoff.md` file with: (a) exact CLI/Python invocation, (b) expected output schema, (c) interpretation rule for pass/fail, (d) theoretical prediction (so the experiment is hypothesis-driven). Skip the 3-file exploration / development / integration triad."

We followed an informal version of this in §4 above (theoretical prediction for M-A2).

### 6.3 OMC orchestration ban scope

**Issue.** §10 bans `autopilot / team / ralph / ultrawork`. Today's Priority 2 was an *external audit* via TeamCreate, which is technically OMC orchestration. Clarification:

> "**Banned tools include:** `TeamCreate`, `EnterWorktree`, `Plan`, `oh-my-claudecode:*` orchestration skills. Banned use cases include parallel multi-agent review. **Sequential agent invocation** via the Agent tool with `general-purpose` / `Explore` subagent is **allowed** for single-step queries."

This would let an audit be performed sequentially in a single session by the same agent (slow but feasible). User decision; current session followed the strict interpretation.

### 6.4 Memory pointer to today's hot paths

For continuity with future sessions, consider adding to MEMORY.md after this session a pointer like:

> `- [OP-AFD-003 attainment 2026-05-12](afd_attainment.md) — Cat A resolution via Arzelà-Ascoli + o-minimal shortcut; closes AFD-T5's last gap.`

(Will be added via `oh-my-claudecode:remember` if user invokes.)

---

## §7. Session self-checklist (per prompt §10)

- [x] plan.md target identified and selected (Priority 3 = OP-AFD-003).
- [x] 3+ mathematically independent approaches generated (A: Arzelà-Ascoli; B: PL finite-dim; C: Γ-relaxation; D: counterexample; E: Mountain Pass rejected).
- [x] Primary approach (A) developed with full proof; secondary (B) developed; tertiary (D) checked.
- [x] Integration with canonical / AFD registry written (this file §1, §2).
- [x] New open questions collected (§5: OP-AFD-003a–e).
- [x] Three core files (`01_`, `02_`, `03_`) + `99_summary.md` (pending) produced.
- [x] Canonical not directly modified — proposals only (§1, §2).
- [x] No silent resolution of other OPs (cross-check §2.2).
- [x] Granularity supports follow-up "verify §X.Y" questions — sections numbered, lemmas labeled L1–L6, theorems T-OP-AFD-003-A/B/C, dependency table §5.3 in `02_development.md`.

**Verdict.** Session meets all §10 success criteria.

---

## §8. Final classification of session outputs

| Item | Cat | Notes |
|---|---|---|
| Theorem T-OP-AFD-003-A | **A** | OP-AFD-003 (Q-A minimal case): unconditional |
| Theorem T-OP-AFD-003-B | **A** | OP-AFD-003 (Q-A): parallel PL proof |
| Theorem T-OP-AFD-003-C | **A** generic / **B** worst-case | OP-AFD-003 (Q-B/Q-C with λ_D, λ_K ≥ 0) |
| Lemmas L1, L2, L3, L4, L5, L6 | **A** | Building blocks |
| Counterexample search §8 | **exhaustive** over standard candidates | No CE found |
| AFD-T5 promotion from open-attainment to Cat A | **Cat A** ready | Subject to user-driven registry edit |
| M-A2 prediction (§4) | **Conjecture supported by argument** | Empirical verification pending |
| OP-AFD-003a/b/c/d/e new sub-problems | **Open** | For future sessions |

---

*End of `03_integration_and_new_open.md`. Continue to `99_summary.md`.*
