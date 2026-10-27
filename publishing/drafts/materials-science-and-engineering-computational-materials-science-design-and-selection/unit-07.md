# Unit 7: Inverse Design, Optimization and Verification

**Guiding question:** How can a computational workflow propose designs without optimizing a flawed model?

## Problem framing and scale selection

An optimizer identifies an apparently ideal composition at the edge of a design domain. Check validity regions, manufacturing constraints, competing objectives, robust margins and cost of physical confirmation. No materials simulation is interpretable until its target observable, reference material state, environmental range and intended downstream decision are fixed. Distinguish a calculated ideal crystal from an actual manufactured material, a numerical fit from independent validation, and a candidate ranking from an authorized design decision. A model should be evaluated by whether it rules out alternatives or informs an observable experiment, not by the complexity of its software or resolution of its graphics.

The unit's evidence record starts with **objective, feasible domain and optimization audit**. Collect **parameter bounds, physical constraints, optimizer starts, surrogate applicability and uncertainty** and prioritize tests such as **higher-fidelity rechecks and independent experimental confirmations**. The most dangerous untested assumption is **whether model exploitation at an extrapolation boundary manufactures a spurious optimum**. Work backward from that possible failure: identify at least two competing explanations, a calculation that could distinguish them, an independently measurable outcome and a decision threshold. Be explicit if available observations cannot constrain the model. The five lessons progressively build a defensible case record.

## Unit field notebook — initial protocol

State a material formulation, one measurable target property, units, intended temperature/time/composition limits, specimen or simulated domain, governing hypotheses and error tolerance. Record a reference model with minimal complexity; describe where added atomistic, mesoscale, continuum or statistical detail would be necessary. List input uncertainty sources, computational convergence tests, independent measurement plans, future update conditions and rejection criteria. At the end of the unit, turn the notebook into a one-page auditable model-use statement.

## Lesson 7.1 — Forward models versus inverse design

### Concept, governing relationships and physical intuition

Forward models map material configuration to properties; inverse design seeks configurations satisfying specified properties and feasibility constraints. The inverse map is generally many-to-one and may not be unique or well posed. Optimization must operate inside the model validity region, not just inside formal variable bounds. The goal is tested candidates, not attractive parameter vectors.

**Modeling rule:** Optimization should minimize a declared loss subject to stoichiometry, manufacturability and safety feasibility. Specify the reference state, physical units, validity domain and a verification test before translating this rule into a material decision.

### Competing explanations: what would actually falsify the model?

**Case:** An algorithm requests negative porosity or an unmanufacturable crystal composition to reach a target strength. Form two mechanisms that predict different observables, then select a discriminating calculation or experiment rather than arguing from graphical fit alone.

**Possible reversal:** Surrogate extrapolation can create false maxima at domain edges. Test how changing temperature, composition, specimen condition or discretization could reverse the conclusion. Distinguish calibration agreement from independent verification.

### Synthetic quantitative notebook — inspect a dependency, not a material claim

The companion offline calculator is **Linear two-phase rule of mixtures** with mathematical expression `120*(x/100)+80*(1-x/100)`. Its adjustable input is **Volume fraction of stiff phase**, measured in %; output is reported in GPa. At an illustrative input of 18 %, the displayed result is **87.2 GPa**. A second invented input of 64 % gives **105.6 GPa**. The finite-difference response is 0.4 GPa per %. Independently check the result and units. Values are illustrative, not measured material properties or validated predictions.

**Fixed assumptions and failure tests:** Invented phase moduli 120 and 80 GPa with iso-strain upper-bound ideal mixture, perfect bonding and no porosity or geometry dependence. Change one declared hidden assumption, identify how the trend might fail, and specify an independent benchmark. The teaching card is not a materials simulation engine.

### Build an evidence and validation protocol

**Targeted measurement or audit:** Re-evaluate final candidates with higher-fidelity methods and explicitly test feasibility. Define material state, specimen/structure provenance, independent replicates, measurement uncertainty and explicit conditions under which your preferred model would be falsified.

**Minimum reproducibility artifact:** supply an input file, exact method and version, a computational convergence check, independent test values, units and uncertainty. Write a diagnostic table contrasting what is computed, what is physically measured and what the hypothesis still assumes. Retain failed calculations instead of filtering them away, and document material identity and sample history at a level a different laboratory could understand. If the full measurement is unavailable, report a conditional prediction rather than describing the candidate as qualified.

