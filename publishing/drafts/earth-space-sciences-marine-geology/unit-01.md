# Unit 1: Mapping and the marine geological record

## Guiding question: How can measurements at sea distinguish actual relief, buried strata and processing artefacts?

**Synthetic case:** A fictional teaching vessel surveys a poorly mapped continental slope. Its navigation is imperfect, the sound-speed profile changes overnight, and archived depth grids combine direct soundings with predictions from gravity. Students must decide where to place the next survey line, what uncertainty to report, and when to collect a sample.

## Geological framework: questions, scales and competing evidence

A multibeam surface is the outcome of numerous processing choices: vessel motion, water-column refraction, time stamping, tidal correction, beam rejection and interpolation. Differing resolutions do not mean that a low-resolution product is false; they mean it supports a different question. A broad slope break could be reliable at kilometer scale while a narrow fault scarp cannot be separated from sonar footprint noise. Geological claims must therefore be matched to the spatial wavelength that the sensor truly resolves. Acoustic reflections add a complementary dimension below the seafloor but require sound-velocity assumptions before a thickness can be reported in meters. A physical sediment sample reduces ambiguity locally while raising issues of disturbance and geographic representativeness. Geologic map classes should always distinguish observed samples, acoustic interpretation and extrapolation.

## Five lessons with evidence notebooks

Each lesson joins a physical principle, an observable, a competing explanation, and a quantified classroom calculation. A numerical result is conditional on the stated synthetic inputs. Details such as local hazard probability, legal extraction requirements or physical-property inversion cannot be derived from the simple cases.

## Lesson 1.1 — Seafloor physiography and depth datums

### Geological principle: what produces the pattern?

Continental shelves, slopes, rises, abyssal plains and trenches occupy distinct morphotectonic positions, but their dimensions vary strongly with tectonic regime, sediment supply and sea-level history. A map of depth is not a map of lithology. A steep gradient can register bedrock relief, incision, mass wasting or an erroneous sounding.

### Observation plan: what is actually measured?

Plan transects orthogonal to major contours and check whether adjacent survey lines overlap. Record geographic coordinate reference, vertical datum, tide correction, heave, pitch, roll, sound-speed correction and cell spacing. Distinguish measured points from interpolated grid cells.

### Alternative hypotheses and what would refute them

Apparent seabed steps can arise from datum mismatches, outer-beam artefacts, gridding or transducer offsets. A smooth regional bathymetric model may contain fewer direct measurements than its resolution suggests; its apparent spatial detail is not proof of precision.

### Worked numerical investigation

**Synthetic problem — Shelf–abyss contrast.** Shelf depth is 180 m and basin depth is 4,380 m; obtain the relief magnitude.

**Equation and substitution:** `4380-180`. The computed answer is **4200 m**. The units in the input determine the units in the answer. Check the dimensional conversion before interpreting a scalar as a geological quantity. A physically meaningful result should also be examined at a second parameter value to determine whether the trend makes sense.

**Interpretation:** The depth difference is positive, but does not describe the distance over which it occurs. **What this does not establish:** Use the same depth datum for both stations.

### A focused field or laboratory investigation

Compare a direct sounding grid with a predicted gravity-based grid; report which canyon or scarp remains supported when only direct observations are considered.

**Design choice:** Replicate the observation. For this topic, describe which parts of a figure are directly measured and which were inferred from calibration, interpolation, geological priors or visual classification. The observation may be convincing even if the preferred explanation remains uncertain. Design a check in which a second observer can reproduce the result using the same input files and clear processing parameters.

## Lesson 1.2 — Multibeam sonar and acoustic backscatter

### Geological principle: what produces the pattern?

A multibeam echo sounder estimates slant ranges along many beams and resolves depth through time-of-flight and beam geometry. Backscatter amplitude responds to incidence angle, sediment roughness, interface properties and instrument settings rather than sediment grain size alone.

### Observation plan: what is actually measured?

Acquire water-column sound speed, motion compensation and reciprocal crossing lines. Inspect beam angle, footprint dimensions and grazing angle. Calibrate mosaics across changing acquisition conditions; preserve raw amplitudes before angle normalization.

### Alternative hypotheses and what would refute them

Strong returns could indicate rock, shell hash, coarse sediment or favourable geometry. Sediment texture cannot be unambiguously identified without photographs or physical samples. A vessel turn can create a convincing false patch in an uncorrected mosaic.

### Worked numerical investigation

**Synthetic problem — Acoustic sounding.** A vertical pulse has two-way travel time 3.8 s at assumed uniform speed 1,500 m/s; find depth.

