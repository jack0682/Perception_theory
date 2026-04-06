"""Supplementary: K=2 vs K=1 at total_c=0.5 (where equal split stays in spinodal)."""

import numpy as np
import sys
sys.path.insert(0, '/home/jack/ex')

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation
from scc.energy import EnergyComputer
from scc.multi import find_k_formations

graph = GraphState.grid_2d(15, 15)
n = graph.n

import math
c_lo = (3 - math.sqrt(3)) / 6
c_hi = (3 + math.sqrt(3)) / 6

# Test with total_c = 0.5 => M = 112.5, each half = 56.25, c_half = 0.25 (in spinodal)
for total_c in [0.5, 0.6, 0.7]:
    total_m = total_c * n
    c_half = total_c / 2

    print(f"\n{'='*60}")
    print(f"Total c={total_c}, M={total_m}, c_half={c_half:.4f}")
    print(f"c_half in spinodal? {c_lo < c_half < c_hi}")
    print(f"{'='*60}")

    # K=1
    params_k1 = ParameterRegistry(volume_fraction=total_c)
    valid, v, _ = params_k1.validate(fiedler_eigenvalue=graph.fiedler)
    if not valid:
        beta_crit = params_k1.beta_critical(graph.fiedler)
        params_k1 = ParameterRegistry(volume_fraction=total_c, beta_bd=max(beta_crit*2, 10))

    result_k1 = find_formation(graph, params_k1, normalize=True)
    ec_k1 = EnergyComputer(graph, params_k1)
    ec_k1.normalize_weights()
    E_k1, terms_k1 = ec_k1.energy(result_k1.u)
    print(f"K=1: E = {E_k1:.6f}, terms={terms_k1}")
    print(f"     lambda_cl={ec_k1.lambda_cl:.6f}, lambda_sep={ec_k1.lambda_sep:.6f}, lambda_bd={ec_k1.lambda_bd:.6f}")

    # K=2 with CORRECT per-formation c
    params_k2 = ParameterRegistry(volume_fraction=c_half)
    valid, v, _ = params_k2.validate(fiedler_eigenvalue=graph.fiedler)
    if not valid:
        beta_crit = params_k2.beta_critical(graph.fiedler)
        params_k2 = ParameterRegistry(volume_fraction=c_half, beta_bd=max(beta_crit*2, 10))
        valid, v, _ = params_k2.validate(fiedler_eigenvalue=graph.fiedler)
        if not valid:
            print(f"K=2: CANNOT validate with c_half={c_half}: {v}")
            continue

    results_k2 = find_k_formations(
        graph, params_k2, K=2, lambda_rep=10.0,
        n_restarts=3, max_iter=2000,
    )

    ec_k2 = EnergyComputer(graph, params_k2)
    ec_k2.normalize_weights()
    E_k2_self = sum(ec_k2.energy(r.u)[0] for r in results_k2)
    E_k2_rep = 10.0 * float(np.sum(results_k2[0].u * results_k2[1].u))
    E_k2_total = E_k2_self + E_k2_rep

    print(f"K=2: E = {E_k2_total:.6f} (self={E_k2_self:.6f}, rep={E_k2_rep:.6f})")
    print(f"     lambda_cl={ec_k2.lambda_cl:.6f}, lambda_sep={ec_k2.lambda_sep:.6f}, lambda_bd={ec_k2.lambda_bd:.6f}")
    for i, r in enumerate(results_k2):
        E_i, t_i = ec_k2.energy(r.u)
        print(f"     Formation {i}: E={E_i:.6f}, diag={r.diagnostics}")

    print(f"\nΔE(K=2 - K=1) = {E_k2_total - E_k1:.6f}")
    print(f"  => {'K=2 PREFERRED' if E_k2_total < E_k1 else 'K=1 PREFERRED'}")

    # Also test: what if we DON'T normalize (raw weights)?
    ec_k1_raw = EnergyComputer(graph, params_k1)
    E_k1_raw = ec_k1_raw.energy(result_k1.u)[0]
    ec_k2_raw = EnergyComputer(graph, params_k2)
    E_k2_raw = sum(ec_k2_raw.energy(r.u)[0] for r in results_k2) + E_k2_rep
    print(f"\n  Raw weights: K=1={E_k1_raw:.6f}, K=2={E_k2_raw:.6f}, ΔE={E_k2_raw - E_k1_raw:.6f}")

    # CRITICAL: compare with SAME EnergyComputer (wrong normalization)
    E_k2_wrongnorm = sum(ec_k1.energy(r.u)[0] for r in results_k2) + E_k2_rep
    print(f"  K=2 with K=1's normalization: E={E_k2_wrongnorm:.6f}, ΔE={E_k2_wrongnorm - E_k1:.6f}")
