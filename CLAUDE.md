> [!nav] Linked: [[THEORY_INDEX]] · [[MOC_canonical_authority]] · [[INDEX|working/INDEX.md]]

# CLAUDE.md

Guidance for Claude Code working on **Soft Cognitive Cohesion (SCC)** — a mathematical theory of how coherent formations emerge prior to discrete objecthood.

## Session Start

Read in order:
1. **`THEORY/0_axis/DECLARATION.md`** — **(DECL-2.0, 2026-05-26) 먼저 읽기.** 중심축: *perception = 가능한 개입(intervention)의 장 형성*; 객체성·affordance·action·control 은 하나의 장 u_t 의 사영(projection). 객체성 = 안정화된 affordance. DECL-1.0 의 objecthood 질문(Q1~Q6, T8)은 §substrate 로 보존. 2분.
1b. **`THEORY/0_axis/CANONICAL_AXIS.md`** + **`PAI_GLOSSARY.md`** — 축의 spine 과 통제 어휘. substrate↔destination 관계와 가드레일.
1c. **`THEORY/0_axis/SCOPE_LEDGER.md`** — 야망-증명 기울기. 증명된 것(Tier 1 = field morphology) vs 방향(Tier 3 = objecthood·actional·𝕌, OPEN). 거시 주장은 티어 태그 의무.
2. **`THEORY/2_substrate/canonical/canonical.md`** — authoritative specification (**CV-1.20**, sealed 2026-05-20). Single source of truth for the theory. Counts: **71A / 20B / 6C / 5R = 102 claims** (~70% fully proved). 증명된 핵심은 *field morphology* (Tier 1); objecthood/actional 은 DIRECTION (SCOPE_LEDGER).
3. **`THEORY/2_substrate/canonical/seals/CV-1.20_SEAL.md`** — 최신 봉인 기록 (seal chain: CV-1.13→…→CV-1.20).
4. **`THEORY/2_substrate/canonical/theorem_status.md`** — theorem index + Open Problems Catalog. Active high-priority OPs: OP-0005, OP-0008, OP-0009, OP-0021; 축 OP: OP-PAI-001..006, OP-UNIFY-1..3, OP-PROLEGOMENA.
5. **`THEORY/2_substrate/canonical/hypothesis_tree.md`** — **(HT-3.12, 2026-05-21)** 의존성 구조 권위 소스. Q1~Q6 + H-PAI branch. 수정 규칙 후미.
6. **`THEORY/CHANGELOG.md`** — theory-side session log; last entry defines carry-forward.

For the reorganization history (what was tried and abandoned), see `_archive/research_os_2026-04-12/` (the original Research OS scaffolding archived 2026-04-18).

## Repository Layout

```
Perception_theory/
├── CLAUDE.md / README.md / CONVENTIONS.md
│
├── CODE/                           executable assets — run from this dir
│   ├── scc/                        Python package (15 modules)
│   ├── tests/                      pytest suite (228 passed, 1 xfailed, 1 pre-existing error)
│   ├── experiments/                exp<N>_<name>.py + results/
│   ├── scripts/                    one-off utilities
│   ├── papers/                     LaTeX + generate_figures.py
│   └── README.md
│
├── THEORY/                         theory documents — read-oriented (perception-action stack, 2026-05-26)
│   ├── CHANGELOG.md                theory state-change log
│   ├── 0_axis/                     ontological center: DECLARATION (DECL-2.0), CANONICAL_AXIS, PAI_GLOSSARY, audit, roadmap
│   ├── 1_sensing/                  raw → field (sensing pipeline)
│   ├── 2_substrate/                cohesion morphology + sealed authority
│   │   ├── canonical/              ← THE spec (canonical.md, CV-1.20) + structural/ (folded SCC-CT) + seals/
│   │   ├── Q1_boundary/ Q2_multiformation/ Q3_dynamics/ Q4_kselection/
│   │   ├── sigma_framework/ multiformation/ foundations/   (+ INDEX.md)
│   ├── 3_projections/              PAI projections (object/affordance/action/control); prolegomena/
│   ├── 4_temporal/                 identity / transport / succession
│   └── logs/                       chronological journal (daily / weekly / monthly)
│
├── private_brainstorm/             personal exploratory notes
└── _archive/                       frozen material — do not edit
    └── research_os_2026-04-12/     abandoned Research OS scaffolding (numbered 00–99; do not revive)
```

## Promotion Pipeline (Contamination Barrier)

```
THEORY/logs/daily/YYYY-MM-DD.md   (raw chronological record)
         ↓ reorganize by topic
THEORY/working/<topic>.md          (active theory development)
         ↓ proof + review + tests
THEORY/2_substrate/canonical/canonical.md      (authoritative — one-way only)
```

**canonical/ accepts only promoted content.** No reverse flow. Retractions stay explicit (inline `*(Retracted YYYY-MM-DD: reason)*`) and are logged in `THEORY/CHANGELOG.md`.

## Policy

