> [!nav] Linked: [[MOC_experiments_validation]] · [[THEORY_INDEX]]

# exp01: K_act = #PersComp vs Slot-Count

## Results

| Scenario | K_act (PersComp) | K_act (slot-count) |
|---|---|---|
| Two separated blobs | 2 | N/A |
| Single blob | 1 | N/A |
| Noisy two blobs | 2 | 4 |

## Claim A

PersComp correctly counts coherent formations; slot-count over-estimates
when noise activates empty slots.

Status: **SUPPORTED**

Notes:
- rho_pers = 0.05
- two_blobs expected K=2, got 2
- one_blob expected K=1, got 1
- noisy_two_blobs: PersComp=2 (robust), slot-count=4 (inflated)
