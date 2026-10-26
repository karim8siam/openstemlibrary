# Unit 8: Quantitative Paleontology, Ethics, and Reproducibility

## Central research question

**How should paleontologists turn fossil observations into transparent and reusable scientific claims?**

**Synthetic field investigation.** A fictional regional fossil survey produces incomplete specimen data, three contradictory identifications and uncertain stratigraphic locations; teams design an open and ethical audit. These observations are invented for teaching, not reports from a real locality.

## Interpreting paleontological evidence

The unit builds a connected argument rather than a specimen catalogue. Its key themes are **collection metadata, uncertainty modeling, digital morphology, data standards, ethical and reproducible workflows**. Every conclusion begins with a documented fossil, trace or associated rock unit and proceeds through a set of explicit assumptions. A fossil is not a direct recording of a living ecosystem: death, transport, burial, chemistry, uplift, erosion, collecting and taxonomic recognition all filter the evidence before it reaches a classroom. The scientific challenge is to separate the signal of past life from the processes that determined which signals survived. When several explanations fit the observations, the appropriate result is a constrained set of hypotheses rather than unwarranted certainty.

Imagine investigating the following setting: A fictional regional fossil survey produces incomplete specimen data, three contradictory identifications and uncertain stratigraphic locations; teams design an open and ethical audit. The first responsibility is to document material provenance, field associations and the sedimentary architecture. Then define what constitutes an independent measurement: a specimen, a shell valve, a fossil bed, a cataloged collection or a stratigraphic sample. An apparent increase in individuals can be created by longer time averaging or preservation of more skeletal fragments, and an apparent loss can arise when the rock containing a former habitat is absent. A robust field notebook therefore records negative searches, changed collecting effort, restricted access and preparation decisions alongside spectacular observations.

The chronology of a fossil occurrence is tied to the geological unit, and may depend on radiometric constraints, magnetostratigraphic information or biostratigraphic comparisons; no one method should be assumed to work in every sedimentary setting. The 2026/06 International Chronostratigraphic Chart is a dated reference, not a promise that numerical boundary ages will never change. Treat the classification of a species, the assignment of an age and the identification of a depositional setting as separately revisable judgments. An assessment that clearly states what is known, what is uncertain and what would decide among alternatives is more scientifically useful than a seemingly exhaustive list of names.

### Lesson 8.1: Specimen metadata and provenance

#### Core idea and biological mechanism

A useful fossil record links an object to locality, unit, horizon, collector, identifier, preservation state, catalog number and collection permissions. This topic belongs to the broader problem of **collection metadata**: an observed fossil pattern is a product of former biology and later geological filtering. Identical apparent shapes or abundance patterns can arise from more than one cause. Rather than treating the textbook category as proof, identify the observations that must be true if the working mechanism is relevant at this particular site.

#### Mechanism lens

A working explanation has to link the material cause, the trace that survived, and the inference drawn from it. The physical evidence comes first; a familiar evolutionary narrative should not be used as an unstated premise. In this lesson, **specimen metadata and provenance** is not an isolated vocabulary item. Implement controlled locality precision, coordinate reference systems, persistent specimen IDs and documented taxonomic revisions. Place that procedure beside the principle: A useful fossil record links an object to locality, unit, horizon, collector, identifier, preservation state, catalog number and collection permissions. A defensible explanation names the preserved feature, what is missing, the transformation linking original organism to specimen, and the circumstances under which that interpretation would cease to be plausible. This chain of reasoning is particularly important whenever the focal specimen is rare or visibly altered.

#### Counterfactual lens

Good explanations predict cases in which the preferred interpretation should fail. Researchers can look for those cases in an independently collected outcrop, a different depositional environment or a carefully chosen replicate. One potential failure mode is specific: Publishing sensitive locality coordinates may accelerate looting; privacy may be required even for scientifically reproducible records. An alternative model could therefore preserve the measured numbers while changing the biological explanation. Make a prediction that differs between the two explanations, specify the material that would distinguish them, and record in advance what observation would count against your favored inference. This prevents a positive identification or an apparent temporal pattern from becoming unfalsifiable.

#### Uncertainty lens

