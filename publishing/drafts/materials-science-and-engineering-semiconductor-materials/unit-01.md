# Unit 1: Crystal structures, bonding, and material families

**Central research question:** How does atomic organization constrain the electronic and mechanical behavior of a semiconductor?

## Material and device context

Composition and crystal structure determine what electronic states are possible, but grown films acquire dislocations, surfaces and strain histories that may dominate performance. Lattice parameter is a geometrical quantity; electrical reliability is a systems measurement.

Diffraction and microscopy complement one another because diffraction averages coherently over probed volume, while local microscopy sees defects that may be rare but electrically catastrophic.

**Scope of this unit:** Study **long-range order, alloy chemistry and crystalline defects** while distinguishing **lattice geometry versus actual epitaxial strain**. Practical interpretation requires **wafer orientation, composition, diffraction geometry and temperature**. An important alternative is **instrument angle offset, relaxation or compositional gradients**, which is why **high-resolution reciprocal-space mapping and calibrated chemical profiling** must be part of a credible validation programme. These topics are inseparable from geometry, scale and specimen history; a nominal textbook material is not a sufficiently specified industrial sample.

The unit contains five distinct lessons and two local calculators. Each lesson names a physical relationship or decision rule, illustrates a real measurement dilemma without inventing real measurements, proposes a second measurement and tests an assumption. All calculator curves are synthetic output from one declared formula. Their intended role is conceptual sensitivity exploration, not material parameter fitting.

## Measurement-first reading checkpoint

Before reading lesson 1, sketch the specimen or experiment. Label axes and state whether your variables are energetic, volumetric, areal, temporal or geometric. Identify one observable that you could record directly, one quantity that requires a model to infer, and one missing process variable. A useful figure has units and a declared temperature; an energy-level sketch should distinguish applied bias from equilibrium. Keep the same conventions throughout the unit and revisit them in the integrated investigation.

## Lesson 1.1: Semiconductor identity beyond a band gap

### A physical explanation before any numerical fit

The distinction between elemental Si and Ge, compound III–V and II–VI families, and layered or organic semiconductors begins with chemistry and bonding. Covalent tetrahedral coordination supports diamond and zinc-blende arrangements, but ionic contributions and chemical ordering modify phonons, dielectric response, and defect energetics. A nominal gap by itself cannot determine electron mobility, dopant solubility, contact resistance, or device reliability. An alloy composition is a state variable, not a material identity: the local ordering, strain, impurity concentrations, and previous heat history must also be specified.

**Primary relationship:** Identity requires structural phase, chemical makeup, electronic state, and measurement condition. The first task is to decide whether it is a structural geometric relation, a balance law, a statistical approximation or an experimentally calibrated response. This matters specifically for **semiconductor identity beyond a band gap**, because the same calculated number can emerge from physically incompatible material states. Explicitly note which band, lattice, impurity, contact or interface degrees of freedom the expression leaves out. A clear statement of validity is often more useful than giving the output to five decimal places.

A team replaces crystalline silicon with a higher-mobility III–V alloy in a low-power transistor. Compare band gap, lattice matching, oxide interface quality, thermal budget, substrate cost, and long-term trap behavior. A substitution based on a tabulated mobility ignores fabrication compatibility.

For a realistic assessment, distinguish directly controlled inputs from inferred ones. In this lesson, the relevant controls include **wafer orientation, composition, diffraction geometry and temperature**; measure each where possible and report the resolution or calibration of the instrument. A model fit that adjusts an unmeasured constant to match one observable does not establish that the associated mechanism is correct. Ask whether **instrument angle offset, relaxation or compositional gradients** could produce the same sign of change and what independent feature would differ. If the two proposed mechanisms are observationally indistinguishable under the existing design, the next scientific contribution is a better experiment rather than a more elaborate fit.

### Transparent worked numerical example

