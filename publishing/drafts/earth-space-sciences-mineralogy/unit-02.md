# Unit 2 — Crystallography and internal order

## Purpose and starting assumptions

Relate translation, symmetry, crystal morphology, reciprocal-space planes, and imperfections. A crystal is a three-dimensional periodic structure, but natural crystals may be bent, intergrown, fractured, twinned, compositionally zoned, or too small for a recognizably euhedral shape. This unit connects five distinct questions rather than memorizing five disconnected lists of features. The repeated aim is to move from an observation, through a process explanation, to a testable mineralogical inference. Each topic includes at least one case in which several different explanations fit the initial evidence, so that the method teaches disciplined uncertainty rather than an automatic answer key.

## A minimum practical workflow

Before naming any mineral, record a specimen code, scale, provenance status, preservation state, and whether the observation came from a single grain or a mixed aggregate. State sample preparation and instrument configuration where relevant. Identify what data would falsify the leading interpretation and whether collecting those data is reasonable and safe. Place a label of synthetic instructional data on every constructed table or reading. Never present a model-generated number as a measurement of a real mine, outcrop or economic resource.

## Learning outcome

Build a symmetry-and-diffraction dossier from a hypothetical crystalline powder and note what remains underdetermined. Students should explain how the five lessons constrain one another, complete the worked calculations with units, and defend a conclusion that reflects—not exaggerates—the strength of the data. Include a clear distinction between observational precision, formula correctness and geological accuracy. The practical exercises are intended for supervised or non-destructive study; they are not permissions for hazardous laboratory work or environmental decisions.

## Lesson 6: Periodic lattice and unit cell

### Mechanism and scientific meaning

An ideal lattice repeats a translational motif; a unit cell spans three lattice vectors and encloses structural contents. The conventional cell is not always the primitive cell. Explain the mechanism at its appropriate scale: an atomic site, an ordered crystal, an individual grain, or a composite hand specimen. It matters whether the predicted feature belongs to a pure phase or reflects altered material surrounding it. A credible identification must distinguish the preferred phase from plausible alternatives, not merely find a familiar attribute.

### What can be observed?

A diffraction pattern samples reciprocal-space periodicity, while crystallographic databases encode lattice parameters, symmetry and atomic positions. Document instrument or test settings and the specimen identifier alongside the result; a number without measurement context can be misleading. If the phase is small, intergrown or altered, question whether the observation volume is appropriately matched to the mineral grain. Describe a feature first, then separately provide the inference that it implies.

### Case analysis with a rival explanation

**Fictional setting:** A schematic unit cell is drawn with two different edge lengths and apparently right-angle corners.

**Different causal accounts:** The sketch might be distorted by perspective; several Bravais-lattice descriptions can share similar projected appearances.

**A proposed discrimination:** Compare numerical cell parameters and indexing results rather than inferring a crystal system from a drawing.

If an observation seems to favor one account, ask what independent result would actually contradict that favored account. State whether a negative result would be decisive or might reflect detection limits, orientation or sample heterogeneity. Where the tests cannot discriminate the candidates, mark the identity unresolved rather than claiming a mineral name with unsupported certainty.

### Limitation and consequence

A lattice point is not the same object as an atom, and unit-cell edge dimensions alone do not determine chemistry. Unit-cell calculations link measured density to composition, site occupancy and uncertainty. Describe the exact claim that is supported and the more ambitious claim that must remain provisional. A result from a selected grain need not represent the host rock; a bulk assay need not identify crystal structure; and a crystallographic result need not determine geological history by itself.

### Worked quantitative example 6

**Fictional problem:** An orthorhombic cell has edges a=4 Å, b=5 Å and c=6 Å. Find its cell volume.

**Inputs:** a = 4, b = 5, c = 6. Use `a*b*c` to obtain **120 Å³**.

**Physical interpretation:** Right angles apply to this system; formula is not general. A mathematical solution is useful only after its units, input precision and model domain are checked. Try changing one input by 10 percent and determine whether the answer varies linearly, inversely or nonlinearly; explain how the changed input would be measured in practice. The full-precision answer and formula are stored in `WORKED-CASES.json` for independent computation.

