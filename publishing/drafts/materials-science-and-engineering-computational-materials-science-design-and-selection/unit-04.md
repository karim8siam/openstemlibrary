# Unit 4: Continuum and Multiscale Modeling

**Guiding question:** When are fields, meshes and constitutive equations trustworthy?

## Problem framing and scale selection

A finite-element model predicts low stress in a welded component that fails near a notch. Diagnose the mesh, residual stress, damage law, fatigue load spectrum, contact, manufacturing history and physical tests. No materials simulation is interpretable until its target observable, reference material state, environmental range and intended downstream decision are fixed. Distinguish a calculated ideal crystal from an actual manufactured material, a numerical fit from independent validation, and a candidate ranking from an authorized design decision. A model should be evaluated by whether it rules out alternatives or informs an observable experiment, not by the complexity of its software or resolution of its graphics.

The unit's evidence record starts with **continuum geometry and constitutive calibration**. Collect **boundary loading, mesh, contacts, thermal properties, plasticity and fracture criteria** and prioritize tests such as **force balance, benchmark solutions and loaded specimens from representative processes**. The most dangerous untested assumption is **whether local defects or uncertainty invalidate a nominally safe stress contour**. Work backward from that possible failure: identify at least two competing explanations, a calculation that could distinguish them, an independently measurable outcome and a decision threshold. Be explicit if available observations cannot constrain the model. The five lessons progressively build a defensible case record.

## Unit field notebook — initial protocol

State a material formulation, one measurable target property, units, intended temperature/time/composition limits, specimen or simulated domain, governing hypotheses and error tolerance. Record a reference model with minimal complexity; describe where added atomistic, mesoscale, continuum or statistical detail would be necessary. List input uncertainty sources, computational convergence tests, independent measurement plans, future update conditions and rejection criteria. At the end of the unit, turn the notebook into a one-page auditable model-use statement.

## Lesson 4.1 — Finite elements and weak formulations

### Concept, governing relationships and physical intuition

Finite-element analysis approximates continuum fields over connected elements and enforces integral forms of balance laws. Constitutive relations link stress to strain and temperature; geometrical and material nonlinearity often change the result. Correct loads, constraints and contacts are as important as element density. Node count is not a proxy for a physically credible model.

**Modeling rule:** For linear isotropic uniaxial elasticity, strain equals stress divided by Young modulus. Specify the reference state, physical units, validity domain and a verification test before translating this rule into a material decision.

### Competing explanations: what would actually falsify the model?

**Case:** A beam simulation shows high stiffness because its boundary was unintentionally clamped against rotation. Form two mechanisms that predict different observables, then select a discriminating calculation or experiment rather than arguing from graphical fit alone.

**Possible reversal:** Linear isotropic material laws omit yield, damage, anisotropy and thermal residual stress. Test how changing temperature, composition, specimen condition or discretization could reverse the conclusion. Distinguish calibration agreement from independent verification.

### Synthetic quantitative notebook — inspect a dependency, not a material claim

The companion offline calculator is **Uniaxial elastic strain** with mathematical expression `s/200000*1e6`. Its adjustable input is **Applied engineering stress**, measured in MPa; output is reported in microstrain. At an illustrative input of 90 MPa, the displayed result is **450 microstrain**. A second invented input of 260 MPa gives **1300 microstrain**. The finite-difference response is 5 microstrain per MPa. Independently check the result and units. Values are illustrative, not measured material properties or validated predictions.

**Fixed assumptions and failure tests:** Linear uniaxial small-strain elasticity with E=200 GPa, no plasticity, creep, anisotropy, thermal stress or damage. Change one declared hidden assumption, identify how the trend might fail, and specify an independent benchmark. The teaching card is not a materials simulation engine.

### Build an evidence and validation protocol

**Targeted measurement or audit:** Check reaction-force balance and benchmark against beam theory and instrumented loading. Define material state, specimen/structure provenance, independent replicates, measurement uncertainty and explicit conditions under which your preferred model would be falsified.

**Minimum reproducibility artifact:** supply an input file, exact method and version, a computational convergence check, independent test values, units and uncertainty. Write a diagnostic table contrasting what is computed, what is physically measured and what the hypothesis still assumes. Retain failed calculations instead of filtering them away, and document material identity and sample history at a level a different laboratory could understand. If the full measurement is unavailable, report a conditional prediction rather than describing the candidate as qualified.

