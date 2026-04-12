---
title: Proofs Registry
type: index
last_updated: 2026-04-12
total_proofs: 0
---

# Proofs Registry — 07_proofs/

Central registry tracking proof attempts, lemmas, and proof status for all theorems.

## Purpose

Document:
- Complete proofs (Category A: fully rigorous)
- Proof outlines (Category B: conditional or sketch)
- Proof attempts and gaps (Category C: very conditional or incomplete)
- Lemmas and supporting results

## Structure

Organized as:
```
07_proofs/
├── T-xxxx/
│   ├── P-xxxx_proof_main.md
│   ├── L-xxxx_lemma_1.md
│   ├── L-xxxx_lemma_2.md
│   └── PROOF_STATUS.md
```

Each proof file uses: `99_templates/TEMPLATE_proof.md`

**ID Scheme:**
- `P-XXXX` — Main proof for theorem T-XXXX
- `L-XXXX` — Supporting lemma
- `X-XXXX` — Counterexample or proof failure

## Theorem Categories

### Category A: Fully Proved (27 items in v2.1)
✅ Complete, rigorous, peer-reviewed proofs

- [List from theorem_registry.md]

### Category B: Conditional Proofs (3 items)
⚠️ Valid under stated conditions; conditions are testable

- [List from theorem_registry.md]

### Category C: Very Conditional (6 items)
❓ Depends on unresolved assumptions or experimental validation

- [List from theorem_registry.md]

## Proof Status by Theorem

| Theorem | Proof Status | Category | Issues |
|---------|--------------|----------|--------|
| T-xxxx | ✅ Complete | A | None |
| T-xxxx | ⚠️ Conditional | B | [Condition] |
| T-xxxx | ❌ Blocked | C | [What's missing] |

## Lemma Registry

Supporting lemmas, ordered by use:

- L-0001: [Title] — Used in [T-xxxx]
- L-0002: [Title] — Used in [T-xxxx]

## Proof Attempts & Failures

Tracking failed proof attempts:

- X-0001: [What failed and why]
- X-0002: [What failed and why]

---

**Created:** 2026-04-12
**Proof Count:** [Number from theorem_registry]
**Next Review:** When new proofs completed
