# sigma_theorem4_canonical_revision.md — T-σ-Theorem-4 Urgent Canonical Revision Packet

**Status:** working draft (W5 Day 4 PM, Task #63 URGENT).
**Created:** 2026-04-30 (W5 Day 4 PM).
**Type:** Urgent canonical-revision packet for T-σ-Theorem-4 — addresses NQ-187 numerical falsification of leading-order $\mu_0 = \mu_1$ degeneracy claim. CV-1.6 release-blocking severity 🔴 CRITICAL.
**Author origin:** Task #63 (urgent). Triggered by NQ-187 scaling test (`logs/daily/2026-04-30/11_nq187_scaling_test_results.md`) and Wave 3 critical findings bulletin (`logs/daily/2026-04-30/13_wave3_critical_findings.md` §1).
**Canonical refs (target locations):** §13 T-σ-Theorem-4 (canonical.md lines 1377-1413, current Cat B); §11.1 Commitment 14 (O7) (line 794).
**Working refs:** Source data `CODE/scripts/test_sigma_theorem4_scaling.py` + `logs/daily/2026-04-30/11_nq187_scaling_test_results.md`; Critic findings `logs/daily/2026-04-30/13_wave3_critical_findings.md` §1.
**Dependencies:** R22 working file `working/SF/symmetry_moduli.md` §3.3 (claims $A_2/A_1 = 4$ on $D_4$ free-BC); NQ-187 working file (proposes higher-order $\epsilon$ resolution).

---

## §1. Mission and Severity

> **"NQ-187 numerical test 가 T-σ-Theorem-4 (ii) leading-order claim $\mu_0 = \mu_1 = 4|W''(c)|\epsilon$ 를 finite L $\in \{4, 8, 16\}$ 에서 falsify ($\mu_1/\mu_0 = 2$ asymptotically; power-law p ≈ 1.03 confirms leading-order non-degeneracy). Canonical revision urgent before CV-1.6 P4 G5 SF Round merge — caveat 추가, R22 $A_2/A_1 = 4$ 가정 verify, NQ-187b L → ∞ extrapolation 등록."**

이 working file 은 T-σ-Theorem-4 의 **3 핵심 이슈** 를 정식 정리하고 CV-1.6 packet 직전 canonical revision text 를 produce 한다:

1. NQ-187 p ≈ 1 falsifies leading-order degeneracy on finite L.
2. R22 $A_2/A_1 = 4$ continuum claim requires verification (NQ-187b L → ∞).
3. T-σ-Theorem-4 (ii) statement requires caveat addition.

**Severity:** 🔴 **CRITICAL for CV-1.6 release narrative**. T-σ-Theorem-4 cannot be re-promoted to Cat A via Wave 3 NQ-187 work; revision must precede CV-1.6 merge.

---

## §2. Numerical Evidence

### §2.1 NQ-187 power-law test (lanczos-engineer, W5 Day 4)

**Setup**: $L \times L$ free-BC grid with $D_4$ symmetry, varying $\epsilon$ at fixed $\beta = \beta_{\mathrm{crit}}^{(2)} + \epsilon$.

**Test configurations**:
- $L \in \{4, 8, 16\}$ (3 grid sizes).
- $\epsilon \in \{0.001, 0.003, 0.01, 0.03, 0.1\}$ (5 epsilon values).
- Total: 15 (L, ε) combinations.

**Measurement**: extract $\mu_0, \mu_1$ from Hessian at first-pitchfork minimizer; fit $\mu_1 - \mu_0 \sim C \epsilon^p$.

### §2.2 Hypothesis comparison

| Hypothesis | Predicted p | Observed p (L=16) | Status |
|---|---|---|---|
| §3.2 polynomial-equivariant (no 5th invariant) | 2 | **1.03** | ❌ REJECTED |
| §5 alternative (5th-equivariant non-zero) | 3/2 | **1.03** | ❌ REJECTED |
| Leading-order non-degeneracy (ratio ≠ 4) | 1 | **1.03** | ✅ CONFIRMED |

### §2.3 Asymptotic ratio

**Numerical result**: $\mu_0 = \epsilon |W''(c)|$, $\mu_1 = 2 \epsilon |W''(c)|$ asymptotically.

**Ratio** $\mu_1 / \mu_0 = 2$ (NOT 1 as canonical claims, NOT 4/1 either).

This implies the *effective* cubic-equivariant ratio on finite L is:
$$(A_2/A_1)_{\mathrm{eff}, L} \approx 2, \quad \text{not the claimed } A_2/A_1 = 4.$$

### §2.4 Implication

The leading-order ratio $\mu_1/\mu_0 = (A_2/A_1)/4$ from canonical (ii):
- (Canonical claim): $A_2/A_1 = 4$ ⇒ $\mu_1/\mu_0 = 1$ (degenerate).
- (Numerical, finite L): $\mu_1/\mu_0 = 2$ ⇒ $(A_2/A_1)_{\mathrm{eff}, L} = 8$ — NOT 4.

Three possible reconciliations:
- **(α)** Continuum $A_2/A_1 = 4$ holds, but finite-L correction makes effective ratio different. NQ-187b L → ∞ extrapolation needed.
- **(β)** R22 cubic-equivariant ratio derivation in `symmetry_moduli.md` §3.3 incorrect. Re-verification needed.
- **(γ)** Σ_m-Hessian convention map (NQ-187 architect's §2.1 absorption derivation) incorrect — the Hessian on Σ_m vs full ℝ^n convention error.

---

## §3. Proposed Canonical Revision Text

### §3.1 §13 T-σ-Theorem-4 revised (proposed for canonical.md lines 1377-1413)

```markdown
**T-σ-Theorem-4. σ at First Pitchfork on $D_4$ Free-BC Grid (Leading Order, **Cat B with finite-L caveat — Wave 3 audited**).** *(Original 2026-04-27, W5 Day 1. Cat A → Cat B retroactive 2026-04-29 W5 Day 3 EOD per Critic verdict. Wave 3 audit revision 2026-XX-XX, CV-1.6: finite-L caveat added per NQ-187 numerical falsification.)*

Setup as T-σ-Theorem-3 with $\beta = \beta_{\mathrm{crit}}^{(2)} + \epsilon$, $\epsilon > 0$ small. By T-Birth-Parametric (Cat A) + R22 axis-aligned selection (`working/SF/symmetry_moduli.md` §3.3, Cat A subject to NQ-187b verification; cubic ratio $A_2/A_1 = 4$ continuum claim under audit), the post-bifurcation minimizer is $u^*_\epsilon = c\mathbf{1} + a_\epsilon \phi_{(1, 0)} + O(\epsilon)$ with $a_\epsilon = c_R\sqrt{\epsilon}$.

**(i) Symmetry breaking $D_4 \to \mathbb{Z}_2$.** [unchanged]

**(i') Orbit-representative choice.** [unchanged]

**(ii) Hessian split (Wave 3 revision: finite-L non-degeneracy).** *(Originally claimed leading-order degeneracy $\mu_0 = \mu_1$; revised per NQ-187 numerical evidence W5 Day 4.)*

By R22 normal-form analysis on Fiedler doublet:
$$\mu_0 = 4|W''(c)|\epsilon + O(\epsilon^{3/2}) \quad \text{(continuum claim, L → ∞)},$$
$$\mu_1 = (A_2/A_1)|W''(c)|\epsilon + O(\epsilon^{3/2}) \quad \text{(continuum)}.$$

**Continuum claim**: $A_2/A_1 = 4$ on $D_4$ free-BC ⇒ $\mu_0 = \mu_1$ at leading order (degenerate).

**Numerical reality on finite L**: NQ-187 scaling test (`CODE/scripts/test_sigma_theorem4_scaling.py`, W5 Day 4) on $L \in \{4, 8, 16\}$ measures:
- $\mu_0 = \epsilon |W''(c)|$, $\mu_1 = 2\epsilon |W''(c)|$ asymptotically.
- Ratio $\mu_1/\mu_0 = 2$ (NOT 1).
- Power-law $\mu_1 - \mu_0 \sim \epsilon^p$ with $p = 1.03$ on $L = 16$ (rejects polynomial-equivariant $p=2$ and 5th-equivariant $p=3/2$ hypotheses).

**Reconciliation candidates** (Wave 4+ audit):
- (α) Continuum $A_2/A_1 = 4$ correct; finite-L correction shifts effective ratio to $(A_2/A_1)_{\mathrm{eff}, L} \approx 8$ at $L \leq 16$; L → ∞ extrapolation (NQ-187b W6+) verifies continuum value.
- (β) R22 derivation `symmetry_moduli.md` §3.3 contains error; re-verification required.
- (γ) Σ_m-Hessian convention map error in NQ-187 architect's §2.1 absorption derivation.

**Until reconciliation completed**: T-σ-Theorem-4 (ii) is conditional on either (α) NQ-187b L → ∞ confirms $A_2/A_1 = 4$, or (β)/(γ) identifies and corrects derivation error producing the observed ratio 2.

**(iii) Irrep labels under $\mathbb{Z}_2 = \langle s_y \rangle$.** [unchanged]

**(iv) Nodal counts.** [unchanged]

**(v) σ-signature** *(Wave 3 revision)*: leading-order σ-tuple structure depends on reconciliation outcome:

- **Continuum case** (post-NQ-187b L → ∞ if confirms $A_2/A_1 = 4$): σ-tuple has degenerate $\mu_0 = \mu_1$ first two entries, distinguished by irrep labels (trivial vs sign per Commitment 14 (O7) Mulliken order).
$$\sigma(u^*_\epsilon)\big|_{\mathrm{cont}} = \big(\mathcal{F}; (2, [+1], 4|W''(c)|\epsilon), (2, [-1], 4|W''(c)|\epsilon), \ldots\big).$$

- **Finite-L case** ($L \leq 16$ as measured): σ-tuple has *distinct* eigenvalues; ordering is straightforward (lowest first):
$$\sigma(u^*_\epsilon)\big|_{L \leq 16} = \big(\mathcal{F}; (2, [+1], \epsilon|W''(c)|), (2, [-1], 2\epsilon|W''(c)|), \ldots\big).$$

The σ-tuple is **L-dependent** in the finite regime; tie-break convention (O7) is unnecessary on finite L (no degeneracy); convention applies only in continuum limit (post-α reconciliation).

**(vi)** $\mathcal{F}(u^*_\epsilon) \in \{0, 1\}$ [unchanged]

*Status:* **Cat B with finite-L caveat (Wave 3 audited)**. Original Cat A (2026-04-27) downgraded to Cat B (2026-04-29 retroactive Critic verdict); Wave 3 audit (2026-04-30) reveals additional finite-L non-degeneracy issue. Cat A re-promotion path requires **all three** of:
- (1) NQ-187b L → ∞ extrapolation confirming $A_2/A_1 \to 4$ in continuum (or correcting to alternative value).
- (2) R22 `symmetry_moduli.md` §3.3 verification or correction.
- (3) Σ_m-Hessian convention audit (NQ-187 §2.1).

Until (1)-(3) closed: Cat B with finite-L numerical anchor; Cat A claim deferred to W6+.

*Erratum 2026-04-27 evening (Round 1)* [unchanged]
*Refinement 2026-04-27 night (Round 2)* [unchanged]
*Status Revision 2026-04-29 (W5 Day 3 EOD, CV-1.5.1)* [unchanged]
*Wave 3 Audit 2026-04-30 (CV-1.6 candidate revision)*: NQ-187 scaling test on $L \in \{4, 8, 16\}$ reveals leading-order non-degeneracy $\mu_1/\mu_0 = 2$ on finite L. Power-law $p = 1.03$ rejects $p=2$ and $p=3/2$ hypotheses. Three reconciliation paths (α: continuum extrapolation; β: R22 error; γ: Σ_m convention error) registered; verification deferred to W6+ (NQ-187b + R22 audit + NQ-187 §2.1 audit). T-σ-Theorem-4 statement augmented with finite-L caveat. *(Source: `working/SF/sigma_theorem4_canonical_revision.md`; numerical evidence `logs/daily/2026-04-30/11_nq187_scaling_test_results.md`; Critic findings `logs/daily/2026-04-30/13_wave3_critical_findings.md` §1.)*

*Note on σ-tuple well-definedness in degenerate case* [unchanged]

*Cross-reference comparison* [unchanged]

*References:* [unchanged + add: `working/SF/sigma_theorem4_canonical_revision.md` (Wave 3 audit packet); `CODE/scripts/test_sigma_theorem4_scaling.py` + `CODE/scripts/results/sigma_theorem4_scaling.json` (numerical evidence)].
```

### §3.2 Commitment 14 (O7) revision (canonical.md line 794)

```markdown
**(O7) Tie-breaking via Mulliken character order *(Wave 3 audited)*.** When two consecutive σ-tuple
entries have identical eigenvalue $\lambda_k = \lambda_{k+1}$ but distinct irreps (e.g., the **continuum**
case of T-σ-Theorem-4 (v) at first pitchfork on $D_4$ where $K_0 = K_1 = 4|W''(c)|\epsilon$ at leading
order — subject to W6+ NQ-187b L → ∞ extrapolation verification), the σ-tuple selects trivial irrep
($A_1$) before sign irrep ($A_2$) per Mulliken character order. Higher-order $\epsilon$ splitting (NQ-187,
W7+) may resolve the leading-order degeneracy if continuum claim verified; tie-break convention applies
on the leading-order plateau.

**On finite L**: NQ-187 W5 Day 4 numerical evidence shows $\mu_0 \neq \mu_1$ at $L \leq 16$
(ratio 2 not 1); tie-break convention is *vacuously satisfied* on finite L (no degeneracy).
Tie-break necessity emerges only in the continuum limit, conditional on NQ-187b W6+ verification.

*(W5 Day 1 Round-2 audit `92_critical_review_round2.md` §2.2; T-σ-Theorem-4 well-definedness note;
Wave 3 audit 2026-04-30 `working/SF/sigma_theorem4_canonical_revision.md`.)*
```

---

## §4. Reconciliation Audit Trail

### §4.1 (α) Continuum L → ∞ extrapolation (NQ-187b)

**Hypothesis**: $A_2/A_1 = 4$ holds in continuum limit; finite-L correction shifts effective ratio.

**Test design**: extend NQ-187 scaling to $L \in \{4, 8, 16, 32, 64\}$ (or larger, computational budget permitting); measure $\mu_1/\mu_0$ as function of $L$; extrapolate to $L \to \infty$.

**Predictions**:
- If (α) correct: $\mu_1/\mu_0(L)$ trends from 2 (L=16) toward 1 (L=∞); extrapolation gives ratio $\to 1$ ⇒ $A_2/A_1 \to 4$.
- If (α) incorrect: $\mu_1/\mu_0(L)$ saturates at 2 (or other value ≠ 1); $A_2/A_1$ continuum value differs from 4.

**Effort estimate**: 2 weeks W6+ (Lanczos eigenvalue extraction at L=32, 64 expensive but feasible).

**Working file target**: `working/SF/nq187b_L_extrapolation.md`.

### §4.2 (β) R22 cubic-equivariant derivation audit

**Target**: `working/SF/symmetry_moduli.md` §3.3 — claims $A_2/A_1 = 4$ via R22 axis-aligned cubic equivariants.

**Audit task**: re-derive $A_2/A_1$ from first principles on $D_4$ free-BC grid; verify each step:
- Cubic-invariant computation $A_1 = \int \phi_{(1,0)}^4$, $A_2 = \int \phi_{(1,0)}^2 \phi_{(0,1)}^2$ — symbolic algebra check.
- Discrete vs continuum: free-BC grid eigenmodes are discrete cosines $\cos((2k-1)\pi x / 2L)$; products / integrals discretize differently from continuum.

**Effort estimate**: 1-2 weeks W6+.

**Working file target**: `working/SF/r22_a2_a1_audit.md`.

### §4.3 (γ) Σ_m-Hessian convention audit (NQ-187 architect's §2.1)

**Target**: NQ-187 working file §2.1 absorption derivation — converts ambient ℝ^n Hessian to Σ_m-tangent Hessian via simplex-projection absorption.

**Audit task**: verify the projection convention. Two common conventions in the literature:
- **Convention I**: project gradient + Hessian onto tangent simplex (centered convention).
- **Convention II**: use Lagrange multiplier reduction (extrinsic convention).

**Test**: compute $\mu_0, \mu_1$ via both conventions on $L = 4$ (small grid, exact symbolic); compare ratio.

**Effort estimate**: 3-5 days W6 Day 1-3.

**Working file target**: `working/SF/sigma_m_hessian_convention_audit.md`.

### §4.4 Audit priority

(γ) Σ_m convention audit: **highest priority** (3-5 days, smallest effort, most likely error source per Critic finding).
(β) R22 derivation audit: **medium priority** (1-2 weeks, can run in parallel).
(α) NQ-187b L → ∞ extrapolation: **lowest priority** (2 weeks, computational intensive — only meaningful after (β)+(γ) audits clear).

---

## §5. CV-1.6 Packet Impact

### §5.1 D-CV1.6 items affected

The Wave 3 finding affects multiple CV-1.6 packet items:

- **D-CV1.6-O? T-σ-Theorem-4 caveat** (NEW, this packet): adopt revised statement (§3.1).
- **D-CV1.6-O? Commitment 14 (O7) revision** (NEW, this packet): adopt finite-L vs continuum disambiguation (§3.2).

These are *additions* to the existing CV-1.6 packet; do not require deferring CV-1.6 release.

### §5.2 Cat status table impact

CV-1.6 Cat status table:
- T-σ-Theorem-4: Cat B (already at CV-1.5.1 retroactive); **Wave 3 audit** subscript added (no further downgrade since Cat B already).
- No 45A → 44A change needed.

### §5.3 No CV-1.6 release blockage

The Wave 3 finding is *contained* — adding caveat to Cat B theorem is non-disruptive. CV-1.6 release on schedule (W6 Day 7 target); Wave 4+ resolves (α)/(β)/(γ) audits.

### §5.4 P4 G5 SF Round merge guidance

Per `13_wave3_critical_findings.md` §1.4 item 4: "T-σ-Theorem-4 cannot be re-promoted to Cat A via Wave 3 NQ-187 work; needs additional verification of continuum extrapolation."

**Guidance**: defer T-σ-Theorem-4 Cat A re-promotion to **CV-1.7+** post (α)+(β)+(γ) audit completion. CV-1.6 retains Cat B with augmented caveat.

---

## §6. Cross-Cluster Connections

### §6.1 σ_rich foundation cluster (Tasks #1-4, #34, #48)

T-σ-Theorem-4 is the *single-formation* σ-tuple supporting structure at first pitchfork. σ_rich extension (Tasks #1-3) operates at multi-formation level; does NOT directly depend on T-σ-Theorem-4 (ii)'s degeneracy claim.

**Implication**: σ_rich Path B (Commitment 18, Task #48) is **not affected** by T-σ-Theorem-4 finite-L finding. CV-1.6 / CV-1.7 σ_rich promotion path independent.

### §6.2 K-Selection cluster (Tasks #5-8, #49)

K-Selection Commitment 19 axiom (Task #49) does not invoke T-σ-Theorem-4 directly. K-Selection (a) free-energy uses $\mathcal{E}^*_K$ minimum, which for K=1 is the uniform $u = c\mathbf{1}$ (pre-pitchfork) or post-pitchfork minimizer. Hessian eigenvalues at minimum are not σ-tuple-specific.

**Implication**: Commitment 19 is **not affected**.

### §6.3 Theorem 2-G Schramm-style restatement (Task #46, completed by team-lead)

If Schramm-restatement (T-σ-Locality) uses T-σ-Theorem-4's σ-tuple form: would inherit finite-L caveat. Cross-check needed at CV-1.6 packet review.

---

## §7. Hard Constraint Verification

- [x] **canonical 직접 수정 0** — `working/SF/`; revision text is *candidate* for canonical.md, not directly applied.
- [x] **Silent resolution 0** — explicit Cat B retained with augmented finite-L caveat; NQ-187 falsification fully documented; reconciliation paths (α)(β)(γ) registered.
- [x] **No Research OS resurrection** — single-topic working file.
- [x] **Not reductive** — numerical evidence (NQ-187 lanczos-engineer) used as constraint on theory; CN10 contrastive maintained.
- [x] **u_t primitive maintained** — T-σ-Theorem-4 operates on $u^*_\epsilon$ first-pitchfork minimizer; σ-tuple is derived diagnostic.
- [x] **CN5 4-energy not merged** — N/A; T-σ-Theorem-4 is single-formation σ-supporting structure.
- [x] **K not dual-treated** — N/A; single-formation context.
- [x] **No metastability claim without P-F flag** — N/A; static σ-extraction at first pitchfork.
- [x] **Cat status accurate** — Cat B retained (was Cat A → Cat B at CV-1.5.1 retroactive); Wave 3 finding *augments* the caveat without changing Cat letter.
- [x] **CV-1.6 release impact contained** — caveat addition is non-disruptive (§5.3).
- [x] **(α)(β)(γ) reconciliation paths explicit** — no silent prioritization; (γ) flagged as highest priority in §4.4.

---

## §8. Forward Roadmap

### §8.1 W6 Day 1-3 immediate

- Execute (γ) Σ_m-Hessian convention audit (`working/SF/sigma_m_hessian_convention_audit.md`).
- If (γ) identifies and corrects error: T-σ-Theorem-4 (ii) statement updated; possible Cat A re-promotion at CV-1.7.
- Otherwise: proceed to (β).

### §8.2 W6 Day 4 – W7

- Execute (β) R22 derivation audit (`working/SF/r22_a2_a1_audit.md`).
- If (β) identifies error: R22 working file revised; T-σ-Theorem-4 follows.

### §8.3 W7 – W8

- Execute (α) NQ-187b L → ∞ extrapolation (`working/SF/nq187b_L_extrapolation.md`).
- Final reconciliation: continuum claim verified or corrected.

### §8.4 CV-1.7 Cat A re-promotion target

If (α)+(β)+(γ) all closed: T-σ-Theorem-4 revised statement with verified $A_2/A_1$ value (continuum 4 or alternative); Cat A re-promotion at CV-1.7 (W12+).

If reconciliation incomplete: Cat B retained at CV-1.7; further W12+ work.

---

## §9. References

### §9.1 Numerical evidence

- `CODE/scripts/test_sigma_theorem4_scaling.py` (NQ-187 power-law test).
- `CODE/scripts/results/sigma_theorem4_scaling.json` (raw data: $\mu_0, \mu_1$ at 15 (L, ε) combinations).
- `THEORY/logs/daily/2026-04-30/11_nq187_scaling_test_results.md` (results report).

### §9.2 Critic findings

- `THEORY/logs/daily/2026-04-30/13_wave3_critical_findings.md` §1 (CRITICAL FINDING #1: NQ-187 p ≈ 1 falsifies T-σ-Theorem-4).
- `THEORY/logs/daily/2026-04-30/05_critic_final_review.md` (Wave 3 Critic comprehensive verdict).

### §9.3 Source canonical entries

- `canonical/canonical.md` §13 lines 1377-1413 (T-σ-Theorem-4 current Cat B).
- `canonical/canonical.md` §11.1 line 794 (Commitment 14 (O7)).

### §9.4 Working files affected

- `working/SF/symmetry_moduli.md` §3.3 (R22 $A_2/A_1 = 4$ claim — audit target (β)).
- (NEW) `working/SF/sigma_m_hessian_convention_audit.md` (audit (γ)).
- (NEW) `working/SF/r22_a2_a1_audit.md` (audit (β)).
- (NEW) `working/SF/nq187b_L_extrapolation.md` (audit (α)).

### §9.5 NQ register

- **NQ-187**: original higher-order $\epsilon$ resolution proposal — now reframed by Wave 3 finding.
- **NQ-187b**: NEW W6+ — L → ∞ extrapolation of $A_2/A_1$ ratio (path α).

---

**End of sigma_theorem4_canonical_revision.md.**

**Status: working draft. Task #63 URGENT complete (canonical-revision packet draft). NQ-187 W5 Day 4 numerical falsification documented (§2): $\mu_1/\mu_0 = 2$ at finite L $\in \{4, 8, 16\}$, contradicting canonical claim $\mu_0 = \mu_1$ at leading order. Three reconciliation paths registered (§4): (α) continuum extrapolation, (β) R22 derivation audit, (γ) Σ_m-Hessian convention audit. Canonical revision text drafted (§3): T-σ-Theorem-4 (ii) augmented with finite-L caveat; Commitment 14 (O7) augmented with finite-L vs continuum disambiguation. CV-1.6 packet impact contained (§5): caveat addition is non-disruptive. Cat status: Cat B retained (Wave 3 audit subscript). Cat A re-promotion target CV-1.7+ post (α)+(β)+(γ) audit closure. Cross-cluster impact: σ_rich (Commitment 18) and K-Selection (Commitment 19) NOT affected. All hard constraints verified. Wave 4+ priorities (§8): (γ) audit W6 Day 1-3 (highest priority); (β) W6 Day 4-W7; (α) W7-W8.**

**File:** `/Users/ojaehong/Perception/Perception_theory/THEORY/working/SF/sigma_theorem4_canonical_revision.md`
**Created:** 2026-04-30 (W5 Day 4 PM, URGENT).
**Promotion target:** CV-1.6 D-CV1.6-O? items (T-σ-Theorem-4 caveat addition + Commitment 14 (O7) finite-L disambiguation); CV-1.7+ Cat A re-promotion post-reconciliation.
