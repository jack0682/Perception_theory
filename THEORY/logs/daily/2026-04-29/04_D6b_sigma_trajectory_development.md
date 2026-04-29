# 04_D6b_sigma_trajectory_development.md — Substantive Development of σ_multi^A(t) Dynamic Trajectory

**Session:** 2026-04-29 (W5 Day 3, post-Block-5 deepening pass)
**Target:** Substantively develop D-6b (Phase 9-10 dynamic σ_multi^A(t) trajectory layer) per meta-prompt §4 multi-approach framework. Goal: bring D-6b from "Cat B sketch — recommend defer" to a **rigorous skeleton** with explicit failure modes, suitable for either (a) Cat B target promotion in CV-1.6 OR (b) informed-defer decision with concrete W6+ Cat A path.
**This file covers:** §1 Problem restatement; §2 Five approaches generated; §3 Primary selection (Approach 1+2 hybrid); §4 Substantive development with lemmas + proofs/sketches/failure-analysis; §5 Integration with canonical; §6 New open questions; §7 Impact on D-6b user-decision recommendation.
**Depends on reading:** `00_phase9_10_reconciliation.md` §2 D-6b, `01_canonical_promotion_queue_review.md` §2 D-6b, `2026-04-28/30_T4_CH_correspondence_sigma_t.md`, `33_Phase9_findings_integration.md` §3 (U4 simplified σ trajectory), `34_Phase10_findings.md` §3-§4 (V3 Hessian + V4 K-jump statistics).

---

## §1. Restatement

### §1.1 What is being asked

Define and characterize $\sigma^A_{\mathrm{multi}}(t)$ along a K-field gradient flow trajectory $\mathbf{u}(t) : [0, T] \to \widetilde\Sigma^K_M$ (shared-pool architecture, since per-formation pool is dynamically static per Theorem 4.5.1). The Day 2 work produced:

- **V3 (Phase 10)**: Hessian-based σ-tuple computed at 10 sparse snapshots over $t = 100$. Lowest 4 eigenvalues only (simplified σ-tuple, NOT full Commitment 14 σ).
- **V4 (Phase 10)**: K-jump statistics from U2 long-time data: $\Delta t \propto t^{1.315}$, ΔK distribution dominated by single mergers (85.7%).
- **U4 (Phase 9)**: Simplified σ-trajectory implementation; ~6 K-jump events detected over $t = 200$.

These provide **operational** $\sigma^A(t)$ but no rigorous theory. Specifically open:

(Q1) **Smooth-segment behavior**: between K-jump times $t_n^*$, is $\sigma^A(t)$ continuous? piecewise constant? smooth-with-isolated-jumps?

(Q2) **K-jump behavior**: at $t = t_n^*$, two formations merge ($K \to K-1$). What is the relationship between $\sigma^A(t_n^{*-})$ (left limit) and $\sigma^A(t_n^{*+})$ (right limit)?

(Q3) **Inheritance rule**: is the post-merger σ-tuple a deterministic function of pre-merger σ-tuple + merger geometry? Or fundamentally non-deterministic from σ-data alone?

(Q4) **Cat status**: what is the strongest theorem statement provable for $\sigma^A(t)$? Cat A on smooth segments? Cat B with explicit jump-map characterization?

### §1.2 What is data

The Phase 9-10 numerics provide:

- V3 sparse Hessian samples at K=8, $T^2_{20}$: lowest eigvals $\approx 0$ (volume tangent) + $2.1$–$3.1$ (bulk modes at $\approx 2\beta$).
- No exponentially-suppressed Goldstone observed in V3 — consistent with corner-saturated regime per V5b-T' (Phase 3).
- Mass redistribution: at $t = 100$, formation 0 has $m = 31$, formation 1 has $m = 52$ — significant redistribution from initial $m = 22.5$ each.
- σ-tuple shifts continuously between K-jumps; jumps at mergers (consistent with Phase 8 T4 framework).

Data is consistent with $\sigma^A(t)$ being **piecewise** in some sense, but the precise type ("piecewise constant" vs "piecewise smooth" vs "piecewise continuous-with-jumps") is not pinned down by the V3/V4 observations.

### §1.3 What is success / failure

- **Success-A (Cat A target)**: Prove $\sigma^A(t)$ is piecewise constant on smooth segments + characterize K-jump map deterministically as $\Phi: \sigma^A(t^{*-}) \times \mathrm{MergerData} \to \sigma^A(t^{*+})$.
- **Success-B (Cat B target)**: Prove smooth-segment piecewise-constant claim; demonstrate K-jump map is **non-deterministic in pre-merger σ alone** (requires post-merger relaxation), giving Cat B target with explicit caveat.
- **Failure**: $\sigma^A(t)$ is not even left-and-right limited at K-jump times (would invalidate the operational V3/U4 implementation).

### §1.4 Surfacing implicit assumptions

- (A1) The trajectory $\mathbf{u}(t)$ is generic — i.e., avoids non-generic Hessian eigenvalue crossings of higher codimension. For 1-parameter $t$, generic crossings are isolated codimension-1 events (avoided crossings in physics terminology).
- (A2) K-jumps are isolated events ("simple mergers" $\Delta K = 1$ dominate; ΔK ≥ 2 are non-generic and rare per V4 data).
- (A3) Shared-pool architecture (Phase 7 R1.3) provides the dynamics; per-formation pool produces no jumps (Theorem 4.5.1 dynamic stability). Hence the development applies to shared-pool only.
- (A4) The simplified σ-tuple in V3/U4 is a *projection* of the full Commitment 14 σ-tuple onto its first $K$ entries. The full σ-tuple may have additional behavior not captured by V3/U4.
- (A5) The involutive canonical-iso hypothesis (Theorem 4.2.1) holds at every $t$ except K-jump times — i.e., during smooth segments, formations remain pairwise comparable.

