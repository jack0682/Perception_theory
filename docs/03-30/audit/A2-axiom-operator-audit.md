# A2: Axiom, Operator, and Diagnostic Predicate Consistency Audit

**Author:** Axiom & Operator Consistency Auditor | **Date:** 2026-03-30

**Scope:** All axiomatic statements, operator definitions, and diagnostic predicate definitions across Canonical Spec v1.0, Canonical Spec v2.0, `scc/operators.py`, `scc/diagnostics.py`, `scc/params.py`, `papers/paper1_math.tex`, and `papers/paper2_cogsci.tex`. Cross-referenced with I5-ontological-audit, I6-registries, and I6-verification-report.

---

## Severity Legend

| Tag | Meaning |
|-----|---------|
| **TERMINOLOGICAL** | Naming inconsistency across documents |
| **FORMAL** | Mathematical definition differs between sources |
| **PROOF-BLOCKING** | Gap prevents a stated theorem from holding |
| **ONTOLOGICAL** | Philosophy-formalism mismatch |
| **COMPUTATIONAL** | Code does not match spec |

---

## 1. CLOSURE OPERATOR (Cl_t)

### Issue 1.1 — TERMINOLOGICAL: "Closure" is triply overloaded

The word "closure" is used in three distinct senses throughout the theory:

1. **Topological closure**: Extensive, monotone, idempotent. Referenced in §4 of v2.0 and interpretive remarks on A3.
2. **SCC soft closure operator Cl_t**: Monotone (A2), conditionally extensive (A1'), deliberately non-idempotent, contractive (A3). A sigmoid-based operator.
3. **Gestalt closure (Geschlossenheit)**: Perceptual completion of incomplete figures. Referenced in paper2_cogsci.tex line 171.

**Assessment:** The spec is reasonably careful about distinguishing these (the interpretive remark on A3 explicitly addresses idempotence), but the term "closure" carries strong connotations of idempotence from topology. The theory's closure satisfies NONE of the three classical closure axioms unconditionally (extensivity is conditional, idempotence is absent, and the operator is contractive). Calling it "closure" is a persistent source of confusion.

**Recommendation:** Consider a parenthetical qualifier in key locations: "soft closure (contractive, non-idempotent)" or define a short alias. This is cosmetic, not structural.

---

### Issue 1.2 — FORMAL: A1' conditional extensivity has an unspecified parameter

**v2.0 §6, Group A, A1':**
$$\mathrm{Cl}_t(u)(x) \geq u(x) \quad \text{whenever } u(x) > 0 \text{ and } (P_t u)(x) \geq \theta_{\mathrm{support}} \cdot u(x)$$

The parameter $\theta_{\mathrm{support}} \in (0,1]$ is introduced but **never assigned a value or range**. It does not appear in `params.py`, is not validated, and is not referenced in any theorem statement or proof.

**Cross-document status:**
- v1.0: A1 was "weak extensivity" with vague "local relational support" condition — no parameter.
- v2.0: A1' introduces $\theta_{\mathrm{support}}$ but leaves it unbound.
- paper1_math.tex: States A1' but does not specify $\theta_{\mathrm{support}}$.
- paper2_cogsci.tex: Does not mention A1' explicitly.
- Code: No implementation of A1' checking; no `theta_support` parameter.

**Severity: FORMAL + PROOF-BLOCKING.** A1' cannot be verified for the sigmoid realization without knowing $\theta_{\mathrm{support}}$. T20 (Axiom Consistency) claims A1' is satisfied but does not specify for what values of $\theta_{\mathrm{support}}$.

---

### Issue 1.3 — FORMAL: A1' creates a layer-crossing dependency (acknowledged but unresolved)

A1' references $P_t$, which is a provisional realization (§9.1). The spec acknowledges this (layer-crossing note) and states A1' holds for "any local aggregation operator satisfying B1-B4." However:

- No formal proof that A1' holds for ALL such operators — only for the specific $P_t$.
- If $P_t$ is replaced (as the theory permits), A1' must be re-verified.
- The axiom is therefore not purely axiomatic; it is conditional on the provisional layer.

**Severity: FORMAL.** The axiom-realization separation is compromised. This was flagged as I6-verification-report priority fix #5 but not resolved.

---

### Issue 1.4 — FORMAL: Cl_t codomain is (0,1)^n, not [0,1]^n

The sigmoid function $\sigma(z) = 1/(1+e^{-z})$ maps $\mathbb{R} \to (0,1)$, never reaching exactly 0 or 1. Therefore:

$$\mathrm{Cl}_t : [0,1]^n \to (0,1)^n \subset [0,1]^n$$

The spec states $\mathrm{Cl}_t : [0,1]^n \to [0,1]^n$, which is technically true (the range is a subset of the codomain) but **the image never includes the boundary values 0 or 1**. This means:

- A field with $u(x) = 0$ always has $\mathrm{Cl}_t(u)(x) > 0$: closure adds cohesion to zero-participation sites.
- A field with $u(x) = 1$ always has $\mathrm{Cl}_t(u)(x) < 1$: closure reduces maximal cohesion.
- The closure residual $\|u - \mathrm{Cl}_t(u)\|$ is **always positive** for any non-trivial field (explaining why Bind caps at ~0.85).

**Severity: FORMAL.** Not proof-blocking (the image is a subset of [0,1]^n), but the discrepancy between actual image and stated codomain has downstream consequences for the Bind predicate interpretation. The spec should note that the image is the open cube.

---

### Issue 1.5 — FORMAL: A3 contraction rate — is it global or local?

**v2.0 §6, A3:** Claims contraction with geometric rate $a_{\mathrm{cl}}/4$ for ALL $u \in [0,1]^n$.

**Analysis:** The Lipschitz constant of $\mathrm{Cl}_t$ is bounded by:
$$\|\mathrm{Cl}_t\|_{\mathrm{Lip}} \leq \max_{z} \sigma'(z) \cdot a_{\mathrm{cl}} \cdot \max(1-\eta_{\mathrm{cl}}, \eta_{\mathrm{cl}}) \leq \frac{a_{\mathrm{cl}}}{4}$$

Since $\max \sigma' = 1/4$ and $\max(1-\eta, \eta) \leq 1$ for $\eta \in [0,1]$.

This bound is GLOBAL (holds for all $u \in [0,1]^n$), as stated. The contraction is uniform. This is correct.

**However:** The bound is tight only when $\eta_{\mathrm{cl}} \in \{0, 1\}$. For the default $\eta_{\mathrm{cl}} = 0.5$, the actual Lipschitz constant is $\leq a_{\mathrm{cl}} \cdot (1/4) \cdot 0.5 = a_{\mathrm{cl}}/8$, which is a significantly tighter bound. The spec correctly gives the worst-case bound.

**Severity: None.** The stated bound is correct. The tighter $\eta$-dependent bound could be noted as an optimization but is not an error.

---

### Issue 1.6 — FORMAL/ONTOLOGICAL: Is Cl_t a "closure" in any standard mathematical sense?

**Standard closure axioms (Kuratowski):**
1. Extensivity: $A \subseteq \mathrm{Cl}(A)$ — SCC: only conditional (A1')
2. Monotonicity: $A \subseteq B \implies \mathrm{Cl}(A) \subseteq \mathrm{Cl}(B)$ — SCC: YES (A2)
3. Idempotence: $\mathrm{Cl}(\mathrm{Cl}(A)) = \mathrm{Cl}(A)$ — SCC: deliberately NO
4. Normalization: $\mathrm{Cl}(\emptyset) = \emptyset$ — SCC: NO ($\mathrm{Cl}(0) = \sigma(-a_{\mathrm{cl}} \tau_{\mathrm{cl}}) > 0$)

SCC's closure satisfies **1 out of 4** Kuratowski axioms unconditionally. It is not a closure in any standard mathematical sense. It is a contractive self-map with a unique fixed point. The name is justified by the Gestalt inspiration (perceptual completion), not by mathematical ancestry.

**Severity: ONTOLOGICAL.** The theory acknowledges this (interpretive remark on A3, CN1). The deliberate departure from standard closure is well-documented. However, calling the operator "closure" when it satisfies none of the standard closure axioms is a persistent source of confusion in the mathematical paper (paper1_math.tex), where readers will expect the standard meaning.

---

## 2. DISTINCTION OPERATOR (D_t)

### Issue 2.1 — FORMAL: The "complement" 1-u is well-defined but ontologically loaded

D_t(x; 1-u) depends on $1-u$, called "the complement" or "the exterior field." The complement is well-defined pointwise: $(1-u)(x) = 1 - u(x) \in [0,1]$. It does not require $u$ to sum to any particular value.

However, the sum $\sum_x (1-u(x)) = n - m$, which is determined by the volume constraint. The "exterior" field has a fixed total mass. This is consistent but worth noting: the volume constraint simultaneously constrains both the formation AND its complement.

**Severity: None.** The complement is well-defined. The ontological concern (what does "exterior" mean for a field that doesn't partition?) is addressed by the theory's commitment to gradedness.

---

### Issue 2.2 — FORMAL: b_D = 0 loses expressiveness (claimed preservation via P_t(1-u) is unproved)

**v1.0:** D_t included a gradient term $b_D \cdot g_t(x; u)$ where $g_t(x;u) = \sum_y N_t(x,y)|u(x) - u(y)|$.

**v2.0:** Sets $b_D = 0$ for analyticity (required by T14, Lojasiewicz).

**Claim (v2.0 §9.3):** "Boundary sensitivity is preserved through the spatial structure of $P_t(1-u)$, which implicitly encodes boundary configuration."

**Assessment:** This claim is plausible but **unproved**. There is no theorem or formal argument showing that $P_t(1-u)$ carries equivalent boundary information to $g_t$. The claim is repeated in the D-Ax3 axiom text. The gradient indicator $g_t$ depends on $|u(x) - u(y)|$ (absolute local differences), while $P_t(1-u)$ depends on the weighted average of $1-u$ in the neighborhood (a smooth quantity). These are structurally different:

- $g_t$ is high at boundary sites where $u$ changes rapidly.
- $P_t(1-u)$ is high wherever the neighborhood has low cohesion, including deep exterior sites far from any boundary.

**Severity: FORMAL.** The claim of expressiveness preservation is not justified. D-Ax3 (boundary sensitivity) may not be satisfied by the b_D=0 realization as strongly as by the original.

---

### Issue 2.3 — FORMAL: D-Ax3 is weaker in v2.0 than in v1.0

**v1.0 D-Ax3:** "Distinction may incorporate sensitivity to the local gradient of cohesion."

**v2.0 D-Ax3:** "The explicit gradient term $b_D \cdot g_t$ from the v1.0 distinction candidate is set to zero... Boundary sensitivity is preserved through the spatial structure of $P_t(1-u)$."

The v2.0 axiom is now descriptive rather than prescriptive. It describes what the current realization does rather than imposing a structural requirement. This is a weakening of the axiomatic framework.

**Severity: FORMAL.** The axiom has become a description of the provisional realization, not a constraint that future realizations must satisfy.

---

## 3. CO-BELONGING OPERATOR (C_t)

### Issue 3.1 — FORMAL: C_t codomain inconsistency WITHIN v2.0

**v2.0 §3.6 (line 115):**
> $\mathbf{C}_t : X_t \times X_t \to [0,\infty)$

**v2.0 §6 Group C header (line 306):**
> The soft co-belonging operator $\mathbf{C}_t : X_t \times X_t \to [0,1]$

These are **contradictory within the same document**. The §3.6 text was updated to [0,∞) to reflect the resolvent realization (whose diagonal entries are ≥ 1), but the Group C axiom header was NOT updated. This was flagged as I6-verification-report priority fix #1 but **remains unfixed in the current spec text**.

**v1.0:** Said [0,1] (consistent with v1.0's undetermined operator form).

**Code (operators.py):** Returns raw resolvent diagonal values, which are ≥ 1. No normalization to [0,1].

**paper2_cogsci.tex line 229:** Says $C_t : X_t \times X_t \to [0,\infty)$ — matches §3.6.

**paper1_math.tex:** Uses C_t without explicit codomain in most places.

**Severity: FORMAL.** A direct contradiction within the canonical spec. The Group C axiom header must be corrected to [0,∞).

---

### Issue 3.2 — FORMAL: C_t is "diagnostic only" — principled or pragmatic?

**v2.0 §3.6:** "Co-belonging enters the theory's predicates... but does not enter the energy functional."

**I6-registries FC12:** "C_t diagnostic only" is listed as a fixed commitment.

**Assessment:** The stated reason is computational tractability: differentiating through the resolvent would be expensive. This is a pragmatic reason elevated to a fixed commitment. The theory does not provide an ontological argument for why co-belonging should be diagnostic-only. One could argue that co-belonging, as a measure of joint participation, should influence the energy (e.g., sites that co-belong should be energetically penalized for having different cohesion values).

**Severity: ONTOLOGICAL.** The decision is pragmatic (computational), not principled (philosophical). Listing it as a "fixed commitment" (FC12) overstates its theoretical grounding.

---

### Issue 3.3 — FORMAL: Neumann series truncation error is bounded but not documented in spec

The code (`operators.py` line 192) uses `k_neumann = 10` terms. The `params.py` validation (line 133-138) computes the Neumann truncation error bound $(\alpha_C \cdot \rho(W_{\mathrm{sym}}))^{K+1}$ and warns if > 1%.

**But:** The spec does not state the truncation error bound or justify the default $K=10$. The error depends on $\alpha_C \cdot \rho(W_{\mathrm{sym}})$, which varies with the field. The spec merely says "Neumann series truncation at $k$ terms."

**Severity: FORMAL.** Minor — the code handles this correctly, but the spec should document the truncation error bound.

---

## 4. DIAGNOSTIC PREDICATES

### Issue 4.1 — **CRITICAL** COMPUTATIONAL: Sep predicate — spec says C_t-weighted, code uses u-weighted

**v2.0 §7.1 (line 404-411):**
$$\mathsf{Sep}_t(u_t) = \frac{\sum_{x \in X_t} \mathbf{C}_t(x,x)\, \mathbf{D}_t(x;\, 1-u_t)}{\sum_{x \in X_t} \mathbf{C}_t(x,x)}$$

**Code (`diagnostics.py` line 51-63):**
```python
def sep_predicate(u, graph, params):
    D_u = distinction(u, graph, params)
    m = np.sum(u)
    return float(np.sum(u * D_u) / m)
```

This computes $\mathsf{Sep} = \sum_x u(x) \cdot D_t(x) / \sum_x u(x)$, which is **u-weighted**, NOT C_t-weighted.

**Cross-document status:**
| Source | Definition |
|--------|-----------|
| Canonical Spec v2.0 §7.1 | C_t-weighted |
| Canonical Spec v1.0 §7.1 | Crisp-threshold average over Int_t |
| `diagnostics.py` | **u-weighted** |
| paper1_math.tex line 261 | C_t-weighted (matches spec) |
| paper1_math.tex line 716 | Mentions u-weighted as experimental variant |
| paper2_cogsci.tex line 184 | C_t-weighted (matches spec) |

**The code does not implement the spec.** The code comment (line 55-57) explains the reason: "The original C_t-weighted-over-all-nodes version averaged ~0.5 regardless of formation quality because exterior nodes (D≈0) and interior (D≈1) cancel out."

**Which is authoritative?** The spec is the canonical reference, but the code's u-weighted version produces better diagnostic discrimination. The spec should either:
1. Change to u-weighted (matching the working code), or
2. The code should be updated to use C_t-weighting.

**Note:** The proved Sep-energy bridge ($\mathsf{Sep}_{\mathrm{old}} = 1 - \mathcal{E}_{\mathrm{sep}}/m$) holds for the u-weighted version (where the weights are u), NOT for the C_t-weighted version. Paper1_math.tex line 837 acknowledges this.

**Severity: COMPUTATIONAL + FORMAL.** This is the single most important discrepancy in the entire codebase. The code, both papers' experimental sections, and the proved theorem all use different definitions than what the spec declares authoritative.

---

### Issue 4.2 — FORMAL: Bind normalization — why √n?

**v2.0 §7.1:** $\mathsf{Bind}_t(u_t) = 1 - \|u_t - \mathrm{Cl}_t(u_t)\|_2 / \sqrt{n}$

**Code:** Matches spec.

**Why √n and not ‖u‖₂?** The spec explains: scale-independence, works for sparse fields, and enables the proved bound $\mathsf{Bind} \geq 1 - \sqrt{\mathcal{E}_{\mathrm{cl}}/n}$.

**Drift from v1.0:** v1.0 used Boolean: $\|u - \mathrm{Cl}(u)\| \leq \varepsilon_{\mathrm{cl}}$, no specified norm. v2.0 changed to graded [0,1] with ℓ² norm and √n normalization. This change is well-documented.

**Potential issue:** For $u \in [0,1]^n$, $\|u - \mathrm{Cl}(u)\|_2 \leq \sqrt{n}$ (since each component difference is ≤ 1). So Bind ∈ [0, 1]. But for realistic formations, the denominator √n may make Bind insensitive to local closure failures when n is large.

**Severity: FORMAL.** Minor. The choice is defensible and well-documented.

---

### Issue 4.3 — **CRITICAL** PROOF-BLOCKING: QM1 (Q_morph vanishes on uniform fields) appears FALSE

**v2.0 §13 (line 797-798):**
> QM1 (vanishing on uniform fields). *Proof:* QM1 — uniform fields have Artic = 0.

**Analysis for a uniform field $u \equiv c > 0$ on a connected graph:**

In the superlevel-set filtration (decreasing threshold from 1 to 0):
- At threshold $c$: ALL $n$ nodes appear simultaneously (all have value $c$).
- They form $n$ singleton components, each born at value $c$.
- As the union-find processes them (arbitrary tie-breaking), adjacent nodes merge.
- Each merge kills one component with bar length $c - c = 0$ (birth and death at same value).
- One component survives with the "infinite bar": birth at $c$, death at 0, length = $c$.

Therefore:
- $\ell_{\max} = c > 0$
- $\ell_{\mathrm{second}} = 0$ (all merge bars have length 0)
- $\mathrm{Artic} = 1 - 0/c = 1$
- $\mathcal{Q}_{\mathrm{morph}} = c \cdot 1 = c \neq 0$

**The spec claims Artic = 0 for uniform fields. The actual value is Artic = 1.**

**The code (`diagnostics.py` _persistence_h0_graph) confirms this:** For equal-valued nodes, all merge bars have zero length, l_max = max(u) = c, l_second = 0, Artic = 1.

QM1 as stated ("vanishing on uniform fields") is FALSE for the current definition. $\mathcal{Q}_{\mathrm{morph}}(c\mathbf{1}) = c$ for any constant $c > 0$.

**Impact:** QM1 is used to justify that Q_morph distinguishes structured from unstructured fields. Without QM1, the Inside predicate assigns non-zero morphological quality to featureless uniform fields, which contradicts the conceptual intent.

**Severity: PROOF-BLOCKING.** QM1 is false. The proof in the proved results registry is incorrect. The formula may need revision (e.g., incorporating a normalization by c, or redefining Artic to account for tie-breaking in uniform fields).

---

### Issue 4.4 — FORMAL: Inside predicate edge cases

**When there is only one persistence bar (n=1 or all nodes in one component from the start):**
- $\ell_{\mathrm{second}} = 0$, Artic = 1, Inside = $\ell_{\max}$.
- This is handled correctly by the code (line 137: `l_second = all_bars[1] if len(all_bars) > 1 else 0.0`).

**When $\ell_{\max} = 0$ (all u values are 0):**
- Code returns 0.0 (line 75-76). Correct.

**Severity: None.** Edge cases are handled.

---

### Issue 4.5 — **CRITICAL** COMPUTATIONAL: Persist predicate — code completely differs from spec

**v2.0 §7.1 (line 440-443):**
$$\mathsf{Persist}_W(\mathbf{u}) = \min_{t < s \in W} \frac{\sum_{x \in \mathrm{Core}_t} \sum_{y \in \mathrm{Core}_s} \mathbf{M}_{t \to s}(x,y)\, u_s(y)}{\rho_{\mathrm{persist}}}$$

This requires: transport kernel $M_{t \to s}$, core extraction at both times, and a temporal window $W$.

**Code (`diagnostics.py` line 142-149):**
```python
def persist_predicate(u_prev, u_curr):
    if u_prev is None:
        return 1.0
    norm_prev = np.linalg.norm(u_prev)
    if norm_prev < 1e-12:
        return 0.0
    return float(max(0.0, 1.0 - np.linalg.norm(u_curr - u_prev) / norm_prev))
```

This computes $\mathsf{Persist} = 1 - \|u_{\mathrm{curr}} - u_{\mathrm{prev}}\|_2 / \|u_{\mathrm{prev}}\|_2$, which is a simple relative field-change measure. It does NOT use:
- Transport kernel $M_{t \to s}$
- Core extraction
- Any temporal window structure
- The formula from the spec

**paper1_math.tex line 272:** Uses the spec formula (core-inheritance based).

**paper1_math.tex line 718:** Notes "temporal persistence has not been computationally validated — no multi-time transport experiments have been conducted."

**Severity: COMPUTATIONAL + FORMAL.** The code implements a completely different quantity than what the spec defines. The code version is a placeholder (acknowledged by the `= 1.0` default for static optimization and the `u_prev is None` guard). The spec formula has never been implemented.

---

### Issue 4.6 — FORMAL: Persist has zero proved results

**v2.0 §7.1 (line 445):** "The persistence predicate has zero proved results across all iterations."

**paper1_math.tex line 841:** Notes 3 of 6 proof gaps closed for T-Persist-1, 3 remain.

All documents agree on this. The temporal dimension is the theory's acknowledged weakest point.

**Severity: FORMAL.** Acknowledged openly. Not a hidden gap.

---

## 5. CROSS-DOCUMENT DEFINITION CONSISTENCY

### Issue 5.1 — Operator definition consistency matrix

| Operator | Spec v2.0 | Code | paper1_math.tex | paper2_cogsci.tex | Status |
|----------|-----------|------|-----------------|-------------------|--------|
| **Cl_t** | σ(a_cl((1-η)u + η·P_t·u - τ)) | Same | Same | Same | **CONSISTENT** |
| **D_t** | σ(a_D(P_t·u - λ_D·P_t(1-u)) - τ_D) | Same | Same | Same | **CONSISTENT** |
| **C_t** | (I - α·W_sym)^{-1} | Neumann truncation | Same (Neumann noted) | Same | **CONSISTENT** (implementation approximation documented) |
| **P_t** | Σ K(x,y)f(y)/(Σ K(x,y) + ε) | Same | Same | Same | **CONSISTENT** |
| **Bind** | 1 - ‖u - Cl(u)‖₂/√n | Same | Same | Same | **CONSISTENT** |
| **Sep** | C_t-weighted | **u-weighted** | C_t-weighted (spec), u-weighted (experiments) | C_t-weighted | **INCONSISTENT** (see Issue 4.1) |
| **Inside** | Q_morph = l_max · Artic | Same | Same | Same | **CONSISTENT** |
| **Persist** | Core-inheritance formula | **Field-change ratio** | Core-inheritance | Not detailed | **INCONSISTENT** (see Issue 4.5) |

---

### Issue 5.2 — FORMAL: v2.0 Group C codomain [0,1] vs §3.6 codomain [0,∞)

As detailed in Issue 3.1. The Group C axiom header at §6 line 306 says [0,1]; §3.6 line 115 says [0,∞). This is a direct internal contradiction. The I6-verification-report flagged this (priority fix #1) but it was NOT corrected.

---

### Issue 5.3 — FORMAL: E_bd summation convention in v1.0 vs v2.0

**v1.0 §8.3:** $\sum_{x,y}$ without specifying ordered vs unordered pairs.

**v2.0 §0:** Explicit ordered-pair summation convention. §8.4 references this.

**Impact:** The factor in the Hessian changes: ordered pairs give $4\alpha L$, unordered pairs would give $2\alpha L$. The phase transition threshold (T8-Core) depends on this factor. v2.0 is correct and explicit. v1.0 was ambiguous.

**Severity: FORMAL.** Resolved in v2.0. The v1.0 ambiguity was the source of the "2λ₂ vs 4λ₂" confusion documented in I6-registries as a false claim.

---

### Issue 5.4 — TERMINOLOGICAL: E1 naming — "Sub-Stochasticity" vs "Soft Stochasticity"

**v1.0 §6 Group E, E1:** "Soft Stochasticity"

**v2.0 §6 Group E, E1:** "Sub-Stochasticity"

Both define the same condition ($\sum_y M_{t \to s}(x,y) \leq 1$). The name change is an improvement (sub-stochastic is the standard mathematical term) but creates a minor naming inconsistency between versions.

**Severity: TERMINOLOGICAL.** Trivial.

---

### Issue 5.5 — FORMAL: E3 reclassification — axiom to solution constraint

**v1.0:** E3 (Core Inheritance) is an axiom: "The transport kernel **must** preferentially preserve the cohesive core."

**v2.0:** E3 reclassified as a solution constraint: "It characterizes what transport *should achieve at formation-structured fields*, not what the kernel *must satisfy universally*."

**Impact:** In v1.0, a transport kernel that fails E3 is axiomatically invalid. In v2.0, a transport kernel that fails E3 at non-formation-structured fields is still valid. This is a weakening of the axiomatic system that reduces the constraints on the transport operator.

**Severity: FORMAL.** Well-motivated (E3 at arbitrary fields is too strong) but not trivially compatible with the v1.0 framework. Any results proved under v1.0's stronger E3 would need re-examination.

---

## 6. PHILOSOPHY-FORMALISM MISMATCHES

### Issue 6.1 — ONTOLOGICAL: Closure fixed point uniqueness vs. philosophical claims

**Philosophy (§2, §4, §10):** "Coherent formation precedes discrete objecthood." Multiple formations should be possible.

**Mathematics (T6b):** In the contraction regime ($a_{\mathrm{cl}} < 4$), the closure operator has a UNIQUE fixed point.

**Resolution attempt (CN9, Two-Landscape Structure):** Multiple formations arise from the energy landscape (multiple metastable minima), not from closure (unique fixed point).

**Assessment:** The resolution is coherent but subtle. The philosophical narrative often talks about closure "completing" formations, while mathematically the closure operator converges to a single universal fixed point regardless of starting field. The multiplicity of formations comes entirely from the energy minimization, not from closure itself. This is well-documented in the commitment notes but not always clear in the papers.

**Severity: ONTOLOGICAL.** Documented and resolved via CN9, but the papers could be clearer about this distinction.

---

### Issue 6.2 — ONTOLOGICAL: C_t diagnostic-only status undermines the operator triad

**Claim (§10, CN7):** The theory's distinctive feature is a "triple-mode operator triad": self-completion (Cl_t), self-contrast (D_t), self-integration (C_t).

**Reality:** C_t enters predicates but NOT the energy. The energy optimization that finds formations uses only Cl_t and D_t. C_t is computed after-the-fact as a diagnostic.

**Impact:** The "operator triad" is asymmetric: two operators are variational (participate in formation-finding), one is purely diagnostic (post-hoc assessment). The "self-integration" mode of self-referentiality does not participate in the formation process. This weakens the philosophical claim of triple-mode self-referentiality.

**Severity: ONTOLOGICAL.** The theory's distinctive claim (triple-mode self-referentiality) is partially undermined by C_t's diagnostic-only status. The theory effectively has dual-mode variational self-referentiality (Cl_t, D_t) plus a diagnostic operator (C_t).

---

## 7. ADDITIONAL ISSUES

### Issue 7.1 — COMPUTATIONAL: Double-well gradient factor

**CLAUDE.md states:** "W'(u) = 2u(1-u)(1-2u) — factor of 2 (I6 correction)."

The standard derivative of $W(u) = u^2(1-u)^2$ is:
$$W'(u) = 2u(1-u)(1-2u)$$

This is the factor-of-2 correction from I6 (not $u(1-u)(1-2u)$ as some implementations had). This should be verified in `energy.py`.

**Severity: COMPUTATIONAL.** The correction is documented; verify implementation.

---

### Issue 7.2 — FORMAL: W_sym definition in C_t — degree normalization ambiguity

**v2.0 §6 Group C (line 330):** "entries $W_{\mathrm{sym}}(x,y) = \sqrt{u_t(x)}\, \mathbf{N}_t(x,y)\, \sqrt{u_t(y)} / d_x$ for appropriate degree normalization $d_x$"

The "appropriate" $d_x$ is not specified. Is it the degree of node $x$ in the adjacency graph? The weighted degree? The code should be checked for the exact formula.

**Severity: FORMAL.** Ambiguous specification of a load-bearing quantity.

---

### Issue 7.3 — FORMAL: C3'' (local monotonicity) proof gap

**v2.0 §13 (line 793-794):** "The C3'' proof relies on a Neumann series monotonicity argument where the symmetrization step ($D^{-1/2}$ depends on $u_t(x)$) awaits formal verification."

This gap was flagged in v2.0 itself and in I6-verification-report (priority fix #4). It remains open.

**Severity: PROOF-BLOCKING.** C3'' is not rigorously proved for the resolvent realization.

---

## SUMMARY TABLE

| # | Issue | Severity | Status |
|---|-------|----------|--------|
| 1.1 | "Closure" triple overload | TERMINOLOGICAL | Acknowledged in spec |
| 1.2 | A1' θ_support unspecified | FORMAL + PROOF-BLOCKING | **OPEN** |
| 1.3 | A1' layer-crossing dependency | FORMAL | Acknowledged, unresolved |
| 1.4 | Cl_t image is (0,1)^n not [0,1]^n | FORMAL | Not documented |
| 1.5 | A3 contraction rate — global? | None | Correct as stated |
| 1.6 | Cl_t not a closure in any standard sense | ONTOLOGICAL | Acknowledged |
| 2.1 | 1-u complement well-definedness | None | Fine |
| 2.2 | b_D=0 expressiveness claim unproved | FORMAL | **OPEN** |
| 2.3 | D-Ax3 weakened to description | FORMAL | **OPEN** |
| 3.1 | C_t codomain [0,1] vs [0,∞) within v2.0 | FORMAL | **UNFIXED** (I6 fix #1) |
| 3.2 | C_t diagnostic-only: pragmatic not principled | ONTOLOGICAL | Elevated to FC12 |
| 3.3 | Neumann truncation error undocumented in spec | FORMAL | Minor |
| 4.1 | **Sep: C_t-weighted (spec) vs u-weighted (code)** | **COMPUTATIONAL + FORMAL** | **CRITICAL — MUST RESOLVE** |
| 4.2 | Bind √n normalization | FORMAL | Justified, minor |
| 4.3 | **QM1 (vanishes on uniform fields) is FALSE** | **PROOF-BLOCKING** | **CRITICAL — THEOREM INCORRECT** |
| 4.4 | Inside edge cases | None | Handled |
| 4.5 | **Persist: code implements different formula** | **COMPUTATIONAL + FORMAL** | **CRITICAL — PLACEHOLDER** |
| 4.6 | Persist has zero proved results | FORMAL | Acknowledged |
| 5.1 | Operator definition matrix | Mixed | See table |
| 5.2 | Group C codomain contradiction | FORMAL | **UNFIXED** |
| 5.3 | E_bd summation convention | FORMAL | Resolved in v2.0 |
| 5.4 | E1 naming change | TERMINOLOGICAL | Trivial |
| 5.5 | E3 reclassification | FORMAL | Well-motivated |
| 6.1 | Unique fixed point vs multiple formations | ONTOLOGICAL | Resolved via CN9 |
| 6.2 | C_t diagnostic-only undermines operator triad | ONTOLOGICAL | Acknowledged tension |
| 7.1 | Double-well gradient factor | COMPUTATIONAL | Verify in energy.py |
| 7.2 | W_sym degree normalization ambiguous | FORMAL | **OPEN** |
| 7.3 | C3'' proof gap | PROOF-BLOCKING | **OPEN** |

---

## CRITICAL ACTIONS REQUIRED

1. **Resolve Sep definition** (Issue 4.1): The spec, code, and proved theorems use three different definitions. The u-weighted version in the code has the proved energy bridge and better diagnostic discrimination. Recommend updating the spec to u-weighted and noting C_t-weighted as an alternative.

2. **Fix QM1** (Issue 4.3): Either revise the $\mathcal{Q}_{\mathrm{morph}}$ formula to actually vanish on uniform fields (e.g., subtract the uniform-field baseline, or redefine Artic), or weaken QM1 to "near-vanishing" with appropriate bounds.

3. **Document Persist placeholder** (Issue 4.5): The code's persist_predicate is a completely different quantity from the spec definition. Either implement the spec formula or explicitly document the code version as a proxy.

4. **Fix C_t codomain** (Issue 3.1): Change Group C header from [0,1] to [0,∞) to match §3.6. This is a one-line fix.

5. **Specify θ_support** (Issue 1.2): Give A1' a concrete parameter value or range, or acknowledge it as open.
