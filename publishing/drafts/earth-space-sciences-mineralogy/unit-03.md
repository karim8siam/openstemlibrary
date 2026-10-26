# Unit 3 — Crystal chemistry and mineral stability

## Purpose and starting assumptions

Explain why substitution, charge balance, coordination, pressure, temperature, and reaction kinetics matter. The chemical formula of a mineral defines a constraint, not necessarily a perfectly fixed composition. Structural sites, disorder and vacancies make a simple ideal formula an incomplete description of many mineral grains. This unit connects five distinct questions rather than memorizing five disconnected lists of features. The repeated aim is to move from an observation, through a process explanation, to a testable mineralogical inference. Each topic includes at least one case in which several different explanations fit the initial evidence, so that the method teaches disciplined uncertainty rather than an automatic answer key.

## A minimum practical workflow

Before naming any mineral, record a specimen code, scale, provenance status, preservation state, and whether the observation came from a single grain or a mixed aggregate. State sample preparation and instrument configuration where relevant. Identify what data would falsify the leading interpretation and whether collecting those data is reasonable and safe. Place a label of synthetic instructional data on every constructed table or reading. Never present a model-generated number as a measurement of a real mine, outcrop or economic resource.

## Learning outcome

Use a hypothetical solid-solution and reaction sequence to distinguish stoichiometric accounting from geological equilibrium. Students should explain how the five lessons constrain one another, complete the worked calculations with units, and defend a conclusion that reflects—not exaggerates—the strength of the data. Include a clear distinction between observational precision, formula correctness and geological accuracy. The practical exercises are intended for supervised or non-destructive study; they are not permissions for hazardous laboratory work or environmental decisions.

## Lesson 11: Ionic bonding, Pauling ideas and structures

### Mechanism and scientific meaning

Electrostatic attractions favor charge balance and plausible polyhedra, while covalency and local distortion complicate purely ionic rules. Bond valence can help assess structural plausibility. Explain the mechanism at its appropriate scale: an atomic site, an ordered crystal, an individual grain, or a composite hand specimen. It matters whether the predicted feature belongs to a pure phase or reflects altered material surrounding it. A credible identification must distinguish the preferred phase from plausible alternatives, not merely find a familiar attribute.

### What can be observed?

Compare known nearest-neighbor distances and bond-valence sums with a proposed coordination environment. Document instrument or test settings and the specimen identifier alongside the result; a number without measurement context can be misleading. If the phase is small, intergrown or altered, question whether the observation volume is appropriately matched to the mineral grain. Describe a feature first, then separately provide the inference that it implies.

### Case analysis with a rival explanation

**Fictional setting:** A cation is placed in a tiny oxygen cavity in a stylized model despite a large tabulated ionic radius.

**Different causal accounts:** A wrong assumed oxidation state, coordination number or radius convention may explain the apparent mismatch.

**A proposed discrimination:** Check oxidation state evidence and occupancy against crystal-structure refinements.

If an observation seems to favor one account, ask what independent result would actually contradict that favored account. State whether a negative result would be decisive or might reflect detection limits, orientation or sample heterogeneity. Where the tests cannot discriminate the candidates, mark the identity unresolved rather than claiming a mineral name with unsupported certainty.

### Limitation and consequence

Ionic radii are context-dependent effective parameters, not hard-sphere atoms of invariant size. Crystal chemistry predicts substitutions and physical changes more reliably than appearance alone. Describe the exact claim that is supported and the more ambitious claim that must remain provisional. A result from a selected grain need not represent the host rock; a bulk assay need not identify crystal structure; and a crystallographic result need not determine geological history by itself.

### Worked quantitative example 11

**Fictional problem:** Compute the sum of formal ionic charges for ideal Al₂O₃ using +3 for Al and -2 for O.

**Inputs:** Al = 3, O = -2. Use `2*Al+3*O` to obtain **0 charge units**.

