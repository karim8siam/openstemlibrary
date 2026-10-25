# Unit 1: Molecular information

## Unit overview

Information stored in nucleic acids must be represented at multiple levels: polymer chemistry, sequence, transcriptional units and observable phenotype. The same base pair can be a stable part of a DNA helix and a mutable target of damage, while the same DNA locus may support several RNA products. The organizing question is which information is copied, which is interpreted, and which is regulated. Distinguish the chemical substrate from an abstract sequence string. A reader should be able to describe strand polarity without confusing it with the orientation of the printed reference genome. Throughout the unit, use separate symbols for gene dosage, transcript abundance and protein output.

## Learning goals

Understand the causal molecular sequence for four named processes; derive and interpret simplified quantitative statements; identify measurement controls; separate experimental observation from molecular inference; and explain the limits of the idealized simulation models.

## Unit synthesis

A particularly useful synthesis question is whether a molecule's existence proves the flow of information proposed for it. Begin with DNA sequence and ask what must happen for it to be copied into RNA, what molecular machinery determines which portion is transcribed, and what further events make a corresponding protein. Distinguish chemical stability of an individual duplex from persistence of a genetic signal through cell divisions. Then add one noncoding RNA with a demonstrated function and explain why its lack of translation does not make it informationally irrelevant. Repeat the diagram for a reverse-transcribing system, marking the unusual RNA-to-DNA step explicitly. At each stage classify the evidence as sequence determination, molecular abundance, direct synthesis, binding interaction or phenotypic output. This exercise prevents the central dogma from being taught as a prohibition against regulatory RNA or reverse transcription. It also motivates why genomics, transcriptomics and proteomics have distinct experimental denominators.

## Unit-specific integrated assessment

Before leaving molecular information, reconstruct the logic of a real sequence annotation. Give a student one short synthetic reference DNA segment, two imagined RNA sequences and one hypothetical peptide sequence. Require a strand-aware alignment and ask whether the RNA observations might represent separate genes, separate isoforms, or an annotation error. The first grading criterion is explicit strand polarity; the second is whether the student can name an assay that distinguishes the explanations. If a second transcript shares several exons but starts at another position, a genome-based gene count can remain unchanged even as measured RNA diversity increases. Mark every claim about function as tentative unless a relevant biochemical or genetic experiment was specified. Students should be able to explain why a list of computationally predicted open reading frames, however long, is not a complete record of cellular proteins.

## 1.1 DNA duplex chemistry

### Mechanistic foundation

DNA antiparallel strands are joined by base pairing between A and T, and between G and C. The sugar–phosphate backbone has directionality: a strand runs from its 5-prime end toward its 3-prime end. Complementarity provides a template for faithful copying but does not itself prevent chemical damage or polymerase error. Base stacking, solvent, counterions and sequence context contribute to helix stability. DNA can adopt conformations other than the familiar B-form, especially under changed hydration or torsional constraints.

### Stepwise reasoning from molecular events to an observation

A useful molecular explanation begins by identifying the actual substrate and product in **dna duplex chemistry**, rather than merely naming a molecule associated with the phenomenon. The starting claim is that dNA antiparallel strands are joined by base pairing between A and T, and between G and C. Ask first which individual components must physically meet; next identify a recognition step, a chemical or structural transformation, and the condition under which the outcome is stable. If those events are not separated, an experiment that detects only the endpoint can mistakenly attribute it to one molecular actor. In an active cell, production and consumption often occur simultaneously. A larger observed pool may arise from stronger synthesis, slower clearance, recruitment of another compartment, or altered sampling. For dna duplex chemistry, the distinction is especially consequential because dNA can adopt conformations other than the familiar B-form, especially under changed hydration or torsional constraints.

Draw a causal diagram for this topic containing at least four nodes: the starting material, a relevant enzyme or molecular complex, an intermediate state, and the measured endpoint. Put a question mark next to any edge for which only a correlation has been described. Compare a perturbation performed before the proposed rate-limiting step with one performed after it. Even if both perturbations change the same endpoint, that result does not imply a common mechanism. The exercise forces an explicit distinction between temporal order and molecular necessity, and it clarifies what observation would be incompatible with the simplest story.

### Study design: choosing what to observe

