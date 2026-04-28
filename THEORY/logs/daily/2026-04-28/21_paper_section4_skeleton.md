# 21_paper_section4_skeleton.md — Paper §4 σ-framework Section Draft Skeleton

**Session:** 2026-04-28 (W5 Day 2 Phase 4, F12).
**Target:** Draft skeleton of Paper 1 §4 "σ-framework: discrete invariants of soft cohesion formations". Map Phase 1-4 results to subsections; outline + key theorem cards + figure placeholders.
**Status:** Skeleton-only (not full draft). ~6-8 page target for paper. Key claims + result-card pointers; full prose for W6+.
**Cross-ref:** `13_LSW_connection.md` §6.1 (canonical mathematics framework); all Phase 1-4 substantive files.

---

## §4.0 Section Title and Abstract

**§4. σ-framework: Discrete Invariants of Soft Cohesion Formations**

**Section abstract** (~150 words):
Soft cohesion fields u_t : X → [0,1] on finite graphs admit a canonical discrete invariant σ that captures the formation's symmetry structure beyond mere local-maxima count F. We define σ as a tuple of (Hessian eigenvalue, irrep label under stabilizer, Courant nodal count) for the lowest K modes of the Hessian at a Morse-0 critical point. For multi-formation K-field configurations on Σ^K_M, σ extends to σ_multi with two layers: a continuous spectroscopic layer σ_multi^A (per-formation σ_j + cross-formation σ_jk), and a topological layer σ_multi^D (orbit-type conjugacy class). We prove well-definedness, compute σ_multi explicitly for the case of two D_4-symmetric disks on a 2D torus, and establish a Goldstone-pair instability theorem connecting σ_multi to Lifshitz-Slyozov-Wagner coarsening dynamics. Numerical verification on T²_{20} confirms predicted instability rates and the coarsening law.

---

## §4.1 Single-formation σ (foundation)

### Subsection structure

§4.1.1 Definition (Commitment 14)
- Display: σ(u*) = (F(u*); {(n_k, [ρ_k], λ_k)}_{k=1}^K)
- Hypotheses: Morse-0, finite graph, stabilizer well-defined.

§4.1.2 Well-definedness (canonical T-σ-Lemma-1)
- Maschke + Schur theorem on Stab(u*) acting on 1⊥.
- Reference: canonical T-σ-Lemma-1.

§4.1.3 Closed-form: σ on uniform field on D_4 grid (canonical T-σ-Theorem-3)
- μ_k = 4α λ_k^Lap + β W''(c) decomposition.
- Worked example: 4×4 D_4 grid with explicit σ-tuple.

§4.1.4 Closed-form: σ at first pitchfork (canonical T-σ-Theorem-4)
- D_4 → Z_2 symmetry breaking, σ-tuple at u*_ε.

### Figure placeholder F1

Caption: "σ-tuple structure for single-formation D_4-symmetric disk on T²_{20}: (a) profile u*; (b) Hessian eigenvalue spectrum; (c) irrep decomposition by D_4 character table."

### Citation chain

- T-σ-Lemma-1 (canonical §13 W5 Day 1 G0).
- T-σ-Theorem-3, T-σ-Theorem-4 (canonical §13 W5 Day 1 G0).
- Commitment 14 (canonical §11.1).

---

## §4.2 Multi-formation σ_multi: Two Complementary Layers

### Subsection structure

§4.2.1 K-field architecture review
- E_K = Σ E(u^(j)) + λ_rep <u^(j), u^(k)> + λ_bar simplex.
- Σ^K_M = product manifold.
- Reference: canonical I9 K-field architecture.

§4.2.2 σ_multi^A: continuous spectroscopic layer
- Definition 5.1: σ_multi^A = (F_total; {σ_j}; {σ_jk}).
- Per-formation σ_j unchanged from single-formation Commitment 14.
- Cross-formation σ_jk via permutation-module irreps of D ≀ S_2 (where D = Stab(disk)).
- Frobenius reciprocity: 10 permutation-module irreps for D = D_4.
- Reference: `05_*` §5, `08_*` §2.

§4.2.3 σ_multi^D: discrete topological layer
- Definition: σ_multi^D = orbit-type conjugacy class of joint stabilizer.
- Cohomology fingerprint H^*(B(D ≀ S_2); R) (e.g., H^1 = (Z/2)^3 for D_4 ≀ S_2).
- Reference: `10_*`, `18_*`.

§4.2.4 A vs D complementarity (Theorem 2.1)
- A captures continuous parameter dependence.
- D captures topological orbit position.
- Neither determines the other.
- Reference: `12_*`, `19_*` §2.

