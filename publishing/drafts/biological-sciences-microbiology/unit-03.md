# Unit 3: Microbial Growth and Metabolism

Growth is a change in cell number or biomass over time, and microbial metabolism is the network of chemical transformations that supports maintenance and reproduction. The two are related but not identical. A population may metabolize substrate without increasing in cell count, and the number of visible cells can remain stable while births and deaths balance. Growth curves provide compact mathematical descriptions but must not be mistaken for invariant biological laws. In this unit, exponential population increase, resource limitation, energy conservation and ecological heterogeneity are used to connect observations to mechanisms. Any numerical illustration is restricted to harmless mathematical quantities; it is not an instruction for culturing pathogens.

## 3.1 Generation time, population change and growth phases

If every cell in an idealized population divides once per generation and all descendants remain alive, the population doubles with each generation. Starting with N0 cells, after n generations the count is N=N0×2^n. If g is the generation time, n=t/g and N(t)=N0×2^(t/g). The same model can be expressed with a specific rate µ=ln(2)/g, giving N(t)=N0 exp(µt). These forms are mathematically equivalent under their stated assumptions. They describe a constant per-capita rate, not a guarantee that a real population can double indefinitely. Cells experience nutrient limitations, metabolic by-products, crowding and changes in physiology as conditions evolve.

A standard schematic growth curve includes lag, exponential, stationary and decline phases. Lag refers to adaptation and may include changes in gene expression or repair without immediate doubling. Exponential increase is the segment where a roughly stable specific growth rate may be estimated. Stationary counts can result from resource limitation or balanced reproduction and death; they do not prove that every cell has stopped metabolism. Decline may reflect loss of viable cells, but measurement itself matters. Optical density estimates light scattering, not viable count, and even the relation between scattering and biomass can vary across cell shapes or concentrations.

Consider a hypothetical population of one million cells with a two-hour generation time. Four hours correspond to two generations; the model predicts four million cells. At eight hours it predicts sixteen million. If an observed count at eight hours is only six million, the discrepancy could indicate resource limitation, loss, unequal division rates, measurement saturation or a model assumption that never applied. One should not 'correct' the observation to fit the exponential expression. The correct scientific response is to examine the evidence and consider models with time-varying rates. A single endpoint cannot establish all growth phases.

A growth-rate calculation also needs attention to units and uncertainty. For two measurements N1 and N2 separated by Δt, a log-slope estimate is µ=[ln(N2)−ln(N1)]/Δt, provided those measurements come from the appropriate growth interval. If counts are near a detection limit, uncertainty in log counts can be large. An experiment should report what was counted, the instrument range, replicate variation and why the interval was considered exponential. Arithmetic without those context statements invites false precision. The interactive doubling model in this unit is an exercise in interpreting assumptions, not a practical prediction for any particular organism.

Distinguish growth rate from generation time and carrying capacity. A shorter generation time implies faster idealized doubling during exponential growth, whereas the eventual stationary population depends on resource availability and system constraints. Two populations may grow at different initial rates and reach different endpoints. A logistic equation can sometimes summarize slowing growth, but its carrying-capacity parameter is an effective description and can change when the environment changes. Good comparisons hold measurement definitions constant and avoid treating growth constants as permanent species labels.

## 3.2 Nutrient uptake, limitation and growth-yield concepts

Microorganisms require sources of energy, electrons and material for building cellular structures, though the chemical sources differ greatly among lineages. Carbon may come from inorganic CO2 or preformed organic molecules; energy may come from light or chemical reactions; electrons may be obtained from organic or inorganic donors. Terms such as phototroph, chemotroph, autotroph and heterotroph describe different dimensions. A phototroph is not necessarily an autotroph, and a heterotroph is not automatically dependent on oxygen. Keeping energy, carbon and electron sources conceptually separate prevents common classification errors.

Nutrient limitation occurs when a resource constrains additional growth under the current conditions. An environment rich in carbon can still limit growth through scarcity of phosphorus, nitrogen or a trace cofactor. A response to adding one resource is evidence of limitation only if competing changes are controlled. The limiting nutrient may shift as organisms grow or as the composition of the community changes. Ratios of available nutrients can be informative, but a ratio alone cannot establish causality without demand estimates and direct responses. Different cell types also differ in acquisition mechanisms and internal storage strategies.

