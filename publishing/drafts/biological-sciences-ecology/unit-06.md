# Unit 06 — Field methods, experiments and inference

> Design representative surveys, control bias, address uncertainty and reproduce evidence.

## Learning goals

For field methods, experiments and inference, explain the processes described in this unit, identify suitable observational and experimental units, connect synthetic numerical cases to physical measurements, and distinguish competing mechanisms. In the context of design representative surveys, control bias, address uncertainty and reproduce evidence., state how variation in sampling effort, habitat, time or model assumptions could change the result. Interpret quantities with units and identify the evidence required before applying results to a real management decision.

## Conceptual foundation

### Ecological methods are part of the scientific claim

Reliable field ecology depends on questions that can be answered with realistic sampling and an explicit counterfactual. A study claiming that fertilizer increases wetland productivity must distinguish the experimental unit from the measurement sample. If fertilizer is applied to one lake and ten water samples are analyzed, there is one fertilized lake, not ten independent treatment replicates. Subsamples can improve precision about that lake, but they do not estimate variation across separate lakes. True replication requires treatment applied to independently comparable experimental units, subject to the physical constraints and ethical permissions of the system.

Randomization helps prevent systematic placement of treatments in better habitats, while blocking can account for known heterogeneity such as altitude or initial vegetation cover. Control plots can themselves be affected by treatment spread through water or mobile organisms, so interference must be considered. Observational studies are sometimes the only ethical or practical option; a cyclone cannot be randomly assigned to coastlines. Then careful before-after monitoring, comparison sites and transparent assumptions become essential. Advanced statistical analyses cannot recover an absent baseline or invent an unobserved control world without assumptions.

Detection bias has distinct consequences. A wildlife survey may record zero animals where the species is present but quiet or concealed. Repeated visits allow simple occupancy models to separate latent site presence from detection chance, provided the population does not change status during the survey window and false positives are limited or modeled. Equal effort and fixed conditions may still fail when detection depends strongly on wind, season or observer. Recording these covariates can matter more than the number of observations. The same issue appears in botany when plants are easier to identify during flowering.

Spatial design controls representativeness. A random quadrat is only random relative to a specified sampling frame; excluding steep or inaccessible habitat without documentation changes what can be inferred. Stratification by habitat type can improve estimates when vegetation varies sharply across a reserve. Weighted averaging is then required if strata occupy different fractions of area. Transects provide useful coverage but can align with ecological gradients or human paths, affecting inference. Map sampling units, report the inclusion rule, and distinguish design-based population estimates from predictions at unsampled sites.

Analytical uncertainty includes sampling variation, instrument noise, temporal process change and structural model error. A narrow confidence interval from a model that assumes independent samples can be misleading when observations are strongly spatially correlated. An ecological effect can be statistically detectable yet too small to alter a management decision. Conversely, a large uncertain effect can merit additional data collection before a costly intervention. Graphs should display raw units, uncertainty definitions and the decision threshold where relevant. Models should be validated across independent sites or seasons rather than only random rows extracted from the same spatial cluster.

Reproducibility and ethics conclude the measurement chain. Keep raw observations immutable, document transformations, state the version of analytical software, and distinguish synthetic teaching data from field records. Sensitive coordinates for threatened organisms may need controlled access or deliberate generalization. Local communities may hold legitimate knowledge and rights that a public dataset cannot override. Permissions, ecological disturbance and safety constrain field experiments. A modest transparent analysis can be scientifically stronger than an opaque elaborate model if another researcher can understand how data were gathered, corrected and interpreted.

## Five focused topics with worked examples

### 6.1 Experimental design, randomization and replication

#### Ecological concept and mechanism

An ecological experiment contrasts treatments against a defensible counterfactual. Random assignment reduces systematic bias, while biological replication ensures variation can be estimated at the level at which treatment is applied.

Experimental units may be plots, streams, enclosures or lakes; subsamples within one unit improve measurement precision but do not create new independent treatment replicates.

#### Worked interpretive case

Applying fertilizer to one lake and measuring ten water samples does not yield ten treated lakes. A separate untreated lake helps but site differences still threaten causal inference.

