---
id: META-0103
type: registry/theorems
status: accepted
last_updated: 2026-04-26
---

# Theorem Registry

**Purpose:** Register all claims (C-xxxx), proofs (P-xxxx), and canonical theorems (T-xxxx, CV-x.y). This is the authoritative index of what has been proved.

**Structure:** Rows are organized by canonical version (CV-1.0, CV-1.1, CV-1.2) then status (active, challenged, deprecated).

---

## Canonical Theorems (Accepted into Canonical Spec)

### Canonical Spec v1.4 (2026-04-26) — Current Version (W4 Extended Close)

**Additions over v1.3** (W4 extended close, 2026-04-26):

| T-ID | Name | Status | Category | Source | Proof | Experiments | Notes |
|------|------|--------|----------|--------|-------|-------------|-------|
| **T-V5b-T** | Pre-Objective Goldstone on Translation-Invariant Graphs | accepted | A | C-0710 | P-0710 | E-0095 (NQ-170b ζ-scan) + E-0096 (NQ-170c graph-class extension + nodal count) + E-0097 (NQ-172 reproducibility) | Sub/super-lattice dichotomy on translation-invariant graphs (torus T^d, cycle C_n); 2D 2-fold doublet with commensurability split; 1D 1-fold Goldstone; ζ_*(G) graph-class dependent; Goldstone nodal count = 2 universal |

**v1.3 → v1.4 release notes (2026-04-26)**:
- Added: 1 Cat A theorem (T-V5b-T) — V5b verification cycle (8 iterations) result.
- Counts: 37A → **38A**, 51 claims → **52 claims**, 73% → **73% fully proved**.
- T classification update (W4 weekly_summary §3): T1 = 2 → **3** (added V5b-T); T2 = 5 → 4 (V5b moved to T1); T3 = 3 → **4** (added V5b-F new finding).
- New finding registered: V5b-F (Partial Goldstone on Boundary-Modified Graphs) — Cat C, NQ-173 carry.
- Reproducibility crisis identified+resolved: NQ-172 (mode-indexing artifact in NQ-170 analysis script).
- W4 scope extended: 2026-04-19 ~ **2026-04-26** (8 days). Per user direction "아직 내용은 전부 W4로 간주해" — 04-26 work is W4 final-day continuation.

### Canonical Spec v1.3 (2026-04-25) — Previous Version (Frozen)

**Additions over v1.2** (W4 merge, 2026-04-19 ~ 2026-04-25):

| T-ID | Name | Status | Category | Source | Proof | Experiments | Notes |
|------|------|--------|----------|--------|-------|-------------|-------|
| **T-PreObj-1** | Pre-Objective Multi-Peak Formation Mechanism | accepted | A | C-0700 | P-0700 | E-0090 (L=12 numerical, 3-digit agreement) + E-0091 (L=32 dichotomy) | F=1 single-disk minimizer non-critical under full SCC; gradient flow attracts to multi-peak F≥2; IC-protocol dichotomy (adaptive bounded vs random ~ L^2.8) |
| **T-PreObj-1G** | Pre-Objective Mechanism Graph-Class Independent | accepted | A | C-0701 | P-0701 | (theoretical, qualitative empirical) | Conclusions (i),(ii) of T-PreObj-1 hold on **any finite connected graph** under (G1)–(G4) hypotheses |
| **Lemma 4** | Quadratic Form Positive Definite (M matrix) | accepted | A | C-0702 | P-0702 | E-0090 | M ∈ R^{2x2} of (g_cl, g_sep) gradients, PD under linear independence; destabilization magnitude Lambda^T M Lambda > 0 |
| **F-1 Resolution Corollary** | F-1 SPLIT-RESOLVED via T-Merge(b) + T-PreObj-1 | accepted | A | (corollary) | (corollary) | — | Pure E_bd portion via T-Merge(b); full SCC portion via T-PreObj-1 (i); see open_problems.md OP-0001 |

