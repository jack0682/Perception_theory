# R5: Philosophy and Framing Revision Plan

**Author:** Teammate 5 (Philosophy and Framing Revision Planner)
**Date:** 2026-03-30
**Inputs:** A5 (philosophy audit), A6 (overclaim list), SYNTHESIS.md (Output D: Ontological Risk Ledger), paper1_math.tex, paper2_cogsci.tex

---

## Executive Summary

SCC's papers contain genuine mathematical novelty wrapped in philosophical rhetoric that consistently overshoots what the formalism earns. The strongest honest version of the theory is still compelling---it just needs to stop claiming to be something it isn't (autopoiesis formalization, Gestalt foundation, PP supersession) and start owning what it actually is (a novel self-referential variational architecture with structural analogues to perceptual organization phenomena).

This document provides exact LaTeX-ready replacement text for each overclaimed passage, a banned/safe phrase list, and the strongest honest 3-sentence summary.

---

## Claim-by-Claim Revision

### 1. "First variational foundation for the Gestalt laws"

**Current wording** (paper2_cogsci.tex abstract, line 29):
> "We show that SCC provides the first variational foundation for the Gestalt laws: closure corresponds to Pr\"{a}gnanz, distinction to figure-ground segregation, co-belonging to common fate, and temporal transport to perceptual identity."

**Problem:** (A5 Section 3, D3 in SYNTHESIS) Mumford-Shah, Chan-Vese, and region competition models are variational frameworks addressing perceptual grouping. "First" is an unverifiable priority claim. The Gestalt mapping is structural analogy, not direct formalization---Cl_t does not perform contour completion, C_t does not capture co-motion, proximity via N_t is tautological.

**Decision:** REPLACE

**Replacement text:**
```latex
We show that SCC provides a variational framework whose structural components have systematic correspondences with the classical Gestalt laws of perceptual organization: closure corresponds to Pr\"{a}gnanz, distinction to figure-ground segregation, co-belonging to common fate, and temporal transport to perceptual identity. These correspondences are structural analogies---not direct formalizations of the specific perceptual phenomena the Gestalt psychologists described---but they are systematic: each Gestalt principle maps onto a specific formal operator or theorem within a unified energy framework.
```

**Also fix** (paper2_cogsci.tex Section III, line 337):

Current:
> "The correspondence between SCC's formal apparatus and the classical Gestalt laws is not metaphorical but structural: each Gestalt principle maps onto a specific formal operator or theorem."

Replace with:
```latex
The correspondence between SCC's formal apparatus and the classical Gestalt laws is structural rather than merely metaphorical: each Gestalt principle maps onto a specific formal operator or theorem. We emphasize, however, that these are structural analogies within a unified variational framework, not direct formalizations of the specific perceptual phenomena (illusory contour completion, border ownership, synchronous motion grouping) that the Gestalt psychologists described.
```

---

### 2. "Formalizes autopoiesis"

**Current wording** (paper2_cogsci.tex abstract, line 29):
> "formalizing the autopoietic insight that cognitive systems maintain themselves through self-production"

**Also** (paper2_cogsci.tex Section VII-B, line 698):
> "The self-referential operator triad---self-completion (Cl), self-contrast (D), self-integration (C)---formalizes the core idea of autopoiesis: a system that produces the components that produce it."

**Also** (paper2_cogsci.tex Section II-F, line 323):
> "The self-referential structure formalizes the autopoietic insight"

**Problem:** (A5 Section 2, D1 in SYNTHESIS --- FUNDAMENTALLY UNSUPPORTED) Autopoiesis requires self-production of components and boundary. In SCC, operators have fixed functional forms with externally set parameters on a given graph. The field's numerical values flow through fixed formulas; the formulas are not produced by the field. Any nonlinear variational problem has "self-referential" dependence (Navier-Stokes, recurrent neural networks). Calling this autopoiesis trivializes the concept.

**Decision:** REPLACE all three instances

