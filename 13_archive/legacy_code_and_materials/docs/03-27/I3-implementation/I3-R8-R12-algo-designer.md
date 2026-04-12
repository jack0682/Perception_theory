# Iteration 3 — Algorithm Designer Consolidated: Q_morph, Multi-Formation, Transport, Scalability

**Author:** Algorithm Designer | **Iteration:** 3, Rounds 8-12

## Q_morph (R8): O(n log n) Union-Find
ℓ_max via superlevel persistence. Artic = Var(u)/(c(1-c)). Product Q_morph ∈ [0,1]. CHEAPEST module.

## Multi-Formation (R9): Sequential Extraction
Find strongest formation → suppress → repeat. K from persistence diagram (free). C_t spectral for v2 (deferred).

## Transport (R10): Softmax k-NN
O(n·k·log n) via k-d tree. Warm-starting: ~30 steps instead of ~500. Feasible for offline video.

## Scalability (R12): n=10⁶ on CPU, 10⁷ on GPU
Bottleneck: semi-implicit factorization (AMG at n>10⁶). C_t diagnostic-only = decoupled from gradient loop.
Without C_t in loop: 10ms/step at n=10⁶. With C_t diagnostic every 50 steps: +20s total.

## Architecture Summary
Per-step: Cl+J, D+J, ∇E_bd, Project — all O(|E|)
Periodic (÷50): Q_morph O(n log n), Sep_new O(|E|), C_t Hutchinson O(90|E|)