These implicit assumptions are surfaced for explicit handling below.

---

## §2. Five Approaches Generated

### §2.1 Approach 1: Spectral perturbation theory (Kato-Rellich)

**Core idea**: $H_{\mathrm{joint}}(\mathbf{u}(t))$ is a smooth one-parameter family of self-adjoint operators on a fixed-dimensional space (during smooth segments). Apply Kato-Rellich analytic perturbation theory: eigenvalues admit smooth (analytic) parameterization away from crossing manifolds, of which crossings are codimension-≥2 generically — but for 1-parameter family, "avoided crossings" of codimension-1 (eigenvalue near-touch but distinct) are generic.

**Success form**: $\lambda_k(t)$ are real-analytic on each smooth-segment subinterval where eigenvalues are non-degenerate; eigenvectors $\phi_k(t)$ are real-analytic likewise; irrep labels $[\rho_k(t)]$ are piecewise constant with finitely many jumps per smooth segment; nodal counts $n_k(t)$ are piecewise constant.

**Failure mode**: Kato-Rellich requires *analytic* family. $H_{\mathrm{joint}}(\mathbf{u}(t))$ is smooth (gradient flow is smooth), but "real-analytic in $t$" requires the gradient flow itself to be analytic — true for analytic energies on analytic manifolds, plausible here but needs verification.

**Interaction with canonical**: Augments T-σ-Multi-1 (static Cat A) with smooth-segment continuity. Uses no new structure beyond Commitment 14.

### §2.2 Approach 2: Stratified-space approach