- **Do not re-introduce Research OS structure** (open-ended numbered 00–99 dirs, 5-role daily logs, D/S/T/A/E/Q/C/P/X registry files). It was tried 2026-04-12, collapsed 2026-04-16, archived 2026-04-18. **Permitted exception:** the five fixed semantic stack layers `THEORY/0_axis … 4_temporal/` (perception-action pipeline; closed set; see `CONVENTIONS.md` §5–6).
- **`THEORY/2_substrate/canonical/canonical.md` is the single authoritative spec.** Any theorem-status change edits it + `theorem_status.md` + appends to `THEORY/CHANGELOG.md`.
- **No per-item registry files.** Proofs live inside canonical.md sections; theorem index + Open Problems Catalog both live in `theorem_status.md` (single file). The previously separate `open_problems.md` was merged into `theorem_status.md` on 2026-05-04 to eliminate documentation drift.
- **Experiments**: keep `experiments/exp<N>_*.py` numbering stable. No E-xxxx renaming.
- **Run everything from `CODE/`.** Tests and experiments locate `scc` via sys.path relative to `CODE/`.

## Test & Build

```bash
# All tests (228 passed, 1 xfailed, 1 pre-existing error, ~6min)
cd CODE && python3 -m pytest tests/ -v

# Single file
cd CODE && python3 -m pytest tests/test_energy.py -v

# Smoke
cd CODE && python3 -c "from scc import *; g=GraphState.grid_2d(10,10); p=ParameterRegistry(); r=find_formation(g,p); print(r.diagnostics)"

# Experiments
cd CODE && python3 experiments/exp1_lambda_sweep.py

# Paper figures
cd CODE && python3 papers/generate_figures.py
```

## Code Architecture (scc/)

Pipeline: `graph → params → operators → energy → optimizer → diagnostics`.

- **graph.py** — `GraphState` (Laplacian, Fiedler, row-normalized P, cohesion-weighted W_sym)
- **params.py** — `ParameterRegistry` (a_cl<4, spinodal, β_crit validation)
- **operators.py** — `closure`, `distinction`, `aggregation`, `resolvent_diagonal` + exact JVPs
- **energy.py** — `EnergyComputer` (E_cl, E_sep, E_bd + exact gradients, FD-verified 1e-9)
- **optimizer.py** — `find_formation` (semi-implicit projected gradient, BB step, multi-start)
- **diagnostics.py** — `DiagnosticVector` (Bind, Sep, Inside, Persist)
- **multi.py** — K-field, `transport_k_formations` (independent/correction/reoptimize)
- **transport.py** — cohesion fingerprint, Sinkhorn log-domain OT, `persist_transport`
- **k_soft.py** — `k_soft(u)` = Σ φ(ℓᵢ) over H₀ persistence bars; C+E framework soft mode count; φ_sat and φ_lin variants; Lipschitz-certified (L_K ≤ 4·L_φ·n)
- **langevin.py** — Projected Euler-Maruyama SDE sampler on Σ_m; implements F3 axiom (Cat A via Lions-Sznitman); used for Kramers-rate / Freidlin-Wentzell analysis
- **sigma_rich.py** — `SigmaRich` namedtuple (sigma_standard, centroids, orientations, wigner_data); derived diagnostic of u_t for K-jump σ-inheritance (OP-0008 Path B); does not add energy terms
- **predicates.py, resolvent.py, persistence.py** — thin compatibility wrappers

### Critical Implementation Details

- E_bd smoothness: `2α·uᵀLu` → gradient `4α·Lu` (factor 4, ordered-pair sum)
- Double-well: `W'(u) = 2u(1-u)(1-2u)` (factor 2, I6 correction)
- Sep predicate: u-weighted (`Σuᵢ·Dᵢ / Σuᵢ`), NOT C_t-weighted (degenerate)
- `b_D = 0` required for analyticity (Łojasiewicz convergence)
- Persist: core-overlap (`diagnostics.py`) + transport-based `persist_transport` (`transport.py`)

## Ontological Constraints (non-negotiable)

1. **Soft cohesion field `u_t : X_t → [0,1]` is the primitive.** Crisp objects are derivative.
2. **Four energy terms (closure, separation, boundary, transport) are conceptually independent.** Do not merge.
3. **Closure has stabilization tendency (A3), not idempotence.** Deliberately omitted.
4. **Not fuzzy segmentation, not clustering, not tracking.** No engineering proxies.
5. **Never silently resolve open problems** (F-1, M-1, MO-1, co-belonging form, transition operator, crisp recovery). Keep explicit until deliberately resolved via promotion pipeline.

## Theory Sketch (CV-1.20)

Formal universe: `C^soft = (T, {X_t}, {u_t}, {Cl_t}, {N_t, D_t}, {M_{t→s}})`

Energy on `Σ_m = {u ∈ [0,1]^n : Σuᵢ = m}`:
`E = λ_cl·E_cl + λ_sep·E_sep + λ_bd·E_bd + λ_tr·E_tr`

Diagnostic: `d = (Bind, Sep, Inside, Persist) ∈ [0,1]⁴`

Phase transition: `β/α > 4λ₂ / |W''(c)|` with c in spinodal `((3-√3)/6, (3+√3)/6)`.

Full theorem catalog: `THEORY/2_substrate/canonical/canonical.md` §13.
