---
type: working/vp1-counterexamples
created: 2026-05-07
version: 1.0
project: Observer Moduli Space of SCC
experiment: exp86_vp1_p_resolution_audit.py
op_target: OP-OMS-009
---

> [!nav] Linked: [[MOC_observer_moduli_OMS]] · [[THEORY_INDEX]]


# VP-1 Counterexample Catalog

Documented counterexamples showing P_min = (Bind, Sep, Inside, Persist) is too coarse to
distinguish perceptually distinct observer parameter configurations.

**Counterexample criterion:** ||d(Θ_A) - d(Θ_B)|| < 0.15 AND D_T(Θ_A, Θ_B) > 0.5

where D_T = 3·|K_core_A - K_core_B| + 1.5·|K_mid_A - K_mid_B| + |l_sec_A - l_sec_B| + |l_thr_A - l_thr_B|.

**Total confirmed counterexamples: 4**

---

## CE-1 (Part B, tightest diagnostic match)

**Source:** Optimizer λ sweep on 12×12 grid (Part B)

| | Θ_A (cl_dominant) | Θ_B (cl_sep) |
|---|---|---|
| **λ = (w_cl, w_sep, w_bd)** | (0.60, 0.20, 0.20) | (0.50, 0.30, 0.20) |
| **Bind** | 0.8774 | 0.8657 |
| **Sep** | 0.849 | 0.906 |
| **Inside** | 0.8469 | 0.8883 |
| **Persist** | 1.0 | 1.0 |
| **K_core** | **2** | **1** |
| **K_mid** | 1 | 1 |
| **l_max** | 0.9097 | 0.9508 |
| **l_second** | 0.0251 | 0.0424 |
| **artic** | 0.9724 | 0.9554 |

**||d(Θ_A) - d(Θ_B)|| = 0.071** (tightest diagnostic distance of all CEs)

**D_T(Θ_A, Θ_B) = 3.028** (K_core difference dominates)

**Topological distinction:** K_core = 2 vs 1. Θ_A produces a two-component core at threshold θ=0.9; Θ_B produces a single connected core.

**Why P_min fails:** Inside collapses H0 bar information into one scalar. For Θ_A: l_max=0.91, l_sec=0.025 → Inside ≈ (0.91-0.3)/0.7 × (1-0.025/0.91) ≈ 0.847. For Θ_B: l_max=0.95, l_sec=0.042 → Inside ≈ (0.95-0.3)/0.7 × (1-0.042/0.95) ≈ 0.888. The numbers are close despite K_core differing by 1.

**Resolved by P_top:** T_Θ includes K_core explicitly. K_core(Θ_A) = 2 ≠ 1 = K_core(Θ_B). P_top immediately distinguishes them.

---

## CE-2 (Part B, smallest ||d||)

**Source:** Optimizer λ sweep on 12×12 grid (Part B)

| | Θ_A (cl_dominant) | Θ_B (balanced_cl) |
|---|---|---|
| **λ** | (0.60, 0.20, 0.20) | (0.40, 0.30, 0.30) |
| **Bind** | 0.8774 | 0.8617 |
| **Sep** | 0.849 | 0.907 |
| **Inside** | 0.8469 | 0.9463 |
| **Persist** | 1.0 | 1.0 |
| **K_core** | **2** | **1** |
| **K_mid** | 1 | 1 |
| **l_max** | 0.9097 | 0.9853 |
| **l_second** | 0.0251 | 0.0328 |
| **artic** | 0.9724 | 0.9667 |

**||d(Θ_A) - d(Θ_B)|| = 0.116**

**D_T(Θ_A, Θ_B) = 3.013** (K_core difference dominates)

**Topological distinction:** Same as CE-1. K_core=2 (two-blob equilibrium) vs K_core=1 (single-blob).

---

## CE-3 (Part B)

**Source:** Optimizer λ sweep on 12×12 grid (Part B)

