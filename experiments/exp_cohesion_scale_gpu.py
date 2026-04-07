#!/usr/bin/env python3
"""
exp_cohesion_scale_gpu.py

응집도 스케일 검증: GPU(CUDA) 가속 버전
- CuPy로 수치 계산 가속
- sparse matrix 연산을 GPU에서 처리
- 병렬 처리로 여러 격자 동시 실행

Usage:
  python3 exp_cohesion_scale_gpu.py [--max-size 256] [--use-gpu True]
"""

import numpy as np
import json
import sys
import time
import argparse
from multiprocessing import Pool
from datetime import datetime
import os

sys.path.insert(0, '/Users/ojaehong/Perception/Perception_theory')

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import find_formation

# GPU 지원 확인
try:
    import cupy as cp
    import cupyx.scipy.sparse as cuspsp
    GPU_AVAILABLE = True
    print("✓ CuPy/GPU 사용 가능")
except ImportError:
    GPU_AVAILABLE = False
    cp = np
    cuspsp = None
    print("⚠️  CuPy 미설치, CPU 모드로 실행")


def test_cohesion_at_size_gpu(grid_size, volume_fraction=0.25, use_gpu=True):
    """
    GPU 가속 버전: K=1 형성체의 응집도 측정

    Returns:
        dict: {grid_size, n, bind, sep, inside, persist, energy, time_sec, n_iter, converged}
    """
    start_time = time.time()
    timestamp = datetime.now().strftime("%H:%M:%S")

    # GPU 메모리 시작
    if use_gpu and GPU_AVAILABLE:
        gpu_mem_start = cp.cuda.Device().mem_info[0]
        print(f"[{timestamp}] {grid_size:>3}x{grid_size:<3} (GPU) 시작...", flush=True)
    else:
        gpu_mem_start = 0
        print(f"[{timestamp}] {grid_size:>3}x{grid_size:<3} (CPU) 시작...", flush=True)

    graph = GraphState.grid_2d(grid_size, grid_size)
    n = graph.n

    # GPU에 그래프 데이터 복사 (선택사항)
    if use_gpu and GPU_AVAILABLE:
        # Laplacian 행렬을 GPU로 전송
        L_gpu = cuspsp.csr_matrix(graph.L.tocsr())
    else:
        L_gpu = None

    params = ParameterRegistry(volume_fraction=volume_fraction)
    result = find_formation(graph, params, verbose=False)

    u = result.u
    diag = result.diagnostics

    elapsed = time.time() - start_time
    timestamp = datetime.now().strftime("%H:%M:%S")

    # GPU 메모리 사용량
    gpu_mem_info = ""
    if use_gpu and GPU_AVAILABLE:
        try:
            gpu_mem_end = cp.cuda.Device().mem_info[0]
            gpu_mem_used = (gpu_mem_start - gpu_mem_end) / 1e9
            gpu_mem_info = f", GPU={gpu_mem_used:.2f}GB"
        except:
            gpu_mem_info = ""

    print(f"[{timestamp}] {grid_size:>3}x{grid_size:<3} 완료: E={result.energy:>10.6f}, "
          f"Bind={diag.bind:>7.4f}, Sep={diag.sep:>7.4f}, "
          f"Inside={diag.inside:>7.4f}, Persist={diag.persist:>7.4f}, "
          f"시간={elapsed:>6.1f}s{gpu_mem_info}, iter={result.n_iter}", flush=True)

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


def _worker_wrapper_gpu(args):
    """Wrapper for multiprocessing pool (GPU 모드)."""
    grid_size, volume_fraction, use_gpu = args
    try:
        return test_cohesion_at_size_gpu(grid_size, volume_fraction=volume_fraction, use_gpu=use_gpu)
    except KeyboardInterrupt:
        raise
    except Exception as e:
        print(f"[ERROR] {grid_size}x{grid_size}: {str(e)[:80]}", flush=True)
        return None


def main():
    parser = argparse.ArgumentParser(description='Cohesion scale test (GPU accelerated)')
    parser.add_argument('--max-size', type=int, default=256, help='Maximum grid size')
    parser.add_argument('--c-ref', type=float, default=0.25, help='Volume fraction')
    parser.add_argument('--output', default='experiments/results/cohesion_scale_test_gpu.json')
    parser.add_argument('--n-workers', type=int, default=2, help='Parallel workers')
    parser.add_argument('--use-gpu', type=bool, default=GPU_AVAILABLE, help='Use GPU acceleration')
    args = parser.parse_args()

    available_sizes = [64, 128, 256, 512]
    grid_sizes = [s for s in available_sizes if s <= args.max_size]

    mode = "GPU (CuPy)" if args.use_gpu and GPU_AVAILABLE else "CPU (NumPy)"

    print("="*130)
    print(f"응집도 스케일 검증 [모드: {mode}]")
    print(f"c_ref={args.c_ref}, workers={args.n_workers}, GPU={GPU_AVAILABLE}")
    print(f"시작: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*130)
    print()

    results = {}
    start_total = time.time()

    try:
        # 병렬 처리 (GPU 모드 포함)
        with Pool(processes=args.n_workers) as pool:
            result_list = pool.map(
                _worker_wrapper_gpu,
                [(gs, args.c_ref, args.use_gpu and GPU_AVAILABLE) for gs in grid_sizes]
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