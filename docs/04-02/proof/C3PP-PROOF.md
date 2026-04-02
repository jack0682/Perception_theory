# Proof of Axiom C3'' (Local Monotonicity of Co-Belonging Diagonal)

**Status:** Complete proof, closing the gap identified in Canonical Spec v2.1 SS13.  
**Date:** 2026-04-02  
**References:** Horn & Johnson, *Matrix Analysis* (2013), Ch. 6; Berman & Plemmons, *Nonneg. Matrices in the Mathematical Sciences* (1994), Ch. 6.

---

## 1. Statement

**Axiom C3'' (Local Monotonicity).** Let $G = (V, E)$ be a finite connected graph with symmetric adjacency $N$, and let $u : V \to [0,1]$ be a cohesion field. Define the resolvent co-belonging operator

$$\mathbf{C}_t = (I - \alpha\, W_{\mathrm{sym}})^{-1}$$

where $W_{\mathrm{sym}} = D_u^{-1/2}\, W_u\, D_u^{-1/2}$ is the symmetrically normalized cohesion-weighted adjacency (see SS2 below), and $\alpha \cdot \rho(W_{\mathrm{sym}}) < 1$.

**Claim.** $\mathbf{C}_t(x,x)$ is monotone non-decreasing in $u(x)$ with all other field values held fixed. The inequality is strict whenever $x$ has at least one neighbor $j$ with $u(j) > 0$.

---

## 2. Setup and Notation

**Cohesion-weighted adjacency.** For a field $u : V \to [0,1]$:

$$W_u(i,j) = \sqrt{u(i)}\; N(i,j)\; \sqrt{u(j)}$$

**Degree matrix.** $D_u = \mathrm{diag}(d)$ where $d(i) = \sum_j W_u(i,j)$.

**Symmetric normalization.** $W_{\mathrm{sym}} = D_u^{-1/2}\, W_u\, D_u^{-1/2}$, so $W_{\mathrm{sym}}(i,j) = W_u(i,j) / \sqrt{d(i)\, d(j)}$.

**Parametrization.** Fix all $u(j)$ for $j \neq x$ and set $u(x) = s^2$ where $s = \sqrt{u(x)} \geq 0$. Define:

- $N_x = \{j \in V : N(x,j) > 0\}$ (neighbors of $x$),
- $w_j = N(x,j) \sqrt{u(j)}$ for $j \in N_x$ (fixed quantities),
- $\sigma = \sum_{j \in N_x} w_j$ (fixed),
- $d(x) = s \cdot \sigma$,
- For $j \in N_x$: $d(j) = d_j^{\mathrm{rest}} + s \cdot w_j$ where $d_j^{\mathrm{rest}} = \sum_{k \neq x} W_u(j,k)$ is independent of $s$.

---

## 3. Conjugation Identity

Since $W_{\mathrm{sym}} = D^{-1/2} W_u D^{-1/2}$, we have $I - \alpha W_{\mathrm{sym}} = D^{-1/2}(D - \alpha W_u) D^{-1/2}$, hence:

$$\mathbf{C}_t = D^{1/2}\, H^{-1}\, D^{1/2}$$

where $H = D - \alpha W_u$. Taking the $(x,x)$ entry:

$$\boxed{\mathbf{C}_t(x,x) = d(x) \cdot [H^{-1}](x,x)}$$

**Structure of $H$.** The matrix $H$ is a Z-matrix (nonpositive off-diagonal) with:
- $H(i,i) = d(i)$ (positive diagonal),
- $H(i,j) = -\alpha\, W_u(i,j) \leq 0$ for $i \neq j$.

Since $\alpha\, \rho(W_{\mathrm{sym}}) < 1$ implies $\alpha < 1$ (as $\rho(W_{\mathrm{sym}}) \leq 1$ for the normalized form), $H$ is strictly diagonally dominant, hence a nonsingular M-matrix with $H^{-1} \geq 0$ (entrywise nonneg). [Berman & Plemmons, Thm 6.2.3]

---

## 4. Schur Complement Formula

Partition the index set as $\{x\} \cup (V \setminus \{x\})$. By the Schur complement for $(x,x)$ entries of $H^{-1}$:

$$[H^{-1}](x,x) = \frac{1}{H(x,x) - \mathbf{h}_x^T\, G^{-1}\, \mathbf{h}_x}$$

where:
- $\mathbf{h}_x = H_{V \setminus \{x\}, x} = (-\alpha\, s\, w_j)_{j \in N_x}$ (padded with zeros for non-neighbors),
- $G = H_{V \setminus \{x\},\, V \setminus \{x\}}$ (the principal submatrix of $H$ excluding row/column $x$).

Define the weight vector $\mathbf{w} = (w_j)_{j \in N_x}$ (padded with zeros). Then $\mathbf{h}_x = -\alpha s\, \mathbf{w}$ and:

$$\mathbf{h}_x^T G^{-1} \mathbf{h}_x = \alpha^2 s^2\, \mathbf{w}^T G^{-1} \mathbf{w}$$

