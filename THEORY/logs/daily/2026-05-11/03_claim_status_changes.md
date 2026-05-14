> [!nav] Linked: [[MOC_research_journal]] · [[THEORY_INDEX]]

# 03 — Claim Status Changes (W7 Arc)

All status changes are dated 2026-05-10 (the actual seal day for CV-1.12 and CV-1.13).

---

## Primary claim status changes

| Claim | Before W7 | After W7-CV1.13 | Notes |
|-------|-----------|-----------------|-------|
| **S-B2 = Lemma 8.2 = H-SINK-S2** | Cat B / pending | **Cat A** | Sinkhorn dual-potential Lipschitz; W7-T1; proof uses DR2 verified from first principles + log-sum-exp |
| **Partial-H-SINK (one-sided OT stability)** | pending / not stated | **Cat A** (new theorem) | SCC E1 is one-sided row-normalized — rows independent — direct row-softmax Lipschitz; W7-FINAL; `partial_ot_stability.md` |
| **H-SINK full theorem (canonical SCC E1)** | OPEN / Cat B | **Cat A** | After Partial-H-SINK closes the partial OT gap; W7-FINAL |
| **Lemma 9 (plan stability under cost perturbation)** | Cat B | **Cat A** | Direct corollary of Theorem Partial-H-SINK; W7-FINAL |
| **Lemma 10 (component confinement)** | Cat B | **Cat A** | Direct corollary of Lemma 9 (Cat A); W7-FINAL |
| **S-B3 = Lemma 11 (kernel independence)** | Cat B conditional | **Cat A conditional** (margin corrected to $2\epsilon_\mathrm{kernel}$) | W7-FINAL + S-C1 margin correction |
| **Lemma S-B1-Weak ($\rho_\mathrm{deep} > \rho_*$, $\Delta_\mathrm{sep} > 0$)** | did not exist | **Cat A** (new) | W7-CV113; positivity path; Γ-convergence + DMP + Theorem 1 CORE-DEPTH-ISOPERIMETRIC |
| **Lemma S-B1-SYM (symbolic identity)** | did not exist | **Cat B** (new) | W7-CV113A; $\rho_\mathrm{deep} \geq \theta_\mathrm{core}(1 - 4C_\mathrm{iso}/\sqrt{m})$ under HWF-1; from Theorem 2b Cat A |
| **Legacy S-B1 Strong (literal $\rho_\mathrm{deep} \geq 0.84$, free-standing)** | working Cat B (pre-W7); Cat B conditional under HWF-1–3 (W7-FINAL) | **superseded / retracted as standalone** | Replaced by ρ_sym; literal 0.84 retained only as evaluation $\rho_\mathrm{sym}(0.2, 25, 1.0)$ (sharp-interface) |
| **T-Temporal-Identity** | working Cat B candidate (not canonical) | **Cat A** (canonical) | Promoted via CV-1.12 (Cat B canonical) → CV-1.13 (Cat A); all four parts certified |
| **OP-SB1-DEEP** | newly registered HIGH-BLOCKING (W7-FINAL) | superseded by OP-SB1-084 | Downgraded NON-BLOCKING (W7-CV113); then superseded (W7-CV113A) |
| **OP-SB1-084** | did not exist | OPEN, **LOW** priority | Successor of OP-SB1-DEEP; not blocking CV-1.13 |
| **OP-0011 (transport kernel exact form)** | STRUCTURED | PARTIALLY RESOLVED (Steps 2–3 Cat A) | W7-FINAL |
| **H-SINK-ENT ($\varepsilon_\mathrm{OT} \geq \varepsilon_\mathrm{min} > 0$)** | implicit, unregistered | registered technical hypothesis | W7-T1 (introduced), W7-FINAL (used canonically) |
| **CV-1.12** | not sealed | **SEALED** | W7-FINAL 2026-05-10; 54A/15B/5C/5R = 79 claims |
| **CV-1.13** | not sealed | **SEALED** | W7-CV1.13 2026-05-10; 59A/14B/5C/5R = 83 claims |

---

