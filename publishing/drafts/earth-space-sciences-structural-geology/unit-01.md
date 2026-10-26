# Unit 1 — Geometry and orientation of geological structures

## Central question

Description, coordinates and uncertainty. Describe structural orientations reproducibly before making tectonic inferences

## Extended unit perspective

The first task in structural geology is to make geometrically explicit observations. A tilted bedding plane, a foliation, and an exposed fracture may all look like lines from a distance. Their geometries are planes in three-dimensional space, intersecting a weathered and eroded surface. In a field notebook, distinguish the orientation of an individual surface from the trace drawn on a horizontal map. A compass measurement is only one sample of that surface; natural surfaces are rough, anisotropic, and sometimes curved. Magnetic declination, dip quadrant, north reference and right-hand-rule conventions must accompany measurements if another person is expected to reproduce them. Combining data from separate structural domains into a single mean may conceal an important geological boundary. Most importantly, geometry is not process. A particular orientation pattern may be produced by folding, rotation about a fault, tilting during sedimentation, or several later deformation episodes. A useful structural map carries the observations separately from the reconstructed movement history. In this unit students should explicitly draw local x, y and z axes, show the horizontal projection of a line, and describe which rotations or projections convert observed directions into map symbols. A stereonet is an aid to comparing orientations, not a substitution for an actual stratigraphic section. Where an exposure is covered, mark missing evidence rather than drawing confident structure through it.

### Field and scientific objectives

Describe relevant structural objects with location and orientation, translate them between map and section, construct a physically and chronologically consistent interpretation, and test at least one alternative. The aim is to communicate exactly which information is observed, which result follows by geometric calculation and which regional mechanism is inferred. Avoid interpreting one structural indicator as proof of a single tectonic event where earlier deformation, reactivation or anisotropic rock properties remain plausible.

## Five core lessons and worked cases
## Lesson 1.1 — Strike, dip and right-hand-rule notation

### Mechanism and observational scale

A plane's strike is the azimuth of a horizontal line lying in it; dip is its steepest descent perpendicular to strike, with the dip direction removing an otherwise ambiguous 180-degree choice. Draw a basic geometric sketch and define the coordinate system, sample orientation and reference state if one is needed. 

### Evidence and documentation

Brunton or digital compass readings and three-dimensional bedding traces constrain orientation, while slope and magnetic interference can bias measurements. Document the exposure, instrument or measurement technique, scale and uncertainty before discussing tectonic implications. Maintain an observation/inference table with **orientation convention, instrument calibration and exact outcrop identity** and illustrate **observed contact, corrected orientation and map trace**. If your evidence is a two-dimensional trace of a three-dimensional surface, state exactly what its projection does and does not resolve. 

### Competing interpretation

A lineament drawn on a map need not coincide with bedding strike, and a weathered planar joint may be mistaken for sedimentary bedding. Record expected results for each explanation before carrying out the test. A model requiring hidden geometry must mark that geometry as inferred.

### Test and scientific protocol

Record strike, dip magnitude, dip quadrant, measurement station, elevation and contact identity; compare corrected and uncorrected measurements with a second operator. State the predicted direction, location, quantity or material signature under both models. Use at least one measurement not previously employed to construct the model. For **strike, dip and right-hand-rule notation**, define sample selection criteria, coordinate conventions and an acceptable range of observation error. 

### Worked numerical case 1: Apparent dip in oblique exposure

**Invented classroom inputs:** true dip 36°, section makes 52° to strike. Evaluate `math.degrees(math.atan(math.tan(math.radians(36))*math.sin(math.radians(52))))` to obtain **29.7921 degrees**. Write the governing equation separately, substitute the stated values, and check the dimensions and sign convention. For a trigonometric expression identify whether angles are entered in radians or degrees; for percentages identify the reference length or population. 

