---
type: working/field_equation_framework/bakry_emery_cd
date: 2026-05-20
session_origin: W8-Day3 Wave 2 (post-critic), Bakry-Émery CD(κ,∞) complementary lane
canonical_version: CV-1.18 SEALED (untouched throughout)
status: draft v0.1 (Cat A target conditional on convex region; complementary to file 04 Schur)
authors: user (Jaehong Oh) via Executor delegation
preceded_by:
  - 01_ns_inspired_synthesis.md (§3, §4 NS↔SCC mapping; §6 dimensionless catalog)
  - 04_h_morse_spectral_quantification.md (Schur complement approach; *file 11 complements, NOT replaces*)
  - 06_surface_tension_rescaling_cat_a.md (rescaling (α,β)→(sα,sβ); cross-link to §8 here)
  - 07_critic_full_review.md §F (consensus baseline σ = (√2/6)√(αβ); ε² convention; line-number anchors)
  - canonical §13 T-PF-A1-AR / T-PF-A1-SDE / T-PF-A1-GI / T-PF-A1-PE (Cat A, CV-1.9); Theorem 4 / T8-Core (Cat A)
purpose: |
  Apply Bakry-Émery CD(κ,∞) curvature-dimension condition to the SCC reflected
  Langevin generator. Derive — *in convex regions* (where Hessian is PSD) —
  (i) Poincaré inequality λ_1 ≥ κ; (ii) Wasserstein contractivity rate κ;
  (iii) relative-entropy decay rate 2κ. Position as *complementary* (not
  replacement) to file 04's Schur complement Sc^{(2)} approach and to canonical
  T-PF-A1-PE Cat A. Bakry-Émery is sharper *inside convex regions* (uniformly
  positive κ vs canonical exp(-osc/T_*)); canonical T-PF-A1-PE is sharper
  *across non-convex regimes* (unconditional vs requiring κ > 0).
canonical_compatibility:
  CN1_canonical_edits: 0
  CN4_analyticity: preserved (no new energy terms)
  CN5_4_term_independence: preserved (all four energy terms enter only via ∇E and ∇²E)
  CN10_no_reductive_reduction: preserved (Bakry-Émery is *contrastive standard tool* — Bakry-Gentil-Ledoux 2014)
  primitive_u_t: preserved (κ = derived spectral diagnostic of ∇²E(u_t))
  inertia_introduction: forbidden (Package I Cat A protection)
  Mori_Zwanzig: forbidden (OP-0021 Routes A/B DEPRECATED CV-1.18)
  CSSL_energy_pattern: forbidden (no E_pers, no E_ridge, no E_surg; pure functional analysis on canonical E)
cot_enforced: yes
coc_enforced: yes
---

> [!nav] Linked: [[../../canonical/canonical|CV-1.18 canonical]] (§13 T-PF-A1-AR/SDE/GI/PE Cat A; Theorem 4 / T8-Core Cat A) · [[../../canonical/DECLARATION|DECL-1.0]] (Q1 T8 boundary; Q3 stochastic dynamics) · [[01_ns_inspired_synthesis|01 NS-inspired synthesis]] · [[04_h_morse_spectral_quantification|04 Schur complement Sc^{(2)} (complementary)]] · [[06_surface_tension_rescaling_cat_a|06 rescaling]] · [[07_critic_full_review|07 critic review §F (consensus baseline)]]

# 11 — Bakry-Émery CD(κ,∞) Curvature-Dimension Condition for SCC

**Mode**: working-layer Cat A target lemma (NOT canonical promotion, NOT SEAL prep)
**Target**: L-BAKRY-EMERY-SCC — In a convex region R ⊂ F_M(G) where Hess(E) ⪰ κ I (κ > 0), the SCC reflected Langevin generator satisfies CD(κ,∞), implying
- (a) Poincaré λ_1(L²(π_{T_*}|_R)) ≥ κ (uniformly positive — sharper than canonical osc-form);
- (b) W_2 contractivity rate κ;
- (c) Relative-entropy decay rate 2κ.

**Cat A status (honest)**: Cat A *in convex regions only* (BGL 2014 is Cat A in literature; SCC application is direct via T-PF-A1-SDE Cat A + bounded-Hessian PSD). **NOT** Cat A across non-convex domain (where T-PF-A1-PE canonical Cat A remains the unconditional anchor).

---

## §0 — Frontmatter + xref check + §8a P1-P6 audit + CONSENSUS BASELINE

### §0.1 Pre-work xref check

- `grep -r "Bakry\|Émery\|Bakry-Emery\|carré du champ\|CD(κ\|displacement convexity" canonical/` → 0 canonical hits. *Novel positioning*: first SCC application of Bakry-Émery CD(κ,∞) framework.
- `grep -r "Bakry" working/` → 0 prior working hits (verified via `grep -i bakry`). 01_ns_inspired_synthesis §6 catalog mentions Pe / Pr / Sc etc but NOT Bakry-Émery.
- Canonical anchors invoked:
  - T-PF-A1-SDE Cat A at `canonical.md` L1668 (reflected Langevin existence + uniqueness, Lions-Sznitman convex case)
  - T-PF-A1-GI Cat A at `canonical.md` L1686 (Gibbs invariant measure π_{T_*}, self-adjoint generator)
  - T-PF-A1-PE Cat A at `canonical.md` L1700-1711 (Poincaré λ_1 ≥ (π²/n) e^{-osc(E)/T_*}; the *unconditional* canonical anchor that L-BAKRY-EMERY-SCC complements)
  - Theorem 4 / T8-Core at `canonical.md` L1134-1136 (μ_k = 4αλ_k + βW''(c) at u* = c·1; threshold β/α > 4λ_2/|W''(c)|)
  - OP-HMORSE-SADDLE at `theorem_status.md` L594 (saddle-point Hessian regularity OPEN)
  - OP-0005-DYN at `theorem_status.md` L803 (Kramers rates, Package II conditional on H5 + OP-0021)

### §0.2 §8a P1-P6 archive pattern audit

| # | Pattern | Audit |
|---|---|---|
| P1 | 근본 질문 우회 | DECL Q1 (T8 spectral gap) + Q3 (stochastic dynamics) 직접 정량 — *우회 아님* ✓ |
| P2 | Vocabulary refactoring | u_t primitive 미변경; κ = derived spectral diagnostic of canonical ∇²E ✓ |
| P3 | Canonical content 중복 | T-PF-A1-PE Cat A 의 *complementary refinement* (sharper in convex regions); 본문 *replacement 아님* ✓ |
| P4 | 외부 도구 도입 | Bakry-Émery 1985 / BGL 2014 / Otto-Villani 2000 = *contrastive standard tools*, T-PF-A1-SDE 직접 후속 ✓ |
| P5 | Self-audit | 본 §0 + §13 hard constraint check (16/16) ✓ |
| P6 | 언어-수학 분리 | 모든 lemma 명시적 수학 statement + proof sketch separation ✓ |

**0/6 부합** → 진행 합법.

### §0.3 CONSENSUS BASELINE (Wave 2 critic §F)

All numerics in §11 reference example use **one** baseline, fixed here:

| Symbol | Value | Anchor |
|---|---|---|
| Graph | 2D torus PBC, L = 16, n = 256 | Wave 2 consensus |
| λ_2(L_G) | 4 sin²(π/16) ≈ **0.152241** | torus Laplacian explicit |
| c (mean field) | **1/2** | spinodal interior |
| W''(1/2) | **-1** | from W(u) = u²(1-u)², I6 correction (factor 2 in W' included) |
| α | **1** | reference |
| β (primary, supercritical) | **10** | T8-supercritical (β/α = 10 > 0.609) |
| β_sub (sub-critical branch for Bakry-Émery) | **0.1** | T8-subcritical (β/α = 0.1 < 0.609); convex Hessian at uniform critical |
| T_* | **0.1** | reference stochastic temperature |
| R | 4 | reference sphere radius (for sphere comparison only, §11 will not use) |
| σ (Modica-Mortola) | **(√2/6) √(αβ)** ≈ 0.236 √(αβ) | Wave 2 critic §F.1 (file 03 correct convention) |
| T8 threshold | β/α > 4λ_2/|W''(c)| ≈ **0.609** | Theorem 4 + SB7 |

Single-baseline commitment: §11 uses β = 10 for *supercritical* discussion (T-PF-A1-PE comparison) and β = 0.1 for *sub-critical convex* Bakry-Émery example; both with α = 1, T_* = 0.1.

---

## §1 — Mission: Bakry-Émery CD(κ,∞) Complementary to File 04 Schur Complement

### §1.1 The functional-analysis ↔ linear-algebra duality

File 04 derived L-SC2-SEPARATION (Cat B target): Sc^{(2)} = μ_bulk / μ_active explicit lower bound via Schur complement on 3-block bulk/active/exterior Hessian. This is the **linear-algebra side** of H-Morse spectral quantification.

File 11 (this document) derives L-BAKRY-EMERY-SCC (Cat A target *in convex regions*): the SCC reflected Langevin generator satisfies CD(κ,∞), implying Poincaré λ_1 ≥ κ + Wasserstein contractivity + entropy decay. This is the **functional-analysis side**.

| Aspect | File 04 (Schur) | File 11 (Bakry-Émery) |
|---|---|---|
| Tool | Schur complement on 3-block Hessian | Carré-du-champ Γ_2 ≥ κ Γ |
| Domain | Bulk + active + exterior decomposition | Convex region R ⊂ F_M(G) |
| Output | Sc^{(2)} = μ_bulk/μ_active ratio | (Poincaré λ_1 ≥ κ, W_2-contractivity κ, entropy 2κ) |
| Cat target | Cat B (conditional on bulk-PSD + saturation) | Cat A in convex R (direct from BGL 2014 + T-PF-A1-SDE Cat A) |
| Regime | H-Morse formation regime (post-T8) | Sub-critical or basin-interior |
| Complementary | Quantifies *which* mode dominates | Quantifies *how fast* dynamics mix |

```
CoT step 1: T-PF-A1-PE Cat A (canonical.md L1700-1711) gives the unconditional spectral
  gap bound λ_1 ≥ (π²/n) e^{-osc(E)/T_*}. This is *exponentially small* in the metastable
  regime (osc(E) ≫ T_*) — correct but uninformative for in-basin dynamics.
CoT step 2: Inside a single basin (convex region) — e.g., a quadratic neighborhood of an
  H-Morse-Local minimum — the local Hessian Hess(E) ⪰ κ I with κ > 0. Bakry-Émery
  CD(κ,∞) on this region gives λ_1(local L^2) ≥ κ — *uniformly positive*, no exp(-osc/T_*)
  smallness.
CoT step 3: This complements (not replaces) T-PF-A1-PE: canonical T-PF-A1-PE bounds the
  *global* mixing rate across all basins (slow, exp(-osc/T_*)); Bakry-Émery bounds the
  *local* mixing rate within one basin (fast, κ). Both are needed for a complete picture.
CoT step 4: Bakry-Émery additionally provides W_2-contractivity (Otto-Villani 2000) and
  entropy decay rate (Bakry-Émery 1985) — quantities T-PF-A1-PE does NOT directly bound.
→ Therefore: L-BAKRY-EMERY-SCC = sharper *in-convex-region* refinement, with
  three additional dynamical consequences (Poincaré + W_2 + entropy).

CoC anchors:
  - canonical T-PF-A1-PE Cat A (L1700-1711)
  - canonical T-PF-A1-SDE Cat A (L1668-1683)
  - canonical Theorem 4 Cat A (L1134-1136)
  - external: Bakry-Émery 1985 ("Diffusions hypercontractives", Sém. Probab. XIX)
  - external: Bakry-Gentil-Ledoux 2014 ("Analysis and Geometry of Markov Diffusion Operators", Grundlehren 348)
  - external: Otto-Villani 2000 ("Generalization of an inequality by Talagrand and links with the logarithmic Sobolev inequality", J. Funct. Anal. 173)
```

### §1.2 Why this is NOT a replacement for file 04

```
CoT step 1: file 04 Sc^{(2)} addresses the *deterministic H-Morse spectrum structure*
  (which modes are bulk vs active). Bakry-Émery does NOT speak to this decomposition.
CoT step 2: file 11 CD(κ,∞) addresses the *dynamical consequences* of spectral
  positivity. File 04 does NOT speak to dynamics (purely spectral).
CoT step 3: Together: file 04 tells *what the spectrum looks like*; file 11 tells *what
  the dynamics do given that spectrum*. Both are *necessary*; neither is sufficient.
→ Honest positioning: file 11 = complementary functional analysis, NOT replacement for
  file 04 linear algebra.
```

---

## §2 — Bakry-Émery CD Setup (BGL 2014 Contrastive Standard)

### §2.1 Markov generator on a manifold with boundary

Let π be a probability measure on a connected domain D (with boundary ∂D in our case the polytope F_M(G)). The Langevin diffusion has generator

$$L f \;=\; \Delta f \,-\, \nabla V \cdot \nabla f, \qquad V := -\log\rho \quad (\rho = d\pi/d\mathrm{vol})$$

In SCC's case (T-PF-A1-SDE Cat A, canonical.md L1668-1683), the reflected Langevin SDE on the affine-reduced polytope C̃ has generator

$$\boxed{\;L_{\mathrm{SCC}} \;=\; T_* \,\Pi_{T\Sigma_m}\, \Delta_{\mathbf{1}^\perp} \;-\; \Pi_{T\Sigma_m}\, \nabla \tilde{\mathcal{E}} \,\cdot\, \Pi_{T\Sigma_m}\, \nabla\;}$$

with reflecting Neumann boundary on ∂C̃ (Skorokhod K_t term in the SDE). The Gibbs measure π_{T_*} ∝ exp(−Ẽ/T_*) dσ_M is the unique invariant measure (T-PF-A1-GI Cat A, canonical.md L1686-1698).

### §2.2 Carré du champ Γ and iterated Γ_2

**Definition (carré du champ).** For smooth test functions f, g on D:

$$\Gamma(f, g) \;:=\; \tfrac{1}{2}\bigl[L(fg) \,-\, f L g \,-\, g L f\bigr]$$

For the standard diffusion form (L = T_* Δ − ∇V · ∇), direct computation gives

$$\Gamma(f, g) \;=\; T_* \,\nabla f \cdot \nabla g, \qquad \Gamma(f) := \Gamma(f, f) = T_* |\nabla f|^2.$$

**Definition (iterated carré du champ Γ_2).**

$$\Gamma_2(f) \;:=\; \tfrac{1}{2}\bigl[L \Gamma(f) \,-\, 2 \Gamma(f, L f)\bigr]$$

For the standard form, the Bochner-Lichnerowicz identity (BGL 2014 §1.16) yields

$$\Gamma_2(f) \;=\; T_*^2 \,\lVert \mathrm{Hess}\,f \rVert_{HS}^2 \;+\; T_* \,\langle \nabla f,\, \mathrm{Hess}(V) \,\nabla f \rangle$$

where ‖·‖_HS is the Hilbert-Schmidt norm.

### §2.3 CD(κ,∞) condition

**Definition (Bakry-Émery 1985 CD(κ,∞)).** The generator L satisfies the CD(κ,∞) condition with constant κ ∈ ℝ if

$$\boxed{\;\Gamma_2(f) \;\geq\; \kappa \,\Gamma(f) \qquad \forall \text{ smooth } f\;}$$

For the Euclidean (or polytope-restricted Euclidean) setting:

$$\kappa \;=\; \inf_{x \in D} \,\lambda_{\min}\bigl(\mathrm{Hess}(V)(x)\bigr) \;=\; \inf_{x \in D} \,T_*^{-1} \lambda_{\min}\bigl(\mathrm{Hess}(\tilde{\mathcal{E}})(x)\bigr)$$

(after factoring the diffusion coefficient T_*; in the SCC setting, V = Ẽ / T_* so Hess(V) = Hess(Ẽ)/T_*; **but** the relevant κ as a *rate* in the Γ_2 ≥ κ Γ form refers to the energy Hessian directly: $\Gamma_2 \geq T_* \langle \nabla f, \mathrm{Hess}(\tilde{\mathcal{E}})\, \nabla f\rangle$, so the inequality becomes $T_* \langle \nabla f, \mathrm{Hess}(\tilde{\mathcal{E}}) \,\nabla f\rangle \geq \kappa \cdot T_* |\nabla f|^2$, i.e., $\kappa = \lambda_{\min}(\mathrm{Hess}\,\tilde{\mathcal{E}})$, *without* a T_* factor when κ refers to the energy Hessian.)

**Convention adopted henceforth** (BGL 2014 §4.7): κ = λ_min(Hess Ẽ) on a region R where this is ≥ 0; in convex region with κ > 0, all downstream consequences hold with κ in this energy-Hessian units.

```
CoT step 1: BGL 2014's Theorem 4.7.2 (Bakry-Émery 1985 original): if L satisfies CD(κ,∞)
  with κ > 0, then the Poincaré inequality holds with constant κ:
  Var_π(f) ≤ (1/κ) ∫ Γ(f) dπ ≡ (T_*/κ) ∫ |∇f|² dπ.
CoT step 2: For Euclidean Langevin diffusion in a convex region D where Hess(Ẽ)|_D ⪰ κ I,
  CD(κ,∞) is *immediate* via Bochner-Lichnerowicz — no further work needed.
CoT step 3: The boundary projector Π_{TΣ_m} restricts gradients to the affine subspace,
  but does NOT change the Hessian eigenvalue structure on T_{u^*}Σ_m. So κ on the
  manifold equals κ on the projected Hessian.
→ Therefore: SCC reflected Langevin in convex region R inherits CD(κ,∞) directly from
  T-PF-A1-SDE Cat A + the linear-algebraic fact that the projected Hessian is PSD.

CoC anchors:
  - BGL 2014 §1.16 (Bochner-Lichnerowicz)
  - BGL 2014 §4.7 (Bakry-Émery CD condition + Poincaré)
  - canonical T-PF-A1-AR Cat A (canonical.md L1652) — the affine reduction structure
  - canonical T-PF-A1-SDE Cat A (canonical.md L1668)
inverse_causation_check:
  - if κ ≤ 0: BGL 2014 §4.7.2 hypothesis fails → no Poincaré from this route
    (canonical T-PF-A1-PE Cat A is the unconditional fallback)
  - if the projector Π broke the diffusion form: Bakry-Émery would not apply
    (but canonical T-PF-A1-AR Cat A guarantees Π is an *affine isometry* — preserves
    the Euclidean diffusion form post-reduction)
```

---

## §3 — SCC Generator + CD Computation

### §3.1 Projected Langevin generator (T-PF-A1-SDE Cat A)

From canonical T-PF-A1-SDE (Cat A, canonical.md L1668-1683), the SCC reflected Langevin SDE on the affine-reduced polytope $\tilde{C} \subset \mathbf{1}^\perp \subset \mathbb{R}^{n-1}$ is

$$dX_t \;=\; -\nabla \tilde{\mathcal{E}}(X_t)\, dt \;+\; \sqrt{2 T_*}\, dB_t \;+\; dK_t,$$

with K_t Skorokhod-reflecting on ∂C̃. The corresponding (unprojected) generator on $X = u - u^*$ coordinates in the tangent space $\mathbf{1}^\perp$ is

$$L_{\mathrm{SCC}} f \;=\; T_* \Delta_{\mathbf{1}^\perp} f \;-\; \nabla \tilde{\mathcal{E}} \cdot \nabla f \quad \text{(interior of $\tilde{C}$, Neumann BC on $\partial \tilde{C}$)}$$

By T-PF-A1-AR Cat A (canonical.md L1652-1666), the affine isometry from $\Sigma_m$ to $\tilde{C}$ preserves the Euclidean structure, so all carré-du-champ computations transfer cleanly.

### §3.2 Carré du champ on T_{u^*}Σ_m

Applying §2.2:

$$\Gamma_{\mathrm{SCC}}(f) \;=\; T_* |\nabla_{\mathbf{1}^\perp} f|^2 \;=\; T_* |\Pi_{T\Sigma_m} \nabla f|^2$$

(the projector enters because gradients live in T_{u^*}Σ_m = $\mathbf{1}^\perp$).

### §3.3 Iterated Γ_2 with the SCC Hessian

By Bochner-Lichnerowicz applied to L_SCC:

$$\boxed{\;\Gamma_{2,\mathrm{SCC}}(f) \;=\; T_*^2 \lVert \mathrm{Hess}_{\mathbf{1}^\perp} f \rVert_{HS}^2 \;+\; T_* \langle \nabla_{\mathbf{1}^\perp} f,\; \mathrm{Hess}_{\mathbf{1}^\perp}(\tilde{\mathcal{E}})\, \nabla_{\mathbf{1}^\perp} f \rangle\;}$$

where Hess_{$\mathbf{1}^\perp$}(Ẽ) = $\Pi_{T\Sigma_m} \mathrm{Hess}(\mathcal{E}) \Pi_{T\Sigma_m}$ is the constrained Hessian on the tangent space (canonical Theorem 4 spectrum: $\mu_k$ on $\mathbf{1}^\perp$).

### §3.4 CD constant for SCC

Drop the (non-negative) first term and apply Cauchy-Schwarz to the second:

$$\Gamma_{2,\mathrm{SCC}}(f) \;\geq\; T_* \cdot \lambda_{\min}\bigl(\mathrm{Hess}_{\mathbf{1}^\perp}(\tilde{\mathcal{E}})|_R\bigr) \cdot |\nabla_{\mathbf{1}^\perp} f|^2$$

Hence on a convex region R ⊂ $\tilde{C}$ where the constrained Hessian satisfies $\mathrm{Hess}_{\mathbf{1}^\perp}(\tilde{\mathcal{E}})|_R \succeq \kappa_R \, I$:

$$\boxed{\;\kappa_{\mathrm{SCC}}(R) \;:=\; \inf_{x \in R}\, \mu_{\min}^{\mathrm{(non\text{-}Gold)}}\bigl(\mathrm{Hess}_{\mathbf{1}^\perp}(\tilde{\mathcal{E}})(x)\bigr)\;}$$

with the "non-Goldstone" qualifier excluding the single null direction $\mathbf{1}$ (Goldstone is already removed by passing to $\mathbf{1}^\perp$ via Π).

**At a critical point u* ∈ R** (uniform or H-Morse-Local): κ_SCC = μ_min^{(non-Gold)}(u*) = smallest non-Goldstone eigenvalue of the canonical Hessian.

```
CoT step 1: BGL 2014 §1.16: for L = T_* Δ - ∇V · ∇, Γ_2 = T_*² ‖Hess f‖² + T_* ⟨∇f, Hess V · ∇f⟩.
CoT step 2: Drop first term (PSD); apply Cauchy-Schwarz: ⟨∇f, Hess V ∇f⟩ ≥ λ_min(Hess V) · |∇f|².
CoT step 3: In SCC, V = Ẽ/T_* (Gibbs density), so Hess(V) = Hess(Ẽ)/T_*. But the Γ_2 ≥ κ Γ
  inequality with Γ = T_*|∇f|² gives: T_*·⟨∇f, Hess(Ẽ)/T_* · ∇f⟩ · T_* = ⟨∇f, Hess(Ẽ)·∇f⟩ ≥ κ · T_*|∇f|².
  So κ = λ_min(Hess(Ẽ))/T_* would be the strictest reading; **BGL convention** (§4.7)
  works with the *potential* Hessian directly, giving κ = λ_min(Hess V).
CoT step 4: Either convention is consistent — the downstream Poincaré bound depends on the
  *product* κ·T_* in the final λ_1 ≥ ... bound. **Convention adopted**: κ = λ_min(Hess Ẽ)
  (energy units), so Poincaré gives λ_1 ≥ κ (in inverse time units; matches the canonical
  T-PF-A1-PE units where ‖P_t f − π(f)‖ ≤ e^{-λ_1 t} · ‖f‖).
→ Therefore: κ_SCC = μ_min^{(non-Gold)} of the canonical Hessian on $\mathbf{1}^\perp$.

CoC anchors:
  - BGL 2014 §1.16 (Bochner-Lichnerowicz)
  - BGL 2014 §4.7.2 (Bakry-Émery CD condition Poincaré)
  - canonical Theorem 4 (μ_k = 4αλ_k + βW''(c) at u*=c·1, Cat A, L1134-1136)
inverse_causation_check:
  - if u* is not in a convex region (Hess has negative eigenvalue): κ < 0, BGL hypothesis
    fails. Canonical T-PF-A1-PE Cat A remains valid as fallback.
  - if Goldstone modes not excluded: μ_min = 0 → κ = 0, no Poincaré bound. But Π_{TΣ_m}
    excludes the volume-Goldstone $\mathbf{1}$, so non-Goldstone κ is the relevant one.
```

---

## §4 — Consequences of CD(κ,∞): Poincaré + Contractivity + Entropy Decay

Given CD(κ,∞) with κ > 0 in a convex region R, three downstream consequences follow as standard BGL 2014 / Otto-Villani 2000 corollaries.

### §4.1 Poincaré inequality (Bakry-Émery 1985)

**Consequence 1 (Poincaré).** For any smooth f compactly supported in R with $\int_R f \,d\pi_{T_*}|_R = 0$:

$$\mathrm{Var}_{\pi_{T_*}|_R}(f) \;\leq\; \frac{1}{\kappa_{\mathrm{SCC}}(R)} \int_R \Gamma_{\mathrm{SCC}}(f) \,d\pi_{T_*}|_R \;=\; \frac{T_*}{\kappa_{\mathrm{SCC}}(R)} \int_R |\nabla_{\mathbf{1}^\perp} f|^2 \,d\pi_{T_*}|_R$$

Equivalently, the spectral gap of L_SCC on $L^2(\pi_{T_*}|_R)$ satisfies

$$\boxed{\;\lambda_1\bigl(L^2(\pi_{T_*}|_R)\bigr) \;\geq\; \kappa_{\mathrm{SCC}}(R)\;}$$

**Comparison with canonical T-PF-A1-PE.** Canonical gives $\lambda_1 \geq (\pi^2/n) e^{-\mathrm{osc}(\tilde{\mathcal{E}})/T_*}$ (Cat A, canonical.md L1700). In the metastable regime where osc(Ẽ) ≫ T_*, this is exponentially small. Inside a convex basin where κ_SCC > 0 is O(1) (not exponentially small), the Bakry-Émery bound is **vastly sharper**.

### §4.2 W_2 Wasserstein contractivity (Otto-Villani 2000)

**Consequence 2 (W_2-contractivity).** Let $\mu_t = \mathrm{Law}(X_t | X_0 \sim \mu_0)$ and $\nu_t = \mathrm{Law}(X_t | X_0 \sim \nu_0)$ for two initial laws supported in R. Then:

$$\boxed{\;W_2(\mu_t, \nu_t) \;\leq\; e^{-\kappa_{\mathrm{SCC}}(R) \, t} \, W_2(\mu_0, \nu_0)\;}$$

where W_2 is the quadratic Wasserstein distance.

This is the *displacement convexity* form (Otto-Villani 2000 §1; McCann 1997). In particular, taking ν_0 = π_{T_*}|_R:

$$W_2(\mu_t, \pi_{T_*}|_R) \;\leq\; e^{-\kappa_{\mathrm{SCC}}(R) \, t} \, W_2(\mu_0, \pi_{T_*}|_R)$$

— **the diffusion contracts toward equilibrium at rate κ in W_2-metric**.

### §4.3 Relative-entropy decay (Bakry-Émery 1985)

**Consequence 3 (entropy decay).** Define relative entropy $H(\mu | \pi) := \int \log(d\mu/d\pi)\, d\mu$. Under CD(κ,∞) with κ > 0 (and the additional regularity for the log-Sobolev inequality — BGL 2014 §5.7 give this for free in convex bounded domains):

$$\boxed{\;H(\mu_t | \pi_{T_*}|_R) \;\leq\; e^{-2 \kappa_{\mathrm{SCC}}(R) \, t} \, H(\mu_0 | \pi_{T_*}|_R)\;}$$

The factor 2 vs the W_2-contractivity rate κ is the standard BGL 2014 result (Theorem 5.7.3: log-Sobolev inequality with constant κ implies entropy decay at rate 2κ).

```
CoT step 1: BGL 2014 §4.7.2 — CD(κ,∞) ⇒ Poincaré λ_1 ≥ κ.
CoT step 2: BGL 2014 §5.7.3 + Otto-Villani 2000 §1.1 — CD(κ,∞) + bounded convex domain
  ⇒ log-Sobolev with constant κ ⇒ entropy decay rate 2κ.
CoT step 3: Otto-Villani 2000 Theorem 1.1 — log-Sobolev + W_2 dual ⇒ W_2-contractivity
  rate κ (Talagrand inequality).
→ Therefore: all three consequences follow directly from CD(κ,∞), without additional SCC
  inputs beyond T-PF-A1-SDE Cat A + the spectral PSD assumption on R.

CoC anchors:
  - BGL 2014 §4.7.2 (Bakry-Émery Poincaré)
  - BGL 2014 §5.7.3 (Bakry-Émery LSI ⇒ entropy decay)
  - Otto-Villani 2000 Theorem 1.1 (LSI ⇒ Talagrand ⇒ W_2-contractivity)
  - external: McCann 1997 ("A convexity principle for interacting gases", Adv. Math. 128)
inverse_causation_check:
  - if log-Sobolev fails (e.g., unbounded domain with sub-Gaussian tails): entropy decay
    weakens to a slower rate. But SCC F_M(G) is bounded convex polytope → LSI holds.
  - if W_2-contractivity claimed without CD(κ,∞): would require alternative proof
    (Sturm-Lott-Villani Ricci-curvature, not applicable here).
```

---

## §5 — Comparison with Canonical T-PF-A1-PE (Cat A)

### §5.1 The two bounds side-by-side

| Bound | Source | Regime | Strength |
|---|---|---|---|
| $\lambda_1 \geq (\pi^2/n)\, e^{-\mathrm{osc}(\tilde{\mathcal{E}})/T_*}$ | Canonical T-PF-A1-PE Cat A (L1700-1711) | **Unconditional** (any T_* > 0, any α, β) | *Exponentially small* in metastable regime |
| $\lambda_1 \geq \kappa_{\mathrm{SCC}}(R)$ | L-BAKRY-EMERY-SCC (this file, Cat A target) | **Conditional** on convex region R with Hess(Ẽ)\|_R ⪰ κI | *Uniformly positive* with O(1) constant when κ > 0 |

### §5.2 Why they are complementary, not competing

```
CoT step 1: Canonical T-PF-A1-PE handles the *global* mixing time across non-convex
  domains (multiple basins, T8-supercritical metastable regime). In such regimes,
  Hess(Ẽ) has negative eigenvalues somewhere, so Bakry-Émery CD(κ,∞) with κ > 0 fails.
  Only the (exponentially small but unconditional) canonical bound applies.

CoT step 2: L-BAKRY-EMERY-SCC handles the *local* mixing time *within a single basin*
  (convex neighborhood of an H-Morse-Local minimum, or sub-T8 regime where uniform critical
  is the unique convex minimum). Here κ > 0 gives a vastly sharper bound.

CoT step 3: Use them together: total dynamics decomposes as (i) fast in-basin equilibration
  at rate ≈ κ (Bakry-Émery); (ii) slow inter-basin transition at rate exp(-osc/T_*)
  (canonical). This is the dynamical analog of file 04's Sc^{(2)} bulk-active separation:
  file 04 separates *modes spectrally*, file 11 separates *timescales dynamically*.

CoT step 4: Honest non-overclaim: L-BAKRY-EMERY-SCC does NOT *replace* T-PF-A1-PE; it
  *refines it inside convex regions*. Outside convex regions, the canonical bound is the
  only available result.
→ Therefore: file 11 strengthens canonical understanding *additively*, with no canonical
  edit and no replacement claim.

CoC anchors:
  - canonical T-PF-A1-PE Cat A non-overclaim block (canonical.md L1709):
    "C_P ∼ (n/π²) e^{βn/16T_*} — exponentially large in n (metastable scaling; correct
    and expected for double-well)."
    — this *acknowledges* the exp-large constant in the canonical bound; L-BAKRY-EMERY-SCC
    is precisely the in-basin refinement that fills this gap.
  - BGL 2014 §4.7.5 (Persson criterion: Bakry-Émery is sharp at quadratic neighborhoods
    of critical points)
inverse_causation_check:
  - if T-PF-A1-PE replaced by Bakry-Émery: would lose unconditional applicability →
    metastable regime claims would have *no* spectral bound. Status: file 11 explicitly
    declines this replacement.
  - if Bakry-Émery applied outside convex region: κ < 0, bound becomes vacuous (or
    inverted sign). Status: file 11 restricts to convex R.
```

---

## §6 — L-BAKRY-EMERY-SCC Cat A Lemma (Convex Region) + Proof Sketch

### §6.1 Statement

**Lemma L-BAKRY-EMERY-SCC (Cat A target, in convex regions).**

*Conditions.*
- **(H1)** T-PF-A1-SDE Cat A (canonical.md L1668) — reflected Langevin SDE well-posed on F_M(G) with T_* > 0.
- **(H2)** R ⊂ F_M(G) is a convex region (open or closed convex subset of the polytope) such that the *constrained Hessian* satisfies
  $$\mathrm{Hess}_{\mathbf{1}^\perp}(\tilde{\mathcal{E}})(x) \;\succeq\; \kappa \, I \qquad \forall x \in R, \;\;\kappa > 0.$$
- **(H3)** The projector $\Pi_{T\Sigma_m}$ from T-PF-A1-AR Cat A (canonical.md L1652) preserves the affine-isometric structure (this is automatic from T-PF-A1-AR Cat A; H3 is a *certification* of the inherited structure, not an extra hypothesis).

*Statement.* Under (H1)(H2)(H3), the SCC reflected Langevin generator L_SCC on R satisfies the CD(κ,∞) condition. Consequently:

**(a) Poincaré on R.** $\lambda_1(L^2(\pi_{T_*}|_R)) \;\geq\; \kappa.$

**(b) W_2-contractivity on R.** For any two initial laws μ_0, ν_0 supported in R:
$$W_2(\mu_t, \nu_t) \;\leq\; e^{-\kappa t} \, W_2(\mu_0, \nu_0).$$

**(c) Entropy decay on R.** Under additional LSI regularity (automatic for bounded convex domains, BGL 2014 §5.7.3):
$$H(\mu_t \mid \pi_{T_*}|_R) \;\leq\; e^{-2\kappa t} \, H(\mu_0 \mid \pi_{T_*}|_R).$$

### §6.2 Proof sketch (4 steps)

```
Step 1 (Generator structure). T-PF-A1-SDE Cat A (canonical.md L1668-1683) gives the
  reflected Langevin SDE on the affine-reduced polytope C̃ = isometric image of Σ_m.
  Generator L_SCC = T_* Δ_{\mathbf{1}^\perp} - ∇_{\mathbf{1}^\perp} Ẽ · ∇_{\mathbf{1}^\perp}
  on the interior, Neumann on ∂C̃. T-PF-A1-AR Cat A (L1652) ensures the projector is an
  affine isometry → Euclidean carré-du-champ structure preserved.

Step 2 (Bochner-Lichnerowicz). Applying BGL 2014 §1.16 to L_SCC:
  Γ(f) = T_* |∇_{\mathbf{1}^\perp} f|²
  Γ_2(f) = T_*² ‖Hess_{\mathbf{1}^\perp} f‖_HS² + T_* ⟨∇_{\mathbf{1}^\perp} f, Hess_{\mathbf{1}^\perp}(Ẽ) ∇_{\mathbf{1}^\perp} f⟩
  No additional terms (no Ricci curvature contributions in Euclidean setting).

Step 3 (Apply hypothesis H2). On R, Hess_{\mathbf{1}^\perp}(Ẽ) ⪰ κ I gives
  ⟨∇f, Hess(Ẽ) ∇f⟩ ≥ κ |∇f|².
  Dropping the (non-negative) ‖Hess f‖_HS² term:
  Γ_2(f) ≥ T_* · κ · |∇_{\mathbf{1}^\perp} f|² = κ · Γ(f).
  This is exactly the CD(κ,∞) condition (BGL 2014 §4.7 Def. 4.7.1).

Step 4 (Invoke BGL 2014 standard corollaries).
  (a) BGL 2014 Theorem 4.7.2: CD(κ,∞) with κ > 0 ⇒ Poincaré λ_1 ≥ κ on L²(π|_R).
  (b) Otto-Villani 2000 Theorem 1.1: CD(κ,∞) + bounded convex ⇒ W_2-contractivity rate κ.
  (c) BGL 2014 Theorem 5.7.3: CD(κ,∞) + bounded convex ⇒ LSI with constant κ ⇒ entropy
      decay rate 2κ.

  All three are direct citations to standard literature — no SCC-specific work beyond
  Step 3's hypothesis application.

CoC anchors (proof):
  - Step 1: canonical T-PF-A1-SDE Cat A (L1668-1683); T-PF-A1-AR Cat A (L1652)
  - Step 2: BGL 2014 §1.16 (Bochner-Lichnerowicz)
  - Step 3: H2 + linear algebra (Cauchy-Schwarz)
  - Step 4(a): BGL 2014 Theorem 4.7.2
  - Step 4(b): Otto-Villani 2000 Theorem 1.1
  - Step 4(c): BGL 2014 Theorem 5.7.3
```

### §6.3 Inverse causation check

```
- If μ_min^{(non-Gold)} → 0 (Σ_T8 wall approach or non-Gold spectral degeneracy via
  Theorem 4 phase transition): κ → 0, contractivity rate → 0, in-basin mixing time → ∞.
  This is *exactly* the expected behavior near the T8 phase transition wall — formations
  emerge precisely when in-basin dynamics slow toward zero rate. Consistency check ✓.

- If R = ∅ (no convex region exists in F_M(G)): L-BAKRY-EMERY-SCC vacuous. Then only
  canonical T-PF-A1-PE applies. This is the deep-metastable regime where the canonical
  bound's exp(-osc/T_*) suppression is the *correct* physical answer.

- If the projector Π broke the diffusion form: Bochner-Lichnerowicz would fail.
  But T-PF-A1-AR Cat A guarantees affine isometry → form preserved.

- If T_* → 0: Γ(f) = T_*|∇f|² → 0, Γ_2(f) = T_*² ‖Hess f‖² + T_* ⟨∇f, Hess Ẽ · ∇f⟩ → 0
  at same rate T_*. CD(κ,∞) inequality stays valid (both sides scale uniformly with T_*),
  but the *spectral gap rate* λ_1 ≥ κ measures inverse time, independent of T_*. This is
  the deterministic limit: as T_* → 0, the diffusion becomes pure gradient flow, and
  λ_1 = κ corresponds to the linear contractivity rate of gradient flow near a quadratic
  minimum. Consistency ✓.
```

### §6.4 Cat assignment honesty

**Cat A *in convex regions only***. The three downstream consequences (a)(b)(c) all follow from CD(κ,∞) by *direct citation* to BGL 2014 / Otto-Villani 2000 standard theorems — these are *Cat A in the literature*. The SCC application is *direct* via:

1. T-PF-A1-SDE Cat A → generator is well-defined Langevin form
2. T-PF-A1-AR Cat A → projector preserves Euclidean diffusion structure
3. T-PF-A1-GI Cat A → Gibbs measure π_{T_*} is the unique invariant measure
4. Linear algebra (Hess ⪰ κI on R) → CD(κ,∞) immediate via Bochner-Lichnerowicz

No new mathematics required beyond Cat A canonical inputs + standard literature citations.

**Outside convex regions: NOT Cat A**. The canonical T-PF-A1-PE Cat A remains the unconditional anchor. L-BAKRY-EMERY-SCC explicitly refuses the replacement claim (§5.2).

---

## §7 — Application to H-Morse Spectral Gap

### §7.1 Connection to file 04's μ_min^{(non-Gold)}

File 04 §3.3 (L-SC2-SEPARATION Cat B target) identified the **active-set spectral gap** $\mu_{\mathrm{active}} = \mu_{\min}^{\neq 0}(H_{\mathrm{eff}}^{AA})$. At an H-Morse-Local critical point u* with no Goldstone other than $\mathbf{1}$:

$$\kappa_{\mathrm{SCC}}(u^*) \;=\; \mu_{\min}^{(\mathrm{non\text{-}Gold})}(u^*) \;=\; \mu_{\mathrm{active}}(u^*) \quad \text{(provided active is the smallest non-Goldstone)}$$

So **L-BAKRY-EMERY-SCC turns file 04's μ_active into a dynamical rate**:
- File 04: Sc^{(2)} = μ_bulk/μ_active gives the *spectral separation* between bulk-stable and active-marginal modes.
- File 11: κ_SCC = μ_active gives the *dynamical contractivity rate* on a convex neighborhood of u*.

These are **two faces of the same H-Morse spectral structure**:

| File 04 reading | File 11 reading |
|---|---|
| μ_active = how marginal is the slowest non-Goldstone mode? | κ_SCC = at what rate does in-basin diffusion contract? |
| Linear-algebra ratio | Functional-analysis rate |
| H-Morse-Local positivity (deterministic spectrum) | Bakry-Émery in-basin dynamics (stochastic) |

### §7.2 Basin-of-attraction implication

```
CoT step 1: file 04 L-HMORSE-LOCAL Cat B (canonical L1948) gives μ_min ≥ c_HML > 0 at u*.
CoT step 2: By continuity of Hess(Ẽ) (CN4 analyticity preserved), there is an open
  neighborhood R_* ∋ u* on which Hess_{\mathbf{1}^\perp}(Ẽ) ⪰ (c_HML/2) I.
CoT step 3: R_* is the basin of attraction (more precisely: the convex neighborhood
  on which Hessian PSD persists) where L-BAKRY-EMERY-SCC applies with κ = c_HML/2.
CoT step 4: Consequence: starting from any initial law μ_0 supported in R_*, the
  diffusion contracts to π_{T_*}|_{R_*} at rate ≥ c_HML/2 in W_2, with entropy decay
  rate ≥ c_HML.
→ Therefore: *every* H-Morse-Local formation u* (file 04 Cat B) inherits a Bakry-Émery
  in-basin dynamical rate (file 11 Cat A target on R_*), modulo identifying R_*'s explicit
  geometry (which depends on graph structure but is *non-vacuous* by L-HMORSE-LOCAL).

CoC anchors:
  - canonical L-HMORSE-LOCAL Cat B (canonical.md L1948)
  - file 04 §3 L-SC2-SEPARATION Cat B target
  - canonical CN4 analyticity (preserved → Hess continuous)
  - canonical T-PF-A1-AR Cat A (L1652) — convexity of $\tilde C$ inherited; convexity
    of R_* requires explicit verification per H-Morse-Local instance
inverse_causation_check:
  - if L-HMORSE-LOCAL Cat B fails (c_HML = 0): no convex basin → no Bakry-Émery rate.
    This is the case at the T8 wall itself (μ_min → 0), where formation onset coincides
    with vanishing in-basin contractivity.
  - if Hess not continuous: would break the basin-of-attraction inheritance. But CN4
    analyticity → Hess is C^∞ → basin exists.
```

### §7.3 Connection to OP-HMORSE-SADDLE (theorem_status.md L594)

OP-HMORSE-SADDLE is OPEN: saddle-point Hessian regularity for full Eyring-Kramers prefactor. **L-BAKRY-EMERY-SCC does NOT close OP-HMORSE-SADDLE**, because:

- L-BAKRY-EMERY-SCC requires convex region (Hess ⪰ κI, κ > 0)
- Saddle points have Hess with ≥1 negative eigenvalue → NOT convex region → Bakry-Émery does not apply at saddles directly

However, L-BAKRY-EMERY-SCC *complements* OP-HMORSE-SADDLE: the *within-basin* dynamics are now Cat A (in convex regions). The *between-basin* dynamics — the Eyring-Kramers transition rates — remain OPEN (Package II, OP-0005-DYN at theorem_status.md L803).

---

## §8 — Surface Tension Rescaling + Bakry-Émery Scaling (file 06 cross-link)

### §8.1 Rescaling (α, β) → (sα, sβ) preserves κ → s·κ

From file 06 (L-SURFACE-TENSION-RESCALE Cat A direct, §3 Proof of (b)): under the rescaling $(\alpha, \beta) \to (s\alpha, s\beta)$, the constrained Hessian scales linearly:

$$\mathrm{Hess}_{\mathbf{1}^\perp}\bigl(\tilde{\mathcal{E}}_{s\alpha, s\beta}\bigr) \;=\; s \cdot \mathrm{Hess}_{\mathbf{1}^\perp}\bigl(\tilde{\mathcal{E}}_{\alpha, \beta}\bigr)$$

(this is because both $E_{\mathrm{bd}} = \alpha u^T L u + \beta \sum W$ scales linearly in (α,β)).

Therefore:

$$\boxed{\;\kappa_{\mathrm{SCC}}^{(s\alpha, s\beta)}(R) \;=\; s \cdot \kappa_{\mathrm{SCC}}^{(\alpha, \beta)}(R)\;}$$

### §8.2 Three timescales scale by s

By the rescaling identity above + §4 consequences:

| Quantity | Scaling under (α,β) → (sα,sβ) |
|---|---|
| κ (CD constant) | s · κ |
| Poincaré spectral gap λ_1 | ≥ s · κ |
| W_2-contractivity rate | s · κ |
| Entropy decay rate | 2s · κ |
| Mixing time (inverse rate) | 1/s · (1/κ) |

**Physical interpretation**: increasing the energy scale by factor s speeds up *all* in-basin dynamical rates by factor s, and reduces mixing time by factor 1/s. This matches the canonical Theorem 4 linearity ($\mu_k$ linear in both α and β) and file 06 surface tension rescaling ($\sigma \to s\sigma$).

### §8.3 Compatibility with σ rescaling

From the consensus baseline σ = (√2/6)·√(αβ) (Wave 2 critic §F.1):

$$\sigma^{(s\alpha, s\beta)} \;=\; (\sqrt{2}/6)\sqrt{(s\alpha)(s\beta)} \;=\; s \cdot \sigma^{(\alpha, \beta)}$$

— σ scales linearly with s, matching κ scaling. **Consistency check**: a 2-scale formula $\lambda_1 \sim \sigma \cdot \mu_2(J_\Gamma)$ from file 03 §13 boxed result also inherits $s$-linearity: $\sigma \cdot \mu_2 \to s\sigma \cdot s\mu_2 = s^2 \cdot (\sigma \mu_2)$ via the J_Γ Jacobi spectrum (which scales as Hessian, i.e., linearly in (α,β)). So *spatial-quadratic* spectral bounds scale as $s^2$, but the *direct* Bakry-Émery κ scales as $s^1$ — different scaling exponents because Bakry-Émery bounds the full Hessian eigenvalue (linear in (α,β)), while sphere-Jacobi bounds the curvature-Jacobi spectrum (quadratic in (α,β) through σ·κ_geom product).

```
CoC anchors:
  - file 06 L-SURFACE-TENSION-RESCALE Cat A direct (proof of (b): Hessian linearity)
  - canonical Theorem 4 Cat A linearity in (α,β)
  - consensus baseline σ = (√2/6)√(αβ) (file 07 critic §F.1; file 03 derivation correct)
inverse_causation_check:
  - if rescaling didn't preserve Hessian linearity: file 06 part (b) would fail (it doesn't).
  - if κ didn't scale linearly: would contradict the direct s-linearity of constrained Hessian.
```

---

## §9 — Otto-Villani Wasserstein Gradient Flow Formulation

### §9.1 Heat flow as W_2 gradient flow of relative entropy

Otto-Villani 2000 + Jordan-Kinderlehrer-Otto 1998 ("The variational formulation of the Fokker-Planck equation", SIAM J. Math. Anal. 29): the heat flow / Fokker-Planck equation can be written as the **W_2 gradient flow of relative entropy**. For the SCC reflected Langevin:

$$\partial_t \mu_t \;=\; -\mathrm{grad}_{W_2} F(\mu_t), \qquad F(\mu) := \int \tilde{\mathcal{E}} \,d\mu \;+\; T_* \int \log\mu \, d\mu \;=\; T_* \cdot H(\mu | \pi_{T_*})$$

(modulo constant). So the diffusion is the gradient descent (in W_2-metric) of the relative entropy functional.

### §9.2 Bakry-Émery CD(κ,∞) ↔ κ-displacement convexity of F

Otto-Villani 2000 Theorem 1.1 + McCann 1997: CD(κ,∞) is equivalent to **κ-geodesic convexity of F along W_2-geodesics** (where W_2-geodesics are McCann's displacement interpolations of optimal transport plans).

In SCC: on a convex region R where Hess(Ẽ) ⪰ κI, the energy functional Ẽ is κ-displacement convex on the corresponding probability measure space. The relative entropy term $T_* \int \log\mu \, d\mu$ is 0-displacement convex (always, by McCann 1997). Sum: F is κ-displacement convex.

### §9.3 Connection to canonical CV-1.15 action-based temporal framework

Canonical CV-1.15 introduces action-based temporal succession (T-ACT-KERNEL-COMP→REL Cat B, P-ACTION-PATH-INHERITANCE Interpretation). The W_2 gradient flow formulation provides a *variational anchor* for this temporal framework:

```
CoT step 1: CV-1.15 action-based framework views temporal succession as a path-cost
  optimization (Sinkhorn-stabilized).
CoT step 2: Otto-Villani 2000 W_2 gradient flow gives the *infinitesimal* (continuous-time)
  version of optimal transport: each Δt step is a W_2 gradient step of relative entropy.
CoT step 3: Bakry-Émery CD(κ,∞) provides the *rate* at which this gradient flow contracts
  toward the invariant Gibbs measure π_{T_*}.
CoT step 4: So the κ-displacement convexity of F = κ-contractivity rate of the dynamics
  = κ-quadratic-cost regularization rate of the Sinkhorn entropic regularization.
→ Therefore: L-BAKRY-EMERY-SCC provides a *spectral grounding* for the rate at which
  CV-1.15's action-based path-inheritance equilibrates.

CoC anchors:
  - canonical CV-1.15 T-ACT-KERNEL-COMP→REL Cat B conditional (canonical §13)
  - canonical CV-1.15 P-ACTION-PATH-INHERITANCE Interpretation
  - Otto-Villani 2000 §1
  - Jordan-Kinderlehrer-Otto 1998 (JKO scheme)
  - McCann 1997 (displacement convexity)
  - NOTE: this is *complementary*, not a CV-1.15 modification. CV-1.15 is sealed canonical.
inverse_causation_check:
  - if W_2 gradient flow structure breaks: no κ-displacement convexity → no CD link.
    But T-PF-A1-SDE Cat A guarantees the Langevin form → JKO 1998 applies →
    W_2 gradient flow structure exists.
```

---

## §10 — OP-0005-DYN Within-Basin vs Between-Basin Decomposition

### §10.1 Two-timescale decomposition

OP-0005-DYN (theorem_status.md L803) is OPEN: Kramers rates for K-transitions (Package II conditional on H5 + OP-0021). L-BAKRY-EMERY-SCC provides a *partial* attack by splitting the problem into two timescales:

| Timescale | Process | Rate | Cat status |
|---|---|---|---|
| Fast (within-basin) | Bakry-Émery contractivity to local equilibrium | κ_SCC(R_*) | **Cat A in convex R_*** (this file) |
| Slow (between-basin) | Kramers/Eyring-Kramers transition | ∝ exp(-ΔE/T_*) | OPEN (file 02 Cat B target; OP-HMORSE-SADDLE OPEN) |

### §10.2 What this gives and does NOT give

```
CoT step 1: Bakry-Émery gives the *in-basin equilibration rate* — once a diffusion sample
  enters basin B(u*) of an H-Morse-Local critical point u*, it equilibrates to
  π_{T_*}|_{B(u*)} at rate κ_SCC(u*) (Cat A within convex R_* ⊂ B(u*)).
CoT step 2: Bakry-Émery does NOT give the *between-basin transition rate* — the rate at
  which a sample escapes B(u*) and enters a different basin. This is the Eyring-Kramers
  rate, dominated by saddle-point barriers.
CoT step 3: file 02 (Kramers prefactor) and file 09 (LDP, if it exists; assumed
  upstream) attack the between-basin rate. Bakry-Émery (file 11) attacks the in-basin
  rate.
CoT step 4: Together they form a *complete* spectral picture: rate = (fast in-basin κ) ×
  (slow between-basin exp(-ΔE/T_*)). But the combination requires explicit interpolation
  formulas (e.g., Eyring-Kramers prefactor with full Hessian determinants — file 02's
  L-KRAMERS-PR-SCC Cat B target).
→ Therefore: L-BAKRY-EMERY-SCC = one half of the OP-0005-DYN attack; not closure.

CoC anchors:
  - canonical OP-0005-DYN (theorem_status.md L803) — OPEN
  - file 02 L-KRAMERS-PR-SCC Cat B target
  - OP-HMORSE-SADDLE (theorem_status.md L594) — OPEN
  - canonical OP-0021 — T_* registration (Routes A/B DEPRECATED CV-1.18)
inverse_causation_check:
  - if claimed L-BAKRY-EMERY-SCC closes OP-0005-DYN: this would be FALSE; saddle-crossing
    requires non-convex analysis Bakry-Émery cannot provide. Explicit non-overclaim ✓.
  - if L-BAKRY-EMERY-SCC didn't exist: in-basin dynamics would be bounded only by
    canonical T-PF-A1-PE exp(-osc/T_*) — uninformative for within-basin equilibration.
```

---

## §11 — 2D Torus L=16 Reference Example (CONSENSUS BASELINE)

### §11.1 Setup (using CONSENSUS BASELINE from §0.3)

- Graph: 2D torus PBC, L = 16, n = 256
- λ_2 = 4 sin²(π/16) ≈ 0.152241
- c = 1/2, W''(1/2) = -1
- α = 1, T_* = 0.1
- Two branches: β = 10 (T8-supercritical, primary) and β = 0.1 (T8-sub-critical, where Bakry-Émery applies at uniform critical)

### §11.2 Where Bakry-Émery applies on this graph

By Theorem 4 (Cat A, canonical.md L1134-1136), at the uniform critical $u^* = c\mathbf{1}$:

$$\mu_k(u^* = c\mathbf{1}) \;=\; 4\alpha \lambda_k(L_G) \;+\; \beta W''(c) \;=\; 4 \cdot 1 \cdot \lambda_k \,+\, \beta \cdot (-1)$$

T8 threshold: β/α > 4λ_2/|W''(c)| = 4 · 0.152241 / 1 ≈ **0.609** (matches §0.3).

| Regime | β | μ_2 at u*=c·1 | Convex at u*? | Bakry-Émery κ at u*? |
|---|---|---|---|---|
| Supercritical (primary) | 10 | 4·0.152 − 10 ≈ **−9.39** | NO | κ < 0 (no bound) |
| At T8 wall | 0.609 | 4·0.152 − 0.609 ≈ 0 | Marginal | κ = 0 (vacuous bound) |
| Sub-critical (Bakry-Émery branch) | 0.1 | 4·0.152 − 0.1 ≈ **+0.509** | YES | **κ = 0.509** |

### §11.3 Bakry-Émery in the sub-critical branch (β = 0.1)

At β = 0.1, the uniform critical $u^* = c\mathbf{1}$ is the unique stable minimum (sub-T8 regime), and Hess_{$\mathbf{1}^\perp$}(Ẽ)(u*) is PSD with smallest non-Goldstone eigenvalue

$$\kappa = \mu_2 = 4\alpha\lambda_2 + \beta W''(c) = 4 \cdot 0.152241 + 0.1 \cdot (-1) \approx \boxed{0.509}.$$

By continuity (CN4 analyticity), there is an open neighborhood R_* ∋ u* on which Hess remains ⪰ (κ/2)·I = 0.254·I. Within R_*:

- **Poincaré**: $\lambda_1(L^2(\pi_{T_*}|_{R_*})) \geq 0.254$
- **W_2-contractivity rate**: 0.254
- **Entropy decay rate**: 0.509
- **In-basin mixing time**: ≈ 1/0.254 ≈ 3.94 (natural time units)

### §11.4 Comparison with canonical T-PF-A1-PE at this baseline

Canonical T-PF-A1-PE (L1700, Cat A) bound: $\lambda_1 \geq (\pi^2/n) e^{-\mathrm{osc}(\tilde{\mathcal{E}})/T_*}$.

Crude upper bound on osc(Ẽ) at β = 0.1: $\mathrm{osc} \leq \beta \cdot n \cdot W_{\max} = 0.1 \cdot 256 \cdot (1/16) = 1.6$ (where $W_{\max} = W(1/2) = 1/16$).

$$\lambda_1^{\mathrm{canonical}} \;\geq\; \frac{\pi^2}{256} \cdot e^{-1.6/0.1} \;=\; 0.0386 \cdot e^{-16} \;\approx\; 0.0386 \cdot 1.13 \times 10^{-7} \;\approx\; 4.4 \times 10^{-9}$$

**Bakry-Émery κ ≈ 0.509 vs canonical ≈ 4.4 × 10^{-9} → ratio ≈ 1.2 × 10^8**.

```
CoT verification (executed in §pre-numerics block):
  - λ_2 = 4 sin²(π/16) = 0.152241 ✓ matches Wave 2 consensus
  - W''(1/2) = -1 ✓ matches Wave 2 consensus
  - β = 0.1 gives μ_2 = 0.509 > 0 ✓ convex region at uniform critical
  - κ = 0.509 in convex R_*; T-PF-A1-PE crude bound ~4·10^{-9} (exponentially small)
  - Bakry-Émery is *~10^8× sharper* than canonical in this sub-critical convex regime
→ L-BAKRY-EMERY-SCC numerically dominates T-PF-A1-PE *inside the convex region* by
  ~8 orders of magnitude on this reference example. Honest disclaimer: this is the
  *correct* canonical behavior — T-PF-A1-PE bound is *unconditional*, but exponentially
  conservative in metastable; Bakry-Émery fills the convex-region gap.
```

### §11.5 What changes in the supercritical (β=10) regime

At β = 10 (primary supercritical, T8-broken):
- u* = c·1 is a saddle (μ_2 < 0 there) → NOT convex region → L-BAKRY-EMERY-SCC does NOT apply at u*
- H-Morse-Local formations $u^*_K$ exist (L-HMORSE-LOCAL Cat B at canonical.md L1948); each has local convex basin R_*(u^*_K) with κ(u^*_K) > 0 inheriting from c_HML (file 04 + L-HMORSE-LOCAL bound)
- L-BAKRY-EMERY-SCC applies *inside each basin R_*(u^*_K)*, giving in-basin rate ≥ c_HML > 0
- Canonical T-PF-A1-PE remains the *global* (cross-basin) anchor with its exp(-osc/T_*) suppression

This matches §10's two-timescale decomposition.

---

## §12 — CoT/CoC Archival

### §12.1 Master CoT chain

```
CoT-M1: canonical T-PF-A1-SDE Cat A gives reflected Langevin SDE with well-defined generator.
CoT-M2: Bochner-Lichnerowicz (BGL 2014 §1.16) gives Γ_2(f) = T_*²‖Hess f‖² + T_*⟨∇f, Hess(Ẽ)∇f⟩.
CoT-M3: On convex region R with Hess(Ẽ)|_R ⪰ κI: Γ_2(f) ≥ κ·Γ(f) ⇒ CD(κ,∞) immediate.
CoT-M4: BGL 2014 Theorem 4.7.2: CD(κ,∞) ⇒ Poincaré λ_1 ≥ κ.
CoT-M5: Otto-Villani 2000 Theorem 1.1: CD(κ,∞) + convex bounded ⇒ W_2-contractivity rate κ.
CoT-M6: BGL 2014 Theorem 5.7.3: CD(κ,∞) + convex bounded ⇒ LSI constant κ ⇒ entropy decay rate 2κ.
CoT-M7: Outside convex R: κ < 0 ⇒ Bakry-Émery vacuous; canonical T-PF-A1-PE remains the
        unconditional fallback (exp(-osc/T_*) bound).
CoT-M8: H-Morse-Local critical points (L-HMORSE-LOCAL Cat B) have convex basins → inherit
        Bakry-Émery in-basin rate κ ≥ c_HML.
CoT-M9: Within-basin (Bakry-Émery, Cat A) + between-basin (Eyring-Kramers, OPEN) = full
        OP-0005-DYN dynamics; this file closes only the first half.
CoT-M10: Surface-tension rescaling (file 06) ⇒ κ → s·κ ⇒ all three rates scale linearly in s.
```

### §12.2 Master CoC chain

| Claim | Canonical anchor | Literature anchor |
|---|---|---|
| Langevin generator structure | T-PF-A1-SDE Cat A (canonical.md L1668-1683) | Lions-Sznitman 1984 |
| Affine isometry of projector | T-PF-A1-AR Cat A (canonical.md L1652-1666) | — |
| Gibbs invariance | T-PF-A1-GI Cat A (canonical.md L1686-1698) | Holley-Stroock 1987 |
| Canonical Poincaré bound | T-PF-A1-PE Cat A (canonical.md L1700-1711) | Payne-Weinberger 1960 |
| Hessian spectrum at critical | Theorem 4 Cat A (canonical.md L1134-1136) | — |
| H-Morse-Local positivity | L-HMORSE-LOCAL Cat B (canonical.md L1948) | — |
| Surface tension rescaling | file 06 Cat A direct (this working layer) | Modica-Mortola 1977 |
| σ = (√2/6)·√(αβ) consensus | file 07 §F.1 critic (Wave 2 consensus baseline) | Modica 1987 |
| Bochner-Lichnerowicz | — | BGL 2014 §1.16 |
| CD(κ,∞) ⇒ Poincaré | — | Bakry-Émery 1985; BGL 2014 §4.7.2 |
| CD(κ,∞) ⇒ W_2-contractivity | — | Otto-Villani 2000 Theorem 1.1; McCann 1997 |
| CD(κ,∞) ⇒ entropy decay | — | BGL 2014 §5.7.3 |
| JKO variational formulation | — | Jordan-Kinderlehrer-Otto 1998 |
| OP-HMORSE-SADDLE OPEN | theorem_status.md L594 | — |
| OP-0005-DYN OPEN | theorem_status.md L803 | — |

### §12.3 Bibliography (external)

- Bakry D., Émery M., 1985. "Diffusions hypercontractives." *Séminaire de Probabilités XIX*, LNM 1123, 177-206.
- Bakry D., Gentil I., Ledoux M., 2014. *Analysis and Geometry of Markov Diffusion Operators*. Grundlehren der mathematischen Wissenschaften 348, Springer.
- Jordan R., Kinderlehrer D., Otto F., 1998. "The variational formulation of the Fokker-Planck equation." *SIAM J. Math. Anal.* 29(1), 1-17.
- Lions P.-L., Sznitman A.-S., 1984. "Stochastic differential equations with reflecting boundary conditions." *Comm. Pure Appl. Math.* 37(4), 511-537.
- McCann R., 1997. "A convexity principle for interacting gases." *Adv. Math.* 128(1), 153-179.
- Otto F., Villani C., 2000. "Generalization of an inequality by Talagrand and links with the logarithmic Sobolev inequality." *J. Funct. Anal.* 173(2), 361-400.
- Payne L.E., Weinberger H.F., 1960. "An optimal Poincaré inequality for convex domains." *Arch. Rat. Mech. Anal.* 5, 286-292.

---

## §13 — Hard Constraint CN1-16 Check (16/16 ✓)

| # | Constraint | Status | Evidence |
|---|---|---|---|
| CN1 | Canonical edits = 0 | ✓ | `git status THEORY/canonical/` clean (verified pre-write) |
| CN2 | No silent OP resolution | ✓ | OP-0005-DYN, OP-HMORSE-SADDLE, OP-0021 all explicitly OPEN; §10.2 non-overclaim |
| CN3 | No retroactive Cat changes | ✓ | All cited Cat A/B/C statuses preserved as-is |
| CN4 | Analyticity (b_D = 0) preserved | ✓ | No new energy terms; Bakry-Émery operates on canonical Ẽ via ∇ and ∇² only |
| CN5 | 4-term independence preserved | ✓ | All four canonical energy terms enter symbolically; no merger |
| CN6 | u_t primitive preserved | ✓ | κ = derived spectral diagnostic of ∇²Ẽ, never replaces u_t |
| CN7 | No new primitives | ✓ | κ, Γ, Γ_2 = derived functionals of canonical objects |
| CN8 | Diagnostic-only for derived quantities | ✓ | κ used only as bound parameter, never in energy |
| CN9 | No K_field/K_act conflation | ✓ | No K-counting introduced; in-basin dynamics K-blind |
| CN10 | No reductive reduction | ✓ | Bakry-Émery + BGL 2014 = *contrastive standard tool*; SCC NOT reduced to "standard diffusion" |
| CN11 | No inertia / Mori-Zwanzig | ✓ | Pure first-order Langevin (T-PF-A1-SDE Cat A); no second-order term, no memory kernel |
| CN12 | No CSSL energy patterns | ✓ | No E_pers, E_ridge, E_surg; pure functional analysis on canonical E |
| CN13 | Per-claim CoT + CoC | ✓ | All major claims (§3.4, §4, §6, §7.2, §8, §9, §10) carry explicit CoT+CoC blocks |
| CN14 | Inverse causation per major claim | ✓ | §3 (κ→0), §6.3, §7.2, §8.3, §9.3, §10.2 all carry inverse causation |
| CN15 | Honest Cat assignment | ✓ | Cat A *only in convex regions*; outside convex R: deferred to canonical T-PF-A1-PE Cat A |
| CN16 | Single consensus baseline | ✓ | §0.3 fixes one baseline (β=10 primary, β=0.1 Bakry-Émery branch); §11 numerics use it consistently |

**16/16 ✓.**

### §13.1 Anti-pattern checks (CSSL critic learnings)

- ❌ Energy refactoring 0 (CN4)
- ❌ Persistence-as-energy 0 (CN12)
- ❌ Derived-as-primitive 0 (CN7)
- ❌ Sign-conflict 0 (κ as bound parameter; no sign-flip pattern)
- ❌ Silent OP closure 0 (CN2)
- ❌ σ-formula drift 0 (consensus baseline σ = (√2/6)·√(αβ) used, §0.3 + §8.3)
- ❌ Line-number drift 0 (all canonical line numbers verified via grep; OP lines at theorem_status.md L594, L803)
- ❌ Cross-file numerical baseline inconsistency 0 (single baseline §0.3, §11 uses both branches transparently)

---

## §14 — One-Paragraph Summary

**L-BAKRY-EMERY-SCC (Cat A target, in convex regions only)**: The SCC reflected Langevin generator on a convex region R ⊂ F_M(G) where the constrained Hessian satisfies Hess_{$\mathbf{1}^\perp$}(Ẽ)|_R ⪰ κI with κ > 0 inherits the Bakry-Émery CD(κ,∞) condition directly from T-PF-A1-SDE Cat A + Bochner-Lichnerowicz. Standard BGL 2014 / Otto-Villani 2000 corollaries then give (a) Poincaré λ_1 ≥ κ; (b) Wasserstein W_2-contractivity rate κ; (c) relative-entropy decay rate 2κ. On the consensus baseline (2D torus L=16, α=1, c=1/2, T_*=0.1) in the sub-critical branch (β=0.1, T8-subcritical), the convex Hessian at u* = c·1 gives κ ≈ 0.509 — *eight orders of magnitude sharper* than canonical T-PF-A1-PE's unconditional exp(-osc/T_*) bound on this reference example. L-BAKRY-EMERY-SCC is **complementary, not replacement**, for canonical T-PF-A1-PE Cat A (canonical handles unconditional global mixing, Bakry-Émery handles sharp in-convex-region dynamics) and for file 04's Sc^{(2)} Schur complement (file 04 = linear-algebra side, file 11 = functional-analysis side; together = full H-Morse spectral structure). The two-timescale decomposition (fast in-basin κ via Bakry-Émery, slow between-basin exp(-ΔE/T_*) via Eyring-Kramers) provides a *partial* attack on OP-0005-DYN (theorem_status.md L803, OPEN) without closing OP-HMORSE-SADDLE (theorem_status.md L594, OPEN). Surface-tension rescaling (file 06) gives κ → s·κ under (α,β)→(sα,sβ), making all three dynamical rates scale linearly with energy. CV-1.15 action-based temporal framework receives a spectral grounding through the Otto-Villani W_2-gradient-flow formulation. **Hard constraints 16/16 ✓; canonical edits 0; consensus baseline σ=(√2/6)√(αβ) preserved**.

---

*End of file 11. Line count: ~640. Cat A target *in convex regions only*. κ at reference example (β=0.1 sub-critical branch): ≈ **0.509** (matches Theorem 4 prediction 4λ_2 + βW''(c) = 0.609 − 0.1). Bakry-Émery vs canonical T-PF-A1-PE: ~10^8× sharper in convex regions, but does NOT replace canonical (which remains the unconditional anchor outside convex regions). Complementary to file 04 Schur. Does NOT close OP-0005-DYN or OP-HMORSE-SADDLE.*
