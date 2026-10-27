# Unit 6: Engineering Materials Selection and Trade-offs

**Guiding question:** How should materials be compared when properties, cost and impacts conflict?

## Problem framing and scale selection

A supplier offers three candidate materials for a long-life lightweight beam. Compare stiffness, density, fatigue, corrosion, manufacturing loss, life-cycle burdens and costs against a precisely stated service requirement. No materials simulation is interpretable until its target observable, reference material state, environmental range and intended downstream decision are fixed. Distinguish a calculated ideal crystal from an actual manufactured material, a numerical fit from independent validation, and a candidate ranking from an authorized design decision. A model should be evaluated by whether it rules out alternatives or informs an observable experiment, not by the complexity of its software or resolution of its graphics.

The unit's evidence record starts with **functional specification and material state evidence**. Collect **property distributions, geometry, acceptance limits, costs, lifecycle and supply constraints** and prioritize tests such as **physical prototypes, supplier records, bounded cost/LCA scenarios and safety review**. The most dangerous untested assumption is **whether a single property index conceals critical failure, cost or environmental burden**. Work backward from that possible failure: identify at least two competing explanations, a calculation that could distinguish them, an independently measurable outcome and a decision threshold. Be explicit if available observations cannot constrain the model. The five lessons progressively build a defensible case record.

## Unit field notebook — initial protocol

State a material formulation, one measurable target property, units, intended temperature/time/composition limits, specimen or simulated domain, governing hypotheses and error tolerance. Record a reference model with minimal complexity; describe where added atomistic, mesoscale, continuum or statistical detail would be necessary. List input uncertainty sources, computational convergence tests, independent measurement plans, future update conditions and rejection criteria. At the end of the unit, turn the notebook into a one-page auditable model-use statement.

## Lesson 6.1 — Functional specification and screening bounds

### Concept, governing relationships and physical intuition

Material selection starts with the actual component function, load environment, lifetime, safety, manufacturing route and hard constraints. A published strength number is meaningful only for a defined processing state, temperature and test direction. Early screening should exclude candidates violating non-negotiable constraints before weighting price or sustainability.

**Modeling rule:** A candidate is feasible only if all hard service, safety, geometric and supply constraints are met. Specify the reference state, physical units, validity domain and a verification test before translating this rule into a material decision.

### Competing explanations: what would actually falsify the model?

**Case:** A high-strength alloy is selected for an outdoor beam without accounting for corrosion allowance and joining. Form two mechanisms that predict different observables, then select a discriminating calculation or experiment rather than arguing from graphical fit alone.

**Possible reversal:** Property averages from different product forms may not represent the supplied stock. Test how changing temperature, composition, specimen condition or discretization could reverse the conclusion. Distinguish calibration agreement from independent verification.

### Synthetic quantitative notebook — inspect a dependency, not a material claim

The companion offline calculator is **Toy stiffness-limited material index** with mathematical expression `Math.sqrt(E)/2.7`. Its adjustable input is **Young modulus**, measured in GPa; output is reported in √GPa/(g/cm³). At an illustrative input of 70 GPa, the displayed result is **3.09874084 √GPa/(g/cm³)**. A second invented input of 200 GPa gives **5.23782801 √GPa/(g/cm³)**. The finite-difference response is 0.0164545167 √GPa/(g/cm³) per GPa. Independently check the result and units. Values are illustrative, not measured material properties or validated predictions.

**Fixed assumptions and failure tests:** Fixed density 2.7 g/cm³ and square-root modulus over density scaling for selected similarly scaled beam designs; does not rank real parts under all constraints. Change one declared hidden assumption, identify how the trend might fail, and specify an independent benchmark. The teaching card is not a materials simulation engine.

### Build an evidence and validation protocol

**Targeted measurement or audit:** Collect certificates and application-specific tests for each candidate and service condition. Define material state, specimen/structure provenance, independent replicates, measurement uncertainty and explicit conditions under which your preferred model would be falsified.

**Minimum reproducibility artifact:** supply an input file, exact method and version, a computational convergence check, independent test values, units and uncertainty. Write a diagnostic table contrasting what is computed, what is physically measured and what the hypothesis still assumes. Retain failed calculations instead of filtering them away, and document material identity and sample history at a level a different laboratory could understand. If the full measurement is unavailable, report a conditional prediction rather than describing the candidate as qualified.

### Design decision and economic consequences

