# Reservoir Reinterpretation of K: From Finite Slots to Latent Formation Reservoir

**File:** `THEORY/working/MF/reservoir_reinterpretation_of_K.md`
**Document type:** Non-canonical theoretical memo. Working draft. Conceptual reinterpretation candidate.
**Created:** 2026-05-02 (post WQ-1.C-R2; conceptual correction motivated by the WQ-1 / WQ-2 / WQ-1.C / WQ-1.C-R2 empirical record).

**Predecessor artifacts:**
- `THEORY/working/MF/layered_ambient_architecture_{candidate,README,agent_notes,next_work}.md`
- `THEORY/working/MF/nq242c_results.md` (WQ-1: F2)
- `THEORY/working/MF/ksoft_kact_bridge_lemma.md` (WQ-2: F-B6 confirmed)
- `THEORY/working/MF/wq1c_layerI_h0_bardeath_results.md` (WQ-1.C: F-C1 / F-C7)
- `THEORY/working/MF/wq1c_r2_projected_layerII_aggregate_sigma_results.md` (WQ-1.C-R2: F-R2-F3 / F-R2-F4 dual reading)
- `THEORY/working/MF/K_status_commitment.md` (Commitment 16 K_field / K_act decomposition)
- `THEORY/working/MF/shared_pool_canonical_proposal.md` (I9' shared-pool ambient)
- `THEORY/working/MF/F_Kstep_K_triple.md` (4-quantity bridge)
- `THEORY/working/E/soft_K_definition.md` ($K_{\mathrm{soft}}^\phi$ persistence-based)
- `THEORY/canonical/canonical.md`, `theorem_status.md`, `open_problems.md`

---

## 1. Status and Scope

This is a **non-canonical theoretical memo**. It does not edit canonical files. It does not promote any model to canonical status. It does not assign a Commitment number. It does not resolve OP-0005, OP-0008, or any other open problem.

It proposes a **conceptual reinterpretation** of the integer $K$ family ($K_{\mathrm{field}}$, $K_{\mathrm{act}}$, $K_{\mathrm{soft}}$) in light of three converging empirical observations:

1. **WQ-1 (F2):** under Layer II shared-pool dynamics with simplex barrier and inter-formation repulsion, the labelled active count $K_{\mathrm{act}}^\varepsilon$ is structurally rigid. No labelled slot ever extincts within reach of the protocol.
2. **WQ-2 (F-B6 confirmed):** the *aggregate* field $U(\mathbf u(t)) = \sum_j u^{(j)}(t)$ undergoes substantial topological transitions ($K_{\mathrm{bar}}^{0.10}(U)$ : 3 → 1) along the same trajectories where $K_{\mathrm{act}}$ is rigid.
3. **WQ-1.C / WQ-1.C-R2:** when the test was reframed at the aggregate $H_0$ level, the σ-standard implementation could not register the bar-death event in either the cluster-structure sense (R2-F4: structure unchanged) or the eigenvalue-magnitude sense (R2-F3: pre-event already differs by O(1)). σ-standard is structurally insensitive to aggregate-topology transitions of the form WQ-2 produced.

The convergent diagnosis: **the integer $K$ family was being treated as if it indexed primitive birth/death events of distinguishable formations.** The empirical record refutes this reading. This memo proposes an alternative reading in which $K_{\mathrm{field}}$ is a *finite-rank truncation* of an underlying *latent formation reservoir*, and $K_{\mathrm{act}}$ / $K_{\mathrm{soft}}$ are two distinct projections of that reservoir into integer or real-valued observables.

**Status grade per claim.**

| Claim | Status |
|---|---|
| WQ-1 / WQ-2 / WQ-1.C empirical observations | working-definition safe (per the cited results files) |
| Layered ambient-state architecture (Layer I / II / III) | working-definition safe; **preserved by this memo** |
| Commitment 1 ($u_t$ primitive), Commitment 11 (crisp derivative), Commitment 16 (K_field / K_act) | canonical theorem-grade; **preserved by this memo** |
| The reinterpretation: $K_{\mathrm{field}}$ as finite-rank truncation of a reservoir | working-grade conceptual proposal |
| Specific reservoir models (measure-theoretic / spectral-mode / nonparametric) | candidate frameworks; not all internally consistent; not promoted |
| OP-0005, OP-0008 reframing implications | conjectural / downstream; the reframe does not resolve them, only relocates them |
| Implication for σ_rich | conjectural; this memo does not promote σ_rich to sufficiency |

**Out of scope.**

- Resolving OP-0005, OP-0008, OP-0009 sub-items.
- Promoting σ-rich to canonical sufficiency.
- Importing gauge theory, full category theory, sheaf cohomology, Geometric Langlands, CBF/CLF, neural operators, Koopman operators, formal verification.
- Application-domain validation (vision, robotics, control).
- Replacing canonical Commitment 1 ($u_t$ primitive). The reservoir, in any of its three readings, lives *above* (not below) the primitive single-field $u_t$.

---

## 2. Motivation: Why "Creation from Nothing" Is the Wrong Model for K-Change

The original WQ-1 protocol design assumed that a K-jump event consists of a *labelled slot's mass dropping to zero* — i.e. an active formation literally going extinct. This is an implicit "annihilation" model: formations are independent entities; their count changes by birth (a slot acquires mass) or death (a slot loses mass).

This model is contradicted by the WQ-1 / WQ-2 / WQ-1.C / WQ-1.C-R2 empirical record on three independent axes.

### 2.1 The dynamics will not annihilate

Per WQ-1 results: under Layer II Option D-2 dynamics with the canonical SCC + simplex barrier energy, no labelled slot extincts in any of 14 trajectories spanning $\lambda_{\mathrm{rep}} \in \{10, 30, 100, 300\}$ and inter-bump distance ∈ [5.1, 10.3]. The minimum slot mass ever observed was **23.94**, more than 100× the activity threshold $\varepsilon = 0.225$. The dynamics does not have an attractor at $m_j = 0$ for active slots; instead, mass redistributes within wells without leaving them.

This is structural: the SCC self-energy of each slot creates a deep basin around its current support; the inter-formation repulsion redistributes mass between wells but does not drain a well to zero. The "annihilation" event the protocol was built to detect is not a feature of the dynamics.

### 2.2 The aggregate field changes topology anyway

Per WQ-2 (`ksoft_kact_bridge_lemma.md` §13): along the same WQ-1 F2 trajectories, the aggregate $U(\mathbf u(t))$ undergoes a robust integer-counted bar-death: $K_{\mathrm{bar}}^{0.10}(U)$ : 3 → 1 for both A and B. Per the bridge lemma's F-B6 framing, **labelled $K_{\mathrm{act}}$ rigidity coexists with aggregate-field topological mobility**.

This means the *topology* of the field (in the unlabelled $H_0$ sense) does change, but it changes by *merging* and *prominence collapse* — not by labelled extinction. Two slots' contributions can fuse into a single $H_0$ feature on $U$ without either slot's mass dropping below threshold. The "death" of a topological feature is not a death of any labelled entity.

### 2.3 σ-standard cannot see the topological change

Per WQ-1.C-R2 dual-reading (`wq1c_r2_projected_layerII_aggregate_sigma_results.md` §5.4):

- Under the **eigenvalue-magnitude** σ-equivalence: A and B aggregate σ pre-event values differ by O(1), far beyond any tested tolerance. The σ-standard reads the *static* geometric difference between equilateral A and compressed B, not the dynamical bar-death event.
- Under the **cluster-structure** σ-equivalence: A and B both have $(1, 1, 1, 1, 1, 1)$ before and after the bar-death. The structure is invariant through the topological transition; σ-standard sees no event.

Either way, σ-standard at the aggregate-projection level is **insensitive** to the aggregate-topology transition. The σ-test was designed for labelled $K_{\mathrm{act}}$-jumps; the aggregate-topology event is a different phenomenon, and σ-standard does not cleanly register it.

### 2.4 Diagnosis

The three observations together imply: **the integer $K$ family does not refer to a fundamental object whose value changes by birth or death**. Specifically:

- $K_{\mathrm{field}}$ is an architectural cap that the dynamics does not respect (it does not drive slots to extinction);
- $K_{\mathrm{act}}^\varepsilon$ is a labelled threshold-gated count that does not move under the natural dynamics;
- $K_{\mathrm{soft}}^\phi(U)$ moves under the dynamics, but it moves by *merging* and *prominence collapse*, not by birth or death of a fundamental entity.

The "things being counted" by these three integers are not the same things, and none of them are primitive birth/death events. This is what motivates the reinterpretation.

---

## 3. The Reinterpretation: $K_{\mathrm{field}}$ as Finite-Rank Truncation of a Latent Reservoir

The reinterpretation is structural, not ontological-additive. It does not introduce a new primitive (Commitment 1's $u_t$ is preserved). It reframes how the integer $K$ family relates to the field.

### 3.1 The picture

Posit an **underlying latent formation reservoir** $\mathcal R$. The reservoir is a structure on top of (and derived from) the primitive single-field state $u \in \Sigma_M(G)$ — *not* a new primitive. Concretely, $\mathcal R$ is a candidate algebraic / measure-theoretic / spectral object that organizes the *potential decomposition* of $u$ into formation-like components.

$K_{\mathrm{field}}$ is then a **finite-rank truncation level** at which the reservoir is sampled. A specific $K_{\mathrm{field}} = K$ choice corresponds to a particular *projection*

$$
\pi_K: \mathcal R \longrightarrow \widetilde\Sigma^K_M(G)
$$

into the labelled $K$-field shared-pool ambient (Layer II). Different $K_{\mathrm{field}}$ choices give different projections of the *same* reservoir.

$K_{\mathrm{act}}^\varepsilon$ is the **thresholded activation count** on a chosen projection: of the $K_{\mathrm{field}}$ slots in $\pi_K(\mathcal R)$, how many carry mass above $\varepsilon$. It is observable-on-the-projection, not observable-on-the-reservoir.

$K_{\mathrm{soft}}^\phi(U)$ is the **field-native morphology count** computed directly on the aggregate $U = \sum_j u^{(j)}$ via $H_0$ persistence. Critically: $U$ is *invariant under the projection level* — different $K_{\mathrm{field}}$ truncations of the same reservoir produce the same aggregate (since aggregation forgets labelling). $K_{\mathrm{soft}}^\phi(U)$ is therefore a reservoir-level observable, not a projection-level observable.

### 3.2 Reading of the empirical record under this reinterpretation

- **WQ-1 F2** is reread as: *the chosen projection $\pi_4$ is too coarse to register topological transitions of the reservoir*. The reservoir's transition (F-B6: aggregate $H_0$ bar death) happens, but the labelled-slot view via $\pi_4$ does not see it because the slot-mass-threshold is the wrong observable.
- **WQ-2 F-B6** is reread as: *the reservoir-level observable ($K_{\mathrm{soft}}$ or $K_{\mathrm{bar}}$ on $U$) sees the transition that the projection-level observable ($K_{\mathrm{act}}$) misses*.
- **WQ-1.C-R2 F-R2-F3 / F-R2-F4** is reread as: *σ-standard, in either of its current readings, is a projection-dependent observable*. The eigenvalue-magnitude reading sees the static reservoir state difference between A and B. The cluster-structure reading sees only the *pattern* of the projection, not the underlying reservoir transition.

In this reading, σ-standard's "incompleteness" question is reframed: the question is no longer "does σ-standard miss labelled inheritance information?" but rather "does any projection-level σ observable encode reservoir-level information?"

### 3.3 What is preserved

- **Commitment 1** ($u_t$ primitive): preserved. The reservoir is derived from / lives above the primitive field, not below it.
- **Commitment 11** (crisp objects derivative): strengthened. Crisp object counts are now seen as triple-derived (field → reservoir → projection → integer count), not just doubly derived (field → integer count).
- **Commitment 16** ($K_{\mathrm{field}}$ / $K_{\mathrm{act}}$ two-tier decomposition): reread. $K_{\mathrm{field}}$ is now "truncation level chosen by the modeler"; $K_{\mathrm{act}}$ is now "post-truncation thresholded count". The two-tier structure persists; its *interpretation* shifts.
- **Layered ambient architecture (Layer I / II / III)**: preserved. The reservoir does not replace the layers; it sits *above* the architecture as a conceptual generator. Layer II is one realization of $\pi_K(\mathcal R)$ for a chosen $K = K_{\mathrm{field}}$.

### 3.4 What changes

- $K_{\mathrm{field}}$ is no longer "architectural cap to be respected by the dynamics" but "modeling choice that determines the projection rank". Different $K_{\mathrm{field}}$ values are different views of the same reservoir.
- $K_{\mathrm{act}}^\varepsilon$ is no longer "active count of distinguishable formations" but "post-projection thresholded activation count, conditioned on a $K_{\mathrm{field}}$ choice".
- $K_{\mathrm{soft}}^\phi$ becomes the *primary* count observable: it lives at the reservoir level via the aggregate $U$ and is the invariant the dynamics actually moves.
- "K-jump" and "bar-death" become two separate phenomena: "K-jump" is a projection-level event ($K_{\mathrm{act}}^\varepsilon$ drops), "bar-death" is a reservoir-level event ($K_{\mathrm{soft}}^\phi$ drops, $K_{\mathrm{bar}}^{\ell_{\min}}$ drops). Under WQ-1 F2 + WQ-2 F-B6 the second occurs without the first.

---

## 4. Three Candidate Reservoir Models

Three specific reservoir formalizations. Each is a candidate; none is promoted; their relative fit to the SCC empirical record is discussed in §5.

### 4.1 Measure-theoretic reservoir

#### 4.1.1 State space

The reservoir is a finite positive measure $\nu$ on a parameter space $\Theta$ of single-field "modes". A natural choice:

$$
\Theta = \big\{ (c, r, A, \theta, \ldots) \big\}
$$

— parameter tuples specifying a single bump's center $c \in X$, characteristic radius / scale $r$, amplitude $A$, orientation $\theta$, etc. $\nu$ assigns mass to each mode-parameter region.

The induced single-field is

$$
u_\nu(x) := \int_\Theta b(x; \theta)\, \nu(d\theta),
$$

where $b(x; \theta)$ is a fixed bump kernel parameterized by $\theta$.

#### 4.1.2 Projection to finite $K_{\mathrm{field}}$

$\pi_K(\nu)$ approximates $\nu$ by a $K$-atom discrete measure:

$$
\pi_K(\nu) = \sum_{j=1}^{K} m_j\, \delta_{\theta_j},
$$

with atoms $\{\theta_j\}_{j=1}^K$ and weights $\{m_j\}_{j=1}^K$ chosen to minimize an optimal-transport distance $W_p(\nu, \sum_j m_j \delta_{\theta_j})$ or to match the first $K$ moments of $\nu$.

The corresponding Layer II state is $\mathbf u = (u^{(1)}, \ldots, u^{(K)})$ with $u^{(j)}(x) = m_j \cdot b(x; \theta_j)$. Total mass conservation: $\sum_j m_j = M$, matching $\nu(\Theta) = M$.

#### 4.1.3 Relation to aggregate $U$

$U(\pi_K(\nu)) = \sum_j m_j b(\cdot; \theta_j)$ is a $K$-atom discretization of $u_\nu$. As $K \to \infty$ (with appropriate atom-placement), $U(\pi_K(\nu)) \to u_\nu$ in $L^p$.

Critical: $u_\nu$ itself depends only on $\nu$, not on the discretization. **The aggregate $U$ is reservoir-level invariant up to discretization error.**

#### 4.1.4 Possible K-selection mechanism

K-selection becomes "what truncation rank is *minimal* for matching $\nu$ within a chosen tolerance $\eta$?":

$$
K^*(\nu, \eta) := \min \{ K : W_p(\nu, \pi_K(\nu)) \le \eta \}.
$$

This connects K-selection to the *complexity* of the reservoir, not to dynamical selection of a particular K. Different reservoirs ν admit different minimal K under the same η.

#### 4.1.5 Relation to $H_0$ persistence

$H_0$ superlevel persistence of $u_\nu$ measures the *modes* of the integrated bump field, not the atoms of $\nu$. The map $\nu \mapsto \mathrm{Dgm}_0^{\sup}(u_\nu; G)$ is many-to-one: different $\nu$ can produce the same $u_\nu$ (and hence the same persistence diagram). $K_{\mathrm{soft}}^\phi(u_\nu)$ is therefore the *image* observable; the reservoir-level invariant is finer.

This is consistent with the WQ-2 F-B6 finding: the aggregate $U$ moves topologically because $u_\nu$ moves under the dynamics; the labelled $K_{\mathrm{act}}$ does not move because the discretization $\pi_4(\nu)$ is rebalancing among its 4 atoms without changing atom count.

#### 4.1.6 Risks and prerequisites

- Choice of bump kernel $b(x; \theta)$ is non-canonical. SCC's primitive is $u : X \to [0,1]$; defining a parametric bump family is an additional commitment.
- Optimal-transport projection is computationally expensive on graphs.
- The space $\Theta$ is finite-dimensional; representing a generic SCC field as an integral over finite-dimensional bumps may be a tight fit (no orthogonal-residual term).
- Mathematical prerequisite: standard finite-measure / OT theory on metric spaces (Villani 2009 *Optimal Transport*); no exotic machinery.

### 4.2 Spectral mode reservoir

#### 4.2.1 State space

The reservoir is a (possibly infinite) sequence of coefficients $\{c_k\}_{k \in \mathbb{N}}$ on a basis of single-field "modes" $\{\phi_k : X \to \mathbb{R}\}_{k \in \mathbb{N}}$. Natural basis: Laplacian eigenfunctions of $G$, or Hessian eigenfunctions of the SCC energy at a reference state, or orthonormal localized bump modes (e.g. Gabor / Hermite / wavelets on $X$).

The reservoir state is

$$
u_{\mathbf c}(x) := \sum_k c_k\, \phi_k(x),
$$

subject to $u_{\mathbf c} \in \Sigma_M(G)$ (mass + box constraints implicitly encoded in the coefficient space).

#### 4.2.2 Projection to finite $K_{\mathrm{field}}$

$\pi_K(\mathbf c)$ keeps the top-$K$ coefficients:

$$
\pi_K(\mathbf c) := (c_1, c_2, \ldots, c_K, 0, 0, \ldots),
$$

where the order of $\{c_k\}$ is by decreasing $|c_k|$ (or by decreasing energy contribution).

A *labelled* Layer II view requires a re-labelling of the top-$K$ modes as $K$ slot-fields:

$$
u^{(j)}(x) := c_j\, \phi_j(x)\, /\, \text{(simplex enforcement)}.
$$

This is *not* a faithful Layer II decomposition — the modes $\phi_j$ are not localized formations in general. The reinterpretation accepts this: labelled Layer II is then a *spectral* labelling, not a *spatial* labelling.

#### 4.2.3 Relation to aggregate $U$

$U(\pi_K(\mathbf c)) = \sum_{k=1}^{K} c_k \phi_k$ is the rank-$K$ truncation of $u_{\mathbf c}$. As $K \to \infty$, $U(\pi_K(\mathbf c)) \to u_{\mathbf c}$ in $L^2$ (if the basis is complete).

The aggregate is *automatically* the truncated reservoir field — there is no separate aggregate operation; aggregation = truncation.

#### 4.2.4 Possible K-selection mechanism

K-selection becomes "what is the effective spectral rank of $u_{\mathbf c}$?":

$$
K^*(\mathbf c, \eta) := \min \{ K : \sum_{k > K} c_k^2 \le \eta \},
$$

i.e. the smallest $K$ that captures fraction $1 - \eta/\|\mathbf c\|^2$ of the spectral energy. This is essentially the *participation ratio* or *effective dimension* familiar from spectral theory.

This connects K-selection to the *concentration* of the field's spectral content — fields with rapidly-decaying coefficients have small $K^*$, broadband fields have large $K^*$.

#### 4.2.5 Relation to $H_0$ persistence

$H_0$ superlevel persistence of $u_{\mathbf c}$ depends on the *spatial* structure of the linear combination $\sum_k c_k \phi_k$, not directly on the coefficient sequence. Two different coefficient sequences can produce $L^p$-close fields with identical persistence diagrams.

The relation is: $K_{\mathrm{soft}}^\phi(u_{\mathbf c})$ is a *coarser* observable than the spectral-rank $K^*(\mathbf c, \eta)$; multiple reservoir states can have the same persistence count. This is the same many-to-one structure as in §4.1.5.

#### 4.2.6 Risks and prerequisites

- Choice of basis $\{\phi_k\}$ is non-canonical and consequential. Laplacian eigenfunctions are global (not localized); localized bump bases require an additional construction (e.g. wavelet-on-graph framework, Hammond-Vandergheynst-Gribonval 2011) which is heavyweight.
- Reservoir modes do not correspond to "formations" in the SCC sense (a single Laplacian eigenfunction is not a localized bump). The reinterpretation must accept that the labelled slots of Layer II are spectral coordinates, not spatial formations.
- The CN10 contrastive boundary: spectral graph theory is *standard mathematical machinery* (`mathematical_scaffolding_4tools.md` already invokes it for σ); using it for the reservoir is a continuation of existing scaffolding, not a new import.
- Mathematical prerequisite: spectral graph theory + finite-rank truncation theory (Chung 1997 *Spectral Graph Theory*); no exotic machinery beyond what `mathematical_scaffolding_4tools.md` already invokes.

### 4.3 Nonparametric / infinite-mixture reservoir

#### 4.3.1 State space

The reservoir is an *infinite-dimensional* ensemble of formation modes drawn from a base measure, with mixture weights drawn from a stick-breaking process. Concretely (Pitman-Yor / Dirichlet process, Pitman 1995, Pitman-Yor 1997):

$$
\nu = \sum_{k=1}^{\infty} w_k\, \delta_{\theta_k}, \qquad \theta_k \sim G_0, \qquad w_k = v_k \prod_{l < k} (1 - v_l), \quad v_k \sim \mathrm{Beta}(1 - \alpha, \beta + k\alpha),
$$

with concentration parameter $\beta > 0$ and discount $\alpha \in [0, 1)$. The atoms are infinitely many (with probability 1) but most carry vanishing weight.

The induced single field is $u_\nu(x) = \int b(x; \theta) \nu(d\theta) = \sum_k w_k b(x; \theta_k)$, as in §4.1 with $\nu$ from the stick-breaking prior.

#### 4.3.2 Projection to finite $K_{\mathrm{field}}$

$\pi_K(\nu)$ keeps the $K$ atoms with largest weights $w_k$. Equivalently, the *effective number of clusters* observed in $n$ samples from $\nu$ grows as $O(\log n)$ (Dirichlet) or $O(n^\alpha)$ (Pitman-Yor with $\alpha > 0$); $K_{\mathrm{field}} = K$ corresponds to capping this at $K$.

The corresponding Layer II state is $\mathbf u = (m_1 b(\cdot; \theta_1), \ldots, m_K b(\cdot; \theta_K))$ with $m_j = M w_j / \sum_{l \le K} w_l$.

#### 4.3.3 Relation to aggregate $U$

$U(\pi_K(\nu)) \to u_\nu$ as $K \to \infty$, with the rate controlled by the tail decay of stick-breaking weights. The aggregate is reservoir-level invariant up to truncation tail.

#### 4.3.4 Possible K-selection mechanism

K-selection is *posterior* rather than architectural: $K_{\mathrm{field}}$ is not chosen ex ante but *observed* as a sufficient statistic of the posterior $\nu | u$ given some likelihood $p(u | \nu)$. Standard nonparametric inference machinery (Gibbs sampling, variational inference) gives a posterior distribution on $K_{\mathrm{field}}$.

This connects K-selection to **Bayesian model-complexity selection** — a well-developed area with explicit consistency theorems (Ghosal-van der Vaart 2017 *Fundamentals of Nonparametric Bayesian Inference*).

#### 4.3.5 Relation to $H_0$ persistence

Same many-to-one structure as §4.1.5 / §4.2.5: $K_{\mathrm{soft}}^\phi(u_\nu)$ is a coarser observable than the posterior $K_{\mathrm{field}}$. Persistence sees the *connected-component* structure of the integrated field; the reservoir distinguishes individual atoms even when they overlap on the field.

#### 4.3.6 Risks and prerequisites

- Heavyweight import: nonparametric Bayes is not a current SCC framework. It introduces probability-space machinery (concentration parameters, stick-breaking, posterior inference) that is far from the canonical $u_t$-on-graph SCC ontology.
- The CN10 contrastive boundary is severely strained: nonparametric Bayes is a *substantive* framework with its own primitives. Using it for K-selection risks reductive identification rather than contrastive comparison.
- Prerequisite literature: Pitman 2006 *Combinatorial Stochastic Processes*; Ghosal-van der Vaart 2017; both are full-textbook commitments.
- This model is the most powerful (it gives K-selection from first principles via posterior inference) but the most expensive ontologically.

---

## 5. Best Fit to Current SCC Evidence

### 5.1 Evidence audit

The three reservoir models predict different relationships between $K_{\mathrm{field}}$, $K_{\mathrm{act}}$, $K_{\mathrm{soft}}$, and the dynamics. The WQ-1 / WQ-2 / WQ-1.C / WQ-1.C-R2 record provides four constraints:

| Constraint | Source | Consequence for reservoir model |
|---|---|---|
| $K_{\mathrm{act}}^\varepsilon$ rigid under Layer II dynamics | WQ-1 F2 | reservoir model must accommodate a stable post-projection slot count |
| $K_{\mathrm{bar}}^{\ell_{\min}}(U)$ moves under Layer II dynamics | WQ-2 F-B6 | reservoir-level field $u_\nu$ must move topologically; aggregate $U$ is reservoir-level |
| σ-standard pre-event differs by O(1) at projection level | WQ-1.C-R2 R2-F3 | static reservoir state is distinguishable at the projection's spectral level even when the projection structure agrees |
| σ-standard cluster pattern unchanged by bar-death event | WQ-1.C-R2 R2-F4 | reservoir-level transition is invisible to projection-level cluster structure |

### 5.2 Fit per model

**Measure-theoretic reservoir (§4.1):**

- Accommodates $K_{\mathrm{act}}$ rigidity: the 4-atom discretization of $\nu$ keeps 4 atoms throughout because the projection is stable under the dynamics' effect on $\nu$.
- Accommodates $K_{\mathrm{bar}}(U)$ mobility: $u_\nu$ moves under the dynamics, and its $H_0$ topology can change (atoms can merge in space).
- Static σ pre-event difference: A and B have different $\nu$ (different center distributions), so different $u_\nu$, so different FD-Hessian eigenvalues. ✓
- Bar-death cluster invariance: the merging of two atoms in space changes connected-component count of $u_\nu$ but not the rank of the Hessian's spectrum (until atoms become indistinguishable, which is past the bar-death time). ✓
- **Mathematical prerequisite cost: low.** Standard finite-measure / OT theory.
- **Best-fit candidate.**

**Spectral mode reservoir (§4.2):**

- Accommodates $K_{\mathrm{act}}$ rigidity: top-4 spectral coefficients are stable (the spectral content of the field doesn't suddenly drop in rank).
- Accommodates $K_{\mathrm{bar}}(U)$ mobility: spatial topology of the rank-$K$ approximation can change while spectral rank is preserved.
- Static σ difference: A and B have different coefficient sequences. ✓
- Bar-death cluster invariance: the FD-Hessian spectrum is computed on $u_{\mathbf c}$ directly; it changes smoothly with $\mathbf c$. ✓
- **Mathematical prerequisite cost: moderate.** Spectral graph theory + localized bump bases.
- **Reasonable alternative.** The spectral-vs-spatial labelling tension (modes are global, not localized formations) is a structural cost.

**Nonparametric / infinite-mixture reservoir (§4.3):**

- Accommodates all four observations naturally (it strictly generalizes §4.1).
- Static σ difference: explained by different posterior $\nu | u_A$ vs $\nu | u_B$.
- Bar-death cluster invariance: explained by atom-merging without atom-disappearance.
- **Mathematical prerequisite cost: high.** Full nonparametric Bayes machinery; heavyweight CN10 strain.
- **Powerful but expensive.** Useful for K-selection mechanism if we accept the import cost; otherwise overengineered for the empirical record we have.

### 5.3 Recommendation

**Best fit per current evidence: §4.1 measure-theoretic reservoir with bump kernel.**

- Lowest prerequisite cost.
- Accommodates all four constraints.
- Naturally connects K-selection to optimal-transport distance to the discretization (concrete, computable).
- Aligns with the existing `sigma_rich.py` centroid + orientation + Wigner data: those are the natural reservoir-level invariants of bump atoms (centroid = atom location; orientation tensor = anisotropy of bump shape; Wigner data = Goldstone-pair coupling between atoms).
- Compatible with the existing $H_0$ persistence framework (`soft_K_definition.md` + `F_Kstep_K_triple.md` §7.4): persistence of $u_\nu$ is the standard observable.

**Spectral mode reservoir (§4.2) as a complementary view.** The spectral and measure-theoretic readings are not exclusive; they can coexist as two *coordinates* on the same reservoir. The spectral view is natural for σ-standard analysis (FD-Hessian eigenvalues are spectral); the measure-theoretic view is natural for K-jump and merger-geometry analysis.

**Nonparametric reservoir (§4.3) deferred.** The K-selection mechanism it provides is attractive but the ontological import cost is too high for the current empirical record. Revisit if K-selection becomes the primary unresolved question.

---

## 6. Implications for OP-0005, OP-0008, σ-rich, and WQ-1 Retry

### 6.1 OP-0005 (K-Selection, HIGH)

**Original framing.** "What mechanism selects the integer $K$ at which formation count stabilizes?"

**Reframed under reservoir reinterpretation.** "What is the *effective rank* of the reservoir under the SCC dynamics, and how does it depend on initial conditions and graph structure?"

Under the measure-theoretic reservoir (§4.1), this becomes:
- A K-selection candidate is the *minimal $K$ for which $W_p(\nu, \pi_K(\nu)) \le \eta$* under a chosen $\eta$.
- The K-selection three-model comparison of WQ-4 (`layered_ambient_architecture_next_work.md`) gains a fourth candidate: (d) **reservoir effective rank**.
- Different initial conditions correspond to different reservoirs $\nu_0$; their evolution under the SCC flow gives time-varying reservoirs $\nu_t$, and effective rank $K^*(\nu_t, \eta)$ is the candidate observable.

**OP-0005 status:** still 🟠 HIGH OPEN. The reframe gives a *new candidate mechanism*, not a resolution.

### 6.2 OP-0008 (σ-standard K-jump inheritance non-determinism)

**Original framing.** "Is σ-standard sufficient to determine post-K-jump state from pre-K-jump state?"

**Reframed under reservoir reinterpretation.** The "K-jump" event is recategorized:

- Projection-level K-jump (slot extinction): does not occur naturally under SCC dynamics (WQ-1 F2). OP-0008 as originally stated tests an event that the dynamics does not produce.
- Reservoir-level transition: $\nu_t$ smoothly evolves; its discretization $\pi_K(\nu_t)$ may rebalance atoms; its aggregate $u_{\nu_t}$ may undergo $H_0$ bar-death. None of these is a "K-jump" in the projection-level slot sense.

The OP-0008 question is therefore reframed as: **"Is σ-standard sufficient to determine post-aggregate-bar-death σ-standard from pre-aggregate-bar-death σ-standard, where σ-standard is computed on the projection at fixed $K_{\mathrm{field}}$?"**

WQ-1.C-R2 result reads: at the projection level, σ-standard is *insensitive* to the aggregate bar-death event. The "incompleteness" is real but is of a different nature than originally framed: σ-standard is *blind to the relevant transition*, not just *under-determined as an inheritance map*.

**OP-0008 status:** still 🟠 HIGH OPEN. The reframe shifts the question from "non-determinism of inheritance" to "blindness to transition type". Path B (σ-rich augmentation) becomes more clearly motivated: σ-rich's centroid + Wigner-data + orientation are exactly the reservoir-level atom invariants that *would* see the merger geometry of an aggregate bar-death.

### 6.3 σ-rich

**Original framing.** "Augment σ-standard with centroid + inertia + Wigner data to make K-jump inheritance deterministic."

**Reframed under reservoir reinterpretation.** σ-rich's components are exactly the **reservoir-level atom invariants** in the measure-theoretic reservoir (§4.1):

- centroid = atom location $c_j = \theta_j^{\mathrm{location}}$;
- inertia / orientation = atom anisotropy $\theta_j^{\mathrm{shape}}$;
- Wigner-pair data = coupling between atom pairs $\theta_{jk}^{\mathrm{coupling}}$.

Under this reading, σ-rich is *natively* a reservoir observable. σ-standard is its projection-level reduction. **σ-rich is the right framework** for testing reservoir-level transitions; σ-standard is structurally too coarse.

This does **not** prove σ-rich sufficiency. It explains *why* σ-rich is the right candidate: σ-rich invariants live at the reservoir level where the actual transitions occur. Whether σ-rich is *sufficient* (deterministic Φ_rich) remains the WQ-3 question. The reframe sharpens the motivation but does not resolve the mathematical question.

**σ-rich status:** still candidate; still requires (R1)–(R4) of `nq242c_explicit_construction.md` §6.2. The reframe makes σ-rich's design less ad hoc but does not promote it.

### 6.4 WQ-1 retry strategy

The WQ-1 retry options under the layered architecture's `..._next_work.md` were:

- **WQ-1.A** (Option D-1 joint projection) — produces real $K_{\mathrm{act}}$-jumps under different projection dynamics.
- **WQ-1.B** (forced extinction intervention) — tests σ-standard *response* to prescribed extinction.
- **WQ-1.C** (Layer I aggregate-topology reframe) — both pure (F-C1 / F-C7) and projected (R2-F3 / R2-F4) variants exhausted.

**Under the reservoir reinterpretation, the WQ-1 retry priorities change:**

- WQ-1.A (joint projection) is still relevant: it tests whether *under a different projection rule* the labelled K-jumps occur. Useful as a control.
- WQ-1.B (forced extinction) is reframed as: "test what happens to the projection when the reservoir is forcibly truncated mid-trajectory by setting an atom's weight to zero". Useful for understanding projection sensitivity.
- WQ-1.C family is *deprecated* — it tested σ-standard on aggregate transitions, which the WQ-1.C-R2 result confirms σ-standard cannot register.

**Newly motivated work packages:**

- **WQ-RES-1** — Construct a reservoir model (§4.1) for the WQ-1 / WQ-2 trajectories: extract $\nu_t$ from $\mathbf u(t)$ via OT-based atom recovery; verify that $\pi_4(\nu_t)$ matches the actual labelled state.
- **WQ-RES-2** — Test σ-rich at reservoir-level invariants: compute σ-rich on the reservoir atoms directly (rather than on the projected slots) at WQ-2 bar-death events. This is the "σ-rich on reservoir" version of WQ-1.C-R2.
- **WQ-RES-3** — Test reservoir effective rank as K-selection candidate: compute $K^*(\nu_t, \eta)$ along WQ-1 / WQ-2 trajectories; compare to the kinetic-metastability candidate of `k_selection_mechanism.md`.

These are *new* work packages, downstream of this memo. They are not promised by the memo; they are sketched as concrete research directions if the reservoir reading is adopted.

---

## 7. Layered Architecture Compatibility Check

The reservoir reinterpretation does not abandon the Layer I / II / III architecture. It adds a conceptual layer *above* Layer II:

```
Layer 0 (conceptual, this memo): Reservoir ν ∈ M(Θ)  [measure-theoretic]
                                      |
                                      | π_K (projection at chosen K_field rank)
                                      v
Layer II: shared-pool ambient \widetilde{Σ}^{K_field}_M(G_t)
                                      |
                                      | U (aggregate projection)
                                      v
Layer I: primitive single-field ambient Σ_m(G_t)
                                      |
                                      | (per Commitment 11 thresholding)
                                      v
                              Crisp object recovery
```

Layer III (fixed-mass smooth local slices $\Sigma_M^A(\mathbf m_A; G_t)$) sits inside Layer II as before.

The new layer is conceptual and non-canonical. It is not promoted to formal-universe inclusion. Layer II remains the working ambient; the reservoir is a *generator* of Layer II states, not a replacement.

Compatible with all of:

- Commitment 1 ($u_t$ primitive): preserved.
- Commitment 11 (crisp objects derivative): strengthened.
- Commitment 16 ($K_{\mathrm{field}}$ / $K_{\mathrm{act}}$): reread.
- CN5 (4-term independence): unaffected (the reservoir does not introduce new energy terms).
- CN10 (contrastive vs. reductive): preserved if the reservoir framework is treated *contrastively* — i.e. as one possible mathematical scaffolding for the formation count question, not as a reductive identification of SCC with measure theory / spectral theory / nonparametric Bayes. The §4.3 nonparametric model carries the highest CN10 risk; §4.1 carries the lowest.
- CN17 (σ-Labeled Formation Quantization): reread — the σ-tuple now refines a *reservoir-level* atom collection rather than a *projection-level* slot collection.

---

## 8. Non-Claims

This memo does not:

- promote any reservoir model to canonical status;
- claim OP-0005 (K-Selection) is resolved;
- claim OP-0008 (σ-standard K-jump inheritance) is resolved;
- claim σ-rich is sufficient;
- claim Φ_rich is deterministic;
- abandon the Layer I / II / III architecture;
- demote $u_t$ from primitive status (the reservoir is *derived* from / lives *above* $u_t$);
- demote Commitment 16 K_field / K_act decomposition (it is reread, not rejected);
- assert $K_{\mathrm{soft}}^\phi = K_{\mathrm{act}}^\varepsilon$ globally;
- import gauge theory, full category theory, sheaf cohomology, Geometric Langlands, CBF/CLF, neural operators, Koopman operators, or formal verification;
- prove the (1)–(4) ⇒ (5) implication of the bridge lemma;
- claim WQ-1 / WQ-1.C succeeded;
- claim the §4.1 measure-theoretic reservoir is the unique correct reading;
- make any vision / robotics / control / application claim;
- modify any canonical or existing working file;
- assign a new Commitment number;
- promote the reservoir to a Layer in the formal-universe sense.

OP-0008 retains 🟠 HIGH severity. OP-0005 retains 🟠 HIGH severity. OP-0009 sub-items retain their CV-1.5.1 status.

---

## 9. Next Work Packages (Conditional on Reservoir Reading)

If the reservoir reading is provisionally adopted as a working frame, three concrete packages follow. These are *additional* to (not replacements of) the WQ-2.A / WQ-2.B / WQ-2.C / WQ-1.A / WQ-1.B items already documented in `layered_ambient_architecture_next_work.md`.

### WQ-RES-1 — Atom recovery from WQ-1 / WQ-2 trajectories

**Goal.** Given a multi-field trajectory $\mathbf u(t) \in \widetilde\Sigma^4_{90}(T^2_{20})$ from WQ-1 / WQ-2, recover a 4-atom measure-theoretic reservoir $\nu_t = \sum_{j=1}^4 m_j(t) \delta_{\theta_j(t)}$ via OT-based atom-fitting on the aggregate $U(t)$.

**Inputs.** WQ-1 / WQ-2 trajectory data (rerun with field-saving if needed); a fixed bump kernel $b(x; \theta)$ with $\theta = (c, r, A)$.

**Output.** Per-snapshot $\{(c_j, r_j, A_j)\}_{j=1}^4$ + verification that $\pi_4(\nu_t) \approx \mathbf u(t)$ within OT tolerance.

**Effort.** ~2–3 days.

**Forbidden claim.** That this reservoir recovery is unique or canonical-target.

### WQ-RES-2 — Reservoir-level σ-rich at bar-death events

**Goal.** Compute σ-rich (centroids, orientations, Wigner-data) directly on the recovered reservoir atoms $\{\theta_j(t)\}$ at WQ-2 bar-death event brackets. Compare A vs B σ-rich pre/post.

**Inputs.** WQ-RES-1 output; existing `compute_sigma_rich` adapted for reservoir input.

**Output.** Reservoir-level Φ_rich determinism check on the WQ-2 events (the WQ-1.C-R2 σ-test, but at the right level).

**Effort.** ~1 week (depends on WQ-RES-1).

**Forbidden claim.** Φ_rich global determinism; OP-0008 resolution; σ-rich global sufficiency.

### WQ-RES-3 — Reservoir effective rank as K-selection candidate

**Goal.** Compute $K^*(\nu_t, \eta) = \min\{K : W_p(\nu_t, \pi_K(\nu_t)) \le \eta\}$ along WQ-1 / WQ-2 trajectories; compare to the kinetic-metastability barrier-height predictor of `k_selection_b_kramers.md`.

**Inputs.** WQ-RES-1 output; OT-distance machinery (POT library or bespoke implementation on graph metric).

**Output.** Empirical comparison: which of the four K-selection candidates (free-energy variational, kinetic metastability, symmetry-broken stabilizer, reservoir effective rank) best fits R23-style data.

**Effort.** ~1–2 weeks; integrates with WQ-4 of `..._next_work.md`.

**Forbidden claim.** OP-0005 resolution; uniqueness of the reservoir-rank candidate.

---

## 10. Summary

The integer $K$ family ($K_{\mathrm{field}}$, $K_{\mathrm{act}}^\varepsilon$, $K_{\mathrm{soft}}^\phi$) is reread as referring to three different aspects of a *latent formation reservoir* $\mathcal R$ that sits conceptually above the Layer II shared-pool ambient:

- $K_{\mathrm{field}}$ — *finite-rank truncation level* at which $\mathcal R$ is sampled by the projection $\pi_K : \mathcal R \to \widetilde\Sigma^K_M(G)$;
- $K_{\mathrm{act}}^\varepsilon$ — *post-projection thresholded activation count*, dependent on both $K_{\mathrm{field}}$ and $\varepsilon$;
- $K_{\mathrm{soft}}^\phi(U)$ — *field-native morphology count* on the aggregate $U$, which is a *reservoir-level invariant* (truncation-level invariant up to discretization error).

The "creation from nothing" model — labelled slots being independent entities born or annihilated — is empirically refuted by the WQ-1 F2 / WQ-2 F-B6 / WQ-1.C-R2 record. The reservoir reinterpretation explains all three observations under a single coherent picture:

- $K_{\mathrm{act}}$ rigidity = projection rank stability;
- aggregate $K_{\mathrm{bar}}$ mobility = reservoir field $u_\nu$ topological evolution;
- σ-standard insensitivity = projection-level coarseness.

Three candidate reservoir models are catalogued: measure-theoretic (§4.1, **best fit by current evidence**), spectral mode (§4.2, complementary), and nonparametric / infinite-mixture (§4.3, powerful but heavyweight).

Implications:

- OP-0005 (K-Selection) gains a new candidate mechanism: reservoir effective rank.
- OP-0008 (σ-standard K-jump inheritance) is reframed as σ-standard *blindness to reservoir transitions*, not just *under-determination of inheritance*.
- σ-rich's centroid + orientation + Wigner-data are recognized as reservoir-level atom invariants — the design becomes principled, not ad hoc. Sufficiency remains open.
- WQ-1 retry strategy: WQ-1.A and WQ-1.B remain valid; WQ-1.C family is deprecated; new packages WQ-RES-1 / WQ-RES-2 / WQ-RES-3 are sketched.

Layered ambient-state architecture is **preserved**. Canonical commitments are **preserved**. No new primitive is introduced. The reservoir is a conceptual generator, not a Layer.

This memo does not resolve any open problem. It reorganizes the question and identifies the framework in which the questions become sharper. Whether the reservoir reading is correct — and which of the three models is the right one — is a downstream question that the WQ-RES-1 / WQ-RES-2 / WQ-RES-3 packages are designed to test.

---

**End of `reservoir_reinterpretation_of_K.md`.**

**Status: working draft. Non-canonical theoretical memo. Best-fit candidate: §4.1 measure-theoretic reservoir with bump kernel. No canonical promotion. No open problem resolved. Layered architecture preserved.**

**Next step (conditional on user adoption): WQ-RES-1 (atom recovery from WQ-1 / WQ-2 trajectories).**
