# sigma_rich_wigner_derivation.md — σ_rich Wigner-von Neumann W_jk Formal Derivation

**Status:** working draft (W5 Day 4, Task #3).
**Created:** 2026-04-30 (W5 Day 4).
**Type:** Formal mathematical derivation of σ_rich Wigner-von Neumann avoided-crossing component $W_{jk}$ — well-definedness, avoided-crossing theorem, Goldstone-pair softening, $\mathrm{Aut}(G)$ invariance.
**Author origin:** Task #3; extends `sigma_rich_augmentation.md` §2.3.3 informal definition.
**Canonical refs:** §11.1 Commitment 14, 14-Multi; §13 T-Persist-K-Sep (Coupling Bound Lemma); T-V5b-T (translation Goldstone); §14 CN10.
**Working refs:** `sigma_rich_augmentation.md` §2.3.3 (W_jk definition); `multi_formation_sigma.md` §5.5 (cross-formation Goldstone-pair observation); `sigma_rich_centroid_derivation.md` (Task #1); `sigma_rich_orientation_derivation.md` (Task #2).

---

## §1. Mission

> **"$W_{jk}(\mathbf{u}) := (\Delta_{jk}^{\mathrm{Gold}}, \theta_{jk}^{\mathrm{mix}}, \mathrm{sign}(d/dt[\Delta_{jk}^{\mathrm{Gold}}]))$ 의 formal derivation: cross-block 2×2 sub-Hessian $\tilde H_{jk}$ Goldstone-pair eigenvalue gap + mixing angle + temporal-sign well-definedness, Wigner-von Neumann avoided-crossing theorem application, $\mathrm{Aut}(G) \wr S_{K_{\mathrm{act}}}$ invariance, Cat status."**

이 working file 은 σ_rich Cat A 승격 path 의 (R2) Wigner-projection eigenvalue collapse rigorous proof 의 핵심 spectral foundation 을 제공한다. Task #1 centroid + Task #2 orientation 과 결합하여 Task #4 Φ_rich determinism proof 를 가능케 한다.

---

## §2. Setup

### §2.1 Cross-block 2×2 sub-Hessian

For $\mathbf{u}^* \in S^\circ_{K_{\mathrm{act}}}$ minimizer of $\mathcal{E}_K$, joint Hessian $H_{\mathrm{joint}}(\mathbf{u}^*)$ on $T_{\mathbf{u}^*} \widetilde\Sigma^K_M$ has block structure $\{H_{ab}\}_{a, b \in \mathrm{act}}$ (per `multi_formation_sigma.md` §3.1).

For a pair $(j, k) \in \mathrm{act}$, $j < k$, the **cross-block 2×2 sub-Hessian** is:
$$\tilde H_{jk}(\mathbf{u}^*) := \begin{pmatrix} H_{jj} & H_{jk} \\ H_{kj} & H_{kk} \end{pmatrix} \in \mathbb{R}^{(n_j + n_k) \times (n_j + n_k)}$$
where $n_j = \dim T_{u^{(j)*}} \Sigma_{m_j}$.

### §2.2 Symmetry and reality

**Lemma 2.1**: $\tilde H_{jk}$ is real symmetric (since $\mathcal{E}_K$ is a real-valued function on $\widetilde\Sigma^K_M$, its Hessian is real symmetric; $H_{jk} = H_{kj}^T$).

By spectral theorem, $\tilde H_{jk}$ admits orthonormal eigendecomposition with $n_j + n_k$ real eigenvalues.

### §2.3 Goldstone-pair subspace

In translation-invariant graph regimes (e.g., $T^2_L$ torus per canonical T-V5b-T), each $u^{(j)*}$ has translation Goldstone modes — eigenvectors of $H_{jj}$ with eigenvalue $0$ (or near-zero in finite-graph approximation). For 2D torus: 2 Goldstone modes per formation (translations in $x, y$).

For cross-block $\tilde H_{jk}$: per `multi_formation_sigma.md` §5.5 Observation 5.4, the per-formation Goldstones become **two near-zero pairs** of eigenvalues, possibly split by inter-formation coupling.

**Definition 2.2 (Goldstone-pair subspace).** $V_{jk}^{\mathrm{Gold}}(\mathbf{u}^*) := $ direct sum of per-formation Goldstone subspaces of $H_{jj}$ and $H_{kk}$, dimension $g_j + g_k$ ($g_j$ = Goldstone count of formation $j$; $g_j = \dim X = 2$ for $T^2_L$).

---

## §3. Wigner-von Neumann Avoided-Crossing Theorem

### §3.1 Statement (classical)

**Theorem 3.1 (Wigner-von Neumann 1929; cf. Reed-Simon IV §XIII.5).** For a smooth one-parameter family of real symmetric matrices $A(t)$, $t \in [0, 1]$, eigenvalue crossings between two simple eigenvalues are *codim-2 generic* — generic 1-parameter families exhibit no eigenvalue crossings; instead, eigenvalues approach and recede ("avoided crossing") with a non-zero minimum gap.

**Mechanism**: at near-crossing, the 2D effective Hamiltonian in the eigenspace of the two close eigenvalues has the form
$$A_{\mathrm{eff}} = \begin{pmatrix} \lambda_+(t) & v(t) \\ v(t) & \lambda_-(t) \end{pmatrix}$$
where $\lambda_\pm(t)$ are diagonal estimates and $v(t)$ is the off-diagonal coupling. The eigenvalue gap is $\Delta(t) = \sqrt{(\lambda_+ - \lambda_-)^2 + 4v^2}$, achieving minimum $2|v(t_0)|$ at the closest-approach time $t_0$.

### §3.2 Application to $\tilde H_{jk}$ near merger

For SCC trajectory $\mathbf{u}(t)$ approaching K-jump time $t^*$ with $(j, k) \to \ell$ merger:
- Effective parameter $\tau = d_{\min}(j, k)(t)$ (inter-formation distance).
- $\tilde H_{jk}(\tau)$ varies smoothly with $\tau$ on the smooth segment.
- Goldstone-pair eigenvalues $\lambda_{jk}^{\mathrm{Gold},\pm}(\tau)$ approach as $\tau \searrow 0$.

**Application of Theorem 3.1**: the Goldstone pair undergoes an avoided crossing (or true crossing in symmetric special cases) at some $\tau = \tau_0 > 0$ before the merger.

### §3.3 Goldstone-pair gap formula

By Coupling Bound Lemma (canonical T-Persist-K-Sep): in well-separated regime,
$$\|H_{jk}\|_{\mathrm{op}} = \lambda_{\mathrm{rep}} \cdot \|I\|_{\mathrm{op}} + O(\exp(-c_0 d_{\min})) \approx \lambda_{\mathrm{rep}}.$$

Restricting to Goldstone-pair subspace $V_{jk}^{\mathrm{Gold}}$, the cross-block coupling is approximately:
$$H_{jk}|_{V^{\mathrm{Gold}}} \approx \lambda_{\mathrm{rep}} \cdot O_{\mathrm{Gold}}(d_{\min})$$
where $O_{\mathrm{Gold}}$ is an exponentially-small overlap matrix (per Coupling Bound Lemma item 2-3).

**Consequence**: Goldstone-pair eigenvalue split:
$$\Delta_{jk}^{\mathrm{Gold}}(d_{\min}) = O(\lambda_{\mathrm{rep}} \cdot \exp(-c_0 d_{\min})).$$

This matches `multi_formation_sigma.md` §5.5 Observation 5.4 prediction.

---

## §4. W_jk Definition (Formal)

### §4.1 Three components

**Definition 4.1 (W_jk formal).** For pair $(j, k) \in \mathrm{act}$, $j < k$:
$$W_{jk}(\mathbf{u}^*) := (\Delta_{jk}^{\mathrm{Gold}}, \theta_{jk}^{\mathrm{mix}}, s_{jk}^{\mathrm{trend}})$$
with components:

**(W4.1a) Gap $\Delta_{jk}^{\mathrm{Gold}}$**: $\Delta_{jk}^{\mathrm{Gold}}(\mathbf{u}^*) := |\lambda_{jk}^{\mathrm{Gold},+} - \lambda_{jk}^{\mathrm{Gold},-}|$ where $\lambda_{jk}^{\mathrm{Gold},\pm}$ are the two smallest-absolute-value (Goldstone-pair) eigenvalues of $\tilde H_{jk}|_{V^{\mathrm{Gold}}_{jk}}$.

**(W4.1b) Mixing angle $\theta_{jk}^{\mathrm{mix}}$**: Let $v_+, v_-$ be the eigenvectors of $\lambda_{jk}^{\mathrm{Gold},\pm}$. Decompose $v_+ = \alpha_j e_j^{\mathrm{trans}} + \alpha_k e_k^{\mathrm{trans}}$ where $e_j^{\mathrm{trans}}, e_k^{\mathrm{trans}}$ are per-formation unperturbed Goldstone modes. Then $\theta_{jk}^{\mathrm{mix}} := \arctan(\alpha_k / \alpha_j) \in [-\pi/2, \pi/2]$.

(For multiple Goldstones per formation, $g_j > 1$: extend to a multi-component mixing tuple, one per Goldstone-direction pair.)

**(W4.1c) Trend sign $s_{jk}^{\mathrm{trend}}$**: Along trajectory $\mathbf{u}(t)$, $s_{jk}^{\mathrm{trend}}(\mathbf{u}^*) := \mathrm{sign}\big(\frac{d \Delta_{jk}^{\mathrm{Gold}}}{dt}\big|_{t = t^*}\big) \in \{-1, 0, +1\}$.

### §4.2 Static vs dynamic data

- (W4.1a), (W4.1b): **static** — defined for any $\mathbf{u}^* \in S^\circ_{K_{\mathrm{act}}}$ at a fixed time.
- (W4.1c): **dynamic** — requires trajectory $\mathbf{u}(t)$. For static σ_rich, $s_{jk}^{\mathrm{trend}}$ is undefined; only $(\Delta_{jk}^{\mathrm{Gold}}, \theta_{jk}^{\mathrm{mix}})$ used.

For Phase 1 numerical pipeline (per `sigma_rich_VR_phase1.md`): $s_{jk}^{\mathrm{trend}}$ extracted from finite-difference of $\Delta_{jk}^{\mathrm{Gold}}(t_i)$ across consecutive sample times.

---

## §5. Well-Definedness

### §5.1 Goldstone subspace identification

**Lemma 5.1.** $V_{jk}^{\mathrm{Gold}}(\mathbf{u}^*)$ is well-defined as the kernel of $\mathrm{block-diag}(H_{jj}, H_{kk})$ restricted to translation modes (or near-zero subspace in finite-graph regime).

**Proof**: $H_{jj}$ has Goldstone eigenvectors at eigenvalue 0 by canonical T-V5b-T (translation invariance). For finite torus, "near-zero" replaces zero; subspace identified by lowest-$g_j$ eigenvalues. ✓

### §5.2 Eigenvalue continuity

**Lemma 5.2.** $\Delta_{jk}^{\mathrm{Gold}}$ is continuous in $\mathbf{u}^*$ on smooth segments where $V_{jk}^{\mathrm{Gold}}$ has constant dimension.

**Proof**: Eigenvalues of restricted $\tilde H_{jk}|_{V^{\mathrm{Gold}}}$ vary continuously by Weyl perturbation. Gap is continuous. ✓

### §5.3 Mixing angle continuity

**Lemma 5.3.** $\theta_{jk}^{\mathrm{mix}}$ is continuous away from eigenvalue degeneracies $\Delta_{jk}^{\mathrm{Gold}} = 0$ (true crossings).

**Proof**: Eigenvectors of simple eigenvalues are smooth functions of matrix entries (Kato-Rellich). At true crossing $\Delta = 0$, eigenvectors are non-unique; mixing angle undefined. By Wigner-von Neumann Theorem 3.1, true crossings are codim-2 ⇒ generic 1-param families avoid them ⇒ $\theta_{jk}^{\mathrm{mix}}$ is continuous on generic trajectories. ✓

### §5.4 Trend sign well-definedness

**Lemma 5.4.** $s_{jk}^{\mathrm{trend}}$ is well-defined when $d\Delta_{jk}^{\mathrm{Gold}}/dt \neq 0$ at $t^*$.

**Pathological case**: at the *minimum-gap* point of an avoided crossing, $d\Delta/dt = 0$ ⇒ $s = 0$. This is a measure-zero set on smooth segments; numerically, $s$ flips sign through this point (negative → 0 → positive, or vice versa).

For Phase 1 pipeline: report $s$ as $\{-1, 0, +1\}$; the $0$ case is a marker for the avoided-crossing minimum.

---

## §6. Aut(G) Invariance

### §6.1 Hessian covariance

**Lemma 6.1.** Under $\sigma \in \mathrm{Aut}(G)$ (acting on $\mathbf{u}$ per Task #1 §5.1), the Hessian transforms as:
$$H_{ab}(\sigma \mathbf{u}) = U(\sigma) H_{ab}(\mathbf{u}) U(\sigma)^{-1}$$
where $U(\sigma)$ is the permutation operator on $\mathbb{R}^X$ corresponding to $\sigma$.

**Proof**: $\mathcal{E}_K$ is $\mathrm{Aut}(G) \wr S_K$-invariant; Hessian transforms by conjugation. ✓

### §6.2 Cross-block sub-Hessian covariance

**Theorem 6.2 ($\tilde H_{jk}$ covariance).** $\tilde H_{jk}(\sigma \mathbf{u}) = (U(\sigma) \oplus U(\sigma)) \cdot \tilde H_{jk}(\mathbf{u}) \cdot (U(\sigma) \oplus U(\sigma))^{-1}$.

**Proof**: by Lemma 6.1 applied to each block. ✓

### §6.3 Eigenvalue invariance

**Corollary 6.3.** Eigenvalues of $\tilde H_{jk}$ are $\mathrm{Aut}(G)$-invariant; in particular, $\Delta_{jk}^{\mathrm{Gold}}$ is $\mathrm{Aut}(G)$-invariant.

**Proof**: orthogonal conjugation preserves spectrum. ✓

### §6.4 $S_{K_{\mathrm{act}}}$ invariance

**Lemma 6.4.** Pair $(j, k)$ is permuted by $S_{K_{\mathrm{act}}}$; the multi-set $\{W_{jk}\}_{j<k}$ is $S_{K_{\mathrm{act}}}$-invariant.

**Proof**: $\pi \in S_{K_{\mathrm{act}}}$ permutes pair indices; $\{W_{\pi(j) \pi(k)}\}_{\pi(j) < \pi(k)} = \{W_{jk}\}_{j < k}$ as multi-sets (after re-labeling). ✓

### §6.5 Combined wreath-product invariance

**Theorem 6.5.** Multi-set $\{W_{jk}\}$ is $\mathrm{Aut}(G) \wr S_{K_{\mathrm{act}}}$-invariant (at the eigenvalue-tuple component level; mixing angle is invariant up to discrete representation choices).

**Proof**: 6.3 + 6.4 combine. ✓

### §6.6 Mixing angle subtlety

$\theta_{jk}^{\mathrm{mix}}$ depends on the *choice of basis* for per-formation Goldstone subspaces ($e_j^{\mathrm{trans}}$ vs alternative bases). Aut(G) covariance of basis introduces a well-defined transformation rule:
$$\theta_{jk}^{\mathrm{mix}}(\sigma \mathbf{u}) = R(\sigma) \cdot \theta_{jk}^{\mathrm{mix}}(\mathbf{u})$$
where $R(\sigma)$ is the induced action on the Goldstone-pair subspace (sub-rotation).

**For invariance**: report $\theta_{jk}^{\mathrm{mix}}$ as the angle of mixing relative to a canonical basis (e.g., principal axes of the merger-axis-defined coordinate system). With canonical-basis convention, $\theta_{jk}^{\mathrm{mix}}$ is Aut(G)-equivariant; its absolute value or eigenvector-projector representation is invariant.

**Phase 1 default**: report mixing-angle projector $P_+ := v_+ v_+^T \otimes v_+ v_+^T$ on Goldstone-pair tensor space (eliminates sign ambiguity).

---

## §7. CN10 Derived Diagnostic Status

### §7.1 $u_t$-functional position

**Proposition 7.1.** $W_{jk}(\mathbf{u})$ is a derived diagnostic of primitive $u_t$ field via Hessian-spectral computation.

**Justification**:
- $H_{ab}$ is the second variation of $\mathcal{E}_K$ at $\mathbf{u}$ — derived from energy functional + state $\mathbf{u}$.
- $\mathcal{E}_K$ is canonical 4-energy (per CN5) + bilinear λ_rep coupling.
- Hessian eigenvalues are spectral data of derived quantity; CN10 contrastive (no new primitive).

### §7.2 Goldstone-pair existence requires translation invariance

$V^{\mathrm{Gold}}_{jk}$ is non-trivial only for translation-invariant graphs (e.g., $T^2_L$, $\mathbb{Z}^d$ subsets at sub-lattice scales). For non-translation-invariant graphs (e.g., random graphs), Goldstone modes are absent or modified; $W_{jk}$ extends to "lowest-eigenvalue-pair" gap without Goldstone interpretation.

**Phase 1 default**: $W_{jk}$ defined only for graphs with non-trivial $\mathrm{Aut}(G)$ acting transitively (translation Goldstones exist).

### §7.3 Compatibility with Commitment 14

Commitment 14 σ-tuple's eigenvalue $\lambda_k$ is the $k$-th eigenvalue of single-formation Hessian. $W_{jk}$ extends to *cross-block* Goldstone-pair eigenvalues — same Hessian-spectral category, different block.

⇒ no conflict.

---

## §8. Connection to Φ_rich (Wigner-Projection at Merger)

### §8.1 Pre-merger to post-merger Hessian relation

At K-jump time $t^*$ with $(j, k) \to \ell$ merger:
- Pre-merger: $\tilde H_{jk}(t^{*-})$ has Goldstone-pair $\lambda_{jk}^{\mathrm{Gold},\pm}(t^{*-})$ approaching crossing; mixing angle $\theta_{jk}^{\mathrm{mix}}(t^{*-})$ defined.
- Post-merger: $H_{\ell\ell}(t^{*+})$ has Goldstones of merged formation $\ell$ — translation modes of $u^{(\ell)}$ which are linear combinations of pre-merger $u^{(j)}, u^{(k)}$ Goldstones.

### §8.2 Wigner-projection claim

**Conjecture 8.1 (Wigner-projection)**. Post-merger Hessian eigenvalues of the merged-formation's Goldstone subspace are determined by:
- Pre-merger Goldstone-pair eigenvalues $\lambda_{jk}^{\mathrm{Gold},\pm}(t^{*-})$.
- Pre-merger mixing angle $\theta_{jk}^{\mathrm{mix}}(t^{*-})$.
- Post-merger total mass $m_\ell = m_j + m_k$.

Specifically: at the merger limit $\Delta_{jk}^{\mathrm{Gold}} \to 0$, the upper Goldstone $\lambda_{jk}^{\mathrm{Gold},+}$ becomes the *internal vibration mode* of the merged formation (zero in symmetric merger); the lower $\lambda_{jk}^{\mathrm{Gold},-}$ remains as the post-merger translation Goldstone (still zero on translation-invariant graph).

**Cat status**: **Cat B sketch** at this file's level. Cat A everywhere requires explicit projection-formula proof — an open item for W9+ (R2 of `sigma_rich_augmentation.md` §10.4).

### §8.3 Numerical anchor target

For NQ-242c-Rich verification (per `nq242c_explicit_construction.md` §6 Step 6):
- Compute $W_{jk}(t^{*-})$ for both A, B configurations.
- Apply Wigner-projection (Conjecture 8.1) to predict post-merger Goldstone spectrum.
- Compare to numerical $H_{\ell\ell}(t^{*+})$ Goldstone spectrum.
- Agreement (within tolerance) ⇒ Conjecture 8.1 numerically supported for the constructed example ⇒ Cat B target reached.

---

## §9. Smoothness and Approach to Merger

### §9.1 Smooth-segment regularity

By Lemma 5.2, 5.3: $W_{jk}(t)$ is continuous on smooth segments where $V_{jk}^{\mathrm{Gold}}$ has constant dimension and no true Goldstone-pair crossing occurs.

### §9.2 Approach to merger

As $d_{\min}(j, k)(t) \searrow 0$:
- $H_{jk}|_{V^{\mathrm{Gold}}}$: coupling element $\lambda_{\mathrm{rep}} \cdot O_{\mathrm{Gold}}(d_{\min})$ grows from exp-small to $O(\lambda_{\mathrm{rep}})$.
- $\Delta_{jk}^{\mathrm{Gold}}(t)$ first widens (avoided-crossing onset), reaches maximum at $\tau_0 > 0$, then either:
  - (Case A) Symmetric merger: closes back to 0 at $t^*$ (true crossing at merger).
  - (Case B) Asymmetric merger: avoided crossing only, gap stays positive but decreases post-$\tau_0$.

In both cases, $s_{jk}^{\mathrm{trend}}$ flips sign at $\tau_0$ (the avoided-crossing onset).

### §9.3 Generic 1-parameter trajectories

By Wigner-von Neumann genericity: most SCC trajectories produce avoided crossings (Case B), not true crossings. Symmetric special configurations (e.g., $D_3$ equilateral configuration A in `nq242c_explicit_construction.md` §2.2) produce true crossings; these are codim-≥1 in configuration space.

---

## §10. Cat Status

### §10.1 Cat A established

- Lemma 2.1 (cross-block Hessian symmetry/reality): **Cat A**.
- Theorem 3.1 (Wigner-von Neumann avoided-crossing, classical reference): **Cat A** by citation (Reed-Simon IV §XIII.5).
- Lemmas 5.1-5.4 (well-definedness of $W_{jk}$ components): **Cat A** under generic-trajectory assumptions.
- Lemma 6.1, Theorem 6.2 (Hessian and sub-Hessian Aut-covariance): **Cat A**.
- Corollary 6.3 (eigenvalue invariance): **Cat A**.
- Lemma 6.4 ($S_{K_{\mathrm{act}}}$ invariance): **Cat A**.
- Theorem 6.5 (combined wreath-product invariance for eigenvalue-tuple): **Cat A**.

### §10.2 Cat B / pending

- §3.3 Goldstone-pair gap formula $O(\lambda_{\mathrm{rep}} \exp(-c_0 d_{\min}))$: **Cat A under Coupling Bound Lemma**; sketch level for explicit constants.
- §6.6 mixing-angle Aut-covariance with canonical basis convention: **Cat B** (explicit basis convention pending).
- Conjecture 8.1 (Wigner-projection eigenvalue collapse): **Cat B sketch**; Cat A requires explicit projection formula proof. Open W9+.

### §10.3 Promotion target

This file's Cat A results provide the **Wigner-data sub-piece** for σ_rich Cat A everywhere path:
- Static $W_{jk}$ Aut-invariance: Cat A ✓ (this file).
- Dynamic $s^{\mathrm{trend}}$ trajectory-dependence: Cat A ✓ under generic-trajectory assumption.
- (R2) Wigner-projection at merger: Cat B sketch (Conjecture 8.1) → Cat A target Task #4 + W9+.

Combined with Tasks #1 (centroid) + #2 (orientation) + this file (Wigner-data): **all three σ_rich extension components Cat A established at static level**. Task #4 (Φ_rich determinism proof) synthesizes these into the Cat A target.

---

## §11. Hard Constraint Verification

- [x] **canonical 직접 수정 0** — `working/MF/` only.
- [x] **Silent resolution 0** — Conjecture 8.1 explicitly Cat B sketch (§8.2); §10.2 pending items registered.
- [x] **No Research OS resurrection** — single-topic.
- [x] **Not reductive** — Wigner-von Neumann is standard mathematical object (1929 theorem); avoided crossings are spectral perturbation theory; CN10 contrastive (§7.1).
- [x] **u_t primitive maintained** — Hessian computed from $\mathcal{E}_K(\mathbf{u})$; derived from primitive (§7.1).
- [x] **CN5 4-energy not merged** — $\mathcal{E}_K$ structure preserved; Hessian is second variation of canonical energy.
- [x] **K not dual-treated** — pair $(j, k)$ labels active formations integer-indexed.
- [x] **No metastability claim without P-F flag** — N/A; static σ-extraction.
- [x] **Goldstone-pair formula scope** — restricted to translation-invariant graphs (§7.2); non-translation-invariant graphs flagged as out-of-scope.

---

## §12. References

### §12.1 Working files

- `working/MF/sigma_rich_augmentation.md` §2.3.3 ($W_{jk}$ informal definition).
- `working/MF/multi_formation_sigma.md` §5.5 (cross-formation Goldstone-pair Observation 5.4).
- `working/MF/sigma_rich_centroid_derivation.md` (Task #1).
- `working/MF/sigma_rich_orientation_derivation.md` (Task #2).
- `working/MF/nq242c_explicit_construction.md` §6 (Wigner-projection numerical anchor target).
- `working/MF/sigma_rich_VR_phase1.md` (Phase 1 numerical pipeline).

### §12.2 Canonical refs

- `canonical/canonical.md` §11.1 Commitment 14, 14-Multi.
- `canonical/canonical.md` §13 T-Persist-K-Sep (Coupling Bound Lemma); T-V5b-T (translation Goldstone).
- `canonical/canonical.md` §14 CN10.

### §12.3 External refs

- Wigner, E. P. & von Neumann, J. (1929). "Über das Verhalten von Eigenwerten bei adiabatischen Prozessen". *Physikalische Zeitschrift* 30, 467–470. — avoided-crossing theorem (Theorem 3.1).
- Reed, M. & Simon, B. (1978). *Methods of Modern Mathematical Physics IV: Analysis of Operators*. Academic Press. §XIII.5 — modern formulation of Wigner-von Neumann.
- Kato, T. (1976). *Perturbation Theory for Linear Operators*. Springer. — Kato-Rellich (Lemmas 5.2, 5.3).
- Stewart-Sun (1990). *Matrix Perturbation Theory*. — Weyl perturbation.

---

**End of sigma_rich_wigner_derivation.md.**

**Status: working draft. Task #3 complete. Wigner-von Neumann $W_{jk}$ formal derivation: cross-block 2×2 sub-Hessian symmetry/reality (Cat A, Lemma 2.1), Wigner-von Neumann avoided-crossing theorem application (Cat A by classical reference, Theorem 3.1), Goldstone-pair gap formula (Cat A under Coupling Bound Lemma, §3.3), $W_{jk}$ definition (formal §4.1), well-definedness of components (Cat A on generic trajectories, Lemmas 5.1-5.4), Aut(G) invariance via Hessian conjugation (Cat A, Theorem 6.2 + Corollary 6.3), combined wreath-product invariance for eigenvalue-tuple (Cat A, Theorem 6.5), CN10 derived diagnostic status (§7.1), Wigner-projection conjecture for merger (Cat B sketch, Conjecture 8.1 open W9+). All hard constraints verified. Promotion: Wigner-data static Aut-invariance Cat A established; Task #4 Φ_rich determinism synthesis next.**

**File:** `/Users/ojaehong/Perception/Perception_theory/THEORY/working/MF/sigma_rich_wigner_derivation.md`
**Created:** 2026-04-30 (W5 Day 4).
**Promotion target:** CV-1.7 W9+ Cat A everywhere proof completion (combined with Tasks #1, #2, #4); R2 (Wigner-projection rigorous proof) is the remaining Cat A blocker.
