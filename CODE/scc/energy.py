"""Energy functionals and gradients for SCC optimization.

Three independent energy terms (closure, separation, boundary/morphology)
plus transport (deferred). Per the theory, these are conceptually independent
and must not be merged.

Summation convention (Spec §0): sum_{x,y} over ordered pairs.
  => E_bd smoothness = alpha * sum_{x,y} N(x,y)(u(x)-u(y))^2 = 2*alpha * u^T L u
  => Gradient of smoothness = 4*alpha*L*u
  => Hessian of smoothness = 4*alpha*L

Gradient correction from I6: W'(u) = 2u(1-u)(1-2u) — factor of 2.
"""
from __future__ import annotations

import numpy as np
import scipy.sparse as sp

from scc.graph import GraphState
from scc.params import ParameterRegistry
from scc.operators import (
    closure, closure_with_jacobian, closure_jacobian_transpose_vec,
    distinction, distinction_with_jacobian, distinction_jacobian_transpose_vec,
)


# ---------------------------------------------------------------------------
# Double-well potential W(u) = u²(1-u)²
# ---------------------------------------------------------------------------

def double_well(u: np.ndarray) -> np.ndarray:
    return u**2 * (1.0 - u)**2

def double_well_deriv(u: np.ndarray) -> np.ndarray:
    return 2.0 * u * (1.0 - u) * (1.0 - 2.0 * u)

def double_well_second_deriv(c: float) -> float:
    return 2.0 * (1.0 - 6.0 * c + 6.0 * c**2)


# ---------------------------------------------------------------------------
# E_bd: Boundary / morphology energy (Ginzburg-Landau / Allen-Cahn)
# ---------------------------------------------------------------------------

def energy_bd(u: np.ndarray, graph: GraphState, params: ParameterRegistry) -> float:
    """E_bd = alpha*sum_{x,y ordered} N(x,y)(u(x)-u(y))^2 + beta*sum W(u_i).

    Ordered-pair smoothness = 2*alpha * u^T L u  (Spec §0, §8.4).
    """
    Lu = np.asarray(graph.L @ u).ravel()
    smooth = 2.0 * params.alpha_bd * float(u @ Lu)
    well = params.beta_bd * np.sum(double_well(u))
    return float(smooth + well)


def grad_bd(u: np.ndarray, graph: GraphState, params: ParameterRegistry) -> np.ndarray:
    """Gradient of E_bd = 4*alpha*L*u + 2*beta*u*(1-u)*(1-2u).

    Smoothness gradient: d/du[2*alpha*u^T*L*u] = 4*alpha*L*u.
    Double-well gradient: W'(u) = 2u(1-u)(1-2u)  (I6 correction: factor of 2).
    """
    Lu = np.asarray(graph.L @ u).ravel()
    return 4.0 * params.alpha_bd * Lu + params.beta_bd * double_well_deriv(u)


# ---------------------------------------------------------------------------
# E_cl: Closure energy = ||Cl(u) - u||^2
# ---------------------------------------------------------------------------

def energy_cl(u: np.ndarray, graph: GraphState, params: ParameterRegistry) -> float:
    """E_cl = ||Cl_t(u) - u||^2. Measures deviation from closure fixed point."""
    Cl_u = closure(u, graph, params)
    return float(np.sum((Cl_u - u)**2))


def grad_cl(u: np.ndarray, graph: GraphState, params: ParameterRegistry) -> np.ndarray:
    """Gradient of E_cl using exact Jacobian transpose.

    E_cl = ||Cl(u) - u||^2
    ∇E_cl = 2 * (J_Cl - I)^T @ (Cl(u) - u)
          = 2 * (J_Cl^T @ residual - residual)
    """
    Cl_u, sigma_prime, z = closure_with_jacobian(u, graph, params)
    residual = Cl_u - u
    JtR = closure_jacobian_transpose_vec(residual, sigma_prime, graph, params)
    return 2.0 * (JtR - residual)


# ---------------------------------------------------------------------------
# E_sep: Separation energy = sum_i u_i * (1 - D_t(x; 1-u)_i)
# ---------------------------------------------------------------------------

def energy_sep(u: np.ndarray, graph: GraphState, params: ParameterRegistry) -> float:
    """E_sep = sum_i u_i * (1 - D_i). Low when high-u regions are well-distinguished."""
    D_u = distinction(u, graph, params)
    return float(np.sum(u * (1.0 - D_u)))


