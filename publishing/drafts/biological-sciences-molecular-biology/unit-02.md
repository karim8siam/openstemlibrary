# Unit 2: Replication

## Unit overview

Replication is a coordinated process that preserves sequence while preparing two complete DNA copies for cell division. It requires molecular initiation, unwinding, primer synthesis, polymerase extension, fragment maturation, and chromosome-end strategies. An estimate of how quickly DNA is copied can be surprisingly accurate for a deliberately simplified fork model, yet an actual cell also regulates when each origin may fire. Focus on a causal timeline: licensing before synthesis, extension at forks, proofreading and repair during or after synthesis, and completion at chromosome boundaries. A measured polymerase error is not equivalent to a heritable mutation.

## Learning goals

Understand the causal molecular sequence for four named processes; derive and interpret simplified quantitative statements; identify measurement controls; separate experimental observation from molecular inference; and explain the limits of the idealized simulation models.

## Unit synthesis

Replicating chromosomes requires both chemistry and scheduling. The polymerase must have an appropriate primer terminus and the template must be accessible, yet an origin cannot fire every time a polymerase is nearby. Separate initiation licensing from physical synthesis. A bacterial chromosome might be well represented by a small number of replication forks, while a human chromosomal domain requires many origins and flexible fork behavior. In a problem-solving diagram, show where lagging-strand fragments are initiated, where primer removal creates gaps, and where ligation completes the backbone. Identify two independent opportunities for error correction: polymerase proofreading and postreplicative mismatch repair. Finally, mark the geometric end of a linear chromosome and explain why the end-replication problem is unlike a simple internal gap. Each element must be situated in the copying sequence rather than treated as a disconnected vocabulary term.

## Unit-specific integrated assessment

A capstone exercise for replication gives learners two sketches of a chromosome copied from differently spaced origins. In the first, all forks move at constant speed; in the second, one fork stalls and an unanticipated origin becomes active. Require them to estimate total synthesized length at each observation and explain whether the original traversal formula still applies. The diagrams should include primer placement on the lagging strand and a plan for joining its fragments. Next ask which measured variable could distinguish a slow polymerase from an origin that fired later. A good response uses the distance between labeled nascent-DNA tracks, rather than just a final DNA-content histogram. Finally, the learner must separate one nucleotide-copying error from a variant that survives mismatch repair and becomes inherited. The numerical part is small, but the conceptual distinctions test whether the entire molecular process has been understood.

## 2.1 Origins and replisomes

### Mechanistic foundation

Replication origins are sites where initiator assemblies promote local DNA unwinding and replication machinery is recruited. Two forks commonly emerge from an origin and move in opposite directions across a replication domain. Bacterial chromosome replication and eukaryotic chromosome replication share template-dependent synthesis but differ markedly in origin number, licensing and chromosome organization. Origin firing is regulated so DNA is duplicated once per cell cycle. A fork has a leading and a lagging strand because DNA polymerases extend a growing chain only in the 5-prime to 3-prime direction.

### Stepwise reasoning from molecular events to an observation

A useful molecular explanation begins by identifying the actual substrate and product in **origins and replisomes**, rather than merely naming a molecule associated with the phenomenon. The starting claim is that replication origins are sites where initiator assemblies promote local DNA unwinding and replication machinery is recruited. In an active cell, production and consumption often occur simultaneously. For origins and replisomes, the distinction is especially consequential because a fork has a leading and a lagging strand because DNA polymerases extend a growing chain only in the 5-prime to 3-prime direction.



### Study design: choosing what to observe

Map nascent-DNA incorporation over short pulses and compare fork movement under modest nucleotide depletion. Distinguish a slower fork from fewer active origins by counting independent replication tracks.

For **origins and replisomes**, write down the expected results for three matched conditions: an unperturbed sample, a targeted perturbation of the proposed molecular step, and a rescue that restores function without otherwise changing the assay. A fourth condition should deliberately test an alternative explanation.

### Quantitative thinking without false precision

For origins and replisomes, distinguishing the number of molecules from the proportion of molecules in a state is often essential.

Start analysis with the limiting cases of an idealized model. When writing about origins and replisomes, state where idealization ends and empirical validation must begin.

### Discriminating causes and ruling out artifacts

