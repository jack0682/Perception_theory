"""G1 cluster analysis: R23 data-only verification of Theorem 1, σ-framework, NQ-136 predictions.

Uses stored exp_orbital_fullscale.json (eigenvalues + angular power per stable minimizer).
No re-computation of eigenvectors needed — purely post-analysis.

Addresses:
  NQ-128: λ_0/λ_1 ratio distribution → Theorem 1 (Mode 0 = Goldstone) verification
  NQ-129: Goldstone universal scaling λ_0 vs d_*
  NQ-137: Continuum vs finite-grid spectrum — compare Pöschl-Teller (NQ-136 Cat A)
  NQ-141: σ ↔ orbital taxonomy map via ℓ mod 4 → D_4 irrep (NQ-146 Cat A)

Run: cd CODE && python3 scripts/G1_analyze_R23.py
Output: scripts/results/G1_R23_analysis.json + console report.
"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np


R23_PATH = '/home/jack/Perception_theory/CODE/results/exp_orbital_fullscale.json'


def load_R23():
    with open(R23_PATH) as f:
        data = json.load(f)
    return data


def ell_mod4_to_irrep(ell):
    """NQ-146 Cat A: ℓ mod 4 → D_4 irrep decomposition."""
    m = ell % 4
    if ell == 0: return ('A_1',)
    if m == 0: return ('A_1', 'A_2')
    if m == 2: return ('B_1', 'B_2')
    return ('E',)  # m == 1 or 3


def dominant_ell(power_dict):
    """Return the ℓ with max power fraction."""
    if not power_dict:
        return None, 0.0
    items = [(int(k), v) for k, v in power_dict.items()]
    items.sort(key=lambda x: -x[1])
    return items[0]


def stable_clusters(data):
    """Filter to stable (Morse=0) clusters from cluster_summaries."""
    return [c for c in data['cluster_summaries'] if c.get('morse_index') == 0]


def analyze_NQ128(clusters, report):
    """λ_0/λ_1 ratio distribution per stable minimizer. Theorem 1: ratio << 1 for bulk-localized."""
    print("\n=== NQ-128: λ_0/λ_1 ratio distribution ===")
    ratios = []
    lambda_0s = []
    lambda_1s = []
    Fs = []
    for c in clusters:
        eigs = c['eigenvalues']
        if len(eigs) < 2:
            continue
        # eigenvalues sorted ascending; lambda_0 = eigs[0], lambda_1 = eigs[1]
        # But eigs[0] is near-zero (tangent direction) — exclude it. The lowest non-tangent is eigs[1].
        # Actually looking at data: eigs[0] ≈ 1e-6 = tangent. Mode 0 in Theorem 1 sense is eigs[1] (lowest physical).
        # So "Mode 0" (Goldstone?) = eigs[1], "Mode 1" (first orbital) = eigs[2].
        lam_0 = eigs[1]  # Goldstone candidate
        lam_1 = eigs[2] if len(eigs) > 2 else None
        if lam_1 is None or lam_1 < 1e-10:
            continue
        ratio = lam_0 / lam_1
        ratios.append(ratio)
        lambda_0s.append(lam_0)
        lambda_1s.append(lam_1)
        Fs.append(c['F_local_max'])

    ratios = np.array(ratios)
    lambda_0s = np.array(lambda_0s)
    lambda_1s = np.array(lambda_1s)
    Fs = np.array(Fs)
    print(f"  N stable clusters analyzed: {len(ratios)}")
    print(f"  λ_0 distribution: min={lambda_0s.min():.4f}, mean={lambda_0s.mean():.4f}, max={lambda_0s.max():.4f}")
    print(f"  λ_1 distribution: min={lambda_1s.min():.4f}, mean={lambda_1s.mean():.4f}, max={lambda_1s.max():.4f}")
    print(f"  λ_0/λ_1 ratio: min={ratios.min():.4f}, mean={ratios.mean():.4f}, max={ratios.max():.4f}, median={np.median(ratios):.4f}")
    # Distribution
    thresholds = [0.1, 0.3, 0.5, 1.0]
    for t in thresholds:
        f = (ratios < t).sum() / len(ratios)
        print(f"  fraction with ratio < {t}: {f:.2%}")

    # Correlation with F
    if len(np.unique(Fs)) > 1:
        corr = np.corrcoef(Fs, ratios)[0, 1]
        print(f"  Corr(F, ratio): {corr:.3f}")

    # Per-F analysis
    print("\n  Per-F statistics:")
    unique_Fs = sorted(np.unique(Fs))
    by_F = {}
    for F in unique_Fs[:10]:
        mask = Fs == F
        rs = ratios[mask]
        if len(rs) == 0:
            continue
        by_F[int(F)] = {'n': int(len(rs)), 'mean_ratio': float(rs.mean()),
                        'min_ratio': float(rs.min()), 'max_ratio': float(rs.max())}
        print(f"    F={F}: n={len(rs)}, ratio mean={rs.mean():.3f}, min={rs.min():.3f}")

    report['NQ128'] = {
        'n_clusters': len(ratios),
        'lambda_0_stats': {'min': float(lambda_0s.min()), 'mean': float(lambda_0s.mean()),
                           'max': float(lambda_0s.max()), 'median': float(np.median(lambda_0s))},
        'lambda_1_stats': {'min': float(lambda_1s.min()), 'mean': float(lambda_1s.mean()),
                           'max': float(lambda_1s.max())},
        'ratio_stats': {'min': float(ratios.min()), 'mean': float(ratios.mean()),
                        'max': float(ratios.max()), 'median': float(np.median(ratios))},
        'fraction_ratio_less_than': {str(t): float((ratios < t).sum() / len(ratios)) for t in thresholds},
        'by_F': by_F,
    }

    # Theorem 1 test:
    # - If most clusters have λ_0 << λ_1 (ratio < 0.1): strong evidence for Goldstone interpretation
    # - If ratio ≈ 1: Mode 0 and Mode 1 comparable, not Goldstone
    goldstone_evidence = float((ratios < 0.1).sum() / len(ratios))
    report['NQ128']['goldstone_evidence_fraction'] = goldstone_evidence
    if goldstone_evidence > 0.5:
        print(f"\n  ✓ GOLDSTONE SUPPORTED: {goldstone_evidence:.1%} of clusters have λ_0/λ_1 < 0.1")
    elif goldstone_evidence > 0.2:
        print(f"\n  ~ GOLDSTONE PARTIAL: {goldstone_evidence:.1%} of clusters consistent with Goldstone")
    else:
        print(f"\n  ✗ GOLDSTONE NOT DOMINANT: only {goldstone_evidence:.1%} have low ratio — Mode 0 genuinely orbital for most")


def analyze_NQ129(clusters, data, report):
    """Goldstone universal scaling: λ_0 vs d_*/xi_0."""
    print("\n=== NQ-129: Goldstone universal scaling ===")
    beta = data['config']['beta']
    alpha = data['config']['alpha']
    grid = data['config']['grid']
    L = grid[0]
    xi_0 = np.sqrt(alpha / beta)

    # For each cluster: compute d_* (distance of CoM to nearest boundary)
    d_stars = []
    lambda_0s = []
    for c in clusters:
        eigs = c['eigenvalues']
        if len(eigs) < 2:
            continue
        lam_0 = eigs[1]  # first non-tangent
        com = c.get('rep_center_of_mass', [L/2, L/2])
        # boundary distance: min(x, L-1-x, y, L-1-y)
        d = min(com[0], L - 1 - com[0], com[1], L - 1 - com[1])
        d_stars.append(d)
        lambda_0s.append(lam_0)

    d_stars = np.array(d_stars)
    lambda_0s = np.array(lambda_0s)

    # Theorem 1 prediction: λ_0 = C * exp(-d_*/xi_0)
    # So log(λ_0) = log(C) - d_*/xi_0
    # Test: log(λ_0) linear in d_*/xi_0?
    d_over_xi = d_stars / xi_0
    # Only use λ_0 > 0 for log
    mask = (lambda_0s > 1e-5) & (d_over_xi > 0)
    d_f = d_over_xi[mask]
    l_f = lambda_0s[mask]
    print(f"  xi_0 = sqrt(α/β) = {xi_0:.4f}")
    print(f"  N usable: {len(d_f)} / {len(d_over_xi)}")
    print(f"  d_* range: [{d_stars.min():.2f}, {d_stars.max():.2f}]")
    print(f"  d_*/xi_0 range: [{d_over_xi.min():.1f}, {d_over_xi.max():.1f}]")
    print(f"  λ_0 range: [{lambda_0s.min():.4f}, {lambda_0s.max():.4f}]")

    if len(d_f) > 3:
        # Fit log(λ_0) = a - b * d_*/xi_0
        log_l = np.log(l_f)
        slope, intercept = np.polyfit(d_f, log_l, 1)
        print(f"  Fit: log(λ_0) = {intercept:.3f} + ({slope:.4f}) * (d_*/xi_0)")
        # Theorem 1 predicts slope = -1 (exponential decay)
        # If slope ≈ 0: no scaling — Mode 0 is NOT Goldstone
        # If slope < -0.5: strong Goldstone evidence
        if slope < -0.1:
            print(f"  ✓ Negative slope consistent with Goldstone prediction λ_0 ~ exp(-d_*/xi_0)")
        else:
            print(f"  ~ Slope not clearly negative — Goldstone scaling not simple exponential")
        # Correlation
        corr = np.corrcoef(d_f, log_l)[0, 1]
        print(f"  Corr(d_*/xi_0, log λ_0): {corr:.3f}")
        report['NQ129'] = {
            'xi_0': float(xi_0),
            'n_usable': int(len(d_f)),
            'slope': float(slope),
            'intercept': float(intercept),
            'corr_d_over_xi_vs_log_lambda': float(corr),
            'goldstone_slope_consistent': bool(slope < -0.1),
        }
    else:
        report['NQ129'] = {'note': 'insufficient data'}


def analyze_NQ137(clusters, data, report):
    """Continuum vs finite-grid: Compare to Pöschl-Teller prediction (NQ-136 Cat A).
    Prediction: λ_0,ℓ = β + 4α(ℓ²-1/4)/r_0²
    """
    print("\n=== NQ-137: Continuum (Pöschl-Teller) vs finite-grid spectrum ===")
    beta = data['config']['beta']
    alpha = data['config']['alpha']
    c = data['config']['c']
    grid = data['config']['grid']
    L = grid[0]
    # m = c * n = 0.5 * 1024 = 512
    m = c * L * L
    r_0 = np.sqrt(m / np.pi)
    print(f"  r_0 = sqrt(m/π) = {r_0:.4f}")

    # Pöschl-Teller prediction per angular ℓ (from NQ-136 Cat A):
    # λ_0,ℓ = β + 4α(ℓ²-1/4)/r_0²
    # In R23 setup, the disk-like minimizers (low F) are the test case.
    # For bulk modes, we can compare the ℓ-th dominant mode's eigenvalue against prediction.

    print(f"  Pöschl-Teller predictions (β={beta}, α={alpha}, r_0={r_0:.2f}):")
    for ell in range(6):
        pred = beta + 4 * alpha * (ell**2 - 0.25) / r_0**2
        print(f"    ℓ={ell}: λ ≈ {pred:.4f}")

    # For each stable cluster, identify the mode with each dominant ℓ and compare eigenvalue
    # Collect predicted vs observed eigenvalues
    preds = []
    obs = []
    ells = []
    Fs = []

    for cluster in clusters:
        F = cluster['F_local_max']
        for mode in cluster['mode_labels']:
            # Find dominant ℓ for this mode
            power = mode.get('power', {})
            if not power:
                continue
            ell, p = dominant_ell(power)
            if p < 0.3:  # skip mixed modes
                continue
            eig = mode['eigenvalue']
            if eig < 1e-4:  # tangent direction
                continue
            pred = beta + 4 * alpha * (ell**2 - 0.25) / r_0**2
            preds.append(pred)
            obs.append(eig)
            ells.append(ell)
            Fs.append(F)

    preds = np.array(preds)
    obs = np.array(obs)
    ells = np.array(ells)
    Fs = np.array(Fs)
    print(f"  N mode-ell pairs: {len(obs)}")

    # Per ℓ comparison
    ell_stats = {}
    for ell in sorted(set(ells)):
        mask = ells == ell
        if mask.sum() == 0:
            continue
        obs_ell = obs[mask]
        pred_ell = preds[mask][0]  # same prediction for all
        print(f"  ℓ={ell}: n={mask.sum()}, obs range=[{obs_ell.min():.2f}, {obs_ell.max():.2f}], predicted={pred_ell:.2f}")
        ell_stats[int(ell)] = {
            'n': int(mask.sum()),
            'predicted': float(pred_ell),
            'obs_min': float(obs_ell.min()),
            'obs_mean': float(obs_ell.mean()),
            'obs_max': float(obs_ell.max()),
            'ratio_obs_over_pred': float(obs_ell.mean() / pred_ell),
        }

    # Correlation test
    if len(obs) > 3:
        corr = np.corrcoef(preds, obs)[0, 1]
        print(f"  Overall corr(predicted, observed): {corr:.3f}")
    else:
        corr = None

    report['NQ137'] = {
        'r_0': float(r_0),
        'predictions': {str(ell): float(beta + 4*alpha*(ell**2-0.25)/r_0**2) for ell in range(6)},
        'n_mode_ell_pairs': int(len(obs)),
        'ell_stats': ell_stats,
        'overall_corr': float(corr) if corr is not None else None,
    }


def analyze_NQ141(clusters, report):
    """σ ↔ orbital taxonomy map via ℓ → D_4 irrep (NQ-146 Cat A)."""
    print("\n=== NQ-141: σ ↔ orbital taxonomy map (via ℓ mod 4 → D_4 irrep) ===")

    label_to_irrep = {}  # orbital label (e.g. "p", "d", "g") → irrep set
    for cluster in clusters:
        F = cluster['F_local_max']
        for mode in cluster['mode_labels']:
            power = mode.get('power', {})
            label = mode.get('label', '')
            ell, p = dominant_ell(power)
            if p < 0.3:
                continue
            irreps = ell_mod4_to_irrep(ell)
            # Extract orbital letter from label "p(0.32)" → "p"
            letter = label.split('(')[0] if '(' in label else label
            if letter in ['s', 'p', 'd', 'f', 'g', 'h', 'i']:
                if letter not in label_to_irrep:
                    label_to_irrep[letter] = {'ells': [], 'irreps': set()}
                label_to_irrep[letter]['ells'].append(ell)
                label_to_irrep[letter]['irreps'].update(irreps)

    # Build taxonomy map
    letter_to_ell = {'s': 0, 'p': 1, 'd': 2, 'f': 3, 'g': 4, 'h': 5, 'i': 6}
    print(f"\n  Taxonomy map (letter → ℓ → D_4 irrep):")
    print(f"  {'Label':>6} {'ℓ':>3} {'ℓ mod 4':>8} {'D_4 irrep':>20} {'observations':>13}")
    taxonomy = {}
    for letter, expected_ell in letter_to_ell.items():
        expected_irreps = ell_mod4_to_irrep(expected_ell)
        observed = label_to_irrep.get(letter, {'ells': [], 'irreps': set()})
        n_obs = len(observed['ells'])
        taxonomy[letter] = {
            'expected_ell': expected_ell,
            'expected_irreps': list(expected_irreps),
            'observed_ells': observed['ells'],
            'observed_irreps': list(observed['irreps']),
            'n_observations': n_obs,
        }
        irrep_str = '+'.join(expected_irreps)
        print(f"  {letter:>6} {expected_ell:>3} {expected_ell % 4:>8} {irrep_str:>20} {n_obs:>13}")

    # Map table for Axiom S1'
    report['NQ141'] = {
        'taxonomy_map': taxonomy,
        'letter_to_ell': letter_to_ell,
    }


def main():
    print("=" * 70)
    print("G1 Cluster Analysis: R23 data-only verification")
    print("=" * 70)
    data = load_R23()
    print(f"Loaded R23: {R23_PATH}")
    print(f"Total clusters: {len(data['cluster_summaries'])}")
    clusters = stable_clusters(data)
    print(f"Stable clusters (Morse=0): {len(clusters)}")

    report = {
        'source': R23_PATH,
        'n_total_clusters': len(data['cluster_summaries']),
        'n_stable_clusters': len(clusters),
        'config': data['config'],
    }

    analyze_NQ128(clusters, report)
    analyze_NQ129(clusters, data, report)
    analyze_NQ137(clusters, data, report)
    analyze_NQ141(clusters, report)

    # Save
    out = os.path.join(os.path.dirname(__file__), 'results', 'G1_R23_analysis.json')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w') as f:
        json.dump(report, f, indent=2)
    print(f"\n\n=== ALL RESULTS SAVED: {out} ===")

    # Summary
    print("\n" + "=" * 70)
    print("G1 FINAL SUMMARY")
    print("=" * 70)
    nq128 = report.get('NQ128', {})
    print(f"NQ-128 (λ_0/λ_1 ratio): {nq128.get('ratio_stats', {}).get('median', 'NA')} median")
    gold = nq128.get('goldstone_evidence_fraction', 0)
    print(f"         Goldstone evidence (ratio<0.1): {gold:.1%}")

    nq129 = report.get('NQ129', {})
    if 'slope' in nq129:
        print(f"NQ-129 (Goldstone scaling): slope={nq129['slope']:.3f} {'✓ Goldstone' if nq129.get('goldstone_slope_consistent') else '✗ not clearly'}")

    nq137 = report.get('NQ137', {})
    if 'overall_corr' in nq137 and nq137['overall_corr'] is not None:
        print(f"NQ-137 (continuum vs finite): corr(pred, obs)={nq137['overall_corr']:.3f}")

    nq141 = report.get('NQ141', {})
    tax = nq141.get('taxonomy_map', {})
    letters_observed = sum(1 for l, info in tax.items() if info['n_observations'] > 0)
    print(f"NQ-141 (σ↔taxonomy): {letters_observed} orbital letters observed with irrep mapping")


if __name__ == "__main__":
    main()
