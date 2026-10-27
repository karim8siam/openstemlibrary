# Unit 7: Characterization, data interpretation and quality

**Guiding question:** Which combinations of analytical methods can establish chemical, thermal and mechanical claims?

## Why this unit matters to polymer science

A manufacturer reports changed DSC melting enthalpy and narrow SEC peaks while field fracture defects are increasing. This is a question about **measurement traceability and orthogonality** and the distinction between **a neat instrument trace versus a supported structure–property conclusion**. A defensible answer identifies chain chemistry, molecular distribution, processing path and morphology before comparing measured properties. It also names the potentially controlling failure mode: a formulation that optimizes short-term stiffness, melt-flow index or optical clarity can still worsen creep resistance, process stability, environmental cracking or barrier lifetime. The technical sections below connect simplified mathematics to the kinds of measurements that would justify a practical claim.

A full analytical conclusion is a cross-consistent account of mass, composition, structure and property, each with stated instrument response and uncertainty.

Flag apparent versus absolute SEC molar masses, heat-flow baseline choices and whether test replicates truly sample process-batch variability.

## Measurement and conservation checkpoints

Write down the starting chain chemistry, distribution, additive package and processing history; define whether reported fractions are by area, mass, moles or volume; and record the process history that could alter **detector calibration, baseline, replicate hierarchy and lot**. For any local observation, describe why its sampling plan represents the part. Treat **apparent SEC calibration or unrepresentative defect sampling** as an explicit rival explanation and plan **orthogonal chemistry, thermal and fracture tests** as an independent check.

## Lesson 7.1: Size-exclusion chromatography and calibration

### Scientific foundation

Size-exclusion chromatography separates dissolved macromolecules primarily according to hydrodynamic volume in a selected solvent and column set. Conventional calibration with narrow standards produces apparent molar masses relative to those standards, which may be biased for branched or chemically different polymers. Multiangle light scattering and viscometry can add information but require concentration, dn/dc and other calibration details. Insoluble gel fractions and shear-degraded chains may be excluded from the reported profile.

**Governing relationship or decision rule:** Empirical SEC calibration may be expressed log10(M_app)=A−Bt over a strictly validated retention interval. Read every term in the equation as part of a declared specimen condition. In **size-exclusion chromatography and calibration**, a valid calculation requires the chain and microstructural state of the polymer, unit system and physical or geometrical meaning of each quantity. A nominally identical repeat-unit formula can conceal different chain-length distributions, branches, additives, crystallinity and processing damage. Equal average molar mass does not guarantee equivalent creep resistance, permeability or thermal transitions. Interpret measurements only after identifying which feature of the state they can support.

### Worked polymer investigation

For a fictional log-linear calibration log10(M/g mol−1)=7.2−0.12t with retention t in minutes, estimate values at 15, 20 and 25 min. Discuss why earlier elution is associated with larger hydrodynamic molecules for size exclusion but not necessarily an absolutely known molar mass. Compare a branched and linear resin at matched SEC elution volume.

A companion calculator called **Illustrative SEC calibration curve** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Retention time = 14.85714 min**, the declared formula returns **261302.07 apparent g/mol**; at **Retention time = 17.71429 min**, it returns **118654.91 apparent g/mol**. On this interval the modeled value decreases, and the two-point slope is **-49926.507 apparent g/mol per min**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real polymer grade.

The browser expression is `Math.pow(10,7.2-0.12*t)`. Model validity is limited to: **Fictional log-linear apparent molar mass calibration; only valid in selected retention window under unspecified demo chromatography conditions**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

Calibrations are specific to solvent, temperature, column performance and detectors; the toy line cannot be transferred to real chromatograms. A single narrow peak cannot prove absence of insoluble crosslinks.

### Exercises and self-assessment

**Exercise 7.1A — Physical mechanism.** Why can conventional SEC assign different molar masses to branched and linear chains that actually have equal absolute molar mass? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 7.1B — Numerical cross-check.** Recalculate **261302.07 apparent g/mol** from the companion formula at **14.85714 min** and compare with **118654.91 apparent g/mol** at **17.71429 min**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real polymer specimen.

**Exercise 7.1C — Test design.** Propose a synthesis, processing or test matrix that addresses **apparent SEC calibration or unrepresentative defect sampling**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_12 -->

## Lesson 7.2: Spectroscopy: chemistry, sequence and reaction

### Scientific foundation

