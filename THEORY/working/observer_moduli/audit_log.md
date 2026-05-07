---
type: working/audit-log
created: 2026-05-07
project: Observer Moduli Space of SCC
---

# Audit Log — Observer Moduli Space

Records all significant mathematical decisions, rejected candidates, and overclaim warnings. Each entry is permanent; corrections are appended, not deleted.

---

## AUDIT-001 — U(1) Gauge Candidate Rejected

**Date:** 2026-05-07  
**Decision:** REJECTED  
**Decision-maker:** User correction (primary); theoretical verification (secondary)

**Proposed candidate.** The action $(\alpha, \beta) \mapsto (e^{i\varphi}\alpha, e^{i\varphi}\beta)$ for $\varphi \in [0, 2\pi)$, giving a $U(1)$ gauge symmetry on the observer parameters.

**Reason for rejection.** $\alpha, \beta > 0$ are strictly real positive. The $U(1)$ action $e^{i\varphi}$ for $\varphi \neq 0, \pi$ produces complex values, which are outside the domain. Even for $\varphi = \pi$: $e^{i\pi} = -1$, so $(\alpha, \beta) \mapsto (-\alpha, -\beta)$ exits $\mathbb{R}_{>0}^2$.

**Correct gauge.** The actual symmetry is $(\alpha, \beta) \mapsto (r\alpha, r\beta)$ for $r > 0$ (an $\mathbb{R}_{>0}$-scaling). This is a non-compact group (not $U(1)$). The compact version is obtained by fixing $\alpha + \beta = 1$, leaving $q = \beta/\alpha$ as the single free parameter — a quotient by $\mathbb{R}_{>0}$, not a compact group action.

**Consequence.** The compact gauge group $G_{\mathrm{SCC}}^{(0)}$ must be sought elsewhere: in label permutations ($S_K$) and spatial symmetries ($\mathrm{Aut}_{task}$), which do act on discrete/finite structures. The real parameters $(\alpha, \beta)$ are handled by normalization, not by a Lie group.

**Files affected.** DEF-3 in `definitions.md` (explicitly notes the U(1) rejection and correct quotient).

---

## AUDIT-002 — Finite Gauge Groups Do Not Reduce Dimension

**Date:** 2026-05-07  
**Decision:** CONFIRMED (standard result applied to SCC setting)

**Claim.** For a finite group $G$ acting on a manifold $M$ of dimension $n$, $\dim(M/G) = n$.

**Justification.** A finite group has dimension 0 as a Lie group. The dimension formula for orbit spaces under free proper actions of a Lie group $G$ of dimension $k$ is $\dim(M/G) = n - k$. For $k = 0$ (finite $G$), dimension is preserved at generic points. At fixed points, local structure is $\mathbb{R}^n / G_p$ (orbifold singularity), still of real dimension $n$.

**Application.** $S_K$ (order $K!$) and $\mathrm{Aut}_{task}$ (order divides $|\mathrm{Aut}(X_t)|$) are both finite, hence $\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}}$ has the same dimension as $\mathcal{M}_{\mathrm{obs}}$ at generic points.

**Overclaim warning.** It would be an error to claim that "the gauge group reduces the DOF count." The gauge group removes representation redundancy (identifies physically equivalent states) but does not lower the ambient dimension.

---

## AUDIT-003 — G_core-weight = {e} is a Default, Not a Theorem

**Date:** 2026-05-07  
**Decision:** DEFAULT (conservative; must be discovered)

**Status.** $G_{\mathrm{core\text{-}weight}} = \{e\}$ is currently set as the default in DEF-8. This means we assume no non-trivial compact group acts on energy weights $\lambda$ while preserving perceptual cores.

**Why this is a default, not a theorem.** No proof exists that such a symmetry is impossible. The $\mathbb{Z}_2$ candidate (closure-separation swap) has not been tested computationally. See OP-OMS-001.

**Risk.** If $G_{\mathrm{core\text{-}weight}}$ is in fact non-trivial (e.g., a $\mathbb{Z}_2$ symmetry), then $\mathcal{M}_{\mathrm{obs}} / G_{\mathrm{SCC}}^{(0)}$ has a smaller effective fundamental domain than currently computed.

**Required for promotion.** Any claim using $G_{\mathrm{core\text{-}weight}} = \{e\}$ must be labeled as "assuming default gauge" until OP-OMS-001 is resolved.

