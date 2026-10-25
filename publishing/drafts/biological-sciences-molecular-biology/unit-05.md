# Unit 5: RNA processing

## Unit overview

RNA maturation determines which molecular messages exist at a given time and in which places. Splice choice, base editing, turnover and guide-RNA interactions can change transcript identity and function without changing the underlying genomic sequence. An isoform fraction is not the same as absolute transcript abundance; an RNA half-life is not a transcription rate. Modern sequencing reveals multiple molecular species but also carries computational ambiguities around overlapping transcripts and repeated sequences. Compare assays that measure precursor RNA, mature RNA, translation and protein abundance to locate regulation.

## Learning goals

Understand the causal molecular sequence for four named processes; derive and interpret simplified quantitative statements; identify measurement controls; separate experimental observation from molecular inference; and explain the limits of the idealized simulation models.

## Unit synthesis

A transcript is better understood as a time-dependent population of molecular isoforms than as a single static text string. Splicing can choose exon combinations, editing can modify selected nucleotides, and surveillance or other turnover mechanisms determine which RNA species persist long enough for detection. Alternative polyadenylation can alter regulatory regions without changing an encoded protein. Consider a locus producing two isoforms: one might dominate RNA sequencing reads and the other produce a more stable protein. A total-gene count would not convey the functional mixture. Design a measurement panel for pre-mRNA abundance, junction usage, RNA half-lives, ribosome association and final protein abundance. Every panel component should have a distinct interpretation and one important measurement failure mode. This design prepares readers to critique simplistic associations between a single RNA read count and a biological phenotype.

## Unit-specific integrated assessment

RNA processing can be assessed by assigning four groups of junction reads to two imaginary tissues, each with different RNA-extraction yields. Students calculate isoform proportions and then notice that the proportions do not reveal how many transcripts were present originally. Add a pre-mRNA assay to estimate synthesis and a pulse-chase experiment to estimate degradation of the mature isoforms. One group may exhibit a high inclusion fraction simply because the skipping isoform decays rapidly. Learners must also decide how to verify an apparent A-to-I editing site using matched genomic DNA and mapping-quality checks. No single RNA-sequencing track can settle all of these questions. The design rewards appropriate complementary measurements and careful reference annotations rather than sheer sequencing depth.

## 5.1 Pre-mRNA splicing

### Mechanistic foundation

The spliceosome recognizes combinations of splice sites, branch-point features and accessory regulatory elements in many eukaryotic pre-mRNAs. RNA is cut and rejoined so intron sequence is removed and exon sequences become adjacent. Alternative splicing changes which exons or splice junctions appear in a transcript, sometimes changing a protein reading frame or a noncoding RNA property. Isoform annotation depends heavily on sequencing read lengths and tissue context.

### Stepwise reasoning from molecular events to an observation

A useful molecular explanation begins by identifying the actual substrate and product in **pre-mrna splicing**, rather than merely naming a molecule associated with the phenomenon. The starting claim is that the spliceosome recognizes combinations of splice sites, branch-point features and accessory regulatory elements in many eukaryotic pre-mRNAs. In an active cell, production and consumption often occur simultaneously. For pre-mrna splicing, the distinction is especially consequential because isoform annotation depends heavily on sequencing read lengths and tissue context.



### Study design: choosing what to observe

Quantify junction-spanning reads for included and skipped forms while considering read-mapping ambiguity and transcript abundance. Validate representative isoforms using independent RT-PCR or targeted long-read sequencing.

For **pre-mrna splicing**, write down the expected results for three matched conditions: an unperturbed sample, a targeted perturbation of the proposed molecular step, and a rescue that restores function without otherwise changing the assay. A fourth condition should deliberately test an alternative explanation.

### Quantitative thinking without false precision

For pre-mrna splicing, distinguishing the number of molecules from the proportion of molecules in a state is often essential.

Start analysis with the limiting cases of an idealized model. When writing about pre-mrna splicing, state where idealization ends and empirical validation must begin.

### Discriminating causes and ruling out artifacts

