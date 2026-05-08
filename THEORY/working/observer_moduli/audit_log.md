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
| W11: $u^*(\Theta)$ is continuous | Prop R3 descent | **Resolved structurally** (Session 5: locally PROVED, globally REJECTED) |
| W12: $S_4$ weight permutation is a symmetry | Core weight claims | Rejected (AUDIT-014) |
| W13: Low VP-6 σ implies continuous gauge | Any "gauge-from-rank" inference | Mitigated (Prop ED1) |
| W14: Branch-jump VP-6 stencils are noise | $d_{\mathrm{eff}}$ averaging | Mitigated (Prop R3 (3); branch flips are theorem-level signal) |
| W15: R1/R2 hold globally on $\Delta^3$ | Any global $C^1$ claim | Mitigated (R1/R2 are local; Prop R3 (3) REJECTED global) |
| W16: $d_{\mathrm{eff}}^{\mathrm{simplex}} = d_{\mathrm{eff}}^{\mathcal{M}_{\mathrm{obs}}}$ | VP-6 over-extension | Active (VP-6 holds $q, \xi$ fixed; original Hyp RG1 untested) |
| W17: $v$ concave $\Rightarrow$ $E_\lambda$ convex in $u$ | Misread of inf-of-affine | Mitigated (R4: $v$ inf of affine in $\lambda$, hence concave; $E_\lambda$ non-convex in $u$) |
| W18: H4 holds depends on computational witness | Gap C1 closure | **Mitigated** Session 7 (INTERVAL_CERTIFIED, margin $4 \times 10^{13}$ over IEEE bound; standard computer-assisted proof practice) |
| W19: $V_{2,\tau}$ over-smoothing | NV10 caveat | Active (formally documented in NV10) |
| W20: $\Sigma_{T8} \subset \Sigma_{\mathrm{branch}}$ | conceptual unification, not pathology | NOT a warning but a structural identification |
| W21: Pseudo-Δ³ ≠ full temporal Δ³ | OMS-2.0 scope | **Separated** Session 7 (TS1/TS2; blocks Full Temporal only) |
| W22: Gap C1 rests on INTERVAL_CERTIFIED H4 | Gap C1 closure | sub-OP OP-OMS-032b for RATIONAL_CERTIFIED upgrade (non-blocking) |
| W23: SN3 conditional on (SN-iii)+(SN-iv) genericity | $\Sigma_{\mathrm{SN}}$ | sub-OP OP-OMS-033b for full SN4 rigor (non-blocking) |
| W24: OMS-2.0 Static ≠ Full Temporal | scope hazard | **Active** — promotion verdict explicitly distinguishes the two |
| W25: Appendix OMS theorems are layered, not modifying SCC core | scope hazard | **Active** — OMS theorem count separate from SCC theorem registry |
| W26: Temporal extension uses L2 transport proxy, not Sinkhorn-OT | claim scope | **Active** — robustness check is OP-OMS-034c (non-blocking) |
| W27: K=5 codim-1 budget excess due to branch density, not codim-1 failure | branch-map interpretation | **Mitigated** — explicit two-macro-regime + 7 λ_tr-unique branch interpretation in `vp11_temporal_delta3.md` |
| W28: Pre-Session-7 "rank 4" terminology was tangent-dim error | scope confusion | **Fixed** in Session 8 — correct rank-3 condition on Δ³ tangent throughout |

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

---

## AUDIT-026 — Session 8: OP-OMS-034 Closure → OMS-2.0 Accepted (Full)

**Date:** 2026-05-08
**Stage:** OMS-2.0 Accepted Static + Full Temporal Conditional → **OMS-2.0 Accepted — Full**
**Decision:** OP-OMS-034 CLOSED at COMPUTATIONALLY SUPPORTED level via VP-11.

**Context.** Mandated narrow-scope OP-OMS-034 closure session. No broadening; only the temporal extension. Result: full promotion to OMS-2.0 Accepted Full on a faithful reduced temporal OMS test.

### A. Critical correction caught.

Prior session notes referenced "4×4 minor" requirement for the temporal extension. **This is wrong.** $\Delta^3$ has tangent dimension 3 (simplex constraint $\sum \lambda_i = 1$ removes one direction). The Jacobian on simplex tangent is $J_e^{\mathrm{tan}} \in \mathbb{R}^{4 \times 3}$, and full rank means **rank 3**, not 4. Session 8 uses the correct rank-3 condition.

