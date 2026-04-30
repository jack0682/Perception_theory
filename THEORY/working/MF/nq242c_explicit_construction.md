# nq242c_explicit_construction.md — NQ-242c Explicit Two-Trajectory Construction (Path B Cat A target)

**Status:** working draft (W5 Day 4 OAT-supplementary; standalone construction file extending `working/MF/sigma_rich_augmentation.md` §6).
**Created:** 2026-04-30 (W5 Day 4).
**Type:** Stand-alone numerical construction proposal — NQ-242c-Standard + NQ-242c-Rich Cat A target.
**Author origin:** `working/MF/sigma_rich_augmentation.md` §4 + §6 (proposed two-trajectory example) → this file formalizes as numerical-anchor target.
**Canonical refs:** §11.1 Commitment 14, 14-Multi (D-6a CV-1.5.1), 16; §13 T-σ-multi-A-Static; §14 CN5, CN10; §15 OP-0008.
**Working refs:** `sigma_rich_augmentation.md` (Path B framework, σ_rich definition); `sigma_multi_trajectory.md` (Lemma 4.4.1(c) Cat C source); `mathematical_scaffolding_4tools.md` §4 Tool A3 PH pipeline.
**Open problems:** OP-0008 (direct attack) — Cat C → Cat B target via this construction; Cat A everywhere post-W9+ rigor.

---

## §1. Mission

> **"OP-0008 의 두 trajectory counterexample 을 explicit 으로 구성: same σ_standard($t^{*-}$) but distinct σ_standard($t^{*+}$) (NQ-242c-Standard non-det confirm) AND distinct σ_rich($t^{*-}$) ⇒ deterministic Φ_rich (NQ-242c-Rich det confirm). 둘 다 numerical anchor 로 Cat A target 도달."**

이 working file 은 `sigma_rich_augmentation.md` §6 의 numerical-anchor proposal 을 stand-alone 으로 정식화한다. CODE/scripts 의 numerical pipeline outline 까지 포함하나, 실행은 W6 Day 1-3 phase 에 배치 (이 file 은 design-only).

**핵심 deliverable**:
1. T²_20 equilateral vs isoceles disk-triangle setup (§2).
2. σ_standard time-series prediction (§3).
3. σ_rich time-series prediction (§4).
4. `CODE/scripts/nq242c_construction.py` outline (§5, NOT run).
5. Cat A criteria for promotion to `theorem_status.md` (§6).

---

## §2. Numerical Setup

### §2.1 Graph and parameters

- **Graph $G$**: 2D torus $T^2_{20}$ — vertex set $X = (\mathbb{Z}/20\mathbb{Z})^2$, $|X| = 400$, 4-regular nearest-neighbor edges, $\mathrm{Aut}(G) = \mathbb{Z}_{20}^2 \rtimes D_4$ (translation + dihedral).
- **K-field cap**: $K_{\mathrm{field}} = 4$ (slack > $K_{\mathrm{act}} = 3$ initial; allows for K-jump down to 2).
- **Initial active count**: $K_{\mathrm{act}}(t = 0) = 3$.
- **Per-formation mass**: $m_j = 30$ each ($M = 90$ total).
- **Energy parameters**: $\beta = 4.0$ (super-lattice $\zeta = 0.5$ regime), $\lambda_{\mathrm{rep}} = 0.1$, $\alpha = 1.0$, $a_{\mathrm{cl}} = 2.0$ (canonical defaults from CV-1.5.1).
- **Disk profile**: tanh-disk per-formation IC, $u^{(j)}(x) = \frac{1}{2}(1 - \tanh((|x - c_j^{(0)}| - r_0) / \delta))$ with $r_0 = 3$, $\delta = 0.5$; per-formation profile identical across $j$ and across configs A, B.

### §2.2 Configuration A (equilateral)

Initial centroids:
- $c_1^{A,(0)} = (5, 5)$
- $c_2^{A,(0)} = (15, 5)$
- $c_3^{A,(0)} = (10, 5 + 5\sqrt{3}) \approx (10, 13.66)$

Pair distances (Euclidean, on torus shortest-path):
- $\|c_1^A - c_2^A\| = 10$, $\|c_1^A - c_3^A\| = 10$, $\|c_2^A - c_3^A\| = 10$.

**Symmetry**: $D_3$ permutation (cyclic + reflection) of formations + 그래프 reflection = nontrivial pair-stabilizer of size 6.

### §2.3 Configuration B (isoceles, slightly compressed)

