# 10_sigma_multi_D_concrete.md — σ_multi^(D) Concrete Computation: T²_{20} K=2 d=8

**Session:** 2026-04-28 (W5 Day 2 Phase 3, E2).
**Target:** Match β-level concrete depth for Approach D (equivariant cohomology / orbit-type invariant) by computing σ_multi^(D) explicitly for the same setup as `05_sigma_multi_concrete_T2_K2.md` (T²_{20}, K=2, d=8).
**Resolves:** Phase 3 weakness #4 (Approach D framework-only).
**Depends on reading:** `06_approach_AB_equivalence_and_D.md` §3 (Approach D framework); `05_sigma_multi_concrete_T2_K2.md` §2-§5 (β concrete computation, comparison target).
**Status:** **Cat C → Cat B target sketched**. Concrete invariant computed for one case; full equivariant cohomology framework still W7+ work.

---

## §1. Setup (matches `05_*` §1)

- 2D torus $T^2_{20}$, $|X| = 400$.
- $\mathrm{Aut}(G) = (\mathbb{Z}_{20})^2 \rtimes D_4$, $|\mathrm{Aut}(G)| = 3200$.
- K=2, two disks at $\mathbf{c}_1 = (0, 0), \mathbf{c}_2 = (8, 0)$.
- Each disk $D_4$-symmetric tanh profile, c=0.10 each.
- Inter-disk distance $d_{\min} = 8$ (well-separated, regime R1).

The full symmetry group acting on the K=2 configuration space:
$$\Gamma := \mathrm{Aut}(G) \wr S_2 = (\mathrm{Aut}(G) \times \mathrm{Aut}(G)) \rtimes S_2.$$
$|\Gamma| = 3200^2 \cdot 2 = 20\,480\,000$.

---

## §2. Orbit-Type Invariant

### 2.1 Joint stabilizer (per `05_*` §2.4 + `08_*` corrected)

$G_{\mathbf{u}^*, 12} = D_4 \wr S_2$, $|G_{\mathbf{u}^*, 12}| = 128$.

The conjugacy class of this subgroup in $\Gamma$ is the **orbit-type label**:
$$[\mathbf{u}^*]_{\Gamma} := \big[ \mathrm{Stab}_{\Gamma}(\mathbf{u}^*) \big]_{\mathrm{conj}} = [D_4 \wr S_2]_{\mathrm{conj}, \Gamma}. \tag{2.1}$$

### 2.2 Counting orbit-types in $\Gamma$

