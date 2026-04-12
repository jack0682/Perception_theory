---
title: Experiments Registry
type: index
last_updated: 2026-04-12
total_experiments: 0
---

# Experiments Registry — 09_experiments/

Central registry of all validation experiments, organized by type and theorem validated.

## Purpose

Track:
- Barrier measurement experiments (exp81–exp85 kinetic validation)
- Single-formation experiments (exp1–exp65)
- Multi-formation experiments (exp66+)
- Ablation studies and robustness checks

All experiments linked to the theorems they validate.

## Structure

```
09_experiments/
├── E-0081/
│   ├── DESIGN.md
│   ├── exp81_barrier_measurement.py
│   ├── RESULTS.md
│   └── ANALYSIS.md
├── E-0082/
│   ├── DESIGN.md
│   ├── exp82_kramers_validation.py
│   ├── RESULTS.md
│   └── ANALYSIS.md
```

**ID Scheme:** `E-XXXX` corresponding to legacy `expXX` numbering

**Format:** See `99_templates/TEMPLATE_experiment.md`

## Kinetic Theory Experiments (2026-04-13 Onward)

**Critical path for validating Option C:**

| Experiment | Status | Validates | Timeline | Critical? |
|-----------|--------|-----------|----------|-----------|
| E-0081 | Designed | A-0023 (barrier exists) | Apr 13–19 | Yes |
| E-0082 | Designed | A-0024 (Kramers law) | Apr 20–May 3 | **CRITICAL** |
| E-0083 | Designed | Temperature scaling | May 4–10 | Yes |
| E-0084 | Designed | K emergence | May 4–10 | Yes |
| E-0085 | Designed | Robustness | Parallel | Yes |

## Single-Formation Experiments (Completed)

Validation experiments for v1.2 and earlier theorems:

| Range | Count | Status |
|-------|-------|--------|
| exp1–exp25 | 25 | ✅ Complete |
| exp26–exp50 | 25 | ✅ Complete |
| exp51–exp65 | 15 | ✅ Complete (exp65 validation failure) |

## By Theorem Validated

### Closure & Binding
- exp[xx] → T-[xxx]

### Separation & Contrast
- exp[xx] → T-[xxx]

### Boundary & Morphology
- exp[xx] → T-[xxx]

### Persistence & Transport
- exp[xx] → T-[xxx]

### Kinetic Framework (Option C)
- E-0081 → A-0023, T-Kinetic-1
- E-0082 → A-0024, T-Kinetic-2
- E-0083 → Temperature scaling
- E-0084 → T-Kinetic-3
- E-0085 → Robustness

## Experimental Results Summary

| Exp | Result | Prediction Match | Status |
|-----|--------|------------------|--------|
| exp1 | [value] | ✅/❌ | [note] |

---

## Escalation Points

🔴 **CRITICAL:**
- E-0082 fails (Kramers law doesn't hold) → Kinetic framework collapses
- Cannot implement E-0081 (reaction coordinate undefined)

🟠 **HIGH:**
- E-0085 shows <50% parameter space success
- E-0083 shows non-monotonic temperature dependence

---

**Created:** 2026-04-12
**Total Experiments:** [Count]
**Completed:** [Count]
**In Progress:** [Count]
**Designed:** [Count]