### Practice and knowledge check

1. Why can two crystals of different chemistry share a lattice type?
2. Make a three-column table: directly observed evidence, what it supports, and a rival explanation. Identify an observation that could genuinely discriminate the rivals.
3. Recalculate the numerical example after modifying one input; include the original and new units and an appropriate uncertainty statement.
4. Propose a feasible and safe supplementary test and specify how the sample or instrument might introduce error.
5. In a short oral answer, name one conclusion that remains justified even if your preferred mineral identification is wrong.

## Lesson 7: Seven crystal systems and symmetry elements

### Mechanism and scientific meaning

Crystal systems organize point symmetry; operations include rotation, reflection, inversion, and rotoinversion. Real crystal faces need not reveal every internal symmetry element. Explain the mechanism at its appropriate scale: an atomic site, an ordered crystal, an individual grain, or a composite hand specimen. It matters whether the predicted feature belongs to a pure phase or reflects altered material surrounding it. A credible identification must distinguish the preferred phase from plausible alternatives, not merely find a familiar attribute.

### What can be observed?

Multiple orientations or diffraction intensity relations are needed to constrain point or space-group assignments. Document instrument or test settings and the specimen identifier alongside the result; a number without measurement context can be misleading. If the phase is small, intergrown or altered, question whether the observation volume is appropriately matched to the mineral grain. Describe a feature first, then separately provide the inference that it implies.

### Case analysis with a rival explanation

**Fictional setting:** A weathered quartz-like crystal has a six-sided outline.

**Different causal accounts:** A hexagonal-looking habit does not imply every internal diffraction symmetry; twinning and pseudo-symmetry can mislead.

**A proposed discrimination:** Measure crystallographic orientations and use diffraction-based symmetry tests.

If an observation seems to favor one account, ask what independent result would actually contradict that favored account. State whether a negative result would be decisive or might reflect detection limits, orientation or sample heterogeneity. Where the tests cannot discriminate the candidates, mark the identity unresolved rather than claiming a mineral name with unsupported certainty.

### Limitation and consequence

Confusing the hexagonal crystal family, trigonal system and an observed hexagonal outline produces classification mistakes. Symmetry predictions reduce candidate structures and guide anisotropic property measurement. Describe the exact claim that is supported and the more ambitious claim that must remain provisional. A result from a selected grain need not represent the host rock; a bulk assay need not identify crystal structure; and a crystallographic result need not determine geological history by itself.

### Worked quantitative example 7

**Fictional problem:** A hypothetical symmetry operation repeats after 60° rotations. How many operations form a complete 360° cycle?

**Inputs:** alpha = 60. Use `360/alpha` to obtain **6 rotations**.

**Physical interpretation:** This describes one rotational component, not the complete space group. A mathematical solution is useful only after its units, input precision and model domain are checked. Try changing one input by 10 percent and determine whether the answer varies linearly, inversely or nonlinearly; explain how the changed input would be measured in practice. The full-precision answer and formula are stored in `WORKED-CASES.json` for independent computation.

### Practice and knowledge check

1. Can a crystal have a six-sided external shape but belong to a lower-symmetry system?
2. Make a three-column table: directly observed evidence, what it supports, and a rival explanation. Identify an observation that could genuinely discriminate the rivals.
3. Recalculate the numerical example after modifying one input; include the original and new units and an appropriate uncertainty statement.
4. Propose a feasible and safe supplementary test and specify how the sample or instrument might introduce error.
5. In a short oral answer, name one conclusion that remains justified even if your preferred mineral identification is wrong.

## Lesson 8: Miller indices and plane geometry

### Mechanism and scientific meaning

Integer Miller indices encode reciprocal intercepts of lattice planes after reducing fractions; a zero index means parallelism to the corresponding crystallographic axis. Explain the mechanism at its appropriate scale: an atomic site, an ordered crystal, an individual grain, or a composite hand specimen. It matters whether the predicted feature belongs to a pure phase or reflects altered material surrounding it. A credible identification must distinguish the preferred phase from plausible alternatives, not merely find a familiar attribute.