A Monod-type equation represents specific growth rate as µ=µmax S/(Ks+S), where S is a limiting substrate concentration and Ks is the concentration at which the rate reaches half of µmax. This phenomenological expression resembles a saturating curve but is not an assertion that every microbial population follows simple enzyme kinetics. It assumes one effective limiting variable and stable conditions; it cannot model toxicity, changing cell composition or several interacting limitations without modification. If µmax=0.8 h−1 and Ks=20 mg/L, S=20 mg/L gives µ=0.4 h−1. At S=100 mg/L the expression yields about 0.667 h−1, not an unlimited increase.

Yield is distinct from growth rate. A biomass yield might be expressed as grams of biomass formed per gram of substrate consumed, provided biomass and substrate are defined consistently. A high yield does not necessarily imply rapid growth: an organism may convert substrate efficiently but slowly, or grow rapidly with substantial overflow metabolism. Maintenance energy, secretion of products and loss of carbon as gas all influence net yield. Experimental interpretations should use conservation laws and state whether measurements describe dry biomass, organic carbon, cells or another quantity. One measurement cannot be exchanged for another without a calibration.

Resource gradients are especially important in heterogeneous environments. A microorganism attached near a surface may experience different oxygen or carbon concentrations from a cell only micrometres away. Bulk measurements average over these differences and can conceal locally limiting conditions. If a mathematical model predicts a smooth monotonic response to substrate, students should ask whether the medium is actually homogeneous and whether the uptake rate modifies the local concentration. Biological inference improves when the spatial scale of observation matches the scale of the proposed mechanism.

## 3.3 Respiration, fermentation and microbial energy budgets

Metabolism consists of chemical transformations connected by energy and matter flows. Catabolic reactions can release usable free energy; anabolic reactions consume energy and precursor molecules to build cellular constituents. The central physical constraint is conservation of atoms and energy, alongside thermodynamic constraints on reaction direction. Microbes differ in the electron donors and acceptors they use, which can generate diverse respiratory strategies. Oxygen respiration is only one option. Some microorganisms use other external electron acceptors; others rely on fermentation pathways to maintain cofactor balance. The fact that energy is released is not sufficient to predict how much supports growth.

Respiration involves electron transfer from donors through pathways that ultimately reduce an acceptor, with some energy conserved in a form that can support cellular work. In many systems, membrane-associated electron transport contributes to an electrochemical gradient. The gradient can be coupled to ATP production or other processes. Detailed chain composition varies, and simple statements like 'all bacteria make ATP the same way' are wrong. A metabolically versatile organism may shift the balance of pathways as conditions change, while one specializing in a narrow environment may have fewer options. Pathway diagrams should annotate electron flow rather than just memorize colorful arrows.

Fermentation differs in its handling of electron balance. Organic molecules can act as electron donors and internal acceptors, allowing regeneration of oxidized cofactors without dependence on an external respiratory electron acceptor for that particular pathway. Products vary among organisms and conditions. The economic importance of fermentation in food and industry does not make every fermentation equivalent to ethanol production. Organic acids, gases and other compounds may accumulate, and carbon recovery must be checked against the stoichiometry of the hypothesized products. A fermentation product is part of a metabolic solution to electron and energy balance, not simply a waste material.

Consider the overall fate of a six-carbon substrate. If only one four-carbon organic product is measured, two carbon equivalents remain to be accounted for somewhere in biomass, dissolved compounds or gaseous products. Without a carbon mass balance, an apparent 'high conversion' could reflect unmeasured outputs or analytical error. The same principle holds for electron equivalents. A report measuring only the disappearance of a reactant cannot distinguish biological conversion from adsorption, physical loss or sampling bias. Parallel controls and independent detection of products are essential for assigning a process to metabolism.

Thermodynamic favorability and kinetic rate must be distinguished. A favorable redox reaction can proceed too slowly to matter biologically without catalysts. Enzymes alter reaction rates without changing the equilibrium free-energy difference. The energy available from a particular transformation depends on actual chemical activities, not merely a textbook standard potential. Cells continuously maintain conditions away from equilibrium, so real metabolic processes are better understood as regulated networks embedded in a changing environment than as a fixed list of equations.

## 3.4 Microbial ecology, constraints and nonuniform environments

