# Unit 05: Phylogenetic inference and comparative analysis

> Reading trees, modeling gene histories, estimating dates and comparing traits with ancestry in view.

## Learning outcomes

By the end of this unit, the reader should be able to investigate phylogenetic inference and comparative analysis, interpret a relevant quantitative model, design a realistic test that controls for alternative explanations, and state the principal limits of the inference. An intellectually satisfactory answer can remain uncertain when the data do not discriminate among mechanisms.

## Integrative foundation

### Trees are hypotheses with branches, not ladders

Trees compress a large amount of historical information into nodes and edges. A tip is a sampled lineage or sequence, not an evolutionary endpoint ranked above another. Internal nodes denote hypothetical ancestors or branching events, while polytomies express unresolved or closely spaced divergence. Rotating descendants around a node does not alter who shares a most recent common ancestor. Students who evaluate relationship by left-right order or visual height can reach the wrong conclusion even when they can recognize every name on the figure.

The interpretation of branch lengths must also be stated. A cladogram may show branching order without proportional distances. A phylogram can express estimated substitutions, while a chronogram represents temporal scaling under a clock model. A branch with many estimated substitutions may not represent a longer elapsed period if substitution rates vary. Good figures state the root method, units, sampling and uncertainty rather than rely on attractive branch styling.

### Gene histories are not always organism histories

Constructing a tree begins before algorithm selection. Collect orthologous sequences, verify that names and sample locations are correct, inspect alignments and remove low-quality regions using predefined criteria. A pipeline can process thousands of loci and still be systematically wrong if hidden paralogs, contamination, extreme base composition or unbalanced sampling persist. A maximum-likelihood model provides a statistically explicit framework, but numerical support is conditional on its assumptions. A high bootstrap value after fitting a poor model is not a measure that the entire historical story is nearly certain.

In rapidly diverging lineages, ancestral gene variants can survive through more than one speciation event. Different descendant species can inherit them in ways that yield gene trees inconsistent with the simplest species tree. This incomplete lineage sorting is not necessarily an analytical failure. Introgression, gene conversion and duplication can add further discrepancies, requiring methods matched to the process. A responsible paper reports concordance, branch-support distributions and alternate plausible relationships instead of suppressing inconvenient loci.

### Quantitative comparative inference

Comparative biology often asks whether two traits evolved together, such as environmental temperature and body size or dispersal type and geographic range. Species are not independent statistical observations because close relatives inherited many characteristics from shared ancestors. A regression treating all tips as fully independent can exaggerate effective sample size. Methods such as phylogenetic generalized least squares or independent contrasts account for covariance under a specified model, but they still cannot turn correlation into definitive causality.

Ancestral-state reconstruction has related limits. It estimates plausible ancestral traits conditional on tips, tree and transition assumptions. If extinct branches are missing, very different histories may fit present species. Test whether results change with alternative trees, branch lengths and transition rates. Report posterior distributions or model comparisons where possible, and distinguish a model-supported ancestral state from a directly observed fossil characteristic.

## Focused studies and worked problems

### 5.1 Reading rooted and unrooted phylogenetic trees

#### Core idea and causal mechanism

A phylogenetic tree is a hypothesis about common descent. Rotating branches around a node does not change topology; ordering tips from left to right is not a scale of evolutionary advancement.

A root indicates the direction of ancestry; unrooted relationships do not specify where the common ancestor of all shown taxa lies. Branch lengths may represent changes, time or nothing depending on annotation.

#### Example in biological context

If birds and crocodilians share a more recent common ancestor than either shares with lizards, rotating the bird/crocodilian branches will not change that claim. A decorative ladder layout can conceal these equivalent forms.

#### Evidence and a workable test

Re-draw the same four-tip topology several ways, label its clades and map one independent character. Ask learners to identify sister groups by nodes rather than by horizontal proximity.

**Investigation prompt.** Reconstruct the same topology with branches rotated and label sister relationships without reading order on the page. Note whether branch lengths mean time, sequence substitutions or purely visual spacing.

#### Where the inference could fail

An outgroup that is too distant may distort inference through long-branch attraction. Polytomies can indicate insufficient resolution or actual closely timed branching and should not be falsely resolved.

Compare two models fitted to the same alignment and identify what evidence would remain unresolved. A numerical support value should not be presented as a probability of the entire evolutionary narrative.

#### Apply and question

Compare two trees with matching tip orders but different connecting edges. Describe why a tip sequence is insufficient to establish topology.

Tree-reading literacy is essential for interpreting pathogen sequences, biodiversity priorities and ancestral trait reconstructions.

Can an extant chimpanzee be described as an ancestor of a living human? Explain the distinction between an extant sister lineage and the ancestor they share. Your answer should include a prediction that differs between hypotheses and state which assumptions would remain untested after the observation.