**Equation and substitution:** `1500*3.8/2`. The computed answer is **2850 m**. The units in the input determine the units in the answer. Check the dimensional conversion before interpreting a scalar as a geological quantity. A physically meaningful result should also be examined at a second parameter value to determine whether the trend makes sense.

**Interpretation:** Divide by two because the pulse travels downward and upward. **What this does not establish:** Refraction and variable water-column sound speed are excluded.

### A focused field or laboratory investigation

Ground-truth two backscatter classes with targeted grab samples, then test classification accuracy on withheld stations rather than those used to tune the model.

**Design choice:** Choose a competing model. List two geologically distinct processes that produce a similar measured pattern, then predict a variable on which those explanations disagree. Prefer the prediction with a measurable sign, geometry, age ordering or composition rather than a vague expectation of greater complexity. Specify both an inexpensive screening observation and a decisive but costly validation.

## Lesson 1.3 — Sub-bottom profiling and reflection geometry

### Geological principle: what produces the pattern?

Sub-bottom acoustic profilers resolve reflections from contrasts in acoustic impedance; penetrating depth and vertical resolution depend on frequency, material attenuation and acquisition geometry. Reflection time is not sediment depth until an appropriate sound-speed conversion is applied.

### Observation plan: what is actually measured?

Trace continuous reflectors, truncations and onlap through crossing profiles. Annotate two-way travel time, polarity conventions, seismic frequency, estimated velocity and any migration or filtering applied.

### Alternative hypotheses and what would refute them

Bright reflections may record lithologic change, gas-related attenuation, an erosional surface or processing artefact. A reflector is a physical interface, not automatically a synchronous time surface; its continuity must be independently tested.

### Worked numerical investigation

**Synthetic problem — Acoustic reflector conversion.** A sub-bottom reflector appears at 0.14 s two-way time under a nominal 1,600 m/s acoustic velocity; infer depth below bed.

**Equation and substitution:** `1600*0.14/2`. The computed answer is **112 m**. The units in the input determine the units in the answer. Check the dimensional conversion before interpreting a scalar as a geological quantity. A physically meaningful result should also be examined at a second parameter value to determine whether the trend makes sense.

**Interpretation:** This is acoustic depth, not a core measurement. **What this does not establish:** Compaction and different layer velocities invalidate a single-speed conversion.

### A focused field or laboratory investigation

Draw two alternative stratigraphic interpretations of the same sub-bottom section and specify what core interval would discriminate them.

**Design choice:** Build a scale-aware cross section. Identify the physical and temporal scale of the process. Specify what a one-dimensional profile hides in the horizontal direction, and what a surface map cannot show about burial history. Represent uncertainty as an interval or alternate boundaries rather than a decorative confidence label; annotate the map with each instrument footprint.

## Lesson 1.4 — Marine sampling, positioning and ground truth

### Geological principle: what produces the pattern?

Sediment grabs, box cores, piston cores, dredges, remotely operated vehicles and drilling sample different depths and geological materials. Every tool has selection biases and disturbance mechanisms; recovery rate is not always equal to the proportion of geology faithfully recorded.

### Observation plan: what is actually measured?

Assign sample identifiers, precise station positions, penetration estimates, recovery lengths, deck photographs, sample handling records and chain of custody. Relate samples to sonar footprints and consider slopes and currents that move a sampler away from its nominal target.

### Alternative hypotheses and what would refute them

A lost fine fraction, disturbed core top or dredge moved along a slope can produce a misleading facies description. One surface sample does not validate a multilayered acoustic model beneath it.

### Worked numerical investigation

**Synthetic problem — Core recovery.** A corer penetrates 3.5 m but recovers 2.73 m; find recovered percentage.

**Equation and substitution:** `100*2.73/3.5`. The computed answer is **78 %**. The units in the input determine the units in the answer. Check the dimensional conversion before interpreting a scalar as a geological quantity. A physically meaningful result should also be examined at a second parameter value to determine whether the trend makes sense.

**Interpretation:** A percentage records recovered length relative to nominal penetration. **What this does not establish:** Core shortening and disturbance may persist even at high recovery.

### A focused field or laboratory investigation

Draft a sampling plan with random, stratified and purposive stations, explaining how each design changes the strength of the inference.

**Design choice:** Audit an inference chain. Write the chain from raw sensor or sample to computed quantity, derived feature and geological explanation. At each arrow name an assumption and a calibration record. If any arrow cannot be supported, retain a provisional descriptive label instead of forcing an unverified genetic classification.

## Lesson 1.5 — Geological uncertainty and seafloor GIS

### Geological principle: what produces the pattern?

A geologic GIS integrates raster soundings, seismic horizons, core points and classified polygons at incompatible support scales. Explicit uncertainty surfaces prevent digital overlays from creating a false impression of seamless certainty.