Compare melting profiles for a short GC-rich duplex and an AT-rich duplex while holding oligonucleotide length and salt concentration constant. A difference in melting temperature can support a stability hypothesis, not directly reveal an individual hydrogen bond energy. A well-designed molecular study adds a reference measurement that checks whether the sample or detection system changed independently of the mechanism. For a sequence experiment the reference may be matched genomic DNA or an external standard; for an RNA experiment it may be spike-in controls and an independently measured cell count; for a protein experiment it may be a verified loading standard and a functional assay. The appropriate selection depends on the mechanism in this section and cannot be chosen solely because a method is common in a textbook. Predefine the treatment dose, collection schedule, exclusion criteria and primary readout before examining results. That prevents the story from being rewritten to fit the most attractive observation.

For **dna duplex chemistry**, write down the expected results for three matched conditions: an unperturbed sample, a targeted perturbation of the proposed molecular step, and a rescue that restores function without otherwise changing the assay. A rescue supports specificity when it reverses the perturbation outcome, but interpretation still depends on expression level, genetic background and compartment localization. A fourth condition should deliberately test an alternative explanation. The resulting contrast can be more informative than taking many additional images or sequencing many more copies of one sample.

### Quantitative thinking without false precision

Convert the biological statement into a quantity with explicit units, a denominator, and a population to which it refers. For dna duplex chemistry, distinguishing the number of molecules from the proportion of molecules in a state is often essential. An observed fraction can rise while its numerator falls if the denominator falls even more. Similarly, a fold change says nothing about the baseline: doubling ten molecules is not the same physical event as doubling ten million. When comparing conditions, preserve the definition of the denominator, the measurement window and the sampling unit. A biological replicate is a separate biological sample, not another read from the same library or another image of the same dish.

Start analysis with the limiting cases of an idealized model. At zero substrate, zero elapsed time, or zero available molecular machinery, what output should remain? At a very large stimulus, does the chosen relation saturate, diverge, or become biologically impossible? A relationship may be mathematically consistent yet violate conservation of mass, finite molecular counts or the experiment's detection limit. When writing about dna duplex chemistry, state where idealization ends and empirical validation must begin. The calculation is there to expose assumptions; it should not conceal missing measurements behind multiple decimal places.

### Discriminating causes and ruling out artifacts

Short-primer rules of thumb are not thermodynamic nearest-neighbor predictions; they should not be applied as though they estimate a whole chromosome melting point. Build two alternative hypotheses that could mimic the predicted observation. One should operate earlier in the causal chain and another later, so that they make distinct predictions at an intermediate measurement. If a signal drops, for example, there are at least three possibilities: less synthesis, more degradation, or a loss of cells that contributed the original signal. The purpose of the second assay is not simply to repeat the first with different labels; it is to measure something whose error sources differ. A deletion mutant, a matched DNA sequence, a time-resolved nascent-product assay, and an independent physical readout answer different questions.

A meaningful negative result needs equal scrutiny. Absence of a detectable effect may reflect redundancy, insufficient perturbation, inadequate sensitivity or the wrong sampling interval. Establish the dynamic range with positive and negative controls. If the proposed change is smaller than instrument variation, a larger sample cannot repair a systematic calibration error. If a mutation alters growth rate, normalize carefully before interpreting any difference in extracted DNA, RNA or protein. Mechanism claims should always be narrower than the evidence available to support them.

### Specific molecular investigation

A graduate student designs two 24-base oligonucleotides to bind adjacent regions of a model plasmid. One contains numerous A–T pairs and the other is G–C rich. The naive prediction that every added G–C pair changes duplex stability by a fixed free-energy amount would be wrong: neighboring stacks, salt, strand concentration and mismatched positions matter. An instructor can use the Wallace short-primer estimate to show a qualitative trend, but primer specificity should be checked by sequence alignment and, when accuracy matters, a nearest-neighbor calculation at experimental salt conditions. A negative amplification result might indicate poor annealing rather than absence of the target sequence. The experimentally discriminating measurement would compare amplification over an annealing-temperature gradient with a known-positive template and a no-template control.

## 1.2 RNA molecular classes

### Mechanistic foundation