#### Quantitative case 5.1: Tree tips and rooted binary nodes

**Assumed data (synthetic).** A fully resolved rooted binary tree has seven terminal species.

**Calculation.** Calculate its total internal branching nodes, n-1. Substituting the stipulated values into `7-1` gives **6 internal nodes**. Confirm the result independently and retain consistent units.

**Interpretation.** There are six internal nodes in this representation, not six necessarily observed ancestral fossils.

**Model limitation.** Polytomies and multiple samples per species change how trees are represented.

**Try next.** Why does rotating branches about an internal node leave this count unchanged? Show the derivation and distinguish the numerical result from any proposed biological cause.


### 5.2 Alignments, models and phylogenetic inference

#### Core idea and causal mechanism

Phylogenetic inference integrates explicit data with assumptions about how sequences or morphological characters change. Parsimony, likelihood and Bayesian frameworks answer related but not identical questions.

Substitution models account for different rates and possible base-frequency biases; likelihood scores quantify fit of a tree and its branch lengths to a specified model. Bayesian inference combines likelihood with priors and samples posterior uncertainty.

#### Example in biological context

A fast-evolving microbial locus may produce spurious similarity by convergent nucleotide composition. Adding a slower locus can improve inference if true orthology and alignment are verified.

#### Evidence and a workable test

Inspect alignment coverage, remove questionable sequence fragments using transparent criteria, compare reasonable models and record branch support from appropriate procedures.



#### Where the inference could fail

High bootstrap support does not establish the correctness of an alignment, a model or taxon sampling. A gene tree can disagree with the species history because of biology rather than computational error.



#### Apply and question

Explain the purpose of a null model, a rate model and a support statistic. Draft a minimal analysis plan for 20 sampled taxa and three independently inherited loci.

Robust phylogenies underpin comparative genomics and taxonomy, but computational precision must not be mistaken for certainty about historical processes.

When do more aligned sites make a biased analysis more confident rather than more accurate? Propose a diagnostic for saturation or compositional heterogeneity. Your answer should include a prediction that differs between hypotheses and state which assumptions would remain untested after the observation.

#### Quantitative case 5.2: Likelihood-ratio statistic

**Assumed data (synthetic).** For illustrative models, fitted log-likelihoods are -1250 and -1241.

**Calculation.** Compute twice the improvement in log-likelihood, 2(LL_advanced-LL_simple). Substituting the stipulated values into `2*(-1241+1250)` gives **18 likelihood-ratio statistic**. Confirm the result independently and retain consistent units.

**Interpretation.** The statistic is 18, but its reference distribution depends on nesting, boundary parameters and other assumptions.

**Model limitation.** Do not report a p-value without establishing the appropriate null distribution.

**Try next.** What model diagnostics could matter more than a large likelihood improvement? Show the derivation and distinguish the numerical result from any proposed biological cause.


### 5.3 Gene trees, species trees and discordance

#### Core idea and causal mechanism

Different gene regions can have distinct genealogies even when species relationships are well defined at a broader scale. Incomplete lineage sorting and gene flow are prominent biological sources of discordance.

An ancestral polymorphism may persist through successive speciation events and sort differently in descendant species. Introgression transfers alleles after divergence; gene duplication creates another category of mismatch if paralogs are confused.

#### Example in biological context

During a rapid radiation, many nuclear loci may support different trees. An organism's species history is not a literal average of its genes, and a single mitochondrial region may provide an incomplete picture.

#### Evidence and a workable test

Compare distributions of trees across unlinked loci, examine concordance factors and use methods that explicitly model ancestral polymorphism when assumptions are plausible.



#### Where the inference could fail

Very few informative sites, gene conversion and alignment error can also generate discordance. Treat disagreement as a result to explain, not an embarrassment to hide.



#### Apply and question

Draw an ancestral population with two alleles persisting across a branching event. Trace two distinct genealogies compatible with the same species tree.

Wildlife management and infectious-disease inference both benefit from separating movement of genes from movement of organisms and from acknowledging uncertainty.

If every locus produces a different tree, which sample design questions would you ask before invoking complex new evolutionary mechanisms? Your answer should include a prediction that differs between hypotheses and state which assumptions would remain untested after the observation.

#### Quantitative case 5.3: Gene-tree discordance share

**Assumed data (synthetic).** Among 200 adequately supported loci, 130 favor topology A and 70 favor alternative topologies.

**Calculation.** Calculate the proportion supporting A. Substituting the stipulated values into `100*130/200` gives **65 percent**. Confirm the result independently and retain consistent units.

**Interpretation.** Sixty-five percent support across loci indicates heterogeneity, not a 65-percent probability that the species tree is A.