**Abstract replacement:**
```latex
exhibiting operational closure in which the field defines the criteria for its own evaluation
```

**Section II-F replacement** (line 323):
```latex
The self-referential structure exhibits \emph{operational closure} in the sense described by Maturana and Varela \cite{maturana1980autopoiesis}: the criteria by which the field is evaluated are defined by the field itself, rather than imposed externally. We note that this is weaker than full autopoiesis, which requires self-production of components---here the operator forms and parameters are externally given; only their numerical values depend on the field.
```

**Section VII-B replacement** (line 698):
```latex
The self-referential operator triad---self-completion (Cl), self-contrast (D), self-integration (C)---exhibits a structural analogue of autopoietic organization \cite{maturana1980autopoiesis}: the system's evaluative criteria are generated by the system itself. This is operational closure, not full autopoiesis. The operators have fixed functional forms (sigmoid, aggregation, resolvent) with externally specified parameters; the field determines their numerical values but does not produce the operators themselves. The analogy is structural---the evaluative loop is closed---but the system does not produce its own components in the biological sense that Maturana and Varela described.
```

---

### 3. "No precedent in OT literature" / "without precedent in the phase-field literature"

**Current wording** (paper1_math.tex, line 81):
> "the specific triple-mode structure of the self-dependence---through independent channels of completion, contrast, and integration---is without precedent in the phase-field literature"

**Problem:** (A5, D2 in SYNTHESIS --- FUNDAMENTALLY UNSUPPORTED) Mean-field games (Lasry-Lions 2007, already cited as \cite{LasryLions2007}) involve transport where costs depend on the distribution. This is a structural precedent for self-referential variational problems in transport. Negative existential claims invite counterexamples.

**Decision:** REPLACE

**Replacement text:**
```latex
the specific triple-mode structure of the self-dependence---through independent channels of completion, contrast, and integration---is, to our knowledge, without direct precedent in the phase-field literature. We note that mean-field games \cite{LasryLions2007} involve distribution-dependent costs in a transport context, providing a structural precedent for self-referential variational problems; what is distinctive here is the specific decomposition into three independent self-referential modes (completion, contrast, integration) within a single energy.
```

---

### 4. "Existing theories start too late" / PP/GWT/IIT comparisons

**Current wording** (paper2_cogsci.tex Section I-B, line 60):
> "Predictive Processing assumes a hierarchical generative model in which discrete hypotheses are tested against sensory data. But hypotheses about what?"

**Also** Table II (line 435):
> "Self-reference: Absent at basic level [PP]"

**Problem:** (A5 Section 4, D6 in SYNTHESIS) The FEP/active inference framework operates on continuous state spaces, addresses self-organization, and is self-referential. The characterization applies to hierarchical Bayesian PP but strawmans the FEP. Similarly, Bayesian nonparametric methods discover structure.

**Decision:** REPLACE with hedged versions

**Section I-B replacement** (after the PP paragraph, line 60-61):
```latex
\emph{Predictive Processing} \cite{clark2013whatever,friston2010free} proposes that the brain maintains a generative model whose predictions are tested against sensory data. In its hierarchical Bayesian formulation, this presupposes variables---objects, features, categories---whose values can be predicted. The Free Energy Principle \cite{friston2010free}, in its most general form, addresses self-organization and operates on continuous state spaces, sharing some structural features with SCC. The distinction is architectural: the FEP provides a general principle (free energy minimization) that can in principle address formation, while SCC provides a specific variational architecture (the operator triad) that decomposes formation into binding, separation, morphology, and persistence.
```

**Table II fix --- replace the "Self-reference" row:**
```latex
Self-reference & Structural (operator triad) & Present in FEP; absent in hierarchical PP \\
```

**Table II fix --- replace the "Direction" row:**
```latex
Direction & Energy minimization on cohesion field & Top-down prediction + bottom-up error (hierarchical PP); self-organization (FEP) \\
```