The offline calculator **Epitaxial lattice mismatch** is deliberately simpler than the phenomenon being discussed. Let **Relaxed film lattice parameter = 5.4377778 angstrom**. From the implemented expression `100*(af-5.431)/5.431`, the predicted value is **0.12479797 %**. Change only the designated control to **5.4666667 angstrom** and the result becomes **0.656723746 %**. In this controlled comparison the predicted quantity rises; the finite-difference sensitivity is **18.4128153 (%)/(angstrom)**. This numerical result is deterministic, derived directly from the stated formula, and is *not* an observation of an actual sample. The two values illustrate what that formula encodes; they do not prove the material will behave this way.

The complete assumptions are: **Cubic aligned substrate a=5.431 Å, same temperature and relaxed film parameter; geometry-only mismatch; not a prediction of dislocations**. Before interpreting the slope, check that the denominator of the expression cannot vanish in the slider range and that the output is in the declared units. A synthetic curve is not a scientific uncertainty band: there are no replicate wafers, measurement errors or competing mechanisms in this dataset. The correct conclusion is conditional—*if the stated assumptions hold, changing the input produces the computed result*. Any statement about a real device needs experimental comparison and fit diagnostics.

A second way to reason about the worked case is through limiting behavior. Choose the smallest permitted input and the largest permitted input, then predict the direction of response from the physical model before viewing the plot. Explain whether the mathematical extrapolation implies an unrealistic carrier state, a breakdown of continuum physics, a strained rather than relaxed material, or a measurement range that would make the assumptions fail. This is an active check on intuition, not an instruction to operate laboratory equipment at the slider endpoints.

### Measurement plan and what the model can miss

A high measured mobility in a pristine bulk crystal does not predict an inversion-channel mobility at a dirty dielectric interface.

Begin with **reciprocal-space X-ray mapping**; record **calibration standard, incident wavelength, alignment, and sample temperature** and independently compare against **atomic-resolution cross-sectional imaging**. Because the original measurement and the independent technique interrogate different aspects of a sample, agreement strengthens a claim, while disagreement can locate the missing effect. A structural analysis might average over a large volume while an electrical test disproportionately samples a thin channel. Temperature-dependent optical data can distinguish activation from transport in some settings, but only if spectral calibration and carrier injection are independently controlled.

Perform a **charge neutrality audit**: Verify the sign and physical units of electrons, holes, ionized donors and acceptors; document compensation. Follow with a **thermodynamic regime audit**: Identify whether equilibrium, degenerate statistics, hot carriers, low injection, or finite-bias gradients alter validity. State which quantity is known from calibration, which is inferred from a model, and which remains unknown. When the largest plausible uncertainty is in an unmeasured constant rather than in instrumental precision, a highly precise displayed number is misleading. Develop a repeatable sample ID and uncertainty budget rather than inventing error bars to make a synthetic demonstration look experimental.

### Experimental counterfactual

The leading interpretation connects **long-range order, alloy chemistry and crystalline defects** with a response in **semiconductor identity beyond a band gap**. Now suppose instead that the change is controlled by **instrument angle offset, relaxation or compositional gradients**. Both mechanisms could sometimes reproduce a monotonic trend in the single-variable calculator. A useful counterfactual is to change a second condition that affects one mechanism more strongly than the other—temperature, optical excitation depth, contact geometry, wafer thickness, crystal orientation or measurement frequency—while leaving the primary comparison matched. Explain how **high-resolution reciprocal-space mapping and calibrated chemical profiling** would be expected to discriminate the two models, and report in advance which outcome would overturn the preferred explanation.

Use the experiment to locate the model's domain, not simply to force a match. If a material has multiple carrier channels, a Hall analysis under the single-carrier approximation must be re-examined. If defect populations change during processing, an initially clean band diagram will not reflect the new trap dynamics. And if a wafer has pronounced spatial inhomogeneity, a measurement at one position should not be called a representative material property. Every conclusion should name its sample, conditions and unresolved alternative.

### Three graded problems

**Problem 1.1A — Conceptual mechanism.** Explain in your own words what **semiconductor identity beyond a band gap** changes about the relation between **lattice geometry versus actual epitaxial strain**. State two different microphysical mechanisms that could produce the same measured sign of response. Identify a relevant energy, length or time scale and show why the difference would matter for interpretation.

