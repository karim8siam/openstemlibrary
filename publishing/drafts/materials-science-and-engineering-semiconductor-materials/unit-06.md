# Unit 6: Heterostructures, thin films, and dielectric interfaces

**Central research question:** What changes when semiconductor properties depend on confinement, strain, or an interface only nanometers thick?

## Material and device context

The last few nanometers of an electronic material can dominate its behavior through confinement, interface charge, roughness and chemistry. Equivalent oxide thickness and physical thickness measure different things.

A channel carrier sheet density is not a bulk dopant concentration. Mixing cm−2 and cm−3 is a dimensional error, not a harmless reporting choice.

**Scope of this unit:** Study **quantum confinement and dielectric interface response** while distinguishing **ideal geometric capacitance versus electrically active interface charge**. Practical interpretation requires **layer thickness, interface composition, 2D sheet density and bias**. An important alternative is **parallel channels, fixed oxide charge or interface trapping**, which is why **frequency-dependent MOS conductance and gated Hall measurements** must be part of a credible validation programme. These topics are inseparable from geometry, scale and specimen history; a nominal textbook material is not a sufficiently specified industrial sample.

## Measurement-first reading checkpoint

## Lesson 6.1: Quantum wells and confinement energy

### A physical explanation before any numerical fit

When carrier motion is constrained to a thin region, subband energies become discrete in the confined direction. In the infinite-square-well approximation, levels scale as n²/(m*L²), demonstrating why thinner wells tend to increase confinement energies. Real heterostructures require finite barriers, strain, effective-mass discontinuities, polarization, and band offsets. An optical peak shift may arise from many-body effects, built-in fields, alloy fluctuations, or interface roughness rather than well thickness alone.

**Primary relationship:** A confined-state estimate is useful only with explicit effective mass, barrier, and dimensionality assumptions. The first task is to decide whether it is a structural geometric relation, a balance law, a statistical approximation or an experimentally calibrated response. This matters specifically for **quantum wells and confinement energy**, because the same calculated number can emerge from physically incompatible material states. Explicitly note which band, lattice, impurity, contact or interface degrees of freedom the expression leaves out. A clear statement of validity is often more useful than giving the output to five decimal places.

Compare nominally identical quantum wells of 5 nm and 8 nm width; predict direction of transition-energy shift while holding alloy composition and strain constant. Check thickness with transmission electron microscopy and offsets with spectroscopy.

For a realistic assessment, distinguish directly controlled inputs from inferred ones. In this lesson, the relevant controls include **layer thickness, interface composition, 2D sheet density and bias**; measure each where possible and report the resolution or calibration of the instrument. A model fit that adjusts an unmeasured constant to match one observable does not establish that the associated mechanism is correct. Ask whether **parallel channels, fixed oxide charge or interface trapping** could produce the same sign of change and what independent feature would differ. If the two proposed mechanisms are observationally indistinguishable under the existing design, the next scientific contribution is a better experiment rather than a more elaborate fit.

### Transparent worked numerical example

The offline calculator **Geometric SiO2 capacitance per area** is deliberately simpler than the phenomenon being discussed. Let **Dielectric thickness = 8.2222222 nm**. From the implemented expression `(3.9*8.8541878128e-14/(t*1e-7))*1e6`, the predicted value is **0.419975665 microF/cm2**. Change only the designated control to **11.333333 nm** and the result becomes **0.304688228 microF/cm2**. In this controlled comparison the predicted quantity falls; the finite-difference sensitivity is **-0.0370566763 (microF/cm2)/(nm)**. This numerical result is deterministic, derived directly from the stated formula, and is *not* an observation of an actual sample. The two values illustrate what that formula encodes; they do not prove the material will behave this way.

The complete assumptions are: **Relative permittivity 3.9; planar uniform oxide, no quantum capacitance, leakage, interface layer or fringe**. Before interpreting the slope, check that the denominator of the expression cannot vanish in the slider range and that the output is in the declared units. A synthetic curve is not a scientific uncertainty band: there are no replicate wafers, measurement errors or competing mechanisms in this dataset. The correct conclusion is conditional—*if the stated assumptions hold, changing the input produces the computed result*. Any statement about a real device needs experimental comparison and fit diagnostics.

