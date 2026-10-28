# Unit 07: Sensors, Spectral Analysis and Vibration Diagnostics

**Course Code**: MVB 207 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Sensors, Spectral Analysis and Vibration Diagnostics**.

# U07-L01 — Accelerometer and displacement measurements

**OpenSTEM Mechanical Engineering / Book 09 / Mechanical Vibrations**  
*Unit 7: Sensors, Spectral Analysis and Vibration Diagnostics | Unreviewed university-level educational manuscript.*

## Learning objectives

After this lesson, you should be able to (1) construct a defensible simplified model of **accelerometer and displacement measurements**, (2) explain the cause-and-effect relationship between its parameters and the observable output, (3) reproduce the quantitative screening example without losing units, (4) identify a realistic failure of the model, and (5) propose a repeatable experiment or sensor strategy. The lesson is intentionally written around a physical decision, not merely a formula to memorize.

## Physical setting and mechanisms

Accelerometers report acceleration along a sensitive axis; displacement may be estimated by integration but low-frequency errors and drift accumulate.

**Running example.** An accelerometer shows a sinusoidal 2 m/s² amplitude at 10 Hz. Start by naming what is *moving*, what imposes the *excitation*, and what establishes the motion reference. A support can be treated as fixed only if its motion is negligible over the frequency range of interest; if a floor, table, shaft or gearbox housing moves, it becomes part of the system. In particular, a displacement reported in millimeters can be either motion in an inertial frame or the difference between two moving points. The two quantities lead to different interpretations of isolation performance and dynamic stress.

A vibration model begins with inertia and a mechanism that transfers forces or energy. Inertia resists acceleration, elastic stiffness supplies a position-dependent restoring force, and mechanical damping removes energy through irreversible processes. A machine may also have forcing from unbalance, pressure pulses, electromagnetic torque, gear contact, road or floor input, or deliberate actuation. Do not include all these effects by default. Begin by isolating the mechanism suggested by the observed response, then test whether omitted effects matter at the operating point. If a linear model cannot reproduce amplitude, phase and frequency dependence together, the disagreement may identify additional physics, rather than an arithmetic problem.

The central interpretive question is not whether an equation has been solved, but whether its dependent variable corresponds to the requested decision. A natural frequency does not alone tell how large the motion will be; frequency of forcing and damping matter as well. Likewise, a reduction in displacement can coincide with a rise in acceleration if the frequency has changed. When comparing candidates, state whether you are minimizing motion, transmitted force, stress, sound, instrument error, fatigue or some weighted combination of those outcomes. These design objectives can conflict.

## Equation and derivation strategy

**Screening calculation:** Displacement amplitude X=a/ω²≈0.0005066 m at 10 Hz.

To reproduce this calculation, first sketch a free-body diagram with a positive coordinate direction, then write the force or energy balance. Next substitute numerical inputs with units attached. Convert between frequency in hertz and angular frequency only through ω=2πf; convert rpm to Hz through f=rpm/60 for one event per revolution. Decide whether an amplitude is peak, peak-to-peak or RMS and maintain that convention throughout. Unless the input is a clean harmonic, conversions such as a_peak=ω²X_peak or v_RMS=v_peak/sqrt(2) should not be applied blindly. Where a model assumes a single mode or one-dimensional motion, describe the coordinate that stands in for the true three-dimensional structure.

A useful consistency check is to alter one parameter before making the final decision. Increasing mass at fixed stiffness lowers the natural frequency; increasing stiffness at fixed mass raises it. Damping generally decreases resonant amplification but can increase high-frequency force transmission. Increasing harmonic forcing frequency changes the inertial contribution quadratically. These tendencies apply only within the model that produced them: changes in geometry, preload, temperature, amplitude or joint contact can change mass distribution or stiffness at the same time. A model can be dimensionally correct and still physically wrong because it predicts a quantity no sensor actually measures.

## Worked engineering interpretation

Return to the case: An accelerometer shows a sinusoidal 2 m/s² amplitude at 10 Hz. The screening result is useful for sizing a measurement range, identifying a suspected mode or testing whether an operating frequency overlaps a predicted response band. It is not a certification result. State the inputs you can actually measure, the ones you have merely assumed, and the likely interval of uncertainty. If two configurations differ by less than measurement variation, choosing the numerically better result is unjustified. For a machine with significant temperature changes, test cold and hot states; for a rotating machine, compare the speed sweep in both directions; for a flexible frame, check whether the fixture and mounting method influence the identified mode.

Introduce a second parameter set, changing one input by 10% while holding the others fixed. Predict the sign of the change before calculating. If the sign differs, identify whether the example crossed a resonance or a stability condition, used the wrong output definition, or violated the small-motion assumption. Record a baseline parameter table with source, unit, uncertainty and date. When the mathematical response is highly sensitive to a small change, refine the test plan before declaring that the first design works.

## Boundaries, failure diagnosis and safety

