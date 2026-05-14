---
id: CV-1.7-release-packet
type: working/release-packet
status: final
created: 2026-05-06
sessions: Sessions A–K (W6 D4, 2026-05-06)
---

> [!nav] Linked: [[MOC_parked_superseded]] · [[THEORY_INDEX]]  — SUPERSEDED (cite 금지)


# CV-1.7 Release Packet — Soft Cognitive Cohesion

**Release date:** 2026-05-06 (W6 D4)
**Canonical version:** CV-1.7 (increments from CV-1.5.2 base; CV-1.6 content integrated in-document)
**Claim count:** **50A / 12B / 5C / 5R = 72 claims, ~69% fully proved**
**Preceding state:** CV-1.5.2 + T-L1-M supervised addition (2026-05-04) → 47A/5B/5C/5R = 62 claims

---

## 2.1 Release Summary

### Date and Count

| Count | Before CV-1.7 (CV-1.5.2 + T-L1-M) | After CV-1.7 |
|---|---|---|
| Cat A | 47 | **50** |
| Cat B | 5 | **12** |
| Cat C | 5 | 5 |
| Retracted | 5 | 5 |
| Total claims | 62 | **72** |
| % fully proved | ~75% | **~69%** |

*(Note: % drops because CV-1.7 adds more Cat B claims (stereo extension) than Cat A, diluting the ratio.)*

### Major promotions

| Theorem | Session | Old status | New status |
|---|---|---|---|
| T-ST-5a (Hard-Depth Topological Locking) | Session E | Cat C candidate | **Cat A** |
| T-P-F-ε0 (Gibbs Measure Continuity) | Session I | — (new) | **Cat A** |
| T-OP6-B (PersRidge Boundary Equivalence) | Session K | Cat B | **Cat A conditional** |
| T-P-F-ε0-K (Kramers Exponent Stability) | Session I | — (new) | **Cat B** |
| T-ST-5b (Smooth-Depth Barrier Raising) | Session G | Cat C | **Cat B** |
| D-ST-1..5 (stereo definitions) | Sessions B–D | — (new) | **Cat B candidates** |

### Major non-promotions

- **P-F-A1** (Effective Stochastic Temperature T_* Axiom): OPEN. Spectral gap + Lions-Sznitman reflection not yet proved. T-P-F-ε0 is NOT P-F-A1.
- **T-ST-5b Cat A**: OPEN. Requires monotonicity over Δz/λ_z + analytical lower bound on barrier gap.
- **T-σ-Theorem-4 Cat A re-promotion**: Deferred; CV-1.8+ candidate.

### Resolved open problems

- **OP-0006 (Boundary Definition Precision)**: RESOLVED. T-OP6-B Cat A: d_H ≤ 2·(α/β)^{1/2} under H1–H5. Residuals: C=2 not tight; H4 required; soft-cut stereo open.

### Remaining high-priority open problems

- OP-0005: K Selection Mechanism
- OP-0008: σ^A K-jump Inheritance Non-Determinism
- OP-0009: Multi-Formation Ontological Foundations (7 sub-items; 1/7 resolved via Commitment 16)

---

## 2.2 New / Promoted Theorems

### T-ST-5a — Hard-Depth Topological Locking

**Statement.** Under hard-cut stereo adjacency D-ST-1, depth-gap pixels disconnect the graph G_t^P. A formation spanning both depth regions requires a merger event with ΔE = +∞ (state-space disconnection). Therefore K_act = 2 is topologically locked — no continuous path in state space connects K=2 to K=1.

**Category:** Cat A (Session E, W6 D4 2026-05-06)

**Proof:** Four gaps G1–G4 closed in Session E:
- G1: Lemma 3 not required; graph topology alone suffices (hard-cut disconnects G_t^P)
- G2: Merger vs. decay distinction via IFT on disconnected domain
- G3: A-STRICT assumption (no boundary formation at depth gap)
- G4: Threshold convention (∅ complement well-defined)

**Experiments:** exp02-NEB binary step (ε-bridge → K=2 locked; ΔE=+∞)

**Limitations:** Hard-cut D-ST-1 only. Smooth-cut (D-ST-1 smooth variant) does NOT lock topology (T-ST-5b). No P-F flag (topological argument, no T_*).

**Location:** `canonical.md §16`; proof: `THEORY/working/MF/tst5a_hard_depth_locking_proof.md`

---

### T-P-F-ε0 — Gibbs Measure Continuity at ε=0

**Statement.** Let μ_ε be the Gibbs measure with Bernoulli regularization R = −T_* S_Bern at strength ε ∈ [0,ε_0]. Under H1 (compact field space F_M(P)), H2 (polynomial energy continuity), H3 (polytope non-degeneracy, Z_0 > 0), H4 (dominated convergence hypothesis): μ_ε ⇒ μ_0 weakly as ε → 0.

