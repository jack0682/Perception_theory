# 02a_unordered_configuration_formalism.md — Unordered K-Field Configuration Formalism

**Session:** 2026-05-06 (W6 Day 3 G3.2, sub-file of `02_op_0009_pre_substantive_start.md`).
**Goal:** §1 of OP-0009-Pre substantive work — symmetric group action on $\Sigma^K_M$, quotient $\widetilde{\widetilde\Sigma}^K_M$, stratification, dimension count, worked example.
**Status (Bronze required):** Substantive. All claims in this file are Cat C (sketch) unless marked Cat B.

---

## §1.1 Setup: K-Field Configuration Space

Let $G = (V, E)$ be a finite graph, $n = |V|$, and fix total cohesion mass $M > 0$. Set per-slot mass $m = M / K_{\mathrm{field}}$ (equal distribution; the equal-mass case is canonical in I9).

**Single-slot configuration space:**
$$\Sigma_m = \left\{ u \in [0,1]^n : \sum_{i=1}^n u_i = m \right\}$$
a convex polytope, topologically a simplex face, dimension $n-1$ (one linear constraint on $n$ variables in a box).

**K-field ordered configuration space:**
$$\Sigma^K_M := \underbrace{\Sigma_m \times \Sigma_m \times \cdots \times \Sigma_m}_{K \text{ copies}}$$
a product polytope, dimension $K(n-1)$.

**Ordered K-field configuration:** $\mathbf{u} = (u^{(1)}, u^{(2)}, \ldots, u^{(K)}) \in \Sigma^K_M$, each $u^{(j)} \in \Sigma_m$.

*Remark.* The index $j \in \{1, \ldots, K\}$ is what creates the *prima facie* conflict with Commitment 1: $j$ plays the role of a class label or instance ID.

---

## §1.2 Symmetric Group Action

**Definition (Symmetric group action on $\Sigma^K_M$).** The symmetric group $S_K$ acts on $\Sigma^K_M$ by permuting slot indices:
$$\sigma \cdot \mathbf{u} := \left( u^{(\sigma^{-1}(1))}, u^{(\sigma^{-1}(2))}, \ldots, u^{(\sigma^{-1}(K))} \right), \quad \sigma \in S_K, \quad \mathbf{u} \in \Sigma^K_M.$$

*Verification (group action):*
- Identity: $\mathrm{id} \cdot \mathbf{u} = \mathbf{u}$. ✓ (trivial)
- Composition: $(\sigma \tau) \cdot \mathbf{u} = \sigma \cdot (\tau \cdot \mathbf{u})$. Check: $[(\sigma \tau) \cdot \mathbf{u}]_j = u^{((\sigma\tau)^{-1}(j))} = u^{(\tau^{-1}(\sigma^{-1}(j)))} = [\tau \cdot \mathbf{u}]_{\sigma^{-1}(j)} = [\sigma \cdot (\tau \cdot \mathbf{u})]_j$. ✓

**Orbit of $\mathbf{u}$:** $S_K \cdot \mathbf{u} = \{ \sigma \cdot \mathbf{u} : \sigma \in S_K \}$ — the set of all permutations of the slot tuple.

**Stabilizer of $\mathbf{u}$:** $\mathrm{Stab}(\mathbf{u}) = \{ \sigma \in S_K : \sigma \cdot \mathbf{u} = \mathbf{u} \}$ — permutations that leave $\mathbf{u}$ fixed. By the orbit-stabilizer theorem: $|S_K \cdot \mathbf{u}| = K! / |\mathrm{Stab}(\mathbf{u})|$.

*Example:* If all slots are distinct ($u^{(j)} \neq u^{(k)}$ for $j \neq k$), then $\mathrm{Stab}(\mathbf{u}) = \{e\}$ (only identity fixes $\mathbf{u}$), orbit size $= K!$. If $u^{(1)} = u^{(2)} \neq u^{(3)}, \ldots$, then the transposition $(12) \in \mathrm{Stab}(\mathbf{u})$, orbit size $= K!/2$.

---

## §1.3 Quotient Construction: Unordered Configuration Space

**Definition.** The *unordered K-field configuration space* is:
$$\widetilde{\widetilde\Sigma}^K_M := \Sigma^K_M / S_K$$
with the quotient topology (finest topology making the projection $\pi : \Sigma^K_M \to \widetilde{\widetilde\Sigma}^K_M$, $\pi(\mathbf{u}) = [\mathbf{u}]$, continuous).

**Unordered configuration class:** $[\mathbf{u}] = S_K \cdot \mathbf{u}$ — the orbit of $\mathbf{u}$ under $S_K$.

Concretely, $[\mathbf{u}]$ is an *unordered multiset* $\{u^{(1)}, u^{(2)}, \ldots, u^{(K)}\}$ (where repetitions are possible if $u^{(j)} = u^{(k)}$, i.e., at symmetric strata).

