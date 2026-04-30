# sigma_trajectory_perturbation.md — σ-tuple Time Evolution under Small Parameter Perturbation (NQ-244)

**Status:** Working draft — Cat A/B demarcated; W6+ promotion candidate.
**Spawned:** 2026-04-30 (NQ-244; SF-axis).
**Author origin:** NQ-188 (σ-uniqueness) identified that σ-class structure is locally constant between bifurcation surfaces; NQ-244 makes this precise as a trajectory theorem under $(\alpha, \beta, c) \to (\alpha + \delta\alpha, \beta + \delta\beta, c + \delta c)$.
**Canonical refs:** §11.1 Commitment 14 (O5')(O7) σ-tuple definition (line 790); §13 T-σ-Lemma-1/2/3; §13 T-σ-Theorem-3/4; §14 CN10 (contrastive vs reductive); §14 CN17 (σ-Labeled Formation Quantization).
**Working refs:** `working/SF/sigma_uniqueness_theorem.md` (NQ-188 σ-class discrete catalog + BC-188-1); `working/SF/sigma_topological_invariance.md` (NQ-190 graph-isomorphism vs subdivision invariance); `working/SF/sigma_theorem4_higher_order.md` (NQ-187 ε² splitting, 5th equivariant absence, 6th equivariant $c_4$).
**External refs:** Crandall–Rabinowitz 1971; Sattinger 1979; Golubitsky–Schaeffer 1985 Vol. I; Golubitsky–Stewart–Schaeffer 1988 Vol. II.

**Hard constraints:**
- Direct canonical edits: 0. This file is W6+ promotion candidate only.
- CN10 contrastive: σ-tuple is SCC-intrinsic Hessian-spectral mathematics; bifurcation theory is referenced contrastively (parallel smooth-manifold structure), not as a reduction of σ.
- F-1, M-1, MO-1 are NOT silently resolved.
- Open problems NQ-244-a through NQ-244-d registered below; none closed.
- Cat A / Cat B / Cat C demarcations are explicit throughout.

---

## §1. Setup — Small-Perturbation Regime

**Parameter space.** Fix a finite connected graph $G = (X, E)$ with $|X| = n$, and a base parameter triple $(\alpha_0, \beta_0, c_0)$ with:
- $c_0 \in \mathcal{S} := ((3-\sqrt{3})/6,\, (3+\sqrt{3})/6)$ (spinodal interior; $W''(c_0) < 0$; canonical §3),
- $\beta_0 > \beta_{\mathrm{crit}}^{(2)} = 4\alpha_0 \lambda_2^{\mathrm{Lap}}/|W''(c_0)|$ (post-bifurcation, non-uniform minimizer regime),
- $u_0^* \in \Sigma_m^\circ$ a Morse-0 non-uniform critical point of $\mathcal{E}(\cdot;\, \alpha_0, \beta_0, c_0)$.

**Small-perturbation regime.** A perturbation $\delta\mathbf{p} = (\delta\alpha, \delta\beta, \delta c)$ is *admissible* if:
1. $c_0 + \delta c$ remains in spinodal interior $\mathcal{S}$;
2. $\beta_0 + \delta\beta$ does not cross any bifurcation critical value $\beta_{\mathrm{crit}}^{(k)}$ for the family $u^*(\mathbf{p})$;
3. $\|\delta\mathbf{p}\|$ is small enough for the implicit function theorem (IFT) to apply at $u_0^*$.

**IFT smooth family.** Under admissible $\delta\mathbf{p}$, the critical-point equation $\nabla_u \mathcal{E}(u^*; \mathbf{p}) = \mu(\mathbf{p})\,\mathbf{1}$ (Lagrange stationarity on $\Sigma_m$) is a smooth equation in $(u^*, \mathbf{p})$. At a Morse-0 minimizer, the constrained Hessian $H(u_0^*;\mathbf{p}_0)$ restricted to $\mathbf{1}^\perp$ is positive definite (all eigenvalues $> 0$). By IFT applied to $F(u, \mathbf{p}) := \nabla_u \mathcal{E}(u;\mathbf{p}) - \mu\,\mathbf{1} = 0$ on $\mathbf{1}^\perp$, there exists a neighborhood $\mathcal{U}(\mathbf{p}_0)$ and a smooth map $\mathbf{p} \mapsto u^*(\mathbf{p})$ such that:
$$u^*(\mathbf{p}_0 + \delta\mathbf{p}) = u_0^* + J_\mathbf{p}\,\delta\mathbf{p} + O(\|\delta\mathbf{p}\|^2),$$
where $J_\mathbf{p} = -[H(u_0^*)]^{-1} \partial_\mathbf{p}(\nabla_u \mathcal{E})$ is the IFT Jacobian. **Cat A for the IFT existence** (standard Banach IFT on $\mathbb{R}^n$; positivity of $H$ guaranteed by Morse-0 hypothesis).

**Bifurcation surface avoidance.** The condition "no bifurcation crossing" in item (2) above is the key non-degeneracy assumption. The set of bifurcation surfaces in $(\alpha, \beta, c)$-space is catalogued in §3 and §5. Outside this set, the σ-tuple trajectory is smooth.

---

## §2. Continuity Claims for σ-tuple Components

Under the IFT smooth family $u^*(\mathbf{p})$, the σ-tuple

$$\sigma(u^*(\mathbf{p})) = \bigl(\mathcal{F}(u^*(\mathbf{p}));\; \{(n_k(\mathbf{p}),\, [\rho_k(\mathbf{p})],\, \lambda_k(\mathbf{p}))\}_{k=1}^{K(\mathbf{p})}\bigr)$$

has four qualitatively distinct components with different continuity behavior.

**2.1 $\mathcal{F}$ — locally constant outside fold/peak-creation events.**

$\mathcal{F}(u^*)$ counts local maxima of the field $u^*: X \to [0,1]$. On a finite graph, a local maximum at site $x$ satisfies $u^*(x) > u^*(y)$ for all $y \sim x$. This is an *open condition* in $u^*$ (strict inequalities). Since $u^*(\mathbf{p})$ is smooth in $\mathbf{p}$ by IFT, and the local-maximum condition is open, $\mathcal{F}$ is locally constant in $\mathbf{p}$ away from the saddle-node threshold where $u^*(x) = u^*(y)$ for some adjacent pair $\{x,y\}$. **Cat A** (open-set argument; immediate from IFT smoothness).

**2.2 $\{n_k\}$ — locally constant outside eigenvalue crossings.**

$n_k = \mathcal{N}(\phi_k)$ is the nodal count of the $k$-th Hessian eigenvector, with $\mathcal{N}$ defined as the number of sign changes (T-σ-Lemma-2 (i)). The nodal count is an integer, hence locally constant in $\phi_k$ away from eigenvector degeneracies. Since $H(u^*(\mathbf{p}))$ varies smoothly in $\mathbf{p}$ (smooth $u^*(\mathbf{p})$, smooth Hessian formula $H = 4\alpha L_G + \beta W''(u^*)\mathrm{diag}$), its eigenvectors $\phi_k(\mathbf{p})$ vary smoothly away from eigenvalue crossings. Hence $n_k(\mathbf{p})$ is locally constant in the open set where $\lambda_k(\mathbf{p}) \neq \lambda_{k+1}(\mathbf{p})$. **Cat A** (integer-valuedness + smoothness of Hessian eigenvectors between crossings).

**2.3 $\{[\rho_k]\}$ — locally constant outside irrep-permutation events at eigenvalue crossings.**

$[\rho_k]$ is the $\widehat{G_u}$-irrep label of the $k$-th eigenspace (Commitment 14 (O5), T-σ-Lemma-1 (ii)). The irrep label is discrete-valued ($\widehat{G_u}$ is finite for finite $G$), hence locally constant in $\mathbf{p}$ as long as: (a) the residual stabilizer $G_{u^*(\mathbf{p})} = \mathrm{Stab}_{\mathrm{Aut}(G)}(u^*(\mathbf{p}))$ does not change (no orbit-type transition), and (b) eigenvalue ordering $\lambda_k < \lambda_{k+1}$ is strict (no eigenvalue crossing that permutes irrep assignment via (O5')(O7) reordering). Both (a) and (b) hold in an open dense subset of $\mathbf{p}$-space. **Cat A** (discreteness + stabilizer group locally constant away from symmetry-breaking/merging events).

**2.4 $\{\lambda_k\}$ — continuous; real-analytic away from crossings.**

The Hessian eigenvalues $\lambda_k(\mathbf{p})$ are continuous functions of $u^*(\mathbf{p})$, hence continuous in $\mathbf{p}$. Away from eigenvalue crossings, the eigenvalues are $C^\infty$ (real-analytic by Rellich's theorem for analytic matrix-valued families; the Hessian $H(\mathbf{p})$ is a polynomial in $\mathbf{p}$ via the double-well $W$). At crossings, eigenvalues remain continuous but the assignment $k \mapsto \lambda_k$ (by ascending order) has a corner. **Cat A** for continuity; **Cat A** for real-analyticity away from crossings (Rellich; canonical §13 T-σ-Theorem-3/4 analytic structure).

**Summary table.**

| Component | Behavior | Cat |
|---|---|---|
| $\mathcal{F}$ | Locally constant; jumps at peak-creation/fold events | A |
| $n_k$ | Locally constant; jumps at eigenvalue crossings | A |
| $[\rho_k]$ | Locally constant; permutes at eigenvalue crossings / orbit-type transitions | A |
| $\lambda_k$ | Continuous; real-analytic away from crossings | A |

---

## §3. Discontinuity Events — σ-trajectory Transition Catalog

There are exactly four types of events at which the σ-tuple has a discontinuity or non-analyticity as a function of $\mathbf{p} = (\alpha, \beta, c)$.

**Type (i): Bifurcation events** ($\beta$ crosses $\beta_{\mathrm{crit}}^{(k)}$ for some $k$).

At $\beta = \beta_{\mathrm{crit}}^{(k)} = 4\alpha \lambda_k^{\mathrm{Lap}}/|W''(c)|$, the $k$-th Laplacian eigenmode becomes a soft direction; a supercritical pitchfork bifurcation (T-Birth-Parametric, Cat A) creates two new Morse-0 minimizers on the Fiedler subspace $V_k$. The existing minimizer $u_0^*$ changes continuously but the σ-tuple acquires new low-eigenvalue entries as the new soft mode's eigenvalue descends to zero. Specifically: $\mathcal{F}$ increases (new peak born), new low-$\lambda$ entry appended to the $\sigma$-sequence, and $K$ increases. **Type (i) events occur on the codimension-1 surface** $\beta = \beta_{\mathrm{crit}}^{(k)}$ in $(\alpha, \beta, c)$-space.

**Type (ii): Eigenvalue crossings** at fixed $\beta$ (varying $\alpha$ or $c$).

When two consecutive Hessian eigenvalues $\lambda_k(\mathbf{p})$ and $\lambda_{k+1}(\mathbf{p})$ become equal at $\mathbf{p}_*$, the σ-tuple's ordering by ascending eigenvalue (Commitment 14 (O5)) permutes the entries $(n_k, [\rho_k])$ and $(n_{k+1}, [\rho_{k+1}])$. The Mulliken tie-break (O7) provides a convention at the crossing point, but the irrep labels $[\rho_k]$ and $[\rho_{k+1}]$ may swap post-crossing. This is a **label permutation event**, not a topological change. The $\lambda_k$ values remain continuous; only the assignment of $(n, [\rho])$ to eigenvalue slots changes. Type (ii) events occur on codimension-1 surfaces $\{\lambda_k(\mathbf{p}) = \lambda_{k+1}(\mathbf{p})\}$ in parameter space. Per NQ-187 (sigma_theorem4_higher_order.md §4.4), the leading degeneracy at the first pitchfork on $D_4$ free-BC has $\lambda_0 = \lambda_1 = 4|W''(c)|\epsilon$ at $O(\epsilon)$ with splitting only at $O(\epsilon^2)$ (no $\epsilon^{3/2}$ term by $D_4$ polynomial equivariance).

**Type (iii): Peak creation/destruction events** at saddle-node thresholds.

A peak in $u^*$ at site $x$ (local maximum) can be created or destroyed as $\mathbf{p}$ varies when two sites satisfy $u^*(x;\mathbf{p}_*) = u^*(y;\mathbf{p}_*)$ for some neighbor $y \sim x$ — the saddle-node condition for the local-maximum predicate. At such a threshold: $\mathcal{F} \to \mathcal{F} \pm 1$ and $K$ may change by $\pm 1$ (a peak's associated Hessian soft mode enters/exits the O3 cutoff window). Type (iii) events form codimension-1 surfaces in $\mathbf{p}$-space. Distinct from Type (i): Type (i) is a bifurcation creating a new minimizer branch; Type (iii) is a peak-count change on an already-existing minimizer.

**Type (iv): σ-class transitions** between distinct $\mathrm{Aut}(G)$-orbits.

When an energy crossing occurs between two minimizers on distinct $\mathrm{Aut}(G)$-orbits — e.g., two local minima with different σ-tuples exchange their relative energy ordering — the σ-tuple of the global minimizer (if tracking the energy-minimum branch) changes discontinuously. On the fixed $D_4$ free-BC grid with its finite minimizer set, such energy crossings occur on codimension-1 hypersurfaces in $\mathbf{p}$-space. This is the only Type that is distinct from spectral/topological events; it is a *branching* event in the sense of Golubitsky–Schaeffer Vol. I §III.1 (orbit-type transition via equivariant symmetry breaking).

**Codimension table.**

| Type | Event | Codimension in $(\alpha,\beta,c)$-space |
|---|---|---|
| (i) | $\beta$ crosses $\beta_{\mathrm{crit}}^{(k)}$ (bifurcation) | 1 |
| (ii) | $\lambda_k(\mathbf{p}) = \lambda_{k+1}(\mathbf{p})$ (eigenvalue crossing) | 1 (generically) |
| (iii) | saddle-node for $\mathcal{F}$ (peak creation/destruction) | 1 |
| (iv) | energy crossing between orbits (σ-class transition) | 1 |

---

## §4. Cat A Claim — σ-trajectory Piecewise Constancy

**Claim BC-244-1 (σ-trajectory piecewise constancy, Cat A candidate).**

*On fixed graph $G$ with parameters $\mathbf{p} = (\alpha, \beta, c)$ in spinodal interior, the σ-tuple $\sigma(u^*(\mathbf{p}))$ is locally constant in the complement of a measure-zero stratified set $\mathcal{B}(G) \subset \mathbb{R}^3_{>0}$. The set $\mathcal{B}(G)$ is a finite union of smooth hypersurfaces (codimension-1 strata), one per transition type (i)–(iv). On each connected open component of $\mathbb{R}^3_{>0} \setminus \mathcal{B}(G)$, the σ-tuple is constant.*

**Proof sketch (Cat A path).**

1. By IFT (§1), $u^*(\mathbf{p})$ is smooth on each stratum.
2. By §2, all four σ-components are locally constant away from transition events.
3. Transition events of types (i)–(iv) are each codimension-1 by smooth-manifold arguments: (i) zeros of $\mu_k(\mathbf{p}) = 4\alpha\lambda_k^{\mathrm{Lap}} - \beta|W''(c)|$, a single equation in 3 parameters; (ii) zeros of $\lambda_k(\mathbf{p}) - \lambda_{k+1}(\mathbf{p})$, again codimension-1; (iii) zeros of $u^*(x;\mathbf{p}) - u^*(y;\mathbf{p})$ for specific pairs $x \sim y$; (iv) zeros of $\mathcal{E}(u_1^*;\mathbf{p}) - \mathcal{E}(u_2^*;\mathbf{p})$ for two distinct-orbit minimizers.
4. Finite graphs have finitely many pairs $\{x,y\}$ and finitely many orbit pairs, so $\mathcal{B}(G)$ is a finite union. Each component is a smooth hypersurface by the implicit function theorem (transversality holds generically per Sard's theorem applied to $\mathbf{p} \mapsto \Delta(\mathbf{p})$ where $\Delta$ is the relevant discriminant).
5. Hence $\mathbb{R}^3_{>0} \setminus \mathcal{B}(G)$ is open dense and σ is locally constant there. $\Box$

**Cat A status:** steps 1–4 are complete in principle; step 4's transversality requires a Sard-type genericity argument for each transition type on each finite graph. For the $D_4$ free-BC grid, the Type (i) and (ii) surfaces are explicit (§5 below). Types (iii) and (iv) require empirical verification per §7. **Full Cat A requires explicit enumeration of $\mathcal{B}(G)$ surfaces on a specific $G$ — Cat B for general $G$.**

---

## §5. Cat B Target — Bifurcation-Surface Enumeration on $D_4$ Free-BC

**Setup.** $G = D_4$ free-BC $L \times L$ grid, $L = 8$. Parameters $(\alpha, \beta, c)$ with $\alpha = 1$ (WLOG by rescaling), $c \in \mathcal{S}$, $\beta > 0$.

**Type (i) surfaces** — $\beta_{\mathrm{crit}}^{(k)}$ hypersurfaces in $(\beta, c)$-plane (fixing $\alpha = 1$):

$$\mathcal{B}_i^{(k)} = \left\{(\beta, c) : \beta = \frac{4\lambda_k^{\mathrm{Lap}}}{|W''(c)|}\right\}, \quad k = 2, 3, 4, \ldots$$

For $D_4$ free-BC $L \times L$ grid, the Laplacian eigenvalues are $\lambda_{pq}^{\mathrm{Lap}} = 4\sin^2(\pi p/(2L)) + 4\sin^2(\pi q/(2L))$ for $(p, q) \in \{0,\ldots,L-1\}^2$ (unnormalized, $p+q > 0$). The Fiedler value is $\lambda_2 = \lambda_{10} = 4\sin^2(\pi/(2L))$.

**Type (ii) surfaces** — eigenvalue-crossing loci. On the $D_4$ grid at the first pitchfork regime ($\beta$ near $\beta_{\mathrm{crit}}^{(2)}$):

By T-σ-Theorem-4 and NQ-187 (sigma_theorem4_higher_order.md §4.4), the eigenvalue split between the Fiedler-doublet modes is:
$$\lambda_1(\mathbf{p}) - \lambda_0(\mathbf{p}) = c_4(\alpha, c)\,\epsilon^2 + O(\epsilon^3), \quad \epsilon = \beta - \beta_{\mathrm{crit}}^{(2)},$$
where $c_4 = (B_4 - 12 B_3)|W''(c)|^2/(8A_1^2)$ depends on $\alpha, c$ through the sextic-coefficient slaving sums. The eigenvalue-crossing surface $\mathcal{B}_{ii}^{(12)}$ is thus $\epsilon = 0$ (the bifurcation surface itself) with a leading-order tangency — the crossing is approached as $O(\epsilon^2)$ splits open, not as a transverse crossing. This means the eigenvalue-crossing Type (ii) event at the first pitchfork is geometrically coincident with the Type (i) bifurcation surface, not an independent surface. **NQ-244-a (open):** are all Type (ii) surfaces on $D_4$ free-BC either coincident with Type (i) surfaces or isolated from them?

**σ-class count per stratum.** The parameter space $(\beta, c) \in (\beta_{\mathrm{crit}}^{(2)}, \infty) \times \mathcal{S}$ is partitioned into strata by $\mathcal{B}(G)$. Per BC-188-1 (NQ-188 sigma_uniqueness_theorem.md §6), the σ-class count is conjectured constant within each $\mathcal{F}$-fixed stratum. The NQ-244 contribution: within each stratum, the σ-tuple of the tracked minimizer $u^*(\mathbf{p})$ is exactly constant (not just σ-class count, but the full tuple).

**Number of strata on $L = 8$.** The critical values $\beta_{\mathrm{crit}}^{(k)}$ for $k = 2, 3, \ldots$ form a discrete sequence in $\beta$ (at fixed $c, \alpha$). On $L = 8$, there are $L^2 - 1 = 63$ non-trivial Laplacian eigenvalues, giving up to 63 Type (i) bifurcation surfaces and hence $\leq 63$ parameter strata in $\beta$. The actual number of distinct strata with different σ-tuples is smaller (multiple eigenvalues may coincide by $D_4$ symmetry).

**Cat B status.** Explicit enumeration of all $\mathcal{B}(G)$ surfaces on $L = 8$ requires: (a) computing all 63 Laplacian eigenvalues (trivial, closed form), (b) tracking which Type (iii)/(iv) crossings occur in each $\beta$-stratum (requires $\beta$-sweep experiment §7). **Cat B pending §7 empirical execution.**

---

## §6. Connection to OP-0008 — σ^A K-jump Non-determinism

**OP-0008** (canonical CV-1.5.1, registered 2026-04-29) concerns the non-determinism in σ^A K-jump events: when a multi-formation system ($K_{\mathrm{act}} > 1$) crosses a merge bifurcation, the post-merge σ^A is non-uniquely determined by the pre-merge σ-tuple.

**NQ-244 as single-formation template.** The present analysis provides the conceptual and computational template for the multi-formation analog:

1. **Single-formation IFT smooth family** (§1) $\leftrightarrow$ **K-coupled IFT smooth family**: replace $u^*(\mathbf{p}) \in \Sigma_m^\circ$ with $\mathbf{u}^*(\mathbf{p}) \in \widetilde{\Sigma}^{K_{\mathrm{field}},\circ}_M$ (Commitment 14-Multi-Static, canonical line 1218). The Hessian $H(\mathbf{u}^*)$ for the multi-formation system has an off-block-diagonal coupling $O(\exp(-c_0 D_{\mathrm{sep}}))$ in the well-separated regime (T-σ-multi-A-Static).
2. **Type (i) bifurcation events** $\leftrightarrow$ **K-jump events**: a K-jump (formation merge or birth) is the multi-formation analog of a Type (i) bifurcation in the single-formation σ-trajectory. The non-determinism of OP-0008 arises because the post-K-jump minimizer branch is not uniquely selected by the σ^A pre-jump value — this is the K-coupled version of the branch-selection problem at Type (i) events.
3. **σ-trajectory piecewise constancy** (§4) $\leftrightarrow$ **σ^A piecewise constancy between K-jumps**: the K-coupled σ^A is conjectured locally constant between K-jump events, by the same IFT + integer-constancy argument applied to the block-diagonal Hessian in the well-separated regime.

**Deferred to W7+.** The K-coupled analog of NQ-244 is registered as the multi-formation σ-trajectory problem (NQ-242, referenced in canonical CV-1.5.1 as the "D-6b path"). The W7+ extension requires: (a) well-separated-regime IFT for K-field minimizers; (b) catalog of K-jump surface types (merge bifurcation, formation death, formation birth); (c) non-determinism mechanism for σ^A post-jump.

---

## §7. Empirical Anchor — $\beta$-Sweep Experiment Design

**Experiment NQ-244-sweep.** $D_4$ free-BC $L = 8$ grid, $\alpha = 1$, $c = 0.5$ (spinodal interior), $\beta \in [\beta_{\mathrm{crit}}^{(2)} + 0.1,\; 50]$ with 50 evenly spaced values.

**Protocol.**
1. For each $\beta_j$, initialize from a small-amplitude Fiedler perturbation: $u_{\mathrm{init}} = 0.5 \cdot \mathbf{1} + \epsilon_{\mathrm{init}} \phi_{(1,0)}$ with $\epsilon_{\mathrm{init}} = 0.01$.
2. Run `find_formation(g, p)` (CODE/scc/optimizer.py) to convergence; obtain $u^*(\beta_j)$.
3. Compute $\sigma(u^*(\beta_j))$: Hessian $H = 4L_G + \beta_j W''(u^*)\,\mathrm{diag}$; diagonalize on $\mathbf{1}^\perp$; assign $(n_k, [\rho_k], \lambda_k)$ per Commitment 14 (O5)(O5')(O7).
4. Record $\mathcal{F}(u^*(\beta_j))$ via local-maxima count.
5. For each consecutive pair $(\beta_j, \beta_{j+1})$: compare σ-tuples component-by-component; flag any change as a transition event and classify by type (i)–(iv).

**Expected output.** A list of $\leq 50$ σ-tuples along the $\beta$-sweep, with transition events identified at their $\beta$ locations. Expected transitions:
- Type (i) at $\beta_{\mathrm{crit}}^{(2)}, \beta_{\mathrm{crit}}^{(3)}, \ldots$ (closed-form from Laplacian eigenvalues).
- Type (iii) between consecutive bifurcations (peak creation events as the formation grows).
- Type (ii) possibly coincident with Type (i) at leading order (NQ-244-a).
- Type (iv) rare on $L = 8$ with low $\mathcal{F}$.

**Deliverable.** `CODE/scripts/sigma_trajectory_sweep.py` + JSON `CODE/scripts/results/sigma_trajectory_L8.json`. Anchors §4 piecewise-constancy claim Cat A at $L = 8$.

---

## §8. Cat Targets

**Cat A — σ-trajectory piecewise constancy (§4 BC-244-1).**
- Full Cat A on $D_4$ free-BC $L = 8$: direct σ-tuple computation at 50 $\beta$-points (§7) + enumeration of transition events. Confirm each event is one of types (i)–(iv) and occurs on a codimension-1 surface.
- Effort: 1 week (§7 experiment + classification).

**Cat B — bifurcation-surface enumeration on $D_4$ free-BC (§5).**
- Enumerate all Type (i)–(iv) surfaces in $(\alpha, \beta, c)$-space for $L = 8$.
- Count σ-classes per parameter stratum; compare with NQ-188 BC-188-1 (parameter-independence conjecture).
- Requires: §7 sweep + additional $(c, \alpha)$ sweep at 2–3 values to confirm surface geometry.
- Effort: 3–4 weeks. **Cat B** (empirical verification needed for Types (iii)/(iv) surfaces; Types (i)/(ii) are analytically determined).

**Cat C — universality of σ-trajectory structure across graph classes.**
- Does the piecewise-constancy result and the four-type transition catalog hold for non-$D_4$ graphs (torus, hexagonal lattice, random regular)?
- Linked to NQ-188 BC-188-2 (universality) and NQ-190 (topological invariance).
- Effort: 4–6 weeks (requires replication on 2–3 additional graph classes). **Cat C** (speculative; requires NQ-190b continuum-limit machinery).

---

## §9. External References (Contrastive, CN10)

The following references provide *parallel smooth-manifold structure* contrasting with the SCC discrete-graph σ-trajectory. They are not used reductively.

- **Crandall, M. G., Rabinowitz, P. H.** (1971). "Bifurcation from simple eigenvalues." *J. Funct. Anal.* 8, 321–340. — Canonical parametric-bifurcation theorem for simple eigenvalue crossings in Banach spaces. Contrastive parallel: the SCC T-Birth-Parametric (Cat A, canonical §13 line 1416) is the discrete-graph specialization of C–R; the smooth-manifold bifurcation surface $\beta = \beta_{\mathrm{crit}}^{(k)}$ is the exact analog of C–R's "simple eigenvalue crossing."
- **Sattinger, D. H.** (1979). *Group Theoretic Methods in Bifurcation Theory*. LNM 762, Springer. — Equivariant Crandall–Rabinowitz framework under finite symmetry groups; isotropy lattice approach. Contrastive parallel: T-σ-Theorem-4's $D_4$-equivariant structure and the irrep-label assignment at bifurcation (Type (i) events) follow the isotropy-lattice logic of Sattinger Ch. IV. Used in `working/SF/symmetry_moduli.md` §3 (R22).
- **Golubitsky, M., Schaeffer, D. G.** (1985). *Singularities and Groups in Bifurcation Theory*, Vol. I. Springer. — Equivariant singularity theory; $D_4$ orbit-decomposition lattice (Ch. VI). Contrastive: the Type (iv) σ-class transition (energy crossing between $\mathrm{Aut}(G)$-orbits) is parallel to orbit-type transitions in the Golubitsky–Schaeffer isotropy stratification.
- **Golubitsky, M., Stewart, I., Schaeffer, D. G.** (1988). *Singularities and Groups in Bifurcation Theory*, Vol. II. Springer. — Multi-parameter bifurcation theory; mode-interaction normal forms. Contrastive: §5's Type (ii) eigenvalue-crossing surfaces are mode-interaction loci in the sense of Vol. II Ch. XV; the $D_4$ mode-coupling coefficient $A_2/A_1 = 4$ (R22 Cat A) is the key mode-interaction parameter.

---

## §10. W6+ Priority and Open Problem Registration

**W6 priority.** The §7 empirical sweep ($L = 8$, 50 $\beta$-points) is the single most valuable deliverable: it anchors BC-244-1 as Cat A at small scale and produces the empirical bifurcation-surface map feeding §5's Cat B target.

**W7+ priority.** Cat B bifurcation-surface enumeration on $D_4$ $L = 8$ and Cat C cross-graph generalization.

**Multi-formation extension.** σ^A K-jump non-determinism (OP-0008) is the K-coupled analog of NQ-244. The conceptual template (IFT smooth family, piecewise constancy, four transition types) extends directly; the additional technical ingredient is the off-block-diagonal coupling in the multi-formation Hessian. Resolution requires NQ-242 (sigma_multi_trajectory.md Cat B framework, canonical CV-1.5.1 reference).

**Open problems registered.**

- **NQ-244-a.** Are all Type (ii) eigenvalue-crossing surfaces on $D_4$ free-BC either geometrically coincident with Type (i) bifurcation surfaces (at leading order) or isolated from them? (§5 discussion; W6 scope.)
- **NQ-244-b.** On $D_4$ free-BC $L = 8$, what is the exact number of parameter strata with distinct σ-tuples in $(\alpha, \beta, c)$-space? (§5 Cat B; W6 empirical scope.)
- **NQ-244-c.** Is the four-type transition catalog (i)–(iv) exhaustive — i.e., does every σ-trajectory transition on a finite graph fall into exactly one of the four types? Or are there mixed-type events at codimension-2 intersections? (W7+ scope.)
- **NQ-244-d.** Does BC-244-1's piecewise-constancy extend to the multi-formation σ^A trajectory between K-jump events, in the well-separated regime? (OP-0008 extension; W7+ scope via NQ-242.)

**Connection to open problems (not resolved):** F-1, M-1, MO-1 are not touched by NQ-244. MO-1 (stratified Morse on $\Sigma^K_M$) would be re-engaged only in the K-coupled σ^A extension (NQ-244-d, W7+, requiring NQ-242 + NQ-248 full corner handling).

---

## §11. Cross-References

- **Canonical §11.1 Commitment 14 (line 790, CV-1.5.1)**: σ-tuple definition with (O5')(O7) tie-breaking; §2 above analyzes continuity of each component of this definition.
- **Canonical §13 T-σ-Lemma-1 (line 1257)**: irrep decomposition well-definedness; anchors §2.3 continuity of $[\rho_k]$.
- **Canonical §13 T-σ-Lemma-2 (line 1277)**: nodal-count properties; anchors §2.2 continuity of $n_k$.
- **Canonical §13 T-σ-Lemma-3 (line 1301)**: Goldstone-$\ell = 1$ angular saturation; relevant to Type (iii) peak-creation events on translation-invariant graphs where Goldstone modes are near-zero.
- **Canonical §13 T-σ-Theorem-3 (line 1334)**: σ at uniform critical point; baseline for $\mathcal{B}_i^{(k)}$ Type (i) surface computation (§5).
- **Canonical §13 T-σ-Theorem-4 (line 1377, Cat B)**: σ at first pitchfork; provides the $\epsilon$-small regime σ-tuple that is perturbed in §1; the O(ε²) splitting (NQ-187) determines Type (ii) surface structure near the first bifurcation.
- **`working/SF/sigma_uniqueness_theorem.md` (NQ-188)**: σ-class discrete catalog and BC-188-1 parameter-independence conjecture. NQ-244 BC-244-1 is the stronger statement that the full σ-tuple (not just σ-class count) is piecewise constant; BC-244-1 implies BC-188-1 within each $\mathcal{F}$-fixed stratum.
- **`working/SF/sigma_topological_invariance.md` (NQ-190)**: graph-isomorphism invariance (Cat A) and subdivision non-invariance. NQ-244 is parameter-space perturbation (fixed $G$); NQ-190 is graph-topology perturbation (fixed $\mathbf{p}$). Orthogonal analyses.
- **`working/SF/sigma_theorem4_higher_order.md` (NQ-187)**: ε² splitting at first pitchfork; establishes that Type (ii) events near the first pitchfork coincide with Type (i) at leading order ($c_4 \epsilon^2$ splitting opens from the bifurcation surface, not from a separate crossing surface). Directly feeds §5's Type (ii) surface structure.
- **OP-0008 (σ^A K-jump non-determinism, canonical CV-1.5.1)**: multi-formation extension of NQ-244; §6 above provides the explicit conceptual bridge.

---

**End of working file.**
**Lines:** ~340. **Status:** Working draft, Cat A/B/C demarcated. **Author:** Executor (NQ-244 spawn, 2026-04-30).
**Promotion target:** §4 BC-244-1 → Cat A via §7 empirical sweep (W6); §5 bifurcation-surface enumeration → Cat B (W6 extended); §8 cross-graph → Cat C open conjecture (W7+).