FTIR identifies bond vibrations and NMR probes local chemical environments, allowing confirmation of repeat units, functional groups and some comonomer sequences. Peak assignment requires overlapping bands, sample thickness and baseline choices to be addressed. A carbonyl-band increase can indicate oxidation for a controlled formulation but may already originate from additives or copolymer content. NMR integrated signals need appropriate acquisition and relaxation conditions to support composition quantification.

**Governing relationship or decision rule:** Under validated Beer–Lambert conditions, absorbance A=ε c l; scattering and heterogeneous specimens require corrections. Read every term in the equation as part of a declared specimen condition. In **spectroscopy: chemistry, sequence and reaction**, a valid calculation requires the chain and microstructural state of the polymer, unit system and physical or geometrical meaning of each quantity. A nominally identical repeat-unit formula can conceal different chain-length distributions, branches, additives, crystallinity and processing damage. Equal average molar mass does not guarantee equivalent creep resistance, permeability or thermal transitions. Interpret measurements only after identifying which feature of the state they can support.

### Worked polymer investigation

Design an experiment to check whether annealing changed chemistry or only crystalline packing. Pair controlled FTIR and NMR with DSC; report baseline-corrected peak ratios and replicate spectra. For a suspected hydrolysis process, use end-group change and SEC as corroborating observations instead of claiming bond scission solely from a single absorbance change.

A companion calculator called **Ideal DSC crystallinity estimate** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Melting enthalpy per sample mass = 42.85714 J/g**, the declared formula returns **26.785714 % crystallinity**; at **Melting enthalpy per sample mass = 64.28571 J/g**, it returns **40.178571 % crystallinity**. On this interval the modeled value increases, and the two-point slope is **0.625 % crystallinity per J/g**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real polymer grade.

The browser expression is `100*H/(0.8*200)`. Model validity is limited to: **Hypothetical 80% polymer mass, reference fusion enthalpy 200 J/g-polymer, no cold crystallization, baseline or multiple-phase issues**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

ATR-FTIR probes a near-surface region, not necessarily a thick specimen core. Spectral changes can arise from orientation, crystallinity and instrument contact.

### Exercises and self-assessment

**Exercise 7.2A — Physical mechanism.** How would you distinguish increased carbonyl absorbance from a genuine rise in oxidative scission for a filled polymer? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 7.2B — Numerical cross-check.** Recalculate **26.785714 % crystallinity** from the companion formula at **42.85714 J/g** and compare with **40.178571 % crystallinity** at **64.28571 J/g**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real polymer specimen.

**Exercise 7.2C — Test design.** Propose a synthesis, processing or test matrix that addresses **apparent SEC calibration or unrepresentative defect sampling**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_13 -->

## Lesson 7.3: Thermal analysis: DSC, DMA and TGA

### Scientific foundation

DSC measures heat flow associated with transition and reaction events; DMA follows temperature and frequency-dependent stiffness and damping; TGA measures mass under specified thermal and gas conditions. These instruments are complementary, not interchangeable. DSC may show a cold-crystallization exotherm preceding melting; ignoring it can overestimate pre-existing crystalline fraction. DMA loss peaks depend on frequency and criterion; TGA onset depends on mass threshold and heating rate.

**Governing relationship or decision rule:** Xc=(ΔHm−ΔHcc)/(w ΔHm,100%) for appropriate signs and baseline conventions; the slider sets ΔHcc=0. Read every term in the equation as part of a declared specimen condition. In **thermal analysis: dsc, dma and tga**, a valid calculation requires the chain and microstructural state of the polymer, unit system and physical or geometrical meaning of each quantity. A nominally identical repeat-unit formula can conceal different chain-length distributions, branches, additives, crystallinity and processing damage. Equal average molar mass does not guarantee equivalent creep resistance, permeability or thermal transitions. Interpret measurements only after identifying which feature of the state they can support.

### Worked polymer investigation

For a sample containing 80% polymer by mass and ideal perfect-crystal melting enthalpy 200 J/g-polymer, calculate nominal crystallinity from observed fusion enthalpy ΔHm=80 J/g-sample: Xc=80/(0.8×200)=0.50. Repeat for another value and state when subtraction of cold-crystallization enthalpy is necessary. Design first- and second-heating scans to separate process history.

A companion calculator called **Illustrative SEC calibration curve** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Retention time = 20.57143 min**, the declared formula returns **53880.122 apparent g/mol**; at **Retention time = 23.42857 min**, it returns **24466.476 apparent g/mol**. On this interval the modeled value decreases, and the two-point slope is **-10294.776 apparent g/mol per min**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real polymer grade.

