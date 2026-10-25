# Unit 4: Microbial Genetics and Evolution

A microbial genome stores heritable information while remaining embedded in a changing ecological context. Mutation creates new genetic variation, recombination rearranges existing variation, and some microbial lineages exchange genetic material through mechanisms not captured by parent-to-offspring inheritance alone. Gene expression then mediates how genetic potential becomes a conditional phenotype. This unit develops the conceptual distinctions needed to understand evolution and regulation without using procedural recipes for constructing or enhancing organisms. Mathematical examples address probability, selection and interpretation; practical manipulation of biological material belongs under institutionally reviewed biosafety procedures.

## 4.1 Mutation, DNA maintenance and population variation

A mutation is a change in nucleic-acid sequence or organization that becomes part of the genetic information of a cell lineage. The effects range from negligible to severe and can depend on environment. Mutations may affect protein coding, gene regulation, mobile elements or chromosomal structure. Calling every mutation 'damage' is imprecise: DNA damage can be chemically repaired without becoming a fixed sequence change, and a mutation can persist even when no ongoing molecular damage remains. The probability of a mutation is different from the probability that the mutation changes observable function.

Replication accuracy depends on nucleotide selection, polymerase-associated proofreading in some systems and downstream repair mechanisms. DNA can also undergo chemical changes independent of replication. Repair pathways recognize certain classes of lesions and restore information using cellular templates or chemistry appropriate to the damage. No repair process is perfect, and the outcome varies with the lesion, genetic background and physiological state. Explaining a molecular mechanism requires naming the intermediate and the evidence for it, rather than presenting an undifferentiated concept of 'DNA repair.'

Mutation rates are generally stated per genetic target per replication or generation, not simply per hour without context. If the expected number of independently occurring events is λ, a Poisson model gives P(0)=e^(−λ) and P(at least one)=1−e^(−λ). With λ=1, the latter is about 63.2%, not 100%. This calculation is useful for translating an expectation into a probability. It does not predict the distribution of benefits, the appearance of a particular phenotype or the outcome of evolutionary selection. Real mutation counts can deviate from Poisson assumptions because lineages share ancestry and biological rates vary.

Selection acts on heritable differences in reproductive success under specified conditions. A neutral change may drift in frequency; a beneficial change may still disappear by chance when populations are finite. The observation that a particular genotype becomes common does not by itself identify whether selection, drift, migration or sampling occurred. Time-series data, replicates and relevant ecological information strengthen inference. In microbial systems, large populations and rapid reproduction can make evolutionary change observable over relatively short time scales, but methodological simplicity should not be confused with mechanistic certainty.

A rigorous analysis separates the origin of variation from its subsequent filtering. Mutation processes determine which changes arise and how frequently; selection and demographic events influence which survive and increase. A phenotype observed in a later population should not be retroactively treated as the purpose of an earlier mutation. Evolution has no foresight. The adaptive interpretation of a genetic change must be supported by a documented difference in performance under the relevant conditions, not only by an appealing biological story.

## 4.2 Plasmids, conjugation and mobile genetic context

A plasmid is a replicating DNA element distinct from the principal chromosomal replicon in many microbial systems, although plasmid diversity is broad. Some carry genes affecting metabolism, environmental interactions or maintenance of the DNA element itself. Plasmid presence is not a guarantee of a particular phenotype; expression may be conditional, the sequence may be defective, and copy number can vary. Chromosomal and extrachromosomal DNA also interact through recombination and regulatory networks. When interpreting genomic data, researchers must determine whether an assembled sequence genuinely belongs to a plasmid or reflects a computational reconstruction error.

Conjugation is one mechanism of horizontal genetic exchange in which genetic material can move between cells through coordinated contact-dependent processes. Its molecular machinery and host range differ among systems. Understanding the existence of this mechanism does not require a laboratory transfer protocol. The educational point is that genealogy for one gene can differ from genealogy for the core genome. A trait can spread through a community without the whole cellular lineage increasing at the same rate, complicating the use of one species tree to explain every genetic character.

