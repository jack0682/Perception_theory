# sigma_rich_VR_phase1.md — σ_rich + Tool A3 Vietoris-Rips PH Integration (NQ-242 Phase 1)

**Status:** working draft (W5 Day 4, Task #34 V-R Phase 1).
**Created:** 2026-04-30 (W5 Day 4).
**Type:** Integration design — σ_rich (`sigma_rich_augmentation.md` §2) coupled to Tool A3 Vietoris-Rips PH (`mathematical_scaffolding_4tools.md` §4) at NQ-242 Phase 1 level (centroid trajectory extraction + V-R PH barcode + K-jump detection).
**Author origin:** Task #34 σ_rich PH integration with Tool A3 (W5 Day 4 PM); follows σ_rich definition `sigma_rich_augmentation.md` + Tool A3 PH framework `mathematical_scaffolding_4tools.md` §4.
**Canonical refs:** §11.1 Commitment 14, 14-Multi, 16; §13 T-σ-multi-A-Static; §14 CN5, CN10; §15 OP-0008.
**Working refs:** `sigma_rich_augmentation.md` (σ_rich definition); `mathematical_scaffolding_4tools.md` §4 (Tool A3 PH); `sigma_multi_trajectory.md` §3.7 + §6.1 (PH reformulation + Phase 1-4 plan); `nq242c_explicit_construction.md` (target numerical anchor).
**Open problems:** OP-0008 (Path B numerical pipeline foundation).

---

## §1. Mission

> **"σ_rich centroid component {c_j(t)}을 Vietoris-Rips persistent homology pipeline 의 입력으로 정식 연결: K_act(t) ↔ H_0 barcode, K-jump events ↔ H_0 bar-deaths, loop structure ↔ H_1 barcode. NQ-242 Phase 1 (W6 Day 1-3) 의 design 산출."**

이 working file 은 σ_rich (`sigma_rich_augmentation.md`) 의 centroid component 가 Tool A3 PH (`mathematical_scaffolding_4tools.md` §4) 의 Vietoris-Rips 입력과 *formally identical* 함을 정식화하고, NQ-242 PH pipeline Phase 1 (centroid extraction + V-R PH barcode + K-jump detection) 의 design specification 을 제공한다.

**핵심 산출**:
1. Centroid trajectory $C(t)$ 의 well-definedness on stratum interiors (§2).
2. V-R complex $R_r(C(t))$ 의 graph-metric instantiation (§3).
3. H_0 barcode ↔ K_act(t) 동치 정식화 (§4).
4. K-jump events ↔ H_0 bar-deaths 매핑 (§5).
5. Phase 1 numerical pipeline spec (§6).
6. Cat status (Cat B target W6 Day 1-3) (§7).

---

## §2. Centroid Trajectory $C(t)$

### §2.1 Definition (recap from `sigma_rich_augmentation.md` §2.3.1)

For trajectory $\mathbf{u}(t) \in \widetilde\Sigma^K_M$ at time $t$, active formation set $\mathrm{act}(t) = \{j : \|u^{(j)}(t)\|_1 > \epsilon\}$. For each $j \in \mathrm{act}(t)$:
$$c_j(t) := \frac{\sum_{x \in X} x \cdot u^{(j)}(t, x)}{\sum_{x \in X} u^{(j)}(t, x)} \in \mathbb{R}^{\dim X}.$$

The **centroid trajectory** is:
$$C(t) := \{c_j(t) : j \in \mathrm{act}(t)\} \subseteq \mathbb{R}^{\dim X}.$$

$|C(t)| = K_{\mathrm{act}}(t)$ (number of active formations at time $t$).

### §2.2 Continuity properties

**Proposition 2.1 (smooth-segment continuity).** On a smooth segment $(t_n^*, t_{n+1}^*)$ with constant $K_{\mathrm{act}} = K'$:
- Each $c_j(t)$ is a smooth function of $t$ (numerator + denominator both smooth in $u^{(j)}(t)$, denominator bounded below by $\epsilon$).
- The set $C(t)$ is a smoothly-evolving $K'$-point configuration in $\mathbb{R}^{\dim X}$.

**Proof sketch**: Quotient of smooth functions with non-vanishing denominator is smooth. ✓

**Proposition 2.2 (K-jump discontinuity in $C(t)$).** At K-jump time $t^*$ with $\Delta K = 1$ simple merger of $(j, k) \to \ell$:
- $C(t^{*-}) = \{\ldots, c_j(t^{*-}), c_k(t^{*-}), \ldots\}$ with $K'$ points.
- $C(t^{*+}) = \{\ldots, c_\ell(t^{*+}), \ldots\}$ with $K' - 1$ points.
- The two points $c_j(t^{*-}), c_k(t^{*-})$ converge: $\|c_j(t^{*-}) - c_k(t^{*-})\| \to 0$ as $t \nearrow t^*$ (under the merger-geometry convention; see §5 below for refinement).

This makes $C(t)$ a **time-varying point cloud** with births/deaths at K-jump times — exactly the input expected by zigzag persistence (Carlsson-de Silva-Morozov 2009).

### §2.3 Graph-embedding convention

For abstract graphs $G = (X, E)$ without ambient embedding, fix a vertex-position assignment $\iota : X \to \mathbb{R}^{\dim X}$:
- **Lattice graphs** ($T^2_L, \mathbb{Z}^d$): $\iota(x) = $ vertex coordinates in $\mathbb{R}^d$.
- **Generic graphs**: $\iota$ via spectral embedding (Fiedler vectors of graph Laplacian, $\dim X = $ number of small Laplacian eigenvalues retained).

The centroid $c_j$ is then $u^{(j)}$-weighted average of $\iota(x)$. For graphs without natural embedding, V-R PH on graph metric $d_G$ (§3.2) avoids this issue by using $d_G$ directly without going through $\mathbb{R}^{\dim X}$.

---

## §3. Vietoris-Rips Complex on Graph Metric

### §3.1 V-R complex definition (recap from `mathematical_scaffolding_4tools.md` §4.1)

Given finite point set $C(t) \subset X$ (or $\subset \mathbb{R}^{\dim X}$ via embedding), and scale $r \geq 0$:
$$R_r(C(t)) := \big\{ \sigma \subseteq C(t) : \forall a, b \in \sigma,\ d_G(a, b) \leq r \big\}$$
where $d_G$ is graph-shortest-path distance. Vertices of $R_r$ are points in $C(t)$; edges connect pairs within distance $r$; higher simplices fill in clique-style.

### §3.2 Two metric conventions

- **Convention G (graph-metric)**: $d_G(c_j, c_k) = $ shortest-path graph distance between *nearest vertices* of $X$ to centroids. Requires snapping centroids to vertices.
- **Convention E (Euclidean)**: $d_E(c_j, c_k) = \|c_j - c_k\|_2$ via embedding $\iota$. Native real-valued.

For lattice graphs (e.g., $T^2_L$), Convention E is preferred (centroids are real-valued in $\mathbb{R}^2$, no need to snap). For abstract graphs, Convention G via Fiedler embedding.

**Phase 1 default**: Convention E for $T^2_{20}$ in NQ-242c construction (`nq242c_explicit_construction.md` §2.1).

### §3.3 V-R PH stability

By Cohen-Steiner-Edelsbrunner-Harer (2007): bottleneck distance between V-R PH diagrams of $C, C'$ is bounded by Hausdorff distance:
$$d_B(\mathrm{Dgm}(R(C)), \mathrm{Dgm}(R(C'))) \leq d_H(C, C').$$

**Implication**: small perturbations in centroid configurations produce small barcode perturbations. σ_rich centroid component is **robust** in the PH-barcode sense.

---

## §4. H_0 Barcode ↔ K_act(t)

### §4.1 H_0 connectivity

$H_0(R_r(C(t)))$ counts connected components of $R_r(C(t))$. As $r \to \infty$:
- All points eventually merge into one component (V-R complex becomes the full simplex).
- $\dim H_0(R_\infty(C(t))) = 1$.

As $r \to 0^+$:
- Each centroid is isolated (assuming distinct).
- $\dim H_0(R_0(C(t))) = K_{\mathrm{act}}(t)$.

**Claim 4.1 (K_act recovery from $H_0$ at $r = 0^+$).**
$$K_{\mathrm{act}}(t) = \dim H_0(R_{0^+}(C(t))).$$

This recovers Commitment 16 active count from the $H_0$ barcode.

### §4.2 H_0 barcode = pair-distance multi-set

For $K' = K_{\mathrm{act}}$ points in $C(t)$, the $H_0$ barcode consists of $K'$ bars:
- One **infinite bar** (a connected component never dies; the "main" component).
- $K' - 1$ **finite bars**, each born at $r = 0$ and dying at $r = r_d$ where $r_d$ is the merger scale of the smallest cluster.

The death scales $\{r_d^{(1)}, \ldots, r_d^{(K'-1)}\}$ form a multi-set. By single-linkage clustering equivalence, this multi-set equals the **minimum-spanning-tree edge weights** of $C(t)$ under metric $d_G$ (or $d_E$).

**Implication**: $H_0$ barcode at time $t$ encodes the *connectivity structure* of $C(t)$ — closer than centroid pair-distance multi-set (because MST edge set ⊆ pair-distance set).

### §4.3 Connection to σ_rich centroid component

σ_rich centroid component: $\{c_j(t)\}$ — the raw point cloud.
V-R H_0 barcode: derived invariant of $\{c_j(t)\}$ — partial info (MST structure, not full pair-distance set).

**σ_rich is strictly richer than H_0 barcode**: e.g., two configurations with same MST but different non-MST distances differ in σ_rich's pair-distance component but coincide in H_0 barcode. For NQ-242c equilateral A (pair distances $\{10, 10, 10\}$) vs isoceles B (pair distances $\{10, 8.60, 8.60\}$): MST of A has weights $\{10, 10\}$ (any two edges of equilateral); MST of B has weights $\{8.60, 8.60\}$. Both H_0 barcodes are 2-bar; barcodes differ in death scales (A: 10; B: 8.60).

So $H_0$ barcode also distinguishes A from B in this example — both σ_rich and $H_0$-barcode-augmented σ work. σ_rich provides *finer* discrimination in non-MST-distinguishing examples.

---

## §5. K-jump Events ↔ H_0 Bar-Deaths

### §5.1 Bar-death at merger time

At K-jump time $t^*$ with $(j, k) \to \ell$ merger:
- Pre-merger: $H_0(R_r(C(t^{*-})))$ has $K' - 1$ finite bars + 1 infinite.
- Post-merger: $H_0(R_r(C(t^{*+})))$ has $K' - 2$ finite bars + 1 infinite.

The "lost" finite bar corresponds to the merger pair $(j, k)$: as $\|c_j - c_k\| \to 0$ approaching $t^*$, the finite bar's death scale $r_d^{(jk)} \to 0$, and at $t^{*+}$ the bar disappears entirely (post-merger formation $\ell$ is a single component, not two).

**Claim 5.1 (K-jump detection).** A K-jump event at $t^*$ is identified as a discontinuity in the H_0 barcode time-series — specifically, the disappearance of one finite bar between $t^{*-}$ and $t^{*+}$.

### §5.2 Zigzag persistence over K-jumps

By Carlsson-de Silva-Morozov 2009: zigzag persistence handles point insertions/deletions over a parameter. K-jump events = point deletions in $C(t)$ (two points merge into one ⇒ net deletion).

**Zigzag persistence pipeline** (per `mathematical_scaffolding_4tools.md` §4.4):
- Sample times $t_0 < t_1 < \cdots < t_N$ across $[0, T]$ at sufficient density.
- At each $t_i$ extract $C(t_i)$.
- Construct zigzag complex $R(C(t_0)) \leftarrow R(C(t_0) \cap C(t_1)) \to R(C(t_1)) \leftarrow \cdots$.
- Compute zigzag barcode via GUDHI library `Zigzag_persistence`.

**K-jump bar-deaths in zigzag**: each K-jump produces a "death" event in the zigzag barcode at the corresponding time-stamp.

### §5.3 Pair identification from zigzag barcode

For pair-identification in Φ_rich (per `sigma_rich_augmentation.md` §3.2 Claim 3.1): the zigzag barcode death at $t^*$ identifies *which two centroids* merged — namely, the pair $(c_j, c_k)$ whose finite $H_0$ bar disappeared.

This is **equivalent** to "minimum centroid-distance pair" criterion: the bar that dies at smallest scale corresponds to the closest pair (by single-linkage MST).

---

## §6. H_1 Loop Structure (3+ Formations)

### §6.1 H_1 birth in cyclic arrangements

For $K' = 3$ formations in equilateral arrangement (NQ-242c Configuration A at $t = 0$):
- At small $r$: 3 disconnected points.
- At $r \in (0, 10)$ (graph-distance unit): no edges, no triangle.
- At $r = 10$: all three pairs simultaneously connect ⇒ triangle (1-cycle) born.
- At $r \to \infty$: 2-simplex (filled triangle) born ⇒ 1-cycle dies.

$H_1$ barcode for A: one bar with birth $r = 10$, death $r = 10 + \epsilon_{\mathrm{fill}}$ (V-R 1-cycle fills at edge length when triangle inequality first satisfied for clique completion).

For $K' = 3$ in isoceles arrangement (Configuration B at $t = 0$, sides 10, 8.60, 8.60):
- $r = 8.60$: edges (1,3), (2,3) born; no triangle yet.
- $r = 10$: edge (1,2) born ⇒ triangle born.
- 1-cycle birth: 10. Death: $10 + \epsilon$.

$H_1$ barcode for B: one bar, birth $r = 10$, death same scale as A.

**$H_1$ bars have same birth scale 10 for both A and B** — does *not* distinguish them. But $H_0$ does (per §4.3 MST argument).

### §6.2 H_1 utility in σ_rich pipeline

$H_1$ barcode is most useful when:
- Multiple loops form sequentially (4+ formations in arrangements with multiple cycles).
- Loop births/deaths track formation-cluster topology evolution.

For Phase 1 (NQ-242c with K=3), $H_1$ is mostly redundant. For Phase 2 onwards (K=4+ trajectories), $H_1$ becomes essential.

---

## §7. Phase 1 Numerical Pipeline Spec

### §7.1 Input

K-field gradient flow trajectory $\mathbf{u}(t) \in \widetilde\Sigma^K_M$, $t \in [0, T]$, sampled at $N$ time-points $t_0 < t_1 < \cdots < t_N$ with $N \geq 100$.

For NQ-242c: T²_20, K=3, T=200, dt=0.01 ⇒ 20000 raw steps; subsample to N=200 (every 100th step).

### §7.2 Steps

**Step P1.1 — Centroid extraction**:
For each $t_i$, compute $C(t_i) = \{c_j(t_i) : j \in \mathrm{act}(t_i)\}$ via §2.1 formula. Store as `(N, K_max, dim_X)` array with NaN for inactive formations.

**Step P1.2 — Pairwise distance matrix**:
For each $t_i$, compute the $K_{\mathrm{act}}(t_i) \times K_{\mathrm{act}}(t_i)$ distance matrix $D_i = (d_E(c_a, c_b))$ (Convention E for $T^2$).

**Step P1.3 — Static H_0 barcode per snapshot**:
For each $t_i$, compute $H_0$ barcode of $R_r(C(t_i))$ via Ripser/GUDHI library:
```python
import gudhi
rips = gudhi.RipsComplex(distance_matrix=D_i, max_edge_length=R_max)
st = rips.create_simplex_tree(max_dimension=1)
diag = st.persistence()
```

Output: list of $(K_{\mathrm{act}}(t_i) - 1)$ finite-bar death scales + 1 infinite bar.

**Step P1.4 — K-jump event detection**:
Compare $H_0$ barcode sizes at consecutive $t_i$. Whenever bar count drops by 1, register K-jump event at $t^* = (t_i + t_{i+1})/2$. Identify merger pair via the bar that disappeared (by tracking bar identities through nearest-neighbor matching).

**Step P1.5 — Zigzag persistence over time**:
Apply `gudhi.Zigzag_persistence` across all $t_i$ snapshots to obtain global zigzag barcode covering the full trajectory.

### §7.3 Output

Phase 1 deliverable: JSON file `CODE/scripts/results/sigma_rich_VR_phase1.json`:
```json
{
  "trajectory_id": "nq242c_A | nq242c_B | ...",
  "n_timepoints": 200,
  "T": 200,
  "K_max": 4,
  "centroids": "(N, K_max, 2) array, NaN for inactive",
  "K_act_trajectory": "(N,) integer array",
  "H_0_barcodes": "list of N barcodes (each a list of (birth, death) tuples)",
  "K_jump_events": [
    {"t_star": 45.5, "merger_pair": [1, 2], "bar_death_scale": 0.05},
    ...
  ],
  "zigzag_barcode": "global zigzag PH output",
  "metadata": {...}
}
```

### §7.4 Dependencies

- **NEW** `CODE/scc/centroid_trajectory.py`: implements §2 + Step P1.1.
- **NEW** `CODE/scc/vr_persistence.py`: wraps GUDHI/Ripser library calls (Step P1.3, P1.5).
- **NEW** `CODE/scc/k_jump_detector.py`: implements Step P1.4.
- **NEW** `CODE/scripts/sigma_rich_VR_phase1.py`: pipeline orchestrator.

External: `pip install gudhi` (or `ripser` for static H_0; `gudhi` required for zigzag).

### §7.5 Estimated runtime

- Trajectory simulation reuse from `nq242c_construction.py` (~10 min per config).
- Centroid extraction (200 timepoints): <1 min.
- H_0 barcodes per snapshot (Ripser): ~10 ms per snapshot × 200 = ~2 sec.
- Zigzag persistence (GUDHI): ~10-30 sec for 200-snapshot zigzag with K_max=4.
- **Total Phase 1 cost**: ~15 min per trajectory; ~30 min for both NQ-242c-A and -B.

---

## §8. Cat Status and Promotion

### §8.1 Phase 1 Cat status (target after W6 Day 3)

**Cat B target** for Phase 1 deliverable upon (P1.1)-(P1.5) successful execution + (C1)-(C4) of `nq242c_explicit_construction.md` §6.1 verified:
- $H_0$ barcode time-series numerically extracted for both A, B trajectories.
- K-jump events detected via $H_0$ bar-deaths.
- Zigzag barcode global view confirmed.

### §8.2 Phase 1 → Phase 2 progression

Phase 1 (W6 Day 1-3) → Phase 2 (W6 Day 4-7): zigzag persistence + Wigner-data extraction (per `sigma_rich_augmentation.md` §2.3.3) → full σ_rich pipeline.

Phase 2 deliverable: `CODE/scc/sigma_rich.py` complete module integrating centroid + orientation + Wigner-data + V-R PH.

### §8.3 Cat A path (post-Phase 4)

Phase 4 (W7-W8) NQ-242c-Rich combined run → Cat A target for the constructed example. Cat A everywhere requires (R1)-(R4) of `nq242c_explicit_construction.md` §6.2 — W9+ theoretical work.

### §8.4 Promotion target

CV-1.6 candidate Commitment 18 (proposed extension to Commitment 17 4-tool packet, per task #48 in TaskList): "σ_rich + V-R PH integrated framework" — Phase 1-4 numerical anchor + theoretical Cat status.

---

## §9. Hard Constraint Verification

- [x] **canonical 직접 수정 0** — `working/MF/` only.
- [x] **Silent resolution 0** — Cat status explicit at every stage. Phase 1 design only; numerical execution scheduled W6 Day 1-3.
- [x] **No Research OS resurrection** — single-topic working file (Phase 1 specifically).
- [x] **Not reductive** — V-R PH used contrastively (CN10): standard mathematical reformulation of K-jump topology, not external reduction. σ_rich is *richer* than V-R PH alone (per §4.3).
- [x] **u_t primitive maintained** — centroids derived from $u^{(j)}$; V-R PH operates on centroid configuration; no new primitive.
- [x] **CN5 4-energy not merged** — V-R PH is topological invariant of centroid configuration, not energy.
- [x] **K not dual-treated** — $K_{\mathrm{act}}(t)$ recovered from $H_0$ barcode (Claim 4.1) per Commitment 16.
- [x] **No metastability claim without P-F flag** — N/A.
- [x] **OP-0008 not silently resolved** — Phase 1 is *foundation* for Path B numerical anchor; OP-0008 severity 🟠 HIGH retained until full Cat A everywhere.

---

## §10. References

### §10.1 Working files

- `working/MF/sigma_rich_augmentation.md` (σ_rich definition; centroid component §2.3.1).
- `working/MF/nq242c_explicit_construction.md` (target numerical anchor for Phase 1 V-R pipeline).
- `working/MF/mathematical_scaffolding_4tools.md` §4 (Tool A3 PH foundation).
- `working/MF/sigma_multi_trajectory.md` §3.7 + §6.1 (PH reformulation + Phase 1-4 plan source).

### §10.2 Canonical refs

- `canonical/canonical.md` §11.1 Commitment 14, 14-Multi, 16; §13 T-σ-multi-A-Static; §14 CN5, CN10.
- `canonical/theorem_status.md` OP-0008.

### §10.3 External refs (PH library + theory)

- Cohen-Steiner, Edelsbrunner, Harer (2007) — bottleneck stability.
- Carlsson, de Silva, Morozov (2009) — zigzag persistence.
- Bauer (2021) — Ripser library.
- The GUDHI Project (2015) — zigzag persistence implementation.
- Edelsbrunner, Harer (2010) — Computational Topology textbook.
- Kim, Mémoli (2021) arXiv:1712.04064 — spatiotemporal persistent homology / formigrams.

---

**End of sigma_rich_VR_phase1.md.**

**Status: working draft. NQ-242 PH pipeline V-R Phase 1 design complete. Centroid trajectory $C(t)$ defined; V-R complex $R_r(C(t))$ on graph-metric instantiated; $H_0$ barcode ↔ $K_{\mathrm{act}}(t)$ + K-jump events ↔ $H_0$ bar-deaths formal mappings established. Phase 1 numerical pipeline spec (§7) with 5-step procedure + JSON output schema + GUDHI/Ripser dependencies. Cat B target upon W6 Day 1-3 execution. Promotion target CV-1.6 candidate Commitment 18 (task #48 future). Hard constraints all checked.**

**File:** `/Users/ojaehong/Perception/Perception_theory/THEORY/working/MF/sigma_rich_VR_phase1.md`
**Created:** 2026-04-30 (W5 Day 4).
**Promotion target:** CV-1.6 W6 Day 7 packet.
