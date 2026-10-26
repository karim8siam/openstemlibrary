# Unit 7 — Analytical and computational mineralogy

## Purpose and starting assumptions

Select measurement methods and evaluate the claims each instrument can support. A technique has an observation scale, detection limit, interference structure, calibration demand and sample preparation cost. Two analyses may disagree because they observe different volumes or answer different questions. This unit connects five distinct questions rather than memorizing five disconnected lists of features. The repeated aim is to move from an observation, through a process explanation, to a testable mineralogical inference. Each topic includes at least one case in which several different explanations fit the initial evidence, so that the method teaches disciplined uncertainty rather than an automatic answer key.

## A minimum practical workflow

Before naming any mineral, record a specimen code, scale, provenance status, preservation state, and whether the observation came from a single grain or a mixed aggregate. State sample preparation and instrument configuration where relevant. Identify what data would falsify the leading interpretation and whether collecting those data is reasonable and safe. Place a label of synthetic instructional data on every constructed table or reading. Never present a model-generated number as a measurement of a real mine, outcrop or economic resource.

## Learning outcome

Choose an analytical workflow that respects preservation, data quality, cost and reproducibility. Students should explain how the five lessons constrain one another, complete the worked calculations with units, and defend a conclusion that reflects—not exaggerates—the strength of the data. Include a clear distinction between observational precision, formula correctness and geological accuracy. The practical exercises are intended for supervised or non-destructive study; they are not permissions for hazardous laboratory work or environmental decisions.

## Lesson 31: Sampling, preparation and contamination

### Mechanism and scientific meaning

Analytical results depend on which volume was sampled, how it was subdivided, preparation-induced alteration and contamination. A phase concentrated in a vein may be absent from a random bulk powder. Explain the mechanism at its appropriate scale: an atomic site, an ordered crystal, an individual grain, or a composite hand specimen. It matters whether the predicted feature belongs to a pure phase or reflects altered material surrounding it. A credible identification must distinguish the preferred phase from plausible alternatives, not merely find a familiar attribute.

### What can be observed?

Field duplicates, blanks, standard reference material and chain-of-custody metadata can expose preparation problems. Document instrument or test settings and the specimen identifier alongside the result; a number without measurement context can be misleading. If the phase is small, intergrown or altered, question whether the observation volume is appropriately matched to the mineral grain. Describe a feature first, then separately provide the inference that it implies.

### Case analysis with a rival explanation

**Fictional setting:** One powdered aliquot shows abundant mica while a neighboring polished section contains little mica.

**Different causal accounts:** Heterogeneous grain distribution, orientation, sampling bias or accidental contamination may explain the discrepancy.

**A proposed discrimination:** Use a documented sampling plan and matched split samples for repeat analyses.

If an observation seems to favor one account, ask what independent result would actually contradict that favored account. State whether a negative result would be decisive or might reflect detection limits, orientation or sample heterogeneity. Where the tests cannot discriminate the candidates, mark the identity unresolved rather than claiming a mineral name with unsupported certainty.

### Limitation and consequence

Grinding may smear soft minerals, oxidize reactive phases or redistribute fine particles. Preparation protocols should preserve the geological question as well as analytical sensitivity. Describe the exact claim that is supported and the more ambitious claim that must remain provisional. A result from a selected grain need not represent the host rock; a bulk assay need not identify crystal structure; and a crystallographic result need not determine geological history by itself.

### Worked quantitative example 31

**Fictional problem:** Seven blanks and controls accompany 40 unknown specimens. Find control count as percentage of unknown count.

**Inputs:** controls = 7, unknowns = 40. Use `100*controls/unknowns` to obtain **17.5 %**.

**Physical interpretation:** This is documentation, not a universal required QA ratio. A mathematical solution is useful only after its units, input precision and model domain are checked. Try changing one input by 10 percent and determine whether the answer varies linearly, inversely or nonlinearly; explain how the changed input would be measured in practice. The full-precision answer and formula are stored in `WORKED-CASES.json` for independent computation.

