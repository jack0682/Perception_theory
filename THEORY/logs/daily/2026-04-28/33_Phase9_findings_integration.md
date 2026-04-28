# 33_Phase9_findings_integration.md — Phase 9 U1+U2+U3+U4 Integrated Findings

**Session:** 2026-04-28 (W5 Day 2 Phase 9, U1-U5 integrated).
**Status:** **5 substantive findings** including REFUTATION of Phase 8 "γ ≈ 0.1 optimal" claim.

---

## §1. U1 — K→∞ Extrapolation Result

L=40, β=4, λ_rep=0.5, c_total=0.20, t=150, 3 seeds:

| K | α | K_init→K_final | R_init→R_final |
|---|---|---|---|
| 5 | 0.105 | 5→3 | 4.46→5.26 |
| 10 | 0.202 | 10→4 | 3.20→4.53 |
| 15 | 0.241 | 15→5 | 2.59→4.39 |
| 20 | 0.243 | 20→6 | 2.26→4.36 |
| 30 | 0.227 | 30→10 | 1.83→3.70 |
| 40 | (in progress) | | |

α(K) is **non-monotonic**: increases from K=5 to K=15 (α: 0.10 → 0.24), then plateaus around K=15-30 (α ≈ 0.24).

**K-asymptotic α ≈ 0.24** (different from Phase 8 T1's 0.28, suggests sensitivity to L, t_max, parameters).

### §1.1 K→∞ extrapolation

Linear fit α(K) = α_∞ + B/K (using K=5,10,15,20,30):
- α_∞ ≈ 0.27 (intercept).
- B ≈ -0.86 (slope).

**Predicted K→∞ asymptotic α ≈ 0.27** for SCC shared-pool LSW on T²_{40} with current parameters.

### §1.2 Comparison

- Classical 2D LSW: α = 0.5.
- SCC measured: α ≈ 0.27.
- Discrepancy ≈ factor 2.

The factor-2 discrepancy may be due to:
- Discrete lattice corrections.
- Non-local mass redistribution (vs CH local diffusion).
- Specific parameter choice; may differ at other (β, c).

---

## §2. U2 — Long-Time α Trajectory

K=10, t=1000 (single run):

| Time window | α |
|---|---|
| 10-100 | 0.218 |
| 50-200 | 0.191 |
| 100-300 | 0.343 |
| 200-500 | -0.062 |
| 300-700 | 0.503 |
| 500-1000 | **0.652** |

**α GROWS over time** from ~0.2 (early) to ~0.65 (late). NOT stabilized.

### §2.1 Interpretation

Late-time α=0.65 corresponds to K_active=1 final state. Once K=1, "R" is a single growing cluster's effective radius — not LSW dynamics.

Phase 8 T1's "α ≈ 0.28 stable for K≥10" was measured in **early-time window** (t ~ 5-200). U2 shows that over much longer times, formations merge to K=1 and "α" becomes meaningless (single cluster shape evolution).

### §2.2 Refined LSW window definition

LSW α should be measured ONLY in the **active-coarsening window** before all-merger. Practical definition:
- Start: $t_1$ where $K_{\mathrm{active}}(t_1) < K_{\mathrm{init}} - 1$ (first merger occurred).
- End: $t_2$ where $K_{\mathrm{active}}(t_2) = 2$ (just before final all-merger).

For U2 K=10 single run: t_1 ≈ 50, t_2 ≈ 500. α in this window: ≈ 0.34 (closer to phase 8 plateau).

### §2.3 Phase 9 finding: Phase 8 α=0.28 was PLATEAU PHASE only

Long-time α is HIGHER (~0.65) but reflects single-cluster growth, not multi-formation coarsening. **The "true LSW α"** for shared-pool SCC is in the plateau phase ~0.25-0.34.

---

## §3. U3 — γ Refined Fit (REFUTES Phase 8 T3 "γ ≈ 0.1 optimal")

β=4.0, c=0.10:

| γ | α |
|---|---|
| 0.0 | **0.689** |
| 0.03 | 0.647 |
| 0.05 | 0.610 |
| 0.07 | 0.582 |
| 0.1 | 0.521 |
| 0.15 | 0.420 |
| 0.2 | 0.425 |
| 0.3 | 0.406 |
| 0.5 | 0.317 |
| 1.0 | 0.202 |

**α(γ) is MONOTONICALLY DECREASING.** γ=0 gives HIGHEST α=0.689. NOT γ=0.1 as Phase 8 T3 claimed.

### §3.1 Refutation of Phase 8 T3

Phase 8 T3 measured γ=0.1: α=0.6, γ=1.0: α=0.12. The pattern matches U3 (decreasing). The Phase 8 T3 INTERPRETATION ("optimal γ ≈ 0.1") was MISLEADING: actual α is highest at γ=0.

### §3.2 Per-formation pool with target-relaxation

**Important caveat**: U3's "γ=0" implementation is the same as T3's: hybrid_project with γ·dt mass-relaxation toward m_per_init. At γ=0, this DOESN'T enforce strict per-formation; it allows transient relaxation toward initial mass distribution.

The "α=0.689 at γ=0" is from this **transient relaxation** dynamics, NOT from genuine LSW.

### §3.3 The TRUE per-formation regime

True per-formation pool (Phase 5+6 numerical: K=3-10 stable for t=200, NO coarsening):
- α ≈ 0 (statically stable).
- This is when m_j is rigidly fixed.

In U3's hybrid implementation at γ=0: m_target = m_per_init constantly, and gradient flow + project to m_per_init = transient adjustment toward initial. NOT strict.

So **U3's γ=0 is a third architecture**, distinct from both pure per-formation (α=0) and pure shared-pool (α=0.28).

### §3.4 Phase 8 T3 + U3 combined: γ-interpolation has THREE regimes

| γ regime | Architecture | α |
|---|---|---|
| Strict per-formation (rigid m_j) | Phase 5+6 numerical | ≈ 0 |
| Hybrid γ=0 (target-relaxation, not strict) | U3 + T3 measurement | ≈ 0.69 (transient) |
| Hybrid γ ∈ [0, 1] interpolation | T3, U3 | monotonically decreases |
| Shared pool (true uniform redistribution) | Phase 7 R1.3 + T1 | ≈ 0.28 |

**Phase 9 conclusion**: γ-interpolation is **between two non-pure intermediate states**, not between strict per-formation and pure shared. The "optimal" finding from Phase 8 T3 was an artifact of confusing implementations.

### §3.5 NQ-229b refined answer

α(γ) is **monotonically decreasing** from γ=0 (transient-relaxation regime, α≈0.69) to γ→∞ (shared-pool regime, α≈0.20). Optimal coarsening rate is **at γ=0** in this implementation (transient regime).

For TRUE optimal γ across architecture spectrum: need to also include strict per-formation (γ → -∞ in some sense, where γ=0 is genuinely "no relaxation"). The PROPER γ-interpolation requires re-implementation.

---

## §4. U4 — σ_multi^A(t) Numerical Trajectory

K=8, t=200, β=4, λ_rep=0.5 with simplified σ-tuple (m, peak_u, peak_idx) per formation:

- t=0: K_active=8, all formations at m=22-23, peak_u≈0.97.
- t=100-200: most formations dead (peak_u=0, m=0); 1-2 survivors with large m.

K_jumps: detected throughout t=20-150. Frequency increases as K decreases.

### §4.1 σ_jump events

Each K-merger event corresponds to a discrete drop in K_active. U4 detected ~6 merger events over t=200 (8→2 transitions).

### §4.2 σ-trajectory structure

Between mergers: smooth m_j(t), peak_u(t) evolution (continuous).
At merger: discrete jump (formation dies, peak_u → 0, m → 0).

Confirms `30_*` §2 σ_multi^A(t) framework: smooth segments separated by discrete jumps.

### §4.3 Limitation

Simplified σ-tuple (m, peak_u, peak_idx) doesn't capture:
- Hessian eigenvalue structure.
- Irrep labels.
- Nodal counts.

Full Hessian-based σ logging deferred to W6+ (NQ-228-Cat-A).

---

## §5. U5 — SCC ↔ CH Theorem

Per `32_*`: γ as mobility analog M_eff = γ/V. Cat B target theorem with proof outline.

Discrepancy between SCC (non-local) and CH (local) in mass-redistribution; convergence asymptotic in K.

NQ-236-239 spawned for full Cat A path.

---

## §6. Combined Phase 9 Implications

### §6.1 LSW α refined understanding

| Setup | α | Note |
|---|---|---|
| Strict per-formation pool | ≈ 0 | Phase 5+6 |
| Hybrid γ=0 (target-relax) | ≈ 0.69 | Phase 8 T3 + U3, **transient** |
| Hybrid γ=0.1 (Phase 8 T3) | ≈ 0.6 | Phase 8 |
| Hybrid γ=1.0 | ≈ 0.20 | Phase 8 + U3 |
| Shared-pool plateau (10<K<30) | ≈ 0.27 | Phase 8 T1 + U1 |
| Shared-pool late-time (K=1) | ≈ 0.65 | U2 (single cluster) |

**The LSW α** has structure not yet fully captured by single number; depends on architecture, time-window, and K.

### §6.2 Phase 8 T3 "optimal γ" interpretation REVISED

Phase 8 T3 reading "γ ≈ 0.1 optimal" was WRONG. Correct reading: α decreases monotonically with γ. The peak at γ=0 reflects transient-relaxation dynamics, not true LSW.

### §6.3 K→∞ thermodynamic α

α_∞ ≈ 0.27 (U1 fit). Below classical 2D LSW (0.5). Reasons:
- Discrete lattice (vs continuum).
- Non-local mass redistribution (vs local diffusion).
- Plateau-window measurement (vs asymptotic).

### §6.4 Long-time complications

U2 reveals α(t) is NOT stable; depends on time window. The "0.28" plateau is a transient phase between LSW-active multi-formation and final single-cluster regime. Asymptotic K=1 state has α=0.65 but represents single-cluster growth, not LSW.

### §6.5 σ_multi^A(t) numerically tracked

Discrete K-jumps detected. σ-trajectory structure: smooth between, jumps at mergers. Confirms `30_*` framework qualitatively.

---

## §7. Cat status updates (Phase 9)

| Item | Phase 8 | Phase 9 |
|---|---|---|
| K-asymptotic α | sketch | **Cat B: α_∞ ≈ 0.27 from K=5-30 fit** |
| Long-time α | unknown | **Cat A: α(t) varies; plateau ≈0.28; late-time 0.65** |
| Hybrid γ=optimal | "γ≈0.1 optimal" | **REVISED: monotonically decreasing α(γ)** |
| σ_multi^A(t) | sketch | **Cat B sketch numerical implementation done (simplified)** |
| SCC ↔ CH | sketch | **Cat B with proof outline (`32_*`)** |

---

## §8. Phase 9 NQ Spawns (4 new)

- NQ-240: True per-formation strict pool simulation with shared-target relaxation (resolve U3 implementation ambiguity).
- NQ-241: α-window definition standardization (active-coarsening window only).
- NQ-242: Full Hessian-based σ-tuple at each timestep (computational scaling W6+).
- NQ-243: Spectral analysis of K-jump events (frequency, magnitude statistics).

**Total Day 2 NQ spawns: 54** (Phase 1: 1 + Phase 2: 7 + Phase 3: 14 + Phase 4: 5 + Phase 5: 7 + Phase 6: 7 + Phase 7: 4 + Phase 8: 5 + Phase 9: 4).

---

## §9. Cross-References

- `13_*` LSW connection (Phase 6+7).
- `28_*` Phase 7 R1.3.
- `30_*` Phase 8 T4 CH correspondence.
- `31_*` Phase 8 T1+T2+T3 findings.
- `32_*` Phase 9 U5 CH theorem.

---

**End of 33_Phase9_findings_integration.md.**
**Status: 5 Phase 9 findings; Phase 8 T3 γ-interpretation REVISED; K→∞ extrapolation gives α_∞≈0.27; long-time α grows to 0.65 at K=1; σ_multi^A(t) trajectory framework numerically implemented (simplified). 4 new NQ.**
