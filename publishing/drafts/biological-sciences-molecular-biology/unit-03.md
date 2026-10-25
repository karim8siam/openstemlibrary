# Unit 3: Genome maintenance

## Unit overview

Genomes are chemically vulnerable but actively maintained. The term repair must always be connected to a substrate, a molecular pathway and an outcome. Removing a damaged base is not identical to restoring sequence, and sealing a break is not always error free. Population survival is a poor substitute for lesion-specific recovery if severely damaged cells disappear from the assay. This unit compares multiple ways of handling damage and explores how recombination and mobile elements also contribute to genome variability. Readers should distinguish conservative restoration from sequence-changing outcomes.

## Learning goals

Understand the causal molecular sequence for four named processes; derive and interpret simplified quantitative statements; identify measurement controls; separate experimental observation from molecular inference; and explain the limits of the idealized simulation models.

## Unit synthesis

The most difficult interpretive problem in genome maintenance is the difference between repairing a lesion and recovering viable cells. A cell may survive with a changed sequence, die without completing repair, or experience correct restoration while temporarily stopping the cell cycle. Construct a study with one lesion-specific endpoint, one sequence-integrity endpoint and one physiological endpoint. Then predict a hypothetical case in which those three disagree. For instance, repair-associated marker disappearance might occur faster than sequence recovery, or a recombination-based reporter might improve while total survival declines through unrelated stress. Consider how mobile DNA changes the meaning of conservation: preserving chromosome continuity can still create a new insertion. A mechanism must therefore be described by chemical substrate, pathway choice and resulting DNA sequence rather than by survival alone.

## Unit-specific integrated assessment

For genome maintenance, present a fictional dataset with three readouts at baseline and after a lesion-producing exposure: chemical damage, cell survival and sequence changes among survivors. The puzzle is to interpret a condition in which damage signal falls but the variant fraction rises. One possible explanation is erroneous repair among living cells; another is selective retention of a subpopulation with distinct starting sequences. A student should request matched untreated controls and lineage information before distinguishing these accounts. Then introduce a reporter that scores only one recombination product and ask whether reporter-negative cells necessarily used end joining. The correct answer is no: several alternative fates can escape the reporter. This exercise requires recognizing both biological pathway competition and measurement-selection bias, without treating all sequence changes as equivalent to unrepaired DNA lesions.

## 3.1 Sources of DNA damage

### Mechanistic foundation

Ultraviolet radiation can produce pyrimidine photoproducts; oxidation can alter bases; spontaneous hydrolysis can generate abasic sites; replication stress can expose stretches of single-stranded DNA. Double-strand breaks arise through distinct physical and enzymatic causes. Some lesions block polymerase progression and others alter base-pairing preferences. The organism must manage damage while maintaining chromosome continuity and preserving function, and there is no single generic pathway that repairs every lesion.

### Stepwise reasoning from molecular events to an observation

A useful molecular explanation begins by identifying the actual substrate and product in **sources of dna damage**, rather than merely naming a molecule associated with the phenomenon. The starting claim is that ultraviolet radiation can produce pyrimidine photoproducts; oxidation can alter bases; spontaneous hydrolysis can generate abasic sites; replication stress can expose stretches of single-stranded DNA. In an active cell, production and consumption often occur simultaneously. For sources of dna damage, the distinction is especially consequential because the organism must manage damage while maintaining chromosome continuity and preserving function, and there is no single generic pathway that repairs every lesion.



### Study design: choosing what to observe

Use lesion-specific antibodies or sequencing-derived signals to measure the disappearance of a particular damage class across several time points. Include a no-exposure background and a viability measurement.

For **sources of dna damage**, write down the expected results for three matched conditions: an unperturbed sample, a targeted perturbation of the proposed molecular step, and a rescue that restores function without otherwise changing the assay. A fourth condition should deliberately test an alternative explanation.

### Quantitative thinking without false precision

For sources of dna damage, distinguishing the number of molecules from the proportion of molecules in a state is often essential.

Start analysis with the limiting cases of an idealized model. When writing about sources of dna damage, state where idealization ends and empirical validation must begin.

### Discriminating causes and ruling out artifacts