### Measurement plan and what the model can miss

A particle-in-a-box prediction should not be treated as a device emission wavelength when excitons and interface fields are significant.

### Experimental counterfactual

The leading interpretation connects **quantum confinement and dielectric interface response** with a response in **quantum wells and confinement energy**. Now suppose instead that the change is controlled by **parallel channels, fixed oxide charge or interface trapping**. Both mechanisms could sometimes reproduce a monotonic trend in the single-variable calculator. A useful counterfactual is to change a second condition that affects one mechanism more strongly than the other—temperature, optical excitation depth, contact geometry, wafer thickness, crystal orientation or measurement frequency—while leaving the primary comparison matched. Explain how **frequency-dependent MOS conductance and gated Hall measurements** would be expected to discriminate the two models, and report in advance which outcome would overturn the preferred explanation.

### Three graded problems

**Problem 6.1A — Conceptual mechanism.** Explain in your own words what **quantum wells and confinement energy** changes about the relation between **ideal geometric capacitance versus electrically active interface charge**. State two different microphysical mechanisms that could produce the same measured sign of response. Identify a relevant energy, length or time scale and show why the difference would matter for interpretation.

**Problem 6.1B — Quantitative verification.** Reproduce the values **0.419975665 microF/cm2** and **0.304688228 microF/cm2** using `(3.9*8.8541878128e-14/(t*1e-7))*1e6` at the two stated input values. Convert at least one related physical quantity to coherent SI units, report units in each algebraic step, and explain why increasing the model's input by the displayed amount makes the computed output falls. Which hidden material parameter could reverse a real-world trend?

**Problem 6.1C — Falsification and reporting.** Design a minimum independent experiment capable of distinguishing the current interpretation from **parallel channels, fixed oxide charge or interface trapping**. Specify sampling locations, temperature, instrument calibration, measurement geometry, between-sample replication, and an observable that would force you to reject the interpretation. Name one specific circumstance in which **Geometric SiO2 capacitance per area** should not be treated as predictive.

<!-- MODEL_10 -->

## Lesson 6.2: Heteroepitaxy and strain relaxation

### A physical explanation before any numerical fit

Heterostructures combine materials with different lattice constants, thermal expansion, chemistry, and band edges. Coherent strain can improve electronic performance but stores elastic energy; relaxation introduces misfit dislocations that may thread into active layers. Composition grading can spread strain and reduce particular defect pathways at the expense of processing complexity and thickness. Growth morphology depends on surface kinetics as well as thermodynamic driving force.

**Primary relationship:** A functional heterointerface must be assessed through structure, electrical quality, and thermomechanical stability. The first task is to decide whether it is a structural geometric relation, a balance law, a statistical approximation or an experimentally calibrated response. This matters specifically for **heteroepitaxy and strain relaxation**, because the same calculated number can emerge from physically incompatible material states. Explicitly note which band, lattice, impurity, contact or interface degrees of freedom the expression leaves out. A clear statement of validity is often more useful than giving the output to five decimal places.

Map in-plane and out-of-plane lattice parameters of a graded epitaxial buffer. Compare reciprocal-space mapping with cross-sectional microscopy before declaring relaxation complete and defect density acceptable.

### Transparent worked numerical example

The offline calculator **Two-dimensional sheet resistance** is deliberately simpler than the phenomenon being discussed. Let **Sheet electron density = 3.4e+12 cm^-2**. From the implemented expression `1/(1.602176634e-19*ns*500)`, the predicted value is **3671.47593 ohm/square**. Change only the designated control to **4.5e+12 cm^-2** and the result becomes **2774.00403 ohm/square**. In this controlled comparison the predicted quantity falls; the finite-difference sensitivity is **-8.15883539e-10 (ohm/square)/(cm^-2)**. This numerical result is deterministic, derived directly from the stated formula, and is *not* an observation of an actual sample. The two values illustrate what that formula encodes; they do not prove the material will behave this way.

