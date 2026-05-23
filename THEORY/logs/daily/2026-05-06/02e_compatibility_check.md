> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]

# 02e_compatibility_check.md — Compatibility Check: Class-Level Formalism vs Existing Theory

**Session:** 2026-05-06 (W6 Day 3 G3.2, sub-file of `02_op_0009_pre_substantive_start.md`).
**Goal:** §5 of OP-0009-Pre — compatibility of unordered class formalism with σ-framework, T-Persist-K, T-L1-F, Commitment 16, and closure operators.
**Status (Cat C sketch, Gold):** All §5.1-§5.5 are first-order sketches; full compatibility proofs are W7 D4-D5 work.

---

## §5.1 σ-Framework Compatibility (T-σ-Lemma-1/2/3, T-σ-Theorem-3/4, T-σ-multi-A/D-Static)

**Current status:** σ-framework (canonical §10 + T-σ theorems) is defined for *fixed K* with ordered K-field $\mathbf{u}$.

**Multi-formation σ-signature:** The static σ-signature $\sigma^A(\mathbf{u})$ (D-6a, canonical §10.4) assigns a formation signature at the ordered level — it knows *which* formation is which.

**Class-level question:** Is $\sigma^A(\mathbf{u})$ $S_K$-equivariant? In other words, does $\sigma^A(\sigma \cdot \mathbf{u}) = \sigma \cdot \sigma^A(\mathbf{u})$ (where $S_K$ acts on the signature by permuting component labels)?

**Sketch answer:** The σ-signature $\sigma^A$ encodes the *pattern* of which nodes co-belong to which formation. Permuting slots permutes the labels in the signature. So $\sigma^A$ is equivariant under the $S_K$-action on signatures:
$$\sigma^A(\sigma \cdot \mathbf{u})_j = \sigma^A(\mathbf{u})_{\sigma^{-1}(j)} \quad \text{(the } j\text{-th component of the signature after permutation is the original } \sigma^{-1}(j)\text{-th component)}.$$

**Class-level σ-signature:** Define $[\sigma^A([\mathbf{u}}])] = \sigma^A(\mathbf{u}) / S_K$ — the *unordered multi-set* of formation signatures. This is $S_K$-invariant and well-defined at the class level.

**T-σ-multi-A-Static / T-σ-multi-D-Static (Cat A, canonical W5 D4):** These theorems state that the static σ-signature of a well-separated multi-formation is (a) in the anti-aligned set $\mathcal{A}$ / (b) in $\mathcal{D}$ (non-dominant neighbor condition). Both properties are properties of *individual slots*, applied to each $u^{(j)}$ separately. As such, they are $S_K$-invariant: if $\mathbf{u}$ satisfies T-σ-multi-A-Static, so does $\sigma \cdot \mathbf{u}$, and the class $[\mathbf{u}]$ inherits the property. ✓ (sketch)

**W7 D4 work needed:** Formalize the $S_K$-equivariance claim for $\sigma^A$ in general; check T-σ-Theorem-4 (continuum-vs-discrete caveat) at class level; check OP-0008 (σ^A K-jump) compatibility with unordered class transitions.

---

## §5.2 T-Persist-K Compatibility (T-Persist-K-Sep / Weak / Unified)

**T-Persist-K chain (canonical §13, Cat A conditional):** Persistence theorems classify stability of K-formation configurations under gradient flow in three regimes: well-separated, weakly-interacting, strongly-interacting.

**Class-level question:** Are the regime conditions and stability properties $S_K$-invariant?

**Sketch answer:**
- **Well-separated regime (T-Persist-K-Sep):** condition $\langle u^{(j)}, u^{(k)} \rangle \leq \delta_{\mathrm{sep}}$ for all $j \neq k$. This is symmetric in $j, k$ — $S_K$-invariant. ✓
- **Weakly-interacting regime (T-Persist-K-Weak):** conditions on pairwise interaction strengths, which are symmetric under slot permutation. $S_K$-invariant. ✓
- **Stability conclusions:** gradient flow starting at $\mathbf{u}$ converges to $\hat{\mathbf{u}}$ (a minimizer); the same is true for $\sigma \cdot \mathbf{u}$ converging to $\sigma \cdot \hat{\mathbf{u}}$. At class level: $[\mathbf{u}] \to [\hat{\mathbf{u}}]$ in the gradient flow on $\widetilde{\widetilde\Sigma}^K_M$ (induced by $\widetilde{\mathcal{E}}$). ✓ (sketch)