**Category:** Cat A (Session I, W6 D4 2026-05-06)

**Proof (4 steps):**
1. F_M(P) compact → σ(F_M) ∈ (0,∞) (H1)
2. E_SCC continuous + non-degeneracy → Z_0 ≥ exp(−E_*/T_*)·σ(F_M) > 0 (H2+H3)
3. Dominating function h(ũ) = exp(−E/T_*)·exp(C/T_*); g_ε → g_0 pointwise; DCT → Z_ε → Z_0 > 0 (H4)
4. Decompose ∫f dμ_ε − ∫f dμ_0 into Term I (→ 0 by DCT) + Term II (→ 0 since Z_ε → Z_0 > 0)

**Non-overclaim:** T-P-F-ε0 is NOT P-F-A1. Does not prove: spectral gap, Eyring-Kramers formula, T_* existence, or Lions-Sznitman construction. It establishes only continuity of the Gibbs target under Bernoulli regularization.

**Location:** `canonical.md §13 Category A`; proof: `THEORY/working/MF/pf_tstar_langevin.md §8.5`

---

### T-OP6-B — PersRidge Boundary Equivalence

**Statement.** Under H1–H5, the persistent gradient ridge boundary and the topological boundary of the persistent formation core satisfy:

d_H(B_PersRidge(ũ*), ∂PersComp(ũ*)) ≤ 2·(α/β)^{1/2}

with C = 2 explicit. ∂PersComp = {x ∈ C_j : ∃y~x, y ∉ C_j}, C_j = {x : ũ*(x) ≥ 1/2}.

**Assumption package H1–H5:**
- H1: Phase separation (β/α > 4λ_2/|W''(c)|)
- H2: Well-formed formation (connected C_j, non-empty interior)
- H3: Canonical ρ_bd = 1/(4ξ), ξ = (2α/β)^{1/2}
- H4: Bounded curvature κ_max·ξ ≤ 0.1
- H5: Hard-cut D-ST-1 stereo adjacency (for stereo B3)

**Category:** Cat A conditional under H1–H5 (promoted Cat B → Cat A, Session K, 2026-05-06)

**Proof (B1–B4 all closed):**
- B4 (Session J): ρ_bd·ξ = 1/4 constant; Δ_1D = ξ·arctanh(1/√2) ≈ 1.246(α/β)^{1/2}
- B2 (Session K): Matched-asymptotic expansion; Pöschl-Teller correction |v_1'| ≤ 1; under H4: d_H < 1.37ξ < 2(α/β)^{1/2}
- B1 (Session K): Any path C_j^int → C_j^ext crosses ∂C_j ⊂ B_t; B_t is vertex separator
- B3 (Session K): G_t^P severs depth-gap edges; PersRidge on stereo graph inherits bound

**Experiments:** exp06 (shadow 5/5 ratio 4.09; blur 5/5 ratio 50.8; SCC 4–51× more stable than raw gradient)

**Limitations:** C=2 not tight (inner bound C < 1.37 under H4); H4 required; continuum proof; soft-cut stereo conditional; not peer-reviewed.

**Location:** `canonical.md §5.3b` + `§13 Category A`; proofs: `THEORY/working/MF/op_0006_boundary_precision.md §9–§12`

---

### T-P-F-ε0-K — Kramers Exponent Stability under Bernoulli Regularization

**Statement.** Under T-P-F-ε0 hypotheses H1–H4 and H5 (Morse stability: saddle and minimum are non-degenerate under ε-perturbation), the perturbed barrier satisfies:

ΔE_ε = ΔE_0 + ε·ΔR

where ΔE_0 = E(ũ*_sad) − E(ũ*_min) and ΔR = R(ũ*_sad) − R(ũ*_min). The Arrhenius factor satisfies Γ_ε = Γ_0·exp(−ε·ΔR/T_*).

Bernoulli specialization: At phase-separated endpoints, S_Bern(ũ*_min) ≈ 0, giving Γ_B/Γ_A = exp(O(δ)) = 1 + O(δ), exponentially small in phase-separated regime.

**Category:** Cat B (conditional on H5 Morse stability; Session I, 2026-05-06)

**Non-overclaim:** T-P-F-ε0-K is NOT P-F-A1. Does not prove: spectral gap, Eyring-Kramers pre-exponential factor A, T_* existence, or rate prefactor equivalence of Target B and Target A.

**Cat A path:** H5 proof (global Morse stability for E_SCC + εR) + spectral gap (P-F-A1).

**Location:** `canonical.md §13 Category B`; proof: `pf_tstar_langevin.md §8.5 Corollary`

---

### T-ST-5b — Smooth-Depth Barrier Raising

