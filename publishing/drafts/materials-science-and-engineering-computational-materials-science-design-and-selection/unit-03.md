# Unit 3: Thermodynamics, Kinetics and Mesoscale Models

**Guiding question:** How do transport and thermodynamic driving forces produce evolving microstructure?

## Problem framing and scale selection

A heat-treated alloy develops a precipitate pattern at odds with an equilibrium phase chart. Connect driving force, nucleation barriers, diffusion, thermal history, defects, and characterization time scales instead of fitting an arbitrary time constant. No materials simulation is interpretable until its target observable, reference material state, environmental range and intended downstream decision are fixed. Distinguish a calculated ideal crystal from an actual manufactured material, a numerical fit from independent validation, and a candidate ranking from an authorized design decision. A model should be evaluated by whether it rules out alternatives or informs an observable experiment, not by the complexity of its software or resolution of its graphics.

The unit's evidence record starts with **calibrated phase and mobility descriptions**. Collect **phase compositions, free energies, diffusivities, nucleation assumptions and thermal history** and prioritize tests such as **phase measurements, spatial patterns and kinetic time-series across controlled specimens**. The most dangerous untested assumption is **whether equilibrium diagrams are mistakenly treated as sufficient kinetic predictions**. Work backward from that possible failure: identify at least two competing explanations, a calculation that could distinguish them, an independently measurable outcome and a decision threshold. Be explicit if available observations cannot constrain the model. The five lessons progressively build a defensible case record.

## Unit field notebook — initial protocol

State a material formulation, one measurable target property, units, intended temperature/time/composition limits, specimen or simulated domain, governing hypotheses and error tolerance. Record a reference model with minimal complexity; describe where added atomistic, mesoscale, continuum or statistical detail would be necessary. List input uncertainty sources, computational convergence tests, independent measurement plans, future update conditions and rejection criteria. At the end of the unit, turn the notebook into a one-page auditable model-use statement.

## Lesson 3.1 — Chemical potentials and phase stability

### Concept, governing relationships and physical intuition

Phase selection follows free-energy minimization under composition, temperature, pressure and phase constraints. A convex hull organizes competing phases at a selected state; distance above the hull indicates metastability within the reference set, not a universal guarantee of synthesizability. Competing structures and reference compositions must be included, and kinetic barriers can preserve metastable structures.

**Modeling rule:** At a fixed state, equilibrium minimizes the appropriate free-energy potential subject to conservation. Specify the reference state, physical units, validity domain and a verification test before translating this rule into a material decision.

### Competing explanations: what would actually falsify the model?

**Case:** A computed low-energy compound fails repeatedly in one synthesis route. Form two mechanisms that predict different observables, then select a discriminating calculation or experiment rather than arguing from graphical fit alone.

**Possible reversal:** Missing competing phases, vibrational terms and kinetics can change the apparent stable set. Test how changing temperature, composition, specimen condition or discretization could reverse the conclusion. Distinguish calibration agreement from independent verification.

### Synthetic quantitative notebook — inspect a dependency, not a material claim

The companion offline calculator is **One-dimensional diffusion RMS displacement** with mathematical expression `Math.sqrt(2*1e-16*t*3600)*1e6`. Its adjustable input is **Diffusion time**, measured in h; output is reported in µm. At an illustrative input of 18.5 h, the displayed result is **3.64965752 µm**. A second invented input of 64 h gives **6.7882251 µm**. The finite-difference response is 0.0689795073 µm per h. Independently check the result and units. Values are illustrative, not measured material properties or validated predictions.

**Fixed assumptions and failure tests:** Constant D=1e−16 m²/s and unbounded 1D diffusion; effective transport in real materials can be anisotropic, concentration-dependent, trapped or boundary-limited. Change one declared hidden assumption, identify how the trend might fail, and specify an independent benchmark. The teaching card is not a materials simulation engine.

### Build an evidence and validation protocol

**Targeted measurement or audit:** Check alternative phase libraries, reference consistency and observed synthesis paths before making a phase claim. Define material state, specimen/structure provenance, independent replicates, measurement uncertainty and explicit conditions under which your preferred model would be falsified.

**Minimum reproducibility artifact:** supply an input file, exact method and version, a computational convergence check, independent test values, units and uncertainty. Write a diagnostic table contrasting what is computed, what is physically measured and what the hypothesis still assumes. Retain failed calculations instead of filtering them away, and document material identity and sample history at a level a different laboratory could understand. If the full measurement is unavailable, report a conditional prediction rather than describing the candidate as qualified.