Subgroups of $\Gamma$ isomorphic to $D_4 \wr S_2$: the conjugacy class is determined by:
- Choice of two $D_4$ subgroups in $\mathrm{Aut}(G)$ (representing the two formations' point-group stabilizers).
- Choice of an involutive element $\rho \in \mathrm{Aut}(G)$ that swaps them.
- Modulo conjugation by $\Gamma$.

For $T^2_{20}$:
- $D_4$ subgroups of $\mathrm{Aut}(G)$: there are $|\mathrm{Aut}(G)| / |\mathrm{Norm}(D_4)|$ conjugates of any single $D_4$, and modulo conjugation just one conjugacy class ($D_4$ at origin / center / lattice corners are all conjugate by translation).
- Pairs $(D_4, D_4)$ of subgroups in $\mathrm{Aut}(G)$: parameterized by relative position of their "centers" on $T^2_{20}$.
- Involutive $\rho$: 180° rotation about midpoint, requires the two centers to be antipodally placed (i.e., separation vector compatible with 180° rotation: must be self-mapped under $-\mathrm{id}$, which on torus means separation $(d_x, d_y)$ with $2 d_x \equiv 0 \mod 20$ AND $2 d_y \equiv 0 \mod 20$, i.e., $d_x \in \{0, 10\}$, $d_y \in \{0, 10\}$).

For separation $(8, 0)$: $2 \cdot 8 = 16 \neq 0 \mod 20$. So **180° rotation by midpoint $(4, 0)$ is NOT a graph automorphism for separation 8**!

Wait, but `05_*` §2.3 claimed 180° rotation about midpoint $(4, 0)$ is the involutive $\rho$. Let me recheck.

The 180° rotation about $(4, 0)$ on $T^2_{20}$ is the map $(x, y) \to (8 - x, -y) \mod 20$. Check this maps $(0, 0) \to (8, 0)$ ✓ and $(8, 0) \to (0, 0)$ ✓.

Is this a **graph automorphism** of $T^2_{20}$? Yes, because rotations and reflections of the lattice that preserve graph adjacency are automorphisms. The map $(x, y) \to (8 - x, -y) \mod 20$ preserves adjacency (sends edges to edges), so it's an automorphism.

Is it **involutive**? $\rho^2(x, y) = (8 - (8 - x), -(-y)) = (x, y)$. ✓

So $\rho$ is involutive AND maps $\mathbf{c}_1 = (0,0) \leftrightarrow \mathbf{c}_2 = (8, 0)$. Good.

### 2.3 Orbit-type label as discrete invariant

For our setup, the orbit-type label is well-defined. Distinguishes:
- ($D_4 \wr S_2$ with separation 8 along x-axis) — this case.
- ($D_4 \wr S_2$ with separation 10 along x-axis) — DIFFERENT orbit-type (different conjugacy class because translation by 10 is order 2 on $T^2_{20}$, giving different rotation midpoint).
- ($D_4 \wr S_2$ with separation $(d_x, d_y)$ with both nonzero) — different orbit-type (rotation midpoint not on x-axis).

**σ_multi^(D)** *= the conjugacy class label of $G_{\mathbf{u}^*, 12}$ in $\Gamma$* — finite set of labels, each is a discrete invariant.

For our specific setup:
$$\sigma_{\text{multi}}^{(D)}(\mathbf{u}^*) = \big[ D_4 \wr S_2 \text{ with } (8, 0)\text{-separation, x-axis swap} \big]. \tag{2.2}$$

### 2.4 Comparison to σ_multi^(A) per `05_*`

σ_multi^(A) = $(\mathcal{F}_{\text{total}}=2; \{\sigma_1, \sigma_2\}; \sigma_{12})$ — **continuous data** (eigenvalues that depend on $\beta, c, \lambda_{\mathrm{rep}}$).

σ_multi^(D) = orbit-type conjugacy class — **purely discrete data** (independent of $\beta, c, \lambda_{\mathrm{rep}}$).

**Different information**:
- A is more granular within a single orbit-type (distinguishes $\lambda_{\mathrm{rep}} = 0.01$ from $\lambda_{\mathrm{rep}} = 0.1$).
- D distinguishes between configurations with different orbit-types (e.g., $d=8$ vs $d=10$ separation).
- D is invariant under continuous deformation within orbit (gives stability info).

---

## §3. Equivariant Cohomology Class

### 3.1 The cohomology setup

The K=2 configuration space $\Sigma^2_{(40, 40)}$ is a smooth manifold with $\Gamma$-action. The minimizer $\mathbf{u}^*$ is a fixed point of $G_{\mathbf{u}^*, 12} = D_4 \wr S_2$ acting on $\Sigma^2_{(40, 40)}$.

Equivariant cohomology $H^*_\Gamma(\Sigma^2_{(40, 40)}; \mathbb{Z})$ contains:
- **Borel cohomology**: $H^*_\Gamma = H^*(E\Gamma \times_\Gamma \Sigma^2_{(40, 40)})$ where $E\Gamma$ is a contractible space with free $\Gamma$-action.
- For $\Gamma$ finite, simplifies via Cartan model / Atiyah-Segal completion.

### 3.2 Localization to fixed points

By Atiyah-Bott localization (for finite group actions on smooth manifolds with isolated fixed points):
$$H^*_\Gamma(\Sigma^2; \mathbb{Q}) \cong \bigoplus_{\mathbf{u}^* \in \Sigma^{2, \Gamma}} H^*(BG_{\mathbf{u}^*}; \mathbb{Q}),$$
where the sum is over $\Gamma$-fixed points and $BG_{\mathbf{u}^*}$ is the classifying space of the stabilizer.

For our case, $\mathbf{u}^*$ is one of the $\Gamma$-fixed-point orbits, with stabilizer $G_{\mathbf{u}^*, 12} = D_4 \wr S_2$.

The contribution of this orbit to $H^*_\Gamma(\Sigma^2; \mathbb{Q})$ is:
$$H^*(B(D_4 \wr S_2); \mathbb{Q}). \tag{3.1}$$

### 3.3 Group cohomology of $D_4 \wr S_2$

$H^*(BG; \mathbb{Q})$ for finite $G$ is well-known:
$$H^*(BG; \mathbb{Q}) \cong \mathbb{Q}[c_1, c_2, \ldots]^G,$$
the ring of $G$-invariant polynomials in the Chern classes of the regular representation. For finite $G$, $H^*(BG; \mathbb{Q}) = H^0(BG; \mathbb{Q}) = \mathbb{Q}$ (only the constant cohomology is non-trivial in rational coefficients).

So **rational equivariant cohomology** is too coarse — it just records the *number* of orbit-types, not their identities.

Need **integer coefficients** $\mathbb{Z}$ (or $\mathbb{Z}_p$ for prime $p$) for finer invariant.

### 3.4 Integer cohomology $H^*(B(D_4 \wr S_2); \mathbb{Z})$

For $G = D_4$: $H^*(BD_4; \mathbb{Z})$ has known structure (Adem-Milgram *Cohomology of Finite Groups* §IV).
- $H^1(BD_4; \mathbb{Z}/2) = (\mathbb{Z}/2)^2$ (two generators $u, v$).
- $H^2(BD_4; \mathbb{Z}/2) = (\mathbb{Z}/2)^3$.
- Higher cohomology has explicit formulas.

For $G \wr S_2$: cohomology computed via Künneth + transfer (Hopf):
$$H^*(B(G \wr S_2); \mathbb{Z}) \cong (H^*(BG)^{\otimes 2})^{S_2} \oplus \text{transfer terms}.$$

The full computation is non-trivial; for the orbit-type-distinguishing role, we use the **lowest non-zero cohomology class** as a fingerprint.

### 3.5 Concrete invariant: $H^1$ part

$H^1(B(D_4 \wr S_2); \mathbb{Z}/2) = $ abelianization of $D_4 \wr S_2$ tensored with $\mathbb{Z}/2$.

**Abelianization**: $(D_4 \wr S_2)^{\mathrm{ab}} = D_4^{\mathrm{ab}} \times D_4^{\mathrm{ab}} \rtimes S_2 / \text{commutators}$.

For $D_4$: $D_4^{\mathrm{ab}} = (\mathbb{Z}/2)^2$ (kills the rotation subgroup, keeps the two reflections).

So $(D_4 \wr S_2)^{\mathrm{ab}} = ((\mathbb{Z}/2)^2 \times (\mathbb{Z}/2)^2) / S_2\text{-action}$.
$S_2$ acts by swapping the two factors.
Quotient: $(\mathbb{Z}/2)^2 \times \mathbb{Z}/2$ (where the first $(\mathbb{Z}/2)^2$ is the diagonal of the original $(\mathbb{Z}/2)^4$, fixed by $S_2$; the second $\mathbb{Z}/2$ comes from $S_2$ itself).

So $H^1(B(D_4 \wr S_2); \mathbb{Z}/2) = (\mathbb{Z}/2)^3$, with generators:
- Two "diagonal" reflections ($\sigma_x \otimes \sigma_x$, $\sigma_y \otimes \sigma_y$).
- One "swap" $\tau$.

**σ_multi^(D) refined value** (for our T²_{20} K=2 d=8 setup):
$$\sigma_{\text{multi}}^{(D)}(\mathbf{u}^*) := H^1(BG_{\mathbf{u}^*, 12}; \mathbb{Z}/2) = (\mathbb{Z}/2)^3, \tag{3.2}$$
with explicit generators identified above.

This **discrete invariant** (a $(\mathbb{Z}/2)^3$ vector space, three generators) is the σ_multi^(D) data.

### 3.6 Distinguishing Power of $H^1$

Two configurations with **same** $H^1$:
- Both K=2 with $D_4$-symmetric disks at antipodally-related positions on $T^2_{20}$.

Two configurations with **different** $H^1$:
- K=2 with $D_4$-symmetric disks vs $\mathbb{Z}_4$-symmetric disks (different individual stabilizers → different wreath product → different $H^1$).
- K=3 instead of K=2 (different wreath base group $S_3$ instead of $S_2$ → different $H^1$).

So $H^1$ distinguishes **major orbit-type changes** (K, individual symmetry, swap symmetry) but is INVARIANT under continuous deformation within an orbit-type (changing $\beta, c$, or even $\lambda_{\mathrm{rep}}$).

This is the **persistence** information of σ_multi^(D): topological, not metric.

---

## §4. Approach D vs A Comparison Concrete

For our setup (T²_{20} K=2 d=8 c=0.10 β=4.0 λ_rep=0.1):

**σ_multi^(A) Phase 3 measurement** (per `05_*` §6.2 + Phase 3 E9 numerical):
- $\sigma_1 = \sigma_2 = $ Commitment 14 σ-tuple of single disk on T²_{20} c=0.10 β=4.0. Per Phase 3 E9: low eigenvalues $[0, 0.0019, 0.0064, 0.0279, ...]$ in $D_4$-irrep sectors.
- $\sigma_{12} = $ joint Hessian eigenvalues = per-block ± λ_rep · c_eff (with c_eff ≈ 0.33 measured).
- Continuous values, depend on $(\beta, c, \lambda_{\mathrm{rep}})$.

**σ_multi^(D) Phase 3 measurement**:
- Orbit-type label = $[D_4 \wr S_2 \text{ with d=8 separation, x-axis swap}]$.
- $H^1 = (\mathbb{Z}/2)^3$ with explicit generators.
- Discrete, independent of $(\beta, c, \lambda_{\mathrm{rep}})$.

### 4.1 What D adds beyond A

In well-separated regime, A determines D up to the orbit-type label (per `06_*` §3.5 claim). **Phase 3 contribution**: D adds **explicit topological labels** (the $(\mathbb{Z}/2)^3$ generators) that A doesn't carry.

But these topological labels are GENERIC for our setup — they don't depend on $d_{\min}$ or $\lambda_{\mathrm{rep}}$. They DO change if we go to a different orbit-type (different K, different individual symmetry).

### 4.2 What A adds beyond D

A captures the **continuous spectrum** which D doesn't. Specifically:
- λ_rep dependence of joint eigenvalues.
- Goldstone instability threshold (T-σ-Multi-1) — quantitative.
- PN-barrier-lifted Goldstone bound.

So A and D are **complementary**:
- A = continuous spectroscopic data (per orbit).
- D = discrete topological label (across orbits).

---

## §5. Promotion Path and NQ Spawns

### 5.1 σ_multi^(D) Cat C → Cat B target

With concrete computation in §2-§3, σ_multi^(D) is:
- Definition: orbit-type conjugacy class + lowest cohomology generator.
- Well-defined: ✓ (group cohomology is a topological invariant).
- Computable: ✓ for finite-group actions on smooth manifolds.
- Comparable to A: ✓ (different information layers).

Cat status: **Cat C → Cat B target** (concrete framework operational; full Cat A requires higher-cohomology computation for richer invariants).

### 5.2 NQ Spawns

**NQ-202** (Phase 3 E2 NEW, W7+): Compute $H^2, H^3$ of $B(D_4 \wr S_2)$ explicitly. Higher cohomology may distinguish orbit-types not separated by $H^1$.

**NQ-203** (Phase 3 E2 NEW, W7+): For K-formation systems with K > 2, generalize $\sigma_{\mathrm{multi}}^{(D)} = H^*(B(G \wr S_K))$. Use Specht/James-Kerber wreath-product cohomology.

**NQ-204** (Phase 3 E2 NEW, W7+): Topological-K transition: at parameter values where $\mathbf{u}^*$ moves from one orbit-type to another (e.g., $\lambda_{\mathrm{rep}}$ tuning that makes K=2 → K=1 merger), σ_multi^(D) jumps discontinuously. Connect to canonical K-jump phenomena.

---

## §6. Cross-References

- Approach D framework: `06_approach_AB_equivalence_and_D.md` §3.
- σ_multi^(A) concrete (comparison): `05_sigma_multi_concrete_T2_K2.md`.
- Lemma 5.1 Step 3 corrected: `08_lemma5_1_step3_proof.md`.
- T-σ-Multi-1 Cat A: `09_goldstone_instability_proved.md`.
- Group cohomology: Adem-Milgram *Cohomology of Finite Groups* (Springer 2004); Brown *Cohomology of Groups* (Springer 1982); for wreath products: Macdonald *Symmetric Functions and Hall Polynomials* §App B.
- Atiyah-Bott localization: Atiyah-Bott *J. Diff. Geom.* 1984.

---

**End of 10_sigma_multi_D_concrete.md.**
**Status: σ_multi^(D) Cat C → Cat B target with concrete H^1 computation = (Z/2)^3 for T²_{20} K=2 d=8. NQ-202/203/204 spawned.**
