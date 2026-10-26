# Unit 4: Marine sediments, facies and diagenesis

## Guiding question: How are particulate materials deposited, buried, mixed and transformed?

**Synthetic case:** A teaching core crosses muddy, sandy and biogenic intervals. Its recovered length differs from drilled depth because of compaction and gaps; several proxies are plausible but not uniquely diagnostic. Students construct a facies and age model, explicitly tracking which depth intervals are missing.

## Geological framework: questions, scales and competing evidence

Core descriptions begin with what can be seen: texture, structures, microfossils, mineral phases and contacts. These observations are later translated into facies and processes, but the translation is many-to-one. Grading may accompany rapid density flow, whereas sorting can also result from persistent bottom currents. Bioturbation mixes recent and old particles, and carbonate dissolution removes a fraction of the original biogenic signal. Burial transforms pore volume, cement and mineral assemblages; these alterations can mimic signals otherwise attributed to ocean circulation or climate. Always log gaps, disturbed intervals and composite sections. A change in an isotope ratio is a measurement of composition relative to a standard, whereas temperature or ice volume are inferred variables with additional assumptions.

## Five lessons with evidence notebooks

Each lesson joins a physical principle, an observable, a competing explanation, and a quantified classroom calculation. A numerical result is conditional on the stated synthetic inputs. Details such as local hazard probability, legal extraction requirements or physical-property inversion cannot be derived from the simple cases.

## Lesson 4.1 — Sediment sources and provenance

### Geological principle: what produces the pattern?

Detrital mineral assemblages, isotopes and grain chemistry can connect marine deposits to terrestrial or volcanic sources, but sorting, weathering and recycling modify the signal along transport paths.

### Observation plan: what is actually measured?

Use paired sediment and plausible source samples, grain-size-matched geochemistry, petrography and detrital mineral ages. Keep analytical uncertainty and mixing assumptions explicit.

### Alternative hypotheses and what would refute them

One distinctive zircon age peak can be inherited through multiple sedimentary cycles. Heavy-mineral concentrations can also reflect hydraulics more strongly than catchment source abundance.

### Worked numerical investigation

**Synthetic problem — Mixing provenance.** A sample is 40% endmember A at 12 proxy units and 60% B at 4; predict conservative mixture.

**Equation and substitution:** `0.4*12+0.6*4`. The computed answer is **7.2 proxy units**. The units in the input determine the units in the answer. Check the dimensional conversion before interpreting a scalar as a geological quantity. A physically meaningful result should also be examined at a second parameter value to determine whether the trend makes sense.

**Interpretation:** Linear mixture gives a prediction for a conservative component. **What this does not establish:** Nonlinear fractionation and additional sources invalidate two-endmember inversion.

### A focused field or laboratory investigation

Calculate a two-end-member mixing estimate, then explain why adding a third unmeasured source makes the original solution non-unique.

**Design choice:** Apply a conservation or kinematic constraint. Define what enters and leaves the chosen region, and distinguish a material inventory from a flux. Where the subject is tectonic rather than depositional, check whether distances, ages and rate units are consistent. A residual indicates something unmeasured or a violated assumption; it does not automatically verify a preferred mechanism.

## Lesson 4.2 — Grain size, texture and depositional energy

### Geological principle: what produces the pattern?

Sediment texture integrates source material, transport energy, sorting and postdepositional mixing. Mean size, sorting and skewness are descriptive parameters; translating them directly into unique velocities is generally invalid.

### Observation plan: what is actually measured?

Report whether sizes were measured by sieving, laser diffraction or settling, since methods respond differently to particle shape and aggregation. Inspect full distributions, not just the median.

### Alternative hypotheses and what would refute them

Biogenic fragmentation, flocculation and multiple transport episodes can create multimodal distributions. Similar median sizes can hide very different sedimentological histories.

### Worked numerical investigation

**Synthetic problem — Grain-size phi scale.** For grain diameter 0.25 mm, compute Krumbein phi = minus log base 2 of mm size.

**Equation and substitution:** `-math.log2(0.25)`. The computed answer is **2 phi**. The units in the input determine the units in the answer. Check the dimensional conversion before interpreting a scalar as a geological quantity. A physically meaningful result should also be examined at a second parameter value to determine whether the trend makes sense.

**Interpretation:** Phi is logarithmic and dimensionless by reference to 1 mm. **What this does not establish:** Aggregate and biogenic particle shapes can invalidate simple size analogies.