#### Evidence and study design

Identify the assignment unit before analysis, randomize treatments where practical and account for blocks such as soil type or elevation. Preregister the primary response and data-exclusion rules for large projects.

Redesign a pseudo-replicated restoration experiment with adequate comparable plots and clear treatment boundaries.

#### Critical limitations and transfer

Spatial spillovers, interference and shared weather can violate independence. Randomization does not repair biased measurements or an intervention applied to only one landscape.

Transparent design choices matter more than complex statistical machinery applied after weak sampling.

#### Worked quantitative example 6.1: Coefficient of variation

**Synthetic data.** Five equal-effort plot replicates give a hypothetical mean biomass 15 grams and sample standard deviation 3 grams.

**Derivation and solution.** Compute the dimensionless coefficient of variation as standard deviation divided by mean. The explicit calculation `3/15` gives **0.2 coefficient of variation**. Identify how the input variables were defined before applying the same arithmetic to new measurements; the result is conditional on that definition.

**Ecological interpretation.** A value of 0.2 summarizes relative spread for positive-scale measurements.

**When the computation would mislead.** With zero or negative means the coefficient may be unstable or meaningless, and spatial autocorrelation can affect variance estimates. For field applications, compare the precision of the input measurements with the apparent precision of the answer, then decide whether model structure or sampling error is likely to dominate uncertainty.

**Independent check and extension.** Compare the coefficient across two habitats with very different means and sample sizes. Recalculate with one altered input and describe the observation that would justify changing that parameter in a real ecological study. Distinguish recalculating an illustrative equation from experimentally validating the biological relationship.


### 6.2 Observation, detectability and occupancy models

#### Ecological concept and mechanism

Imperfect detection means a site may be occupied even when a survey records no organism. Repeated surveys under suitable closure assumptions can help estimate detection separately from occupancy.

In a simple single-season framework, occupancy probability psi governs presence, while detection probability p governs whether an occupied site yields a detection on a visit. Distinct observation histories inform the two processes.

#### Worked interpretive case

No frogs are heard during a windy evening although animals are present, creating an apparent decline if windier sites are surveyed later in the season.

#### Evidence and study design

Survey sites repeatedly within a period where occupancy is plausibly unchanged and record wind, temperature, observer and effort. Fit detection covariates as appropriate.

Calculate probability of at least one detection in three visits for an occupied site with fixed p.

#### Critical limitations and transfer

If animals move into or out of sites between visits, a closed occupancy model is misspecified. False positives and misidentification require additional treatment.

Citizen-science data become more informative when reporting effort and detection conditions accompany sightings.

#### Worked quantitative example 6.2: Repeated-detection probability

**Synthetic data.** Detection probability on one visit is 0.4 if a species occupies a site, with three conditionally independent visits.

**Derivation and solution.** Probability of at least one detection equals one minus the probability of missing the animal on all three visits. The explicit calculation `1-(1-0.4)**3` gives **0.784 conditional detection probability**. Identify how the input variables were defined before applying the same arithmetic to new measurements; the result is conditional on that definition.

**Ecological interpretation.** A 0.784 chance of one or more detections holds only under the stated assumptions.

**When the computation would mislead.** Detection often depends on weather and observer, and repeated presence is not guaranteed if occupancy changes. For field applications, compare the precision of the input measurements with the apparent precision of the answer, then decide whether model structure or sampling error is likely to dominate uncertainty.

**Independent check and extension.** Recalculate for one or five visits and discuss the diminishing return of repeated sampling. Recalculate with one altered input and describe the observation that would justify changing that parameter in a real ecological study. Distinguish recalculating an illustrative equation from experimentally validating the biological relationship.


### 6.3 Transects, quadrats and spatial sampling

#### Ecological concept and mechanism

Transects and quadrats convert landscapes into measurable sampling frames. Design-based inference depends on how units were selected and whether inclusion probabilities are known.

Systematic grids capture broad structure but may align with periodic habitat features; random and stratified samples can support explicit area-weighted estimation. Distance sampling adds detectability assumptions.

#### Worked interpretive case

