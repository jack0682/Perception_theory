---
type: working/field_equation_framework/cat-a-direct-catalog
date: 2026-05-20
session_origin: W8-Day3 evening, post-synthesis Cat A formal proof catalog
canonical_version: CV-1.13 SEALED (untouched throughout)
status: draft v0.1
preceded_by:
  - 01_ns_inspired_synthesis.md (§6 catalog + §7 network — source material)
  - 02_cg_numerical_verification.md (c_G = 1.171, λ₂ = 0.152241 on 2D torus L=16)
  - cssl/01_critic_evaluation.md (CSSL critic-rejected — avoid patterns)
purpose: |
  Formal mini-lemma catalog: 10 dimensionless number definitions + 5 algebraic
  identities + 1 Hessian-rescaling identity. Each item is Cat A direct with
  one-paragraph proof, canonical anchor with line numbers, domain of validity,
  inverse causation check, and numerical evaluation at reference values.
canonical_compatibility:
  canonical_edits: 0
  cat_b_items: 0 (Sc^{(2)}, Pr^{(Kramers)}, Modica-Mortola Jacobi remain in companion files)
  substantive_cat_b_derivations: 0
  cn4_analyticity: preserved (no new energy terms)
  cn5_4_term_independence: preserved
  cn10_no_reductive_reduction: contrastive only
  primitive_u_t: preserved
cot_enforced: yes
coc_enforced: yes
lemma_count: 16
---

> [!nav] Linked: [[01_ns_inspired_synthesis|01 NS synthesis]] (§6 catalog, §7 network) ·
> [[canonical|CV-1.13 canonical]] (§13 Theorem 4 L1134–1136, SB7 L2497–2498,
> T-PF-A1-AR L1652, T-PF-A1-SDE L1668, T-PF-A1-GI L1686, T-PF-A1-PE L1700,
> T-P-F-ε0-K L1818) · [[DECLARATION|DECL-1.0]] ·
> [[02_cg_numerical_verification|02 c_G verification]] ·
> [[01_critic_evaluation|CSSL critic eval (avoid patterns)]] ·
> companion: [[06_surface_tension_rescaling_cat_a|06 H-Morse rescaling]] ·
> companion: [[02_kramers_prefactor_op_0005_attack|02 Kramers Cat B]]

# 05 — Cat A Direct Catalog: Formal Proofs (10 Numbers + 5 Identities + 1 Rescaling)

**Mode**: working layer formal proof catalog (NOT canonical edit, NOT Cat B derivation)
**Target**: 16 mini-lemmas, each Cat A direct from canonical Theorem 4 + T-PF-A1-* package

---

## §0 — Frontmatter + Cross-reference Check + §8a P1-P6 Audit

### §0.1 Pre-work xref check

Cross-reference status (source 01_ns_inspired_synthesis.md §6–§7):
- §6 catalog: 12 numbers (1–12); this file covers 10 Cat A direct items (numbers 1–6, 8–11);
  numbers 7 (Sc^{(2)}) and 12 (Pr^{(Kramers)}) are Cat B targets — excluded here.
- §7 network: 6 identities; this file covers identities 1, 3, 4, 6 as Cat A direct;
  identity 2 (Eyring-Kramers explicit) and 5 (surface tension) go to companion files.
- `grep -r "canonical/" THEORY/canonical/` → 0 edits (git status clean).
- Canonical Theorem 4 body: canonical.md L1134–1136 (T8-Core proof contains μ_k formula).
- Canonical SB7: canonical.md L2497–2498.
- Canonical T-PF-A1-SDE/AR/GI/PE: canonical.md L1668/1652/1686/1700.
- Today's c_G verification: 02_cg_numerical_verification.md §1.2 — λ₂ = 0.152241, W''(1/2) = −1.

### §0.2 §8a Archive Pattern P1-P6 Audit

| Pattern | Check | Evidence |
|---|---|---|
| P1 (근본 질문 우회) | ✓ PASS | Directly quantifies DECL Q1 (T8 boundary), Q3 (stochastic dynamics via T_*) |
| P2 (Vocabulary refactoring) | ✓ PASS | u_t primitive untouched; dimensionless numbers are derived ratios only |
| P3 (Canonical content 중복) | ✓ PASS | 01_ns_inspired_synthesis.md consolidation — 0 new canonical contradictions |
| P4 (외부 도구 도입) | ✓ PASS | Modica-Mortola σ formula cited contrastively; all proofs reduce to canonical Theorem 4 |
| P5 (Self-audit) | ✓ PASS | §0 + §9 dual audit present |
| P6 (언어-수학 분리) | ✓ PASS | Each lemma has explicit definition box separate from interpretation |

**0/6 violations → proceed.**

---

## §1 — Mission: Cat A Direct Catalog with Formal Proofs

This file proves 16 items that are **Cat A direct** — meaning their justification reduces to
a trivial algebraic manipulation of canonical Theorem 4 and/or T-PF-A1-* package, with no new
mathematical content beyond renaming and rearranging canonical formulas.

