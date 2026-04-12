# Fiedler Extreme Limit: Theory Validation from 64×64 to 1024×1024

**Date:** 2026-04-07  
**Session:** High-resolution grid scaling analysis  
**Category:** theory (asymptotic analysis)  
**Status:** In progress — awaiting computation results

---

## Research Question

**Does the Fiedler resonance phenomenon persist into the continuum limit (n → ∞)?**

The grid-size scan (10×10 to 30×30) revealed:
- Asymmetry oscillates with lattice size
- 20×20 is a resonance peak (Fiedler correlation 0.599)
- Larger grids show sign flips and magnitude changes

**Key question:** Is this a finite-size artifact that disappears for large n, or a fundamental property of soft cohesion on graph lattices?

---

## Hypothesis

### H1: Finite-Size Artifact (asymmetry → 0 as n → ∞)
If soft cohesion fields naturally seek symmetric configurations in the large-n limit:
- Asymmetry should decay: asym(n) ~ O(1/√n) or faster
- Fiedler resonance peaks should smooth out
- K=2 converges to balanced configurations globally
- **Implication:** Asymmetry is a lattice discretization effect, not physical

### H2: Persistent Resonance (asymmetry oscillates forever)
If asymmetry is tied to lattice geometry's spectral structure:
- Oscillations persist: asym(n) remains order O(1) or bounded away from 0
- Fiedler vectors maintain asymmetry even for large n
- K=2 configurations show location-dependent energy landscapes
- **Implication:** Asymmetry is intrinsic to how fields couple to graph structure

### H3: Weak Convergence (asymmetry → negative bias)
Intermediate case observed in earlier scan (n ≥ 200):
- Asymmetry stabilizes at negative bias: asym(n) → −c < 0
- Oscillations dampen above n = 200
- Large grids favor Type A (centered K=2) universally
- **Implication:** Type selection is n-dependent, convergence to one phase

---

## Measurement Plan

### Data to Collect (64×64 to 1024×1024)

For each grid size g ∈ {64, 128, 256, 512, 1024}:

1. **Fiedler Eigenvalue**
   - λ₂ (second smallest eigenvalue of Laplacian)
   - Scaling law: λ₂ ∝ ? vs n

2. **Fiedler Vector Properties**
   - Min/max values: v₂ ∈ [v_min, v_max]
   - Range: Δv = v_max − v_min
   - Asymmetry (skewness): How concentrated is weight toward extremes?

3. **Spectral Asymptotics**
   - Spectrum shape: Are small eigenvalues O(1) or O(1/n)?
   - Gap λ₃ − λ₂: Does the eigengap shrink?

4. **Fiedler-Formation Alignment**
   - (From exp66 when available) Does K=1 formation center align with v₂?
   - Correlation: ⟨u, v₂⟩ / (||u|| ||v₂||)

---

## Expected Behavior Under Each Hypothesis

### H1: Decay to Symmetry
```
n:          64      128     256     512     1024    ∞
asym(n):    ±0.5 → ±0.3 → ±0.2 → ±0.1 → ±0.05 → 0
λ₂:         ~ 0.1  ~ 0.05 ~ 0.025 ~ 0.01 ~ 0.005 ~ 0
Pattern:    Random → dampens → symmetric
```
- Conclusion: Finite-size lattice artifact, irrelevant to continuum SCC

### H2: Persistent Oscillation
```
n:          64      128     256     512     1024    ∞
asym(n):    ±0.5 → ±0.4 → ±0.35 → ±0.33 → ±0.35 → oscillates
λ₂:         ~ 0.1  ~ 0.05 ~ 0.025 ~ 0.01 ~ 0.005 → 0 (but asym persists)
Pattern:    Peak at 64, then periodic with amplitude staying O(1)
```
- Conclusion: Fundamental to graph-field coupling, persists in continuum

### H3: Convergence to Type A
```
n:          64      128     256     512     1024    ∞
asym(n):    −0.2 → −0.15 → −0.10 → −0.08 → −0.05 → −c
λ₂:         ~ 0.1  ~ 0.05 ~ 0.025 ~ 0.01 ~ 0.005 → 0
Pattern:    Small oscillations around −c, amplitude decays
```
- Conclusion: Large grids select Type A formation universally, asymptotic bias toward centered K=2

---

## Analysis Methods

### 1. Scaling Law Fitting

For each observable X(n):

```
X(n) = A + B·n^α + C·sin(ω·log n) + ...
```

Fit power law and periodic components separately:
- Power law exponent α tells if X → 0, constant, or diverges
- Period ω in log(n) space reveals lattice resonance frequency

### 2. Spectral Asymptotics

For Laplacian spectrum on d-dimensional lattice:
- Known theory (continuum): λ_k ~ (kπ)²/L² for continuous domain
- On graphs: λ_k ~ O(k/n^{1/d}) for d-dimensional lattice
- Check: Does λ₂(n) match asymptotic formula?

### 3. Phase Transition Detection

If there's a critical n* where behavior changes:
- Look for discontinuities in derivatives d(asym)/d(log n)
- Check if oscillation frequency changes

### 4. Conformal Invariance

Does the behavior depend on lattice type?
- Square vs rectangular (16:9 aspect ratio)
- Does asym(n) for rectangular grids follow same law?

---

## Deliverables

1. **Plot 1:** Asymmetry vs log(n)
   - Raw data + power law fit + periodic component
   - Shows whether H1, H2, or H3 is supported

2. **Plot 2:** Fiedler eigenvalue λ₂ vs n
   - Check if λ₂ ~ 1/n (continuous limit) or O(1)
   - Overlay with asym to see correlation

3. **Plot 3:** Fiedler vector properties (range, skewness)
   - Do they decay to zero or stabilize?

4. **Table 1:** Numerical values for each grid size
   - Exact λ₂, asym, Fiedler range, time taken

5. **Conclusion Document**
   - Which hypothesis (H1/H2/H3) is supported?
   - What does this tell us about SCC in the continuum limit?

---

## Theoretical Implications

### If H1 (Decay): 
- Asymmetry is a finite-lattice discretization effect
- In continuum limit (HD images, 1920×1080), expect symmetric K=2 configurations
- Fiedler resonance is an artifact of coarse discretization
- **For applications:** Use fine grids (>512×512) for symmetric, stable formations

### If H2 (Persistent):
- Asymmetry reflects fundamental graph-field interaction
- Even in continuum limit, K=2 formations may not be perfectly centered
- Fiedler modes permanently bias formation placement
- **For applications:** Expect location-dependent formation types even at HD resolution

### If H3 (Convergence to Type A):
- Large-scale grids universally prefer centered K=2 (Type A)
- Oscillations dampen for n > 1000
- Intermediate grids (100-500) show transient asymmetry
- **For applications:** 1024×1024 and above should show stable, centered K=2 formations

---

## Next Steps (Conditional)

**After collecting Fiedler data:**

1. **If H1 supported** → Move to image applications immediately (asymmetry won't matter)
2. **If H2 supported** → Need exp66 (formation tracking) to understand Type B permanence
3. **If H3 supported** → Skip to exp67 (rectangular grids) to confirm universal Type A at large n

---

## Status

- [x] Hypothesis formulation
- [x] Measurement plan
- [ ] Data collection (64×64 to 1024×1024) — in progress
- [ ] Scaling law fitting
- [ ] Conclusion

**ETA for results:** ~5 minutes (Fiedler computation ongoing)
