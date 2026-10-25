# Unit 04 — Biodiversity observation and inference

> **Book 18 / undergraduate editorial draft**. All numerical cases in this book are invented for classroom use. Independent academic review is pending.

## Core unit inquiry

**Question:** How can scientists detect real ecological trends when organisms and habitats are imperfectly observed?

**Bounded setting:** sampling frames, repeat visits, traceable identity and measured detectability. **Fictional running setting:** a fictional wetland observation network using field plots and sensors. The five lessons share the conceptual aim of following an ecological claim from biological mechanism to measurement, inference and a justifiable decision. Data volume does not repair selection bias, and additional detections do not necessarily mean additional organisms. The emphasis is neither pessimism nor optimism; it is disciplined reasoning about actions that influence living systems over time.

Conservation monitoring relies on observations that are imperfect. Organisms hide, migrate, vocalize seasonally or become less active under different conditions. Observers change methods, satellites change resolution, taxonomy changes, and access biases field sites toward roads and settlements. The resulting data may be abundant and seemingly accurate while describing the wrong population. A carefully specified sampling frame and detection process often matter more than the total number of photographs or sightings.

Sampling, occupancy, mark–recapture, remote sensing and public biodiversity records each have different observation models. Every data product should record its denominator, domain, time, uncertainty and restrictions on sensitive locations. A distinction between ecological condition and raw sensor signal is central: a higher green reflectance index does not certify restoration, just as louder acoustic detection counts do not establish more animals.

Before starting, create a two-column notebook. In the first column write statements that directly follow from a defined observation; in the second place the wider interpretation that needs extra assumptions. At the end of the unit, record which observation would most change your preferred conservation decision. This exercise is deliberately not a ranking of students' values. Its purpose is to make the relationship between observations, inference and public choices explicit.

## Lesson 4.1 — Sampling design and baseline definition

**Guiding question.** How can we distinguish a defensible finding about **sampling design and baseline definition** from a pattern that could arise through an alternative mechanism or a biased sample? The aim is to explain the ecological idea, define an appropriate quantity, reproduce an elementary numerical example, interrogate a counterargument, and connect the evidence to a legitimate practical decision.

### The ecological mechanism and what it predicts

The inferential unit is the sampled population or landscape, and biased placement of plots can defeat careful statistical calculations; baseline choice controls reported change. For this mechanism, identify the biological scale and time interval. Does an observation concern one organism, a local population or regional persistence? Name one observation that could contradict the explanation and distinguish the measured state from its inferred cause.

### A field measurement contract

Define target population, random or stratified site selection, field effort, seasonal timing, sample size and preregistered indicators. Define the sampling unit, eligibility, survey timing and denominators in advance. Keep auditable observations and appropriately restricted provenance so independent analysts can identify sources of bias.

**Methodological lens — comparison across space.** Select at least three independent locations within each management class, describe how sites were chosen and report environmental covariates. Differences between sites may precede the management action; avoid claiming intervention effects from one-time cross-sectional samples. Document how site choice or altered detection could change the measured result.

### Synthetic ecological case and competing interpretation

Volunteers survey accessible roadside wetlands and report higher diversity than an earlier remote-site inventory. This is a fictional case, not a measured local trend. Identify response, suspected driver and an unmeasured common cause. Would the conclusion change if the monitoring method became more sensitive?

**Main interpretive trap.** Convenience samples and changing methods make apparent differences hard to interpret as ecological trends. Name a comparison site and independent indicator that could expose this error. Specify the result that would force revision of the preferred explanation.

### Worked quantitative case: Accessible plot sampling coverage

**Assumed invented input.** Twenty-four randomly selected sites from a defined frame of eighty; design precision is not encoded.

**Expression:** `24/80*100`. **Calculated answer:** **30 % of frame sampled**.

Identify the units and denominator. This arithmetic alone supplies no uncertainty interval or causal evidence. Change a central input by 20%; report whether the management interpretation changes and why.

### Evidence appraisal and practical choice

**Inference and evidence.** Separate the estimand—the quantity the study intends to learn—from the statistic reported by a field method. A sample mean, proportion or index has a denominator and inclusion rule; a demographic forecast adds model assumptions; a management classification adds policy judgment. Ask whether the observation domain is representative of the population for which a recommendation is made. A confidence interval can capture sampling variation while omitting systematic selection bias. Apply this lens to **sampling design and baseline definition**: identify the actual observation, the larger unsupported inference and the smallest useful independent check. Explain how new evidence might change the next action.