Repeat the calculation after varying the least certain input. Explain whether the change is important relative to plausible field error. If the formula neglects a deformation component, assumes a planar fault or uses a restricted stress model, identify that assumption rather than interpreting the number as exact. Distinguish geometric separation from true displacement, finite strain from its time rate and stress from material strength whenever those concepts arise in the calculation. 

### Limitation, cross-check and synthesis

Magnetic disturbance, overturned bedding and irregular surfaces violate the notion of a perfect single plane. Consider the alternative that changes the interpretation most while retaining the measured observations. Make a two-column field record. Put verifiable geometric and material facts in the left column and causal or historical interpretation in the right. For each interpreted event, cite the specific measured feature and its location. An interpretation without such a link is a hypothesis to test rather than a supported result. 

Use a consistent azimuth convention and state explicitly whether orientation is measured or inferred. A defensible conclusion therefore has five components: observed feature, ideal relation used, leading interpretation, decisive contrary test and residual uncertainty. Indicate whether each is local to the measured exposure or can legitimately be extended across the mapped domain.

### Practice

1. Sketch **strike, dip and right-hand-rule notation** with orientation or movement arrows and a north or section reference.
2. List three direct observations and identify a plausible rival mechanism.
3. Recalculate case 1 for a revised parameter, retaining meaningful units.
4. Design a two-site or two-orientation test that distinguishes the interpretations.
5. Write a short final paragraph reporting what remains uncertain and which measurement would reduce the uncertainty.

## Lesson 1.2 — Apparent dip and map geometry

### Mechanism and observational scale

True dip is the maximum inclination in the dip direction; sections cut obliquely to strike display smaller apparent dip according to the section azimuth. Draw a basic geometric sketch and define the coordinate system, sample orientation and reference state if one is needed. 

### Evidence and documentation

The same bedding surface exposed on north- and east-facing cuts may show different apparent angles without any geological rotation. Document the exposure, instrument or measurement technique, scale and uncertainty before discussing tectonic implications. Maintain an observation/inference table with **orientation convention, instrument calibration and exact outcrop identity** and illustrate **observed contact, corrected orientation and map trace**. If your evidence is a two-dimensional trace of a three-dimensional surface, state exactly what its projection does and does not resolve. 

### Competing interpretation

Changing dip between roadcuts can instead reflect real folding or spatial variation of bedding. Record expected results for each explanation before carrying out the test. A model requiring hidden geometry must mark that geometry as inferred.

### Test and scientific protocol

Predict apparent dip for a known section azimuth using tangent geometry, then compare with measured traces in two perpendicular exposures. State the predicted direction, location, quantity or material signature under both models. Use at least one measurement not previously employed to construct the model. For **apparent dip and map geometry**, define sample selection criteria, coordinate conventions and an acceptable range of observation error. 

### Worked numerical case 2: True bed thickness on horizontal traverse

**Invented classroom inputs:** 7.4 m measured horizontally perpendicular to strike; bedding 32° dip. Evaluate `7.4*math.sin(math.radians(32))` to obtain **3.9214 m**. Write the governing equation separately, substitute the stated values, and check the dimensions and sign convention. For a trigonometric expression identify whether angles are entered in radians or degrees; for percentages identify the reference length or population. 

Repeat the calculation after varying the least certain input. Explain whether the change is important relative to plausible field error. If the formula neglects a deformation component, assumes a planar fault or uses a restricted stress model, identify that assumption rather than interpreting the number as exact. Distinguish geometric separation from true displacement, finite strain from its time rate and stress from material strength whenever those concepts arise in the calculation. 

### Limitation, cross-check and synthesis

The equation assumes a locally planar surface and a properly defined angle from strike. Consider the alternative that changes the interpretation most while retaining the measured observations. Write two incompatible predictions *before* inspecting another observation. Make one prediction spatial, such as a contact location or expected change in orientation, and the other material, such as fault rock or crosscutting microstructure. Explain which result could falsify the leading model. 

A valid three-dimensional interpretation fits all independent apparent-dip views at once. A defensible conclusion therefore has five components: observed feature, ideal relation used, leading interpretation, decisive contrary test and residual uncertainty. Indicate whether each is local to the measured exposure or can legitimately be extended across the mapped domain.