### Design decision and economic consequences

**Competing objectives:** A simple mechanics model is interpretable; a complex mesh is not intrinsically more accurate. Rank alternatives only after hard safety, feasibility and manufacturing requirements are satisfied; record the cost of a false positive and a missed candidate.

### Three substantial practice exercises and solution strategies

**Exercise 1 — physical reconstruction.** Explain “For linear isotropic uniaxial elasticity, strain equals stress divided by Young modulus.” in your own notation. Define the system, reference state, units, independent/dependent variables and at least two assumptions. Determine whether conservation, symmetry, force balance or statistical independence should be checked. Sketch one limiting case where the statement should simplify to a known result. **Solution strategy:** the derivation must use consistent dimensions and clearly say what the law does not predict; check an analytic, energy or mass-balance limit where available.

**Exercise 2 — calculation and uncertainty.** From `s/200000*1e6`, independently derive 450 microstrain for 90 MPa and compute one additional point halfway between the two example inputs. Estimate the sensitivity using a central perturbation, describe whether nonlinear dependence makes a one-number slope misleading, and add one plausible uncertainty in a fixed assumption. **Solution strategy:** perform an independent numerical calculation, propagate units before rounding, and report the interval conditional on the invented assumptions; do not use the resulting number as an empirical constant.

**Exercise 3 — independent comparison.** For “A beam simulation shows high stiffness because its boundary was unintentionally clamped against rotation.”, design the smallest credible cross-check using **Check reaction-force balance and benchmark against beam theory and instrumented loading.**. Specify two competing hypotheses, an observable they predict differently, necessary independent specimens or structures and a falsification criterion. Explain which observation would force you to abandon the simpler model, and which uncertainty could remain even if the immediate test passed. **Solution strategy:** make the experiment capable of rejecting the preferred mechanism and protect the test from fitting-data leakage or unrecorded sample exclusions.

### Research memo and readiness check

Write an evidence table separating observations, simulations, calibration, independent tests and remaining risk. Propose a small reversible next experiment with a stop/go rule.

<!-- MODEL_6 -->

## Lesson 4.3 — Constitutive laws, plasticity and damage

### Concept, governing relationships and physical intuition

Elasticity, plasticity, viscoelasticity and damage require different history variables. Yield criteria and hardening laws describe paths rather than single property values. An equivalent stress result can hide multiaxiality and cyclic load effects. Parameter fitting from one monotonic curve usually cannot validate fatigue or creep predictions.

**Modeling rule:** Constitutive state evolves with load, temperature, rate and prior deformation, not geometry alone. Specify the reference state, physical units, validity domain and a verification test before translating this rule into a material decision.

### Competing explanations: what would actually falsify the model?

**Case:** A polymer insert passes short compression testing but creeps during long-term service. Form two mechanisms that predict different observables, then select a discriminating calculation or experiment rather than arguing from graphical fit alone.

**Possible reversal:** Rate-independent plasticity cannot automatically model time-dependent creep. Test how changing temperature, composition, specimen condition or discretization could reverse the conclusion. Distinguish calibration agreement from independent verification.

### Synthetic quantitative notebook — inspect a dependency, not a material claim

The companion offline calculator is **Uniaxial elastic strain** with mathematical expression `s/200000*1e6`. Its adjustable input is **Applied engineering stress**, measured in MPa; output is reported in microstrain. At an illustrative input of 120 MPa, the displayed result is **600 microstrain**. A second invented input of 280 MPa gives **1400 microstrain**. The finite-difference response is 5 microstrain per MPa. Independently check the result and units. Values are illustrative, not measured material properties or validated predictions.

**Fixed assumptions and failure tests:** Linear uniaxial small-strain elasticity with E=200 GPa, no plasticity, creep, anisotropy, thermal stress or damage. Change one declared hidden assumption, identify how the trend might fail, and specify an independent benchmark. The teaching card is not a materials simulation engine.

### Build an evidence and validation protocol

**Targeted measurement or audit:** Use loading/unloading cycles, rate sweeps and independent hold tests to identify parameter scope. Define material state, specimen/structure provenance, independent replicates, measurement uncertainty and explicit conditions under which your preferred model would be falsified.

