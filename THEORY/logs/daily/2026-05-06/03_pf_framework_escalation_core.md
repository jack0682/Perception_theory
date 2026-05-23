> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]

# 03_pf_framework_escalation_core.md — P-F Framework Escalation Proposal

**Session:** 2026-05-06 (W6 Day 3 G3.3, P1).
**Debt addressed:** W5 P-F framework — zero-T determinism's implicit finite-T assumptions.
**Sub-files:** `03a_pf_framework_axiom_proposal_v0.md` (P-F-A1..A8); `03b_op_0005_layer_b_kramers_pf_dependence.md`.
**Proposal:** Escalate P-F stochastic framework from OP-0010-0013 Medium → **OP-0014 HIGH** (proposed ID). W9 본격 framework formalism.

---

## §1. Implicit P-F Usage Catalog (5 Examples)

The canonical theory currently makes several implicit finite-T / stochastic assumptions without a declared framework. This section catalogs the five most significant.

### (a) Barrier height scaling $O(\beta^{0.89})$

**Location:** `canonical.md` §15 closing summary (empirical parameter regime analysis).

**Implicit assumption:** "Barrier height scales as $O(\beta^{0.89})$" is an Arrhenius-type empirical claim. Barrier height is meaningful only relative to a *noise scale* or *thermal energy* $T_*$. Without $T_*$, the phrase "barrier height" is a statement about local curvature of $\mathcal{E}$ (a deterministic quantity), NOT a statement about escape rates or kinetic selection. The $O(\beta^{0.89})$ claim conflates these two — it is valid as a deterministic curvature statement only if interpreted purely geometrically.

**P-F dependency:** To interpret $O(\beta^{0.89})$ as a statement about *escape rates* (Arrhenius-type kinetics), requires P-F framework with noise scale $T_*$ defined.

### (b) T-Persist-K-* "ε-gentle transition" (transition operator perturbation)

**Location:** T-Persist-K-Unified (canonical §13) and supporting T-Persist-K-Sep.

**Implicit assumption:** The perturbation bound $\lVert \delta u \rVert_\infty \leq \varepsilon_{\mathrm{pert}}$ assumes a *source* of perturbation — but the source's statistical properties are unspecified. Is $\delta u$ deterministic (bounded-magnitude external perturbation)? Or stochastic (noise with some distribution)?

**P-F dependency:** The transition operator results (Cat A conditional) hold for deterministic bounded perturbations. If interpreted as a stochastic stability result, requires P-F framework specifying the perturbation distribution.

### (c) exp55 "zero merges in 5000 iterations at $\sigma \leq 0.5$"

**Location:** `CODE/experiments/exp55_*.py` results; referenced in W5 D7 working notes.

**Implicit assumption:** $\sigma$ = noise standard deviation injected into the gradient flow. But what *type* of noise? The experiment uses additive Gaussian noise with std $\sigma$, but the canonical theory has no such $\sigma$ parameter. The experiment result is informal evidence for metastability under noise — it implies the existence of an effective temperature $T_* \propto \sigma^2$, but this connection is not formalized.

**P-F dependency:** To interpret exp55 formally, requires P-F framework connecting $\sigma$ (noise std) to $T_*$ (effective temperature) and to Kramers escape rates.

### (d) T-Persist-1(b) metastable basin escape rate

**Location:** T-Persist-1(b) (canonical §13, Cat A conditional under non-degenerate IFT + positive Hessian).

**Implicit assumption:** T-Persist-1(b) states the basin is metastable under deterministic gradient flow (local minimizer, Hessian positive definite). But the statement is often *informally* interpreted as "the formation persists for a long time under perturbations" — which is a kinetic statement requiring escape rate bounds (Arrhenius/Kramers).

**P-F dependency:** The metastability interpretation requires P-F framework. The deterministic stability interpretation (Hessian PD → local attractor) is valid without P-F, but the *duration* of metastability under noise requires $T_*$.

### (e) $\widehat{K}_{\mathrm{step}}(\pi, \beta, c, G, u_0)$ protocol-dependence (CN15 / CN16)

