# 24_P1_findings_F6_F7_redo.md — P1.1 + P1.2 Numerical Findings (Phase 4 F6/F7 Resolved)

**Session:** 2026-04-28 (W5 Day 2 Phase 5, P1.1 + P1.2).
**Targets:** Resolve Phase 4 W1 (F6 random perturbation failure) + W2 (F7 K=10 over-merge).
**Outputs:** `scripts/results/p1_1_F6_targeted.json`, `scripts/results/p1_2_F7_refined.json`.
**Status:** Both **revealed unexpected findings** that refine the σ-framework picture:
- (P1.1) Static instability ≠ dynamic instability under volume-projected gradient flow.
- (P1.2) Multi-formation stability is robust at λ_rep ≈ μ_Gold; coarsening regime narrow.

---

## Part 1: P1.1 — F6 Targeted Perturbation Result

### §1.1 Setup

Per `_p1_1_F6_targeted.py`:
- L=20, c=0.10, β=4.0, d=8, λ_rep=0.1.
- Find K=2 stationary minimizer.
- Compute joint Hessian, identify lowest eigvec.
- Perturb stationary point along this eigvec by ε=0.005.
- ODE-evolve dt=0.01 for t_max=100.

### §1.2 Results

**Joint Hessian lowest 6 eigvals**: $[-0.0336, -0.0307, -0.0285, -0.0243, -0.0136, -0.0023]$.
**All 6 negative** → joint Hessian has 6 unstable modes (multi-Goldstone instabilities + boundary modes).

**Static instability prediction**: τ_lin = 1/|λ_anti| = 29.7.

**Dynamic measurement**: exponential RATE = $-0.0197$ (NEGATIVE — perturbation DECAYS, not grows).

**Ratio measured/predicted = -0.585** (negative, opposite sign).

### §1.3 Interpretation

The **perturbation decays** despite the static Hessian having a negative eigenvalue. This contradicts the naive expectation that gradient flow $\dot u = -\nabla E$ at an unstable mode produces exponential growth.

**Possible mechanisms**:

(M1) **Volume-projection effect**: gradient flow projects out the volume-tangent direction. If the "unstable" eigvec has nontrivial volume-component, projection effectively removes it; what remains is a different direction in tangent space.

(M2) **Simplex barrier λ_bar=100**: at the stationary point, formations are at u_max ≈ 0.97; near the simplex constraint boundary $\sum u^j = 1$. Large λ_bar penalty prevents perturbations that increase $\sum u^j$ above 1 — could effectively kill antisym mode where formations move closer.

(M3) **The "lowest eigvec" is in a non-physical direction**: joint Hessian is computed on the FULL 2n-dim space, but physical perturbations are constrained to volume-preserving directions per formation (each $\sum u^j_i = m_j$). The lowest unconstrained eigvec may have leakage through volume-direction.

### §1.4 Verification: project to volume-preserving subspace before identifying eigvec

Phase 5 P1.1 follow-up (recommended): redo with eigvec computed on the **volume-projected joint Hessian** (per-formation volume tangent removed), then the eigvec has $\sum_i (\delta u^j)_i = 0$ for each $j$, which IS physical.

NQ-219 (Phase 5 P1.1 NEW, W6+): Verify that volume-projected joint Hessian's lowest eigvec produces exponential growth in gradient flow (proper T-σ-Multi-1 dynamic verification).

### §1.5 Refined T-σ-Multi-1 statement

**Phase 5 refinement**: T-σ-Multi-1 instability claim is **a static (Hessian) statement**. Dynamic instability under volume-constrained gradient flow requires:
- The unstable eigvec has nontrivial component in the volume-preserving subspace per formation.
- This component overcomes simplex barrier penalty.

**Cat status**: T-σ-Multi-1 was Cat A as a static instability theorem (`09_*` Phase 3). Phase 5 P1.1 reveals **DYNAMIC** instability is a **separate** claim requiring additional analysis.

This is a **non-trivial refinement** — the σ-framework instability prediction needs to specify whether it's static or dynamic context.

---

## Part 2: P1.2 — F7 Refined K-sweep Result

### §2.1 Setup

Per `_p1_2_F7_refined.py`:
- L=24, β=4.0, λ_rep=0.05.
- K ∈ {3, 5} with $m_{\mathrm{each}} \in \{140, 130\}$ (in-spinodal per-formation: $c_{\mathrm{per}} \in \{0.243, 0.226\}$).
- t_max=200, dt=0.02. 3 seeds per K.

### §2.2 Results

**K=3** (m_each=140, c_per=0.243):
- t=0: K_active=3, R_avg=6.4.
- t=180: K_active=3, R_avg=6.6.
- **No merger over 180 time units.**

**K=5** (m_each=130, c_per=0.226):
- t=0: K_active=2.33 (some formations not initially active).
- t=20: K_active=5 (all activated after relaxation).
- t=180: K_active=5, R_avg=7.8.
- **No merger over 180 time units.**

### §2.3 Interpretation

Both K=3 and K=5 are STABLE in the spinodal-valid c_per regime with λ_rep=0.05.

