# Unit 3: Enzymes

## Conceptual introduction

Enzyme kinetics connects microscopic reaction mechanisms to laboratory measurements of time and concentration. The chemistry determines what bond changes can occur; the kinetic scheme determines how fast the observable products appear under defined conditions. Those statements are related but not equivalent. A catalyst accelerates approach to equilibrium without changing the equilibrium itself. A reaction that is thermodynamically downhill can still be negligible in an experiment if its activation barrier is large. Conversely, an enzyme can catalyze a reaction that proceeds predominantly in reverse under a particular concentration regime. Reaction direction, catalytic mechanism and measured flux must be distinguished explicitly.

The Michaelis–Menten expression is a powerful teaching model because it converts a mechanistic network into a saturating initial-velocity curve. Its hyperbolic shape follows specified approximations involving enzyme–substrate complex formation, catalytic conversion, steady state and negligible reverse product effects. The curve has two accessible limiting forms. At low substrate concentration, the velocity is approximately proportional to substrate, with slope Vmax/Km. At high substrate concentration, velocity approaches Vmax. Neither limit by itself identifies all microscopic rate constants. A reported Km is an apparent composite parameter for the chosen kinetic scheme; in the ordinary Briggs–Haldane mechanism it includes turnover as well as binding and dissociation.

Strong experimental design begins by checking that the measured signal really reports product formation. Many enzyme studies use a secondary reaction to convert invisible chemical changes into an optical or fluorescent readout. If the coupling reaction becomes limiting, a false saturation curve can appear. If a candidate inhibitor absorbs at the reporting wavelength, apparent inhibition can arise without any change in catalysis. A useful control introduces a known amount of product directly into the detection system, with and without the tested compound. Another control compares the direct chemical product with the indirect signal. These controls probe assay validity, not the enzyme mechanism, and should be presented as distinct lines of evidence.

Substrate titration works best when concentrations span both sides of the expected Km. At very low concentration the measurements may be noisy; at extremely high concentration substrate inhibition, solvent changes or viscosity effects may arise. The measured time interval also matters. An initial velocity assumes that substrate depletion, product rebinding, enzyme inactivation and heating have not yet altered the conditions appreciably. If the progress curve bends, fitting one straight line across the whole time range can produce an arbitrary rate. Repeating time courses at selected substrate levels provides more information than adding many replicate endpoint measurements under one condition.

Inhibitors modify kinetic parameters according to their mechanism. Classical competitive inhibition increases apparent Km while leaving asymptotic Vmax the same; mixed and uncompetitive schemes change other combinations of apparent parameters. But a laboratory observation is not identical to a theoretical category. Enzyme aggregation, a time-dependent covalent reaction, substrate sequestration or an interfering detergent can all imitate portions of a simple inhibition plot. A responsible analysis compares candidate models, evaluates confidence intervals and asks which new experiment most sharply discriminates among them.

At the cellular level, kinetics becomes a network problem. Feedback metabolites, covalent modification and substrate transport can change the fraction of enzyme in active states. Pool concentration is not the same as flux. A metabolite that accumulates might be produced faster, consumed slower or transported differently. Allosteric regulation provides one molecular mechanism by which a pathway responds to changing conditions, but it must be interpreted alongside compartmentation, energy state and gene expression. Students should leave this unit capable of fitting a rate curve and, more importantly, capable of stating what the fitted rate curve cannot yet prove.


## 3.1 Transition states and catalysis

### Chemical mechanism and material constraints

Enzymes accelerate reactions by lowering the free-energy barrier along a productive reaction pathway. Stabilizing relevant transition-state interactions is one mechanism, along with appropriate orientation, general acid–base chemistry, covalent intermediates and metal-ion participation. An enzyme does not change the equilibrium constant of a net reaction because it accelerates forward and reverse routes compatible with the same thermodynamics.

Rate constants often depend on activation free energy through an exponential relation; small energetic changes can therefore cause substantial rate changes. At ordinary temperatures, differences of only a few kilojoules per mole can have measurable consequences, but comparing observed velocities across enzymes requires controlling substrate concentration and the number of active sites.

### Quantitative and experimental reasoning

