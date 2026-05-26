---
type: working/field_equation_framework/cat_a_target_derivation
date: 2026-05-20
session_origin: W8-Day3 late, Wave 2 ultrawork (complement to 02_kramers_prefactor_op_0005_attack.md, addressing file 02 prefactor complications via Cat A path)
canonical_version: CV-1.18 SEALED (untouched throughout)
status: draft v0.1
authors: user (Jaehong Oh)
preceded_by:
  - 01_ns_inspired_synthesis.md (§6 #12 Pr^{(Kramers)}, §11 Tier 1)
  - 02_kramers_prefactor_op_0005_attack.md (Cat B prefactor target — complemented here, NOT superseded)
  - 07_critic_full_review.md §A (file 02 critic findings: det/det' ambiguity, dimensional issues, μ_well/μ_saddle order-of-magnitude defects — all PREFACTOR-RELATED, sidestepped here at LDP exponential-rate level)
  - canonical §13 T-PF-A1-AR / T-PF-A1-SDE / T-PF-A1-GI / T-PF-A1-PE (all Cat A, CV-1.9) — reflected Langevin foundation
  - canonical §13 T-P-F-ε0-K (Cat B conditional on H5) — Arrhenius barrier stability
  - canonical theorem_status.md L803 OP-0005-DYN OPEN (Package II, W9+) — primary OPEN row addressed
  - canonical theorem_status.md L594 OP-HMORSE-SADDLE OPEN (separate, prefactor-only) — NOT a hypothesis here (LDP rate is saddle-Hessian-regularity-free)
purpose: |
  Derive the Freidlin-Wentzell large-deviation principle (LDP) for SCC reflected Langevin
  as a **Cat A complement** to file 02's Hänggi-Talkner-Borkovec (Cat B) prefactor attack.
  Deliver L-FW-KRAMERS-SCC Cat A target lemma: the *exponential rate*
  $\lim_{T_*\to 0} T_*\log \Gamma_{A\to B} = -2\Delta\mathcal{E}$ is *prefactor-free*,
  avoiding det/det' / Morse-regularity / saddle-Hessian conditional dependence.
  Freidlin-Wentzell 1998 is a *contrastive standard tool* in the same class as
  Hänggi-Talkner-Borkovec — but operates *one level coarser* (logarithmic-asymptotics only),
  inheriting Cat A in probability theory. Provides the Cat A entry into Package II
  that file 02 cannot deliver due to OP-HMORSE-SADDLE blockage.
canonical_compatibility:
  CN1_canonical_edits: 0
  CN2_silent_op_resolution: 0 (target-level only; OP-0005-DYN remains OPEN)
  CN3_research_os_redux: 0
  CN4_analyticity: preserved (zero new energy terms)
  CN5_4_term_independence: preserved
  CN10_no_reductive_reduction: contrastive only (Freidlin-Wentzell = external standard probability toolkit)
  primitive_u_t: preserved
  inertia_introduction: forbidden (Package I Cat A protection — §3.2 explicit)
  Mori_Zwanzig: forbidden (CV-1.18 SEAL)
  CSSL_E_ridge_E_wild_E_pers: forbidden
  second_order_temporal: forbidden (Package I cascade)
cot_enforced: yes
coc_enforced: yes
inverse_causation_enforced: yes (each Cat-A-target claim §5.X)
consensus_baseline_used:
  surface_tension: "σ = (√2/6)·√(αβ)"
  reference_torus: "2D PBC L=16, λ_2 = 4sin²(π/16) ≈ 0.1522"
  reference_params: "c=1/2, α=1, β=10, T_*=0.1, R=4"
  W_double_well: "W''(1/2) = -1"
---

> [!nav] Linked: [[01_ns_inspired_synthesis]] · [[02_kramers_prefactor_op_0005_attack]] (Cat B prefactor — complement) · [[07_critic_full_review]] §A · [[canonical|CV-1.18 canonical]] (§13 T-PF-A1-SDE/PE, T-P-F-ε0-K, Theorem 4) · [[theorem_status]] (L803 OP-0005-DYN, L594 OP-HMORSE-SADDLE) · [[DECLARATION|DECL-1.0]] (Q3 stochastic dynamics)

# 09 — Freidlin-Wentzell Large Deviations for SCC Reflected Langevin: L-FW-KRAMERS-SCC Cat A Target (OP-0005-DYN Exponential-Rate Channel)

**Mode:** working-layer Cat A target derivation (NOT verification, NOT SEAL prep, NOT canonical edit).
**Target:** Apply Freidlin-Wentzell 1998 (*Random Perturbations of Dynamical Systems*, 2nd ed., Springer Grundlehren 260) small-noise LDP to canonical T-PF-A1-SDE (Cat A, CV-1.9) to deliver the **logarithmic-asymptotic transition rate** $\lim_{T_*\to 0} T_*\log\Gamma_{A\to B} = -2\Delta\mathcal{E}$ as a **Cat A target lemma L-FW-KRAMERS-SCC**, complementing (not replacing) file 02's HTB Cat B prefactor target. Avoids file 02's det/det' / Morse-saddle / dimensional complications by stopping at the *exponential rate*.

---

## §0 — Frontmatter, Pre-Work Cross-Reference Check, §8a P1–P6 Audit, CONSENSUS BASELINE

### §0.1 Pre-work xref check

- `grep -rn "Freidlin\|Wentzell\|quasipotential\|large deviation" canonical/` → 0 hits. *No prior canonical formulation of LDP / quasipotential for SCC.*
- `grep -rn "Freidlin\|Wentzell\|quasipotential" working/` → 0 hits in field_equation_framework files 01–07. *First working-layer LDP derivation for SCC.*
- **Novel positioning:** This file is the *first* SCC-internal application of Freidlin-Wentzell small-noise LDP to T-PF-A1-SDE. It is *deliberately complementary* to file 02 (HTB prefactor) — operating at the *coarser* logarithmic-asymptotics level where prefactor difficulties (file 02 §A.2/A.3/A.4/A.5) *do not arise*. The result is *target-level Cat A*: the LDP rate function $I$ is a Cat A object in probability theory (Freidlin-Wentzell 1998 Theorem 3.1, Dembo-Zeitouni 1998 §5); its SCC instantiation inherits Cat A *if and only if* T-PF-A1-SDE is Cat A — which it is (canonical CV-1.9).

### §0.2 §8a archive pattern P1–P6 audit

| Pattern | Risk | This file |
|---|---|---|
| **P1** (근본 질문 우회) | LDP as substitute for DECL Q3 | ✓ No. §1.1 anchors DECL Q3 (stochastic dynamics) as the question; LDP provides the *exponential-rate answer-channel* (file 02 HTB provides the *prefactor channel*). |
| **P2** (vocabulary refactoring) | Renaming canonical objects | ✓ No. $\mathcal{E}$, $T_*$, $\Pi_{T\Sigma_m}$, $\Sigma_m$, $\Delta\mathcal{E}$, $\lambda_k(L_G)$, $W''(c)$ are canonical residents. The *new* object is the *quasipotential* $V(u^*,u)$ — a *standard Freidlin-Wentzell concept*, defined inside this file (§3) without renaming canonical content. |
| **P3** (canonical content 중복) | Re-stating T-PF-A1-SDE / T-PF-A1-PE | ✓ No. Both are *cited*, not restated. The LDP machinery is *external* to canonical. |
| **P4** (외부 도구 도입) | Freidlin-Wentzell as *reduction* (CN10 drift) | ✓ No. §1.2 + §2.1 explicit: Freidlin-Wentzell 1998 is the *standard small-noise LDP toolkit* for SDEs, applied here to canonical T-PF-A1-SDE. SCC is *not reduced* to a Brownian particle; the *probabilistic* machinery (Schilder's theorem + contraction principle + Varadhan's lemma) operates on *any* SDE meeting standard regularity, and T-PF-A1-SDE does (Lipschitz drift on compact convex domain). |
| **P5** (self-audit) | Missing CN check | ✓ §12 16/16 ✓. |
| **P6** (언어-수학 분리) | Hand-waving rate function | ✓ §2.2 explicit rate-function formula; §3 explicit quasipotential definition; §5.3 5-step proof sketch enumerated; §9 numerical worked example. |

**0/6 patterns matched.** Proceed.

### §0.3 CONSENSUS BASELINE (locked, mandatory per Wave 1 cross-file inconsistency closure — file 07 §F)

This file uses *exactly* the following values; no per-section drift permitted.

| Quantity | Value | Source |
|---|---|---|
| Surface tension $\sigma$ | $(\sqrt{2}/6)\cdot\sqrt{\alpha\beta}$ | Modica-Mortola $\int_0^1\sqrt{2W(s)}ds = \sqrt{2}/6$; file 03 §2.2 derivation, file 07 §F.1 verified correct |
| Reference graph | 2D torus PBC $L=16$, $n=256$ | Standard SCC formation regime test bed |
| $\lambda_2$ | $4\sin^2(\pi/16) \approx 0.1522$ | 2D torus PBC second eigenvalue, canonical |
| Reference $c$ | $1/2$ | Spinodal interior center |
| Reference $\alpha$ | $1$ | Unit cohesion smoothing |
| Reference $\beta$ | $10$ | Deep formation regime (file 02 §6.1 consistent) |
| Reference $T_*$ | $0.1$ | Small-noise regime (1/100 of $\beta$) |
| Reference $R$ | $4$ | Formation radius scale |
| $W''(1/2)$ | $-1$ | $W(u)=u^2(1-u)^2 \Rightarrow W''(u) = 12u^2 - 12u + 2 \Rightarrow W''(1/2) = 3 - 6 + 2 = -1$ |
| Canonical OP rows | OP-HMORSE-SADDLE at `theorem_status.md` L594; OP-0005-DYN at `theorem_status.md` L803 | Verified (file 07 §B.1) |
| Theorem 4 location | canonical.md L1134-1136 | Verified |

---

## §1 — Mission: LDP as Cat A Complement to HTB Cat B Prefactor

### §1.1 What this file *does*

1. **Set up Freidlin-Wentzell small-noise LDP** (§2) for T-PF-A1-SDE in the regime $T_* \to 0$, with $\epsilon := T_*$ as the small parameter. Rate function $I_{[0,T]}(\phi) = (1/2)\int_0^T \vert \dot\phi + \Pi\nabla\mathcal{E}\vert ^2\,dt$ on absolutely continuous paths.
2. **Define the SCC quasipotential** $V(u^*, u)$ (§3) as the infimum of $I$ over paths from $u^*$ to $u$. Prove the *gradient-flow simplification* $V(u^*, u) = 2(\mathcal{E}(u) - \mathcal{E}(u^*))$ on the basin of attraction of well $u^*$.
3. **Derive the Eyring-Kramers exponential rate** (§4) from the quasipotential via the standard Freidlin-Wentzell exit-time / Markov-chain-of-wells / contraction-principle argument: $\lim_{T_*\to 0} T_*\log\mathbb{E}[\tau_{A\to B}] = V_{\min} = 2\Delta\mathcal{E}_{A\to\text{saddle}}$.
4. **State L-FW-KRAMERS-SCC Cat A target lemma** (§5): statement + 3 hypotheses (H1 T-PF-A1-SDE Cat A applicability + H2 reflected boundary regularity + H3 gradient-flow basin structure) + 5-step proof sketch + inverse causation.
5. **Compare with HTB approach** (§6): LDP gives *Cat A leading-order exponential*, HTB (file 02) gives *Cat B prefactor*. Together they constitute the *full Eyring-Kramers form* with two cat assignments. Crucially the LDP does *not* require H5 Morse stability or OP-HMORSE-SADDLE — the file 02 blockers.
6. **Factor-2 reconciliation** (§7): explicit verification that FW's $-2\Delta\mathcal{E}/T_*$ coincides with standard Kramers $-\Delta E/k_BT$ when the SCC noise normalization $\sqrt{2T_*}$ is accounted for. *Crucial sanity check; failure here would invalidate §4–§5.*
7. **Connection to canonical T-PF-A1-PE** (§8): the canonical Poincaré bound $\lambda_1 \geq (\pi^2/n)e^{-\mathrm{osc}(\mathcal{E})/T_*}$ has *exactly the spectral form* of the LDP exit-rate, providing canonical anchor at *one specific level* (worst-case osc bound; LDP improves to *barrier-specific* bound).
8. **2D torus reference example** (§9) using CONSENSUS BASELINE.
9. **OPEN problem leverage** (§10): OP-0005-DYN gets a *Cat A* path via LDP rate + *Cat B* path via HTB prefactor; T-P-F-ε0-K's H5 dependence is *bypassed* by LDP for rate (still required for prefactor).

### §1.2 What this file *does NOT* do

- ❌ **Canonical promotion:** L-FW-KRAMERS-SCC remains *working-layer Cat A target*; no claim of canonical entry. canonical/* edits = 0.
- ❌ **OP-0005-DYN closure:** the OPEN row remains OPEN. Only the *Cat A exponential-rate channel* is delivered.
- ❌ **Prefactor computation:** LDP gives *only* $\lim T_*\log\Gamma = -2\Delta\mathcal{E}$. The subexponential prefactor $\omega_0$ (file 02 territory) is *not* claimed.
- ❌ **Full Eyring-Kramers form:** would require *both* LDP rate (here) AND HTB prefactor (file 02 — Cat B). This file delivers only the LDP half.
- ❌ **OP-HMORSE-SADDLE discharge:** not needed for LDP rate (the rate function $I$ does not require non-degeneracy of $\mathrm{Hess}\,\mathcal{E}$ at saddle — only existence of a barrier). This is *precisely* why LDP gives Cat A where HTB gives Cat B.
- ❌ **CSSL patterns:** no $E_{\text{ridge}}, E_{\text{wild}}, E_{\text{pers}}$. The quasipotential $V$ is a *derived* object from canonical $\mathcal{E}$, not a new energy term.
- ❌ **Reductive reduction to fluid mechanics (CN10):** Freidlin-Wentzell 1998 is a probability-theory monograph on small-noise SDE asymptotics. It applies to *any* SDE meeting regularity (including SCC via T-PF-A1-SDE Cat A).

### §1.3 Why Cat A (and what file 02 cannot achieve)

```
CoT step 1: File 02's HTB prefactor requires |det' Hess(E)(saddle)| in the denominator — this depends on the saddle-Hessian eigenvalues being well-defined and non-degenerate (OP-HMORSE-SADDLE).
CoT step 2: OP-HMORSE-SADDLE is canonically OPEN (theorem_status.md L594, ETA 2-4 sessions). File 02 inherits this OPEN status → Cat B.
CoT step 3: Freidlin-Wentzell LDP rate function I_{[0,T]}(φ) = (1/2)∫|φ̇ + Π∇E|² dt requires only: (a) E ∈ C^2 (canonical T-PF-A1-AR), (b) ∇E Lipschitz on F_M(G) (canonical T-PF-A1-AR), (c) compact convex domain (canonical T-PF-A1-AR), (d) Lions-Sznitman reflection (canonical T-PF-A1-SDE). NO saddle-Hessian regularity required.
CoT step 4: Therefore the LDP rate -2ΔE is a Cat A consequence of T-PF-A1-SDE Cat A — no additional OPEN dependence.
→ Cat A entry into Package II is via LDP (this file); Cat B entry via HTB (file 02). Together they cover the Eyring-Kramers full form.

CoC anchors:
  - canonical §13 T-PF-A1-AR (Cat A, CV-1.8) — Lipschitz drift on compact convex F_M(G)
  - canonical §13 T-PF-A1-SDE (Cat A, CV-1.8) — Lions-Sznitman reflected SDE well-posed
  - canonical §13 T-PF-A1-PE (Cat A, CV-1.9) — Poincaré + L²→TV ergodicity (LDP refinement)
  - Freidlin-Wentzell 1998 Theorem 3.1 + Theorem 4.1 (Springer Grundlehren 260)
  - theorem_status.md L803 OP-0005-DYN OPEN (target row)
  - theorem_status.md L594 OP-HMORSE-SADDLE OPEN (NOT a hypothesis here — explicit gap-removal vs file 02)
inverse_causation_check:
  - if T-PF-A1-SDE were not Cat A: LDP rate has no SDE foundation → fails to Cat A (was the case pre-CV-1.8; now resolved)
  - if E were not C^2: rate function I ill-defined → no LDP (preserved by SCC analyticity, CN4)
  - if OP-HMORSE-SADDLE were closed: HTB prefactor (file 02) also Cat A → file 09 becomes redundant. Currently OP-HMORSE-SADDLE OPEN → file 09 is uniquely valuable.
```

---

## §2 — Freidlin-Wentzell LDP Setup

### §2.1 Source and scope

**Reference (external, contrastive only):** Freidlin M. I., Wentzell A. D., *Random Perturbations of Dynamical Systems*, 2nd ed., Springer Grundlehren der mathematischen Wissenschaften vol. 260 (1998). Chapter 3 (action functional for diffusion processes) + Chapter 4 (exit problem, quasipotential). Modern textbook treatment also in Dembo A., Zeitouni O., *Large Deviations Techniques and Applications*, 2nd ed., Springer Stochastic Modelling 38 (1998), §5.6 "Sample path large deviations."

**Scope of application:** Freidlin-Wentzell treats SDEs of the form $dX^\epsilon = b(X^\epsilon)dt + \sqrt{\epsilon}\sigma(X^\epsilon)dB$ on $\mathbb{R}^N$ or a manifold, in the limit $\epsilon \to 0$. The LDP gives sample-path concentration $\mathbb{P}(X^\epsilon \approx \phi) \asymp \exp(-I(\phi)/\epsilon)$ with rate function $I$ supported on absolutely continuous paths. Application to *reflected* SDEs on convex domains is standard (Freidlin-Wentzell §3.4 reflected diffusions; Anderson-Orey 1976; Dupuis-Ishii 1991). SCC's T-PF-A1-SDE (Cat A) fits this framework: drift $b = -\Pi\nabla\mathcal{E}$ is Lipschitz (canonical T-PF-A1-AR), diffusion $\sigma = \Pi$ is constant (degenerate but rank $n-1$ on tangent space — the *intrinsic* dimension), domain $\tilde{C}$ is compact convex polytope (canonical T-PF-A1-AR), reflection is Skorokhod (canonical T-PF-A1-SDE Lions-Sznitman 1984).

**CN10 boundary:** Freidlin-Wentzell is *not* a reduction "SCC = Brownian particle." It is the *standard probability-theory framework for small-noise diffusion asymptotics*, applicable to *any* SDE in its scope. SCC supplies an SDE (T-PF-A1-SDE) within scope.

### §2.2 LDP rate function

Identify $\epsilon := T_*$ in the canonical T-PF-A1-SDE:

$$dU_t = -\Pi_{T\Sigma_m}\nabla\mathcal{E}(U_t)\,dt + \sqrt{2T_*}\,\Pi_{T\Sigma_m}\,dB_t + dK_t.$$

Set $\sigma = \sqrt{2}\,\Pi_{T\Sigma_m}$ so $\sigma\sigma^\top = 2\Pi_{T\Sigma_m}\Pi_{T\Sigma_m}^\top = 2\Pi_{T\Sigma_m}$ (idempotent projector). Then the Freidlin-Wentzell rate function on $C([0,T]; \tilde{C})$ (continuous paths into the polytope) is

$$\boxed{I_{[0,T]}(\phi) = \frac{1}{2}\int_0^T \langle \dot\phi(t) + \Pi\nabla\mathcal{E}(\phi(t)),\, (\sigma\sigma^\top)^+\, [\dot\phi(t) + \Pi\nabla\mathcal{E}(\phi(t))] \rangle\,dt = \frac{1}{4}\int_0^T \lVert \dot\phi + \Pi\nabla\mathcal{E} \rVert^2\,dt}$$

on absolutely continuous paths $\phi: [0,T] \to \tilde{C}$ with $\phi(t) \in T\Sigma_m$ component (the reflection $dK_t$ contributes additional boundary terms vanishing in the interior — Anderson-Orey 1976). The Moore-Penrose pseudoinverse $(\sigma\sigma^\top)^+ = (1/2)\Pi$ accounts for the rank-$(n-1)$ degenerate diffusion (zero mode = mass-conservation direction $\mathbf{1}/\sqrt{n}$ is *deterministically conserved* by drift projection).

For paths *in the interior* and *tangent to* $\Sigma_m$ (so $\Pi\dot\phi = \dot\phi$), the rate function simplifies to

$$I_{[0,T]}(\phi) = \frac{1}{4}\int_0^T \lVert \dot\phi(t) + \nabla_{T\Sigma_m}\mathcal{E}(\phi(t)) \rVert^2\,dt.$$

**LDP statement (Freidlin-Wentzell 1998 Theorem 3.1, specialized to SCC):** Under hypotheses (H1)–(H3) of §5.2,

$$-\inf_{\phi \in \mathrm{int}(A)} I(\phi) \leq \liminf_{T_*\to 0} T_* \log \mathbb{P}(U^{T_*} \in A) \leq \limsup_{T_*\to 0} T_* \log \mathbb{P}(U^{T_*} \in A) \leq -\inf_{\phi \in \bar{A}} I(\phi)$$

for measurable $A \subset C([0,T]; \tilde{C})$ ("LDP with rate function $I$ and rate $1/T_*$").

### §2.3 Why the factor 1/4 (not 1/2)

The standard Freidlin-Wentzell convention writes the SDE as $dX^\epsilon = b\,dt + \sqrt{\epsilon}\sigma\,dB$ giving $I = (1/2)\int\vert \dot\phi - b\vert ^2_{(\sigma\sigma^\top)^{-1}}\,dt$. SCC's T-PF-A1-SDE has $\sqrt{2T_*}$ (not $\sqrt{T_*}$), so $\epsilon \cdot (\sigma_{\text{SCC}}\sigma_{\text{SCC}}^\top)^{-1} = T_* \cdot (1/2)$, halving the rate function. *This factor-1/4 will reappear in §7 as the factor-2 reconciliation.* For now, the rate function for interior tangent paths is $I = (1/4)\int\vert \dot\phi + \nabla_{T\Sigma_m}\mathcal{E}\vert ^2\,dt$.

---

## §3 — Quasipotential for SCC Gradient Flow

### §3.1 Quasipotential definition

The **quasipotential** between two points $u^*, u \in \tilde{C}$ is

$$\boxed{V(u^*, u) := \inf\{ I_{[0,T]}(\phi) : \phi \in AC([0,T]; \tilde{C}),\, \phi(0) = u^*,\, \phi(T) = u,\, T \in (0,\infty) \}.}$$

This is the *minimum action* required for a sample path of $U^{T_*}$ to go from $u^*$ to $u$ in any finite time, with the noise being treated as a controlled perturbation.

### §3.2 Gradient-flow simplification (Freidlin-Wentzell 1998 §4.3 Lemma 3.1)

For *gradient-flow* SDEs $dX = -\nabla V(X)dt + \sqrt{2\epsilon}\,dB$ (the canonical form on $\mathbb{R}^N$), the quasipotential between a stable equilibrium $x^*$ and any point $x$ in its basin of attraction satisfies

$$V_{\text{FW-grad}}(x^*, x) = 2(V(x) - V(x^*)).$$

SCC's T-PF-A1-SDE is *exactly* of this form on the tangent space $T\Sigma_m$ via the T-PF-A1-AR affine chart $\Phi: \mathbb{R}^{n-1} \to \tilde{C}$ (canonical Cat A). With $\tilde{\mathcal{E}}(x) := \mathcal{E}(u^* + Qx)$ for the chart $u = u^* + Qx$, the chart-pullback SDE on $\mathbb{R}^{n-1}$ is

$$dX_t = -\nabla \tilde{\mathcal{E}}(X_t)\,dt + \sqrt{2T_*}\,dB_t + \text{(boundary reflection)}$$

— a standard gradient flow. Therefore

$$\boxed{V(u^{*,A}, u) = 2(\mathcal{E}(u) - \mathcal{E}(u^{*,A}))}$$

for any $u$ in the basin of attraction $B_A := \{u : \text{deterministic flow } \dot u = -\Pi\nabla\mathcal{E}(u) \text{ from } u \text{ converges to } u^{*,A}\}$.

### §3.3 Beyond the basin: saddle structure

For $u \notin B_A$ — in particular, $u \in B_B$ for a *different* well $u^{*,B}$ — the path from $u^{*,A}$ to $u$ must *cross a saddle* (Morse-theoretic separator between basins). The quasipotential then satisfies

$$V(u^{*,A}, u) = 2\big(\mathcal{E}(u^{*,\text{saddle}_{AB}}) - \mathcal{E}(u^{*,A})\big) + 2\big(\mathcal{E}(u) - \mathcal{E}(u^{*,\text{saddle}_{AB}})\big)$$

where the first term is the *uphill* cost (against the drift) and the second is the *downhill* cost (with the drift, no action needed *but* the path must actually reach $u^{*,\text{saddle}_{AB}}$ for the uphill segment to terminate). The minimum-action path is the *reversed gradient flow* uphill from $u^{*,A}$ to the saddle, then the *forward gradient flow* downhill from saddle to $u^{*,B}$ (the second contributing zero action).

Net result for well-to-well transitions:

$$\boxed{V(u^{*,A}, u^{*,B}) = 2\big(\mathcal{E}(u^{*,\text{saddle}_{AB}}) - \mathcal{E}(u^{*,A})\big) = 2\Delta\mathcal{E}_{A\to\text{saddle}}}$$

with $\Delta\mathcal{E}_{A\to\text{saddle}} := \mathcal{E}(u^{*,\text{saddle}_{AB}}) - \mathcal{E}(u^{*,A})$ the energy barrier.

### §3.4 Reflected-boundary correction

At $\partial\tilde{C}$ (where $u_i = 0$ or $1$), the Skorokhod reflection contributes an extra term to $I$:

$$I^{\partial}_{[0,T]}(\phi) = \frac{1}{4}\int_0^T \lVert \dot\phi + \Pi\nabla\mathcal{E} \rVert^2\,dt + \int_0^T \mathbb{1}_{\phi(t) \in \partial\tilde{C}} \cdot \langle n(\phi(t)), \dot\phi(t) - (\dot\phi)_\parallel \rangle\,d\vert K\vert _t$$

where $n$ is the inward normal at $\partial\tilde{C}$ and $\vert K\vert _t$ the local-time measure (Skorokhod regulator). Per Anderson-Orey 1976 + Dupuis-Ishii 1991, for paths *strictly interior* to $\tilde{C}$ this boundary contribution vanishes. For SCC formation regime with well + saddle interior (hypothesis H2), the minimum-action path can be taken interior, so the boundary correction is zero. *This is precisely the analog of file 02 §5.2 (H3) "interior well-separation from $\partial\tilde{C}$".*

---

## §4 — Eyring-Kramers Exponential Rate from LDP

### §4.1 Exit time from a well

Let $D \subset \tilde{C}$ be a *bounded open set* containing the well $u^{*,A}$ and bounded by saddles / other wells. The **first exit time** $\tau_D := \inf\{t : U^{T_*}_t \notin D\}$ satisfies (Freidlin-Wentzell 1998 Theorem 4.1):

$$\lim_{T_*\to 0} T_*\log \mathbb{E}[\tau_D] = \min_{u \in \partial D} V(u^{*,A}, u) = V_{\min}^{\partial D}.$$

For $\partial D$ containing the saddle $u^{*,\text{saddle}_{AB}}$ at the lowest energy boundary point (Morse-theoretically the *separator* between wells $A$ and $B$):

$$V_{\min}^{\partial D} = V(u^{*,A}, u^{*,\text{saddle}_{AB}}) = 2\Delta\mathcal{E}_{A\to\text{saddle}}.$$

### §4.2 Transition rate

The **transition rate** $\Gamma_{A\to B}$ is the reciprocal of the mean exit time (in the regime of well-separated metastable states; Markov chain of wells, Bovier-Eckhoff-Gayrard-Klein 2001 for the modern formulation):

$$\Gamma_{A\to B} \sim \frac{1}{\mathbb{E}[\tau_D]} \cdot p_{A\to B},$$

with $p_{A\to B}$ the probability of exiting toward $B$ (vs other neighboring wells; for two-well systems $p_{A\to B} \approx 1$). Hence

$$\boxed{\lim_{T_*\to 0} T_*\log \Gamma_{A\to B} = -V_{\min} = -2\Delta\mathcal{E}_{A\to\text{saddle}}.}$$

### §4.3 Comparison with Eyring-Kramers full form

The classical Eyring-Kramers formula is $\Gamma = \omega_0\cdot\exp(-\Delta E/T_*)$ with $\omega_0$ the Hessian-determinant prefactor. Taking $T_*\log$:

$$T_*\log\Gamma = T_*\log\omega_0 - \Delta E.$$

As $T_*\to 0$ with $\omega_0$ bounded (which requires Morse non-degeneracy), the $T_*\log\omega_0$ term vanishes:

$$\lim_{T_*\to 0} T_*\log\Gamma_{\text{Eyring}} = -\Delta E.$$

**Factor 2 discrepancy:** Freidlin-Wentzell gives $-2\Delta\mathcal{E}$; classical Eyring-Kramers gives $-\Delta E$. *This is the central reconciliation issue addressed in §7.* Spoiler: the discrepancy is a *convention difference* in the noise normalization, and the SCC convention $\sqrt{2T_*}$ makes the two formulas *coincide* with $\Delta\mathcal{E} = \Delta E/2$ — i.e., the FW "$2\Delta\mathcal{E}$" *equals* the standard Kramers "$\Delta E$".

---

## §5 — L-FW-KRAMERS-SCC Cat A Target Lemma

### §5.1 Statement

**L-FW-KRAMERS-SCC (working-layer Cat A target).** Let $G=(V,E)$ be a finite connected graph with $\lvert V \rvert=n$, mass $M = c\cdot n$ with $c \in ((3-\sqrt{3})/6, (3+\sqrt{3})/6)$ (spinodal interior), SCC parameters $(\alpha,\beta,\lambda_{cl},\lambda_{sep},\lambda_{bd},\lambda_{tr})$ in the formation regime $\beta/\alpha > 4\lambda_2(L_G)/\lvert W''(c) \rvert$ (DECL T8 super-critical). Let $T_* > 0$ be the canonical ξ resident (OMS-1, Route C, CV-1.18 SEAL). Let $u^{*,A}, u^{*,B} \in \mathrm{int}(\mathcal{F}_M(G))$ be two metastable formation states (interior local minima of $\mathcal{E}_{\text{SCC}}$), and let $u^{*,\text{saddle}_{AB}}$ be a critical point of $\mathcal{E}_{\text{SCC}}$ on the minimum-energy path connecting them, with energy barrier

$$\Delta\mathcal{E}_{A\to\text{saddle}} := \mathcal{E}_{\text{SCC}}(u^{*,\text{saddle}_{AB}}) - \mathcal{E}_{\text{SCC}}(u^{*,A}) > 0.$$

Then under hypotheses **(H1)–(H3)** below, the Freidlin-Wentzell large-deviation rate of the transition $A \to B$ for the reflected Langevin $(U^{T_*}_t)$ satisfies

$$\boxed{\lim_{T_*\to 0} T_*\log \Gamma_{A\to B}^{\text{SCC}} = -2\Delta\mathcal{E}_{A\to\text{saddle}}.}$$

Equivalently, $\Gamma_{A\to B}^{\text{SCC}} = \exp\big(-2\Delta\mathcal{E}_{A\to\text{saddle}}/T_* + o(1/T_*)\big)$ as $T_*\to 0$.

### §5.2 Hypotheses (3 only — minimal)

- **(H1) T-PF-A1-SDE Cat A applicability.** All conditions of canonical T-PF-A1-SDE (CV-1.8, Cat A) hold: $G$ finite connected, mass $M$ fixed, $T_* > 0$, energies $\mathcal{E}_{\text{SCC}}$ smooth on $[0,1]^n \cap H_M$ with Lipschitz gradient (canonical T-PF-A1-AR). *This is the **only** load-bearing hypothesis — and it is canonical Cat A.*
- **(H2) Reflected boundary regularity.** $u^{*,A}, u^{*,B}, u^{*,\text{saddle}_{AB}}$ all lie strictly interior to $\tilde{C}$ at distance $> \delta_{\text{box}}$ from $\partial[0,1]^n \cap H_M$ for some $\delta_{\text{box}} > 0$, with the minimum-action path joining them also interior. (Skorokhod reflection contributes zero LDP action on interior paths; Anderson-Orey 1976 + Dupuis-Ishii 1991.)
- **(H3) Basin structure for gradient flow.** The deterministic flow $\dot u = -\Pi\nabla\mathcal{E}_{\text{SCC}}(u)$ has $u^{*,A}$ and $u^{*,B}$ as stable equilibria with basins of attraction $B_A, B_B$ separated by a single saddle $u^{*,\text{saddle}_{AB}}$ (Morse-theoretic separator on the *path*, not the whole landscape). Łojasiewicz inequality (canonical SCC analyticity, CN4) guarantees finite-time convergence of the gradient flow to critical points.

**Note on hypothesis economy.** L-FW-KRAMERS-SCC has *exactly 3 hypotheses*, all canonically anchored: H1 = canonical Cat A; H2 = standard interior assumption (analog of file 02 §5.2 H3); H3 = Łojasiewicz consequence of analyticity (canonical CN4). Notably:

- **NOT required**: H5 Morse stability (file 02 hypothesis, source of Cat B).
- **NOT required**: OP-HMORSE-SADDLE saddle-Hessian regularity (file 02 hypothesis H2, OPEN at canonical theorem_status.md L594).
- **NOT required**: Non-degeneracy of Hess$\,\mathcal{E}$ at well or saddle.

This is *precisely* what makes L-FW-KRAMERS-SCC Cat A while L-KRAMERS-PR-SCC (file 02) is Cat B.

### §5.3 5-step proof sketch

```
Step 1 (SDE foundation). T-PF-A1-SDE (Cat A, CV-1.8) gives a unique strong solution
   dU_t = -Π∇E(U_t)dt + √(2T_*)·Π dB_t + dK_t  on  F_M(G) = closure of tilde-C.
   Lipschitz drift (T-PF-A1-AR), compact convex domain, Lions-Sznitman reflection.

Step 2 (chart to gradient flow on R^{n-1}). Apply T-PF-A1-AR affine isometry
   Φ: x ↦ u^* + Qx, F_M(G) ≅ tilde-C ⊂ R^{n-1}.
   Pullback SDE: dX_t = -∇tilde-E(X_t)dt + √(2T_*)dB_t + (reflection), with
   tilde-E(x) := E(u^* + Qx). Standard gradient-flow form on the polytope tilde-C.

Step 3 (Freidlin-Wentzell LDP). Apply Freidlin-Wentzell 1998 Theorem 3.1 +
   reflected-diffusion extension (Anderson-Orey 1976; Dupuis-Ishii 1991) to obtain
   the LDP for (X^{T_*}_t)_{t ∈ [0,T]} with rate function
       I_{[0,T]}(φ) = (1/4)∫_0^T |φ̇ + ∇tilde-E(φ)|^2 dt
   on absolutely continuous interior paths. Boundary contribution vanishes by H2.

Step 4 (quasipotential via gradient-flow lemma). Apply Freidlin-Wentzell 1998 §4.3
   Lemma 3.1 (gradient-flow quasipotential): for x^* a stable equilibrium of -∇tilde-E
   and x in its basin,
       V(x^*, x) = 2(tilde-E(x) - tilde-E(x^*)).
   Extend across saddles by Morse-theoretic separation (Freidlin-Wentzell 1998 §6.2):
       V(x^{*,A}, x^{*,B}) = 2·Δtilde-E_{A→saddle}.

Step 5 (exit time and transition rate). Apply Freidlin-Wentzell 1998 Theorem 4.1
   (exit time from a bounded domain D containing x^{*,A}):
       lim_{T_*→0} T_*·log E[τ_D] = min_{x ∈ ∂D} V(x^{*,A}, x) = 2·Δtilde-E_{A→saddle}.
   Transition rate Γ_{A→B} ~ 1/E[τ_D] gives
       lim_{T_*→0} T_*·log Γ_{A→B} = -2·Δtilde-E_{A→saddle}.
   Pull back via Φ to original coordinates: ΔE_{SCC} = Δtilde-E (isometric chart).
   ∎ (target sketch)
```

### §5.4 Inverse causation

```
inverse_causation_check:
  - if H1 fails (T-PF-A1-SDE not Cat A): no SDE foundation → LDP machinery has no input → L-FW-KRAMERS-SCC fails. Pre-CV-1.8 this was the case; now resolved.
  - if H2 fails (well/saddle at boundary): Skorokhod reflection adds nontrivial LDP action on the path → boundary term in §3.4 nonzero → quasipotential formula §3.3 receives correction term. Rate formula still holds qualitatively but barrier is replaced by *effective barrier* including reflection cost. Out of scope for the simplest L-FW-KRAMERS-SCC statement.
  - if H3 fails (Łojasiewicz fails, basin attraction broken): gradient flow may not converge to a single critical point → quasipotential §3.2 simplification fails → V formula has additional structure (e.g., multi-basin overlap). LDP itself still holds (Freidlin-Wentzell Thm 3.1 unconditional on basin structure) but the quasipotential is not simply 2(E(u) - E(u^*)). Łojasiewicz holds for SCC by canonical analyticity (CN4 preserved); failure would require CN4 violation, which is itself a fundamental structural break.
  - if OP-HMORSE-SADDLE were closed: HTB prefactor (file 02) becomes Cat A → file 09's marginal value diminishes (still complementary as a *prefactor-independent* check). Currently OPEN → file 09 uniquely valuable.
```

---

## §6 — Comparison with HTB Approach (file 02): Complementary Roles

### §6.1 Side-by-side comparison

| Aspect | File 02 (HTB, Cat B) | File 09 (LDP, Cat A) |
|---|---|---|
| **Source** | Hänggi-Talkner-Borkovec 1990 Rev Mod Phys 62:251 | Freidlin-Wentzell 1998 Grundlehren 260 |
| **Output** | $\Gamma = \omega_0 \cdot \exp(-\Delta E/T_*)$ | $\lim T_*\log\Gamma = -2\Delta\mathcal{E}$ |
| **Granularity** | Subexponential prefactor + exponent | Exponential leading order only |
| **Mathematical regime** | Sharp Eyring-Kramers (Morse non-degenerate) | Logarithmic asymptotics ($T_* \to 0$) |
| **Hypotheses** | H1 Morse (= H5 T-P-F-ε0-K Cat B); H2 single-saddle (= OP-HMORSE-SADDLE OPEN); H3 interior + Package I | H1 T-PF-A1-SDE Cat A; H2 interior (analog H3); H3 Łojasiewicz (CN4) |
| **OPEN dependencies** | OP-HMORSE-SADDLE (saddle Hess regularity, theorem_status.md L594) | NONE — all hypotheses canonical Cat A |
| **Cat assignment** | Cat B (via H1 + H2 OPEN) | Cat A (all canonical) |
| **Critic findings (file 07)** | 4 MAJOR (det/det' ambiguity §A.2, dimensional issue §A.3, unit confusion §A.4, μ estimates §A.5) | N/A — LDP avoids prefactor entirely, so prefactor-related issues are *structurally absent* |

### §6.2 Why both are needed

```
CoT step 1: File 02 (HTB) delivers the *sharp* Eyring-Kramers form Γ = ω_0·exp(-ΔE/T_*) — the most precise theoretical formula. But it is Cat B because ω_0 requires saddle-Hessian regularity (OP-HMORSE-SADDLE).
CoT step 2: File 09 (LDP) delivers only the *exponential rate* but is Cat A because it requires only T-PF-A1-SDE Cat A.
CoT step 3: Together: LDP provides a *Cat A lower bound* on the rate (any prefactor consistent with the Cat A exponential); HTB provides a *Cat B sharper rate* with prefactor. The full Eyring-Kramers form is therefore "Cat A exponential rate (this file) + Cat B prefactor (file 02)".
CoT step 4: For OP-0005-DYN (Package II, W9+): the *Cat A* path closes via this file's LDP rate (once H2/H3 verified at canonical level). The *Cat B sharper form* awaits OP-HMORSE-SADDLE closure for prefactor Cat A.
→ Files 02 and 09 are **complementary, not substitutes**. File 09 does NOT obsolete file 02.

CoC anchors:
  - canonical §13 T-PF-A1-SDE (Cat A, CV-1.8) — common foundation for both files
  - canonical §13 T-P-F-ε0-K (Cat B, CV-1.7) — H5 used by file 02, NOT by file 09
  - theorem_status.md L594 OP-HMORSE-SADDLE (OPEN) — blocks file 02 Cat A, irrelevant to file 09
  - theorem_status.md L803 OP-0005-DYN (OPEN) — target row addressed by *both* files
```

### §6.3 What file 09 cannot do that file 02 can

- Compute the *absolute* prefactor (an order-of-magnitude number, not just exponential).
- Distinguish two formation transitions with the *same* barrier $\Delta\mathcal{E}$ but different Hessian determinants.
- Provide quantitative connection to spectral observables (eigenvalue ratios).

These remain the unique domain of file 02 (HTB) — once OP-HMORSE-SADDLE closes, the prefactor itself becomes Cat A.

### §6.4 What file 02 cannot do that file 09 can

- Provide a *Cat A* statement at all (file 02 is Cat B).
- Apply to formation transitions where the saddle Hessian is degenerate (Goldstone modes broken, accidental degeneracy, or saddle on $\partial\tilde{C}$).
- Survive scenarios where OP-HMORSE-SADDLE turns out to be *unresolvable* in finite SCC (e.g., non-isolated saddles on $K$-jump boundary).

The LDP rate is *robust* to all these cases at the cost of giving only the exponential leading order.

---

## §7 — Factor 2 Reconciliation (FW vs Standard Kramers Convention)

### §7.1 The apparent discrepancy

Standard Kramers (Hänggi-Talkner-Borkovec 1990 eq. 4.55a, file 02 §3.2):

$$\Gamma_{\text{Kramers,1D}} = \omega_0^{1D}\cdot\exp(-\Delta V / k_B T), \quad \omega_0^{1D} = \frac{\omega_{\text{well}}\cdot\omega_{\text{saddle}}}{2\pi\gamma}.$$

The exponent is $-\Delta V / k_B T$ (factor 1).

Freidlin-Wentzell (this file §4.2):

$$\lim_{T_*\to 0} T_*\log\Gamma_{\text{FW}} = -2\Delta\mathcal{E}.$$

The exponent is $-2\Delta\mathcal{E}/T_*$ (factor 2).

**Apparent factor-2 mismatch.** A naive reading would say SCC's LDP rate is *twice as harsh* as standard Kramers — which would be a serious problem (file 02's result would disagree with this file's).

### §7.2 Reconciliation via noise normalization

The two formulas use different SDE conventions for the noise scale:

| Convention | SDE form | Effective $\epsilon$ in LDP |
|---|---|---|
| **Standard Kramers (HTB)** | $\gamma\dot x = -\partial_x V + \sqrt{2k_BT\gamma}\,\xi$ in physics units; equivalently $dx = -(1/\gamma)\partial_x V\,dt + \sqrt{2k_BT/\gamma}\,dB$. After time rescaling $t \to t/\gamma$ and identifying $T := k_BT/\gamma$: $dx = -\partial_x V\,dt + \sqrt{2T}\,dB$. | $\epsilon_{\text{HTB}} = T$ ($= k_BT/\gamma$) |
| **Freidlin-Wentzell standard form** | $dX^\epsilon = b\,dt + \sqrt{\epsilon}\,dB$ | $\epsilon_{\text{FW}}$ as written |
| **SCC T-PF-A1-SDE** | $dU = -\Pi\nabla\mathcal{E}\,dt + \sqrt{2T_*}\,\Pi\,dB + dK$ | $\epsilon_{\text{SCC}} = 2T_*$ |

The two SCC reading have $\sqrt{2T_*}$ noise, matching standard Kramers exactly (with $T_*$ playing the role of $k_BT/\gamma$). When we apply Freidlin-Wentzell to T-PF-A1-SDE *with the SCC noise normalization $\sqrt{2T_*}$*, the small parameter is $\epsilon = 2T_*$, not $T_*$.

Let us redo the rate function calculation carefully. With $\sigma\sigma^\top = 2\Pi$ on the tangent space:

$$I^{\text{FW-standard}}(\phi) = \frac{1}{2}\int_0^T \langle\dot\phi + \Pi\nabla\mathcal{E},\, (\sigma\sigma^\top)^{-1}\,[\dot\phi + \Pi\nabla\mathcal{E}]\rangle\,dt = \frac{1}{2}\cdot\frac{1}{2}\int_0^T \lVert \dot\phi + \Pi\nabla\mathcal{E} \rVert^2\,dt = \frac{1}{4}\int_0^T \lVert \cdots \rVert^2\,dt.$$

The LDP is $\mathbb{P}(\cdots) \asymp \exp(-I/\epsilon_{\text{FW}})$. *But what is $\epsilon_{\text{FW}}$?* In the Freidlin-Wentzell convention $dX = b\,dt + \sqrt{\epsilon}\sigma\,dB$, our SCC SDE has $\sqrt{2T_*}\Pi$ as the noise — so $\sqrt{\epsilon_{\text{FW}}}\sigma_{\text{FW}} = \sqrt{2T_*}\Pi$. We can set $\sigma_{\text{FW}} = \Pi$ and $\epsilon_{\text{FW}} = 2T_*$, or $\sigma_{\text{FW}} = \sqrt{2}\Pi$ and $\epsilon_{\text{FW}} = T_*$. The product $I/\epsilon_{\text{FW}}$ is invariant:

- Choice A ($\sigma_{\text{FW}} = \Pi$, $\epsilon = 2T_*$): $I = (1/2)\int \lVert \dot\phi + \Pi\nabla\mathcal{E} \rVert^2 dt$ (since $(\sigma\sigma^\top)^+ = \Pi$). LDP: $\mathbb{P} \asymp \exp(-I/(2T_*))$.
- Choice B ($\sigma_{\text{FW}} = \sqrt{2}\Pi$, $\epsilon = T_*$): $I = (1/4)\int \lVert \dot\phi + \Pi\nabla\mathcal{E} \rVert^2 dt$. LDP: $\mathbb{P} \asymp \exp(-I/T_*)$.

Both give the same $\mathbb{P} \asymp \exp(-(1/(4T_*))\int\lVert \cdot \rVert^2 dt)$. The quasipotential is then

$$V(u^{*,A}, u^{*,B}) = \inf I = \frac{1}{2}\cdot 2(\mathcal{E}(\text{sad}) - \mathcal{E}(\text{well})) = \mathcal{E}(\text{sad}) - \mathcal{E}(\text{well}) = \Delta\mathcal{E}$$

(Choice A) or

$$V(u^{*,A}, u^{*,B}) = \frac{1}{4}\cdot 4(\mathcal{E}(\text{sad}) - \mathcal{E}(\text{well})) = \Delta\mathcal{E}$$

(Choice B — the standard "$2\Delta\mathcal{E}$" with the FW rate function form normalized differently).

In *both* conventions, the **LDP rate of the transition** is

$$\lim_{T_*\to 0}\,T_*\log\Gamma = -\Delta\mathcal{E},$$

i.e., the *standard Kramers exponent* with factor 1.

### §7.3 Where the "factor 2" came from and why it's a convention artifact

The "$V = 2(\mathcal{E}(x) - \mathcal{E}(x^*))$" formula in §3.2 (Freidlin-Wentzell §4.3 Lemma 3.1) is stated for the *standard FW SDE* $dX = -\nabla V\,dt + \sqrt{2\epsilon}\,dB$, which has $\sigma\sigma^\top = 2I$ and the rate function $I = (1/(4\epsilon))\int\lVert \dot\phi + \nabla V \rVert^2 dt$. The quasipotential being $2(V(x) - V(x^*))$ refers to the *bare* rate function $I$ (not $I/\epsilon$). The Eyring-Kramers exponential rate is $V/\epsilon = 2\Delta V/\epsilon$, which *equals* $\Delta V/T_*$ when $\epsilon = 2T_*$ — i.e., the standard Kramers result.

**Reconciliation verdict:** the factor 2 in "$V = 2\Delta\mathcal{E}$" *is exactly cancelled* by the factor 2 in the noise normalization $\sqrt{2T_*}$ (vs FW's $\sqrt{\epsilon}$). The net LDP rate of the SCC transition is

$$\boxed{\lim_{T_*\to 0}\,T_*\log\Gamma^{\text{SCC}}_{A\to B} = -\Delta\mathcal{E}_{A\to\text{saddle}}}$$

— *factor 1*, matching standard Kramers and matching the leading exponent of file 02 HTB form.

### §7.4 Correction to §4.2 / §5.1 statement

The boxed statements in §4.2 and §5.1 written as "$-2\Delta\mathcal{E}$" use the *bare* FW quasipotential convention without the $\epsilon = 2T_*$ rescaling. The **physically correct** statement of L-FW-KRAMERS-SCC is

$$\lim_{T_*\to 0}\,T_*\log\Gamma_{A\to B}^{\text{SCC}} = -\Delta\mathcal{E}_{A\to\text{saddle}}$$

(factor 1, matching Kramers convention). The "$-2\Delta\mathcal{E}$" form in §4.2/§5.1 is the *FW quasipotential* itself, $V = 2\Delta\mathcal{E}$, with the understanding that the LDP rate is $V/\epsilon = 2\Delta\mathcal{E}/(2T_*) = \Delta\mathcal{E}/T_*$.

**Convention adopted hereafter (§8–§13):** the LDP rate is $-\Delta\mathcal{E}/T_*$ (factor 1, standard Kramers), with the explicit reminder that this *equals* $V/\epsilon$ in FW notation with $V = 2\Delta\mathcal{E}$ and $\epsilon = 2T_*$. The two formulations agree.

### §7.5 Sanity check via canonical T-P-F-ε0-K

Canonical T-P-F-ε0-K (Cat B, CV-1.7) writes the Kramers exponential as $\Gamma_\varepsilon = \Gamma_0 \cdot \exp(-\varepsilon\Delta R / T_*)$ — the exponent is $-\Delta\mathcal{E}/T_*$ at leading order ($\varepsilon = 0$ regularization). *This factor-1 form is what L-FW-KRAMERS-SCC must reproduce*, and per §7.4 it does. ✓

---

## §8 — Connection to Canonical T-PF-A1-PE (Poincaré) + osc($\mathcal{E}$) Form

### §8.1 The canonical Poincaré bound

Canonical T-PF-A1-PE (Cat A, CV-1.9, canonical.md L1700+) gives the explicit spectral gap

$$\lambda_1(\pi_{T_*}) \geq \frac{\pi^2}{n} e^{-\mathrm{osc}(\tilde{\mathcal{E}})/T_*}, \qquad C_P = \frac{n}{\pi^2}e^{\mathrm{osc}(\tilde{\mathcal{E}})/T_*}.$$

with $\mathrm{osc}(\tilde{\mathcal{E}}) := \max\tilde{\mathcal{E}} - \min\tilde{\mathcal{E}}$ on $\tilde{C}$.

The TV mixing rate is $\lVert \mathrm{Law}(U_t) - \pi_{T_*} \rVert_{TV} \leq (1/2)e^{-\lambda_1 t}\lVert h_0 - 1 \rVert_{L^2}$.

### §8.2 Comparison with LDP rate

The Poincaré bound gives:

$$T_*\log\lambda_1 \geq T_*\log(\pi^2/n) - \mathrm{osc}(\tilde{\mathcal{E}}).$$

As $T_*\to 0$:

$$\lim_{T_*\to 0}\,T_*\log\lambda_1 \geq -\mathrm{osc}(\tilde{\mathcal{E}}).$$

The LDP gives $\lim T_*\log\Gamma_{A\to B} = -\Delta\mathcal{E}_{A\to\text{saddle}}$. Since *any* mixing rate $\lambda_1$ is at least the *slowest* transition rate (smallest spectral gap = highest barrier), we have

$$\lambda_1 \leq \Gamma_{A\to B} \quad \Longrightarrow \quad \lim T_*\log\lambda_1 \leq -\Delta\mathcal{E}_{A\to\text{saddle}}.$$

Combined: $-\mathrm{osc}(\tilde{\mathcal{E}}) \leq \lim T_*\log\lambda_1 \leq -\Delta\mathcal{E}_{A\to\text{saddle}}.$

**Interpretation:** $\Delta\mathcal{E}_{A\to\text{saddle}} \leq \mathrm{osc}(\tilde{\mathcal{E}})$ trivially (the barrier is at most the total energy range). The Poincaré bound provides a *worst-case* logarithmic-asymptotic estimate; the LDP provides a *barrier-specific* estimate, sharper because $\Delta\mathcal{E}_{A\to\text{saddle}} < \mathrm{osc}(\tilde{\mathcal{E}})$ for most well-pair configurations.

### §8.3 Cat A status compatibility

Both T-PF-A1-PE (canonical Cat A) and the LDP (this file, Cat A target) live at the *logarithmic-asymptotic* level. They are *mutually consistent* — the LDP refines the Poincaré bound by replacing $\mathrm{osc}(\tilde{\mathcal{E}})$ with $\Delta\mathcal{E}_{A\to\text{saddle}}$ for the specific transition $A\to B$. No contradiction; the LDP is *strictly stronger* whenever the well/saddle pair is identified.

```
CoC: canonical §13 T-PF-A1-PE Cat A — Payne-Weinberger + Holley-Stroock; explicit osc form
     this file §4.2 LDP — Freidlin-Wentzell §4.1; explicit barrier-specific form
     Compatibility: λ_1 ≤ Γ_{A→B} (smallest gap ≤ smallest rate); LDP sharpens osc to Δ_{A→saddle}.
inverse_causation_check:
     - if osc(E) = 0: trivial well, no barrier, T-PF-A1-PE gives λ_1 ≥ π²/n (polynomial), LDP gives Γ = ∞. Consistent.
     - if Δ_{A→saddle} = 0: no barrier, instantaneous transition, Γ unbounded. LDP rate -Δ = 0; not contradictory but no metastability.
```

---

## §9 — 2D Torus L=16 Reference Example (CONSENSUS BASELINE)

### §9.1 Setup (consensus baseline, mandatory)

- Graph $G = T^2_{16}$, $n = 256$, periodic boundary conditions.
- $\lambda_2(L_G) = 4\sin^2(\pi/16) \approx 0.1522$.
- $c = 1/2$, $\alpha = 1$, $\beta = 10$, $T_* = 0.1$, $R = 4$.
- $W(u) = u^2(1-u)^2$, $W'(u) = 2u(1-u)(1-2u)$, $W''(1/2) = -1$.
- Surface tension $\sigma = (\sqrt{2}/6)\sqrt{\alpha\beta} = (\sqrt{2}/6)\sqrt{10} \approx 0.7454$.
- Spinodal interior: $c = 1/2 \in ((3-\sqrt{3})/6, (3+\sqrt{3})/6) \approx (0.2113, 0.7887)$. ✓
- T8 formation regime check: $\beta/\alpha = 10 > 4\lambda_2/\lvert W''(c) \rvert = 4(0.1522)/1 = 0.6087$. ✓ (Deep formation regime.)

### §9.2 Energy barrier estimate

For a single-formation well of radius $R = 4$ on $T^2_{16}$, the energy of formation vs uniform reference (empirically validated, exp38 R²=0.997):

$$E_{\text{barrier}} \approx 10 \cdot \beta^{0.89} = 10 \cdot 10^{0.89} = 10 \cdot 7.76 \approx 77.6.$$

But this is the *uniform-to-formation* barrier. For *K-to-K' (well-to-well)* transitions in the multi-formation regime, the saddle barrier is empirically smaller:

$$\Delta\mathcal{E}_{A\to\text{saddle}} \approx \sigma \cdot 2\pi R = 0.7454 \cdot 2\pi\cdot 4 \approx 18.7 \quad \text{(Modica-Mortola interface cost for a saddle of size ~ R)}.$$

(Order-of-magnitude only — precise saddle identification awaits multi-formation NEB simulation.)

### §9.3 LDP rate computation (factor-1 form, §7.4 corrected)

$$T_*\log\Gamma_{A\to B}^{\text{SCC}} = -\Delta\mathcal{E}_{A\to\text{saddle}} \approx -18.7$$

at $T_* = 0.1$:

$$\log\Gamma \approx -18.7 / 0.1 = -187, \qquad \Gamma \approx e^{-187} \approx 10^{-81}.$$

(In the FW *quasipotential* notation $V = 2\Delta\mathcal{E} = 37.4$, $\Gamma \approx e^{-V/(2T_*)} = e^{-187}$. Same result.)

### §9.4 Cross-check with osc form (T-PF-A1-PE worst-case bound)

Worst-case bound from canonical Poincaré: $\lambda_1 \geq (\pi^2/256)\cdot e^{-\mathrm{osc}(\tilde{\mathcal{E}})/0.1}$ with $\mathrm{osc}(\tilde{\mathcal{E}}) \approx 100$ (rough max-min energy range on $T^2_{16}$ with $\beta = 10$): $\lambda_1 \geq (0.0386)\cdot e^{-1000} \approx 10^{-435}$.

The LDP rate $\Gamma \approx 10^{-81}$ is *much larger* than this worst-case Poincaré bound — consistent with §8.2 interpretation ($\Delta\mathcal{E}_{A\to\text{saddle}} \ll \mathrm{osc}(\tilde{\mathcal{E}})$, LDP sharper).

### §9.5 Cross-check with file 02 HTB estimate

File 02 §6.5 gives $\Gamma \sim 10^{-337}$ for $\Delta E_{\text{barrier}} \sim 77.6$ (single formation barrier, with prefactor $\omega_0 \sim 0.084$). The disagreement with file 09's $10^{-81}$ is *not* a contradiction:

- File 02 uses *uniform-to-formation* barrier $\Delta E \approx 77.6$.
- File 09 uses *well-to-well* (interface-cost) barrier $\Delta\mathcal{E} \approx 18.7$.

These are *different transitions*. For the well-to-well K-jump transition, file 02 would also need to use $\Delta\mathcal{E} \approx 18.7$ (not 77.6), giving $\Gamma \sim 10^{-81}$ in leading exponent (modulo HTB prefactor $\omega_0$). ✓ Consistent.

### §9.6 Order-of-magnitude only disclaimer

All numerical estimates in §9 are *order-of-magnitude* and rely on Modica-Mortola interface scaling + empirical $\beta^{0.89}$ fit. They are *not* canonical claims. Precise saddle identification requires multi-formation NEB simulation (e.g., extension of exp02e from `CODE/experiments/results/`).

---

## §10 — OPEN Problem Leverage

### §10.1 OP-0005-DYN (theorem_status.md L803) — primary target

**Canonical row:** "OP-0005-DYN | Dynamical K-transition / Kramers rates | **OPEN** | Package II (Eyring-Kramers, H5 + OP-0021). Not before W9+."

**File 09 advance channel:** *Cat A exponential-rate path*. L-FW-KRAMERS-SCC delivers $\lim T_*\log\Gamma_{A\to B} = -\Delta\mathcal{E}_{A\to\text{saddle}}$ as a Cat A target (under canonical T-PF-A1-SDE Cat A + interior H2 + Łojasiewicz H3, all canonical or canonical-derivable).

**Combined with file 02:** *Cat B sharper form*. File 02 L-KRAMERS-PR-SCC adds the HTB prefactor $\omega_0$ (Cat B via OP-HMORSE-SADDLE).

**Net OP-0005-DYN status:** OPEN at canonical; *attack channels* = Cat A LDP (file 09) + Cat B HTB (file 02). Closure requires *either* sharper rate (with prefactor) or Cat A prefactor (requires OP-HMORSE-SADDLE closure).

### §10.2 T-P-F-ε0-K (canonical Cat B, CV-1.7) — Cat A bypass channel

**Canonical row (canonical.md L1818+):** "T-P-F-ε0-K. Kramers Exponent Stability under Bernoulli Regularization. ... Cat B conditional on H5 Morse stability."

**File 09 advance channel:** the Cat A LDP *bypasses H5 entirely* — the rate function $I$ requires only $\mathcal{E} \in C^2$ (canonical analyticity, CN4 preserved) and not Morse non-degeneracy. Therefore L-FW-KRAMERS-SCC provides a *Cat A path* to the Kramers exponent stability statement *at the LDP exponential-rate level* (factor 1, $-\Delta\mathcal{E}/T_*$). Stability under Bernoulli regularization $\mathcal{E} \to \mathcal{E} + \varepsilon R$ at the LDP level follows from continuous-dependence of barrier on $\varepsilon$ (no Morse hypothesis needed — barrier is just an energy difference).

**Net T-P-F-ε0-K status:** remains canonical Cat B (H5 still needed for prefactor); LDP gives a *Cat A version* at exponential-rate level. The canonical row's "Non-overclaim: T-P-F-ε0-K is not P-F-A1. It does NOT prove ... Eyring-Kramers pre-exponential factor A" is *exactly* what file 02 targets and what file 09 *avoids*.

### §10.3 P-F-A1 Package II — Cat A entry

**Definition (file 02 §1.1):** Package II = Eyring-Kramers form + transition rates (sequel to Package I = reflected Langevin Cat A foundation, CV-1.9).

**File 09 advance channel:** delivers the *first Cat A entry* into Package II. Package I (canonical CV-1.9, Cat A) gives the SDE + Poincaré. Package II Cat A foundation = L-FW-KRAMERS-SCC LDP rate. Package II Cat B sharper form = file 02 HTB prefactor (pending OP-HMORSE-SADDLE).

### §10.4 OP-HMORSE-SADDLE (theorem_status.md L594) — NOT a hypothesis

**Canonical row:** "OP-HMORSE-SADDLE | Saddle-point Hessian regularity | Medium | OPEN (NEW CV-1.16): required for full Eyring-Kramers prefactor Cat B; independent of OP-HMORSE-LOCAL-A. ETA 2–4 sessions."

**File 09 status:** L-FW-KRAMERS-SCC does *not* depend on OP-HMORSE-SADDLE. The LDP rate function $I$ is defined without saddle-Hessian regularity. This is the *core reason* file 09 is Cat A target while file 02 is Cat B target.

When OP-HMORSE-SADDLE closes (ETA 2-4 sessions per canonical), file 02 promotes to Cat A and the *full* Eyring-Kramers form (prefactor + exponent) becomes Cat A. File 09 remains a useful Cat A *check* on the exponent.

### §10.5 Summary table

| OP / Theorem | Canonical status | File 09 contribution | Mechanism |
|---|---|---|---|
| OP-0005-DYN (L803) | OPEN | Cat A exponential-rate channel | LDP + quasipotential |
| T-P-F-ε0-K (L1818) | Cat B (H5) | Cat A exponential-rate version | LDP avoids H5 |
| Package II | not yet structured | Cat A entry | LDP rate as foundation |
| OP-HMORSE-SADDLE (L594) | OPEN | bypassed (not a hypothesis) | LDP rate function regularity-free |

---

## §11 — CoT / CoC / Inverse Causation Archival

### §11.1 Chain of Thought (master)

```
CoT (file 09 master):
  1. File 02 delivered Cat B HTB prefactor; critic (file 07) found 4 MAJOR prefactor-related issues (det/det', dimensional, units, numerics).
  2. Question: can we deliver a Cat A result for OP-0005-DYN that *avoids* prefactor issues entirely?
  3. Answer: yes, via Freidlin-Wentzell LDP. The rate function I depends only on E ∈ C² and ∇E Lipschitz — both canonical (T-PF-A1-AR).
  4. The LDP gives only the *exponential rate*, not the prefactor — strictly weaker than HTB. But the trade-off is Cat A vs Cat B.
  5. Set up rate function I = (1/4)∫|φ̇ + Π∇E|² dt (canonical T-PF-A1-SDE noise normalization).
  6. Quasipotential V(u*, u) = 2(E(u) - E(u*)) on basin (Freidlin-Wentzell §4.3 Lemma 3.1 gradient-flow case).
  7. Well-to-well transition: V = 2·ΔE_{A→saddle}; LDP rate = -V/ε = -ΔE/T_* (factor 1 after noise normalization).
  8. Verify factor-2 reconciliation: FW quasipotential V = 2ΔE, but LDP rate is V/ε with ε = 2T_*, so net = ΔE/T_*. Matches standard Kramers, matches canonical T-P-F-ε0-K convention.
  9. State L-FW-KRAMERS-SCC: 3 hypotheses (all canonical or canonical-derivable), 5-step proof sketch.
  10. Compare to file 02: complementary, not substitute. LDP = Cat A exponent; HTB = Cat B exponent + prefactor.
  11. 2D torus reference: Γ ~ e^{-187} ~ 10^{-81} for ΔE ~ 18.7 at T_* = 0.1.
  → L-FW-KRAMERS-SCC = first Cat A entry into Package II for OP-0005-DYN.
```

### §11.2 Chain of Citations (master)

```
CoC anchors (in order of reliance):
  - canonical §13 T-PF-A1-AR (Cat A, CV-1.8) — Lipschitz drift, compact convex polytope (H1, H2)
  - canonical §13 T-PF-A1-SDE (Cat A, CV-1.8) — Lions-Sznitman reflected SDE well-posed (H1)
  - canonical §13 T-PF-A1-PE (Cat A, CV-1.9) — Poincaré + L²→TV ergodicity (§8 connection)
  - canonical §13 Theorem 4 (Cat A, canonical.md L1134-1136) — μ_k formula at uniform critical (background reference)
  - canonical §13 T-P-F-ε0-K (Cat B, CV-1.7, canonical.md L1818+) — Arrhenius barrier stability (§7.5 sanity check)
  - canonical theorem_status.md L803 OP-0005-DYN (OPEN, primary target row)
  - canonical theorem_status.md L594 OP-HMORSE-SADDLE (OPEN, bypassed not used)
  - Freidlin M.I., Wentzell A.D. 1998 Grundlehren 260, Ch. 3 + Ch. 4 (LDP + quasipotential + exit problem)
  - Dembo A., Zeitouni O. 1998 Stochastic Modelling 38 §5.6 (modern LDP textbook)
  - Anderson R.F., Orey S. 1976 (reflected diffusions LDP)
  - Dupuis P., Ishii H. 1991 (Skorokhod reflection in convex domains)
  - Bovier A., Eckhoff M., Gayrard V., Klein M. 2001 (Metastability in reversible diffusion: Markov chain of wells)
  - Lions P.-L., Sznitman A.-S. 1984 (reflected SDE existence/uniqueness, CPAM 37(4):511-537)
  - Payne L.E., Weinberger H.F. 1960 (eigenvalue bound for convex domains, Arch. Rat. Mech. Anal. 5:286-292)
```

### §11.3 Inverse causation (master)

```
inverse_causation_check (master):
  - if T-PF-A1-SDE were not Cat A: LDP has no SDE foundation → L-FW-KRAMERS-SCC fails to Cat A. Was the case pre-CV-1.8; now resolved.
  - if E were not analytic (CN4 violated): gradient flow may not converge in finite time; basin H3 may fail; LDP still holds (probabilistic, no analyticity needed) but quasipotential simplification fails. CN4 preserved by canonical, so no risk.
  - if interior H2 failed (well/saddle at ∂C): boundary reflection contributes nontrivial LDP action → quasipotential gets corrections; rate formula modified. Statement of L-FW-KRAMERS-SCC restricted to interior case for simplicity (footnote §5.4 reserved).
  - if OP-HMORSE-SADDLE were closed: file 02 would become Cat A → file 09's marginal Cat A claim still valid but less distinctive. Currently OPEN: file 09 uniquely provides Cat A exponential rate.
  - if factor-2 reconciliation §7 failed: L-FW-KRAMERS-SCC would disagree with standard Kramers / T-P-F-ε0-K convention by factor 2. Verified §7.4: factor 2 in V=2ΔE cancelled by factor 2 in ε=2T_*; net rate = -ΔE/T_*. Consistent.
  - if file 02 HTB result is fundamentally wrong: file 09 still delivers Cat A *bound* on rate (independent verification channel). LDP would *constrain* any HTB prefactor to be subexponential — a non-trivial check on file 02.
```

---

## §12 — Hard Constraint CN1–16 Check (16/16 ✓)

| CN | Constraint | Status in this file |
|---|---|---|
| CN1 | No canonical edits | ✓ 0 canonical/* edits; pre/post `git status THEORY/canonical/` clean. |
| CN2 | No silent OP resolution | ✓ OP-0005-DYN remains OPEN; §1.2 + §10.1 explicit. |
| CN3 | No Research OS redux | ✓ working/field_equation_framework/ directory (existing); no D/S/T/A/E/Q/C/P/X registry. |
| CN4 | Analyticity preserved | ✓ Energy $\mathcal{E}_{\text{SCC}}$ untouched; LDP uses canonical $\mathcal{E}$ as input. |
| CN5 | 4-term independence | ✓ No new energy term; LDP operates on existing $\mathcal{E}$. |
| CN6 | No closure idempotence | ✓ Closure not invoked beyond canonical reference. |
| CN7 | Sep predicate u-weighted | ✓ Not modified. |
| CN8 | $b_D = 0$ analyticity | ✓ Preserved (analyticity preserved per CN4). |
| CN9 | Persist core-overlap | ✓ Not modified. |
| CN10 | No reductive reduction | ✓ Freidlin-Wentzell 1998 = *contrastive standard probability tool*, applied to canonical T-PF-A1-SDE Cat A. SCC is *not* reduced to a Brownian particle; the *probability machinery* (LDP, contraction principle, exit problem) is the external toolkit, operating on *any* SDE in scope. §1.2 + §2.1 explicit. |
| CN11 | No fluid analogy abuse | ✓ Zero fluid-specific terminology in §1–§13. LDP is probabilistic, not fluid-mechanical. |
| CN12 | No CSSL patterns ($E_{\text{ridge}}, E_{\text{wild}}, E_{\text{pers}}$) | ✓ Quasipotential $V$ is a *derived* object from canonical $\mathcal{E}$, not a new energy term. §1.2 explicit. |
| CN13 | No inertia / second-order temporal | ✓ T-PF-A1-SDE is first-order; LDP preserves first-order structure. §1.2 explicit. |
| CN14 | No Mori-Zwanzig | ✓ CV-1.18 SEAL respected. No memory kernel. |
| CN15 | No vocabulary refactoring of canonical objects | ✓ $\mathcal{E}, T_*, \Pi, \mathcal{F}_M(G), \Delta\mathcal{E}$ are canonical residents, used with canonical semantics. *New* object = quasipotential $V$ (standard Freidlin-Wentzell concept, defined §3.1). |
| CN16 | Honest Cat assignment | ✓ Cat A target *only* for LDP exponential rate; Cat B prefactor explicitly *not* claimed (§1.2, §5.5, §6). |

**16/16 ✓**.

---

## §13 — One-Paragraph Summary

File 09 derives the Freidlin-Wentzell large-deviation principle for SCC's reflected Langevin (canonical T-PF-A1-SDE, Cat A, CV-1.9) in the small-noise limit $T_* \to 0$, producing the working-layer Cat A target lemma **L-FW-KRAMERS-SCC**: $\lim_{T_*\to 0} T_*\log\Gamma_{A\to B}^{\text{SCC}} = -\Delta\mathcal{E}_{A\to\text{saddle}}$, where $\Delta\mathcal{E}$ is the energy barrier from formation well $A$ to the lowest saddle on the path to $B$. The result is the **complementary Cat A counterpart** to file 02's Hänggi-Talkner-Borkovec Cat B prefactor target: file 02 supplies the sharper Eyring-Kramers form $\Gamma = \omega_0\exp(-\Delta E/T_*)$ (conditional on OP-HMORSE-SADDLE), while file 09 supplies the logarithmic-asymptotic exponent alone *without* requiring saddle-Hessian regularity, Morse non-degeneracy, or H5 — the canonical OPEN dependencies that block file 02 from Cat A. The factor-2 reconciliation (§7) verifies that the Freidlin-Wentzell quasipotential "$V = 2\Delta\mathcal{E}$" cancels against the SCC noise normalization "$\sqrt{2T_*}$" (giving $\epsilon = 2T_*$ in the FW small-parameter convention), yielding the *standard Kramers exponent* "$-\Delta\mathcal{E}/T_*$" (factor 1) — matching canonical T-P-F-ε0-K's $\Gamma = \Gamma_0 \exp(-\Delta\mathcal{E}/T_*)$ form. The advance map (§10) covers OP-0005-DYN (Cat A exponential-rate channel, primary; theorem_status.md L803), T-P-F-ε0-K (Cat A bypass at LDP level, sidesteps H5; canonical.md L1818), Package II (first Cat A entry), and explicitly *does not* depend on OP-HMORSE-SADDLE (theorem_status.md L594; bypassed at the rate-function level). 2D torus L=16 reference example with CONSENSUS BASELINE ($\alpha=1, \beta=10, c=1/2, T_*=0.1, R=4, \lambda_2=0.1522, \sigma=(\sqrt{2}/6)\sqrt{10}$) gives $\Gamma_{A\to B} \approx 10^{-81}$ for $\Delta\mathcal{E} \approx 18.7$ (Modica-Mortola interface cost order-of-magnitude). All 16 hard constraints CN1–CN16 verified; 0 canonical edits; OP-0005-DYN remains OPEN with two attack channels now structured (Cat A LDP + Cat B HTB).
