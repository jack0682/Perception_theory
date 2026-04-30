# schramm_sigma_locality_theorem.md — σ-Framework Locality Theorem at First Pitchfork

**Status:** Working — Cat BC target candidate (σ-tuple locality at first pitchfork via local automorphism stabilizer + irrep-compatible isomorphism).
**Spawned:** W5 Day 4 PM Wave 3 (2026-04-30) — Bridge B-2 deep-research extension (`working/MF/foundational_bridges_2026.md` §3).
**Author origin:** scc-wave3-deep-research team commission (NQ-262 detailed development; Hutchcroft–Easo 2023 percolation locality structural parallel).
**Canonical refs:** §13 T-PreObj-1G (Theorem 2-G); §13 T-σ-Theorem-3 (closed-form Hessian on uniform); §13 T-σ-Theorem-4 (first pitchfork σ-tuple); §13 T-σ-Lemma-1 ($\mathrm{Aut}(G)$-orbit invariance); §11.1 Commitment 14 (σ-tuple ordering O5')(O7); §11.1 Commitment 17 (proposed Tool A2 quotient promotion).
**Working refs:** `working/MF/foundational_bridges_2026.md` §3 Bridge B-2; `working/SF/sigma_uniqueness_theorem.md` §2 Definition 2.1' (canonical conjugation rule); `working/MF/mathematical_scaffolding_4tools.md` Tool A2 (quotient + irrep decomposition); `working/SF/symmetry_moduli.md` §3.3 ($D_4$ axis-aligned cubic ratio).
**External refs:** Hutchcroft, T. & Easo, P. (2023). *"Locality of percolation thresholds."* arXiv:2310.10983 (verification status ⚠️ pending per `foundational_bridges_2026.md` §12.2). Schramm, O. (early 2000s, conjecture statement, communicated). Serre 1977, *Linear Representations of Finite Groups*. Sattinger 1979, *Group Theoretic Methods in Bifurcation Theory*.

**Hard constraints (CN10 + canonical promotion):**
- Direct canonical edits: 0. This file is a W6+ promotion candidate, not a §13 entry yet.
- σ-tuple locality is SCC-intrinsic Hessian-spectral mathematics (CN10 contrastive vs percolation theory).
- Open problems (F-1, M-1, MO-1) are NOT silently resolved.
- 4-energy decomposition not merged.
- $u_t : X_t \to [0,1]$ primitive maintained throughout.

---

## §1. Mission

**Goal.** Prove a Cat BC theorem in the σ-framework that mirrors the **Schramm locality conjecture** (Hutchcroft–Easo 2023 arXiv:2310.10983 in percolation): namely, that the σ-tuple at the first pitchfork bifurcation depends only on the **local automorphism stabilizer structure** at the would-be uniform minimizer, not on the global topology of the underlying graph.

**Slogan.** *"Local stabilizer + irrep structure ⇒ first-pitchfork σ-tuple."* The first-pitchfork bifurcation surface in σ-space is a **locality property**: graphs sharing isomorphic stabilizer + compatible irrep structure share their first-pitchfork σ-tuple modulo canonical conjugation (Definition 2.1' from `sigma_uniqueness_theorem.md` §2).

**Why it matters.** σ-tuples are the §11.1 Commitment 14 invariants designating "formation identity". A locality theorem on σ-tuples shows that the σ-framework's discriminative power is **graph-class-independent at the local-stabilizer level** — paralleling Theorem 2-G's graph-class-independence at the pre-objective mechanism level (T-PreObj-1G, Cat A). Just as percolation $p_c$ is local in finite-ball structure (Hutchcroft–Easo 2023), the SCC first-pitchfork σ-tuple is local in stabilizer + irrep structure.

**CN10.** SCC is **not** percolation theory. The structural parallel is methodological (locality bridge); subject matter is intrinsically distinct (Hessian-spectral σ-tuples vs critical edge probabilities).

---

## §2. Statement of theorem (Cat BC target)

> **T-σ-Schramm-Locality (NQ-262 candidate, single-formation, Cat BC target).** Let $G_1 = (X_1, E_1)$ and $G_2 = (X_2, E_2)$ be two finite connected graphs admitting would-be uniform critical minimizers $u_1^* = c \cdot \mathbf{1}_{X_1}$ and $u_2^* = c \cdot \mathbf{1}_{X_2}$ at common spinodal-interior $c \in ((3-\sqrt{3})/6, (3+\sqrt{3})/6)$ and shared parameter $\alpha > 0$. Assume hypotheses (G1)–(G4) of Theorem 2-G (T-PreObj-1G) hold for both. Suppose there exists a group isomorphism
> $$\varphi: \mathrm{Aut}(G_1)_{u_1^*} \xrightarrow{\;\cong\;} \mathrm{Aut}(G_2)_{u_2^*}$$
> of local automorphism stabilizers (Definition 3.1) that is **irrep-compatible** (Definition 3.3) with respect to the natural action on $T_{u_1^*}\Sigma_m^{(1)} = \mathbf{1}_{X_1}^\perp$ and $T_{u_2^*}\Sigma_m^{(2)} = \mathbf{1}_{X_2}^\perp$.
>
> Then at the first pitchfork bifurcation $\beta_1 = \beta_{\mathrm{crit}}^{(2)}(G_1) + \epsilon$ and $\beta_2 = \beta_{\mathrm{crit}}^{(2)}(G_2) + \epsilon$ (matched $\epsilon > 0$ small), the σ-tuples agree under canonical conjugation:
> $$\sigma\big(u_{1, \mathrm{pitchfork}}^*\big) \equiv \sigma\big(u_{2, \mathrm{pitchfork}}^*\big) \quad \text{(per NQ-188 §2 Definition 2.1' canonical conjugation rule).}$$

**Status decomposition:**
- **Cat A** (definitional, conditional): given Definition 2.1' and irrep-compatibility hypothesis, the structural identification of first-pitchfork σ-tuples is forced by Schur orthogonality on the smallest-eigenvalue eigenspace.
- **Cat B** (target): the existence of $\beta_{\mathrm{crit}}^{(2)}$ matching across graphs and the irrep-compatibility ↔ first-pitchfork-irrep correspondence must be verified beyond the closed-form $D_4$ free-BC case.
- **Cat C** (graph-class lift): full Cat A would require (a) graph-class independence of T-σ-Theorem-3 (currently Cat A on uniform $D_4$ free-BC; generalization open), (b) Tool A2 quotient promotion at CV-1.6 via Commitment 17 (proposed).

---

## §3. Definitions

**Definition 3.1 (Local automorphism stabilizer).** For a finite connected graph $G$ admitting a critical point $u^* \in \Sigma_m \subset [0,1]^X$,
$$\mathrm{Aut}(G)_{u^*} := \{\pi \in \mathrm{Aut}(G) : \pi \cdot u^* = u^*\}$$
is the subgroup of graph automorphisms fixing $u^*$ pointwise. For $u^* = c \cdot \mathbf{1}$, $\mathrm{Aut}(G)_{u^*} = \mathrm{Aut}(G)$ (uniform fields are fixed by all automorphisms by definition of permutation action).

**Examples.**
- $G = D_4$ free-BC $L \times L$ grid, $u^* = c\mathbf{1}$: $\mathrm{Aut}(G)_{u^*} = D_4$ (8 elements).
- $G = C_n$ cycle, $u^* = c\mathbf{1}$: $\mathrm{Aut}(G)_{u^*} = D_n$ (dihedral, $2n$ elements).
- $G = T^2_{n \times n}$ torus, $u^* = c\mathbf{1}$: $\mathrm{Aut}(G)_{u^*} = (\mathbb{Z}_n \times \mathbb{Z}_n) \rtimes D_4$.

**Definition 3.2 (Tangent-space representation).** The stabilizer $\mathrm{Aut}(G)_{u^*}$ acts on the tangent space $T_{u^*}\Sigma_m = \mathbf{1}^\perp \subset \mathbb{R}^X$ via coordinate permutation: $(\pi \cdot v)_i = v_{\pi^{-1}(i)}$. Per T-σ-Lemma-1 (i), this action commutes with the constrained Hessian $H(u^*) = \pi_{\mathbf{1}^\perp} \nabla^2 \mathcal{E}(u^*) \pi_{\mathbf{1}^\perp}$, so each Hessian eigenspace decomposes into $\mathrm{Aut}(G)_{u^*}$-isotypic components (T-σ-Lemma-1 (ii)).

**Definition 3.3 (Irrep-compatible isomorphism).** Let $\varphi: \mathrm{Aut}(G_1)_{u_1^*} \xrightarrow{\cong} \mathrm{Aut}(G_2)_{u_2^*}$ be a group isomorphism. We say $\varphi$ is **irrep-compatible** if there exists a linear isomorphism
$$\Phi: T_{u_1^*}\Sigma_m^{(1)} \xrightarrow{\;\cong\;} T_{u_2^*}\Sigma_m^{(2)}$$
satisfying:

- **(IC1) Equivariance.** $\Phi(\pi \cdot v) = \varphi(\pi) \cdot \Phi(v)$ for all $\pi \in \mathrm{Aut}(G_1)_{u_1^*}$ and $v \in T_{u_1^*}\Sigma_m^{(1)}$.
- **(IC2) Hessian intertwining.** $\Phi \circ H(u_1^*) = H(u_2^*) \circ \Phi$ at the uniform Hessian (Prop 1.3a closed form $H(c\mathbf{1}) = 4\alpha L_G + \beta W''(c) I$).
- **(IC3) Irrep-multiplicity matching.** For each irrep $[\rho] \in \widehat{\mathrm{Aut}(G_1)_{u_1^*}}$ and corresponding $[\varphi_*\rho] \in \widehat{\mathrm{Aut}(G_2)_{u_2^*}}$, the multiplicities in the smallest non-volume eigenspace agree: $m_{[\rho]}(V_1^{\min}) = m_{[\varphi_*\rho]}(V_2^{\min})$, where $V_i^{\min} := \ker(H(u_i^*) - \mu_2(G_i, c, \alpha, \beta) I)|_{\mathbf{1}^\perp}$ is the lowest non-volume Hessian eigenspace at $u_i^*$.

*Remark.* (IC3) is the heart of irrep-compatibility: it forces the **first-pitchfork eigenvector irrep label** to coincide between $G_1$ and $G_2$. Combined with T-σ-Theorem-3 (Hessian spectrum closed-form on uniform) and T-σ-Theorem-4 (post-pitchfork σ-tuple structure), this propagates to σ-tuple agreement.

*Schur-degenerate case.* When $V_i^{\min}$ contains a multi-dimensional irrep summand (e.g., $D_4$ E-irrep on the $(1,0)/(0,1)$ doublet at $L = 4$), Definition 2.1' clause (c) (`sigma_uniqueness_theorem.md` §2) absorbs the basis-choice ambiguity: only the **isomorphism class** of $[\rho]$ is required to match, not a specific basis. Schur's Lemma (Serre 1977 §2.2) ensures basis-independence of the multiplicity count $m_{[\rho]}$.

---

## §4. Proof outline

The proof proceeds in five steps via Tool A2 quotient + irrep decomposition.

**Step 1 — Pre-objectivity and uniform criticality (graph-class-independent).**

By T-PreObj-1G (canonical §13, W4-04-24, Cat A), under hypotheses (G1)–(G4) the pre-objective mechanism holds on **any finite connected graph**. In particular, for $u_i^* = c\mathbf{1}_{X_i}$ in the spinodal interior with $c$ at the uniform critical point, the variational structure (KKT first-order condition + Hessian decomposition) is identical in form on both $G_1$ and $G_2$. The only graph-dependent quantity entering is the Laplacian eigenvalue spectrum $\{\lambda_k^{\mathrm{Lap}}(G_i)\}$.

**Step 2 — Closed-form Hessian spectrum at uniform.**

By T-σ-Theorem-3 (canonical §13, W5 Day 1, Cat A on $D_4$ free-BC; **graph-class lift Cat C target** for general $G$), the constrained Hessian at $u_i^* = c\mathbf{1}$ takes the form
$$H(c\mathbf{1}_{X_i}) = 4\alpha L_{G_i} + \beta W''(c) I \quad \text{on } \mathbf{1}_{X_i}^\perp,$$
with eigenvalues
$$\mu_k(G_i) = 4\alpha \lambda_k^{\mathrm{Lap}}(G_i) + \beta W''(c), \qquad k = 2, 3, \ldots, |X_i|,$$
and Hessian eigenvectors coinciding with Laplacian eigenvectors on $\mathbf{1}_{X_i}^\perp$ (Prop 1.3a). The smallest non-volume eigenvalue is $\mu_2(G_i) = 4\alpha \lambda_2^{\mathrm{Lap}}(G_i) + \beta W''(c)$, governing the first pitchfork crossing $\beta_{\mathrm{crit}}^{(2)}(G_i) = 4\alpha \lambda_2^{\mathrm{Lap}}(G_i) / |W''(c)|$.

*Caveat (Cat C lift).* T-σ-Theorem-3 is currently Cat A on $D_4$ free-BC. Generalization to arbitrary finite connected $G$ requires either (a) direct verification on each graph class (e.g., $C_n$, $T^d$, complete graphs), or (b) a graph-class-independent restatement based on Prop 1.3a structure alone (which generalizes verbatim because $H(c\mathbf{1}) = 4\alpha L_G + \beta W''(c) I$ uses no graph-specific structure beyond the Laplacian). The latter is the **CV-1.6 promotion target** — see §6.

**Step 3 — Tool A2 quotient + isotypic decomposition.**

By T-σ-Lemma-1 + Tool A2 (`mathematical_scaffolding_4tools.md` §4 — proposed Commitment 17), the tangent space $T_{u_i^*}\Sigma_m^{(i)}$ decomposes canonically into $\mathrm{Aut}(G_i)_{u_i^*}$-isotypic components:
$$T_{u_i^*}\Sigma_m^{(i)} = \bigoplus_{[\rho] \in \widehat{\mathrm{Aut}(G_i)_{u_i^*}}} V^{(i), [\rho]},$$
where $V^{(i), [\rho]} = P_{[\rho]} T_{u_i^*}\Sigma_m^{(i)}$ via the standard isotypic projector $P_{[\rho]} = \frac{\dim \rho}{|G_u|} \sum_{\pi} \overline{\chi_\rho(\pi)} \pi$ (Serre 1977 §2.6).

**The smallest-eigenvalue eigenspace at criticality determines the first pitchfork.** Specifically, $V_i^{\min} := \ker(H(u_i^*) - \mu_2(G_i) I) |_{\mathbf{1}^\perp}$ is the eigenspace whose Hessian eigenvalue first crosses zero as $\beta \to \beta_{\mathrm{crit}}^{(2)}(G_i)^+$. By T-σ-Theorem-4 (canonical §13, W5 Day 1, Cat A on $D_4$ free-BC; generalization conditional), the post-bifurcation minimizer $u_{i, \mathrm{pitchfork}}^* = c\mathbf{1} + a_\epsilon \phi_{\min}^{(i)} + O(\epsilon)$ has its symmetry breaking pattern governed by the irrep decomposition of $V_i^{\min}$.

**Step 4 — Irrep-compatibility forces first-pitchfork irrep agreement.**

Suppose $\varphi$ is an irrep-compatible isomorphism (Definition 3.3). Then by (IC1)+(IC2), $\Phi$ maps the lowest non-volume eigenspace of $H(u_1^*)$ onto the lowest non-volume eigenspace of $H(u_2^*)$:
$$\Phi(V_1^{\min}) = V_2^{\min}.$$
By (IC1) equivariance, this map intertwines the $\mathrm{Aut}(G_1)_{u_1^*}$ action with the $\varphi$-pushforward $\mathrm{Aut}(G_2)_{u_2^*}$ action. By Schur orthogonality (Serre 1977 §2.4),
$$V_1^{\min} = \bigoplus_{[\rho]} V_1^{\min, [\rho]} \xrightarrow{\;\Phi\;} V_2^{\min} = \bigoplus_{[\rho']} V_2^{\min, [\rho']}$$
preserves isotypic decomposition: $\Phi(V_1^{\min, [\rho]}) = V_2^{\min, [\varphi_* \rho]}$. By (IC3), the multiplicities $m_{[\rho]}(V_1^{\min}) = m_{[\varphi_* \rho]}(V_2^{\min})$ match.

Hence the **first-pitchfork irrep labels agree**: the irrep that becomes critical (smallest-eigenvalue irrep) is the same on both graphs modulo the conjugation $\varphi_*$.

**Step 5 — σ-tuple agreement at first pitchfork.**

By T-σ-Theorem-4 (v) (canonical §13), the σ-tuple at first pitchfork is determined by:
1. $\mathcal{F}(u_{i, \mathrm{pitchfork}}^*) \in \{0, 1\}$ depending on tie-breaking convention (NQ-143/NQ-184). On both graphs, the same convention applied to a structurally matched bifurcation gives the same $\mathcal{F}$ value.
2. The leading-order eigenvalue multiplicities, which by Step 4 match: each entry $(n_k, [\rho_k], \lambda_k)$ at $k \in \{0, 1\}$ depends only on the irrep structure of $V_i^{\min}$, which is preserved by $\Phi$.
3. Higher-mode tail $\mu_k(c\mathbf{1}) + O(\sqrt{\epsilon})$ at $k \geq 4$: matches because (IC2) extends to all eigenspaces (the full Hessian intertwines, not just the first eigenspace; (IC2) is stated on the full $H(c\mathbf{1})$).

Applying canonical conjugation rule Definition 2.1' (`sigma_uniqueness_theorem.md` §2):
- (a) $\varphi^{-1} \mathrm{Aut}(G_1)_{u_1^*} \varphi = \mathrm{Aut}(G_2)_{u_2^*}$ (by isomorphism hypothesis).
- (b) Irrep labels translate under $\varphi$ via (IC1) Schur-orthogonality.
- (c) Schur-degenerate eigenspaces (e.g., $D_4$ E-irrep doublet at $L = 4$) are preserved as isomorphism classes by Definition 3.3 (IC3).
- (d) Mulliken-order convention picks the lex-smallest $\varphi$ when non-unique, ensuring decidability.

Therefore $\sigma(u_{1, \mathrm{pitchfork}}^*) \equiv \sigma(u_{2, \mathrm{pitchfork}}^*)$ per Definition 2.1'. $\Box$

---

## §5. Hypotheses needed

**Inherited from T-PreObj-1G (canonical §13).**

- **(G1)** Pure $\mathcal{E}_{\mathrm{bd}}$ admits a non-uniform critical point on $\Sigma_m$ for both $G_1$ and $G_2$.
- **(G2)** $\mathrm{Cl}$ is a contraction with unique fixed point $c^* \mathbf{1}$ ($a_{\mathrm{cl}} \in (0, 4)$).
- **(G3)** $D$ takes the canonical sigmoid form.
- **(G4)** $u_0^*$ is non-constant (ensures bifurcation theory non-trivial).

**Theorem-specific.**

- **(SH1) Spinodal interior.** $c \in ((3-\sqrt{3})/6, (3+\sqrt{3})/6)$ with $W''(c) < 0$ (T-σ-Theorem-3 hypothesis discussion).
- **(SH2) First-pitchfork regime.** $\beta_i = \beta_{\mathrm{crit}}^{(2)}(G_i) + \epsilon$ with $\epsilon > 0$ small and matched between $G_1, G_2$.
- **(SH3) Irrep-compatibility.** $\varphi$ satisfies Definition 3.3 (IC1)+(IC2)+(IC3).
- **(SH4) Stabilizer non-triviality.** $\mathrm{Aut}(G_i)_{u_i^*}$ is non-trivial on both graphs (uniform $u^* = c\mathbf{1}$ guarantees this; $\mathrm{Aut}(G_i)_{u_i^*} = \mathrm{Aut}(G_i)$ at uniform).

**Conditional Cat A lift hypotheses.**

- **(SH5) Graph-class-independent T-σ-Theorem-3.** Currently Cat A on $D_4$ free-BC; lift requires direct verification on $C_n$, $T^d$, complete graphs, or a graph-class-independent restatement of Prop 1.3a (CV-1.6 promotion target).
- **(SH6) Tool A2 promotion at CV-1.6 via Commitment 17.** The Tool A2 quotient + irrep decomposition framework (`mathematical_scaffolding_4tools.md`) is currently a working scaffold; canonical promotion via Commitment 17 would lift Step 3 from working to canonical.

---

## §6. Cat target — BC

**Cat BC justification.**

- **Cat A (conditional, definitional).** Given Definition 2.1' (canonical conjugation rule), Definition 3.3 (irrep-compatibility), and graph-class-independent T-σ-Theorem-3 + T-σ-Theorem-4, Steps 1–5 of §4 are forced by Schur orthogonality + Maschke decomposition (standard finite-group representation theory, Serre 1977). The structural identification at first-pitchfork is rigorous **conditional on the irrep-compatibility hypothesis being verifiable**.

- **Cat B (target).** Verifying that for given graph pairs $(G_1, G_2)$ an irrep-compatible $\varphi$ exists, and that the first-pitchfork irrep correspondence is preserved across non-trivial graph-class transitions ($D_4$ ↔ $C_n$ ↔ $T^d$), is an empirical/numerical task. §7 protocol covers this.

- **Cat C (graph-class lift).** Full Cat A would require:
  - **(a) Graph-class independence of T-σ-Theorem-3.** Currently Cat A on uniform $u = c\mathbf{1}$ on $D_4$ free-BC grid. The Hessian formula $H(c\mathbf{1}) = 4\alpha L_G + \beta W''(c) I$ uses *no graph-specific structure* beyond the Laplacian, so the lift is structurally forced; however, formal canonical promotion to "T-σ-Theorem-3-G" (graph-class-independent) is a CV-1.6 candidate.
  - **(b) Tool A2 quotient promotion at CV-1.6 via Commitment 17.** The isotypic decomposition framework (`mathematical_scaffolding_4tools.md` Tool A2) is currently working; canonical promotion via Commitment 17 (proposed) would anchor Step 3.

**Decision.** **Cat BC** target — the structural locality theorem is rigorous given Definitions 2.1' and 3.3 plus T-σ-Theorem-3-G; numerical verification gates promotion to full Cat A.

---

## §7. Numerical verification protocol

**Three-graph-class comparison.** Verify the locality theorem on three structurally distinct graph classes, each with non-trivial uniform stabilizer:

1. **R23 (D₄ free-BC grid, $L = 8$).** $\mathrm{Aut}(G)_{u^*} = D_4$, $|G_u| = 8$. First-pitchfork mode by T-σ-Theorem-4: $\phi_{(1, 0)}/\phi_{(0, 1)}$ doublet, irrep $E$ (2-dim).
2. **$Z_n$ cycle ($n = 20$).** $\mathrm{Aut}(G)_{u^*} = D_{20}$, $|G_u| = 40$. First-pitchfork mode: lowest non-volume Laplacian eigenvector $\phi_1(x) = \cos(2\pi x/n)$ doublet, irrep is the 2-dim $D_{20}$-irrep $E_1$.
3. **$Z_n \times Z_n$ torus ($n = 10$).** $\mathrm{Aut}(G)_{u^*} = (\mathbb{Z}_{10} \times \mathbb{Z}_{10}) \rtimes D_4$, $|G_u| = 800$. First-pitchfork mode: lowest non-volume torus eigenvector doublet $\{\phi_{(1,0)}, \phi_{(0,1)}\}$, 4-dimensional irrep.

**Protocol.**

1. **Compute uniform stabilizer.** For each graph $G$, compute $\mathrm{Aut}(G)_{u^*} = \mathrm{Aut}(G)$ at $u^* = c\mathbf{1}$ via permutation-group enumeration (PyNautyq/SageMath). Record $|G_u|$ and irrep set $\widehat{G_u}$.
2. **Compute first-pitchfork minimizer.** For each $G$, set $\beta = \beta_{\mathrm{crit}}^{(2)}(G) + \epsilon$ with matched $\epsilon = 0.01 \cdot \beta_{\mathrm{crit}}^{(2)}(G)$. Run `find_formation` from random IC near $u^* = c\mathbf{1}$ to obtain $u_{\mathrm{pitchfork}}^*$.
3. **Extract σ-tuple.** Apply `sigma_uniqueness_theorem.md` §5 protocol (steps 1–7) to compute $\sigma(u_{\mathrm{pitchfork}}^*)$.
4. **Test irrep-compatibility.** Pairwise: do there exist $\varphi: G_u^{(1)} \to G_u^{(2)}$ satisfying Definition 3.3? — Note: $D_4 \not\cong D_{20}$ as groups, so direct $\varphi$ existence fails between R23 and $Z_n$ cycle. The test is **negative** — confirming that σ-tuples differ between non-isomorphic stabilizers.
5. **Test isomorphism-class consistency within fixed $G_u$.** Vary the graph topology while preserving $\mathrm{Aut}(G)_{u^*}$ — e.g., $D_4$ free-BC $L = 8$ vs $D_4$ free-BC $L = 16$ vs a $D_4$-symmetric SBM with locally-isomorphic structure. Predict identical first-pitchfork σ-tuple modulo conjugation.
6. **Output.** `CODE/scripts/results/sigma_locality_R23_cycle_torus.json` containing per-graph $(|G_u|, \widehat{G_u}, \mu_2, \beta_{\mathrm{crit}}^{(2)}, \sigma(u_{\mathrm{pitchfork}}^*))$ and pairwise locality-consistency Boolean.

**Implementation outline** (`CODE/scripts/sigma_locality_R23_cycle_torus.py`):

```python
# Schramm-style σ-locality numerical verification at first pitchfork.
# Output: results/sigma_locality_R23_cycle_torus.json

from scc import GraphState, ParameterRegistry, find_formation
from scc.energy import EnergyComputer
import numpy as np
import json

graphs = {
    "R23_D4_L8":    GraphState.grid_2d(8, 8),       # D_4 free-BC
    "cycle_Z20":    GraphState.cycle(20),           # D_20
    "torus_Z10x10": GraphState.torus_2d(10, 10),    # (Z_10)^2 ⋊ D_4
}

results = {}
for name, G in graphs.items():
    p   = ParameterRegistry(alpha=1.0, c_target=0.5, beta=...)  # spinodal interior
    Ec  = EnergyComputer(G, p)
    H   = Ec.constrained_hessian_at_uniform(c=p.c_target)
    spec, vecs = np.linalg.eigh(H)
    mu2 = spec[1]                                       # smallest non-volume eigenvalue
    beta_crit = 4 * p.alpha * mu2_laplacian(G) / abs(W2(p.c_target))
    p.beta = beta_crit + 0.01 * beta_crit               # post-pitchfork ε

    u_star = find_formation(G, p, ic="near_uniform").u
    sigma  = compute_sigma_tuple(u_star, G, p)          # protocol per sigma_uniqueness §5
    aut    = compute_auto_stabilizer(G, u_star)         # SageMath / PyNauty
    results[name] = {
        "|G_u|":         aut.order,
        "irreps":        aut.irreps,
        "mu_2":          mu2,
        "beta_crit_2":   beta_crit,
        "sigma_tuple":   sigma,
    }

# Pairwise irrep-compatibility test
for (n1, n2) in [("R23_D4_L8", "cycle_Z20"),
                 ("R23_D4_L8", "torus_Z10x10"),
                 ("cycle_Z20", "torus_Z10x10")]:
    compat = test_irrep_compatibility(results[n1], results[n2])  # Definition 3.3
    sigma_eq = sigma_equiv_modulo_conjugation(results[n1]["sigma_tuple"],
                                              results[n2]["sigma_tuple"])
    results[f"pair_{n1}_vs_{n2}"] = {
        "irrep_compatible": compat,
        "sigma_equivalent": sigma_eq,
        "locality_holds":   (compat == sigma_eq),
    }

json.dump(results, open("results/sigma_locality_R23_cycle_torus.json", "w"), indent=2)
```

**Falsifiable prediction.**
- $D_4 \not\cong D_{20} \not\cong (\mathbb{Z}_{10} \times \mathbb{Z}_{10}) \rtimes D_4$ ⇒ pairwise σ-tuples **differ** at first pitchfork.
- Within a fixed stabilizer class (e.g., $D_4$ free-BC at varying $L$): σ-tuples **agree modulo conjugation**.
- Locality predicate `(irrep_compatible == sigma_equivalent)` holds across all 3 pairs ⇒ Cat B verification.

---

## §8. Connection to Hutchcroft–Easo

| Hutchcroft–Easo 2023 (percolation locality) | T-σ-Schramm-Locality (this file) |
|---|---|
| $p_c(G)$ = critical edge probability | $\sigma(u_{\mathrm{pitchfork}}^*)$ = first-pitchfork σ-tuple |
| Locality: $G_1, G_2$ locally isomorphic ⇒ same $p_c$ | Locality: $\mathrm{Aut}(G_1)_{u_1^*} \cong \mathrm{Aut}(G_2)_{u_2^*}$ via irrep-compatible $\varphi$ ⇒ same σ-tuple modulo conjugation |
| "Local" = same finite ball up to large radius | "Local" = isomorphic stabilizer + irrep-multiplicity match in lowest eigenspace |
| Proved for transitive graphs (Hutchcroft–Easo 2023) | Cat BC target on finite connected graphs under (G1)–(G4) + (SH1)–(SH3) |
| Conjecture by Schramm (early 2000s) | NQ-262 candidate (W6, 4–6 weeks) |

**CN10 status.** **SCC is not percolation theory.** The structural parallel is methodological: percolation locality says "graph-class-invariant critical thresholds depend only on local structure"; σ-locality says "graph-class-invariant first-pitchfork σ-tuples depend only on local stabilizer + irrep structure." The two results share *spirit* (locality of a critical invariant) but **subject matter differs**: percolation studies edge-occupation probability cluster transitions; SCC studies cohesion-field bifurcations. No theorem is borrowed. The bridge is structural/methodological inspiration only.

**Differences from Hutchcroft–Easo.**
1. Hutchcroft–Easo proves locality on **transitive infinite graphs**; T-σ-Schramm-Locality targets **finite connected graphs** (CN10 — SCC primitive is finite-graph soft cohesion).
2. Hutchcroft–Easo uses combinatorial-probabilistic arguments (random graph percolation theory); T-σ-Schramm-Locality uses representation-theoretic + bifurcation-theoretic arguments (Schur orthogonality + equivariant Crandall–Rabinowitz).
3. Hutchcroft–Easo: locality is at the edge-density level. T-σ-Schramm-Locality: locality is at the σ-tuple level (multi-coordinate Hessian-spectral invariant).

---

## §9. W6+ priority

**Bridge B-2 numerical verification — Task #23 (claim post-this-file).**

| Item | Description | W-band | Effort |
|---|---|---|---|
| **NQ-262** | T-σ-Schramm-Locality canonical target | W6 | 4–6 weeks |
| Step 1 | §7 protocol implementation (`sigma_locality_R23_cycle_torus.py`) | W6 Day 1–3 | 3 days |
| Step 2 | R23 ($D_4$, $L=8$) + cycle ($Z_{20}$) + torus ($Z_{10} \times Z_{10}$) σ-tuple extraction | W6 Day 4–8 | 5 days |
| Step 3 | Pairwise irrep-compatibility test + locality predicate verification | W6 Day 9–10 | 2 days |
| Step 4 | T-σ-Theorem-3-G graph-class lift (CV-1.6 promotion target) | W7 | 2 weeks |
| Step 5 | Tool A2 + Commitment 17 promotion at CV-1.6 | W7+ | 2–3 weeks |

**Cat target:** **BC** (definitional locality + numerical verification). Effort: **4–6 weeks**.

**Promotion gate.** Lift to Cat A requires:
- (a) T-σ-Theorem-3-G canonical lift (currently Cat C target).
- (b) Tool A2 + Commitment 17 canonical promotion at CV-1.6.
- (c) §7 numerical verification across at least 3 graph classes with locality predicate satisfied.

---

## §10. Hard constraint check

- [x] **$u_t : X_t \to [0,1]$ primitive maintained.** Soft cohesion field is the primitive; σ-tuple is a *derived* Hessian-spectral invariant computed at minimizers. No replacement of $u_t$ by external apparatus.
- [x] **CN10 contrastive vs percolation theory.** §8 explicitly distinguishes: "SCC is not percolation theory." Bridge is methodological (locality spirit), not subject matter (no theorems borrowed; Hessian-spectral σ-tuples ≠ critical edge probabilities).
- [x] **CN5 4-energy decomposition not merged.** $\mathcal{E} = \lambda_{\mathrm{cl}} \mathcal{E}_{\mathrm{cl}} + \lambda_{\mathrm{sep}} \mathcal{E}_{\mathrm{sep}} + \lambda_{\mathrm{bd}} \mathcal{E}_{\mathrm{bd}} + \lambda_{\mathrm{tr}} \mathcal{E}_{\mathrm{tr}}$ structure is preserved; T-σ-Theorem-3 closed-form Hessian uses the full $\mathcal{E}$ at uniform with $\mathcal{E}_{\mathrm{cl}}, \mathcal{E}_{\mathrm{sep}}, \mathcal{E}_{\mathrm{bd}}$ contributions kept distinct.
- [x] **F-1 / M-1 / MO-1 not silently resolved.** F-1 (W4 split-resolved per T-Merge (b) + T-PreObj-1 (i)) is referenced as inherited resolution; M-1 (W4 layer-clarified) is not invoked; MO-1 sidestepped for single-formation σ scope (multi-formation extension via $\mathrm{Aut}(G) \wr S_{K_{\mathrm{act}}}$ deferred to W7+, OP-0008/OP-0009).
- [x] **No re-introduction of Research OS structure.** Single working file per topic per CLAUDE.md policy. No 5-role daily-log mapping.
- [x] **Direct canonical edits: 0.** This file is a W6+ promotion candidate; canonical §13 entries are not modified.
- [x] **No silent resolution of OP-0005 K-Selection.** K-selection mechanism (multi-formation regime) is outside single-formation σ-locality scope. Multi-formation locality extension noted as W7+ deferred (§9 Step 5).
- [x] **K_field/K_act decomposition respected** (Commitment 16). Single-formation regime $K_{\mathrm{field}} = K_{\mathrm{act}} = 1$ throughout this theorem.

---

## §11. References

**Canonical (§13 anchors, post-CV-1.5.1).**
- T-PreObj-1G (canonical §13, line ~1123). Pre-Objective Mechanism — Graph-Class Independent Generalization. Cat A (qualitative).
- T-σ-Theorem-3 (canonical §13, lines 1334–1375). σ at Uniform on $D_4$ Free-BC Grid (Closed Form). Cat A on $D_4$; graph-class lift Cat C target.
- T-σ-Theorem-4 (canonical §13, lines 1377–1399). σ at First Pitchfork on $D_4$ Free-BC Grid (Leading Order). Cat B (Critic verdict, retroactive 2026-04-29).
- T-σ-Lemma-1 (canonical §13, lines 1257–1275). σ-Framework Irrep Decomposition Well-Defined. Cat A.
- T-σ-Lemma-2 (canonical §13, lines 1277–1299). σ-Framework Nodal Count Properties. Cat A (i)–(iv); Cat C (v)–(vi) general; Cat A (v) balanced-Laplacian.
- §11.1 Commitment 14 + (O5')(O7) ordering conventions (CV-1.5.1, 2026-04-29).
- §11.1 Commitment 17 (proposed) — Tool A2 quotient promotion at CV-1.6.
- §14 CN10 Contrastive vs Reductive — invoked in §8 percolation distinction.

**Working files.**
- `working/MF/foundational_bridges_2026.md` §3 Bridge B-2 (NQ-262 candidate originator). Status: working draft, W5 Day 4 PM Wave 3.
- `working/SF/sigma_uniqueness_theorem.md` §2 Definition 2.1' (canonical conjugation rule, NQ-188 §2). W5 Day 4 PM Wave 3 revision.
- `working/MF/mathematical_scaffolding_4tools.md` Tool A2 (quotient + irrep decomposition). Working scaffold for §3 Step 3 + §6 Cat C lift.
- `working/SF/symmetry_moduli.md` §3.3 ($D_4$ axis-aligned cubic ratio $A_2/A_1 = 4$). Cat A.
- `working/SF/sigma_lie_algebra_structure.md` §4 (σ-tuple as $\mathrm{Aut}(G)_{u^*}$-irrep decomposition). Working file.

**External.**
- **Hutchcroft, T. & Easo, P. (2023).** *"Locality of percolation thresholds on graphs."* arXiv:2310.10983. ⚠️ citation status pending verification per `foundational_bridges_2026.md` §12.2; verify at NQ-262 promotion gate.
- **Schramm, O.** (early 2000s, conjecture statement, communicated). The original Schramm locality conjecture for percolation thresholds.
- **Serre, J.-P. (1977).** *Linear Representations of Finite Groups.* Springer GTM 42. §2.4 Schur orthogonality; §2.6 isotypic projectors. Foundation for §3 Step 3, §4 Step 4.
- **Sattinger, D. H. (1979).** *Group Theoretic Methods in Bifurcation Theory.* Springer LNM 762. Equivariant Crandall–Rabinowitz; foundation for first-pitchfork analysis (T-σ-Theorem-4 setup).

---

## §12. Wave 3 Provenance Log (W5 Day 4 PM, 2026-04-30)

**Created:** Wave 3 dispatch via scc-wave3-deep-research team commission (executor agent under team-lead coordination), 2026-04-30.

**Status:** working draft. Cat BC target. NQ-262 detailed scaffolding. 0 canonical edits.

**Inheritance.**
- Inherits T-PreObj-1G (W4-04-24, Cat A) graph-class-independence framing.
- Inherits T-σ-Theorem-3 + T-σ-Theorem-4 (W5 Day 1, Cat A on $D_4$ free-BC) closed-form Hessian + first-pitchfork σ-tuple structure.
- Inherits T-σ-Lemma-1 ($\mathrm{Aut}(G)$-orbit invariance, W5 Day 1, Cat A) representation-theoretic framework.
- Inherits Definition 2.1' canonical conjugation rule (`sigma_uniqueness_theorem.md` §2 W5 Day 4 PM Wave 3 revision).

**Bridge mapping.** Bridge B-2 (`foundational_bridges_2026.md` §3) Schramm locality → T-σ-Schramm-Locality. NQ-262 (HIGH priority, W6, 4–6 weeks).

**Promotion target:** W7+ canonical §13 candidate entry "T-σ-Schramm-Locality" subject to (a) T-σ-Theorem-3-G graph-class lift, (b) Tool A2 + Commitment 17 CV-1.6 promotion, (c) §7 numerical verification across 3 graph classes.

---

**End of working file.** Promotion pipeline next stage: §7 protocol execution (`CODE/scripts/sigma_locality_R23_cycle_torus.py`) → empirical 3-graph-class verification → W7 T-σ-Theorem-3-G lift + Commitment 17 CV-1.6 promotion → W7+ canonical §13 candidate "T-σ-Schramm-Locality."
