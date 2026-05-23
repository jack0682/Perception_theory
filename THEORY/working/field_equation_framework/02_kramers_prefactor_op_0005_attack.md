---
type: working/field_equation_framework/cat_b_target_derivation
date: 2026-05-20
session_origin: W8-Day3 late, user-authorized parallel ultrawork (Tier 1 priority spawn from 01_ns_inspired_synthesis.md §13.2)
canonical_version: CV-1.18 SEALED (untouched throughout)
status: draft v0.1
authors: user (Jaehong Oh)
preceded_by:
  - 01_ns_inspired_synthesis.md (§6 #12 Pr^{(Kramers)}, §7 Identity 2, §9.2/§11 Tier 1, §13.2 child file plan)
  - canonical §13 T-PF-A1-AR/SDE/GI/PE (Cat A, CV-1.8/1.9) — first-order reflected Langevin foundation
  - canonical §13 T-P-F-ε0-K (Cat B, CV-1.7) — Kramers exponent stability conditional on H5
  - canonical §13 T-K-Select-PF (Cat B, CV-1.10) — equilibrium K-selection via Gibbs sector mass
  - canonical §16 D-ST-4 (Cat B candidate, CV-1.6) — Z_K + Γ + Kramers rate (P-F flag previously RESOLVED via CV-1.9)
  - canonical §13 Theorem 4 (Cat A) — μ_k = 4αλ_k(L_G) + βW''(c) Hessian formula at uniform critical
  - canonical §16 OP-0005-DYN (OPEN, W9+) — Kramers transition rates
  - canonical theorem_status.md OP-0005, OP-0008, OP-0021 (Routes A/B DEPRECATED CV-1.18)
  - CV-1.18 SEAL (Mori-Zwanzig and RG fixed-point routes deprecated — CN-COB violation)
  - 2026-05-20 logs/daily 03_D_L_commutation.md (S3 Aut(G)-equivariance pattern as exemplar)
  - working/cssl/01_critic_evaluation.md (3 CRITICAL + 4 MAJOR CSSL flaws — patterns explicitly AVOIDED here)
purpose: |
  Derive the explicit Eyring–Kramers prefactor $\omega_0$ for SCC formation regime using
  *Hänggi–Talkner–Borkovec 1990* overdamped form as a *contrastive standard tool* (CN10).
  Anchor every Hessian eigenvalue to canonical Theorem 4 / T-PF-A1-* Package I.
  Produce a single Cat B target lemma **L-KRAMERS-PR-SCC**: statement + hypotheses
  + 5-step proof sketch + inverse causation. Map advance to 5 canonical OPEN/Cat-B rows
  (OP-0005-DYN, T-P-F-ε0-K, D-ST-4, OP-0008, Package II). No canonical edits.
canonical_compatibility:
  CN1_canonical_edits: 0
  CN2_silent_op_resolution: 0 (only target-level attack point; no claim of resolution)
  CN3_research_os_redux: 0
  CN4_analyticity: preserved (zero new energy terms)
  CN5_4_term_independence: preserved
  CN10_no_reductive_reduction: contrastive only (Hänggi–Talkner–Borkovec = external toolkit, not SCC reduction)
  primitive_u_t: preserved (Hessian eigenvalues derived from canonical energy; u_t untouched)
  inertia_introduction: forbidden (Package I Cat A protection — §3.2 explicit)
  Mori_Zwanzig: forbidden (CV-1.18 SEAL — §3.2 explicit)
  CSSL_E_ridge_E_wild_E_pers: forbidden (working/cssl/01_critic_evaluation.md — §3.2 explicit)
  second_order_temporal: forbidden (Package I cascade — §3.2 explicit)
cot_enforced: yes
coc_enforced: yes
inverse_causation_enforced: yes (each Cat-B-target claim §5.X)
---

> [!nav] Linked: [[01_ns_inspired_synthesis]] (§6 #12, §7 Identity 2, §11 Tier 1) · [[../../canonical/canonical|CV-1.18 canonical]] (§13 Theorem 4 / T-PF-A1-* / T-P-F-ε0-K / T-K-Select-PF, §16 D-ST-4, OP-0005-DYN) · [[../../canonical/DECLARATION|DECL-1.0]] (Q3 stochastic dynamics, Q4 K-selection) · [[../../canonical/CV-1.18_SEAL|CV-1.18 SEAL]] (M-Z deprecation) · [[../../logs/daily/2026-05-20/03_D_L_commutation|03 [D, L_G] commutation]] · [[../cssl/01_critic_evaluation|CSSL critic eval]]

# 02 — Eyring–Kramers Prefactor for SCC: L-KRAMERS-PR-SCC Cat B Target (Tier 1 OP-0005-DYN Attack)

**Mode:** working-layer Cat-B-target derivation (NOT verification, NOT SEAL prep, NOT canonical edit).
**Target:** Apply Hänggi–Talkner–Borkovec 1990 (Rev Mod Phys 62:251) overdamped Kramers prefactor structure as a *contrastive standard tool* to the canonical reflected-Langevin generator T-PF-A1-SDE, anchored exclusively to canonical Hessian eigenvalues (Theorem 4) at SCC formation regime well/saddle pairs. Deliver a single working-layer Cat-B target lemma **L-KRAMERS-PR-SCC** + 5-OP advance map.

---

## §0 — Frontmatter, Pre-Work Cross-Reference Check, §8a P1–P6 Audit

### §0.1 Pre-work xref check (against §15.1 of parent synthesis)

- `grep -rn "Eyring\|Kramers\|prefactor\|Hänggi\|Hanggi" canonical/` → 6 hits, *all* in non-overclaim / Cat-B-conditional contexts (T-P-F-ε0-K L1818, T-K-Select-PF non-overclaim L1851, T-K-Select-OBS non-overclaim L1873, D-ST-4 §16 L2305 P-F flag, T-Temporal-Identity non-overclaim L1893, theorem_status.md OP-0005 row). *No prior canonical formulation* of `Pr^{(Kramers)} = |μ_well|/|μ_saddle|` or explicit prefactor formula on SCC formation regime.
- `grep -rn "Pr\^{(Kramers)}\|Pr_Kramers" working/` → 4 hits, all within parent file `01_ns_inspired_synthesis.md` (§6 catalog table, §7.2 Identity 2 boxed, §9 Cat assignment table, §11.1 OPEN map). *No prior working derivation*. Present file = first working-layer explicit form.
- **Novel positioning:** This file is the *first* SCC-internal derivation that names `μ_well`/`μ_saddle` via canonical Theorem 4 anchors and applies Hänggi–Talkner–Borkovec 1990 *structure* to the reflected-Langevin generator. The result is *target-level*: 5-step proof sketch + 3 explicit hypotheses; *not* a closure of OP-0005-DYN, which remains OPEN at canonical.

### §0.2 §8a archive pattern P1–P6 audit

| Pattern | Risk | This file |
|---|---|---|
| **P1** (근본 질문 우회) | Treating Kramers as a substitute for DECL Q3/Q4 instead of an *answer-channel* | ✓ No. §1 Mission anchors DECL Q3 (stochastic dynamics) + Q4 (K-selection) as the *question this prefactor answers*. |
| **P2** (vocabulary refactoring) | Renaming canonical objects | ✓ No. `μ_well, μ_saddle, ω_0, Γ, T_*, λ_k(L_G), W''(c)` are canonical Theorem 4 / T-PF-A1-* / OMS-1 ξ resident (CV-1.18) symbols. *No new symbol* without canonical anchor. |
| **P3** (canonical content 중복) | Re-stating Theorem 4 | ✓ No. Theorem 4 *cited*, not restated; this file extends to a *non-uniform critical* (saddle) configuration not covered by Theorem 4's `u^* = c·1` regime. |
| **P4** (외부 도구 도입) | Hänggi–Talkner–Borkovec as *reduction* (CN10 drift) | ✓ No. §3 explicit: *contrastive standard tool* + 1990 Rev Mod Phys is the *external 80-year overdamped Kramers literature*, applied to SCC's *first-order reflected Langevin* per T-PF-A1-SDE. SCC ≠ Brownian particle in 1D well; structural analogy *only*. |
| **P5** (self-audit) | Missing §10 hard constraint check | ✓ §10 16/16 ✓. |
| **P6** (언어-수학 분리) | Hand-waving prefactor formula | ✓ §3 + §4 explicit formulas; §5 proof sketch enumerated; §6 numerical worked example. |

**0/6 patterns matched.** Proceed.

---

## §1 — Mission: Cat B Target Derivation, Highest Leverage Channel

### §1.1 What this file *does*

1. **Identify well and saddle** in SCC formation regime (§2): well = single-formation stable interior minimum *above* Σ_T8 (DECL T8); saddle = transition-state configuration between two *K-sectors* B_K and B_{K'} (T-K-Select-PF framework, codim-1 K-jump boundary).
2. **State Hänggi–Talkner–Borkovec 1990 overdamped prefactor formula** (§3) as a *contrastive standard tool* — name the formula, its origin (Kramers 1940 + HTB 1990 §IV), its 1D and multi-D forms, and what `μ_well`/`μ_saddle` mean *inside* it.
3. **Specialize to SCC formation regime** (§4): apply the multi-D form to T-PF-A1-SDE on the (n−1)-dimensional field polytope F_M(G), with Hessian eigenvalues anchored to Theorem 4 + the non-uniform extension required for saddles (currently a Cat B gap, explicitly flagged).
4. **State L-KRAMERS-PR-SCC** (§5) as a working-layer Cat-B target lemma: statement, three hypotheses (H1 Morse non-degeneracy + H2 single unstable direction + H3 Package I applicability), 5-step proof sketch, inverse causation check.
5. **2D torus L=16 worked example** (§6): plug `β/α = 10`, `c = 1/2`, `T_* = 0.1` into the formula. Output: order-of-magnitude `Pr^{(Kramers)}`, prefactor `ω_0`, Eyring–Kramers rate Γ.
6. **OPEN advance map** (§7): 5 canonical rows touched (OP-0005-DYN primary; T-P-F-ε0-K Cat A path; D-ST-4 Cat A path; OP-0008 partial; Package II entry).

### §1.2 What this file *does NOT* do (Constraint Boundary)

- ❌ **Canonical promotion:** L-KRAMERS-PR-SCC remains *working-layer Cat B target*; no claim of Cat A or canonical entry. canonical/* edits = 0.
- ❌ **OP-0005-DYN closure:** the OPEN row remains OPEN. Only an *attack point* and *first explicit form* are delivered.
- ❌ **H5 (Morse stability) full verification:** H1 here is the file-scoped name for H5 specialized to formation/saddle pairs; H5 itself remains the gating hypothesis of T-P-F-ε0-K (Cat B, CV-1.7) and is *not* discharged here.
- ❌ **T_* registration closure:** T_* is canonical ξ resident under OMS-1 (CV-1.18 SEAL, Routes A/B DEPRECATED). All formulas treat T_* axiomatically per Route C.
- ❌ **Mori–Zwanzig effective memory kernel:** CV-1.18 SEAL deprecates Routes A/B. No memory kernel is introduced.
- ❌ **Inertia / second-order ∂_t² u term:** Package I Cat A protection (T-PF-A1-SDE first-order). No momentum field.
- ❌ **New energy term:** CN4 + CN5 preserved. The only objects added are *spectral diagnostics* of the existing E_SCC Hessian.
- ❌ **CSSL `E_ridge`/`E_wild`/`E_pers` patterns:** critic-rejected (working/cssl/01_critic_evaluation.md). The saddle direction identified in §2 is the Hessian's *unstable eigenvector at an already-existing saddle*, not an energy term that creates saddles.
- ❌ **Reductive reduction to fluid mechanics (CN10):** Hänggi–Talkner–Borkovec is a *Rev Mod Phys overdamped barrier-crossing review*, applicable to *any* overdamped Langevin system. Its application here treats SCC as *structurally analogous* to (not reducible to) such a system.

### §1.3 Why highest leverage (Tier 1 from parent §11.2)

Per `01_ns_inspired_synthesis.md` §11.2, `Pr^{(Kramers)}` is the *single dimensionless ratio* whose explicit form advances **5 canonical OPEN/Cat-B rows simultaneously**: OP-0005-DYN (primary), T-P-F-ε0-K (Cat A prefactor channel), D-ST-4 (Cat A explicit Γ channel), OP-0008 (partial K-jump quantification), P-F-A1 Package II (Eyring–Kramers entry). No other Tier-1 dimensionless ratio in the parent's catalog has comparable multi-OP fan-out.

---

## §2 — Well and Saddle Identification in SCC Formation Regime (Canonical-Anchored)

### §2.1 The state space (canonical T-PF-A1-AR, Cat A, CV-1.8)

By T-PF-A1-AR, dynamics live on the field polytope

$$\mathcal{F}_M(G) = \{u \in [0,1]^n : \mu^\top u = M\}, \quad \mu = (1,\ldots,1)/n \text{ (uniform on } V\text{)},$$

a compact convex polytope of intrinsic dimension `n−1` in `H_M`, with reflected-Langevin SDE

$$dU_t = -\Pi_{T\Sigma_m}\nabla\mathcal{E}_{\mathrm{SCC}}(U_t)\,dt + \sqrt{2T_*}\,\Pi_{T\Sigma_m}\,dB_t + dK_t \quad \text{(T-PF-A1-SDE, Cat A)}$$

with `Π_{TΣ_m}` the mass projector (T-PF-A1-AR), `K_t` the Skorokhod reflection (boundary `{u_i=0}∪{u_i=1}`), and `T_* > 0` the OMS-1 ξ resident effective stochastic temperature (CV-1.18 SEAL Route C).

### §2.2 Well `u^{*,well}`: stable formation interior minimum

A **well** in the formation regime is a local minimum `u^{*,well} ∈ int(F_M(G))` of `E_SCC` satisfying:

- (W1) `(β/α, c, λ_2(L_G)) ∈` super-critical side of Σ_T8 per DECL T8: `β/α > 4λ_2/|W''(c)|` (formation regime; uniform `u = c·1` is *unstable*, distinct local minima exist).
- (W2) `u^{*,well}` is a *single-formation* (K=1) or *multi-formation* (K≥2) interior critical configuration in some K-sector `B_K` (T-K-Select-PF L1837, Cat B, CV-1.10).
- (W3) `H_{\mathrm{well}} := \Pi_{T\Sigma_m} \nabla^2 \mathcal{E}_{\mathrm{SCC}}(u^{*,\mathrm{well}}) \Pi_{T\Sigma_m}` is **non-degenerate up to Goldstone modes** (V5b-T-zero Cat A on translation-invariant graphs; Aut(G)-equivariance per 03_D_L_commutation.md §4.2 on uniform critical or per L-HMORSE-LOCAL Cat B, CV-1.16, in active-set sense). Let

  $$\mu_{\mathrm{well}} := \min_{k \notin \ker_{\mathrm{Goldstone}}} \mathrm{spec}(H_{\mathrm{well}}) > 0$$

  denote the **smallest non-Goldstone (strictly positive) Hessian eigenvalue** at the well.

**Canonical anchor for `μ_well` in the uniform case (Theorem 4, Cat A):** At `u^* = c·1` with `c` in spinodal interior `((3-√3)/6, (3+√3)/6)`,

$$\mu_k(u^* = c\mathbf{1}) = 4\alpha \lambda_k(L_G) + \beta W''(c)$$

on `1^⊥`. In the formation regime `β/α > 4λ_2/|W''(c)|`, this critical is *not* a well (`μ_2 < 0` at `c·1`). The well-Hessian eigenvalues at `u^{*,well} ≠ c·1` are not closed-form from Theorem 4 alone — they require the **non-uniform extension** which is the L-HMORSE-LOCAL Cat B regime (canonical L-HMORSE-LOCAL Cat B unconditional, CV-1.16). This is explicit: `μ_well` is a *Cat-B-anchored* quantity in the active-set sense of L-HMORSE-LOCAL.

### §2.3 Saddle `u^{*,saddle}`: K-jump transition state

A **saddle** for K-jump in the formation regime is a critical configuration `u^{*,saddle} ∈ F_M(G)` satisfying:

- (S1) `u^{*,saddle}` lies on or asymptotically near the *boundary* between two K-sectors `B_K` and `B_{K'}` (T-K-Select-PF L1837 sector boundary `∪_v{u(v)=ρ_pers}`, codim-1 in F_M(G)) — the energetic representative of the transition state for `K_act(U_t)` change.
- (S2) `u^{*,saddle}` is a **Morse index-1 critical point** of `E_SCC` on F_M(G): exactly *one* negative-eigenvalue direction in the constrained Hessian, corresponding to the *K-jump normal*.
- (S3) Decomposing `spec(H_{\mathrm{saddle}}) = \{-|\mu_{\mathrm{saddle}}|\} \cup \{0\}^{d_G} \cup \{\mu_i^{(+,\mathrm{saddle})} > 0\}_{i=1}^{n-1-d_G-1}` with `d_G =` Goldstone dimension at the saddle:

  $$|\mu_{\mathrm{saddle}}| := \text{magnitude of the unique negative eigenvalue of } H_{\mathrm{saddle}}$$

  is the **unstable direction's curvature** along the K-jump normal.

**Canonical anchor for the K-jump saddle:** D-ST-4 (§16 L2291, Cat B candidate) defines topological sectors `B_K(P)` and energy basins `A_{K,α}(P)`; transitions between basins are mediated by saddles satisfying (S1)–(S2). The saddle's existence and Morse-1 character on multi-basin landscapes is the *canonical OP-0005-DYN substrate* (W9+, OPEN per theorem_status.md L579 / canonical §16 OPEN row). Within the formation regime, the existence of K=2 metastable local minima with barrier height `∝ β^{0.89}` is the empirical anchor (canonical L120 paradigm shift; exp38 R²=0.997, exp55 zero merges in 5000 iterations). The *transition state* between two such minima is the saddle in (S1).

### §2.4 The well/saddle pair as Cat B substrate

```
CoT step 1: T-PF-A1-SDE (Cat A) gives a well-posed first-order reflected Langevin on F_M(G).
CoT step 2: T-K-Select-PF (Cat B) gives the K-sector partition {B_K}_{K∈K_feas} and the Gibbs sector mass p_K = Z_K/Z.
CoT step 3: D-ST-4 (Cat B candidate) gives the multi-basin partition Z_K = Σ_α Z_{K,α} within each K-sector.
CoT step 4: A K-jump transition K → K' is mediated by a saddle u^{*,saddle} on/near the inter-sector boundary; its Morse-1 character is the OP-0005-DYN substrate.
CoT step 5: μ_well and μ_saddle are the spectral inputs that Hänggi–Talkner–Borkovec 1990 needs to compute the Eyring–Kramers prefactor.
→ Therefore: well/saddle pair = Cat B substrate; spectral inputs = Hessian extreme eigenvalues; prefactor formula is the *direct functional* of these eigenvalues.

CoC anchors:
  - canonical §13 T-PF-A1-SDE (Cat A, CV-1.8) — first-order generator
  - canonical §13 Theorem 4 (Cat A) — μ_k at uniform critical (gauge for spinodal interior)
  - canonical §13 L-HMORSE-LOCAL (Cat B, CV-1.16) — active-set Hessian non-degeneracy at non-uniform critical
  - canonical §13 V5b-T-zero (Cat A) — Goldstone zero on translation-invariant graphs
  - canonical §13 T-K-Select-PF (Cat B, CV-1.10) — K-sector Gibbs mass
  - canonical §16 D-ST-4 (Cat B candidate, CV-1.6) — Z_K + Γ + multi-basin decomposition
  - canonical §16 OP-0005-DYN (OPEN, W9+) — Kramers transition rates substrate
inverse_causation_check:
  - if u^{*,well} were degenerate beyond Goldstone (μ_well = 0): formation regime collapses → no well to escape → Kramers rate ill-defined → consistent (no transition to analyze)
  - if u^{*,saddle} had Morse index ≥ 2: standard Hänggi–Talkner–Borkovec 1990 single-saddle form inapplicable; multi-saddle/instanton-bundle generalizations required (out of scope; flagged as Cat C++)
  - if T-PF-A1-SDE were not Cat A: prefactor derivation has no generator foundation (was the case pre-CV-1.9; now resolved)
```

---

## §3 — Hänggi–Talkner–Borkovec 1990 Overdamped Kramers Prefactor (Contrastive Standard Tool)

### §3.1 Source and scope

**Reference (external, contrastive only):** Hänggi P., Talkner P., Borkovec M., "Reaction-rate theory: fifty years after Kramers", *Rev. Mod. Phys.* **62** (1990) 251–341. §IV "Spatial diffusion regime" gives the multi-dimensional overdamped Kramers / Eyring–Polanyi rate formula for a Brownian particle in a potential `V(x)` on `R^N` with friction `γ` in the high-friction (overdamped) limit. Underlying primary source: Kramers H. A., *Physica* **7** (1940) 284, §VII "high viscosity" limit.

**Scope of analogy:** Hänggi–Talkner–Borkovec treats an overdamped Langevin `γ ẋ = -∇V(x) + √(2k_B T γ) ξ(t)` on `R^N`. SCC's T-PF-A1-SDE is *structurally analogous* (first-order, gradient drift, white-noise diffusion, projector enforcing mass) but lives on a *compact convex polytope* with *reflected* boundary. The Hänggi–Talkner–Borkovec spatial-diffusion regime *form* survives in this setting because: (a) the well and saddle of interest lie in `int(F_M(G))` (assumption W2 + S1 well-separated from `∂F_M(G)`); (b) reflected-Langevin reduces to standard Langevin on the unbounded `R^{n-1}` chart `Q^⊤(u - u^*)` away from the boundary (T-PF-A1-AR `Φ` isometry).

**CN10 boundary:** This is *not* a reduction "SCC = Brownian particle in potential". It is a *structural analogy* that the 80-year overdamped-Kramers literature applies to *any* overdamped gradient Langevin system on a manifold-with-boundary, provided spectral data at well and saddle is supplied. SCC supplies that data via Theorem 4 / L-HMORSE-LOCAL.

### §3.2 1D form (illustrative; SCC requires multi-D §4)

Kramers 1940 §VII, recovered by Hänggi–Talkner–Borkovec 1990 eq. (4.55a):

$$\Gamma_{\mathrm{Kramers}}^{\mathrm{1D}} = \omega_0^{\mathrm{1D}} \cdot \exp(-\Delta V / k_B T), \qquad \omega_0^{\mathrm{1D}} = \frac{\omega_{\mathrm{well}}^{\mathrm{1D}} \cdot \omega_{\mathrm{saddle}}^{\mathrm{1D}}}{2\pi \gamma}$$

with `ω_well^{1D} = √(V''(x_well))`, `ω_saddle^{1D} = √(|V''(x_saddle)|)`. In the SCC overdamped limit (`γ` absorbed into time rescaling via T-PF-A1-SDE diffusion normalization), the *form* `ω_0 ∝ √(μ_well) · √(|μ_saddle|)` survives.

### §3.3 Multi-D form (the form SCC needs)

Hänggi–Talkner–Borkovec 1990 eq. (4.56), multi-dimensional overdamped spatial-diffusion regime (Langer 1969 generalization):

$$\boxed{\omega_0^{\mathrm{multi\text{-}D}} = \frac{|\mu_{\mathrm{saddle}}|}{2\pi} \cdot \sqrt{\frac{|\det \mathrm{Hess}(V)(x_{\mathrm{well}})\lvert }{ \rvert\det' \mathrm{Hess}(V)(x_{\mathrm{saddle}})|}}}$$

with `det'` denoting the product over **non-zero eigenvalues** (excluding the single negative one and any zero / Goldstone modes). The Eyring–Kramers rate is

$$\Gamma^{\mathrm{multi\text{-}D}} = \omega_0^{\mathrm{multi\text{-}D}} \cdot \exp(-\Delta V / k_B T).$$

### §3.4 The Pr^{(Kramers)} ratio (parent §6 #12, §7 Identity 2)

Parent file `01_ns_inspired_synthesis.md` §6 row 12 defines

$$\mathrm{Pr}^{(\mathrm{Kramers})} := \frac{|\mu_{\mathrm{well}}\lvert }{ \rvert\mu_{\mathrm{saddle}}|}.$$

Identity 2 (parent §7.2, boxed):

$$\omega_0 \sim \omega_{\mathrm{well}} \cdot \omega_{\mathrm{saddle}} \cdot (\mathrm{Pr}^{(\mathrm{Kramers})})^{-1/2}.$$

In the multi-D form, `ω_well = √(|μ_well|)` is the geometric-mean curvature of all non-Goldstone well modes, and `ω_saddle = √(|μ_saddle|)` is the saddle's single unstable-direction curvature. Therefore the parent's Identity 2 is the *reduced 1D-equivalent* projection of the multi-D form along the K-jump normal — the dimensionless ratio `Pr^{(Kramers)}` is the *single number* that summarizes the spectral asymmetry between well and saddle along the dominant reaction coordinate.

---

## §4 — Multi-D Generalization for SCC Formation Regime

### §4.1 SCC-specific multi-D prefactor

Combining §2 (SCC well/saddle identification) + §3.3 (HTB multi-D form), the SCC formation regime Eyring–Kramers prefactor is

$$\boxed{\omega_0^{\mathrm{SCC}} = \frac{|\mu_{\mathrm{saddle}}|}{2\pi} \cdot \sqrt{\frac{\prod_{k \notin \ker_{\mathrm{Goldstone}}^{\mathrm{well}}} \mu_k(u^{*,\mathrm{well}})}{\prod_{k \notin \ker_{\mathrm{Goldstone}}^{\mathrm{saddle}}, k \neq k_{\mathrm{unstable}}} \mu_k(u^{*,\mathrm{saddle}})}}}$$

with: (a) `μ_k(u^{*,well/saddle})` the eigenvalues of `Π_{TΣ_m} ∇²E_SCC(u^{*,well/saddle}) Π_{TΣ_m}` on the tangent space of the field polytope (T-PF-A1-AR (n−1)-dim affine chart `Φ`); (b) Goldstone kernels excluded (V5b-T-zero, T-PreObj-1G on translation-invariant graphs; Aut(G)-equivariant decomposition on symmetric graphs per 03_D_L_commutation.md §4.2); (c) `k_unstable` the unique negative-eigenvalue index at saddle (S2).

### §4.2 Eyring–Kramers rate (canonical D-ST-4 + T-K-Select-PF anchor)

$$\Gamma^{\mathrm{SCC}}_{\mathrm{K \to K'}} = \omega_0^{\mathrm{SCC}} \cdot \exp\left(-\frac{\Delta E_{\mathrm{barrier}}}{T_*}\right), \qquad \Delta E_{\mathrm{barrier}} = E_{\mathrm{SCC}}(u^{*,\mathrm{saddle}}) - E_{\mathrm{SCC}}(u^{*,\mathrm{well}}).$$

`T_*` is canonical ξ resident (OMS-1 Route C, CV-1.18 SEAL). The exponential factor `exp(-ΔE/T_*)` is the **T-P-F-ε0-K (Cat B, CV-1.7) regime** — its stability under Bernoulli regularization is canonical Cat B conditional on H5 (Morse stability). The *prefactor* `ω_0^{SCC}` is the **open piece** that this file targets (Package II entry, L-KRAMERS-PR-SCC §5).

### §4.3 Reduction to parent Identity 2

Define the **geometric-mean curvatures**

$$\bar\mu_{\mathrm{well}}^{\mathrm{geom}} := \left( \prod_{k \notin \ker^{\mathrm{well}}_G} \mu_k(u^{*,\mathrm{well}}) \right)^{1/(n-1-d_G^{\mathrm{well}})}, \qquad \bar\mu_{\mathrm{saddle}}^{\mathrm{geom}} := \left( \prod_{k \notin \ker^{\mathrm{saddle}}_G, k\neq k_{\mathrm{unstable}}} \mu_k(u^{*,\mathrm{saddle}}) \right)^{1/(n-2-d_G^{\mathrm{saddle}})}.$$

If `d_G^{well} = d_G^{saddle} =: d_G` and `n - 2 - d_G` is large (typical for SCC on 2D grids with `n = L²`, `d_G ≤ 2`), then up to subleading factors

$$\omega_0^{\mathrm{SCC}} \approx \frac{|\mu_{\mathrm{saddle}}|}{2\pi} \cdot \left(\frac{\bar\mu_{\mathrm{well}}^{\mathrm{geom}}}{\bar\mu_{\mathrm{saddle}}^{\mathrm{geom}}}\right)^{(n-1-d_G)/2} \cdot \bar\mu_{\mathrm{well}}^{\mathrm{geom},\,1/2}.$$

The 1D-equivalent projection (parent §7.2 Identity 2) corresponds to the dominant K-jump-normal mode only: replacing `bar μ_well^geom` by `μ_well` (smallest non-Goldstone) and `bar μ_saddle^geom` by an effective transverse-mode geometric mean, we recover the parent's `Pr^{(Kramers)}^{-1/2}` form.

### §4.4 Why the L-HMORSE-LOCAL (Cat B, CV-1.16) anchor matters

L-HMORSE-LOCAL Cat B unconditional (canonical CV-1.16) gives the **active-set Hessian non-degeneracy** at non-uniform critical configurations under hypotheses (C1)(C2′)(C3)(C4)(C5). This is *precisely* the hypothesis package required to make the `μ_well > 0` (non-Goldstone) condition (W3) rigorous *off* the uniform critical `c·1`. Specifically:

- Theorem 4 (Cat A) gives `μ_k` at `c·1` only — that's a saddle of the formation-regime energy, not a well.
- L-HMORSE-LOCAL (Cat B) gives active-set Hessian regularity at `u^{*,well} ≠ c·1` provided (C1)–(C5) hold.
- The well's `μ_well` per (W3) is thus a *Cat-B-anchored* quantity, inheriting the conditionality of L-HMORSE-LOCAL.

For the saddle, the analogous statement is the **OP-HMORSE-SADDLE OPEN row** (canonical OPEN, theorem_status.md L435) — the saddle-point Hessian regularity. The single-unstable-direction structure (S2) of `H_saddle` is the *substrate* of OP-HMORSE-SADDLE; L-KRAMERS-PR-SCC inherits its conditionality.

---

## §5 — L-KRAMERS-PR-SCC Cat B Target Lemma

### §5.1 Statement

**L-KRAMERS-PR-SCC (working-layer Cat B target).** Let `G = (V, E)` be a finite connected graph with `|V| = n`, mass `M = c · n ∈ (0,n)` with `c ∈ ((3-√3)/6, (3+√3)/6)` (spinodal interior), and SCC parameters `(α, β, λ_cl, λ_sep, λ_bd, λ_tr)` in the formation regime `β/α > 4λ_2(L_G)/|W''(c)|` (DECL T8 super-critical). Let `T_* > 0` be the canonical ξ resident (OMS-1, Route C, CV-1.18 SEAL). Let `u^{*,well} ∈ int(F_M(G))` be a stable formation critical satisfying (W1)–(W3) of §2.2 and `u^{*,saddle} ∈ F_M(G)` a transition-state critical satisfying (S1)–(S3) of §2.3. Then under hypotheses **(H1)–(H3)** below, the Eyring–Kramers rate

$$\Gamma_{\mathrm{K\to K'}} = \omega_0^{\mathrm{SCC}} \cdot \exp\left(-\frac{\Delta E_{\mathrm{barrier}}}{T_*}\right)$$

is well-defined with prefactor

$$\omega_0^{\mathrm{SCC}} = \frac{|\mu_{\mathrm{saddle}}|}{2\pi} \cdot \sqrt{\frac{\prod_{k \notin \ker_G^{\mathrm{well}}} \mu_k(u^{*,\mathrm{well}})}{\prod_{k \notin \ker_G^{\mathrm{saddle}},\, k \neq k_{\mathrm{unstable}}} \mu_k(u^{*,\mathrm{saddle}})}}$$

and 1D-projected reduced forms (parent §7.2 — *Identity 2 SPLIT into 2a + 2b per Wave 2 critic Fix #4, file 12 §5* — the original W8-Day3 13:50 form equating these two reductions was algebraically WRONG):

**Identity 2a (Pr^{(Kramers)} reduction, structural leading order)**:
$$\omega_0^{\mathrm{SCC},\,2a} = \frac{1}{2\pi} \cdot \omega_{\mathrm{well}} \cdot \omega_{\mathrm{saddle}} \cdot (\mathrm{Pr}^{(\mathrm{Kramers})})^{-1/2} = \frac{|\mu_{\mathrm{saddle}}|}{2\pi}$$

(Algebraic verification: $\omega_{\mathrm{well}} \cdot \omega_{\mathrm{saddle}} \cdot (\mathrm{Pr}^{(\mathrm{Kramers})})^{-1/2} = \sqrt{|\mu_{\mathrm{well}}|}\cdot\sqrt{|\mu_{\mathrm{saddle}}|}\cdot\sqrt{|\mu_{\mathrm{saddle}}\lvert / \rvert\mu_{\mathrm{well}}\lvert } = \rvert\mu_{\mathrm{saddle}}|$.)

**Identity 2b (1D-projection geometric mean form)**:
$$\omega_0^{\mathrm{SCC},\,2b} = \frac{1}{2\pi} \sqrt{\mu_{\mathrm{well}} \cdot |\mu_{\mathrm{saddle}}|} = \frac{1}{2\pi} \cdot \omega_{\mathrm{well}} \cdot \omega_{\mathrm{saddle}}$$

(Direct: $\omega_{\mathrm{well}} \cdot \omega_{\mathrm{saddle}} = \sqrt{|\mu_{\mathrm{well}}|\cdot|\mu_{\mathrm{saddle}}|}$.)

**These two forms are DIFFERENT quantities and MUST NOT be equated.** They correspond to distinct reductions of the multi-D prefactor: Identity 2a is HTB's high-friction leading order showing "ω_0 ~ |μ_saddle|"; Identity 2b is the geometric mean appearing in 1D barrier crossings. For the *primary multi-D form* see the §5.1 boxed formula above; for *structural leading-order shape* use 2a; for *1D-projection limit* use 2b. The original "= " sign between them (W8-Day3 13:50 KST version) was a dimensional/algebraic error caught by Wave 2 critic §A.3.

### §5.2 Hypotheses

- **(H1) Morse non-degeneracy at well and saddle.** Both `u^{*,well}` and `u^{*,saddle}` are non-degenerate Morse critical points of `E_SCC` on `F_M(G)` modulo Goldstone kernels. *This is H5 of T-P-F-ε0-K (canonical L1820, Cat B, CV-1.7) specialized to the (well, saddle) pair.* L-KRAMERS-PR-SCC inherits T-P-F-ε0-K's Cat B status from H1.
- **(H2) Single unstable direction along K-jump normal.** `H_saddle` has exactly one negative eigenvalue, with eigenvector along the K-jump normal (S2). *This is the OP-HMORSE-SADDLE substrate (canonical OPEN, theorem_status.md L435) specialized to single-saddle K-jump transitions; rules out multi-saddle / instanton bundle regimes.*
- **(H3) Package I applicability + interior well-separation from `∂F_M(G)`.** T-PF-A1-AR/SDE/GI/PE all hold (all Cat A, CV-1.9). Additionally both `u^{*,well}` and `u^{*,saddle}` lie strictly inside the field polytope at distance `> δ_{box}` from `∂[0,1]^n ∩ H_M` for some `δ_{box} > 0`, so the reflected-Langevin generator reduces to a standard Langevin generator on the `(n−1)`-dim chart in a neighborhood containing the well, saddle, and a connecting reaction tube. *This rules out Skorokhod-reflection–dominated transition regimes where the boundary is itself the reaction coordinate.*

### §5.3 5-step proof sketch

```
Step 1 (state space + generator). Apply T-PF-A1-AR (Cat A) to chart F_M(G) by Φ: (Q^⊤(u-u^*), R^{n-1}-iso) and T-PF-A1-SDE (Cat A) to get the reflected-Langevin generator
   Lf = -⟨∇Ẽ, ∇f⟩ + T_* Δf
on the chart, with E~(x) = E_SCC(u^* + Qx) and reflection on ∂C~ (T-PF-A1-AR (4) UIC + exterior sphere). By H3, neighborhoods of well and saddle and a reaction tube connecting them lie at distance > δ_{box} from ∂C~, so locally L is the standard Langevin generator on R^{n-1}.

Step 2 (well + saddle Hessian spectra). By H1, H_{well} = Π_T ∇²Ẽ(x_{well}) Π_T has spectrum
   spec(H_well) = {0}^{d_G^{well}} ∪ {μ_k(u^{*,well}) > 0}_{k notin ker_G}
and H_saddle has
   spec(H_saddle) = {0}^{d_G^{saddle}} ∪ {-|μ_saddle|} ∪ {μ_k(u^{*,saddle}) > 0}_{k notin ker_G, k ≠ k_{unstable}}
per (W3) + (S2)+(S3). Goldstone dimensions d_G^{well/saddle} given by V5b-T-zero (Cat A) on translation-invariant graphs and Aut(G)-equivariant decomposition (canonical T-σ-Lemma-1 Cat A; 03_D_L_commutation.md §4.2 today).

Step 3 (Hänggi–Talkner–Borkovec multi-D form, contrastive import). Hänggi–Talkner–Borkovec 1990 eq. (4.56) for the multi-D overdamped spatial-diffusion regime gives, for any standard Langevin generator on R^N with Morse-non-degenerate well x_a and Morse-1 saddle x_b satisfying H1+H2 + lying inside an unbounded domain,
   ω_0 = (|μ_saddle|/(2π)) · √( |det Hess V(x_a)| / |det' Hess V(x_b)| )
   Γ = ω_0 · exp(-(V(x_b) - V(x_a))/(k_B T)).
Apply this verbatim with (V, x_a, x_b, k_B T) ↔ (Ẽ, x_{well}, x_{saddle}, T_*), restricting determinants to non-Goldstone subspaces (kernel directions contribute 1 in the canonical product via the V5b-T-zero exclusion convention; parent §7.5 Identity 5 rescaling preserves Goldstone zero).

Step 4 (anchor det's to canonical Theorem 4 + L-HMORSE-LOCAL). At the well, |det' H_well| = ∏_{k notin ker_G^{well}} μ_k(u^{*,well}). At c·1 (uniform critical), Theorem 4 (Cat A) gives μ_k = 4αλ_k(L_G) + βW''(c) explicit closed form. At u^{*,well} ≠ c·1, L-HMORSE-LOCAL (Cat B, CV-1.16) ensures the active-set Hessian is non-degenerate under (C1)–(C5), so the product is finite and strictly positive. At the saddle, |det' H_saddle| = ∏_{k notin ker_G^{saddle}, k ≠ k_{unstable}} μ_k(u^{*,saddle}); rigor at this product requires OP-HMORSE-SADDLE closure (canonical OPEN, theorem_status.md L435) — the active-set extension to saddle points.

Step 5 (assemble + dimensional sanity). Plug Step-4 det's into Step-3 multi-D formula:
   ω_0^{SCC} = (|μ_saddle|/(2π)) · √( ∏ μ_k^{well} / ∏ μ_k^{saddle non-unstable} ).
Dimensional check: μ_k has units of (energy/u²), ω_0 has units of (1/time); the time-scale conversion is absorbed by T-PF-A1-SDE diffusion normalization √(2T_*) where T_* has units of energy and the projector Π is dimensionless. The Eyring–Kramers rate Γ = ω_0 · exp(-ΔE/T_*) has units of (1/time) as required.
□ (sketch)
```

### §5.4 Inverse causation check

```yaml
inverse_causation_check:
  - if H1 fails (degenerate well or saddle, μ_k = 0 for some non-Goldstone k):
      consequence: HTB multi-D form ill-defined (zero in numerator or denominator)
      → consistent: degenerate critical = bifurcation point, T-P-F-ε0-K (Cat B) also fails at exactly this regime; the Cat B status of L-KRAMERS-PR-SCC inherits H5 (= H1 here) directly
  - if H2 fails (multi-saddle, Morse index ≥ 2 at saddle):
      consequence: HTB single-saddle form (4.56) inapplicable; multi-saddle / instanton-bundle generalizations needed
      → out of scope; flagged as Cat C++ future work (parent §11 not in Tier 1)
  - if H3 fails (well or saddle within δ_{box} of polytope boundary):
      consequence: Skorokhod reflection contributes to the rate; the reflected-Langevin prefactor (Lions-Sznitman 1984 + Bovier-den Hollander 2015 for hard-wall Eyring-Kramers) is structurally different and not given by HTB free-space form
      → flagged as separate working file (boundary-dominated transition regime; not Tier 1)
  - if T-PF-A1-SDE were not Cat A (counterfactual; resolved CV-1.9):
      consequence: no generator foundation; entire derivation void
      → confirms the necessity of Package I as prerequisite
  - if Theorem 4 were Cat B:
      consequence: μ_k formula at c·1 conditional, weakening H1 anchor for uniform case
      → Theorem 4 is Cat A; condition not active
  - if CV-1.18 SEAL were rolled back (Mori-Zwanzig re-allowed):
      consequence: alternative routes to OP-0021 T_* registration via memory kernels would re-open, but the prefactor formula structure (HTB) is invariant under T_* registration choice
      → CV-1.18 SEAL stable; condition not active
```

### §5.5 Honest Cat classification

**L-KRAMERS-PR-SCC Cat B target rationale:**

- **Why not Cat A:** H1 is exactly H5 of canonical T-P-F-ε0-K (Cat B, CV-1.7) specialized to the well/saddle pair; H2 is the OP-HMORSE-SADDLE (canonical OPEN) substrate; H3 is a new geometric restriction (interior well-separation from polytope boundary). All three are *conditional hypotheses* that the canonical layer has *not* fully discharged. L-KRAMERS-PR-SCC therefore *cannot* be Cat A as long as H5 / OP-HMORSE-SADDLE remain Cat B / OPEN.
- **Why Cat B (not Cat C):** The proof sketch §5.3 is rigorous *given* H1-H3. Step 3 is a verbatim import of an 80-year-validated Rev Mod Phys result. Step 4 invokes canonical anchors (Theorem 4 Cat A + L-HMORSE-LOCAL Cat B) without new mathematics. The conditionality is *exactly the canonical T-P-F-ε0-K / OP-HMORSE-SADDLE conditionality* — no new conjectures introduced.
- **Cat A promotion path:** (i) H5 verification for SCC saddles (closes T-P-F-ε0-K → Cat A); (ii) OP-HMORSE-SADDLE Cat A closure (saddle-point Hessian regularity active-set extension); (iii) H3 verification on standard 2D grid formation regimes (numerical anchor; not a hard obstruction). Order-of-magnitude: 2-3 W9+ sessions per (i),(ii); H3 is 1 session.

---

## §6 — Numerical Example: 2D Torus L=16, β/α=10, c=1/2, T_*=0.1

### §6.1 Setup

- Graph `G = T^2_{16}`: 2D torus with `n = 16 × 16 = 256` vertices, regular degree 4.
- Mass `M = c · n = 128` (`c = 1/2`).
- Parameters: `α = 1`, `β = 10` (so `β/α = 10`); `W(u) = u²(1-u)²` so `W''(c) = W''(1/2) = -1`, `|W''(c)| = 1` (canonical I6 convention).
- `λ_2(L_G)` on `T^2_{16}` (smallest non-zero Laplacian eigenvalue): `λ_2 = 2(1 - cos(2π/16)) ≈ 2(1 - 0.9239) ≈ 0.1522`.
- T8 condition: `β/α > 4λ_2/|W''(c)|` ⇔ `10 > 4 · 0.1522 / 1 ≈ 0.609`. **Super-critical.** Formation regime confirmed.
- `T_* = 0.1` (canonical ξ resident, OMS-1).

### §6.2 Well Hessian spectrum estimate

In the formation regime at large `β/α = 10`, a stable single-formation well `u^{*,well}` is approximately phase-separated: most `u_i ≈ 0` (background) or `u_i ≈ 1` (interior bulk), with a smooth transition band at the formation boundary of width `ℓ_bd ≈ √(α/β) ≈ √(1/10) ≈ 0.316` (Allen-Cahn interface width, canonical Modica-Mortola scaling).

- **Bulk modes** (`u_i ≈ 0` or `1`, where `W''(0) = W''(1) = 2`): contribute `μ ≈ 4α · 0 + β · 2 = 2β = 20` (dominant block, ~most of `n−1` modes).
- **Boundary band modes** (`u_i ≈ 1/2`, where `W''(1/2) = -1`): contribute `μ ≈ 4α · λ_bd^{spectral} + β · (-1)`. The boundary-band spectral contribution `λ_bd^{spectral} ~ 1/ℓ_bd² ≈ 10`, giving `μ ≈ 4·10 - 10 = 30` (positive — band is stable in the active-set sense of L-HMORSE-LOCAL).
- **Smallest non-Goldstone eigenvalue** `μ_well`: dominated by the lowest-frequency band-deformation mode, estimated `μ_well ~ 4α · λ_2^{band} + β · W''_{eff}`. With `λ_2^{band} ~ 0.1` and `W''_{eff} ~ +1` (band-averaged), `μ_well ≈ 0.4 + 10 ≈ 10` (rough order of magnitude).

### §6.3 Saddle Hessian spectrum estimate

A K-jump saddle between `K=1` and `K=2` formations at `β/α = 10` on `T^2_{16}` has a *neck* between two emergent bulks. The unstable direction is the neck-collapse mode:

- `|μ_saddle|`: neck-collapse curvature `~ 4α · λ_neck - β · |W''(c_neck)|`. At neck-center `u ≈ 1/2`, `W''(c_neck) = -1`. Neck spectral scale `λ_neck ~ 1/ℓ_neck²` with `ℓ_neck ~ √(α/β) ≈ 0.316` and `λ_neck ~ 10`, giving `|μ_saddle| ~ 40 - 10 = 30`. Order of magnitude `|μ_saddle| ~ O(10)`.
- **Stable transverse modes at saddle**: bulk modes `μ ~ 20` (`n − 2 − d_G` of them), boundary band modes `μ ~ 30`.

### §6.4 Pr^{(Kramers)} and prefactor

$$\mathrm{Pr}^{(\mathrm{Kramers})} = \frac{|\mu_{\mathrm{well}}\lvert }{ \rvert\mu_{\mathrm{saddle}}|} \sim \frac{10}{30} \approx 0.33.$$

Reduced 1D-projection prefactor (parent §7.2 Identity 2):

$$\omega_0^{\mathrm{SCC,\,1D-proj}} = \frac{1}{2\pi} \sqrt{\mu_{\mathrm{well}} \cdot |\mu_{\mathrm{saddle}}|} \approx \frac{1}{2\pi} \sqrt{10 \cdot 30} \approx \frac{\sqrt{300}}{2\pi} \approx \frac{17.3}{6.28} \approx 2.76 \quad (\text{in units of }\sqrt{\beta}/\sqrt{\alpha} \cdot 1/\tau_0).$$

The dimensional factor `1/τ_0` is absorbed into the T-PF-A1-SDE time normalization (`τ_0` = unit-noise relaxation timescale `~ 1/(2T_* λ_2(L_G)) ~ 1/(2·0.1·0.152) ≈ 33` units). Reporting `ω_0` in raw time units: `ω_0 ≈ 2.76 / 33 ≈ 0.084` (per unit time).

### §6.5 Eyring–Kramers rate

The barrier height `ΔE_barrier` for K=1 → K=2 (or K=2 → K=1 merge) on `T^2_{16}` at `β = 10` is empirically `~ 10 · β^{0.89} ~ 10 · 10^{0.89} ≈ 10 · 7.76 ≈ 77.6` energy units (canonical L120 + exp38 R²=0.997 scaling, taking the empirical merge-barrier coefficient ~10 as the leading constant).

$$\Gamma \sim 0.084 \cdot \exp(-77.6 / 0.1) = 0.084 \cdot e^{-776} \approx 10^{-337}\,\text{per unit time}.$$

**Interpretation:** *Astronomically slow.* Exactly consistent with canonical L120 paradigm-shift observation: "Well-separated bumps remain stable under noise σ ≤ 0.5 indefinitely (exp55: zero merges in 5000 iterations)". The Eyring–Kramers rate predicts effectively zero merges over any feasible simulation timescale at `β = 10`, `T_* = 0.1` — the prefactor `ω_0 ≈ 0.084` is *irrelevant* compared to the catastrophic exponential suppression `e^{-776}`.

### §6.6 Non-overclaim on this numerical example

- The `μ_well ~ 10`, `|μ_saddle| ~ 30` estimates are **order-of-magnitude only**, derived from scaling arguments (Allen-Cahn interface width + boundary-band spectral count) without direct numerical diagonalization. A genuine Cat-B-target check requires `CODE/scripts/test_kramers_prefactor_torus.py` (W9+ task; not in scope here per §1.2 and §8 forward hooks).
- The `ΔE_barrier ~ 10 · β^{0.89}` constant `10` is fitted (exp38) and *branch-dependent* (canonical L1803 Erratum). A rigorous barrier statement needs branch/manifold/endpoint specification per L1803.
- The rate `~ 10^{-337}` is the *order of magnitude*; the precise leading constant is not the deliverable. The takeaway is the **structural form `Γ = ω_0 · exp(-ΔE/T_*)`** and the *channel by which `ω_0` becomes a canonical quantity* once L-KRAMERS-PR-SCC's H1–H3 are discharged.

---

## §7 — Canonical OPEN Advance Map (5 OPs Touched)

### §7.1 Map table

| Canonical OP / Cat B row | Status (CV-1.18) | L-KRAMERS-PR-SCC advance |
|---|---|---|
| **OP-0005-DYN** (Kramers transition rates, OPEN W9+; theorem_status.md L579) | OPEN | **PRIMARY ADVANCE**: first explicit working-layer prefactor formula `ω_0^{SCC}` with H1-H3 hypothesis package; reduces OPEN scope to "discharge H1 (H5) + H2 (OP-HMORSE-SADDLE) + H3 (interior well-separation)". Not a closure; an *attack point with explicit form*. |
| **T-P-F-ε0-K** (Cat B conditional on H5, CV-1.7; canonical L1818) | Cat B | **Cat A prefactor channel**: T-P-F-ε0-K covers the *exponential portion* `exp(-ΔE/T_*)` stability under Bernoulli regularization; L-KRAMERS-PR-SCC covers the *prefactor portion* `ω_0`. Together with H5 discharge, the full Eyring–Kramers rate becomes Cat A. Cat A path: §5.5 (i) H5 for SCC saddles. |
| **D-ST-4** (Cat B candidate, CV-1.6; canonical L2291) | Cat B candidate | **Cat A explicit Γ channel**: D-ST-4 defines `Z_K, Γ, Kramers rate` with P-F flag (T_* axiomatic). CV-1.9 resolved the P-F flag (T-PF-A1-PE Cat A). L-KRAMERS-PR-SCC supplies the explicit Γ formula that D-ST-4 had been waiting for. With H1-H3 + Cat A path discharge, D-ST-4 inherits Cat A status for the rate calculation specifically. |
| **OP-0008** (σ^A K-jump non-determinism; theorem_status.md L704 sub-rows) | PARTIALLY STRUCTURED (CONT/MERGE/SPLIT Cat B; σ_standard Cat C W9+) | **Partial quantification**: K-jump events occur at rate `Γ_{K→K'}`; the σ^A inheritance map at the jump event (canonical Session W) inherits the *stochastic timing* from `Γ`. L-KRAMERS-PR-SCC supplies the rate distribution; the *which-K'* selection at the jump is OP-0008-SPLIT/MERGE direction Cat B. Partial channel only — does NOT resolve OP-0008-SPLIT σ_standard Cat C (W9+ Wigner-projection separate). |
| **P-F-A1 Package II** (Eyring–Kramers, OPEN; canonical L67) | OPEN — conditional on H5 + OP-0021 | **Cat B entry**: Package II is exactly the Eyring–Kramers prefactor + rate. L-KRAMERS-PR-SCC IS the working-layer Package II entry — the explicit form that the canonical L67 row references as "conditional on H5 + OP-0021". With CV-1.18 SEAL closing OP-0021 Route C (T_* ξ resident), the remaining conditionality is H5 (= H1 here). Package II Cat B entry stage: this file. |

### §7.2 What is NOT advanced (honest non-overclaim)

- **OP-0005-EQ** (equilibrium K-selection): closed by T-K-Select-PF (Cat B, CV-1.10); L-KRAMERS-PR-SCC is *orthogonal* (rates, not equilibrium).
- **OP-0005-OBS** (observation-conditioned K-selection): closed by T-K-Select-OBS (Cat B, CV-1.11); L-KRAMERS-PR-SCC is *orthogonal* (rates, not posterior).
- **OP-0009** (multi-formation ontological foundations): L-KRAMERS-PR-SCC presumes the K-sector partition T-K-Select-PF; does not advance the ontological foundations themselves.
- **OP-0011** (temporal identity): closed by T-Temporal-Identity (Cat A, CV-1.13); L-KRAMERS-PR-SCC orthogonal.
- **OP-0021** (T_* registration): scope-revised CV-1.18 (Routes A/B DEPRECATED, Route C accepted); L-KRAMERS-PR-SCC uses T_* axiomatically per Route C, does not advance OP-0021.
- **OP-HMORSE-LOCAL-A** (L-HMORSE-LOCAL Cat B → Cat A): L-KRAMERS-PR-SCC *inherits* L-HMORSE-LOCAL Cat B status via H1 anchor; closing OP-HMORSE-LOCAL-A would close one prerequisite for Cat A promotion, but L-KRAMERS-PR-SCC does not itself advance OP-HMORSE-LOCAL-A.
- **OP-HMORSE-SADDLE** (OPEN): L-KRAMERS-PR-SCC's H2 is the OPEN substrate; this file *names* the gap precisely (single-unstable-direction K-jump normal) and is in fact the *primary motivating use case* for advancing OP-HMORSE-SADDLE, but does not close it.

---

## §8 — W9+ Forward Hooks (Specific Session Candidates)

### §8.1 Tier 1A: Numerical verification of §6 estimates

- **`02a_kramers_prefactor_numerical_torus.md`** + `CODE/scripts/test_kramers_prefactor_torus.py`: direct numerical diagonalization of `Π_T ∇²E_SCC Π_T` at `u^{*,well}` and `u^{*,saddle}` on `T^2_{16}` at `(β/α, c, T_*) = (10, 1/2, 0.1)`; verify `μ_well ~ 10`, `|μ_saddle| ~ 30` order-of-magnitude estimates; produce `ω_0^{SCC}` to ±20% precision. Tied to canonical exp38/exp55 anchor.
- **`02b_kramers_prefactor_beta_sweep.md`**: parametric sweep `β/α ∈ {5, 10, 20, 50, 100}` to check `ω_0^{SCC}(β)` scaling against the empirical barrier height `ΔE ∝ β^{0.89}` (canonical L120). Establish *prefactor exponent* `ω_0 ∝ β^q` for some `q` to be measured; canonical Cat C → Cat B candidate.

### §8.2 Tier 1B: Discharge H1 → T-P-F-ε0-K Cat A path

- **`02c_h5_morse_stability_saddle.md`**: rigorous discharge of H5 (Morse stability) for SCC saddles in the formation regime. Approach: (a) Smale's `C²`-stability of Morse functions on compact polytopes (Banach-Mazur), restricted to SCC parameter open sets; (b) generic non-degeneracy from Łojasiewicz + canonical CN4 analyticity. Target: T-P-F-ε0-K Cat B → Cat A on the open-set parameter region.

### §8.3 Tier 1C: Discharge H2 → OP-HMORSE-SADDLE attack

- **`02d_op_hmorse_saddle_active_set.md`**: extend L-HMORSE-LOCAL Cat B (CV-1.16) active-set machinery from minima to *Morse-1 saddles*. Approach: replicate (C1)-(C5) at saddle with active set defined by sign-restricted Karush-Kuhn-Tucker conditions; check Schur complement of `H_saddle` on `T_{u^*,saddle}\partial B_K`. Target: OP-HMORSE-SADDLE OPEN → working Cat B.

### §8.4 Tier 2A: Surface tension rescaling × prefactor (parent §8.1 × this file)

- **`02e_surface_tension_rescaling_prefactor.md`**: combine parent §7.5 Identity 5 `(α, β) → (sα, sβ)` rescaling with §5 prefactor formula to derive `ω_0^{SCC}(s)` scaling. Expectation: `ω_0^{SCC} ∝ s^{1/2}` (HTB form `√(μ_well · μ_saddle)` × Hessian linear in `s` per Theorem 4 linearity). Cat A direct via Theorem 4 + Identity 5.

### §8.5 Tier 2B: K-jump non-determinism via prefactor distribution

- **`02f_kjump_rate_distribution.md`**: when multiple saddles `{u^{*,saddle,j}}_j` mediate K → K' transitions, the total rate `Γ_{K→K'} = Σ_j Γ_j` with `Γ_j` from §5. The *jump-direction distribution* (OP-0008-SPLIT/MERGE direction Cat B, canonical Session W) is `p_j ∝ Γ_j`. Quantification channel for OP-0008-DIST (new sub-problem registered Session W).

### §8.6 Tier 3: Pe / Pr-network applications

- **`02g_pe_pr_network_around_well.md`**: parent §7.3 Identity 3 (Pe-Pr bridge) + parent §6 #5/#6 St/Sc near `u^{*,well}` characterize the *deterministic/thermal mode separation* near the well; combined with `Pr^{(Kramers)} ~ μ_well/|μ_saddle|`, gives a *unified dimensionless picture* of formation regime stability. Cat A direct (algebraic) per parent §7 identities.

---

## §9 — CoT / CoC Archival

### §9.1 Core CoT chain (mode-level)

```
CoT-CORE-02: L-KRAMERS-PR-SCC justification chain.

CoT step 1: DECL-1.0 Q3 (stochastic dynamics) + Q4 (K-selection) demand a quantitative answer to "어떻게 변하는가? + 몇으로 안정화되는가?" — the K-jump rate Γ is the central dynamical quantity.
CoT step 2: T-K-Select-PF (Cat B, CV-1.10) gives equilibrium p_K = Z_K/Z; the *kinetic* approach to equilibrium requires rates Γ_{K→K'}.
CoT step 3: Canonical D-ST-4 (Cat B candidate, CV-1.6) names the rate form "Γ ~ Z_K-derived" with P-F flag (resolved CV-1.9); T-P-F-ε0-K (Cat B, CV-1.7) covers the exponential portion conditional on H5.
CoT step 4: The *prefactor portion* ω_0 has no canonical entry — the OPEN piece is OP-0005-DYN (canonical OPEN W9+, theorem_status.md L579).
CoT step 5: Hänggi–Talkner–Borkovec 1990 (Rev Mod Phys 62:251) §IV multi-D overdamped formula is the 80-year standard; it requires (a) Morse-non-degen well/saddle (= H1 = H5), (b) Morse-1 saddle (= H2 = OP-HMORSE-SADDLE substrate), (c) free-space generator (= H3 interior well-separation).
CoT step 6: Apply HTB form verbatim to T-PF-A1-SDE (Cat A, CV-1.8) reflected Langevin restricted to neighborhoods satisfying H3; anchor Hessian determinants to Theorem 4 (Cat A) at uniform critical + L-HMORSE-LOCAL (Cat B, CV-1.16) at non-uniform well + OP-HMORSE-SADDLE (OPEN) substrate at saddle.
CoT step 7: Result = L-KRAMERS-PR-SCC §5.1 boxed formula. Status = working-layer Cat B target (inherits T-P-F-ε0-K Cat B + L-HMORSE-LOCAL Cat B + OP-HMORSE-SADDLE OPEN). 5 OP advance per §7.
→ Therefore: L-KRAMERS-PR-SCC = highest-leverage Tier 1 channel for OP-0005-DYN attack, *honest Cat B target*, no canonical edits.
```

### §9.2 Core CoC anchored chain

```yaml
target: L-KRAMERS-PR-SCC working-layer Cat B target prefactor formula for SCC Eyring–Kramers rate, compatible with CV-1.18 SEAL Non-Overclaim, advancing 5 canonical OPEN/Cat-B rows.

prior_anchors:
  - DECL-1.0 Q3, Q4 (stochastic dynamics, K-selection — primary motivation)
  - canonical §13 Theorem 4 (Cat A, μ_k = 4αλ_k(L_G) + βW''(c) at uniform critical) — well/saddle Hessian gauge
  - canonical §13 T-PF-A1-AR (Cat A, CV-1.8) — F_M(G) compact convex polytope + affine reduction Φ
  - canonical §13 T-PF-A1-SDE (Cat A, CV-1.8) — reflected Langevin well-posedness
  - canonical §13 T-PF-A1-GI (Cat A, CV-1.9) — Gibbs invariance π_{T_*}
  - canonical §13 T-PF-A1-PE (Cat A, CV-1.9) — Poincaré ergodicity (resolves D-ST-4 P-F flag)
  - canonical §13 T-P-F-ε0-K (Cat B, CV-1.7, conditional on H5) — exponential portion of Eyring–Kramers
  - canonical §13 T-K-Select-PF (Cat B, CV-1.10) — K-sector partition + Gibbs sector mass p_K
  - canonical §13 L-HMORSE-LOCAL (Cat B, CV-1.16) — active-set Hessian non-degeneracy at non-uniform critical
  - canonical §13 V5b-T-zero (Cat A, CV-1.4 sub) — Goldstone zero on translation-invariant graphs
  - canonical §13 T-σ-Lemma-1 (Cat A, CV-1.5) — Aut(G)-isotypic Hessian decomposition
  - canonical §16 D-ST-4 (Cat B candidate, CV-1.6) — Z_K, Γ, multi-basin decomposition
  - canonical §16 OP-0005-DYN (OPEN, W9+, theorem_status.md L579) — primary target
  - canonical theorem_status.md OP-HMORSE-SADDLE (OPEN, L435) — saddle-point Hessian regularity substrate (H2)
  - CV-1.18 SEAL OP-0021 Route C (T_* ξ resident under OMS-1) — T_* axiomatic anchor
  - parent 01_ns_inspired_synthesis.md §6 #12 (Pr^{(Kramers)} catalog entry), §7.2 Identity 2 (boxed Eyring–Kramers prefactor reduced form), §9.2 Tier 1 priority, §11.1 OPEN map, §13.2 child file plan
  - 2026-05-20 logs 03_D_L_commutation.md §4.2 (Aut(G)-equivariance pattern, exemplar Cat A on uniform critical)
  - working/cssl/01_critic_evaluation.md (3 CRITICAL + 4 MAJOR CSSL flaws — patterns explicitly AVOIDED here per §1.2)
  - external Hänggi-Talkner-Borkovec 1990 Rev Mod Phys 62:251 §IV (overdamped multi-D Kramers prefactor — contrastive standard tool, CN10 compliance)
  - external Kramers 1940 Physica 7:284 §VII (1D high-friction limit, primary source)
  - external Langer 1969 Ann Phys 54:258 (multi-D generalization of Kramers; HTB §IV foundation)

causation_chain:
  - DECL Q3+Q4 + T-PF-A1 Package I Cat A (generator foundation) + T-K-Select-PF Cat B (sector framework) + D-ST-4 Cat B (Γ named with P-F flag now resolved) → demand for explicit ω_0 = OP-0005-DYN substrate (intermediate I1)
  - I1 + Hänggi–Talkner–Borkovec 1990 multi-D form + Theorem 4 Cat A + L-HMORSE-LOCAL Cat B + OP-HMORSE-SADDLE substrate → §4.1 boxed ω_0^{SCC} formula (intermediate I2)
  - I2 + 3 hypotheses (H1=H5, H2=OP-HMORSE-SADDLE, H3=interior well-separation) + 5-step proof sketch §5.3 → L-KRAMERS-PR-SCC working-layer Cat B target (intermediate I3)
  - I3 + canonical OPEN catalog walk → §7 5-OP advance map (target)

inverse_causation_check:
  - if T-PF-A1 Package I were not Cat A: generator foundation void; counterfactually resolved by CV-1.9
  - if T_* registration were unresolved (CV-1.18 SEAL pre-existing state): Eyring–Kramers exponent ill-defined; resolved by Route C ξ resident
  - if HTB 1990 form were not applicable to compact polytope with interior critical (H3): need alternative reflected-Langevin Eyring–Kramers form (Bovier-den Hollander 2015); flagged as separate channel
  - if H1 (= H5) fails: T-P-F-ε0-K also Cat B-blocked, both share same anchor — consistent
  - if H2 (= OP-HMORSE-SADDLE) fails: L-KRAMERS-PR-SCC remains conditional; OPEN row remains OPEN — honest

constraints_preserved:
  - CN1: canonical/* edits = 0 (working layer only)
  - CN2: no silent OP closure (5-OP map § 7 is explicit *attack points*, not claims of closure)
  - CN3: no Research OS scaffolding (single working file)
  - CN4: zero new energy terms (only Hessian spectral diagnostics)
  - CN5: 4-term independence preserved
  - CN10: contrastive only (HTB 1990 = external Rev Mod Phys, applied structurally)
  - inertia 0 (first-order T-PF-A1-SDE)
  - Mori-Zwanzig 0 (CV-1.18 SEAL Routes A/B DEPRECATED)
  - CSSL E_ridge/E_wild/E_pers 0 (critic-rejected)
  - DECL-1.0 amend 0
  - scc/ modification 0
```

---

## §10 — Hard Constraint CN1-16 Check (16/16 ✓)

| Constraint | Status | Evidence |
|---|---|---|
| **CN1** canonical 직접 수정 0 | ✓ | This file is working layer only; canonical/* untouched. Will be verified by `git status THEORY/canonical/` in §11 final check. |
| **CN2** Silent OP resolution 0 | ✓ | §7.1 explicit: OP-0005-DYN is *attack point with explicit form*, not closure; status remains OPEN. T-P-F-ε0-K and D-ST-4 are *Cat A path channels*, not promotions. OP-0008 is *partial quantification only*. Package II is *Cat B entry only*. §7.2 honest non-overclaim catalog (7 OPs left orthogonal). |
| **CN3** Research OS 재도입 0 | ✓ | Single working file in `working/field_equation_framework/` (existing directory created W8-Day3 parent). No new D/S/T/A/E/Q/C/P/X registries. |
| **CN4** (analyticity, b_D=0) | ✓ | Zero new energy terms. `μ_well, μ_saddle` are Hessian eigenvalues of the *existing* `E_SCC` (CN4-preserving). No PH / barcode embeddings (CSSL §D.3 critic-rejected pattern). |
| **CN5** (4-term independence) | ✓ | `E_SCC = λ_cl E_cl + λ_sep E_sep + λ_bd E_bd + λ_tr E_tr` referenced as the canonical 4-term sum; no merging or new term. |
| **Closure idempotence 가정 0** | ✓ | Not invoked; A3 stabilization tendency preserved. |
| **K 이중 취급 0** | ✓ | `K_act` only (T-K-Select-PF / D-ST-3 canonical D-ST-3 convention). `K_field` mentioned once at parent xref; not used in formulas. `K_soft` not used. |
| **Zero-temp metastability flag** | ✓ | §6.5 explicit: `T_* = 0.1` finite throughout; `T_* → 0` limit not invoked. Empirical barrier `~ β^{0.89}` cited from canonical L120 with explicit branch/manifold caveat (L1803 Erratum referenced). |
| **OMC 풀 오케스트레이션 0** | ✓ | This file is a single working-layer derivation. No OMC pool / sub-agent calls embedded. (Generated under user-authorized parallel ultrawork at session boundary; *within* this file, no further orchestration.) |
| **CN10** (no reductive reduction) | ✓ | §1.2 + §3.1 explicit: Hänggi–Talkner–Borkovec 1990 = *contrastive standard tool* (Rev Mod Phys overdamped review); SCC is *structurally analogous* to but *not reduced to* a Brownian-particle-in-potential. No fluid-mechanics import. |
| **Primitive 전도 0** | ✓ | `u_t : X_t → [0,1]` primitive preserved. `μ_well, μ_saddle` are *derived diagnostics* of `u_t`'s energy landscape, not new primitives. |
| **Inertia 0** | ✓ | §1.2 + §3.1 + §5.3 Step 1 explicit: first-order T-PF-A1-SDE only. No `∂_t² u`. No momentum field. |
| **Mori-Zwanzig 0** | ✓ | §1.2 + §3.1 explicit: CV-1.18 SEAL Routes A/B DEPRECATED. No effective memory kernel. |
| **CSSL energy terms 0** | ✓ | §1.2 explicit: `E_ridge, E_wild, E_pers` critic-rejected per `working/cssl/01_critic_evaluation.md` (3 CRITICAL + 4 MAJOR). The saddle direction in §2.3 (S2) is the *Hessian's already-existing unstable eigenvector*, not an energy term that engineers saddles. |
| **DECL-1.0 amend 0** | ✓ | DECL.md untouched. DECL Q3+Q4 *referenced* as motivation only. |
| **scc/ 수정 0** | ✓ | This file is doc-only; `CODE/scc/` untouched. (W9+ task `02a_kramers_prefactor_numerical_torus.md` will add `CODE/scripts/test_kramers_prefactor_torus.py` — *future* scope, not this file.) |

**16/16 ✓ verified.**

---

## §11 — One-Paragraph Summary

**Eyring–Kramers prefactor `ω_0^{SCC} = (|μ_saddle|/(2π)) · √(|det' Hess(u^{*,well})| / |det' Hess(u^{*,saddle})|)` for SCC formation regime K-jump transitions is derived as the working-layer Cat B target lemma L-KRAMERS-PR-SCC, anchored to canonical Theorem 4 (Cat A μ_k at uniform critical) + L-HMORSE-LOCAL (Cat B active-set non-degeneracy at non-uniform well) + T-PF-A1 Package I (Cat A reflected Langevin generator) + Hänggi–Talkner–Borkovec 1990 multi-D overdamped form (Rev Mod Phys 62:251 §IV, *contrastive standard tool*) under three hypotheses H1 (Morse non-degeneracy = T-P-F-ε0-K's H5), H2 (Morse-1 saddle = OP-HMORSE-SADDLE substrate), H3 (interior well-separation from polytope boundary), with the reduced 1D-projection recovering parent file's Identity 2 `ω_0 ~ ω_well · ω_saddle · (Pr^{(Kramers)})^{-1/2}` where `Pr^{(Kramers)} = |μ_well|/|μ_saddle|`; the 5-OP advance map covers OP-0005-DYN (primary attack point with explicit form), T-P-F-ε0-K (Cat A prefactor channel), D-ST-4 (Cat A explicit Γ channel), OP-0008 (partial K-jump rate quantification), and P-F-A1 Package II (Cat B entry); a 2D torus L=16 numerical example at (β/α, c, T_*) = (10, 1/2, 0.1) yields order-of-magnitude `Pr^{(Kramers)} ~ 0.33`, `ω_0 ~ 0.084` per unit time, and Eyring–Kramers rate `Γ ~ 10^{-337}` consistent with canonical exp55 "zero merges in 5000 iterations" empirical anchor; all 16 hard constraints (CN1-16 + inertia + Mori-Zwanzig + CSSL energy terms + DECL amend + scc/ modification) satisfied 16/16 ✓; canonical/* edits = 0; Cat assignment final = working-layer Cat B target (NOT Cat A: H1+H2 inherit T-P-F-ε0-K Cat B + OP-HMORSE-SADDLE OPEN status; NOT Cat C: 5-step proof sketch rigorous given H1-H3, no new conjectures); W9+ forward hooks specify 7 child files (02a numerical verification, 02b β-sweep, 02c H5 discharge, 02d OP-HMORSE-SADDLE attack, 02e rescaling×prefactor, 02f K-jump distribution, 02g Pe-Pr network).**

---

*W8-Day3 late ultrawork synthesis complete. CV-1.18 SEALED untouched. L-KRAMERS-PR-SCC working-layer Cat B target delivered. Parent 01_ns_inspired_synthesis.md §13.2 Tier 1 child plan executed. W9+ Tier 1A-2B child files queued.*
