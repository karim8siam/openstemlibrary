# Unit 8: Inversion, uncertainty, reproducibility and applications

## Central question: How can geophysical datasets be combined while preserving ambiguity, validation and safe intended use?

**Fictional unit investigation:** A fictional multidisciplinary survey combines gravity, magnetic, seismic, resistivity and GNSS information over a candidate infrastructure corridor. Its purpose is to rank hypotheses and new measurements, not certify foundations or predict earthquakes.

## Geophysical foundation and the measurement-to-model chain

A geophysical interpretation is a reproducible chain: raw readings, calibration, quality flags, coordinates, transformations, physical model, inversion and geological claim. At each transition uncertainty may grow, change character or become correlated. The standard least-squares objective must not become a substitute for science; regularization encodes prior preferences and sensitivity depends on parameter scaling. Synthetic recovery and checkerboard experiments are useful but can create false reassurance because inverse crime tests reuse the same forward assumptions. Withheld stations, alternative physics and independent geological information provide stronger checks. Communicate resolution gaps, alternative models and use restrictions to downstream readers.

## Five lessons: hypotheses, observables and field checks

For each lesson the forward physics and observation type are explicit. The lesson is complete only when the student can name a competing explanation, check units in the worked calculation and explain a measurement that could reject the preferred interpretation. Every stated numerical value is invented for this textbook; none is a field station or an operational parameter.

## Lesson 8.1: Designing geophysical surveys

### The physical mechanism and its measurable consequence

Survey design begins with a falsifiable target, expected signal amplitude, depth, wavelength, environment and minimum detectable difference. Sensor choice follows target physics rather than the reverse. Coverage, access, licensing and safety change whether an ideal sampling grid is achievable.

### Acquisition protocol and observable variables

Build a matrix of methods, physical properties, target sensitivity, noise sources, cost and achievable coverage. Document why some methods were rejected.

### The inverse ambiguity: alternative explanations

An expensive high-resolution dataset may still be uninformative if its measurement physics is unrelated to the target. Dense sampling does not cure systematic model bias.

### Worked calculation: synthetic classroom data

**Question — Reduced chi-square illustration.** Four squared normalized residuals total 12 and 2 degrees of freedom remain; calculate reduced statistic.

**Explicit computation:** `12/2` = **6 ratio**. Express the result in the units requested; perform any conversion before substituting into the equation rather than concealing a factor of one thousand in a final sentence. A rounded answer should not imply accuracy better than the synthetic inputs. This arithmetic operation provides a physical scale, not a certified subsurface interpretation.

**Why the calculation matters.** Relative misfit scale can be used diagnostically. **Boundary of validity:** It assumes correct noise model and independence. For an independent sensitivity check, change one stated input by ten percent, leaving others fixed. Explain how the result responds, and whether a plausible alternative hypothesis could produce the same scalar.

### Practical: an observation that could disprove the preferred model

Create a budget-neutral redesign that replaces half the stations with independent validation points and compare expected information gain.

**Sensitivity study.** Alter the assumed physical-property contrast, source depth or acquisition spacing. Determine whether the sign of the conclusion persists or whether the interpretation is contingent on a narrow prior. Draw a table containing at least two testable predictions, the needed instrument reading, its physical units, and one reason the observation might be biased.

### Analysis note: how to decide whether the interpretation survives

**Inspect the observation footprint.** Ask which wavelengths and parts of the Earth contribute to the instrument. Potential fields integrate over substantial volumes, seismic picks follow ray paths and electrode arrays have diffuse sensitivity; a pixel-sized interpretation usually exceeds the resolving claim. In the context of **designing geophysical surveys**, explain what a reviewer should expect to see in raw data if the mechanism is credible, and what unexpected pattern would require a revised geological model.

### Synthesis and interpretation checkpoint

Write a short technical conclusion that separates three items: (1) what the instrument directly records in the inversion, uncertainty, reproducibility and applications problem; (2) the material property or process inferred from it; and (3) a geological claim that would still be unsupported. The exercise is not passed merely by obtaining 6 ratio. Explain why the uncertainty in the assumptions can exceed calculator precision and identify a discriminating field observation.

## Lesson 8.2: Likelihoods, priors and regularization

### The physical mechanism and its measurable consequence

A simple least-squares solution assigns a residual penalty that depends on noise assumptions and weights. Geological priors and smoothness or sparsity constraints select particular members of a model family. Regularization is not a physical law and must be reported as a methodological choice.

### Acquisition protocol and observable variables

Inspect residual distribution, spatial correlation, misfit versus model complexity and dependence on initial conditions. Generate several admissible solutions.