def grad_sep(u: np.ndarray, graph: GraphState, params: ParameterRegistry) -> np.ndarray:
    """Gradient of E_sep.

    ∇E_sep = (1 - D) - J_D^T @ u  (from R7 algo designer).
    """
    D_u, sigma_prime_D, z_D = distinction_with_jacobian(u, graph, params)
    frozen_part = 1.0 - D_u
    jac_part = distinction_jacobian_transpose_vec(u, sigma_prime_D, graph, params)
    return frozen_part - jac_part


# ---------------------------------------------------------------------------
# Total energy and gradient (dict-based interface for experiments)
# ---------------------------------------------------------------------------

class EnergyComputer:
    """Stateful energy computer for a fixed graph and parameter set.

    Supports optional Hessian normalization: lambda_i = w_i / (sigma_i + eps).
    Before normalization, lambda_i = w_i (the raw weights from params).
    """

    def __init__(self, graph: GraphState, params: ParameterRegistry, lambda_tr: float = 0.0):
        self.graph = graph
        self.params = params
        # Effective weights (start as raw w_i, updated by normalize_weights)
        self.lambda_cl = params.w_cl
        self.lambda_sep = params.w_sep
        self.lambda_bd = params.w_bd
        self.lambda_tr = lambda_tr

    def transport_energy(self, u: np.ndarray, M: np.ndarray, cost: np.ndarray) -> float:
        """E_tr = Σ_{x,y} M(x,y) · c(x,y) — transport mismatch energy."""
        return float(np.sum(M * cost))

    def energy(self, u: np.ndarray, M: np.ndarray | None = None, cost: np.ndarray | None = None) -> tuple[float, dict[str, float]]:
        """Compute total weighted energy and per-term breakdown.

        When M and cost are provided and lambda_tr > 0, includes E_tr.
        """
        terms: dict[str, float] = {}
        E = 0.0
        if self.lambda_bd > 0:
            e = energy_bd(u, self.graph, self.params)
            E += self.lambda_bd * e
            terms['E_bd'] = e
        if self.lambda_cl > 0:
            e = energy_cl(u, self.graph, self.params)
            E += self.lambda_cl * e
            terms['E_cl'] = e
        if self.lambda_sep > 0:
            e = energy_sep(u, self.graph, self.params)
            E += self.lambda_sep * e
            terms['E_sep'] = e
        if self.lambda_tr > 0 and M is not None and cost is not None:
            e = self.transport_energy(u, M, cost)
            E += self.lambda_tr * e
            terms['E_tr'] = e
        terms['E_total'] = E
        return E, terms

    def gradient(self, u: np.ndarray) -> np.ndarray:
        """Compute total weighted gradient (Euclidean).

        NOTE: E_tr gradient w.r.t. u is not included here. The transport
        energy is self-referential (u → fingerprint → cost → M → E_tr),
        so its gradient is handled by the outer fixed-point iteration in
        transport.py, not by direct differentiation.
        """
        g = np.zeros_like(u)
        if self.lambda_bd > 0:
            g += self.lambda_bd * grad_bd(u, self.graph, self.params)
        if self.lambda_cl > 0:
            g += self.lambda_cl * grad_cl(u, self.graph, self.params)
        if self.lambda_sep > 0:
            g += self.lambda_sep * grad_sep(u, self.graph, self.params)
        return g

    def gradient_projected(self, u: np.ndarray) -> np.ndarray:
        """Gradient projected onto T(Sigma_m): g - mean(g)*1."""
        g = self.gradient(u)
        return g - np.mean(g)

    # ------------------------------------------------------------------
    # Hessian normalization (I3-R13 §II, Phase 1)
    # ------------------------------------------------------------------

    def normalize_weights(self, c: float | None = None, eps: float = 1e-8) -> dict[str, float]:
        """Set lambda_i = w_i / (sigma_i + eps) via Hessian spectral norm at u=c*1.

        Returns dict of spectral norms for inspection.
        """
        from scipy.sparse.linalg import eigsh

        if c is None:
            c = self.params.volume_fraction
        n = self.graph.n
        u0 = np.full(n, c)

        # E_bd Hessian is analytic: 4*alpha*L + beta*W''(c)*I
        # Spectral norm = max_k |4*alpha*lambda_k + beta*W''(c)|
        # Must check BOTH lambda_max (largest positive) and lambda_2
        # (where beta*W''(c) < 0 can make the eigenvalue most negative)
        W_pp = double_well_second_deriv(c)
        if n > 3:
            lam_max_L = eigsh(
                self.graph.L.astype(np.float64), k=1, which="LM",
                return_eigenvectors=False,
            )[0]
        else:
            lam_max_L = np.max(np.linalg.eigvalsh(self.graph.L.toarray()))
        lam2_L = self.graph.fiedler  # second-smallest eigenvalue
        eig_at_max = 4.0 * self.params.alpha_bd * lam_max_L + self.params.beta_bd * W_pp
        eig_at_lam2 = 4.0 * self.params.alpha_bd * lam2_L + self.params.beta_bd * W_pp
        sigma_bd = max(abs(eig_at_max), abs(eig_at_lam2))

        # E_cl, E_sep: finite-difference power iteration
        sigma_cl = self._fd_spectral_norm(
            lambda u_: grad_cl(u_, self.graph, self.params), u0
        )
        sigma_sep = self._fd_spectral_norm(
            lambda u_: grad_sep(u_, self.graph, self.params), u0
        )

        norms = {"sigma_cl": sigma_cl, "sigma_sep": sigma_sep, "sigma_bd": sigma_bd}
        self.lambda_cl = self.params.w_cl / (sigma_cl + eps)
        self.lambda_sep = self.params.w_sep / (sigma_sep + eps)
        self.lambda_bd = self.params.w_bd / (sigma_bd + eps)
        return norms

    @staticmethod
    def _fd_spectral_norm(
        grad_fn, u0: np.ndarray, n_iter: int = 30, h: float = 1e-6,
    ) -> float:
        """Estimate Hessian spectral norm via power iteration on finite diffs."""
        g0 = grad_fn(u0)
        n = len(u0)
        rng = np.random.RandomState(0)
        v = rng.randn(n)
        v -= np.mean(v)
        nv = np.linalg.norm(v)
        if nv < 1e-15:
            return 0.0
        v /= nv

        sigma = 0.0
        for _ in range(n_iter):
            g1 = grad_fn(u0 + h * v)
            Hv = (g1 - g0) / h
            Hv -= np.mean(Hv)
            sigma = np.linalg.norm(Hv)
            if sigma < 1e-15:
                break
            v = Hv / sigma
        return sigma


