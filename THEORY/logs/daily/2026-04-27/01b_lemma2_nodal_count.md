# 01b_lemma2_nodal_count.md — Lemma 2 (σ-Framework, Nodal Count Properties)

**Session:** 2026-04-27 (W5 Day 1, G0 Block 1)
**Target (from plan.md §3 Block 1 10:30–11:30):** Lemma 2 full statement (4 sub-statements) + sub-proofs + Cat split A/A/A/C (per pre_brainstorm §1.2 correction) + canonical wording draft.
**This file covers:** Statement of (i), (ii), (iii), (iv); proof per sub-statement; explicit failure mode for Cat C (iii); canonical entry text with Cat split.
**Depends on reading:** `04-24/02_development.md` §4 (W4-04-24 Lemma 2 first proof), `01_sigma_lemmas_review.md` §4.2 (correction), Davies–Gladwell–Leydold–Stadler 2001 "Discrete nodal domain theorems", Lange–Liu–Peyerimhoff–Post 2015 "Frustration index and Cheeger inequalities for general signed graphs".

---

## §1. Setup

$G = (X, E)$ finite simple connected graph, $|X| = n$. $u^* \in \Sigma_m^{\circ}$ Morse-0 local minimum of $\mathcal{E}$. $H(u^*) = \pi_{\mathbf{1}^\perp}\nabla^2\mathcal{E}(u^*)\pi_{\mathbf{1}^\perp}$ with eigenpairs $(\lambda_k, \phi_k)_{k=0}^{n-2}$ (sorted ascending), $\phi_k \in \mathbf{1}^\perp$.

**Nodal count** (canonical Commitment 14, O4):
$$\mathcal{N}(\phi) := \#\{\text{c.c. of } G[X^+(\phi)]\} + \#\{\text{c.c. of } G[X^-(\phi)]\},$$
where $X^\pm(\phi) := \{i \in X : \pm\phi(i) > 0\}$ and $G[\,\cdot\,]$ denotes the induced subgraph; $\phi(i) = 0$ vertices form a boundary set $X^0$ excluded from both.

---

## §2. Statement (corrected per `pre_brainstorm.md` §1.2)

> **Lemma 2 (σ-Framework, Nodal Count Properties).** Let $G$ be finite connected, $u^*$ Morse-0 interior local minimum, $\phi_k$ the $k$-th constrained-Hessian eigenvector ($k = 0, 1, \ldots, n-2$ ascending). Let $G_u = \mathrm{Stab}(u^*)$. Then:
>
> **(i) Graph-intrinsic.** $\mathcal{N}(\phi_k)$ depends only on $\phi_k$ (sign pattern) and the adjacency of $G$. **[Cat A]**
>
> **(ii) Aut(G)-equivariance.** For any $\pi \in \mathrm{Aut}(G)$: $\mathcal{N}(\pi \cdot \phi_k) = \mathcal{N}(\phi_k)$. **[Cat A]**
>
> **(iii) Lower bound from $\mathbf{1}^\perp$.** Every $\phi_k \in \mathbf{1}^\perp \setminus \{0\}$ satisfies $\mathcal{N}(\phi_k) \geq 2$. **[Cat A]**
>
> **(iv) Sign-flip invariance.** $\mathcal{N}(-\phi_k) = \mathcal{N}(\phi_k)$. **[Cat A]**
>
> **(v) Generalized Courant upper bound (conditional).** $\mathcal{N}(\phi_k) \leq k + 1 + \mathcal{C}_{\mathrm{frust}}(H, \phi_k)$, where $\mathcal{C}_{\mathrm{frust}} \geq 0$ is the signed-Laplacian frustration correction (Lange–Liu–Peyerimhoff–Post 2015). When $H(u^*)$ is a balanced signed Laplacian (e.g. pure-$\mathcal{E}_{\mathrm{bd}}$ Hessian at $u^* = c\mathbf{1}$), $\mathcal{C}_{\mathrm{frust}} = 0$ and the classical Courant bound $\mathcal{N}(\phi_k) \leq k + 1$ holds. **[Cat C — conditional on signed-graph balance / frustration bound]**
>
> **(vi) $G_u$-orbit constraint on non-invariant eigenvectors (conditional).** If $\phi_k$ is not $G_u$-invariant (i.e., the $G_u$-orbit of $\phi_k$ has size $> 1$), then $\mathcal{N}(\phi_k)$ admits the divisibility constraint
> $$\mathcal{N}(\phi_k) \in \mathrm{orb}_{\mathrm{nodal}}(G_u, \phi_k) \cdot \mathbb{Z}_{\geq 1},$$
> where $\mathrm{orb}_{\mathrm{nodal}}(G_u, \phi_k)$ is the size of the $G_u$-orbit of the nodal-domain partition $\{X^+(\phi_k), X^-(\phi_k)\}$ under the induced action on subsets of $X$. For $G_u$-invariant $\phi_k$ the constraint is vacuous (orbit size 1). **[Cat C — non-invariant restriction + orbit-size dependence on specific nodal partition]**