### The inverse ambiguity: alternative explanations

Model uncertainty can remain huge even when a formal covariance estimate is small under fixed prior assumptions. Equal rms need not imply equal predictive skill.

### Worked calculation: synthetic classroom data

**Question — Holdout improvement.** Prediction errors change from 12 to 9 mGal; compute percent reduction.

**Explicit computation:** `100*(12-9)/12` = **25 %**. Express the result in the units requested; perform any conversion before substituting into the equation rather than concealing a factor of one thousand in a final sentence. A rounded answer should not imply accuracy better than the synthetic inputs. This arithmetic operation provides a physical scale, not a certified subsurface interpretation.

**Why the calculation matters.** Reduced holdout error supports, but does not prove, prediction improvement. **Boundary of validity:** Holdout data must be independent of model tuning. For an independent sensitivity check, change one stated input by ten percent, leaving others fixed. Explain how the result responds, and whether a plausible alternative hypothesis could produce the same scalar.

### Practical: an observation that could disprove the preferred model

Construct a two-parameter problem with a curved trade-off valley, then test how a prior on one parameter changes the inferred other parameter.

**Blind crosscheck.** Give the input series and quality flags to another analyst while hiding the preferred interpretation. Compare their residual and inferred structure with the original and preserve genuine disagreements. Draw a table containing at least two testable predictions, the needed instrument reading, its physical units, and one reason the observation might be biased.

### Analysis note: how to decide whether the interpretation survives

**State the forward equation and its domain.** Write the physical equation together with geometry, units and assumed constants. List a realistic departure that changes the prediction and distinguish a useful approximation from an unjustified physical claim. In the context of **likelihoods, priors and regularization**, explain what a reviewer should expect to see in raw data if the mechanism is credible, and what unexpected pattern would require a revised geological model.

### Synthesis and interpretation checkpoint

Write a short technical conclusion that separates three items: (1) what the instrument directly records in the inversion, uncertainty, reproducibility and applications problem; (2) the material property or process inferred from it; and (3) a geological claim that would still be unsupported. The exercise is not passed merely by obtaining 25 %. Explain why the uncertainty in the assumptions can exceed calculator precision and identify a discriminating field observation.

## Lesson 8.3: Cross-validation and resolving power

### The physical mechanism and its measurable consequence

A forward-recovery test measures how a chosen inverse procedure performs on a defined synthetic world. It is easier than predicting independent field observations because the simulated truth may share identical assumptions with inversion. Withholding adjacent stations can leak spatially correlated information.

### Acquisition protocol and observable variables

Withhold an entire independent line or station cluster and measure predictive error in physical units. Repeat under more than one noise model.

### The inverse ambiguity: alternative explanations

A checkerboard inversion can look excellent at the cells chosen by the analyst while poorly resolving a geological body with realistic geometry.

### Worked calculation: synthetic classroom data

**Question — Joint weighted misfit.** Gravity residual/σ=2, magnetic residual/σ=3; calculate sum of squares.

**Explicit computation:** `2**2+3**2` = **13 ratio**. Express the result in the units requested; perform any conversion before substituting into the equation rather than concealing a factor of one thousand in a final sentence. A rounded answer should not imply accuracy better than the synthetic inputs. This arithmetic operation provides a physical scale, not a certified subsurface interpretation.

**Why the calculation matters.** Normalized residuals combine only under specified weights. **Boundary of validity:** Correlated errors and incompatible support may invalidate simple sum. For an independent sensitivity check, change one stated input by ten percent, leaving others fixed. Explain how the result responds, and whether a plausible alternative hypothesis could produce the same scalar.

### Practical: an observation that could disprove the preferred model

Compare random-point withholding against whole-line withholding and explain why the latter can be the stronger test.

**Instrument validation.** Compare a repeat transect, crossing line or reciprocal reading with original acquisition. Explain what kind of systematic effect the check is capable of detecting and what remains invisible. Draw a table containing at least two testable predictions, the needed instrument reading, its physical units, and one reason the observation might be biased.

### Analysis note: how to decide whether the interpretation survives

**Decide a safe intended use.** Clarify whether the result is a numerical exercise, exploratory screening, academic interpretation or professional decision product. Educational calculations do not confer authority to make engineering, emergency or environmental determinations. In the context of **cross-validation and resolving power**, explain what a reviewer should expect to see in raw data if the mechanism is credible, and what unexpected pattern would require a revised geological model.

### Synthesis and interpretation checkpoint