**v1.2 → v1.3 release notes (2026-04-25):**
- Added: 2 Cat A theorems (T-PreObj-1, T-PreObj-1G), 1 Cat A lemma (Lemma 4), 1 Cat A corollary (F-1 split-resolution).
- Status changes: C-0550 (F-1), C-0551 (M-1), C-0552 (MO-1) — challenged → resolved/clarified/sidestepped (see Active Claims table below).
- Counts: 35A → **37A**, 49 claims → **51 claims**, 71% → **73% fully proved**.
- Critical blockers: 3 (F-1, M-1, MO-1) → **0** (all resolved/clarified/sidestepped).
- Pending W4 merge (user decision required, deferred): T2 candidates including σ-framework (Lemma 1/2/3, Theorem 3/4), Theorem 1 V5b, Axiom S1' v1, CN15/16/17, Commitment 14/15 v2.

### Canonical Spec v1.2 (2026-04-12) — Previous Version (Frozen)

| T-ID | Name | Status | Category | Source | Proof | Experiments | Notes |
|------|------|--------|----------|--------|-------|-------------|-------|
| **T-1** | Existence of Minimizers | accepted | A | C-0001 | P-0001 | E-0001, E-0002 | SCC minimizer always exists on Σ_m |
| **T-3** | Stability of Interior Minimizers | accepted | A | C-0003 | P-0003 | E-0003 | Hessian positive on interior; local stability |
| **T-6a** | Closure Fixed Point (Existence) | accepted | A | C-0006a | P-0006a | E-0005 | u* = Cl_t(u*) ∃ for all parameters |
| **T-6b** | Closure Fixed Point (Stability) | accepted | A | C-0006b | P-0006b | E-0006 | Closure FP is attracting in stability metric |
| **T-6-Stability** | Stability of Closure FP | accepted | A | C-0006c | P-0006c | E-0007 | Full spectral analysis |
| **T-7** | Enhanced Metastability | accepted | A | C-0007 | P-0007 | E-0008, E-0009 | Residence time > expected near saddle |
| **T-8-Core** | Phase Transition (Core Dominance) | accepted | A | C-0008 | P-0008 | E-0010, E-0011 | Binuclear → mononuclear at critical β |
| **T-8-Full** | Phase Transition (Global) | accepted | A | C-0009 | P-0009 | E-0012, E-0013 | Full energy landscape bifurcation |
| **T-11** | Γ-Convergence | accepted | A | C-0011 | P-0011 | E-0014 | Variational convergence under scaling |
| **T-14** | Gradient Flow | accepted | A | C-0014 | P-0014 | E-0020:E-0022 | Gradient descent converges to minimizer |
| **T-20** | Axiom Consistency | accepted | A | C-0020 | P-0020 | E-0025 | Axioms A1–E mutually consistent |
| **C-Axioms** | Cohomology-Resolvent Alignment | accepted | A | C-0101 | P-0101 | E-0030:E-0032 | C3'' symmetrization complete (upgraded 04-03) |
| **QM-1** | Quantum Mechanical Analogy (Eigenvalue) | accepted | A | C-0110 | P-0110 | E-0040 | Fiedler eigenvalue is binding edge |
| **QM-2** | QM-2 (Spectral Gap) | accepted | A | C-0111 | P-0111 | E-0041 | Spectral gap related to phase transition |
| **QM-3** | QM-3 (Perturbation) | accepted | A | C-0112 | P-0112 | E-0042 | Perturbations stay confined |
| **QM-4** | QM-4 (Commutation) | accepted | A | C-0113 | P-0113 | E-0043 | Operator commutation holds generically |
| **T-Bind-Proj** | Bind Projection (for τ=1/2) | accepted | B | C-0200 | P-0200 | E-0050:E-0052 | Bind projects onto lower Σ_m layers (condition: τ=1/2) |
| **T-Bind-Full** | Bind Projection (General τ) | accepted | C | C-0201 | P-0201 | E-0053 | Very conditional; full τ dependence unclear |
| **Predicate-Energy Bridge** | Energy ↔ Diagnostic Alignment | accepted | A | C-0300 | P-0300 | E-0060:E-0063 | Energy minimization ↔ diagonal optimization (upgraded 04-03) |
| **Deep Core Dom. 2b** | Deep Core Dominance | accepted | A | C-0301 | P-0301 | E-0064, E-0065 | Core is always dominant in asymmetric regime (upgraded 04-03) |
| **T-Persist-1(a)** | Transport Persistence (base) | accepted | C | C-0400 | P-0400 | E-0070 | Conditional: assumes generic parameters |
| **T-Persist-1(b)** | Transport Persistence (basin unconditional) | accepted | A | C-0401 | P-0401 | E-0071, E-0072 | Unconditional: genericity automatic (upgraded 04-03) |
| **T-Persist-1(d)** | Transport Persistence (fixed stratum) | accepted | C | C-0402 | P-0402 | E-0073 | Conditional: on fixed active stratum |
| **T-Persist-1(e)** | Transport Persistence (confinement) | accepted | A | C-0403 | P-0403 | E-0074 | Tight confinement bound (upgraded 04-03) |
| **T-Persist-Full** | Transport Persistence (full composition) | accepted | C | C-0404 | P-0404 | E-0075 | Conditional on multiple regime conditions |
| **T-Persist-K-Sep** | K-field Persistence (well-separated) | accepted | B | C-0500 | P-0500 | E-0076, E-0077 | Conditional: on well-separated regime + per-formation persist |
| **T-Persist-K-Weak** | K-field Persistence (weak coupling) | accepted | C | C-0501 | P-0501 | E-0078 | Conditional: on weakly-interacting regime |
| **T-Persist-K-Unified** | K-field Persistence (parametric) | accepted | B | C-0502 | P-0502 | E-0046, E-0047 | Parametric family (Sep/Weak/Strong); 100% validation (new v1.2) |