**Important limitation:** This conversion assumes a single known sinusoidal component and correct calibration and orientation. An industrial decision should not replace this qualification with a generic “allow a safety factor.” A factor cannot compensate for an incorrect vibration mode, unseen forcing order, missing contact state, defective sensor mounting or a wrong datum. If a simulation forecasts safe operation but measured vibration increases, stop escalating excitation and investigate the disagreement under controlled conditions. The responsibility to establish safe operating procedures, guards, machine access and acceptance limits belongs to qualified engineering personnel.

One way to diagnose discrepancy is to compare three distinct representations: a time trace, a spectrum or frequency-response curve, and a simple physical sketch of the expected motion. The time trace reveals clipping, impulses, drifting offsets and intermittent contact. The spectrum identifies periodic orders and broadband content but loses much time-localized information. The sketch tests whether the sensor direction can observe the hypothesized mode. A well-fitted numerical peak cannot establish a mechanism if the proposed mode shape is incompatible with the structure.

For measurement, **Compare integrated acceleration with a displacement transducer at steady speed.** Measure more than once under a documented load and speed; preserve settings and raw traces. A single amplitude without its frequency band, operating state, transducer orientation and convention is inadequate for comparison. Report model residuals where possible, and identify one datum that could prove the model false. The most useful conclusion may be that a simplified model is insufficient and a more complete test is required.

## Relations to nearby lessons

This lesson builds on **the previous unit foundation** and prepares for **Sampling and aliasing**. These connections matter because the motion predicted in one lesson becomes a forcing input or boundary condition in another. The algebra may look similar while the physical question changes: free response is not forced response, absolute displacement is not relative travel, and a modal natural frequency is not necessarily the frequency of peak operational vibration. Carry definitions of coordinates, units and assumptions forward; do not carry numerical values forward without checking whether the system has changed.

## Guided exercises and assessment

1. **Derivation:** Starting with a labeled free-body diagram or energy balance, derive or explain the screening relationship in this lesson. Show units and confirm at least one limiting case.
2. **Numerical sensitivity:** Recalculate the illustrative case with a 10% change in the parameter most likely to vary in service. Compare the relative change in output with the input change. State whether a linear approximation is justified.
3. **Measurement plan:** For “An accelerometer shows a sinusoidal 2 m/s² amplitude at 10 Hz.”, choose sensor positions and quantities to measure, and specify a sampling or repeatability requirement. What observation would contradict the simple model?
4. **Model criticism:** Explain exactly why the following warning could overturn a proposed selection: This conversion assumes a single known sinusoidal component and correct calibration and orientation.
5. **Design trade-off:** Compare two possible interventions, one changing inertia or stiffness and the other changing damping or forcing. Explain which practical requirement each intervention might worsen.
6. **Technical communication:** Write a short decision record separating a model-based prediction, an independent measurement, and a required acceptance condition. Explicitly label any unavailable evidence.

**Self-check:** Explain your result in physical words before looking again at the equation. If its magnitude or trend would surprise an engineer watching the mechanism move, review its coordinate, unit conversions, excitation type and validity limits. Do not use any draft value as an equipment setting without a complete review.


---

# U07-L02 — Sampling and aliasing

**OpenSTEM Mechanical Engineering / Book 09 / Mechanical Vibrations**  
*Unit 7: Sensors, Spectral Analysis and Vibration Diagnostics | Unreviewed university-level educational manuscript.*

## Learning objectives

After this lesson, you should be able to (1) construct a defensible simplified model of **sampling and aliasing**, (2) explain the cause-and-effect relationship between its parameters and the observable output, (3) reproduce the quantitative screening example without losing units, (4) identify a realistic failure of the model, and (5) propose a repeatable experiment or sensor strategy. The lesson is intentionally written around a physical decision, not merely a formula to memorize.

## Physical setting and mechanisms

Nyquist sampling must exceed twice the highest frequency of interest; anti-alias filtering and transition bands require practical margin.

**Running example.** An accelerometer sampled at 100 Hz measures a true 70 Hz tone. Start by naming what is *moving*, what imposes the *excitation*, and what establishes the motion reference. A support can be treated as fixed only if its motion is negligible over the frequency range of interest; if a floor, table, shaft or gearbox housing moves, it becomes part of the system. In particular, a displacement reported in millimeters can be either motion in an inertial frame or the difference between two moving points. The two quantities lead to different interpretations of isolation performance and dynamic stress.

A vibration model begins with inertia and a mechanism that transfers forces or energy. Inertia resists acceleration, elastic stiffness supplies a position-dependent restoring force, and mechanical damping removes energy through irreversible processes. A machine may also have forcing from unbalance, pressure pulses, electromagnetic torque, gear contact, road or floor input, or deliberate actuation. Do not include all these effects by default. Begin by isolating the mechanism suggested by the observed response, then test whether omitted effects matter at the operating point. If a linear model cannot reproduce amplitude, phase and frequency dependence together, the disagreement may identify additional physics, rather than an arithmetic problem.

