---
type: working/afd/v_afd
status: V-AFD Draft v0.1 (2026-05-12)
---

# V-AFD Internal Audit

15-question internal audit per prompt §10. Each question is answered with a verdict (✓ PASS / ⚠ NEEDS CARE / ✗ FAIL) plus a short justification and a pointer to the relevant location in V-AFD.

The audit follows the AFD-0 audit style (`../afd_audit.md` 20-question pattern).

---

## Q1. Is V-AFD clearly a projection / coarse-graining, not a replacement for SCC field dynamics?

**Verdict.** ✓ PASS.

**Justification.** `vector_abstract_formation_dynamics.md` §0 (Executive Summary) and §1.4 (What V-AFD does not add) state explicitly: "V-AFD is a projection / coarse-graining of SCC field dynamics" and "V-AFD does not redefine SCC field dynamics; V-AFD studies its image under Z." V-AFD-D12 names the projection `π_Z : V_form → V_Z` as a *surjective projection*. The slogan in §0 explicitly says: "AFD-0 builds G_form. V-AFD builds the vector quotient π_Z : G_form → G_V."

**Locations.** §0, §1.4, §2.1–2.3, V-AFD-D12.

---

## Q2. Is D(u) defined for single fields or temporal windows? Is Persist handled correctly?

**Verdict.** ✓ PASS.

**Justification.** V-AFD-D1 provides three forms:
- (Static) `D(u) ∈ [0,1]^4` with `Persist(u) := 1` placeholder.
- (Pairwise) `Persist_pair(u, v, M)` via core-overlap under transition operator.
- (Window) `Persist_W({u_t})` infimum over time window.

The static placeholder is explicitly labeled as such — not a substantive value. The substantive temporal/pairwise forms are deferred to T-Temporal-Identity Cat A inputs.

**Limitation acknowledged.** OP-VAFD-002 captures the *temporal-extension protocol*: when to use which form. This is open.

**Locations.** V-AFD-D1, §6.3 (warnings), OP-VAFD-002.

---

## Q3. Are Bind / Sep / Inside / Persist continuity assumptions explicit?

**Verdict.** ✓ PASS.

**Justification.** V-AFD-T5 (Cat A) gives a per-component Lipschitz bound:
- Bind via A3 closure Cat A.
- Sep via Predicate-Energy Bridge Cat A.
- Inside via QM3 + CSEH Cat A, **modulo OP-AFD-001 vineyard stability**.
- Persist static placeholder is trivially Lipschitz; pairwise/window forms via T-Temporal-Identity Cat A.

The vineyard-stability dependence of Inside is explicitly flagged (V-AFD-T5 Per-component honest status).

**Locations.** V-AFD-T5, OP-VAFD-001.

---

## Q4. Is K_act discontinuity acknowledged?

**Verdict.** ✓ PASS.

**Justification.** V-AFD-T4 caveat: "K_act ∘ γ is integer-valued, with càdlàg structure for generic γ (transversal to V)." V-AFD-T10 makes this precise: piecewise constant with finitely many jumps at transversal V-crossings. Non-transversal case (OP-VAFD-007) acknowledged.

The overall `z_γ` is labeled **càdlàg** in V-AFD-T4, not Lipschitz.

**Locations.** V-AFD-T4, V-AFD-T10, V-AFD-D10, §6.5, OP-VAFD-007.

---

## Q5. Is topology signature stability acknowledged?

**Verdict.** ✓ PASS.

**Justification.** V-AFD-D2 specifies τ stability as **Lipschitz in d_B (bottleneck)** per CSEH 2007. V-AFD-T4 says `τ ∘ γ` is continuous in d_B. V-AFD-T5 uses `L_τ = 1` in bottleneck.

The **sorted-bar vector** is acknowledged as discontinuous (§6.4 warning). The relationship between bottleneck-Lipschitz and sorted-bar discontinuity is precisely captured by càdlàg classification.

**Locations.** V-AFD-D2, V-AFD-T4, V-AFD-T5, §6.4, OP-VAFD-005.

---

## Q6. Is Z injectivity loss acknowledged?

**Verdict.** ✓ PASS.

**Justification.** V-AFD-T9 (Vector Projection Information Loss) is a dedicated *Theorem* establishing non-injectivity by examples (symmetric, Goldstone, topologically coincident). V-AFD-D12 formalizes the projection and notes "π_Z may identify dynamically distinct basins with similar diagnostic vectors. This is the *fundamental information loss* of V-AFD." Section 6.1 lists three mitigation strategies (basin label, field fingerprint, Aut(G)-quotient).

OP-VAFD-004 registers the **characterization** of *when* loss matters as open.

**Locations.** V-AFD-T9, V-AFD-D12, §6.1, OP-VAFD-004.

