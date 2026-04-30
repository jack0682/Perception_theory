# sigma_topological_invariance.md — σ-tuple Invariance under Graph Homeomorphism / Topological Equivalence (NQ-190)

**Status:** working draft (NQ-190, W5 Day 4+ open question; SF-axis spawn 2026-04-29).
**Author origin:** Commitment 14 σ-tuple is currently defined per-fixed-graph $G$ via $\mathrm{Stab}_{\mathrm{Aut}(G)}(u^*)$; finite-graph hypothesis is essential to T-σ-Lemma-1 (Maschke). T-PreObj-1G establishes *qualitative* graph-class independence of the σ-framework. Open: does the σ-tuple, as a *quantitative* invariant, survive graph isomorphism, subdivision, homotopy equivalence, quasi-isometry, or continuum limit?
**Canonical refs:** §13 T-σ-Lemma-1 (finite-graph Maschke); T-σ-Theorem-3/4 (closed-form $D_4$ free-BC grid); T-PreObj-1G (graph-class independent qualitative result); Commitment 14 (O5)(O5')(O7) σ-tuple definition + tie-break.
**Working refs:** `working/SF/symmetry_moduli.md` §1.1–§1.2 ($\mathrm{Aut}(G)$ action + invariant/equivariant structure); `working/SF/mode_count.md` (Prop 1.3a/b spectral base, $L \times L$ specific); `working/MF/mathematical_scaffolding_4tools.md` Tool A1 (stratified-space generalization), Tool A3 (persistent-homology bridge); `working/MF/F_Kstep_K_triple.md` BC-1 (per-formation/aggregate bridge under WS regime).
**External refs:** Diestel (2017) *Graph Theory* Ch. 1 §1.10 (subdivision, contraction); Chung (1997) *Spectral Graph Theory* Ch. 1 (eigenvalue interlacing under subdivision); von Luxburg (2007) "A Tutorial on Spectral Clustering" §8 (Fiedler stability); Hatcher (2002) *Algebraic Topology* Ch. 0 (CW homotopy equivalence); Goresky–MacPherson (1988) *Stratified Morse Theory*.

---

## §1. Mission

**Question (NQ-190).** Let $G, G'$ be finite simple connected graphs related by a *topological-flavored* equivalence $\Phi: G \rightsquigarrow G'$ (isomorphism, subdivision, edge contraction, homotopy equivalence as 1-complexes, quasi-isometry, or continuum limit). Let $u^*$ be a Morse-0 minimizer of $\mathcal{E}_G$ on $\Sigma_m^\circ(G)$ and $u'^* := \Phi_*(u^*)$ a corresponding minimizer of $\mathcal{E}_{G'}$ (in whatever sense $\Phi$ provides). Is the σ-tuple

$$\sigma(u^*) = \big(\mathcal{F}(u^*);\ \{(n_k, [\rho_k], \lambda_k)\}_{k}\big)$$

