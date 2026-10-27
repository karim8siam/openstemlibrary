# Unit 1: Simulation Foundations and Model Credibility

**Guiding question:** What makes a calculation scientifically useful rather than merely numerical?

## Problem framing and scale selection

A research team proposes a lighter structural alloy from calculations with unknown boundary conditions. Determine what performance must be reproduced, which length scales control failure, and how discretization, numerical error, input uncertainty and experiments will be tracked before screening candidates. No materials simulation is interpretable until its target observable, reference material state, environmental range and intended downstream decision are fixed. Distinguish a calculated ideal crystal from an actual manufactured material, a numerical fit from independent validation, and a candidate ranking from an authorized design decision. A model should be evaluated by whether it rules out alternatives or informs an observable experiment, not by the complexity of its software or resolution of its graphics.

The unit's evidence record starts with **model specification, nondimensional units and boundary checks**. Collect **input state, governing laws, mesh/basis/timestep convergence, solver tolerance and validation observables** and prioritize tests such as **analytic limits, matched independent experiments and conservation residuals**. The most dangerous untested assumption is **whether stable numerical output is actually a prediction of the relevant physical material state**. Work backward from that possible failure: identify at least two competing explanations, a calculation that could distinguish them, an independently measurable outcome and a decision threshold. Be explicit if available observations cannot constrain the model. The five lessons progressively build a defensible case record.

## Unit field notebook — initial protocol

State a material formulation, one measurable target property, units, intended temperature/time/composition limits, specimen or simulated domain, governing hypotheses and error tolerance. Record a reference model with minimal complexity; describe where added atomistic, mesoscale, continuum or statistical detail would be necessary. List input uncertainty sources, computational convergence tests, independent measurement plans, future update conditions and rejection criteria. At the end of the unit, turn the notebook into a one-page auditable model-use statement.

## Lesson 1.1 — Models as structured hypotheses

### Concept, governing relationships and physical intuition

A material model is an explicit mapping from composition, geometry, processing and environment to a defined observable. Molecular, mesoscopic and continuum models answer different questions; no single descriptor captures all scales. Equations express hypotheses about neglected interactions as well as included mechanisms. Start with quantities, units, domain of applicability and one falsifiable predicted trend.

**Modeling rule:** Model output is conditional on state, boundary conditions, constitutive assumptions and observable definition. Specify the reference state, physical units, validity domain and a verification test before translating this rule into a material decision.

### Competing explanations: what would actually falsify the model?

**Case:** A student compares a quantum calculation of ideal defect-free strength with measured tensile strength of a porous product. Form two mechanisms that predict different observables, then select a discriminating calculation or experiment rather than arguing from graphical fit alone.

**Possible reversal:** Ideal strength ignores defect populations, sample geometry, thermal exposure and processing. Test how changing temperature, composition, specimen condition or discretization could reverse the conclusion. Distinguish calibration agreement from independent verification.

### Synthetic quantitative notebook — inspect a dependency, not a material claim

The companion offline calculator is **Toy discretization-error scaling** with mathematical expression `0.02*h*h`. Its adjustable input is **Grid spacing ratio**, measured in dimensionless; output is reported in relative error. At an illustrative input of 0.45 dimensionless, the displayed result is **0.00405 relative error**. A second invented input of 1.3 dimensionless gives **0.0338 relative error**. The finite-difference response is 0.035 relative error per dimensionless. Independently check the result and units. Values are illustrative, not measured material properties or validated predictions.

**Fixed assumptions and failure tests:** Hypothetical second-order error coefficient 0.02; only truncation scaling is represented, not the total error or spatial convergence of any actual PDE code. Change one declared hidden assumption, identify how the trend might fail, and specify an independent benchmark. The teaching card is not a materials simulation engine.

### Build an evidence and validation protocol

**Targeted measurement or audit:** Map every input to provenance and demonstrate one comparison with a measured, independently specified observable. Define material state, specimen/structure provenance, independent replicates, measurement uncertainty and explicit conditions under which your preferred model would be falsified.

**Minimum reproducibility artifact:** supply an input file, exact method and version, a computational convergence check, independent test values, units and uncertainty. Write a diagnostic table contrasting what is computed, what is physically measured and what the hypothesis still assumes. Retain failed calculations instead of filtering them away, and document material identity and sample history at a level a different laboratory could understand. If the full measurement is unavailable, report a conditional prediction rather than describing the candidate as qualified.