The complete assumptions are: **One electron layer, μ=500 cm2/(V s), simple weak-field Drude response; no parallel channels, contacts or localization**. Before interpreting the slope, check that the denominator of the expression cannot vanish in the slider range and that the output is in the declared units. A synthetic curve is not a scientific uncertainty band: there are no replicate wafers, measurement errors or competing mechanisms in this dataset. The correct conclusion is conditional—*if the stated assumptions hold, changing the input produces the computed result*. Any statement about a real device needs experimental comparison and fit diagnostics.

### Measurement plan and what the model can miss

Thin-film stress inferred from wafer curvature is an average and cannot by itself locate individual threading dislocations.

### Experimental counterfactual

The leading interpretation connects **quantum confinement and dielectric interface response** with a response in **heteroepitaxy and strain relaxation**. Now suppose instead that the change is controlled by **parallel channels, fixed oxide charge or interface trapping**. Both mechanisms could sometimes reproduce a monotonic trend in the single-variable calculator. A useful counterfactual is to change a second condition that affects one mechanism more strongly than the other—temperature, optical excitation depth, contact geometry, wafer thickness, crystal orientation or measurement frequency—while leaving the primary comparison matched. Explain how **frequency-dependent MOS conductance and gated Hall measurements** would be expected to discriminate the two models, and report in advance which outcome would overturn the preferred explanation.

### Three graded problems

**Problem 6.2A — Conceptual mechanism.** Explain in your own words what **heteroepitaxy and strain relaxation** changes about the relation between **ideal geometric capacitance versus electrically active interface charge**. State two different microphysical mechanisms that could produce the same measured sign of response. Identify a relevant energy, length or time scale and show why the difference would matter for interpretation.

**Problem 6.2B — Quantitative verification.** Reproduce the values **3671.47593 ohm/square** and **2774.00403 ohm/square** using `1/(1.602176634e-19*ns*500)` at the two stated input values. Convert at least one related physical quantity to coherent SI units, report units in each algebraic step, and explain why increasing the model's input by the displayed amount makes the computed output falls. Which hidden material parameter could reverse a real-world trend?

**Problem 6.2C — Falsification and reporting.** Design a minimum independent experiment capable of distinguishing the current interpretation from **parallel channels, fixed oxide charge or interface trapping**. Specify sampling locations, temperature, instrument calibration, measurement geometry, between-sample replication, and an observable that would force you to reject the interpretation. Name one specific circumstance in which **Two-dimensional sheet resistance** should not be treated as predictive.

## Lesson 6.3: Gate oxides and oxide capacitance

### A physical explanation before any numerical fit

For a uniform dielectric slab, geometric capacitance per area Cox=εox/tox. The electric field and insulator reliability do not follow from capacitance alone: fixed charge, interface states, mobile ions, leakage, breakdown statistics, and interfacial layers matter. Equivalent oxide thickness expresses capacitance relative to a specified SiO2 dielectric constant, not physical thickness of high-k material. As oxide thickness approaches nanometers, quantum capacitance and inversion-layer centroid effects can change total measured capacitance.

**Primary relationship:** Cox/A=εox/tox with consistent length units and explicitly defined effective dielectric constant. The first task is to decide whether it is a structural geometric relation, a balance law, a statistical approximation or an experimentally calibrated response. This matters specifically for **gate oxides and oxide capacitance**, because the same calculated number can emerge from physically incompatible material states. Explicitly note which band, lattice, impurity, contact or interface degrees of freedom the expression leaves out. A clear statement of validity is often more useful than giving the output to five decimal places.

Compute ideal SiO2 capacitance per area at 5 nm, then at 2 nm. Discuss why observed capacitance does not scale exactly inversely with thickness if interface layers or quantum effects contribute.

### Transparent worked numerical example

The offline calculator **Geometric SiO2 capacitance per area** is deliberately simpler than the phenomenon being discussed. Let **Dielectric thickness = 14.444444 nm**. From the implemented expression `(3.9*8.8541878128e-14/(t*1e-7))*1e6`, the predicted value is **0.239063071 microF/cm2**. Change only the designated control to **17.555556 nm** and the result becomes **0.196697463 microF/cm2**. In this controlled comparison the predicted quantity falls; the finite-difference sensitivity is **-0.0136175167 (microF/cm2)/(nm)**. This numerical result is deterministic, derived directly from the stated formula, and is *not* an observation of an actual sample. The two values illustrate what that formula encodes; they do not prove the material will behave this way.

