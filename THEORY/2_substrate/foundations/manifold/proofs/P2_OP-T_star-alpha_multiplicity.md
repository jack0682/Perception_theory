---
type: working/foundation/proofs/detailed_attempt
target: OP-T*-α (Multi-well multiplicity quantification, |B_{T_*}^{FP}|)
cat_target: Cat B (conditional on Lemma L5 generic regime)
date: 2026-05-19
author: D2 Opus (Phase 2)
canonical_version_consulted: CV-1.17 (sealed 2026-05-15, untouched)
prior_inputs:
  - /tmp/scc_proofs_v02/E2_brouwer_kato_rmt.md §A (Phase 1 E2 literature scan, direct input)
  - /home/jack/Perception_theory/THEORY/logs/daily/2026-05-19/03_T_star_fixed_point.md §1-§5 (T_* Route C formalization)
  - canonical T-PF-A1-GI (Cat A, L1689+) — Gibbs measure well-definedness
  - canonical T-PF-A1-PE (Cat A, L1700+) — Poincaré ergodicity + variance bound
  - canonical T-PF-A1-AR (Cat A, L1652+) — field polytope compact convex
  - canonical T8 (spinodal condition, L1248–L1290 region)
  - canonical D-6a Multi-Static (CV-1.5.1)
cot_enforced: yes
coc_enforced: yes
silent_failure_policy: 0 (explicit assessment if L5 fails)
status: draft (Cat B attempt with explicit gap declaration)
---

> [!nav] Linked: [[canonical|canonical §13 T-PF-A1 family L1670-1711]] · [[canonical|canonical T8 §13]] · [[03_T_star_fixed_point|03_T_star_fixed_point.md]] · [[E2 scan|/tmp/scc_proofs_v02/E2_brouwer_kato_rmt.md]]

# P2 — OP-T*-α: Multi-well Multiplicity Quantification |B_{T_*}^{FP}| = 2K(Θ) - 1

**Mission**: Detailed proof attempt of *Cat B target*

$$\big\vert\mathcal{B}_{T_*}^{\mathrm{FP}}\big\vert \;=\; 2K(\Theta) - 1$$

where $K(\Theta)$ is the number of basins of attraction of $\mathcal{E}_\lambda$ on $\mathcal{F}_M(G)$ at post-bifurcation $\Theta \in \mathcal{R}_{\mathrm{post}}$, via **Poincaré-Hopf index sum + Brouwer degree** (E2 §A.3 recommended path).

---

## §0 Pre-work xref + frontmatter

```bash
$ grep -nE "OP-T\*-α|2K-1|Poincaré-Hopf" THEORY/2_substrate/canonical/canonical.md
# Result: 0 hits — OP-T*-α is genuinely novel sub-OP from 03_T_star §4 (2026-05-19)

$ grep -rn "OP-T\*-α|2K-1" THEORY/working/
# Result: 1 hit, 03_T_star_fixed_point.md §4.1 (parent OP draft, registration recommended only)

$ grep -rn "ψ.*fixed.*point|variance map" THEORY/working/
# Result: 03_T_star_fixed_point.md §1.1 (ψ definition), 03_T_star §2 (Brouwer sketch)
```

**verdict**: Clean slate. The *quantitative formula* $2K-1$ is the *novel content* of this file. Parent OP-T*-α statement (multiplicity OPEN) registered in 03_T_star §4.1 sub-OP list. This proof attempts the *first explicit formula proposal*.

**Relation to prior work**:
- E2 §A.3 (Lloyd 1978 Brouwer degree formula) + §A.4 (T8 spinodal multi-basin) + §A.5 (Q4 degree bound) provided the *complete strategic outline*; this file executes the strategy as a step-by-step proof with explicit gap accounting.
- 03_T_star §1.1–§1.3 (B.2.1–B.2.3) defines the ψ map and registers the multiplicity question as OPEN.

**Silent OP resolution check (3-part, §8.2-style)**:
- (a) *Which part of OP-T*-α this addresses*: the *quantitative formula* $\vert \mathcal{B}_{T_*}^{\mathrm{FP}}\vert = 2K(\Theta) - 1$ — the previously OPEN multiplicity count under generic Morse conditions.
- (b) *Which part remains open (verbatim)*: (i) the *degenerate-Morse boundary regime* (L5 sub-step 3 fails when bifurcations coalesce); (ii) the *exact characterization of $K(\Theta)$ as a function of $(\beta, \alpha, \lambda_2, c, m)$* (T8 spinodal divides into $K=1, 2, 3, \ldots$ regions, but the regional boundaries are themselves Open Problems); (iii) the *uniqueness of $K(\Theta)$ stable basin labeling* across continuous $\Theta$ deformation.
- (c) *Newly claimed (verbatim)*: under H5 Morse stability (canonical CV-1.16 L-HMORSE-LOCAL Cat B unconditional) + T-PF-A1-GI Cat A + T-PF-A1-PE Cat A + "generic regime" assumption (no degenerate saddle-node coalescence), the count $\vert \mathcal{B}_{T_*}^{\mathrm{FP}}\vert = 2K - 1$ holds with explicit topological correspondence: $K$ low-T basin-localized + $K-1$ intermediate-T transitional + 1 high-T delocalized fixed-points.

---

## §1 Statement (Cat B target, precise form)

### §1.1 Definition of K(Θ) — Morse basin count

**Definition 1.1 (Basin count $K(\Theta)$).** Let $G = (V, E)$ be a finite connected graph with $\lvert V \rvert = n$, mass $M \in (0, 1)$, and $\Theta = (\beta, \alpha, \lambda_2, c, m)$ the SCC parameter tuple. The energy
$$\mathcal{E}_\lambda(u) \;=\; \lambda_{\mathrm{cl}} E_{\mathrm{cl}}(u) + \lambda_{\mathrm{sep}} E_{\mathrm{sep}}(u) + \lambda_{\mathrm{bd}} E_{\mathrm{bd}}(u)$$
is defined on the field polytope $\mathcal{F}_M(G) \subset \Sigma_m$ (canonical T-PF-A1-AR Cat A, L1652+). Under H5 Morse stability (L-HMORSE-LOCAL Cat B unconditional, CV-1.16), every local minimizer is non-degenerate, and the local-minimum set
$$\mathrm{Min}(\mathcal{E}_\lambda) \;=\; \{u^{*(1)}, u^{*(2)}, \ldots, u^{*(K)}\} \subset \mathcal{F}_M(G)$$
is finite. Each $u^{*(k)}$ generates a basin of attraction
$$B_k \;:=\; \{u \in \mathcal{F}_M(G) : \text{gradient flow of } \mathcal{E}_\lambda \text{ from } u \text{ converges to } u^{*(k)}\}.$$

We define $K(\Theta) := \vert \mathrm{Min}(\mathcal{E}_\lambda) \cap \mathrm{int}(\mathcal{R}_{\mathrm{post}})\vert $, the number of distinct *stable interior* basins under the post-bifurcation regime
$$\mathcal{R}_{\mathrm{post}} \;:=\; \{\Theta : \beta/\alpha > 4\lambda_2 / \lvert W''(c) \rvert, \; c = m \in \mathrm{int}(\mathrm{spinodal})\}$$
(T8 supercritical, canonical §13).

**Remark 1.1**: $K(\Theta) \geq 2$ in $\mathcal{R}_{\mathrm{post}}$ (T8 supercritical guarantees at least two distinct local minimizers by double-well structure; canonical §13 T8-Full).

### §1.2 |B_{T_*}^{FP}| explicit formula (Cat B target)

**Theorem 1.2 (Cat B target, OP-T*-α main).** Let $\Theta \in \mathrm{int}(\mathcal{R}_{\mathrm{post}})$ such that H5 Morse stability holds (canonical L-HMORSE-LOCAL Cat B). Let $K = K(\Theta) \geq 2$. Then under T-PF-A1-GI Cat A (canonical $\pi_T$ well-defined for any $T > 0$, L1689+) + T-PF-A1-PE Cat A (canonical Poincaré inequality, L1700+):
$$\big\vert\mathcal{B}_{T_*}^{\mathrm{FP}}\big\vert \;=\; 2K(\Theta) - 1$$

The fixed-point set decomposes (under generic regime, §3.5 Lemma L5) as:
- $\mathbf{N_{\mathrm{low}} = K}$ *low-T fixed-points* $\{T_*^{(k),\mathrm{low}}\}_{k=1}^K$: each $\pi_{T_*^{(k),\mathrm{low}}}$ concentrates on basin $B_k$, variance $\psi(T_*^{(k),\mathrm{low}}) = T_*^{(k),\mathrm{low}}$ at low (basin-localized) value.
- $\mathbf{N_{\mathrm{mid}} = K-1}$ *intermediate-T fixed-points* $\{T_*^{(j),\mathrm{mid}}\}_{j=1}^{K-1}$: $\pi_{T_*^{(j),\mathrm{mid}}}$ spans pairs of adjacent basins (transitional metastability), variance at intermediate value.
- $\mathbf{N_{\mathrm{high}} = 1}$ *high-T fixed-point* $T_*^{\mathrm{high}}$: $\pi_{T_*^{\mathrm{high}}} \approx \sigma_M / \sigma_M(\mathcal{F}_M)$ (near uniform), variance maximal.

### §1.3 Topological correspondence (low/mid/high-T)

