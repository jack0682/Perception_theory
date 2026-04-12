---
id: META-0102
type: registry/symbols
status: accepted
last_updated: 2026-04-12
---

# Symbol Registry (S-xxxx)

**Purpose:** Define all mathematical symbols and notation to prevent ambiguity and collisions.

**Format:** Each row registers a symbol with its meaning, definition, and usage constraints.

---

## Registry Table

| ID | Symbol | Name | Definition / Meaning | Domain | Status | Notes |
|----|--------|------|-----------|--------|--------|-------|
| **S-0001** | u_t | Cohesion Field | u_t : X_t → [0,1] | SCC core | accepted | Primitive; lowercase u with subscript t |
| **S-0002** | X_t | Support Space | (V_t, E_t); vertices and edges at time t | SCC core | accepted | Graph structure; subscript t for time index |
| **S-0003** | E(u) | Energy Functional | E(u) = λ_cl E_cl + λ_sep E_sep + λ_bd E_bd + λ_tr E_tr | SCC core | accepted | Capital E; argument is field (usually u_t) |
| **S-0004** | E_cl | Closure Energy | ∫ (u - Cl(u))² dx | SCC energy | accepted | Subscript cl for closure |
| **S-0005** | E_sep | Separation Energy | ∫ u^T W_sym u dx | SCC energy | accepted | Subscript sep for separation |
| **S-0006** | E_bd | Boundary Energy | ∫ u^T L u dx + ∫ W(u) dx | SCC energy | accepted | Subscript bd for boundary |
| **S-0007** | E_tr | Transport Energy | ∫ ∫ C(u_s, u_t) × M_{s→t}(u_s, u_t) ds dt | SCC energy | accepted | Subscript tr for transport |
| **S-0008** | λ_cl | Closure Weight | Weight on E_cl in total energy | Parameter | accepted | Greek lambda; subscript cl |
| **S-0009** | λ_sep | Separation Weight | Weight on E_sep in total energy | Parameter | accepted | Greek lambda; subscript sep |
| **S-0010** | λ_bd | Boundary Weight | Weight on E_bd in total energy | Parameter | accepted | Greek lambda; subscript bd |
| **S-0011** | λ_tr | Transport Weight | Weight on E_tr in total energy | Parameter | accepted | Greek lambda; subscript tr |
| **S-0012** | λ_rep | Repulsion Weight | Weight on E_rep in K-field (inter-formation) | K-field param | accepted | Greek lambda; subscript rep for repulsion |
| **S-0013** | Cl_t | Closure Operator | Cl_t : [0,1]^n → [0,1]^n; axiom A3' | SCC core | accepted | Capital C and l; subscript t for time-indexed |
| **S-0014** | D_t | Distinction Operator | D_t : [0,1]^n → [0,1]; boundary contrast | SCC core | accepted | Capital D; subscript t for time-indexed |
| **S-0015** | C_t | Resolvent | C_t = L^{-1}[u_t]; co-belonging measure | SCC core | accepted | Capital C; subscript t for time-indexed; different from Cl_t |
| **S-0016** | M_{t→s} | Transport Kernel | M_{t→s} : [0,1]^n_s × [0,1]^n_t → [0,1]; temporal correspondence | SCC core | accepted | Capital M; subscript t→s indicates time direction |
| **S-0017** | L | Graph Laplacian | L = D - A; degree matrix minus adjacency | Graph ops | accepted | Capital L; context determines graph |
| **S-0018** | W_sym | Cohesion-Weighted Adjacency | W_sym = A ⊙ √(u^T u) | Energy | accepted | Subscript sym for symmetry |
| **S-0019** | W(u) | Double-Well Potential | W(u) = u²(1-u)² | Energy | accepted | Capital W; argument is field (coordinate-wise) |
| **S-0020** | W'(u) | Double-Well Derivative | W'(u) = 2u(1-u)(1-2u) | Energy | accepted | Prime notation for derivative (by u) |
| **S-0021** | d | Proto-Cohesion Diagnostic | d = (Bind, Sep, Inside, Persist) ∈ [0,1]^4 | Diagnostics | accepted | Lowercase d; 4-tuple of measurements |
| **S-0022** | Bind | Cohesion Strength | ℓ²(u_t) / √n = ∑ u_i² / √n | Diagnostics | accepted | English word; no subscript |
| **S-0023** | Sep | K-Field Separation | u-weighted average distance between formations | K-field diag | accepted | English word; used for K ≥ 2 |
| **S-0024** | Inside | Topological Persistence | H₀ persistence Q_morph; core rank via filtration | Diagnostics | accepted | English word; topological measure |
| **S-0025** | Persist | Transport Fidelity | ∑ min(u_curr, u_prev) / max(∑ u_curr, ∑ u_prev) | Diagnostics | accepted | English word; or via M_{t→s} fixed-point |
| **S-0026** | Σ_m | Volume-Constrained Manifold | {u ∈ [0,1]^n : ∫ u dx = m} | Constraint set | accepted | Capital sigma; subscript m for mass |
| **S-0027** | Σ²_M | K=2 Mass-Constrained Manifold | {(u¹, u²) : u^j ∈ [0,1]^n, m_j = M/2 for j=1,2} | K-field | accepted | Superscript 2 for K=2; subscript M for total mass |
| **S-0028** | m_j | Per-Formation Mass | ∫ u^j_t dx; "volume" of formation j | K-field | accepted | Lowercase m; subscript j for formation index |
| **S-0029** | K | Number of Formations | Number of independent cohesion fields | K-field | accepted | Capital K; externally imposed (F-1 issue) |
| **S-0030** | u^j_t | j-th Cohesion Field | j-th field in K-field configuration | K-field | accepted | Superscript j for formation index; subscript t for time |
| **S-0031** | t, s | Time Indices | Time parameter; s, t ∈ [0, T] typically | Temporal | accepted | Lowercase; s < t often |
| **S-0032** | ∇_u | Gradient w.r.t. u | Variational derivative; δE / δu | Energy | accepted | Nabla with subscript u; functional derivative |
| **S-0033** | ∇² | Hessian | Second variational derivative | Energy | accepted | Nabla squared; for second-order analysis |
| **S-0034** | τ | Constraint Parameter | Used in Bind normalization (τ = 1/2 typical) | Parameter | tentative | Greek tau; scaling parameter in some theorems |
| **S-0035** | β | Bifurcation Parameter | β = λ_sep / λ_cl; related to phase transition | Parameter | accepted | Greek beta; controls bifurcation |
| **S-0036** | α | Energy Coefficient | Appears in boundary energy (E_bd ~ α·u^T L u) | Parameter | accepted | Greek alpha; scaling coefficient |
| **S-0037** | β_crit | Critical Bifurcation | Critical value of β at phase transition | Threshold | accepted | Critical point for K=1 → K=2 transition |
| **S-0038** | ℓ² | Euclidean Norm Squared | ∑ u_i² | Norm | accepted | ell-squared; standard notation |
| **S-0039** | √n | Grid Size Normalization | Square root of number of sites | Normalization | accepted | For dimensional consistency |
| **S-0040** | Ω | Core Region | {i : u_i > threshold} at given time | Set | accepted | Capital omega; core indicator set |
| **S-0041** | Λ_coupling | K-field Coupling Strength | λ_rep · ω_jk / min(μ_j, μ_k); unified coupling metric | K-field | accepted | Capital lambda with subscript; from T-Persist-K-Unified |
| **S-0042** | H₀ | 0-Homology | Connected components (topological rank) | Topology | accepted | 0th homology group; counts components |
| **S-0043** | Q_morph | Morphological Persistence | Filtration-based persistence metric | Topology | tentative | Custom notation; see Transport paper section |
| **S-0044** | OT | Optimal Transport | Wasserstein distance + Sinkhorn algorithm | Transport | accepted | Abbreviation; entropy-regularized variant used |
| **S-0045** | BB | Barzilai-Borwein | Step-size selection in gradient descent | Optimization | accepted | Initials; used in scc/optimizer.py |
| **S-0046** | FD | Finite Difference | Numerical derivative check (tolerance 1e-8 typical) | Numerics | accepted | Abbreviation; for verification |

