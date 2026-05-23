---
type: working/field_equation_framework/derivation
date: 2026-05-20
session_origin: W8-Day3 evening, post-01_ns_inspired_synthesis Tier-1 (Modica-Mortola Jacobi Cat B target)
canonical_version: CV-1.18 SEALED (untouched throughout)
status: draft v0.1
authors: user (Jaehong Oh)
preceded_by:
  - W8-Day3 01_ns_inspired_synthesis.md §8.2 Path 2 + §7 Identity 5 (Cat B target placeholder)
  - W8-Day3 03_D_L_commutation.md §6 (L-INV-1/2/3 invariant-subspace condition on uniform critical)
  - W8-Day3 04_dynamic_class_investigation.md §6 (L-PROJ-1/L-PROJ-2/Corollary: SCC ≠ Cahn-Hilliard spectrum)
  - W8-Day3 working/cssl/01_critic_evaluation.md §A.1 + §D.3 + §E.4 + §F.6 + §I.3 (anti-patterns to avoid)
  - canonical §3.5 (E_bd structure), §3.7 + §9.3 (D operator), §13 Theorem 4, T-V5b-T-zero, T-σ-Lemma-1, L-HMORSE-LOCAL/DECOMP, L-BOUNDARY-MODE-EXCLUSION, T-OP6-B, OP-HMORSE-SADDLE