Microbial populations do not experience the environment as a smooth average. Soil aggregates, aquatic particles, roots, sediments and biological tissues present local gradients of oxygen, nutrients, light and pH. The physical structure of these habitats affects diffusion, advection and residence time. At a scale where one microbe sees abundant substrate, another cell only a short distance away may experience limitation. Such heterogeneity can sustain neighboring activities that appear chemically incompatible when averaged over the whole sample. An ecosystem model must decide whether to resolve those gradients or represent their combined effect with effective parameters.

Temperature influences enzyme-catalyzed processes, membrane physical properties and damage rates, but response curves are not universal. A modest temperature rise may accelerate one reaction and destabilize another; ecological competition can shift as species respond differently. Simple exponential or Arrhenius relationships are locally useful approximations rather than guarantees across all temperatures. Likewise, pH changes charge states and affects transport and enzyme function. Organisms may regulate their internal chemistry within a range, so external pH alone cannot reveal intracellular pH. Stress tolerance emerges from multiple linked processes.

Oxygen illustrates an important ecological distinction. Its presence can enable energy-conserving pathways, yet reactive oxygen chemistry can damage cellular components. Some microorganisms require oxygen for growth; others grow without it, and some are harmed under particular oxygen exposures. A label describing oxygen preference must be linked to the organism and experimental context. The chemical availability of oxygen can differ greatly within one habitat, especially when consumption is rapid and replenishment is limited. A high oxygen concentration at a surface does not guarantee oxygen at the center of a dense aggregate.

To investigate a field observation, begin by separating correlation from mechanism. If a microbial marker increases after rainfall, possible explanations include transport of cells from another source, changes in water volume, altered growth, differential survival and measurement artifacts. A time series can narrow hypotheses but rarely proves a single cause. Pairing concentration measurements with flow, nutrient data and community composition can provide stronger constraints. Repeated sampling across comparable sites distinguishes a consistent pattern from an isolated event. A mechanistic model must also specify whether its variables refer to cells, DNA, biochemical activity or population fractions.

Ecological generalization requires careful boundaries. A mathematical model based on a uniform liquid system may fail in layered soil, and a relationship inferred from one carbon source may not apply under mixed-substrate conditions. This is not an argument against models. Rather, models make assumptions visible so they can be tested and revised. The proper conclusion is not that microbial physiology is too complicated for quantitative analysis, but that the chosen level of simplification should be matched to evidence, experimental resolution and the scientific question.


## Guided investigation A: Why a growth curve cannot stand alone

Imagine receiving three measurements of a microbial population in a hypothetical teaching dataset: one million units at hour zero, two million at hour two and six million at hour six. A student fits an exponential model and predicts eight million at hour six by assuming a two-hour doubling time. The disagreement is important. An exponential law is a description of one possible growth regime; it does not grant permission to replace the observed six million with the predicted eight million. Nor should the student automatically assign the discrepancy to 'stationary phase' without examining measurement and physiological alternatives.

A first step is to estimate interval-specific log slopes. From zero to two hours the ratio is 2, so µ=ln2/2≈0.3466 h−1. From two to six hours the ratio is 3 across four hours, so µ=ln3/4≈0.2747 h−1. The reduction is consistent with a slowing effective growth rate across the latter interval. Yet with only endpoints, one cannot tell whether slowing occurred smoothly or abruptly. Uncertainty in counts, a period of death balanced by division, and sample heterogeneity could alter the interpretation. Additional time points with independent repeats would improve the evidence.

Measurement choice is equally important. Optical density responds to light scattering, which can change as cell size or aggregation changes. Direct microscopic counts include cells regardless of their ability to form colonies. A culture-based count depends on which individuals produce a countable event in the selected assay. If these are mixed on one plot without conversion and uncertainty, the curve may combine incomparable quantities. A useful investigation states the operational definition of N before fitting an equation. When calibration exists, it should be checked over the full observed range.

The Monod model offers one possible mechanistic extension if a specific nutrient becomes limiting. The rate µ(S)=µmax S/(Ks+S) slows as substrate falls, but a time-course prediction additionally requires a mass balance linking growth to substrate depletion and yield. Fitting the Monod expression to cell counts alone does not establish the actual limiting nutrient. Other conditions such as pH, accumulated products or oxygen availability may explain similar slowing. Model identifiability matters: several different causes can produce a similar curve.

A strong student report would compare the observed data with a fixed exponential baseline, estimate intervals with appropriate uncertainty and identify plausible mechanisms requiring more data. It would refrain from identifying the strain, metabolism or physical bottleneck from a short growth series. This approach uses quantitative tools to organize uncertainty rather than to conceal it behind a smooth fitted line.