**Location:** CN15 Static/Dynamic Separation + CN16 Protocol Conditionality (canonical §14).

**Implicit assumption:** CN15 states that $K_{\mathrm{act}}$ at long times depends on the protocol (IC + noise + annealing schedule). CN16 states protocol-conditionality. But both assume a *stochastic* interpretation of "IC distribution" and "long-time behavior" — without P-F framework, the "IC distribution" $p_0(\mathbf{u})$ and "long-time distribution" $p_\infty(\mathbf{u})$ are undefined.

**P-F dependency:** CN15 + CN16 are *implicitly* P-F claims. Making them explicit requires defining: (a) the stochastic process $\mathbf{u}_t$ on $\Sigma_M$; (b) the stationary distribution $p_*$; (c) the convergence rate.

---

## §2. OP-0005 Layer B (Kramers) P-F Dependency

**OP-0005 Layer B** (in `working/MF/k_selection_b_kramers.md`): K-Selection via Kramers escape rate theory.

The Layer B candidate states that $K_{\mathrm{act}}$ at long times is selected by the Kramers rates:
$$k_{K \to K-1} = \frac{\omega_0}{2\pi} \exp\left(-\frac{\Delta E_{\mathrm{barrier}}}{T_*}\right)$$
where $T_*$ is the effective temperature, $\omega_0$ the saddle-point prefactor.