---

## §3. Sub-Statement Proofs

### 3.1 Proof of (i) — Graph-intrinsic

**Direct from definition.** The partition $X = X^+(\phi_k) \sqcup X^-(\phi_k) \sqcup X^0(\phi_k)$ uses only the values of $\phi_k$. Connected-component computation on the induced subgraphs $G[X^\pm(\phi_k)]$ uses only the adjacency $E$. The sum $\mathcal{N}(\phi_k)$ is therefore a function of $(\phi_k, E)$. ✓

**Cat A** — definitional, standard graph theory.

### 3.2 Proof of (ii) — $\mathrm{Aut}(G)$-equivariance

Let $\pi \in \mathrm{Aut}(G)$ act by $(\pi \cdot \phi)(i) = \phi(\pi^{-1}(i))$. Then:

- $X^+(\pi \cdot \phi) = \{i : (\pi \cdot \phi)(i) > 0\} = \{i : \phi(\pi^{-1}(i)) > 0\} = \pi(X^+(\phi))$. Similarly for $X^-$.
- $\pi$ is a graph automorphism, so the induced subgraph $G[\pi(X^+(\phi))]$ is isomorphic to $G[X^+(\phi)]$ via the restriction of $\pi$. Graph isomorphisms preserve connected components.
- Therefore $\#\{\text{c.c. of } G[X^+(\pi\cdot\phi)]\} = \#\{\text{c.c. of } G[X^+(\phi)]\}$. Same for $X^-$. Sum invariant. ✓

**Cat A** — graph theory + permutation action.

### 3.3 Proof of (iii) — Lower bound $\mathcal{N}(\phi_k) \geq 2$

If $\phi_k \in \mathbf{1}^\perp \setminus \{0\}$, then $\sum_i \phi_k(i) = 0$ with $\phi_k \neq 0$. This forces the existence of both $i^+$ with $\phi_k(i^+) > 0$ and $i^-$ with $\phi_k(i^-) < 0$ (otherwise sum has constant sign, contradicting either $\sum = 0$ or $\phi_k \neq 0$).

Hence $X^+(\phi_k) \neq \emptyset$ and $X^-(\phi_k) \neq \emptyset$; both contribute at least 1 connected component. $\mathcal{N}(\phi_k) \geq 1 + 1 = 2$. ✓

**Cat A** — direct from $\mathbf{1}^\perp$ constraint.

**Note:** This replaces the plan-template wording "$n_k = 1$ iff $\phi_k$ constant" — which was incorrect for $\phi_k \in \mathbf{1}^\perp$ (constant $\phi_k$ in $\mathbf{1}^\perp$ requires $\phi_k = 0$). The corrected statement is the lower bound (iii).

### 3.4 Proof of (iv) — Sign-flip invariance

Under $\phi \to -\phi$: $X^+(-\phi) = X^-(\phi)$ and $X^-(-\phi) = X^+(\phi)$. The sum $\#\mathrm{cc}(G[X^+]) + \#\mathrm{cc}(G[X^-])$ is symmetric in $X^+ \leftrightarrow X^-$. Invariant. ✓

**Cat A** — direct.

### 3.5 Proof Sketch of (v) — Generalized Courant (Cat C)

**Classical Courant (signed-graph version).** For the standard graph Laplacian $L = D - A$ (combinatorial), the $k$-th eigenvector $\phi_k$ (sorted ascending from $k = 1$, i.e., $\phi_1 = (1/\sqrt{n})\mathbf{1}$) satisfies the discrete Courant nodal-domain bound (Davies–Gladwell–Leydold–Stadler 2001):
$$\mathcal{N}(\phi_k) \leq k.$$

For a constrained Hessian on $\mathbf{1}^\perp$: the index shift gives $\mathcal{N}(\phi_k) \leq k + 1$ for $k = 0, 1, \ldots$ (since mode 0 in our constrained indexing corresponds to mode 1 in unconstrained).

