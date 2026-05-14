# 03 — Integration and New Open Questions

**Session:** 2026-05-14 (W7-Day5)
**Target:** H-MORSE-Local Cat B working-layer integration with existing canonical + 4 new open problems.
**This file covers:** §4.5 Integration (existing canonical interactions, no silent resolutions) + §4.6 New open questions + canonical proposal draft (no actual canonical edit) + prompt improvement note.
**Depends on reading:** `01_exploration.md`, `02_development.md`; canonical.md §13 (T7-Enhanced line 1138, V5b-T-zero, T-PreObj-1, T-OP6-B, T8-Core); theorem_status.md (OP-0005-DYN, OP-0021, H-SR, H-WS, H-κ rows); HT-3.6 (post Track-1 CV-1.15 promotion).

---

## §1. Integration with existing canonical (no silent resolutions per Rule §8 of autonomous prompt)

### §1.1 Direct inputs (canonical Cat A used as premises)

| Canonical input | Used as | Direction of dependency |
|---|---|---|
| **T7-Enhanced** (canonical Cat A, §13 line 1138) | Primary input for L-CLOSURE-LIFT closure-correction lift inequality $\Pi_T H_{\mathrm{cl}} \Pi_T \succeq 2\lambda_{\mathrm{cl}}(1-a_{\mathrm{cl}}/4)^2 \Pi_T$ | H-MORSE-Local ← T7-Enhanced |
| **V5b-T-zero** (canonical Cat A) | Exclusion clause anchor (C4); explicit zero Goldstone family identified | H-MORSE-Local ⊃ exclusion (V5b-T-zero out of scope) |
| **T-PreObj-1G** (canonical Cat A, graph-class independent) | Non-vacuity of D-HMORSE-LOCAL: symmetry-broken interior minimizers exist on generic graphs | H-MORSE-Local ← T-PreObj-1G |
| **T-OP6-B** (canonical Cat A conditional, §5.3b) | $\rho_{\mathrm{bd-band}} \leq 2\sqrt{\alpha/\beta} \cdot \|\partial \Omega\|/n$ bound used in L-CLOSURE-LIFT spinodal attenuation | H-MORSE-Local ← T-OP6-B |
| **T-PF-A1-AR** (canonical Cat A) | Tangent-space affine reduction; volume Goldstone mod-out | H-MORSE-Local ← T-PF-A1-AR |
| **T8-Core** (canonical Cat A) | Phase-separated regime $\beta/\alpha > 4\lambda_2/\|W''(c)\|$ as Conditions (C2)+supercritical | H-MORSE-Local ← T8-Core |
| **D-ST-3** (CV-1.6 Cat B; D-HMORSE-LOCAL (C3) uses single-formation = $\#\mathrm{PersComp}(u^*) = 1$) | Definitional input | H-MORSE-Local ← D-ST-3 |
| **CN1 closure dual-mode self-referentiality** | Foundational alignment (Approach α justified) | conceptual |
| **CN4 analyticity ($b_D = 0$)** | Required for spectrum of $H_{\mathcal{E}}$ to be well-defined | H-MORSE-Local ← CN4 |

### §1.2 Downstream effects (H-MORSE-Local Cat B *if achieved* would imply)

| Canonical entry potentially affected | Direction of effect | Status today |
|---|---|---|
| **T-P-F-ε0-K** (canonical Cat B, conditional on H5) | H5 assumption *partially* upgrades from "assumed" to "Cat B established (under (C1)–(C5))" | Partial upgrade possible; full upgrade requires Cat A or further conditions. To be made explicit in `CV-1.16_SEAL.md` if Cat B achieved. |
| **Package II (Eyring-Kramers, OPEN)** | Cat B prefactor estimate becomes available under (C1)–(C5); full EK still requires OP-0021 (T_*) | Partial enablement; not full unlock. |
| **OP-0005-DYN (Kramers rates, OPEN)** | Cat B path for symmetry-broken interior single-formation regime; multi-formation case still depends on H-SR + H-WS | Partial path opened; multi-formation case remains OPEN. |

### §1.3 Explicit "out of scope today" (no silent resolution)

Per Rule §8 of autonomous prompt ("Silent resolution 금지"), the following are **NOT** resolved by this session, regardless of any partial intersection with H-MORSE-Local:

- **OP-0008 (σ-Inherit MERGE/SPLIT):** untouched. Wigner-projection W9+ not affected.
- **OP-0009 (Multi-formation foundations):** untouched. Multi-formation Hessian (block structure) outside (C3) single-formation scope.
- **OP-0021 (T_* registration):** untouched. H-MORSE and OP-0021 are *independent* per CV114 `06_packageII_dependency_map.md`.
- **OP-0011 (Transport kernel uniqueness):** resolved at CV-1.12; not touched.
- **T-σ-Theorem-4 retroactive Cat B (NQ-187):** untouched. The continuum vs discrete lattice mismatch is unrelated to H-MORSE-Local's interior single-formation case.
- **OP-SB1-084 (LOW):** untouched.
- **Mountain pass theorem on $\Sigma_M^K$:** structurally absent; not re-introduced.

### §1.4 Interaction with CV-1.15 (just promoted in Track 1, this same session)

H-MORSE-Local Cat B has **no direct dependency** on CV-1.15 Action-Based Temporal Succession Package. They are *orthogonal*:

- CV-1.15 operates on *temporal* succession (path-action cost, Gibbs kernel composition).
- H-MORSE-Local operates on *static* critical-point spectrum of $\mathcal{E}$ on $\Sigma_m$.

Possible *future* interaction: if CV-1.16 H-MORSE-Local Cat B is established, then T-ACT-KERNEL-COMP→REL (CV-1.15 Cat B conditional) becomes structurally easier to upgrade (because the action-Gibbs-kernel composition acts on a smooth Hessian-positive landscape post-H-MORSE-Local). This is *speculation* (not provable today); registered as new OP-HMORSE-ACTION-INTERACT below.

### §1.5 Canonical proposal draft (no actual canonical edit)

Per autonomous prompt §8.1, this section provides *proposal text only*. No `THEORY/canonical/*.md` is modified by Track 2.

**Proposed §13 Cat B entry for CV-1.16 promotion (if Path B succeeds):**

```markdown
**L-HMORSE-LOCAL.** *(Cat B candidate; CV-1.16; conditional on (C1)–(C5) + L-CLOSURE-LIFT broadness.)*

*Conditions.* (C1)–(C5) per D-HMORSE-LOCAL working-layer definition (`THEORY/working/CV114_H_MORSE_PACKAGEII/02_*` + `THEORY/logs/daily/2026-05-14/02_development.md §1`):
- (C1) $u^* \in \Sigma_m^\circ$ critical, $\Pi_T \nabla \mathcal{E}(u^*) = 0$.
- (C2) Interior: $u^*(x) \in (0,1)$ for all $x \in X$.
- (C3) Single-formation: $K_{\mathrm{act}}(u^*) = 1$ per D-ST-3.
- (C4) Symmetry-broken: trivial $\mathrm{Aut}(G)$-stabilizer.
- (C5) Non-boundary mode: $\|v_{\min}|_{\partial X}\|^2/\|v_{\min}\|^2 \leq 1/2$.

*Statement.* For every $u^*$ satisfying (C1)–(C5),
$$\mu_{\min}\bigl(\Pi_T H_{\mathcal{E}}(u^*) \Pi_T\bigr) \;\geq\; 2\lambda_{\mathrm{cl}}(1-a_{\mathrm{cl}}/4)^2 - \beta \cdot \rho_{\mathrm{bd-band}}(u^*) + \alpha\lambda_2(L) \;>\; 0,$$
where $\rho_{\mathrm{bd-band}}(u^*) \leq 2\sqrt{\alpha/\beta} \cdot |\partial\Omega|/n$ via T-OP6-B (Cat A).

*Proof sketch.* L-HMORSE-DECOMP (Cat B SKETCH) + L-CLOSURE-LIFT (Cat B with CONJECTURE-broadness) per `THEORY/logs/daily/2026-05-14/02_development.md §3–§4`.

*Cat B conditional status.* Cat B *conditional* on L-CLOSURE-LIFT broadness conjecture (OP-HMORSE-BROADNESS, registered §2 below). Cat A path: H-SR + H-WS + H-κ closure (OP-HMORSE-LOCAL-A).

*Numerical anchor.* $\mu_{\min} \in [0.96, 60.2]$ all tested canonical configs (W7-CV1.13 status note; exp25, exp63, exp_hessian_uniform_v2). Future: `exp_hmorse_local_path_b_*.py` (5/15+).

*References.* T7-Enhanced (Cat A); V5b-T-zero (exclusion anchor); T-PreObj-1G (non-vacuity); T-OP6-B ($\rho_{\mathrm{bd-band}}$ bound); CV114 `02–09`; daily logs `2026-05-14/01–02`.
```

**Caveat.** This proposal is *not* committed today. Actual canonical promotion requires:
- Round 4 Explore alignment audit (Rule R5) — *follow-up*.
- L-CLOSURE-LIFT broadness analytic strengthening OR explicit numerical envelope confirmation.
- User P7 authorization (separate from CV-1.15 P7 turn).

---

## §2. New Open Questions (4 new OPs registered)

### §2.1 OP-HMORSE-BROADNESS (HIGH severity)

**Statement.** Does T7-Enhanced (canonical Cat A) closure-correction gap $2\lambda_{\mathrm{cl}}(1-a_{\mathrm{cl}}/4)^2$ lift the *minimum* eigenvalue of $\Pi_T H_{\mathrm{cl}} \Pi_T$, not merely a single closure-aligned eigenmode?

**Why important.** L-CLOSURE-LIFT's Cat B claim *hinges* on this. If the lift is *narrow* (single eigenmode only), then the bound applies only to that direction; the actual $\mu_{\min}$ could still be small if the lowest mode is *orthogonal* to the closure-aligned direction.

**Approach candidates.**
- (a) Spectral mixing via closure Jacobian off-diagonal terms; show that $J_{\mathrm{Cl}}(u^*)$ couples all tangent modes ⇒ lift propagates.
- (b) Quadratic-form analysis: $H_{\mathrm{cl}}$ is a quadratic form on $\Sigma_m$; T7-Enhanced gives a *trace* lower bound; combine with $H_{\mathrm{bd}}$'s eigenvalue spread.
- (c) Numerical verification at canonical 15×15 grid: compute *all* eigenvalues of $\Pi_T H_{\mathrm{cl}} \Pi_T$ and verify uniform lower bound.

**Severity.** HIGH. Blocks L-HMORSE-LOCAL Cat B unconditional formulation. Cat B *conditional on broadness* is achievable today, but unconditional Cat B requires this OP.

**ETA.** 1–2 sessions for approach (c) numerical; 3–5 sessions for (a)/(b) analytic.

**Registered.** Today, 2026-05-14. Source: `02_development.md §4 failure mode`.

### §2.2 OP-HMORSE-SBM (LOW-MEDIUM severity)

**Statement.** On SBM (Stochastic Block Model), barbell, small-world graph classes (not the canonical 15×15 grid), does L-HMORSE-LOCAL Cat B hold under (C1)–(C5)? Specifically: does $\mu_{\min} > c(\lambda_{\mathrm{cl}}, \lambda_{\mathrm{sep}}, \beta, a_{\mathrm{cl}})$ hold uniformly across non-grid graph classes?

**Why important.** T-PreObj-1G is graph-class independent (Cat A), but T7-Enhanced and T-OP6-B may have implicit grid-locality assumptions. Verifying H-MORSE-Local on heterogeneous graphs strengthens the *generality* claim.

**Approach.**
- Numerical sweep: generate $u^*$ minimizers on SBM (planted-cluster), barbell (two cliques + bridge), small-world (Watts-Strogatz) ⇒ measure $\mu_{\min}(\Pi_T H_{\mathcal{E}} \Pi_T)$.
- Verify scaling with $\beta$, $\lambda_2(L)$, $\rho_{\mathrm{bd-band}}$ matches L-CLOSURE-LIFT prediction.

**Severity.** LOW-MEDIUM. Not a blocker for L-HMORSE-LOCAL Cat B (the grid case suffices for canonical-default-parameter claims). Strengthens robustness.

**ETA.** 1 session (numerical extension; uses existing `find_formation` + `EnergyComputer`).

**Registered.** Today. Source: `00_plan.md §"Track 2 first step"` + 5/13 state report `§7.5 Roadmap C 1번째`.

### §2.3 OP-HMORSE-GENERIC-PATH (MEDIUM severity)

**Statement.** Does Smale-Sard transversality + Allen-Cahn Morse transition (Bates-Fife-Wang 1997, Fei-Wang-Zhou 2019) yield a *generic* Cat A H-MORSE under generic small perturbation $\mathcal{E}_\delta = \mathcal{E} + \delta R$ for $\delta > 0$ small?

**Why important.** This is the *fallback Cat A path* for H-MORSE-Local (Approach γ from `01_exploration.md §2.3`). If achievable, gives Cat A (generic-measure-theoretic) without requiring H-SR + H-WS + H-κ closures.

**Approach candidates.**
- (a) Direct adaptation of Bates-Fife-Wang 1997 (sharp-interface limit Morse on Allen-Cahn) to SCC's closure-corrected energy; verify the proof relies only on energy smoothness and not on specific Allen-Cahn structure.
- (b) Fei-Wang-Zhou 2019 manifold Morse-Bott extension; check compatibility with $\Sigma_m$ polytope structure.

**Severity.** MEDIUM. Alternative Cat A path (not single-route critical), but valuable as backup if H-SR/H-WS/H-κ closure fails.

**Risk.** Approach γ depends on external framework (transversality, sharp-interface). Possible "framework drift" from canonical SCC self-containment. Need to verify SCC self-contained version exists.

**ETA.** 3–5 sessions.

**Registered.** Today. Source: `01_exploration.md §2.3` Approach (γ).

### §2.4 OP-HMORSE-SADDLE (MEDIUM severity, **separate from minimum**)

**Statement.** D-HMORSE-LOCAL covers *minimum* critical points (C1)–(C5). For *saddle* critical points (index ≥ 1), is there a corresponding Cat B Hessian-spectrum lower bound on *negative-index*-orthogonal directions?

**Why important.** Package II (Eyring-Kramers prefactor) requires *both* minimum Hessian determinant *and* saddle Hessian determinant. H-MORSE-Local Cat B covers minimum only; saddle is a separate problem.

**Approach.**
- Extend (C1)–(C5) to saddle: (C1') $\Pi_T \nabla \mathcal{E}(u^*) = 0$, Morse index $k \geq 1$; (C5') non-boundary on negative-eigenmode-orthogonal subspace.
- Saddle Hessian decomp: $H_{\mathrm{bd}}$ contributes negative eigenvalues in spinodal regime *exactly* on saddle's negative-index directions; closure lift may or may not transfer.

**Severity.** MEDIUM. Required for full Eyring-Kramers Cat B prefactor; not required for minimum-spectrum Cat B alone.

**ETA.** 2–4 sessions after H-MORSE-Local Cat B.

**Registered.** Today. Source: CV114 `06_packageII_dependency_map.md` "EK prefactor needs both Hessian determinants".

### §2.5 OP-HMORSE-EXCLUSION-VOLUME (LOW severity)

**Statement.** Beyond the volume Goldstone $\mathbf{1}$ (handled by $\Pi_T$), are there *other* zero modes that emerge from the mass-conservation $\mathbf{1}^\top u = m$ constraint, e.g., second-order Lagrange-multiplier effects?

**Why important.** Robustness check on D-HMORSE-LOCAL (C1)–(C5) completeness. If yes, additional clause needed.

**Approach.**
- Analyze the full Lagrangian $L(u, \lambda) = \mathcal{E}(u) - \lambda(\mathbf{1}^\top u - m)$; verify $H_L = \begin{pmatrix} H_{\mathcal{E}} & -\mathbf{1} \\ -\mathbf{1}^\top & 0 \end{pmatrix}$ has only the volume zero on the augmented kernel.

**Severity.** LOW. Likely closeable in <1 session (routine linear algebra). Included for completeness.

**ETA.** 1 session.

**Registered.** Today.

### §2.6 OP-HMORSE-ACTION-INTERACT (LOW severity; speculative)

**Statement.** Does H-MORSE-Local Cat B (CV-1.16+ target) enable an *unconditional* upgrade of T-ACT-KERNEL-COMP→REL (CV-1.15 Cat B conditional) — specifically by replacing (GK) hypothesis with a smoothness-from-H-MORSE argument?

**Severity.** LOW (speculative). Not a critical path.

**ETA.** Future investigation; reserve until both CV-1.15 and CV-1.16 are settled.

**Registered.** Today. Source: §1.4 above.

---

## §3. Updated Cat A path (OP-HMORSE-LOCAL-A)

**OP-HMORSE-LOCAL-A** (MEDIUM-HIGH severity, MEDIUM-HIGH ETA).

**Statement.** Upgrade L-HMORSE-LOCAL from Cat B (conditional on broadness + grid-specific) to **unconditional Cat A**.

**Required closures.**
- **H-SR** (canonical OPEN): $\min_k \mu_k > (K-1)\lambda_{\mathrm{rep}}$ — gives spectral repulsion guarantee, removes Cat B "conditional" annotation.
- **H-WS** (canonical OPEN): well-separation $d_{\min}^*$ explicit formula — needed for *fine-tune* exclusion (avoid fold-bifurcation proximities).
- **H-κ** (canonical OPEN): curvature condition $\kappa_{\max} \xi \leq 0.1$ derived from energy — affects T-OP6-B's $\rho_{\mathrm{bd-band}}$ constant.
- OR: closure of OP-HMORSE-GENERIC-PATH (§2.3) for *generic* Cat A via Smale-Sard.

**ETA.** 4–8 sessions post-Cat B (depends on which canonical OPs close first).

**Registered.** Today. Source: `02_development.md §8`.

---

## §4. Prompt improvement notes (optional, per autonomous prompt §14)

### §4.1 "H-MORSE Cat A" → "H-MORSE-Local Cat B (Path B)"

The 2026-05-13 state report `THEORY/logs/daily/2026-05-13/10_scc_current_state_and_next_expansion_report.md` §7.5 used the phrase "H-MORSE Cat A 먼저" as the recommended Roadmap C entry. The CV114 audit (2026-05-11) *already* established that *unconditional* Cat A is **impossible** (V5b-T-zero exact Goldstone zero structural counterexample).

**Recommendation for future plans / state reports.** Use the phrase **"H-MORSE-Local Cat B (Path B)"** instead of "H-MORSE Cat A 먼저". This is the realistic target. Cat A is a long-term aspiration via OP-HMORSE-LOCAL-A (§3) or OP-HMORSE-GENERIC-PATH (§2.3).

### §4.2 Plan-mode authority over agentic prompt-template wording

The 5/14 `01_pre_brainstorm.md` and `00_plan.md` correctly noted Option A "H-MORSE Cat A". Plan-mode review caught the correction. This is the right place for *target-precision* judgment calls. Future plan-mode reviews should similarly catch any "Cat A" claims against existing structural counterexamples — register a Decision Gate check.

### §4.3 Track 1 + Track 2 single-session execution

The combined CV-1.15 P7 promotion + H-MORSE-Local Cat B working draft in a single session is *aggressive* but *successful* (this session). The pattern works when:
- Track 1 is a *housekeeping closure* (no new mathematics).
- Track 2 is *strict working-layer* (no canonical edit during Track 2).
- Tracks are mathematically orthogonal (CV-1.15 temporal succession ⟂ H-MORSE-Local static spectrum).

This pattern is worth preserving as a template.

---

## §5. Rule R2 verification record (canonical alignment, post-write)

Per `01_exploration.md §4` and Rule R2:

| Lemma | Pre-write grep | Result |
|---|---|---|
| L-HMORSE-DECOMP | `grep "L-HMORSE-DECOMP\|HMORSE-DECOMP" canonical/ working/` | 0 hits — no name collision |
| L-CLOSURE-LIFT | `grep "L-CLOSURE-LIFT\|CLOSURE-LIFT" canonical/ working/` | 0 hits — no collision |
| L-BOUNDARY-MODE-EXCLUSION | `grep "BOUNDARY-MODE-EXCLUSION" canonical/ working/` | 0 hits — no collision |
| D-HMORSE-LOCAL | `grep "HMORSE-LOCAL\|H-MORSE-Local" canonical/ working/` | hits in CV114 only (target folder; this file extends it) |
| Exclusion clause (C1)–(C5) | content-level check vs CV114 02 + 05 + canonical V5b-T-zero | every CV114 counterexample explicitly excluded |

**Post-write follow-up (Rule R5, deferred to 5/15+).** Spawn fresh-context Explore agent with query: "Are the lemmas L-HMORSE-DECOMP, L-CLOSURE-LIFT, L-BOUNDARY-MODE-EXCLUSION (defined in `THEORY/logs/daily/2026-05-14/02_development.md`) duplicating any content in `THEORY/canonical/canonical.md` or in `THEORY/working/MF/`, `SF/`, `temporal/`, `CV114_*/`, `CV115_*/`?" — Round 4 alignment audit.

---

*End of `03_integration_and_new_open.md`. Next: `99_summary.md`.*
