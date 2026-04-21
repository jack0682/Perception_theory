"""
scc/langevin.py — Projected Langevin SDE sampler on Σ_m for C+E framework.

Implements F3 (Round 3 §8, upgraded to Cat A via Lions-Sznitman) of the
F-group axioms. The continuous SDE is:

    du = -∇_{Σ_m} F_{C+E}(u) dt + sqrt(2T) dW_t,       (Stratonovich or Itô eqv.)

with reflection at ∂Σ_m (u_i = 0 or 1). We implement projected Euler-Maruyama
on the volume-tangent space 1^⊥ with box clipping.

Input:
  u_init : initial field on Σ_m (Σ u = m)
  graph  : GraphState
  params : ParameterRegistry (for ℰ evaluation)
  T      : temperature (F1 Gibbs scale)
  lambda_K : K_soft coupling (default γ_K · T)
  gamma_K  : dimensionless γ_K in [0.01, 0.1] per Round 3 E-7
  dt     : time step
  n_steps : number of Euler steps
  seed   : RNG seed

Output:
  trajectory: list of u_t over n_steps (optionally subsampled)
  summary: energy, K_soft, diagnostics over time

References:
  - Lions-Sznitman 1984 (reflection at boundary)
  - Freidlin-Wentzell (Kramers rate theory)
  - Round 3 §8 (F3 upgrade to Cat A on Σ_m^ε)
  - Round 4 Thm 2.1 (three-regime phase diagram)
"""
import numpy as np
from typing import Optional


def _get_energy_and_gradient(ec, u):
    """Try multiple scc API patterns to get (E, ∇E)."""
    # Pattern 1: ec.energy(u) returns (E, grad)
    try:
        out = ec.energy(u)
        if isinstance(out, tuple) and len(out) == 2 and out[1] is not None:
            g = np.asarray(out[1])
            if g.shape == u.shape:
                return float(out[0]), g
    except Exception:
        pass

    # Pattern 2: separate gradient method
    try:
        E = ec.energy(u)
        if isinstance(E, tuple):
            E = E[0]
        g = np.asarray(ec.gradient(u))
        return float(E), g
    except Exception:
        pass

    # Pattern 3: FD on energy (slow fallback)
    n = len(u)
    E0 = ec.energy(u)
    if isinstance(E0, tuple):
        E0 = E0[0]
    E0 = float(E0)
    eps = 1e-5
    g = np.zeros(n)
    for i in range(n):
        u_p = u.copy(); u_p[i] += eps
        E_p = ec.energy(u_p)
        if isinstance(E_p, tuple):
            E_p = E_p[0]
        g[i] = (float(E_p) - E0) / eps
    return E0, g


def _project_tangent(v, n):
    """Project v onto 1^⊥ (remove constant direction)."""
    return v - np.mean(v)


def _reflect_to_box(u, eps_box=1e-8):
    """Clip u to [eps_box, 1 - eps_box], then rescale to maintain Σ u = const."""
    m_before = u.sum()
    u_clipped = np.clip(u, eps_box, 1.0 - eps_box)
    m_after = u_clipped.sum()
    if m_after > 0:
        u_clipped *= (m_before / m_after)
    return u_clipped


def _compute_k_soft_safely(u, grid_size):
    """Try to compute K_soft via scc.k_soft. Return None if unavailable."""
    try:
        from scc.k_soft import k_soft
        return float(k_soft(u, grid_size))
    except Exception:
        return None


def bernoulli_entropy_grad(u, eps=1e-10):
    """∇S(u) = -log(u / (1-u)) = log((1-u)/u), with clipping."""
    u_safe = np.clip(u, eps, 1.0 - eps)
    return np.log((1.0 - u_safe) / u_safe)


def k_soft_gradient_safely(u, grid_size, eps=1e-4):
    """FD gradient of K_soft. O(n) k_soft evaluations."""
    try:
        from scc.k_soft import k_soft
        K0 = k_soft(u, grid_size)
        n = len(u)
        g = np.zeros(n)
        for i in range(n):
            u_p = u.copy(); u_p[i] += eps
            u_m = u.copy(); u_m[i] -= eps
            g[i] = (k_soft(u_p, grid_size) - k_soft(u_m, grid_size)) / (2 * eps)
        return g
    except Exception:
        return np.zeros(len(u))