Percent-spliced-in is an isoform proportion for the chosen assay and event, not a measure of the total number of transcripts produced at the locus. Build two alternative hypotheses that could mimic the predicted observation.

A meaningful negative result needs equal scrutiny. Establish the dynamic range with positive and negative controls.

### Specific molecular investigation

An experiment finds that 360 reads span an exon-inclusion junction and 240 reads span a skipping junction. The naive junction-derived inclusion estimate is sixty percent. But junction counts may differ in effective mapping probability if isoforms have different sequences or if reads overlap repetitive regions. Validate primer specificity with synthetic templates or known mixtures before comparing tissues. A change in isoform fraction could occur even when total gene transcription does not change; quantify mature RNA abundance independently. If the skipped exon changes frame, examine whether nonsense-mediated decay selectively removes one resulting isoform. Isoform proportion and transcript stability must be interpreted as related but separate phenomena.

## 5.2 RNA editing

### Mechanistic foundation

RNA editing alters specific nucleotides in RNA compared with the DNA template. A-to-I editing by ADAR proteins is a well-studied example in metazoans, where inosine is often interpreted as guanosine during sequencing or translation. Editing can alter coding capacity, splicing, RNA stability or innate immune recognition, depending on locus. Sequence differences between RNA and a reference genome can also result from genomic variants, mapping problems or technical artifacts.

### Stepwise reasoning from molecular events to an observation

A useful molecular explanation begins by identifying the actual substrate and product in **rna editing**, rather than merely naming a molecule associated with the phenomenon. The starting claim is that rNA editing alters specific nucleotides in RNA compared with the DNA template. In an active cell, production and consumption often occur simultaneously. For rna editing, the distinction is especially consequential because sequence differences between RNA and a reference genome can also result from genomic variants, mapping problems or technical artifacts.



### Study design: choosing what to observe

Compare matched DNA and RNA sequencing from the same sample, inspect strand and read quality, and validate a small set of high-confidence sites.

For **rna editing**, write down the expected results for three matched conditions: an unperturbed sample, a targeted perturbation of the proposed molecular step, and a rescue that restores function without otherwise changing the assay. A fourth condition should deliberately test an alternative explanation.

### Quantitative thinking without false precision

For rna editing, distinguishing the number of molecules from the proportion of molecules in a state is often essential.

Start analysis with the limiting cases of an idealized model. When writing about rna editing, state where idealization ends and empirical validation must begin.

### Discriminating causes and ruling out artifacts

Do not label every DNA–RNA mismatch as editing. RNA modifications that affect reverse transcription may create apparent mismatch patterns. Build two alternative hypotheses that could mimic the predicted observation.

A meaningful negative result needs equal scrutiny. Establish the dynamic range with positive and negative controls.

### Specific molecular investigation

RNA sequencing identifies a frequent A-to-G mismatch relative to a reference genome in a transcript that folds into a double-stranded region. A-to-I editing is plausible but not established. First compare matched genomic DNA to rule out a genomic allele. Then assess mapping uniqueness and read orientation to avoid interpreting a duplicated locus or antisense transcript as editing. If ADAR perturbation reduces the candidate signal, sequence and health controls are needed to ensure the effect does not arise indirectly through altered RNA production. The functional consequence could be coding, splicing or RNA-recognition related, so a single mismatch percentage is not enough to infer protein function.

## 5.3 RNA turnover and surveillance

### Mechanistic foundation

RNA lifetimes depend on deadenylation, decapping, exonucleases, endonucleases, RNA-binding proteins and surveillance pathways. Nonsense-mediated decay can reduce some transcripts with premature termination contexts but is not simply a rule that every stop codon triggers degradation. Degradation competes with ongoing transcription, so stable abundance does not imply molecular stability. Different isoforms from one gene may decay at different rates.

### Stepwise reasoning from molecular events to an observation