Write a short technical conclusion that separates three items: (1) what the instrument directly records in the inversion, uncertainty, reproducibility and applications problem; (2) the material property or process inferred from it; and (3) a geological claim that would still be unsupported. The exercise is not passed merely by obtaining 13 ratio. Explain why the uncertainty in the assumptions can exceed calculator precision and identify a discriminating field observation.

## Lesson 8.4: Multi-physics integration and contradictions

### The physical mechanism and its measurable consequence

Density, velocity, conductivity, magnetization, temperature and deformation depend on partly overlapping but nonidentical geology. Combined interpretation is strongest when disagreements trigger investigation, not when every dataset is coerced into one narrative.

### Acquisition protocol and observable variables

Display data provenance, coordinate system, resolution, sensitivity and error next to each map. Predict uncollected observations from each geological interpretation.

### The inverse ambiguity: alternative explanations

Hard petrophysical constraints may force incorrect convergence; two geophysical datasets with the same shared inversion prior are not independent verification.

### Worked calculation: synthetic classroom data

**Question — Metadata completeness.** A survey has 22 required reproducibility fields and 19 documented; calculate completion percent.

**Explicit computation:** `100*19/22` = **86.36364 %**. Express the result in the units requested; perform any conversion before substituting into the equation rather than concealing a factor of one thousand in a final sentence. A rounded answer should not imply accuracy better than the synthetic inputs. This arithmetic operation provides a physical scale, not a certified subsurface interpretation.

**Why the calculation matters.** Documentation metric can identify omissions. **Boundary of validity:** A missing coordinate datum matters more than many trivial fields. For an independent sensitivity check, change one stated input by ten percent, leaving others fixed. Explain how the result responds, and whether a plausible alternative hypothesis could produce the same scalar.

### Practical: an observation that could disprove the preferred model

Present two conflicting cross-sections and rank which independent sample or method would settle the disagreement with least disturbance.

**Physical sanity test.** Evaluate the model at an extreme but admissible input and check dimensions, sign, limiting behaviour and plausibility. A correct arithmetic result with a broken physical assumption is not a sound geological conclusion. Draw a table containing at least two testable predictions, the needed instrument reading, its physical units, and one reason the observation might be biased.

### Analysis note: how to decide whether the interpretation survives

**Track the reference frame.** Coordinates, vertical datums, event origin times, magnetic epochs and polarity conventions are parts of the measurement. Confusing reference frames can shift all stations coherently without producing conspicuous random residuals. In the context of **multi-physics integration and contradictions**, explain what a reviewer should expect to see in raw data if the mechanism is credible, and what unexpected pattern would require a revised geological model.

### Synthesis and interpretation checkpoint

Write a short technical conclusion that separates three items: (1) what the instrument directly records in the inversion, uncertainty, reproducibility and applications problem; (2) the material property or process inferred from it; and (3) a geological claim that would still be unsupported. The exercise is not passed merely by obtaining 86.36364 %. Explain why the uncertainty in the assumptions can exceed calculator precision and identify a discriminating field observation.

## Lesson 8.5: Ethics, communication and field limitations

### The physical mechanism and its measurable consequence

Geophysical maps can influence public safety, property, environmental management and exploration. An attractive synthetic image may be mistaken for measured truth if labels are hidden. Real seismic, utility and subsurface work requires permissions and professional standards.

### Acquisition protocol and observable variables

Maintain provenance, accessible uncertainty explanations, public-impact review and responsible data-handling records. Mark synthetic stations and forbid operational use of teaching outputs.

### The inverse ambiguity: alternative explanations

Results may be abused when a filtered lineament is sold as a safe-building assessment, mineral resource estimate or earthquake prediction. No single classroom metric supports those claims.

### Worked calculation: synthetic classroom data

**Question — Survey coverage.** A regional survey has 18 lines each 5 km long; compute the total straight-line distance.

**Explicit computation:** `18*5` = **90 km**. Express the result in the units requested; perform any conversion before substituting into the equation rather than concealing a factor of one thousand in a final sentence. A rounded answer should not imply accuracy better than the synthetic inputs. This arithmetic operation provides a physical scale, not a certified subsurface interpretation.

**Why the calculation matters.** Length is a useful survey planning quantity. **Boundary of validity:** Turnaround, line overlap and usable acquisition fractions are excluded. For an independent sensitivity check, change one stated input by ten percent, leaving others fixed. Explain how the result responds, and whether a plausible alternative hypothesis could produce the same scalar.

### Practical: an observation that could disprove the preferred model

Draft a two-paragraph public explanation distinguishing measurements, scenarios, possible models, consequences and decisions requiring qualified review.