### Practice

1. Sketch **apparent dip and map geometry** with orientation or movement arrows and a north or section reference.
2. List three direct observations and identify a plausible rival mechanism.
3. Recalculate case 2 for a revised parameter, retaining meaningful units.
4. Design a two-site or two-orientation test that distinguishes the interpretations.
5. Write a short final paragraph reporting what remains uncertain and which measurement would reduce the uncertainty.

## Lesson 1.3 — Geologic map symbols and contacts

### Mechanism and observational scale

The map trace of a bedding contact reflects topography, the attitude of the contact and erosion; contacts are intersections of surfaces rather than independent line drawings. Draw a basic geometric sketch and define the coordinate system, sample orientation and reference state if one is needed. 

### Evidence and documentation

Outcrop elevations, contact positions, contour lines and recorded attitudes should predict each other on a topographic base. Document the exposure, instrument or measurement technique, scale and uncertainty before discussing tectonic implications. Maintain an observation/inference table with **orientation convention, instrument calibration and exact outcrop identity** and illustrate **observed contact, corrected orientation and map trace**. If your evidence is a two-dimensional trace of a three-dimensional surface, state exactly what its projection does and does not resolve. 

### Competing interpretation

A curved trace may be caused by a horizontal bed crossing a winding valley rather than a fold hinge. Record expected results for each explanation before carrying out the test. A model requiring hidden geometry must mark that geometry as inferred.

### Test and scientific protocol

Fit a plane through at least three well-located contact points, predict its trace across a new contour and check it against an unmapped outcrop. State the predicted direction, location, quantity or material signature under both models. Use at least one measurement not previously employed to construct the model. For **geologic map symbols and contacts**, define sample selection criteria, coordinate conventions and an acceptable range of observation error. 

### Worked numerical case 3: Vertical difference between mapped contour crossings

**Invented classroom inputs:** two mapped contact intersections at 460 and 405 m elevation. Evaluate `460-405` to obtain **55 m**. Write the governing equation separately, substitute the stated values, and check the dimensions and sign convention. For a trigonometric expression identify whether angles are entered in radians or degrees; for percentages identify the reference length or population. 

Repeat the calculation after varying the least certain input. Explain whether the change is important relative to plausible field error. If the formula neglects a deformation component, assumes a planar fault or uses a restricted stress model, identify that assumption rather than interpreting the number as exact. Distinguish geometric separation from true displacement, finite strain from its time rate and stress from material strength whenever those concepts arise in the calculation. 

### Limitation, cross-check and synthesis

Sparse control and relief distort the apparent structural complexity of map patterns. Consider the alternative that changes the interpretation most while retaining the measured observations. Identify the least certain input, vary it by a physically plausible amount, and show its effect on the computed result. Variation in a trigonometric angle may produce a nonlinear uncertainty even where angle readings appear precise. Report significant figures in proportion to the instrument and assumptions. 

Draw map geometry independently of the geological story before naming folds or faults. A defensible conclusion therefore has five components: observed feature, ideal relation used, leading interpretation, decisive contrary test and residual uncertainty. Indicate whether each is local to the measured exposure or can legitimately be extended across the mapped domain.

### Practice

1. Sketch **geologic map symbols and contacts** with orientation or movement arrows and a north or section reference.
2. List three direct observations and identify a plausible rival mechanism.
3. Recalculate case 3 for a revised parameter, retaining meaningful units.
4. Design a two-site or two-orientation test that distinguishes the interpretations.
5. Write a short final paragraph reporting what remains uncertain and which measurement would reduce the uncertainty.

## Lesson 1.4 — Lineations, trend and plunge

### Mechanism and observational scale

An oriented line is specified by horizontal trend and downward plunge, distinct from the strike and dip used for a plane. Draw a basic geometric sketch and define the coordinate system, sample orientation and reference state if one is needed. 

