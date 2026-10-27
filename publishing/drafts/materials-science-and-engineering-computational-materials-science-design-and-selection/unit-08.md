# Unit 8: Application Case Studies and Research Reproducibility

**Guiding question:** How do model results translate into defensible science and engineering decisions?

## Problem framing and scale selection

An interdisciplinary group must recommend materials for a cell, device or structure and make the decision auditable. Define the complete chain of data, assumptions, physics, numerical convergence, experimental validation, economics and future monitoring. No materials simulation is interpretable until its target observable, reference material state, environmental range and intended downstream decision are fixed. Distinguish a calculated ideal crystal from an actual manufactured material, a numerical fit from independent validation, and a candidate ranking from an authorized design decision. A model should be evaluated by whether it rules out alternatives or informs an observable experiment, not by the complexity of its software or resolution of its graphics.

The unit's evidence record starts with **integrated multidisciplinary reproducibility review**. Collect **electronic/atomistic inputs, property handoffs, device model, experimental data, cost and carbon records** and prioritize tests such as **blinded replication, cross-scale consistency, prospective tests and document checksums**. The most dangerous untested assumption is **whether the recommended material passes all hard constraints under realistic variability**. Work backward from that possible failure: identify at least two competing explanations, a calculation that could distinguish them, an independently measurable outcome and a decision threshold. Be explicit if available observations cannot constrain the model. The five lessons progressively build a defensible case record.

## Unit field notebook — initial protocol

State a material formulation, one measurable target property, units, intended temperature/time/composition limits, specimen or simulated domain, governing hypotheses and error tolerance. Record a reference model with minimal complexity; describe where added atomistic, mesoscale, continuum or statistical detail would be necessary. List input uncertainty sources, computational convergence tests, independent measurement plans, future update conditions and rejection criteria. At the end of the unit, turn the notebook into a one-page auditable model-use statement.

## Lesson 8.1 — Battery materials and coupled degradation

### Concept, governing relationships and physical intuition

Electrochemical cells link diffusion, interfacial reaction kinetics, mechanical stress and thermal transport. A high theoretical capacity is not equal to practical cycle-life performance. Voltage windows, phase transformations, electrolyte stability and current density modify lifetime; coupled models need comparable electrochemical and thermal boundary data.

**Modeling rule:** Characteristic concentration equilibration time grows with the square of transport length. Specify the reference state, physical units, validity domain and a verification test before translating this rule into a material decision.

### Competing explanations: what would actually falsify the model?

**Case:** A high-capacity electrode looks superior in an ideal crystal calculation but rapidly loses measured capacity during cycling. Form two mechanisms that predict different observables, then select a discriminating calculation or experiment rather than arguing from graphical fit alone.

**Possible reversal:** An ideal diffusion coefficient cannot predict dendrites, electrolyte reactions or mechanical cracking. Test how changing temperature, composition, specimen condition or discretization could reverse the conclusion. Distinguish calibration agreement from independent verification.

### Synthetic quantitative notebook — inspect a dependency, not a material claim

The companion offline calculator is **Toy thermal activation transport** with mathematical expression `1e-7*Math.exp(-0.40/(8.617333262e-5*T))`. Its adjustable input is **Operating temperature**, measured in K; output is reported in m²/s. At an illustrative input of 390 K, the displayed result is **6.7763641e-13 m²/s**. A second invented input of 620 K gives **5.60441392e-11 m²/s**. The finite-difference response is 2.40723925e-13 m²/s per K. Independently check the result and units. Values are illustrative, not measured material properties or validated predictions.

**Fixed assumptions and failure tests:** Fixed hypothetical prefactor 1e−7 m²/s and activation energy 0.40 eV; no changes in phase, chemistry, mechanism or temperature-dependent prefactor. Change one declared hidden assumption, identify how the trend might fail, and specify an independent benchmark. The teaching card is not a materials simulation engine.

### Build an evidence and validation protocol

**Targeted measurement or audit:** Compare half-cell, full-cell and realistic rate/temperature cycling with degradation measurements. Define material state, specimen/structure provenance, independent replicates, measurement uncertainty and explicit conditions under which your preferred model would be falsified.

**Minimum reproducibility artifact:** supply an input file, exact method and version, a computational convergence check, independent test values, units and uncertainty. Write a diagnostic table contrasting what is computed, what is physically measured and what the hypothesis still assumes. Retain failed calculations instead of filtering them away, and document material identity and sample history at a level a different laboratory could understand. If the full measurement is unavailable, report a conditional prediction rather than describing the candidate as qualified.