A wetland survey oversamples accessible boardwalk edges and reports too many edge-associated plants relative to the whole wetland.

#### Evidence and study design

Map strata and allocate quadrats using area and variance considerations. Record excluded sites and access limitations; use georeferenced points without exposing sensitive species locations publicly.

Calculate weighted vegetation cover from unequal habitat strata, comparing it with an unweighted average.

#### Critical limitations and transfer

Sampling only along roads or trails can create strong selection bias. Correlation among nearby quadrats affects effective sample size.

A carefully documented sampling frame is as important as the statistical test used afterward.

#### Worked quantitative example 6.3: Stratified cover estimate

**Synthetic data.** Two strata cover 20 and 80 percent of a reserve and have vegetation cover means of 0.30 and 0.70 respectively.

**Derivation and solution.** Weight each cover estimate by the corresponding share of total area. The explicit calculation `0.2*0.3+0.8*0.7` gives **0.62 area-weighted cover fraction**. Identify how the input variables were defined before applying the same arithmetic to new measurements; the result is conditional on that definition.

**Ecological interpretation.** The reserve-wide estimate is 0.62; the unweighted mean would misrepresent strata of unequal sizes.

**When the computation would mislead.** A representative stratum sample and correct area estimates are still necessary. For field applications, compare the precision of the input measurements with the apparent precision of the answer, then decide whether model structure or sampling error is likely to dominate uncertainty.

**Independent check and extension.** Assess how the result changes if the smaller stratum's cover drops to zero. Recalculate with one altered input and describe the observation that would justify changing that parameter in a real ecological study. Distinguish recalculating an illustrative equation from experimentally validating the biological relationship.


### 6.4 Uncertainty, model selection and causal interpretation

#### Ecological concept and mechanism

Confidence intervals, predictive distributions and sensitivity analyses address different uncertainties. Models are simplified hypotheses, not verdicts, and their parameters may be poorly identifiable from available data.

Measurement error, process variation, sampling uncertainty and structural model mismatch enter at different stages. Independent validation tests whether fitted relationships travel to new sites or periods.

#### Worked interpretive case

A regression links stream nitrate concentration to algal biomass but both vary with discharge, making a simple positive coefficient difficult to interpret causally.

#### Evidence and study design

Plot residuals, examine confounders and compare plausible models chosen before viewing outcomes when possible. Hold out independent sites or years, not random samples from the same autocorrelated series.

Describe a result that is statistically detectable but too small to matter for habitat management, and the reverse.

#### Critical limitations and transfer

A narrow interval from a misspecified model can create false confidence. P-values and information criteria do not measure ecological importance on their own.

Model evaluation should ask what decision changes under the remaining uncertainty.

#### Worked quantitative example 6.4: Approximate interval upper bound

**Synthetic data.** A model parameter estimate is 20 with an approximate standard error of 2 and a symmetric normal interval approximation is assumed.

**Derivation and solution.** Compute the upper 95 percent bound as estimate plus 1.96 standard errors. The explicit calculation `20+1.96*2` gives **23.92 upper confidence bound units**. Identify how the input variables were defined before applying the same arithmetic to new measurements; the result is conditional on that definition.

**Ecological interpretation.** The resulting bound is 23.92 in the original parameter units under normal approximation.

**When the computation would mislead.** An interval from a biased or misspecified model will not fix those errors; bounded or skewed estimates need other methods. For field applications, compare the precision of the input measurements with the apparent precision of the answer, then decide whether model structure or sampling error is likely to dominate uncertainty.

**Independent check and extension.** Calculate the lower limit and explain why a confidence interval is not the probability the parameter lies within it. Recalculate with one altered input and describe the observation that would justify changing that parameter in a real ecological study. Distinguish recalculating an illustrative equation from experimentally validating the biological relationship.


### 6.5 Open data, reproducibility and ethical fieldwork

#### Ecological concept and mechanism

Reproducible ecology requires traceable data provenance, analytical code, measurement units and ethical treatment of organisms and communities. Openness must be balanced with privacy, Indigenous rights and sensitive habitat protection.

