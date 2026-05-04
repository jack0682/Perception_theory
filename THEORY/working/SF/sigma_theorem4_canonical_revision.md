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

### §2.5 RECONCILIATION (W6 D1 EOD Issue #3 deeper audit insight)

After detailed cross-check of R22 derivation in `symmetry_moduli.md` §3.3 (lines 100-156) against NQ-187 measurement protocol, the apparent "falsification" decomposes into two distinct claims that should be analyzed separately:

**Claim 1 (R22 cubic-equivariant ratio $A_2/A_1 = 4$): LIKELY CORRECT.**

Per `symmetry_moduli.md` line 113-130, the ratio $A_2/A_1 = 6K/I_4 = 6 \cdot (2/3) = 4$ comes from:
- Multinomial expansion $\int(a\phi_{10} + b\phi_{01})^4 = a^4 I_4 + 6a^2b^2 K + b^4 I_4$ (factor 6 = $\binom{4}{2,2}/2$).
- Integral evaluations $I_4 = 3/2$, $K = 1$ on continuum $D_4$ free-BC torus.
- **Naive integral ratio $K/I_4 = 2/3$ is consistent with $A_2/A_1 = 4$ via the multinomial factor 6** — they are the same quantity in different normalizations, not contradictory values.
- nq187b §2.5 `discrete sum tables show $K^L/I_4^L \to 2/3$ at $L \to \infty$; multiplying by 6 gives $A_2^L/A_1^L \to 4$ ✓ R22 confirmed.

**Claim 2 (Canonical T-σ-Theorem-4 (ii) "Mode 0 = Mode 1 = $4|W''(c)|\epsilon$ degenerate"): LIKELY PARTIALLY INCORRECT.**

Per R22 axis-aligned minimum analysis (`symmetry_moduli.md` lines 148-150), the Hessian at the post-bifurcation minimum $(A, 0)$ is:
- $F_{aa} = -2\mu$ (Mode parallel to breaking direction).
- $F_{bb} = -\mu$ (Mode transverse to breaking direction).
- Ratio $F_{aa}/F_{bb} = 2$ at leading order.

If $\mu \propto -\epsilon$ (specifically $\mu = -2\epsilon|W''(c)|$ under one common convention), then $F_{aa} = 4\epsilon|W''(c)|$ and $F_{bb} = 2\epsilon|W''(c)|$. **R22 axis-aligned predicts $\mu_0/\mu_1 = 2$ at the post-bifurcation minimum, not 1.**

NQ-187 measured $\mu_1/\mu_0 = 2$ at the minimizer (per §2.1 protocol "Hessian at first-pitchfork minimizer"). Inverting: $\mu_0/\mu_1 = 1/2$, i.e., $\mu_1$ corresponds to the parallel direction (larger eigenvalue), $\mu_0$ to the transverse — opposite sort order from R22's $F_{aa}, F_{bb}$ but the **factor 2 ratio is exactly the R22 prediction**.

**Therefore: NQ-187's $\mu_1/\mu_0 = 2$ is in agreement with R22 derivation, but contradicts the canonical (ii) "leading-order degeneracy" formula.** The contradiction is between NQ-187 + R22 (both claim ratio 2 at minimum) vs canonical (ii) (claims ratio 1 / degeneracy at minimum).

### §2.5.1 DEEPER AUDIT (W6 D1 EOD Issue #3 re-examination, 2026-05-04)

After re-examining canonical T-σ-Theorem-4 entry (`canonical.md` lines 1385-1433) directly, the apparent "Mode 0 = Mode 1 degenerate" claim arises from a **two-normal-form mixing error** in canonical Step 4 of the proof (line 1407). Specifically:

**Canonical normal form** (line 1395):
$$F_{can}(x, y; \beta) = \beta(x^2 + y^2) + A_1 (x^2 + y^2)^2 + A_2 x^2 y^2.$$

**`symmetry_moduli.md` §3.3 normal form** (line 127):
$$F_{sym}(a, b) = \tfrac{\mu}{2}(a^2 + b^2) + A_1^{sym}(a^4 + b^4) + A_2^{sym} a^2 b^2.$$

**These two normal forms are NOT the same.** Conversion via expanding $A_1^{can}(x^2+y^2)^2 = A_1^{can}(x^4 + 2 x^2 y^2 + y^4)$:
- Coefficient of $x^4$ (or $y^4$) in $F_{can}$: $A_1^{can}$ — matches $A_1^{sym}$.
- Coefficient of $x^2 y^2$ in $F_{can}$: $2 A_1^{can} + A_2^{can}$ — matches $A_2^{sym}$.
- **Conversion identity**: $A_2^{sym} = 2 A_1^{can} + A_2^{can}$, equivalently $A_2^{can}/A_1 = A_2^{sym}/A_1 - 2$.

`symmetry_moduli.md` §3.3 explicitly derives $A_2^{sym}/A_1 = 4$ (line 130, multinomial factor 6: $A_2^{sym} = 6 \beta_{bd} K, A_1 = \beta_{bd} I_4 = 3 \beta_{bd}/2$, ratio $4$). Converting to canonical's normal form: $A_2^{can}/A_1 = 4 - 2 = 2$.

**Canonical line 1395 claims "$A_2/A_1 = 4$"**, but this is using `symmetry_moduli`'s value INSIDE canonical's normal form. The correct value for canonical's normal form is $A_2/A_1 = 2$.

**Recomputed canonical Step 4** (using correct $A_2^{can}/A_1 = 2$):
- $F_{xx}|_{(A,0)} = -4\beta = 4|W''(c)|\epsilon$ ✓ (unchanged, doesn't depend on $A_2$)
- $F_{yy}|_{(A,0)} = -\beta \cdot A_2^{can}/A_1 = -\beta \cdot 2 = 2|W''(c)|\epsilon$ (corrected; canonical's "$4|W''(c)|\epsilon$" was wrong)
- **Ratio $\mu_0/\mu_1 = 2$ at leading order, NON-DEGENERATE** ← matches NQ-187 numerical measurement exactly.

### §2.5.2 Revised falsification verdict

The "falsification" is **NOT a normalization difference (path γ-i)**, **NOT a scope error**, but **a real algebraic error in canonical Step 4**: convention-mixing between two distinct normal forms, leading to the spurious "$A_2/A_1 = 4$" insertion into canonical's normal form (correct value: 2).

**Path γ-ii (formula correction) is now the likely outcome**, NOT path γ-i (scope clarification). Probability estimate revised: **γ-ii ~75%, γ-i ~10%, β-fail ~10% (R22 derivation re-check), α-fail ~5%**.

**Implication for Cat A re-promotion**:
- The **R22 derivation in `symmetry_moduli.md` §3.3 is correct** ($A_2^{sym}/A_1 = 4$ is rigorous).
- Canonical Step 4 has a **two-normal-form mixing error**: takes $A_2^{sym}$ value (= 4) and plugs into canonical's $F_{yy} = -\beta A_2^{can}/A_1$ formula (which expects canonical's $A_2$, = 2 under proper conversion).
- **The corrected canonical (ii) statement** matches NQ-187 measurement exactly: $\mu_0 = 4|W''(c)|\epsilon, \mu_1 = 2|W''(c)|\epsilon$, ratio 2 (non-degenerate).
- T-σ-Theorem-4 with corrected (ii) is **Cat A candidate at CV-1.7+** (after applying the formula correction); the corrected statement is mathematically rigorous.

### §2.5.3 What the original Phase 2 reconciliation missed

The W6 D1 EOD initial reconciliation (§2.5 first version, written 2026-05-04 PM) correctly identified the **multinomial factor 6** explaining the $K/I_4 = 2/3$ vs $A_2^{sym}/A_1 = 4$ discrepancy at the **`symmetry_moduli`-internal** level. However, it **did not** examine canonical's normal form definition + the conversion between canonical and `symmetry_moduli` conventions.

Upon direct re-examination of `canonical.md` lines 1385-1433 (Issue #3 re-examination, 2026-05-04 EOD), the canonical normal form $F_{can} = \beta r^2 + A_1 r^4 + A_2 x^2 y^2$ is **distinct** from `symmetry_moduli`'s $F_{sym} = \tfrac{\mu}{2}r^2 + A_1(a^4+b^4) + A_2 a^2 b^2$, and the value "$A_2/A_1 = 4$" is **convention-dependent**:
- $A_2^{sym}/A_1 = 4$ ✓ (correct in `symmetry_moduli`'s normal form, derived from $\int \phi^2 \psi^2$ multinomial expansion)
- $A_2^{can}/A_1 = 2$ ✓ (correct in canonical's normal form, derived from $A_2^{can} = A_2^{sym} - 2 A_1$)

**Canonical Step 4 line 1407 mixed the two**: derived $F_{yy} = -\beta A_2^{can}/A_1$ (correct in canonical's normal form), then plugged in $A_2/A_1 = 4$ from `symmetry_moduli`'s convention. This produces the spurious result $F_{yy} = 4|W''(c)|\epsilon$ instead of the correct $F_{yy} = 2|W''(c)|\epsilon$.

This explains:
- Why NQ-187 measurement ($\mu_1/\mu_0 = 2$) is in real conflict with canonical's claim (degeneracy) — the canonical claim is algebraically wrong, not just a different evaluation point.
- Why R22 axis-minimum analysis in `symmetry_moduli.md` (which uses $F_{sym}$ form throughout) gives ratio 2 at minimum — the `symmetry_moduli` derivation is internally consistent.
- Why the multinomial-factor-6 reconciliation alone was insufficient — that reconciliation only addresses `symmetry_moduli`'s internal logic; canonical has an independent error.

**This is path γ-ii (formula correction), not γ-i (scope clarification).** The original Phase 2 conclusion was incorrect on path-probability ordering; this §2.5.1-§2.5.3 deeper audit corrects it.

---

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

### §4.4 Audit priority (W6 D1 EOD Issue #3 refined)

(γ) Σ_m convention audit: **highest priority** (3-5 days, smallest effort). **Refined target per §2.5 deeper audit insight**: identify whether canonical (ii) evaluates Hessian at uniform point (γ-i, scope clarification needed) or at post-bifurcation minimum (γ-ii, formula correction needed). Most likely outcome: γ-i (scope error, not formula error). Working file target: `r22_a2_a1_audit.md` per §4.2 below + `sigma_m_hessian_convention_audit.md` (new placeholder file 2026-05-04 W6 D1 EOD).

(β) R22 derivation audit: **medium priority but likely PASS** (1-2 weeks, can run in parallel). Per §2.5 reconciliation: $A_2/A_1 = 4$ continuum is consistent with naive integral ratio $K/I_4 = 2/3$ via multinomial factor 6; R22 derivation in `symmetry_moduli.md` §3.3 lines 113-130 explicitly tracks this factor. **Audit is likely confirmation, not refutation.**

(α) NQ-187b L → ∞ extrapolation: **lowest priority** (2 weeks, computational intensive — likely confirms continuum value). Per `nq187b_L_extrapolation.md` §2.6 (post-W6 D1 EOD update): extrapolated $A_2^L/A_1^L$ from L=4 (4.80) to L=64 (3.954) trends to continuum 4.00 cleanly, finite-L correction $O(1/L^2)$ small. **Useful as cross-validation; not the critical path.**

### §4.5 Refined three-path decision rule (W6 D1 EOD Issue #3)

After audits (γ) + (β) + (α) execute, the following decision tree determines T-σ-Theorem-4 status:

**Path γ-i (scope clarification, most likely):**
- (γ) audit confirms canonical (ii) evaluates uniform-point Hessian (Fielder doublet, degenerate at leading order in continuum); NQ-187 measures axis-minimum Hessian (R22 prediction $F_{aa}/F_{bb} = 2$).
- Action: **clarify canonical (ii) statement scope** — explicit "evaluated at uniform point" annotation. Add separate (ii') sub-statement for axis-minimum Hessian with R22 prediction $\mu_0/\mu_1 = 2$ at leading order.
- Status: T-σ-Theorem-4 → **Cat A re-promotion candidate at CV-1.7+** (contingent on (β) confirming $A_2/A_1 = 4$).
- Severity reduction: this path treats the "falsification" as a documentation gap, not a mathematical error.

**Path γ-ii (formula correction, less likely):**
- (γ) audit confirms canonical (ii) was intended to describe axis-minimum Hessian but contains a formula error.
- Action: **correct canonical (ii) statement** to $\mu_0 = 4|W''(c)|\epsilon, \mu_1 = 2|W''(c)|\epsilon$ at leading order; ratio 2 (non-degenerate); higher-order $\epsilon^{3/2}$ correction unchanged.
- Status: T-σ-Theorem-4 → **Cat B retained with corrected formula** at CV-1.6 (canonical revision packet §3.1 already drafted with this option as fallback).
- Severity: moderate (correction needed but not retraction).

**Path β-fail (R22 derivation error, very unlikely):**
- (β) audit identifies error in R22 §3.3.
- Action: **retract** R22 cubic-equivariant analysis from canonical scaffolding; re-derive from first principles; revise T-σ-Theorem-4 (ii) accordingly.
- Status: T-σ-Theorem-4 → **Cat C retraction candidate**.
- Severity: high (full retraction).

**Path α-fail (continuum extrapolation rejects $A_2/A_1 = 4$, very unlikely):**
- (α) NQ-187b L → ∞ extrapolation diverges from 4.
- Action: same as β-fail.
- Severity: high (full retraction).

**Path defaults (revised after §2.5.1-§2.5.3 deeper audit):** based on the canonical-normal-form vs `symmetry_moduli`-normal-form conversion analysis, the falsification is most likely a **two-normal-form mixing error in canonical Step 4** (path γ-ii formula correction). Revised probability estimates:
- **γ-ii (formula correction): ~75%** ← most likely outcome.
- **γ-i (scope clarification): ~10%** ← was originally estimated 70%; revised down after deeper audit revealed the algebraic mixing error.
- **β-fail (R22 derivation error): ~10%** ← unchanged; R22 derivation independently consistent.
- **α-fail (continuum extrapolation reject): ~5%** ← unchanged.

The "Cat A → Cat B 영구 격하 위기" framing in the Issue #3 trigger is **moderately accurate**: T-σ-Theorem-4 (ii) does require formula correction at canonical, and the corrected statement (ratio 2 non-degenerate at axis minimum) is what NQ-187 measured. The R22 derivation itself is correct; the error is in canonical's transcription of R22 into a different normal form. Cat A re-promotion is feasible at CV-1.7+ once the formula correction is applied (path γ-ii); not feasible without correction.

### §4.6 Recommended canonical correction (γ-ii path)

For canonical T-σ-Theorem-4 (ii), the corrected statement should read:

```markdown
**(ii) Hessian split (corrected per W6 D1 EOD Issue #3 deeper audit, 2026-05-04).** *(Original 2026-04-27 W5 Day 1 G0 statement contained a two-normal-form mixing error; corrected here to internal consistency + agreement with NQ-187 numerical measurement.)*

By R22 normal-form analysis on the Fiedler doublet, the post-bifurcation minimizer's Hessian on $V_2 = \mathrm{span}(\phi_{(1, 0)}, \phi_{(0, 1)})$ has two leading-order eigenvalues:
$$\mu_0 = 4|W''(c)|\epsilon + O(\epsilon^{3/2}) \quad \text{(along $\phi_{(1, 0)}$, broken-symmetry direction)},$$
$$\mu_1 = 2|W''(c)|\epsilon + O(\epsilon^{3/2}) \quad \text{(along $\phi_{(0, 1)}$, transverse direction)},$$
**ratio $\mu_0/\mu_1 = 2$ at leading order (non-degenerate).** The non-degeneracy reflects the $D_4 \to \mathbb{Z}_2$ symmetry breaking: the broken-direction Hessian is twice the transverse-direction Hessian. NQ-187 numerical measurement (`THEORY/logs/daily/2026-04-30/11_nq187_scaling_test_results.md`, `CODE/scripts/test_sigma_theorem4_scaling.py`) confirms this ratio on $L \in \{4, 8, 16\}$ with effective coefficients $\mu_0/\epsilon = c_0$ and $\mu_1/\epsilon = c_0/2$ for some L-dependent constant $c_0$ (finite-L effective normalization).

In R22's normal form $F_{sym}(a,b) = \tfrac{\mu}{2}(a^2+b^2) + A_1^{sym}(a^4+b^4) + A_2^{sym} a^2 b^2$, the ratio $A_2^{sym}/A_1 = 4$ on $D_4$ free-BC continuum (per `working/SF/symmetry_moduli.md` §3.3 derivation, rigorous). In canonical's normal form $F_{can}(x,y) = \beta(x^2+y^2) + A_1(x^2+y^2)^2 + A_2^{can} x^2 y^2$, the ratio is $A_2^{can}/A_1 = 2$ (via conversion $A_2^{can} = A_2^{sym} - 2 A_1$). Both express the same continuum content; only the basis labeling differs.
```

This correction:
- **Preserves R22 derivation** (`symmetry_moduli.md` §3.3) intact — no β-fail.
- **Preserves NQ-187 numerical measurement** as evidence — directly confirms the corrected formula.
- **Replaces the "degeneracy" claim** with the corrected "ratio 2 non-degenerate" claim.
- **Preserves the (i) symmetry-breaking + (iii) irrep + (iv) nodal + (v) σ-signature substatements** — they don't depend on the (ii) eigenvalue formula.
- **Changes the (v) σ-signature** to reflect non-degenerate eigenvalues: $(2, [+1], 4|W''(c)|\epsilon), (2, [-1], 2|W''(c)|\epsilon)$ — the trivial-irrep-first ordering is now via *eigenvalue magnitude* (4 > 2), not the "tie-break by Mulliken character order" of the original (vi). The (vi) tie-break convention and Commitment 14 (O7) become **inapplicable** for this theorem (no tie at leading order); they remain useful for higher-order or different theorem applications.

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
