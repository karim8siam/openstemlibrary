# Unit 8: Molecular methods

## Unit overview

Molecular methods transform mechanisms into experimentally testable propositions, but the test method itself can introduce artifacts. Construct sequencing verifies a design but not protein function; PCR can amplify trace contamination; sequencing depth does not guarantee even coverage; gene editing may create mixtures of alleles. The aim here is to assemble methods into a chain of corroboration. Every quantitative result should have a denominator, assumptions and a quality-control record. The final skill is deciding when a causal claim requires a functional rescue or orthogonal assay rather than another measurement with the same source of error.

## Learning goals

Understand the causal molecular sequence for four named processes; derive and interpret simplified quantitative statements; identify measurement controls; separate experimental observation from molecular inference; and explain the limits of the idealized simulation models.

## Unit synthesis

A reliable molecular workflow begins with a specific causal question, not with whichever sequencing or amplification platform is easiest to obtain. A verified plasmid insert establishes molecular identity; it does not establish expression. A fluorescent reporter confirms signal in the assay; it does not establish target specificity. An amplification threshold measures a reaction in a defined linear range; it does not directly establish initial molecule count unless efficiency and controls are credible. A sequencing variant call requires mapping, base quality and independent validation. A knockout phenotype needs independent alleles or guides and ideally a rescue. When planning the final project, record all intermediate controls as a chain: intended construct, molecular expression, target engagement, measured biochemical process and final phenotype. Each link should be inspectable separately so a failure can be located rather than disguised in the conclusion.

## Unit-specific integrated assessment

The final molecular-methods assessment is a chain of evidence for a proposed loss-of-function edit. Start with an intended guide sequence and require construct verification. Proceed to a DNA-level assessment of the edited allele distribution, a transcript-level test, a protein-level test and a cellular phenotype. A plausible result may show abundant edited reads with modest phenotype; students should consider mosaicism, copy number, residual protein and compensatory regulation. Add qPCR for the transcript and require a positive amplification control, a negative template control and appropriate normalization. Conclude with a sequencing dataset whose mean coverage is high but whose critical locus lies in a poorly mapped repeat. A valid final claim acknowledges that the global coverage estimate does not guarantee an accurate variant call. The exercise is finished only when one independent rescue or orthogonal method has been proposed.

## 8.1 Cloning and construct verification

### Mechanistic foundation

A DNA construct combines one or more fragments with a vector backbone using suitable assembly chemistry. Restriction–ligation, recombination-based assembly and overlap-based methods have different sequence constraints and verification needs. Orientation, frame and regulatory context determine whether a cloned coding region can produce the intended transcript and protein. A correct colony phenotype is insufficient evidence that every junction and insert sequence is correct.

### Stepwise reasoning from molecular events to an observation

A useful molecular explanation begins by identifying the actual substrate and product in **cloning and construct verification**, rather than merely naming a molecule associated with the phenomenon. The starting claim is that a DNA construct combines one or more fragments with a vector backbone using suitable assembly chemistry. In an active cell, production and consumption often occur simultaneously. For cloning and construct verification, the distinction is especially consequential because a correct colony phenotype is insufficient evidence that every junction and insert sequence is correct.



### Study design: choosing what to observe

Plan junction primers and verify the full relevant insert with sequencing, not only a single restriction digest. Use a no-insert control to estimate vector background.

For **cloning and construct verification**, write down the expected results for three matched conditions: an unperturbed sample, a targeted perturbation of the proposed molecular step, and a rescue that restores function without otherwise changing the assay. A fourth condition should deliberately test an alternative explanation.

### Quantitative thinking without false precision

For cloning and construct verification, distinguishing the number of molecules from the proportion of molecules in a state is often essential.

Start analysis with the limiting cases of an idealized model. When writing about cloning and construct verification, state where idealization ends and empirical validation must begin.

### Discriminating causes and ruling out artifacts