Choose a substrate analog designed to distinguish general acid–base catalysis from a purely binding-based explanation. Measure pH-dependent kinetic changes with an independent binding assay if possible; changed catalysis and changed affinity can generate similar velocity differences.

Use a pre–steady-state kinetic experiment to capture transient intermediates if a proposed mechanism predicts accumulation. A steady-state assay collapses multiple elementary steps into an apparent overall rate and may not identify which step limits turnover.

### Limits of inference and neighboring pathways

Active-site mutations can reveal which chemical groups are important, but reduced activity alone does not prove a direct catalytic role. A substitution can unfold a local region, weaken substrate binding, change oligomerization or disrupt metal incorporation.

An effective classroom explanation identifies the elementary bond changes, the energy landscape and the assumptions connecting them to measured kinetics. Merely saying that an enzyme “makes a reaction easier” hides why orientation, solvent organization and chemical states matter.

### Applied laboratory scenario

A candidate catalytic residue is changed to alanine and the reaction rate falls 100-fold. The laboratory separately measures substrate dissociation, enzyme folding and metal occupancy. If these also change, the drop in activity cannot isolate transition-state stabilization. An alternate mutation that preserves polarity but changes geometry may reveal a different pattern. Solvent isotope effects and pH dependence can support, but rarely uniquely identify, general acid–base catalysis. A mechanistic proposal should predict a chemically plausible transition state or intermediate that is consistent with stoichiometry. The team presents a reaction-coordinate diagram that distinguishes activation free energy from the overall equilibrium free-energy difference.

### Counterfactual interpretation and discrimination

A mutation substantially changes kcat but barely changes Km. It is tempting to conclude that substrate binding is unchanged, but Km depends on turnover as well as binding in the simple steady-state mechanism. Direct measurement of Kd or kon and koff is needed to establish a binding interpretation. A single altered rate parameter can also emerge from a different rate-limiting step, not just from slower chemistry at the transition state. Compare pre-steady-state behavior and isotope effects. State explicitly which physical property each experiment interrogates, and avoid treating a model parameter as though it were a direct molecular photograph.


## 3.2 Michaelis–Menten kinetics

### Chemical mechanism and material constraints

For E+S reversible binding followed by product formation, the Briggs–Haldane steady-state approximation yields v=Vmax[S]/(Km+[S]) under an initial-rate regime with appropriate mixing, negligible product effects and substrate in sufficient excess. Km is (koff+kcat)/kon for this simple mechanism. Km is not automatically the dissociation constant of substrate binding.

At [S]=Km the initial velocity is half Vmax; at concentrations much smaller than Km, v is approximately proportional to [S]. At concentrations far above Km, enzyme saturation produces an approach to Vmax. The ratio kcat/Km captures apparent catalytic efficiency at low substrate and becomes a particularly useful comparison when enzymes operate well below saturation.

### Quantitative and experimental reasoning

Collect initial-rate measurements across substrate concentrations around the suspected Km and include replicate blank-corrected readings. Check linearity of product against time before estimating an initial slope. Substrate inhibition, depletion, product rebinding, enzyme degradation and coupling-assay bottlenecks can all violate the hyperbolic model.

To compare two enzyme preparations, normalize Vmax by the estimated concentration of active enzyme if the goal is kcat. Total protein mass does not establish active-site count; inactive aggregates and contaminating proteins can bias a nominal turnover number.

### Limits of inference and neighboring pathways

Fit velocities by nonlinear regression using a specified error model rather than relying on a Lineweaver–Burk reciprocal plot, which strongly amplifies uncertainty at low substrate concentration. Inspect residuals and report uncertainty for both Km and Vmax.

The common mechanistic trap is to infer “high affinity” from a small Km without checking whether chemical conversion is fast relative to dissociation. Compare an independently estimated Kd to Km if the distinction matters in a particular system.

### Applied laboratory scenario