**Physical interpretation:** Formal valence describes electroneutrality, not exact electron localization. A mathematical solution is useful only after its units, input precision and model domain are checked. Try changing one input by 10 percent and determine whether the answer varies linearly, inversely or nonlinearly; explain how the changed input would be measured in practice. The full-precision answer and formula are stored in `WORKED-CASES.json` for independent computation.

### Practice and knowledge check

1. Where does a rigid ionic-radius rule break down in mixed ionic–covalent compounds?
2. Make a three-column table: directly observed evidence, what it supports, and a rival explanation. Identify an observation that could genuinely discriminate the rivals.
3. Recalculate the numerical example after modifying one input; include the original and new units and an appropriate uncertainty statement.
4. Propose a feasible and safe supplementary test and specify how the sample or instrument might introduce error.
5. In a short oral answer, name one conclusion that remains justified even if your preferred mineral identification is wrong.

## Lesson 12: Coordination polyhedra and site occupancy

### Mechanism and scientific meaning

Mineral structures arrange oxygen or other ligands around cations in coordination polyhedra; sites may be preferentially occupied by different elements according to size, charge and thermodynamic conditions. Explain the mechanism at its appropriate scale: an atomic site, an ordered crystal, an individual grain, or a composite hand specimen. It matters whether the predicted feature belongs to a pure phase or reflects altered material surrounding it. A credible identification must distinguish the preferred phase from plausible alternatives, not merely find a familiar attribute.

### What can be observed?

Site occupancies can be refined from diffraction and constrained by microprobe chemistry when elements scatter differently. Document instrument or test settings and the specimen identifier alongside the result; a number without measurement context can be misleading. If the phase is small, intergrown or altered, question whether the observation volume is appropriately matched to the mineral grain. Describe a feature first, then separately provide the inference that it implies.

### Case analysis with a rival explanation

**Fictional setting:** An amphibole analysis reports more sodium than expected from a simplified end-member formula.

**Different causal accounts:** Sodium may occupy more than one structural site, and analytical normalization may also be wrong.

**A proposed discrimination:** Normalize cation totals, check charge balance, and compare site models from crystallographic evidence.

If an observation seems to favor one account, ask what independent result would actually contradict that favored account. State whether a negative result would be decisive or might reflect detection limits, orientation or sample heterogeneity. Where the tests cannot discriminate the candidates, mark the identity unresolved rather than claiming a mineral name with unsupported certainty.

### Limitation and consequence

Treating bulk chemistry as a complete site assignment is an inverse-problem mistake. Site occupancy helps explain compositional trends across metamorphic and igneous assemblages. Describe the exact claim that is supported and the more ambitious claim that must remain provisional. A result from a selected grain need not represent the host rock; a bulk assay need not identify crystal structure; and a crystallographic result need not determine geological history by itself.

### Worked quantitative example 12

**Fictional problem:** A site has occupancy 0.65 Mg and 0.35 Fe. What fraction of the site is occupied?

**Inputs:** Mg = 0.65, Fe = 0.35. Use `Mg+Fe` to obtain **1 fraction**.

**Physical interpretation:** Vacancies or other ions must be included if occupancy is incomplete. A mathematical solution is useful only after its units, input precision and model domain are checked. Try changing one input by 10 percent and determine whether the answer varies linearly, inversely or nonlinearly; explain how the changed input would be measured in practice. The full-precision answer and formula are stored in `WORKED-CASES.json` for independent computation.

### Practice and knowledge check

1. How could occupancy change without producing a new named mineral species?
2. Make a three-column table: directly observed evidence, what it supports, and a rival explanation. Identify an observation that could genuinely discriminate the rivals.
3. Recalculate the numerical example after modifying one input; include the original and new units and an appropriate uncertainty statement.
4. Propose a feasible and safe supplementary test and specify how the sample or instrument might introduce error.
5. In a short oral answer, name one conclusion that remains justified even if your preferred mineral identification is wrong.

## Lesson 13: Solid solution, substitution and exsolution

### Mechanism and scientific meaning

