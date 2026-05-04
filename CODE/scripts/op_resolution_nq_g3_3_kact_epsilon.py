"""
op_resolution_nq_g3_3_kact_epsilon.py — NQ-G3-3 K_act stability under ε perturbation
at fixed initial state (W6 D1 op_resolution session).

Question (per logs/daily/2026-05-04/op_resolution.md §8):
  For a fixed multi-formation state $\mathbf u$, $K_{\mathrm{act}}^\epsilon(\mathbf u)$ is
  monotone non-increasing in ε. At what ε does $K_{\mathrm{act}}$ jump? Is the jump set
  "structural" or "noise-driven"?

Approach: trivial numerical experiment.
  - Standard L1-I initial state: T^2_{20}, M=90, K_field=4, initial_masses=(30, 30, 30, 0).
  - Per-slot mass values: {30, 30, 30, 0}.
  - Sweep ε over a wide range; compute K_act^ε per ε.
  - Identify jump points.

Expected result (theoretical pre-analysis): single structural jump at ε=30 (where all
3 active slots simultaneously deactivate, since they have identical mass). K_act = 3
on [0, 30); K_act = 0 on (30, ∞).

Output: stdout table + JSON to results/.
"""
from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone

# Standard L1-I configuration (from CODE/scripts/l1i_constants_feasibility.py + nq242c_counterexample.py)
INITIAL_MASSES = (30.0, 30.0, 30.0, 0.0)
K_FIELD = 4
M_TOTAL = sum(INITIAL_MASSES)  # 90.0


def k_act(epsilon: float) -> tuple[int, list[bool]]:
    """Compute K_act^ε for the standard L1-I initial state.

    Returns (K_act count, per-slot activation list).
    """
    activations = [m > epsilon for m in INITIAL_MASSES]
    return sum(activations), activations


def main(out_dir: str = None) -> int:
    # Sweep epsilon over a wide range covering all interesting transitions
    epsilon_values = [
        0.0, 0.0001, 0.001, 0.01, 0.05, 0.10, 0.225, 0.5, 1.0, 5.0, 10.0,
        20.0, 25.0, 29.999, 30.0, 30.001, 35.0, 50.0, 100.0,
    ]

    print("NQ-G3-3 K_act stability under ε perturbation at fixed initial state")
    print(f"Standard L1-I configuration: T^2_{{20}}, M={M_TOTAL}, K_field={K_FIELD}")
    print(f"Per-slot initial masses: {INITIAL_MASSES}")
    print()
    print(f"{'epsilon':>10} | {'K_act':>5} | per-slot active")
    print("-" * 50)

    rows = []
    prev_kact = None
    jumps = []
    for eps in epsilon_values:
        kact, activations = k_act(eps)
        active_str = "[" + ",".join("T" if a else "F" for a in activations) + "]"
        rows.append({
            "epsilon": eps,
            "K_act": kact,
            "per_slot_active": activations,
        })
        marker = ""
        if prev_kact is not None and kact != prev_kact:
            jumps.append({"epsilon": eps, "K_act_before": prev_kact, "K_act_after": kact})
            marker = "  ← JUMP"
        print(f"{eps:>10.4f} | {kact:>5d} | {active_str}{marker}")
        prev_kact = kact

    print()
    print("Jump analysis:")
    for j in jumps:
        print(f"  ε crossing ≈ {j['epsilon']}: K_act {j['K_act_before']} → {j['K_act_after']}")

    print()
    print("Verdict: K_act^ε is structurally stable in [0, 30) at K_act = 3.")
    print("Single simultaneous jump at ε = 30 (all 3 active slots have identical mass = 30).")
    print("This is the trivial-case structural baseline; dynamic-state analog is deferred (NQ-G3-3-dynamic).")

    out = {
        "spec": {
            "task": "NQ-G3-3",
            "purpose": (
                "K_act stability under epsilon perturbation at fixed initial state. "
                "Standard L1-I configuration (T^2_20, M=90, K_field=4, initial_masses=(30,30,30,0))."
            ),
            "datetime_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        },
        "initial_state": {
            "K_field": K_FIELD,
            "M_total": M_TOTAL,
            "initial_masses": list(INITIAL_MASSES),
        },
        "epsilon_sweep": rows,
        "jumps": jumps,
        "verdict": (
            "K_act^epsilon is structurally stable in [0, 30) at K_act=3. "
            "Single simultaneous jump at epsilon=30. Cat A absolute (initial state). "
            "Dynamic-state analog (post-gradient-flow with continuous per-slot mass distribution) "
            "deferred as NQ-G3-3-dynamic (W7+)."
        ),
    }

    if out_dir is None:
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "op_resolution_nq_g3_3_kact_epsilon.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nSaved: {out_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