**Statement (narrow claim, Session G sign-off).** Under smooth depth-weighted adjacency D-ST-1 smooth variant, with full SCC energy active (E_cl + E_sep), intermediate β regime: the NEB barrier height increases relative to monocular SCC by approximately 25% at β=10.

**Category:** Cat B (Session G, 2026-05-06)

**Evidence:** exp02e (full_scc β=10: 6/6 SUPPORTED, 25% increase; gl_only NULL; β=20: 3/6 PARTIAL)

**Limitations (mandatory):**
- GL-only (no E_cl/E_sep): NULL result — T-ST-5b does NOT hold for GL-only
- Monotonicity over Δz/λ_z: NOT confirmed
- NOT a universal theorem
- P-F flag for Kramers interpretation (T_* undefined)
- β=20: only partially supported (3/6)

**Cat A path:** Monotonicity + analytical lower bound on barrier gap.

**Location:** `canonical.md §16`; results: `CODE/experiments/results/exp02e_single_field_neb_summary.md`

---

## 2.3 Open Problem Status Changes

| OP-ID | Name | Before CV-1.7 | After CV-1.7 |
|---|---|---|---|
| OP-0006 | Boundary Definition Precision | TENTATIVE (Cat B candidate) | **RESOLVED** (Session K: T-OP6-B Cat A) |
| P-F-A1 | Effective Stochastic Temperature T_* | OPEN | **OPEN** (surveyed: Bakry-Émery fails, Holley-Stroock weak, route: Lions-Sznitman + Freidlin-Wentzell) |
| T-ST-5b Cat A | Monotonicity + analytical bound | OPEN | **OPEN** (Cat B achieved; monotonicity not confirmed) |
| OP-0009-Pre-a | Architecture migration K-field vs shared-pool | OPEN | **OPEN** (exp02d V3 failure; v2.0 W11–W12) |

---

## 2.4 Technical Corrections

### ρ_bd Scaling Correction (Session J)

**Error (Session I Working Note):** ρ_bd = ½(α/β)^{1/2}. Product ρ_bd·ξ = (α/β)/√2 → 0 as β→∞. This causes Δ → ∞, violating d_H ≤ C·(α/β)^{1/2}.

**Correction:** ρ_bd = 1/(4ξ) = ¼(β/(2α))^{1/2} (half-maximum gradient threshold). ρ_bd·ξ = 1/4 (constant, independent of α, β).

**Also corrected:** Δ formula. Error: ξ·arctanh(√(1−4ρ²ξ²)). Correct: Δ = ξ·arctanh(√(1−2ρ·ξ)) (from sech²(Δ/ξ) = 2ρ·ξ). Gives Δ_1D = ξ·arctanh(1/√2) ≈ 0.881ξ ≈ 1.246(α/β)^{1/2}.

### K-field Endpoint Invalidity / exp02d (Session F)

exp02d V3 failure: K-field endpoints (shared-pool architecture I9) produced invalid states in NEB computation. K-field architecture is NOT the correct shared-pool framework for T-OP6-B and NEB barrier studies. Single-field endpoints validated in exp02e (Session F) which produced T-ST-5b Cat B evidence.

### P-F Target A/B/C Distinction (Session F §8.4)

Three distinct targets for P-F-A1:
- **Target A:** Pure Gibbs μ ∝ exp(−E_SCC/T_*), ε=0 (canonical P-F-A1 axiom v0)
- **Target B:** Bernoulli-regularized, ε=1, λ_K=0 (current `langevin.py` implementation)
- **Target C:** Temperature-annealed, ε→0 schedule (numerical optimization)

T-P-F-ε0 proves Target B → Target A weakly as ε → 0 (these are the same formula with continuous ε parameter). T-P-F-ε0-K shows the Arrhenius barrier is stable under this transition. Full P-F-A1 (spectral gap, mixing time, T_* registration) remains open.

### Non-Overclaim Notes

- T-OP6-B Cat A is CONDITIONAL under H1–H5. C=2 is an upper bound, not tight. H4 is required.
- T-P-F-ε0 is NOT P-F-A1. Weak convergence ≠ spectral gap.
- T-ST-5b is a NARROW claim. Full SCC only, intermediate β only, monotonicity not proved.
- T-ST-5a requires hard-cut D-ST-1. Smooth-cut does not lock topology.

---

## 2.5 Code / Test Status

| Item | Status |
|---|---|
| pytest (215 + 1 xfailed) | PASS (confirmed Sessions J, K, L) |
| Regressions | None (Sessions J–K introduced no code changes) |
| exp06 (boundary stability) | SUPPORTED: shadow 5/5, blur 5/5 |
| exp02e (NEB single-field) | full_scc β=10 6/6 SUPPORTED; gl_only NULL; β=20 3/6 PARTIAL |
| exp01 (PersComp=2 vs slot=4) | SUPPORTED |
| exp02-NEB (T-ST-5a) | Binary step (ε-bridge) SUPPORTED |

