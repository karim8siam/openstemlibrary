# Unit 5: Materials Data Science and Surrogate Models

**Guiding question:** Can a machine-learning materials predictor generalize beyond its training set?

## Problem framing and scale selection

A regression system reports excellent accuracy on randomly split alloy records but fails for a new alloy family. Audit duplicates, leakage, distribution shift, uncertainty, extrapolation, chemistry features and measurement labels. No materials simulation is interpretable until its target observable, reference material state, environmental range and intended downstream decision are fixed. Distinguish a calculated ideal crystal from an actual manufactured material, a numerical fit from independent validation, and a candidate ranking from an authorized design decision. A model should be evaluated by whether it rules out alternatives or informs an observable experiment, not by the complexity of its software or resolution of its graphics.

The unit's evidence record starts with **label and feature provenance plus pre-registered evaluation**. Collect **structures, test conditions, duplicates, splits, representations, random seeds and prediction intervals** and prioritize tests such as **grouped out-of-domain holdouts and prospective laboratory measurements**. The most dangerous untested assumption is **whether apparent accuracy is an artifact of leakage or overlapping material families**. Work backward from that possible failure: identify at least two competing explanations, a calculation that could distinguish them, an independently measurable outcome and a decision threshold. Be explicit if available observations cannot constrain the model. The five lessons progressively build a defensible case record.

## Unit field notebook — initial protocol

State a material formulation, one measurable target property, units, intended temperature/time/composition limits, specimen or simulated domain, governing hypotheses and error tolerance. Record a reference model with minimal complexity; describe where added atomistic, mesoscale, continuum or statistical detail would be necessary. List input uncertainty sources, computational convergence tests, independent measurement plans, future update conditions and rejection criteria. At the end of the unit, turn the notebook into a one-page auditable model-use statement.

## Lesson 5.1 — Materials data provenance and FAIR workflows

### Concept, governing relationships and physical intuition

Computational records need structures, units, methods, convergence settings, code versions and licensing as well as numerical property labels. A materials identifier alone may collapse distinct phases, orientations and processing histories. FAIR principles encourage findable, accessible, interoperable and reusable datasets, yet publication of a CSV does not ensure quality. Material identity and test context must survive transformations.

**Modeling rule:** A useful label is a measured or calculated observable plus state, provenance and uncertainty. Specify the reference state, physical units, validity domain and a verification test before translating this rule into a material decision.

### Competing explanations: what would actually falsify the model?

**Case:** Two property tables have the same composition formula but different elastic moduli and unspecified sample states. Form two mechanisms that predict different observables, then select a discriminating calculation or experiment rather than arguing from graphical fit alone.

**Possible reversal:** Duplicate materials with alternative measurement conditions can poison a benchmark split. Test how changing temperature, composition, specimen condition or discretization could reverse the conclusion. Distinguish calibration agreement from independent verification.

### Synthetic quantitative notebook — inspect a dependency, not a material claim

The companion offline calculator is **Nominal Gaussian predictive half-width** with mathematical expression `1.96*sig`. Its adjustable input is **Residual standard deviation**, measured in property units; output is reported in property units. At an illustrative input of 0.15 property units, the displayed result is **0.294 property units**. A second invented input of 0.4 property units gives **0.784 property units**. The finite-difference response is 1.96 property units per property units. Independently check the result and units. Values are illustrative, not measured material properties or validated predictions.

**Fixed assumptions and failure tests:** Assumes unbiased Gaussian independent residuals and correct σ including model and measurement uncertainty; not guaranteed calibrated out of distribution. Change one declared hidden assumption, identify how the trend might fail, and specify an independent benchmark. The teaching card is not a materials simulation engine.

### Build an evidence and validation protocol

**Targeted measurement or audit:** Audit source documentation, normalize units and hash stable source records before modeling. Define material state, specimen/structure provenance, independent replicates, measurement uncertainty and explicit conditions under which your preferred model would be falsified.

**Minimum reproducibility artifact:** supply an input file, exact method and version, a computational convergence check, independent test values, units and uncertainty. Write a diagnostic table contrasting what is computed, what is physically measured and what the hypothesis still assumes. Retain failed calculations instead of filtering them away, and document material identity and sample history at a level a different laboratory could understand. If the full measurement is unavailable, report a conditional prediction rather than describing the candidate as qualified.

### Design decision and economic consequences