purpose: |
  Derive the Modica-Mortola Γ-convergence + Jacobi-operator-on-boundary framework as a *Cat B target* for SCC non-uniform critical H-Morse. The graph→continuum step is the explicit conditional. Honest contrastive analytical tool — SCC is *not* Allen-Cahn (today's 04 §6 spectrum proof), but its continuum limit *belongs to the constrained Allen-Cahn class* (Rubinstein-Sternberg 1992). All canonical CN1-16 preserved; canonical 0 edits.
canonical_compatibility:
  CN1_canonical_edits: 0
  CN2_silent_OP_resolution: 0 (Cat B target only; OP-HMORSE-SADDLE attack point named, not solved)
  CN4_analyticity: preserved (no new energy term; continuum limit analysis only)
  CN5_4_term_independence: preserved (E_cl, E_sep, E_bd, E_tr separate; this file analyzes E_bd only)
  CN10_no_reductive_reduction: contrastive only ("SCC continuum limit ⊂ constrained-AC class", not "SCC = AC")
  primitive_u_t: preserved (Γ derived from u_t via sharp-interface limit, not primitive)
  canonical_edits: 0
  inertia_introduction: forbidden (first-order Langevin only)
  Mori_Zwanzig: forbidden (CV-1.18 SEAL deprecation)
  CSSL_energy_terms: forbidden (E_ridge / E_wild / E_pers — critic-rejected, §I.3 anti-pattern)
cot_enforced: yes
coc_enforced: yes
---

> [!nav] Linked: [[../../canonical/canonical|CV-1.18 canonical]] (§3.5, §3.7, §9.3, §13 Theorem 4, T-V5b-T-zero, T-σ-Lemma-1, L-HMORSE-LOCAL/DECOMP, L-BOUNDARY-MODE-EXCLUSION, T-OP6-B, OP-HMORSE-SADDLE L594) · [[../../canonical/DECLARATION|DECL-1.0]] · [[01_ns_inspired_synthesis|01 NS synthesis §8.2]] · [[../../logs/daily/2026-05-20/03_D_L_commutation|03 [D, L_G] §6]] · [[../../logs/daily/2026-05-20/04_dynamic_class_investigation|04 dynamic class §6]] · [[../cssl/01_critic_evaluation|CSSL critic §A.1 §D.3 §F.6 anti-patterns]]

# 03 — Modica-Mortola Jacobi Cat B Target for SCC Non-Uniform Critical H-Morse

**Mode**: working layer derivation (NOT verification, NOT SEAL prep, NOT canonical edit)
**Target**: derive `L-MODICA-JACOBI-HMORSE` as *Cat B target* lemma — the analytical foundation for non-uniform critical H-Morse via sharp-interface limit + Jacobi operator on the formation boundary `Γ`.
**Pre-work xref check** (canonical/working/* grep):
- `grep -rn "Modica\|Sternberg\|Jacobi.*operator\|second fundamental form" canonical/ working/`:
  - canonical §13 (T8 proof line 1169): *"Standard Modica-Mortola for the leading term; perturbation analysis for corrections."* (Cat A reference, R11) — **already in canonical at the energy-asymptotics level**.
  - working/field_equation_framework/01_ns_inspired_synthesis.md §8.2 (Path 2 placeholder, Cat B target).
  - working/cssl/01_critic_evaluation.md §F.6 (segmentation-drift risk, CN10 boundary).
- **Novel positioning**: 본 문서 = *first explicit derivation* of the Modica-Mortola → Jacobi spectrum chain on the SCC formation boundary `Γ`, with the *graph→continuum conditional* made explicit (Cat B classification). canonical line 1169 only mentions Modica-Mortola for E_bd energy *asymptotics*; the **Jacobi-spectrum side** (second variation of the Γ-limit functional on `Γ`) is novel here.

**§8a archive pattern P1-P6 audit**:
- **P1** (Foundational vacuity / DECL question 우회): DECL Q1 (T8 boundary appearance) + Q5 (시간 동일성) 직접 — Jacobi spectrum 의 *positive wobble gap* = 경계 안정성, Goldstone = 시간동일 invariance — *우회 아님* ✓.
- **P2** (Vocabulary refactoring): `u_t` primitive 미변경; `Γ = ∂{u^* ≈ 1}` 은 *derived* surface (sharp-interface limit 의 output), *primitive 아님* ✓.
- **P3** (Canonical content 중복): canonical §13 line 1169 "Standard Modica-Mortola" 는 *energy 의 leading-term asymptotics only*; 본 문서 = *second variation 의 Jacobi-spectrum derivation* — *strict extension, contradiction 0* ✓.
- **P4** (외부 도구 도입): Modica 1987 / Sternberg 1988 / Allard 1972 / Simon 1968 / Reilly 1977 / van Gennip-Bertozzi 2012 = *contrastive standard tools only*, *canonical L-HMORSE-LOCAL Cat B 의 직접 후속 analytical framework* ✓.
- **P5** (Self-audit): 본 §0 (this section) + §12 (CN1-16 hard constraint check) 의 dual audit ✓.
- **P6** (언어-수학 분리): 모든 정리 statement 수학으로 명시; 자연어 motivation 은 *contextual only* ✓.
- **0/6 부합** → 진행 합법.

---

## §1 Mission — Non-Uniform Critical H-Morse Analytical Foundation

### §1.1 본 문서가 *하는 것*

1. State Modica-Mortola Γ-convergence theorem (Modica 1987 + Sternberg 1988) — *contrastive standard tool*.
2. Map SCC `E_bd` to Allen-Cahn scaling: ε² ~ α/β, σ = c_W·√(αβ), ℓ_bd ~ √(α/β).
3. Derive Jacobi operator `J_Γ = −Δ_Γ − |A|²` at the formation boundary `Γ = ∂{u^* ≈ 1}` via second variation of the Γ-limit functional.
4. Analyze Jacobi spectrum on canonical model surfaces (sphere `S^{d−1}_R`): Goldstone (translation/rotation) = 0, first wobble `μ_ℓ=2 ~ (d−1)/R² > 0` (Morse non-degenerate).
5. State **L-MODICA-JACOBI-HMORSE** Cat B target lemma (5-step proof sketch + inverse causation).
6. Map to canonical anchors: L-HMORSE-LOCAL / L-HMORSE-DECOMP / L-BOUNDARY-MODE-EXCLUSION / T-V5b-T-zero / T-σ-Lemma-1 / T-OP6-B.
7. Discrete-graph corrections via van Gennip-Bertozzi 2012 (SIAM J Imaging Sci 5:1115) + Chambolle-Giacomini-Lussardi 2014.
8. Combined surface-tension scaling: combining with `06_surface_tension_rescaling_cat_a.md` rescaling `(α,β)→(sα,sβ)`, Jacobi spectrum gap scales as `σ/R² ~ s√(αβ)/R²`.
9. OP-HMORSE-SADDLE (theorem_status.md L594; cross-ref canonical.md L1967 caveat, OPEN) attack framework — saddle-point Jacobi operator has **one** negative eigenvalue (along K-jump direction) + Goldstone + positive wobble.

### §1.2 본 문서가 *하지 않는 것* (CN10 + CSSL anti-pattern boundary)

명시 금지:

- ❌ **SCC = Allen-Cahn 환원**: 04 §6 corollary (L-PROJ-1 + L-PROJ-2 + Corollary) 가 *SCC ≠ Cahn-Hilliard at spectrum level* 증명. 동일 logic 으로 *SCC ≠ Allen-Cahn at full dynamics level* (관성 부재 + 4 energy term 독립 + global mass conservation). Modica-Mortola 는 *contrastive analytical tool only* — *"SCC's continuum limit *belongs to* constrained-AC class"* 표현 사용, *"SCC = AC"* 표현 금지.
- ❌ **CSSL E_ridge / E_wild / E_pers 재도입**: critic-rejected (3 CRITICAL + 4 MAJOR). §I.3 anti-pattern 명시. Modica-Mortola Jacobi 는 *canonical E_bd* 만 사용.
- ❌ **Mori-Zwanzig**: CV-1.18 SEAL deprecation 위반 — 미도입.
- ❌ **새 energy term**: 본 문서 는 *canonical E_bd 의 sharp-interface 극한 spectrum analysis*. 새 항 0.
- ❌ **CSSL §F.6 segmentation drift**: 본 문서 는 *Jacobi spectrum analysis* 에 한정; *segmentation-based reformulation* (CN10 free-boundary drift 위험) 금지.
- ❌ **L-MODICA-JACOBI-HMORSE 의 Cat A 주장**: graph→continuum step 이 명시적 conditional — *Cat B target only*. Sub-claim 들 (Modica-Mortola Γ-convergence 자체 = Cat A in PDE literature; sphere Jacobi spectrum = Cat A in differential geometry literature) 은 *external Cat A*, *SCC 적용 시 Cat B conditional*.

### §1.3 Why this analytical framework matters

```
CoT step 1: SCC 의 *비-uniform critical H-Morse* (L-HMORSE-LOCAL Cat B, CV-1.16) 는 *active set 의 saturated nodes + free-tangent subspace* 의 정량 정밀도가 부족 — *왜 Goldstone 만 zero, wobble 은 positive*인가에 대한 *근본 analytical reason* 부재.
CoT step 2: Modica-Mortola Γ-convergence + Jacobi operator framework 는 *비-uniform critical* 의 H-Morse 의 *기하학적 source* (boundary Γ 의 curvature + Laplace-Beltrami spectrum) 의 explicit 정량.
CoT step 3: 이 framework 가 *OP-HMORSE-SADDLE* (theorem_status.md L594; cross-ref canonical.md L1967 caveat, OPEN) 의 직접 attack: saddle 의 한 negative direction = K-jump direction, 나머지 = Goldstone + positive wobble.
CoT step 4: 단, graph→continuum step 자체가 *Cat B conditional* (van Gennip-Bertozzi 2012 의 discrete Allen-Cahn Γ-convergence 결과 의 SCC 적용은 hypothesis chain 필요).
→ Therefore: L-MODICA-JACOBI-HMORSE = *Cat B target* (analytical framework with explicit conditional on graph→continuum).

CoC anchors:
  - canonical: §13 L-HMORSE-LOCAL Cat B (D-HMORSE-LOCAL (C1)(C2′)(C3)(C4)(C5) conditional)
  - canonical: §13 OP-HMORSE-SADDLE (OPEN, theorem_status.md L594; cross-ref canonical.md L1967 caveat)
  - canonical: §13 T-V5b-T-zero (Cat A, Goldstone exact zero on translation-invariant graphs)
  - canonical: §13 T-σ-Lemma-1 (Cat A, Hessian–G_u commutation)
  - DECL Q1 (T8 boundary) + Q5 (시간 동일성)
```

---

## §2 Modica-Mortola Γ-Convergence Theorem (Standard Contrastive Tool)

### §2.1 Theorem statement (Modica 1987 / Sternberg 1988)

**Theorem (Modica-Mortola Γ-Convergence)**. *Let `Ω ⊂ ℝ^d` (d ≥ 2) be open bounded, `W: ℝ → [0,∞)` a double-well potential with `W(0) = W(1) = 0`, `W > 0` on `(0,1)` and `W'(0) = W'(1) = 0`. Define the ε-Allen-Cahn energy*

$$
\mathcal{F}_\epsilon(u) = \int_\Omega \left( \epsilon \vert \nabla u\vert ^2 + \frac{1}{\epsilon} W(u) \right) dx, \quad u \in H^1(\Omega).
$$

*Subject to the mass constraint `∫_Ω u dx = m`, the family `{ℱ_ε}` Γ-converges (in `L¹(Ω)`-topology) as `ε → 0` to the perimeter functional*

$$
\boxed{\mathcal{F}_0(u) = c_W \cdot \mathcal{H}^{d-1}(\partial^* \{u = 1\} \cap \Omega), \quad c_W = \int_0^1 \sqrt{2 W(s)}\, ds,}
$$

*where `∂^*` denotes the reduced boundary and `u ∈ BV(Ω; \{0,1\})` (bounded variation, binary-valued).*

*References*: Modica 1987 (*Arch Rat Mech Anal* **98**:123–142); Sternberg 1988 (*Arch Rat Mech Anal* **101**:209–260, constrained version with mass).

### §2.2 Surface tension `c_W` for SCC double well

SCC double-well (canonical CV-1.18 I6): `W(u) = u²(1−u)²`.

```
CoT step 1: 2 W(s) = 2 s² (1-s)² → √(2W(s)) = √2 · s(1-s) (for s ∈ [0,1], integrand non-negative)
CoT step 2: c_W = ∫_0^1 √2 · s(1-s) ds
         = √2 · [s²/2 - s³/3]_0^1
         = √2 · (1/2 - 1/3)
         = √2 · (1/6)
         = √2 / 6  ≈ 0.2357
→ For SCC double well W(u) = u²(1-u)², the Modica-Mortola surface tension constant is c_W = √2/6.
```

*Cross-check*: Standard normalization `W̃(u) = (1/4)(1−u²)²` gives `c_W̃ = 2√2/3` (Modica's original form). SCC convention `W(u) = u²(1−u)²` (range `[0,1]` vs Modica's `[−1,1]`) yields `c_W = √2/6` — *scale-equivalent, normalization-different*.

### §2.3 Caveats / hypotheses for Γ-convergence

- **Continuum domain**: standard statement is on `Ω ⊂ ℝ^d`. *Graph version requires van Gennip-Bertozzi 2012* (see §7).
- **Smooth `Ω` regularity**: required for boundary integral `ℋ^{d−1}` to be well-defined.
- **Mass-constraint compatibility**: `m / |Ω| ∈ (0,1)` for non-trivial interface.
- **W double-well structure**: `W ≥ 0` with two distinct minima at `{0, 1}` — *exactly the SCC case*.

---

## §3 SCC `E_bd` → Allen-Cahn Scaling Map

### §3.1 Canonical `E_bd` form (canonical §3.5)

$$
\mathcal{E}_{\text{bd}}(u) = \alpha\, u^T L_G u + \beta \sum_{i \in X_t} W(u_i), \quad W(u) = u^2(1-u)^2.
$$

- `α u^T L_G u` = Dirichlet smoothness (graph Laplacian `L_G = D_G − A_G`); ordered-pair sum convention (CLAUDE.md I6: gradient is `4α·L u`, factor 4 from ordered-pair).
- `β W(u_i)` = double-well pointwise potential.

### §3.2 Allen-Cahn ε-scaling identification

```
CoT step 1: Rewrite E_bd in Allen-Cahn ε-form. Define ε such that the two terms balance in the sharp-interface limit:
  - E_bd / β = (α/β) · u^T L_G u + Σ W(u_i)
  - Identify: ε² = α/β (Allen-Cahn small-parameter)
  - Continuum analog (graph → continuum, see §7):
    α u^T L_G u  ↔  α ∫|∇u|² dx
    β Σ W(u_i)  ↔  β ∫ W(u) dx
  - Match to standard form ε|∇u|² + (1/ε)W(u):
    α = ε · K1, β = K2 / ε (for some K1, K2)
    → α β = K1 K2; α/β = ε² (K1/K2) → ε ~ √(α/β)
CoT step 2: Therefore the *effective ε* for sharp-interface limit is
  ε ~ √(α/β)
  with β/α → ∞ ⟺ ε → 0 (Allen-Cahn sharp-interface regime)
```

### §3.3 Surface tension `σ` and boundary width `ℓ_bd`

Combining §2.2 (`c_W = √2/6`) with §3.2 (`ε² ~ α/β`):

$$
\boxed{\sigma_{\text{SCC}} = c_W \cdot \sqrt{\alpha \beta} = \frac{\sqrt{2}}{6} \sqrt{\alpha\beta}.}
$$

Boundary transition width:

$$
\boxed{\ell_{\text{bd}} = \sqrt{\alpha/\beta} = \epsilon.}
$$

*Cross-check* (canonical T-OP6-B Cat A, §5.3b): boundary band measure `ρ_bd-band ≤ 2√(α/β) · |∂Ω|/n`. The `√(α/β)` factor *exactly matches `ℓ_bd`* — independent canonical anchor for the scaling.

### §3.4 Anchor table

| SCC quantity | Allen-Cahn analog | SCC explicit form | Canonical cross-anchor |
|---|---|---|---|
| α (smoothness coefficient) | ε (small parameter, scaled) | — | canonical §3.5 |
| β (double-well coefficient) | 1/ε (inverse scale) | — | canonical §3.5 |
| α/β | ε² | small parameter² | T-OP6-B √(α/β) bound |
| c_W (surface tension constant) | ∫₀¹√(2W) ds | √2/6 (W = u²(1−u)²) | canonical I6 W convention |
| σ (surface tension) | c_W √(αβ) | (√2/6)·√(αβ) | T-OP6-B, surface tension rescaling §7.5 |
| ℓ_bd (boundary width) | √(α/β) | √(α/β) | T-OP6-B 2√(α/β) factor |

---

## §4 Jacobi Operator at Formation Boundary `Γ`

### §4.1 Setup: non-uniform critical `u^*` with smooth boundary `Γ`

Let `u^*: X_t → [0,1]` be a non-uniform critical point of `E_bd|_{Σ_m}` with formation core `Ω^* = {x : u^*(x) ≈ 1}`. In the sharp-interface limit (`ε → 0`, i.e., `β/α → ∞`), `u^*` collapses to a binary indicator `1_{Ω^*}` with smooth boundary

$$
\Gamma = \partial \Omega^* \subset \text{(continuum domain via §7)},
$$

a (d−1)-dimensional embedded submanifold (assuming sufficient regularity — see hypothesis H2 in §6).

### §4.2 Second variation of `ℱ_0` at `Γ`

By Modica-Mortola Γ-convergence (§2.1), `ℱ_0(u) = σ · ℋ^{d−1}(Γ)` for `u = 1_{Ω}`. The mass constraint `∫ u dx = m` restricts variations to area-preserving normal perturbations:

$$
\Gamma_t = \{ x + t f(x) \nu(x) : x \in \Gamma \}, \quad \int_\Gamma f \, d\mathcal{H}^{d-1} = 0.
$$

where `ν` is the outward unit normal and `f: Γ → ℝ` is the normal variation field (mean-zero for area preservation).

**Second variation formula** (Allard 1972, *Ann Math* **95**:417; Simon 1968; Reilly 1977, *Indiana Univ Math J* **26**:459):

$$
\boxed{\delta^2 \mathcal{F}_0(\Gamma)[f, f] = \sigma \int_\Gamma \left( \vert \nabla_\Gamma f\vert ^2 - \lvert A \rvert^2 f^2 \right) d\mathcal{H}^{d-1},}
$$

where `∇_Γ` is the surface gradient (intrinsic gradient on `Γ`) and `|A|²` is the squared norm of the second fundamental form (sum of squared principal curvatures).

### §4.3 Jacobi operator definition

The *Jacobi operator* `J_Γ` is the negative of the symmetric bilinear form's defining operator:

$$
\boxed{J_\Gamma = -\Delta_\Gamma - \lvert A \rvert^2,}
$$

where `Δ_Γ` is the Laplace-Beltrami operator on `Γ`. Equivalently:

$$
\delta^2 \mathcal{F}_0(\Gamma)[f, f] = \sigma \int_\Gamma f \cdot J_\Gamma f \, d\mathcal{H}^{d-1}.
$$

**Standard references**: Simons 1968 (*Ann Math* **88**:62); Allard 1972 (*Ann Math* **95**:417, §8); Reilly 1977 (*Indiana Univ Math J* **26**:459); modern treatment Colding-Minicozzi 2011 (*A Course in Minimal Surfaces*, Ch. 1).

### §4.4 Spectral problem

The Morse-non-degenerate condition for `Γ` (in the constrained variational sense, normal variations `∫ f = 0`) is:

$$
J_\Gamma f = \mu f, \quad f \in C^\infty(\Gamma), \quad \int_\Gamma f \, d\mathcal{H}^{d-1} = 0 \quad \Longrightarrow \quad \mu \geq 0,
$$

with equality only on Goldstone (symmetry) modes (§5).

---

## §5 Jacobi Spectrum Analysis: Goldstone + Wobble Structure

### §5.1 Canonical model: sphere `Γ = S^{d−1}_R`

For sphere of radius `R` in `ℝ^d`:
- `Δ_Γ = Δ_{S^{d−1}_R} = (1/R²) · Δ_{S^{d−1}}` (Laplace-Beltrami, scaled).
- `|A|² = (d−1)/R²` (sum of `(d−1)` principal curvatures each `= 1/R`).
- Eigenvalues of `−Δ_{S^{d−1}}` on the unit sphere: `ℓ(ℓ + d − 2)` with eigenfunctions = spherical harmonics of degree `ℓ`.

Therefore Jacobi spectrum:

$$
\boxed{\mu_\ell = \frac{\ell(\ell + d - 2)}{R^2} - \frac{d-1}{R^2} = \frac{\ell(\ell + d - 2) - (d-1)}{R^2}.}
$$

### §5.2 Mode-by-mode interpretation

| Mode `ℓ` | Geometric role | Eigenvalue `μ_ℓ` | Spectral status |
|---|---|---|---|
| `ℓ = 0` | Uniform dilation (volume-changing) | `−(d−1)/R²` | *Negative* — but excluded by mass constraint `∫ f = 0` (volume preservation) |
| `ℓ = 1` | Translation (rigid `ℝ^d` motion of center) | `(1·(d−1) − (d−1))/R² = 0` | **Goldstone** = exact zero (translation invariance) |
| `ℓ = 2` | First wobble (quadrupole deformation) | `(2·d − (d−1))/R² = (d+1)/R²` | **Positive** — *Morse non-degenerate* |
| `ℓ ≥ 2` | Higher multipole wobble | `(ℓ(ℓ+d−2) − (d−1))/R²` | Positive (monotone increasing in `ℓ`) |

**Verification of `ℓ = 1` Goldstone**: `ℓ(ℓ+d−2) = 1·(d−1) = d−1`, so `μ_1 = (d−1)/R² − (d−1)/R² = 0` exactly ✓.

**Verification of `ℓ = 2` wobble positivity**:
- `d = 2` (circle in plane): `μ_2 = (2·2 − 1)/R² = 3/R² > 0` ✓.
- `d = 3` (sphere in space): `μ_2 = (2·3 − 2)/R² = 4/R² > 0` ✓.

### §5.3 Goldstone correspondence with SCC T-V5b-T-zero

```
CoT step 1: SCC canonical T-V5b-T-zero (Cat A definitional, CV-1.5.1, L1328): on translation-invariant graphs (T^d, C_n) under sub-spinodal c < c_spinodal, corner-saturated minimizers have Goldstone eigenvalue μ_Gold = 0 exactly, from Z_L^d translation orbit.
CoT step 2: Sharp-interface limit correspondence: on sphere Γ = S^{d-1}_R embedded in continuum analog of T^d, the ℓ=1 spherical harmonics (translation modes) give μ_1 = 0 — *exact match with T-V5b-T-zero*.
CoT step 3: Therefore: Modica-Mortola Jacobi spectrum on sphere reproduces T-V5b-T-zero (Cat A) in the continuum limit — *anchor compatibility verified*.

CoC anchors:
  - canonical: §13 T-V5b-T-zero (Cat A, μ_Gold = 0 exact)
  - external: standard spherical harmonics + Jacobi operator on sphere (Allard 1972, Reilly 1977)
inverse_causation_check:
  - if T-V5b-T-zero fails (graph admits no Z_L^d orbit): no continuum analog Goldstone — Jacobi spectrum may have non-zero μ_1
  - if sphere model replaced by non-spherical Γ: rotation Goldstone (if Γ has rotation symmetry) still zero; non-symmetric Γ has no Goldstone, all μ > 0
```

### §5.4 Rotation Goldstone (if applicable)

If `Γ` is a round sphere (full `SO(d)` symmetry), the `ℓ = 1` modes include *both* translation (`d` modes, `Δx_i` for each axis) and rotation modes are subsumed (rotation acts trivially on sphere center). Total Goldstone dimension = `d` (translation only; sphere is rotation-invariant about its center).

For non-spherical `Γ` (e.g., ellipsoid, dumbbell from K=2 splitting): rotation Goldstone activates if `Γ` has `SO(d)`-stabilizer subgroup; otherwise broken.

### §5.5 Degeneracy structure (T-σ-Lemma-1 compatibility)

```
CoT step 1: SCC canonical T-σ-Lemma-1 (Cat A, L1391): Hessian H(u*) commutes with G_u-action on 1^⊥; isotypic decomposition V_k = ⊕_[ρ] V_k^{[ρ]} per Maschke + Schur.
CoT step 2: Continuum analog: Jacobi operator J_Γ commutes with Isom(Γ)-action (isometries of Γ preserving the embedding). For sphere Γ = S^{d-1}_R: Isom(S^{d-1}_R) ⊇ O(d), spherical harmonics V_ℓ = irrep of O(d) of dimension (2ℓ+d-2)·(ℓ+d-3)!/(ℓ!(d-2)!).
CoT step 3: Therefore: Jacobi spectrum {μ_ℓ} has Isom(Γ)-isotypic structure paralleling SCC's G_u-isotypic structure — *T-σ-Lemma-1 has direct continuum analog* via Allard 1972 + Reilly 1977.

→ Cat A correspondence (canonical T-σ-Lemma-1 Cat A) verified at continuum limit.
```

---

## §6 L-MODICA-JACOBI-HMORSE Cat B Target Lemma (Full Statement)

### §6.1 Statement

**Lemma L-MODICA-JACOBI-HMORSE** *(Cat B target; W8-Day3 2026-05-20)*.

**Statement.** *Let `(X_t, L_G, W)` be a canonical SCC graph-energy system. Let `u^* ∈ Σ_m` be a non-uniform critical point of `E_bd|_{Σ_m}` satisfying D-HMORSE-LOCAL (C1)(C2′)(C3)(C4)(C5) (canonical L1934). Let `Γ = ∂Ω^*` be the formation boundary in the sharp-interface limit `ε = √(α/β) → 0`. Then under hypotheses H1–H3 below, the constrained Hessian `H(u^*)` of `E_bd` restricted to mass-preserving variations has spectrum that *converges* (as `ε → 0`, after appropriate rescaling) to the Jacobi-operator spectrum `Spec(J_Γ) = Spec(−Δ_Γ − |A|²)`. In particular, `u^*` is **H-Morse non-degenerate** (in the sense of L-HMORSE-LOCAL) with kernel equal to the geometric Goldstone modes (translation, rotation) of `Γ`, and the first non-Goldstone eigenvalue (wobble gap) is `≥ σ · μ_2(J_Γ)`, where `σ = c_W √(αβ)` is the Modica-Mortola surface tension.*

### §6.2 Hypotheses

- **H1** (Boundary regularity): formation `u^*` has well-defined sharp boundary `Γ = ∂{u^* ≈ 1}` in the sense of D-HMORSE-LOCAL (C1)(C2′) Cat A.
- **H2** (Smooth submanifold): `Γ` is a smooth `(d−1)`-dimensional embedded submanifold of the continuum domain `Ω ⊂ ℝ^d` (standard regularity assumption in geometric measure theory).
- **H3** (graph→continuum applicability): the discrete graph-energy `E_bd^{(G)}(u)` Γ-converges to the continuum perimeter functional `ℱ_0(u) = σ · ℋ^{d−1}(Γ)` under suitable mesh-refinement scaling (van Gennip-Bertozzi 2012; see §7 for explicit conditions).

### §6.3 5-Step Proof Sketch (Γ-convergence + Jacobi spectrum chain)

```
CoT step 1 — graph→continuum Γ-convergence (H3):
  E_bd^{(G)}(u) = α u^T L_G u + β Σ W(u_i)
  Mesh refinement: graph X_t → continuum domain Ω, with rescaling α = α₀/h², β = β₀ where h = mesh spacing (canonical T8-Core "Finite-element rescaling" remark, L1144).
  Under this rescaling, E_bd^{(G)} Γ-converges to E_ε(u) = ε∫|∇u|² + (1/ε)∫W(u) with ε ~ √(α/β) — van Gennip-Bertozzi 2012 Theorem 4.1 (graph TV → continuum TV).

CoT step 2 — Modica-Mortola sharp-interface limit (§2, ε → 0):
  E_ε → ℱ_0(u) = c_W · ℋ^{d-1}(∂{u=1}) = σ · ℋ^{d-1}(Γ)
  Modica 1987 + Sternberg 1988 (constrained Γ-convergence with mass).

CoT step 3 — second variation at Γ (§4):
  δ² ℱ_0(Γ)[f, f] = σ ∫_Γ (|∇_Γ f|² - |A|² f²) dℋ^{d-1}
  Standard area-functional second variation (Allard 1972, Simon 1968, Reilly 1977).

CoT step 4 — Jacobi operator spectrum (§5):
  J_Γ = -Δ_Γ - |A|² has spectrum classified by Isom(Γ)-isotypic decomposition (T-σ-Lemma-1 continuum analog).
  Sphere Γ = S^{d-1}_R: μ_0 = -(d-1)/R² (excluded by mass), μ_1 = 0 (translation Goldstone), μ_ℓ ≥ (d+1)/R² for ℓ ≥ 2 (positive wobble).

CoT step 5 — H-Morse certification:
  Goldstone kernel = translation modes (dimension d) + rotation modes (if Isom(Γ) admits)
  First wobble gap = σ · μ_2(J_Γ) > 0 strict
  → u^* is H-Morse non-degenerate in the L-HMORSE-LOCAL sense, with explicit gap formula.

→ Therefore L-MODICA-JACOBI-HMORSE holds Cat B (conditional on H1-H3). ∎ (sketch)
```

### §6.4 CoC anchored causation chain

```yaml
target: L-MODICA-JACOBI-HMORSE Cat B — SCC non-uniform critical u^* in sharp-interface limit has H-Morse spectral structure = Jacobi operator J_Γ spectrum.

prior_anchors:
  - canonical: §13 L-HMORSE-LOCAL (Cat B, CV-1.16) — D-HMORSE-LOCAL (C1)(C2′)(C3)(C4)(C5) conditional H-Morse
  - canonical: §13 L-HMORSE-DECOMP (Cat B conditional, CV-1.16) — Schur complement structure
  - canonical: §13 L-BOUNDARY-MODE-EXCLUSION (Cat C, CV-1.16) — boundary modes
  - canonical: §13 T-V5b-T-zero (Cat A, CV-1.5.1) — Goldstone exact zero translation-invariant
  - canonical: §13 T-σ-Lemma-1 (Cat A, CV-1.5) — Hessian–G_u commutation (continuum analog: J_Γ–Isom(Γ) commutation)
  - canonical: §13 T-OP6-B (Cat A, CV-1.7) — PersRidge boundary equivalence d_H ≤ 2√(α/β)
  - canonical: §13 OP-HMORSE-SADDLE (OPEN, theorem_status.md L594; cross-ref canonical.md L1967 caveat) — saddle-point regularity attack target
  - canonical: §3.5 (E_bd structure) + §3.7 + §9.3 (D operator role); §13 Theorem 4 (μ_k formula uniform critical)
  - external: Modica 1987 Arch Rat Mech Anal 98:123 (Cat A in PDE literature)
  - external: Sternberg 1988 Arch Rat Mech Anal 101:209 (Cat A constrained version)
  - external: Allard 1972 Ann Math 95:417 §8 (Cat A second-variation formula)
  - external: Simons 1968 Ann Math 88:62 (Cat A Jacobi operator minimal surfaces)
  - external: Reilly 1977 Indiana Univ Math J 26:459 (Cat A constrained Jacobi)
  - external: Colding-Minicozzi 2011 A Course in Minimal Surfaces Ch.1 (modern treatment)
  - external: van Gennip-Bertozzi 2012 SIAM J Imaging Sci 5:1115 (discrete graph Γ-convergence)
  - external: Chambolle-Giacomini-Lussardi 2014 (graph-based Modica-Mortola)
  - external: Rubinstein-Sternberg 1992 IMA J Appl Math 48:249 (Lagrange-multiplier-constrained AC class)

causation_chain:
  - H3 + graph→continuum scaling → E_bd^{(G)} Γ-converges to E_ε (intermediate I1)
  - I1 + Modica-Mortola (Modica 1987 + Sternberg 1988) → E_ε → σ · ℋ^{d-1}(Γ) as ε → 0 (intermediate I2)
  - I2 + Allard-Simons-Reilly second-variation → δ² ℱ_0(Γ)[f,f] = σ ∫_Γ (|∇_Γ f|² - |A|² f²) (intermediate I3)
  - I3 + Jacobi-operator spectrum analysis (sphere model + T-σ-Lemma-1 continuum analog) → Spec(J_Γ) has Goldstone-only kernel + positive wobble gap (intermediate I4)
  - I4 + L-HMORSE-LOCAL D-HMORSE-LOCAL (C1)(C2′) → u^* H-Morse non-degenerate with explicit wobble gap σ · μ_2(J_Γ) (target)

inverse_causation_check_per_step:
  - H1 fails: u^* has no sharp boundary → Γ ill-defined → Modica-Mortola Γ-limit undefined → entire chain breaks (correctly classified Cat B conditional)
  - H2 fails: Γ has corners/cusps (e.g., dumbbell pinch-point at K=2 split): Allard second-variation requires generalized treatment (Federer-Fleming varifold framework); standard Jacobi operator inadequate → require regularity proof OR weakened conclusion
  - H3 fails: graph→continuum Γ-convergence not applicable (e.g., graph too sparse, mesh refinement constraint violated): van Gennip-Bertozzi 2012 hypotheses must hold; otherwise Cat B reduces to Cat C
  - T-V5b-T-zero fails (no translation orbit): no Goldstone μ_1 = 0 — Jacobi spectrum has μ_1 > 0, but conclusion (H-Morse) STRENGTHENS (no kernel → strict H-Morse)
  - T-σ-Lemma-1 fails (G_u trivial): isotypic decomposition vacuous, spectrum analysis still holds (Schur trivially), conclusion unchanged
  - L-HMORSE-LOCAL (C2′) fails (active set ill-defined): no formation Γ → entire framework inapplicable; correctly classified inapplicable
  - Modica-Mortola removed: no σ surface-tension formula → Jacobi operator coefficient undetermined; entire chain breaks
```

### §6.5 Cat B classification justification

**Why Cat B, not Cat A**: graph→continuum step (H3) is the explicit conditional. *Modica-Mortola itself* is Cat A in PDE literature (Modica 1987 proves Γ-convergence rigorously). *Sphere Jacobi spectrum* is Cat A in differential geometry (Allard-Simons-Reilly). However, the *SCC-specific graph→continuum bridge* (van Gennip-Bertozzi 2012 Γ-convergence for discrete TV) requires:

1. Mesh refinement protocol (canonical T8-Core finite-element rescaling, L1144 — *recommendation*, not theorem);
2. SCC-specific α/β scaling compatibility with van Gennip-Bertozzi 2012 hypotheses;
3. Active-set (C2′) regime compatibility with continuum sharp-interface.

These are **non-trivial conditional steps**. Honest Cat B classification matches:
- canonical L-HMORSE-LOCAL (Cat B unconditional — i.e., under D-HMORSE-LOCAL); 
- canonical L-HMORSE-DECOMP (Cat B conditional);
- canonical T-OP6-B (originally Cat B, promoted Cat A only after H1-H5 closure W6-D4 Session K, CV-1.7).

**Cat B → Cat A path**: similar to T-OP6-B promotion, would require:
- (H3-PROOF): explicit graph→continuum Γ-convergence theorem for the *specific* SCC graph families (T^d torus, K_n complete, regular tree, 2D grid) — extending van Gennip-Bertozzi 2012;
- (H2-REG): smoothness of `Γ` proven from D-HMORSE-LOCAL (C1)(C2′) — regularity theorem for SCC formations;
- (H1-INHERIT): inherited from canonical D-HMORSE-LOCAL (C1)(C2′) Cat A (active-set form), no additional work.

Each is a substantive proof obligation, justifying Cat B status.

---

## §7 Discrete-Graph Corrections (van Gennip-Bertozzi 2012)

### §7.1 Discrete Allen-Cahn on graphs

**van Gennip & Bertozzi 2012** (*SIAM J. Imaging Sci.* **5**:1115). Theorem 4.1: for sequence of graphs `{G_n}` approximating continuum domain `Ω` with mesh size `h_n → 0`, the discrete graph TV functional Γ-converges (after rescaling) to the continuum TV functional:

$$
\mathrm{TV}_{G_n}(u) = \sum_{(i,j) \in E_n} w_{ij} \lvert u_i - u_j \rvert \quad \xrightarrow[n \to \infty]{\Gamma} \quad \mathrm{TV}_\Omega(u) = \int_\Omega \vert \nabla u\vert \, dx.
$$

For the **squared TV / Dirichlet form** (relevant to SCC `α u^T L_G u`):

$$
\sum_{(i,j) \in E_n} w_{ij} (u_i - u_j)^2 / h_n^{d-2} \quad \xrightarrow[n \to \infty]{\Gamma} \quad \int_\Omega \vert \nabla u\vert ^2\, dx,
$$

under suitable scaling (van Gennip-Bertozzi 2012 §5; Chambolle-Giacomini-Lussardi 2014, *Math Models Methods Appl Sci* **24**:847, full graph-based Modica-Mortola).

### §7.2 SCC compatibility conditions

For `E_bd^{(G)} → E_ε^{(Ω)}` Γ-convergence:

- **(GC1)** Graph sequence `{X_t^{(n)}}` is *quasi-uniform* (bounded degree variation): satisfied by regular graphs (T^d, K_n, regular trees, regular bulk grids) — canonical SCC examples.
- **(GC2)** Mesh refinement `h_n → 0` with finite-element rescaling `α = α₀ / h_n²` (canonical L1144 Remark) — ensures `λ_2(L_G) → λ_2^{cont}` Laplacian spectral convergence.
- **(GC3)** Double-well potential `W(u_i)` is *pointwise* (no graph coupling) — automatically satisfied by `W(u) = u²(1−u)²`.
- **(GC4)** `m / |Ω| ∈ (0,1)` non-degenerate mass density — interior of canonical spinodal `c ∈ ((3−√3)/6, (3+√3)/6)`.

Under (GC1)-(GC4), van Gennip-Bertozzi 2012 + Chambolle-Giacomini-Lussardi 2014 yield H3.

### §7.3 Failure modes (when graph→continuum breaks)

- **Random graphs (Erdős-Rényi)**: degree variation unbounded → (GC1) fails → continuum limit undefined (Garcia Trillos-Slepčev 2016 analyze separately).
- **Stochastic block models (SBM)**: structural heterogeneity → (GC1) may fail in transition region.
- **Finite-size effects (small n)**: `1/n` corrections to Modica-Mortola constant `c_W` — Cat B conditional becomes Cat C if `n` is not asymptotically large.

These failure modes are *legitimate Cat B → Cat C downgrades* under explicit hypotheses, matching the Cat B classification in §6.5.

---

## §8 Connection to Canonical Anchors

### §8.1 L-HMORSE-LOCAL (Cat B, CV-1.16)

L-MODICA-JACOBI-HMORSE *provides analytical foundation* for L-HMORSE-LOCAL:
- L-HMORSE-LOCAL gives `μ_min(Π_T H_E Π_T) > 0` under D-HMORSE-LOCAL conditions (numerical anchor 15/15 PASS).
- L-MODICA-JACOBI-HMORSE *explains why* `μ_min > 0`: the spectrum equals `σ · Spec(J_Γ)`, and `J_Γ`'s lowest non-Goldstone eigenvalue is `μ_2 = (d+1)/R² > 0` (sphere model).
- Explicit gap formula: `μ_min ≥ σ · μ_2(J_Γ) = (√2/6) √(αβ) · (d+1)/R²` for sphere-like formations.

### §8.2 L-HMORSE-DECOMP (Cat B conditional, CV-1.16)

L-HMORSE-DECOMP provides *Schur complement structure* `H_E = H_bd + H_cl + H_sep` with per-term bounds. L-MODICA-JACOBI-HMORSE addresses the `H_bd` part directly:
- `H_bd` contribution to Jacobi spectrum: `σ · J_Γ` (dominant in sharp-interface limit).
- `H_cl`, `H_sep` contribute *subleading corrections* via T-OP6-B's `δ_res` term (saturated minimizers: `|σ''(z)| → 0` reduces correction magnitude).

### §8.3 L-BOUNDARY-MODE-EXCLUSION (Cat C, CV-1.16)

L-BOUNDARY-MODE-EXCLUSION says minimum eigenvector does *not* concentrate on graph boundary `∂X`. Modica-Mortola Jacobi gives the *complement* statement:
- Minimum non-Goldstone eigenvector concentrates on *formation boundary* `Γ` (via `|A|²` curvature peak) — the geometric source of the wobble mode.
- These are *different boundaries*: `∂X` = graph boundary (finite-size effect), `Γ` = formation boundary (intrinsic to `u^*`).
- L-BOUNDARY-MODE-EXCLUSION removes graph-boundary artifact; L-MODICA-JACOBI-HMORSE identifies the *geometric source* of the surviving eigenmode (formation `Γ`).

### §8.4 T-V5b-T-zero (Cat A, CV-1.5.1)

T-V5b-T-zero (translation Goldstone exact zero on translation-invariant graphs) is the **discrete graph analog** of the `ℓ = 1` Jacobi mode on `Γ = S^{d−1}_R` (§5.2). Both:
- give `μ_Gold = 0` exactly (not approximate);
- arise from continuous symmetry (`Z_L^d` on graph; `ℝ^d` translation on continuum sphere);
- distinguish from non-Goldstone modes by symmetry irrep.

T-V5b-T-zero is the *graph-side Cat A anchor*; L-MODICA-JACOBI-HMORSE is the *continuum-side Cat B target* establishing the *full spectrum structure* beyond Goldstone alone.

### §8.5 T-σ-Lemma-1 (Cat A, CV-1.5)

T-σ-Lemma-1 (Hessian commutes with `G_u`-action via Maschke + Schur) has *direct continuum analog*: `J_Γ` commutes with `Isom(Γ)`-action (rotations of sphere, translations of plane, etc.). The continuum analog enables isotypic decomposition of Jacobi spectrum (sphere: irreps of `O(d)` = spherical harmonics).

### §8.6 T-OP6-B (Cat A, CV-1.7)

T-OP6-B gives `d_H(B_PR, ∂C) ≤ 2√(α/β) · |∂Ω|/n` — boundary band width = `√(α/β) = ℓ_bd` exactly matches Modica-Mortola scaling §3.3. This is *independent canonical anchor* for the scaling argument.

### §8.7 OP-HMORSE-SADDLE (OPEN; registration: theorem_status.md L594; cross-ref: canonical.md L1967 non-overclaim caveat — CORRECTED 2026-05-20 per Wave 2 critic Fix #2)

L-MODICA-JACOBI-HMORSE provides *attack framework* for OP-HMORSE-SADDLE — see §10.

---

## §9 Surface Tension Scaling (Combined with Rescaling)

Combining with `06_surface_tension_rescaling_cat_a.md` (forthcoming, Cat A direct via §7.5 Identity 5 of `01_ns_inspired_synthesis.md`):

```
CoT step 1: Rescaling (α, β) → (sα, sβ) gives σ = c_W √(αβ) → s · σ (linear in s).
CoT step 2: Modica-Mortola surface tension scales as s → Jacobi operator coefficient scales as s.
CoT step 3: Jacobi spectrum gap: μ_2(J_Γ) is geometric (depends only on Γ, not on α, β) → unchanged.
CoT step 4: Combined spectral gap of constrained Hessian:
  μ_min^{non-Goldstone} ≥ σ · μ_2(J_Γ) = s · (√2/6)√(αβ) · (d+1)/R²
→ Linear in rescaling parameter s; geometric (d, R) and graph (αβ) factors separate.
```

**Boxed scaling identity**:

$$
\boxed{\mu_{\min}^{\text{non-Goldstone}} \geq \frac{s\sqrt{2}}{6} \sqrt{\alpha\beta} \cdot \frac{d+1}{R^2}.}
$$

**Interpretation**:
- Increasing `s` (parameter rescaling) → linear increase in spectral gap. *Surface-tension rescaling Cat A path* (§8.1 of `01_ns_inspired_synthesis.md`).
- Increasing `R` (formation size) → spectral gap decreases as `1/R²`. *Large formations are softer* — consistent with DECL Q1 resolution-dependence (λ_2 vs scale).
- Increasing `d` (dimension) → gap increases linearly. *Higher-dimensional formations are stiffer*.

This combined formula provides the **quantitative Cat A bridge** from the canonical L-HMORSE-LOCAL (Cat B unconditional) to a *parameter-explicit Cat B target* (L-MODICA-JACOBI-HMORSE Cat B with explicit `s · √(αβ) · (d+1)/R²` lower bound).

---

## §10 OP-HMORSE-SADDLE Attack Framework

### §10.1 Canonical OP-HMORSE-SADDLE statement (registration: theorem_status.md L594; cross-ref: canonical.md L1967 caveat)

OP-HMORSE-SADDLE (OPEN; *registration*: theorem_status.md L594; *cross-ref*: canonical.md L1967 is a non-overclaim caveat within L-HMORSE-LOCAL body): *"Does NOT prove saddle-point Hessian regularity (OP-HMORSE-SADDLE, separate OP)."* (CORRECTED 2026-05-20 per Wave 2 critic Fix #2, file 12 §3 — canonical OP catalog lives in theorem_status.md; canonical.md L1967 is only a caveat.) — saddle-point Hessian spectrum analysis is **unaddressed** by L-HMORSE-LOCAL (Cat B), which covers only local minima.

### §10.2 Saddle Jacobi operator structure

At a *saddle point* `u^†` between two formations (K-jump transition state), the formation boundary `Γ^†` has the structure of a **min-max critical surface** of the perimeter functional. By Allard-Simons saddle analysis (Simons 1968 *Ann Math* **88**:62 — Bernstein theorem; Caffarelli-Hardt-Simon 1984):

```
CoT step 1: At u^† saddle, ℱ_0(u^†) = σ · ℋ^{d-1}(Γ^†) is a critical value (not minimum) of ℱ_0 restricted to mass-constrained admissible class.
CoT step 2: Second variation δ² ℱ_0(Γ^†)[f, f] = σ ∫_Γ (|∇_Γ f|² - |A|² f²) — same formula, but now indefinite quadratic form.
CoT step 3: Jacobi spectrum at saddle: Spec(J_Γ^†) has structure:
  - 1 negative eigenvalue: μ^- = -ν < 0 (unstable mode along K-jump direction, e.g., dumbbell pinch coordinate)
  - d Goldstone zero eigenvalues: μ_Gold = 0 (translation)
  - rest positive (wobble + higher modes)
CoT step 4: Saddle index = 1 (single unstable direction) — *Morse-saddle structure preserved*.
→ Therefore: OP-HMORSE-SADDLE attack via Modica-Mortola Jacobi gives the structural answer (saddle index = 1) Cat B conditional on graph→continuum.

CoC anchors:
  - canonical: OP-HMORSE-SADDLE (OPEN, theorem_status.md L594; cross-ref canonical.md L1967 caveat)
  - external: Simons 1968 Ann Math 88:62 (saddle Jacobi analysis)
  - external: Caffarelli-Hardt-Simon 1984 (minimal surface saddle structure)
  - W8-Day3 01_ns_inspired_synthesis.md §11 Tier 1 priority (OP-0005-DYN + OP-HMORSE-SADDLE)
inverse_causation_check:
  - if Γ^† has codim-2 singularity (e.g., catenoid neck collapse): standard Jacobi inadequate; require generalized varifold treatment
  - if K-jump direction not localized on Γ^† curvature peak: saddle index may exceed 1 (multiple unstable directions); refutable by direct numerical Hessian diagonalization at u^†
```

### §10.3 Attack channel (Cat B target → Cat A path)

OP-HMORSE-SADDLE Cat A path via this framework:

1. **Step 1** (Cat B target — established here): L-MODICA-JACOBI-HMORSE Cat B at saddle → Jacobi spectrum has 1 negative + Goldstone + positive wobble.
2. **Step 2** (Cat B → Cat A graph-side): explicit graph→continuum Γ-convergence on canonical SCC graph families (T^d, K_n, etc.) — extends van Gennip-Bertozzi 2012.
3. **Step 3** (Cat A): combine with L-HMORSE-LOCAL Cat B for stable minima → full saddle-minimum Morse structure → OP-HMORSE-SADDLE RESOLVED Cat A.

This is *strictly target framework*, not a resolution claim — *attack point named, not solved* (CN2 silent OP resolution).

---

## §11 CoT/CoC Archival (Mode-Level Summary)

### §11.1 CoT-CORE

```
CoT step 1: SCC non-uniform critical H-Morse problem (DECL Q1 boundary + Q5 temporal identity) requires *analytical reason* why kernel = Goldstone only and wobble = positive — beyond numerical 15/15 PASS of L-HMORSE-LOCAL.
CoT step 2: Modica-Mortola Γ-convergence (Modica 1987 + Sternberg 1988) provides the *sharp-interface limit* analytical bridge from discrete graph energy E_bd to continuum perimeter functional ℱ_0 = σ · ℋ^{d-1}(Γ).
CoT step 3: Second variation of ℱ_0 at Γ gives the Jacobi operator J_Γ = -Δ_Γ - |A|² (Allard 1972 + Simon 1968 + Reilly 1977).
CoT step 4: Jacobi spectrum on sphere model: μ_0 < 0 (excluded by mass), μ_1 = 0 (Goldstone — matches T-V5b-T-zero Cat A), μ_ℓ ≥ (d+1)/R² for ℓ ≥ 2 (positive wobble — matches L-HMORSE-LOCAL numerical anchor).
CoT step 5: Combined with surface-tension rescaling (s · σ scaling), spectral gap = s · (√2/6)·√(αβ)·(d+1)/R² — explicit parameter-dependent formula.
CoT step 6: Application to OP-HMORSE-SADDLE: saddle Jacobi has 1 negative + Goldstone + wobble → Morse saddle index = 1, structural attack channel.
CoT step 7: Cat B classification: graph→continuum step (van Gennip-Bertozzi 2012) is explicit conditional; Modica-Mortola itself is Cat A in PDE literature; SCC-specific application is Cat B target.
→ Therefore: L-MODICA-JACOBI-HMORSE Cat B target = analytical foundation for SCC non-uniform critical H-Morse, with explicit OP-HMORSE-SADDLE attack channel.
```

### §11.2 CoC anchored chain (mode-level)

```yaml
target: L-MODICA-JACOBI-HMORSE Cat B target lemma — SCC non-uniform critical u^* in sharp-interface limit has H-Morse spectral structure determined by Jacobi operator J_Γ on formation boundary Γ.

prior_anchors:
  canonical_Cat_A:
    - §13 T-V5b-T-zero (Cat A) — Goldstone exact zero, continuum analog μ_1 = 0
    - §13 T-σ-Lemma-1 (Cat A) — Hessian–G_u commutation, continuum analog J_Γ–Isom(Γ)
    - §13 T-OP6-B (Cat A) — d_H ≤ 2√(α/β), matches Modica-Mortola ℓ_bd scaling
    - §13 Theorem 4 (Cat A) — μ_k = 4αλ_k + βW''(c) uniform critical
    - canonical L1169 R11 "Standard Modica-Mortola for the leading term" (existing canonical reference)
  canonical_Cat_B:
    - §13 L-HMORSE-LOCAL (Cat B unconditional) — provides D-HMORSE-LOCAL conditions
    - §13 L-HMORSE-DECOMP (Cat B conditional) — Schur complement structure
  canonical_Cat_C:
    - §13 L-BOUNDARY-MODE-EXCLUSION (Cat C SKETCH) — graph boundary mode exclusion
  canonical_OPEN:
    - OP-HMORSE-SADDLE (theorem_status.md L594; cross-ref canonical.md L1967 caveat) — saddle-point Hessian regularity (attack target)
  external_Cat_A:
    - Modica 1987 Arch Rat Mech Anal 98:123 (Γ-convergence theorem)
    - Sternberg 1988 Arch Rat Mech Anal 101:209 (constrained Γ-convergence)
    - Allard 1972 Ann Math 95:417 (second variation formula)
    - Simons 1968 Ann Math 88:62 (Jacobi operator minimal surfaces, saddle structure)
    - Reilly 1977 Indiana Univ Math J 26:459 (constrained Jacobi)
    - Colding-Minicozzi 2011 (modern Jacobi treatment)
    - van Gennip-Bertozzi 2012 SIAM J Imaging Sci 5:1115 (discrete graph Γ-convergence)
    - Chambolle-Giacomini-Lussardi 2014 Math Models Methods Appl Sci 24:847 (graph-based Modica-Mortola)
    - Rubinstein-Sternberg 1992 IMA J Appl Math 48:249 (constrained AC class — SCC continuum analog class)

causation_chain:
  - H3 (graph→continuum, van Gennip-Bertozzi 2012) + (GC1)-(GC4) → E_bd^{(G)} Γ-converges to E_ε
  - Modica 1987 + Sternberg 1988 → E_ε → σ · ℋ^{d-1}(Γ) as ε → 0
  - Allard-Simons-Reilly second-variation → δ² ℱ_0(Γ) = σ ∫_Γ (|∇_Γ f|² - |A|² f²)
  - J_Γ = -Δ_Γ - |A|² spectrum analysis (sphere model + isotypic decomposition via T-σ-Lemma-1 continuum analog)
  - Goldstone-only kernel + positive wobble gap σ · μ_2(J_Γ)
  - L-HMORSE-LOCAL D-HMORSE-LOCAL (C1)(C2′) match
  → L-MODICA-JACOBI-HMORSE Cat B

inverse_causation_per_anchor:
  - Modica 1987 removed: no Γ-convergence theorem → ε-energy → perimeter limit unproven → cannot derive surface tension σ
  - Sternberg 1988 removed: constrained Γ-convergence undefined → mass-conservation incompatible → SCC application breaks
  - Allard 1972 removed: second-variation formula unavailable → Jacobi operator definition unclear → spectrum undefined
  - van Gennip-Bertozzi 2012 removed: discrete graph → continuum bridge unavailable → H3 conditional unjustified → Cat B downgrades to ad-hoc
  - T-V5b-T-zero Cat A failure: Goldstone exact zero on graphs unproven → continuum μ_1 = 0 lacks discrete anchor
  - T-σ-Lemma-1 Cat A failure: G_u-isotypic structure unavailable → spectrum classification ad-hoc
  - L-HMORSE-LOCAL D-HMORSE-LOCAL (C1)(C2′) failure: active set ill-defined → formation Γ undefined → entire framework inapplicable (correctly classified)
```

---

## §12 Hard Constraint CN1-16 Check

Per canonical CN1-16 + prompt strict constraints + CV-1.18 SEAL deprecation:

| Constraint | Status | Evidence |
|---|---|---|
| **CN1** canonical 직접 수정 0 | ✓ | working layer draft; canonical 미접근 (only read-only references to §3.5, §3.7, §9.3, §13, OMS, line 1169 R11 Modica-Mortola reference) |
| **CN2** Silent OP resolution 0 | ✓ | OP-HMORSE-SADDLE explicitly *attack channel named*, *not solved* (§10.3 explicit "attack point named, not solved"). Cat B target — *graph→continuum step is the conditional* (§6.5). |
| **CN3** Research OS 재도입 0 | ✓ | single working file in `THEORY/working/field_equation_framework/`, no new registry directory |
| **CN4 (analyticity, b_D=0)** | ✓ | NO new energy term; SCC `E_bd` 형식 미변경; b_D = 0 자동 (analytical chain unchanged). PH/combinatorial S(u) 미도입 (CSSL critic §D.3 anti-pattern). |
| **CN5 (4-term independence)** | ✓ | 본 문서 analyzes `E_bd` only; `E_cl`, `E_sep`, `E_tr` 별개 (§8.2 L-HMORSE-DECOMP Schur complement structure 별도 처리) |
| **CN6 Closure idempotence 가정 0** | ✓ | 미적용 |
| **CN7 K 이중 취급 0** | ✓ | K-vocabulary: K-jump (saddle direction) 의미로만 사용 (§10); K_field/K_act/K_soft 어휘 부재 |
| **Zero-temp metastability flag** | ✓ | T_* 어휘 부재 (this file = static spectral, not dynamical); metastability claim 0 |
| **OMC 풀 오케스트레이션 0** | ✓ | 호출 0 |
| **CN10 (no reductive reduction)** | ✓ | §1.2 explicit "SCC ≠ Allen-Cahn" + "SCC's continuum limit *belongs to* constrained-AC class (Rubinstein-Sternberg 1992)"; Modica-Mortola = *contrastive standard tool*; *no SCC = AC reduction*. CSSL §F.6 segmentation-drift anti-pattern explicitly avoided (Jacobi spectrum analysis only, no segmentation reformulation). |
| **Primitive u_t 전도 0** | ✓ | u_t primitive 유지; Γ = ∂{u^* ≈ 1} 는 *derived* surface (sharp-interface limit output), *not primitive*. |
| **Inertia 0** | ✓ | first-order Langevin only (§3 SCC SDE not modified); second-order temporal term 0 |
| **Mori-Zwanzig 0** | ✓ | CV-1.18 SEAL OP-0021 Routes A/B DEPRECATED preserved; memory kernel 0 |
| **CSSL energy terms (E_ridge / E_wild / E_pers) 0** | ✓ | critic-rejected 3 CRITICAL + 4 MAJOR; 본 문서 미사용; §1.2 explicit anti-pattern |
| **DECL-1.0 amend 0** | ✓ | DECL 미수정; Q1 (T8) + Q5 (시간 동일성) 직접 활용 only |
| **scc/ 수정 0** | ✓ | 본 문서 = doc-only |

**16/16 ✓ verified**.

---

## §13 One-Paragraph Summary

**Modica-Mortola Γ-convergence (Modica 1987 + Sternberg 1988 constrained version) gives sharp-interface limit `E_bd^{(G)} → σ·ℋ^{d-1}(Γ)` with surface tension `σ = c_W·√(αβ)`, `c_W = √2/6` for SCC double-well `W(u)=u²(1-u)²` and boundary width `ℓ_bd = √(α/β)` (independently anchored by canonical T-OP6-B Cat A `d_H ≤ 2√(α/β)`); second variation at formation boundary `Γ` gives the Jacobi operator `J_Γ = -Δ_Γ - |A|²` (Allard 1972 + Simons 1968 + Reilly 1977); spectrum on sphere `Γ = S^{d-1}_R` has `μ_0 < 0` (excluded by mass), `μ_1 = 0` (translation Goldstone — matches canonical T-V5b-T-zero Cat A on translation-invariant graphs), `μ_ℓ ≥ (d+1)/R²` for `ℓ ≥ 2` (positive wobble); combined with surface-tension rescaling `(α,β)→(sα,sβ)` (Cat A direct, `01_ns_inspired_synthesis.md` Identity 5), explicit non-Goldstone spectral gap `μ_min^{non-Goldstone} ≥ s·(√2/6)·√(αβ)·(d+1)/R²`; this provides *analytical foundation* for canonical L-HMORSE-LOCAL (Cat B unconditional) numerical 15/15 PASS and direct attack framework for canonical OP-HMORSE-SADDLE (OPEN, theorem_status.md L594; cross-ref canonical.md L1967 caveat) via saddle Jacobi operator structure (1 negative direction along K-jump + Goldstone + positive wobble = Morse index 1); honestly classified as **L-MODICA-JACOBI-HMORSE Cat B target** with explicit conditional on graph→continuum step (van Gennip-Bertozzi 2012 + Chambolle-Giacomini-Lussardi 2014 + (GC1)-(GC4) hypothesis package); Modica-Mortola itself is Cat A in PDE literature, sphere Jacobi spectrum is Cat A in differential geometry, but SCC-specific graph→continuum bridge requires (H3-PROOF) + (H2-REG) + (H1-INHERIT) — substantive Cat B → Cat A proof obligations parallel to T-OP6-B's promotion path (CV-1.7 Session K); strictly *contrastive analytical tool*, NOT *SCC = Allen-Cahn reduction* (today's 04 §6.3 corollary `L-PROJ-1 + L-PROJ-2` proves SCC ≠ Cahn-Hilliard at spectrum level; same logic gives SCC ≠ Allen-Cahn at full dynamics level — Modica-Mortola gives *only* the boundary-energy sharp-interface analytical scaffold, not a dynamics reduction); 16/16 hard-constraint CN1-16 verified (canonical 0 edits, CSSL energy terms 0, Mori-Zwanzig 0, inertia 0, primitive `u_t` preserved, CN10 contrastive-only enforced); CV-1.18 SEAL Non-Overclaim fully preserved.**

---

*W8-Day3 evening synthesis Tier 1 child file `03_modica_mortola_jacobi_cat_b.md` complete. → W9+ session entry input for OP-HMORSE-SADDLE attack + L-HMORSE-LOCAL Cat B→A path (with graph→continuum Γ-convergence proof obligation).*