**Implementation feasibility.** State equipment, expertise, permits, tenure and maintenance requirements. A biological gain that cannot be delivered under the available institutions is not a feasible forecast. Preserve site selection probabilities and document exactly which geographic domain results represent. A decision brief must still specify feasible alternatives, baseline and rights-related constraints; no quantitative success probability is implied.

### Independent application exercise

1. Sketch a causal graph of this case, naming a confounder and an observation that could disprove the leading explanation.
2. Improve the survey design: specify sampling units, detection controls, an appropriate comparison and a revision trigger.
3. Repeat the calculation with a 20% adverse change in one input, then draft a brief memo separating measured facts from management judgments.

**Lesson takeaway.** Trace the scientific mechanism, observed indicator and authorized decision separately; no synthetic model is a forecast of a real site.

## Lesson 4.2 — Occupancy and imperfect detection

**Guiding question.** How can we distinguish a defensible finding about **occupancy and imperfect detection** from a pattern that could arise through an alternative mechanism or a biased sample? The aim is to explain the ecological idea, define an appropriate quantity, reproduce an elementary numerical example, interrogate a counterargument, and connect the evidence to a legitimate practical decision.

### The ecological mechanism and what it predicts

Failure to detect a species on one visit does not demonstrate absence; repeated detection histories can estimate occurrence and detection under stated closure assumptions. For this mechanism, identify the biological scale and time interval. Does an observation concern one organism, a local population or regional persistence? Name one observation that could contradict the explanation and distinguish the measured state from its inferred cause.

### A field measurement contract

Conduct multiple standardized visits within a suitable season and record non-detections, observer identity and habitat covariates. Define the sampling unit, eligibility, survey timing and denominators in advance. Keep auditable observations and appropriately restricted provenance so independent analysts can identify sources of bias.

**Methodological lens — repeat observations through time.** Schedule repeated observations during biologically informative seasons and record observer effort, equipment and protocol changes. A trend can reflect a shift in the detection process; retain a calibration subset when methods change. Document how site choice or altered detection could change the measured result.

### Synthetic ecological case and competing interpretation

A secretive marsh bird is heard on one of four dawn visits in a simulated series. This is a fictional case, not a measured local trend. Identify response, suspected driver and an unmeasured common cause. Would the conclusion change if the monitoring method became more sensitive?

**Main interpretive trap.** Treating all non-detection sites as truly unoccupied underestimates distribution when detection is imperfect. Name a comparison site and independent indicator that could expose this error. Specify the result that would force revision of the preferred explanation.

### Worked quantitative case: Detection after four visits at p=0.30

**Assumed invented input.** Conditional probability of at least one encounter in four independent visits when per-visit detection is 0.3.

**Expression:** `(1-(1-.30)^4)*100`. **Calculated answer:** **75.99 % detection if present**.

Identify the units and denominator. This arithmetic alone supplies no uncertainty interval or causal evidence. Change a central input by 20%; report whether the management interpretation changes and why.

### Evidence appraisal and practical choice

**Decision quality.** An actionable claim should identify a decision maker, a feasible alternative, an indicator that responds on the appropriate time scale and a rule for revisiting the choice. When both options could harm affected people, ecological urgency does not remove the obligation to identify rights and safeguards. Note whether the action prevents a pressure, repairs a process, protects remaining habitat or merely improves knowledge. The intended outcome must match that pathway. Apply this lens to **occupancy and imperfect detection**: identify the actual observation, the larger unsupported inference and the smallest useful independent check. Explain how new evidence might change the next action.

**Stakeholder assessment.** Identify who gains, who bears costs, who controls access and who can challenge a decision. Good biodiversity statistics do not supply consent or equitable governance. Use an occupancy framework and avoid assigning hard absence labels from sparse data. A decision brief must still specify feasible alternatives, baseline and rights-related constraints; no quantitative success probability is implied.

### Independent application exercise

1. Sketch a causal graph of this case, naming a confounder and an observation that could disprove the leading explanation.
2. Improve the survey design: specify sampling units, detection controls, an appropriate comparison and a revision trigger.
3. Repeat the calculation with a 20% adverse change in one input, then draft a brief memo separating measured facts from management judgments.

**Lesson takeaway.** Trace the scientific mechanism, observed indicator and authorized decision separately; no synthetic model is a forecast of a real site.

## Lesson 4.3 — Mark–recapture and abundance inference

