# R1: Emergency Repair Checklist

**Date:** 2026-03-30
**Priority:** MUST FIX BEFORE ANY SUBMISSION
**Source:** Unified audit synthesis (SYNTHESIS.md), audits A1, A2, A6

---

## Dependency Graph

```
R1 (Sep spec) ──→ R3 (paper1 Sep) ──→ R4 (paper2 Sep)
                                   └──→ R5 (T7 restatement)
R2 (C_t codomain) ── no dependencies
R6 (QM1) ── no dependencies
R7 (Transport FP) ── no dependencies
R8 (Autopoiesis) ── no dependencies
R9 (MFG precedent) ── no dependencies
R10 (paper2 closure) ── no dependencies
R11 (CLAUDE.md counts) ── no dependencies
R12 (Persist code label) ── no dependencies
R13 (paper1 conclusion) ── no dependencies
```

Items R2, R6–R13 are independent and can be done in any order or in parallel.
R3/R4/R5 depend on R1 being decided first.

---

## R1: Sep Definition — Spec Must Adopt u-weighted Form

**Severity:** CRITICAL (E1, A2 §4.1, SYNTHESIS #1)
**File:** `Canonical Spec v2.0.md`, §7.1 (around line 404–411)
**Why urgent:** The spec defines C_t-weighted Sep; the code, all experiments, and the proved Sep=1−E_sep/m bridge all use u-weighted. A reviewer comparing the formal definition to the experiments will see a contradiction. The C_t-weighted form is demonstrably broken (gives ~0.5 regardless of formation quality).

**Current text (spec §7.1):**
```
$$\mathsf{Sep}_t(u_t) = \frac{\sum_{x \in X_t} \mathbf{C}_t(x,x)\, \mathbf{D}_t(x;\, 1-u_t)}{\sum_{x \in X_t} \mathbf{C}_t(x,x)}$$

This is a $\mathbf{C}_t$-weighted average of distinction over all sites, where the self-co-belonging $\mathbf{C}_t(x,x)$ serves as a natural importance weight: sites with higher cohesive participation (and hence higher self-co-belonging, by C3'') contribute more to the separation score. This formulation is threshold-independent and naturally continuous.

**Change from v1.0:** The original Sep was a simple average of $\mathbf{D}_t$ over the crisp interior $\mathrm{Int}_t$. The revised form avoids crisp thresholds and incorporates the non-local information carried by $\mathbf{C}_t$.

**Note on proved bounds:** The exact equality $\mathsf{Sep} = 1 - \mathcal{E}_{\mathrm{sep}}/m$ was proved for the original (unweighted) Sep. The relationship between the $\mathbf{C}_t$-weighted Sep and $\mathcal{E}_{\mathrm{sep}}$ is an open problem.
```

**Replacement text:**
```
$$\mathsf{Sep}_t(u_t) = \frac{\sum_{x \in X_t} u_t(x)\, \mathbf{D}_t(x;\, 1-u_t)}{\sum_{x \in X_t} u_t(x)}$$

This is a $u$-weighted average of distinction over all sites. The cohesion value $u_t(x)$ serves as a natural importance weight: sites with higher cohesion contribute more to the separation score. This formulation is threshold-independent, naturally continuous, and restricts the average to the formation's own support.

**Change from v1.0:** The original Sep was a simple average of $\mathbf{D}_t$ over the crisp interior $\mathrm{Int}_t$. The v2.0 revision avoids crisp thresholds and focuses on the formation support. An intermediate $\mathbf{C}_t$-weighted formulation was considered but rejected: because $\mathbf{C}_t(x,x)$ assigns substantial weight to exterior nodes, the $\mathbf{C}_t$-weighted average yields approximately $0.5$ regardless of formation quality, providing no diagnostic discrimination.

**Proved bounds:** The exact equality $\mathsf{Sep} = 1 - \mathcal{E}_{\mathrm{sep}}/m$ holds for this $u$-weighted formulation (see proved results below).
```

**Dependencies:** None. This is the root fix.

---

## R2: C_t Codomain — Fix Internal Spec Contradiction

**Severity:** MODERATE (E2, A2 §3.1, SYNTHESIS #17)
**File:** `Canonical Spec v2.0.md`, §6 Group C header (around line 306)
**Why urgent:** The spec contradicts itself: §3.6 says `[0,∞)`, Group C header says `[0,1]`. The resolvent produces diagonal values ≥ 1, so `[0,1]` is wrong.

**Current text (spec §6, Group C header):**
```
The soft co-belonging operator $\mathbf{C}_t : X_t \times X_t \to [0,1]$ measures the degree to which two sites participate in the same cohesive formation.
```

**Replacement text:**
```
The soft co-belonging operator $\mathbf{C}_t : X_t \times X_t \to [0,\infty)$ measures the degree to which two sites participate in the same cohesive formation.
```

**Dependencies:** None.

---

## R3: Paper1 Sep Definition — Align with u-weighted

**Severity:** CRITICAL (E1, A6 §1.1)
**File:** `papers/paper1_math.tex`, line 259–262
**Why urgent:** The formal definition says C_t-weighted but all experiments use u-weighted. Reviewer will catch this immediately.

**Current text:**
```latex
\textbf{Separation.} The $\mathbf{C}$-weighted separation predicate:
\begin{equation}
\Sep(u) = \frac{\sum_{x} \mathbf{C}(x,x)\,\mathbf{D}(x; 1-u)}{\sum_{x} \mathbf{C}(x,x)}.
\end{equation}
```

**Replacement text:**
```latex
\textbf{Separation.} The $u$-weighted separation predicate:
\begin{equation}
\Sep(u) = \frac{\sum_{x} u(x)\,\mathbf{D}(x; 1-u)}{\sum_{x} u(x)}.
\end{equation}
```

**Dependencies:** R1 (spec decision must be made first).

---

## R4: Paper2 Sep Definition — Align with u-weighted

**Severity:** CRITICAL (E1, A6 §1.1)
**File:** `papers/paper2_cogsci.tex`, lines 183–186
**Why urgent:** Same contradiction as R3.

**Current text:**
```latex
\text{Sep}(u) = \frac{\sum_x C_t(x,x) \cdot D_t(x; 1-u)}{\sum_x C_t(x,x)}
```
and the subsequent sentence referencing "the co-belonging operator's diagonal $C_t(x,x)$."

**Replacement text:**
```latex
\text{Sep}(u) = \frac{\sum_x u(x) \cdot D_t(x; 1-u)}{\sum_x u(x)}
```
Replace the explanation sentence with:
```
This is a $u$-weighted average of distinction: sites with higher cohesion contribute more to the separation score. This formulation avoids crisp thresholds and restricts the assessment to the formation's own support.
```

**Dependencies:** R1 (spec decision must be made first).

---

## R5: T7 (Enhanced Metastability) — Restate as Hessian Curvature, Not Barrier Depth

**Severity:** CRITICAL (E8, A1, SYNTHESIS #2)
**File:** `papers/paper1_math.tex`, lines 386–408
**Why urgent:** The proof shows larger minimum Hessian eigenvalue (local curvature), not deeper energy barrier (saddle-point height). These are different quantities. "Deeper basins" is a conceptual error. A reviewer familiar with Morse theory will reject this.

**Current theorem statement (line 387–389):**
```latex
Let $\hat{u}$ be a non-trivial constrained minimizer of the full energy $\mathcal{E} = \lambda_{\mathrm{cl}}\mathcal{E}_{\mathrm{cl}} + \lambda_{\mathrm{sep}}\mathcal{E}_{\mathrm{sep}} + \lambda_{\mathrm{bd}}\mathcal{E}_{\mathrm{bd}}$ on $\Sigma_m$. Then $\hat{u}$ has a strictly larger energy barrier than any corresponding minimizer of $\mathcal{E}_{\mathrm{bd}}$ alone with the same $\alpha, \beta$ parameters.
```

**Replacement theorem statement:**
```latex
Let $\hat{u}$ be a non-trivial constrained minimizer of the full energy $\mathcal{E} = \lambda_{\mathrm{cl}}\mathcal{E}_{\mathrm{cl}} + \lambda_{\mathrm{sep}}\mathcal{E}_{\mathrm{sep}} + \lambda_{\mathrm{bd}}\mathcal{E}_{\mathrm{bd}}$ on $\Sigma_m$, and assume $\hat{u}$ lies in a neighborhood of the closure fixed point where $\|J_{\mathrm{Cl}}\|_{\mathrm{op}} < 1$. Then the minimum eigenvalue of $\nabla^2 \mathcal{E}|_{T_{\hat{u}}\Sigma_m}$ strictly exceeds that of $\nabla^2 \mathcal{E}_{\mathrm{bd}}|_{T_{\hat{u}}\Sigma_m}$, with the enhancement bounded below by $\lambda_{\mathrm{cl}} \cdot 2(1 - \|J_{\mathrm{Cl}}\|_{\mathrm{op}})^2$.
```

**Also fix the proof text (line 395–396).** Current:
```latex
a larger minimum eigenvalue means a deeper basin.
```
Replace with:
```latex
a larger minimum eigenvalue means greater local curvature at the minimizer.
```

**Also fix the conclusion (line ~871).** Current:
```
Self-referential energy basins are $4$--$17\times$ deeper than pure Allen--Cahn basins, quantitatively confirming Theorem~\ref{thm:metastability}.
```
Replace with:
```
Self-referential energy basins exhibit $4$--$17\times$ larger minimum Hessian eigenvalues than pure Allen--Cahn basins in our experiments, consistent with Theorem~\ref{thm:metastability}.
```

**Dependencies:** None.

---

## R6: QM1 — Fix False Theorem (Q_morph = c for Uniform Field, Not 0)

**Severity:** CRITICAL (E6, A2 §4.3, SYNTHESIS #4)
**File:** `Canonical Spec v2.0.md`, §13 (around line 797–798)
**Why urgent:** QM1 claims Q_morph vanishes on uniform fields. It does not: for u ≡ c > 0, l_max = c, l_second = 0, Artic = 1, Q_morph = c. The proof says "uniform fields have Artic = 0" — this is false (Artic = 1 for uniform fields because all merge bars have zero length).

**Current text:**
```
QM1 (vanishing on uniform fields) ... *Proof:* QM1 — uniform fields have Artic = 0.
```

**Two options (choose one):**

**Option A (redefine Q_morph — recommended):** Change the formula to subtract the uniform baseline:
```
$\mathcal{Q}_{\mathrm{morph}} = \ell_{\max} \cdot \mathrm{Artic} - c$

where $c = m/n$ is the mean field value. QM1: for $u \equiv c$, $\mathcal{Q}_{\mathrm{morph}} = c \cdot 1 - c = 0$. ✓
```

**Option B (weaken QM1):** Change the axiom:
```
QM1 (bounded by mean value on uniform fields): For $u \equiv c$, $\mathcal{Q}_{\mathrm{morph}}(u) = c$, which vanishes only when $c = 0$. Structured fields with the same mean achieve strictly higher $\mathcal{Q}_{\mathrm{morph}}$.
```
This is weaker but avoids changing the formula used in code and other theorems.

**Note:** If Option A is chosen, `scc/diagnostics.py` `inside_predicate()` must also be updated to subtract `c`, and tests will need adjustment.

**Dependencies:** None.

---

## R7: Transport Fixed-Point — Downgrade from "Theorem" to Conditional

**Severity:** HIGH (E3, A6 §1.8, SYNTHESIS #3)
**File:** `papers/paper1_math.tex`, lines 610–629
**Why urgent:** The Brouwer proof requires continuity of Φ, but the energy re-optimization step is discontinuous at degenerate/bifurcation points. The proof sketch says "at non-degenerate points" in passing but this is an essential hypothesis, not an aside.

**Current theorem statement (line 611–613):**
```latex
\begin{theorem}[Self-Referential Transport: Fixed-Point Existence]
\label{thm:transport-existence}
The map $\Phi : \Sigma_m \to \Sigma_m$ has at least one fixed point.
\end{theorem}
```

**Replacement:**
```latex
\begin{theorem}[Self-Referential Transport: Fixed-Point Existence (Conditional)]
\label{thm:transport-existence}
Assume the energy minimizer at each time step is non-degenerate (i.e., the constrained Hessian has no zero eigenvalues). Then the map $\Phi : \Sigma_m \to \Sigma_m$ is continuous, and by Brouwer's theorem has at least one fixed point.
\end{theorem}
```

**Also update the abstract (line ~55).** Current:
```latex
whose existence we establish via Brouwer's theorem
```
Replace with:
```latex
whose existence we establish via Brouwer's theorem under a non-degeneracy hypothesis
```

**Dependencies:** None.

---

## R8: Autopoiesis Claim — Downgrade to "Structural Analogue"

**Severity:** HIGH (D1, A6 O10, SYNTHESIS #5)
**File:** `papers/paper2_cogsci.tex`, abstract (line 29)
**Why urgent:** Autopoiesis requires physical self-production of components (Maturana & Varela). SCC has fixed operators with fixed parameters — this is nonlinear optimization, not self-production. Autopoiesis scholars (Thompson, Di Paolo) will reject this claim.

**Current text (abstract, line 29):**
```
formalizing the autopoietic insight that cognitive systems maintain themselves through self-production
```

**Replacement:**
```
capturing a structural analogue of the autopoietic insight that cognitive systems maintain themselves through self-referential organization
```

**Also search paper2 for other "formaliz* autopoie*" instances** (likely in §VII-B) and apply the same softening: "structural analogue" not "formalization."

**Dependencies:** None.

---

## R9: "No OT Precedent" — Add MFG Citation

**Severity:** HIGH (D2, A6 O3/U4, SYNTHESIS #6)
**File:** `papers/paper1_math.tex`, line ~81
**Why urgent:** Mean-field games (Lasry & Lions 2007) involve transport where costs depend on the distribution — a structural precedent. A reviewer familiar with MFG will immediately provide a counterexample.

**Current text (line ~81):**
```latex
is without precedent in the phase-field literature
```

**Replacement:**
```latex
is, to our knowledge, without direct precedent in the phase-field literature, though mean-field games~\cite{LasryLions2007} involve distribution-dependent transport costs in a different mathematical setting
```

Add to bibliography:
```latex
@article{LasryLions2007,
  author={Lasry, Jean-Michel and Lions, Pierre-Louis},
  title={Mean field games},
  journal={Japanese Journal of Mathematics},
  volume={2},
  number={1},
  pages={229--260},
  year={2007}
}
```

**Dependencies:** None.

---

## R10: Paper2 Closure Formula — Align with Spec/Paper1/Code

**Severity:** MODERATE (E4, A6 §1.2/O14, SYNTHESIS #18)
**File:** `papers/paper2_cogsci.tex`, line 159
**Why urgent:** Paper2 presents a "pure aggregation" closure formula missing the self-retention term `(1-η)*u(x)`. A reader comparing the two papers sees different operators with no explanation.

**Current text (line 159):**
```latex
\mathrm{Cl}_t(u)(x) = \sigma\!\left(\frac{a_{\mathrm{cl}}}{z_x} \sum_{y} N_t(x,y)\, u_t(y) - b_{\mathrm{cl}}\right)
```

**Replacement (option: full formula with pedagogical note):**
```latex
\mathrm{Cl}_t(u)(x) = \sigma\!\left(a_{\mathrm{cl}}\left[(1-\eta_{\mathrm{cl}})\, u(x) + \eta_{\mathrm{cl}} \sum_{y} \frac{N_t(x,y)}{z_x}\, u_t(y)\right] - \tau_{\mathrm{cl}}\right)
```
Add after the equation:
```
where $\eta_{\mathrm{cl}} \in [0,1]$ balances self-retention against neighborhood aggregation (the companion paper~\cite{paper1} provides the full mathematical treatment).
```

**Dependencies:** None.

---

## R11: CLAUDE.md — Correct Theorem Count and Sep Description

**Severity:** MODERATE (E5, A6 §1.5, SYNTHESIS #23)
**File:** `/home/jack/ex/CLAUDE.md`, line 106
**Why urgent:** "22+ proved theorems" conflates rigorous proofs, proofs-with-gaps, and conjectures. Misleads contributors.

**Current text (line 106):**
```
**22+ proved theorems** including: closure contraction (T6), phase transition (T8-Core), gradient flow convergence (T14), Γ-convergence (T11), Sep covariance identity, T-Persist-1 (conditional)
```

**Replacement:**
```
**12 rigorously proved theorems** (closure contraction T6, phase transition T8-Core, gradient flow convergence T14, Γ-convergence T11, Sep covariance identity, axiom consistency T20, and others), plus ~10 additional results at various stages (conditional, proved-with-gaps, or conjectured). See Canonical Spec §13 for the full registry.
```

**Dependencies:** None.

---

## R12: Persist Code — Label as Placeholder

**Severity:** MODERATE (E9, A2 §4.5, SYNTHESIS #9)
**File:** `scc/diagnostics.py`, lines 142–149
**Why urgent:** The code computes `1 - ||u_curr - u_prev|| / ||u_prev||` (L2 field similarity). The spec defines core-to-core structural inheritance via transport kernel M_{t→s}. These are completely different quantities. Anyone comparing code to spec will be confused.

**Current docstring (line 143):**
```python
"""Persist in [0,1]: temporal inheritance. 1.0 for static optimization."""
```

**Replacement docstring:**
```python
"""Persist in [0,1]: PLACEHOLDER — L2 field-change proxy.

    NOTE: This does NOT implement the spec formula (Spec §7.1), which requires
    a transport kernel M_{t->s} and core-to-core structural inheritance.
    This placeholder computes 1 - ||u_curr - u_prev||/||u_prev|| as a simple
    field-similarity measure. Returns 1.0 for static (single-time) optimization.
    See Open Problem: temporal transport implementation.
    """
```

**Dependencies:** None.

---

## R13: Paper1 Conclusion — Remove Unsubstantiated Claims

**Severity:** MODERATE (E7, A6 O6/O7, SYNTHESIS #22)
**File:** `papers/paper1_math.tex`, lines ~871–873
**Why urgent:** The conclusion cites K=2 multi-formation experiments and 45-config sensitivity analysis, but neither is described in the experiments section (Section V). A reviewer will look for these and not find them.

**Current text:**
```latex
Parameter sensitivity analysis across 45 configurations shows formation quality is structurally robust (44/45 achieve min(Bind, Sep, Inside) $> 0.7$). Multi-formation (K$=$2) experiments confirm spatially separated formations with per-formation diagnostics.
```

**Two options:**

**Option A (remove — recommended for now):** Delete both sentences entirely. They can be restored when the experiments are added to Section V.

**Option B (hedge):** Replace with:
```latex
Preliminary parameter sweeps suggest structural robustness across a range of configurations, and initial multi-formation experiments are promising; full results are deferred to future work.
```

**Dependencies:** None.

---

## Execution Order (Recommended)

**Phase 1 — Root decisions (do first):**
1. R1: Decide Sep = u-weighted in spec (root dependency)
2. R6: Decide QM1 fix strategy (Option A or B)

**Phase 2 — Propagate decisions + independent fixes (parallelizable):**
3. R2: Fix C_t codomain in spec (1-line fix)
4. R3: Fix paper1 Sep definition
5. R4: Fix paper2 Sep definition
6. R5: Fix T7 in paper1 (theorem + proof + conclusion)
7. R7: Downgrade transport theorem in paper1
8. R8: Soften autopoiesis in paper2
9. R9: Add MFG citation in paper1
10. R10: Fix closure formula in paper2
11. R11: Fix CLAUDE.md theorem count
12. R12: Label Persist code as placeholder
13. R13: Remove unsubstantiated conclusion claims

**Phase 3 — Verify consistency:**
14. Grep all files for stale "C_t-weighted Sep" language
15. Grep paper2 for other autopoiesis "formaliz*" instances
16. Run `python3 -m pytest tests/ -v` to confirm no code breakage (only R6 Option A and R12 touch code)

---

## What This Checklist Does NOT Cover

These are important but not submission-blocking:
- β_crit → 0 at scale (SYNTHESIS #7) — requires new analysis
- C3'' symmetrization proof gap — acknowledged in paper1 already
- A1' θ_support specification — not referenced in papers
- Proto-cohesion downgrade from theorem to conjecture — papers already hedge
- "Triple-mode self-reference" overclaim — moderate, not fatal
- Paper2 Persist formula mismatch (line 219, crisp set-intersection vs continuous) — should also be fixed but lower priority than the items above