### A focused field or laboratory investigation

Compare two synthetic samples with equal medians but different tails and propose the additional sedimentary structures needed to infer transport regime.

**Design choice:** Replicate the observation. For this topic, describe which parts of a figure are directly measured and which were inferred from calibration, interpolation, geological priors or visual classification. The observation may be convincing even if the preferred explanation remains uncertain. Design a check in which a second observer can reproduce the result using the same input files and clear processing parameters.

## Lesson 4.3 — Pelagic, hemipelagic and biogenic sediment

### Geological principle: what produces the pattern?

Open-ocean deposits may include windblown dust, volcaniclastic particles, biogenic shells and slowly settling clays, whereas margin-proximal hemipelagic sediment receives stronger land-derived input. Carbonate preservation is affected by water chemistry and burial environment.

### Observation plan: what is actually measured?

Measure carbonate content, microfossil assemblages, clay mineralogy and accumulation rates; interpret changes alongside productivity and dissolution rather than treating abundance as production alone.

### Alternative hypotheses and what would refute them

A low carbonate percentage may reflect dilution by terrigenous sediment instead of increased dissolution. Dissolution and changing plankton communities can also bias an isotope archive.

### Worked numerical investigation

**Synthetic problem — Carbonate mass accumulation.** Dry bulk density is 0.8 g/cm³, linear sedimentation 3 cm/ka, carbonate fraction 0.6; compute carbonate mass flux.

**Equation and substitution:** `0.8*3*0.6`. The computed answer is **1.44 g/cm²/ka**. The units in the input determine the units in the answer. Check the dimensional conversion before interpreting a scalar as a geological quantity. A physically meaningful result should also be examined at a second parameter value to determine whether the trend makes sense.

**Interpretation:** Density times rate times mass fraction yields constituent flux. **What this does not establish:** Sediment focusing, dissolved carbonate and temporal averaging are omitted.

### A focused field or laboratory investigation

Use a simple mass accumulation rate calculation and evaluate three causes of a changing carbonate fraction.

**Design choice:** Choose a competing model. List two geologically distinct processes that produce a similar measured pattern, then predict a variable on which those explanations disagree. Prefer the prediction with a measurable sign, geometry, age ordering or composition rather than a vague expectation of greater complexity. Specify both an inexpensive screening observation and a decisive but costly validation.

## Lesson 4.4 — Carbonate platforms and reef-associated deposits

### Geological principle: what produces the pattern?

Carbonate factories depend on organism ecology, light, water chemistry and accommodation space. Their growth can produce platforms, slopes and debris aprons, but exposure, dolomitization and dissolution alter the original record.

### Observation plan: what is actually measured?

Identify depositional textures, skeletal components, cement generations and exposure surfaces from imagery and core. Date boundaries independently when possible.

### Alternative hypotheses and what would refute them

A cemented surface may be submarine hardground rather than subaerial exposure. A reef-looking seismic mound requires fossil, microfacies or geomorphic ground truth.

### Worked numerical investigation

**Synthetic problem — Platform accommodation.** Relative accommodation increases at 2 mm/yr over 2 ka; find new vertical space.

**Equation and substitution:** `2*2000/1000`. The computed answer is **4 m**. The units in the input determine the units in the answer. Check the dimensional conversion before interpreting a scalar as a geological quantity. A physically meaningful result should also be examined at a second parameter value to determine whether the trend makes sense.

**Interpretation:** Rate and time estimate maximum generated accommodation under simplifications. **What this does not establish:** Changes in subsidence, eustasy and sediment infilling are excluded.

### A focused field or laboratory investigation

Build an idealized carbonate platform cross section and annotate where environmental, diagenetic and sea-level interpretations could be confused.

**Design choice:** Build a scale-aware cross section. Identify the physical and temporal scale of the process. Specify what a one-dimensional profile hides in the horizontal direction, and what a surface map cannot show about burial history. Represent uncertainty as an interval or alternate boundaries rather than a decorative confidence label; annotate the map with each instrument footprint.

## Lesson 4.5 — Sedimentary facies and vertical stacking

### Geological principle: what produces the pattern?

Facies group observable lithologic, textural and structural properties. Vertical successions may record migration of depositional environments, but cores are one-dimensional samples through complex three-dimensional bodies.

### Observation plan: what is actually measured?

Log color, grain size, contacts, sedimentary structures, fossils and bioturbation consistently. Align core photos with core depth and note disturbed intervals or incomplete recovery.