### Design decision and economic consequences

**Competing objectives:** Equilibrium screening is fast; a useful processing recommendation also needs kinetic and safety evidence. Rank alternatives only after hard safety, feasibility and manufacturing requirements are satisfied; record the cost of a false positive and a missed candidate.

### Three substantial practice exercises and solution strategies

**Exercise 1 — physical reconstruction.** Explain “At a fixed state, equilibrium minimizes the appropriate free-energy potential subject to conservation.” in your own notation. Define the system, reference state, units, independent/dependent variables and at least two assumptions. Determine whether conservation, symmetry, force balance or statistical independence should be checked. Sketch one limiting case where the statement should simplify to a known result. **Solution strategy:** the derivation must use consistent dimensions and clearly say what the law does not predict; check an analytic, energy or mass-balance limit where available.

**Exercise 2 — calculation and uncertainty.** From `Math.sqrt(2*1e-16*t*3600)*1e6`, independently derive 3.64965752 µm for 18.5 h and compute one additional point halfway between the two example inputs. Estimate the sensitivity using a central perturbation, describe whether nonlinear dependence makes a one-number slope misleading, and add one plausible uncertainty in a fixed assumption. **Solution strategy:** perform an independent numerical calculation, propagate units before rounding, and report the interval conditional on the invented assumptions; do not use the resulting number as an empirical constant.

**Exercise 3 — independent comparison.** For “A computed low-energy compound fails repeatedly in one synthesis route.”, design the smallest credible cross-check using **Check alternative phase libraries, reference consistency and observed synthesis paths before making a phase claim.**. Specify two competing hypotheses, an observable they predict differently, necessary independent specimens or structures and a falsification criterion. Explain which observation would force you to abandon the simpler model, and which uncertainty could remain even if the immediate test passed. **Solution strategy:** make the experiment capable of rejecting the preferred mechanism and protect the test from fitting-data leakage or unrecorded sample exclusions.

### Research memo and readiness check

Write an evidence table separating observations, simulations, calibration, independent tests and remaining risk. Propose a small reversible next experiment with a stop/go rule.

<!-- MODEL_4 -->

## Lesson 3.3 — Nucleation, growth and stochastic events

### Concept, governing relationships and physical intuition

The appearance of a new phase involves interfacial cost, chemical driving force and local structural fluctuations. Classical nucleation theory illustrates why a barrier can persist even when a product phase lowers bulk free energy. Kinetic Monte Carlo propagates probabilities for defined event catalogs and rates; omitting an important event can invalidate simulated time.

**Modeling rule:** Arrhenius-type event rates depend exponentially on an activation barrier over thermal energy. Specify the reference state, physical units, validity domain and a verification test before translating this rule into a material decision.

### Competing explanations: what would actually falsify the model?

**Case:** A precipitate distribution forms hours later than a fitted deterministic transformation curve predicts. Form two mechanisms that predict different observables, then select a discriminating calculation or experiment rather than arguing from graphical fit alone.

**Possible reversal:** Small changes in the assumed barrier, available sites and attempt frequency can dominate predictions. Test how changing temperature, composition, specimen condition or discretization could reverse the conclusion. Distinguish calibration agreement from independent verification.

### Synthetic quantitative notebook — inspect a dependency, not a material claim

The companion offline calculator is **One-dimensional diffusion RMS displacement** with mathematical expression `Math.sqrt(2*1e-16*t*3600)*1e6`. Its adjustable input is **Diffusion time**, measured in h; output is reported in µm. At an illustrative input of 26 h, the displayed result is **4.32666153 µm**. A second invented input of 70 h gives **7.09929574 µm**. The finite-difference response is 0.0630144138 µm per h. Independently check the result and units. Values are illustrative, not measured material properties or validated predictions.

**Fixed assumptions and failure tests:** Constant D=1e−16 m²/s and unbounded 1D diffusion; effective transport in real materials can be anisotropic, concentration-dependent, trapped or boundary-limited. Change one declared hidden assumption, identify how the trend might fail, and specify an independent benchmark. The teaching card is not a materials simulation engine.

### Build an evidence and validation protocol

**Targeted measurement or audit:** Measure transformed fractions at multiple times and thermal conditions and compare distribution shapes, not only averages. Define material state, specimen/structure provenance, independent replicates, measurement uncertainty and explicit conditions under which your preferred model would be falsified.