**Competing objectives:** Aggressive screening saves effort but wrongly narrow thresholds can discard robust alternatives. Rank alternatives only after hard safety, feasibility and manufacturing requirements are satisfied; record the cost of a false positive and a missed candidate.

### Three substantial practice exercises and solution strategies

**Exercise 1 — physical reconstruction.** Explain “A candidate is feasible only if all hard service, safety, geometric and supply constraints are met.” in your own notation. Define the system, reference state, units, independent/dependent variables and at least two assumptions. Determine whether conservation, symmetry, force balance or statistical independence should be checked. Sketch one limiting case where the statement should simplify to a known result. **Solution strategy:** the derivation must use consistent dimensions and clearly say what the law does not predict; check an analytic, energy or mass-balance limit where available.

**Exercise 2 — calculation and uncertainty.** From `Math.sqrt(E)/2.7`, independently derive 3.09874084 √GPa/(g/cm³) for 70 GPa and compute one additional point halfway between the two example inputs. Estimate the sensitivity using a central perturbation, describe whether nonlinear dependence makes a one-number slope misleading, and add one plausible uncertainty in a fixed assumption. **Solution strategy:** perform an independent numerical calculation, propagate units before rounding, and report the interval conditional on the invented assumptions; do not use the resulting number as an empirical constant.

**Exercise 3 — independent comparison.** For “A high-strength alloy is selected for an outdoor beam without accounting for corrosion allowance and joining.”, design the smallest credible cross-check using **Collect certificates and application-specific tests for each candidate and service condition.**. Specify two competing hypotheses, an observable they predict differently, necessary independent specimens or structures and a falsification criterion. Explain which observation would force you to abandon the simpler model, and which uncertainty could remain even if the immediate test passed. **Solution strategy:** make the experiment capable of rejecting the preferred mechanism and protect the test from fitting-data leakage or unrecorded sample exclusions.

### Research memo and readiness check

Write an evidence table separating observations, simulations, calibration, independent tests and remaining risk. Propose a small reversible next experiment with a stop/go rule.

<!-- MODEL_10 -->

## Lesson 6.3 — Cost models, manufacturing yields and lifecycle economics

### Concept, governing relationships and physical intuition

Procurement price per kilogram is not a delivered qualified-part price. Include processing yield, tooling, labor, energy, inspection, replacement, repair and discount rate as needed. Compare on identical functional lifetimes; a cheaper material with more frequent replacement may cost more. All currency and assumptions should be dated and geographically scoped.

**Modeling rule:** Lifecycle cost equals discounted acquisition, operation, inspection, replacement and end-of-life cash flows. Specify the reference state, physical units, validity domain and a verification test before translating this rule into a material decision.

### Competing explanations: what would actually falsify the model?

**Case:** A composite panel seems cheaper by nominal material price but requires expensive inspection and scrap disposal. Form two mechanisms that predict different observables, then select a discriminating calculation or experiment rather than arguing from graphical fit alone.

**Possible reversal:** A deterministic cost model misleads when scrap rate and lifetime are poorly estimated. Test how changing temperature, composition, specimen condition or discretization could reverse the conclusion. Distinguish calibration agreement from independent verification.

### Synthetic quantitative notebook — inspect a dependency, not a material claim

The companion offline calculator is **Toy stiffness-limited material index** with mathematical expression `Math.sqrt(E)/2.7`. Its adjustable input is **Young modulus**, measured in GPa; output is reported in √GPa/(g/cm³). At an illustrative input of 90 GPa, the displayed result is **3.51364184 √GPa/(g/cm³)**. A second invented input of 215 GPa gives **5.43069567 √GPa/(g/cm³)**. The finite-difference response is 0.0153364306 √GPa/(g/cm³) per GPa. Independently check the result and units. Values are illustrative, not measured material properties or validated predictions.

**Fixed assumptions and failure tests:** Fixed density 2.7 g/cm³ and square-root modulus over density scaling for selected similarly scaled beam designs; does not rank real parts under all constraints. Change one declared hidden assumption, identify how the trend might fail, and specify an independent benchmark. The teaching card is not a materials simulation engine.

### Build an evidence and validation protocol

**Targeted measurement or audit:** Run sensitivity cases, solicit credible supplier process quotations, and test actual yield before procurement. Define material state, specimen/structure provenance, independent replicates, measurement uncertainty and explicit conditions under which your preferred model would be falsified.