**Minimum reproducibility artifact:** supply an input file, exact method and version, a computational convergence check, independent test values, units and uncertainty. Write a diagnostic table contrasting what is computed, what is physically measured and what the hypothesis still assumes. Retain failed calculations instead of filtering them away, and document material identity and sample history at a level a different laboratory could understand. If the full measurement is unavailable, report a conditional prediction rather than describing the candidate as qualified.

### Design decision and economic consequences

**Competing objectives:** A more complex law needs more independent characterization and may be less stable numerically. Rank alternatives only after hard safety, feasibility and manufacturing requirements are satisfied; record the cost of a false positive and a missed candidate.

### Three substantial practice exercises and solution strategies

**Exercise 1 — physical reconstruction.** Explain “Constitutive state evolves with load, temperature, rate and prior deformation, not geometry alone.” in your own notation. Define the system, reference state, units, independent/dependent variables and at least two assumptions. Determine whether conservation, symmetry, force balance or statistical independence should be checked. Sketch one limiting case where the statement should simplify to a known result. **Solution strategy:** the derivation must use consistent dimensions and clearly say what the law does not predict; check an analytic, energy or mass-balance limit where available.

**Exercise 2 — calculation and uncertainty.** From `s/200000*1e6`, independently derive 600 microstrain for 120 MPa and compute one additional point halfway between the two example inputs. Estimate the sensitivity using a central perturbation, describe whether nonlinear dependence makes a one-number slope misleading, and add one plausible uncertainty in a fixed assumption. **Solution strategy:** perform an independent numerical calculation, propagate units before rounding, and report the interval conditional on the invented assumptions; do not use the resulting number as an empirical constant.

**Exercise 3 — independent comparison.** For “A polymer insert passes short compression testing but creeps during long-term service.”, design the smallest credible cross-check using **Use loading/unloading cycles, rate sweeps and independent hold tests to identify parameter scope.**. Specify two competing hypotheses, an observable they predict differently, necessary independent specimens or structures and a falsification criterion. Explain which observation would force you to abandon the simpler model, and which uncertainty could remain even if the immediate test passed. **Solution strategy:** make the experiment capable of rejecting the preferred mechanism and protect the test from fitting-data leakage or unrecorded sample exclusions.

### Research memo and readiness check

Write an evidence table separating observations, simulations, calibration, independent tests and remaining risk. Propose a small reversible next experiment with a stop/go rule.

<!-- MODEL_7 -->

## Lesson 4.5 — Concurrent and hierarchical multiscale coupling

### Concept, governing relationships and physical intuition

Atomistic calculations can suggest defect energies, diffusivities or moduli passed to mesoscale and continuum tools. A handoff can amplify input bias, ignore microstructural distributions, or double count physical mechanisms. Coupled schemes must conserve relevant quantities and reconcile interfaces in time and length scale. Propagating uncertainty is more important than passing a single best-fit number.

**Modeling rule:** Effective property depends on microstructure, volume fractions, topology and loading as well as constituents. Specify the reference state, physical units, validity domain and a verification test before translating this rule into a material decision.

### Competing explanations: what would actually falsify the model?

**Case:** An atomistically estimated elastic modulus is applied to a porous printed lattice as if it were a dense continuum. Form two mechanisms that predict different observables, then select a discriminating calculation or experiment rather than arguing from graphical fit alone.

**Possible reversal:** Scale-bridging assumptions fail near localization, interfaces or unrepresentative volume elements. Test how changing temperature, composition, specimen condition or discretization could reverse the conclusion. Distinguish calibration agreement from independent verification.

### Synthetic quantitative notebook — inspect a dependency, not a material claim

The companion offline calculator is **Uniaxial elastic strain** with mathematical expression `s/200000*1e6`. Its adjustable input is **Applied engineering stress**, measured in MPa; output is reported in microstrain. At an illustrative input of 150 MPa, the displayed result is **750 microstrain**. A second invented input of 310 MPa gives **1550 microstrain**. The finite-difference response is 5 microstrain per MPa. Independently check the result and units. Values are illustrative, not measured material properties or validated predictions.

**Fixed assumptions and failure tests:** Linear uniaxial small-strain elasticity with E=200 GPa, no plasticity, creep, anisotropy, thermal stress or damage. Change one declared hidden assumption, identify how the trend might fail, and specify an independent benchmark. The teaching card is not a materials simulation engine.

### Build an evidence and validation protocol

**Targeted measurement or audit:** Compare effective constants against representative-volume simulations and physical specimens at relevant scales. Define material state, specimen/structure provenance, independent replicates, measurement uncertainty and explicit conditions under which your preferred model would be falsified.

