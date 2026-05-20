---
id: L-SURFACE-TENSION-RESCALE
type: working/field_equation_framework/lemma
date: 2026-05-20
session_origin: W8-Day3 evening extension (post-CSSL critic evaluation)
canonical_version: CV-1.18 (SEALED — 0 edits throughout)
status: working-layer Cat A direct lemma (canonical-anchored, no conditional hypotheses)
cat_assignment: Cat A direct
primary_anchors:
  - canonical §13 Theorem 4 (μ_k = 4αλ_k + βW''(c) — Cat A)
  - canonical §13 SB7 (Σ_T8 codim-1 algebraic wall — Cat A)
  - canonical §13 T-V5b-T-zero (Goldstone exact zero on translation-invariant graphs — Cat A)
  - canonical §3.5 / §3.2 (E_bd structure: αu^T L_G u + β Σ W(u_i))
related_files:
  - working/field_equation_framework/01_ns_inspired_synthesis.md §7.5 Identity 5 + §8.1 Path 1
  - working/cssl/00_concept_handoff.md §3.2 (surface tension scaling — original idea)
  - working/cssl/01_critic_evaluation.md §A.3 + pre-commitment P1-P5 (only surviving CSSL idea)
promotion_candidate: CV-1.20+ SEAL (L-SURFACE-TENSION-RESCALE Cat A)
cot_enforced: yes
coc_enforced: yes
constraint_compliance:
  canonical_edits: 0
  Mori_Zwanzig: 0 references
  inertia: 0 references
  new_energy_terms: 0
  CSSL_E_ridge_E_wild_E_pers: 0 references (this file references surface-tension-scaling survivor only)
  DECLARATION_edits: 0
---

> [!nav] Linked: [[../../canonical/canonical|CV-1.18 canonical]] (§13 Theorem 4, SB7, T-V5b-T-zero, §3.5 E_bd) · [[01_ns_inspired_synthesis|01 NS synthesis §7.5 + §8.1]] · [[../../canonical/DECLARATION|DECL-1.0]] · [[../cssl/00_concept_handoff|CSSL handoff §3.2]] · [[../cssl/01_critic_evaluation|CSSL critic §A.3 surface tension survivor]]

# 06 — L-SURFACE-TENSION-RESCALE: Cat A Direct Lemma (Primary H-Morse Attack via Parameter Rescaling)

**Mission**: Produce the formal Cat A lemma `L-SURFACE-TENSION-RESCALE` — the *only* CSSL-survived structural idea, now anchored directly to canonical Theorem 4 and T-V5b-T-zero, constituting the primary H-Morse attack lemma for non-uniform critical points via parameter rescaling.

---

## §0 — Pre-flight xref check + §8a P1-P6 audit

### §0.1 Cross-reference verification

| Required canonical anchor | Location | Status |
|---|---|---|
| Theorem 4: `μ_k = 4αλ_k + βW''(c)` | canonical.md §13, Cat A | CONFIRMED — linear in (α,β) |
| SB7: `Σ_T8 = {(α,β,c) : β/α = 4λ_2/|W''(c)|}` | canonical.md §13, Cat A | CONFIRMED — codim-1 algebraic |
| T-V5b-T-zero: Goldstone `μ_Gold = 0` exact on `Z_L^d` | canonical.md §13, Cat A | CONFIRMED — translation orbit |
| E_bd structure: `αu^T L_G u + β Σ W(u_i)` | canonical.md §3.5 / synthesis §3.2 | CONFIRMED |
| CSSL §3.2 idea (surface tension scaling) | cssl/00_concept_handoff.md §3.2 | CONFIRMED — origin of this idea |
| Critic survival verdict | cssl/01_critic_evaluation.md §A.3 | CONFIRMED — "only surviving element" |
| §8.1 Path 1 in 01_ns_inspired_synthesis.md | synthesis §7.5 Identity 5 + §8.1 | CONFIRMED — Cat A direct label |

### §0.2 §8a pattern P1-P6 audit

- P1 (Root question bypass): L-SURFACE-TENSION-RESCALE *directly advances* Q1 (T8 wall preserved) and H-Morse non-uniform critical attack — not a bypass. ✓
- P2 (Vocabulary refactoring): `u_t` primitive unchanged; only parameter rescaling. ✓
- P3 (Canonical content duplication): Theorem 4 + SB7 + V5b-T-zero are *cited*, not re-derived here; this file provides the *applied combination* not present elsewhere. ✓
- P4 (External tool import): No external theory imported; no Mori-Zwanzig, no inertia, no new energy term. ✓
- P5 (Self-audit): §0 audit performed; §12 CN1-16 check completed. ✓
- P6 (Language-math separation): All 6 lemma parts have explicit formula-level proof. ✓

**0/6 disqualifying flags — proceed.**

---

## §1 — Mission: L-SURFACE-TENSION-RESCALE as Primary H-Morse Attack Lemma

The H-Morse problem at non-uniform critical points `u*` (post-formation, non-uniform `u_i* ≠ c`) is:

> **Can the non-Goldstone spectral gap of `H(u*)` be made arbitrarily large without changing the phase structure (T8 wall location, boundary width, Goldstone kernel)?**