---

## AUDIT-004 — Criticality Hypothesis is Optional

**Date:** 2026-05-07  
**Decision:** TWO-VERSION POLICY

**Statement.** The criticality hypothesis ($q = q_c(X_t)$) makes $q$ scene-determined, removing it from the observer's free parameters. This is not required by the current SCC axioms — it is an additional assumption.

**Two versions:**
- $\mathcal{M}_{\mathrm{obs}}$ (unconstrained): $q \in [q_{\min}, q_{\max}]$ is free; full observer space.
- $\mathcal{M}_{\mathrm{obs}}^{\mathrm{crit}}$: criticality imposed; $q$ eliminated; reduced space.

**Overclaim warning.** It would be wrong to write "$q$ is not an observer parameter" as a theorem. It IS an observer parameter in the base model. Under the criticality hypothesis, it becomes scene-determined — but the hypothesis is a physical claim, not a mathematical necessity.

**Files affected.** DEF-4 and DEF-5 in `definitions.md` distinguish the two cases.

---

## AUDIT-005 — $\mathrm{Aut}_{task}$ is Not Pure Graph Automorphism

**Date:** 2026-05-07  
**Decision:** TASK-ANCHORED SUBGROUP

**Statement.** $\mathrm{Aut}_{task}(X_t, \mathcal{N}_t, K, \mathcal{A})$ is NOT the full graph automorphism group $\mathrm{Aut}(X_t)$. It is the subgroup preserving additional task-relevant structure.

**Anchors (from DEF-8):**
1. $\mathcal{N}_t$: task-relevant neighborhood structure (not purely graph-theoretic)
2. $K$: formation count (a permutation that changes which nodes are "formation-eligible" is excluded)
3. $\mathcal{A}$: attention mask (only symmetries that fix $\mathcal{A}$ setwise are included)

**Why this matters.** $\mathrm{Aut}(X_t)$ can be large (e.g., $S_n$ for the complete graph). Using the full $\mathrm{Aut}(X_t)$ would over-identify observer states and potentially collapse distinct perceptual configurations to a single point.

**Overclaim warning.** Never write "$G$ acts by graph automorphisms" without specifying the task anchors.

---

## AUDIT-006 — Observer Space is Compact by Tychonoff

**Date:** 2026-05-07  
**Decision:** CONFIRMED

**Claim.** $\mathcal{M}_{\mathrm{obs}} = [q_{\min}, q_{\max}] \times \Delta^3 \times B_\xi$ is compact.

**Proof method.** Each factor is compact:
- $[q_{\min}, q_{\max}]$: closed bounded interval in $\mathbb{R}$
- $\Delta^3$: closed bounded subset of $\mathbb{R}^4$ (proved in toy_models.md Prop A1)
- $B_\xi$: closed bounded polytope (by finite intersection of linear constraints on $\xi$)

Product of finitely many compact spaces is compact (Tychonoff for finite products = Heine-Borel in the product).

**Consequence.** $\mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}} = \mathcal{M}_{\mathrm{obs}} / G$ is compact (continuous image of compact under quotient map).

**Required for $B_\xi$.** The bound $a_{\mathrm{cl}} \in [1, a_{\mathrm{cl}}^{\max}]$ must be finite (which it is by physical interpretation). Similarly $\varepsilon_{\mathrm{OT}}, \theta_{\mathrm{core}}, \theta_{\mathrm{in}}$ are bounded by their physical domains.

---

## AUDIT-007 — Readout Map $P$ Descends to Quotient

**Date:** 2026-05-07  
**Decision:** CONFIRMED (conditional on gauge-invariance of $P$)

**Claim (DEF-10 / Prop 6).** The readout map $P : \mathcal{M}_{\mathrm{obs}} \to \mathcal{P}$ descends to a well-defined map $\bar{P} : \mathfrak{M}_{\mathrm{SCC}}^{\mathrm{obs}} \to \mathcal{P}$ iff $P$ is gauge-invariant: $P(g \cdot \Theta) = P(\Theta)$ for all $g \in G$.