**This statement is vacuous without P-F framework:**
- $T_*$ is not defined in canonical SCC theory (zero-T determinism).
- The "barrier" $\Delta E_{\mathrm{barrier}}$ is a property of the energy landscape (computable), but its relevance to selection requires that escape rates follow Arrhenius law — which requires the Langevin equation on $\Sigma_M$.
- The Eyring-Kramers prefactor formula $A = (|\lambda_-|/2\pi)\sqrt{\det H_{\min}/|\det' H_{\mathrm{saddle}}|}$ requires existence of a saddle point on $\Sigma_M$ and the Hessian spectrum at saddle — purely geometric quantities — but the formula itself comes from the Kramers (1940) / Hänggi-Talkner-Borkovec (1990) escape rate theory under Brownian dynamics.

**Conclusion:** OP-0005 Layer B is structurally complete (barrier + prefactor formulas are well-defined geometrically on $\Sigma_M$) but *physically vacuous* without P-F framework declaring the stochastic dynamics. Closing OP-0005 Layer B requires closing OP-P-F first.

---

## §3. OP-0008 (σ^A K-jump Non-determinism) P-F Dependency

**OP-0008 (canonical, HIGH):** Under deterministic gradient flow, K-jumps ($K_{\mathrm{act}} : k \to k+1$) are forbidden (NQ-253 §4.3 Claim 4.3, N-1 Soft-Hard Asymmetry). Under finite noise, K-jumps are possible at rate $\propto \exp(-\Delta E_{k \to k+1}/T_*)$.

**The non-determinism of σ^A:** When a K-jump occurs ($K_{\mathrm{act}} : k \to k+1$), the new formation's σ-signature $\sigma^A_{\mathrm{new}}$ is not deterministically predictable from the pre-jump state. It depends on which saddle point is crossed (there may be multiple) and the noise realization at the moment of crossing.

**P-F dependency:**
- The K-jump event itself requires P-F framework (stochastic dynamics, finite $T_*$).
- The σ^A distribution after K-jump requires knowledge of: (a) the saddle landscape near the K-threshold (multiple saddles possible); (b) the noise-weighted probability of crossing each saddle; (c) the σ^A value at each saddle.
- Without P-F, OP-0008 reduces to the trivial statement "K-jumps don't happen deterministically" — which is already known (N-1 + T-Merge(b)). The interesting part of OP-0008 (the *distribution* of σ^A after a jump) requires P-F.

**Conclusion:** OP-0008 Path B (Cat B target) = compute $P(\sigma^A_{\mathrm{new}} | \text{K-jump from } [\hat{\mathbf{u}}])$ as a Gibbs-weighted average over saddles. This is a P-F computation. Closing OP-0008 requires P-F framework.

---

## §4. Escalation Proposal: OP-P-F (OP-0014, tentative)

**Proposed ID:** OP-0014 (tentative; formal ID assignment W7 D1 with theorem_status.md update, user supervised).

**Proposed title:** P-F Stochastic Framework for SCC — Langevin dynamics on $\Sigma_M$.

**Proposed severity:** HIGH (escalated from Medium-tier implicit status).

**Justification:**
1. **Blocking dependency:** OP-0005 Layer B + OP-0008 both require OP-P-F to be substantively closed. As long as OP-P-F is unresolved, these two HIGH-priority OPs are blocked.
2. **Implicit usage:** 5+ canonical claims implicitly use P-F assumptions without a declared framework (§1 above). This represents a *hidden ontological assumption* contrary to the SCC policy of explicit commitment declaration.
3. **W9 timeline:** P-F framework formalism is achievable in W9 (~30-37h budget) given:
   - Axiom set v0 (Day 3 `03a_*.md`, 8 axioms sketched).
   - Kramers integration in `working/MF/k_selection_b_kramers.md` (existing).
   - σ-framework compatibility (`working/MF/stereo_observation_framework.md` §6, W6 D2 evening).
4. **Proportionality:** Escalating to HIGH ensures W9 is allocated sufficient budget (~30-37h) for formalism. Medium-tier would defer to W10+ (conflict with CV-1.7 release).

**Relationship to OP-0021 (Stochastic SCC extension, LOW):** OP-0021 proposes field-level Langevin; OP-P-F (OP-0014) proposes the full framework including K-level master equation. Default: keep separate (see `01b_op_priority_reassessment_table.md` §2.2). Merge decision W9 D1.

---

## §5. W9 D-by-D Framework Work Outline

| W9 Day | Task | Output |
|---|---|---|
| D1 | P-F axiom set v1 (Cat C target; refine `03a_*.md` v0 → v1 with existence proofs for stationary distribution) + formal OP-0014 registration in theorem_status.md | working/MF/pf_stochastic_framework_v1.md (new working file) |
| D2 | Kramers integration: OP-0005 Layer B Kramers rates under P-F-A4/A5 formalized; barrier computation from $\Sigma_M$ Hessian | working/MF/k_selection_b_kramers.md extend + working/MF/pf_stochastic_framework_v1.md §2 |
| D3 | OP-0008 σ^A K-jump under P-F: Path B formulation (Gibbs-weighted saddle averaging) + σ-rich + Φ-rich combined | working/MF/pf_op_0008_path_b.md (new) |
| D4-D5 | σ-rich + Φ-rich combined formalism 본격; OP-0008 partial resolution proof attempt | extend working/MF/sigma_rich_augmentation.md + pf_op_0008_path_b.md |
| D6 | P-F framework canonical promotion preparation (daily-log proposal form for CV-1.7 or v2.0) | 2026-05-XX/pf_canonical_promotion_proposal.md |
| D7 | Weekly summary W9 + retrospective | weekly_summary W9 |

---

## §6. W11-W12 v2.0 Relationship

P-F framework canonical promotion (axiom set + Kramers integration + OP-0008 application) is a CV-1.7 or v2.0 candidate depending on proof completeness by W10:

- **CV-1.7 (W10):** If P-F axiom set v1 reaches Cat B (working sketch with explicit hypotheses) by W9 D6, it is a CV-1.7 promotion candidate at W10.
- **v2.0 (W11-W12):** If P-F requires deeper Langevin theory (existence/uniqueness of stationary distribution, convergence proofs), it is deferred to v2.0 where the full mathematical framework is introduced.

P-F is a *prerequisite* for any v2.0 claims about metastability, barrier heights, or kinetic selection — making it load-bearing for the entire W11-W12 expansion.

---

**End of `03_pf_framework_escalation_core.md`. G3.3 main complete: 5 implicit P-F usages cataloged; OP-0005 Layer B + OP-0008 P-F dependencies established; OP-0014 (P-F) escalation to HIGH proposed; W9 D-by-D outline. Sub-files: `03a_pf_framework_axiom_proposal_v0.md` + `03b_op_0005_layer_b_kramers_pf_dependence.md`.**
