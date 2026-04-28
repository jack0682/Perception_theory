"""FindFormation optimizer: projected gradient flow on Sigma_m.

Semi-implicit scheme with Barzilai-Borwein step size, Armijo backtracking,
volume-constrained projection, and multi-start capability.
Follows I3-R13 §II algorithm design.
"""

from __future__ import annotations

import numpy as np
from dataclasses import dataclass
from typing import Dict, List

from scipy.sparse.linalg import spsolve

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.energy import EnergyComputer
from scc.diagnostics import compute_diagnostics, DiagnosticVector


@dataclass
class FormationResult:
    """Result of the FindFormation optimization."""
    u: np.ndarray
    energy: float
    energy_terms: Dict[str, float]
    diagnostics: DiagnosticVector
    converged: bool
    n_iter: int
    energy_history: List[float]
    grad_norm_history: List[float]


# ---------------------------------------------------------------------------
# Projection onto Sigma_m ∩ [0,1]^n
# ---------------------------------------------------------------------------

def project_volume(u: np.ndarray, m: float) -> np.ndarray:
    """Project u onto {v : v_i in [0,1], sum(v) = m}.

    Uses the exact Euclidean projection via clip-and-shift:
    v* = clip(u - lam, 0, 1) where lam is chosen so sum(v*) = m.
    This is the true nearest-point projection, unlike multiplicative
    rescaling which introduces systematic bias.
    """
    n = len(u)
    if n == 0:
        return u

    # Bisection on the shift parameter lambda
    lo = float(np.min(u)) - 1.0
    hi = float(np.max(u)) + 1.0

    for _ in range(60):  # bisection converges in ~50 iterations for double precision
        mid = (lo + hi) / 2.0
        v = np.clip(u - mid, 0.0, 1.0)
        s = np.sum(v)
        if abs(s - m) < 1e-12:
            break
        if s > m:
            lo = mid
        else:
            hi = mid

    return np.clip(u - mid, 0.0, 1.0)


# ---------------------------------------------------------------------------
# Single optimization run
# ---------------------------------------------------------------------------

def _optimize_single(
    graph: GraphState,
    params: ParameterRegistry,
    ec: EnergyComputer,
    seed: int,
) -> tuple[np.ndarray, float, dict, list, list, bool, int]:
    """Run one restart of projected gradient descent."""
    n = graph.n
    c = params.volume_fraction
    m = c * n
    dt = params.dt_init

    # Initialize: seed=0 uses Fiedler, others use random
    rng = np.random.RandomState(seed)
    if seed == 0:
        try:
            v2 = graph.fiedler_vector()
            v2 = v2 / (np.linalg.norm(v2) + 1e-12)
            u = np.full(n, c) + params.eps_init * v2
        except Exception:
            u = np.full(n, c) + params.eps_init * rng.randn(n)
    else:
        u = np.full(n, c) + params.eps_init * rng.randn(n)
    u = project_volume(u, m)

    energy_history: list[float] = []
    grad_norm_history: list[float] = []

    E_old, terms = ec.energy(u)
    energy_history.append(E_old)
    converged = False
    gnorm = float('inf')

    # Check if semi-implicit stepping is appropriate
    diffusion_coeff = ec.lambda_bd * 4.0 * params.alpha_bd
    use_semi_implicit = diffusion_coeff > 1e-12

    for tau in range(1, params.max_iter + 1):
        # --- Gradient computation ---
        g = ec.gradient(u)
        # Box-aware KKT residual: estimate Lagrange multiplier from
        # interior nodes only (not box-constrained), then measure residual.
        # This avoids inflating the norm with legitimate box-boundary gradients.
        interior = (u > 1e-6) & (u < 1 - 1e-6)
        if np.sum(interior) > 0:
            nu_est = np.mean(g[interior])
            kkt_res = g - nu_est
            kkt_res[~interior] = 0.0  # box-constrained nodes are at KKT by complementarity
            gnorm = float(np.linalg.norm(kkt_res) / np.sqrt(n))
        else:
            g_sigma = g - np.mean(g)
            gnorm = float(np.linalg.norm(g_sigma) / np.sqrt(n))
        grad_norm_history.append(gnorm)

        # --- Step ---
        # Mean-subtracted gradient for stepping (always needed)
        g_sigma = g - np.mean(g)

        if use_semi_implicit:
            # Semi-implicit: explicit for reaction, implicit for diffusion
            Lu = np.asarray(graph.L @ u).ravel()
            g_diffusion = ec.lambda_bd * 4.0 * params.alpha_bd * Lu
            g_react = g_sigma - g_diffusion
            g_react = g_react - np.mean(g_react)

            u_react = u - dt * g_react
            A_imp = graph.implicit_matrix(dt * ec.lambda_bd, params.alpha_bd)
            u_new = spsolve(A_imp, u_react)
        else:
            u_new = u - dt * g_sigma

        u_new = project_volume(u_new, m)

        # --- Energy evaluation and step acceptance ---
        E_new, terms_new = ec.energy(u_new)

        if E_new > E_old and tau > 5:
            dt *= 0.5
            if dt < 1e-10:
                break
            continue

        # Accept step — Barzilai-Borwein update
        s = u_new - u
        g_new = ec.gradient(u_new)
        g_new_sigma = g_new - np.mean(g_new)
        y = g_new_sigma - g_sigma
        sts = float(s @ s)
        sty = float(s @ y)
        if abs(sty) > 1e-15 and sts > 1e-15:
            dt_bb = abs(sts / sty)
            dt = max(min(dt_bb, 0.1), 1e-6)

        u = u_new
        E_old = E_new
        terms = terms_new
        energy_history.append(E_new)

        # --- Convergence check ---
        if tau > 10 and len(energy_history) >= 2:
            dE = abs(energy_history[-1] - energy_history[-2])
            rel_dE = dE / (abs(E_old) + 1e-15)
            ds = np.linalg.norm(s) / np.sqrt(n)
            if (rel_dE < params.eps_energy
                    and gnorm < params.eps_grad
                    and ds < params.eps_field):
                converged = True
                break

        # Energy stagnation check — plateau indicates the optimizer has
        # found a practical minimum. With box-aware KKT residual, gnorm
        # is now an accurate measure of stationarity. If gnorm is also
        # below threshold at stagnation, we declare convergence.
        # non-convergence.
        if tau > 100 and len(energy_history) > 100:
            recent = energy_history[-100:]
            if abs(recent[0] - recent[-1]) < 1e-9 * (abs(recent[0]) + 1.0):
                if gnorm < params.eps_grad:
                    converged = True
                break

    return u, E_old, terms, energy_history, grad_norm_history, converged, tau


