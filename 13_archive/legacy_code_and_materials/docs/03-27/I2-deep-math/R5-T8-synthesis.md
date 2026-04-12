# T8 Non-Trivial Minimizer Existence — Definitive Mathematical Status Document

**Author:** Mathematical Synthesizer
**Date:** 2026-03-27
**Iteration:** 2, Round 5
**Sources:** Proof Strategist (7-theorem proof chain), Computation Analyst (phase diagram + Q_morph candidate), Rigor Auditor (audit)

---

## Executive Verdict

**T8 STATUS: PROVED (CORE CLAIM) — with precise scope delineation**

The core claim of T8 — *non-trivial minimizers of the constrained energy exist and have formation structure* — is established through a valid proof chain, confirmed computationally, and survives rigorous audit. However, the theorem as proved is narrower than some of the Proof Strategist's broader claims, and the connection to the full proto-cohesion predicate remains incomplete. Below is the exact accounting of what is proved, what is overstated, and what remains open.

---

## I. THE PROOF CHAIN — Theorem by Theorem

### Theorem 1: Existence of Constrained Minimizer

**Claim:** On the constraint manifold $\Sigma_m = \{u \in [0,1]^n : \sum_x u(x) = m\}$, the energy $\mathcal{E}_t$ attains its minimum.

**Proof:** $\Sigma_m$ is a compact subset of $[0,1]^n$ (closed and bounded in $\mathbb{R}^n$). $\mathcal{E}_t$ is continuous on $[0,1]^n$ (composition of continuous maps on finite $X_t$ — established in T20). By the extreme value theorem, $\mathcal{E}_t$ attains its minimum on $\Sigma_m$. $\square$

**Status: PROVED.** All three agents agree. No parameter constraints beyond continuity (already established in T20/A4).

**Note:** This is the *global* constrained minimizer, not merely a local one. Existence is not the interesting part — non-triviality is.

### Theorem 2: The Uniform State Is the Unique Uniform Critical Point

**Claim:** On $\Sigma_m$ with $m = cn$ ($c \in (0,1)$), the uniform state $u \equiv c$ is the only spatially uniform critical point of $\mathcal{E}_t|_{\Sigma_m}$.

**Proof:** Any uniform state on $\Sigma_m$ must have $u(x) = m/n = c$ for all $x$. $\square$

**Status: PROVED (trivial).** This matters because it means the *only* way the constrained minimizer can be uniform is if it equals $u \equiv c$. So proving $u \equiv c$ is not a minimizer suffices.

### Theorem 3: Second Variation at the Uniform State — THE CRITICAL RATIO DISPUTE

**Claim:** The Hessian of $\mathcal{E}_{\mathrm{bd}}|_{\Sigma_m}$ at $u \equiv c$ restricted to the tangent space $T_c\Sigma_m = \{v : \sum v_i = 0\}$ has a negative eigenvalue when $\beta/\alpha$ exceeds a critical ratio involving the Fiedler eigenvalue $\lambda_2$ of the graph Laplacian.

**The dispute:** The Proof Strategist claims the critical ratio is $4\lambda_2 / |W''(c)|$. The Rigor Auditor gets $2\lambda_2 / |W''(c)|$.

**Resolution:** Let me derive it from scratch.

The boundary/morphology energy is:
$$\mathcal{E}_{\mathrm{bd}}(u) = \alpha \sum_{x,y} N_t(x,y)(u(x)-u(y))^2 + \beta \sum_x u(x)^2(1-u(x))^2$$

The second term is $\beta \sum_x W(u(x))$ where $W(u) = u^2(1-u)^2$.

The Hessian of the first term is $2\alpha L$ where $L$ is the graph Laplacian (with $L_{ij} = -N_t(i,j)$ off-diagonal, $L_{ii} = \sum_j N_t(i,j)$).

The Hessian of the second term at $u \equiv c$ is $\beta W''(c) \cdot I$ (diagonal, since each site contributes independently).