### Observation plan: what is actually measured?

Keep source method, acquisition date, processing version, data type, resolution and vertical reference alongside each layer. Inspect slope at multiple grid scales and perform leave-one-track-out validation where survey density permits.

### Alternative hypotheses and what would refute them

Spatial autocorrelation, interpolation smoothing and the modifiable area unit problem can make model accuracy look artificially strong. A classification trained on adjacent samples may fail when tested in a new physiographic zone.

### Worked numerical investigation

**Synthetic problem — Position uncertainty.** Two independent planimetric error components are 6 m and 8 m; calculate an RMS magnitude.

**Equation and substitution:** `math.sqrt(6**2+8**2)`. The computed answer is **10 m**. The units in the input determine the units in the answer. Check the dimensional conversion before interpreting a scalar as a geological quantity. A physically meaningful result should also be examined at a second parameter value to determine whether the trend makes sense.

**Interpretation:** Orthogonal independent terms combine in quadrature. **What this does not establish:** Systematic offsets must not be treated as independent random errors.

### A focused field or laboratory investigation

Design a four-level evidence map showing measured, interpreted, interpolated and unknown seabed, and require every published feature to expose its provenance.

**Design choice:** Design a disconfirming observation. Suppose the leading geological hypothesis is wrong. Which new sample, repeat transect or independent instrument would most readily reveal the mistake? Prefer high-information contrasts over uniformly increasing sample counts; explicitly discuss how limited ship time changes the geographic representativeness of the result.

### Research deep dive: why a gorgeous map can be wrong

Imagine a survey that acquires excellent multibeam coverage along parallel north–south tracks but none between them. The grid interpolator produces continuous contours across the missing swaths. It is tempting to estimate the width of a narrow scarp from those contours. Yet interpolation is a mathematical guess that was conditioned by track spacing: narrowing grid cells does not create extra observations. First plot the raw soundings by source type and beam angle. Second calculate the sounding density in each cell. Third mask cells farther than a chosen distance from any directly measured point. The scarp interpretation should be reconsidered if it crosses a wide unsounded area.

Echo travel time is linked to distance by an assumed sound-speed field, but the ray is not necessarily straight and the return is not necessarily from the nadir point. At oblique incidence, refraction and attitude errors can grow. If a sound-speed profile was measured at the beginning of the day but the vessel crossed a changing water mass, outer beams may show spurious ridge-like streaks. Crossing survey lines provide a diagnostic because the same patch of seabed appears at different beam angles. Consistent crossline residuals are valuable; correlated errors in the same calibration system are not eliminated by adding nearby points.

Sub-bottom profiles have their own inversion ambiguity. A reflector at 0.2 seconds of two-way travel time is 160 meters deep if a constant 1600 m/s sound velocity is appropriate, but the same reflection time means 180 meters if the true velocity is 1800 m/s. This 20-meter mismatch could change a claimed thickness trend or burial estimate. A physical core helps calibrate velocity and composition locally, yet a core may not penetrate the reflector of interest. Do not publish a lithologic contact as ground-truthed when no sample reaches it.

The research output should include two aligned images: an attractive best-estimate geological map and a source-coverage map. The second is not supplementary decoration. It tells readers where the first image is evidence and where it is an inference. Add a short provenance note distinguishing GEBCO predicted bathymetry from direct multibeam information when using global maps, and explicitly prohibit navigational use of these classroom outputs.

## Unit investigation: linking map, core and mechanism

**Aim.** Use the forty synthetic stations in `datasets/unit-01.csv` to test a question involving mapping and the marine geological record. Treat the CSV as invented material for practicing statistical quality control, not as an actual seabed dataset. Plot water depth and acoustic sediment thickness along the transect; add markers for the `review` flags and record how the conclusions change after excluding them. The along-track separation is a schematic distance, not latitude or longitude, and therefore cannot establish the orientation or full area of a geological body.

**Background synthesis.** A multibeam surface is the outcome of numerous processing choices: vessel motion, water-column refraction, time stamping, tidal correction, beam rejection and interpolation. Differing resolutions do not mean that a low-resolution product is false; they mean it supports a different question. A broad slope break could be reliable at kilometer scale while a narrow fault scarp cannot be separated from sonar footprint noise. Geological claims must therefore be matched to the spatial wavelength that the sensor truly resolves. Acoustic reflections add a complementary dimension below the seafloor but require sound-velocity assumptions before a thickness can be reported in meters. A physical sediment sample reduces ambiguity locally while raising issues of disturbance and geographic representativeness. Geologic map classes should always distinguish observed samples, acoustic interpretation and extrapolation.