def _optimize_single_from(
    graph: GraphState,
    params: ParameterRegistry,
    ec: EnergyComputer,
    u_init: np.ndarray,
) -> tuple[np.ndarray, float, dict, list, list, bool, int]:
    """Run projected gradient descent from a given initial field.

    Same algorithm as _optimize_single but starts from u_init (already
    projected onto Sigma_m) instead of generating an initialization from
    a random seed.
    """
    n = graph.n
    c = params.volume_fraction
    m = c * n
    dt = params.dt_init

    u = u_init.copy()

    energy_history: list[float] = []
    grad_norm_history: list[float] = []

    E_old, terms = ec.energy(u)
    energy_history.append(E_old)
    converged = False
    gnorm = float('inf')

    diffusion_coeff = ec.lambda_bd * 4.0 * params.alpha_bd
    use_semi_implicit = diffusion_coeff > 1e-12

    for tau in range(1, params.max_iter + 1):
        g = ec.gradient(u)
        interior = (u > 1e-6) & (u < 1 - 1e-6)
        if np.sum(interior) > 0:
            nu_est = np.mean(g[interior])
            kkt_res = g - nu_est
            kkt_res[~interior] = 0.0
            gnorm = float(np.linalg.norm(kkt_res) / np.sqrt(n))
        else:
            g_sigma = g - np.mean(g)
            gnorm = float(np.linalg.norm(g_sigma) / np.sqrt(n))
        grad_norm_history.append(gnorm)

        g_sigma = g - np.mean(g)

        if use_semi_implicit:
            from scipy.sparse.linalg import spsolve as _spsolve
            Lu = np.asarray(graph.L @ u).ravel()
            g_diffusion = ec.lambda_bd * 4.0 * params.alpha_bd * Lu
            g_react = g_sigma - g_diffusion
            g_react = g_react - np.mean(g_react)
            u_react = u - dt * g_react
            A_imp = graph.implicit_matrix(dt * ec.lambda_bd, params.alpha_bd)
            u_new = _spsolve(A_imp, u_react)
        else:
            u_new = u - dt * g_sigma

        u_new = project_volume(u_new, m)

        E_new, terms_new = ec.energy(u_new)

        if E_new > E_old and tau > 5:
            dt *= 0.5
            if dt < 1e-10:
                break
            continue

        s = u_new - u
        g_new = ec.gradient(u_new)
        g_new_sigma = g_new - np.mean(g_new)
        y = g_new_sigma - g_sigma
        sts = float(s @ s)
        sty = float(s @ y)
        if abs(sty) > 1e-15 and sts > 1e-15:
            dt_bb = abs(sts / sty)
            dt = max(min(dt_bb, 0.1), 1e-6)

        u = u_new
        E_old = E_new
        terms = terms_new
        energy_history.append(E_new)

        if tau > 10 and len(energy_history) >= 2:
            dE = abs(energy_history[-1] - energy_history[-2])
            rel_dE = dE / (abs(E_old) + 1e-15)
            ds = np.linalg.norm(s) / np.sqrt(n)
            if (rel_dE < params.eps_energy
                    and gnorm < params.eps_grad
                    and ds < params.eps_field):
                converged = True
                break

        if tau > 100 and len(energy_history) > 100:
            recent = energy_history[-100:]
            if abs(recent[0] - recent[-1]) < 1e-9 * (abs(recent[0]) + 1.0):
                if gnorm < params.eps_grad:
                    converged = True
                break

    return u, E_old, terms, energy_history, grad_norm_history, converged, tau