invariant under $\Phi$, i.e., $\sigma(u^*) \stackrel{?}{=} \sigma(u'^*)$ (modulo a canonical translation of irrep labels)?

**Strategic frame.** Three sub-questions of decreasing tractability:

- **(Q1, Cat A target):** Graph isomorphism. **Trivially invariant.**
- **(Q2, Cat C target / generic non-invariance):** Edge subdivision / contraction / homotopy equivalence as a 1-complex.
- **(Q3, Cat C target / partial invariance):** Continuum limit ($h \to 0$) — which sub-part of σ-tuple survives?

**Why this matters.** Currently every σ-framework theorem (T-σ-Theorem-3/4, T-σ-Lemma-1) is anchored on a *fixed* graph (typically $D_4$ free-BC $L \times L$ grid). If σ-tuple lacks topological invariance, then OP-0009-Emp R23 fullscale results on 32×32 are graph-class-specific empirical data points, not universal claims. If a partial invariance holds (e.g., $H_0$-component, lowest-eigenvalue ratios, irrep multiplicities modulo refinement), the σ-framework gains cross-graph-class generalization.

---

## §2. Graph topological notions (precise definitions)

### §2.1 Graph isomorphism

$\phi: G = (X, E) \to G' = (X', E')$ is a graph isomorphism iff $\phi$ is a vertex bijection with $\{x, y\} \in E \Leftrightarrow \{\phi(x), \phi(y)\} \in E'$. Equivalently, $A_{G'} = P_\phi A_G P_\phi^\top$ for the permutation matrix $P_\phi$. Diestel (2017) §1.1.

### §2.2 Edge subdivision

Replace edge $\{x, y\} \in E$ by a path $x — z — y$ with $z \notin X$ a fresh vertex. Iterating subdivisions on $G$ produces a *topological refinement* $G_{\mathrm{sub}}$. Diestel (2017) §1.10. The 1-dim CW complex $|G|$ underlying $G$ is unchanged up to homeomorphism by subdivisions: $|G_{\mathrm{sub}}| \cong_{\mathrm{Top}} |G|$.

### §2.3 Edge contraction

Identify endpoints of $\{x, y\} \in E$ to a single vertex $z$, removing the edge. Inverse to subdivision in the topological-equivalence sense (modulo loops/multi-edges, which we excise to retain "simple graph"). Diestel (2017) §1.10.

### §2.4 Homotopy equivalence as 1-complex

Realize $G$ as 1-dim CW complex $|G|$. Two graphs $G, G'$ are *topologically homotopy equivalent* iff $|G| \simeq |G'|$ in $\mathrm{Top}$ (continuous maps $f: |G| \to |G'|, g: |G'| \to |G|$ with $f \circ g \simeq \mathrm{id}$, $g \circ f \simeq \mathrm{id}$). For finite connected graphs, $|G| \simeq \bigvee^r S^1$ where $r = |E| - |X| + 1$ is the cycle rank (Hatcher 2002 Ch. 0). Hence: **two finite connected graphs are homotopy equivalent iff they have the same cycle rank $r$.** A tree ($r=0$) is contractible; any cycle ($r=1$) is $\simeq S^1$.

### §2.5 Quasi-isometry

$\phi: G \to G'$ is a $(K, C)$-quasi-isometry iff $\frac{1}{K} d_G(x, y) - C \leq d_{G'}(\phi(x), \phi(y)) \leq K\, d_G(x, y) + C$ and $\phi(G)$ is $C$-dense in $G'$. Coarse-geometry equivalence; sees only large-scale structure (Bridson–Haefliger 1999).

### §2.6 Continuum limit (graph homeomorphism in scaling sense)

Sequence $G_h$ ($h \to 0$ mesh) embedded in $M \subset \mathbb{R}^d$ with $|X_h| \to \infty$, edges $\to$ infinitesimal links. In the GH (Gromov–Hausdorff) limit, $G_h \to (M, d_M)$ as a metric space; combinatorial Laplacian $L_{G_h}$ (suitably rescaled) converges in spectrum to $-\Delta_M$ (Burago–Ivanov–Kurylev 2011). This is the "graph homeomorphism" sense of NQ-217.

---

## §3. σ-tuple under graph isomorphism (Q1: Trivial Cat A)

**Claim 3.1 (σ-tuple is a graph-isomorphism invariant).** Let $\phi: G \to G'$ be a graph isomorphism, $u^* \in \Sigma_m^\circ(G)$ a Morse-0 minimizer, $u'^* := u^* \circ \phi^{-1}$. Then $\sigma(u'^*) = \sigma(u^*)$ as tuples in the canonical irrep-label translation $\widehat{G_u} \to \widehat{G'_{u'}}$ induced by $\phi$.

*Proof sketch.* Three observations:

1. **Energy invariance.** $\mathcal{E}_{G'}(u'^*) = \mathcal{E}_G(u^*)$ since $\mathcal{E}$ depends on $u$ only through the graph adjacency, which is preserved by $\phi$. (`symmetry_moduli.md` §1.2.)
2. **Hessian conjugation.** $H_{G'}(u'^*) = P_\phi H_G(u^*) P_\phi^\top$, so spectra agree exactly: $\lambda_k(G', u'^*) = \lambda_k(G, u^*)$ for all $k$, and eigenspaces are conjugate under $P_\phi$.
3. **Stabilizer transport.** $\phi$ induces a group isomorphism $\mathrm{Aut}(G) \to \mathrm{Aut}(G')$ by $\pi \mapsto \phi \pi \phi^{-1}$, and this restricts to $G_u := \mathrm{Stab}_{\mathrm{Aut}(G)}(u^*) \xrightarrow{\sim} G'_{u'} := \mathrm{Stab}_{\mathrm{Aut}(G')}(u'^*)$. Irrep labels $[\rho_k]$ on $V_k$ correspond canonically to $[\rho'_k]$ on $V'_k = P_\phi V_k$ under this isomorphism.

Combining: $\mathcal{F}(u^*) = \mathcal{F}(u'^*)$ (local-maxima count is graph-intrinsic — `symmetry_moduli.md` §1.2 + T-σ-Lemma-2 (i)–(ii)), $(n_k, \lambda_k)$ identical, $[\rho_k]$ identical modulo canonical translation. $\Box$

**Claim 3.1' (canonical conjugation-translation rule for the inter-graph setting — joint with NQ-188 §2 Definition 2.1'; Critic carry-forward #1, W5 Day 4 PM Wave 3 revision 2026-04-30).** *(See NQ-188 §2 Definition 2.1'; this file uses the same rule.)* In the graph-isomorphism setting, the isomorphism $\phi: G \to G'$ plays the role of $\pi \in \mathrm{Aut}(G)$ in the intra-graph case. $\sigma(u^*) \equiv \sigma(u'^*)$ iff there exists $\phi: G \to G'$ (a graph isomorphism) such that:

- **(a)** $\phi^{-1} G_{u^*} \phi = G'_{u'^*}$ — stabilizers are conjugate via $\phi$ (equivalently, $\phi$ transports the stabilizer group).
- **(b)** For all $k$, $\rho_k(u'^*) = \rho_k(u^*) \circ \phi^{-1}$ — irrep labels translate under $\phi$.
- **(c)** On Schur-degenerate eigenspaces of $\dim \geq 2$ (multi-dim irreps, e.g., $D_4$ E-irrep), equivalence requires equality of *isomorphism class* of the irrep (not basis choice). Use the canonical conjugacy-class label $[\rho_k]$ throughout.
- **(d)** When $\phi$ is non-unique (i.e., $G \cong G'$ admit multiple isomorphisms, equivalently $\mathrm{Aut}(G)$ acts non-trivially on the isomorphism set), pick the lex-smallest $\phi$ in a fixed total order on graph isomorphisms (the **Mulliken-order convention on $\mathrm{Aut}(G)$**, Commitment 14 O7 sibling, carried over to the inter-graph case).

*Why (c)–(d) are needed here (CN10 contrastive remark).* Claim 3.1 states invariance "modulo canonical translation"; without (c), two computations of $\sigma(u'^*)$ using different $P_\phi$-eigenbases on a degenerate $D_4$ E-irrep eigenspace can yield different irrep labels, defeating the invariance claim. Clauses (c)–(d) make "canonical translation" explicit and decidable. This is an SCC-internal precision requirement, not a borrowing from McKay's canonical labeling or Schur orthogonality in the representation-theory literature (CN10: contrastive, not reductive).

**Status.** **Cat A trivial / definitional.** This is the σ-framework analog of "the Hessian spectrum is a similarity invariant." Verification path: 1 week canonical-merge writeup as a corollary to T-σ-Lemma-1.

**Cat target & promotion.** Cat A (conditional on CV-1.6 adoption of canonical conjugation rule); canonical §13 corollary to T-σ-Lemma-1 ("σ-tuple is a graph-isomorphism invariant"). 1-week effort. See §15 for conditionality details.

---

## §4. σ-tuple under edge subdivision and contraction (Q2: Generic non-invariance)

### §4.1 Subdivision as spectral perturbation

Subdividing edge $\{x, y\}$ into $x - z - y$ adds vertex $z$ (degree 2) and changes:

- $|X| \to |X| + 1$ (manifold dimension of $\Sigma_m$ increases by 1).
- Combinatorial Laplacian $L_G \to L_{G_{\mathrm{sub}}}$: row/column for $z$ has $\deg(z) = 2$ on diagonal, $-1$ to $x$ and $y$.
- Total mass constraint $\sum u_i = m$ now sums over $|X| + 1$ vertices; the old minimizer $u^*$ does *not* directly extend (need to specify $u^*(z)$).

### §4.2 Counterexample (single-edge subdivision changes spectrum)

**Example 4.2 (Path $P_3$ vs $P_4$).** $P_3 = (\bullet — \bullet — \bullet)$ subdivided once gives $P_4 = (\bullet — \bullet — \bullet — \bullet)$. Combinatorial Laplacian eigenvalues:

- $L_{P_3}$ spectrum: $\{0, 1, 3\}$.
- $L_{P_4}$ spectrum: $\{0, 2 - \sqrt{2}, 2, 2 + \sqrt{2}\} \approx \{0, 0.586, 2, 3.414\}$.

The Fiedler eigenvalue $\lambda_2$ drops from $1$ to $0.586$; the spectrum is strictly different, and there is no canonical bijection between $L_{P_3}$ and $L_{P_4}$ eigenvalues (different cardinality). A fortiori, the SCC Hessian spectrum at the corresponding uniform configuration is different — so σ-tuple changes. (Chung 1997 §1.3 documents general spectral interlacing under subdivision: $\lambda_k(G_{\mathrm{sub}}) \neq \lambda_k(G)$ generically.)

### §4.3 Generic non-invariance under homotopy equivalence

A path graph $P_n$ has cycle rank $r = 0$ for all $n \geq 1$, so $|P_n| \simeq \mathrm{point}$ for all $n$ — all path graphs are homotopy-equivalent to a point. But the σ-tuples differ: $L_{P_n}$ eigenvalues are $\{2(1 - \cos(k\pi/n)) : k = 0, 1, \ldots, n-1\}$, which depend on $n$. SCC Hessian at uniform $c\mathbf{1}$ gives $H = 4\alpha L_{P_n} + \beta W''(c) I$, so the eigenvalue tuple $\{\lambda_k\}$ explicitly depends on $n$.

**Conclusion 4.3 (Conjecture BC-2 — σ-tuple is NOT a topological homotopy invariant).** σ-tuple distinguishes graphs with the same cycle rank $r$ but different vertex count $n$. This is *expected*: σ-tuple encodes geometric (eigenvalue, eigenvector) data, while homotopy equivalence is a coarse topological relation that erases vertex count.

### §4.4 Stabilizer behavior under subdivision

Subdivision of a $D_4$-symmetric edge in the $L \times L$ free-BC grid breaks $D_4$ if the subdivision is asymmetric, but a $D_4$-symmetric subdivision (subdivide all four orbit-edges simultaneously) preserves $D_4 \subseteq \mathrm{Aut}(G_{\mathrm{sub}})$. Hence the *irrep-label* part $[\rho_k]$ may survive a symmetry-respecting subdivision, even though the *eigenvalue* part $\lambda_k$ does not.

This is the key partial-invariance hint: **under a symmetry-respecting refinement, the irrep-multiplicity structure $(n_k, [\rho_k])_k$ may be more stable than the eigenvalues $\lambda_k$ themselves.**

**Status.** **Cat C generic (non-invariance) + Cat C partial-invariance conjecture** (irrep labels under symmetry-respecting refinement). Counterexample 4.2 already provides the negative result; the positive irrep-stability is an open conjecture (NQ-190a, deferred to W7+).

---

## §5. σ-tuple under quasi-isometry (Q2 continued)

**Claim 5.1 (σ-tuple is NOT quasi-isometry-invariant).** Quasi-isometry preserves coarse geometry (large-scale distance) but *not* spectral data. Counterexample: the cycle $C_n$ is $(1, 1)$-quasi-isometric to $C_{n+1}$ (insert one vertex), but eigenvalues of $L_{C_n}$ are $\{2(1 - \cos(2\pi k/n)) : k = 0, \ldots, n-1\}$ — visibly $n$-dependent.

**Caveat.** Quasi-isometry preserves the *Cheeger constant* $h(G)$ up to multiplicative factors of $K$, and via Cheeger's inequality, $h(G)^2 / 2 \leq \lambda_2(L_G) \leq 2 h(G)$ — so $\lambda_2$ is preserved up to a multiplicative factor (von Luxburg 2007 §8). This is far weaker than σ-tuple equality.

**Conclusion.** σ-tuple is *eigenvalue-sensitive*; quasi-isometry only controls $\lambda_2$ up to constants. **Cat C non-invariance with explicit counterexample.**

---

## §6. Continuum limit topological invariance (Q3, NQ-217 connection)

### §6.1 Setup

Let $M \subset \mathbb{R}^d$ be a compact smooth manifold with boundary, and $\{G_h\}_{h \to 0}$ a family of graphs embedded in $M$ with mesh $h$ (e.g., $L \times L$ grid with $L = 1/h$). Suitably rescaled SCC energy $\mathcal{E}_{G_h}$ converges to a continuum SCC functional

$$\mathcal{E}_M[u] = \int_M \left[\lambda_{\mathrm{cl}} F_{\mathrm{cl}}(u) + \lambda_{\mathrm{sep}} F_{\mathrm{sep}}(u) + \lambda_{\mathrm{bd}}\big(\alpha |\nabla u|^2 + \beta W(u)\big)\right] dV_M$$

for $u \in H^1(M; [0,1])$, $\int_M u\, dV = m$. The discrete-Hessian spectrum of $L_{G_h}$ converges (in the distributional / pseudo-spectral sense) to that of $-\Delta_M$ (Burago–Ivanov–Kurylev 2011 for GH spectral convergence).

### §6.2 What is topologically invariant in the continuum?

The Laplace–Beltrami spectrum on $M$ is a **Riemannian invariant**, not a topological invariant — Milnor's celebrated isospectral non-isometric pair (Milnor 1964) shows the converse fails too. However:

- **$\lambda_0 = 0$ kernel (constant function).** Topological invariant: dimension of kernel = number of connected components $= b_0(M)$.
- **Heat-kernel small-time asymptotics.** $\sum_k e^{-\lambda_k t} \sim t^{-d/2} \cdot (\mathrm{vol}(M) + O(t))$ — encodes Riemannian invariants (volume, curvature), not topological invariants.
- **Persistent homology of sublevel sets.** Topologically invariant. The $H_0$-PH of $\{x : u^*(x) \geq \tau\}$ matches across diffeomorphic $M$, and (with care) across continuum-homotopy-equivalent $M$.

### §6.3 σ-tuple decomposition into topological + geometric parts

Tentative decomposition of σ-tuple under continuum limit:

| σ-tuple component | Topological invariant? | Continuum analog |
|---|---|---|
| $\mathcal{F}(u^*)$ (local-maxima count) | Topological in $C^0$-Morse sense | Critical-point count of $u^*: M \to \mathbb{R}$ |
| $(n_k)_k$ irrep multiplicities | Symmetry-group invariant | $\dim$ of $\mathrm{Sym}(M)$-isotypic spaces of $-\Delta_M$ eigenspaces |
| $[\rho_k]$ irrep labels | Symmetry-group invariant (up to canonical translation $\widehat{G_u} \to \widehat{\mathrm{Sym}(M)_u}$) | Same |
| $\lambda_k$ eigenvalues | NOT topological — Riemannian / spectral | Eigenvalues of $-\Delta_M$ |

**Conjecture 6.3 (NQ-190b).** Under continuum limit $G_h \to M$, the σ-tuple components $(\mathcal{F}, n_k, [\rho_k])$ stabilize and are continuum-homotopy / symmetry-respecting-diffeomorphism invariants of $u^* \in H^1(M)$. The eigenvalue tuple $\{\lambda_k\}$ is *not* invariant — only the relative gap structure $\lambda_k / \lambda_2$ has hope of partial scaling-invariance (and even then, only up to Weyl-law leading order).

**Status.** **Cat C target, ~4–6 weeks effort** (requires Burago–Ivanov–Kurylev spectral-convergence machinery + Riemann-vs-topology dichotomy). Defer to W7+.

---

## §7. Cat targets + verification path

| Sub-question | Cat target | Effort | Path |
|---|---|---|---|
| Q1: Graph isomorphism | **Cat A** trivial | 1 week | Corollary to T-σ-Lemma-1 (canonical §13). |
| Q2a: Subdivision (eigenvalue) | **Cat C** generic non-invariance | 1 week | Counterexample 4.2 ($P_3$ vs $P_4$). |
| Q2b: Subdivision (irrep labels) | **Cat C** partial-invariance conjecture (NQ-190a) | 4–6 weeks | Symmetry-respecting refinement + Schur-Maschke transfer. |
| Q2c: Quasi-isometry | **Cat C** non-invariance | already done (counterexample $C_n$ vs $C_{n+1}$) | §5. |
| Q3: Continuum limit topological subset | **Cat C** conjecture (NQ-190b) | 4–6 weeks | Burago–Ivanov–Kurylev + spectral / Morse decomposition. |

**Promotion priority.** Q1 first (Cat A, definitional), then Q2a counterexample as Cat C remark in canonical §13, then Q2b/Q3 conjectures registered as open problems (W7+ candidates).

---

## §8. Persistent-homology connection (Tool A3)

`mathematical_scaffolding_4tools.md` Tool A3 introduces persistent homology (PH) of sublevel sets $\{u^* \leq \tau\}$ as a candidate framework for cross-graph aggregate observables. Key facts:

1. **$H_0$-persistence is graph-isomorphism invariant** (trivially; it depends only on connectivity and $u^*$ values).
2. **$H_0$-persistence is NOT subdivision-invariant** (subdivision adds a new vertex with $u^*(z)$ chosen by interpolation; the persistence diagram shifts by the interpolated value's birth/death points). However, in the *continuum limit* $h \to 0$, the discrete $H_0$-PH converges to the continuum sublevel-set $H_0$-PH, which is a homeomorphism invariant of $M$.
3. **σ-tuple's $\mathcal{F}$ component is the leading-order $H_0$-PH count** (persistent-loops at large persistence; cf. Edelsbrunner–Harer 2010).

**Bridge claim 8.1 (σ-PH partial overlap).** The $\mathcal{F}(u^*)$ entry of σ-tuple matches the $H_0$-PH bar count above persistence threshold $\tau_*$ in the limit $\tau_* \to 0$ (no thresholding). Hence the σ-tuple's *first component* is morally a topological invariant in the PH sense; the Hessian-spectrum component is geometric and not PH-derivable.

This justifies the §6.3 decomposition: **σ-tuple = (PH-derivable topological skeleton: $\mathcal{F}$ + irrep labels) ⊕ (geometric Riemannian skeleton: eigenvalues).**

Cross-link to OAT-2 BC-1 (`F_Kstep_K_triple.md` §3.6): BC-1 fails generically in R23 (overlapping regime), but its *well-separated* version succeeds. Analogously, σ-tuple's PH-skeleton invariance under refinement may hold only in a "well-separated peaks" regime where peak-merging under refinement is bounded.

---

## §9. OP-0009-Emp connection — R23 fullscale and cross-graph generalization

R23 fullscale (NQ-141, 32×32 $D_4$ grid, 90 runs) provides empirical σ-tuple data *exclusively on one graph class*. If σ-tuple has **no** topological invariance beyond graph isomorphism (the conservative reading of §3–§5), then R23 results are graph-class-specific and require independent replication on:

- $L \times L$ torus (translation-invariant; T-V5b-T territory).
- Hexagonal lattice (different $\mathrm{Aut}(G)$, $D_6$).
- Random regular graph (trivial $\mathrm{Aut}(G)$).
- Erdős–Rényi (trivial $\mathrm{Aut}(G)$, fluctuating spectrum).

If §6.3's Conjecture 6.3 holds (continuum-limit topological invariance of $\mathcal{F}, n_k, [\rho_k]$), then R23's *qualitative* σ-tuple structure (e.g., $\mathcal{F} = 9$ with specific irrep pattern) can be promoted to a graph-class-independent claim *in the continuum limit*. Quantitative eigenvalue ratios remain graph-class-specific.

**OP-0009-Emp implication.** R23 σ-tuple data should be reported as

$$\sigma_{R23}(u^*) = \big(\text{PH-skeleton: } \mathcal{F}, n_k, [\rho_k]\ \text{— conjecturally graph-class universal};\ \text{geometric skeleton: } \lambda_k\ \text{— grid-32 specific}\big).$$

This separation is the cross-graph generalization path opened by the present analysis.

---

## §10. External references

- Diestel (2017) *Graph Theory* (5th ed.) — graph isomorphism (§1.1), subdivision and contraction (§1.10), topological minors (§1.10).
- Chung (1997) *Spectral Graph Theory* — Laplacian eigenvalue stability under subdivision (§1.3); Cheeger inequality (§2.2).
- von Luxburg (2007) "A Tutorial on Spectral Clustering" *Stat. Comput.* 17:395–416 — Fiedler-eigenvalue stability, Cheeger constant (§8).
- Hatcher (2002) *Algebraic Topology* Ch. 0 — CW homotopy equivalence; finite graph $\simeq \bigvee^r S^1$ via cycle rank.
- Bridson–Haefliger (1999) *Metric Spaces of Non-Positive Curvature* — quasi-isometry (Part III §I.8).
- Burago–Ivanov–Kurylev (2011) "A graph discretization of the Laplace–Beltrami operator" — discrete-to-continuum spectral convergence.
- Milnor (1964) "Eigenvalues of the Laplace operator on certain manifolds" — isospectral non-isometric counterexample.
- Edelsbrunner–Harer (2010) *Computational Topology: An Introduction* — persistent homology.
- Davies–Gladwell–Leydold–Stadler (2001) "Discrete nodal domain theorems" — already cited in T-σ-Lemma-2.
- Goresky–MacPherson (1988) *Stratified Morse Theory* — already cited in `symmetry_moduli.md`.
- Serre (1977) *Linear Representations of Finite Groups* Ch. 2 — already cited in T-σ-Lemma-1; *finite-group hypothesis*.

---

## §11. W7+ priority + Cat target summary

| Item | Cat target | Priority | Effort |
|---|---|---|---|
| §3 σ-tuple is a graph-isomorphism invariant | **Cat A** | High (canonical §13 corollary) | 1 week |
| §4.2 Subdivision counterexample $(P_3, P_4)$ | **Cat C** remark | High (canonical §13 caveat) | 1 week |
| §4.4 Symmetry-respecting refinement irrep stability (NQ-190a) | **Cat C** conjecture | Medium (W7+) | 4–6 weeks |
| §5 Quasi-isometry non-invariance | **Cat C** remark | Low (already empirically clear) | 0.5 week |
| §6 Continuum-limit topological invariance (Conjecture 6.3, NQ-190b) | **Cat C** conjecture | Medium (W7+) | 4–6 weeks |
| §8 σ-PH skeleton bridge | **Cat C** structural claim | Medium (W7+) | 2–3 weeks |
| §9 R23 reframe (PH-skeleton vs geometric skeleton) | **Cat A** reporting convention | High (immediate, OP-0009-Emp) | 1 week |

**Working-file total estimated 8–12 weeks for full canonical promotion of all §11 items.**

---

## §12. Hard-constraint compliance check

- **Canonical direct edits = 0.** All proposed canonical changes are §13 corollaries / remarks via the standard promotion pipeline through W5+ daily logs.
- **CN10 contrastive (algebraic topology contrastive, not reductive).** §6 + §8 carefully distinguish: σ-tuple has *both* a topological skeleton (PH-derivable) *and* a geometric skeleton (eigenvalue-derivable). Algebraic topology (PH, homotopy) is invoked to *contrast* with the geometric component, not to replace it. The σ-framework is not reduced to PH; PH is a *partial* invariant of σ.
- **Silent open-problem resolution = 0.** F-1, M-1, MO-1 untouched. NQ-190a, NQ-190b, NQ-217 explicitly remain open and registered as W7+ targets.
- **Finite-graph hypothesis.** All §3–§5 claims respect T-σ-Lemma-1's finite-graph requirement; §6 continuum limit treated separately as a distinct (manifold) regime, not as an "extension" of finite-graph theorems.

---

## §13. Cross-references

- **Canonical §13 T-σ-Lemma-1** (finite-graph Maschke hypothesis): the *finite-graph* hypothesis is what blocks naive extension to infinite or continuum settings. §3 is essentially a corollary; §6 requires a separate continuum-graph apparatus.
- **Canonical §13 T-PreObj-1G** (graph-class independent qualitative result): this is the model for §6's σ-PH-skeleton invariance — qualitative graph-class independence already proved for pre-objective mechanism, but only at the level of "$\mathcal{F} \geq 2$", not full σ-tuple.
- **OAT-supplementary `mathematical_scaffolding_4tools.md` §2 Tool A1 (stratified space)**: provides the natural ambient framework for graph-class generalization — strata = $\mathrm{Aut}(G)$-orbit types; transitions across strata are graph-refinement / symmetry-breaking events.
- **OAT-2 `F_Kstep_K_triple.md` BC-1 (per-formation/aggregate bridge)**: BC-1 fails generic in overlapping regime, succeeds in well-separated regime. Direct analog: §6.3's σ-PH-skeleton invariance likely fails in the "peak-merging under refinement" regime, succeeds in the "well-separated peaks" regime.
- **`working/SF/symmetry_moduli.md` §1.1–§1.2**: $\mathrm{Aut}(G)$ action on $\Sigma_m$, invariant/equivariant structure — direct foundation for §3's stabilizer-transport argument.
- **NQ-217 (continuum limit, currently open)**: §6 is the σ-tuple-specific instance of NQ-217. Resolution of NQ-217 (continuum SCC well-posedness) is a prerequisite for §6's Conjecture 6.3.
- **`working/MF/formation_birth_string_breaking.md` §3, §6 (NQ-253; W5 Day 4 PM Wave 3 cross-link, carry-forward #10)**: $L_{\mathrm{crit}}$ (string-breaking critical length) is a graph-class-specific quantity. The §4.2 subdivision counterexample $(P_3, P_4)$ predicts that $L_{\mathrm{crit}}$ is *not* invariant under edge subdivision (boundary-count rescales linearly with subdivision); §6.3 continuum-limit conjecture provides the topological-invariance test for $L_{\mathrm{crit}}/n$ universality. Bilateral with NQ-253 §11.
- **`working/SF/sigma_lie_algebra_structure.md` §3.1 (NQ-258; W5 Day 4 PM Wave 3 cross-link)**: $\mathrm{Aut}(G)$ finiteness + isomorphism invariance — direct foundation for §3 graph-isomorphism σ-invariance. The §4 irrep decomposition restated under graph isomorphism via Claim 3.1' clauses (a)–(d).

---

## §14. Next-action checklist

- [ ] **(Q1, 1 week)** Draft canonical §13 corollary "σ-tuple is a graph-isomorphism invariant" via promotion pipeline through W5 Day 5+ daily log.
- [ ] **(Q2a, 1 week)** Draft canonical §13 remark + counterexample $(P_3, P_4)$ "σ-tuple is NOT subdivision-invariant"; cross-link as caveat to T-σ-Lemma-1.
- [ ] **(NQ-190a, NQ-190b registration)** Register §4.4 + §6.3 conjectures in canonical Open-Problems index as NQ-190a (irrep-stability under symmetry-respecting refinement) and NQ-190b (continuum-limit topological invariance subset).
- [ ] **(R23 reframe, 1 week)** Update OP-0009-Emp documentation with §9's PH-skeleton / geometric-skeleton report split.
- [ ] **(W7+ deferral)** §6 + §8 deferred to W7+; require resolution of NQ-217 (continuum well-posedness) and PH-pipeline build-out (`F_Kstep_K_triple.md` §8).

---

## §15. Cat A (conditional under canonical conjugation rule) vs Cat A (unconditional)

**Conditionality statement (Critic carry-forward #2, W5 Day 4 PM).** All Cat A claims in this file are *conditional* on Claim 3.1' (the canonical conjugation-translation rule, §3 above) — equivalently, on NQ-188 §2 Definition 2.1' — being adopted as a canonical convention.

Specifically:

- **Cat A (conditional)** — Claim 3.1 (σ-tuple is a graph-isomorphism invariant, §3): The proof sketch's step 3 ("irrep labels correspond canonically") is complete *given* that "canonical translation" means clauses (a)–(d) of Claim 3.1'. Without a canonical conjugation rule, the "modulo canonical translation" phrase in Claim 3.1 is informal and does not pin down a unique σ-tuple value for $\sigma(u'^*)$ when $G'_{u'^*}$ has multi-dim irreps. Claim 3.1' closes this gap.

- **Cat A (conditional)** — §11 table row "§3 σ-tuple is a graph-isomorphism invariant": carries "(conditional)" qualifier until CV-1.6 is adopted.

- **Cat A (unconditional)** — §4.2 counterexample (non-invariance under subdivision), §5 counterexample (non-invariance under quasi-isometry): both are negative results that do not depend on the conjugation rule — the spectra differ regardless of how irrep labels are translated.

- **Cat C (unconditional)** — §4.4 irrep-label stability under symmetry-respecting refinement (NQ-190a), §6.3 continuum-limit conjecture (NQ-190b): these remain Cat C conjectures regardless of CV-1.6 adoption.

**CV-1.6 candidate.** Claim 3.1' provides the inter-graph instance of the canonical conjugation-translation rule. It is a sibling to NQ-188 §2 Definition 2.1' (the intra-graph instance). Together they constitute a single CV-1.6 candidate for canonical §11.1 Commitment 14. Adoption path: (1) NQ-188 §2 and NQ-190 §3 both carry the rule; (2) daily-log promotion through W5 Day 5+; (3) canonical §11.1 edit adding clauses (a)–(d) under Commitment 14; (4) theorem-status.md update. Until then, all Cat A claims above carry "(conditional)".

**Cross-reference.** NQ-188 §13 carries the symmetric conditionality statement for the intra-graph σ-uniqueness claims.

---

## §16. Wave 3 Revision Log (W5 Day 4 PM)

**Timestamp:** 2026-04-30, Wave 3 W5 Day 4 PM revision.

**Critic finding addressed:** Critic re-review `logs/daily/2026-04-30/09_critic_re_review_5files.md` §3.4 and §4.3 — joint issue NQ-188/NQ-190: "modulo conjugation" / "modulo canonical translation" under-specified on Schur-degenerate multi-dim irreps (e.g., $D_4$ E-irrep); carry-forward item #1.

**Changes made:**

1. **§3 Claim 3.1'** (new, inserted after Claim 3.1 proof sketch) — added the four-clause canonical conjugation-translation rule (a)–(d) for the inter-graph ($\phi$-transport) setting, verbatim with NQ-188 §2 Definition 2.1' adapted to the graph-isomorphism context. Includes CN10 contrastive remark distinguishing SCC-internal precision requirement from McKay canonical labeling / Schur orthogonality literature references. Added cross-reference "(see NQ-188 §2 Definition 2.1'; this file uses the same rule)".

2. **§3 Cat target sentence** — updated to state "Cat A (conditional on CV-1.6 adoption)" and reference §15.

3. **§15 (new)** — added "Cat A (conditional) vs Cat A (unconditional)" section clarifying that Claim 3.1 invariance proof is conditional on Claim 3.1' adoption; negative results (§4.2, §5) and Cat C conjectures (NQ-190a, NQ-190b) are unconditional.

4. **Cross-link installed** — §3 Claim 3.1' now cites NQ-188 §2 Definition 2.1' (carry-forward #10, missing pair NQ-188 ↔ NQ-190); §15 cites NQ-188 §13 symmetrically.

5. **No canonical/ edits** — working-only per promotion pipeline policy.

6. **CN10, CN5, u_t primitive** — unchanged; no new theorems introduced; change is a canonical-translation-rule cleanup.

---

**End of working file.**
**Lines:** ~350 (target 250–350; extended by W3 revision). **Author:** Architect (NQ-190 spawn, W5 Day 4+); W3 revision by Executor (W5 Day 4 PM).
**Promotion target:** §3 → Cat A canonical §13 (T-σ-Lemma-1 corollary, conditional on CV-1.6); §4.2 → Cat C remark; §4.4 + §6 → NQ-190a/b open-problem registry.