### Alternative hypotheses and what would refute them

A coarsening-upward sequence may reflect progradation, current reworking or episodic input; it is not sufficient proof of a single sea-level trend. Bioturbation can blur original contacts.

### Worked numerical investigation

**Synthetic problem — Facies transitions.** Of 20 logged sand beds, 7 pass upward into mud; compute observed transition percentage.

**Equation and substitution:** `100*7/20`. The computed answer is **35 %**. The units in the input determine the units in the answer. Check the dimensional conversion before interpreting a scalar as a geological quantity. A physically meaningful result should also be examined at a second parameter value to determine whether the trend makes sense.

**Interpretation:** A categorical transition frequency summarizes this log only. **What this does not establish:** Bed independence and unequal bed thickness cannot be assumed.

### A focused field or laboratory investigation

Design a facies transition matrix from a fictional core and compare an environmental succession with a mass-transport alternative.

**Design choice:** Audit an inference chain. Write the chain from raw sensor or sample to computed quantity, derived feature and geological explanation. At each arrow name an assumption and a calibration record. If any arrow cannot be supported, retain a provisional descriptive label instead of forcing an unverified genetic classification.

### Research deep dive: separating primary signals from burial effects

Take a fictional core in which carbonate content declines upwards, fine-grained material becomes more abundant and the number of preserved microfossil fragments decreases. One attractive explanation is a change in ocean chemistry. But carbonate percentage is a compositional ratio: the same decline can occur when extra terrigenous clay dilutes an unchanged carbonate mass flux. Begin with dry bulk density and a credible accumulation rate to calculate carbonate mass accumulation per area per time. If the flux remained stable while the percentage fell, dilution may be a better interpretation than dissolution.

The size distribution of sediment also encodes more than water velocity. The phi scale is logarithmic: 0.25 mm corresponds to phi = 2, while 0.5 mm is phi = 1. A plot that places phi values on a linear axis compresses physical size differently from a millimeter plot. Particle shape, aggregates and biogenic shells can make hydraulic equivalence ambiguous. Document whether a sample was analyzed by sieve, microscope or laser diffraction. Different techniques may produce different statistics even from the same sample, because they measure different aspects of the particle population.

During burial, pore space may shrink and cement may develop. A dry or saturated density estimate with only a single pore fluid and a single mineral grain density is useful for learning the mass-volume relationship, but real marine sediment may contain organic material, carbonate, opal, mixed clays and gas. A seismic low-velocity layer might reflect high porosity, gas or different lithology. Do not use acoustic velocity as a perfect porosity meter without calibration.

The lesson is that sedimentary facies, composition and diagenetic alteration are related but not identical. First log contacts and structures without assigning cause. Second identify which processes could produce each feature. Third add age constraints that separate episodes of deposition from later transformation. Finally explain which core intervals are disturbed, absent or insufficient to support a regional history. Good sedimentology is an exercise in preserving evidence and uncertainty, not just naming rock types.

## Unit investigation: linking map, core and mechanism

**Aim.** Use the forty synthetic stations in `datasets/unit-04.csv` to test a question involving marine sediments, facies and diagenesis. Treat the CSV as invented material for practicing statistical quality control, not as an actual seabed dataset. Plot water depth and acoustic sediment thickness along the transect; add markers for the `review` flags and record how the conclusions change after excluding them. The along-track separation is a schematic distance, not latitude or longitude, and therefore cannot establish the orientation or full area of a geological body.

**Background synthesis.** Core descriptions begin with what can be seen: texture, structures, microfossils, mineral phases and contacts. These observations are later translated into facies and processes, but the translation is many-to-one. Grading may accompany rapid density flow, whereas sorting can also result from persistent bottom currents. Bioturbation mixes recent and old particles, and carbonate dissolution removes a fraction of the original biogenic signal. Burial transforms pore volume, cement and mineral assemblages; these alterations can mimic signals otherwise attributed to ocean circulation or climate. Always log gaps, disturbed intervals and composite sections. A change in an isotope ratio is a measurement of composition relative to a standard, whereas temperature or ice volume are inferred variables with additional assumptions.