Mobile elements impose both benefits and costs. A new metabolic function may allow access to a resource in a specific habitat, but maintaining and expressing additional DNA can consume resources or alter regulation. Genetic elements may persist because they help the host, because they have their own maintenance mechanisms, or because population structure enables repeated transmission. Predicting stability requires specifying the environment and the mechanism. It is erroneous to assume that a transferred gene is always advantageous or will spread unopposed through any microbial community.

A conceptual frequency model illustrates one simplified selective effect. Suppose genotype A begins at frequency p=0.3 and has relative reproductive output 1+s compared with an alternative of output 1. After deterministic proportional reproduction, p′=p(1+s)/(p(1+s)+1−p). If s=0.1, then p′=0.33/1.03≈0.3204. The calculation assumes no horizontal transfer, mutation, drift or ecological feedback. A real plasmid-bearing population may violate nearly all of these conditions. The model is useful because it makes the consequences of a small frequency advantage explicit, and its limitations are readily identifiable.

Interpreting gene transfer in an environmental sample also involves measurement uncertainty. Detection of two genes in pooled DNA does not establish that they resided in the same cell. Detection of a mobile-element signature does not establish that an exchange event occurred during sampling. Genomic linkage, single-cell observations or carefully validated longitudinal evidence can support stronger statements. Responsible microbiology reports genetic association and possible mobility without implying an unobserved transfer event as established fact.

## 4.3 Transformation, transduction and tangled gene histories

Transformation describes the uptake and potential incorporation of extracellular genetic material by some cells under suitable biological circumstances. Transduction describes genetic transfer mediated by viruses that infect microorganisms. Both differ from conjugation in the physical form of the transfer process. Their existence demonstrates that inheritance need not be strictly vertical, but their outcomes depend on cellular physiology, sequence compatibility, ecological contact and other barriers. A textbook should emphasize the conceptual architecture and ecological significance rather than provide actionable steps for performing transfers.

Extracellular DNA can originate from diverse sources, including cells that have released genetic material. The presence of DNA outside cells does not ensure that the DNA remains intact, enters another cell or contributes to inheritance. Detection methods can find fragments long after the associated cells have stopped growing. Viral particles likewise have life histories that affect whether genetic transfer is possible, and the capacity for transfer varies across virus–host systems. A phylogenetic discrepancy between genes can motivate an HGT hypothesis, but differences may also arise from recombination, rate heterogeneity, contamination or limitations of tree inference.

To reason about conflicting gene trees, imagine two genetic markers sampled from the same set of microbial isolates. One marker groups isolates by their core genome, while a second groups them by a shared metabolic island. This discrepancy can indicate a different history for the island. Before asserting horizontal transfer, an investigator checks alignment quality, gene orthology, possible duplicated genes and support for the alternative branchings. The final claim can be graded: 'consistent with transfer' is weaker than 'supported by multiple independent lines of evidence.' Scientific precision depends on using those qualifiers deliberately.

Gene flow affects how microbial species boundaries are understood. Some populations exchange many genes within ecological networks, while others are more isolated. Recombination can homogenize parts of genomes yet leave adaptive differences at particular loci. Different genes may trace different genealogies, so a single bifurcating tree is sometimes insufficient to represent all relationships. Network diagrams can capture some reticulate histories but introduce their own visualization choices. The most informative representation is the one that corresponds to the question and the data quality, not automatically the most complex diagram available.

These concepts also connect evolution to public interpretation. A detected gene with a familiar label does not automatically convey a measured risk or guarantee that a trait will be expressed. Host background, regulation and environmental exposure all intervene between sequence and phenotype. Responsible genomic surveillance separates detection, confirmation, phenotypic evidence and actual ecological or public-health significance. Oversimplified claims of transfer can mislead just as much as claims that microbes never exchange genetic material.

## 4.4 Regulation, tradeoffs and inference from genotype to phenotype

Gene regulation allows cells to alter the amount and timing of molecular products in response to internal and external cues. Control can occur through transcription initiation, RNA stability, translation, protein modification or degradation. A regulator can respond to a metabolite, a physical condition or another signal, producing changes in pathway expression. Networks often contain feedback and multiple inputs, so a single external stimulus does not always determine a single response. The distinction between gene presence and expression is especially important when interpreting environmental sequence surveys.