**Problem 1.1B — Quantitative verification.** Reproduce the values **0.12479797 %** and **0.656723746 %** using `100*(af-5.431)/5.431` at the two stated input values. Convert at least one related physical quantity to coherent SI units, report units in each algebraic step, and explain why increasing the model's input by the displayed amount makes the computed output rises. Which hidden material parameter could reverse a real-world trend?

**Problem 1.1C — Falsification and reporting.** Design a minimum independent experiment capable of distinguishing the current interpretation from **instrument angle offset, relaxation or compositional gradients**. Specify sampling locations, temperature, instrument calibration, measurement geometry, between-sample replication, and an observable that would force you to reject the interpretation. Name one specific circumstance in which **Epitaxial lattice mismatch** should not be treated as predictive.

<!-- MODEL_0 -->

## Lesson 1.2: Diamond, zinc blende, and wurtzite lattices

### A physical explanation before any numerical fit

Diamond cubic Si has two interpenetrating face-centered-cubic sublattices with identical atoms. Zinc blende retains the tetrahedral connectivity but assigns different species to the sublattices. Wurtzite uses hexagonal stacking and can support a polar axis and spontaneous polarization depending on chemical identity. Miller indices identify plane families, while interplanar spacing and the reciprocal lattice connect atomic geometry to diffraction. When reporting a lattice parameter, distinguish conventional cubic cell parameters from nearest-neighbor distance and measured strain.

**Primary relationship:** Bragg diffraction relates plane spacing d, order m, wavelength λ, and angle θ by mλ=2d sin θ. The first task is to decide whether it is a structural geometric relation, a balance law, a statistical approximation or an experimentally calibrated response. This matters specifically for **diamond, zinc blende, and wurtzite lattices**, because the same calculated number can emerge from physically incompatible material states. Explicitly note which band, lattice, impurity, contact or interface degrees of freedom the expression leaves out. A clear statement of validity is often more useful than giving the output to five decimal places.

A diffraction peak moves after a GaN epitaxial growth run. Calculate whether a changed spacing or a different diffracting plane could account for the angular shift. Confirm instrumental zero offset before attributing the movement to strain.

### Transparent worked numerical example

The offline calculator **Bragg diffraction angle** is deliberately simpler than the phenomenon being discussed. Let **Plane spacing = 0.23333333 nm**. From the implemented expression `(360/Math.PI)*Math.asin(0.15406/(2*d))`, the predicted value is **38.5531589 degrees 2θ**. Change only the designated control to **0.25777778 nm** and the result becomes **34.7738801 degrees 2θ**. In this controlled comparison the predicted quantity falls; the finite-difference sensitivity is **-154.606859 (degrees 2θ)/(nm)**. This numerical result is deterministic, derived directly from the stated formula, and is *not* an observation of an actual sample. The two values illustrate what that formula encodes; they do not prove the material will behave this way.

The complete assumptions are: **First order m=1; monochromatic Cu Kα-like λ=0.15406 nm; perfect geometric diffraction, no refraction or instrument zero**. Before interpreting the slope, check that the denominator of the expression cannot vanish in the slider range and that the output is in the declared units. A synthetic curve is not a scientific uncertainty band: there are no replicate wafers, measurement errors or competing mechanisms in this dataset. The correct conclusion is conditional—*if the stated assumptions hold, changing the input produces the computed result*. Any statement about a real device needs experimental comparison and fit diagnostics.

### Measurement plan and what the model can miss

Thin films may be textured and strained; a bulk powder pattern or single peak is insufficient to establish complete phase purity.

Begin with **Hall and four-terminal transport**; record **field reversal, thickness, current level, temperature, and contact geometry** and independently compare against **infrared absorption or carrier-resolved optical probe**. Because the original measurement and the independent technique interrogate different aspects of a sample, agreement strengthens a claim, while disagreement can locate the missing effect. A structural analysis might average over a large volume while an electrical test disproportionately samples a thin channel. Temperature-dependent optical data can distinguish activation from transport in some settings, but only if spectral calibration and carrier injection are independently controlled.

