---
id: META-0103
type: registry/theorems
status: accepted
last_updated: 2026-05-06
---

# Theorem Registry

**Purpose:** Register all claims (C-xxxx), proofs (P-xxxx), and canonical theorems (T-xxxx, CV-x.y). This is the authoritative index of what has been proved.

**Structure:** Rows are organized by canonical version (CV-1.0 .. CV-1.10; current = **CV-1.10**) then status (active, challenged, deprecated). *(Updated 2026-05-06 after T-OP6-B Cat A promotion, T-P-F-ε0/T-P-F-ε0-K canonical additions, OP-0006 resolution, CV-1.8 P-F-A1 Package I (T-PF-A1-AR/SDE/GI/PE), CV-1.9 Session P T-PF-A1-GI + T-PF-A1-PE Cat B → Cat A, and CV-1.10 Session R T-K-Select-PF Cat B.)*

---

## Canonical Theorems (Accepted into Canonical Spec)

### CV-1.6 Candidates — Stereo-SCC Extension (W6 D4, 2026-05-06, Sessions A–D)

*Not yet canonical — pending CV-1.6 promotion. Bodies in `canonical.md §3.9–§3.11` and `§16`. Source: `THEORY/working/MF/stereo_scc_canonical_memo_v1.1.md`.*

| T-ID / D-ID | Name | Status | Category | Experiments | Notes |
|---|---|---|---|---|---|
| **D-ST-1** | Stereo Adjacency (Hard + Smooth) | in §3.10 | B candidate | exp01 (implicit) | Hard/smooth variants; hard-cut produces disconnected graph (T-ST-5a); smooth uses depth-weighted edges (T-ST-5b) |
| **D-ST-2** | Field Space F_M(P) and Mass Constraint | in §3.9 | B candidate | — | Foundational state space; replaces Σ_M^K as integration domain |
| **D-ST-3** | K_act as #PersComp Observable | in §3.11 | B candidate | exp01 SUPPORTED (PersComp=2 vs slot=4) | Correct definition; slot-count is regime-conditional approx (T-L1-F under L1-J) |
| **D-ST-4** | Topological Sector B_K, Partition Function Z_K, Kramers Rate | §16 | B candidate (P-F flagged) | exp02-NEB (barrier term) | Z_K and Γ require P-F-A1 (T_* undefined); ΔE barriers computable without P-F-A1 |
| **D-ST-5** | Backprojection, Pullback, Prior/Likelihood Sep (CN5) | §16 | B candidate | exp03 (round-trip=0), exp04 (photo sep.) | E_photo is likelihood, not 5th SCC energy term (CN5-compliant) |
| **T-ST-5a** | Hard-Depth Topological Locking | §16; proof: `tst5a_hard_depth_locking_proof.md` | **A** | exp02-NEB: binary step (ε-bridge) | Disconnected graph → K=2 topologically locked; ΔE=+∞ (state-space disconnection); G1–G4 gaps closed (Session E): G1 Lemma 3 not required (graph topology alone suffices); G2 merger/decay distinction; G3 A-STRICT assumption; G4 threshold convention. No P-F flag |
| **T-OP6-B** | PersRidge Boundary Equivalence (Phase-Sep Regime, H1–H5) | §5.3b; proofs: `working/MF/op_0006_boundary_precision.md §9–§12` | **A** (conditional) | exp06: shadow 5/5 ratio 4.09, blur 5/5 ratio 50.8; Session K: B1–B4 all closed | d_H ≤ 2(α/β)^{1/2} explicit; B1 topological separator CLOSED; B2 curved Hausdorff CLOSED (C<1.37 under H4); B3 stereo conditioning CLOSED (hard-cut D-ST-1); B4 ρ_bd=1/(4ξ) CLOSED (Session J). Promoted Cat B → Cat A Session K 2026-05-06. |
| **T-ST-5b** | Smooth-Depth Barrier Raising | §16; results: `exp02e_single_field_neb_summary.md` | **B** | exp02e (Session F): full_scc β=10 6/6 SUPPORTED (25% increase); gl_only NULL; β=20 3/6 PARTIAL | Narrow claim (Session G sign-off): Requires E_cl + E_sep active (GL alone NULL); intermediate β regime; smooth depth-weighted adjacency. Monotone-in-Δz NOT confirmed. NOT a universal theorem. Cat A: monotonicity + analytical lower bound on barrier gap. P-F flag for Kramers interpretation. |

*Claim counts from CV-1.5.2 (47A/5B/5C/5R = 62 claims): stereo extension adds 1A/6B/1C (post Session E, 2026-05-06). T-ST-5a formally signed off as Cat A (W6 D4 Session E: G1–G4 gaps closed; increments Cat A count). T-OP6-B added as Cat B (§5.3b canonical amendment, Session E). T-ST-5b formally signed off as Cat B (W6 D4 Session G: narrow claim, exp02e evidence; moved from Cat C → Cat B). T-P-F-ε0 promoted Cat A + T-P-F-ε0-K promoted Cat B (W6 D4 Session I, §13 canonical.md; CV-1.7). T-OP6-B promoted Cat B → Cat A conditional under H1–H5 (W6 D4 Session K, 2026-05-06, CV-1.7; blockers B1–B4 all closed). Running total (CV-1.7, at Session K close): **50A/12B/5C/5R = 72 claims, ~69% fully proved.** *(Superseded — current count: 54A/13B/5C/5R = 77 claims; see CV-1.10 count update above.)*

---

### CV-1.7 Canonical Additions — P-F-A1 Stochastic Foundation (W6 D4, 2026-05-06, Sessions H–I)

*T-P-F-ε0 and T-P-F-ε0-K promoted to canonical §13 in Session I. Bodies in `THEORY/working/MF/pf_tstar_langevin.md` §8.5. P-F-A1 axiom remains OPEN.*

| T-ID | Name | Status | Category | Proof | Notes |
|---|---|---|---|---|---|
| **T-P-F-ε0** | Gibbs Measure Continuity at ε=0 (Target B → Target A Weak Convergence) | **canonical Cat A** (Session I, 2026-05-06) | **A** | Steps 1–4 in §8.5: compactness (H1), Z_0>0 (H2+H3), DCT for Z_ε (H4), convergence of expectations. H1–H4 verified in SCC setting. In canonical.md §13 Category A. | μ_ε ⇒ μ_0 weakly as ε→0. **NOT P-F-A1.** Does not prove spectral gap, Eyring-Kramers, T_* existence, or Lions-Sznitman construction. |
| **T-P-F-ε0-K** | Kramers Exponent Stability under Bernoulli Regularization | **canonical Cat B** (Session I, 2026-05-06) | **B** | Conditional on H5 (Morse stability): ΔE_ε = ΔE_0 + ε·ΔR; Γ_B/Γ_A = exp(O(δ)) at phase-separated endpoints. H5 plausible but not globally proved. In canonical.md §13 Category B. | **NOT P-F-A1.** No pre-exponential factor proof. Cat A path: H5 proof + spectral gap. |
| **P-F-A1 (v0)** | Effective Stochastic Temperature T_* Axiom | **OPEN (working/blocker)** | **C (working)** | Open — Package I (4 theorem candidates written Session M; working grade): T-PF-A1-AR, T-PF-A1-SDE, T-PF-A1-GI, T-PF-A1-PE. Canonical promotion target CV-1.8. Package II (Eyring-Kramers) conditional on H5 + T_* registration (OP-0021). | Blocker for D-ST-4 rate claims (Γ, Z_K, π_K). ΔE barriers Cat B without P-F-A1. Working file: `pf_tstar_langevin.md`. Route memo: `working/MF/pf_a1_lions_sznitman_freidlin_route.md`. |

*CV-1.7 count update (Session I): T-P-F-ε0 → Cat A (+1A), T-P-F-ε0-K → Cat B (+1B), P-F-A1 → C working (unchanged). Running total post-Session I: **49A/13B/5C/5R = 72 claims, ~68% fully proved.***

*CV-1.7 count update (Session K, 2026-05-06): T-OP6-B Cat B → Cat A (+1A, −1B; blockers B1–B4 closed). Running total post-Session K: 50A/12B/5C/5R = 72 claims, ~69% fully proved.*

*CV-1.8 count update (Sessions M–N–O, 2026-05-06): T-PF-A1-AR Cat A (+1A); T-PF-A1-SDE Cat A (+1A); T-PF-A1-GI Cat B (+1B); T-PF-A1-PE Cat B (+1B). Running total: 52A/14B/5C/5R = 76 claims, ~68% fully proved.*

*CV-1.9 count update (Session P, 2026-05-06): T-PF-A1-GI Cat B → Cat A (+1A/−1B); T-PF-A1-PE Cat B → Cat A (+1A/−1B). Running total: **54A/12B/5C/5R = 76 claims, ~71% fully proved.** P-F-A1 Package I fully Cat A.*

*CV-1.10 count update (Session R, 2026-05-06): T-K-Select-PF Cat B new (+1B). Running total: **54A/13B/5C/5R = 77 claims, ~70% fully proved.** OP-0005-EQ partially resolved.*

*CV-1.8 candidates registered (Session M, 2026-05-06): T-PF-A1-Affine-Reduction, T-PF-A1-Finite-Reflected-SDE, T-PF-A1-Gibbs-Invariance, T-PF-A1-Poincare-Ergodicity. No count change — pending canonical promotion (Session O).*

*CV-1.8 proof review complete (Session N, 2026-05-06): All four Package I theorems reviewed. Categories after review: T-PF-A1-AR (Cat A — elementary polytope geometry); T-PF-A1-SDE (Cat A — Lions-Sznitman Thm 1 convex case + Tanaka uniqueness, no remaining gaps); T-PF-A1-GI (Cat B → Cat A path: zero-current derivation complete, uniqueness needs Doeblin/Stroock-Varadhan citation); T-PF-A1-PE (Cat B → Cat A path: Payne-Weinberger + explicit Holley-Stroock computation, L²→TV formalization needed). Explicit lower bound: λ_1(π_{T_*}) ≥ (π²/n)·exp(−osc(Ẽ)/T_*) > 0; C_P = n·exp(osc(Ẽ)/T_*)/π². **Promoted to canonical in Session O (CV-1.8).***

*CV-1.8 canonical promotion (Session O, 2026-05-06): T-PF-A1-AR → Cat A; T-PF-A1-SDE → Cat A; T-PF-A1-GI → Cat B; T-PF-A1-PE → Cat B. Running total: 52A/14B/5C/5R = 76 claims, ~68% fully proved.*

*Non-overclaim note (mandatory): T-P-F-ε0 is not P-F-A1. T-PF-A1-AR + T-PF-A1-SDE + T-PF-A1-GI + T-PF-A1-PE constitute P-F-A1 Package I (existence of well-posed SDE + Gibbs invariant measure + Poincaré inequality for any T_* > 0). Eyring-Kramers is Package II (conditional on H5 + T_* registration), not P-F-A1. T_* canonical registration is OP-0021 (W9+).*

---

### CV-1.9 Canonical Additions — P-F-A1 Package I Cat A Completion (W6 D4, 2026-05-06, Session P)

*T-PF-A1-GI and T-PF-A1-PE promoted Cat B → Cat A in Session P. Bodies now in `canonical.md §13 Category A`. Working-file proof detail: `THEORY/working/MF/pf_a1_lions_sznitman_freidlin_route.md`.*

| T-ID | Name | Status | Category | Proof | Notes |
|---|---|---|---|---|---|
| **T-PF-A1-GI** | Gibbs Measure Unique Invariant Measure | **canonical Cat A** (Session P, 2026-05-06) | **A** | Zero-current J[ρ*]=0; Dirichlet form self-adjointness; Neumann heat kernel existence (Aronson 1968, uniformly elliptic on Lipschitz domain) → any invariant ν ≪ Leb ≪ π; L²(π) kernel argument (P_t h=h → Lh=0 → ∇h=0 → h=1). | Promoted from Cat B. Uniqueness via heat kernel + L² kernel (not Stroock-Varadhan). Stationarity (zero-current) unchanged. Does NOT prove convergence rate. |
| **T-PF-A1-PE** | Poincaré Inequality + Exponential Ergodicity | **canonical Cat A** (Session P, 2026-05-06) | **A** | Payne-Weinberger 1960 for bounded convex domains (Steiner symmetrization, no smoothness, applies to polytopes); Holley-Stroock perturbation (self-contained); L²→TV via Cauchy-Schwarz with explicit L²(π) density assumption. Explicit: λ₁ ≥ (π²/n)exp(−osc/T_*). | Promoted from Cat B. TV convergence for L²(π_{T_*}) initial density; L² convergence unconditional for t>0. C_P exponentially large (metastable scaling; correct). |

*CV-1.9 promotion detail (Session P, 2026-05-06): T-PF-A1-GI Cat B → Cat A: uniqueness gap closed by (A) Neumann heat kernel positivity → any invariant ν ≪ π, and (B) self-adjoint L²(π) semigroup fixed-point → trivial kernel → h=1. T-PF-A1-PE Cat B → Cat A: (a) Payne-Weinberger 1960 covers bounded convex domains including polytopes (Steiner symmetrization proof requires only convexity, no boundary smoothness); (b) L²→TV formalized as Cauchy-Schwarz with explicit L²(π_{T_*}) density assumption stated in non-overclaim. **P-F-A1 Package I is now fully Cat A.** Package II (Eyring-Kramers) remains conditional on H5 + T_* registration (OP-0021). Running total: **54A/12B/5C/5R = 76 claims, ~71% fully proved.***

---

### CV-1.10 Canonical Additions — Equilibrium K-Selection (W6 D4, 2026-05-06, Session R)

*T-K-Select-PF promoted from Session Q working candidate to canonical Cat B. Body in `canonical.md §13 Category B`. Working-file source: `THEORY/working/MF/k_select_pf_equilibrium.md` (tightened Session R: K_feas §3.5 added, §5.1 A5 updated). Count: +1B → 54A/13B/5C/5R = 77 claims.*

| T-ID | Name | Status | Category | Proof | Notes |
|---|---|---|---|---|---|
| **T-K-Select-PF** | Equilibrium K-Selection under P-F-A1 Package I | **canonical Cat B** (Session R, 2026-05-06, CV-1.10) | **B** | Measurability: K_act step function on finite graph → Borel. Sector boundary null: ∂B_K ⊆ ∪_v {u(v)=ρ_pers}, codimension-1 in F_M(G), σ_M-null (π_{T_*} ≪ σ_M by T-PF-A1-GI). K_feas = {K : σ_M(B_K)>0} finite non-empty. Stationarity: pushforward of π_{T_*} (T-PF-A1-GI unique invariant) under K_act gives {p_K}. K* = argmin_K F(K;P) = argmax_K p_K. | Addresses OP-0005-EQ only. Does NOT prove Kramers rates (OP-0005-DYN, Package II). Does NOT prove K* unique. Does NOT resolve OP-0008. T_* axiomatic (OP-0021). Cat A path: explicit σ_M-null computation in T-PF-A1-AR coordinates; K_feas per-instance characterization; K_act fixed to D-ST-3. |

*Session Q→R promotion note (2026-05-06): Session Q introduced T-K-Select-PF as working Cat B candidate. Session R tightened sector definition (K_feas §3.5), updated §5.1 assumption A5, and promoted to canonical.md §13 Category B. P-F flag on Z_K RESOLVED by Package I (CV-1.9). OP-0005 3-way split maintained: OP-0005-EQ partially resolved (T-K-Select-PF Cat B), OP-0005-DYN OPEN (Kramers/Package II, W9+), OP-0005-OBS OPEN (observation-conditioned).*

---

### Session S Working Candidates — OP-0005-OBS Observation-Conditioned K-Selection (W6 D4, 2026-05-06, Session S)

*T-K-Select-OBS is a new Cat B candidate using P-F-A1 Package I + T-K-Select-PF + explicit likelihood model LM1–LM3. NOT yet canonical — working-file only. No count change to canonical total (77 claims). Source: `THEORY/working/MF/k_select_obs_posterior.md`.*