The central interpretive question is not whether an equation has been solved, but whether its dependent variable corresponds to the requested decision. A natural frequency does not alone tell how large the motion will be; frequency of forcing and damping matter as well. Likewise, a reduction in displacement can coincide with a rise in acceleration if the frequency has changed. When comparing candidates, state whether you are minimizing motion, transmitted force, stress, sound, instrument error, fatigue or some weighted combination of those outcomes. These design objectives can conflict.

## Equation and derivation strategy

**Screening calculation:** Under ideal sampling, 70 Hz aliases to |70-100|=30 Hz.

To reproduce this calculation, first sketch a free-body diagram with a positive coordinate direction, then write the force or energy balance. Next substitute numerical inputs with units attached. Convert between frequency in hertz and angular frequency only through ω=2πf; convert rpm to Hz through f=rpm/60 for one event per revolution. Decide whether an amplitude is peak, peak-to-peak or RMS and maintain that convention throughout. Unless the input is a clean harmonic, conversions such as a_peak=ω²X_peak or v_RMS=v_peak/sqrt(2) should not be applied blindly. Where a model assumes a single mode or one-dimensional motion, describe the coordinate that stands in for the true three-dimensional structure.

A useful consistency check is to alter one parameter before making the final decision. Increasing mass at fixed stiffness lowers the natural frequency; increasing stiffness at fixed mass raises it. Damping generally decreases resonant amplification but can increase high-frequency force transmission. Increasing harmonic forcing frequency changes the inertial contribution quadratically. These tendencies apply only within the model that produced them: changes in geometry, preload, temperature, amplitude or joint contact can change mass distribution or stiffness at the same time. A model can be dimensionally correct and still physically wrong because it predicts a quantity no sensor actually measures.

## Worked engineering interpretation

Return to the case: An accelerometer sampled at 100 Hz measures a true 70 Hz tone. The screening result is useful for sizing a measurement range, identifying a suspected mode or testing whether an operating frequency overlaps a predicted response band. It is not a certification result. State the inputs you can actually measure, the ones you have merely assumed, and the likely interval of uncertainty. If two configurations differ by less than measurement variation, choosing the numerically better result is unjustified. For a machine with significant temperature changes, test cold and hot states; for a rotating machine, compare the speed sweep in both directions; for a flexible frame, check whether the fixture and mounting method influence the identified mode.

Introduce a second parameter set, changing one input by 10% while holding the others fixed. Predict the sign of the change before calculating. If the sign differs, identify whether the example crossed a resonance or a stability condition, used the wrong output definition, or violated the small-motion assumption. Record a baseline parameter table with source, unit, uncertainty and date. When the mathematical response is highly sensitive to a small change, refine the test plan before declaring that the first design works.

## Boundaries, failure diagnosis and safety

**Important limitation:** The Nyquist criterion alone does not prevent alias contamination without analog anti-alias filtering. An industrial decision should not replace this qualification with a generic “allow a safety factor.” A factor cannot compensate for an incorrect vibration mode, unseen forcing order, missing contact state, defective sensor mounting or a wrong datum. If a simulation forecasts safe operation but measured vibration increases, stop escalating excitation and investigate the disagreement under controlled conditions. The responsibility to establish safe operating procedures, guards, machine access and acceptance limits belongs to qualified engineering personnel.

One way to diagnose discrepancy is to compare three distinct representations: a time trace, a spectrum or frequency-response curve, and a simple physical sketch of the expected motion. The time trace reveals clipping, impulses, drifting offsets and intermittent contact. The spectrum identifies periodic orders and broadband content but loses much time-localized information. The sketch tests whether the sensor direction can observe the hypothesized mode. A well-fitted numerical peak cannot establish a mechanism if the proposed mode shape is incompatible with the structure.

For measurement, **Repeat with higher sample rate and verify the tone frequency remains stable.** Measure more than once under a documented load and speed; preserve settings and raw traces. A single amplitude without its frequency band, operating state, transducer orientation and convention is inadequate for comparison. Report model residuals where possible, and identify one datum that could prove the model false. The most useful conclusion may be that a simplified model is insufficient and a more complete test is required.

## Relations to nearby lessons

This lesson builds on **Accelerometer and displacement measurements** and prepares for **FFT resolution and windowing**. These connections matter because the motion predicted in one lesson becomes a forcing input or boundary condition in another. The algebra may look similar while the physical question changes: free response is not forced response, absolute displacement is not relative travel, and a modal natural frequency is not necessarily the frequency of peak operational vibration. Carry definitions of coordinates, units and assumptions forward; do not carry numerical values forward without checking whether the system has changed.

## Guided exercises and assessment