**Minimum reproducibility artifact:** supply an input file, exact method and version, a computational convergence check, independent test values, units and uncertainty. Write a diagnostic table contrasting what is computed, what is physically measured and what the hypothesis still assumes. Retain failed calculations instead of filtering them away, and document material identity and sample history at a level a different laboratory could understand. If the full measurement is unavailable, report a conditional prediction rather than describing the candidate as qualified.

### Design decision and economic consequences

**Competing objectives:** Low initial cost may conflict with long life, repairability or supply reliability. Rank alternatives only after hard safety, feasibility and manufacturing requirements are satisfied; record the cost of a false positive and a missed candidate.

### Three substantial practice exercises and solution strategies

**Exercise 1 — physical reconstruction.** Explain “Lifecycle cost equals discounted acquisition, operation, inspection, replacement and end-of-life cash flows.” in your own notation. Define the system, reference state, units, independent/dependent variables and at least two assumptions. Determine whether conservation, symmetry, force balance or statistical independence should be checked. Sketch one limiting case where the statement should simplify to a known result. **Solution strategy:** the derivation must use consistent dimensions and clearly say what the law does not predict; check an analytic, energy or mass-balance limit where available.

**Exercise 2 — calculation and uncertainty.** From `Math.sqrt(E)/2.7`, independently derive 3.51364184 √GPa/(g/cm³) for 90 GPa and compute one additional point halfway between the two example inputs. Estimate the sensitivity using a central perturbation, describe whether nonlinear dependence makes a one-number slope misleading, and add one plausible uncertainty in a fixed assumption. **Solution strategy:** perform an independent numerical calculation, propagate units before rounding, and report the interval conditional on the invented assumptions; do not use the resulting number as an empirical constant.

**Exercise 3 — independent comparison.** For “A composite panel seems cheaper by nominal material price but requires expensive inspection and scrap disposal.”, design the smallest credible cross-check using **Run sensitivity cases, solicit credible supplier process quotations, and test actual yield before procurement.**. Specify two competing hypotheses, an observable they predict differently, necessary independent specimens or structures and a falsification criterion. Explain which observation would force you to abandon the simpler model, and which uncertainty could remain even if the immediate test passed. **Solution strategy:** make the experiment capable of rejecting the preferred mechanism and protect the test from fitting-data leakage or unrecorded sample exclusions.

### Research memo and readiness check

Write an evidence table separating observations, simulations, calibration, independent tests and remaining risk. Propose a small reversible next experiment with a stop/go rule.

<!-- MODEL_11 -->

## Lesson 6.5 — Pareto fronts, safety constraints and decision transparency

### Concept, governing relationships and physical intuition

Multiobjective selection often has no single option best on cost, stiffness, mass, environmental impact and repairability. A candidate is Pareto dominated if another is no worse in every objective and better in at least one. Hard safety constraints must not be traded for weighted scores. Rankings depend on normalization, missing data and stakeholders.

**Modeling rule:** A Pareto frontier contains nondominated feasible options under declared objectives. Specify the reference state, physical units, validity domain and a verification test before translating this rule into a material decision.

### Competing explanations: what would actually falsify the model?

**Case:** Two materials have similar strength, but one is easier to recycle and the other has lower mass. Form two mechanisms that predict different observables, then select a discriminating calculation or experiment rather than arguing from graphical fit alone.

**Possible reversal:** Weight tuning can mask explicit safety failures or unacknowledged priorities. Test how changing temperature, composition, specimen condition or discretization could reverse the conclusion. Distinguish calibration agreement from independent verification.

### Synthetic quantitative notebook — inspect a dependency, not a material claim

The companion offline calculator is **Toy stiffness-limited material index** with mathematical expression `Math.sqrt(E)/2.7`. Its adjustable input is **Young modulus**, measured in GPa; output is reported in √GPa/(g/cm³). At an illustrative input of 115 GPa, the displayed result is **3.97177974 √GPa/(g/cm³)**. A second invented input of 230 GPa gives **5.61694477 √GPa/(g/cm³)**. The finite-difference response is 0.0143057829 √GPa/(g/cm³) per GPa. Independently check the result and units. Values are illustrative, not measured material properties or validated predictions.

**Fixed assumptions and failure tests:** Fixed density 2.7 g/cm³ and square-root modulus over density scaling for selected similarly scaled beam designs; does not rank real parts under all constraints. Change one declared hidden assumption, identify how the trend might fail, and specify an independent benchmark. The teaching card is not a materials simulation engine.

### Build an evidence and validation protocol

