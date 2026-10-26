# Unit 8: Laboratory methods, uncertainty and scientific communication

## Central research question

**How should a geochemical result be validated and reported so others can reproduce its interpretation?**

**Synthetic field investigation.** A fictional laboratory processes rock digests and river-water samples with reference materials, blanks, duplicates and spike recoveries. The setting, sampling values and numerical observations are invented for instruction; they do not describe a monitored site or an operational geochemical assessment. Compare at least two hypotheses before drawing conclusions, and make every material balance dimensionally explicit.

## Conceptual roadmap: linking molecules to landscapes

An element's presence in a sample records the combined influence of source composition, fractionation, physical transport, reaction pathways and analytical preparation. A bulk geochemical measurement is therefore not automatically a direct measurement of a reaction rate or source history. This unit starts with the physical and chemical mechanism, identifies the measurable data, introduces a quantitative calculation and closes by asking what observation would challenge the interpretation. The distinction between *concentration*, *inventory* and *flux* is essential: doubling water discharge can double transport while dissolved concentration stays constant; concentrating a fluid by evaporation can raise a concentration even if no material enters the system.

In practice the reported concentration depends on the sampled phase and method. Unfiltered water may contain colloids that a dissolved-only filtration removes; a total-rock digestion may include grains excluded by a selective extraction; a sediment sample may reflect a chosen particle-size fraction. These distinctions are part of the evidence, not clerical details. Students should write units beside every column, use consistent oxidation-state and elemental nomenclature, and retain method blanks and field duplicates when the problem concerns observation quality. Chemical signatures are most convincing when a forward reaction model can explain several independent species at once.

### A unit-level map of uncertainties

Consider three layers of uncertainty before interpreting the unit's synthetic results. First are observational errors: detection limits, contamination, temperature, storage, calibration and representative sampling. Second are physicochemical model errors: activity assumptions, unknown phases, heterogeneous rates, mineral composition, open-system exchange and dependence on pressure or temperature. Third are attribution errors: several source and reaction combinations may predict similar elemental or isotopic patterns. Keeping these layers separate allows the class to decide whether better analysis, more samples or a different conceptual model is the next justified step.

## Unit learning outcomes

By the end of this unit, students should be able to name the relevant reservoirs, express governing relations with units, calculate at least one interpretable quantity, check a competing explanation, and specify what extra observation would increase confidence. The worked calculations are tightly simplified and do not constitute a validated geochemical speciation model, a professional environmental investigation or a public-health threshold determination.

## Lesson 8.1: Sampling design and contamination control

### Mechanism and why it matters

Representative sampling requires defined support, chain of custody and containers appropriate for intended analytes. Identify the named chemical phase and its exchange boundaries. Distinguish measured species totals from inferred reactions; one pattern can have several mechanisms.

### Sampling and measurement protocol

Write a field and laboratory protocol covering filtration, preservation, blanks, duplicate locations and holding conditions. Record phase, sampling support, date, concentration or ratio units, calibration and detection limit. Define which quantities are observed and which depend on an assumed model.

### Competing explanations and identifiability

A clean-looking sample can still be contaminated by tools, acids, bottles or atmospheric dust. Specify an independently testable observation capable of distinguishing this explanation from an alternative source, reaction or laboratory bias.

### Worked numerical example — Sample dilution

**Problem.** A 2 mL aliquot is diluted to 50 mL and analyzed at 0.8 mg/L; original mg/L.

**Mathematical setup:** `0.8*50/2`. After checking the listed mass, time and amount units, the calculated answer is **20 mg/L**. Write down the inputs separately from the chosen constant or reference so an independent reviewer can recompute the result. If the expression uses a logarithm or a ratio, confirm that its argument is dimensionless; if a molar amount is involved, convert grams to moles before applying reaction coefficients. Because the values are invented for this lesson, the arithmetic demonstrates the physical scale and not a measurement-derived regional conclusion.

**Sensitivity check.** Compare the sign and magnitude with a limiting case and perturb the main input by ten percent. Report whether the relationship is linear or nonlinear, and avoid overstating numerical precision.

### Targeted investigation and practical interpretation

