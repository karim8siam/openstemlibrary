# Unit 7: Earth Structure, Imaging, and Inverse Methods

## Guiding question

How do seismic recordings support models of crust, mantle and Earth interior?

**Fictional unit investigation.** An invented regional array observes arrivals from local events and distant earthquakes. Several three-dimensional velocity structures fit the limited travel times, and students assess uncertainty and resolution.

## Physical context

Earth imaging is inference from wave propagation, not direct photography. Every inversion contains trade-offs among model discretization, noise covariance, regularization, source distribution and spatial resolution. A valuable map displays both structure and its recoverability.

## Learning workflow

Before beginning, distinguish the scientific question, the measured quantity and the latent parameter that the student hopes to infer. Assign physical units, name a plausible alternate hypothesis, and state what data are fictional. For seismic imaging, document ray coverage and model resolution. A smooth image may reflect regularization rather than a physically smooth medium; surface-wave and body-wave data constrain different properties. The experiments are deliberately simplified so their calculations can be independently checked. They are not validated field instruments, real-time forecasts, or site-specific hazard assessments.

### Lesson 7.1: Travel-time curves and Earth layers

**Learning goals.** Explain the mechanism, translate the problem into measurable quantities, test an alternative interpretation and defend an uncertainty statement.

**Physical foundation.** Arrival times across epicentral distance reveal broad changes in seismic speed and discontinuities with depth. Interpreting global travel-time branches requires identifying phases and understanding curved raypaths. In the broader unit, Earth imaging is inference from wave propagation, not direct photography. Every inversion contains trade-offs among model discretization, noise covariance, regularization, source distribution and spatial resolution. A valuable map displays both structure and its recoverability.

**Observational method.** Compare first-arrival travel-time curves for hypothetical crustal and mantle velocities; annotate discontinuities in slope. Specify the coordinate frame, observation period, relevant units, acquisition and calibration limitations before interpreting the resulting figure.

**Common interpretive trap.** A piecewise straight plot is a simplified inference; velocity gradients produce curvature, triplications and shadow-zone effects. A neat numeric solution does not remove this interpretive ambiguity. Ask which further independent measurement could reveal whether the preferred explanation is incorrect.

**Applied investigation.** Estimate a travel-time difference across two ray-length assumptions. Provide a labeled sketch, a short reproducible table and a paragraph separating observed evidence from inferred process.

#### Interpretation and quantitative example

**Worked case 7.1: Ideal teleseismic travel time.** Synthetic input: `1134.0` km. Apply the explicitly declared relationship `x/8` to obtain **141.75 s**. Restrictions: Constant 8 km/s ray velocity, not realistic curved-ray global travel times. For this worked exercise, treat the input as a declared hypothetical value rather than a measurement. Copy the formula into a fresh calculation and check the unit conversion independently. Vary the input by ten percent and decide whether the output changes proportionally or nonlinearly. Explain which real-world conditions violate the assumptions listed. If the numeric result seems implausibly precise, round it appropriately and describe a physically meaningful range instead of inventing calibration. The purpose is transparent reasoning, not an official estimate. An inversion reconstructs a volume from limited wave paths. Assess where ray coverage is dense and where smooth colors are model extrapolation. Change the regularization to see whether a localized anomaly survives, and label the recovered parameter with correct units. Treat the result as a hypothesis subject to independent geological constraints.

#### Evidence design and falsification

Reconstruct the inference backwards. Start with the headline result and locate every conversion, classification and assumption required to obtain it. An estimate based on a chosen velocity, phase pick or site parameter should be labelled conditional on those inputs. Review the same steps after making one intentional mistake in the input metadata; document which output would become misleading and why. Here, the principal source of ambiguity is stated explicitly: A piecewise straight plot is a simplified inference; velocity gradients produce curvature, triplications and shadow-zone effects. Method A: compute a baseline result using the stated relation, preserving all units. Method B: perturb one relevant input and record the change. Method C: replace the simplest assumption with an alternative that would be plausible at the study scale; if you cannot recalculate it with the available information, state what is missing. Method D: compare with an independent kind of observation, if available. This order avoids hiding assumptions under additional significant figures. End the notebook by explaining how the proposed investigation (Estimate a travel-time difference across two ray-length assumptions.) addresses at least one weakness of the primary model.

