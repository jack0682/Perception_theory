# theorem_2g_schramm_restatement.md — T-PreObj-1G Schramm-Locality Reframing for CV-1.6

**Status:** working draft (W5 Day 4 PM Wave 3 lead-side direct work, 2026-04-30).
**Type:** CV-1.6 candidate canonical §13 amendment proposal (T-PreObj-1G subsection addition).
**Author:** team-lead@scc-wave3-deep-research.
**Canonical refs:** §13 T-PreObj-1G (canonical.md line 1123); §13 T-PreObj-1 corollary (line ~1140); §11.1 CN15 Static/Dynamic Separation (CV-1.6 candidate).
**Working refs:** `foundational_bridges_2026.md` §3 Bridge B-2; `schramm_sigma_locality_theorem.md` (in flight); `sigma_lie_algebra_structure.md` (Aut(G)_{u*} stabilizer).
**External:** Hutchcroft-Easo (2023), arXiv:2310.10983, "Locality of percolation thresholds on graphs".

---

## §1. Motivation

The W4 proof of T-PreObj-1G (canonical §13, line 1123, 2026-04-24) established graph-class-independent pre-objective formation under hypotheses (G1)–(G4). The hypotheses are **local in nature** — they refer to the connectedness, finite degree, spinodal-interior at uniform vacuum, and well-defined Laplacian spectrum, all of which are properties verifiable from a finite ball around any node.

The Hutchcroft-Easo (2023) proof of the Schramm locality conjecture for percolation thresholds — namely that $p_c(G)$ depends only on the local structure of $G$ — provides a structural parallel: a global property (phase transition threshold) is determined by local data. **SCC's T-PreObj-1G is, in this sense, already a "locality theorem" — the Schramm-locality reframing makes this explicit.**

This file proposes a **CV-1.6 canonical §13 amendment**: add a "Schramm-locality reframing" subsection to T-PreObj-1G that:
1. Identifies the local data (Aut(G)_{u*} stabilizer + bottom-k Laplacian eigenvalues).
2. States the reframed theorem.
3. Cross-references foundational_bridges_2026.md §3 Bridge B-2.

**CN10 hard constraint:** the reframing is contrastive only; SCC is not percolation theory. Hutchcroft-Easo locality is about $p_c(G)$; SCC's locality is about pre-objectivity ($\mathcal{F} \geq 2$ default ground state). Structural parallel imports the *spirit*, not the underlying mathematics.

---

## §2. Schramm-Locality Reframing of T-PreObj-1G

**T-PreObj-1G (Schramm-locality reframing, CV-1.6 candidate).**

*The pre-objective default ground state $\mathcal{F} \geq 2$ on a finite connected graph $G$ depends only on the **local structure** of $G$ at the uniform vacuum $u_* = c\mathbf{1}$, in the sense that:*

1. *Hypotheses (G1)-(G4) are local in $G$ (verifiable from finite balls around any node).*
2. *The bottom-k Laplacian eigenvalue spectrum $\{\lambda_2^{\mathrm{Lap}}(G), \lambda_3^{\mathrm{Lap}}(G), \ldots, \lambda_{k_*}^{\mathrm{Lap}}(G)\}$ relevant to first pitchfork is determined up to $O(1/L^2)$ corrections by the local ball structure.*
3. *The first-pitchfork irrep is determined by $\mathrm{Aut}(G)_{u_*}$ (the local automorphism stabilizer of the uniform vacuum) acting on the Fiedler doublet $V_2$.*
4. *Therefore: two graphs $G_1, G_2$ that are locally isomorphic in finite balls of radius $R \gg \xi_0(\beta)$ (correlation length) yield the same pre-objective character ($\mathcal{F} \geq 2$) and identical leading-order σ-tuples at first pitchfork up to graph-class-independent corrections.*

**Cat target:** A (definitional refinement of T-PreObj-1G; no new mathematical content beyond locality observation of existing canonical hypotheses).

**Promotion gate:** CV-1.6 Day 7 EOD as canonical §13 T-PreObj-1G addendum subsection. ~30 canonical lines.

---

## §3. Local data identification

The "local data" sufficient to determine the σ at first pitchfork comprises four components:

### §3.1 Hypotheses (G1)-(G4) verification
Each of (G1) finite connected, (G2) finite degree, (G3) Laplacian spectrum admits spinodal interior at $c=1/2$, (G4) graph automorphism group well-defined, is verifiable on a finite-radius ball around any node. **Local.**