Perform a **thermodynamic regime audit**: Identify whether equilibrium, degenerate statistics, hot carriers, low injection, or finite-bias gradients alter validity. Follow with a **instrument de-embedding audit**: Check contact resistance, substrate channels, parasitic capacitance, optical reflection and thermal offsets. State which quantity is known from calibration, which is inferred from a model, and which remains unknown. When the largest plausible uncertainty is in an unmeasured constant rather than in instrumental precision, a highly precise displayed number is misleading. Develop a repeatable sample ID and uncertainty budget rather than inventing error bars to make a synthetic demonstration look experimental.

### Experimental counterfactual

The leading interpretation connects **long-range order, alloy chemistry and crystalline defects** with a response in **diamond, zinc blende, and wurtzite lattices**. Now suppose instead that the change is controlled by **instrument angle offset, relaxation or compositional gradients**. Both mechanisms could sometimes reproduce a monotonic trend in the single-variable calculator. A useful counterfactual is to change a second condition that affects one mechanism more strongly than the other—temperature, optical excitation depth, contact geometry, wafer thickness, crystal orientation or measurement frequency—while leaving the primary comparison matched. Explain how **high-resolution reciprocal-space mapping and calibrated chemical profiling** would be expected to discriminate the two models, and report in advance which outcome would overturn the preferred explanation.

### Three graded problems

**Problem 1.2A — Conceptual mechanism.** Explain in your own words what **diamond, zinc blende, and wurtzite lattices** changes about the relation between **lattice geometry versus actual epitaxial strain**. State two different microphysical mechanisms that could produce the same measured sign of response. Identify a relevant energy, length or time scale and show why the difference would matter for interpretation.

**Problem 1.2B — Quantitative verification.** Reproduce the values **38.5531589 degrees 2θ** and **34.7738801 degrees 2θ** using `(360/Math.PI)*Math.asin(0.15406/(2*d))` at the two stated input values. Convert at least one related physical quantity to coherent SI units, report units in each algebraic step, and explain why increasing the model's input by the displayed amount makes the computed output falls. Which hidden material parameter could reverse a real-world trend?

**Problem 1.2C — Falsification and reporting.** Design a minimum independent experiment capable of distinguishing the current interpretation from **instrument angle offset, relaxation or compositional gradients**. Specify sampling locations, temperature, instrument calibration, measurement geometry, between-sample replication, and an observable that would force you to reject the interpretation. Name one specific circumstance in which **Bragg diffraction angle** should not be treated as predictive.

## Lesson 1.3: Alloy composition and Vegard-type estimates

### A physical explanation before any numerical fit

A lattice parameter is often approximated as a composition-weighted interpolation, a(x)=xa_A+(1−x)a_B, for a substitutional alloy. This is a first screening approximation, not a guarantee of linearity or single-phase miscibility. Elastic bowing, ordering, point defects, and temperature can shift the actual lattice constants. Optical gaps can exhibit stronger bowing than lattice parameter; a standard schematic interpolation is Eg(x)=xEgA+(1−x)EgB−b x(1−x), where the bowing parameter b is empirical. Never infer band gap from lattice constant alone.

**Primary relationship:** Report alloy composition x, lattice parameter a, bowing assumption, uncertainty, and phase evidence. The first task is to decide whether it is a structural geometric relation, a balance law, a statistical approximation or an experimentally calibrated response. This matters specifically for **alloy composition and vegard-type estimates**, because the same calculated number can emerge from physically incompatible material states. Explicitly note which band, lattice, impurity, contact or interface degrees of freedom the expression leaves out. A clear statement of validity is often more useful than giving the output to five decimal places.

For a hypothetical alloy between lattice parameters 5.43 and 5.65 Å, compute an interpolated lattice constant at x=0.3, then ask whether the alloy actually remains a solid solution. Record relaxation before comparing with an epitaxial substrate.

### Transparent worked numerical example

The offline calculator **Epitaxial lattice mismatch** is deliberately simpler than the phenomenon being discussed. Let **Relaxed film lattice parameter = 5.4955556 angstrom**. From the implemented expression `100*(af-5.431)/5.431`, the predicted value is **1.18864952 %**. Change only the designated control to **5.5244444 angstrom** and the result becomes **1.7205753 %**. In this controlled comparison the predicted quantity rises; the finite-difference sensitivity is **18.4128153 (%)/(angstrom)**. This numerical result is deterministic, derived directly from the stated formula, and is *not* an observation of an actual sample. The two values illustrate what that formula encodes; they do not prove the material will behave this way.

