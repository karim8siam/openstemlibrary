# Unit 4: Viscoelasticity, rheology and time-dependent response

**Guiding question:** Why do polymers respond differently as loading rate, temperature and timescale change?

## Why this unit matters to polymer science

A polymer seal passes initial compression testing but its clamping force decays during hot service. This is a question about **relaxation spectra and non-Newtonian flow** and the distinction between **instantaneous modulus versus long-time stress response**. A defensible answer identifies chain chemistry, molecular distribution, processing path and morphology before comparing measured properties. It also names the potentially controlling failure mode: a formulation that optimizes short-term stiffness, melt-flow index or optical clarity can still worsen creep resistance, process stability, environmental cracking or barrier lifetime. The technical sections below connect simplified mathematics to the kinds of measurements that would justify a practical claim.

Polymer viscoelasticity has timescales, not a single universal stiffness. Extensional strain hardening and long-time creep can diverge between formulations with the same nominal tensile modulus.

Explain whether each measurement controls stress, strain or rate and whether the response is transient, oscillatory or steady before comparing parameter values.

## Measurement and conservation checkpoints

Write down the starting chain chemistry, distribution, additive package and processing history; define whether reported fractions are by area, mass, moles or volume; and record the process history that could alter **time, temperature, humidity and specimen shear history**. For any local observation, describe why its sampling plan represents the part. Treat **wall slip or changing crystallinity** as an explicit rival explanation and plan **DMA and independent creep/relaxation measurement** as an independent check.

## Lesson 4.1: Linear viscoelasticity and constitutive elements

### Scientific foundation

A spring stores deformation energy and responds instantaneously under linear elasticity; a dashpot dissipates under a viscosity-proportional rate. Combining them as Maxwell or Kelvin–Voigt elements illustrates stress relaxation versus creep under small deformations. Real materials have distributions of relaxation times and nonlinearities, so a single mechanical analog should be presented as a minimal model. Temperature, molecular mass, crystallinity and physical aging shift the observed modulus.

**Governing relationship or decision rule:** Maxwell stress relaxation after a small step strain follows σ(t)=E0 ε0 exp(−t/τ), with τ=η/E0 for the ideal element. Read every term in the equation as part of a declared specimen condition. In **linear viscoelasticity and constitutive elements**, a valid calculation requires the chain and microstructural state of the polymer, unit system and physical or geometrical meaning of each quantity. A nominally identical repeat-unit formula can conceal different chain-length distributions, branches, additives, crystallinity and processing damage. Equal average molar mass does not guarantee equivalent creep resistance, permeability or thermal transitions. Interpret measurements only after identifying which feature of the state they can support.

### Worked polymer investigation

For an ideal single Maxwell element with E0=1000 MPa and relaxation time τ=10 seconds, estimate stress modulus E(t)=E0 exp(−t/τ) at t=0,10 and 30 seconds: 1000, about 368 and about 49.8 MPa. Discuss how a stress-controlled creep test differs from the imposed-strain relaxation case, and which test would distinguish multiple timescales.

A companion calculator called **Single Maxwell relaxation modulus** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Time after step strain = 7.142857 s**, the declared formula returns **489.54166 MPa**; at **Time after step strain = 14.28571 s**, it returns **239.65104 MPa**. On this interval the modeled value decreases, and the two-point slope is **-34.984687 MPa per s**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real polymer grade.

The browser expression is `1000*Math.exp(-t/10)`. Model validity is limited to: **Single small-strain Maxwell mode E0=1000 MPa, tau=10 s, temperature fixed; not a full relaxation spectrum**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

A single exponential ignores entanglement spectra, glass transitions and nonlinear strain. Do not fit relaxation time from only one noisy measurement.

### Exercises and self-assessment

**Exercise 4.1A — Physical mechanism.** Why can a polymer gasket lose sealing force under fixed compression even though its shape appears unchanged? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 4.1B — Numerical cross-check.** Recalculate **489.54166 MPa** from the companion formula at **7.142857 s** and compare with **239.65104 MPa** at **14.28571 s**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real polymer specimen.

**Exercise 4.1C — Test design.** Propose a synthesis, processing or test matrix that addresses **wall slip or changing crystallinity**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_6 -->

## Lesson 4.2: Time–temperature superposition

### Scientific foundation

Increasing temperature typically accelerates segmental motion, so frequency sweeps at several temperatures may shift horizontally to form a master curve when the material is thermorheologically simple. Shift factors are convention-sensitive and may follow a Williams–Landel–Ferry-type relation in a restricted range near Tg. Crystallization, chemical aging or different relaxation mechanisms can prevent reliable superposition. A master curve extends measurement timescale but is not automatically a lifetime prediction.