**Data stewardship.** Document synthetic status, provenance, coordinates, units, processing version, license and intended use. Keep measurements in a separate file from interpolated or inversion-derived quantities. Draw a table containing at least two testable predictions, the needed instrument reading, its physical units, and one reason the observation might be biased.

### Analysis note: how to decide whether the interpretation survives

**Use a withheld test.** Fit the parameters with one subset and predict genuinely unobserved measurements. Spatial clustering, repeated use of validation stations or tuning after inspecting the holdout exaggerates predictive evidence. In the context of **ethics, communication and field limitations**, explain what a reviewer should expect to see in raw data if the mechanism is credible, and what unexpected pattern would require a revised geological model.

### Synthesis and interpretation checkpoint

Write a short technical conclusion that separates three items: (1) what the instrument directly records in the inversion, uncertainty, reproducibility and applications problem; (2) the material property or process inferred from it; and (3) a geological claim that would still be unsupported. The exercise is not passed merely by obtaining 90 km. Explain why the uncertainty in the assumptions can exceed calculator precision and identify a discriminating field observation.

## Research clinic — trustworthy inversion as a decision process

A typical geophysical inversion minimizes a weighted data-misfit term combined with some model penalty. The weights reflect believed measurement uncertainty, while the regularization expresses prior preference for smoothness, smallness or sparsity. This can be defensible, but the chosen answer inherits both the measurement model and the prior. Do not describe a regularized output as a direct observation of rock type. Provide the actual measurement fit, sensitivity and alternative acceptable models alongside the preferred cross-section.

Consider a fictional infrastructure corridor where a gravity low and resistivity high overlap. A naive interpreter may claim a dry sedimentary basin; another may claim a low-density rock with minimal pore fluid. Seismic velocity and targeted geological samples could distinguish these, but only if the petrophysical link is justified. Joint inversions can be overconfident when they enforce a hard density–velocity relation that is not observed locally. Where physical properties disagree, the disagreement can signal a wrong model or a scientifically interesting heterogeneity.

Validation should predict genuinely withheld observations. Randomly withholding neighbouring stations is weak in autocorrelated fields, because nearby training readings nearly reveal the test values. Withhold an entire line or a geographically separated cluster. Re-run with altered regularization, noise scale and starting model; compare predicted data in measured physical units. A perfect checkerboard recovery under identical synthetic forward and inverse assumptions is not proof of real-world resolving power.

Communication requires a readable uncertainty ledger and an intended-use boundary. Explain which arrays were simulated, which raw readings were collected, which transformations were applied, and which interfaces were inferred. Maps for classroom exercises must not be used to judge earthquake risk, buried utilities, dam foundations or mineable resources. If a public-facing visualization is more persuasive than the underlying evidence permits, redesign the legend so unsupported certainty is impossible to miss.


## Unit investigation: reproducible synthetic dataset and experimental design

**Research aim.** The invented scenario is: A fictional multidisciplinary survey combines gravity, magnetic, seismic, resistivity and GNSS information over a candidate infrastructure corridor. Its purpose is to rank hypotheses and new measurements, not certify foundations or predict earthquakes. Treat `datasets/unit-08.csv` as forty fictional rows deliberately designed to exercise quality control and model criticism. Read the file header before drawing any map. Plot the two relevant measured fields from unit 8; display the `quality_flag` column rather than deleting all flagged stations silently. The synthetic table contains no geographic coordinate reference system or real site identifiers and cannot be used to identify a place.

**Part A — raw measurements and dimensions.** Read each column as a quantity, not as a decorative label. For inversion, uncertainty, reproducibility and applications, check whether the stated units are compatible with its equation and record which columns represent observed signals, instrument corrections, independent controls or model-derived quantities. Identify missing information such as date, site geology, true coordinate system, instrument orientation or calibration. If those omissions prevent a physical inversion, state the limitation and limit the task to transparent exploratory analysis. This is a stronger result than assigning fictitious precision.

**Part B — repeat and quality flags.** Count the rows marked `review`. Compare summary statistics, plotted gradients and model parameters with all forty records against the subset that passes the flag. Document every change; flags indicate inspection priority, not a universal mandate to delete. Check whether questionable values cluster along position or signal amplitude, because exclusions can introduce bias. If the noise appears correlated, do not assume a root-sum-square independent-error formula without a justification.