A course laboratory assays enzyme velocity at five substrate concentrations and obtains a curved trend. A reciprocal plot suggests an extraordinarily high Vmax, but the lowest-substrate measurement had the greatest relative error. The group refits the original velocities using weighted nonlinear regression, extends the range around the inferred Km and inspects reaction progress during the first minute. An apparent plateau can be caused by substrate inhibition, enzyme instability or the coupled detection reagent becoming rate limiting. The experiment reports both raw measurements and the fitted equation, together with uncertainty. The students then predict which additional substrate values would best separate alternative kinetic models.

### Counterfactual interpretation and discrimination

An experiment estimates Km from one pair of substrate and velocity values by assuming Vmax from a separate assay. The inference may be algebraically possible but unstable if the velocity is near Vmax or the separate preparation differs. A better study measures many initial velocities and repeats near the transition from linear to saturating response. Plot residuals against substrate concentration. If residuals curve systematically, consider substrate inhibition, multiple enzyme forms or product accumulation. Uncertainty in active enzyme count affects kcat more directly than it affects the shape of one normalized saturation curve. Reporting confidence intervals protects against false precision.


## 3.3 Enzyme inhibition

### Chemical mechanism and material constraints

An inhibitor may compete for the substrate binding region, bind an allosteric site, stabilize an inactive state or react covalently. The classical competitive model raises the apparent Km while leaving Vmax unchanged because sufficient substrate can overcome reversible competition. This statement assumes a simple competitive scheme and valid initial-rate measurements.

For the competitive mechanism with inhibitor concentration [I] and inhibition constant Ki, define alpha=1+[I]/Ki. The initial velocity is Vmax[S]/(alpha Km+[S]). A graphical displacement of the saturation curve to higher substrate concentration is a model prediction, not a guarantee of mechanism when the enzyme has multiple sites or conformations.

### Quantitative and experimental reasoning

Mixed, uncompetitive and time-dependent inhibition have different signatures. In a general mixed model, inhibitor can bind both free enzyme and enzyme–substrate complex. A change in apparent Vmax alone does not uniquely identify noncompetitive inhibition because enzyme loss, aggregation and assay interference can produce similar effects.

Reversible inhibitors can be distinguished from certain irreversible effects through dilution or dialysis tests, but some slow-binding reversible compounds recover only after long periods. Covalent identification or mass spectrometry provides different evidence from a kinetic curve.

### Limits of inference and neighboring pathways

Test inhibitor potency at several substrate concentrations, not just one. Include controls for inhibitor absorbance, fluorescence quenching, aggregation and solvent effects. A compound that changes the signal of a coupled assay may have no effect on the enzyme of interest.

Interpret an IC50 within its assay context. It generally varies with substrate concentration and mechanism, and should not be substituted directly for Ki without checking an appropriate model and assumptions.

### Applied laboratory scenario

A chemical library hit decreases the colorimetric rate of an enzyme in vitro. Before calling the molecule an inhibitor, the investigators add it to a sample containing product but no enzyme. The dye signal also falls, revealing interference with the reporter system. They move to an orthogonal measurement of product by chromatography and compare rates at multiple substrate concentrations. A reversible competitive pattern becomes plausible only if increasing substrate progressively offsets the rate decrease under appropriate conditions. Because inhibition models are mechanistic simplifications, a good report does not infer an intracellular drug effect solely from a one-point in vitro IC50.

### Counterfactual interpretation and discrimination

An inhibitor has an IC50 of 10 micromolar in one assay and 40 micromolar when substrate concentration increases. A reversible competitive scheme could explain the direction, but potency might also depend on nonspecific binding, assay duration or compound depletion. Test whether the molecule remains soluble at both concentrations and whether enzyme mass influences apparent potency. Use a matrix of substrate and inhibitor conditions rather than a single curve. An inhibitor binding to both E and ES can display more complicated behavior than the textbook competitive model. Mechanism should follow global model comparison and orthogonal measurement, not simply the observation that IC50 changed.


## 3.4 Allostery and pathway regulation

### Chemical mechanism and material constraints

Allosteric regulation arises when binding or modification at one site alters an ensemble of states that influences function elsewhere. Multiple subunits, concerted conformational transitions and sequential changes can all produce cooperative behavior. Feedback inhibition can prevent unnecessary synthesis by allowing an end product to influence an upstream committed step.

