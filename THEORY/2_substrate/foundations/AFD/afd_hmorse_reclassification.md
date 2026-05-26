---
type: working/afd
status: AFD-0 Draft (2026-05-12)
---

> [!nav] Linked: [[MOC_AFD_0_foundation]] · [[THEORY_INDEX]]


# H-MORSE Reclassification: Layer 3 Regularity, Not Layer 2 Foundation

**Formal claim.** `H-MORSE ∈ Layer 3.   H-MORSE ∉ Layer 2.`

---

## 1. What H-MORSE is

H-MORSE = the hypothesis that the SCC energy `E` is **Morse-nondegenerate on the constraint** `Σ_m` at every critical point relevant for Eyring-Kramers.

It has two sub-hypotheses (separated in `CV114_H_MORSE_PACKAGEII/`):

- **H-MORSE-Local.** At every local minimizer `u_min` of E on Σ_m, the projected Hessian `Π_T H_E(u_min) Π_T` on the tangent space `T_{u_min} Σ_m = 1^⊥` is strictly positive definite (no zero eigenvalues).
- **H-MORSE-Saddle.** At every index-1 saddle `u_sad` of E on Σ_m, the projected Hessian `Π_T H_E(u_sad) Π_T` has exactly one strictly negative eigenvalue and no zero eigenvalues.

**History.** H-MORSE was formulated in W6 D6 (2026-05-06 Session H) as the regularity prerequisite for the EK prefactor (`A_ij = (|λ^−|/2π) sqrt(|det H_sad^proj|/det H_min^proj)`). It was originally proposed as a working hypothesis for the entire Package II programme.

**Current Cat status (2026-05-12).**

- H-MORSE-Local: **Cat B target** (CV-1.14), Hessian-positivity arguments in progress in `working/CV114_H_MORSE_PACKAGEII/03_energy_landscape_and_hessian.md`. Counterexamples catalogued in `04_degeneracy_catalogue.md` (Goldstone, D_4 symmetry, T8-Full bifurcation).
- H-MORSE-Saddle: **not yet registered** as a Cat target; requires saddle-existence theorem first.

---

## 2. What H-MORSE provides (Layer 3 only)

H-MORSE supplies exactly the Hessian-determinant data needed for the **Eyring-Kramers prefactor**:

> `A_ij = (|λ^−_sad| / 2π) · sqrt( |det Π_T H_E(u_sad) Π_T|_{1^⊥} / det Π_T H_E(u_F_i^*) Π_T|_{1^⊥} )`

This prefactor multiplies the exponential `exp(−Bar/T_*)` to give the asymptotically exact rate

> `r_ij = A_ij · exp(−Bar(F_i, F_j) / T_*) · (1 + O(T_*))`.

Without H-MORSE the prefactor is ill-defined (degenerate determinants), so exact EK rates are not available. **But:** the exponential `Bar(F_i, F_j)` is well-defined regardless of H-MORSE, and the rate *ordering* is governed entirely by Bar.

H-MORSE also supplies the technical conditions needed for the FW instanton uniqueness and saddle-path geometry inside the standard EK proof. The reflected-boundary correction (Bovier-Eckhoff 2003) is an additional Layer-3 component.

---

## 3. What AFD-0 needs (Layer 2)

AFD-0 needs the following Layer-1 facts (all Cat A):