Distinguish measurement precision, model choice, taxonomic uncertainty, age control and sampling incompleteness. These sources can affect a conclusion differently and should not be hidden in a single unexplained error bar. Publishing sensitive locality coordinates may accelerate looting; privacy may be required even for scientifically reproducible records. Where dates or boundaries enter the argument, give the chronostratigraphic source and its version. Where taxonomy enters, identify the revision followed. Where anatomical measurements enter, describe landmarks and observer repeatability. Always distinguish an interval bounded by first and last *observed* occurrences from the unobservable true lifespan of the taxon; this distinction protects conclusions against an overly complete picture of deep time.

#### Field notebook and worked problem

**Worked quantitative case 8.1: Metadata completeness.** 180 required metadata fields across specimen rows, 22 missing.

**Calculation.** Use the explicit arithmetic expression `(180-22)/180*100`. With the given hypothetical measurements the result is **87.78 %**. The calculation is reproducible from the stated values; precision of the displayed result is not a measurement uncertainty. **Interpretation boundary:** Some metadata fields are more critical than others.

**Independent task.** Quantify missing-value rates for required specimen fields. Produce a figure with named axes or a specimen-character table, a statement of the sampling unit, and a two-sentence comparison between your preferred interpretation and a defensible alternative. Include the observation most likely to revise your conclusion.

**Check for understanding.** What would change if a portion of the fossil record were never preserved? How might an independent collector find a different result? What information is required before the number calculated above can become a biological claim? How will the specimen and locality be recoverable for a later researcher?

### Lesson 8.2: Measurement, morphometrics, and error

#### Core idea and biological mechanism

Digital imaging and landmarks can improve repeatability but depend on scale, orientation, scanner resolution and homologous point definitions. This topic belongs to the broader problem of **uncertainty modeling**: an observed fossil pattern is a product of former biology and later geological filtering. Identical apparent shapes or abundance patterns can arise from more than one cause. Rather than treating the textbook category as proof, identify the observations that must be true if the working mechanism is relevant at this particular site.

#### Mechanism lens

A working explanation has to link the material cause, the trace that survived, and the inference drawn from it. The physical evidence comes first; a familiar evolutionary narrative should not be used as an unstated premise. In this lesson, **measurement, morphometrics, and error** is not an isolated vocabulary item. Use replicate photographs with measurement standards and evaluate observer effects using blinded remeasurement. Place that procedure beside the principle: Digital imaging and landmarks can improve repeatability but depend on scale, orientation, scanner resolution and homologous point definitions. A defensible explanation names the preserved feature, what is missing, the transformation linking original organism to specimen, and the circumstances under which that interpretation would cease to be plausible. This chain of reasoning is particularly important whenever the focal specimen is rare or visibly altered.

#### Counterfactual lens

Good explanations predict cases in which the preferred interpretation should fail. Researchers can look for those cases in an independently collected outcrop, a different depositional environment or a carefully chosen replicate. One potential failure mode is specific: More decimal places do not represent more biological precision when deformation and landmark ambiguity dominate. An alternative model could therefore preserve the measured numbers while changing the biological explanation. Make a prediction that differs between the two explanations, specify the material that would distinguish them, and record in advance what observation would count against your favored inference. This prevents a positive identification or an apparent temporal pattern from becoming unfalsifiable.

#### Uncertainty lens

Distinguish measurement precision, model choice, taxonomic uncertainty, age control and sampling incompleteness. These sources can affect a conclusion differently and should not be hidden in a single unexplained error bar. More decimal places do not represent more biological precision when deformation and landmark ambiguity dominate. Where dates or boundaries enter the argument, give the chronostratigraphic source and its version. Where taxonomy enters, identify the revision followed. Where anatomical measurements enter, describe landmarks and observer repeatability. Always distinguish an interval bounded by first and last *observed* occurrences from the unobservable true lifespan of the taxon; this distinction protects conclusions against an overly complete picture of deep time.

#### Field notebook and worked problem

**Worked quantitative case 8.2: Observer coefficient of variation.** Repeated linear measure mean 18.6 mm, SD 1.3 mm.

**Calculation.** Use the explicit arithmetic expression `1.3/18.6*100`. With the given hypothetical measurements the result is **6.989 %**. The calculation is reproducible from the stated values; precision of the displayed result is not a measurement uncertainty. **Interpretation boundary:** Deformation can dominate repeatability estimates.

**Independent task.** Compute the coefficient of variation of repeated measurements. Produce a figure with named axes or a specimen-character table, a statement of the sampling unit, and a two-sentence comparison between your preferred interpretation and a defensible alternative. Include the observation most likely to revise your conclusion.