**Relevant experiments:**
- `exp01_lambda_sweep.py` — formation existence / PersComp count
- `CODE/experiments/results/exp02e_single_field_neb_summary.md` — T-ST-5b evidence
- `CODE/stereo_scc/experiments/exp06_boundary_stability_shadow_blur.py` — T-OP6-B evidence

**Note:** xfailed test marks `scc.aut_g` as deferred NQ-259 W6+ deliverable. This is intentional.

---

## 2.6 Remaining Blockers

| Blocker | Priority | Route |
|---|---|---|
| P-F-A1 (spectral gap + T_*) | High | Lions-Sznitman reflection + Freidlin-Wentzell quasipotential; see `pf_a1_lions_sznitman_freidlin_route.md` |
| T-ST-5b Cat A (monotonicity + analytical bound) | Medium | Analytical: Allen-Cahn + smooth-adjacency barrier lower bound; Experimental: sweep over Δz/λ_z |
| OP-0009 Multi-Formation v2.0 (architecture migration) | Medium | exp02d V3 failure resolved in exp02e; v2.0 shared-pool architecture W11–W12 |
| T-OP6-B C tightening (C=2 → explicit C < 1.37) | Low | Refine matched-asymptotic; exact Pöschl-Teller bound; numerical verification |
| T-OP6-B soft-cut stereo conditioning | Low | Soft-cut (GL-weighted adjacency) does not have hard depth cut; need separate argument |
| T-OP6-B global H4 verification | Low | κ_max·ξ ≤ 0.1 assumed; should be verified experimentally across formation geometries |
| T-σ-Theorem-4 Cat A re-promotion | Low | γ-path Σ_m-Hessian convention audit; NQ-187 higher-order ε-splitting |

---

## 2.7 CV-1.7 Consistency Audit (Session L)

**Audit conducted:** Session L, 2026-05-06.

**Files audited:**
- `THEORY/canonical/canonical.md` — frontmatter, §5.3b header, §13 headers, §11 count para, §16 end note, active OPs list
- `THEORY/canonical/theorem_status.md` — version line, T-OP6-B row, count footnotes, problem statistics table, cross-reference table, OP-0006 body
- `Perception_theory/CLAUDE.md` — count, T-OP6-B status, OP active list
- `CLAUDE.md` (parent Perception/) — count, T-OP6-B status, theorem_status description

**Fixes applied:**
1. canonical.md frontmatter: CV-1.5.2 → CV-1.7
2. canonical.md §5.3b header: "Cat B — CV-1.6" → "Cat A conditional — CV-1.7"
3. canonical.md §11 count paragraph: "47 fully proved / 62 claims / 75%" → "50 / 72 / ~69%"; added CV-1.7 update entry
4. canonical.md theory-status paragraph: added CV-1.7 forward reference
5. canonical.md active OPs list: 4 High → 3 High; OP-0006 RESOLVED
6. canonical.md §16 end note: added forward reference to Sessions I/K; updated "CV-1.7 completed" target
7. theorem_status.md "current" line: CV-1.5.2 → CV-1.7
8. theorem_status.md problem stats table: High 5 → 4; OP-0006 RESOLVED
9. theorem_status.md summary table: High 4 active → 3 active; OP-0006 RESOLVED
10. theorem_status.md cross-reference table: OP-0006 struck through with RESOLVED note
11. theorem_status.md OP-0006 body: Cat B candidate → RESOLVED with full details
12. Perception_theory/CLAUDE.md: 49A/13B/T-OP6-B Cat B/~68% → 50A/12B/T-OP6-B Cat A/~69%; OP-0006 removed from active list
13. Perception/CLAUDE.md (parent): count and description updated

**Residue search results:**
| Pattern | Result |
|---|---|
| OP-0006 TENTATIVE (not historical) | CLEAN after fixes |
| T-P-F-ε0 conflated with P-F-A1 | CLEAN (all instances have "NOT P-F-A1") |
| T-ST-5b monotonicity overclaim | CLEAN ("Monotone-in-Δz NOT confirmed" in all references) |
| GL-only supporting T-ST-5b | CLEAN ("gl_only NULL" in all references) |
| Σ_M^K as foundational (not local chart) | CLEAN (F_M(P) is foundational; Σ_M^K is local chart per §3.9/§16) |
| slot-count K_act (not qualified) | CLEAN (all references say "regime-conditional approximation") |
| raw image edge as SCC boundary | CLEAN (§5.3b explicitly distinguishes) |
| T_* as raw observation noise | CLEAN (no such conflation found) |
| P-F-A1 marked Cat A | CLEAN (P-F-A1 is "C (working)" / OPEN in all references) |
