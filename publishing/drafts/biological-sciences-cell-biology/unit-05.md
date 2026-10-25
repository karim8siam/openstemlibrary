# Unit 5: Cell cycles

## Introduction

Cell reproduction is organized by a changing molecular network rather than a universally fixed timer. DNA must be replicated and appropriately distributed, while the cell's growth and mechanical apparatus adapt to each phase. In mitosis sister chromatids separate; in meiosis homologous chromosomes segregate before sisters, generating the distinctive genetic consequences of sexual reproduction. Checkpoints delay transitions when key requirements are unmet, although imperfect control can produce abnormal outcomes. Time-lapse evidence is particularly important: a single image of many cells does not identify each cell's history. The worked exercises distinguish the fraction of time one cell spends in a phase from the percentage of an asynchronous population found in that phase.



## 5.1 Checkpoints

### Central mechanism and vocabulary

Progress through the cell cycle depends on cyclin-dependent kinase activity, regulated proteolysis, and checkpoints that assess conditions such as DNA integrity, replication status, and spindle attachment. Checkpoint signaling can delay transitions, but it is not an infallible inspector guaranteeing perfect chromosomes. The restriction point and other decision networks integrate growth factors, nutrient state, cell size, and damage responses. A phase-duration distribution is more biologically informative than a single universal clock because even genetically similar cells vary in their timing.

### Why this mechanism matters

The central issue in **checkpoints** is not only naming the constituent structures but explaining which physical or biochemical events change the state of a cell. Start with the specific statement: Progress through the cell cycle depends on cyclin-dependent kinase activity, regulated proteolysis, and checkpoints that assess conditions such as DNA integrity, replication status, and spindle attachment. Description and mechanism are not equivalent.

Consider a thought experiment involving **checkpoints**. Equal-looking images need not imply identical histories. The same pool size then conceals different mechanisms. For this topic, examine the meaning of state residence times and lineage history; ask which additional time point, reference marker, or independent assay would break the ambiguity. This is especially important because survivorship bias can make population averages deceptively stable even when individuals change substantially.

### Mechanism from molecular to cellular scale

A mechanism for checkpoints should be articulated at no fewer than three connected levels. In this topic, the physical description above culminates in the following insight: A phase-duration distribution is more biologically informative than a single universal clock because even genetically similar cells vary in their timing.

### Experimental evidence and its interpretation

Use live-cell reporters that distinguish G1, S, G2, and M transitions. Under a controlled perturbation, quantify each phase's residence time and the probability of arrest or death. Compare DNA-damage markers with actual repair and survival outcomes; include unstressed cells and sensor-calibration controls.

**Track transitions.** Begin with a prespecified comparison that changes one primary factor and holds other plausible causes as constant as practicable. For checkpoints, take the proposed intervention from the preceding protocol and state the expected direction of change before measuring it.

### Quantitative and modeling viewpoint

The exact form depends on checkpoints, but dimensional consistency always constrains what can be added, multiplied, or compared. Estimate uncertainty from biological replicates and instrument variation separately when possible.

Think through three limiting cases before trusting a fitted relation for checkpoints.

### Competing explanations, limitations, and quality controls

An accumulation of cells in one phase may mean arrest or simply faster entry with unchanged exit. Molecular markers sometimes persist after a phase transition. Checkpoint proteins have roles outside their most familiar pathway.

A persuasive conclusion about checkpoints has to specify what evidence would count against it.

### Guided interpretation and transfer

Suppose a collaborator reports a statistically clear difference in checkpoints after a treatment and asks whether to describe the treatment as acting directly on the named process. Then request a second measurement with a different vulnerability.

### Applied biological investigation