Compute concentration after a documented sample dilution. Create a six-row synthetic table with inputs, predicted outputs and one replicate. Compare a rival process and document a falsifiable difference.

### Advanced reasoning: Metrological traceability

A numerical result is credible only when measurement units, calibration range, matrix effects and correction steps are visible. Replicates characterize scatter, reference materials can reveal bias, and recovery estimates test matrix effects. None is a universal replacement for the others; below-quantification results require careful censoring treatment.

### Knowledge check and research questions


1. Recalculate the numerical example using consistent units.
2. Which competing physical process could reproduce the observation?
3. Which new measurement would discriminate the mechanisms?
4. Which assumed parameter creates the greatest model sensitivity?

**Instructor benchmark.** 20 mg/L, conditional on the stated model and units.

## Lesson 8.2: Instrument calibration and detection limits

### Mechanism and why it matters

Calibration curves connect measured signal to analyte amount only within tested response and matrix conditions. Identify the named chemical phase and its exchange boundaries. Distinguish measured species totals from inferred reactions; one pattern can have several mechanisms.

### Sampling and measurement protocol

Include multi-point standards, laboratory control samples and matrix spikes, recording any intercept and linearity check. Record phase, sampling support, date, concentration or ratio units, calibration and detection limit. Define which quantities are observed and which depend on an assumed model.

### Competing explanations and identifiability

A result beneath quantification limit should not be published with unjustified significant figures. Specify an independently testable observation capable of distinguishing this explanation from an alternative source, reaction or laboratory bias.

### Worked numerical example — Blank-derived LOD

**Problem.** Blank standard deviation is 0.6 signal units and calibration sensitivity is 2 units/(mg/L); 3 sigma LOD.

**Mathematical setup:** `3*0.6/2`. After checking the listed mass, time and amount units, the calculated answer is **0.9 mg/L**. Write down the inputs separately from the chosen constant or reference so an independent reviewer can recompute the result. If the expression uses a logarithm or a ratio, confirm that its argument is dimensionless; if a molar amount is involved, convert grams to moles before applying reaction coefficients. Because the values are invented for this lesson, the arithmetic demonstrates the physical scale and not a measurement-derived regional conclusion.

**Sensitivity check.** Compare the sign and magnitude with a limiting case and perturb the main input by ten percent. Report whether the relationship is linear or nonlinear, and avoid overstating numerical precision.

### Targeted investigation and practical interpretation

Estimate a simple detection limit from blank signal variability. Create a six-row synthetic table with inputs, predicted outputs and one replicate. Compare a rival process and document a falsifiable difference.

### Advanced reasoning: Metrological traceability

A numerical result is credible only when measurement units, calibration range, matrix effects and correction steps are visible. Replicates characterize scatter, reference materials can reveal bias, and recovery estimates test matrix effects. None is a universal replacement for the others; below-quantification results require careful censoring treatment.

### Knowledge check and research questions


1. Recalculate the numerical example using consistent units.
2. Which competing physical process could reproduce the observation?
3. Which new measurement would discriminate the mechanisms?
4. Which assumed parameter creates the greatest model sensitivity?

**Instructor benchmark.** 0.9 mg/L, conditional on the stated model and units.

## Lesson 8.3: Accuracy, precision and spike recovery

### Mechanism and why it matters

Repeatability, recovery and systematic bias measure different properties of a method; one cannot replace the others. Identify the named chemical phase and its exchange boundaries. Distinguish measured species totals from inferred reactions; one pattern can have several mechanisms.

### Sampling and measurement protocol

Use replicate measurements, certified reference materials and matrix spikes with separate acceptance criteria. Record phase, sampling support, date, concentration or ratio units, calibration and detection limit. Define which quantities are observed and which depend on an assumed model.

### Competing explanations and identifiability

Excellent precision around a biased value may produce a misleadingly narrow uncertainty interval. Specify an independently testable observation capable of distinguishing this explanation from an alternative source, reaction or laboratory bias.

### Worked numerical example — Spike recovery

**Problem.** Native level 3 mg/L, spiked sample 7.5 mg/L, added spike 5 mg/L; recovery %.