Cloning success does not prove that the encoded protein folds, localizes or functions in the host. A correct sequence is a necessary but not universally sufficient check. Build two alternative hypotheses that could mimic the predicted observation.

A meaningful negative result needs equal scrutiny. Establish the dynamic range with positive and negative controls.

### Specific molecular investigation

An assembled vector contains the expected insert length when checked by restriction digest but produces no detectable protein. The digest cannot exclude a point mutation, wrong reading frame, promoter loss or an altered junction. Sequence the entire critical expression cassette, verify transcription and examine the expected subcellular localization. A negative protein signal may instead reflect antibody failure or rapid degradation. Including a positive-control construct and a tag-independent assay can discriminate these possibilities. A restriction-site map is a valuable design check, not a substitute for verifying sequence identity and functional expression.

## 8.2 PCR and quantitative amplification

### Mechanistic foundation

Polymerase chain reaction repeatedly uses denaturation, primer annealing and extension to generate copies of a defined region. In an idealized model the number of amplifiable templates multiplies by (1+E) each cycle, with efficiency E between zero and one; real reactions plateau as reagents become limiting and inhibition increases. Quantitative PCR requires reliable baseline treatment, amplification efficiency and reference normalization.

### Stepwise reasoning from molecular events to an observation

A useful molecular explanation begins by identifying the actual substrate and product in **pcr and quantitative amplification**, rather than merely naming a molecule associated with the phenomenon. The starting claim is that polymerase chain reaction repeatedly uses denaturation, primer annealing and extension to generate copies of a defined region. In an active cell, production and consumption often occur simultaneously. For pcr and quantitative amplification, the distinction is especially consequential because quantitative PCR requires reliable baseline treatment, amplification efficiency and reference normalization.



### Study design: choosing what to observe

Use serial-dilution standards and no-template controls. Compare primer sets for efficiency and inspect melt curves or product sequences for specificity.

For **pcr and quantitative amplification**, write down the expected results for three matched conditions: an unperturbed sample, a targeted perturbation of the proposed molecular step, and a rescue that restores function without otherwise changing the assay. A fourth condition should deliberately test an alternative explanation.

### Quantitative thinking without false precision

For pcr and quantitative amplification, distinguishing the number of molecules from the proportion of molecules in a state is often essential.

Start analysis with the limiting cases of an idealized model. When writing about pcr and quantitative amplification, state where idealization ends and empirical validation must begin.

### Discriminating causes and ruling out artifacts

A final fluorescence value is not inherently proportional to initial molecules once a reaction saturates; amplification curves must be interpreted in a validated dynamic range. Build two alternative hypotheses that could mimic the predicted observation.

A meaningful negative result needs equal scrutiny. Establish the dynamic range with positive and negative controls.

### Specific molecular investigation

A qPCR standard curve looks linear across early dilutions but deviates at high template abundance. If a naive analyst uses endpoint fluorescence to infer starting copy number, reaction saturation produces biased estimates. Fit amplification efficiencies within a validated range, test for primer dimers and include no-template controls. In the ideal model ten starting molecules with 85% efficiency for twenty cycles yield tens of millions of modeled copies, but a physical PCR reaction cannot remain exponential indefinitely. Report the instrument threshold and analysis method so different batches can be compared. A low Ct value is not automatically a direct measure of biologically active protein.

## 8.3 DNA and RNA sequencing

### Mechanistic foundation

Read sequencing samples molecules through platform-dependent chemistry and computational processing. Depth and coverage describe different properties: mean coverage is the total sequenced aligned bases divided by reference size, while fraction of the genome sufficiently observed depends on uneven sampling, repeats and mappability. RNA sequencing counts are shaped by transcription, turnover, library preparation and normalization.

### Stepwise reasoning from molecular events to an observation

A useful molecular explanation begins by identifying the actual substrate and product in **dna and rna sequencing**, rather than merely naming a molecule associated with the phenomenon. The starting claim is that read sequencing samples molecules through platform-dependent chemistry and computational processing. In an active cell, production and consumption often occur simultaneously. For dna and rna sequencing, the distinction is especially consequential because rNA sequencing counts are shaped by transcription, turnover, library preparation and normalization.