1. **Derivation:** Starting with a labeled free-body diagram or energy balance, derive or explain the screening relationship in this lesson. Show units and confirm at least one limiting case.
2. **Numerical sensitivity:** Recalculate the illustrative case with a 10% change in the parameter most likely to vary in service. Compare the relative change in output with the input change. State whether a linear approximation is justified.
3. **Measurement plan:** For “An accelerometer sampled at 100 Hz measures a true 70 Hz tone.”, choose sensor positions and quantities to measure, and specify a sampling or repeatability requirement. What observation would contradict the simple model?
4. **Model criticism:** Explain exactly why the following warning could overturn a proposed selection: The Nyquist criterion alone does not prevent alias contamination without analog anti-alias filtering.
5. **Design trade-off:** Compare two possible interventions, one changing inertia or stiffness and the other changing damping or forcing. Explain which practical requirement each intervention might worsen.
6. **Technical communication:** Write a short decision record separating a model-based prediction, an independent measurement, and a required acceptance condition. Explicitly label any unavailable evidence.

**Self-check:** Explain your result in physical words before looking again at the equation. If its magnitude or trend would surprise an engineer watching the mechanism move, review its coordinate, unit conversions, excitation type and validity limits. Do not use any draft value as an equipment setting without a complete review.


---

# U07-L03 — FFT resolution and windowing

**OpenSTEM Mechanical Engineering / Book 09 / Mechanical Vibrations**  
*Unit 7: Sensors, Spectral Analysis and Vibration Diagnostics | Unreviewed university-level educational manuscript.*

## Learning objectives

After this lesson, you should be able to (1) construct a defensible simplified model of **fft resolution and windowing**, (2) explain the cause-and-effect relationship between its parameters and the observable output, (3) reproduce the quantitative screening example without losing units, (4) identify a realistic failure of the model, and (5) propose a repeatable experiment or sensor strategy. The lesson is intentionally written around a physical decision, not merely a formula to memorize.

## Physical setting and mechanisms

For N uniformly sampled points at sampling rate f_s, bin spacing Δf=f_s/N=1/T; windowing controls leakage but changes amplitude calibration.

**Running example.** A 4 s measurement is used to distinguish 24.5 Hz from 25 Hz signals. Start by naming what is *moving*, what imposes the *excitation*, and what establishes the motion reference. A support can be treated as fixed only if its motion is negligible over the frequency range of interest; if a floor, table, shaft or gearbox housing moves, it becomes part of the system. In particular, a displacement reported in millimeters can be either motion in an inertial frame or the difference between two moving points. The two quantities lead to different interpretations of isolation performance and dynamic stress.

A vibration model begins with inertia and a mechanism that transfers forces or energy. Inertia resists acceleration, elastic stiffness supplies a position-dependent restoring force, and mechanical damping removes energy through irreversible processes. A machine may also have forcing from unbalance, pressure pulses, electromagnetic torque, gear contact, road or floor input, or deliberate actuation. Do not include all these effects by default. Begin by isolating the mechanism suggested by the observed response, then test whether omitted effects matter at the operating point. If a linear model cannot reproduce amplitude, phase and frequency dependence together, the disagreement may identify additional physics, rather than an arithmetic problem.

The central interpretive question is not whether an equation has been solved, but whether its dependent variable corresponds to the requested decision. A natural frequency does not alone tell how large the motion will be; frequency of forcing and damping matter as well. Likewise, a reduction in displacement can coincide with a rise in acceleration if the frequency has changed. When comparing candidates, state whether you are minimizing motion, transmitted force, stress, sound, instrument error, fatigue or some weighted combination of those outcomes. These design objectives can conflict.

## Equation and derivation strategy

**Screening calculation:** With T=4 s, Δf=0.25 Hz.

To reproduce this calculation, first sketch a free-body diagram with a positive coordinate direction, then write the force or energy balance. Next substitute numerical inputs with units attached. Convert between frequency in hertz and angular frequency only through ω=2πf; convert rpm to Hz through f=rpm/60 for one event per revolution. Decide whether an amplitude is peak, peak-to-peak or RMS and maintain that convention throughout. Unless the input is a clean harmonic, conversions such as a_peak=ω²X_peak or v_RMS=v_peak/sqrt(2) should not be applied blindly. Where a model assumes a single mode or one-dimensional motion, describe the coordinate that stands in for the true three-dimensional structure.

A useful consistency check is to alter one parameter before making the final decision. Increasing mass at fixed stiffness lowers the natural frequency; increasing stiffness at fixed mass raises it. Damping generally decreases resonant amplification but can increase high-frequency force transmission. Increasing harmonic forcing frequency changes the inertial contribution quadratically. These tendencies apply only within the model that produced them: changes in geometry, preload, temperature, amplitude or joint contact can change mass distribution or stiffness at the same time. A model can be dimensionally correct and still physically wrong because it predicts a quantity no sensor actually measures.

## Worked engineering interpretation

