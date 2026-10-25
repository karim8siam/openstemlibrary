# Unit 08 — Applied ecology and adaptive decisions

> Connect ecological evidence to agriculture, cities, health, services and practical learning.

## Learning goals

For applied ecology and adaptive decisions, explain the processes described in this unit, identify suitable observational and experimental units, connect synthetic numerical cases to physical measurements, and distinguish competing mechanisms. In the context of connect ecological evidence to agriculture, cities, health, services and practical learning., state how variation in sampling effort, habitat, time or model assumptions could change the result. Interpret quantities with units and identify the evidence required before applying results to a real management decision.

## Conceptual foundation

### Applying ecology without confusing observation with intervention

Ecological principles enter farms, cities, disease surveillance, environmental accounting and public decisions. In each setting, the scientific question competes with operational limits: money, labor, institutions, local knowledge and the costs of errors. Applying a plausible ecological mechanism does not guarantee that an intervention succeeds. A field margin intended to support beneficial insects may require long-term mowing, land access and compatibility with farm management. A street-tree program may reduce local heat but fail when saplings die without maintenance. A watershed project may measure improved water quality only after delayed nutrient transport becomes visible.

Agroecology explores how crop diversity, soil protection and biological interactions influence production and resource use. Comparing an intercrop with monoculture requires measuring all component yields against appropriate baselines. A land-equivalent ratio above one suggests an area efficiency advantage under the chosen yields; it says little by itself about labor costs, market prices or risk. A farmer facing limited water may rationally choose a method with lower average output if its worst-season losses are smaller. Thus ecological productivity and livelihood feasibility belong in the same decision framework without collapsing into one metric.

Urban ecology follows energy, water and organisms through built landscapes. Impervious surfaces accelerate runoff, vegetation changes shade and evapotranspiration, and artificial light can alter animal behavior. Environmental benefits are distributed unequally, so average city temperature is not enough to evaluate heat-reduction policy. A successful analysis considers where vulnerable residents live, whether green spaces are accessible, and whether maintenance expenses or housing changes create unintended harm. Land-surface temperature maps are useful, but personal heat exposure depends on shelter, work, airflow and time of day. Ecological findings should not be used to imply that any neighborhood's residents are individually responsible for their exposure.

Disease ecology requires particular care. A change in vector abundance does not translate mechanically into changes in human infection because pathogen presence, contact behavior, host susceptibility and reporting systems also matter. Different pathogens can respond differently to biodiversity and land use. Ecological correlations are not a license for unsupervised sampling of pathogens, medical diagnosis or control interventions. Responsible work uses non-invasive records and collaboration with public-health specialists, with appropriate privacy and ethical approvals. The goal of the introductory analysis is to map causal pathways and identify evidence needs, not issue individual medical advice.

Ecosystem-services valuation can help compare interventions when the benefited population and counterfactual are clearly specified. The flood-protection value of a wetland depends on hydrology, upstream construction, downstream exposure and maintenance alternatives. Carbon credits raise additional issues of permanence, leakage and attribution. Double counting is a danger when both an intermediate ecological function and its final service are monetized separately. Cultural and ecological values also may not have meaningful market prices; transparent decision documents retain these dimensions instead of quietly assigning them zero.

Adaptive management closes the loop between knowledge and action. A manager chooses among options, states predicted outcomes under several hypotheses, implements within a monitoring framework and revisits the decision with new evidence. Updating should follow a predetermined schedule and decision rule wherever feasible. Otherwise, any disappointing result can be reinterpreted after the fact as success. Budget, monitoring continuity, legal permissions and stakeholder governance determine whether learning can actually occur. Ecological literacy is valuable here because it separates input actions—trees planted, meters of bank fenced, meetings held—from biological outcomes, such as surviving native recruits, reduced nutrient loads or sustained habitat functions.

## Five focused topics with worked examples

### 8.1 Agroecology and land-use mosaics

#### Ecological concept and mechanism

Agricultural landscapes supply food while altering soils, water, habitat structure and biotic interactions. Ecological design seeks productive systems that manage resources and support desired ecological services.

Crop rotation, diversity, cover and integrated pest management can alter resource availability, herbivore dynamics and erosion. Outcomes depend on local climate, labor, markets and management intensity.

