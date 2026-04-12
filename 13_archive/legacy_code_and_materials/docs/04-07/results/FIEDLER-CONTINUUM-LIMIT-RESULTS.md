# Fiedler Continuum Limit Results (64×64 to 1024×1024)

**Date:** 2026-04-07  
**Analysis:** High-resolution grid scaling — theory validation  
**Status:** Computation in progress — awaiting results

---

## Experimental Setup

**Question:** Does Fiedler resonance (20×20 asymmetry spike) persist into the continuum limit?

**Method:**
- Square grids: 64×64, 128×128, 256×256, 512×512, 1024×1024
- For each: compute Fiedler vector v₂, eigenvalue λ₂, measure asymmetry

**Hypotheses to test:**

| Hypothesis | Prediction | Implication |
|-----------|-----------|------------|
| **H1: Decay to symmetry** | asym(n) → 0 as n → ∞ | Artifact of discretization |
| **H2: Persistent resonance** | asym(n) ~ O(1), oscillates | Fundamental to graph-field coupling |
| **H3: Type A convergence** | asym(n) → negative constant | Large grids universally prefer centered K=2 |

---

## Results (To Be Filled)

### Raw Data

```
Grid Size   n           λ₂          v₂ Range    Asymmetry   Time (sec)
64×64       4,096       [pending]   [pending]   [pending]   [pending]
128×128     16,384      [pending]   [pending]   [pending]   [pending]
256×256     65,536      [pending]   [pending]   [pending]   [pending]
512×512     262,144     [pending]   [pending]   [pending]   [pending]
1024×1024   1,048,576   [pending]   [pending]   [pending]   [pending]
```

### Scaling Law Analysis

**Fiedler Eigenvalue λ₂:**
```
Fit: λ₂ ~ A · n^α

Expected from theory:
  - Continuum Laplacian: λ_k ~ (πk)²/L²  →  λ₂ ~ 1/n for d=2
  - Graph Laplacian: λ_k ~ k/n^{2/d}     →  λ₂ ~ 1/n for d=2

Observed:
  α = [pending]
  A = [pending]
  
Conclusion: [pending]
```

**Asymmetry:**
```
Fit: |asym| ~ A · n^α + periodic component

If H1 (decay): α < −0.5, A small
If H2 (persistent): α ≈ 0, A ~ O(0.1-0.3)
If H3 (convergence): α < −0.3, trend to negative

Observed:
  Power law: α = [pending], A = [pending]
  Oscillations: [pending]
  
Conclusion: [pending]
```

---

## Analysis

(To be filled after computation completes)

### Plot 1: Fiedler Eigenvalue Scaling

```
[Text-based ASCII plot will be inserted]
λ₂ vs log₁₀(n)
```

### Plot 2: Asymmetry Scaling

```
[Text-based ASCII plot will be inserted]
|asym| vs log₁₀(n)
```

### Plot 3: Formation Type Prediction

```
[Based on asymmetry sign and magnitude]
n = 64:     Type [pending]
n = 128:    Type [pending]
n = 256:    Type [pending]
n = 512:    Type [pending]
n = 1024:   Type [pending]
```

---

## Interpretation

(To be filled after analysis)

**Which hypothesis is supported?**

- [ ] **H1: Decay to symmetry** — Fiedler resonance is finite-lattice artifact
- [ ] **H2: Persistent resonance** — Fiedler resonance is fundamental
- [ ] **H3: Type A convergence** — Large grids universally prefer centered K=2
- [ ] **Mixed/Inconclusive** — Need more data

**Theoretical Implications:**

```
[Will be written based on results]
```

**For Image Applications:**

```
[Will specify: safe to use 1024×1024? How to handle Type B formations?]
```

---

## Extreme Limit Characterization

If results support H1 or H3, we can write:

$$\text{asym}(n) \sim C \cdot n^{\alpha} + O(\text{oscillations})$$

where C and α encode the continuum behavior.

**Limiting behavior (n → ∞):**
```
[Will be determined from data]
```

---

## Next Steps

Contingent on results:

1. **If H1:** Move directly to 1920×1080 image applications (asymmetry negligible)
2. **If H2:** Run exp66 (formation tracking) to understand Type B permanence
3. **If H3:** Validate on rectangular grids (1280×720, 960×540) to confirm universal Type A

---

## Status Log

- [ ] 64×64 computation complete
- [ ] 128×128 computation complete
- [ ] 256×256 computation complete
- [ ] 512×512 computation complete
- [ ] 1024×1024 computation complete
- [ ] Analysis complete
- [ ] Hypothesis selection complete
- [ ] Theory update complete

---

## Related Documents

- `FIEDLER-EXTREME-LIMIT-ANALYSIS.md` — Experimental design and hypotheses
- `GRID-SIZE-RESONANCE.md` — 20×20 peak discovery
- `K2-FLAVOURS-AND-GRID-SIZE.md` — Type A/B classification