Return to the case: A 4 s measurement is used to distinguish 24.5 Hz from 25 Hz signals. The screening result is useful for sizing a measurement range, identifying a suspected mode or testing whether an operating frequency overlaps a predicted response band. It is not a certification result. State the inputs you can actually measure, the ones you have merely assumed, and the likely interval of uncertainty. If two configurations differ by less than measurement variation, choosing the numerically better result is unjustified. For a machine with significant temperature changes, test cold and hot states; for a rotating machine, compare the speed sweep in both directions; for a flexible frame, check whether the fixture and mounting method influence the identified mode.

Introduce a second parameter set, changing one input by 10% while holding the others fixed. Predict the sign of the change before calculating. If the sign differs, identify whether the example crossed a resonance or a stability condition, used the wrong output definition, or violated the small-motion assumption. Record a baseline parameter table with source, unit, uncertainty and date. When the mathematical response is highly sensitive to a small change, refine the test plan before declaring that the first design works.

## Boundaries, failure diagnosis and safety

**Important limitation:** Closely spaced tones, nonstationary speed and inadequate window choices can still blur a spectrum despite fine bin spacing. An industrial decision should not replace this qualification with a generic “allow a safety factor.” A factor cannot compensate for an incorrect vibration mode, unseen forcing order, missing contact state, defective sensor mounting or a wrong datum. If a simulation forecasts safe operation but measured vibration increases, stop escalating excitation and investigate the disagreement under controlled conditions. The responsibility to establish safe operating procedures, guards, machine access and acceptance limits belongs to qualified engineering personnel.

One way to diagnose discrepancy is to compare three distinct representations: a time trace, a spectrum or frequency-response curve, and a simple physical sketch of the expected motion. The time trace reveals clipping, impulses, drifting offsets and intermittent contact. The spectrum identifies periodic orders and broadband content but loses much time-localized information. The sketch tests whether the sensor direction can observe the hypothesized mode. A well-fitted numerical peak cannot establish a mechanism if the proposed mode shape is incompatible with the structure.

For measurement, **Document window, record length, averaging and amplitude correction.** Measure more than once under a documented load and speed; preserve settings and raw traces. A single amplitude without its frequency band, operating state, transducer orientation and convention is inadequate for comparison. Report model residuals where possible, and identify one datum that could prove the model false. The most useful conclusion may be that a simplified model is insufficient and a more complete test is required.

## Relations to nearby lessons

This lesson builds on **Sampling and aliasing** and prepares for **RMS, crest factor and severity**. These connections matter because the motion predicted in one lesson becomes a forcing input or boundary condition in another. The algebra may look similar while the physical question changes: free response is not forced response, absolute displacement is not relative travel, and a modal natural frequency is not necessarily the frequency of peak operational vibration. Carry definitions of coordinates, units and assumptions forward; do not carry numerical values forward without checking whether the system has changed.

## Guided exercises and assessment

1. **Derivation:** Starting with a labeled free-body diagram or energy balance, derive or explain the screening relationship in this lesson. Show units and confirm at least one limiting case.
2. **Numerical sensitivity:** Recalculate the illustrative case with a 10% change in the parameter most likely to vary in service. Compare the relative change in output with the input change. State whether a linear approximation is justified.
3. **Measurement plan:** For “A 4 s measurement is used to distinguish 24.5 Hz from 25 Hz signals.”, choose sensor positions and quantities to measure, and specify a sampling or repeatability requirement. What observation would contradict the simple model?
4. **Model criticism:** Explain exactly why the following warning could overturn a proposed selection: Closely spaced tones, nonstationary speed and inadequate window choices can still blur a spectrum despite fine bin spacing.
5. **Design trade-off:** Compare two possible interventions, one changing inertia or stiffness and the other changing damping or forcing. Explain which practical requirement each intervention might worsen.
6. **Technical communication:** Write a short decision record separating a model-based prediction, an independent measurement, and a required acceptance condition. Explicitly label any unavailable evidence.

**Self-check:** Explain your result in physical words before looking again at the equation. If its magnitude or trend would surprise an engineer watching the mechanism move, review its coordinate, unit conversions, excitation type and validity limits. Do not use any draft value as an equipment setting without a complete review.


---

# U07-L04 — RMS, crest factor and severity

**OpenSTEM Mechanical Engineering / Book 09 / Mechanical Vibrations**  
*Unit 7: Sensors, Spectral Analysis and Vibration Diagnostics | Unreviewed university-level educational manuscript.*

## Learning objectives

After this lesson, you should be able to (1) construct a defensible simplified model of **rms, crest factor and severity**, (2) explain the cause-and-effect relationship between its parameters and the observable output, (3) reproduce the quantitative screening example without losing units, (4) identify a realistic failure of the model, and (5) propose a repeatable experiment or sensor strategy. The lesson is intentionally written around a physical decision, not merely a formula to memorize.

## Physical setting and mechanisms

RMS characterizes energy-weighted amplitude for stationary vibration; crest factor is peak/RMS and may reveal shocks but is sensitive to clipping and noise.