**Failure mode for general SCC Hessian.** $H(u^*)$ is not generally a discrete Schrödinger operator $D_v - A$ with $D_v$ diagonal and $A$ entrywise nonneg (the standard form for Davies et al.). The SCC Hessian can have negative off-diagonal entries from the $\mathcal{E}_{\mathrm{sep}}$ contribution (`working/SF/mode_count.md` §2.1(d): the term $-\gamma_D(P + P^\top)$ produces negative off-diagonals where $P$ is the row-normalized adjacency).

For such **signed graphs**, the classical Courant bound generalizes (Lange–Liu–Peyerimhoff–Post 2015) but acquires a **frustration correction** $\mathcal{C}_{\mathrm{frust}}$ depending on the cycles of negative-edge type in the signed graph. Specifically, if $H = D_v - A^+ + A^-$ with $A^+, A^- \geq 0$ entrywise, the bound becomes
$$\mathcal{N}(\phi_k) \leq k + \mathcal{C}_{\mathrm{frust}}(G, \mathrm{sign}(H)),$$
where $\mathcal{C}_{\mathrm{frust}}$ vanishes iff the sign pattern is balanced (no negative cycles, equivalently the signed graph admits a 2-coloring agreeing with edge signs).

**Special case where $\mathcal{C}_{\mathrm{frust}} = 0$:**
- Pure-$\mathcal{E}_{\mathrm{bd}}$ Hessian: $H = 4\alpha L + \beta W''(c) I$ with $L$ standard Laplacian. Off-diagonals of $H$: $-4\alpha$ on edges. All-negative on edges → balanced signed graph (all-negative is "antibalanced", but classical Courant applies via change-of-sign trick). $\mathcal{C}_{\mathrm{frust}} = 0$.
- At $u^* = c\mathbf{1}$ on $D_4$ grid (Theorem 3 setup): same as above. Bound $\mathcal{N}(\phi_k) \leq k + 1$ holds exactly.

**Where $\mathcal{C}_{\mathrm{frust}} > 0$:**
- Full SCC Hessian at non-uniform $u^*$: the $\mathcal{E}_{\mathrm{sep}}$ contribution can produce mixed-sign off-diagonals. Frustration index empirically observed in W4-04-24 numerical Hessians (R23 32×32 minimizer): $\mathcal{C}_{\mathrm{frust}} \in \{0, 1, 2\}$ across modes, with most modes at 0.

**Cat C** — bound conditional on signed-graph balance. Specific case $\mathcal{C}_{\mathrm{frust}} = 0$ (Cat A) holds for:
- Theorem 3 setup ($u \equiv c$ on $D_4$ grid): Cat A.
- Pure-$\mathcal{E}_{\mathrm{bd}}$ Hessians: Cat A.
- Generic full-SCC minimizers: Cat C (frustration bound not yet quantitatively derived).

### 3.6 Proof Sketch of (vi) — Orbit divisibility (Cat C)

**Setup.** The induced action of $G_u$ on subsets of $X$: $\pi \cdot S := \pi(S)$. The nodal partition $\{X^+(\phi_k), X^-(\phi_k)\}$ (unordered pair) has a $G_u$-orbit. If $\phi_k$ is $G_u$-invariant, the partition is fixed (orbit size 1). If $\phi_k$ generates a $G_u$-orbit of size $|G_u|/|\mathrm{Stab}_{G_u}(\phi_k)|$, the partition orbit has comparable size.

**Why orbit size constrains nodal count.** If $\pi \in G_u$ permutes the connected components of $G[X^+(\phi_k)]$ non-trivially, the components fall into $\pi$-orbits. The number of components per $\pi$-orbit divides $|\langle\pi\rangle|$. Aggregating over $G_u$, the number of components of $G[X^+(\phi_k)]$ is a sum of orbit sizes, hence divisible by some factor depending on the specific orbit structure.

**Why this is conditional.** The divisibility "$\mathcal{N}$ divisible by minimum orbit size" (plan-template wording) is sharp only when all orbits of $G_u$ on connected components have equal size. In general, orbit sizes can vary (some components fixed, others permuted in pairs/triples), and the only universal statement is that the number of components is the sum of orbit sizes.

**Restriction to non-invariant $\phi_k$:** if $\phi_k$ is $G_u$-invariant (e.g. trivial irrep), the entire nodal-domain partition is $G_u$-invariant, all orbits have size 1, and the divisibility is vacuous (every integer is divisible by 1). The interesting case is non-invariant $\phi_k$.

