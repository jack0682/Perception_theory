# exp05: K_act Markov Chain Stationary Distribution (Claim E)

## Setup

- K_max = 5
- barriers_down = 0.50 (uniform; K->K-1 merger)
- barriers_up = 1.50 (uniform; K->K+1 birth)
- Asymmetry: E_up >> E_down => merger-dominant at low T*
- Gillespie simulation, t_max=200, K_init=5

## Stationary Distributions pi(K)

| T* | K=0 | K=1 | K=2 | K=3 | K=4 | K=5 | K_mode |
|---|---|---|---|---|---|---|---|
| T*=0.20 | 0.993 | 0.007 | 0.000 | 0.000 | 0.000 | 0.000 | K_mode=0 |
| T*=0.50 | 0.865 | 0.117 | 0.016 | 0.002 | 0.000 | 0.000 | K_mode=0 |
| T*=1.00 | 0.634 | 0.233 | 0.086 | 0.032 | 0.012 | 0.004 | K_mode=0 |
| T*=2.00 | 0.414 | 0.251 | 0.152 | 0.092 | 0.056 | 0.034 | K_mode=0 |

## Claim E

At low T* (N-1 asymmetry), K_act concentrates at low K (merger-dominant).
At high T*, distribution spreads over K values.

Status: **SUPPORTED**

Notes:
- low_T_concentrates (pi_low[K<=1] > 0.7): True
  pi_low = [0.993, 0.007, 0.000, 0.000, 0.000, 0.000]
- high_T_spreads (pi_high.max < 0.5): True
  pi_high = [0.414, 0.251, 0.152, 0.092, 0.056, 0.034]

P-F flag: T_star undefined until P-F-A1 Langevin on F_M(P) is formalized.