**Design brief.** A fictional teaching vessel surveys a poorly mapped continental slope. Its navigation is imperfect, the sound-speed profile changes overnight, and archived depth grids combine direct soundings with predictions from gravity. Students must decide where to place the next survey line, what uncertainty to report, and when to collect a sample. Specify one observation that you expect to see if your mechanism is correct and a different one expected under a plausible alternative. Identify three layers of evidence: a survey observation, a physical sample, and a geophysical or chronologic constraint. Give each evidence layer a separate confidence score and justification. Do not average those scores unless their dependence is explicitly justified. Two products derived from the same ship track are not fully independent corroboration.

**Procedure, Part A — reconstruct what was measured.** Load the CSV and confirm that depth, thickness and size values are positive where expected. Calculate the smallest and largest water depths, the range of recovered thicknesses, and the number of flagged rows. Make two alternative maps: one preserving all points with quality flags visible, another excluding flagged stations. Label this contrast a sensitivity study. The second view should not be automatically judged more correct; removal can itself bias the spatial pattern if poor observations cluster in difficult terrain.

**Procedure, Part B — inspect model dependency.** Examine the plotted gradient at an interval of two, five and ten stations, and identify which short features are averaged away. Estimate a simple slope in metres per kilometer using a defined pair of samples. State whether this is a geometric seabed slope or a sediment thickness gradient; the distinction affects interpretation. If you attempt uncertainty propagation, specify assumed error correlations rather than selecting a root-sum-square formula by habit.

**Procedure, Part C — compare competing histories.** Write two plausible geological narratives that fit the synthetic pattern. One should emphasize a structural or long-timescale explanation; the other should emphasize deposition, redistribution or erosional overprinting where meaningful. List predictions that differ: reflector geometry, sediment type, age ordering, fault offsets, pore-fluid signals or mineralogical provenance. Rank possible next observations by ability to distinguish those predictions, not by how dramatic their imagery would look.

**Procedure, Part D — communicate limitations.** Prepare a four-panel reproducible report: data provenance, primary measurement plot, competing explanation diagram and uncertainty ledger. In the ledger, list unknown vertical datum, unrealistically simplified synthetic values, unmeasured lithology, timing uncertainty and any relevant instrument bias. Explicitly describe which claims the report cannot make. For marine hazards, resource assessment and navigational uses, do not substitute this exercise for official data or specialist review.

**Deliverables and grading:** 20% clean reproducible analysis, 20% physically coherent interpretations, 20% alternative hypotheses, 20% quantitative unit and sensitivity checks, and 20% uncertainty communication. A technically polished visualization that hides the fact that the data are synthetic cannot receive full credit. Submit the processing steps, plots, an evidence matrix and a revision note explaining which conclusion changed after reviewing uncertainties.

## Unit assessment: reasoning rather than memorization

**Question A:** Design a way to disprove the leading hypothesis for mapping and the marine geological record while spending no more than two new stations on the fictional cruise. Justify each station by the predicted difference between models.

**Question B:** Explain how an erroneous vertical datum, poor coring recovery, or inappropriate age tie point would affect at least two of the results presented in this unit. Distinguish changed numerical answers from changed geological conclusions.

**Question C:** Propose a figure caption for an unfamiliar scientific reader. It must name what was measured, the units, geographic or stratigraphic coverage, important transformations, and one explicit limitation.

**Question D:** Choose one of the unit models and identify which environmental or geological variable is intentionally held constant. Explain how failure of that constant would change the interpretation but not necessarily invalidate the model as a teaching aid.

## Further investigation and practical extension

To extend the fictional unit project into real research, start with the references and select a genuine open dataset with clear acquisition date, license, method, processing version and coordinate reference system. For mapping and the marine geological record, seek at least one direct measurement that does not originate from the same inversion as the map. Compare two spatial resolutions before discussing morphology. Keep real observations strictly separated from the invented training CSV. A reproducible report should link each plotted feature to a raw record, show how missing values were handled, and make failed interpretations visible rather than deleting them from the final narrative.


## Interactive models accompanying Unit 1

Open the HTML chapter to move the sliders and see a quantity recomputed from a transparent equation. These are intentionally simplified demonstrations; read the limitations beside each model before drawing a conclusion.

### Sounding depth from echo return

Input: Two-way travel time (s); range 0.5–8; initial 3. Output in m.

**Equation:** `1500*x/2`. **Limit:** Uniform 1500 m/s sound speed; vertical geometry and no refraction.

### Sub-bottom acoustic conversion

Input: Two-way reflection time (s); range 0.05–0.5; initial 0.18. Output in m.

**Equation:** `1600*x/2`. **Limit:** Uniform 1600 m/s sediment velocity; not a calibrated depth conversion.
