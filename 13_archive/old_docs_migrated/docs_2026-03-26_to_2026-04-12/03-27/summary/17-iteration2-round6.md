# Iteration 2 — Round 6: C_t Formalization — Complete Axiom Verification

**Date:** 2026-03-27
**Iteration:** 2 (Deep Mathematical Development)
**Theme:** Making C_t rigorous — from candidate to proved operator

---

## Executive Summary

**C_t STATUS: ALL AXIOMS (C1-C4) PROVED** for the diffusion candidate on finite X_t.

**Critical finding: Cesàro form is axiom-compliant but structurally deficient.** The Cesàro average destroys within-formation pairwise distance information (converges to stationary distribution π(y) independent of source x). The resolvent form G_α = α(I-(1-α)P)^{-1} is strictly superior — preserves distance sensitivity, same axiom proofs apply, adds principled scale parameter α.

**Two mandatory axiom amendments:**
1. **Add C5 (Symmetry):** C_t(x,y) = C_t(y,x). Conceptually required; current form has ‖asymmetry‖ = 0.058.
2. **Amend C3 to local monotonicity:** C_t(x,x) monotone in u(x) with other values fixed.

---

## Proof Results (Proof Strategist)

| Axiom | Status | Key Technique |
|-------|--------|--------------|
| C1 (Dependence) | **PROVED** | Construction inspection |
| C2 (≠ Adjacency) | **PROVED** | Two explicit witnesses (4-site bottleneck, 3-site chain) |
| C3 (Monotone reflexivity) | **PROVED** | Derivative ≥ 0 (general, including self-loops); u(x) cancels from outgoing, increases incoming |
| C4 (Convergence) | **PROVED** | Cesàro of finite Markov chain; block structure for disconnected components |

**Sep reformulation demonstrated:** C_t-weighted Sep differs from old Sep (example: 0.68 → 0.74 for same field). Structural improvement: threshold-free site selection, global awareness, multi-formation ready.

## Computation Results (Computation Analyst)

- **3 orders of magnitude discrimination:** core-core 0.06-0.16 vs transition-boundary 0.00003
- **Boundary identification binary-sharp:** 2940-12500× drop at formation edge
- **C_t NOT symmetric:** ‖C_t - C_tᵀ‖ = 0.058 (needs fixing)
- **C_t-weighted Sep:** 15% E_sep reduction (boundary noise smoothed)
- **Self-co-belonging monotone in u(x):** confirmed numerically

## Rigor Audit Findings

### Cesàro Degeneration (CRITICAL)
Within connected components: P̄(x,y) → π(y) regardless of source x. All core sites have nearly identical C_t profiles. **Within-formation pairwise information DESTROYED.**

- For Sep (uses diagonal C_t(x,x)): Cesàro adequate ✓
- For multi-formation (T11, T12, needs pairwise): Cesàro **insufficient** ✗

### Resolvent Recommendation
G_α = α(I-(1-α)P)^{-1} preserves distance via geometric decay (1-α)^k. Same C3 proof applies. Symmetrizable. Scale parameter α is a feature. **Strictly superior at no cost.**

### Symmetry Requirement
Conceptually: co-belonging is mutual. Computationally: ‖asymmetry‖ = 0.058 (non-negligible). Fix: similarity transform Ĝ = Π^{-1/2}G_αΠ^{1/2}.

---

## Cumulative Status (R4-R6)

| Component | Status |
|-----------|--------|
| A1 | Revised (conditional extensivity below c*) |
| A2 | Proved unconditionally |
| A3 | Proved for a_cl < 4 |
| A4 | Trivially satisfied |
| C1-C4 | **ALL PROVED** |
| C5 (Symmetry) | **NEW — proposed** |
| D-Ax1-4 | All satisfied |
| E1-E4 | Satisfied (E3 conditional) |
| Volume constraint | **MANDATORY** |
| Q_morph | **STILL UNDEFINED** (→ R7) |
| T8 (non-trivial minimizer) | **PROVED** |

## Files Produced

- `R6-Ct-proof-strategist.md` — Complete C1-C4 proofs + Sep reformulation
- `R6-Ct-computation.md` — Full numerical verification on 5×5 grid
- `R6-Ct-rigor-preaudit.md` — Cesàro vs resolvent analysis
- `R6-Ct-rigor-audit.md` — Complete audit with symmetry/degeneration findings
- `R6-Ct-synthesis.md` — Definitive C_t status (pending from Synthesizer)
