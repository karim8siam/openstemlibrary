# Unit 8: Integration, modeling, ethics and reproducible marine geology

## Guiding question: How can multiple imperfect data streams be combined into defensible geological decisions?

**Synthetic case:** A class assembles a regional marine geological atlas from synthetic sonar, core, magnetics, samples and acoustic stratigraphy. Conflicting interpretations are expected. The final deliverable is a reproducible evidence table, uncertainty map, conservative recommendation and explicit list of unresolved questions.

## Geological framework: questions, scales and competing evidence

Regional synthesis links depth, acoustic stratigraphy, geophysics, core data and geological reasoning, yet joint models often have many acceptable solutions. A simple model is useful when it makes its assumptions visible, predicts observables and suggests a test that could reject it. Cross-validation must guard against geographic leakage: withholding neighbouring points is less demanding than withholding an entire survey line. Data release requires raw versions, processing records, sample identifiers, controlled units, coordinate systems and permission information. Research communication must mark unknown areas, make limitations easy to find and state explicitly when a model is educational only. A map’s persuasive visual polish must never outrun the quality of its underlying evidence.

## Five lessons with evidence notebooks

Each lesson joins a physical principle, an observable, a competing explanation, and a quantified classroom calculation. A numerical result is conditional on the stated synthetic inputs. Details such as local hazard probability, legal extraction requirements or physical-property inversion cannot be derived from the simple cases.

## Lesson 8.1 — Marine benthic habitats and geodiversity

### Geological principle: what produces the pattern?

Rock type, sediment grain size, relief, flow and geochemical flux help structure benthic habitats. Geological maps can provide habitat predictors but cannot substitute for direct biological observation.

### Observation plan: what is actually measured?

Integrate substrate imagery, seabed samples, bathymetric roughness, currents and independent biological transects. Validate ecological class predictions with spatially separated observations.

### Alternative hypotheses and what would refute them

A backscatter class is not a species map. Geological associations are scale-dependent, and rare habitats can be missed by grid averages or opportunistic sampling.

### Worked numerical investigation

**Synthetic problem — Benthic relief metric.** Three adjacent elevations differ by 8 m over 400 m distance; compute percent gradient.

**Equation and substitution:** `100*8/400`. The computed answer is **2 %**. The units in the input determine the units in the answer. Check the dimensional conversion before interpreting a scalar as a geological quantity. A physically meaningful result should also be examined at a second parameter value to determine whether the trend makes sense.

**Interpretation:** A local terrain metric may help identify substrate and flow contrasts. **What this does not establish:** Slope depends on sampling baseline and cannot uniquely map biological diversity.

### A focused field or laboratory investigation

Prepare a habitat-linked geologic sensitivity map without turning it into an unsupported regulatory impact assessment.

**Design choice:** Audit an inference chain. Write the chain from raw sensor or sample to computed quantity, derived feature and geological explanation. At each arrow name an assumption and a calibration record. If any arrow cannot be supported, retain a provisional descriptive label instead of forcing an unverified genetic classification.

## Lesson 8.2 — Integrated marine survey design

### Geological principle: what produces the pattern?

A survey should be designed backwards from a testable question, required spatial scale and tolerance for uncertainty. Adaptive sampling can improve coverage of ambiguous features but also introduce selection bias if exploratory findings are treated as confirmatory.

### Observation plan: what is actually measured?

Construct a survey matrix linking each target feature to instrument, location accuracy, resolution, quality control, sampling coverage and expected decision. Reserve calibration lines and independent validation samples.

### Alternative hypotheses and what would refute them

More observations are not automatically better: duplicated tracks can overrepresent accessible zones, and sensor precision cannot repair an incorrect geological conceptual model.

### Worked numerical investigation

**Synthetic problem — Survey coverage.** A multibeam swath is 2.5 km wide and an effective on-line survey distance is 72 km; find nominal mapped area.

**Equation and substitution:** `2.5*72`. The computed answer is **180 km²**. The units in the input determine the units in the answer. Check the dimensional conversion before interpreting a scalar as a geological quantity. A physically meaningful result should also be examined at a second parameter value to determine whether the trend makes sense.

**Interpretation:** Swath width times line distance describes gross coverage. **What this does not establish:** Overlap, gaps and unusable beams reduce effective independent coverage.

### A focused field or laboratory investigation

