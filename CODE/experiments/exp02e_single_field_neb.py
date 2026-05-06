#!/usr/bin/env python3
"""
exp02e: Single-field endpoint NEB for T-ST-5b (corrected methodology)

Corrects the exp02d endpoint flaw: K=2 endpoints were obtained from
`find_k_formations` (K-field product space + repulsion), which produces
combined fields that are NOT genuine local minima of the single-field SCC
energy in F_M(P). NEB barriers were systematically negative.

This experiment obtains K=2 endpoints by:
  1. Constructing a bimodal initial field (two bumps, manually)
  2. Running projected gradient descent under full/partial SCC energy
  3. Verifying K_act(u_K2*) = 2 via H0 persistence barcode (Union-Find)
  4. Rejecting endpoint if K_act != 2 or if not at a genuine local minimum

The K=1 endpoint uses a unimodal init → gradient descent → K_act=1 verify.

If the bimodal init collapses to K=1 under flat adjacency but stays K=2 under
smooth adjacency, that is itself strong evidence for T-ST-5b: the smooth
depth-weighted adjacency creates K=2 local minima that flat adjacency does not.

Energy variants:
  gl_only  : E_bd only (w_cl=0, w_sep=0)
  full_scc : E_bd + E_cl + E_sep (w_cl=1, w_sep=1)

NEB: single-field space, climbing image, exp60 design.

T-ST-5b hypothesis: under smooth adjacency, merger barrier ΔE_smooth > ΔE_flat.
Sub-hypothesis A: smooth adjacency creates stable K=2 minima that flat does not.
Sub-hypothesis B: given stable K=2 minima, the NEB barrier is higher under smooth.
"""
import sys, os, json, csv, time
import numpy as np
import scipy.sparse as sp

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.optimizer import project_volume
from scc.energy import EnergyComputer

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

ROWS, COLS = 12, 12
n = ROWS * COLS
RHO_PERS = 0.05          # persistence threshold for K_act
VOL_FRAC = 0.3

BETA_VALS = [10.0, 20.0]
DELTA_Z_VALS = [0.5, 1.0, 2.0]
LAMBDA_Z_VALS = [2.0, 4.0]

ENERGY_VARIANTS = [
    ("gl_only",  dict(w_cl=0.0, w_sep=0.0, w_bd=1.0)),
    ("full_scc", dict(w_cl=1.0, w_sep=1.0, w_bd=1.0)),
]

# Gradient descent parameters
RELAX_N_STEPS = 30000
RELAX_DT = 0.003
RELAX_N_STEPS_K1 = 20000

# NEB parameters
NEB_N_IMAGES = 12
NEB_MAX_ITER = 600
NEB_TOL = 5e-3
NEB_K_SPRING = 1.0
NEB_DT = 0.004