**Governing relationship or decision rule:** In one common convention log10(aT)=−C1(T−Tref)/(C2+T−Tref), for a temperature window where empirical fit is justified. Read every term in the equation as part of a declared specimen condition. In **time–temperature superposition**, a valid calculation requires the chain and microstructural state of the polymer, unit system and physical or geometrical meaning of each quantity. A nominally identical repeat-unit formula can conceal different chain-length distributions, branches, additives, crystallinity and processing damage. Equal average molar mass does not guarantee equivalent creep resistance, permeability or thermal transitions. Interpret measurements only after identifying which feature of the state they can support.

### Worked polymer investigation

Collect DMA storage and loss modulus over overlapping temperatures and frequencies and check whether one horizontal shift aligns both. Examine a semicrystalline resin before and after annealing. If shift factors produce inconsistent master curves, consider new crystallites or multiple transition processes rather than forcing a single WLF fit.

A companion calculator called **Power-law shear-thinning melt viscosity** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Shear rate = 285.7857 1/s**, the declared formula returns **10.41319 Pa s**; at **Shear rate = 428.6286 1/s**, it returns **8.8545716 Pa s**. On this interval the modeled value decreases, and the two-point slope is **-0.01091142 Pa s per 1/s**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real polymer grade.

The browser expression is `100*Math.pow(g,-0.4)`. Model validity is limited to: **Power-law synthetic fit with K=100 Pa s at 1/s, n=0.6; excludes Newtonian plateaus, shear heating, slip and melt fracture**. Reproduce the first result with a calculator using the expression and units stated here. Before accepting the number, check the units analytically and identify what is being held constant. If a result looks realistic, that coincidence does not establish physical validation. Try an extreme permitted slider input and ask whether the computed change is physically interpretable or an artifact of the simplifying assumptions.

### Evidence, uncertainty, and a competing mechanism

WLF constants depend on reference temperature and material; extrapolation decades beyond measured time can be unsafe. The Maxwell slider in this unit only shows one relaxation mode and does not perform empirical superposition.

### Exercises and self-assessment

**Exercise 4.2A — Physical mechanism.** Why is a visually smooth shifted modulus curve insufficient evidence that accelerated aging predicts ten-year performance? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 4.2B — Numerical cross-check.** Recalculate **10.41319 Pa s** from the companion formula at **285.7857 1/s** and compare with **8.8545716 Pa s** at **428.6286 1/s**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real polymer specimen.

**Exercise 4.2C — Test design.** Propose a synthesis, processing or test matrix that addresses **wall slip or changing crystallinity**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_7 -->

## Lesson 4.3: Melt viscosity and shear thinning

### Scientific foundation

Most polymer melts are shear-thinning: apparent viscosity declines when the applied shear rate disrupts stress-bearing chain conformations more rapidly than they recover. At low shear rates a Newtonian plateau may exist; at high rates flow can show wall slip, shear heating or melt fracture. A power-law η=K γdot^(n−1) represents a limited intermediate-rate window rather than a material identity. The melt may also exhibit significant extensional elasticity.

**Governing relationship or decision rule:** Over its fitted regime, shear stress τ=K γdot^n and apparent viscosity ηapp=K γdot^(n−1), 0<n<1 for shear thinning. Read every term in the equation as part of a declared specimen condition. In **melt viscosity and shear thinning**, a valid calculation requires the chain and microstructural state of the polymer, unit system and physical or geometrical meaning of each quantity. A nominally identical repeat-unit formula can conceal different chain-length distributions, branches, additives, crystallinity and processing damage. Equal average molar mass does not guarantee equivalent creep resistance, permeability or thermal transitions. Interpret measurements only after identifying which feature of the state they can support.

### Worked polymer investigation

For a pedagogical shear-thinning law η=100 γdot^(−0.4) Pa·s when γdot is expressed relative to 1 s−1, compute apparent viscosity at 1, 10 and 100 s−1. Compare the ratio with experimental capillary or rotational measurements and state which corrections are needed for true wall shear rate.

A companion calculator called **Single Maxwell relaxation modulus** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Time after step strain = 21.42857 s**, the declared formula returns **117.31917 MPa**; at **Time after step strain = 28.57143 s**, it returns **57.432619 MPa**. On this interval the modeled value decreases, and the two-point slope is **-8.3841166 MPa per s**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real polymer grade.

### Evidence, uncertainty, and a competing mechanism