---

## Q7. Is vector transition cost nonnegative?

**Verdict.** ✓ PASS.

**Justification.** V-AFD-T6 Theorem (a): "J_V(γ; F_i) ≥ 0 for any admissible γ." Each summand is non-negative; non-negative weights preserve. C_V ∈ [0, +∞] follows.

**Locations.** V-AFD-T6.

---

## Q8. Is vector transition cost called a metric anywhere? If yes, remove unless proven.

**Verdict.** ✓ PASS.

**Justification.** `C_V` is consistently labeled **cost** or **edge weight**. V-AFD-D6 closing note: "C_V, like C_AFD, is **not** a metric: asymmetric, triangle inequality fails in general. The terminology is **cost** or **edge weight**, never metric." Section 6.7 reiterates the warning.

A text-grep of `vector_abstract_formation_dynamics.md` for "metric" finds:
- Product metric on Z (V-AFD-D2): this is a metric (Σ of metrics on factor spaces), correctly named.
- Bottleneck metric d_B (V-AFD-D2): standard PD metric, correctly named.
- "C_V is not a metric" (V-AFD-D6, §6.7): negation, correctly stated.

No false metric claim for `C_V`.

**Locations.** V-AFD-D6 (closing note), §6.7.

---

## Q9. Does vector graph require H-MORSE? It should not.

**Verdict.** ✓ PASS.

**Justification.** V-AFD-T7 (Theorem by-inspection) states: "V-AFD-D1..D12 and V-AFD-T1..T11 do not use H-MORSE-Local, H-MORSE-Saddle, Hessian determinants, or Morse genericity." V-AFD-T11 (vector graph well-definedness) is by-construction Cat A; no Hessian appears.

The only V-AFD result that interfaces with H-MORSE is V-AFD-T8 (EK Compatibility), which is **Layer-3 conditional** and explicitly marked.

**Locations.** V-AFD-T7, V-AFD-T11, V-AFD-T8, §6.8.

---

## Q10. Is EK only a refinement? It should be.

**Verdict.** ✓ PASS.

**Justification.** V-AFD-T8 is labeled "**Lemma Candidate (Conditional, Layer 3)**." The statement explicitly assumes "Layer-3 hypotheses (H-MORSE-Local + H-MORSE-Saddle + Package I + T_*)." The conclusion is **exponential-order compatibility only**: `T_* log E[τ] → Bar`. Prefactors are not claimed.

Section 1.2 ("Why not exact Eyring-Kramers as foundation") explicitly defers EK to Layer 3.

The V-AFD baseline `Z = (D, K_act, E, τ)` is independent of EK.

**Locations.** V-AFD-T8, §1.2, V-AFD-T7 caveat.

---

## Q11. Is scalar diagnostic quality optional? It should be.

**Verdict.** ✓ PASS.

**Justification.** V-AFD-D9 (Scalarization) opens with: "A **scalar quality** on 𝒵 is `Q_w(D) := w_B Bind + ...`." It then states explicitly: "Scalarization is **optional** and **lossy**." Section 6.6 reiterates the warning: "scalarization loses Pareto information."

V-AFD-D9 does **not** commit to canonical weights `w`; the choice is "application-specific."

The Pareto preorder V-AFD-D8 / V-AFD-T2 stands independently of scalarization.

**Locations.** V-AFD-D9, V-AFD-T2, §6.6.

---

## Q12. Is Pareto incomparability acknowledged?

**Verdict.** ✓ PASS.

**Justification.** V-AFD-T2 part (c) states: "Not total: there exist F_i, F_j ∈ V_form with d_i, d_j componentwise incomparable." Explicit counterexample provided: `d_i = (0.8, 0.2, 0.5, 1)`, `d_j = (0.2, 0.8, 0.5, 1)`.

V-AFD-D8 defines `\|_D` (Pareto-incomparable relation) explicitly.

**Locations.** V-AFD-T2 (c), V-AFD-D8.

---

## Q13. Is Markovianity of vector dynamics left open unless proven?

**Verdict.** ✓ PASS.

**Justification.** V-AFD-T12 is explicitly labeled "**Open Problem** (OP-VAFD-003)." No Markov claim is made. The heuristic considerations (H-1 to H-4) note: "Without basin label, the vector Z(u) alone is insufficient for Markov."

OP-VAFD-003 is the single H-severity open problem in V-AFD.

**Locations.** V-AFD-T12, OP-VAFD-003.

---

## Q14. Are examples concrete enough to test the abstraction?

**Verdict.** ✓ PASS.

**Justification.** `v_afd_examples.md` provides 8 scenarios, each with:
- Concrete setup (canonical 15×15 grid, named β, vol_frac, parameters).
- Expected `Z` per coordinate with plausibility estimates.
- What V-AFD captures (specific quantities).
- What V-AFD loses (specific information).
- Whether additional coordinates are needed (specific recommendations).