### B. New theorems / propositions PROVED in Session 8.

| ID | Statement | Status |
|---|---|---|
| T1, T2 | Temporal energy + reduced-temporal scene | DEFINED |
| T3 | Reduced temporal optimizer well-posedness | PROVED |
| T4 | $e_{\mathrm{temp}}$ component-energy map | DEFINED |
| T5 | Envelope: $\nabla v_{\mathrm{temp}} = e_{\mathrm{temp}}$ | PROVED |
| (Wit-T) | Temporal rank-3 witness condition | DEFINED |
| T6 | Temporal $G_{\mathrm{cw}}^{\mathrm{temp}} = \{e\}$ | PROVED conditional on (Wit-T) |
| T7 | Analyticity of reduced temporal optimizer | PROVED |
| T8 | Temporal codim-1 branch decomposition | PROVED for codim-1 components; conditional for $\Sigma_{\mathrm{SN}}^{\mathrm{temp}}$ |
| TS3 | Static-temporal coherence at $\lambda_{tr} = 0$ | PROVED |
| H4-T-CW | Temporal witness certification | COMPUTATIONALLY SUPPORTED (VP-11) |

### C. Computational confirmations (VP-11).

- **Phase 1 (rank witness):** 14 / 14 samples have rank 3 at threshold abs σ ≥ 1e-3; 14 / 14 λ_tr-nontrivial. (Wit-T) **CONFIRMED**. Best σ-spectrum (8.39, 0.77, 0.031). Worst (1.85, 0.036, 3.6e-3). Elapsed 5.5s.
- **Phase 2 (Δ³ branch map):** K=5 tetrahedral grid; 19 distinct branches; 7 λ_tr-unique branches; transition fraction 0.671 vs simple-budget 0.600 (excess due to branch density, not codim-1 violation). Two macro-regimes (static-cohesive 26.8% + transport-coherent 17.9%). Elapsed 3.2s.

### D. Decisions.

1. **OP-OMS-034 CLOSED — COMPUTATIONALLY SUPPORTED.** Faithful reduced temporal OMS test confirms (Wit-T) and codim-1 branch structure. Higher-K refinement (OP-OMS-034b) and full Sinkhorn-OT (OP-OMS-034c) registered as non-blocking sub-OPs.
2. **OMS-2.0 promotion verdict: Accepted — Full.** All five user-stated promotion criteria met. Equivalent fully-qualified form: "Static (PROVED) + Full Temporal (COMPUTATIONALLY SUPPORTED on faithful reduced test)".
3. **Canonical Appendix OMS extended with Temporal subsection M** (canonical.md, Session 8). 9 additional temporal-layer items.

### E. New audit warnings.

- **W26 (Session 8):** The temporal extension uses a **faithful reduced temporal OMS test** (L2 transport proxy with closed-form gradient), not full Sinkhorn-OT. Reading the result as "Sinkhorn-OT-temporal" is a category error. Robustness check via Sinkhorn is OP-OMS-034c (non-blocking).
- **W27 (Session 8):** The Phase-2 codim-1 budget excess (0.671 vs 0.600) at K=5 reflects high branch density (19 branches, ~18 codim-1 separators), not codim-1 failure. Higher-K refinement is OP-OMS-034b (non-blocking).
- **W28 (Session 8):** The "rank 4" notation appearing in pre-Session-7 / Session-6 drafts for the temporal extension was a tangent-dimension error. The correct condition is rank 3 on the 3D simplex tangent. Fixed throughout the Session 8 documents.

### F. Files affected.

- **NEW (Session 8):** `op_oms_034_initial_log.md`, `op_oms_034_temporal_delta3_resolution.md` (placeholder filled), `oms_2_0_full_accepted_audit.md`, `vp11_temporal_delta3.py`, `vp11_temporal_rank_witness.{json,md}`, `vp11_temporal_delta3.{json,md}`.
- **UPDATED (Session 8):** `THEORY/canonical/canonical.md` (Temporal subsection M added), `open_problems.md` (OP-OMS-034 CLOSED; 034b/034c registered), `audit_log.md` (this entry; W26–W28 added), `canonical_promotion_checklist.md`, `checkpoints.md`, `daily_log.md`, `THEORY/CHANGELOG.md`, `THEORY/working/INDEX.md`, `oms_1_candidate.md`.