A useful molecular explanation begins by identifying the actual substrate and product in **rna turnover and surveillance**, rather than merely naming a molecule associated with the phenomenon. The starting claim is that rNA lifetimes depend on deadenylation, decapping, exonucleases, endonucleases, RNA-binding proteins and surveillance pathways. In an active cell, production and consumption often occur simultaneously. For rna turnover and surveillance, the distinction is especially consequential because different isoforms from one gene may decay at different rates.



### Study design: choosing what to observe

Use a carefully controlled transcriptional pulse or metabolic RNA labeling and fit multiple time points. Include spike-ins and cell-number normalization to separate decay from global shifts in RNA recovery.

For **rna turnover and surveillance**, write down the expected results for three matched conditions: an unperturbed sample, a targeted perturbation of the proposed molecular step, and a rescue that restores function without otherwise changing the assay. A fourth condition should deliberately test an alternative explanation.

### Quantitative thinking without false precision

For rna turnover and surveillance, distinguishing the number of molecules from the proportion of molecules in a state is often essential.

Start analysis with the limiting cases of an idealized model. When writing about rna turnover and surveillance, state where idealization ends and empirical validation must begin.

### Discriminating causes and ruling out artifacts

Half-life follows an exponential curve only when a first-order approximation is appropriate; multi-phase decay and changing transcription violate the model. Build two alternative hypotheses that could mimic the predicted observation.

A meaningful negative result needs equal scrutiny. Establish the dynamic range with positive and negative controls.

### Specific molecular investigation

After transcriptional shutoff, an RNA species declines to one-eighth of its starting amount after ten and a half hours. Under a first-order model that implies three elapsed half-lives and an estimated half-life of 3.5 hours. If cellular conditions change during shutoff, the disappearance curve may not represent the unperturbed RNA's native lifetime. Metabolic labeling with pulse-chase and suitable spike-in controls can provide a complementary strategy. A sample may also contain distinct isoforms with different decay rates, producing a non-exponential aggregate. Plot residuals rather than choosing an exponential simply because it yields a convenient numerical half-life.

## 5.4 Noncoding-RNA control

### Mechanistic foundation

MicroRNAs can promote translational repression or transcript destabilization through target-complex interactions; small interfering RNAs and other guide RNAs participate in context-dependent silencing pathways. Long noncoding RNAs have diverse reported associations, but function should be demonstrated at the endogenous locus, avoiding confounding effects from overlap with nearby promoters. RNA localization and binding partner availability shape outcomes.

### Stepwise reasoning from molecular events to an observation

A useful molecular explanation begins by identifying the actual substrate and product in **noncoding-rna control**, rather than merely naming a molecule associated with the phenomenon. The starting claim is that microRNAs can promote translational repression or transcript destabilization through target-complex interactions; small interfering RNAs and other guide RNAs participate in context-dependent silencing pathways. In an active cell, production and consumption often occur simultaneously. For noncoding-rna control, the distinction is especially consequential because rNA localization and binding partner availability shape outcomes.



### Study design: choosing what to observe

Use genetic perturbation and sequence-specific rescue, then measure both target protein and RNA. Include controls for global stress induced by transfection or editing.

For **noncoding-rna control**, write down the expected results for three matched conditions: an unperturbed sample, a targeted perturbation of the proposed molecular step, and a rescue that restores function without otherwise changing the assay. A fourth condition should deliberately test an alternative explanation.

### Quantitative thinking without false precision

For noncoding-rna control, distinguishing the number of molecules from the proportion of molecules in a state is often essential.

Start analysis with the limiting cases of an idealized model. When writing about noncoding-rna control, state where idealization ends and empirical validation must begin.

### Discriminating causes and ruling out artifacts

Sequence complementarity predicts possible interactions, not proof of functional regulation. A reporter may respond differently from a native target in chromatin context. Build two alternative hypotheses that could mimic the predicted observation.

A meaningful negative result needs equal scrutiny. Establish the dynamic range with positive and negative controls.

### Specific molecular investigation