#### Worked interpretive case

Intercropping reduces bare soil in a hypothetical smallholding, but competition for moisture lowers one crop's yield during a dry year. The system-level result depends on combined harvest and input costs.

#### Evidence and study design

Compare replicated management plots over multiple seasons, documenting labor, inputs, rainfall, pests and yields per area rather than only plant height.

Calculate land-equivalent ratio from two intercrop yields and monocrop benchmarks; interpret the result carefully.

#### Critical limitations and transfer

Claims about universally sustainable techniques ignore land tenure, costs, spillovers and local ecology. A small experimental gain may not justify adoption at commercial scale.

Ecological outcomes should be assessed together with the economic feasibility faced by farmers.

#### Worked quantitative example 8.1: Intercrop land-equivalent ratio

**Synthetic data.** Crop A yields 3 units per hectare in the mixture versus 4 in monoculture; crop B yields 2 in mixture versus 3 in monoculture.

**Derivation and solution.** Sum mixture yields divided by their corresponding monocrop reference yields. The explicit calculation `3/4+2/3` gives **1.41667 land-equivalent ratio**. Identify how the input variables were defined before applying the same arithmetic to new measurements; the result is conditional on that definition.

**Ecological interpretation.** The ratio above one suggests a land-use advantage under consistent yields and reference systems.

**When the computation would mislead.** Labor, product value, risks and altered input requirements are not represented by this metric. For field applications, compare the precision of the input measurements with the apparent precision of the answer, then decide whether model structure or sampling error is likely to dominate uncertainty.

**Independent check and extension.** Calculate change if crop A's mixture yield drops to 2.5 while all other values stay fixed. Recalculate with one altered input and describe the observation that would justify changing that parameter in a real ecological study. Distinguish recalculating an illustrative equation from experimentally validating the biological relationship.


### 8.2 Urban ecology and environmental justice

#### Ecological concept and mechanism

Cities contain ecological systems shaped by impervious surfaces, heat, stormwater infrastructure, vegetation, wildlife movement and unequal exposure to environmental burdens.

Tree cover and soil influence shade and infiltration; artificial light alters animal behavior; fragmented green areas affect connectivity. Heat, flooding and pollution often correlate with housing and infrastructure inequality.

#### Worked interpretive case

Two neighborhoods experience similar regional temperatures but differ in street-tree cover and surface temperatures. Residents' exposure also depends on shade access, work patterns and building quality.

#### Evidence and study design

Sample temperatures and vegetation consistently across neighborhoods, account for land cover and street geometry, and work with residents to interpret relevant health and access outcomes.

Plan an evaluation of street-tree planting that measures shade, survival, water use, access and long-term maintenance.

#### Critical limitations and transfer

Satellite land-surface temperature is not a direct measure of personal heat exposure. Greening may raise maintenance costs or intensify displacement without protective policy.

Ecological benefits are not just physical averages: distribution and governance determine who actually receives them.

#### Worked quantitative example 8.2: Observed cooling contrast

**Synthetic data.** A shaded street has standardized afternoon air temperature 31.7 degrees Celsius and a nearby comparable unshaded street records 34.8.

**Derivation and solution.** Subtract shaded temperature from exposed temperature. The explicit calculation `34.8-31.7` gives **3.1 degrees Celsius**. Identify how the input variables were defined before applying the same arithmetic to new measurements; the result is conditional on that definition.

**Ecological interpretation.** The 3.1 degree contrast is a paired observational difference, not proven treatment effect.

**When the computation would mislead.** Wind, traffic, street geometry and placement of sensors can produce confounding. For field applications, compare the precision of the input measurements with the apparent precision of the answer, then decide whether model structure or sampling error is likely to dominate uncertainty.

**Independent check and extension.** Specify a before-after control-impact design across multiple blocks. Recalculate with one altered input and describe the observation that would justify changing that parameter in a real ecological study. Distinguish recalculating an illustrative equation from experimentally validating the biological relationship.


### 8.3 Disease ecology and One Health

#### Ecological concept and mechanism

Disease patterns arise from interactions among hosts, pathogens, vectors and environments, rather than from a single isolated organism. Ecological analyses can identify risk pathways without substituting for clinical guidance.