A cohort of cells exposed to a replication stressor accumulates with DNA content near the S-phase region. This could indicate checkpoint-induced slowing, but a rise in the S-phase fraction can also result from more cells entering S while the exit rate remains unchanged. Time-lapse reporters or short nucleotide-labeling pulses reveal entry and exit rates separately. The experimental design includes an untreated culture and a release phase after the stressor is removed. A persistently arrested group must be distinguished from cells that die or detach, because missing cells bias inferred phase duration. The cell-cycle simulation varies G1 and S duration for a single idealized cycle; the resulting time fraction is not equal to the phase fraction of a proliferating asynchronous culture unless age distribution and growth effects are modeled. This distinction is important for interpreting clinical or laboratory proliferation assays.


## 5.2 Mitosis

### Central mechanism and vocabulary

Mitosis distributes replicated chromosomes through coordinated chromosome condensation, kinetochore attachment, spindle dynamics, and chromatid separation. The spindle is an active mechanical machine assembled from microtubules, motors, and structural proteins. Chromosomes can move because of microtubule polymerization changes and molecular-motor activity, not because one universal cable pulls them through the cell. The spindle assembly checkpoint monitors attachment-related conditions and postpones anaphase until critical requirements are sufficiently met. Cytokinesis partitions the cytoplasm through a distinct but coordinated machinery.

### Why this mechanism matters

The central issue in **mitosis** is not only naming the constituent structures but explaining which physical or biochemical events change the state of a cell. Start with the specific statement: Mitosis distributes replicated chromosomes through coordinated chromosome condensation, kinetochore attachment, spindle dynamics, and chromatid separation. Description and mechanism are not equivalent.

Consider a thought experiment involving **mitosis**. Equal-looking images need not imply identical histories. The same pool size then conceals different mechanisms.

### Mechanism from molecular to cellular scale

A mechanism for mitosis should be articulated at no fewer than three connected levels. In this topic, the physical description above culminates in the following insight: Cytokinesis partitions the cytoplasm through a distinct but coordinated machinery.

### Experimental evidence and its interpretation

Time-lapse a chromosome marker and a spindle marker, then measure the lag from alignment to anaphase onset. Perturb microtubule dynamics mildly enough to retain viable cells, and quantify segregation errors. A fixed-image count should be supplemented with live tracking to distinguish transient misalignment from persistent defects.

For mitosis, take the proposed intervention from the preceding protocol and state the expected direction of change before measuring it.

### Quantitative and modeling viewpoint

The exact form depends on mitosis, but dimensional consistency always constrains what can be added, multiplied, or compared. Estimate uncertainty from biological replicates and instrument variation separately when possible.

Think through three limiting cases before trusting a fitted relation for mitosis.

### Competing explanations, limitations, and quality controls

Images of condensed chromosomes cannot alone identify the molecular cause of spindle failure. Drugs that affect microtubules can also indirectly change signaling and cell shape. Beware interpreting microscope stage drift as chromosome movement.

A persuasive conclusion about mitosis has to specify what evidence would count against it.

### Guided interpretation and transfer

Suppose a collaborator reports a statistically clear difference in mitosis after a treatment and asks whether to describe the treatment as acting directly on the named process. Then request a second measurement with a different vulnerability.

### Applied biological investigation

In a mitotic movie, one chromosome remains outside the metaphase plate for several minutes. A fixed endpoint after the movie shows an apparently normal anaphase. One hypothesis is that the chromosome was corrected and segregated properly; another is that the fluorescent marker hid a persistent attachment error. To discriminate, follow both chromatids into daughter nuclei and assess lagging fragments or micronuclei after cytokinesis. A spindle marker can reveal microtubule organization, but it may not report kinetochore tension accurately. A checkpoint inhibitor could shorten metaphase yet raise segregation errors, demonstrating the tradeoff between progression and quality control. In this exercise students should state whether each observation concerns alignment, attachment, tension, checkpoint signaling, or successful inheritance. Mixing those distinct variables under a single label of normal mitosis prevents mechanistic interpretation.


## 5.3 Meiosis

### Central mechanism and vocabulary

Meiosis generates haploid products through one round of DNA replication followed by two nuclear divisions in the canonical sexual life cycle. Homologs pair and may exchange DNA during prophase I; homologous chromosomes segregate in the first division, while sister chromatids segregate in the second. Recombination rearranges alleles and assists homolog segregation in many organisms. Variation arises not from meiosis alone but from chromosome assortment, recombination, mutation, and fertilization. Meiotic programs vary in detail across taxa, and not every organism has an identical recombination landscape.

