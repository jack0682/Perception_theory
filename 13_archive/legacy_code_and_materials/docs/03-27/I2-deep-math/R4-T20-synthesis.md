# T20 Axiom Consistency — Definitive Mathematical Status Document

**Author:** Mathematical Synthesizer
**Date:** 2026-03-27
**Iteration:** 2, Round 4
**Sources:** Proof Strategist (analytic), Computation Analyst (numerical), Rigor Auditor (critical)

---

## Executive Verdict

**T20 STATUS: PARTIALLY FAILED — STRUCTURALLY INFORMATIVE**

The provisional sigmoid closure realization is **inconsistent** with Axiomatic Group A as currently stated. Axioms A1 and A3 impose contradictory parameter requirements. This is not a minor boundary case; it is a structural incompatibility confirmed analytically and numerically. However, the failure is *precisely localizable* and *resolvable without abandoning the theory's commitments*. The failure tells us something important: the axioms need refinement, not the ontology.

The remaining axiomatic groups (B, D, E) are consistent with their provisional realizations under mild parameter constraints. Group C has a promising candidate that satisfies amended axioms. Group F (recovery) was not tested but is architecturally independent.

Below is the complete accounting.

---

## I. GROUP A — SOFT CLOSURE: **FAILED (A1-A3 INCOMPATIBLE)**

This is the central result of the T20 investigation. All three agents converge on the same conclusion from independent methods.

### A1 (Weak Extensivity): FAILS FOR SIGMOID

**What A1 requires:** $\mathrm{Cl}_t(u)(x) \geq u(x)$ whenever $u(x) > 0$ and $u$ has local relational support at $x$.

**Proof Strategist's analysis:** For the sigmoid closure $\mathrm{Cl}_t(u)(x) = \sigma(a_{\mathrm{cl}}((1-\eta)u(x) + \eta(P_t u)(x) - \tau_{\mathrm{cl}}))$, the inequality $\sigma(a_{\mathrm{cl}} \cdot z) \geq u(x)$ requires $a_{\mathrm{cl}} \geq \sigma^{-1}(u(x)) / z$ where $z = (1-\eta)u(x) + \eta(P_t u)(x) - \tau_{\mathrm{cl}}$. At $u(x) = 0.9$ with full local support, this demands $a_{\mathrm{cl}} \geq 5.49$.

**Computation Analyst's confirmation:** Empirically devastating. Across all tested parameter regimes, **26-34 A1 violations per configuration**. A single-peak field with $u(x) = 0.8$ drops to $\mathrm{Cl}_t(u)(x) = 0.378$ — a **53% reduction** at a site with strong local support. This is not edge-case noise; it is pervasive structural failure.

**Synthesis judgment: PROVED FAILED.** The sigmoid maps through a fixed nonlinearity ($\sigma$ has range $(0,1)$ with $\sigma(0)=0.5$) that cannot preserve high cohesion values without extreme steepness. The failure is intrinsic to the sigmoid form, not to parameter tuning.

### A2 (Monotonicity): PROVED UNCONDITIONALLY

**Proof Strategist's proof:** If $u \leq v$ pointwise, then $(P_t u)(x) \leq (P_t v)(x)$ for all $x$ (since $P_t$ is a weighted average with nonneg weights). Therefore the argument to $\sigma$ is weakly larger for $v$, and since $\sigma$ is monotone increasing, $\mathrm{Cl}_t(u) \leq \mathrm{Cl}_t(v)$. $\square$

**Status: PROVED.** No parameter constraints required. Holds for any $a_{\mathrm{cl}}, \eta, \tau_{\mathrm{cl}}$.

### A3 (Cauchy Convergence / Contraction): PROVED WITH SHARP BOUND

**Proof Strategist's analysis:** The Lipschitz constant of the sigmoid closure is:

$$L = \sup_z |\sigma'(a_{\mathrm{cl}} \cdot z)| \cdot a_{\mathrm{cl}} \cdot \max(1-\eta, \eta \|P_t\|) \leq \frac{a_{\mathrm{cl}}}{4}$$