A metabolic pathway may be useful only when its substrate is available. Constitutive expression of all its enzymes could waste resources, while a regulated response requires sensing and may impose a delay. The balance depends on resource variability and energetic cost. Biological systems can show anticipatory or history-dependent behavior, but such interpretations require evidence of regulatory dynamics rather than anthropomorphic descriptions of microbes as making deliberate plans. Terms such as 'decision' can be pedagogical shorthand only if the molecular meaning is explained.

A reporter signal is a proxy for a molecular process, and proxy interpretation requires calibration. Fluorescence, for example, can depend on protein maturation, oxygen availability, optical geometry and cellular growth. An apparent change in reporter intensity might reflect altered expression, protein stability or cell size. Suitable controls would distinguish those possibilities while respecting institutional biosafety practice. Mathematical normalization is not a substitute for verifying the origin of a measured signal. The most useful quantitative output may be a fold change with confidence intervals and control measurements rather than a visually dramatic color difference.

The simple deterministic selection equation used in this unit captures one component of genotype-frequency change, but real regulated phenotypes can modify the selection coefficient itself. A trait can be costly in one environment and beneficial in another, causing temporal fluctuations. Frequency-dependent interactions further complicate the picture: one type may perform better only when rare or when another type produces a shared resource. Such examples show why evolutionary predictions require explicit statements about environment and population structure.

A genome annotation is therefore a starting map, not a finished explanation. To argue that a particular genetic feature causes a process, evidence must connect sequence, expression, biochemical function and the resulting cellular or ecological outcome. Where direct measurements are absent, alternative interpretations should remain visible. A scientist can be confident that a sequence is present while remaining uncertain about its current activity. This separation of evidence levels is among the most transferable skills in microbial genetics.


## Guided investigation A: Separating mutation, selection and sampling noise

An investigator compares genotype frequencies in an abstract microbial population across two times. The frequency of type A changes from 0.30 to 0.34. It would be tempting to infer that type A evolved because of a particular adaptive advantage. Yet a change in frequency is a result, not a mechanism. Three broad explanations require consideration: differences in reproductive success, random demographic fluctuations and movement or exchange of genetic material. Mutation may also introduce new variation. In a finite population, even neutral genetic variants can change frequency substantially by chance, particularly under small effective population sizes or bottlenecks.

Start with a deterministic reference model. Assign type A relative fitness 1+s and type B fitness 1, so p′=p(1+s)/(p(1+s)+(1−p)). For p=0.30 and s=0.10, the predicted next frequency is approximately 0.3204. This does not exactly match 0.34. One possible conclusion is that the assumed relative advantage was different; another is that multiple evolutionary processes occurred. The model cannot uniquely infer a selection coefficient from one pair of noisy measurements. If the study sampled only 100 cells at each time, binomial sampling uncertainty alone might explain an appreciable fraction of the observed change.

Evidence about mutation origin requires another distinction. A variant appearing at a later time need not have arisen during the observed interval: it might have been present earlier below detection or introduced from another population. Genetic mutations do not occur because an organism anticipates future environmental needs. A later increase in the frequency of a mutation under a new condition reflects filtering of variants; it does not prove that a directed adaptive mutation happened in response to the challenge. Time-resolved sequence sampling and appropriate neutral comparisons can improve inference, but every claim must remain proportionate to the design.

The observation may also mix organism-level and gene-level histories. A mobile genetic element can change frequency independently of the full host lineage, while ecological sorting changes which lineages are sampled. An apparent increase in a marker gene could arise from expansion of carriers, movement of the genetic element or analytical variation in marker recovery. Without linking the marker to genomic backgrounds, these explanations may be indistinguishable. A sequencing signal alone is not a measurement of transmission events or adaptive value.

The strongest conclusion from the hypothetical example is narrow: the measured sample proportion increased. A mechanistic account requires more observations, explicit demographic assumptions and independent evidence. Students learn to use models as rival explanations rather than to retrofit one favored causal story to every curve that slopes upward.

## Guided investigation B: Interpreting conflicting genomic evidence

