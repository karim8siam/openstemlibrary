# Unit 7: Optical properties, photocarriers, and defects

**Central research question:** How can illumination diagnose states, generate current, and expose recombination pathways?

## Material and device context

Optical experiments report the product of illumination, allowed excitation pathways, transport and extraction. A strong absorption coefficient is not a complete explanation for high photocurrent.

Spectroscopy and electrical measurements often resolve the same defect hypothesis from different angles, but spectral peaks and electrical transient activation energies are not unique atomic fingerprints.

**Scope of this unit:** Study **photon absorption and optically active defect states** while distinguishing **incident photon flux versus electrically collected carriers**. Practical interpretation requires **irradiance calibration, wavelength, sample thickness and surface reflectance**. An important alternative is **nonradiative recombination, trap tails or imperfect extraction**, which is why **spectrally calibrated EQE and excitation-dependent lifetime spectra** must be part of a credible validation programme. These topics are inseparable from geometry, scale and specimen history; a nominal textbook material is not a sufficiently specified industrial sample.

## Measurement-first reading checkpoint

## Lesson 7.1: Absorption edge and spectral response

### A physical explanation before any numerical fit

A photon may excite carriers across an allowed optical transition if its energy and transition selection rules permit it. Direct-gap absorption near the edge often rises more sharply than indirect-gap phonon-assisted absorption, but excitons, Urbach tails, free-carrier absorption, and defects complicate the picture. The absorption coefficient α has units inverse length, while transmittance depends on thickness, reflections, and interference. A drop in optical transmission is not automatically equivalent to band-to-band absorption.

**Primary relationship:** For no reflections and uniform α, absorbed fraction is 1−exp(−αd). The first task is to decide whether it is a structural geometric relation, a balance law, a statistical approximation or an experimentally calibrated response. This matters specifically for **absorption edge and spectral response**, because the same calculated number can emerge from physically incompatible material states. Explicitly note which band, lattice, impurity, contact or interface degrees of freedom the expression leaves out. A clear statement of validity is often more useful than giving the output to five decimal places.

Compare polished 100-µm and 500-µm semiconductor slices under matched wavelength. Use αd to estimate ideal absorbed fraction, then explain how surface reflectance and backside interference alter actual detector response.

For a realistic assessment, distinguish directly controlled inputs from inferred ones. In this lesson, the relevant controls include **irradiance calibration, wavelength, sample thickness and surface reflectance**; measure each where possible and report the resolution or calibration of the instrument. A model fit that adjusts an unmeasured constant to match one observable does not establish that the associated mechanism is correct. Ask whether **nonradiative recombination, trap tails or imperfect extraction** could produce the same sign of change and what independent feature would differ. If the two proposed mechanisms are observationally indistinguishable under the existing design, the next scientific contribution is a better experiment rather than a more elaborate fit.

### Transparent worked numerical example

The offline calculator **Beer–Lambert absorbed percentage** is deliberately simpler than the phenomenon being discussed. Let **Active-layer thickness = 4.5222222 micrometers**. From the implemented expression `100*(1-Math.exp(-1000*d*1e-4))`, the predicted value is **36.3787227 %**. Change only the designated control to **6.7333333 micrometers** and the result becomes **48.9994278 %**. In this controlled comparison the predicted quantity rises; the finite-difference sensitivity is **5.70785659 (%)/(micrometers)**. This numerical result is deterministic, derived directly from the stated formula, and is *not* an observation of an actual sample. The two values illustrate what that formula encodes; they do not prove the material will behave this way.

The complete assumptions are: **Single-pass α=1000 cm^-1, no surface reflection, spectral changes, scattering or interference**. Before interpreting the slope, check that the denominator of the expression cannot vanish in the slider range and that the output is in the declared units. A synthetic curve is not a scientific uncertainty band: there are no replicate wafers, measurement errors or competing mechanisms in this dataset. The correct conclusion is conditional—*if the stated assumptions hold, changing the input produces the computed result*. Any statement about a real device needs experimental comparison and fit diagnostics.

### Measurement plan and what the model can miss

