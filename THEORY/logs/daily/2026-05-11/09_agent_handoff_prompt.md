# 09 — Agent Handoff Prompt: W7-CV114 Entry Audit

This is a ready-to-run prompt for the next agent. Copy from below the dividing line and execute.

The next session is an **audit / entry**, not a proof session. Goal: reconstruct H-MORSE, map Package II dependencies, identify routes and blockers, and produce a CV-1.14 candidate plan.

---

```
/oh-my-claudecode:ultraqa

Task: W7-CV114 — H-MORSE and Package II Entry Audit

You are operating inside the SCC / Perception Theory repository
(/home/jack/Perception_theory).

Mode:
- Use ultraqa for repository-wide audit and reconstruction work.
- Time limit: none.
- Token limit: none.
- Do not perform full H-MORSE proof.
- Do not perform full Package II / Eyring-Kramers proof.
- Do not change theorem statuses unless a documentation inconsistency
  is discovered.
- This is an audit, dependency-mapping, and proof-plan preparation
  session.

============================================================
CURRENT BASELINE
============================================================

- Canonical version: CV-1.13 SEALED (2026-05-10).
- Claim count: 59A / 14B / 5C / 5R = 83 claims (~71%).
- Hypothesis tree: HT-3.5.
- T-Temporal-Identity: full Cat A (parts a,b,c,d).
- H-SINK: FULLY CLOSED Cat A.
- Single-formation temporal identity arc is closed.

Do NOT reopen any of:
- H-SINK Cat A.
- T-Temporal-Identity Cat A.
- The deep-core density chain (S-B1-Weak Cat A; S-B1-SYM Cat B; literal
  0.84 retracted as standalone, preserved as ρ_sym(0.2, 25, 1.0)).
- The S-C1 margin correction (Δ_sep ≥ Δ_sep* + 2 ε_kernel).

Note: the earlier HT-3.4 leftover label on line ~308 of
hypothesis_tree.md was repaired on 2026-05-11. The Modification
Protocol section now correctly reads "현재: HT-3.5", and the 변경 이력
table includes an explicit HT-3.5 row.

============================================================
MISSION
============================================================

Inspect H-MORSE / Package II working files and produce:

1. The exact reconstructed H-MORSE statement (or candidate forms if
   multiple drafts exist).
2. A full Package II dependency map (downstream of H-MORSE).
3. A proof-route list with at least three independent routes.
4. A blocker list with explicit attribution per route.
5. A CV-1.14 candidate proof plan: sequenced sub-tasks with estimated
   session counts.

Do not expand prematurely into full dynamic K-selection unless the
prerequisites (H-MORSE statement, P-F-A1 Package II audit, T_*
registration plan) are all clearly mapped first.

============================================================
INSPECT THESE FILES FIRST
============================================================

Required reading (in order):

    THEORY/canonical/DECLARATION.md
    THEORY/canonical/hypothesis_tree.md (especially Q3 / H-MORSE block)
    THEORY/canonical/canonical.md (§13 — Category B / T-PF-ε0-K;
                                   §13 Category A — T-PF-A1 Package I)
    THEORY/canonical/theorem_status.md (T-PF-A1 Package I; T-P-F-ε0;
                                        T-P-F-ε0-K; T-K-Select-*)
    THEORY/canonical/CV-1.13_SEAL.md
    THEORY/logs/daily/2026-05-11/ (this folder — for full W7 context)

Search the working tree for:

    H-MORSE
    Morse stability
    Morse-Bott
    Eyring-Kramers
    Package II
    Friedlin-Wentzell
    Bovier
    saddle index
    Hessian
    T-PF-ε0-K
    T-PF-A1
    OP-0021
    H-T*
    Σ_m
    polytope critical point
    metastability
    capacity estimate

Likely locations:

    THEORY/working/MF/pf_tstar_langevin.md
    THEORY/working/MF/pf_a1_lions_sznitman_freidlin_route.md
    THEORY/working/MF/op_0006_boundary_precision.md (T-OP6-B; H1–H5)
    THEORY/working/MF/k_select_pf_equilibrium.md
    THEORY/working/MF/k_select_obs_posterior.md
    THEORY/working/MF/emergent_multi_formation_synthesis.md
      (T-MF-Synthesis future candidate)
    THEORY/working/observer_moduli/
    THEORY/logs/daily/2026-05-06/ (Sessions H-I, Q-R, S-T-Y — P-F-A1
                                   Package I + K-Selection canonical)

============================================================
WHAT TO PRODUCE
============================================================

Create a working directory:

    THEORY/working/morse/

If different naming is conventional, follow the repository convention.
Suggested files:

    00_h_morse_statement_reconstruction.md
    01_package_ii_dependency_map.md
    02_proof_route_list.md
    03_blocker_list.md
    04_cv114_candidate_plan.md
    05_open_questions_for_user.md (if escalation is needed)

If the repository prefers a single audit document, fold all sections
into one file (e.g., THEORY/working/morse/W7_CV114_AUDIT.md).

============================================================
RECONSTRUCT H-MORSE STATEMENT
============================================================

The likely H-MORSE form (verify against working files):

> For every critical point u* of E on the volume-constrained polytope
> Σ_m = {u ∈ [0,1]^n : Σ_x u(x) = m}, the Hessian H(u*) projected
> onto T_{u*} Σ_m has μ_min > 0 modulo symmetry-induced zero
> eigenvalues.

Verify exact form. Identify:
- Which energy E is meant (full SCC vs. restricted variant).
- How the projection is defined.
- What symmetry quotient is used.
- Whether interior + boundary critical points are both covered.

============================================================
PACKAGE II DEPENDENCY MAP
============================================================

Likely graph (verify):

    H-MORSE ──┐
              ├──→ T-PF-ε0-K Cat B → Cat A
              │
              ├──→ Eyring-Kramers prefactor
              │     │
              │     └──→ Γ_{K → K±1}
              │            │
              │            └──→ Dynamic K-selection
              │                  │
              │                  └──→ D-ST-4 rate claims
              │
              └──→ H-SR via Hessian spectral structure
                    │
                    └──→ T-Persist-K-Sep/Weak unconditionalization

    P-F-A1 Package I (Cat A) ────┐
    H-T* / OP-0021 (axiomatic) ──┴──→ Package II (Eyring-Kramers)

Identify the precise downstream consumers and the exact form in which
H-MORSE feeds them.

============================================================
PROOF ROUTES — AT LEAST THREE
============================================================

For H-MORSE specifically, sketch at least three candidate proof routes:

Route 1 — Generic perturbation + Smale transversality
Route 2 — Explicit Morse decomposition under β > 7α (Allen-Cahn style)
Route 3 — Finite-dim Morse on Σ_m polytope + stratified Morse on
          boundary (Goresky-MacPherson)

Optional Route 4 — Morse-Bott + Bismut-Lebeau lift (if symmetry zero
modes are unresolvable).

For each route:
- Statement form.
- Method.
- Required new hypotheses (if any).
- Estimated session count.
- Blocker list.

============================================================
EXPLICIT NON-GOALS FOR THIS SESSION
============================================================

Do NOT:
- Attempt full H-MORSE proof.
- Attempt full Package II / Eyring-Kramers proof.
- Attempt OP-0008 σ-inheritance proof.
- Attempt OP-0021 T_* canonical registration.
- Change theorem statuses except for documentation inconsistencies.
- Erase or rewrite W7 work or the CV-1.13 seal.
- Restore the literal 0.84 as a standalone theorem constant.
- Re-introduce Research OS structure or per-item registry files.

DO:
- Reconstruct exact statements from working files.
- Build the dependency graph.
- Identify routes and blockers.
- Produce a candidate CV-1.14 proof plan with effort estimates.

============================================================
ESTIMATED EFFORT
============================================================

- Entry audit: 1–2 sessions.
- CV-1.14 seal estimate (post-audit): 3–6 sessions depending on
  Morse-degeneracy resolution.

============================================================
CONSISTENCY CHECKS
============================================================

After producing the audit, run:

    1. ls THEORY/working/morse/                (folder exists)
    2. grep -R "H-MORSE statement" THEORY/working/morse/
    3. grep -R "Package II"        THEORY/working/morse/
    4. grep -R "T-PF-ε0-K"        THEORY/working/morse/
    5. grep -R "blocker"           THEORY/working/morse/
    6. grep -R "OP-0021"           THEORY/working/morse/

Each grep should return at least one substantive hit if the audit is
complete.

============================================================
FINAL REPORT IN KOREAN
============================================================

End your session with a Korean report including:

    1. 생성한 폴더와 파일 경로.
    2. H-MORSE 정확한 진술 (또는 후보).
    3. Package II 의존성 그래프 요약.
    4. 식별된 증명 경로 (최소 3개).
    5. 식별된 차단 요인 (route별).
    6. CV-1.14 후보 세션 계획.
    7. 다음 권장 행동 (auditor handoff 또는 prove H-MORSE-1).

Do not stop until the W7-CV114 entry audit is complete.
```

---

## Notes for the orchestrator

- The prompt above is self-contained — the next agent does not need this folder pre-loaded, but it will be more efficient if `THEORY/logs/daily/2026-05-11/` is read first.
- The expected output is an audit folder under `THEORY/working/morse/` (or single audit document), **not** any canonical-spec change.
- If the agent uncovers an inconsistency in canonical state, it should flag it but not auto-fix without explicit authorization. (The HT-3.4 → HT-3.5 line-308 drift in `hypothesis_tree.md` was already repaired on 2026-05-11.)
- The agent should not invoke H-MORSE proof prematurely; the audit deliverable is itself the entry contribution.