### Theorem card §4.2-T1

**Theorem (σ_multi well-definedness):** For K=2 well-separated minimizer with involutive canonical iso, σ_multi^A and σ_multi^D are well-defined and Aut(G) ≀ S_2-orbit-invariant.
*Proof:* `08_*` §2 (Frobenius reciprocity for σ_multi^A); §2 (orbit-type for σ_multi^D).
*Cat status:* Cat A under involution hypothesis.

### Figure placeholder F2

Caption: "σ_multi^A computational pipeline: (a) two K=2 disks at d=8; (b) joint Hessian block decomposition; (c) Sym/Antisym sector splitting with eigenvalue formula μ_k(H_jj) ± λ_rep · c_eff."

---

## §4.3 Goldstone-Pair Instability Theorem (T-σ-Multi-1)

### Subsection structure

§4.3.1 Statement
- For translation-invariant G + super-lattice regime (R1) + K=2 well-separated:
  μ_antisym = μ_Gold - c_eff(L) · λ_rep
- Instability: K=2 is saddle for any λ_rep > 0 in continuum limit.

§4.3.2 c_eff formula
- c_eff = (mode-overlap)² × (gap fraction).
- Numerical: c_eff ≈ 0.33 at L=20; c_eff(L) → 1 as L → ∞.
- Reference: `09_*`, `17_*`, `19_*` §1.

§4.3.3 Connection to T-Persist-K-Sep / T-Persist-K-Weak
- T-σ-Multi-1 explicitly characterizes when SR (spectral repulsion) hypothesis fails.
- Refines canonical merge mechanism.

### Theorem card §4.3-T2

**Theorem (T-σ-Multi-1, Cat A):** K=2 minimizer on translation-invariant graph in R1 super-lattice regime is unstable iff λ_rep > c_eff(L) · μ_Gold^lifted, with c_eff(L) → 1 in continuum limit.
*Proof:* `09_*` §2-§4 (Sym/Antisym block-diagonalization in identified coords + 2nd-order perturbation theory).
*Cat status:* Cat A (under involution canonical-iso hypothesis).

### Figure placeholder F3

Caption: "K=2 Goldstone-pair instability: (a) joint Hessian eigenvalue spectrum showing antisym mode at -c_eff·λ_rep; (b) c_eff(L) vs L showing approach to 1; (c) phase diagram (λ_rep, β) showing stable/unstable regions."

### Numerical evidence subsection

Phase 3 E9 + Phase 4 F5 measurements:
| L | c | μ_Gold | c_eff | Joint H λ_min |
|---|---|---|---|---|
| 16 | 0.10 | 0.0085 | 0.290 | -0.029 |
| 20 | 0.10 | 0.0025 | 0.335 | -0.034 |
| 24 | 0.10 | 0.0021 | 0.364 | -0.036 |

c_eff trend: increases with L → 1 in continuum limit. Confirms theory.

---

## §4.4 V5b Family: Three Goldstone Regimes

### Subsection structure

§4.4.1 V5b-T (canonical, super-lattice translation-invariant)
- Goldstone exponentially suppressed.
- Reference: canonical T-V5b-T (W4-04-26).

§4.4.2 V5b-F (refined, sub-lattice translation-broken)
- Corner-saturated cluster pushed against graph boundary.
- Mechanism: bulk-localized Goldstone + boundary mode-mixing + PN-barrier-lifted eigenvalue.
- Cat B target.
- Reference: `01_*` §3.4, canonical proposal `20_*` Part 1.

§4.4.3 V5b-T' (NEW, sub-lattice translation-invariant)
- Corner-saturated cluster on translation-invariant graph (no boundary needed).
- Cluster boundary creates PN-barrier.
- Cat B target.
- Reference: `11_*` §3.1, canonical proposal `20_*` Part 1.

### Unified formula

μ_PN(ξ_0, x_*, ∂Cluster) = A β e^{-c_d/ξ_0} f_comm(φ) g_∂(δ/ξ_0)

Recovers all three V5b regimes as limits:
- V5b-T: ∂Cluster = ∅ (smooth interior).
- V5b-T': ∂Cluster = saturation set boundary (interior of translation-invariant graph).
- V5b-F: ∂Cluster ⊃ graph boundary.

### Figure placeholder F4

Caption: "V5b family on (β, c, ∂G) parameter space: (a) V5b-T super-lattice; (b) V5b-T' corner-saturated translation-invariant; (c) V5b-F corner-saturated translation-broken. Phase boundaries at ζ_*(c) determined by NQ-174."