### Practice and knowledge check

1. Why does a technically precise instrument result not fix a biased sampling design?
2. Make a three-column table: directly observed evidence, what it supports, and a rival explanation. Identify an observation that could genuinely discriminate the rivals.
3. Recalculate the numerical example after modifying one input; include the original and new units and an appropriate uncertainty statement.
4. Propose a feasible and safe supplementary test and specify how the sample or instrument might introduce error.
5. In a short oral answer, name one conclusion that remains justified even if your preferred mineral identification is wrong.

## Lesson 32: X-ray diffraction and Bragg geometry

### Mechanism and scientific meaning

Constructive interference occurs when wave path differences satisfy integer multiples of wavelength. For first-order diffraction, Bragg law relates wavelength, lattice-plane spacing and scattering angle. Explain the mechanism at its appropriate scale: an atomic site, an ordered crystal, an individual grain, or a composite hand specimen. It matters whether the predicted feature belongs to a pure phase or reflects altered material surrounding it. A credible identification must distinguish the preferred phase from plausible alternatives, not merely find a familiar attribute.

### What can be observed?

Peak positions and relative intensities support phase identification when background, instrument geometry and preferred orientation are considered. Document instrument or test settings and the specimen identifier alongside the result; a number without measurement context can be misleading. If the phase is small, intergrown or altered, question whether the observation volume is appropriately matched to the mineral grain. Describe a feature first, then separately provide the inference that it implies.

### Case analysis with a rival explanation

**Fictional setting:** A powder pattern shows a strong peak near an expected quartz reflection but little else.

**Different causal accounts:** Quartz, an overlapping phase, texture effects or background treatment might produce an incomplete resemblance.

**A proposed discrimination:** Measure several independent peaks and compare a standard pattern with consistent wavelength metadata.

If an observation seems to favor one account, ask what independent result would actually contradict that favored account. State whether a negative result would be decisive or might reflect detection limits, orientation or sample heterogeneity. Where the tests cannot discriminate the candidates, mark the identity unresolved rather than claiming a mineral name with unsupported certainty.

### Limitation and consequence

Peak matching on a single reflection creates false positives; mixtures and amorphous fractions may be missed. Powder diffraction is central to phase identification and crystallinity characterization. Describe the exact claim that is supported and the more ambitious claim that must remain provisional. A result from a selected grain need not represent the host rock; a bulk assay need not identify crystal structure; and a crystallographic result need not determine geological history by itself.

### Worked quantitative example 32

**Fictional problem:** For first-order Bragg reflection with λ=.154 nm and θ=15°, compute interplanar spacing.

**Inputs:** lam = 0.154, theta = 15. Use `lam/(2*math.sin(math.radians(theta)))` to obtain **0.2975 nm**.

**Physical interpretation:** Instrument angle conventions use measured 2θ, not θ. A mathematical solution is useful only after its units, input precision and model domain are checked. Try changing one input by 10 percent and determine whether the answer varies linearly, inversely or nonlinearly; explain how the changed input would be measured in practice. The full-precision answer and formula are stored in `WORKED-CASES.json` for independent computation.

### Practice and knowledge check

1. What additional peak data would disprove a proposed phase identity?
2. Make a three-column table: directly observed evidence, what it supports, and a rival explanation. Identify an observation that could genuinely discriminate the rivals.
3. Recalculate the numerical example after modifying one input; include the original and new units and an appropriate uncertainty statement.
4. Propose a feasible and safe supplementary test and specify how the sample or instrument might introduce error.
5. In a short oral answer, name one conclusion that remains justified even if your preferred mineral identification is wrong.

## Lesson 33: Electron microscopy and EDS

### Mechanism and scientific meaning