**Guiding question.** How can we distinguish a defensible finding about **mark–recapture and abundance inference** from a pattern that could arise through an alternative mechanism or a biased sample? The aim is to explain the ecological idea, define an appropriate quantity, reproduce an elementary numerical example, interrogate a counterargument, and connect the evidence to a legitimate practical decision.

### The ecological mechanism and what it predicts

Mark–recapture estimates abundance from marked fractions and later encounters if marks persist, capture probabilities are appropriately modeled and animals mix between samples. For this mechanism, identify the biological scale and time interval. Does an observation concern one organism, a local population or regional persistence? Name one observation that could contradict the explanation and distinguish the measured state from its inferred cause.

### A field measurement contract

Track individual identity and sampling occasion, test unequal capture probability and report uncertainty and animal welfare constraints. Define the sampling unit, eligibility, survey timing and denominators in advance. Keep auditable observations and appropriately restricted provenance so independent analysts can identify sources of bias.

**Methodological lens — mechanism-based evidence.** Construct a directed causal diagram with the proposed driver, mediating process, ecological response and confounders. Association can be entirely real yet not caused by the proposed mechanism; test plausible alternatives. Document how site choice or altered detection could change the measured result.

### Synthetic ecological case and competing interpretation

A hypothetical turtle study marks 80 animals, later encounters 60, of which 12 are marked. This is a fictional case, not a measured local trend. Identify response, suspected driver and an unmeasured common cause. Would the conclusion change if the monitoring method became more sensitive?

**Main interpretive trap.** Lincoln–Petersen estimates can be biased by immigration, loss of marks, response to traps or heterogeneous capture probabilities. Name a comparison site and independent indicator that could expose this error. Specify the result that would force revision of the preferred explanation.

### Worked quantitative case: Lincoln–Petersen simple estimate

**Assumed invented input.** Eighty marked in sample one; sixty total in sample two; twelve marked recaptures, with restrictive closed-population assumptions.

**Expression:** `80*60/12`. **Calculated answer:** **400 animals**.

Identify the units and denominator. This arithmetic alone supplies no uncertainty interval or causal evidence. Change a central input by 20%; report whether the management interpretation changes and why.

### Evidence appraisal and practical choice

**Research integrity.** Scientific disagreement is most useful when it is attached to a falsifiable assumption. Document the version of the habitat map, taxonomic name, protocol, instrument calibration and analysis rules used in the inference. If a relevant record must be generalized for species protection or cultural confidentiality, explain that limitation without revealing the restricted information. A transparent report can be reproducible without disclosing sensitive coordinates. Apply this lens to **mark–recapture and abundance inference**: identify the actual observation, the larger unsupported inference and the smallest useful independent check. Explain how new evidence might change the next action.

**Comparator selection.** Choose untreated or reference sites using ecological similarity rather than ease of access. A valid comparator can differ from a desired restoration state but must represent a plausible alternative trajectory. Use estimators appropriate to the sampling design and do not equate a point estimate with an exact census. A decision brief must still specify feasible alternatives, baseline and rights-related constraints; no quantitative success probability is implied.

### Independent application exercise

1. Sketch a causal graph of this case, naming a confounder and an observation that could disprove the leading explanation.
2. Improve the survey design: specify sampling units, detection controls, an appropriate comparison and a revision trigger.
3. Repeat the calculation with a 20% adverse change in one input, then draft a brief memo separating measured facts from management judgments.

**Lesson takeaway.** Trace the scientific mechanism, observed indicator and authorized decision separately; no synthetic model is a forecast of a real site.

## Lesson 4.4 — Remote sensing and habitat verification

**Guiding question.** How can we distinguish a defensible finding about **remote sensing and habitat verification** from a pattern that could arise through an alternative mechanism or a biased sample? The aim is to explain the ecological idea, define an appropriate quantity, reproduce an elementary numerical example, interrogate a counterargument, and connect the evidence to a legitimate practical decision.

### The ecological mechanism and what it predicts

Satellite and drone products measure reflected or emitted signals; vegetation indices and land-cover classifications are proxies requiring local reference data. For this mechanism, identify the biological scale and time interval. Does an observation concern one organism, a local population or regional persistence? Name one observation that could contradict the explanation and distinguish the measured state from its inferred cause.

### A field measurement contract

Match image resolution and acquisition season to habitat features, use independent ground-truth points and report classification errors by class. Define the sampling unit, eligibility, survey timing and denominators in advance. Keep auditable observations and appropriately restricted provenance so independent analysts can identify sources of bias.

