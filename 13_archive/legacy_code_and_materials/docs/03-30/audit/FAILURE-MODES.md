# SCC Failure Modes — Destructive Testing Results

**Date:** 2026-03-30

## Identified Failure Modes

### 1. Complete/Dense Graphs: Sep → 0, Inside → 0
On K_30 (complete graph): Sep=0.119, Inside=0.000. When every node is equally connected to every other, the distinction operator D_t cannot find interior-vs-exterior asymmetry. Formation is structurally impossible on graphs without relational heterogeneity.

**Interpretation:** SCC requires relational structure to work. This is by design — the theory claims that formation emerges from relational organization, so a graph with no relational variation cannot support formation.

### 2. Hub-Spoke (Star) Graphs: Degraded Quality
On star graph (n=50): Sep=0.215, Inside=0.355. The extreme degree heterogeneity (hub has degree 49, spokes have degree 1) creates a single dominant site that captures most cohesion, preventing clean formation.

**Interpretation:** SCC assumes moderate degree heterogeneity. Extreme hub structures may require degree normalization or graph preprocessing.

### 3. Near-Spinodal Volume Fractions: Inside Collapses
At c=0.78 on 10×10 grid: Inside=0.126. When the volume fraction approaches the spinodal boundary, the formation covers most of the graph, leaving no room for boundary-exterior structure.

**Interpretation:** The spinodal constraint (c between 0.211 and 0.789) is necessary but not sufficient. Practically, c should be well within the spinodal range (c < 0.6) for good morphological quality.

## Working Well
- Path graphs (trees): Bind=0.85, Sep=0.97, Inside=1.0
- Disconnected graphs: Formation correctly localizes to one component
- Grid graphs: Robust across all sizes tested
- Community graphs: Best self-referential advantage