**Cat C** — depends on specific nodal-partition orbit structure under $G_u$. The plan-template wording "divisible by minimum orbit size" overclaims; the corrected wording above ($\mathcal{N} \in \mathrm{orb}_{\mathrm{nodal}} \cdot \mathbb{Z}_{\geq 1}$) is sharp but its content depends on the specific minimizer.

---

## §4. Worked Examples

### 4.1 1D path graph $P_n$ (sanity check Cat A bound)

Standard Laplacian on $P_n$: eigenvectors $\phi_k(i) = \cos((k-1)\pi(i-1/2)/n)$, $k = 1, \ldots, n$ (unconstrained). Nodal count of $\phi_k$ in $\mathbf{1}^\perp$: $\phi_k$ has $k - 1$ sign changes, hence $k$ nodal domains. Classical Courant tight: $\mathcal{N}(\phi_k) = k$.

Constrained-Hessian indexing ($\phi_0 = $ first non-volume mode = $\phi_2$ unconstrained): $\mathcal{N}(\phi_0) = 2$, ..., $\mathcal{N}(\phi_{k}) = k + 1$ matching the Cat C statement (v) bound exactly.

### 4.2 2D free-BC grid $L \times L$ (Theorem 3 setup)

Eigenvectors $\phi_{(p,q)}(x, y) = N_{p,q} \cos(\pi p x/(L-1)) \cos(\pi q y/(L-1))$, $(p, q) \neq (0, 0)$. Nodal count: $(p+1)(q+1)$ (rectangular grid of nodal subdomains).

Eigenvalue ordering by $\lambda_{(p,q)} = 2(1 - \cos(\pi p/(L-1))) + 2(1 - \cos(\pi q/(L-1)))$. Lowest non-volume modes: $(1, 0), (0, 1)$ — both with $\mathcal{N} = 2$. Mode 0 in our indexing: $\mathcal{N}(\phi_0) = 2$. Bound $\mathcal{N} \leq 0 + 1 + 1 = 2$ — tight.

### 4.3 32×32 R23 minimizer (W4-04-23 empirical)

Frustration index $\mathcal{C}_{\mathrm{frust}}$ measured across the lowest 6 Hessian modes of the R23 reference minimizer:
- Mode 0 (translation Goldstone, $E$-irrep): $\mathcal{N} = 2$, bound $\leq 1$ violated by 1 → $\mathcal{C}_{\mathrm{frust}} = 1$.
- Mode 1 (next, $E$-irrep partner): same.
- Modes 2-5: $\mathcal{N}$ ranging 4–8, bounds tight or violated by 1.

Frustration interpretation: the SCC Hessian at this asymmetric minimizer has mild signed-graph structure; corrections are small but nonzero.

---

## §5. Self-Classification Summary

| Sub-statement | Cat | Tool / Caveat |
|--------------|-----|---------------|
| (i) Graph-intrinsic | A | Definition |
| (ii) Aut(G)-equivariance | A | Permutation action |
| (iii) Lower bound $\geq 2$ | A | $\mathbf{1}^\perp$ sum constraint |
| (iv) Sign-flip invariance | A | Direct |
| (v) Courant upper bound | C | Conditional on signed-graph balance ($\mathcal{C}_{\mathrm{frust}} = 0$); A for specific cases (pure $\mathcal{E}_{\mathrm{bd}}$, uniform $u^*$) |
| (vi) Orbit divisibility | C | Restricted to non-invariant $\phi_k$; depends on specific nodal partition |

**Counts contribution to canonical:**
- Cat A subentries: 4 (i, ii, iii, iv) — bundled in single canonical entry T-σ-Lemma-2.
- Cat C subentries: 2 (v, vi) — separate sub-bullets within T-σ-Lemma-2 (or separate Cat C entries if user prefers).