A focused electron beam generates multiple interactions including backscattered electrons and characteristic X-rays. EDS estimates elemental composition over a finite interaction volume. Explain the mechanism at its appropriate scale: an atomic site, an ordered crystal, an individual grain, or a composite hand specimen. It matters whether the predicted feature belongs to a pure phase or reflects altered material surrounding it. A credible identification must distinguish the preferred phase from plausible alternatives, not merely find a familiar attribute.

### What can be observed?

Backscatter contrast, maps, spectral peaks and standards together aid phase characterization. Document instrument or test settings and the specimen identifier alongside the result; a number without measurement context can be misleading. If the phase is small, intergrown or altered, question whether the observation volume is appropriately matched to the mineral grain. Describe a feature first, then separately provide the inference that it implies.

### Case analysis with a rival explanation

**Fictional setting:** An EDS spectrum of a tiny bright inclusion shows Fe, S and unexpectedly high Si.

**Different causal accounts:** The spot may include the host silicate due to interaction volume, or there may be genuine mixed phases.

**A proposed discrimination:** Reduce beam interaction volume appropriately, map boundaries and use analytical standards.

If an observation seems to favor one account, ask what independent result would actually contradict that favored account. State whether a negative result would be decisive or might reflect detection limits, orientation or sample heterogeneity. Where the tests cannot discriminate the candidates, mark the identity unresolved rather than claiming a mineral name with unsupported certainty.

### Limitation and consequence

EDS does not identify oxidation state, crystal structure or every light element reliably. Microscopy reveals textures but cannot by itself prove full mineral species identity. Describe the exact claim that is supported and the more ambitious claim that must remain provisional. A result from a selected grain need not represent the host rock; a bulk assay need not identify crystal structure; and a crystallographic result need not determine geological history by itself.

### Worked quantitative example 33

**Fictional problem:** An electron-beam signal volume spans about 18 µm across a 5 µm inclusion. Calculate width ratio.

**Inputs:** interaction = 18, inclusion = 5. Use `interaction/inclusion` to obtain **3.6 ratio**.

**Physical interpretation:** Shape, depth and matrix effects make this only a screening metric. A mathematical solution is useful only after its units, input precision and model domain are checked. Try changing one input by 10 percent and determine whether the answer varies linearly, inversely or nonlinearly; explain how the changed input would be measured in practice. The full-precision answer and formula are stored in `WORKED-CASES.json` for independent computation.

### Practice and knowledge check

1. Why is a tiny inclusion particularly vulnerable to host-signal contamination?
2. Make a three-column table: directly observed evidence, what it supports, and a rival explanation. Identify an observation that could genuinely discriminate the rivals.
3. Recalculate the numerical example after modifying one input; include the original and new units and an appropriate uncertainty statement.
4. Propose a feasible and safe supplementary test and specify how the sample or instrument might introduce error.
5. In a short oral answer, name one conclusion that remains justified even if your preferred mineral identification is wrong.

## Lesson 34: Bulk chemistry, normalization and uncertainty

### Mechanism and scientific meaning

XRF or wet chemistry reports bulk elemental or oxide abundances; mineral formula calculations convert analyses into proportions on specified oxygen or cation bases and require oxidation assumptions. Explain the mechanism at its appropriate scale: an atomic site, an ordered crystal, an individual grain, or a composite hand specimen. It matters whether the predicted feature belongs to a pure phase or reflects altered material surrounding it. A credible identification must distinguish the preferred phase from plausible alternatives, not merely find a familiar attribute.

### What can be observed?

Replicate analyses, standards, closure checks and charge balance constrain formula quality. Document instrument or test settings and the specimen identifier alongside the result; a number without measurement context can be misleading. If the phase is small, intergrown or altered, question whether the observation volume is appropriately matched to the mineral grain. Describe a feature first, then separately provide the inference that it implies.

### Case analysis with a rival explanation

**Fictional setting:** A mineral report sums to 96.5 percent oxides and gives an implausible cation occupancy.

