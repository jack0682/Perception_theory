# Latent Index Space Design for SCC / Multi-Formation

**File:** `THEORY/working/MF/latent_index_space_design.md`
**Document type:** Non-canonical mathematical-design memo. Working draft. Candidate latent index space $\mathcal A$ specification.
**Created:** 2026-05-02 (post WQ-1.C-R2 + reservoir reinterpretation memo).

**Predecessor / sibling artifacts:**
- `THEORY/working/MF/reservoir_reinterpretation_of_K.md` — conceptual reinterpretation of finite-slot $K$ as truncation of a latent reservoir. **This memo is the mathematical-design follow-up.**
- `THEORY/working/MF/layered_ambient_architecture_{candidate,README,agent_notes,next_work}.md` — Layer I/II/III ambient definitions.
- `THEORY/working/MF/nq242c_results.md` — WQ-1 F2 outcome.
- `THEORY/working/MF/ksoft_kact_bridge_lemma.md` — WQ-2 bridge lemma + F-B6 confirmation.
- `THEORY/working/MF/wq1c_layerI_h0_bardeath_results.md` — WQ-1.C F-C1 / F-C7 outcome.
- `THEORY/working/MF/wq1c_r2_projected_layerII_aggregate_sigma_results.md` — WQ-1.C-R2 F-R2-F3 / F-R2-F4 outcome.
- `THEORY/working/MF/K_status_commitment.md` — Commitment 16 K_field / K_act decomposition.
- `THEORY/working/MF/shared_pool_canonical_proposal.md` — I9' shared-pool ambient.
- `THEORY/working/MF/F_Kstep_K_triple.md` — 4-quantity bridge.
- `THEORY/working/E/soft_K_definition.md` — $K_{\mathrm{soft}}^\phi$ persistence-based.
- `THEORY/working/MF/sigma_rich_augmentation.md` — σ-rich Path B candidate.
- `THEORY/canonical/canonical.md`, `theorem_status.md`, `open_problems.md` — canonical baseline (CV-1.5.1).

---

## 1. Status and Scope

This is a **non-canonical mathematical-design memo**. It does not edit canonical files. It does not promote any object to canonical status. It does not assign a Commitment number.

It introduces a candidate **latent index space** $\mathcal A$ together with a **reservoir state** $\rho : \mathcal A \times X_t \to [0, 1]$ such that the existing finite multi-field state

$$
\mathbf u = (u^{(1)}, \dots, u^{(K_{\mathrm{field}})}) \in \widetilde\Sigma^{K_{\mathrm{field}}}_M(G_t)
$$

can be interpreted as a finite approximation of $\rho$. It does **not** replace the layered ambient-state architecture of `..._candidate.md`. It does **not** discard $K_{\mathrm{field}}$. It reinterprets $K_{\mathrm{field}}$ as a finite-resolution chart on $\mathcal A$.

**Status grade per claim.**