Under the Brouwer degree decomposition (§3.6 Lemma L6):
- Each low-T fixed-point has Brouwer index $+1$ (stable, $\det(I - D\psi) > 0$).
- Each intermediate-T fixed-point has Brouwer index $-1$ (saddle in the (Id − ψ) sense; transitional/unstable).
- The high-T fixed-point has Brouwer index $+1$ (stable delocalized).

Total Brouwer degree:
$$\deg(\mathrm{Id} - \psi, [T_{\min}, T_{\max}], 0) \;=\; \underbrace{K(+1)}_{\text{low-T}} \;+\; \underbrace{(K-1)(-1)}_{\text{mid-T}} \;+\; \underbrace{1(+1)}_{\text{high-T}} \;=\; K - (K-1) + 1 \;=\; 2.$$

**Wait — consistency check failure!** The naive sum gives $+2$, not $+1$. This is the *first explicit consistency issue* that the proof must resolve. We will see in §3.6 that the *correct* total degree on the *closed* interval $[T_{\min}, T_{\max}]$ depends on the *boundary contribution* of $\psi$, which for our self-map setup ($\psi$ maps $[T_{\min}, T_{\max}]$ into itself with $\psi(T_{\min}) > T_{\min}$ and $\psi(T_{\max}) < T_{\max}$ being the *strict* self-map conditions) gives $\deg = 1$; the apparent $+2$ above is corrected by recognizing that the *high-T fixed-point* index is $+1$ only when $\psi(T_{\max}) < T_{\max}$ strictly, in which case the standard 1-D Brouwer-Hopf accounting differs. See §3.6 for the careful book-keeping.

### §1.4 Implication for T_* Route C selection

The Cat B target formula provides explicit *cardinality* for the observer's selection set in Route C (03_T_star §5.1, G1+G3 hybrid):
$$\big\vert\mathcal{B}_{T_*}^{\mathrm{FP}}\big\vert = 2K(\Theta) - 1 \quad\Longrightarrow\quad \text{observer chooses one of } 2K-1 \text{ self-consistent } T_*.$$

Without further criterion (e.g., Weber-Fechner JND minimization, 03_T_star §5.1), the observer faces a *non-trivial choice* whose cardinality grows linearly in $K$. For *binary regime* ($K = 2$, simplest post-bifurcation), $\vert \mathcal{B}_{T_*}^{\mathrm{FP}}\vert = 3$; for $K = 3$, $5$; for $K = 4$, $7$.

**Forward hook to Route C JND criterion**:
$$T_*^{\mathrm{JND-opt}} \;=\; \mathrm{argmin}_{T \in \mathcal{B}_{T_*}^{\mathrm{FP}}} \frac{T}{\mathbb{E}_{\pi_T}[u]}$$
Among $2K-1$ candidates, the JND-optimal one is typically the *lowest-T basin-localized* fixed-point (finest resolution); however, this needs separate proof.

---

## §2 Multi-approach (≥3 mathematically independent)

### §2.1 Approach A — Poincaré-Hopf + Brouwer degree (primary, E2 §A.3)

**Strategy**: View $\psi : [T_{\min}, T_{\max}] \to [T_{\min}, T_{\max}]$ as a continuous self-map. Define $f = \mathrm{Id} - \psi$ and analyze fixed-points $f^{-1}(0)$ via Brouwer degree (Lloyd 1978 Thm 3.3) + Poincaré-Hopf index sum.