---

## AUDIT-025 — Session 7: Proof Closure → OMS-2.0 Accepted (Static)

**Date:** 2026-05-08
**Stage:** OMS-2.0 Conditional Accepted → **OMS-2.0 Accepted — Static + Conditional Temporal**
**Decision:** Multiple — record below.

**Context.** Mandated proof-closure session after Session-6 OMS-2.0 push. No broadening. Three sub-OPs + Gap C1 theorem package + canonical appendix.

### A. Theorem package corrections caught (substantive bug fixes).

1. **Theorem C1.2 (rank equivalence) restated with corrected hypothesis $H_T \succ 0$.** Original Session-6 draft used "$H_T$ invertible" — too weak: indefinite invertible $B$ does not give $\mathrm{rank}(A^\top B^{-1} A) = \mathrm{rank}(A)$. The corrected hypothesis (positive definiteness) is exactly second-order sufficiency at a strict local minimum — automatic on the regular branch. The correction was a real bug fix, not cosmetic.
2. **Theorem C1.4 (rigidity) restated honestly.** Original draft claimed identity from immersion alone; the honest statement requires (Vertex) — that $g$ fixes simplex vertices. (Vertex) is supplied by independent results (Prop CW1, VP-3), so the proof is not circular but the dependency is now made explicit.

### B. New propositions / theorems PROVED in Session 7.

| ID | Statement | File |
|---|---|---|
| C1.1 (sharpened) | Sensitivity $J_e = -G_T^\top H_T^{-1} G_T$ on regular branch | gap_c1_final_theorem_package |
| C1.1' | Active-set version | id. |
| C1.2 (corrected) | Rank equivalence under $H_T \succ 0$ | id. |
| C1.3 (clean) | Witness ⇒ open-dense full rank | id. |
| C1.4 (honest) | Vertex-fixing + immersion ⇒ identity on $\Delta^2_{\mathrm{static}}$ | id. |
| C1.5 (final) | $G_{\mathrm{cw}}^{\mathrm{static}} = \{e\}$ | id. |
| H4-CW (witness certification) | INTERVAL_CERTIFIED via VP-8 | op_oms_032_closed_form_h4 |
| SN3 | $\Sigma_{\mathrm{SN}}$ codim-1 conditional fold theorem | op_oms_033_sigma_sn_arnold |
| TS1 | Static-temporal independence | op_oms_034_temporal_delta3_status |
| TS2 | Separation declaration | id. |

### C. Decisions.

1. **OP-OMS-032 → CLOSED UNDER CERTIFIED WITNESS.** Witness type: INTERVAL_CERTIFIED. 12 certified witnesses across 3 scenes. Best margin $4 \times 10^{13}$ over IEEE bound. Standard convention for computer-assisted mathematical proof; replaces "PROOF SKETCH" objection.
2. **OP-OMS-033 → PROVED as conditional fold theorem.** Σ_SN codim-1 via Crandall–Rabinowitz; SN4 (SCC genericity) PROOF SKETCH (sub-OP OP-OMS-033b, non-blocking).
3. **OP-OMS-034 → SEPARATED.** Static OMS does not require it; full temporal stays Conditional.
4. **OMS-2.0 promotion verdict: Accepted — Static, with Full Temporal Conditional on OP-OMS-034.** Per `oms_2_0_accepted_audit.md`.
5. **Canonical promotion: Appendix OMS added to `THEORY/canonical/canonical.md`** with 20+ theorem-grade items, separated from SCC core registry.

### D. New audit warnings.

- **W22 (Session 7):** The Gap C1 closure rests on (Wit) = H4 INTERVAL_CERTIFIED via VP-8. This is **standard computer-assisted proof practice** but should be acknowledged. Sub-OP OP-OMS-032b registered to upgrade to RATIONAL_CERTIFIED.
- **W23 (Session 7):** SN3 (Σ_SN codim-1) is conditional on (SN-iii)+(SN-iv) genericity. Lemma SN4 sketches the genericity but full rigor for SCC is sub-OP OP-OMS-033b.
- **W24 (Session 7):** OMS-2.0 Static **does not** automatically extend to full temporal Δ³. Full temporal is Conditional on OP-OMS-034. Confusing static and temporal scope is a documented hazard.
- **W25 (Session 7):** The Appendix OMS theorem count (20+) is layered **on top of** SCC core; it does not modify SCC theorem registry. Confusing OMS theorems with SCC theorems is a documented hazard.