**Minimum reproducibility artifact:** supply an input file, exact method and version, a computational convergence check, independent test values, units and uncertainty. Write a diagnostic table contrasting what is computed, what is physically measured and what the hypothesis still assumes. Retain failed calculations instead of filtering them away, and document material identity and sample history at a level a different laboratory could understand. If the full measurement is unavailable, report a conditional prediction rather than describing the candidate as qualified.

### Design decision and economic consequences

**Competing objectives:** Stochastic models capture rare events but can become impractical when event catalogs are incomplete. Rank alternatives only after hard safety, feasibility and manufacturing requirements are satisfied; record the cost of a false positive and a missed candidate.

### Three substantial practice exercises and solution strategies

**Exercise 1 — physical reconstruction.** Explain “Arrhenius-type event rates depend exponentially on an activation barrier over thermal energy.” in your own notation. Define the system, reference state, units, independent/dependent variables and at least two assumptions. Determine whether conservation, symmetry, force balance or statistical independence should be checked. Sketch one limiting case where the statement should simplify to a known result. **Solution strategy:** the derivation must use consistent dimensions and clearly say what the law does not predict; check an analytic, energy or mass-balance limit where available.

**Exercise 2 — calculation and uncertainty.** From `Math.sqrt(2*1e-16*t*3600)*1e6`, independently derive 4.32666153 µm for 26 h and compute one additional point halfway between the two example inputs. Estimate the sensitivity using a central perturbation, describe whether nonlinear dependence makes a one-number slope misleading, and add one plausible uncertainty in a fixed assumption. **Solution strategy:** perform an independent numerical calculation, propagate units before rounding, and report the interval conditional on the invented assumptions; do not use the resulting number as an empirical constant.

**Exercise 3 — independent comparison.** For “A precipitate distribution forms hours later than a fitted deterministic transformation curve predicts.”, design the smallest credible cross-check using **Measure transformed fractions at multiple times and thermal conditions and compare distribution shapes, not only averages.**. Specify two competing hypotheses, an observable they predict differently, necessary independent specimens or structures and a falsification criterion. Explain which observation would force you to abandon the simpler model, and which uncertainty could remain even if the immediate test passed. **Solution strategy:** make the experiment capable of rejecting the preferred mechanism and protect the test from fitting-data leakage or unrecorded sample exclusions.

### Research memo and readiness check

Write an evidence table separating observations, simulations, calibration, independent tests and remaining risk. Propose a small reversible next experiment with a stop/go rule.

<!-- MODEL_5 -->

## Lesson 3.5 — Calphad, database coverage and multiscale handoffs

### Concept, governing relationships and physical intuition

CALPHAD uses parameterized Gibbs energy descriptions fitted to thermochemical and phase-equilibrium evidence. Thermodynamic assessments have composition, temperature and phase-coverage boundaries. Linking CALPHAD to diffusion or phase-field models requires compatible reference states and mobility databases. Uncertainty can increase near sparse data or metastable extrapolation.

**Modeling rule:** Phase fractions and chemical potentials follow constrained minimization of the assessed Gibbs energy model. Specify the reference state, physical units, validity domain and a verification test before translating this rule into a material decision.

### Competing explanations: what would actually falsify the model?

**Case:** A promising five-element alloy composition lies outside the experimentally assessed composition ranges. Form two mechanisms that predict different observables, then select a discriminating calculation or experiment rather than arguing from graphical fit alone.

**Possible reversal:** Extrapolating a binary assessment into high-order alloys is not a validated prediction by itself. Test how changing temperature, composition, specimen condition or discretization could reverse the conclusion. Distinguish calibration agreement from independent verification.

### Synthetic quantitative notebook — inspect a dependency, not a material claim

The companion offline calculator is **One-dimensional diffusion RMS displacement** with mathematical expression `Math.sqrt(2*1e-16*t*3600)*1e6`. Its adjustable input is **Diffusion time**, measured in h; output is reported in µm. At an illustrative input of 33.5 h, the displayed result is **4.91121166 µm**. A second invented input of 75.5 h gives **7.37292344 µm**. The finite-difference response is 0.0586121851 µm per h. Independently check the result and units. Values are illustrative, not measured material properties or validated predictions.

**Fixed assumptions and failure tests:** Constant D=1e−16 m²/s and unbounded 1D diffusion; effective transport in real materials can be anisotropic, concentration-dependent, trapped or boundary-limited. Change one declared hidden assumption, identify how the trend might fail, and specify an independent benchmark. The teaching card is not a materials simulation engine.

### Build an evidence and validation protocol

