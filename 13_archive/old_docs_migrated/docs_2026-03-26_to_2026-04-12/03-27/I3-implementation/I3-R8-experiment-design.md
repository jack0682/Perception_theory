# Iteration 3 R8 — Experiment Designer: Q_morph Validation

**Author:** Experiment Designer | **Iteration:** 3, Round 8

## 8 Adversarial Test Cases (ADV1-ADV8)
Key: ADV2 (checkerboard) may expose Q_morph weakness — high Artic but no spatial coherence.

## 3 Artic Variants Compared
- v1: threshold counting (19 levels) — likely worst
- v2: variance-based — principled
- v3: entropy-based — robust

## Large-Grid Scaling: n up to 10⁶
Persistence is O(n log n). Expected: 1000×1000 in <5s.

## Predictions
- P-Q1: Checkerboard is the critical adversarial case
- P-Q2: Persistence computation is practically free
- P-Q4: ℓ_max · Artic beats PersistDom-based variants (discontinuity issue)

## Budget: ~45 minutes, 2,025 evaluations