Compare two survey budgets in fictional instrument-hours and identify the design that best reduces uncertainty in the stated scientific decision.

**Design choice:** Design a disconfirming observation. Suppose the leading geological hypothesis is wrong. Which new sample, repeat transect or independent instrument would most readily reveal the mistake? Prefer high-information contrasts over uniformly increasing sample counts; explicitly discuss how limited ship time changes the geographic representativeness of the result.

## Lesson 8.3 — Joint inversion and competing geological models

### Geological principle: what produces the pattern?

Potential-field data, seismic velocity, bathymetry and samples can constrain subsurface structure, but inverse problems often admit many models. Geological plausibility and independent data can reduce ambiguity, not abolish it.

### Observation plan: what is actually measured?

Report model parameterization, priors, resolution tests, forward prediction residuals and out-of-sample checks. Display at least two structurally distinct models that fit the observational errors.

### Alternative hypotheses and what would refute them

A small least-squares residual does not prove the inferred rock distribution. Regularization choices may determine smoothness and parameter trade-offs more strongly than the observations.

### Worked numerical investigation

**Synthetic problem — Weighted seismic misfit.** Observed travel times differ from predicted by 0.02, -0.03, 0.01 s with common σ=0.02 s; compute sum of squared normalized errors.

**Equation and substitution:** `(0.02/0.02)**2+(-0.03/0.02)**2+(0.01/0.02)**2`. The computed answer is **3.5 dimensionless**. The units in the input determine the units in the answer. Check the dimensional conversion before interpreting a scalar as a geological quantity. A physically meaningful result should also be examined at a second parameter value to determine whether the trend makes sense.

**Interpretation:** Chi-square-style misfit is conditional on the claimed noise scale. **What this does not establish:** The residuals may be correlated and model complexity matters.

### A focused field or laboratory investigation

Perturb a model prior, compare predicted fields and describe which future measurement would most efficiently separate the surviving interpretations.

**Design choice:** Inspect sensitivity to processing. Imagine regridding an acoustic field, changing a lithology classification threshold or revising one age control. Determine which apparent geological boundary persists and which vanishes. Report a stable core of interpretation as well as the disputed region, rather than selecting the single map with the neatest outlines.

## Lesson 8.4 — Marine geospatial statistics and uncertainty propagation

### Geological principle: what produces the pattern?

Marine data have spatial clustering, anisotropy, unequal support and instrument-specific bias. Uncertainty propagation should reflect covariance and calibration uncertainty rather than adding independent errors by assumption.

### Observation plan: what is actually measured?

Use cross-validation grouped by cruise track or region. Keep a measurement uncertainty table and test sensitivity to interpolation method, grid spacing and outlier handling.

### Alternative hypotheses and what would refute them

Randomly splitting neighboring samples across training and test sets can overstate predictive skill. Coarse maps may hide a hazard smaller than a grid cell even when average residuals look modest.

### Worked numerical investigation

**Synthetic problem — Independent-error propagation.** Two independent Gaussian depth uncertainties are 3 m and 4 m; find root-sum-square uncertainty.

**Equation and substitution:** `math.sqrt(3**2+4**2)`. The computed answer is **5 m**. The units in the input determine the units in the answer. Check the dimensional conversion before interpreting a scalar as a geological quantity. A physically meaningful result should also be examined at a second parameter value to determine whether the trend makes sense.

**Interpretation:** Quadrature assumes uncorrelated errors in the same measured dimension. **What this does not establish:** Systematic datum shifts require separate treatment.

### A focused field or laboratory investigation

Run a fictional leave-one-transect-out validation and compare it with random point holdout, explaining the differences in expected optimism.

**Design choice:** Separate event from background. Estimate whether a measured layer or acoustic feature records a short-lived high-intensity event or the integration of many smaller processes. A process can dominate preserved sediment while occupying little elapsed time. Search for event boundaries, independent dates and reworked materials before extending the inference beyond one location.

## Lesson 8.5 — Reproducible cores, archives and metadata

### Geological principle: what produces the pattern?

Reproducibility requires retaining raw observations, instrument settings, calibration, sample provenance, units, code versions and documented transformations. A published map without this information may be impossible to revisit when new evidence appears.

### Observation plan: what is actually measured?

Package a machine-readable station table, file checksums, explicit coordinate system, calibration and processing logs, and a methods narrative. Link core images and stratigraphic interpretations to the same depth reference.

### Alternative hypotheses and what would refute them