A declining damage signal may represent repair, degradation of damaged DNA, dilution during replication or selective loss of heavily damaged cells. Build two alternative hypotheses that could mimic the predicted observation.

A meaningful negative result needs equal scrutiny. Establish the dynamic range with positive and negative controls.

### Specific molecular investigation

A light-exposed cell culture shows a declining signal from a lesion-specific antibody over twelve hours. Disappearance is compatible with lesion processing but not a unique signature of enzymatic repair. Cells carrying the largest lesion loads might detach or die, leaving a biased surviving fraction. Collect lesion signal per cell together with cell number, viability and lesion-site enrichment. If the initial damage is uneven, normalize within comparable damage-load strata rather than assuming all cells received identical exposure. A photoproduct-specific assay should not be treated as a measure of oxidized purines. Lesion classes differ in their chemistry and in the processing complexes that recognize them.

## 3.2 Excision and mismatch repair

### Mechanistic foundation

Base-excision repair usually removes altered bases through glycosylase-initiated pathways, followed by backbone processing, synthesis and ligation. Nucleotide-excision repair removes short oligonucleotide segments containing certain bulky lesions. Mismatch repair recognizes some copying errors or insertion–deletion loops after replication. Pathway components and strand-discrimination mechanisms differ across organisms. Repair pathway names describe characteristic substrates and reaction logic, not perfectly isolated channels with no overlap.

### Stepwise reasoning from molecular events to an observation

A useful molecular explanation begins by identifying the actual substrate and product in **excision and mismatch repair**, rather than merely naming a molecule associated with the phenomenon. The starting claim is that base-excision repair usually removes altered bases through glycosylase-initiated pathways, followed by backbone processing, synthesis and ligation. In an active cell, production and consumption often occur simultaneously. For excision and mismatch repair, the distinction is especially consequential because repair pathway names describe characteristic substrates and reaction logic, not perfectly isolated channels with no overlap.



### Study design: choosing what to observe

Measure reporter restoration after introducing a defined lesion and compare genetically complemented and repair-defective cells. Complementation strengthens a causal claim but does not eliminate indirect effects of the introduced gene.

For **excision and mismatch repair**, write down the expected results for three matched conditions: an unperturbed sample, a targeted perturbation of the proposed molecular step, and a rescue that restores function without otherwise changing the assay. A fourth condition should deliberately test an alternative explanation.

### Quantitative thinking without false precision

For excision and mismatch repair, distinguishing the number of molecules from the proportion of molecules in a state is often essential.

Start analysis with the limiting cases of an idealized model. When writing about excision and mismatch repair, state where idealization ends and empirical validation must begin.

### Discriminating causes and ruling out artifacts

Do not infer repair-pathway participation solely from transcriptional upregulation of a repair gene. Functional substrate measurements and genetic epistasis are necessary. Build two alternative hypotheses that could mimic the predicted observation.

A meaningful negative result needs equal scrutiny. Establish the dynamic range with positive and negative controls.

### Specific molecular investigation

A genetic screen identifies cells unusually sensitive to a chemical that forms bulky DNA adducts. A tempting conclusion is that a missing protein carries out direct adduct removal. However, the gene may instead affect damage signaling, cell-cycle arrest or the supply of repair precursors. Sequence or biochemical evidence for excised oligonucleotides would provide a more direct readout of one pathway class. Compare with a different lesion type processed by another route and test whether restoring the gene rescues both survival and lesion removal. A survival curve should be reported as a physiological endpoint; it is not an assay of chemical repair stoichiometry.

## 3.3 Homologous recombination and end joining

### Mechanistic foundation

Homologous recombination can use a related DNA sequence as information for repair of a broken molecule, often involving resection, strand invasion and DNA synthesis. Nonhomologous end joining restores continuity by directly processing and joining DNA ends, potentially with sequence change. Pathway selection depends on cell-cycle state, available template, end chemistry and species. Meiosis uses recombination in another context to exchange genetic information between homologs.

### Stepwise reasoning from molecular events to an observation