**Verification for $S_K$.** Permuting formation labels $(u^{(1)}, \ldots, u^{(K)}) \mapsto (u^{(\sigma(1))}, \ldots, u^{(\sigma(K))})$ does not change the set of formations, only their labeling. Since $P_{\mathrm{top}}$ is defined in terms of topological invariants of the formation set (not individual labels), $P_{\mathrm{top}}$ is $S_K$-invariant. CONFIRMED for $S_K$.

**Verification for $\mathrm{Aut}_{task}$.** A spatial automorphism permutes graph nodes but preserves the graph structure and edge weights. The energy functional $E$ is defined in terms of graph operations (Laplacian, closure operator), hence is $\mathrm{Aut}(X_t)$-invariant. Since $\mathrm{Aut}_{task} \leq \mathrm{Aut}(X_t)$, gauge invariance holds. CONFIRMED for $\mathrm{Aut}_{task}$.

**Open.** For any non-trivial $G_{\mathrm{core\text{-}weight}}$ (if it exists), gauge-invariance of $P$ under its action must be checked explicitly. This is part of OP-OMS-001.

---

## AUDIT-008 — $\Delta^3$ is the Correct Minimal Moduli Space

**Date:** 2026-05-07  
**Decision:** CONFIRMED

**Claim.** Under the minimal assumptions (K=1, trivial $G$, $\xi$ fixed, strict criticality), the moduli space is $\mathfrak{M}_{\min} \cong \Delta^3$.

**Chain of reductions:**
1. Strict criticality: $q = q_c(X_t)$ eliminated. Remaining: $(\lambda, \xi)$.
2. $\xi$ fixed: $B_\xi$ reduced to a point. Remaining: $\lambda$.
3. $K = 1$: $S_K = \{e\}$, trivial $G$. Remaining: $\Delta^3 / \{e\} = \Delta^3$.

**No overclaim here.** The claim is specifically about the minimal case with all assumptions applied. For general $K$, non-trivial $G$, or free $\xi$, the moduli space is larger and more complex.

---

## AUDIT-009 — $b_D = 0$ Required; Not an Observer Choice

**Date:** 2026-05-07  
**Decision:** SCENE-DETERMINED (fixed)

**Statement.** The parameter $b_D = 0$ (distinction operator scale) is required for analyticity (Łojasiewicz convergence of the optimizer). It is NOT a free observer parameter.

**Classification.** $b_D$ belongs to the "fixed by theory" column in DEF-1, not to observer-controlled parameters. It should not appear in $\Theta = (q, \lambda, \xi)$.

**Files affected.** DEF-1 table in `definitions.md` marks $b_D = 0$ with note "fixed for analyticity (Łojasiewicz)."

---

## AUDIT-010 — Mass $m$ is Scene-Determined, Not Observer-Controlled

**Date:** 2026-05-07  
**Decision:** CONFIRMED

**Statement.** $m = \sum_i u_i$ (total mass, cohesion constraint) is set by the scene content, not by the observer. The observer cannot choose $m$.

**Justification.** The mass constraint arises from the SCC field axioms: $u_t \in \Sigma_m = \{u \in [0,1]^n : \sum u_i = m\}$ where $m$ is a scene-determined quantity (related to the "amount of perceptually active material" in the scene).

**Consequence.** $m$ does not appear in $\Theta_o = (q, \lambda, \xi)$.

---

---

## AUDIT-011 — $P_{\min}$ is Too Coarse: Prop R1 is Hypothesized, Not Proved

**Date:** 2026-05-07  
**Stage:** OMS-0.2 (readout map audit)  
**Decision:** HYPOTHESIZED (pending VP-1 computational confirmation)

**Statement.** $P_{\min}(\Theta) = d_\Theta = (\mathrm{Bind, Sep, Inside, Persist})$ is claimed to be informationally too coarse — two observers with identical diagnostic vectors can differ in topological signature (component count $K^*$, persistence diagram).

**Why this matters.** If true, the recommended readout $P_{\mathrm{top}}$ (which adds $T_\Theta$ to $d_\Theta$) is strictly necessary for perceptual discriminability. If false, $P_{\min}$ already discriminates all physically distinct observers.

**Evidence for.** Conceptual argument: closure-dominant vs. separation-dominant observers on a path graph may produce equal aggregate diagnostics (since Bind and Sep are u-weighted averages) but different component structures.

**Evidence against.** No computational counterexample has been run.

