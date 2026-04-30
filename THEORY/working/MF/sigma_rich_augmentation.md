# sigma_rich_augmentation.md — OP-0008 Path B: Rich-σ Augmentation for Deterministic K-jump Inheritance

**Status:** working draft (W5 Day 4 OAT-supplementary; OP-0008 Path B candidate proposal; CV-1.6 candidate, NOT promoted).
**Created:** 2026-04-30 (W5 Day 4).
**Type:** Direct attack on OP-0008 σ^A K-jump Inheritance Non-Determinism via Path B (rich-σ augmentation).
**Author origin:** OP-0008 registration `THEORY/canonical/open_problems.md` (CV-1.5.1) + Path A/B bifurcation per OP-0008 Impact section + 4-tool mathematical scaffolding `working/MF/mathematical_scaffolding_4tools.md` Tool A3 PH framing.
**Canonical refs:** §11.1 Commitment 14 (single-formation σ); §11.1 Commitment 14-Multi (D-6a static σ_multi^A + σ_multi^D, CV-1.5.1); §13 T-σ-multi-A-Static, T-σ-Multi-1; §11.1 Commitment 16 (K_field/K_act); §14 CN5, CN10; §15 OP-0008.
**Working refs:** `working/MF/sigma_multi_trajectory.md` (D-6b dynamic, Lemma 4.4.1(c) Cat C); `working/MF/multi_formation_sigma.md` (D-6a static, Approach A primary); `working/MF/mathematical_scaffolding_4tools.md` §4 Tool A3 (Persistent Homology).
**Open problems referenced:** OP-0008 (direct attack); OP-0009-A (architecture, related); OP-0009-Pre (pre-objective vs labels, related).

---

## §1. Mission

> **"OP-0008 σ^A K-jump 비결정성을 Path B (rich-σ augmentation) 로 직접 공격: σ_rich = σ^standard + (centroids, orientations, Wigner–von Neumann avoided-crossing data) 를 정의하고, 이 augmented invariant 위에서 K-jump 상속 사상 Φ_rich 가 *deterministic* 하다는 candidate construction 을 제시한다. NQ-242c+d explicit Cat A 구성 + CV-1.6 release path 권고."**

OP-0008 는 CV-1.5.1 시점 σ^A 인 K-jump 시 inheritance map $\Phi : \sigma^A(t^{*-}) \to \sigma^A(t^{*+})$ 가 pre-merger σ^A 만으로 결정되지 않으며, **merger-geometry data $\mathcal{M}$** (which two formations $j,k$ merge; cluster centroids; post-merger relaxation trajectory; orientation alignment) 를 추가로 요구함을 conjectured (Cat C, severity 🟠 HIGH). CV-1.6 release path 두 갈래:

- **Path A** (accept non-determinism): D-6b Cat B target with explicit non-deterministic K-jump map. σ_standard 유지.
- **Path B** (rich-σ augmentation): σ_tuple 을 centroid + orientation + Wigner–von Neumann data 로 확장. Cat A target 회복 가능.

이 working file 은 **Path B 의 mathematical content 를 first 정식화** 하고, NQ-242c (explicit two-trajectory counterexample distinguishing σ_standard from σ_rich) + NQ-242d (σ^D symmetry-emergence) 의 Cat A construction 을 candidate level 로 제안한다.

**핵심 결론**:
1. σ_rich 가 잘 정의되며 (§2), 모든 정보 component 가 derived diagnostic (CN10 contrastive 보존).
2. Φ_rich 가 K-jump 시 deterministic 후보 map (§3) — Path B Cat A target 도달 가능.
3. NQ-242c explicit construction 이 PH literature 의 표준 counterexample 패턴과 일치 (§6).
4. Path B 가 Path A 보다 **권고됨** — Cat A 보존 + standard PH/centroid framework 정합성 (§5).
5. CV-1.6 candidate Commitment 14-Multi (D) addendum 으로 propose, NOT promoted (§9).

---

## §2. σ_rich Definition

### §2.1 Underlying setup

K-field gradient flow trajectory $\mathbf{u}(t) : [0, T] \to \widetilde\Sigma^K_M$ on shared-pool stratified space (per `working/MF/mathematical_scaffolding_4tools.md` Tool A1 §2). Active formation set at time $t$: $\mathrm{act}(t) = \{j : \|u^{(j)}(t)\|_1 > \epsilon\}$. $K_{\mathrm{act}}(t) = |\mathrm{act}(t)|$.

For each $j \in \mathrm{act}(t)$, the formation $u^{(j)}(t) : X \to [0, 1]$ has support $\mathrm{supp}(u^{(j)}) := \{x \in X : u^{(j)}(x) > \delta\}$ (with $\delta < \epsilon$ a small threshold).

### §2.2 σ_standard recap

The canonical Commitment 14-Multi static σ-tuple (D-6a CV-1.5.1):
$$\sigma_{\mathrm{multi}}^{A,\mathrm{standard}}(\mathbf{u}) := \big( \mathcal{F}_{\mathrm{total}}; \{\sigma_j\}_{j \in \mathrm{act}}; \{\sigma_{jk}\}_{j<k} \big),$$
where $\sigma_j = (n_j^{(p)}, [\rho_j^{(p)}], \lambda_j^{(p)})_p$ (per-formation Hessian eigenvalue / irrep / nodal triples) and $\sigma_{jk}$ is the cross-block tuple (per `multi_formation_sigma.md` §5.1(b)).

This is the σ^A whose K-jump inheritance is non-deterministic (OP-0008 Lemma 4.4.1(c)).

### §2.3 Rich-σ definition

**Definition 2.1 (σ_rich).** For $\mathbf{u} \in \widetilde\Sigma^K_M$ in the interior of stratum $S_{K_{\mathrm{act}}}$ (per Tool A1):
$$
\boxed{\;\sigma_{\mathrm{rich}}(\mathbf{u}) := \big(\sigma_{\mathrm{multi}}^{A,\mathrm{standard}}(\mathbf{u});\ \{c_j(\mathbf{u})\}_{j \in \mathrm{act}};\ \{\Theta_j(\mathbf{u})\}_{j \in \mathrm{act}};\ \{W_{jk}(\mathbf{u})\}_{j<k}\big)\;}
$$
with the four extension components defined as follows.

