"""Shared fixtures for SCC test suite."""

import numpy as np
import pytest
from scc.graph import GraphState
from scc.params import ParameterRegistry


@pytest.fixture
def rng():
    return np.random.default_rng(42)


@pytest.fixture
def grid_5x5():
    return GraphState.grid_2d(5, 5)


@pytest.fixture
def grid_10x10():
    return GraphState.grid_2d(10, 10)


@pytest.fixture
def grid_20x20():
    return GraphState.grid_2d(20, 20)


@pytest.fixture
def default_params():
    return ParameterRegistry(
        a_cl=3.0, eta_cl=0.5, tau_cl=0.5,
        a_D=5.0, lambda_D=1.0, tau_D=0.0,
        alpha_bd=1.0, beta_bd=10.0,
        w_cl=1.0, w_sep=1.0, w_bd=1.0,
        volume_fraction=0.5,
    )


def make_params(**overrides):
    defaults = dict(
        a_cl=3.0, eta_cl=0.5, tau_cl=0.5,
        a_D=5.0, lambda_D=1.0, tau_D=0.0,
        alpha_bd=1.0, beta_bd=10.0,
        w_cl=1.0, w_sep=1.0, w_bd=1.0,
        volume_fraction=0.5,
    )
    defaults.update(overrides)
    return ParameterRegistry(**defaults)


@pytest.fixture
def bump_field_10x10(grid_10x10):
    """Gaussian bump on 10x10, projected to Sigma_m."""
    n = grid_10x10.n
    size = 10
    c = 0.5
    m = c * n
    u = np.zeros(n)
    cx, cy = size // 2, size // 2
    for i in range(size):
        for j in range(size):
            r2 = (i - cx) ** 2 + (j - cy) ** 2
            u[i * size + j] = np.exp(-r2 / 8.0)
    u = np.clip(u, 0, 1)
    u = u * (m / u.sum())
    u = np.clip(u, 0, 1)
    return u


@pytest.fixture
def two_region_field(grid_10x10):
    """Sharp left=0.95, right=0.05 field."""
    n = grid_10x10.n
    size = 10
    u = np.zeros(n)
    for i in range(size):
        for j in range(size):
            u[i * size + j] = 0.95 if j < size // 2 else 0.05
    return u