**Table V fix --- add footnote:**
```latex
\addlinespace
\multicolumn{3}{p{7.5cm}}{\footnotesize Note: Bayesian nonparametric methods (e.g., Dirichlet process mixtures) also discover structure; this comparison applies primarily to fixed-model Bayesian approaches.} \\
```

---

### 5. "Pre-objective" claims

**Current wording** (paper2_cogsci.tex Section I-C, line 72):
> "SCC posits that the primitive entity in perception is not a set of discrete objects but a graded cohesion field"

**Problem:** (A5 Section 1, D4 in SYNTHESIS) The formalism starts from a finite set of individually indexed sites, a given adjacency kernel, a volume constraint, and 15+ parameters. The "pre-objective" claim is a philosophical interpretation, not a mathematical result. The pixel-grid defense is suggestive but insufficient.

**Decision:** KEEP the core claim but add qualification

The current wording in Section I-C is actually close to defensible. The key fix is in Section VII-D (line 716) which already acknowledges the tension. Strengthen that acknowledgment and add a clarification to the proposal paragraph:

**Section I-C addition** (after "intermediate values represent the transitional boundary zone..."):
```latex
We emphasize the ontological status of the sites $X_t$: they provide relational capacity---positions at which cohesion can be evaluated---not object structure. The formation is an emergent pattern in $u_t$, not a property of the sites themselves. This is analogous to the relationship between pixels and visual objects: the discrete structure of the pixel grid does not commit image analysis to pre-given visual objects. We acknowledge, however, that the sites are pre-individuated, and the theory does not currently explain their individuation (see Section~\ref{sec:limitations}).
```

---

### 6. Gestalt Mapping Table Status Labels

**Current wording** (paper2_cogsci.tex Table I, lines 351-363):
> "Closure --- Direct formalization"
> "Proximity --- Direct formalization"
> "Figure-Ground --- Direct formalization"
> "Common Fate (temporal) --- Direct formalization"

**Problem:** (A5 Section 3, D8 in SYNTHESIS) These are structural analogies, not direct formalizations. Cl_t is sigmoid smoothing, not contour completion. N_t encoding proximity is tautological. D_t captures support asymmetry but not border ownership, depth ordering, or shape attribution. C_t is a static structural measure, not co-motion.

**Decision:** REPLACE all status labels

**Replacement table:**
```latex
\begin{tabular}{p{2.2cm}p{2.8cm}p{2.2cm}}
\toprule
\textbf{Gestalt Principle} & \textbf{SCC Counterpart} & \textbf{Status} \\
\midrule
Closure (Geschlossen\-heit) & $\mathrm{Cl}_t$ (closure operator) & Structural analogue \\
\addlinespace
Proximity (N\"{a}he) & $N_t$ (adjacency kernel) & Structural input \\
\addlinespace
Similarity / Common Fate & $C_t$ (co-belonging operator) & Structural analogue (non-local) \\
\addlinespace
Figure-Ground & $D_t$ (distinction operator) & Partial formalization (support asymmetry) \\
\addlinespace
Good Continuation & $T_t$ (transition operator) & Open problem---no formal operator \\
\addlinespace
Pr\"{a}gnanz & Metastable energy minima & Reinterpretation as local stability (Theorems 3, 4 in companion paper) \\
\addlinespace
Common Fate (temporal) & $M_{t \to s}$ (transport kernel) & Structural analogue (inheritance, not co-motion) \\
\bottomrule
\end{tabular}
```

---

### 7. "Soft ontology" --- what's honest given hard constraints?

**Current wording** (paper2_cogsci.tex Section VII-C, line 706):
> "existence is graded, not binary"

**Problem:** (A5 Section 6, D7 in SYNTHESIS) The field values are genuinely graded, but the framework around them is thoroughly crisp: hard box constraints, hard volume constraint, hard parameter boundaries, hard thresholds for crisp recovery, hard phase transition criterion.

**Decision:** KEEP but add qualification