A hypothetical genome analysis places three isolates close together according to multiple conserved genes, while a metabolic gene clusters one isolate with a distant environmental group. The discrepancy is consistent with several histories. A horizontally acquired gene is one possibility; an ancient duplication followed by differential loss is another. Alignment problems, mixed samples, assembly errors and reference-database gaps can also create misleading patterns. A single gene tree should not be presented as evidence of a specific physical transfer mechanism.

A structured analysis begins with quality and orthology. Are the compared sequences true homologues performing comparable molecular roles, or are distant paralogues grouped by a misleading annotation? Do the sequences cover the same region, and are uncertain alignment blocks disproportionately driving the inferred grouping? Is the sequence placed on a genomic segment whose coverage or composition differs from the remainder of the assembly? Such questions have different answers depending on data type. They should be investigated as independent lines of evidence rather than summarized by one unsupported claim that the gene was 'obviously transferred.'

A statistical tree includes uncertainty. Strong support for a surprising gene grouping may indicate a genuine distinct history, but it does not by itself identify a donor, recipient, date or ecological setting. Sampling is sparse compared with microbial diversity, so an unsampled relative may explain an apparently distant association. Tree methods also make assumptions about substitution patterns and branch rates. Comparing outcomes from several defensible analyses can reveal whether the result is robust or sensitive to methodological choices. Strong disagreements can motivate new observations rather than immediate narrative closure.

Functional evidence is another distinct layer. A genomic region encoding a predicted metabolic pathway might suggest a potential phenotype, but expression and biochemical performance remain untested. A gene may be incomplete, poorly regulated or incompatible with the host's other pathways. Even an observed phenotype may depend on other genes outside the candidate region. A careful result therefore distinguishes sequence similarity, likely genomic context, measured expression and demonstrated function. These are progressively stronger claims, not interchangeable synonyms.

In communicating the result, authors should choose appropriate language: 'gene history differs from the core-genome reconstruction' is a direct observation; 'consistent with horizontal transfer' names a hypothesis; 'transfer from isolate X to Y in habitat Z' is a much stronger historical account needing substantial additional evidence. This ladder of claims helps students apply evolutionary reasoning without overstating what comparative genomics can reconstruct.


## Research note: An allele-frequency increase does not reveal how a gene moved

Suppose the frequency of a gene rises from 0.2 to 0.4 in a mixed community. This could result from growth of cells already carrying the gene, acquisition by additional lineages, arrival of carriers from elsewhere or biased recovery during sequencing. The observation alone cannot separate these mechanisms. Even a sequence associated with a plasmid does not demonstrate that a new transfer event occurred during the monitoring period. To estimate a mechanism, the investigator would need additional evidence connecting the gene to particular hosts over time and distinguishing biological change from sampling and assembly artifacts.

Horizontal exchange also complicates the definition of a microbial lineage. A cellular tree may be inferred from many conserved genes, whereas an individual gene can have a different genealogy. That difference is a feature of microbial evolution rather than a defect in the idea of ancestry. However, conflicting trees can also arise from sparse taxon sampling, alignment errors and gene duplications. A robust analysis states which data support the cellular relationship and which support a distinct gene history. Presenting either result with a single unexplained confidence score misses the biological question.

## Research note: Fitness depends on the chosen denominator

A relative fitness coefficient is meaningful only relative to a specified competitor, environment and time window. A type that performs well under one resource condition may perform poorly when that resource disappears. Deterministic selection equations assume simplified reproduction and cannot capture every ecological feedback. When presenting the graph of p′ against s, readers should notice that the initial fraction p is fixed and that the output is a hypothetical next-generation frequency. Changing the sampling unit, population structure or definition of reproductive output changes the model's biological interpretation.


## Synthesis: genetic variation, inheritance and causal claims

A Poisson model can express the probability that at least one event occurs within an abstract observation window when events are treated as independent and the expected number is specified. It does not establish how mutations arise in real cell lineages. Descendants share ancestry, selective amplification alters observed frequencies, and environmental conditions may change event rates. A calculation of one minus the probability of zero events is consequently a mathematical baseline, not a measurement of hazard or a recommendation about biological manipulation. Any connection to an observed population must be justified by the underlying experimental design.