**Targeted measurement or audit:** Show decision tables under several weights, excluded options and threshold sensitivity. Define material state, specimen/structure provenance, independent replicates, measurement uncertainty and explicit conditions under which your preferred model would be falsified.

**Minimum reproducibility artifact:** supply an input file, exact method and version, a computational convergence check, independent test values, units and uncertainty. Write a diagnostic table contrasting what is computed, what is physically measured and what the hypothesis still assumes. Retain failed calculations instead of filtering them away, and document material identity and sample history at a level a different laboratory could understand. If the full measurement is unavailable, report a conditional prediction rather than describing the candidate as qualified.

### Design decision and economic consequences

**Competing objectives:** Transparent trade-offs preserve legitimate disagreements while avoiding false mathematical certainty. Rank alternatives only after hard safety, feasibility and manufacturing requirements are satisfied; record the cost of a false positive and a missed candidate.

### Three substantial practice exercises and solution strategies

**Exercise 1 — physical reconstruction.** Explain “A Pareto frontier contains nondominated feasible options under declared objectives.” in your own notation. Define the system, reference state, units, independent/dependent variables and at least two assumptions. Determine whether conservation, symmetry, force balance or statistical independence should be checked. Sketch one limiting case where the statement should simplify to a known result. **Solution strategy:** the derivation must use consistent dimensions and clearly say what the law does not predict; check an analytic, energy or mass-balance limit where available.

**Exercise 2 — calculation and uncertainty.** From `Math.sqrt(E)/2.7`, independently derive 3.97177974 √GPa/(g/cm³) for 115 GPa and compute one additional point halfway between the two example inputs. Estimate the sensitivity using a central perturbation, describe whether nonlinear dependence makes a one-number slope misleading, and add one plausible uncertainty in a fixed assumption. **Solution strategy:** perform an independent numerical calculation, propagate units before rounding, and report the interval conditional on the invented assumptions; do not use the resulting number as an empirical constant.

**Exercise 3 — independent comparison.** For “Two materials have similar strength, but one is easier to recycle and the other has lower mass.”, design the smallest credible cross-check using **Show decision tables under several weights, excluded options and threshold sensitivity.**. Specify two competing hypotheses, an observable they predict differently, necessary independent specimens or structures and a falsification criterion. Explain which observation would force you to abandon the simpler model, and which uncertainty could remain even if the immediate test passed. **Solution strategy:** make the experiment capable of rejecting the preferred mechanism and protect the test from fitting-data leakage or unrecorded sample exclusions.

### Research memo and readiness check

Write an evidence table separating observations, simulations, calibration, independent tests and remaining risk. Propose a small reversible next experiment with a stop/go rule.

## Unit 6 capstone: integrate calculations with evidence

**Practical challenge:** A supplier offers three candidate materials for a long-life lightweight beam. Compare stiffness, density, fatigue, corrosion, manufacturing loss, life-cycle burdens and costs against a precisely stated service requirement.

1. **Define material state and performance.** State composition, phase/microstructure, processing history, external constraints, independent material specimens and the exact observable to be predicted. State the intended decision and penalty of a wrong choice.
2. **Reproduce quantitative work.** Run both synthetic interactive formulas at three inputs, independently recompute the results, and identify the nonphysical or unmeasured assumptions. Develop one additional first-principles or measured-model benchmark that would test the physics rather than just the code.
3. **Test alternative explanations.** Use **functional specification and material state evidence**, explicitly log **property distributions, geometry, acceptance limits, costs, lifecycle and supply constraints**, and challenge the model with **physical prototypes, supplier records, bounded cost/LCA scenarios and safety review**. Describe an observation that would falsify the preferred hypothesis. Separate calibration, validation and engineering qualification evidence.
4. **Quantify uncertainty and feasibility.** Include one numerical convergence test, one physical or statistical uncertainty propagation, one out-of-domain stress test, one materials supply or production constraint and a feasible low-cost validation plan.
5. **Deliver an auditable recommendation.** Produce a two-page technical decision, reproducibility checklist, complete candidate table and stop/go rule. Explicitly revisit **whether a single property index conceals critical failure, cost or environmental burden**. No synthetic formula output authorizes use of a safety-critical material or device.

### Concluding reflection

A physical model earns trust by surviving attempts to falsify its assumptions within a defined application, not by producing a large dataset or intricate graphics. Distinguish numerical convergence, agreement on fitted points, generalization to new material states and functional qualification of real parts. If any step remains missing, state which research question is answerable and which engineering recommendation must be deferred.