**Required.** VP-1 (P-resolution audit) must be executed to confirm or refute. Until then, Prop R1 remains HYPOTHESIZED and Warning R1 in `readout_map_audit.md` stays active.

**Files affected.** `readout_map_audit.md` Warning R1; `canonical_promotion_checklist.md` B8.

---

## AUDIT-012 — No Unique Canonical $V$: $\mathcal{V}_{\mathrm{adm}}$ is the Canonical Object at OMS-1.0

**Date:** 2026-05-07  
**Stage:** OMS-0.2 (observer landscape)  
**Decision:** CLASS DEFINITION (not unique V)

**Statement.** OMS-1.0 does NOT designate a unique canonical observer landscape $V : \mathcal{M}_{\mathrm{obs}} \to \mathbb{R}_{\geq 0}$. Instead, it defines the admissible class $\mathcal{V}_{\mathrm{adm}}$ by five criteria (V1–V5: continuity, Morse-like genericity, bounded below, SCC-derived, gauge-invariant).

**Why the class, not a unique V.** Different scientific contexts call for different $V$:
- Computational work: $V_D^0(\lambda) = \|d_\lambda - d^*\|^2$ (diagnostic loss)
- Theoretical work: $V_P$ (readout-induced)
- Empirical work: $V_{\mathrm{pop}}$ (population distribution)

Forcing a unique $V$ at this stage would be an overclaim not supported by existing proofs.

**Consequence.** Basin count, basin shapes, and perceptual type assignments are all $V$-dependent. Any claim of the form "there are exactly $N$ perceptual types" requires specifying $V$.

**Overclaim warning.** Do not write "OMS predicts $N$ observer types" without specifying $V \in \mathcal{V}_{\mathrm{adm}}$.

**Files affected.** `observer_landscape_candidates.md` §1–§7; `canonical_promotion_checklist.md` C9, D2.

---

## AUDIT-013 — Multiple Basins on Connected Space: No Contradiction

**Date:** 2026-05-07  
**Stage:** OMS-0.2 (basin stratification)  
**Decision:** CONFIRMED (apparent paradox resolved)

**Apparent tension.** $\mathfrak{M}$ is connected (Prop 6, proved). But OMS claims multiple perceptual types (attractor basins of $V$). How can a connected space have multiple basins?

**Resolution.** Connectedness says there is a path between any two points in $\mathfrak{M}$. It does NOT say that $V$ has a unique minimum. A smooth function on a connected manifold can have multiple local minima. Perceptual types are attractor basins of $V$, not connected components of $\mathfrak{M}$.

**Explicit construction.** $V(\lambda) = \lambda_{cl}^2(1 - \lambda_{cl})^2$ on $\Delta^3$: two local minima at $\lambda_{cl} = 0$ and $\lambda_{cl} = 1$, separated by a saddle at $\lambda_{cl} = 1/2$. Basin boundary = level set $\{V = V(\text{saddle})\}$ (codimension-1 hypersurface).

**Filed as.** Prop BS1 in `basin_stratification.md`.

**Files affected.** `basin_stratification.md` Prop BS1; `oms_1_candidate.md` §13.

---

## AUDIT-014 — $S_4$ Weight Permutation is Not a Gauge Symmetry

**Date:** 2026-05-07  
**Stage:** OMS-0.3 (core-weight symmetry)  
**Decision:** REJECTED

**Proposed candidate.** Full $S_4$ permutation on $(\lambda_{cl}, \lambda_{sep}, \lambda_{bd}, \lambda_{tr})$, treating all four energy weights as interchangeable.

**Reason for rejection.** The four energy terms $E_{cl}, E_{sep}, E_{bd}, E_{tr}$ have distinct functional forms:
- $E_{cl}$: resolvent-based compactness
- $E_{sep}$: distinction-weighted u-separation
- $E_{bd}$: boundary term via $\|Lu\|^2$
- $E_{tr}$: Sinkhorn OT transport cost

Swapping $\lambda_{cl} \leftrightarrow \lambda_{sep}$ generically changes the optimizer solution $u^*(\Theta)$ and hence $P_{\mathrm{top}}(\Theta)$. Therefore $\sigma \cdot \Theta \not\equiv \Theta$ under $P_{\mathrm{top}}$ for most $\sigma \in S_4$.

**Filed as.** Prop CW1 in `core_weight_symmetry.md`.

