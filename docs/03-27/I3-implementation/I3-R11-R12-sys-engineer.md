# Iteration 3 R11-R12 — Systems Engineer: Benchmarks + Scalability Modules

**Author:** Systems Engineer | **Iteration:** 3, Rounds 11-12

## R11: Benchmarks Module
- SCCMethod vs baselines: Otsu, spectral clustering, normalized cuts, Allen-Cahn (no self-ref)
- Quality metrics: formation count, boundary IoU, diagnostic vector, noise stability
- Key comparison: SCC vs Allen-Cahn. Hypothesis: self-referential terms produce qualitatively different formations.
- Synthetic suite + real-proxy datasets

## R12: Scalability Module
- 6 acceleration strategies: sparse ops, Hutchinson C_t, warm-start, gradient caching, batch eigen, BB step size
- Scaling targets: n=100 (instant) → n=100K (feasibility test)
- Profile: grid sequence 10²→316². Plot time vs n. Identify C_t backend crossover.
- Bottleneck: C_t dominates for n>2500; persistence and D_t negligible