Solid solution occurs when a structural framework tolerates compositional substitution; substitutions can be simple isovalent or coupled to maintain charge neutrality. Immiscibility at lower temperatures may produce exsolution. Explain the mechanism at its appropriate scale: an atomic site, an ordered crystal, an individual grain, or a composite hand specimen. It matters whether the predicted feature belongs to a pure phase or reflects altered material surrounding it. A credible identification must distinguish the preferred phase from plausible alternatives, not merely find a familiar attribute.

### What can be observed?

Composition profiles, lamellae, phase diagrams and bulk chemical balance constrain whether a grain once formed at a different condition. Document instrument or test settings and the specimen identifier alongside the result; a number without measurement context can be misleading. If the phase is small, intergrown or altered, question whether the observation volume is appropriately matched to the mineral grain. Describe a feature first, then separately provide the inference that it implies.

### Case analysis with a rival explanation

**Fictional setting:** A feldspar contains two optically distinct intergrowths with coherent orientation.

**Different causal accounts:** Exsolution during cooling, replacement, or later deformation-related recrystallization could account for the pattern.

**A proposed discrimination:** Map elements across lamellae and examine crystallographic continuity before inferring the origin.

If an observation seems to favor one account, ask what independent result would actually contradict that favored account. State whether a negative result would be decisive or might reflect detection limits, orientation or sample heterogeneity. Where the tests cannot discriminate the candidates, mark the identity unresolved rather than claiming a mineral name with unsupported certainty.

### Limitation and consequence

A straight compositional mixing line is not proof of equilibrium at every temperature. Solid solutions can store a record of temperature history, but kinetics and subsequent alteration matter. Describe the exact claim that is supported and the more ambitious claim that must remain provisional. A result from a selected grain need not represent the host rock; a bulk assay need not identify crystal structure; and a crystallographic result need not determine geological history by itself.

### Worked quantitative example 13

**Fictional problem:** An olivine composition has 0.72 mol Mg and 0.28 mol Fe on the relevant divalent site. Compute Mg fraction.

**Inputs:** Mg = 0.72, Fe = 0.28. Use `Mg/(Mg+Fe)` to obtain **0.72 fraction**.

**Physical interpretation:** Assumes simple Fe-Mg binary treatment and Fe²⁺. A mathematical solution is useful only after its units, input precision and model domain are checked. Try changing one input by 10 percent and determine whether the answer varies linearly, inversely or nonlinearly; explain how the changed input would be measured in practice. The full-precision answer and formula are stored in `WORKED-CASES.json` for independent computation.

### Practice and knowledge check

1. What might preserve a metastable homogeneous mineral below its equilibrium solvus?
2. Make a three-column table: directly observed evidence, what it supports, and a rival explanation. Identify an observation that could genuinely discriminate the rivals.
3. Recalculate the numerical example after modifying one input; include the original and new units and an appropriate uncertainty statement.
4. Propose a feasible and safe supplementary test and specify how the sample or instrument might introduce error.
5. In a short oral answer, name one conclusion that remains justified even if your preferred mineral identification is wrong.

## Lesson 14: Polymorphism and phase transformations

### Mechanism and scientific meaning

Polymorphs have the same overall chemical composition but different atomic arrangements. Relative stability depends on free energy, pressure and temperature; kinetic barriers may preserve metastable phases. Explain the mechanism at its appropriate scale: an atomic site, an ordered crystal, an individual grain, or a composite hand specimen. It matters whether the predicted feature belongs to a pure phase or reflects altered material surrounding it. A credible identification must distinguish the preferred phase from plausible alternatives, not merely find a familiar attribute.

### What can be observed?

The combination of diffraction and well-contextualized host rock can constrain a polymorph more effectively than chemical analysis alone. Document instrument or test settings and the specimen identifier alongside the result; a number without measurement context can be misleading. If the phase is small, intergrown or altered, question whether the observation volume is appropriately matched to the mineral grain. Describe a feature first, then separately provide the inference that it implies.

### Case analysis with a rival explanation

**Fictional setting:** A silica-bearing sample gives an unfamiliar diffraction pattern but routine chemistry shows approximately SiO2.