**Different causal accounts:** Water, unmeasured volatiles, altered surfaces, valence assumptions and preparation bias are candidates.

**A proposed discrimination:** Check analytical totals, sample basis, iron valence constraints and structural normalization rules.

If an observation seems to favor one account, ask what independent result would actually contradict that favored account. State whether a negative result would be decisive or might reflect detection limits, orientation or sample heterogeneity. Where the tests cannot discriminate the candidates, mark the identity unresolved rather than claiming a mineral name with unsupported certainty.

### Limitation and consequence

Renormalizing a poor oxide total to 100 percent can conceal analytical problems. A valid formula calculation states stoichiometric basis and its uncertainty. Describe the exact claim that is supported and the more ambitious claim that must remain provisional. A result from a selected grain need not represent the host rock; a bulk assay need not identify crystal structure; and a crystallographic result need not determine geological history by itself.

### Worked quantitative example 34

**Fictional problem:** Measured oxide total is 96.5 wt%. Compute shortfall from 100 wt%.

**Inputs:** total = 96.5. Use `100-total` to obtain **3.5 percentage points**.

**Physical interpretation:** Water and analytical bias may contribute; cannot infer cause uniquely. A mathematical solution is useful only after its units, input precision and model domain are checked. Try changing one input by 10 percent and determine whether the answer varies linearly, inversely or nonlinearly; explain how the changed input would be measured in practice. The full-precision answer and formula are stored in `WORKED-CASES.json` for independent computation.

### Practice and knowledge check

1. Under what conditions would reporting oxide percentages without mineral context mislead?
2. Make a three-column table: directly observed evidence, what it supports, and a rival explanation. Identify an observation that could genuinely discriminate the rivals.
3. Recalculate the numerical example after modifying one input; include the original and new units and an appropriate uncertainty statement.
4. Propose a feasible and safe supplementary test and specify how the sample or instrument might introduce error.
5. In a short oral answer, name one conclusion that remains justified even if your preferred mineral identification is wrong.

## Lesson 35: Spectroscopy and multimethod identification

### Mechanism and scientific meaning

Raman and infrared spectroscopy probe vibrational modes influenced by bonds and symmetry. Spectral positions and intensities require calibration and fluorescence/background treatment. Explain the mechanism at its appropriate scale: an atomic site, an ordered crystal, an individual grain, or a composite hand specimen. It matters whether the predicted feature belongs to a pure phase or reflects altered material surrounding it. A credible identification must distinguish the preferred phase from plausible alternatives, not merely find a familiar attribute.

### What can be observed?

Spatially resolved Raman maps can complement diffraction and elemental mapping, especially for polymorphs or micro-inclusions. Document instrument or test settings and the specimen identifier alongside the result; a number without measurement context can be misleading. If the phase is small, intergrown or altered, question whether the observation volume is appropriately matched to the mineral grain. Describe a feature first, then separately provide the inference that it implies.

### Case analysis with a rival explanation

**Fictional setting:** A fluorescence background obscures most of a candidate mineral Raman spectrum.

**Different causal accounts:** The problem may be contamination, organic coating, laser-induced fluorescence or inappropriate excitation wavelength.

**A proposed discrimination:** Change acquisition conditions within safe instrument protocols and cross-check with an independent method.

If an observation seems to favor one account, ask what independent result would actually contradict that favored account. State whether a negative result would be decisive or might reflect detection limits, orientation or sample heterogeneity. Where the tests cannot discriminate the candidates, mark the identity unresolved rather than claiming a mineral name with unsupported certainty.

### Limitation and consequence

Overpowering fluorescence or laser-induced alteration can create apparent features unrelated to the original phase. Multimethod workflows reduce false confidence from a single instrument. Describe the exact claim that is supported and the more ambitious claim that must remain provisional. A result from a selected grain need not represent the host rock; a bulk assay need not identify crystal structure; and a crystallographic result need not determine geological history by itself.

### Worked quantitative example 35

