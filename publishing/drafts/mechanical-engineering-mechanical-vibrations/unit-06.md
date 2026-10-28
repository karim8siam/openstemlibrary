# Unit 06: Continuous Systems, Rotors and Flexible Structures

**Course Code**: MVB 206 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Continuous Systems, Rotors and Flexible Structures**.

# U06-L01 — Vibrating strings and tension

**OpenSTEM Mechanical Engineering / Book 09 / Mechanical Vibrations**  
*Unit 6: Continuous Systems, Rotors and Flexible Structures | Unreviewed university-level educational manuscript.*

## Learning objectives

After this lesson, you should be able to (1) construct a defensible simplified model of **vibrating strings and tension**, (2) explain the cause-and-effect relationship between its parameters and the observable output, (3) reproduce the quantitative screening example without losing units, (4) identify a realistic failure of the model, and (5) propose a repeatable experiment or sensor strategy. The lesson is intentionally written around a physical decision, not merely a formula to memorize.

## Physical setting and mechanisms

A uniform string with tension T and linear density μ has wave speed c=sqrt(T/μ) and fixed-end frequencies f_n=n c/(2L).

**Running example.** A tensioned cable of length 2 m has T=100 N and μ=0.01 kg/m. Start by naming what is *moving*, what imposes the *excitation*, and what establishes the motion reference. A support can be treated as fixed only if its motion is negligible over the frequency range of interest; if a floor, table, shaft or gearbox housing moves, it becomes part of the system. In particular, a displacement reported in millimeters can be either motion in an inertial frame or the difference between two moving points. The two quantities lead to different interpretations of isolation performance and dynamic stress.

A vibration model begins with inertia and a mechanism that transfers forces or energy. Inertia resists acceleration, elastic stiffness supplies a position-dependent restoring force, and mechanical damping removes energy through irreversible processes. A machine may also have forcing from unbalance, pressure pulses, electromagnetic torque, gear contact, road or floor input, or deliberate actuation. Do not include all these effects by default. Begin by isolating the mechanism suggested by the observed response, then test whether omitted effects matter at the operating point. If a linear model cannot reproduce amplitude, phase and frequency dependence together, the disagreement may identify additional physics, rather than an arithmetic problem.

The central interpretive question is not whether an equation has been solved, but whether its dependent variable corresponds to the requested decision. A natural frequency does not alone tell how large the motion will be; frequency of forcing and damping matter as well. Likewise, a reduction in displacement can coincide with a rise in acceleration if the frequency has changed. When comparing candidates, state whether you are minimizing motion, transmitted force, stress, sound, instrument error, fatigue or some weighted combination of those outcomes. These design objectives can conflict.

## Equation and derivation strategy

**Screening calculation:** Fundamental frequency f_1=sqrt(100/0.01)/(2×2)=25 Hz.

To reproduce this calculation, first sketch a free-body diagram with a positive coordinate direction, then write the force or energy balance. Next substitute numerical inputs with units attached. Convert between frequency in hertz and angular frequency only through ω=2πf; convert rpm to Hz through f=rpm/60 for one event per revolution. Decide whether an amplitude is peak, peak-to-peak or RMS and maintain that convention throughout. Unless the input is a clean harmonic, conversions such as a_peak=ω²X_peak or v_RMS=v_peak/sqrt(2) should not be applied blindly. Where a model assumes a single mode or one-dimensional motion, describe the coordinate that stands in for the true three-dimensional structure.

A useful consistency check is to alter one parameter before making the final decision. Increasing mass at fixed stiffness lowers the natural frequency; increasing stiffness at fixed mass raises it. Damping generally decreases resonant amplification but can increase high-frequency force transmission. Increasing harmonic forcing frequency changes the inertial contribution quadratically. These tendencies apply only within the model that produced them: changes in geometry, preload, temperature, amplitude or joint contact can change mass distribution or stiffness at the same time. A model can be dimensionally correct and still physically wrong because it predicts a quantity no sensor actually measures.

## Worked engineering interpretation

Return to the case: A tensioned cable of length 2 m has T=100 N and μ=0.01 kg/m. The screening result is useful for sizing a measurement range, identifying a suspected mode or testing whether an operating frequency overlaps a predicted response band. It is not a certification result. State the inputs you can actually measure, the ones you have merely assumed, and the likely interval of uncertainty. If two configurations differ by less than measurement variation, choosing the numerically better result is unjustified. For a machine with significant temperature changes, test cold and hot states; for a rotating machine, compare the speed sweep in both directions; for a flexible frame, check whether the fixture and mounting method influence the identified mode.

Introduce a second parameter set, changing one input by 10% while holding the others fixed. Predict the sign of the change before calculating. If the sign differs, identify whether the example crossed a resonance or a stability condition, used the wrong output definition, or violated the small-motion assumption. Record a baseline parameter table with source, unit, uncertainty and date. When the mathematical response is highly sensitive to a small change, refine the test plan before declaring that the first design works.

