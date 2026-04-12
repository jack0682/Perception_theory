# SCC on Realistic Graph Topologies

**Date:** 2026-03-30

## All 4 realistic topologies produce healthy formations

| Graph | n | Fiedler | Bind | Sep | Inside | Notes |
|-------|---|---------|------|-----|--------|-------|
| Small-world (k=6, p=0.1) | 100 | 0.281 | 0.861 | 0.931 | 0.878 | Stable |
| Scale-free (BA, m=3) | 100 | 1.345 | 0.831 | 0.796 | 0.889 | Sep lower (hub effect) |
| Image-like (8-conn, Gaussian) | 225 | 0.003 | 0.858 | 0.918 | 0.955 | Weighted edges work |
| Hierarchical (4 comms of 25) | 100 | 0.489 | 0.847 | 0.958 | 1.000 | Formation in single community |

## Key Findings

1. **SCC works on non-grid, non-synthetic graphs** — small-world, scale-free, image-like, hierarchical all produce formations with min_diag > 0.79.

2. **Scale-free graphs have lowest Sep** — hub nodes create asymmetric degree distribution that weakens distinction. This is consistent with the star-graph failure mode (diluted version).

3. **Hierarchical graphs give the best results** — formation precisely localizes to one community with Inside=1.0. This validates the topology-dependent value finding: SCC excels on graphs with community structure.

4. **Weighted edges are handled correctly** — the image-like graph with Gaussian distance-dependent weights works without modification.

## Implications for Papers

This data strengthens the claim that SCC is applicable beyond synthetic grids. The scale-free result (Sep=0.796) is the weakest but still above 0.7 threshold.