### What can be observed?

Planar spacings can be related to diffraction peaks; the correct metric depends on the crystal system, and cubic simplifications must not be transferred blindly. Document instrument or test settings and the specimen identifier alongside the result; a number without measurement context can be misleading. If the phase is small, intergrown or altered, question whether the observation volume is appropriately matched to the mineral grain. Describe a feature first, then separately provide the inference that it implies.

### Case analysis with a rival explanation

**Fictional setting:** A cube-shaped specimen shows a repeated set of equally spaced planar markings.

**Different causal accounts:** Growth striations, actual cleavage, and mechanically produced scratches can all yield parallel visual traces.

**A proposed discrimination:** Use orientation-consistent diffraction measurements, not surface markings alone, to establish a plane family.

If an observation seems to favor one account, ask what independent result would actually contradict that favored account. State whether a negative result would be decisive or might reflect detection limits, orientation or sample heterogeneity. Where the tests cannot discriminate the candidates, mark the identity unresolved rather than claiming a mineral name with unsupported certainty.

### Limitation and consequence

Mixing directions [uvw], single planes (hkl), and families {hkl} changes the claim being made. Indexing enables reproducible comparisons between modeled structures and observed peaks. Describe the exact claim that is supported and the more ambitious claim that must remain provisional. A result from a selected grain need not represent the host rock; a bulk assay need not identify crystal structure; and a crystallographic result need not determine geological history by itself.

### Worked quantitative example 8

**Fictional problem:** For a cubic lattice with a=4 Å, find d(111) from d=a/sqrt(h²+k²+l²).

**Inputs:** a = 4, h = 1, k = 1, l = 1. Use `a/math.sqrt(h*h+k*k+l*l)` to obtain **2.3094 Å**.

**Physical interpretation:** Use only for cubic geometry. A mathematical solution is useful only after its units, input precision and model domain are checked. Try changing one input by 10 percent and determine whether the answer varies linearly, inversely or nonlinearly; explain how the changed input would be measured in practice. The full-precision answer and formula are stored in `WORKED-CASES.json` for independent computation.

### Practice and knowledge check

1. Explain why changing a plane index does not automatically change chemical composition.
2. Make a three-column table: directly observed evidence, what it supports, and a rival explanation. Identify an observation that could genuinely discriminate the rivals.
3. Recalculate the numerical example after modifying one input; include the original and new units and an appropriate uncertainty statement.
4. Propose a feasible and safe supplementary test and specify how the sample or instrument might introduce error.
5. In a short oral answer, name one conclusion that remains justified even if your preferred mineral identification is wrong.

## Lesson 9: Twinning, growth zoning and habit

### Mechanism and scientific meaning

Twins share crystallographically specified orientation relations; growth zoning records changes in composition or growth conditions, while sector zoning can arise from face-specific incorporation. Explain the mechanism at its appropriate scale: an atomic site, an ordered crystal, an individual grain, or a composite hand specimen. It matters whether the predicted feature belongs to a pure phase or reflects altered material surrounding it. A credible identification must distinguish the preferred phase from plausible alternatives, not merely find a familiar attribute.

### What can be observed?

Crossed polarizers, electron imaging and spatially resolved chemistry distinguish optical twins, deformation twins and compositional bands. Document instrument or test settings and the specimen identifier alongside the result; a number without measurement context can be misleading. If the phase is small, intergrown or altered, question whether the observation volume is appropriately matched to the mineral grain. Describe a feature first, then separately provide the inference that it implies.

### Case analysis with a rival explanation

**Fictional setting:** A plagioclase grain shows stripes in a thin section, but the stripes terminate irregularly.

**Different causal accounts:** Polysynthetic twinning, exsolution lamellae, alteration seams or cutting artifacts require different explanations.

