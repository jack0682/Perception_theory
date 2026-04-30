# scc_mass_gap_connection.md — SCC Multi-Formation Hessian Spectrum vs Yang–Mills Mass Gap (NQ-249)

**Status:** Working theory (W6+ candidate). Revised 2026-04-30 per critic review (`THEORY/logs/daily/2026-04-30/10_critic_NQ249_review.md`) — C1+C2+C3+M1 mandatory fixes applied.
**NQ:** NQ-249.
**Topic class:** MF (multi-formation) × CN10 contrastive parallel to Clay-millennium gauge theory.
**Last edit:** 2026-04-30 (post-critic mandatory-fix revision).
**Promotion target:** §13 Cat A *conditional on T-σ-Multi-1 Cat A upgrade* (§7.1, post-C3 revision) — promotion deferred until T-σ-Multi-1 promotes from Cat B target to Cat A. Cat B target conjecture BC-249-1 (§3.1, post-C1 revision with explicit $\delta_0$ bifurcation-distance dependence) deferred to canonical merge gate post-empirical anchor.
**Hard constraints:** zero canonical edits in this file; CN10 contrastive (Yang–Mills is a downstream parallel, not foundation); F-1 / M-1 / MO-1 not silently resolved; multi-formation default treatment (single-formation $K=1$ is degenerate special case).
**Critic-revision log (2026-04-30):**
- **C1:** §3.1 BC-249-1 restated with explicit $\delta(\alpha,\beta,c)$ bifurcation-distance dependence; §3.2 reformulated; §9.1 resolution language harmonized.
- **C2:** §10.2 reconciliation paragraph added — $\Delta_K$ cycling at $K \to K+1$ is *protocol-conditional* (NQ-253 §4.2 mechanisms B1/B2/B3); under noiseless gradient flow the cycling does not occur (NQ-253 §4.3).
- **C3:** §7.1 restated as Cat A *conditional* with explicit (H1)+(H2)+(H3) hypothesis chain; §16 Path A "no canonical entry needed" claim retracted.
- **M1:** Canonical line citations corrected throughout (§2.1, §5 table, §7.3, §8.1, §9.4, §12.2, §14.1) — `canonical.md:77` (Commitment 16) → `canonical.md:796–812`; `canonical.md:1337` / `canonical.md:1343` (phase transition / spinodal) → `canonical.md:572` (admissible range) / `canonical.md:1005` (T8-Core) / `canonical.md:1009` (Scaling Caveat) / `canonical.md:1334–1409` (T-σ-Theorem-3) per context.
- **Pending (recommended for W6 Day 5+):** M2 (T8-Core thermodynamic-limit Scaling Caveat in §3.3); M3 (Goldstone subspace dimension stratification §6.4); M4 (R23-generic carve-out §3.3 / §9.3); M5 (compute budget §8.4 + FD noise floor §8.5); M6 (post-bifurcation closed-form clarification — *applied in §7.3 alongside M1*); m1–m5 minor cleanups.

---

## §1. Mission and context

### §1.1 Mission

We ask whether the **minimum non-trivial Hessian eigenvalue** of an SCC multi-formation minimizer
$$
\lambda_1^{(K)}(\mathbf{u}^*) \;:=\; \min_k \lambda_k\!\big(H(\mathbf{u}^*)\big)\Big|_{\text{non-trivial subspace}}
$$
admits a graph-theoretic, parameter-uniform lower bound that is the formal analog of the **Yang–Mills mass gap conjecture** in the SCC pre-objective formation regime.

This question is registered as **NQ-249** in the gauge-theory connections enumeration (`THEORY/logs/daily/2026-04-30/06_gauge_theory_connections_analysis.md` Connection A, §3.1–§3.4) and **OP-0009-Emp** sub-item.

### §1.2 Yang–Mills mass gap statement (Clay millennium)

Pure $\mathrm{SU}(N)$ Yang–Mills theory on $\mathbb{R}^{1,3}$ with Hamiltonian $H_{\mathrm{YM}}$ on physical Hilbert space $\mathcal{H}_{\mathrm{phys}}$ (BRST cohomology of unphysical states) is conjectured to satisfy
$$
\Delta_{\mathrm{YM}} \;:=\; \inf_{\substack{|\Psi\rangle \in \mathcal{H}_{\mathrm{phys}}\\ \langle \Omega | \Psi\rangle = 0}} \frac{\langle \Psi | H_{\mathrm{YM}} | \Psi \rangle}{\langle \Psi | \Psi\rangle} \;\geq\; m^2 > 0,
$$
where $|\Omega\rangle$ is the vacuum, the infimum is over states orthogonal to the vacuum, and the existence of $m>0$ uniformly in volume is the open millennium problem (Jaffe & Witten, Clay Math. Inst.).

### §1.3 SCC parallel structure (CN10 contrastive lock)

