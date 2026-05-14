> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]

# 02b_reduction_map_pi.md — Reduction Map π: Σ^K_M → Σ̃̃^K_M

**Session:** 2026-05-06 (W6 Day 3 G3.2, sub-file of `02_op_0009_pre_substantive_start.md`).
**Goal:** §2 of OP-0009-Pre — canonical projection $\pi$, continuity, local sections, fiber structure.
**Status (Bronze required):** Substantive.
**Depends on:** `02a_unordered_configuration_formalism.md` (§1 formalism complete).

---

## §2.1 Explicit Construction of π

**Definition.** The *canonical projection* is the quotient map:
$$\pi : \Sigma^K_M \to \widetilde{\widetilde\Sigma}^K_M, \qquad \pi(\mathbf{u}) = [\mathbf{u}] = S_K \cdot \mathbf{u}$$
sending each ordered K-field configuration $\mathbf{u} = (u^{(1)}, \ldots, u^{(K)})$ to its equivalence class under slot-permutation.

Concretely, $\pi$ identifies $\mathbf{u}$ with all $K!$ permutations of its slots (fewer at symmetric strata per §1.4).

**Key point:** $\pi$ *forgets the labeling*. Two configurations that differ only in how the formations are assigned to slots map to the *same* point in $\widetilde{\widetilde\Sigma}^K_M$.

---

## §2.2 Continuity of π

**Claim.** $\pi : \Sigma^K_M \to \widetilde{\widetilde\Sigma}^K_M$ is continuous.

**Proof (direct, via quotient topology definition).** The quotient topology on $\widetilde{\widetilde\Sigma}^K_M$ is defined as the *finest topology* making $\pi$ continuous. By definition, $U \subseteq \widetilde{\widetilde\Sigma}^K_M$ is open if and only if $\pi^{-1}(U)$ is open in $\Sigma^K_M$. Therefore $\pi$ is continuous by construction. $\square$

**Further regularity:** Since $S_K$ is a finite group acting on the compact polytope $\Sigma^K_M$ by homeomorphisms (each permutation of coordinates is continuous and open on $\Sigma^K_M$), $\pi$ is:
- A *proper map* (preimage of compact = compact, trivially here since $\Sigma^K_M$ is compact).
- An *open map* (a general fact: quotient by compact group action is open on the orbit space).
- $\widetilde{\widetilde\Sigma}^K_M$ is compact (continuous image of compact).
- $\widetilde{\widetilde\Sigma}^K_M$ is Hausdorff at generic points (open stratum is a manifold quotient); symmetric strata are lower-dimensional orbifold boundary components.

---

## §2.3 Local Sections on the Open Stratum

On the symmetric strata, $\pi$ is not injective (multiple ordered configurations map to the same class). On the open stratum, $\pi$ is $K!$-to-1.

**Local section (canonical representative selection rule):** Given a point $[\mathbf{u}] \in \pi(\Sigma^K_{M,\mathrm{free}})$ (open stratum quotient), we need to choose a canonical representative $s([\mathbf{u}]) \in \Sigma^K_{M,\mathrm{free}}$ continuously.

**Construction.** Define the *mass-centroid* of slot $j$ as $c^{(j)} = \sum_{i=1}^n i \cdot u^{(j)}_i / m$ (weighted centroid of node indices, using node ordering of the graph). Given $[\mathbf{u}] = \{u^{(j_1)}, \ldots, u^{(j_K)}\}$ as an unordered multiset, choose the representative with:
$$s([\mathbf{u}]) = \text{the ordered tuple sorted by } c^{(j_1)} \leq c^{(j_2)} \leq \cdots \leq c^{(j_K)}$$
with tie-breaking by lexicographic order on $u^{(j)}$ (compare componentwise).

**Claim (continuity of $s$ on open stratum).** On the open stratum $\pi(\Sigma^K_{M,\mathrm{free}})$, the section $s$ is continuous.

*Proof sketch:* On a small neighborhood $U$ around $[\mathbf{u}] \in \pi(\Sigma^K_{M,\mathrm{free}})$ with all slots distinct and centroids $c^{(1)} < c^{(2)} < \cdots < c^{(K)}$ (strict ordering — valid on open set), the sorted representative is determined by the same permutation $\sigma_0$ throughout $U$. Thus $s|_U = $ the composition of $\pi^{-1}$ (inverse to $\pi|_{\sigma_0 \cdot \text{neighborhood}}$, which is continuous) and the sorting, which is locally constant at $\sigma_0$. Continuity follows. $\square$