**Ontological significance:** $[\mathbf{u}]$ contains no labeling information. It is a collection of $K$ cohesion fields (with multiplicity), but no field is designated field 1 vs field 2 vs ... vs field K. The label is gone at the class level.

---

## §1.4 Stratification Analysis

The quotient space $\widetilde{\widetilde\Sigma}^K_M$ inherits a *stratification* from the orbit structure of $S_K$.

### Open stratum (generic configurations)

$$\Sigma^K_{M, \mathrm{free}} := \{ \mathbf{u} \in \Sigma^K_M : u^{(j)} \neq u^{(k)} \text{ for all } j \neq k \}$$

On $\Sigma^K_{M, \mathrm{free}}$:
- Stabilizer = $\{e\}$ (trivial) for each $\mathbf{u}$.
- Orbit size = $K!$.
- Quotient $\pi(\Sigma^K_{M, \mathrm{free}})$ is an open subset of $\widetilde{\widetilde\Sigma}^K_M$, topologically a smooth orbifold-manifold (locally homeomorphic to $\mathbb{R}^{K(n-1)}/\{e\} = \mathbb{R}^{K(n-1)}$).
- **Dimension of open stratum quotient = $K(n-1)$** (same as $\Sigma^K_M$; the discrete quotient doesn't reduce dim).

### Symmetric strata

For each subset $P \subseteq \{1, \ldots, K\}$ with $|P| \geq 2$, define the *P-diagonal stratum*:
$$D_P := \{ \mathbf{u} \in \Sigma^K_M : u^{(j)} = u^{(k)} \text{ for all } j, k \in P \}$$

Properties:
- $D_P$ requires $u^{(j)} = u^{(k)}$ for all pairs in $P$: this is $|P| - 1$ independent equality constraints, each of codimension $n-1$ (since $u^{(j)} = u^{(k)} \in \Sigma_m$ is an $(n-1)$-dimensional set).
- Actually, the constraint $u^{(j)} = u^{(k)}$ forces the pair $(u^{(j)}, u^{(k)}) \in \Sigma_m \times \Sigma_m$ to lie on the diagonal $\Delta_m := \{(u, u) : u \in \Sigma_m\}$, which has dim $n-1$ inside the $(2(n-1))$-dimensional $\Sigma_m \times \Sigma_m$ — so codim $= n-1$ per equality constraint.
- **Dimension of $D_P$:** $K(n-1) - (|P|-1)(n-1) = (K - |P| + 1)(n-1)$.
- Stabilizer of $\mathbf{u} \in D_P$ (with all other slots distinct): contains $S_P$ (all permutations within $P$), so $|\mathrm{Stab}(\mathbf{u})| \geq |P|!$.
- Codimension of $D_P$ in $\Sigma^K_M$: $(|P|-1)(n-1)$.

**Important special case $P = \{j, k\}$ (pair equality):** codim $= n-1$, dim $= (K-1)(n-1)$. These are the "walls" of the open stratum.

**Boundary/corner strata:** For $|P| = K$ (all slots equal), dim $= n-1$, codim $= (K-1)(n-1)$.

**Stratification of $\widetilde{\widetilde\Sigma}^K_M$:**
$$\widetilde{\widetilde\Sigma}^K_M = \pi(\Sigma^K_{M,\mathrm{free}}) \sqcup \bigsqcup_{P \subseteq \{1,\ldots,K\},\, |P| \geq 2} \pi(D_P^\circ)$$
where $D_P^\circ = D_P \setminus \bigcup_{P' \supsetneq P} D_{P'}$ is the locally-closed stratum with exactly the stabilizer group generated by $S_P$.

---

## §1.5 Worked Example: $T^2_4$ Graph, $K = 2$

**Setup:**
- $T^2_4$ = 2D torus $4 \times 4$ = 16-node graph ($n = 16$).
- $K = 2$, $M = 2m$ (total mass split equally).
- $\Sigma_m$: $(n-1) = 15$-dimensional simplex face.
- $\Sigma^2_M = \Sigma_m \times \Sigma_m$: $(2 \times 15) = 30$-dimensional.
- $S_2 = \{\mathrm{id}, \tau_{12}\}$ where $\tau_{12}$ is the transposition of slots 1 and 2.

**Quotient $\widetilde{\widetilde\Sigma}^2_M = \Sigma^2_M / S_2$:**

Action of $\tau_{12}$: $(u^{(1)}, u^{(2)}) \mapsto (u^{(2)}, u^{(1)})$. This is a $\mathbb{Z}_2$ reflection.

**Open stratum:** $\{(u^{(1)}, u^{(2)}) : u^{(1)} \neq u^{(2)}\}$, dim 30, orbit size 2. The quotient is homeomorphic to $(\Sigma_m \times \Sigma_m \setminus \Delta_m) / \mathbb{Z}_2$ (unordered pairs of distinct elements of $\Sigma_m$).

**Symmetric stratum (diagonal):** $\Delta_m = \{(u, u) : u \in \Sigma_m\}$. Fixed by $\tau_{12}$ (since $(u,u) \mapsto (u,u)$). Dimension = 15, codim = 15. Under quotient: $\pi(\Delta_m) = \Delta_m$ (the symmetric stratum maps to itself; it is the "boundary" of $\widetilde{\widetilde\Sigma}^2_M$).

**Concrete configuration sample:**

Take $G = T^2_4$ (16 nodes, 2D torus adjacency). Fix $m = 8$ (half the nodes active on average).

- **Ordered representative** $\mathbf{u} = (u_A, u_B)$ where $u_A, u_B \in \Sigma_8$ are two distinct soft cohesion fields.
  - $u_A$ = "left half" field: $u_A(i) = 1$ for $i \in L$ (8 left nodes), $u_A(i) = 0$ otherwise (a sharp formation, for illustration).
  - $u_B$ = "right half" field: $u_B(i) = 1$ for $i \in R$ (8 right nodes), $u_B(i) = 0$ otherwise.
  - Clearly $u_A \neq u_B$ (disjoint support), so $\mathbf{u} \in \Sigma^2_{M,\mathrm{free}}$.

- **The unordered class** $[(u_A, u_B)] = \{u_A, u_B\}$ (as a multiset with $u_A \neq u_B$).
  - $[(u_A, u_B)] = [(u_B, u_A)]$: the ordering is gone.
  - This is the point in $\widetilde{\widetilde\Sigma}^2_M$ corresponding to the *two-formation configuration* with left and right formations — no labeling of which is "formation 1" vs "formation 2".

- **Representative selection rule** (canonical choice for computation): Given $[\mathbf{u}] = \{u^{(1)}, u^{(2)}\}$ with $u^{(1)} \neq u^{(2)}$, choose the representative with $\sum_i (u^{(1)}_i \cdot i) \leq \sum_i (u^{(2)}_i \cdot i)$ (lexicographic centroid ordering). This gives a canonical section $s: \pi(\Sigma^2_{M,\mathrm{free}}) \to \Sigma^2_{M,\mathrm{free}}$ that is continuous away from $\Delta_m$.

- **Symmetric stratum example**: $u_C = (1/2) \cdot \mathbf{1}_n$ (uniform field, mass $m = n/2 = 8$). Then $(u_C, u_C) \in \Delta_m$. The class $[(u_C, u_C)] = \{u_C, u_C\}$ (a multiset with one repeated element) is in the symmetric stratum of $\widetilde{\widetilde\Sigma}^2_M$.

**Dimension count summary for $T^2_4$, $K=2$:**

| Stratum | Dim | Codim | Description |
|---|---|---|---|
| Open stratum $\pi(\Sigma^2_{M,\mathrm{free}})$ | 30 | 0 | Generic unordered pairs $(u^{(1)}, u^{(2)})$ with $u^{(1)} \neq u^{(2)}$ |
| Symmetric stratum $\pi(\Delta_m)$ | 15 | 15 | "Two equal formations" (degenerate, repeated multiset element) |

**Summary:** $\widetilde{\widetilde\Sigma}^2_M$ is a 30-dimensional space with a 15-dimensional boundary stratum. The open part (dim 30) corresponds to genuine two-formation states; the boundary (dim 15) to degenerate "single-type repeated" states.

---

## §1.6 General Dimension Count (K arbitrary)

For $K$ slots on an $n$-node graph with equal-mass $m = M/K$:

| Stratum | Dimension |
|---|---|
| Full space $\Sigma^K_M$ | $K(n-1)$ |
| Open stratum quotient $\widetilde{\widetilde\Sigma}^K_{M,\mathrm{free}}$ | $K(n-1)$ (same dim; quotient is by discrete group) |
| Symmetric stratum $D_P$ (equal slots in $P$, $|P| \geq 2$) | $(K - |P| + 1)(n-1)$ |
| All-equal stratum ($P = \{1,\ldots,K\}$) | $n-1$ |

The quotient $\widetilde{\widetilde\Sigma}^K_M$ is topologically an orbifold: smooth away from symmetric strata; each symmetric stratum is a lower-dimensional orbifold in its own right.

---

**End of `02a_unordered_configuration_formalism.md`. §1 (formalism) complete: $S_K$ action defined, quotient $\widetilde{\widetilde\Sigma}^K_M$ constructed, stratification analyzed, dimension count given, worked example $T^2_4 \times K=2$ with concrete configurations. Continues to `02b_reduction_map_pi.md`.**

**Day 3 Bronze criterion §1 (formalism): MET.**