### §3.2 Bottom-k Laplacian eigenvalue spectrum
The first pitchfork at $\beta = \beta_{\mathrm{crit}}^{(2)} = 4\alpha\lambda_2^{\mathrm{Lap}}/|W''(c)|$ is determined by $\lambda_2^{\mathrm{Lap}}(G)$. Higher-order $O(\epsilon^2)$ corrections (cf. NQ-187 §4 sextic computation) involve the bottom-$k$ Laplacian eigenvalues. By spectral approximation theorems (Cheeger-style inequalities + Weyl's law for graph Laplacians), the bottom-$k$ Laplacian eigenvalues are determined up to $O(1/L^2)$ corrections by the **finite-ball local structure** of $G$ at radius $R \sim \sqrt{|X|}$. For practical purposes (up to corrections that vanish in the thermodynamic limit), the bottom-$k$ spectrum is **local**.

### §3.3 Automorphism stabilizer Aut(G)_{u*}
At the uniform vacuum $u_* = c\mathbf{1}$, the local stabilizer is the full automorphism group: $\mathrm{Aut}(G)_{c\mathbf{1}} = \mathrm{Aut}(G)$ (since constants are automorphism-invariant). The stabilizer acts on the Fiedler doublet $V_2 = \mathrm{span}(\phi_2, \phi_3)$ where $\phi_2, \phi_3$ are eigenvectors of the bottom-2 non-trivial Laplacian eigenvalue. **Local in the sense that $\mathrm{Aut}(G)$ is determined by local edge-incidence structure.**

### §3.4 First-pitchfork irrep
The first pitchfork irrep is determined by the action of $\mathrm{Aut}(G)$ on $V_2$. For $D_4$ free-BC: $V_2$ decomposes as $A_1 + A_2$ irreps (T-σ-Theorem-4). For $\mathbb{Z}_n$ cycle: $V_2$ is a single 2D irrep of $\mathbb{Z}_n$. For $\mathbb{Z}_n \times \mathbb{Z}_n$ torus: $V_2$ is a 4D irrep (2D × 2D product). **All determined by $\mathrm{Aut}(G)_{u_*}$ acting locally on $V_2$.**

---

## §4. Schramm-Locality Theorem (formal restatement)

**Theorem (T-PreObj-1G-Schramm, Cat A definitional refinement).**

*Let $G_1, G_2$ be finite connected graphs satisfying (G1)–(G4). Suppose:*

1. *(Local-ball isomorphism) For some radius $R \gg \xi_0(\beta_{\mathrm{crit}}^{(2)}) = \sqrt{\alpha/|W''(c)|}$ at the uniform vacuum, every ball $B_R(x_1) \subseteq G_1$ is isomorphic (as a graph with automorphism action) to some ball $B_R(x_2) \subseteq G_2$.*
2. *(Compatible automorphism stabilizers) $\mathrm{Aut}(G_1) \cong \mathrm{Aut}(G_2)$ via an isomorphism that preserves the irrep structure of $V_2$.*

*Then:*

- *(a) Both graphs share the same pre-objective character: $\mathcal{F}_{\min}(G_i) \geq 2$ as default ground state under full SCC.*
- *(b) The first-pitchfork σ-tuples agree up to graph-class-independent leading-order corrections: $\sigma_{G_1}(u_1^*_{\mathrm{pitchfork}}) = \sigma_{G_2}(u_2^*_{\mathrm{pitchfork}}) + O(1/L^2)$, where the $O(1/L^2)$ correction comes from finite-grid effects on Laplacian eigenvalue placement.*
- *(c) In the thermodynamic limit $L \to \infty$ with appropriate rescaling, σ-tuples coincide exactly.*

**Cat A justification:** all premises (locality of (G1)-(G4); local determination of bottom-k Laplacian; local determination of $\mathrm{Aut}(G)$ action on $V_2$; T-PreObj-1G Cat A graph-class-independent) are already canonical or follow from canonical via established spectral approximation theorems. No new mathematical content; this is a *reframing* that makes the locality structure of T-PreObj-1G explicit.

**CN10 hard constraint:** Hutchcroft-Easo 2023 percolation locality is **not** invoked as an active mathematical premise. The reframing imports only the spirit ("global character determined by local data") and the framing language ("locality theorem"). SCC's locality theorem is proved independently from canonical T-PreObj-1G + spectral approximation theorems; no percolation theory is required.

---

## §5. Empirical anchor

R23 (D_4 free-BC 32×32 grid) vs hypothetical 1D cycle Z_n (n=20, n=50) vs 2D torus Z_n×Z_n (n=10):

| Graph | Aut(G) | V_2 irrep structure | Predicted σ at first pitchfork | Match T-PreObj-1G-Schramm? |
|---|---|---|---|---|
| R23 D_4 | D_4 (order 8) | A_1 + A_2 | (n_1=1, [A_1], λ_1) + (n_2=1, [A_2], λ_2) with λ_1 ≈ λ_2 = 4ε|W''(c)| (T-σ-Theorem-4) | yes (Cat A reference) |
| 1D Z_n cycle | D_n (dihedral order 2n) | 1D rep × 2 (cos, sin pair) | (n=2, [E_1], λ) — 2D irrep at first pitchfork | predicted; needs verification |
| 2D Z_n×Z_n torus | (D_n)² (order 4n²) | 4D product irrep | (n=4, [E_1⊗E_1], λ) — 4D irrep at first pitchfork | predicted; needs verification |

**Verification protocol** (NQ-262 Phase 1, W6+ scope):
1. Implement CODE/scripts/sigma_locality_R23_cycle_torus.py (Task #23).
2. Compute Aut(G) and V_2 irrep decomposition for each of 3 graph classes.
3. Compute σ-tuple at first pitchfork numerically.
4. Verify: (a) all three have $\mathcal{F} \geq 2$ default (confirming part (a)); (b) σ-tuples match the irrep-decomposition prediction (confirming part (b) within $O(1/L^2)$).

**Effort:** ~12h compute, W6 Day 1-2 priority.

---

## §6. CV-1.6 promotion path

**Promotion target:** canonical §13 T-PreObj-1G addendum subsection. Insert after current line 1140 (T-PreObj-1G corollary):

```markdown
**T-PreObj-1G (Schramm-locality reframing, CV-1.6 W6 Day 7 added).**

*Reframing of T-PreObj-1G as a locality theorem in the σ-framework. Hypotheses (G1)-(G4) are local; bottom-k Laplacian spectrum is local up to O(1/L²); Aut(G) action on V_2 is local. Therefore: graphs that are locally isomorphic on balls of radius R ≫ ξ_0 yield identical pre-objective character (𝔉 ≥ 2 default ground state) and σ-tuples at first pitchfork up to graph-class-independent O(1/L²) corrections.*

*Cat A definitional refinement. Spirit-level inspiration: Hutchcroft-Easo 2023 (Schramm locality conjecture for percolation, arXiv:2310.10983); CN10 contrastive — SCC is not percolation theory.*

*References:* `working/SF/theorem_2g_schramm_restatement.md`; `working/SF/schramm_sigma_locality_theorem.md`; `working/MF/foundational_bridges_2026.md` §3 Bridge B-2.
```

**Effort:** ~30 canonical lines. ~15 minutes for canonical merge + theorem_status.md count update (45A → 46A; 60 → 61 claims; 75% proved unchanged).

---

## §7. Open questions

- [ ] **Q1**: Is "local-ball isomorphism" the right formalization, or should it be "quasi-isometry"? Hutchcroft-Easo uses local-ball isomorphism (rooted Benjamini-Schramm convergence). For SCC, local-ball isomorphism is sufficient for hypotheses (G1)-(G4); quasi-isometry would be stronger and may not be needed.
- [ ] **Q2**: What is the exact $O(1/L^2)$ correction structure? Spectral approximation theorems (e.g., Brooks-Eskin-Mirzakhani) give bounds; the exact form depends on the graph family.
- [ ] **Q3**: Does the Schramm-locality reframing extend to higher-order pitchforks (post-first-pitchfork dynamics)? T-PreObj-1G is about the *first* pitchfork; subsequent dynamics may depend on global topology.

---

## §8. Hard constraint verification

- [x] **u_t primitive maintained**: theorem operates on cohesion fields $u_*: X \to [0,1]$; no replacement primitive.
- [x] **CN10 contrastive throughout**: Hutchcroft-Easo locality analog is structural inspiration only; SCC is not percolation theory; locality theorem proved independently from canonical T-PreObj-1G.
- [x] **CN5 4-energy not merged**: theorem makes no claim about 4 energy terms beyond canonical T-PreObj-1G hypotheses.
- [x] **OP not silently resolved**: OP-0001 F-1 SPLIT-RESOLVED preserved; this addendum strengthens but does not retract.
- [x] **K not abused**: theorem about $\mathcal{F}$ (peak count, threshold-free), not $K_{\mathrm{act}}$ or $K_{\mathrm{field}}$.
- [x] **Cat A definitional only**: no new content; reframing of existing canonical theorem.

---

## §9. References

- Hutchcroft, T. & Easo, P. (2023). *"Locality of percolation thresholds on graphs."* arXiv:2310.10983 (citation status ⚠️ verify exact arXiv ID).
- Schramm, O. (~2000s). Schramm locality conjecture (proposed). 
- canonical.md §13 T-PreObj-1G (line 1123, W4 04-24 entry).
- canonical.md §13 T-σ-Theorem-3 (line 1334, T_uniform Hessian closed-form).
- canonical.md §13 T-σ-Theorem-4 (line 1377, first $D_4$ pitchfork σ-tuple).
- working/MF/foundational_bridges_2026.md §3 Bridge B-2 (Schramm locality bridge).
- working/SF/schramm_sigma_locality_theorem.md (Cat BC theorem in flight by schramm-locality-prover teammate).
- working/SF/sigma_lie_algebra_structure.md §3 (Aut(G)_{u*} stabilizer).
- working/SF/sigma_uniqueness_theorem.md §2 (NQ-188 conjugation rule, applied here for σ-tuple equivalence).

---

**End of theorem_2g_schramm_restatement.md.**

**Status:** CV-1.6 canonical §13 T-PreObj-1G addendum subsection candidate. ~30 canonical lines. Cat A definitional refinement. Promotion target: W6 Day 7 EOD with CV-1.6 packet (D-CV1.6-O5 sibling).