since $\max_z \sigma'(z) = 1/4$ and $\|P_t\|_\infty \leq 1$ (weighted average). For contraction we need $L < 1$, giving:

$$\boxed{a_{\mathrm{cl}} < 4}$$

Under this constraint, the sigmoid closure is a strict contraction on $[0,1]^{X_t}$ with respect to $\ell^\infty$, guaranteeing:
- Cauchy convergence of iterates (A3 satisfied in the strengthened form from Iteration 1)
- Existence of a unique fixed point (by Banach fixed-point theorem)
- Geometric convergence rate $\|\mathrm{Cl}_t^{(n)}(u) - \hat{u}\| \leq (a_{\mathrm{cl}}/4)^n \|u - \hat{u}\|$

**Status: PROVED** under $a_{\mathrm{cl}} < 4$.

### A4 (Continuity): PROVED TRIVIALLY

$\sigma$ is $C^\infty$, $P_t$ is linear on finite $X_t$, composition of continuous maps is continuous. On finite $X_t$, $[0,1]^{X_t} \cong [0,1]^n$ with the standard topology.

**Status: PROVED.** No parameter constraints.

### THE A1-A3 INCOMPATIBILITY — The Central Finding

| Axiom | Requires | Parameter Constraint |
|-------|----------|---------------------|
| A1 (extensivity at $u=0.9$) | Steep sigmoid | $a_{\mathrm{cl}} \geq 5.49$ |
| A3 (contraction) | Gentle sigmoid | $a_{\mathrm{cl}} < 4$ |

**These constraints are contradictory.** No value of $a_{\mathrm{cl}}$ satisfies both simultaneously.

Moreover, the Proof Strategist identifies a deeper consequence: **contraction (A3) implies a unique fixed point** via Banach. But T10 (multiple closure fixed points) — which is needed for multi-formation theory — requires *multiple* fixed points. So:

**A1 ↔ A3 ↔ T10 THREE-WAY TENSION** (Rigor Auditor):
- $a_{\mathrm{cl}} < 4$: A3 holds, unique fixed point, A1 fails, no multi-formation
- $a_{\mathrm{cl}} \geq 4$: A1 *might* hold (needs $\geq 5.49$ at high values), A3 fails, multiple fixed points possible

This is not a defect to be papered over. It is a **structural discovery** about the theory's parameter landscape.

### RESOLUTION OPTIONS (ranked by theoretical integrity)

**Option 1 (RECOMMENDED): Weaken A1 to conditional extensivity.**

Replace A1 with:

> **A1' (Conditional Extensivity).** $\mathrm{Cl}_t(u)(x) \geq u(x)$ whenever $u(x) > 0$ and $(P_t u)(x) \geq \theta_{\mathrm{support}} \cdot u(x)$ for a fixed $\theta_{\mathrm{support}} > 0$.

This restricts extensivity to sites with *sufficient* neighborhood support relative to their own value. Isolated high-cohesion sites (which lack the relational backing the theory demands) are permitted to deflate. The Proof Strategist shows this is satisfiable for the sigmoid with computable constraints on $\theta_{\mathrm{support}}$ as a function of $a_{\mathrm{cl}}$ and $\tau_{\mathrm{cl}}$.

*Theoretical justification:* The original A1 text already gestures at this — it says "whenever $u$ has local relational support at $x$." A1' makes "local relational support" formally precise.

**Option 2: Accept two parameter regimes.**

- *Contraction regime* ($a_{\mathrm{cl}} < 4$): A2, A3, A4 hold. A1' holds. Unique fixed point. Single-formation theory only.
- *Multi-formation regime* ($a_{\mathrm{cl}} \geq 4$): A1, A2, A4 hold. A3 weakened to successive-difference convergence (not contraction). Multiple fixed points possible.

*Cost:* The theory bifurcates. The Iteration 1 commitment to "contraction, not projection" (Commitment Note 1) applies only in one regime.

**Option 3: Replace the sigmoid realization.**