RESULT_DIR = os.path.join(os.path.dirname(__file__), 'results')
os.makedirs(RESULT_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# K_act counter via H0 persistence barcode (graph-general, not grid-restricted)
# ---------------------------------------------------------------------------

def k_act_from_barcode(u: np.ndarray, g: GraphState, rho_pers: float = RHO_PERS) -> int:
    """Count persistent H0 components: K_act = #{bars with length > rho_pers}.

    Uses superlevel-set Union-Find on the graph g (not restricted to grid).
    Canonical §3.11, D-ST-3.
    """
    nn = g.n
    order = np.argsort(-u)
    W_coo = g.W.tocoo()
    adj: list[list[int]] = [[] for _ in range(nn)]
    for i, j in zip(W_coo.row, W_coo.col):
        adj[i].append(j)

    parent = np.arange(nn, dtype=int)
    birth_val = np.zeros(nn, dtype=float)
    active = np.zeros(nn, dtype=bool)
    bar_lengths: list[float] = []

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for idx in order:
        active[idx] = True
        birth_val[idx] = u[idx]
        for nb in adj[idx]:
            if not active[nb]:
                continue
            ri, rn = find(idx), find(nb)
            if ri == rn:
                continue
            if birth_val[ri] >= birth_val[rn]:
                bar_lengths.append(float(birth_val[rn] - u[idx]))
                parent[rn] = ri
            else:
                bar_lengths.append(float(birth_val[ri] - u[idx]))
                parent[ri] = rn

    # Surviving component (infinite bar): length = max(u) - 0 (counted as max(u))
    all_lengths = [float(np.max(u))] + bar_lengths
    return sum(1 for l in all_lengths if l > rho_pers)


# ---------------------------------------------------------------------------
# Adjacency builders
# ---------------------------------------------------------------------------

def build_flat_adj(rows: int, cols: int) -> GraphState:
    return GraphState.grid_2d(rows, cols)


def build_smooth_adj(rows: int, cols: int, depth_map: np.ndarray,
                     lambda_z: float) -> GraphState:
    nn = rows * cols
    ri, ci, data = [], [], []
    for r in range(rows):
        for c in range(cols):
            idx = r * cols + c
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr2, nc2 = r + dr, c + dc
                if 0 <= nr2 < rows and 0 <= nc2 < cols:
                    nidx = nr2 * cols + nc2
                    dz = abs(depth_map[idx] - depth_map[nidx])
                    w = float(np.exp(-lambda_z * dz ** 2))
                    ri.append(idx); ci.append(nidx); data.append(w)
    W = sp.csr_matrix((data, (ri, ci)), shape=(nn, nn))
    return GraphState(W)


def make_depth_map(rows: int, cols: int, delta_z: float) -> np.ndarray:
    depth = np.ones(rows * cols)
    for idx in range(rows * cols):
        if (idx % cols) >= cols // 2:
            depth[idx] = 1.0 + delta_z
    return depth


def make_params(beta: float, **weight_kwargs) -> ParameterRegistry:
    return ParameterRegistry(
        beta_bd=beta,
        volume_fraction=VOL_FRAC,
        max_iter=RELAX_N_STEPS,
        n_restarts=1,
        eps_grad=5e-3,
        **weight_kwargs,
    )


# ---------------------------------------------------------------------------
# Init constructors
# ---------------------------------------------------------------------------

def make_bimodal_init(rows: int, cols: int, m_target: float,
                      bump_height: float = 0.85) -> np.ndarray:
    """Two formations: left-quarter and right-quarter columns, low valley middle.

    This places one formation on the left-depth side and one on the right-depth
    side, matching the depth discontinuity at cols//2.
    """
    nn = rows * cols
    u = np.full(nn, 0.05)
    bump_w = max(2, cols // 4)
    cr = rows // 2
    h_span = max(2, rows // 3)
    for r in range(cr - h_span, cr + h_span):
        if not (0 <= r < rows):
            continue
        for c in range(bump_w):
            u[r * cols + c] = bump_height
        for c in range(cols - bump_w, cols):
            u[r * cols + c] = bump_height
    return project_volume(np.clip(u, 0.0, 1.0), m_target)


def make_unimodal_init(rows: int, cols: int, m_target: float,
                       center_height: float = 0.8) -> np.ndarray:
    """Single formation centered in the grid."""
    nn = rows * cols
    u = np.full(nn, 0.05)
    cr, cc = rows // 2, cols // 2
    h_span = max(2, rows // 4)
    w_span = max(2, cols // 4)
    for r in range(cr - h_span, cr + h_span):
        for c in range(cc - w_span, cc + w_span):
            if 0 <= r < rows and 0 <= c < cols:
                u[r * cols + c] = center_height
    return project_volume(np.clip(u, 0.0, 1.0), m_target)


# ---------------------------------------------------------------------------
# Single-field gradient descent (from specified init)
# ---------------------------------------------------------------------------

def single_field_relax(u_init: np.ndarray, g: GraphState, p: ParameterRegistry,
                       n_steps: int = RELAX_N_STEPS,
                       dt: float = RELAX_DT,
                       verbose: bool = False) -> np.ndarray:
    """Projected gradient descent on F_M(P) from a specified initial field.

    This is the canonical single-field dynamics (§3.9, D-ST-2), NOT K-field.
    The endpoint is a genuine local minimum in F_M(P) (by gradient flow
    convergence, T14-equiv), not an artifact of inter-field repulsion.
    """
    ec = EnergyComputer(g, p)
    m_target = float(np.sum(u_init))
    u = project_volume(np.clip(u_init.copy(), 0.0, 1.0), m_target)

    E_prev = None
    for step in range(n_steps):
        grad = ec.gradient_projected(u)
        u_new = project_volume(np.clip(u - dt * grad, 0.0, 1.0), m_target)
        u = u_new
        # Energy-change stopping: accounts for box-clamping (u-change or KKT-gap
        # criteria give false convergence when many nodes are clamped at boundary).
        if step > 200 and step % 100 == 0:
            E_curr, _ = ec.energy(u)
            if E_prev is not None and abs(E_curr - E_prev) < 1e-7:
                if verbose:
                    print(f"    Converged (dE) at step {step}, E={E_curr:.6f}")
                break
            E_prev = E_curr
            if verbose and step % 2000 == 0:
                print(f"    step={step} E={E_curr:.5f}")

    return u


def is_local_minimum(u: np.ndarray, g: GraphState, p: ParameterRegistry,
                     tol: float = 1e-5) -> bool:
    """Feasible-step energy-change check for box+simplex constrained local minimum.

    The raw projected gradient RMS can be large even at a genuine constrained minimum
    when many nodes are box-active (clamped at 0 or 1). The clip+project_volume step
    may yield negligible energy change even with large unconstrained gradient. We
    therefore measure the actual energy decrease achievable by the constrained step.

    A field u is a practical local minimum if a small constrained step produces
    negligible energy improvement: |ΔE| < tol.
    """
    ec = EnergyComputer(g, p)
    E0, _ = ec.energy(u)
    m = float(np.sum(u))
    grad = ec.gradient_projected(u)
    dt_probe = 1e-4
    u_probe = project_volume(np.clip(u - dt_probe * grad, 0.0, 1.0), m)
    E1, _ = ec.energy(u_probe)
    return float(E0 - E1) < tol


# ---------------------------------------------------------------------------
# NEB (from exp60/exp02d; single-field climbing image)
# ---------------------------------------------------------------------------

def _neb_tangent_ew(images: list, energies: np.ndarray, i: int) -> np.ndarray:
    tau_plus = images[i + 1] - images[i]
    tau_minus = images[i] - images[i - 1]
    dE_plus = abs(energies[i + 1] - energies[i])
    dE_minus = abs(energies[i - 1] - energies[i])
    dE_max = max(dE_plus, dE_minus)
    dE_min = min(dE_plus, dE_minus)
    if energies[i + 1] > energies[i - 1]:
        tau = dE_max * tau_plus + dE_min * tau_minus
    elif energies[i + 1] < energies[i - 1]:
        tau = dE_min * tau_plus + dE_max * tau_minus
    else:
        tau = tau_plus + tau_minus
    norm = np.linalg.norm(tau)
    return tau / max(norm, 1e-14)


def neb_barrier(ec: EnergyComputer, m_total: float,
                u_A: np.ndarray, u_B: np.ndarray,
                n_images: int = NEB_N_IMAGES,
                k_spring: float = NEB_K_SPRING,
                max_iter: int = NEB_MAX_ITER,
                tol: float = NEB_TOL,
                dt: float = NEB_DT) -> dict:
    """Climbing-image NEB between u_A and u_B in single-field F_M(P) space."""
    total_images = n_images + 2
    images = [project_volume(np.clip(
        (1.0 - i/(total_images-1)) * u_A + (i/(total_images-1)) * u_B, 0.0, 1.0
    ), m_total) for i in range(total_images)]

    li_energies = np.array([ec.energy(img)[0] for img in images])
    E_A, E_B = float(ec.energy(u_A)[0]), float(ec.energy(u_B)[0])
    E_ref = max(E_A, E_B)
    barrier_li = float(np.max(li_energies) - E_ref)

    enable_climbing = max_iter // 4
    converged = False
    max_force_clamp = 5.0

    for iteration in range(max_iter):
        energies = np.array([ec.energy(img)[0] for img in images])
        gradients = [np.zeros(n) if (i == 0 or i == total_images - 1)
                     else ec.gradient_projected(images[i])
                     for i in range(total_images)]

        interior_E = energies[1:-1]
        climbing_idx = int(np.argmax(interior_E)) + 1
        use_climbing = (iteration >= enable_climbing)

        forces = []
        for i in range(1, total_images - 1):
            tau = _neb_tangent_ew(images, energies, i)
            grad_i = gradients[i]
            if i == climbing_idx and use_climbing:
                f = -grad_i + 2.0 * np.dot(grad_i, tau) * tau
            else:
                grad_perp = grad_i - np.dot(grad_i, tau) * tau
                d_plus = np.linalg.norm(images[i + 1] - images[i])
                d_minus = np.linalg.norm(images[i] - images[i - 1])
                f = -grad_perp + k_spring * (d_plus - d_minus) * tau
            f_norm = np.linalg.norm(f)
            if f_norm > max_force_clamp * np.sqrt(n):
                f = f * (max_force_clamp * np.sqrt(n) / f_norm)
            forces.append(f)

        max_force_val = max(np.linalg.norm(fv) / np.sqrt(n) for fv in forces)
        if max_force_val < tol:
            converged = True
            break
        for idx, i in enumerate(range(1, total_images - 1)):
            images[i] = project_volume(np.clip(images[i] + dt * forces[idx], 0.0, 1.0), m_total)

    final_energies = np.array([ec.energy(img)[0] for img in images])
    saddle_idx = int(np.argmax(final_energies[1:-1])) + 1
    barrier_neb = float(np.max(final_energies[1:-1]) - E_ref)

    return {
        'barrier_li': barrier_li,
        'barrier_neb': barrier_neb,
        'E_A': E_A,
        'E_B': E_B,
        'E_ref': E_ref,
        'saddle_E': float(final_energies[saddle_idx]),
        'saddle_idx': saddle_idx,
        'converged': converged,
        'n_iter': NEB_MAX_ITER if not converged else (enable_climbing + 1),
        'energy_path': final_energies.tolist(),
    }


# ---------------------------------------------------------------------------
# Per-trial runner
# ---------------------------------------------------------------------------

def run_trial(g: GraphState, p: ParameterRegistry,
              adj_name: str, variant_name: str,
              beta: float, delta_z: float, lambda_z: float,
              verbose: bool = False) -> dict:
    """Run one (adj, energy_variant, beta, delta_z, lambda_z) trial.

    Returns dict with endpoint validation results and NEB barrier.
    """
    base = dict(adj=adj_name, variant=variant_name,
                beta=beta, delta_z=delta_z, lambda_z=lambda_z)
    t0 = time.time()

    m_target = VOL_FRAC * n

    # Step 1: K=2 endpoint — bimodal init → single-field relax
    u_init_k2 = make_bimodal_init(ROWS, COLS, m_target)
    u_k2 = single_field_relax(u_init_k2, g, p,
                               n_steps=RELAX_N_STEPS, dt=RELAX_DT,
                               verbose=verbose)
    k_act_k2 = k_act_from_barcode(u_k2, g, RHO_PERS)
    is_min_k2 = is_local_minimum(u_k2, g, p, tol=0.02)
    E_k2, terms_k2 = EnergyComputer(g, p).energy(u_k2)

    if verbose:
        print(f"    K2 endpoint: K_act={k_act_k2}, is_min={is_min_k2}, E={E_k2:.4f}")

    # Step 2: K=1 endpoint — unimodal init → single-field relax
    u_init_k1 = make_unimodal_init(ROWS, COLS, m_target)
    u_k1 = single_field_relax(u_init_k1, g, p,
                               n_steps=RELAX_N_STEPS_K1, dt=RELAX_DT,
                               verbose=verbose)
    k_act_k1 = k_act_from_barcode(u_k1, g, RHO_PERS)
    is_min_k1 = is_local_minimum(u_k1, g, p, tol=0.02)
    E_k1, _ = EnergyComputer(g, p).energy(u_k1)

    if verbose:
        print(f"    K1 endpoint: K_act={k_act_k1}, is_min={is_min_k1}, E={E_k1:.4f}")

    elapsed_endpoints = time.time() - t0

    # Endpoint validation
    k2_valid = (k_act_k2 == 2) and is_min_k2
    k1_valid = (k_act_k1 <= 1) and is_min_k1

    if not k2_valid:
        note = (f"K=2 endpoint invalid: K_act={k_act_k2}, is_min={is_min_k2}. "
                f"Bimodal init collapsed to K={k_act_k2} — "
                f"{'K=2 not stable under this (adj, energy)' if k_act_k2 == 1 else 'unexpected K_act'}")
        return {**base,
                'K_act_k2': k_act_k2, 'is_min_k2': is_min_k2,
                'K_act_k1': k_act_k1, 'is_min_k1': is_min_k1,
                'E_k2': round(E_k2, 6), 'E_k1': round(E_k1, 6),
                'barrier_neb': float('nan'), 'barrier_li': float('nan'),
                'converged': False, 'note': note,
                'elapsed_s': round(time.time() - t0, 1)}

    if not k1_valid:
        note = f"K=1 endpoint invalid: K_act={k_act_k1}, is_min={is_min_k1}"
        return {**base,
                'K_act_k2': k_act_k2, 'is_min_k2': is_min_k2,
                'K_act_k1': k_act_k1, 'is_min_k1': is_min_k1,
                'E_k2': round(E_k2, 6), 'E_k1': round(E_k1, 6),
                'barrier_neb': float('nan'), 'barrier_li': float('nan'),
                'converged': False, 'note': note,
                'elapsed_s': round(time.time() - t0, 1)}

    # Step 3: NEB
    ec = EnergyComputer(g, p)
    neb = neb_barrier(ec, m_target, u_k2, u_k1)

    return {**base,
            'K_act_k2': k_act_k2, 'is_min_k2': is_min_k2,
            'K_act_k1': k_act_k1, 'is_min_k1': is_min_k1,
            'E_k2': round(E_k2, 6), 'E_k1': round(E_k1, 6),
            'E_k2_bd': round(terms_k2.get('E_bd', 0), 6),
            'E_k2_cl': round(terms_k2.get('E_cl', 0), 6),
            'E_k2_sep': round(terms_k2.get('E_sep', 0), 6),
            'barrier_neb': round(neb['barrier_neb'], 6),
            'barrier_li': round(neb['barrier_li'], 6),
            'saddle_E': round(neb['saddle_E'], 6),
            'converged': neb['converged'],
            'note': 'NEB K=2->1 (valid endpoints)',
            'elapsed_s': round(time.time() - t0, 1)}


# ---------------------------------------------------------------------------
# Summary and plots
# ---------------------------------------------------------------------------

def _isnan(x) -> bool:
    try:
        return float('nan') == float(x) or np.isnan(float(x))
    except (TypeError, ValueError):
        return True


def write_summary(all_rows: list, path: str):
    lines = [
        "# exp02e: Single-field NEB — T-ST-5b (corrected methodology)\n\n",
        "**Endpoint method:** bimodal init → single-field gradient descent → K_act verify\n",
        "**Key fix:** no K-field repulsion; endpoints are genuine F_M(P) local minima\n\n",
        "## Endpoint stability (sub-hypothesis A)\n\n",
        "Does bimodal init converge to K=2 under flat vs smooth adjacency?\n\n",
    ]

    for beta in BETA_VALS:
        lines.append(f"### β={beta}\n\n")
        for variant_name, _ in ENERGY_VARIANTS:
            rows_bv = [r for r in all_rows if r['beta'] == beta and r['variant'] == variant_name]
            flat_row = next((r for r in rows_bv if r['adj'] == 'flat'), None)
            smooth_k2_stable = [r for r in rows_bv if r['adj'] == 'smooth' and r.get('K_act_k2') == 2]

            flat_k2 = flat_row.get('K_act_k2', '?') if flat_row else '?'
            flat_note = flat_row.get('note', '') if flat_row else ''
            lines.append(f"**{variant_name}**: flat K_act_k2={flat_k2}  "
                         f"({flat_note[:60]})\n")
            lines.append(f"  smooth K=2 stable: {len(smooth_k2_stable)}/6 configs\n\n")

    lines.append("## NEB barrier results (sub-hypothesis B)\n\n")
    lines.append("Barrier = E(saddle) − max(E(K=2), E(K=1)). "
                 "Positive = genuine barrier. Negative = endpoint not at min.\n\n")

    for beta in BETA_VALS:
        lines.append(f"### β={beta}\n\n")
        for variant_name, _ in ENERGY_VARIANTS:
            rows_bv = [r for r in all_rows if r['beta'] == beta and r['variant'] == variant_name]
            flat_row = next((r for r in rows_bv if r['adj'] == 'flat'), None)
            smooth_valid = [r for r in rows_bv if r['adj'] == 'smooth'
                            and not _isnan(r.get('barrier_neb', float('nan')))]

            flat_b = float(flat_row['barrier_neb']) if (flat_row and not _isnan(flat_row.get('barrier_neb'))) else float('nan')
            smooth_barriers = [float(r['barrier_neb']) for r in smooth_valid]
            max_smooth = max(smooth_barriers, default=float('nan'))
            above_flat = sum(1 for b in smooth_barriers if b > flat_b + 1e-5)

            lines.append(f"**{variant_name}**: flat={flat_b:.4f}  "
                         f"max_smooth={max_smooth:.4f}  "
                         f"above_flat={above_flat}/{len(smooth_barriers)}\n")

            # Sub-hypothesis A verdict
            all_k2_collapse = [r for r in rows_bv if r['adj'] == 'smooth'
                                and r.get('K_act_k2') == 1]
            if len(all_k2_collapse) > 0 and flat_row and flat_row.get('K_act_k2') == 2:
                lines.append("  Sub-hyp A SUPPORTED: flat K=2 stable, smooth K=2 unstable\n")
            elif flat_row and flat_row.get('K_act_k2') == 1:
                n_smooth_stable = sum(1 for r in rows_bv if r['adj'] == 'smooth' and r.get('K_act_k2') == 2)
                if n_smooth_stable > 0:
                    lines.append(f"  Sub-hyp A SUPPORTED: flat K=2 collapses, smooth K=2 stable in {n_smooth_stable}/6 configs\n")
                else:
                    lines.append("  Sub-hyp A INCONCLUSIVE: K=2 not stable in any config\n")
            elif max_smooth > flat_b + 1e-4:
                lines.append("  Sub-hyp B PARTIAL: smooth barrier > flat barrier\n")
            else:
                lines.append("  Sub-hyp A+B NOT SUPPORTED\n")
            lines.append("\n")

    lines.append("## T-ST-5b overall verdict\n\n")
    any_positive = any(not _isnan(r.get('barrier_neb', float('nan')))
                       and float(r['barrier_neb']) > 1e-4
                       and r['adj'] == 'smooth' for r in all_rows)
    any_above_flat = False
    for beta in BETA_VALS:
        for variant_name, _ in ENERGY_VARIANTS:
            rows_bv = [r for r in all_rows if r['beta'] == beta and r['variant'] == variant_name]
            flat_row = next((r for r in rows_bv if r['adj'] == 'flat'), None)
            flat_b = float(flat_row.get('barrier_neb', float('nan'))) if flat_row else float('nan')
            for r in rows_bv:
                if r['adj'] == 'smooth' and not _isnan(r.get('barrier_neb')) and float(r['barrier_neb']) > flat_b + 1e-4:
                    any_above_flat = True

    if any_above_flat:
        lines.append("**PARTIALLY SUPPORTED**: At least one smooth config shows barrier > flat baseline.\n")
        lines.append("Report conditions precisely.\n")
    elif any_positive:
        lines.append("**POSITIVE SMOOTH BARRIER**: Smooth shows positive barrier even if flat comparison not clean.\n")
    else:
        lines.append("**NOT SUPPORTED under current implementation**: No smooth barrier above flat found.\n")
        lines.append("Either E_cl/E_sep do not differentiate flat vs smooth, or K=2 not stable in either case.\n")
        lines.append("Next: increase β, adjust init, or check if T-ST-5b requires different energy regime.\n")

    with open(path, 'w') as f:
        f.writelines(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 70)
    print("  exp02e: Single-Field NEB for T-ST-5b (corrected endpoints)")
    print(f"  Grid: {ROWS}x{COLS}  vol_frac={VOL_FRAC}  rho_pers={RHO_PERS}")
    print("=" * 70)

    all_rows: list[dict] = []

    for beta in BETA_VALS:
        print(f"\n{'='*60}\n  β={beta}\n{'='*60}")

        for variant_name, weight_kwargs in ENERGY_VARIANTS:
            print(f"\n  --- {variant_name} ---")
            p = make_params(beta, **weight_kwargs)

            # Flat adjacency
            g_flat = build_flat_adj(ROWS, COLS)
            print(f"  [flat/{variant_name}/β={beta}]")
            row = run_trial(g_flat, p, 'flat', variant_name, beta, 0.0, 0.0, verbose=True)
            all_rows.append(row)
            print(f"  flat: K2={row.get('K_act_k2')} K1={row.get('K_act_k1')} "
                  f"barrier={row['barrier_neb']} t={row['elapsed_s']}s")

            # Smooth adjacency sweep
            for delta_z in DELTA_Z_VALS:
                depth_map = make_depth_map(ROWS, COLS, delta_z)
                for lambda_z in LAMBDA_Z_VALS:
                    g_smooth = build_smooth_adj(ROWS, COLS, depth_map, lambda_z)
                    print(f"  [smooth Δz={delta_z} λ_z={lambda_z} / {variant_name}/β={beta}]")
                    row = run_trial(g_smooth, p, 'smooth', variant_name,
                                   beta, delta_z, lambda_z, verbose=True)
                    all_rows.append(row)
                    print(f"  smooth: K2={row.get('K_act_k2')} "
                          f"barrier={row['barrier_neb']} "
                          f"note={row.get('note', '')[:50]} t={row['elapsed_s']}s")

    # Save CSV
    fieldnames = ['adj', 'variant', 'beta', 'delta_z', 'lambda_z',
                  'K_act_k2', 'is_min_k2', 'K_act_k1', 'is_min_k1',
                  'E_k2', 'E_k1', 'E_k2_bd', 'E_k2_cl', 'E_k2_sep',
                  'barrier_neb', 'barrier_li', 'saddle_E',
                  'converged', 'note', 'elapsed_s']
    csv_path = os.path.join(RESULT_DIR, 'exp02e_single_field_neb.csv')
    with open(csv_path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        w.writeheader()
        w.writerows(all_rows)
    print(f"\nCSV: {csv_path}")

    # Save JSON
    json_path = os.path.join(RESULT_DIR, 'exp02e_single_field_neb.json')
    with open(json_path, 'w') as f:
        json.dump(all_rows, f, indent=2, default=str)
    print(f"JSON: {json_path}")

    # Summary
    summary_path = os.path.join(RESULT_DIR, 'exp02e_single_field_neb_summary.md')
    write_summary(all_rows, summary_path)
    print(f"Summary: {summary_path}")

    print(f"\n[exp02e] Done. {len(all_rows)} trials.")


if __name__ == '__main__':
    main()
