# 20_canonical_proposals_F10_F11.md — Canonical Proposal Drafts: V5b-T' + σ_multi A⊕D

**Session:** 2026-04-28 (W5 Day 2 Phase 4, F10 + F11).
**Target:** Draft canonical §13 entry text for **V5b-T'** (NQ-206) AND canonical §11.1 Commitment 14-Multi extension for **σ_multi A⊕D combined invariant** (NQ-208). User-decision-ready form.
**Resolves:** Phase 4 NQ-206 (V5b-T' canonical) + NQ-208 (combined invariant canonical).
**Depends on reading:** `11_PN_unification.md` §3.1 (V5b-T' new finding); `12_D_to_A_reduction.md` + `19_*` §2 (Theorem 2.1 formal); `06_approach_AB_equivalence_and_D.md` §3 (Approach D framework).
**Status:** Draft canonical text ready for user review. NOT applied (per meta-prompt §8.1 hard constraint).

---

## Part 1: F10 — V5b-T' Canonical Entry Proposal

### §1.1 Proposed §13 entry placement

Insert AFTER existing T-V5b-T entry (canonical line 1117-1167), as a sister theorem.

### §1.2 Proposed text

```
**T-V5b-T'. Pre-Objective Goldstone on Translation-Invariant Graphs in Corner-Saturated Regime.** *(New, 2026-04-28, W5 Day 2 Phase 3.)*

Let G be a finite translation-invariant graph (torus T^d, cycle C_n, or d-fold lattice with periodic boundary conditions). Let u_t : X → [0,1] be a cohesion field subject to volume constraint Σu = m with c = m/n < c_s = (3-√3)/6 ≈ 0.211 (below-spinodal volume fraction). Let β > 1/a² (sub-lattice regime, ξ_0 = √(α/β) < a). Let u* ∈ Σ_m be an F=1 single-cluster minimizer of pure E_bd from a localized initial condition.

**Statement:** Under (β > 1/a², c < c_s, IC localized per Definition T-Corner-Cond-IC):
(V5b-T'-a) **Corner saturation**: u*(x) = 1 on a connected cluster S ⊂ X with |S| ≈ m sites; u*(x) = 0 on most of X \ S; u*(x) ∈ (0, 1) only on a thin transition layer of size O(perimeter of S).
(V5b-T'-b) **Goldstone of saturated cluster**: the lowest non-tangent Hessian mode is an approximate translation Goldstone of the saturated cluster S. Its eigenvalue is PN-barrier-lifted from zero by the cluster boundary's interaction with the discrete lattice.
(V5b-T'-c) **PN-barrier-lifted eigenvalue formula** (per `11_PN_unification.md` §4.1):
    μ_Gold^lifted ≈ A_R3b · β · (cluster perimeter)/ξ_0 (regime R3b)
    Empirically: O(β) magnitude (not exponentially small).
(V5b-T'-d) **Mode-mixing with cluster-boundary modes**: lowest eigenvector hybridizes translation Goldstone with cluster-boundary spectral modes; full-space overlap < 0.9 (sub-super-lattice signature).

*Status:* **Cat B target** for the corner-saturation existence claim (numerical anchor: NQ-173 + E10). Cat A path = analytic PN-barrier-lifted Goldstone formula (NQ-198 W6+).

*Numerical confirmation* (NQ-173, E10, F5):
- 2D torus L=20, c=0.10, β=4.0 (ζ=0.5): u_max = 1.000 corner-saturation observed. Goldstone eigenvalue ≈ 4-5. Mode-mixing α²+β² < 0.95 confirmed.
- ζ = 0.42 → 0.43 transition reveals R3a (smooth) → R3b (corner-saturated) regime change at fixed (L, c).

*Distinct from V5b-T*: V5b-T characterizes super-lattice (ξ_0 ≫ a) on translation-invariant graph; smooth interior minimizer; Goldstone exponentially suppressed. V5b-T' characterizes sub-lattice (ξ_0 < a) on translation-invariant graph; corner-saturated minimizer; Goldstone PN-barrier-lifted to O(β). 

*Distinct from V5b-F*: V5b-F characterizes corner-saturation on translation-broken graph (graph boundary); cluster pushed against graph boundary. V5b-T' is the analog on translation-invariant graph; cluster boundary is purely the saturation-set boundary, not graph boundary.

*Iteration history*: V5b underwent 8 iterations in W4 + W5 Phase 3:
- V5b-T canonical (W4 04-26): super-lattice translation Goldstone.
- V5b-F (W4 04-26 → Cat C → W5 Day 2 Phase 2 → Cat B target Branch B refined → Phase 3 → Cat B verified mechanism (a)+(b)+(c) per `01_*` §3.4).
- **V5b-T' (W5 Day 2 Phase 3)**: corner-saturation on translation-invariant graphs; new finding from E10 mode-crossing observation at ζ=0.43.

*References*:
- Original observation: `THEORY/logs/daily/2026-04-28/01_NQ173_v5b_f_verdict.md` §6 (single-formation corner-saturation finding).
- Mode-crossing: `THEORY/logs/daily/2026-04-28/16_K2_baseline_and_zeta45_results.md` §2 (R3a → R3b transition at ζ=0.43).
- PN-barrier formula: `THEORY/logs/daily/2026-04-28/11_PN_unification.md` §4.
- Regime classification: `THEORY/logs/daily/2026-04-28/07_corner_touching_quantification.md` §5 (R1-R4) refined per `16_*` §2.5 (R3 → R3a + R3b).
```

### §1.3 Estimated canonical line delta if approved

~50-60 lines for new §13 entry.

### §1.4 Implications

This canonical addition would:
- Complete the V5b family: V5b-T (super-lattice translation-invariant) + V5b-T' (sub-lattice translation-invariant) + V5b-F (sub-lattice translation-broken).
- Provide explicit mechanism for σ-framework Hessian study at small c (regime R3b).
- Fix Phase 1 self-critique #4 hidden assumption (Option A interior-only) by acknowledging that sub-lattice c<c_s minimizers ARE corner-saturated and require V5b-T' / V5b-F treatment.

---

## Part 2: F11 — σ_multi A⊕D Combined Invariant Proposal

### §2.1 Proposed §11.1 Commitment 14-Multi extension

Insert AFTER existing Commitment 14 (canonical line 768).

### §2.2 Proposed text

```
**Commitment 14-Multi (New, 2026-04-28, W5 Day 2 Phase 4).** Extension of Commitment 14 to multi-formation K-field architecture.

Let u* = (u^(1)*, ..., u^(K)*) ∈ Σ^K_M be a Morse-0 K-formation joint minimizer of K-field energy E_K under involutive canonical iso ρ ∈ Aut(G) on each pair (assumption (H1) of T-Persist-K-Sep + Phase 3 wreath-iso involution requirement).

**σ_multi(u*) := (σ_multi^A(u*), σ_multi^D(u*))** — combined invariant with two layers:

Layer A (continuous spectroscopic):
σ_multi^A(u*) = (F_total(u*); {σ_j(u^(j)*)}_{j=1}^K; {σ_jk(pair (j,k))}_{1 ≤ j < k ≤ K})
where:
- F_total = total local-maxima count (in well-separated regime: Σ_j F(u^(j)*)).
- σ_j = Commitment 14 σ-tuple of formation j.
- σ_jk = cross-block σ-tuple via permutation-module irreps of Stab(u^(j), u^(k)) ≀ S_2 (per `08_lemma5_1_step3_proof.md` §2 Frobenius reciprocity).

Layer D (discrete topological):
σ_multi^D(u*) = orbit-type conjugacy class O ∈ ConjugacyClasses(Aut(G) ≀ S_K) of the joint stabilizer.

**Reduction**: When K=1, σ_multi^A reduces to single-formation Commitment 14 σ-tuple, and σ_multi^D reduces to conjugacy class of Stab(u*) in Aut(G).

**Complementarity**: Per `12_D_to_A_reduction.md` Theorem 2.1' (refined `19_*` §2.3), σ_multi^A and σ_multi^D are complementary — A captures continuous parameter dependence (β, c, λ_rep), D captures discrete orbit structure (geometric placement).

**Goldstone-pair instability**: For translation-invariant graph in regime R1 super-lattice, K=2 minimizer is generically a saddle by T-σ-Multi-1 (`09_goldstone_instability_proved.md`):
    μ_antisym ≈ μ_Gold - c_eff(L) · λ_rep
where c_eff(L) → 1 as L → ∞ (continuum limit) and c_eff ≈ 0.29-0.37 measured at finite L (Phase 4 F5).

**Numerical anchor**: Phase 3 + Phase 4 numerical (`scripts/results/{nq173, nq174, e9, e10, f5, f6, f7, f8}_*.json`): σ_multi^A structure verified for K=2 (regime R1) and K=3 (triangular) at L ∈ {16, 20, 24}, c ∈ {0.10, 0.15}. σ_multi^D orbit-type label trivial at full D_4-symmetric configurations; non-trivial at reduced-symmetry configurations.

**Note (paper exposition)**: A is the operational form for numerical computation; D is the topological form for persistence / orbit-type classification. Recommend presenting both layers in any paper-§4-style exposition.
```

### §2.3 Estimated canonical line delta if approved

~30-40 lines for Commitment 14-Multi extension.

### §2.4 Implications

- Establishes multi-formation σ-framework with formal canonical commitment.
- Distinguishes continuous (A) vs topological (D) layers.
- Refines T-Persist-K-Sep (canonical §13 line 854) by explicitly stating Goldstone-pair instability mechanism (`09_*`).
- Sets up paper §4 σ-framework section structure.

---

## §3. Combined User Decision Package

The user has THREE canonical-edit decisions pending Day 2:
1. **Commitment 14 (O5')/(O7)** — Day 1 carry, Phase 1+2 review (`03_canonical_proposal_v5b_t_update.md` §5).
2. **V5b-T'** — Phase 4 F10 (this file Part 1).
3. **σ_multi A⊕D Commitment 14-Multi** — Phase 4 F11 (this file Part 2).

If user approves all three, total canonical edit:
- §11.1: ~30 + 40 = 70 lines (Commitment 14 (O5')(O7) + Commitment 14-Multi).
- §13: ~50 + 60 + 50 = 160 lines (V5b-F mechanism + ζ_*(graph,c) + V5b-T').
- theorem_status.md: ~30 lines (CV-1.5.1 release + new C-IDs).
- CHANGELOG.md: ~200-300 lines (Phase 1 + 2 + 3 + 4 cumulative changelog entry).

**Total**: ~280-340 lines if all approved → v1.5 → v1.6 release.

Per meta-prompt §8.1, user must explicitly trigger canonical edit. Default: D-5 conservative (no edits Day 2).

---

## §4. Cross-References

- `01_NQ173_v5b_f_verdict.md` §3.4: V5b-F refined statement (Branch B).
- `03_canonical_proposal_v5b_t_update.md` §5: Commitment 14 (O5')(O7).
- `06_approach_AB_equivalence_and_D.md` §3: Approach D framework.
- `09_goldstone_instability_proved.md`: T-σ-Multi-1 Cat A.
- `11_PN_unification.md` §4: PN-barrier unified formula.
- `12_D_to_A_reduction.md` + `19_*` §2: Theorem 2.1.
- `16_K2_baseline_and_zeta45_results.md` §2: R3a/R3b transition.
- `17_c_eff_derivation.md`: c_eff formula.
- `18_wreath_cohomology_computation.md`: H^1 verification.

---

**End of 20_canonical_proposals_F10_F11.md.**
**Status: V5b-T' canonical entry text drafted (~50-60 lines). Commitment 14-Multi extension drafted (~30-40 lines). Combined with Phase 1+2 proposals: ~280-340 lines total canonical edit available for user-approved batch (CV-1.5.1 candidate).**