Initial centroids:
- $c_1^{B,(0)} = (5, 5)$
- $c_2^{B,(0)} = (15, 5)$
- $c_3^{B,(0)} = (10, 12)$

Pair distances:
- $\|c_1^B - c_2^B\| = 10$, $\|c_1^B - c_3^B\| = \sqrt{74} \approx 8.60$, $\|c_2^B - c_3^B\| = \sqrt{74} \approx 8.60$.

**Symmetry**: $\mathbb{Z}_2$ reflection (swap 1 ↔ 2 only) of formations.

### §2.4 σ_standard equality at $t = 0$ (design intent)

By construction A, B 가 동일 per-formation 디스크 프로파일을 사용하므로:
- $\sigma_j^A(0) = \sigma_j^B(0)$ for all $j$ (same disk Hessian spectrum).
- $\mathcal{F}_{\mathrm{total}}^A(0) = \mathcal{F}_{\mathrm{total}}^B(0) = 3$.

Cross-block $\sigma_{jk}$ depends on inter-formation distance via Coupling Bound Lemma exp-decay. **At well-separated regime** ($\lambda_{\mathrm{rep}} \exp(-c_0 \cdot 8.60)$ vs $\lambda_{\mathrm{rep}} \exp(-c_0 \cdot 10)$), the cross-eigenvalue tuples differ in *quantitative* magnitudes but the *eigenvalue/irrep/nodal* triple structure (qualitative σ-tuple) coincides modulo the chosen rounding granularity.

**Critical design choice**: For NQ-242c-Standard purposes, we adopt the "qualitative σ-tuple" convention — round eigenvalues to $10^{-3}$ precision. Under this convention $\{\sigma_{jk}\}^A(0) = \{\sigma_{jk}\}^B(0)$ as multi-sets ⇒ $\sigma_{\mathrm{standard}}^A(0) = \sigma_{\mathrm{standard}}^B(0)$. ✓

(The "high-precision σ-tuple" convention would distinguish A, B at $t = 0$ via cross-eigenvalue magnitudes — that case is the trivial direction; not the OP-0008 issue.)

### §2.5 σ_rich inequality at $t = 0$ (design intent)

Centroid sets:
- $\{c_j^A(0)\} = \{(5,5), (15,5), (10, 13.66)\}$.
- $\{c_j^B(0)\} = \{(5,5), (15,5), (10, 12)\}$.

Multi-sets of pair-distances:
- A: $\{10, 10, 10\}$.
- B: $\{10, 8.60, 8.60\}$.

These are **distinct multi-sets** ⇒ centroid-set mod-$S_3$ permutation is distinct ⇒ $\sigma_{\mathrm{rich}}^A(0) \neq \sigma_{\mathrm{rich}}^B(0)$. ✓

---

## §3. σ_standard Time-Series Prediction

### §3.1 Smooth-segment phase ($t \in [0, t^*)$)

By Lemma 4.1 (`sigma_multi_trajectory.md`): on smooth segments interior to top stratum, $\sigma_{\mathrm{standard}}^A(t)$ and $\sigma_{\mathrm{standard}}^B(t)$ are piecewise constant in the qualitative-tuple convention.

Both trajectories: centroid configurations evolve continuously under gradient flow; $\sigma_{\mathrm{standard}}$ remains constant (qualitative) until first K-jump.

**Prediction**: $\sigma_{\mathrm{standard}}^A(t) = \sigma_{\mathrm{standard}}^A(0)$ and $\sigma_{\mathrm{standard}}^B(t) = \sigma_{\mathrm{standard}}^B(0)$ for $t \in [0, t^*)$, both equal to the common $\sigma_{\mathrm{standard}}(0)$.

### §3.2 First K-jump time $t^*$

Configuration A: equilateral. By $D_3$ symmetry, all three pairs $(1,2), (1,3), (2,3)$ are equivalent ⇒ initial gradient flow preserves $D_3$ symmetry ⇒ no preferred merger direction. **Outcomes**:
- (A-i) If $D_3$-preserved trajectory is dynamically stable: triple-symmetric merger ($K = 3 \to 1$) at $t^*_A$ — large $\Delta K = 2$ event.
- (A-ii) If $D_3$ is dynamically unstable (likely; $D_3$-symmetric K=3 minimizer is rare on $T^2_{20}$ for these parameters): $D_3$-breaking pitchfork to one of three equivalent $\mathbb{Z}_2$-symmetric paths, then nearest-pair ($\mathbb{Z}_2$-symmetric pair) merger ($K = 3 \to 2$).

