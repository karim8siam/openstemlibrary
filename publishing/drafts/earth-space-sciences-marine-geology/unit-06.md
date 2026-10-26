# Unit 6: Submarine hazards, fluid flow and slope stability

## Guiding question: What processes trigger seabed failure, deformation, seepage and tsunami-related disturbances?

**Synthetic case:** A fictional infrastructure corridor crosses a canyon head and an area of shallow gas. Surveys contain signs of possible past mass movement but no measured probability of failure. Learners separate susceptibility from a quantified forecast and identify the additional evidence required for engineering decisions.

## Geological framework: questions, scales and competing evidence

An underwater slope can be steep, weakly consolidated or incised by faults without an imminent failure. Geological evidence can support screening for hazards but not credible site-specific probabilities unless calibrated with timing, material properties, pressure and forcing history. A landslide trigger is different from long-term preconditioning; multiple combinations of sedimentation, fluid flow and earthquake shaking may produce the same failed layer. Long-wave speed provides a first physical insight into tsunami propagation but is not an inundation forecast. Gas-hydrate stability depends on temperature, pressure, salinity and composition, not pressure alone. Studies supporting cables, energy facilities or public safety need professionally reviewed geotechnical data, not classroom charts.

## Five lessons with evidence notebooks

Each lesson joins a physical principle, an observable, a competing explanation, and a quantified classroom calculation. A numerical result is conditional on the stated synthetic inputs. Details such as local hazard probability, legal extraction requirements or physical-property inversion cannot be derived from the simple cases.

## Lesson 6.1 — Marine redox, organic carbon and sediment records

### Geological principle: what produces the pattern?

Organic carbon burial and redox-sensitive minerals respond to productivity, oxygen supply, burial rates and diagenesis. Anoxic sediment does not necessarily mean surface-water conditions were anoxic.

### Observation plan: what is actually measured?

Analyze total organic carbon, sulfur phases, iron speciation, trace metals and sedimentary lamination; check sampling contamination and temporal averaging.

### Alternative hypotheses and what would refute them

High organic carbon may reflect better preservation or rapid sedimentation rather than higher primary productivity. Trace-metal enrichments are concentration ratios that also depend on detrital dilution.

### Worked numerical investigation

**Synthetic problem — Organic carbon accumulation.** Dry bulk density 0.7 g/cm³, accumulation 2 cm/ka and carbon mass fraction 0.04; compute carbon mass accumulation.

**Equation and substitution:** `0.7*2*0.04`. The computed answer is **0.056 g/cm²/ka**. The units in the input determine the units in the answer. Check the dimensional conversion before interpreting a scalar as a geological quantity. A physically meaningful result should also be examined at a second parameter value to determine whether the trend makes sense.

**Interpretation:** Mass flux can distinguish dilution from concentration effects. **What this does not establish:** The rate is assumed constant, with no organic carbon loss after burial.

### A focused field or laboratory investigation

Create a multi-proxy decision tree for reduced pore waters versus oxygen-poor bottom waters, highlighting assumptions that cannot be solved from a single core.

**Design choice:** Choose a competing model. List two geologically distinct processes that produce a similar measured pattern, then predict a variable on which those explanations disagree. Prefer the prediction with a measurable sign, geometry, age ordering or composition rather than a vague expectation of greater complexity. Specify both an inexpensive screening observation and a decisive but costly validation.

## Lesson 6.2 — Seafloor mass movements and slope instability

### Geological principle: what produces the pattern?

Submarine slides, slumps and debris flows deform or remobilize seabed material when driving shear stress exceeds available strength. Pore pressure, rapid deposition, earthquakes and erosion can contribute, but timing and trigger attribution require evidence.

### Observation plan: what is actually measured?

Map headscarps, displaced blocks, chaotic seismic units and runout deposits; estimate local slope, sediment properties and failure volumes with uncertainty. Inspect pre- and post-event bathymetry where available.

### Alternative hypotheses and what would refute them

A deposit volume can be mistaken for the volume of the failure scar due to bulking and erosion. A nearby earthquake is not automatically the trigger; preconditioning may have lasted centuries.

### Worked numerical investigation

**Synthetic problem — Slope driving shear stress.** A 5 m thick saturated slab has submerged bulk density 900 kg/m³ on a 5° slope; calculate gravity-driven shear stress.

**Equation and substitution:** `900*9.81*5*math.sin(math.radians(5))*math.cos(math.radians(5))`. The computed answer is **3832.8 Pa**. The units in the input determine the units in the answer. Check the dimensional conversion before interpreting a scalar as a geological quantity. A physically meaningful result should also be examined at a second parameter value to determine whether the trend makes sense.