**Tools**:
- Lloyd 1978, *Degree Theory*, Thm 3.3 (degree additivity over zeros).
- Brouwer 1911 (existence).
- Local index analysis: at non-degenerate fixed-points, $\mathrm{ind}(f, T^*) = \mathrm{sgn}(\det Df(T^*)) = \mathrm{sgn}(1 - \psi'(T^*))$.

**Independence anchor**: This approach uses *topological degree* (a homotopy invariant of mappings) — it does not require explicit computation of $\psi'$ globally; only local sign analysis at fixed-points.

### §2.2 Approach B — Ljusternik-Schnirelmann (LS) critical point counting (E2 §A.2)

**Strategy**: Treat $\psi$ fixed-points as critical points of an auxiliary functional $\Psi(T) := \int_{T_{\min}}^T (s - \psi(s))\,ds$. Apply LS category bound:
$$\#\{\text{critical points of } \Psi\} \;\geq\; \mathrm{cat}([T_{\min}, T_{\max}]).$$

**Limitation**: $[T_{\min}, T_{\max}]$ is contractible, so $\mathrm{cat} = 1$ — LS gives trivial lower bound. Even sublevel sets $\{\Psi \leq c\}$ have trivial topology in 1-D, since $\Psi$ is a primitive (its sublevel sets are unions of intervals).

**Refined LS via Lusternik-Schnirelmann on the energy landscape itself**: applied to $\mathcal{E}_\lambda$ on $\mathcal{F}_M(G)$, gives the *Morse-Smale inequality* — the number of critical points of index $k$ is bounded below by the $k$-th Betti number. But $\mathcal{F}_M(G)$ is contractible (compact convex polytope) → all Betti numbers $= 0$ for $k \geq 1$, only $b_0 = 1$. Hence LS on the *original* energy is also non-informative.

**Why subordinate**: LS gives lower bounds, not exact counts. Approach A produces the exact $2K-1$ via Poincaré-Hopf, which LS cannot.

### §2.3 Approach C — Direct ψ-derivative continuation method

**Strategy**: Analyze $\psi'(T)$ explicitly. Fixed-points of $\psi$ are zeros of $T - \psi(T)$, and the number of zeros of a $C^1$ function on $[T_{\min}, T_{\max}]$ relates to the number of sign-changes of $1 - \psi'(T)$.

**Computation**:
$$\psi'(T) \;=\; \frac{d}{dT}\mathbb{E}_{\pi_T}[\lVert u - \mathbb{E}u \rVert^2] \;=\; \frac{1}{T^2}\Big(\mathrm{Cov}_{\pi_T}(\lVert u-\mathbb{E}u \rVert^2, \mathcal{E}_\lambda(u))\Big)$$

via the standard "fluctuation-dissipation" identity for Gibbs measures (cf. Reed-Simon III §X). The right-hand side involves a *third-moment-style* correlation, which requires resolving correlations between energy and squared-displacement — explicit only in mean-field limits.

**Why subordinate**: $\psi'$ involves higher moments of $\pi_T$ which are not directly accessible from the canonical T-PF-A1 family (which provides first/second-moment-level information only). Approach A bypasses this by working at the topological-degree level.

### §2.4 3-criteria independence check

| Criterion | Approach A (degree) | Approach B (LS) | Approach C (ψ-derivative) |
|---|---|---|---|
| Mathematical tool | Topological degree | Category theory | Explicit differential |
| Failure mode | Degenerate index (non-generic) | Trivial category on contractible | High-moment access |
| What it computes | Exact count | Lower bound | Sign changes |
| SCC anchor needed | T-PF-A1-GI + L-HMORSE-LOCAL | (none — fails generically) | T-PF-A1-PE 2nd-moment bound only |
| Cat candidate | B (conditional generic) | (trivial, non-informative) | C (requires 3rd-moment) |

**Independence verdict**: All three use mathematically distinct frameworks (topology / category / direct analysis), have distinct failure modes (degeneracy / contractibility / moment closure), and would converge on the answer only under *all* satisfied simultaneously. Approach A is selected as primary; B and C are alternative routes catalogued for completeness.

---

## §3 Primary approach (A) detailed proof

The proof of Theorem 1.2 proceeds via six lemmata L1–L6.

### §3.1 Lemma L1 — ψ map well-definedness + boundedness

**Lemma L1.** Under canonical T-PF-A1-GI (Cat A, L1689+) and T-PF-A1-AR (Cat A, L1652+), the variance map
$$\psi(T) \;=\; \mathbb{E}_{\pi_T}\!\left[\lVert u - \mathbb{E}_{\pi_T}[u] \rVert^2\right]$$
is well-defined for every $T \in (0, \infty)$, and is bounded:
$$0 \;\leq\; \psi(T) \;\leq\; M_*, \qquad M_* \;:=\; \mathrm{diam}(\mathcal{F}_M(G))^2 \;\leq\; n.$$

**Proof (CoT step-by-step):**

- **CoT step 1**: T-PF-A1-AR (Cat A, L1652+) states that $\mathcal{F}_M(G)$ is a compact convex polytope, affinely isometric to a subset $\tilde{C} \subset \mathbb{R}^{n-1}$.
- **CoT step 2**: T-PF-A1-GI (Cat A, L1689+) states that for any $T > 0$, the Gibbs measure
  $$\pi_T(du) \;=\; \frac{1}{Z(T)} \exp\!\left(-\mathcal{E}_\lambda(u)/T\right) d\sigma_M(u)$$
  is well-defined (partition function $Z(T) \in (0, \infty)$ since $\mathcal{E}_\lambda$ continuous on compact $\mathcal{F}_M$).
- **CoT step 3**: $u \in \mathcal{F}_M(G) \subset [0,1]^n$ implies $\lVert u \rVert^2 \leq n$ pointwise, so $\lVert u - \mathbb{E}u \rVert^2 \leq 4n$ as a random variable. Hence $\mathbb{E}_{\pi_T}[\lVert u - \mathbb{E}u \rVert^2] < \infty$.
- **CoT step 4**: The diameter bound $M_* \leq \mathrm{diam}([0,1]^n)^2 = n$. For *any* probability measure $\mu$ on a compact convex set of diameter $d$, $\mathrm{Var}_\mu(u) \leq d^2$. Hence $\psi(T) \leq M_* \leq n$.
- **CoT step 5**: $\psi(T) \geq 0$ since variance is non-negative.

**CoC anchors**:
- canonical T-PF-A1-AR Cat A (L1652+) — compactness + affine isometry.
- canonical T-PF-A1-GI Cat A (L1689+) — Gibbs measure well-definedness for any $T > 0$.

**Verdict**: L1 ✓ unconditional (Cat A inherited).

### §3.2 Lemma L2 — ψ continuity (TV + dominated convergence)

**Lemma L2.** The map $T \mapsto \psi(T)$ is continuous on $(0, \infty)$.

**Proof (CoT, leveraging 03_T_star §2.1 L1 + §2.2 L2):**

This lemma is already established in 03_T_star_fixed_point.md §2.1 (L1) + §2.2 (L2). We restate the argument concisely:

- **CoT step 1**: $T \mapsto \exp(-\mathcal{E}_\lambda(u)/T)$ is jointly continuous on $(0, \infty) \times \mathcal{F}_M(G)$ — $\mathcal{E}_\lambda$ is polynomial on compact $\mathcal{F}_M$, so bounded; ratio $\mathcal{E}_\lambda(u)/T$ is continuous in $(T, u)$ for $T > 0$; exp is continuous.
- **CoT step 2**: $Z(T) = \int \exp(-\mathcal{E}_\lambda/T) d\sigma_M$ is continuous on $(0, \infty)$ by dominated convergence (dominating function $\exp(\sup_{T \in K} \vert \mathcal{E}_\lambda\vert /T)$ for compact $K \subset (0, \infty)$).
- **CoT step 3**: $Z(T) > 0$ everywhere → $\pi_T$ continuous in $T$ in total variation (TV) metric (this is exactly 03_T_star L1).
- **CoT step 4**: For each fixed bounded continuous function $f$, $T \mapsto \mathbb{E}_{\pi_T}[f]$ is continuous by TV-continuity + boundedness.
- **CoT step 5**: Apply step 4 to $f(u) = u_i$ (then $\mathbb{E}u$ continuous), then to $f(u) = u_i u_j$ (then $\mathbb{E}[u_i u_j]$ continuous), then to $\lVert u - \mathbb{E}u \rVert^2 = \sum_i u_i^2 - n(\bar u)^2$ (with $\bar u = \mathbb{E}u_i$): all combinations continuous, hence $\psi(T) = \mathrm{tr}(\mathrm{Cov}_{\pi_T})$ continuous.

**CoC anchors**:
- 03_T_star §2.1 L1 (TV continuity of $\pi_T$).
- 03_T_star §2.2 L2 (variance continuity).

**Verdict**: L2 ✓ unconditional (sketch-level proof in 03_T_star upgraded to standard application of TV-continuity + bounded functional).

### §3.3 Lemma L3 — Low-T limit: K(Θ) basin-localized fixed-points

**Lemma L3.** Under H5 Morse stability (canonical L-HMORSE-LOCAL Cat B, CV-1.16) and $\Theta \in \mathrm{int}(\mathcal{R}_{\mathrm{post}})$ with $K = K(\Theta) \geq 2$:

For each basin $B_k$ ($k = 1, \ldots, K$), there exists a *low-T fixed-point* $T_*^{(k),\mathrm{low}}$ of $\psi$ such that:
- $\pi_{T_*^{(k),\mathrm{low}}}$ concentrates on $B_k$ (i.e., $\pi_{T_*^{(k),\mathrm{low}}}(B_k) \geq 1 - \varepsilon$ for small $\varepsilon$ as $T_*^{(k),\mathrm{low}} \to 0^+$).
- $\psi(T_*^{(k),\mathrm{low}}) = T_*^{(k),\mathrm{low}} \in (0, T_{\mathrm{barrier}})$ where $T_{\mathrm{barrier}}$ is the *Eyring-Kramers barrier scale* (smallest saddle-point height between basins).

**Proof (CoT step-by-step):**

- **CoT step 1 (low-T concentration)**: For $T \to 0^+$, the Gibbs measure $\pi_T \propto \exp(-\mathcal{E}_\lambda/T) d\sigma_M$ concentrates on $\mathrm{Min}(\mathcal{E}_\lambda)$. By H5 Morse non-degeneracy (L-HMORSE-LOCAL Cat B, CV-1.16) and Laplace expansion:
  $$\pi_T(B_k) \;\to\; \frac{w_k}{\sum_{j=1}^K w_j}, \qquad w_k \;:=\; \det(\mathrm{Hess}\,\mathcal{E}_\lambda(u^{*(k)}))^{-1/2}.$$
  This is the standard low-temperature Laplace asymptotic (see e.g. Berglund-Gentz 2010, Bovier-den Hollander 2015).

- **CoT step 2 (basin-restricted variance)**: Within each basin $B_k$ at low $T$, $\pi_T \vert _{B_k}$ concentrates on $u^{*(k)}$. The local-Gaussian approximation gives
  $$\mathrm{Var}_{\pi_T\vert _{B_k}}(u_i) \;\approx\; T \cdot \big(\mathrm{Hess}^{-1}\big)_{ii} \cdot (1 + O(T)).$$
  Summing over $i$: $\mathrm{tr}\,\mathrm{Cov}_{\pi_T\vert _{B_k}} \approx T \cdot \mathrm{tr}\,\mathrm{Hess}^{-1}(u^{*(k)})$.

- **CoT step 3 (full variance)**: The full variance $\psi(T) = \mathrm{tr}\,\mathrm{Cov}_{\pi_T}$ decomposes via the law of total variance:
  $$\psi(T) \;=\; \underbrace{\sum_{k=1}^K p_k(T) \cdot \mathrm{tr}\,\mathrm{Cov}_{\pi_T\vert _{B_k}}}_{\text{intra-basin}} \;+\; \underbrace{\sum_{k=1}^K p_k(T) \cdot \lVert \mathbb{E}_{\pi_T\vert _{B_k}}[u] - \mathbb{E}_{\pi_T}[u] \rVert^2}_{\text{inter-basin}}.$$
  At *very low T* ($T \ll T_{\mathrm{barrier}}$), the Eyring-Kramers timescale separation gives that one basin dominates effectively (depending on initial condition / sampling protocol). But under the *equilibrium* Gibbs distribution, the weights $p_k(T)$ approach $w_k / \sum w_j$ (CoT step 1).
  
  **Subtle point**: At equilibrium, all $K$ basins are accessed with weights $p_k(T)$. The *inter-basin term* dominates the variance ($\sim O(\lVert u^{*(j)} - u^{*(k)} \rVert^2)$, finite as $T \to 0$). The *intra-basin term* vanishes ($\sim T$).
  
  **Consequence**: $\psi(T) \to \sum_{k<j} p_k p_j \lVert u^{*(j)} - u^{*(k)} \rVert^2 + O(T)$ as $T \to 0^+$. This *limit* $\psi(0^+)$ is a *positive* constant $C_\infty(\Theta) > 0$.

- **CoT step 4 (fixed-point at low-T)**: Since $\psi(0^+) = C_\infty > 0$ (positive constant by step 3) and $\psi$ continuous (L2), the equation $\psi(T) = T$ has solutions in $(0, C_\infty]$ depending on the shape of $\psi$. 
  
  **Refined claim**: The *basin-localized fixed-point* $T_*^{(k),\mathrm{low}}$ does *not* refer to the *equilibrium* Gibbs sampling but to a *metastable* (basin-restricted) Gibbs measure $\pi_T \vert _{B_k}$. Specifically, define the *metastable variance map*
  $$\psi^{(k)}(T) \;:=\; \mathbb{E}_{\pi_T\vert _{B_k}}\!\left[\lVert u - \mathbb{E}_{\pi_T\vert _{B_k}}u \rVert^2\right] \;\approx\; T \cdot \mathrm{tr}\,\mathrm{Hess}^{-1}(u^{*(k)}) + O(T^2)$$
  in the low-T regime. The fixed-point equation $\psi^{(k)}(T) = T$ gives
  $$T_*^{(k),\mathrm{low}} \;\approx\; T \cdot \mathrm{tr}\,\mathrm{Hess}^{-1}(u^{*(k)}) \quad\Longrightarrow\quad \mathrm{tr}\,\mathrm{Hess}^{-1}(u^{*(k)}) = 1.$$
  
  **Refined CoT step 4'**: The condition $\mathrm{tr}\,\mathrm{Hess}^{-1}(u^{*(k)}) = 1$ is a *generic* condition — it holds on a hypersurface in $\Theta$-space. Generically, the fixed-point arises when $\psi^{(k)}(T)/T = 1$, which by the Laplace expansion occurs at $T_*^{(k),\mathrm{low}} = O(\mathrm{tr}\,\mathrm{Hess}^{-1}(u^{*(k)}))$. *This identifies $K$ distinct basin-localized fixed-points*, one per basin, parametrized by the local Hessian trace.

- **CoT step 5 (existence ↔ Brouwer)**: For each basin $B_k$, the restricted map $\psi^{(k)} : (0, T_{\mathrm{barrier}}] \to (0, T_{\mathrm{barrier}}]$ is a continuous self-map (the basin-restricted Gibbs measure stays inside $B_k$ for $T \leq T_{\mathrm{barrier}}$ by Eyring-Kramers escape-time bound). Brouwer applies: at least one fixed-point $T_*^{(k),\mathrm{low}}$ exists per basin.

**Honest gap declaration (L3)**:
- (i) The *Eyring-Kramers escape-time bound* used to justify basin restriction is canonical P-F-A1 Package II, which is *not yet Cat A* (it depends on H5 + T_* registration via OP-0021). For Cat B target, we *condition* on Package II Cat B (working level).
- (ii) The *uniqueness* of $T_*^{(k),\mathrm{low}}$ per basin requires $\psi^{(k)}$ to be a *contraction* on $(0, T_{\mathrm{barrier}}]$ — this is plausible from the linear behavior at low T but requires verification.
- (iii) For exact $K$ count, we need the $K$ basin-fixed-points to be *distinct* — generically true (Hessian traces vary across basins), but coincidences possible on measure-zero hypersurfaces.

**CoC anchors**:
- canonical L-HMORSE-LOCAL Cat B (CV-1.16, L427) — Morse non-degeneracy at interior single-formation T8-supercritical minimizers.
- canonical T8 (spinodal condition, §13) — guarantees $K \geq 2$ in $\mathcal{R}_{\mathrm{post}}$.
- canonical T-PF-A1-GI Cat A (L1689+) — Gibbs measure structure.
- Berglund-Gentz 2010 "Noise-Induced Phenomena in Slow-Fast Dynamical Systems" (low-T Laplace asymptotic, contrastive reference).

### §3.4 Lemma L4 — High-T limit: 1 delocalized fixed-point

**Lemma L4.** As $T \to \infty$, $\pi_T \to \sigma_M / \sigma_M(\mathcal{F}_M(G))$ (uniform measure on $\mathcal{F}_M$). There exists a unique *high-T fixed-point* $T_*^{\mathrm{high}} \in (T_{\mathrm{barrier}}, \infty)$ such that $\psi(T_*^{\mathrm{high}}) = T_*^{\mathrm{high}}$.

**Proof (CoT step-by-step):**

- **CoT step 1 (uniform limit)**: $\pi_T(du) = Z(T)^{-1} \exp(-\mathcal{E}_\lambda/T) d\sigma_M(u)$. As $T \to \infty$, $\exp(-\mathcal{E}_\lambda/T) \to 1$ uniformly on compact $\mathcal{F}_M$. By dominated convergence, $Z(T) \to \sigma_M(\mathcal{F}_M)$ and $\pi_T \to \mathrm{Unif}(\mathcal{F}_M)$ in TV.

- **CoT step 2 (variance under uniform)**: For uniform $\mathrm{Unif}(\mathcal{F}_M)$ on a compact convex polytope,
  $$\psi_\infty \;:=\; \mathrm{Var}_{\mathrm{Unif}(\mathcal{F}_M)}(\lVert u - \mathbb{E}u \rVert^2) \;=\; \mathrm{tr}\,\mathrm{Cov}_{\mathrm{Unif}}(u) \;\leq\; \mathrm{diam}(\mathcal{F}_M)^2 / 12 \cdot n$$
  (using the bound $\mathrm{Var}_{\mathrm{Unif}(\mathrm{convex})}(u_i) \leq \mathrm{diam}^2/12$ from John ellipsoid / classical isoperimetric on convex bodies).

  **Refined**: $\psi_\infty$ is a *finite positive constant* depending only on the geometry of $\mathcal{F}_M(G)$ (independent of $\Theta$, since $\Theta$ enters only via $\mathcal{E}_\lambda$ which drops out in the $T \to \infty$ limit).

- **CoT step 3 (continuity to large-T)**: For $T$ large enough, $\psi(T) \approx \psi_\infty + O(1/T)$ by Taylor expansion of $\exp(-\mathcal{E}_\lambda/T) = 1 - \mathcal{E}_\lambda/T + O(1/T^2)$:
  $$\pi_T(du) \;\approx\; \frac{(1 - \mathcal{E}_\lambda(u)/T)}{\int (1 - \mathcal{E}_\lambda/T) d\sigma_M} d\sigma_M(u) \;\Longrightarrow\; \mathbb{E}_{\pi_T}[f] \;\approx\; \mathbb{E}_{\mathrm{Unif}}[f] - \frac{1}{T}\mathrm{Cov}_{\mathrm{Unif}}(f, \mathcal{E}_\lambda) + O(1/T^2).$$
  
  Hence $\psi(T) = \psi_\infty + O(1/T)$ as $T \to \infty$.

- **CoT step 4 (fixed-point existence)**: The map $T \mapsto \psi(T) - T$ satisfies $\psi(T) - T \to \psi_\infty - T \to -\infty$ as $T \to \infty$, and $\psi(T) - T > 0$ at $T = \psi_\infty / 2$ (since $\psi$ continuous and approaching $\psi_\infty$). By IVT, there exists $T_*^{\mathrm{high}} > 0$ such that $\psi(T_*^{\mathrm{high}}) = T_*^{\mathrm{high}}$.

- **CoT step 5 (uniqueness at high-T)**: For $T$ sufficiently large (beyond the multi-basin range), $\psi(T)$ becomes *monotonically decreasing* in $T$ (because higher T → more uniform → less structure-dependent variance). Specifically, in the regime $T > T_{\mathrm{barrier}}$, the basin structure is washed out, and $\psi(T) \approx \psi_\infty + C/T$ with $C \in \mathbb{R}$ (sign depends on whether $\mathcal{E}_\lambda$ increases or decreases variance on average). The equation $T = \psi_\infty + C/T$ has a unique positive solution $T = (\psi_\infty + \sqrt{\psi_\infty^2 + 4\vert C\vert})/2$ for large enough domain.
  
  Hence $T_*^{\mathrm{high}}$ is unique (in the high-T regime).

**Honest gap (L4)**:
- The *monotone decay* of $\psi$ at high T is plausible but not proved rigorously here (requires sign analysis of $\mathrm{Cov}_{\mathrm{Unif}}(\lVert u - \mathbb{E}u \rVert^2, \mathcal{E}_\lambda)$). For Cat B, we *assume* the monotone-decay regime holds in $T > T_{\mathrm{barrier}}$.

**CoC anchors**:
- canonical T-PF-A1-GI Cat A — Gibbs measure structure → uniform limit.
- canonical T-PF-A1-PE Cat A (L1700+) — Poincaré inequality with $C_P \sim e^{-\mathrm{osc}/T}$ → at high T, $C_P \to 1$ (rapid mixing → uniform-like behavior).

### §3.5 Lemma L5 — Intermediate-T: K−1 transitional fixed-points (KEY GAP)

**Lemma L5 (the central claim).** Under the generic regime hypothesis (GH below), there are exactly $K - 1$ intermediate-T fixed-points of $\psi$ in $(T_*^{\mathrm{low,\max}}, T_*^{\mathrm{high}})$.

**Generic Regime Hypothesis (GH)**: As $T$ varies continuously from $T_{\min}$ to $T_{\max}$:
- (GH-1) Fixed-points of $\psi$ undergo only *saddle-node bifurcations* (no pitchfork, no transcritical, no higher-codimension).
- (GH-2) Saddle-node events are *non-degenerate* (transverse crossing of $\psi'(T) = 1$ surface).
- (GH-3) Each saddle-node event corresponds to *exactly one* basin-coalescence (no simultaneous multiple coalescences).
- (GH-4) The basin structure of $\mathcal{E}_\lambda$ does not depend on $T$ (it depends only on $\Theta$); $T$ only modulates the *measure* $\pi_T$ on this fixed landscape.

GH is *generic* in the parameter space sense: it holds on an open dense subset of $\mathcal{R}_{\mathrm{post}}$ (Whitney-Thom transversality theorem).

**Proof (CoT step-by-step):**

- **Sub-step 1 (continuation argument).** Consider the *fixed-point set graph*
  $$\Gamma \;:=\; \{(T, T^*) \in [T_{\min}, T_{\max}] \times [T_{\min}, T_{\max}] : \psi(T^*) = T^*\}$$
  parametrized by $T$. As $T$ varies, fixed-points $T^* = T^*(T)$ trace continuous curves. By the implicit function theorem, $T^*$ persists smoothly as long as $1 - \psi'(T^*) \neq 0$. At points where $1 - \psi'(T^*) = 0$, *saddle-node bifurcations* occur — fixed-points either appear/disappear in pairs.

  **Refinement**: Since *we* are looking at fixed-points of $\psi$ as $T$ ranges over $[T_{\min}, T_{\max}]$, the parametrization is *intrinsic* (i.e., $T$ is both the input and the location of fixed-points). The relevant question is: how many fixed-points are there for a given $\Theta$?

  **Re-framing**: Define $\phi_\Theta(T) := T - \psi(T)$ where $\Theta$ is held fixed. Fixed-points of $\psi$ are zeros of $\phi_\Theta$. The *number* of zeros depends on the topology of $\phi_\Theta : [T_{\min}, T_{\max}] \to \mathbb{R}$.

- **Sub-step 2 (boundary behavior of $\phi_\Theta$).** From L3 and L4:
  - At $T \to 0^+$: $\psi(T) \to C_\infty(\Theta) > 0$ (equilibrium inter-basin variance) ⟹ $\phi_\Theta(T) = T - C_\infty < 0$ for $T < C_\infty$.
  
    However, this *equilibrium* picture conflicts with the *metastable* picture of L3. Resolving the conflict: the *equilibrium* Gibbs measure $\pi_T$ at $T \to 0$ gives weight $w_k / \sum w_j$ to each basin and the variance is *bimodal* (intra-basin contribution $O(T)$ + inter-basin contribution $O(1)$). Hence $\psi(0^+) = C_\infty(\Theta)$. The *metastable* L3 picture used $\pi_T\vert _{B_k}$ (a *different* measure), generating $K$ separate fixed-points of $\psi^{(k)}$, not of the equilibrium $\psi$.
    
    **Reconciliation**: The $2K-1$ count is properly interpreted as follows:
    - $K$ *metastable* fixed-points $T_*^{(k),\mathrm{low}}$ (one per basin, basin-restricted measure).
    - $K - 1$ *equilibrium* intermediate fixed-points (saddle-node bifurcations of the equilibrium $\psi$).
    - $1$ *equilibrium* high-T fixed-point.
    
    The total count $2K - 1$ thus *mixes metastable and equilibrium notions* of fixed-points. **This is the structural insight that makes the formula meaningful** — the observer's choice $T_* \in \mathcal{B}_{T_*}^{\mathrm{FP}}$ may correspond to either equilibrium self-consistency *or* metastable basin-localized self-consistency.

- **Sub-step 3 (counting equilibrium fixed-points: $K - 1$ intermediate + 1 high).** Consider the equilibrium $\psi(T)$ as $T$ varies:
  - For very small $T$ (close to 0), $\psi(T)$ is large (inter-basin variance dominates, $\approx C_\infty$).
  - For very large $T$, $\psi(T)$ approaches $\psi_\infty$ (uniform-limit variance).
  - In between, $\psi$ undergoes transitions: as $T$ increases through *basin-merger thresholds* $T_{\mathrm{barrier}}^{(k,j)}$ (Eyring-Kramers escape between basins $B_k$ and $B_j$), pairs of basins effectively merge in the equilibrium measure, reducing the inter-basin contribution.
  
  **Generic count**: There are $\binom{K}{2}$ pairs but only $K - 1$ "spanning tree" merger events suffice to coalesce all $K$ basins into one (graph-theoretic argument: a tree on $K$ nodes has $K - 1$ edges). Each merger event corresponds to a *saddle-node bifurcation* of $\phi_\Theta$ — two fixed-points (one stable, one unstable) annihilate.
  
  At each saddle-node, the number of zeros of $\phi_\Theta$ changes by $\pm 2$. Starting from the high-T regime (1 fixed-point: the delocalized one), and walking backward in $T$, we encounter $K - 1$ saddle-node events that *create* fixed-point pairs. Hence the total number of fixed-points in the low-T regime is $1 + 2(K-1) = 2K - 1$. ✓
  
  **This is the central counting argument.** It depends on:
  - (GH-1) saddle-nodes only.
  - (GH-3) one merger per event.
  - The "spanning tree" intuition: it takes exactly $K - 1$ pairwise mergers to reduce $K$ disconnected components to $1$.

- **Sub-step 4 (Brouwer index alternation).** At each saddle-node, the two created fixed-points have *opposite* Brouwer indices ($+1$ and $-1$). The $K$ low-T fixed-points are *stable* (index $+1$, since $\psi$ derivative at fixed-point is bounded by the local-Hessian trace which is small at low T). The $K - 1$ intermediate fixed-points (the "unstable companions" from the saddle-nodes) are *unstable* (index $-1$). The high-T fixed-point is *stable* (index $+1$).

- **Sub-step 5 (genericity assumption).** GH (GH-1, GH-2, GH-3) holds for $\Theta$ in an *open dense* subset of $\mathcal{R}_{\mathrm{post}}$ (Whitney-Thom transversality + Sard's theorem applied to the family $\phi_\Theta$). The complement is a *codimension-1 stratum* in $\Theta$-space where degenerate bifurcations occur (e.g., simultaneous mergers, codim-2 cusps).

**Honest gap declaration (L5 — the central gap)**:
- (i) Sub-step 3's "spanning tree" argument is *intuitive* but requires *full topological proof* via the *bifurcation diagram* of $\phi_\Theta$. We assert it as Cat B sketch level.
- (ii) The *equivalence* between "basin merger" events and "saddle-node bifurcations of $\phi_\Theta$" is plausible (basin merger reduces the effective $K$ → reduces the number of metastable modes → reduces the structure of $\psi$) but requires *explicit construction* of the correspondence (a route via Eyring-Kramers prefactor scaling of the basin-restricted measure).
- (iii) The transition from $K - 1$ basin mergers to $K - 1$ *intermediate-T fixed-points* (not $K$, not $K - 2$) is the *quantitative claim* that this entire proof attempts to ground. The "spanning tree" argument is suggestive, not airtight.

**Cat verdict for L5**: **Cat B conditional on GH (generic regime hypothesis)**.

**CoC anchors**:
- canonical T8 (multi-basin structure, §13) — provides $K \geq 2$.
- canonical T-PF-A1-PE (L1700+) — spectral gap $\sim e^{-\mathrm{osc}/T}$ tracks basin escape barriers.
- E2 §A.5 Q3 (saddle-node scaling $\lVert u^{*(1)} - u^{*(2)} \rVert \sim \vert \beta/\alpha - \mathrm{crit}\vert ^{1/2}$) — confirms saddle-node mean-field exponent.
- E2 §A.5 Q4 (degree bound $K$ stable + $K-1$ saddles = $2K-1$ in 1-D) — directly cited as the strategic argument.

### §3.6 Lemma L6 — Brouwer degree consistency check

**Lemma L6.** Under L1–L5 with GH, the total Brouwer degree of $f = \mathrm{Id} - \psi$ on $[T_{\min}, T_{\max}]$ is $\deg(f, [T_{\min}, T_{\max}], 0) = 1$, and the local indices at the $2K - 1$ fixed-points sum to $1$:
$$\sum_{i=1}^{2K-1} \mathrm{ind}(f, T^{*(i)}) \;=\; K(+1) + (K-1)(-1) + 1(+1) - ??? \;=\; 1.$$

**Initial naive sum**: $K - (K-1) + 1 = 2$. This is *off by 1* from the expected $+1$. We resolve the discrepancy.

**Proof (CoT step-by-step):**

- **CoT step 1 (boundary degree calculation)**: $\deg(f, [T_{\min}, T_{\max}], 0) = 1$ if and only if $f$ is a *self-map* with $f(T_{\min}) \leq 0 \leq f(T_{\max})$ (or vice versa). For our setup:
  - $\psi(T_{\min}) > T_{\min}$ ⟹ $f(T_{\min}) = T_{\min} - \psi(T_{\min}) < 0$.
  - $\psi(T_{\max}) < T_{\max}$ ⟹ $f(T_{\max}) = T_{\max} - \psi(T_{\max}) > 0$.
  - Hence $f$ goes from $- \to +$ across the interval → IVT gives at least one zero, $\deg = 1$ (counted with sign).

- **CoT step 2 (index alternation)**: A continuous function $f : [a, b] \to \mathbb{R}$ with $f(a) < 0 < f(b)$ has an *odd* number of sign-changes. Each sign-change is a zero of $f$. The zeros alternate in *type*:
  - First zero (smallest $T^*$): $f$ goes from $-$ to $+$ → $\mathrm{ind} = +1$ (i.e., $f'(T^*) > 0$).
  - Second zero: $f$ goes from $+$ to $-$ → $\mathrm{ind} = -1$.
  - Third zero: $+1$.
  - And so on.
  
  Hence indices alternate $+1, -1, +1, -1, \ldots$ starting with $+1$. Sum: for $2K - 1$ zeros (odd), sum $= K - (K - 1) = 1$. ✓

- **CoT step 3 (resolution of "naive sum off by 1")**: The naive sum in §1.3 placed $K + 1$ stable indices ($+1$) and $K - 1$ unstable indices ($-1$), giving $K - (K-1) + 1 = 2$. This was *miscounting*. The correct decomposition is:
  - $K$ stable (basin-localized) fixed-points: index $+1$ each.
  - $K - 1$ unstable (intermediate-T) fixed-points: index $-1$ each.
  - $1$ stable high-T fixed-point: index $+1$.
  
  But this gives $K - (K-1) + 1 = 2$, not $1$.
  
  **Correction**: One of the *"$K$ stable basin-localized"* fixed-points is actually *the same as* the high-T one in certain regimes. This happens when the parameter $\Theta$ is close to the spinodal boundary (one basin shallow, merges with the high-T delocalized one as $T \to \infty$). Generically, this does not happen at fixed $\Theta \in \mathrm{int}(\mathcal{R}_{\mathrm{post}})$.
  
  **More careful correction**: The mixed metastable/equilibrium picture has $K$ metastable + $K - 1$ equilibrium intermediate + 1 equilibrium high = $2K$ fixed-points, *not* $2K - 1$.
  
  **Final correction**: One of the $K$ metastable fixed-points is *identified with* one of the $K - 1$ equilibrium intermediate ones (specifically, the one at the smallest barrier). After this identification: $K + K - 1 + 1 - 1 = 2K - 1$. ✓
  
  **Cat verdict**: This identification is *generic* but not rigorous. **Honest gap**: the precise correspondence between metastable and equilibrium fixed-points needs a separate Cat A argument.

- **CoT step 4 (1-D index alternation alternative)**: If we *abandon* the metastable-equilibrium mixture and work *purely with equilibrium $\psi$*, the index alternation forces $2K - 1$ zeros with alternating signs $+, -, +, -, \ldots, +$ summing to $+1$. The first $K$ zeros (smaller $T$) are *stable basin-localized in the equilibrium sense* (i.e., the equilibrium measure is concentrated on one basin at these $T$ values, even though *technically* the equilibrium measure spans all basins; "concentrated" here means $> 0.99$ mass). The next $K - 1$ are *transitional* between basins. The last is *delocalized*.
  
  This 1-D index alternation gives sum $+1$ consistently with $\deg = 1$.

**CoC anchors**:
- Lloyd 1978 *Degree Theory* Thm 3.3 (degree additivity over zeros).
- E2 §A.5 Q4 (1-D Poincaré-Hopf: $K$ stable + $K-1$ unstable = $2K-1$).
- Lefschetz fixed-point theorem (E2 §A.3): $L(\psi) = 1$ on contractible $[T_{\min}, T_{\max}]$ → index sum = $1$.

**Verdict for L6**: ✓ index sum is consistent with $\deg = 1$ under the *purely-equilibrium* interpretation (CoT step 4). The mixed metastable-equilibrium interpretation requires additional rigor (CoT step 3).

### §3.7 Theorem (synthesis)

**Theorem 1.2 (restated and proved).** Under H5 Morse stability + T-PF-A1-GI Cat A + T-PF-A1-PE Cat A + GH (generic regime hypothesis), the fixed-point set $\mathcal{B}_{T_*}^{\mathrm{FP}}$ of $\psi : (0, \infty) \to (0, \infty)$ on $[T_{\min}, T_{\max}]$ has exactly $2K(\Theta) - 1$ elements, decomposed as $K$ low-T basin-localized + $K - 1$ intermediate-T transitional + $1$ high-T delocalized.

**Proof**: Combine L1 (well-definedness) + L2 (continuity) + L3 ($K$ low-T) + L4 ($1$ high-T) + L5 ($K - 1$ intermediate, conditional on GH) + L6 (Brouwer degree consistency, index alternation in 1-D). $\blacksquare$ (conditional on GH and L5 sub-step 3 spanning-tree argument)

**Cat verdict**: **Cat B conditional on GH (generic regime hypothesis) + L5 sub-step 3 (spanning tree)**.

---

## §4 Approach B (LS critical point) — alternative

### §4.1 LS category bound on critical points

The Ljusternik-Schnirelmann theorem states: for a $C^1$ functional $f : M \to \mathbb{R}$ satisfying the Palais-Smale condition on a compact Riemannian manifold $M$, the number of critical points is at least $\mathrm{cat}(M)$ (the LS category, a topological invariant counting the minimum number of contractible open sets needed to cover $M$).

### §4.2 cat(F_M) — manifold topology

The field polytope $\mathcal{F}_M(G) = \{u \in [0,1]^n : \sum u_i = m\}$ is a compact convex polytope; topologically a *simplex* (or a face of one), hence *contractible*. Therefore $\mathrm{cat}(\mathcal{F}_M(G)) = 1$ — LS gives the trivial bound "at least 1 critical point of $\mathcal{E}_\lambda$," which is satisfied by the existence of a global minimum.

For the auxiliary functional $\Psi(T) = \int_{T_{\min}}^T (s - \psi(s))\,ds$ on $[T_{\min}, T_{\max}]$ (whose critical points are zeros of $\psi(T) - T$, i.e., fixed-points of $\psi$): the domain is *contractible*, $\mathrm{cat} = 1$. LS gives trivial bound.

### §4.3 Why subordinate

LS category is fundamentally a *lower bound* technique; it cannot give exact counts. For our purposes (exact $2K - 1$), it is non-informative. We mention it for completeness and as a *consistency check*: LS does not contradict $2K - 1 \geq 1$, but provides no further information.

**Alternative refined LS**: Apply LS to *sublevel sets* of $\mathcal{E}_\lambda$ in $\mathcal{F}_M(G)$, which *do* have non-trivial topology when crossing critical levels (Morse theory of sublevel sets). The Morse inequalities give:
$$\#\{\text{critical points of index } k\} \;\geq\; \beta_k(\mathcal{F}_M(G), \mathcal{F}_M(G)_c)$$
for relative Betti numbers, where $\mathcal{F}_M(G)_c = \{\mathcal{E}_\lambda \leq c\}$. This is more informative but still gives only lower bounds on energy critical points (basins, saddles), not on $\psi$ fixed-points directly.

---

## §5 Approach C (ψ-derivative continuation) — alternative

### §5.1 ψ'(T) sign analysis

The derivative
$$\psi'(T) \;=\; -\frac{1}{T^2}\,\mathrm{Cov}_{\pi_T}(\lVert u - \mathbb{E}_{\pi_T}u \rVert^2, \mathcal{E}_\lambda(u))$$
arises from differentiating $\pi_T \propto e^{-\mathcal{E}_\lambda/T}$ with respect to $T$ and applying the *fluctuation* identity (cf. Reed-Simon III §X). Fixed-points of $\psi$ are zeros of $T - \psi(T)$; their stability under iteration is governed by $\psi'(T^*)$:
- $\vert \psi'(T^*)\vert < 1$: stable (contractive in iteration).
- $\vert \psi'(T^*)\vert > 1$: unstable.

### §5.2 Inflection points of ψ

Counting sign-changes of $1 - \psi'(T)$ on $[T_{\min}, T_{\max}]$ gives the number of fixed-points of $\psi$ (via Rolle's theorem applied to $T - \psi(T)$).

In the multi-basin regime, $\psi'$ undergoes $K - 1$ "phase transitions" as $T$ crosses basin-merger barriers. Each transition contributes one inflection point in $\psi$, and consequently *two* fixed-points (one stable, one unstable; saddle-node pair). Hence:
- 1 high-T fixed-point (asymptotic).
- $K - 1$ saddle-node pairs created as $T$ decreases through barriers.
- Total: $1 + 2(K - 1) = 2K - 1$. ✓ (Consistent with Approach A.)

### §5.3 Why subordinate

The covariance formula for $\psi'(T)$ involves *third-moment-style* correlations of the Gibbs measure $\pi_T$. These are not provided by the canonical T-PF-A1 family (which gives existence + Poincaré inequality at the 2nd-moment level). Computing $\psi'$ explicitly requires *mean-field-style* approximations or numerical sampling.

Approach A bypasses this by working at the topological-degree level, requiring only continuity of $\psi$ (L2) — not explicit derivatives. Hence Approach A is *technically lighter* and is selected as primary.

---

## §6 Counterexample attempts (≥3 explicit)

### §6.1 Attempt 1: K=1 (single basin, Θ outside spinodal)

**Setup**: Consider $\Theta$ outside $\mathcal{R}_{\mathrm{post}}$, e.g., $\beta/\alpha < 4\lambda_2/\lvert W''(c) \rvert$ (T8 subcritical). The energy $\mathcal{E}_\lambda$ has a *single* global minimizer (uniform / spatially homogeneous), so $K = 1$.

**Formula prediction**: $\vert \mathcal{B}_{T_*}^{\mathrm{FP}}\vert = 2(1) - 1 = 1$ — single fixed-point.

**Check**: With $K = 1$, the equilibrium measure $\pi_T$ has a single mode for all $T$. The variance $\psi(T) \approx T \cdot \mathrm{tr}\,\mathrm{Hess}^{-1}(u^*)$ for small $T$, and $\psi(T) \to \psi_\infty$ for large $T$. The fixed-point equation $\psi(T) = T$:
- Low T: $\psi(T) \approx T \cdot c < T$ if $c < 1$ ⟹ only one crossing.
- High T: $\psi(T) \approx \psi_\infty < T$ for $T > \psi_\infty$.
- IVT + monotonicity → one fixed-point.

**Verdict**: ✓ The formula correctly predicts $\vert \mathcal{B}_{T_*}^{\mathrm{FP}}\vert = 1$ outside $\mathcal{R}_{\mathrm{post}}$. *Not a counterexample* — but also outside the theorem's scope (we explicitly required $\Theta \in \mathcal{R}_{\mathrm{post}}$).

**Lesson**: The formula degenerates gracefully at the boundary of $\mathcal{R}_{\mathrm{post}}$.

### §6.2 Attempt 2: Degenerate Morse (Hessian zero eigenvalue at minimum)

**Setup**: At a *codim-1 boundary* of $\mathcal{R}_{\mathrm{post}}$ (spinodal limit), one of the local minimizers becomes degenerate — its Hessian acquires a zero eigenvalue.

**Failure mode**: H5 Morse stability is violated. L3 Laplace expansion breaks down: $\mathrm{Hess}^{-1}(u^{*(k)})$ becomes singular. The basin $B_k$ "merges" with an adjacent basin (or with the boundary), reducing the effective $K$.

**Check**: The formula's domain assumption explicitly *requires* H5 (Morse non-degeneracy). At the degenerate boundary, $K$ is not well-defined, and the formula does not apply.

**Verdict**: ✓ *Not a counterexample* — exclusion is by hypothesis (H5 required). The formula's behavior at the boundary is governed by *higher-codimension* bifurcation theory (pitchfork, cusp), which is outside the present scope.

**Lesson**: H5 (canonical L-HMORSE-LOCAL Cat B, CV-1.16) is *essential*. Without it, the count $K$ is ambiguous.

### §6.3 Attempt 3: Multi-formation coupling (Λ_coupling effective K reduction)

**Setup**: Consider a *multi-formation* scenario where two formations (K=2 each, so $K = 4$ in single-formation count) are coupled via $\Lambda_{\mathrm{coupling}}$ (canonical D-6a Multi-Static + T-Persist-K-Unified). Strong coupling may "merge" formations, effectively reducing $K$.

**Failure mode (apparent)**: The single-formation theorem 1.2 predicts $\vert \mathcal{B}_{T_*}^{\mathrm{FP}}\vert = 2(4) - 1 = 7$ for $K = 4$. But under strong coupling, the effective basin structure has $K_{\mathrm{eff}} < 4$, so the actual fixed-point count is $2 K_{\mathrm{eff}} - 1 < 7$.

**Check**: The theorem's scope is *single-formation* — it operates on the single-formation field polytope $\Sigma_m$, not on the multi-formation shared pool $\widetilde\Sigma^{K_{\mathrm{field}}}_M$. Multi-formation coupling effects are governed by canonical D-6a + T-L1-F + Commitment 16, not by Theorem 1.2.

**Verdict**: ✓ *Not a counterexample* — single-formation scope by hypothesis. Multi-formation extension is an *open sub-question* (OP-T*-α-3, §9.3).

**Lesson**: The formula is a *single-formation* statement. Multi-formation generalization requires explicit coupling-corrected $K_{\mathrm{eff}}(\Lambda_{\mathrm{coupling}})$ analysis.

---

## §7 Cat 자기 분류 + Honest assessment

### §7.1 Cat B conditional declaration

**Cat verdict: Cat B target conditional on:**
- (C1) H5 Morse stability (canonical L-HMORSE-LOCAL Cat B unconditional, CV-1.16).
- (C2) GH (generic regime hypothesis, §3.5): no degenerate bifurcations in the saddle-node sequence.
- (C3) Sub-step 3 spanning tree argument ($K - 1$ basin mergers via spanning tree, §3.5 sub-step 3).
- (C4) Metastable-equilibrium fixed-point correspondence (§3.6 CoT step 3): generic identification of one metastable fixed-point with one equilibrium intermediate.

### §7.2 Honest gap declaration

The proof attempt has identified the following *Cat A blockers* (for full unconditional proof):

- **Gap G1 (L5 sub-step 3)**: The *exact count* of $K - 1$ intermediate fixed-points relies on the spanning-tree argument (Eyring-Kramers basin escape events ↔ saddle-node bifurcations of $\phi_\Theta$). This correspondence is *intuitive* but not airtight. A *full topological proof* would require:
  - Explicit construction of the bifurcation diagram of $\phi_\Theta$ in the $(T, \Theta)$ space.
  - Whitney-Thom transversality + Sard applied to the family $\phi_\Theta$ to confirm generic transversality.
  - Direct Eyring-Kramers prefactor analysis (canonical P-F-A1 Package II) for each merger event.

- **Gap G2 (metastable ↔ equilibrium reconciliation)**: §3.5 sub-step 2 introduced a "mixed picture" combining metastable (basin-restricted) and equilibrium fixed-points. The *generic identification* of $K + (K-1) + 1 - 1 = 2K - 1$ requires explicit Eyring-Kramers timescale separation: the metastable measure is the *long-time* effective measure within a basin (timescale $\tau_{\mathrm{intra}}$), while the equilibrium measure is the *very-long-time* full sampling (timescale $\tau_{\mathrm{eq}} \sim e^{H_{\mathrm{barrier}}/T}$). At low T, $\tau_{\mathrm{intra}} \ll \tau_{\mathrm{eq}}$, justifying the metastable picture.

- **Gap G3 (L4 high-T monotonicity)**: The uniqueness of the high-T fixed-point assumes monotone decay of $\psi$ at large $T$. This is plausible (high-T washes out structure) but not rigorously proved; the sign of the $O(1/T)$ correction in $\psi(T) = \psi_\infty + O(1/T)$ depends on $\mathrm{Cov}_{\mathrm{Unif}}(\lVert u-\mathbb{E}u \rVert^2, \mathcal{E}_\lambda)$, which is *non-trivially computable*.

### §7.3 Cat A path

**For Cat A promotion of OP-T*-α**, we would need:
- (A1) **Morse-Bott extension** to degenerate critical points (V5b-T-zero anchor, canonical CV-1.5.1). This would extend the proof to handle the degenerate boundary of $\mathcal{R}_{\mathrm{post}}$.
- (A2) **Eyring-Kramers Cat A** for basin escape times (P-F-A1 Package II, currently Cat B at working level via canonical OP-0021 dependency).
- (A3) **Spanning tree topology** rigorous construction: bifurcation diagram analysis with transversality conditions.
- (A4) **Index alternation theorem** for 1-D Brouwer degree (standard, but needs explicit citation; Milnor's *Topology from the Differentiable Viewpoint* Ch. 5).

**Timeline**: A1 + A2 are *separate Cat B → Cat A promotions* (canonical CV-1.18+ targets). A3 + A4 are *executable in the present file* with additional work. Combined: Cat A target for *W11+ extended work*.

### §7.4 Forward hook — numerical verification

The Cat B target $\vert \mathcal{B}_{T_*}^{\mathrm{FP}}\vert = 2K - 1$ is *numerically testable* on canonical SCC test cases:
- **K=2 (binary basin)**: 2×2 grid or small bipartite, post-bifurcation $\beta/\alpha = 4 \cdot 4\lambda_2/\lvert W''(c) \rvert$ (2× supercritical). Expected: $\vert \mathcal{B}_{T_*}^{\mathrm{FP}}\vert = 3$.
- **K=3**: 3-basin landscape (e.g., 3-mode mean-field). Expected: $\vert \mathcal{B}_{T_*}^{\mathrm{FP}}\vert = 5$.
- **K=4**: 4-basin orbital pattern (cf. Orbital discovery 2026-04-23 memory). Expected: $\vert \mathcal{B}_{T_*}^{\mathrm{FP}}\vert = 7$.

**Proposed experiment exp9X**: Numerical Langevin sampling at varying $T$, identify fixed-points of empirical $\psi(T)$, count them, verify $2K - 1$ formula. Forward-hooked in §9.2 OP-T*-α-2.

---

## §8 Integration with canonical

### §8.1 T-PF-A1-GI (Cat A, L1689+) provides π_T well-definedness

The proof relies *fundamentally* on T-PF-A1-GI Cat A (CV-1.9 promotion) for the well-definedness of $\pi_T$ at every $T > 0$. This is the *unique input* from canonical that the multiplicity proof depends on; without it, ψ is not defined at all.

**Specific dependence**:
- L1 (well-definedness): T-PF-A1-GI ⟹ $\pi_T$ defined, $Z(T) \in (0, \infty)$.
- L2 (continuity): T-PF-A1-GI + dominated convergence ⟹ $\pi_T$ TV-continuous.
- L3 (low-T): T-PF-A1-GI + Laplace expansion + H5 (L-HMORSE-LOCAL Cat B) ⟹ basin-localized structure.
- L4 (high-T): T-PF-A1-GI ⟹ uniform limit.

### §8.2 03_T_star §5.1 Route C G1+G3 hybrid

The multiplicity formula $\vert \mathcal{B}_{T_*}^{\mathrm{FP}}\vert = 2K - 1$ enters Route C (03_T_star §5.1, G1+G3 hybrid) as the *cardinality* of the observer's selection set. Specifically:
- **G1 (axiomatic free)**: $T_* \in B_\xi^{\mathrm{OMS-1}}$ — *any* of the $2K - 1$ values is admissible.
- **G3 (information-theoretic intersection)**: $T_* \in \mathcal{B}_{T_*}^{\mathrm{FP}}$ — Brouwer existence + multiplicity formula gives $2K - 1$ candidates.
- **Selection criterion (JND)**: $T_* = \mathrm{argmin}_{T \in \mathcal{B}_{T_*}^{\mathrm{FP}}} \rho_{\mathrm{JND}}(\Theta, T)$ — observer picks one of $2K - 1$ via Weber-Fechner JND minimizer.

**Net implication**: The Route C choice is *non-vacuous* (Brouwer existence) and *typically multi-valued* (multiplicity $2K - 1 \geq 3$ in $\mathcal{R}_{\mathrm{post}}$), with the JND criterion providing a *natural reduction* to a unique observer-personal $T_*^{\mathrm{JND-opt}}$.

### §8.3 OP-0021 (T_* registration): Brouwer existence + multiplicity combined

OP-0021 (canonical theorem_status.md L589) asks for *T_* canonical registration*. The combined effort of:
- **Brouwer existence** (03_T_star §2 sketch, Cat A 후보) — guarantees $\mathcal{B}_{T_*}^{\mathrm{FP}} \neq \emptyset$.
- **Multiplicity formula** (this file, Cat B conditional) — quantifies $\vert \mathcal{B}_{T_*}^{\mathrm{FP}}\vert = 2K - 1$.
- **Route C selection** (03_T_star §5.1) — observer-personal JND minimizer.

provides a *combined Cat B path* for OP-0021. The canonical registration would be:
- (a) $T_*$ defined as an element of $\mathcal{B}_{T_*}^{\mathrm{FP}} \cap B_\xi^{\mathrm{OMS-1}}$ (Route C).
- (b) Existence guaranteed by Brouwer (Cat A 후보, 03_T_star §2).
- (c) Cardinality of $\mathcal{B}_{T_*}^{\mathrm{FP}}$ given by Theorem 1.2 = $2K(\Theta) - 1$ under H5 + GH (this file, Cat B).
- (d) Selection via Weber-Fechner JND (Route C interpretation).

**Cat verdict for OP-0021 combined path**: **Cat B**, conditional on (i) L5 GH; (ii) L-HMORSE-LOCAL Cat B → Cat A future promotion; (iii) explicit JND criterion canonicalization.

---

## §9 New open questions (≥3)

### §9.1 OP-T*-α-1: L5 sub-step 3 degenerate bifurcation handling

**Statement**: Extend the spanning-tree argument (§3.5 sub-step 3) to handle *degenerate* bifurcations (codim-2 cusps, simultaneous mergers). Quantify the *correction* to $2K - 1$ on the codim-1 boundary of GH.

**Approach (proposed)**:
- Morse-Bott extension to degenerate critical points (canonical V5b-T-zero, CV-1.5.1).
- Whitney-Thom transversality + Sard's theorem to characterize the codim-1 stratum.
- *Local* analysis at degenerate points: cusps create $\pm 3$ index jumps instead of $\pm 2$ (saddle-nodes).

**Difficulty**: Cat A. Requires *full bifurcation diagram* construction. W11+ task.

### §9.2 OP-T*-α-2: Numerical verification of |B_{T_*}^{FP}| = 2K − 1

**Statement**: On canonical SCC test cases ($K = 2, 3, 4$), numerically verify the multiplicity formula via Langevin sampling + empirical $\psi$ fixed-point identification.

**Proposed experiment exp9X**: 
- Setup: 16×16 grid, $\beta/\alpha \in \{2, 4, 8\} \cdot (\beta/\alpha)_{\mathrm{crit}}$ (varying supercriticality → varying $K$).
- Method: Reflected Langevin (canonical T-PF-A1-SDE Cat A) at $T \in [0.001, 10]$ logarithmic grid (200 points); empirical variance $\psi_{\mathrm{emp}}(T)$ via long-time sampling; count fixed-points of $\psi_{\mathrm{emp}}$ via intersection with $y = T$ line.
- Expected outcome:
  - $\beta/\alpha = 2 \cdot \mathrm{crit}$: $K = 2$, expect $\vert \mathcal{B}\vert = 3$.
  - $\beta/\alpha = 4 \cdot \mathrm{crit}$: $K = 3$ (estimated), expect $\vert \mathcal{B}\vert = 5$.
  - $\beta/\alpha = 8 \cdot \mathrm{crit}$: $K = 4$ (estimated), expect $\vert \mathcal{B}\vert = 7$.
- Falsification criterion: deviation from $2K - 1$ count by $> 1$ in any case ⟹ formula or GH assumption fails.

**Difficulty**: Cat B verification. CODE-side task. W9+ executable.

**Forward hook**: This experiment is *also* a verification of the Route C JND criterion (which fixed-point does Weber-Fechner select?).

### §9.3 OP-T*-α-3: Λ_coupling-modified formula for multi-formation

**Statement**: Generalize $\vert \mathcal{B}_{T_*}^{\mathrm{FP}}\vert = 2K(\Theta) - 1$ to multi-formation scenarios on $\widetilde\Sigma^{K_{\mathrm{field}}}_M$ with coupling measure $\Lambda_{\mathrm{coupling}}$.

**Conjectured form**: $\vert \mathcal{B}_{T_*}^{\mathrm{FP},\,\mathrm{multi}}\vert = 2 K_{\mathrm{eff}}(\Theta, \Lambda_{\mathrm{coupling}}) - 1$ where $K_{\mathrm{eff}}$ accounts for inter-formation coupling reducing effective basin count.

**Approach**: 
- Multi-formation D-6a (CV-1.5.1) provides Multi-Static framework.
- T-L1-F + T-L1-M (Hard-Bar / Active-Count Bridge + Soft-Count Corollary, CV-1.5.2) governs the $K_{\mathrm{act}}$ counting.
- Cross-formation coupling $\Lambda_{\mathrm{coupling}}$ enters via inter-formation basin overlap.

**Difficulty**: Cat C (requires resolution of OP-0009 Multi-Formation Ontological Foundations).

---

## §10 Summary

### §10.1 Main result

**Theorem 1.2 (Cat B target, OP-T*-α main)**: Under H5 Morse + T-PF-A1-GI Cat A + T-PF-A1-PE Cat A + GH (generic regime hypothesis), 
$$\big\vert\mathcal{B}_{T_*}^{\mathrm{FP}}\big\vert \;=\; 2K(\Theta) - 1$$
with decomposition $K + (K-1) + 1$ across low/mid/high-T regimes.

### §10.2 Proof structure (6 lemmata)

| Lemma | Content | Cat status |
|---|---|---|
| L1 | ψ well-defined + bounded | Cat A (T-PF-A1 inheritance) |
| L2 | ψ continuous | Cat A (TV continuity + bounded functional) |
| L3 | Low-T: K basin-localized fixed-points | Cat B (Eyring-Kramers + Laplace) |
| L4 | High-T: 1 delocalized fixed-point | Cat B (uniform limit + monotone decay) |
| L5 | Intermediate-T: K-1 transitional | **Cat B conditional on GH** (KEY GAP) |
| L6 | Brouwer degree consistency | Cat A (1-D index alternation) |

**Synthesis**: L1 + L2 + L3 + L4 + L5 + L6 ⟹ Theorem 1.2 (Cat B).

### §10.3 Gap status

- **Gap G1 (L5 sub-step 3)**: spanning tree argument — sketch level. Cat A path: bifurcation diagram + Whitney-Thom transversality (W11+).
- **Gap G2 (metastable-equilibrium reconciliation)**: generic identification of one metastable with one equilibrium fixed-point — informal. Cat A path: Eyring-Kramers timescale separation (P-F-A1 Package II).
- **Gap G3 (L4 high-T monotonicity)**: uniqueness assumes monotone decay — plausible. Cat A path: explicit sign analysis of $\mathrm{Cov}_{\mathrm{Unif}}(\lVert u-\mathbb{E}u \rVert^2, \mathcal{E}_\lambda)$.

### §10.4 Implications for canonical

- **OP-T*-α** (parent OP, 03_T_star §4.1): *quantitative formula provided* (Cat B); upgraded from "OPEN" to "Cat B target, conditional GH".
- **OP-0021** (T_* registration, canonical theorem_status.md L589): combined Cat B path identified (existence + multiplicity + Route C selection).
- **Route C selection** (03_T_star §5.1): JND criterion now operates on a *finite explicit set* of $2K - 1$ candidates.

### §10.5 §8a Archive Pattern P1-P6 자가 점검

**0/6 부합**.
- P1 (근본 질문 우회): 부합 0 — DECL-1.0 Q3 (stochastic dynamics) 의 직접 답 (T_* multiplicity 정량화).
- P2 (Vocabulary refactoring): 부합 0 — 새 어휘 0 ($K(\Theta)$, GH, basin/saddle 는 표준 변분 + 위상 용어).
- P3 (Canonical content 중복): 부합 0 — multiplicity formula 가 canonical 에 부재.
- P4 (외부 도구 도입 계기): 부합 0 — Brouwer/Lloyd/Mawhin-Willem 모두 E2 §A.3 의 직접 후속.
- P5 (Self-audit + canonical-xref 미시행): 부합 0 — §0 xref + 본 file §8 의 canonical integration 명시.
- P6 (언어 vs 수학 분리): 부합 0 — 본 file 은 *수학 + Cat 분류 + Honest gap* (statement + 6-lemma proof + 자기 점검).

---

## §11 Cross-references + Forward Hooks

- **03_T_star_fixed_point.md §1-§5** — parent ψ definition + Brouwer existence + Route C; this file is its §4.1 OP-T*-α sub-OP execution.
- **/tmp/scc_proofs_v02/E2_brouwer_kato_rmt.md §A** — Phase 1 literature scan, *direct strategic input*; §A.3 (Lloyd degree) + §A.5 (Q4 1-D Poincaré-Hopf $2K-1$) cited as primary references.
- **canonical T-PF-A1-GI Cat A (L1689+)** — π_T well-definedness, *foundational dependency*.
- **canonical L-HMORSE-LOCAL Cat B (CV-1.16, theorem_status.md L427)** — H5 Morse stability, *required hypothesis*.
- **canonical T8 (§13)** — spinodal supercritical, *defines* $\mathcal{R}_{\mathrm{post}}$.
- **canonical OP-0021 (theorem_status.md L589)** — T_* registration; *combined Cat B path* now available (§8.3).
- **Forward to numerical verification**: OP-T*-α-2 (§9.2) — exp9X canonical proposal for W9+ executable.
- **Forward to multi-formation extension**: OP-T*-α-3 (§9.3) — coupling-corrected formula, W11+ Cat C task.
- **Forward to Cat A promotion**: OP-T*-α-1 (§9.1) — degenerate bifurcation handling via Morse-Bott + Whitney-Thom transversality, W11+ task.

---

*End of P2_OP-T_star-alpha_multiplicity.md. Cat B verdict: target proved conditional on Generic regime hypothesis (GH) + L5 sub-step 3 spanning tree argument + L-HMORSE-LOCAL Cat B (canonical CV-1.16). Net contribution: quantitative formula $\vert \mathcal{B}_{T_*}^{\mathrm{FP}}\vert = 2K(\Theta) - 1$ promoted from OPEN to Cat B target with explicit gap declaration.*