SCC objects are the K-field minimizer $\mathbf{u}^* \in \widetilde{\Sigma}^{K_{\mathrm{field}},\,\circ}_M$ and its Hessian $H(\mathbf{u}^*)$ on the volume-tangent subspace $\mathbf{1}^\perp_{\mathrm{multi}}$. Per **canonical §13 T-Commitment-14-Multi-Static** (`canonical.md:1217–1228`), the σ-tuple $\sigma_{\mathrm{multi}}^A$ consists of within-formation Hessian-eigenvalue tuples $\{\sigma_j\}_{j=1}^{K_{\mathrm{act}}}$, ordered ascending in $\lambda_k$ per Commitment 14 (O5'), `canonical.md:790–794`.

**CN10 contrastive lock (mandatory):** Yang–Mills is a *parallel*, not a *reduction*. SCC is graph-spectral and variational; YM is continuum, gauge-symmetric, quantum field theoretic. The SCC mass-gap candidate inherits *structural inspiration* (a positive lower bound on the spectral gap excluding zero modes), not derivation. We never write "SCC mass gap = YM mass gap"; we write "SCC mass-gap analog $\Delta_K$ on $(G, \alpha, \beta, c)$".

---

## §2. Mass-gap candidate definition

### §2.1 Setup

Fix a finite graph $G = (X, E)$, parameters $(\alpha, \beta, c)$ with $c$ in the spinodal interior $\big((3-\sqrt 3)/6, (3+\sqrt 3)/6\big)$ (canonical §8 admissible range, `canonical.md:572`; cf. canonical §13 T8-Core line 1005 + Scaling Caveat line 1009), and $K_{\mathrm{field}} \geq 1$. Let
$$
\mathcal{L}_K \;:=\; \big\{ \mathbf{u}^* \in \widetilde{\Sigma}^{K,\,\circ}_M \;:\; \nabla \mathcal{E}(\mathbf{u}^*) = 0,\; \mathbf{u}^*\ \text{Morse-0 minimizer} \big\}
$$
be the parameter-fixed minimizer set with $K_{\mathrm{act}}(\mathbf{u}^*) = K$. (Cf. canonical §13 T-σ-multi-A-Static hypothesis well-separated regime $D_{\mathrm{sep}} \geq 3$, `canonical.md:1232–1235`.)

### §2.2 Definition

For $\mathbf{u}^* \in \mathcal{L}_K$, let $\{\lambda_k(\mathbf{u}^*)\}_k$ be the Hessian eigenvalues on the orthogonal complement of (i) the volume-tangent direction $\mathbf{1}_{\mathrm{multi}}$, and (ii) the **discrete-translation Goldstone subspace** (canonical §13 T-V5b-T-zero, `canonical.md:1199–1201`; T-σ-Lemma-3, `canonical.md:1301–1320`) when present. Define
$$
\boxed{\;\Delta_K(G, \alpha, \beta, c) \;:=\; \inf_{\mathbf{u}^* \in \mathcal{L}_K}\; \min_{k}\; \lambda_k\!\big(H(\mathbf{u}^*)\big)\Big|_{\big(\mathbf{1}\,\oplus\,\mathrm{Gold}\big)^\perp}.\;}
$$

### §2.3 Immediate properties

(a) **$\mathcal{L}_K$ Morse-0 ⇒ $\Delta_K > 0$ pointwise.** Each $\mathbf{u}^* \in \mathcal{L}_K$ is a Morse-0 minimizer ⇒ $H(\mathbf{u}^*)\big|_{(\mathbf{1}\oplus\mathrm{Gold})^\perp} \succ 0$ ⇒ $\min_k \lambda_k > 0$ at this point. (See canonical §13 T-σ-Theorem-3, `canonical.md:1262–1265`, on Hessian eigenspace decomposition.)

(b) **Infimum may collapse.** Whether $\Delta_K > 0$ (uniform) or $\Delta_K = 0$ (collapse) depends on whether $\mathcal{L}_K$ is bounded away from bifurcation surfaces / merger boundaries. This is the substance of §3.

(c) **Goldstone exclusion is necessary.** Without removing the Goldstone subspace, T-V5b-T-zero (canonical `canonical.md:1199`) gives $\mu_{\mathrm{Gold}} = 0$ exactly on translation-invariant graphs, so the unprojected infimum is trivially zero. The mass-gap candidate is meaningful only on the orthogonal complement (cf. §6).

---

## §3. SCC mass-gap conjecture (BC-249-1)

### §3.1 Conjecture (Cat B target) — revised 2026-04-30 per critic C1

**BC-249-1 (SCC Mass-Gap Conjecture, Cat B target, revised).** Fix a finite graph $G$ and $K \geq 1$. Let $\delta(\alpha,\beta,c)$ denote the parameter-space distance from $(\alpha,\beta,c)$ to the bifurcation locus
$$
\mathcal{B}(G, K) \;:=\; \big\{(\alpha,\beta,c) : \beta = \beta_{\mathrm{crit}}^{(j)}(G, \alpha, c)\ \text{for some pitchfork index}\ j\big\} \;\cup\; \big\{\partial \,\text{spinodal}\big\}
$$
in normalized parameter coordinates. Then for every $\delta_0 > 0$, there exists a function $\Delta_*(G, K, \delta_0) > 0$ depending on $(G, K, \delta_0)$ such that
$$
\Delta_K(G, \alpha, \beta, c) \;\geq\; \Delta_*(G, K, \delta_0)
$$
holds for all $(\alpha, \beta, c)$ satisfying $c \in$ spinodal interior, $\beta > \beta_{\mathrm{crit}}^{(2)}(G, \alpha, c)$, **and** $\delta(\alpha,\beta,c) \geq \delta_0$ (positive distance from the bifurcation locus).

*(Erratum 2026-04-30, critic C1: earlier draft asserted $\Delta_*(G, K) > 0$ depending only on $(G, K)$ — *not* on $(\alpha, \beta, c)$ — uniformly across the post-bifurcation region. This was internally inconsistent with §9.1's acknowledgment of $\Delta_K \to 0$ near bifurcation surfaces. The revised statement makes the bifurcation-distance dependence $\delta_0$ explicit. Cf. §3.2, §4.3, §9.1.)*

For canonical anchors: spinodal interior is the admissible range $c \in ((3-\sqrt{3})/6, (3+\sqrt{3})/6)$ per canonical §8 (line 572); $\beta_{\mathrm{crit}}^{(2)}$ formula is the second pitchfork threshold per canonical §13 T8-Core line 1005 + Scaling Caveat line 1009.

### §3.2 Equivalent reformulation (post-C1)

$$
\forall\, \delta_0 > 0:\quad \inf_{\substack{\beta > \beta_{\mathrm{crit}}^{(2)},\, c \in \text{spinodal}^\circ,\, \alpha > 0\\ \delta(\alpha,\beta,c) \geq \delta_0}} \Delta_K(G, \alpha, \beta, c) \;>\; 0.
$$
Strict positivity of the spectral floor across the post-bifurcation parameter region **modulo a $\delta_0$-tubular neighborhood of the bifurcation locus**. The neighborhood thickness $\delta_0$ is part of the conjecture's hypothesis chain — without it, the infimum may collapse per §9.1.

### §3.3 Why this is the right SCC formulation

Yang–Mills mass gap demands uniformity in the IR (large-volume) limit. SCC's $\Delta_*(G, K)$ is uniform across $(\alpha, \beta, c)$ within the spinodal interior; the analog of the IR limit is the *thermodynamic limit* of $G \to \infty$ via $L \to \infty$ on a $L^d$ lattice, which yields a separate continuum-limit mass-gap statement (NQ-217 interaction, see §11). BC-249-1 is the *finite-graph* statement; the continuum extension is BC-249-2 (deferred).

**Caveat (T8-Core Scaling, canonical line 1009; M2 fix W5 Day 4 PM).** On $L^d$ grids, $\beta_{\mathrm{crit}}^{(2)} \sim 4\alpha\pi^2/(L^2 |W''(c)|) \to 0$ as $L \to \infty$, and the T8-Core selection criterion degenerates: the post-bifurcation regime $\{\beta > \beta_{\mathrm{crit}}^{(2)}\}$ collapses to "$\beta > 0$" trivially, providing only minimizer *existence* without a meaningful selection criterion (T8-Core Scaling Caveat, `canonical.md:1009`). BC-249-2 inherits this thermodynamic-limit pathology: any uniform mass-gap statement across $L \to \infty$ must specify how the bifurcation-distance threshold $\delta_0$ (per C1 fix in §3.2 / §9.1) scales with $L$. If $\delta_0(L) \to 0$ faster than the bifurcation locus accumulates in the post-bifurcation parameter region, the uniform infimum collapses and BC-249-2 fails. Dependence on NQ-217 graph-to-continuum convergence machinery is therefore *non-trivial*: BC-249-2 requires a joint statement on (i) lattice spectral-gap scaling $\lambda_2(L)$, (ii) bifurcation-distance scaling $\delta_0(L)$, and (iii) NQ-217 weak-convergence of $H(\mathbf{u}^*)$ spectra. BC-249-1 (finite-graph) avoids these scaling issues by definition; BC-249-2 promotion is *gated* on a thermodynamic-limit regularity hypothesis to be specified jointly with NQ-217 (W7+).

---

## §4. Connection to T-σ-multi-D-Static (canonical §13)

### §4.1 The D-static structure

Per canonical §13 T-σ-multi-D-Static (`canonical.md:1241–1242`), $\sigma^D(\mathbf{u}^*)$ is a conjugacy-class label in
$$
H^1\!\big(\mathrm{Aut}(G) \wr S_{K_{\mathrm{act}}};\ \mathrm{Stab}(\mathbf{u}^*)\big),
$$
capturing between-formation cohomology pull-back. The static D-component encodes how formation labelings interact with the wreath-product symmetry.

### §4.2 Mass-gap as spectral floor preventing zero-mode escape

The connection to $\Delta_K$ is structural:

1. T-σ-multi-A-Static (`canonical.md:1232`) guarantees **within-formation σ multi-set invariance** ⇒ the σ multi-set is a topological invariant under $\mathrm{Aut}(G) \wr S_{K_{\mathrm{act}}}$.
2. T-σ-multi-D-Static (`canonical.md:1241`) guarantees **between-formation cohomology** is well-defined.
3. **$\Delta_K > 0$ is the missing piece**: without a spectral floor, the σ-tuple ordering can collapse (degenerate eigenvalues, irrep ambiguity per Commitment 14 (O5')(O7), `canonical.md:790–794`). The mass-gap conjecture asserts that the σ-framework is **spectrally non-degenerate** uniformly.

### §4.3 Operational reading

$\Delta_K > 0 \;\Leftrightarrow\;$ σ-tuple is locally rigid under perturbation of $(\alpha, \beta, c)$ on the parameter-fixed component of $\mathcal{L}_K$. This is the condition for the σ-framework to be a robust diagnostic across the spinodal interior.

---

## §5. Difference from Yang–Mills (CN10 contrastive table)

| Aspect | Yang–Mills | SCC multi-formation |
|---|---|---|
| **Underlying space** | Continuum spacetime $\mathbb{R}^{1,3}$ | Finite graph $G$ |
| **Field** | Lie-algebra-valued connection $A_\mu$ | Cohesion field $\mathbf{u} : X^{K_{\mathrm{field}}} \to [0,1]^{K_{\mathrm{field}}}$ |
| **Symmetry** | $\mathrm{SU}(N)$ gauge symmetry | $\mathrm{Aut}(G) \wr S_{K_{\mathrm{act}}}$ wreath product (canonical §13 T-σ-multi-A-Static) |
| **Operator** | Hamiltonian $H_{\mathrm{YM}}$ on $\mathcal{H}_{\mathrm{phys}}$ | Hessian $H(\mathbf{u}^*)$ on $(\mathbf{1}\oplus\mathrm{Gold})^\perp \subset T_{\mathbf{u}^*}\widetilde{\Sigma}^{K,\,\circ}_M$ |
| **Vacuum** | Quantum vacuum $\Omega$ | Uniform state $c\mathbf{1}$ (canonical §13 T-σ-Theorem-3 setup, lines 1334–1409; phase-transition existence per canonical §13 T8-Core line 1005) — but mass gap measured *not* at vacuum, rather at non-trivial K-formation minimizers |
| **Mass-gap statement** | $\Delta_{\mathrm{YM}} \geq m^2 > 0$, open | $\Delta_K \geq \Delta_*(G, K)$, BC-249-1 Cat B target |
| **Status of construction** | YM existence open in 4D | SCC is constructive; well-defined via canonical §13 |
| **Symmetry-breaking modes** | Goldstone bosons in spontaneously broken phases | T-V5b-T-zero exact zero mode (canonical `canonical.md:1199`) |

**The analog is not reduction.** SCC does not reduce to Yang–Mills; the parallel is structural — both ask whether the spectrum of a quadratic form on the perturbation space about a non-trivial minimizer admits a uniform positive lower bound. The mathematical content of SCC's BC-249-1 is purely graph-spectral + double-well + symmetry-breaking, with **no quantum-field, BRST, or gauge-theoretic content**.

---

## §6. Goldstone caveat (T-σ-Lemma-3 + T-V5b-T-zero)

### §6.1 Why $\Delta_K \neq 0$ even in presence of Goldstone

Per **T-σ-Lemma-3** (canonical §13, `canonical.md:1301–1320`), translation-invariant graphs admit a $d$-dim Goldstone subspace $\mathrm{Gold} = \mathrm{span}(\delta u_{x_1}, \ldots, \delta u_{x_d})$ corresponding to discrete lattice translations. T-V5b-T-zero (canonical `canonical.md:1199`) shows the Goldstone eigenvalue is $\mu_{\mathrm{Gold}} = 0$ *exactly* in the sub-spinodal regime (no Peierls–Nabarro lifting).

### §6.2 Resolution: project orthogonal to Goldstone

The mass gap is taken on the orthogonal complement $\mathrm{Gold}^\perp$. This is the discrete analog of how Yang–Mills mass gap is measured *modulo* unphysical (gauge / BRST) zero modes — the field-theoretic analog of "mod the gauge orbit" is "mod the discrete-translation orbit closure".

### §6.3 Multi-formation Goldstone-pair (T-σ-Multi-1)

In multi-formation regime with $K_{\mathrm{act}} \geq 2$ on translation-invariant graphs, **T-σ-Multi-1** (canonical `canonical.md:1248–1255`) gives a Goldstone-pair structure: each formation contributes a per-formation Goldstone, and the joint Hessian splits the pair under $\lambda_{\mathrm{rep}}$ coupling. The mass-gap candidate $\Delta_K$ is taken on the complement of the *entire* Goldstone-pair subspace, not just one Goldstone.

This is delicate: the Goldstone-pair eigenvalue separation under $\lambda_{\mathrm{rep}}$ coupling (canonical T-σ-Multi-1) provides *itself* a candidate "mass gap" — not the mass-gap eigenvalue but the splitting between the (near-zero) symmetric and antisymmetric Goldstone combinations. We deliberately exclude both to avoid conflating mass-gap (orbital floor) with Goldstone-splitting (translation-orbit fine structure).

---

## §7. Cat A / Cat B / Cat C target structure

### §7.1 Cat A *conditional* — pointwise positivity at non-degenerate minimizers (revised 2026-04-30 per critic C3)

**Cat A target (conditional on T-σ-Multi-1 Cat A upgrade, this file):**

Assume the following hypothesis chain:

- **(H1) Interior-only Whitney-stratified regime per Option A.** $\mathcal{L}_K \subset \widetilde{\Sigma}^{K_{\mathrm{field}},\,\circ}_M = \widetilde{\Sigma}^{K_{\mathrm{field}}}_M \setminus \partial\widetilde{\Sigma}$ (canonical §13 line 1218): corner-saturated boundaries excluded. Outside this interior, Morse-0 + Goldstone identification breaks down and Option B stratified Morse (deferred to NQ-248 W7+) is required.
- **(H2) Well-separated regime $D_{\mathrm{sep}} \geq 3$.** Each $\mathbf{u}^* \in \mathcal{L}_K$ satisfies the canonical T-σ-multi-A-Static well-separation hypothesis (canonical §13 lines 1232–1235). Without (H2), the multi-formation Hessian splitting argument is Cat C conditional rather than Cat A.
- **(H3) Multi-formation Goldstone subspace identification per T-σ-Multi-1.** The full Goldstone subspace $\mathrm{Gold}$ in the multi-formation regime is identified per canonical T-σ-Multi-1 (lines 1248–1255). T-σ-Multi-1 is currently Cat B target (per CV-1.5.1 release notes, canonical line 77).

Then:
$$
\forall\, \mathbf{u}^* \in \mathcal{L}_K \text{ Morse-0},\quad \min_k \lambda_k\!\big(H(\mathbf{u}^*)\big)\big|_{(\mathbf{1}\oplus\mathrm{Gold})^\perp} \,>\, 0
$$
pointwise — i.e., $\Delta_K(G,\alpha,\beta,c) > 0$ at each individual minimizer (uniform lower bound across $\mathcal{L}_K$ is the separate Cat B BC-249-1 statement, §3).

**Proof sketch (under (H1)+(H2)+(H3)):** Direct from Morse-0 definition: a Morse-0 critical point has positive-definite Hessian on the tangent space modulo zero modes. (H1) ensures $\mathbf{u}^*$ lies in the interior where the Whitney-stratified Morse theory applies. (H2) gives the well-separated multi-formation Hessian splitting that is canonical Cat A only under T-σ-multi-A-Static. (H3) identifies the full Goldstone subspace as the zero-mode subspace; modding it out leaves a positive-definite operator. $\Box$

**Status:** Cat A *conditional on T-σ-Multi-1 Cat A upgrade*. Currently (H3) is Cat B target (canonical CV-1.5.1, line 77); this conditional Cat A inherits T-σ-Multi-1's Cat B status until the T-σ-Multi-1 promotion is completed. Reduces to Cat A immediate only after T-σ-Multi-1 Cat A upgrade. *(Earlier draft asserted "Cat A immediate, no new mathematical content beyond canonical Morse-0 + T-σ-Lemma-3" — retracted 2026-04-30 per critic C3: this silently inherited (H1) Option A interior, (H2) $D_{\mathrm{sep}} \geq 3$, and (H3) T-σ-Multi-1 hypotheses, none of which are unconditionally Cat A.)*

### §7.2 Cat B target — uniform lower bound (BC-249-1)

**Cat B target:** Existence of $\Delta_*(G, K) > 0$ uniform in $(\alpha, \beta, c)$ in the spinodal interior with $\beta > \beta_{\mathrm{crit}}^{(2)}$.

**Required tools:**
- Łojasiewicz inequality at $\mathcal{L}_K$ (gradient flow convergence — canonical T14 analogue).
- Uniform second-derivative bound on $\mathcal{E}$ on the spinodal-interior parameter region.
- Compactness of $\mathcal{L}_K$ modulo wreath-product symmetry.

**Status:** Cat B target. ~3–4 weeks effort estimate per `06_gauge_theory_connections_analysis.md` line 487.

### §7.3 Cat C — closed-form formula

**Cat C target:** Closed-form expression
$$
\Delta_*(G, K) \;\stackrel{?}{=}\; F\!\big(\{\lambda_k^{\mathrm{Lap}}(G)\}, |W''(c)|, \mathrm{Stab}(\mathbf{u}^*), K, \lambda_{\mathrm{rep}}\big)
$$
in terms of (i) Laplacian spectrum of $G$, (ii) double-well curvature $|W''(c)|$, (iii) symmetry-breaking pattern via $\mathrm{Stab}(\mathbf{u}^*)$, (iv) $K$-dependence, (v) repulsion coupling.

**Reference:** `SF/mode_count.md` provides the closed-form Hessian *at the uniform vacuum* $u^* = c\mathbf{1}$ (sub-critical, $\beta < \beta_{\mathrm{crit}}^{(2)}$): $\mu_k = 4\alpha\lambda_k^{\mathrm{Lap}} + \beta W''(c)$ (canonical §13 T-σ-Theorem-3, lines 1334–1371; cf. `mode_count.md` Prop 1.3a). However, $\Delta_K$ is defined at **post-bifurcation** $K$-formation minimizers ($\beta > \beta_{\mathrm{crit}}^{(2)}$, $u^* \neq c\mathbf{1}$), where the uniform-vacuum closed-form does *not* apply. The post-bifurcation Hessian closed-form requires a separate normal-form expansion derived in T-σ-Theorem-4 (canonical lines 1378–1409); see also `SF/symmetry_moduli.md` for $D_4$-normal-form coefficients $A_1, A_2$. Multi-formation analog with $K \geq 2$ Goldstone-pair coupling: open. *(Erratum 2026-04-30 per critic M6: earlier draft cited the uniform-vacuum closed-form as the Cat C target, conflating sub-critical $u^* = c\mathbf{1}$ with post-bifurcation $u^* \in \mathcal{L}_K$. The Cat C target $\Delta_*(G, K, \delta_0)$ closed-form must be derived in the post-bifurcation regime — substantially harder than the uniform-vacuum case, justifying the 6–8 week effort estimate.)*

**Status:** Cat C, deferred to W7+ post-BC-249-1.

---

## §8. Empirical anchor (CODE/scripts experiment)

### §8.1 Experimental design

Build on canonical empirical pattern (NQ-141, single-formation Hessian on uniform validation; canonical §13 T-σ-Theorem-3 / T-σ-Theorem-4 anchors at lines 1334–1409; empirical artifact `CODE/scripts/results/exp_hessian_uniform_v2.json`), extend to multi-formation:

**Configuration:**
- Graph: $D_4$-symmetric free-BC 2D grid, $L \in \{4, 8, 16\}$.
- $K_{\mathrm{field}} \in \{1, 2, 3\}$.
- Parameter sweep: $\alpha = 1$ fixed; $c = 0.5$ fixed (spinodal center); $\beta \in [\beta_{\mathrm{crit}}^{(2)}(L, c), 50]$ with 20 log-spaced points.
- Multi-start: 10 random initial conditions per parameter point.

**Procedure:**
1. Run `find_formation` (CODE/scc/optimizer.py) to obtain $\mathbf{u}^* \in \mathcal{L}_K$.
2. Compute full Hessian $H(\mathbf{u}^*)$ via finite-difference (CODE/scc/diagnostics.py existing utility extended to multi-formation).
3. Project to $(\mathbf{1}\oplus\mathrm{Gold})^\perp$ — Gold subspace identified by T-σ-Lemma-3 explicit basis $\{\delta u_{x_1}, \delta u_{x_2}\}$ (lattice translation differences).
4. Tabulate $\min_k \lambda_k(\mathbf{u}^*)$ as function of $\beta$.

**Diagnostic question:** Does $\inf_\beta \min_k \lambda_k$ stay bounded away from 0 across the sweep, or does it collapse near bifurcation points?

### §8.2 Falsification test

If $\min_k \lambda_k \to 0$ uniformly as $\beta \uparrow$ a bifurcation surface (e.g., second pitchfork at $\beta_{\mathrm{crit}}^{(2)}$ on $K=2$ grids), then BC-249-1 *fails* at the bifurcation — exactly the scenario where mass-gap closure occurs in continuum field theories at phase transitions. This is **not** a refutation of BC-249-1 but a refinement: the conjecture must specify "away from bifurcation surfaces".

### §8.3 Predicted regime structure

| Regime | Predicted $\min_k \lambda_k$ behavior | Mass-gap status |
|---|---|---|
| $\beta \in (\beta_{\mathrm{crit}}^{(2)}, \beta_*)$ near pitchfork | $\to 0$ as $\beta \to \beta_{\mathrm{crit}}^{(2)+}$ | Mass-gap closure at phase transition |
| $\beta \gg \beta_{\mathrm{crit}}^{(2)}$ deep in spinodal | $\geq c_1 \beta |W''(c)|$ | Mass-gap saturates double-well scale |
| Near $K$-formation merger | $\to 0$ as $D_{\mathrm{sep}} \to D_{\mathrm{merge}}^*$ | Mass-gap closure at merger |
| Generic interior | Bounded below | BC-249-1 holds |

---

## §9. Failure modes

### §9.1 Mass-gap closure at bifurcation surfaces — consistent with C1 reformulation

**Failure (a):** $\Delta_K \to 0$ as $(\alpha, \beta, c)$ approaches bifurcation surface where $\beta_{\mathrm{crit}}^{(j)}$ thresholds intersect. This is *expected* at phase transitions and corresponds to YM IR critical phenomena.

**Resolution (revised 2026-04-30 per critic C1):** BC-249-1 (§3.1, revised) explicitly restricts to $\delta(\alpha,\beta,c) \geq \delta_0$ — i.e., the post-bifurcation spinodal-interior region **minus a $\delta_0$-tubular neighborhood of the bifurcation locus** $\mathcal{B}(G,K)$. The neighborhood thickness $\delta_0 > 0$ is part of the conjecture's hypothesis chain and the lower bound $\Delta_*(G, K, \delta_0)$ explicitly depends on $\delta_0$ (the bifurcation-distance scalar). This is consistent with §3.1's revised statement: $\Delta_*$ depends on $(G, K, \delta_0)$ — *not* uniformly across the entire post-bifurcation region. As $\delta_0 \to 0$, the lower bound $\Delta_*(G, K, \delta_0)$ may collapse to $0$; quantifying the rate of collapse is NQ-249c (§15).

### §9.2 Goldstone proliferation on highly symmetric graphs

**Failure (b):** If $G$ admits continuous-like symmetries (e.g., highly regular near-Abelian Cayley graphs), the Goldstone subspace dimension may exceed $d$, eating into the orthogonal complement. Resolution: Mass-gap defined relative to the *full* Goldstone subspace $\mathrm{Gold}_{\mathrm{full}}$; uniform bound conditional on $\dim \mathrm{Gold}_{\mathrm{full}}$ being finite (always true on finite graphs).

### §9.3 Multi-formation merger

**Failure (c):** Two formations approach each other ($D_{\mathrm{sep}} \to D_{\mathrm{merge}}^*$). **T-Merge** phenomenology (canonical retracted (c)(d)(e), `canonical.md:1664`) describes the merge path; the joint Hessian develops a soft mode in the merger direction ⇒ $\Delta_K \to 0$. This is the **discrete analog of vacuum decay / instanton mass-gap closure**.

**Resolution:** Restrict $\mathcal{L}_K$ to well-separated regime $D_{\mathrm{sep}} \geq 3$ per T-Persist-K-Sep (canonical T-σ-multi-A-Static hypothesis, `canonical.md:1233`). The R23 generic-state caveat (canonical `canonical.md:1239`) shows the well-separated regime is non-generic on $32\times32$ $D_4$ free-BC grids — implying BC-249-1 in its current form holds on a non-generic submanifold. Generalization to overlapping regime requires NQ-242 PH pipeline (canonical `canonical.md:1239`).

### §9.4 K-jump non-determinism (OP-0008)

**Failure (d):** σ^A K-jump non-determinism (OP-0008, registered in canonical §1.1 CV-1.5.1 release-notes line 77; full open-problem statement at `THEORY/canonical/open_problems.md` OP-0008) implies $\mathcal{L}_K$ is not connected and the infimum may be taken over a path-disconnected union with different mass-gap values per connected component. Resolution: BC-249-1 (revised §3.1 form) stated per-component, with $\Delta_*(G, K, \delta_0)$ depending on the connected component label as well as $(G, K, \delta_0)$.

---

## §10. Connection to other gauge-theory parallels

### §10.1 Connection G — statistical localization (Duke 2026)

`06_gauge_theory_connections_analysis.md` Connection G (line 26): SCC K-jump fragmented strata correspond to statistical-localization regime in lattice gauge theory.

**Mass-gap correspondence:** *Localization ↔ large $\Delta_K$.* Strongly localized formations have stiff Hessian → $\Delta_K$ saturated at $\sim \beta |W''(c)|$ scale. Delocalized / drifting formations have soft Hessian → $\Delta_K$ small. Rigorous parallel with Anderson-localization mass-gap analog deferred (NQ-251 candidate).

### §10.2 Connection H — string breaking (QuEra 2025)

`06_gauge_theory_connections_analysis.md` Connection H (line 27): formation birth/death = string breaking analog.

**Mass-gap correspondence:** *Formation birth ↔ mass-gap closure + reopening (protocol-conditional).* When $K_{\mathrm{act}}$ jumps $K \to K+1$, the $K$-component mass gap closes (a flat direction opens for the new formation to nucleate); after birth, $(K+1)$-component mass gap re-opens. This $\Delta_K$ cycling structurally parallels QuEra-observed string breaking.

**Reconciliation with NQ-253 (added 2026-04-30 per critic C2).** Per `THEORY/working/MF/formation_birth_string_breaking.md` §4.3, the $\Delta K = +1$ formation-birth event is **forbidden under noiseless SCC gradient flow** on $\widetilde\Sigma^K_M$ (NQ-253 Claim 4.3, anchored on T-Merge (b) Cat A monotone $K_{\mathrm{act}}$ decrease). The $\Delta_K$ cycling described above is therefore **protocol-conditional**, occurring only under one of the NQ-253 §4.2 mechanisms — **B1** (thermal noise added to canonical dynamics), **B2** (initial-condition manipulation placing $\mathbf{u}(0) \in S_{K_{\mathrm{act}}+1}$), or **B3** (stretching protocol externally driving the string-length parameter past $L_{\mathrm{crit}}$). Under generic noiseless canonical SCC dynamics, $\Delta_K$ does **not** cycle: the system descends monotonically through $K$-strata and the QuEra-style oscillatory mass-gap pattern is absent. The QuEra parallel is therefore one-way (SCC inherits the *threshold structure* of birth via §3 string-breaking energetics), not bidirectional (QuEra spontaneous-vacuum-pair-creation is not an SCC ontological input — CN10 contrastive lock applies). NQ-249g (§15) effort estimate must therefore depend on NQ-253 Phase 1 completion.

### §10.3 Connection F — Fukaya symplectic Floer

`06_gauge_theory_connections_analysis.md` Connection F (line 25): SCC stratified configuration space candidate categorification.

**Mass-gap correspondence:** Floer mass-gap analog — symplectic Floer homology has a "gap" in its grading filtration. SCC analog: σ-tuple-graded Hessian eigenspace decomposition (canonical T-σ-Theorem-3, `canonical.md:1262–1265`) admits a mass-gap-graded filtration. Currently *speculative*; categorical structure not developed.

### §10.4 Connection summary

| Connection | Direction | NQ-249 contribution |
|---|---|---|
| **A (YM mass gap)** | Inspires BC-249-1 | Direct parallel — this file |
| **G (Duke stat. loc.)** | Localization metric | $\Delta_K$ as localization indicator |
| **H (QuEra string break)** | Formation birth | $\Delta_K$ cycling at K-jumps |
| **F (Fukaya)** | Categorification | Speculative — defer |

---

## §11. W7+ priority and interactions

### §11.1 Immediate priorities

| Item | Cat | Effort | Slot |
|---|---|---|---|
| §7.1 Cat A pointwise positivity (this file) | Cat A | 0 (definitional) | Ready for canonical merge if user approves |
| §3 BC-249-1 Cat B proof attempt | Cat B target | 3–4 weeks | W7 Day 1–7 |
| §8 empirical anchor (CODE/scripts) | Cat A empirical | 1 week | W6 Day 5+ |
| §7.3 Cat C closed-form $\Delta_*(G, K)$ | Cat C target | 6–8 weeks | W8+ |
| Continuum-limit BC-249-2 | Cat B target | 12+ weeks | NQ-217 interaction, W11+ |

### §11.2 Interaction with NQ-217 (continuum limit)

NQ-217 (continuum-limit theorem) is the hypothesized graph-to-continuum convergence statement. BC-249-1 is finite-graph; BC-249-2 (the continuum extension) requires NQ-217's machinery to translate $\Delta_K$ on $L^d$ lattice to a continuum mass-gap as $L \to \infty$. The mathematical heavy lifting is in NQ-217; BC-249-2 is a *corollary* once NQ-217 is in place.

### §11.3 Interaction with NQ-242

NQ-242 (full Hessian σ-tuple time-series, canonical `canonical.md:1226`) provides the dynamic extension. Static $\Delta_K$ (BC-249-1, this file) corresponds to time-frozen σ; dynamic $\Delta_K(t)$ tracks how the mass gap evolves under gradient flow. K-jump events (where $\Delta_K \to 0$) align with σ^A K-jump non-determinism (OP-0008).

### §11.4 Tool sharing with V5b family

T-V5b-T-zero (canonical `canonical.md:1199–1201`) Goldstone-eigenvalue exact-zero mechanism is reused: the Goldstone projection in $\Delta_K$'s definition is exactly the V5b-T-zero subspace. NQ-249 inherits V5b empirical infrastructure (CODE/scripts T^d torus + free-BC grid Hessian computation) directly.

---

## §12. External references

### §12.1 Yang–Mills / gauge theory

- **Jaffe, A. & Witten, E.** (2000). *Quantum Yang–Mills Theory.* Clay Mathematics Institute Millennium Problem statement. [Foundational mass-gap conjecture statement.]
- **Faddeev, L. D.** (2005). *Yang–Mills perspectives.* [Modern algebraic perspectives on mass gap, BRST cohomology, vacuum.]
- **Sheffield, S.** (2026). *Random surfaces and 2D Yang–Mills.* Annals of Mathematics. [Sheffield framework, see Connection B in `06_gauge_theory_connections_analysis.md`.]
- **Witten, E.** (1989, 1991). *Quantum field theory and the Jones polynomial; Chern–Simons gauge theory.* [Topological gauge theory; see Connection C / F.]
- **QuEra/Harvard/Innsbruck** (2025 June). *String breaking observation in 2D quantum simulator.* [Connection H phenomenology, line 342 of `06_gauge_theory_connections_analysis.md`.]

### §12.2 Internal SCC references

- `THEORY/canonical/canonical.md`:
  - §11.1 Commitment 14 + sub-conventions (O5')(O7) — `canonical.md:785–794`
  - §11.1 Commitment 16 K-status — `canonical.md:796–812` *(Erratum 2026-04-30, critic M1: previous citation `canonical.md:77` pointed to the CV-1.5.1 version-history table row, not Commitment 16 itself.)*
  - §13 T-Commitment-14-Multi-Static — `canonical.md:1217–1228`
  - §13 T-σ-multi-A-Static — `canonical.md:1232–1239`
  - §13 T-σ-multi-D-Static — `canonical.md:1241–1242`
  - §13 T-σ-Multi-1 — `canonical.md:1248–1255`
  - §13 T-σ-Lemma-3 — `canonical.md:1301–1320`
  - §13 T-V5b-T — `canonical.md:1159–1198`
  - §13 T-V5b-T-zero — `canonical.md:1199–1201`
  - §13 T-σ-Theorem-3 — `canonical.md:1262–1265`
  - §13 T-σ-Theorem-4 + (i') orbit-rep — `canonical.md:1382–1409`
  - §13 T8-Core phase transition (existence) — `canonical.md:1005` + Scaling Caveat `canonical.md:1009`
  - §13 T-σ-Theorem-3 (Hessian on uniform, σ at uniform) — `canonical.md:1334–1371`
  - §8 admissible spinodal range $((3-\sqrt{3})/6, (3+\sqrt{3})/6)$ — `canonical.md:572`
- `THEORY/working/SF/mode_count.md` — closed-form Hessian on $u_{\mathrm{uniform}}$, Prop 1.3a/b.
- `THEORY/working/MF/multi_formation_sigma.md` — multi-formation σ framework, V5b-F transfer mechanism §5.5.
- `THEORY/working/MF/sigma_multi_trajectory.md` — dynamic σ trajectory, K-jump events.
- `THEORY/logs/daily/2026-04-30/06_gauge_theory_connections_analysis.md` — 9 gauge-theory connections enumeration; Connection A §3 (NQ-249 origin), Connection G §9, Connection H §10, Connection F §8.
- OP-0009 sub-item OP-0009-Emp (R23 σ verification) — `canonical/open_problems.md` OP-0009.
- OP-0008 σ^A K-jump non-determinism — registered in canonical §1.1 CV-1.5.1 release-notes (`canonical.md:77`); full open-problem statement at `THEORY/canonical/open_problems.md` OP-0008.

---

## §13. Hard constraints compliance

| Constraint | Status | Evidence |
|---|---|---|
| **0 canonical edits** | ✅ | This file is in `working/MF/`; no `canonical.md` write. |
| **CN10 contrastive (YM downstream parallel, not foundation)** | ✅ | §1.3, §5 contrastive table, §10 connection structure. SCC content is graph-spectral; YM is structural inspiration only. |
| **F-1 not silently resolved** | ✅ | F-1 (vacuity) is about pre-objective formation existence; this file restricts to non-trivial $\mathcal{L}_K$ Morse-0 minimizers ⇒ F-1 regime is *outside* scope. We do not claim F-1 resolved; we restrict hypothesis. |
| **M-1 not silently resolved** | ✅ | M-1 (K=1 preference) is about ground-state K-selection; this file analyzes spectral structure *given* K, not selection of K. M-1 untouched. |
| **MO-1 not silently resolved** | ✅ | MO-1 (Morse inapplicability) is sidestepped in canonical via single-formation framework; multi-formation Morse re-engagement deferred to MO-1 OP-0003 rider (canonical §1.1 CV-1.5.1 release-notes line 77; full statement at `THEORY/canonical/open_problems.md` OP-0003). This file uses Morse-0 hypothesis explicitly *as hypothesis*, never claims MO-1 resolved. |
| **Cat A/B/C distinctions explicit** | ✅ | §7 Cat A immediate (§7.1), Cat B target BC-249-1 (§7.2), Cat C closed-form (§7.3). |
| **Multi-formation default; K=1 degenerate special case** | ✅ | Throughout, $K_{\mathrm{act}} \geq 1$ general; $K=1$ recovers single-formation per canonical T-σ-multi-A-Static reduction (`canonical.md:1233`). |

---

## §14. Cross-references

### §14.1 Canonical references (read-only)

- `THEORY/canonical/canonical.md`
  - §3 phase transition (lines 1337–1371)
  - §11.1 Commitment 14 (lines 785–794)
  - §11.1 Commitment 16 (line 77)
  - §13 T-Commitment-14-Multi-Static (lines 1217–1228)
  - §13 T-σ-multi-A-Static (lines 1232–1239)
  - §13 T-σ-multi-D-Static (lines 1241–1242)
  - §13 T-σ-Multi-1 (lines 1248–1255)
  - §13 T-σ-Lemma-3 (lines 1301–1320)
  - §13 T-V5b-T-zero (lines 1199–1201)
  - §13 T-σ-Theorem-3 (lines 1262–1265)
- `THEORY/canonical/open_problems.md` — OP-0009 sub-items (OP-0009-Emp), OP-0008.
- `THEORY/canonical/theorem_status.md` — Cat A/B/C registry.

### §14.2 Working references

- `THEORY/working/MF/multi_formation_sigma.md` (510 lines) — σ-framework multi-formation extension; V5b-F → multi transfer §5.5.
- `THEORY/working/MF/sigma_multi_trajectory.md` (283 lines) — dynamic σ trajectory + K-jump events; OP-0008 dependence.
- `THEORY/working/MF/F_Kstep_K_triple.md` (359 lines) — F / K_step / K_act triple bridge; OP-0009-F partial resolution.
- `THEORY/working/SF/mode_count.md` (359 lines) — Prop 1.3a/b closed-form Hessian on uniform; SF baseline.
- `THEORY/working/SF/symmetry_moduli.md` — D_4 normal-form coefficients $A_1, A_2$ (used in T-σ-Theorem-4).

### §14.3 Daily log references

- `THEORY/logs/daily/2026-04-30/06_gauge_theory_connections_analysis.md` (622 lines) — 9 gauge-theory connections enumeration + NQ-249 / NQ-250 / NQ-253 origin.
- `THEORY/logs/daily/2026-04-30/08_pm_infinite_develop_batch.md` — OP-0009-Emp (this file's anchoring sub-item).
- `THEORY/logs/daily/2026-04-29/11_NQ198fg_results_and_D5_withdraw.md` — V5b-T-zero anchor; T-V5b-T' withdrawn.
- `THEORY/logs/daily/2026-04-28/27_Q1_Q2_findings_dynamic_stability.md` — T-σ-Multi-1 dynamic stability finding.

### §14.4 Code references (CODE/)

- `CODE/scc/optimizer.py` — `find_formation` for $\mathcal{L}_K$ realization.
- `CODE/scc/multi.py` — K-field multi-formation; `transport_k_formations`.
- `CODE/scc/diagnostics.py` — Hessian utilities (extension to multi-formation needed for §8).
- `CODE/scripts/results/exp_hessian_uniform_v2.json` — single-formation Hessian validation reference (canonical §13 T-σ-Theorem-3/T-σ-Theorem-4, lines 1334–1409).

---

## §15. Open questions registered

| ID | Statement | Cat | Effort | Slot |
|---|---|---|---|---|
| **NQ-249** (this file) | BC-249-1 SCC Mass-Gap Conjecture proof on $D_4$ free-BC grids | Cat B target | 3–4 weeks | W7 |
| **NQ-249a** | §8 empirical anchor — $\inf_\beta \min_k \lambda_k$ on $L \in \{4,8,16\}$, $K \in \{1,2,3\}$ | Cat A empirical | 1 week | W6 Day 5+ |
| **NQ-249b** | Cat C closed-form $\Delta_*(G, K)$ in terms of Laplacian spectrum + $W''(c)$ + Stab + $\lambda_{\mathrm{rep}}$ | Cat C target | 6–8 weeks | W8+ |
| **NQ-249c** | Mass-gap closure at bifurcation surfaces — quantitative neighborhood thickness | Cat B target | 2–3 weeks | W7 Day 5+ |
| **NQ-249d** | Multi-formation merger mass-gap closure rate $\Delta_K \sim e^{-c D_{\mathrm{sep}}}$ | Cat B target | 2 weeks | W7+ |
| **NQ-249e** | Continuum-limit BC-249-2 via NQ-217 interaction | Cat B target | 12+ weeks | W11+ |
| **NQ-249f** | $\Delta_K$ as localization indicator (Connection G to Duke 2026 stat. loc.) | Cat C | 4 weeks | W8+ |
| **NQ-249g** | $\Delta_K$ cycling at formation birth (Connection H to QuEra 2025 string break) | Cat C | 4 weeks | W8+ |

---

## §16. Promotion gate (to canonical)

**Path A (Cat A *conditional*, §7.1 only — revised 2026-04-30 per critic C3):** Pointwise positivity at non-degenerate Morse-0 minimizers is conditional on the (H1)+(H2)+(H3) hypothesis chain restated in §7.1: (H1) Option A interior regime (canonical §13 line 1218); (H2) $D_{\mathrm{sep}} \geq 3$ well-separated hypothesis (canonical T-σ-multi-A-Static, lines 1232–1235); (H3) T-σ-Multi-1 multi-formation Goldstone identification (canonical lines 1248–1255, currently **Cat B target** per CV-1.5.1 line 77). Promotion to canonical §13 deferred until T-σ-Multi-1 Cat A upgrade is achieved (NQ-2xx, W7+). *(Earlier draft asserted "no new canonical entry needed" — retracted 2026-04-30 per critic C3: the silent hypothesis chain (H1)+(H2)+(H3) makes the Cat A claim conditional, not immediate. The "no canonical entry" claim is also retracted; conditional Cat A may merit a canonical §13 entry once the T-σ-Multi-1 dependency is resolved.)*

**Path B (Cat B target, BC-249-1):** Once §8 empirical anchor is run and BC-249-1 is proved at Cat B level (uniform lower bound with explicit $\Delta_*(G, K)$ structural form), the conjecture promotes to canonical §13 as **T-σ-Multi-MassGap** with status Cat B target → Cat A pending Łojasiewicz machinery.

**Path C (Cat C, §7.3 closed form):** Closed-form $\Delta_*(G, K)$ in Laplacian-spectral basis promotes to canonical §13 only after generic-graph analysis matures (likely W11+ post NQ-217 continuum limit).

**No promotion at this iteration; this file remains in `working/MF/` until empirical anchor + BC-249-1 proof lane converge.**