A useful molecular explanation begins by identifying the actual substrate and product in **homologous recombination and end joining**, rather than merely naming a molecule associated with the phenomenon. The starting claim is that homologous recombination can use a related DNA sequence as information for repair of a broken molecule, often involving resection, strand invasion and DNA synthesis. In an active cell, production and consumption often occur simultaneously. For homologous recombination and end joining, the distinction is especially consequential because meiosis uses recombination in another context to exchange genetic information between homologs.



### Study design: choosing what to observe

Use matched reporters that score distinct repair outcomes after the same engineered break, measuring both total survival and sequence of repaired junctions.

For **homologous recombination and end joining**, write down the expected results for three matched conditions: an unperturbed sample, a targeted perturbation of the proposed molecular step, and a rescue that restores function without otherwise changing the assay. A fourth condition should deliberately test an alternative explanation.

### Quantitative thinking without false precision

For homologous recombination and end joining, distinguishing the number of molecules from the proportion of molecules in a state is often essential.

Start analysis with the limiting cases of an idealized model. When writing about homologous recombination and end joining, state where idealization ends and empirical validation must begin.

### Discriminating causes and ruling out artifacts

A fluorescent reporter only detects its permitted class of outcomes. Off-target events and death of cells with another outcome create measurement bias. Build two alternative hypotheses that could mimic the predicted observation.

A meaningful negative result needs equal scrutiny. Establish the dynamic range with positive and negative controls.

### Specific molecular investigation

Two reporter constructs are integrated at different chromosomal positions: one measures sequence restoration through a homologous template, the other scores junction formation after a break. Differences between constructs may reflect chromatin access as well as pathway choice. A more controlled design places distinct reporters at comparable loci or quantifies the relevant chromosomal context. Sequence the repaired junctions to distinguish precise restoration from insertions and deletions. Count repaired cells relative to the number initially eligible to experience the break, not only the number that survive. Recombination is also used for programmed chromosome exchanges in meiosis; repair outcomes and meiotic crossovers should not be collapsed into one rate.

## 3.4 Transposons and genome plasticity

### Mechanistic foundation

Transposable elements move or copy portions of sequence through DNA- or RNA-associated intermediates. Insertion may interrupt coding regions, change regulatory elements or supply material later co-opted by evolution. Some elements depend on enzymes encoded by the element and others on machinery supplied in trans. Genome assemblies often struggle in repeated regions; a sudden increase in inferred copy number can reflect improved assembly rather than contemporary transposition.

### Stepwise reasoning from molecular events to an observation

A useful molecular explanation begins by identifying the actual substrate and product in **transposons and genome plasticity**, rather than merely naming a molecule associated with the phenomenon. The starting claim is that transposable elements move or copy portions of sequence through DNA- or RNA-associated intermediates. In an active cell, production and consumption often occur simultaneously. For transposons and genome plasticity, the distinction is especially consequential because genome assemblies often struggle in repeated regions; a sudden increase in inferred copy number can reflect improved assembly rather than contemporary transposition.



### Study design: choosing what to observe

Combine long-read junction evidence with short-read coverage and locus-specific validation before inferring a new insertion. Follow generations to distinguish somatic mosaicism from germline transmission.

For **transposons and genome plasticity**, write down the expected results for three matched conditions: an unperturbed sample, a targeted perturbation of the proposed molecular step, and a rescue that restores function without otherwise changing the assay. A fourth condition should deliberately test an alternative explanation.

### Quantitative thinking without false precision

For transposons and genome plasticity, distinguishing the number of molecules from the proportion of molecules in a state is often essential.

Start analysis with the limiting cases of an idealized model. When writing about transposons and genome plasticity, state where idealization ends and empirical validation must begin.

### Discriminating causes and ruling out artifacts

A simple multiplying copy-number model ignores insertional selection, silencing, depletion of active copies and host-specific regulation. Build two alternative hypotheses that could mimic the predicted observation.

A meaningful negative result needs equal scrutiny. Establish the dynamic range with positive and negative controls.

### Specific molecular investigation

An assembled genome appears to contain thirty copies of a transposon family where a prior release listed twenty. The difference is not necessarily new transposition: a more contiguous assembly may resolve repeats previously hidden or collapsed. Identify new genomic junctions supported by independent long reads and verify the germline status of the insertion. A copy-number amplification curve can illustrate hypothetical unchecked expansion, but insertions can alter their own host environment and may be silenced. Comparing active transposase expression with insertion-site evidence distinguishes expression of a mobile element from actual movement. Evolutionary presence of repeats is not a record of movement within one experiment.

