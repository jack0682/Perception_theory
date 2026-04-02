"""Graph infrastructure: adjacency, Laplacian, Fiedler eigenvalue.

Supports both grid graphs and general sparse graphs.
"""

from __future__ import annotations

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla


class GraphState:
    """Encapsulates graph structure and precomputed quantities.

    Attributes:
        W: Sparse symmetric adjacency matrix N_t. Shape (n, n).
        n: Number of nodes.
    """

    def __init__(self, W: sp.spmatrix):
        self.W = sp.csr_matrix(W, dtype=np.float64)
        self.n = self.W.shape[0]
        # Cached quantities
        self._degree: np.ndarray | None = None
        self._laplacian: sp.csr_matrix | None = None
        self._fiedler: float | None = None
        self._P: sp.csr_matrix | None = None  # row-normalized adjacency

    @classmethod
    def grid_2d(cls, rows: int, cols: int, weight: float = 1.0) -> GraphState:
        """Create a 2D grid graph with 4-connectivity."""
        n = rows * cols
        row_idx = []
        col_idx = []
        for r in range(rows):
            for c in range(cols):
                idx = r * cols + c
                if c + 1 < cols:
                    row_idx.extend([idx, idx + 1])
                    col_idx.extend([idx + 1, idx])
                if r + 1 < rows:
                    row_idx.extend([idx, idx + cols])
                    col_idx.extend([idx + cols, idx])
        data = np.full(len(row_idx), weight, dtype=np.float64)
        adj = sp.csr_matrix((data, (row_idx, col_idx)), shape=(n, n))
        return cls(adj)

    @classmethod
    def from_dense(cls, W: np.ndarray) -> GraphState:
        """Create from a dense adjacency matrix."""
        return cls(sp.csr_matrix(W))

    @property
    def degree(self) -> np.ndarray:
        """Degree vector: sum of adjacency weights per node."""
        if self._degree is None:
            self._degree = np.asarray(self.W.sum(axis=1)).ravel()
        return self._degree

    @property
    def L(self) -> sp.csr_matrix:
        """Graph Laplacian L = D - W (sparse)."""
        if self._laplacian is None:
            D = sp.diags(self.degree)
            self._laplacian = (D - self.W).tocsr()
        return self._laplacian

    @property
    def P(self) -> sp.csr_matrix:
        """Row-normalized adjacency: P_t.

        (P_t f)(x) = sum_y N(x,y) f(y) / (sum_y N(x,y) + eps)
        """
        if self._P is None:
            deg = self.degree + 1e-10
            D_inv = sp.diags(1.0 / deg)
            self._P = (D_inv @ self.W).tocsr()
        return self._P

    @property
    def P_1(self) -> np.ndarray:
        """P_t applied to the all-ones vector.

        P_1[x] = sum_y N(x,y) / (sum_y N(x,y) + eps)
        Precomputed for the D_t trick: P_t(1-u) = P_1 - P_t(u).
        """
        return np.asarray(self.P.sum(axis=1)).ravel()

    @property
    def fiedler(self) -> float:
        """Second-smallest eigenvalue of the Laplacian (algebraic connectivity)."""
        if self._fiedler is None:
            if self.n <= 3:
                eigvals = np.sort(np.linalg.eigvalsh(self.L.toarray()))
                self._fiedler = float(eigvals[1]) if len(eigvals) > 1 else 0.0
            else:
                eigvals = spla.eigsh(
                    self.L.astype(np.float64),
                    k=min(3, self.n - 1),
                    which="SM",
                    return_eigenvectors=False,
                )
                eigvals = np.sort(eigvals)
                self._fiedler = float(eigvals[1])
        return self._fiedler

    def fiedler_vector(self) -> np.ndarray:
        """Compute the Fiedler vector (eigenvector for lambda_2)."""
        if self.n <= 3:
            eigvals, eigvecs = np.linalg.eigh(self.L.toarray())
            idx = np.argsort(eigvals)
            return eigvecs[:, idx[1]]
        eigvals, eigvecs = spla.eigsh(
            self.L.astype(np.float64),
            k=min(3, self.n - 1),
            which="SM",
        )
        idx = np.argsort(eigvals)
        return eigvecs[:, idx[1]]

    def spectrum(self, k: int = 10) -> np.ndarray:
        """First k eigenvalues of the Laplacian (smallest to largest).

        Useful for spectral K-selection: counting eigenvalues below the
        phase transition threshold predicts the optimal formation count.
        """
        k = min(k, self.n - 1)
        if self.n <= k + 2:
            eigvals = np.sort(np.linalg.eigvalsh(self.L.toarray()))
            return eigvals[:k]
        eigvals = spla.eigsh(
            self.L.astype(np.float64),
            k=k,
            which="SM",
            return_eigenvectors=False,
        )
        return np.sort(eigvals)

    def cohesion_weighted_symmetric(self, u: np.ndarray) -> sp.csr_matrix:
        """Symmetrized cohesion-weighted adjacency W_sym for resolvent C_t.

        W_sym(x,y) = sqrt(u(x)) * N(x,y) * sqrt(u(y)) / d_x
        then symmetrized: W_sym = 0.5 * (W_norm + W_norm^T).
        """
        sqrt_u = np.sqrt(np.clip(u, 0, 1))
        Su = sp.diags(sqrt_u)
        W_weighted = Su @ self.W @ Su
        deg = np.asarray(W_weighted.sum(axis=1)).ravel() + 1e-10
        D_inv = sp.diags(1.0 / deg)
        W_norm = D_inv @ W_weighted
        W_sym = 0.5 * (W_norm + W_norm.T)
        return W_sym.tocsr()

    def implicit_matrix(self, dt: float, alpha_bd: float) -> sp.csr_matrix:
        """A_imp = I + dt * 4 * alpha_bd * L for semi-implicit stepping.

        The factor of 4 comes from the ordered-pair summation convention:
        E_bd smoothness = alpha * sum_{x,y} N(x,y)(u(x)-u(y))^2 = 2*alpha*u^T L u
        so gradient = 4*alpha*L*u, and Hessian = 4*alpha*L.
        """
        I = sp.eye(self.n, format="csr")
        return I + dt * 4.0 * alpha_bd * self.L
