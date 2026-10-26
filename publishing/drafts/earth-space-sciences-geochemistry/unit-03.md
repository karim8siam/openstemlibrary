# Unit 3: Igneous processes and element partitioning

## Central research question

**Which chemical patterns constrain melting, crystallization and mantle source composition?**

**Synthetic field investigation.** A hypothetical basalt suite has incompatible-element trends and variable magnesium; alternative crystallization and melting histories are compared. The setting, sampling values and numerical observations are invented for instruction; they do not describe a monitored site or an operational geochemical assessment. Compare at least two hypotheses before drawing conclusions, and make every material balance dimensionally explicit.

## Conceptual roadmap: linking molecules to landscapes

An element's presence in a sample records the combined influence of source composition, fractionation, physical transport, reaction pathways and analytical preparation. A bulk geochemical measurement is therefore not automatically a direct measurement of a reaction rate or source history. This unit starts with the physical and chemical mechanism, identifies the measurable data, introduces a quantitative calculation and closes by asking what observation would challenge the interpretation. The distinction between *concentration*, *inventory* and *flux* is essential: doubling water discharge can double transport while dissolved concentration stays constant; concentrating a fluid by evaporation can raise a concentration even if no material enters the system.

In practice the reported concentration depends on the sampled phase and method. Unfiltered water may contain colloids that a dissolved-only filtration removes; a total-rock digestion may include grains excluded by a selective extraction; a sediment sample may reflect a chosen particle-size fraction. These distinctions are part of the evidence, not clerical details. Students should write units beside every column, use consistent oxidation-state and elemental nomenclature, and retain method blanks and field duplicates when the problem concerns observation quality. Chemical signatures are most convincing when a forward reaction model can explain several independent species at once.

### A unit-level map of uncertainties

Consider three layers of uncertainty before interpreting the unit's synthetic results. First are observational errors: detection limits, contamination, temperature, storage, calibration and representative sampling. Second are physicochemical model errors: activity assumptions, unknown phases, heterogeneous rates, mineral composition, open-system exchange and dependence on pressure or temperature. Third are attribution errors: several source and reaction combinations may predict similar elemental or isotopic patterns. Keeping these layers separate allows the class to decide whether better analysis, more samples or a different conceptual model is the next justified step.

## Unit learning outcomes

By the end of this unit, students should be able to name the relevant reservoirs, express governing relations with units, calculate at least one interpretable quantity, check a competing explanation, and specify what extra observation would increase confidence. The worked calculations are tightly simplified and do not constitute a validated geochemical speciation model, a professional environmental investigation or a public-health threshold determination.

## Lesson 3.1: Crystal–melt partition coefficients

### Mechanism and why it matters

The partition coefficient D is a mineral concentration divided by its coexisting melt concentration under specified conditions. Identify the named chemical phase and its exchange boundaries. Distinguish measured species totals from inferred reactions; one pattern can have several mechanisms.

### Sampling and measurement protocol

State element, mineral phase, melt composition, temperature and pressure before using a numerical D. Record phase, sampling support, date, concentration or ratio units, calibration and detection limit. Define which quantities are observed and which depend on an assumed model.

### Competing explanations and identifiability

Partition coefficients vary among minerals and conditions; using a fixed tabulated value across an evolving magma is an approximation. Specify an independently testable observation capable of distinguishing this explanation from an alternative source, reaction or laboratory bias.

### Worked numerical example — Mineral-melt coefficient

**Problem.** With D=0.4 and melt content of 80 mg/kg, compute mineral concentration.

**Mathematical setup:** `0.4*80`. After checking the listed mass, time and amount units, the calculated answer is **32 mg/kg**. Write down the inputs separately from the chosen constant or reference so an independent reviewer can recompute the result. If the expression uses a logarithm or a ratio, confirm that its argument is dimensionless; if a molar amount is involved, convert grams to moles before applying reaction coefficients. Because the values are invented for this lesson, the arithmetic demonstrates the physical scale and not a measurement-derived regional conclusion.

**Sensitivity check.** Compare the sign and magnitude with a limiting case and perturb the main input by ten percent. Report whether the relationship is linear or nonlinear, and avoid overstating numerical precision.

### Targeted investigation and practical interpretation

Compute a hypothetical mineral concentration for a known melt. Create a six-row synthetic table with inputs, predicted outputs and one replicate. Compare a rival process and document a falsifiable difference.

### Advanced reasoning: Petrogenetic scope

Trace-element models presuppose a mineral assemblage and process history. A single element is rarely diagnostic, especially if alteration, contamination, magma recharge or crystal accumulation occurred. Whenever a model fixes a partition coefficient, compare the result with another plausible coefficient and show why the conclusion depends on that assumption.