### Design decision and economic consequences

**Competing objectives:** Greater physical detail increases computation and parameter requirements, and is not always the best predictive model. Rank alternatives only after hard safety, feasibility and manufacturing requirements are satisfied; record the cost of a false positive and a missed candidate.

### Three substantial practice exercises and solution strategies

**Exercise 1 — physical reconstruction.** Explain “Model output is conditional on state, boundary conditions, constitutive assumptions and observable definition.” in your own notation. Define the system, reference state, units, independent/dependent variables and at least two assumptions. Determine whether conservation, symmetry, force balance or statistical independence should be checked. Sketch one limiting case where the statement should simplify to a known result. **Solution strategy:** the derivation must use consistent dimensions and clearly say what the law does not predict; check an analytic, energy or mass-balance limit where available.

**Exercise 2 — calculation and uncertainty.** From `0.02*h*h`, independently derive 0.00405 relative error for 0.45 dimensionless and compute one additional point halfway between the two example inputs. Estimate the sensitivity using a central perturbation, describe whether nonlinear dependence makes a one-number slope misleading, and add one plausible uncertainty in a fixed assumption. **Solution strategy:** perform an independent numerical calculation, propagate units before rounding, and report the interval conditional on the invented assumptions; do not use the resulting number as an empirical constant.

**Exercise 3 — independent comparison.** For “A student compares a quantum calculation of ideal defect-free strength with measured tensile strength of a porous product.”, design the smallest credible cross-check using **Map every input to provenance and demonstrate one comparison with a measured, independently specified observable.**. Specify two competing hypotheses, an observable they predict differently, necessary independent specimens or structures and a falsification criterion. Explain which observation would force you to abandon the simpler model, and which uncertainty could remain even if the immediate test passed. **Solution strategy:** make the experiment capable of rejecting the preferred mechanism and protect the test from fitting-data leakage or unrecorded sample exclusions.

### Research memo and readiness check

Write an evidence table separating observations, simulations, calibration, independent tests and remaining risk. Propose a small reversible next experiment with a stop/go rule.

<!-- MODEL_0 -->

## Lesson 1.3 — Discretization, convergence and stability

### Concept, governing relationships and physical intuition

Numerical discretization approximates derivatives, integrals or eigenproblems over a finite basis or mesh. Convergence means a chosen observable approaches a stable value with increasing resolution; a tiny iterative residual on one coarse mesh is not evidence of spatial accuracy. Examine order of accuracy, element aspect ratio, timestep restrictions and stopping tolerances separately.

**Modeling rule:** Total reported error can include discretization, solver, parameter and model-form contributions. Specify the reference state, physical units, validity domain and a verification test before translating this rule into a material decision.

### Competing explanations: what would actually falsify the model?

**Case:** A finite-element design appears 9% lighter after switching to a coarse mesh. Form two mechanisms that predict different observables, then select a discriminating calculation or experiment rather than arguing from graphical fit alone.

**Possible reversal:** A visually smooth plot can mask stress singularities and insufficient crack-tip resolution. Test how changing temperature, composition, specimen condition or discretization could reverse the conclusion. Distinguish calibration agreement from independent verification.

### Synthetic quantitative notebook — inspect a dependency, not a material claim

The companion offline calculator is **Toy discretization-error scaling** with mathematical expression `0.02*h*h`. Its adjustable input is **Grid spacing ratio**, measured in dimensionless; output is reported in relative error. At an illustrative input of 0.6 dimensionless, the displayed result is **0.0072 relative error**. A second invented input of 1.4 dimensionless gives **0.0392 relative error**. The finite-difference response is 0.04 relative error per dimensionless. Independently check the result and units. Values are illustrative, not measured material properties or validated predictions.

**Fixed assumptions and failure tests:** Hypothetical second-order error coefficient 0.02; only truncation scaling is represented, not the total error or spatial convergence of any actual PDE code. Change one declared hidden assumption, identify how the trend might fail, and specify an independent benchmark. The teaching card is not a materials simulation engine.

### Build an evidence and validation protocol

**Targeted measurement or audit:** Compare at least three systematically refined resolutions, preserve raw data and use observable-specific convergence criteria. Define material state, specimen/structure provenance, independent replicates, measurement uncertainty and explicit conditions under which your preferred model would be falsified.