---

## Active Claims (Not Yet Canonical) / Resolved Claims

| C-ID | Name | Status | Category (Intended) | Proof (P-ID) | Experiments | Notes |
|------|------|--------|---------|----------|-------------|-------|
| **C-0550** | F-1: K=2 Vacuity Problem | ✅ **SPLIT-RESOLVED (2026-04-24)** | A | P-0700 + T-Merge(b) | E-0090, E-0091 | Pure E_bd portion: T-Merge(b) Cat A pre-existing. Full SCC portion: T-PreObj-1 (i) Cat A. See open_problems.md OP-0001. |
| **C-0551** | M-1: K=1 Always Preferred | ✅ **LAYER-CLARIFIED (2026-04-24)** | A | T-Merge(b) | none | Proved theorem (T-Merge(b)) misframed as problem. Pure E_bd: theorem holds. Full SCC: comparison not framed (Theorem 2 makes F=1 non-critical). |
| **C-0552** | MO-1: Morse Theory Invalid | ⚪ **SIDESTEPPED (2026-04-24)** | A (single-formation) | (sidestep) | none | Single-formation σ-framework operates on Σ_m (no corners). Multi-formation extension to Σ^K_M still open (Phase 5). |
| **C-0553** | Type A/B Classification | challenged | OP | exp65 | E-0065 | exp65 invalidates; Type B never observed (unchanged from v1.2). |
| **C-0600** | K-field Model Selection | tentative (partially addressed) | pending | none | exp66:exp73 | W4 σ-framework + Static/Dynamic Separation (CN15 candidate) provides partial answer; full mechanism still open. |
| **C-0700** | T-PreObj-1 Pre-Objective Mechanism | ✅ **accepted Cat A** | A | P-0700 | E-0090, E-0091 | New 2026-04-24. F=1 disk non-criticality + multi-peak attractor + IC-protocol dichotomy. |
| **C-0701** | T-PreObj-1G Graph-Class Independent | ✅ **accepted Cat A** | A | P-0701 | (theoretical) | New 2026-04-24. Conclusions (i),(ii) hold on any finite connected graph under (G1)–(G4). |
| **C-0702** | Lemma 4 Quadratic Form PD | ✅ **accepted Cat A** | A | P-0702 | E-0090 | New 2026-04-24. M positive definite under g_cl, g_sep linear independence. |
| **C-0710** | T-V5b-T Pre-Objective Goldstone on Translation-Invariant Graphs | ✅ **accepted Cat A** | A | P-0710 | E-0095, E-0096, E-0097 | New 2026-04-26 (W4 extended). Sub/super-lattice spectral dichotomy on torus T^d / cycle C_n; 2D commensurability split; 1D Goldstone; nodal count = 2 universal. After 8 V5b iterations (V1 → V5b''). |
| **C-0711** | V5b-F Partial Goldstone on Boundary-Modified Graphs | tentative | C | P-0711 | E-0096 (free BC partial) | New 2026-04-26 (W4 extended). Cat C new finding. NQ-173 quantification carry. |

