# Iteration 3 R4 — Algorithm Designer: Core Optimization Algorithm

**Author:** Algorithm Designer
**Date:** 2026-03-27
**Iteration:** 3 (Implementation), Round 4

---

## CORE ALGORITHM: FindFormation

### Phase 0: Setup
- Validate admissibility (a_cl < 4, β/α > 4λ₂/|W''(c)|, volume range, resolvent spectral bound)
- Compute L, λ₂ (sparse Lanczos)
- Auto-normalize λ weights by energy scale

### Phase 1: Initialization
- u⁰ = c·1 + ε·v₂ (Fiedler perturbation seeds dominant instability)
- Project to Σ_m ∩ [0,1]^n

### Phase 2: Gradient Flow (Semi-Implicit)
- (I + Δτ·4αλ_bd·L)u^{k+1} = u^k − Δτ·[explicit Cl + Sep + double-well terms]
- Armijo backtracking for step size
- Every 10 steps: diagnostic vector check
- Converge when ‖∇E_proj‖ < ε AND Bind > threshold AND Sep > threshold

### Phase 3: Refinement
- Iterated closure to fixed point (~24 iterations for a_cl=3)
- Final diagnostic vector

### Phase 4: Multi-Start
- Repeat with different perturbations
- Collect distinct minimizers

## KEY OPERATORS

| Operator | Algorithm | Complexity |
|----------|-----------|-----------|
| Cl_t | Sparse mat-vec + sigmoid | O(|E|) |
| D_t | Two P_t products + sigmoid | O(|E|) |
| C_t (resolvent) | Neumann series k=5-10 | O(k·|E|) |
| Q_morph | Union-Find persistence + Var | O(n log n) |
| ∇E_bd | Laplacian + double-well | O(|E|) |
| ∇E_cl | Jacobian transpose × residual | O(|E|) |
| ∇E_sep | Distinction Jacobian | O(|E|) |

## SCALING

n=10⁶ feasible in ~20s. Bottleneck: C_t via Neumann (k·|E|). For n>10⁶: lazy C_t update (every 50-100 steps).

## PARAMETER NORMALIZATION

MANDATORY. At initialization, evaluate each E_i, set λ_i = w_i/E_i so all terms contribute comparably. User controls relative weights w_cl:w_sep:w_bd.

## PHASE TRANSITION DISPLAY

Compute and show: "β/α = X. Critical threshold = Y. Status: Z% above/below threshold."