Each scenario is a different topological / dynamical situation (single, weak, merge, split, reconfiguration, vector-degeneracy, Goldstone, topology-event-low-energy). The diversity stress-tests V-AFD breadth.

**Locations.** `v_afd_examples.md`, V-AFD-D-section §5.

---

## Q15. Are all theorem candidates assigned honest statuses?

**Verdict.** ✓ PASS.

**Justification.** Per `v_afd_theorem_registry.md`:

| ID | Status |
|---|---|
| V-AFD-T1 | Proposition (Cat A) |
| V-AFD-T2 | Proposition (Cat A) |
| V-AFD-T3 | Proposition (well-def) + Conjecture (monotonicity) |
| V-AFD-T4 | Theorem (Cat A) |
| V-AFD-T5 | Theorem (Cat A) |
| V-AFD-T6 | Theorem (Cat A) |
| V-AFD-T6' | Theorem **modulo Claim B.3** |
| V-AFD-T7 | Theorem (by-inspection) |
| V-AFD-T8 | Lemma Candidate (Conditional, Layer 3) |
| V-AFD-T9 | Theorem (by examples) |
| V-AFD-T10 | Proposition (Cat B modulo OP-AFD-002 reach) |
| V-AFD-T11 | Proposition (by-construction Cat A) |
| V-AFD-T12 | Open Problem |

No claim is upgraded to a stronger label than its proof supports. Specifically:
- V-AFD-T3 is not claimed to be a Lyapunov theorem (only the well-definedness is proved; monotonicity is conjecture).
- V-AFD-T6 is finiteness only; attainment is V-AFD-T6'.
- V-AFD-T6' is modulo Claim B.3 (matches today's audit of T-OP-AFD-003-A).
- V-AFD-T10 is Cat B modulo a reach lower bound from OP-AFD-002 (vineyard codim-1 regularity).
- V-AFD-T8 is Conditional Layer 3.
- V-AFD-T12 is Open.

**Locations.** `v_afd_theorem_registry.md`, V-AFD-T1..T12.

---

## Summary

| Question | Verdict |
|---|---|
| Q1 Projection not replacement | ✓ |
| Q2 D / Persist forms | ✓ |
| Q3 Continuity explicit | ✓ |
| Q4 K_act discontinuity | ✓ |
| Q5 τ stability | ✓ |
| Q6 Injectivity loss | ✓ |
| Q7 Nonnegativity | ✓ |
| Q8 Not a metric | ✓ |
| Q9 H-MORSE free | ✓ |
| Q10 EK Layer-3 only | ✓ |
| Q11 Scalarization optional | ✓ |
| Q12 Pareto incomparability | ✓ |
| Q13 Markovianity open | ✓ |
| Q14 Examples concrete | ✓ |
| Q15 Honest statuses | ✓ |

**Audit Verdict.** **PASS** on all 15 questions.

No claim in V-AFD overstates. All caveats are inline. All Cat ratings match the proofs.

The single largest residual gap is V-AFD-T12 (Markovianity, OP-VAFD-003 H-severity) — this is correctly registered as open rather than claimed.

The next largest residual gap is V-AFD-T6' modulo Claim B.3, which inherits the same status as T-OP-AFD-003-A in this-session's `logs/daily/2026-05-12/02b_L3_tightening_and_op003c.md`. When Claim B.3 verification lands, V-AFD-T6' upgrades automatically.

---

## Cross-check against AFD-0 audit principles

Per `../afd_audit.md` Q11 (C_AFD not a metric) and Q12 (pairwise C_AFD not a preorder): V-AFD propagates both:

- V-AFD-D6 inherits non-metricity (Q8 verified above).
- V-AFD-T2 uses Pareto preorder, which is distinct from pairwise `C_V` comparison. The scalar preorder analog is V-AFD-D7 `Stab_V`, defined explicitly as a *design quantity* rather than a preorder.

Per `../afd_audit.md` Q15 (K-strata not smooth): V-AFD-T10 acknowledges the strata are set-theoretic only; smoothness depends on OP-AFD-002.

Per `../afd_audit.md` Q19 (AFD resolves OP-0005?): V-AFD does not claim to resolve OP-0005. K-Selection remains open at the higher level; V-AFD provides only vector-language for stating it.

Per `../afd_audit.md` Q20 (H-MORSE Non-Necessity proven?): V-AFD-T7 inherits AFD-T9; the proof is by-inspection of V-AFD definitions and is consistent with AFD-T9.

No conflicts with AFD-0 audit principles.

---

*End of `v_afd_audit.md`.*