**Mathematical setup:** `100*(7.5-3)/5`. After checking the listed mass, time and amount units, the calculated answer is **90 percent**. Write down the inputs separately from the chosen constant or reference so an independent reviewer can recompute the result. If the expression uses a logarithm or a ratio, confirm that its argument is dimensionless; if a molar amount is involved, convert grams to moles before applying reaction coefficients. Because the values are invented for this lesson, the arithmetic demonstrates the physical scale and not a measurement-derived regional conclusion.

**Sensitivity check.** Compare the sign and magnitude with a limiting case and perturb the main input by ten percent. Report whether the relationship is linear or nonlinear, and avoid overstating numerical precision.

### Targeted investigation and practical interpretation

Compute recovery percentage for a spiked sample. Create a six-row synthetic table with inputs, predicted outputs and one replicate. Compare a rival process and document a falsifiable difference.

### Advanced reasoning: Metrological traceability

A numerical result is credible only when measurement units, calibration range, matrix effects and correction steps are visible. Replicates characterize scatter, reference materials can reveal bias, and recovery estimates test matrix effects. None is a universal replacement for the others; below-quantification results require careful censoring treatment.

### Knowledge check and research questions


1. Recalculate the numerical example using consistent units.
2. Which competing physical process could reproduce the observation?
3. Which new measurement would discriminate the mechanisms?
4. Which assumed parameter creates the greatest model sensitivity?

**Instructor benchmark.** 90 percent, conditional on the stated model and units.

## Lesson 8.4: Uncertainty propagation and significant figures

### Mechanism and why it matters

Every reported value has uncertainty from measurement, calibration, handling and model conversion. Identify the named chemical phase and its exchange boundaries. Distinguish measured species totals from inferred reactions; one pattern can have several mechanisms.

### Sampling and measurement protocol

Propagate independent random errors using declared assumptions and separately report correlated systematic effects. Record phase, sampling support, date, concentration or ratio units, calibration and detection limit. Define which quantities are observed and which depend on an assumed model.

### Competing explanations and identifiability

Rounding only the final answer does not correct an omitted uncertainty source. Specify an independently testable observation capable of distinguishing this explanation from an alternative source, reaction or laboratory bias.

### Worked numerical example — Uncertainty of multiplication

**Problem.** Independent relative errors 3% and 4%: combined relative standard uncertainty.

**Mathematical setup:** `math.sqrt(3**2+4**2)`. After checking the listed mass, time and amount units, the calculated answer is **5 percent**. Write down the inputs separately from the chosen constant or reference so an independent reviewer can recompute the result. If the expression uses a logarithm or a ratio, confirm that its argument is dimensionless; if a molar amount is involved, convert grams to moles before applying reaction coefficients. Because the values are invented for this lesson, the arithmetic demonstrates the physical scale and not a measurement-derived regional conclusion.

**Sensitivity check.** Compare the sign and magnitude with a limiting case and perturb the main input by ten percent. Report whether the relationship is linear or nonlinear, and avoid overstating numerical precision.

### Targeted investigation and practical interpretation

Calculate the relative uncertainty of a product or ratio. Create a six-row synthetic table with inputs, predicted outputs and one replicate. Compare a rival process and document a falsifiable difference.

### Advanced reasoning: Metrological traceability

A numerical result is credible only when measurement units, calibration range, matrix effects and correction steps are visible. Replicates characterize scatter, reference materials can reveal bias, and recovery estimates test matrix effects. None is a universal replacement for the others; below-quantification results require careful censoring treatment.

### Knowledge check and research questions


1. Recalculate the numerical example using consistent units.
2. Which competing physical process could reproduce the observation?
3. Which new measurement would discriminate the mechanisms?
4. Which assumed parameter creates the greatest model sensitivity?

**Instructor benchmark.** 5 percent, conditional on the stated model and units.

## Lesson 8.5: Data integrity and reproducible reporting

### Mechanism and why it matters

A robust geochemical dataset retains raw signals, units, data dictionaries, standards and method changes. Identify the named chemical phase and its exchange boundaries. Distinguish measured species totals from inferred reactions; one pattern can have several mechanisms.

### Sampling and measurement protocol

Assign stable sample identifiers, document missingness and publish scripts with versions and testable assertions. Record phase, sampling support, date, concentration or ratio units, calibration and detection limit. Define which quantities are observed and which depend on an assumed model.