**Methodological lens — hierarchical evidence.** Separate raw observations from modeled parameters, predictions, classifications and management choices. Model uncertainty often has several layers; numerical output should not hide unmeasured inputs. Document how site choice or altered detection could change the measured result.

### Synthetic ecological case and competing interpretation

An image classification reports increased greenness after invasive plants colonize a degraded marsh. This is a fictional case, not a measured local trend. Identify response, suspected driver and an unmeasured common cause. Would the conclusion change if the monitoring method became more sensitive?

**Main interpretive trap.** Greenness is not native-species recovery, and cloud, atmosphere or phenology can drive apparent change. Name a comparison site and independent indicator that could expose this error. Specify the result that would force revision of the preferred explanation.

### Worked quantitative case: Normalized difference vegetation index

**Assumed invented input.** Near infrared reflectance 0.65, red reflectance 0.20; vegetation signal is not native biodiversity.

**Expression:** `(.65-.20)/(.65+.20)`. **Calculated answer:** **0.529 index**.

Identify the units and denominator. This arithmetic alone supplies no uncertainty interval or causal evidence. Change a central input by 20%; report whether the management interpretation changes and why.

### Evidence appraisal and practical choice

**Scale and transfer.** An effect observed in one patch does not automatically apply to a landscape, and a ten-year forecast is not validated by a two-month trial. Consider spatial heterogeneity, ecological feedbacks, temporal autocorrelation and the potential displacement of pressures. When extending a conclusion, explicitly identify which biological processes are plausibly stable and which depend on new conditions. Poor transportability often matters more than precision within the original sample. Apply this lens to **remote sensing and habitat verification**: identify the actual observation, the larger unsupported inference and the smallest useful independent check. Explain how new evidence might change the next action.

**Measurement reliability.** State whether the indicator measures abundance, occupancy, area, survival, pressure or a subjective rating. Some indicators can move in opposite directions under the same ecological change. Combine remote observations with ecological condition surveys and uncertainty mapping. A decision brief must still specify feasible alternatives, baseline and rights-related constraints; no quantitative success probability is implied.

### Independent application exercise

1. Sketch a causal graph of this case, naming a confounder and an observation that could disprove the leading explanation.
2. Improve the survey design: specify sampling units, detection controls, an appropriate comparison and a revision trigger.
3. Repeat the calculation with a 20% adverse change in one input, then draft a brief memo separating measured facts from management judgments.

**Lesson takeaway.** Trace the scientific mechanism, observed indicator and authorized decision separately; no synthetic model is a forecast of a real site.

## Lesson 4.5 — Biodiversity data provenance and ethics

**Guiding question.** How can we distinguish a defensible finding about **biodiversity data provenance and ethics** from a pattern that could arise through an alternative mechanism or a biased sample? The aim is to explain the ecological idea, define an appropriate quantity, reproduce an elementary numerical example, interrogate a counterargument, and connect the evidence to a legitimate practical decision.

### The ecological mechanism and what it predicts

Occurrence data contain taxonomic, temporal and spatial uncertainties, while detailed locations of vulnerable species may increase exploitation risks. For this mechanism, identify the biological scale and time interval. Does an observation concern one organism, a local population or regional persistence? Name one observation that could contradict the explanation and distinguish the measured state from its inferred cause.

### A field measurement contract

Retain source, coordinates uncertainty, taxonomic authority, date, license, observer effort and access restrictions for sensitive information. Define the sampling unit, eligibility, survey timing and denominators in advance. Keep auditable observations and appropriately restricted provenance so independent analysts can identify sources of bias.

**Methodological lens — decision-focused study.** Specify the decision that will change if a result is high or low, then choose the least complex credible measurement. Collecting more data is not always useful if the result cannot change an authorized decision. Document how site choice or altered detection could change the measured result.

### Synthetic ecological case and competing interpretation

A public species-observation dashboard accidentally reveals exact nest coordinates of a hunted bird. This is a fictional case, not a measured local trend. Identify response, suspected driver and an unmeasured common cause. Would the conclusion change if the monitoring method became more sensitive?

**Main interpretive trap.** More open raw location data are not automatically more ethical or useful; duplicate observations bias density maps. Name a comparison site and independent indicator that could expose this error. Specify the result that would force revision of the preferred explanation.

### Worked quantitative case: Georeference quality rate

**Assumed invented input.** One hundred forty-four of 180 synthetic occurrence records have acceptable coordinate uncertainty for this use.

**Expression:** `144/180*100`. **Calculated answer:** **80 % georeferenced**.