### Why this mechanism matters

The central issue in **meiosis** is not only naming the constituent structures but explaining which physical or biochemical events change the state of a cell. Start with the specific statement: Meiosis generates haploid products through one round of DNA replication followed by two nuclear divisions in the canonical sexual life cycle. Description and mechanism are not equivalent.

Consider a thought experiment involving **meiosis**. Equal-looking images need not imply identical histories. The same pool size then conceals different mechanisms.

### Mechanism from molecular to cellular scale

A mechanism for meiosis should be articulated at no fewer than three connected levels. In this topic, the physical description above culminates in the following insight: Meiotic programs vary in detail across taxa, and not every organism has an identical recombination landscape.

### Experimental evidence and its interpretation

Score markers on homologous chromosomes in meiotic products and compare linkage patterns to a genetic model. Crossovers can be inferred statistically from progeny classes, whereas cytological foci suggest positions of repair or recombination proteins rather than proving final crossovers. Include sample-size uncertainty when estimating a recombination fraction.

For meiosis, take the proposed intervention from the preceding protocol and state the expected direction of change before measuring it.

### Quantitative and modeling viewpoint

The exact form depends on meiosis, but dimensional consistency always constrains what can be added, multiplied, or compared. Estimate uncertainty from biological replicates and instrument variation separately when possible.

Think through three limiting cases before trusting a fitted relation for meiosis.

### Competing explanations, limitations, and quality controls

A recombination fraction near 0.5 does not prove that two loci reside on different chromosomes; widely separated loci on one chromosome may also assort approximately independently. Meiosis is not simply mitosis performed twice.

A persuasive conclusion about meiosis has to specify what evidence would count against it.

### Guided interpretation and transfer

Suppose a collaborator reports a statistically clear difference in meiosis after a treatment and asks whether to describe the treatment as acting directly on the named process. Then request a second measurement with a different vulnerability.

### Applied biological investigation

A genetics class crosses two loci and observes that about 18% of informative progeny carry recombinant marker combinations. The apparent recombination fraction is compatible with linkage and can serve as an approximate map distance over relatively short intervals, but it undercounts multiple crossover events that restore parental combinations. The instructor asks students to distinguish the behavior of homologs at meiosis I from sister chromatid separation at meiosis II. Cytological images showing a crossover-related protein focus are evidence of a molecular intermediate, not a complete count of final genetic exchanges. Crossing-over probabilities can differ by chromosomal position and genotype. A properly designed experiment records sample size and parental haplotypes and separates biological recombination from genotyping error. The aim is to connect molecular events, whole-chromosome mechanics, and observed inheritance rather than equating a single fluorescent focus with a genetic outcome.


## 5.4 Chromosome segregation

### Central mechanism and vocabulary

Faithful segregation relies on cohesion, tension generation, kinetochore–microtubule attachment, and regulated separation. Errors produce aneuploid daughter cells, mosaics, or gametes, with consequences depending on chromosome and cell context. Nondisjunction and lagging chromosomes arise through distinguishable mechanisms. The relation between spindle mechanics and genome inheritance can be studied at multiple scales, from a single kinetochore's force to population frequencies of abnormal karyotypes.

### Why this mechanism matters

The central issue in **chromosome segregation** is not only naming the constituent structures but explaining which physical or biochemical events change the state of a cell. Start with the specific statement: Faithful segregation relies on cohesion, tension generation, kinetochore–microtubule attachment, and regulated separation. Description and mechanism are not equivalent.

Consider a thought experiment involving **chromosome segregation**. Equal-looking images need not imply identical histories. The same pool size then conceals different mechanisms.

### Mechanism from molecular to cellular scale

A mechanism for chromosome segregation should be articulated at no fewer than three connected levels. In this topic, the physical description above culminates in the following insight: The relation between spindle mechanics and genome inheritance can be studied at multiple scales, from a single kinetochore's force to population frequencies of abnormal karyotypes.