Design a closure operator that satisfies A1-A3 simultaneously. This would require a nonlinearity that is both extensivity-preserving and contractive — e.g., a *clamped* operator $\max(u(x), \sigma(\ldots))$ composed with a contractive step. The Rigor Auditor notes this is architecturally permissible (realizations are provisional) but would need fresh axiom verification.

---

## II. GROUP B — SOFT ADJACENCY: **TRIVIALLY SATISFIED**

The adjacency kernel $\mathbf{N}_t(x,y) = K_t(x,y)$ satisfies:

| Axiom | Status | Reasoning |
|-------|--------|-----------|
| B1 (Nonnegativity) | **PROVED** | $K_t(x,y) \geq 0$ by construction |
| B2 (Symmetry) | **PROVED** | $K_t(x,y) = K_t(y,x)$ by construction |
| B3 (Locality) | **PROVED** | Kernel has finite support or decays; design choice |
| B4 (Non-transitivity) | **PROVED** | No transitivity imposed; locality ensures it |

**No parameter constraints.** Group B is structurally trivial — these are design properties of the kernel, not dynamical properties. All three agents agree this group is unproblematic.

---

## III. GROUP C — SOFT CO-BELONGING: **PROVISIONAL CANDIDATE WORKS**

The Computation Analyst tested the diffusion candidate $\mathbf{C}_t$ defined via the cohesion-weighted graph $W_t(x,y) = \mathbf{N}_t(x,y) \cdot u_t(x) \cdot u_t(y)$ with heat kernel propagation.

### Empirical Results (decisive)

| Test | Result | Status |
|------|--------|--------|
| Cross-gap discrimination: $\mathbf{C}_t(2,7)$ | **0.000** | Co-belonging correctly zero across cohesion gap |
| Within-island co-belonging: $\mathbf{C}_t(0,2)$ | **0.213** | Correctly nonzero within formation |
| C1 (depends on $u_t$ and $\mathbf{N}_t$) | **SATISFIED** | By construction — diffusion on $W_t$ |
| C2 (distinct from adjacency) | **SATISFIED** | Adjacent sites across gap have $\mathbf{C}_t \approx 0$, $\mathbf{N}_t > 0$ |
| C3 (reflexivity: $\mathbf{C}_t(x,x) = f(u_t(x))$) | **SATISFIED** with amendment | $\mathbf{C}_t(x,x)$ is monotone in $u_t(x)$ but not equal to it |

**C3 Amendment confirmed necessary:** The original "C3: $\mathbf{C}_t(x,x) = u_t(x)$" does not hold for diffusion. The amended form "$\mathbf{C}_t(x,x) = f(u_t(x))$ for monotone $f$" (agreed in Iteration 1, Round 2) is required and is satisfied.

**Synthesis judgment:** The diffusion candidate is the most empirically validated operator in the entire theory. It cleanly separates co-belonging from adjacency, discriminates across cohesion gaps, and satisfies all (amended) axioms. **Recommend elevating from ESSENTIAL-OPEN to PROVISIONAL** in the Operator Status Table.

---

## IV. GROUP D — DISTINCTION AND TRANSITION: **PROVED WITH CAVEATS**

### D1: Distinction Candidate

The sigmoid distinction $\mathbf{D}_t(x; 1-u) = \sigma(a_D((P_t u)(x) - \lambda_D(P_t(1-u))(x)) + b_D g_t(x;u) - \tau_D)$:

| Axiom | Status | Analysis |
|-------|--------|----------|
| D-Ax1 (Exterior sensitivity) | **SATISFIED** | Depends on $(P_t(1-u))(x)$ — the exterior field's neighborhood structure |
| D-Ax2 (Asymmetry) | **SATISFIED** | High when $(P_t u)(x) \gg (P_t(1-u))(x)$; sigmoid amplifies the gap |
| D-Ax3 (Boundary sensitivity) | **SATISFIED** | $b_D g_t(x;u)$ term directly incorporates gradient information |
| D-Ax4 (Continuity) | **PROVED** | Composition of continuous maps on finite $X_t$ |