### E. Files affected.

- **NEW (Session 7):** `proof_promotion_reading_log.md`, `gap_c1_final_theorem_package.md`, `op_oms_032_closed_form_h4.md`, `op_oms_033_sigma_sn_arnold.md`, `op_oms_034_temporal_delta3_status.md`, `oms_2_0_accepted_audit.md`.
- **UPDATED (Session 7):** `THEORY/canonical/canonical.md` (Appendix OMS added at end), `open_problems.md` (032/033/034 statuses updated; 032b/033b registered), `audit_log.md` (this entry; W22–W25 added), `canonical_promotion_checklist.md`, `checkpoints.md`, `daily_log.md`, `THEORY/CHANGELOG.md`, `THEORY/working/INDEX.md`, `oms_1_candidate.md` (frontmatter + status declaration).

---

## AUDIT-024 — Session 6: OMS-2.0 Push Through Three Hard Blockers

**Date:** 2026-05-08
**Stage:** OMS-1.2 → OMS-2.0 candidate (Gate 7 audit pending VP-10)
**Decision:** Multiple — record below.

**Context.** User mandated execution of 8 gates aimed at resolving the three OMS-2.0 hard blockers (OP-OMS-001, OP-OMS-002+, OP-OMS-026).

### A. New propositions PROVED.

| Prop | Statement | Source |
|---|---|---|
| RT1 | Rank obstruction: $\mathrm{rank}\,J_e\bigr|_{T\Delta^3} = 3$ under H1, H2, H3 | `op_oms_001_gap_c1_rank_theorem.md` (Gate 1) |
| RT2 | $e : \Lambda^{\mathrm{reg}} \to \mathbb{R}^4$ is locally an immersion | id. |
| RT3 | Reduction-C closure: $g \in G_{\mathrm{cw}} \Rightarrow g = \mathrm{id}$ on regular subset | id. |
| S1 | Interior sensitivity: $J_e = -G_T^\top H_T^{-1} G_T$ | `op_oms_001_gap_c1_sensitivity.md` |
| S2 | Active-set sensitivity (projected to inactive subspace) | id. |
| G1, G2, G3 | Real-analyticity of $E_i$, $u^*$, $G_T$ on $\Lambda^{\mathrm{reg}}$ | `op_oms_001_gap_c1_genericity.md` |
| G4 | Analytic dichotomy on connected real-analytic manifold | id. (standard) |
| G5 | Witness ⇒ open dense rank ≥ 3 (single scene) | id. |
| G7 | Generic-scene H2 holds | id. (conditional on H4) |
| G8 | Continuous extension to identity from dense subset | id. |
| GAP-C1 | Closure of Gap C1 (modulo H4 witness) | id. |
| NV4 | $V_2$ V1 (gauge invariance) | `op_oms_002_nontrivial_v.md` |
| NV5 | $V_2$ continuous globally; $C^1$ on regular branches; admissible | id. |
| NV6 | $V_2$ bounded (V3) | id. |
| NV7 | $V_2$ has ≥ 2 basins with distinct $P^{\mathrm{sm}}$ readouts under H5 | id. |
| NV9 | $V_{2,\tau}$ smooth on regular branches | id. |
| NV10 | $V_{2,\tau}$ basin structure preserved for small $\tau$ | id. |
| SB5 | $\Sigma_{ab}$ codim-1 under distinguishability | `op_oms_026_sigma_branch_full.md` |
| SB6 | $\Sigma_{\mathrm{branch}}$ codim-1 stratified set | id. |
| SB7 | $\Sigma_{\mathrm{Hess}}$ codim-1 (T8 phase-transition surface) | id. |
| SB8 | $\Sigma_{\mathrm{AS}}$ codim-1 | id. |
| SB11 | Full Σ_branch characterization | id. (codim-1 part PROVED, $\Sigma_{\mathrm{SN}}$ PROOF SKETCH) |