A Hill-type expression, v/Vmax=[S]^n/(K_half^n+[S]^n), illustrates how steepness changes with an empirical exponent n. It is phenomenological: n need not equal a count of physical binding sites. A response that appears cooperative can reflect the entire pathway rather than allostery within a single purified enzyme.

### Quantitative and experimental reasoning

Measure the effect of a regulatory metabolite using purified components and compare with cellular flux changes after perturbation. Cells contain transport, phosphorylation, sequestration and competing reactions, so a change in metabolite concentration may not reproduce the isolated enzyme response.

A single metabolite concentration cannot identify pathway flux. A metabolite pool may accumulate when production increases or when consumption decreases. Stable-isotope tracing, enzyme activity and time-resolved perturbations provide complementary constraints on reaction directions and magnitudes.

### Limits of inference and neighboring pathways

Enzymes can also be regulated by reversible phosphorylation, proteolysis, compartmentalization and substrate availability. Distinguish regulation of enzyme abundance from regulation of activity per molecule because the two have different timescales and feedback consequences.

The most informative biochemical model states what input controls a sensor, how the regulator changes catalysis and where the response closes a feedback loop. Without those links, a pathway diagram is only a list of arrows.

### Applied laboratory scenario

A metabolic enzyme displays a sigmoidal substrate-rate curve in crude lysate but becomes almost hyperbolic when purified. The initial explanation invokes cooperativity, yet the discrepancy could result from a second enzyme that removes substrate or generates an inhibitor. The researchers add back defined lysate fractions and independently measure the concentration of the proposed metabolite regulator. They compare mutant subunits and phosphorylation states while preserving active protein concentration. A sigmoidal curve is a property of the observed system and its assay conditions, not by itself proof of four cooperative binding sites. The case motivates distinguishing molecular allostery, network feedback and sample heterogeneity.

### Counterfactual interpretation and discrimination

A pathway responds sharply to small changes in a metabolite even though the purified regulatory enzyme shows only mild cooperative behavior. Network feedback and competition for substrates can amplify a weak molecular change. Construct a mass-balance map including the pool that is measured and enzymes that produce and consume it. Perturb the putative feedback metabolite independently of substrate addition, if feasible. A slope measured from whole-cell output must not be assigned to the binding stoichiometry of a particular enzyme. Distinguishing direct regulation from system-level amplification is essential when predicting how a pathway will behave after a genetic perturbation.


## Quantitative model studio

### Model 1: Michaelis–Menten initial velocity

The Michaelis–Menten model uses the familiar steady-state expression v=Vmax S/(Km+S). The graph starts at zero, reaches half the stated Vmax when S=Km and asymptotically approaches Vmax as substrate becomes large. This is a model of initial reaction velocity under defined conditions, not total product after an arbitrary interval. At S=3 mM with Km=3 mM and Vmax=12 micromoles per minute, the output is 6 micromoles per minute. Doubling S to 6 mM increases v to 8, not 12, demonstrating diminishing returns as saturation grows. One can derive a useful sensitivity by differentiating: dv/dS=Vmax Km/(Km+S)^2, which decreases as substrate increases. In the laboratory, select several substrate concentrations on either side of Km and confirm that product formation is approximately linear over the interval used to estimate each initial slope. Substrate depletion and product accumulation violate assumptions before the model itself need be incorrect. Residual analysis and repeat measurements should accompany fitted kinetic parameters.

Investigation challenge: inspect the velocity curve near zero substrate and at substrate well above Km. Show that the low-substrate slope approaches Vmax/Km by substituting S much smaller than Km, while high-substrate increments produce diminishing changes. Measure three replicate slopes from product time courses at a substrate below Km, near Km and above Km. If the estimated velocity falls at the highest substrate, compare substrate inhibition and reporter saturation as alternatives. Do not extend the Michaelis–Menten equation beyond its support merely to keep an elegant plot. The scientifically useful model is the simplest one that fits controlled observations without systematic residual patterns.

**Underlying relation:** v=Vmax[S]/(Km+[S]); Vmax=12 µmol/min, Km=3 mM.

### Model 2: Competitive inhibitor initial velocity