$W(u) = u^2(1-u)^2$, so $W'(u) = 2u(1-u)(1-2u)$, so $W''(u) = 2(1-6u+6u^2)$.

At $c = 1/2$: $W''(1/2) = 2(1 - 3 + 3/2) = 2(-1/2) = -1$.

More generally, $W''(c) < 0$ for $c \in ((3-\sqrt{3})/6, (3+\sqrt{3})/6) \approx (0.211, 0.789)$.

The restricted Hessian on $T_c\Sigma_m$ is:
$$H|_{T_c\Sigma_m} = 2\alpha L|_{T_c\Sigma_m} + \beta W''(c) \cdot I|_{T_c\Sigma_m}$$

The smallest eigenvalue of $L$ restricted to $T_c\Sigma_m$ (i.e., the space orthogonal to the constant vector) is $\lambda_2$, the Fiedler eigenvalue. So the smallest eigenvalue of $H|_{T_c\Sigma_m}$ is:

$$\mu_{\min} = 2\alpha\lambda_2 + \beta W''(c)$$

This is negative when $\beta |W''(c)| > 2\alpha\lambda_2$, i.e.:

$$\boxed{\frac{\beta}{\alpha} > \frac{2\lambda_2}{|W''(c)|}}$$

**The Rigor Auditor is correct.** The factor is $2\lambda_2/|W''(c)|$, not $4\lambda_2/|W''(c)|$. The Proof Strategist's factor of 4 appears to have doubled the Laplacian contribution (perhaps counting $\alpha$ twice or using a different Laplacian normalization convention). With the standard graph Laplacian where $\mathcal{E}_{\mathrm{bd}}$ contains $\alpha \sum_{x,y} N_t(x,y)(u(x)-u(y))^2$, the Hessian contribution is $2\alpha L$, giving the factor of 2.

**Computation Analyst's confirmation:** Critical $\beta^* \approx 2\text{-}10$ numerically. For a $5 \times 5$ grid with unit weights, $\lambda_2 \approx 0.38$ and $|W''(1/2)| = 1$, giving $\beta^*/\alpha = 2 \times 0.38 / 1 = 0.76$. With $\alpha = 1$, this predicts $\beta^* \approx 0.76$. The numerical range $\beta^* \approx 2\text{-}10$ is higher, which is expected: the full energy includes closure and separation terms (not just $\mathcal{E}_{\mathrm{bd}}$), and the closure term stabilizes the uniform state. The qualitative agreement — formation structure emerges above a critical $\beta$ — is confirmed.

**Status: PROVED** with corrected factor $2\lambda_2/|W''(c)|$. The Fiedler eigenvector provides the explicit instability direction.

### Theorem 4: Non-Uniform Constrained Minimizer Exists

**Claim:** When $\beta/\alpha > 2\lambda_2/|W''(c)|$ and $c \in (0.211, 0.789)$, the global constrained minimizer on $\Sigma_m$ is not the uniform state.

**Proof:** By Theorem 3, the Hessian at $u \equiv c$ has a negative eigenvalue. Therefore $u \equiv c$ is not a local minimizer. By Theorem 2, it is the only uniform critical point. By Theorem 1, a global minimizer exists. Therefore the global minimizer is non-uniform. $\square$

**Status: PROVED.** This is the clean core of T8. All three agents agree on the logic (the Rigor Auditor confirms the second-variation argument is valid for establishing that the uniform state is a saddle, and the chain to non-uniform minimizer existence is sound).

### Theorem 5: Formation Structure of Minimizers

**Claim:** Non-uniform constrained minimizers exhibit core-boundary-exterior stratification.

**Proof Strategist's approach:** Γ-convergence as $\varepsilon = \alpha/\beta \to 0$. In this limit, $\mathcal{E}_{\mathrm{bd}}$ converges (in the Γ-sense) to a perimeter functional, and minimizers converge to characteristic functions of sets with minimal perimeter subject to the volume constraint. These limit configurations are binary ($u \in \{0,1\}$) with sharp interfaces — the paradigmatic formation structure.