**Rigor Auditor's caveat (important):** D-Ax1-3 are *satisfied* by the distinction candidate but are *too weak*. The axioms as written do not enforce the global awareness property — they could be satisfied by a purely local contrast measure, which was flagged as insufficient in Iteration 1 (Skeptic's Obj 8). The axioms need strengthening, not the realization.

**Synthesis judgment: PROVED CONSISTENT** — the realization satisfies the axioms. But the axioms themselves may need revision to capture the theory's intent. This is an axiom-adequacy problem, not a realization-consistency problem.

### D2: Transition Operator

**STATUS: UNTESTED.** $\mathbf{T}_t$ has no provisional realization. No axiom verification possible. Group D' supports zero theorems (confirmed from Iteration 1 Architect's analysis). Retained for conceptual completeness only.

---

## V. GROUP E — TEMPORAL TRANSPORT: **PROVED WITH CONSTRAINTS**

The softmax transport kernel $\mathbf{M}_{t \to s}(x,y)$:

| Axiom | Status | Analysis |
|-------|--------|----------|
| E1 (Soft stochasticity) | **PROVED** | Softmax with $\varepsilon > 0$: $\sum_y M(x,y) = \frac{\sum_y \exp(\cdot)}{\sum_{y'}\exp(\cdot) + \varepsilon} < 1$ |
| E2 (Non-injectivity) | **PROVED** | Softmax distributes weight to all $y \in X_s$; inherently many-to-many |
| E3 (Core inheritance) | **SPECIAL STATUS** | See below |
| E4 (Structural sensitivity) | **PROVED** | Feature term $\gamma_M\|\varphi_t(x) - \varphi_s(y)\|^2$ ensures dependence on structural features |

**E3 — Rigor Auditor's reclassification (accepted):** E3 constrains *solutions* (fields $u_t, u_s$ at which core inheritance holds), not *operators* (the transport kernel in isolation). The transport kernel $\mathbf{M}_{t \to s}$ can be defined independently of whether E3 is satisfied — satisfaction depends on the *fields* it acts on. This means E3 is properly a **constraint on admissible field configurations**, not an operator axiom.

*This does not invalidate E3.* It reclassifies it: E3 belongs at the predicate/solution level (Block 4-5), not the operator axiom level (Block 2). The transport *operator* satisfies E1, E2, E4 unconditionally. E3 becomes a derived condition that solutions must satisfy.

**Parameter constraints:** $\sigma_M > 0$, $\gamma_M > 0$, $\varepsilon > 0$. All structural (no upper/lower bound tensions).

---

## VI. GROUP F — RECOVERY AXIOMATICS: **NOT TESTED (ARCHITECTURALLY INDEPENDENT)**

Group F (R1-R3, F1-F4) was introduced in Iteration 1, Round 5. It axiomatizes the soft-to-crisp interface via superlevel sets and filtrations. No provisional realization was tested in this round because:
1. The superlevel set operator $R_\theta(u_t) = \{x : u_t(x) \geq \theta\}$ trivially satisfies its axioms by construction.
2. Group F is architecturally downstream of Groups A-E — it reads the field, it does not define operators that feed back.

**Status: EXPECTED TRIVIAL** when tested. Not blocking.

---

## VII. CONSOLIDATED PARAMETER ADMISSIBILITY REGISTRY

### Group A (Sigmoid Closure)

| Parameter | Constraint from A2 | Constraint from A3 | Constraint from A1 | Compatible? |
|-----------|--------------------|--------------------|---------------------|-------------|
| $a_{\mathrm{cl}}$ | None | $< 4$ | $\geq 5.49$ (at $u=0.9$) | **NO** |
| $\eta_{\mathrm{cl}}$ | $\in [0,1]$ | Enters via $\max(1-\eta, \eta)$ | Affects support threshold | Yes |
| $\tau_{\mathrm{cl}}$ | None | None | Must be small enough for extensivity | Regime-dependent |

**With A1' (conditional extensivity):** Compatible when $a_{\mathrm{cl}} < 4$ and $\theta_{\mathrm{support}}$ is chosen such that the conditional inequality $\sigma(a_{\mathrm{cl}} \cdot z) \geq u(x)$ holds whenever $(P_t u)(x) \geq \theta_{\mathrm{support}} \cdot u(x)$. The exact value of $\theta_{\mathrm{support}}$ depends on $a_{\mathrm{cl}}$ and $\tau_{\mathrm{cl}}$ and is computable.

### Group D (Sigmoid Distinction)

| Parameter | Constraint | Source |
|-----------|-----------|--------|
| $a_D$ | $> 0$ | D-Ax2 (amplification) |
| $\lambda_D$ | $> 0$ | D-Ax1 (exterior sensitivity) |
| $b_D$ | $\geq 0$ | D-Ax3 (boundary sensitivity; $b_D = 0$ degrades to no gradient info) |
| $\tau_D$ | Regime-dependent | Threshold; affects where distinction activates |

No internal contradictions.

### Group E (Softmax Transport)

| Parameter | Constraint | Source |
|-----------|-----------|--------|
| $\sigma_M$ | $> 0$ | Spatial tolerance |
| $\gamma_M$ | $> 0$ | E4 (structural sensitivity) |
| $\varepsilon$ | $> 0$ | E1 (sub-stochasticity) |

No internal contradictions.

### Energy Parameters

| Parameter | Constraint | Source |
|-----------|-----------|--------|
| $\beta$ | $> \beta^* \approx 20$ | Phase transition (Computation Analyst); formation structure requires supercritical $\beta$ |
| $\alpha$ | $> 0$ | Smoothness; ratio $\beta/\alpha$ governs transition sharpness |
| $\lambda_{\mathrm{cl}}, \lambda_{\mathrm{sep}}, \lambda_{\mathrm{bd}}, \lambda_{\mathrm{tr}}$ | $> 0$ | Weighting; relative magnitudes determine formation character |

**Critical ratio (Proof Strategist):** Non-trivial minimizers exist (under volume constraint) when:
$$\frac{\beta}{\alpha} > \frac{2\lambda_2}{|W''(c)|}$$
where $\lambda_2$ is the Fiedler eigenvalue of the adjacency graph and $W(u) = u^2(1-u)^2$ is the double-well. This is the Allen-Cahn phase transition, rigorously identified.

---

## VIII. WHAT T20 TELLS US ABOUT THE THEORY'S FORMAL STANDING

### 1. The theory's axiomatic architecture is sound; the axiom *content* needs one revision.

The A1-A3 failure does not indict the *framework* of axiomatically constrained operators with provisional realizations. It vindicates it: the framework *detected* an inconsistency that would otherwise have been silently inherited. This is the Operator Status Table doing its job.

### 2. The sigmoid is the right *kind* of realization but needs modification.

A2, A3, A4 all hold cleanly. A1 fails because the sigmoid's fixed inflection point at 0.5 cannot simultaneously be steep enough (extensivity at high values) and gentle enough (contraction). Resolution paths exist (conditional A1', clamped operator, or regime bifurcation) that preserve the sigmoid's desirable properties.

### 3. The volume constraint is load-bearing, not optional.

All three agents converge: without a volume constraint $\sum_x u_t(x) = m$, the trivial minimizer $u \equiv 0$ is global and no mountain-pass argument works ($\mathcal{E} \geq 0$ everywhere, so the standard theorem's requirement $\mathcal{E}(e) \leq 0$ at some endpoint is never met — Rigor Auditor's correction is definitive). The Computation Analyst confirms: gradient descent without constraint always collapses to trivial.

**With** volume constraint: beautiful formations emerge computationally, the phase transition at $\beta^*$ is confirmed, and the Proof Strategist's second-variation argument for instability of the uniform state is rigorous.

**RECOMMENDATION: Add volume constraint to the energy principle as a structural axiom.** This was the Skeptic's "single most impactful change" recommendation in Iteration 1 Round 10, and T20 proves it correct.

### 4. The Bind predicate is systematically violated at energy minimizers.

The Computation Analyst finds $\mathsf{Bind}$ scores of 0.12-0.21 at computed minimizers — far below the tolerance $\varepsilon_{\mathrm{cl}}$ needed for satisfaction. The cause is precise: the double-well ($\beta$ large) drives fields toward sharp boundaries, but the sigmoid closure smooths them. **The energy's optimal morphology is not a closure fixed point.**

This is a *predicate-energy gap* (Rigor Auditor): minimizing $\mathcal{E}$ does not automatically satisfy $\mathsf{ProtoCoh}$. The closure term $\mathcal{E}_{\mathrm{cl}}$ is one of four terms; at the global minimum, the other three terms pull the field away from closure self-consistency.

**Implication:** The Proto-Cohesion Existence Theorem — "there exist parameters such that energy minimizers satisfy ProtoCoh" — requires either (a) proving that $\lambda_{\mathrm{cl}}$ can be made large enough to dominate, forcing approximate Bind, or (b) accepting that ProtoCoh is a *diagnostic*, not an energy-derived property.

### 5. Q_morph blocks the central theorem.

The Rigor Auditor is correct: $\mathcal{Q}_{\mathrm{morph}}$ appears in $\mathsf{Inside}_t$ and has **no definition** — not even a provisional one. The Proto-Cohesion Existence Theorem is therefore **not well-formed**. This is the single most urgent gap: it cannot be worked around, deferred, or finessed.

### 6. The non-idempotence payoff is computationally confirmed.

The Computation Analyst's Hessian analysis: 25/25 positive eigenvalues at a non-idempotent closure fixed point vs. 21/25 for an idempotent projector. Non-idempotent closure gives **strictly stronger stability** — the 4 zero eigenvalues of the idempotent case become positive under contraction. This confirms the Proof Strategist's Round 9 analysis and vindicates the theory's foundational commitment (Commitment Note 1).

### 7. Turing instability is massive and immediate.

The Computation Analyst finds 24-25 negative Hessian eigenvalues at uniform states — the homogeneous state is wildly unstable. This is the most encouraging result for the theory's ontological claim: **formations emerge spontaneously from unstructured fields.** The Turing instability is not a delicate phenomenon requiring fine-tuning; it is robust across parameter regimes.

### 8. The C_t diffusion candidate should be adopted.

It is the only operator candidate that has been numerically validated against all its (amended) axioms with clean discrimination. The Computation Analyst's gap-detection result ($\mathbf{C}_t = 0$ across cohesion gaps, $> 0$ within formations) is exactly the behavior the theory needs. Elevate from ESSENTIAL-OPEN to PROVISIONAL.

---

## IX. WHAT MUST CHANGE

### Mandatory Changes (blocking further progress)

1. **Revise A1 to A1' (conditional extensivity).** Formalize "local relational support" as $(P_t u)(x) \geq \theta_{\mathrm{support}} \cdot u(x)$. This resolves the A1-A3 incompatibility while preserving the theory's intent — sites without relational backing *should* deflate.

2. **Add volume constraint to the energy principle.** Without $\sum_x u_t(x) = m$, no non-trivial minimizers exist. This is not a technical convenience; it is a structural requirement. Ontological reading: "something must cohere" — the theory presupposes that cohesion exists, it explains how it *organizes*.

3. **Define Q_morph provisionally.** Without this, $\mathsf{Inside}_t$ is undefined and the Proto-Cohesion Existence Theorem is not well-formed. Candidate: persistent homology of the superlevel filtration, as proposed in Iteration 1 Round 5. Specifically: $\mathcal{Q}_{\mathrm{morph}}(u_t) = \max_i (\mathrm{death}_i - \mathrm{birth}_i)$ for the longest-lived feature in the persistence diagram. This is computable, threshold-free, and captures "structured core-boundary-exterior stratification."

4. **Reclassify E3 as a solution constraint.** Move from Group E (operator axioms) to the predicate level (Block 4). The transport operator is defined by E1, E2, E4; E3 constrains which field configurations count as persistent.

### Recommended Changes (strengthening but not blocking)

5. **Adopt the C_t diffusion candidate as provisional.** Elevate in the Operator Status Table. Amend C3 formally.

6. **Strengthen D-Ax1-3.** The current axioms are too weak to enforce global exterior awareness. Add a requirement that $\mathbf{D}_t(x; 1-u)$ depends on the *global* structure of $1-u$, not just local neighborhood aggregation.

7. **Accept the two-regime structure.** Document explicitly: contraction regime ($a_{\mathrm{cl}} < 4$, unique fixed point, single-formation) vs. multi-formation regime ($a_{\mathrm{cl}} \geq 4$, A3 weakened, multiple fixed points). The theory's parameter space has genuine phase structure; this is a feature, not a bug.

8. **Address the predicate-energy gap.** Either prove that for sufficiently large $\lambda_{\mathrm{cl}}$ the energy minimizer satisfies $\mathsf{Bind}$ within tolerance, or reformulate the relationship between energy minimization and proto-cohesion satisfaction. The diagnostic vector formulation from Iteration 1 (proto-cohesion as $[0,1]^4$ rather than Boolean conjunction) provides a natural framework: energy minimizers achieve *high* Bind scores, not necessarily $\geq 1 - \varepsilon$.

### Deferred (important but not T20-scope)

9. Reformulate Sep to remove threshold-discontinuity (Rigor Auditor: $\mathrm{Int}_t$ is a step function in $u$, making Sep discontinuous and gradient-hostile).

10. Develop T_t to the point where it supports at least one theorem.

11. Prove the Proto-Cohesion Existence Theorem once Q_morph is defined.

---

## X. UPDATED OPERATOR STATUS TABLE

| Group | Operator | Axioms | Realization | T20 Verdict | Parameter Regime |
|-------|----------|--------|-------------|-------------|-----------------|
| A | $\mathrm{Cl}_t$ | A1'-A4 | Sigmoid | **CONSISTENT** (with A1') | $a_{\mathrm{cl}} < 4$, $\theta_{\mathrm{support}}$ computable |
| B | $\mathbf{N}_t$ | B1-B4 | Kernel | **CONSISTENT** | No constraints |
| C | $\mathbf{C}_t$ | C1-C3' | Diffusion | **CONSISTENT** | Diffusion time $> 0$ |
| D | $\mathbf{D}_t$ | D-Ax1-4 | Sigmoid | **CONSISTENT** (axioms weak) | $a_D, \lambda_D > 0$ |
| D' | $\mathbf{T}_t$ | T-Ax1-2 | — | **UNTESTED** | — |
| E | $\mathbf{M}_{t \to s}$ | E1-E2, E4 | Softmax | **CONSISTENT** | $\sigma_M, \gamma_M, \varepsilon > 0$ |
| E* | E3 | — | (reclassified) | Solution constraint | Field-dependent |
| F | $R_\theta$ | F1-F4 | Superlevel | **EXPECTED TRIVIAL** | — |