Contact structure, host density, vector life cycles and habitat modification can alter transmission opportunities. Biodiversity effects on infection can vary by pathogen and setting.

#### Worked interpretive case

Mosquito counts rise after the creation of stagnant pools, but disease cases may not track counts without infected vectors, host exposure and surveillance consistency.

#### Evidence and study design

Use non-invasive surveillance records, environmental measurements and appropriate public-health collaborations. Distinguish vector abundance, infection prevalence and human incidence.

Explain why doubling vector abundance does not necessarily double infection incidence and what additional measurements would be necessary.

#### Critical limitations and transfer

Assuming biodiversity universally dilutes disease is an overgeneralization. Observational associations between land cover and cases are confounded by testing, movement and behavior.

Ecological health studies require qualified partners, ethical approvals and caution about personal medical data.

#### Worked quantitative example 8.3: Illustrative relative incidence

**Synthetic data.** In two synthetic cohorts, observed cases are 18 per 1000 and 10 per 1000 person-periods with comparable observation duration.

**Derivation and solution.** Divide the reported incidence proportions to obtain an illustrative relative comparison. The explicit calculation `(18/1000)/(10/1000)` gives **1.8 relative rate proxy**. Identify how the input variables were defined before applying the same arithmetic to new measurements; the result is conditional on that definition.

**Ecological interpretation.** The ratio 1.8 describes an association across these invented populations only.

**When the computation would mislead.** Confounding, differences in testing and unobserved exposure prevent causal interpretation; it is not a clinical risk forecast. For field applications, compare the precision of the input measurements with the apparent precision of the answer, then decide whether model structure or sampling error is likely to dominate uncertainty.

**Independent check and extension.** List data needed to separate vector density from human contact or reporting differences. Recalculate with one altered input and describe the observation that would justify changing that parameter in a real ecological study. Distinguish recalculating an illustrative equation from experimentally validating the biological relationship.


### 8.4 Ecosystem services, valuation and externalities

#### Ecological concept and mechanism

Ecosystems provide food, water regulation, pollination, recreation and cultural values, but valuation depends on the beneficiaries, baseline and method. Some ecological significance cannot be represented adequately by a market price.

A wetland can attenuate flood peaks, retain sediment and support species; draining it may shift costs onto downstream communities. Benefits and trade-offs vary over space and time.

#### Worked interpretive case

A city considers replacing an urban wetland with hard drainage infrastructure. Financial costs are easy to estimate, but long-term maintenance, flood risk and habitat losses require scenario analysis.

#### Evidence and study design

Identify service pathways and beneficiaries, compare counterfactual scenarios and avoid double counting intermediate ecological functions and final human benefits.

Calculate an illustrative net present value for maintenance costs while keeping nonmarket and distributional considerations visible.

#### Critical limitations and transfer

A willingness-to-pay survey is not a measure of intrinsic ecological worth. Transfers from unrelated regions may misvalue services and overlook inequity.

Economic evidence can inform conservation without defining all ecological or ethical value.

#### Worked quantitative example 8.4: Discounted future maintenance

**Synthetic data.** A restoration structure requires 1000 monetary units of maintenance two years from now and the stipulated annual discount rate is five percent.

**Derivation and solution.** Calculate present value by dividing future cost by 1.05 squared. The explicit calculation `1000/(1.05**2)` gives **907.029 present-value money units**. Identify how the input variables were defined before applying the same arithmetic to new measurements; the result is conditional on that definition.

**Ecological interpretation.** The cost is about 907 in today's units at the assumed discount rate.

**When the computation would mislead.** A single rate may mask inflation, unequal impacts on communities and nonmarket ecological values. For field applications, compare the precision of the input measurements with the apparent precision of the answer, then decide whether model structure or sampling error is likely to dominate uncertainty.

**Independent check and extension.** Compute present value with zero discounting and examine distributional assumptions. Recalculate with one altered input and describe the observation that would justify changing that parameter in a real ecological study. Distinguish recalculating an illustrative equation from experimentally validating the biological relationship.


### 8.5 Adaptive management and ecological futures

#### Ecological concept and mechanism

