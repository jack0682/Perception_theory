"""Compute the CORRECT M₂ energy landscape for 15×15 grid.

Key insight: EnergyComputer.normalize_weights() uses params.volume_fraction
as the Hessian linearization point. To get correct E*(m), we must set
volume_fraction = m/n for each mass m.

Computes:
1. E*(m) = min_{u∈Σ_m} E_self(u) for m = 10, 20, 30, 40, 50, 60
2. E*''(M/2) to determine F'' sign
3. K=2 vs K=1 comparison with correct parameters
"""

import numpy as np
import sys
sys.path.insert(0, '/home/jack/ex')

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation
from scc.energy import EnergyComputer, double_well_second_deriv
from scc.multi import find_k_formations, _total_energy

# Setup
n_side = 15
graph = GraphState.grid_2d(n_side, n_side)
n = graph.n  # 225
print(f"Grid: {n_side}x{n_side}, n={n}")
print(f"Fiedler eigenvalue: {graph.fiedler:.6f}")

# Spinodal bounds
import math
c_lo = (3 - math.sqrt(3)) / 6
c_hi = (3 + math.sqrt(3)) / 6
print(f"Spinodal range: ({c_lo:.4f}, {c_hi:.4f})")
print(f"  => mass range: ({c_lo*n:.1f}, {c_hi*n:.1f})")

# ============================================================
# Part 1: E*(m) landscape
# ============================================================
print("\n" + "="*60)
print("PART 1: E*(m) — optimized self-energy at each mass")
print("="*60)

masses = [10, 20, 30, 40, 50, 60]
results = {}

for m in masses:
    c = m / n
    print(f"\n--- m={m}, c={c:.4f} ---")

    # Check spinodal
    if c <= c_lo or c >= c_hi:
        print(f"  OUTSIDE spinodal! Skipping.")
        continue

    params = ParameterRegistry(volume_fraction=c)

    # Validate
    valid, violations, warnings = params.validate(fiedler_eigenvalue=graph.fiedler)
    if not valid:
        print(f"  Validation FAILED: {violations}")
        # Try with higher beta
        beta_crit = params.beta_critical(graph.fiedler)
        print(f"  beta_crit={beta_crit:.4f}, trying beta_bd={beta_crit*2:.1f}")
        params = ParameterRegistry(volume_fraction=c, beta_bd=max(beta_crit * 2, 10.0))
        valid, violations, warnings = params.validate(fiedler_eigenvalue=graph.fiedler)
        if not valid:
            print(f"  Still failed: {violations}")
            continue

    result = find_formation(graph, params, normalize=True, verbose=False)

    # Also compute with raw (unnormalized) weights for comparison
    result_raw = find_formation(graph, params, normalize=False, verbose=False)

    # Record E_self components
    ec = EnergyComputer(graph, params)
    ec.normalize_weights()
    E_norm, terms_norm = ec.energy(result.u)

    ec_raw = EnergyComputer(graph, params)
    E_raw, terms_raw = ec_raw.energy(result_raw.u)

    results[m] = {
        'c': c,
        'E_normalized': E_norm,
        'E_raw': E_raw,
        'terms_norm': terms_norm,
        'terms_raw': terms_raw,
        'converged': result.converged,
        'converged_raw': result_raw.converged,
        'diagnostics': result.diagnostics,
        'u': result.u,
        'params': params,
    }

    print(f"  E*(normalized) = {E_norm:.6f}")
    print(f"  E*(raw weights) = {E_raw:.6f}")
    print(f"  Terms(norm): {terms_norm}")
    print(f"  Converged: norm={result.converged}, raw={result_raw.converged}")
    print(f"  Diagnostics: {result.diagnostics}")

# ============================================================
# Part 2: E*''(M/2) — curvature at half-mass
# ============================================================
print("\n" + "="*60)
print("PART 2: E*''(M/2) — second derivative of E*(m)")
print("="*60)

# Use finite differences on the E*(m) curve
m_vals = sorted(results.keys())
E_vals = [results[m]['E_normalized'] for m in m_vals]
E_raw_vals = [results[m]['E_raw'] for m in m_vals]

print("\nE*(m) table (normalized weights):")
for m, E in zip(m_vals, E_vals):
    print(f"  m={m:3d}  c={m/n:.4f}  E*={E:.6f}")

print("\nE*(m) table (raw weights):")
for m, E in zip(m_vals, E_raw_vals):
    print(f"  m={m:3d}  c={m/n:.4f}  E*={E:.6f}")