| T-ID | Name | Status | Category | Proof | Notes |
|---|---|---|---|---|---|
| **T-K-Select-OBS** | Observation-Conditioned K-Selection via Posterior Sector Mass | **working Cat B candidate** (Session S, 2026-05-06) | **B candidate** | Posterior well-definedness: Bayes on Gibbs prior (Package I) with positive measurable likelihood (LM1–LM3). Posterior sector masses $p_K(\mathfrak{O}_t) = Z_K^{obs}/Z^{obs}$ form probability distribution. $K^*(\mathfrak{O}_t) = \arg\min_K F_\mathrm{obs}(K;\mathcal{P},\mathfrak{O}_t)$. Prior {p_K} recovered when $\mathcal{L}_\mathrm{obs} \equiv 1$. | Addresses OP-0005-OBS only. Does NOT prove Kramers rates (OP-0005-DYN). Does NOT prove temporal K-dynamics. Does NOT prove K* uniqueness. Does NOT resolve OP-0008 (σ-inheritance). $E_\mathrm{photo}$ in likelihood only (CN5). Cat A path: canonicalize likelihood model; verify LM1–LM3; exp54 validation. |

*Session S working note (2026-05-06): T-K-Select-OBS defines observation-conditioned K-selection as Bayesian posterior over Gibbs prior. Mathematical structure complete given Package I + T-K-Select-PF + LM1–LM3. OP-0005-OBS status: OPEN → STRUCTURED (Cat B candidate). OP-0005 overall remains OPEN. CN5 preserved: $E_\mathrm{photo}$ in likelihood only. Stereo bridge: connects to D-ST-5 backprojection $b_t$ and `stereo_observation_framework.md` §4 prior/likelihood separation. exp54 plan written (§8 of working file). Canonical count unchanged at 77 pending promotion review.*

---

### CV-1.8 Canonical Additions — P-F-A1 Package I (W6 D4, 2026-05-06, Sessions M–N–O)

*T-PF-A1-AR and T-PF-A1-SDE promoted to canonical §13 Category A in Session O. T-PF-A1-GI and T-PF-A1-PE promoted to canonical §13 Category B in Session O. Bodies in `THEORY/working/MF/pf_a1_lions_sznitman_freidlin_route.md`.*

| T-ID | Name | Status | Category | Proof | Notes |
|---|---|---|---|---|---|
| **T-PF-A1-AR** | Field Polytope Compact Convex Structure and Affine Reduction | **canonical Cat A** (Session O, 2026-05-06) | **A** | Elementary: polytope intersection; affine isometry via ONB of ker(μ^T); energy smoothness on compact set. All gaps filled in Session N. In canonical.md §13 Category A. | F_M(G) compact convex polytope dim n-1; isometry Φ: C̃ → F_M(G); ∇²Ẽ bounded; ∇Ẽ Lipschitz. Foundational for T-PF-A1-SDE/GI/PE. |
| **T-PF-A1-SDE** | Well-Posedness of Reflected Langevin SDE on Field Polytope | **canonical Cat A** (Session O, 2026-05-06) | **A** | Lions-Sznitman (1984) Thm 1 convex-domain case; Tanaka Gronwall uniqueness; Itô lift to intrinsic form. Authority: CPAM 37(4):511–537. In canonical.md §13 Category A. | Unique strong solution (X_t, K_t); Π_M = QQ^T projection; dK̃_t in normal cone. For any T_* > 0. Does NOT prove Gibbs invariance. |
| **T-PF-A1-GI** | Gibbs Measure is the Unique Invariant Measure | **canonical Cat B** (Session O, 2026-05-06); **promoted Cat A** (Session P, 2026-05-06) | **A** | Zero-current: J[ρ*] = −ρ*∇Ẽ − T_*∇ρ* = 0 algebraically. Dirichlet form identity via IBP. Uniqueness (Session P): Aronson 1968 Neumann heat kernel → ν ≪ Leb ≪ π; L²(π) kernel: P_t h=h → Lh=0 → ∇h=0 → h=1. In canonical.md §13 Category A. | π_{T_*} = Z^{-1}exp(−E/T_*)dσ_M unique invariant measure. Z finite (compact). Does NOT prove convergence rate. |
| **T-PF-A1-PE** | Poincaré Inequality and Exponential Ergodicity | **canonical Cat B** (Session O, 2026-05-06); **promoted Cat A** (Session P, 2026-05-06) | **A** | Payne-Weinberger (1960) on C̃: μ_1 ≥ π²/n (Steiner symmetrization, covers polytopes, no smoothness needed). Holley-Stroock perturbation: gap(π_{T_*}) ≥ (π²/n)·exp(−osc(Ẽ)/T_*). L²→TV (Session P): Cauchy-Schwarz with explicit L²(π_{T_*}) density assumption. In canonical.md §13 Category A. | λ_1 ≥ (π²/n)·exp(−osc(Ẽ)/T_*) > 0; C_P = n·exp(osc/T_*)/π²; exponentially large for metastable systems (acceptable: P-F-A1 requires existence, not polynomial bound). |

*CV-1.8 count update (Sessions M–N–O, 2026-05-06): T-PF-A1-AR → Cat A (+1A); T-PF-A1-SDE → Cat A (+1A); T-PF-A1-GI → Cat B (+1B); T-PF-A1-PE → Cat B (+1B). Running total: 52A/14B/5C/5R = 76 claims, ~68% fully proved. (Historical — superseded by CV-1.9 count update above.)*

---

### Canonical Spec v1.5.2 (2026-05-02) — Current Version (W6: L1-F Hard-Bar / Active-Count Bridge Conditional Cat-A)

**Additions over v1.5.1** (W6, 2026-05-02):

| T-ID | Name | Status | Category | Source | Proof | Experiments | Notes |
|------|------|--------|----------|--------|-------|-------------|-------|
| **T-L1-F** | Hard-Bar / Active-Count Bridge under L1-J Regime | accepted | A (conditional under L1-J package) | C-0721 | P-0721 | (theoretical via L1-A..L1-L chain; numerical L1-I 439/1920 FEASIBLE_WITH_BUDGET on $T^2_{20}$; L1-H2 stress tests 5/5; L1-J PO-1 decay-to-cut 6/6; L1-K external audit passed) | Conditional theorem on finite shared-pool multi-formation states under hypothesis package $(P0)$–$(P11)$: $K_{\mathrm{bar}}^{\ell_{\min}}(U(\mathbf u);G)=K_{\mathrm{act}}^{\varepsilon}(\mathbf u)$ AND labeled bijection $\mathcal A_{\mathrm{bar}}:A^\varepsilon\to\mathrm{Bars}_0^{\mathrm{term}}(U;G)$ via primary representative $q_j^U=\arg\max^\prec_{x\in N_j^r}U(x)$. NOT a global identity; explicit hypothesis package required. P7 decay-to-cut adopted as safe technical regime hypothesis; L1-L provides Combes-Thomas / discrete Agmon backing under strong stationarity (P7_DERIVED_UNDER_STRONG_STATIONARITY) but P7 is not asserted for all SCC states. Does NOT solve OP-0005 (K-Selection) or OP-0008 ($\sigma^A$ K-jump non-determinism). Does NOT establish $K_{\mathrm{soft}}^\phi=K_{\mathrm{act}}$ (additionally requires $\phi\in\Phi_{\mathrm{res}}$ per WQ-LAT-1.B). Does NOT claim $\sigma_{\mathrm{rich}}$ sufficiency. Reservoir theory not promoted to canonical. |

**v1.5.1 → v1.5.2 release notes (2026-05-02)**:

- **Added (1 new C-ID)**: 1 Cat A conditional (T-L1-F) synthesizing the L1-A..L1-L chain.
- **Hypothesis package (P0)–(P11)**:
  - P0 terminal-death $H_0$ superlevel persistence convention (code-aligned with `scc.diagnostics._persistence_h0_graph`);
  - P1 deterministic tie convention (fixed total order $\prec$ on $X$; ties in descending-$U$ broken by ascending $\prec$);
  - P2 active mass + connected $\delta$-support;
  - P3 disjoint active neighborhoods $N_j^r\cap N_k^r=\emptyset$;
  - P4 low boundary collar $\max_{\partial N_j^r}U\le b_j-\ell_{\min}-r_{\mathrm{assoc}}$;
  - P5 background suppression $\|U\|_{\infty,X_{\mathrm{bg}}}\le\ell_{\min}-\rho_{\mathrm{bg}}$ (on $U$, not just on $R_{\mathrm{inact}}$);
  - P6 birth height $b_j\ge h_{\min}\ge\ell_{\min}$;
  - P7 decay-to-cut (heterogeneous form): $u^{(\ell)}(x)\le\psi_\ell(d_G(x,S_\ell^\delta))$ and $H_{C_{jk}}(U)\le\sum_{\ell\in A}\psi_\ell(q_{\ell,jk})+\|R_{\mathrm{inact}}\|_{\infty,C_{jk}}$;
  - P8 tightened H6 on $G_j^r$: $\ell_{j,2}(u^{(j)};G_j^r)\le\ell_{\min}-3\rho_{\mathrm{pert}}$;
  - P9 NE-2 perturbation $\|R_j\|_{\infty,N_j^r}\le\rho_{\mathrm{pert}}/2$;
  - P10 inactive residual suppression $\|R_{\mathrm{inact}}\|_\infty\le\ell_{\min}-\rho_{\mathrm{res}}$;
  - P11 margin ledger $h_{\min}-\max_{k\neq j}B_{jk}\ge\ell_{\min}+r_{\mathrm{assoc}}+r_{\mathrm{birth}}$.
- **L1 chain provenance**: L1-A merge / death / contact level; L1-B cut bound; L1-C slot-to-bar + terminal-death convention; L1-D no-extra-bar / secondary-bar suppression; L1-E inactive suppression; L1-F synthesis; L1-G empirical diagnostic; L1-H local-to-global transfer; L1-H2 boundary-leakage proof (Lemma 1: $\ell_{\mathrm{glob}}\le\ell_{\mathrm{loc}}$ from graph inclusion); L1-I constants feasibility (439/1920 FEASIBLE_WITH_BUDGET); L1-J Cat-A attempt; L1-K external audit (THEOREM_CANDIDATE_STRONG_AUDIT_PASSED); L1-K-REPAIR (4 proof-hygiene repairs R-1, R-2, R-3, R-4 applied); L1-L P7 status decision.
- **Counts**: 45A → **46A** (+1 conditional Cat A — T-L1-F at CV-1.5.2 release 2026-05-02), 60 → **61 claims**, 75% → **75% fully proved** (unchanged %). *(W6 D1 EOD post-supervision addition 2026-05-04: T-L1-M Soft-Count Corollary under $\Phi_{\mathrm{res}}$ following T-L1-F promoted as supervised special-case after external L-M-K-style audit PASS. Net post-W6-D1-EOD: 46A → **47A** (+1 conditional Cat A), 61 → **62 claims**, 75% fully proved unchanged. C-0722 row added in Active Claims table; CHANGELOG W6 D1 EOD second addendum.)*
- **Non-claims preserved**: no global $K_{\mathrm{bar}}=K_{\mathrm{act}}$; no global $K_{\mathrm{soft}}=K_{\mathrm{act}}$; no OP-0005 or OP-0008 solution; no $\sigma_{\mathrm{rich}}$ sufficiency; reservoir theory not promoted to canonical; P7 not generally derived from all SCC states; no application / vision / robotics claims.
- **Source**: `THEORY/working/MF/kbar_kact_bridge_L1A..L1L_*.md` (full L1 chain — 13 working documents); `CODE/scripts/l1g_l1hyp_diagnostic.py`, `l1h_local_to_global_counterexample.py`, `l1h2_boundary_leakage_counterexample.py`, `l1i_constants_feasibility.py`, `l1j_bridge_cut_decay_diagnostic.py` (5 diagnostic / counterexample scripts); `CODE/scripts/results/l1*.json`.
- **canonical.md growth**: ~25 lines added in §13 Category A (T-L1-F entry).

### Canonical Spec v1.5.1 (2026-04-29) — Previous Version (W5 Day 3 EOD: D-6a Multi-Static + Ontological Depth + Critic 보강)

**Additions over v1.5** (W5 Day 3 EOD, 2026-04-29):

| T-ID | Name | Status | Category | Source | Proof | Experiments | Notes |
|------|------|--------|----------|--------|-------|-------------|-------|
| **T-Commitment-14-Multi-Static** | Multi-Formation σ-Signature on K-field (Static) | accepted | A definitional | C-0717 | P-0717 | (theoretical extension of Commitment 14) | Defined on $\widetilde{\Sigma}^{K_{\mathrm{field}},\circ}_M$ interior (Option A pragmatic; corners deferred to NQ-248 W7+). $\sigma_{\mathrm{multi}} = (\sigma^A, \sigma^D)$ joint invariant under wreath-product $\mathrm{Aut}(G) \wr S_{K_{\mathrm{act}}}$ |
| **T-σ-multi-A-Static** | Within-Formation σ-Tuple Multi-Set Invariance | accepted | A (well-separated regime) | C-0718 | P-0718 | (theoretical via Coupling Bound Lemma + T-σ-Lemma-1) | Multi-set $\{\sigma_j\}_{j=1}^{K_{\mathrm{act}}}$ under $S_{K_{\mathrm{act}}}$ permutation; reduces to Commitment 14 σ at $K_{\mathrm{act}}=1$. Cat B target in T-Persist-K-Weak overlap regime |
| **T-σ-multi-D-Static** | Between-Formation Cohomology Pull-Back | accepted | A definitional | C-0719 | P-0719 | (wreath-product representation theory, Specht 1935 + James-Kerber 1981) | Conjugacy-class label in $H^1(\mathrm{Aut}(G) \wr S_{K_{\mathrm{act}}}; \mathrm{Stab}(\mathbf{u}^*))$. Explicit cohomology computation (D_4 × S_2 etc.) Cat B target via NQ-242d W6+ |
| **T-σ-Multi-1** | Multi-Formation Goldstone-Pair Instability (Phase 4 Static) | tentative | B target | C-0720 | (sketch) | (Phase 4 D-6a numerical, Phase 6 Q1 box-clipping) | Goldstone-pair separation $\Delta\lambda \approx O(\lambda_{\mathrm{rep}} e^{-c_0 D_{\mathrm{sep}}})$ under V5b-T per-formation regime. Static instability iff $\lambda_{\mathrm{rep}} > c_{\mathrm{eff}} \mu_{\mathrm{Gold}}^{\mathrm{single}}$. Cat A pending NQ-242 numerical anchor |

**Sub-statement additions to T-V5b-T**:

| Sub-ID | Name | Status | Category | Notes |
|--------|------|--------|----------|-------|
| **(V5b-F-empirical)** | V5b-F Goldstone Mass Scaling | accepted | B target | $\mu_{\mathrm{Gold}}^{\mathrm{V5b-F}} \approx C(\beta) \cdot \|\partial S\|/n$, $C(\beta=4, \xi_0=0.5) \approx 13.2 \pm 0.4$ (NQ-198a 6 corner-sat, SNR 35). Refutes Phase 3 heuristic + Day 3 §4 derivation. Full $C(\beta, \xi_0)$ open via NQ-198k W6+ |
| **(V5b-T-zero)** | Sub-Spinodal Translation-Invariant Regime | accepted | A definitional | $\mu_{\mathrm{Gold}}^{\mathrm{V5b-T-zero}} = 0$ exactly (discrete translation orbit on $\mathbb{Z}_L^d$). Replaces V5b-T' WITHDRAWN. Empirical anchor NQ-198f $T^2_{20}/T^2_{28}$ $|\mu| \leq 0.028$ within FD numerical noise |

**Status changes to existing entries**:

| C-ID | Name | Old Status | New Status | Reason |
|------|------|-----------|-----------|--------|
| **C-0716** | T-σ-Theorem-4 σ at First Pitchfork | Cat A in $\epsilon$-small regime | **Cat B in $\epsilon$-small regime** | Retroactive Critic 7-agent verdict 2026-04-29: Errata Round 1 caught structural error in original (ii) ("would-be transverse Goldstone" inapplicable to discrete sym breaking); original Cat A merge had unresolved Morse-index contradiction. Higher-order $\epsilon$ splitting NQ-187 W7+ may re-promote. |
| **D-5 (V5b-T' new entry candidate)** | V5b-T' Pre-Objective Goldstone (Phase 3 proposal) | Cat B target proposal | **WITHDRAWN** | NQ-198f phantom on torus (μ ≈ 0 exact, not PN-barrier-lifted O(β)). Replaced by V5b-T-zero sub-statement. |

**v1.5 → v1.5.1 release notes (2026-04-29)**:

- **Added (4 new C-IDs)**: 3 Cat A definitional (Multi-Static + multi-A-Static + multi-D-Static) + 1 Cat B target (Multi-1).
- **Added (sub-statements)**: V5b-T-zero (Cat A def, replaces V5b-T' phantom) + V5b-F-empirical (Cat B target) within T-V5b-T entry.
- **Status revision**: T-σ-Theorem-4 Cat A → Cat B retroactive (Critic 보강).
- **Withdrawn**: D-5 V5b-T' new entry candidate (NQ-198f phantom finding).
- **Counts**: 43A → **45A** (net +2: +3 D-6a Cat A − 1 Theorem-4 격하), 4B → **5B** (+1 Theorem-4 + 1 Multi-1 vs −1 hypothetical), 57 → **60 claims**, 75% → **75% fully proved** (unchanged % due to balanced category shift).
- **Commitment 16 K-status** added to §11.1 (K_field architectural cap / K_act dynamic stratum index two-tier decomposition; resolves 4-month K ontological ambiguity per OP-0009). *(Erratum 2026-05-04 W6 D1 G3 audit: K_act default ε convention clarified — $\bar m := M / K_{\mathrm{field}}$ is the architectural per-formation mean. Standard $T^2_{20}$ regime $M=90, K_{\mathrm{field}}=4 \Rightarrow \bar m = 22.5, \epsilon = 0.225$, matching production-script default and T-L1-F's L1-I "439/1920" empirical anchor. See canonical.md line 810 amendment + CHANGELOG 2026-05-04 W6 D1 G3 entry.)*
- **Commitment 14 (O5')(O7) sub-conventions** added (multi-irrep ordering + tie-breaking via Mulliken character order).
- **CN6 refined** (line 1603): "K kinetically determined" now refers specifically to K_act per Commitment 16.
- **Open problems**: OP-0008 σ^A K-jump non-determinism + OP-0009 Multi-Formation Ontological Foundations registered; OP-0003 MO-1 re-activation rider added.
- **canonical.md growth**: 1593 → 1664 lines (~71 lines added).
- **Source**: `THEORY/logs/daily/2026-04-29/04..11_*` (Day 3 deepening + numerical + 7-agent + 4-agent ontological depth analysis); `THEORY/working/MF/K_status_commitment.md` (OAT-1 Commitment 16 audit); `THEORY/CHANGELOG.md` 2026-04-29 entry.

### Canonical Spec v1.5 (2026-04-27) — Previous Version (W5 Day 1: σ-Framework Supporting Structures)

**Additions over v1.4** (W5 Day 1 G0, 2026-04-27):

| T-ID | Name | Status | Category | Source | Proof | Experiments | Notes |
|------|------|--------|----------|--------|-------|-------------|-------|
| **T-σ-Lemma-1** | σ-Framework Irrep Decomposition Well-Defined | accepted | A | C-0712 | P-0712 | (theoretical, finite-group rep theory) | Hessian commutes with $G_u$-action; isotypic decomposition via Maschke + Schur; finite-graph hypothesis essential; trivial-stabilizer case vacuous |
| **T-σ-Lemma-2** | σ-Framework Nodal Count Properties | accepted | A (i,ii,iii,iv) + C (v,vi conditional) | C-0713 | P-0713 | (theoretical + W4-04-25 NQ-141 32×32 numerical) | Graph-intrinsic + Aut(G)-equivariance + lower bound $\geq 2$ + sign-flip Cat A; Courant upper bound + $G_u$-orbit divisibility Cat C |
| **T-σ-Lemma-3** | Goldstone–ℓ=1 Angular Saturation | accepted | A (continuum) | C-0714 | P-0714 | W4-04-26 NQ-170c 2D torus L=20 ζ=0.5 (overlap 0.97) | IBP identity $\mathcal{P}_{\ell=1}[\delta u_x] = (-c_d \int u^*(r)\, dr, 0)$ *(corrected per canonical.md Errata Round 1, 2026-04-27 evening; original brief stated $(-m, 0)$ which was a Jacobian error)*; Goldstone basis automatically ℓ=1; nodal count = 2 universal (anchors T-V5b-T-(e)) |
| **T-σ-Theorem-3** | σ at Uniform on $D_4$ Free-BC Grid (Closed Form) | accepted | A | C-0715 | P-0715 | exp_hessian_uniform_v2 (NQ-141 W4-04-25, $L = 4$ to $32$, $< 10^{-9}$ precision) | $\mu_k = 4\alpha\lambda_k^{\mathrm{Lap}} + \beta W''(c)$; full $D_4$ irrep table on cosine basis; $\mathcal{N}(\phi_{(p,q)}) = (p+1)(q+1)$. *(Erratum 2026-04-27 Round 1: §13 worked example originally listed irrep label A_1 for the $(1,1)$ singlet; corrected to B_2.)* |
| **T-σ-Theorem-4** | σ at First Pitchfork on $D_4$ Free-BC Grid (Leading Order, **continuum-limit claim**) | Cat A at CV-1.5; **Cat A → Cat B retroactive at CV-1.5.1 (2026-04-29)** per Critic 7-agent verdict (Errata Round 1 Morse-index inconsistency at merge time). **Continuum vs discrete grid caveat added 2026-05-04 W6 NQ-187 audit** (canonical.md §13 T-σ-Theorem-4 entry now contains explicit continuum-vs-discrete note): canonical statement (ii) — leading-order degeneracy $\mu_0 = \mu_1 = 4\|W''(c)\|\epsilon$ from $A_2/A_1 = 4$ — is a continuum-limit prediction (R22 §3.3 Lebesgue integral on unit square) **not realized on finite discrete grids** $L \le 16$. NQ-187 numerical (`logs/daily/2026-04-30/11_nq187_scaling_test_results.md`, script `CODE/scripts/test_sigma_theorem4_scaling.py`, $L \in \{4, 8, 16\}$, $\epsilon \in \{0.001..0.1\}$, analytic sparse $\Sigma_m$-Hessian + shift-invert Lanczos): measured $\mu_0/\epsilon \approx 1$, $\mu_1/\epsilon \approx 2$, ratio $\mu_1/\mu_0 \approx 2$ (not $1$ degeneracy) and exponent $p \approx 1.03$ (not $p = 2$ predicted, not $p = 3/2$ alternative). Three reconciliation hypotheses (α continuum extrapolation $L \to \infty$, β R22 derivation re-audit, γ $\Sigma_m$-Hessian convention) under audit. Cat A re-promotion deferred to CV-1.7+ post-γ/β/α path closure. | B (was A in $\epsilon$-small regime at CV-1.5) | C-0716 | P-0716 | (theoretical via T-Birth-Parametric + R22 axis-aligned, continuum-limit; numerical NQ-187 on discrete grid) | $D_4 \to \mathbb{Z}_2$ symmetry breaking; continuum prediction Mode 0 trivial irrep / Mode 1 sign irrep both with eigenvalue $4\|W''(c)\|\epsilon$ (degenerate at continuum leading order); on discrete $L \le 16$ grid measured $\mu_1/\mu_0 \approx 2$ and effective coefficient $\approx 1$ (not $4$). $\mathcal{F}$ tie-break NQ-143/NQ-184. Statement now read as **continuum-limit claim** until γ/β/α audit closes. |

**v1.4 → v1.5 release notes (2026-04-27)**:
- Added: 5 Cat A entries (T-σ-Lemma-1 + T-σ-Lemma-2 + T-σ-Lemma-3 + T-σ-Theorem-3 + T-σ-Theorem-4) — σ-framework supporting structures grounding Commitment 14.
- Decision: Option α (5 separate entries) per W5 strategic plan §0.4 Decision 1 default; rationale "mathematically independent statements deserve individual canonical visibility".
- Counts: 38A → **43A**, 52 claims → **57 claims**, 73% → **75% fully proved**.
- T classification update: T1 = 3 → **8** (Lemma 1, 2, 3, Theorem 3, 4 each individually T1 per Option α). T2 reduced (σ supporting structures moved out of T2).
- Sub-statement caveats canonically registered: T-σ-Lemma-2 internal Cat A/C split (sub-statements (v) Courant + (vi) orbit divisibility are Cat C riders within the Cat A entry); T-σ-Theorem-4 explicit "in $\epsilon$-small regime" qualifier; T-σ-Lemma-3 explicit "in continuum limit" qualifier.
- Pre-brainstorm corrections folded in: Lemma 1 finite-graph hypothesis explicit; Lemma 2 sub-statement (iii) reframed as lower-bound-from-$\mathbf{1}^\perp$ (was incorrectly stated as "$n_k = 1$ iff constant" in plan templates); Lemma 3 IBP interpretation B (δu^ref = unit vector in ℓ=1 angular subspace) adopted.
- σ-framework now fully canonical-grounded: definitional Commitment 14 + irrep apparatus (T-σ-Lemma-1) + nodal count (T-σ-Lemma-2) + Goldstone–ℓ=1 saturation (T-σ-Lemma-3) + worked examples on uniform (T-σ-Theorem-3) and post-bifurcation (T-σ-Theorem-4) configurations.
- **Source:** `THEORY/logs/daily/2026-04-27/01_sigma_lemmas_review.md` (decision packet) + `01a-01e` (per-statement files); `THEORY/canonical/canonical.md` §13 (T-σ-Lemma-1 ~ T-σ-Theorem-4 entries inserted after T-V5b-T at lines 1169-1283); `THEORY/CHANGELOG.md` 2026-04-27 entry.

### Canonical Spec v1.4 (2026-04-26) — Previous Version (W4 Extended Close)

**Additions over v1.3** (W4 extended close, 2026-04-26):

| T-ID | Name | Status | Category | Source | Proof | Experiments | Notes |
|------|------|--------|----------|--------|-------|-------------|-------|
| **T-V5b-T** | Pre-Objective Goldstone on Translation-Invariant Graphs | accepted | A | C-0710 | P-0710 | E-0095 (NQ-170b ζ-scan) + E-0096 (NQ-170c graph-class extension + nodal count) + E-0097 (NQ-172 reproducibility) | Sub/super-lattice dichotomy on translation-invariant graphs (torus T^d, cycle C_n); 2D 2-fold doublet with commensurability split; 1D 1-fold Goldstone; ζ_*(G) graph-class dependent; Goldstone nodal count = 2 universal |

**v1.3 → v1.4 release notes (2026-04-26)**:
- Added: 1 Cat A theorem (T-V5b-T) — V5b verification cycle (8 iterations) result.
- Counts: 37A → **38A**, 51 claims → **52 claims**, 73% → **73% fully proved**.
- T classification update (W4 weekly_summary §3): T1 = 2 → **3** (added V5b-T); T2 = 5 → 4 (V5b moved to T1); T3 = 3 → **4** (added V5b-F new finding).
- New finding registered: V5b-F (Partial Goldstone on Boundary-Modified Graphs) — Cat C, NQ-173 carry.
- Reproducibility crisis identified+resolved: NQ-172 (mode-indexing artifact in NQ-170 analysis script).
- W4 scope extended: 2026-04-19 ~ **2026-04-26** (8 days). Per user direction "아직 내용은 전부 W4로 간주해" — 04-26 work is W4 final-day continuation.

### Canonical Spec v1.3 (2026-04-25) — Previous Version (Frozen)

**Additions over v1.2** (W4 merge, 2026-04-19 ~ 2026-04-25):

| T-ID | Name | Status | Category | Source | Proof | Experiments | Notes |
|------|------|--------|----------|--------|-------|-------------|-------|
| **T-PreObj-1** | Pre-Objective Multi-Peak Formation Mechanism | accepted | A | C-0700 | P-0700 | E-0090 (L=12 numerical, 3-digit agreement) + E-0091 (L=32 dichotomy) | F=1 single-disk minimizer non-critical under full SCC; gradient flow attracts to multi-peak F≥2; IC-protocol dichotomy (adaptive bounded vs random ~ L^2.8) |
| **T-PreObj-1G** | Pre-Objective Mechanism Graph-Class Independent | accepted | A | C-0701 | P-0701 | (theoretical, qualitative empirical) | Conclusions (i),(ii) of T-PreObj-1 hold on **any finite connected graph** under (G1)–(G4) hypotheses |
| **Lemma 4** | Quadratic Form Positive Definite (M matrix) | accepted | A | C-0702 | P-0702 | E-0090 | M ∈ R^{2x2} of (g_cl, g_sep) gradients, PD under linear independence; destabilization magnitude Lambda^T M Lambda > 0 |
| **F-1 Resolution Corollary** | F-1 SPLIT-RESOLVED via T-Merge(b) + T-PreObj-1 | accepted | A | (corollary) | (corollary) | — | Pure E_bd portion via T-Merge(b); full SCC portion via T-PreObj-1 (i); see theorem_status.md OP-0001 |

**v1.2 → v1.3 release notes (2026-04-25):**
- Added: 2 Cat A theorems (T-PreObj-1, T-PreObj-1G), 1 Cat A lemma (Lemma 4), 1 Cat A corollary (F-1 split-resolution).
- Status changes: C-0550 (F-1), C-0551 (M-1), C-0552 (MO-1) — challenged → resolved/clarified/sidestepped (see Active Claims table below).
- Counts: 35A → **37A**, 49 claims → **51 claims**, 71% → **73% fully proved**.
- Critical blockers: 3 (F-1, M-1, MO-1) → **0** (all resolved/clarified/sidestepped).
- Pending W4 merge (user decision required, deferred): T2 candidates including σ-framework (Lemma 1/2/3, Theorem 3/4), Theorem 1 V5b, Axiom S1' v1, CN15/16/17, Commitment 14/15 v2.

### Canonical Spec v1.2 (2026-04-12) — Previous Version (Frozen)

| T-ID | Name | Status | Category | Source | Proof | Experiments | Notes |
|------|------|--------|----------|--------|-------|-------------|-------|
| **T-1** | Existence of Minimizers | accepted | A | C-0001 | P-0001 | E-0001, E-0002 | SCC minimizer always exists on Σ_m |
| **T-3** | Stability of Interior Minimizers | accepted | A | C-0003 | P-0003 | E-0003 | Hessian positive on interior; local stability |
| **T-6a** | Closure Fixed Point (Existence) | accepted | A | C-0006a | P-0006a | E-0005 | u* = Cl_t(u*) ∃ for all parameters |
| **T-6b** | Closure Fixed Point (Stability) | accepted | A | C-0006b | P-0006b | E-0006 | Closure FP is attracting in stability metric |
| **T-6-Stability** | Stability of Closure FP | accepted | A | C-0006c | P-0006c | E-0007 | Full spectral analysis |
| **T-7** | Enhanced Metastability | accepted | A | C-0007 | P-0007 | E-0008, E-0009 | Residence time > expected near saddle |
| **T-8-Core** | Phase Transition (Core Dominance) | accepted | A | C-0008 | P-0008 | E-0010, E-0011 | Binuclear → mononuclear at critical β |
| **T-8-Full** | Phase Transition (Global) | accepted | A | C-0009 | P-0009 | E-0012, E-0013 | Full energy landscape bifurcation |
| **T-11** | Γ-Convergence | accepted | A | C-0011 | P-0011 | E-0014 | Variational convergence under scaling |
| **T-14** | Gradient Flow | accepted | A | C-0014 | P-0014 | E-0020:E-0022 | Gradient descent converges to minimizer |
| **T-20** | Axiom Consistency | accepted | A | C-0020 | P-0020 | E-0025 | Axioms A1–E mutually consistent |
| **C-Axioms** | Cohomology-Resolvent Alignment | accepted | A | C-0101 | P-0101 | E-0030:E-0032 | C3'' symmetrization complete (upgraded 04-03) |
| **QM-1** | Quantum Mechanical Analogy (Eigenvalue) | accepted | A | C-0110 | P-0110 | E-0040 | Fiedler eigenvalue is binding edge |
| **QM-2** | QM-2 (Spectral Gap) | accepted | A | C-0111 | P-0111 | E-0041 | Spectral gap related to phase transition |
| **QM-3** | QM-3 (Perturbation) | accepted | A | C-0112 | P-0112 | E-0042 | Perturbations stay confined |
| **QM-4** | QM-4 (Commutation) | accepted | A | C-0113 | P-0113 | E-0043 | Operator commutation holds generically |
| **T-Bind-Proj** | Tangential Residual Bound at Constrained Minimizers | accepted | A (for all τ_cl ∈ (0,1)) | C-0200 | P-0200 | E-0050:E-0052 | Phase 13 upgrade applied 2026-04-07 (Erratum, see canonical.md §13 line 1440 and Cat B section erratum line 1481): T-Bind-Proj/Full moved to Category A. Bound: $\|r_T\|_2 \le (\lambda_{\mathrm{sep}} G_{\mathrm{sep}} + \lambda_{\mathrm{bd}} G_{\mathrm{bd}}) / (2\lambda_{\mathrm{cl}}(1-a_{\mathrm{cl}}/4)) + (1+a_{\mathrm{cl}}/4)\sqrt{n}\,\bar r_0/(1-a_{\mathrm{cl}}/4)$. Proof: KKT projection + Banach inversion of restricted operator with $\sigma_{\min} \ge 1-a_{\mathrm{cl}}/4$; general τ via binary mass-balance formula $\Phi(\tau; a_{\mathrm{cl}}, c)$. *(Brief corrected 2026-05-04 W6 G2 audit; previously listed Cat B with τ=1/2 restriction, which contradicted canonical and was the result of the Phase 13 upgrade not being propagated to this index.)* |
| **T-Bind-Full** | Bind Lower Bound at Constrained Minimizers | accepted | A | C-0201 | P-0201 | E-0053 | Phase 13 upgrade applied 2026-04-07 (Erratum, see canonical.md §13 line 1445 and Cat B section erratum line 1481): T-Bind-Full moved to Category A. Statement: $\mathsf{Bind}(\hat u) \ge 1 - f(\text{params})$, $n$-independent when parameters are $O(1)$. Proof: follows from T-Bind-Proj + universal gradient bounds. *(Brief corrected 2026-05-04 W6 G2 audit; previously listed Cat C "very conditional, full τ dependence unclear", which contradicted canonical.)* |
| **Predicate-Energy Bridge** | Energy ↔ Diagnostic Alignment | accepted | A | C-0300 | P-0300 | E-0060:E-0063 | Energy minimization ↔ diagonal optimization (upgraded 04-03) |
| **Deep Core Dom. 2b** | Deep Core Dominance | accepted | A | C-0301 | P-0301 | E-0064, E-0065 | Core is always dominant in asymmetric regime (upgraded 04-03) |
| **T-Persist-1(a)** | Transport Persistence (base) | accepted | C | C-0400 | P-0400 | E-0070 | Conditional: assumes generic parameters |
| **T-Persist-1(b)** | Transport Persistence (basin unconditional) | accepted | A | C-0401 | P-0401 | E-0071, E-0072 | Unconditional: genericity automatic (upgraded 04-03) |
| **T-Persist-1(d)** | Transport Persistence (fixed stratum) | accepted | C | C-0402 | P-0402 | E-0073 | Conditional: on fixed active stratum |
| **T-Persist-1(e)** | Transport Persistence (confinement) | accepted | A | C-0403 | P-0403 | E-0074 | Tight confinement bound (upgraded 04-03) |
| **T-Persist-Full** | Transport Persistence (full composition) | accepted | C | C-0404 | P-0404 | E-0075 | Conditional on multiple regime conditions |
| **T-Persist-K-Sep** | K-field Persistence (well-separated) | accepted | B | C-0500 | P-0500 | E-0076, E-0077 | Conditional: on well-separated regime + per-formation persist |
| **T-Persist-K-Weak** | K-field Persistence (weak coupling) | accepted | C | C-0501 | P-0501 | E-0078 | Conditional: on weakly-interacting regime |
| **T-Persist-K-Unified** | K-field Persistence (parametric) | accepted | B | C-0502 | P-0502 | E-0046, E-0047 | Parametric family (Sep/Weak/Strong); 100% validation (new v1.2) |

---

## Active Claims (Not Yet Canonical) / Resolved Claims

| C-ID | Name | Status | Category (Intended) | Proof (P-ID) | Experiments | Notes |
|------|------|--------|---------|----------|-------------|-------|
| **C-0550** | F-1: K=2 Vacuity Problem | ✅ **SPLIT-RESOLVED (2026-04-24)** | A | P-0700 + T-Merge(b) | E-0090, E-0091 | Pure E_bd portion: T-Merge(b) Cat A pre-existing. Full SCC portion: T-PreObj-1 (i) Cat A. See theorem_status.md OP-0001. |
| **C-0551** | M-1: K=1 Always Preferred | ✅ **LAYER-CLARIFIED (2026-04-24)** | A | T-Merge(b) | none | Proved theorem (T-Merge(b)) misframed as problem. Pure E_bd: theorem holds. Full SCC: comparison not framed (Theorem 2 makes F=1 non-critical). |
| **C-0552** | MO-1: Morse Theory Invalid | ⚪ **SIDESTEPPED (2026-04-24)** | A (single-formation) | (sidestep) | none | Single-formation σ-framework operates on Σ_m (no corners). Multi-formation extension to Σ^K_M still open (Phase 5). |
| **C-0553** | Type A/B Classification | challenged | OP | exp65 | E-0065 | exp65 invalidates; Type B never observed (unchanged from v1.2). |
| **C-0600** | K-field Model Selection | tentative (partially addressed) | pending | none | exp66:exp73 | W4 σ-framework + Static/Dynamic Separation (CN15 candidate) provides partial answer; full mechanism still open. |
| **C-0700** | T-PreObj-1 Pre-Objective Mechanism | ✅ **accepted Cat A** | A | P-0700 | E-0090, E-0091 | New 2026-04-24. F=1 disk non-criticality + multi-peak attractor + IC-protocol dichotomy. |
| **C-0701** | T-PreObj-1G Graph-Class Independent | ✅ **accepted Cat A** | A | P-0701 | (theoretical) | New 2026-04-24. Conclusions (i),(ii) hold on any finite connected graph under (G1)–(G4). |
| **C-0702** | Lemma 4 Quadratic Form PD | ✅ **accepted Cat A** | A | P-0702 | E-0090 | New 2026-04-24. M positive definite under g_cl, g_sep linear independence. |
| **C-0710** | T-V5b-T Pre-Objective Goldstone on Translation-Invariant Graphs | ✅ **accepted Cat A** | A | P-0710 | E-0095, E-0096, E-0097 | New 2026-04-26 (W4 extended). Sub/super-lattice spectral dichotomy on torus T^d / cycle C_n; 2D commensurability split; 1D Goldstone; nodal count = 2 universal. After 8 V5b iterations (V1 → V5b''). |
| **C-0711** | V5b-F Partial Goldstone on Boundary-Modified Graphs | tentative | C | P-0711 | E-0096 (free BC partial) | New 2026-04-26 (W4 extended). Cat C new finding. NQ-173 quantification carry. |
| **C-0712** | T-σ-Lemma-1 σ-Framework Irrep Decomposition Well-Defined | ✅ **accepted Cat A** | A | P-0712 | (theoretical, Maschke + Schur orthogonality) | New 2026-04-27 (W5 Day 1 G0). Hessian-$G_u$ commutation + canonical isotypic projector. Finite-graph hypothesis essential. |
| **C-0713** | T-σ-Lemma-2 σ-Framework Nodal Count Properties | ✅ **accepted Cat A** (i,ii,iii,iv) + Cat C riders (v,vi) | A/C-split | P-0713 | NQ-141 (W4-04-25 R23 32×32 empirical) | New 2026-04-27 (W5 Day 1 G0). Lower bound $\mathcal{N} \geq 2$ corrected from "constant" template; orbit divisibility restricted to non-invariant case. |
| **C-0714** | T-σ-Lemma-3 Goldstone–ℓ=1 Angular Saturation | accepted Cat A in continuum | A | P-0714 | NQ-170c (W4-04-26 2D torus ζ=0.5 overlap 0.97) | New 2026-04-27 (W5 Day 1 G0). IBP saturation identity $\mathcal{P}_{\ell=1}[\delta u_x] = (-c_d \int u^*(r)\, dr, 0)$ *(Erratum 2026-04-27 Round 1: original brief stated $(-m, 0)$ which was a Jacobian error)*. Anchors T-V5b-T-(e) Goldstone nodal=2 universal. |
| **C-0715** | T-σ-Theorem-3 σ at Uniform on $D_4$ Grid (Closed Form) | accepted Cat A | A | P-0715 | exp_hessian_uniform_v2 (NQ-141, $L = 4$ to $32$, $< 10^{-9}$ precision) | New 2026-04-27 (W5 Day 1 G0). $\mu_k = 4\alpha\lambda_k^{\mathrm{Lap}} + \beta W''(c)$ closed form. *(Erratum 2026-04-27 Round 1: §13 worked example originally listed irrep label A_1 for the $(1,1)$ singlet; corrected to B_2.)* |
| **C-0716** | T-σ-Theorem-4 σ at First Pitchfork (Leading Order, continuum-limit claim) | Cat A → Cat B retroactive (CV-1.5.1, 2026-04-29) per Critic 7-agent verdict + Errata Round 1 (Morse-index inconsistency at original merge time). **Continuum vs discrete grid caveat added 2026-05-04 W6 NQ-187 audit:** canonical statement (ii) is now explicitly a continuum-limit claim; NQ-187 measured $\mu_1/\mu_0 \approx 2$ and effective $A_2/A_1 \approx 2$ on discrete $L \le 16$ free-BC grids (continuum prediction is degeneracy with $A_2/A_1 = 4$). Cat A re-promotion deferred to CV-1.7+ post-γ/β/α path closure. | B (was A) | P-0716 | (theoretical via T-Birth-Parametric + R22 axis-aligned, continuum-limit; numerical NQ-187 on discrete grid) | New 2026-04-27 (W5 Day 1 G0); retroactively downgraded 2026-04-29; continuum-vs-discrete caveat added 2026-05-04. $D_4 \to \mathbb{Z}_2$ symmetry breaking. Continuum-limit Mode 0 = Mode 1 = $4\|W''(c)\|\epsilon$ degenerate; discrete-grid measured $\mu_1/\mu_0 \approx 2$. $\mathcal{F}$ tie-break NQ-143/NQ-184. |
| **C-0722** | T-L1-M Soft-Count Corollary under $\Phi_{\mathrm{res}}$ following T-L1-F | ✅ **accepted Cat A conditional** (post-W6-D1-AUDIT + external audit PASS, 2026-05-04 EOD) | A conditional under L1-J + $\Phi_{\mathrm{res}}$ + $\tau<\tau_*^{\mathrm{post-R2}}$ | P-0722 | (theoretical via L-M-1 + L-M-2 post-repair + T-L1-F substitution; WQ-LAT-1.B empirical anchor on $T^2_{20}$ with $K_{\mathrm{field}}\in\{3,4,6,8,12\}$: $\phi_{\mathrm{hard}}$ exact, $\phi_{\mathrm{logistic}}^{100}$ ~$10^{-3}$, $\phi_{\mathrm{shift\text{-}sat}}^{20}$ ~$10^{-2}$; W6 D1 EOD external L-M-K-style audit PASS) | New 2026-05-04 W6 D1 G1-AUDIT closure (R-0/R-1/R-2/R-3 all resolved; was Cat-B sketched pre-audit). Promoted to canonical §13 same day post-supervised user authorization. Cat-A-conditional under $(P0)$–$(P11)$ + $\phi\in\Phi_{\mathrm{res}}(\ell_{\min},\tau)$ + $\tau<\tau_*^{\mathrm{post-R2}}=\min(2\rho_{\mathrm{pert}},\rho_{\mathrm{bg}},r_{\mathrm{birth}})$. Per-family corollaries: L-M.A (hard) Cat A absolute, L-M.B (logistic $s\ge 50$) + L-M.C (shift-sat $\beta\ge 20$) Cat A conditional inheriting. NOT a global identity. Does NOT solve OP-0005 or OP-0008. NQ-G1-1 self-correction integrated ($\rho_{\mathrm{bg}}$ vs $\rho_{\mathrm{res}}$ configuration-dependent; NQ-G1-1-ext W7+ for empirical anchor; Cat A conditional self-classification unaffected). External audit (cold-review general-purpose agent, 2026-05-04 W6 D1 EOD) verdict: PASS — all 4 closures + Theorem composition rigorous. |

---

## Counterexamples & Challenges (X-xxxx)

| X-ID | Refutes | Status | Description | Impact |
|------|---------|--------|-------------|--------|
| **X-0001** | ~~C-0550 (F-1 Validity)~~ — **superseded 2026-04-24** | superseded | Originally: K=2 energy 4.66 vs K=1 energy 2.25. **W4 reframing**: this evidence is the *correct* T-Merge(b) statement, not a refutation. F-1 was misframed as problem. | F-1 SPLIT-RESOLVED via Option D (premise dissolution); see C-0550 entry. |
| **X-0002** | Type A/B Classification | validated | exp65: all configs Type A (0 Type B observed); breaks 04-07 interpretation | Type classification rejected as non-real phenomenon |

---

## Canonical Spec Version History

### CV-1.5 (2026-04-27) — W5 Day 1 G0: σ-Framework Supporting Structures Canonical Merge

- **Added Cat A**: T-σ-Lemma-1 (Irrep Decomposition Well-Defined), T-σ-Lemma-2 (Nodal Count Properties — sub-statements (i,ii,iii,iv) Cat A; (v) Courant + (vi) orbit-divisibility Cat C riders), T-σ-Lemma-3 (Goldstone–ℓ=1 Angular Saturation, Cat A in continuum), T-σ-Theorem-3 (σ at uniform on $D_4$ free-BC grid closed form), T-σ-Theorem-4 (σ at first pitchfork leading order, Cat A in $\epsilon$-small regime).
- **σ-framework status change**: Commitment 14 (W4 04-25) supporting structures (Lemma 1/2/3, Theorem 3/4) — T2 (deferred) → **T1 (canonical-merged)**.
- **Decision**: Option α (5 separate §13 entries) — per W5 strategic plan §0.4 Decision 1 default; chosen because mathematically independent statements deserve individual canonical visibility for paper §4 σ-framework reference.
- **Pre-brainstorm corrections folded in** (`logs/daily/2026-04-27/pre_brainstorm.md` §1.1/1.2/1.3/1.4):
  - T-σ-Lemma-1: finite-graph hypothesis essential (Maschke fails on infinite groups without compact-Lie or amenable extension); trivial-stabilizer case vacuous remark added.
  - T-σ-Lemma-2 (iii): plan-template wording "$n_k = 1$ iff $\phi_k$ constant" was incorrect for $\phi_k \in \mathbf{1}^\perp$ (constant in $\mathbf{1}^\perp$ requires $\phi_k = 0$). Replaced with lower bound $\mathcal{N}(\phi_k) \geq 2$ from $\sum \phi_k = 0$ constraint. **Cat A** (was "Cat A" but with wrong content).
  - T-σ-Lemma-2 (vi): orbit divisibility restricted to non-invariant $\phi_k$ (vacuous for $G_u$-invariant case).
  - T-σ-Lemma-3: IBP interpretation B adopted ($\delta u^{\mathrm{ref}} = $ unit vector in ℓ=1 angular subspace) per W4-04-24 §3.3 actual proof structure; sat. identity is between Goldstone basis and ℓ=1 angular basis.
- **Counts**: 38 + 5 = **43** Category A; 52 + 5 = **57 claims**; 73% → **75% fully proved**.
- **T1 explosion**: 3 → **8** (Option α: each of Lemma 1, 2, 3, Theorem 3, 4 individually T1).
- **canonical.md growth**: 1420 → 1537 lines (~117 lines added; entries are concise per W4 §13 style).
- **Source**: `THEORY/logs/daily/2026-04-27/01_sigma_lemmas_review.md` (decision packet); `01a_lemma1_irrep_decomposition.md`, `01b_lemma2_nodal_count.md`, `01c_lemma3_goldstone_saturation.md`, `01d_theorem3_uniform_D4_grid.md`, `01e_theorem4_first_pitchfork.md` (per-statement files); `THEORY/canonical/canonical.md` §13 lines 1169-1306 (new entries between T-V5b-T and T-Birth-Parametric).

**Errata Round 1 (2026-04-27 evening, post-merge re-review)**: User-requested re-audit caught 3 substantive math errors in this morning's canonical merge. All errors fixed in canonical entries (with embedded `*Erratum 2026-04-27 evening:*` notes). **Theorem status NOT changed**: all 5 σ structures remain Cat A. See `THEORY/logs/daily/2026-04-27/91_critical_review.md`.

- T-σ-Lemma-3 (i): IBP identity value $-m \to -c_d \int u^*(r) dr$ (factor-$r_0$ correction inherited from W4-04-24 source; $c_d$ dimension-dependent).
- T-σ-Theorem-4 (ii): $K_1 < K_0$ → $K_1 = K_0$ on $D_4$ ($A_2/A_1 = 4$); "would-be Goldstone" framing removed.
- T-σ-Theorem-3 (vi): irrep-table speculative entries replaced with rigorous Schur-orthogonality character calculation.

**Round 2 refinements (2026-04-27 night, second re-review)**: User-requested second re-audit caught structural issues beyond Round-1 value errors. 7 issues fixed in canonical (with `*Refinement 2026-04-27 night*` markers); 2 commitment-level changes deferred to user decision; 4 NQs spawned (NQ-187..NQ-190). **Theorem status still NOT changed**. See `THEORY/logs/daily/2026-04-27/92_critical_review_round2.md`.

- T-σ-Lemma-3: (i) reframed to lead with rank/injectivity (IBP value as corollary); statement extended to general dimension $d$ (1D cycle, 2D/3D bulk and torus); (iii) nodal=2 made explicit for all dimensions. **Fully anchors T-V5b-T-(e) "universal on translation-invariant graphs"** (previously only 2D-localized).
- T-σ-Lemma-3: anchoring footer added — registers which T-V5b-T sub-statements σ supports structures anchor (only (e)) vs leave canonical-empirical ((a)/(b)/(c)/(d)).
- T-σ-Theorem-3: spinodal hypothesis discussion added — clarifies role of $W''(c) < 0$ vs outside-spinodal vs spinodal-boundary cases.
- T-σ-Theorem-4: (i') orbit-representative remark added — clarifies σ-tuple is for chosen representative; conjugate stabilizers across orbit give σ-equivalence.
- T-σ-Theorem-4: well-definedness note added — flags $K_0 = K_1$ degeneracy requires Commitment 14 (O7) tie-breaking convention (deferred to user decision).
- 04_nq174_setup.md: PRE-RUN sanity test snippet added (Round-1 §6.G follow-through).

**Deferred to W5 Day 2+ user decision (Commitment-level changes)**:
- Commitment 14 (O5') multi-irrep eigenspace convention.
- Commitment 14 (O7) tie-breaking convention by canonical irrep order.

### CV-1.4 (2026-04-26) — W4 Extended Close: V5b-T Verification + Partial Goldstone Discovery

- **Added Cat A**: T-V5b-T (Pre-Objective Goldstone on Translation-Invariant Graphs) — sub/super-lattice spectral dichotomy with commensurability splitting on 2D torus, 1-fold Goldstone on 1D cycle, universal nodal count.
- **New Cat C finding**: V5b-F (Partial Goldstone on Boundary-Modified Graphs) — boundary lifting mechanism qualitative observation. NQ-173 carry.
- **V5b 8 iterations resolved**: V1 (W4-04-24 morning) → V5b'' (W4-extended 04-26 evening). Healthy iterative refinement pattern.
- **Reproducibility crisis identified+resolved**: NQ-172 (mode-indexing artifact in NQ-170 analysis script). Mode-agnostic detection adopted.
- **σ-framework strengthening**: NQ-141 single-graph empirical → multi-graph (3 classes) empirical Cat A.
- **Count**: 37 + 1 = **38** Category A; 51 + 1 = **52 claims**; 73% fully proved.
- **W4 extended scope**: 2026-04-19 ~ 2026-04-26 (8 days). Per user direction "아직 내용은 전부 W4로 간주해".
- **Source**: `THEORY/logs/weekly/2026-04-W4/weekly_summary.md` (extended close, post-2026-04-26 update); `logs/daily/2026-04-26/04_NQ170c_graph_extension_nodal.md`.

### CV-1.3 (2026-04-25) — W4 Merge: Pre-Objective Mechanism + F-1/M-1/MO-1 Resolution

- **Added Cat A:** T-PreObj-1 (Pre-Objective Multi-Peak Formation Mechanism), T-PreObj-1G (graph-class independent), Lemma 4 (Quadratic form PD).
- **Added Cat A corollary:** F-1 SPLIT-RESOLVED via T-Merge(b) + T-PreObj-1 (i).
- **Critical blocker resolution:** F-1 (OP-0001) split-resolved, M-1 (OP-0002) layer-clarified, MO-1 (OP-0003) sidestepped. **3 → 0** Critical blockers.
- **Status changes:** C-0550, C-0551, C-0552 (challenged → resolved/clarified/sidestepped).
- **Count:** 35 + 2 = **37** Category A; 49 + 2 = **51 claims**; 71% → **73% fully proved**.
- **Pending user decision (T2 candidates, deferred):** σ-framework (Lemma 1/2/3, Theorem 3/4), Theorem 1 V5b, Axiom S1' v1 placement, CN15/16/17 (Static/Dynamic Separation, Protocol-Parameterized observables, σ-labeled FQ), Commitment 14/15 v2.
- **Source:** `THEORY/logs/weekly/2026-04-W4/weekly_summary.md` (W4 closing summary, ~25 pages).

### CV-1.2 (2026-04-12) — Frozen, with Audit Clarifications

- **Added:** T-Persist-K-Unified (Category B; parametric coverage of Sep/Weak/Strong regimes)
- **Explicit Assumptions:** All K-field theorems now state "fixed K, fixed m" constraint
- **Status Clarifications:**
  - F-1, M-1, MO-1 documented as unresolved (not silently ignored) — *resolved in CV-1.3*
  - Type A/B classification retracted (exp65 invalidated)
  - Morse theory MO-1 vulnerability flagged (mitigation: use existing results, defer full Morse) — *sidestepped in CV-1.3*
- **Count:** 38 + 1 (T-Persist-K-Unified) = 39 theorems (per CV-1.2 release accounting; honest recount 04-07 → 35A/4B/5C/5R)

### CV-1.1 (2026-04-03) — PLAN_0403 Tier 1 Complete

- **Upgraded to Category A:**
  - C-Axioms (C3'' symmetrization gap closed)
  - Predicate-Energy Bridge (formalized)
  - Deep Core Dominance 2b (strengthened)
- **New Unconditional Results:**
  - T-Persist-1(b): Basin unconditional via genericity argument
  - T-Persist-1(e): Confinement tight bounds (2.4-3.5×)
- **New:** T-Bind-Full (Category A, τ=1/2 only)
- **Count:** 35 → 38 Category A (3 upgraded)

### CV-1.0 (2026-04-01) — Initial Comprehensive Spec

- **Theorems:** T-1, T-3, T-6a, T-6b, T-6-Stability, T-7, T-8-Core, T-8-Full, T-11, T-14, T-20
- **QM Results:** QM-1, QM-2, QM-3, QM-4 (11 Category A)
- **Provisional:** Predicate-Energy Bridge, Deep Core Dom. 2b (Category B at the time)
- **K-field:** T-Persist-K-Sep (Category B), T-Persist-K-Weak (Category C)
- **Notes:** Initial comprehensive spec; 35+ theorems claimed
- **Retracted:** K-Saddle Conjecture, r̄₀ general τ (kept in archive)

---

## Open Problems Catalog (OP-xxxx)

> Note (2026-05-04 audit, second pass): this catalog absorbed the previously separate `THEORY/canonical/theorem_status.md` file. The merge eliminates a documentation drift surface (the two files used different OP-ID assignments and disagreed on body-level status flags). All OP body content (Statement, Evidence, Resolution mechanism, Sub-item tables, References, Statistics, Critical Path) lives here. Severity flags are kept in plain-text form (Critical / High / Medium / Low) rather than color emojis. Cross-references in working files that still point to `theorem_status.md` should be read as pointing to this section.

### Quick Index

| OP-ID | Problem | Severity | Status |
|-------|---------|----------|--------|
| **OP-0001** | F-1: K=2 vacuous | (was Critical) Resolved | SPLIT-RESOLVED (2026-04-24) via T-PreObj-1 (i) + T-Merge (b) |
| **OP-0002** | M-1: K=1 preferred | (was Critical) Resolved | LAYER-CLARIFIED (2026-04-24) — proved theorem misframed |
| **OP-0003** | MO-1: Morse fails | (was High) Sidestepped | SIDESTEPPED (2026-04-24) for single-formation σ scope; re-activation rider on D-6b approval or NQ-248 multi-formation Morse work |
| **OP-0004** | Type A/B Classification Invalidation | High | RETRACTED (empirically invalidated; exp65 0/4 Type B observed) |
| **OP-0005** | K Selection Mechanism (Missing) | High | OPEN; partial via 4-layer composite (free-energy / Kramers / numerical anchor / Commitment 16); CV-1.7+ Commitment 19 candidate |
| **OP-0006** | Boundary Definition Precision | High | RESOLVED (Session K, 2026-05-06): T-OP6-B promoted Cat A; d_H ≤ 2(α/β)^{1/2} under H1–H5; B1–B4 all closed. Residual: C=2 not tight; H4 required; soft-cut stereo open. |
| **OP-0008** | σ^A K-jump Inheritance Non-Determinism | High | OPEN (CV-1.5.1, W5 Day 4); Path B σ-rich + Φ-rich Cat B target; CV-1.7 Commitment 18 candidate |
| **OP-0009** | Multi-Formation Ontological Foundations | High | OPEN (CV-1.5.1, W5 Day 4; 8 sub-items post W6 D4 split); 1/8 RESOLVED via Commitment 16 (OP-0009-K); OP-0009-Pre SPLIT into Pre-a (PARTIALLY RESOLVED) + Pre-b (PARTIALLY RESOLVED, exp01 support) |
| **OP-0010** | Bind Generalization | Medium | OPEN (T-Bind-Proj/Full now Cat A per Phase 13 — see W6 G2 audit; OP-0010 retains for any further generalization questions) |
| **OP-0011** | Transport kernel exact form | Medium | TENTATIVE |
| **OP-0012** | Persistence composition | Medium | OPEN |
| **OP-0013** | Closure operator convergence rate | Medium | OPEN |
| **OP-0020** | Dynamic Topology (Out of Scope) | Low | seed (formerly listed as OP-0007 in this file pre-2026-05-04 unification) |
| **OP-0021** | Stochastic Dynamics | Low | UNDER INVESTIGATION (exp54–exp59 Kramers rate theory) |
| **OP-0022** | Continuous-Time Limit | Low | seed |

**W4 changes (2026-04-25):** Critical blockers 3 → 0. F-1 / M-1 / MO-1 all resolved / clarified / sidestepped via T-PreObj-1 family + T-Merge(b) + σ-framework single-formation scope.

**W5 changes (2026-04-29 CV-1.5.1 + 2026-04-30 W5 Day 4):** OP-0008 σ^A K-jump non-determinism + OP-0009 Multi-Formation Ontological Foundations registered High. OP-0009-K resolved via Commitment 16. OP-0003 MO-1 re-activation rider added.

---

### CRITICAL PROBLEMS (Foundational) — All Resolved in W4

#### OP-0001: F-1 — K=2 Vacuity

**Statement.** K=2 global stability is "vacuous" without external per-formation mass constraint. If masses $m_j$ are allowed to vary, energy minimization always selects K=1 (energetically ~50% cheaper).

**Evidence.**
- exp62, exp63: K=2 energy $E \approx 4.66$; K=1 energy $E \approx 2.25$.
- M-1 analysis: $M_2$ landscape monotonically decreasing toward K=1.
- All K-field theorems originally assumed "$m_j$ fixed externally".

**Impact (original framing).** All K-field theorems (T-Persist-K-Sep, T-Persist-K-Unified, etc.) depend on this external assumption; K-field theory is not self-contained; no mechanism explained why K would be fixed in biological/cognitive systems; blocked publication as self-contained theory.

**Status:** **SPLIT-RESOLVED (2026-04-24)** — both portions Cat A.

**Resolution (2026-04-24, W4).** F-1 decomposes into two layers, each Cat A resolved:
- **Pure $\mathcal{E}_{\mathrm{bd}}$ portion:** resolved by T-Merge (b) canonical theorem (already proved, isoperimetric ordering on connected graphs). The "K=1 cheaper" statement in pure $\mathcal{E}_{\mathrm{bd}}$ is a *correct theorem*, not an open problem. Original framing as "open problem" was a misclassification — see also OP-0002.
- **Full SCC portion:** resolved by T-PreObj-1 (i) (Pre-Objective Mechanism, Cat A graph-class independent via T-PreObj-1G). Under full SCC parameters, the F=1 single-disk minimizer of pure $\mathcal{E}_{\mathrm{bd}}$ is **not a critical point** of full $\mathcal{E}$. Therefore the dichotomy "K=1 cheaper vs observed K>1" does not arise — F=1 is non-critical, F ≥ 2 is the default ground state under full SCC. The premise of F-1 collapses.

Net effect: the originally-paradoxical comparison ("global static minimum K=1 vs empirical K>1") is dissolved. Pure $\mathcal{E}_{\mathrm{bd}}$ statement is a proved theorem (T-Merge (b)); full SCC statement is reversed (F ≥ 2 default).

**Severity:** was Critical → Resolved (no longer blocking).
**Last reviewed:** 2026-04-25 (W4 weekly close).
**References:** `THEORY/logs/daily/2026-04-24/16_C2_closure.md` §F-1 resolution; `THEORY/logs/daily/2026-04-24/11a_C2_generalization.md` (T-PreObj-1G); `THEORY/logs/daily/2026-04-24/08_C2_phase1_theory.md` (T-PreObj-1 (i) proof); canonical.md §13 T-Merge (b) (pure portion); canonical.md §13 T-PreObj-1 (full SCC portion).

#### OP-0002: M-1 — K=1 Energetic Preference

**Statement.** The K=2 energy landscape $E(m_1, m_2)$ where $m_1 + m_2 = M$ is monotonically decreasing as one formation size decreases ($m_2 \to 0$). Therefore, K=1 with total mass $M$ is always energetically cheaper than any K=2 split.

**Evidence.** Direct calculation $E_{K1}(M) < E_{K2}(M/2, M/2)$ always; empirical confirmation exp62, exp63, exp71–exp73; consequence of energy functional form (no K>1 preference mechanism).

**Status:** **LAYER-CLARIFIED (2026-04-24)** — proved theorem misframed.

**Clarification (2026-04-24, W4).** M-1 is **not an open problem**; it is the *correct mathematical statement* (T-Merge (b), canonical §13 Cat A) about isoperimetric ordering on the constraint manifold $\Sigma_m$. The original framing as "problem" arose from conflating two distinct quantities:
- **Pure $\mathcal{E}_{\mathrm{bd}}$ layer:** M-1 statement holds — K=1 has lower energy than K=2 by perimeter minimization (Γ-convergence). This is T-Merge (b), already canonical.
- **Full SCC layer:** the comparison "K=1 cheaper vs K=2" is not even framed, because under full SCC parameters the F=1 single-disk minimizer is **not a critical point** (T-PreObj-1 (i)). The "K=1 ground state" of pure $\mathcal{E}_{\mathrm{bd}}$ does not survive into the full SCC landscape.

Net effect: M-1 is *proved* (T-Merge (b)); the misframe was treating it as a *problem*. The actual problem (in original framing) was the apparent conflict between this proved theorem and empirically observed K>1 — that conflict is resolved by Static/Dynamic Separation (CN15) and T-PreObj-1: static global minimum is K=1 only on pure $\mathcal{E}_{\mathrm{bd}}$, but dynamic protocol-endpoint observables ($\widehat K$, $\mathcal F$) need not equal it.

**Severity:** was Critical → Clarified (proved theorem, not a problem).
**Last reviewed:** 2026-04-25 (W4 weekly close).
**References:** canonical.md §13 T-Merge (b); `THEORY/logs/daily/2026-04-24/08_C2_phase1_theory.md` §M-1 layer analysis; `THEORY/logs/daily/2026-04-24/16_C2_closure.md` §4; `THEORY/logs/daily/2026-04-23/MF_multi_quantization.md` §7 (Landau monotone — same statement under FQ framework).

#### OP-0003: MO-1 — Morse Theory Inapplicability

**Statement.** The K=2 constrained manifold $\Sigma^2_M = \{(u^1, u^2) : m_1 = m_2 = M/2\}$ is not a smooth manifold; it has corners (at boundary where one formation's mass $\to 0$). Smooth Morse theory requires manifolds without boundary and is thus inapplicable.

**Status:** **SIDESTEPPED (2026-04-24)** — single-formation σ-framework operates on $\Sigma_m$ (no corners). Multi-formation extension to $\Sigma^K_M$ remains open.

**Sidestep mechanism (2026-04-24, W4).** MO-1 was a blocker for global landscape analysis on the multi-formation manifold $\Sigma^K_M$ (corners). The W4 work introduced:
- **σ-framework** (canonical-ready, Cat A definitional): operates on **single-formation** $\Sigma_m$ (smooth simplex, no corners). Hessian eigenvalue/irrep/nodal-count signature $\sigma(u^*) = (\mathcal F; \{(n_k, [\rho_k], \lambda_k)\})$ is well-posed.
- **T-PreObj-1 family** (Cat A graph-class independent): operates on **single-formation** $\Sigma_m$. Pre-objective formation mechanism (F ≥ 2 default under full SCC) does not require multi-formation Morse analysis.

Therefore the principal results of W4 (T-PreObj-1 family + σ-framework + F-1 split-resolution) **do not require Morse theory on $\Sigma^K_M$**. MO-1 is not a blocker for current scope.

Multi-formation extension still open: stratified Morse on $\Sigma^K_M$ (multi-formation σ, Phase 5) remains genuine open work. MO-1 returns as an active blocker if/when the theory extends to multi-formation σ.

**Severity:** was High (multi-formation scope) → Not blocking (single-formation scope).

**Re-activation trigger (W5 added 2026-04-29 CV-1.5.1).** D-6b dynamic $\sigma_{\mathrm{multi}}^A(t)$ approval at CV-1.6 OR NQ-248 multi-formation stratified Morse work begins → High automatic re-activation. Single-formation σ-framework (CV-1.5+) operates on $\Sigma_m$ corner-free; multi-formation σ Phase 5 (D-6a CV-1.5.1, D-6b CV-1.6+) operates on $\widetilde\Sigma^{K_{\mathrm{field}}}_M$ corner-saturated regime — MO-1 stratified Morse on $\widetilde\Sigma^K_M$ becomes relevant. Current Day 3 EOD CV-1.5.1 D-6a uses Option A pragmatic (interior only, corners excluded) which preserves SIDESTEPPED status. Critical-blocker count "0" at CV-1.5.1 is **temporally conditional** on architecture choice (per Commitment 16 K-status + OAT-4 Shared-pool architecture decision pending CV-1.6).

**Last reviewed:** 2026-04-29 (W5 Day 3 EOD CV-1.5.1; rider added per 4-agent ontological depth analyst recommendation).
**References:** `THEORY/logs/daily/2026-04-24/02_development.md` §2, §5; `THEORY/logs/daily/2026-04-24/16_C2_closure.md` §7 (MO-1 sidestep note); `THEORY/logs/daily/2026-04-24/99_summary.md` §8 (sidestep vs resolution distinction); `THEORY/logs/daily/2026-04-29/04_D6b_sigma_trajectory_development.md` §5.4 (explicit re-engagement of MO-1 at multi-formation level); D-6a static merged at CV-1.5.1; D-6b dynamic deferred to W6+ via NQ-242.

---

### HIGH-PRIORITY PROBLEMS

#### OP-0008: σ^A K-jump Inheritance Non-Determinism

**Statement.** Under K-field gradient flow on shared-pool $\widetilde\Sigma^K_M$ (Phase 7 R1.3 architecture), at K-jump times $t^*$ (where $K_{\mathrm{act}}(t^{*-}) > K_{\mathrm{act}}(t^{*+})$, formation merger event), the post-merger $\sigma^A(t^{*+})$ is **NOT deterministic** in pre-merger $\sigma^A(t^{*-})$ alone. Inheritance map $\Phi : \sigma^A(t^{*-}) \to \sigma^A(t^{*+})$ requires merger-geometry data $\mathcal M$ = (which two formation indices $j, k$ merge; cluster centroids; post-merger relaxation trajectory; orientation alignment).

**Evidence.**
- Day 3 deepening pass `THEORY/logs/daily/2026-04-29/04_D6b_sigma_trajectory_development.md` Lemma 4.4.1(c): formal non-determinism claim, Cat C asserted.
- Self-critique `THEORY/logs/daily/2026-04-29/09_session_self_critique.md` §2.3: Lemma 4.4.1(c) downgraded "Cat B sketch" → "Cat C (conjectured)".
- Phase 8 T4 SCC↔CH correspondence (`2026-04-28/32_U5_SCC_CH_theorem.md` Cat B target): implicit assumption of deterministic σ-trajectory under CH-correspondence flow — violated by Lemma 4.4.1(c).
- Working file `THEORY/working/MF/sigma_multi_trajectory.md` §4.2 Lemma 4.2(c) Cat status: conjectured (Cat C).

**Impact.** D-6b Commitment 14-Multi DYNAMIC Cat A path (CV-1.6+) requires **rich-σ augmentation**: σ-tuple expanded to include cluster centroid, orientation, and Wigner-von Neumann data beyond eigenvalue tuple. Bifurcates CV-1.6 release path:
- Path A: accept non-determinism, register Cat B target with explicit non-deterministic K-jump map.
- Path B (Cat A target): rich-σ augmentation (NQ-242c explicit construction + NQ-242d σ^D symmetry-emergence).

Phase 8 T4 caveat needed in any Paper §4.5.7 SCC↔CH correspondence section: "static correspondence intact; dynamic $\sigma_{\mathrm{multi}}^A(t)$ ↔ CH flow correspondence requires σ-rich".

**Status:** TENTATIVE (Cat C asserted; explicit construction NQ-242c open).
**Severity:** High — affects D-6b canonical path; CV-1.6 release-blocking for Cat A target if Path B chosen.
**Last reviewed:** 2026-04-29 (W5 Day 3 EOD, registered at CV-1.5.1).

**Direct-attack NQs:**
- **NQ-242c**: explicit construction of two trajectories with same $\sigma^A(t^{*-})$ but distinct $\sigma^A(t^{*+})$. Cat A target. ~2-3 weeks. W6+ priority.
- **NQ-242d**: $\sigma^D$ symmetry-emergence characterization (post-merger stabilizer $\supseteq$ pull-back image). Cat A target. ~2-3 weeks. W6+.
- **NQ-242**: full Hessian σ-tuple time-series with rigorous K-jump theory. Cat A or B target. 4-6 weeks.

**Related problems:** OP-0003 MO-1 (re-activation at multi-formation level via D-6b path); OP-0005 K-Selection (K-jump-event path-dependence implication); OP-0009 (OP-0008 ⊂ OP-0009 sub-item dynamic-σ-trajectory aspect).

**References:** `THEORY/logs/daily/2026-04-29/04_D6b_sigma_trajectory_development.md` §4.4.1(c); `THEORY/logs/daily/2026-04-29/09_session_self_critique.md` §2.3; `THEORY/working/MF/sigma_multi_trajectory.md` §4.2; `THEORY/logs/daily/2026-04-28/32_U5_SCC_CH_theorem.md`.

#### OP-0009: Multi-Formation Ontological Foundations

**Statement.** Multi-formation σ-framework (D-6a static at CV-1.5.1 + D-6b dynamic at CV-1.6+) implicitly relies on 7 ontological commitments that are NOT all canonically registered as of CV-1.5.1. The implicit foundation is:

1. **OP-0009-K (K-status)**: K (formation count) ontological position. **PARTIALLY RESOLVED** by Commitment 16 (CV-1.5.1) — K_field/K_act two-tier decomposition. (OAT-1 done; working file `working/MF/K_status_commitment.md`.)
2. **OP-0009-F (F as derived diagnostic)**: F (peak count, threshold-free upper semi-continuous) canonical registration. Currently inline in T-PreObj-1 + CN17 only; not in §5 derived diagnostics. OPEN (OAT-2 W6 Day 1).
3. **OP-0009-λ (λ_rep ontology)**: $\lambda_{\mathrm{rep}}\,\langle u^j, u^k\rangle$ as 5th energy term vs 4-term coupling realization vs simplex-enforcement Lagrange. CN5 (4-term independence) is single-formation 약속 — multi-formation extension status undecided. OPEN (OAT-3 W6 Day 2).
4. **OP-0009-A (Architecture choice)**: K-field architecture I9 ($\Sigma^K_M$, fixed K) vs Shared-pool architecture I9' ($\widetilde\Sigma^K_M$, $K_{\mathrm{act}}$ variable). Currently I9 canonical, I9' working only. OPEN (OAT-4 W6 Day 2).
5. **OP-0009-C ($C_t$ multi-formation)**: Co-belonging $C_t$ demoted single-formation; multi-formation status (subsumed by $\sigma_{\mathrm{multi}}^D$ vs revived primitive). OPEN (OAT-5 W6 Day 3).
6. **OP-0009-Pre-a (K-field as local chart)**: The K-field product manifold $\Sigma_M^K = \prod_j \Sigma_{m_j}$ is a local coordinate chart within one energy basin $\mathcal{A}_{K,\alpha}(\mathcal{P})$, NOT the foundational state space. The foundational state space is $\mathcal{F}_M(\mathcal{P})$; K-act is derived via #PersComp on this space. PARTIALLY RESOLVED (2026-05-06 W6 D4): canonical argument established in D-ST-1..D-ST-4 (canonical.md §16); $\mathcal{B}_K(\mathcal{P})$ registered as correct integration domain replacing $\Sigma_M^K$. Working files updated: `k_selection_a_free_energy.md`, `k_selection_b_kramers.md`.

6b. **OP-0009-Pre-b ($K_{\mathrm{act}}$ as #PersComp observable)**: $K_{\mathrm{act}}(\tilde{u})$ is derived as the count of persistent connected components of $\tilde{u}$ via threshold filtration — NOT a slot-count $|\{j: \|u^{(j)}\|_\infty > \varepsilon\}|$. The slot-count is a regime-conditional approximation (T-L1-F under L1-J package), not a definition. PARTIALLY RESOLVED (2026-05-06 W6 D4): D-ST-3 (canonical.md §16) registers the correct definition; `CODE/stereo_scc/topology.py:persistent_component_count` implements it. Empirical support: exp01 (W6 D4). **FURTHER RESOLVED (W6 D4 Session C):** D-ST-3 body migrated to canonical.md §3.11 (Formal Universe). The §3 migration satisfies the CV-1.6 §3 amendment requirement. Remaining blocker: OP-0009-Pre-a foundational fix (§3.9/§3.10 already migrated; the remaining tension is the K-field architecture I9 vs shared-pool I9').
7. **OP-0009-Emp (R23 F=9 σ verification)**: σ-framework Cat A claims (CV-1.5) anchored at F=1 uniform / F=2 first-pitchfork; F=9 default ground state σ behavior empirical only (NQ-141). OPEN (OAT-7 W6 Day 5+6).

**Evidence.**
- 4-agent ontological depth analysis 2026-04-29 EOD (architect / critic / analyst / planner): convergent identification of 5 implicit commitments + 2 supplementary as multi-formation initiation foundations.
- Critic 7-agent verdict 2026-04-29: REVISE — D-6a should not merge without ontological audit; 5 CRITICAL findings.
- W4-W5 working trajectory: 5 conflicting K-status uses (External I9 / Kinetic CN6 / Derivative R22 / K_soft / Integer per N-1) coexisted in canonical/working without explicit reconciliation.

**Status:** PARTIALLY ADDRESSED at CV-1.5.1 + Day 4 morning OAT batch session (2026-04-30). 1 of 7 sub-items RESOLVED (OP-0009-K via Commitment 16 CV-1.5.1); 6 of 7 PARTIALLY RESOLVED at CV-1.6 candidate level via OAT-2..7 working files.
**Severity:** High — release-blocking for Cat A multi-formation σ-framework completeness; not blocking for CV-1.5.1 D-6a static (Cat A definitional only).
**Last reviewed:** 2026-04-29 (W5 Day 3 EOD, registered at CV-1.5.1).

**Sub-item Status Table (W5 Day 4 EOD post-Critic verdict propagation):**

| Sub-item | Pre-Day 4 | Post-Day 4 OAT batch | Resolution mechanism | Working file | Promotion target |
|---|---|---|---|---|---|
| **OP-0009-K** (K-status) | OPEN | RESOLVED | Commitment 16 K_field/K_act two-tier decomposition | `K_status_commitment.md` (480 lines) | CV-1.5.1 (DONE) |
| **OP-0009-F** (F derived diagnostic) | OPEN | PARTIALLY RESOLVED | F as derived diagnostic register §5.5 + CN17+ amendment + 4-quantity bridge | `F_Kstep_K_triple.md` (359 lines) | CV-1.6 D-CV1.6-O3 |
| **OP-0009-λ** (λ_rep ontology) | OPEN | PARTIALLY RESOLVED | Argument B (architectural-layer coupling) + Option 3 (CN10 contrastive); strict KKT identification verification fail | `lambda_rep_ontology.md` (242 lines) | CV-1.6 D-CV1.6-O3 |
| **OP-0009-A** (Architecture: K-field vs Shared-pool) | OPEN | PARTIALLY RESOLVED | I9 + I9' complementary modeling-layer commitments via Tool A1 stratified space | `shared_pool_canonical_proposal.md` (335 lines) | CV-1.6 D-CV1.6-O2 |
| **OP-0009-C** ($C_t$ multi-formation) | OPEN | PARTIALLY RESOLVED | Option C-3 variant: $C_t$ demoted maintained + $\sigma_{\mathrm{multi}}^D$ orthogonal (not subsumes); architecture-conditional (K-field 4a primary) | `cobelonging_vs_sigmaD.md` (392 lines) | CV-1.6 D-CV1.6-O4 |
| **OP-0009-Pre-a** (K-field as local chart, not foundational) | OPEN | PARTIALLY RESOLVED (W6 D4); chart validity conditions V1–V4 formalized (Session D) | $\mathcal{F}_M(\mathcal{P})$ foundational; $\Sigma_M^K$ = local chart; $\mathcal{B}_K(\mathcal{P})$ = topological sector; V1(K-stability)/V2(basin)/V3(separation)/V4(mass budget) conditions formalised | `pre_objective_K_field_tension.md`, `op_0009_pre_a_kfield_chart_validity.md`, `k_selection_a/b.md` | v2.0 §1 amendment (W11–W12) |
| **OP-0009-Pre-b** ($K_{\mathrm{act}}$ = #PersComp observable) | OPEN | PARTIALLY RESOLVED (W6 D4) | D-ST-3 registered; `topology.py` implements; exp01 SUPPORTED (PersComp=2 vs slot=4 under noise) | `stereo_scc_canonical_memo_v1.1.md`, `topology.py` | CV-1.6 §3 amendment |
| **OP-0009-Emp** (R23 empirical verification) | OPEN | PARTIALLY RESOLVED | R23 fullscale dataset numerical analysis: F=63 max, all 56 minimizers $F > K_{\mathrm{step}}$, σ-irrep CONFIRMED 0 exceptions; **BC-1 fails generic** (R23 generic = overlapping regime) | `single_high_F_equivalence.md` (511 lines) | CV-1.6 partial; full v2.0 |

**Net OP-0009 status post-Day 4 OAT batch:** PARTIALLY ADDRESSED (1 RESOLVED + 6 PARTIALLY RESOLVED). Full RESOLVED status not achieved at CV-1.6; v2.0 (W11–W12) deferred for Pre-objective + K-field tension full canonical §1 amendment.

**Net OP-0009 status post-W6 D4 stereo-SCC session (2026-05-06):** OP-0009-Pre SPLIT into Pre-a + Pre-b (total sub-items now 8). Both Pre-a and Pre-b PARTIALLY RESOLVED via D-ST-1..D-ST-4 canonical registration (§16) + exp01 empirical support. Net count: 1 RESOLVED (OP-0009-K) + 7 PARTIALLY RESOLVED (Pre-a, Pre-b, F, λ, A, C, Emp). Remaining blockers for full resolution: P-F-A1 Langevin (for $T_*$, affects Pre-a via $Z_K$ partition function), NEB barrier validation (for Pre-b claim quality), CV-1.6 §3 amendment (to move D-ST-3 from §16 extension into §3 Formal Universe).

**Important caveat (W5 Day 4 EOD post-Critic, 2026-04-30):** per Critic 7-agent verdict (`daily/2026-04-30/05_critic_final_review.md`) MAJOR-3 finding, OP-0009 should be framed as "framework + 1/7 sub-items closed (K via Commitment 16) + 6/7 sub-items partially addressed", **not** as "OP-0009 framework-level resolved" or "Theory Deepening Stretch 100%". Future canonical/CHANGELOG/paper claims should reflect this calibrated status to avoid inflated-resolution mis-citations.

**Direct-attack NQs and OAT working files.**
- OAT-1 (DONE): `working/MF/K_status_commitment.md` — Commitment 16 K-status proposal.
- OAT-2 (W6 Day 1 evening): F/$K_{\mathrm{step}}$/$K_{\mathrm{act}}$/$K_{\mathrm{field}}$ bridge — `working/MF/F_Kstep_K_triple.md`.
- OAT-3 (W6 Day 2 evening): $\lambda_{\mathrm{rep}}$ ontological status — `working/MF/lambda_rep_ontology.md`.
- OAT-4 (W6 Day 2 evening): Shared-pool architecture I9' — `working/MF/shared_pool_canonical_proposal.md`.
- OAT-5 (W6 Day 3 PM): $C_t$ vs $\sigma_{\mathrm{multi}}^D$ coexistence — `working/MF/cobelonging_vs_sigmaD.md`.
- OAT-6 (W6 Day 4 PM): Pre-objective + K-field tension — `working/MF/pre_objective_K_field_tension.md`.
- OAT-7 (W6 Day 5+6): R23 F=9 ↔ K=9 K-field empirical equivalence — `working/MF/single_high_F_equivalence.md`.

**Related problems:** OP-0003 MO-1 (sub-item OP-0009-A architecture decision triggers MO-1 re-activation); OP-0005 K-Selection (sub-item OP-0009-K addresses what K is, not what selects $K_{\mathrm{act}}$); OP-0008 σ^A K-jump non-determinism (OP-0008 ⊂ OP-0009 sub-item dynamic-σ-trajectory aspect).

**References.** 4-agent ontological depth analysis: inline conversation 2026-04-29 EOD (architect/critic/analyst/planner); OAT-1 working file; D-6a static merge: canonical.md §13 T-Commitment-14-Multi-Static (CV-1.5.1); D-6b dynamic deferred: `THEORY/working/MF/sigma_multi_trajectory.md` Theorem 4.6.1 Cat C/B target; Critic 7-agent verdict 2026-04-29 EOD.

#### OP-0004: Type A/B Classification Invalidation

**Statement.** 04-07 proposed "Type A vs Type B" classification of K=2 configurations: Type A = centered, stable, no valley-hopping; Type B = off-center, swap-prone, valley-hopping. exp65 conducted validation; Type B was never observed (0/4 configurations).

**Evidence.** exp65_formation_tracking.json: all 4 configs clustered at Type A; max_center_offset = 0.01–0.08 (all < Type B threshold 0.12); swap_count = 0 everywhere (Type B marker absent).

**Status:** RETRACTED (empirically invalidated).
**Severity:** High (affects theoretical narrative).
**Last reviewed:** 2026-04-12 audit.
**References:** exp65 data, `AUDIT_REPORT_2026-04-12.md` (in archived form).

#### OP-0005: K Selection Mechanism (Missing)

**Statement.** Theory provides no mechanism for how K (number of formations) is determined. Is it:
- Fixed externally (current assumption A-0012, unresolved F-1)?
- Emerged from energy minimization (contradicted by M-1)?
- Determined by model selection (BIC, free energy)?
- Kinetically determined (metastability barriers)?

**Impact.** Cannot predict K from initial conditions alone; theory cannot explain K emergence in biological/cognitive systems; required for moving from v1.2 to v2.0.

**Status:** OPEN — partially addressed via 4-layer composite (free-energy / Kramers / numerical anchor / Commitment 16; CV-1.7+ Commitment 19 candidate). *Session Q (2026-05-06): OP-0005 split into three subproblems (see below).*
**Severity:** High (foundational question).
**Related:** F-1, M-1.

**Session Q split (2026-05-06) — OP-0005 decomposes into:**

| Sub-ID | Name | Status | Blocker |
|---|---|---|---|
| **OP-0005-EQ** | Equilibrium K-selection | **PARTIALLY RESOLVED** — T-K-Select-PF **canonical Cat B** (Session R, CV-1.10). P-F flag on Z_K lifted by Package I (CV-1.9). {p_K = π_{T_*}(B_K)} is the stationary K-distribution. K_feas defined. Body in `canonical.md §13 Category B`. | Cat A path: explicit σ_M-null in T-PF-A1-AR coordinates + K_feas per-instance characterization + K_act fixed to D-ST-3. |
| **OP-0005-DYN** | Dynamical K-transition / Kramers rates | **OPEN** | Package II (Eyring-Kramers, H5 + OP-0021). Not before W9+. |
| **OP-0005-OBS** | Observation-conditioned K selection | **STRUCTURED** — T-K-Select-OBS working Cat B candidate (Session S, 2026-05-06). Posterior sector masses $p_K(\mathfrak{O}_t) = \pi_t^{obs}(\mathcal{B}_K)$ defined. $K^*(\mathfrak{O}_t) = \arg\min_K F_\mathrm{obs}(K;\mathcal{P},\mathfrak{O}_t)$. Working file: `THEORY/working/MF/k_select_obs_posterior.md`. | Cat B conditions: canonical likelihood model (LM1–LM3); exp54 validation. OP-0005 overall OPEN. |

*OP-0005 overall remains OPEN until all three subproblems are addressed.*

**2026-04-17 integration note (Phase 4).** Current audited E-0082 surface provides only weak, proxy-level support for a persistence-scope reading, not observed-K selection closure. Current runnable/artifact evidence still lacks τ/T/B/cross-K observables and locked reruns remain blocked by "No Type B base found". This is an evidence-boundary alignment note only; it does not change OP-0005 status or severity. OP-0005 therefore remains OPEN; selection-mechanism status is unchanged pending a runnable E-0082 path plus explicit selection-grade outputs.

#### OP-0006: Boundary Definition Precision

**Statement.** Boundary $B_t$ is currently defined via $D_t$ (distinction operator) threshold: $B_t = \{x : D_t(u_t) > \text{threshold}\}$. But this is not morphologically precise (what is "boundary" exactly?), lacks gradient/articulation measure, and is graded rather than crisp.

**Impact.** Affects articulation diagnostic (part of proto-cohesion d); needed for precise morphological quality measure $\mathcal Q_{\mathrm{morph}}$; currently incomplete.

**Status: RESOLVED (W6 D4 Session K, 2026-05-06).** T-OP6-B promoted Cat B → Cat A conditional under H1–H5. d_H(B_PersRidge, ∂PersComp) ≤ 2·(α/β)^{1/2} with explicit constant. All four blockers closed:
- B1 Topological separator: ∂C_j ⊂ B_t → vertex separator. CLOSED.
- B2 Hausdorff constant: C=2 explicit via matched-asymptotic expansion (H4: κ_max·ξ ≤ 0.1). CLOSED.
- B3 Stereo conditioning: G_t^P edges only (hard-cut D-ST-1). CLOSED.
- B4 ρ_bd = 1/(4ξ) canonical (Session J). CLOSED.

Prior Cat B achievement (W6 D4 Session D): barcode stability (Chazal et al.) + PersRidge equivalence + exp06 support (shadow 5/5 ratio 4.09, blur 5/5 ratio 50.8). Full proofs: `THEORY/working/MF/op_0006_boundary_precision.md §9–§12`. Canonical entry: `canonical.md §5.3b` + `§13 Category A`.

**Residual open items (not blockers for OP-0006 resolution):**
- C=2 not tight (inner bound C < 1.37 under H4); H4 (κ_max·ξ ≤ 0.1) required.
- Soft-cut stereo (GL-weighted adjacency without hard depth cut) open.
- P-F-A1 OPEN (separate OP-0021; affects D-ST-4 Kramers rate but not T-OP6-B boundary bound).

**Severity:** High — RESOLVED.
**Related:** D-0004 (distinction operator), D-ST-3 (§3.11 K_act as #PersComp), stereo D-ST-1 (depth-conditioned adjacency).

---

### MEDIUM-PRIORITY PROBLEMS

#### OP-0010: Bind Generalization

**Statement.** Originally framed as: T-Bind-Proj proved for τ=1/2 only (Cat B); T-Bind-Full general τ (Cat C). 2026-05-04 W6 G2 audit decided both at Cat A per canonical Erratum 2026-04-07 Phase 13 upgrade (KKT projection + Banach inversion, general τ via binary mass-balance formula $\Phi(\tau; a_{\mathrm{cl}}, c)$). The original "general τ unclear" question is now resolved; OP-0010 retains for any further generalization questions (e.g. $\tau$ outside $(0,1)$, non-strict-interior minimizers).

**Status:** Largely resolved at canonical level by W6 G2 decision; retain for residual generalization scope.
**Severity:** Medium (specialty case).
**References:** canonical.md §13 T-Bind-Proj (line 1440), T-Bind-Full (line 1445); W6 G2 audit entry in CHANGELOG 2026-05-04.

#### OP-0011: Transport Kernel Uniqueness

**Statement.** Current transport kernel $M_{t \to s}$ form (entropy-regularized OT) is *one* realization satisfying axioms E1–E5. Is it unique? Are there other realizations?

**Impact.** Theoretical completeness; robustness of persistence results; may affect characterization of formation inheritance.

**Status:** UNDER INVESTIGATION (exp30–exp35).
**Severity:** Medium (impacts formalism).
**Related:** T-Persist-1(a–e).

#### OP-0012: Persistence Composition

**Statement.** T-Persist-Full (composition of persistence across 3+ time steps) is Cat C (very conditional). Can general composition formula be proved?

**Impact.** Affects long-timescale predictions; currently only T-Persist-1 (two-step) fully proved; limits temporal theory.

**Status:** UNRESOLVED (Cat C conditional).
**Severity:** Medium (temporal extension).
**References:** canonical.md §13 T-Persist-Full.

#### OP-0013: Closure Operator Convergence Rate

**Statement.** T-6 proves closure operator has fixed point with contraction; exact rate unknown.

**Question.** What is the convergence rate as function of parameters?

**Impact.** Affects efficiency of closure-based algorithms; currently only asymptotic guarantee known; low practical impact.

**Status:** UNDER INVESTIGATION.
**Severity:** Medium (implementation detail).

---

### LOW-PRIORITY PROBLEMS

#### OP-0020: Dynamic Topology (Out of Scope)

**Statement.** Current theory assumes $X_t$ is fixed. What if graph topology changes over time?
**Status:** Not in current scope.
**Severity:** Low (future extension).
**Note:** previously listed as OP-0007 in earlier theorem_status.md OP table; unified to OP-0020 per 2026-05-04 audit pass.

#### OP-0021: Stochastic Dynamics

**Statement.** Theory focuses on deterministic gradient descent. How do thermal fluctuations affect dynamics?
**Status:** UNDER INVESTIGATION (exp54–exp59 Kramers rate theory).
**Severity:** Low (extension work).

#### OP-0022: Continuous-Time Limit

**Statement.** Theory on discrete graphs; what is continuous limit?
**Status:** Not addressed.
**Severity:** Low (theoretical extension).

---

### Problem Statistics (post-W6 G2 audit, 2026-05-04)

| Severity | Count | Status |
|----------|-------|--------|
| Critical | 0 | All 3 (F-1, M-1, MO-1) addressed in W4 (2026-04-24) |
| High | 4 | OP-0005, OP-0008, OP-0009 active; OP-0004 retracted; **OP-0006 RESOLVED** (Session K 2026-05-06) |
| Medium | 4 | OP-0010 largely resolved at canonical level (W6 G2); OP-0011, OP-0012, OP-0013 active |
| Low | 3 | OP-0020, OP-0021, OP-0022 (extensions / out of scope) |
| Total active open | 7 (4 High + 3 Medium + a residual scope of OP-0010) | — |
| Resolved / clarified / sidestepped (W4) | 3 | F-1, M-1, MO-1 |
| Retracted | 1 | OP-0004 |

---

### Critical Path to Resolution

**Completed in W4 (2026-04-19 ~ 2026-04-25).**
1. F-1 SPLIT-RESOLVED (OP-0001) — both portions Cat A. Pure $\mathcal{E}_{\mathrm{bd}}$ portion: T-Merge (b) canonical; full SCC portion: T-PreObj-1 (i) Cat A graph-class independent (W4 04-24).
2. M-1 LAYER-CLARIFIED (OP-0002) — proved theorem (T-Merge (b)) misframed as problem. Static/Dynamic Separation (CN15) explains apparent K=1 vs K>1 conflict.
3. MO-1 SIDESTEPPED (OP-0003) — single-formation σ-framework operates on $\Sigma_m$ (no corners); current scope does not require Morse on $\Sigma^K_M$.
4. Resolution path: Option D (premise dissolution) — neither original A/B/C, but a fourth path discovered via SCC-intrinsic re-framing.

**W5 close + W6 actions (2026-04-26 onward).**
- W5 Day 1 G0: σ-framework supporting structures merged (CV-1.5).
- W5 Day 3 EOD: D-6a multi-formation σ static + Commitment 16 K-status (CV-1.5.1); OP-0008 + OP-0009 registered.
- W5 Day 4: 17 working files / ~8,145 lines added in Wave 3 burst (now in CV-1.7 parking lot).
- W5 Day 5: reconciliation day; 9 retractions documented.
- W5 Day 6: T-L1-F canonical promotion (CV-1.5.2) — first multi-formation Cat A theorem.
- W5 Day 7: L-M soft-count corollary working draft (Cat B sketched).
- W6 Day 1 (today, 2026-05-04): full audit pass + OP-ID unification + theorem_status.md merge into this file + W6 G2 (T-Bind decision) + NQ-187 falsification handling for T-σ-Theorem-4.

**W6 remaining (per `THEORY/logs/weekly/2026-05-W1/W6_strategic_plan.md`).**
- G1 L1-M-AUDIT (R-1/R-2/R-3 closure for L-M-2).
- G3 K_act ε-convention decision.
- G4 CV-1.7 parking-lot Stage 0 inventory.

**Future (W7+).**
- CV-1.7 parking-lot Stages 1–3 (per `THEORY/working/CV-1.7_PARKING_LOT_REVIEW_PLAN.md`).
- OP-0008 Path B (σ-rich + Φ-rich) Cat B target — Commitment 18 candidate.
- OP-0005 K-Selection 4-layer composite — Commitment 19 candidate.
- T-σ-Theorem-4 γ/β/α path audit (Cat A re-promotion attempt; CV-1.7+).
- L1-M canonical promotion (post L1-M-AUDIT closure).
- OP-0009 sub-items 2–7 PARTIAL → READY upgrades via OAT-2..7 short integrations.

---

### Problem Lifecycle Example: F-1

- **Discovery:** 2026-04-06 audit identified K=2 energy paradox.
- **Formalization:** 2026-04-12 documented as critical.
- **Reframing:** 2026-04-19 N-1 (Soft-Hard Switching Asymmetry) discovered as single source of F-1/M-1/MO-1 (W4 reframing).
- **Foundation work:** 2026-04-21 K_soft + $\mathcal F_{C+E}$ framework — F/M/MO architectural dissolution candidate.
- **Empirical pivot:** 2026-04-23 R23 Orbital Discovery + 56 stable minimizers + closure-eliminates-F=1.
- **Resolution:** 2026-04-24 T-PreObj-1 family Cat A (graph-class independent via T-PreObj-1G) + T-Merge (b) canonical → SPLIT-RESOLVED.
- **Current status:** OP-0001 RESOLVED (no longer blocking).
- **Resolution path:** Option D (premise dissolution via SCC-intrinsic re-framing).
- **Timeline (actual):** reframing-to-resolution: 6 days (04-19 to 04-24).
- **Outcome:** v2.0 release path unblocked.

---

---

## Proof Status Summary (Updated 2026-05-04 W6 D1 EOD, post-T-L1-M supervised promotion; CV-1.5.2 release 2026-05-02 baseline)

| Status | Count | Examples |
|--------|-------|----------|
| **Category A (Fully Proved)** | **47** (CV-1.5.2 release: 46; W6 D1 EOD supervised addition: +1 T-L1-M; was 43 post-v1.5, 38 post-v1.4, 37 post-v1.3, 35 pre-W4) | T-1, T-20, QM-1:4, C-Axioms, Predicate-Energy Bridge, T-PreObj-1, T-PreObj-1G, Lemma 4 (W4), T-V5b-T (W4 extended), T-σ-Lemma-1, T-σ-Lemma-2, T-σ-Lemma-3, T-σ-Theorem-3 (W5 Day 1 G0; T-σ-Theorem-4 retroactively격하 to Cat B at CV-1.5.1), **T-Commitment-14-Multi-Static, T-σ-multi-A-Static, T-σ-multi-D-Static (W5 Day 4 D-6a multi-formation σ static)**, **T-L1-F (W5 Day 6 CV-1.5.2 hard-bar / active-count bridge under L1-J regime, conditional)**, **T-L1-M (W6 D1 EOD supervised addition 2026-05-04 — Soft-Count Corollary under $\Phi_{\mathrm{res}}$ following T-L1-F, Cat A conditional under $(P0)$–$(P11) + \phi \in \Phi_{\mathrm{res}} + \tau < \tau_*^{\mathrm{post-R2}}$, post external L-M-K-style audit PASS)**, etc. |
| **Category B (Conditional)** | **5** (canonical §13 hard Cat B = 4: γ_eff, T-Birth-Parametric General, T-d_min-Formula, T-Beyond-Weyl; plus T-σ-Theorem-4 retroactive Cat A → Cat B at CV-1.5.1; plus T-σ-Multi-1 Cat B target. T-Persist-K-Sep / T-Persist-K-Unified previously listed here have actually been Cat C since 2026-04-07 per canonical Erratum.) | γ_eff ≈ 0.89 (empirical, branch-conditioned); T-Birth-Parametric General (non-D₄ graphs); T-d_min-Formula (regression fit); T-Beyond-Weyl (grid-specific quantification); **T-σ-Theorem-4 (Cat A → Cat B retroactive at CV-1.5.1, NQ-187 finding + Critic 7-agent verdict; Cat A re-promotion deferred to CV-1.7+ post-γ/β/α audit)**; **T-σ-Multi-1 (Cat B target, Goldstone-pair instability under V5b-T per-formation regime)**. *(Corrected 2026-05-04 W6 G2 audit: removed T-Bind-Proj per Phase 13 Cat A upgrade; the resulting count is 6 entries — pending §15 / §13 Cat B header reconciliation, see CHANGELOG W6 G2 entry. The "5" headline kept for now to match canonical §15 wording until the next canonical-merge cycle resolves the count.)* |
| **Category C (Very Conditional)** | 5 + 1 (new finding) + 2 (W5 Day 1 sub-statements within T-σ-Lemma-2) | T-Persist-1(a/d), T-Persist-Full, T-Persist-K-Sep (per canonical Erratum 2026-04-07), T-Persist-K-Weak, T-Persist-K-Unified; V5b-F (new finding 2026-04-26, NQ-173 carry); T-σ-Lemma-2 (v) Courant upper bound + (vi) $G_u$-orbit divisibility (W5 Day 1 sub-statements bundled in single Cat A parent entry). *(Corrected 2026-05-04 W6 G2 audit: removed T-Bind-Full per Phase 13 Cat A upgrade.)* |
| **Resolved/Clarified/Sidestepped (W4)** | 3 | C-0550 (F-1 split-resolved), C-0551 (M-1 layer-clarified), C-0552 (MO-1 sidestepped) |
| **Challenged** | 1 | C-0553 (Type A/B) |
| **Retracted** | 5 | K-Saddle Conjecture; r̄₀ general τ (Theorem 3.3); T-Merge (c); T-Merge (d); T-Merge (e). *(Corrected 2026-05-04 audit: prior "2" entry was inconsistent with `canonical.md` §13 Retracted block which catalogues 5 distinct retractions.)* |
| **Open (active)** | **High: 3 (OP-0005 K-Selection, OP-0008 σ^A K-jump, OP-0009 Multi-Formation Foundations); Medium: 4 (OP-0010..OP-0013); Low: 3 (OP-0020..OP-0022)** — total 10 active. OP-0001/0002 resolved (W4); OP-0003 sidestepped; OP-0004 retracted; **OP-0006 RESOLVED** (Session K 2026-05-06: T-OP6-B Cat A, d_H ≤ 2(α/β)^{1/2}). | OP-0005 K-Selection partial via 4-layer composite (CV-1.7+ candidate); OP-0008 σ^A K-jump (Path B σ-rich + Φ-rich Cat B target, CV-1.7 Commitment 18 candidate); OP-0009 7 sub-items (1/7 RESOLVED via Commitment 16, 6/7 PARTIALLY per `theorem_status.md` body). |
| **Reproducibility crises identified+resolved** | 1 | NQ-172 (mode-indexing artifact, 2026-04-26 resolved) |
| **W4-extended carry NQ** | 3 (G1/G2/G4) | NQ-173 (V5b-F partial Goldstone — G1 W5 Day 1), NQ-174 (ζ_* graph-dependence — G2 W5 Day 2-3), NQ-175 (3D extension — G4 W5 Day 5) |
| **W5 Day 1 G0 spawn NQ** | 11 (NQ-176..NQ-186) | NQ-176/177 (functoriality, multi-irrep ordering — Lemma 1); NQ-178/179 (frustration bound, orbit sharpening — Lemma 2); NQ-180/181 (discrete correction, higher-ℓ analog — Lemma 3); NQ-182/183 (discrete nodal count, periodic-BC analog — Theorem 3); NQ-184/185/186 (tie-break, higher pitchforks, cascade — Theorem 4) |
| **W5 Day 1 Round-2 spawn NQ** | 4 (NQ-187..NQ-190) | NQ-187 (higher-order $\epsilon$-splitting of $K_0 = K_1$ on $D_4$ — Theorem 4); NQ-188 (σ-uniqueness theorem — # distinct σ-classes per graph/parameter regime); NQ-189 (σ → crisp object recovery — Commitment 11 derivative-objecthood); NQ-190 (σ topological invariance under graph homeomorphism). See `THEORY/logs/daily/2026-04-27/92_critical_review_round2.md` §10, §12. |

---

## Cross-Reference by Topic

### Single-Formation Theory
- **Existence:** T-1
- **Stability:** T-3, T-6-Stability, T-7
- **Phase Transition:** T-8-Core, T-8-Full
- **Convergence:** T-11, T-14
- **Diagnostics:** T-Bind-Proj/Full, Predicate-Energy Bridge

### Multi-Formation (K-field / Shared-pool $\widetilde\Sigma_M^{K_{\mathrm{field}}}$)
- **Temporal Persistence:** T-Persist-K-Sep, T-Persist-K-Weak, T-Persist-K-Unified
- **Global Stability:** Deep Core Dominance 2b (conditional)
- **σ-framework Multi (W5 Day 4 D-6a static, CV-1.5.1):** T-Commitment-14-Multi-Static, T-σ-multi-A-Static, T-σ-multi-D-Static, T-σ-Multi-1 (Cat B target)
- **Hard-Bar / Active-Count Bridge (W5 Day 6, CV-1.5.2):** **T-L1-F** (Cat A conditional under L1-J regime $(P0)$–$(P11)$)
- **K-status (CV-1.5.1):** Commitment 16 K_field/K_act Two-Tier Decomposition
- **Open:** F-1 / M-1 (W4 resolved), ~~OP-0006~~ **(RESOLVED Session K 2026-05-06 — T-OP6-B Cat A)**, **OP-0008 σ^A K-jump non-determinism (HIGH)**, **OP-0009 Multi-Formation Ontological Foundations (HIGH, 7 sub-items, 1/7 RESOLVED + 6/7 PARTIALLY)**

### Foundational
- **Consistency:** T-20, C-Axioms
- **Quantum Analogy:** QM-1:4

---

## Maintenance

- **Owned by:** Lead + Archivist
- **Updated:** When new C-xxxx promoted to canonical or P-xxxx completed
- **Validation:** build_dependency_graph.py checks for consistency

---

**Last updated:** 2026-05-04 (W6 Day 1 EOD: audit pass + G2 + G3 + G1 closures + T-L1-M supervised canonical promotion + 12-NQ batch + parking-lot Stage 0 inventory + Issue #1–#5 series + NQ-G1-2 EXECUTED; 14 CHANGELOG addendums)
**Total canonical theorems:** **57** = **47 Cat A** (CV-1.5.2 release 46 + W6 D1 EOD T-L1-M supervised +1) + 5 Cat B + 5 Cat C — 5 retracted (**62 claims, 75% fully proved**)
**Open problems:** see Open Problems table above (4 High + 4 Medium + 3 Low active; 3 Critical resolved in W4; 1 retracted)

**Note (2026-05-04 audit):** prior versions of this section listed forward-looking content ("W5 Day 7 working draft", "Pending W6+", "Future-stale items pending CV-1.6 release") that belong in `THEORY/CHANGELOG.md` (chronological session log) and `THEORY/logs/weekly/...strategic_plan.md` (forward planning). Per CLAUDE.md contamination barrier ("canonical/ accepts only promoted content"), those forward-looking lines were moved out of this canonical-layer file. The W5 Day 7 L1-M soft-count working draft, the pending W6+ promotion targets, and the future-stale list are recorded in CHANGELOG.md (2026-05-04 audit-pass entry).

**Recent W4 additions (2026-04-25)**: T-PreObj-1, T-PreObj-1G, Lemma 4 (Pre-Objective Mechanism graph-class independent), Commitment 14/15, CN15/16/17.
**W4 extended addition (2026-04-26)**: T-V5b-T (Pre-Objective Goldstone on Translation-Invariant Graphs) — sub/super-lattice dichotomy on torus T^d, cycle C_n; 2D doublet commensurability split; 1D Goldstone; nodal count = 2 universal. V5b 8-iteration cycle resolved.
**W5 Day 1 G0 addition (2026-04-27, CV-1.5)**: T-σ-Lemma-1/2/3 + T-σ-Theorem-3/4 — σ-framework supporting structures grounding Commitment 14 in §13 directly. Option α (5 separate entries). Pre-brainstorm corrections folded in (finite-graph hypothesis explicit, Lemma 2 (iii) reframed as lower bound, Lemma 3 IBP interpretation B adopted). Round-1 (3 numerical errors) + Round-2 (11 structural issues) audit applied same session.
**W5 Day 4 addition (2026-04-30, CV-1.5.1)**: D-6a multi-formation σ static (3 Cat A: T-Commitment-14-Multi-Static, T-σ-multi-A-Static, T-σ-multi-D-Static) + 1 Cat B target (T-σ-Multi-1 Goldstone-pair instability) + Commitment 16 K-status Two-Tier Decomposition (K_field/K_act; resolves OP-0009-K). T-σ-Theorem-4 Cat A → Cat B retroactive (NQ-187 RED finding + Critic 7-agent verdict). OP-0008 + OP-0009 registered High; OP-0003 MO-1 re-activation rider added.
**W5 Day 6 addition (2026-05-02, CV-1.5.2 — release baseline)**: T-L1-F (Hard-Bar / Active-Count Bridge under L1-J Regime) Cat A conditional under hypothesis package $(P0)$–$(P11)$. First multi-formation canonical Cat A theorem. L1-A through L1-L 13-step working chain + L1-K external audit + L1-K-REPAIR cycle (R-1..R-4) completed. theorem_status.md unchanged (T-L1-F is a bridge, not a K-selection mechanism).
**W6 D1 EOD supervised addition (2026-05-04, CV-1.5.2 + T-L1-M post-supervision)**: T-L1-M (Soft-Count Corollary under $\Phi_{\mathrm{res}}$ following T-L1-F) Cat A conditional under $(P0)$–$(P11) + \phi \in \Phi_{\mathrm{res}}(\ell_{\min}, \tau) + \tau < \tau_*^{\mathrm{post-R2}}$ where $\tau_*^{\mathrm{post-R2}} = \min(2\rho_{\mathrm{pert}}, \rho_{\mathrm{bg}}, r_{\mathrm{birth}})$. W6 G1 deliverable: R-0/R-1/R-2/R-3 self-audit closures + Lemma L-M-2 Cat A conditional + Theorem L-M Cat A conditional + per-family corollaries L-M.A absolute / L-M.B/L-M.C conditional inheriting + external L-M-K-style audit PASS (cold-review general-purpose agent ~7 min). Promoted same-day post-supervised user authorization per CHANGELOG W6 D1 EOD second addendum. C-0722 row added in Active Claims table. NQ-G1-1 self-correction integrated ($\rho_{\mathrm{bg}}$ vs $\rho_{\mathrm{res}}$ configuration-dependent; NQ-G1-1-ext W7+ for empirical anchor). NQ-G1-2 EXECUTED post-EOD (P9-tight regime; (P9-tight) candidate for L1-J' regime promotion enabling factor-1 sharpening empirically penalty-free; NQ-G1-2-ext W7+ for direct $\|R_j\|_\infty$ measurement). T-L1-M does NOT solve OP-0005 / OP-0008.
**See also:** `weekly_summary.md` (W4 extended close), `theorem_status.md` (active OPs), `canonical.md` §13 (theorem catalog), `THEORY/logs/daily/2026-04-27/` (W5 Day 1 artifacts), `THEORY/logs/weekly/2026-04-W5/W5_strategic_plan.md` (8-goal blueprint), `THEORY/CHANGELOG.md` (2026-04-27 entry + 2026-05-04 W6 D1 entries with 14 addendums).
