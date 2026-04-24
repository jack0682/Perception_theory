# 02_development.md — Definitions, Lemmas, Proofs (Primary Approach Deep Development)

**Session:** 2026-04-24
**Target (from plan.md):** Orbital structure 의 SCC-intrinsic 정의 + Cat A 승급 작업.
**This file covers:** §4.4 의 primary 접근 심층 전개. **A1 (irrep) + A2 (nodal) + A6 (axiomatic σ) 합성**, A3 (continuum) 부수, A5 (frustration) 부분 사용. 정의, 보조정리, 정리, 명시적 반례 시도, 자체 Cat 분류.
**Depends on reading:** `01_exploration.md` (이 세션의 §1–§3); `canonical.md` §3, §13 (T-Birth-Parametric, Prop 1.3a/b 는 working 에서 구체); `working/SF/mode_count.md` §1–§2; `working/SF/symmetry_moduli.md` §1–§3.

---

## §1. Setup and notation

### 1.1 Graph and field structure

$G = (X, E)$ 는 finite simple connected graph, $n = |X|$. Adjacency matrix $A$, degree matrix $D = \text{diag}(d_i)$, **combinatorial Laplacian** $L = D - A$ (PSD, $L \mathbf{1} = 0$, eigenvalues $0 = \lambda_1 < \lambda_2 \leq \cdots \leq \lambda_n$). 모든 site index $i \in X$.

**Volume-constrained simplex:** for $m \in (0, n)$,
$$\Sigma_m := \Big\{u \in [0,1]^X : \sum_i u_i = m\Big\}.$$
$\Sigma_m$ 의 interior 는 convex polytope (codim 1, dim $n-1$). 어느 internal point $u$ 에서 tangent space $T_u \Sigma_m = \{v \in \mathbb{R}^X : \sum_i v_i = 0\} = \mathbf{1}^\perp$.

### 1.2 Energy and Hessian

$\mathcal{E} : \Sigma_m \to \mathbb{R}$, $\mathcal{E} = \lambda_\text{cl} \mathcal{E}_\text{cl} + \lambda_\text{sep} \mathcal{E}_\text{sep} + \mathcal{E}_\text{bd} (+ \lambda_\text{tr} \mathcal{E}_\text{tr})$. (이 세션은 single-time formation 분석 → $\mathcal{E}_\text{tr}$ 부재로 가정.)

$u^*$ 가 $\mathcal{E}$ 의 local minimizer 이면 unconstrained Hessian $\mathbf{H}(u^*) := \nabla^2 \mathcal{E}(u^*) \in \mathbb{R}^{X \times X}$ 의 $T_{u^*}\Sigma_m = \mathbf{1}^\perp$ 위로의 restriction
$$H(u^*) := \pi_{\mathbf{1}^\perp} \mathbf{H}(u^*) \pi_{\mathbf{1}^\perp},\qquad \pi_{\mathbf{1}^\perp} = I - \tfrac{1}{n}\mathbf{1}\mathbf{1}^\top$$
의 spectrum 을 분석한다. **Morse index 0 minimizer** 의 정의: $H(u^*)|_{\mathbf{1}^\perp} \succeq 0$ 그리고 모든 nonzero eigenvalue $> 0$.

### 1.3 Group action

$\Gamma := \text{Aut}(G) = \{\pi \in S_n : (i,j) \in E \iff (\pi(i), \pi(j)) \in E\}$. $\pi \in \Gamma$ 가 $\mathbb{R}^X$ 에 $(\pi \cdot u)_i := u_{\pi^{-1}(i)}$ 로 작용. 이 action 은 $\Sigma_m$, $\mathbf{1}^\perp$, $\mathcal{E}$ 를 보존 (graph-symmetric).

**Stabilizer:** $u^* \in \Sigma_m$ 의 stabilizer $S(u^*) := \{\pi \in \Gamma : \pi \cdot u^* = u^*\} \leq \Gamma$. $S(u^*)$ 는 $\mathbf{H}(u^*)$ 와 commute → eigenspaces 는 $S(u^*)$-invariant.

**Examples** (canonical):
- $L \times L$ free-BC grid: $\Gamma = D_4$ (4 rot + 4 refl, $|\Gamma| = 8$).
- $L \times L$ torus: $\Gamma = D_4 \ltimes (\mathbb{Z}_L)^2$ ($|\Gamma| = 8L^2$).
- $C_n$ cycle: $\Gamma = D_n$.
- 일반 random graph: $\Gamma = \{e\}$.

---

## §2. Definition: Cohesion Signature σ

