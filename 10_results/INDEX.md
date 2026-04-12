---
title: Results Registry
type: index
last_updated: 2026-04-12
total_results: 0
---

# Results Registry — 10_results/

Central registry of analyzed experimental and theoretical results, with interpretation and evidence links.

## Purpose

Track:
- Quantitative measurements and analyses
- Qualitative observations
- Comparison with theoretical predictions
- Evidence chains (result → supports/challenges → theorem)

## Structure

Each result: `R-XXXX` linking to source experiment E-XXXX

**Format:** See `99_templates/TEMPLATE_result.md`

## Results by Source

### From E-0081 (Barrier Measurement)
- R-0081-a: Barrier height B value
- R-0081-b: Parameter dependence analysis

### From E-0082 (Kramers Validation)
- R-0082-a: Escape time τ measurements
- R-0082-b: Theory vs. observed agreement
- R-0082-c: Temperature scaling

### From E-0083 (Thermal Effects)
- R-0083-a: τ(T) relationship
- R-0083-b: Scaling exponent

### From E-0084 (K Emergence)
- R-0084-a: Frequency of K=2 visits
- R-0084-b: Residence time distribution

### From E-0085 (Robustness)
- R-0085-a: Parameter sweep results
- R-0085-b: Success rate across space

## Evidence Chain Examples

```
E-0081 (barrier measured)
  ↓
R-0081 (B = 1.234 ± 0.045 k_B T)
  ↓
Supports T-Kinetic-1 (K=2 is metastable)
Confirms A-0023 (barriers exist)
```

## By Theorem Supported

### T-Kinetic-1 Support
- [R-xxxx]
- [R-xxxx]

### T-Kinetic-2 Support
- [R-xxxx]
- [R-xxxx]

### T-Kinetic-3 Support
- [R-xxxx]
- [R-xxxx]

## Critical Results (May 2026 Decision Points)

**By May 3:** E-0082 results determine viability of kinetic framework
- If τ_empirical ≈ τ_theory (within 2×) → Continue
- If τ_empirical ≠ τ_theory → Framework fails, escalate

## Results Status

| Result | Experiment | Status | Interpretation |
|--------|-----------|--------|-----------------|
| [R-xxxx] | E-xxxx | ✅ Analyzed | [Brief finding] |

---

**Created:** 2026-04-12
**Total Results:** [Count]
**Analyzed:** [Count]
**Awaiting Analysis:** [Count]
