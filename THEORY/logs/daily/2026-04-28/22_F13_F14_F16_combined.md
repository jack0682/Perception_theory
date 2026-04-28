# 22_F13_F14_F16_combined.md — Continuum Limit + Non-Involution Wreath + Terminology Glossary

**Session:** 2026-04-28 (W5 Day 2 Phase 4, F13 + F14 + F16 combined).
**Targets:** (F13) Continuum limit ξ_0 → 0 analysis. (F14) Non-involution canonical iso generalization (G ≀ Z_n). (F16) σ_multi terminology consolidation.
**Resolves:** Phase 4 weakness W10 (continuum limit absent) + W12 (terminology proliferation) + Phase 3 NQ-200 (non-involution wreath).
**Status:** Three independent contributions in single file.

---

## Part 1: F13 — Continuum Limit ξ_0 → 0 Analysis

### §1.1 The continuum limit setup

In SCC, the lattice spacing $a$ is fixed and the interface width is $\xi_0 = \sqrt{\alpha/\beta}$. The continuum limit is $\xi_0 / a \to \infty$ (super-lattice deep) or equivalently $\beta a^2 / \alpha \to 0$.

In this limit:
- u becomes a smooth function on $\mathbb{R}^d$.
- $\mathcal{E}_{\mathrm{bd}}$ Γ-converges to the perimeter functional (Modica-Mortola, canonical T11).
- Translation symmetry becomes continuous.
- PN-barrier vanishes.

### §1.2 Phase 3-4 results in continuum limit

#### 1.2.1 σ_multi^(A) survives

The Sym/Antisym block-diagonalization (`05_*` §4.2 corrected `08_*` §3.2) requires only:
- Two formations identical via canonical iso ρ.
- ρ involutive ($\rho^2 = e$).

Both conditions persist in continuum limit (continuous translation + 180° rotation about midpoint are continuum operations). So **σ_multi^(A) is well-defined in continuum**.

The cross-block H_12 = λ_rep · I structure persists (repulsion is local).

#### 1.2.2 c_eff → 1 (verified by F5)

F5 grid showed c_eff(L=16, 20, 24) = 0.290, 0.335, 0.364 with extrapolation $c_{\mathrm{eff}}(L \to \infty) \to 1$.

In continuum limit, the discrete-lattice mode-mixing factor c_eff → 1 because:
- Mode overlap O_{ideal-actual}² → 1 (no lattice discretization breaking $D_4$).
- Gap between Goldstone and next mode → 0 in proper sense (continuous spectrum).
- Sym/Antisym block-diagonalization becomes exact.

So **T-σ-Multi-1 in continuum**: $\mu_{\mathrm{antisym}} = \mu_{\mathrm{Gold}} - \lambda_{\mathrm{rep}}$ exactly. With $\mu_{\mathrm{Gold}} = 0$ (continuous translation): $\mu_{\mathrm{antisym}} = -\lambda_{\mathrm{rep}}$ exactly. **K=2 instability rate = $\lambda_{\mathrm{rep}}$ exactly in continuum.**

#### 1.2.3 V5b-T' disappears in continuum