**Minimum reproducibility artifact:** supply an input file, exact method and version, a computational convergence check, independent test values, units and uncertainty. Write a diagnostic table contrasting what is computed, what is physically measured and what the hypothesis still assumes. Retain failed calculations instead of filtering them away, and document material identity and sample history at a level a different laboratory could understand. If the full measurement is unavailable, report a conditional prediction rather than describing the candidate as qualified.

### Design decision and economic consequences

**Competing objectives:** Fine grids cost memory and time; refine near gradients without falsely claiming global convergence. Rank alternatives only after hard safety, feasibility and manufacturing requirements are satisfied; record the cost of a false positive and a missed candidate.

### Three substantial practice exercises and solution strategies

**Exercise 1 — physical reconstruction.** Explain “Total reported error can include discretization, solver, parameter and model-form contributions.” in your own notation. Define the system, reference state, units, independent/dependent variables and at least two assumptions. Determine whether conservation, symmetry, force balance or statistical independence should be checked. Sketch one limiting case where the statement should simplify to a known result. **Solution strategy:** the derivation must use consistent dimensions and clearly say what the law does not predict; check an analytic, energy or mass-balance limit where available.

**Exercise 2 — calculation and uncertainty.** From `0.02*h*h`, independently derive 0.0072 relative error for 0.6 dimensionless and compute one additional point halfway between the two example inputs. Estimate the sensitivity using a central perturbation, describe whether nonlinear dependence makes a one-number slope misleading, and add one plausible uncertainty in a fixed assumption. **Solution strategy:** perform an independent numerical calculation, propagate units before rounding, and report the interval conditional on the invented assumptions; do not use the resulting number as an empirical constant.

**Exercise 3 — independent comparison.** For “A finite-element design appears 9% lighter after switching to a coarse mesh.”, design the smallest credible cross-check using **Compare at least three systematically refined resolutions, preserve raw data and use observable-specific convergence criteria.**. Specify two competing hypotheses, an observable they predict differently, necessary independent specimens or structures and a falsification criterion. Explain which observation would force you to abandon the simpler model, and which uncertainty could remain even if the immediate test passed. **Solution strategy:** make the experiment capable of rejecting the preferred mechanism and protect the test from fitting-data leakage or unrecorded sample exclusions.

### Research memo and readiness check

Write an evidence table separating observations, simulations, calibration, independent tests and remaining risk. Propose a small reversible next experiment with a stop/go rule.

<!-- MODEL_1 -->

## Lesson 1.5 — Verification, validation and reproducibility

### Concept, governing relationships and physical intuition

Verification asks whether equations were solved correctly; validation asks whether the chosen equations adequately predict reality for a defined use. Regression tests and analytical limits support verification, whereas independent experiments and uncertainty-aware comparisons support validation. Reproducibility additionally requires exact inputs, software version, seeds, scripts, checksums and environment details.

**Modeling rule:** Predictive credibility requires tested implementation, applicable physics and out-of-sample evidence. Specify the reference state, physical units, validity domain and a verification test before translating this rule into a material decision.

### Competing explanations: what would actually falsify the model?

**Case:** A simulation matches an experiment only after tuning three parameters to that exact data series. Form two mechanisms that predict different observables, then select a discriminating calculation or experiment rather than arguing from graphical fit alone.

**Possible reversal:** Calibration agreement cannot be reused as independent validation evidence. Test how changing temperature, composition, specimen condition or discretization could reverse the conclusion. Distinguish calibration agreement from independent verification.

### Synthetic quantitative notebook — inspect a dependency, not a material claim

The companion offline calculator is **Toy discretization-error scaling** with mathematical expression `0.02*h*h`. Its adjustable input is **Grid spacing ratio**, measured in dimensionless; output is reported in relative error. At an illustrative input of 0.75 dimensionless, the displayed result is **0.01125 relative error**. A second invented input of 1.55 dimensionless gives **0.04805 relative error**. The finite-difference response is 0.046 relative error per dimensionless. Independently check the result and units. Values are illustrative, not measured material properties or validated predictions.

**Fixed assumptions and failure tests:** Hypothetical second-order error coefficient 0.02; only truncation scaling is represented, not the total error or spatial convergence of any actual PDE code. Change one declared hidden assumption, identify how the trend might fail, and specify an independent benchmark. The teaching card is not a materials simulation engine.

### Build an evidence and validation protocol

**Targeted measurement or audit:** Use conservation benchmarks, manufactured or analytic solutions and a sealed independent experimental test. Define material state, specimen/structure provenance, independent replicates, measurement uncertainty and explicit conditions under which your preferred model would be falsified.

