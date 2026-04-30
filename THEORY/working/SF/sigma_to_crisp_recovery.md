# sigma_to_crisp_recovery.md — σ → Crisp K-Object Recovery Procedure (NQ-189)

**Status:** working draft (NQ-189, W5 Day 5+ self-spawn 2026-04-29).
**Type:** Foundational gap closure; pre-objective → object derivation procedure formalization.
**Author origin:** Round-2 spawn 2026-04-27 NQ-189 ("σ → crisp object recovery, Commitment 11 derivative-objecthood"). Critic 7-agent verdict (W5 Day 3 EOD, §"What's Missing"): "No discussion of crisp-object recovery (Issue R / NQ-189). Foundational gap, not just research extension. Paper 1 cannot be submitted without addressing it."
**Canonical refs:** §11.1 #1 Commitment 1 (line 758: u_t primitive, not crisp subset / class label / instance ID); §11.1 #3 Commitment 11 (line 762: crisp objects derivative via thresholding/stabilization); §11.1 #14 Commitment 14 (line 784: σ-tuple = $(\mathcal{F}; \{(n_k,[\rho_k],\lambda_k)\}_{k=1}^K)$); §11.1 #16 Commitment 16 (line 796: K_field/K_act); §11.2 #3 (line 822: threshold recovery rules — open design choice); §14 CN4 (line 1601: Group F crisp recovery interface architecturally distinct); §14 CN10 (contrastive vs reductive); §14 CN17 (line 1645: σ-Labeled Formation Quantization, F=1 single-mode vs F≥2 multi-mode).
**Working refs:** `working/MF/F_Kstep_K_triple.md` §2.1, §3, §7 (F/K_step/K_act/K_field quadruple bridge + Tool A3 PH); `working/MF/mathematical_scaffolding_4tools.md` §4 (Tool A3 PH); `working/SF/mode_count.md` §1 (N_unst spectral); `working/MF/from_single.md` §3.3 (R23 F=9 empirical anchor).
**Open problems:** OP-0009-K (resolved CV-1.5.1 via Commitment 16); OP-0009-A (architecture choice); **NQ-189 (this file's resolution candidate)**.

---

## §1. Mission Statement

> **"σ-tuple → crisp K-object recovery procedure는 무엇인가? Commitment 11 'crisp objects는 derivative'의 *구체적 derivation procedure*는 어떻게 정식화되는가?"**

이 working file은 NQ-189 (σ → crisp object recovery) 의 resolution candidate이며, SCC의 foundational *pre-objective → object* derivation procedure를 정식화한다.

**핵심 주장**:
1. Commitment 11이 약속하는 "crisp objects derivative status"는 σ-tuple로부터 명시적 5-step recovery procedure로 실현된다 (§3).
2. K-field architecture는 trivial recovery (Cat A) 를 제공한다 (§4); single-field F-multi case는 gradient flow basin assignment 를 요구한다 (§5, Cat B target).
3. F (within-formation peaks) 와 K (architecture-level objects) 의 distinction은 crisp recovery 결과에 보존된다: K objects each with $F_j$ parts (§6).
4. Threshold $\theta$ 의 canonical 선택은 §11.2 #3 (line 822, "open design choice") 에 위임된다; σ-tuple-driven $\theta^*$ derivation은 Cat C target (§7).
5. Persistent homology (Tool A3) 가 recovery procedure 의 standard mathematical framework 를 제공한다 (§8).
6. Paper 1 §1 (foundational ontology) 는 §3 + §4 minimal version (Cat A trivial K-field + Cat B target single-field) 으로 충족 가능하다 (§11).

**SCC 핵심 약속의 mathematical 충실화**: Commitment 11 ("crisp objects는 derivative") 이 단순 ontological declaration 이 아니라, σ-tuple → crisp 5-step procedure 의 *명시적 algorithmic content* 를 갖는 commitment 임을 본 working file 이 정식화한다.

---

## §2. Crisp Object Definition

### §2.1 Crisp object as vertex subset

**Definition 2.1 (crisp object).** A *crisp object* on graph state $X_t$ is a non-empty subset
$$O \subseteq X_t.$$

**Definition 2.2 (crisp object family).** A *crisp object family* of cardinality $K$ is a collection
$$\mathcal{O} = \{O_j\}_{j=1}^K, \quad O_j \subseteq X_t,$$
satisfying:
- (D1) **Non-emptiness**: $O_j \neq \emptyset$ for all $j$.
- (D2) **Disjointness**: $O_j \cap O_{j'} = \emptyset$ for $j \neq j'$.
- (D3) **Peak coverage**: each strict local maximum of $u^*$ (i.e., each peak counted by $\mathcal{F}(u^*)$) lies in some $O_j$.

Note (D2) is the defining feature of "K distinct objects": disjoint vertex membership reproduces classical individuation (no overlap, no shared sites). (D3) ensures the crisp family preserves all peaks identified by $\mathcal{F}$; failure of (D3) discards information available in the soft system.

### §2.2 Recovery from soft minimizer

**Definition 2.3 (threshold recovery).** Given $u^* \in [0,1]^n$ a local minimizer of $\mathcal{E}$ on $\Sigma_m$ and threshold $\theta \in (0,1)$,
$$\mathrm{supp}_\theta(u^*) := \{x \in X : u^*(x) \geq \theta\}.$$
This is the crisp *superlevel set* at threshold $\theta$.

The crisp object family is then defined as the set of connected components of $\mathrm{supp}_\theta(u^*)$ in $G$:
$$\mathcal{O}_\theta(u^*) := \mathrm{ConnComp}_G(\mathrm{supp}_\theta(u^*)).$$

This realizes Commitment 11's "thresholding" branch. The "stabilization" branch (gradient descent → local minimum, then threshold) is the implicit prerequisite (we apply recovery to $u^*$, not to arbitrary $u$).

### §2.3 Cardinality dependencies

The cardinality $|\mathcal{O}_\theta(u^*)| = K_{\mathrm{step}}(u^*; \theta)$ (canonical §12 line 827; cf. F_Kstep_K_triple.md §2.2). Hence
$$|\mathcal{O}_\theta(u^*)| \leq \mathcal{F}(u^*) \quad \text{(canonical §12 line 832)}$$
with equality iff every peak is isolated above threshold (no bridged-bilobed configuration).

This makes **the crisp recovery output explicitly threshold-dependent**, a feature that §7 will address via $\theta^*$ canonicalization.

---

## §3. σ-tuple → K Objects: Five-Step Procedure (Proposed)

We propose an explicit 5-step procedure mapping the σ-tuple
$$\sigma(u^*) = \big(\mathcal{F}(u^*);\ \{(n_k,[\rho_k],\lambda_k)\}_{k=1}^K\big)$$
to a crisp object family $\{O_j\}_{j=1}^{K_{\mathrm{out}}}$. Steps 1–2 produce the partition; Steps 3–5 attach σ-derived structural labels.

### §3.1 Step 1 — Peak extraction

From $u^*$, extract the set of strict local maxima:
$$P(u^*) := \{x \in X : u^*(x) > u^*(y)\ \forall y \sim x\}.$$
Then $|P(u^*)| = \mathcal{F}(u^*)$. These are the *candidate object centers*.

**Output of Step 1**: ordered peak set $P = \{p_1, \ldots, p_{\mathcal{F}}\}$ (ordering convention: descending $u^*(p_i)$, tie-break by lexicographic vertex index).

### §3.2 Step 2 — Basin assignment (gradient-flow / discrete Voronoi)

Each non-peak vertex $x \in X \setminus P$ is assigned to a peak via discrete gradient flow:
$$\mathrm{basin}(x) := \lim_{n \to \infty} \phi^n(x), \quad \phi(x) := \arg\max_{y \in N(x) \cup \{x\}} u^*(y),$$
where $N(x)$ denotes the closed graph neighborhood of $x$. Termination occurs when $\phi(x) = x$ (i.e., $x$ is a peak), giving $\mathrm{basin}(x) \in P$.

**Tie-breaking**: when $\phi$ is not single-valued (multiple neighbors achieve the argmax), a canonical graph-intrinsic tie-break rule applies:
1. **Primary**: assign to the basin containing the neighbor with smaller graph distance to its peak $p_i$ (i.e., prefer the neighbor whose peak is closest in graph metric).
2. **Secondary (equal distance)**: among remaining ties, assign to the basin whose peak $p_i$ has the lex-smaller vertex index under the fixed canonical node ordering on $G$.
3. **Tertiary (equal peak lex-index)**: assign to the basin whose peak $p_i$ has smaller graph distance to the fiducial node $x_0 \in X$ (the lex-smallest node in $G$).

This tie-break is **graph-intrinsic**: it depends only on the graph metric of $G$ and the fixed canonical node ordering, not on the σ-tuple or irrep labels. In particular, it does not use σ-derived quantities to resolve ambiguities in the procedure that is used to *produce* σ-derived labels — avoiding the circularity in the prior formulation (Mulliken character order requires Step 4 output to be available at Step 2).

**Output of Step 2**: partition of $X$ into basins $\{B_1, \ldots, B_{\mathcal{F}}\}$ where $B_i := \{x : \mathrm{basin}(x) = p_i\}$.

This is the discrete analogue of the Morse-theoretic stable manifold decomposition; it reproduces the *Voronoi tessellation under graph metric weighted by $u^*$*.

### §3.3 Step 3 — Boundary refinement (σ nodal count)

The σ-tuple's $k$-th entry $n_k$ is the nodal-domain count of the $k$-th Hessian eigenvector (Courant; canonical §11.1 #14). For unstable directions $\lambda_k < 0$, the nodal pattern indicates *how peaks split* under perturbation along $\phi_k$.

**Boundary structure rule**: assign each basin pair $(B_i, B_j)$ a *boundary type* based on how the Hessian eigenvectors restricted to $B_i \cup B_j$ behave at the inter-basin edge:
- if $\sum_k \mathbb{1}[\phi_k|_{B_i \cup B_j} \text{ has nodal wall between } B_i, B_j]$ is large, $\partial(B_i, B_j)$ is *strongly distinct*.
- if all $\phi_k$ are co-aligned across $B_i \cup B_j$, the basins are *weakly distinct* (candidate for merging at finer threshold).

This step is a refinement, not a partition revision; it labels each inter-basin boundary edge with a structural-strength score derived from the σ Hessian.

### §3.4 Step 4 — Irrep label (σ symmetry class)

Each peak $p_i$ inherits the irrep label of the dominant Hessian eigenvector determined by projection onto the basin indicator — computed on the **full eigenspace**, not a basin-restricted subspace:
$$\mathrm{irrep}(O_i) := [\rho_{k^*(i)}], \quad k^*(i) := \arg\max_k \bigl\{\mathrm{Re}\langle \psi_k, \chi_{B_i} \rangle^2\bigr\},$$
where $\psi_k$ are the eigenvectors of $H(u^*)$ on the full space $\mathbb{R}^n$ (equivalently, the constrained Hessian $H(u^*)|_{T_u\Sigma_m}$ restricted to the full eigenspace), $\chi_{B_i} \in \{0,1\}^n$ is the basin indicator function with $(\chi_{B_i})_x = \mathbb{1}[x \in B_i]$, and $\langle \cdot, \cdot \rangle$ is the canonical inner product on $\mathbb{R}^n$.

**Rationale for full-eigenspace formulation**: the basin-restricted norm $\|\psi_k|_{B_i}\|^2$ was the prior formulation; it is ill-posed because $\psi_k$ supported mostly outside $B_i$ (e.g., a delocalized global mode) can still score large by normalization of the restriction. The projection $\langle \psi_k, \chi_{B_i} \rangle^2$ instead measures how much of the unit-normalized $\psi_k$ aligns with the basin's characteristic function — a well-defined, basis-independent quantity on the full space. Tie-break: by lex order in $(n_k, [\rho_k])$ Mulliken order (smaller $n_k$ first, then alphabetical irrep label).

This assigns each crisp object a *symmetry class* under the residual stabilizer $\mathrm{Stab}_G(u^*)$. On $D_4$-symmetric graphs, $\mathrm{irrep}(O_i) \in \{A_1, A_2, B_1, B_2, E\}$, mapping each crisp object to one of 5 atomic-orbital-style classes (canonical §11.1 #14 W4 04-25 NQ-141 anchor: $\ell \bmod 4 \to D_4$ irrep table, 0-exception correspondence on R23 dataset).

This is **the σ-framework's specific contribution** to crisp recovery — irrep labels are not available to threshold-only or persistent-homology-only recovery procedures.

### §3.5 Step 5 — σ-eigenvalue (object stability ranking)

Each crisp object $O_i$ inherits the eigenvalue label
$$\mathrm{stab}(O_i) := \lambda_{k^*(i)}.$$
Stable directions ($\lambda_k > 0$) produce *robust* objects; near-zero eigenvalues mark *marginally stable* objects (candidates for K-jump events under perturbation; cf. Commitment 16 K_act dynamic).

The crisp object family with attached labels is therefore
$$\mathcal{O}^\sigma(u^*) = \{(O_i,\ \mathrm{irrep}(O_i),\ \mathrm{stab}(O_i))\}_{i=1}^{\mathcal{F}}.$$

### §3.6 Procedure summary

| Step | Input | Output | σ-tuple component used |
|---|---|---|---|
| 1 Peak extract | $u^*$ | $P = \{p_1, \ldots, p_{\mathcal{F}}\}$ | $\mathcal{F}$ |
| 2 Basin assign | $u^*, P$ | $\{B_1, \ldots, B_{\mathcal{F}}\}$ partition | (none — gradient flow only) |
| 3 Boundary refine | $\{B_i\}$, Hessian eigenvectors | inter-basin boundary scores | $\{n_k\}$ |
| 4 Irrep label | $\{B_i\}$, Hessian eigenvectors | $\{\mathrm{irrep}(O_i)\}$ | $\{[\rho_k]\}$ |
| 5 Stability rank | $\{B_i\}$, Hessian eigenvalues | $\{\mathrm{stab}(O_i)\}$ | $\{\lambda_k\}$ |

The procedure exhausts all four σ-tuple components $(\mathcal{F}, n_k, [\rho_k], \lambda_k)$, demonstrating that **σ contains exactly the information needed to recover the crisp object family with full structural labeling**. This is the *mathematical content* of Commitment 11.

### §3.7 Static-dynamic correspondence: NQ-189 ↔ NQ-253

**NQ-189 (this file)** establishes the *static* recovery procedure: given a fixed minimizer $u^*$ with its σ-tuple $\sigma(u^*)$, the 5-step procedure above produces the crisp object family $\{O_j\}_{j=1}^K$ with full structural labels. This is a snapshot procedure — it answers "what crisp objects does this soft-field configuration correspond to?"

**NQ-253** (`working/MF/formation_birth_string_breaking.md`) addresses the *dynamic* counterpart: how does the σ-trajectory $\sigma(u_t)$ behave when the system crosses a K-jump event (a moment at which the number of active formations changes discontinuously)? At a K-jump, the crisp recovery output $\{O_j\}_{j=1}^K$ changes cardinality; NQ-253 characterizes the string-breaking mechanism by which one formation birth/death event propagates into the σ-tuple structure.

Together, NQ-189 and NQ-253 define the **static-dynamic σ↔crisp correspondence** at the foundation of the multi-formation framework:
- **Static side** (NQ-189): $\sigma(u^*) \mapsto \{O_j\}_{j=1}^K$ — the recovery map at equilibrium.
- **Dynamic side** (NQ-253): $\sigma(u_t) \xrightarrow{K\text{-jump}} \sigma(u_{t+\epsilon})$ — the σ-trajectory across formation birth/death events.

This correspondence is a prerequisite for any Paper 1 treatment of the multi-formation framework: without the static recovery (NQ-189), the dynamic trajectory has no crisp-object interpretation; without the dynamic crossing characterization (NQ-253), the static recovery is a point procedure with no narrative of how the crisp-object family evolves.

---

## §4. K-field Architecture Recovery (Trivial Case, Cat A Target)

### §4.1 Direct support thresholding

Under K-field architecture (canonical §11.1 #16; modeling-layer commitment $K_{\mathrm{field}}$), the soft system is a tuple of K fields:
$$\mathbf{u}^* = (u^{(1)*}, \ldots, u^{(K_{\mathrm{field}})*}), \quad u^{(j)*}: X \to [0,1].$$
Each $u^{(j)*}$ is a soft cohesion field associated to slot $j$ of the architecture. Crisp recovery is then *trivial*:
$$O_j := \mathrm{supp}_\theta(u^{(j)*}) = \{x : u^{(j)*}(x) \geq \theta\}.$$

The K-field architecture *labels* objects ex ante through slot index $j$. The crisp family is automatically partitioned by the architectural index, no basin assignment needed.

### §4.2 Active stratum filtering (Commitment 16 K_act)

Active objects are those above support threshold $\epsilon$ (Commitment 16(ii)):
$$\mathcal{O}_{\mathrm{act}} := \{O_j : \|u^{(j)*}\|_1 > \epsilon\}, \quad |\mathcal{O}_{\mathrm{act}}| = K_{\mathrm{act}}.$$
Inactive slots (those with $\|u^{(j)*}\|_1 \leq \epsilon$) produce empty crisp objects, excluded from $\mathcal{O}_{\mathrm{act}}$ by convention.

### §4.3 Cat A status

> **Cat A (conditional)**: under the disjoint-support hypothesis. Multi.py minimizers with $\lambda_{\mathrm{rep}} > 0$ generically satisfy small inter-formation overlap (see canonical CN5 + `working/MF/multi_formation_sigma.md`), making this hypothesis generically applicable in the K-field architecture. **Cat B target** for the generic overlap regime (NQ-242 PH pipeline addresses this in W6+).

**Theorem candidate (Cat A K-field recovery)**. Under K-field architecture with disjoint-support condition $\mathrm{supp}_\theta(u^{(j)*}) \cap \mathrm{supp}_\theta(u^{(j')*}) = \emptyset$ for $j \neq j'$, the crisp recovery $\mathcal{O}_{\mathrm{act}} = \{O_j : j \in \mathrm{active}(\mathbf{u}^*)\}$ is well-defined as a crisp object family per Definition 2.2, with $|\mathcal{O}_{\mathrm{act}}| = K_{\mathrm{act}}$.

**Proof sketch**: (D1) by activation filter; (D2) by hypothesis; (D3) reduces to: each peak of $\mathbf{u}^*$ (locally maximal in the joint state) lies in some active slot's support, which holds whenever $\theta < \max_j \max_x u^{(j)*}(x)$. ∎

The disjoint-support hypothesis is the **non-trivial content** — coupling-induced overlaps require the basin-assignment generalization (§5).

---

## §5. Single-field K=1 with F≥2: F-multi Crisp Recovery (Cat B Target)

### §5.1 Configuration

Single-field state $u^* : X \to [0,1]$, single K-field slot ($K_{\mathrm{field}} = 1$, equivalently no K-field architecture imposed), but $\mathcal{F}(u^*) \geq 2$ — multiple peaks within a single connected formation.

This is the **default configuration under full SCC** by T-PreObj-1 (canonical §11.1 #15: $\mathcal{F} \geq 2$ ground state). Empirical anchor: R23 90-run enumeration, F=9 maximum, F≥5 universal lower bound (working/MF/from_single.md §3.3).

### §5.2 CN17 σ-Labeled FQ refinement (canonical §14 line 1645–1650)

CN17 distinguishes two regimes:
- **F=1 single-mode** (atomic-like; rare under full SCC).
- **F≥2 multi-mode** (molecular-like; default).

In the multi-mode case, the F peaks are **within-formation parts** rather than separate formations. The cognitive correlate: F-multi peaks are *internal articulation* of a single object (e.g., parts of a complex shape), not a multi-object scene.

### §5.3 Recovery procedure for F-multi

Apply the §3 5-step procedure with no architectural pre-labeling:
- Steps 1–2 produce the partition $\{B_1, \ldots, B_{\mathcal{F}}\}$ via peak extraction + basin assignment.
- The crisp recovery output is $\mathcal{F}$ "object parts" rather than $\mathcal{F}$ separate objects.

The cognitive interpretation is therefore **K=1 single object with F internal parts**, not K=F separate objects. This preserves the SCC pre-objective ontology: the soft system articulates internal structure that is *one cohesive thing* despite multi-peak topology.

### §5.4 Cat B status

The procedure is mathematically defined (Cat A in spec) but the *interpretation rule* (when to read $\mathcal{F}$ peaks as "parts of one object" vs "separate objects") requires an additional commitment beyond the σ-tuple alone. The K-field architecture provides this commitment trivially (§4); without it, the interpretation falls back on $K_{\mathrm{step}}$ (connectivity at a chosen $\theta$): connected superlevel set ⇒ one object with parts; disconnected ⇒ separate objects.

This is **Cat B target**: structural procedure clear, interpretation parameter ($\theta$ choice or architectural commitment) external.

---

## §6. Distinction: Object Parts (F) vs Distinct Objects (K)

### §6.1 Vocabulary alignment with OAT-2 F_Kstep_K_triple

Per `working/MF/F_Kstep_K_triple.md` §1, §3:
- **$\mathcal{F}$** — within-formation peak count (threshold-free derived diagnostic).
- **$K_{\mathrm{step}}$** — connectivity-based count at threshold $\theta$ (observer artifact, threshold-dependent).
- **$K_{\mathrm{act}}$** — active stratum index from K-field state (dynamic diagnostic).
- **$K_{\mathrm{field}}$** — architectural cap (modeling-layer commitment).

Crisp recovery output:

| Configuration | K (object count) | F per object | Interpretation |
|---|---|---|---|
| K-field, all slots active | $K = K_{\mathrm{act}}$ | $F_j$ within slot $j$ | $K$ objects, slot $j$ has $F_j$ parts |
| Single-field, F-multi, $K_{\mathrm{step}} = 1$ | $K = 1$ | $F_1 = \mathcal{F}$ | 1 object, $\mathcal{F}$ parts |
| Single-field, F-multi, $K_{\mathrm{step}} \geq 2$ | $K = K_{\mathrm{step}}$ | $F_j$ per component | $K_{\mathrm{step}}$ objects, component $j$ has $F_j$ parts |

### §6.2 Key inequality

In all configurations:
$$K \leq \mathcal{F}, \qquad \sum_{j=1}^{K} F_j = \mathcal{F}.$$
The crisp object family $\{O_j\}_{j=1}^K$ is disjoint by Definition 2.2; each $O_j$ further decomposes into $F_j$ basins (parts) per the §3 Step 2 basin partition restricted to $O_j$.

### §6.3 Cognitive interpretation lock

Per CN10 (contrastive vs reductive), the K vs F distinction is *SCC-intrinsic* — the K-field/single-field decomposition is the formal commitment, not a downstream cog-sci borrowing. Marr's "primal sketch → 2.5D sketch → 3D model" (Marr 1982) is a *contrastive parallel*, not a reduction (§10).

**Important boundary**: $K_{\mathrm{step}}$-based recovery (no K-field commitment) places the K vs F distinction on a *threshold-dependent observer artifact*, with all attendant ambiguities (canonical §11.2 #3 line 822). K-field architecture commitment removes this ambiguity by ex ante labeling.

---

## §7. Threshold $\theta$ Choice

### §7.1 Standard $\theta = 1/2$

The symmetric choice $\theta = 1/2$ corresponds to the unstable fixed point of the double-well $W'(u) = 2u(1-u)(1-2u)$ (canonical CODE convention; CLAUDE.md "Critical Implementation Details"). Under sharp-interface limit, $\theta = 1/2$ produces the canonical interface contour.

**Pros**: convention-free, double-well-symmetric, computable without σ.
**Cons**: not σ-derived (ignores spectral structure), may miss bridged-bilobed configurations.

### §7.2 σ-tuple-derived optimal $\theta^*$ (proposal)

A natural σ-derived threshold is the value at which the superlevel-set partition achieves exactly $\mathcal{F}(u^*)$ connected components — the "natural" individuation threshold:
$$\theta^* := \sup\{\theta : K_{\mathrm{step}}(u^*; \theta) = \mathcal{F}(u^*)\}.$$
At $\theta^*$, we are at the **highest** threshold for which all $\mathcal{F}$ peaks remain in disjoint connected components; raising $\theta$ further above $\theta^*$ begins to erode one or more components below the threshold (dropping $K_{\mathrm{step}}$ below $\mathcal{F}$).

**Choice of sup over inf**: the set $\{\theta : K_{\mathrm{step}}(u^*; \theta) = \mathcal{F}(u^*)\}$ is an interval $[\theta_{\mathrm{lo}}, \theta^*]$ where $\theta_{\mathrm{lo}}$ is the threshold at which the $\mathcal{F}$-th component first appears (components split from below as $\theta$ rises). The sup $\theta^*$ is the last stable point before components start disappearing — the tightest individuation that still separates all $\mathcal{F}$ peaks. The inf would give $\theta_{\mathrm{lo}}$, which is the first moment the partition achieves $\mathcal{F}$ components and corresponds to a much looser boundary.

**Properties** (proposed, unverified):
- $\theta^* < \max_x u^*(x)$ (otherwise no peak survives).
- $\theta^*$ is the *highest* threshold at which $\mathrm{supp}_{\theta^*}(u^*)$ retains all $\mathcal{F}$ peaks in disjoint components; equivalently, the basin partition is stable for all $\theta \leq \theta^*$ and begins to degrade above $\theta^*$.

This corresponds to the **death threshold** of the lowest-persistence H_0 bar in the superlevel-set persistent homology of $u^*$ (cf. §8).

### §7.3 Cat C status (canonical §11.2 #3 line 822 deferred)

The threshold choice protocol is canonically *open* (§11.2 #3): "The precise protocol by which crisp objects are extracted from soft cohesion fields (choice of thresholds, stability criteria, hysteresis rules) is not canonically fixed." This working file proposes $\theta^*$ as a Cat C target (~4–6 weeks); Paper 1 §6 (outlook) flags this as future work per Critic 7-agent verdict (W5 Day 3 EOD).

---

## §8. Persistent Homology Approach (Tool A3)

### §8.1 PH framework reference

Per `working/MF/mathematical_scaffolding_4tools.md` §4 (Tool A3) and `working/MF/F_Kstep_K_triple.md` §7, the superlevel-set persistent homology of $u^*$ provides a standard mathematical framework for the recovery procedure.

For threshold filtration $\theta \in [0, 1]$, define
$$U_\theta(u^*) := \{x : u^*(x) \geq \theta\}, \quad \theta_1 \geq \theta_2 \implies U_{\theta_1} \subseteq U_{\theta_2}.$$
The PH barcode tracks $H_0$ (connected components) and $H_1$ (loops) across this filtration.

### §8.2 $H_0$ barcode = peak structure

- Each $H_0$ bar corresponds to a peak of $u^*$.
- **Birth**: bar $b_i$ is born at $\theta = u^*(p_i)$ (peak value).
- **Death**: bar $b_i$ dies at the threshold where its component merges with a higher peak's component (a *saddle merge*).
- **At $\theta = 0$**: all bars merge into the single component $X$ (assuming $G$ connected). One bar is *infinite* (the global maximum's component); the rest die at finite saddle thresholds.

$$|\{H_0 \text{ bars at } \theta\}| = K_{\mathrm{step}}(u^*; \theta).$$

### §8.3 $\mathcal{F}$ recovery from $H_0$ barcode

$$\mathcal{F}(u^*) = |\{H_0 \text{ bars total}\}| = |\{\text{birth times}\}|.$$
Per F_Kstep_K_triple.md §7.1: "F는 persistent homology의 0차 invariant. 4-quantity bridge가 PH 표준 framework로 reformulate됨."

### §8.4 Crisp recovery via PH barcode persistence

**Persistence-based recovery**: given persistence threshold $\delta > 0$, retain only $H_0$ bars with $\mathrm{lifetime}(b_i) := \mathrm{birth}(b_i) - \mathrm{death}(b_i) \geq \delta$.
$$K^{\delta}(u^*) := |\{b_i : \mathrm{lifetime}(b_i) \geq \delta\}|.$$
- $\delta = 0$: $K^0 = \mathcal{F}$ (all peaks).
- $\delta \to \infty$: $K^\infty = 1$ (only the global max survives; total mass coarsens to single object).
- intermediate $\delta$: gives a *robust* object count, filtering out shallow peaks.

This realizes Cohen-Steiner–Edelsbrunner–Harer (2007) PH stability: the recovered count is stable under $L^\infty$ perturbations of $u^*$ up to magnitude $\delta/2$.

### §8.5 PH-based crisp object family

For each retained bar $b_i$ with $\mathrm{lifetime}(b_i) \geq \delta$:
$$O_i^{\delta} := \mathrm{ConnComp}_G(U_{\mathrm{death}(b_i) + \epsilon}(u^*))_{\ni p_i}$$
(the connected component containing $p_i$ at threshold infinitesimally above the death time). The family $\{O_i^\delta\}$ is disjoint by construction (death thresholds separate components).

**Connection to §3 5-step procedure**: PH-based recovery (this section) is structurally equivalent to §3 Steps 1–2 with $\theta = \mathrm{death}(b_i) + \epsilon$ used per-peak rather than uniformly. The σ-derived labels (§3 Steps 3–5) are an *additional* layer not present in pure PH.

### §8.6 $H_1$ barcode = inter-object loops

The $H_1$ barcode tracks cluster topology: persistent 1-cycles correspond to *holes* in the formation (e.g., torus-like configurations). For Paper 1 §1 scope (foundational), $H_0$-only recovery suffices; $H_1$ extension is research-level (Cat C).

---

## §9. Category Targets

### §9.1 Cat A — K-field architecture direct recovery (§4)

**Status**: Cat A target.
**Content**: Theorem candidate §4.3. Trivial under disjoint-support hypothesis.
**Effort**: low. Spec-level verification only.

### §9.2 Cat B — Single-field F-multi recovery via gradient flow (§5)

**Status**: Cat B target.
**Content**: §3 5-step procedure applied to single-field $u^*$. Mathematical procedure clear; interpretation (parts vs objects) requires external commitment ($\theta$ choice or K-field architecture).
**Effort**: medium. Standard graph-theoretic discrete Morse procedure.
**Sufficient for Paper 1 §1 minimal version** (Critic 7-agent verdict §"What's Missing" addressed).

### §9.3 Cat C — σ-tuple-driven $\theta^*$ derivation (§7.2)

**Status**: Cat C target (~4–6 weeks).
**Content**: Canonical $\theta^*$ from σ spectral structure; equivalence with PH lowest-persistence death threshold; stability theorem under perturbation.
**Effort**: high. Research-level open problem; canonical §11.2 #3 line 822 deferred.

### §9.4 Cat C extension — σ-irrep-labeled crisp recovery

**Status**: Cat C extension.
**Content**: §3 Steps 4–5 (irrep + eigenvalue labels) elevated to canonical theorem-level claims; $D_4$ irrep table connection (R23 NQ-141 anchor) generalized to arbitrary stabilizer subgroups.
**Effort**: high. Requires generalizing W4 04-25 NQ-141 anchor beyond R23 dataset.

---

## §10. Cognitive Correlate (CN10 Downstream)

### §10.1 Marr's tri-level vision hierarchy (parallel, not reduction)

Marr (1982, *Vision*, Freeman) proposes three representational levels:
- **Primal sketch** — local intensity changes, no objects yet.
- **2.5D sketch** — viewer-centered surface representation.
- **3D model** — object-centered structural description.

**SCC parallel** (CN10 contrastive):
- Soft cohesion field $u_t$ ↔ primal sketch (graded, pre-objective).
- σ-tuple intermediate ↔ 2.5D sketch (structurally articulated, not yet objects).
- Crisp object family $\{O_j, \mathrm{irrep}(O_j), \mathrm{stab}(O_j)\}$ ↔ 3D model (object-centered, structurally labeled).

This is **contrastive**: the SCC procedure is mathematically self-contained (graph + spectral + variational), not derived from Marr. The parallel is a downstream interpretation, not an ontological foundation (CN10).

### §10.2 Pylyshyn FINSTs

Pylyshyn (1989, "FINST," *Cognition*) proposes a cognitive architecture with K visual indices binding to K objects pre-attentively. **SCC parallel**: K crisp objects (recovered per §3) = K cognitive slots. The K-field architecture (canonical §11.1 #16) provides the formal counterpart to FINST's K=4–5 capacity bound.

CN10 forbids the reverse identification (Pylyshyn K-slots ⇒ SCC K_field): the SCC ontological flow is one-way, $u_t$ → ($K_{\mathrm{field}}$, $K_{\mathrm{act}}$) → cog-sci comparisons (canonical Commitment 16 line 810).

### §10.3 Treisman FIT

Treisman (1982, *J. Exp. Psychol.*) Feature Integration Theory: pre-attentive features bound into objects via attention. **SCC parallel**: σ-tuple components (irrep, eigenvalue) = pre-bound features; crisp object family = bound features post-recovery. The §3 5-step procedure formalizes the *binding mechanism* in graph-spectral terms.

Again CN10 contrastive: σ-irrep is SCC-intrinsic representation theory of $\mathrm{Stab}_G(u^*)$, not borrowed from FIT.

---

## §11. Paper 1 §1 Critical Content

### §11.1 Critic 7-agent verdict reference

W5 Day 3 EOD Critic 7-agent verdict, §"What's Missing":
> "No discussion of crisp-object recovery (Issue R / NQ-189). Foundational gap, not just research extension. Paper 1 cannot be submitted without addressing it."

### §11.2 Resolution via this working file

**Minimal Paper 1 §1 inclusion** (sufficient for submission per Critic verdict):
1. **§3 5-step procedure** explicit statement (Step 1–2 procedural; Steps 3–5 σ-label decoration).
2. **§4 K-field architecture trivial Cat A case** (recovery is `supp_θ(u^(j)*)`).
3. **§5 single-field F-multi Cat B case** (basin assignment via gradient flow).
4. **§7 threshold choice flagged as open** (§11.2 #3 line 822 deferral).
5. **§10 cog-sci parallels** (Marr/Pylyshyn/Treisman) noted with CN10 contrastive lock.

Items 1–3 close the foundational gap; item 4 honestly demarcates the open research extension; item 5 connects to cog-sci downstream without violating CN10.

### §11.3 Paper 1 outlook (§6)

The σ-driven $\theta^*$ derivation (§7.2) and PH-based stable recovery (§8) are explicitly listed in Paper 1 §6 as research extensions, satisfying the "honest gap accounting" requirement (canonical §15 closing summary).

---

## §12. OP-0009-K + Commitment 11 Connection

### §12.1 OP-0009-K resolution status

OP-0009-K (K-status ambiguity) was **resolved at CV-1.5.1** via Commitment 16 K_field/K_act decomposition (canonical §11.1 #16, line 796). The two-tier (K_field architectural cap, K_act dynamic diagnostic) decomposition provides the formal commitment that crisp recovery (§4) inherits.

### §12.2 Commitment 11 mathematical content (this file's contribution)

Prior to this working file, Commitment 11 (canonical line 762) stated only:
> "Crisp objects may be recovered from the soft system by thresholding or stabilization, but they are derivative constructs, not foundational primitives."

This was an **ontological declaration without algorithmic content**. The §3 5-step procedure provides the *explicit derivation*:
- Steps 1–2 realize "thresholding/stabilization" branch concretely (peak extraction + basin assignment).
- Steps 3–5 add σ-derived structural labels not available to threshold-only recovery.

**Result**: Commitment 11 is upgraded from declaration to *procedurally specified commitment*. The "derivative" status is now *constructively backed* by the 5-step procedure.

### §12.3 OP-0009-A architecture choice

Architecture choice (single-field F-multi vs K-field) determines which §3 / §4 / §5 branch applies. This is the modeling-layer commitment per Commitment 16(i): the modeler chooses K_field ≥ 1 ex ante; crisp recovery follows §4 if K_field ≥ 2, §5 if K_field = 1 with F ≥ 2.

OP-0009-A remains **partially open** as canonical §11.2 #8 line 832 (multi-formation architecture choice). This working file does not resolve OP-0009-A but does assume its resolution per Commitment 16 to deliver concrete recovery procedures.

---

## §13. W7+ Priority + Cross-References

### §13.1 W7+ work plan

| Item | Cat | Effort | Trigger |
|---|---|---|---|
| §3 5-step procedure formal proof | Cat A | low (already constructive) | W6 promotion candidate |
| §4 disjoint-support theorem candidate | Cat A | low–medium | W6 promotion candidate |
| §5 basin assignment well-definedness | Cat B | medium | W7 |
| §7.2 $\theta^*$ from σ spectral structure | Cat C | high (~4–6 weeks) | W7+ |
| §8.4 PH-stability theorem under SCC perturbation | Cat C | high | W8+ |
| §3.4 irrep label canonical theorem | Cat C ext | high | W8+ |
| Paper 1 §1 minimal inclusion | — | low | Paper 1 submission gate |

### §13.2 Cross-references

- **canonical §11.1 #1 Commitment 1** (line 758): u_t primitive; not crisp subset / class label / instance ID. Maintained throughout (§14 hard constraint).
- **canonical §11.1 #3 Commitment 11** (line 762): crisp objects derivative — now procedurally specified per §3 (§12.2).
- **canonical §11.1 #14 Commitment 14** (line 784): σ-tuple = $(\mathcal{F}; \{(n_k,[\rho_k],\lambda_k)\})$. Source of all label-generation steps (§3 Steps 3–5).
- **canonical §11.1 #16 Commitment 16** (line 796): K_field/K_act. Source of §4 K-field recovery branch (§4.2 active filter).
- **canonical §11.2 #3** (line 822): threshold recovery rules (open). $\theta$ choice deferred per §7.3.
- **canonical §14 CN4** (line 1601): Group F crisp recovery interface architecturally distinct. The 5-step procedure §3 fits this Group F slot.
- **canonical §14 CN10**: contrastive vs reductive. Cog-sci parallels §10 are downstream comparisons, not foundations.
- **canonical §14 CN17** (line 1645): σ-Labeled Formation Quantization. F=1 vs F≥2 distinction underlies §5 single-field branch.
- **OAT-2 `working/MF/F_Kstep_K_triple.md`** §2.1, §3, §7: F/K_step/K_act/K_field quadruple bridge; Tool A3 PH connection.
- **OAT-supplementary `working/MF/mathematical_scaffolding_4tools.md`** §4: Tool A3 persistent homology framework.
- **OP-0009 family**: OP-0009-K (resolved CV-1.5.1); OP-0009-A (partially open); NQ-189 (this file).

---

## §14. Hard Constraints

### §14.1 canonical 직접 수정 0

This working file proposes **no edits to canonical.md**. Promotion to canonical is a separate action requiring:
1. Cat A theorem candidates (§4.3, §3 5-step well-definedness) verified to step-granularity.
2. Theorem-status registry update (`theorem_status.md`).
3. Critic review pass.
4. CHANGELOG.md entry.

### §14.2 u_t primitive maintained

Throughout the procedure, $u_t$ remains the **input** to the recovery process; crisp objects are the **output**. The directionality is one-way: $u_t \to \sigma \to \{O_j\}$. No step requires crisp objects as input. Commitment 1 (canonical line 758) is preserved.

### §14.3 CN10 contrastive lock

Cog-sci parallels (§10) are **downstream comparisons**. The SCC procedure (§3) is mathematically self-contained: graph $G$, soft field $u^*$, Hessian spectrum, basin partition. No cog-sci concept enters as definitional input. CN10 (canonical §14) preserved.

### §14.4 No premature resolution of NQ-189

This working file is a **resolution candidate**, not a closure. The §3 5-step procedure is well-defined as a *procedural specification*; its category status (Cat A vs B) and the $\theta^*$ canonicalization (Cat C) require further work. Per CLAUDE.md "Never silently resolve open problems," NQ-189 remains explicitly listed as open until promotion.

### §14.5 Paper 1 §1 minimum vs research extension separation

The Paper 1 §1 minimum (§11.2: items 1–3 + 5 with item 4 as flagged outlook) is **explicitly demarcated** from Cat C research extensions (§9.3, §9.4). Failure to maintain this separation would risk submitting Paper 1 with research-level claims masquerading as foundational results.

---

## §15. External References

- **Marr, D.** (1982). *Vision: A Computational Investigation into the Human Representation and Processing of Visual Information*. W. H. Freeman, San Francisco. — Tri-level (primal sketch → 2.5D → 3D model) cognitive vision hierarchy; §10.1 contrastive parallel.
- **Pylyshyn, Z. W.** (1989). "The role of location indexes in spatial perception: A sketch of the FINST spatial-index model." *Cognition* 32(1), 65–97. — FINST K-slot pre-attentive object indexing; §10.2 contrastive parallel for K_field architectural cap.
- **Treisman, A.** (1982). "Perceptual grouping and attention in visual search for features and for objects." *Journal of Experimental Psychology: Human Perception and Performance* 8(2), 194–214. — Feature Integration Theory binding mechanism; §10.3 contrastive parallel for σ-tuple → crisp recovery.
- **Cohen-Steiner, D., Edelsbrunner, H., Harer, J.** (2007). "Stability of persistence diagrams." *Discrete & Computational Geometry* 37(1), 103–120. — PH stability theorem; §8.4 robustness foundation.
- **Edelsbrunner, H., Harer, J.** (2010). *Computational Topology: An Introduction*. American Mathematical Society. — Standard reference for $H_0$ barcode / superlevel-set filtration framework (§8.2).

---

**End of working file.**

**Status:** working draft. NQ-189 resolution candidate. §3 5-step procedure specifies the σ → crisp K-object recovery; §4 K-field trivial Cat A and §5 single-field F-multi Cat B branches sufficient for Paper 1 §1 minimal inclusion (Critic 7-agent verdict §"What's Missing" addressed); §7 θ* + §8 PH stable recovery flagged Cat C research extensions per canonical §11.2 #3 line 822 open design choice.

**Promotion gates remaining**: §3 / §4 / §5 well-definedness theorems → Cat A targets at W6+; θ* canonicalization → Cat C target W7+; canonical merge via theorem_status.md update + CHANGELOG.md entry pending Critic review.

---

## §16. Wave 3 Revision Log (W5 Day 4 PM)

**Date**: 2026-04-30. **Trigger**: Critic verdict (logs/daily/2026-04-30/09_critic_re_review_5files.md §3.3) on NQ-189 flagged 4 gaps requiring immediate repair before W6 promotion gating.

### §16.1 Fix 1 — Step 4 irrep-label well-definedness (§3.4)

**Problem**: Prior formulation $k^*(i) = \arg\max_k \|\phi_k|_{B_i}\|^2$ used basin-restricted norm. Critic identified gap: eigenvectors delocalized outside $B_i$ can score large by normalization of the restriction, making the "dominant eigenvector for basin $B_i$" ill-defined in the basin-restriction sense.

**Fix**: Replaced with full-eigenspace inner product: $k^*(i) = \arg\max_k \{\mathrm{Re}\langle \psi_k, \chi_{B_i} \rangle^2\}$ where $\psi_k$ are eigenvectors of $H(u^*)$ on the full space $\mathbb{R}^n$ and $\chi_{B_i}$ is the basin indicator function. Added explicit rationale paragraph explaining why full-eigenspace projection is well-posed where basin restriction is not. Tie-break: lex order in $(n_k, [\rho_k])$ Mulliken order.

**Assessment**: Straightforward once the geometric issue was identified. The inner-product formulation is standard in spectral geometry (projection onto subspace indicator); no new mathematical machinery required.

### §16.2 Fix 2 — Step 2 circular σ-tie-break (§3.2)

**Problem**: Prior tie-break invoked "σ-irrep-based further tie-break (Mulliken character order)" — circular because Step 4 irrep labels are computed *after* the basin partition produced by Step 2. Using Step 4 output to resolve Step 2 ambiguity breaks the sequential dependency of the 5-step procedure.

**Fix**: Replaced with 3-level graph-intrinsic rule: (1) smaller graph distance from the contested vertex's neighbor to its peak; (2) lex-smaller peak vertex index; (3) smaller peak graph distance to fiducial node $x_0$ (lex-smallest node). Added explicit circularity diagnosis in the text.

**Assessment**: Required interpretation — the task specified "lex order, distance" but left the exact 3-level cascade implicit. The cascade order chosen (distance-to-peak first, lex index second, distance-to-fiducial third) is the most natural from Voronoi/gradient-flow theory (distance-primary) with lex as a pure tie-breaker.

### §16.3 Fix 3 — §4.3 Cat A conditionality (§4.3)

**Problem**: The Cat A theorem candidate stated disjoint-support as a hypothesis without flagging the regime split: Cat A applies under disjoint support (generically satisfied by multi.py minimizers with $\lambda_{\mathrm{rep}} > 0$), but Cat B applies for generic overlap.

**Fix**: Inserted a blockquote above the theorem candidate explicitly labeling "Cat A (conditional)" with the disjoint-support hypothesis, citing canonical CN5 + working/MF/multi_formation_sigma.md for the generic applicability argument, and naming NQ-242 PH pipeline as the Cat B target for the overlap regime (W6+).

**Assessment**: Straightforward insertion. No change to the theorem candidate itself; the conditionality was implicit in the proof sketch's hypothesis — this fix makes it explicit at the status-label level.

### §16.4 Fix 4 — §7.2 inf → sup (§7.2)

**Problem**: Line 238 defined $\theta^*$ as $\inf\{\theta : K_{\mathrm{step}} = \mathcal{F}\}$ but line 243 described $\theta^*$ as the "highest threshold" — a direct contradiction. inf gives the *first* threshold at which $\mathcal{F}$ components appear (from below); sup gives the *last* stable threshold before components erode (from above).

**Fix**: Replaced inf with sup throughout §7.2. Added a dedicated "Choice of sup over inf" paragraph explaining: (a) the relevant set is an interval $[\theta_{\mathrm{lo}}, \theta^*]$; (b) sup gives the tightest individuation that still separates all $\mathcal{F}$ peaks; (c) inf ($= \theta_{\mathrm{lo}}$) gives a looser, less informative boundary. Updated the Properties bullet to correctly describe $\theta^*$ as the last stable point before component erosion.

**Assessment**: Required the most careful interpretation. The "highest threshold" description in the Properties bullet was the correct intended meaning; the inf definition was the error. The PH connection in §7.2 (death threshold of lowest-persistence $H_0$ bar) is consistent with the sup interpretation — the death threshold is exactly the sup of thresholds for which that bar's component survives, confirming the fix.

### §16.5 Bonus addition — NQ-189 ↔ NQ-253 static-dynamic correspondence (§3.7)

Added §3.7 to the 5-step procedure section cross-referencing NQ-253 (formation_birth_string_breaking.md). Established the static-dynamic σ↔crisp correspondence: NQ-189 handles the static snapshot recovery; NQ-253 handles the dynamic K-jump trajectory. Together they form the complete σ↔crisp framework required for multi-formation Paper 1 treatment.