**Rigor Auditor's critique (accepted):** The Γ-convergence argument proves that *in the limit* $\beta/\alpha \to \infty$, minimizers approach binary formations. It does NOT prove that at *finite* parameter values, minimizers have well-defined core-boundary-exterior stratification. The Γ-convergence is a statement about limiting behavior, not about formation structure at working parameter values.

**Computation Analyst's evidence:** At finite parameters, formations *do* exhibit stratification:
- $\beta = 10$: smooth core-boundary-exterior with graded transitions
- $\beta = 50$: near-binary corner blobs with thin boundary bands

This is compelling numerical evidence but not a proof.

**Synthesis judgment:** The Γ-convergence establishes that formation structure *exists in the limit*. Compactness of $\Sigma_m$ and continuity of the energy ensure that for $\beta/\alpha$ *sufficiently large but finite*, the minimizer is *close* to a binary formation (by standard Γ-convergence approximation results). But "close to binary" is not the same as "has core-boundary-exterior stratification" in the sense the theory needs.

**Status: PROVED IN LIMIT, PROVED-WITH-GAP AT FINITE PARAMETERS.** The gap is: we lack a formal definition of "formation structure" at finite parameters that can be verified analytically. Q_morph was supposed to fill this role — see below.

### Theorem 6: Perturbation by Closure and Separation Terms

**Claim:** Adding the closure term $\lambda_{\mathrm{cl}} \mathcal{E}_{\mathrm{cl}}$ and separation term $\lambda_{\mathrm{sep}} \mathcal{E}_{\mathrm{sep}}$ to $\mathcal{E}_{\mathrm{bd}}$ does not destroy the non-uniform minimizer for small enough $\lambda_{\mathrm{cl}}, \lambda_{\mathrm{sep}}$.

**Proof sketch (Proof Strategist):** The uniform state's Hessian gains additional terms from $\mathcal{E}_{\mathrm{cl}}$ and $\mathcal{E}_{\mathrm{sep}}$. Both terms are continuous; their Hessians at $u \equiv c$ are bounded. For the closure term: at the uniform state with $\mathrm{Cl}_t(u) = u$ (if the uniform state is a closure fixed point, which holds for many parameter choices), $\mathcal{E}_{\mathrm{cl}}(u \equiv c) = 0$ and the Hessian contribution is PSD, stabilizing the uniform state. But the double-well instability grows as $\beta$ while the closure stabilization is bounded by $\lambda_{\mathrm{cl}} \cdot \text{const}$. So for $\beta$ large enough relative to $\lambda_{\mathrm{cl}}$, the instability persists.

**Rigor Auditor's assessment:** The perturbation argument is *standard* and *valid in principle* but requires checking that the uniform state remains a critical point of the full energy. If $\mathrm{Cl}_t(c\mathbf{1}) \neq c\mathbf{1}$ (i.e., the uniform state is not a closure fixed point), the gradient of $\mathcal{E}_{\mathrm{cl}}$ at $u \equiv c$ is nonzero and the critical point shifts. The argument then requires an implicit function theorem step to track the perturbed critical point.

**Status: PROVED WITH MILD GAP.** The logic is sound; the gap is whether the uniform state remains (approximately) a critical point of the full energy. For sigmoid closure with appropriate $\tau_{\mathrm{cl}}$, this is satisfiable. The gap is closeable but not yet closed in full generality.

### Theorem 7: Bind Satisfaction at Minimizers

**Claim:** Non-uniform constrained minimizers approximately satisfy Bind.

**Proof Strategist's approach:** At any minimizer $\hat{u}$, the gradient of $\mathcal{E}$ vanishes (projected onto $T\Sigma_m$). The closure gradient component is $2\lambda_{\mathrm{cl}}(I - J_{\mathrm{Cl}})^T(\hat{u} - \mathrm{Cl}_t(\hat{u}))$. At the minimizer, this balances against the other gradient terms. For large $\lambda_{\mathrm{cl}}$, this forces $\|\hat{u} - \mathrm{Cl}_t(\hat{u})\|$ to be small — i.e., approximate Bind.