### Design decision and economic consequences

**Competing objectives:** Energy density, safety, lifetime, cost and mineral supply must be screened together. Rank alternatives only after hard safety, feasibility and manufacturing requirements are satisfied; record the cost of a false positive and a missed candidate.

### Three substantial practice exercises and solution strategies

**Exercise 1 — physical reconstruction.** Explain “Characteristic concentration equilibration time grows with the square of transport length.” in your own notation. Define the system, reference state, units, independent/dependent variables and at least two assumptions. Determine whether conservation, symmetry, force balance or statistical independence should be checked. Sketch one limiting case where the statement should simplify to a known result. **Solution strategy:** the derivation must use consistent dimensions and clearly say what the law does not predict; check an analytic, energy or mass-balance limit where available.

**Exercise 2 — calculation and uncertainty.** From `1e-7*Math.exp(-0.40/(8.617333262e-5*T))`, independently derive 6.7763641e-13 m²/s for 390 K and compute one additional point halfway between the two example inputs. Estimate the sensitivity using a central perturbation, describe whether nonlinear dependence makes a one-number slope misleading, and add one plausible uncertainty in a fixed assumption. **Solution strategy:** perform an independent numerical calculation, propagate units before rounding, and report the interval conditional on the invented assumptions; do not use the resulting number as an empirical constant.

**Exercise 3 — independent comparison.** For “A high-capacity electrode looks superior in an ideal crystal calculation but rapidly loses measured capacity during cycling.”, design the smallest credible cross-check using **Compare half-cell, full-cell and realistic rate/temperature cycling with degradation measurements.**. Specify two competing hypotheses, an observable they predict differently, necessary independent specimens or structures and a falsification criterion. Explain which observation would force you to abandon the simpler model, and which uncertainty could remain even if the immediate test passed. **Solution strategy:** make the experiment capable of rejecting the preferred mechanism and protect the test from fitting-data leakage or unrecorded sample exclusions.

### Research memo and readiness check

Write an evidence table separating observations, simulations, calibration, independent tests and remaining risk. Propose a small reversible next experiment with a stop/go rule.

<!-- MODEL_14 -->

## Lesson 8.3 — Structural alloys, fatigue and damage tolerance

### Concept, governing relationships and physical intuition

Structural choice combines phase stability, manufacturing texture, inclusions, environment, load spectra and inspectability. Fatigue initiation can be controlled by rare defects that are invisible in small ideal-cell simulations. Cumulative damage approximations require careful limits and generally do not replace specimen-level life testing. Computational screening is best used to narrow hypotheses and design informative trials.

**Modeling rule:** In simplified fracture mechanics, crack-driving intensity increases with load and sqrt(crack size). Specify the reference state, physical units, validity domain and a verification test before translating this rule into a material decision.

### Competing explanations: what would actually falsify the model?

**Case:** A lightweight aerospace bracket is qualified by static FEA but its real failure originates at a surface pore. Form two mechanisms that predict different observables, then select a discriminating calculation or experiment rather than arguing from graphical fit alone.

**Possible reversal:** Real short cracks, residual stress and random spectra can invalidate ideal long-crack assumptions. Test how changing temperature, composition, specimen condition or discretization could reverse the conclusion. Distinguish calibration agreement from independent verification.

### Synthetic quantitative notebook — inspect a dependency, not a material claim

The companion offline calculator is **Toy thermal activation transport** with mathematical expression `1e-7*Math.exp(-0.40/(8.617333262e-5*T))`. Its adjustable input is **Operating temperature**, measured in K; output is reported in m²/s. At an illustrative input of 430 K, the displayed result is **2.05037948e-12 m²/s**. A second invented input of 650 K gives **7.91768172e-11 m²/s**. The finite-difference response is 3.50574717e-13 m²/s per K. Independently check the result and units. Values are illustrative, not measured material properties or validated predictions.

**Fixed assumptions and failure tests:** Fixed hypothetical prefactor 1e−7 m²/s and activation energy 0.40 eV; no changes in phase, chemistry, mechanism or temperature-dependent prefactor. Change one declared hidden assumption, identify how the trend might fail, and specify an independent benchmark. The teaching card is not a materials simulation engine.

### Build an evidence and validation protocol

**Targeted measurement or audit:** Use orientation-aware fatigue tests, NDT defect mapping and representative process lots. Define material state, specimen/structure provenance, independent replicates, measurement uncertainty and explicit conditions under which your preferred model would be falsified.