**Running example.** A sinusoidal velocity has peak 6 mm/s. Start by naming what is *moving*, what imposes the *excitation*, and what establishes the motion reference. A support can be treated as fixed only if its motion is negligible over the frequency range of interest; if a floor, table, shaft or gearbox housing moves, it becomes part of the system. In particular, a displacement reported in millimeters can be either motion in an inertial frame or the difference between two moving points. The two quantities lead to different interpretations of isolation performance and dynamic stress.

A vibration model begins with inertia and a mechanism that transfers forces or energy. Inertia resists acceleration, elastic stiffness supplies a position-dependent restoring force, and mechanical damping removes energy through irreversible processes. A machine may also have forcing from unbalance, pressure pulses, electromagnetic torque, gear contact, road or floor input, or deliberate actuation. Do not include all these effects by default. Begin by isolating the mechanism suggested by the observed response, then test whether omitted effects matter at the operating point. If a linear model cannot reproduce amplitude, phase and frequency dependence together, the disagreement may identify additional physics, rather than an arithmetic problem.

The central interpretive question is not whether an equation has been solved, but whether its dependent variable corresponds to the requested decision. A natural frequency does not alone tell how large the motion will be; frequency of forcing and damping matter as well. Likewise, a reduction in displacement can coincide with a rise in acceleration if the frequency has changed. When comparing candidates, state whether you are minimizing motion, transmitted force, stress, sound, instrument error, fatigue or some weighted combination of those outcomes. These design objectives can conflict.

## Equation and derivation strategy

**Screening calculation:** RMS velocity=6/sqrt(2)=4.243 mm/s for an ideal sinusoid.

To reproduce this calculation, first sketch a free-body diagram with a positive coordinate direction, then write the force or energy balance. Next substitute numerical inputs with units attached. Convert between frequency in hertz and angular frequency only through ω=2πf; convert rpm to Hz through f=rpm/60 for one event per revolution. Decide whether an amplitude is peak, peak-to-peak or RMS and maintain that convention throughout. Unless the input is a clean harmonic, conversions such as a_peak=ω²X_peak or v_RMS=v_peak/sqrt(2) should not be applied blindly. Where a model assumes a single mode or one-dimensional motion, describe the coordinate that stands in for the true three-dimensional structure.

A useful consistency check is to alter one parameter before making the final decision. Increasing mass at fixed stiffness lowers the natural frequency; increasing stiffness at fixed mass raises it. Damping generally decreases resonant amplification but can increase high-frequency force transmission. Increasing harmonic forcing frequency changes the inertial contribution quadratically. These tendencies apply only within the model that produced them: changes in geometry, preload, temperature, amplitude or joint contact can change mass distribution or stiffness at the same time. A model can be dimensionally correct and still physically wrong because it predicts a quantity no sensor actually measures.

## Worked engineering interpretation

Return to the case: A sinusoidal velocity has peak 6 mm/s. The screening result is useful for sizing a measurement range, identifying a suspected mode or testing whether an operating frequency overlaps a predicted response band. It is not a certification result. State the inputs you can actually measure, the ones you have merely assumed, and the likely interval of uncertainty. If two configurations differ by less than measurement variation, choosing the numerically better result is unjustified. For a machine with significant temperature changes, test cold and hot states; for a rotating machine, compare the speed sweep in both directions; for a flexible frame, check whether the fixture and mounting method influence the identified mode.

Introduce a second parameter set, changing one input by 10% while holding the others fixed. Predict the sign of the change before calculating. If the sign differs, identify whether the example crossed a resonance or a stability condition, used the wrong output definition, or violated the small-motion assumption. Record a baseline parameter table with source, unit, uncertainty and date. When the mathematical response is highly sensitive to a small change, refine the test plan before declaring that the first design works.

## Boundaries, failure diagnosis and safety

**Important limitation:** A broadband or impulsive signal does not obey the sinusoidal conversion; severity standards depend on equipment class. An industrial decision should not replace this qualification with a generic “allow a safety factor.” A factor cannot compensate for an incorrect vibration mode, unseen forcing order, missing contact state, defective sensor mounting or a wrong datum. If a simulation forecasts safe operation but measured vibration increases, stop escalating excitation and investigate the disagreement under controlled conditions. The responsibility to establish safe operating procedures, guards, machine access and acceptance limits belongs to qualified engineering personnel.

One way to diagnose discrepancy is to compare three distinct representations: a time trace, a spectrum or frequency-response curve, and a simple physical sketch of the expected motion. The time trace reveals clipping, impulses, drifting offsets and intermittent contact. The spectrum identifies periodic orders and broadband content but loses much time-localized information. The sketch tests whether the sensor direction can observe the hypothesized mode. A well-fitted numerical peak cannot establish a mechanism if the proposed mode shape is incompatible with the structure.