**Files affected.** `core_weight_symmetry.md` CW1; `canonical_promotion_checklist.md` B13.

---

## AUDIT-015 — No Continuous Vertex-Preserving Symmetry of $\Delta^3$

**Date:** 2026-05-07  
**Stage:** OMS-0.3 (latent symmetry)  
**Decision:** PROVED

**Claim.** No continuous group $G$ acts on $\Delta^3$ preserving all four vertices $\{e_0, e_1, e_2, e_3\}$.

**Proof sketch.** Any continuous group action preserving the four vertices fixes four points of $\Delta^3$. By the fixed-point property of simplices, if a topological group acts continuously on $\Delta^3$ fixing the vertices, every element of $G$ fixes the vertices and their convex combinations — hence fixes all of $\Delta^3$. So the action is trivial.

**Consequence.** There is no continuous compact group $G_{\mathrm{core\text{-}weight}}$ acting faithfully on $\Delta^3$ and preserving all four energy-weight extremes. Only discrete symmetries (permutations of vertices = $S_4$ subgroups) are possible, and $S_4$ itself is rejected by AUDIT-014.

**Filed as.** Prop LS1 in `latent_symmetry.md`.

**Files affected.** `latent_symmetry.md` Prop LS1; `canonical_promotion_checklist.md` B15.

---

## AUDIT-016 — RG Relevance Flow is a Program, Not a Theorem

**Date:** 2026-05-07  
**Stage:** OMS-0.4 (RG relevance flow)  
**Decision:** PROGRAM DECLARATION

**Statement.** The renormalization group (RG) relevance flow analysis for OMS — including the perceptual Jacobian $J_P(\Theta)$, singular value spectrum, effective dimension $d_{\mathrm{eff}}$, and coarse-graining map $\mathcal{C}_\varepsilon$ — is a research program, not a completed theorem.

**What is proved:** The definitions RG1–RG8 are formally consistent. The mandatory distinction between three dimension reduction mechanisms (normalization, gauge, RG) is proved to be conceptually necessary.

**What is hypothesized:** $d_{\mathrm{eff}}^{\mathrm{typical}}(0.05) \in [2, 4]$ (Hypothesis RG1). This requires VP-6 (Jacobian singular spectrum computation) to test.

**What is deferred:** Proving that the RG flow converges to a well-defined fixed point; relating the fixed point to universal perceptual classes.

**Filed as.** Warning RG1 in `rg_relevance_flow.md`.

**Files affected.** `rg_relevance_flow.md` §5 (warnings); `canonical_promotion_checklist.md` C10, B19.

---

## AUDIT-017 — Boundary Faces as Absorbing Walls (Prop SD1)

**Date:** 2026-05-07  
**Stage:** OMS-0.5 (stratified dynamics)  
**Decision:** PROVED (conditional on $V$ differentiability)

**Claim.** Under projected gradient flow $\dot{\lambda} = -\Pi_{T_\lambda \Delta^3} \nabla_\lambda V(\lambda)$ on $\Delta^3$, the boundary faces $\partial_I \Delta^3 = \{\lambda : \lambda_i = 0, i \in I\}$ are forward-invariant (absorbing walls).

**Proof.** At a face $\partial_I \Delta^3$, the simplex constraint forces $\lambda_i \geq 0$. The projected gradient satisfies $\dot{\lambda}_i \geq 0$ whenever $\lambda_i = 0$ (projection kills the inward-pointing component). Hence $\lambda_i(t) \geq 0$ is maintained — the flow cannot exit a face once it enters.

**Consequence.** An observer who has "turned off" an energy term (reached the face $\lambda_i = 0$) cannot spontaneously reactivate it under gradient flow alone. Reactivation requires an external perturbation or a non-gradient mechanism.

**Conditional on.** $V$ must be $C^1$ on $\Delta^3$ for the gradient to be defined at boundary faces. This is guaranteed if $V \in \mathcal{V}_{\mathrm{adm}}$ (criterion V1: continuity; criterion V2: Morse-like, requiring $C^2$ generically).

**Filed as.** Prop SD1 in `stratified_dynamics.md`.

**Files affected.** `stratified_dynamics.md` Prop SD1; `canonical_promotion_checklist.md` B12.

---