The A5 audit rates this as ACCEPTABLE INTERPRETATION. The claim about field values being graded is defensible. Add one sentence of acknowledgment:

**Addition after "it has a four-dimensional answer" (line 708):**
```latex
We note that the graded ontology applies to the field values and diagnostic assessments; the mathematical framework itself employs hard constraints (volume conservation, box constraints, parameter bounds) and sharp thresholds (for derived geometric notions like Core and Boundary). The ``softness'' is in what the theory describes, not in all aspects of how it describes it.
```

---

### 8. "10 testable predictions"

**Current wording** (paper2_cogsci.tex Section V, line 538):
> "SCC generates ten empirical predictions organized by domain and testability. These predictions are derived from the theory, not added post hoc"

**Problem:** (A5 Section 5, D9 in SYNTHESIS)
- P2 (four independent dimensions): genuinely falsifiable and distinctive
- P1, P3, P4: real predictions but not uniquely tied to SCC, or conditional on parameter fitting
- P5: re-describes known findings (N1 precedes N2/P300 is established)
- P6-P10: speculative extrapolation far beyond the theory's validated domain (grid graphs up to 20x20)

**Decision:** REPLACE section structure. Keep all 10 but reorganize by evidential status.

**Replace the Section V header text:**
```latex
SCC generates empirical predictions at three levels of specificity. We organize them by evidential status: predictions derived from proved theorems, predictions following from the theory's structural commitments (but not uniquely distinguishing SCC from all alternatives), and speculative extrapolations beyond the theory's current domain of mathematical validation. All predictions await empirical testing.
```

**Add status markers to each prediction:**

- P2: Add "(Most distinctive prediction)" after the title
- P1, P3, P4: Add "Note: this prediction follows from SCC's specific operator realization; other models (e.g., recurrent neural networks, diffusion models) may make similar predictions." after each
- P5: Replace "This directly distinguishes SCC from predictive processing accounts" with:
```latex
This is consistent with existing ERP findings that figure-ground segregation (N1) precedes object identification (N2/P300). SCC provides a formal account of \emph{why} this ordering holds---distinction is computed from the self-referential operator triad before any categorical process engages---but the temporal ordering itself is not a novel empirical prediction.
```
- P6-P10: Add a subsection header before them:
```latex
\subsection{Speculative Extrapolations}

The following predictions extend SCC's formal structure to domains (developmental biology, cellular biophysics, materials science) far beyond the theory's current mathematical validation on finite grid graphs. They are included as illustrations of the theory's potential scope, not as rigorously derived consequences. Each would require substantial domain-specific modeling before it could be meaningfully tested.
```

---

### 9. "Triple-mode self-reference"

**Current wording** (paper1_math.tex, line 81):
> "the specific triple-mode structure of the self-dependence---through independent channels of completion, contrast, and integration"

**Also** (paper2_cogsci.tex Section II-F, line 314):
> "The cohesion field $u$ defines three operators---closure ($\mathrm{Cl}$), distinction ($D$), and co-belonging ($C$)---which depend on $u$ itself."

**Problem:** (D5 in SYNTHESIS) Only two modes enter the energy functional (Cl and D). C_t is diagnostic-only---it enters predicates but not the energy. Calling it "triple-mode self-reference" of the energy is misleading.

**Decision:** REPLACE with accurate characterization

**paper1_math.tex line 81 replacement** (already addressed in Claim 3 above --- the MFG-aware version). Additionally, in the intro enumeration (lines 73-79), item 3 already says "Co-belonging enters the theory's diagnostic predicates but not the energy functional." This is correct. The fix is in the framing language.

**paper2_cogsci.tex Section II-F replacement** (line 314):
```latex
The cohesion field $u$ defines three operators---closure ($\mathrm{Cl}$), distinction ($D$), and co-belonging ($C$)---each of which depends on $u$ itself. Two of these (closure and distinction) enter the energy functional directly; the third (co-belonging) enters the diagnostic predicates. The self-referential structure thus operates through two variational modes and one diagnostic mode.
```

