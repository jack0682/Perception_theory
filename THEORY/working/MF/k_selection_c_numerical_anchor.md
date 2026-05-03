# k_selection_c_numerical_anchor.md — K-Selection (c) Symmetry-Broken Numerical Anchor

**Status:** working draft (W5 Day 4, Task #7).
**Created:** 2026-04-30 (W5 Day 4).
**Type:** Numerical anchor design for K-Selection mechanism — option (c) of OP-0005 4-option list. Empirical validation target for Tasks #5 (free-energy) + #6 (Kramers) predictions.
**Author origin:** Task #7 K-Selection (c); empirical complement to Tasks #5, #6. Companion to Task #8 (compatibility proof).
**Canonical refs:** §11.1 Commitment 14, 14-Multi, 16; §13 T-Persist-K family; §14 CN15; §15 OP-0005.
**Working refs:** `k_selection_a_free_energy.md` (Task #5; equilibrium $K^*_{\mathrm{eq}}(T)$ + crossover $T_c$ predictions); `k_selection_b_kramers.md` (Task #6; barrier-scaling + V4 $t^{1.315}$ predictions); `nq242c_explicit_construction.md` (companion numerical script template).

---

## §1. Mission

> **"OP-0005 K-Selection 4-옵션 중 (c) symmetry-broken numerical anchor: gradient flow trajectory 에서 $K_{\mathrm{act}}(t)$, K-jump 시간 통계 $\Delta t_n$, barrier scaling $\Delta E_n$ 를 측정하여 Tasks #5+#6 예측을 empirical 검증. 7개 specific measurements (M1-M7) 정의 + script outline 제공."**

이 working file 은 K-Selection mechanism 의 *empirical* 측면을 design — 어떤 numerical experiments 가 Tasks #5 (free-energy equilibrium $K^*_{\mathrm{eq}}(T)$, crossover $T_c$) 와 #6 (Kramers barriers, V4 scaling, LSW coarsening) 의 *quantitative predictions* 를 검증할 수 있는지 specify 한다.

**핵심 deliverable**: 7 specific measurements (M1-M7) + 4 graph-class anchors (T²_20, T²_30, R23, hexagonal) + script outline + Cat B target via successful (M1)-(M7).

---

## §2. Setup and Scope

### §2.1 Graph anchors

Four representative graphs:
- **A1: $T^2_{20}$** (2D torus, 400 vertices, $D_4$ + $\mathbb{Z}_{20}^2$ Aut). Standard Phase 10 V4 graph.
- **A2: $T^2_{30}$** (900 vertices). Larger torus to test size scaling.
- **A3: R23** (existing canonical dataset). Verifies σ-framework anchor at multi-formation level (per OAT-7 / OP-0009-Emp).
- **A4: Hexagonal lattice $H_{16}$** (16×16 ≈ 256 vertices, $D_6$ Aut). Tests Aut(G) class-dependence.

### §2.2 Parameters scan

- **Energy parameters**: $\beta \in \{2, 4, 6\}$ (super-lattice scale); $\lambda_{\mathrm{rep}} \in \{0.01, 0.1, 1.0\}$ (repulsion strength); $\alpha = 1.0$ (boundary); $a_{\mathrm{cl}} = 2.0$ (closure).
- **Temperature**: $T \in \{0, 10^{-4}, 10^{-3}, 10^{-2}, 10^{-1}\}$ (zero-noise default + 4 thermal levels). Implementation: Gaussian noise added to gradient-flow ODE.
- **Total mass**: $M \in \{40, 80, 160\}$ — varies $K_{\mathrm{eq}}^{\mathrm{kinetic}}$ (more mass ⇒ more formations supportable).
- **$K_{\mathrm{field}}$**: 4 (slack above expected $K_{\mathrm{eq}}$).

### §2.3 Out of scope

- 3D K-fields (NQ-244 W6+).
- Non-canonical embeddings (graph-class beyond A1-A4).
- Full Whitney-stratified Morse on $\widetilde\Sigma^K_M$ (NQ-248 W7+).

---

## §3. Seven Measurements (M1-M7)

### §3.1 M1: $K_{\mathrm{act}}(t)$ trajectory

**Goal**: measure $K_{\mathrm{act}}(t)$ as a function of time on each graph + parameter set.

**Method**: gradient flow with $K_{\mathrm{act}}(0) = K_{\mathrm{field}} = 4$ (random symmetry-broken IC); detect K-jumps via $\|u^{(j)}\|_1$ crossings.

**Output**: time-series $\{(t_i, K_{\mathrm{act}}(t_i))\}_{i=1}^N$ for each (graph, parameters, $T$, IC) configuration. ~50-100 trajectories.

**Validation target**: Tasks #5+#6 predictions on long-time $K_{\mathrm{eq}}^{\mathrm{kinetic}}$ vs $K^*_{\mathrm{eq}}(T)$.

### §3.2 M2: Crossover temperature $T_c$

**Goal**: measure $T_c$ at which equilibrium $K^*_{\mathrm{eq}}(T)$ jumps from 1 → 2 (and 2 → 3, etc.).

**Method**: at very long times ($t \to \infty$ approximation, $t = 10^4$ in numerical units), measure equilibrium distribution $\pi(K)$. Identify $T$ at which $\pi(1) = \pi(2)$ — the crossover.

Alternative: equilibrium ensemble approach — sample many IC's, measure $K_{\mathrm{eq}}^{\mathrm{kinetic}}$ distribution; cumulative shift indicates $T_c$.

**Output**: $T_c(\beta, \lambda_{\mathrm{rep}}, M, G)$ — table of crossover temperatures per parameter set.

**Validation target**: Task #5 §4.3 prediction $T_c = (\mathcal{E}^*_2 - \mathcal{E}^*_1) / (S(2) - S(1))$.

### §3.3 M3: K-jump time intervals $\Delta t_n$

**Goal**: measure consecutive K-jump time intervals; verify V4 scaling.

**Method**: from M1 trajectories, extract K-jump times $\{t_n\}$; compute $\Delta t_n = t_{n+1} - t_n$.

**Output**: log-log plot of $\Delta t_n$ vs $t_n$ + fitted exponent $\alpha$ where $\Delta t_n \propto t_n^\alpha$.

**Validation target**: 
- Task #6 §7 prediction $\alpha \approx 1.315$ (V4) or $\alpha = 4/3$ (LSW).
- Cross-graph universality: does $\alpha$ depend on graph class?

### §3.4 M4: Barrier height $\Delta E_n$

**Goal**: measure barrier height at each K-jump.

**Method**: at each K-jump time $t_n$, extract pre-merger configuration $\mathbf{u}(t_n^-)$ and post-merger $\mathbf{u}(t_n^+)$; compute energy at saddle (interpolation midpoint or nudged-elastic-band saddle search) minus min.

**Output**: $\{\Delta E_n\}$ time-series; scaling $\Delta E_n$ vs $K_n = K_{\mathrm{act}}(t_n)$.

**Validation target**: Task #6 §3.3 barrier scaling $\Delta E \sim \lambda_{\mathrm{rep}} m_j m_k / |X|^{d-2}$.

### §3.5 M5: Pair-distance at merger

**Goal**: measure inter-formation distance $d_{\min}(j, k)(t_n^-)$ at each K-jump.

**Method**: from M1 trajectories at K-jump times, identify merging pair $(j, k)$ via centroid-distance min (per `sigma_rich_phi_proof.md` Theorem 3.1); record $d_{\min}(j, k)$.

**Output**: distribution of $d_{\min}$ at K-jumps.

**Validation target**: Task #6 §3.3 prediction barrier ∝ $\exp(-c_0 d_{\min})$ ⇒ K-jumps occur at small $d_{\min}$.

### §3.6 M6: σ_rich vs σ_standard non-determinism

**Goal**: verify NQ-242c-Standard non-determinism + NQ-242c-Rich determinism.

**Method**: per `nq242c_explicit_construction.md` §6.2: equilateral A vs isoceles B disk-triangle on $T^2_{20}$; measure σ_standard, σ_rich at $t^{*-}, t^{*+}$.

**Output**: distinct σ_standard($t^{*+}_A$) vs σ_standard($t^{*+}_B$); Φ_rich-predicted vs numerical σ_rich($t^{*+}$) match within tolerance.

**Validation target**: OP-0008 Path B confirmation; (C1)+(C2)+(C3) of `nq242c_explicit_construction.md` §6.1.

### §3.7 M7: Cluster-level topology PH barcode

**Goal**: extract centroid Vietoris-Rips PH barcode + zigzag persistence, per `sigma_rich_VR_phase1.md` §7.

**Method**: from M1 trajectories, run Phase 1 numerical pipeline (P1.1-P1.5).

**Output**: $H_0$ barcodes per snapshot + zigzag PH global view + K-jump bar-deaths.

**Validation target**: $K_{\mathrm{act}}(t) = \dim H_0$ verification (Claim 4.1 of `sigma_rich_VR_phase1.md`); $H_0$ bar-death events match K-jump times from M1.

---

## §4. Graph-Class Anchor Specifications

### §4.1 A1: $T^2_{20}$ baseline

- Reuse Phase 10 V4 setup; verifies $\Delta t \propto t^{1.315}$ across new measurements (M3-M7).
- Default for NQ-242c-Rich (M6) per `nq242c_explicit_construction.md`.

### §4.2 A2: $T^2_{30}$ size scaling

- Tests $|X|$-dependence of $T_c$, barrier heights.
- Predicts: $T_c$ shifts as $\log |X|$ (Task #5 §4.3 with $S(2) - S(1) \sim \log |X|$).

### §4.3 A3: R23 dataset

- Multi-formation σ-framework Cat A claims (CV-1.5) anchored at F=1, F=2 only (per OP-0009-Emp).
- M6 + M7 on R23 high-F configurations validates σ-framework at empirical default ground state.

### §4.4 A4: Hexagonal $H_{16}$

- Different Aut(G) class ($D_6$ vs $D_4$).
- Tests cross-graph universality of barrier-scaling exponents.
- Predicts: same $\alpha = 4/3$ LSW exponent (universality); $T_c$ shifts due to different $S(K)$ counting.

---

## §5. Numerical Script Outline

### §5.1 Script structure

`CODE/scripts/k_selection_c_numerical.py`:
```python
"""
K-Selection (c) symmetry-broken numerical anchor.

Validates Task #5 free-energy predictions + Task #6 Kramers/LSW predictions
via 7 measurements (M1-M7) on 4 graph-class anchors (A1-A4).

DO NOT RUN at design phase (W5 Day 4); execute at W6 Day 4-7 + W7.
"""

import numpy as np
from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.multi import gradient_flow_trajectory_with_noise  # NEW: thermal version W6
from scc.diagnostics import compute_sigma_tuple_multi
# from scc.sigma_rich import compute_sigma_rich  # NEW W6 Day 1-3
# from scc.k_jump_detector import detect_k_jumps  # from sigma_rich_VR_phase1 §7

# Graph anchors
GRAPHS = {
    'A1_T2_20': lambda: GraphState.torus_2d(20, 20),
    'A2_T2_30': lambda: GraphState.torus_2d(30, 30),
    'A3_R23': lambda: load_R23_graph(),
    'A4_H_16': lambda: GraphState.hexagonal_2d(16),
}

# Parameter scan
BETAS = [2.0, 4.0, 6.0]
LAMBDA_REPS = [0.01, 0.1, 1.0]
TEMPERATURES = [0.0, 1e-4, 1e-3, 1e-2, 1e-1]
MASSES = [40, 80, 160]
K_FIELD = 4
N_TRAJECTORIES_PER_CONFIG = 20  # ensemble size for stochastic measurement

def run_trajectory(graph, params, T, IC, T_max=10000, dt=0.01):
    """Gradient flow with optional thermal noise."""
    return gradient_flow_trajectory_with_noise(graph, params, IC, T_max, dt, noise_T=T)

def measure_M1_trajectory(traj, epsilon=0.01):
    """K_act(t) via formation mass thresholding."""
    return [(np.linalg.norm(u, axis=1, ord=1) > epsilon).sum() for u in traj]

def measure_M2_T_c(graphs, params, masses, n_long_runs=200):
    """Crossover temperature scan: pi(K=1) = pi(K=2)."""
    T_c_table = {}
    for g_id, g_factory in graphs.items():
        for params_id, params in iter_params():
            g = g_factory()
            T_c = bisect_T_c(g, params, masses, n_long_runs)
            T_c_table[(g_id, params_id)] = T_c
    return T_c_table

def measure_M3_K_jump_intervals(traj_list):
    """Extract Δt_n vs t_n; fit exponent alpha."""
    all_intervals = []
    for traj in traj_list:
        K_act = measure_M1_trajectory(traj)
        jump_times = [i for i in range(1, len(K_act)) if K_act[i] != K_act[i-1]]
        intervals = np.diff(jump_times)
        all_intervals.extend(zip(jump_times[:-1], intervals))
    # Power-law fit
    times, dts = zip(*all_intervals)
    alpha = np.polyfit(np.log(times), np.log(dts), 1)[0]
    return alpha, all_intervals

def measure_M4_barrier(traj, jump_times, params):
    """Barrier ΔE at each K-jump via NEB or interpolation."""
    barriers = []
    for t_n in jump_times:
        u_pre = traj[t_n - 1]
        u_post = traj[t_n + 1]
        E_saddle = compute_saddle_energy(u_pre, u_post, params)
        E_min = compute_energy(u_pre, params)
        barriers.append(E_saddle - E_min)
    return barriers

def measure_M5_d_min_at_merger(traj, jump_times):
    """d_min(j,k) at K-jump times."""
    d_mins = []
    for t_n in jump_times:
        u_pre = traj[t_n - 1]
        centroids = compute_centroids(u_pre)
        # Find merging pair (closest centroids per Theorem 3.1)
        d_min = min(np.linalg.norm(c_a - c_b) for c_a, c_b in pairs(centroids))
        d_mins.append(d_min)
    return d_mins

def measure_M6_nq242c(graph_T2_20, params):
    """NQ-242c-Standard + NQ-242c-Rich verification."""
    # Reuse from CODE/scripts/nq242c_construction.py
    return run_nq242c_pipeline(graph_T2_20, params)

def measure_M7_PH_barcode(traj):
    """V-R PH barcode pipeline per sigma_rich_VR_phase1 §7."""
    # Reuse from CODE/scripts/sigma_rich_VR_phase1.py
    return run_VR_phase1_pipeline(traj)

def main():
    results = {}
    for g_id, g_factory in GRAPHS.items():
        for beta in BETAS:
            for lambda_rep in LAMBDA_REPS:
                for T_thermal in TEMPERATURES:
                    for M in MASSES:
                        config_id = f"{g_id}_b{beta}_lr{lambda_rep}_T{T_thermal}_M{M}"
                        graph = g_factory()
                        params = ParameterRegistry(beta=beta, lambda_rep=lambda_rep, alpha=1.0, a_cl=2.0)
                        traj_list = []
                        for ic_seed in range(N_TRAJECTORIES_PER_CONFIG):
                            IC = random_symmetry_broken_IC(graph, M, K_FIELD, seed=ic_seed)
                            traj = run_trajectory(graph, params, T_thermal, IC)
                            traj_list.append(traj)

                        # Measurements
                        m1 = [measure_M1_trajectory(traj) for traj in traj_list]
                        m3_alpha, m3_intervals = measure_M3_K_jump_intervals(traj_list)
                        m4_barriers = [measure_M4_barrier(traj, jumps, params) for traj, jumps in zip(traj_list, m1_jumps)]
                        m5_d_mins = [measure_M5_d_min_at_merger(traj, jumps) for traj, jumps in zip(traj_list, m1_jumps)]
                        m7_barcodes = [measure_M7_PH_barcode(traj) for traj in traj_list[:5]]

                        results[config_id] = {
                            "M1_K_act_trajectories": m1,
                            "M3_alpha_exponent": m3_alpha,
                            "M3_intervals": m3_intervals,
                            "M4_barriers": m4_barriers,
                            "M5_d_mins": m5_d_mins,
                            "M7_PH_barcodes": m7_barcodes,
                        }
    
    # M2 + M6 separate (longer running)
    results['M2_T_c_table'] = measure_M2_T_c(GRAPHS, ALL_PARAMS, MASSES)
    results['M6_NQ242c'] = measure_M6_nq242c(GRAPHS['A1_T2_20'](), default_params())

    save_results(results, "results/k_selection_c_numerical.json")

if __name__ == "__main__":
    main()
```

### §5.2 Estimated runtime

- M1 trajectories: ~10 min/trajectory × 20 trajectories × 5 graphs × 3β × 3λ × 5T × 3M = ~67500 min ≈ 1100 hours single CPU.
- **Mitigation**: parallelize over (graph, params, T, M) combinations; use 16-core machine reduces to ~70 hours.
- **Subsampling**: full scan reduced to representative slice (~20% of full grid) ⇒ ~14 hours achievable.
- M2: 200 long-runs × 5 graphs × ... ≈ 70 hours single CPU.
- M6: NQ-242c per `nq242c_explicit_construction.md` ≈ 30 min.
- M7: PH per snapshot × 200 snapshots × 100 trajectories ≈ 5 hours.

**Total**: ~100 single-CPU hours; ~10 hours on 16-core machine.

### §5.3 Output

`CODE/scripts/results/k_selection_c_numerical.json`:
```json
{
  "M1_K_act_trajectories": "(graph, params, T, M, ic_seed) -> K_act(t)",
  "M2_T_c_table": "{(g, params): T_c}",
  "M3_alpha_exponent": "{(g, params, T, M): alpha}",
  "M4_barriers": "[Delta_E_n]",
  "M5_d_mins": "[d_min at jumps]",
  "M6_NQ242c": "{sigma_std_nondet, sigma_rich_distinct, Phi_rich_det}",
  "M7_PH_barcodes": "[zigzag PH per trajectory]"
}
```

---

## §6. Cat Status and Promotion

### §6.1 Pre-execution Cat status (this file)

- **Cat A established**: design specification, measurement specs, script outline.
- **Cat B target post-execution**: M1-M7 numerical results + agreement with Tasks #5+#6 predictions.

### §6.2 Validation criteria

For Cat B target (post W6 Day 4-7 + W7 execution):
- (V1) M3 $\alpha \approx 1.315$ (V4) or $4/3$ (LSW) on A1 $T^2_{20}$.
- (V2) M3 $\alpha$ universality across A2, A4 (within 5% tolerance).
- (V3) M2 $T_c \propto 1/\log |X|$ scaling between A1, A2.
- (V4) M4 barrier scaling $\Delta E \propto \lambda_{\mathrm{rep}}$ at fixed $d_{\min}$ regime.
- (V5) M5 $d_{\min}$ at K-jumps approaches 0 (small distance ⇒ low barrier triggers crossing).
- (V6) M6 NQ-242c-Standard non-determinism + NQ-242c-Rich determinism (per `nq242c_explicit_construction.md` §6.1 (C1)-(C3)).
- (V7) M7 $K_{\mathrm{act}}(t) = \dim H_0(R(C(t)))$ Claim 4.1 of `sigma_rich_VR_phase1.md`.

(V1)+(V2) ⇒ K-Selection (b) Kramers + LSW universality numerically confirmed.
(V3)+(V4) ⇒ K-Selection (a) free-energy crossover formula numerically confirmed.
(V6) ⇒ OP-0008 Path B confirmed.
(V7) ⇒ Tool A3 PH integration confirmed.

### §6.3 Cat A path

Cat A everywhere requires:
- (V1)+(V2) cross-graph universality theoretical proof — LSW correspondence (Task #6 §7.4).
- (V3) thermodynamic-limit theoretical $T_c$ formula — Task #5 §7.2 closed-form $S(K)$.
- (V4)+(V5) explicit barrier-scaling theoretical proof — Task #6 §3.3 → Cat A.

W7-W12 theoretical work, combined with this file's numerical anchor.

### §6.4 Promotion target

CV-1.7+ candidate Commitment 19 (K-Selection axiom) per task #49 in TaskList; this file's numerical anchor + Tasks #5+#6 theoretical foundation = full canonical promotion package.

---

## §7. Hard Constraint Verification

- [x] **canonical 직접 수정 0** — `working/MF/` only.
- [x] **Silent resolution 0** — measurement specs explicit; Cat status pre-execution; W6+ execution timeline.
- [x] **No Research OS resurrection** — single-topic.
- [x] **Not reductive** — measurements are *empirical complement* to Tasks #5+#6 theoretical predictions; no external reduction. CN10 contrastive (LSW theory cited as standard reference, not SCC reduction).
- [x] **u_t primitive maintained** — all measurements operate on $u^{(j)}(t)$ trajectories.
- [x] **CN5 4-energy not merged** — N/A.
- [x] **K not dual-treated** — $K_{\mathrm{act}}$ integer per Commitment 16.
- [x] **P-F flag** — M1, M3, M4, M6 all involve thermal noise (T > 0); P-F flagged.
- [x] **CN15 Static/Dynamic Separation** — equilibrium $K^*_{\mathrm{eq}}$ (M2) vs trajectory $K_{\mathrm{act}}(t)$ (M1) explicitly separated.
- [x] **OP-0005 not silently resolved** — option (c) is *one* of 4 options; full K-Selection mechanism via Task #8 compatibility proof.
- [x] **OP-0009-Emp R23 verification** — A3 R23 anchor addresses OP-0009-Emp (high-F empirical anchor).

---

## §8. References

### §8.1 Working files

- `working/MF/k_selection_a_free_energy.md` (Task #5; equilibrium predictions tested by M2).
- `working/MF/k_selection_b_kramers.md` (Task #6; Kramers + LSW predictions tested by M3, M4, M5).
- `working/MF/sigma_rich_VR_phase1.md` (Phase 1 PH pipeline used by M7).
- `working/MF/nq242c_explicit_construction.md` (NQ-242c numerical pipeline used by M6).

### §8.2 Canonical refs

- `canonical/canonical.md` §11.1 Commitment 14, 14-Multi, 16; §13 T-Persist-K family; §14 CN15.
- `canonical/theorem_status.md` OP-0005 (direct attack); OP-0008, OP-0009.

### §8.3 External refs

- Phase 10 V4 source: `THEORY/logs/daily/2026-04-28/34_Phase10_findings.md` §3-§4.
- Lifshitz-Slyozov (1961), Wagner (1961) — LSW coarsening (V1, V2 prediction source via Task #6).
- Nudged-elastic-band (NEB) for saddle-point identification: Henkelman, Uberuaga, Jónsson (2000). *J. Chem. Phys.* 113: 9901-9904.

### §8.4 CODE infrastructure

- `CODE/scripts/k_selection_c_numerical.py` (NEW W6 Day 4-7).
- Dependencies: `scc/multi.py` (existing); `scc/sigma_rich.py` (NEW W6 Day 1-3); `scc/k_jump_detector.py` (NEW W6 Day 4-5); `gudhi`/`ripser` (PH).

---

**End of k_selection_c_numerical_anchor.md.**

**Status: working draft. Task #7 complete (design phase). K-Selection (c) symmetry-broken numerical anchor: 7 measurements (M1 K_act trajectory, M2 crossover T_c, M3 K-jump intervals + LSW exponent, M4 barrier heights, M5 pair-distance at merger, M6 NQ-242c verification, M7 V-R PH barcode); 4 graph-class anchors (A1 T²_20, A2 T²_30, A3 R23, A4 hexagonal); script outline at CODE/scripts/k_selection_c_numerical.py (NOT run); ~100 single-CPU hours runtime with parallelization mitigation; 7 validation criteria (V1-V7) for Cat B target post-execution. Forward: Task #8 compatibility proof composing options (a)+(b)+(c)+(d). CV-1.7+ Commitment 19 K-Selection axiom target.**

**File:** `/Users/ojaehong/Perception/Perception_theory/THEORY/working/MF/k_selection_c_numerical_anchor.md`
**Created:** 2026-04-30 (W5 Day 4).
**Promotion target:** CV-1.7+ W12+ packet (combined with Tasks #5, #6, #8 + numerical execution W6-W7).