**Knowledge check.** (1) Which claim is directly observed and which is inferred? (2) How would an alternate model change the expected observation? (3) Which number must be accompanied by uncertainty? (4) Why is the worked result unsuitable as a real-time safety conclusion?

### Lesson 7.2: Refraction and reflection seismology

**Learning goals.** Explain the mechanism, translate the problem into measurable quantities, test an alternative interpretation and defend an uncertainty statement.

**Physical foundation.** Controlled-source and earthquake-based imaging use reflections, refractions and converted arrivals to map contrasts in material properties. Resolution depends on wavelength, coverage and signal quality. In the broader unit, Earth imaging is inference from wave propagation, not direct photography. Every inversion contains trade-offs among model discretization, noise covariance, regularization, source distribution and spatial resolution. A valuable map displays both structure and its recoverability.

**Observational method.** Sketch shot-receiver paths through a layered crust and identify direct, head and reflected phases. Specify the coordinate frame, observation period, relevant units, acquisition and calibration limitations before interpreting the resulting figure.

**Common interpretive trap.** A strong reflector indicates impedance contrast, not necessarily a lithologic boundary of one unique type. A neat numeric solution does not remove this interpretive ambiguity. Ask which further independent measurement could reveal whether the preferred explanation is incorrect.

**Applied investigation.** Compare two models that share first arrivals but differ in deeper layers. Provide a labeled sketch, a short reproducible table and a paragraph separating observed evidence from inferred process.

#### Interpretation and quantitative example

**Worked case 7.2: Ideal thickness from vertical P-to-S delay.** Synthetic input: `3.56` s. Apply the explicitly declared relationship `x/(1/3.7-1/6.4)` to obtain **31.2225 km**. Restrictions: Simplified vertical ray approximation with Vp=6.4 and Vs=3.7 km/s. For this worked exercise, treat the input as a declared hypothetical value rather than a measurement. Copy the formula into a fresh calculation and check the unit conversion independently. Vary the input by ten percent and decide whether the output changes proportionally or nonlinearly. Explain which real-world conditions violate the assumptions listed. If the numeric result seems implausibly precise, round it appropriately and describe a physically meaningful range instead of inventing calibration. The purpose is transparent reasoning, not an official estimate. An inversion reconstructs a volume from limited wave paths. Assess where ray coverage is dense and where smooth colors are model extrapolation. Change the regularization to see whether a localized anomaly survives, and label the recovered parameter with correct units. Treat the result as a hypothesis subject to independent geological constraints.

#### Evidence design and falsification

A strong evidence chain identifies what the observer physically controls. Specify waveform or map provenance, the acquisition time standard, the instrument or field method, the adopted calibration, and an independent comparison. Is the observed pattern repeatable across genuinely separate records or did it arise after multiple views of the same data? Where an observation is transformed into a calculated quantity, retain its original units and values. Write an audit note on which data would be decisive and which are merely compatible. Here, the principal source of ambiguity is stated explicitly: A strong reflector indicates impedance contrast, not necessarily a lithologic boundary of one unique type. Create a four-row evidence matrix: observed quantity, inferred physical quantity, principal confounder, and proposed falsifying observation. Mark an entry as measured only when acquisition metadata is known. Repeat the matrix for a second hypothesis instead of dismissing it without calculation. This discipline prevents a tidy narrative from substituting for testable physical interpretation. End the notebook by explaining how the proposed investigation (Compare two models that share first arrivals but differ in deeper layers.) addresses at least one weakness of the primary model.

**Knowledge check.** (1) Which claim is directly observed and which is inferred? (2) How would an alternate model change the expected observation? (3) Which number must be accompanied by uncertainty? (4) Why is the worked result unsuitable as a real-time safety conclusion?

### Lesson 7.3: Tomography and inverse-problem regularization

**Learning goals.** Explain the mechanism, translate the problem into measurable quantities, test an alternative interpretation and defend an uncertainty statement.

**Physical foundation.** Seismic tomography infers velocity variations by relating travel-time residuals to sensitivity along paths. Many model cells are weakly sampled, so damping and smoothing influence the result. In the broader unit, Earth imaging is inference from wave propagation, not direct photography. Every inversion contains trade-offs among model discretization, noise covariance, regularization, source distribution and spatial resolution. A valuable map displays both structure and its recoverability.