**Model limitation.** Locus independence and selection of high-support gene trees influence the summary.

**Try next.** What does a concordance factor capture that concatenated bootstrap percentage may hide? Show the derivation and distinguish the numerical result from any proposed biological cause.


### 5.4 Molecular clocks and dating divergence

#### Core idea and causal mechanism

Sequence differences can accumulate over time, but molecular clocks need calibration and assumptions about rates. A dated tree is an estimated distribution of histories, not a precise timetable of origin events.

A strict clock imposes one rate on the selected sequences; relaxed-clock approaches allow variation among branches. Fossil or geological calibrations need explicit priors and defensible placement.

#### Example in biological context

Two sister groups with different generation times may have different substitution rates per year. An unusually old estimated divergence can signal calibration mismatch or model inadequacy rather than a surprising event.

#### Evidence and a workable test

Compare strict-clock and relaxed-clock outputs, perform a calibration sensitivity analysis and show date intervals rather than a single falsely exact value.



#### Where the inference could fail

The oldest fossil assigned to a clade generally sets a minimum age, not its exact origin. Sequencing more genes cannot independently fix a poorly justified calibration.



#### Apply and question

Compute an elementary substitution-distance estimate using an assumed rate, then explain why saturation, rate variation and uncertain ancestral states limit the calculation.

Time-scaled trees let researchers relate diversification to geological or climatic events, provided coincidence is not presented as proof of causation.

How would a newly validated older fossil change a time-calibrated phylogeny? Distinguish a bound violation from a small shift within a prior interval. Your answer should include a prediction that differs between hypotheses and state which assumptions would remain untested after the observation.

#### Quantitative case 5.4: Elementary clock estimate

**Assumed data (synthetic).** An assumed two-lineage sequence distance is 0.04 substitutions per site and rate r=0.002 substitutions per site per million years on each lineage.

**Calculation.** Under a strict, equal-rate model, T=d/(2r). Substituting the stipulated values into `0.04/(2*0.002)` gives **10 million years**. Confirm the result independently and retain consistent units.

**Interpretation.** The ten-million-year estimate is purely illustrative and depends directly on the stipulated rate and corrected distance.

**Model limitation.** Saturation and uncertainty in the calibration broaden the plausible times.

**Try next.** How does the estimate change if the assumed rate doubles? Show the derivation and distinguish the numerical result from any proposed biological cause.


### 5.5 Ancestral-state and comparative methods

#### Core idea and causal mechanism

Mapping trait values onto a tree helps distinguish history from independent ecological responses. Related species are not statistically independent replicates simply because they occupy separate rows in a dataset.

Parsimony or model-based ancestral-state reconstruction estimates likely changes given the tree and model; phylogenetic comparative methods account for expected covariance under specified trait-evolution processes.

#### Example in biological context

Large body size appears in multiple mammalian branches, sometimes under distinct ecological pressures. Treating all species as independent can inflate apparent support for environmental relationships.

#### Evidence and a workable test

Code traits under clear definitions, compare alternative trees, model measurement error and perform sensitivity analyses under different trait-evolution assumptions.



#### Where the inference could fail

Reconstructed ancestral traits can be uncertain or nonidentifiable, particularly when only living tip species are sampled. Correlation between two traits does not establish one caused the other.



#### Apply and question

Explain why adding a close relative is not equivalent to adding an independent evolutionary origin of a trait. Suggest a comparative analysis using replicated origins across the tree.

Comparative inference supports studies of host shifts, life-history variation and evolutionary constraints, with statistical controls for shared ancestry.

Could a trait appear ancestral under one reconstruction and derived under another? Identify how tip sampling, branch lengths and transition models affect the answer. Your answer should include a prediction that differs between hypotheses and state which assumptions would remain untested after the observation.

#### Quantitative case 5.5: Independent trait transitions

**Assumed data (synthetic).** Trait mapping on a model tree supports five separate origins and two losses.

**Calculation.** Add origins and losses for a minimum total of scored transitions. Substituting the stipulated values into `5+2` gives **7 transitions**. Confirm the result independently and retain consistent units.

**Interpretation.** A minimum of seven transitions is a parsimony-style summary, not proof that the actual number was seven.

**Model limitation.** Hidden transitions and uncertainty at internal nodes may increase the inferred number.

**Try next.** How would a stochastic transition model express uncertainty differently? Show the derivation and distinguish the numerical result from any proposed biological cause.


## Integrated investigation 5: Stress-testing a small phylogenetic dataset

**Research aim.** Compare tree hypotheses under changes in alignment, outgroup selection and rate models, using entirely synthetic sequence data. The investigation is designed for an introductory undergraduate seminar or computational laboratory; its specimens, dates, counts and measurements are hypothetical. Do not represent any result as a published empirical discovery.