---

## Counterexamples & Challenges (X-xxxx)

| X-ID | Refutes | Status | Description | Impact |
|------|---------|--------|-------------|--------|
| **X-0001** | ~~C-0550 (F-1 Validity)~~ — **superseded 2026-04-24** | superseded | Originally: K=2 energy 4.66 vs K=1 energy 2.25. **W4 reframing**: this evidence is the *correct* T-Merge(b) statement, not a refutation. F-1 was misframed as problem. | F-1 SPLIT-RESOLVED via Option D (premise dissolution); see C-0550 entry. |
| **X-0002** | Type A/B Classification | validated | exp65: all configs Type A (0 Type B observed); breaks 04-07 interpretation | Type classification rejected as non-real phenomenon |

---

## Canonical Spec Version History

### CV-1.4 (2026-04-26) — W4 Extended Close: V5b-T Verification + Partial Goldstone Discovery

- **Added Cat A**: T-V5b-T (Pre-Objective Goldstone on Translation-Invariant Graphs) — sub/super-lattice spectral dichotomy with commensurability splitting on 2D torus, 1-fold Goldstone on 1D cycle, universal nodal count.
- **New Cat C finding**: V5b-F (Partial Goldstone on Boundary-Modified Graphs) — boundary lifting mechanism qualitative observation. NQ-173 carry.
- **V5b 8 iterations resolved**: V1 (W4-04-24 morning) → V5b'' (W4-extended 04-26 evening). Healthy iterative refinement pattern.
- **Reproducibility crisis identified+resolved**: NQ-172 (mode-indexing artifact in NQ-170 analysis script). Mode-agnostic detection adopted.
- **σ-framework strengthening**: NQ-141 single-graph empirical → multi-graph (3 classes) empirical Cat A.
- **Count**: 37 + 1 = **38** Category A; 51 + 1 = **52 claims**; 73% fully proved.
- **W4 extended scope**: 2026-04-19 ~ 2026-04-26 (8 days). Per user direction "아직 내용은 전부 W4로 간주해".
- **Source**: `THEORY/logs/weekly/2026-04-W4/weekly_summary.md` (extended close, post-2026-04-26 update); `logs/daily/2026-04-26/04_NQ170c_graph_extension_nodal.md`.

### CV-1.3 (2026-04-25) — W4 Merge: Pre-Objective Mechanism + F-1/M-1/MO-1 Resolution

- **Added Cat A:** T-PreObj-1 (Pre-Objective Multi-Peak Formation Mechanism), T-PreObj-1G (graph-class independent), Lemma 4 (Quadratic form PD).
- **Added Cat A corollary:** F-1 SPLIT-RESOLVED via T-Merge(b) + T-PreObj-1 (i).
- **Critical blocker resolution:** F-1 (OP-0001) split-resolved, M-1 (OP-0002) layer-clarified, MO-1 (OP-0003) sidestepped. **3 → 0** Critical blockers.
- **Status changes:** C-0550, C-0551, C-0552 (challenged → resolved/clarified/sidestepped).
- **Count:** 35 + 2 = **37** Category A; 49 + 2 = **51 claims**; 71% → **73% fully proved**.
- **Pending user decision (T2 candidates, deferred):** σ-framework (Lemma 1/2/3, Theorem 3/4), Theorem 1 V5b, Axiom S1' v1 placement, CN15/16/17 (Static/Dynamic Separation, Protocol-Parameterized observables, σ-labeled FQ), Commitment 14/15 v2.
- **Source:** `THEORY/logs/weekly/2026-04-W4/weekly_summary.md` (W4 closing summary, ~25 pages).

