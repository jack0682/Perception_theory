# Exp78 Search-Protocol Upgrade on 20x20:0.6

**Date:** 2026-04-11
**Session:** Cycle 64 — direct optimization with injected continuation seed
**Category:** experiment
**Status:** complete
**Depends on:** docs/04-11/experiment/EXP77-SELECTION-VS-PERSISTENCE-20x20_c0.6.md; experiments/exp78_search_protocol_upgrade.py

---

## 1. CURRENT GAP

Exp77 showed that the persistent seeded Type B continuation already beats every branch found by the raw catalog search. The next question was whether that persistent branch is itself the best branch the optimizer can find once the search protocol is upgraded.

---

## 2. Upgrade Rule

For representative lambdas `0.1, 0.5, 1.0`:

1. recover the zero-lambda Type B seed;
2. warm-continue it to the target lambda;
3. rerun direct optimization at that lambda with the continued branch supplied as an initializer/restart candidate;
4. compare three totals:
   - continued branch,
   - best raw-catalog branch,
   - best branch returned by the upgraded direct optimization.

---

## 3. Results

| Lambda | Continued total | Best raw-catalog total | Upgraded-direct best total | direct - continued | direct - catalog | Direct best type |
|---:|---:|---:|---:|---:|---:|---|
| 0.10 | 19.187927 | 20.392262 | 18.338833 | -0.849093 | -2.053429 | Type B candidate |
| 0.50 | 18.388390 | 21.761029 | 17.981141 | -0.407249 | -3.779888 | Type B candidate |
| 1.00 | 18.002577 | 23.471988 | 17.515833 | -0.486743 | -5.956155 | Type B candidate |

---

## 4. Main Findings

1. **The search upgrade matters immediately.** At every tested lambda, direct optimization with the continuation seed returns a branch better than both the raw-catalog winner and the continued branch itself.
2. **The improved best branch stays in the Type B family.** All upgraded-direct winners are still labeled `Type B candidate`.
3. **The energy gain is substantial relative to the raw catalog.** The upgraded search beats the raw catalog by roughly `2.05`, `3.78`, and `5.96` energy units at `lambda = 0.1, 0.5, 1.0` respectively.

---

## 5. Interpretation

This is the clearest diagnosis so far of the active R1-Q bottleneck:

- branch existence is not the main problem;
- branch persistence is not the main problem;
- even selection-versus-persistence was still one layer too shallow;
- the dominant issue is now **optimizer/search reliability**.

On the hardest sentinel `20x20:0.6`, the selected-branch picture changes materially once the optimizer is given access to the recovered continuation branch. Therefore any inference from raw multistart search alone is unsafe.

Safe statement:

> **NUMERICAL SUPPORT ONLY:** on `20x20:0.6`, injecting the recovered continuation branch into direct optimization yields a lower-energy Type B branch than either the raw catalog winner or the plain continued branch, so selected-branch conclusions are highly search-protocol dependent.

---

## 6. Decision

| Claim | Outcome |
|---|---|
| raw catalog search is adequate for selected-branch inference on `20x20:0.6` | rejected |
| persistent continuation branch is already search-optimal | rejected |
| upgraded direct optimization still prefers Type B at tested lambdas | numerical support |
| R1-Q closed | no |

---

## 7. Next Trigger

Generalize the upgraded search test:

> extend the injected-seed optimization protocol to additional lambdas/configs and determine whether the search-upgraded Type B dominance is a local sentinel phenomenon or a broader branch-selection pattern.