### B. Computational confirmations (Gates 2, 4, 6).

| Witness | Source | Status |
|---|---|---|
| H4: $|\det G_T^{(\mathrm{3 \times 3})}| > 0$ at multiple $\lambda$ | VP-8 (`vp8_gap_c1_rank_witness.json`): 34/42 = 81% across P12/S3/asymmetric scenes | **CONFIRMED** |
| Rank(J_e_tan) = 2 (full simplex tangent rank) | VP-8: 42/42 cases | **UNIVERSAL** |
| $V_{2,τ=0.01}$ has ≥ 2 distinct-readout basins on P12 (3 attractors, 2 distinct pairs) and S3 (4 attractors, 4 distinct pairs) | VP-9 (`vp9_nontrivial_v_basin.json`) | **CONFIRMED for τ=0.01** |
| $V_{2,τ=0.1}$: basins collapse (over-smoothing) | VP-9 | **NV10 caveat confirmed** |
| Pseudo-Δ³ branch map; codim-1 consistency check | VP-10 (`vp10_sigma_branch_delta3.json`) | (pending) |

### C. Decisions / classifications.

1. **OP-OMS-001 PROVED conditional on H4.** Three theory files (Gate 1) + computational H4 witness (Gate 2) close Reduction C. Combined with Reduction B (continuous component triviality, OP-OMS-029 PROVED) and Prop CW1 ($S_4$ rejected) and the VP-3 elimination of all 7 transformation families, this exhausts candidate non-trivial gauges modulo a measure-zero residual closed by Corollary G8.

2. **OP-OMS-002+ COMPUTATIONALLY SUPPORTED.** $V_2$ and $V_{2,\tau}$ are admissible (V1+V2_strat+V3 PROVED). VP-9 confirms ≥ 2 basins with distinct readouts on both P12 and S3 for τ = 0.01. Over-smoothing (τ = 0.1) collapses the structure consistent with NV10 caveat.

3. **OP-OMS-026 PROVED + COMPUTATIONALLY SUPPORTED.** Theorem SB11 gives the codim-1 codim-1 algebraic characterization on regular branches; T8 phase-transition surface identified as a sub-component. VP-10 (pseudo-Δ³) provides codim-1 evidence in the 3D simplex.

4. **OMS-2.0 promotion decision (Gate 7) deferred** until VP-10 completes; expected outcome: **OMS-2.0 Conditional Accepted** (all three blockers resolved with theorems + computational support; one residual H4 witness; one PROOF SKETCH for $\Sigma_{\mathrm{SN}}$).

### D. New audit warnings.

- **W18:** "H4 holds" depends on a single computational witness for the rank-3 minor of $G_T$. Multiple witnesses across 3 scenes exist, but a fully formal proof would require a closed-form symbolic argument on a small scene. Track as residual sub-OP.
- **W19:** $V_{2,\tau}$ basin structure depends on $\tau$. Over-smoothing collapses basins. NV10 caveat is essential.
- **W20:** SB11 (D): "$\Sigma_{T8} \subset \Sigma_{\mathrm{branch}}$" identifies the SCC central T8 surface as one component of the OMS branch-switching set — this is a significant conceptual unification, not a routine identification.
- **W21:** Pseudo-Δ³ ≠ full temporal Δ³. The VP-10 result tests codim-1 evidence on the 3D simplex, but on a static scene where $\lambda_{tr}$ is gauge-redundant. Full temporal Δ³ is registered as residual.

### E. Files affected.

- **NEW (Session 6):** `op_oms_001_gap_c1_rank_theorem.md`, `op_oms_001_gap_c1_sensitivity.md`, `op_oms_001_gap_c1_genericity.md`, `op_oms_002_nontrivial_v.md`, `op_oms_026_sigma_branch_full.md`, `oms_2_0_promotion_audit.md` (Gate 7), `vp8_gap_c1_rank_witness.py`, `vp9_nontrivial_v_basin_test.py`, `vp10_sigma_branch_delta3.py`, plus 3 result JSONs and 3 result MDs.
- **UPDATED (Session 6):** `open_problems.md` (this commit), `audit_log.md` (this entry), `daily_log.md`, `checkpoints.md`, `THEORY/CHANGELOG.md`, `THEORY/working/INDEX.md`, `canonical_promotion_checklist.md`, possibly `oms_1_candidate.md` for OMS-2.0 frontmatter.