Power-law viscosity diverges as γdot approaches zero and omits terminal relaxation, temperature dependence and pressure. Do not apply the slider's bounds to safe extruder settings.

### Exercises and self-assessment

**Exercise 4.3A — Physical mechanism.** Why can the same polymer show lower apparent shear viscosity but worse extrudate surface quality at higher throughput? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 4.3B — Numerical cross-check.** Recalculate **117.31917 MPa** from the companion formula at **21.42857 s** and compare with **57.432619 MPa** at **28.57143 s**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real polymer specimen.

**Exercise 4.3C — Test design.** Propose a synthesis, processing or test matrix that addresses **wall slip or changing crystallinity**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_6 -->

## Lesson 4.4: Extensional flow and strain hardening

### Scientific foundation

Fiber spinning, film blowing and foam-cell growth involve extensional motion, not just shear. A polymer with long-chain branches can show substantial extensional strain hardening even when its steady shear curves resemble a linear analog. This helps stabilize a stretched melt against local necking, but high elasticity can also cause die swell and flow instability. A single capillary viscosity curve cannot characterize extension-dominated processes.

**Governing relationship or decision rule:** In uniaxial flow, transient extensional viscosity is tensile stress difference divided by imposed extension rate; the linear Trouton ratio of three applies only to a Newtonian fluid. Read every term in the equation as part of a declared specimen condition. In **extensional flow and strain hardening**, a valid calculation requires the chain and microstructural state of the polymer, unit system and physical or geometrical meaning of each quantity. A nominally identical repeat-unit formula can conceal different chain-length distributions, branches, additives, crystallinity and processing damage. Equal average molar mass does not guarantee equivalent creep resistance, permeability or thermal transitions. Interpret measurements only after identifying which feature of the state they can support.

### Worked polymer investigation

Compare two resins with similar zero-shear viscosities but different long-chain branching. Measure transient extensional viscosity using a filament-stretching or contraction-flow method while controlling temperature and prior deformation. Discuss whether differences in film bubble stability align with extensional behavior rather than ordinary shear viscosity.

A companion calculator called **Power-law shear-thinning melt viscosity** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Shear rate = 571.4714 1/s**, the declared formula returns **7.8922747 Pa s**; at **Shear rate = 714.3143 1/s**, it returns **7.2184552 Pa s**. On this interval the modeled value decreases, and the two-point slope is **-0.004717208 Pa s per 1/s**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real polymer grade.

### Evidence, uncertainty, and a competing mechanism

Filament tests can suffer nonuniform strain, necking, evaporation or thermal gradients. The shear-thinning model attached to this unit is not a predictor of extensional strain hardening.

### Exercises and self-assessment

**Exercise 4.4A — Physical mechanism.** Why is extensional rheology more informative than steady shear viscosity when choosing a film-blowing grade? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 4.4B — Numerical cross-check.** Recalculate **7.8922747 Pa s** from the companion formula at **571.4714 1/s** and compare with **7.2184552 Pa s** at **714.3143 1/s**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real polymer specimen.

**Exercise 4.4C — Test design.** Propose a synthesis, processing or test matrix that addresses **wall slip or changing crystallinity**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_7 -->

## Lesson 4.5: Creep, recovery and permanent set

### Scientific foundation

Under sustained load, polymers can strain over time even when the initial applied stress is below conventional yield. Recoverable delayed strain, viscoplastic flow, physical aging and damage need not share the same time dependence. For design, compare creep compliance under a specified stress and temperature rather than reporting only short-term tensile modulus. Recovery testing can separate reversible response from permanent set but interpretation depends on recovery duration.

**Governing relationship or decision rule:** In linear viscoelasticity ε(t)=σ0 J(t); J(t) is creep compliance and depends on test history and thermodynamic state. Read every term in the equation as part of a declared specimen condition. In **creep, recovery and permanent set**, a valid calculation requires the chain and microstructural state of the polymer, unit system and physical or geometrical meaning of each quantity. A nominally identical repeat-unit formula can conceal different chain-length distributions, branches, additives, crystallinity and processing damage. Equal average molar mass does not guarantee equivalent creep resistance, permeability or thermal transitions. Interpret measurements only after identifying which feature of the state they can support.

### Worked polymer investigation

Plan a stepped creep–recovery test for a flexible component: condition at controlled humidity and temperature, apply several stress levels below and near practical limits, then unload while tracking strain for long enough to observe recovery. Compare a strain-time curve for Maxwell-like flow with one that reaches a plateau.