# ---------------------------------------------------------------------------
# Dict-param compatibility wrappers (for test harness)
# ---------------------------------------------------------------------------

def _make_graph_params(N_t, params: dict):
    """Convert raw sparse matrix + dict to GraphState + ParameterRegistry."""
    from scc.operators import _make_graph_params as _mgp
    return _mgp(N_t, params)


def energy_closure(u: np.ndarray, N_t, params: dict) -> float:
    """E_cl — dict-param interface."""
    graph, p = _make_graph_params(N_t, params)
    return energy_cl(u, graph, p)


def energy_separation(u: np.ndarray, N_t, params: dict) -> float:
    """E_sep — dict-param interface."""
    graph, p = _make_graph_params(N_t, params)
    return energy_sep(u, graph, p)


def energy_boundary(u: np.ndarray, N_t, params: dict) -> float:
    """E_bd — dict-param interface. Accepts partial params with just alpha_bd/beta_bd."""
    graph, p = _make_graph_params(N_t, params)
    return energy_bd(u, graph, p)


def energy_total(u: np.ndarray, N_t, params: dict) -> float:
    """E_total — dict-param interface."""
    graph, p = _make_graph_params(N_t, params)
    ec = EnergyComputer(graph, p)
    E, _ = ec.energy(u)
    return E


def grad_closure(u: np.ndarray, N_t, params: dict) -> np.ndarray:
    """∇E_cl — dict-param interface."""
    graph, p = _make_graph_params(N_t, params)
    return grad_cl(u, graph, p)


def grad_separation(u: np.ndarray, N_t, params: dict) -> np.ndarray:
    """∇E_sep — dict-param interface."""
    graph, p = _make_graph_params(N_t, params)
    return grad_sep(u, graph, p)


def grad_boundary(u: np.ndarray, N_t, params: dict) -> np.ndarray:
    """∇E_bd — dict-param interface."""
    graph, p = _make_graph_params(N_t, params)
    return grad_bd(u, graph, p)


def grad_total(u: np.ndarray, N_t, params: dict) -> np.ndarray:
    """∇E_total — dict-param interface."""
    graph, p = _make_graph_params(N_t, params)
    ec = EnergyComputer(graph, p)
    return ec.gradient(u)