**Check for understanding.** What would change if a portion of the fossil record were never preserved? How might an independent collector find a different result? What information is required before the number calculated above can become a biological claim? How will the specimen and locality be recoverable for a later researcher?

### Lesson 8.3: Statistical inference and publication bias

#### Core idea and biological mechanism

Small and selectively collected datasets can distort effect size estimates; uncertainty intervals and sensitivity analyses are essential for honest claims. This topic belongs to the broader problem of **digital morphology**: an observed fossil pattern is a product of former biology and later geological filtering. Identical apparent shapes or abundance patterns can arise from more than one cause. Rather than treating the textbook category as proof, identify the observations that must be true if the working mechanism is relevant at this particular site.

#### Mechanism lens

A working explanation has to link the material cause, the trace that survived, and the inference drawn from it. The physical evidence comes first; a familiar evolutionary narrative should not be used as an unstated premise. In this lesson, **statistical inference and publication bias** is not an isolated vocabulary item. State a causal question, define units of analysis and distinguish specimens, localities and collections before statistical testing. Place that procedure beside the principle: Small and selectively collected datasets can distort effect size estimates; uncertainty intervals and sensitivity analyses are essential for honest claims. A defensible explanation names the preserved feature, what is missing, the transformation linking original organism to specimen, and the circumstances under which that interpretation would cease to be plausible. This chain of reasoning is particularly important whenever the focal specimen is rare or visibly altered.

#### Counterfactual lens

Good explanations predict cases in which the preferred interpretation should fail. Researchers can look for those cases in an independently collected outcrop, a different depositional environment or a carefully chosen replicate. One potential failure mode is specific: Treating dozens of fossils from one concentrated bed as independent environmental replicates is pseudoreplication. An alternative model could therefore preserve the measured numbers while changing the biological explanation. Make a prediction that differs between the two explanations, specify the material that would distinguish them, and record in advance what observation would count against your favored inference. This prevents a positive identification or an apparent temporal pattern from becoming unfalsifiable.

#### Uncertainty lens

Distinguish measurement precision, model choice, taxonomic uncertainty, age control and sampling incompleteness. These sources can affect a conclusion differently and should not be hidden in a single unexplained error bar. Treating dozens of fossils from one concentrated bed as independent environmental replicates is pseudoreplication. Where dates or boundaries enter the argument, give the chronostratigraphic source and its version. Where taxonomy enters, identify the revision followed. Where anatomical measurements enter, describe landmarks and observer repeatability. Always distinguish an interval bounded by first and last *observed* occurrences from the unobservable true lifespan of the taxon; this distinction protects conclusions against an overly complete picture of deep time.

#### Field notebook and worked problem

**Worked quantitative case 8.3: Binomial standard error.** One independent sample of n=150 has focal identification fraction 0.4.

**Calculation.** Use the explicit arithmetic expression `math.sqrt(0.4*(1-0.4)/150)`. With the given hypothetical measurements the result is **0.04 proportion**. The calculation is reproducible from the stated values; precision of the displayed result is not a measurement uncertainty. **Interpretation boundary:** Clustered specimens violate an independent Bernoulli approximation.

**Independent task.** Calculate a proportion and approximate standard error under an explicit independence assumption. Produce a figure with named axes or a specimen-character table, a statement of the sampling unit, and a two-sentence comparison between your preferred interpretation and a defensible alternative. Include the observation most likely to revise your conclusion.

**Check for understanding.** What would change if a portion of the fossil record were never preserved? How might an independent collector find a different result? What information is required before the number calculated above can become a biological claim? How will the specimen and locality be recoverable for a later researcher?

### Lesson 8.4: Open databases and interoperable workflows

#### Core idea and biological mechanism

Large occurrence datasets need stable taxonomy, documented licensing, reproducible filters and versioned downloads before species-range analyses can be trusted. This topic belongs to the broader problem of **data standards**: an observed fossil pattern is a product of former biology and later geological filtering. Identical apparent shapes or abundance patterns can arise from more than one cause. Rather than treating the textbook category as proof, identify the observations that must be true if the working mechanism is relevant at this particular site.

#### Mechanism lens