Converting non-detections to zeros, changing core depth without a crosswalk or dropping poor-quality observations silently can bias subsequent synthesis. Metadata omissions may matter more than plotting aesthetics.

### Worked numerical investigation

**Synthetic problem — Metadata completeness.** A data release has 18 required metadata fields and fills 15; find completeness.

**Equation and substitution:** `100*15/18`. The computed answer is **83.333 %**. The units in the input determine the units in the answer. Check the dimensional conversion before interpreting a scalar as a geological quantity. A physically meaningful result should also be examined at a second parameter value to determine whether the trend makes sense.

**Interpretation:** A percentage can help triage documentation gaps. **What this does not establish:** All fields are not of equal consequence; missing datum or licensing is critical.

### A focused field or laboratory investigation

Audit a synthetic archive for missing fields, draft a versioned correction log and provide a minimal reproducibility checklist that another student can follow.

**Design choice:** Apply a conservation or kinematic constraint. Define what enters and leaves the chosen region, and distinguish a material inventory from a flux. Where the subject is tectonic rather than depositional, check whether distances, ages and rate units are consistent. A residual indicates something unmeasured or a violated assumption; it does not automatically verify a preferred mechanism.

### Research deep dive: designing an atlas that cannot hide the unknown

An integrated regional atlas may combine global bathymetry, multibeam soundings, magnetics, sub-bottom profiles, cores and sedimentological classifications. These layers were often acquired in different years, with different datums and at different spatial scales. Start with a provenance matrix. For every dataset record the cruise or repository, acquisition method, coordinate system, vertical reference, resolution, uncertainty and exact use permission. Do not silently fill unknown fields by copying metadata from another source.

An inverse geological model can fit the same geophysical observations with more than one subsurface structure. For instance, a gravity anomaly may result from a thin dense body or a deeper larger body. A low-residual fit can be achieved under many competing priors. To evaluate models, hold out observations at spatially separated locations and test forward predictions. If the result changes substantially when regularization strength is adjusted, present the range as geological non-uniqueness instead of selecting the single optimal image.

Geological maps are communication tools, so design is part of epistemic quality. Use visually distinct layers for measured points, interpreted boundaries and unconstrained zones; do not use identical strong colours for all three. Provide a legend explaining whether contours are interpolated and whether a sample genuinely penetrated the interpreted unit. Caption every figure with units, dataset age and processing version. A student should be able to reconstruct the argument without contacting the original analyst for missing parameters.

Before publishing an atlas, run a reproducibility test from a fresh folder with no internet connectivity. Can another researcher open the raw tables, run the calculation and obtain the same plots? Do all local navigation links work? Are quality flags exposed? Does the summary explicitly say the stations and cases were fabricated? Finally, distinguish an initial scientific screening product from a regulatory, engineering or emergency service. A carefully documented uncertain map is a more responsible contribution than a misleadingly certain one.

## Unit investigation: linking map, core and mechanism

**Aim.** Use the forty synthetic stations in `datasets/unit-08.csv` to test a question involving integration, modeling, ethics and reproducible marine geology. Treat the CSV as invented material for practicing statistical quality control, not as an actual seabed dataset. Plot water depth and acoustic sediment thickness along the transect; add markers for the `review` flags and record how the conclusions change after excluding them. The along-track separation is a schematic distance, not latitude or longitude, and therefore cannot establish the orientation or full area of a geological body.

**Background synthesis.** Regional synthesis links depth, acoustic stratigraphy, geophysics, core data and geological reasoning, yet joint models often have many acceptable solutions. A simple model is useful when it makes its assumptions visible, predicts observables and suggests a test that could reject it. Cross-validation must guard against geographic leakage: withholding neighbouring points is less demanding than withholding an entire survey line. Data release requires raw versions, processing records, sample identifiers, controlled units, coordinate systems and permission information. Research communication must mark unknown areas, make limitations easy to find and state explicitly when a model is educational only. A map’s persuasive visual polish must never outrun the quality of its underlying evidence.

**Design brief.** A class assembles a regional marine geological atlas from synthetic sonar, core, magnetics, samples and acoustic stratigraphy. Conflicting interpretations are expected. The final deliverable is a reproducible evidence table, uncertainty map, conservative recommendation and explicit list of unresolved questions. Specify one observation that you expect to see if your mechanism is correct and a different one expected under a plausible alternative. Identify three layers of evidence: a survey observation, a physical sample, and a geophysical or chronologic constraint. Give each evidence layer a separate confidence score and justification. Do not average those scores unless their dependence is explicitly justified. Two products derived from the same ship track are not fully independent corroboration.