### Knowledge check and research questions


1. Recalculate the numerical example using consistent units.
2. Which competing physical process could reproduce the observation?
3. Which new measurement would discriminate the mechanisms?
4. Which assumed parameter creates the greatest model sensitivity?

**Instructor benchmark.** 32 mg/kg, conditional on the stated model and units.

## Lesson 3.2: Batch partial melting

### Mechanism and why it matters

Ideal batch melting redistributes a trace element between melt and residual solid; low bulk D creates enriched small-degree melts. Identify the named chemical phase and its exchange boundaries. Distinguish measured species totals from inferred reactions; one pattern can have several mechanisms.

### Sampling and measurement protocol

Choose a bulk partition coefficient from a declared mineral assemblage and calculate melt fraction F. Record phase, sampling support, date, concentration or ratio units, calibration and detection limit. Define which quantities are observed and which depend on an assumed model.

### Competing explanations and identifiability

A disequilibrium melting column and melting with melt extraction do not obey the same simple batch expression. Specify an independently testable observation capable of distinguishing this explanation from an alternative source, reaction or laboratory bias.

### Worked numerical example — Batch-melt concentration

**Problem.** Compute C_l=C0/[D+F(1-D)] for C0=12, D=0.05, F=0.2.

**Mathematical setup:** `12/(0.05+0.2*(1-0.05))`. After checking the listed mass, time and amount units, the calculated answer is **50 mg/kg**. Write down the inputs separately from the chosen constant or reference so an independent reviewer can recompute the result. If the expression uses a logarithm or a ratio, confirm that its argument is dimensionless; if a molar amount is involved, convert grams to moles before applying reaction coefficients. Because the values are invented for this lesson, the arithmetic demonstrates the physical scale and not a measurement-derived regional conclusion.

**Sensitivity check.** Compare the sign and magnitude with a limiting case and perturb the main input by ten percent. Report whether the relationship is linear or nonlinear, and avoid overstating numerical precision.

### Targeted investigation and practical interpretation

Estimate melt concentration using batch melting. Create a six-row synthetic table with inputs, predicted outputs and one replicate. Compare a rival process and document a falsifiable difference.

### Advanced reasoning: Petrogenetic scope

Trace-element models presuppose a mineral assemblage and process history. A single element is rarely diagnostic, especially if alteration, contamination, magma recharge or crystal accumulation occurred. Whenever a model fixes a partition coefficient, compare the result with another plausible coefficient and show why the conclusion depends on that assumption.

### Knowledge check and research questions


1. Recalculate the numerical example using consistent units.
2. Which competing physical process could reproduce the observation?
3. Which new measurement would discriminate the mechanisms?
4. Which assumed parameter creates the greatest model sensitivity?

**Instructor benchmark.** 50 mg/kg, conditional on the stated model and units.

## Lesson 3.3: Fractional crystallization

### Mechanism and why it matters

Rayleigh-style crystallization models an evolving residual melt whose composition depends on remaining melt fraction F and D. Identify the named chemical phase and its exchange boundaries. Distinguish measured species totals from inferred reactions; one pattern can have several mechanisms.

### Sampling and measurement protocol

Plot residual melt concentration against F and note that F decreases while solid accumulates. Record phase, sampling support, date, concentration or ratio units, calibration and detection limit. Define which quantities are observed and which depend on an assumed model.

### Competing explanations and identifiability

Crystal accumulation, recharge and magma mixing can generate trends similar to fractional crystallization. Specify an independently testable observation capable of distinguishing this explanation from an alternative source, reaction or laboratory bias.

### Worked numerical example — Fractional crystallization

**Problem.** C_l=C0 F^(D-1), C0=20 mg/kg, F=0.4 and D=0.3.

**Mathematical setup:** `20*0.4**(0.3-1)`. After checking the listed mass, time and amount units, the calculated answer is **37.9829 mg/kg**. Write down the inputs separately from the chosen constant or reference so an independent reviewer can recompute the result. If the expression uses a logarithm or a ratio, confirm that its argument is dimensionless; if a molar amount is involved, convert grams to moles before applying reaction coefficients. Because the values are invented for this lesson, the arithmetic demonstrates the physical scale and not a measurement-derived regional conclusion.

**Sensitivity check.** Compare the sign and magnitude with a limiting case and perturb the main input by ten percent. Report whether the relationship is linear or nonlinear, and avoid overstating numerical precision.

### Targeted investigation and practical interpretation

Compute residual melt enrichment under fixed D. Create a six-row synthetic table with inputs, predicted outputs and one replicate. Compare a rival process and document a falsifiable difference.

### Advanced reasoning: Petrogenetic scope

