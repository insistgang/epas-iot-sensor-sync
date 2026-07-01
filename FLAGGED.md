# FLAGGED

These items require human review before submission. They were not resolved by inventing data or references.

## Must Review Before Submission

1. Ref. [17] is a confirmed bibliographic error.

Current entry:
```latex
M. N. Zaman et al., ``Privacy-preserving machine learning in IoT:
Challenges and opportunities,'' arXiv:2604.07199, 2026
```

Problem: `arXiv:2604.07199` is the timer-synchronization paper now used by Ref. [9], not the Zaman privacy survey. I added TODO comments at the Section 2.2 citation and at the bibitem, but did not invent a replacement.

Human action: find the correct arXiv id/DOI for the Zaman survey, or replace it with a real IoT privacy-ML survey.

2. Confirm simulation code consistency for the trigger statistic.

The manuscript now defines:
```latex
\xi_i(t)=\|x_i(t)-\tilde{x}_i(t_{\mathrm{last}})\|^2
```

Human action: confirm the simulation code computes `xi_i` from the clean current state and the last published noisy value. If the code instead used a noisy current value, Fig. 7 trigger-rate validation may need re-running. No Fig. 7 numbers were changed.

3. Verify all references manually.

Only Ref. [9] was edited using the user-provided verified fix. All other references, especially arXiv-only entries [7], [8], [13], [14], [26], and [29], need manual id-title-author-year checking on arxiv.org or publisher pages.

## Drafted But Needs Human Approval

4. DP positioning paragraph.

I drafted a paragraph clarifying that `\varepsilon` is an operational per-release value-channel calibration target and not a certified sequence-level DP guarantee. This is consistent with the current scope, but the authors should approve the wording before submission.

5. Convergence-factor rigor note.

I added a short note after Eq. (18) stating that `\rho\in(0,1)` needs both the existing upper-side condition and a positivity-side requirement. Human action: re-check the exact inequality and whether the note should remain in the submitted manuscript.

6. Proof coefficient bookkeeping.

Human action: re-check Proof Steps 4-7 in the main convergence theorem. The `(1/2) \kappa_min (1-p_loss) lambda_2 ||e||^2` term from bounding the mismatch cross-term via Young's inequality does not visibly appear in the final `\rho`, which shows `-2 \kappa_min...`, not `-1.5 \kappa_min...`. I did not re-derive or rewrite the proof.

7. Fig. 6 label regeneration.

The visible label for the budget-step scan was changed from `\rho` to `\rho_b` in the figure source. No data changed. Human action: inspect the regenerated Fig. 6 in the compiled PDF for layout/readability.