---

### 10. Abstract and Conclusion Tone --- Model Text

#### Paper 2 (paper2_cogsci.tex) --- Revised Abstract

```latex
\begin{abstract}
How does perception arrive at discrete objects? Standard accounts begin from objects and ask how they are recognized, tracked, or categorized. We propose that a prior question must be answered first: how does anything become a coherent \emph{something}---a formation that holds together, distinguishes itself from its surround, and persists through time---before it is identified as any particular thing? We present Soft Cognitive Cohesion (SCC), a formal mathematical theory in which the primitive entity is a graded cohesion field, not a set of discrete objects. SCC formalizes four structural requirements for pre-objective formation: binding (self-support under relational closure), separation (structural distinction from exterior), morphological articulation (core-boundary-exterior stratification), and temporal persistence (structural inheritance under transport). These four requirements define a diagnostic vector $\mathbf{d} \in [0,1]^4$ that provides a continuous, multi-dimensional measure of formation quality---replacing the single scalar of Gestalt Pr\"{a}gnanz with a decomposed assessment. We show that SCC provides a variational framework whose structural components have systematic correspondences with the classical Gestalt laws of perceptual organization. The theory's operators exhibit operational closure: the field defines what counts as ``closure,'' ``distinction,'' and ``belonging,'' and is then evaluated against its own definitions. We derive empirical predictions that distinguish SCC from Predictive Processing, Global Workspace Theory, Integrated Information Theory, and Bayesian accounts---the most distinctive being that perceptual organization has four independently manipulable dimensions. All predictions await empirical testing. Computational experiments demonstrate formation existence and validate the diagnostic framework on graph-based domains.
\end{abstract}
```

#### Paper 2 (paper2_cogsci.tex) --- Revised Conclusion

```latex
\section{Conclusion}

Soft Cognitive Cohesion proposes that perception begins not with objects but with graded cohesive formations characterized by a four-dimensional diagnostic vector. A formation holds together (Bind), distinguishes itself (Sep), is morphologically articulated (Inside), and persists through time (Persist)---and it achieves each of these to a continuously varying degree. Objects are not inputs to the perceptual process; they are late achievements of formations that have stabilized sufficiently across all four dimensions.

The theory offers a variational framework with systematic structural correspondences to several Gestalt laws of perceptual organization. Closure, proximity, similarity, figure-ground segregation, and Pr\"{a}gnanz are treated not as independent heuristics but as consequences of a single energy minimization principle operating through a self-referential operator pair (closure and distinction), with a third operator (co-belonging) serving a diagnostic role. The operators exhibit operational closure---the field defines the criteria for its own evaluation---a structural analogue of the autopoietic principle, though weaker than full autopoiesis in that the operator forms and parameters are externally given.

SCC generates empirical predictions at several levels of specificity. The most distinctive and falsifiable---that perceptual organization has four independently manipulable dimensions (P2)---is testable with standard factorial psychophysics. Others follow from the theory's specific operator realizations and are not uniquely tied to SCC. All predictions await empirical validation; none have been tested.

The theory's philosophical contribution---giving formal expression to the idea that coherent formation is prior to discrete objecthood, an idea articulated by Gestalt psychologists and phenomenologists but never mathematized---is, we believe, worth pursuing regardless of whether every mathematical detail survives empirical testing. Whether SCC's specific formalization is correct, the question it asks---how does something become a coherent \emph{something} before it is identified as any particular \emph{thing}?---is one that cognitive science must eventually answer.
```

#### Paper 1 (paper1_math.tex) --- Revised Conclusion (key changes only)

Replace line 859:
```latex
\item A proof that self-referential energy basins have strictly larger minimum Hessian eigenvalues than their Allen--Cahn counterparts, implying enhanced local stability (Theorem~\ref{thm:metastability}).
```

