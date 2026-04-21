"""K_soft — soft persistence-weighted mode count (C+E framework).

Implements `K_soft(u) = Σ_i φ(ℓ_i)` where ℓ_i are H₀ persistence bar lengths
of the superlevel-set filtration of u.

Theoretical reference: `THEORY/working/E/soft_K_definition.md` (G1).
Numerical verification: `THEORY/logs/daily/2026-04-21/12_code_verification.md`.

Hard-K recovery (Prop 4.1 verified):
    sharp K=1 → K_soft = φ(1) = 0.5 (φ-sat default)
    sharp K=2 → K_soft = 2·φ(1) = 1.0
    sharp K   → K_soft = K·φ(1)

Lipschitz (Cor 4.1 verified): L_K ≤ 4·L_φ·n globally on Σ_m.
"""

from __future__ import annotations

from typing import Callable

import numpy as np

from scc.persistence import persistence_h0


def phi_sat(ell: float) -> float:
    """Saturating φ: φ(ℓ) = ℓ/(1+ℓ) ∈ [0, 1). Lipschitz constant L_φ = 1."""
    return ell / (1.0 + ell)


def phi_lin(ell: float, ell_0: float = 0.1) -> float:
    """Truncated linear φ: φ(ℓ) = min(ℓ/ℓ_0, 1). Lipschitz constant L_φ = 1/ℓ_0."""
    return min(ell / ell_0, 1.0)


def k_soft(
    u: np.ndarray,
    grid_size: tuple[int, int] | int,
    phi: Callable[[float], float] = phi_sat,
    eps: float = 1e-12,
) -> float:
    """Compute K_soft(u) = Σ_i φ(ℓ_i) over positive-length H₀ bars.

    Parameters
    ----------
    u : (n,) array of cohesion values, n = rows × cols.
    grid_size : (rows, cols) or single int for square grid.
    phi : weighting function ℝ_≥0 → ℝ_≥0, default (φ-sat).
    eps : threshold below which bar lengths are treated as zero.

    Returns
    -------
    K_soft value (≥ 0). For φ-sat default: bounded above by number of bars · φ(1).

    Notes
    -----
    Superlevel filtration convention: persistence_h0 returns (b, d) with b ≥ d.
    Bar length ℓ = b - d ≥ 0. Essential bar (death = 0) is included if length > eps.
    """
    bars = persistence_h0(u, grid_size)
    return sum(phi(b - d) for b, d in bars if (b - d) > eps)


def k_soft_gradient_sparse(
    u: np.ndarray,
    grid_size: tuple[int, int] | int,
    phi_prime: Callable[[float], float] = lambda l: 1.0 / (1.0 + l) ** 2,
    eps: float = 1e-12,
) -> np.ndarray:
    """Sparse gradient ∇K_soft (off vineyard set V).

    For each H₀ bar i with birth at vertex v_b^i and death at vertex v_d^i:
        ∂K_soft/∂u_x = φ'(ℓ_i) · (δ_{x, v_b^i} - δ_{x, v_d^i})

    On the vineyard set V (codim-1, where bar identities reorder), gradient is
    discontinuous. Returns a representative gradient (one of the limiting values).

    Parameters
    ----------
    u : (n,) array.
    grid_size : grid spec.
    phi_prime : derivative of φ, default for (φ-sat) = 1/(1+ℓ)².

    Returns
    -------
    grad : (n,) sparse-style gradient array.

    Notes
    -----
    This implementation uses a finite-difference fallback for vertex assignment
    accuracy, rather than tracking the persistence computation's birth/death
    vertices directly (which would require extending scc.persistence).
    """
    n = u.size
    grad = np.zeros(n)
    h = 1e-6
    ks0 = k_soft(u, grid_size)
    for i in range(n):
        u_p = u.copy()
        u_p[i] += h
        ks_p = k_soft(u_p, grid_size)
        grad[i] = (ks_p - ks0) / h
    return grad


def free_energy_ce(
    u: np.ndarray,
    energy_total: float,
    T: float,
    grid_size: tuple[int, int] | int,
    gamma_K: float = 0.05,
    phi: Callable[[float], float] = phi_sat,
) -> float:
    """C+E free energy ℱ_C+E[u] = ℰ[u] - T·S(u) + λ_K·K_soft(u).

    With λ_K = γ_K · T (Round 3 §4.3 commit, γ_K ∈ [0.01, 0.1] for φ-sat).

    Parameters
    ----------
    u : cohesion field.
    energy_total : ℰ(u) (compute externally via EnergyComputer).
    T : temperature > 0.
    grid_size : grid spec.
    gamma_K : K_soft scaling coefficient.
    phi : K_soft weighting.

    Returns
    -------
    F_C+E (free energy).
    """
    s = bernoulli_entropy(u)
    ks = k_soft(u, grid_size, phi=phi)
    lambda_K = gamma_K * T
    return energy_total - T * s + lambda_K * ks


def bernoulli_entropy(u: np.ndarray, eps: float = 1e-9) -> float:
    """Bernoulli entropy S(u) = -Σ_x [u(x) log u(x) + (1-u(x)) log(1-u(x))].

    With convention 0 log 0 := 0. Bounded `0 ≤ S ≤ n log 2`.
    """
    u_clip = np.clip(u, eps, 1 - eps)
    return float(-np.sum(u_clip * np.log(u_clip) + (1 - u_clip) * np.log(1 - u_clip)))


def bernoulli_entropy_gradient(u: np.ndarray, eps: float = 1e-9) -> np.ndarray:
    """∇S(u) = -[log u - log(1-u)] = log((1-u)/u) per site."""
    u_clip = np.clip(u, eps, 1 - eps)
    return np.log((1 - u_clip) / u_clip)