**Limitation:** At the symmetric stratum boundary ($u^{(j)} = u^{(k)}$ for some $j, k$), the centroid ordering becomes degenerate (tie between $c^{(j)}$ and $c^{(k)}$) and $s$ is not continuous. The lexicographic tie-break extends continuity to measure-zero edge cases but not to the entire symmetric stratum (where $u^{(j)} = u^{(k)}$ identically). This is expected: local sections of a non-free group action are necessarily discontinuous at fixed-point strata.

---

## §2.4 Fiber Structure

**Definition.** The *fiber* of $\pi$ over $[\mathbf{u}] \in \widetilde{\widetilde\Sigma}^K_M$ is:
$$\pi^{-1}([\mathbf{u}]) = S_K \cdot \mathbf{u} = \{ \sigma \cdot \mathbf{u} : \sigma \in S_K \}$$
the orbit of $\mathbf{u}$ under $S_K$.

**Fiber sizes:**

| Configuration type | $|\mathrm{Stab}(\mathbf{u})|$ | Fiber size $|\pi^{-1}([\mathbf{u}])|$ |
|---|---|---|
| All slots distinct (generic) | 1 | $K!$ |
| Exactly one pair equal $u^{(j)} = u^{(k)}$ | 2 | $K!/2$ |
| Exactly one triple equal $u^{(j)} = u^{(k)} = u^{(l)}$ | 6 | $K!/6$ |
| $r$ groups with $n_1, \ldots, n_r$ equal slots ($\sum n_i = K$) | $\prod_i n_i!$ | $K! / \prod_i n_i!$ (multinomial) |
| All slots equal $u^{(1)} = \cdots = u^{(K)}$ | $K!$ | 1 |

**Fiber dimension:** $\pi^{-1}([\mathbf{u}])$ is a *discrete* set (finite, 0-dimensional). The fiber has no continuous structure — the symmetric group $S_K$ is finite, so orbits are discrete. This is in contrast to Lie group quotients where fibers are higher-dimensional manifolds.

**Implication for gradient flow:** When doing gradient flow on $\Sigma^K_M$ (the optimizer in `scc/optimizer.py`), the flow is blind to slot permutations — it will converge to some ordered representative of $[\hat{\mathbf{u}}]$. The descent path is slot-label-dependent. The *final configuration class* $[\hat{\mathbf{u}}]$ is the natural invariant quantity. This is precisely the modeling-layer structure: the optimizer works in ordered coordinates (computational efficiency), but the result is interpreted as a class.

---

## §2.5 Functoriality (brief)

**Claim.** Any $S_K$-equivariant map $f : \Sigma^K_M \to Y$ (meaning $f(\sigma \cdot \mathbf{u}) = f(\mathbf{u})$ for all $\sigma \in S_K$) factors uniquely through $\pi$: there exists a unique $\widetilde{f} : \widetilde{\widetilde\Sigma}^K_M \to Y$ such that $f = \widetilde{f} \circ \pi$.

*Proof:* Standard quotient topology universal property. $\widetilde{f}([\mathbf{u}]) := f(\mathbf{u})$ is well-defined by equivariance. $\square$

**Application:** The SCC energy $\mathcal{E}$ is $S_K$-equivariant (proved in `02c_minimization_principle_unordered.md` §3.1). Therefore $\mathcal{E}$ factors through $\pi$: there is a well-defined $\widetilde{\mathcal{E}} : \widetilde{\widetilde\Sigma}^K_M \to \mathbb{R}$ with $\mathcal{E} = \widetilde{\mathcal{E}} \circ \pi$.

Similarly, $K_{\mathrm{act}}(\mathbf{u}) = |\{j : \|u^{(j)}\|_\infty > \varepsilon\}|$ is $S_K$-equivariant (permuting slots doesn't change the count). So $K_{\mathrm{act}}$ factors through $\pi$ to a well-defined $\widetilde{K}_{\mathrm{act}} : \widetilde{\widetilde\Sigma}^K_M \to \mathbb{Z}_{\geq 0}$. This is how $K_{\mathrm{act}}$ is already orbit-invariant in the canonical theory.

---

**End of `02b_reduction_map_pi.md`. §2 (reduction map) complete: $\pi$ constructed, continuity proved, local sections defined on open stratum, fiber structure (discrete, finite) characterized. Day 3 Bronze criterion §2 (reduction): MET. Continues to `02c_minimization_principle_unordered.md`.**