A microRNA perturbation reduces target protein by half while total target RNA decreases only modestly. This pattern is compatible with translational repression but does not prove that direct RNA binding caused the change. A target-site reporter lacking the endogenous 3-prime untranslated region may miss the native regulation, and transfection itself can cause stress responses. Measure nascent protein synthesis, ribosome association and RNA decay in matched conditions; perform a target-site rescue or compensatory-sequence test. Seed matches are widespread, so a computationally predicted target should remain a hypothesis until a defined functional interaction is established.

## Guided molecular investigation

### Evidence integration lab

The aim of this studio is to compare molecular readouts that often have different denominators or experimental biases. Begin with a blinded sample label and a recorded protocol. In the analysis, separate substrate abundance, product abundance, reaction rate, and biological outcome. Use three genuinely independent biological samples per condition as an illustrative minimal planning exercise, while acknowledging that sample-size requirements depend on power, variation and experimental design. The hypothetical study below asks you to predict data patterns rather than pretending the described results have been observed.

### Investigation 5.1: Pre-mRNA splicing and RNA editing

A lab attempts to connect pre-mrna splicing to rna editing using a shared perturbation. The first obligation is to keep the prediction narrow. The spliceosome recognizes combinations of splice sites, branch-point features and accessory regulatory elements in many eukaryotic pre-mRNAs. RNA is cut and rejoined so intron sequence is removed and exon sequences become adjacent. Alternative splicing changes which exons or splice junctions appear in a transcript, sometimes changing a protein reading frame or a noncoding RNA property. Isoform annotation depends heavily on sequencing read lengths and tissue context. The connected response should be measured separately because RNA editing alters specific nucleotides in RNA compared with the DNA template. A-to-I editing by ADAR proteins is a well-studied example in metazoans, where inosine is often interpreted as guanosine during sequencing or translation. Editing can alter coding capacity, splicing, RNA stability or innate immune recognition, depending on locus. Sequence differences between RNA and a reference genome can also result from genomic variants, mapping problems or technical artifacts. A single terminal measurement cannot determine whether the perturbation changed upstream material, a rate-limiting processing step, or sample survival. The study therefore predefines an early molecular observation and a late functional output, with an explicit normalization rule for each.

The proposed primary assay follows this plan: Quantify junction-spanning reads for included and skipped forms while considering read-mapping ambiguity and transcript abundance. Validate representative isoforms using independent RT-PCR or targeted long-read sequencing. An orthogonal procedure addresses the downstream question: Compare matched DNA and RNA sequencing from the same sample, inspect strand and read quality, and validate a small set of high-confidence sites. Its independent readout should not reuse the same molecular normalization error. Include a negative treatment, a validated positive comparison if available, and a material-balance or integrity control. When analyzing a gene perturbation, record allele or construct verification separately from RNA abundance and protein abundance. That prevents the convenient but unsupported inference that a verified DNA change automatically changed function.

For the interpretation, construct a table with rows for no change, increased upstream signal only, changed downstream signal only, and concordant changes in both. State at least two plausible mechanisms for each nonzero pattern. The most serious limitation may involve rna turnover and surveillance: Half-life follows an exponential curve only when a first-order approximation is appropriate; multi-phase decay and changing transcription violate the model. A satisfactory report includes the type of observation that would falsify the chosen mechanism, the magnitude of technical uncertainty, and an explanation of which conclusions are about a model versus observed living cells. The outcome is a proposed experimental logic, not a claim that biological data were collected.

## Fully worked questions

All numerical inputs are constructed teaching examples. Where a model is conditional, that condition is part of the solution.

### Problem 1: Alternative splicing fraction

Junction counts are 360 inclusion-supporting and 240 skipping-supporting reads after a validated junction-counting workflow. Calculate percent spliced in (PSI).

**Worked reasoning**

1. PSI≈360/(360+240)=360/600=0.60, or 60%.
2. This simple estimator assumes comparable mapping and sampling for both junction classes.
3. Compare biological replicates and use transcript-specific methods where isoforms or junction lengths introduce bias.

### Problem 2: RNA half-life