An ideal formula for replication time assumes symmetric constant fork speeds and equally spaced origins; fork pausing and dormant-origin activation break it. Build two alternative hypotheses that could mimic the predicted observation.

A meaningful negative result needs equal scrutiny. Establish the dynamic range with positive and negative controls.

### Specific molecular investigation

Suppose a bacterial replication locus is labeled at regular intervals and fluorescent tracks extending away from it are mapped over time. Two symmetric tracks support bidirectional movement, but they do not reveal whether initiation at a second origin occurred elsewhere. A 2.4-megabase genome copied by two uninterrupted 600-nt/s forks has a model traversal time of about thirty-three minutes. This bound is only meaningful after identifying origin configuration and initiation time. An experiment should record fork asymmetry and cell-to-cell variance rather than report only a single mean length. Nucleotide depletion could slow movement while triggering compensatory changes in initiation. Independent tracks from distinct origins must be separated before inferring the global completion time.

## 2.2 Polymerases and strand synthesis

### Mechanistic foundation

Replicative polymerases add complementary nucleotides to a 3-prime hydroxyl at a growing primer terminus. Helicases separate template strands; primases provide primers; sliding clamps enhance processivity; ligases join completed fragments after primer removal and gap filling. The lagging strand is synthesized in segments rather than continuously in the direction of fork advance. Coordination prevents large regions of single-stranded DNA from remaining exposed, but the actual architecture differs between bacteria and eukaryotes.

### Stepwise reasoning from molecular events to an observation

A useful molecular explanation begins by identifying the actual substrate and product in **polymerases and strand synthesis**, rather than merely naming a molecule associated with the phenomenon. The starting claim is that replicative polymerases add complementary nucleotides to a 3-prime hydroxyl at a growing primer terminus. In an active cell, production and consumption often occur simultaneously. For polymerases and strand synthesis, the distinction is especially consequential because coordination prevents large regions of single-stranded DNA from remaining exposed, but the actual architecture differs between bacteria and eukaryotes.



### Study design: choosing what to observe

Compare pulse-labeled fragment size distributions with and without a controlled ligase perturbation. Accumulation of shorter unjoined pieces supports an effect on maturation but could also reflect altered primer removal or degradation.

For **polymerases and strand synthesis**, write down the expected results for three matched conditions: an unperturbed sample, a targeted perturbation of the proposed molecular step, and a rescue that restores function without otherwise changing the assay. A fourth condition should deliberately test an alternative explanation.

### Quantitative thinking without false precision

For polymerases and strand synthesis, distinguishing the number of molecules from the proportion of molecules in a state is often essential.

Start analysis with the limiting cases of an idealized model. When writing about polymerases and strand synthesis, state where idealization ends and empirical validation must begin.

### Discriminating causes and ruling out artifacts

Do not infer polymerase direction from the physical direction of a replisome. Molecular movement, template polarity and product extension are separate descriptions. Build two alternative hypotheses that could mimic the predicted observation.

A meaningful negative result needs equal scrutiny. Establish the dynamic range with positive and negative controls.

### Specific molecular investigation

A ligase-defective strain accumulates short DNA species after a pulse of nucleotide label. One interpretation is failed sealing of adjacent fragments; another is increased degradation following replication stress. Analyze size distributions immediately after the pulse and after a chase, then compare ligase restoration and a control that affects DNA degradation. Polymerase moves along a template 3-prime to 5-prime while its product extends 5-prime to 3-prime, and confusing these orientations would reverse the strand assignment. A newly isolated fragment is not necessarily a nascent Okazaki fragment merely because it is short. Its sequence location, strand specificity, primer signature and maturation kinetics provide complementary evidence.

## 2.3 Proofreading and replication fidelity

### Mechanistic foundation

Many replicative DNA polymerases reject mismatched incoming nucleotides through selectivity and also use a 3-prime to 5-prime exonuclease activity to remove certain misincorporations. Post-replicative mismatch repair can correct additional errors. Observed mutation frequency is a downstream result of copying errors, repair efficiency, damage, selection and sampling. Errors at neighboring positions can be correlated, so the independent-event model used in introductory calculations is only a baseline.

### Stepwise reasoning from molecular events to an observation