### CV-1.2 (2026-04-12) — Previous Version (Frozen)

### CV-1.0 (2026-04-01)

- **Theorems:** T-1, T-3, T-6a, T-6b, T-6-Stability, T-7, T-8-Core, T-8-Full, T-11, T-14, T-20
- **QM Results:** QM-1, QM-2, QM-3, QM-4 (11 Category A)
- **Provisional:** Predicate-Energy Bridge, Deep Core Dom. 2b (Category B at the time)
- **K-field:** T-Persist-K-Sep (Category B), T-Persist-K-Weak (Category C) 
- **Notes:** Initial comprehensive spec; 35+ theorems claimed

### CV-1.1 (2026-04-03) — PLAN_0403 Tier 1 Complete

- **Upgraded to Category A:**
  - C-Axioms (C3'' symmetrization gap closed)
  - Predicate-Energy Bridge (formalized)
  - Deep Core Dominance 2b (strengthened)
- **New Unconditional Results:**
  - T-Persist-1(b): Basin unconditional via genericity argument
  - T-Persist-1(e): Confinement tight bounds (2.4-3.5×)
- **New:** T-Bind-Full (Category A, τ=1/2 only)
- **Count:** 35 → 38 Category A (3 upgraded)

### CV-1.2 (2026-04-12) — Frozen, with Audit Clarifications

- **Added:** T-Persist-K-Unified (Category B; parametric coverage of Sep/Weak/Strong regimes)
- **Explicit Assumptions:** All K-field theorems now state "fixed K, fixed m" constraint
- **Status Clarifications:**
  - F-1, M-1, MO-1 documented as unresolved (not silently ignored) — *resolved in CV-1.3*
  - Type A/B classification retracted (exp65 invalidated)
  - Morse theory MO-1 vulnerability flagged (mitigation: use existing results, defer full Morse) — *sidestepped in CV-1.3*
- **Count:** 38 + 1 (T-Persist-K-Unified) = 39 theorems (per CV-1.2 release accounting; honest recount 04-07 → 35A/4B/5C/5R)
- **Retracted:** K-Saddle Conjecture, r̄₀ general τ (kept in archive)

---

## Open Problems (OP-xxxx) — Updated 2026-04-25 (W4 close)

| OP-ID | Problem | Severity | Status | Blocker For |
|-------|---------|----------|--------|-------------|
| **OP-0001** | F-1: K=2 vacuous | 🔴 ~~CRITICAL~~ → ✅ | **SPLIT-RESOLVED (2026-04-24)** | (no longer blocking) |
| **OP-0002** | M-1: K=1 preferred | 🔴 ~~CRITICAL~~ → ✅ | **LAYER-CLARIFIED (2026-04-24)** — proved theorem misframed | (no longer blocking) |
| **OP-0003** | MO-1: Morse fails | 🟠 ~~HIGH~~ → ⚪ | **SIDESTEPPED (2026-04-24)** for single-formation σ scope | Multi-formation σ Phase 5 (re-engages) |
| **OP-0004** | Boundary definition precision | 🟡 MEDIUM | tentative (D-0004) | Morphology formalization |
| **OP-0005** | Transport kernel exact form | 🟡 MEDIUM | tentative | Full persist theorem |
| **OP-0006** | Type A/B characterization | 🟠 HIGH | challenged (exp65) | Branch selection theory |
| **OP-0007** | Dynamic topology | 🟢 LOW | seed | Future multi-scale extension |

**W4 changes (2026-04-25):** Critical blockers 3 → **0**. F-1/M-1/MO-1 all resolved/clarified/sidestepped via Theorem 2 family + T-Merge(b) + σ-framework single-formation scope. See `open_problems.md` for detailed entries.