### Measurement plan and what the model can miss

The parallel-plate approximation omits fringe fields, roughness, nonuniform permittivity, and gate leakage.

### Experimental counterfactual

The leading interpretation connects **quantum confinement and dielectric interface response** with a response in **gate oxides and oxide capacitance**. Now suppose instead that the change is controlled by **parallel channels, fixed oxide charge or interface trapping**. Both mechanisms could sometimes reproduce a monotonic trend in the single-variable calculator. A useful counterfactual is to change a second condition that affects one mechanism more strongly than the other—temperature, optical excitation depth, contact geometry, wafer thickness, crystal orientation or measurement frequency—while leaving the primary comparison matched. Explain how **frequency-dependent MOS conductance and gated Hall measurements** would be expected to discriminate the two models, and report in advance which outcome would overturn the preferred explanation.

### Three graded problems

**Problem 6.3A — Conceptual mechanism.** Explain in your own words what **gate oxides and oxide capacitance** changes about the relation between **ideal geometric capacitance versus electrically active interface charge**. State two different microphysical mechanisms that could produce the same measured sign of response. Identify a relevant energy, length or time scale and show why the difference would matter for interpretation.

**Problem 6.3B — Quantitative verification.** Reproduce the values **0.239063071 microF/cm2** and **0.196697463 microF/cm2** using `(3.9*8.8541878128e-14/(t*1e-7))*1e6` at the two stated input values. Convert at least one related physical quantity to coherent SI units, report units in each algebraic step, and explain why increasing the model's input by the displayed amount makes the computed output falls. Which hidden material parameter could reverse a real-world trend?

**Problem 6.3C — Falsification and reporting.** Design a minimum independent experiment capable of distinguishing the current interpretation from **parallel channels, fixed oxide charge or interface trapping**. Specify sampling locations, temperature, instrument calibration, measurement geometry, between-sample replication, and an observable that would force you to reject the interpretation. Name one specific circumstance in which **Geometric SiO2 capacitance per area** should not be treated as predictive.

## Lesson 6.4: Interface traps and electronic passivation

### A physical explanation before any numerical fit

Interface defects can exchange charge with semiconductor bands, influencing threshold voltage, subthreshold swing, mobility, generation current, and hysteresis. Surface states depend on oxide growth, surface preparation, impurity contamination, and measurement frequency. A flat-band shift can arise from fixed oxide charge or work-function difference as well as interface traps. Post-deposition anneals can improve one interface metric while degrading another such as diffusion-barrier integrity.

**Primary relationship:** Quote interface-trap density with units per area per energy and include the measurement frequency and temperature. The first task is to decide whether it is a structural geometric relation, a balance law, a statistical approximation or an experimentally calibrated response. This matters specifically for **interface traps and electronic passivation**, because the same calculated number can emerge from physically incompatible material states. Explicitly note which band, lattice, impurity, contact or interface degrees of freedom the expression leaves out. A clear statement of validity is often more useful than giving the output to five decimal places.

A MOS capacitor shows strong frequency dispersion and hysteresis. Compare high- and low-frequency C–V, conductance methods, and bias-stress tests before extracting trap density.

### Transparent worked numerical example

The offline calculator **Two-dimensional sheet resistance** is deliberately simpler than the phenomenon being discussed. Let **Sheet electron density = 5.6e+12 cm^-2**. From the implemented expression `1/(1.602176634e-19*ns*500)`, the predicted value is **2229.11038 ohm/square**. Change only the designated control to **6.7e+12 cm^-2** and the result becomes **1863.13704 ohm/square**. In this controlled comparison the predicted quantity falls; the finite-difference sensitivity is **-3.32703042e-10 (ohm/square)/(cm^-2)**. This numerical result is deterministic, derived directly from the stated formula, and is *not* an observation of an actual sample. The two values illustrate what that formula encodes; they do not prove the material will behave this way.

### Measurement plan and what the model can miss

Trap distributions across energy and time constants cannot be reduced to one scalar without specifying extraction protocol.