**Competing objectives:** Strict provenance management costs effort but prevents accidental mixing of incomparable labels. Rank alternatives only after hard safety, feasibility and manufacturing requirements are satisfied; record the cost of a false positive and a missed candidate.

### Three substantial practice exercises and solution strategies

**Exercise 1 — physical reconstruction.** Explain “A useful label is a measured or calculated observable plus state, provenance and uncertainty.” in your own notation. Define the system, reference state, units, independent/dependent variables and at least two assumptions. Determine whether conservation, symmetry, force balance or statistical independence should be checked. Sketch one limiting case where the statement should simplify to a known result. **Solution strategy:** the derivation must use consistent dimensions and clearly say what the law does not predict; check an analytic, energy or mass-balance limit where available.

**Exercise 2 — calculation and uncertainty.** From `1.96*sig`, independently derive 0.294 property units for 0.15 property units and compute one additional point halfway between the two example inputs. Estimate the sensitivity using a central perturbation, describe whether nonlinear dependence makes a one-number slope misleading, and add one plausible uncertainty in a fixed assumption. **Solution strategy:** perform an independent numerical calculation, propagate units before rounding, and report the interval conditional on the invented assumptions; do not use the resulting number as an empirical constant.

**Exercise 3 — independent comparison.** For “Two property tables have the same composition formula but different elastic moduli and unspecified sample states.”, design the smallest credible cross-check using **Audit source documentation, normalize units and hash stable source records before modeling.**. Specify two competing hypotheses, an observable they predict differently, necessary independent specimens or structures and a falsification criterion. Explain which observation would force you to abandon the simpler model, and which uncertainty could remain even if the immediate test passed. **Solution strategy:** make the experiment capable of rejecting the preferred mechanism and protect the test from fitting-data leakage or unrecorded sample exclusions.

### Research memo and readiness check

Write an evidence table separating observations, simulations, calibration, independent tests and remaining risk. Propose a small reversible next experiment with a stop/go rule.

<!-- MODEL_8 -->

## Lesson 5.3 — Supervised learning and rigorous splits

### Concept, governing relationships and physical intuition

Regression predicts continuous properties; classification predicts categories with specified label definitions. Training error measures fit, not generalization. Random splits can leak near-duplicate materials or publication series, while group, temporal or composition-family splits test more realistic deployment. Baseline physics and simple regressions are mandatory comparators for deep models.

**Modeling rule:** Evaluation must match the intended deployment distribution and exclude train/test leakage. Specify the reference state, physical units, validity domain and a verification test before translating this rule into a material decision.

### Competing explanations: what would actually falsify the model?

**Case:** A neural network reaches high R² on held-out rows but poor performance on entirely unseen element combinations. Form two mechanisms that predict different observables, then select a discriminating calculation or experiment rather than arguing from graphical fit alone.

**Possible reversal:** Data leakage from repeated calculations or related compositions inflates accuracy. Test how changing temperature, composition, specimen condition or discretization could reverse the conclusion. Distinguish calibration agreement from independent verification.

### Synthetic quantitative notebook — inspect a dependency, not a material claim

The companion offline calculator is **Nominal Gaussian predictive half-width** with mathematical expression `1.96*sig`. Its adjustable input is **Residual standard deviation**, measured in property units; output is reported in property units. At an illustrative input of 0.19 property units, the displayed result is **0.3724 property units**. A second invented input of 0.43 property units gives **0.8428 property units**. The finite-difference response is 1.96 property units per property units. Independently check the result and units. Values are illustrative, not measured material properties or validated predictions.

**Fixed assumptions and failure tests:** Assumes unbiased Gaussian independent residuals and correct σ including model and measurement uncertainty; not guaranteed calibrated out of distribution. Change one declared hidden assumption, identify how the trend might fail, and specify an independent benchmark. The teaching card is not a materials simulation engine.

### Build an evidence and validation protocol

**Targeted measurement or audit:** Pre-register split logic, keep an external test set sealed and inspect residuals by chemistry family. Define material state, specimen/structure provenance, independent replicates, measurement uncertainty and explicit conditions under which your preferred model would be falsified.

**Minimum reproducibility artifact:** supply an input file, exact method and version, a computational convergence check, independent test values, units and uncertainty. Write a diagnostic table contrasting what is computed, what is physically measured and what the hypothesis still assumes. Retain failed calculations instead of filtering them away, and document material identity and sample history at a level a different laboratory could understand. If the full measurement is unavailable, report a conditional prediction rather than describing the candidate as qualified.

