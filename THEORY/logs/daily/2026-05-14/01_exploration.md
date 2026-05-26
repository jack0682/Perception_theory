> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]

# 01 — Exploration: H-MORSE-Local Cat B First Lemma Structure

**Session:** 2026-05-14 (W7-Day5, post V-AFD + R-2 archives, post CV-1.15 P7 promotion)
**Target (from `00_plan.md` + `01_pre_brainstorm.md` §6):** H-MORSE-Local Cat B candidate — lemma structure 와 첫 substantive lemma 의 working draft.
**This file covers:** §4.1 Restatement (target re-stating) + §4.2 Multi-approach generation (3 mathematically independent approaches) + §4.3 Primary selection rationale.
**Depends on reading:** `THEORY/2_substrate/canonical/canonical.md` §6 (Axiomatic Groups), §13 T7-Enhanced (line 1138), §13 T-V5b-T-zero, §13 T-PreObj-1; `THEORY/working/CV114_H_MORSE_PACKAGEII/00–09`; `THEORY/2_substrate/sigma_framework/sigma_m_hessian_convention_audit.md` (placeholder).

---

## 1. Restatement

### 1.1 The plan's intent

The user's `00_plan.md` and `01_pre_brainstorm.md` §6 recommend "Option A: H-MORSE Cat A 정면 공격" as the afternoon track of 2026-05-14. The plan-mode review subsequently corrected this to **Path B — H-MORSE-Local Cat B** based on CV114 audit (2026-05-11) finding that *unconditional Cat A is impossible* (V5b-T-zero structural Goldstone counterexample).

### 1.2 Precise question

**Given:** the full SCC energy $\mathcal{E}: \Sigma_m \to \mathbb{R}$ on the volume-constrained simplex
$$\mathcal{E}(u) = \lambda_{\mathrm{cl}} \mathcal{E}_{\mathrm{cl}}(u) + \lambda_{\mathrm{sep}} \mathcal{E}_{\mathrm{sep}}(u) + \alpha\, u^\top L u + \beta \sum_x W(u(x))$$
on the simplex $\Sigma_m = \{u \in [0,1]^n : \mathbf{1}^\top u = m\}$.

**Prove (Cat B target):** For every interior $u^* \in \Sigma_m^\circ$ that is a critical point of $\mathcal{E}$ *and* is **symmetry-broken** (no nontrivial $\sigma \in \mathrm{Aut}(G)$ fixes $u^*$) *and* is **non-boundary** (no Lagrange-multiplier-active corner constraints), the projected Hessian
$$H^{\mathrm{proj}}(u^*) := \Pi_T\, H_{\mathcal{E}}(u^*)\, \Pi_T$$
on the tangent space $T_{u^*}\Sigma_m = \{v : \mathbf{1}^\top v = 0\}$ satisfies
$$\mu_{\min}(H^{\mathrm{proj}}(u^*)) \;\geq\; c(\lambda_{\mathrm{cl}}, \lambda_{\mathrm{sep}}, \beta, a_{\mathrm{cl}}, c^*) > 0$$
for some explicit constant $c$ depending only on the parameters and the self-support threshold $c^* \in ((3-\sqrt{3})/6, (3+\sqrt{3})/6)$.

### 1.3 What is data, what is success, what is failure

**Data (given):**
- The canonical 4-term energy structure (CN5 independence).
- Pre-existing canonical results: T7-Enhanced (Cat A), T-PreObj-1 (Cat A), T-V5b-T-zero (Cat A), T-PF-A1-AR (Cat A; tangent-space affine reduction).
- Numerical envelope $\mu_{\min} \in [0.96, 60.2]$ across tested configs (W7-CV1.13 status note).
- CV114 audit: 7 explicit counterexamples to unconditional H-MORSE.

**Success:**
- A working theorem statement D-HMORSE-LOCAL + 3 supporting lemmas L-HMORSE-DECOMP, L-CLOSURE-LIFT, L-BOUNDARY-MODE-EXCLUSION + explicit exclusion clause + Cat B self-judgment.

**Failure:**
- (a) Path B itself proves infeasible because the symmetry-broken / interior / non-boundary exclusions are insufficient and a *new* counterexample emerges. Outcome: documented failure + Cat C downgrade.
- (b) Closure-lift mechanism (L-CLOSURE-LIFT) is too weak to produce a useful $\mu_{\min}$ bound. Outcome: Path B remains conjectural; partial bound only.

### 1.4 Implicit assumptions surfaced

