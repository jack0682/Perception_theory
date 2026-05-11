---
type: working/afd
status: AFD-0 Draft (2026-05-12)
---

# AFD-0 Honesty Audit

20-question audit applied to AFD-0 (Draft v0.1). Each question is answered honestly with the specific definition / theorem reference and any caveats. Overclaim corrections are summarized at the bottom.

---

## 1. Does any AFD definition secretly require Morse nondegeneracy?

**No.** This is the central content of AFD-T9 (Theorem, proved by inspection). All of AFD-D1..D15 and AFD-T1..T7 are checked case-by-case in the proof.

## 2. Does any AFD transition cost require a unique saddle?

**No.** `C_AFD` is defined as an infimum over the entire admissible class Adm(F_i, F_j) (AFD-D7). No saddle uniqueness or even saddle existence is assumed at Layer 2. Layer 3 (AFD-T8) does require a saddle path for the EK prefactor, but that is a Layer-3 hypothesis.

## 3. Does the formation graph require exact rates?

**No.** G_form is built from C_AFD (a cost, not a rate). Rates appear only at Layer 3 (AFD-D15, AFD-T8) and are *not used* to define the graph.

## 4. Does K_act have a stable definition?

**Yes.** Commitment 16 (Cat A, canonical.md §11.1) fixes K_act as `#PersComp` at threshold `ε = 0.01 · m̄` with `m̄ = M / K_field`. The standard regime is documented (T^2_{20}, M = 90, K_field = 4 ⇒ m̄ = 22.5, ε = 0.225). This is the single canonical convention used in AFD-0.

## 5. Is K_act continuous?

**No.** K_act is integer-valued and is generically locally constant on `Σ_m^◦ \ V`, where V ⊂ Σ_m is the vineyard set. K_act has discontinuities precisely on V. K-jumps are vineyard crossings (AFD-D13). V is codimension-1 in Σ_m (semi-algebraic).

## 6. Is S_K really a stratum?

**No.** S_K = {u : K_act(u) = K} is **only a set-theoretic level set** of an integer-valued function. AFD-0 does not prove S_K is a smooth manifold and does not prove S_K is a Whitney stratum. The warning is given verbatim in AFD-D12 and AFD-T3. The terminology "stratum" is used in the loose set-theoretic sense only. Upgrading to a genuine stratification is OP-AFD-002.

## 7. Is D continuous?

**Yes.** AFD-T2 proves D = (Bind, Sep, Inside, Persist) is Lipschitz from (Σ_m, ‖·‖_2) to ([0,1]^4, ‖·‖_∞).

**Caveat.** Inside(u) uses the H_0 persistence diagram, which is continuous in bottleneck distance (CSEH 2007) but whose *bar-assignment* is discontinuous on the vineyard set V. The Inside *value* remains continuous; only the bar-indexing is non-continuous on V. K_soft itself is Lipschitz (QM3, Cat A) and Inside is built from the same machinery.

## 8. Is τ stable?

**Yes.** Bottleneck stability `d_B(τ(u), τ(v)) ≤ ‖u − v‖_∞` is the Cohen-Steiner-Edelsbrunner-Harer 2007 theorem (accepted external; cited at AFD-D11 and in `working/E/soft_K_definition.md` §2.1).

## 9. Are bottleneck / Wasserstein distances justified?

- **Bottleneck d_B**: yes, fully justified by CSEH 2007.
- **Wasserstein W_2**: justified on finite persistence diagrams (always the case here, since X_t is finite); stability constants differ from d_B (CSEH 2010 for the Wasserstein version). AFD-0 defaults to d_B; W_2 is offered as an alternative.

## 10. Is C_AFD symmetric?

**No.** Bar(γ, F_i) is asymmetric (different reference energy E_F_i vs E_F_j). C_AFD is therefore asymmetric in general. A symmetric variant Bar_sym is defined in AFD-D8 but is not used for the FW / EK identification.

## 11. Is C_AFD a metric?

**No.** Explicit warning in AFD-T5 properties block:

- **Symmetry**: fails.
- **Triangle inequality**: fails in general (max-along-path does not concatenate additively).

C_AFD is a *cost*, not a metric. It is the edge weight of a weighted directed graph.

## 12. Does the barrier preorder satisfy transitivity?

- **ExitCost-based ≼_bar (AFD-D14)**: yes. AFD-T6 proves it is a total preorder (reflexive, transitive, total). It is not antisymmetric (ties allowed).
- **Pairwise C_AFD(F_i, F_j) ⋚ C_AFD(F_j, F_i)**: **no**. This pairwise comparison is not a preorder in general — explicit warning in AFD-D14 and AFD-T6. Use only the exit-cost scalar version.

## 13. Does the theory confuse basin / attractor / minimizer / Conley index?

**Checked, no confusion.**

- AFD-D1 = local minimizer of E on Σ_m (the *representative* of a formation).
- AFD-D2 = deterministic basin of attraction = set of u that flow to u_F^* under constrained gradient flow. Well-defined by T14.
- Conley index = optional refinement in §12 / AFD-T10 (Design Principle), not used as a default in AFD-0.
- "Attractor" in the dynamical-systems sense is not used as a primitive; the basin AFD-D2 is the closest analogue.

## 14. AFD-0 deterministic or stochastic?

**Deterministic by default (AFD-D2).** Stochastic basin is provided as an optional variant AFD-D2' for compatibility with FW / EK in §11 / §13. The choice is *named* in AFD-D3 (`B_F = B_det` or `B_stoch`).

## 15. AFD-0 reduces to FW in the small-noise limit?