### Study design: choosing what to observe

Track per-base coverage, mapping quality, strandedness, duplicate fraction, and biological replicates. Verify critical variants with an orthogonal assay and report reference assembly version.

For **dna and rna sequencing**, write down the expected results for three matched conditions: an unperturbed sample, a targeted perturbation of the proposed molecular step, and a rescue that restores function without otherwise changing the assay. A fourth condition should deliberately test an alternative explanation.

### Quantitative thinking without false precision

For dna and rna sequencing, distinguishing the number of molecules from the proportion of molecules in a state is often essential.

Start analysis with the limiting cases of an idealized model. When writing about dna and rna sequencing, state where idealization ends and empirical validation must begin.

### Discriminating causes and ruling out artifacts

Thirtyfold mean coverage does not guarantee every base has thirty reads; under ideal Poisson sampling some sites will still be unobserved. Build two alternative hypotheses that could mimic the predicted observation.

A meaningful negative result needs equal scrutiny. Establish the dynamic range with positive and negative controls.

### Specific molecular investigation

A genomic assay reports fiftyfold mean coverage of a five-megabase reference. Even under uniform independent sampling, a mean is a distribution parameter rather than a promise of fifty reads at each site. Repeats, GC bias, duplicated library molecules and mapping quality create departures from the ideal Poisson model. Examine a per-position coverage histogram and proportion of high-confidence callable sites, especially near structural variants. RNA sequencing introduces another layer: measured counts vary with transcript length and abundance and must not be read as genomic copy number. Use independent replicates to distinguish expression changes from library construction effects.

## 8.4 Gene perturbation and causal tests

### Mechanistic foundation

Gene knockouts, targeted edits, RNA interference and programmable repression perturb gene activity at different stages. Off-target effects, mosaicism, compensation and selection can create misleading phenotypes. Rescue with a suitably resistant or corrected construct can strengthen an attribution, as can independent guide RNAs or genetic alleles. A strong phenotype may reflect loss of viability rather than a specific pathway.

### Stepwise reasoning from molecular events to an observation

A useful molecular explanation begins by identifying the actual substrate and product in **gene perturbation and causal tests**, rather than merely naming a molecule associated with the phenomenon. The starting claim is that gene knockouts, targeted edits, RNA interference and programmable repression perturb gene activity at different stages. In an active cell, production and consumption often occur simultaneously. For gene perturbation and causal tests, the distinction is especially consequential because a strong phenotype may reflect loss of viability rather than a specific pathway.



### Study design: choosing what to observe

Compare independent targeting guides, a non-targeting control and a validated rescue, then measure DNA edit state, RNA, protein and phenotype as appropriate.

For **gene perturbation and causal tests**, write down the expected results for three matched conditions: an unperturbed sample, a targeted perturbation of the proposed molecular step, and a rescue that restores function without otherwise changing the assay. A fourth condition should deliberately test an alternative explanation.

### Quantitative thinking without false precision

For gene perturbation and causal tests, distinguishing the number of molecules from the proportion of molecules in a state is often essential.

Start analysis with the limiting cases of an idealized model. When writing about gene perturbation and causal tests, state where idealization ends and empirical validation must begin.

### Discriminating causes and ruling out artifacts

Changing one gene is not always equivalent to changing one molecular mechanism. Pleiotropy and adaptation require cautious causal language. Build two alternative hypotheses that could mimic the predicted observation.

A meaningful negative result needs equal scrutiny. Establish the dynamic range with positive and negative controls.

### Specific molecular investigation

An editing assay finds 55% of sequenced molecules carry an intended nucleotide change, yet only 20% of cells show an altered phenotype. This need not be contradictory: some cells have different allele copy numbers, a threshold may be required for function, or edited cells may express protein made before editing. Amplicon fractions do not directly report the fraction of fully edited cells. Measure allele distribution in single cells, protein turnover and the phenotype over time, with multiple independent guide RNAs and a rescue construct. The strongest interpretation preserves distinctions among edit fraction, cell fraction, and functional impact.