Strongly scattering or textured films violate a simple one-pass Beer–Lambert optical path interpretation.

### Experimental counterfactual

The leading interpretation connects **photon absorption and optically active defect states** with a response in **absorption edge and spectral response**. Now suppose instead that the change is controlled by **nonradiative recombination, trap tails or imperfect extraction**. Both mechanisms could sometimes reproduce a monotonic trend in the single-variable calculator. A useful counterfactual is to change a second condition that affects one mechanism more strongly than the other—temperature, optical excitation depth, contact geometry, wafer thickness, crystal orientation or measurement frequency—while leaving the primary comparison matched. Explain how **spectrally calibrated EQE and excitation-dependent lifetime spectra** would be expected to discriminate the two models, and report in advance which outcome would overturn the preferred explanation.

### Three graded problems

**Problem 7.1A — Conceptual mechanism.** Explain in your own words what **absorption edge and spectral response** changes about the relation between **incident photon flux versus electrically collected carriers**. State two different microphysical mechanisms that could produce the same measured sign of response. Identify a relevant energy, length or time scale and show why the difference would matter for interpretation.

**Problem 7.1B — Quantitative verification.** Reproduce the values **36.3787227 %** and **48.9994278 %** using `100*(1-Math.exp(-1000*d*1e-4))` at the two stated input values. Convert at least one related physical quantity to coherent SI units, report units in each algebraic step, and explain why increasing the model's input by the displayed amount makes the computed output rises. Which hidden material parameter could reverse a real-world trend?

**Problem 7.1C — Falsification and reporting.** Design a minimum independent experiment capable of distinguishing the current interpretation from **nonradiative recombination, trap tails or imperfect extraction**. Specify sampling locations, temperature, instrument calibration, measurement geometry, between-sample replication, and an observable that would force you to reject the interpretation. Name one specific circumstance in which **Beer–Lambert absorbed percentage** should not be treated as predictive.

<!-- MODEL_12 -->

## Lesson 7.2: Photogeneration and photon-flux accounting

### A physical explanation before any numerical fit

Optical irradiance gives energy arriving per area per time; photon flux requires division by single-photon energy Eγ. A photon of E eV carries qE joules. In a perfect single-pass absorber, at most one electron–hole pair is produced per absorbed above-gap photon in the simple classical model; internal gain or carrier multiplication requires separately described mechanisms. Spectral weighting matters: one watt of blue light contains fewer photons than one watt of red light.

**Primary relationship:** Photon flux Φ=Popt/(qEγ) using W/cm² and Eγ in eV. The first task is to decide whether it is a structural geometric relation, a balance law, a statistical approximation or an experimentally calibrated response. This matters specifically for **photogeneration and photon-flux accounting**, because the same calculated number can emerge from physically incompatible material states. Explicitly note which band, lattice, impurity, contact or interface degrees of freedom the expression leaves out. A clear statement of validity is often more useful than giving the output to five decimal places.

Convert 1 mW/cm² monochromatic irradiance at 2 eV into photons cm⁻² s⁻¹. Compare with 1.5 eV illumination at the same irradiance, and identify why this does not directly determine short-circuit photocurrent.

### Transparent worked numerical example

The offline calculator **Photon flux at fixed irradiance** is deliberately simpler than the phenomenon being discussed. Let **Photon energy = 1.8333333 eV**. From the implemented expression `(0.001/(1.602176634e-19*E))/1e15`, the predicted value is **3.4044595 10^15 photons/(cm2 s)**. Change only the designated control to **2.1111111 eV** and the result becomes **2.9565043 10^15 photons/(cm2 s)**. In this controlled comparison the predicted quantity falls; the finite-difference sensitivity is **-1.61263871 (10^15 photons/(cm2 s))/(eV)**. This numerical result is deterministic, derived directly from the stated formula, and is *not* an observation of an actual sample. The two values illustrate what that formula encodes; they do not prove the material will behave this way.