Identify the units and denominator. This arithmetic alone supplies no uncertainty interval or causal evidence. Change a central input by 20%; report whether the management interpretation changes and why.

### Evidence appraisal and practical choice

**Field reasoning.** Represent the causal pathway as a set of stages: ecological source condition, exposure or interaction, demographic or community response, observed indicator and management interpretation. Describe which stage the proposed evidence directly addresses. A value measured at the end of a chain is not automatically a direct measurement of its cause. Record time delays between pressure and response; persistent adults, stored propagules and transient habitat use can postpone visible change. Apply this lens to **biodiversity data provenance and ethics**: identify the actual observation, the larger unsupported inference and the smallest useful independent check. Explain how new evidence might change the next action.

**Uncertainty propagation.** Distinguish variation among sites, error in individual measurements, uncertainty in modeled parameters and lack of knowledge about causal structure. Combining them into a single unsupported percentage hides weakness. Share appropriately generalized data with governance and privacy safeguards, using GBIF-style metadata concepts. A decision brief must still specify feasible alternatives, baseline and rights-related constraints; no quantitative success probability is implied.

### Independent application exercise

1. Sketch a causal graph of this case, naming a confounder and an observation that could disprove the leading explanation.
2. Improve the survey design: specify sampling units, detection controls, an appropriate comparison and a revision trigger.
3. Repeat the calculation with a 20% adverse change in one input, then draft a brief memo separating measured facts from management judgments.

**Lesson takeaway.** Trace the scientific mechanism, observed indicator and authorized decision separately; no synthetic model is a forecast of a real site.

## Integrated unit investigation — Wetland monitoring and imperfect observation

**Research and management setting.** Three field teams record different sightings despite using the same mapped site boundaries. True ecological differences and recording differences are both possible. This dataset is fictional and is not sourced from an actual site. Begin by specifying the intended population and the decision that requires evidence. A useful research question should distinguish a state variable, such as breeding occupancy or native habitat condition, from management inputs, such as field labor or expenditure. Decide which indicator could in principle move because the proposed intervention changed an ecological mechanism rather than because the observation process was altered.

**Classroom data.** Three synthetic teams record detections [9,15,11] in four visits per site; weather and equipment differ. Put each synthetic observation into a small table with a column for its unit, survey date or period, uncertainty and collection method. If an input is a judgment or a scenario assumption rather than an observation, label it as such. Draw a diagram showing how each measurement relates to the ecological process. Check dimensions before constructing composite indices: an area in hectares and a conservation score without units cannot be added without an explicit decision rule.

**Analysis assignment.** Describe a repeated-visit design that could estimate detection separately from occupancy, including appropriate closure assumptions. For each alternative, state what is observed, what is assumed and what would require external validation. Give a best-case and a downside scenario, but do not attach unsupported probabilities. Explain which changes in sampling design or stakeholder priorities would change the conclusion. Illustrate your results with a chart that shows raw points alongside summary values; avoid hiding sample size in a visually smooth curve.

**Critical evaluation.** List data fields and privacy precautions required for independent reuse without releasing sensitive nesting coordinates. A responsible report names at least two plausible alternative explanations. Propose a stronger monitoring design with a baseline or counterfactual, a biological outcome metric, a record of implementation and a realistic revision trigger. If the intervention entails handling wildlife, exposing locations or changing access, identify independent specialist review, legal permissions and affected decision makers; the invented project grants none of those permissions.

**Submission format.** Produce (1) a one-page causal map, (2) a reproducible calculation sheet, (3) a table separating raw observations from modeled outputs, (4) a comparison of intervention and nonintervention alternatives, and (5) a short decision memo stating uncertainty and who can authorize further work. Peer reviewers should be able to find a changed assumption and recompute the conclusion without modifying undocumented spreadsheet cells. Respond in writing to one challenge from a skeptical reviewer rather than simply repeating the original recommendation.

## Unit synthesis and knowledge check

The key result from this unit is not an isolated numerical score. Explain how **sampling frames, repeat visits, traceable identity and measured detectability** shapes the evidence required, how the fictional running setting differs from an actual conservation authority's decision, and which biological time scales could make early monitoring misleading. Connect a model output to an observation that could reject it. Finally, write a short critique of the following statement: *“The project achieved its activity target, so it has conserved biodiversity.”* Show why the conclusion either lacks a measurable biological outcome, a credible counterfactual, a legitimate governance process, or more than one of those ingredients. Formulate an alternative statement that does not exceed what the available evidence can support.