**A proposed discrimination:** Rotate the stage and compare extinction with element maps and microtextures.

If an observation seems to favor one account, ask what independent result would actually contradict that favored account. State whether a negative result would be decisive or might reflect detection limits, orientation or sample heterogeneity. Where the tests cannot discriminate the candidates, mark the identity unresolved rather than claiming a mineral name with unsupported certainty.

### Limitation and consequence

A twin boundary is not automatically a metamorphic event marker; some twins form during growth. Correct interpretation informs cooling history and later deformation without assuming a single cause. Describe the exact claim that is supported and the more ambitious claim that must remain provisional. A result from a selected grain need not represent the host rock; a bulk assay need not identify crystal structure; and a crystallographic result need not determine geological history by itself.

### Worked quantitative example 9

**Fictional problem:** 18 of 42 plagioclase grains show visible twin bands. Estimate prevalence in this selected thin-section traverse.

**Inputs:** n = 18, N = 42. Use `100*n/N` to obtain **42.8571 %**.

**Physical interpretation:** Thin-section orientation controls twin detectability. A mathematical solution is useful only after its units, input precision and model domain are checked. Try changing one input by 10 percent and determine whether the answer varies linearly, inversely or nonlinearly; explain how the changed input would be measured in practice. The full-precision answer and formula are stored in `WORKED-CASES.json` for independent computation.

### Practice and knowledge check

1. What evidence would demonstrate that zoning predates a later deformation event?
2. Make a three-column table: directly observed evidence, what it supports, and a rival explanation. Identify an observation that could genuinely discriminate the rivals.
3. Recalculate the numerical example after modifying one input; include the original and new units and an appropriate uncertainty statement.
4. Propose a feasible and safe supplementary test and specify how the sample or instrument might introduce error.
5. In a short oral answer, name one conclusion that remains justified even if your preferred mineral identification is wrong.

## Lesson 10: Crystal defects and diffraction peak width

### Mechanism and scientific meaning

Vacancies, substitutions, interstitials, dislocations and stacking faults interrupt perfect order. Domain size and microstrain can both broaden diffraction peaks; instrumental broadening adds another component. Explain the mechanism at its appropriate scale: an atomic site, an ordered crystal, an individual grain, or a composite hand specimen. It matters whether the predicted feature belongs to a pure phase or reflects altered material surrounding it. A credible identification must distinguish the preferred phase from plausible alternatives, not merely find a familiar attribute.

### What can be observed?

Peak shapes, electron microscopy and controlled annealing experiments can constrain defects, but a single broad peak rarely gives a unique defect mechanism. Document instrument or test settings and the specimen identifier alongside the result; a number without measurement context can be misleading. If the phase is small, intergrown or altered, question whether the observation volume is appropriately matched to the mineral grain. Describe a feature first, then separately provide the inference that it implies.

### Case analysis with a rival explanation

**Fictional setting:** A clay-rich sample has much broader peaks than a crystalline quartz standard.

**Different causal accounts:** Nanometer-scale domains, lattice disorder, hydration state, interlayer mixing and instrumental effects may contribute.

**A proposed discrimination:** Measure a standard under identical conditions, examine humidity treatment and compare multiple reflections.

If an observation seems to favor one account, ask what independent result would actually contradict that favored account. State whether a negative result would be decisive or might reflect detection limits, orientation or sample heterogeneity. Where the tests cannot discriminate the candidates, mark the identity unresolved rather than claiming a mineral name with unsupported certainty.

### Limitation and consequence

Treating the Scherrer estimate as true particle size ignores strain and particle morphology. Defect descriptions help assess reaction rate, mechanical properties and catalytic activity. Describe the exact claim that is supported and the more ambitious claim that must remain provisional. A result from a selected grain need not represent the host rock; a bulk assay need not identify crystal structure; and a crystallographic result need not determine geological history by itself.

### Worked quantitative example 10

**Fictional problem:** Estimate an apparent coherent-domain size by D=Kλ/(βcosθ), with K=.9, λ=.154 nm, β=.003 rad and θ=15°.