## Guided investigation B: Closing an elementary carbon balance

Consider a theoretical reactor boundary receiving 100 carbon-moles of a generic substrate over a defined accounting interval. A report identifies 40 carbon-moles in a measured product and 35 carbon-moles in recovered biomass. By conservation of carbon, 25 carbon-moles remain unaccounted for unless they crossed the boundary through other outputs or were retained in another pool. Possible destinations include gaseous carbon compounds, dissolved by-products and unmeasured residues. The arithmetic does not identify the missing chemical species; it only demonstrates that the claimed complete accounting is false.

A proper mass balance defines a system boundary and sign convention. Total input equals changes in stored material plus all outputs when quantities are expressed in the same elemental units. If carbon content is compared using grams of total product instead of grams or moles of carbon, the balance may be invalid because molecules contain different proportions of hydrogen, oxygen and nitrogen. For example, conversion to a hydrated organic product can increase product mass through incorporation of oxygen or water without generating additional carbon. A mass yield and a carbon yield are therefore distinct measurements.

An electron balance can provide another constraint, especially when redox transformations occur. Electron donors and acceptors must be considered consistently with oxidation states, though introductory calculations usually simplify the chemistry. If a substrate disappears but the expected oxidized or reduced products are absent, the investigator should ask whether competing pathways, accumulation or analytical detection limits are involved. The absence of one expected product is not proof that the pathway did not occur; it may indicate a transient intermediate or unmeasured route. Conversely, disappearance of material alone does not prove biodegradation rather than physical transfer.

Experimental comparisons should use time-matched controls and measurements that represent the same boundary. A concentration reduction during a change in water volume can falsely suggest mass loss. Uncertainty propagates through the difference between input and output, and a small residual relative to instrument precision may not be significant. A written report should indicate whether uncertainty estimates are based on repeated biological samples, technical instrument replicates or assumed detection limits. These sources of variation have different meanings.

The educational objective is to connect biochemical narrative to conservation laws. Terms such as 'efficient conversion' or 'complete removal' need definitions that can be tested. A plausible pathway diagram is a hypothesis about where material travels; a closed mass balance provides a constraint on whether the hypothesis is complete. When the numbers do not add up, revising the hypothesis is better science than discarding the inconvenient remainder.


## Research note: Relative growth rates can conceal absolute loss

Suppose a microbial sample contains two populations with counts 100 and 900. After a hypothetical environmental change, both double to 200 and 1800. Their relative abundances remain 10% and 90%, even though each absolute abundance increased. Conversely, the percentage of one group can rise while its absolute count falls if the other declines faster. This simple arithmetic matters because many microbial surveys report composition rather than absolute counts. Any claim about growth from compositional data should be supported by a measurement linked to actual cell or biomass quantities. A positive change in fraction is not the same thing as a positive per-capita growth rate.

In an ideal exponential interval, a specific growth-rate estimate uses the change in logarithmic counts divided by elapsed time. If count measurements have known uncertainty, the uncertainty of a logarithm depends on the relative uncertainty of the original count. A near-zero count is particularly problematic, since the logarithm becomes unstable or undefined. Arbitrarily adding a small constant can change the estimated slope and should not be done without justification. This example reveals a broader limitation of elegant growth equations: the mathematics presumes that the measured quantities correspond to the variables in the model.

## Research note: Energy yield does not equal ATP production rate

A pathway diagram may indicate a theoretical ATP yield per substrate molecule. That stoichiometric potential differs from the actual ATP production rate of a cell, which depends on pathway flux, coupling, maintenance and competing uses. Dividing a substrate consumption rate by an assumed yield does not necessarily estimate energy available for growth. To make a credible rate calculation, one must identify the process, time units and independently measured stoichiometry under relevant conditions. The distinction prevents confusion between biochemical bookkeeping and a physiological performance claim.


## Synthesis: what a microbial growth curve can and cannot identify

A doubling-time calculation assumes a population that maintains one effective generation interval while net losses are negligible. Under that idealization, an initially counted population grows by the factor two raised to the elapsed time divided by the generation time. The corresponding specific exponential rate equals natural logarithm of two divided by the generation interval. The arithmetic can be correct while the model is inappropriate. A cell count from a real culture may rise slowly during physiological adjustment, accelerate, slow as conditions change, or decline. Optical density and viable counts measure related but nonidentical aspects of this history. A time series with biological replicates is needed to decide where an exponential approximation is defensible.