1. **Tangent-space convention.** `sigma_m_hessian_convention_audit.md` is placeholder; both Convention I (intrinsic) and Convention II (Lagrange multiplier extrinsic) give *the same* eigenvalues on the tangent space (the audit's prerequisite conclusion). Convention I adopted for this work.
2. **Volume Goldstone mod-out.** The constant mode $v = \mathbf{1}/\sqrt{n}$ is the *trivial* zero of $H^{\mathrm{proj}}$ from $\Sigma_m$ constraint. Mod out automatically (T-PF-A1-AR affine reduction).
3. **Discrete symmetry mod-out (Goldstone Bott).** Per V5b-T-zero, $\mathrm{Aut}(G)$-orbit zeros must be excluded by the *symmetry-broken position* assumption (not by mod-out — exclusion).
4. **No saturation.** "Non-boundary" excludes corner-saturated $u_x \in \{0, 1\}$. This is necessary for $W''(u_x)$ to be defined and bounded below on the relevant tangent directions.
5. **$b_D = 0$ or ε-smoothed.** Required for analyticity (canonical CN4); already standard.

---

## 2. Multi-Approach (3 mathematically independent approaches)

The three approaches differ in *what they take as input*, *what proof technique they invoke*, *what failure mode they exhibit*, and *what conditions they require*.

### 2.1 Approach (α) — Hessian decomposition + closure-correction lift (T7-Enhanced primary)

**Core idea.**
Decompose $H_{\mathcal{E}}(u^*) = H_{\mathrm{bd}}(u^*) + H_{\mathrm{cl}}(u^*) + H_{\mathrm{sep}}(u^*)$ where:
- $H_{\mathrm{bd}} = 2\alpha L + \beta\,\mathrm{diag}(W''(u^*_x))$ (explicit, Allen–Cahn standard).
- $H_{\mathrm{cl}}$: closure contribution; involves Jacobian $J_{\mathrm{Cl}}(u^*)$ of sigmoid closure.
- $H_{\mathrm{sep}}$: separation; positive on tangent space by self-induced-exterior structure.

Bound each term *separately* on the tangent space mod volume:
1. $H_{\mathrm{bd}}$ tangent eigenvalue $\geq \alpha \lambda_2(L) - \beta \lVert W'' \rVert_\infty$ — can be negative in spinodal regime.
2. $H_{\mathrm{cl}} \succeq 2 \lambda_{\mathrm{cl}} (1 - a_{\mathrm{cl}}/4)^2 \cdot \Pi_T$ — *strictly positive* via T7-Enhanced (canonical Cat A, line 1138). This is the "closure lift".
3. $H_{\mathrm{sep}} \succeq 0$ on $\Sigma_m^\circ$ (positivity of self-induced quadratic form; minor verification).

Sum: $\mu_{\min}(H^{\mathrm{proj}}) \geq 2\lambda_{\mathrm{cl}}(1 - a_{\mathrm{cl}}/4)^2 - \beta\lVert W'' \rVert_\infty + \alpha\lambda_2(L)$. When the closure-lift term dominates the spinodal deficit, $\mu_{\min} > 0$.

**Success form.** Explicit Cat B lower bound: $\mu_{\min} \geq c(\lambda_{\mathrm{cl}}, \beta, a_{\mathrm{cl}}) > 0$ with conditions $\lambda_{\mathrm{cl}}(1 - a_{\mathrm{cl}}/4)^2 \geq \beta\lVert W'' \rVert_\infty / 2 - \alpha\lambda_2(L)/2$.

**Failure mode.** If the closure-lift inequality from T7-Enhanced applies only to a *specific* eigenmode (the one along closure direction) rather than uniformly across the tangent space, $\mu_{\min}$ is not bounded by this argument — only the closure-direction eigenvalue is. This is the *narrow vs broad lift* question.

**Interaction with canonical.** Direct input from T7-Enhanced (canonical Cat A); no new external theorem. Self-contained within SCC framework. *Strongest* alignment with DECL-1.0 (closure dual-mode self-referentiality, CN1).

### 2.2 Approach (β) — Symmetry-broken interior + tangent space spectral lower bound

**Core idea.**
Treat the symmetry-broken assumption *directly* as an absence of degenerate orbit. On $\Sigma_m^\circ$, the only generic source of $\mathrm{ker}\, H^{\mathrm{proj}}$ is:
1. Volume mode $\mathbf{1}$ — modded out by tangent projection.
2. Goldstone modes from continuous symmetry — none on discrete graph.
3. Discrete-orbit Bott modes from $\mathrm{Aut}(G)$ — eliminated by symmetry-broken assumption (V5b-T-zero corner exclusion *and* general orbit exclusion).

Use *Implicit Function Theorem*: in a neighborhood of $u^*$, the Lagrangian $L(u, \lambda) = \mathcal{E}(u) - \lambda(\mathbf{1}^\top u - m)$ has Hessian $H_{\mathcal{E}}$; tangent positivity follows from *non-degenerate* critical point. Symmetry-broken position + interior + non-boundary together guarantee non-degeneracy (no Bott manifold containing $u^*$).

**Success form.** Generic Cat B with explicit conditions: symmetry-broken + interior + non-boundary + (T8 phase-separated regime) $\Rightarrow$ $\mu_{\min} > 0$. The bound is *qualitative* unless quantitative spectral analysis is added.

**Failure mode.** Doesn't give an *explicit* lower bound; only *positivity*. Cat B requires quantitative bound (canonical convention). Could combine with (α) for quantitative version, but then is no longer independent.

**Interaction with canonical.** Uses V5b-T-zero (Cat A) as the *exclusion* anchor (every excluded configuration is documented). T-PreObj-1G (Cat A graph-class independent) ensures the symmetry-broken regime is *non-empty* on generic graphs.

### 2.3 Approach (γ) — Perturbation Generic Morse (Smale–Sard + Allen–Cahn Morse transition)

**Core idea.**
Consider *generic* energies $\mathcal{E}_\delta = \mathcal{E} + \delta \cdot R$ where $R: \Sigma_m \to \mathbb{R}$ is a small smooth perturbation. By Smale-Sard transversality, for *generic* $R$ (in $C^\infty$ topology), all critical points of $\mathcal{E}_\delta$ are non-degenerate.

Allen–Cahn Morse transition theorems (Bates–Fife–Wang 1997; Fei–Wang–Zhou 2019) provide the *quantitative* version: for $\varepsilon = \alpha/\beta$ small enough, the Allen-Cahn energy has finitely many non-degenerate critical points, each indexed by phase configuration.

**Success form.** Generic-Morse Cat A (post-perturbation) or Cat B (without perturbation, dense generic subset). The bound is *generic in parameter space*, not pointwise constructive.

**Failure mode.** "Generic" is a measure-theoretic statement; gives no useful *pointwise* bound at a *specific* canonical minimizer. SCC has closure-correction terms not in standard Allen-Cahn, so adaptation needed. The transition theorems are sharp-interface ($\varepsilon \to 0$); SCC operates at $\varepsilon$ small but finite.

**Interaction with canonical.** Heaviest external-framework dependence (Smale-Sard, Bates-Fife-Wang, Fei-Wang-Zhou). Risk: framework drift from canonical SCC self-contained axiomatic. AFD-0's `afd_hmorse_reclassification.md` already classifies H-MORSE as Layer-3 *regularity* — compatible with this approach but does not strengthen SCC's self-containment.

### 2.4 Independence verification

| Aspect | (α) Hessian decomp + closure-lift | (β) Symmetry-broken IFT | (γ) Generic Morse |
|---|---|---|---|
| **Primary input** | T7-Enhanced Cat A (closure spectrum) | V5b-T-zero + T-PreObj-1G (exclusion + existence) | Smale-Sard + Bates-Fife-Wang |
| **Proof technique** | term-by-term spectral bound + sum | implicit function theorem on Lagrangian | transversality + sharp-interface limit |
| **Output type** | quantitative explicit constant | qualitative positivity | generic measure-theoretic |
| **Failure mode** | closure-lift narrow vs broad | no explicit bound | not pointwise; framework drift |
| **Conditions required** | $\lambda_{\mathrm{cl}}(1-a_{\mathrm{cl}}/4)^2 \geq \beta\lVert W'' \rVert_\infty / 2 - \alpha\lambda_2(L)/2$ | symmetry-broken + interior + non-boundary | generic in $\mathcal{E}_\delta$ space |
| **Canonical self-containment** | full | full | partial (external framework) |

The three approaches:
- (a) use different mathematical inputs (closure spectrum vs symmetry vs transversality);
- (b) fail in different ways (narrow eigenmode vs no explicit bound vs framework drift);
- (c) succeed under different conditions (parameter inequality vs structural exclusion vs measure-theoretic genericity);
- (d) produce different output types (quantitative vs qualitative vs generic).

These are *mathematically independent* per the §5 criteria of the autonomous prompt.

---

## 3. Primary Selection Rationale

**Primary: Approach (α) — Hessian decomposition + closure-correction lift.**

Reasons:

1. **T7-Enhanced is already canonical Cat A** (canonical.md line 1138). The closure-correction gap $2\lambda_{\mathrm{cl}}(1-a_{\mathrm{cl}}/4)^2$ is a closed-form expression in canonical parameters. No external theorem dependence beyond standard linear algebra.

2. **DECL-1.0 alignment.** Closure dual-mode self-referentiality (CN1) is the *foundational mechanism* of SCC. Using it as the primary lift mechanism is the most natural reading of "what makes SCC robust under perturbation." DECL-1.0 §"중심 정리 — T8" emphasizes the closure-stabilization tendency.

3. **Quantitative output.** Path B Cat B requires an *explicit* lower bound $c(\lambda_{\mathrm{cl}}, \lambda_{\mathrm{sep}}, \beta, a_{\mathrm{cl}})$. Approach (α) produces exactly that; (β) gives only qualitative positivity; (γ) is generic, not pointwise.

4. **Numerical alignment.** The empirical envelope $\mu_{\min} \in [0.96, 60.2]$ matches the *order of magnitude* of $2\lambda_{\mathrm{cl}}(1 - a_{\mathrm{cl}}/4)^2$ at canonical parameters ($\lambda_{\mathrm{cl}} = 1$, $a_{\mathrm{cl}} = 1$: $2 \cdot 1 \cdot (3/4)^2 = 1.125$). This is *consistent* with approach (α)'s prediction at the low end of the empirical envelope.

5. **CV114 recommendation.** `09_CV114_recommendation.md` explicitly proposes "closure-correction gap of canonical.md §13 line 1138" as the closeable mechanism. This plan adopts CV114's recommended path verbatim.

6. **Failure containment.** If approach (α) fails (narrow eigenmode), the failure mode is *spectrally localized* and triggers a clean fallback to approach (β) (qualitative positivity via symmetry exclusion). The failure does not contaminate adjacent canonical results.

**Fallback: Approach (β).** If (α)'s closure-lift turns out to be narrow (single eigenmode rather than uniform), we retreat to (β)'s qualitative IFT argument. This still yields Cat B (qualitative) and preserves the option of (γ) for a future Cat A attempt via generic perturbation.

**Not pursued today: Approach (γ).** Reserved as the *long-term Cat A path*. Generic Morse via Smale-Sard transversality is a known route in geometric analysis but is heavier (external framework) and gives generic-only output. Documented for completeness (`03_integration_and_new_open.md` §2 OP-HMORSE-GENERIC-PATH).

---

## 4. Decision Gate Self-Check (Rule R1–R6 from pre-brainstorm §7)

| Rule | Check | Result |
|---|---|---|
| R1 — No language refactor | All terms (H-MORSE-Local, T7-Enhanced, T-PreObj-1, V5b-T-zero, Hessian decomp) are canonical or pre-existing working vocabulary | ✓ PASS |
| R2 — Canonical alignment pre-check | Will be performed for each lemma in `02_development.md` (grep canonical.md + working/SF, MF, temporal, CV114) | will check at lemma time |
| R3 — Numerical demo obligation | `exp_hmorse_local_*.py` is *out of scope today* (plan mode does not allow new experiment scripts, deferred to 5/15+). Existing numerical envelope $\mu_{\min} \in [0.96, 60.2]$ serves as preliminary anchor | partial (deferred) |
| R4 — Cat status honest | Lemmas will be tagged PROVED / SKETCH / CONJECTURE / OPEN; Cat self-judgment in `02_development.md §7` | will tag |
| R5 — Round 4 external audit | Will be flagged for 5/15+ fresh-context Explore agent | flagged |
| R6 — Lifetime ceiling | Working on *existing* CV114 directory + canonical anchors; no new working folder | ✓ PASS |

**Net:** R1, R6 pass at exploration stage; R2, R3, R4, R5 to be applied/flagged in subsequent files.

---

## 5. Cross-references for `02_development.md`

| Lemma | Primary source | Type |
|---|---|---|
| L-HMORSE-DECOMP | `THEORY/2_substrate/Q3_dynamics/h_morse_packageII/03_energy_landscape_and_hessian.md` + canonical §13 | decomposition statement + per-term bound |
| L-CLOSURE-LIFT | canonical.md §13 T7-Enhanced (line 1138); `THEORY/2_substrate/Q3_dynamics/h_morse_packageII/02_H_MORSE_statement_reconstruction.md §9` | closure spectrum lower bound |
| L-BOUNDARY-MODE-EXCLUSION | `CODE/experiments/exp25_hessian_diagonal.py` (>90% boundary concentration); CV114 04 §boundary degeneracy | exclusion of boundary-localized eigenmodes |
| Counterexample exclusion | CV114 `05_counterexample_search.md` 7 CE explicit | scope-limit anchor |

---

*End of `01_exploration.md`. Next: `02_development.md` — D-HMORSE-LOCAL + exclusion clause + 3 lemmas + counterexample attempt + Cat self-judgment.*