### Design decision and economic consequences

**Competing objectives:** Tightening constraints may reduce headline performance but yield usable designs. Rank alternatives only after hard safety, feasibility and manufacturing requirements are satisfied; record the cost of a false positive and a missed candidate.

### Three substantial practice exercises and solution strategies

**Exercise 1 — physical reconstruction.** Explain “Optimization should minimize a declared loss subject to stoichiometry, manufacturability and safety feasibility.” in your own notation. Define the system, reference state, units, independent/dependent variables and at least two assumptions. Determine whether conservation, symmetry, force balance or statistical independence should be checked. Sketch one limiting case where the statement should simplify to a known result. **Solution strategy:** the derivation must use consistent dimensions and clearly say what the law does not predict; check an analytic, energy or mass-balance limit where available.

**Exercise 2 — calculation and uncertainty.** From `120*(x/100)+80*(1-x/100)`, independently derive 87.2 GPa for 18 % and compute one additional point halfway between the two example inputs. Estimate the sensitivity using a central perturbation, describe whether nonlinear dependence makes a one-number slope misleading, and add one plausible uncertainty in a fixed assumption. **Solution strategy:** perform an independent numerical calculation, propagate units before rounding, and report the interval conditional on the invented assumptions; do not use the resulting number as an empirical constant.

**Exercise 3 — independent comparison.** For “An algorithm requests negative porosity or an unmanufacturable crystal composition to reach a target strength.”, design the smallest credible cross-check using **Re-evaluate final candidates with higher-fidelity methods and explicitly test feasibility.**. Specify two competing hypotheses, an observable they predict differently, necessary independent specimens or structures and a falsification criterion. Explain which observation would force you to abandon the simpler model, and which uncertainty could remain even if the immediate test passed. **Solution strategy:** make the experiment capable of rejecting the preferred mechanism and protect the test from fitting-data leakage or unrecorded sample exclusions.

### Research memo and readiness check

Write an evidence table separating observations, simulations, calibration, independent tests and remaining risk. Propose a small reversible next experiment with a stop/go rule.

<!-- MODEL_12 -->

## Lesson 7.3 — Bayesian optimization and sample efficiency

### Concept, governing relationships and physical intuition

Bayesian optimization combines a predictive surrogate and an acquisition rule to seek costly experimental or computational optima. Expected improvement trades exploitation against exploration under its uncertainty model. No acquisition function saves a misspecified target or unrepresentative domain. Feasibility probabilities and practical testing costs should enter candidate selection.

**Modeling rule:** Acquisition values depend on predicted objective, uncertainty and incumbent best feasible result. Specify the reference state, physical units, validity domain and a verification test before translating this rule into a material decision.

### Competing explanations: what would actually falsify the model?

**Case:** A laboratory can afford only 12 high-fidelity calculations to find an alloy composition. Form two mechanisms that predict different observables, then select a discriminating calculation or experiment rather than arguing from graphical fit alone.

**Possible reversal:** Wrong surrogate variance may repeatedly prioritize poor regions. Test how changing temperature, composition, specimen condition or discretization could reverse the conclusion. Distinguish calibration agreement from independent verification.

### Synthetic quantitative notebook — inspect a dependency, not a material claim

The companion offline calculator is **Linear two-phase rule of mixtures** with mathematical expression `120*(x/100)+80*(1-x/100)`. Its adjustable input is **Volume fraction of stiff phase**, measured in %; output is reported in GPa. At an illustrative input of 26 %, the displayed result is **90.4 GPa**. A second invented input of 70 % gives **108 GPa**. The finite-difference response is 0.4 GPa per %. Independently check the result and units. Values are illustrative, not measured material properties or validated predictions.

**Fixed assumptions and failure tests:** Invented phase moduli 120 and 80 GPa with iso-strain upper-bound ideal mixture, perfect bonding and no porosity or geometry dependence. Change one declared hidden assumption, identify how the trend might fail, and specify an independent benchmark. The teaching card is not a materials simulation engine.

### Build an evidence and validation protocol

**Targeted measurement or audit:** Compare candidate choice to simple space-filling and random baselines at equal budgets. Define material state, specimen/structure provenance, independent replicates, measurement uncertainty and explicit conditions under which your preferred model would be falsified.