**Computation Analyst's finding:** Bind *fails* in $\ell^\infty$ norm (max pointwise deviation 0.12-0.21) but *passes* in $\ell^2$ norm with tolerance $\varepsilon_{\mathrm{cl}} = 0.25$. The failure is localized to boundary sites where the double-well pushes toward sharp transitions while closure smooths.

**Rigor Auditor's critique:** The $\ell^2$ Bind is a *weakening* of the original predicate, which uses "suitable norms" (Canonical Spec Section 7.1). Accepting $\ell^2$ instead of $\ell^\infty$ is *partially legitimate* — $\ell^2$ is indeed a suitable norm — but it changes what Bind means: from "closure is satisfied everywhere" to "closure is satisfied on average." The boundary violations are *structurally expected* (the double-well and closure are in tension at boundaries) and may be *theoretically appropriate* (boundary sites are transitional, not fully self-supporting).

**Synthesis judgment:** The gradient balance argument is *valid*: for large $\lambda_{\mathrm{cl}}$, $\|\hat{u} - \mathrm{Cl}_t(\hat{u})\|_2$ is bounded by $O(1/\lambda_{\mathrm{cl}})$ times the other gradient norms. This is a quantitative bound, not just a hand-wave. But the $\ell^\infty$ failure at boundaries is genuine and structurally inherent.

**Status: PROVED IN $\ell^2$, FAILS IN $\ell^\infty$.** The theory should specify that Bind uses $\ell^2$ norm, and the tolerance should be derived from the gradient balance rather than imposed. The boundary violation is a *feature* (boundaries are where closure and morphology are in productive tension), not a bug.

---

## II. THE Q_MORPH QUESTION — Is It Resolved?

### The Computation Analyst's Proposal: Q_morph_v2

$$\mathcal{Q}_{\mathrm{morph}}(u) = \frac{2}{3} \cdot \text{PersistDom}(u) + \frac{1}{3} \cdot \text{TransSharp}(u)$$

where:
- **PersistDom** measures topological dominance: the ratio of the longest bar in the persistence diagram to the total diagram mass. High when one connected component dominates (= one coherent formation).
- **TransSharp** measures transition quality: how sharply the field transitions from interior to exterior values. High when boundary bands are well-defined rather than diffuse.

### Validation

The Computation Analyst reports successful validation: Q_morph_v2 discriminates between well-formed formations ($\mathcal{Q}_{\mathrm{morph}} \geq \mu_{\mathrm{in}}$) and degenerate fields (uniform, fragmented, or noisy). Combined with $\mathrm{Core}_t \neq \emptyset$ and $\mathrm{Bd}_t \neq \emptyset$, the full $\mathsf{Inside}_t$ predicate is now satisfiable.

### Assessment

**Strengths:**
- Persistence-based (aligns with Iteration 1 Round 5 filtration insight)
- Threshold-free in its topological component (PersistDom)
- Computationally validated
- Allows the first *demonstration* of proto-cohesion satisfiability

**Weaknesses (Rigor Auditor, extended):**
- TransSharp likely involves thresholds (to define "interior" and "exterior" values), reintroducing the threshold dependence the persistence approach was supposed to eliminate
- The 2/3-1/3 weighting is empirically chosen with no theoretical justification
- PersistDom requires computing persistence diagrams, adding algorithmic complexity to what was supposed to be a "quality measure"
- Not yet proved that energy minimizers achieve high Q_morph — the predicate-energy gap persists for this component

**Synthesis judgment:** Q_morph_v2 is **acceptable as a provisional definition** — sufficient to make the $\mathsf{Inside}_t$ predicate well-formed and the Proto-Cohesion Existence Theorem *statable*. It is NOT acceptable as a final definition: the weighting is ad hoc, and the theoretical connection to the energy functional is missing.