For measurement, **Compare unfiltered waveform, RMS trend and spectrum under matched machine loads.** Measure more than once under a documented load and speed; preserve settings and raw traces. A single amplitude without its frequency band, operating state, transducer orientation and convention is inadequate for comparison. Report model residuals where possible, and identify one datum that could prove the model false. The most useful conclusion may be that a simplified model is insufficient and a more complete test is required.

## Relations to nearby lessons

This lesson builds on **FFT resolution and windowing** and prepares for **Diagnosing faults with context**. These connections matter because the motion predicted in one lesson becomes a forcing input or boundary condition in another. The algebra may look similar while the physical question changes: free response is not forced response, absolute displacement is not relative travel, and a modal natural frequency is not necessarily the frequency of peak operational vibration. Carry definitions of coordinates, units and assumptions forward; do not carry numerical values forward without checking whether the system has changed.

## Guided exercises and assessment

1. **Derivation:** Starting with a labeled free-body diagram or energy balance, derive or explain the screening relationship in this lesson. Show units and confirm at least one limiting case.
2. **Numerical sensitivity:** Recalculate the illustrative case with a 10% change in the parameter most likely to vary in service. Compare the relative change in output with the input change. State whether a linear approximation is justified.
3. **Measurement plan:** For “A sinusoidal velocity has peak 6 mm/s.”, choose sensor positions and quantities to measure, and specify a sampling or repeatability requirement. What observation would contradict the simple model?
4. **Model criticism:** Explain exactly why the following warning could overturn a proposed selection: A broadband or impulsive signal does not obey the sinusoidal conversion; severity standards depend on equipment class.
5. **Design trade-off:** Compare two possible interventions, one changing inertia or stiffness and the other changing damping or forcing. Explain which practical requirement each intervention might worsen.
6. **Technical communication:** Write a short decision record separating a model-based prediction, an independent measurement, and a required acceptance condition. Explicitly label any unavailable evidence.

**Self-check:** Explain your result in physical words before looking again at the equation. If its magnitude or trend would surprise an engineer watching the mechanism move, review its coordinate, unit conversions, excitation type and validity limits. Do not use any draft value as an equipment setting without a complete review.


---

# U07-L05 — Diagnosing faults with context

**OpenSTEM Mechanical Engineering / Book 09 / Mechanical Vibrations**  
*Unit 7: Sensors, Spectral Analysis and Vibration Diagnostics | Unreviewed university-level educational manuscript.*

## Learning objectives

After this lesson, you should be able to (1) construct a defensible simplified model of **diagnosing faults with context**, (2) explain the cause-and-effect relationship between its parameters and the observable output, (3) reproduce the quantitative screening example without losing units, (4) identify a realistic failure of the model, and (5) propose a repeatable experiment or sensor strategy. The lesson is intentionally written around a physical decision, not merely a formula to memorize.

## Physical setting and mechanisms

Unbalance, misalignment, looseness, bearing defects and cavitation have overlapping spectral features. An evidence-based diagnosis combines speed orders, phase, temperature, process state and inspection.

**Running example.** A pump vibrates at one times shaft speed while pressure also fluctuates. Start by naming what is *moving*, what imposes the *excitation*, and what establishes the motion reference. A support can be treated as fixed only if its motion is negligible over the frequency range of interest; if a floor, table, shaft or gearbox housing moves, it becomes part of the system. In particular, a displacement reported in millimeters can be either motion in an inertial frame or the difference between two moving points. The two quantities lead to different interpretations of isolation performance and dynamic stress.

A vibration model begins with inertia and a mechanism that transfers forces or energy. Inertia resists acceleration, elastic stiffness supplies a position-dependent restoring force, and mechanical damping removes energy through irreversible processes. A machine may also have forcing from unbalance, pressure pulses, electromagnetic torque, gear contact, road or floor input, or deliberate actuation. Do not include all these effects by default. Begin by isolating the mechanism suggested by the observed response, then test whether omitted effects matter at the operating point. If a linear model cannot reproduce amplitude, phase and frequency dependence together, the disagreement may identify additional physics, rather than an arithmetic problem.

The central interpretive question is not whether an equation has been solved, but whether its dependent variable corresponds to the requested decision. A natural frequency does not alone tell how large the motion will be; frequency of forcing and damping matter as well. Likewise, a reduction in displacement can coincide with a rise in acceleration if the frequency has changed. When comparing candidates, state whether you are minimizing motion, transmitted force, stress, sound, instrument error, fatigue or some weighted combination of those outcomes. These design objectives can conflict.

## Equation and derivation strategy

**Screening calculation:** At 1800 rpm the 1× rotational frequency is 30 Hz.

To reproduce this calculation, first sketch a free-body diagram with a positive coordinate direction, then write the force or energy balance. Next substitute numerical inputs with units attached. Convert between frequency in hertz and angular frequency only through ω=2πf; convert rpm to Hz through f=rpm/60 for one event per revolution. Decide whether an amplitude is peak, peak-to-peak or RMS and maintain that convention throughout. Unless the input is a clean harmonic, conversions such as a_peak=ω²X_peak or v_RMS=v_peak/sqrt(2) should not be applied blindly. Where a model assumes a single mode or one-dimensional motion, describe the coordinate that stands in for the true three-dimensional structure.