### Measurement plan and what the model can miss

Real alloy parameters and their temperature and composition dependence must be measured for each system; mixing unstable phases invalidates interpolation.

Begin with **capacitance–voltage analysis**; record **small-signal frequency, applied bias, area, sweep direction, and parasitic capacitance** and independently compare against **secondary-ion mass spectrometry and deep-level transients**. Because the original measurement and the independent technique interrogate different aspects of a sample, agreement strengthens a claim, while disagreement can locate the missing effect. A structural analysis might average over a large volume while an electrical test disproportionately samples a thin channel. Temperature-dependent optical data can distinguish activation from transport in some settings, but only if spectral calibration and carrier injection are independently controlled.

Perform a **geometry and dimensionality audit**: Distinguish three-dimensional volume density from two-dimensional sheet density and separate area from length. Follow with a **charge neutrality audit**: Verify the sign and physical units of electrons, holes, ionized donors and acceptors; document compensation. State which quantity is known from calibration, which is inferred from a model, and which remains unknown. When the largest plausible uncertainty is in an unmeasured constant rather than in instrumental precision, a highly precise displayed number is misleading. Develop a repeatable sample ID and uncertainty budget rather than inventing error bars to make a synthetic demonstration look experimental.

### Experimental counterfactual

The leading interpretation connects **long-range order, alloy chemistry and crystalline defects** with a response in **alloy composition and vegard-type estimates**. Now suppose instead that the change is controlled by **instrument angle offset, relaxation or compositional gradients**. Both mechanisms could sometimes reproduce a monotonic trend in the single-variable calculator. A useful counterfactual is to change a second condition that affects one mechanism more strongly than the other—temperature, optical excitation depth, contact geometry, wafer thickness, crystal orientation or measurement frequency—while leaving the primary comparison matched. Explain how **high-resolution reciprocal-space mapping and calibrated chemical profiling** would be expected to discriminate the two models, and report in advance which outcome would overturn the preferred explanation.

### Three graded problems

**Problem 1.3A — Conceptual mechanism.** Explain in your own words what **alloy composition and vegard-type estimates** changes about the relation between **lattice geometry versus actual epitaxial strain**. State two different microphysical mechanisms that could produce the same measured sign of response. Identify a relevant energy, length or time scale and show why the difference would matter for interpretation.

**Problem 1.3B — Quantitative verification.** Reproduce the values **1.18864952 %** and **1.7205753 %** using `100*(af-5.431)/5.431` at the two stated input values. Convert at least one related physical quantity to coherent SI units, report units in each algebraic step, and explain why increasing the model's input by the displayed amount makes the computed output rises. Which hidden material parameter could reverse a real-world trend?

**Problem 1.3C — Falsification and reporting.** Design a minimum independent experiment capable of distinguishing the current interpretation from **instrument angle offset, relaxation or compositional gradients**. Specify sampling locations, temperature, instrument calibration, measurement geometry, between-sample replication, and an observable that would force you to reject the interpretation. Name one specific circumstance in which **Epitaxial lattice mismatch** should not be treated as predictive.

## Lesson 1.4: Strain and epitaxial mismatch

### A physical explanation before any numerical fit

For pseudomorphic thin films, the film adopts the substrate in-plane lattice spacing, producing biaxial strain that modifies electronic bands and can generate a compensating out-of-plane response. A common mismatch convention is f=(a_f−a_s)/a_s. Signs matter: positive relaxed-film mismatch typically means in-plane compression if coherent with a smaller substrate. Beyond a thickness affected by dislocation energetics and growth details, partial relaxation can begin. Coherence should be tested rather than asserted from nominal film thickness alone.