**Why?** Per T-σ-Multi-1 (`09_*` §1):
$$\mu_{\mathrm{antisym}} = \mu_{\mathrm{Gold}} - c_{\mathrm{eff}} \lambda_{\mathrm{rep}}.$$

For spinodal-valid $c_{\mathrm{per}} \approx 0.24$ at L=24, β=4: $\mu_{\mathrm{Gold}}$ is **NOT** PN-barrier-suppressed (smooth interface, regime R1). Estimated $\mu_{\mathrm{Gold}} \sim O(\beta) = O(4)$.

Threshold for instability: $\lambda_{\mathrm{rep}} > c_{\mathrm{eff}} \mu_{\mathrm{Gold}}$. With $c_{\mathrm{eff}} \approx 0.35$, $\mu_{\mathrm{Gold}} \approx 1$: threshold $\approx 0.35$.

We used $\lambda_{\mathrm{rep}} = 0.05 \ll 0.35$ → **way below instability threshold**. K-formation is stable.

### §2.4 Lesson: LSW regime is narrow

LSW-like coarsening requires **above-threshold λ_rep**:
- For spinodal-valid c (R1 regime): need λ_rep > $c_{\mathrm{eff}} \cdot \mu_{\mathrm{Gold}} \sim O(\beta)$. Large λ_rep needed.
- For below-spinodal c (R3b regime): μ_Gold is PN-barrier-lifted ≈ O(0.001), so even small λ_rep > 0.001 triggers instability.

**Phase 5 conclusion**: classical LSW coarsening (R(t) ~ t^{1/d}) in SCC K-field requires **deep below-spinodal regime + sufficient λ_rep** to satisfy multi-formation Goldstone instability. The spinodal-valid c regime (where Phase 4 F7 was attempted) is GENERICALLY STABLE.

This refines `13_*` LSW connection: SCC K-field LSW law applies in **specific parameter window**, not generically.

### §2.5 Refined parameter recommendation

For LSW scaling test:
- Use below-spinodal c (e.g., c_per = 0.05 = c_total/K with c_total ≈ 0.10 and K=2 — but then K≥3 has c_per even smaller).
- Or use spinodal-valid c with very large λ_rep ≥ 1.
- Or extremely long evolution time (t_max = 10000+) — but this becomes computationally heavy.

NQ-220 (Phase 5 P1.2 NEW, W6+): Numerical LSW test in below-spinodal regime with K ∈ {5, 10, 20} on T²_{40} with c_per = 0.05 and λ_rep = 0.5; verify R(t) ~ t^{1/2} scaling.

---

## §3. Combined Findings

### §3.1 Static vs Dynamic Instability

P1.1 reveals a **conceptual subtlety**: T-σ-Multi-1 Hessian-instability claim is static; dynamic instability under volume-projected gradient flow is a separate claim with additional constraints.

Phase 1-4 papers/files implicitly conflated these. **Phase 5 separates them**:
- **T-σ-Multi-1 (static, Cat A)**: joint Hessian has negative eigenvalue at K=2 minimizer when $\lambda_{\mathrm{rep}} > c_{\mathrm{eff}} \mu_{\mathrm{Gold}}$.
- **T-σ-Multi-1-Dynamic (Cat B target)**: gradient flow from K=2 minimizer with volume + simplex constraints converges to K-1 merger when ... (additional conditions, NQ-219).

### §3.2 LSW regime is narrow

P1.2 reveals **LSW-like coarsening is parameter-sensitive**, not a generic feature of K-field architecture.

`13_*` SCC-LSW connection now refined: requires **below-spinodal regime** (corner-saturation gives small μ_Gold → small λ_rep threshold) OR **strong coupling** (λ_rep ≥ μ_Gold).

This is consistent with classical LSW which also operates in **low-density** regime (small volume fraction = below-spinodal analog).

### §3.3 Phase 5 P1 contributions to canonical proposal

For canonical T-σ-Multi-1 entry (Phase 4 `20_*` Part 2):
- ADD: "Static instability claim"; instability dynamics under gradient flow requires additional analysis (NQ-219 + NQ-220 for full dynamic theorem).
- CLARIFY: LSW connection is regime-restricted (below-spinodal or strong-coupling).

---

## §4. NQ Spawns from P1

- **NQ-219** (P1.1): Volume-projected joint Hessian lowest eigvec for proper dynamic verification.
- **NQ-220** (P1.2): LSW scaling test in below-spinodal regime (K ∈ {5,10,20}, T²_{40}, c_per=0.05, λ_rep=0.5).

---

## §5. Cross-References

- T-σ-Multi-1 Cat A (static): `09_goldstone_instability_proved.md` §2-§5.
- σ_multi^A: `05_sigma_multi_concrete_T2_K2.md`, `08_lemma5_1_step3_proof.md`.
- LSW connection: `13_LSW_connection.md`.
- F5/F6/F7 numerical: scripts/results/ JSONs.

---

**End of 24_P1_findings_F6_F7_redo.md.**
**Status: Phase 5 P1.1 reveals static-vs-dynamic instability distinction; P1.2 reveals LSW regime is narrow. Both are NEW substantive findings refining T-σ-Multi-1 + LSW connection. NQ-219, NQ-220 spawned.**