**Interpretation:** This idealized infinite-slope stress is only one component of stability analysis. **What this does not establish:** It omits shear strength, stratigraphy, pore pressure and dynamic shaking.

### A focused field or laboratory investigation

Rank survey zones by relative susceptibility, explicitly refusing to convert a qualitative score into a failure probability without calibration data.

**Design choice:** Build a scale-aware cross section. Identify the physical and temporal scale of the process. Specify what a one-dimensional profile hides in the horizontal direction, and what a surface map cannot show about burial history. Represent uncertainty as an interval or alternate boundaries rather than a decorative confidence label; annotate the map with each instrument footprint.

## Lesson 6.3 — Tsunami geology and offshore earthquake evidence

### Geological principle: what produces the pattern?

Large seafloor displacement can generate tsunamis, but the ocean response depends on displacement geometry, time history, water depth and coastal morphology. Marine deposits can preserve evidence of past events, though event attribution is difficult.

### Observation plan: what is actually measured?

Compare offshore fault geometry and deformation estimates with marine turbidite sequences and coastal sediment records. Use independent age constraints for event correlations.

### Alternative hypotheses and what would refute them

Multiple turbidite layers may result from storms or slope failures unrelated to large earthquakes. A modeled tsunami from an idealized fault is not a site-specific emergency forecast.

### Worked numerical investigation

**Synthetic problem — Shallow-water wave speed.** An idealized long wave crosses uniform 4,000 m depth; calculate phase speed.

**Equation and substitution:** `math.sqrt(9.81*4000)`. The computed answer is **198.09 m/s**. The units in the input determine the units in the answer. Check the dimensional conversion before interpreting a scalar as a geological quantity. A physically meaningful result should also be examined at a second parameter value to determine whether the trend makes sense.

**Interpretation:** Long-wave speed depends on water depth under shallow-water assumptions. **What this does not establish:** Not a tsunami warning or site-specific propagation forecast.

### A focused field or laboratory investigation

Analyze the distinction between a source scenario, propagation simulation and validated inundation forecast, and document why the book's toy models cannot replace official warnings.

**Design choice:** Audit an inference chain. Write the chain from raw sensor or sample to computed quantity, derived feature and geological explanation. At each arrow name an assumption and a calibration record. If any arrow cannot be supported, retain a provisional descriptive label instead of forcing an unverified genetic classification.

## Lesson 6.4 — Gas hydrates and bottom-simulating reflectors

### Geological principle: what produces the pattern?

Gas hydrates can occur within suitable pressure-temperature and methane conditions beneath seafloor sediments. A bottom-simulating reflector may relate to a contrast across the base of hydrate stability, but seismic interpretation needs controls.

### Observation plan: what is actually measured?

Examine reflection polarity, crosscutting of stratigraphy, pore-water chloride, temperature gradient and direct samples where available. Keep thermodynamic stability distinct from measured hydrate saturation.

### Alternative hypotheses and what would refute them

Not every bottom-simulating reflector proves hydrate, and a hydrate stability field does not imply high concentration or extractable resource. Gas migration can distort velocities and produce wipeout zones.

### Worked numerical investigation

**Synthetic problem — Hydrostatic pressure increment.** Assume water density 1,025 kg/m³ at a depth increment of 1,000 m; estimate pressure increase.

**Equation and substitution:** `1025*9.81*1000/1e6`. The computed answer is **10.055 MPa**. The units in the input determine the units in the answer. Check the dimensional conversion before interpreting a scalar as a geological quantity. A physically meaningful result should also be examined at a second parameter value to determine whether the trend makes sense.

**Interpretation:** Pressure scales with depth for fixed density. **What this does not establish:** The calculation is not a methane-hydrate stability prediction.

### A focused field or laboratory investigation

Trace two possible BSR interpretations and propose a non-invasive observation set to test each before suggesting coring.

**Design choice:** Design a disconfirming observation. Suppose the leading geological hypothesis is wrong. Which new sample, repeat transect or independent instrument would most readily reveal the mistake? Prefer high-information contrasts over uniformly increasing sample counts; explicitly discuss how limited ship time changes the geographic representativeness of the result.

## Lesson 6.5 — Cold seeps, faults and fluid pathways

### Geological principle: what produces the pattern?

Methane and other fluids can migrate through permeable strata, faults or fractures, altering pore-water chemistry and benthic ecology. Seeps may be episodic, and surface expressions can outlive active discharge.

### Observation plan: what is actually measured?

