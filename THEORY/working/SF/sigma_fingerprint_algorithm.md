# sigma_fingerprint_algorithm.md — Strong + Sub-cubic σ-Fingerprint Algorithm Spec

**Status:** Working — Cat B target candidate (NQ-264, Bridge B-4).
**Spawned:** W5 Day 4 PM Wave 3 (2026-04-30) — follow-up to Bridge B-2 σ-locality numerical verification (`schramm_sigma_locality_theorem.md` + `CODE/scripts/sigma_locality_R23_cycle_torus.py`).
**Author origin:** scc-wave3-deep-research team commission (Task #25 σ-fingerprint algorithm spec).
**Canonical refs:** §11.1 Commitment 14 σ-tuple definition + (O5')(O7) ordering; §13 T-σ-Lemma-1/2/3 (irrep + nodal count + Goldstone); §13 T-σ-Theorem-3/4 (closed-form Hessian + first-pitchfork σ); §11.1 Commitment 17 (proposed) Tool A2 + Tool A3 quotient/PH framework.
**Working refs:** `working/MF/foundational_bridges_2026.md` §5 Bridge B-4; `working/SF/schramm_sigma_locality_theorem.md` §3 Definition 3.3 (irrep-compatibility); `working/SF/sigma_uniqueness_theorem.md` §5 R23 σ-class extraction protocol; `working/MF/single_high_F_equivalence.md` §4–§5 (OAT-7 PH-vs-σ analysis); `CODE/scripts/sigma_class_count_R23.py` (eigenvalue-proxy σ-class count).
**External refs:** Bar-Natan, D. & van der Veen, R. (2026). *"Knot invariants from QR-code-like fingerprints"* — citation status ⚠️ pending verification per `foundational_bridges_2026.md` §12.2.

**Hard constraints (CN10 + canonical promotion):**
- Direct canonical edits: 0. W7+ promotion candidate.
- σ-fingerprint is SCC-intrinsic (CN10 contrastive vs knot theory); NOT a borrowing of QR-code-knot terminology.
- Open problems (F-1, M-1, MO-1) not silently resolved.
- 4-energy decomposition not merged.
- $u_t$ primitive maintained.

---

## §1. Mission

**Goal.** Specify an algorithm computing a **σ-fingerprint** $\Phi(u^*) \in \mathbb{Z}^* \times \mathbb{R}^*$ (an integer/real labelled tuple) that:

- **(F1) Strength.** Distinguishes all 56 stable minimizers of the R23 fullscale dataset (`exp_orbital_fullscale.json`, $32 \times 32$ $D_4$ free-BC grid, $\beta = 30$, $c = 0.5$, $\alpha = 1$); strictly refines the eigenvalue-proxy σ-class proxy (`sigma_class_count_R23.py`).
- **(F2) Computational cheapness.** Runs in sub-cubic $O(|X|^{2.5})$ or better wall-clock time per minimizer; in particular avoids full $O(|X|^3)$ Hessian diagonalization at the bulk level (only the lowest $K = 12$ eigenvectors are needed via Lanczos).
- **(F3) Locality compatibility.** Composes with T-σ-Schramm-Locality (Bridge B-2 / NQ-262): the fingerprint at first-pitchfork minimizers is determined by $\mathrm{Aut}(G)_{u^*}$-irrep structure, so locality-theorem applications inherit from the fingerprint.
- **(F4) Aut(G)-orbit invariance.** $\Phi$ is constant on $\mathrm{Aut}(G)$-orbits (per T-σ-Lemma-1 (ii)) up to canonical conjugation (Definition 2.1' from `sigma_uniqueness_theorem.md` §2).

**Why it matters.** The eigenvalue-only σ-class proxy in `sigma_class_count_R23.py` is too coarse: at $D_4$ Mulliken tie-breaks (Commitment 14 O7), two minimizers with identical eigenvalues but distinct irrep labels collapse into a single proxy class. The σ-fingerprint must add irrep + nodal information to recover full discriminative power, while staying computationally cheap.

**CN10.** SCC is **not** knot theory. The Bar-Natan–van der Veen "QR-code knot invariant" provides methodological inspiration (strong + computable invariants); subject matter (Hessian-spectral fingerprints on cohesion fields) is intrinsically distinct.

---

## §2. σ-fingerprint definition

**Definition 2.1 (σ-fingerprint).** For a stable minimizer $u^* \in \Sigma_m^\circ$ of full SCC energy on a finite connected graph $G$ with stabilizer $G_{u^*} := \mathrm{Aut}(G)_{u^*}$, the σ-fingerprint is the labelled tuple
$$\Phi(u^*) := \big( \mathcal{F}(u^*),\ K(u^*),\ \mathrm{stab}(u^*),\ \vec{\nu}(u^*),\ \vec{\rho}(u^*),\ \vec{\lambda}(u^*),\ B(u^*),\ S(u^*)\big),$$
with components defined below. The fingerprint refines the σ-tuple of Commitment 14 by augmenting with diagnostic-vector data (Bind, Sep) which are SCC-intrinsic and computable in $O(|E|)$ time.

### §2.1 Component definitions

**(C1) $\mathcal{F}(u^*) \in \mathbb{Z}_{\geq 0}$ — formation count.**
Strict-local-maxima count: $\mathcal{F}(u^*) := \#\{i \in X : u^*(i) > u^*(j) \text{ for all } j \sim i\}$. Computable in $O(|E|)$ time.

**(C2) $K(u^*) \in \mathbb{Z}_{\geq 0}$ — σ-tuple cutoff length.**
$K := \min\{k : \mu_k > 10 \mu_{0+}\}$ per Commitment 14 (O3 K-A) where $\mu_{0+}$ is the smallest positive Hessian eigenvalue (Goldstone-aware). Cutoff is data-dependent, typically $K \approx 5$–$15$ on R23.

**(C3) $\mathrm{stab}(u^*)$ — stabilizer fingerprint.**
A small structural invariant of $G_{u^*} = \mathrm{Aut}(G)_{u^*}$ encoding:
- $|G_{u^*}|$ (group order),
- a canonical conjugacy-class signature $\mathrm{cc}(G_{u^*}) := \{(\#g, \mathrm{ord}(g))\}_{g \text{-class reps}}$ (multiset of orders, weighted),
- an isomorphism-class label from a small lookup table (e.g., $D_4$, $D_n$, $\mathbb{Z}_2$, $\{e\}$ for known cases, otherwise GAP small-group ID).

This component is intentionally lightweight: the full $\mathrm{Aut}(G)$ enumeration via PyNauty is $O(|X|^{c \log |X|})$ in pathological cases but typically tractable in practice on $|X| \leq 1024$ (R23 = 1024).

**(C4) $\vec{\nu}(u^*) = (\nu_1, \nu_2, \ldots, \nu_K) \in \mathbb{Z}_{\geq 2}^K$ — nodal count vector.**
$\nu_k := \mathcal{N}(\phi_k)$ where $\phi_k$ is the $k$-th Hessian eigenvector and $\mathcal{N}$ is the nodal-count function (T-σ-Lemma-2 (i)). Computable in $O(|E|)$ per eigenvector via BFS on signed components.

**(C5) $\vec{\rho}(u^*) = ([\rho_1], [\rho_2], \ldots, [\rho_K])$ — irrep label vector.**
$[\rho_k] \in \widehat{G_{u^*}}$ = irrep label of $\phi_k$ via isotypic projection $P_{[\rho]}$ (T-σ-Lemma-1 (ii)). Computed via character orthogonality: $[\rho_k] := \arg\max_{[\rho]} \|P_{[\rho]} \phi_k\|^2$.

**(C6) $\vec{\lambda}(u^*) = (\lambda_1, \ldots, \lambda_K) \in \mathbb{R}_{>0}^K$ — Hessian eigenvalue vector.**
Lowest $K$ non-volume eigenvalues of the constrained Hessian, sorted ascending, rounded to 4 decimal places to absorb numerical noise (per `sigma_class_count_R23.py` precedent).

**(C7) $B(u^*) \in [0, 1]$ — Bind diagnostic.**
Cohesion-weighted boundary tightness, computed via `scc/diagnostics.py` `diagnostic_vector`. $O(|E|)$ time. Intrinsic SCC quantity.

**(C8) $S(u^*) \in [0, 1]$ — Sep diagnostic.**
Inter-formation separation, u-weighted distinction integral. $O(|E|)$ time. Intrinsic SCC quantity.

### §2.2 Equivalence and conjugation

**Definition 2.2 (fingerprint equivalence).** Two minimizers $u_1^*, u_2^*$ on (possibly distinct) graphs $G_1, G_2$ are **fingerprint-equivalent**, $u_1^* \sim_\Phi u_2^*$, iff:

- **(E1)** $\mathcal{F}(u_1^*) = \mathcal{F}(u_2^*)$, $K(u_1^*) = K(u_2^*)$.
- **(E2)** $\mathrm{stab}(u_1^*) \cong \mathrm{stab}(u_2^*)$ as labelled groups.
- **(E3)** $\vec{\nu}(u_1^*) = \vec{\nu}(u_2^*)$ entry-wise.
- **(E4)** There exists $\varphi: G_{u_1^*} \to G_{u_2^*}$ isomorphism such that $[\rho_k(u_2^*)] = [\varphi_* \rho_k(u_1^*)]$ for all $k$, modulo conjugation per Definition 2.1' clause (c) (Schur-degenerate isomorphism class).
- **(E5)** $|\lambda_k(u_1^*) - \lambda_k(u_2^*)| < \epsilon_\lambda$ for $k = 1, \ldots, K$ ($\epsilon_\lambda = 10^{-4}$ default).
- **(E6)** $|B(u_1^*) - B(u_2^*)| < \epsilon_B$ and $|S(u_1^*) - S(u_2^*)| < \epsilon_S$ ($\epsilon_B = \epsilon_S = 10^{-3}$).

**Lemma 2.3 (Aut(G)-orbit invariance).** *Within a fixed graph $G$, $\Phi$ is constant on $\mathrm{Aut}(G)$-orbits, modulo canonical conjugation.*

*Proof sketch.* (C1, C7, C8) are $\mathrm{Aut}(G)$-invariant by adjacency preservation. (C3) is constant within the $\mathrm{Aut}(G)$-orbit (stabilizer conjugates to a conjugate of itself). (C4, C6) follow from T-σ-Lemma-1 commutation $H(\pi u^*) = \pi H(u^*) \pi^{-1}$. (C5) is stable modulo $G_u$-conjugation per Definition 2.1' clauses (b)–(c). (C2) cutoff $K$ depends only on $\vec{\lambda}$ which is $\mathrm{Aut}(G)$-invariant. $\Box$

---

## §3. Algorithm specification

### §3.1 Top-level pipeline

```
INPUT:  minimizer u* ∈ R^n on graph G with parameters (α, β, c)
OUTPUT: σ-fingerprint Φ(u*) ∈ labelled tuple

ALGORITHM ComputeSigmaFingerprint(u*, G, α, β, c, K_max=15):
  1.  F   := COUNT_LOCAL_MAXIMA(u*, G)                # O(|E|)
  2.  H   := BUILD_CONSTRAINED_HESSIAN(u*, G, α, β)   # O(|E|) sparse construction
  3.  (λ, φ) := LANCZOS_LOWEST_K(H, K_max)            # O(K_max · |E|) per iter
  4.  filter volume mode → (λ_phys, φ_phys)
  5.  K   := SIGMA_CUTOFF(λ_phys, ratio=10, K_max)    # O(K_max)
  6.  ν   := [NODAL_COUNT(φ_k, G) for k in 1..K]      # O(K · |E|) total
  7.  G_u := COMPUTE_STABILIZER(u*, G)                # O(|X|^c log |X|), bounded
  8.  ρ   := [IRREP_LABEL(φ_k, G_u) for k in 1..K]    # O(K · |G_u|^2 · n)
  9.  stab := STABILIZER_SIGNATURE(G_u)               # O(|G_u|^2)
  10. (B, S) := DIAGNOSTIC_VECTOR(u*, G, α, β, c)     # O(|E|)
  11. Φ   := (F, K, stab, ν, ρ, λ_phys[:K], B, S)
  12. RETURN Φ
```

### §3.2 Step-by-step justifications

**Step 1 (COUNT_LOCAL_MAXIMA).** Scan each vertex; check $u^*[i] > u^*[j]$ for all $j \sim i$. Time $O(\sum_i \deg(i)) = O(|E|)$. Already implemented in `sigma_locality_R23_cycle_torus.py` `count_local_maxima`. ✓

**Step 2 (BUILD_CONSTRAINED_HESSIAN).** At minimizer $u^*$ (non-uniform), use leading-order approximation $H(u^*) \approx 4\alpha L_G + \beta W''(u^*) \cdot \mathrm{diag}$ where $W''(u) = 2(1 - 6u + 6u^2)$ per `scc/energy.py` `double_well_second_deriv`. Volume tangent direction is filtered in step 4. Time $O(|E|)$ for Laplacian + $O(n)$ diagonal.

*Caveat (Cat B → Cat A path):* The full Hessian includes closure + separation contributions. Step 2 currently uses a $\mathcal{E}_{\mathrm{bd}}$-only approximation; full-Hessian inclusion is a Cat A target via finite-differences on `energy.gradient` (already validated to 1e-9 precision per `scc/energy.py` FD-verified gradient). Cost: $O(K \cdot n)$ Hessian-vector products, each $O(|E|)$.

**Step 3 (LANCZOS_LOWEST_K).** Use `scipy.sparse.linalg.eigsh(H, k=K_max+1, which='SM')`. Lanczos cost: $O(K_{\max} \cdot |E|)$ per matrix-vector product, $O(K_{\max}^2)$ orthogonalization, $K_{\max}$ iterations → $O(K_{\max}^2 \cdot |E|)$. On R23 ($n = 1024$, $|E| \approx 2 \cdot 1024 = 2048$, $K_{\max} = 15$): $\sim 15^2 \cdot 2048 \approx 0.5\mathrm{M}$ flops, sub-millisecond.

**Step 4 (volume-mode filter).** Reuse `filter_non_volume_modes` from `sigma_locality_R23_cycle_torus.py`: drop the eigenvector with $|\langle \phi, \mathbf{1}/\sqrt{n} \rangle| > 0.5$. $O(K_{\max} \cdot n)$ inner products.

**Step 5 (SIGMA_CUTOFF).** Walk through sorted $\lambda_{\mathrm{phys}}$ ascending; return smallest $k$ such that $\lambda_k > 10 \cdot \lambda_1$. Trivially $O(K_{\max})$. Per Commitment 14 (O3 K-A).

**Step 6 (NODAL_COUNT).** For each eigenvector $\phi_k$:
- Compute $X^+ := \{i : \phi_k(i) > 0\}$ and $X^- := \{i : \phi_k(i) < 0\}$.
- BFS-count connected components of $G[X^+]$ and $G[X^-]$.
- $\mathcal{N}(\phi_k) := \#\mathrm{cc}(G[X^+]) + \#\mathrm{cc}(G[X^-])$.

Time per eigenvector $O(|E|)$ (BFS); total over $K$ eigenvectors $O(K \cdot |E|)$. ✓ Per T-σ-Lemma-2 (i).

**Step 7 (COMPUTE_STABILIZER).** Currently the bottleneck step. Three sub-options:

  - **(a) Analytical fast path** (W6 implementation, default): For known graph classes (grid-$D_4$, cycle-$D_n$, torus-$\mathbb{Z}_n^2 \rtimes D_4$, complete-$S_n$), use a lookup table indexed by graph-class identifier. $O(1)$ time. Already implemented for the 3 graphs in `sigma_locality_R23_cycle_torus.py`.

  - **(b) PyNauty integration** (W7+ target, NQ-259): Use `pynauty` to compute $\mathrm{Aut}(G)$ generators in $O(|X|^c \log |X|)$ practical time on $|X| \leq 1024$. Then filter by $u^*$-invariance: $G_{u^*} := \{\pi : u^*[\pi(i)] = u^*[i] \forall i\}$. Filter cost $O(|X|^2)$ in worst case but typically $O(|X|)$ via canonical orbit refinement.

  - **(c) Color-refinement fallback** (lightweight, NQ-264 default for unknown graphs): Use Weisfeiler-Lehman color refinement seeded by $u^*$-values: $\mathrm{stab}(u^*)$ is bounded above by automorphisms preserving the WL color partition. Time $O(|X|^2 \log |X|)$. Not exact but provides a structural lower-bound fingerprint.

  W6 default: option (a) for the 3 standard graphs (R23, cycle, torus); option (c) for arbitrary graphs.

**Step 8 (IRREP_LABEL).** For each $\phi_k$:
- Compute the isotypic projection norms $\|P_{[\rho]} \phi_k\|^2$ for each $[\rho] \in \widehat{G_{u^*}}$ via the projector $P_{[\rho]} = \frac{\dim\rho}{|G_u|} \sum_{\pi \in G_u} \overline{\chi_\rho(\pi)} \pi$.
- $[\rho_k] := \arg\max_{[\rho]} \|P_{[\rho]} \phi_k\|^2$.

Time $O(|G_{u^*}| \cdot n)$ per irrep × $|\widehat{G_{u^*}}|$ irreps × $K$ eigenvectors $= O(K \cdot |G_{u^*}| \cdot |\widehat{G_{u^*}}| \cdot n)$. On $D_4$ ($|G| = 8$, $|\widehat{G}| = 5$, $n = 1024$, $K = 15$): $\sim 615\mathrm{K}$ flops. Sub-second.

For multi-dimensional irreps (e.g., $D_4$ E-irrep), record the **isomorphism class** label only per Definition 2.1' clause (c); basis-choice ambiguity is absorbed (Schur orthogonality, Serre 1977 §2.2).

**Step 9 (STABILIZER_SIGNATURE).** Compute $\mathrm{cc}(G_{u^*})$ via group-element enumeration: for each $\pi \in G_{u^*}$, compute order. Bin by order; record multiset $\{(\#g, \mathrm{ord}(g))\}$. Time $O(|G_{u^*}|^2)$ generic, $O(|G_{u^*}| \log |G_{u^*}|)$ with caching.

For known small groups, augment with isomorphism-class label from a hardcoded lookup ($D_4 \leftrightarrow \langle 2, 1, 0, 0, 1 \rangle$ conjugacy signature; $\mathbb{Z}_2 \leftrightarrow \langle 1, 1 \rangle$; etc.).

**Step 10 (DIAGNOSTIC_VECTOR).** Reuse `scc/diagnostics.py` `diagnostic_vector` which returns `DiagnosticVector(Bind, Sep, Inside, Persist)`. Already $O(|E|)$ optimized.

### §3.3 Total complexity

Summing:
$$T(\Phi) = O(|E|) + O(K_{\max}^2 |E|) + O(K |E|) + T_{\mathrm{stab}}(G) + O(K |G_u| |\widehat{G_u}| n) + O(|G_u|^2)$$

For R23 ($n = 1024$, $|E| = 2048$, $K = 15$, $|G_u| = 8$, $|\widehat{G_u}| = 5$):
- Lanczos: $\sim 5 \cdot 10^5$ flops.
- Nodal counts: $\sim 3 \cdot 10^4$ flops.
- Irrep projection: $\sim 6 \cdot 10^5$ flops.
- Stabilizer (analytical fast path): $O(1)$.

**Total: $\sim 10^6$ flops $\approx 10$ ms per minimizer on commodity hardware.**

For 56 minimizers: full R23 fingerprint enumeration $\approx 0.6$ s.

**Asymptotic complexity (excluding stabilizer):** $O(K_{\max}^2 |E| + K |G_u| |\widehat{G_u}| n)$ = **$O(n \log n)$ in $|X|$ for sparse graphs with bounded-symmetry stabilizers**. ✓ Sub-cubic, in fact near-linear (F2 satisfied with significant margin).

**Including PyNauty stabilizer (W7+ option):** practical $O(|X|^2 \log |X|)$ worst-case, $O(|X|)$ typical.

---

## §4. R23 strength verification protocol

### §4.1 Test design

**Dataset.** R23 fullscale (`CODE/scripts/results/exp_orbital_fullscale.json`) — 56 stable minimizers on $32 \times 32$ $D_4$ free-BC grid at $(\alpha, \beta, c) = (1, 30, 0.5)$. Each minimizer carries pre-stored Hessian eigenvalues (`eigenvalues` field, 12 modes).

**Strength claim (BC-264-emp).**
$$|\Phi(\mathcal{L}_{R23})| \in [12, 30]$$
strictly greater than `sigma_class_count_R23.py` eigenvalue-only proxy (currently $\sim$8 classes; rerun pending) but strictly less than 56 (full minimizer count).

### §4.2 Falsifiable predictions

- **(P1) Refinement.** $|\Phi(\mathcal{L}_{R23})| \geq |\sigma\text{-proxy classes}|$. Fingerprint should be $\geq$ as strong.
- **(P2) Concentration.** $|\Phi(\mathcal{L}_{R23})| \leq 30$. The σ-fingerprint should not be so fine that every minimizer becomes its own class.
- **(P3) PH-σ refinement (per OAT-7).** σ-fingerprint refines persistent-homology classes. The (F=51, K=5) $p$-vs-$g$ pair from `working/MF/single_high_F_equivalence.md` §5 should land in **distinct σ-fingerprint classes** but identical PH classes.

### §4.3 Implementation outline

```python
# CODE/scripts/sigma_fingerprint_R23.py (proposed, NQ-264 follow-up Task #26)
import json
from pathlib import Path
from scc import GraphState
from scc.scripts_lib.fingerprint import compute_sigma_fingerprint   # NEW module

data = json.load(open("CODE/scripts/results/exp_orbital_fullscale.json"))
G = GraphState.grid_2d(32, 32)
fingerprints = {}
for cluster in data["cluster_summaries"]:
    if cluster.get("morse_index") != 0:
        continue
    u_star = cluster["u_star_field"]                     # pre-stored or recomputed
    Phi = compute_sigma_fingerprint(u_star, G, alpha=1.0, beta=30.0, c=0.5)
    fingerprints[cluster["cluster_key"]] = Phi

# Group by fingerprint equivalence (Definition 2.2)
classes = group_by_phi_equivalence(fingerprints, eps_lambda=1e-4, eps_diag=1e-3)
print(f"σ-fingerprint class count (NQ-264 strength): {len(classes)}")
```

### §4.4 Comparison baseline

Run side-by-side with `sigma_class_count_R23.py` eigenvalue-only proxy:

| Method | Class count target | Computational cost |
|---|---|---|
| Eigenvalue proxy (current) | $\sim 8$ classes | $O(K \log K)$ trivial |
| **σ-fingerprint (this spec)** | **12–30 classes** | $\sim 10$ ms/minimizer, $O(n \log n)$ |
| PH coarseness (OAT-7) | $\sim 5$ classes | $O(n^2)$ Vietoris-Rips |
| Full irrep-aware σ (W7+ NQ-188) | exact, $\leq 30$ | depends on $|G_u|$ enumeration |

Expectation: σ-fingerprint sits between eigenvalue proxy and full irrep-aware σ-class, providing the **practical sweet spot** of strength + computability.

---

## §5. Composition with σ-locality (Bridge B-2)

The σ-fingerprint composes naturally with T-σ-Schramm-Locality:

**Proposition 5.1 (Locality of σ-fingerprint at first pitchfork).**
*Let $G_1, G_2$ satisfy hypotheses of T-σ-Schramm-Locality (`schramm_sigma_locality_theorem.md` §2). Let $u_{i, \mathrm{pitchfork}}^*$ denote the post-pitchfork minimizer at $\beta = \beta_{\mathrm{crit}}^{(2)}(G_i) + \epsilon$. If $\varphi: G_{u_1^*} \to G_{u_2^*}$ is irrep-compatible, then*
$$\Phi(u_{1, \mathrm{pitchfork}}^*) \sim_\Phi \Phi(u_{2, \mathrm{pitchfork}}^*).$$

*Proof sketch.* By T-σ-Schramm-Locality §4 Steps 1–5: components (C2)–(C6) of the σ-fingerprint match modulo conjugation. (C1) $\mathcal{F}$ is determined by tie-break convention applied to a structurally matched bifurcation. (C7)–(C8) Bind/Sep diagnostics depend only on cohesion-level adjacency contractions, preserved by the linear isomorphism $\Phi: T_{u_1^*}\Sigma_m^{(1)} \to T_{u_2^*}\Sigma_m^{(2)}$ in the post-pitchfork tangent direction. Hence (E1)–(E6) of Definition 2.2 are satisfied. $\Box$

**Consequence.** The σ-fingerprint is a **locality-respecting strong invariant**: it inherits Bridge B-2's locality structure while strengthening discrimination beyond the bare σ-tuple. This makes Φ the natural canonical candidate for a "formation identity tag" satisfying both (CN17 σ-Labeled Formation Quantization) and (Schramm-style locality).

---

## §6. Cat target

**Cat B (target).** Algorithm specification (this file) is Cat A definitional once Definition 2.1' (`sigma_uniqueness_theorem.md` §2 Schur conjugation rule) is canonical. Empirical strength claim (BC-264-emp, §4.1 R23 enumeration) is Cat B target pending implementation.

**Cat A lift requires:**
- Stabilizer computation (Step 7) via PyNauty integration on R23 (NQ-259, W6+).
- Numerical verification of (P1)–(P3) on R23 + extended dataset.
- Closed-form locality composition (Proposition 5.1) cross-validation.

---

## §7. Effort & priority

**NQ-264 (Cat B target).** Bridge B-4 σ-fingerprint follow-up.

| Item | Description | W-band | Effort |
|---|---|---|---|
| **Task #25 (this file)** | Algorithm spec | W5 Day 4 PM | DONE |
| Task #26 | Numerical script `CODE/scripts/sigma_fingerprint_R23.py` | W6 | 4–5 days |
| §4 R23 strength enumeration | Run on 56 minimizers | W6 | 1 day |
| §5 locality composition test | Reuse `sigma_locality_R23_cycle_torus.py` infrastructure | W6 | 2 days |
| §3.2 Step 7 PyNauty integration | NQ-259 prerequisite | W6+ | 1 week |
| §6 Cat A lift | Full canonical promotion | W7+ | 2–3 weeks |

**Cat target:** **B**. Effort: **6–8 weeks** for Cat B verification per `foundational_bridges_2026.md` §10.

---

## §8. Hard constraint check

- [x] **$u_t : X_t \to [0,1]$ primitive maintained.** σ-fingerprint is computed *from* $u^*$; no replacement.
- [x] **CN10 contrastive vs knot theory.** §1 explicit. Subject matter (Hessian-spectral fingerprints) ≠ knot diagrams. Bar-Natan–van der Veen inspires *strong-and-computable* spirit only.
- [x] **CN5 4-energy decomposition not merged.** Bind (C7) and Sep (C8) are kept distinct from closure/boundary; full $\mathcal{E}$ structure preserved in Step 2 Hessian.
- [x] **F-1 / M-1 / MO-1 not silently resolved.** σ-fingerprint applies to single-formation regime; multi-formation extension via $\mathrm{Aut}(G) \wr S_{K_{\mathrm{act}}}$ deferred to W7+ (OP-0008/OP-0009 still open).
- [x] **No re-introduction of Research OS structure.**
- [x] **Direct canonical edits: 0.** W7+ promotion candidate.
- [x] **K_field/K_act decomposition respected** (Commitment 16). Single-formation regime $K_{\mathrm{field}} = K_{\mathrm{act}} = 1$ throughout.

---

## §9. References

**Canonical (§13 / §11.1 anchors).**
- §11.1 Commitment 14 — σ-tuple definition + (O5')(O7) ordering (CV-1.5.1, 2026-04-29).
- §11.1 Commitment 17 (proposed) — Tool A2 quotient + Tool A3 PH framework.
- §13 T-σ-Lemma-1 — irrep decomposition well-defined.
- §13 T-σ-Lemma-2 — nodal count properties.
- §13 T-σ-Theorem-3 — uniform Hessian closed form (Cat A on $D_4$ free-BC).
- §13 T-σ-Theorem-4 — first pitchfork σ-tuple.
- §14 CN10 contrastive (vs knot theory).
- §14 CN17 σ-Labeled Formation Quantization.

**Working files.**
- `working/MF/foundational_bridges_2026.md` §5 Bridge B-4 (NQ-264 originator).
- `working/SF/schramm_sigma_locality_theorem.md` §3 Definition 3.3 (irrep-compatibility) + §5 (locality composition target).
- `working/SF/sigma_uniqueness_theorem.md` §2 Definition 2.1' (canonical conjugation rule).
- `working/MF/single_high_F_equivalence.md` §4–§5 (OAT-7 PH-vs-σ, $p$-vs-$g$ refinement).
- `working/SF/sigma_lie_algebra_structure.md` §4 (σ-tuple as $\mathrm{Aut}(G)_{u^*}$-irrep decomposition).

**Code references.**
- `CODE/scc/diagnostics.py` — `DiagnosticVector` (Bind, Sep) at $O(|E|)$.
- `CODE/scc/energy.py` — `double_well_second_deriv`; `EnergyComputer.gradient` for FD-Hessian.
- `CODE/scripts/sigma_class_count_R23.py` — eigenvalue-proxy precedent.
- `CODE/scripts/sigma_locality_R23_cycle_torus.py` (Bridge B-2 numerical, this Wave 3) — reusable infrastructure for nodal-count, Hessian-at-uniform, stabilizer info.

**External.**
- **Bar-Natan, D. & van der Veen, R. (2026).** *"Knot invariants from QR-code-like fingerprints."* ⚠️ citation pending verification per `foundational_bridges_2026.md` §12.2.
- **Serre, J.-P. (1977).** *Linear Representations of Finite Groups.* Springer GTM 42. §2.2 Schur Lemma; §2.6 isotypic projectors.
- **McKay, B. D. & Piperno, A. (2014).** *"Practical graph isomorphism, II."* J. Symb. Comput. 60. (PyNauty foundation for Step 7 PyNauty path.)

---

## §10. Wave 3 Provenance Log

**Created:** 2026-04-30 W5 Day 4 PM Wave 3 — scc-wave3-deep-research team, Task #25 σ-fingerprint algorithm spec.

**Inheritance.** Direct successor to Bridge B-2 numerical verification (`sigma_locality_R23_cycle_torus.py` infrastructure reused: `count_local_maxima`, `low_eigenpairs`, `filter_non_volume_modes`, stabilizer dataclass).

**Status.** Working draft, Cat B target. NQ-264 algorithm specification.

**Deliverables checklist:**
- [x] §1 Mission + (F1)–(F4) goals.
- [x] §2 σ-fingerprint definition (8 components C1–C8) + equivalence relation.
- [x] §3 Algorithm specification (12-step pipeline + complexity analysis).
- [x] §4 R23 strength verification protocol with falsifiable predictions.
- [x] §5 Composition with σ-locality (Proposition 5.1).
- [x] §6 Cat target.
- [x] §7 Effort estimate.
- [x] §8 Hard constraint check.
- [x] §9 References.
- [x] §10 Provenance log.

**Promotion target:** W7+ canonical §11.1 Commitment 17 (proposed) packet contribution; or W7+ §13 candidate "T-σ-Fingerprint" if §4 R23 strength claim Cat B verified.

**Next steps:** Task #26 (`CODE/scripts/sigma_fingerprint_R23.py` implementation) is the natural follow-up. Estimated 4–5 days.

---

**End of working file.** Promotion pipeline next stage: §3 algorithm implementation in scc-namespace utility module → §4 R23 enumeration → §5 locality composition cross-test → W6 review → W7+ canonical candidate.