**Primary relationship:** Mismatch percent equals 100(a_f−a_s)/a_s using the same temperature and lattice orientation. The first task is to decide whether it is a structural geometric relation, a balance law, a statistical approximation or an experimentally calibrated response. This matters specifically for **strain and epitaxial mismatch**, because the same calculated number can emerge from physically incompatible material states. Explicitly note which band, lattice, impurity, contact or interface degrees of freedom the expression leaves out. A clear statement of validity is often more useful than giving the output to five decimal places.

An epitaxial film with a relaxed in-plane lattice constant 5.50 Å grows on a 5.431 Å substrate. Compute mismatch magnitude and compare high-resolution reciprocal-space maps before and after annealing to distinguish coherent strain and relaxation.

### Transparent worked numerical example

The offline calculator **Bragg diffraction angle** is deliberately simpler than the phenomenon being discussed. Let **Plane spacing = 0.28222222 nm**. From the implemented expression `(360/Math.PI)*Math.asin(0.15406/(2*d))`, the predicted value is **31.6786909 degrees 2θ**. Change only the designated control to **0.30666667 nm** and the result becomes **29.0952652 degrees 2θ**. In this controlled comparison the predicted quantity falls; the finite-difference sensitivity is **-105.685596 (degrees 2θ)/(nm)**. This numerical result is deterministic, derived directly from the stated formula, and is *not* an observation of an actual sample. The two values illustrate what that formula encodes; they do not prove the material will behave this way.

### Measurement plan and what the model can miss

Critical-thickness formulas depend on dislocation geometry and kinetics, and a single numerical cutoff cannot certify a particular wafer.

Begin with **photoluminescence and time-resolved optics**; record **pump spectrum, pulse fluence, collection calibration, temperature, and optical lifetime window** and independently compare against **microwave photoconductance decay or thickness series**. Because the original measurement and the independent technique interrogate different aspects of a sample, agreement strengthens a claim, while disagreement can locate the missing effect. A structural analysis might average over a large volume while an electrical test disproportionately samples a thin channel. Temperature-dependent optical data can distinguish activation from transport in some settings, but only if spectral calibration and carrier injection are independently controlled.

Perform a **instrument de-embedding audit**: Check contact resistance, substrate channels, parasitic capacitance, optical reflection and thermal offsets. Follow with a **geometry and dimensionality audit**: Distinguish three-dimensional volume density from two-dimensional sheet density and separate area from length. State which quantity is known from calibration, which is inferred from a model, and which remains unknown. When the largest plausible uncertainty is in an unmeasured constant rather than in instrumental precision, a highly precise displayed number is misleading. Develop a repeatable sample ID and uncertainty budget rather than inventing error bars to make a synthetic demonstration look experimental.

### Experimental counterfactual

The leading interpretation connects **long-range order, alloy chemistry and crystalline defects** with a response in **strain and epitaxial mismatch**. Now suppose instead that the change is controlled by **instrument angle offset, relaxation or compositional gradients**. Both mechanisms could sometimes reproduce a monotonic trend in the single-variable calculator. A useful counterfactual is to change a second condition that affects one mechanism more strongly than the other—temperature, optical excitation depth, contact geometry, wafer thickness, crystal orientation or measurement frequency—while leaving the primary comparison matched. Explain how **high-resolution reciprocal-space mapping and calibrated chemical profiling** would be expected to discriminate the two models, and report in advance which outcome would overturn the preferred explanation.

### Three graded problems

**Problem 1.4A — Conceptual mechanism.** Explain in your own words what **strain and epitaxial mismatch** changes about the relation between **lattice geometry versus actual epitaxial strain**. State two different microphysical mechanisms that could produce the same measured sign of response. Identify a relevant energy, length or time scale and show why the difference would matter for interpretation.

**Problem 1.4B — Quantitative verification.** Reproduce the values **31.6786909 degrees 2θ** and **29.0952652 degrees 2θ** using `(360/Math.PI)*Math.asin(0.15406/(2*d))` at the two stated input values. Convert at least one related physical quantity to coherent SI units, report units in each algebraic step, and explain why increasing the model's input by the displayed amount makes the computed output falls. Which hidden material parameter could reverse a real-world trend?