# Compute second derivative by FD at closest available mass to n/2=112.5
# We need denser sampling near M/2
print("\n--- Dense sampling near M/2 for curvature ---")
M_half = n / 2  # 112.5
dense_masses = [50, 55, 60, 65, 70, 75]  # around M/2... but spinodal limits
# Actually M/2 = 112.5, c = 0.5 which is in spinodal. Let's sample there.
dense_masses = [95, 100, 105, 110, 115, 120, 125, 130]
dense_results = {}

for m in dense_masses:
    c = m / n
    if c <= c_lo or c >= c_hi:
        print(f"  m={m}, c={c:.4f} — outside spinodal, skip")
        continue

    params = ParameterRegistry(volume_fraction=c)
    valid, violations, _ = params.validate(fiedler_eigenvalue=graph.fiedler)
    if not valid:
        beta_crit = params.beta_critical(graph.fiedler)
        params = ParameterRegistry(volume_fraction=c, beta_bd=max(beta_crit * 2, 10.0))
        valid, violations, _ = params.validate(fiedler_eigenvalue=graph.fiedler)
        if not valid:
            print(f"  m={m} — validation failed even with higher beta")
            continue

    result = find_formation(graph, params, normalize=True, verbose=False)
    ec = EnergyComputer(graph, params)
    ec.normalize_weights()
    E_norm, terms = ec.energy(result.u)
    dense_results[m] = E_norm
    print(f"  m={m:3d}, c={c:.4f}, E*={E_norm:.6f}")

# FD second derivative
if len(dense_results) >= 3:
    dm = sorted(dense_results.keys())
    Em = [dense_results[m] for m in dm]

    # Find closest triplet to M/2
    best_idx = min(range(1, len(dm)-1), key=lambda i: abs(dm[i] - M_half))
    h1 = dm[best_idx] - dm[best_idx-1]
    h2 = dm[best_idx+1] - dm[best_idx]
    E_pp = 2 * (Em[best_idx+1]/(h2*(h1+h2)) - Em[best_idx]/(h1*h2) + Em[best_idx-1]/(h1*(h1+h2)))

    print(f"\nE*''(m≈{dm[best_idx]}) ≈ {E_pp:.8f}")
    print(f"  Using m = {dm[best_idx-1]}, {dm[best_idx]}, {dm[best_idx+1]}")
    print(f"  F''(M/2) sign: {'POSITIVE (convex → K=1 preferred)' if E_pp > 0 else 'NEGATIVE (concave → K=2 preferred)'}")

# ============================================================
# Part 3: K=2 vs K=1 comparison with CORRECT parameters
# ============================================================
print("\n" + "="*60)
print("PART 3: K=2 vs K=1 with correct volume_fraction per formation")
print("="*60)

total_m = 67.5  # 0.3 * 225
total_c = total_m / n  # 0.3

print(f"\nTotal mass M = {total_m}, total c = {total_c}")

# K=1: single formation with all mass
print("\n--- K=1: single formation, m=M ---")
params_k1 = ParameterRegistry(volume_fraction=total_c)
result_k1 = find_formation(graph, params_k1, normalize=True, verbose=False)
ec_k1 = EnergyComputer(graph, params_k1)
ec_k1.normalize_weights()
E_k1, terms_k1 = ec_k1.energy(result_k1.u)
print(f"  E_single(m={total_m}) = {E_k1:.6f}")
print(f"  Terms: {terms_k1}")
print(f"  Converged: {result_k1.converged}")

# K=2: equal split, m₁=m₂=M/2
print("\n--- K=2 equal split: m₁=m₂=M/2 ---")
c_half = (total_m / 2) / n
params_k2 = ParameterRegistry(volume_fraction=c_half)

# Validate
valid, violations, _ = params_k2.validate(fiedler_eigenvalue=graph.fiedler)
if not valid:
    beta_crit = params_k2.beta_critical(graph.fiedler)
    params_k2 = ParameterRegistry(volume_fraction=c_half, beta_bd=max(beta_crit * 2, 10.0))

results_k2 = find_k_formations(
    graph, params_k2, K=2, lambda_rep=10.0,
    n_restarts=3, max_iter=2000, verbose=False,
)

# Compute total energy with correct EnergyComputer
ec_k2 = EnergyComputer(graph, params_k2)
ec_k2.normalize_weights()
E_k2_self = sum(ec_k2.energy(r.u)[0] for r in results_k2)
E_k2_rep = 10.0 * float(np.sum(results_k2[0].u * results_k2[1].u))
E_k2_total = E_k2_self + E_k2_rep

print(f"  c_per_formation = {c_half:.4f}")
print(f"  E_self total = {E_k2_self:.6f}")
print(f"  E_repulsion = {E_k2_rep:.6f}")
print(f"  E_K=2 total = {E_k2_total:.6f}")
for i, r in enumerate(results_k2):
    E_i, terms_i = ec_k2.energy(r.u)
    print(f"  Formation {i}: E={E_i:.6f}, diag={r.diagnostics}")

