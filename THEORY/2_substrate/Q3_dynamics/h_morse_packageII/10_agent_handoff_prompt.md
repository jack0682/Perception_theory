> [!nav] Linked: [[MOC_H_MORSE_packageII]] · [[MOC_Q3_stochastic_dynamics]] · [[THEORY_INDEX]]

# 10 — Next Agent Handoff Prompt

Ready-to-paste prompt for W7-CV114B. Use after this audit (W7-CV114) is complete.

---

```
/oh-my-claudecode:ultraqa
/math
/long-form-math
/aristotle-prover

Task: W7-CV114B — H-MORSE-Local Cat B Proof + Package II Pre-Theorem
       Registration → CV-1.14 Seal Candidate.

You are operating inside the SCC / Perception Theory repository
(/home/jack/Perception_theory).

============================================================
BASELINE (do not reopen)
============================================================

- CV-1.13 SEALED (2026-05-10).
- 59A / 14B / 5C / 5R = 83 claims (~71%).
- HT-3.5.
- T-Temporal-Identity Cat A (all 4 parts).
- H-SINK FULLY CLOSED Cat A.
- P-F-A1 Package I fully Cat A.
- T-P-F-ε0-K Cat B (conditional on H5 = H-MORSE).

W7-CV114 audit (2026-05-11) established:
- Unconditional H-MORSE is FALSE (4 explicit counterexamples).
- H-MORSE must be local + quotient + interior.
- Path B (H-MORSE-Local Cat B) is the recommended CV-1.14 target.

Do NOT reopen:
- H-SINK Cat A.
- T-Temporal-Identity Cat A.
- The deep-core density chain.
- The S-C1 margin correction.

============================================================
W7-CV114 AUDIT FOLDER (read first)
============================================================

THEORY/working/CV114_H_MORSE_PACKAGEII/
    00_index.md
    01_canonical_audit.md
    02_H_MORSE_statement_reconstruction.md
    03_energy_landscape_and_hessian.md
    04_degeneracy_catalogue.md
    05_counterexample_search.md
    06_packageII_dependency_map.md
    07_Eyring_Kramers_requirements.md
    08_candidate_lemma_chain.md
    09_CV114_recommendation.md   ← READ FIRST
    10_agent_handoff_prompt.md   ← this file

============================================================
RECOMMENDED PATH (from W7-CV114 audit)
============================================================

Path B (primary) + Path D (companion).

PRIMARY: H-MORSE-Local Cat B proof
COMPANION: Package II Pre-Theorem Cat B-conditional registration

CV-1.14 deliverable target: +2B → 59A/16B/5C/5R = 85 claims, HT-3.6.

============================================================
EXACT FIRST THEOREM TO ATTACK
============================================================

Theorem H-MORSE-Local (Cat B candidate).

Statement: Let G be a finite connected graph (canonical 15×15 free BC,
n = 225). Let u* ∈ Σ_m^∘ be a non-uniform single-formation local
minimizer of full SCC energy E = λ_cl E_cl + λ_sep E_sep + λ_bd E_bd,
satisfying

  (M-A1) Canonical parameter window:
         a_cl ∈ (0, 4), b_D = 0,
         β/α > 4 λ_2 / |W''(c)| + η  for some η > 0
         (strictly above T8-Full bifurcation threshold).

  (M-A2) Trivial stabilizer: Stab_{Aut(G)}(u*) = {e}.

  (M-A3) Strict interiority: 0 < δ_0 ≤ u*_i ≤ 1 - δ_0  for some δ_0 > 0.

Then the projected Hessian H^proj(u*) = Π_T H_E(u*) Π_T on
T_{u*}Σ_m = 1^⊥ is positive definite, with explicit lower bound

  μ_min(H^proj(u*)) ≥ μ_0(λ_cl, λ_sep, β, a_cl, δ_0, η) > 0,

where μ_0 is derived from:
  - the closure-correction Hessian gap (canonical.md line 1139, Cat A),
  - the T8-Full sub-bifurcation margin η,
  - the closure spectral gap (1 - a_cl/4)^2 = (1 - L_cl)^2 from H-SINK-1.

Status: Cat B (conditional on M-A1 + M-A2 + M-A3).
Cat A path: derive M-A2, M-A3 from canonical T8-Core for the specific
canonical 15×15 minimizer (deferred to CV-1.15).

============================================================
REQUIRED LEMMA CHAIN
============================================================

L1. Π_T = I - n^{-1} 1 1^T projector well-defined.            (Trivial)
L2. E ∈ C^ω on Σ_m^∘ under b_D = 0.                          (Cat A canonical.md §9.2)
L3. Closure-correction Hessian gap (canonical.md line 1139).  (Cat A — USE DIRECTLY)
L4. Orbital decomposition under G_u = {e}: trivial irrep,
    no enforced eigenvalue degeneracy.                         (Cat A canonical.md Thm 1 line 1362)
L5. T8-Full sub-bifurcation: β/α > 4 λ_2/|W''(c)| + η
    excludes the codim-1 bifurcation locus.                    (Cat A T8-Full)
L6. M-A3 strict interiority excludes ∂Σ_m critical points.    (Trivial)
L7. Closure operator spectral norm < 1 under a_cl < 4:
    ||J_Cl||_op ≤ L_cl = a_cl/4 < 1.                          (Cat A H-SINK-1)
L8. NEW: Compose L3 + L4 + L5 + L7 to extract explicit
    μ_0(λ_cl, λ_sep, β, a_cl, δ_0, η).

============================================================
ANTICIPATED BLOCKERS AND RESPONSES
============================================================

B1. M-A2 audit on canonical 15×15 minimizer fails.
    Response: switch to orbital quotient (Theorem 1 canonical) —
    work modulo G_u; prove block-Morse on each irrep.
    Alternative: switch to Path C (Generic H-MORSE), or fall back to
    Path A (audit-only OP-MORSE registration).

B2. M-A3 audit: canonical minimizer has u*_i very close to 0 or 1.
    Response: pin δ_0 from existing exp01 / exp83 data; verify the
    proof's μ_0 lower bound is non-vacuous at the empirical δ_0.

B3. Explicit μ_0 formula requires tightening canonical.md line 1139
    statement.
    Response: extract the proof from canonical (or its source
    THEORY/working/MF/) and re-derive the explicit numerical constant.

B4. T8-Full margin η: needs an explicit choice.
    Response: η can be defined as the canonical parameter offset from
    threshold; canonical 15×15 with β/α ≈ 7+ is well above threshold.

============================================================
PACKAGE II PRE-THEOREM (companion deliverable)
============================================================

After Path B closes, register:

Theorem Package-II-Entry-Conditional (Cat B-conditional).

Statement: Let u^*_1, u^*_2 ∈ Σ_m^∘ be two non-uniform local minimizers
satisfying M-A1, M-A2, M-A3; let s be an index-1 saddle between their
basins satisfying M-A1, M-A2, M-A3. Conditional on:

  (P1) H-MORSE-Local Cat B (this CV-1.14 result),
  (P2) H-MORSE-Saddle (analogous statement at s, OPEN, CV-1.15),
  (P3) ΔE_{1,2} = E(s) - E(u^*_1) > 0 (T-P-F-ε0-K Cat B + barrier
       analysis),
  (P4) T_* > 0 canonical registration (OP-0021, axiomatic),

the reflected Langevin transition rate from basin u^*_1 to basin u^*_2
satisfies the Bouchet-Reygner / Bovier-Den Hollander reflected
Eyring-Kramers formula:

  k_{1→2} = (|λ_-(s)| / 2π) · √(|det Π_T H_E(s) Π_T| /
                                  det Π_T H_E(u^*_1) Π_T) ·
            exp(-ΔE_{1,2}/T_*) · (1 + o(1))  as T_* → 0.

Status: Cat B conditional on P1–P4.

Bibliographic anchors:
  - Bouchet-Reygner 2016 (irreversible / reflected EK)
  - Bovier-Den Hollander 2015 §10–§11
  - Berglund-Gentz 2010 (review)
  - Lions-Sznitman 1984 (reflected SDE; already cited in canonical)

This Pre-Theorem requires NO new mathematics — it is a bibliographic +
notation translation. Effort: ≤ 1 session.

============================================================
CANONICAL UPDATE POLICY
============================================================

At CV-1.14 seal (after Path B + Path D both close):

- canonical.md: add §13 Category B entry for H-MORSE-Local and for
  Package II Pre-Theorem; update header banner to CV-1.14.
- theorem_status.md: add two Cat B rows; update count to 85 claims.
- hypothesis_tree.md: HT-3.5 → HT-3.6; H-MORSE node OPEN → PARTIALLY
  CLOSED; add HT-3.6 row to 변경 이력 table.
- CHANGELOG.md: prepend CV-1.14 W7-CV114B entry.
- canonical/CV-1.14_SEAL.md: create seal document mirroring CV-1.13_SEAL.

Do NOT modify canonical state until both Path B and Path D deliverables
exist as working files and have passed an audit equivalent to S-A1/S-A3/
S-C1.

============================================================
STOP CONDITIONS
============================================================

STOP and seal CV-1.14 when:
  - H-MORSE-Local Cat B proof written, audited, canonicalized.
  - Package II Pre-Theorem Cat B conditional registered.
  - canonical edits made.
  - +2B count increase verified (85 claims).
  - HT-3.6 update written.

STOP and fall back to Path A (audit-only) when:
  - M-A2 + M-A3 cannot be made to hold for canonical 15×15 minimizers
    even with orbital quotient.
  - Explicit μ_0 lower bound cannot be derived.
  - Three sessions elapsed with no positive proof progress.

STOP and switch to Path C (Generic) when:
  - Local proof blocked but generic-perturbation argument cleanly
    available.

============================================================
EXPECTED EFFORT
============================================================

Path B alone: 2–3 sessions.
Path B + Path D: 3–5 sessions.
Full CV-1.14 seal (with canonical edits, daily log, audits): 4–6 sessions.

============================================================
FINAL REPORT IN KOREAN
============================================================

At session end, report:

  1. 새로 생성한 작업 파일 목록.
  2. H-MORSE-Local 증명 상태 (Cat B / Cat A / OPEN).
  3. Package II Pre-Theorem 등록 상태.
  4. canonical 파일 수정 내역.
  5. claim count 변화 (현재 → CV-1.14).
  6. HT version 변화.
  7. CV-1.14 봉인 가능 여부.
  8. 다음 권장 목표 (CV-1.15 후보).
  9. 다음 에이전트 프롬프트 위치.

Do not stop until Path B has a definitive outcome (Cat B proven OR
falls back to Path A with explicit blocker report).
```

---

## Notes for the orchestrator

- The handoff prompt is self-contained; the next agent does not need this audit pre-loaded but should at minimum read `09_CV114_recommendation.md` and `02_H_MORSE_statement_reconstruction.md` for the precise statement.
- Expected canonical changes: only at CV-1.14 seal (after both Path B and Path D deliverables exist as working files).
- If the next agent uncovers an inconsistency in canonical state, it should flag it but not auto-fix without explicit authorization.
- The next agent should NOT attempt full Eyring-Kramers Cat A (Path E) — that is reserved for CV-1.15 or later, after H-MORSE-Saddle and OP-0021 individually close.