### Design decision and economic consequences

**Competing objectives:** More expressive models improve fit but can worsen extrapolation and auditability. Rank alternatives only after hard safety, feasibility and manufacturing requirements are satisfied; record the cost of a false positive and a missed candidate.

### Three substantial practice exercises and solution strategies

**Exercise 1 — physical reconstruction.** Explain “Evaluation must match the intended deployment distribution and exclude train/test leakage.” in your own notation. Define the system, reference state, units, independent/dependent variables and at least two assumptions. Determine whether conservation, symmetry, force balance or statistical independence should be checked. Sketch one limiting case where the statement should simplify to a known result. **Solution strategy:** the derivation must use consistent dimensions and clearly say what the law does not predict; check an analytic, energy or mass-balance limit where available.

**Exercise 2 — calculation and uncertainty.** From `1.96*sig`, independently derive 0.3724 property units for 0.19 property units and compute one additional point halfway between the two example inputs. Estimate the sensitivity using a central perturbation, describe whether nonlinear dependence makes a one-number slope misleading, and add one plausible uncertainty in a fixed assumption. **Solution strategy:** perform an independent numerical calculation, propagate units before rounding, and report the interval conditional on the invented assumptions; do not use the resulting number as an empirical constant.

**Exercise 3 — independent comparison.** For “A neural network reaches high R² on held-out rows but poor performance on entirely unseen element combinations.”, design the smallest credible cross-check using **Pre-register split logic, keep an external test set sealed and inspect residuals by chemistry family.**. Specify two competing hypotheses, an observable they predict differently, necessary independent specimens or structures and a falsification criterion. Explain which observation would force you to abandon the simpler model, and which uncertainty could remain even if the immediate test passed. **Solution strategy:** make the experiment capable of rejecting the preferred mechanism and protect the test from fitting-data leakage or unrecorded sample exclusions.

### Research memo and readiness check

Write an evidence table separating observations, simulations, calibration, independent tests and remaining risk. Propose a small reversible next experiment with a stop/go rule.

<!-- MODEL_9 -->

## Lesson 5.5 — Active learning and design of experiments

### Concept, governing relationships and physical intuition

Active learning uses model uncertainty, expected improvement or diversity to prioritize costly new labels. Selection criteria should reflect experimental availability, expected scientific information and safety constraints. Iterative model updates need a budget ledger and prospective record of every candidate chosen, including failures. A greedy exploitation policy can become trapped near a spurious optimum.

**Modeling rule:** Expected value of a test includes information gain, feasible outcome probability and decision relevance. Specify the reference state, physical units, validity domain and a verification test before translating this rule into a material decision.

### Competing explanations: what would actually falsify the model?

**Case:** A small research group can run only ten new syntheses and must choose whether to sample the most promising or uncertain compositions. Form two mechanisms that predict different observables, then select a discriminating calculation or experiment rather than arguing from graphical fit alone.

**Possible reversal:** Uncertainty rankings may be poorly calibrated or dominated by experimentally impossible points. Test how changing temperature, composition, specimen condition or discretization could reverse the conclusion. Distinguish calibration agreement from independent verification.

### Synthetic quantitative notebook — inspect a dependency, not a material claim

The companion offline calculator is **Nominal Gaussian predictive half-width** with mathematical expression `1.96*sig`. Its adjustable input is **Residual standard deviation**, measured in property units; output is reported in property units. At an illustrative input of 0.23 property units, the displayed result is **0.4508 property units**. A second invented input of 0.46 property units gives **0.9016 property units**. The finite-difference response is 1.96 property units per property units. Independently check the result and units. Values are illustrative, not measured material properties or validated predictions.

**Fixed assumptions and failure tests:** Assumes unbiased Gaussian independent residuals and correct σ including model and measurement uncertainty; not guaranteed calibrated out of distribution. Change one declared hidden assumption, identify how the trend might fail, and specify an independent benchmark. The teaching card is not a materials simulation engine.

### Build an evidence and validation protocol

**Targeted measurement or audit:** Run a budget-matched comparison against random/diversity sampling and monitor independent performance. Define material state, specimen/structure provenance, independent replicates, measurement uncertainty and explicit conditions under which your preferred model would be falsified.