A working explanation has to link the material cause, the trace that survived, and the inference drawn from it. The physical evidence comes first; a familiar evolutionary narrative should not be used as an unstated premise. In this lesson, **open databases and interoperable workflows** is not an isolated vocabulary item. Write a workflow with source snapshot, extraction date, field descriptions, curation choices, code and checkable sample outputs. Place that procedure beside the principle: Large occurrence datasets need stable taxonomy, documented licensing, reproducible filters and versioned downloads before species-range analyses can be trusted. A defensible explanation names the preserved feature, what is missing, the transformation linking original organism to specimen, and the circumstances under which that interpretation would cease to be plausible. This chain of reasoning is particularly important whenever the focal specimen is rare or visibly altered.

#### Counterfactual lens

Good explanations predict cases in which the preferred interpretation should fail. Researchers can look for those cases in an independently collected outcrop, a different depositional environment or a carefully chosen replicate. One potential failure mode is specific: Crowdsourced or literature-derived occurrence counts do not replace checking disputed specimen identifications or original publications. An alternative model could therefore preserve the measured numbers while changing the biological explanation. Make a prediction that differs between the two explanations, specify the material that would distinguish them, and record in advance what observation would count against your favored inference. This prevents a positive identification or an apparent temporal pattern from becoming unfalsifiable.

#### Uncertainty lens

Distinguish measurement precision, model choice, taxonomic uncertainty, age control and sampling incompleteness. These sources can affect a conclusion differently and should not be hidden in a single unexplained error bar. Crowdsourced or literature-derived occurrence counts do not replace checking disputed specimen identifications or original publications. Where dates or boundaries enter the argument, give the chronostratigraphic source and its version. Where taxonomy enters, identify the revision followed. Where anatomical measurements enter, describe landmarks and observer repeatability. Always distinguish an interval bounded by first and last *observed* occurrences from the unobservable true lifespan of the taxon; this distinction protects conclusions against an overly complete picture of deep time.

#### Field notebook and worked problem

**Worked quantitative case 8.4: Taxonomic synonym impact.** A catalog has 130 species labels, with 18 resolved as duplicate synonyms; what fraction remains?

**Calculation.** Use the explicit arithmetic expression `(130-18)/130*100`. With the given hypothetical measurements the result is **86.15 %**. The calculation is reproducible from the stated values; precision of the displayed result is not a measurement uncertainty. **Interpretation boundary:** Synonym reconciliation must be defensible and documented.

**Independent task.** Compare apparent richness before and after synonym reconciliation. Produce a figure with named axes or a specimen-character table, a statement of the sampling unit, and a two-sentence comparison between your preferred interpretation and a defensible alternative. Include the observation most likely to revise your conclusion.

**Check for understanding.** What would change if a portion of the fossil record were never preserved? How might an independent collector find a different result? What information is required before the number calculated above can become a biological claim? How will the specimen and locality be recoverable for a later researcher?

### Lesson 8.5: Collection law, Indigenous interests, and research ethics

#### Core idea and biological mechanism

Fossil collecting is governed by local laws, land ownership, permits and community relationships; ownership assumptions and destructive sampling require prior checks. This topic belongs to the broader problem of **ethical and reproducible workflows**: an observed fossil pattern is a product of former biology and later geological filtering. Identical apparent shapes or abundance patterns can arise from more than one cause. Rather than treating the textbook category as proof, identify the observations that must be true if the working mechanism is relevant at this particular site.

#### Mechanism lens

A working explanation has to link the material cause, the trace that survived, and the inference drawn from it. The physical evidence comes first; a familiar evolutionary narrative should not be used as an unstated premise. In this lesson, **collection law, indigenous interests, and research ethics** is not an isolated vocabulary item. Record legal authority and specimen stewardship, consult relevant communities, and document consent and proposed destructive techniques. Place that procedure beside the principle: Fossil collecting is governed by local laws, land ownership, permits and community relationships; ownership assumptions and destructive sampling require prior checks. A defensible explanation names the preserved feature, what is missing, the transformation linking original organism to specimen, and the circumstances under which that interpretation would cease to be plausible. This chain of reasoning is particularly important whenever the focal specimen is rare or visibly altered.

#### Counterfactual lens

Good explanations predict cases in which the preferred interpretation should fail. Researchers can look for those cases in an independently collected outcrop, a different depositional environment or a carefully chosen replicate. One potential failure mode is specific: Commercial purchase without clear legal provenance can destroy contextual information and damage trust with custodians and researchers. An alternative model could therefore preserve the measured numbers while changing the biological explanation. Make a prediction that differs between the two explanations, specify the material that would distinguish them, and record in advance what observation would count against your favored inference. This prevents a positive identification or an apparent temporal pattern from becoming unfalsifiable.