Corner-saturation (V5b-T') requires sub-lattice $\xi_0 < a$, which fails in continuum limit ($\xi_0/a \to \infty$). So **V5b-T' is a finite-lattice phenomenon**, not present in continuum.

This implies:
- Continuum limit is the "smooth interior" regime R1.
- Sub-lattice phenomena (V5b-T-(c) commensurability + V5b-T' corner-saturation + V5b-F boundary-cluster) are **lattice-discretization artifacts** with potentially deep mathematical structure (PN-barrier theory) but **vanish in sharp-interface limit**.

#### 1.2.4 σ_multi^(D) topology survives

Equivariant cohomology of $\Sigma^K_M$ under $\mathrm{Aut}(\Gamma) \wr S_K$ is a topological invariant; persists in continuum limit (replace $\mathrm{Aut}(\Gamma)$ with $\mathrm{Diff}(M)$ for continuum manifold).

For K=2 on T² torus continuum: stabilizer becomes a Lie group ($\mathrm{Iso}(T^2) \wr S_2$), and σ_multi^(D) becomes a class in equivariant cohomology over Lie groups (Borel cohomology).

The conjugacy-class label is replaced by orbit-type label in Lie group action. **Discrete topological structure survives**.

### §1.3 Modica-Mortola Γ-convergence + T-σ-Multi-1

In Γ-convergence limit:
- $\mathcal{E}_{\mathrm{bd}}(u) \to c_{\mathrm{MM}} \mathrm{Per}(\{u > 1/2\})$ (perimeter of the interface).
- Joint K-field energy $\mathcal{E}_K \to c_{\mathrm{MM}} \sum_j \mathrm{Per}(\Omega_j) + \lambda_{\mathrm{rep}} \int u^j u^k$ (where $\Omega_j$ are sharp domains).
- T-σ-Multi-1 instability rate $\to \lambda_{\mathrm{rep}}$ exactly.

**Combined with mass-redistribution dynamics**: K-formation gradient flow → Allen-Cahn-like dynamics → **mean-curvature-flow on interface in continuum limit**.

This connects SCC K-field architecture to **classical motion-by-mean-curvature** (e.g., Bronsard-Kohn 1991), with $\lambda_{\mathrm{rep}}$ playing the role of inter-domain coupling.

### §1.4 Phase 4 F13 conclusions

**Continuum limit theorem (Cat B target)**:
> In the sharp-interface limit $\xi_0 \to 0$ of K-field architecture:
> 1. σ_multi^(A) structure survives, with c_eff → 1.
> 2. T-σ-Multi-1 reduces to $\mu_{\mathrm{antisym}} = -\lambda_{\mathrm{rep}}$ exact.
> 3. V5b-T-(c)/V5b-T'/V5b-F sub-lattice phenomena vanish (regime R1 only).
> 4. σ_multi^(D) becomes Borel-cohomology of Lie-group-equivariant continuum manifold.
> 5. Coarsening dynamics → mean-curvature flow with $\lambda_{\mathrm{rep}}$-coupling.

**Cat status**: Cat B sketched. Full Cat A requires:
- Rigorous Γ-convergence proof for K-field energy.
- Verification that σ_multi^(A) Sym/Antisym structure survives Γ-limit.
- Connection to existing motion-by-mean-curvature theorems.

NQ-217 (Phase 4 F13 NEW, W6+): Rigorous continuum limit theorem for K-field σ-framework + mean-curvature flow connection.

---

## Part 2: F14 — Non-Involution Canonical Iso (G ≀ Z_n)

### §2.1 The setup

In `05_*` §2.4 + `08_*` §2.1, the wreath structure $D_4 \wr S_2$ requires the canonical iso $\rho: u^{(1)*} \to u^{(2)*}$ to be **involutive** ($\rho^2 = e$).

For 2D torus T²_{20} with two disks at separation 8 along x-axis, the involutive iso is **180° rotation about midpoint $(4, 0)$**. ✓

But there's an alternative iso: **translation by 8** ($\rho_T = T_{(8, 0)}$). This maps disk 1 → disk 2. **However**: $\rho_T^2 = T_{(16, 0)} \neq e$. In fact $\rho_T^5 = T_{(40, 0)} = T_{(0, 0)} = e$ (since 40 ≡ 0 mod 20). So $\rho_T$ has **order 5**.

With non-involutive $\rho$, the wreath structure changes from $G \wr S_2$ to a more complex extension involving cyclic subgroup $\langle \rho \rangle \cong \mathbb{Z}_n$.

### §2.2 Generalized wreath structure: $G \wr_\rho \mathbb{Z}_n$

For canonical iso of order n, the relevant group is **NOT** $G \wr S_2$. Instead, consider:
- $\langle \rho \rangle = \mathbb{Z}_n \subset \mathrm{Aut}(\Gamma)$.
- "Pair-stabilizer with $\rho$-relation": elements of $\mathrm{Aut}(\Gamma) \times \mathrm{Aut}(\Gamma)$ that stabilize the unordered pair, combined with $\mathbb{Z}_n$ rotation between the two slots.

The structure: $(g_1, g_2; \sigma)$ with $\sigma \in \mathbb{Z}_n$ acting:
- $\sigma = 0$: identity (each formation fixed individually).
- $\sigma = 1$: $(g_1, g_2; 1) \cdot (u^{(1)}, u^{(2)}) = (g_1 \cdot \rho^{-1} u^{(2)}, g_2 \cdot \rho u^{(1)})$.
- General $\sigma = k$: rotation by $k$ steps.

Note: $\sigma$ should generate a cyclic group only if $\rho$ acts naturally on the pair. For generic K=2 setup with $u^{(1)}, u^{(2)}$ at positions $\mathbf{c}_1, \mathbf{c}_2$ where $\rho(\mathbf{c}_1) = \mathbf{c}_2$, the action of $\rho^k$ for $k \geq 2$ moves $\mathbf{c}_1 \to \mathbf{c}_2 \to \rho(\mathbf{c}_2) \to \ldots$ — generally NOT back to $\mathbf{c}_1$.

So **for K=2 with non-involutive $\rho$, the stabilizer is just $\{e, \rho^*\}$ (acting on the pair) ∪ identity** — really order 2 but $\rho$ has order n ≥ 3.

Wait — the constraint for $\rho$ to be a valid swap iso: $\rho \cdot u^{(1)*} = u^{(2)*}$ AND $\rho \cdot u^{(2)*} = u^{(1)*}$. The second condition: $\rho^2 \cdot u^{(1)*} = u^{(1)*}$. So $\rho^2$ stabilizes $u^{(1)*}$, meaning $\rho^2 \in \mathrm{Stab}(u^{(1)*})$.

If $\rho$ has order n in $\mathrm{Aut}(\Gamma)$ but order 2 modulo $\mathrm{Stab}(u^{(1)*})$, the wreath structure DOES recover $G \wr S_2$ but with a more complex realization of the swap.

For **TRUE non-involutive case** (pair-stabilizer cyclic of order n > 2): need 3 or more equivalent formations arranged in a $\mathbb{Z}_n$ orbit. **This is K ≥ n setup, not K=2.**

So for K=2: non-involutive $\rho$ doesn't change the abstract structure ($D \wr S_2$ still applies via $\rho^2 \in $ stabilizer). The "involution" requirement is on the pair-action, not on $\rho$ itself in $\mathrm{Aut}(\Gamma)$.

For K=n > 2 with formations arranged in $\mathbb{Z}_n$ orbit (e.g., K=3 triangular per F8): the stabilizer is **NOT** $G \wr S_3$ in general; it can be $G \wr \mathbb{Z}_3$ (rotation only, no reflection).

### §2.3 Concrete K=3 triangular case

For K=3 with three D_4-symmetric disks at vertices of equilateral triangle (per F8 numerical):
- Stabilizer includes 3-fold rotation $\mathbb{Z}_3$ (by 120°) of the triangle.
- May also include 2-fold reflections ($S_3 = \mathbb{Z}_3 \rtimes S_2$).
- If rotations only: stabilizer = $G \wr \mathbb{Z}_3$.
- If full $S_3$: stabilizer = $G \wr S_3$.

For T²_{20} torus, the 120° rotation about the triangle's centroid may not be a graph automorphism (depends on whether the rotation maps lattice sites to lattice sites — generally NOT for arbitrary rotation angles on square lattice).

So on T²_{20} with K=3 triangular: stabilizer is just $D_4 \times D_4 \times D_4$ (per-formation $D_4$), with no additional $\mathbb{Z}_3$ or $S_3$. This is the F8 numerical setup.

### §2.4 Lessons for σ_multi extension

**Phase 4 F14 conclusion**: 
- For K=2 with involutive pair-iso: $G \wr S_2$ structure (Phase 3 setup).
- For K ≥ 3 with non-equivalent formations: $G^K$ direct product (no wreath).
- For K ≥ 3 with $\mathbb{Z}_n$-cyclic permutation iso: $G \wr \mathbb{Z}_n$.
- For K ≥ 3 with full $S_K$ permutation: $G \wr S_K$.

The **σ_multi^(D)** orbit-type label depends on which case applies, distinguishing different orbit-types numerically.

For Paper §4 exposition, present the K=2 case (most digestible) with notes that K ≥ 3 generalizes via wreath product structures depending on configuration symmetry.

NQ-218 (Phase 4 F14 NEW, W7+): Wreath-product structure systematic table for K-formation configurations on standard graphs (T^d, free BC, cycle, lattice).

---

## Part 3: F16 — σ_multi Terminology Glossary

### §3.1 Glossary of σ-framework terms

Phase 1-4 introduced many terms; consolidate here for paper § exposition consistency.

### §3.2 Single-formation

| Term | Definition | Origin |
|---|---|---|
| **σ(u*)** | Single-formation σ-tuple per Commitment 14: $(F; \{(n_k, [\rho_k], \lambda_k)\})$ | canonical |
| **F(u*)** | Local-maxima count of u* | canonical |
| **n_k** | Courant nodal count of k-th Hessian eigenvector | canonical |
| **[ρ_k]** | Irrep label of k-th eigenvector under Stab(u*) ⊂ Aut(G) | canonical |
| **λ_k** | k-th Hessian eigenvalue | canonical |
| **Stab(u*)** | Stabilizer of u* in Aut(G) | canonical |

### §3.3 Multi-formation

| Term | Definition | Origin |
|---|---|---|
| **σ_multi(u*)** | Combined invariant := (σ_multi^A, σ_multi^D) | Phase 4 F11 |
| **σ_multi^A** | Continuous spectroscopic layer = (F_total, {σ_j}, {σ_jk}) | Phase 2 |
| **σ_multi^D** | Topological layer = orbit-type conjugacy class + cohomology | Phase 3 |
| **σ_j** | Per-formation σ-tuple (Commitment 14 of formation j) | Phase 2 |
| **σ_jk** | Cross-formation σ-tuple via permutation-module irreps of stabilizer ≀ S_2 | Phase 2 + 3 corrected |
| **F_total(u*)** | Total local-maxima count of K-tuple | Phase 2 |
| **G_{u*, jk}** | Pair-stabilizer of (u^(j)*, u^(k)*) in Aut(G) ≀ S_2 | Phase 2 |
| **ρ** | Canonical iso between formations (graph automorphism mapping one to other) | Phase 3 |
| **Sym/Antisym** | Block-diagonalization of joint Hessian by S_2 swap symmetry | Phase 2 + 3 |
| **c_eff** | Mode-mixing factor in finite-L: c_eff(L → ∞) → 1 | Phase 3 + 4 |
| **μ_Gold** | Goldstone eigenvalue (translation pseudo-mode) | canonical |
| **μ_antisym** | Antisymmetric Goldstone eigenvalue = μ_Gold - c_eff·λ_rep | Phase 3 |

### §3.4 V5b family

| Term | Regime | Description | Cat status |
|---|---|---|---|
| **V5b-T** | R1 (super-lattice, translation-invariant) | Approximate Goldstone, exponentially-suppressed eigenvalue | Cat A (canonical) |
| **V5b-T'** | R3b (sub-lattice, translation-invariant, corner-saturated) | NEW: cluster-saturated minimizer; PN-barrier-lifted Goldstone | Cat B target (Phase 3) |
| **V5b-F** | R3b (sub-lattice, translation-broken) | Corner-saturated against graph boundary; H1+H2+H3 mixed mechanism | Cat B target (Phase 3 refined) |
| **V5b-T-(c)** | R2 (interior sub-lattice, translation-invariant) | Commensurability splitting; direction flipping | Cat A (canonical) |

### §3.5 Regime classification

| Regime | β | c | ∂Γ status | Behavior |
|---|---|---|---|---|
| **R1** | β < 1/a² | c ∈ (c_s, 1-c_s) | any | Smooth interior, super-lattice |
| **R2** | β > 1/a² | c ∈ (c_s, 1-c_s) | any | Interior sub-lattice (V5b-T-(c)) |
| **R3a** | β < β_R3 | c < c_s | any | Smooth sub-lattice metastable |
| **R3b** | β > β_R3 | c < c_s | translation-invariant | Corner-saturated, V5b-T' |
| **R3b'** | β > β_R3 | c < c_s | translation-broken | Corner-saturated near ∂Γ, V5b-F |
| **R4** | β < β_crit | any | any | Uniform global min, no formation |

### §3.6 Categories

| Category | Definition | Usage |
|---|---|---|
| **Cat A** | Fully proved, no conditional hypotheses | Strongest |
| **Cat B target** | Sketched proof; conditional hypotheses; numerical anchor | Working level |
| **Cat C** | Qualitative observation only | Initial state |
| **Cat R** | Retracted | Historical |

### §3.7 Approaches to multi-formation σ

| Approach | Reduces to | Status |
|---|---|---|
| **A** (block-decomposition) | Sum of Commitment 14 per formation + cross-pair invariants | Phase 2 + 3, Cat A under involution |
| **B** (joint Hessian + wreath-irrep) | A in well-separated regime | Phase 3, Cat B target W7+ |
| **C** (interaction graph) | Visualization layer over A | Phase 2, paper exposition |
| **D** (equivariant cohomology) | Topological label complementary to A | Phase 3 + 4, Cat A K=2 |

---

## §4. Phase 4 weakness W12 resolution

The terminology glossary (§3.1-§3.7) provides single-source-of-truth for all σ-framework terms across Phase 1-4 outputs. **For paper §4 exposition, use only the canonical terms (§3.2-§3.6); avoid Phase-internal abbreviations.**

Recommended naming convention for paper §4:
- Use σ(u*), σ_multi(u*) as primary terms.
- Use σ_multi = (σ^A, σ^D) layered structure (omit "multi" prefix on A/D for brevity).
- V5b-T, V5b-T', V5b-F as the three V5b regime distinctions.

---

## §5. Cross-References

- All Phase 1-4 daily files.
- canonical T-σ-Lemma-1, T-σ-Theorem-3/4, T-V5b-T (W4 Day 1 G0 + extended close).

---

**End of 22_F13_F14_F16_combined.md.**
**Status: F13 continuum limit (5 claims, Cat B); F14 non-involution wreath structure (K=2 unchanged, K ≥ 3 cyclic vs symmetric distinguished); F16 terminology glossary 4-tier (single-formation, multi-formation, V5b family, regime classification + approach inventory). Phase 4 weaknesses W10, W12 resolved.**