An RNA population has an experimentally justified first-order half-life of 3.5 h. What fraction remains after 10.5 h with synthesis blocked?

**Worked reasoning**

1. Ten and a half hours represent exactly three half-lives.
2. Remaining proportion =2^(−10.5/3.5)=2^(−3)=0.125 or 12.5%.
3. The model assumes no new synthesis and constant clearance rate; measured fluorescence alone could change for other reasons.

### Problem 3: Isoform normalization

A transcript rises from 50 to 90 normalized counts after perturbation, while total library scaling differs by a factor 1.2. What is the scaling-corrected fold change using 90/1.2?

**Worked reasoning**

1. Divide the second condition count by its scaling factor: 90/1.2=75.
2. Corrected fold =75/50=1.5.
3. The uncorrected fold would have been 1.8.
4. This toy computation does not replace robust library normalization and biological replicate analysis.

## Simulations and assumptions

The two simulation cards below are local, offline-capable numerical thought experiments. They are parameterized formula demonstrations, not mechanistic claims about a real cell type. Inspect the stated assumptions first, then vary an input, compare limiting cases and reset the model to its default.

### Model focus: Splice-junction inclusion

A simplified percent-spliced-in estimate is 100I/(I+S), where I and S are usable reads supporting inclusion and skipping of a particular exon event. The simulation treats both classes as comparable and nonnegative, with the skipping count constrained above zero so the denominator cannot vanish. Three hundred sixty inclusion reads and two hundred forty skipping reads yield sixty percent. Doubling both counts leaves the estimate unchanged but increases the available sampling information. If two isoforms have different mappability or a third isoform is omitted, the estimate may be biased even with many reads. Use junction-aware alignments and validate selected events with isoform-specific assays. This fraction is not the same as the number of RNA molecules expressed from the gene.

### Model application and sensitivity test

Construct two hypothetical junction-count datasets: sample A has 360 inclusion and 240 skipping reads; sample B has 36 inclusion and 24 skipping reads. Both yield sixty percent PSI, but sample B provides much less information about sampling variation. If true junction detection probabilities are unequal, simple scaling of counts does not correct the bias. Add an illustrative case in which the inclusion isoform has a segment that cannot be uniquely mapped. The observed inclusion count may be systematically low even at deep sequencing coverage. Model a synthetic mixture with a known isoform proportion and quantify the estimator bias before evaluating unknown samples. Biological interpretation should consider whether included and skipped isoforms share the same stability. An increase in PSI can accompany no change, an increase or a decrease in total gene expression. Plot PSI together with absolute or carefully normalized RNA abundance for a more complete account.

### Model focus: RNA first-order half-life

First-order RNA decay uses M(t)/M0=2^(−t/h), where h is the half-life in hours. This is equivalent to exp[−ln(2)t/h]. When t=h, the value is fifty percent; after three half-lives, twelve and a half percent remains. At t=0, every permitted h gives a normalized value of one hundred percent. Changing the half-life parameter stretches or contracts the time axis but does not by itself specify the RNA-production rate. A biological experiment must distinguish molecular degradation from dilution by cell division, incomplete synthesis inhibition and isoform mixtures. If measured residuals do not follow one exponential, fitting a single half-life may conceal several processes rather than provide a universal molecular property.

### Model application and sensitivity test

A single half-life is not sufficient to describe an RNA population when it contains two kinetic subgroups. Suppose half the molecules have a half-life of one hour and half a half-life of six hours. The combined residual at time t is 0.5×2^(−t/1)+0.5×2^(−t/6), which is not itself a single exponential. Compare this mixture against a uniform three-and-a-half-hour model at one, four and twelve hours. Early and late differences will reveal why a one-parameter fit can obscure molecular heterogeneity. RNA labels may also be recycled or imperfectly chased, and cell division dilutes intracellular molecules even if no chemical degradation takes place. For an assay design, collect several time points spanning more than one expected half-life and use independently measured cell growth to assess dilution. Avoid inferring degradation mechanisms directly from the shape of one uncalibrated fluorescence curve.