A useful molecular explanation begins by identifying the actual substrate and product in **proofreading and replication fidelity**, rather than merely naming a molecule associated with the phenomenon. The starting claim is that many replicative DNA polymerases reject mismatched incoming nucleotides through selectivity and also use a 3-prime to 5-prime exonuclease activity to remove certain misincorporations. In an active cell, production and consumption often occur simultaneously. For proofreading and replication fidelity, the distinction is especially consequential because errors at neighboring positions can be correlated, so the independent-event model used in introductory calculations is only a baseline.



### Study design: choosing what to observe

Compare mutation accumulation in isogenic proofreading-proficient and proofreading-defective lines under matched growth conditions, then confirm candidate variants with an independent sequencing method.

For **proofreading and replication fidelity**, write down the expected results for three matched conditions: an unperturbed sample, a targeted perturbation of the proposed molecular step, and a rescue that restores function without otherwise changing the assay. A fourth condition should deliberately test an alternative explanation.

### Quantitative thinking without false precision

For proofreading and replication fidelity, distinguishing the number of molecules from the proportion of molecules in a state is often essential.

Start analysis with the limiting cases of an idealized model. When writing about proofreading and replication fidelity, state where idealization ends and empirical validation must begin.

### Discriminating causes and ruling out artifacts

An error rate measured per incorporated nucleotide cannot be substituted directly for the probability that an organism develops a particular phenotype. Build two alternative hypotheses that could mimic the predicted observation.

A meaningful negative result needs equal scrutiny. Establish the dynamic range with positive and negative controls.

### Specific molecular investigation

Imagine a mutation-accumulation experiment with lines propagated through repeated bottlenecks. A proofreading mutation raises the number of called variants relative to the parental strain. Before claiming a specific intrinsic incorporation error rate, distinguish nucleotide misincorporation from postreplicative mismatch repair and from the probability that a variant becomes fixed in the analyzed lineage. The observed mutational spectrum can be informative: transition and transversion classes may shift differently under distinct mechanisms. Long sequencing reads can reveal haplotype structure, but read-level damage and base-calling artifacts still need controls. A mutator phenotype should be established across multiple independently grown lines, not only many reads from one clone.

## 2.4 Chromosome ends and telomerase

### Mechanistic foundation

Linear chromosome ends pose an end-replication problem because primer removal can leave a terminal segment unfilled by ordinary synthesis. Telomeres comprise repetitive DNA and associated protective proteins; telomerase can extend certain chromosome ends using an RNA template contained within the ribonucleoprotein. Telomere lengths vary between chromosomes and individual cells. Shortening rate depends on cell type, replication history, repair and telomerase activity; it is not a universal clock for aging.

### Stepwise reasoning from molecular events to an observation

A useful molecular explanation begins by identifying the actual substrate and product in **chromosome ends and telomerase**, rather than merely naming a molecule associated with the phenomenon. The starting claim is that linear chromosome ends pose an end-replication problem because primer removal can leave a terminal segment unfilled by ordinary synthesis. In an active cell, production and consumption often occur simultaneously. For chromosome ends and telomerase, the distinction is especially consequential because shortening rate depends on cell type, replication history, repair and telomerase activity; it is not a universal clock for aging.



### Study design: choosing what to observe

Track distributions of telomere length rather than only the mean during a long-term cell culture experiment. Pair size measurements with telomerase activity and DNA-damage markers.

For **chromosome ends and telomerase**, write down the expected results for three matched conditions: an unperturbed sample, a targeted perturbation of the proposed molecular step, and a rescue that restores function without otherwise changing the assay. A fourth condition should deliberately test an alternative explanation.

### Quantitative thinking without false precision

For chromosome ends and telomerase, distinguishing the number of molecules from the proportion of molecules in a state is often essential.

Start analysis with the limiting cases of an idealized model. When writing about chromosome ends and telomerase, state where idealization ends and empirical validation must begin.

### Discriminating causes and ruling out artifacts

A linear loss-per-division exercise is a deliberately simplified upper-level illustration, not a biological prediction of clinical aging or cancer risk. Build two alternative hypotheses that could mimic the predicted observation.

A meaningful negative result needs equal scrutiny. Establish the dynamic range with positive and negative controls.

### Specific molecular investigation