A reproducible pipeline preserves raw inputs, documents transformations and fixes software versions or seeds. Field metadata record collection conditions, while permissions govern legitimate re-use and location disclosure.

#### Worked interpretive case

A dataset lists 400 records without observer, time zone or sampling method. Even if numerical values are correct, later analysts cannot separate ecological changes from shifting effort.

#### Evidence and study design

Create a data dictionary, timestamp standard, licensing notes, code repository and a decision log for exclusions. Archive generalized public coordinates when exact localities endanger protected organisms.

Write a minimum metadata checklist for a biodiversity survey that could be reproduced next year by another team.

#### Critical limitations and transfer

A shared spreadsheet without version history can obscure corrections. Consent to field access does not automatically authorize publication of cultural knowledge or private property details.

Scientific transparency includes acknowledging limitations and respecting local expertise, not simply publishing all raw coordinates.

#### Worked quantitative example 6.5: Metadata completeness

**Synthetic data.** A survey archive contains 400 field records, 280 of which contain the required site, date, method and effort fields.

**Derivation and solution.** Divide records with complete required metadata by all records. The explicit calculation `280/400` gives **0.7 fraction of records complete**. Identify how the input variables were defined before applying the same arithmetic to new measurements; the result is conditional on that definition.

**Ecological interpretation.** Completeness of 70 percent flags a data-management problem separate from ecological trends.

**When the computation would mislead.** Some missing metadata may be concentrated in earlier years, biasing time-series results. For field applications, compare the precision of the input measurements with the apparent precision of the answer, then decide whether model structure or sampling error is likely to dominate uncertainty.

**Independent check and extension.** Propose a validation rule for future records that cannot be completed without key effort details. Recalculate with one altered input and describe the observation that would justify changing that parameter in a real ecological study. Distinguish recalculating an illustrative equation from experimentally validating the biological relationship.


## Integrated computational and observation-design laboratory 6: Sampling effort, bias and repeatability

### Research aim and study system

Compare systematic roadside quadrats with a stratified random sample covering upland and marsh habitat; give all observations effort metadata. This is an educational, entirely synthetic exercise for readers without laboratory equipment. Its case is **occupancy and quadrat survey redesign**, represented by **a mosaic of accessible paths, marsh interiors and upland grassland plots**. The key quantities to observe are **detection, stratum area and sampling effort**. The question is not simply whether two columns differ: it is whether the chosen evidence can **avoid treating repeated observations as independent treatment replicates**. State the central alternative before generating any synthetic measurements. Otherwise changes in a plot can be explained after the fact without a meaningful test.

### Data dictionary and reproducibility requirements

Provide one row per actual study unit or visit, depending on the stage of measurement, and include explicit identifiers. Document **randomization unit and visit-level metadata**; also retain location class, date, survey duration, method version and a reason when data are missing. Define every unit, including degrees of temperature, area, individual counts or mass-per-time flux. Use distinct codes for zero, unobserved and not applicable. A table in which no organisms were seen despite valid sampling is not equivalent to a table in which a site was never visited. Save a read-only raw dataset and a second transformed dataset alongside a reproducible calculation log.

The book contains a synthetic example dataset for this unit under `datasets/lab-06.csv`. It illustrates a stable column structure rather than empirical evidence; its numerical values and site labels are invented. Review whether the input data are logically coherent before fitting any equation. A physically impossible concentration or a date outside the sampling window should trigger validation. Record any corrected values and preserve the originals so another reader can explain every change.

### Procedure