## Guided molecular investigation

### Evidence integration lab

The aim of this studio is to compare molecular readouts that often have different denominators or experimental biases. Begin with a blinded sample label and a recorded protocol. In the analysis, separate substrate abundance, product abundance, reaction rate, and biological outcome. Use three genuinely independent biological samples per condition as an illustrative minimal planning exercise, while acknowledging that sample-size requirements depend on power, variation and experimental design. The hypothetical study below asks you to predict data patterns rather than pretending the described results have been observed.

### Investigation 8.1: Cloning and construct verification and PCR and quantitative amplification

A lab attempts to connect cloning and construct verification to pcr and quantitative amplification using a shared perturbation. The first obligation is to keep the prediction narrow. A DNA construct combines one or more fragments with a vector backbone using suitable assembly chemistry. Restriction–ligation, recombination-based assembly and overlap-based methods have different sequence constraints and verification needs. Orientation, frame and regulatory context determine whether a cloned coding region can produce the intended transcript and protein. A correct colony phenotype is insufficient evidence that every junction and insert sequence is correct. The connected response should be measured separately because Polymerase chain reaction repeatedly uses denaturation, primer annealing and extension to generate copies of a defined region. In an idealized model the number of amplifiable templates multiplies by (1+E) each cycle, with efficiency E between zero and one; real reactions plateau as reagents become limiting and inhibition increases. Quantitative PCR requires reliable baseline treatment, amplification efficiency and reference normalization. A single terminal measurement cannot determine whether the perturbation changed upstream material, a rate-limiting processing step, or sample survival. The study therefore predefines an early molecular observation and a late functional output, with an explicit normalization rule for each.

The proposed primary assay follows this plan: Plan junction primers and verify the full relevant insert with sequencing, not only a single restriction digest. Use a no-insert control to estimate vector background. An orthogonal procedure addresses the downstream question: Use serial-dilution standards and no-template controls. Compare primer sets for efficiency and inspect melt curves or product sequences for specificity. Its independent readout should not reuse the same molecular normalization error. Include a negative treatment, a validated positive comparison if available, and a material-balance or integrity control. When analyzing a gene perturbation, record allele or construct verification separately from RNA abundance and protein abundance. That prevents the convenient but unsupported inference that a verified DNA change automatically changed function.

For the interpretation, construct a table with rows for no change, increased upstream signal only, changed downstream signal only, and concordant changes in both. State at least two plausible mechanisms for each nonzero pattern. The most serious limitation may involve dna and rna sequencing: Thirtyfold mean coverage does not guarantee every base has thirty reads; under ideal Poisson sampling some sites will still be unobserved. A satisfactory report includes the type of observation that would falsify the chosen mechanism, the magnitude of technical uncertainty, and an explanation of which conclusions are about a model versus observed living cells. The outcome is a proposed experimental logic, not a claim that biological data were collected.

## Fully worked questions

All numerical inputs are constructed teaching examples. Where a model is conditional, that condition is part of the solution.

### Problem 1: PCR amplification

A reaction starts with 100 target molecules, holds per-cycle amplification efficiency E=0.85 and completes 20 ideal cycles. Estimate modeled copies.

**Worked reasoning**

1. Ideal count N=N0(1+E)^n=100×1.85^20≈2.215×10^7 molecules.
2. This is only an unsaturated amplification model, not a prediction of endpoint yield; a real PCR approaches a plateau and different molecule species may amplify at different rates.
3. Check the numerical units and domain against the quantity in pcr amplification; interpret the result only under the assumptions stated in the question.

### Problem 2: Sequencing depth

A study sequences 2 million mapped reads of mean length 125 bp from a 5 million bp target reference. Estimate mean depth.

**Worked reasoning**