RNA uses ribose and uracil and is typically single-stranded, yet base pairing produces stems, loops and complex folded architectures. Messenger RNA carries coding information; ribosomal and transfer RNAs participate directly in translation; small nuclear RNAs help splice pre-mRNA; microRNAs and long noncoding RNAs can regulate processes in particular contexts. RNA stability depends on sequence, structure, associated proteins and compartment. Some RNAs act as enzymes; the ribosome peptidyl-transferase center is an important example of RNA-mediated catalysis.

### Stepwise reasoning from molecular events to an observation

A useful molecular explanation begins by identifying the actual substrate and product in **rna molecular classes**, rather than merely naming a molecule associated with the phenomenon. The starting claim is that rNA uses ribose and uracil and is typically single-stranded, yet base pairing produces stems, loops and complex folded architectures. In an active cell, production and consumption often occur simultaneously. For rna molecular classes, the distinction is especially consequential because some RNAs act as enzymes; the ribosome peptidyl-transferase center is an important example of RNA-mediated catalysis.



### Study design: choosing what to observe

Separate total RNA into size classes and use an appropriate hybridization probe to follow one transcript after transcriptional shutoff. Measure both the RNA itself and a candidate protein product, since a change in RNA abundance is not necessarily a matching change in protein.

For **rna molecular classes**, write down the expected results for three matched conditions: an unperturbed sample, a targeted perturbation of the proposed molecular step, and a rescue that restores function without otherwise changing the assay. A fourth condition should deliberately test an alternative explanation.

### Quantitative thinking without false precision

For rna molecular classes, distinguishing the number of molecules from the proportion of molecules in a state is often essential.

Start analysis with the limiting cases of an idealized model. When writing about rna molecular classes, state where idealization ends and empirical validation must begin.

### Discriminating causes and ruling out artifacts

Not every transcript encodes a protein. Detection of a noncoding RNA does not demonstrate a particular regulatory function without perturbation and rescue. Build two alternative hypotheses that could mimic the predicted observation.

A meaningful negative result needs equal scrutiny. Establish the dynamic range with positive and negative controls.

### Specific molecular investigation

Consider a tissue sample yielding a prominent RNA band near 2 kilobases. The band could contain many different transcripts with similar size, including coding messages and long noncoding species. If a lab labels newly synthesized RNA and then measures total signal at one endpoint, it cannot distinguish production from turnover for any particular RNA class. A targeted probe to a defined exon, a probe for an intronic precursor, and an independently quantified mature RNA would give contrasting evidence about synthesis versus processing. Ribosomal RNA often dominates total-RNA mass, so normalizing an individual messenger RNA to all recovered RNA has context-specific assumptions. When one knockdown alters translation but scarcely changes transcript abundance, an RNA-dependent translational mechanism becomes plausible, but remains to be verified by a protein-production assay.

## 1.3 Genes and genomic architecture

### Mechanistic foundation

A gene may include transcribed untranslated regions, coding exons, introns and regulatory information spread across considerable genomic distances. In bacteria, an operon can place several protein-coding regions in one transcription unit, whereas many eukaryotic transcripts are processed through splicing and alternative polyadenylation. Gene boundaries depend partly on whether one is describing a DNA locus, a transcription unit or an annotated protein product. Repetitive elements, regulatory sites and structural regions are not expendable merely because they lack a conventional open reading frame.

### Stepwise reasoning from molecular events to an observation

A useful molecular explanation begins by identifying the actual substrate and product in **genes and genomic architecture**, rather than merely naming a molecule associated with the phenomenon. The starting claim is that a gene may include transcribed untranslated regions, coding exons, introns and regulatory information spread across considerable genomic distances. In an active cell, production and consumption often occur simultaneously. For genes and genomic architecture, the distinction is especially consequential because repetitive elements, regulatory sites and structural regions are not expendable merely because they lack a conventional open reading frame.



### Study design: choosing what to observe

Compare genomic DNA, nascent RNA and mature RNA tracks across the same locus. Introns present in DNA and pre-mRNA but absent in a mature splice isoform distinguish transcription from mature-RNA structure.

For **genes and genomic architecture**, write down the expected results for three matched conditions: an unperturbed sample, a targeted perturbation of the proposed molecular step, and a rescue that restores function without otherwise changing the assay. A fourth condition should deliberately test an alternative explanation.

### Quantitative thinking without false precision

For genes and genomic architecture, distinguishing the number of molecules from the proportion of molecules in a state is often essential.