### Evidence, uncertainty, and a competing mechanism

A reference enthalpy is chemistry-specific, and DSC baseline selection, overlapping transitions and additives contribute uncertainty. A TGA onset temperature does not certify continuous service temperature.

### Exercises and self-assessment

**Exercise 7.3A — Physical mechanism.** Why can first-heating and second-heating DSC traces differ strongly even when chemical composition remains constant? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 7.3B — Numerical cross-check.** Recalculate **53880.122 apparent g/mol** from the companion formula at **20.57143 min** and compare with **24466.476 apparent g/mol** at **23.42857 min**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real polymer specimen.

**Exercise 7.3C — Test design.** Propose a synthesis, processing or test matrix that addresses **apparent SEC calibration or unrepresentative defect sampling**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_12 -->

## Lesson 7.4: Scattering, microscopy and multiscale morphology

### Scientific foundation

Optical microscopy resolves spherulites and large defects, while SAXS captures mesoscale density correlations such as lamellar long periods and WAXS probes crystalline lattice spacings. Electron microscopy can reveal fracture morphology or filler dispersion at shorter scales, subject to preparation artifacts. Each technique reports a limited reciprocal or real-space window; one peak or one micrograph cannot specify an entire hierarchical structure.

**Governing relationship or decision rule:** For a dominant one-dimensional scattering peak q*, the associated real-space repeat distance is approximately d=2π/q*, with texture and structural assumptions. Read every term in the equation as part of a declared specimen condition. In **scattering, microscopy and multiscale morphology**, a valid calculation requires the chain and microstructural state of the polymer, unit system and physical or geometrical meaning of each quantity. A nominally identical repeat-unit formula can conceal different chain-length distributions, branches, additives, crystallinity and processing damage. Equal average molar mass does not guarantee equivalent creep resistance, permeability or thermal transitions. Interpret measurements only after identifying which feature of the state they can support.

### Worked polymer investigation

Use combined polarized optical microscopy, SAXS and WAXS on an annealed semicrystalline film. Predict which technique can test increasing spherulite radius, which measures lamellar periodicity, and which measures lattice unit-cell changes. Verify results on multiple sections and orientations rather than a single attractive image.

A companion calculator called **Ideal DSC crystallinity estimate** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Melting enthalpy per sample mass = 85.71429 J/g**, the declared formula returns **53.571429 % crystallinity**; at **Melting enthalpy per sample mass = 107.1429 J/g**, it returns **66.964286 % crystallinity**. On this interval the modeled value increases, and the two-point slope is **0.625 % crystallinity per J/g**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real polymer grade.

### Evidence, uncertainty, and a competing mechanism

SAXS spacing may include alternating crystal and amorphous regions and must not automatically equal crystalline lamellar thickness. Cutting or beam damage can create apparent voids.

### Exercises and self-assessment

**Exercise 7.4A — Physical mechanism.** Why can SAXS show a constant long period while optical spherulite size increases after annealing? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 7.4B — Numerical cross-check.** Recalculate **53.571429 % crystallinity** from the companion formula at **85.71429 J/g** and compare with **66.964286 % crystallinity** at **107.1429 J/g**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real polymer specimen.

**Exercise 7.4C — Test design.** Propose a synthesis, processing or test matrix that addresses **apparent SEC calibration or unrepresentative defect sampling**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_13 -->

## Lesson 7.5: Mechanical qualification and uncertainty

### Scientific foundation

Polymer property data are conditional on geometry, loading mode, thermal and moisture conditioning, production direction and testing speed. A quality system should separate calibration repeatability, specimen-to-specimen spread and batch-to-batch variability; reporting a single mean without the actual sample hierarchy understates uncertainty. A minimum performance threshold may require a lower confidence or tolerance bound, not merely a mean above specification.

**Governing relationship or decision rule:** Stress equals measured force divided by the specified area; reported uncertainty must propagate force, geometry, conditioning and lot variability. Read every term in the equation as part of a declared specimen condition. In **mechanical qualification and uncertainty**, a valid calculation requires the chain and microstructural state of the polymer, unit system and physical or geometrical meaning of each quantity. A nominally identical repeat-unit formula can conceal different chain-length distributions, branches, additives, crystallinity and processing damage. Equal average molar mass does not guarantee equivalent creep resistance, permeability or thermal transitions. Interpret measurements only after identifying which feature of the state they can support.