## T-Temporal-Identity part-by-part transitions

| Part | Pre-W7 | After W7-FINAL (CV-1.12) | After W7-CV113 (preliminary) | After W7-CV113A | **After W7-CV1.13 (CV-1.13 sealed)** | Basis |
|------|--------|--------------------------|------------------------------|------------------|--------------------------------------|-------|
| (a) Existence of $R_{t \to s}$ | working Cat B | canonical Cat B | canonical Cat B; blocker S-A3 | unchanged | **Cat A** | S-A3 CERTIFIED — finite graph + finite cost gives score matrix finiteness; 5 event types exhaust all cases |
| (b) Uniqueness (stable-K + $\Delta_\mathrm{sep} > 0$) | working Cat B | canonical Cat B (conditional HWF-1–3) | canonical Cat B; $\Delta_\mathrm{sep} > 0$ Cat A via S-B1-Weak | unchanged; quantitative magnitude via S-B1-SYM Cat B | **Cat A** | S-A1 (D-ST-3 integration) + Lemma S-B1-Weak (Cat A) |
| (c) Kernel independence | working Cat B | Cat A conditional (margin $\Delta_\mathrm{sep} \geq \Delta_\mathrm{sep}^* + \epsilon_\mathrm{kernel}$, S-B3 upgraded) | unchanged | unchanged | **Cat A conditional** (corrected margin $+ 2\epsilon_\mathrm{kernel}$) | S-C1 CERTIFIED with correction; Lemmas 9–11 all Cat A; satisfied at canonical parameters $\Delta_\mathrm{sep}^* \approx 0.837 \gg 2\epsilon_\mathrm{kernel}$ |
| (d) K=1 reduction | working Cat B | canonical Cat B | canonical Cat B; blocker S-A1, S-A3 | unchanged | **Cat A** | S-A1 (D-ST-3 consistency) + routine algebra |
| **Overall** | working Cat B | **canonical Cat B (CV-1.12)** | preliminary Cat B + improvements | preliminary Cat B + provenance | **canonical Cat A (CV-1.13)** | — |

---

## Count timeline

| Snapshot | Date | A | B | C | R | Total |
|----------|------|---|---|---|---|-------|
| CV-1.11 (entry) | 2026-05-08 | 54 | 14 | 5 | 5 | 78 |
| CV-1.12 (W7-FINAL) | 2026-05-10 | 54 | 15 | 5 | 5 | 79 |
| CV-1.13 preliminary (W7-CV113) | 2026-05-10 | 55 | 15 | 5 | 5 | 80 |
| CV-1.13 preliminary (W7-CV113A) | 2026-05-10 | 55 | 15 | 5 | 5 | 80 |
| **CV-1.13 SEALED (W7-CV1.13)** | **2026-05-10** | **59** | **14** | **5** | **5** | **83** |

**Net change from CV-1.11 → CV-1.13: +5A, +0B, +0C, +0R = +5 claims.** (Includes +1B for T-Temporal-Identity at CV-1.12, then −1B converted to +4A at CV-1.13.)

---

## Hypothesis tree (HT) version trail

| Phase | HT version |
|-------|-----------|
| Pre-W7 entry | HT-3.0 |
| W7-T1 | HT-3.1 |
| W7-FINAL | HT-3.2 |
| W7-CV113 | HT-3.3 |
| W7-CV113A | HT-3.4 |
| **W7-CV1.13** | **HT-3.5** |

---

## Documentation inconsistency (resolved 2026-05-11)

`THEORY/canonical/hypothesis_tree.md` line 308 ("Modification Protocol" section) previously read "현재: **HT-3.4**" although the frontmatter and rest of the file were HT-3.5 — a non-blocking version-label drift introduced during the HT-3.4 → HT-3.5 update on 2026-05-10 (W7-CV1.13). **Fixed today (2026-05-11):** line 308 updated to "현재: **HT-3.5**", and the variation history table (변경 이력) extended with a new HT-3.5 row documenting CV-1.13 SEALED + T-Temporal-Identity full Cat A. No claim status affected; documentation-only repair.