---

## Symbol Collision Prevention Rules

1. **Case-sensitivity matters:**
   - `u` (lowercase) = cohesion field
   - `U` (uppercase) = forbidden (reserved for future use)

2. **Subscripts vs. Superscripts:**
   - Subscripts (t, j, i) = indices (time, formation, position)
   - Superscripts (j, T) = exponents or field labels (u^j = j-th field)

3. **Operators:**
   - All operators (Cl, D, C, M, L) are capital letters
   - Must not collide with standard notation (no π, e used as custom symbols)

4. **Greek letters:**
   - λ (lambda) = weights/parameters
   - α (alpha), β (beta) = coefficients/thresholds
   - τ (tau) = specific constraint parameter
   - ∇ (nabla) = gradient
   - Σ (capital sigma) = manifold constraint

5. **New symbols must go through registration:**
   - Cannot use symbol in paper/proof without S-xxxx registration
   - Archivist validates before adding to registry

---

## Symbol Conflicts to Avoid

| Symbol | ❌ Incorrect Use | ✅ Correct Use | Status |
|--------|---|---|---|
| `C` | Generic set; constant | Resolvent C_t only; or capital constant | Restricted |
| `D` | Set dimension; data | Distinction operator D_t only | Restricted |
| `M` | Mass (use m_j instead); number of data points | Transport kernel M_{t→s}; manifold M₂ | Restricted |
| `E` | Set (use X instead) | Energy functional E(u) | Restricted |
| `u` | Generic unknown; vector variable | Cohesion field u_t only | Strict |
| `t` | Any time parameter (use s, τ, etc. if needed) | Temporal index in u_t, X_t, Cl_t | Flexible |
| `λ` | Generic Lagrange multiplier | Energy weights λ_cl, λ_sep, λ_bd, λ_tr, λ_rep | Restricted |

---

## Maintenance

- **Added by:** Author (proposal) + Archivist (registration)
- **Reviewed by:** Critic Agent (collision check, clarity)
- **Validation:** find_unregistered_symbols.py scans for new symbols not in registry

---

**Last updated:** 2026-04-12  
**Rows:** 46 symbols (44 active, 2 tentative)  
**See also:** concept_registry.md, glossary.md, naming_convention.md