## Boundaries, failure diagnosis and safety

**Important limitation:** Cable sag, bending rigidity and support compliance violate the ideal taut-string model. An industrial decision should not replace this qualification with a generic “allow a safety factor.” A factor cannot compensate for an incorrect vibration mode, unseen forcing order, missing contact state, defective sensor mounting or a wrong datum. If a simulation forecasts safe operation but measured vibration increases, stop escalating excitation and investigate the disagreement under controlled conditions. The responsibility to establish safe operating procedures, guards, machine access and acceptance limits belongs to qualified engineering personnel.

One way to diagnose discrepancy is to compare three distinct representations: a time trace, a spectrum or frequency-response curve, and a simple physical sketch of the expected motion. The time trace reveals clipping, impulses, drifting offsets and intermittent contact. The spectrum identifies periodic orders and broadband content but loses much time-localized information. The sketch tests whether the sensor direction can observe the hypothesized mode. A well-fitted numerical peak cannot establish a mechanism if the proposed mode shape is incompatible with the structure.

For measurement, **Change tension systematically and verify the approximate square-root scaling.** Measure more than once under a documented load and speed; preserve settings and raw traces. A single amplitude without its frequency band, operating state, transducer orientation and convention is inadequate for comparison. Report model residuals where possible, and identify one datum that could prove the model false. The most useful conclusion may be that a simplified model is insufficient and a more complete test is required.

## Relations to nearby lessons

This lesson builds on **the previous unit foundation** and prepares for **Beam bending vibrations**. These connections matter because the motion predicted in one lesson becomes a forcing input or boundary condition in another. The algebra may look similar while the physical question changes: free response is not forced response, absolute displacement is not relative travel, and a modal natural frequency is not necessarily the frequency of peak operational vibration. Carry definitions of coordinates, units and assumptions forward; do not carry numerical values forward without checking whether the system has changed.

## Guided exercises and assessment

1. **Derivation:** Starting with a labeled free-body diagram or energy balance, derive or explain the screening relationship in this lesson. Show units and confirm at least one limiting case.
2. **Numerical sensitivity:** Recalculate the illustrative case with a 10% change in the parameter most likely to vary in service. Compare the relative change in output with the input change. State whether a linear approximation is justified.
3. **Measurement plan:** For “A tensioned cable of length 2 m has T=100 N and μ=0.01 kg/m.”, choose sensor positions and quantities to measure, and specify a sampling or repeatability requirement. What observation would contradict the simple model?
4. **Model criticism:** Explain exactly why the following warning could overturn a proposed selection: Cable sag, bending rigidity and support compliance violate the ideal taut-string model.
5. **Design trade-off:** Compare two possible interventions, one changing inertia or stiffness and the other changing damping or forcing. Explain which practical requirement each intervention might worsen.
6. **Technical communication:** Write a short decision record separating a model-based prediction, an independent measurement, and a required acceptance condition. Explicitly label any unavailable evidence.

**Self-check:** Explain your result in physical words before looking again at the equation. If its magnitude or trend would surprise an engineer watching the mechanism move, review its coordinate, unit conversions, excitation type and validity limits. Do not use any draft value as an equipment setting without a complete review.


---

# U06-L02 — Beam bending vibrations

**OpenSTEM Mechanical Engineering / Book 09 / Mechanical Vibrations**  
*Unit 6: Continuous Systems, Rotors and Flexible Structures | Unreviewed university-level educational manuscript.*

## Learning objectives

After this lesson, you should be able to (1) construct a defensible simplified model of **beam bending vibrations**, (2) explain the cause-and-effect relationship between its parameters and the observable output, (3) reproduce the quantitative screening example without losing units, (4) identify a realistic failure of the model, and (5) propose a repeatable experiment or sensor strategy. The lesson is intentionally written around a physical decision, not merely a formula to memorize.

## Physical setting and mechanisms

For Euler–Bernoulli cantilever bending, f_1≈1.8751²/(2πL²)sqrt(EI/(ρA)), with a fixed ideal root and uniform section.

**Running example.** A steel sensor bracket is a slender cantilever with an end-mounted device. Start by naming what is *moving*, what imposes the *excitation*, and what establishes the motion reference. A support can be treated as fixed only if its motion is negligible over the frequency range of interest; if a floor, table, shaft or gearbox housing moves, it becomes part of the system. In particular, a displacement reported in millimeters can be either motion in an inertial frame or the difference between two moving points. The two quantities lead to different interpretations of isolation performance and dynamic stress.

A vibration model begins with inertia and a mechanism that transfers forces or energy. Inertia resists acceleration, elastic stiffness supplies a position-dependent restoring force, and mechanical damping removes energy through irreversible processes. A machine may also have forcing from unbalance, pressure pulses, electromagnetic torque, gear contact, road or floor input, or deliberate actuation. Do not include all these effects by default. Begin by isolating the mechanism suggested by the observed response, then test whether omitted effects matter at the operating point. If a linear model cannot reproduce amplitude, phase and frequency dependence together, the disagreement may identify additional physics, rather than an arithmetic problem.