## Guided molecular investigation

### Evidence integration lab

The aim of this studio is to compare molecular readouts that often have different denominators or experimental biases. Begin with a blinded sample label and a recorded protocol. In the analysis, separate substrate abundance, product abundance, reaction rate, and biological outcome. Use three genuinely independent biological samples per condition as an illustrative minimal planning exercise, while acknowledging that sample-size requirements depend on power, variation and experimental design. The hypothetical study below asks you to predict data patterns rather than pretending the described results have been observed.

### Investigation 3.1: Sources of DNA damage and Excision and mismatch repair

A lab attempts to connect sources of dna damage to excision and mismatch repair using a shared perturbation. The first obligation is to keep the prediction narrow. Ultraviolet radiation can produce pyrimidine photoproducts; oxidation can alter bases; spontaneous hydrolysis can generate abasic sites; replication stress can expose stretches of single-stranded DNA. Double-strand breaks arise through distinct physical and enzymatic causes. Some lesions block polymerase progression and others alter base-pairing preferences. The organism must manage damage while maintaining chromosome continuity and preserving function, and there is no single generic pathway that repairs every lesion. The connected response should be measured separately because Base-excision repair usually removes altered bases through glycosylase-initiated pathways, followed by backbone processing, synthesis and ligation. Nucleotide-excision repair removes short oligonucleotide segments containing certain bulky lesions. Mismatch repair recognizes some copying errors or insertion–deletion loops after replication. Pathway components and strand-discrimination mechanisms differ across organisms. Repair pathway names describe characteristic substrates and reaction logic, not perfectly isolated channels with no overlap. A single terminal measurement cannot determine whether the perturbation changed upstream material, a rate-limiting processing step, or sample survival. The study therefore predefines an early molecular observation and a late functional output, with an explicit normalization rule for each.

The proposed primary assay follows this plan: Use lesion-specific antibodies or sequencing-derived signals to measure the disappearance of a particular damage class across several time points. Include a no-exposure background and a viability measurement. An orthogonal procedure addresses the downstream question: Measure reporter restoration after introducing a defined lesion and compare genetically complemented and repair-defective cells. Complementation strengthens a causal claim but does not eliminate indirect effects of the introduced gene. Its independent readout should not reuse the same molecular normalization error. Include a negative treatment, a validated positive comparison if available, and a material-balance or integrity control. When analyzing a gene perturbation, record allele or construct verification separately from RNA abundance and protein abundance. That prevents the convenient but unsupported inference that a verified DNA change automatically changed function.

For the interpretation, construct a table with rows for no change, increased upstream signal only, changed downstream signal only, and concordant changes in both. State at least two plausible mechanisms for each nonzero pattern. The most serious limitation may involve homologous recombination and end joining: A fluorescent reporter only detects its permitted class of outcomes. Off-target events and death of cells with another outcome create measurement bias. A satisfactory report includes the type of observation that would falsify the chosen mechanism, the magnitude of technical uncertainty, and an explanation of which conclusions are about a model versus observed living cells. The outcome is a proposed experimental logic, not a claim that biological data were collected.

## Fully worked questions

All numerical inputs are constructed teaching examples. Where a model is conditional, that condition is part of the solution.

### Problem 1: First-order lesion clearance

A marker for a specific DNA lesion follows ideal first-order disappearance with rate constant 0.18 h⁻¹. What fraction of initial signal remains after 6 h?

**Worked reasoning**

1. Write L(t)/L0=e^(−kt), so e^(−0.18×6)=e^(−1.08)≈0.3396.
2. The model therefore predicts 34.0% of baseline marker signal.
3. Experimental interpretation must exclude loss of damaged cells and signal dilution; marker disappearance is not by itself proof of error-free repair.

### Problem 2: At least one recombination event

Suppose a reporter has independent probability p=0.08 of an observable homologous-recombination event per eligible cell. Among 12 eligible independent cells, what is P(at least one event)?