**Note:** The gradient flow on $\Sigma^K_M$ factorizes to a flow on $\widetilde{\widetilde\Sigma}^K_M$ via $\pi$, since $\mathcal{E}$ is $S_K$-equivariant (§3.1) and $\pi$ is equivariant. The induced flow on the quotient is well-defined.

**W7 D5 work needed:** Formalize the induced gradient flow on $\widetilde{\widetilde\Sigma}^K_M$ rigorously (differential structure on orbifold quotient; tangent space at class level). Full persistence theorem statement at class level.

---

## §5.3 T-L1-F / T-L1-M Compatibility

**T-L1-F (canonical §13 ~line 1452, Cat A conditional under L1-J regime):** The L1-J feasibility theorem states that an active set $A^\varepsilon(\mathbf{u}) = \{j : \lVert u^{(j)} \rVert_\infty > \varepsilon\}$ satisfies $\vert A^\varepsilon\vert = K_{\mathrm{act}}^\varepsilon$ and there is a bijection $\mathcal{A}_{\mathrm{bar}} : \bar{A}^\varepsilon \to \text{(threshold active formations)}$.

**Class-level question:** T-L1-F's bijection $\mathcal{A}_{\mathrm{bar}}$ uses *ordered* slot indices to construct the correspondence. Does this lift to the class level?

**Sketch answer:**
- $K_{\mathrm{act}}^\varepsilon(\mathbf{u}) = \vert A^\varepsilon(\mathbf{u})\lvert = \rvert\{j : \lVert u^{(j)} \rVert_\infty > \varepsilon\}\vert $. This is $S_K$-invariant (just a count). ✓
- The active *set* $A^\varepsilon(\mathbf{u}) \subseteq \{1, \ldots, K\}$ is an index set — it is $S_K$-equivariant: $A^\varepsilon(\sigma \cdot \mathbf{u}) = \sigma(A^\varepsilon(\mathbf{u}))$.
- The active *fields* $\{u^{(j)} : j \in A^\varepsilon(\mathbf{u})\}$ form an unordered multi-set of cohesion fields. This is $S_K$-invariant. ✓
- The bijection $\mathcal{A}_{\mathrm{bar}}$: at the class level, the correct statement is a *multi-set bijection* (not an ordered bijection). The number of active formations $K_{\mathrm{act}}^\varepsilon$ equals the size of the active formation multi-set. The "bar" structure (bar active set in L1-J sense) carries over to the multi-set level.

**What is new at class level (T-L1-F lift):** The ordered bijection $\mathcal{A}_{\mathrm{bar}}$ becomes a *cardinality equality* at the class level: $\vert \text{active class multi-set}\vert = K_{\mathrm{act}}^\varepsilon$. The bijection itself (ordering of formations) is a modeling-layer artifact.

**T-L1-M compatibility:** T-L1-M counts $K_{\mathrm{soft}} = \vert \{j : \lVert u^{(j)} \rVert_\infty \in (\varepsilon, 1-\varepsilon)\}\vert $ (soft slots). This is also $S_K$-invariant (count of fields satisfying a unilateral threshold condition). ✓

**W8 D3 work needed:** Formalize the multi-set bijection statement for T-L1-F at class level; derive the correct class-level statement of the L1-J regime conditions.

---

## §5.4 Commitment 16 Compatibility (K_field / K_act Two-Tier)

**Commitment 16 (canonical, CV-1.5.1):** $K_{\mathrm{field}}$ = numerical truncation parameter (maximum slot count; modeling-layer ceiling); $K_{\mathrm{act}} = \vert \{j : \lVert u^{(j)} \rVert_\infty > \varepsilon\}\vert $ = derived active formation count (orbit-invariant by §5.3).

**Class-level reading:**
- $K_{\mathrm{field}}$ = the number of slots in the ordered representative, which equals the orbit group order ($\vert S_{K_{\mathrm{field}}}\vert = K_{\mathrm{field}}!$). At the class level, $K_{\mathrm{field}}$ is the "ambient" size of the modeling layer — it determines the *capacity* but not the *actual* formation count.
- $K_{\mathrm{act}} = \widetilde{K}_{\mathrm{act}}([\mathbf{u}])$ = orbit-invariant derived count. This is well-defined at the class level as established in `02b` §2.5. ✓

**Commitment 16 unordered version:**
- Layer I (architectural): $K_{\mathrm{field}}$ = size of the unordered class $\vert [\mathbf{u}]\vert $ (multiset cardinality including inactive slots) = a modeling-layer parameter.
- Layer II (active): $K_{\mathrm{act}} = \widetilde{K}_{\mathrm{act}}([\mathbf{u}])$ = derived from the actual cohesion fields, orbit-invariant.