**Minimum reproducibility artifact:** supply an input file, exact method and version, a computational convergence check, independent test values, units and uncertainty. Write a diagnostic table contrasting what is computed, what is physically measured and what the hypothesis still assumes. Retain failed calculations instead of filtering them away, and document material identity and sample history at a level a different laboratory could understand. If the full measurement is unavailable, report a conditional prediction rather than describing the candidate as qualified.

### Design decision and economic consequences

**Competing objectives:** Conservative damage tolerance may cost mass but prevents false confidence from nominal FEA. Rank alternatives only after hard safety, feasibility and manufacturing requirements are satisfied; record the cost of a false positive and a missed candidate.

### Three substantial practice exercises and solution strategies

**Exercise 1 — physical reconstruction.** Explain “In simplified fracture mechanics, crack-driving intensity increases with load and sqrt(crack size).” in your own notation. Define the system, reference state, units, independent/dependent variables and at least two assumptions. Determine whether conservation, symmetry, force balance or statistical independence should be checked. Sketch one limiting case where the statement should simplify to a known result. **Solution strategy:** the derivation must use consistent dimensions and clearly say what the law does not predict; check an analytic, energy or mass-balance limit where available.

**Exercise 2 — calculation and uncertainty.** From `1e-7*Math.exp(-0.40/(8.617333262e-5*T))`, independently derive 2.05037948e-12 m²/s for 430 K and compute one additional point halfway between the two example inputs. Estimate the sensitivity using a central perturbation, describe whether nonlinear dependence makes a one-number slope misleading, and add one plausible uncertainty in a fixed assumption. **Solution strategy:** perform an independent numerical calculation, propagate units before rounding, and report the interval conditional on the invented assumptions; do not use the resulting number as an empirical constant.

**Exercise 3 — independent comparison.** For “A lightweight aerospace bracket is qualified by static FEA but its real failure originates at a surface pore.”, design the smallest credible cross-check using **Use orientation-aware fatigue tests, NDT defect mapping and representative process lots.**. Specify two competing hypotheses, an observable they predict differently, necessary independent specimens or structures and a falsification criterion. Explain which observation would force you to abandon the simpler model, and which uncertainty could remain even if the immediate test passed. **Solution strategy:** make the experiment capable of rejecting the preferred mechanism and protect the test from fitting-data leakage or unrecorded sample exclusions.

### Research memo and readiness check

Write an evidence table separating observations, simulations, calibration, independent tests and remaining risk. Propose a small reversible next experiment with a stop/go rule.

<!-- MODEL_15 -->

## Lesson 8.5 — Integrated design review and open-science capstone

### Concept, governing relationships and physical intuition

A complete materials decision begins with measurable functional requirements and ends with evidence-backed validation, documented gaps and a stop/go gate. Each team member must distinguish modeled observables, measured behavior, calibration data, independent test data and assumptions. Reproducible notebooks and data lineage are necessary but not sufficient for safety or commercial qualification.

**Modeling rule:** Acceptance requires every declared hard constraint and relevant independent validation check to pass. Specify the reference state, physical units, validity domain and a verification test before translating this rule into a material decision.

### Competing explanations: what would actually falsify the model?

**Case:** A multidisciplinary team must select a material and process for a reusable sensor enclosure under cost, durability and carbon constraints. Form two mechanisms that predict different observables, then select a discriminating calculation or experiment rather than arguing from graphical fit alone.

**Possible reversal:** Summing multiple scores can conceal a single disqualifying failure mode. Test how changing temperature, composition, specimen condition or discretization could reverse the conclusion. Distinguish calibration agreement from independent verification.

### Synthetic quantitative notebook — inspect a dependency, not a material claim

The companion offline calculator is **Toy thermal activation transport** with mathematical expression `1e-7*Math.exp(-0.40/(8.617333262e-5*T))`. Its adjustable input is **Operating temperature**, measured in K; output is reported in m²/s. At an illustrative input of 470 K, the displayed result is **5.13839015e-12 m²/s**. A second invented input of 680 K gives **1.08498716e-10 m²/s**. The finite-difference response is 4.92192026e-13 m²/s per K. Independently check the result and units. Values are illustrative, not measured material properties or validated predictions.

**Fixed assumptions and failure tests:** Fixed hypothetical prefactor 1e−7 m²/s and activation energy 0.40 eV; no changes in phase, chemistry, mechanism or temperature-dependent prefactor. Change one declared hidden assumption, identify how the trend might fail, and specify an independent benchmark. The teaching card is not a materials simulation engine.

### Build an evidence and validation protocol

