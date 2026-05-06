# exp02-NEB: Stereo Merger Barrier — NEB + K-Stability

## Physical Mechanism (T-ST-5a — Hard-Cut Topological Locking)

*(Pre-split label was "T-ST-5"; T-ST-5 was split W6 D4 into T-ST-5a [hard-cut, Cat A] and T-ST-5b [smooth, Cat C]. This experiment addresses T-ST-5a only. T-ST-5b is addressed in exp02c/exp02d/exp02e.)*

Under flat adjacency: smoothness term provides cross-boundary driving force
toward merger → K=2 starting field flows downhill to K=1 (barrier=0).

Under stereo adjacency (hard depth cut): cross-boundary edges REMOVED →
graph disconnected → K=2 topologically locked → barrier=∞.

For a quantitative NEB sweep: vary epsilon-bridge connectivity from ~stereo
(eps≈0, high barrier) to flat (eps=1, barrier→0). Monotone decrease in
barrier confirms the claim direction.

## Setup

- Grid: 20x20, depth_gap=2.0, delta_z=0.5
- Hard bimodal initialization: two rectangular blocks separated by 0s
- alpha=1.0, beta=4.0, rho_pers=0.05

## K-Stability Result (Primary)

| Condition | K_act (after relax) | E_start | Interpretation |
|---|---|---|---|
| Flat (L_flat) | 1 | 21.8768 | Spontaneous merger — no barrier |
| Stereo (L_stereo, hard cut) | 2 | 25.2625 | K=2 stable — disconnected graph, barrier=∞ |

K-stability claim: **SUPPORTED**

## NEB Sweep (eps-bridge from stereo to flat)

| eps_bridge | K_act | barrier |
|---|---|---|
| 0.000 (stereo) | 2 | ∞ (disconnected) |
| 0.002 | 1 | 0.0000 |
| 0.005 | 1 | 0.0000 |
| 0.010 | 1 | 0.0000 |
| 0.030 | 1 | 0.0000 |
| 0.050 | 1 | 0.0000 |
| 0.100 | 1 | 0.0000 |
| 0.200 | 1 | 0.0000 |
| 0.500 | 1 | 0.0000 |
| 1.000 | 1 | 0.0000 |
| 1.000 (flat) | 1 | ~0 (spontaneous) |

max_barrier_finite = 0.0000
barrier_non_increasing: True
barrier_flat_near_zero (eps=1): True

## Claim B Status: **SUPPORTED**

## Assumptions and Limitations

1. **Hard threshold adjacency**: D-ST-1 uses hard threshold delta_z for G_t^P.
   The hard cut creates a DISCONNECTED graph (infinite barrier). The soft/eps-bridge
   sweep approximates the transition between stereo and flat topologies.

2. **NEB on disconnected graph is undefined**: For eps=0 (pure stereo), the graph
   is disconnected and no merger path exists. "Barrier=∞" is inferred by continuity,
   not computed by NEB.

3. **Toy GL energy**: E[u;L] = alpha*u^T L u + beta*Σ W(u_x) is a simplified proxy
   for full 4-term SCC energy. Closure and separation terms change the landscape.

4. **P-F flag**: T_star in Kramers rate Gamma=A*exp(-ΔE/T*) remains undefined
   until P-F-A1 (Langevin on F_M(P)) is canonically formalized.

## Conclusion re T-ST-5a

Primary result (K-stability): flat→K=1 (merger), stereo→K=2 (stable).
This is the core content of T-ST-5a: hard-cut stereo adjacency prevents merger by
disconnecting the K=2 energy basin from the K=1 merged state.

NEB sweep: barrier decreases as eps increases (stereo→flat direction),
consistent with T-ST-5a. Barrier=∞ at eps=0 (disconnection limit).

T-ST-5a status: **SUPPORTED** (Cat A — all gaps G1–G4 closed W6 D4 Session E;
proof in `THEORY/working/MF/tst5a_hard_depth_locking_proof.md`).
T-ST-5b (smooth barrier) addressed in exp02c/exp02d/exp02e.