**Minimum reproducibility artifact:** supply an input file, exact method and version, a computational convergence check, independent test values, units and uncertainty. Write a diagnostic table contrasting what is computed, what is physically measured and what the hypothesis still assumes. Retain failed calculations instead of filtering them away, and document material identity and sample history at a level a different laboratory could understand. If the full measurement is unavailable, report a conditional prediction rather than describing the candidate as qualified.

### Design decision and economic consequences

**Competing objectives:** Documentation overhead is real but far smaller than the cost of irreproducible design decisions. Rank alternatives only after hard safety, feasibility and manufacturing requirements are satisfied; record the cost of a false positive and a missed candidate.

### Three substantial practice exercises and solution strategies

**Exercise 1 — physical reconstruction.** Explain “Predictive credibility requires tested implementation, applicable physics and out-of-sample evidence.” in your own notation. Define the system, reference state, units, independent/dependent variables and at least two assumptions. Determine whether conservation, symmetry, force balance or statistical independence should be checked. Sketch one limiting case where the statement should simplify to a known result. **Solution strategy:** the derivation must use consistent dimensions and clearly say what the law does not predict; check an analytic, energy or mass-balance limit where available.

**Exercise 2 — calculation and uncertainty.** From `0.02*h*h`, independently derive 0.01125 relative error for 0.75 dimensionless and compute one additional point halfway between the two example inputs. Estimate the sensitivity using a central perturbation, describe whether nonlinear dependence makes a one-number slope misleading, and add one plausible uncertainty in a fixed assumption. **Solution strategy:** perform an independent numerical calculation, propagate units before rounding, and report the interval conditional on the invented assumptions; do not use the resulting number as an empirical constant.

**Exercise 3 — independent comparison.** For “A simulation matches an experiment only after tuning three parameters to that exact data series.”, design the smallest credible cross-check using **Use conservation benchmarks, manufactured or analytic solutions and a sealed independent experimental test.**. Specify two competing hypotheses, an observable they predict differently, necessary independent specimens or structures and a falsification criterion. Explain which observation would force you to abandon the simpler model, and which uncertainty could remain even if the immediate test passed. **Solution strategy:** make the experiment capable of rejecting the preferred mechanism and protect the test from fitting-data leakage or unrecorded sample exclusions.

### Research memo and readiness check

Write an evidence table separating observations, simulations, calibration, independent tests and remaining risk. Propose a small reversible next experiment with a stop/go rule.

## Unit 1 capstone: integrate calculations with evidence

**Practical challenge:** A research team proposes a lighter structural alloy from calculations with unknown boundary conditions. Determine what performance must be reproduced, which length scales control failure, and how discretization, numerical error, input uncertainty and experiments will be tracked before screening candidates.

1. **Define material state and performance.** State composition, phase/microstructure, processing history, external constraints, independent material specimens and the exact observable to be predicted. State the intended decision and penalty of a wrong choice.
2. **Reproduce quantitative work.** Run both synthetic interactive formulas at three inputs, independently recompute the results, and identify the nonphysical or unmeasured assumptions. Develop one additional first-principles or measured-model benchmark that would test the physics rather than just the code.
3. **Test alternative explanations.** Use **model specification, nondimensional units and boundary checks**, explicitly log **input state, governing laws, mesh/basis/timestep convergence, solver tolerance and validation observables**, and challenge the model with **analytic limits, matched independent experiments and conservation residuals**. Describe an observation that would falsify the preferred hypothesis. Separate calibration, validation and engineering qualification evidence.
4. **Quantify uncertainty and feasibility.** Include one numerical convergence test, one physical or statistical uncertainty propagation, one out-of-domain stress test, one materials supply or production constraint and a feasible low-cost validation plan.
5. **Deliver an auditable recommendation.** Produce a two-page technical decision, reproducibility checklist, complete candidate table and stop/go rule. Explicitly revisit **whether stable numerical output is actually a prediction of the relevant physical material state**. No synthetic formula output authorizes use of a safety-critical material or device.

### Concluding reflection

A physical model earns trust by surviving attempts to falsify its assumptions within a defined application, not by producing a large dataset or intricate graphics. Distinguish numerical convergence, agreement on fitted points, generalization to new material states and functional qualification of real parts. If any step remains missing, state which research question is answerable and which engineering recommendation must be deferred.