The central interpretive question is not whether an equation has been solved, but whether its dependent variable corresponds to the requested decision. A natural frequency does not alone tell how large the motion will be; frequency of forcing and damping matter as well. Likewise, a reduction in displacement can coincide with a rise in acceleration if the frequency has changed. When comparing candidates, state whether you are minimizing motion, transmitted force, stress, sound, instrument error, fatigue or some weighted combination of those outcomes. These design objectives can conflict.

## Equation and derivation strategy

**Screening calculation:** A doubling of beam length lowers f_1 by a factor of four when all other properties are unchanged.

To reproduce this calculation, first sketch a free-body diagram with a positive coordinate direction, then write the force or energy balance. Next substitute numerical inputs with units attached. Convert between frequency in hertz and angular frequency only through ω=2πf; convert rpm to Hz through f=rpm/60 for one event per revolution. Decide whether an amplitude is peak, peak-to-peak or RMS and maintain that convention throughout. Unless the input is a clean harmonic, conversions such as a_peak=ω²X_peak or v_RMS=v_peak/sqrt(2) should not be applied blindly. Where a model assumes a single mode or one-dimensional motion, describe the coordinate that stands in for the true three-dimensional structure.

A useful consistency check is to alter one parameter before making the final decision. Increasing mass at fixed stiffness lowers the natural frequency; increasing stiffness at fixed mass raises it. Damping generally decreases resonant amplification but can increase high-frequency force transmission. Increasing harmonic forcing frequency changes the inertial contribution quadratically. These tendencies apply only within the model that produced them: changes in geometry, preload, temperature, amplitude or joint contact can change mass distribution or stiffness at the same time. A model can be dimensionally correct and still physically wrong because it predicts a quantity no sensor actually measures.

## Worked engineering interpretation

Return to the case: A steel sensor bracket is a slender cantilever with an end-mounted device. The screening result is useful for sizing a measurement range, identifying a suspected mode or testing whether an operating frequency overlaps a predicted response band. It is not a certification result. State the inputs you can actually measure, the ones you have merely assumed, and the likely interval of uncertainty. If two configurations differ by less than measurement variation, choosing the numerically better result is unjustified. For a machine with significant temperature changes, test cold and hot states; for a rotating machine, compare the speed sweep in both directions; for a flexible frame, check whether the fixture and mounting method influence the identified mode.

Introduce a second parameter set, changing one input by 10% while holding the others fixed. Predict the sign of the change before calculating. If the sign differs, identify whether the example crossed a resonance or a stability condition, used the wrong output definition, or violated the small-motion assumption. Record a baseline parameter table with source, unit, uncertainty and date. When the mathematical response is highly sensitive to a small change, refine the test plan before declaring that the first design works.

## Boundaries, failure diagnosis and safety

**Important limitation:** End mass, shear effects, rotary inertia and nonideal clamping alter mode frequencies. An industrial decision should not replace this qualification with a generic “allow a safety factor.” A factor cannot compensate for an incorrect vibration mode, unseen forcing order, missing contact state, defective sensor mounting or a wrong datum. If a simulation forecasts safe operation but measured vibration increases, stop escalating excitation and investigate the disagreement under controlled conditions. The responsibility to establish safe operating procedures, guards, machine access and acceptance limits belongs to qualified engineering personnel.

One way to diagnose discrepancy is to compare three distinct representations: a time trace, a spectrum or frequency-response curve, and a simple physical sketch of the expected motion. The time trace reveals clipping, impulses, drifting offsets and intermittent contact. The spectrum identifies periodic orders and broadband content but loses much time-localized information. The sketch tests whether the sensor direction can observe the hypothesized mode. A well-fitted numerical peak cannot establish a mechanism if the proposed mode shape is incompatible with the structure.

For measurement, **Run a geometry sensitivity test and compare with a tap-test on the mounted bracket.** Measure more than once under a documented load and speed; preserve settings and raw traces. A single amplitude without its frequency band, operating state, transducer orientation and convention is inadequate for comparison. Report model residuals where possible, and identify one datum that could prove the model false. The most useful conclusion may be that a simplified model is insufficient and a more complete test is required.

## Relations to nearby lessons

This lesson builds on **Vibrating strings and tension** and prepares for **Rotor imbalance excitation**. These connections matter because the motion predicted in one lesson becomes a forcing input or boundary condition in another. The algebra may look similar while the physical question changes: free response is not forced response, absolute displacement is not relative travel, and a modal natural frequency is not necessarily the frequency of peak operational vibration. Carry definitions of coordinates, units and assumptions forward; do not carry numerical values forward without checking whether the system has changed.

## Guided exercises and assessment