**Design brief.** A teaching core crosses muddy, sandy and biogenic intervals. Its recovered length differs from drilled depth because of compaction and gaps; several proxies are plausible but not uniquely diagnostic. Students construct a facies and age model, explicitly tracking which depth intervals are missing. Specify one observation that you expect to see if your mechanism is correct and a different one expected under a plausible alternative. Identify three layers of evidence: a survey observation, a physical sample, and a geophysical or chronologic constraint. Give each evidence layer a separate confidence score and justification. Do not average those scores unless their dependence is explicitly justified. Two products derived from the same ship track are not fully independent corroboration.

**Procedure, Part A — reconstruct what was measured.** Load the CSV and confirm that depth, thickness and size values are positive where expected. Calculate the smallest and largest water depths, the range of recovered thicknesses, and the number of flagged rows. Make two alternative maps: one preserving all points with quality flags visible, another excluding flagged stations. Label this contrast a sensitivity study. The second view should not be automatically judged more correct; removal can itself bias the spatial pattern if poor observations cluster in difficult terrain.

**Procedure, Part B — inspect model dependency.** Examine the plotted gradient at an interval of two, five and ten stations, and identify which short features are averaged away. Estimate a simple slope in metres per kilometer using a defined pair of samples. State whether this is a geometric seabed slope or a sediment thickness gradient; the distinction affects interpretation. If you attempt uncertainty propagation, specify assumed error correlations rather than selecting a root-sum-square formula by habit.

**Procedure, Part C — compare competing histories.** Write two plausible geological narratives that fit the synthetic pattern. One should emphasize a structural or long-timescale explanation; the other should emphasize deposition, redistribution or erosional overprinting where meaningful. List predictions that differ: reflector geometry, sediment type, age ordering, fault offsets, pore-fluid signals or mineralogical provenance. Rank possible next observations by ability to distinguish those predictions, not by how dramatic their imagery would look.

**Procedure, Part D — communicate limitations.** Prepare a four-panel reproducible report: data provenance, primary measurement plot, competing explanation diagram and uncertainty ledger. In the ledger, list unknown vertical datum, unrealistically simplified synthetic values, unmeasured lithology, timing uncertainty and any relevant instrument bias. Explicitly describe which claims the report cannot make. For marine hazards, resource assessment and navigational uses, do not substitute this exercise for official data or specialist review.

**Deliverables and grading:** 20% clean reproducible analysis, 20% physically coherent interpretations, 20% alternative hypotheses, 20% quantitative unit and sensitivity checks, and 20% uncertainty communication. A technically polished visualization that hides the fact that the data are synthetic cannot receive full credit. Submit the processing steps, plots, an evidence matrix and a revision note explaining which conclusion changed after reviewing uncertainties.

## Unit assessment: reasoning rather than memorization

**Question A:** Design a way to disprove the leading hypothesis for marine sediments, facies and diagenesis while spending no more than two new stations on the fictional cruise. Justify each station by the predicted difference between models.

**Question B:** Explain how an erroneous vertical datum, poor coring recovery, or inappropriate age tie point would affect at least two of the results presented in this unit. Distinguish changed numerical answers from changed geological conclusions.

**Question C:** Propose a figure caption for an unfamiliar scientific reader. It must name what was measured, the units, geographic or stratigraphic coverage, important transformations, and one explicit limitation.

**Question D:** Choose one of the unit models and identify which environmental or geological variable is intentionally held constant. Explain how failure of that constant would change the interpretation but not necessarily invalidate the model as a teaching aid.

## Further investigation and practical extension

To extend the fictional unit project into real research, start with the references and select a genuine open dataset with clear acquisition date, license, method, processing version and coordinate reference system. For marine sediments, facies and diagenesis, seek at least one direct measurement that does not originate from the same inversion as the map. Compare two spatial resolutions before discussing morphology. Keep real observations strictly separated from the invented training CSV. A reproducible report should link each plotted feature to a raw record, show how missing values were handled, and make failed interpretations visible rather than deleting them from the final narrative.


## Interactive models accompanying Unit 4

Open the HTML chapter to move the sliders and see a quantity recomputed from a transparent equation. These are intentionally simplified demonstrations; read the limitations beside each model before drawing a conclusion.

### Grain diameter in phi scale

Input: Grain size (mm); range 0.063–2; initial 0.25. Output in phi.

**Equation:** `-Math.log2(x)`. **Limit:** Ideal log scale; shape and flocculation not represented.

### Two-phase bulk sediment density

Input: Porosity fraction (fraction); range 0–0.8; initial 0.5. Output in g/cm³.

**Equation:** `2.65*(1-x)+1.03*x`. **Limit:** Single grain and fluid density; no gas or mineral variability.