## AUDIT-018 — Latent Symmetry Framework Belongs to OMS-Gen, Not OMS Core

**Date:** 2026-05-07  
**Stage:** OMS-0.3 (latent symmetry)  
**Decision:** SCOPE CLASSIFICATION

**Statement.** The latent generator framework — defining a latent space $Z$ and generator $\Gamma : Z \to \Delta^3$ with a compact group $H$ acting on $Z$ such that $\Gamma \circ h = \Gamma$ — is a generalization extension of OMS, not part of OMS core.

**Reason.** OMS core is defined entirely in terms of the explicit parameter space $\Theta = (q, \lambda, \xi)$. The latent generator framework introduces an additional structure (the latent space $Z$) that is not required to state or prove the core OMS propositions.

**Classification.** Latent symmetry analysis is Prop LS3 (ASSUMED in OMS core): "if latent structure exists, it belongs to OMS-Gen." VP-5 (latent symmetry simulation) can explore this extension.

**Overclaim warning.** Do not claim that OMS has a latent continuous symmetry without specifying the generator $\Gamma$ and the group $H$ explicitly.

**Files affected.** `latent_symmetry.md` Prop LS3; `canonical_promotion_checklist.md` C12.

---

## AUDIT-019 — Transport Weight Invariance on Static Scenes (Prop CW2)

**Date:** 2026-05-07  
**Stage:** OMS-0.3 (core-weight symmetry)  
**Decision:** CONDITIONALLY PROVED

**Claim.** On static scenes ($X_{t+1} = X_t$), $P_{\min}(\Theta)$ is independent of $\lambda_{tr}$ (the transport weight).

**Proof sketch.** On static scenes, $E_{tr}$ measures the OT distance between $u_t$ and $u_{t+1}$, but since the scene is the same, the optimizer sets $u_{t+1} = u_t$ (or an equivalent solution), making $E_{tr} = 0$ regardless of $\lambda_{tr}$. Thus varying $\lambda_{tr}$ does not change the optimizer output $u^*$ or the diagnostic $d_\Theta$.

**Conditional on.** (1) The SCC optimizer is stable enough that the static-scene solution is unique (or the diagnostic is unique despite non-uniqueness of $u^*$). (2) The OT cost function satisfies $\mathrm{OT}(u, u) = 0$.

**Consequence.** The face $F_{tr} = \{\lambda_{tr} = 0\}$ of $\Delta^3$ produces the same $P_{\min}$ as any interior point on static scenes. Hence the static sub-theory is a valid reduction without loss of generality.

**Filed as.** Prop CW2 in `core_weight_symmetry.md`.

**Files affected.** `core_weight_symmetry.md` CW2; `integration_with_scc.md` §3.1.

---

## AUDIT-020 — Continuity of $u^*(\Theta)$ is an Unproved Assumption

**Date:** 2026-05-07  
**Stage:** OMS-0.7 (integration); OMS-1.0 (candidate)  
**Decision:** OPEN BLOCKER

**Statement.** The OMS construction requires that the optimizer output $u^*(\Theta, X_t)$ is continuous (or at least measurable) in $\Theta$. This is used to prove that $P_{\mathrm{top}}$ descends continuously to $\mathfrak{M}$ (Prop R3).

**Current status.** No proof exists in the SCC literature that $u^*(\Theta)$ is continuous in $\Theta$. The optimizer (semi-implicit projected gradient with BB step) converges to a local minimum, but the location of that minimum may jump discontinuously at parameter bifurcation points.

**Known regularity results in adjacent fields.** For strictly convex energies, the minimizer is unique and continuous in parameters (implicit function theorem). SCC energy $E$ is not globally convex, but may be strongly convex near local minima — regularity then holds locally.

**Impact.** Without continuity of $u^*$, the readout map $P_{\mathrm{top}}$ may not be continuous, and the descent to $\mathfrak{M}$ may not preserve topological structure.

**Required for promotion.** Either prove continuity of $u^*$ (or of $P_{\mathrm{top}}$ directly) by a regularity argument, or weaken the readout map claims to measurable (not continuous) readout.

**Filed as.** Part of OP-OMS-009 in `open_problems.md`.

**Files affected.** `readout_map_audit.md` Prop R3; `canonical_promotion_checklist.md` B7, B17.

---

## Summary of Overclaim Warnings