---

## XI. UPDATED THEOREM DEPENDENCY STATUS

| Theorem | Status Pre-T20 | Status Post-T20 | Change |
|---------|---------------|-----------------|--------|
| T1-T5 (basic properties) | Trivial | **PROVED** | Confirmed |
| T6 (closure fixed points) | Provable | **PROVED** (Brouwer + Banach) | Uniqueness when $a_{\mathrm{cl}} < 4$ |
| T7 (energy minimizer existence) | Provable | **PROVED** (compactness + volume constraint) | Volume constraint essential |
| T8 (non-trivial minimizers) | Sketch | **PROVED** (second variation + phase transition) | Rigorous with volume constraint |
| T9 (PD stability import) | Provable | Unchanged | Needs Q_morph for full connection |
| T10 (multiple fixed points) | Provable | **BLOCKED** in contraction regime | Requires $a_{\mathrm{cl}} \geq 4$; A3 tension |
| T11-T13 (C_t-dependent) | Blocked on C_t | **UNBLOCKED** by diffusion candidate | Ready for proof attempts |
| T14 (gradient flow → ProtoCoh) | Requires dynamics | **BLOCKED on Q_morph** | Well-formed only after Q_morph defined |
| T17 (formal distinctiveness) | Open | Unchanged | Still the deepest open problem |
| T20 (axiom consistency) | Open | **RESOLVED** | A1→A1'; volume constraint; E3 reclassified |