**Fictional problem:** A Raman feature shifts from 520 to 532 cm⁻¹. Compute relative shift percentage referenced to 520.

**Inputs:** new = 532, old = 520. Use `100*(new-old)/old` to obtain **2.3077 %**.

**Physical interpretation:** Instrument calibration, temperature, stress and phase differences may cause shifts. A mathematical solution is useful only after its units, input precision and model domain are checked. Try changing one input by 10 percent and determine whether the answer varies linearly, inversely or nonlinearly; explain how the changed input would be measured in practice. The full-precision answer and formula are stored in `WORKED-CASES.json` for independent computation.

### Practice and knowledge check

1. Why are chemical and structural measurements complementary rather than interchangeable?
2. Make a three-column table: directly observed evidence, what it supports, and a rival explanation. Identify an observation that could genuinely discriminate the rivals.
3. Recalculate the numerical example after modifying one input; include the original and new units and an appropriate uncertainty statement.
4. Propose a feasible and safe supplementary test and specify how the sample or instrument might introduce error.
5. In a short oral answer, name one conclusion that remains justified even if your preferred mineral identification is wrong.

## Integrative investigation 7: Which analysis should be ordered first?

### Research problem and scope

An imaginary conservation laboratory has a tiny mineral fragment from a protected archaeological collection; sampling permissions limit invasive preparation. It must answer whether the fragment contains a specific polymorph or simply has the same bulk elemental formula as the target. Rank non-destructive photography, micro-Raman, micro-XRF, powder XRD and electron microscopy for the exact question, acknowledging that some methods require a prepared surface or powder. A phase-identity claim needs crystallographic or vibrational evidence; an elemental signature alone generally cannot distinguish polymorphs. Document both the potential knowledge gain and the material alteration risk of each step.

### Synthetic analysis and interpretation

A second scenario features a heterogeneous mine-waste teaching composite with one sulfide inclusion smaller than the approximate electron interaction volume. Estimate the dimensionless ratio of interaction width to inclusion diameter before trusting the EDS result. Require instrument settings, spot location, standardization, raw spectra and a map of the region. If whole-rock oxides sum to 96.5 percent, resist the temptation to automatically normalize and move on: consider volatiles, analytical omissions, mineral heterogeneity and matrix corrections. Write a procedural audit with a blank, duplicate and reference material. A reliable interpretation records how the sample changed between collection, preparation and each subsequent test.

### Practical workflow, phase 1 — sampling and the question

Start with the decision that the study is supposed to support: Choose an analytical workflow that respects preservation, data quality, cost and reproducibility. Make a numbered sampling plan rather than collecting data opportunistically. For each proposed specimen list selection criteria, sampling location or teaching provenance, predicted heterogeneity, the expected spatial scale of the relevant mineral property, and how the sample will be preserved. Selection effects are part of the result. If the question concerns a trace phase, one homogenized bulk measurement can destroy the very spatial context needed to locate the phase; if the question concerns average composition, selecting only the most interesting-looking grain can severely bias the answer. Explain how the objective determines whether you prioritize hand specimen, polished section, thin section, powder, or in-situ analysis.

### Phase 2 — measurement, calibration and reproducibility

Prepare a record of instrument or classroom method, date, operator, settings, standards, detection limits and data-processing steps. Put raw observations in one table and proposed mineral names in another. Record replicates rather than silently combining them; when results disagree, ask whether the difference is repeatability, spatial heterogeneity, true chemical zoning or changing ambient conditions. The fictional dataset in `datasets/unit-07.csv` demonstrates the mechanics of a tidy table without pretending to represent a geological location. Choose one column as a measurement proxy, sketch it against sample index, and identify whether its pattern justifies a mechanistic inference. An upward trend in arbitrary proxy numbers is not evidence of a geological reaction unless calibration, spatial metadata, and a physically meaningful causal model exist.

### Phase 3 — competing explanatory models

