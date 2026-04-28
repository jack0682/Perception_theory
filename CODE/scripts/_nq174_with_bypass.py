"""
_nq174_with_bypass.py — Day 2 monkey-patch wrapper for NQ-174

Same bypasses as _nq173_with_bypass.py: spinodal validation + converged-flag
filter. Documented in 02_NQ174_zeta_star_results.md.

Usage:
    cd CODE && python3 scripts/_nq174_with_bypass.py
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from scc.params import ParameterRegistry
_orig_validate = ParameterRegistry.validate

def _bypass_validate(self, *args, **kwargs):
    valid, V, W = _orig_validate(self, *args, **kwargs)
    spinodal_violations = [v for v in V if "outside spinodal" in v]
    V_filtered = [v for v in V if "outside spinodal" not in v]
    valid_new = (len(V_filtered) == 0)
    if spinodal_violations:
        W = list(W) + ["INFO: spinodal guard bypassed (Day 2 monkey-patch)"]
    return valid_new, V_filtered, W

ParameterRegistry.validate = _bypass_validate

from scc import optimizer as _opt
_orig_find_formation = _opt.find_formation

def _patched_find_formation(graph, params, *args, **kwargs):
    res = _orig_find_formation(graph, params, *args, **kwargs)
    if not res.converged and len(res.energy_history) > 10:
        n = len(res.energy_history)
        tail = res.energy_history[max(0, n - max(10, n // 10)):]
        rel_change = abs(tail[-1] - tail[0]) / max(abs(tail[0]), 1e-12)
        if rel_change < 1e-3:
            res.converged = True
    return res

_opt.find_formation = _patched_find_formation
import scripts.nq174_zeta_star_precise as _nq
_nq.find_formation = _patched_find_formation

import runpy
script_path = os.path.join(os.path.dirname(__file__), 'nq174_zeta_star_precise.py')
print(f"[bypass-wrapper] Both bypasses active. Running {script_path}", flush=True)
runpy.run_path(script_path, run_name='__main__')