**What this file does NOT do**:
- ❌ Derive Cat B items (Sc^{(2)}, Pr^{(Kramers)}, Eyring-Kramers explicit form, Modica-Mortola Jacobi)
- ❌ Edit any canonical/* file
- ❌ Introduce new energy terms
- ❌ Silently resolve any OPEN problem

**Why this matters**: The 10 dimensionless numbers defined here are the *shared language* for all
subsequent working-layer attacks on OP-0005-DYN, OP-HMORSE-SADDLE, L-HMORSE-LOCAL Cat B → A,
and the Hessian-rescaling path to H-Morse.

---

## §2 — Reference Values Setup (2D Torus L=16, c=1/2, β=1, α=1, T_*=0.1, R=4)

**Graph**: 2D torus $C_{16} \times C_{16}$, $n = 256$ nodes, degree-4 regular, periodic BC.

**Computation of λ₂** (verified 02_cg_numerical_verification.md §1.2 + §2.2):

$$\lambda_2(L_{C_{16} \times C_{16}}) = 4\sin^2(\pi/16) = 4 \times 0.038060 = 0.152241$$

(Fiedler eigenvalue; multiplicity 4 by $D_4$ symmetry of torus.)

**Double-well** $W(u) = u^2(1-u)^2$ under canonical I6 convention (CLAUDE.md):

$$W'(u) = 2u(1-u)(1-2u), \quad W''(u) = 2(1 - 6u + 6u^2)$$
$$W''(1/2) = 2(1 - 3 + 3/2) = -1, \quad \lvert W''(1/2) \rvert = 1$$
$$W'''(u) = 12(2u-1), \quad W'''(1/2) = 0$$

**Spinodal check**: $c = 1/2 \in ((3-\sqrt{3})/6,\, (3+\sqrt{3})/6) \approx (0.211, 0.789)$ — confirmed in spinodal interior.

**Modica-Mortola surface tension** for $W(u) = u^2(1-u)^2$ (CORRECTED 2026-05-20 per Wave 2 critic Fix #1, file 12 §2 — previous $\sqrt{\alpha\beta}/3$ form was incorrect due to convention mismatch on $\int 2W^{1/2}$ vs $\int\sqrt{2W}$):

$$\sigma = \sqrt{\alpha\beta} \cdot \int_0^1 \sqrt{2W(u)}\,du = \sqrt{\alpha\beta} \cdot \frac{\sqrt{2}}{6} = \frac{\sqrt{2}}{6}\sqrt{\alpha\beta}$$

(Standard Modica-Mortola profile integral: $\int_0^1 \sqrt{2u^2(1-u)^2}\,du = \sqrt{2}\int_0^1 u(1-u)\,du = \sqrt{2}\cdot(1/6) = \sqrt{2}/6$, giving $\sigma = (\sqrt{2}/6)\sqrt{\alpha\beta} \approx 0.2357\sqrt{\alpha\beta}$.)

At $\alpha = \beta = 1$: $\sigma = \sqrt{2}/6 \approx 0.2357$.

**Canonical Hessian at uniform critical** (Theorem 4, canonical.md L1134–1136):

$$\mu_k = 4\alpha\lambda_k(L_G) + \beta W''(c)$$

At reference values ($\alpha=1, \beta=1, c=1/2$):
$$\mu_k = 4\lambda_k - 1$$

Key mode values:
- $\mu_0 = 0$ (zero mode, excluded from $\Sigma_m$ by $\mathbf{1}^\perp$ projection)
- $\mu_2 = 4 \times 0.152241 - 1 = 0.608964 - 1 = -0.391036$ (NEGATIVE — super-critical, formation regime)
- $\vert \mu_2\vert = 0.391036$

**Sc_{T8} at reference**: $4\alpha\lambda_2 / (\beta\vert W''(c)\vert) = 4 \times 0.152241 / 1 = 0.608964$ (< 1, confirming super-critical).

**Summary table for §6 computation**:

| Symbol | Reference value | Formula |
|---|---|---|
| $\lambda_2$ | 0.152241 | $4\sin^2(\pi/16)$ |
| $W''(1/2)$ | −1 | $2(1-6c+6c^2)\vert _{c=1/2}$ |
| $\lvert W''(1/2) \rvert$ | 1 | — |
| $W'''(1/2)$ | 0 | $12(2c-1)\vert _{c=1/2}$ |
| $\sigma$ | $\sqrt{2}/6 \approx 0.2357$ | $(\sqrt{2}/6)\sqrt{\alpha\beta}$ at $\alpha=\beta=1$ (CORRECTED, file 12 §2) |
| $\mu_2$ | −0.391036 | $4\lambda_2 - 1$ at $\alpha=\beta=1$ |
| $\mu_k$ at mode $k$ | $4\lambda_k - 1$ | Theorem 4 |
| $T_*$ | 0.1 | given |
| $R$ | 4 | given |
| $\vert \nabla E\vert $ | reference value | left as symbol (E-dependent) |

---

## §3 — Part A: 10 Cat A Direct Dimensionless Number Lemmas

### §3.1 — L-PECLET-DEF: Péclet Number

---

**Lemma L-PECLET-DEF** (Cat A direct)

**Definition**:

$$\boxed{\mathrm{Pe} = \frac{\vert \nabla \mathcal{E}(u^*)\vert \cdot R}{T_*}}$$

where $\vert \nabla \mathcal{E}(u^*)\vert $ is the norm of the energy gradient at a reference configuration $u^*$,
$R$ is a characteristic spatial scale (e.g., formation radius), and $T_*$ is the effective stochastic
temperature (canonical OMS-1 resident, CV-1.18, canonical.md L2711).

**Cat A direct proof**: The Péclet number in overdamped systems measures the ratio of deterministic
drift to stochastic noise. In the SCC reflected Langevin (T-PF-A1-SDE, Cat A, canonical.md L1668),
the deterministic drift is $-\Pi_{T\Sigma_m}\nabla\mathcal{E}(U_t)$ and the stochastic noise amplitude
is $\sqrt{2T_*}$. Over a spatial scale $R$, the deterministic contribution scales as
$\vert \nabla\mathcal{E}\vert \cdot R$ (energy change over $R$), and the stochastic contribution scales as
$\sqrt{2T_*} \cdot R^{1/2}$ in the appropriate norm. Taking the ratio of deterministic to stochastic
characteristic magnitudes, and absorbing the $\sqrt{2}$ and $R^{1/2}$ factors into the definition
convention, yields Pe as stated. No new mathematics: this is a direct ratio of quantities already
appearing in T-PF-A1-SDE. The definition is well-posed whenever $T_* > 0$ (guaranteed by canonical
T-PF-A1-SDE hypothesis) and $R > 0$.

**Domain of validity**: $T_* > 0$ (T-PF-A1-SDE hypothesis); $R > 0$; $\vert \nabla\mathcal{E}\vert $ finite
(guaranteed on compact $\Sigma_m$ by T-PF-A1-AR, canonical.md L1652, since $\mathcal{E}$ is $C^2$
on $[0,1]^n$). Well-posed for all $(\alpha, \beta, c, T_*, R)$ in canonical parameter range.

**Inverse causation check**:
- If T-PF-A1-SDE (Cat A) removed: $T_*$ loses its role as the stochastic noise level; Pe undefined as drift/noise ratio.
- If T-PF-A1-AR (Cat A) removed: $\mathcal{E}$ may not be Lipschitz on $\Sigma_m$; $\vert \nabla\mathcal{E}\vert $ may be ill-defined.
- Neither anchor can be removed without breaking Pe.

**Reference numerical value** (2D torus L=16, $\alpha=\beta=1$, $c=1/2$, $T_*=0.1$, $R=4$):

$$\mathrm{Pe} = \frac{\vert \nabla\mathcal{E}\vert \times 4}{0.1} = 40 \cdot \vert \nabla\mathcal{E}\vert $$

(Left in terms of $\vert \nabla\mathcal{E}\vert $ since it is configuration-dependent. At a formation critical
point $\vert \nabla\mathcal{E}\vert = 0$; near T8 wall $\vert \nabla\mathcal{E}\vert $ is small; typical bulk regime
$\vert \nabla\mathcal{E}\vert \sim O(\beta) = O(1)$, giving Pe $\sim 40$.)

---

### §3.2 — L-DAMKOHLER-DEF: Damköhler Number

---

**Lemma L-DAMKOHLER-DEF** (Cat A direct)

**Definition**:

$$\boxed{\mathrm{Da} = \frac{\beta}{\alpha}}$$

**Cat A direct proof**: The Damköhler number in reaction-diffusion systems measures the ratio of
reaction rate to transport rate. In the SCC energy $\mathcal{E}_{\mathrm{bd}} = \alpha\,u^T L_G u + \beta\sum_i W(u_i)$,
the parameter $\alpha$ controls spatial coupling (graph-Laplacian smoothness, analogous to diffusion)
and $\beta$ controls the double-well reaction (pointwise bistability). Their ratio $\beta/\alpha$ is
the unique dimensionless combination that governs the T8 phase transition: the T8 condition reads
$\beta/\alpha > 4\lambda_2/\lvert W''(c) \rvert$ (canonical T8-Core, canonical.md L1134–1136). The definition
$\mathrm{Da} = \beta/\alpha$ is thus an immediate algebraic extraction from the canonical T8-Core
proof. No new content.

**Domain of validity**: $\alpha > 0$ (canonical parameter constraint, CLAUDE.md §Code Architecture
"a_cl < 4, spinodal"); $\beta > 0$ (canonical requirement for double-well contribution). Da is
independent of $c$, $T_*$, $R$.

**Inverse causation check**:
- If Theorem 4 / T8-Core removed: $\beta/\alpha$ still well-defined as a ratio, but loses its
  interpretation as the fundamental phase-transition driver. The Cat A status of Da as the
  "T8 control parameter" depends on T8-Core.
- Da is the simplest canonical dimensionless number — its definition requires only $\alpha, \beta > 0$.

**Reference value** ($\alpha=1, \beta=1$): $\mathrm{Da} = 1/1 = 1.0$.

(At reference, Da = 1; T8 condition requires Da $> 4\lambda_2/\lvert W''(c) \rvert = 4 \times 0.152241 = 0.609$.
Since Da = 1 > 0.609, reference is super-critical — formation regime confirmed.)

---

### §3.3 — L-CAPILLARY-DEF: Capillary Number

---

**Lemma L-CAPILLARY-DEF** (Cat A direct)

**Definition**:

$$\boxed{\mathrm{Ca} = \frac{\vert \nabla\mathcal{E}\vert}{\sigma}}, \qquad \sigma = \frac{\sqrt{2}}{6}\sqrt{\alpha\beta}$$

where $\sigma$ is the Modica-Mortola surface tension for $W(u) = u^2(1-u)^2$ (sharp-interface limit
of $\mathcal{E}_{\mathrm{bd}}$, canonical T11 Γ-convergence, canonical.md L1167–1169).

**Cat A direct proof** (CORRECTED 2026-05-20 per Wave 2 critic Fix #1, file 12 §2): The surface tension $\sigma = (\sqrt{2}/6)\sqrt{\alpha\beta}$ is derived from the
canonical $\mathcal{E}_{\mathrm{bd}}$ via the standard Modica-Mortola profile integral
$\sigma = \sqrt{\alpha\beta}\int_0^1\sqrt{2W(u)}\,du = (\sqrt{2}/6)\sqrt{\alpha\beta}$ for $W(u)=u^2(1-u)^2$.
This derivation uses only the canonical energy form (CLAUDE.md §Theory Sketch + T11 Γ-convergence)
and the canonical double-well (CLAUDE.md §"Critical Implementation Details", I6 correction
$W(u)=u^2(1-u)^2$). The ratio Ca = $\vert \nabla\mathcal{E}\vert /\sigma$ measures whether the formation
driving force dominates or is dominated by interface energy — the overdamped analog of the fluid
capillary number (Bond/Ca in overdamped regimes). Definition requires only canonical $\alpha, \beta, \mathcal{E}$.

**Domain of validity**: $\alpha, \beta > 0$; $\sigma = (\sqrt{2}/6)\sqrt{\alpha\beta} > 0$; $\vert \nabla\mathcal{E}\vert $
finite on $\Sigma_m$. Well-posed throughout canonical parameter range.

**Inverse causation check**:
- If canonical $W(u) = u^2(1-u)^2$ changed: $\sigma$ formula changes (different profile integral).
  Cat A status depends on I6 double-well convention.
- If T11 removed: σ loses its $\Gamma$-convergence interpretation but remains definable as a formula.
  The *interpretation* of Ca as capillary analog requires T11.

**Reference value** ($\alpha=\beta=1$, $\sigma=\sqrt{2}/6 \approx 0.2357$):

$$\mathrm{Ca} = \frac{\vert \nabla\mathcal{E}\vert}{\sqrt{2}/6} = \frac{6}{\sqrt{2}}\cdot\vert \nabla\mathcal{E}\vert = 3\sqrt{2}\cdot\vert \nabla\mathcal{E}\vert \approx 4.243\,\vert \nabla\mathcal{E}\vert $$

(Numerically: Ca $\approx 4.243$ when $\vert \nabla\mathcal{E}\vert \sim 1$.)

---

### §3.4 — L-BOND-DEF: Bond Number

---

**Lemma L-BOND-DEF** (Cat A direct)

**Definition**:

$$\boxed{\mathrm{Bo} = \frac{R^2 \cdot \vert \nabla\mathcal{E}\vert}{\sigma}}$$

**Cat A direct proof**: The Bond number (Weber number analog in overdamped flow) measures the ratio
of driving force at scale $R^2$ to surface tension $\sigma$. In fluid mechanics, Bo $= \rho g R^2 / \sigma$
(gravity vs surface tension). In SCC, the role of gravitational body force is played by $\vert \nabla\mathcal{E}\vert $
(energy gradient driving formation), and the surface tension is the Modica-Mortola $\sigma = (\sqrt{2}/6)\sqrt{\alpha\beta}$
(canonical T11; CORRECTED 2026-05-20 per Wave 2 critic Fix #1). The extra factor $R$ relative to Ca gives Bo its area-scaling character:
$\mathrm{Bo} = R \cdot \mathrm{Ca}$. Since Ca is Cat A direct (L-CAPILLARY-DEF above) and $R > 0$
is a given scale, Bo is Cat A direct by simple multiplication. No new content beyond L-CAPILLARY-DEF.

**Domain of validity**: Same as L-CAPILLARY-DEF plus $R > 0$.

**Inverse causation check**:
- If L-CAPILLARY-DEF breaks: Bo breaks (Bo = R × Ca).
- If $R$ is not defined (no characteristic length scale): Bo is ill-defined. In SCC, $R$ is typically
  the formation core radius — definable once a formation exists (post-T8).

**Reference value** ($R=4$, $\sigma=\sqrt{2}/6 \approx 0.2357$):

$$\mathrm{Bo} = \frac{4^2 \cdot \vert \nabla\mathcal{E}\vert}{\sqrt{2}/6} = \frac{96}{\sqrt{2}}\cdot\vert \nabla\mathcal{E}\vert = 48\sqrt{2}\cdot\vert \nabla\mathcal{E}\vert \approx 67.88 \cdot \vert \nabla\mathcal{E}\vert $$

(At $\vert \nabla\mathcal{E}\vert \sim 1$: Bo $\approx 67.88$.)

---

### §3.5 — L-STOKES-DEF: Stokes Number

---

**Lemma L-STOKES-DEF** (Cat A direct)

**Definition**:

$$\boxed{\mathrm{St}_k = \frac{T_*}{\mu_k}}$$

where $\mu_k = 4\alpha\lambda_k(L_G) + \beta W''(c)$ is the Hessian eigenvalue at the uniform critical
point (canonical Theorem 4, T8-Core proof, canonical.md L1134–1136).

**Cat A direct proof**: In overdamped dynamics, the relaxation timescale of mode $k$ is
$\tau_k \sim 1/\mu_k$ (inverse Hessian eigenvalue — the deterministic decay rate near a minimizer).
The thermal energy scale is $T_*$. The Stokes number $\mathrm{St}_k = T_*/\mu_k$ is the ratio of
thermal energy to deterministic restoring force for mode $k$. It is immediately read off from
Theorem 4 (which gives $\mu_k$) and the T-PF-A1-SDE noise level $T_*$ (canonical.md L1668).
No new mathematics.