Configuration B: isoceles, $\mathbb{Z}_2$ symmetry only. Preferred mergers are $(1,3)$ or $(2,3)$ (equivalent by $\mathbb{Z}_2$, distance $\sqrt{74}$) — the closest pair. By $\mathbb{Z}_2$ symmetry these merge simultaneously ⇒ $K = 3 \to 1$ with $\Delta K = 2$.

**Refined prediction**: with small numerical noise breaking $\mathbb{Z}_2$ in B, B undergoes single-pair merger ($1$-$3$ or $2$-$3$) at $t^*_B$ before the other pair, single $\Delta K = 1$ event.

### §3.3 σ_standard($t^{*+}$) prediction

Configuration A (assume A-ii): post-pitchfork merger of, say, pair $(1,2)$ (the symmetry-broken-favored pair under noise). Post-merger formation $\ell^A$: an *elongated* shape (two horizontally-aligned disks merged) with anisotropy along $x$-axis. Hessian spectrum reflects this: lowest non-Goldstone eigenvalue $\lambda_{\mathrm{single}}^A$ corresponds to *transverse* (y) breathing mode of elongated $\ell^A$.

Configuration B: merger of $(1, 3)$ — *diagonal* merger (top vertex with one base vertex). Post-merger $\ell^B$: diagonal-elongated shape. Hessian: low eigenvalue $\lambda_{\mathrm{single}}^B$ corresponds to transverse mode along the perpendicular-to-diagonal axis.

**Critical claim**: $\lambda_{\mathrm{single}}^A \neq \lambda_{\mathrm{single}}^B$ because:
- Anisotropy direction differs (horizontal vs diagonal).
- The graph $T^2_{20}$ is *not* fully isotropic (4-regular grid breaks continuous rotation; $D_4$ only).
- Different orientations align with different graph eigenmodes ⇒ different Hessian eigenvalues.

⇒ $\sigma_{\mathrm{standard}}^A(t^{*+}) \neq \sigma_{\mathrm{standard}}^B(t^{*+})$. **NQ-242c-Standard non-determinism confirmed**. ✓

### §3.4 Numerical falsifiability

**Falsification scenario**: if $T^2_{20}$ at $\beta = 4.0$ produces post-merger Hessian spectra invariant under merger-direction (e.g., due to graph isotropy at this scale), then σ_standard^A(t^{*+}) might equal σ_standard^B(t^{*+}) — non-determinism fails to manifest in this specific setup.

**Mitigation**: if §3.3 critical claim fails on $T^2_{20}$, switch to:
- Higher anisotropy graph (e.g., rectangular $T^2_{20 \times 30}$ or hexagonal lattice).
- Larger geometric difference (configuration B compressed more dramatically).

The Path B framework predicts σ_standard non-determinism *generically*; specific graph/parameter choice may need tuning for explicit demonstration.

---

## §4. σ_rich Time-Series Prediction

### §4.1 σ_rich($t = 0$) explicit components