**Inputs:** K = 0.9, lam = 0.154, beta = 0.003, theta = 15. Use `K*lam/(beta*math.cos(math.radians(theta)))` to obtain **47.8298 nm**.

**Physical interpretation:** Broadening must be instrument-corrected and strain separated. A mathematical solution is useful only after its units, input precision and model domain are checked. Try changing one input by 10 percent and determine whether the answer varies linearly, inversely or nonlinearly; explain how the changed input would be measured in practice. The full-precision answer and formula are stored in `WORKED-CASES.json` for independent computation.

### Practice and knowledge check

1. Why does instrumental deconvolution matter before interpreting peak broadening?
2. Make a three-column table: directly observed evidence, what it supports, and a rival explanation. Identify an observation that could genuinely discriminate the rivals.
3. Recalculate the numerical example after modifying one input; include the original and new units and an appropriate uncertainty statement.
4. Propose a feasible and safe supplementary test and specify how the sample or instrument might introduce error.
5. In a short oral answer, name one conclusion that remains justified even if your preferred mineral identification is wrong.

## Integrative investigation 2: Indexing an invented powder pattern

### Research problem and scope

Consider an ideal cubic teaching crystal with cell edge 4 Å and assumed single-phase diffraction reflections assigned to (100), (110), and (111). Compute the family spacings with d=a/sqrt(h²+k²+l²), taking care not to confuse the plane and direction symbols. Describe how the reciprocal relation makes higher-index families generally have smaller d. Draw three planes intersecting a conventional cube, and explain what each drawing omits about actual basis atoms. Next introduce an imaginary sample with broadened peaks; discuss coherent-domain length, microstrain, zero shift and instrumental broadening before offering a size estimate. No mineral identity is guaranteed: any candidate lattice must also be compatible with peak intensities, absences, symmetry and chemical evidence.

### Synthetic analysis and interpretation

Students can simulate imperfect datasets by multiplying every ideal d value by a small calibration factor while adding independent random scatter, explicitly seeded and labeled synthetic. Calculate which error affects every reflection systematically and which contributes point-by-point uncertainty. Derive the cubic value a_i=d_i*sqrt(h²+k²+l²) from each indexed reflection and compare the spread. If the lattice parameters disagree beyond reasonable uncertainty, consider misindexing, multiple phases, noncubic symmetry or instrument geometry. End with a written referee report rejecting a phase identification based only on one intense peak. Explain why assigning an index is a hypothesis about structure rather than a pattern-matching decoration.

### Practical workflow, phase 1 — sampling and the question

Start with the decision that the study is supposed to support: Build a symmetry-and-diffraction dossier from a hypothetical crystalline powder and note what remains underdetermined. Make a numbered sampling plan rather than collecting data opportunistically. For each proposed specimen list selection criteria, sampling location or teaching provenance, predicted heterogeneity, the expected spatial scale of the relevant mineral property, and how the sample will be preserved. Selection effects are part of the result. If the question concerns a trace phase, one homogenized bulk measurement can destroy the very spatial context needed to locate the phase; if the question concerns average composition, selecting only the most interesting-looking grain can severely bias the answer. Explain how the objective determines whether you prioritize hand specimen, polished section, thin section, powder, or in-situ analysis.

### Phase 2 — measurement, calibration and reproducibility

Prepare a record of instrument or classroom method, date, operator, settings, standards, detection limits and data-processing steps. Put raw observations in one table and proposed mineral names in another. Record replicates rather than silently combining them; when results disagree, ask whether the difference is repeatability, spatial heterogeneity, true chemical zoning or changing ambient conditions. The fictional dataset in `datasets/unit-02.csv` demonstrates the mechanics of a tidy table without pretending to represent a geological location. Choose one column as a measurement proxy, sketch it against sample index, and identify whether its pattern justifies a mechanistic inference. An upward trend in arbitrary proxy numbers is not evidence of a geological reaction unless calibration, spatial metadata, and a physically meaningful causal model exist.