이 절은 A6 의 합성. 정의는 graph-intrinsic, axiom 후보 (S1') 의 statement 안에서 사용 예정.

### 2.1 Constituent objects

$u^* \in \Sigma_m$ 가 $\mathcal{E}$ 의 Morse-index-0 local minimum 이라 가정. 다음 객체들을 차례로 정의:

**(O1) Local-maxima count** ($\mathcal{F}$).
$$\mathcal{F}(u^*) := \#\{i \in X : u^*(i) > u^*(j) \text{ for all } j \sim i\}.$$
$\mathcal{F}(u^*) \in \mathbb{Z}_{\geq 0}$. **Threshold-independent**, **graph-intrinsic**, **Aut(G)-invariant** (왜냐하면 $u^*$ 와 graph adjacency $\sim$ 가 모두 $\Gamma$-equivariant).

**(O2) Hessian eigenstructure**. $H(u^*)$ 의 spectrum (with multiplicity) $0 \leq \lambda_0(u^*) \leq \lambda_1(u^*) \leq \cdots$ on $\mathbf{1}^\perp$. (Morse-0 가정 하에 모든 $\lambda_k > 0$ 이지만, 일부 $\lambda_k$ 는 0 에 매우 가까울 수 있음 — Goldstone-like.) 대응하는 정규직교 eigenvectors $\phi_0, \phi_1, \ldots, \phi_{n-2}$ in $\mathbf{1}^\perp$.

**(O3) Spectral cutoff** ($K$). 어떤 자연수 $K \leq n - 1$ 까지의 mode 만 σ 에 포함. $K$ 는 다음 중 한 방식으로 결정:
- (옵션 K-A) **Spectral gap cutoff**: $K = \min\{k : \lambda_k > c \cdot \lambda_{0+}\}$ where $\lambda_{0+}$ is smallest non-Goldstone eigenvalue and $c > 1$ a fixed multiple (e.g. $c = 10$).
- (옵션 K-B) **Sub-extensive cutoff**: $K = K_0$ a fixed small constant (e.g. $K = 20$ matching pre_brainstorm §3).
- (옵션 K-C) **Adaptive nodal cutoff**: $K = \max\{k : \mathcal{N}(\phi_k) \leq c_n \cdot \log n\}$ for some $c_n$.

이 cutoff 의 임의성은 σ-정의의 약점 (§01 §2 A6 (c1)). 본 문서는 (K-A) 를 default 로 사용 (이유: 물리적 의미 ─ "Goldstone band 위 첫 spectral gap 까지의 'shell band'").

**(O4) Nodal count** ($n_k$). Each $\phi_k$ 의 nodal count
$$\mathcal{N}(\phi_k) := \#\{\text{connected components of } \{i : \phi_k(i) > 0\}\} + \#\{\text{c.c. of } \{i : \phi_k(i) < 0\}\}.$$
("Connected" 는 graph-induced 부분그래프 위에서.) $\phi_k(i) = 0$ 인 site 는 두 sign 영역 어디에도 포함하지 않음 (boundary). $n_k := \mathcal{N}(\phi_k) \in \mathbb{Z}_{\geq 1}$.

**(O5) Irrep label** ($[\rho_k]$). $S(u^*)$ 가 $\mathbf{1}^\perp$ 에 작용. $\phi_k$ 의 eigenspace $V_k := \ker(H - \lambda_k I)|_{\mathbf{1}^\perp}$ 가 $S(u^*)$-invariant, 따라서 $S(u^*)$ 의 representation 으로 분해
$$V_k = \bigoplus_{[\rho] \in \widehat{S(u^*)}} m_{k,\rho} \cdot V_\rho.$$
$\phi_k$ 가 simple eigenvector ($\dim V_k = 1$) 이면 $V_k$ 는 1-dim irrep 이고 $[\rho_k] := [V_\rho]$. $\dim V_k > 1$ 이면 isotypic decomposition 의 한 component 를 (eigenvector 의 group-equivariant Gram-Schmidt 로) canonical 선택 — see §3 Lemma 2 detail.

**(O6) Eigenvalue** ($\lambda_k$). 위 $H(u^*)$ 의 $k$-th eigenvalue.

### 2.2 The signature

> **Definition (Cohesion Signature).** Morse-index-0 local minimizer $u^* \in \Sigma_m$ 의 **cohesion signature** 는
> $$\sigma(u^*) \;:=\; \big(\mathcal{F}(u^*);\; \{(n_k, [\rho_k], \lambda_k)\}_{k=0}^{K-1}\big),$$
> 여기서 $K$ 는 (O3) 의 옵션 중 하나로 고정된 cutoff. $\{(n_k, [\rho_k], \lambda_k)\}$ 는 $k$ 에 대한 ordered tuple (sorted by eigenvalue ascending, ties broken lexicographically by $(n_k, [\rho_k])$).

### 2.3 Equivalence

> **Definition (Signature equivalence).** 두 local minimizer $u^*, u^{*\prime}$ 가 **σ-equivalent**, 표기 $u^* \sim_\sigma u^{*\prime}$, 는 만약 $\sigma(u^*) = \sigma(u^{*\prime})$ as ordered tuples (with $[\rho_k]$ compared up to $\Gamma$-conjugation of stabilizer subgroups).

**Aut(G)-action 과의 양립.** $\pi \cdot u^*$ 의 signature 는 $u^*$ 의 signature 와 같음 (왜냐하면 $\mathcal{F}, \mathcal{N}, [\rho]$ 모두 Aut(G)-action 하에 적절하게 transform: $\mathcal{F}, \lambda_k$ 는 invariant; $n_k$ 는 invariant; $[\rho_k]$ 는 conjugate stabilizer 의 irrep 으로 transform → equivalence class 동일). 따라서 σ 는 **자동으로 Aut(G)-orbit invariant**. $\Box$

### 2.4 Self-classification

이 정의는 **Cat A definitional**: 모든 구성요소가 graph-intrinsic 객체로 부터 유한 algorithm 으로 계산 가능. 임의성은 (O3) 의 cutoff 선택 한 곳에 집중.

---

## §3. Lemma 1 — Irrep decomposition is well-defined

> **Lemma 1.** Let $u^* \in \Sigma_m$ a Morse-0 local minimizer with stabilizer $S = S(u^*) \leq \text{Aut}(G)$. Then $H(u^*)$ commutes with the linear $S$-action on $\mathbf{1}^\perp$, and each Hessian eigenspace $V_k$ admits a canonical decomposition
> $$V_k = \bigoplus_{[\rho] \in \widehat{S}} V_k^{[\rho]}$$
> into isotypic components. The orbital irrep label $[\rho_k]$ in (O5) is well-defined whenever $\dim V_k = 1$. For $\dim V_k > 1$, the multi-set $\{(\dim V_k^{[\rho]}, [\rho])\}_{[\rho]}$ is canonical.

### Proof

**Step 1 (Commutation).** $\mathcal{E}(\pi \cdot u) = \mathcal{E}(u)$ (Aut(G)-invariance of energy on graph-symmetric formulations of $\mathcal{E}_\text{cl}, \mathcal{E}_\text{sep}, \mathcal{E}_\text{bd}$ — established in `working/SF/symmetry_moduli.md` §1.2 for our canonical operators). Differentiating twice with $u = u^* + \epsilon v$ and equivariance of $\pi$:
$$v^\top \mathbf{H}(u^*) v = (\pi v)^\top \mathbf{H}(\pi \cdot u^*)(\pi v).$$
For $\pi \in S = \text{Stab}(u^*)$: $\pi \cdot u^* = u^*$, so
$$v^\top \mathbf{H}(u^*) v = (\pi v)^\top \mathbf{H}(u^*)(\pi v) \quad \forall v.$$
By polarization, $\mathbf{H}(u^*) = \pi^\top \mathbf{H}(u^*) \pi$, i.e. $\pi$ commutes with $\mathbf{H}(u^*)$. Restriction to $\mathbf{1}^\perp$ preserves commutation (since $\pi \mathbf{1} = \mathbf{1}$). Therefore $S$-action on $\mathbf{1}^\perp$ commutes with $H(u^*)$.

**Step 2 (Eigenspace invariance).** Let $H \phi = \lambda \phi$. Then $H (\pi \phi) = \pi H \phi = \lambda (\pi \phi)$. Hence $\pi V_k \subseteq V_k$ for all $\pi \in S$. So each $V_k$ is $S$-stable.

**Step 3 (Isotypic decomposition).** $S$ is a finite group acting on the finite-dim real vector space $V_k$. By Maschke's theorem (alternatively, since $S$ acts unitarily after choosing the standard inner product on $\mathbf{1}^\perp$), $V_k$ decomposes as a direct sum of $S$-irreducible subrepresentations. Group these by isomorphism class:
$$V_k = \bigoplus_{[\rho] \in \widehat{S}} V_k^{[\rho]}.$$
**Canonical**: the projector onto $V_k^{[\rho]}$ is given by the **isotypic projector**
$$P_{[\rho]} = \frac{\dim \rho}{|S|} \sum_{\pi \in S} \overline{\chi_\rho(\pi)} \cdot \pi$$
with $\chi_\rho$ the character of $\rho$. This projector depends only on $S$ and $\rho$, not on a choice of basis. Hence the decomposition (and the multi-set $\{(\dim V_k^{[\rho]}, [\rho])\}$) is canonical.

**Step 4 (1-dim case).** If $\dim V_k = 1$, $V_k$ is a single 1-dim subrepresentation, hence equals $V_k^{[\rho]}$ for a unique $[\rho]$. This $[\rho]$ is $[\rho_k]$ in (O5). $\Box$

### Remarks

- (R1.1) "Real" vs "complex" representations. $S$-action 는 originally real linear. Maschke 가 직접 적용; complex chars 사용 시 $V_k$ 의 복소화 위에서 분해. 두 표기 가 본질 차이 없음.
- (R1.2) **Generic non-degeneracy.** Generic $u^*$ (sufficiently asymmetric energy parameters) 에 대해 모든 $V_k$ 의 dim = 1 이며 $[\rho_k]$ 는 well-defined single irrep. 비-일반적 (parameter co-dim ≥ 1) 한 점에서 $\dim V_k \geq 2$ 발생.
- (R1.3) **Translation-broken case.** Free-BC grid 에서 $u^*$ 가 grid 중심 위에 있고 $S = D_4$ 인 경우, $\widehat{D_4} = \{A_1, A_2, B_1, B_2, E\}$ (5 irreps, last 는 2-dim).

### Self-classification: **Cat A** (full proof, standard tools).

---

## §4. Lemma 2 — Nodal count is graph-intrinsic and Aut(G)-equivariant

> **Lemma 2.** For each Hessian eigenvector $\phi_k \in \mathbf{1}^\perp$ with $\phi_k(i) \neq 0$ for all $i \in X$ (generic case), the nodal count $\mathcal{N}(\phi_k)$ in (O4) satisfies:
> (i) $\mathcal{N}(\phi_k) \in \mathbb{Z}_{\geq 1}$ 는 graph-intrinsic (그래프 구조와 $\phi_k$ 만으로 결정).
> (ii) For any $\pi \in \text{Aut}(G)$, $\mathcal{N}(\pi \cdot \phi_k) = \mathcal{N}(\phi_k)$.
> (iii) **Courant bound**: if $\phi_k$ is the $k$-th eigenvector of $H(u^*)$ (sorted ascending, $k = 0, 1, \ldots$), then $\mathcal{N}(\phi_k) \leq k + 1$.
> (iv) Sign-flip invariance: $\mathcal{N}(-\phi_k) = \mathcal{N}(\phi_k)$.

### Proof

**(i)** Direct from definition: the partition $X = X^+ \cup X^- \cup X^0$ with $X^\pm = \{i : \pm\phi_k(i) > 0\}$, $X^0 = \{i : \phi_k(i) = 0\}$ uses only $\phi_k$'s values. Connected components computed on the subgraphs $G[X^+]$ and $G[X^-]$ via BFS use only graph adjacency. 결과는 두 정보의 함수.

**(ii)** $\pi$ permutes vertices preserving adjacency, hence permutes connected components of any vertex subset's induced subgraph. $(\pi \phi_k)(i) = \phi_k(\pi^{-1} i)$, so $X^+ \cdot \pi := \{i : (\pi\phi_k)(i) > 0\} = \pi(X^+)$. The induced subgraphs $G[\pi X^+] \cong G[X^+]$ (graph isomorphism via $\pi$), so same number of connected components. Similarly for $X^-$. Sum is invariant. $\Box$

**(iii)** Standard graph Courant–Fischer (Davies, Gladwell, Leydold, Stadler 2001 "Discrete nodal domain theorems"): for the $k$-th eigenvalue (counting from $k=1$, multiplicity counted) of any symmetric matrix $H = D_v - A$ with $D_v$ diagonal and $A$ off-diagonal nonneg-symmetric, the eigenvector has $\leq k$ strong nodal domains. Our Hessian $H(u^*)$ in general is **not** of this discrete-Schrödinger form — it can have negative off-diagonals (from $\mathcal{E}_\text{sep}$'s $-\gamma_D(P + P^\top)$ term per `working/SF/mode_count.md` §2.1(d)). The Courant theorem in this **signed** case admits a generalized version (Lange–Liu–Peyerimhoff–Post 2015 "Frustration index and Cheeger inequalities for general signed graphs") that bounds the number of nodal domains by $k$ with respect to the *frustration index* of the signed graph. For our case the bound becomes $\mathcal{N}(\phi_k) \leq k + 1 + \text{(frustration correction)}$; the correction vanishes when $H$ is balanced (= $\mathcal{E}_\text{sep}$ contribution dominated by Laplacian).

**Status of (iii):** Strong Courant 는 **conditional** on signed-Laplacian structure of $H(u^*)$. For pure-$\mathcal{E}_\text{bd}$ Hessian ($H = 4\alpha L + \beta W''(c) I$ at $u^* = c\mathbf{1}$ — Prop 1.3a), Courant bound is exactly $\mathcal{N}(\phi_k) \leq k$. For full SCC, it holds **modulo** the correction term, which we do not bound here. → 본 (iii) 는 **Cat C conditional**.

**(iv)** Sign flip swaps $X^+$ and $X^-$ but does not change individual connected component counts. $\Box$

### Examples

- 1D path graph $P_n$: $\phi_k$ from $L = D - A$ takes form $\phi_k(i) = \cos((k-1)\pi(i-1/2)/n)$; nodal count $= k$, exactly Courant-tight.
- 2D grid $L \times L$: Laplacian eigenvectors $\phi_{(p,q)}(x, y) = \cos(\pi p x / L) \cos(\pi q y / L)$ with $\lambda_{(p,q)} = (\pi p / L)^2 + (\pi q / L)^2$ in continuum approximation. Nodal domains = $(p+1)(q+1)$. Courant ordering: ascending $\lambda$ gives mode index, but multiple $(p,q)$ can have same $\lambda$ (degeneracies → mixing).

### Self-classification: **(i), (ii), (iv) = Cat A**; **(iii) = Cat C** (conditional on signed-Laplacian frustration index).

---

## §5. Theorem 1 — Mode-0 reinterpretation as (pseudo-)Goldstone

이 정리가 R23 의 A-01 statement 의 가장 중요한 수정점. pre_brainstorm §2.3 의 통찰을 정형화.

### 5.1 Setup

$G$ 는 $L \times L$ free-BC 2D square grid, $u^* \in \Sigma_m$ Morse-0 local minimizer, **localized** in the bulk (즉 $u^*$ 의 support 의 majority 가 boundary 로부터 거리 $\geq L/4$ at the bulk site closest to boundary).

### 5.2 Translation pseudo-symmetry

free-BC grid 의 finite vertex set $X = \{0, \ldots, L-1\}^2$ 에 대해 lattice translation $\tau_{(a,b)}(x,y) := (x+a, y+b)$ 는 일반적으로 graph automorphism이 **아니다** (boundary vertex set 이 변동하면 그래프 구조 다름). 그러나 boundary 로부터 충분히 멀리 떨어진 bulk 에서는 translation 이 **approximate** symmetry.

> **Definition (Pseudo-translation).** $u^*$ 가 boundary 로부터 거리 $\geq d_*$ 인 bulk 에 localized 되어 있고, $|a|, |b| \leq d_* / 2$ 인 small translation $\tau_{(a,b)}$ 에 대해 $u^*_{(a,b)} := \tau_{(a,b)} \cdot u^*$ 는 다시 $\Sigma_m$ 의 valid configuration. Energy $\mathcal{E}(u^*_{(a,b)})$ 는 $\mathcal{E}(u^*)$ 와 동일 (boundary 에 닿지 않으므로 graph 구조가 effectively translationally-invariant in the supported region).

### 5.3 Translation modes are near-zero of Hessian

> **Theorem 1.** Under the Setup of §5.1, define **translation modes**
> $$\delta u_x := \nabla_x u^* := u^*(\cdot + e_1) - u^*,\qquad \delta u_y := \nabla_y u^* := u^*(\cdot + e_2) - u^*$$
> (finite-difference translations along the two axes). Then:
> (a) $\delta u_x, \delta u_y \in \mathbf{1}^\perp$ (mass-preserving to leading order; $O(L^{-1})$ correction from boundary leakage).
> (b) $\langle \delta u_x, H(u^*) \delta u_x \rangle = O(\exp(-d_*/\xi_0))$ where $\xi_0 = \sqrt{\alpha/\beta}$ is the interface width (Cor 2.2).
> (c) Equivalent statement for $\delta u_y$ by 90° rotation.
> (d) For a localized $u^*$ that is approximately invariant under reflections through the center of mass ($S(u^*) \supseteq D_4$ at center), $\delta u_x$ and $\delta u_y$ together carry the $E$ irrep of $D_4$ (the 2-dim "vector" representation).

### Proof (sketch — Cat B)

**(a)** $\sum_i \delta u_x(i) = \sum_i [u^*(i+e_1) - u^*(i)]$. For any vertex $i$ with $i + e_1$ in $X$ (interior): contributions cancel pairwise by telescoping. For $i$ on the boundary (no $i+e_1$ neighbor or value undefined): contribution $|u^*(i)|$ or $|u^*(i+e_1)|$. In the localized regime ($u^* \approx 0$ near boundary), these residual sums are $O(\exp(-d_*/\xi_0))$ (Cor 2.2 quantitative tail). Hence $\sum \delta u_x = O(\exp(-d_*/\xi_0))$ — approximately mass-preserving.

**(b)** Bulk evaluation. In the bulk (away from boundary), $u^*$ satisfies
$$\nabla \mathcal{E}(u^*) = 0 \quad \text{up to constraint multiplier (volume)},$$
i.e. $\frac{\partial \mathcal{E}}{\partial u(i)}(u^*) = \mu$ (constant Lagrange multiplier) for all $i$ in bulk. Apply the discrete derivative $\partial / \partial x$:
$$\partial_x \frac{\partial \mathcal{E}}{\partial u(i)}(u^*) = 0 \quad \text{for }i\text{ in bulk}.$$
But $\partial_x \frac{\partial \mathcal{E}}{\partial u(i)} = \sum_j \frac{\partial^2 \mathcal{E}}{\partial u(i) \partial u(j)} \cdot (\partial_x u^*)(j) = (\mathbf{H}(u^*) \delta u_x)(i)$. So $(\mathbf{H} \delta u_x)(i) = 0$ in bulk.

Boundary contribution: residual where translation breaks, of size $O(\exp(-d_*/\xi_0))$ in $L^2$ norm (Cor 2.2 tail). So $\|\mathbf{H} \delta u_x\|_2 = O(\exp(-d_*/\xi_0)) \cdot \|\delta u_x\|_2$. Restriction to $\mathbf{1}^\perp$: similar bound. Hence $\langle \delta u_x, H \delta u_x\rangle / \|\delta u_x\|^2 = O(\exp(-d_*/\xi_0))$.

**(c)** By 90° rotation 대칭 (D₄ rotational subgroup).

**(d)** Standard $D_4$ representation theory: $D_4$ has a 2-dim irrep $E$ with basis transforming as $(x, y)$ under rotation. The pair $(\delta u_x, \delta u_y)$ transforms exactly as $(x, y)$ (up to sign): rotation by 90° sends $\delta u_x \to \delta u_y$ and $\delta u_y \to -\delta u_x$. Reflections through $x$-axis send $\delta u_x \to \delta u_x$, $\delta u_y \to -\delta u_y$. This matches the $E$ irrep matrix representation. $\Box$

### 5.4 Consequence: A-01 statement revision

R23 의 A-01: "Mode 0 = p-dominant (ℓ=1)". 이것이 angular multipole power 측정에 기반.

본 정리가 보이는 것:
- Mode 0 (lowest non-Goldstone) eigenvalue 가 $O(\exp(-d_*/\xi_0))$ 로 near-zero 이면 그것은 **translation pseudo-Goldstone** ($E$ irrep).
- 같은 "p-dominant" 라벨이 angular multipole power decomposition 에서 발생하는 이유는 $E$ irrep 의 basis $(x, y)$ 가 angular ℓ=1 Fourier component 와 일치하기 때문.

따라서 A-01 의 statement 는 **수정**:
- (구) "Mode 0 = p-dominant orbital excitation"
- (신) "Mode 0 = translation pseudo-Goldstone, carrying $E$ irrep, $\lambda_0 \sim \exp(-d_*/\xi_0)$. Angular multipole projection onto ℓ=1 channel reflects the $(x, y)$ basis of the $E$ irrep, not a genuine p-orbital excitation."
- (신 corollary) "Mode 1 = first genuine non-Goldstone orbital excitation; its irrep is generically $A_1$, $A_2$, $B_1$, or $B_2$ (1-dim irreps of $D_4$)."

### Self-classification: **Cat B** — sketched proof using known tools (Cor 2.2 tail, $D_4$ rep theory). 명시적 경계 상수와 $d_*$ scaling 이 더 정밀해야 Cat A. **Recommended verification**: 32×32 grid 의 R23 stable minimizer 의 $\lambda_0$ 측정. 만약 $\lambda_0 \ll \lambda_1$ (e.g. ratio < 0.1) 이면 Theorem 1 지지. ratio ≈ 1 이면 반증 (즉 Mode 0 가 진짜 orbital).

### 5.5 What this implies for SCC vs atomic

**Atom 에서**: nucleus 가 fixed → no translation Goldstone → 모든 low-lying modes 가 진짜 orbital excitation, p-orbital ($\ell = 1$) 가 first excited (after 1s).

**SCC 에서** (free-BC grid 또는 torus, localized minimizer): translational degree of freedom 이 Σ_m 위에서 broken (정확히 broken in torus, approximately broken in free-BC); Goldstone $E$ irrep 이 spectrum 의 lowest non-trivial position 을 점유 → first **genuine** orbital excitation 이 $A_1, A_2, B_1, B_2$ 중 하나이며, 일반적으로 quadrupole-like ($B_1$ 또는 $B_2$, ℓ=2 angular character) 가 첫 번째.

이것은 **SCC 와 atom 사이의 구조적 차이**에 대한 Theorem 1 의 prediction. R23 데이터의 "Mode 1 = d-dominant" 는 이 prediction 과 부합. 따라서:

- 차용 (atomic 어휘) 에서는 "anomaly" 로 보이는 SCC 의 d-first-excited 가
- SCC-intrinsic 어휘 (translation Goldstone + $D_4$ irrep) 에서는 **자연스러운 따름정리**.

이것이 §01 §1.2 의 (2-iii) 가 요구한 "차용 제거의 가치".

---

## §6. Theorem 2 — Pre-objective structure (closure removes F=1)

R23 의 A-04 (Full SCC 가 F=1 stable minimizer 를 saddle 로 만든다) 의 mechanism 적 정리. Cat C conditional.

### 6.1 Setup

Pure $\mathcal{E}_\text{bd}$ 만 활성화된 ($\lambda_\text{cl} = \lambda_\text{sep} = 0$) 경우, F=1 single-disk minimizer 가 존재 (Cor 2.2: tanh profile $u_\text{disk}^*(r) = \tfrac{1}{2}(1 - \tanh((r-r_0)/\xi_0))$, mass $m = \pi r_0^2$).

> **Question.** Full SCC ($\lambda_\text{cl}, \lambda_\text{sep} > 0$) 에서 동일 $u_\text{disk}^*$ 가 여전히 critical / stable 인가?

### 6.2 Closure gradient at disk

$\mathcal{E}_\text{cl}(u) = \tfrac{a_\text{cl}}{2} \|u - \text{Cl}(u)\|^2$ with $\text{Cl}(u) = \sigma(\text{contraction})$. At $u = u_\text{disk}^*$, $\text{Cl}(u_\text{disk}^*) \neq u_\text{disk}^*$ generally. Specifically:

**Interior** ($u_\text{disk}^* \approx 1$): $\text{Cl}$ pulls toward fixed point $c^*$. Since $1 > c^*$ (closure FP 는 일반적으로 $c^* \in (0, 1)$ 이고 spinodal 영역 안), $\text{Cl}(1) < 1$. Mismatch: $u - \text{Cl}(u) = 1 - c^* > 0$.
**Exterior** ($u_\text{disk}^* \approx 0$): $\text{Cl}(0) > 0$. Mismatch: $u - \text{Cl}(u) = -c^* < 0$.
**Interface** ($u_\text{disk}^* \approx 1/2 = c$): if $c = c^*$, mismatch ≈ 0. Else nontrivial.

이 mismatch 가 closure gradient $\nabla \mathcal{E}_\text{cl}(u_\text{disk}^*) \neq 0$. 정확한 형태:
$$\nabla \mathcal{E}_\text{cl}(u_\text{disk}^*) = a_\text{cl} (I - J_\text{Cl}^\top)(u_\text{disk}^* - \text{Cl}(u_\text{disk}^*))$$
(이는 `working/SF/mode_count.md` §2 에 quote 된 Hessian factor 와 부합 — 같은 (I - J_Cl) 구조).

### 6.3 Separation gradient at disk

$\mathcal{E}_\text{sep}(u) = \sum_i u_i (1 - D(u)_i)$ with $D(u) = \sigma(\kappa_D P u - \delta_D \mathbf{1})$, $P$ row-normalized.

At disk minimizer $u_\text{disk}^*$:
- Interior: $u \approx 1$, neighbors $\approx 1$, so $P u \approx 1$, $D(u) \approx \sigma(\kappa_D - \delta_D) \approx 1$ (high distinction value). Then $u_i (1 - D_i) \approx 1 \cdot 0 = 0$ contribution.
- Exterior: $u \approx 0$, $D \approx 0$, contribution $0 \cdot 1 = 0$.
- Interface 부근: $u \in (0, 1)$, $D$ intermediate, nonzero gradient.

핵심: Interior 에서 $u_i (1 - D(u)_i) \approx 0$ (낮은 sep cost). 그러나 sep 의 gradient 는 nonzero 일 수 있음 (functional derivative 가 linear 이고 $D$ 가 nontrivial 의존성). 정확한 식 (`working/SF/mode_count.md` §2.1(d)):
$$\nabla \mathcal{E}_\text{sep}(u) = (1 - D(u)) - \kappa_D P^\top (u \odot D(u) (1 - D(u))) + \text{const(i)}$$
(approximate; sign of certain terms depends on normalization).

Generally, $\nabla \mathcal{E}_\text{sep}(u_\text{disk}^*) \neq 0$ in the interior bulk (where $P^\top$ smearing of $D(u)$ residuals creates net force).

### 6.4 Theorem statement

> **Theorem 2 (Pre-Objective Structure, conditional).** For a 2D grid $G$ of size $L \geq L_0$ (with $L_0$ a graph-dependent constant), and parameters satisfying:
> - **(C1)** $\beta > \beta_\text{disk}$ (large enough to make the disk minimizer well-defined, per T8-Full),
> - **(C2)** $a_\text{cl} \in (0, 4)$ (closure contraction regime, per T6b),
> - **(C3)** $c \in ((3-\sqrt{3})/6, (3+\sqrt{3})/6)$ (spinodal),
> - **(C4)** $c^* \neq c$ (closure FP differs from operating point),
> - **(C5)** $\lambda_\text{cl} > \lambda_\text{cl}^\text{crit}(L, \beta, a_\text{cl}, c)$ for some explicit threshold,
>
> the disk minimizer $u_\text{disk}^*$ of pure $\mathcal{E}_\text{bd}$ is **not** a critical point of full $\mathcal{E} = \lambda_\text{cl} \mathcal{E}_\text{cl} + \lambda_\text{sep} \mathcal{E}_\text{sep} + \mathcal{E}_\text{bd}$ on $\Sigma_m$. In particular, $u_\text{disk}^*$ is not a local minimum of $\mathcal{E}$.

### Proof (sketch — Cat C)

**Step 1.** $u_\text{disk}^*$ critical of $\mathcal{E}_\text{bd}$ on $\Sigma_m$: $\nabla \mathcal{E}_\text{bd}(u_\text{disk}^*) = \mu_\text{bd} \mathbf{1}$ for some Lagrange multiplier $\mu_\text{bd}$. (Standard variational, T8-Full proof.)

**Step 2.** Critical of full $\mathcal{E}$ on $\Sigma_m$ iff $\nabla \mathcal{E}(u_\text{disk}^*) = \mu \mathbf{1}$ for some $\mu$. Equivalently, $\pi_{\mathbf{1}^\perp} \nabla \mathcal{E}(u_\text{disk}^*) = 0$.

**Step 3.** $\pi_{\mathbf{1}^\perp} \nabla \mathcal{E} = \pi_{\mathbf{1}^\perp}(\lambda_\text{cl} \nabla \mathcal{E}_\text{cl} + \lambda_\text{sep} \nabla \mathcal{E}_\text{sep} + \nabla \mathcal{E}_\text{bd}) = \lambda_\text{cl} g_\text{cl} + \lambda_\text{sep} g_\text{sep}$ where $g_\text{cl} := \pi_{\mathbf{1}^\perp} \nabla \mathcal{E}_\text{cl}(u_\text{disk}^*)$, $g_\text{sep} := \pi_{\mathbf{1}^\perp} \nabla \mathcal{E}_\text{sep}(u_\text{disk}^*)$ (using Step 1).

**Step 4.** **Claim**: $g_\text{cl} \neq 0$ under (C2)–(C4). Reason: $u_\text{disk}^* - \text{Cl}(u_\text{disk}^*)$ is interior-positive ($\approx 1 - c^*$) and exterior-negative ($\approx -c^*$). The image under $(I - J_\text{Cl}^\top)$ retains spatial inhomogeneity (a constant 0 image would require $(I - J_\text{Cl}^\top) v = 0$ for non-zero spatially-varying $v$, contradicting injectivity in contraction regime per T6b). Projection to $\mathbf{1}^\perp$ removes only the mean, leaving nonzero variation. Hence $g_\text{cl} \neq 0$.

**Step 5.** Therefore $\lambda_\text{cl} g_\text{cl} + \lambda_\text{sep} g_\text{sep} \neq 0$ unless precise cancellation $\lambda_\text{cl} g_\text{cl} = -\lambda_\text{sep} g_\text{sep}$. This cancellation occurs only on a codim-1 subset of parameter space (a single equation in the 2D space $(\lambda_\text{cl}, \lambda_\text{sep})$). For generic $(\lambda_\text{cl}, \lambda_\text{sep}) > 0$, no cancellation → $u_\text{disk}^*$ not critical. (C5) makes "generic" precise via threshold $\lambda_\text{cl}^\text{crit}$ above which $\|g_\text{cl}\| > \|g_\text{sep}\|$.

**Step 6.** Not-critical implies not-local-min (since local min ⊂ critical points). $\Box$

### 6.5 Self-classification

**Cat C** — sketched proof with conditions (C1)–(C5). Steps 1, 2, 6 are Cat A. Steps 3, 4, 5 require verification:
- Step 4: $(I - J_\text{Cl}^\top)$ injectivity proof needs more care (T6b 는 $(I - J_\text{Cl})$ injectivity 만; transpose 도 동일하나 명시 필요).
- Step 5: the cancellation locus is codim-1 — need to compute $g_\text{cl}, g_\text{sep}$ explicitly and show they are not anti-parallel except in measure-zero set.
- (C5)'s explicit threshold formula is needed for full rigor.

**Independent evidence**: R23 §11 FSC1 (full SCC at $c=0.5, \beta=30$, $32 \times 32$): F=1 disk is saddle (Morse index 1). 56 stable minimizers all have $\mathcal{F} \geq 5$. **Empirically Cat A** at this specific parameter point.

### 6.6 Pre-objective interpretation

Theorem 2 의 의미: closure (self-completion) 의 self-reference 가 "single object" (unique disk = F=1) 를 actively destabilize. Self-reference 가 localization 을 방해 = "object 가 자체로 존재할 수 없음" 의 mechanism적 표현.

Sep 항 (self-contrast) 도 같은 방향: interior uniformity 가 sep 비용을 generate → interior 가 distort.

**둘이 합쳐져**: cl/sep 둘 다 single-disk 를 destabilize 하고, 그 destabilization 의 결과가 multi-peak (multi-formation) configuration. R23 의 56 stable basins 은 이 destabilization 후 기존하는 "multi-peak compromise" landscape 의 minimum 들.

이것이 SCC 의 "pre-objective" 라는 commitment (canonical §2 의 commitment 1) 의 첫 번째 **수학적 형식화**. 단, full Cat A 에 도달하려면 다음이 필요:
- (C5) 의 explicit threshold
- "single-formation 만 destabilize, multi-formation 은 stable" 의 quantitative statement
- F=1 → F≥5 의 jump 의 통일적 설명 (왜 F≥5 가 minimum F? — 이는 spectral gap 과 Cor 2.2 의 interface scale 의 결합; 본 세션에서 sketched 만)

---

## §7. Continuum corollary (A3 sketch)

이 절은 supporting (Cat C scoping). 본격적 전개는 다음 세션 또는 G4 에서.

### 7.1 Linearization around circular minimizer

Continuum 위 disk minimizer $u^*(r) = \tfrac{1}{2}(1 - \tanh((r - r_0)/\xi_0))$ 에서 $\delta u$ fluctuation:
$$\delta \mathcal{E} = \int (4\alpha |\nabla \delta u|^2 + V(r) (\delta u)^2) dx + \mathcal{O}(\delta u^3)$$
with $V(r) = \beta W''(u^*(r))$, $W(u) = u^2(1-u)^2$, $W''(u) = 2(1 - 6u + 6u^2)$.

Polar coordinates $(r, \theta)$, separation $\delta u(r, \theta) = R(r) e^{i \ell \theta}$:
$$-4\alpha\Big[R'' + \frac{R'}{r} - \frac{\ell^2}{r^2} R\Big] + V(r) R = \lambda R.$$

**Shell well**: $V(r)$ is positive at interior ($r \to 0$, $u \to 1$, $W''(1) = 2$), negative near interface ($r \approx r_0$, $u \approx 1/2$, $W''(1/2) = -1$), positive at exterior ($r \to \infty$, $u \to 0$, $W''(0) = 2$). So $V(r)$ is attractive shell well of width $\sim \xi_0$ at depth $\sim \beta/\alpha$.

### 7.2 Spectrum structure

Near the shell ($r \approx r_0$, width $\xi_0$), use Schrödinger 1D approximation with $\theta$-dependent centrifugal term $\ell^2/r_0^2$:
$$\lambda_{n, \ell} \approx \lambda_n^{(0)} + 4\alpha \ell^2 / r_0^2$$
where $\lambda_n^{(0)}$ are radial-only eigenvalues (radial quantum number $n = 0, 1, 2, \ldots$).

**Predictions** (Cat C, sketch):
- Lowest eigenvalue: $\lambda_{0, 0} = -\beta/\alpha + O(\alpha/\xi_0^2)$ (depth of well minus zero-point).
- $\ell$-spacing: $\Delta \lambda_\ell = 4\alpha \ell^2 / r_0^2$. For $r_0 \gg \xi_0$, ℓ-spacing 은 radial $\lambda^{(0)}$-spacing 보다 작음.
- Radial $n=0$ shell 위에서 $\ell = 0, 1, 2, \ldots$ ladder 가 좁은 spacing 으로 쌓임 → ℓ-ordering 우세.
- 이 continuum prediction 은 atom 의 hydrogenic ordering 과 다름 (atom 은 $-1/n^2$).

### 7.3 $D_4$ correction

Continuum 은 $SO(2)$ rotational symmetry. Finite grid 의 $D_4$ 는 $SO(2)$ 의 discrete subgroup. Lattice perturbation $V(r, \theta) = V_0(r) + \delta V_4(r) \cos(4\theta) + \delta V_8(r) \cos(8\theta) + \ldots$ (even orders 가 $D_4$-invariant이므로).

**Ramifications**:
- Pure $SO(2)$: ℓ=2 doublet $(\cos 2\theta, \sin 2\theta)$ degenerate.
- $D_4$ correction $\delta V_4 \cos 4\theta$: ℓ=2 doublet 와 ℓ=6 doublet 가 mix (matrix element $\langle \cos 2\theta | \cos 4\theta | \cos 6\theta \rangle \neq 0$). Mixing strength $\sim \delta V_4 / |\Delta \lambda_{\ell=2 \to 6}|$.

### 7.4 Translation Goldstone in continuum vs free-BC

Continuum on $\mathbb{R}^2$ 는 translation $\mathbb{R}^2$ 도 대칭 → 정확한 Goldstone 두 개 (x, y translation), 이것이 ($x, y$) 의 derivative basis 와 일치 → ℓ=1 channel 의 zero mode.

Free-BC grid 에서는 translation 이 깨졌지만 bulk 에서 approximate (Theorem 1).

이 corollary 가 "continuum 에서도 ℓ=1 first excited 가 Goldstone" 임을 보임. 즉 atom 과 SCC 의 차이는 **"nucleus 가 fixed 인가 free 인가"**의 차이이지 spectral 도구의 차이가 아님. Atomic Hamiltonian 도 만약 nucleus translational d.o.f. 를 포함하면 같은 Goldstone 갖게 됨.

### 7.5 Self-classification

**Cat C** (conditional sketch). Effective Schrödinger derivation 은 standard analytical 작업이나 (i) 정확한 $r_0, \xi_0$ formula 의 finite-grid 확인, (ii) shell well bound state 수의 정확한 결정, (iii) 32×32 의 lowest 20 mode 와의 numerical 부합, 이 셋이 본 세션에서 이행되지 않음.

---

## §8. Falsification attempts

본 세션의 정의 / 정리에 대한 명시적 반례 시도. 무너지지 않는 이유를 함께 기록.

### 8.1 σ 정의의 모호성에 대한 반례 시도

**시도 1**: 두 stable minimizer $u^*_1, u^*_2$ 가 같은 σ 를 갖지만 Aut(G)-orbit 으로 묶이지 않음.

**구성**: 32×32 grid, c=0.5, β=30. R23 §10 의 56 stable 중 두 minimizer 가 같은 (F, mode-1 angular label) 를 갖는 경우 존재 (37 distinct mode-1 labels, 56 stable → 평균 1.5 stable per mode-1 label). 이 두 minimizer 가 graph automorphism 으로 연결 안 될 수 있음.

**무너지는 이유 (σ-정의가 살아남는 이유)**: σ 는 mode-1 label 만이 아니라 **K mode 전체** 의 sequence. 두 다른 minimizer 가 모든 K mode 의 (n_k, [ρ_k], λ_k) 가 일치하는 것은 매우 드뭄 (eigenvalue 가 continuous parameter ⇒ generic 하게 distinct). 따라서 K cutoff 가 충분히 크면 σ 가 사실상 유일 라벨.

**잔여 위험**: K cutoff 가 너무 작으면 σ 가 not unique. (O3) 의 옵션 K-A (spectral gap cutoff) 가 이를 부분 완화하지만, 두 minimizer 가 spectral gap 도 같으면 여전히 ambiguous.

→ **결론**: σ-정의 위 minimizer 는 unique-up-to-Aut(G) 의 **generic** 주장만 가능. Special non-generic configurations 에서는 ambiguous. **Cat A definitional, Cat B uniqueness**.

### 8.2 Mode-0 reinterpretation 의 반례 시도

**시도 2**: A-01 의 Mode 0 가 진짜 d-orbital (not Goldstone) 인 경우.

**구성**: $u^*$ 가 grid 중심에 정확히 align되지 않거나, $u^*$ 가 boundary 에 닿아 있어서 translation symmetry 가 강하게 깨졌다면, $\delta u_x, \delta u_y$ 의 Hessian eigenvalue 가 더이상 near-zero 가 아닐 수 있음.

**무너지는 이유 (Theorem 1 가 살아남는 이유)**: Theorem 1 은 명시적으로 "localized in bulk, $d_* \geq L/4$" 가정. R23 의 stable minimizer 중 boundary 가까운 것은 가정 위반이므로 Theorem 1 적용 불가 — 그 경우 Mode 0 가 진짜 orbital 일 수 있음.

→ **결론**: Mode 0 = Goldstone interpretation 은 **bulk-localized minimizer 한정**. Empirical 검증 필요: R23 의 56 stable 중 몇 % 가 bulk-localized 인가? 만약 다수가 boundary-touching 이면 Theorem 1 의 적용 범위 limited.

### 8.3 Theorem 2 (F=1 removal) 의 반례 시도

**시도 3**: 어떤 disk-like configuration 이 cl+sep 하에서도 critical 일 수 있음.

**구성**: $c = c^*$ (closure FP 와 operating point 일치). 그러면 (C4) 위반, $u - \text{Cl}(u) = 0$ 은 정확하지 않지만 interior 에서 작아짐 → $g_\text{cl}$ 작아짐 → cancellation 가능.

**무너지는 이유**: $c = c^*$ 는 special parameter (codim-1). Generic $(c, c^*)$ 에서는 $g_\text{cl} \neq 0$. 또한 $c = c^*$ 라도 interface 에서의 mismatch 는 잔존 ($u \in (0,1)$ 의 점에서 $u \neq c^*$).

→ **결론**: Theorem 2 는 "generic parameter" hypothesis 하에 성립. Special parameter point 에서 disk-like F=1 minimizer 가 살아남을 수 있으나, R23 데이터 (FSC1) 는 generic $c=0.5, \beta=30$ 영역.

### 8.4 σ-정의가 R23 데이터를 분류 못 하는 경우

**시도 4**: R23 의 mode-1 label 분포가 σ 의 (n_1, [ρ_1]) 분포와 일치하지 않을 수 있음.

**구성**: angular multipole (R23 의 도구) 와 nodal count + irrep (σ-정의) 가 다른 결과를 줄 수 있다면 σ 가 R23 데이터를 자연스럽게 분류 못함.

**무너지는 이유**: angular multipole 은 R23 의 측정이지만, σ 의 (n_1, [ρ_1]) 은 더 raw (graph-intrinsic). 이론적으로 angular multipole $\to$ irrep 의 map 은 well-defined (continuum limit 에서 ℓ → irrep). Finite grid 에서 mismatch 가 있을 수 있으나 그것은 angular multipole 측정의 finite-size artifact 이지 σ 의 결함이 아님.

→ **결론**: σ-정의가 더 raw 한 정보를 사용 → R23 의 angular multipole 측정의 artifact 를 우회. 단 **검증 필요**: σ 와 angular multipole 의 부합도가 finite grid 에서 얼마나 좋은가.

### 8.5 종합

위 4 개 반례 시도는 모두 σ-정의 / 정리 1 / 정리 2 의 **boundary regime** 을 발견했으나 core claim 을 무너뜨리지는 않음. 본 세션의 결과는 **generic regime 에서 valid**. 후속 세션의 verification 작업은 (a) R23 데이터의 σ-라벨링 numerics, (b) bulk-localized fraction 측정, (c) angular multipole vs irrep 부합도 확인.

---

## §9. Self-classification summary

| 결과 | Cat | 비고 |
|---|---|---|
| §2 σ definition | A definitional | (O3) cutoff 임의성 한 곳 |
| §3 Lemma 1 (irrep decomposition) | A | full proof, standard tools |
| §4 Lemma 2 (i,ii,iv) | A | standard graph theory |
| §4 Lemma 2 (iii) Courant bound | C | conditional on signed-Laplacian frustration index |
| §5 Theorem 1 (Mode-0 Goldstone) | B | sketched, needs explicit constants |
| §6 Theorem 2 (F=1 removal) | C | conditional (C1)–(C5), Steps 4-5 need rigor |
| §7 Continuum corollary | C | sketch, lacking finite-grid numerics |
| §8 Falsification attempts | identified boundary regimes, no core claim broken |

**총평**: 본 세션의 primary deliverable 인 σ-정의는 Cat A definitional 이며, Lemma 1 가 Cat A. Lemma 2(iii), Theorem 1, Theorem 2 는 Cat B/C 로 후속 세션의 검증 / 정량화 대상. 본 세션의 주 contribution 은 (a) σ-정의의 axiomatic 정형화, (b) Mode-0 의 translation Goldstone reinterpretation 의 명시적 정리화, (c) F=1 removal 의 mechanism 적 정리 sketch.

---

## §10. 다음 파일 (`03_integration_and_new_open.md`) 의 예고

- §1: σ-정의의 canonical 통합 — Axiom S1' 의 SCC-intrinsic redraft (CN17 sharpening 포함)
- §2: CN15 / CN16 의 proof-of-need + falsification test
- §3: A-01 statement revision 권고 (Theorem 1 기반)
- §4: 기존 OP (F-1, M-1, MO-1, OP-0001..0007, N-1, P-A..P-H) 와의 partial-resolution 표
- §5: Silent-resolution audit
- §6: 새 open question (NQ-125..) seeding
- §7: 본 prompt template 개선 제안