**Different causal accounts:** Quartz, cristobalite, tridymite, coesite or an unrelated multi-phase mixture require different structural tests.

**A proposed discrimination:** Collect a quality-controlled diffraction dataset and use textures to assess whether any phase is inherited or transformed.

If an observation seems to favor one account, ask what independent result would actually contradict that favored account. State whether a negative result would be decisive or might reflect detection limits, orientation or sample heterogeneity. Where the tests cannot discriminate the candidates, mark the identity unresolved rather than claiming a mineral name with unsupported certainty.

### Limitation and consequence

An identified high-pressure polymorph cannot be converted directly into a precise single pressure without a full phase assemblage. Polymorphs inform burial and impact histories when accompanied by contextual evidence. Describe the exact claim that is supported and the more ambitious claim that must remain provisional. A result from a selected grain need not represent the host rock; a bulk assay need not identify crystal structure; and a crystallographic result need not determine geological history by itself.

### Worked quantitative example 14

**Fictional problem:** A toy phase transition has ΔS=30 J/(mol K), ΔV=1×10⁻⁶ m³/mol. Compute dP/dT in MPa/K.

**Inputs:** dS = 30, dV = 1e-06. Use `dS/dV/1e6` to obtain **30 MPa/K**.

**Physical interpretation:** Constant slope assumes values do not vary with conditions. A mathematical solution is useful only after its units, input precision and model domain are checked. Try changing one input by 10 percent and determine whether the answer varies linearly, inversely or nonlinearly; explain how the changed input would be measured in practice. The full-precision answer and formula are stored in `WORKED-CASES.json` for independent computation.

### Practice and knowledge check

1. Why is a composition-only laboratory report insufficient to distinguish quartz from coesite?
2. Make a three-column table: directly observed evidence, what it supports, and a rival explanation. Identify an observation that could genuinely discriminate the rivals.
3. Recalculate the numerical example after modifying one input; include the original and new units and an appropriate uncertainty statement.
4. Propose a feasible and safe supplementary test and specify how the sample or instrument might introduce error.
5. In a short oral answer, name one conclusion that remains justified even if your preferred mineral identification is wrong.

## Lesson 15: Reaction textures and thermodynamic constraints

### Mechanism and scientific meaning

Minerals can react when changes in temperature, pressure or fluid chemistry change the stable assemblage. Reaction progress may be limited by diffusion, fluid supply or nucleation. Explain the mechanism at its appropriate scale: an atomic site, an ordered crystal, an individual grain, or a composite hand specimen. It matters whether the predicted feature belongs to a pure phase or reflects altered material surrounding it. A credible identification must distinguish the preferred phase from plausible alternatives, not merely find a familiar attribute.

### What can be observed?

Reaction rims, inclusion patterns and zoning constrain sequence, but equilibrium is an interpretive assumption that must be examined. Document instrument or test settings and the specimen identifier alongside the result; a number without measurement context can be misleading. If the phase is small, intergrown or altered, question whether the observation volume is appropriately matched to the mineral grain. Describe a feature first, then separately provide the inference that it implies.

### Case analysis with a rival explanation

**Fictional setting:** A garnet core is surrounded by a green reaction corona at a grain boundary.

**Different causal accounts:** Decompression, hydration, localized fluid access or incomplete equilibration are plausible.

**A proposed discrimination:** Compare rim chemistry, inclusion trails, reaction stoichiometry and whole-rock composition.

If an observation seems to favor one account, ask what independent result would actually contradict that favored account. State whether a negative result would be decisive or might reflect detection limits, orientation or sample heterogeneity. Where the tests cannot discriminate the candidates, mark the identity unresolved rather than claiming a mineral name with unsupported certainty.

### Limitation and consequence

One texture does not uniquely determine whether a reaction happened during heating or cooling. Reaction analysis informs metamorphic paths, alteration studies and materials durability. Describe the exact claim that is supported and the more ambitious claim that must remain provisional. A result from a selected grain need not represent the host rock; a bulk assay need not identify crystal structure; and a crystallographic result need not determine geological history by itself.