The complete assumptions are: **Monochromatic radiant power 1 mW/cm2; all photons counted regardless of absorption, no photocarrier yield predicted**. Before interpreting the slope, check that the denominator of the expression cannot vanish in the slider range and that the output is in the declared units. A synthetic curve is not a scientific uncertainty band: there are no replicate wafers, measurement errors or competing mechanisms in this dataset. The correct conclusion is conditional—*if the stated assumptions hold, changing the input produces the computed result*. Any statement about a real device needs experimental comparison and fit diagnostics.

### Measurement plan and what the model can miss

Reflections, quantum yield, interference, exciton dissociation, and electrical collection efficiency separate photon input from usable current.

### Experimental counterfactual

The leading interpretation connects **photon absorption and optically active defect states** with a response in **photogeneration and photon-flux accounting**. Now suppose instead that the change is controlled by **nonradiative recombination, trap tails or imperfect extraction**. Both mechanisms could sometimes reproduce a monotonic trend in the single-variable calculator. A useful counterfactual is to change a second condition that affects one mechanism more strongly than the other—temperature, optical excitation depth, contact geometry, wafer thickness, crystal orientation or measurement frequency—while leaving the primary comparison matched. Explain how **spectrally calibrated EQE and excitation-dependent lifetime spectra** would be expected to discriminate the two models, and report in advance which outcome would overturn the preferred explanation.

### Three graded problems

**Problem 7.2A — Conceptual mechanism.** Explain in your own words what **photogeneration and photon-flux accounting** changes about the relation between **incident photon flux versus electrically collected carriers**. State two different microphysical mechanisms that could produce the same measured sign of response. Identify a relevant energy, length or time scale and show why the difference would matter for interpretation.

**Problem 7.2B — Quantitative verification.** Reproduce the values **3.4044595 10^15 photons/(cm2 s)** and **2.9565043 10^15 photons/(cm2 s)** using `(0.001/(1.602176634e-19*E))/1e15` at the two stated input values. Convert at least one related physical quantity to coherent SI units, report units in each algebraic step, and explain why increasing the model's input by the displayed amount makes the computed output falls. Which hidden material parameter could reverse a real-world trend?

**Problem 7.2C — Falsification and reporting.** Design a minimum independent experiment capable of distinguishing the current interpretation from **nonradiative recombination, trap tails or imperfect extraction**. Specify sampling locations, temperature, instrument calibration, measurement geometry, between-sample replication, and an observable that would force you to reject the interpretation. Name one specific circumstance in which **Photon flux at fixed irradiance** should not be treated as predictive.

## Lesson 7.3: Photoluminescence and defect signatures

### A physical explanation before any numerical fit

Photoluminescence samples the competition between optical excitation, radiative recombination, carrier trapping, nonradiative loss, and extraction of emitted photons. Peak energy can reflect band-edge transitions, excitons, impurities, donor–acceptor pairs, or defect complexes. Intensity differences across samples are uninterpretable without excitation power, collection optics, spectral correction, geometry, and temperature. Time-resolved methods add dynamics but do not by themselves distinguish surface loss from bulk traps.

**Primary relationship:** Use calibrated spectral position, polarization, lifetime, and intensity dependence as complementary observables. The first task is to decide whether it is a structural geometric relation, a balance law, a statistical approximation or an experimentally calibrated response. This matters specifically for **photoluminescence and defect signatures**, because the same calculated number can emerge from physically incompatible material states. Explicitly note which band, lattice, impurity, contact or interface degrees of freedom the expression leaves out. A clear statement of validity is often more useful than giving the output to five decimal places.

A low-temperature spectrum develops a strong sub-gap peak. Use power-dependent and temperature-dependent photoluminescence alongside capacitance or deep-level measurements to assess whether the peak indicates a specific defect.

### Transparent worked numerical example

The offline calculator **Beer–Lambert absorbed percentage** is deliberately simpler than the phenomenon being discussed. Let **Active-layer thickness = 8.9444444 micrometers**. From the implemented expression `100*(1-Math.exp(-1000*d*1e-4))`, the predicted value is **59.1165334 %**. Change only the designated control to **11.155556 micrometers** and the result becomes **67.2266846 %**. In this controlled comparison the predicted quantity rises; the finite-difference sensitivity is **3.66790756 (%)/(micrometers)**. This numerical result is deterministic, derived directly from the stated formula, and is *not* an observation of an actual sample. The two values illustrate what that formula encodes; they do not prove the material will behave this way.