Adaptive management connects decisions, monitoring and revision under uncertainty. It differs from trial and error when competing models and decision rules are specified beforehand.

Managers select actions based on predicted outcomes, gather monitoring data and update their beliefs or practices. Robust strategies perform acceptably across several plausible future conditions.

#### Worked interpretive case

A watershed agency pilots buffer strips in selected subcatchments and compares nutrient export under differing storms. The next investment depends on both effect size and maintenance cost.

#### Evidence and study design

Set baseline measurements, thresholds for revisiting policy, transparent counterfactuals and a public schedule for reviewing results. Include failed interventions in the evidence record.

Outline a two-cycle decision process that changes one management parameter only after sufficient observed evidence.

#### Critical limitations and transfer

Without sustained monitoring, governance and budget, adaptive management becomes a label rather than a learning process. Changing multiple interventions together obscures attribution.

Useful ecological science leaves a trail from quantified uncertainty to a practical, revisable action.

#### Worked quantitative example 8.5: Monitoring-based load reduction

**Synthetic data.** A pilot's estimated downstream nutrient load falls from 50 to 35 kilograms per day after implementation under a simplified matched flow regime.

**Derivation and solution.** Compute relative reduction from the initial benchmark. The explicit calculation `(50-35)/50` gives **0.3 fractional load reduction**. Identify how the input variables were defined before applying the same arithmetic to new measurements; the result is conditional on that definition.

**Ecological interpretation.** The observed thirty percent reduction is a monitored contrast, not automatic proof of causation.

**When the computation would mislead.** Storm distribution, calibration drift, upstream inputs and sample uncertainty can explain apparent change. For field applications, compare the precision of the input measurements with the apparent precision of the answer, then decide whether model structure or sampling error is likely to dominate uncertainty.

**Independent check and extension.** Design a replication and evaluation schedule to determine whether the intervention can be expanded. Recalculate with one altered input and describe the observation that would justify changing that parameter in a real ecological study. Distinguish recalculating an illustrative equation from experimentally validating the biological relationship.


## Integrated computational and observation-design laboratory 8: Adaptive decision across land uses

### Research aim and study system

Consider one hypothetical farm-buffer intervention and one street-shade intervention with different costs, confidence ranges and access patterns. This is an educational, entirely synthetic exercise for readers without laboratory equipment. Its case is **two-stage ecological policy trial**, represented by **three farm catchments with buffer strips and a city block with new street trees**. The key quantities to observe are **benefit, operational cost, uncertainty and stakeholder access**. The question is not simply whether two columns differ: it is whether the chosen evidence can **predefine thresholds for changing an intervention after monitoring**. State the central alternative before generating any synthetic measurements. Otherwise changes in a plot can be explained after the fact without a meaningful test.

### Data dictionary and reproducibility requirements

Provide one row per actual study unit or visit, depending on the stage of measurement, and include explicit identifiers. Document **decision authority and exposure of affected groups**; also retain location class, date, survey duration, method version and a reason when data are missing. Define every unit, including degrees of temperature, area, individual counts or mass-per-time flux. Use distinct codes for zero, unobserved and not applicable. A table in which no organisms were seen despite valid sampling is not equivalent to a table in which a site was never visited. Save a read-only raw dataset and a second transformed dataset alongside a reproducible calculation log.

The book contains a synthetic example dataset for this unit under `datasets/lab-08.csv`. It illustrates a stable column structure rather than empirical evidence; its numerical values and site labels are invented. Review whether the input data are logically coherent before fitting any equation. A physically impossible concentration or a date outside the sampling window should trigger validation. Record any corrected values and preserve the originals so another reader can explain every change.

### Procedure