**Targeted measurement or audit:** Inspect model assessment records and compare targeted diffraction, calorimetry or microscopy across the design region. Define material state, specimen/structure provenance, independent replicates, measurement uncertainty and explicit conditions under which your preferred model would be falsified.

**Minimum reproducibility artifact:** supply an input file, exact method and version, a computational convergence check, independent test values, units and uncertainty. Write a diagnostic table contrasting what is computed, what is physically measured and what the hypothesis still assumes. Retain failed calculations instead of filtering them away, and document material identity and sample history at a level a different laboratory could understand. If the full measurement is unavailable, report a conditional prediction rather than describing the candidate as qualified.

### Design decision and economic consequences

**Competing objectives:** Databases accelerate screening but require licensing, provenance and explicit validity checks. Rank alternatives only after hard safety, feasibility and manufacturing requirements are satisfied; record the cost of a false positive and a missed candidate.

### Three substantial practice exercises and solution strategies

**Exercise 1 — physical reconstruction.** Explain “Phase fractions and chemical potentials follow constrained minimization of the assessed Gibbs energy model.” in your own notation. Define the system, reference state, units, independent/dependent variables and at least two assumptions. Determine whether conservation, symmetry, force balance or statistical independence should be checked. Sketch one limiting case where the statement should simplify to a known result. **Solution strategy:** the derivation must use consistent dimensions and clearly say what the law does not predict; check an analytic, energy or mass-balance limit where available.

**Exercise 2 — calculation and uncertainty.** From `Math.sqrt(2*1e-16*t*3600)*1e6`, independently derive 4.91121166 µm for 33.5 h and compute one additional point halfway between the two example inputs. Estimate the sensitivity using a central perturbation, describe whether nonlinear dependence makes a one-number slope misleading, and add one plausible uncertainty in a fixed assumption. **Solution strategy:** perform an independent numerical calculation, propagate units before rounding, and report the interval conditional on the invented assumptions; do not use the resulting number as an empirical constant.

**Exercise 3 — independent comparison.** For “A promising five-element alloy composition lies outside the experimentally assessed composition ranges.”, design the smallest credible cross-check using **Inspect model assessment records and compare targeted diffraction, calorimetry or microscopy across the design region.**. Specify two competing hypotheses, an observable they predict differently, necessary independent specimens or structures and a falsification criterion. Explain which observation would force you to abandon the simpler model, and which uncertainty could remain even if the immediate test passed. **Solution strategy:** make the experiment capable of rejecting the preferred mechanism and protect the test from fitting-data leakage or unrecorded sample exclusions.

### Research memo and readiness check

Write an evidence table separating observations, simulations, calibration, independent tests and remaining risk. Propose a small reversible next experiment with a stop/go rule.

## Unit 3 capstone: integrate calculations with evidence

**Practical challenge:** A heat-treated alloy develops a precipitate pattern at odds with an equilibrium phase chart. Connect driving force, nucleation barriers, diffusion, thermal history, defects, and characterization time scales instead of fitting an arbitrary time constant.

1. **Define material state and performance.** State composition, phase/microstructure, processing history, external constraints, independent material specimens and the exact observable to be predicted. State the intended decision and penalty of a wrong choice.
2. **Reproduce quantitative work.** Run both synthetic interactive formulas at three inputs, independently recompute the results, and identify the nonphysical or unmeasured assumptions. Develop one additional first-principles or measured-model benchmark that would test the physics rather than just the code.
3. **Test alternative explanations.** Use **calibrated phase and mobility descriptions**, explicitly log **phase compositions, free energies, diffusivities, nucleation assumptions and thermal history**, and challenge the model with **phase measurements, spatial patterns and kinetic time-series across controlled specimens**. Describe an observation that would falsify the preferred hypothesis. Separate calibration, validation and engineering qualification evidence.
4. **Quantify uncertainty and feasibility.** Include one numerical convergence test, one physical or statistical uncertainty propagation, one out-of-domain stress test, one materials supply or production constraint and a feasible low-cost validation plan.
5. **Deliver an auditable recommendation.** Produce a two-page technical decision, reproducibility checklist, complete candidate table and stop/go rule. Explicitly revisit **whether equilibrium diagrams are mistakenly treated as sufficient kinetic predictions**. No synthetic formula output authorizes use of a safety-critical material or device.

### Concluding reflection

A physical model earns trust by surviving attempts to falsify its assumptions within a defined application, not by producing a large dataset or intricate graphics. Distinguish numerical convergence, agreement on fitted points, generalization to new material states and functional qualification of real parts. If any step remains missing, state which research question is answerable and which engineering recommendation must be deferred.