### Experimental evidence and its interpretation

Analyze chromosome counts using a validated probe or sequencing-derived copy-number assay and compare to time-lapse observations of anaphase. Use technical replicates and blind classification. Calculate a missegregation-event rate from a defined denominator such as observed divisions rather than total cells at an arbitrary snapshot.

For chromosome segregation, take the proposed intervention from the preceding protocol and state the expected direction of change before measuring it.

### Quantitative and modeling viewpoint

The exact form depends on chromosome segregation, but dimensional consistency always constrains what can be added, multiplied, or compared. Estimate uncertainty from biological replicates and instrument variation separately when possible.

Think through three limiting cases before trusting a fitted relation for chromosome segregation.

### Competing explanations, limitations, and quality controls

Apparent copy-number variation can arise from cell-cycle effects, sequencing coverage, or segmentation errors. Low-frequency events require large samples and confidence intervals; a small absolute difference may be meaningless when detection sensitivity is low.

A persuasive conclusion about chromosome segregation has to specify what evidence would count against it.

### Guided interpretation and transfer

Suppose a collaborator reports a statistically clear difference in chromosome segregation after a treatment and asks whether to describe the treatment as acting directly on the named process. Then request a second measurement with a different vulnerability.

### Applied biological investigation

A tissue sample has a small fraction of cells with apparently altered chromosome copy number. If the sample contains cells in S phase, uneven replication timing can alter relative sequencing coverage and mimic some changes in copy number. Imaging-based enumeration with chromosome-specific probes offers an orthogonal measurement, although overlapping spots can cause errors. The laboratory predefines what qualifies as a segregation error per observed division and quantifies both successful and abnormal divisions, including those later lost from the field. Using the interactive probability model, students can see how a small independent per-division risk accumulates across many trials. They must then assess the independence assumption: shared spindle perturbations or inherited defects can cause correlated errors. The final conclusion requires a denominator, detection sensitivity, uncertainty, and a description of whether the abnormality is mosaic, persistent, or transient.


## Fully worked problems

### CB-U5-P1: Cell-cycle time allocation

**Question:** For an illustrative single cell, G1 lasts 9 h, S 8 h, G2 3 h and M 1 h. Find total cycle time and fraction spent in S phase.

- 1. The total time is 9+8+3+1 = 21 hours.
- 2. The S-phase fraction of that single trajectory is 8/21≈0.38095.
- 3. Expressed as a percentage this is approximately 38.1%.
- 4. This is not necessarily the S-phase fraction in an asynchronous exponentially growing population, where birth and age distributions are nonuniform.
- 5. A DNA-content histogram or live reporter can test an appropriately specified population model.

**Verified final result:** 21 h; S occupies 38.1% of that cell's cycle

### CB-U5-P2: Mitotic index

**Question:** In a snapshot of 800 fixed cells, 48 are classified as mitotic using prespecified morphological criteria. Estimate the mitotic index and describe uncertainty.

- 1. Use mitotic index M=(number in mitosis)/(total counted).
- 2. Compute 48/800=0.06.
- 3. Convert to 6.0%.
- 4. An approximate binomial standard error is sqrt(0.06×0.94/800)≈0.0084, or 0.84 percentage points.
- 5. Clustering by field and biased field selection can make binomial-only uncertainty underestimate variability; replicate cultures are needed.

**Verified final result:** 6.0%; approximate simple-binomial SE 0.84 percentage points

### CB-U5-P3: Segregation error probability

**Question:** Assume each of 40 divisions independently has a 1% probability of an observable chromosome segregation error. Estimate the probability of at least one error.

- 1. Write P(no errors)=(1−p)^n under independence.
- 2. Substitute (0.99)^40≈0.66897.
- 3. Take the complement: P(at least one)=1−0.66897≈0.3310.
- 4. The result is about 33.1%, despite the per-division error risk being only 1%.
- 5. Real divisions share environmental and genetic conditions, so independence can fail and increase between-culture variability.