**Problem 1.4C — Falsification and reporting.** Design a minimum independent experiment capable of distinguishing the current interpretation from **instrument angle offset, relaxation or compositional gradients**. Specify sampling locations, temperature, instrument calibration, measurement geometry, between-sample replication, and an observable that would force you to reject the interpretation. Name one specific circumstance in which **Bragg diffraction angle** should not be treated as predictive.

<!-- MODEL_1 -->

## Lesson 1.5: Real microstructures: grains, dislocations, and stacking faults

### A physical explanation before any numerical fit

Polycrystalline semiconductors combine grains with boundaries that can host dangling bonds, segregated dopants, charged traps, and enhanced diffusion paths. Threading dislocations in epitaxial films can cause nonradiative recombination and leakage, but electrical impact depends on core structure and decoration, not simply defect count. Stacking faults alter local layer sequence and sometimes electronic confinement. Characterization must distinguish structural defect density from electrically active trap density and must specify area and length units.

**Primary relationship:** A structural defect is electrically harmful only through a demonstrated coupling to relevant states or transport pathways. The first task is to decide whether it is a structural geometric relation, a balance law, a statistical approximation or an experimentally calibrated response. This matters specifically for **real microstructures: grains, dislocations, and stacking faults**, because the same calculated number can emerge from physically incompatible material states. Explicitly note which band, lattice, impurity, contact or interface degrees of freedom the expression leaves out. A clear statement of validity is often more useful than giving the output to five decimal places.

Two wafers have similar X-ray diffraction peak widths yet different LED efficiency. Compare defect-resolved cathodoluminescence maps and temperature-dependent luminescence. Peak width alone cannot establish the recombination mechanism.

### Transparent worked numerical example

The offline calculator **Epitaxial lattice mismatch** is deliberately simpler than the phenomenon being discussed. Let **Relaxed film lattice parameter = 5.5533333 angstrom**. From the implemented expression `100*(af-5.431)/5.431`, the predicted value is **2.25250107 %**. Change only the designated control to **5.5822222 angstrom** and the result becomes **2.78442685 %**. In this controlled comparison the predicted quantity rises; the finite-difference sensitivity is **18.4128153 (%)/(angstrom)**. This numerical result is deterministic, derived directly from the stated formula, and is *not* an observation of an actual sample. The two values illustrate what that formula encodes; they do not prove the material will behave this way.

### Measurement plan and what the model can miss

Many defects are invisible to one tool; surface-sensitive images need correlation with buried structure and devices.

Begin with **electrical test structures**; record **contact mask layout, current compliance, voltage sweep, environmental stability, and repeatability** and independently compare against **four-point probe and transmission line method**. Because the original measurement and the independent technique interrogate different aspects of a sample, agreement strengthens a claim, while disagreement can locate the missing effect. A structural analysis might average over a large volume while an electrical test disproportionately samples a thin channel. Temperature-dependent optical data can distinguish activation from transport in some settings, but only if spectral calibration and carrier injection are independently controlled.

Perform a **statistical independence audit**: Distinguish repeated scans of a single wafer from independent process lots and predeclare rejection criteria. Follow with a **statistical independence audit**: Distinguish repeated scans of a single wafer from independent process lots and predeclare rejection criteria. State which quantity is known from calibration, which is inferred from a model, and which remains unknown. When the largest plausible uncertainty is in an unmeasured constant rather than in instrumental precision, a highly precise displayed number is misleading. Develop a repeatable sample ID and uncertainty budget rather than inventing error bars to make a synthetic demonstration look experimental.

### Experimental counterfactual

The leading interpretation connects **long-range order, alloy chemistry and crystalline defects** with a response in **real microstructures: grains, dislocations, and stacking faults**. Now suppose instead that the change is controlled by **instrument angle offset, relaxation or compositional gradients**. Both mechanisms could sometimes reproduce a monotonic trend in the single-variable calculator. A useful counterfactual is to change a second condition that affects one mechanism more strongly than the other—temperature, optical excitation depth, contact geometry, wafer thickness, crystal orientation or measurement frequency—while leaving the primary comparison matched. Explain how **high-resolution reciprocal-space mapping and calibrated chemical profiling** would be expected to discriminate the two models, and report in advance which outcome would overturn the preferred explanation.