| Need | Source |
|---|---|
| Existence of local minimizer u_F^* | T8-Core |
| Basin B_det(F) well-defined | T14 Lojasiewicz |
| K_act integer-valued, locally constant off V | Commitment 16, D-ST-3 |
| K_soft Lipschitz | QM3 |
| Diagnostic D = (Bind, Sep, Inside, Persist) Lipschitz | Predicate-Energy Bridge + A3 + QM3 + CSEH 2007 |
| Energy E continuous on compact Σ_m | canonical §8.1 |
| Reflected Langevin dynamics (for AFD-D2', §11) | T-PF-A1-SDE/GI/PE |

**Crucially:** *none of these require nondegenerate Hessians at minima or saddles.* AFD-T9 is the formal statement and inspection-level proof of this independence.

AFD-0 needs:

- Local minima (existence). T8-Core, no Hessian assumption.
- Energy values at minima and along paths. Continuity, no Hessian.
- Gradient-flow basins. T14 (Łojasiewicz), works for any analytic E on Σ_m.
- Persistence-diagram topology of u. CSEH 2007 + QM3, no Hessian.
- Integer K_act with vineyard set V codim-1. Commitment 16 + persistence machinery.

AFD-0 does **not** need:

- Determinant of any Hessian.
- Index-1 classification of saddles.
- Uniqueness of saddle paths.
- Spectral gap of any Hessian.
- T_* → 0 small-noise limit (used only in AFD-T8 / AFD-D15 / §11 / §13).

This independence is the structural reason H-MORSE belongs to Layer 3.

---

## 4. Formal statement

> **H-MORSE ∈ Layer 3. H-MORSE ∉ Layer 2.**

Reading: H-MORSE is a hypothesis used by Layer-3 quantitative-rate theory (Eyring-Kramers, exact prefactor). It is *not* a hypothesis used by Layer-2 abstract dynamics (AFD-0). Layer-2 results AFD-T1..T7 + AFD-T9 hold *unconditionally on H-MORSE*; only AFD-T8 / AFD-D15 (the Layer-3 interface) require it.

Equivalent operational statement:

- If H-MORSE-Local + H-MORSE-Saddle hold, AFD-0 results are unchanged; Layer 3 additionally yields exact EK rates.
- If H-MORSE-Local fails (e.g. Goldstone family, D_4-symmetric minimizers), AFD-0 results are unchanged; Layer 3 is unavailable for the affected formations.
- AFD-0 therefore "fails gracefully" in degenerate cases (AFD-T10 Design Principle).

---

## 5. CV-1.14 implications

CV-1.14 is the canonical-version target for H-MORSE-Local **Cat B promotion**. AFD-0 is **compatible** with CV-1.14 in the following sense:

- AFD-0 can be promoted (in part) to canonical *independently* of CV-1.14, since AFD-0 does not use H-MORSE.
- CV-1.14 + AFD-0 together enable AFD-T8 / AFD-D15 (the EK refinement compatibility statement).
- A future Layer-3 canonical addition would state: under CV-1.14 H-MORSE-Local + a future H-MORSE-Saddle result, AFD-T8 promotes from Lemma Candidate to Theorem.

**Parallel-development recommendation.** AFD-0 promotion (Layer 2) and CV-1.14 promotion (Layer 3 prerequisite) can proceed in parallel; neither blocks the other.

---

## 6. Cross-reference to AFD-T9

The formal claim "H-MORSE ∉ Layer 2" is the corollary of **AFD-T9 (H-MORSE Non-Necessity for AFD)** in `abstract_formation_dynamics.md` §14:

> AFD-D1..D15 and AFD-T1..T7 do not use:
> (a) Nondegeneracy of the Hessian at any critical point,
> (b) Existence of index-1 saddle points,
> (c) Hessian determinants,
> (d) Morse-type genericity conditions.

The proof is by inspection of each definition and theorem. AFD-T9 is the central architectural commitment of AFD-0 and is the formally proved version of the reclassification claim of this document.

---

## 7. Practical consequences

1. **Promotion order.** AFD-0 (Layer 2) can be promoted to canonical *before* H-MORSE-Local achieves Cat B/A. The promotion targets in `abstract_formation_dynamics.md` §18 (AFD-T9, AFD-D1..D5, AFD-T1, AFD-T6, AFD-T3) are all H-MORSE-free.

2. **Counterexamples are fine.** The degeneracy catalogue in `CV114_H_MORSE_PACKAGEII/04_degeneracy_catalogue.md` (Goldstone families, D_4 symmetric minimizers, T8-Full threshold) does not threaten AFD-0. It threatens only the Layer-3 prefactor.

3. **Statement of progress.** Progress on AFD-0 should *not* be reported as progress on H-MORSE, and progress on H-MORSE-Local should *not* be reported as a prerequisite for any AFD-0 result other than AFD-T8.

4. **Communication.** When discussing formation dynamics with collaborators or external auditors, AFD-0 should be presented as the *primary* dynamics layer. H-MORSE / EK is the *refinement* layer. This inversion of presentation order (relative to the historical W6–W7 trajectory, which emphasized EK first) is the architectural correction AFD-0 enacts.

---

## 8. Summary

| Aspect | Layer 1 (SCC Core) | Layer 2 (AFD-0) | Layer 3 (EK / Pkg II) |
|---|---|---|---|
| Field u, energy E | provides | uses | uses |
| Local minimizers | provides (T8-Core) | uses | uses |
| Basin (deterministic) | (via T14) | provides | uses |
| Diagnostic vector D | provides | uses (Lipschitz) | uses |
| K_act, K-strata | provides | uses | uses |
| Persistence τ | provides | uses (CSEH) | uses |
| Barrier Bar(F_i, F_j) | (energy) | provides | uses (exponent) |
| EK prefactor A_ij | — | — | provides |
| H-MORSE-Local | — | — | **requires** |
| H-MORSE-Saddle | — | — | **requires** |
| Exact rate r_ij | — | — | provides (asymptotic) |

**The fundamental rearrangement enacted by AFD-0:** H-MORSE drops from "foundational hypothesis of formation dynamics" to "regularity hypothesis of the rate-refinement layer." Everything that can be done without H-MORSE is consolidated at Layer 2. Layer 3 receives only the H-MORSE-dependent fragments.

This is the AFD-0 reclassification.