Start analysis with the limiting cases of an idealized model. When writing about genes and genomic architecture, state where idealization ends and empirical validation must begin.

### Discriminating causes and ruling out artifacts

Avoid treating an annotation as complete ground truth; alternative transcript starts and tissue-specific exons alter what a gene produces. Build two alternative hypotheses that could mimic the predicted observation.

A meaningful negative result needs equal scrutiny. Establish the dynamic range with positive and negative controls.

### Specific molecular investigation

Imagine a gene catalog that lists a single long protein isoform from a locus, while long-read transcript data identify an additional exon-skipping RNA in one differentiated cell type. A simple count of genes would miss the isoform difference. Map each observed RNA onto genomic coordinates, mark the splice junctions, and determine whether the resulting reading frame is preserved. If the skipped exon changes a receptor-binding domain, an expression assay for total RNA cannot tell which functional protein species is present. A junction-specific assay and isoform-aware protein measurement would be useful complements. A nearby enhancer can act on several genes, so a DNA interval annotated as regulatory must not automatically be assigned to its nearest coding sequence. Annotation is an evolving evidence model.

## 1.4 Information flow and its exceptions

### Mechanistic foundation

DNA replication preserves heritable sequence across divisions, transcription produces RNA, and translation uses messenger RNA to specify amino-acid order. This framing captures much of cellular information flow but is not a claim that every information transfer is DNA to RNA to protein. Reverse transcription transfers information from RNA to DNA, and many regulatory RNAs influence phenotype without being translated. Protein conformational inheritance and RNA editing also illustrate why genotype-to-phenotype relationships cannot be reduced to a single unidirectional arrow.

### Stepwise reasoning from molecular events to an observation

A useful molecular explanation begins by identifying the actual substrate and product in **information flow and its exceptions**, rather than merely naming a molecule associated with the phenomenon. The starting claim is that dNA replication preserves heritable sequence across divisions, transcription produces RNA, and translation uses messenger RNA to specify amino-acid order. In an active cell, production and consumption often occur simultaneously. For information flow and its exceptions, the distinction is especially consequential because protein conformational inheritance and RNA editing also illustrate why genotype-to-phenotype relationships cannot be reduced to a single unidirectional arrow.



### Study design: choosing what to observe

Trace an inducible reporter at DNA, RNA and protein levels over time. The sequence of appearance and disappearance distinguishes the measurement stages but does not automatically identify which stage is rate limiting.

For **information flow and its exceptions**, write down the expected results for three matched conditions: an unperturbed sample, a targeted perturbation of the proposed molecular step, and a rescue that restores function without otherwise changing the assay. A fourth condition should deliberately test an alternative explanation.

### Quantitative thinking without false precision

For information flow and its exceptions, distinguishing the number of molecules from the proportion of molecules in a state is often essential.

Start analysis with the limiting cases of an idealized model. When writing about information flow and its exceptions, state where idealization ends and empirical validation must begin.

### Discriminating causes and ruling out artifacts

RNA abundance is neither equal to protein abundance nor a universal proxy for enzymatic activity; translation efficiency, protein turnover and post-translational modification matter. Build two alternative hypotheses that could mimic the predicted observation.

A meaningful negative result needs equal scrutiny. Establish the dynamic range with positive and negative controls.

### Specific molecular investigation

A researcher introduces a reporter cassette into cultured cells and observes RNA after two hours, fluorescence after eight hours, and a stable phenotype after a day. These lags do not prove that the reporter drives the phenotype. Protein maturation, RNA export and integration of downstream signals could explain the delay. Measure nascent RNA, total mature RNA and functional protein at matched time points. If the reporter RNA disappears after stimulus withdrawal but protein fluorescence persists, protein lifetime and fluorophore maturation become critical alternatives. Reverse-transcription activity, where relevant, should be analyzed as a distinct RNA-to-DNA flow rather than treated as an exception that makes the whole information framework useless. Clearly annotate which arrows were directly measured and which are presumed.

## Guided molecular investigation

### Evidence integration lab