#### §2.3.1 Centroid $c_j$

For each $j \in \mathrm{act}(\mathbf{u})$:
$$c_j(\mathbf{u}) := \frac{\sum_{x \in X} x \cdot u^{(j)}(x)}{\sum_{x \in X} u^{(j)}(x)} \quad \in \mathbb{R}^{\dim X}$$
(treating $X \subseteq \mathbb{R}^{\dim X}$ for embedded graphs; for abstract graphs use vertex-position embedding from $G$'s ambient geometry). The denominator $\|u^{(j)}\|_1 > \epsilon$ for active formations, so $c_j$ is well-defined.

**Status as derived diagnostic**: $c_j$ is a $u$-weighted spatial average — derived from primitive $u_t$ field, not a new primitive. Compatible with CN10 (preserves u_t primacy).

**Cross-ref**: identical to centroid used in Tool A3 PH §4 of `mathematical_scaffolding_4tools.md`.

#### §2.3.2 Orientation $\Theta_j$

For each $j \in \mathrm{act}(\mathbf{u})$, define the **inertia tensor** of formation $j$:
$$M_j(\mathbf{u}) := \sum_{x \in X} u^{(j)}(x) \, (x - c_j)(x - c_j)^T \quad \in \mathbb{R}^{\dim X \times \dim X}.$$

$M_j$ is a real symmetric positive-semidefinite matrix. Diagonalize $M_j = \sum_{\alpha} \mu_{j,\alpha} v_{j,\alpha} v_{j,\alpha}^T$ with $\mu_{j,1} \geq \mu_{j,2} \geq \cdots$.

**Definition (orientation)**: $\Theta_j(\mathbf{u}) := (\mu_{j,\alpha}, [v_{j,\alpha}])_\alpha$ where $[v_{j,\alpha}]$ denotes the principal-axis eigenvector modulo $\pm 1$ (RP^{dim X-1} representative; sign-ambiguity resolved by canonical convention, e.g., first non-zero coordinate $> 0$).

For 2D ($\dim X = 2$): $\Theta_j = ((\mu_{j,1}, \mu_{j,2}), \theta_j)$ where $\theta_j \in [0, \pi)$ is the angle of the principal axis from a fixed reference. **Orientation alignment** between formations $j, k$ is captured by $|\theta_j - \theta_k| \mod \pi$.

**Status as derived diagnostic**: $\Theta_j$ is the spectral data of the second-moment tensor of $u^{(j)}$ — derived from primitive field. Matches the "orientation alignment" merger-geometry component $\mathcal{M}$ identified in OP-0008.

#### §2.3.3 Wigner–von Neumann avoided-crossing data $W_{jk}$

The Wigner–von Neumann theorem (1929; cf. Reed-Simon IV §XIII.5) states that, for symmetric real matrices depending on a single real parameter, eigenvalue crossings are codim-2 generic; for **paired Goldstone modes** of two formations approaching merger, the pair of near-zero eigenvalues of $\tilde H_{jk}$ undergoes an **avoided crossing** as the inter-formation distance $d_{\min}(j,k) \searrow 0$.

For each pair $j < k$ with $j, k \in \mathrm{act}(\mathbf{u})$, define:

$$W_{jk}(\mathbf{u}) := \big(\Delta_{jk}^{\mathrm{Gold}}, \theta_{jk}^{\mathrm{mix}}, \mathrm{sign}(d/dt[\Delta_{jk}^{\mathrm{Gold}}])\big)$$

where:
- **$\Delta_{jk}^{\mathrm{Gold}}$**: gap between the two near-zero (Goldstone-pair) eigenvalues of the cross-block 2×2 sub-Hessian $\tilde H_{jk} = \begin{pmatrix} H_{jj} & H_{jk} \\ H_{kj} & H_{kk} \end{pmatrix}$. By `multi_formation_sigma.md` §5.5 (Observation 5.4): $\Delta_{jk}^{\mathrm{Gold}} = O(\|H_{jk}\|_{\mathrm{op}}) = O(\lambda_{\mathrm{rep}} \cdot \exp(-c_0 d_{\min}))$ in the well-separated regime.
- **$\theta_{jk}^{\mathrm{mix}}$**: mixing angle of the two Goldstone-pair eigenvectors — the linear combination coefficient $\alpha$ in $v_{\mathrm{Gold},+} = \alpha \, e_j^{\mathrm{trans}} + \sqrt{1-\alpha^2} \, e_k^{\mathrm{trans}}$ (each $e_j^{\mathrm{trans}}$ being the per-formation translation Goldstone). $\theta_{jk}^{\mathrm{mix}} = \arctan(\alpha / \sqrt{1-\alpha^2}) \in [-\pi/2, \pi/2]$.
- **$\mathrm{sign}(d/dt[\Delta_{jk}^{\mathrm{Gold}}])$**: temporal sign of the Goldstone-pair gap derivative. As $j, k$ approach merger ($d_{\min}(j,k) \searrow 0$), $\Delta_{jk}^{\mathrm{Gold}}$ first widens (avoided crossing onset), then contracts (one mode goes to true zero post-merger as $j \oplus k = \ell$). Sign flips at the avoided-crossing onset, providing a *temporal* fingerprint.

**Status as derived diagnostic**: $W_{jk}$ is purely Hessian-spectral data restricted to the Goldstone-pair subspace — derived. Matches the "post-merger relaxation trajectory" component of $\mathcal{M}$ in OP-0008.

### §2.4 σ_rich is well-defined and CN10-compatible

**Claim 2.4.** Each component $\sigma_{\mathrm{multi}}^{A,\mathrm{standard}}, \{c_j\}, \{\Theta_j\}, \{W_{jk}\}$ is:
- **(W1) $u_t$-derived**: function of primitive $u^{(j)} : X \to [0,1]$ via spatial integrals or Hessian-spectral computation.
- **(W2) Aut-orbit-invariant**: under $\mathrm{Aut}(G) \wr S_{K_{\mathrm{field}}}$ action, each component transforms covariantly; multi-set treatment under $S_{K_{\mathrm{act}}}$ yields invariance.
- **(W3) Stratum-interior well-defined**: $K_{\mathrm{act}}$-stratum interior (no boundary touching, no formation coincidence) ensures denominators $\|u^{(j)}\|_1 > \epsilon$ and Goldstone-pair non-degeneracy.

(W1)+(W2)+(W3) ⇒ σ_rich is well-defined Aut-orbit invariant on stratum interiors.

**Status**: Cat B sketch (CV-1.6 candidate). Full proof of (W2) under wreath-product action requires explicit irrep treatment (per `multi_formation_sigma.md` §5.6 OQ-A1 forward gap).

---

## §3. K-jump Inheritance Map Φ_rich

### §3.1 K-jump event setup

At a K-jump time $t^*$ with $\Delta K = 1$ simple merger (formations $j$ and $k$ merge into $\ell$ at $t^{*+}$):
- Pre-merger: $\mathrm{act}(t^{*-}) = \{j, k, \ldots\}$, $K_{\mathrm{act}}(t^{*-}) = K'$.
- Post-merger: $\mathrm{act}(t^{*+}) = \{\ell, \ldots\}$ where $u^{(\ell)}(t^{*+})$ is the post-merger formation, $K_{\mathrm{act}}(t^{*+}) = K' - 1$.

Per `sigma_multi_trajectory.md` Lemma 4.2: left and right limits $\sigma^A(t^{*\pm})$ exist (Cat A under interior regime).

### §3.2 Encoding of $(j,k)$ in σ_rich

**Claim 3.1 (merger pair identification from σ_rich).** Given $\sigma_{\mathrm{rich}}(t^{*-})$, the merging pair $(j, k)$ is identifiable as the unique pair satisfying:
1. $\|c_j(t^{*-}) - c_k(t^{*-})\|$ is the unique minimum in $\{\|c_a - c_b\| : a, b \in \mathrm{act}, a < b\}$.
2. $\Delta_{jk}^{\mathrm{Gold}} \to 0$ approach (Goldstone-pair softening: of all $W_{ab}$, the pair $(j,k)$ has $W_{jk}$ with $\mathrm{sign}(d\Delta/dt) = -1$ and minimum $|\Delta_{jk}^{\mathrm{Gold}}|$).

**Verification sketch**: Two formations merge when their boundaries touch and the inter-formation barrier softens. Both centroid-distance minimum (geometric) and Goldstone-pair gap softening (spectral) characterize this softening. In the well-separated regime, both criteria identify the same pair (consistent in non-degenerate trajectories).

**Edge case**: simultaneous mergers ($\Delta K \geq 2$ at single $t^*$) — measure-zero in generic 1-parameter trajectories (codim-≥2 in $\widetilde\Sigma^K_M$); non-generic. Excluded in the simple-merger Path B target.

### §3.3 Φ_rich definition (candidate deterministic map)

**Definition 3.2 (Φ_rich).** Under simple-merger conditions (§3.2):
$$\Phi_{\mathrm{rich}} : \sigma_{\mathrm{rich}}(t^{*-}) \;\mapsto\; \sigma_{\mathrm{rich}}(t^{*+})$$
defined by the following components:

(a) **Pair identification** $(j, k) \leftarrow$ Claim 3.1.

(b) **Post-merger centroid**: $c_\ell(t^{*+}) = (m_j c_j(t^{*-}) + m_k c_k(t^{*-})) / (m_j + m_k)$ — mass-weighted centroid (instantaneous, before relaxation).

(c) **Post-merger orientation**: $M_\ell(t^{*+}) = M_j(t^{*-}) + M_k(t^{*-}) + (m_j m_k / (m_j + m_k)) \cdot (c_j - c_k)(c_j - c_k)^T$ (parallel-axis theorem application). $\Theta_\ell$ is the spectral decomposition of $M_\ell$.

(d) **Post-merger Hessian eigenvalues**: $\sigma_\ell(t^{*+})$ is recovered from $\tilde H_{jk}(t^{*-})$ post-Wigner-projection — the avoided-crossing pair $\Delta_{jk}^{\mathrm{Gold}}$ collapses to a single zero (post-merger Goldstone of the merged formation $\ell$), and the remaining eigenvalues of $\tilde H_{jk}$ project to $H_{\ell\ell}(t^{*+})$ via the Wigner–von Neumann mixing $\theta_{jk}^{\mathrm{mix}}$.

(e) **Post-merger Wigner-data $\{W_{\ell m}\}$**: derived from the post-merger Hessian via standard cross-block construction.

(f) **Other formations** ($a \neq j, k$): $\sigma_a, c_a, \Theta_a$ unchanged at $t^{*+}$ (instantaneous limit; relaxation is a separate W6+ refinement).

### §3.4 Φ_rich determinism claim

**Claim 3.3 (Path B Cat A target).** Φ_rich as defined in §3.3 is **deterministic** in σ_rich(t^{*-}) alone — no merger-geometry data $\mathcal{M}$ is needed beyond what σ_rich already encodes.

**Verification**: $\mathcal{M}$ in OP-0008 = (which two formations merge; cluster centroids; relaxation trajectory; orientation alignment) is *fully encoded* in σ_rich:
- "Which two formations merge" → §3.2 Claim 3.1 from $\{c_a\}, \{W_{ab}\}$.
- "Cluster centroids" → $\{c_j\}$ component of σ_rich directly.
- "Relaxation trajectory" → encoded in $\{W_{jk}\}$ via $\mathrm{sign}(d\Delta/dt)$ + $\theta_{jk}^{\mathrm{mix}}$.
- "Orientation alignment" → $\{\Theta_j\}$ component.

Therefore $\Phi_{\mathrm{rich}} : \sigma_{\mathrm{rich}}(t^{*-}) \to \sigma_{\mathrm{rich}}(t^{*+})$ is well-defined as a function (single-valued).

**Cat status**: Cat B target (sketched). Cat A requires:
- §6 NQ-242c explicit construction confirming uniqueness.
- Rigorous proof of §3.3(d) Wigner-projection eigenvalue collapse (current sketch level).

---

## §4. Comparison with σ_standard Non-Determinism

### §4.1 σ_standard 비결정성 explicit example

**Construction 4.1 (two trajectories with same σ_standard but distinct σ_rich).**

Setup: 2D torus $T^2_{20}$, $K_{\mathrm{field}} = 4$, $K_{\mathrm{act}}(t = 0) = 3$, $\beta = 4.0$, $\lambda_{\mathrm{rep}} = 0.1$.

Initial configurations:
- **Trajectory A**: three tanh-disk formations at positions $(5, 5), (15, 5), (10, 15)$ with identical radii $r = 3$. Triangular arrangement.
- **Trajectory B**: three tanh-disk formations at positions $(5, 5), (15, 5), (10, 12)$ with identical radii $r = 3$. *Slightly* compressed triangle (vertical compression).

Both have:
- Same per-formation σ_j (identical disks ⇒ identical $H_{jj}$ spectrum ⇒ identical Commitment 14 σ).
- Same $\mathcal{F}_{\mathrm{total}} = 3$.
- Same multi-set $\{\sigma_{jk}\}$ structure *up to op-norm scaling* — but if we only retain the σ-tuple eigenvalue/irrep/nodal triples without quantitative coupling-strength labels, the multi-sets coincide. ⇒ **Same σ_standard**.

But:
- Trajectory A: centroids $c_1, c_2, c_3$ form an equilateral triangle (side 10).
- Trajectory B: centroids form an isoceles triangle (base 10, height 7).

Under gradient flow, Trajectory A: triple-symmetric merger (or single nearest-pair merger by symmetry-breaking noise) — multiple possible outcomes. Trajectory B: clear nearest-pair (top vertex with one base vertex) merger first.

**At first K-jump time $t^*$**:
- Trajectory A *might* merge (1, 2) with σ^A(t^{*+}) eigenvalue spectrum $\Lambda_A$.
- Trajectory B *will* merge (1, 3) (closest pair) with σ^A(t^{*+}) eigenvalue spectrum $\Lambda_B$.

**$\Lambda_A \neq \Lambda_B$** because the merging pair geometry differs (A: horizontal merger; B: diagonal merger), and the resulting merged-formation Hessian spectrum differs accordingly.

So: **same σ_standard(t^{*-}) → distinct σ_standard(t^{*+})**. This is OP-0008's non-determinism, made explicit.

### §4.2 σ_rich 결정성 same example

For the same Trajectories A, B above:
- $\sigma_{\mathrm{rich}}^A(t^{*-})$ encodes centroids $c_1^A = (5,5), c_2^A = (15,5), c_3^A = (10, 15)$ ⇒ pair distances $(10, \sqrt{125}, \sqrt{125})$.
- $\sigma_{\mathrm{rich}}^B(t^{*-})$ encodes centroids $c_1^B = (5,5), c_2^B = (15,5), c_3^B = (10, 12)$ ⇒ pair distances $(10, \sqrt{74}, \sqrt{74})$.

**$\sigma_{\mathrm{rich}}^A(t^{*-}) \neq \sigma_{\mathrm{rich}}^B(t^{*-})$** (different centroid configurations). Hence $\Phi_{\mathrm{rich}}$ distinguishes them at the input level, and the deterministic claim is consistent.

**Critical observation**: σ_rich's centroid component is the single ingredient that lifts the σ_standard degeneracy. Orientation $\Theta_j$ and Wigner-data $W_{jk}$ provide *finer* discriminations (e.g., for non-disk formations with anisotropy, or Goldstone-mixing-sensitive mergers); but the centroid alone suffices for the §4.1 example.

### §4.3 Why σ_standard misses this

σ_standard is *intrinsic* (per-formation Hessian spectrum is invariant under rigid translation of the formation in $X$). Centroid information is *extrinsic* (depends on absolute position in $X$). The non-determinism of $\Phi$ arises because the *spatial arrangement* (centroid configuration) of the K formations is needed to predict which pair merges first, and σ_standard doesn't carry this data.

σ_rich = σ_standard + extrinsic geometric data ⇒ recovers determinism.

---

## §5. Path B vs Path A — Recommendation

### §5.1 Path A: accept non-determinism (Cat B target)

**Description**: Keep σ_standard; register K-jump map $\Phi^{\mathrm{standard}}$ as **non-deterministic** (multi-valued, depends on $\mathcal{M}$). Canonical Commitment 14-Multi (D) at CV-1.6 with explicit caveat:
> $\sigma_{\mathrm{multi}}^A(t)$ is càdlàg with deterministic smooth-segment continuation; at K-jump events $t^*$, $\sigma^A(t^{*+})$ is determined by $\sigma^A(t^{*-}) \cup \mathcal{M}$ where $\mathcal{M}$ is auxiliary merger-geometry data.

**Pros**:
- Minimal canonical commitment expansion (σ_standard unchanged).
- $\mathcal{M}$ as auxiliary data is honest about the gap.
- Compatible with PH-only framing (Tool A3 §4.3 of `mathematical_scaffolding_4tools.md`: 0-dim PH ↛ 1-dim PH non-determinism).

**Cons**:
- Cat A target lost; D-6b dynamic σ-trajectory canonical entry pinned at Cat B.
- Phase 8 T4 SCC↔CH correspondence (`2026-04-28/32_*`) requires explicit non-determinism caveat — affects Paper §4.5.7.
- $\mathcal{M}$ remains an "auxiliary blob" without canonical structure.

### §5.2 Path B: rich-σ augmentation (Cat A target)

**Description**: Replace σ_standard with σ_rich (this file). Φ_rich deterministic candidate at Cat B; Cat A target via NQ-242c+d completion.

**Pros**:
- **Cat A target preserved** for D-6b dynamic σ_multi^A(t) at CV-1.6+.
- σ_rich components (centroid, orientation, Wigner-data) are *standard mathematical objects* — not ad hoc — with literature support: centroid in PH (Tool A3); orientation in inertia tensor analysis (mechanics/PCA); Wigner–von Neumann in spectral perturbation theory.
- Tool A3 PH framing of `mathematical_scaffolding_4tools.md` §4 *natively* uses centroid trajectories — Path B aligns σ-framework with PH scaffolding.
- $\mathcal{M}$ data is *internalized* (no longer auxiliary).

**Cons**:
- σ-tuple expansion: canonical Commitment 14 + 14-Multi text needs amendment — heavier canonical commitment.
- σ_rich Aut-invariance proof (Claim 2.4 W2) requires explicit pair-stabilizer + wreath-product treatment (currently Cat B sketch).
- §3.3(d) Wigner-projection eigenvalue collapse requires rigorous proof (currently sketch).

### §5.3 Recommendation: Path B (preferred)

**Rationale**:

1. **Cat A preservation is the main D-6b CV-1.6 success criterion**: Path A locks Cat B forever; Path B keeps Cat A on the table.
2. **σ_rich components are standard**: centroid (PH), inertia tensor (mechanics), Wigner–von Neumann (spectral perturbation). No exotic mathematical content; aligns with `mathematical_scaffolding_4tools.md` Tool A3 framework already proposed for CV-1.6.
3. **Internalization of $\mathcal{M}$**: rather than registering an opaque "merger-geometry data" object, σ_rich makes each piece explicit and ontologically grounded as derived diagnostic of $u_t$ (CN10 contrastive preserved).
4. **CV-1.6 release timing compatible**: rich-σ augmentation requires §3.3 deterministic claim sketch + NQ-242c+d Cat A target by W6+ — within plausible CV-1.6 W6-W8 release window.

**Decision recommendation**: **Path B**. Path A as fallback if Path B's Cat A target cannot be reached by W8.

### §5.4 Hybrid path (intermediate)

If neither pure-A nor pure-B is feasible by CV-1.6:
- Adopt σ_rich definition (this file §2) at Cat B candidate level.
- Register Φ_rich determinism as Cat B target (sketch level, this file §3).
- Defer Cat A confirmation (NQ-242c+d explicit construction) to CV-1.7+.
- Keep CV-1.6 Path-B-candidate language flagged: σ_rich as *proposed* canonical extension, not adopted.

This is the pragmatic CV-1.6 default if W6 effort budget tight.

---

## §6. NQ-242c Explicit Construction Proposal

### §6.1 Goal

NQ-242c (per `open_problems.md` OP-0008): "explicit construction of two trajectories with same σ^A($t^{*-}$) but distinct σ^A($t^{*+}$)". Cat A target. ~2-3 weeks W6+.

Path B reframing: NQ-242c becomes **two-fold construction**:
- (NQ-242c-Standard): two trajectories with same σ_standard($t^{*-}$) but distinct σ_standard($t^{*+}$). *Confirms* σ_standard non-determinism.
- (NQ-242c-Rich): same two trajectories have *distinct* σ_rich($t^{*-}$). Φ_rich uniquely maps each to its post-merger σ_rich. *Confirms* σ_rich determinism.

Combined, NQ-242c-Standard + NQ-242c-Rich establish: σ_standard insufficient, σ_rich sufficient ⇒ Path B Cat A.

### §6.2 Construction sketch (extends §4 example)

**Step 1 (numerical setup)**: 2D torus $T^2_{20}$ as in §4.1, $K = 3$ disk formations.

**Step 2 (configuration design)**:
- Configuration A: equilateral triangle of disks (centroids $C_A$).
- Configuration B: isoceles triangle of disks (centroids $C_B \neq C_A$, but per-disk profiles identical).

Verify σ_standard(A) = σ_standard(B) (per §4.1).

**Step 3 (trajectory simulation)**: Run gradient flow from each configuration, identify first K-jump time $t^*_A, t^*_B$.

**Step 4 (post-merger σ)**: Compute σ_standard($t^{*+}_A$), σ_standard($t^{*+}_B$). Verify distinct.

**Step 5 (rich-σ verification)**: Compute σ_rich($t^{*-}_A$), σ_rich($t^{*-}_B$). Verify distinct (centroid configurations differ).

**Step 6 (Φ_rich check)**: Apply §3.3 Φ_rich definition to σ_rich($t^{*-}_A$) and σ_rich($t^{*-}_B$). Verify result matches numerically computed σ_rich($t^{*+}_A$), σ_rich($t^{*+}_B$).

### §6.3 Numerical pipeline

Computed via existing SCC infrastructure:
- `scc/multi.py`: K-field gradient flow.
- `scc/diagnostics.py` + `scc/persistence.py`: Hessian + σ-tuple extraction (already in CV-1.5).
- New script `CODE/scripts/nq242c_path_b_explicit.py`: implements §6.2 Steps 1-6.
- PH integration via GUDHI/Ripser (per `mathematical_scaffolding_4tools.md` §4.4).

**Estimated effort**: 1-2 weeks scripting + analysis (lighter than the 4-6-week original NQ-242 estimate, because Path B reuses centroid+PH pipeline already proposed for Tool A3).

### §6.4 Cat A target and release

NQ-242c-Rich numerical confirmation (§6.2 Step 6 successful) → Φ_rich determinism is Cat A for the *constructed example*. Generalization to all Path B simple-merger events is Cat B (numerical anchor + theoretical Φ_rich definition consistency). Cat A everywhere requires §3.3(d) rigorous Wigner-projection proof.

CV-1.6 candidate level: **Cat B target** with NQ-242c-Rich numerical anchor; CV-1.7+ Cat A everywhere via theoretical proof.

---

## §7. NQ-242d σ^D Symmetry-Emergence

### §7.1 Statement

NQ-242d (per `open_problems.md`): "σ^D symmetry-emergence characterization (post-merger stabilizer ⊇ pull-back image)". Cat A target. ~2-3 weeks W6+.

The post-merger stabilizer $G_{\mathbf{u}^*}^{(t^{*+})} = \mathrm{Stab}_{\mathrm{Aut}(G) \wr S_{K'-1}}(\mathbf{u}^*(t^{*+}))$ may be **strictly larger** than the pull-back image of the pre-merger stabilizer $G_{\mathbf{u}^*}^{(t^{*-})}$ under the merger quotient $S_{K'} \to S_{K'-1}$ (with merging-pair $\mathbb{Z}_2$ collapse).

### §7.2 Path B framing

In σ_rich language:
- Pre-merger σ^D component records the wreath-product stabilizer $G_{\mathbf{u}^*}^{(t^{*-})}$.
- Post-merger formation $u^{(\ell)}$ inherits a new symmetry: the merger's $\mathbb{Z}_2$ swap (between $j$ and $k$) becomes a *trivial* action on $\ell$, but the merged formation may *gain* new $\mathrm{Aut}(G)$ subgroup invariance (e.g., if $j, k$ were a horizontally-symmetric pair, the merged $\ell$ has horizontal reflection symmetry intrinsically).

**Claim 7.1 (σ^D inheritance with symmetry emergence)**:
$$G_{\mathbf{u}^*}^{(t^{*+})} \supseteq \mathrm{quot}_{j \oplus k} \big(G_{\mathbf{u}^*}^{(t^{*-})}\big) \cdot G_{\mathrm{emerge}, jk}$$
where $\mathrm{quot}_{j \oplus k}$ is the merger quotient and $G_{\mathrm{emerge}, jk}$ is the symmetry emerging from $(j,k)$-merger (depends on the geometric configuration of $u^{(j)}, u^{(k)}$).

### §7.3 Determination from σ_rich

$G_{\mathrm{emerge}, jk}$ is determined by:
- Centroid pair $(c_j, c_k)$ → merger axis line.
- Orientation pair $(\Theta_j, \Theta_k)$ → relative orientation alignment.
- Wigner-mixing $\theta_{jk}^{\mathrm{mix}}$ → which Goldstone modes survive vs are absorbed.

All three are σ_rich components ⇒ **σ^D symmetry-emergence is deterministic in σ_rich** (Cat A target).

### §7.4 Status

Claim 7.1 + §7.3 σ_rich determination: Cat B sketch. Cat A requires:
- Explicit characterization of $G_{\mathrm{emerge}, jk}$ as a function of (centroid-pair, orientation-pair, Wigner-mixing).
- Verification on NQ-242c-Rich numerical example.

NQ-242d effort estimate: 2-3 weeks W6+ (consistent with `open_problems.md` original estimate). Path B reframing reduces to characterization of $G_{\mathrm{emerge}, jk}$ from σ_rich data.

---

## §8. PH Layer (Tool A3) Connection

### §8.1 σ_rich centroid component = Tool A3 PH input

The centroid set $\{c_j(\mathbf{u})\}_{j \in \mathrm{act}}$ in σ_rich §2.3.1 is *exactly* the input to the Vietoris-Rips PH pipeline of `mathematical_scaffolding_4tools.md` §4.

Specifically:
- $H_0$ barcode of $R_r(\{c_j\})$ over $r$: cluster-level connectivity → captures K-jump events (bar-deaths at merger times).
- $H_1$ barcode: loop structure of formation arrangement (3+ formations in cyclic / triangular arrangement).

**σ_rich subsumes Tool A3 PH information**: $\{c_j\}$ + Vietoris-Rips computation = $H_*$ barcodes. Hence σ_rich is *richer* than σ_standard + PH alone — σ_rich also contains $\Theta_j$ (orientation) and $W_{jk}$ (Wigner-data) which $H_*$ barcodes do not directly capture.

### §8.2 PH non-lift fact and σ_rich determinism

Per `sigma_multi_trajectory.md` §3.7 + `mathematical_scaffolding_4tools.md` §4.3: $H_0$ barcode (K-jump sequence) does not determine $H_1$+ barcodes (within-cluster topology / σ-tuple). This is the standard PH non-lift fact.

σ_rich determinism (Φ_rich §3.3) is consistent with this: σ_rich contains *both* $H_0$-determining centroids AND $H_1$-determining geometry (full centroid configuration). The non-lift fact constrains $H_0$ → $H_1$ inference, but σ_rich provides $H_0 + H_1$ data simultaneously, escaping the non-lift constraint.

**Key insight**: σ_rich is *not* about extracting $H_1$ from $H_0$ (impossible per PH non-lift); it's about *retaining* both layers explicitly in the σ-invariant from the start.

### §8.3 NQ-242 numerical pipeline integration

Per `mathematical_scaffolding_4tools.md` §4.4 + this file §6.3:

**NQ-242 reframed Phase 1-4** (per `sigma_multi_trajectory.md` §6.1):
- **Phase 1** (W6 Days 1-3): centroid extraction + Vietoris-Rips $H_0/H_1$ computation. *Now also computes σ_rich centroid + orientation components*.
- **Phase 2** (W6 Days 4-7): zigzag persistence over K-jump events + Wigner–von Neumann data extraction at avoided crossings. *Constructs $W_{jk}$ component of σ_rich*.
- **Phase 3** (W7 Days 1-5): σ-tuple integration with PH barcodes + $\Theta_j$ + $W_{jk}$ → full σ_rich pipeline.
- **Phase 4** (W7 Day 6 – W8 Day 3): NQ-242c-Rich explicit construction (this file §6).

**Net effect**: NQ-242 pipeline = σ_rich numerical extractor for any K-field trajectory. Path B's σ_rich operationalized.

---

## §9. CV-1.6 Release Path

### §9.1 Commitment 14-Multi (D) addendum (proposed, NOT promoted)

Proposed canonical addendum at CV-1.6 (D-6b path):

```markdown
**Commitment 14-Multi (D) addendum: Rich-σ augmentation for K-jump deterministic inheritance (CV-1.6 candidate, Path B).**

For deterministic K-jump inheritance map $\Phi : \sigma(t^{*-}) \to \sigma(t^{*+})$, σ-tuple is augmented to:
$$\sigma_{\mathrm{rich}}(\mathbf{u}) := (\sigma_{\mathrm{standard}}; \{c_j\}; \{\Theta_j\}; \{W_{jk}\})$$
where:
- $c_j$ is the $u^{(j)}$-weighted centroid (Definition per `working/MF/sigma_rich_augmentation.md` §2.3.1).
- $\Theta_j$ is the principal-axis decomposition of inertia tensor $M_j = \sum_x u^{(j)}(x)(x-c_j)(x-c_j)^T$ (§2.3.2).
- $W_{jk}$ is the Wigner–von Neumann avoided-crossing data of paired Goldstone modes of $\tilde H_{jk}$ (§2.3.3).

All four components are derived diagnostics of primitive $u_t$ field (CN10 contrastive preserved).

Φ_rich (per `working/MF/sigma_rich_augmentation.md` §3.3) is the candidate deterministic K-jump map; Cat A target via NQ-242c-Rich numerical confirmation + theoretical Wigner-projection proof.

OP-0008 σ^A K-jump inheritance non-determinism: PARTIALLY RESOLVED via Path B σ_rich augmentation; Cat A everywhere pending NQ-242c+d completion.
```

**Status**: CV-1.6 candidate. NOT promoted to canonical at CV-1.5.1. Promotion requires: (a) §3.3 deterministic claim sketch upgraded to Cat B target with explicit verification; (b) NQ-242c-Rich numerical anchor (§6); (c) user approval at CV-1.6 packet.

### §9.2 Path A fallback registration

If Path B does not reach Cat B target by CV-1.6: register Path A at canonical with explicit non-deterministic K-jump map and $\mathcal{M}$ as auxiliary data (non-canonical), as per OP-0008 Path A description.

### §9.3 Hybrid intermediate

If Path B reaches partial maturity by CV-1.6: register σ_rich definition (§2) at canonical as **proposed extension** with promotion deferred to CV-1.7+ pending Cat A confirmation.

---

## §10. W6+ Priorities

### §10.1 NQ-242c+d explicit Cat A construction (W6 Days 1-7)

**Effort**: 2-3 weeks (consistent with `open_problems.md` estimate).

- **NQ-242c-Standard**: §6.2 Steps 1-4 — confirms σ_standard non-determinism. ~3-5 days numerical.
- **NQ-242c-Rich**: §6.2 Steps 5-6 — confirms σ_rich determinism. ~3-5 days numerical (reuses Step 1-4 trajectories).
- **NQ-242d**: §7 σ^D symmetry-emergence characterization. ~5-7 days theoretical + verification.

**Deliverable**: `CODE/scripts/nq242c_path_b_explicit.py` + `CODE/scripts/nq242d_sigma_D_emergence.py` + working file extension to this file with results.

### §10.2 NQ-242 PH pipeline integration (W6 Days 4 – W7 Days 5)

**Effort**: 3-4 weeks (per `sigma_multi_trajectory.md` §6.1 PH-augmented; this file §8.3).

- **Phase 1-2**: centroid + orientation + Wigner-data extraction (W6).
- **Phase 3**: σ_rich integration (W7).
- **Phase 4**: NQ-242c-Rich combined run (W7-W8).

**Deliverable**: `CODE/scc/sigma_rich.py` module + `tests/test_sigma_rich.py`.

### §10.3 Path B vs Path A decision (D-CV1.6-O5 candidate)

**Effort**: 1 week (W8 Days 1-5).

Rigorous Cat status assessment after §10.1 + §10.2 completion. CV-1.6 packet decision item:
- D-CV1.6-O5: adopt Path B σ_rich? Y/N decision.
- If Y: Commitment 14-Multi (D) addendum (§9.1).
- If N: Path A non-determinism registration.
- If hybrid: §9.3 intermediate.

**Deliverable**: D-CV1.6-O5 decision document (`THEORY/logs/daily/2026-05-XX/...`).

### §10.4 Theoretical rigor upgrades (W7-W9)

Cat A everywhere (post-CV-1.6) requires:
- σ_rich Aut-invariance proof (§2.4 W2): explicit pair-stabilizer + wreath-product treatment.
- §3.3(d) Wigner-projection eigenvalue collapse rigorous proof.
- §7.2 σ^D symmetry-emergence Cat A: full $G_{\mathrm{emerge}, jk}$ characterization.

**Effort**: 4-6 weeks W9-W12 (theoretical, post-CV-1.6 release).

---

## §11. Hard Constraint Verification

- [x] **canonical 직접 수정 0** — this is `working/MF/`, not canonical/. §9 proposed addendum is conditional on user approval at CV-1.6.
- [x] **Silent resolution 0** — OP-0008 explicitly attacked, NOT silently resolved. Path B is **candidate**, not adoption. Cat status (Cat B sketch level for §3.3 Φ_rich claim; Cat B target with NQ-242c-Rich anchor for full Path B; Cat A only post-§10.4 theoretical proof). All retained as open work at canonical until promotion via pipeline.
- [x] **No Research OS resurrection** — single-topic working file per `working/README.md`.
- [x] **Not reductive to external framework** — σ_rich components (centroid, inertia tensor, Wigner–von Neumann) are referenced as **standard mathematical objects**; their use is *contrastive* (CN10) — they augment SCC σ-framework, not replace SCC ontology.
- [x] **u_t primitive maintained** — all four σ_rich components are *derived diagnostics* of primitive $u^{(j)}$ field. No new primitive introduced. CN10 contrastive: centroid is $u$-weighted spatial moment; orientation is second-moment-tensor decomposition; Wigner-data is Hessian-spectral. All function-of-$u$ via standard derivations.
- [x] **CN5 4-energy not merged** — σ-tuple is a discrete invariant of the energy minimizer, not an energy term itself. σ_rich extension does not introduce new energy terms; CN5 4-term independence at single-formation preserved (per `mathematical_scaffolding_4tools.md` §8.3 amended CN5).
- [x] **Closure not assumed idempotent** — N/A.
- [x] **K not dual-treated** — K_act integer per Commitment 16; σ_rich components defined per active formation index; K-jump events are stratum transitions per Tool A1.
- [x] **No metastability claim without P-F flag** — N/A; σ_rich is static-Hessian invariant (zero-T equilibrium framework). Dynamic σ_rich(t) trajectory inherits the metastability flag from `sigma_multi_trajectory.md` (P-F flagged in §8 of that file).
- [x] **OP-0008 not silently resolved** — Path B is **candidate** for CV-1.6 release; explicit Cat status (Cat B sketch / Cat B target with NQ-242c-Rich anchor / Cat A everywhere only post-W9+ theoretical proof). Severity 🟠 HIGH retained on `open_problems.md` until promotion. Path A fallback registered (§5.1, §9.2). Hybrid intermediate registered (§5.4, §9.3). No claim of resolution at this working file.
- [x] **OP-0009-related sub-items**: OP-0009-A architecture (stratified space) per Tool A1 §2 of `mathematical_scaffolding_4tools.md` — σ_rich operates on stratum interiors; OP-0009-Pre pre-objective primacy preserved via $u_t$-derived components per CN10.

---

## §12. References

### §12.1 Working files

- `THEORY/working/MF/sigma_multi_trajectory.md` (D-6b dynamic σ_multi^A(t) framework; Lemma 4.4.1(c) Cat C non-determinism source for OP-0008).
- `THEORY/working/MF/multi_formation_sigma.md` (D-6a static σ_multi^A; §5.5 cross-formation Goldstone observation, Wigner-pair source).
- `THEORY/working/MF/mathematical_scaffolding_4tools.md` (4-tool framework; §4 Tool A3 PH foundation; §3 Tool A2 quotient framework).
- `THEORY/working/MF/K_status_commitment.md` (Commitment 16 K_field/K_act decomposition; ordered/unordered architecture).
- `THEORY/working/MF/lambda_rep_ontology.md` (planned W6 OAT-3; λ_rep status; relevant for §2.3.3 $W_{jk}$ which depends on λ_rep coupling strength).

### §12.2 Canonical references

- `THEORY/canonical/canonical.md` §11.1 Commitment 14 (single-formation σ).
- `THEORY/canonical/canonical.md` §11.1 Commitment 14-Multi (D-6a static, CV-1.5.1).
- `THEORY/canonical/canonical.md` §11.1 Commitment 16 (K_field/K_act, CV-1.5.1).
- `THEORY/canonical/canonical.md` §13 T-σ-multi-A-Static, T-σ-Multi-1.
- `THEORY/canonical/canonical.md` §14 CN5, CN10, CN17.
- `THEORY/canonical/open_problems.md` OP-0008 (direct attack subject), OP-0009 (related ontological foundations).
- `THEORY/canonical/theorem_status.md` (D-6a entries; D-6b deferred to CV-1.6 with Path B candidate per this file).

### §12.3 Open problem / NQ register

- **OP-0008** (this file's direct attack): σ^A K-jump non-determinism. Path A / Path B / Hybrid bifurcation per `open_problems.md`. **Severity 🟠 HIGH retained** until Path B Cat A everywhere or Path A canonicalization.
- **NQ-242** (W6+ 4-6 weeks → 3-4 weeks PH-augmented): full Hessian σ-tuple time-series + rigorous K-jump theory. Reframed as σ_rich numerical pipeline per §8.3.
- **NQ-242c** (W6+ 2-3 weeks): explicit two-trajectory counterexample. Two-fold reframe per §6.1 (σ_standard non-det confirm + σ_rich det confirm).
- **NQ-242d** (W6+ 2-3 weeks): σ^D symmetry-emergence characterization. Path B framing per §7.

### §12.4 External references (mathematical content of σ_rich)

- Wigner, E. P. & von Neumann, J. (1929). "Über das Verhalten von Eigenwerten bei adiabatischen Prozessen". *Physikalische Zeitschrift* 30, 467–470. — Wigner–von Neumann avoided-crossing theorem (§2.3.3 source).
- Reed, M. & Simon, B. (1978). *Methods of Modern Mathematical Physics IV: Analysis of Operators*. Academic Press. §XIII.5 — perturbation of eigenvalues; codim-2 generic crossings.
- Cohen-Steiner, D., Edelsbrunner, H., & Harer, J. (2007). "Stability of persistence diagrams". *Discrete Comput. Geom.* — PH stability foundation (§8.2 non-lift fact).
- Kim, W. & Mémoli, F. (2021). "Spatiotemporal Persistent Homology for Dynamic Metric Spaces". arXiv:1712.04064. — time-dependent zigzag PH (NQ-242 pipeline §8.3).
- Goresky, M. & MacPherson, R. (1988). *Stratified Morse Theory*. Springer. — stratum interior framework (§2.3 σ_rich definition domain).

### §12.5 Daily logs

- `THEORY/logs/daily/2026-04-29/04_D6b_sigma_trajectory_development.md` Lemma 4.4.1(c) — OP-0008 source.
- `THEORY/logs/daily/2026-04-29/09_session_self_critique.md` §2.3 — Lemma 4.4.1(c) Cat downgrade C.
- `THEORY/logs/daily/2026-04-30/01_canonical_promotion_log.md` — CV-1.5.1 D-6a context.
- `THEORY/logs/daily/2026-04-30/02_4tool_mapping_summary.md` — Tool A3 PH framing related to §8.

---

**End of sigma_rich_augmentation.md.**

**Status: working draft. OP-0008 Path B (rich-σ augmentation) candidate proposal. σ_rich definition (§2) Cat B sketch; Φ_rich determinism claim (§3.3) Cat B sketch; NQ-242c-Rich + NQ-242d explicit construction proposed (§6, §7) for W6+ Cat A target. CV-1.6 Commitment 14-Multi (D) addendum (§9.1) marked CANDIDATE NOT PROMOTED. Path B vs Path A vs Hybrid registered (§5, §9). Hard constraints verified (§11). OP-0008 severity 🟠 HIGH retained.**

**File:** `/Users/ojaehong/Perception/Perception_theory/THEORY/working/MF/sigma_rich_augmentation.md`
**Created:** 2026-04-30 (W5 Day 4).
**Promotion target:** CV-1.6 W8 D-CV1.6-O5 packet (Path B vs Path A vs Hybrid decision item).