**Yes.** §11 documents the reduction:

- FW quasipotential `V(u_F_i^*, u_F_j^*)` = AFD barrier `Bar(F_i, F_j)` for gradient SDEs.
- T-PF-A1-SDE provides the well-posed reflected Langevin dynamics.
- AFD-T8 is the small-noise asymptotic statement.

This identification does not require H-MORSE. (H-MORSE adds the *prefactor*, not the *exponent*.)

## 16. Does EK refine AFD or replace it?

**Refines.** AFD provides the exponent (Bar). EK provides the prefactor (A_ij from Hessian determinants). Together, AFD + EK = exact rate. This is the central canonical statement of §13 (Slogan 1) and AFD-D15.

## 17. Is temporal persistence overclaimed?

**No.** T-Temporal-Identity is **Cat A** (CV-1.13, sealed W7-CV1.13 2026-05-10), all 4 parts. AFD-0 uses temporal identity only as a compatibility property of the formation state τ component under the transport kernel R_{t → s}; this is exactly what CV-1.13 provides. No overclaim.

## 18. Are multi-formation claims honest?

**Yes.** K_act is Cat A (Commitment 16). K_field is the architectural cap. AFD-0 default treats single representatives; multi-formation (K_field > 1) extension is explicitly carried as OP-AFD-007. No claim about K-field dynamics is made at AFD-0 level beyond what Commitment 16 + Pkg I gives.

## 19. Are categorical ideas overused?

**Not used in AFD-0.** No functors, no enriched categories, no operads, no infinity-categories. G_form is a plain weighted directed graph. The "formation-state graph" is a graph in the elementary combinatorial sense. Categorical reformulations are deferred to future work (not even listed as an OP).

## 20. Is every theorem correctly labeled?

**Yes.** Labels in `afd_theorem_registry.md`:

| ID | Label |
|---|---|
| AFD-T1 | Proposition |
| AFD-T2 | Theorem |
| AFD-T3 | Proposition |
| AFD-T4 | Proposition |
| AFD-T5 | Theorem |
| AFD-T6 | Proposition |
| AFD-T7 | Proposition |
| AFD-T8 | Lemma Candidate (Conditional, Layer 3) |
| AFD-T9 | Theorem |
| AFD-T10 | Design Principle |

Theorem is used only where the statement is substantive (AFD-T2 assembles Cat A facts to a global Lipschitz claim; AFD-T5 combines compactness + continuity + Lipschitz; AFD-T9 is the central H-MORSE-non-necessity claim with by-inspection proof). All others are correctly labeled as Proposition / Lemma Candidate / Design Principle.

---

## Overclaims identified and corrected

| Tempting overclaim | Correction in AFD-0 |
|---|---|
| "C_AFD is a metric on V_form." | **Removed.** C_AFD is asymmetric and may fail the triangle inequality. It is a cost, not a metric. (AFD-T5 properties.) |
| "K-strata S_K are smooth manifolds." | **Removed.** S_K is only a set-theoretic level set. Whitney/smooth structure is OP-AFD-002. (AFD-D12 warning, AFD-T3 warning.) |
| "Barrier preorder is antisymmetric." | **Removed.** Only a total preorder. Ties are explicitly allowed. (AFD-T6.) |
| "EK rate is identified with C_AFD." | **Refined.** Only the *exponent* (Bar) matches. The prefactor A_ij is Layer 3. (AFD-D15, AFD-T8.) |
| "AFD replaces EK." | **Refined.** EK refines AFD. (§13 slogan 1, AFD-D15.) |
| "K-jumps are Morse saddle crossings." | **Refined.** A K-jump is a vineyard crossing of γ, not necessarily a Morse saddle event. The two coincide only under additional regularity. (§13 slogan 3, AFD-D13 comment.) |
| "AFD-T8 is a Theorem." | **Refined.** AFD-T8 is a Lemma Candidate (Conditional) under Layer-3 hypotheses. Full proof is OP-AFD-005. |
| "V_form is finite." | **Held.** Finiteness is not claimed; OP-AFD-010 records it as a genuine open problem. |
| "Infimum in AFD-D7 is attained." | **Held.** Attainment is OP-AFD-003; AFD-T5 only claims finiteness of the inf, not attainment. |
| "S_K is a Whitney stratum." | **Removed.** Same as the second row. |
| "AFD provides a Markov chain on V_form." | **Held.** Markov / lumpability is OP-AFD-006. AFD-0 provides only a graph + cost, not a Markov chain. |

---

## Audit conclusion

AFD-0 (Draft v0.1) passes the 20-question audit with:

- 1 central Theorem (AFD-T9) carrying the H-MORSE reclassification, proved by inspection — no gaps.
- 2 assembly Theorems (AFD-T2, AFD-T5) building on Cat A inputs — minor bookkeeping gaps (exact Lipschitz constants; J_K bound).
- 1 Lemma Candidate (AFD-T8) explicitly labeled Conditional and tied to Layer 3 — no overclaim.
- 6 Propositions with short proofs from Cat A inputs.
- 1 Design Principle (AFD-T10) explicitly labeled as such.
- 10 Open Problems clearly carried (OP-AFD-001..010).

No definition or theorem is hidden-dependent on H-MORSE. No claim is mislabeled. The four canonical slogans of §13 are stated verbatim and consistent with the formal results.

Recommendation: AFD-0 is ready for one round of external audit before any canonical promotion. Promotion candidates (AFD-T9, AFD-D1..D5, AFD-T1, AFD-T6, AFD-T3) are listed in the main document §18.