### Evidence and documentation

Mineral elongation, stretching lineations, intersection lineations and fold axes can have similar orientations but different origins. Document the exposure, instrument or measurement technique, scale and uncertainty before discussing tectonic implications. Maintain an observation/inference table with **orientation convention, instrument calibration and exact outcrop identity** and illustrate **observed contact, corrected orientation and map trace**. If your evidence is a two-dimensional trace of a three-dimensional surface, state exactly what its projection does and does not resolve. 

### Competing interpretation

A linear groove may be glacial striation or fault slickenside rather than tectonic stretching of rock. Record expected results for each explanation before carrying out the test. A model requiring hidden geometry must mark that geometry as inferred.

### Test and scientific protocol

Measure the three-dimensional line, its host surface and crosscutting fabric, then test whether neighboring exposures display the same vector. State the predicted direction, location, quantity or material signature under both models. Use at least one measurement not previously employed to construct the model. For **lineations, trend and plunge**, define sample selection criteria, coordinate conventions and an acceptable range of observation error. 

### Worked numerical case 4: Lineation plunge from components

**Invented classroom inputs:** downward change 3.2 m over 8.6 m horizontal displacement. Evaluate `math.degrees(math.atan2(3.2,8.6))` to obtain **20.4099 degrees**. Write the governing equation separately, substitute the stated values, and check the dimensions and sign convention. For a trigonometric expression identify whether angles are entered in radians or degrees; for percentages identify the reference length or population. 

Repeat the calculation after varying the least certain input. Explain whether the change is important relative to plausible field error. If the formula neglects a deformation component, assumes a planar fault or uses a restricted stress model, identify that assumption rather than interpreting the number as exact. Distinguish geometric separation from true displacement, finite strain from its time rate and stress from material strength whenever those concepts arise in the calculation. 

### Limitation, cross-check and synthesis

A line has orientation but may lack a known shear sense; lineation direction alone is not a displacement history. Consider the alternative that changes the interpretation most while retaining the measured observations. Translate the interpretation between a map, a cross-section and a three-dimensional conceptual diagram. Check that all three representations show compatible orientations and movement directions. A model that works in one section but fails in map view needs revision. 

Never infer fault motion merely from lineation trend. A defensible conclusion therefore has five components: observed feature, ideal relation used, leading interpretation, decisive contrary test and residual uncertainty. Indicate whether each is local to the measured exposure or can legitimately be extended across the mapped domain.

### Practice

1. Sketch **lineations, trend and plunge** with orientation or movement arrows and a north or section reference.
2. List three direct observations and identify a plausible rival mechanism.
3. Recalculate case 4 for a revised parameter, retaining meaningful units.
4. Design a two-site or two-orientation test that distinguishes the interpretations.
5. Write a short final paragraph reporting what remains uncertain and which measurement would reduce the uncertainty.

## Lesson 1.5 — Stereographic projections and orientation populations

### Mechanism and observational scale

Lower-hemisphere equal-angle and equal-area stereonets project directions and planes to two dimensions while preserving different geometric properties. Draw a basic geometric sketch and define the coordinate system, sample orientation and reference state if one is needed. 

### Evidence and documentation

Pole clusters can reveal bedding populations, girdles can reveal cylindrical fold geometry and great circles represent measured planes. Document the exposure, instrument or measurement technique, scale and uncertainty before discussing tectonic implications. Maintain an observation/inference table with **orientation convention, instrument calibration and exact outcrop identity** and illustrate **observed contact, corrected orientation and map trace**. If your evidence is a two-dimensional trace of a three-dimensional surface, state exactly what its projection does and does not resolve. 

### Competing interpretation

A girdle in pooled data can arise from sampling several unrelated domains rather than one regional fold. Record expected results for each explanation before carrying out the test. A model requiring hidden geometry must mark that geometry as inferred.

### Test and scientific protocol