| | Θ_A (cl_dominant) | Θ_B (balanced) |
|---|---|---|
| **λ** | (0.60, 0.20, 0.20) | (0.30, 0.40, 0.30) |
| **Bind** | 0.8774 | 0.8557 |
| **Sep** | 0.849 | 0.9216 |
| **Inside** | 0.8469 | 0.9647 |
| **Persist** | 1.0 | 1.0 |
| **K_core** | **2** | **1** |
| **K_mid** | 1 | 1 |
| **l_max** | 0.9097 | 1.0 |
| **l_second** | 0.0251 | 0.0353 |

**||d(Θ_A) - d(Θ_B)|| = 0.140**

**D_T(Θ_A, Θ_B) = 3.012**

---

## CE-4 (Part D, independent replication on larger graph)

**Source:** High-resolution λ sweep on 15×15 grid (Part D)

| | Θ_A | Θ_B |
|---|---|---|
| **λ** | (0.52, 0.10, 0.38) | (0.66, 0.10, 0.24) |
| **Bind** | 0.8857 | 0.9035 |
| **Sep** | 0.8148 | 0.7132 |
| **Inside** | 0.856 | 0.7916 |
| **Persist** | 1.0 | 1.0 |
| **K_core** | **1** | **0** |
| **l_second** | 0.0087 | 0.0116 |

**||d(Θ_A) - d(Θ_B)|| = 0.122**

**D_T(Θ_A, Θ_B) = 3.003**

**Note:** K_core=0 in Θ_B means the optimizer equilibrium has no connected component above threshold θ=0.9, while Θ_A maintains one. The 15×15 grid replicates the phenomenon at larger scale, independently of the 12×12 results.

---

## Common Structure of All Counterexamples

All 4 counterexamples share the following pattern:

1. **K_core is the discriminating invariant.** In every case, K_core(Θ_A) ≠ K_core(Θ_B), while K_mid and K_low agree (or are within noise).

2. **Inside almost compensates.** The Inside predicate = `(l_max - c)/(1-c) × (1 - l_second/l_max)` partially tracks K_core changes (more components → lower l_max, higher l_second → lower Inside). But the compensation is not exact: ||d|| < 0.15 is achievable because l_max and l_second trade off against each other across parameter changes.

3. **All counterexamples involve closure-dominant λ.** The cl_dominant configuration (w_cl=0.6) consistently produces K_core=2 on 12×12 grids, while more balanced weights produce K_core=1. This is a repeatable basin-boundary phenomenon in the observer parameter space.

4. **P_top resolves all four.** T_Θ = (..., K_core, ...) includes K_core as an explicit component. Every counterexample pair has |K_core_A - K_core_B| = 1, giving D_T ≥ 3.0 and trivially separating the pairs under P_top.

---

## Mechanism: Why Inside Cannot Track K_core

Let u* be the optimizer equilibrium for Θ. Define:
- L_max = largest H0 bar length (= fraction of nodes in largest component at threshold c)
- L_sec = second H0 bar length

Then: Inside(Θ) = (L_max - c)/(1-c) × (1 - L_sec/L_max)

Case K_core=1: typically L_max≈1, L_sec≈small → Inside ≈ (1-c)/(1-c) × 1 = 1 (near 1)
Case K_core=2: L_max≈1 but L_sec also nontrivial → Inside reduced

But the reduction depends on the precise geometry of u*. When the two components have unequal mass, L_sec can be very small (one small blob + one large blob), and Inside can remain high despite K_core=2. CE-1 demonstrates this: L_sec=0.025 for the K_core=2 configuration gives Inside≈0.85, close to the K_core=1 Inside≈0.89 case.

Formally: the map K_core → Inside is not injective. Inside factors through (L_max, L_sec, c), and this factorization loses the integer count K_core.

---

*Generated: 2026-05-07 | exp86_vp1_p_resolution_audit.py*