**Minimum reproducibility artifact:** supply an input file, exact method and version, a computational convergence check, independent test values, units and uncertainty. Write a diagnostic table contrasting what is computed, what is physically measured and what the hypothesis still assumes. Retain failed calculations instead of filtering them away, and document material identity and sample history at a level a different laboratory could understand. If the full measurement is unavailable, report a conditional prediction rather than describing the candidate as qualified.

### Design decision and economic consequences

**Competing objectives:** Sophisticated search may reduce expensive trials but add modeling overhead and selection bias. Rank alternatives only after hard safety, feasibility and manufacturing requirements are satisfied; record the cost of a false positive and a missed candidate.

### Three substantial practice exercises and solution strategies

**Exercise 1 — physical reconstruction.** Explain “Acquisition values depend on predicted objective, uncertainty and incumbent best feasible result.” in your own notation. Define the system, reference state, units, independent/dependent variables and at least two assumptions. Determine whether conservation, symmetry, force balance or statistical independence should be checked. Sketch one limiting case where the statement should simplify to a known result. **Solution strategy:** the derivation must use consistent dimensions and clearly say what the law does not predict; check an analytic, energy or mass-balance limit where available.

**Exercise 2 — calculation and uncertainty.** From `120*(x/100)+80*(1-x/100)`, independently derive 90.4 GPa for 26 % and compute one additional point halfway between the two example inputs. Estimate the sensitivity using a central perturbation, describe whether nonlinear dependence makes a one-number slope misleading, and add one plausible uncertainty in a fixed assumption. **Solution strategy:** perform an independent numerical calculation, propagate units before rounding, and report the interval conditional on the invented assumptions; do not use the resulting number as an empirical constant.

**Exercise 3 — independent comparison.** For “A laboratory can afford only 12 high-fidelity calculations to find an alloy composition.”, design the smallest credible cross-check using **Compare candidate choice to simple space-filling and random baselines at equal budgets.**. Specify two competing hypotheses, an observable they predict differently, necessary independent specimens or structures and a falsification criterion. Explain which observation would force you to abandon the simpler model, and which uncertainty could remain even if the immediate test passed. **Solution strategy:** make the experiment capable of rejecting the preferred mechanism and protect the test from fitting-data leakage or unrecorded sample exclusions.

### Research memo and readiness check

Write an evidence table separating observations, simulations, calibration, independent tests and remaining risk. Propose a small reversible next experiment with a stop/go rule.

<!-- MODEL_13 -->

## Lesson 7.5 — Research pipelines, provenance and go/no-go gates

### Concept, governing relationships and physical intuition

An automated research pipeline should pin versions, data schemas, units, model settings and random seeds. Immutable logs and checksums make results comparable. Gates reject invalid inputs, non-converged calculations and candidates lacking independent confirmation. Publication should keep failures and negative results, and should not imply that screening amounts to engineering qualification.

**Modeling rule:** A trustworthy result traces data and code through transformations to outputs, tests and limitations. Specify the reference state, physical units, validity domain and a verification test before translating this rule into a material decision.

### Competing explanations: what would actually falsify the model?

**Case:** A project cannot reproduce its strongest alloy candidate because the potential and training split have changed. Form two mechanisms that predict different observables, then select a discriminating calculation or experiment rather than arguing from graphical fit alone.

**Possible reversal:** Mutable remote databases and missing metadata can silently alter published results. Test how changing temperature, composition, specimen condition or discretization could reverse the conclusion. Distinguish calibration agreement from independent verification.

### Synthetic quantitative notebook — inspect a dependency, not a material claim

The companion offline calculator is **Linear two-phase rule of mixtures** with mathematical expression `120*(x/100)+80*(1-x/100)`. Its adjustable input is **Volume fraction of stiff phase**, measured in %; output is reported in GPa. At an illustrative input of 33 %, the displayed result is **93.2 GPa**. A second invented input of 75 % gives **110 GPa**. The finite-difference response is 0.4 GPa per %. Independently check the result and units. Values are illustrative, not measured material properties or validated predictions.

**Fixed assumptions and failure tests:** Invented phase moduli 120 and 80 GPa with iso-strain upper-bound ideal mixture, perfect bonding and no porosity or geometry dependence. Change one declared hidden assumption, identify how the trend might fail, and specify an independent benchmark. The teaching card is not a materials simulation engine.

### Build an evidence and validation protocol

**Targeted measurement or audit:** Rebuild from clean environment, inspect hashes, rerun key cases and conduct adversarial review. Define material state, specimen/structure provenance, independent replicates, measurement uncertainty and explicit conditions under which your preferred model would be falsified.