#### Uncertainty lens

Distinguish measurement precision, model choice, taxonomic uncertainty, age control and sampling incompleteness. These sources can affect a conclusion differently and should not be hidden in a single unexplained error bar. Commercial purchase without clear legal provenance can destroy contextual information and damage trust with custodians and researchers. Where dates or boundaries enter the argument, give the chronostratigraphic source and its version. Where taxonomy enters, identify the revision followed. Where anatomical measurements enter, describe landmarks and observer repeatability. Always distinguish an interval bounded by first and last *observed* occurrences from the unobservable true lifespan of the taxon; this distinction protects conclusions against an overly complete picture of deep time.

#### Field notebook and worked problem

**Worked quantitative case 8.5: Audit discrepancy rate.** Seven of 84 records in a teaching archive have unresolved locality or horizon discrepancies.

**Calculation.** Use the explicit arithmetic expression `7/84*100`. With the given hypothetical measurements the result is **8.333 %**. The calculation is reproducible from the stated values; precision of the displayed result is not a measurement uncertainty. **Interpretation boundary:** A low average error rate does not justify publishing sensitive localities.

**Independent task.** Design a scored ethics-and-risk decision matrix rather than treating it as a numeric permit substitute. Produce a figure with named axes or a specimen-character table, a statement of the sampling unit, and a two-sentence comparison between your preferred interpretation and a defensible alternative. Include the observation most likely to revise your conclusion.

**Check for understanding.** What would change if a portion of the fossil record were never preserved? How might an independent collector find a different result? What information is required before the number calculated above can become a biological claim? How will the specimen and locality be recoverable for a later researcher?

## Integrated investigation: an evidence-to-inference audit

**Research brief.** A fictional regional fossil survey produces incomplete specimen data, three contradictory identifications and uncertain stratigraphic locations; teams design an open and ethical audit. Design a student investigation that tests whether an observed difference reflects ancient biology or the way rocks and specimens were sampled. Begin with a map, stratigraphic table or measured section; create unique IDs, lithology fields, preservation grades, sample dates and collector identifiers. Make a distinction between information recorded directly from fossil material and information inferred by a model, and mark fictional values as synthetic at every stage.

### Recommended workflow

1. Define a focused question and mutually distinguishable predictions before any calculation. Identify the comparison units and the temporal resolution.
2. Audit original observations, including unknown and unusable specimens. Document facies changes and the risk of reworking or time averaging.
3. Examine at least two admissible analysis choices and preserve the alternative results alongside the selected result.
4. Use the provided synthetic dataset as a calculation exercise, not as evidence about a real outcrop.
5. Report a figure, an uncertainty statement, an explicit limitation, and an observation that would cause revision.
6. Record collection permissions and archive metadata, including any reason not to publish exact locality coordinates.

### Reporting and interpretation

A final report should distinguish the statement “we observed this character on this preserved element” from “this animal used this behavior” or “this group diversified at this time.” Explain the inferential bridge that connects each stage. A statistical trend in specimen counts requires assumptions about collection effort, taxonomic consistency and geological availability before it supports an evolutionary claim. Conversely, a well-preserved fossil with excellent anatomical detail can be weak evidence for local abundance if its origin or geological setting is poorly documented. A transparent limitations paragraph is an essential result, not a concession.

## Practical simulation notes

Two self-contained browser models accompany this unit: **Provenance metadata completeness** and **Binomial standard error of a sampled proportion**. Each changes one explicitly described parameter and computes a toy result using the expression provided in MODELS.json. Record values near the minimum, midpoint and maximum, and explain why the output should not be treated as a field-validated biological estimate. In particular, avoid applying a visual trend line to stratigraphic gaps, population histories or laboratory processes for which the underlying simplifications are false.

## Assessment prompts

- Explain the difference between a direct fossil observation and a model-dependent paleoecological interpretation.
- Propose a preservation or sampling mechanism that could reverse a naive abundance comparison.
- Document an alternate character coding, correlation or stratigraphic age interpretation.
- Show the units and arithmetic in one worked case and identify a meaningful source of uncertainty.
- Describe how you would make your analysis reproducible without exposing protected fossil localities.