Frequency-change models introduce a different distinction between mathematical expectation and causal history. Suppose a hypothetical type begins at frequency p and has relative reproductive weight one plus s while another type has weight one. Normalization produces a new expected frequency, but the result excludes sampling drift, population structure, environmental fluctuation and incoming lineages. A change in measured marker frequency can also arise from shifts in copy number or detection, not only from a biological fitness difference. Students should identify the dependent quantity before describing a signal as evidence of adaptation.

Horizontal transfer, plasmids, recombination and gene regulation require evidence at more than one level. Similarity between a gene in distant lineages may be compatible with movement of genetic material, yet gene duplication, loss, contamination and reconstruction error are alternatives. Detecting a gene does not ensure that it is transcribed, translated or expressed as a phenotype. Gene-regulatory models distinguish cellular context from sequence content: the same genetic capability may be silent under one condition and active under another. A strong explanation records identity, genomic context, regulatory state and measured outcome as separate pieces of evidence. The chapter emphasizes inference and conceptual mechanisms rather than procedural protocols for altering microbes.


## Quantitative investigations: interactive models

### At least one hypothetical event

A controlled teaching model uses **Expected events per window** and **Window scaling factor** to predict %. Its stated relationship is **100 × (1 − exp(−λ × scale))**. Poisson independent constant-rate event model; not a measurement of mutation biology. With expected events two at scale one, compare with the probability of zero events. Use the paired reference curve only to compare the stated parameter choice; it represents a mathematical counterfactual, not biological replicate evidence.

### Deterministic one-generation frequency change

A controlled teaching model uses **Starting type-A frequency** and **Relative advantage s** to predict proportion. Its stated relationship is **p(1+s)/[p(1+s)+(1−p)]**. Type A weight 1+s; type B weight 1; excludes drift, transfer and changing environment. Verify normalization for s=0 and compare changing starting frequency. Use the paired reference curve only to compare the stated parameter choice; it represents a mathematical counterfactual, not biological replicate evidence.

## Fully worked problems

### Problem 4.1: At least one random event

**Question.** An independent-event model predicts λ=2 mutation events in a specified abstract observation window. Find P(0) and P(≥1).

**Step 1.** For a Poisson random count, P(N=0)=e^−λ. At λ=2 this is e^−2≈0.1353. It is a probability of no events, not a mutation rate per base or generation.

**Step 2.** The complement gives P(N≥1)=1−e^−2≈0.8647, or 86.47%. Expected number two does not mean exactly two events must occur in a realization.

**Step 3.** The calculation assumes independent constant-rate events. Real mutation histories, cell lineages and variable rates can violate these conditions, and the model does not tell whether an event changes a phenotype.

### Problem 4.2: Selection frequency model

**Question.** Type A starts at frequency p=0.3 and has relative fitness 1.1 while type B has relative fitness 1. Find the deterministic one-generation frequency.

**Step 1.** Expected weighted contributions are p×1.1=0.33 for A and (1−p)×1=0.70 for B. Their total is 1.03, not exactly one before normalization.

**Step 2.** Normalize the A contribution: p′=0.33/1.03≈0.320388. Frequency rises by about 0.0204, or 2.04 percentage points, not a relative 2.04%.

**Step 3.** This single-generation model excludes drift, gene transfer and changes of environment. A measured frequency rise is consistent with selection, but alone cannot establish the underlying cause.

### Problem 4.3: Evidence for horizontal exchange

**Question.** Two genes in the same microbial sample give different phylogenetic groupings. State a reasoned inference and three non-transfer alternatives.

**Step 1.** Describe the data before explaining it: the inferred branching relationships differ between gene trees, assuming comparable sampled taxa. The discrepancy does not itself constitute a visual record of transfer.

**Step 2.** Horizontal transfer is one possibility. Other explanations include alignment errors, duplicated paralogues confused with orthologues, unequal evolutionary rates and tree-model misfit; contamination can also create misleading sequences.

**Step 3.** Check orthology, alignments, sampling and branch support. Report the result as a pattern consistent with exchange until independent genomic-context or functional evidence strengthens the transfer hypothesis.