### Worked quantitative example 15

**Fictional problem:** A mineral reaction consumed 24 g of 80 g of limiting component. Calculate reacted fraction.

**Inputs:** consumed = 24, initial = 80. Use `100*consumed/initial` to obtain **30 %**.

**Physical interpretation:** Mass loss is not by itself proof of chemical equilibrium. A mathematical solution is useful only after its units, input precision and model domain are checked. Try changing one input by 10 percent and determine whether the answer varies linearly, inversely or nonlinearly; explain how the changed input would be measured in practice. The full-precision answer and formula are stored in `WORKED-CASES.json` for independent computation.

### Practice and knowledge check

1. How does a kinetic barrier permit a phase to persist outside its equilibrium field?
2. Make a three-column table: directly observed evidence, what it supports, and a rival explanation. Identify an observation that could genuinely discriminate the rivals.
3. Recalculate the numerical example after modifying one input; include the original and new units and an appropriate uncertainty statement.
4. Propose a feasible and safe supplementary test and specify how the sample or instrument might introduce error.
5. In a short oral answer, name one conclusion that remains justified even if your preferred mineral identification is wrong.

## Integrative investigation 3: A hypothetical Fe–Mg mineral series

### Research problem and scope

A set of five fictional olivine-like analyses varies smoothly from an Mg-rich end member to a Fe-richer member. Express each end-member fraction as Mg/(Mg+Fe) on a molar cation basis, not by directly dividing elemental mass percentages. Show why atomic-mass conversion matters if data were originally reported in weight units. Then select two hypothetical grain profiles: one nearly uniform and another with a systematic core-rim shift. The variation can indicate growth or exchange, but neither a straight line nor a steep gradient automatically proves equilibration. A kinetic model would need diffusivities, temperatures, time, crystallographic orientation, grain geometry and appropriate boundaries.

### Synthetic analysis and interpretation

Prepare a charge-balance sheet for an idealized simple oxide and then explore an Al-bearing substitution that would require coupled charge compensation. Separate a chemical possibility from crystallographic evidence that the sites are actually occupied as proposed. Ask whether the same reported analysis could contain two unresolved intergrowths whose bulk average mimics a homogeneous solid solution. A second investigation compares a hypothetical phase transformation slope dP/dT=ΔS/ΔV. Track units carefully: J/m³ equals Pa, and 10^6 Pa equals 1 MPa. The model slope demonstrates thermodynamic logic but not a validated pressure-temperature calibration for an actual mantle reaction.

### Practical workflow, phase 1 — sampling and the question

Start with the decision that the study is supposed to support: Use a hypothetical solid-solution and reaction sequence to distinguish stoichiometric accounting from geological equilibrium. Make a numbered sampling plan rather than collecting data opportunistically. For each proposed specimen list selection criteria, sampling location or teaching provenance, predicted heterogeneity, the expected spatial scale of the relevant mineral property, and how the sample will be preserved. Selection effects are part of the result. If the question concerns a trace phase, one homogenized bulk measurement can destroy the very spatial context needed to locate the phase; if the question concerns average composition, selecting only the most interesting-looking grain can severely bias the answer. Explain how the objective determines whether you prioritize hand specimen, polished section, thin section, powder, or in-situ analysis.

### Phase 2 — measurement, calibration and reproducibility

Prepare a record of instrument or classroom method, date, operator, settings, standards, detection limits and data-processing steps. Put raw observations in one table and proposed mineral names in another. Record replicates rather than silently combining them; when results disagree, ask whether the difference is repeatability, spatial heterogeneity, true chemical zoning or changing ambient conditions. The fictional dataset in `datasets/unit-03.csv` demonstrates the mechanics of a tidy table without pretending to represent a geological location. Choose one column as a measurement proxy, sketch it against sample index, and identify whether its pattern justifies a mechanistic inference. An upward trend in arbitrary proxy numbers is not evidence of a geological reaction unless calibration, spatial metadata, and a physically meaningful causal model exist.