**Observational method.** Build a tiny synthetic path–cell matrix and identify its null space conceptually before regularization. Specify the coordinate frame, observation period, relevant units, acquisition and calibration limitations before interpreting the resulting figure.

**Common interpretive trap.** A sharp colored anomaly can be an inversion artifact or a regularization choice, not a directly photographed structure. A neat numeric solution does not remove this interpretive ambiguity. Ask which further independent measurement could reveal whether the preferred explanation is incorrect.

**Applied investigation.** Map checkerboard recovery limits and identify cells with poor crossing-ray coverage. Provide a labeled sketch, a short reproducible table and a paragraph separating observed evidence from inferred process.

#### Interpretation and quantitative example

**Worked case 7.3: Ideal teleseismic travel time.** Synthetic input: `2234.0` km. Apply the explicitly declared relationship `x/8` to obtain **279.25 s**. Restrictions: Constant 8 km/s ray velocity, not realistic curved-ray global travel times. For this worked exercise, treat the input as a declared hypothetical value rather than a measurement. Copy the formula into a fresh calculation and check the unit conversion independently. Vary the input by ten percent and decide whether the output changes proportionally or nonlinearly. Explain which real-world conditions violate the assumptions listed. If the numeric result seems implausibly precise, round it appropriately and describe a physically meaningful range instead of inventing calibration. The purpose is transparent reasoning, not an official estimate. An inversion reconstructs a volume from limited wave paths. Assess where ray coverage is dense and where smooth colors are model extrapolation. Change the regularization to see whether a localized anomaly survives, and label the recovered parameter with correct units. Treat the result as a hypothesis subject to independent geological constraints.

#### Evidence design and falsification

When comparing scenarios, preserve the same measurement geometry if possible. A change in a source parameter may look like a path effect when stations or filters differ. Design a sensitivity table with columns for adopted value, plausible range, reason for uncertainty and effect on inference. Distinguish an instrumental limitation from a physical ambiguity: improving sampling can solve the former while the latter may need an entirely different experiment. Here, the principal source of ambiguity is stated explicitly: A sharp colored anomaly can be an inversion artifact or a regularization choice, not a directly photographed structure. Build the result graph only after labelling its axes and quantities. Include a plausible range of inputs rather than a single favorable selection. Annotate any discontinuity, threshold or saturated measurement. Next, state whether the curve demonstrates a general law, a restricted approximation or merely the numerical behavior of an arbitrary toy formula. The caption should not promise resolution that the data cannot support. End the notebook by explaining how the proposed investigation (Map checkerboard recovery limits and identify cells with poor crossing-ray coverage.) addresses at least one weakness of the primary model.

**Knowledge check.** (1) Which claim is directly observed and which is inferred? (2) How would an alternate model change the expected observation? (3) Which number must be accompanied by uncertainty? (4) Why is the worked result unsuitable as a real-time safety conclusion?

### Lesson 7.4: Receiver functions and crustal structure

**Learning goals.** Explain the mechanism, translate the problem into measurable quantities, test an alternative interpretation and defend an uncertainty statement.

**Physical foundation.** Converted phases near a receiver can reveal velocity contrasts such as the Moho when interpreted with a velocity model and assumptions about incidence and layering. In the broader unit, Earth imaging is inference from wave propagation, not direct photography. Every inversion contains trade-offs among model discretization, noise covariance, regularization, source distribution and spatial resolution. A valuable map displays both structure and its recoverability.

**Observational method.** Compare time offsets of schematic P-to-S conversions and a simplified crustal thickness estimate. Specify the coordinate frame, observation period, relevant units, acquisition and calibration limitations before interpreting the resulting figure.

**Common interpretive trap.** Trade-offs between crustal thickness and velocity ratio can give multiple solutions to the same conversion delay. A neat numeric solution does not remove this interpretive ambiguity. Ask which further independent measurement could reveal whether the preferred explanation is incorrect.

**Applied investigation.** Propose a joint observation that could reduce the trade-off. Provide a labeled sketch, a short reproducible table and a paragraph separating observed evidence from inferred process.