### Competing explanations and identifiability

A highly polished map cannot rescue undocumented filtering, selective omission or unit mismatch. Specify an independently testable observation capable of distinguishing this explanation from an alternative source, reaction or laboratory bias.

### Worked numerical example — Blank correction

**Problem.** Signal-based concentration=1.35 mg/L, blank=0.12 mg/L; subtract blank.

**Mathematical setup:** `1.35-0.12`. After checking the listed mass, time and amount units, the calculated answer is **1.23 mg/L**. Write down the inputs separately from the chosen constant or reference so an independent reviewer can recompute the result. If the expression uses a logarithm or a ratio, confirm that its argument is dimensionless; if a molar amount is involved, convert grams to moles before applying reaction coefficients. Because the values are invented for this lesson, the arithmetic demonstrates the physical scale and not a measurement-derived regional conclusion.

**Sensitivity check.** Compare the sign and magnitude with a limiting case and perturb the main input by ten percent. Report whether the relationship is linear or nonlinear, and avoid overstating numerical precision.

### Targeted investigation and practical interpretation

Calculate a blank-corrected value and provide a transparent processing trail. Create a six-row synthetic table with inputs, predicted outputs and one replicate. Compare a rival process and document a falsifiable difference.

### Advanced reasoning: Metrological traceability

A numerical result is credible only when measurement units, calibration range, matrix effects and correction steps are visible. Replicates characterize scatter, reference materials can reveal bias, and recovery estimates test matrix effects. None is a universal replacement for the others; below-quantification results require careful censoring treatment.

### Knowledge check and research questions


1. Recalculate the numerical example using consistent units.
2. Which competing physical process could reproduce the observation?
3. Which new measurement would discriminate the mechanisms?
4. Which assumed parameter creates the greatest model sensitivity?

**Instructor benchmark.** 1.23 mg/L, conditional on the stated model and units.

## Integrated investigation 8: Laboratory methods, uncertainty and scientific communication capstone

('Laboratory audit', 'Invent an eight-sample laboratory batch with two blanks, two duplicates, a calibration check and two spiked matrix aliquots. Calculate blank-subtracted data, recovery, relative precision and a detection-limit proxy. Document whether a value below quantification is a zero, a censored number or an unresolved signal. Show how a missed 25-fold dilution propagates into an apparently compelling but false regional anomaly.')

### Design and controls

Before computing any numbers, list the intended mechanistic question, the sampling unit, plausible confounding influences and the criteria for rejecting a proposed explanation. Separate control treatments from replicates. Specify one independent check that was not used to choose model coefficients, since a model cannot be validated merely by predicting its own calibration inputs. Synthetic scenarios are safe for classroom inference but do not replace field permissions, contamination control or specialist laboratory work.

### A complete synthetic data record

Use a header with the following fields: sample_id, phase, dry_mass_g or volume_L, chemical_species, measured_value, analytical_unit, uncertainty, model_assumption, replicate_id and observation_status. Every derived column should include a formula and an audit trail. Avoid blanks that could ambiguously mean zero; label missing or below-quantification values explicitly. The class should archive its original input table and a derived working table so updates to calculations cannot overwrite evidence.

### Expected result and alternatives

Analyze the invented measurements with the simplest mass balance or equilibrium relationship appropriate to the question. Choose plausible parameter ranges before looking at the pattern. Next deliberately generate an alternative dataset under a different process that yields a similar headline gradient. Explain which additional variable, sampling depth, time series or reference material would distinguish them. This step addresses the practical reality that geological and chemical processes are often nonunique when seen through sparse observations.

### Sensitivity and uncertainty

Build a one-at-a-time sensitivity table varying at least two inputs by 5%, 10% and 20%. Use a separate scenario for systematic calibration shift, because correlated bias does not vanish by averaging independent samples. Include sampling uncertainty when a large reservoir is represented by a few rock chips or bottles. Report the resulting range as a model-conditioned bound rather than an objectively measured confidence interval unless a statistical sampling model was justified.

### Interpretation and reporting