A companion calculator called **Single Maxwell relaxation modulus** supplies a separate, deliberately limited numerical experiment. Its controls isolate one effect so a reader can check dimensions and sensitivity instead of guessing the direction of change. At **Time after step strain = 35.71429 s**, the declared formula returns **28.11566 MPa**; at **Time after step strain = 42.85714 s**, it returns **13.763787 MPa**. On this interval the modeled value decreases, and the two-point slope is **-2.0092622 MPa per s**. These are *worked calculations*, not fabricated experimental observations or certified properties of any real polymer grade.

### Evidence, uncertainty, and a competing mechanism

Creep is strongly nonlinear near yield, with moisture plasticization and stress-assisted cracking in some materials. Short-time extrapolation from a single test is not qualified lifetime prediction.

### Exercises and self-assessment

**Exercise 4.5A — Physical mechanism.** What two measurements would distinguish recoverable delayed strain from solvent-driven permanent deformation? State one plausible explanation, one competing explanation and the material-state observation that separates them. Relate the claim to the governing relationship written above rather than merely repeating definitions.

**Exercise 4.5B — Numerical cross-check.** Recalculate **28.11566 MPa** from the companion formula at **35.71429 s** and compare with **13.763787 MPa** at **42.85714 s**. State the sign of the sensitivity and explain whether the changed input would reasonably be controlled independently in a real polymer specimen.

**Exercise 4.5C — Test design.** Propose a synthesis, processing or test matrix that addresses **wall slip or changing crystallinity**. Give the specimen orientation, spatial sampling scheme, temperature-time record, environmental exposure and principal instrument calibration. Explain which observation would falsify your first hypothesis and name a condition under which your model should not be used.

<!-- MODEL_6 -->

## Integrated investigation: A seal that loses force

### The evidence problem

A polymer seal passes initial compression testing but its clamping force decays during hot service. The problem cannot be solved by selecting the equation that gives the most convenient number. First define which property must be achieved, the physical constraint that could prevent it, and the microstructural condition of the specimen being evaluated. List known facts separately from inferred mechanisms, uncertain constants and quantities not yet measured. The central decision is not simply which polymerization route or formulated resin seems attractive: it is what observations would allow a researcher or an engineer to prefer one explanation over competing causes.

### Integrated analysis and model workflow

Map creep, stress relaxation, temperature dependence, moisture uptake and oxidation as separate hypotheses. Build a minimal processing–structure–property map linking the material history with observed state and relevant response. Carry the distinction between **relaxation spectra and non-Newtonian flow** and **instantaneous modulus versus long-time stress response** through the map. For polymer mixing, show composition conservation and do not infer processing kinetics from a static phase diagram. For a melt-state relation, distinguish relaxation time from shear-rate-dependent flow and actual process heating. For chemical function, distinguish molecular diffusion, partitioning, chain mobility and chemical degradation. Use the actual specimen time–temperature history instead of only a machine-temperature set point. For damage, compare local flaw driving force with rate- and environment-dependent measured fracture resistance.

### Validation plan, report, and counterfactual

Measure force relaxation under actual compression, DMA, chemical changes and accelerated holds with mechanism checks. Include an alternative interpretation capable of explaining the same first observation and choose a different instrument or held-out processing condition that separates it. State which measurement would cause you to reject the favored hypothesis. Retain raw counts, image scales, processing logs and sample identifiers. If comparing polymer families, write down the constraints that matter for stiffness, creep, permeability, thermal history and chemical exposure rather than reporting only one maximum strength metric.

**Known limits:** A single Maxwell time constant cannot certify multi-year seal performance. A reader should be able to reconstruct the entire inference from original specimen provenance and measured inputs. The synthetic datasets intentionally contain no physical replicate scatter or hidden model mismatch; those omissions would make a real-world confidence interval far wider than a formula plot suggests.

### Five cumulative exam questions

1. Draw a cause-and-effect diagram linking composition, process history, **relaxation spectra and non-Newtonian flow** and the decision-controlling property; mark one arrow that cannot yet be established from the observations.
2. Write a conservation or constitutive relation for **instantaneous modulus versus long-time stress response** with all units and physical validity assumptions; interpret one limiting case.
3. Propose two mutually exclusive experimental signatures for the favored and competing mechanisms and name the required independent instruments.
4. Show how **wall slip or changing crystallinity** could reverse a seemingly beneficial result, and design the minimum additional test needed to detect that reversal.
5. Write a one-paragraph evidence statement specifying what has been demonstrated, what is merely predicted, and which industrial decision is unjustified until qualification.

<!-- MODEL_7 -->