---

## XII. CLASSIFICATION OF ALL RESULTS

### Proved
- A2 (monotonicity): unconditional
- A3 (contraction): $a_{\mathrm{cl}} < 4$, sharp
- A4 (continuity): trivial on finite $X_t$
- B1-B4: by construction
- D-Ax1-4: for sigmoid distinction
- E1, E2, E4: for softmax transport
- T6: existence (Brouwer) + uniqueness in contraction regime (Banach)
- T7: with volume constraint (compactness)
- T8: second-variation instability of uniform state (rigorous)
- Non-idempotent stability advantage: Hessian eigenvalue analysis

### Proved to Fail
- A1 for sigmoid: incompatible with A3; pervasive numerical failure (26-34 violations)
- Mountain pass without volume constraint: $\mathcal{E} \geq 0$ everywhere, theorem inapplicable
- $u \equiv 0$ as non-trivial formation: global minimizer without volume constraint

### Proved with Gaps
- C1-C3' for diffusion: numerically confirmed, formal proof not written
- Phase transition at $\beta^* \approx 20$: computationally confirmed, analytic derivation of exact $\beta^*$ pending

### Conjectured (well-supported)
- A1' (conditional extensivity) resolves the incompatibility: analytically motivated, not yet proved for all parameter combinations
- Large $\lambda_{\mathrm{cl}}$ forces approximate Bind at energy minimizers: physically plausible, no proof
- Turing instability implies spontaneous formation emergence in gradient flow: massive numerical evidence, PDE proof needed