# K=2: asymmetric split (K=1 limit)
print("\n--- K=2 asymmetric (K=1 limit): m₁=M-1, m₂=1 ---")
m_big = total_m - 1
m_small = 1
c_big = m_big / n
c_small = m_small / n

print(f"  c_big={c_big:.4f}, c_small={c_small:.6f}")
print(f"  c_small in spinodal? {c_lo < c_small < c_hi}")

# For the asymmetric case, we can't use find_k_formations directly
# because c_small is outside spinodal. Instead compute E_self(m_big) + E_self(m_small)
if c_lo < c_big < c_hi:
    params_big = ParameterRegistry(volume_fraction=c_big)
    valid_big, _, _ = params_big.validate(fiedler_eigenvalue=graph.fiedler)
    if not valid_big:
        beta_crit = params_big.beta_critical(graph.fiedler)
        params_big = ParameterRegistry(volume_fraction=c_big, beta_bd=max(beta_crit * 2, 10.0))
    result_big = find_formation(graph, params_big, normalize=True)
    ec_big = EnergyComputer(graph, params_big)
    ec_big.normalize_weights()
    E_big, _ = ec_big.energy(result_big.u)
    print(f"  E*(m_big={m_big:.1f}) = {E_big:.6f}")
else:
    print(f"  c_big outside spinodal!")
    E_big = float('inf')

# For small mass: uniform field at c_small is the minimizer (no phase separation)
u_small = np.full(n, c_small)
# Use big-formation params for energy eval (small field is ~uniform)
params_small_eval = ParameterRegistry(volume_fraction=c_big)  # won't matter for raw energy
ec_small = EnergyComputer(graph, params_small_eval)
E_small_raw, terms_small = ec_small.energy(u_small)
print(f"  E_raw(uniform at c_small) = {E_small_raw:.6f}")
print(f"  Terms: {terms_small}")

E_asymm = E_big + E_small_raw  # No repulsion since fields don't overlap
print(f"  E_asymmetric total ≈ {E_asymm:.6f}")

# ============================================================
# Summary
# ============================================================
print("\n" + "="*60)
print("SUMMARY")
print("="*60)
print(f"\nE*(m) landscape (normalized):")
all_m = sorted(set(list(results.keys()) + list(dense_results.keys())))
for m in all_m:
    if m in results:
        print(f"  m={m:3d}  c={m/n:.4f}  E*={results[m]['E_normalized']:.6f}")
    elif m in dense_results:
        print(f"  m={m:3d}  c={m/n:.4f}  E*={dense_results[m]:.6f}")

print(f"\nK=1 (single, m={total_m}):  E = {E_k1:.6f}")
print(f"K=2 (equal, m₁=m₂={total_m/2}): E = {E_k2_total:.6f}  (self={E_k2_self:.6f} + rep={E_k2_rep:.6f})")
print(f"K=2 (asymm, m₁={m_big:.0f}, m₂={m_small}): E ≈ {E_asymm:.6f}")

print(f"\nK=2 equal vs K=1: ΔE = {E_k2_total - E_k1:.6f}")
if E_k2_total < E_k1:
    print("  => K=2 PREFERRED (splitting reduces energy)")
else:
    print("  => K=1 PREFERRED (splitting increases energy)")

# Check: does normalize_weights matter?
print("\n--- Normalization sensitivity check ---")
# Recompute K=1 without normalization
result_k1_raw = find_formation(graph, ParameterRegistry(volume_fraction=total_c), normalize=False)
ec_raw = EnergyComputer(graph, ParameterRegistry(volume_fraction=total_c))
E_k1_raw, _ = ec_raw.energy(result_k1_raw.u)
print(f"  K=1 raw weights: E = {E_k1_raw:.6f}")
print(f"  K=1 normalized:  E = {E_k1:.6f}")

# Check what happens if we use WRONG c for normalization
params_wrong = ParameterRegistry(volume_fraction=total_c)  # c=0.3 for all
ec_wrong = EnergyComputer(graph, params_wrong)
ec_wrong.normalize_weights()  # normalized at c=0.3
# Evaluate the K=2 equal-split formations with wrong normalization
E_wrong = sum(ec_wrong.energy(r.u)[0] for r in results_k2) + E_k2_rep
print(f"\n  K=2 with WRONG normalization (c=0.3 for half-mass fields): E = {E_wrong:.6f}")
print(f"  K=2 with CORRECT normalization (c=0.15):                    E = {E_k2_total:.6f}")
print(f"  Difference: {abs(E_wrong - E_k2_total):.6f}")