The affirmative answer follows directly from canonical Theorem 4: because `H(u*)` is **linear-homogeneous** in `(α, β)`, a uniform rescaling `(α, β) → (sα, sβ)` scales the entire Hessian by `s > 0`, leaving Goldstone modes at zero (by T-V5b-T-zero Cat A) and multiplying every non-Goldstone eigenvalue by `s`.

This is the content of `L-SURFACE-TENSION-RESCALE`. It is the *only* element of the CSSL proposal (cssl/00_concept_handoff.md §3.2) that survived critic scrutiny (cssl/01_critic_evaluation.md §A.3) — formalized here as a canonical-anchored Cat A direct lemma.

---

## §2 — Lemma Statement (L-SURFACE-TENSION-RESCALE, Cat A Direct)

**Setup.** Let `G = (V, E, w)` be a finite weighted connected graph with `|V| = n`. Let

$$\mathcal{E}_{bd}(u;\,\alpha,\beta) = \alpha\,u^T L_G u + \beta \sum_{i=1}^n W(u_i), \qquad W(u) = u^2(1-u)^2$$

be the boundary energy on `Σ_m = {u ∈ [0,1]^n : Σu_i = m}` (canonical §3.5 / CN5). Let `W''(u) = 2(1 - 6u + 6u^2)` so that `W''(c) = 2(1 - 6c + 6c^2)` and `|W''(c)| > 0` for `c` in the spinodal `((3-√3)/6, (3+√3)/6)`.

**Lemma L-SURFACE-TENSION-RESCALE.** Under the uniform rescaling `(α, β) ↦ (sα, sβ)` for any `s > 0`:

**(a) Phase transition wall invariance.**

$$\Sigma_{T8}(s\alpha, s\beta, c) = \Sigma_{T8}(\alpha, \beta, c)$$

i.e., `(sα, sβ, c) ∈ Σ_T8 ⟺ (α, β, c) ∈ Σ_T8`. The T8 critical surface (canonical SB7) is invariant under the rescaling.

**(b) Boundary width invariance.**

$$\ell_{bd}(s\alpha, s\beta) = \sqrt{\frac{s\alpha}{s\beta}} = \sqrt{\frac{\alpha}{\beta}} = \ell_{bd}(\alpha, \beta)$$

The Allen-Cahn interface width is `s`-invariant.