**Verified final result:** Approximately 33.1%



## Integrative study: how a checkpoint protects chromosome inheritance

A treatment delays mitosis in a cultured mammalian cell line. An endpoint DNA-content histogram shows more cells in the G2/M region, and a short movie shows prolonged chromosome alignment. The naive conclusion is that the drug improved chromosome segregation by giving cells extra time. A competing interpretation is that the treatment damages spindle attachment, triggers a checkpoint, and eventually increases errors among cells that escape or adapt. Distinguishing these stories requires tracking what happens to individual cells after the delay rather than inferring successful inheritance from residence time alone.

Start by collecting a time-lapse series with a chromosome marker and an appropriate spindle or kinetochore marker. Record how long each cell spends in interphase, prometaphase, metaphase, anaphase, and cytokinesis. Define events before observing treatment labels and, where possible, use blinded scoring. In a synchronized cohort, estimate phase transitions and loss of cells from the observation field. A snapshot fraction must not be equated automatically with the duration of the corresponding phase, because entry rates, division rates, death, and population age distributions alter observed proportions. Use live reporters to distinguish entry from exit and a recovery experiment to assess whether arrest reverses.

At the chromosome level, differentiate sister-chromatid separation during mitosis from homolog segregation in meiosis I. Their mechanisms share elements of chromosome architecture and spindle force, but genetic outcomes differ. In meiotic material, linkage-marker data can provide an indirect measure of recombination and segregation; in mitotic material, cell-lineage imaging and copy-number assays test the success of inheritance. If the treated group has more micronuclei, evaluate whether these stem from lagging chromosomes or breakage rather than labeling every abnormal structure as nondisjunction.

For a quantitative illustration, a per-division detectable error probability p produces probability 1−(1−p)^n of at least one event among n independent divisions. This teaching model clarifies how rare risks accumulate but does not establish independence across cells from one stressed culture. A shared environmental insult can correlate failures. Report the number of divisions observed, segmentation reliability, and confidence interval rather than only the number of abnormal cells. The scientific result should distinguish what was measured—timing, attachment quality, chromosome distribution, or viable descendants—from the causal claim that a checkpoint did or did not protect genome integrity.

## Unit synthesis and interpretation

The cell-cycle module ends by contrasting three denominators. The fraction of elapsed time a single cell spends in S phase uses that cell's total cycle duration. A mitotic index in a fixed sample uses the number of scored cells. The probability that at least one segregation error occurs over multiple divisions uses the number of relevant observed trials. These cannot be interchanged even when they are all reported as percentages. A high mitotic index can reflect prolonged mitosis, rapid entry, or population turnover. A low error proportion may still be important over numerous divisions. Students should propose a time-lapse protocol that records cells lost from view and the time of anaphase onset, then compare it with a fixed-image snapshot. This exercise ties mathematical denominators to the actual biology of division, differentiation, and chromosome inheritance.

## Interactive model specifications

### Single-cell S-phase allocation

**Question tested by the model:** what share of one idealized cell's cycle is spent in DNA synthesis? The percentage is 100S/(S+G1+G2+M), with G2 fixed at 3 h and M fixed at 1 h in this demonstration. With S=8 h and G1=9 h, the result is 38.1% of a 21-hour trajectory. Increasing S increases its fraction but simultaneously increases the full cycle duration. This fraction must not be equated to the fraction of S-phase cells in a freely proliferating asynchronous population, where the cell-age distribution and state-dependent loss can bias counts.

### At-least-one segregation error

**Question tested by the model:** how does a small error risk accumulate over many observed divisions? With independent per-division probability p, the chance of one or more detectable errors is 100[1−(1−p)^n] percent. With n=40 and p=0.01, the result is about 33.1%. The graph approaches 100% as the number of trials grows while leaving the individual per-division probability unchanged. Real errors can be correlated within a stressed culture or lineage, and assays miss some events; therefore use the model as an independence benchmark, not as a measured population hazard without evidence.