def projected_langevin(
    u_init: np.ndarray,
    graph,
    params,
    T: float,
    n_steps: int = 10000,
    dt: float = 1e-3,
    lambda_K: Optional[float] = None,
    gamma_K: float = 0.05,
    use_k_soft: bool = False,
    grid_size: Optional[int] = None,
    seed: int = 42,
    subsample: int = 100,
    eps_box: float = 1e-4,
    verbose: bool = False,
):
    """Run projected Langevin on Σ_m under ℱ_C+E = ℰ - T·S + λ_K·K_soft.

    Returns dict with:
      'trajectory' : (n_samples, n) array of subsampled u values
      'times'      : subsampled time points
      'energies'   : ℰ(u_t) over subsampled time
      'k_soft'     : K_soft(u_t) over subsampled time (None if disabled)
      'mean_u'     : Σ u_i / n at each subsampled time (should be ≈ c)
      'final_u'    : last u
    """
    from scc.energy import EnergyComputer

    ec = EnergyComputer(graph, params)
    u = np.asarray(u_init, dtype=np.float64).copy()
    n = len(u)
    m_target = u.sum()
    c = m_target / n

    if lambda_K is None:
        lambda_K = gamma_K * T if use_k_soft else 0.0

    rng = np.random.default_rng(seed)
    noise_scale = np.sqrt(2.0 * T * dt)

    trajectory = []
    times = []
    energies = []
    k_softs = []
    mean_us = []

    for step in range(n_steps):
        # 1. Gradient of F_C+E = ℰ - T·S + λ_K·K_soft
        E, grad_E = _get_energy_and_gradient(ec, u)
        grad_S = bernoulli_entropy_grad(u)
        grad_F = grad_E - T * grad_S
        if use_k_soft and lambda_K > 0 and grid_size is not None:
            grad_F += lambda_K * k_soft_gradient_safely(u, grid_size)

        # 2. Project onto volume-tangent 1^⊥
        grad_F_proj = _project_tangent(grad_F, n)

        # 3. Gaussian noise, projected
        xi = rng.standard_normal(n)
        xi_proj = _project_tangent(xi, n)

        # 4. Euler-Maruyama step
        u_next = u - dt * grad_F_proj + noise_scale * xi_proj

        # 5. Reflect to box [eps_box, 1 - eps_box], preserving mass
        u_next = _reflect_to_box(u_next, eps_box)

        u = u_next

        # Subsample
        if step % subsample == 0:
            trajectory.append(u.copy())
            times.append(step * dt)
            energies.append(E)
            mean_us.append(float(np.mean(u)))
            if use_k_soft and grid_size is not None:
                ks = _compute_k_soft_safely(u, grid_size)
                k_softs.append(ks)
            if verbose and step % (subsample * 10) == 0:
                print(f"  step={step:>6d}, E={E:.4f}, mean_u={np.mean(u):.4f}, "
                      f"min_u={u.min():.4f}, max_u={u.max():.4f}")

    return {
        'trajectory': np.array(trajectory),
        'times': np.array(times),
        'energies': np.array(energies),
        'k_soft': np.array(k_softs) if k_softs else None,
        'mean_u': np.array(mean_us),
        'final_u': u,
        'params': {
            'T': T, 'dt': dt, 'n_steps': n_steps,
            'lambda_K': lambda_K, 'gamma_K': gamma_K,
            'use_k_soft': use_k_soft, 'c': c,
        },
    }


def sample_gibbs_ensemble(
    graph, params, T, u_inits, n_steps_per=5000, dt=1e-3,
    gamma_K=0.05, use_k_soft=False, grid_size=None, seeds=None,
):
    """Run multiple independent Langevin chains from different u_inits,
    collect final states for Gibbs ensemble sampling.
    """
    if seeds is None:
        seeds = list(range(len(u_inits)))

    results = []
    for i, (u_init, seed) in enumerate(zip(u_inits, seeds)):
        r = projected_langevin(
            u_init, graph, params, T=T,
            n_steps=n_steps_per, dt=dt,
            gamma_K=gamma_K, use_k_soft=use_k_soft,
            grid_size=grid_size, seed=seed,
            subsample=n_steps_per // 20,
        )
        results.append(r)
    return results