1. **Derivation:** Starting with a labeled free-body diagram or energy balance, derive or explain the screening relationship in this lesson. Show units and confirm at least one limiting case.
2. **Numerical sensitivity:** Recalculate the illustrative case with a 10% change in the parameter most likely to vary in service. Compare the relative change in output with the input change. State whether a linear approximation is justified.
3. **Measurement plan:** For “A steel sensor bracket is a slender cantilever with an end-mounted device.”, choose sensor positions and quantities to measure, and specify a sampling or repeatability requirement. What observation would contradict the simple model?
4. **Model criticism:** Explain exactly why the following warning could overturn a proposed selection: End mass, shear effects, rotary inertia and nonideal clamping alter mode frequencies.
5. **Design trade-off:** Compare two possible interventions, one changing inertia or stiffness and the other changing damping or forcing. Explain which practical requirement each intervention might worsen.
6. **Technical communication:** Write a short decision record separating a model-based prediction, an independent measurement, and a required acceptance condition. Explicitly label any unavailable evidence.

**Self-check:** Explain your result in physical words before looking again at the equation. If its magnitude or trend would surprise an engineer watching the mechanism move, review its coordinate, unit conversions, excitation type and validity limits. Do not use any draft value as an equipment setting without a complete review.


---

# U06-L03 — Rotor imbalance excitation

**OpenSTEM Mechanical Engineering / Book 09 / Mechanical Vibrations**  
*Unit 6: Continuous Systems, Rotors and Flexible Structures | Unreviewed university-level educational manuscript.*

## Learning objectives

After this lesson, you should be able to (1) construct a defensible simplified model of **rotor imbalance excitation**, (2) explain the cause-and-effect relationship between its parameters and the observable output, (3) reproduce the quantitative screening example without losing units, (4) identify a realistic failure of the model, and (5) propose a repeatable experiment or sensor strategy. The lesson is intentionally written around a physical decision, not merely a formula to memorize.

## Physical setting and mechanisms

An eccentric mass produces a once-per-revolution harmonic centrifugal-force amplitude F=m_e e ω².

**Running example.** A fan rotor has residual unbalance product 0.0002 kg·m and runs at 3000 rpm. Start by naming what is *moving*, what imposes the *excitation*, and what establishes the motion reference. A support can be treated as fixed only if its motion is negligible over the frequency range of interest; if a floor, table, shaft or gearbox housing moves, it becomes part of the system. In particular, a displacement reported in millimeters can be either motion in an inertial frame or the difference between two moving points. The two quantities lead to different interpretations of isolation performance and dynamic stress.

A vibration model begins with inertia and a mechanism that transfers forces or energy. Inertia resists acceleration, elastic stiffness supplies a position-dependent restoring force, and mechanical damping removes energy through irreversible processes. A machine may also have forcing from unbalance, pressure pulses, electromagnetic torque, gear contact, road or floor input, or deliberate actuation. Do not include all these effects by default. Begin by isolating the mechanism suggested by the observed response, then test whether omitted effects matter at the operating point. If a linear model cannot reproduce amplitude, phase and frequency dependence together, the disagreement may identify additional physics, rather than an arithmetic problem.

The central interpretive question is not whether an equation has been solved, but whether its dependent variable corresponds to the requested decision. A natural frequency does not alone tell how large the motion will be; frequency of forcing and damping matter as well. Likewise, a reduction in displacement can coincide with a rise in acceleration if the frequency has changed. When comparing candidates, state whether you are minimizing motion, transmitted force, stress, sound, instrument error, fatigue or some weighted combination of those outcomes. These design objectives can conflict.

## Equation and derivation strategy

**Screening calculation:** ω=314.16 rad/s; F≈0.0002 ω²=19.74 N.

To reproduce this calculation, first sketch a free-body diagram with a positive coordinate direction, then write the force or energy balance. Next substitute numerical inputs with units attached. Convert between frequency in hertz and angular frequency only through ω=2πf; convert rpm to Hz through f=rpm/60 for one event per revolution. Decide whether an amplitude is peak, peak-to-peak or RMS and maintain that convention throughout. Unless the input is a clean harmonic, conversions such as a_peak=ω²X_peak or v_RMS=v_peak/sqrt(2) should not be applied blindly. Where a model assumes a single mode or one-dimensional motion, describe the coordinate that stands in for the true three-dimensional structure.

A useful consistency check is to alter one parameter before making the final decision. Increasing mass at fixed stiffness lowers the natural frequency; increasing stiffness at fixed mass raises it. Damping generally decreases resonant amplification but can increase high-frequency force transmission. Increasing harmonic forcing frequency changes the inertial contribution quadratically. These tendencies apply only within the model that produced them: changes in geometry, preload, temperature, amplitude or joint contact can change mass distribution or stiffness at the same time. A model can be dimensionally correct and still physically wrong because it predicts a quantity no sensor actually measures.

## Worked engineering interpretation

