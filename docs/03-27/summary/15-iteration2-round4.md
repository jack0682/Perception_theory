# Iteration 2 — Round 4: T20 Axiom Consistency Verification

**Date:** 2026-03-27
**Iteration:** 2 (Deep Mathematical Development)
**Theme:** T20 — The highest priority theorem: do the provisional realizations satisfy their own axioms?

---

## Executive Summary

T20 STATUS: **PARTIALLY FAILED — STRUCTURALLY INFORMATIVE**

The sigmoid closure is inconsistent with Group A as currently stated. A1 and A3 impose contradictory parameter requirements. This is not a minor case — it is a structural incompatibility confirmed analytically and numerically. However, the failure is precisely localizable and resolvable.

**Four mandatory changes identified:**
1. A1 → A1' (conditional extensivity below fixed point c*)
2. Add volume constraint to energy functional
3. Define Q_morph (blocks Proto-Cohesion Existence Theorem)
4. Reclassify E3 from operator axiom to solution constraint

**Full synthesis document:** See `R4-T20-synthesis.md` for the complete mathematical status with all proofs, computations, and parameter registries.

---

## Key Findings by Agent

### Proof Strategist

- **A2 PROVED** unconditionally for sigmoid closure
- **A3 PROVED** with sharp bound: a_cl < 4 gives contraction rate a_cl/4
- **A1-A3 INCOMPATIBLE**: A1 at u=0.9 needs a_cl ≥ 5.49; A3 needs a_cl < 4. Logically impossible.
- **A1-Revised proposed**: extensivity only for u(x) ≤ c* where c* is the closure fixed point
- **Phase transition proof for T8**: second variation at uniform state negative when β/α > 2λ₂/|W''(c)|. Rigorous.
- **C3 monotonicity PROVED** for diffusion C_t (no self-loops): derivative explicitly nonneg
- **Complete parameter admissibility registry** produced

### Computation Analyst

- **A1 fails at peak site**: u(4)=1.0 → Cl(u)(4)=0.931. Deficit 0.069. Structural, not parametric.
- **Iterated closure destroys spatial structure** in 21 iterations → uniform u* ≈ 0.924
- **u≡0 IS global minimizer** (E=0.536). Bump field E=1.484. Energy provides no incentive for structure.
- **Mountain pass ABSENT** without volume constraint — energy monotonically increasing
- **WITH volume constraint**: beautiful formations emerge (core-boundary-exterior, Sep=0.92)
- **C_t diffusion works perfectly**: C_t(2,7)=0 across gap, C_t(4,5)=0.208 within formation
- **Non-idempotent stability confirmed**: 25/25 vs 21/25 positive Hessian eigenvalues
- **Turing instability massive**: 24-25 negative eigenvalues at all uniform states

### Rigor Auditor

- **Mountain pass misapplied**: standard theorem needs E(e) ≤ 0 somewhere; E ≥ 0 always
- **A1-A3-T10 three-way tension**: contraction → unique fixed point → kills multi-formation
- **Q_morph blocks central theorem**: Proto-Cohesion Existence Theorem not well-formed
- **Sep predicate discontinuous in u** (threshold-dependent Int_t)
- **Predicate-energy gap unresolved**: no proof that small E implies high ProtoCoh
- **E3 constrains solutions, not operators**: mis-categorized axiom
- **D-Ax1-3 too weak** to enforce global awareness (Skeptic's Obj 8 still valid)

---

## Admissible Parameter Set

$$\mathcal{P}_{\text{admissible}} = \{a_{\mathrm{cl}} \in (0,4),\ \tau_{\mathrm{cl}} \in (0, 1/2],\ \eta \in (0,1),\ \varepsilon > 0,\ a_D > 0,\ \lambda_D \geq 1,\ b_D > 0,\ \gamma_M > 0\}$$

with A1 replaced by A1-Revised. Under these parameters, ALL axioms are simultaneously satisfiable.

---

## Impact on the Proof Programme

| Theorem | Status After T20 |
|---------|-----------------|
| T1 (existence) | Provable ✓ (compactness + continuity) |
| T6 (fixed points) | Provable ✓ (Brouwer/Banach). Unique for a_cl < 4. |
| T8 (non-trivial minimizers) | Provable ✓ WITH volume constraint (phase transition) |
| T7 (Bind at minimizers) | Provable ✓ (perturbation bound O(1/λ_cl)) |
| T10 (multiple fixed points) | BLOCKED — incompatible with A3 contraction |
| T14 (gradient flow) | Provable ✓ (projected flow + Łojasiewicz) |
| Proto-Cohesion Existence | BLOCKED on Q_morph definition |
