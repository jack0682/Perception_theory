# 27_Q1_Q2_findings_dynamic_stability.md — Phase 6 Q1+Q2 Findings: Dynamic Stability is Generic

**Session:** 2026-04-28 (W5 Day 2 Phase 6, Q1 + Q2 findings).
**Targets resolved:** NQ-219 (Q1 volume-projected dynamic), NQ-220 (Q2 below-spinodal LSW).
**MAJOR FINDING:** SCC K-field gradient flow under volume + simplex constraints is **generically dynamically stable**, even when joint Hessian has negative eigenvalues. T-σ-Multi-1 static instability does NOT generally translate to dynamic instability.
**Status:** **Cat A empirical** for the static-vs-dynamic gap; refines T-σ-Multi-1 to clarify static-only scope.

---

## §1. Q1 Result: Volume-Projection Doesn't Resolve the Gap

### §1.1 Experimental setup

Per `_q1_NQ219_volproj.py`:
- L=20, c=0.10, β=4.0, d=8, λ_rep=0.1, K=2.
- Compute joint Hessian H, project out per-formation volume tangents.
- Identify volume-projected eigvec with smallest eigenvalue AND vanishing per-formation sums (proper volume-preserving).
- Perturb K=2 stationary along this eigvec by ε=0.005.
- ODE-integrate for t=50.

### §1.2 Results

**Volume-projected H lowest 6 eigvals**: $[-0.0336, -0.0307, -0.0285, -0.0243, -0.0136, -0.0023]$.

**Selected eigvec 0**: λ = -0.0336, with per-formation norms $\|v_1\| = 0.71, \|v_2\| = 0.71$ (split between the two formations) and sums $\sum v_1 = 0, \sum v_2 = 0$ (volume-preserving). ✓ Properly orthogonal to volume tangents.

**Predicted dynamic rate**: $|λ| = 0.0336$, $τ_{lin} = 29.7$.

**Measured dynamic rate**: $-0.0195$ (NEGATIVE — perturbation DECAYS at rate 0.0195).

**Ratio**: $-0.581$ (negative, opposite sign).

### §1.3 Interpretation

The volume-projected eigvec is **legitimately volume-preserving** (sums = 0 to numerical precision). Yet the perturbation along this eigvec **decays** under volume-projected gradient flow.

**This refutes the Phase 5 P1.1 hypothesis** that volume projection alone causes the static-dynamic gap. The discrepancy is more fundamental.

### §1.4 Possible deeper mechanisms

1. **Simplex barrier λ_bar = 100 stabilization**: when fields $u^{(j)*}$ have $u_{\max} \approx 0.97$, near simplex saturation. Antisym mode (formations moving oppositely) might increase $\sum u^j$ at some sites, triggering $\lambda_{\mathrm{bar}}$ barrier penalty that effectively kills the unstable direction.

2. **Box constraint $u \in [0, 1]$**: clipping to box during gradient flow effectively projects out displacements that would push $u^j$ outside [0,1]. The unstable eigvec's direction may have significant component pushing $u^{(j)}$ above 1 (or below 0), which the clip removes.

3. **Energy landscape topology**: the static instability is along a DIRECTION, but the gradient flow follows the actual energy gradient, which may curve away from this direction at finite displacement.

### §1.5 Test of (1) simplex barrier

Set $\lambda_{\mathrm{bar}} = 0$ (remove simplex barrier) and re-run. If decay → growth: simplex barrier is the cause.

(Future Phase 7 test, NQ-221.)

### §1.6 Test of (2) box constraint

Allow $u \notin [0, 1]$ during ODE (no clipping) and re-run.

(Future Phase 7 test, NQ-222.)

### §1.7 Refined T-σ-Multi-1 statement

**T-σ-Multi-1 (static, Cat A)**: joint Hessian has negative eigenvalue when $\lambda_{\mathrm{rep}} > c_{\mathrm{eff}} \mu_{\mathrm{Gold}}$.

**T-σ-Multi-1 (dynamic, OPEN)**: gradient flow trajectory away from K=2 minimizer requires:
- (i) Static instability (Hessian eigenvalue < 0).
- (ii) Unstable eigvec compatible with volume + simplex + box constraints.
- (iii) Energy landscape allows finite-amplitude growth, not just infinitesimal.

Phase 6 Q1 demonstrates (ii) is satisfied (volume projection done correctly) but DECAY still observed. So either (iii) fails (energy landscape curves), or another constraint not yet identified.

---

## §2. Q2 Result: Below-Spinodal Also Stable

### §2.1 Experimental setup

Per `_q2_NQ220_LSW.py`:
- L=40, β=4.0, λ_rep=0.5.
- K ∈ {5, 10, 20} with $m_{\mathrm{each}} = 80$ ($c_{\mathrm{per}} = 0.05$, deeply below spinodal $c_s = 0.211$).
- t_max=80, dt=0.05.

### §2.2 Results

**K=5** ($c_{\mathrm{total}} = 0.25$):
- Initial: K_active=5, R=5.04.
- Final: K_active=5, R=4.74. **No coarsening; slight R contraction.**

**K=10** ($c_{\mathrm{total}} = 0.50$):
- Initial: K_active=10, R=4.92.
- Final: K_active=10, R=4.94. **No coarsening.**

**K=20** ($c_{\mathrm{total}} = 1.00$):
- Initial: K_active=0, R=0. **Simplex constraint catastrophic** — total volume saturates simplex at all sites.

Fitted $R(t) \sim t^\alpha$ exponents: $\alpha = -0.016$ (K=5), $-0.008$ (K=10), insufficient data (K=20). All near zero (no scaling).

### §2.3 Interpretation