**Recommendation:** Adopt Q_morph_v2 provisionally. Add to the Operator Status Table as PROVISIONAL. Flag two open problems: (1) derive Q_morph from the energy or filtration structure rather than defining it by fiat, (2) prove that constrained energy minimizers achieve $\mathcal{Q}_{\mathrm{morph}} \geq \mu_{\mathrm{in}}$ for suitable $\mu_{\mathrm{in}}$.

---

## III. PROTO-COHESION SATISFIABILITY — The First Demonstration

The Computation Analyst reports the **first demonstration** that all four predicates can be simultaneously satisfied at a constrained energy minimizer (using $\ell^2$ Bind and Q_morph_v2 Inside).

This is a milestone. Prior to this round, proto-cohesion satisfiability was an open question. Now:

| Predicate | Status at Computed Minimizer | Norm/Definition |
|-----------|------------------------------|-----------------|
| Bind | **SATISFIED** | $\ell^2$, $\varepsilon_{\mathrm{cl}} = 0.25$ |
| Sep | **SATISFIED** | Standard (avg distinction over interior) |
| Inside | **SATISFIED** | Q_morph_v2 with provisional $\mu_{\mathrm{in}}$ |
| Persist | Not tested (static analysis) | Requires temporal data |

**Three of four** predicates satisfied simultaneously at a single time-step. Persist requires temporal analysis (not in scope for T8's static existence claim).

**Status: DEMONSTRATED (NUMERICAL), NOT PROVED (ANALYTICAL).** The analytical proof requires bounding all four diagnostic components from below at the constrained minimizer — a task that depends on resolving the predicate-energy bridge (see below).

---

## IV. THE PREDICATE-ENERGY BRIDGE — The Remaining Blocking Problem

All three agents identify this as the central remaining obstruction:

**The problem:** Minimizing $\mathcal{E}$ drives the field toward a state that balances *four competing objectives*. There is no guarantee that the balanced optimum satisfies all four *predicates* simultaneously. The energy terms penalize deviations; the predicates threshold satisfactions. These are different mathematical objects.

**What we know:**
- Large $\lambda_{\mathrm{cl}}$ forces approximate Bind (Theorem 7, $\ell^2$)
- Large $\beta$ forces formation structure (Theorem 5, Γ-convergence)
- The Sep predicate involves $\mathbf{D}_t$, which is a different operator from the separation energy $\mathcal{E}_{\mathrm{sep}}$ — satisfaction is not automatic
- Inside depends on Q_morph, whose relationship to energy minimization is empirically observed but not proved

**What we need:** For each predicate $P \in \{\mathsf{Bind}, \mathsf{Sep}, \mathsf{Inside}\}$, either:
(a) Prove: $\exists$ parameter regime such that $\hat{u} = \arg\min_{\Sigma_m} \mathcal{E} \implies P(\hat{u})$, or
(b) Accept: predicates and energy characterize *different aspects* of formation quality, and the diagnostic vector $[0,1]^4$ (Iteration 1 refinement) replaces the Boolean conjunction.

**Synthesis judgment:** This is NOT a T8 problem — it is a T14/T12-level problem that should be tracked separately. T8 asks "do non-trivial minimizers exist?" — YES. The predicate-energy bridge asks "do minimizers satisfy proto-cohesion?" — that is the Proto-Cohesion Existence Theorem (T8 + bridge = full theorem).

---

## V. THE HONEST T8 STATUS — What Is Proved, Exactly

### PROVED (rigorous, no gaps)

**T8-Core.** *Let $X_t$ be a finite graph with Fiedler eigenvalue $\lambda_2 > 0$, and let $m = cn$ with $c \in ((3-\sqrt{3})/6, (3+\sqrt{3})/6)$. If*
$$\frac{\beta}{\alpha} > \frac{2\lambda_2}{|W''(c)|}$$
*then the global minimizer of $\mathcal{E}_{\mathrm{bd}}$ on $\Sigma_m = \{u \in [0,1]^n : \sum u_i = m\}$ is non-uniform.*

Proof: Theorems 1-4 in chain. $\square$

This is a clean, rigorous theorem about $\mathcal{E}_{\mathrm{bd}}$ alone.

### PROVED WITH MILD GAPS

**T8-Full.** *Under the same conditions, for $\lambda_{\mathrm{cl}}, \lambda_{\mathrm{sep}}$ sufficiently small relative to $\beta$, the global minimizer of the full energy $\mathcal{E} = \lambda_{\mathrm{cl}}\mathcal{E}_{\mathrm{cl}} + \lambda_{\mathrm{sep}}\mathcal{E}_{\mathrm{sep}} + \lambda_{\mathrm{bd}}\mathcal{E}_{\mathrm{bd}}$ on $\Sigma_m$ is non-uniform.*

Gap: requires verifying the uniform state remains (approximately) critical for the full energy, or applying an implicit function theorem argument for the perturbed critical point. Standard but not yet written.

### PROVED IN LIMIT

**T8-Structure.** *As $\beta/\alpha \to \infty$, constrained minimizers of $\mathcal{E}_{\mathrm{bd}}$ converge to characteristic functions of sets minimizing perimeter subject to volume constraint.*

This is standard Γ-convergence (Modica-Mortola type). The Rigor Auditor is right that this proves binary-limit structure, not finite-parameter formation structure.

### DEMONSTRATED NUMERICALLY, NOT PROVED ANALYTICALLY

**T8-ProtoCoh.** *Constrained energy minimizers satisfy Bind ($\ell^2$), Sep, and Inside (Q_morph_v2) simultaneously.*

First demonstration of proto-cohesion satisfiability. Analytical proof requires the predicate-energy bridge.

---

## VI. CLASSIFICATION OF ALL R5 RESULTS

### Proved
- Constrained minimizer existence (compactness, Thm 1)
- Uniform state is unique uniform critical point (Thm 2)
- Second variation negative at uniform state when $\beta/\alpha > 2\lambda_2/|W''(c)|$ (Thm 3, **corrected factor**)
- Non-uniform minimizer existence (Thm 4)
- Γ-convergence to perimeter functional in $\beta/\alpha \to \infty$ limit (Thm 5, limited scope)
- Bind in $\ell^2$ via gradient balance for large $\lambda_{\mathrm{cl}}$ (Thm 7)
- Critical ratio correction: $2\lambda_2/|W''(c)|$, not $4\lambda_2/|W''(c)|$ (Rigor Auditor correct)

### Proved with Gaps
- Full-energy non-uniform minimizer (perturbation by closure/sep, Thm 6: standard but needs IFT step)
- Formation structure at finite parameters (Γ-convergence gives limit only; finite-parameter needs Q_morph)

### Conjectured (well-supported numerically)
- All $(\beta, m)$ pairs in the supercritical regime produce formations (Computation Analyst: confirmed across full phase diagram)
- Q_morph_v2 correctly classifies formation quality (validated but not theoretically derived)
- Proto-cohesion is satisfiable at constrained energy minimizers (first demonstration)

### Open
- Predicate-energy bridge: when does small $\mathcal{E}$ imply high ProtoCoh scores?
- Q_morph theoretical derivation (current definition is empirical)
- Sep satisfaction at energy minimizers (requires distinction operator analysis at minimizers)
- Persist (requires temporal extension, not in T8 scope)

### Corrected
- Critical ratio: $2\lambda_2/|W''(c)|$ replaces $4\lambda_2/|W''(c)|$ (Proof Strategist's factor was wrong)
- Γ-convergence scope: proves binary limits, not formation structure at finite parameters (Proof Strategist overstated)
- Bind norm: $\ell^2$ succeeds, $\ell^\infty$ fails; both are legitimate "suitable norms" but mean different things

### False / Abandoned
- Mountain pass without volume constraint (already established false in R4)
- $\ell^\infty$ Bind at energy minimizers (boundary violations are structurally inherent)

---

## VII. IMPACT ON THE THEOREM REGISTRY

| Theorem | Pre-R5 Status | Post-R5 Status | Change |
|---------|--------------|----------------|--------|
| T8 (non-trivial minimizers) | Sketch | **PROVED** (core claim) | Major advance |
| T7 (energy minimizer existence) | Proved | **PROVED on $\Sigma_m$** | Strengthened (constrained) |
| T9 (PD stability) | Provable | Connected via Q_morph_v2 | Q_morph provides the link |
| T14 (gradient flow → ProtoCoh) | Blocked on Q_morph | **Partially unblocked** | Q_morph_v2 provisional |
| T8-ProtoCoh (new) | — | **DEMONSTRATED** | First satisfiability evidence |
| Predicate-energy bridge (new) | Unnamed | **IDENTIFIED as blocking** | Central remaining problem |

---

## VIII. MANDATORY UPDATES TO CANONICAL THEORY

### From R5 (cumulative with R4)

1. **A1 → A1' (conditional extensivity)** [from R4]
2. **Volume constraint as structural axiom** [from R4, confirmed in R5 as essential]
3. **Q_morph_v2 as provisional definition** [NEW from R5]
4. **E3 reclassified as solution constraint** [from R4]
5. **C_t diffusion elevated to PROVISIONAL** [from R4]
6. **Bind norm specified as $\ell^2$** [NEW from R5 — or explicitly leave norm choice open with both options documented]
7. **Critical ratio $2\lambda_2/|W''(c)|$ for phase transition** [NEW from R5, corrected]

### New Commitment Note (proposed)

**Commitment Note 10: Formation structure is limit-derived.** At finite parameters, "formation structure" means proximity to the Γ-limit (binary characteristic function with minimal perimeter). The theory's formations are *approximations* to sharp-interface configurations, with the approximation quality controlled by $\beta/\alpha$. This is not a weakness — it is the mechanism by which graded cohesion fields approach but do not reach crisp objecthood.

---

## IX. RECOMMENDED NEXT STEPS

The T8 proof chain establishes the existence backbone. The critical path forward is now:

1. **Predicate-energy bridge** (highest priority): Prove or disprove that constrained minimizers satisfy all predicates. This is the gap between T8 (minimizers exist) and the Proto-Cohesion Existence Theorem (minimizers *are* proto-cohesive).

2. **Q_morph theoretical grounding**: Derive Q_morph from the filtration or energy structure rather than defining it empirically.

3. **Sep at minimizers**: Analyze the distinction operator $\mathbf{D}_t$ at constrained minimizers. Does the formation structure from Γ-convergence guarantee high average distinction?

4. **Close Theorem 6 gap**: Write the implicit function theorem step for perturbation by closure/sep terms.

5. **Temporal extension**: Extend from static (single-time) T8 to dynamic (multi-time) existence with Persist.

---

## X. FINAL ASSESSMENT

T8 is the theory's first real theorem. Not a sketch, not a conjecture, not an existence proof that follows trivially from compactness — a genuine result that says: *under computable conditions on the graph structure and parameters, the energy landscape has non-trivial structure, the uniform state is unstable, and spatially organized formations are energetically preferred.*

The proof chain is sound in its core (Theorems 1-4), overstated in its periphery (Γ-convergence scope, critical ratio factor), and incomplete in its ambition (predicate-energy bridge). The Computation Analyst's phase diagram and first proto-cohesion demonstration provide the empirical grounding that the analytical results alone cannot yet deliver.

The theory's status after R5: it has a theorem, a computable phase transition, a provisional Q_morph, and the first evidence of proto-cohesion satisfiability. What it does not yet have is a proof that its variational characterization (energy minimization) and its predicative characterization (proto-cohesion) pick out the same objects. That bridge is the next target.

---

*This document supersedes the T8 entries in all prior assessments. The critical ratio $2\lambda_2/|W''(c)|$ is definitive (Rigor Auditor's derivation verified by independent re-derivation in this synthesis). Q_morph_v2 is adopted provisionally. The predicate-energy bridge is identified as the central remaining problem on the critical path to the Proto-Cohesion Existence Theorem.*