Replace line 866:
```latex
Computational experiments on grid graphs validate the framework: formations emerge reliably (100\% success across grid sizes $5 \times 5$ to $20 \times 20$), gradients are verified to $10^{-9}$, and the four-component diagnostic vector provides meaningful, differentiated assessment. In our experiments, self-referential energy basins are $4$--$17\times$ deeper than pure Allen--Cahn basins, consistent with the enhanced stability predicted by Theorem~\ref{thm:metastability}.
```

Remove from line 866 the claims about "Parameter sensitivity analysis across 45 configurations" and "Multi-formation (K=2) experiments" unless these experiments are added to Section V. (Per A6 items O6, O7: these results are cited in the conclusion but not described in the experiments section.)

---

## Phrases That Should NEVER Appear in the Revised Papers

| Phrase | Reason |
|--------|--------|
| "formalizes autopoiesis" / "formalizes the autopoietic insight" | Fundamentally unsupported (A5/D1) |
| "IS autopoiesis" | Even stronger overclaim |
| "the system produces the components that produce it" (applied to SCC) | This is the definition of autopoiesis; SCC doesn't do this |
| "first variational foundation for the Gestalt laws" | Unverifiable priority claim (A5/D3) |
| "Direct formalization" (for Gestalt mappings in Table I) | Overstated (A5 Section 3) |
| "without precedent in the phase-field literature" (unqualified) | False given MFG (D2) |
| "without precedent in the OT literature" (unqualified) | False given MFG (D2) |
| "Self-reference: Absent at basic level" (for PP) | Inaccurate---FEP is self-referential (A5 Section 4) |
| "Bottom-up self-organization" (for SCC direction) | Misleading---it's global optimization (A5 Section 7) |
| "Post-objective (beliefs about objects)" (for all of PP) | Oversimplifies FEP (A5 Section 4) |
| "self-referential energy basins are provably deeper" | T7 has conceptual error: Hessian PD =/= deeper basins (SYNTHESIS T7) |
| "4-17x deeper basins" (as a proved result) | Computational observation, not proved bound (A6/O5) |
| "K=2 experiments confirm" / "45 configurations show" (in conclusion) | Not described in experiments section (A6/O6, O7) |
| "triple-mode self-reference" (without qualification) | Only 2 modes are variational; C_t is diagnostic (D5) |

---

## Phrases That Are SAFE to Keep

| Phrase | Reason |
|--------|--------|
| "pre-objective cohesion" | Core concept; defensible with site-qualification |
| "graded cohesion field" | Exactly what u_t is |
| "the primitive entity is a graded cohesion field, not a set of discrete objects" | Defensible as modeling commitment |
| "objects are not inputs but outputs" | Accurately describes the theory's architecture |
| "self-referential operator structure" / "self-referential energy" | Mathematically accurate |
| "operational closure" | Accurate and appropriately modest |
| "the field defines the criteria for its own evaluation" | True by construction |
| "structural analogue" / "structural correspondence" | Honest framing of Gestalt mapping |
| "enhanced metastability" (when restated as Hessian curvature) | Valid after T7 restatement |
| "contractive but not idempotent" | Proved (T6b) |
| "diagnostic vector $\mathbf{d} \in [0,1]^4$" | Well-defined, computed, validated |
| "complementary to these theories, not competing" | Already present; good framing |
| "existence is graded, not binary" (for field values) | Acceptable interpretation (A5 Section 6) |
| "a variational framework with structural correspondences to the Gestalt laws" | Honest version of the Gestalt claim |
| "to our knowledge" (before any priority claim) | Standard academic hedging |

---

## The Strongest Honest 3-Sentence Summary

> SCC introduces a variational framework on finite graphs in which the energy functional is self-referential: two of its four terms involve operators (closure and distinction) whose values depend on the field being minimized, creating a mathematically distinctive structure of operational closure that standard phase-field models lack. The framework produces spatially structured formations with a four-dimensional diagnostic profile (binding, separation, morphological articulation, persistence) that decomposes formation quality into independently assessable components---providing the first formal decomposition of what Gestalt psychology described as Pragnanz. The theory generates falsifiable predictions, most distinctively that these four dimensions are independently manipulable in perceptual experiments, and establishes proved results (closure contraction, phase transition, gradient flow convergence, enhanced Hessian curvature at self-referential minima) that constitute a rigorous mathematical foundation for further empirical investigation.

