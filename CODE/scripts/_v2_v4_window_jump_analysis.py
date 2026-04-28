"""
_v2_v4_window_jump_analysis.py — V2 α-window standardization + V4 K-jump statistics

Phase 10 V2+V4: Re-analyze Phase 8 T1 + T2 + Phase 9 U1 + U2 data with:
- V2: standardized α-window [t_first_merger, t_K=2_last] only.
- V4: K-jump events statistics (inter-jump intervals, ΔK).
"""
import json
import os
import numpy as np


def load(name):
    path = f"/home/jack/Perception_theory/CODE/scripts/results/{name}.json"
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return json.load(f)


def detect_K_jumps(log, K_init):
    """Detect time points where K_active drops."""
    jumps = []
    K_prev = K_init
    for d in log:
        if d['K_active'] < K_prev:
            jumps.append({
                't': d['t'],
                'K_before': K_prev,
                'K_after': d['K_active'],
                'delta_K': K_prev - d['K_active'],
                'R_at_jump': d.get('R_avg'),
            })
        K_prev = d['K_active']
    return jumps


def fit_alpha_in_window(log, t_start, t_end, K_min_active=2):
    """Fit α in time window where K_active >= K_min_active and t in [t_start, t_end]."""
    ts = []; Rs = []
    for d in log:
        if t_start <= d['t'] <= t_end and d['R_avg'] > 0.3 and d['K_active'] >= K_min_active:
            ts.append(d['t'])
            Rs.append(d['R_avg'])
    if len(ts) > 5:
        coeffs = np.polyfit(np.log(ts), np.log(Rs), 1)
        return float(coeffs[0]), len(ts)
    return None, len(ts)


def standardize_window_analysis(log, K_init):
    """V2: standardized α-window [t_first_merger, t_last_K_2_active]."""
    jumps = detect_K_jumps(log, K_init)
    if not jumps:
        return {'alpha': None, 't_window': None, 'note': 'no merger detected'}
    t_first_merger = jumps[0]['t']
    # t_last where K_active >= 2
    t_last_K2 = None
    for d in reversed(log):
        if d['K_active'] >= 2:
            t_last_K2 = d['t']
            break
    if t_last_K2 is None or t_last_K2 <= t_first_merger:
        return {'alpha': None, 't_window': None, 'note': 'no valid window'}
    alpha, n_pts = fit_alpha_in_window(log, t_first_merger, t_last_K2)
    return {
        'alpha': alpha,
        't_window': (t_first_merger, t_last_K2),
        'n_pts': n_pts,
        'jumps': jumps,
    }


def main():
    print("=== V2: α-window standardization re-analysis ===\n")

    # Phase 8 T1 (K∈{5,10,15,20}, L=30)
    print("--- Phase 8 T1 (K=5,10,15,20 on L=30) ---")
    d = load("t1_higher_K_LSW")
    if d is None:
        print("T1 data not found; using Phase 9 U1 instead")
    else:
        for K in [5, 10, 15, 20]:
            seed_alphas = []
            for seed in [0, 1, 2]:
                key = f"K={K}_seed={seed}"
                if key in d['logs']:
                    log = d['logs'][key]
                    res = standardize_window_analysis(log, K)
                    if res['alpha'] is not None:
                        seed_alphas.append(res['alpha'])
            if seed_alphas:
                avg_alpha = np.mean(seed_alphas)
                print(f"  K={K}: standardized α = {avg_alpha:.3f} (mean of {len(seed_alphas)} seeds)")

    # Phase 9 U1 (K∈{5,10,15,20,30,40}, L=40)
    print("\n--- Phase 9 U1 (K=5..40 on L=40) ---")
    d = load("u1_K_infinity")
    if d:
        for K in [5, 10, 15, 20, 30, 40]:
            seed_alphas = []
            for seed in [0, 1, 2]:
                key = f"K={K}_seed={seed}"
                if key in d['logs']:
                    log = d['logs'][key]
                    res = standardize_window_analysis(log, K)
                    if res['alpha'] is not None:
                        seed_alphas.append(res['alpha'])
            if seed_alphas:
                avg_alpha = np.mean(seed_alphas)
                orig_alpha = d['fit_alpha_per_K'].get(str(K))
                orig_str = f"{orig_alpha:.3f}" if orig_alpha else "N/A"
                print(f"  K={K}: standardized α = {avg_alpha:.3f}, original = {orig_str}")

    # Phase 9 U2 (K=10, t_max=1000)
    print("\n--- Phase 9 U2 (K=10, t_max=1000) ---")
    d = load("u2_long_time")
    if d:
        log = d['log']
        K_init = 10
        res = standardize_window_analysis(log, K_init)
        print(f"  Standardized α (K=10, t∈[{res['t_window'][0]:.1f}, {res['t_window'][1]:.1f}]) = {res['alpha']:.3f}")
        print(f"  K-jumps detected: {len(res['jumps'])}")
        for j in res['jumps']:
            print(f"    t={j['t']:.2f}: K {j['K_before']}→{j['K_after']} (ΔK={j['delta_K']})")

    # V4: K-jump statistics from U2
    print("\n=== V4: K-jump statistics (U2 long-time K=10) ===\n")
    if d:
        log = d['log']
        jumps = detect_K_jumps(log, 10)
        print(f"Total K-jumps: {len(jumps)}")
        if len(jumps) > 1:
            inter_intervals = [jumps[i+1]['t'] - jumps[i]['t'] for i in range(len(jumps)-1)]
            print(f"Inter-jump intervals: {[round(x, 2) for x in inter_intervals]}")
            print(f"  Mean: {np.mean(inter_intervals):.2f}, Std: {np.std(inter_intervals):.2f}")
            print(f"  Min: {min(inter_intervals):.2f}, Max: {max(inter_intervals):.2f}")
            # Check if inter-intervals INCREASE (LSW: t_n+1 - t_n ~ t_n^q)
            ts_jumps = [j['t'] for j in jumps]
            if len(ts_jumps) > 3:
                # Fit log(interval) ~ log(t)
                inters = np.array(inter_intervals)
                ts_avg = np.array([(jumps[i]['t'] + jumps[i+1]['t'])/2 for i in range(len(jumps)-1)])
                mask = (inters > 0) & (ts_avg > 0)
                if mask.sum() >= 3:
                    p_inter = np.polyfit(np.log(ts_avg[mask]), np.log(inters[mask]), 1)
                    print(f"  Inter-interval scaling: dt ∝ t^{p_inter[0]:.3f}")

        delta_Ks = [j['delta_K'] for j in jumps]
        print(f"ΔK distribution: {sorted(delta_Ks)}")
        print(f"  Mean ΔK: {np.mean(delta_Ks):.2f}, single-jump fraction: {delta_Ks.count(1)/len(delta_Ks):.2%}")

    # Save results
    out = {
        'meta': {'description': 'V2 α-window + V4 K-jump statistics from cumulative data'},
    }
    out_path = "/home/jack/Perception_theory/CODE/scripts/results/v2_v4_analysis.json"
    with open(out_path, 'w') as f:
        json.dump(out, f, indent=2)
    print(f"\nWrote {out_path}")


if __name__ == '__main__':
    main()