**Targeted measurement or audit:** Produce a versioned decision dossier with blinded confirmation trials and stakeholder review. Define material state, specimen/structure provenance, independent replicates, measurement uncertainty and explicit conditions under which your preferred model would be falsified.

**Minimum reproducibility artifact:** supply an input file, exact method and version, a computational convergence check, independent test values, units and uncertainty. Write a diagnostic table contrasting what is computed, what is physically measured and what the hypothesis still assumes. Retain failed calculations instead of filtering them away, and document material identity and sample history at a level a different laboratory could understand. If the full measurement is unavailable, report a conditional prediction rather than describing the candidate as qualified.

### Design decision and economic consequences

**Competing objectives:** The strongest recommendation may be to defer procurement until one decisive uncertainty is measured. Rank alternatives only after hard safety, feasibility and manufacturing requirements are satisfied; record the cost of a false positive and a missed candidate.

### Three substantial practice exercises and solution strategies

**Exercise 1 — physical reconstruction.** Explain “Acceptance requires every declared hard constraint and relevant independent validation check to pass.” in your own notation. Define the system, reference state, units, independent/dependent variables and at least two assumptions. Determine whether conservation, symmetry, force balance or statistical independence should be checked. Sketch one limiting case where the statement should simplify to a known result. **Solution strategy:** the derivation must use consistent dimensions and clearly say what the law does not predict; check an analytic, energy or mass-balance limit where available.

**Exercise 2 — calculation and uncertainty.** From `1e-7*Math.exp(-0.40/(8.617333262e-5*T))`, independently derive 5.13839015e-12 m²/s for 470 K and compute one additional point halfway between the two example inputs. Estimate the sensitivity using a central perturbation, describe whether nonlinear dependence makes a one-number slope misleading, and add one plausible uncertainty in a fixed assumption. **Solution strategy:** perform an independent numerical calculation, propagate units before rounding, and report the interval conditional on the invented assumptions; do not use the resulting number as an empirical constant.

**Exercise 3 — independent comparison.** For “A multidisciplinary team must select a material and process for a reusable sensor enclosure under cost, durability and carbon constraints.”, design the smallest credible cross-check using **Produce a versioned decision dossier with blinded confirmation trials and stakeholder review.**. Specify two competing hypotheses, an observable they predict differently, necessary independent specimens or structures and a falsification criterion. Explain which observation would force you to abandon the simpler model, and which uncertainty could remain even if the immediate test passed. **Solution strategy:** make the experiment capable of rejecting the preferred mechanism and protect the test from fitting-data leakage or unrecorded sample exclusions.

### Research memo and readiness check

Write an evidence table separating observations, simulations, calibration, independent tests and remaining risk. Propose a small reversible next experiment with a stop/go rule.

## Unit 8 capstone: integrate calculations with evidence

**Practical challenge:** An interdisciplinary group must recommend materials for a cell, device or structure and make the decision auditable. Define the complete chain of data, assumptions, physics, numerical convergence, experimental validation, economics and future monitoring.

1. **Define material state and performance.** State composition, phase/microstructure, processing history, external constraints, independent material specimens and the exact observable to be predicted. State the intended decision and penalty of a wrong choice.
2. **Reproduce quantitative work.** Run both synthetic interactive formulas at three inputs, independently recompute the results, and identify the nonphysical or unmeasured assumptions. Develop one additional first-principles or measured-model benchmark that would test the physics rather than just the code.
3. **Test alternative explanations.** Use **integrated multidisciplinary reproducibility review**, explicitly log **electronic/atomistic inputs, property handoffs, device model, experimental data, cost and carbon records**, and challenge the model with **blinded replication, cross-scale consistency, prospective tests and document checksums**. Describe an observation that would falsify the preferred hypothesis. Separate calibration, validation and engineering qualification evidence.
4. **Quantify uncertainty and feasibility.** Include one numerical convergence test, one physical or statistical uncertainty propagation, one out-of-domain stress test, one materials supply or production constraint and a feasible low-cost validation plan.
5. **Deliver an auditable recommendation.** Produce a two-page technical decision, reproducibility checklist, complete candidate table and stop/go rule. Explicitly revisit **whether the recommended material passes all hard constraints under realistic variability**. No synthetic formula output authorizes use of a safety-critical material or device.

### Concluding reflection

A physical model earns trust by surviving attempts to falsify its assumptions within a defined application, not by producing a large dataset or intricate graphics. Distinguish numerical convergence, agreement on fitted points, generalization to new material states and functional qualification of real parts. If any step remains missing, state which research question is answerable and which engineering recommendation must be deferred.