The aim of this studio is to compare molecular readouts that often have different denominators or experimental biases. Begin with a blinded sample label and a recorded protocol. In the analysis, separate substrate abundance, product abundance, reaction rate, and biological outcome. Use three genuinely independent biological samples per condition as an illustrative minimal planning exercise, while acknowledging that sample-size requirements depend on power, variation and experimental design. The hypothetical study below asks you to predict data patterns rather than pretending the described results have been observed.

### Investigation 1.1: DNA duplex chemistry and RNA molecular classes

A lab attempts to connect dna duplex chemistry to rna molecular classes using a shared perturbation. The first obligation is to keep the prediction narrow. DNA antiparallel strands are joined by base pairing between A and T, and between G and C. The sugar–phosphate backbone has directionality: a strand runs from its 5-prime end toward its 3-prime end. Complementarity provides a template for faithful copying but does not itself prevent chemical damage or polymerase error. Base stacking, solvent, counterions and sequence context contribute to helix stability. DNA can adopt conformations other than the familiar B-form, especially under changed hydration or torsional constraints. The connected response should be measured separately because RNA uses ribose and uracil and is typically single-stranded, yet base pairing produces stems, loops and complex folded architectures. Messenger RNA carries coding information; ribosomal and transfer RNAs participate directly in translation; small nuclear RNAs help splice pre-mRNA; microRNAs and long noncoding RNAs can regulate processes in particular contexts. RNA stability depends on sequence, structure, associated proteins and compartment. Some RNAs act as enzymes; the ribosome peptidyl-transferase center is an important example of RNA-mediated catalysis. A single terminal measurement cannot determine whether the perturbation changed upstream material, a rate-limiting processing step, or sample survival. The study therefore predefines an early molecular observation and a late functional output, with an explicit normalization rule for each.

The proposed primary assay follows this plan: Compare melting profiles for a short GC-rich duplex and an AT-rich duplex while holding oligonucleotide length and salt concentration constant. A difference in melting temperature can support a stability hypothesis, not directly reveal an individual hydrogen bond energy. An orthogonal procedure addresses the downstream question: Separate total RNA into size classes and use an appropriate hybridization probe to follow one transcript after transcriptional shutoff. Measure both the RNA itself and a candidate protein product, since a change in RNA abundance is not necessarily a matching change in protein. Its independent readout should not reuse the same molecular normalization error. Include a negative treatment, a validated positive comparison if available, and a material-balance or integrity control. When analyzing a gene perturbation, record allele or construct verification separately from RNA abundance and protein abundance. That prevents the convenient but unsupported inference that a verified DNA change automatically changed function.

For the interpretation, construct a table with rows for no change, increased upstream signal only, changed downstream signal only, and concordant changes in both. State at least two plausible mechanisms for each nonzero pattern. The most serious limitation may involve genes and genomic architecture: Avoid treating an annotation as complete ground truth; alternative transcript starts and tissue-specific exons alter what a gene produces. A satisfactory report includes the type of observation that would falsify the chosen mechanism, the magnitude of technical uncertainty, and an explanation of which conclusions are about a model versus observed living cells. The outcome is a proposed experimental logic, not a claim that biological data were collected.

## Fully worked questions

All numerical inputs are constructed teaching examples. Where a model is conditional, that condition is part of the solution.

### Problem 1: Duplex GC fraction

A 40-base-pair DNA duplex contains 14 G–C pairs and 26 A–T pairs. Find the GC percentage and the total number of hydrogen bonds in an idealized counting exercise.

**Worked reasoning**

1. GC fraction = 14/40 = 0.35, or 35%.
2. Count three nominal hydrogen bonds per G–C pair and two per A–T pair: 14×3 + 26×2 = 94.
3. This count is a bookkeeping description of pairing contacts, not a thermodynamic melting-energy estimate.
4. Base stacking and solution conditions have substantial effects.

### Problem 2: Sequence information entropy

Consider an independent-base model with base probabilities A=T=0.35 and G=C=0.15. Calculate Shannon information entropy per nucleotide.

**Worked reasoning**

1. Use H=−Σp log2 p.
2. Group the equal probabilities: H=−2[0.35 log2(0.35)+0.15 log2(0.15)] ≈1.8813 bits per base.
3. The maximum with four equally probable independent bases is 2 bits.
4. Correlations, repeats and biological constraints make this base-frequency-only model an upper-level summary, not a compression rate for an actual genome.

### Problem 3: Coding frame translation