### Experimental counterfactual

The leading interpretation connects **quantum confinement and dielectric interface response** with a response in **interface traps and electronic passivation**. Now suppose instead that the change is controlled by **parallel channels, fixed oxide charge or interface trapping**. Both mechanisms could sometimes reproduce a monotonic trend in the single-variable calculator. A useful counterfactual is to change a second condition that affects one mechanism more strongly than the other—temperature, optical excitation depth, contact geometry, wafer thickness, crystal orientation or measurement frequency—while leaving the primary comparison matched. Explain how **frequency-dependent MOS conductance and gated Hall measurements** would be expected to discriminate the two models, and report in advance which outcome would overturn the preferred explanation.

### Three graded problems

**Problem 6.4A — Conceptual mechanism.** Explain in your own words what **interface traps and electronic passivation** changes about the relation between **ideal geometric capacitance versus electrically active interface charge**. State two different microphysical mechanisms that could produce the same measured sign of response. Identify a relevant energy, length or time scale and show why the difference would matter for interpretation.

**Problem 6.4B — Quantitative verification.** Reproduce the values **2229.11038 ohm/square** and **1863.13704 ohm/square** using `1/(1.602176634e-19*ns*500)` at the two stated input values. Convert at least one related physical quantity to coherent SI units, report units in each algebraic step, and explain why increasing the model's input by the displayed amount makes the computed output falls. Which hidden material parameter could reverse a real-world trend?

**Problem 6.4C — Falsification and reporting.** Design a minimum independent experiment capable of distinguishing the current interpretation from **parallel channels, fixed oxide charge or interface trapping**. Specify sampling locations, temperature, instrument calibration, measurement geometry, between-sample replication, and an observable that would force you to reject the interpretation. Name one specific circumstance in which **Two-dimensional sheet resistance** should not be treated as predictive.

<!-- MODEL_11 -->

## Lesson 6.5: Two-dimensional gases and sheet resistance

### A physical explanation before any numerical fit

High-density carriers may be confined close to an interface, forming a two-dimensional electron or hole gas. Sheet density ns in cm⁻² differs from three-dimensional concentration in cm⁻³; sheet conductivity is q ns μ and sheet resistance is its inverse in Ω per square. Polarization, modulation doping, interface states, and charge transfer can contribute to carrier confinement. A larger sheet density does not guarantee higher mobility because remote-ionized scattering and interface disorder may increase.

**Primary relationship:** Rsheet=1/(q ns μ) only for a single dominant 2D carrier channel in the Drude approximation. The first task is to decide whether it is a structural geometric relation, a balance law, a statistical approximation or an experimentally calibrated response. This matters specifically for **two-dimensional gases and sheet resistance**, because the same calculated number can emerge from physically incompatible material states. Explicitly note which band, lattice, impurity, contact or interface degrees of freedom the expression leaves out. A clear statement of validity is often more useful than giving the output to five decimal places.

For ns=10^12 cm⁻² and μ=500 cm²/(V s), calculate sheet resistance. Then compare Hall-derived ns after gate bias changes; distinguish electrostatic charge accumulation from trap filling.

### Transparent worked numerical example

The offline calculator **Geometric SiO2 capacitance per area** is deliberately simpler than the phenomenon being discussed. Let **Dielectric thickness = 20.666667 nm**. From the implemented expression `(3.9*8.8541878128e-14/(t*1e-7))*1e6`, the predicted value is **0.167087093 microF/cm2**. Change only the designated control to **23.777778 nm** and the result becomes **0.14522523 microF/cm2**. In this controlled comparison the predicted quantity falls; the finite-difference sensitivity is **-0.00702702726 (microF/cm2)/(nm)**. This numerical result is deterministic, derived directly from the stated formula, and is *not* an observation of an actual sample. The two values illustrate what that formula encodes; they do not prove the material will behave this way.

### Measurement plan and what the model can miss

Current spreading near ohmic contacts and anisotropic conduction can make four-point sheet-resistance extraction geometry dependent.

### Experimental counterfactual