### Measurement plan and what the model can miss

A plausible peak assignment is not identification unless alternate transitions and reabsorption are excluded.

### Experimental counterfactual

The leading interpretation connects **photon absorption and optically active defect states** with a response in **photoluminescence and defect signatures**. Now suppose instead that the change is controlled by **nonradiative recombination, trap tails or imperfect extraction**. Both mechanisms could sometimes reproduce a monotonic trend in the single-variable calculator. A useful counterfactual is to change a second condition that affects one mechanism more strongly than the other—temperature, optical excitation depth, contact geometry, wafer thickness, crystal orientation or measurement frequency—while leaving the primary comparison matched. Explain how **spectrally calibrated EQE and excitation-dependent lifetime spectra** would be expected to discriminate the two models, and report in advance which outcome would overturn the preferred explanation.

### Three graded problems

**Problem 7.3A — Conceptual mechanism.** Explain in your own words what **photoluminescence and defect signatures** changes about the relation between **incident photon flux versus electrically collected carriers**. State two different microphysical mechanisms that could produce the same measured sign of response. Identify a relevant energy, length or time scale and show why the difference would matter for interpretation.

**Problem 7.3B — Quantitative verification.** Reproduce the values **59.1165334 %** and **67.2266846 %** using `100*(1-Math.exp(-1000*d*1e-4))` at the two stated input values. Convert at least one related physical quantity to coherent SI units, report units in each algebraic step, and explain why increasing the model's input by the displayed amount makes the computed output rises. Which hidden material parameter could reverse a real-world trend?

**Problem 7.3C — Falsification and reporting.** Design a minimum independent experiment capable of distinguishing the current interpretation from **nonradiative recombination, trap tails or imperfect extraction**. Specify sampling locations, temperature, instrument calibration, measurement geometry, between-sample replication, and an observable that would force you to reject the interpretation. Name one specific circumstance in which **Beer–Lambert absorbed percentage** should not be treated as predictive.

## Lesson 7.4: Deep levels and capacitance transients

### A physical explanation before any numerical fit

A point defect or defect complex may introduce localized states within the gap, enabling thermal emission and capture. Deep-level transient spectroscopy can extract apparent activation energy and capture parameters by tracking capacitance relaxation across controlled temperature intervals. Peak identification must account for field-assisted emission, multiple levels, spatial inhomogeneity, and capture cross-section temperature dependence. Electron and hole trap labels refer to charge exchange, not a fixed structural identity.

**Primary relationship:** Temperature-dependent transient rates are measurements; microscopic defect assignments are hypotheses to test. The first task is to decide whether it is a structural geometric relation, a balance law, a statistical approximation or an experimentally calibrated response. This matters specifically for **deep levels and capacitance transients**, because the same calculated number can emerge from physically incompatible material states. Explicitly note which band, lattice, impurity, contact or interface degrees of freedom the expression leaves out. A clear statement of validity is often more useful than giving the output to five decimal places.

An anneal changes a DLTS peak area but also junction capacitance. Correct for depletion width and injection bias; compare electron microscopy or chemical analysis before declaring that one atomic vacancy was eliminated.

### Transparent worked numerical example

The offline calculator **Photon flux at fixed irradiance** is deliberately simpler than the phenomenon being discussed. Let **Photon energy = 2.3888889 eV**. From the implemented expression `(0.001/(1.602176634e-19*E))/1e15`, the predicted value is **2.61272473 10^15 photons/(cm2 s)**. Change only the designated control to **2.6666667 eV** and the result becomes **2.3405659 10^15 photons/(cm2 s)**. In this controlled comparison the predicted quantity falls; the finite-difference sensitivity is **-0.979771773 (10^15 photons/(cm2 s))/(eV)**. This numerical result is deterministic, derived directly from the stated formula, and is *not* an observation of an actual sample. The two values illustrate what that formula encodes; they do not prove the material will behave this way.

### Measurement plan and what the model can miss