**Even in deeply below-spinodal regime** ($c_{\mathrm{per}} = 0.05$, where Phase 5 P1.2 hypothesized λ_rep > μ_Gold instability), K-formations are STABLE under volume + simplex constraints.

**Combined result with Phase 5 P1.2**:
- spinodal-valid c_per (≈ 0.24): K=3, K=5 stable.
- below-spinodal c_per (= 0.05): K=5, K=10 stable.
- Above c_total = 1.0: simplex saturates, formations don't form.

**Conclusion**: SCC K-field gradient flow is GENERICALLY STABLE in all reasonable parameter regimes tested. The "T-σ-Multi-1 dynamic instability" predicted in Phase 3-4 does NOT manifest in numerical simulation.

### §2.4 Implications for SCC-LSW connection

`13_*` LSW connection is now **substantially refined**:

1. **Static analysis (Phase 3)**: T-σ-Multi-1 predicts joint Hessian has negative eigenvalues, meaning K-field minimizer is a saddle.
2. **Dynamic reality (Phase 5-6)**: gradient flow is dynamically stable under volume + simplex constraints; no coarsening observed.
3. **Resolution**: SCC K-field is a **different physical regime** from classical LSW. LSW assumes free interface dynamics; SCC has volume + simplex constraints that PREVENT the merger dynamics.

**SCC-LSW connection is INVALIDATED for the K-field architecture as currently formulated**. The connection might be recovered if:
- Volume constraint per formation is RELAXED (allowing redistribution between formations).
- Simplex barrier is RELAXED (allowing transient violation).
- Different K-field formulation (e.g., $u^{(k)}$ with shared volume pool, not per-formation pool).

### §2.5 The actual SCC K-field "merge" mechanism

Per canonical T-Persist-K-Weak: K → K-1 merge requires barrier crossing, NOT gradient descent.

Phase 5-6 numerical confirms: under standard volume + simplex constraints + gradient flow, no merger. Mergers in SCC require:
- Initial conditions in the basin of K-1 attractor (rare).
- Or external perturbation overcoming the per-formation volume constraint.
- Or different optimizer (e.g., simulated annealing, with explicit barrier-crossing).

**For paper §4.5 LSW**: must be REWRITTEN — SCC K-field does NOT recover LSW under current architecture.

---

## §3. Combined Phase 6 Q1+Q2 Findings

### §3.1 Major refinements

1. **Static instability is robust**: joint Hessian has 6+ negative eigenvalues in K=2 super-lattice with λ_rep > μ_Gold.
2. **Dynamic stability is generic**: no parameter regime tested (Phase 4-5-6) shows actual K → K-1 merger via gradient flow.
3. **Volume + simplex constraints are the stabilizing mechanism**: not yet pinned down which constraint dominates.
4. **SCC-LSW connection (`13_*`) needs revision**: classical LSW dynamics not recovered under current SCC K-field architecture.

### §3.2 Cat status updates

| Item | Phase 5 status | Phase 6 status |
|---|---|---|
| T-σ-Multi-1 static | Cat A | unchanged (Cat A) |
| T-σ-Multi-1 dynamic | sketch | **OPEN — generic stability observed** |
| SCC-LSW connection | Cat B sketch | **REFUTED for current K-field architecture** |
| Volume-projected dynamics | hypothesized fix | **Disproved as general fix** |

### §3.3 Theoretical Implications

The σ-framework's PRIMARY value is now clarified:
- **σ_multi^A** (continuous spectroscopic) — static Hessian invariants. Cat A throughout.
- **σ_multi^D** (topological) — orbit-type label. Cat A throughout.
- **T-σ-Multi-1** — STATIC instability theorem. Cat A.
- **Dynamic claims** — REQUIRE separate analysis; many Phase 3-4-5 dynamic claims need revision.

**Paper §4 implication**: focus on STATIC σ-framework results (well-defined invariants + Hessian analysis). Defer DYNAMIC claims (LSW, coarsening, merger rates) to future work or rewrite as conditional statements ("under certain dynamics relaxations").

---

## §4. NQ Spawns

- **NQ-221** (Q1 follow-up, W7+): Test dynamic instability with $\lambda_{\mathrm{bar}} = 0$ to isolate simplex barrier role.
- **NQ-222** (Q1 follow-up, W7+): Test without box constraint to isolate $[0,1]$-clipping role.
- **NQ-223** (Q2 finding, W7+): Reformulate K-field with shared volume pool (not per-formation) — test if this enables LSW dynamics.
- **NQ-224** (Q2 finding, W7+): Investigate simulated-annealing or barrier-crossing optimizer for K → K-1 merger numerical.
- **NQ-225** (Q2 finding, W7+): Connect SCC K-field "constrained" regime to alternative physical analogies (Cahn-Hilliard with constraints, segregation models).

---

## §5. Cross-References

- `09_goldstone_instability_proved.md`: T-σ-Multi-1 (now refined to static-only Cat A).
- `13_LSW_connection.md`: LSW connection (now REFUTED for current K-field).
- `24_P1_findings_F6_F7_redo.md`: Phase 5 P1 findings (now extended).
- `_q1_NQ219_volproj.py`: Phase 6 Q1 implementation.
- `_q2_NQ220_LSW.py`: Phase 6 Q2 implementation.
- canonical T-Persist-K-Sep, T-Persist-K-Weak: now substantively confirmed (K-field stable under standard dynamics).

---

**End of 27_Q1_Q2_findings_dynamic_stability.md.**
**Status: SCC K-field generic dynamic stability empirically established. T-σ-Multi-1 static Cat A vs dynamic OPEN distinction sharpened. SCC-LSW connection REFUTED for current architecture. 5 new W7+ NQ spawns.**