A useful consistency check is to alter one parameter before making the final decision. Increasing mass at fixed stiffness lowers the natural frequency; increasing stiffness at fixed mass raises it. Damping generally decreases resonant amplification but can increase high-frequency force transmission. Increasing harmonic forcing frequency changes the inertial contribution quadratically. These tendencies apply only within the model that produced them: changes in geometry, preload, temperature, amplitude or joint contact can change mass distribution or stiffness at the same time. A model can be dimensionally correct and still physically wrong because it predicts a quantity no sensor actually measures.

## Worked engineering interpretation

Return to the case: A pump vibrates at one times shaft speed while pressure also fluctuates. The screening result is useful for sizing a measurement range, identifying a suspected mode or testing whether an operating frequency overlaps a predicted response band. It is not a certification result. State the inputs you can actually measure, the ones you have merely assumed, and the likely interval of uncertainty. If two configurations differ by less than measurement variation, choosing the numerically better result is unjustified. For a machine with significant temperature changes, test cold and hot states; for a rotating machine, compare the speed sweep in both directions; for a flexible frame, check whether the fixture and mounting method influence the identified mode.

Introduce a second parameter set, changing one input by 10% while holding the others fixed. Predict the sign of the change before calculating. If the sign differs, identify whether the example crossed a resonance or a stability condition, used the wrong output definition, or violated the small-motion assumption. Record a baseline parameter table with source, unit, uncertainty and date. When the mathematical response is highly sensitive to a small change, refine the test plan before declaring that the first design works.

## Boundaries, failure diagnosis and safety

**Important limitation:** A 1× line is not proof of unbalance; structural resonance and hydraulic excitation can produce the same component. An industrial decision should not replace this qualification with a generic “allow a safety factor.” A factor cannot compensate for an incorrect vibration mode, unseen forcing order, missing contact state, defective sensor mounting or a wrong datum. If a simulation forecasts safe operation but measured vibration increases, stop escalating excitation and investigate the disagreement under controlled conditions. The responsibility to establish safe operating procedures, guards, machine access and acceptance limits belongs to qualified engineering personnel.

One way to diagnose discrepancy is to compare three distinct representations: a time trace, a spectrum or frequency-response curve, and a simple physical sketch of the expected motion. The time trace reveals clipping, impulses, drifting offsets and intermittent contact. The spectrum identifies periodic orders and broadband content but loses much time-localized information. The sketch tests whether the sensor direction can observe the hypothesized mode. A well-fitted numerical peak cannot establish a mechanism if the proposed mode shape is incompatible with the structure.

For measurement, **Build a before/after diagnostic record with machine condition and operating-point metadata.** Measure more than once under a documented load and speed; preserve settings and raw traces. A single amplitude without its frequency band, operating state, transducer orientation and convention is inadequate for comparison. Report model residuals where possible, and identify one datum that could prove the model false. The most useful conclusion may be that a simplified model is insufficient and a more complete test is required.

## Relations to nearby lessons

This lesson builds on **RMS, crest factor and severity** and prepares for **the unit capstone**. These connections matter because the motion predicted in one lesson becomes a forcing input or boundary condition in another. The algebra may look similar while the physical question changes: free response is not forced response, absolute displacement is not relative travel, and a modal natural frequency is not necessarily the frequency of peak operational vibration. Carry definitions of coordinates, units and assumptions forward; do not carry numerical values forward without checking whether the system has changed.

## Guided exercises and assessment

1. **Derivation:** Starting with a labeled free-body diagram or energy balance, derive or explain the screening relationship in this lesson. Show units and confirm at least one limiting case.
2. **Numerical sensitivity:** Recalculate the illustrative case with a 10% change in the parameter most likely to vary in service. Compare the relative change in output with the input change. State whether a linear approximation is justified.
3. **Measurement plan:** For “A pump vibrates at one times shaft speed while pressure also fluctuates.”, choose sensor positions and quantities to measure, and specify a sampling or repeatability requirement. What observation would contradict the simple model?
4. **Model criticism:** Explain exactly why the following warning could overturn a proposed selection: A 1× line is not proof of unbalance; structural resonance and hydraulic excitation can produce the same component.
5. **Design trade-off:** Compare two possible interventions, one changing inertia or stiffness and the other changing damping or forcing. Explain which practical requirement each intervention might worsen.
6. **Technical communication:** Write a short decision record separating a model-based prediction, an independent measurement, and a required acceptance condition. Explicitly label any unavailable evidence.

**Self-check:** Explain your result in physical words before looking again at the equation. If its magnitude or trend would surprise an engineer watching the mechanism move, review its coordinate, unit conversions, excitation type and validity limits. Do not use any draft value as an equipment setting without a complete review.


---