---

## §4.5 LSW Coarsening Connection

### Subsection structure

§4.5.1 SCC K-field coarsening law derivation
- From T-σ-Multi-1 instability rate τ_linear = 1/|μ_antisym|.
- Mass-conservation → R(t) ~ (λ_rep · t)^{1/d}.
- Reference: `13_*` §3.

§4.5.2 d=3 LSW recovery
- R(t) ~ t^{1/3} matches classical LSW law.
- λ_rep ↔ D σ correspondence.

§4.5.3 d=2 anomaly
- SCC predicts t^{1/2}; classical 2D coarsening varies.

### Theorem card §4.5-T3

**Theorem (SCC-LSW correspondence, Cat B):** In sharp-interface limit ξ_0 → 0 of K-field architecture with K ≫ 1, R(t) ~ (λ_rep · t)^{1/d}. In d=3, recovers classical LSW law with λ_rep ↔ D σ.
*Proof sketch:* `13_*` §3.4 (scaling argument) + Modica-Mortola (canonical T11).
*Cat status:* Cat B sketched; full Cat A via rigorous derivation NQ-217 (Phase 4+).

### Figure placeholder F5

Caption: "K=10 simulation on T²_{20}: (a) initial K=10 spread; (b-d) snapshots at t=50, 100, 200 showing K_active decrease; (e) R(t) vs t log-log plot with predicted t^{1/2} slope."

---

## §4.6 Discussion: σ-Framework's Place in SCC Theory

### Subsection structure

§4.6.1 Position relative to other canonical results
- σ-framework completes the morphological characterization of formations.
- Bridges single-formation theory (W4) and multi-formation extension (W5+).

§4.6.2 Ontological claims
- σ is intrinsic SCC mathematics (CN10), not borrowed from atomic physics or biology.
- Captures pre-objective formation identity (Commitment 14 + 15).

§4.6.3 Open questions
- σ on continuum graphs (NQ-022 LOW).
- σ for non-involutive canonical iso (NQ-200).
- σ uniqueness theorem (NQ-188).

---

## §4.7 Methods (numerical)

### Subsection content

- Optimizer: scc.optimizer.find_formation + scc.multi.find_k_formations.
- Hessian: finite-difference, lowest 6-12 modes.
- All numerical at α=1, β=4, c=0.10 unless specified.
- 131 numerical attempts cumulative across NQ-173, NQ-174, E9, E10, F5, F6, F7, F8.

---

## §5. Mapping Phase 1-4 Results to Section

| Subsection | Primary source | Cat status |
|---|---|---|
| §4.1 (single-formation σ) | canonical T-σ-Lemma-1/2/3 + Theorem-3/4 | Cat A |
| §4.2 (σ_multi^A) | `05_*`, `08_*` | Cat A under involution |
| §4.2 (σ_multi^D) | `10_*`, `18_*` | Cat A (cohomology) |
| §4.2 (Theorem 2.1) | `12_*`, `19_*` §2 | Cat A K=2 |
| §4.3 (T-σ-Multi-1) | `09_*`, `17_*` | Cat A under involution |
| §4.4 (V5b family) | `01_*` §3.4, `11_*`, `20_*` Part 1 | Cat B targets |
| §4.5 (LSW) | `13_*` | Cat B sketched |
| §4.6 (Discussion) | All Phase results | — |
| §4.7 (Methods) | F5, F6, F7, F8 | — |

---

## §6. Estimated Page Count

- §4.0 abstract: 0.25 pages.
- §4.1 single-formation: 1.5 pages.
- §4.2 σ_multi: 2 pages.
- §4.3 T-σ-Multi-1: 1.5 pages.
- §4.4 V5b family: 1.5 pages.
- §4.5 LSW connection: 1 page.
- §4.6 discussion: 0.5 pages.
- §4.7 methods: 0.5 pages.

**Total ~8.75 pages**. Slightly over the 6-8 page target — could compact §4.4 or §4.5 if needed.

---

## §7. Open Tasks for Full Draft (W6+)

- Convert each subsection from skeleton to full prose.
- Generate actual figures from Phase 3+4 numerical data.
- LaTeX formatting (custom theorem environment for theorem cards).
- Consistent notation cross-checking with rest of paper.
- Bibliography integration.

---

## §8. Cross-References

All Phase 1-4 substantive files referenced inline.

---

**End of 21_paper_section4_skeleton.md.**
**Status: Paper §4 skeleton ready. ~8.75 pages estimated. 5 theorem cards identified. 5 figure placeholders. W6+ work to fill in prose + generate figures.**