A cultured cell line has a mean telomere length of 8 kilobases at baseline and a reduced mean after several passages. Such data cannot demonstrate a constant 60-bp loss per division unless divisions and length changes are independently tracked. A population can change its mean through selective survival of subclones with different initial telomeres. Determine whether a putative telomerase increase reflects a genuinely active ribonucleoprotein and whether it acts uniformly across chromosome ends. Use both an average-length measure and a method sensitive to short-end distributions. The shortest telomeres may influence checkpoint responses even when the overall average changes only slightly. This is a lesson in interpreting a distribution rather than a single aggregate.

## Guided molecular investigation

### Evidence integration lab

The aim of this studio is to compare molecular readouts that often have different denominators or experimental biases. Begin with a blinded sample label and a recorded protocol. In the analysis, separate substrate abundance, product abundance, reaction rate, and biological outcome. Use three genuinely independent biological samples per condition as an illustrative minimal planning exercise, while acknowledging that sample-size requirements depend on power, variation and experimental design. The hypothetical study below asks you to predict data patterns rather than pretending the described results have been observed.

### Investigation 2.1: Origins and replisomes and Polymerases and strand synthesis

A lab attempts to connect origins and replisomes to polymerases and strand synthesis using a shared perturbation. The first obligation is to keep the prediction narrow. Replication origins are sites where initiator assemblies promote local DNA unwinding and replication machinery is recruited. Two forks commonly emerge from an origin and move in opposite directions across a replication domain. Bacterial chromosome replication and eukaryotic chromosome replication share template-dependent synthesis but differ markedly in origin number, licensing and chromosome organization. Origin firing is regulated so DNA is duplicated once per cell cycle. A fork has a leading and a lagging strand because DNA polymerases extend a growing chain only in the 5-prime to 3-prime direction. The connected response should be measured separately because Replicative polymerases add complementary nucleotides to a 3-prime hydroxyl at a growing primer terminus. Helicases separate template strands; primases provide primers; sliding clamps enhance processivity; ligases join completed fragments after primer removal and gap filling. The lagging strand is synthesized in segments rather than continuously in the direction of fork advance. Coordination prevents large regions of single-stranded DNA from remaining exposed, but the actual architecture differs between bacteria and eukaryotes. A single terminal measurement cannot determine whether the perturbation changed upstream material, a rate-limiting processing step, or sample survival. The study therefore predefines an early molecular observation and a late functional output, with an explicit normalization rule for each.

The proposed primary assay follows this plan: Map nascent-DNA incorporation over short pulses and compare fork movement under modest nucleotide depletion. Distinguish a slower fork from fewer active origins by counting independent replication tracks. An orthogonal procedure addresses the downstream question: Compare pulse-labeled fragment size distributions with and without a controlled ligase perturbation. Accumulation of shorter unjoined pieces supports an effect on maturation but could also reflect altered primer removal or degradation. Its independent readout should not reuse the same molecular normalization error. Include a negative treatment, a validated positive comparison if available, and a material-balance or integrity control. When analyzing a gene perturbation, record allele or construct verification separately from RNA abundance and protein abundance. That prevents the convenient but unsupported inference that a verified DNA change automatically changed function.

For the interpretation, construct a table with rows for no change, increased upstream signal only, changed downstream signal only, and concordant changes in both. State at least two plausible mechanisms for each nonzero pattern. The most serious limitation may involve proofreading and replication fidelity: An error rate measured per incorporated nucleotide cannot be substituted directly for the probability that an organism develops a particular phenotype. A satisfactory report includes the type of observation that would falsify the chosen mechanism, the magnitude of technical uncertainty, and an explanation of which conclusions are about a model versus observed living cells. The outcome is a proposed experimental logic, not a claim that biological data were collected.

## Fully worked questions

All numerical inputs are constructed teaching examples. Where a model is conditional, that condition is part of the solution.

### Problem 1: Bidirectional replication time

A 2.4 Mb circular chromosome replicates from one origin with two equal-speed forks, each moving 600 nucleotides per second. Estimate traversal time ignoring pauses.

**Worked reasoning**

1. The forks together cover 2×600 = 1200 bp per second.
2. Time = 2.4×10^6/1200 = 2000 seconds, or about 33.3 minutes.
3. This represents fork traversal after initiation; cell-cycle and termination overheads are excluded.
4. Alternative origin structures require another denominator.

### Problem 2: Error-free copying probability

An illustrative polymerase has a residual independent per-base error probability 10⁻⁶ after the specified correction stages. For a 20,000-base stretch, estimate probability that zero errors occur.

