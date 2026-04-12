---
title: Counterexamples Registry
type: index
last_updated: 2026-04-12
total_counterexamples: 0
---

# Counterexamples Registry — 08_counterexamples/

Central registry of counterexamples, failures, and boundary cases that reveal limitations.

## Purpose

Document:
- Counterexamples that refute claims (with resolution)
- Boundary cases where theory breaks down
- Parameter ranges where assumptions fail
- Failure modes and edge cases

This is a **protective mechanism** against silent assumptions.

## Structure

Each entry: `X-XXXX` (X for "counterexample" or failure)

**Format:** See `99_templates/TEMPLATE_counterexample.md`

**Severity:**
- 🔴 **Critical:** Refutes core theorem; needs fundamental rethinking
- 🟠 **Major:** Limits theorem to narrower domain; needs assumption refinement
- 🟡 **Minor:** Edge case; handled by caveat

## Current Counterexamples

(Will be populated as failures are discovered during development)

| ID | Refutes | Severity | Status |
|----|---------|----------|--------|
| X-0001 | [T-xxxx or C-xxxx] | 🔴/🟠/🟡 | [open/resolved] |

## By Severity

### 🔴 Critical Failures
[X-xxxx list — require fundamental change]

### 🟠 Major Limitations
[X-xxxx list — require domain restriction or assumption refinement]

### 🟡 Minor Edge Cases
[X-xxxx list — handled by caveats]

## By Type

### Theorem Counterexamples
Claims that appeared true but have exceptions:
- [X-xxxx]

### Assumption Violations
Cases where implicit assumptions fail:
- [X-xxxx]

### Parameter Range Failures
Parameter combinations where theory breaks:
- [X-xxxx]

### Edge Cases
Boundary conditions that reveal behavior:
- [X-xxxx]

## Resolution Tracking

### Resolved (Assumption Refined)
[X-xxxx] → [How resolved]

### Resolved (Domain Restricted)
[X-xxxx] → [Restricted to what domain]

### Open (No Resolution Yet)
[X-xxxx] → [Why still open]

---

## Purpose & Value

This registry serves as a **firewall against implicit assumptions**. Every counterexample either:

1. **Forces refinement** of a claim (good scientific practice)
2. **Reveals unstated assumptions** that must be documented
3. **Maps the boundary** of what the theory actually covers

---

**Created:** 2026-04-12
**Counterexamples Found:** [Count]
**Resolved:** [Count]
**Still Open:** [Count]