1. **Specify hypotheses.** Choose one explanatory process drawn from **agroecology and land-use mosaics** and a serious competing explanation related to **disease ecology and one health**. Describe the response variable and whether the process predicts an increase, decrease, threshold or no change. Include a null pattern that could plausibly arise through sampling variation.
2. **Establish comparability.** Match sites, periods, effort or experimental units appropriately. If the study uses simulated random assignment, preserve the random seed and show treatment balance. Do not treat several measurements from one habitat block as independent blocks. Explain how space, time and shared weather might introduce dependence even under a seemingly random scheme.
3. **Explore the data.** Construct a scatterplot or time series with labeled axes, raw points and explicit group names. Report sample size at the actual experimental or observational-unit level. Inspect non-detections and extreme values, but do not delete observations solely because they contradict the initial hypothesis.
4. **Calculate and compare.** Develop pre-committed decision rules, specify additional evidence needs and compare robustness across dry and wet years. Check arithmetic using two methods—a spreadsheet and a manual calculation, for example. Explain what part of the comparison was identified by a definition and what part required a model assumption. A graph that looks smooth does not demonstrate the validity of a causal pathway.
5. **Stress-test the conclusion.** Change one defensible parameter or data-quality rule: detection probability, sampling area, rate assumption, autocorrelation or reference choice. Recompute the principal estimate. If a moderate alteration reverses the sign or action threshold, present both outcomes and recommend improved measurement before a high-cost decision.
6. **Interpret with an alternative.** Compare the leading mechanism with the explicitly named rival. Propose a new independent measurement that would discriminate them. Include uncertainty and an ethical or logistical limitation. If results are inconsistent, label the result unresolved instead of inventing an unobserved pathway to rescue a favorite hypothesis.

### Results discussion and expected reasoning

The exercise contains no prespecified discovery. Its purpose is to make plausible ecological stories answerable through measurements. Explain how **urban ecology and environmental justice** may affect a predicted outcome while **ecosystem services, valuation and externalities** can change the interpretation. Where the calculation involves probability, distinguish conditional probabilities from frequencies over repeated independent systems. Where a budget is calculated, distinguish flow rates from stocks and sum only compatible quantities. Where a management action is proposed, separate the number of actions implemented from the measured response of the ecosystem.

Urban greening, farm management and public health decisions require local expertise, permissions and participation. Report the synthetic status prominently. If a model produces an impossible value, do not silently truncate it unless the modeling rule explicitly requires a bound. Instead identify the biological restriction omitted by the simple equation. Some ecological systems can have alternative stable trajectories or long lag times, but neither should be claimed from the dataset without specific evidence.

### Deliverables, assessment and extension

Submit an annotated data dictionary, an analysis script or spreadsheet formula log, two labeled figures, one complete hand-worked numerical calculation and a one-page discussion with prediction, result, competing explanation and limitation. Include a paragraph on reproducibility and any constraints on safe field transfer. For extension, choose **adaptive management and ecological futures** as a new potential driver and design a minimally more informative follow-up study. Explain the number and kind of genuinely independent replicates that would be needed for a small pilot, rather than declaring arbitrary sample sizes statistically adequate.


## Unit 8 synthesis and critical assessment

1. **Mechanism map.** Relate Agroecology and land-use mosaics to Ecosystem services, valuation and externalities. Mark the measured processes, their directions and the place where a biological outcome could be changed by an unobserved driver. Distinguish a numerical ecological gain from cost-effectiveness and fairness.
2. **Rival explanation.** A report concludes that urban ecology and environmental justice must be responsible for a mapped pattern. Identify an environmental or measurement-based alternative, an observation consistent with both, and an independent comparison that could distinguish them.
3. **Quantitative audit.** Reconstruct all five examples in this unit without looking at the displayed result. Check units and dimensions, identify the reference value, and vary an input by ten percent. Record the effect size and the meaning of a negative, zero or unexpected result where applicable.
4. **Evidence review.** Examine a hypothetical study with four sites, two of them treated and two untreated, where investigators repeated twenty subsamples at every site. Explain why there are four independent site-level units, then discuss what additional temporal and spatial controls would strengthen the inference. Adjust the explanation if treatment spills between adjacent sites.
5. **Transfer and limits.** State a rule that would change a monitoring program after contradictory evidence. Draft a concise comparison of how the model's assumptions change when moved from the constructed teaching scenario to a coastal, urban, agricultural or protected-area system. Explicitly indicate which ecological outcomes need long-term monitoring.
6. **Research communication.** Write a 500-word mini-review of two concepts from the unit, distinguishing established general mechanisms from synthetic calculations and uncertain real-world consequences. Cite at least one reliable open textbook or scientific reference, and state exactly which claim the reading supports. An external reference is not an endorsement of the OpenSTEM draft.