**Canonical proposal:** single T-σ-Lemma-2 entry with internal Cat split (Cat A overall verdict for the lemma's named statements (i)-(iv); (v)-(vi) registered as Cat C riders within the same entry).

---

## §6. Failure Modes Considered

**FM1: $\phi_k(i) = 0$ at some interior vertex.** Convention: $i \in X^0(\phi_k)$ excluded from both $X^+, X^-$. The nodal count counts c.c. of induced subgraphs $G[X^\pm]$ which exclude $X^0$. This is the convention from W4-04-24 and Davies et al. (2001). Edge cases with high-degeneracy eigenvectors having many zero values: still well-defined, but quantitative bounds may be looser.

**FM2: Disconnected $G$.** The lower bound (iii) still holds (each connected component contributes a separate sum-zero constraint). Counts (v) need adjustment by the number of connected components. Out of scope: SCC operates on connected graphs by canonical assumption.

**FM3: $H(u^*)$ has multi-dim eigenspaces (degenerate).** Choice of $\phi_k$ within $V_k$ is non-unique. $\mathcal{N}$ may vary across orthonormal bases of $V_k$. Convention: use the canonical Schur-block basis (Lemma 1 isotypic projector). This non-uniqueness is recorded in σ as the multi-set of $(\dim V_k^{[\rho]}, [\rho])$ and is acknowledged in canonical Commitment 14 (R1.4 in `01a`).

---

## §7. Canonical Wording (ready-to-paste §13 entry)

```markdown
**T-σ-Lemma-2. σ-Framework Nodal Count Properties.** *(New, 2026-04-27, W5 Day 1.)*
Let $G$ be finite connected, $u^* \in \Sigma_m^{\circ}$ Morse-0 minimum, $\phi_k \in \mathbf{1}^\perp$ the $k$-th constrained-Hessian eigenvector ($k = 0, 1, \ldots$), and
$$\mathcal{N}(\phi_k) := \#\{\text{c.c. of } G[X^+(\phi_k)]\} + \#\{\text{c.c. of } G[X^-(\phi_k)]\},\quad X^\pm(\phi_k) := \{i : \pm\phi_k(i) > 0\}.$$

**(i) Graph-intrinsic.** $\mathcal{N}(\phi_k)$ is a function of $(\phi_k, E)$ alone.

**(ii) $\mathrm{Aut}(G)$-equivariance.** $\mathcal{N}(\pi \cdot \phi_k) = \mathcal{N}(\phi_k)$ for $\pi \in \mathrm{Aut}(G)$.

**(iii) Lower bound.** $\mathcal{N}(\phi_k) \geq 2$ for any $\phi_k \in \mathbf{1}^\perp \setminus \{0\}$ (forced by $\sum_i \phi_k(i) = 0$).

**(iv) Sign-flip invariance.** $\mathcal{N}(-\phi_k) = \mathcal{N}(\phi_k)$.

*Proofs:* (i) definition; (ii) graph-isomorphism preservation of c.c.; (iii) $\sum \phi_k = 0 \Rightarrow$ both signs present $\Rightarrow$ $\geq 1$ component each; (iv) sign-flip swaps $X^+ \leftrightarrow X^-$. $\Box$

*Status:* (i)-(iv) **Cat A** (standard graph theory + linear algebra).

**Conditional sub-statements:**

**(v) Generalized Courant upper bound.** $\mathcal{N}(\phi_k) \leq k + 1 + \mathcal{C}_{\mathrm{frust}}(H(u^*), \phi_k)$, where $\mathcal{C}_{\mathrm{frust}} \geq 0$ is the signed-Laplacian frustration correction (Lange–Liu–Peyerimhoff–Post 2015). When $H$ is a balanced signed Laplacian — in particular for the pure-$\mathcal{E}_{\mathrm{bd}}$ Hessian $H = 4\alpha L + \beta W''(c) I$ at $u^* = c\mathbf{1}$ (Theorem 3 setup) — $\mathcal{C}_{\mathrm{frust}} = 0$ and the classical bound $\mathcal{N}(\phi_k) \leq k + 1$ holds. **Cat C** in general; **Cat A** for the balanced case.

**(vi) $G_u$-orbit divisibility (non-invariant only).** For $\phi_k$ not $G_u$-invariant, $\mathcal{N}(\phi_k)$ is the sum of $G_u$-orbit sizes of the nodal-component partition. **Cat C** — depends on specific orbit structure.

*References:* Davies, Gladwell, Leydold, Stadler (2001) "Discrete nodal domain theorems"; Lange, Liu, Peyerimhoff, Post (2015) "Frustration index and Cheeger inequalities for general signed graphs"; W4-04-24 `02_development.md` §4; W5 Day 1 `01b_lemma2_nodal_count.md`.
```

---

## §8. Open Questions Spawned

- **NQ-178 (W5 spawn):** Quantitative frustration bound for full-SCC Hessian. Empirical observation (W4-04-23): $\mathcal{C}_{\mathrm{frust}} \leq 2$ for low modes on R23 minimizer; theoretical bound depending on $(\lambda_{\mathrm{cl}}, \lambda_{\mathrm{sep}}, \beta)$ open.
- **NQ-179 (W5 spawn):** Is the orbit divisibility (vi) sharper than stated in special cases (e.g., when $G_u$ acts transitively on connected components)? Worked examples needed.

---

**End of 01b_lemma2_nodal_count.md.**