### Phase 3 — competing explanatory models

Write a first hypothesis using the principal mechanism of this unit: Relate translation, symmetry, crystal morphology, reciprocal-space planes, and imperfections. Then write a genuinely different hypothesis consistent with the same initial observations, motivated by this difficulty: A crystal is a three-dimensional periodic structure, but natural crystals may be bent, intergrown, fractured, twinned, compositionally zoned, or too small for a recognizably euhedral shape. Predict three distinct outcomes under each model. A useful discriminating observation is not merely “more data”; it is a measurement whose possible results change the relative plausibility of the competing models. Look for possible confounding by sample alteration, orientation, unrecognized intergrowths, selection effects, data reduction, or unknown provenance. If the rival models yield identical predictions at the available scale, report non-identifiability rather than assigning a fabricated confidence percentage.

### Phase 4 — quantitative reasoning with the five lesson calculations

Use the worked problems from lessons 6–10 as transparent reference calculations. For each, reproduce the numeric answer and unit, then change one input and compute a sensitivity ratio. Record where a method assumes a pure single mineral, a cubic structure, a fixed section thickness, homogeneous mixing, or other simplifications. A reasonable mathematical curve is not a calibrated natural-system model. Review whether an expression is dimensionally consistent and whether it predicts nonsensical behavior near a boundary. If so, state the domain of validity and what physical effects the equation leaves out. Keep the numerical assumptions adjacent to the output chart to prevent reuse outside their teaching context.

### Phase 5 — reporting and oral defense

Create a short abstract that states the question and the bounded conclusion. Attach specimen metadata, a simple observation matrix, a calculation table, a list of candidate phases, the diagnostic evidence, two remaining uncertainties and a prioritized next measurement. Provide raw measurements or enough metadata for an independent reanalysis; use sample identifiers that link photographs to laboratory measurements. Ask a second group to read the data without seeing the original conclusion and record whether they reach the same phase family, a different species, or a justified unresolved answer. In oral defense, identify the strongest contradicting observation and explain what would make you revise your preferred explanation. If practical environmental, engineering or economic consequences arise, clearly refer those judgments to qualified professionals and independently validated measurements.

### Laboratory questions

1. Which of the proposed tests is both least destructive and most likely to exclude a strong competitor? Justify the tradeoff.
2. What is the main difference between analytical precision, phase identification accuracy and geological representativeness in this specific case?
3. How could a small inclusion, alteration rim or unfavorable crystallographic orientation change the apparent result without changing the core mineral identity?
4. Which inference is robust to losing one of the observations? Which collapses if a single measurement proves wrong?
5. State a conclusion under three scenarios: predicted data, unexpectedly contradictory data and measurements below detection. Do not force a species name when evidence is ambiguous.

## Unit 2 synthesis and transferable habits

A mineralogical investigation should end with a table of claims rather than an unqualified list of mineral names. Distinguish observations made directly by a person or instrument from derived values computed with a model. List each candidate identification together with supporting and contradicting properties. For every contested phase, write down the independent measurement that would change the answer and whether that test is feasible, safe and appropriately calibrated. Each step should preserve the ability to revisit the original evidence when instruments or classifications improve.

Compare the five lessons by placing their central quantities on a scale ladder: atomic or unit-cell dimensions, crystalline domains, grains, hand specimens and whole-rock assemblages. A model valid on one rung cannot automatically be applied to another. Where phases have the same elements but different structures, elemental assays must be complemented by phase-sensitive measurements. Where a crystal is chemically zoned, one bulk analysis may erase the growth sequence. Where an aggregate has pores or inclusions, mass-volume density reflects the composite rather than a pure end member.

For a short written exam, choose two of the unit's computations, recreate both results, and evaluate the meaning of a plausible measurement uncertainty. Report units and assumptions before providing a final rounded value. Then construct a fresh hypothetical sample that could fool a student who learned only the most visible property. Explain why your preferred test actually discriminates between the candidates. This synthesis is intended to improve scientific reasoning rather than encourage another memorized identification rule.