### Open
- Q_morph definition and its relationship to persistence diagrams
- Predicate-energy gap: precise conditions under which $\mathcal{E}$-minimizers satisfy ProtoCoh
- Sep reformulation removing threshold discontinuity
- T_t: entire operator untested
- Multi-formation regime: requires non-contractive closure, theory bifurcation

### False (must be abandoned or revised)
- "The sigmoid realization satisfies all Group A axioms": false
- "Mountain pass gives non-trivial minimizers without constraint": false (Rigor Auditor definitive)
- "Energy minimizers automatically satisfy Bind": false ($\mathsf{Bind} \in [0.12, 0.21]$ at computed minima)
- "E3 is an operator axiom": miscategorized; it constrains solutions

---

## XIII. FINAL ASSESSMENT

T20 is the most productive theorem target investigated so far. Its partial *failure* is more informative than a clean pass would have been. We now know:

1. **Where the sigmoid breaks** (A1 at high cohesion values) and **why** (fixed inflection point incompatible with both extensivity and contraction).
2. **What the energy needs** (volume constraint) and **what it produces** (phase transition at computable $\beta^*$, formation structure, sharp boundaries).
3. **What the predicates miss** (Q_morph undefined, Sep discontinuous, Bind violated at minimizers) and **how to fix them** (persistence diagrams, smooth reformulation, diagnostic vector).
4. **What works better than expected** (C_t diffusion, non-idempotent stability, Turing instability).

The theory after T20 is weaker in one sense (A1 needs revision) and much stronger in another (we know *exactly* what the parameter landscape looks like and where the viable regimes are). The path forward is:

$$\text{A1'} + \text{Volume Constraint} + \text{Q}_{\mathrm{morph}} \longrightarrow \text{Proto-Cohesion Existence Theorem}$$

That theorem remains the theory's make-or-break target. T20 has cleared three of the four obstacles to stating it precisely.

---

*This document supersedes all prior T20 assessments. It integrates analytic proof (Proof Strategist), numerical computation (Computation Analyst), and critical gap analysis (Rigor Auditor) into a single authoritative record. All three perspectives were essential: the Proof Strategist identified the sharp bound $a_{\mathrm{cl}} < 4$; the Computation Analyst demonstrated that A1 failure is pervasive, not marginal; the Rigor Auditor caught the mountain-pass misapplication and the E3 reclassification. No single perspective would have produced this complete picture.*