Write a first hypothesis using the principal mechanism of this unit: Select measurement methods and evaluate the claims each instrument can support. Then write a genuinely different hypothesis consistent with the same initial observations, motivated by this difficulty: A technique has an observation scale, detection limit, interference structure, calibration demand and sample preparation cost. Two analyses may disagree because they observe different volumes or answer different questions. Predict three distinct outcomes under each model. A useful discriminating observation is not merely “more data”; it is a measurement whose possible results change the relative plausibility of the competing models. Look for possible confounding by sample alteration, orientation, unrecognized intergrowths, selection effects, data reduction, or unknown provenance. If the rival models yield identical predictions at the available scale, report non-identifiability rather than assigning a fabricated confidence percentage.

### Phase 4 — quantitative reasoning with the five lesson calculations

Use the worked problems from lessons 31–35 as transparent reference calculations. For each, reproduce the numeric answer and unit, then change one input and compute a sensitivity ratio. Record where a method assumes a pure single mineral, a cubic structure, a fixed section thickness, homogeneous mixing, or other simplifications. A reasonable mathematical curve is not a calibrated natural-system model. Review whether an expression is dimensionally consistent and whether it predicts nonsensical behavior near a boundary. If so, state the domain of validity and what physical effects the equation leaves out. Keep the numerical assumptions adjacent to the output chart to prevent reuse outside their teaching context.

### Phase 5 — reporting and oral defense

Create a short abstract that states the question and the bounded conclusion. Attach specimen metadata, a simple observation matrix, a calculation table, a list of candidate phases, the diagnostic evidence, two remaining uncertainties and a prioritized next measurement. Provide raw measurements or enough metadata for an independent reanalysis; use sample identifiers that link photographs to laboratory measurements. Ask a second group to read the data without seeing the original conclusion and record whether they reach the same phase family, a different species, or a justified unresolved answer. In oral defense, identify the strongest contradicting observation and explain what would make you revise your preferred explanation. If practical environmental, engineering or economic consequences arise, clearly refer those judgments to qualified professionals and independently validated measurements.

### Laboratory questions

1. Which of the proposed tests is both least destructive and most likely to exclude a strong competitor? Justify the tradeoff.
2. What is the main difference between analytical precision, phase identification accuracy and geological representativeness in this specific case?
3. How could a small inclusion, alteration rim or unfavorable crystallographic orientation change the apparent result without changing the core mineral identity?
4. Which inference is robust to losing one of the observations? Which collapses if a single measurement proves wrong?
5. State a conclusion under three scenarios: predicted data, unexpectedly contradictory data and measurements below detection. Do not force a species name when evidence is ambiguous.

## Unit 7 synthesis and transferable habits

A mineralogical investigation should end with a table of claims rather than an unqualified list of mineral names. Distinguish observations made directly by a person or instrument from derived values computed with a model. List each candidate identification together with supporting and contradicting properties. For every contested phase, write down the independent measurement that would change the answer and whether that test is feasible, safe and appropriately calibrated. Each step should preserve the ability to revisit the original evidence when instruments or classifications improve.

Compare the five lessons by placing their central quantities on a scale ladder: atomic or unit-cell dimensions, crystalline domains, grains, hand specimens and whole-rock assemblages. A model valid on one rung cannot automatically be applied to another. Where phases have the same elements but different structures, elemental assays must be complemented by phase-sensitive measurements. Where a crystal is chemically zoned, one bulk analysis may erase the growth sequence. Where an aggregate has pores or inclusions, mass-volume density reflects the composite rather than a pure end member.

For a short written exam, choose two of the unit's computations, recreate both results, and evaluate the meaning of a plausible measurement uncertainty. Report units and assumptions before providing a final rounded value. Then construct a fresh hypothetical sample that could fool a student who learned only the most visible property. Explain why your preferred test actually discriminates between the candidates. This synthesis is intended to improve scientific reasoning rather than encourage another memorized identification rule.