Trace-element models presuppose a mineral assemblage and process history. A single element is rarely diagnostic, especially if alteration, contamination, magma recharge or crystal accumulation occurred. Whenever a model fixes a partition coefficient, compare the result with another plausible coefficient and show why the conclusion depends on that assumption.

### Knowledge check and research questions


1. Recalculate the numerical example using consistent units.
2. Which competing physical process could reproduce the observation?
3. Which new measurement would discriminate the mechanisms?
4. Which assumed parameter creates the greatest model sensitivity?

**Instructor benchmark.** 37.9829 mg/kg, conditional on the stated model and units.

## Lesson 3.4: Major-element indices and mineral controls

### Mechanism and why it matters

Oxide weight percentages are compositional data, and classification indices require a stated convention and an appropriate rock type. Identify the named chemical phase and its exchange boundaries. Distinguish measured species totals from inferred reactions; one pattern can have several mechanisms.

### Sampling and measurement protocol

Check totals, iron oxidation state and whether Mg-number is defined on molar rather than mass fractions. Record phase, sampling support, date, concentration or ratio units, calibration and detection limit. Define which quantities are observed and which depend on an assumed model.

### Competing explanations and identifiability

Weathering or alteration can modify alkalis and iron and invalidate a primary-magmatic interpretation. Specify an independently testable observation capable of distinguishing this explanation from an alternative source, reaction or laboratory bias.

### Worked numerical example — Molar magnesium number

**Problem.** Compute 100 Mg/(Mg+Fe2+) for Mg=0.70 mol, Fe2+=0.30 mol.

**Mathematical setup:** `100*0.70/(0.70+0.30)`. After checking the listed mass, time and amount units, the calculated answer is **70 percent**. Write down the inputs separately from the chosen constant or reference so an independent reviewer can recompute the result. If the expression uses a logarithm or a ratio, confirm that its argument is dimensionless; if a molar amount is involved, convert grams to moles before applying reaction coefficients. Because the values are invented for this lesson, the arithmetic demonstrates the physical scale and not a measurement-derived regional conclusion.

**Sensitivity check.** Compare the sign and magnitude with a limiting case and perturb the main input by ten percent. Report whether the relationship is linear or nonlinear, and avoid overstating numerical precision.

### Targeted investigation and practical interpretation

Compute a simple molar Mg-number from atomic amounts. Create a six-row synthetic table with inputs, predicted outputs and one replicate. Compare a rival process and document a falsifiable difference.

### Advanced reasoning: Petrogenetic scope

Trace-element models presuppose a mineral assemblage and process history. A single element is rarely diagnostic, especially if alteration, contamination, magma recharge or crystal accumulation occurred. Whenever a model fixes a partition coefficient, compare the result with another plausible coefficient and show why the conclusion depends on that assumption.

### Knowledge check and research questions


1. Recalculate the numerical example using consistent units.
2. Which competing physical process could reproduce the observation?
3. Which new measurement would discriminate the mechanisms?
4. Which assumed parameter creates the greatest model sensitivity?

**Instructor benchmark.** 70 percent, conditional on the stated model and units.

## Lesson 3.5: Trace-element anomalies and petrogenetic ambiguity

### Mechanism and why it matters

Anomaly patterns are comparative signatures, not unique genetic labels; source heterogeneity and accessory minerals can dominate a trace budget. Identify the named chemical phase and its exchange boundaries. Distinguish measured species totals from inferred reactions; one pattern can have several mechanisms.

### Sampling and measurement protocol

Compare incompatible and compatible elements with uncertainty and appropriate normalization. Record phase, sampling support, date, concentration or ratio units, calibration and detection limit. Define which quantities are observed and which depend on an assumed model.

### Competing explanations and identifiability

A negative europium anomaly can reflect several mineralogical or redox histories rather than one mandatory process. Specify an independently testable observation capable of distinguishing this explanation from an alternative source, reaction or laboratory bias.

### Worked numerical example — Normalized ratio

**Problem.** If sample element ratios are 18/6 and reference ratios are 3/2, calculate double-normalized ratio.

**Mathematical setup:** `(18/6)/(3/2)`. After checking the listed mass, time and amount units, the calculated answer is **2 dimensionless**. Write down the inputs separately from the chosen constant or reference so an independent reviewer can recompute the result. If the expression uses a logarithm or a ratio, confirm that its argument is dimensionless; if a molar amount is involved, convert grams to moles before applying reaction coefficients. Because the values are invented for this lesson, the arithmetic demonstrates the physical scale and not a measurement-derived regional conclusion.

**Sensitivity check.** Compare the sign and magnitude with a limiting case and perturb the main input by ten percent. Report whether the relationship is linear or nonlinear, and avoid overstating numerical precision.

### Targeted investigation and practical interpretation