**Minimum reproducibility artifact:** supply an input file, exact method and version, a computational convergence check, independent test values, units and uncertainty. Write a diagnostic table contrasting what is computed, what is physically measured and what the hypothesis still assumes. Retain failed calculations instead of filtering them away, and document material identity and sample history at a level a different laboratory could understand. If the full measurement is unavailable, report a conditional prediction rather than describing the candidate as qualified.

### Design decision and economic consequences

**Competing objectives:** Exploration reduces immediate performance but can improve reliability of later discoveries. Rank alternatives only after hard safety, feasibility and manufacturing requirements are satisfied; record the cost of a false positive and a missed candidate.

### Three substantial practice exercises and solution strategies

**Exercise 1 — physical reconstruction.** Explain “Expected value of a test includes information gain, feasible outcome probability and decision relevance.” in your own notation. Define the system, reference state, units, independent/dependent variables and at least two assumptions. Determine whether conservation, symmetry, force balance or statistical independence should be checked. Sketch one limiting case where the statement should simplify to a known result. **Solution strategy:** the derivation must use consistent dimensions and clearly say what the law does not predict; check an analytic, energy or mass-balance limit where available.

**Exercise 2 — calculation and uncertainty.** From `1.96*sig`, independently derive 0.4508 property units for 0.23 property units and compute one additional point halfway between the two example inputs. Estimate the sensitivity using a central perturbation, describe whether nonlinear dependence makes a one-number slope misleading, and add one plausible uncertainty in a fixed assumption. **Solution strategy:** perform an independent numerical calculation, propagate units before rounding, and report the interval conditional on the invented assumptions; do not use the resulting number as an empirical constant.

**Exercise 3 — independent comparison.** For “A small research group can run only ten new syntheses and must choose whether to sample the most promising or uncertain compositions.”, design the smallest credible cross-check using **Run a budget-matched comparison against random/diversity sampling and monitor independent performance.**. Specify two competing hypotheses, an observable they predict differently, necessary independent specimens or structures and a falsification criterion. Explain which observation would force you to abandon the simpler model, and which uncertainty could remain even if the immediate test passed. **Solution strategy:** make the experiment capable of rejecting the preferred mechanism and protect the test from fitting-data leakage or unrecorded sample exclusions.

### Research memo and readiness check

Write an evidence table separating observations, simulations, calibration, independent tests and remaining risk. Propose a small reversible next experiment with a stop/go rule.

## Unit 5 capstone: integrate calculations with evidence

**Practical challenge:** A regression system reports excellent accuracy on randomly split alloy records but fails for a new alloy family. Audit duplicates, leakage, distribution shift, uncertainty, extrapolation, chemistry features and measurement labels.

1. **Define material state and performance.** State composition, phase/microstructure, processing history, external constraints, independent material specimens and the exact observable to be predicted. State the intended decision and penalty of a wrong choice.
2. **Reproduce quantitative work.** Run both synthetic interactive formulas at three inputs, independently recompute the results, and identify the nonphysical or unmeasured assumptions. Develop one additional first-principles or measured-model benchmark that would test the physics rather than just the code.
3. **Test alternative explanations.** Use **label and feature provenance plus pre-registered evaluation**, explicitly log **structures, test conditions, duplicates, splits, representations, random seeds and prediction intervals**, and challenge the model with **grouped out-of-domain holdouts and prospective laboratory measurements**. Describe an observation that would falsify the preferred hypothesis. Separate calibration, validation and engineering qualification evidence.
4. **Quantify uncertainty and feasibility.** Include one numerical convergence test, one physical or statistical uncertainty propagation, one out-of-domain stress test, one materials supply or production constraint and a feasible low-cost validation plan.
5. **Deliver an auditable recommendation.** Produce a two-page technical decision, reproducibility checklist, complete candidate table and stop/go rule. Explicitly revisit **whether apparent accuracy is an artifact of leakage or overlapping material families**. No synthetic formula output authorizes use of a safety-critical material or device.

### Concluding reflection

A physical model earns trust by surviving attempts to falsify its assumptions within a defined application, not by producing a large dataset or intricate graphics. Distinguish numerical convergence, agreement on fitted points, generalization to new material states and functional qualification of real parts. If any step remains missing, state which research question is answerable and which engineering recommendation must be deferred.

