"""Kramers rates and K-selection Markov chain.

Implements the effective Markov jump process over K_act(t) after
Born-Oppenheimer adiabatic elimination (Canonical Memo v1.1 §T2).

P-F flag: all quantitative claims require stochastic SCC (P-F-A1
Langevin on F_M(P)) to be canonically formalized first.

See: stereo_scc_canonical_memo_v1.1.md §T2, §T3; D7
"""
from __future__ import annotations

import numpy as np


def kramers_rate(
    delta_E: float,
    T_star: float,
    prefactor: float = 1.0,
) -> float:
    """Arrhenius / Kramers escape rate.

    Gamma = prefactor * exp(-delta_E / T_star)

    P-F flag: T_star is undefined until P-F-A1 Langevin is formalized.

    Args:
        delta_E: Barrier height (energy units)
        T_star: Effective Langevin temperature on F_M(P) (P-F-A1; not observation noise)
        prefactor: Eyring-Kramers prefactor A = |lambda_-| / (2*pi) * sqrt(...)

    Returns:
        rate: Transition rate (non-negative)
    """
    if T_star <= 0:
        raise ValueError("T_star must be positive")
    return prefactor * np.exp(-delta_E / T_star)


def build_rate_matrix(
    barriers_down: np.ndarray,
    barriers_up: np.ndarray,
    T_star: float,
    prefactors_down: np.ndarray | None = None,
    prefactors_up: np.ndarray | None = None,
) -> np.ndarray:
    """Build the Markov jump rate matrix Q for K_act dynamics.

    States: K = 0, 1, ..., K_max  (size = K_max + 1)
    Transitions:
      K -> K-1 (merger):  rate = prefactor_down[K] * exp(-barriers_down[K] / T_star)
      K -> K+1 (birth):   rate = prefactor_up[K]   * exp(-barriers_up[K]   / T_star)

    N-1 asymmetry (T5 working hypothesis): barriers_up >> barriers_down at low T_star
    -> merger dominates -> K_act non-increasing on average.

    Args:
        barriers_down: Delta_E for K -> K-1, shape (K_max,) for K=1..K_max
        barriers_up: Delta_E for K -> K+1, shape (K_max,) for K=0..K_max-1
        T_star: Effective temperature
        prefactors_down, prefactors_up: Optional prefactors (default 1.0)

    Returns:
        Q: Rate matrix (K_max+1, K_max+1); Q[i,j] = rate i->j for i!=j;
           Q[i,i] = -sum_j Q[i,j]
    """
    K_max = len(barriers_down)
    n_states = K_max + 1
    Q = np.zeros((n_states, n_states))

    if prefactors_down is None:
        prefactors_down = np.ones(K_max)
    if prefactors_up is None:
        prefactors_up = np.ones(K_max)

    for K in range(1, K_max + 1):
        rate_down = kramers_rate(barriers_down[K - 1], T_star, prefactors_down[K - 1])
        Q[K, K - 1] = rate_down

    for K in range(0, K_max):
        rate_up = kramers_rate(barriers_up[K], T_star, prefactors_up[K])
        Q[K, K + 1] = rate_up

    # Diagonal: -sum of off-diagonal rates
    for i in range(n_states):
        Q[i, i] = -Q[i, :].sum() + Q[i, i]  # avoids double-subtracting diagonal

    return Q


def simulate_markov_chain(
    Q: np.ndarray,
    K_init: int,
    t_max: float,
    rng: np.random.Generator | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    """Gillespie simulation of the K_act Markov chain.

    Simulates exact CTMC trajectories using the Gillespie (direct) algorithm.

    Args:
        Q: Rate matrix (n_states, n_states)
        K_init: Initial state
        t_max: Maximum simulation time
        rng: Random number generator (default: new default_rng)

    Returns:
        times: Jump times, shape (n_jumps+1,) starting at 0
        states: State values, shape (n_jumps+1,) starting at K_init
    """
    if rng is None:
        rng = np.random.default_rng(42)

    times = [0.0]
    states = [K_init]
    t = 0.0
    K = K_init
    n_states = Q.shape[0]

    while t < t_max:
        # Total escape rate from current state
        rate_total = -Q[K, K]
        if rate_total < 1e-12:
            # Absorbing state
            times.append(t_max)
            states.append(K)
            break

        # Time to next event
        dt = rng.exponential(1.0 / rate_total)
        t = t + dt
        if t >= t_max:
            break

        # Choose next state
        off_diag_rates = Q[K, :].copy()
        off_diag_rates[K] = 0.0
        probs = off_diag_rates / off_diag_rates.sum()
        K_next = rng.choice(n_states, p=probs)

        times.append(t)
        states.append(K_next)
        K = K_next

    return np.array(times), np.array(states)


def stationary_distribution(Q: np.ndarray) -> np.ndarray:
    """Compute stationary distribution pi of CTMC with rate matrix Q.

    Solves pi Q = 0, sum(pi) = 1 via null-space of Q^T.

    Args:
        Q: Rate matrix (n_states, n_states)

    Returns:
        pi: Stationary distribution, shape (n_states,)
    """
    n = Q.shape[0]
    # Build system: Q^T pi = 0, sum(pi) = 1
    A = Q.T.copy()
    A[-1, :] = 1.0  # replace last equation with normalization
    b = np.zeros(n)
    b[-1] = 1.0
    pi = np.linalg.solve(A, b)
    pi = np.abs(pi)
    pi /= pi.sum()
    return pi


def free_energy_from_barriers(
    barriers_down: np.ndarray,
    barriers_up: np.ndarray,
    T_star: float,
) -> np.ndarray:
    """Effective free energy F(K) from detailed balance.

    Under detailed balance: P_eq(K) / P_eq(K-1) = rate_{K-1->K} / rate_{K->K-1}

    Args:
        barriers_down: Merger barriers, shape (K_max,) for K=1..K_max
        barriers_up: Birth barriers, shape (K_max,) for K=0..K_max-1
        T_star: Effective temperature

    Returns:
        F_rel: F(K) - F(0), shape (K_max+1,) [free energy relative to K=0]
    """
    K_max = len(barriers_down)
    log_ratios = []
    for K in range(1, K_max + 1):
        # log(rate_{K-1->K} / rate_{K->K-1}) = -(E_up[K-1] - E_down[K-1]) / T_star
        log_ratio = -(barriers_up[K - 1] - barriers_down[K - 1]) / T_star
        log_ratios.append(log_ratio)

    # log P_eq(K) = log P_eq(0) + sum_{j=0}^{K-1} log_ratios[j]
    log_P_rel = np.zeros(K_max + 1)
    for K in range(1, K_max + 1):
        log_P_rel[K] = log_P_rel[K - 1] + log_ratios[K - 1]

    F_rel = -T_star * log_P_rel
    F_rel -= F_rel.min()
    return F_rel