Integrate high-frequency acoustic anomalies, pore-water profiles, authigenic carbonates, thermal observations and repeat ROV imagery. Establish background controls away from suspected conduits.

### Alternative hypotheses and what would refute them

Bubble plumes, seep carbonates and chemical anomalies occur on different timescales; a historical carbonate deposit is not proof of current high flux. Biological communities can also vary for non-seep reasons.

### Worked numerical investigation

**Synthetic problem — Seep carbon flux.** A hypothetical seep releases 0.3 mol methane per m² per day across 150 m²; compute daily molar flux.

**Equation and substitution:** `0.3*150`. The computed answer is **45 mol/day**. The units in the input determine the units in the answer. Check the dimensional conversion before interpreting a scalar as a geological quantity. A physically meaningful result should also be examined at a second parameter value to determine whether the trend makes sense.

**Interpretation:** Flux density must be integrated over source area. **What this does not establish:** Bubble dissolution and temporal variability complicate measurements.

### A focused field or laboratory investigation

Design repeat observations to distinguish persistent flow from episodic venting, and describe how to report uncertainty in seep flux estimates.

**Design choice:** Inspect sensitivity to processing. Imagine regridding an acoustic field, changing a lithology classification threshold or revising one age control. Determine which apparent geological boundary persists and which vanishes. Report a stable core of interpretation as well as the disputed region, rather than selecting the single map with the neatest outlines.

### Research deep dive: when a hazard map is only a screening map

Submarine landslide susceptibility may increase where a slope is steep, deposits are weak, a canyon undercuts the foot or pore pressures are elevated. Yet a susceptibility map is not a probability of failure next year. Turning it into a forecast requires event histories, forcing rates, material parameters and defensible statistical or mechanical calibration. The simple gravitational shear-stress expression used in the course can show the influence of slope angle, but without shear strength, pore pressure and boundary conditions it cannot quantify a factor of safety.

Repeated acoustic surveys can identify changes in scarp form or sediment movement. In contrast, a single high-resolution bathymetric mosaic often records ancient features alongside modern ones. A sharp-looking scar does not guarantee recent activity. To date movement, seek buried deposits, stratigraphic offsets, repeat bathymetry, or independently dated event horizons. Be cautious when a nearby earthquake appears in the same geological interval: the chronological overlap may be broad and competing triggers remain possible.

For ideal long gravity waves, phase speed depends on water depth through the square root of gravitational acceleration times depth. This is a physical principle, not a tsunami exposure product. Real tsunami propagation and inundation depend on a moving seafloor source, dispersion conditions, bathymetric detail, coastal topology and numerical schemes. Neither a toy wave-speed slider nor a sediment layer allows readers to identify safe evacuation routes. A scientifically responsible textbook demonstrates this boundary explicitly.

Methane-related seabed features add further ambiguity. A bottom-simulating reflector may be associated with the base of gas-hydrate stability, but without velocity, chemistry and thermal information it is not conclusive evidence of hydrate saturation. Fluid seepage may create authigenic carbonates that persist after emissions cease. For a proposed infrastructure corridor, the right output of a desk study is an evidence-ranked list of features requiring specialist geotechnical survey, not a declaration of construction safety.

## Unit investigation: linking map, core and mechanism

**Aim.** Use the forty synthetic stations in `datasets/unit-06.csv` to test a question involving submarine hazards, fluid flow and slope stability. Treat the CSV as invented material for practicing statistical quality control, not as an actual seabed dataset. Plot water depth and acoustic sediment thickness along the transect; add markers for the `review` flags and record how the conclusions change after excluding them. The along-track separation is a schematic distance, not latitude or longitude, and therefore cannot establish the orientation or full area of a geological body.

**Background synthesis.** An underwater slope can be steep, weakly consolidated or incised by faults without an imminent failure. Geological evidence can support screening for hazards but not credible site-specific probabilities unless calibrated with timing, material properties, pressure and forcing history. A landslide trigger is different from long-term preconditioning; multiple combinations of sedimentation, fluid flow and earthquake shaking may produce the same failed layer. Long-wave speed provides a first physical insight into tsunami propagation but is not an inundation forecast. Gas-hydrate stability depends on temperature, pressure, salinity and composition, not pressure alone. Studies supporting cables, energy facilities or public safety need professionally reviewed geotechnical data, not classroom charts.