A saturating substrate-response function makes a different prediction. In a Monod-type representation, the specific growth rate approaches an upper bound as the named substrate concentration increases. The half-saturation constant is the substrate level at which the predicted response reaches half that upper bound. Neither parameter is a universal species constant; both depend on the experimental context and model fit. If oxygen or another nutrient becomes limiting, the one-substrate curve is insufficient. More importantly, a Monod fit is phenomenological: it summarizes a relationship but does not uniquely identify the molecular transporter or the limiting pathway. Different mechanisms may produce similar curves across a limited measurement range.

Mass and energy accounting complement both growth models. The yield of dry biomass per mass of consumed substrate is distinct from production rate per unit time or unit reactor volume. A process can show high yield but low productivity, and these differences matter in ecological comparisons and industrial interpretations. Carbon conservation, electron balances and nutrient composition place additional constraints on plausible conclusions. When interpreting microbial ecology, students should first identify what was measured, state the units, and then check whether the proposed mechanism predicts a pattern that could have been falsified by the available observations.


## Quantitative investigations: interactive models

### Ideal unrestricted population doubling

A controlled teaching model uses **Elapsed time (h)** and **Generation time (h)** to predict × initial population. Its stated relationship is **2^(time/generation time)**. No lag, death, nutrient exhaustion or population heterogeneity; relative counts only. At three generations the predicted multiplier is eight. Use the paired reference curve only to compare the stated parameter choice; it represents a mathematical counterfactual, not biological replicate evidence.

### Monod-type substrate response

A controlled teaching model uses **Substrate concentration (mg/L)** and **Half-saturation Ks (mg/L)** to predict h⁻¹. Its stated relationship is **0.8 × S/(Ks + S)**. Illustrative µmax=0.8/h and one limiting substrate; not an empirically fitted culture model. At S=Ks the predicted rate is half the specified upper rate. Use the paired reference curve only to compare the stated parameter choice; it represents a mathematical counterfactual, not biological replicate evidence.

## Fully worked problems

### Problem 3.1: Population doubling and rate

**Question.** An ideal population starts at one million cells, with a generation time of two hours. Calculate the predicted count at 6 hours and its exponential specific rate.

**Step 1.** Use n=t/g=6/2=3 generations and N=N0×2^n. The model assumes all generations complete, no deaths and stable generation time.

**Step 2.** N=1,000,000×2³=8,000,000 cells. The exponential rate is µ=ln2/g≈0.693147/2=0.3466 h⁻¹, giving the same result with N=N0 exp(µt).

**Step 3.** Explain the boundary: these are predictions only for ideal unrestricted growth. A real system may have lag, resource limitation, heterogeneous cells or counting error, none captured by a fixed-rate law.

### Problem 3.2: Monod saturation

**Question.** For µmax=0.8 per hour and Ks=20 mg/L, calculate the predicted specific growth rate at S=20 and 60 mg/L.

**Step 1.** Write µ=µmax×S/(Ks+S) with concentration S and half-saturation constant Ks in the same units; their ratio is dimensionless.

**Step 2.** At 20 mg/L, µ=0.8×20/40=0.4 h⁻¹. At 60 mg/L, µ=0.8×60/80=0.6 h⁻¹. Threefold substrate concentration increases rate only 1.5-fold in this saturating model.

**Step 3.** Do not interpret the values as measured for a species. The model neglects other limiting resources, toxicity and changing environmental conditions; validate µmax and Ks against data before applying it.

### Problem 3.3: Biomass yield versus productivity

**Question.** A hypothetical process consumes 40 g substrate, accumulates 12 g dry biomass and takes 8 hours in a 2 L system. Determine yield and volumetric productivity.

**Step 1.** Define yield Yx/s as mass dry biomass produced per mass substrate consumed, so Yx/s=12/40=0.30 g/g. This denominator is substrate, not total liquid volume.

**Step 2.** Volumetric productivity over the entire interval is 12 g/(2 L×8 h)=0.75 g L⁻¹ h⁻¹. An instantaneous rate would require a time-resolved measurement rather than this interval average.

**Step 3.** These quantities answer different questions. A larger yield may coexist with a lower productivity. Neither calculation accounts for dry biomass composition, byproducts or maintenance energy without further measurements.