Return to the case: A fan rotor has residual unbalance product 0.0002 kg·m and runs at 3000 rpm. The screening result is useful for sizing a measurement range, identifying a suspected mode or testing whether an operating frequency overlaps a predicted response band. It is not a certification result. State the inputs you can actually measure, the ones you have merely assumed, and the likely interval of uncertainty. If two configurations differ by less than measurement variation, choosing the numerically better result is unjustified. For a machine with significant temperature changes, test cold and hot states; for a rotating machine, compare the speed sweep in both directions; for a flexible frame, check whether the fixture and mounting method influence the identified mode.

Introduce a second parameter set, changing one input by 10% while holding the others fixed. Predict the sign of the change before calculating. If the sign differs, identify whether the example crossed a resonance or a stability condition, used the wrong output definition, or violated the small-motion assumption. Record a baseline parameter table with source, unit, uncertainty and date. When the mathematical response is highly sensitive to a small change, refine the test plan before declaring that the first design works.

## Boundaries, failure diagnosis and safety

**Important limitation:** Bearing load does not equal the free unbalance force if rotor dynamics and structural resonance modify the transfer path. An industrial decision should not replace this qualification with a generic “allow a safety factor.” A factor cannot compensate for an incorrect vibration mode, unseen forcing order, missing contact state, defective sensor mounting or a wrong datum. If a simulation forecasts safe operation but measured vibration increases, stop escalating excitation and investigate the disagreement under controlled conditions. The responsibility to establish safe operating procedures, guards, machine access and acceptance limits belongs to qualified engineering personnel.

One way to diagnose discrepancy is to compare three distinct representations: a time trace, a spectrum or frequency-response curve, and a simple physical sketch of the expected motion. The time trace reveals clipping, impulses, drifting offsets and intermittent contact. The spectrum identifies periodic orders and broadband content but loses much time-localized information. The sketch tests whether the sensor direction can observe the hypothesized mode. A well-fitted numerical peak cannot establish a mechanism if the proposed mode shape is incompatible with the structure.

For measurement, **Use phase-referenced speed tracking and assess change after controlled balancing.** Measure more than once under a documented load and speed; preserve settings and raw traces. A single amplitude without its frequency band, operating state, transducer orientation and convention is inadequate for comparison. Report model residuals where possible, and identify one datum that could prove the model false. The most useful conclusion may be that a simplified model is insufficient and a more complete test is required.

## Relations to nearby lessons

This lesson builds on **Beam bending vibrations** and prepares for **Critical speeds and gyroscopic effects**. These connections matter because the motion predicted in one lesson becomes a forcing input or boundary condition in another. The algebra may look similar while the physical question changes: free response is not forced response, absolute displacement is not relative travel, and a modal natural frequency is not necessarily the frequency of peak operational vibration. Carry definitions of coordinates, units and assumptions forward; do not carry numerical values forward without checking whether the system has changed.

## Guided exercises and assessment

1. **Derivation:** Starting with a labeled free-body diagram or energy balance, derive or explain the screening relationship in this lesson. Show units and confirm at least one limiting case.
2. **Numerical sensitivity:** Recalculate the illustrative case with a 10% change in the parameter most likely to vary in service. Compare the relative change in output with the input change. State whether a linear approximation is justified.
3. **Measurement plan:** For “A fan rotor has residual unbalance product 0.0002 kg·m and runs at 3000 rpm.”, choose sensor positions and quantities to measure, and specify a sampling or repeatability requirement. What observation would contradict the simple model?
4. **Model criticism:** Explain exactly why the following warning could overturn a proposed selection: Bearing load does not equal the free unbalance force if rotor dynamics and structural resonance modify the transfer path.
5. **Design trade-off:** Compare two possible interventions, one changing inertia or stiffness and the other changing damping or forcing. Explain which practical requirement each intervention might worsen.
6. **Technical communication:** Write a short decision record separating a model-based prediction, an independent measurement, and a required acceptance condition. Explicitly label any unavailable evidence.

**Self-check:** Explain your result in physical words before looking again at the equation. If its magnitude or trend would surprise an engineer watching the mechanism move, review its coordinate, unit conversions, excitation type and validity limits. Do not use any draft value as an equipment setting without a complete review.


---

# U06-L04 — Critical speeds and gyroscopic effects

**OpenSTEM Mechanical Engineering / Book 09 / Mechanical Vibrations**  
*Unit 6: Continuous Systems, Rotors and Flexible Structures | Unreviewed university-level educational manuscript.*

## Learning objectives

After this lesson, you should be able to (1) construct a defensible simplified model of **critical speeds and gyroscopic effects**, (2) explain the cause-and-effect relationship between its parameters and the observable output, (3) reproduce the quantitative screening example without losing units, (4) identify a realistic failure of the model, and (5) propose a repeatable experiment or sensor strategy. The lesson is intentionally written around a physical decision, not merely a formula to memorize.

## Physical setting and mechanisms

Rotating shafts may exhibit bending critical speeds; gyroscopic coupling and anisotropic bearings lead to forward and backward whirl modes.