Competitive inhibition in this model raises the effective substrate concentration scale by α=1+I/Ki. The selected substrate is held at 5 mM while inhibitor concentration I varies; Km remains 3 mM, Ki=2 mM and Vmax=12 micromoles per minute. With no inhibitor the rate is 12×5/(3+5)=7.5. At inhibitor I=2 mM, α=2 and v=60/11, approximately 5.455. This is a declining curve because the inhibitor competes for a binding mode needed for catalysis. The classical competitive scheme predicts that a sufficiently large substrate concentration can largely overcome the inhibition, unlike a loss of active enzyme concentration. A strong experiment therefore repeats entire substrate titrations at several inhibitor levels. Testing only a single substrate concentration cannot cleanly separate competitive behavior from several alternatives. The slider shows a reversible competitive model, not time-dependent covalent inhibition or aggregation. Careful controls check whether the inhibitor modifies the optical readout rather than the enzyme.

Investigation challenge: set inhibitor to zero and record the reference velocity. Double the inhibitor concentration twice while keeping substrate fixed. Explain why the observed decrease is nonlinear: inhibitor increases the effective apparent Km, which enters the denominator alongside fixed substrate. Next predict what would happen if substrate, rather than inhibitor, increased at fixed I. Classical competitive inhibition can be overcome at sufficiently large S, unlike an actual removal of catalytically competent enzyme molecules. A useful control is to add inhibitor after product has already formed; if it alters the reporting signal, apparent inhibition may not reflect enzymatic chemistry. The comparison should identify model assumptions and differentiate Ki from an empirically measured IC50.

**Underlying relation:** v=Vmax[S]/(Km(1+I/Ki)+[S]); [S]=5 mM, Ki=2 mM.


## Integrative fieldwork

Integrated investigation: an enzyme preparation loses activity after addition of a test compound. The task is to discriminate reversible competitive inhibition, enzyme degradation, reporter interference and slow-binding effects. Begin with a direct assay of product identity or a validated independent reporter. Measure a short time course rather than relying only on a single endpoint. If activity decays progressively, preincubation and dilution experiments become particularly informative. Collect full substrate titrations at several inhibitor concentrations and estimate parameters from untransformed velocity data, reporting residual trends. Competitive inhibition should show a pattern compatible with increased apparent Km in the classical model, but this signature must be interpreted in the context of active enzyme concentration and substrate depletion. Include a control that adds the compound directly to a known quantity of product in the reporter system; decreased detector signal there is evidence for assay interference. A second control checks whether activity recovers after removal of compound, recognizing that slow reversible binding may require extended observation. Examine protein aggregation and stability when possible. The final decision tree separates observations consistent with each mechanism from observations that actually rule mechanisms out. An ideal result may leave two plausible explanations; that is a scientifically useful finding if the next discriminating experiment is specified.


## Worked questions and solutions

### Question 1: Michaelis–Menten rate

For Vmax=12 µmol/min, Km=3 mM and [S]=6 mM, calculate initial reaction velocity.

1. Use v=Vmax[S]/(Km+[S]).

2. Insert numbers v=12×6/(3+6)=72/9.

3. v=8 µmol/min. Confirm this is below Vmax and above Vmax/2 because [S]>Km.

### Question 2: Competitive inhibitor

At Vmax=12 µmol/min, Km=3 mM, [S]=5 mM, inhibitor I=4 mM and Ki=2 mM, find v.

1. Compute α=1+[I]/Ki=1+4/2=3.

2. v=Vmax[S]/(αKm+[S])=12×5/(3×3+5)=60/14.

3. v≈4.2857 µmol/min; the inhibited rate is below the uninhibited 7.5 µmol/min.

### Question 3: Turnover number

An enzyme preparation contains 0.020 µmol of genuinely active enzyme sites and reaches Vmax=1.8 µmol product/min. Calculate kcat.

1. kcat=Vmax/[E]active, with both quantities expressed in compatible molar units.

2. 1.8 µmol/min ÷0.020 µmol=90 min−1.

3. In seconds kcat=90/60=1.5 s−1. Counting inactive protein would underestimate the active-site turnover.