This is fully consistent with Commitment 16; it sharpens the layer distinction by making explicit that $K_{\mathrm{field}}$ is the ambient group order and $K_{\mathrm{act}}$ is the orbit-invariant count. ✓

---

## §5.5 Closure Operator Compatibility

**Closure operator (canonical §6.1):** $\mathrm{Cl}(u) : X \to [0,1]$ is a single-slot operator applied to a cohesion field $u$. In K-field architecture, each slot has a per-slot closure $\mathrm{Cl}^{(j)} u^{(j)} := \mathrm{Cl}(u^{(j)})$ (applied independently to each slot).

**Class-level question:** Is the per-slot closure system compatible with the unordered class?

**Sketch answer:** The multi-slot closure is the map $\mathbf{u} \mapsto (\mathrm{Cl}(u^{(1)}), \ldots, \mathrm{Cl}(u^{(K)}))$. This is $S_K$-equivariant:
$$\mathrm{Cl}(\sigma \cdot \mathbf{u})_j = \mathrm{Cl}(u^{(\sigma^{-1}(j))}) = [\sigma \cdot (\mathrm{Cl}(u^{(1)}), \ldots, \mathrm{Cl}(u^{(K)}))]_j.$$
So the closure operator commutes with $S_K$-action. The induced closure at class level:
$$\widetilde{\mathrm{Cl}} : \widetilde{\widetilde\Sigma}^K_M \to \widetilde{\widetilde\Sigma}^K_M, \qquad \widetilde{\mathrm{Cl}}([\mathbf{u}]) = [\mathrm{Cl}(\mathbf{u})] = \{\mathrm{Cl}(u^{(1)}), \ldots, \mathrm{Cl}(u^{(K)})\}$$
is the *multi-set* of individual closure operators applied to each field. ✓

**A3 stabilization tendency (canonical §4.3):** $\mathrm{Cl}$ has the stabilization tendency (Axiom 3), not idempotence. At class level: $\widetilde{\mathrm{Cl}}([\mathbf{u}])$ has the same stabilization tendency (since it acts field-by-field). ✓

**W7 D5 work needed:** Verify that the interplay between closure and the inter-slot repulsion $\lambda_{\mathrm{rep}}$ is $S_K$-invariant at the gradient-flow level (the gradient of $\mathcal{E}$ includes $\lambda_{\mathrm{rep}}$ coupling, and closure is applied to the result of gradient flow, not to the energy directly).

---

## §5.6 Summary: Compatibility Scorecard

| Existing theory | Class-level compatibility | Status | W7 work needed |
|---|---|---|---|
| σ-framework (T-σ-Lemma/Theorem) | $S_K$-equivariant; class-level $[\sigma^A]$ = unordered multiset of signatures | ✓ sketch | W7 D4: formalize |
| T-σ-multi-A/D-Static (Cat A) | Per-slot properties → $S_K$-invariant → class inherits | ✓ sketch | W7 D4 |
| T-Persist-K-Sep/Weak/Unified | Regime conditions $S_K$-invariant; induced flow on quotient | ✓ sketch | W7 D5: formalize |
| T-L1-F (active set bijection) | $K_{\mathrm{act}}$ orbit-invariant; ordered bijection → class-level cardinality equality | ✓ sketch | W8 D3: multi-set bijection |
| T-L1-M (soft count) | $S_K$-invariant count | ✓ trivial | — |
| Commitment 16 ($K_{\mathrm{field}}/K_{\mathrm{act}}$) | $K_{\mathrm{act}}$ orbit-invariant; $K_{\mathrm{field}}$ = modeling-layer ambient capacity | ✓ substantive | — |
| Closure operator $\mathrm{Cl}$ | $S_K$-equivariant; $\widetilde{\mathrm{Cl}}$ well-defined at class level | ✓ sketch | W7 D5 |

**Preliminary finding:** No incompatibility found at the sketch level. All existing theorems and commitments appear compatible with the class-level formalism. The ordered K-field formalism is a valid *coordinate system* on $\widetilde{\widetilde\Sigma}^K_M$ and all existing results can be read as coordinate-level statements with coordinate-free class-level counterparts.

---

**End of `02e_compatibility_check.md`. §5 compatibility check complete (Cat C sketch): σ-framework, T-Persist-K, T-L1-F/M, Commitment 16, closure operator — all sketched compatible. No incompatibility found. Day 3 Gold criterion §5: MET (Cat C sketch as planned). G3.2 cluster complete: Bronze ✓ Silver ✓ Gold ✓ (sketch level).**