Calculate a normalized ratio and outline competing explanations. Create a six-row synthetic table with inputs, predicted outputs and one replicate. Compare a rival process and document a falsifiable difference.

### Advanced reasoning: Petrogenetic scope

Trace-element models presuppose a mineral assemblage and process history. A single element is rarely diagnostic, especially if alteration, contamination, magma recharge or crystal accumulation occurred. Whenever a model fixes a partition coefficient, compare the result with another plausible coefficient and show why the conclusion depends on that assumption.

### Knowledge check and research questions


1. Recalculate the numerical example using consistent units.
2. Which competing physical process could reproduce the observation?
3. Which new measurement would discriminate the mechanisms?
4. Which assumed parameter creates the greatest model sensitivity?

**Instructor benchmark.** 2 dimensionless, conditional on the stated model and units.

## Integrated investigation 3: Igneous processes and element partitioning capstone

('Volcanic differentiation', 'Create six synthetic lavas with fractional crystal contents and two trace elements having contrasting D values. Predict residual melt compositions for fixed-coefficient Rayleigh crystallization, then add a recharge event to produce a different fit. Plot incompatible-element enrichment and a compatible-element depletion. Explain which isotope or textural observation could separate a recharge-mixing story from a pure fractional crystallization story.')

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

1. At checkpoint 1, identify which assumptions in investigation 3 are directly tested, which still require external constraints, and how one alternative reaction or transport pathway could change the conclusion without necessarily altering the measured primary tracer. Record the expected sign of the change and the observation that would distinguish it.
2. At checkpoint 2, identify which assumptions in investigation 3 are directly tested, which still require external constraints, and how one alternative reaction or transport pathway could change the conclusion without necessarily altering the measured primary tracer. Record the expected sign of the change and the observation that would distinguish it.
3. At checkpoint 3, identify which assumptions in investigation 3 are directly tested, which still require external constraints, and how one alternative reaction or transport pathway could change the conclusion without necessarily altering the measured primary tracer. Record the expected sign of the change and the observation that would distinguish it.
4. At checkpoint 4, identify which assumptions in investigation 3 are directly tested, which still require external constraints, and how one alternative reaction or transport pathway could change the conclusion without necessarily altering the measured primary tracer. Record the expected sign of the change and the observation that would distinguish it.
5. At checkpoint 5, identify which assumptions in investigation 3 are directly tested, which still require external constraints, and how one alternative reaction or transport pathway could change the conclusion without necessarily altering the measured primary tracer. Record the expected sign of the change and the observation that would distinguish it.
6. At checkpoint 6, identify which assumptions in investigation 3 are directly tested, which still require external constraints, and how one alternative reaction or transport pathway could change the conclusion without necessarily altering the measured primary tracer. Record the expected sign of the change and the observation that would distinguish it.
7. At checkpoint 7, identify which assumptions in investigation 3 are directly tested, which still require external constraints, and how one alternative reaction or transport pathway could change the conclusion without necessarily altering the measured primary tracer. Record the expected sign of the change and the observation that would distinguish it.
8. At checkpoint 8, identify which assumptions in investigation 3 are directly tested, which still require external constraints, and how one alternative reaction or transport pathway could change the conclusion without necessarily altering the measured primary tracer. Record the expected sign of the change and the observation that would distinguish it.

## Unit 3 synthesis: claim, evidence, limitations

The correct output of a geochemical investigation is not just a fitted number. A defensible conclusion links an observation to a specific physical or chemical mechanism while making conditional assumptions explicit. In this unit, write a three-column comparison: **observed or invented data**, **quantitative model result**, and **possible geological explanation**. Any statement that relies on a presumed endmember, reference standard or equilibrium assumption belongs in the last two columns. For a stronger claim, propose observations that would separate mechanism from coincidence.

### Independent short assessment

- Choose one of the five numerical cases and reconstruct it using a different sequence of unit conversions. Confirm that the dimensions still cancel.
- Choose the most important environmental, geological or laboratory confounder from the five lessons. Explain whether it creates random scatter, systematic bias or a genuine alternative Earth process.
- Choose two variables of different spatial scales and explain why plotting them on the same grid would not establish causation.
- Write a transparent uncertainty statement: data are fictional, reference assumptions are specified, sensitivity has been tested, and a professional application requires additional measurements.

### Suggested group discussion

Compare a precise but unrepresentative measurement with a noisy but representative sampling design. The former may look more convincing in a graph yet produce a more biased inventory or flux. Discuss a case where adding more significant digits does not improve geological accuracy. Discuss whether a model with a near-perfect fit has proved its reaction pathway or merely fitted several free parameters. End by identifying one prediction not used in the original fit, and describe how a prospective measurement could potentially falsify the process model.

