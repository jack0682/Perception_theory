"""Run all stereo-SCC experiments (exp01–exp05) and print a summary table.

Usage (from CODE/):
    python stereo_scc/run_all_experiments.py
"""
from __future__ import annotations

import sys
import os
import time
import traceback

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

EXPERIMENTS = [
    ("exp01", "stereo_scc.experiments.exp01_persistent_components"),
    ("exp02", "stereo_scc.experiments.exp02_stereo_merger_barrier"),
    ("exp03", "stereo_scc.experiments.exp03_backprojection_pullback"),
    ("exp04", "stereo_scc.experiments.exp04_prior_likelihood_map"),
    ("exp05", "stereo_scc.experiments.exp05_kramers_markov_chain"),
]


def main():
    results = []
    for name, module_path in EXPERIMENTS:
        print(f"\n{'='*60}")
        print(f"Running {name} ...")
        t0 = time.time()
        try:
            import importlib
            mod = importlib.import_module(module_path)
            mod.run()
            elapsed = time.time() - t0
            results.append((name, "OK", f"{elapsed:.1f}s"))
        except Exception as e:
            elapsed = time.time() - t0
            traceback.print_exc()
            results.append((name, f"FAILED: {e}", f"{elapsed:.1f}s"))

    print(f"\n{'='*60}")
    print("EXPERIMENT SUMMARY")
    print(f"{'='*60}")
    print(f"{'Exp':<8} {'Status':<50} {'Time'}")
    print("-" * 70)
    for name, status, elapsed in results:
        print(f"{name:<8} {status:<50} {elapsed}")
    n_ok = sum(1 for _, s, _ in results if s == "OK")
    print(f"\n{n_ok}/{len(results)} experiments passed.")


if __name__ == "__main__":
    main()
