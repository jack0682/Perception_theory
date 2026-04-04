#!/usr/bin/env python3
"""Master script: generate all SCC textbook figures (80-100 total).

Usage:
    python3 run_all_figures.py          # Run all sequentially
    python3 run_all_figures.py --part 1  # Run only P1
    python3 run_all_figures.py --parallel # Run all in parallel
"""

import subprocess
import sys
import os
import time
import argparse
from pathlib import Path

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FIGURE_DIR = os.path.join(SCRIPT_DIR, '..', 'figures')

SCRIPTS = [
    ('P1: Foundations', 'generate_p1_foundations.py'),
    ('P2: Formal Theory', 'generate_p2_formal_theory.py'),
    ('P3: Experiments', 'generate_p3_experiments.py'),
    ('P4: Applications', 'generate_p4_applications.py'),
]


def run_sequential(parts=None):
    """Run scripts sequentially."""
    total_start = time.time()
    for i, (label, script) in enumerate(SCRIPTS, 1):
        if parts and i not in parts:
            continue
        print(f"\n{'='*60}")
        print(f"Running {label} ({script})...")
        print('='*60)
        start = time.time()
        result = subprocess.run(
            [sys.executable, os.path.join(SCRIPT_DIR, script)],
            cwd=os.path.join(SCRIPT_DIR, '..', '..', '..', '..'),
        )
        elapsed = time.time() - start
        status = '✓' if result.returncode == 0 else '✗'
        print(f"{status} {label} completed in {elapsed:.1f}s (exit code {result.returncode})")

    total = time.time() - total_start
    print(f"\n{'='*60}")
    print(f"Total time: {total:.1f}s")
    count_figures()


def run_parallel():
    """Run all scripts in parallel."""
    import concurrent.futures

    total_start = time.time()
    print("Running all figure scripts in parallel...")

    def run_one(label, script):
        start = time.time()
        result = subprocess.run(
            [sys.executable, os.path.join(SCRIPT_DIR, script)],
            cwd=os.path.join(SCRIPT_DIR, '..', '..', '..', '..'),
            capture_output=True, text=True,
        )
        elapsed = time.time() - start
        return label, result.returncode, elapsed, result.stdout, result.stderr

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = {
            executor.submit(run_one, label, script): label
            for label, script in SCRIPTS
        }

        for future in concurrent.futures.as_completed(futures):
            label, code, elapsed, stdout, stderr = future.result()
            status = '✓' if code == 0 else '✗'
            print(f"{status} {label} completed in {elapsed:.1f}s")
            if code != 0 and stderr:
                print(f"  STDERR: {stderr[:200]}")

    total = time.time() - total_start
    print(f"\nTotal time: {total:.1f}s")
    count_figures()


def count_figures():
    """Count and list all generated figures."""
    total = 0
    for subdir in ['P1_foundations', 'P2_formal', 'P3_experiments', 'P4_applications']:
        path = os.path.join(FIGURE_DIR, subdir)
        if os.path.exists(path):
            files = [f for f in os.listdir(path) if f.endswith('.pdf')]
            total += len(files)
            print(f"  {subdir}: {len(files)} figures")
    print(f"\n✓ Total: {total} figures generated")


def generate_manifest():
    """Generate CSV manifest of all figures."""
    manifest_path = os.path.join(FIGURE_DIR, 'FIGURE_MANIFEST.csv')
    lines = ['filename,part,description']

    part_names = {
        'P1_foundations': 'P1',
        'P2_formal': 'P2',
        'P3_experiments': 'P3',
        'P4_applications': 'P4',
    }

    for subdir, part in part_names.items():
        path = os.path.join(FIGURE_DIR, subdir)
        if os.path.exists(path):
            for f in sorted(os.listdir(path)):
                if f.endswith('.pdf'):
                    desc = f.replace('.pdf', '').replace('_', ' ').title()
                    lines.append(f"{subdir}/{f},{part},{desc}")

    with open(manifest_path, 'w') as fh:
        fh.write('\n'.join(lines) + '\n')
    print(f"\n✓ Manifest written to {manifest_path}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate SCC textbook figures')
    parser.add_argument('--part', type=int, nargs='+', help='Run specific parts (1-4)')
    parser.add_argument('--parallel', action='store_true', help='Run in parallel')
    parser.add_argument('--manifest', action='store_true', help='Generate manifest only')
    args = parser.parse_args()

    if args.manifest:
        generate_manifest()
    elif args.parallel:
        run_parallel()
        generate_manifest()
    else:
        run_sequential(args.part)
        generate_manifest()