**Running example.** A flexible rotor has a resonance that shifts when speed is varied. Start by naming what is *moving*, what imposes the *excitation*, and what establishes the motion reference. A support can be treated as fixed only if its motion is negligible over the frequency range of interest; if a floor, table, shaft or gearbox housing moves, it becomes part of the system. In particular, a displacement reported in millimeters can be either motion in an inertial frame or the difference between two moving points. The two quantities lead to different interpretations of isolation performance and dynamic stress.

A vibration model begins with inertia and a mechanism that transfers forces or energy. Inertia resists acceleration, elastic stiffness supplies a position-dependent restoring force, and mechanical damping removes energy through irreversible processes. A machine may also have forcing from unbalance, pressure pulses, electromagnetic torque, gear contact, road or floor input, or deliberate actuation. Do not include all these effects by default. Begin by isolating the mechanism suggested by the observed response, then test whether omitted effects matter at the operating point. If a linear model cannot reproduce amplitude, phase and frequency dependence together, the disagreement may identify additional physics, rather than an arithmetic problem.

The central interpretive question is not whether an equation has been solved, but whether its dependent variable corresponds to the requested decision. A natural frequency does not alone tell how large the motion will be; frequency of forcing and damping matter as well. Likewise, a reduction in displacement can coincide with a rise in acceleration if the frequency has changed. When comparing candidates, state whether you are minimizing motion, transmitted force, stress, sound, instrument error, fatigue or some weighted combination of those outcomes. These design objectives can conflict.

## Equation and derivation strategy

**Screening calculation:** A 60 Hz one-per-revolution order corresponds to 3600 rpm.

To reproduce this calculation, first sketch a free-body diagram with a positive coordinate direction, then write the force or energy balance. Next substitute numerical inputs with units attached. Convert between frequency in hertz and angular frequency only through ω=2πf; convert rpm to Hz through f=rpm/60 for one event per revolution. Decide whether an amplitude is peak, peak-to-peak or RMS and maintain that convention throughout. Unless the input is a clean harmonic, conversions such as a_peak=ω²X_peak or v_RMS=v_peak/sqrt(2) should not be applied blindly. Where a model assumes a single mode or one-dimensional motion, describe the coordinate that stands in for the true three-dimensional structure.

A useful consistency check is to alter one parameter before making the final decision. Increasing mass at fixed stiffness lowers the natural frequency; increasing stiffness at fixed mass raises it. Damping generally decreases resonant amplification but can increase high-frequency force transmission. Increasing harmonic forcing frequency changes the inertial contribution quadratically. These tendencies apply only within the model that produced them: changes in geometry, preload, temperature, amplitude or joint contact can change mass distribution or stiffness at the same time. A model can be dimensionally correct and still physically wrong because it predicts a quantity no sensor actually measures.

## Worked engineering interpretation

Return to the case: A flexible rotor has a resonance that shifts when speed is varied. The screening result is useful for sizing a measurement range, identifying a suspected mode or testing whether an operating frequency overlaps a predicted response band. It is not a certification result. State the inputs you can actually measure, the ones you have merely assumed, and the likely interval of uncertainty. If two configurations differ by less than measurement variation, choosing the numerically better result is unjustified. For a machine with significant temperature changes, test cold and hot states; for a rotating machine, compare the speed sweep in both directions; for a flexible frame, check whether the fixture and mounting method influence the identified mode.

Introduce a second parameter set, changing one input by 10% while holding the others fixed. Predict the sign of the change before calculating. If the sign differs, identify whether the example crossed a resonance or a stability condition, used the wrong output definition, or violated the small-motion assumption. Record a baseline parameter table with source, unit, uncertainty and date. When the mathematical response is highly sensitive to a small change, refine the test plan before declaring that the first design works.

## Boundaries, failure diagnosis and safety

**Important limitation:** The conversion is not a prediction of critical speed; a Campbell diagram needs a validated speed-dependent rotor model. An industrial decision should not replace this qualification with a generic “allow a safety factor.” A factor cannot compensate for an incorrect vibration mode, unseen forcing order, missing contact state, defective sensor mounting or a wrong datum. If a simulation forecasts safe operation but measured vibration increases, stop escalating excitation and investigate the disagreement under controlled conditions. The responsibility to establish safe operating procedures, guards, machine access and acceptance limits belongs to qualified engineering personnel.

One way to diagnose discrepancy is to compare three distinct representations: a time trace, a spectrum or frequency-response curve, and a simple physical sketch of the expected motion. The time trace reveals clipping, impulses, drifting offsets and intermittent contact. The spectrum identifies periodic orders and broadband content but loses much time-localized information. The sketch tests whether the sensor direction can observe the hypothesized mode. A well-fitted numerical peak cannot establish a mechanism if the proposed mode shape is incompatible with the structure.