**Worked reasoning**

1. P(0)=(1−0.08)^12=0.92^12≈0.3677.
2. Therefore P(≥1)=1−0.3677≈0.6323.
3. This assumes equal independent opportunities and perfect reporter detection.
4. Biological clone relationships and cell-state heterogeneity undermine the independence assumption.

### Problem 3: Mutation frequency interpretation

A sequencing screen has 36 candidate variant-supporting molecules among 12,000 high-quality independent molecules. Estimate the observed fraction and a simple binomial standard error.

**Worked reasoning**

1. Observed fraction =36/12000=0.003 or 0.30%.
2. Approximate SE=sqrt[p(1−p)/n]≈0.000499, or 0.050 percentage points.
3. Repeated reads of one original molecule are not independent observations; quality filters and systematic errors can dominate binomial uncertainty.

## Simulations and assumptions

The two simulation cards below are local, offline-capable numerical thought experiments. They are parameterized formula demonstrations, not mechanistic claims about a real cell type. Inspect the stated assumptions first, then vary an input, compare limiting cases and reset the model to its default.

### Model focus: Lesion-marker first-order disappearance

In a one-compartment first-order model of a lesion-specific marker, L(t)=L0 exp(−kt). The variable k is a nonnegative per-hour disappearance constant, and t is measured in hours. The modeled percentage remaining is 100 exp(−kt). For k=0.18 h⁻¹ and t=6 h, the result is approximately 34 percent. The half-disappearance time would be ln(2)/k, about 3.85 hours for this example. Such a calculation does not distinguish chemical excision and repair from loss of damaged cells, label breakdown or other routes for the measured marker to disappear. A research study should pair the signal with cell viability and, if possible, direct lesion-specific sequence recovery. An appropriate model check is to ask whether the logarithm of the corrected remaining signal is nearly linear over an experimentally justified interval.

### Model application and sensitivity test

The half-disappearance time of a lesion marker can be derived without directly examining the graph. Set exp(−kt)=1/2, take logarithms and obtain t=ln(2)/k. At k=0.18 per hour the predicted time is approximately 3.85 hours. At twice that rate, the predicted half-time is halved. Now consider two cell populations with exactly the same marker-disappearance curve but different survival. In one, a pathway removes the chemical lesion; in another, cells carrying the marker die or detach. The same normalized chart would not discriminate the mechanisms. Design a flow-cytometry or imaging experiment that records both per-cell marker intensity and the number of eligible cells over time. Validate the label using a chemically specific reference whenever available. If substantial damage persists in cells that stop proliferating, bulk normalization by total culture material may further distort the trend. A modeled kinetic constant describes the measured disappearance process only when the denominator and biological mechanism are independently established.

### Model focus: At least one reporter recombination

Let p be an independently observed recombination event probability for one eligible cell and n the number of independently eligible cells. The chance of no observed event is (1−p)^n, so the probability of at least one is 1−(1−p)^n. The interface takes p as a percentage, which must be divided by 100 before substitution. Twelve independent opportunities with p=8 percent give a probability near 63 percent of at least one event. Increasing sample size raises the likelihood of at least one event but says nothing about the average number of events per successfully repaired cell. Correlated cell states, reporter sensitivity and selective survival invalidate identical independent trials. To test whether the model is reasonable, compare empirical frequencies across many genuinely independent cultures, not many cells from a single shared colony.

### Model application and sensitivity test

Calculate the relationship between reporter-event probability and sample size without treating a probability of at least one event as an event rate. At p=0.08 per eligible cell, the chance of no events among one, five and twelve independent eligible cells is 0.92, about 0.659 and about 0.368. The complementary values describe at least one event, not the expected number of events. The expected number under independent Bernoulli trials is np, so twelve eligible cells give an expectation of 0.96 observed event-positive cells. An expected count below one can coexist with a probability above one-half of seeing at least one event. Now consider two independent cultures each containing six sibling cells. Correlations within one culture may make the effective number of independent opportunities smaller than twelve. Report the experimental sampling hierarchy and examine how reporter silencing or cell death biases eligibility. A model that assumes equal p should be challenged by measuring cell-state differences before pooling events.