### Phase 3 — competing explanatory models

Write a first hypothesis using the principal mechanism of this unit: Explain why substitution, charge balance, coordination, pressure, temperature, and reaction kinetics matter. Then write a genuinely different hypothesis consistent with the same initial observations, motivated by this difficulty: The chemical formula of a mineral defines a constraint, not necessarily a perfectly fixed composition. Structural sites, disorder and vacancies make a simple ideal formula an incomplete description of many mineral grains. Predict three distinct outcomes under each model. A useful discriminating observation is not merely “more data”; it is a measurement whose possible results change the relative plausibility of the competing models. Look for possible confounding by sample alteration, orientation, unrecognized intergrowths, selection effects, data reduction, or unknown provenance. If the rival models yield identical predictions at the available scale, report non-identifiability rather than assigning a fabricated confidence percentage.

### Phase 4 — quantitative reasoning with the five lesson calculations

Use the worked problems from lessons 11–15 as transparent reference calculations. For each, reproduce the numeric answer and unit, then change one input and compute a sensitivity ratio. Record where a method assumes a pure single mineral, a cubic structure, a fixed section thickness, homogeneous mixing, or other simplifications. A reasonable mathematical curve is not a calibrated natural-system model. Review whether an expression is dimensionally consistent and whether it predicts nonsensical behavior near a boundary. If so, state the domain of validity and what physical effects the equation leaves out. Keep the numerical assumptions adjacent to the output chart to prevent reuse outside their teaching context.

### Phase 5 — reporting and oral defense

Create a short abstract that states the question and the bounded conclusion. Attach specimen metadata, a simple observation matrix, a calculation table, a list of candidate phases, the diagnostic evidence, two remaining uncertainties and a prioritized next measurement. Provide raw measurements or enough metadata for an independent reanalysis; use sample identifiers that link photographs to laboratory measurements. Ask a second group to read the data without seeing the original conclusion and record whether they reach the same phase family, a different species, or a justified unresolved answer. In oral defense, identify the strongest contradicting observation and explain what would make you revise your preferred explanation. If practical environmental, engineering or economic consequences arise, clearly refer those judgments to qualified professionals and independently validated measurements.

### Laboratory questions

1. Which of the proposed tests is both least destructive and most likely to exclude a strong competitor? Justify the tradeoff.
2. What is the main difference between analytical precision, phase identification accuracy and geological representativeness in this specific case?
3. How could a small inclusion, alteration rim or unfavorable crystallographic orientation change the apparent result without changing the core mineral identity?
4. Which inference is robust to losing one of the observations? Which collapses if a single measurement proves wrong?
5. State a conclusion under three scenarios: predicted data, unexpectedly contradictory data and measurements below detection. Do not force a species name when evidence is ambiguous.

## Unit 3 synthesis and transferable habits

A mineralogical investigation should end with a table of claims rather than an unqualified list of mineral names. Distinguish observations made directly by a person or instrument from derived values computed with a model. List each candidate identification together with supporting and contradicting properties. For every contested phase, write down the independent measurement that would change the answer and whether that test is feasible, safe and appropriately calibrated. Each step should preserve the ability to revisit the original evidence when instruments or classifications improve.

Compare the five lessons by placing their central quantities on a scale ladder: atomic or unit-cell dimensions, crystalline domains, grains, hand specimens and whole-rock assemblages. A model valid on one rung cannot automatically be applied to another. Where phases have the same elements but different structures, elemental assays must be complemented by phase-sensitive measurements. Where a crystal is chemically zoned, one bulk analysis may erase the growth sequence. Where an aggregate has pores or inclusions, mass-volume density reflects the composite rather than a pure end member.

For a short written exam, choose two of the unit's computations, recreate both results, and evaluate the meaning of a plausible measurement uncertainty. Report units and assumptions before providing a final rounded value. Then construct a fresh hypothetical sample that could fool a student who learned only the most visible property. Explain why your preferred test actually discriminates between the candidates. This synthesis is intended to improve scientific reasoning rather than encourage another memorized identification rule.