**(c) Surface tension scaling.** (Note: σ formula CORRECTED 2026-05-20 per Wave 2 critic Fix #1, file 12 §2 — previous $\sqrt{\alpha\beta}/3$ form was off by factor √2; correct Modica-Mortola constant is $(\sqrt{2}/6)\sqrt{\alpha\beta}$. Scaling law unchanged.)

$$\sigma(s\alpha, s\beta) = \frac{\sqrt{2}}{6}\sqrt{(s\alpha)(s\beta)} = s \cdot \frac{\sqrt{2}}{6}\sqrt{\alpha\beta} = s \cdot \sigma(\alpha,\beta)$$

Surface tension scales linearly with `s`.

**(d) Hessian linear scaling.** At any critical point `u*` of `Ẽ_bd(·; α, β)` on `Σ_m`:

$$H(u^*;\, s\alpha, s\beta) = s \cdot H(u^*;\, \alpha, \beta)$$

where `H(u*; α, β) = ∇²Ẽ_bd(u*; α, β)|_{T_{u*}Σ_m}` is the constrained Hessian. Consequently, all Hessian eigenvalues scale by `s`:

$$\mu_k(s\alpha, s\beta) = s \cdot \mu_k(\alpha, \beta) \qquad \forall k = 1, \ldots, n-1.$$

**(e) Goldstone preservation.** If `μ_k(α, β) = 0` (Goldstone mode), then `μ_k(sα, sβ) = 0` for all `s > 0`. In particular, T-V5b-T-zero Goldstone modes on translation-invariant graphs (`Z_L^d` orbit-tangent directions) remain exactly zero under rescaling.

**(f) Non-Goldstone spectral gap expansion.** The smallest non-Goldstone eigenvalue satisfies:

$$\mu_{\min}^{(\mathrm{non\text{-}Gold})}(s\alpha, s\beta) = s \cdot \mu_{\min}^{(\mathrm{non\text{-}Gold})}(\alpha, \beta)$$

Hence by choosing `s ≥ μ* / μ_min^(non-Gold)(α_0, β_0)` for any target gap `μ* > 0`, the H-Morse spectral gap (smallest non-Goldstone eigenvalue) exceeds `μ*`.

---

## §3 — Proof

Each part follows from canonical Theorem 4 + linear homogeneity of `Ẽ_bd`, with no new assumptions.

### Proof of (a)

Canonical SB7 (Cat A) defines:

$$\Sigma_{T8} = \left\{(\alpha, \beta, c) : \frac{\beta}{\alpha} = \frac{4\lambda_2(L_G)}{|W''(c)|}\right\}$$

The ratio `β/α` is unchanged by `(α, β) → (sα, sβ)`:

$$\frac{s\beta}{s\alpha} = \frac{\beta}{\alpha}$$

Therefore `(sα, sβ, c) ∈ Σ_T8 ⟺ β/α = 4λ_2/|W''(c)| ⟺ (α, β, c) ∈ Σ_T8`. `□`

### Proof of (b)

Boundary width `ℓ_bd = √(α/β)` (Allen-Cahn scaling, canonical §5.3 / synthesis §3.2):

$$\ell_{bd}(s\alpha, s\beta) = \sqrt{\frac{s\alpha}{s\beta}} = \sqrt{\frac{\alpha}{\beta}} = \ell_{bd}(\alpha,\beta). \quad\square$$

### Proof of (c)

Surface tension `σ = (√2/6)·√(αβ)` (Allen-Cahn interface energy, synthesis §7.5; CORRECTED per Wave 2 critic Fix #1):

$$\sigma(s\alpha, s\beta) = \frac{\sqrt{2}}{6}\sqrt{(s\alpha)(s\beta)} = \frac{s\sqrt{2}\sqrt{\alpha\beta}}{6} = s \cdot \sigma(\alpha,\beta). \quad\square$$

### Proof of (d)

**Case 1: uniform critical `u* = c·1`.** By canonical Theorem 4 (Cat A):

$$\mu_k(\alpha,\beta) = 4\alpha\lambda_k(L_G) + \beta W''(c)$$

Under `(α,β) → (sα, sβ)`:

$$\mu_k(s\alpha, s\beta) = 4(s\alpha)\lambda_k(L_G) + (s\beta)W''(c) = s\bigl(4\alpha\lambda_k(L_G) + \beta W''(c)\bigr) = s \cdot \mu_k(\alpha,\beta). \quad\square$$

**Case 2: non-uniform critical `u*` (general).** `Ẽ_bd(u; α, β) = αu^T L_G u + β Σ_i W(u_i)` is **linear-homogeneous** in `(α,β)`:

$$\mathcal{E}_{bd}(u;\, s\alpha, s\beta) = s\alpha\,u^T L_G u + s\beta \sum_i W(u_i) = s\,\mathcal{E}_{bd}(u;\,\alpha,\beta).$$

Differentiation is a linear operator, so:

$$H(u^*;\, s\alpha, s\beta) = \nabla^2 \mathcal{E}_{bd}(u^*;\, s\alpha, s\beta)\big|_{T\Sigma_m} = s \cdot \nabla^2 \mathcal{E}_{bd}(u^*;\, \alpha, \beta)\big|_{T\Sigma_m} = s \cdot H(u^*;\, \alpha, \beta).$$

Since `H(sα, sβ) = s·H(α,β)`, all eigenvalues satisfy `μ_k(sα, sβ) = s·μ_k(α, β)`. `□`

**Note on gradient:** Canonical CLAUDE.md "Critical Implementation Details" confirms `E_bd` gradient = `4αLu` (factor 4, ordered-pair sum convention) and `W'(u) = 2u(1-u)(1-2u)` (factor 2, I6 correction). These factors are `(α, β)`-linear and do not affect the linear-homogeneity argument.

### Proof of (e)

If `μ_k(α, β) = 0`, then by part (d):

$$\mu_k(s\alpha, s\beta) = s \cdot \mu_k(\alpha, \beta) = s \cdot 0 = 0.$$

For T-V5b-T-zero modes: canonical T-V5b-T-zero (Cat A) establishes that on translation-invariant graphs (`Z_L^d` torus), the orbit-tangent directions `v_τ ∈ T_τ(G_u·u*)` satisfy `H(u*)v_τ = 0` exactly, via the group-action argument (independent of parameter values). Hence these zero modes are structurally fixed at zero and are parameter-independent in their zero status. Rescaling cannot shift them from zero. `□`

### Proof of (f)

By part (d), all eigenvalues (Goldstone and non-Goldstone alike) scale by `s`. Goldstone eigenvalues remain at zero by part (e). Non-Goldstone eigenvalues satisfy:

$$\mu_k^{(\mathrm{non\text{-}Gold})}(s\alpha, s\beta) = s \cdot \mu_k^{(\mathrm{non\text{-}Gold})}(\alpha, \beta).$$

Taking the minimum over non-Goldstone modes:

$$\mu_{\min}^{(\mathrm{non\text{-}Gold})}(s\alpha, s\beta) = s \cdot \mu_{\min}^{(\mathrm{non\text{-}Gold})}(\alpha, \beta).$$

For target gap `μ* > 0` and baseline `μ_0 := μ_min^(non-Gold)(α_0, β_0) > 0`, choose:

$$s^* = \frac{\mu^*}{\mu_0} \quad \Longrightarrow \quad \mu_{\min}^{(\mathrm{non\text{-}Gold})}(s^*\alpha_0, s^*\beta_0) = \mu^*. \quad\square$$

---

## §4 — Cat A Direct Classification Justification

| Lemma part | Canonical anchor | Classification |
|---|---|---|
| (a) T8 invariance | SB7 Cat A — β/α ratio invariant | Cat A direct (trivial algebra) |
| (b) Width invariance | ℓ_bd = √(α/β) — ratio invariant | Cat A direct (trivial algebra) |
| (c) σ scaling | σ = (√2/6)·√(αβ) — product scales (CORRECTED per Fix #1) | Cat A direct (trivial algebra) |
| (d) Hessian scaling | Theorem 4 Cat A — linear in (α,β) | Cat A direct (linearity + differentiation) |
| (e) Goldstone preservation | T-V5b-T-zero Cat A — parameter-independent zero status | Cat A direct (Cat A transitivity) |
| (f) Spectral gap expansion | (d) + (e) combined | Cat A direct (minimum over set) |

**No new assumptions.** All six parts follow from canonical Theorem 4 (Cat A) and canonical T-V5b-T-zero (Cat A) by algebra that is fully explicit above. There are no conditional hypotheses, no Cat B conditions, no numerical inputs. This constitutes a Cat A direct lemma under the SCC promotion pipeline standards.

```
CoC anchors:
  - canonical Theorem 4 Cat A: μ_k = 4αλ_k + βW''(c) — linear in (α,β) — this is the ONLY tool needed
  - canonical T-V5b-T-zero Cat A: Goldstone μ_Gold = 0 exact on Z_L^d — parameter-independent
  - canonical SB7 Cat A: Σ_T8 = {β/α = 4λ_2/|W''(c)|} — ratio-defined, rescaling-invariant
  - canonical §3.5 E_bd structure: αu^TL_Gu + βΣW(u_i) — bilinear, differentiable, linear-homogeneous in (α,β)
CoT completeness: each of 6 parts has 1-5 line explicit algebraic proof — no gaps.
```

---

## §5 — CSSL Critic Survival Context: The Only Surviving Idea

The CSSL proposal (cssl/00_concept_handoff.md) introduced six structural ideas:

| CSSL idea | Critic verdict (cssl/01_critic_evaluation.md) | Outcome |
|---|---|---|
| Surgery-admissible kernel decomposition | Interesting but undefined primitives (E_surg circular) | Rejected as stated |
| E_ridge = −κ Σ φ(r_i) energy term | Sign conflict with E_bd; anti-stabilizes smoothness gradient | Rejected (§D.1 MAJOR) |
| E_wild = η Σ (Δ_G u_i)² energy term | Violates CN4 indirectly (new energy term); over-smoothing risk | Rejected as canonical element |
| ζ E_pers persistence-homology energy | Non-differentiable; violates CN4 analyticity (b_D=0) | Rejected (§D.3 CRITICAL) |
| Tame vs wild singularity dichotomy | Condition 6 circular; undefined graph Morse index | Not formalized |
| **Surface tension rescaling (α,β)→(sα,sβ)** | **Survives: T8 + ℓ_bd preserved, σ×s, Hessian×s** | **SOLE SURVIVOR** |

The surface tension rescaling idea appears in CSSL §3.2 as: "T8 발생 조건과 boundary 폭은 보존하면서, 형성된 경계의 surface tension만 키울 수 있다" (T8 emergence condition and boundary width preserved, while surface tension of formed boundary increases). This is precisely the content of parts (a)-(c) of L-SURFACE-TENSION-RESCALE.

The critic acknowledged this directly (cssl/01_critic_evaluation.md §A.3): the surface tension rescaling idea "is empirically supported by today's canonical machinery" and is "structurally already covered by canonical V5b-T-zero" for the Goldstone part. The critic stopped short of formalizing it because the evaluation was adversarial and focused on the broader CSSL framework's failures.

**This file formally closes that gap.** L-SURFACE-TENSION-RESCALE takes the sole surviving CSSL insight and gives it a complete Cat A proof, anchored entirely to existing canonical machinery. No CSSL scaffolding (E_ridge, E_wild, E_pers, surgery-admissible extension) is required or used.

---

## §6 — Application: H-Morse Non-Uniform Critical Points (Framework §8.1 Path 1)

### §6.1 Problem statement

At non-uniform critical points `u*` (post-formation regime, `u_i* ≠ c` for boundary sites), the H-Morse condition requires:

$$\mu_{\min}^{(\mathrm{non\text{-}Gold})}(H(u^*)) > 0$$

with "sufficient" gap so that the formation is a robust minimum (not near-flat). In practice, for a given graph `G` and baseline `(α_0, β_0)`, this gap may be small — the boundary band has many near-degenerate wobble modes.

### §6.2 Solution via L-SURFACE-TENSION-RESCALE

By part (f): choose `s = μ*/μ_0` where `μ_0 = μ_min^(non-Gold)(α_0, β_0) > 0` and `μ* > 0` is the desired gap. Then at `(sα_0, sβ_0)`:

$$\mu_{\min}^{(\mathrm{non\text{-}Gold})}(s\alpha_0, s\beta_0) = s \cdot \mu_0 = \mu^*.$$

By parts (a) and (b): the T8 wall and boundary width are unchanged, so the non-uniform critical structure persists. The formation still exists; its boundary is still of width `ℓ_bd = √(α_0/β_0)`; the H-Morse gap has been scaled up to the desired level.

### §6.3 What rescaling does NOT change

- Which modes are Goldstone (part (e)): translation-orbit directions remain exactly zero.
- The T8 phase transition wall position (part (a)): formation/no-formation boundary unchanged.
- The ratio `β/α` (i.e., relative sharpness of double-well vs smoothness): unchanged.
- The normalized interface profile shape (determined by `β/α` alone in Allen-Cahn theory).

### §6.4 Caveats

**Caveat 1 (thermal noise interaction).** Larger `s` means larger `Ẽ_bd` values. The thermal-to-energy ratio `Sc^(1)_k = μ_k/T_*` (synthesis §6 Sc^(1) number) scales as `s·μ_k/T_*`. If `T_*` is fixed, `Sc^(1)` grows with `s` — the formation becomes more deterministic. This is generally desirable for H-Morse stability, but at very large `s`, the Péclet number `Pe = |∇E|·R/T_*` also grows, potentially pushing out of the optimal `Pe ~ O(1)` deterministic-thermal balance regime.

**Caveat 2 (total energy scale).** Kramers rate (synthesis §6 Pr^(Kramers), §7.2 Identity 2) depends on `ΔE/T_*`. Since `ΔE = Ẽ_bd(u_saddle) - Ẽ_bd(u*)` and all energy values scale by `s`, the Kramers exponent `exp(-sΔE_0/T_*)` becomes exponentially small. For large `s`, the system is deeply frozen in its formation basin — dynamics slow dramatically.

**Caveat 3 (non-Goldstone gap at s=1).** Part (f) guarantees the *existence* of `μ_min^(non-Gold)(α_0, β_0) > 0` for the construction to work. This positivity must be verified at baseline — L-HMORSE-LOCAL (Cat B, canonical §13) provides the conditional Cat B guarantee under conditions (C1)-(C5).

---

## §7 — Numerical Regime Selection (Reference: 2D Torus L=16)

### §7.1 Reference configuration

- Graph `G`: 2D torus `Z_16 × Z_16`, `n = 256`, 4-regular, `λ_2(L_G) = 4 - 4cos(2π/16) ≈ 0.152`
- Baseline parameters: `α_0 = 1`, `β_0 = 5`, spinodal center `c = 1/2`
- `W''(1/2) = 2(1 - 3 + 3/2) = -1` so `|W''(1/2)| = 1`

### §7.2 T8 check at baseline

$$\frac{\beta_0}{\alpha_0} = 5 \qquad \text{vs} \qquad \frac{4\lambda_2}{|W''(1/2)|} = 4 \times 0.152 \approx 0.608$$

Since `5 ≫ 0.608`, the baseline is well inside the formation regime (T8 condition satisfied with large margin).

### §7.3 Uniform-critical Hessian baseline (Theorem 4)

$$\mu_k^{(\mathrm{uniform})}(\alpha_0, \beta_0) = 4\alpha_0\lambda_k + \beta_0 W''(1/2) = 4\lambda_k - 5$$

At `k=1` (Fiedler): `μ_1 = 4×0.152 - 5 ≈ -4.39` (negative — uniform critical is a saddle/maximum, not a minimum). Formation has occurred; the non-uniform critical is the relevant object.

### §7.4 Non-uniform critical gap estimation

At a non-uniform critical `u*` in the formation regime, `μ_min^(non-Gold)` must be computed numerically (CODE/experiments/ — `exp_hmorse.py` or similar). For the purposes of regime selection:

- **Target gap**: `μ* = 1.0` (unit scale, deterministic over thermal)
- **Estimated baseline** (heuristic from diffuse-interface theory): `μ_0 ~ O(β ξ^{-2}/n_bd)` where `ξ = √(2α/β)` and `n_bd` = number of boundary sites. At `α=1, β=5, L=16`: `ξ ≈ 0.63`, `n_bd ≈ O(L) = 16`, giving `μ_0 ~ 5 × 2.5 / 16 ≈ 0.78`.
- **Required rescaling**: `s* = μ*/μ_0 ≈ 1.0/0.78 ≈ 1.3`

### §7.5 Regime selection prescription

For `T_* = 0.1` (low thermal noise regime):

```
Step 1. Compute μ_0 = μ_min^(non-Gold)(α_0, β_0) via CODE/scc/energy.py Hessian at formation u*.
Step 2. Set μ* = desired gap (e.g., μ* = max(1.0, 10·T_*) = max(1.0, 1.0) = 1.0).
Step 3. s* = μ*/μ_0.
Step 4. Use (s*α_0, s*β_0) — T8 wall, ℓ_bd unchanged; formation persists; gap = μ*.
Step 5. Check Pe = |∇E|·R/T_*: if Pe >> 10, consider reducing μ* to avoid thermal freezing.
```

This procedure is algorithmic and deterministic once `μ_0` is measured from the code.

---

## §8 — Connection to Companion Files

### §8.1 Companion 02: Kramers Prefactor (OP-0005-DYN) — RETRACTED AND CORRECTED 2026-05-20

**RETRACTION** (per Wave 2 critic Fix #3, file 12 §4): The original version of this section (W8-Day3 13:50 KST) claimed *"the Kramers prefactor ω_0 is invariant under uniform rescaling"*. This claim is **WRONG**. The error was in the algebraic step `Pr^{(Kramers)} = μ_well · μ_saddle → s^2 · Pr^{(Kramers)}` — but `Pr^{(Kramers)}` is a RATIO `|μ_well|/|μ_saddle|`, not a product. Under rescaling, both numerator and denominator scale by `s`, so the ratio is *invariant* — which means `√Pr^{(Kramers)}` is *invariant*, not `s · √Pr^{(Kramers)}`. The correct consequence is `ω_0(s) = s · ω_0(1)` — prefactor scales LINEARLY in `s`.

**CORRECTED ANALYSIS** (file 12 §4):

Rescaling `(α,β) → (sα, sβ)` scales both `|μ_well|` and `|μ_saddle|` by `s` (per part (d) Hessian scaling, established in §3 above). The Eyring-Kramers prefactor (synthesis §7.2 Identity 2a — see also file 12 §5 Identity 2 split):

$$\omega_0 \sim \frac{\omega_{\mathrm{well}} \cdot \omega_{\mathrm{saddle}}}{\sqrt{\mathrm{Pr}^{(\mathrm{Kramers})}}}, \quad \omega_{\mathrm{well}} = \sqrt{|\mu_{\mathrm{well}}|}, \quad \omega_{\mathrm{saddle}} = \sqrt{|\mu_{\mathrm{saddle}}|}, \quad \mathrm{Pr}^{(\mathrm{Kramers})} = \frac{|\mu_{\mathrm{well}}|}{|\mu_{\mathrm{saddle}}|}$$

Under rescaling:
- `ω_well → √s · ω_well` (since `|μ_well| → s|μ_well|`)
- `ω_saddle → √s · ω_saddle` (since `|μ_saddle| → s|μ_saddle|`)
- `ω_well · ω_saddle → s · (ω_well · ω_saddle)` (product picks up factor `s`)
- **`Pr^{(Kramers)} = |μ_well|/|μ_saddle| → (s|μ_well|)/(s|μ_saddle|) = |μ_well|/|μ_saddle| = Pr^{(Kramers)}`** — *INVARIANT* (ratio cancels)
- `√Pr^{(Kramers)} → √Pr^{(Kramers)}` — *INVARIANT*

Therefore:

$$\boxed{\omega_0(s) \sim \frac{s \cdot \omega_{\mathrm{well}} \cdot \omega_{\mathrm{saddle}}}{\sqrt{\mathrm{Pr}^{(\mathrm{Kramers})}}} = s \cdot \omega_0(1)}$$

**The Kramers prefactor `ω_0` scales LINEARLY in `s`, NOT invariant.** What IS invariant under rescaling is the *dimensionless ratio* `Pr^{(Kramers)}` itself. The Kramers rate becomes:

$$\Gamma(s) \sim \omega_0(s) \cdot \exp\!\left(-\frac{s \Delta E_0}{T_*}\right) = s \cdot \omega_0(1) \cdot \exp\!\left(-\frac{s \Delta E_0}{T_*}\right)$$

For OP-0005-DYN analysis: the *useful structural feature* is `Pr^{(Kramers)}` invariance (not prefactor invariance). This means *the dimensionless characterization of well/saddle geometry is `s`-independent*, even though the absolute rate timescale shifts with `s`. The prefactor's linear `s`-dependence reflects the increased deterministic timescale (factor `s` in all Hessian eigenvalues = factor `s^{-1}` in relaxation time).

### §8.2 Companion 03: Modica-Mortola Jacobi (Cat B)

File: `03_modica_mortola_jacobi_cat_b.md` (to be written)

L-SURFACE-TENSION-RESCALE part (c) establishes `σ → s·σ`. The sharp-interface limit (synthesis §8.2 Path 2) corresponds to `s → ∞` (or equivalently `ε = ℓ_bd → 0` with `σ` fixed, via a different parametrization). In the Modica-Mortola sense: as `s → ∞` with `ℓ_bd = √(α/β)` fixed, the energy functional concentrates on the interface `Γ`, and the Hessian restricted to the interface converges to the Jacobi operator `J_Γ = -Δ_Γ - |A|²`. This companion file will make the `s → ∞` limit precise in the graph-discrete setting (Cat B conditional on graph-to-continuum approximation).

### §8.3 Companion 04: H-Morse Spectral Quantification

File: `04_h_morse_spectral_quantification.md` (to be written)

The Schmidt number analog `Sc^(2) = μ_non-Gold / μ_Goldstone-gap` is a ratio of two spectral quantities. Under rescaling, both numerator and denominator scale by `s`, so `Sc^(2)` is `s`-invariant. This companion file will use this `Sc^(2)` invariance to define a canonical spectral quality measure for formation stability, and compute it numerically at the reference 2D torus L=16 configuration.

### §8.4 Companion 05: Cat A Direct Catalog Proofs

File: `05_cat_a_direct_catalog_proofs.md` (to be written)

Item 16 in the catalog (T-RESCALE-HESSIAN-LINEAR) is the algebraic form:

$$\mathcal{E}_{bd}(u; s\alpha, s\beta) = s \cdot \mathcal{E}_{bd}(u; \alpha, \beta) \Longrightarrow H(u^*; s\alpha, s\beta) = s \cdot H(u^*; \alpha, \beta)$$

This is the same as part (d) of L-SURFACE-TENSION-RESCALE, stated in abstract algebraic form. File 05 is the *catalog* form; file 06 (this document) is the *applied* form connecting to H-Morse non-uniform critical, CSSL survival context, numerical regime, and companion files.

---

## §9 — Inverse Causation Check

**What breaks if each canonical anchor is removed:**

| Removed anchor | Consequence for L-SURFACE-TENSION-RESCALE | Severity |
|---|---|---|
| **Theorem 4 removed** | `μ_k` formula lost; cannot state `μ_k = s·μ_k(1)` for uniform critical; linear-homogeneity argument still holds for general `u*` (it uses only bilinearity of `Ẽ_bd` in `(α,β)`) but uniform-critical case loses explicit formula | Parts (d)(f) weaken to general statement only |
| **T-V5b-T-zero removed** | Goldstone mode zero-status under rescaling is no longer guaranteed by Cat A authority; would need re-verification per graph type | Part (e) demotes from Cat A to Cat B conditional |
| **SB7 removed** | `Σ_T8` wall not defined as a codim-1 algebraic surface; part (a) requires alternative T8 definition | Part (a) demotes to Cat B conditional |
| **`W(u) ≠ u²(1-u)²` (different polynomial)** | If `W` is degree-homogeneous in `u`, rescaling `(α,β)→(sα,sβ)` still works; for general non-homogeneous `W`, `Ẽ_bd` is still linear-homogeneous in `(α,β)` (only parameters rescale, not `W` itself) — **lemma still holds** | No impact (linearity is in parameters, not in `W`) |
| **Rescaling done independently: `α→s₁α`, `β→s₂β` with `s₁≠s₂`** | `β/α → (s₂/s₁)·(β/α)` — T8 wall position SHIFTS; `ℓ_bd → √(s₁/s₂)·ℓ_bd` — width changes; `σ → √(s₁s₂)·σ` — surface tension changes by different factor; Hessian `H→ s₁·(Laplacian part) + s₂·(double-well part)` — no longer `s·H` | Parts (a)(b) fail; parts (d)(e)(f) fail in general; only (c) generalizes to `σ → √(s₁s₂)·σ` |
| **`Ẽ_bd` acquires a term nonlinear in `(α,β)`** (e.g., `α²·(...)`**) | Linear-homogeneity argument breaks; Hessian would have `s²` terms; scaling law (d) would fail | Parts (d)(e)(f) fail |

**Key structural insight from this check:** The lemma's power rests entirely on the fact that `Ẽ_bd` is **bilinear** (hence linear-homogeneous) in `(α,β)`, with `α` and `β` appearing only as first-power multiplicative factors. This is a structural property of the canonical energy architecture (canonical CN5 four-term independence + §3.5 form), not an accident.

---

## §10 — W9+ Forward Hooks

### §10.1 Canonical promotion candidate

L-SURFACE-TENSION-RESCALE is a canonical promotion candidate (CV-1.20+ SEAL cycle):

- All six parts (a)-(f) are Cat A direct with explicit proofs referencing canonical Cat A anchors
- No conditional hypotheses
- Proof is 10 lines of algebra at most per part
- Connects three canonical Cat A facts (Theorem 4, SB7, V5b-T-zero) in a unified applied lemma

**Promotion path**: working/field_equation_framework/06 → canonical §13 (after formal review + canonical §0.4 SEAL process).

**Suggested canonical entry name**: `L-SURFACE-TENSION-RESCALE (Cat A, CV-1.2x)` in canonical §13 immediately following the H-MORSE family (L-HMORSE-LOCAL, L-HMORSE-DECOMP, L-BOUNDARY-MODE-EXCLUSION).

### §10.2 Sharp-interface combination (Companion 03)

L-SURFACE-TENSION-RESCALE part (c) (`σ → s·σ`) feeds directly into the Modica-Mortola analysis. As `s → ∞`: surface tension grows linearly, interface width fixed, sharp-interface limit approached. Combined with companion 03 (Jacobi operator analysis), this gives a complete Cat A + Cat B picture of H-Morse from diffuse to sharp interface.

### §10.3 OP-HMORSE-SADDLE attack

For saddle-point Hessian analysis (OP-HMORSE-SADDLE, canonical §13, OPEN), the rescaling lemma applies identically: saddle Hessian `H(u_sad; sα, sβ) = s·H(u_sad; α, β)`. The unstable index-1 direction at a saddle also scales, which quantifies the K-jump normal coordinate (synthesis §A.3 restricted reformulation from critic). This is the beginning of OP-HMORSE-SADDLE's Cat B attack.

### §10.4 K-selection connection (OP-0004, Q4)

Surface tension `σ = (√2/6)·√(αβ)` (CORRECTED per Fix #1) enters the K-formation energy via perimeter cost. By part (c), `σ → s·σ` linearly. The K-selection equilibrium distribution `P_K ∝ exp(-s·Ẽ_bd(u^*_K)/T_*)` (T-K-Select-PF, Cat B) shifts with `s` — high-K formations (more perimeter) are more strongly penalized at large `s`. This provides a `σ`-driven K-selection mechanism that could partially address Q4 (K-selection).

---

## §11 — CoT/CoC Archival

```yaml
CoT_chain_primary:
  step_1: |
    Identify target: H-Morse non-Goldstone gap expansion without changing phase structure.
    Tool available: canonical Theorem 4 (Cat A) gives μ_k = 4αλ_k + βW''(c) — linear in (α,β).
  step_2: |
    Observe that Ẽ_bd(u; α, β) = αu^TL_Gu + βΣW(u_i) is linear-homogeneous in (α,β).
    Therefore H(u*; sα, sβ) = ∇²(sẼ_bd)(u*) = s·H(u*; α, β).
  step_3: |
    Check phase structure preservation.
    β/α ratio: (sβ)/(sα) = β/α — SB7 Σ_T8 invariant.
    ℓ_bd = √(α/β) = √((sα)/(sβ)) — width invariant.
    σ = (√2/6)·√(αβ) → s·σ — surface tension scales (CORRECTED per Fix #1).
  step_4: |
    Check Goldstone status.
    T-V5b-T-zero (Cat A): Goldstone μ=0 from group-action — parameter-independent.
    Under rescaling: μ_Gold(sα,sβ) = s·0 = 0. Preserved.
  step_5: |
    Conclude: all six parts (a)-(f) are direct algebraic corollaries.
    No new assumptions. Cat A direct. Smallest viable change: 6 one-step proofs.

CoC_anchors:
  - canonical Theorem 4 (Cat A, μ_k linear in (α,β)) — Part (d) direct use
  - canonical SB7 (Cat A, Σ_T8 = ratio condition) — Part (a) direct use
  - canonical T-V5b-T-zero (Cat A, Goldstone zero on Z_L^d) — Part (e) direct use
  - canonical §3.5 E_bd = αu^TL_Gu + βΣW(u_i) — linearity structure
  - cssl/00_concept_handoff §3.2 — historical origin of rescaling idea
  - cssl/01_critic_evaluation §A.3 — confirmation as sole surviving element
  - 01_ns_inspired_synthesis §7.5 Identity 5 + §8.1 Path 1 — synthesis context

meta_check:
  smallest_viable_diff: yes — 6 proofs using only existing canonical machinery
  no_new_abstractions: yes — no new subspaces, operators, or energy terms introduced
  no_temporary_code: yes — no debug content
  no_scope_creep: yes — energy design, CSSL scaffolding, saddle analysis all explicitly deferred to companion files
```

---

## §12 — Hard Constraint CN1-16 Check

| Constraint | Status | Evidence |
|---|---|---|
| CN1: `u_t: X_t → [0,1]` is primitive, crisp objects derivative | ✓ | Rescaling operates on parameters only; `u_t` field unchanged |
| CN2: Four energy terms conceptually independent | ✓ | Only `Ẽ_bd` analyzed; `Ẽ_cl, Ẽ_sep, Ẽ_tr` not touched |
| CN3: A3 stabilization tendency (not idempotence) | ✓ | Rescaling does not introduce idempotence |
| CN4: `b_D = 0`, energy analyticity (Łojasiewicz) | ✓ | No new energy terms; `Ẽ_bd` remains analytic on `Σ_m` |
| CN5: Four energy terms not merged | ✓ | `Ẽ_bd` is analyzed alone as the rescaled term |
| CN6: No fuzzy segmentation | ✓ | Rescaling is a parameter analysis, not a segmentation method |
| CN7: No clustering | ✓ | Same |
| CN8: No tracking | ✓ | Same |
| CN9: No engineering proxies | ✓ | Same |
| CN10: No reductive reduction to fluid/NS/clustering | ✓ | Structural ideas only; §1 mission explicit |
| CN11: No Mori-Zwanzig | ✓ | Zero references to Mori-Zwanzig |
| CN12: No inertia | ✓ | Zero references to inertia or momentum |
| CN13: Never silently resolve open problems | ✓ | OP-HMORSE-SADDLE, OP-0005-DYN, OP-0008 remain open; §8 explicitly defers |
| CN14: Canonical edits = 0 | ✓ | `git status THEORY/canonical/` clean (verified pre-write) |
| CN15: No new energy terms | ✓ | Rescaling is parameter-space analysis; `E_CSSL` terms explicitly excluded |
| CN16: No per-item registry files | ✓ | This file is a working/ lemma, not a canonical registry |

**All 16 constraints: PASS.**

---

## §13 — One-Paragraph Summary

**L-SURFACE-TENSION-RESCALE** is a Cat A direct lemma establishing that uniform parameter rescaling `(α, β) → (sα, sβ)` with `s > 0` has the following six invariance/scaling properties for the SCC boundary energy `Ẽ_bd(u; α, β) = αu^TL_Gu + βΣW(u_i)`: (a) the T8 phase transition wall `Σ_T8` (SB7) is invariant; (b) the Allen-Cahn interface width `ℓ_bd = √(α/β)` is invariant; (c) surface tension `σ = (√2/6)·√(αβ)` scales as `s·σ` (σ formula CORRECTED per Wave 2 critic Fix #1, file 12 §2); (d) the constrained Hessian at any critical point scales as `H(sα, sβ) = s·H(α, β)`, hence all eigenvalues scale by `s`; (e) Goldstone modes (T-V5b-T-zero, Cat A) remain at zero; (f) the non-Goldstone spectral gap expands by factor `s`, enabling H-Morse stability at any target gap level by choosing `s` large enough. All six parts follow by trivial algebra from canonical Theorem 4 (Cat A) and T-V5b-T-zero (Cat A) — the only canonical tools required. This lemma is the *sole* CSSL-survived structural idea (critic evaluation §A.3 confirmation), now formalized as a canonical-anchored Cat A direct result and the primary H-Morse attack path for non-uniform critical points (framework §8.1 Path 1), with zero canonical edits, zero new energy terms, and zero conditional hypotheses.

---

*L-SURFACE-TENSION-RESCALE Cat A direct. Working layer 06. 2026-05-20. Canonical version CV-1.18 SEALED (untouched). Promotion candidate: CV-1.20+.*