The leading interpretation connects **quantum confinement and dielectric interface response** with a response in **two-dimensional gases and sheet resistance**. Now suppose instead that the change is controlled by **parallel channels, fixed oxide charge or interface trapping**. Both mechanisms could sometimes reproduce a monotonic trend in the single-variable calculator. A useful counterfactual is to change a second condition that affects one mechanism more strongly than the other—temperature, optical excitation depth, contact geometry, wafer thickness, crystal orientation or measurement frequency—while leaving the primary comparison matched. Explain how **frequency-dependent MOS conductance and gated Hall measurements** would be expected to discriminate the two models, and report in advance which outcome would overturn the preferred explanation.

### Three graded problems

**Problem 6.5A — Conceptual mechanism.** Explain in your own words what **two-dimensional gases and sheet resistance** changes about the relation between **ideal geometric capacitance versus electrically active interface charge**. State two different microphysical mechanisms that could produce the same measured sign of response. Identify a relevant energy, length or time scale and show why the difference would matter for interpretation.

**Problem 6.5B — Quantitative verification.** Reproduce the values **0.167087093 microF/cm2** and **0.14522523 microF/cm2** using `(3.9*8.8541878128e-14/(t*1e-7))*1e6` at the two stated input values. Convert at least one related physical quantity to coherent SI units, report units in each algebraic step, and explain why increasing the model's input by the displayed amount makes the computed output falls. Which hidden material parameter could reverse a real-world trend?

**Problem 6.5C — Falsification and reporting.** Design a minimum independent experiment capable of distinguishing the current interpretation from **parallel channels, fixed oxide charge or interface trapping**. Specify sampling locations, temperature, instrument calibration, measurement geometry, between-sample replication, and an observable that would force you to reject the interpretation. Name one specific circumstance in which **Geometric SiO2 capacitance per area** should not be treated as predictive.

## Integrated case study: Evaluating a high-k interface

### Problem statement and evidence hierarchy

Two gate dielectrics have similar nominal equivalent oxide thickness but different low-frequency response. Treat the problem as a comparison of several causes, not a request to select one formula. First write down what was controlled and directly measured; separate that from what is an inference about **quantum confinement and dielectric interface response**. Material recipes, deposition logs and temperature setpoints should not be substituted for actual measured carrier concentrations, layer thicknesses, microstructural maps or local junction responses. In high-stakes applications, state what level of evidence would be sufficient before committing design resources or fabrication capacity.

### Linked calculations and missing-variable audit

Calculate ideal capacitance scaling and interface sheet resistance, then assess charge trapping, frequency dispersion, and interfacial layer thickness. Work both interactive models for the unit, first at their default conditions and then after changing one input by 10% within slider bounds. Recalculate one output manually and compare it to a second independent program or calculator. The two formulas address different features of the material, so their combination is not automatically a multi-physics simulation. Build a box-and-arrow account of how processing influences structure, carrier populations, electrical or optical response and eventual device performance. Label any link that is still only hypothetical.

### Experimental discrimination and judgment

Require measured C–V, conductance–frequency, gate leakage, mobility, and stress-stability at matched fields. Distinguish a paired repeat on the same device from an independently fabricated replicate; predeclare what discrepancy requires reassessment. Preserve raw observations, geometry, uncertainties and model configurations. A credible conclusion identifies an observation that a rival explanation could not produce under the same controls. **Warning:** Geometric capacitance is not full electrical performance or reliability. Report evidence status separately as demonstrated, provisional, or not yet assessed. The cost of overclaiming a semiconductor property rises sharply when it becomes a process-selection or field-reliability decision.

### Five cumulative university examination prompts

1. Draw an atomistic-to-device diagram for **quantum confinement and dielectric interface response**, with a label on each directly measured or assumed arrow.
2. Compare **ideal geometric capacitance versus electrically active interface charge** and state the governing assumptions and units for one calculation.
3. Recompute one unit model in two independent ways and perform one limiting-case or monotonicity check.
4. Formulate a rival explanation using **parallel channels, fixed oxide charge or interface trapping** and specify the result of **frequency-dependent MOS conductance and gated Hall measurements** that would distinguish it.
5. Deliver a one-page technical decision note that separates known facts, conditional calculations, uncertainty and additional qualification before scale-up.