An activation energy alone rarely reveals a unique microscopic defect without independent structural evidence.

### Experimental counterfactual

The leading interpretation connects **photon absorption and optically active defect states** with a response in **deep levels and capacitance transients**. Now suppose instead that the change is controlled by **nonradiative recombination, trap tails or imperfect extraction**. Both mechanisms could sometimes reproduce a monotonic trend in the single-variable calculator. A useful counterfactual is to change a second condition that affects one mechanism more strongly than the other—temperature, optical excitation depth, contact geometry, wafer thickness, crystal orientation or measurement frequency—while leaving the primary comparison matched. Explain how **spectrally calibrated EQE and excitation-dependent lifetime spectra** would be expected to discriminate the two models, and report in advance which outcome would overturn the preferred explanation.

### Three graded problems

**Problem 7.4A — Conceptual mechanism.** Explain in your own words what **deep levels and capacitance transients** changes about the relation between **incident photon flux versus electrically collected carriers**. State two different microphysical mechanisms that could produce the same measured sign of response. Identify a relevant energy, length or time scale and show why the difference would matter for interpretation.

**Problem 7.4B — Quantitative verification.** Reproduce the values **2.61272473 10^15 photons/(cm2 s)** and **2.3405659 10^15 photons/(cm2 s)** using `(0.001/(1.602176634e-19*E))/1e15` at the two stated input values. Convert at least one related physical quantity to coherent SI units, report units in each algebraic step, and explain why increasing the model's input by the displayed amount makes the computed output falls. Which hidden material parameter could reverse a real-world trend?

**Problem 7.4C — Falsification and reporting.** Design a minimum independent experiment capable of distinguishing the current interpretation from **nonradiative recombination, trap tails or imperfect extraction**. Specify sampling locations, temperature, instrument calibration, measurement geometry, between-sample replication, and an observable that would force you to reject the interpretation. Name one specific circumstance in which **Photon flux at fixed irradiance** should not be treated as predictive.

<!-- MODEL_13 -->

## Lesson 7.5: Photovoltaic and detector trade-offs

### A physical explanation before any numerical fit

A detector or solar cell combines optical absorption, charge separation, transport, and selective extraction. Making an absorber thicker often increases generated charge while worsening transport loss, recombination, and material cost. External quantum efficiency includes absorption and collection, whereas internal quantum efficiency depends on how absorbed photons are counted. Noise, dark current, and bandwidth matter for photodetectors even when responsivity is high.

**Primary relationship:** Specify wavelength, optical power calibration, bias, temperature, and noise bandwidth when comparing devices. The first task is to decide whether it is a structural geometric relation, a balance law, a statistical approximation or an experimentally calibrated response. This matters specifically for **photovoltaic and detector trade-offs**, because the same calculated number can emerge from physically incompatible material states. Explicitly note which band, lattice, impurity, contact or interface degrees of freedom the expression leaves out. A clear statement of validity is often more useful than giving the output to five decimal places.

A new passivation treatment improves detector responsivity but also increases dark current. Compare detectivity at matched bandwidth and temperature instead of declaring overall superiority based on photocurrent alone.

### Transparent worked numerical example

The offline calculator **Beer–Lambert absorbed percentage** is deliberately simpler than the phenomenon being discussed. Let **Active-layer thickness = 13.366667 micrometers**. From the implemented expression `100*(1-Math.exp(-1000*d*1e-4))`, the predicted value is **73.7280056 %**. Change only the designated control to **15.577778 micrometers** and the result becomes **78.9396441 %**. In this controlled comparison the predicted quantity rises; the finite-difference sensitivity is **2.35702241 (%)/(micrometers)**. This numerical result is deterministic, derived directly from the stated formula, and is *not* an observation of an actual sample. The two values illustrate what that formula encodes; they do not prove the material will behave this way.

### Measurement plan and what the model can miss

A formula for photon flux or Beer–Lambert absorption does not predict complete photovoltaic efficiency or noise-equivalent power.

### Experimental counterfactual