1. Total sequenced bases=2×10^6×125=250×10^6 bases.
2. Mean nominal depth=250×10^6/(5×10^6)=50×.
3. Uneven coverage, mapping ambiguity and duplicate molecules mean this average is not the minimum depth across the target.

### Problem 3: CRISPR-editing event fraction

In a validated amplicon assay, 550 of 1000 usable independent molecules carry the intended edit. Compute the observed edit fraction and a simple SE.

**Worked reasoning**

1. Observed edit fraction=550/1000=0.55 or 55%.
2. Independent-binomial SE=sqrt[0.55×0.45/1000]≈0.0157, or 1.57 percentage points.
3. This statistical model does not account for PCR duplication, allele dropout, mosaicism or site-specific sequencing bias.

## Simulations and assumptions

The two simulation cards below are local, offline-capable numerical thought experiments. They are parameterized formula demonstrations, not mechanistic claims about a real cell type. Inspect the stated assumptions first, then vary an input, compare limiting cases and reset the model to its default.

### Model focus: Ideal PCR amplification

An ideal PCR amplification model begins with N0 target molecules and multiplies the number of amplifiable templates by 1+E each cycle: Nn=N0(1+E)^n, where E is per-cycle efficiency between zero and one. The interface fixes N0 at ten. With twenty cycles and E=0.85 the model predicts roughly 2.2 million copies from ten starting molecules; increasing efficiency or cycle count changes the prediction exponentially. No real experiment can sustain unrestricted multiplication: reagents, products and polymerase activity impose a plateau, while primer dimers and nonspecific products may distort fluorescence. A dilution-series standard curve and no-template controls are necessary to interpret quantitative PCR measurements. Treat the simulation as a derivation of early exponential behavior only.

### Model application and sensitivity test

PCR efficiency is best interpreted through fold amplification and its sensitivity to cycle number. At eighty-five-percent per-cycle efficiency, one cycle multiplies the ideal template number by 1.85; ten cycles multiply it by about 469, and twenty cycles by approximately 220,000. A small efficiency difference compounded over many cycles can change the inferred starting amount substantially. In quantitative PCR, an unknown threshold cycle is therefore not directly comparable between primer pairs without validated efficiency. Make a dilution series that spans the intended dynamic range and inspect the relationship between log starting quantity and threshold cycle. A no-template control tests contamination, while a melt curve or product sequencing examines specificity. A late fluorescent signal may result from primer dimers rather than a small initial target population. The model's explosive upper range is deliberately an illustration of why endpoint fluorescence cannot be used as an unrestricted counting device.

### Model focus: Nominal sequence-read coverage

Nominal mean sequencing depth equals total aligned sequenced bases divided by reference length. For a five-megabase reference and R million mapped reads of length l base pairs, the model simplifies to C=Rl/5. With two million 125-base reads, nominal mean depth is fiftyfold. This does not guarantee fiftyfold coverage at a particular base: library duplicates, variable GC content, mapping ambiguities and alignment filters generate uneven distribution. Mean depth also differs from the percentage of positions meeting a chosen callable-depth threshold. A genome analysis should show coverage distributions, fraction of uniquely mapped reads and sequence-quality measures; an RNA experiment additionally requires accounting for transcript expression and effective length.

### Model application and sensitivity test

At a nominal mean depth of fiftyfold, an ideal Poisson sampling model would predict a very small fraction of completely unobserved positions, approximately exp(−50). However, real sequencing includes nonrandom read distribution, genomic repeats and mapping filters. Therefore a fiftyfold global mean does not justify the ideal Poisson assumption for every locus. Compare libraries with the same total sequenced bases but different read lengths, duplicates and mapping outcomes. A longer read can span repeated sequence and improve unique placement even when the nominal base-count depth is held constant. For variant analysis, report callable target fraction above a chosen quality and depth threshold, not only arithmetic mean depth. For expression measurements, transcript-specific abundance, effective length and library composition become part of the denominator. A trustworthy summary states whether its depth refers to raw reads, mapped bases or unique molecules.
