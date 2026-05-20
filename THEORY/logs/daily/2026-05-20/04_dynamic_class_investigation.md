---
type: log/daily/survey-light
date: 2026-05-20
mode: hybrid (survey-tertiary primary, deep-attack-secondary for §6 selective light derivation per user expansion)
session_label: W8-Day3 Priority 3 — SCC dynamic class investigation (outline + spectrum argument)
canonical_version: CV-1.18 (sealed 2026-05-19, untouched)
status: complete (outline + §6 selective derivation, W9+ staging maintained)
cot_enforced: yes
coc_enforced: yes
priority: 3
core_finding: "SCC ≠ Cahn-Hilliard at the algebraic spectrum level (L-PROJ-1 + L-PROJ-2 + corollary in §6). SCC's P_{TΣ_m} is rank-1 (removes only constant mode); CH's ∇² is mode-dependent (q² scaling). Therefore retraction #2 (z = 2.17 Model A wrong) does NOT promote to Model B (CH) either — SCC is in a *constrained Allen-Cahn (Rubinstein-Sternberg)* regime, or its own SCC-specific class. Universality class value (z) itself remains W9+ open."
---

> [!nav] Linked: [[00_plan|today's plan §B.3]] · [[01_pre_brainstorm|reference §3]] · [[02_cg_numerical_verification|Priority 1]] · [[03_D_L_commutation|Priority 2]] · [[../2026-05-19/99_summary|§POST-SEAL EXTENSION retractions #1-3]] · [[../../../canonical/canonical|CV-1.18 T-PF-A1-SDE]]

# 04 — SCC Dynamic Class Investigation (W8-Day3 Priority 3)

**Mode**: hybrid (survey-tertiary primary; deep-attack-secondary for §6 selective light derivation per user expansion)
**Target / mission**: outline + framework for the open question "What is the SCC dynamic universality class?" (raised by retraction #2: Model A z=2.17 wrong). Selective light derivation L-PROJ-1/L-PROJ-2/corollary establishes *spectrum-level* contrast (SCC P ≠ Cahn-Hilliard ∇²). Universality class value (z) itself remains W9+.

**Pre-work xref check** (§15.1):
- `grep -r "dynamic class\|Hohenberg-Halperin\|Model B\|Cahn-Hilliard" THEORY/canonical/ THEORY/working/` → 20 hits, mostly in superseded `fractal_dynamic_dim_v0.md` (retracted) + W8-Day2 evening report.
- Canonical hits: only 1 — `canonical.md L2737` Cugliandolo 2011 reference in OP-0021 Routes A/B deprecation context (CV-1.18 SEAL). Not the same topic.
- **Novel positioning**: 본 file 은 *first verification-day outline* for SCC dynamic class question; spectrum-level contrast (L-PROJ-1/L-PROJ-2) 은 *new algebraic content* (사용자 명시 expansion).
- §8a P1-P6: P1 (DECL Q3 직접 — stochastic dynamics) / P2 (u_t 본체 미변경, derived spectrum analysis) / P3 (canonical 1 hit unrelated, working hits in retracted archive — novel positioning OK) / P4 (canonical T-PF-A1-SDE 직접 후속) / P5 (4 audit dimension 명시) / P6 (수학 only). **0/6 부합 → 진행 합법**.

**Depends on reading**: 00_plan §B.3 + 01_pre_brainstorm §3 + canonical §13 T-PF-A1-SDE + W8-Day2 evening retraction #2
**CoT enforced for**: §1, §2, §3, §4, §5, §6
**CoC enforced for**: §1, §2, §3, §4, §5, §6
**W9+ staging note**: 본 file 의 *증명 시도 0* (outline + §6 spectrum argument only). Universality class value z 의 정확한 값 또는 class 명명 자체는 W9+ Priority 2 (v1 §5.2, 3-5 sessions).

---

## §1 SCC SDE Form (canonical T-PF-A1-SDE Cat A)

From canonical CV-1.9 (W6 D4 Session P, Cat A), the reflected Langevin SDE on $\Sigma_m$:

$$\boxed{dU_t = -\Pi_{T\Sigma_m} \nabla \mathcal{E}(U_t)\,dt + \sqrt{2T_*}\,\Pi_{T\Sigma_m}\,dB_t + dK_t}$$

Where:
- $\Pi_{T\Sigma_m} = I - (1/n)\mathbf{1}\mathbf{1}^T$: orthogonal projector onto the *mean-zero subspace* (tangent space to the simplex $\Sigma_m$)
- $B_t$: standard Brownian motion on $\mathbb{R}^n$
- $K_t$: Skorokhod reflection at the boundary $\partial \Sigma_m$ (faces $\{u_i = 0\}, \{u_i = 1\}$)
- $T_*$: effective temperature (open per OP-0021, route C ξ resident accepted CV-1.18)

**Conservation law**: $\sum_i U_t^{(i)} = m$ for all $t$ (mass-conserved). This is **GLOBAL** conservation (one constraint), NOT **LOCAL** flux conservation.

**CoT step 1**: P_T_Sigma_m removes one degree of freedom (constant mode). The remaining $n-1$ degrees evolve under projected gradient flow + projected noise.

---

## §2 Hohenberg-Halperin Classification (Hohenberg & Halperin 1977, RMP 49:435)

Standard taxonomy:

| Model | Order parameter | Conservation | Equation | Dynamic exponent (2D Ising) |
|---|---|---|---|---|
| **A** | Non-conserved scalar | None | $\partial_t \phi = -\delta H/\delta \phi + \eta$ | $z \approx 2.17$ |
| **B** | Conserved scalar | LOCAL flux: $\int_V \phi$ conserved for ANY $V$ | $\partial_t \phi = +\nabla^2(\delta H/\delta \phi) - \nabla \cdot \boldsymbol{\xi}$ | $z = 4 - \eta \approx 3.75$ |
| C, D, E, ..., J | Multi-field coupled | Various | Various | Various |

**Critical structural feature distinguishing A from B**: presence of the *outer Laplacian* $\nabla^2$ in the deterministic part of B's evolution — this $\nabla^2$ is what enforces LOCAL flux conservation (current $J = -\nabla(\delta H/\delta\phi)$ has zero divergence on average).

---

## §3 SCC vs Cahn-Hilliard — at the level of *structure*

### §3.1 Conservation Comparison

| Property | SCC | Cahn-Hilliard (Model B) |
|---|---|---|
| Order parameter | $U_t : X_t \to [0,1]$ (graph-valued) | $\phi : \mathbb{R}^d \to \mathbb{R}$ (continuum scalar) |
| Conserved quantity | $\sum_i U_t^{(i)} = m$ (GLOBAL only) | $\int_V \phi$ for any $V$ (LOCAL flux) |
| Enforcement | Projector $\Pi_{T\Sigma_m}$ | Outer Laplacian $\nabla^2$ |
| Operator type | Rank-1 projector (constant-mode-removal) | Differential operator (mode-dependent) |

### §3.2 The Question

The W8-Day2 evening retraction #2 noted: "With mass conservation via P, SCC is actually Model B, NOT Model A. z = 4-η ≈ 3.75 (Model B 2D Ising), NOT z = 2.17 (Model A)."

**But**: this re-classification assumes $\Pi_{T\Sigma_m}$ plays the role of $\nabla^2$. Is that justified? §6 below shows **NO** — the operators are structurally different at the spectrum level.

---

## §4 Constrained Allen-Cahn (Rubinstein-Sternberg 1992) as the actual analogue

The closer continuum analogue to SCC is **constrained Allen-Cahn**:

$$\partial_t \phi = -\frac{\delta H}{\delta \phi} + \mu(t), \quad \mu(t) = \frac{1}{|D|}\int_D \frac{\delta H}{\delta \phi}\,d^d x$$

where $\mu(t)$ is a *Lagrange multiplier* enforcing global conservation $\int_D \phi = $ const. (Rubinstein & Sternberg 1992, *IMA J. Appl. Math.* 48:249.)

This is exactly what SCC's $\Pi_{T\Sigma_m} = I - (1/n)\mathbf{1}\mathbf{1}^T$ does: subtract the spatial mean. The continuum limit of the SCC projector IS the Lagrange-multiplier subtraction in Rubinstein-Sternberg.

**Coarsening prediction (Bray 1994, Adv. Phys. 43:357)**: for constrained Allen-Cahn:
- Early time (AC-like, motion by mean curvature): $L(t) \sim (\alpha t/\beta)^{1/2}$
- Late time (LSW-like, mass redistribution): $L(t) \sim t^{1/3}$
- Crossover: $t_\times \sim \alpha/\beta$ (Bray §3-4 explicit; correcting W8-Day2 retraction #3 "$t_\times \sim (\beta/\alpha)^{3/2}$")

---

## §5 References (≥3 external + canonical anchors)

External:
1. **Hohenberg, P. C. & Halperin, B. I.** (1977) "Theory of dynamic critical phenomena", *Rev. Mod. Phys.* **49**:435-479 — Model A/B classification (Table I)
2. **Rubinstein, J. & Sternberg, P.** (1992) "Nonlocal reaction-diffusion equations and nucleation", *IMA J. Appl. Math.* **48**:249-264 — Lagrange-multiplier-constrained Allen-Cahn
3. **Bray, A. J.** (1994) "Theory of phase ordering kinetics", *Adv. Phys.* **43**:357-459 — coarsening exponents + crossover (§3-4 explicit derivation of $t_\times \sim \alpha/\beta$)
4. **Allen, S. M. & Cahn, J. W.** (1979) "A microscopic theory for antiphase boundary motion", *Acta Metall.* **27**:1085-1095 — Allen-Cahn primary source
5. **Lifshitz, I. M. & Slyozov, V. V.** (1961) "The kinetics of precipitation from supersaturated solid solutions", *J. Phys. Chem. Solids* **19**:35-50 — LSW late-time

Canonical anchors:
- canonical §13 T-PF-A1-SDE (Cat A, CV-1.9) — reflected Langevin SDE
- canonical §13 T-PF-A1-GI (Cat A, CV-1.9) — Gibbs invariant measure
- canonical §13 T-PF-A1-PE (Cat A, CV-1.9) — Poincaré ergodicity
- canonical §13 T-P-F-ε0-K (Cat B, CV-1.7) — Kramers exponent stability (conditional on H5)
- W8-Day2 evening §POST-SEAL retractions #1 (EW wrong), #2 (Model A/B wrong), #3 ($t_\times$ wrong)

---

## §6 NEW — Spectrum-level proof that SCC ≠ Cahn-Hilliard (Sub-task 3.5, 사용자 명시 expansion)

### §6.1 Lemma L-PROJ-1: SCC's $\Pi_{T\Sigma_m}$ is a rank-1 projector

**Lemma L-PROJ-1**. The SCC tangent-space projector
$$\Pi_{T\Sigma_m} = I - \frac{1}{n}\mathbf{1}\mathbf{1}^T \quad \in \mathbb{R}^{n \times n}$$
is an *orthogonal projector* with spectrum
$$\sigma(\Pi_{T\Sigma_m}) = \{0 \text{ (mult 1)},\; 1 \text{ (mult } n-1\text{)}\}.$$

**Proof (CoT)**:
```
CoT step 1: Π is symmetric (manifestly).
CoT step 2: Π² = Π:
  - Π² = (I - (1/n)11^T)(I - (1/n)11^T)
       = I - (2/n)11^T + (1/n²)11^T 11^T
       = I - (2/n)11^T + (1/n²) · n · 11^T   [since 1^T 1 = n]
       = I - (2/n)11^T + (1/n)11^T
       = I - (1/n)11^T = Π  ✓
CoT step 3: Eigenvalues. Π is a symmetric idempotent, so eigenvalues ∈ {0, 1}.
  - Π · 1 = 1 - (1/n)1(1^T 1) = 1 - 1 = 0 → 1 is in 0-eigenspace
  - For any v ∈ 1^⊥ (i.e., 1^T v = 0): Π v = v - (1/n)1(1^T v) = v - 0 = v → 1-eigenspace
  - dim(0-eigenspace) = 1 (the constant direction); dim(1-eigenspace) = n - 1
→ Therefore spectrum {0 (mult 1), 1 (mult n-1)}. ∎

CoC anchors:
  - canonical §13 T-PF-A1-AR (Cat A, CV-1.8) — Π defined as orthogonal projector onto T_{u} Σ_m
  - external: linear algebra (orthogonal projector = symmetric idempotent → spectrum ⊆ {0,1})
Causation chain:
  - Π defined as I - (1/n)11^T (T-PF-A1-AR) → Π² = Π (computational check)
  - Π² = Π + Π symmetric → Π orthogonal projector
  - Projector spectrum ⊆ {0, 1}; rank-1 column space (span{1}) → 1 zero-eigenvalue + (n-1) unit-eigenvalues
inverse_causation_check:
  - if Π replaced by D^{-1}A or similar non-projector → spectrum continuous in [-1, 1]
  - if mass conservation removed (no Σ u_i = m constraint) → no need for Π at all
```

**Numerical verification** (n=16): `np.linalg.eigvalsh(I - (1/16) ones((16,16)))` returns `[3.3e-16, 1.0, 1.0, ..., 1.0]`. ✓

### §6.2 Lemma L-PROJ-2: Cahn-Hilliard's $\nabla^2$ is mode-dependent (continuous spectrum)

**Lemma L-PROJ-2**. The continuum Laplacian $\nabla^2$ on the torus $\mathbb{T}^d = (\mathbb{R}/L\mathbb{Z})^d$ has spectrum
$$\sigma(\nabla^2) = \{-|q|^2 : q \in (2\pi/L) \mathbb{Z}^d\},$$
which (for $d \geq 1$) is a *countably infinite, mode-dependent* spectrum. On the discrete $L \times L$ torus (Cahn-Hilliard regularized), the spectrum is
$$\sigma(\nabla^2_\text{discrete}) = \{-4\sin^2(\pi j/L) - 4\sin^2(\pi k/L) : (j,k) \in \mathbb{Z}/L \times \mathbb{Z}/L\}.$$

**Proof (CoT)**:
```
CoT step 1: Continuum: ∇² acts on plane waves e^{iq·x} as eigenvalue -|q|².
  - q ∈ Fourier-dual lattice (2π/L)Z^d for periodic BC.
  - Eigenvalues are -|q|² for each q.
CoT step 2: Discrete: Laplacian L_d (with our sign convention L = D - A) on torus L×L:
  - Eigenvalues = 4 sin²(πj/L) + 4 sin²(πk/L) (positive convention)
  - For Cahn-Hilliard ∂_t φ = ∇²(δH/δφ), use -L_d (matching continuum sign).
CoT step 3: Number of distinct eigenvalues for 1D torus L=16: 9 (in [0, 4]). Spectrum is genuinely *mode-dependent* — each eigenvalue is a smooth function of mode index.

CoC anchors:
  - external: standard Fourier analysis on torus (Reed-Simon I §IV.5)
  - external: discrete Laplacian spectrum on cyclic graph C_n (Spielman 2007 spectral graph theory)
Causation chain:
  - ∇² translation-invariant + periodic BC → diagonalized by Fourier modes
  - Each mode q gets eigenvalue -|q|² (q² for our positive convention)
  - Therefore spectrum has at least L distinct values (in 1D) or ~L²/4 (in 2D), grows with L
inverse_causation_check:
  - if ∇² replaced by rank-1 projector → loses mode dependence; degenerate spectrum {0, 1}
  - if torus replaced by ball with Dirichlet BC → Bessel function eigenvalues, still mode-dependent
```

**Numerical verification** (n=16, 1D torus): 9 distinct eigenvalues in [0, 4]. ✓

### §6.3 Corollary: SCC dynamics ≠ Cahn-Hilliard dynamics at the spectrum level

**Corollary**. The deterministic linear part of SCC's reflected Langevin (linearized at uniform critical $u^* = c\mathbf{1}$):
$$-\Pi_{T\Sigma_m} \mathrm{Hess}(\mathcal{E})(u^*) \cdot v$$
has spectrum that differs *fundamentally* from the deterministic linear part of Cahn-Hilliard:
$$\nabla^2 \mathrm{Hess}(H)(\phi^*) \cdot v.$$

**Specifically**:
- SCC's outer operator $\Pi$ has spectrum $\{0, 1\}$ (binary)
- CH's outer operator $\nabla^2$ has spectrum $\{-q^2 : q \in 2\pi\mathbb{Z}/L\}$ (continuous range)

**Implication for universality class**: any mapping "SCC = Model B" requires the OUTER conservation operator to match. The outer operators do NOT match (binary vs continuous spectrum). Therefore:

> **SCC is NOT in the standard Cahn-Hilliard / Model B universality class.**

This refutes the W8-Day2 evening retraction-#2 *promotion* "Model A → Model B" — Model B is also wrong, just like Model A. SCC requires its own analysis, likely as a **constrained Allen-Cahn (Rubinstein-Sternberg 1992)** with Lagrange-multiplier conservation, possibly with its own SCC-specific dynamic exponent or a Model-A-like exponent with corrections.

**Proof of Corollary (CoT + CoC)**:
```
CoT step 1: SCC linear operator at u* = c·1: M_SCC = -Π · Hess(E)(u*) = -Π · (4α L_G + β W''(c) I + λ_cl H_cl + λ_sep H_sep)
  - Π is rank-1 projector (L-PROJ-1)
  - The factor -Π in front DOES NOT depend on the mode being acted on (it just kills the constant component)
  - Therefore: after Π, the operator restricted to 1^⊥ is just -Hess(E)(u*)|_{1^⊥}, which has the SAME spectrum as for *unconstrained* Allen-Cahn (modulo the kernel direction)

CoT step 2: CH linear operator at φ* = c: M_CH = +∇² · Hess(H)(φ*) = ∇² · (κ ∇² + W''(c)) ≈ -κ q^4 + |W''(c)| q² for each mode q (in Fourier)
  - Here ∇² appears TWICE: once inside Hess(H) (κ ∇² gradient term), once outside (the conservation enforcer)
  - The OUTER ∇² penalizes high-q modes MORE → "rough" modes evolve faster
  - Dispersion ω(q) = q² (κ q² - |W''|) — quartic at high q, parabolic at long-wave

CoT step 3: Comparing spectra:
  - SCC eigenvalues on 1^⊥: -(4α λ_k(L_G) + β W''(c)) — same scaling as Allen-Cahn
  - CH eigenvalues on 1^⊥: q² (κ q² - |W''(c)|) — q²-enhanced relative to AC
  - For long-wave modes (small q or low λ_k): SCC ~ |W''(c)|, CH ~ -q²|W''(c)| (slow)
  - For short-wave modes (large q or high λ_k): SCC ~ 4α λ_k (linear in λ_k), CH ~ κ q^4 (quartic in q)
  - These have FUNDAMENTALLY different scaling — SCC linear in spectral mode, CH quartic.

→ Therefore SCC ≠ Model B at the linearized dispersion relation level. ∎

CoC anchors:
  - L-PROJ-1 (rank-1 projector spectrum) + L-PROJ-2 (mode-dependent spectrum)
  - canonical T-PF-A1-SDE (SCC SDE form)
  - Hohenberg-Halperin 1977 §II.B (Model B equation)
Causation chain:
  - L-PROJ-1: Π spectrum binary → SCC outer operator does not amplify high-q modes
  - L-PROJ-2: ∇² spectrum continuous → CH outer operator strongly amplifies high-q modes
  - Combined: linearized SCC vs CH have different dispersion at high q (linear vs quartic)
  - Therefore: SCC dynamic class ≠ CH (Model B) universality class
inverse_causation_check:
  - if Π replaced by ∇² → SCC becomes Model B exactly (trivially)
  - if H_sep dispersion happens to match CH at long-wave (small q): late-time coarsening could still cross over to LSW
  - The early-time short-wave dynamics differ structurally
```

### §6.4 What SCC IS (open W9+ question)

**Most likely**: SCC is in the universality class of **non-local constrained Allen-Cahn** (Rubinstein-Sternberg 1992 + Bray 1994 §3-4), with:
- Early time: Allen-Cahn-like, motion by mean curvature, $L(t) \sim (\alpha t / \beta)^{1/2}$
- Late time: LSW-like mass redistribution, $L(t) \sim t^{1/3}$, effective dynamic exponent $z = 3$
- Crossover: $t_\times \sim \alpha/\beta$ (Bray 1994 §3-4 explicit)

**Possible alternative**: SCC-specific class with novel exponent from the *self-referential* dependence of E on $u$ via closure $E_{cl}$ + separation $E_{sep}$ (canonical CN7 dual-mode self-referentiality). This requires a *full RG analysis* — W9+ deep-attack scope.

**What is NOT acceptable** (per anti-goals):
- ❌ "SCC = Model B z = 3.75" (Corollary above refutes)
- ❌ "SCC = Model A z = 2.17" (W8-Day2 retraction #2)
- ❌ "SCC = EW z = 2" (W8-Day2 retraction #1)

---

## §7 W9+ Staging Note

**Outline value**: 본 file 의 *primary deliverable* = (a) §6 lemmas L-PROJ-1/L-PROJ-2/corollary establishing *SCC ≠ Model B* spectrum-level, (b) §4 constrained Allen-Cahn (Rubinstein-Sternberg) framing as the *likeliest correct analogue*, (c) §7.1 below 의 *W9+ session entry input map*.

### §7.1 W9+ Session Entry Map

| W9+ session | Direct input |
|---|---|
| W9+ S1 (1 session): Verify Bray 1994 §3-4 $t_\times \sim \alpha/\beta$ on SCC numerically | This file §4 + Bray §3-4 reference |
| W9+ S2 (2-3 sessions): Compute SCC linearized dispersion ω(λ_k) explicitly + compare with Model A | This file §6 corollary CoT step 3 |
| W9+ S3 (3-5 sessions): RG analysis of self-referential closure loop | v1 §5.2 + canonical CN7 + retraction #6 (closure RG-irrelevance unproved) |
| W9+ S4 (long-term): SCC-specific universality class candidates + experimental crossover detection | This file §6.4 + W8-Day2 retraction #2 |

### §7.2 New Open Question Candidates (per §G.1 #2 — explicit registration, not silent)

| NQ ID candidate | Statement |
|---|---|
| NQ-DYN-1 | What is the precise dynamic exponent z of SCC in the bulk regime (away from Σ_T8)? Model A z=2.17 ruled out; Model B z=3.75 ruled out (this file). Candidates: constrained AC (z=3 LSW-like) or SCC-specific. |
| NQ-DYN-2 | Does the closure $E_{cl}$ self-referential loop generate a marginal operator at 1-loop RG? (retraction #6 still open) |
| NQ-DYN-3 | What is the SCC-specific crossover time $t_\times$ in terms of $(\alpha, \beta, \lambda_{cl}, \lambda_{sep}, n, T_*)$? Bray $t_\times \sim \alpha/\beta$ is for *pure* constrained AC; full SCC adds H_cl + H_sep contributions. |

---

## §8 CoC archival (key anchored chains)

```yaml
target_statement_SCC_neq_ModelB: SCC dynamics is NOT in the Cahn-Hilliard (Model B) universality class at the linearized dispersion level.
prior_anchors:
  - canonical: §13 T-PF-A1-SDE (Cat A, CV-1.9) — SCC SDE form with Π_T_Σ_m
  - canonical: §13 T-PF-A1-AR (Cat A, CV-1.8) — Π definition
  - L-PROJ-1 (§6.1) — Π rank-1 projector, binary spectrum
  - L-PROJ-2 (§6.2) — CH ∇² mode-dependent spectrum
  - external: Hohenberg-Halperin 1977 Model B equation (∂_t φ = ∇²(δH/δφ) + ...)
causation_chain:
  - SCC SDE has outer Π (binary spectrum)
  - CH SDE has outer ∇² (continuous q² spectrum)
  - Linearized at uniform critical, dispersion relations differ structurally (SCC linear in λ_k, CH quartic in q)
  - Therefore SCC ≠ Model B
inverse_causation_check:
  - if SCC SDE replaced with CH SDE → trivially Model B
  - if linearization regime changed (e.g., near Σ_T8 Goldstone modes) → universality may differ from bulk
  - if discrete graph effects ignored → continuum limit may smooth the distinction

target_statement_constrained_AC_likely: SCC dynamic class likely corresponds to constrained Allen-Cahn (Rubinstein-Sternberg 1992) rather than Cahn-Hilliard.
prior_anchors:
  - external: Rubinstein-Sternberg 1992 (Lagrange-multiplier-constrained AC)
  - external: Bray 1994 §3-4 (coarsening + $t_\times \sim \alpha/\beta$)
  - canonical: §13 T-PF-A1-SDE (SCC Π acts as Lagrange-multiplier subtraction)
causation_chain:
  - SCC Π_T_Σ_m = I - (1/n)11^T literally implements "subtract spatial mean" — same as Lagrange multiplier in Rubinstein-Sternberg
  - This match is structural (operator-level) not just dimensional
  - Therefore: continuum limit of SCC dynamics ⊂ Rubinstein-Sternberg class
inverse_causation_check:
  - if SCC graph is bounded (finite n): exact match holds for all n
  - if continuum limit involves new effects (renormalization of α, β, ...): may add corrections
```

---

## §9 Hard constraint check (§G.1 모든 10 항목)

| Constraint | Status | Evidence |
|---|---|---|
| canonical 0 edits | ✓ | daily log; canonical untouched |
| Silent OP resolution | ✓ | NQ-DYN-1/2/3 explicitly registered as candidates (§7.2), not silently resolved |
| Research OS 재도입 | ✓ | daily log format |
| Reductive 환원 | ✓ | Hohenberg-Halperin / Rubinstein-Sternberg / Bray = *contrastive* references (§3.2 explicitly refutes Model B mapping); not "SCC = constrained AC", but "SCC's continuum limit *likely belongs to* constrained AC class" |
| Primitive 전도 | ✓ | u_t primitive maintained; Π and ∇² are derived operators |
| 4 에너지 항 병합 | ✓ | E_cl, E_sep, E_bd, E_tr treated separately |
| Closure idempotence | ✓ | 미적용 |
| K 이중 취급 | ✓ | K-어휘 부재 |
| Zero-temp metastability flag | ✓ | T_* appears (canonical T-PF-A1-SDE); no kinetic metastability claim — "dynamic exponent" is *static-equilibrium-near-critical* concept, not metastable basin escape |
| OMC 풀 오케스트레이션 | ✓ | 호출 0 |

---

## §10 결과 요약 (one-paragraph)

**SCC dynamic class question: outline + spectrum-level contrast (사용자 명시 expansion 의 selective light derivation) 완료. Lemma L-PROJ-1 (SCC Π_T_Σ_m rank-1 projector with binary spectrum {0, 1}) + Lemma L-PROJ-2 (Cahn-Hilliard ∇² mode-dependent continuous spectrum) + Corollary (SCC ≠ Model B at linearized dispersion level) — *spectrum 분리 의 algebraic fact* 등록. W8-Day2 evening retraction #2 의 "Model A → Model B" 의 *Model B 측도 wrong*; SCC 는 likely **constrained Allen-Cahn (Rubinstein-Sternberg 1992)** class with possible SCC-specific corrections. *Universality class 의 정확한 값* (z exponent) 및 *class 의 정확한 명명* 은 W9+ Priority 2 (3-5 sessions, NQ-DYN-1/2/3 후보 등록). 외부 ref ≥5건 (Hohenberg-Halperin / Rubinstein-Sternberg / Bray / Allen-Cahn / LSW). canonical 0 edits / 새 어휘 0 / 8 retractions 재시도 0.**

---

*Priority 3 outline + selective light derivation complete. 04 file 작성 종료. → 99_summary EOD 진입.*
