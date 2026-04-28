"""Parameter registry with validation for SCC.

All constraints from Canonical Spec v2.0 and I3-R13 synthesis.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class ParameterRegistry:
    """Complete parameter set for the SCC pipeline.

    Tier 1: Theoretically constrained (must satisfy or theory breaks).
    Tier 2: Theoretically motivated defaults.
    Tier 3: Empirically determined.
    """

    # --- Closure (Spec §9.2) ---
    a_cl: float = 3.5       # steepness; MUST be < 4 for A3 contraction
    eta_cl: float = 0.5     # self-retention vs neighbor balance [0,1]
    tau_cl: float = 0.5     # closure threshold

    # --- Distinction (Spec §9.3) ---
    a_D: float = 5.0        # asymmetry sensitivity
    lambda_D: float = 1.0   # interior/exterior weighting
    tau_D: float = 0.0      # distinction threshold
    b_D: float = 0.0        # gradient term; MUST be 0 for analyticity (T14)

    # --- Co-belonging / Resolvent (Spec §9.4) ---
    alpha_C: float = 0.5    # resolvent parameter; alpha_C * rho(W_sym) < 1
    k_neumann: int = 10     # Neumann series truncation

    # --- Energy weights (Spec §8.1) ---
    w_cl: float = 1.0       # closure energy weight (pre-normalization)
    w_sep: float = 1.0      # separation energy weight
    w_bd: float = 1.0       # boundary/morphology energy weight

    # --- Boundary/morphology (Spec §8.4) ---
    alpha_bd: float = 1.0   # smoothness weight
    beta_bd: float = 10.0   # double-well weight; must satisfy T8-Core

    # --- Volume constraint (Spec §8.0) ---
    volume_fraction: float = 0.3  # c = m/n; must be in spinodal (0.211, 0.789)

    # --- Optimizer ---
    dt_init: float = 0.01
    max_iter: int = 10_000
    n_restarts: int = 5
    k_diag: int = 100
    eps_energy: float = 1e-6  # relative energy change threshold
    eps_field: float = 1e-6
    eps_grad: float = 1e-3  # box-aware KKT residual threshold
    eps_init: float = 0.01  # Gaussian perturbation scale

    # --- Thresholds for crisp recovery (Spec §5) ---
    theta_core: float = 0.9
    theta_in: float = 0.5
    theta_bd_lo: float = 0.2
    theta_bd_hi: float = 0.8
    theta_ext: float = 0.1

    # --- Transport (Spec §8.5, §10) ---
    w_tr: float = 0.5            # transport energy base weight (before normalization)
    sigma_transport: float = 1.0  # spatial tolerance for transport cost
    gamma_transport: float = 1.0  # fingerprint weight for transport cost
    eps_ot: float = 1.0           # entropic regularization for OT (>0)

    # --- Aggregation stabilization ---
    eps_agg: float = 1e-10  # division-by-zero guard in P_t

    def validate(
        self,
        fiedler_eigenvalue: float | None = None,
        spectral_radius_W_sym: float | None = None,
        allow_outside_spinodal: bool = False,
    ) -> Tuple[bool, List[str], List[str]]:
        """Validate all parameter constraints.

        Args:
            fiedler_eigenvalue: optional second-smallest Laplacian eigenvalue
            spectral_radius_W_sym: optional spectral radius of cohesion-weighted Laplacian
            allow_outside_spinodal: if True, demote spinodal-range violation from
                FATAL to WARNING. Used for IC-driven metastable-stationary studies
                (e.g., σ-framework Hessian analysis at small c, NQ-191).
                Default False preserves variational-use semantics.

        Returns (valid, violations, warnings).
        """
        V: List[str] = []
        W: List[str] = []

        # A3 contraction
        if self.a_cl >= 4.0:
            V.append(
                f"FATAL: a_cl={self.a_cl} >= 4 — A3 contraction violated. "
                "Closure not guaranteed to converge."
            )

        # Transport parameter constraints
        if self.eps_ot <= 0:
            V.append(
                f"FATAL: eps_ot={self.eps_ot} <= 0 — entropic regularization "
                "must be strictly positive for Sinkhorn convergence."
            )
        if self.sigma_transport <= 0:
            V.append(
                f"FATAL: sigma_transport={self.sigma_transport} <= 0 — "
                "spatial tolerance must be strictly positive."
            )
        if self.gamma_transport < 0:
            V.append(
                f"FATAL: gamma_transport={self.gamma_transport} < 0 — "
                "fingerprint weight must be non-negative."
            )
        if not (0 < self.theta_core < 1):
            V.append(
                f"FATAL: theta_core={self.theta_core} not in (0,1) — "
                "core threshold must be strictly between 0 and 1."
            )

        # Analyticity (T14)
        if self.b_D != 0:
            V.append(
                f"FATAL: b_D={self.b_D} != 0 — energy not analytic. "
                "Gradient flow convergence (T14) not guaranteed."
            )

        # Spinodal range
        c = self.volume_fraction
        import math

        c_lo = (3 - math.sqrt(3)) / 6  # ~0.2113
        c_hi = (3 + math.sqrt(3)) / 6  # ~0.7887
        if not (c_lo < c < c_hi):
            msg = (
                f"c={c:.3f} outside spinodal ({c_lo:.3f}, {c_hi:.3f}). "
                "No spontaneous phase separation; metastable formations only via "
                "prepared IC (σ-framework Hessian use)."
            )
            if allow_outside_spinodal:
                W.append(f"WARNING (allow_outside_spinodal=True): {msg}")
            else:
                V.append(f"FATAL: {msg} Set allow_outside_spinodal=True to bypass for metastable use.")

        # Resolvent convergence
        if spectral_radius_W_sym is not None:
            if self.alpha_C * spectral_radius_W_sym >= 1.0:
                V.append(
                    f"FATAL: alpha_C*rho = {self.alpha_C * spectral_radius_W_sym:.3f} >= 1 — "
                    f"resolvent diverges. Reduce alpha_C below {1.0/spectral_radius_W_sym:.4f}."
                )

        # T8-Core phase transition
        if fiedler_eigenvalue is not None:
            W_pp = 2 * (1 - 6 * c + 6 * c**2)  # W''(c) for W(u) = u^2(1-u)^2
            if abs(W_pp) > 1e-12:
                beta_crit = 4 * self.alpha_bd * fiedler_eigenvalue / abs(W_pp)
                if self.beta_bd <= beta_crit:
                    V.append(
                        f"FATAL: beta_bd={self.beta_bd:.2f} <= beta_crit={beta_crit:.2f} — "
                        "uniform state is global minimizer. No formation possible (T8-Core)."
                    )

        # Quality warnings
        if self.a_D <= abs(self.tau_D):
            W.append(
                f"WARNING: a_D={self.a_D} <= |tau_D|={abs(self.tau_D)} — "
                "distinction operator may be near-zero everywhere."
            )

        if spectral_radius_W_sym is not None:
            neumann_error = (self.alpha_C * spectral_radius_W_sym) ** (self.k_neumann + 1)
            if neumann_error > 0.01:
                W.append(
                    f"WARNING: Neumann error bound = {neumann_error:.4f} > 1%. "
                    "Increase k_neumann or decrease alpha_C."
                )

        return len(V) == 0, V, W

    @property
    def spinodal_bounds(self) -> Tuple[float, float]:
        import math
        return (3 - math.sqrt(3)) / 6, (3 + math.sqrt(3)) / 6

    def beta_critical(self, fiedler_eigenvalue: float) -> float:
        """Compute the critical beta for phase transition (T8-Core)."""
        c = self.volume_fraction
        W_pp = 2 * (1 - 6 * c + 6 * c**2)
        if abs(W_pp) < 1e-12:
            return float("inf")
        return 4 * self.alpha_bd * fiedler_eigenvalue / abs(W_pp)