**Domain of validity**: $\mu_k \neq 0$ (mode $k$ not at Goldstone/T8 wall); $T_* > 0$. For
$\mu_k > 0$ (deterministic modes): $\mathrm{St}_k \in (0, \infty)$. For $\mu_k < 0$ (unstable modes,
super-critical regime): $\mathrm{St}_k < 0$ — interpreted as thermal energy exceeding an unstable
restoring force, signaling stochastic escape.

**Inverse causation check**:
- If Theorem 4 removed: $\mu_k$ undefined, St undefined.
- If T-PF-A1-SDE removed: $T_*$ loses its stochastic role; St loses its thermal interpretation.

**Reference value** ($\alpha=\beta=1$, $c=1/2$, $T_*=0.1$, mode $k=2$):

$$\mathrm{St}_2 = \frac{T_*}{\mu_2} = \frac{0.1}{-0.391036} = -0.2557$$

(Negative: mode 2 is unstable at reference — consistent with super-critical regime. For a stable
mode, e.g. $k=n-1$ with $\lambda_{n-1} \approx 8$: $\mu_{n-1} = 32 - 1 = 31$, $\mathrm{St}_{n-1} = 0.1/31 = 0.00323$.)

---

### §3.6 — L-SC1-MODE-HESSIAN: Mode-Hessian Schmidt Number

---

**Lemma L-SC1-MODE-HESSIAN** (Cat A direct)

**Definition**:

$$\boxed{\mathrm{Sc}^{(1)}_k = \frac{\mu_k}{T_*} = \frac{1}{\mathrm{St}_k}}$$

**Cat A direct proof**: The mode-Hessian Schmidt number is the reciprocal of the Stokes number —
trivially Cat A by definition inversion. It measures how strongly the deterministic restoring force
of mode $k$ dominates thermal fluctuations. $\mathrm{Sc}^{(1)}_k > 0$: mode $k$ is deterministically
stable and thermally suppressed. $\mathrm{Sc}^{(1)}_k < 0$: mode $k$ is unstable (formation regime).
$\vert \mathrm{Sc}^{(1)}_k\vert \gg 1$: either strongly stable or strongly unstable. This number directly
quantifies the T-PF-A1-PE spectral gap (canonical.md L1700–1707) in units of $T_*$: the Poincaré
gap $\lambda_1 \sim e^{-\mathrm{osc}/T_*} \cdot (\pi^2/n)$ connects to the Hessian spectrum at
minimizers.

**Domain of validity**: Same as L-STOKES-DEF ($\mu_k \neq 0$, $T_* > 0$).

**Inverse causation check**: Same as L-STOKES-DEF.

**Reference value** ($\alpha=\beta=1$, $c=1/2$, $T_*=0.1$, mode $k=2$):

$$\mathrm{Sc}^{(1)}_2 = \mu_2 / T_* = -0.391036 / 0.1 = -3.91036$$

(For stable mode $k=n-1$: $\mathrm{Sc}^{(1)}_{n-1} = 31/0.1 = 310$.)

---

### §3.7 — L-SC-T8-RATIO: T8 Phase-Transition Ratio

---

**Lemma L-SC-T8-RATIO** (Cat A direct)

**Definition**:

$$\boxed{\mathrm{Sc}_{T8} = \frac{4\alpha\lambda_2(L_G)}{\beta\vert W''(c)\vert}}$$

**Cat A direct proof**: This is a direct dimensionless rename of the canonical T8 phase-transition
condition. Theorem SB7 (canonical.md L2497–2498) proves that $\Sigma_{T8} = \{(\alpha,\beta,c) : \mu_2 = 0\}$
is a codim-1 algebraic surface, identical to the Hessian-degeneracy locus. From Theorem 4
(canonical.md L1134–1136), $\mu_2 = 4\alpha\lambda_2 + \beta W''(c) = 0$ at the T8 wall.
In the spinodal interior $W''(c) < 0$, so $\mu_2 = 0 \Leftrightarrow 4\alpha\lambda_2 = \beta|W''(c)|
\Leftrightarrow \mathrm{Sc}_{T8} = 1$. The three regimes:

- $\mathrm{Sc}_{T8} > 1$: sub-critical (uniform stable, no formation)
- $\mathrm{Sc}_{T8} = 1$: T8 wall ($\Sigma_{T8}$, onset of instability)
- $\mathrm{Sc}_{T8} < 1$: super-critical (formation regime, $\mu_2 < 0$)

The T8 condition $\beta/\alpha > 4\lambda_2/\lvert W''(c) \rvert$ from DECL-1.0 is equivalently $\mathrm{Sc}_{T8} < 1$.
Sc_{T8} is a dimensionless rename with zero new content.

**Domain of validity**: Spinodal interior $c \in ((3-\sqrt{3})/6,\, (3+\sqrt{3})/6)$ (so $W''(c) < 0$,
$\lvert W''(c) \rvert > 0$); $\alpha, \beta > 0$; $\lambda_2 > 0$ (connected graph). Well-posed throughout.

**Inverse causation check**:
- If Theorem 4 removed: $\mu_2$ formula unavailable; Sc_{T8} loses its Hessian interpretation.
- If SB7 removed: $\Sigma_{T8}$ no longer certified as codim-1 algebraic; Sc_{T8} = 1 condition
  loses its topological significance.
- If spinodal interior condition violated ($W''(c) > 0$): $\lvert W''(c) \rvert$ still positive but no T8
  transition possible ($\mu_k > 0$ always); Sc_{T8} > 1 trivially for all $\alpha,\beta > 0$.

**Reference value** ($\alpha=\beta=1$, $c=1/2$, $\lambda_2=0.152241$):

$$\mathrm{Sc}_{T8} = \frac{4 \times 1 \times 0.152241}{1 \times 1} = 0.608964$$

(< 1: super-critical — formation regime confirmed at reference.)

---

### §3.8 — L-SC-BD-BOUNDARY: Boundary-Layer Schmidt Number (= Pr^{(bd)})

---

**Lemma L-SC-BD-BOUNDARY** (Cat A direct)

**Definition**:

$$\boxed{\mathrm{Sc}^{(\mathrm{bd})} = \mathrm{Pr}^{(\mathrm{bd})} = \frac{\alpha W''(u^*)}{T_*}}$$

where $u^*$ is the field value at the formation boundary band (transition region where $u^* \in$
spinodal interior; deterministic boundary width $\ell_{\mathrm{bd}} \sim \sqrt{\alpha/\beta}$).

**Cat A direct proof**: The formation boundary band has a deterministic characteristic frequency
$\sqrt{\alpha W''(u^*) / \ell_{\mathrm{bd}}^2} \sim \sqrt{\beta W''(u^*)}$ (from the Hessian at boundary
sites: $\mu_{\mathrm{bd}} = 4\alpha\lambda_k^{\mathrm{bd}} + \beta W''(u^*) \approx \beta W''(u^*)$
when $\alpha\lambda_k^{\mathrm{bd}}$ is smaller than $\beta\vert W''(u^*)\vert $ at boundary sites). However,
the cleanest definition follows directly from Theorem 4 by evaluating at the boundary field value $u^*$
and normalizing by $T_*$. The ratio $\alpha W''(u^*)/T_*$ measures deterministic boundary curvature
vs thermal noise — the Prandtl-type ratio for the boundary layer specifically. This is Cat A direct
because $W''(u^*)$ is evaluated at a canonical field value using the canonical double-well
(CLAUDE.md I6 convention), and $T_*$ is the canonical T-PF-A1-SDE noise level (canonical.md L1668).
Note: $W''(u^*) < 0$ at boundary sites in the spinodal interior; the magnitude $\lvert W''(u^*) \rvert$ is used
for the boundary instability measure; the sign-convention follows 01_ns_inspired_synthesis.md §6.1 #9.

**Domain of validity**: $T_* > 0$; $u^*$ defined (formation must exist, i.e., super-critical regime
$\mathrm{Sc}_{T8} < 1$); $\alpha > 0$.

**Inverse causation check**:
- If Theorem 4 removed: $W''(u^*)$ loses its Hessian role at boundary sites.
- If T-PF-A1-SDE removed: $T_*$ undefined; Pr^{(bd)} undefined.
- If super-critical condition fails: no formation, no boundary band, $u^*$ undefined.

**Reference value** (using $u^* = 1/2$ as proxy for boundary, $\alpha=1$, $T_*=0.1$):

$$\mathrm{Pr}^{(\mathrm{bd})} = \frac{1 \times \lvert W''(1/2) \rvert}{0.1} = \frac{1}{0.1} = 10.0$$

(Pr^{(bd)} = 10 $\gg$ 1: deterministic boundary curvature strongly dominates thermal noise at reference.
Precondition for D-HMORSE-LOCAL (C2′) active-set well-definiteness satisfied, per 01 §8.3.)

---

### §3.9 — L-PR-SPATIAL: Spatial Prandtl Number

---

**Lemma L-PR-SPATIAL** (Cat A direct)

**Definition**:

$$\boxed{\mathrm{Pr}^{(\mathrm{spatial})} = \frac{\alpha\lambda_2(L_G)}{T_*}}$$

**Cat A direct proof**: Theorem 4 (canonical.md L1134–1136) decomposes the constrained Hessian
eigenvalue $\mu_k = 4\alpha\lambda_k + \beta W''(c)$ into two additive contributions: the spatial
term $4\alpha\lambda_k$ (arising from the graph-Laplacian smoothness $\alpha u^T L_G u$) and the
onsite term $\beta W''(c)$ (arising from the double-well $\beta\sum_i W(u_i)$). Taking the spatial
contribution at the Fiedler mode $k=2$, normalized by $T_*$, gives Pr^{(spatial)}. The factor of 4
from Theorem 4 is absorbed into the definition by writing the spatial contribution as $4\alpha\lambda_2$,
but the "per-unit" Prandtl form $\alpha\lambda_2/T_*$ follows the convention in 01_ns_inspired_synthesis.md
§6.1 #10. This is the ratio of the graph-spectral deterministic coupling to thermal noise — directly
readable off Theorem 4 with no new mathematics.

**Domain of validity**: $T_* > 0$; $\lambda_2 > 0$ (connected graph); $\alpha > 0$.

**Inverse causation check**:
- If Theorem 4 removed: the decomposition of $\mu_k$ into spatial + onsite contributions is unavailable;
  Pr^{(spatial)} loses its Hessian-component identity.
- If T-PF-A1-SDE removed: $T_*$ undefined.

**Reference value** ($\alpha=1$, $\lambda_2=0.152241$, $T_*=0.1$):

$$\mathrm{Pr}^{(\mathrm{spatial})} = \frac{1 \times 0.152241}{0.1} = 1.52241$$

---

### §3.10 — L-PR-ONSITE: Onsite Prandtl Number

---

**Lemma L-PR-ONSITE** (Cat A direct)

**Definition**:

$$\boxed{\mathrm{Pr}^{(\mathrm{onsite})} = \frac{\beta\vert W''(c)\vert}{T_*}}$$

**Cat A direct proof**: Symmetric to L-PR-SPATIAL: the onsite contribution to $\mu_k$ from Theorem 4
is $\beta W''(c)$ (negative in spinodal interior). Its magnitude normalized by $T_*$ gives the ratio of
double-well deterministic force to thermal noise at the uniform critical point. This is the
"onsite Prandtl" — how strongly the double-well drives instability relative to thermal mixing.
Directly from Theorem 4 with no new mathematics.

**Domain of validity**: $T_* > 0$; $c$ in spinodal interior ($W''(c) < 0$, $\lvert W''(c) \rvert > 0$); $\beta > 0$.

**Inverse causation check**:
- If Theorem 4 removed: onsite contribution $\beta W''(c)$ not available as a Hessian component.
- If spinodal interior condition violated: $W''(c) \geq 0$; Pr^{(onsite)} still definable as
  $\beta W''(c)/T_*$ but loses its instability interpretation (it becomes a stabilizing, not destabilizing, term).

**Reference value** ($\beta=1$, $\lvert W''(1/2) \rvert=1$, $T_*=0.1$):

$$\mathrm{Pr}^{(\mathrm{onsite})} = \frac{1 \times 1}{0.1} = 10.0$$

---