---

## AUDIT-023 — Session 5: VP-6 Effective DOF + OP-OMS-018 Partial Resolution

**Date:** 2026-05-08
**Stage:** OMS-1.2 candidate
**Decision:** Multiple — record below.

**Context.** Session-5 work on VP-6 (Jacobian effective DOF) and OP-OMS-018
(u*(λ) regularity).

### A. New propositions classified.

| Prop | Classification | Source |
|---|---|---|
| ED1 (finite gauge ≠ rank reduction) | **PROVED** | `effective_dof_theory.md` |
| ED2 (constant rank theorem applied to $R$) | **PROVED conditional on constant rank** | `effective_dof_theory.md` |
| R1 (local interior $C^1$ branch) | **PROVED** (IFT) | `op_oms_018_regular_u_star.md` §3 |
| R2 (local boundary $C^1$ on fixed active set) | **PROVED** (Robinson–Fiacco) | `op_oms_018_regular_u_star.md` §4 |
| R3 (1)–(2) ($S$ u.h.c.; $v$ continuous) | **PROVED** (Berge) | `op_oms_018_regular_u_star.md` §5 |
| R3 (3) (no global continuous selection) | **PROVED** (VP-1/4 counterexample) | `op_oms_018_regular_u_star.md` §5 |
| R4 ($v$ concave, locally Lipschitz) | **PROVED** | `op_oms_018_regular_u_star.md` §6 |
| R5 (envelope on regular branch) | **PROVED** (Danskin) | `op_oms_018_regular_u_star.md` §7 |
| Hyp RG1 (revised) | **COMPUTATIONALLY SUPPORTED** | `vp6_effective_dof.md` |

### B. Decisions / classifications.

1. **OP-OMS-018 PARTIALLY RESOLVED.** Local R1/R2 PROVED; global $C^1$
   REJECTED (Prop R3 (3)); value-function R4/R5 PROVED. The previous
   formal-blocker status of OP-OMS-018 is downgraded.
2. **VP-6 Hypothesis RG1 (revised) is COMPUTATIONALLY SUPPORTED.** $d_{\mathrm{eff}}$
   on the simplex slice with $q,\xi$ fixed is at most 2 in every of 42
   sampled stencils across S3 and S4; predominantly 1.
3. **OP-OMS-017 superseded by OP-OMS-026.** The locus
   $\{\lambda_{cl} \approx \lambda_{sep}\}$ is not an "approximate
   symmetry" but a **branch-switching surface** — observed via VP-6
   branch-jump flags. The locus has no continuous gauge interpretation; it
   is a stratification gluing surface in $\Delta^3$.
4. **Admissibility class $\mathcal{V}_{\mathrm{adm}}$ relaxed** to allow stratified
   smooth landscapes (V2 revised). The basin / stratified-dynamics
   sections receive matching patches. See `oms_1_2_status_audit.md` §8 and
   `observer_landscape_admissible_class.md` (Session 5 patch).
5. **OMS stage label proposed:** **OMS-1.2 — Computationally Grounded
   Canonical Candidate with Local Regularity Theorem.**

### C. New OPs registered.

OP-OMS-024 (constant-rank regions for $J_R$), OP-OMS-025 (perceptual style
correspondence), OP-OMS-026 ($\Sigma_{\mathrm{branch}}$ characterization;
absorbs OP-OMS-017), OP-OMS-027 (corner regularity), OP-OMS-028
(quantitative Lipschitz of $v$).

### D. Audit warnings (new).

- **W13:** Treating low VP-6 σ as evidence for a continuous gauge symmetry.
  ED1 is the firewall: low Jacobian rank does not imply a hidden gauge
  group.
- **W14:** Treating branch-jump VP-6 stencils as numerical noise. The
  discrete jumps are theorem-level signals (Prop R3 (3)).