| Warning | Affected claim | Status |
|---|---|---|
| W1: $G_{\mathrm{core\text{-}weight}}$ is non-trivial | Any claim about full $G$ | Open (OP-OMS-001) |
| W2: Criticality hypothesis is a theorem | DEF-5 (M_obs^crit) | Mitigated (labeled "hypothesis") |
| W3: Finite $G$ reduces dimension | Any DOF claim | Mitigated (AUDIT-002) |
| W4: $\mathrm{Aut}_{task} = \mathrm{Aut}(X_t)$ | DEF-8 | Mitigated (task anchors explicit) |
| W5: Effective DOF = 1-3 is a theorem | Any DOF claim | Open (OP-OMS-005) |
| W6: $V(\Theta)$ is explicitly defined | Any basin claim | Open (OP-OMS-002) |
| W7: $P_{\min}$ coarseness is proved | Prop R1 | **CONFIRMED** (VP-1, exp86, 2026-05-07) |
| W8: Basin count is universal | Any "N types" claim | V-dependent (OP-OMS-002) |
| W9: Latent symmetry is a core OMS result | OMS-Gen claim | Scope-classified (AUDIT-018) |
| W10: RG flow is a theorem | $d_{\mathrm{eff}}$ claims | Program only (AUDIT-016) |
| W11: $u^*(\Theta)$ is continuous | Prop R3 descent | Open (OP-OMS-009 residual — resolution sub-question closed, continuity still open) |
| W12: $S_4$ weight permutation is a symmetry | Core weight claims | Rejected (AUDIT-014) |

---

## AUDIT-021 — VP-1 P-Resolution Audit: OP-OMS-009 Resolution

**Date:** 2026-05-07
**Decision:** OP-OMS-009 (readout resolution completeness) RESOLVED-NEGATIVE by explicit counterexample

**Context.** Protocol VP-1 was run to attack sub-question (a) of OP-OMS-009: is $P_{\min}$ strictly coarser than $P_{\mathrm{top}}$? Prop R1 in `readout_map_audit.md` hypothesized affirmatively but lacked computational evidence.

**Execution.** `exp86_vp1_p_resolution_audit.py` on 2026-05-07. Four complementary approaches (synthetic fields, optimizer sweep on 12×12, analytic construction on 10×10, dense $\lambda$ sweep on 15×15). Total: 4 definitive counterexamples (criterion: $\|d(\Theta_1) - d(\Theta_2)\| < 0.15$ AND $D_T > 0.5$).

**Key counterexample (CE-1).** $\lambda_A = (0.6, 0.2, 0.2)$ vs $\lambda_B = (0.5, 0.3, 0.2)$ on 12×12 grid. Diagnostic distance $\|d_A - d_B\| = 0.071$. Topology distance $D_T = 3.028$. $K_{\mathrm{core}}(\Theta_A) = 2$, $K_{\mathrm{core}}(\Theta_B) = 1$. P_min sees near-identical 4-vectors; $P_{\mathrm{top}}$ immediately distinguishes via $K_{\mathrm{core}}$.

**Mechanism.** Inside predicate $= (l_{\max} - c)/(1-c) \times (1 - l_{\mathrm{sec}}/l_{\max})$ collapses H0 bar information. A two-component field with one small satellite produces $l_{\mathrm{sec}} \approx 0$, giving Inside $\approx (l_{\max}-c)/(1-c)$ — the same as a one-component field with identical $l_{\max}$. Integer count $K_{\mathrm{core}}$ is lost.

**Proposition R1 update.** Upgraded from HYPOTHESIZED to PROVED (constructive proof by CE-1).

**OP-OMS-009 blocker removed.** The resolution sub-question (a) is closed. Residual sub-questions (b)–(d) (continuity of $u^*$, uniqueness, tie-breaking) remain open but are no longer canonical blockers.

**Remaining canonical blockers.** OP-OMS-001 (core-weight gauge group), OP-OMS-002 (admissible $V$ existence).

**Files affected.** `open_problems.md` OP-OMS-009; `readout_map_audit.md` Prop R1; `canonical_promotion_checklist.md` B7; `vp1_p_resolution_audit.md`, `vp1_counterexamples.md`, `vp1_results.md` (new); `CODE/experiments/results/observer_moduli/vp1_pairs.json`.