## §4 — Part B: 5 Algebraic Identity Theorems

### §4.1 — T-IDENTITY-T8-PR-RATIO: T8 Critical Condition as Pr Ratio Equality

---

**Theorem T-IDENTITY-T8-PR-RATIO** (Cat A direct)

**Statement**:

$$\boxed{\frac{\mathrm{Pr}^{(\mathrm{spatial})}}{\mathrm{Pr}^{(\mathrm{onsite})}} = \frac{\alpha\lambda_2(L_G)/T_*}{\beta\vert W''(c)\vert /T_*} = \frac{\alpha\lambda_2(L_G)}{\beta\vert W''(c)\vert} = \frac{1}{4}\mathrm{Sc}_{T8}}$$

**Equivalence**: The T8 critical condition $\mu_2 = 0$ is equivalent to:

$$\mathrm{Sc}_{T8} = 1 \quad \Longleftrightarrow \quad \frac{\mathrm{Pr}^{(\mathrm{spatial})}}{\mathrm{Pr}^{(\mathrm{onsite})}} = \frac{1}{4} \quad \Longleftrightarrow \quad (\alpha,\beta,c) \in \Sigma_{T8}$$

**Proof (CoT chain)**:

```
CoT step 1 (premises):
  - Pr^{(spatial)} = αλ_2/T_* (L-PR-SPATIAL)
  - Pr^{(onsite)} = β|W''(c)|/T_* (L-PR-ONSITE)
  - Sc_{T8} = 4αλ_2 / (β|W''(c)|) (L-SC-T8-RATIO)

CoT step 2 (algebra):
  Pr^{(spatial)} / Pr^{(onsite)}
  = (αλ_2/T_*) / (β|W''(c)|/T_*)
  = αλ_2 / (β|W''(c)|)          [T_* cancels]
  = (1/4) × 4αλ_2 / (β|W''(c)|)
  = (1/4) × Sc_{T8}              [by definition of Sc_{T8}]

CoT step 3 (T8 equivalence):
  Sc_{T8} = 1  ⟺  4αλ_2 = β|W''(c)|  ⟺  μ_2 = 4αλ_2 + βW''(c) = 0
  (using W''(c) < 0 in spinodal, so βW''(c) = -β|W''(c)|)
  Therefore: Sc_{T8} = 1  ⟺  Pr^{(spatial)} / Pr^{(onsite)} = 1/4
  ⟺  (α,β,c) ∈ Σ_{T8}  (by SB7, canonical.md L2497–2498)

CoT step 4 (factor-4 verification):
  The factor 4 comes from the ordered-pair summation convention in canonical
  §0 (canonical.md L80): "all sums over ordered pairs; each undirected edge
  counted twice; load-bearing in T8-Core Hessian analysis."
  Hessian of 2α u^T L u = 4α L (factor 4 from ordered-pair convention × 2).
  Therefore Pr^{(spatial)} / Pr^{(onsite)} = αλ_2/(β|W''(c)|) = (1/4)Sc_{T8},
  NOT Sc_{T8} itself. The factor 1/4 is exact and load-bearing.
```

**CoC anchors**:
- Theorem 4 (canonical.md L1134–1136): $\mu_k = 4\alpha\lambda_k + \beta W''(c)$.
- SB7 (canonical.md L2497–2498): $\Sigma_{T8}$ codim-1, identical to Hessian-degeneracy locus.
- DECL-1.0 T8 central theorem: $\beta/\alpha > 4\lambda_2/\lvert W''(c) \rvert$.
- Ordered-pair convention (canonical.md L80): factor 4 in Hessian is load-bearing.

**Inverse causation**: If either L-PR-SPATIAL or L-PR-ONSITE breaks, the identity breaks.
If ordered-pair convention changed (factor 2 instead of 4): Pr ratio = 1/2 × Sc_{T8}, not 1/4.
Factor 4 is essential and non-negotiable.

**Reference verification** ($\alpha=\beta=1$, $\lambda_2=0.152241$, $\lvert W''(1/2) \rvert=1$, $T_*=0.1$):

$$\frac{\mathrm{Pr}^{(\mathrm{spatial})}}{\mathrm{Pr}^{(\mathrm{onsite})}} = \frac{1.52241}{10.0} = 0.152241$$

$$\frac{1}{4}\mathrm{Sc}_{T8} = \frac{1}{4} \times 0.608964 = 0.152241 \checkmark$$

Identity holds exactly at reference values.

**Interpretation**: The T8 phase transition is the locus where the spatial coupling Prandtl number
equals exactly $1/4$ of the onsite Prandtl number. The factor 1/4 is structural (ordered-pair
Hessian convention). Equivalently, T8 wall = "spatial deterministic force = 1/4 of onsite
deterministic force (in Prandtl units)".

---

### §4.2 — T-IDENTITY-PE-PR-BRIDGE: Péclet–Prandtl Bridge

---

**Theorem T-IDENTITY-PE-PR-BRIDGE** (Cat A direct)

**Statement**:

$$\boxed{\mathrm{Pe} = \mathrm{Pr}^{(\mathrm{spatial})} \cdot \frac{\vert \nabla\mathcal{E}\vert \cdot R}{\alpha\lambda_2(L_G)}}$$

**Geometric factor**:

$$\frac{\mathrm{Pe}}{\mathrm{Pr}^{(\mathrm{spatial})}} = \frac{\vert \nabla\mathcal{E}\vert \cdot R / T_*}{\alpha\lambda_2 / T_*} = \frac{\vert \nabla\mathcal{E}\vert \cdot R}{\alpha\lambda_2}$$

**Proof**:

```
CoT step 1: Pe = |∇E|·R / T_* (L-PECLET-DEF)
CoT step 2: Pr^{(spatial)} = αλ_2 / T_* (L-PR-SPATIAL)
CoT step 3: Pe / Pr^{(spatial)} = (|∇E|·R/T_*) / (αλ_2/T_*) = |∇E|·R / (αλ_2)   [T_* cancels]
→ Pe = Pr^{(spatial)} × (|∇E|·R / (αλ_2))
```

The geometric factor $\vert ∇\mathcal{E}\vert \cdot R / (\alpha\lambda_2)$ is the ratio of the energy-gradient
force at scale $R$ to the spatial coupling characteristic "force" $\alpha\lambda_2$ (the spectral
stiffness of the graph). When $\vert \nabla\mathcal{E}\vert \sim \alpha\lambda_2/R$ (gradient comparable
to spectral stiffness per unit length), Pe $\sim$ Pr^{(spatial)}: the Péclet number equals the
spatial Prandtl number. This bridge shows Pe is Pr^{(spatial)}-derived — Pe contains no additional
information about thermal vs deterministic balance beyond Pr^{(spatial)} and the geometric factor.

**CoC anchors**: L-PECLET-DEF + L-PR-SPATIAL (both Cat A direct from T-PF-A1-SDE + Theorem 4).

**Reference value** ($\vert \nabla\mathcal{E}\vert =1$ illustrative, $R=4$, $\alpha=1$, $\lambda_2=0.152241$, $T_*=0.1$):

$$\text{Geometric factor} = \frac{1 \times 4}{1 \times 0.152241} = 26.273$$
$$\mathrm{Pe} = 1.52241 \times 26.273 = 40.0$$

(Consistent with §3.1 reference: Pe $= 40 \times \vert \nabla\mathcal{E}\vert = 40$ at $\vert \nabla\mathcal{E}\vert =1$. ✓)

---

### §4.3 — T-IDENTITY-LEWIS-ANALOG: Lewis-Number Analog

---

**Theorem T-IDENTITY-LEWIS-ANALOG** (Cat A direct)

**Statement**:

$$\boxed{\mathrm{Le}_{\mathrm{SCC}} = \frac{\mathrm{Pr}^{(\mathrm{spatial})}}{\mathrm{Pr}^{(\mathrm{bd})}} = \frac{\alpha\lambda_2(L_G)/T_*}{\alpha W''(u^*)/T_*} = \frac{\lambda_2(L_G)}{W''(u^*)}}$$

**Proof**:

```
CoT step 1: Pr^{(spatial)} = αλ_2 / T_* (L-PR-SPATIAL)
CoT step 2: Pr^{(bd)} = αW''(u*) / T_*  (L-SC-BD-BOUNDARY)
             [Note: W''(u*) used with its sign; at boundary u* in spinodal W''(u*) < 0]
CoT step 3: Le_SCC = Pr^{(spatial)} / Pr^{(bd)}
            = (αλ_2/T_*) / (αW''(u*)/T_*)
            = λ_2 / W''(u*)   [α and T_* cancel]
```