### Worked polymer investigation

Construct a nested test plan with at least three processing lots and multiple specimens per lot, identifying which conditions are randomized and which are blocked. Compare a universal test machine's force calibration to errors from specimen thickness and grip slippage. List predeclared rejection conditions and post-test fracture-origin evidence.

A companion calculator called **Illustrative SEC calibration curve** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Retention time = 26.28571 min**, the declared formula returns **11110.006 apparent g/mol**; at **Retention time = 29.14286 min**, it returns **5044.9532 apparent g/mol**. On this interval the modeled value decreases, and the two-point slope is **-2122.7684 apparent g/mol per min**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real polymer grade.

### Evidence, uncertainty, and a competing mechanism

Five adjacent samples from one molded plaque are not five independent production lots. A statistically narrow error bar from repeated readings cannot establish field reliability.

### Exercises and self-assessment

**Exercise 7.5A — Physical mechanism.** How can a highly repeatable lab value still be a poor predictor of manufacturing variation? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 7.5B — Numerical cross-check.** Recalculate **11110.006 apparent g/mol** from the companion formula at **26.28571 min** and compare with **5044.9532 apparent g/mol** at **29.14286 min**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real polymer specimen.

**Exercise 7.5C — Test design.** Propose a synthesis, processing or test matrix that addresses **apparent SEC calibration or unrepresentative defect sampling**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_12 -->

## Integrated investigation: A disputed batch rejection

### The evidence problem

A manufacturer reports changed DSC melting enthalpy and narrow SEC peaks while field fracture defects are increasing. The problem cannot be solved by selecting the equation that gives the most convenient number. First define which property must be achieved, the physical constraint that could prevent it, and the microstructural condition of the specimen being evaluated. List known facts separately from inferred mechanisms, uncertain constants and quantities not yet measured. The central decision is not simply which polymerization route or formulated resin seems attractive: it is what observations would allow a researcher or an engineer to prefer one explanation over competing causes.

### Integrated analysis and model workflow

Separate crystallinity, size exclusion calibration, additive concentration and rare flaw distributions. Build a minimal processing–structure–property map linking the material history with observed state and relevant response. Carry the distinction between **measurement traceability and orthogonality** and **a neat instrument trace versus a supported structure–property conclusion** through the map. For polymer mixing, show composition conservation and do not infer processing kinetics from a static phase diagram. For a melt-state relation, distinguish relaxation time from shear-rate-dependent flow and actual process heating. For chemical function, distinguish molecular diffusion, partitioning, chain mobility and chemical degradation. Use the actual specimen time–temperature history instead of only a machine-temperature set point. For damage, compare local flaw driving force with rate- and environment-dependent measured fracture resistance.

### Validation plan, report, and counterfactual

Use orthogonal spectroscopy, scattering, GPC/SEC calibration, mechanical replicates and fracture microscopy. Include an alternative interpretation capable of explaining the same first observation and choose a different instrument or held-out processing condition that separates it. State which measurement would cause you to reject the favored hypothesis. Retain raw counts, image scales, processing logs and sample identifiers. If comparing polymer families, write down the constraints that matter for stiffness, creep, permeability, thermal history and chemical exposure rather than reporting only one maximum strength metric.

**Known limits:** Instrument agreement is not evidence of sampling representative field failures unless specimen provenance is linked. A reader should be able to reconstruct the entire inference from original specimen provenance and measured inputs. The synthetic datasets intentionally contain no physical replicate scatter or hidden model mismatch; those omissions would make a real-world confidence interval far wider than a formula plot suggests.

### Five cumulative exam questions

1. Draw a cause-and-effect diagram linking composition, process history, **measurement traceability and orthogonality** and the decision-controlling property; mark one arrow that cannot yet be established from the observations.
2. Write a conservation or constitutive relation for **a neat instrument trace versus a supported structure–property conclusion** with all units and physical validity assumptions; interpret one limiting case.
3. Propose two mutually exclusive experimental signatures for the favored and competing mechanisms and name the required independent instruments.
4. Show how **apparent SEC calibration or unrepresentative defect sampling** could reverse a seemingly beneficial result, and design the minimum additional test needed to detect that reversal.
5. Write a one-paragraph evidence statement specifying what has been demonstrated, what is merely predicted, and which industrial decision is unjustified until qualification.

<!-- MODEL_13 -->