Substituting $H(x,x) = s\sigma$ and $d(x) = s\sigma$:

$$\mathbf{C}_t(x,x) = \frac{s\sigma}{s\sigma - \alpha^2 s^2\, \mathbf{w}^T G^{-1} \mathbf{w}} = \frac{\sigma}{\sigma - \alpha^2 s\, \mathbf{w}^T G(s)^{-1} \mathbf{w}}$$

Define:

$$f(s) \;=\; s \cdot \mathbf{w}^T G(s)^{-1} \mathbf{w}$$

so that $\mathbf{C}_t(x,x) = \sigma / (\sigma - \alpha^2 f(s))$.

Since $\sigma > 0$ and $\alpha^2 f(s) < \sigma$ (by convergence), $\mathbf{C}_t(x,x)$ is a strictly increasing function of $f(s)$.

**Therefore, C3'' reduces to showing $f'(s) \geq 0$.**

---

## 5. Monotonicity of $f(s)$

### 5.1. Structure of $G(s)$

The submatrix $G = H_{-x,-x}$ depends on $s$ only through the diagonal entries at neighbors of $x$:

$$G(s) = G_0 + s\, \Delta$$

where:
- $G_0$ is $G$ evaluated at $s = 0$: has diagonal $G_0(j,j) = d_j^{\mathrm{rest}}$ for $j \in N_x$ and $G_0(j,j) = d(j)$ for $j \notin N_x$; off-diagonal $G_0(i,j) = -\alpha\, W_u(i,j)$ (independent of $s$),
- $\Delta = \mathrm{diag}(w_j \cdot \mathbf{1}_{j \in N_x})$ (nonneg diagonal, zero outside $N_x$).

Both $G_0$ and $G(s)$ are nonsingular M-matrices for all $s \geq 0$ (diagonal dominance: $G_0(j,j) = d_j^{\mathrm{rest}} > \alpha\, d_j^{\mathrm{rest}} = \alpha \sum_{k \neq x} W_u(j,k) \geq |\text{off-diag row sum}|$, since $\alpha < 1$).

### 5.2. Derivative Computation

$$f(s) = s \cdot \mathbf{w}^T G(s)^{-1} \mathbf{w}$$

$$f'(s) = \mathbf{w}^T G(s)^{-1} \mathbf{w} + s \cdot \mathbf{w}^T \frac{d}{ds}\big[G(s)^{-1}\big] \mathbf{w}$$

Using the matrix derivative $\frac{d}{ds} G^{-1} = -G^{-1}\, \Delta\, G^{-1}$:

$$f'(s) = \mathbf{w}^T G^{-1} \mathbf{w} - s \cdot \mathbf{w}^T G^{-1} \Delta\, G^{-1} \mathbf{w}$$

Define $\mathbf{v} = G(s)^{-1} \mathbf{w} \geq 0$ (nonneg by M-matrix inverse). Then:

$$f'(s) = \mathbf{w}^T \mathbf{v} - s \cdot \mathbf{v}^T \Delta\, \mathbf{v}$$

Substitute $\mathbf{w} = G(s)\, \mathbf{v} = (G_0 + s\Delta)\, \mathbf{v}$:

$$\mathbf{w}^T \mathbf{v} = \mathbf{v}^T (G_0 + s\Delta)\, \mathbf{v} = \mathbf{v}^T G_0\, \mathbf{v} + s \cdot \mathbf{v}^T \Delta\, \mathbf{v}$$

Therefore:

$$\boxed{f'(s) = \mathbf{v}^T G_0\, \mathbf{v}}$$

### 5.3. Positive-Definiteness of $G_0$

We decompose $G_0$:

$$G_0 = (1 - \alpha)\, D_0 + \alpha\, L_0$$

where:
- $D_0 = \mathrm{diag}(G_0(j,j))$ is the degree matrix of the restricted graph (positive diagonal),
- $L_0 = D_0 - W_0$ is the graph Laplacian of $W_u$ restricted to $V \setminus \{x\}$, with $W_0(i,j) = W_u(i,j)$ for $i,j \neq x$.

**The graph Laplacian $L_0$ is positive semidefinite** (standard: $\mathbf{v}^T L_0\, \mathbf{v} = \tfrac{1}{2} \sum_{i,j \neq x} W_u(i,j)(v_i - v_j)^2 \geq 0$).

**The diagonal $(1-\alpha)\, D_0$ is positive definite** since $1 - \alpha > 0$ (from $\alpha < 1$) and all diagonal entries $d_j^{\mathrm{rest}} > 0$ (each vertex $j \in N_x$ has positive degree in the restricted graph, since $w_j > 0$ requires $u(j) > 0$, ensuring $j$ participates in the weighted graph).

Therefore $G_0 = (1-\alpha) D_0 + \alpha L_0$ is positive definite, and:

$$f'(s) = \mathbf{v}^T G_0\, \mathbf{v} > 0 \quad \text{whenever } \mathbf{v} \neq 0$$

Since $\mathbf{v} = G(s)^{-1} \mathbf{w} \neq 0$ (because $\mathbf{w} \neq 0$ and $G(s)$ is nonsingular), we conclude $f'(s) > 0$ for all $s > 0$.

---

## 6. Conclusion

Since $f'(s) > 0$, the function $f(s) = s\, \mathbf{w}^T G(s)^{-1} \mathbf{w}$ is strictly increasing for $s > 0$, and therefore:

$$\mathbf{C}_t(x,x) = \frac{\sigma}{\sigma - \alpha^2 f(s)}$$

is strictly increasing in $s = \sqrt{u(x)}$, hence strictly increasing in $u(x)$.

**Boundary cases:**
- $u(x) = 0$: $f(0) = 0$, so $\mathbf{C}_t(x,x) = 1$ (the identity contribution).
- $x$ isolated ($N_x = \varnothing$): $\sigma = 0$, the $x$-row/column of $W_{\mathrm{sym}}$ is zero, so $\mathbf{C}_t(x,x) = 1$ identically (trivially non-decreasing).

**Axiom C3'' is proved.** $\quad\blacksquare$

---

## 7. Discussion

### 7.1. Why the Gap Was Non-Trivial

The original Neumann-series argument observed that each term $[W_{\mathrm{sym}}^k](x,x)$ counts length-$k$ closed walks from $x$, weighted by products of $W_{\mathrm{sym}}$ entries. Increasing $u(x)$ increases the entries $W_{\mathrm{sym}}(x,j)$ for neighbors $j$, suggesting each term increases. The gap: increasing $u(x)$ also *decreases* entries $W_{\mathrm{sym}}(i,j)$ for pairs $(i,j)$ where both $i,j$ are neighbors of $x$ but neither equals $x$, due to the degree normalization (their row/column degrees increase, diluting the normalized weight). So individual Neumann terms are not monotone.

The resolution is to avoid term-by-term analysis entirely. The conjugation identity $\mathbf{C}_t(x,x) = d(x) \cdot [H^{-1}](x,x)$ absorbs the degree normalization into a multiplicative factor, and the Schur complement formula isolates the $u(x)$-dependence into a single scalar function $f(s)$ whose derivative has a clean positive-definite quadratic form.

### 7.2. The Key Algebraic Cancellation

The central computation (SS5.2) produces a remarkable cancellation: in $f'(s) = \mathbf{w}^T \mathbf{v} - s \cdot \mathbf{v}^T \Delta \mathbf{v}$, substituting $\mathbf{w} = (G_0 + s\Delta)\mathbf{v}$ yields $f'(s) = \mathbf{v}^T G_0 \mathbf{v}$, which is manifestly nonneg by the PD structure of $G_0$. The $s\Delta$ terms cancel exactly. This is why the result holds for *all* valid $\alpha$, not just small $\alpha$.

### 7.3. Code Discrepancy

The current implementation (`scc/graph.py:140-153`) uses *arithmetic-mean symmetrization*:

$$W_{\mathrm{sym}}^{\mathrm{code}}(i,j) = \tfrac{1}{2}\, W_u(i,j)\Big(\frac{1}{d(i)} + \frac{1}{d(j)}\Big)$$

while this proof uses the *geometric-mean (D^{-1/2}) symmetrization*:

$$W_{\mathrm{sym}}^{\mathrm{spec}}(i,j) = \frac{W_u(i,j)}{\sqrt{d(i)\, d(j)}}$$

The D^{-1/2} form admits the conjugation $I - \alpha W_{\mathrm{sym}} = D^{-1/2}(D - \alpha W_u)D^{-1/2}$, which is essential for the proof. The arithmetic-mean form does not factor this way.

**Recommendation:** Update `GraphState.cohesion_weighted_symmetric` to use `D^{-1/2} W_u D^{-1/2}`, aligning the code with the spec's D^{-1/2} convention and ensuring C3'' holds for the implemented operator. This is a one-line change:

```python
# Current:
D_inv = sp.diags(1.0 / deg)
W_norm = D_inv @ W_weighted
W_sym = 0.5 * (W_norm + W_norm.T)

# Proposed:
D_inv_sqrt = sp.diags(1.0 / np.sqrt(deg))
W_sym = D_inv_sqrt @ W_weighted @ D_inv_sqrt
```

### 7.4. Conditions and Scope

The proof requires:
1. $\alpha < 1$ (automatic from the convergence condition $\alpha \rho(W_{\mathrm{sym}}) < 1$ since $\rho \leq 1$ for the normalized form).
2. $N(x,j) \geq 0$ (nonneg adjacency; holds by construction).
3. Strict monotonicity requires $x$ to have at least one neighbor $j$ with $u(j) > 0$. For isolated vertices or vertices surrounded by $u = 0$, $\mathbf{C}_t(x,x) = 1$ identically.

No assumptions on graph topology (trees, grids, general graphs all covered), dimensionality, or field smoothness are needed. The result is purely algebraic.