For measurement, **Measure order-tracked amplitude and phase and compare run-up with coast-down.** Measure more than once under a documented load and speed; preserve settings and raw traces. A single amplitude without its frequency band, operating state, transducer orientation and convention is inadequate for comparison. Report model residuals where possible, and identify one datum that could prove the model false. The most useful conclusion may be that a simplified model is insufficient and a more complete test is required.

## Relations to nearby lessons

This lesson builds on **Rotor imbalance excitation** and prepares for **Nonlinear contact and clearance**. These connections matter because the motion predicted in one lesson becomes a forcing input or boundary condition in another. The algebra may look similar while the physical question changes: free response is not forced response, absolute displacement is not relative travel, and a modal natural frequency is not necessarily the frequency of peak operational vibration. Carry definitions of coordinates, units and assumptions forward; do not carry numerical values forward without checking whether the system has changed.

## Guided exercises and assessment

1. **Derivation:** Starting with a labeled free-body diagram or energy balance, derive or explain the screening relationship in this lesson. Show units and confirm at least one limiting case.
2. **Numerical sensitivity:** Recalculate the illustrative case with a 10% change in the parameter most likely to vary in service. Compare the relative change in output with the input change. State whether a linear approximation is justified.
3. **Measurement plan:** For “A flexible rotor has a resonance that shifts when speed is varied.”, choose sensor positions and quantities to measure, and specify a sampling or repeatability requirement. What observation would contradict the simple model?
4. **Model criticism:** Explain exactly why the following warning could overturn a proposed selection: The conversion is not a prediction of critical speed; a Campbell diagram needs a validated speed-dependent rotor model.
5. **Design trade-off:** Compare two possible interventions, one changing inertia or stiffness and the other changing damping or forcing. Explain which practical requirement each intervention might worsen.
6. **Technical communication:** Write a short decision record separating a model-based prediction, an independent measurement, and a required acceptance condition. Explicitly label any unavailable evidence.

**Self-check:** Explain your result in physical words before looking again at the equation. If its magnitude or trend would surprise an engineer watching the mechanism move, review its coordinate, unit conversions, excitation type and validity limits. Do not use any draft value as an equipment setting without a complete review.


---

# U06-L05 — Nonlinear contact and clearance

**OpenSTEM Mechanical Engineering / Book 09 / Mechanical Vibrations**  
*Unit 6: Continuous Systems, Rotors and Flexible Structures | Unreviewed university-level educational manuscript.*

## Learning objectives

After this lesson, you should be able to (1) construct a defensible simplified model of **nonlinear contact and clearance**, (2) explain the cause-and-effect relationship between its parameters and the observable output, (3) reproduce the quantitative screening example without losing units, (4) identify a realistic failure of the model, and (5) propose a repeatable experiment or sensor strategy. The lesson is intentionally written around a physical decision, not merely a formula to memorize.

## Physical setting and mechanisms

Loose joints, backlash, rub and intermittent contact can produce harmonics and jumps beyond linear modal predictions.

**Running example.** A machine develops a sudden second harmonic and intermittently contacts a housing. Start by naming what is *moving*, what imposes the *excitation*, and what establishes the motion reference. A support can be treated as fixed only if its motion is negligible over the frequency range of interest; if a floor, table, shaft or gearbox housing moves, it becomes part of the system. In particular, a displacement reported in millimeters can be either motion in an inertial frame or the difference between two moving points. The two quantities lead to different interpretations of isolation performance and dynamic stress.

A vibration model begins with inertia and a mechanism that transfers forces or energy. Inertia resists acceleration, elastic stiffness supplies a position-dependent restoring force, and mechanical damping removes energy through irreversible processes. A machine may also have forcing from unbalance, pressure pulses, electromagnetic torque, gear contact, road or floor input, or deliberate actuation. Do not include all these effects by default. Begin by isolating the mechanism suggested by the observed response, then test whether omitted effects matter at the operating point. If a linear model cannot reproduce amplitude, phase and frequency dependence together, the disagreement may identify additional physics, rather than an arithmetic problem.

The central interpretive question is not whether an equation has been solved, but whether its dependent variable corresponds to the requested decision. A natural frequency does not alone tell how large the motion will be; frequency of forcing and damping matter as well. Likewise, a reduction in displacement can coincide with a rise in acceleration if the frequency has changed. When comparing candidates, state whether you are minimizing motion, transmitted force, stress, sound, instrument error, fatigue or some weighted combination of those outcomes. These design objectives can conflict.

## Equation and derivation strategy

**Screening calculation:** A 25 Hz rotational tone has second harmonic at 50 Hz.

To reproduce this calculation, first sketch a free-body diagram with a positive coordinate direction, then write the force or energy balance. Next substitute numerical inputs with units attached. Convert between frequency in hertz and angular frequency only through ω=2πf; convert rpm to Hz through f=rpm/60 for one event per revolution. Decide whether an amplitude is peak, peak-to-peak or RMS and maintain that convention throughout. Unless the input is a clean harmonic, conversions such as a_peak=ω²X_peak or v_RMS=v_peak/sqrt(2) should not be applied blindly. Where a model assumes a single mode or one-dimensional motion, describe the coordinate that stands in for the true three-dimensional structure.

