#!/usr/bin/env python3
"""
exp_cohesion_scale.py

응집도 스케일 검증: 격자 크기에 따라 응집 강도가 유지되는가?

Usage:
  python3 exp_cohesion_scale.py [--max-size 256] [--n-workers 4]
"""

import numpy as np
import json
import sys
import time
import argparse
from multiprocessing import Pool
from datetime import datetime
import os
from pathlib import Path

# 프로젝트 루트 동적 설정 (experiments 폴더 기준)
REPO_ROOT = Path(__file__).resolve().parent.parent
# PYTHONPATH에 추가
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation

def test_cohesion_at_size(grid_size, volume_fraction=0.25):
    """
    Single grid size에서 K=1 형성체의 응집도 측정

    Returns:
        dict: {n, bind, sep, inside, persist, u_max, u_mean, u_std, energy, time_sec}
    """
    start_time = time.time()
    timestamp = datetime.now().strftime("%H:%M:%S")

    graph = GraphState.grid_2d(grid_size, grid_size)
    n = graph.n

    print(f"[{timestamp}] {grid_size:>3}x{grid_size:<3} (n={n:>6}) 시작...", flush=True)

    params = ParameterRegistry(volume_fraction=volume_fraction)
    result = find_formation(graph, params, verbose=False)

    u = result.u
    diag = result.diagnostics

    elapsed = time.time() - start_time
    timestamp = datetime.now().strftime("%H:%M:%S")

    print(f"[{timestamp}] {grid_size:>3}x{grid_size:<3} 완료: E={result.energy:>10.6f}, "
          f"Bind={diag.bind:>7.4f}, Sep={diag.sep:>7.4f}, "
          f"Inside={diag.inside:>7.4f}, Persist={diag.persist:>7.4f}, "
          f"시간={elapsed:>6.1f}s, iter={result.n_iter}", flush=True)

    return {
        'grid_size': grid_size,
        'n': n,
        'volume_fraction': volume_fraction,
        'bind': float(diag.bind),
        'sep': float(diag.sep),
        'inside': float(diag.inside),
        'persist': float(diag.persist),
        'u_max': float(np.max(u)),
        'u_min': float(np.min(u)),
        'u_mean': float(np.mean(u)),
        'u_std': float(np.std(u)),
        'energy': float(result.energy),
        'time_sec': elapsed,
        'n_iter': result.n_iter,
        'converged': result.converged
    }

def _worker_wrapper(grid_size, volume_fraction):
    """Wrapper for multiprocessing pool."""
    try:
        return test_cohesion_at_size(grid_size, volume_fraction=volume_fraction)
    except KeyboardInterrupt:
        raise
    except Exception as e:
        print(f"[ERROR] {grid_size}x{grid_size}: {str(e)[:80]}", flush=True)
        return None


def main():
    parser = argparse.ArgumentParser(description='Cohesion scale test')
    parser.add_argument('--max-size', type=int, default=256, help='Maximum grid size (64, 128, 256, 512)')
    parser.add_argument('--c-ref', type=float, default=0.25, help='Volume fraction')
    parser.add_argument('--output', default='experiments/results/cohesion_scale_test.json')
    parser.add_argument('--n-workers', type=int, default=4, help='Number of parallel workers')
    args = parser.parse_args()

    # 격자 크기 선택
    available_sizes = [64]
    grid_sizes = [s for s in available_sizes if s <= args.max_size]

    print("="*130)
    mode = "CPU"
    print(f"응집도 스케일 검증 (c_ref={args.c_ref}, workers={args.n_workers}, mode={mode})")
    print(f"시작: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*130)
    print()

    results = {}
    start_total = time.time()

    try:
        # 병렬 처리
        with Pool(processes=args.n_workers) as pool:
            result_list = pool.starmap(
                _worker_wrapper,
                [(gs, args.c_ref) for gs in grid_sizes]
            )

        # 결과 수집
        for result in result_list:
            if result is not None:
                key = f'{result["grid_size"]}x{result["grid_size"]}'
                results[key] = result

    except KeyboardInterrupt:
        print(f"\n\n중단됨 (by user)")
        print("="*130)
        return

    # 저장
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, 'w') as f:
        json.dump(results, f, indent=2)

    elapsed_total = time.time() - start_total
    print(f"\n✓ 저장: {args.output}")
    print(f"총 실행 시간: {elapsed_total:.1f}s")
    print()

    # 분석
    print(f"{'='*130}")
    print("분석")
    print(f"{'='*130}\n")

    if len(results) < 1:
        print("결과 없음.")
        return

    sorted_keys = sorted(results.keys())
    bind_vals = [results[k]['bind'] for k in sorted_keys]
    sep_vals = [results[k]['sep'] for k in sorted_keys]
    time_vals = [results[k]['time_sec'] for k in sorted_keys]

    print(f"{'Grid':>10} {'Bind':>10} {'Sep':>10} {'Inside':>10} {'Persist':>10} {'Energy':>12} {'Time(s)':>10} {'Iter':>8}")
    print("-"*130)
    for k in sorted_keys:
        r = results[k]
        print(f"{k:>10} {r['bind']:>10.4f} {r['sep']:>10.4f} {r['inside']:>10.4f} {r['persist']:>10.4f} "
              f"{r['energy']:>12.6f} {r['time_sec']:>10.1f} {r['n_iter']:>8d}")

    # 통계
    print(f"\n{'─'*130}")
    print("통계:")
    print(f"  Bind:  min={min(bind_vals):.4f}, max={max(bind_vals):.4f}, "
          f"mean={np.mean(bind_vals):.4f}, std={np.std(bind_vals):.4f}")
    print(f"  Sep:   min={min(sep_vals):.4f}, max={max(sep_vals):.4f}, "
          f"mean={np.mean(sep_vals):.4f}, std={np.std(sep_vals):.4f}")
    print(f"  Time:  total={sum(time_vals):.1f}s, mean={np.mean(time_vals):.1f}s/grid")

    bind_change = (bind_vals[-1] - bind_vals[0]) / bind_vals[0] * 100 if bind_vals[0] != 0 else 0
    sep_change = (sep_vals[-1] - sep_vals[0]) / sep_vals[0] * 100 if sep_vals[0] != 0 else 0

    # 결론
    print(f"\n{'─'*130}")
    print("결론:")

    if min(bind_vals) > 0.5:
        print(f"  ✓ 강한 응집: 모든 격자에서 Bind > 0.5")
    elif min(bind_vals) > 0.3:
        print(f"  △ 중간 응집: 모든 격자에서 0.3 < Bind < 0.5")
    else:
        print(f"  ✗ 약한 응집: Bind < 0.3 (최소값={min(bind_vals):.4f})")

    if abs(bind_change) < 10:
        print(f"  ✓ 안정적: Bind 변화 {bind_change:+.1f}% (< 10%)")
    else:
        print(f"  △ 변동: Bind 변화 {bind_change:+.1f}%")

    if all(sep < 0.5 for sep in sep_vals):
        print(f"  ✓ 분리 안정: 모든 격자에서 Sep < 0.5")
    else:
        print(f"  △ 분리 증가: 일부 격자에서 Sep > 0.5")

    print(f"\n{'='*130}\n")

if __name__ == '__main__':
    main()