### Materials, assumptions and ethical boundaries

Four ingroup taxa, two outgroups of different divergence, five orthologous simulated loci, and annotations for ambiguous alignment columns. Use a spreadsheet or local script to create tables and plots, recording pseudorandom seeds if stochastic simulations are used. Collect no personal genetic data. Do not culture pathogens, collect protected wildlife, disturb habitats or undertake medical tests. Where the real-world analog requires permits, trained staff or ethical approval, use simulation or openly available teaching data instead.

### Step-by-step procedure

1. For **stress-testing a small phylogenetic dataset**, define biological units, sampling frame, time coordinate and outcome variables. Write the competing hypotheses as distinct predictions: Compare tree hypotheses under changes in alignment, outgroup selection and rate models, using entirely synthetic sequence data. A generic statement that 'evolution occurs' is not a testable outcome.
2. Assemble the synthetic input table and verify totals. For counts, check whether each observation represents an individual, gene copy, fossil occurrence or independent lineage. For traits, specify scale and units. Leave missing observations explicitly missing rather than silently substituting zero.
3. Produce a first visualization with individual values visible when practical. Include replicates, not only a pooled mean. Label assumptions, treatment groups and what uncertainty is shown; error bars without a stated definition are ambiguous.
4. Recalculate the outcome after changing one defensible assumption: sampling effort, effective size, migration, branch rate or measurement error, as appropriate. The change in conclusion is a sensitivity result, not a failure of the exercise.
5. Write a short report separating observation, model, interpretation and limitation. Include a figure caption, a reproducibility note and one proposed independent test.

### Expected reasoning, not prescribed results

A correctly implemented analysis can still be unstable when informative sites are few or substitution model assumptions fail. In this synthetic scenario, a strongly supported locus tree conflicts with the majority of other unlinked loci. Resist presenting a single calculated value as the only outcome consistent with the mechanism. Explain what a failed prediction would require you to reconsider: an incorrect method, an unrealistic assumption or a genuinely unsupported biological hypothesis. Negative results are informative when sampling was capable of detecting the predicted difference.

### Troubleshooting the inference

Read a tree through branching nodes, not tip positions. When discussing trait evolution, remember that related species contribute correlated evidence and that ancestors reconstructed from modern tips are model-based estimates. Pseudoreplication is a major threat when multiple measurements from one biological unit are treated as independent organisms or populations. Similarly, sampling several fossils from one well-exposed outcrop may not represent equal coverage across geological intervals. Identify the true replication unit and justify the comparator. If simulations use the same seed or parameter configuration, discuss whether the apparently repeated outcome is truly independent.

### Submission and further questions

Submit a hypothesis table, methods summary, results figure with labeled axes, numerical worked example, explanation of assumptions and a 150-word limitations statement. How would you distinguish a genuine gene-history discordance from contamination or paralogy? For extension, describe one observation that would distinguish the leading hypothesis from a realistic competing mechanism, and state how much uncertainty would remain even if that observation agreed with the prediction.


## End-of-unit integrative assessment

1. Construct a concept map linking **Reading rooted and unrooted phylogenetic trees** and **Gene trees, species trees and discordance**. Each connecting arrow must be labeled with a measurable or historically constrained mechanism, not a vague phrase such as 'related to'. Include at least one causal hypothesis and one statement of historical relationship.
2. Contrast **Alignments, models and phylogenetic inference** with **Ancestral-state and comparative methods**. Describe a plausible observational pattern compatible with both, then design a new measurement that would make their predictions diverge. State your relevant biological unit and justify how many independent replicates you would need for a preliminary test.
3. Reproduce all five solved quantitative cases from this unit without viewing their answers. Change one parameter in each case, label units and explain whether the biological conclusion is sensitive to the change. A model calculation is not a field observation.
4. Evaluate a hypothetical paper claiming that **molecular clocks and dating divergence** has been conclusively demonstrated from a small unreplicated dataset. Draft a respectful scientific response explaining the most serious limitation, a rival mechanism, and a feasible next step.
5. Prepare a 600-word mini-review integrating chronology or inheritance, mechanism and evidence for two topics of your choice. Define your terminology precisely, distinguish observed data from inferred history and cite a credible external scientific source. Close with a statement of what remains unknown.

**Self-check rubric for this unit.** When writing about **reading rooted and unrooted phylogenetic trees** or **molecular clocks and dating divergence**, identify a defined population or lineage, give a defensible observation, show appropriate units or character coding and distinguish the leading hypothesis from a competitor. Evaluation rewards testable reasoning and candid limitations rather than memorization of a favored interpretation.