**Minimum reproducibility artifact:** supply an input file, exact method and version, a computational convergence check, independent test values, units and uncertainty. Write a diagnostic table contrasting what is computed, what is physically measured and what the hypothesis still assumes. Retain failed calculations instead of filtering them away, and document material identity and sample history at a level a different laboratory could understand. If the full measurement is unavailable, report a conditional prediction rather than describing the candidate as qualified.

### Design decision and economic consequences

**Competing objectives:** Reproducibility effort raises short-term workload but protects later translation and collaboration. Rank alternatives only after hard safety, feasibility and manufacturing requirements are satisfied; record the cost of a false positive and a missed candidate.

### Three substantial practice exercises and solution strategies

**Exercise 1 — physical reconstruction.** Explain “A trustworthy result traces data and code through transformations to outputs, tests and limitations.” in your own notation. Define the system, reference state, units, independent/dependent variables and at least two assumptions. Determine whether conservation, symmetry, force balance or statistical independence should be checked. Sketch one limiting case where the statement should simplify to a known result. **Solution strategy:** the derivation must use consistent dimensions and clearly say what the law does not predict; check an analytic, energy or mass-balance limit where available.

**Exercise 2 — calculation and uncertainty.** From `120*(x/100)+80*(1-x/100)`, independently derive 93.2 GPa for 33 % and compute one additional point halfway between the two example inputs. Estimate the sensitivity using a central perturbation, describe whether nonlinear dependence makes a one-number slope misleading, and add one plausible uncertainty in a fixed assumption. **Solution strategy:** perform an independent numerical calculation, propagate units before rounding, and report the interval conditional on the invented assumptions; do not use the resulting number as an empirical constant.

**Exercise 3 — independent comparison.** For “A project cannot reproduce its strongest alloy candidate because the potential and training split have changed.”, design the smallest credible cross-check using **Rebuild from clean environment, inspect hashes, rerun key cases and conduct adversarial review.**. Specify two competing hypotheses, an observable they predict differently, necessary independent specimens or structures and a falsification criterion. Explain which observation would force you to abandon the simpler model, and which uncertainty could remain even if the immediate test passed. **Solution strategy:** make the experiment capable of rejecting the preferred mechanism and protect the test from fitting-data leakage or unrecorded sample exclusions.

### Research memo and readiness check

Write an evidence table separating observations, simulations, calibration, independent tests and remaining risk. Propose a small reversible next experiment with a stop/go rule.

## Unit 7 capstone: integrate calculations with evidence

**Practical challenge:** An optimizer identifies an apparently ideal composition at the edge of a design domain. Check validity regions, manufacturing constraints, competing objectives, robust margins and cost of physical confirmation.

1. **Define material state and performance.** State composition, phase/microstructure, processing history, external constraints, independent material specimens and the exact observable to be predicted. State the intended decision and penalty of a wrong choice.
2. **Reproduce quantitative work.** Run both synthetic interactive formulas at three inputs, independently recompute the results, and identify the nonphysical or unmeasured assumptions. Develop one additional first-principles or measured-model benchmark that would test the physics rather than just the code.
3. **Test alternative explanations.** Use **objective, feasible domain and optimization audit**, explicitly log **parameter bounds, physical constraints, optimizer starts, surrogate applicability and uncertainty**, and challenge the model with **higher-fidelity rechecks and independent experimental confirmations**. Describe an observation that would falsify the preferred hypothesis. Separate calibration, validation and engineering qualification evidence.
4. **Quantify uncertainty and feasibility.** Include one numerical convergence test, one physical or statistical uncertainty propagation, one out-of-domain stress test, one materials supply or production constraint and a feasible low-cost validation plan.
5. **Deliver an auditable recommendation.** Produce a two-page technical decision, reproducibility checklist, complete candidate table and stop/go rule. Explicitly revisit **whether model exploitation at an extrapolation boundary manufactures a spurious optimum**. No synthetic formula output authorizes use of a safety-critical material or device.

### Concluding reflection

A physical model earns trust by surviving attempts to falsify its assumptions within a defined application, not by producing a large dataset or intricate graphics. Distinguish numerical convergence, agreement on fitted points, generalization to new material states and functional qualification of real parts. If any step remains missing, state which research question is answerable and which engineering recommendation must be deferred.