| Claim | Status |
|---|---|
| Layer I / II / III architecture | working-definition safe; **preserved** |
| Commitment 1 ($u_t$ primitive) | canonical theorem-grade; **preserved** |
| Commitment 16 ($K_{\mathrm{field}}$ / $K_{\mathrm{act}}$ decomposition) | canonical theorem-grade; **reinterpreted, not rejected** |
| Latent index space $\mathcal A$ | working-grade conceptual proposal |
| Reservoir state $\rho$ and aggregate projection $U_\rho$ | working-definition safe (within this memo's scope) |
| Three candidate $\mathcal A$ models | candidate frameworks; not all internally equivalent; not promoted |
| Connection to OP-0005, OP-0008, σ-rich | conjectural / downstream — *reframing*, not resolution |

**Out of scope.**

- Resolving OP-0005, OP-0008, OP-0009 sub-items.
- Promoting σ-rich to canonical sufficiency.
- Importing gauge theory, full category theory, sheaf cohomology, Geometric Langlands, CBF / CLF, neural operators, Koopman operators, formal verification.
- Replacing canonical Commitment 1 ($u_t$ primitive). The reservoir lives *above* the primitive single-field, not below.
- Application-domain validation.

---

## 2. Motivation: Why Finite Slots Are Not Primitive

### 2.1 Empirical record

Three converging observations from prior work packages:

| Observation | Source | Implication |
|---|---|---|
| $K_{\mathrm{act}}^\varepsilon$ rigid under Layer II Option D-2 dynamics; min slot mass 23.94 vs ε=0.225 | WQ-1 F2 | finite slots do not extinct under natural dynamics |
| $K_{\mathrm{bar}}^{0.10}(U)$ : 3 → 1 along the same trajectories where $K_{\mathrm{act}}$ is rigid | WQ-2 F-B6 | aggregate field topology moves while labelled count stays static |
| pure Layer I single-field flow exhibits asymmetric event occurrence (B drops, A doesn't) | WQ-1.C F-C1 / F-C7 | aggregate-topology transition is not a property of any single dynamics in isolation |
| σ-standard at the projection level has cluster-pattern $(1,1,1,1,1,1)$ before and after the bar-death | WQ-1.C-R2 F-R2-F3 / F-R2-F4 | finite-coordinate σ does not register reservoir-level transitions |

### 2.2 Diagnosis

The integer family $\{K_{\mathrm{field}}, K_{\mathrm{act}}^\varepsilon, K_{\mathrm{soft}}^\phi\}$ does not consistently count the same thing:

- $K_{\mathrm{act}}^\varepsilon$ counts *active labelled coordinates*. It is a property of the **finite chart**.
- $K_{\mathrm{soft}}^\phi(U)$ counts *robust morphological features* of the aggregate field. It is a property of the **field**.
- $K_{\mathrm{field}}$ caps the number of available labels. It is a property of the **observation rank**.

The "creation from nothing" reading — formations being independent entities born or annihilated — is incompatible with this empirical record. Per `reservoir_reinterpretation_of_K.md` §2–3:

- formations are not "born ex nihilo";
- formations are *resolved* from a deeper field of formation potential;
- $K_{\mathrm{field}}$ is the **finite-rank coordinate chart** on that latent potential;
- $K_{\mathrm{soft}}$ is the **field-native morphology observable**;
- $K_{\mathrm{act}}$ is the **chart-dependent activation diagnostic**.

This memo formalizes the latent potential as the index space $\mathcal A$ and the reservoir state $\rho$.

---

## 3. Existing Architecture Recap

### 3.1 Three layers (preserved)

$$
\text{Layer I: } \quad \Sigma_m(G_t) = \Big\{ u : X_t \to [0, 1] \;\Big|\; \sum_{x \in X_t} u(x) = m \Big\}.
$$

$$
\text{Layer II: } \quad \widetilde\Sigma^{K_{\mathrm{field}}}_M(G_t) = \Big\{ \mathbf u \in [0,1]^{K_{\mathrm{field}} \times X_t} \;:\; \sum_{j,x} u^{(j)}(x) = M, \;\; \sum_j u^{(j)}(x) \le 1 \;\forall x \Big\}.
$$

$$
\text{Layer III: } \quad \Sigma_M^A(\mathbf m_A; G_t) = \big\{ \mathbf u \in \widetilde\Sigma^{K_{\mathrm{field}}}_M(G_t) \;:\; m_j(\mathbf u) = m_j \text{ for } j \in A,\;\; m_j(\mathbf u) = 0 \text{ for } j \notin A \big\}.
$$

### 3.2 Latent index space sits *above* Layer II

The latent index space $\mathcal A$ and reservoir state $\rho$ form a candidate **Layer II∞** — a non-canonical, working-grade conceptual structure that generates Layer II states by truncation:

```
                Layer II∞ (this memo): (A, ρ)         [latent reservoir]
                            ↓ π_K (truncation to K_field labels)
                Layer II:  \widetilde{Σ}^{K_field}_M(G_t)   [labelled multi-formation]
                            ↓ U (aggregate projection)
                Layer I:   Σ_m(G_t)                          [primitive single-field]
```

The reservoir ambient is denoted

$$
\mathcal R_M(G_t, \mathcal A) := \Big\{ \rho : \mathcal A \times X_t \to [0, 1] \;\Big|\; (\text{constraints, §4 below}) \Big\}.
$$

**Layer II∞ is not a fourth canonical layer.** It is a non-canonical extension that makes precise *where Layer II's $K_{\mathrm{field}}$-slot structure comes from*.

---

## 4. Design Requirements for $\mathcal A$

A candidate latent index space $\mathcal A$ together with a reservoir state $\rho : \mathcal A \times X_t \to [0, 1]$ must satisfy the following design requirements.

### 4.1 Required (R1–R10)

1. **(R1) Finite-rank truncation.** There exists a family of projections $\{\pi_K\}_{K \ge 1}$ with $\pi_K : \mathcal R_M(G_t, \mathcal A) \to \widetilde\Sigma^K_M(G_t)$ such that the existing Layer II state is reached by an appropriate $K = K_{\mathrm{field}}$ choice.

2. **(R2) Latent potential precedes activation.** A reservoir state $\rho$ may carry mass at index $\alpha \in \mathcal A$ that does not appear in the truncation $\pi_{K_{\mathrm{field}}}(\rho)$ for the chosen $K_{\mathrm{field}}$. Latent ≠ active.

3. **(R3) No ex nihilo creation.** A $K$-jump in the truncation ($K_{\mathrm{act}}^\varepsilon$ drops or rises) must correspond to **redistribution of mass within** $\rho$, not to mass appearing or disappearing globally.

4. **(R4) Aggregate is reservoir-level invariant.** The aggregate field

   $$
   U_\rho(x) := \int_{\mathcal A} \rho(\alpha, x)\, d\nu(\alpha) \quad \text{or} \quad \sum_{\alpha \in \mathcal A} \rho(\alpha, x)
   $$

   (depending on whether $\mathcal A$ is continuous or countable) is independent of the truncation rank. $U_\rho \in \Sigma_M(G_t)$ (Layer I).

5. **(R5) Finite slot approximation exists.** For some choice of $K = K_{\mathrm{field}}$ atoms $\{\alpha_j\}_{j=1}^K \subset \mathcal A$ and weights $\{u^{(j)}(\cdot)\}_{j=1}^K$,

   $$
   \rho_K(\alpha, x) := \sum_{j=1}^{K} u^{(j)}(x) \cdot \delta_{\alpha_j}(\alpha)
   $$

   (atomic measure variant) or

   $$
   \rho_K(\alpha, x) := \sum_{j=1}^{K} u^{(j)}(x)\, \psi_j(\alpha)
   $$

   (basis-function variant, with $\{\psi_j\}$ a partition-of-unity-like family on $\mathcal A$) approximates $\rho$ with respect to a chosen distance (OT, $L^p$, persistence-bottleneck) up to a tolerance $\eta(K)$ that vanishes as $K \to \infty$.

6. **(R6) $K_{\mathrm{act}}^\varepsilon$ is a chart-dependent diagnostic.** Given the truncation $\pi_K(\rho) = \mathbf u$, the active count

   $$
   K_{\mathrm{act}}^\varepsilon(\mathbf u) = \#\{ j : m_j(\mathbf u) > \varepsilon \}
   $$

   is a *property of the finite chart*, not of the reservoir state.

7. **(R7) $K_{\mathrm{soft}}^\phi$ is a field-native observable.** The persistence-based soft count

   $$
   K_{\mathrm{soft}}^\phi(U_\rho) = \sum_i \phi(\ell_i(U_\rho))
   $$

   depends only on $U_\rho$ (a Layer I object), $G_t$, and the envelope $\phi$. It is invariant under the truncation rank up to discretization error.

8. **(R8) Future dynamics support.** $\mathcal A$ must support natural definitions of:
   - **activation:** a previously latent index acquires non-zero $\rho$-mass;
   - **deactivation:** an active index's $\rho$-mass goes below threshold;
   - **splitting:** $\rho$-mass at a single index spreads to a neighborhood of indices;
   - **merging:** $\rho$-mass from neighboring indices concentrates at a single index;
   - **resegmentation:** the optimal-$K$ truncation atoms $\{\alpha_j\}$ rearrange.

9. **(R9) Mathematical usability without infinite-dimensional heavy machinery.** $\mathcal A$ should be finite or countable, or admit finite-dimensional truncations that are computationally tractable. Continuum / measure-theoretic versions are admissible but should be approximable by finite versions.

10. **(R10) Code compatibility.** Existing code (`scc/multi.py`, `scc/sigma_rich.py`, `scc/diagnostics.py`, all WQ-1 / WQ-2 / WQ-1.C scripts) must remain runnable as the *finite-truncation* layer. The reservoir is added on top, not retrofitted into existing primitives.

### 4.2 Forbidden (F1–F4)

- **(F1)** $\mathcal A$ must not be promoted to canonical-primitive status. Commitment 1 ($u_t$ primitive) is preserved.
- **(F2)** $\rho$ must not be presented as a probability distribution unless the model explicitly invokes Bayesian / nonparametric machinery (and even then only as analogy, per §7 below).
- **(F3)** Truncation rank $K_{\mathrm{field}}$ must not be eliminated; it must be reread as a *choice*, not as an *ontological fact*.
- **(F4)** Aggregate $U_\rho$ must not be claimed equal to any single $u^{(j)}$ — it is the integral / sum.

---

## 5. Candidate Model I — Measure-Theoretic Reservoir

### 5.1 Index space

$\mathcal A$ is a **measurable space** $(\mathcal A, \mathcal B_{\mathcal A}, \nu)$ equipped with a $\sigma$-finite reference measure $\nu$. Concretely, two natural choices:

- **(M.a)** $\mathcal A = \Theta$ a *finite-dimensional bump-parameter space*: e.g. $\Theta = X_t \times (0, R_{\max}] \times (0, 1] \times [0, 2\pi)$ encoding (center, radius, amplitude, orientation) of a single bump kernel. $\nu$ = Lebesgue on $\Theta$.
- **(M.b)** $\mathcal A = X_t \times \mathcal S$ for a fixed shape space $\mathcal S$ (graph-Hausdorff balls, persistence-stable shapelets, etc.). Each $\alpha = (c, S)$ is a (location, shape) pair. $\nu$ = counting × shape-prior.

### 5.2 Reservoir state

$$
\rho : \mathcal A \times X_t \to [0, 1], \quad (\alpha, x) \mapsto \rho(\alpha, x),
$$

with constraints

$$
0 \le \rho(\alpha, x) \le 1 \quad \nu \otimes \#\text{-a.e.},
$$

$$
\int_{\mathcal A} \sum_{x \in X_t} \rho(\alpha, x)\, d\nu(\alpha) = M \quad \text{(total reservoir mass)},
$$

$$
\int_{\mathcal A} \rho(\alpha, x)\, d\nu(\alpha) \le 1 \quad \forall x \in X_t \quad \text{(simplex / box constraint at each site)}.
$$

The first constraint ensures reservoir mass is finite; the third is the field-level box constraint inherited from Layer I.

### 5.3 Aggregate projection

$$
U_\rho(x) := \int_{\mathcal A} \rho(\alpha, x)\, d\nu(\alpha) \in [0, 1].
$$

Mass conservation: $\sum_x U_\rho(x) = M$. Therefore $U_\rho \in \Sigma_M(G_t)$ — the Layer I primitive single-field ambient.

### 5.4 Finite slot truncation

For atoms $\{\alpha_j\}_{j=1}^K \subset \mathcal A$ and weights $\{u^{(j)} \in [0, 1]^{X_t}\}_{j=1}^K$,

$$
\rho_K(\alpha, x) := \sum_{j=1}^{K} u^{(j)}(x) \cdot \delta_{\alpha_j}(\alpha) \quad \text{(atomic measure)},
$$

or, for differentiability convenience,

$$
\rho_K(\alpha, x) := \sum_{j=1}^{K} u^{(j)}(x)\, \psi_j(\alpha), \qquad \int_{\mathcal A} \psi_j(\alpha)\, d\nu(\alpha) = 1, \quad \mathrm{supp}\,\psi_j \cap \mathrm{supp}\,\psi_k = \emptyset \text{ for } j \ne k.
$$

The truncation map $\pi_K : \rho \mapsto \rho_K$ is realized e.g. by Wasserstein projection: choose $\{(\alpha_j, u^{(j)})\}_{j=1}^K$ minimizing $W_p(\rho, \rho_K)$ for some $p \ge 1$.

### 5.5 Interpretation of finite $K$

- **$K_{\mathrm{field}}$:** number of atoms / basis functions used in $\rho_K$. Modeling-layer choice.
- **$K_{\mathrm{act}}^\varepsilon(\mathbf u)$:** number of atoms $j$ with $\sum_x u^{(j)}(x) > \varepsilon$. Threshold-gated post-truncation count.
- **$K_{\mathrm{soft}}^\phi(U_\rho)$:** persistence-weighted morphology count of $U_\rho$. Independent of $K_{\mathrm{field}}$.

### 5.6 Advantages

- Most direct expression of latent potential.
- Avoids ex nihilo creation — atom locations $\alpha_j$ persist in $\mathcal A$ even when their finite-truncation weights are zero.
- Finite Layer II model is a quadrature / atomic approximation of an integral.
- Compatible with existing `scc/sigma_rich.py` centroid + orientation: those are atom-parameter readouts.
- Connects to OT machinery; no exotic prerequisites (Villani 2009 *Optimal Transport*, standard).

### 5.7 Risks

- Choice of reference measure $\nu$ on $\Theta$ is non-canonical and consequential.
- Choice of bump kernel (in M.a) or shape space (in M.b) is non-canonical.
- $\rho$ is **non-identifiable from $U_\rho$ alone**: many reservoir states project to the same aggregate. This is *features and bug both* — features because the aggregate is the right invariant; bug because reservoir-level analysis requires more data than $U_\rho$.
- Truncation accuracy depends on the regularity of $\rho$; spiky / fractal reservoirs would require large $K$.
- Computational cost of OT-based projection grows with $K$.

---

## 6. Candidate Model II — Spectral Mode Reservoir

### 6.1 Index space

$\mathcal A = \mathbb N$ (or $\{0, 1, \ldots, |X_t| - 1\}$ for the finite-graph case) — a *spectral parameter set*. Each index $\alpha$ corresponds to an eigenmode of an operator on $G_t$ (graph Laplacian $L_t$, SCC linearized Hessian at a reference state, or similar).

Let $\{\varphi_n : X_t \to \mathbb R\}_{n \in \mathcal A}$ be the corresponding orthonormal eigenmodes ordered by increasing eigenvalue $\lambda_n$.

### 6.2 Reservoir state

$$
\rho : \mathcal A \times X_t \to \mathbb R, \quad \rho(n, x) = a_n\, \varphi_n(x),
$$

where $\{a_n\}_{n \in \mathcal A}$ is a coefficient sequence. Equivalent compact form:

$$
u(x) = \sum_{n \in \mathcal A} a_n \varphi_n(x).
$$

For multi-formation extension, partition $\mathcal A$ into mode packets $\{A_j\}_{j=1}^{K_{\mathrm{field}}}$ with $A_j \cap A_k = \emptyset$ for $j \ne k$ and $\bigcup_j A_j \subseteq \mathcal A$:

$$
u^{(j)}(x) := \sum_{n \in A_j} a_n \varphi_n(x).
$$

The reservoir state is the full sequence $\{a_n\}_{n \in \mathcal A}$; the multi-formation truncation chooses *which packets* and *which modes within packets* to retain.

### 6.3 Aggregate projection

$$
U(x) = \sum_{j=1}^{K_{\mathrm{field}}} u^{(j)}(x) = \sum_{n \in \bigcup_j A_j} a_n \varphi_n(x).
$$

If $\bigcup_j A_j = \mathcal A$ then $U$ is the full reconstruction; if a strict subset, $U$ is a band-limited approximation.

### 6.4 Finite slot truncation

Two truncation knobs:

- **Mode-set truncation:** keep only top-$N$ modes by amplitude $|a_n|$ or by spectral-weight $|a_n|^2$. Discards small-amplitude modes.
- **Packet-set truncation:** group retained modes into $K_{\mathrm{field}}$ packets via a clustering on $\mathcal A$ (e.g. by spectral proximity, by spatial localization of $\varphi_n$, or by frequency band).

A specific finite truncation is parameterized by $(N, K_{\mathrm{field}})$ with $K_{\mathrm{field}} \le N$.

### 6.5 Interpretation of finite $K$

- **$K_{\mathrm{field}}$:** number of mode packets (= number of formations).
- **$K_{\mathrm{act}}^\varepsilon$:** number of packets with non-negligible total spectral weight.
- **$K_{\mathrm{soft}}^\phi(U)$:** persistence count of the reconstructed field — depends on which modes are present and their phases.

### 6.6 Advantages

- Directly tied to the existing graph Laplacian, Hessian, σ-standard machinery (`scc/sigma_rich.py::_sigma_standard` *is* a spectral readout).
- Natural bridge to Wigner / avoided crossing / σ-rich Wigner-data: those are spectral perturbation-theory invariants.
- "Object formation" reads as **localization / condensation of spectral packets**; "K-change" reads as **re-clustering of active packets**.
- Compatible with `mathematical_scaffolding_4tools.md` Tool A1 / A2 (spectral graph theory + symmetry quotients).

### 6.7 Risks

- Spectral modes are **global**; a single Laplacian eigenmode is not a localized formation. The "formation" concept maps to *combinations* of modes, not single modes.
- Packet decomposition is **non-unique**: different clusterings of modes give different multi-formation views of the same field.
- Time-varying graph $G_t$ implies time-varying eigenbasis, complicating tracking.
- Risk of overfitting to σ-framework: if $\mathcal A$ = spectral indices and σ = spectral cluster, the design becomes circular.

---

## 7. Candidate Model III — Nonparametric / Infinite-Mixture Reservoir

### 7.1 Index space

$\mathcal A = \mathbb N$ — a *countable component index set*. Each $k \in \mathcal A$ is a "component" with location / shape parameter $\theta_k$ and weight $w_k \ge 0$.

### 7.2 Reservoir state

$$
\rho(k, x) = w_k\, f_k(x), \quad f_k(x) = b(x; \theta_k),
$$

where $b(\cdot; \theta)$ is a fixed component shape (bump kernel, atom). The aggregate is

$$
U(x) = \sum_{k=1}^{\infty} w_k\, f_k(x), \qquad w_k \ge 0, \quad \sum_k w_k = M.
$$

Components for which $w_k = 0$ are **latent but inactive**; they exist as indices in $\mathcal A$ but do not contribute to $U$. This is the structural difference from Model I: latency is *built in* via countable indexing.

### 7.3 Finite slot truncation

$$
U_K(x) := \sum_{k=1}^{K_{\mathrm{field}}} w_k f_k(x), \qquad U_K \to U \text{ as } K \to \infty
$$

(under tail-decay assumptions on the weight sequence). The active count is

$$
K_{\mathrm{act}}^\varepsilon = \#\{ k : w_k > \varepsilon \} \le K_{\mathrm{field}}.
$$

### 7.4 Probabilistic analogy (optional, marked as analogy)

In Bayesian nonparametrics, the weight sequence $\{w_k\}$ is drawn from a stick-breaking process (Dirichlet process: $w_k = v_k \prod_{l < k}(1 - v_l)$, $v_k \sim \mathrm{Beta}(1, \beta)$). The Indian Buffet Process gives a similar latent-feature structure for binary activation.

**This is an analogy, not a claim that SCC is Bayesian nonparametrics.** The probabilistic machinery (priors, posteriors, sampling) is *not adopted*; only the *structural* picture (countable latent components, sparsity-inducing weight distributions, posterior-effective-K) is borrowed for intuition.

### 7.5 Interpretation of finite $K$

- **$K_{\mathrm{field}}$:** truncation rank — only the top-$K$ components by weight are tracked.
- **$K_{\mathrm{act}}^\varepsilon$:** number of components with weight above threshold.
- **$K_{\mathrm{soft}}^\phi(U)$:** persistence count of the aggregate; not equal to active-component count in general.

### 7.6 Advantages

- Intuitive for variable object count: components always exist; "K-change" is weight redistribution.
- Natural activation / deactivation semantics (R8 of §4.1).
- Computationally approximable: truncation at rank $K$ is well-studied.
- Strong connection to existing K-selection literature in mixture models (concentration parameter, Dirichlet-process effective K).

### 7.7 Risks

- Probabilistic / Bayesian assumptions are not native to SCC. Even as analogy, this drags ontological baggage.
- Choice of base measure / prior dominates posterior in low-data regimes.
- Weight ordering by magnitude breaks permutation invariance — care needed to preserve $S_{K_{\mathrm{field}}}$ symmetry.
- Less directly tied to the SCC energy / σ-standard framework than Models I or II.

---

## 8. Comparison Table

| Aspect | Model I (measure-theoretic) | Model II (spectral mode) | Model III (nonparametric / infinite-mixture) |
|---|---|---|---|
| $\mathcal A$ | measurable space $(\mathcal A, \mathcal B_{\mathcal A}, \nu)$, e.g. bump-parameter $\Theta$ | spectral index set $\mathbb N$ (eigenmodes of Laplacian / Hessian) | countable component set $\mathbb N$ |
| Reservoir state | $\rho(\alpha, x) \in [0, 1]$ on $\mathcal A \times X_t$ | coefficient sequence $\{a_n\}$ with $\rho(n, x) = a_n \varphi_n(x)$ | $\{(w_k, \theta_k)\}_{k \ge 1}$ with $\rho(k, x) = w_k f_k(x)$ |
| Finite $K_{\mathrm{field}}$ meaning | atomic / basis-function quadrature rank | mode-packet count | top-$K$ weight truncation |
| Relation to $U$ | $U = \int \rho\,d\nu$ | $U = \sum_n a_n \varphi_n$ | $U = \sum_k w_k f_k$ |
| Relation to $K_{\mathrm{soft}}^\phi(U)$ | morphology count of integrated bumps | morphology count of band-limited reconstruction | morphology count of mixture |
| Relation to σ-standard | atom-parameter readout (centroid / orientation) | direct spectral readout (FD-Hessian eigenvalues) | mixture-component spectral readout |
| Readiness (current code) | high — `compute_centroids` / `compute_orientations` already align | high — `_sigma_standard` already spectral | medium — needs mixture-model machinery |
| Mathematical prerequisite | finite-measure / OT (low) | spectral graph theory (moderate, already in use) | nonparametric Bayes (high) |
| Key risk | non-identifiability of $\rho$ from $U$ | spectral modes are global, not localized | probabilistic baggage |
| CN10 contrastive boundary | clean (OT is contrastive scaffolding) | clean (spectral theory already used) | strained (Bayesian framework is substantive) |

---

## 9. Recommended Primary Model

### 9.1 Recommendation

- **Primary: Model I — measure-theoretic reservoir.** Most general; lowest mathematical-prerequisite cost; cleanest CN10 contrastive boundary; aligns with existing σ-rich centroid + orientation + Wigner-data design.
- **Secondary: Model II — spectral mode reservoir.** Useful as a *near-term computational bridge* because SCC already uses Laplacians, Hessians, σ-standard. Coexists with Model I as a complementary view (the Wasserstein projection of Model I and the spectral truncation of Model II describe the *same* truncation operation in different coordinates).
- **Tertiary: Model III — nonparametric / infinite-mixture reservoir.** Useful as an *analogy* for variable-K computational models and as a framework for K-selection mechanism research, but the heavyweight probabilistic import is not justified for the current empirical record.

### 9.2 Rationale

Model I best satisfies the design requirements:

| Requirement | Model I | Model II | Model III |
|---|---|---|---|
| R1 finite-rank truncation | ✓ via OT projection | ✓ via mode truncation | ✓ via top-K weight truncation |
| R2 latent potential precedes activation | ✓ (atoms with zero weight remain in $\mathcal A$) | partial (modes always have an amplitude) | ✓ (built in by countable indexing) |
| R3 no ex nihilo | ✓ (atom locations persist) | partial (mode amplitudes can become arbitrarily small) | ✓ (components always exist) |
| R4 aggregate invariant | ✓ | ✓ | ✓ |
| R5 finite slot approximation | ✓ explicit (atomic / partition-of-unity) | ✓ (truncation) | ✓ (top-K) |
| R6 K_act chart-dependent | ✓ | ✓ | ✓ |
| R7 K_soft field-native | ✓ | ✓ | ✓ |
| R8 activation / deactivation / split / merge / resegment | ✓ natural | partial (no clean activation if modes are global) | ✓ natural |
| R9 finite usability | ✓ (Wasserstein on finite atoms) | ✓ (finite eigendecomposition) | ✓ (truncated mixture) |
| R10 code compatibility | ✓ | ✓ | partial |

Model I dominates Model II on R8 (activation semantics) and dominates Model III on R10 (code compatibility) and on CN10 (contrastive scope). Models II and III can be developed *as views of Model I* — Model II as a Fourier-side coordinate change, Model III as an atomic-measure interpretation with stick-breaking weights.

### 9.3 Working frame

Adopt **Model I as the design baseline**. Use Model II's spectral coordinates when σ-standard analysis is the focus. Reserve Model III for K-selection research where its posterior-effective-K machinery is the natural fit.

This is *not* a canonical commitment. It is a working-frame choice for the next downstream work packages.

---

## 10. Relation to $K_{\mathrm{field}}$, $K_{\mathrm{act}}^\varepsilon$, and $K_{\mathrm{soft}}^\phi$

Under the latent-index-space design (Model I):

$$
K_{\mathrm{field}} = \text{finite-resolution chart rank on } \mathcal A;
$$

$$
K_{\mathrm{act}}^\varepsilon(\mathbf u) = \#\{ j \in \{1, \dots, K_{\mathrm{field}}\} : m_j(\mathbf u) > \varepsilon \} = \text{thresholded active-coordinate count};
$$

$$
K_{\mathrm{soft}}^\phi(U_\rho) = \sum_i \phi(\ell_i(U_\rho)) = \text{field-native morphology count}.
$$

### 10.1 What WQ-1 / WQ-2 / WQ-1.C taught us

- **WQ-1 F2:** $K_{\mathrm{act}}$ is rigid under the chosen Layer II dynamics. *Reservoir reading:* the truncation $\pi_4(\rho)$ is dynamically stable at 4 atoms; atom weights redistribute but no atom acquires zero weight.
- **WQ-2 F-B6:** $K_{\mathrm{bar}}^{0.10}(U)$ : 3 → 1. *Reservoir reading:* the aggregate $U_\rho$ undergoes spatial-merging of bumps, registering a topological transition at the field level even though the truncation remains 4-atom.
- **WQ-1.C R2-F3 / R2-F4:** σ-standard cluster pattern $(1,1,1,1,1,1)$ before and after the bar-death; eigenvalue magnitudes shift by O(1). *Reservoir reading:* σ-standard is a *projection-level* observable that reads the FD-Hessian of the truncated field, and its cluster structure is invariant under the spatial bump-merger event.

### 10.2 Hierarchy

The three count quantities sit at three different layers:

```
Reservoir level (Layer II∞):  ρ : A × X_t → [0,1]              (no integer count; full ρ is the state)
                                       ↓ π_K
Truncation level (Layer II):  K_field, K_act^ε                 (integer counts of finite chart)
                                       ↓ aggregation U
Field level (Layer I):        K_soft^φ, K_bar^{ℓ_min}, F       (field-native counts)
```

$K_{\mathrm{soft}}^\phi$ is the count quantity *closest to SCC's field-native objecthood*. $K_{\mathrm{act}}^\varepsilon$ is useful for finite multi-field bookkeeping but is a chart-dependent observable.

### 10.3 Bridge between layers

The bridge inequalities of `F_Kstep_K_triple.md` §3 lift to the reservoir framework:

$$
K_{\mathrm{step}}(U_\rho; \tau) \le \mathcal{F}(U_\rho) \le \infty \text{ (bounded by graph)},
$$

$$
K_{\mathrm{act}}^\varepsilon(\pi_K(\rho)) \le K = K_{\mathrm{field}},
$$

$$
\mathcal{F}(U_\rho) = \sum_{\alpha \in \mathrm{supp}\,\rho_\nu} \mathcal{F}(\rho(\alpha, \cdot)) \quad \text{(well-separated regime)}.
$$

The K-soft / K-act bridge of `ksoft_kact_bridge_lemma.md` §5 lifts to a comparison between $K_{\mathrm{bar}}^{\ell_{\min}}(U_\rho)$ and $K_{\mathrm{act}}^\varepsilon(\pi_K(\rho))$ under well-separation hypotheses.

---

## 11. Relation to OP-0005 K-Selection

### 11.1 Old formulation

> *"What mechanism selects the integer $K$ at which formation count stabilizes?"*

This formulation assumes $K$ is a single, well-defined object whose value is selected by a mechanism.

### 11.2 Reservoir reformulation

> *"What determines the effective resolution of persistent morphology in the aggregate $U_\rho$, and how does a finite coordinate chart $\pi_K$ detect it?"*

Three sub-questions, each potentially distinct:

(a) **Reservoir effective rank:** $K^*_{\mathrm{rank}}(\rho, \eta) := \min \{ K : W_p(\rho, \pi_K(\rho)) \le \eta \}$ — the smallest truncation rank that captures $\rho$ within OT tolerance $\eta$.

(b) **Aggregate persistence count:** $K^*_{\mathrm{pers}}(U_\rho, \ell_{\min}) := K_{\mathrm{bar}}^{\ell_{\min}}(U_\rho)$ — the field-native robust morphology count.

(c) **Chart activation count:** $K^*_{\mathrm{act}}(\pi_K(\rho), \varepsilon) := K_{\mathrm{act}}^\varepsilon(\pi_K(\rho))$ — the chart-dependent active count.

The three need not coincide. (a) is reservoir-level; (b) is field-level; (c) is chart-level. Their relation is governed by:

- (a) ↔ (b): under well-separated hypotheses (R5 + WQ-2 §9.1), $K^*_{\mathrm{rank}}$ and $K^*_{\mathrm{pers}}$ agree up to truncation tolerance.
- (b) ↔ (c): under (R5) + (R6) + sufficient $K_{\mathrm{field}}$, $K^*_{\mathrm{pers}}$ and $K^*_{\mathrm{act}}$ agree per the K-soft / K-act bridge (`ksoft_kact_bridge_lemma.md` §5).
- (a) ↔ (c): chained via (b).

### 11.3 Candidate K-selection mechanisms (under reservoir reformulation)

| Mechanism | Selects which K? | Provenance |
|---|---|---|
| (a) Free-energy variational | $K^*_{\mathrm{act}}$ via energy basin count | `k_selection_a_free_energy.md` |
| (b) Kinetic metastability (Kramers) | $K^*_{\mathrm{act}}$ via barrier rates | `k_selection_b_kramers.md` |
| (c) Symmetry-broken automorphism-stabilizer | $K^*_{\mathrm{act}}$ via stabilizer dim | `k_selection_c_numerical_anchor.md` |
| **(d) Reservoir effective rank (NEW)** | $K^*_{\mathrm{rank}}$ via OT distance to discretization | this memo §5 |
| **(e) Persistence-prominence (NEW)** | $K^*_{\mathrm{pers}}$ via robust bar count | `soft_K_definition.md` + `F_Kstep_K_triple.md` |

### 11.4 Status

OP-0005 is **not resolved**. The reformulation gives two new candidate mechanisms (d) and (e), shifts the question from "select integer $K$" to "select effective resolution", and clarifies that the existing three candidates (a)–(c) all act at the chart level $K^*_{\mathrm{act}}$, leaving the reservoir-level $K^*_{\mathrm{rank}}$ and field-level $K^*_{\mathrm{pers}}$ unaddressed by them.

WQ-4 (`layered_ambient_architecture_next_work.md` K-selection three-model comparison) gains two new candidates and becomes a five-model comparison.

---

## 12. Relation to OP-0008 K-Jump / σ-Inheritance

### 12.1 Old formulation

> *"Does pre-jump σ-standard determine post-jump σ-standard across $K_{\mathrm{act}}^\varepsilon$-jumps?"*

### 12.2 Reservoir reformulation

> *"Does the finite σ-packet observable on $\pi_K(\rho)$ carry sufficient information to determine how the latent reservoir resegments under projection?"*

Three nested observations from WQ-1 / WQ-2 / WQ-1.C:

- $K_{\mathrm{act}}$-jumps **do not occur** under SCC + simplex barrier dynamics in the WQ-1 regime. The OP-0008 question as originally stated tests an event that the dynamics does not produce.
- The closest analogue — aggregate $K_{\mathrm{bar}}$ bar-death — does occur, but σ-standard is structurally insensitive to it (cluster pattern unchanged, eigenvalue drift not informative).
- The reservoir reformulation reveals *why*: σ-standard is a chart-level observable (FD-Hessian on $\pi_K(\rho)$), but the bar-death event is a field-level reorganization of $U_\rho$. The chart-level σ does not see field-level resegmentation.

### 12.3 σ-rich as candidate finite reservoir-statistic

The σ-rich extension (`sigma_rich_augmentation.md`) augments σ-standard with:

- **centroid** $c_j = \int x \rho(\alpha_j, x) dx / m_j$ — atom *location* in $\mathcal A$ ;
- **orientation tensor** $\Theta_j = \int (x - c_j)(x - c_j)^T \rho(\alpha_j, x) dx / m_j$ — atom *shape*;
- **Wigner data** $W_{jk}$ — atom-pair *coupling* (off-diagonal Hessian block).

Under the reservoir reformulation, these are **reservoir-level atom invariants**: they read the parameters $\theta_j = (c_j, \text{shape}_j, \text{coupling}_{jk})$ of the atoms in $\rho_K(\alpha, x) = \sum_j u^{(j)}(x) \delta_{\alpha_j}(\alpha)$.

σ-rich is therefore a **candidate finite sufficient-statistic packet for reservoir transitions**. Whether the packet is *actually sufficient* (Φ_rich determinism, per `nq242c_explicit_construction.md` §6) remains the WQ-3 question. The reframe makes σ-rich's design principled, not ad hoc.

### 12.4 NQ-242c and WQ-1.C as finite-observable insufficiency tests

The NQ-242c protocol and the WQ-1.C / WQ-1.C-R2 retries become tests of:

> *"Is the chart-level σ-standard observable sufficient to determine reservoir-level transitions?"*

The collected outcomes (F2, F-B6, F-C1, F-C7, F-R2-F3, F-R2-F4) consistently say **no** — the chart-level observable does not see reservoir-level structure. They do not say σ-standard "fails" in the sense of giving wrong answers; they say σ-standard is **blind to the relevant level**.

### 12.5 Status

OP-0008 is **not resolved**. The reformulation:

- explains *why* the original test design (labelled K-jumps) does not produce events under natural dynamics;
- reframes incompleteness from "non-determinism of inheritance" to "blindness to reservoir level";
- motivates σ-rich's design as candidate reservoir-level packet, without proving its sufficiency.

OP-0008 retains 🟠 HIGH severity.

---

## 13. Relation to $\sigma_{\mathrm{rich}}$

### 13.1 Reservoir interpretation of σ-rich

Per `sigma_rich_augmentation.md` §2.3, σ-rich = (σ-standard, centroids, orientations, Wigner data).

Under Model I:

- σ-standard ↔ chart-level FD-Hessian readout (projection of reservoir Hessian operator onto truncation modes).
- centroids ↔ atom locations $\theta_j^{\mathrm{location}}$ in $\mathcal A$.
- orientations ↔ atom shape parameters $\theta_j^{\mathrm{shape}}$ (anisotropy tensor).
- Wigner data ↔ atom-pair couplings $\theta_{jk}^{\mathrm{coupling}}$ (cross-block Goldstone gap + mixing).

σ-rich is the **finite chart's best approximation to reservoir-level atom invariants**.

### 13.2 What σ-rich preserves vs. forgets

σ-rich captures (under the bump-kernel atom reservoir):

- atom locations (via centroids);
- atom shapes (via orientations);
- atom-pair couplings (via Wigner data).

σ-rich does *not* capture:

- intra-atom internal multimodality ($\mathcal{F}(\rho(\alpha_j, \cdot)) > 1$);
- subdominant atoms ($w_k$ below σ-rich's resolution);
- atom-class multiplicity beyond pair couplings (3-atom interactions).

### 13.3 Sufficiency status

Whether σ-rich is sufficient — i.e. whether $\Phi_{\mathrm{rich}}: \sigma_{\mathrm{rich}}(\rho_K(t^-)) \to \sigma_{\mathrm{rich}}(\rho_K(t^+))$ is deterministic across resegmentation events — remains **open**. The reservoir framework explains *why* σ-rich is the right candidate (its components match atom parameters), but does not prove that the chosen components exhaust the relevant information.

This memo does **not** claim σ-rich sufficiency. It claims that σ-rich's design is **principled relative to the reservoir reading**.

---

## 14. Computational Consequences

The reservoir reading suggests several computational protocols.

### 14.1 Treat $K_{\mathrm{field}}$ as a resolution hyperparameter

Run experiments at multiple $K_{\mathrm{field}}$ values and check stability of field-level observables:

```
K_field ∈ {3, 4, 6, 8, 12}
```

Expected behavior: $K_{\mathrm{soft}}^\phi(U)$ should *converge* as $K_{\mathrm{field}}$ increases past the reservoir's effective rank $K^*_{\mathrm{rank}}$. If $K_{\mathrm{soft}}$ keeps changing as $K_{\mathrm{field}}$ grows, the truncation is still under-resolving the reservoir.

### 14.2 Track field-native observables as primary

Make $U(\mathbf u)$ and $K_{\mathrm{soft}}^\phi(U)$ the *first-class* observables. Track $K_{\mathrm{act}}^\varepsilon$ as a chart-level diagnostic.

### 14.3 Reservoir-consistency diagnostics

For each trajectory, compute:

- $K_{\mathrm{soft}}^\phi(U(t))$ stability across $K_{\mathrm{field}}$ values;
- σ-standard stability across $K_{\mathrm{field}}$ values (truncation-invariance);
- σ-rich stability across $K_{\mathrm{field}}$ values (does σ-rich reduce truncation ambiguity?);
- atom-recovery via OT projection: do the recovered atoms $\{\alpha_j(t)\}$ track continuously, or do they jump as the dynamics resegments?

### 14.4 Possible future scripts

Each is **not** part of this memo; they are sketched as natural downstream artifacts:

- `CODE/scripts/reservoir_resolution_sweep.py` — vary $K_{\mathrm{field}}$, measure observable stability.
- `CODE/scripts/atom_recovery_OT.py` — extract $\rho_K$ from $\mathbf u$ via Wasserstein projection.
- `CODE/scripts/sigma_packet_truncation_invariance.py` — check σ-standard / σ-rich variance across truncation rank.

These scripts are **not implemented** by this memo.

### 14.5 Backward compatibility

Existing scripts (`nq242c_counterexample.py`, `ksoft_kact_diagnostics.py`, `wq1c_layerI_h0_bardeath.py`, `wq1c_r2_projected_layerII_aggregate_sigma.py`) remain runnable as-is. Their outputs are reread under the reservoir framework as **single-resolution slices** of a multi-resolution observation.

---

## 15. Non-Claims

This memo does **not**:

- promote $\mathcal A$ or $\rho$ to canonical status;
- claim OP-0005 (K-Selection) is resolved;
- claim OP-0008 (σ-standard K-jump inheritance) is resolved;
- claim σ-rich is sufficient;
- claim Φ_rich is deterministic;
- commit to any of Models I, II, or III as canonical;
- adopt Bayesian / nonparametric framework for SCC (Model III is presented as analogy only);
- abandon the layered Layer I / II / III architecture;
- abandon Commitment 16 ($K_{\mathrm{field}}$ / $K_{\mathrm{act}}$);
- claim $K_{\mathrm{field}}$ is irrelevant — it remains an essential modeling choice;
- claim $K_{\mathrm{act}}^\varepsilon$ is useless — it remains a useful chart-dependent diagnostic;
- assert $K_{\mathrm{soft}}^\phi = K_{\mathrm{act}}^\varepsilon$ globally;
- prove an infinite-dimensional theorem;
- import gauge theory, full category theory, sheaf cohomology, Geometric Langlands, CBF / CLF, neural operators, Koopman operators, formal verification;
- make any vision / robotics / control / application claim;
- modify any canonical or existing working file;
- assign a new Commitment number.

OP-0008 retains 🟠 HIGH severity. OP-0005 retains 🟠 HIGH severity. OP-0009 sub-items retain their CV-1.5.1 status.

---

## 16. Next Work Packages

Conditional on adoption of the reservoir reading as a working frame, four concrete packages follow. These extend (do not replace) the WQ-1.A / WQ-1.B / WQ-2.A / WQ-2.B / WQ-2.C / WQ-4 / WQ-5 packages already documented in `layered_ambient_architecture_next_work.md`, and the WQ-RES-1 / WQ-RES-2 / WQ-RES-3 packages already sketched in `reservoir_reinterpretation_of_K.md` §9.

### WQ-LAT-1 — Reservoir Resolution Sweep

**Goal.** Empirically test whether $K_{\mathrm{soft}}^\phi(U(t))$ stabilizes as $K_{\mathrm{field}}$ increases past the reservoir's effective rank.

**Inputs.** WQ-1 / WQ-2 trajectory infrastructure (existing scripts); $K_{\mathrm{field}}$ sweep $\{3, 4, 6, 8, 12\}$.

**Output.** Per-$K_{\mathrm{field}}$ trajectory + $K_{\mathrm{soft}}^\phi$ time series. Convergence plot showing $K_{\mathrm{soft}}^\phi$ vs $K_{\mathrm{field}}$.

**Success criterion.** $K_{\mathrm{soft}}^\phi$ stabilizes for $K_{\mathrm{field}} \ge K^*$ for some $K^*$; the value $K^*$ is interpretable as reservoir effective rank.

**Forbidden claim.** That $K^*$ resolves OP-0005 K-selection (it is one candidate among five, per §11.3).

**Effort.** ~2 days.

### WQ-LAT-2 — Spectral Packet Prototype

**Goal.** Construct an explicit Model II spectral mode reservoir on $T^2_{20}$. Define mode packets via clustering of Laplacian eigenmodes by spatial localization. Test whether the WQ-2 bar-death event corresponds to a reorganization of the active spectral packets.

**Inputs.** Graph Laplacian of $T^2_{20}$; eigenmode decomposition; WQ-2 trajectories.

**Output.** Per-snapshot spectral-packet decomposition; packet-evolution diagnostic; comparison to aggregate $H_0$ bar-death timing.

**Success criterion.** Bar-death event time correlates with a clean re-clustering of active spectral packets.

**Forbidden claim.** That spectral packets *are* SCC formations (they are a coordinate change, not an ontological identification).

**Effort.** ~3–5 days.

### WQ-LAT-3 — Reservoir Reformulation of OP-0005

**Goal.** Rewrite the K-selection three-model comparison of WQ-4 as a five-model comparison including (d) reservoir effective rank and (e) persistence-prominence. Identify which of the five is closest to the WQ-1 / WQ-2 / WQ-1.C / WQ-1.C-R2 empirical record.

**Inputs.** All five candidate-mechanism working files; WQ-1 / WQ-2 / WQ-1.C trajectory data.

**Output.** Five-model comparison document `THEORY/working/MF/k_selection_five_model_comparison.md`. Falsification register per candidate.

**Success criterion.** A definitive verdict per candidate (passes / fails / partial); OP-0005 *is not resolved*.

**Forbidden claim.** OP-0005 resolution; uniqueness of any single candidate.

**Effort.** ~1 week.

### WQ-LAT-4 — Reservoir Reformulation of OP-0008

**Goal.** Rewrite the σ-standard incompleteness question as "finite-observable insufficiency under latent resegmentation". Articulate which of σ-standard, σ-rich, or σ-rich-extended captures reservoir-level resegmentation events.

**Inputs.** WQ-1.C-R2 result; σ-rich design; reservoir Model I framework.

**Output.** A working document recasting OP-0008 as a chart-level vs. reservoir-level distinction; identification of which finite observables can detect reservoir-level events.

**Success criterion.** Articulated reformulation; OP-0008 *is not resolved*.

**Forbidden claim.** σ-rich sufficiency; deterministic Φ_rich.

**Effort.** ~3–5 days.

### Summary of new packages

| Pkg | Goal | Effort | Forbidden top claim |
|---|---|---|---|
| WQ-LAT-1 | Reservoir resolution sweep over $K_{\mathrm{field}}$ | ~2 days | OP-0005 resolved |
| WQ-LAT-2 | Spectral packet prototype on $T^2_{20}$ | ~3–5 days | Spectral packets ≡ SCC formations |
| WQ-LAT-3 | Five-model K-selection comparison | ~1 week | OP-0005 resolved |
| WQ-LAT-4 | OP-0008 reframe as observable insufficiency | ~3–5 days | OP-0008 resolved |

---

## 17. Summary

- **Finite slots are not primitive.** Per WQ-1 / WQ-2 / WQ-1.C / WQ-1.C-R2 empirical record, the integer $K$ family does not consistently count primitive birth/death events.
- **Latent index space $\mathcal A$ is the proposed extension layer.** The reservoir state $\rho : \mathcal A \times X_t \to [0, 1]$ generates Layer II states by truncation, with aggregate $U_\rho \in \Sigma_M(G_t)$ as a Layer I object.
- **Three candidate models for $\mathcal A$:** measure-theoretic (recommended primary), spectral-mode (recommended secondary, near-term computational bridge), nonparametric / infinite-mixture (analogy only, K-selection-research framework).
- **Three count quantities at three layers:**
  - $K_{\mathrm{field}}$ at the chart level — finite-resolution coordinate count;
  - $K_{\mathrm{act}}^\varepsilon$ at the chart level — thresholded activation diagnostic;
  - $K_{\mathrm{soft}}^\phi(U_\rho)$ at the field level — field-native morphology count, the count closest to SCC's primitive objecthood.
- **Implications:**
  - OP-0005 reformulated as "effective resolution selection"; gains two new candidates (reservoir effective rank, persistence-prominence). Not resolved.
  - OP-0008 reframed as "chart-level σ blindness to reservoir-level events"; explains why labelled $K_{\mathrm{act}}$-jumps are not the natural test. Not resolved.
  - σ-rich's design becomes principled (atom-parameter readouts of bump-kernel reservoir). Sufficiency still open.
  - WQ-1 retry strategy: WQ-1.A and WQ-1.B remain valid; WQ-1.C family is reread as chart-level test of reservoir-level transitions; new WQ-LAT-1..4 packages organize downstream work.
- **What is preserved.** Layer I / II / III architecture; Commitment 1 ($u_t$ primitive); Commitment 11 (crisp objects derivative); Commitment 16 ($K_{\mathrm{field}}$ / $K_{\mathrm{act}}$ decomposition, reread); CN5; CN10; CN17.
- **What is added.** Layer II∞ as a non-canonical conceptual extension; the latent index space $\mathcal A$ and reservoir state $\rho$ as candidate mathematical objects; three model families with explicit truncation rules.
- **What is not done.** No open problem is resolved. No model is promoted. No theorem is proved. The memo is a *design document* for downstream work.

---

**End of `latent_index_space_design.md`.**

**Status: working draft. Non-canonical mathematical-design memo. Recommended primary model: measure-theoretic reservoir (§5). Recommended secondary: spectral mode reservoir (§6). Tertiary (analogy only): nonparametric / infinite-mixture reservoir (§7). No canonical promotion. No open problem resolved. Layered architecture preserved.**

**Next step (conditional on user adoption): WQ-LAT-1 (Reservoir Resolution Sweep, ~2 days) — empirical test whether $K_{\mathrm{soft}}^\phi$ stabilizes as $K_{\mathrm{field}}$ increases.**
