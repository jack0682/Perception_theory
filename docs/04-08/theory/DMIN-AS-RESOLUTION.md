# d_min as Perceptual Resolution: Conceptual Reframing

**Date:** 2026-04-08
**Session:** d_min reconceptualization
**Category:** theory
**Status:** active
**Depends on:** DMIN-FORMULA.md, T7-Enhanced, Canonical Spec §12

---

## 1. Reframing

d_min is NOT a universal constant to be derived. It IS the theory's core prediction about perceptual resolution.

**Old view:** d_min = 4.8 + 0.31√(β/α) - 0.018β/α (a formula to prove)
**New view:** d_min = f(a_cl, τ, α, β) (a personal parameter, determined by individual closure structure)

Just as visual acuity varies between individuals (20/20 vs 20/40), the cohesion field's spatial resolution d_min varies with the closure operator's parameters. This is not a limitation — it is how perception works.

## 2. What d_min Means

$$d_{\min} = \text{minimum distance at which the cohesion field recognizes two separate entities}$$

- d > d_min: closure "sees" two separate formations → two proto-objects
- d < d_min: closure "sees" one formation → one proto-object
- d = d_min: bifurcation point — the moment of perceptual splitting/merging

The mechanism: closure operator Cl(u) = σ(a_cl·(Pu - τ)) performs spatial averaging via P (neighbor mean). When two formations are closer than the averaging scale, P blurs them together → closure treats them as one.

## 3. d_min as Individual Parameter

Each individual's perceptual system is characterized by closure parameters:
- a_cl: closure gain (self-reinforcement strength)
- τ: threshold (boundary criterion)
- α: smoothness (spatial diffusion)
- β: phase separation strength (sharpness)

These determine d_min(a_cl, τ, α, β) for that individual.

**Cat B resolution:** The specific regression coefficients (4.8, 0.31, 0.018) are NOT what the theory needs to predict. They are empirical parameters of a specific "individual" (= specific parameter set). The theory predicts the FUNCTION d_min(·), not specific values.

## 4. What IS Provable (Cat A Targets)

### 4.1 Existence of d_min (sharp threshold)
**Claim:** For any parameter set in the admissible range, there exists a sharp d_min such that:
- d > d_min: two-bump local minimizer exists on the single field
- d < d_min: no two-bump local minimizer exists

**Proof route:** Volume constraint + closure averaging → exterior field ū_ext(d) is monotone increasing as d decreases → ū_ext crosses spinodal u_sp at exactly one point → sharp threshold.

### 4.2 Monotonicity in a_cl
**Claim:** d_min is monotonically decreasing in a_cl (for a_cl < 4):
$$\frac{\partial d_{\min}}{\partial a_{\mathrm{cl}}} < 0$$

Higher closure gain → stronger self-reinforcement → sharper boundaries → better resolution → smaller d_min.

**Proof route:** T7-Enhanced (Hessian boost from closure Gram matrix) → larger stability basin → metastability at smaller d.

### 4.3 Monotonicity in β
**Claim:** d_min is monotonically decreasing in β:
$$\frac{\partial d_{\min}}{\partial \beta} < 0$$

Stronger phase separation → sharper interfaces → shorter tails → smaller d_min.

**Proof route:** Interface width ε = √(2α/β) → tail decay rate increases with β → spinodal threshold reached at shorter d.

### 4.4 d_min^SCC < d_min^AC
**Claim:** Already Cat A. Self-referential closure improves resolution:
$$d_{\min}(a_{\mathrm{cl}} > 0) < d_{\min}(a_{\mathrm{cl}} = 0)$$

**Proof:** T7-Enhanced metastability + mass redistribution (§10.6 of DMIN-FORMULA.md).

## 5. New Prediction

**P6 (Closure-Resolution Correlation):** Individuals with stronger self-referential cohesion (higher neural gain in closure-related processing) exhibit finer spatial resolution in perceptual grouping tasks.

Testable: measure closure-related EEG/fMRI signatures and correlate with psychophysical spatial resolution thresholds in the same subjects.

## 6. Implications for Theory Architecture

d_min moves from "empirical formula (Cat B)" to "structural prediction (Cat A for properties, individual-dependent for values)":

| Aspect | Old Status | New Status |
|--------|-----------|------------|
| d_min existence (sharp threshold) | assumed | **Cat A target** |
| d_min monotone in a_cl | empirical (exp57) | **Cat A target** |
| d_min monotone in β | empirical (exp28) | **Cat A target** |
| d_min^SCC < d_min^AC | Cat A | **Cat A** (unchanged) |
| d_min specific value | Cat B (regression) | **individual parameter** (not a theory prediction) |
| d_min formula coefficients | Cat B | **N/A** (no longer meaningful as universal constants) |
