# CHANGES

This file records the guarded manuscript edits applied on 2026-07-01. No experimental numbers, table values, data arrays, or simulation outputs were changed.

## Reference Fixes

1. Ref. [9] `zhou2026timer_sync` was replaced with the user-provided verified bibliographic data.

Before:
```latex
T. Zhou, C. Wang, M. Z. Win, J. K. Dauwels, M. H. Ahmed, and W. Saad,
``Timer synchronization in IoT networks,'' arXiv:2603.13570, 2026
```

After:
```latex
Z. Zhou, T. Cao, C. Shen, J. Zhang, Y. Liu, and H.-W. Huang,
``Multiprotocol Wireless Timer Synchronization for IoT Systems,'' arXiv:2604.07199, 2026
```

2. Ref. [17] `zaman2026iot_privacy` was not replaced. A TODO was added at the Section 2.2 citation and at the bibitem.

Added:
```latex
% TODO(ref-17): arXiv:2604.07199 is wrong for the Zaman et al. privacy survey; it is the timer-sync paper.
```

## Trigger Statistic Logic

Location: Condition A, Algorithm 1, and Assumption 5.7.

Before:
```latex
\xi_i(t)=\|\tilde{x}_i(t)-\tilde{x}_i(t_{\mathrm{last}})\|^2
```

After:
```latex
\xi_i(t)=\|x_i(t)-\tilde{x}_i(t_{\mathrm{last}})\|^2
```

Algorithm 1 now states that the statistic is computed from the local clean state and the last published noisy value.

## Symbol De-collision

### `\rho` vs. `\rho_b`

Occurrence audit before edit:
- Budget update equation used `\rho(p_i(t)-\bar p)`.
- Section 6.7 text and Fig. 6 caption used budget step `\rho`.
- Convergence theorem, proof, settling-time bound, trade-off bound, and energy bound used contraction factor `\rho`.

Changed only the budget-step uses:
```latex
1-\rho(p_i(t)-\bar p)
```
to:
```latex
1-\rho_b(r_i(t)-\bar r)
```

The convergence-factor `\rho` occurrences were left unchanged.

### `\lambda_1,\lambda_2,\lambda_3` vs. Laplacian eigenvalues

Occurrence audit before edit:
- `\lambda_2,\lambda_N` and `\lambda_1\leq\lambda_2\leq\cdots\leq\lambda_N` are graph eigenvalues.
- Eq. (8) used `\lambda_1,\lambda_2,\lambda_3` as adaptive gain coefficients.

Changed only Eq. (8):
```latex
\lambda_1(...)+\lambda_2(...)+\lambda_3(...)
```
to:
```latex
g_1(...)+g_2(...)+g_3(...)
```

### Communication Set

Occurrence audit before edit:
- `|\mathcal{C}_i(t)|` occurred in the communication energy equation.
- The sensitivity shorthand `C_i` remained a separate symbol in the TGM calibration equation.

Changed:
```latex
\alpha|\mathcal{C}_i(t)|(P_{\mathrm{TX}}+P_{\mathrm{RX}})
```
to:
```latex
\alpha|\mathcal{N}_i(t)|(P_{\mathrm{TX}}+P_{\mathrm{RX}})
```

### Trigger Rates

Occurrence audit before edit:
- `p_i(t)` and `\bar p` occurred only in the budget update equation.
- AR order `p` was left unchanged.

Changed:
```latex
p_i(t), \bar p
```
to:
```latex
r_i(t), \bar r
```

The notation table now includes `\rho_b`, `g_1,g_2,g_3`, and `r_i(t),\bar r`.

## Scalability Analysis

Location: Section 6.6.

Before:
```latex
\subsection{Scalability Analysis}

\begin{table}[htbp]
```

After:
```latex
\subsection{Scalability Analysis}\label{sec:scalability}

In Table~\ref{tab:scale}, ``Ideal MSE'' denotes the no-privacy-noise setting ...
```

The added paragraph explains only values already present in Table 4: ideal MSE range, 93.1% communication reduction, 0.074 relative energy, and runtime growth from 0.071 ms to 0.382 ms. Table 4 was cross-referenced against Table 3.

## Consistency Polish

1. Added scenario tags to communication/energy percentages:
- Abstract: `about 92% (privacy setting)`.
- Energy proof: `about 91.2% (privacy setting)`.
- Section 6.8: `roughly 91%, privacy setting`.
- Table 4: `93.1% (ideal, no-noise setting)`.

2. Unified section references from hard-coded forms such as `Section~VI`, `Section~VI-E`, `Section~V-F`, and `Section~4.6` to `Section~\ref{...}` or `Proposition~\ref{...}`.

3. Added a clause after paired Cohen's `d`:
```latex
the very large effect size follows from the near-deterministic, tiny-variance
(approximately $10^{-5}$) steady-state behavior
```

## Drafted Human-Review Notes in the Manuscript

1. Added a draft paragraph near the TGM privacy scope clarifying that `\varepsilon` is an operational per-release value-channel calibration target and an input for later composition/RDP analysis.

2. Added a draft note after Eq. (18) that `\rho\in(0,1)` needs both the stated upper-side condition and a positivity-side requirement.

## Figure Label Source

Changed only the visible Fig. 6(b) budget-step label from `\rho` to `\rho_b` in:
- `generate_polished_figures.py`
- `figures_tikz/parameter_sensitivity_scan.tex`

No plotted data arrays or experimental numbers were changed.
