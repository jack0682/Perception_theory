# Exp78 Cross-Config Follow-up on 10x10:0.6

**Date:** 2026-04-11
**Session:** Cycle 66 — third-config search-protocol audit
**Category:** experiment
**Status:** complete
**Depends on:** docs/04-11/experiment/EXP78-CROSS-CONFIG-15x15_c0.6.md; experiments/results/exp78_search_protocol_upgrade_10x10_0.6.json

---

## 1. CURRENT GAP

The remaining question after `20x20:0.6` and `15x15:0.6` was whether search sensitivity also appears in a smaller sentinel where the geometry is cleaner.

---

## 2. Results

| Lambda | Continued total | Best raw-catalog total | Upgraded-direct best total | direct - continued | direct - catalog | Direct best type |
|---:|---:|---:|---:|---:|---:|---|
| 0.10 | 4.835071 | 5.183605 | 4.591157 | -0.243914 | -0.592448 | Type B candidate |
| 0.50 | 4.614395 | 5.186227 | 4.529475 | -0.084920 | -0.656753 | Type B candidate |
| 1.00 | 4.544644 | 5.189506 | 4.511362 | -0.033282 | -0.678144 | Type B candidate |

---

## 3. Main Findings

1. The same qualitative pattern persists on `10x10:0.6`: upgraded direct optimization beats both the raw catalog and the warm continuation branch at all tested lambdas.
2. The improved direct winner remains `Type B candidate` throughout the tested set.
3. So the raw-catalog Type A picture is not just fragile on large or difficult grids; it is also search-sensitive on a smaller sentinel.

---

## 4. Interpretation

With `10x10:0.6`, `15x15:0.6`, and `20x20:0.6` all showing the same failure mode, search sensitivity is now a cross-config pattern rather than a one-off anomaly.

---

## 5. Decision

| Claim | Outcome |
|---|---|
| search sensitivity is confined to a subset of difficult grids | rejected |
| cross-config search-aware branch-selection issue | strongly numerically supported |
| R1-Q closed | no |

---

## 6. Next Trigger

Promote the numerical pattern into an explicit search-aware statement so future theorem wording never conflates discovered branches with selected branches without specifying the search protocol.