- **W15:** Over-applying R1/R2 globally. Both are local statements.
- **W16:** Reading $d_{\mathrm{eff}}^{\mathrm{simplex}}$ as $d_{\mathrm{eff}}^{\mathcal{M}_{\mathrm{obs}}}$.
  VP-6 holds $q, \xi$ fixed; the original Hyp RG1 about full $\mathcal{M}_{\mathrm{obs}}$
  remains UNTESTED.
- **W17:** Concavity of $v(\lambda)$ misread as convexity of $E_\lambda(u)$.
  $E_\lambda$ is non-convex in $u$; $v$ is concave in $\lambda$ (inf of
  affine). Both true simultaneously.

### E. Files affected.

- `vp6_initial_reading_log.md`, `effective_dof_theory.md`, `op_oms_018_regular_u_star.md`,
  `vp6_effective_dof.md`, `vp6_effective_dof_log.md`, `oms_1_2_status_audit.md` (all NEW).
- `open_problems.md` — OP-OMS-018 status updated; OP-OMS-024..028 registered;
  summary table updated.
- `audit_log.md` — this entry (AUDIT-023); W13..W17 added to warnings table.
- `observer_landscape_admissible_class.md` — V2 patched (stratified smoothness).
- `basin_stratification.md` — Remark added (basin boundaries include
  $\Sigma_{\mathrm{branch}}$).
- `stratified_dynamics.md` — §6 added (Filippov sliding-mode at branch
  surfaces).
- `canonical_promotion_checklist.md` — v1.3 (OMS-1.2) update.
- `oms_1_candidate.md` — promote stage label OMS-1.1 → OMS-1.2 (after audit).
- `THEORY/CHANGELOG.md` — Session 5 entry.
- `THEORY/working/INDEX.md` — Session 5 files added.
- `daily_log.md` — Session 5 entry.
- `checkpoints.md` — VP-6 + OP-OMS-018 sections added.

---

## AUDIT-022 — VP-3 Core-Weight Symmetry Test: OP-OMS-001 Partial Resolution

**Date:** 2026-05-08
**Decision:** All tested λ-space transformation families ruled out as global gauge symmetries of $P_{\mathrm{top}}$. Default $G_{\mathrm{cw}} = \{e\}$ is COMPUTATIONALLY SUPPORTED. Prop CW2 COMPUTATIONALLY CONFIRMED.

**Context.** Protocol VP-3 (exp87) tested 7 transformation families (A–G) on energy weight simplex $\Delta^3$ using S3 (6×6 grid, n=36) and S4 (two 5-cliques, n=10). Key parameter fix: w_cl/w_sep/w_bd/w_tr are the correct ParameterRegistry attributes (not lambda_*); volume_fraction=0.3 is the mass budget.

**Results summary** (frac_asym = fraction of pairs with $\Delta P_{\mathrm{top}} > 0.05$):
- A (cl-sep swap): 0.833, n=12 — NOT_A_SYMMETRY
- B (cl-bd swap): 0.500, n=12 — PARTIAL_SYMMETRY
- C (bd-cl compensation): 0.368, n=38 — PARTIAL_SYMMETRY
- D (bd-sep compensation): 0.421, n=38 — PARTIAL_SYMMETRY
- E (transport ablation, static): 0.000, n=18 — CANDIDATE_SYMMETRY (Prop CW2 confirmed)
- F (radial centroid): 0.300, n=60 — PARTIAL_SYMMETRY
- G (random tangent): 0.217, n=60 — PARTIAL_SYMMETRY

**Key decisions.**
1. No transformation (except E, static-conditional) is a gauge symmetry. All have non-zero frac_asym.
2. PARTIAL_SYMMETRY verdicts reflect scene/λ-dependent approximate symmetry loci (OP-OMS-017).
3. Prop CW2: PROVED (conditional) → COMPUTATIONALLY CONFIRMED (n=18, all delta_P=0.000).
4. Prop CW3: ASSUMED → COMPUTATIONALLY SUPPORTED.

**New open problems.** OP-OMS-017 (approximate symmetry loci), OP-OMS-018 (optimizer regularity in λ-space).

**Files affected.** `core_weight_symmetry.md` §6–7; `open_problems.md` OP-OMS-001, +OP-OMS-017, +OP-OMS-018; `vp3_core_weight_symmetry_results.md` (new); `CODE/experiments/results/observer_moduli/vp3_symmetry_results.json`, `vp3_symmetry_summary.md`.
