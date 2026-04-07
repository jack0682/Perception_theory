"""
exp_fiedler_analysis.py

Theory validation: Does Fiedler resonance persist to 1024×1024?
Analysis of H1/H2/H3 hypotheses using high-resolution Fiedler data.

Usage:
  python3 exp_fiedler_analysis.py < results/fiedler_higres_scan.json
"""

import json
import numpy as np
from scipy.optimize import curve_fit
import sys

def load_results(filepath):
    """Load fiedler_higres_scan.json results"""
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data

def extract_square_grids(data):
    """Extract only square grid results (for continuum limit analysis)"""
    square = data.get('square', {})

    # Sort by grid size
    grid_sizes = []
    n_vals = []
    lambda2_vals = []
    asym_vals = []

    for key in sorted(square.keys(), key=lambda x: int(x.split('x')[0])):
        val = square[key]
        gs = val['grid_size']
        n = val['n']
        l2 = val['lambda2']

        # Estimate asymmetry from Fiedler range
        v_range = val.get('fiedler_range', 0)
        skew = val.get('skewness', 0.5)
        asym = (skew - 0.5) * 2  # Normalize to [-1, 1]

        grid_sizes.append(gs)
        n_vals.append(n)
        lambda2_vals.append(l2)
        asym_vals.append(asym)

    return np.array(grid_sizes), np.array(n_vals), np.array(lambda2_vals), np.array(asym_vals)

def fit_power_law(n_vals, y_vals):
    """Fit y ~ A * n^α"""
    def power_law(n, A, alpha):
        return A * n**alpha

    try:
        popt, _ = curve_fit(power_law, n_vals, np.abs(y_vals), p0=[1, -1], maxfev=10000)
        return popt[0], popt[1]
    except:
        return None, None

def fit_exponential_decay(n_vals, y_vals):
    """Fit y ~ A * exp(-α * n)"""
    def exp_decay(n, A, alpha):
        return A * np.exp(-alpha * n)

    try:
        popt, _ = curve_fit(exp_decay, n_vals, np.abs(y_vals), p0=[1, 0.01], maxfev=10000)
        return popt[0], popt[1]
    except:
        return None, None

def analyze_hypotheses(grid_sizes, n_vals, lambda2_vals, asym_vals):
    """
    Test H1 (decay), H2 (persistent), H3 (convergence to Type A)
    """
    print("="*110)
    print("이론 검증: Fiedler 공진의 극한 행동")
    print("="*110)

    print(f"\n데이터 요약:")
    print(f"{'Grid':>12} {'n':>10} {'λ₂':>12} {'Asym':>12}")
    print("-"*110)
    for gs, n, l2, asym in zip(grid_sizes, n_vals, lambda2_vals, asym_vals):
        print(f"{gs:>3}x{gs:<3} {n:>10} {l2:>12.6f} {asym:>12.4f}")

    # Test H1: Decay to zero (λ₂ and asym both → 0)
    print(f"\n{'='*110}")
    print("H1: 유한격자 효과 (공진이 사라짐)")
    print(f"{'='*110}")

    A_l2, alpha_l2 = fit_power_law(n_vals, lambda2_vals)
    A_asym, alpha_asym = fit_power_law(n_vals, asym_vals)

    if A_l2 and A_asym:
        print(f"\nFiedler 고유값: λ₂ ~ {A_l2:.3e} * n^{alpha_l2:.3f}")
        print(f"비대칭성: asym ~ {A_asym:.3e} * n^{alpha_asym:.3f}")

        if alpha_l2 < -0.5 and alpha_asym < -0.5:
            print("✓ 강한 지지: 둘 다 빠르게 감소")
            return "H1"
        elif alpha_l2 > -0.2 and alpha_asym > -0.2:
            print("✗ 약한 지지: 감소가 느림")
        else:
            print("? 혼합적: 고유값은 감소하지만 비대칭성은 유지")

    # Test H2: Persistent oscillation (asym stays O(1), doesn't decay)
    print(f"\n{'='*110}")
    print("H2: 영구적 공진 (비대칭성 유지)")
    print(f"{'='*110}")

    asym_mean = np.mean(np.abs(asym_vals))
    asym_std = np.std(asym_vals)
    asym_range = np.max(asym_vals) - np.min(asym_vals)

    print(f"\n비대칭성 통계:")
    print(f"  평균 |asym|: {asym_mean:.4f}")
    print(f"  표준편차: {asym_std:.4f}")
    print(f"  범위: {asym_range:.4f}")

    if asym_mean > 0.1 and asym_std > 0.05:
        print("✓ 강한 지지: 비대칭성이 유지되고 진동")
        return "H2"
    elif asym_mean < 0.05:
        print("✗ 약한 지지: 비대칭성이 너무 작음")

    # Test H3: Convergence to Type A (asym → negative)
    print(f"\n{'='*110}")
    print("H3: Type A로 수렴 (음수 비대칭성)")
    print(f"{'='*110}")

    print(f"\n비대칭성 추세:")
    for i, (gs, asym) in enumerate(zip(grid_sizes, asym_vals)):
        sign = '+' if asym > 0 else '-'
        trend = "↓" if i > 0 and asym_vals[i] < asym_vals[i-1] else "↑" if i > 0 else "·"
        print(f"  {gs:>4}x{gs:<4}: {sign}{abs(asym):>6.4f} {trend}")

    # Check if converging to negative
    if all(a < 0 for a in asym_vals[-2:]):
        print("\n✓ 강한 지지: 큰 격자에서 음수로 수렴")
        # Estimate convergence limit
        converge_limit = np.mean(asym_vals[-2:])
        print(f"  수렴값 추정: {converge_limit:.4f}")
        return "H3"
    elif all(a > 0 for a in asym_vals[-2:]):
        print("\n✗ 약한 지지: 양수로 유지")
    else:
        print("\n? 불명확: 부호가 진동")

    return None