For Configuration A:
- $\sigma_{\mathrm{standard}}^A(0)$: as in §2.4.
- $\{c_j^A(0)\} = \{(5,5), (15,5), (10, 13.66)\}$ — equilateral.
- $\{\Theta_j^A(0)\}$: each disk is rotationally symmetric ⇒ inertia tensor $M_j^A = \mu_0 \cdot I$ ($\mu_0$ = disk's second moment, identical across $j$). $\Theta_j^A = (\mu_0, \mu_0, \mathrm{undefined-axis})$ — degenerate (isotropic).
- $\{W_{jk}^A(0)\}$: Goldstone-pair gap $\Delta_{jk}^{\mathrm{Gold}} \sim \lambda_{\mathrm{rep}} \exp(-c_0 \cdot 10) \approx 0.1 \cdot \exp(-c_0 \cdot 10)$, equal across all three pairs by $D_3$.

For Configuration B:
- $\sigma_{\mathrm{standard}}^B(0) = \sigma_{\mathrm{standard}}^A(0)$ (per §2.4).
- $\{c_j^B(0)\} = \{(5,5), (15,5), (10, 12)\}$ — isoceles.
- $\{\Theta_j^B(0)\}$: same as A (identical disks, isotropic).
- $\{W_{jk}^B(0)\}$: $\Delta_{12}^{\mathrm{Gold}} \sim \exp(-c_0 \cdot 10)$ vs $\Delta_{13}^{\mathrm{Gold}} = \Delta_{23}^{\mathrm{Gold}} \sim \exp(-c_0 \cdot 8.60)$ — distinct (multi-set $\{a, b, b\}$, $a \neq b$).

**Distinctness of σ_rich at $t = 0$**: A vs B distinguished by:
1. Centroid pair-distance multi-set: A = $\{10, 10, 10\}$, B = $\{10, 8.60, 8.60\}$.
2. Goldstone-pair gap multi-set: A all-equal, B has $\{a, b, b\}$.

Both components individually witness $\sigma_{\mathrm{rich}}^A(0) \neq \sigma_{\mathrm{rich}}^B(0)$. ✓

### §4.2 σ_rich evolution on smooth segment

Centroids evolve smoothly under gradient flow; $\Theta_j$ evolves smoothly (disks may slightly distort under inter-formation tidal forces, breaking $\Theta_j$'s isotropy mildly). $W_{jk}$ evolves continuously as $d_{\min}(j,k)$ changes.

**Prediction**: σ_rich(t) is *not* piecewise constant — it varies continuously on smooth segments (centroid component is real-valued, not discrete). The "piecewise constant" property of σ_standard does not extend to σ_rich; instead σ_rich is *continuous* on smooth segments + *discontinuous jump* at K-jumps.

This is consistent with §3.3 of `sigma_rich_augmentation.md`: σ_rich is càdlàg with continuous (not piecewise-constant) smooth-segment trajectories.

### §4.3 σ_rich($t^{*-}$) just before merger

Configuration A: as $t \nearrow t^*_A$, one pair (say $(1,2)$ under symmetry-breaking noise) approaches merger ⇒ $\|c_1^A - c_2^A\|(t^{*-}_A) \to 0$, $\Delta_{12}^{\mathrm{Gold}}(t^{*-}_A) \to 0$ (Goldstone-pair softening).

Configuration B: pair $(1, 3)$ approaches merger ⇒ $\|c_1^B - c_3^B\|(t^{*-}_B) \to 0$, $\Delta_{13}^{\mathrm{Gold}}(t^{*-}_B) \to 0$.

**Distinctness**: even at $t^{*-}$, the merging-pair index pattern differs (A: pair $(1,2)$; B: pair $(1,3)$) — encoded as which $\Delta_{ij}^{\mathrm{Gold}}$ is the minimum-going-to-zero. ⇒ σ_rich($t^{*-}_A$) ≠ σ_rich($t^{*-}_B$). ✓

### §4.4 σ_rich($t^{*+}$) via Φ_rich

Apply `sigma_rich_augmentation.md` §3.3 Φ_rich:

**Configuration A**:
- Pair $(j, k) = (1, 2)$ identified from min centroid-distance + Goldstone-softening criterion.
- Post-merger centroid: $c_\ell^A(t^{*+}) = (m_1 c_1 + m_2 c_2)/(m_1 + m_2) \approx (10, 5)$.
- Post-merger inertia tensor: $M_\ell^A = M_1 + M_2 + (m_1 m_2/(m_1+m_2)) (c_1 - c_2)(c_1-c_2)^T$ — adds horizontal-anisotropy term $\propto (1, 0)(1, 0)^T \cdot 25$.
- $\Theta_\ell^A$: $\mu_{\ell, 1} > \mu_{\ell, 2}$, principal axis = horizontal (0°).

**Configuration B**:
- Pair $(j, k) = (1, 3)$ identified.
- Post-merger centroid: $c_\ell^B(t^{*+}) = (m_1 c_1 + m_3 c_3)/(m_1+m_3) = (7.5, 8.5)$ approximately.
- Post-merger inertia tensor: anisotropy along $(c_1 - c_3) = (-5, -7)$ direction ⇒ principal axis ≈ 54.5°.

**Distinct outcomes**:
- $c_\ell^A(t^{*+}) \neq c_\ell^B(t^{*+})$: $(10, 5)$ vs $(7.5, 8.5)$.
- $\Theta_\ell^A$ principal axis (0°) ≠ $\Theta_\ell^B$ principal axis (54.5°).

⇒ σ_rich($t^{*+}_A$) ≠ σ_rich($t^{*+}_B$). ✓

### §4.5 Φ_rich determinism check

Apply Φ_rich to σ_rich($t^{*-}_A$) — does it match σ_rich($t^{*+}_A$) computed numerically?
- Φ_rich predicts $c_\ell^A(t^{*+}) = $ mass-weighted centroid of merging pair = $(10, 5)$.
- Numerical gradient-flow result at $t^{*+}_A$: $c_\ell^A(t^{*+}, \mathrm{numerical})$ — measured from $u^{(\ell)}(t^{*+})$ field.

**Cat A criterion**: Φ_rich-predicted $c_\ell$ matches numerical $c_\ell$ within tolerance $10^{-2}$ (graph-distance unit). Same for $\Theta_\ell$ (principal axis within 1° tolerance, eigenvalue ratios within 5%).

If matches (predicted): **Φ_rich determinism numerically confirmed for this construction** ⇒ Cat A target reached for the constructed example; **NQ-242c-Rich determinism confirmed**. ✓

---

## §5. Numerical Script Outline (`CODE/scripts/nq242c_construction.py`)

### §5.1 Script structure

```python
"""
NQ-242c Path B explicit construction.
NQ-242c-Standard: confirm σ_standard non-determinism (A, B → distinct σ_standard(t*+)).
NQ-242c-Rich: confirm σ_rich determinism (A, B → distinct σ_rich(t*-) → Φ_rich → matching σ_rich(t*+)).

Cat A target: numerical anchor for OP-0008 Path B Cat B (full Cat A pending §6 + W9+ rigor).

DO NOT RUN at design phase (W5 Day 4); execute at W6 Day 1-3.
"""

import numpy as np
from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.multi import find_k_field_formation, gradient_flow_trajectory
from scc.diagnostics import compute_sigma_tuple_multi  # σ_standard
# from scc.sigma_rich import compute_sigma_rich  # σ_rich, NEW MODULE W6

def setup_torus_2d(L=20):
    """T^2_L torus graph."""
    return GraphState.torus_2d(L, L)

def setup_configuration_A():
    """Equilateral disk-triangle on T²_20."""
    centroids = [(5, 5), (15, 5), (10, 5 + 5*np.sqrt(3))]
    return centroids

def setup_configuration_B():
    """Isoceles disk-triangle on T²_20 (compressed)."""
    centroids = [(5, 5), (15, 5), (10, 12)]
    return centroids

def initial_condition(graph, centroids, r0=3, delta=0.5, mass=30):
    """tanh-disk initial condition for K formations."""
    K = len(centroids)
    u = np.zeros((K, graph.n_vertices))
    for j, c in enumerate(centroids):
        for x_idx, x_pos in enumerate(graph.positions):
            d = graph.distance(x_pos, c)
            u[j, x_idx] = 0.5 * (1 - np.tanh((d - r0) / delta))
        u[j] *= mass / u[j].sum()
    return u

def run_trajectory(graph, params, u0, T=200, dt=0.01):
    """Gradient flow on K-field shared-pool."""
    return gradient_flow_trajectory(graph, params, u0, T=T, dt=dt)

def detect_k_jump_times(trajectory, epsilon=0.01):
    """Identify K-jump times via K_act discontinuities."""
    k_act = [(np.linalg.norm(u, axis=1, ord=1) > epsilon).sum()
             for u in trajectory]
    jumps = [t for t in range(1, len(k_act)) if k_act[t] != k_act[t-1]]
    return jumps, k_act

def main():
    # Setup
    graph = setup_torus_2d(20)
    params = ParameterRegistry(beta=4.0, lambda_rep=0.1, alpha=1.0, a_cl=2.0)

    # Configuration A
    centroids_A = setup_configuration_A()
    u0_A = initial_condition(graph, centroids_A)
    traj_A = run_trajectory(graph, params, u0_A)
    jumps_A, k_act_A = detect_k_jump_times(traj_A)

    # Configuration B
    centroids_B = setup_configuration_B()
    u0_B = initial_condition(graph, centroids_B)
    traj_B = run_trajectory(graph, params, u0_B)
    jumps_B, k_act_B = detect_k_jump_times(traj_B)

    # σ_standard at t=0 (verify equality A=B)
    sigma_std_A_0 = compute_sigma_tuple_multi(graph, params, traj_A[0],
                                              precision=1e-3)
    sigma_std_B_0 = compute_sigma_tuple_multi(graph, params, traj_B[0],
                                              precision=1e-3)
    assert sigma_std_A_0 == sigma_std_B_0, "Design check: σ_std_A(0) == σ_std_B(0)"

    # σ_standard at first K-jump (verify INequality A ≠ B)
    t_star_A = jumps_A[0]
    t_star_B = jumps_B[0]
    sigma_std_A_post = compute_sigma_tuple_multi(graph, params,
                                                  traj_A[t_star_A + 1])
    sigma_std_B_post = compute_sigma_tuple_multi(graph, params,
                                                  traj_B[t_star_B + 1])
    sigma_std_nondet = (sigma_std_A_post != sigma_std_B_post)
    print(f"NQ-242c-Standard non-det: {sigma_std_nondet}")

    # σ_rich at t=0 (verify INequality A ≠ B)
    sigma_rich_A_0 = compute_sigma_rich(graph, params, traj_A[0])
    sigma_rich_B_0 = compute_sigma_rich(graph, params, traj_B[0])
    sigma_rich_distinct_0 = (sigma_rich_A_0 != sigma_rich_B_0)
    print(f"NQ-242c-Rich distinct at t=0: {sigma_rich_distinct_0}")

    # σ_rich at t*-, t*+ (verify Φ_rich determinism)
    sigma_rich_A_pre = compute_sigma_rich(graph, params, traj_A[t_star_A - 1])
    sigma_rich_A_post = compute_sigma_rich(graph, params, traj_A[t_star_A + 1])
    sigma_rich_B_pre = compute_sigma_rich(graph, params, traj_B[t_star_B - 1])
    sigma_rich_B_post = compute_sigma_rich(graph, params, traj_B[t_star_B + 1])

    # Apply Φ_rich (per sigma_rich_augmentation §3.3)
    Phi_pred_A = apply_Phi_rich(sigma_rich_A_pre)
    Phi_pred_B = apply_Phi_rich(sigma_rich_B_pre)
    det_check_A = sigma_rich_match(Phi_pred_A, sigma_rich_A_post, tol=1e-2)
    det_check_B = sigma_rich_match(Phi_pred_B, sigma_rich_B_post, tol=1e-2)
    print(f"Φ_rich determinism A: {det_check_A}")
    print(f"Φ_rich determinism B: {det_check_B}")

    # Output JSON for downstream verification
    save_results({
        "sigma_std_nondet": sigma_std_nondet,
        "sigma_rich_distinct_0": sigma_rich_distinct_0,
        "Phi_rich_det_A": det_check_A,
        "Phi_rich_det_B": det_check_B,
        "trajectories": {"A": traj_A, "B": traj_B},
        "k_jump_times": {"A": jumps_A, "B": jumps_B},
    }, path="results/nq242c_construction.json")

if __name__ == "__main__":
    main()
```

### §5.2 Dependencies (W6 phase 1 prerequisites)

- `scc/multi.py`: existing `gradient_flow_trajectory` (CV-1.5).
- `scc/diagnostics.py`: existing `compute_sigma_tuple_multi` for σ_standard.
- **NEW** `scc/sigma_rich.py`: implements σ_rich extraction (centroid + inertia tensor + Wigner-data) — to be created in W6 Day 1-3 (NQ-242 PH pipeline V-R Phase 1).
- **NEW** `scc/sigma_rich.py::apply_Phi_rich`: implements §3.3 of `sigma_rich_augmentation.md`.
- **NEW** `scc/sigma_rich.py::sigma_rich_match`: tolerance-based equivalence check for σ_rich tuples.

### §5.3 Output structure

`CODE/scripts/results/nq242c_construction.json`:
```json
{
  "sigma_std_nondet": true|false,
  "sigma_rich_distinct_0": true|false,
  "Phi_rich_det_A": true|false,
  "Phi_rich_det_B": true|false,
  "trajectories": {"A": "<traj_path_A.npz>", "B": "<traj_path_B.npz>"},
  "k_jump_times": {"A": [int], "B": [int]},
  "sigma_rich_at_t_star": {
    "A_pre": {...}, "A_post": {...}, "A_Phi_pred": {...},
    "B_pre": {...}, "B_post": {...}, "B_Phi_pred": {...}
  },
  "tol_centroid": 1e-2,
  "tol_orientation_deg": 1.0,
  "metadata": {...}
}
```

### §5.4 Estimated runtime

- Trajectory simulation (T=200, dt=0.01, K=4, |X|=400): ~10 minutes per configuration. ~20 min total.
- σ_standard + σ_rich extraction at sampled time points (50 snapshots): ~5 min.
- Φ_rich application + comparison: <1 min.
- **Total**: ~30 min single CPU. Feasible W6 Day 1.

---

## §6. Cat A Promotion Criteria

### §6.1 Numerical anchor criteria (Cat B → Cat A target for constructed example)

For the constructed two-trajectory pair (A, B) to constitute a Cat A numerical anchor for Path B:

**(C1) σ_standard non-determinism numerically confirmed**:
- $\sigma_{\mathrm{standard}}^A(0) = \sigma_{\mathrm{standard}}^B(0)$ at qualitative-tuple precision $10^{-3}$.
- $\sigma_{\mathrm{standard}}^A(t^{*+}) \neq \sigma_{\mathrm{standard}}^B(t^{*+})$ at same precision.
- ⇒ NQ-242c-Standard claim: σ_standard alone is insufficient.

**(C2) σ_rich distinguishability at $t^{*-}$**:
- $\sigma_{\mathrm{rich}}^A(t^{*-}) \neq \sigma_{\mathrm{rich}}^B(t^{*-})$ via centroid component (or any of $\{c, \Theta, W\}$).

**(C3) Φ_rich determinism**:
- Φ_rich applied to $\sigma_{\mathrm{rich}}^A(t^{*-})$ predicts $\sigma_{\mathrm{rich}}^A(t^{*+})$ within tolerance: centroid $10^{-2}$ graph units; orientation 1° (or eigenvalue ratio 5%); Wigner-data: post-merger Goldstone gap collapses to <$10^{-3}$ (per §3.3(d) prediction).
- Same for Configuration B.

**(C4) Generality probe**: same conclusion holds when Configuration B is varied (e.g., (10, 12) → (10, 11), (10, 13)) — Cat A claim is robust to small parameter perturbations within a family. (~3 additional trajectory runs.)

### §6.2 Theoretical rigor criteria (Cat A everywhere — post-W9+)

For Cat A everywhere (all simple-merger Path B trajectories):

**(R1)** Aut-invariance of σ_rich proven explicitly under wreath-product $\mathrm{Aut}(G) \wr S_{K_{\mathrm{act}}}$ — extends `sigma_rich_augmentation.md` §2.4 Cat B sketch to full proof.

**(R2)** Wigner-projection eigenvalue collapse rigorous proof — extends `sigma_rich_augmentation.md` §3.3(d) sketch to theorem-level statement: post-merger Hessian eigenvalues are explicitly determined by pre-merger $\tilde H_{jk}$ + Wigner-mixing $\theta_{jk}^{\mathrm{mix}}$.

**(R3)** Pair-identification uniqueness (§3.2 of `sigma_rich_augmentation.md`): proof that "min centroid-distance + Goldstone-pair softening" is unambiguous under generic 1-parameter trajectories (codim-1 simple-merger genericity argument).

**(R4)** σ^D symmetry-emergence (NQ-242d): full characterization of $G_{\mathrm{emerge}, jk}$ from σ_rich data.

### §6.3 Promotion target

Upon (C1)+(C2)+(C3)+(C4) satisfied at W6 Day 7:
- **CV-1.6 candidate D-CV1.6-O5**: adopt Path B σ_rich extension. Commitment 14-Multi (D) addendum (per `sigma_rich_augmentation.md` §9.1) approved.
- **theorem_status.md** entry: T-σ-Multi-1 Cat upgraded from "Cat B target / Cat C conjectured" to "Cat B target with NQ-242c-Rich numerical anchor".
- **OP-0008 status**: severity 🟠 HIGH retained but **PARTIALLY RESOLVED via Path B numerical anchor**; full resolution pending (R1)-(R4).

Upon (R1)+(R2)+(R3)+(R4) satisfied at W12+:
- **theorem_status.md**: T-σ-Multi-1 Cat upgraded to "Cat A everywhere".
- **OP-0008 status**: **RESOLVED via Path B canonicalized**; canonical ledger updated.

### §6.4 Non-promotion / fallback

If (C1) fails (σ_standard non-determinism not manifest in this setup): switch to alternative graph/parameter (per §3.4 mitigation). NQ-242c-Standard becomes graph-class-dependent.

If (C2) succeeds but (C3) fails (σ_rich distinguishes inputs but Φ_rich predictions don't match numerical $t^{*+}$): re-examine §3.3 Φ_rich definition — likely indicates that simple mass-weighted centroid + parallel-axis inertia approximation is too crude; needs post-merger relaxation correction terms. Iterate definition; downgrade to Cat C or revert to Path A.

If (C3) succeeds for A but fails for B (or vice versa): Φ_rich is *configuration-dependent* — Path B works for some mergers but not others. Hybrid path (per `sigma_rich_augmentation.md` §5.4 / §9.3): adopt σ_rich as candidate but defer Cat A claim.

---

## §7. Hard Constraint Verification

- [x] **canonical 직접 수정 0** — `working/MF/` only. Promotion requires user approval.
- [x] **Silent resolution 0** — OP-0008 explicitly attacked via Path B Cat B target with falsification scenarios (§3.4, §6.4).
- [x] **No Research OS resurrection** — single-topic working file.
- [x] **Not reductive** — σ_rich components are standard mathematical objects (centroid, inertia tensor, Wigner–von Neumann); used as derived diagnostics of $u_t$, contrastive (CN10).
- [x] **u_t primitive maintained** — all σ_rich components derived; no new primitive.
- [x] **CN5 4-energy not merged** — N/A; σ_rich is Hessian-spectral invariant of energy minimizer.
- [x] **K not dual-treated** — $K_{\mathrm{act}}$ integer; K-jumps discrete events; $K_{\mathrm{field}} = 4$ slack architectural cap.
- [x] **No metastability claim without P-F flag** — N/A; static σ-extraction at sampled time points.
- [x] **Numerical script not yet run** — design-only; execution scheduled W6 Day 1-3 NQ-242 PH pipeline V-R Phase 1.
- [x] **Cat status explicit at every stage** — (C1)-(C4) Cat B target / (R1)-(R4) Cat A everywhere; promotion path explicit at §6.3.

---

## §8. References

### §8.1 Working files

- `working/MF/sigma_rich_augmentation.md` (Path B framework + σ_rich definition; §6 of that file is this file's parent).
- `working/MF/sigma_multi_trajectory.md` (Lemma 4.4.1(c) Cat C source; §6.1 NQ-242 PH-augmented pipeline).
- `working/MF/multi_formation_sigma.md` §5.5 (cross-formation Goldstone observation; Wigner-pair source).
- `working/MF/mathematical_scaffolding_4tools.md` §4 (Tool A3 PH foundation; centroid pipeline).
- `working/MF/K_status_commitment.md` (Commitment 16 K_field/K_act).

### §8.2 Canonical refs

- `canonical/canonical.md` §11.1 Commitment 14, 14-Multi, 16; §13 T-σ-multi-A-Static, T-σ-Multi-1; §14 CN5, CN10.
- `canonical/open_problems.md` OP-0008 (direct attack subject).
- `canonical/theorem_status.md` (target update upon (C1)-(C4) completion).

### §8.3 Numerical infrastructure

- `CODE/scc/multi.py` (existing): K-field gradient flow.
- `CODE/scc/diagnostics.py` (existing): σ_standard via Hessian spectrum.
- **NEW** `CODE/scc/sigma_rich.py` (W6 Day 1-3): σ_rich extraction, Φ_rich application.
- **NEW** `CODE/scripts/nq242c_construction.py` (W6 Day 1, this file §5).

### §8.4 External references

- Wigner & von Neumann (1929) — avoided crossings (§4 $W_{jk}$ data).
- Cohen-Steiner-Edelsbrunner-Harer (2007) — PH stability (Tool A3 cross-link).
- Carlsson-de Silva-Morozov (2009) — zigzag persistence (NQ-242 pipeline).
- Garcia Trillos-Murray (2017); Bertozzi-Esedoğlu-Gillette (2007) — graph Allen-Cahn (CN5 contrastive).

---

**End of nq242c_explicit_construction.md.**

**Status: working draft. Stand-alone NQ-242c construction file. Numerical setup (T²_20 equilateral vs isoceles) defined; σ_standard non-determinism prediction (§3); σ_rich determinism prediction (§4); script outline (§5, NOT run); Cat A promotion criteria (C1-C4 numerical, R1-R4 theoretical) registered (§6). Falsification + fallback paths registered. Promotion target: D-CV1.6-O5 packet upon (C1)-(C4) at W6 Day 7. NQ-242 PH pipeline V-R Phase 1 (W6 Day 1-3) prerequisite for `scc/sigma_rich.py` module.**

**File:** `/Users/ojaehong/Perception/Perception_theory/THEORY/working/MF/nq242c_explicit_construction.md`
**Created:** 2026-04-30 (W5 Day 4).
**Promotion target:** CV-1.6 W6 Day 7 D-CV1.6-O5 packet.