**Design brief.** A fictional infrastructure corridor crosses a canyon head and an area of shallow gas. Surveys contain signs of possible past mass movement but no measured probability of failure. Learners separate susceptibility from a quantified forecast and identify the additional evidence required for engineering decisions. Specify one observation that you expect to see if your mechanism is correct and a different one expected under a plausible alternative. Identify three layers of evidence: a survey observation, a physical sample, and a geophysical or chronologic constraint. Give each evidence layer a separate confidence score and justification. Do not average those scores unless their dependence is explicitly justified. Two products derived from the same ship track are not fully independent corroboration.

**Procedure, Part A — reconstruct what was measured.** Load the CSV and confirm that depth, thickness and size values are positive where expected. Calculate the smallest and largest water depths, the range of recovered thicknesses, and the number of flagged rows. Make two alternative maps: one preserving all points with quality flags visible, another excluding flagged stations. Label this contrast a sensitivity study. The second view should not be automatically judged more correct; removal can itself bias the spatial pattern if poor observations cluster in difficult terrain.

**Procedure, Part B — inspect model dependency.** Examine the plotted gradient at an interval of two, five and ten stations, and identify which short features are averaged away. Estimate a simple slope in metres per kilometer using a defined pair of samples. State whether this is a geometric seabed slope or a sediment thickness gradient; the distinction affects interpretation. If you attempt uncertainty propagation, specify assumed error correlations rather than selecting a root-sum-square formula by habit.

**Procedure, Part C — compare competing histories.** Write two plausible geological narratives that fit the synthetic pattern. One should emphasize a structural or long-timescale explanation; the other should emphasize deposition, redistribution or erosional overprinting where meaningful. List predictions that differ: reflector geometry, sediment type, age ordering, fault offsets, pore-fluid signals or mineralogical provenance. Rank possible next observations by ability to distinguish those predictions, not by how dramatic their imagery would look.

**Procedure, Part D — communicate limitations.** Prepare a four-panel reproducible report: data provenance, primary measurement plot, competing explanation diagram and uncertainty ledger. In the ledger, list unknown vertical datum, unrealistically simplified synthetic values, unmeasured lithology, timing uncertainty and any relevant instrument bias. Explicitly describe which claims the report cannot make. For marine hazards, resource assessment and navigational uses, do not substitute this exercise for official data or specialist review.

**Deliverables and grading:** 20% clean reproducible analysis, 20% physically coherent interpretations, 20% alternative hypotheses, 20% quantitative unit and sensitivity checks, and 20% uncertainty communication. A technically polished visualization that hides the fact that the data are synthetic cannot receive full credit. Submit the processing steps, plots, an evidence matrix and a revision note explaining which conclusion changed after reviewing uncertainties.

## Unit assessment: reasoning rather than memorization

**Question A:** Design a way to disprove the leading hypothesis for submarine hazards, fluid flow and slope stability while spending no more than two new stations on the fictional cruise. Justify each station by the predicted difference between models.

**Question B:** Explain how an erroneous vertical datum, poor coring recovery, or inappropriate age tie point would affect at least two of the results presented in this unit. Distinguish changed numerical answers from changed geological conclusions.

**Question C:** Propose a figure caption for an unfamiliar scientific reader. It must name what was measured, the units, geographic or stratigraphic coverage, important transformations, and one explicit limitation.

**Question D:** Choose one of the unit models and identify which environmental or geological variable is intentionally held constant. Explain how failure of that constant would change the interpretation but not necessarily invalidate the model as a teaching aid.

## Further investigation and practical extension

To extend the fictional unit project into real research, start with the references and select a genuine open dataset with clear acquisition date, license, method, processing version and coordinate reference system. For submarine hazards, fluid flow and slope stability, seek at least one direct measurement that does not originate from the same inversion as the map. Compare two spatial resolutions before discussing morphology. Keep real observations strictly separated from the invented training CSV. A reproducible report should link each plotted feature to a raw record, show how missing values were handled, and make failed interpretations visible rather than deleting them from the final narrative.


## Interactive models accompanying Unit 6

Open the HTML chapter to move the sliders and see a quantity recomputed from a transparent equation. These are intentionally simplified demonstrations; read the limitations beside each model before drawing a conclusion.

### Ideal driving shear stress

Input: Slope angle (degrees); range 0–20; initial 5. Output in Pa.

**Equation:** `900*9.81*5*Math.sin(x*Math.PI/180)*Math.cos(x*Math.PI/180)`. **Limit:** Uniform infinite-slope geometry; excludes strength and pore pressure.

### Ideal long-wave speed

Input: Water depth (m); range 100–6000; initial 4000. Output in m/s.

**Equation:** `Math.sqrt(9.81*x)`. **Limit:** Shallow-water limit only; never for emergency warnings.
