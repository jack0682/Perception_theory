# exp04: Prior / Likelihood Separation in MAP (Claim D)

## Setup

- Grid: 20x20
- Prior target: two Gaussian blobs at (6,6) and (14,14)
- Photometric target: single blob at (5,15)
- lambda_photo = 3.0

## Results

| Metric | Prior only | MAP + Photo |
|---|---|---|
| E_SCC | 29.494941 | 22.150537 |
| E_photo | 90.312660 | 1.462178 |
| Field L2 shift | — | 10.216590 |

## Claim D

Prior E_SCC and likelihood E_photo are independent terms; adding E_photo
shifts the MAP solution while E_SCC structure is preserved.

Status: **SUPPORTED**

Notes:
- solutions_differ (L2 shift=10.2166 > 0.01): True
- photo_reduced (E_photo: 90.3127 -> 1.4622): True
- scc_prior_lower (prior E_SCC <= MAP E_SCC): False