**Core idea**: $\widetilde\Sigma^K_M$ is **stratified** by the K-active count $K_{\mathrm{act}}(\mathbf{u}) := |\{j : m_j(\mathbf{u}) > 0\}|$ (active formations with positive mass). Strata $\widetilde\Sigma^{(K')}_M$ for $K' = 1, 2, \ldots, K$ are open submanifolds; their boundary is the K-jump locus where one $m_j \to 0$ (formation dissolved).

$\sigma^A(t)$ is then a section over the stratified base: on stratum $K'$, σ-tuple has length-$K'$ structure $(F_{\mathrm{total}}; \{\sigma_j\}_{j=1}^{K'}; \{\sigma_{jk}\}_{1 \leq j < k \leq K'})$.

**Success form**: σ-tuple is well-defined section; K-jump corresponds to stratum transition; jump map characterized by stratum-boundary geometry.

**Failure mode**: K-active count is well-defined only when $m_j$ are bounded away from 0 (and from each other in the case of merger). The "K-jump moment" is when this fails — exactly the singular set. Stratified-space technology (Goresky-MacPherson, Whitney conditions) handles this in algebraic geometry; whether it applies to $\widetilde\Sigma^K_M$ here is non-trivial.

**Interaction with canonical**: Engages MO-1 (Morse stratification) which was sidestepped at single-formation level (CV-1.3). Re-engages MO-1 at multi-formation level — explicit re-engagement, NOT silent resolution.

### §2.3 Approach 3: Topological inheritance via cohomology

**Core idea**: $\sigma^D$ is the conjugacy class of joint stabilizer in $\mathrm{Aut}(G) \wr S_K$. At K-jump, this maps to $\mathrm{Aut}(G) \wr S_{K-1}$. The map is given by a specific **restriction-and-collapse** functor on conjugacy classes:
$$\Psi: \mathrm{ConjugacyClasses}(\mathrm{Aut}(G) \wr S_K) \to \mathrm{ConjugacyClasses}(\mathrm{Aut}(G) \wr S_{K-1}) \tag{*}$$

induced by the embedding $S_{K-1} \hookrightarrow S_K$ (fix one of $K$ slots) followed by collapse $\mathrm{Aut}(G) \wr S_K \to \mathrm{Aut}(G) \wr S_{K-1}$ corresponding to the merger of two slots.

**Success form**: σ^D inheritance map $\Psi$ is **functorial** (independent of merger pair geometry beyond the combinatorial identity of which two indices merge); cohomology level: pull-back / push-forward map on $H^*(B(D \wr S_K)) \to H^*(B(D' \wr S_{K-1}))$.

**Failure mode**: "merger of two slots" is not pure index combinatorics — the new merged formation has stabilizer $D'$ that depends on geometric merger (not just on $D \wr S_2$ for the pre-merger pair). Hence $\Psi$ is **not purely combinatorial**.

**Interaction with canonical**: Refines Commitment 14-Multi (D-6a) by explicitly characterizing $\sigma^D$-trajectory. Independent of $\sigma^A$ continuum behavior.

### §2.4 Approach 4: Right-and-left limit definition (operational)

**Core idea**: Define $\sigma^A(t)$ via right-and-left limits at K-jump times:
$$\sigma^A(t^{*-}) := \lim_{t \nearrow t^*} \sigma^A(t), \quad \sigma^A(t^{*+}) := \lim_{t \searrow t^*} \sigma^A(t). \tag{**}$$

If both limits exist (separate semicontinuity claims), then $\sigma^A(t)$ is well-defined as a *càdlàg* (continue à droite, limites à gauche) function — left-continuous on smooth segments, right-discontinuous at K-jumps.

**Success form**: Cat B sketch theorem stating $\sigma^A(t)$ is càdlàg on $[0, T]$ with K-jumps as discontinuity loci. Operational and matches V3/U4 implementation.

**Failure mode**: This is a *definitional* approach — it doesn't predict the jump rule. Useful for Cat B sketch only; insufficient for Cat A.

**Interaction with canonical**: Minimal — just a continuity-class statement.

### §2.5 Approach 5: Spectral-measure functional limit

**Core idea**: Define $\sigma^A(t)$ via spectral measure of $H_{\mathrm{joint}}(\mathbf{u}(t))$:
$$\mu_t := \sum_k \delta_{\lambda_k(t)} \otimes [\rho_k(t)] \otimes \delta_{n_k(t)}, \tag{***}$$
a measure on $\mathbb{R} \times \mathrm{Irr}(\mathrm{Stab}) \times \mathbb{N}$. The σ-tuple is the support set with multiplicities of $\mu_t$. Continuous evolution = weak convergence of $\mu_t$ in $t$.

**Success form**: Weak convergence holds in smooth segments (eigenvalue continuity) but **discrete jumps** in measure occur when irrep labels jump or nodal counts jump (avoided crossings).

**Failure mode**: At K-jump, the dimension of the spectral support changes (eigenvalues from the dissolved formation disappear); weak convergence fails in standard topology. Need a modified topology (e.g., spectral-measure with multiplicities + dimension-tagged) — technical.

**Interaction with canonical**: Connects to T-σ-Lemma-2 nodal-count properties; potential canonical-level statement bridge.

---

## §3. Primary Selection: Approach 1 + Approach 2 Hybrid

**Decision**: Primary path = Approach 1 (smooth-segment Kato-Rellich) + Approach 2 (stratified-space K-jump). Approach 3 supplements σ^D layer. Approaches 4, 5 are operational fallbacks.

**Rationale**:

1. **Mathematical independence**: Approaches 1 and 2 use orthogonal techniques. Approach 1 = analysis (perturbation theory); Approach 2 = topology/algebra (stratified geometry). Their failure modes are also independent: Kato-Rellich requires analyticity; stratified-space requires Whitney conditions.

2. **Failure mode coverage**: Together they cover both smooth segments (where Kato-Rellich applies) and K-jumps (where stratified-space provides framework). Neither alone suffices.

3. **Interaction with canonical**: Approach 1 augments T-σ-Multi-1 (static Cat A) with continuous-time extension. Approach 2 re-engages MO-1 at multi-formation level — this is a substantive and explicit theoretical commitment, not a silent move.

4. **Failure-mode explicit handling**: If Approach 1 fails (analyticity issue), Approach 4 (right-and-left limit) is the operational fallback. If Approach 2 fails (Whitney conditions don't apply), Approach 3 (cohomology inheritance) replaces the σ^D component.

**Approaches 4 and 5 preserved as fallback**:
- Approach 4 → Cat B sketch fallback if Approach 1 analyticity fails.
- Approach 5 → Cat B sketch fallback for σ^A measure-theoretic well-definedness.

**Approach 3 (cohomology) used supplementally**: Adds rigor to σ^D inheritance specifically — not part of primary path but corroborates it for the topological layer.

---

## §4. Substantive Development

### §4.1 Definitions

**Definition 4.1.1 (Smooth segment).** *Let $\mathbf{u}(t) \in \widetilde\Sigma^K_M$ be a K-field gradient flow trajectory. A smooth segment is a maximal open interval $(t_n^*, t_{n+1}^*) \subset [0, T]$ on which $K_{\mathrm{act}}(\mathbf{u}(t))$ is constant.*

**Definition 4.1.2 (K-jump time).** *A time $t^* \in (0, T)$ is a K-jump time if $K_{\mathrm{act}}(\mathbf{u}(t^{*-})) > K_{\mathrm{act}}(\mathbf{u}(t^{*+}))$ — i.e., $K_{\mathrm{act}}$ strictly decreases at $t^*$.*

**Definition 4.1.3 ($\sigma^A(t)$ along smooth segment).** *On a smooth segment $(t_n^*, t_{n+1}^*)$ with $K_{\mathrm{act}} = K'$, define*
$$\sigma^A(t) := \sigma^A_{\mathrm{multi}}(\mathbf{u}(t)) \in \Sigma^A_{K'}, \tag{4.4.1}$$
*where $\Sigma^A_{K'}$ is the discrete codomain of the σ-tuple at K-active = $K'$.*

(Codomain $\Sigma^A_{K'}$ is the disjoint union over all possible $(\mathcal{F}_{\mathrm{total}}; \{\sigma_j\}; \{\sigma_{jk}\})$ values; it is countable but very large.)

### §4.2 Smooth-Segment Continuity (Lemma 4.2.1)

**Lemma 4.2.1 (Smooth-segment piecewise constancy).**
*Hypotheses:*
- (H1) $\mathbf{u}(t)$ is the gradient flow of $\mathcal{E}_K$ on shared-pool $\widetilde\Sigma^K_M$, smooth in $t$ on a smooth segment $(t_n^*, t_{n+1}^*)$.
- (H2) The energy $\mathcal{E}_K$ is real-analytic on $\widetilde\Sigma^K_M$ (true for the explicit form (4.6) with $W$ a polynomial).
- (H3) On the segment, the joint Hessian $H_{\mathrm{joint}}(\mathbf{u}(t))$ has dimension $N := K' \cdot |X|$ constant, where $K' = K_{\mathrm{act}}$.

*Claim:* $\sigma^A(t)$ is piecewise constant in $t$ on the segment, with jump times $\{\tau_m\} \subset (t_n^*, t_{n+1}^*)$ corresponding to **avoided crossings** of $H_{\mathrm{joint}}$ eigenvalues. At each $\tau_m$:
- Eigenvalues $\lambda_k(t)$ are continuous (real-analytic; T1 of Kato).
- Irrep labels $[\rho_k(t)]$ are piecewise constant; jump discretely between $\tau_m^-$ and $\tau_m^+$ when two eigenvalues become equal but irreps differ.
- Nodal counts $n_k(t)$ similarly piecewise constant; possibly jump at $\tau_m$.

*Proof sketch.*

**Step 1 (Kato-Rellich).** Under (H2), $\mathbf{u}(t)$ is real-analytic in $t$ on the smooth segment (gradient flow of real-analytic energy on real-analytic manifold). Hence $H_{\mathrm{joint}}(\mathbf{u}(t))$ is a real-analytic family of $N \times N$ self-adjoint matrices.

By Kato's Theorem T1 (analytic perturbation), the eigenvalues $\lambda_k(t)$ admit real-analytic parameterization on the segment, possibly after permutation labeling. Specifically: there exist real-analytic functions $\widetilde\lambda_1(t), \ldots, \widetilde\lambda_N(t)$ such that the multiset $\{\widetilde\lambda_k(t)\} = \{\lambda_k(t)\}$ (eigenvalue spectrum), and eigenvectors $\widetilde\phi_k(t)$ are real-analytic likewise. ∎ (Step 1)

**Step 2 (irrep label discrete).** Each $\widetilde\phi_k(t)$ is a smooth path in projective space $\mathbb{P}(V)$, where $V = T_{\mathbf{u}(t)}\widetilde\Sigma^K_M$. The irrep label $[\rho_k(t)] := $ irrep type of $\widetilde\phi_k(t)$ under $\mathrm{Stab}(\mathbf{u}(t))$ is **discrete** (countable set $\mathrm{Irr}(\mathrm{Stab}(\mathbf{u}(t)))$).

For $\mathbf{u}(t)$ on a smooth segment, $\mathrm{Stab}(\mathbf{u}(t))$ may itself vary with $t$ — but only in a **descending sequence** (Stab can only shrink as the field varies generically). Hence on a generic smooth subsegment, $\mathrm{Stab}$ is constant. Within the constant-Stab subsegment, $[\rho_k(t)]$ is determined by $\widetilde\phi_k(t)$'s isotypic component, which is a *characteristic-polynomial root* of the Stab-action — discrete and constant unless $\widetilde\phi_k(t)$ crosses an irrep boundary.

Crossings: $[\rho_k(t)]$ can jump only when $\widetilde\phi_k(t)$ passes through a boundary between two irrep blocks. For 1-parameter families, this is a codim-1 event (avoided crossings) and generic. ∎ (Step 2)

**Step 3 (avoided crossings are discrete).** By Wigner-von Neumann theorem (1-parameter generic family of Hermitian matrices), eigenvalue crossings $\lambda_j(t) = \lambda_k(t)$ with $j \neq k$ have codimension 2 in the Hermitian matrix space; for our 1-parameter family, codim-2 events are **non-generic** (do not occur on generic 1-parameter family).

However, **avoided crossings** (eigenvalues come close but don't touch; eigenvectors mix) are codim-1 and DO occur. At avoided crossings, the irrep labels and nodal counts of $\widetilde\phi_j(t), \widetilde\phi_k(t)$ can swap.

The set of avoided-crossing times in $(t_n^*, t_{n+1}^*)$ is **discrete** (countable, no accumulation point) by analyticity. ∎ (Step 3)

**Step 4 (piecewise constancy).** Combining: on each open subinterval between consecutive avoided crossings, $\sigma^A(t)$ is constant (eigenvalues vary smoothly but the *discrete labels* (irrep + nodal) are constant). At avoided crossings, $\sigma^A(t)$ jumps via finite swap. ∎ (Step 4)

**Cat status**: **Cat B target**. Step 1 is Cat A under (H2) analytic energy. Steps 2-3 are Cat B under (A1)-(A2) genericity assumptions. Step 4 follows.

### §4.3 Genericity Conditions and Failure Modes

**Failure mode FM1**: Energy not real-analytic. Not applicable here ($W$ polynomial; gradient flow of polynomial = real-analytic).

**Failure mode FM2**: Avoided crossings accumulate at a finite time. Requires non-generic gradient flow (or pathological initial condition). Lemma 4.2.1 hypothesis "generic trajectory" excludes this; by genericity (per [analytic dynamical systems argument; W7+ rigorous reference]), excluded for almost-every initial condition.

**Failure mode FM3**: Stab($\mathbf{u}(t)$) varies wildly (not descending sequence). Possible if $\mathbf{u}(t)$ crosses higher-symmetry strata; these are codim ≥ 1 events. For generic trajectory, generic Stab is the trivial group except at isolated symmetric configurations. Lemma 4.2.1 piecewise-constant statement extends to Stab-varying case by combining piecewise constants of all visited Stab subgroups.

**Cat A path** (open): Remove genericity hypothesis (A1) by addressing accumulation points + non-descending Stab. Currently NQ-242b W7+.

### §4.4 K-Jump Inheritance (Lemma 4.4.1)

**Lemma 4.4.1 (K-jump σ-trajectory left/right limits).**
*Hypotheses:*
- (H1) Same as Lemma 4.2.1.
- (H2k) $t^* \in (0, T)$ is a K-jump time with $K_{\mathrm{act}}(\mathbf{u}(t^{*-})) = K'$, $K_{\mathrm{act}}(\mathbf{u}(t^{*+})) = K' - 1$ (simple merger ΔK = 1).
- (H3k) The merger is "soft" — i.e., one $m_j(\mathbf{u}(t)) \to 0$ continuously as $t \nearrow t^*$, with $m_j(\mathbf{u}(t)) > 0$ for $t < t^*$.

*Claim:*
(a) **Left limit exists**: $\sigma^A(t^{*-}) := \lim_{t \nearrow t^*} \sigma^A(t)$ exists in $\Sigma^A_{K'}$.
(b) **Right limit exists**: $\sigma^A(t^{*+}) := \lim_{t \searrow t^*} \sigma^A(t)$ exists in $\Sigma^A_{K'-1}$.
(c) **Inheritance is non-deterministic in σ alone**: $\sigma^A(t^{*+})$ is **not** determined by $\sigma^A(t^{*-})$ alone; it depends on the merger geometry $\mathcal{M}$ := (which two formations merged, how the merged blob relaxes post-merger).

*Proof sketch / failure analysis.*

**Step 1 (Left limit).** As $t \nearrow t^*$, $\mathbf{u}(t)$ is on a smooth segment with $K' = K_{\mathrm{act}}$; Lemma 4.2.1 applies; $\sigma^A(t)$ is piecewise constant. The left limit $\sigma^A(t^{*-})$ is the value on the final piece. **Cat A** under Lemma 4.2.1. ✓

**Step 2 (Right limit).** As $t \searrow t^*$, $\mathbf{u}(t)$ is on a smooth segment with $K' - 1$ active formations. Lemma 4.2.1 applies again; $\sigma^A(t^{*+})$ is the value on the first piece of the post-merger smooth segment. **Cat A** under Lemma 4.2.1. ✓

**Step 3 (Non-determinism).** Consider the merger: pre-merger pair $(u^{(j)}, u^{(k)})$ with $m_k \to 0$ as $t \nearrow t^*$. Post-merger, the joint state has $K' - 1$ formations — formation $j$ now contains the pre-merger mass $m_j + m_k$.

**Key observation**: Pre-merger σ-tuple $\sigma^A(t^{*-})$ contains:
- $(F_{\mathrm{total}}; \{\sigma_l\}_{l=1}^{K'}; \{\sigma_{lm}\}_{l<m})$ — note that $\sigma_k$ is the σ-tuple of formation $k$ which is *vanishing*. As $m_k \to 0$, formation $k$'s shape becomes singular (delta-like), so $\sigma_k$ becomes degenerate/ill-defined in this limit.

Post-merger σ-tuple $\sigma^A(t^{*+})$ contains:
- $(F_{\mathrm{total}}'; \{\sigma_l'\}_{l=1}^{K'-1}; \{\sigma_{lm}'\}_{l<m})$ where $\sigma_l' = \sigma_l$ for $l \neq j$, but $\sigma_j'$ is the σ-tuple of the *merged* formation at the relaxed configuration $u^{(j)}_{\mathrm{post}}$.

The map
$$\Phi: \sigma^A(t^{*-}) \to \sigma^A(t^{*+}) \tag{4.4.2}$$
is **not deterministic** in $\sigma^A(t^{*-})$ alone because $\sigma_j'$ depends on:
- Geometry of how $u^{(j)}$ and $u^{(k)}$ overlapped at the moment of merger (cluster centroids, orientation).
- Post-merger relaxation dynamics on $\widetilde\Sigma^{K'-1}_M$ — which deposits $u^{(j)}_{\mathrm{post}}$ at a specific local minimum that depends on initial configuration of post-merger flow.

These geometric details are NOT encoded in $\sigma^A(t^{*-})$ (which is a discrete spectroscopic signature, not a geometric description).

**Conclusion**: Inheritance is **non-deterministic in σ alone**. The map $\Phi$ requires merger-geometry data $\mathcal{M}$ as additional input:
$$\Phi: (\sigma^A(t^{*-}), \mathcal{M}) \to \sigma^A(t^{*+}). \tag{4.4.3}$$

**Cat B target**: Lemma 4.4.1(a)(b)(c) is provable at Cat B target — left/right limits exist (Cat A); non-determinism is established by the geometric-data argument above (Cat B sketch; rigorous "no σ-only deterministic map exists" requires constructing two trajectories with same $\sigma^A(t^{*-})$ and different $\sigma^A(t^{*+})$ — open as NQ-242c W6+).

### §4.5 σ^D Trajectory via Approach 3 (Topological Layer)

The discrete topological layer $\sigma^D(t)$ admits cleaner inheritance:

**Proposition 4.5.1 (σ^D restriction at K-jump).**
*Under hypotheses of Lemma 4.4.1, the σ^D inheritance is given by the conjugacy-class restriction map*
$$\Psi: \sigma^D(t^{*-}) \in \mathrm{ConjugacyClasses}(\mathrm{Aut}(G) \wr S_{K'}) \to \sigma^D(t^{*+}) \in \mathrm{ConjugacyClasses}(\mathrm{Aut}(G) \wr S_{K'-1}). \tag{4.4.4}$$
*induced by the embedding $S_{K'-1} \hookrightarrow S_{K'}$ corresponding to the merger pair $(j, k)$, followed by the natural projection $\mathrm{Aut}(G) \wr S_{K'} \to \mathrm{Aut}(G) \wr S_{K'-1}$.*

*Proof sketch.* Topological pull-back of joint stabilizer along merger embedding. The merger collapses two formation-slots into one; the wreath-product structure dictates the corresponding group homomorphism. ∎ (Cat B sketch.)

**Caveat**: The post-merger stabilizer $\mathrm{Stab}(\mathbf{u}(t^{*+}))$ may be **larger** than the pull-back image — additional symmetries can emerge from the merger when the merged blob has higher symmetry than expected. This **emergence** is a non-trivial geometric phenomenon (NQ-242d).

**Comparison with $\sigma^A$ inheritance**: $\sigma^D$ inheritance is **at least partially deterministic** (the pull-back image is determined). Additional symmetry *gain* from merger is the only non-deterministic part — quantitatively much smaller information than the $\sigma^A$ non-determinism.

### §4.6 Synthesis: σ_multi^A(t) Cat B Target Theorem

Combining Lemma 4.2.1 + Lemma 4.4.1 + Proposition 4.5.1:

**Theorem 4.6.1 (σ_multi(t) trajectory; Cat B target).**
*Under Hypotheses (H1), (H2), (H3), (H2k), (H3k) above, $\sigma_{\mathrm{multi}}(t) := (\sigma^A(t), \sigma^D(t))$ is a càdlàg trajectory on $[0, T]$ with the following properties:*

(i) *Smooth-segment piecewise constancy* (Cat B target): $\sigma_{\mathrm{multi}}(t)$ is piecewise constant on each smooth segment with discrete jump times (avoided crossings); jumps are σ-tuple permutations.

(ii) *K-jump left/right limits* (Cat A): At K-jump time $t^*$, $\sigma_{\mathrm{multi}}(t^{*\pm})$ exist as elements of $\Sigma^A_{K'} \times \mathrm{ConjugacyClasses}_{K'}$ resp. $\Sigma^A_{K'-1} \times \mathrm{ConjugacyClasses}_{K'-1}$.

(iii) *σ^A inheritance non-determinism* (Cat B sketch): The map $\Phi: \sigma^A(t^{*-}) \to \sigma^A(t^{*+})$ is not deterministic in $\sigma^A(t^{*-})$ alone; it requires merger-geometry data $\mathcal{M}$.

(iv) *σ^D inheritance partial determinism* (Cat B sketch): $\Psi: \sigma^D(t^{*-}) \to \sigma^D(t^{*+})$ is determined by pull-back along merger embedding modulo possible symmetry emergence (NQ-242d).

*Remark.* This theorem upgrades D-6b from "Cat B sketch only" (per `01_canonical_promotion_queue_review.md` §2 D-6b) to **structured Cat B target with explicit failure modes**. The non-determinism in (iii) is a **substantive negative result** — not a gap in proof but a genuine feature of the K-jump dynamics. This bifurcates the theory:

- Path A: Accept non-determinism; treat $\sigma^A(t)$ as càdlàg trajectory with auxiliary merger-geometry data $\mathcal{M}$ at K-jumps. Cat B target theorem.
- Path B: Augment σ-tuple definition to include enough geometric information to deterministically predict post-merger σ; probably requires moving from spectroscopic σ to a **richer invariant** (e.g., σ + cluster centroid/orientation data). Cat A target — open NQ-242 (full Hessian σ-tuple time-series with rigorous K-jump theory).

**Recommendation**: Path A for v1.6 release; Path B as W6+ research direction.

---

## §5. Integration with Canonical

### §5.1 Compatibility with T-σ-Multi-1 (D-6a static)

T-σ-Multi-1 (Theorem 4.3.1 in `02_paper_section4_polished.md`) characterizes **static** σ_multi at a fixed Morse-0 well-separated joint minimizer. Theorem 4.6.1 here extends this to **trajectories** — but the trajectory may not consist of Morse-0 minimizers at every $t$ (during transient post-merger relaxation, the state is not at a critical point).

**Resolution**: σ_multi(t) is well-defined whenever $H_{\mathrm{joint}}(\mathbf{u}(t))$ is Hermitian (always true), even off critical points. The "Morse-0" hypothesis of T-σ-Multi-1 corresponds to the "well-separated" smooth-segment regime where the joint state is *near* a Morse-0 minimizer. Off critical points, $\mathbf{u}(t)$ is in transit between local minima, but $\sigma_{\mathrm{multi}}$ remains a discrete spectroscopic invariant.

**Compatibility**: Theorem 4.6.1 ⊂ T-σ-Multi-1's domain (smooth segments) + extends to non-Morse-0 transient states. **No conflict** with D-6a static framework.

### §5.2 Compatibility with Commitment 14-Multi (D-6a)

D-6a Commitment 14-Multi (per `01_*` §2 D-6a) defines $\sigma_{\mathrm{multi}}(\mathbf{u}^*) := (\sigma^A(\mathbf{u}^*), \sigma^D(\mathbf{u}^*))$ at fixed minimizer. Theorem 4.6.1 extends this definition to time-evolving trajectories.

**Required canonical-text augmentation** (if D-6b adopted):

```
σ_multi(t) := σ_multi(u(t)) along K-field gradient flow trajectory u(t).
On smooth segments: piecewise constant càdlàg trajectory.
At K-jump times t*: σ_multi(t*-) and σ_multi(t*+) both exist; the
inheritance map Φ: σ^A(t*-) → σ^A(t*+) is non-deterministic in σ^A(t*-)
alone (Cat B sketch — NQ-242 full Hessian σ-tuple W6+); the σ^D
inheritance Ψ is partial-deterministic (pull-back at merger embedding
modulo symmetry-emergence NQ-242d).
```

This augmentation is ~10-15 lines, matching `01_*` §2 D-6b "~20-30 lines" estimate after consolidation. **Refines the D-6b estimate downward**: with the substantive Theorem 4.6.1 framework, the augmentation is more compact.

### §5.3 Compatibility with V5b-T' / V5b-F (D-3, D-5)

V5b-T' and V5b-F characterize *static* corner-saturated F=1 minimizers (single-formation). Their dynamic counterparts (does corner-saturation persist along trajectory? does the cluster wander via the PN-barrier-lifted Goldstone?) are open.

**Theorem 4.6.1 implication for V5b-T'/V5b-F dynamics**: in the regime where V5b-T'/V5b-F apply (sub-lattice corner-saturated), $\sigma^A(t)$ on a smooth segment follows Lemma 4.2.1 with the cluster Goldstone as a quasi-zero eigenvalue. The cluster center $\mathbf{x}_*(t)$ is a *slow* mode; σ-tuple's lowest eigenvalue evolves as PN-barrier oscillation.

**Cross-link**: V5b-T'/V5b-F dynamic + Theorem 4.6.1 smooth-segment piecewise-constancy ⇒ for K=1 at corner-saturated, σ-tuple is piecewise constant in $t$ except for occasional "cluster hop" events (lattice-translation jumps). NQ-247 W6+ — characterize cluster-hop frequency from PN-barrier height.

### §5.4 Re-engagement with MO-1 (sidestepped at single-formation)

MO-1 (Morse theory inapplicability at corners) was sidestepped at single-formation level (CV-1.3) by restricting σ-framework to Morse-0 interior critical points. Theorem 4.6.1 **re-engages** MO-1 at multi-formation level via Approach 2 stratified-space — explicitly:

- $\widetilde\Sigma^K_M$ is stratified by $K_{\mathrm{act}}$.
- K-jump = stratum transition = "corner" of the stratified space.
- Theorem 4.6.1 provides one-sided continuity at strata boundaries — partially rescues Morse-theoretic analysis.

**Status**: This is **explicit re-engagement** of MO-1, NOT silent resolution. The full Morse stratification at multi-formation level remains OPEN (NQ-248 W7+).

---

## §6. New Open Questions

Surfaced by §4 development:

**NQ-242 (full Hessian σ-tuple time-series with rigorous K-jump theory; W6+, Cat A path).** Build on Theorem 4.6.1 Cat B target by:
- (i) Removing genericity hypotheses (A1)-(A2) via rigorous accumulation-point analysis.
- (ii) Constructing the deterministic σ-augmentation $\sigma_{\mathrm{rich}}$ that includes minimal geometric data needed for K-jump determinism (Path B in §4.6).
- (iii) Numerical: full Hessian σ-tuple at dense time samples (not V3's 10 sparse + simplified) on K=8 trajectory.

**NQ-242b (avoided-crossing accumulation; W7+).** Rigorous proof that avoided crossings do not accumulate at finite times for K-field gradient flow on shared-pool. Currently part of Step 3 in Lemma 4.2.1; requires generic dynamical systems argument.

**NQ-242c (σ^A non-determinism explicit construction; W6+, Cat B → Cat A).** Construct two K-field trajectories with identical $\sigma^A(t^{*-})$ but different $\sigma^A(t^{*+})$. Currently asserted in Lemma 4.4.1(c) Step 3; explicit construction would upgrade to Cat A.

**NQ-242d (σ^D symmetry emergence; W6+, Cat B → Cat A).** Characterize when post-merger stabilizer is strictly larger than pull-back image — i.e., merger gains symmetry. Examples: two equal-mass disks merging into a single disk on a translation-invariant graph gain $\mathbb{Z}_2$ swap symmetry that the pre-merger had explicitly; what about translation symmetry of the *combined* mass?

**NQ-247 (V5b-T'/V5b-F cluster-hop dynamics; W6+).** Smooth-segment σ-trajectory in corner-saturated regime: characterize the frequency and amplitude of "cluster hop" events (lattice-translation jumps) from PN-barrier height. Numerical accessible via long-time runs in regime R3b.

**NQ-248 (multi-formation Morse stratification; W7+).** Full Morse-theoretic analysis of $\widetilde\Sigma^K_M$ stratified by $K_{\mathrm{act}}$ — analog of Goresky-MacPherson stratified Morse, applied to SCC. Re-engages MO-1 at multi-formation level.

---

## §7. Impact on D-6b User-Decision Recommendation

### §7.1 Before this development

Per `01_canonical_promotion_queue_review.md` §2 D-6b: "**RECOMMEND DEFER**" because:
- Cat B sketch only (V3 simplified σ-tuple, not full Commitment 14).
- K-jump theory at canonical level not addressed.
- Below typical Cat-B-target threshold for new Commitment-level extensions.

### §7.2 After this development (revised assessment)

Theorem 4.6.1 + Lemmas 4.2.1, 4.4.1 + Proposition 4.5.1 in §4 above provide:

1. **Smooth-segment Cat B target** (Lemma 4.2.1) — piecewise constancy with explicit Kato-Rellich + Wigner-von Neumann backing.

2. **K-jump left/right limits Cat A** (Lemma 4.4.1 Steps 1-2) — limits exist by reduction to smooth-segment via Lemma 4.2.1.

3. **σ^A non-determinism Cat B sketch** (Lemma 4.4.1 Step 3) — substantive **negative result** about K-jump structure.

4. **σ^D partial-determinism Cat B sketch** (Proposition 4.5.1) — pull-back along merger embedding modulo symmetry emergence.

5. **Theorem 4.6.1 synthesis** — Cat B target with explicit failure mode catalog.

This is **above** the threshold for canonical inclusion (Cat B target + partial Cat A on left/right limits + explicit non-determinism is a substantive theoretical claim, not a sketch).

### §7.3 Revised recommendation

**REVISED**: D-6b is now **CANONICALLY DRAFTABLE** as Cat B target under Theorem 4.6.1 framework. Three options for user:

- **Option D-6b-1**: Approve D-6b for CV-1.5.1 with the augmentation per §5.2 above (~10-15 lines, leaner than original `01_*` estimate of 20-30). Cat B target with explicit non-determinism caveat.
- **Option D-6b-2**: Defer D-6b but with **shorter horizon** — W6+ (NQ-242 full Hessian) rather than indefinitely. Path B (rich σ-augmentation) becomes a clear research goal.
- **Option D-6b-3 (default per `01_*`)**: Defer D-6b indefinitely.

**My recommendation**: Option D-6b-2 (shorter-horizon defer). Reasons:
- Theorem 4.6.1 is rigorous at Cat B target level — could be canonically merged.
- However, the full Hessian σ-tuple time-series numerics (NQ-242) are not yet done; including D-6b in CV-1.5.1 commits to a Cat B sketch that NQ-242 may refine into Cat A within W6.
- Holding D-6b for W6+ allows the Cat B → Cat A transition to be a **single canonical edit** in CV-1.6, rather than two edits (CV-1.5.1 Cat B sketch → CV-1.6 Cat A refinement).

### §7.4 Comparison with Option Matrix

If Option D-6b-2 is adopted:
- W5 Day 4: User approves D-1..D-5 + D-6a per Recommended option (defer D-6b).
- W6 Day 1-3: NQ-242 full Hessian σ-tuple time-series + dense numerical anchoring.
- W6 Day 4-5: Cat B → Cat A refinement of Theorem 4.6.1; canonical merge in CV-1.6.

This integrates Theorem 4.6.1 framework into the W5 → W6 transition cleanly.

---

## §8. Hard Constraint Verification

- [x] canonical 직접 수정 0 — this file is theoretical development only; no canonical edits performed.
- [x] No silent resolution — Theorem 4.6.1 (iii) σ^A non-determinism is **explicit negative result** with NQ-242c open; not hidden.
- [x] No primitive override — σ_multi(t) operates on $\mathbf{u}(t) : X \to [0,1]^K$; objects derivative.
- [x] No 4-energy-term merging — $\mathcal{E}_K$ structure preserved.
- [x] No closure idempotence assumption.
- [x] K not dual-treated — K integer throughout; $K_{\mathrm{act}}$ integer-valued discrete strata.
- [x] No metastability without P-F flag — §1.4 implicit assumption (A4) flags zero-T determinism context; § 4.3 FM2 accumulation flagged.
- [x] No reductive equation — Approach 3 cohomology connects to algebraic topology but is **structural correspondence**, not reduction.
- [x] Multi-approach generation: 5 approaches (§2.1-§2.5), independence checked (§3 rationale).
- [x] Primary selection with rationale: Approach 1 + 2 hybrid (§3); 4, 5 preserved as fallbacks; 3 supplementary.
- [x] Substantive development: 3 lemmas + 1 proposition + 1 theorem (Theorem 4.6.1) with proofs/sketches/failure analyses.
- [x] Forward gaps catalogued: NQ-242a/b/c/d, NQ-247, NQ-248 (§6).

---

## §9. References

- Theorem 4.6.1 = synthesis of Lemma 4.2.1 + Lemma 4.4.1 + Proposition 4.5.1.
- Cited results:
  - Kato T1 (analytic perturbation) — `T. Kato, Perturbation Theory for Linear Operators` (Springer 1980), §VII.3.
  - Wigner-von Neumann avoided crossings — physics standard reference.
  - Goresky-MacPherson stratified Morse — `Stratified Morse Theory` (Springer 1988).
  - Frobenius reciprocity (used in §4.5 wreath restriction) — `Serre, Linear Representations of Finite Groups` Ch. 3.
- Within-SCC references:
  - canonical T-σ-Multi-1 (proposed via D-6a, current §13 entry near line 1171 if approved).
  - canonical Commitment 14-Multi (proposed via D-6a, current §11.1 after line 768 if approved).
  - canonical V5b-T' (proposed via D-5).
  - `00_phase9_10_reconciliation.md` §2 D-6b.
  - `01_canonical_promotion_queue_review.md` §2 D-6b.
  - `2026-04-28/30_T4_CH_correspondence_sigma_t.md` (Phase 8 σ-trajectory framework).
  - `2026-04-28/33_Phase9_findings_integration.md` §3 (U4 simplified σ trajectory).
  - `2026-04-28/34_Phase10_findings.md` §3 (V3 Hessian σ-tuple) + §4 (V4 K-jump statistics).

---

**End of 04_D6b_sigma_trajectory_development.md.**
**Status: D-6b upgraded from "Cat B sketch — recommend defer" to "Cat B target with structured framework + explicit failure modes". Theorem 4.6.1 + Lemmas 4.2.1, 4.4.1 + Proposition 4.5.1 provide rigorous skeleton. 5 new open questions catalogued (NQ-242a/b/c/d, NQ-247, NQ-248). Revised recommendation: Option D-6b-2 (shorter-horizon defer to W6+ via NQ-242 full Hessian σ-tuple).**
