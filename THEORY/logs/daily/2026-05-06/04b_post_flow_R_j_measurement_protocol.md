# 04b_post_flow_R_j_measurement_protocol.md — Post-Flow R_j Measurement Protocol

**Session:** 2026-05-06 (W6 Day 3 G3.4, sub-file of `04_nq_g1_2_ext_design.md`).
**Goal:** Sampling protocol, aggregation rules, and statistical reporting for NQ-G1-2-ext.
**Status:** Protocol spec. Implements §2-§3 of the main design `04_nq_g1_2_ext_design.md`.

---

## §1. Sampling Protocol

**Measurement variable:** $\|R_j(t)\|_\infty = \max_{i \in V} |u^{(j)}(t)_i - u^{(j),\mathrm{ideal}}_i|$ for each active slot $j$.

**Sampling schedule:** Every 50 gradient steps, at $t \in \{50, 100, 150, \ldots, 1000\}$ → 20 measurement snapshots per config.

**Active slot filter:** Only measure $j$ with $\|u^{(j)}(t)\|_\infty > \varepsilon = 0.225$ at snapshot time (inactive slots excluded from statistics; their $\|R_j\|_\infty$ is trivially small and uninformative for regime assessment).

**Reference held fixed:** $u^{(j),\mathrm{ideal}}$ is computed once from $\mathbf{u}_0$ (see `04a` §3) and reused for all 20 snapshots. This tests whether the flow *exits* the regime, not whether the ideal *tracks* the flow.

---

## §2. Per-Config Aggregation

For each of the 960 wq1 configs, compute:

| Quantity | Formula | Purpose |
|---|---|---|
| `max_R_inf` | $\max_{t, j\,\mathrm{active}} \|R_j(t)\|_\infty$ | Worst-case residual; primary hypothesis test |
| `avg_R_inf` | $\frac{1}{|\text{active slots}| \cdot 20}\sum_{t,j} \|R_j(t)\|_\infty$ | Average regime deviation |
| `final_R_inf` | $\max_{j\,\mathrm{active}} \|R_j(1000)\|_\infty$ | Near-convergence residual; stable-regime check |
| `t_exit_50` | first $t$ s.t. $\max_j \|R_j(t)\|_\infty > \rho_\mathrm{pert}/2$, or $\infty$ | Regime exit time |

---

## §3. Threshold Values

From `l1i_constants_feasibility.py` parameter setup (canonical ε=0.225, β standard):

| Threshold | Value | Source |
|---|---|---|
| $\rho_\mathrm{pert}/4$ | `l1i_constants.rho_pert / 4` | T-L1-F P9 tight bound (H-G1-2-ext-A) |
| $\rho_\mathrm{pert}/2$ | `l1i_constants.rho_pert / 2` | T-L1-F P9 exact bound (H-G1-2-ext-B threshold) |

**If `l1i_constants.rho_pert` is not yet implemented:** use $\rho_\mathrm{pert} = 0.1$ as a conservative placeholder (to be updated W7 D1 after checking `l1i_constants_feasibility.py`).

---

## §4. Population-Level Statistical Reporting

After collecting 960 per-config summaries, compute:

**Primary classification (mutually exclusive):**
- `frac_A`: fraction of configs with `max_R_inf` ≤ $\rho_\mathrm{pert}/4$ → supports H-G1-2-ext-A
- `frac_B`: fraction of configs with `max_R_inf` > $\rho_\mathrm{pert}/2$ → supports H-G1-2-ext-B
- `frac_C`: fraction of configs with $\rho_\mathrm{pert}/4 <$ `max_R_inf` ≤ $\rho_\mathrm{pert}/2$ → intermediate

**Hypothesis determination rule:**
```
if frac_A > 0.5:   outcome = "H-G1-2-ext-A"   # majority satisfy P9-tight
elif frac_B > 0.5: outcome = "H-G1-2-ext-B"   # majority exit regime
else:              outcome = "H-G1-2-ext-C"   # mixed distribution
```

**Histogram output:**
- Bin `max_R_inf` values into 20 bins over $[0, 1]$; report bin counts.
- Bin `final_R_inf` values similarly (near-convergence distribution).
- Bin `t_exit_50` (capped at 1000 for non-exiters); shows regime exit timing.

**Summary table** (write to `results/nq_g1_2_ext_summary.txt`):

```
NQ-G1-2-ext Results Summary
============================
N_configs : 960
rho_pert  : <value>
rho_pert/4: <value>
rho_pert/2: <value>

frac_A (max_R_inf <= rho/4) : XX.X%
frac_C (rho/4 < max_R_inf <= rho/2): XX.X%
frac_B (max_R_inf > rho/2)  : XX.X%

Outcome: H-G1-2-ext-[A/B/C]

mean max_R_inf : X.XXXX
median max_R_inf: X.XXXX
p95 max_R_inf  : X.XXXX

Canonical implication: [from 04_nq_g1_2_ext_design.md §6 table]
```

---

## §5. Connection to Canonical Implication

From `04_nq_g1_2_ext_design.md` §6:

| Outcome | Action |
|---|---|
| H-A (`frac_A > 50%`) | Add positive production reach note to T-L1-F entry; no caveat needed |
| H-B (`frac_B > 50%`) | W7 D2 supervised canonical erratum: retroactive caveat on T-L1-F/M Cat A conditional |
| H-C (mixed) | NQ-G1-2-ext-2 follow-up: regime-dependent characterization; W8 |

The W7 D2 supervised erratum (if H-B) follows the T-σ-Theorem-4 pattern: add a precision remark after the main theorem statement clarifying the production-reach limitation.

---

**End of `04b_post_flow_R_j_measurement_protocol.md`. G3.4 cluster complete (main + 04a + 04b). NQ-G1-2-ext fully specified for W7 D1 cold-start execution.**