**Procedure, Part A — reconstruct what was measured.** Load the CSV and confirm that depth, thickness and size values are positive where expected. Calculate the smallest and largest water depths, the range of recovered thicknesses, and the number of flagged rows. Make two alternative maps: one preserving all points with quality flags visible, another excluding flagged stations. Label this contrast a sensitivity study. The second view should not be automatically judged more correct; removal can itself bias the spatial pattern if poor observations cluster in difficult terrain.

**Procedure, Part B — inspect model dependency.** Examine the plotted gradient at an interval of two, five and ten stations, and identify which short features are averaged away. Estimate a simple slope in metres per kilometer using a defined pair of samples. State whether this is a geometric seabed slope or a sediment thickness gradient; the distinction affects interpretation. If you attempt uncertainty propagation, specify assumed error correlations rather than selecting a root-sum-square formula by habit.

**Procedure, Part C — compare competing histories.** Write two plausible geological narratives that fit the synthetic pattern. One should emphasize a structural or long-timescale explanation; the other should emphasize deposition, redistribution or erosional overprinting where meaningful. List predictions that differ: reflector geometry, sediment type, age ordering, fault offsets, pore-fluid signals or mineralogical provenance. Rank possible next observations by ability to distinguish those predictions, not by how dramatic their imagery would look.

**Procedure, Part D — communicate limitations.** Prepare a four-panel reproducible report: data provenance, primary measurement plot, competing explanation diagram and uncertainty ledger. In the ledger, list unknown vertical datum, unrealistically simplified synthetic values, unmeasured lithology, timing uncertainty and any relevant instrument bias. Explicitly describe which claims the report cannot make. For marine hazards, resource assessment and navigational uses, do not substitute this exercise for official data or specialist review.

**Deliverables and grading:** 20% clean reproducible analysis, 20% physically coherent interpretations, 20% alternative hypotheses, 20% quantitative unit and sensitivity checks, and 20% uncertainty communication. A technically polished visualization that hides the fact that the data are synthetic cannot receive full credit. Submit the processing steps, plots, an evidence matrix and a revision note explaining which conclusion changed after reviewing uncertainties.

## Unit assessment: reasoning rather than memorization

**Question A:** Design a way to disprove the leading hypothesis for integration, modeling, ethics and reproducible marine geology while spending no more than two new stations on the fictional cruise. Justify each station by the predicted difference between models.

**Question B:** Explain how an erroneous vertical datum, poor coring recovery, or inappropriate age tie point would affect at least two of the results presented in this unit. Distinguish changed numerical answers from changed geological conclusions.

**Question C:** Propose a figure caption for an unfamiliar scientific reader. It must name what was measured, the units, geographic or stratigraphic coverage, important transformations, and one explicit limitation.

**Question D:** Choose one of the unit models and identify which environmental or geological variable is intentionally held constant. Explain how failure of that constant would change the interpretation but not necessarily invalidate the model as a teaching aid.

## Further investigation and practical extension

To extend the fictional unit project into real research, start with the references and select a genuine open dataset with clear acquisition date, license, method, processing version and coordinate reference system. For integration, modeling, ethics and reproducible marine geology, seek at least one direct measurement that does not originate from the same inversion as the map. Compare two spatial resolutions before discussing morphology. Keep real observations strictly separated from the invented training CSV. A reproducible report should link each plotted feature to a raw record, show how missing values were handled, and make failed interpretations visible rather than deleting them from the final narrative.


## Interactive models accompanying Unit 8

Open the HTML chapter to move the sliders and see a quantity recomputed from a transparent equation. These are intentionally simplified demonstrations; read the limitations beside each model before drawing a conclusion.

### Gross bathymetric survey area

Input: Usable swath width (km); range 0.5–6; initial 2.5. Output in km².

**Equation:** `72*x`. **Limit:** Fixed 72-km effective track length; overlap omitted.

### Independent depth uncertainty combination

Input: Second random uncertainty (m); range 0–20; initial 4. Output in m.

**Equation:** `Math.sqrt(3*3+x*x)`. **Limit:** Independent zero-mean errors; systematic datum bias excluded.
