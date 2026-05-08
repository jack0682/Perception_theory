---
type: log/daily
date: 2026-05-08
session: Session 6 (OMS-2.0 push) — Gates 3 & 4
attacks: OP-OMS-002+
deliverables: op_oms_002_nontrivial_v.md, vp9_nontrivial_v_basin_test.py + .json + .md
---

# Session 6 Gates 3 & 4 — OP-OMS-002+ Non-Trivial Admissible $V$

## Mission

Construct an explicit non-trivial admissible landscape $V \in \mathcal{V}_{\mathrm{adm}}$ with at least 2 stable basins with **distinct** $P_{\mathrm{top}}$ readouts; verify computationally.

## Gate 3 — Theory file `op_oms_002_nontrivial_v.md`

### Construction

For two targets $y_1, y_2 \in \mathbb{R}^6$ (smooth-component readouts at canonical $\lambda^{(1)}, \lambda^{(2)}$) and offset $c \ge 0$:

**Hard min:**
$$V_2(\lambda) = \min\bigl\{ \|P^{\mathrm{sm}}(\lambda) - y_1\|_2^2,\ \|P^{\mathrm{sm}}(\lambda) - y_2\|_2^2 + c \bigr\}.$$

**Smoothed (soft-min):**
$$V_{2,\tau}(\lambda) = -\tau \log\!\bigl(\exp(-D_1/\tau) + \exp(-(D_2 + c)/\tau)\bigr).$$

### Propositions PROVED

| ID | Statement | Status |
|---|---|---|
| NV3, NV8 | $V_2$, $V_{2,\tau}$ DEFINED | DEFINED |
| NV4 | V1 (gauge invariance) | PROVED |
| NV5 | V2 stratified-$C^1$ + continuity | PROVED |
| NV6 | V3 (bounded) | PROVED |
| NV7 | $V_2$ has ≥ 2 basins with distinct readouts | PROVED conditional on H5 (analyticity-supported) |
| NV9 | $V_{2,\tau}$ smooth on regular branches | PROVED |
| NV10 | $V_{2,\tau}$ basin structure preserved for small τ | PROVED (perturbation) |

### Net theory status

$V_2$ and $V_{2,\tau}$ are **PROVED admissible** (V1, V2_strat, V3) and **PROVED nontrivial** (≥ 2 basins) under H5 (target-Jacobian rank ≥ 1). H5 is weaker than H2 of Gap C1; same analyticity argument.

## Gate 4 — Computational verification (VP-9)

### Method

`vp9_nontrivial_v_basin_test.py`:
1. Pre-compute $P^{\mathrm{sm}}$ at the two targets.
2. Triangular grid on Δ²; per-point optimization.
3. Evaluate $V_{2,\tau}$ on each grid point.
4. Discrete gradient descent on the 6-neighbor adjacency.
5. Cluster grid points by attractor; report basin sizes and readout distinctness.

### Targets

- $\lambda^{(1)} = (0.70, 0.15, 0.15)$ — cl-dominant (VP-4 P1).
- $\lambda^{(2)} = (0.15, 0.70, 0.15)$ — sep-dominant (VP-4 P2).

### Results

| Scene | τ | Attractors | Distinct-readout pairs | Verdict |
|---|---|---|---|---|
| **P12** (K=12, 91 pts) | 0.01 | **3** | **2** | ✓ NONTRIVIAL |
| **P12** (K=12, 91 pts) | 0.10 | 2 | 0 | ✗ collapsed (NV10 caveat) |
| **S3** (K=8, 45 pts) | 0.01 | **4** | **4** | ✓ NONTRIVIAL |
| **S3** (K=8, 45 pts) | 0.10 | 2 | 0 | ✗ collapsed |

Total runtime: 97.4 s.

### Readout separations

- P12: $\|y_1 - y_2\| = 0.2424$.
- S3:  $\|y_1 - y_2\| = 0.3238$.

### NV10 caveat confirmed

For τ = 0.10, the soft-min over-smooths and the two basins merge into
one. NV10 explicitly says "for τ small enough"; τ = 0.01 is small enough,
τ = 0.10 is not, for these targets / scenes.

## Net status of OP-OMS-002+

| Sub-claim | Status |
|---|---|
| Definition of $V_2, V_{2,\tau}$ | DEFINED |
| Admissibility (V1+V2_strat+V3) | PROVED |
| ≥ 2 basins on representative scenes | **COMPUTATIONALLY CONFIRMED** for τ = 0.01 |
| Distinct-readout basins | **COMPUTATIONALLY CONFIRMED** (2–4 distinct pairs) |
| H5 (target-Jacobian rank ≥ 1) | COMPUTATIONALLY SUPPORTED |

**OP-OMS-002+ → PROVED admissible + COMPUTATIONALLY SUPPORTED for nontriviality.**

## Files produced

- `THEORY/working/observer_moduli/op_oms_002_nontrivial_v.md`
- `CODE/experiments/observer_moduli/vp9_nontrivial_v_basin_test.py`
- `CODE/experiments/results/observer_moduli/vp9_nontrivial_v_basin.json`
- `CODE/experiments/results/observer_moduli/vp9_nontrivial_v_basin.md`