**Worked reasoning**

1. The exact independent model gives (1−10⁻⁶)^20000 ≈0.98020.
2. The rare-event approximation e^(−Np) = e^(−0.02) ≈0.98020 agrees.
3. The chance of at least one error is about 1.98%.
4. This is not equivalent to an observed fixed mutation rate after selection and subsequent repair.

### Problem 3: Linear telomere shortening

In a deliberately simplified model, telomere length begins at 8,000 bp and loses 60 bp per division. What remains after 35 divisions?

**Worked reasoning**

1. Calculate 35×60 = 2100 bp modeled loss, then 8000−2100 = 5900 bp.
2. Verify units remain base pairs throughout.
3. Real telomere length is heterogeneous and may change through telomerase, oxidative damage or pathway-dependent processing; use the result only as a test of the linear null model.

## Simulations and assumptions

The two simulation cards below are local, offline-capable numerical thought experiments. They are parameterized formula demonstrations, not mechanistic claims about a real cell type. Inspect the stated assumptions first, then vary an input, compare limiting cases and reset the model to its default.

### Model focus: Bidirectional fork travel

For a bidirectionally replicated region of L megabases with two equal-speed forks of v nucleotides per second, the traversal estimate is t=L×10⁶/(2v). Divide seconds by sixty to obtain minutes. A 2.4-Mb region and a 600-nt/s fork rate yield about 33.3 minutes. If one fork stalls while the other proceeds, the equal-sharing assumption fails and the true completion time can grow considerably. Extra active origins or fork convergence may shorten completion under particular layouts. Plotting L against estimated time at fixed v gives a straight line; doubling v at fixed L halves the time. Students should sketch actual physical fork positions on the same chromosome before using this formula, because fork count is not necessarily uniform in a eukaryotic replication domain.

### Model application and sensitivity test

Imagine two replication experiments with identical chromosome length but visibly different fork-track distributions. In experiment A, both tracks are straight and symmetric over time. In experiment B, one track pauses repeatedly while another origin appears. The bidirectional two-fork equation can summarize A but may give an invalid completion estimate for B. Map a fork rate of 600 nucleotides each second into distances traveled at ten-minute intervals, and mark where the forks would meet for a 2.4-Mb region. At ten minutes, each ideal fork has covered 360 kilobases, so together they have copied 720 kilobases, leaving 1.68 megabases to be traversed. Compare this with a condition in which rate is halved, and explain why the amount left after ten minutes doubles neither exactly nor necessarily under more complicated replication architecture. In a laboratory, origin timing and fork velocity should be quantified separately by DNA-fiber or related nascent-DNA methods. Chromosome copy-number profiles may corroborate the trend but require cell-cycle distribution controls.

### Model focus: Probability of zero copying errors

Assume a residual probability e of copying an individual nucleotide incorrectly after the specified proofreading stage and independent copying events across N bases. The probability of an error-free copied segment is (1−e)^N, and the complement is the probability of one or more errors. With N=20,000 and e=10⁻⁶, the no-error probability is approximately 98.02 percent. A shorter sequence has a larger error-free probability at unchanged e, but the relationship is not linear with length. The Poisson approximation e^(−Ne) becomes accurate for small e with moderate Ne. A mutation spectrum or observed organism-level mutation count requires downstream repair, cell selection and sequencing error to be considered. In the simulation, 'error-free' refers only to this stated mathematical stage and should never be interpreted as an assurance of chromosomal stability.

### Model application and sensitivity test

To inspect the difference between incorporation errors and fixed variants, create a table for segment lengths of 2,000, 20,000 and 200,000 nucleotides at a constant one-in-a-million modeled residual copying-error probability. The no-error probabilities are approximately 99.80, 98.02 and 81.87 percent. That progression makes visible the cumulative effect of many small independent risks. It does not imply that almost one in five long replicated segments will be recovered as a permanent mutant molecule after all repair stages. Suppose a sample is sequenced at high depth and one position has a few variant-supporting reads. A simple binomial copying model is insufficient because the reads may originate from duplicated molecules or systematic base-call artifacts. Use unique molecular identifiers, matched controls and independent templates to estimate measurement error. For a true biological interpretation, identify the step at which an event becomes heritable, and state which repair and selection processes take place before sequencing.