---

## Proof Status Summary (Updated 2026-04-26, post-W4 extended close)

| Status | Count | Examples |
|--------|-------|----------|
| **Category A (Fully Proved)** | **38** (was 37 post-v1.3, 35 pre-W4) | T-1, T-20, QM-1:4, C-Axioms, Predicate-Energy Bridge, T-PreObj-1, T-PreObj-1G, Lemma 4 (W4), **T-V5b-T (W4 extended)**, etc. |
| **Category B (Conditional)** | 4 | T-Bind-Proj (τ=1/2), T-Persist-K-Sep, T-Persist-K-Unified |
| **Category C (Very Conditional)** | 5 + 1 (new finding) | T-Bind-Full (general τ), T-Persist-1(a/d), T-Persist-Full, T-Persist-K-Weak; **V5b-F (new finding 2026-04-26, NQ-173 carry)** |
| **Resolved/Clarified/Sidestepped (W4)** | 3 | C-0550 (F-1 split-resolved), C-0551 (M-1 layer-clarified), C-0552 (MO-1 sidestepped) |
| **Challenged** | 1 | C-0553 (Type A/B) |
| **Retracted** | 2 | K-Saddle Conjecture, r̄₀ general τ |
| **Open (active)** | 4 (was 7) | OP-0004, OP-0005, OP-0006, OP-0007 (Critical 3건은 W4에서 해소) |
| **Reproducibility crises identified+resolved** | 1 | NQ-172 (mode-indexing artifact, 2026-04-26 resolved) |
| **W4-extended carry NQ** | 3 (new) | NQ-173 (V5b-F partial Goldstone), NQ-174 (ζ_* graph-dependence), NQ-175 (3D extension) |

---

## Cross-Reference by Topic

### Single-Formation Theory
- **Existence:** T-1
- **Stability:** T-3, T-6-Stability, T-7
- **Phase Transition:** T-8-Core, T-8-Full
- **Convergence:** T-11, T-14
- **Diagnostics:** T-Bind-Proj/Full, Predicate-Energy Bridge

### Multi-Formation (K-field)
- **Temporal Persistence:** T-Persist-K-Sep, T-Persist-K-Weak, T-Persist-K-Unified
- **Global Stability:** Deep Core Dominance 2b (conditional)
- **Open:** F-1, M-1, OP-0006

### Foundational
- **Consistency:** T-20, C-Axioms
- **Quantum Analogy:** QM-1:4

---

## Maintenance

- **Owned by:** Lead + Archivist
- **Updated:** When new C-xxxx promoted to canonical or P-xxxx completed
- **Validation:** build_dependency_graph.py checks for consistency

---

**Last updated:** 2026-04-26 (W4 extended close + V5b-T canonical merge)
**Total canonical theorems:** 42 = **38 Cat A** + 4 Cat B + 5 Cat C — 5 retracted (52 claims, 73% fully proved)
**Open problems:** 4 active (was 7) — Critical 3건 (F-1, M-1, MO-1) 모두 해소
**Recent W4 additions (2026-04-25)**: T-PreObj-1, T-PreObj-1G, Lemma 4 (Pre-Objective Mechanism graph-class independent), Commitment 14/15, CN15/16/17.
**W4 extended addition (2026-04-26)**: T-V5b-T (Pre-Objective Goldstone on Translation-Invariant Graphs) — sub/super-lattice dichotomy on torus T^d, cycle C_n; 2D doublet commensurability split; 1D Goldstone; nodal count = 2 universal. V5b 8-iteration cycle resolved.
**Pending W5+ (T2/T3 carry)**: NQ-173 (V5b-F partial Goldstone characterization), NQ-174 (ζ_*(graph) precise dependence), NQ-175 (3D extension), σ supporting lemmas (Lemma 1/2/3, Theorem 3/4) §13 entries decision, SF Round 1-5 Cat A merge (Q29-Q34).
**See also:** `weekly_summary.md` (W4 extended close), `open_problems.md` (active OPs), `canonical.md` §13 (theorem catalog)