The leading interpretation connects **photon absorption and optically active defect states** with a response in **photovoltaic and detector trade-offs**. Now suppose instead that the change is controlled by **nonradiative recombination, trap tails or imperfect extraction**. Both mechanisms could sometimes reproduce a monotonic trend in the single-variable calculator. A useful counterfactual is to change a second condition that affects one mechanism more strongly than the other—temperature, optical excitation depth, contact geometry, wafer thickness, crystal orientation or measurement frequency—while leaving the primary comparison matched. Explain how **spectrally calibrated EQE and excitation-dependent lifetime spectra** would be expected to discriminate the two models, and report in advance which outcome would overturn the preferred explanation.

### Three graded problems

**Problem 7.5A — Conceptual mechanism.** Explain in your own words what **photovoltaic and detector trade-offs** changes about the relation between **incident photon flux versus electrically collected carriers**. State two different microphysical mechanisms that could produce the same measured sign of response. Identify a relevant energy, length or time scale and show why the difference would matter for interpretation.

**Problem 7.5B — Quantitative verification.** Reproduce the values **73.7280056 %** and **78.9396441 %** using `100*(1-Math.exp(-1000*d*1e-4))` at the two stated input values. Convert at least one related physical quantity to coherent SI units, report units in each algebraic step, and explain why increasing the model's input by the displayed amount makes the computed output rises. Which hidden material parameter could reverse a real-world trend?

**Problem 7.5C — Falsification and reporting.** Design a minimum independent experiment capable of distinguishing the current interpretation from **nonradiative recombination, trap tails or imperfect extraction**. Specify sampling locations, temperature, instrument calibration, measurement geometry, between-sample replication, and an observable that would force you to reject the interpretation. Name one specific circumstance in which **Beer–Lambert absorbed percentage** should not be treated as predictive.

## Integrated case study: Explaining a mismatch in photocurrent

### Problem statement and evidence hierarchy

A photon-flux estimate predicts more photoelectrons than the measured photodiode current. Treat the problem as a comparison of several causes, not a request to select one formula. First write down what was controlled and directly measured; separate that from what is an inference about **photon absorption and optically active defect states**. Material recipes, deposition logs and temperature setpoints should not be substituted for actual measured carrier concentrations, layer thicknesses, microstructural maps or local junction responses. In high-stakes applications, state what level of evidence would be sufficient before committing design resources or fabrication capacity.

### Linked calculations and missing-variable audit

Balance incident photons, reflected photons, absorbed photons, recombination, and carrier collection; use the absorption model and photon-flux calculator. Work both interactive models for the unit, first at their default conditions and then after changing one input by 10% within slider bounds. Recalculate one output manually and compare it to a second independent program or calculator. The two formulas address different features of the material, so their combination is not automatically a multi-physics simulation. Build a box-and-arrow account of how processing influences structure, carrier populations, electrical or optical response and eventual device performance. Label any link that is still only hypothetical.

### Experimental discrimination and judgment

Measure EQE wavelength dependence and reflectance plus lifetime and collection under controlled illumination. Distinguish a paired repeat on the same device from an independently fabricated replicate; predeclare what discrepancy requires reassessment. Preserve raw observations, geometry, uncertainties and model configurations. A credible conclusion identifies an observation that a rival explanation could not produce under the same controls. **Warning:** Absorbed fraction alone is not the measured quantum efficiency. Report evidence status separately as demonstrated, provisional, or not yet assessed. The cost of overclaiming a semiconductor property rises sharply when it becomes a process-selection or field-reliability decision.

### Five cumulative university examination prompts

1. Draw an atomistic-to-device diagram for **photon absorption and optically active defect states**, with a label on each directly measured or assumed arrow.
2. Compare **incident photon flux versus electrically collected carriers** and state the governing assumptions and units for one calculation.
3. Recompute one unit model in two independent ways and perform one limiting-case or monotonicity check.
4. Formulate a rival explanation using **nonradiative recombination, trap tails or imperfect extraction** and specify the result of **spectrally calibrated EQE and excitation-dependent lifetime spectra** that would distinguish it.
5. Deliver a one-page technical decision note that separates known facts, conditional calculations, uncertainty and additional qualification before scale-up.