### Three graded problems

**Problem 1.5A — Conceptual mechanism.** Explain in your own words what **real microstructures: grains, dislocations, and stacking faults** changes about the relation between **lattice geometry versus actual epitaxial strain**. State two different microphysical mechanisms that could produce the same measured sign of response. Identify a relevant energy, length or time scale and show why the difference would matter for interpretation.

**Problem 1.5B — Quantitative verification.** Reproduce the values **2.25250107 %** and **2.78442685 %** using `100*(af-5.431)/5.431` at the two stated input values. Convert at least one related physical quantity to coherent SI units, report units in each algebraic step, and explain why increasing the model's input by the displayed amount makes the computed output rises. Which hidden material parameter could reverse a real-world trend?

**Problem 1.5C — Falsification and reporting.** Design a minimum independent experiment capable of distinguishing the current interpretation from **instrument angle offset, relaxation or compositional gradients**. Specify sampling locations, temperature, instrument calibration, measurement geometry, between-sample replication, and an observable that would force you to reject the interpretation. Name one specific circumstance in which **Epitaxial lattice mismatch** should not be treated as predictive.

## Integrated case study: Selecting an epitaxial substrate

### Problem statement and evidence hierarchy

A research group must choose between lattice match and growth compatibility for a new optoelectronic structure. Treat the problem as a comparison of several causes, not a request to select one formula. First write down what was controlled and directly measured; separate that from what is an inference about **long-range order, alloy chemistry and crystalline defects**. Material recipes, deposition logs and temperature setpoints should not be substituted for actual measured carrier concentrations, layer thicknesses, microstructural maps or local junction responses. In high-stakes applications, state what level of evidence would be sufficient before committing design resources or fabrication capacity.

### Linked calculations and missing-variable audit

Build a table with thermal expansion, dislocation density, interface quality, thermal management, and substrate supply; calculate lattice mismatch while fixing measurement temperature. Work both interactive models for the unit, first at their default conditions and then after changing one input by 10% within slider bounds. Recalculate one output manually and compare it to a second independent program or calculator. The two formulas address different features of the material, so their combination is not automatically a multi-physics simulation. Build a box-and-arrow account of how processing influences structure, carrier populations, electrical or optical response and eventual device performance. Label any link that is still only hypothetical.

Evaluate a dimensionless or normalized sensitivity, Δy/y relative to Δx/x, when mathematically meaningful. For a relation dominated by an exponential, check whether a small uncertainty in absolute temperature or activation energy overwhelms instrumental precision. For a geometrical relation, check whether an unresolved orientation or film thickness changes the result. For a circuit-response relation, ask whether equivalent series resistance, contact injection or measurement frequency should enter the expression. Do not aggregate these into an invented confidence interval; describe the unmodeled terms explicitly.

### Experimental discrimination and judgment

Collect reciprocal-space maps, microscopy, and wavelength-resolved emission on independent wafers before rank ordering substrates. Distinguish a paired repeat on the same device from an independently fabricated replicate; predeclare what discrepancy requires reassessment. Preserve raw observations, geometry, uncertainties and model configurations. A credible conclusion identifies an observation that a rival explanation could not produce under the same controls. **Warning:** Best band gap does not imply best growable device. Report evidence status separately as demonstrated, provisional, or not yet assessed. The cost of overclaiming a semiconductor property rises sharply when it becomes a process-selection or field-reliability decision.

### Five cumulative university examination prompts

1. Draw an atomistic-to-device diagram for **long-range order, alloy chemistry and crystalline defects**, with a label on each directly measured or assumed arrow.
2. Compare **lattice geometry versus actual epitaxial strain** and state the governing assumptions and units for one calculation.
3. Recompute one unit model in two independent ways and perform one limiting-case or monotonicity check.
4. Formulate a rival explanation using **instrument angle offset, relaxation or compositional gradients** and specify the result of **high-resolution reciprocal-space mapping and calibrated chemical profiling** that would distinguish it.
5. Deliver a one-page technical decision note that separates known facts, conditional calculations, uncertainty and additional qualification before scale-up.