A bacterial open reading frame has 901 nucleotides including a start codon and a three-nucleotide stop codon. Is the annotation consistent with an uninterrupted standard reading frame?

**Worked reasoning**

1. A coding region including the stop must contain a multiple of three nucleotides.
2. Because 901 ÷ 3 = 300 remainder 1, the indicated length cannot represent exactly 300 codons plus a complete terminal codon.
3. Recheck coordinate conventions, whether an intron is present, or a base was included erroneously.
4. A one-base discrepancy is not proof of biological programmed frameshifting.

## Simulations and assumptions

The two simulation cards below are local, offline-capable numerical thought experiments. They are parameterized formula demonstrations, not mechanistic claims about a real cell type. Inspect the stated assumptions first, then vary an input, compare limiting cases and reset the model to its default.

### Model focus: Short-primer Wallace estimate

The simplest short-oligonucleotide melting estimate treats each A–T pair as contributing two Celsius degrees and each G–C pair as four. Let L denote duplex length and g the count of GC pairs; then T≈2(L−g)+4g=2L+2g. For a 28-bp duplex with eight GC pairs this produces 72°C, a deliberately rough estimate. At fixed L, replacing one AT pair with one GC pair raises this rule-of-thumb prediction by two degrees. At fixed g, lengthening the duplex by one AT pair produces an additional two degrees. These are mathematical properties of the approximation, not measured changes in thermodynamic stability. Long oligonucleotides require sequence-order-dependent, salt-corrected models; mismatches and strand concentration can alter melting behavior. A suitable learning experiment is to compare the plotted prediction against nearest-neighbor software for several realistic candidate primers while explaining why the two curves differ.

### Model application and sensitivity test

Take three candidate 24-bp primer duplexes with six, twelve and eighteen G–C pairs, respectively. The Wallace estimate predicts temperatures of 60, 72 and 84 Celsius degrees because replacing an A–T pair by a G–C pair adds two degrees in this deliberately crude rule. With duplex length changed to 32 pairs while holding the GC count at twelve, the rule instead predicts 88 degrees. Use these observations to distinguish the effects of length and composition in the algebra. Now construct a pair of primers with the same GC count but different adjacent base ordering. The model gives them equal estimated temperatures even though nearest-neighbor stacking effects may differ; this is a concrete model falsification exercise, not a computational bug. Evaluate whether each proposed primer could form an off-target match, a hairpin or a self-dimer. Those structures involve thermodynamics and specificity absent from the simplified graph. The best real-world design procedure reports annealing conditions, sequence-dependent energy estimation and an empirically validated temperature range. A model can be internally correct and unsuitable for an experimental decision.

### Model focus: Sequence-base entropy

Shannon entropy depends on base proportions in an independent-symbol approximation. Let g be total GC fraction and b a within-group bias; this model assigns G=gb, C=g(1−b), A=(1−g)(1−b), and T=(1−g)b. The four probabilities sum to one. The formula H=−Σp log₂p yields at most two bits per nucleotide when all base probabilities equal one-quarter. Making one base class dominate reduces this marginal-frequency entropy even when sequence length is unchanged. An actual genome contains correlations, codon constraints, repetitive DNA and functional motifs that this four-frequency model cannot capture. To explore the boundary, choose g=0.5 and b=0.5, then move either control toward a biased composition. If a plotted curve descends, this tells you only that base-frequency uncertainty has decreased under the model; it does not prove biological information has been lost.

### Model application and sensitivity test

Begin with an imagined DNA collection in which all four bases are equally common and independent. Entropy per position is exactly two bits. Now set GC fraction to ninety percent while dividing GC evenly between G and C and dividing the remaining ten percent evenly between A and T. The marginal entropy becomes smaller, even if the sequence still contains many regulatory motifs. Compute the contribution from each class rather than judging entropy by the most common letter alone. Next construct two sequences with identical A, C, G and T counts: one is shuffled at random and another consists of long repeated blocks. The simulation assigns equal base-frequency entropy to both because it lacks positional dependencies. A context-dependent model would not. This thought experiment shows why a base histogram is not synonymous with genomic complexity, genome size or biological meaning. When comparing real genomes, document ambiguous bases, strand representation, organellar sequences and whether the counts cover assembled reference regions or raw sequence reads.