A useful consistency check is to alter one parameter before making the final decision. Increasing mass at fixed stiffness lowers the natural frequency; increasing stiffness at fixed mass raises it. Damping generally decreases resonant amplification but can increase high-frequency force transmission. Increasing harmonic forcing frequency changes the inertial contribution quadratically. These tendencies apply only within the model that produced them: changes in geometry, preload, temperature, amplitude or joint contact can change mass distribution or stiffness at the same time. A model can be dimensionally correct and still physically wrong because it predicts a quantity no sensor actually measures.

## Worked engineering interpretation

Return to the case: A machine develops a sudden second harmonic and intermittently contacts a housing. The screening result is useful for sizing a measurement range, identifying a suspected mode or testing whether an operating frequency overlaps a predicted response band. It is not a certification result. State the inputs you can actually measure, the ones you have merely assumed, and the likely interval of uncertainty. If two configurations differ by less than measurement variation, choosing the numerically better result is unjustified. For a machine with significant temperature changes, test cold and hot states; for a rotating machine, compare the speed sweep in both directions; for a flexible frame, check whether the fixture and mounting method influence the identified mode.

Introduce a second parameter set, changing one input by 10% while holding the others fixed. Predict the sign of the change before calculating. If the sign differs, identify whether the example crossed a resonance or a stability condition, used the wrong output definition, or violated the small-motion assumption. Record a baseline parameter table with source, unit, uncertainty and date. When the mathematical response is highly sensitive to a small change, refine the test plan before declaring that the first design works.

## Boundaries, failure diagnosis and safety

**Important limitation:** A harmonic may also arise from forcing geometry or instrumentation; spectrum alone does not prove rubbing. An industrial decision should not replace this qualification with a generic “allow a safety factor.” A factor cannot compensate for an incorrect vibration mode, unseen forcing order, missing contact state, defective sensor mounting or a wrong datum. If a simulation forecasts safe operation but measured vibration increases, stop escalating excitation and investigate the disagreement under controlled conditions. The responsibility to establish safe operating procedures, guards, machine access and acceptance limits belongs to qualified engineering personnel.

One way to diagnose discrepancy is to compare three distinct representations: a time trace, a spectrum or frequency-response curve, and a simple physical sketch of the expected motion. The time trace reveals clipping, impulses, drifting offsets and intermittent contact. The spectrum identifies periodic orders and broadband content but loses much time-localized information. The sketch tests whether the sensor direction can observe the hypothesized mode. A well-fitted numerical peak cannot establish a mechanism if the proposed mode shape is incompatible with the structure.

For measurement, **Use inspection, speed dependence and correlated time traces before fault attribution.** Measure more than once under a documented load and speed; preserve settings and raw traces. A single amplitude without its frequency band, operating state, transducer orientation and convention is inadequate for comparison. Report model residuals where possible, and identify one datum that could prove the model false. The most useful conclusion may be that a simplified model is insufficient and a more complete test is required.

## Relations to nearby lessons

This lesson builds on **Critical speeds and gyroscopic effects** and prepares for **the unit capstone**. These connections matter because the motion predicted in one lesson becomes a forcing input or boundary condition in another. The algebra may look similar while the physical question changes: free response is not forced response, absolute displacement is not relative travel, and a modal natural frequency is not necessarily the frequency of peak operational vibration. Carry definitions of coordinates, units and assumptions forward; do not carry numerical values forward without checking whether the system has changed.

## Guided exercises and assessment

1. **Derivation:** Starting with a labeled free-body diagram or energy balance, derive or explain the screening relationship in this lesson. Show units and confirm at least one limiting case.
2. **Numerical sensitivity:** Recalculate the illustrative case with a 10% change in the parameter most likely to vary in service. Compare the relative change in output with the input change. State whether a linear approximation is justified.
3. **Measurement plan:** For “A machine develops a sudden second harmonic and intermittently contacts a housing.”, choose sensor positions and quantities to measure, and specify a sampling or repeatability requirement. What observation would contradict the simple model?
4. **Model criticism:** Explain exactly why the following warning could overturn a proposed selection: A harmonic may also arise from forcing geometry or instrumentation; spectrum alone does not prove rubbing.
5. **Design trade-off:** Compare two possible interventions, one changing inertia or stiffness and the other changing damping or forcing. Explain which practical requirement each intervention might worsen.
6. **Technical communication:** Write a short decision record separating a model-based prediction, an independent measurement, and a required acceptance condition. Explicitly label any unavailable evidence.

**Self-check:** Explain your result in physical words before looking again at the equation. If its magnitude or trend would surprise an engineer watching the mechanism move, review its coordinate, unit conversions, excitation type and validity limits. Do not use any draft value as an equipment setting without a complete review.


---