**Minimum reproducibility artifact:** supply an input file, exact method and version, a computational convergence check, independent test values, units and uncertainty. Write a diagnostic table contrasting what is computed, what is physically measured and what the hypothesis still assumes. Retain failed calculations instead of filtering them away, and document material identity and sample history at a level a different laboratory could understand. If the full measurement is unavailable, report a conditional prediction rather than describing the candidate as qualified.

### Design decision and economic consequences

**Competing objectives:** Multiscale detail is valuable when it changes a decision, not merely because multiple solvers are available. Rank alternatives only after hard safety, feasibility and manufacturing requirements are satisfied; record the cost of a false positive and a missed candidate.

### Three substantial practice exercises and solution strategies

**Exercise 1 — physical reconstruction.** Explain “Effective property depends on microstructure, volume fractions, topology and loading as well as constituents.” in your own notation. Define the system, reference state, units, independent/dependent variables and at least two assumptions. Determine whether conservation, symmetry, force balance or statistical independence should be checked. Sketch one limiting case where the statement should simplify to a known result. **Solution strategy:** the derivation must use consistent dimensions and clearly say what the law does not predict; check an analytic, energy or mass-balance limit where available.

**Exercise 2 — calculation and uncertainty.** From `s/200000*1e6`, independently derive 750 microstrain for 150 MPa and compute one additional point halfway between the two example inputs. Estimate the sensitivity using a central perturbation, describe whether nonlinear dependence makes a one-number slope misleading, and add one plausible uncertainty in a fixed assumption. **Solution strategy:** perform an independent numerical calculation, propagate units before rounding, and report the interval conditional on the invented assumptions; do not use the resulting number as an empirical constant.

**Exercise 3 — independent comparison.** For “An atomistically estimated elastic modulus is applied to a porous printed lattice as if it were a dense continuum.”, design the smallest credible cross-check using **Compare effective constants against representative-volume simulations and physical specimens at relevant scales.**. Specify two competing hypotheses, an observable they predict differently, necessary independent specimens or structures and a falsification criterion. Explain which observation would force you to abandon the simpler model, and which uncertainty could remain even if the immediate test passed. **Solution strategy:** make the experiment capable of rejecting the preferred mechanism and protect the test from fitting-data leakage or unrecorded sample exclusions.

### Research memo and readiness check

Write an evidence table separating observations, simulations, calibration, independent tests and remaining risk. Propose a small reversible next experiment with a stop/go rule.

## Unit 4 capstone: integrate calculations with evidence

**Practical challenge:** A finite-element model predicts low stress in a welded component that fails near a notch. Diagnose the mesh, residual stress, damage law, fatigue load spectrum, contact, manufacturing history and physical tests.

1. **Define material state and performance.** State composition, phase/microstructure, processing history, external constraints, independent material specimens and the exact observable to be predicted. State the intended decision and penalty of a wrong choice.
2. **Reproduce quantitative work.** Run both synthetic interactive formulas at three inputs, independently recompute the results, and identify the nonphysical or unmeasured assumptions. Develop one additional first-principles or measured-model benchmark that would test the physics rather than just the code.
3. **Test alternative explanations.** Use **continuum geometry and constitutive calibration**, explicitly log **boundary loading, mesh, contacts, thermal properties, plasticity and fracture criteria**, and challenge the model with **force balance, benchmark solutions and loaded specimens from representative processes**. Describe an observation that would falsify the preferred hypothesis. Separate calibration, validation and engineering qualification evidence.
4. **Quantify uncertainty and feasibility.** Include one numerical convergence test, one physical or statistical uncertainty propagation, one out-of-domain stress test, one materials supply or production constraint and a feasible low-cost validation plan.
5. **Deliver an auditable recommendation.** Produce a two-page technical decision, reproducibility checklist, complete candidate table and stop/go rule. Explicitly revisit **whether local defects or uncertainty invalidate a nominally safe stress contour**. No synthetic formula output authorizes use of a safety-critical material or device.

### Concluding reflection

A physical model earns trust by surviving attempts to falsify its assumptions within a defined application, not by producing a large dataset or intricate graphics. Distinguish numerical convergence, agreement on fitted points, generalization to new material states and functional qualification of real parts. If any step remains missing, state which research question is answerable and which engineering recommendation must be deferred.