Plot each measurement with domain labels and error estimates, calculate mean orientation only when the population is meaningful, and examine outliers. State the predicted direction, location, quantity or material signature under both models. Use at least one measurement not previously employed to construct the model. For **stereographic projections and orientation populations**, define sample selection criteria, coordinate conventions and an acceptable range of observation error. 

### Worked numerical case 5: Fraction of poles in one structural domain

**Invented classroom inputs:** 23 out of 31 poles meet a specified domain criterion. Evaluate `100*23/31` to obtain **74.1935 %**. Write the governing equation separately, substitute the stated values, and check the dimensions and sign convention. For a trigonometric expression identify whether angles are entered in radians or degrees; for percentages identify the reference length or population. 

Repeat the calculation after varying the least certain input. Explain whether the change is important relative to plausible field error. If the formula neglects a deformation component, assumes a planar fault or uses a restricted stress model, identify that assumption rather than interpreting the number as exact. Distinguish geometric separation from true displacement, finite strain from its time rate and stress from material strength whenever those concepts arise in the calculation. 

### Limitation, cross-check and synthesis

Pole density is sensitive to projection type, uneven sampling and clustered stations. Consider the alternative that changes the interpretation most while retaining the measured observations. List which surfaces or fabrics predate which others using direct cut, fold, overprint or growth relations. Leave pairs unordered where no observation establishes priority. Reactivation means a single surface may occur more than once in the event graph. 

Interpret a stereonet together with geological location and facing evidence, not as an independent tectonic map. A defensible conclusion therefore has five components: observed feature, ideal relation used, leading interpretation, decisive contrary test and residual uncertainty. Indicate whether each is local to the measured exposure or can legitimately be extended across the mapped domain.

### Practice

1. Sketch **stereographic projections and orientation populations** with orientation or movement arrows and a north or section reference.
2. List three direct observations and identify a plausible rival mechanism.
3. Recalculate case 5 for a revised parameter, retaining meaningful units.
4. Design a two-site or two-orientation test that distinguishes the interpretations.
5. Write a short final paragraph reporting what remains uncertain and which measurement would reduce the uncertainty.
## Integrated investigation 1 — Reconstruct an overturned contact

A fictional map covers a 2.5 km wide ridge with a sandstone–shale contact exposed at five elevations and three bedding attitudes. Produce two models: a uniformly dipping planar contact and a shallow plunging fold with one overturned limb. Sketch predicted traces on each contour, select where to test younging indicators and mark the difference between observed contact and inferred continuation. If a stereonet girdle is present, compare its pole with a directly measured fold axis. Deliver an error table for compass bearing, GPS point location and section orientation.

### Analysis protocol and deliverables

The following integrated investigation uses fictional measurements expressly manufactured to demonstrate methods. It is not a published field survey or a substitute for collecting data. Begin with original measurements and metadata; present interpreted structures in separate layers. Compute at least one simple quantity with its units, make two competing predictions, and decide which additional piece of evidence would be most informative. Report any failure of the data to distinguish models. Submit a map or diagram, annotated calculations, a brief uncertainty table and a paragraph explaining whether the result has any practical limitations. The first panel of the submitted figure should contain observations only. The second may show an inferred geometry, but include a legend differentiating solid observation lines from dashed extrapolations. The third should compare an alternative model and identify the measurement that would select between them. A model should be judged against the data it did **not** use for fitting whenever possible.

### Interpreting the synthetic dataset

Open `datasets/unit-01.csv` from the offline reader. All station names, orientations, distances and categories in this CSV are fictional. Plot the values and report which trend, if any, is robust against removal of two observations. Where the data do not contain enough directional or temporal context to support a tectonic claim, write that limitation explicitly. Do not claim a physical trend is established just because a graphing tool draws a smooth line.

### Independent review

Exchange interpretations with another student. Ask them to identify one term or symbol whose meaning is unclear, one unstated convention and one observation that could disprove the preferred reconstruction. Revise the final diagram to make these items visible. Grade the work on measurement transparency and falsifiability, not on whether every student selected the same visually attractive fault or fold model.