**Part C — model competition.** Describe two geophysical models that explain the synthetic observations in inversion, uncertainty, reproducibility and applications; they must differ in physical property, geometry or forcing rather than just parameter precision. For each hypothesis make an observable prediction about station response, uncertainty pattern, external control or independent method. Select one new measurement that would best discriminate them, and explain its predicted signal under both hypotheses. A new dense sample from the same short profile may add less independent information than a crossing line or sample.

**Part D — numerical sensitivity.** Recompute one of the unit worked cases with the principal input increased by 10% and decreased by 10%. Check if the response is linear, inverse, logarithmic, quadratic or subject to another nonlinearity. Show a table with input, computed output, unit and physical assumption. Do not claim a sensitivity of the geological interpretation itself if only the toy forward equation was changed; the inverse solution may have a much broader family of possibilities.

**Part E — out-of-sample prediction and reporting.** Split the synthetic observations by physical position, retaining a contiguous group as a blind holdout. Fit a deliberately simple forward trend to remaining rows and predict the held-out quantity without retuning. Compare predictive error with a baseline that uses a constant mean. State why geographic separation can be a stronger test than random point withholding. Report all transformations, quality flags, fitted parameters, residual plots and failure modes in a compact methods appendix.

**Unit-specific evidence synthesis.** A geophysical interpretation is a reproducible chain: raw readings, calibration, quality flags, coordinates, transformations, physical model, inversion and geological claim. At each transition uncertainty may grow, change character or become correlated. The standard least-squares objective must not become a substitute for science; regularization encodes prior preferences and sensitivity depends on parameter scaling. Synthetic recovery and checkerboard experiments are useful but can create false reassurance because inverse crime tests reuse the same forward assumptions. Withheld stations, alternative physics and independent geological information provide stronger checks. Communicate resolution gaps, alternative models and use restrictions to downstream readers. Map the chain of evidence from sensor to interpretation; highlight an uncertainty not reducible by extra decimal places. In your conclusion, indicate which measurement you would acquire next if the synthetic experiment were replaced with licensed real-world data. Keep any real data sourced from the references separate from these forty invented rows.

**Suggested report.** Submit a transparent CSV-reading script or spreadsheet calculation, one raw-data figure, a sensitivity plot, two candidate geological explanations, a withheld-test result and a one-page uncertainty ledger. Grade on conceptual correctness (25%), numerical units and reproducibility (25%), alternate hypotheses (20%), validation logic (20%) and scientific communication (10%). Never reward a map for appearing more certain than its underlying observations.

## End-of-unit reflection and problems

1. Identify which part of **inversion, uncertainty, reproducibility and applications** would remain ambiguous even if measurement noise were reduced to zero. Explain how the survey geometry or parameter relationship creates that ambiguity.

2. Find a case where a large change in the observed signal would not imply a proportionally large change in target size. Write the forward relation, name fixed parameters, and state why inversion differs from prediction.

3. Propose a new survey that would risk rejecting the preferred geological interpretation. Its value should be based on discriminating predictions rather than its technological sophistication.

4. Draw a data lineage chart from raw instrument data through correction, inversion and geological claim. Underline any operation that assumes a material property not measured in the original dataset.

5. Explain why the synthetic data and interactive sliders are educational examples and cannot support emergency warnings, ground-investigation certification, resource appraisal or environmental enforcement.

## Additional reading and independent replication

Use `REFERENCES.md` to find a genuine program or open repository relevant to inversion, uncertainty, reproducibility and applications. Before downloading any data, check the provider documentation, citation requirements, usage permissions and the time period represented. Record the instrument type, station metadata and acquisition geometry, then reproduce one simple physical calculation from scratch. The objective is not to match a published colored inversion image exactly; it is to understand the observable and give a defensible account of differences.


## Interactive physical-model explanations

Open this chapter in the HTML reader to change one controlled physical variable at a time. Each model is a simplified *forward* calculation, not an inversion or a real-world estimator.

### Normalized least-squares misfit

Input quantity: Second normalized residual measured in standard deviations; demonstration range 0–5, initial setting 3. Output: ratio. Computed from `4+x*x`.

**Unmodelled influences and interpretation boundary:** Assumes one fixed normalized residual of 2 and independent standard errors. Students should articulate a case where this formula yields a numerically precise but physically misleading answer and state an independently measurable quantity needed for a more complete model.

### Prediction error reduction

Input quantity: New holdout error measured in mGal; demonstration range 2–12, initial setting 9. Output: %. Computed from `100*(12-x)/12`.

**Unmodelled influences and interpretation boundary:** Baseline prediction error fixed 12 mGal; no confidence interval. Students should articulate a case where this formula yields a numerically precise but physically misleading answer and state an independently measurable quantity needed for a more complete model.