def plot_results(grid_sizes, n_vals, lambda2_vals, asym_vals):
    """Generate analysis plots (text-based)"""

    print(f"\n{'='*110}")
    print("시각화: 로그 스케일에서의 추세")
    print(f"{'='*110}")

    log_n = np.log10(n_vals)

    print(f"\nλ₂ vs log₁₀(n):")
    print(f"{'log₁₀(n)':>12} {'λ₂':>12} {'그래프':>80}")
    for ln, l2 in zip(log_n, lambda2_vals):
        bar = '█' * max(1, int(l2 * 100))
        print(f"{ln:>12.2f} {l2:>12.6f} {bar}")

    print(f"\n|Asym| vs log₁₀(n):")
    print(f"{'log₁₀(n)':>12} {'|Asym|':>12} {'그래프':>80}")
    for ln, asym in zip(log_n, asym_vals):
        bar = '█' * max(1, int(np.abs(asym) * 30))
        print(f"{ln:>12.2f} {np.abs(asym):>12.4f} {bar}")

def main(filepath):
    """Main analysis"""

    # Load results
    data = load_results(filepath)

    # Extract square grids
    grid_sizes, n_vals, lambda2_vals, asym_vals = extract_square_grids(data)

    # Analyze hypotheses
    winner = analyze_hypotheses(grid_sizes, n_vals, lambda2_vals, asym_vals)

    # Plot trends
    plot_results(grid_sizes, n_vals, lambda2_vals, asym_vals)

    # Conclusion
    print(f"\n{'='*110}")
    print("결론")
    print(f"{'='*110}")

    if winner == "H1":
        print("""
✓ 지지됨: H1 (유한격자 효과)

해석:
  - Fiedler 공진은 유한 격자의 이산화 산물
  - 격자가 커질수록 대칭성으로 수렴
  - 극한: 연속 도메인에서는 공진 없음

응용 의미:
  - 고해상도 (>512×512)에서는 K=2 항상 중심형
  - 비대칭성은 무시 가능한 효과
        """)

    elif winner == "H2":
        print("""
✓ 지지됨: H2 (영구적 공진)

해석:
  - Fiedler 공진은 기본적 특성
  - 격자 기하학이 영구적으로 형성체 배치를 결정
  - 연속 극한에서도 비대칭성 유지

응용 의미:
  - 고해상도에서도 Type B (비대칭형) 가능
  - 형성체 위치는 Fiedler 벡터 의존
  - 영상 응용시 위치 선호도 고려
        """)

    elif winner == "H3":
        print("""
✓ 지지됨: H3 (Type A 수렴)

해석:
  - 큰 격자는 항상 중심형 K=2 선호
  - 진동은 감소, 음수 비대칭성으로 안정화
  - 충분히 큰 n에서는 Type A 유일

응용 의미:
  - 1024×1024 이상: 안정적, 중심형 K=2
  - 공진 효과는 소규모 격자에만 제한
  - HD 이미지 응용 안전
        """)
    else:
        print("""
결론 미확정: 더 많은 데이터 필요
또는 중간 상황 (H1과 H3 혼합)
        """)

if __name__ == '__main__':
    filepath = '/Users/ojaehong/Perception/Perception_theory/experiments/results/fiedler_higres_scan.json'
    main(filepath)