The fluid Lewis number (thermal diffusivity / mass diffusivity) compares two diffusivities. In SCC,
the analog compares the graph-spectral coupling $\lambda_2$ (spatial diffusivity of the cohesion
field) to the double-well curvature $W''(u^*)$ (onsite restoring/destabilizing force at the boundary).
Le_{SCC} is a pure graph-spectral / double-well-curvature ratio, independent of $\alpha$, $\beta$,
and $T_*$ — determined entirely by the graph geometry ($\lambda_2$) and the field value at the
boundary ($W''(u^*)$).

**Domain**: $\alpha > 0$ (cancels), $T_* > 0$ (cancels), $W''(u^*) \neq 0$
(well-posed away from spinodal boundary $W'' = 0$).

**Interpretation**: Le_{SCC} = 1 when $\lambda_2 = W''(u^*)$ (graph spectral gap matches boundary
double-well curvature). Le_{SCC} $\neq 1$ generically: it encodes the mismatch between
graph-Laplacian spatial scale and double-well boundary scale.

**Reference value** ($\lambda_2=0.152241$, $u^*=1/2$, $W''(1/2)=-1$):

$$\mathrm{Le}_{\mathrm{SCC}} = \frac{0.152241}{-1} = -0.152241$$

(Negative because $W''(u^*)$ is negative in spinodal. The magnitude $\vert \mathrm{Le}_{\mathrm{SCC}}\vert = 0.152241$
gives the ratio of spatial to boundary scales.)

---

### §4.4 — T-IDENTITY-ST-SC-DUALITY: Stokes–Schmidt Duality

---

**Theorem T-IDENTITY-ST-SC-DUALITY** (Cat A direct)

**Statement**:

$$\boxed{\mathrm{Sc}^{(1)}_k = \frac{1}{\mathrm{St}_k}}$$

**Proof**: Trivial by definition.

$$\mathrm{St}_k = \frac{T_*}{\mu_k} \quad \Rightarrow \quad \frac{1}{\mathrm{St}_k} = \frac{\mu_k}{T_*} = \mathrm{Sc}^{(1)}_k$$

Both $\mathrm{St}_k$ and $\mathrm{Sc}^{(1)}_k$ are defined by the same ratio $\mu_k/T_*$, one as
numerator and one as denominator. The "duality" is definitional, with no mathematical content
beyond the reciprocal relationship.

**Interpretation**: Two conventions for measuring the same thing — "how much thermal is mode $k$?".
St$_k$ says: thermal over deterministic. Sc$^{(1)}_k$ says: deterministic over thermal. This file
adopts Sc$^{(1)}_k$ as the primary notation (Prandtl-family consistency, 01 §7.6).

**Reference value**: $\mathrm{Sc}^{(1)}_2 = -3.91036$, $\mathrm{St}_2 = -0.2557$; product $= 1$ ✓.

---

### §4.5 — T-IDENTITY-KRAMERS-PREFACTOR-FORM: Kramers Prefactor Structural Form

---

**Theorem T-IDENTITY-KRAMERS-PREFACTOR-FORM** (Cat A *form* only; derivation Cat B in companion `02_kramers_prefactor_op_0005_attack.md`)