1. **Specify hypotheses.** Choose one explanatory process drawn from **experimental design, randomization and replication** and a serious competing explanation related to **transects, quadrats and spatial sampling**. Describe the response variable and whether the process predicts an increase, decrease, threshold or no change. Include a null pattern that could plausibly arise through sampling variation.
2. **Establish comparability.** Match sites, periods, effort or experimental units appropriately. If the study uses simulated random assignment, preserve the random seed and show treatment balance. Do not treat several measurements from one habitat block as independent blocks. Explain how space, time and shared weather might introduce dependence even under a seemingly random scheme.
3. **Explore the data.** Construct a scatterplot or time series with labeled axes, raw points and explicit group names. Report sample size at the actual experimental or observational-unit level. Inspect non-detections and extreme values, but do not delete observations solely because they contradict the initial hypothesis.
4. **Calculate and compare.** Calculate a weighted abundance or cover estimate, then perform a sensitivity check for incomplete detection. Check arithmetic using two methods—a spreadsheet and a manual calculation, for example. Explain what part of the comparison was identified by a definition and what part required a model assumption. A graph that looks smooth does not demonstrate the validity of a causal pathway.
5. **Stress-test the conclusion.** Change one defensible parameter or data-quality rule: detection probability, sampling area, rate assumption, autocorrelation or reference choice. Recompute the principal estimate. If a moderate alteration reverses the sign or action threshold, present both outcomes and recommend improved measurement before a high-cost decision.
6. **Interpret with an alternative.** Compare the leading mechanism with the explicitly named rival. Propose a new independent measurement that would discriminate them. Include uncertainty and an ethical or logistical limitation. If results are inconsistent, label the result unresolved instead of inventing an unobserved pathway to rescue a favorite hypothesis.

### Results discussion and expected reasoning

The exercise contains no prespecified discovery. Its purpose is to make plausible ecological stories answerable through measurements. Explain how **observation, detectability and occupancy models** may affect a predicted outcome while **uncertainty, model selection and causal interpretation** can change the interpretation. Where the calculation involves probability, distinguish conditional probabilities from frequencies over repeated independent systems. Where a budget is calculated, distinguish flow rates from stocks and sum only compatible quantities. Where a management action is proposed, separate the number of actions implemented from the measured response of the ecosystem.

Do not record locations of endangered species in public datasets without qualified approval. Report the synthetic status prominently. If a model produces an impossible value, do not silently truncate it unless the modeling rule explicitly requires a bound. Instead identify the biological restriction omitted by the simple equation. Some ecological systems can have alternative stable trajectories or long lag times, but neither should be claimed from the dataset without specific evidence.

### Deliverables, assessment and extension

Submit an annotated data dictionary, an analysis script or spreadsheet formula log, two labeled figures, one complete hand-worked numerical calculation and a one-page discussion with prediction, result, competing explanation and limitation. Include a paragraph on reproducibility and any constraints on safe field transfer. For extension, choose **open data, reproducibility and ethical fieldwork** as a new potential driver and design a minimally more informative follow-up study. Explain the number and kind of genuinely independent replicates that would be needed for a small pilot, rather than declaring arbitrary sample sizes statistically adequate.


## Unit 6 synthesis and critical assessment

1. **Mechanism map.** Relate Experimental design, randomization and replication to Uncertainty, model selection and causal interpretation. Mark the measured processes, their directions and the place where a biological outcome could be changed by an unobserved driver. Repair a pseudo-replicated study by identifying independent units.
2. **Rival explanation.** A report concludes that observation, detectability and occupancy models must be responsible for a mapped pattern. Identify an environmental or measurement-based alternative, an observation consistent with both, and an independent comparison that could distinguish them.
3. **Quantitative audit.** Reconstruct all five examples in this unit without looking at the displayed result. Check units and dimensions, identify the reference value, and vary an input by ten percent. Record the effect size and the meaning of a negative, zero or unexpected result where applicable.
4. **Evidence review.** Examine a hypothetical study with four sites, two of them treated and two untreated, where investigators repeated twenty subsamples at every site. Explain why there are four independent site-level units, then discuss what additional temporal and spatial controls would strengthen the inference. Adjust the explanation if treatment spills between adjacent sites.
5. **Transfer and limits.** Explain how imperfect detection can masquerade as abundance decline. Draft a concise comparison of how the model's assumptions change when moved from the constructed teaching scenario to a coastal, urban, agricultural or protected-area system. Explicitly indicate which ecological outcomes need long-term monitoring.
6. **Research communication.** Write a 500-word mini-review of two concepts from the unit, distinguishing established general mechanisms from synthetic calculations and uncertain real-world consequences. Cite at least one reliable open textbook or scientific reference, and state exactly which claim the reading supports. An external reference is not an endorsement of the OpenSTEM draft.

