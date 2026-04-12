# Iteration 3 R10 — Experiment Designer: Temporal Persistence

**Author:** Experiment Designer | **Iteration:** 3, Round 10

## FIRST-EVER PERSIST COMPUTATION

6 synthetic temporal sequences on 20×20 grid, T=10 steps:
- T1: Simple translation (1px/step)
- T2: Translation + deformation
- T3: Translation + occlusion
- T4: Stationary (control)
- T5: Dissolving formation
- T6: Splitting formation

4 transport strategies compared: oracle correspondence, feature matching, no transport, identity.

## KEY PREDICTION: P-T7
T1 (translate) and T4 (static) should achieve Bind≥0.9, Sep≥0.8, Inside≥0.5, Persist≥0.7 simultaneously. **FIRST COMPLETE PROTO-COHESION DEMONSTRATION** — all 4 components.

## BUDGET: ~3 hours (240 optimizer runs + 900 transport computations)

## SIGNIFICANCE
Addresses "largest remaining gap" from R13. Any Persist computation is a first. If it works on a translating blob, temporal theory is viable. If it fails, fundamental rework needed.