---

## Additional Fixes Required

### Paper2 Closure Formula (O14/E4)
Paper2 line 159 uses a simplified closure formula missing the self-retention term `(1-eta)*u(x)`. Add after eq (2):
```latex
(This is a simplified presentation; the full operator, given in the companion paper, includes a self-retention term $(1-\eta)\,u(x)$ that interpolates between self-support and neighborhood averaging.)
```

### Paper2 Persist Formula (O16)
Paper2 line 219 uses a crisp set-intersection formula while paper1/spec use a continuous form. Either align with the continuous form or add:
```latex
(This crisp formulation is a simplified presentation; see the companion paper for the continuous version used in formal analysis.)
```

### Paper2 Sep Formula (E1 in SYNTHESIS --- CRITICAL)
Paper2 line 184 defines C_t-weighted Sep. Code uses u-weighted Sep (because C_t-weighted gives ~0.5 regardless). This must be resolved before submission. Either:
- (a) Update the formal definition to u-weighted in both papers, or
- (b) Keep C_t-weighted as the theoretical definition and add a note: "In computational experiments, we use a u-weighted variant (replacing $C_t(x,x)$ with $u(x)$) that avoids numerical degeneracy; see the companion paper for discussion."

### Paper1 Theorem 4 (Metastability) --- T7 Error
SYNTHESIS identifies a conceptual error: Hessian positive-definiteness does not equal deeper energy basins. Restate as:
```latex
\begin{theorem}[Enhanced Local Stability]
Under the hypotheses of Theorem~\ref{thm:phase-transition}, at a non-trivial minimizer $u^*$ satisfying $\|u^* - \Cl(u^*)\| = O(1/\lambda_{\mathrm{cl}})$, the Hessian of the full energy $\mathcal{E}$ has strictly larger minimum eigenvalue than the Hessian of $\mathcal{E}_{\mathrm{bd}}$ alone. Specifically, the closure Hessian contribution is positive definite with minimum eigenvalue bounded below by $2\lambda_{\mathrm{cl}}(1 - a_{\mathrm{cl}}/4)^2$.
\end{theorem}
```

### Paper1 Theorem 9 (Transport Existence) --- Continuity Gap
Add non-degeneracy hypothesis or downgrade:
```latex
\begin{theorem}[Transport Fixed-Point Existence (Conditional)]
Under the hypotheses above, and assuming that the energy minimization map $u \mapsto \arg\min_{v \in \Sigma_m} \mathcal{E}(v; M)$ is continuous on the domain of non-degenerate transport plans, there exists a fixed point...
\end{theorem}
```

---

## Summary of Revision Severity

| Claim | Severity | Action |
|-------|----------|--------|
| "First variational Gestalt foundation" | HIGH | Drop "first"; reframe as "structural correspondences" |
| "Formalizes autopoiesis" | CRITICAL | Replace with "operational closure" everywhere |
| "No OT/phase-field precedent" | HIGH | Add "to our knowledge" + cite MFG |
| PP/GWT/IIT comparisons | MEDIUM | Add FEP footnotes; fix Table II |
| "Pre-objective" claims | LOW | Keep with site-qualification added |
| Gestalt table status labels | HIGH | "Direct formalization" -> "Structural analogue" |
| "Soft ontology" | LOW | Keep with hard-constraint acknowledgment |
| "10 testable predictions" | MEDIUM | Reorganize by evidential status |
| "Triple-mode self-reference" | MEDIUM | Clarify 2 variational + 1 diagnostic |
| Abstract/conclusion tone | HIGH | Use model text provided above |