#### Interpretation and quantitative example

**Worked case 7.4: Ideal thickness from vertical P-to-S delay.** Synthetic input: `5.685` s. Apply the explicitly declared relationship `x/(1/3.7-1/6.4)` to obtain **49.8596 km**. Restrictions: Simplified vertical ray approximation with Vp=6.4 and Vs=3.7 km/s. For this worked exercise, treat the input as a declared hypothetical value rather than a measurement. Copy the formula into a fresh calculation and check the unit conversion independently. Vary the input by ten percent and decide whether the output changes proportionally or nonlinearly. Explain which real-world conditions violate the assumptions listed. If the numeric result seems implausibly precise, round it appropriately and describe a physically meaningful range instead of inventing calibration. The purpose is transparent reasoning, not an official estimate. An inversion reconstructs a volume from limited wave paths. Assess where ray coverage is dense and where smooth colors are model extrapolation. Change the regularization to see whether a localized anomaly survives, and label the recovered parameter with correct units. Treat the result as a hypothesis subject to independent geological constraints.

#### Evidence design and falsification

Choose one prediction that would differ under a competing mechanism. A useful prediction has a measurable sign, timing, spectral or spatial signature rather than an undefined expectation that a map should look different. Explain how the predicted quantity would be calculated before looking at the fictional test record. If both explanations remain consistent with the evidence, report the unresolved alternatives and the next practical observation needed. Here, the principal source of ambiguity is stated explicitly: Trade-offs between crustal thickness and velocity ratio can give multiple solutions to the same conversion delay. Keep a processing log with coordinate reference, UTC times, units, processing order and exclusion rules. Compare pre- and post-processing records and explain discrepancies. In the conclusion, identify which claim survives the most consequential alternative parameterization. Reproducibility means another researcher could regenerate the result and find the same limitations, not simply the same decimal answer. End the notebook by explaining how the proposed investigation (Propose a joint observation that could reduce the trade-off.) addresses at least one weakness of the primary model.

**Knowledge check.** (1) Which claim is directly observed and which is inferred? (2) How would an alternate model change the expected observation? (3) Which number must be accompanied by uncertainty? (4) Why is the worked result unsuitable as a real-time safety conclusion?

### Lesson 7.5: Surface-wave and ambient-noise imaging

**Learning goals.** Explain the mechanism, translate the problem into measurable quantities, test an alternative interpretation and defend an uncertainty statement.

**Physical foundation.** Surface-wave dispersion and cross-correlations of ambient seismic noise constrain structure over useful depth ranges, subject to uneven source illumination and dispersion interpretation. In the broader unit, Earth imaging is inference from wave propagation, not direct photography. Every inversion contains trade-offs among model discretization, noise covariance, regularization, source distribution and spatial resolution. A valuable map displays both structure and its recoverability.

**Observational method.** Analyze invented period-dependent phase speeds and noise correlations from pairs of stations. Specify the coordinate frame, observation period, relevant units, acquisition and calibration limitations before interpreting the resulting figure.

**Common interpretive trap.** A symmetric noise correlation is not automatically a perfect Green's function, and phase velocity is not group velocity. A neat numeric solution does not remove this interpretive ambiguity. Ask which further independent measurement could reveal whether the preferred explanation is incorrect.

**Applied investigation.** Create a resolution discussion for long-period and short-period measurements. Provide a labeled sketch, a short reproducible table and a paragraph separating observed evidence from inferred process.

#### Interpretation and quantitative example

**Worked case 7.5: Ideal teleseismic travel time.** Synthetic input: `3334.0` km. Apply the explicitly declared relationship `x/8` to obtain **416.75 s**. Restrictions: Constant 8 km/s ray velocity, not realistic curved-ray global travel times. For this worked exercise, treat the input as a declared hypothetical value rather than a measurement. Copy the formula into a fresh calculation and check the unit conversion independently. Vary the input by ten percent and decide whether the output changes proportionally or nonlinearly. Explain which real-world conditions violate the assumptions listed. If the numeric result seems implausibly precise, round it appropriately and describe a physically meaningful range instead of inventing calibration. The purpose is transparent reasoning, not an official estimate. An inversion reconstructs a volume from limited wave paths. Assess where ray coverage is dense and where smooth colors are model extrapolation. Change the regularization to see whether a localized anomaly survives, and label the recovered parameter with correct units. Treat the result as a hypothesis subject to independent geological constraints.