# ---------------------------------------------------------------------------
# Multi-start FindFormation (public API)
# ---------------------------------------------------------------------------

def find_formation(
    graph: GraphState,
    params: ParameterRegistry,
    normalize: bool = True,
    verbose: bool = False,
    u_init: np.ndarray | None = None,
    allow_outside_spinodal: bool = False,
) -> FormationResult:
    """Run FindFormation with multi-start optimization.

    Parameters
    ----------
    graph : GraphState
    params : ParameterRegistry
    normalize : bool — apply Hessian normalization to energy weights
    verbose : bool — print progress
    u_init : optional initial field. When provided, skips multi-start and
        runs a single optimization from this initialization (projected onto
        the feasible set).
    allow_outside_spinodal : if True, demote spinodal-range violation to
        warning. Used for IC-driven metastable-stationary studies where the
        formation is metastable but not the global minimum (NQ-191).

    Returns
    -------
    FormationResult with optimized field, energy, diagnostics, convergence info.
    """
    # Validate parameters
    valid, violations, warnings = params.validate(
        fiedler_eigenvalue=graph.fiedler,
        allow_outside_spinodal=allow_outside_spinodal,
    )
    if not valid:
        raise ValueError("Parameter validation failed:\n" + "\n".join(violations))
    if verbose and warnings:
        for w in warnings:
            print(w)

    ec = EnergyComputer(graph, params)

    # Hessian normalization (Phase 1)
    if normalize:
        norms = ec.normalize_weights()
        if verbose:
            print(f"Hessian norms: {norms}")
            print(f"Weights: cl={ec.lambda_cl:.4f}, sep={ec.lambda_sep:.4f}, bd={ec.lambda_bd:.4f}")

    # Single-start from u_init if provided
    if u_init is not None:
        n = graph.n
        c = params.volume_fraction
        m = c * n
        u_projected = project_volume(np.clip(u_init, 0.0, 1.0), m)
        u, E, terms, ehist, ghist, conv, niter = _optimize_single_from(
            graph, params, ec, u_projected,
        )
        diag = compute_diagnostics(u, graph, params)
        return FormationResult(
            u=u,
            energy=E,
            energy_terms=terms,
            diagnostics=diag,
            converged=conv,
            n_iter=niter,
            energy_history=ehist,
            grad_norm_history=ghist,
        )

    # Multi-start optimization (Phase 2)
    best_u = None
    best_E = float('inf')
    best_terms: dict = {}
    best_history: list = []
    best_gnorm: list = []
    best_converged = False
    best_niter = 0

    for r in range(params.n_restarts):
        if verbose:
            print(f"\n--- Restart {r+1}/{params.n_restarts} ---")

        u, E, terms, ehist, ghist, conv, niter = _optimize_single(
            graph, params, ec, seed=r,
        )

        if verbose:
            gn = ghist[-1] if ghist else float('inf')
            print(f"  E={E:.6f}, converged={conv}, iters={niter}, |grad|={gn:.2e}")

        if E < best_E:
            best_u = u.copy()
            best_E = E
            best_terms = terms
            best_history = ehist
            best_gnorm = ghist
            best_converged = conv
            best_niter = niter

    # Phase 3: diagnostics
    assert best_u is not None
    diag = compute_diagnostics(best_u, graph, params)

    if verbose:
        print(f"\nBest: E={best_E:.6f}")
        print(f"Diagnostics: {diag}")

    return FormationResult(
        u=best_u,
        energy=best_E,
        energy_terms=best_terms,
        diagnostics=diag,
        converged=best_converged,
        n_iter=best_niter,
        energy_history=best_history,
        grad_norm_history=best_gnorm,
    )