The final deliverable is a short field-style memo with a figure, a unit-checked table, a reproducible calculation and two rival explanations. Distinguish measured variables from estimated parameters by typography or column label. Provide the domain where the simple model is defensible, including temperature, composition and phase assumptions. Avoid making health, engineering or management decisions from synthetic data; those require validated data and appropriate regulatory and professional guidance.

### Further experimental design

Propose two follow-up observations and rank them by discrimination power, cost and likelihood of analytical bias. A new sample that merely repeats the same confounded measurement may reduce noise without reducing the ambiguity of the hypothesis. A strategically chosen cross-phase, isotope or seasonal measurement can be more informative. Set a stopping rule: what numerical discrepancy or missing diagnostic signature would be sufficient to reject the favored model?

### Research notebook prompts

1. At checkpoint 1, identify which assumptions in investigation 8 are directly tested, which still require external constraints, and how one alternative reaction or transport pathway could change the conclusion without necessarily altering the measured primary tracer. Record the expected sign of the change and the observation that would distinguish it.
2. At checkpoint 2, identify which assumptions in investigation 8 are directly tested, which still require external constraints, and how one alternative reaction or transport pathway could change the conclusion without necessarily altering the measured primary tracer. Record the expected sign of the change and the observation that would distinguish it.
3. At checkpoint 3, identify which assumptions in investigation 8 are directly tested, which still require external constraints, and how one alternative reaction or transport pathway could change the conclusion without necessarily altering the measured primary tracer. Record the expected sign of the change and the observation that would distinguish it.
4. At checkpoint 4, identify which assumptions in investigation 8 are directly tested, which still require external constraints, and how one alternative reaction or transport pathway could change the conclusion without necessarily altering the measured primary tracer. Record the expected sign of the change and the observation that would distinguish it.
5. At checkpoint 5, identify which assumptions in investigation 8 are directly tested, which still require external constraints, and how one alternative reaction or transport pathway could change the conclusion without necessarily altering the measured primary tracer. Record the expected sign of the change and the observation that would distinguish it.
6. At checkpoint 6, identify which assumptions in investigation 8 are directly tested, which still require external constraints, and how one alternative reaction or transport pathway could change the conclusion without necessarily altering the measured primary tracer. Record the expected sign of the change and the observation that would distinguish it.
7. At checkpoint 7, identify which assumptions in investigation 8 are directly tested, which still require external constraints, and how one alternative reaction or transport pathway could change the conclusion without necessarily altering the measured primary tracer. Record the expected sign of the change and the observation that would distinguish it.
8. At checkpoint 8, identify which assumptions in investigation 8 are directly tested, which still require external constraints, and how one alternative reaction or transport pathway could change the conclusion without necessarily altering the measured primary tracer. Record the expected sign of the change and the observation that would distinguish it.

## Unit 8 synthesis: claim, evidence, limitations

The correct output of a geochemical investigation is not just a fitted number. A defensible conclusion links an observation to a specific physical or chemical mechanism while making conditional assumptions explicit. In this unit, write a three-column comparison: **observed or invented data**, **quantitative model result**, and **possible geological explanation**. Any statement that relies on a presumed endmember, reference standard or equilibrium assumption belongs in the last two columns. For a stronger claim, propose observations that would separate mechanism from coincidence.

### Independent short assessment

- Choose one of the five numerical cases and reconstruct it using a different sequence of unit conversions. Confirm that the dimensions still cancel.
- Choose the most important environmental, geological or laboratory confounder from the five lessons. Explain whether it creates random scatter, systematic bias or a genuine alternative Earth process.
- Choose two variables of different spatial scales and explain why plotting them on the same grid would not establish causation.
- Write a transparent uncertainty statement: data are fictional, reference assumptions are specified, sensitivity has been tested, and a professional application requires additional measurements.

### Suggested group discussion

Compare a precise but unrepresentative measurement with a noisy but representative sampling design. The former may look more convincing in a graph yet produce a more biased inventory or flux. Discuss a case where adding more significant digits does not improve geological accuracy. Discuss whether a model with a near-perfect fit has proved its reaction pathway or merely fitted several free parameters. End by identifying one prediction not used in the original fit, and describe how a prospective measurement could potentially falsify the process model.