#### Evidence design and falsification

Reconstruct the inference backwards. Start with the headline result and locate every conversion, classification and assumption required to obtain it. An estimate based on a chosen velocity, phase pick or site parameter should be labelled conditional on those inputs. Review the same steps after making one intentional mistake in the input metadata; document which output would become misleading and why. Here, the principal source of ambiguity is stated explicitly: A symmetric noise correlation is not automatically a perfect Green's function, and phase velocity is not group velocity. Method A: compute a baseline result using the stated relation, preserving all units. Method B: perturb one relevant input and record the change. Method C: replace the simplest assumption with an alternative that would be plausible at the study scale; if you cannot recalculate it with the available information, state what is missing. Method D: compare with an independent kind of observation, if available. This order avoids hiding assumptions under additional significant figures. End the notebook by explaining how the proposed investigation (Create a resolution discussion for long-period and short-period measurements.) addresses at least one weakness of the primary model.

**Knowledge check.** (1) Which claim is directly observed and which is inferred? (2) How would an alternate model change the expected observation? (3) Which number must be accompanied by uncertainty? (4) Why is the worked result unsuitable as a real-time safety conclusion?

## Unit 7 capstone: Interpret an illustrative multi-path travel-time matrix and two velocity models. Report residual reduction, resolution loss and the response to regularization. Produce a compact methods figure with color scale units and a separate uncertainty panel.

**Research scenario:** An invented regional array observes arrivals from local events and distant earthquakes. Several three-dimensional velocity structures fit the limited travel times, and students assess uncertainty and resolution. The goal is to produce a reasoned comparison of at least two defensible models, not to reverse-engineer a predetermined answer. Start by recording each input variable with units, a confidence grade and a plausible range. Name the forward calculation associated with each inference and outline how the inputs enter the formula. Preserve the fabricated dataset in its supplied CSV form and cite its generation method; these records do not correspond to real earthquakes or real sensor networks.

**Procedure.** First, draw a map or schematic that makes geometric assumptions visible. Second, check station or sample identifiers and the relationship of the observation period to the question. Third, compute baseline statistics and at least one worked relation by hand before using the browser model. Fourth, investigate a competing hypothesis using an independently chosen measurement or a perturbation of a consequential parameter. Fifth, repeat after withholding one doubtful observation. Compare whether the scientific conclusion survives that choice. An inversion reconstructs a volume from limited wave paths. Assess where ray coverage is dense and where smooth colors are model extrapolation. Change the regularization to see whether a localized anomaly survives, and label the recovered parameter with correct units. Treat the result as a hypothesis subject to independent geological constraints.

**Required outputs.** Submit a two-page technical brief with a hypothesis table, raw and corrected values, an equation inventory, an uncertainty budget, a labelled graphic and a short limitations section. Include all model parameters. Do not omit unsuccessful tests and do not represent computer-generated data as measured field observations. Students should record their own explanations rather than copying one another's interpretation. Discuss how different station distributions or sampling choices could cause an apparently significant spatial pattern without a corresponding physical change.

**Extensions.** Earth imaging is inference from wave propagation, not direct photography. Every inversion contains trade-offs among model discretization, noise covariance, regularization, source distribution and spatial resolution. A valuable map displays both structure and its recoverability. Write an explicit counterfactual: what observation would undermine the main hypothesis? Consider what a larger dataset could resolve and what it would leave uncertain. Finally, design an accessible presentation of the result with a descriptive figure caption, a plain-language explanation of each symbol, and a table of numerical values for readers who cannot interpret a colored graph. Re-evaluate the result against professional source and public-safety boundaries before suggesting a consequential application.

**Peer-review rubric.** Assign 0–4 points each for correctness of units, explicit assumptions, data provenance, comparison with alternatives, uncertainty treatment, computational reproducibility and ethical communication. A polished figure without units, or a convincing narrative without a falsifiable test, should not receive full credit. Explain in prose why the least certain input affects confidence, and identify at least one result that could change with additional observations.