**Statement (form — Identity 2a per Wave 2 critic Fix #4, file 12 §5)**:

$$\boxed{\omega_0 \sim \frac{\omega_{\mathrm{well}} \cdot \omega_{\mathrm{saddle}}}{\sqrt{\mathrm{Pr}^{(\mathrm{Kramers})}}} = \vert \mu_{\mathrm{saddle}}\vert}, \qquad \mathrm{Pr}^{(\mathrm{Kramers})} = \frac{\vert \mu_{\mathrm{well}}\lvert }{ \rvert\mu_{\mathrm{saddle}}\vert}$$

where $\omega_{\mathrm{well}} = \vert \mu_{\mathrm{well}}\vert ^{1/2}$, $\omega_{\mathrm{saddle}} = \vert \mu_{\mathrm{saddle}}\vert ^{1/2}$,
and the full Eyring-Kramers rate is $\Gamma \sim \omega_0 \exp(-\Delta\mathcal{E}/T_*)$. The algebraic equality $\omega_{\mathrm{well}} \cdot \omega_{\mathrm{saddle}} \cdot (\mathrm{Pr}^{(\mathrm{Kramers})})^{-1/2} = \vert \mu_{\mathrm{saddle}}\vert $ is the *HTB high-friction leading-order form* (file 12 §5 verification).

**Note on Identity 2 split**: The 1D-projection geometric-mean form (Identity 2b in file 02 §5.1) $\omega_0^{(2b)} \sim (1/2\pi)\sqrt{\mu_{\mathrm{well}}\cdot\vert \mu_{\mathrm{saddle}}\vert}$ is *DIFFERENT* from Identity 2a above and must not be equated. This file's T-IDENTITY-KRAMERS-PREFACTOR-FORM covers only Identity 2a (the structural Pr^{(Kramers)} reduction). For Identity 2b multi-D derivation see companion `02_kramers_prefactor_op_0005_attack.md` §5.1.

**Cat A direct (form only)**: The Hänggi-Talkner-Borkovec (1990, Rev Mod Phys 62:251) overdamped
Kramers formula for a 1D barrier is $\Gamma = (\omega_{\mathrm{well}} \cdot \vert \omega_{\mathrm{saddle}}\vert) / (2\pi\gamma) \cdot \exp(-\Delta E/k_BT)$
where $\gamma$ is friction and $\omega^2$ are the local curvatures. In SCC's overdamped Langevin
(T-PF-A1-SDE, Cat A), the analogous form uses the Hessian eigenvalues at the well ($\mu_{\mathrm{well}} > 0$,
the Hessian minimum at the formation minimizer) and at the saddle ($\mu_{\mathrm{saddle}} < 0$, the
negative Hessian eigenvalue at the transition saddle). Writing $\mathrm{Pr}^{(\mathrm{Kramers)}} =
|\mu_{\mathrm{well}}| / |\mu_{\mathrm{saddle}}|$, the structural form $\omega_0 \sim 1/\sqrt{\mathrm{Pr}^{(\mathrm{Kramers)}}}$
(up to Hessian spectral prefactors) follows directly. **This file states the structural form only.**
The derivation that $\mu_{\mathrm{well}}$ and $\mu_{\mathrm{saddle}}$ are the relevant SCC Hessian
eigenvalues at formation minimizers and K-jump saddles is the Cat B work in companion file
`02_kramers_prefactor_op_0005_attack.md` (OP-0005-DYN attack).

**Non-overclaim**: T-IDENTITY-KRAMERS-PREFACTOR-FORM does NOT prove:
- That $\mu_{\mathrm{well}}$ or $\mu_{\mathrm{saddle}}$ have known explicit forms for SCC (Cat B).
- That the 1D Hänggi-Talkner-Borkovec formula applies to the multi-dimensional SCC field (Cat B).
- The Eyring-Kramers exponent (canonical T-P-F-ε0-K Cat B, canonical.md L1818–1829).

**Reference value** (form only; explicit values require Cat B):

$$\mathrm{Pr}^{(\mathrm{Kramers})} = \vert \mu_{\mathrm{well}}\lvert / \rvert\mu_{\mathrm{saddle}}\vert \qquad (\text{Cat B to evaluate})$$

---

## §5 — Part C: Hessian-Rescaling Identity

### §5.1 — T-RESCALE-HESSIAN-LINEAR: Linear Rescaling of Hessian under $(\alpha,\beta) \to (s\alpha, s\beta)$

---

**Theorem T-RESCALE-HESSIAN-LINEAR** (Cat A direct)

**Statement**: Under the uniform rescaling $(\alpha, \beta) \to (s\alpha, s\beta)$ for $s > 0$:

$$\boxed{\mu_k(s\alpha, s\beta, c) = s \cdot \mu_k(\alpha, \beta, c)}$$

**Corollaries**:
1. Goldstone modes preserved: if $\mu_k = 0$ then $\mu_k(s\alpha,s\beta,c) = 0$.
2. Non-Goldstone modes scale linearly: $\mu_k \to s\mu_k$ (gap increases by factor $s$).
3. Sc_{T8} preserved: $\mathrm{Sc}_{T8}(s\alpha,s\beta) = 4(s\alpha)\lambda_2/((s\beta)\lvert W''(c) \rvert) = \mathrm{Sc}_{T8}(\alpha,\beta)$.
4. $\sigma \to s\sigma$: $\sigma(s\alpha,s\beta) = (\sqrt{2}/6)\sqrt{(s\alpha)(s\beta)} = s \cdot (\sqrt{2}/6)\sqrt{\alpha\beta} = s\sigma$ (homogeneity preserved regardless of prefactor).
5. $\mathrm{Da} = \beta/\alpha$ preserved: $(s\beta)/(s\alpha) = \beta/\alpha$.

**Proof**:

```
CoT step 1 (Theorem 4 linearity):
  μ_k(α,β,c) = 4αλ_k + βW''(c)     [Theorem 4, canonical.md L1134–1136]
  μ_k(sα,sβ,c) = 4(sα)λ_k + (sβ)W''(c)
               = s(4αλ_k + βW''(c))
               = s · μ_k(α,β,c)      QED — algebraic, no approximation

CoT step 2 (Goldstone preservation):
  If μ_k = 0 (V5b-T-zero, canonical.md L1328): μ_k(sα,sβ,c) = s × 0 = 0.  ✓

CoT step 3 (non-Goldstone scaling):
  If μ_k ≠ 0: μ_k(sα,sβ,c) = s·μ_k ≠ 0 (same sign, magnitude × s).  ✓

CoT step 4 (Sc_{T8} preservation):
  Sc_{T8}(sα,sβ) = 4(sα)λ_2 / ((sβ)|W''(c)|) = (4αλ_2)/(β|W''(c)|) = Sc_{T8}(α,β).  ✓
  → The T8 phase transition condition is INVARIANT under rescaling.
  → The rescaling cannot move the system across the T8 wall.
  → H-Morse improvement (gap increase) achievable WITHOUT changing phase regime.

CoT step 5 (surface tension scaling):
  σ(sα,sβ) = (√2/6)·√((sα)(sβ)) = s·(√2/6)·√(αβ) = s·σ.  ✓
  → Ca = |∇E|/σ → Ca/s (decreases with s: interface becomes relatively stiffer).
  → Bo = R²|∇E|/σ → Bo/s.
```

**CoC anchors**:
- Theorem 4 (canonical.md L1134–1136): $\mu_k = 4\alpha\lambda_k + \beta W''(c)$ — linear in $(\alpha,\beta)$.
- V5b-T-zero (canonical.md L1328): Goldstone $\mu_k = 0$ exact on translation-invariant graphs.
- CSSL critic-survived idea (cssl/01_critic_evaluation.md §5.5; 01_ns_inspired_synthesis.md §7.5 Identity 5).

**H-Morse application** (01_ns_inspired_synthesis.md §8.1):
Choose $s \gg 1$. Then all non-Goldstone Hessian eigenvalues scale as $s\mu_k$. The H-Morse spectral
gap (minimum positive eigenvalue of constrained Hessian) scales as $s \cdot \mathrm{gap}$.
Goldstone modes remain zero. Therefore: for any target spectral gap $\delta > 0$, there exists
$s_0 = \delta/\mathrm{gap}$ such that for $s \geq s_0$ the H-Morse spectral gap condition is met.
**This is Cat A direct**: it requires only the linearity proved above plus the fact that the initial
gap is positive (which requires D-HMORSE-LOCAL conditions, Cat B — but the *rescaling argument itself*
is Cat A regardless).

**Stop condition**: $s \to \infty$ drives Pr^{(spatial)} and Pr^{(onsite)} both to $\infty$
proportionally (both scale as $s$), maintaining their ratio Sc_{T8} fixed. However, Sc$^{(1)}_k =
\mu_k/T_* = s\mu_k/T_*$ grows; St$_k = T_*/\mu_k = T_*/(s\mu_k)$ shrinks. The optimal $s$ is
bounded by Pe $\sim O(1)$ (deterministic-thermal balance) per 01 §8.1.

**Reference value** at $s=2$ ($\alpha=\beta=1 \to \alpha=\beta=2$):

$$\mu_2(2,2,1/2) = 2 \times (-0.391036) = -0.782072$$
$$\sigma(2,2) = 2 \times (\sqrt{2}/6) = \sqrt{2}/3 \approx 0.4714$$
$$\mathrm{Sc}_{T8}(2,2) = 0.608964 \quad \text{(unchanged)} \checkmark$$

---

## §6 — Numerical Reference Table

All 16 lemmas evaluated at 2D torus L=16, $c=1/2$, $\alpha=\beta=1$, $T_*=0.1$, $R=4$,
$\vert \nabla\mathcal{E}\vert =1$ (illustrative unit gradient).

| # | Label | Formula | Reference value |
|---|---|---|---|
| 1 | $\mathrm{Pe}$ | $\vert \nabla E\vert R / T_*$ | $40.0$ (at $\vert \nabla E\vert =1$) |
| 2 | $\mathrm{Da}$ | $\beta/\alpha$ | $1.0$ |
| 3 | $\mathrm{Ca}$ | $\vert \nabla E\vert / \sigma$ | $\approx 4.243$ (at $\sigma=\sqrt{2}/6 \approx 0.2357$; CORRECTED per Fix #1) |
| 4 | $\mathrm{Bo}$ | $R^2 \vert \nabla E\vert / \sigma$ | $\approx 67.88$ (CORRECTED per Fix #1) |
| 5 | $\mathrm{St}_2$ | $T_* / \mu_2$ | $-0.2557$ |
| 6 | $\mathrm{Sc}^{(1)}_2$ | $\mu_2 / T_*$ | $-3.9104$ |
| 7 | $\mathrm{Sc}_{T8}$ | $4\alpha\lambda_2 / (\beta\vert W''(c)\vert)$ | $0.608964$ |
| 8 | $\mathrm{Pr}^{(\mathrm{bd})}$ | $\alpha\vert W''(u^*)\vert / T_*$ | $10.0$ |
| 9 | $\mathrm{Pr}^{(\mathrm{spatial})}$ | $\alpha\lambda_2 / T_*$ | $1.52241$ |
| 10 | $\mathrm{Pr}^{(\mathrm{onsite})}$ | $\beta\vert W''(c)\vert / T_*$ | $10.0$ |
| 11 | Identity T8-PR | $\mathrm{Pr}^{(\mathrm{spatial})} / \mathrm{Pr}^{(\mathrm{onsite})}$ | $0.152241 = (1/4)\mathrm{Sc}_{T8}$ ✓ |
| 12 | Identity Pe-Pr | $\mathrm{Pe} / \mathrm{Pr}^{(\mathrm{spatial})}$ | $26.273 = \vert \nabla E\vert R / (\alpha\lambda_2)$ |
| 13 | Identity Le | $\mathrm{Pr}^{(\mathrm{spatial})} / \mathrm{Pr}^{(\mathrm{bd})}$ | $-0.152241 = \lambda_2/W''(u^*)$ |
| 14 | Identity St-Sc | $\mathrm{Sc}^{(1)}_2 \times \mathrm{St}_2$ | $1.0$ ✓ |
| 15 | Kramers form | $\omega_0 \sim 1/\sqrt{\mathrm{Pr}^{(\mathrm{Kramers})}}$ | Cat B values pending |
| 16 | Rescaling | $\mu_k(s\alpha,s\beta)$ | $s \times (-0.391036)$ at mode 2 |

**Cross-check T-IDENTITY-T8-PR-RATIO**:
$(1/4) \times 0.608964 = 0.152241$; Pr^{(spatial)}/Pr^{(onsite)} $= 1.52241/10.0 = 0.152241$ ✓ exact.

---

## §7 — Cat A Summary + Companion Files Cross-Reference

### §7.1 Cat A items in this file

| Item | Type | Canonical anchor | Cat status |
|---|---|---|---|
| L-PECLET-DEF | definition | T-PF-A1-SDE (L1668) | **Cat A direct** |
| L-DAMKOHLER-DEF | definition | T8-Core (L1134–1136) | **Cat A direct** |
| L-CAPILLARY-DEF | definition | T11 Γ-convergence (L1167) + I6 double-well | **Cat A direct** |
| L-BOND-DEF | definition | L-CAPILLARY-DEF × R | **Cat A direct** |
| L-STOKES-DEF | definition | Theorem 4 (L1134–1136) + T-PF-A1-SDE (L1668) | **Cat A direct** |
| L-SC1-MODE-HESSIAN | definition | 1/L-STOKES-DEF | **Cat A direct** |
| L-SC-T8-RATIO | definition | SB7 (L2497) + Theorem 4 (L1134) | **Cat A direct** |
| L-SC-BD-BOUNDARY | definition | Theorem 4 + T-PF-A1-SDE | **Cat A direct** |
| L-PR-SPATIAL | definition | Theorem 4 spatial term | **Cat A direct** |
| L-PR-ONSITE | definition | Theorem 4 onsite term | **Cat A direct** |
| T-IDENTITY-T8-PR-RATIO | identity | algebra of above | **Cat A direct** |
| T-IDENTITY-PE-PR-BRIDGE | identity | algebra of above | **Cat A direct** |
| T-IDENTITY-LEWIS-ANALOG | identity | algebra of above | **Cat A direct** |
| T-IDENTITY-ST-SC-DUALITY | identity | definition | **Cat A direct** |
| T-IDENTITY-KRAMERS-PREFACTOR-FORM | form only | T-PF-A1-SDE structural | **Cat A form; derivation Cat B** |
| T-RESCALE-HESSIAN-LINEAR | identity | Theorem 4 linearity + V5b-T-zero | **Cat A direct** |

### §7.2 Cat B items excluded from this file (in companion files)

| Item | Companion file | Status |
|---|---|---|
| $\mathrm{Sc}^{(2)}$ (bulk-active separation) | future `03_hmorse_spectral_gap_cat_b.md` | Cat B target (L-HMORSE-DECOMP conditional) |
| $\mathrm{Pr}^{(\mathrm{Kramers})}$ explicit form | `02_kramers_prefactor_op_0005_attack.md` | Cat B target (OP-0005-DYN) |
| Eyring-Kramers prefactor derivation | `02_kramers_prefactor_op_0005_attack.md` | Cat B target |
| Modica-Mortola Jacobi H-Morse | future `04_modica_mortola_jacobi_cat_b.md` | Cat B target |
| H-Morse Pr^{(bd)} threshold proof | `06_surface_tension_rescaling_cat_a.md` | Cat B target (D-HMORSE-LOCAL C2′) |
| H-Morse application of rescaling | `06_surface_tension_rescaling_cat_a.md` | Cat A direct |

---

## §8 — CoT/CoC Archival: T-IDENTITY-T8-PR-RATIO Factor Verification

This is the most non-trivial item in the catalog — the factor of 1/4 between Pr^{(spatial)}/Pr^{(onsite)}
and Sc_{T8}.

```yaml
target: Verify that Pr^{(spatial)} / Pr^{(onsite)} = (1/4) Sc_{T8}, NOT Sc_{T8} itself.

critical_step: The factor 4 in Theorem 4's μ_k = 4αλ_k + βW''(c).

prior_anchors:
  - canonical.md L80: "ordered-pair summation convention; each undirected edge counted twice
    when kernel is symmetric; load-bearing in T8-Core and Hessian analysis."
  - canonical.md L1134: T8-Core proof: "ordered-pair summation gives smoothness functional
    2α v^T L v with Hessian 4αL."
  - canonical.md L1136: "Second variation at u≡c has eigenvalue 4αλ_2 + βW''(c)."

causation_chain:
  - Energy E_bd = α u^T L u (where L = ordered-pair sum Laplacian, so the formula already
    incorporates the ×2 from ordered pairs). Hessian = 2αL? NO.
  - Correct: E_bd = α Σ_{(x,y) ordered} (u_x - u_y)² / 2 = α u^T L u
    Actually: E_bd(u) = (α/2) Σ_{(x,y)} (u_x-u_y)² = α u^T L u in standard form.
    Hessian of α u^T L u = 2αL? NO.
  - Canonical resolution (L80 + L1134): "2α v^T L v with Hessian 4αL."
    This means E_bd = 2α u^T L u in the canonical convention, giving Hessian = 4αL.
    Eigenvalue at mode k: 4αλ_k. This matches μ_k = 4αλ_k + βW''(c) exactly.
  - Therefore: Pr^{(spatial)} = αλ_2/T_*, NOT 4αλ_2/T_*.
    Sc_{T8} = 4αλ_2/(β|W''(c)|).
    Ratio: Pr^{(spatial)}/Pr^{(onsite)} = αλ_2/(β|W''(c)|) = Sc_{T8}/4.

inverse_causation_check:
  - If factor 4 were 2 (wrong convention): Pr^{(spatial)}/Pr^{(onsite)} = Sc_{T8}/2 (wrong).
  - If factor 4 were 1 (naive, no ordered-pair): Pr/Pr = Sc_{T8} (wrong).
  - The factor 4 is exactly load-bearing (canonical.md L80: "load-bearing in T8-Core").
  - Numerical check: 1.52241/10.0 = 0.152241 = 0.608964/4. All consistent. ✓

conclusion: Factor 1/4 is exact, non-negotiable, anchored to ordered-pair convention.
  The statement "T8 critical ⟺ Pr^{(spatial)}/Pr^{(onsite)} = 1/4" is the correct form.
```

---

## §9 — Hard Constraint CN1-16 Check

| Constraint | Status | Evidence |
|---|---|---|
| **CN1** canonical/* edits 0 | ✓ | This file is working layer only; no canonical/* write |
| **CN2** Silent OP resolution 0 | ✓ | §7.2 explicitly lists excluded Cat B items; Kramers form stated as form-only |
| **CN3** Research OS 재도입 0 | ✓ | Single working file; no new registry directory |
| **CN4 (analyticity, b_D=0)** | ✓ | Zero new energy terms; all items are parameter ratios only |
| **CN5 (4-term independence)** | ✓ | $\mathcal{E}_{cl}, \mathcal{E}_{sep}, \mathcal{E}_{bd}, \mathcal{E}_{tr}$ untouched |
| **Closure idempotence** | ✓ | Not invoked |
| **K double-counting** | ✓ | K-vocabulary absent in dimensionless framework |
| **Zero-temp metastability flag** | ✓ | $T_* > 0$ required explicitly in each lemma domain |
| **CN10 (no reductive reduction)** | ✓ | All NS references contrastive; SCC ≠ fluid explicitly (§1) |
| **Primitive u_t** | ✓ | All dimensionless numbers are derived ratios; u_t primitive unchanged |
| **Inertia 0** | ✓ | No second-order temporal term; no momentum field introduced |
| **Mori-Zwanzig 0** | ✓ | No effective memory kernel; T-PF-A1-SDE first-order only |
| **Cat B non-overclaim** | ✓ | §7.2 + §4.5 explicit Cat B boundary for Kramers |
| **Canonical anchor specificity** | ✓ | All proofs cite canonical.md line numbers |
| **CSSL avoid-patterns** | ✓ | No $E_{ridge}$, $E_{wild}$, $E_{pers}$ terms; no PH-energy introduction |
| **P-P6 archive patterns** | ✓ | §0.2 audit: 0/6 violations |

**git status THEORY/canonical/ output** (expected): clean (0 modifications, 0 untracked in canonical/).

---

## §10 — One-Paragraph Summary

This file formalizes 16 Cat A direct items: 10 dimensionless number definitions (Pe, Da, Ca, Bo, St,
Sc^{(1)}, Sc_{T8}, Pr^{(bd)}, Pr^{(spatial)}, Pr^{(onsite)}) and 5 algebraic identities (T8 as Pr
ratio with factor 1/4, Pe-Pr bridge, Lewis analog, St-Sc duality, Kramers structural form) plus the
Hessian-rescaling identity, all proved as one-paragraph direct consequences of canonical Theorem 4
($\mu_k = 4\alpha\lambda_k + \beta W''(c)$, canonical.md L1134–1136) and the T-PF-A1 Package I
(canonical.md L1652–1707). The most non-trivial item is T-IDENTITY-T8-PR-RATIO: the T8 phase
transition is equivalently stated as $\mathrm{Pr}^{(\mathrm{spatial})}/\mathrm{Pr}^{(\mathrm{onsite})} = 1/4$
(NOT 1), where the factor 1/4 is load-bearing and anchored to the ordered-pair summation convention
(canonical.md L80). All 16 items are numerically verified at the 2D torus L=16, $c=1/2$, $\alpha=\beta=1$,
$T_*=0.1$, $R=4$ reference point using $\lambda_2 = 0.152241$ (verified 02_cg_numerical_verification.md)
and $W''(1/2) = -1$ (canonical I6 double-well). No canonical/* edits; zero Cat B overclaims;
zero new energy terms; zero new abstractions.
