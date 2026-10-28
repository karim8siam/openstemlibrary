# Unit 01: Oscillatory Motion and Single-Degree-of-Freedom Models

**Course Code**: MVB 201 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Oscillatory Motion and Single-Degree-of-Freedom Models**.

# U01-L01 — Displacement, velocity and acceleration

**OpenSTEM Mechanical Engineering / Book 09 / Mechanical Vibrations**  
*Unit 1: Oscillatory Motion and Single-Degree-of-Freedom Models | Unreviewed university-level educational manuscript.*

## Learning objectives

After this lesson, you should be able to (1) construct a defensible simplified model of **displacement, velocity and acceleration**, (2) explain the cause-and-effect relationship between its parameters and the observable output, (3) reproduce the quantitative screening example without losing units, (4) identify a realistic failure of the model, and (5) propose a repeatable experiment or sensor strategy. The lesson is intentionally written around a physical decision, not merely a formula to memorize.

## Physical setting and mechanisms

Sinusoidal displacement x=X cos(ωt+φ) has velocity -ωX sin(ωt+φ) and acceleration -ω²x. The acceleration amplitude grows with frequency squared, even at fixed movement amplitude.

**Running example.** A sensor head travels 0.002 m at 15 Hz; its acceleration may be significant despite millimetric motion. Start by naming what is *moving*, what imposes the *excitation*, and what establishes the motion reference. A support can be treated as fixed only if its motion is negligible over the frequency range of interest; if a floor, table, shaft or gearbox housing moves, it becomes part of the system. In particular, a displacement reported in millimeters can be either motion in an inertial frame or the difference between two moving points. The two quantities lead to different interpretations of isolation performance and dynamic stress.

A vibration model begins with inertia and a mechanism that transfers forces or energy. Inertia resists acceleration, elastic stiffness supplies a position-dependent restoring force, and mechanical damping removes energy through irreversible processes. A machine may also have forcing from unbalance, pressure pulses, electromagnetic torque, gear contact, road or floor input, or deliberate actuation. Do not include all these effects by default. Begin by isolating the mechanism suggested by the observed response, then test whether omitted effects matter at the operating point. If a linear model cannot reproduce amplitude, phase and frequency dependence together, the disagreement may identify additional physics, rather than an arithmetic problem.

The central interpretive question is not whether an equation has been solved, but whether its dependent variable corresponds to the requested decision. A natural frequency does not alone tell how large the motion will be; frequency of forcing and damping matter as well. Likewise, a reduction in displacement can coincide with a rise in acceleration if the frequency has changed. When comparing candidates, state whether you are minimizing motion, transmitted force, stress, sound, instrument error, fatigue or some weighted combination of those outcomes. These design objectives can conflict.

## Equation and derivation strategy

**Screening calculation:** a_peak=(2πf)^2 X; for X=0.002 m and f=15 Hz, a_peak=17.77 m/s².

To reproduce this calculation, first sketch a free-body diagram with a positive coordinate direction, then write the force or energy balance. Next substitute numerical inputs with units attached. Convert between frequency in hertz and angular frequency only through ω=2πf; convert rpm to Hz through f=rpm/60 for one event per revolution. Decide whether an amplitude is peak, peak-to-peak or RMS and maintain that convention throughout. Unless the input is a clean harmonic, conversions such as a_peak=ω²X_peak or v_RMS=v_peak/sqrt(2) should not be applied blindly. Where a model assumes a single mode or one-dimensional motion, describe the coordinate that stands in for the true three-dimensional structure.

A useful consistency check is to alter one parameter before making the final decision. Increasing mass at fixed stiffness lowers the natural frequency; increasing stiffness at fixed mass raises it. Damping generally decreases resonant amplification but can increase high-frequency force transmission. Increasing harmonic forcing frequency changes the inertial contribution quadratically. These tendencies apply only within the model that produced them: changes in geometry, preload, temperature, amplitude or joint contact can change mass distribution or stiffness at the same time. A model can be dimensionally correct and still physically wrong because it predicts a quantity no sensor actually measures.

## Worked engineering interpretation

Return to the case: A sensor head travels 0.002 m at 15 Hz; its acceleration may be significant despite millimetric motion. The screening result is useful for sizing a measurement range, identifying a suspected mode or testing whether an operating frequency overlaps a predicted response band. It is not a certification result. State the inputs you can actually measure, the ones you have merely assumed, and the likely interval of uncertainty. If two configurations differ by less than measurement variation, choosing the numerically better result is unjustified. For a machine with significant temperature changes, test cold and hot states; for a rotating machine, compare the speed sweep in both directions; for a flexible frame, check whether the fixture and mounting method influence the identified mode.

Introduce a second parameter set, changing one input by 10% while holding the others fixed. Predict the sign of the change before calculating. If the sign differs, identify whether the example crossed a resonance or a stability condition, used the wrong output definition, or violated the small-motion assumption. Record a baseline parameter table with source, unit, uncertainty and date. When the mathematical response is highly sensitive to a small change, refine the test plan before declaring that the first design works.

## Boundaries, failure diagnosis and safety

**Important limitation:** Peak and RMS values are not interchangeable; f denotes cycles per second whereas ω is radians per second. An industrial decision should not replace this qualification with a generic “allow a safety factor.” A factor cannot compensate for an incorrect vibration mode, unseen forcing order, missing contact state, defective sensor mounting or a wrong datum. If a simulation forecasts safe operation but measured vibration increases, stop escalating excitation and investigate the disagreement under controlled conditions. The responsibility to establish safe operating procedures, guards, machine access and acceptance limits belongs to qualified engineering personnel.

One way to diagnose discrepancy is to compare three distinct representations: a time trace, a spectrum or frequency-response curve, and a simple physical sketch of the expected motion. The time trace reveals clipping, impulses, drifting offsets and intermittent contact. The spectrum identifies periodic orders and broadband content but loses much time-localized information. The sketch tests whether the sensor direction can observe the hypothesized mode. A well-fitted numerical peak cannot establish a mechanism if the proposed mode shape is incompatible with the structure.

For measurement, **Compare displacement, accelerometer and encoder traces at the same sampling clock.** Measure more than once under a documented load and speed; preserve settings and raw traces. A single amplitude without its frequency band, operating state, transducer orientation and convention is inadequate for comparison. Report model residuals where possible, and identify one datum that could prove the model false. The most useful conclusion may be that a simplified model is insufficient and a more complete test is required.

## Relations to nearby lessons

This lesson builds on **the previous unit foundation** and prepares for **Mass–spring idealization**. These connections matter because the motion predicted in one lesson becomes a forcing input or boundary condition in another. The algebra may look similar while the physical question changes: free response is not forced response, absolute displacement is not relative travel, and a modal natural frequency is not necessarily the frequency of peak operational vibration. Carry definitions of coordinates, units and assumptions forward; do not carry numerical values forward without checking whether the system has changed.

## Guided exercises and assessment

1. **Derivation:** Starting with a labeled free-body diagram or energy balance, derive or explain the screening relationship in this lesson. Show units and confirm at least one limiting case.
2. **Numerical sensitivity:** Recalculate the illustrative case with a 10% change in the parameter most likely to vary in service. Compare the relative change in output with the input change. State whether a linear approximation is justified.
3. **Measurement plan:** For “A sensor head travels 0.002 m at 15 Hz; its acceleration may be significant despite millimetric motion.”, choose sensor positions and quantities to measure, and specify a sampling or repeatability requirement. What observation would contradict the simple model?
4. **Model criticism:** Explain exactly why the following warning could overturn a proposed selection: Peak and RMS values are not interchangeable; f denotes cycles per second whereas ω is radians per second.
5. **Design trade-off:** Compare two possible interventions, one changing inertia or stiffness and the other changing damping or forcing. Explain which practical requirement each intervention might worsen.
6. **Technical communication:** Write a short decision record separating a model-based prediction, an independent measurement, and a required acceptance condition. Explicitly label any unavailable evidence.

**Self-check:** Explain your result in physical words before looking again at the equation. If its magnitude or trend would surprise an engineer watching the mechanism move, review its coordinate, unit conversions, excitation type and validity limits. Do not use any draft value as an equipment setting without a complete review.


---

# U01-L02 — Mass–spring idealization

**OpenSTEM Mechanical Engineering / Book 09 / Mechanical Vibrations**  
*Unit 1: Oscillatory Motion and Single-Degree-of-Freedom Models | Unreviewed university-level educational manuscript.*

## Learning objectives

After this lesson, you should be able to (1) construct a defensible simplified model of **mass–spring idealization**, (2) explain the cause-and-effect relationship between its parameters and the observable output, (3) reproduce the quantitative screening example without losing units, (4) identify a realistic failure of the model, and (5) propose a repeatable experiment or sensor strategy. The lesson is intentionally written around a physical decision, not merely a formula to memorize.

## Physical setting and mechanisms

In a linear undamped oscillator, m x¨ + k x=0 after displacement is measured from static equilibrium. The solution is sinusoidal when m and k are positive and constant.

**Running example.** An isolated instrument platform has mass 12 kg and effective vertical stiffness 4800 N/m. Start by naming what is *moving*, what imposes the *excitation*, and what establishes the motion reference. A support can be treated as fixed only if its motion is negligible over the frequency range of interest; if a floor, table, shaft or gearbox housing moves, it becomes part of the system. In particular, a displacement reported in millimeters can be either motion in an inertial frame or the difference between two moving points. The two quantities lead to different interpretations of isolation performance and dynamic stress.

A vibration model begins with inertia and a mechanism that transfers forces or energy. Inertia resists acceleration, elastic stiffness supplies a position-dependent restoring force, and mechanical damping removes energy through irreversible processes. A machine may also have forcing from unbalance, pressure pulses, electromagnetic torque, gear contact, road or floor input, or deliberate actuation. Do not include all these effects by default. Begin by isolating the mechanism suggested by the observed response, then test whether omitted effects matter at the operating point. If a linear model cannot reproduce amplitude, phase and frequency dependence together, the disagreement may identify additional physics, rather than an arithmetic problem.

The central interpretive question is not whether an equation has been solved, but whether its dependent variable corresponds to the requested decision. A natural frequency does not alone tell how large the motion will be; frequency of forcing and damping matter as well. Likewise, a reduction in displacement can coincide with a rise in acceleration if the frequency has changed. When comparing candidates, state whether you are minimizing motion, transmitted force, stress, sound, instrument error, fatigue or some weighted combination of those outcomes. These design objectives can conflict.

## Equation and derivation strategy

**Screening calculation:** ω_n=sqrt(k/m)=20 rad/s; f_n=ω_n/(2π)=3.183 Hz.

To reproduce this calculation, first sketch a free-body diagram with a positive coordinate direction, then write the force or energy balance. Next substitute numerical inputs with units attached. Convert between frequency in hertz and angular frequency only through ω=2πf; convert rpm to Hz through f=rpm/60 for one event per revolution. Decide whether an amplitude is peak, peak-to-peak or RMS and maintain that convention throughout. Unless the input is a clean harmonic, conversions such as a_peak=ω²X_peak or v_RMS=v_peak/sqrt(2) should not be applied blindly. Where a model assumes a single mode or one-dimensional motion, describe the coordinate that stands in for the true three-dimensional structure.

A useful consistency check is to alter one parameter before making the final decision. Increasing mass at fixed stiffness lowers the natural frequency; increasing stiffness at fixed mass raises it. Damping generally decreases resonant amplification but can increase high-frequency force transmission. Increasing harmonic forcing frequency changes the inertial contribution quadratically. These tendencies apply only within the model that produced them: changes in geometry, preload, temperature, amplitude or joint contact can change mass distribution or stiffness at the same time. A model can be dimensionally correct and still physically wrong because it predicts a quantity no sensor actually measures.

## Worked engineering interpretation

Return to the case: An isolated instrument platform has mass 12 kg and effective vertical stiffness 4800 N/m. The screening result is useful for sizing a measurement range, identifying a suspected mode or testing whether an operating frequency overlaps a predicted response band. It is not a certification result. State the inputs you can actually measure, the ones you have merely assumed, and the likely interval of uncertainty. If two configurations differ by less than measurement variation, choosing the numerically better result is unjustified. For a machine with significant temperature changes, test cold and hot states; for a rotating machine, compare the speed sweep in both directions; for a flexible frame, check whether the fixture and mounting method influence the identified mode.

Introduce a second parameter set, changing one input by 10% while holding the others fixed. Predict the sign of the change before calculating. If the sign differs, identify whether the example crossed a resonance or a stability condition, used the wrong output definition, or violated the small-motion assumption. Record a baseline parameter table with source, unit, uncertainty and date. When the mathematical response is highly sensitive to a small change, refine the test plan before declaring that the first design works.

## Boundaries, failure diagnosis and safety

**Important limitation:** Effective stiffness depends on direction and constraints; multiple mounts in parallel add stiffness but serial mounts do not. An industrial decision should not replace this qualification with a generic “allow a safety factor.” A factor cannot compensate for an incorrect vibration mode, unseen forcing order, missing contact state, defective sensor mounting or a wrong datum. If a simulation forecasts safe operation but measured vibration increases, stop escalating excitation and investigate the disagreement under controlled conditions. The responsibility to establish safe operating procedures, guards, machine access and acceptance limits belongs to qualified engineering personnel.

One way to diagnose discrepancy is to compare three distinct representations: a time trace, a spectrum or frequency-response curve, and a simple physical sketch of the expected motion. The time trace reveals clipping, impulses, drifting offsets and intermittent contact. The spectrum identifies periodic orders and broadband content but loses much time-localized information. The sketch tests whether the sensor direction can observe the hypothesized mode. A well-fitted numerical peak cannot establish a mechanism if the proposed mode shape is incompatible with the structure.

For measurement, **Weigh payload and estimate mount stiffness by a calibrated quasi-static load–deflection test.** Measure more than once under a documented load and speed; preserve settings and raw traces. A single amplitude without its frequency band, operating state, transducer orientation and convention is inadequate for comparison. Report model residuals where possible, and identify one datum that could prove the model false. The most useful conclusion may be that a simplified model is insufficient and a more complete test is required.

## Relations to nearby lessons

This lesson builds on **Displacement, velocity and acceleration** and prepares for **Equivalent stiffness and compliance**. These connections matter because the motion predicted in one lesson becomes a forcing input or boundary condition in another. The algebra may look similar while the physical question changes: free response is not forced response, absolute displacement is not relative travel, and a modal natural frequency is not necessarily the frequency of peak operational vibration. Carry definitions of coordinates, units and assumptions forward; do not carry numerical values forward without checking whether the system has changed.

## Guided exercises and assessment

1. **Derivation:** Starting with a labeled free-body diagram or energy balance, derive or explain the screening relationship in this lesson. Show units and confirm at least one limiting case.
2. **Numerical sensitivity:** Recalculate the illustrative case with a 10% change in the parameter most likely to vary in service. Compare the relative change in output with the input change. State whether a linear approximation is justified.
3. **Measurement plan:** For “An isolated instrument platform has mass 12 kg and effective vertical stiffness 4800 N/m.”, choose sensor positions and quantities to measure, and specify a sampling or repeatability requirement. What observation would contradict the simple model?
4. **Model criticism:** Explain exactly why the following warning could overturn a proposed selection: Effective stiffness depends on direction and constraints; multiple mounts in parallel add stiffness but serial mounts do not.
5. **Design trade-off:** Compare two possible interventions, one changing inertia or stiffness and the other changing damping or forcing. Explain which practical requirement each intervention might worsen.
6. **Technical communication:** Write a short decision record separating a model-based prediction, an independent measurement, and a required acceptance condition. Explicitly label any unavailable evidence.

**Self-check:** Explain your result in physical words before looking again at the equation. If its magnitude or trend would surprise an engineer watching the mechanism move, review its coordinate, unit conversions, excitation type and validity limits. Do not use any draft value as an equipment setting without a complete review.


---

# U01-L03 — Equivalent stiffness and compliance

**OpenSTEM Mechanical Engineering / Book 09 / Mechanical Vibrations**  
*Unit 1: Oscillatory Motion and Single-Degree-of-Freedom Models | Unreviewed university-level educational manuscript.*

## Learning objectives

After this lesson, you should be able to (1) construct a defensible simplified model of **equivalent stiffness and compliance**, (2) explain the cause-and-effect relationship between its parameters and the observable output, (3) reproduce the quantitative screening example without losing units, (4) identify a realistic failure of the model, and (5) propose a repeatable experiment or sensor strategy. The lesson is intentionally written around a physical decision, not merely a formula to memorize.

## Physical setting and mechanisms

Springs in parallel share deflection and have stiffness k_eq=Σk; springs in series share force and have compliance 1/k_eq=Σ1/k. The path of load decides the correct combination.

**Running example.** A machinery support has two 2500 N/m isolators in parallel, mounted on another compliant layer. Start by naming what is *moving*, what imposes the *excitation*, and what establishes the motion reference. A support can be treated as fixed only if its motion is negligible over the frequency range of interest; if a floor, table, shaft or gearbox housing moves, it becomes part of the system. In particular, a displacement reported in millimeters can be either motion in an inertial frame or the difference between two moving points. The two quantities lead to different interpretations of isolation performance and dynamic stress.

A vibration model begins with inertia and a mechanism that transfers forces or energy. Inertia resists acceleration, elastic stiffness supplies a position-dependent restoring force, and mechanical damping removes energy through irreversible processes. A machine may also have forcing from unbalance, pressure pulses, electromagnetic torque, gear contact, road or floor input, or deliberate actuation. Do not include all these effects by default. Begin by isolating the mechanism suggested by the observed response, then test whether omitted effects matter at the operating point. If a linear model cannot reproduce amplitude, phase and frequency dependence together, the disagreement may identify additional physics, rather than an arithmetic problem.

The central interpretive question is not whether an equation has been solved, but whether its dependent variable corresponds to the requested decision. A natural frequency does not alone tell how large the motion will be; frequency of forcing and damping matter as well. Likewise, a reduction in displacement can coincide with a rise in acceleration if the frequency has changed. When comparing candidates, state whether you are minimizing motion, transmitted force, stress, sound, instrument error, fatigue or some weighted combination of those outcomes. These design objectives can conflict.

## Equation and derivation strategy

**Screening calculation:** Two equal k=2500 N/m elements in parallel yield k_eq=5000 N/m.

To reproduce this calculation, first sketch a free-body diagram with a positive coordinate direction, then write the force or energy balance. Next substitute numerical inputs with units attached. Convert between frequency in hertz and angular frequency only through ω=2πf; convert rpm to Hz through f=rpm/60 for one event per revolution. Decide whether an amplitude is peak, peak-to-peak or RMS and maintain that convention throughout. Unless the input is a clean harmonic, conversions such as a_peak=ω²X_peak or v_RMS=v_peak/sqrt(2) should not be applied blindly. Where a model assumes a single mode or one-dimensional motion, describe the coordinate that stands in for the true three-dimensional structure.

A useful consistency check is to alter one parameter before making the final decision. Increasing mass at fixed stiffness lowers the natural frequency; increasing stiffness at fixed mass raises it. Damping generally decreases resonant amplification but can increase high-frequency force transmission. Increasing harmonic forcing frequency changes the inertial contribution quadratically. These tendencies apply only within the model that produced them: changes in geometry, preload, temperature, amplitude or joint contact can change mass distribution or stiffness at the same time. A model can be dimensionally correct and still physically wrong because it predicts a quantity no sensor actually measures.

## Worked engineering interpretation

Return to the case: A machinery support has two 2500 N/m isolators in parallel, mounted on another compliant layer. The screening result is useful for sizing a measurement range, identifying a suspected mode or testing whether an operating frequency overlaps a predicted response band. It is not a certification result. State the inputs you can actually measure, the ones you have merely assumed, and the likely interval of uncertainty. If two configurations differ by less than measurement variation, choosing the numerically better result is unjustified. For a machine with significant temperature changes, test cold and hot states; for a rotating machine, compare the speed sweep in both directions; for a flexible frame, check whether the fixture and mounting method influence the identified mode.

Introduce a second parameter set, changing one input by 10% while holding the others fixed. Predict the sign of the change before calculating. If the sign differs, identify whether the example crossed a resonance or a stability condition, used the wrong output definition, or violated the small-motion assumption. Record a baseline parameter table with source, unit, uncertainty and date. When the mathematical response is highly sensitive to a small change, refine the test plan before declaring that the first design works.

## Boundaries, failure diagnosis and safety

**Important limitation:** Compliance of frame and fastener assembly can dominate; the catalog stiffness is not an assembled-system stiffness. An industrial decision should not replace this qualification with a generic “allow a safety factor.” A factor cannot compensate for an incorrect vibration mode, unseen forcing order, missing contact state, defective sensor mounting or a wrong datum. If a simulation forecasts safe operation but measured vibration increases, stop escalating excitation and investigate the disagreement under controlled conditions. The responsibility to establish safe operating procedures, guards, machine access and acceptance limits belongs to qualified engineering personnel.

One way to diagnose discrepancy is to compare three distinct representations: a time trace, a spectrum or frequency-response curve, and a simple physical sketch of the expected motion. The time trace reveals clipping, impulses, drifting offsets and intermittent contact. The spectrum identifies periodic orders and broadband content but loses much time-localized information. The sketch tests whether the sensor direction can observe the hypothesized mode. A well-fitted numerical peak cannot establish a mechanism if the proposed mode shape is incompatible with the structure.

For measurement, **Measure full-platform stiffness with the actual supporting structure and fastening torque.** Measure more than once under a documented load and speed; preserve settings and raw traces. A single amplitude without its frequency band, operating state, transducer orientation and convention is inadequate for comparison. Report model residuals where possible, and identify one datum that could prove the model false. The most useful conclusion may be that a simplified model is insufficient and a more complete test is required.

## Relations to nearby lessons

This lesson builds on **Mass–spring idealization** and prepares for **Energy and phase-plane motion**. These connections matter because the motion predicted in one lesson becomes a forcing input or boundary condition in another. The algebra may look similar while the physical question changes: free response is not forced response, absolute displacement is not relative travel, and a modal natural frequency is not necessarily the frequency of peak operational vibration. Carry definitions of coordinates, units and assumptions forward; do not carry numerical values forward without checking whether the system has changed.

## Guided exercises and assessment

1. **Derivation:** Starting with a labeled free-body diagram or energy balance, derive or explain the screening relationship in this lesson. Show units and confirm at least one limiting case.
2. **Numerical sensitivity:** Recalculate the illustrative case with a 10% change in the parameter most likely to vary in service. Compare the relative change in output with the input change. State whether a linear approximation is justified.
3. **Measurement plan:** For “A machinery support has two 2500 N/m isolators in parallel, mounted on another compliant layer.”, choose sensor positions and quantities to measure, and specify a sampling or repeatability requirement. What observation would contradict the simple model?
4. **Model criticism:** Explain exactly why the following warning could overturn a proposed selection: Compliance of frame and fastener assembly can dominate; the catalog stiffness is not an assembled-system stiffness.
5. **Design trade-off:** Compare two possible interventions, one changing inertia or stiffness and the other changing damping or forcing. Explain which practical requirement each intervention might worsen.
6. **Technical communication:** Write a short decision record separating a model-based prediction, an independent measurement, and a required acceptance condition. Explicitly label any unavailable evidence.

**Self-check:** Explain your result in physical words before looking again at the equation. If its magnitude or trend would surprise an engineer watching the mechanism move, review its coordinate, unit conversions, excitation type and validity limits. Do not use any draft value as an equipment setting without a complete review.


---

# U01-L04 — Energy and phase-plane motion

**OpenSTEM Mechanical Engineering / Book 09 / Mechanical Vibrations**  
*Unit 1: Oscillatory Motion and Single-Degree-of-Freedom Models | Unreviewed university-level educational manuscript.*

## Learning objectives

After this lesson, you should be able to (1) construct a defensible simplified model of **energy and phase-plane motion**, (2) explain the cause-and-effect relationship between its parameters and the observable output, (3) reproduce the quantitative screening example without losing units, (4) identify a realistic failure of the model, and (5) propose a repeatable experiment or sensor strategy. The lesson is intentionally written around a physical decision, not merely a formula to memorize.

## Physical setting and mechanisms

Kinetic energy 0.5m v² trades with elastic energy 0.5k x² in undamped free vibration. A phase portrait of x versus v traces an ellipse.

**Running example.** A 4 kg slider oscillates at amplitude 0.012 m with a restoring stiffness of 1600 N/m. Start by naming what is *moving*, what imposes the *excitation*, and what establishes the motion reference. A support can be treated as fixed only if its motion is negligible over the frequency range of interest; if a floor, table, shaft or gearbox housing moves, it becomes part of the system. In particular, a displacement reported in millimeters can be either motion in an inertial frame or the difference between two moving points. The two quantities lead to different interpretations of isolation performance and dynamic stress.

A vibration model begins with inertia and a mechanism that transfers forces or energy. Inertia resists acceleration, elastic stiffness supplies a position-dependent restoring force, and mechanical damping removes energy through irreversible processes. A machine may also have forcing from unbalance, pressure pulses, electromagnetic torque, gear contact, road or floor input, or deliberate actuation. Do not include all these effects by default. Begin by isolating the mechanism suggested by the observed response, then test whether omitted effects matter at the operating point. If a linear model cannot reproduce amplitude, phase and frequency dependence together, the disagreement may identify additional physics, rather than an arithmetic problem.

The central interpretive question is not whether an equation has been solved, but whether its dependent variable corresponds to the requested decision. A natural frequency does not alone tell how large the motion will be; frequency of forcing and damping matter as well. Likewise, a reduction in displacement can coincide with a rise in acceleration if the frequency has changed. When comparing candidates, state whether you are minimizing motion, transmitted force, stress, sound, instrument error, fatigue or some weighted combination of those outcomes. These design objectives can conflict.

## Equation and derivation strategy

**Screening calculation:** E_total=0.5kX²=0.1152 J; velocity amplitude ω_n X=0.24 m/s.

To reproduce this calculation, first sketch a free-body diagram with a positive coordinate direction, then write the force or energy balance. Next substitute numerical inputs with units attached. Convert between frequency in hertz and angular frequency only through ω=2πf; convert rpm to Hz through f=rpm/60 for one event per revolution. Decide whether an amplitude is peak, peak-to-peak or RMS and maintain that convention throughout. Unless the input is a clean harmonic, conversions such as a_peak=ω²X_peak or v_RMS=v_peak/sqrt(2) should not be applied blindly. Where a model assumes a single mode or one-dimensional motion, describe the coordinate that stands in for the true three-dimensional structure.

A useful consistency check is to alter one parameter before making the final decision. Increasing mass at fixed stiffness lowers the natural frequency; increasing stiffness at fixed mass raises it. Damping generally decreases resonant amplification but can increase high-frequency force transmission. Increasing harmonic forcing frequency changes the inertial contribution quadratically. These tendencies apply only within the model that produced them: changes in geometry, preload, temperature, amplitude or joint contact can change mass distribution or stiffness at the same time. A model can be dimensionally correct and still physically wrong because it predicts a quantity no sensor actually measures.

## Worked engineering interpretation

Return to the case: A 4 kg slider oscillates at amplitude 0.012 m with a restoring stiffness of 1600 N/m. The screening result is useful for sizing a measurement range, identifying a suspected mode or testing whether an operating frequency overlaps a predicted response band. It is not a certification result. State the inputs you can actually measure, the ones you have merely assumed, and the likely interval of uncertainty. If two configurations differ by less than measurement variation, choosing the numerically better result is unjustified. For a machine with significant temperature changes, test cold and hot states; for a rotating machine, compare the speed sweep in both directions; for a flexible frame, check whether the fixture and mounting method influence the identified mode.

Introduce a second parameter set, changing one input by 10% while holding the others fixed. Predict the sign of the change before calculating. If the sign differs, identify whether the example crossed a resonance or a stability condition, used the wrong output definition, or violated the small-motion assumption. Record a baseline parameter table with source, unit, uncertainty and date. When the mathematical response is highly sensitive to a small change, refine the test plan before declaring that the first design works.

## Boundaries, failure diagnosis and safety

**Important limitation:** Energy conservation applies only without losses or external excitation; dry friction changes the orbit. An industrial decision should not replace this qualification with a generic “allow a safety factor.” A factor cannot compensate for an incorrect vibration mode, unseen forcing order, missing contact state, defective sensor mounting or a wrong datum. If a simulation forecasts safe operation but measured vibration increases, stop escalating excitation and investigate the disagreement under controlled conditions. The responsibility to establish safe operating procedures, guards, machine access and acceptance limits belongs to qualified engineering personnel.

One way to diagnose discrepancy is to compare three distinct representations: a time trace, a spectrum or frequency-response curve, and a simple physical sketch of the expected motion. The time trace reveals clipping, impulses, drifting offsets and intermittent contact. The spectrum identifies periodic orders and broadband content but loses much time-localized information. The sketch tests whether the sensor direction can observe the hypothesized mode. A well-fitted numerical peak cannot establish a mechanism if the proposed mode shape is incompatible with the structure.

For measurement, **Reconstruct energy from synchronized displacement and velocity measurements.** Measure more than once under a documented load and speed; preserve settings and raw traces. A single amplitude without its frequency band, operating state, transducer orientation and convention is inadequate for comparison. Report model residuals where possible, and identify one datum that could prove the model false. The most useful conclusion may be that a simplified model is insufficient and a more complete test is required.

## Relations to nearby lessons

This lesson builds on **Equivalent stiffness and compliance** and prepares for **Nondimensionalization and modeling boundaries**. These connections matter because the motion predicted in one lesson becomes a forcing input or boundary condition in another. The algebra may look similar while the physical question changes: free response is not forced response, absolute displacement is not relative travel, and a modal natural frequency is not necessarily the frequency of peak operational vibration. Carry definitions of coordinates, units and assumptions forward; do not carry numerical values forward without checking whether the system has changed.

## Guided exercises and assessment

1. **Derivation:** Starting with a labeled free-body diagram or energy balance, derive or explain the screening relationship in this lesson. Show units and confirm at least one limiting case.
2. **Numerical sensitivity:** Recalculate the illustrative case with a 10% change in the parameter most likely to vary in service. Compare the relative change in output with the input change. State whether a linear approximation is justified.
3. **Measurement plan:** For “A 4 kg slider oscillates at amplitude 0.012 m with a restoring stiffness of 1600 N/m.”, choose sensor positions and quantities to measure, and specify a sampling or repeatability requirement. What observation would contradict the simple model?
4. **Model criticism:** Explain exactly why the following warning could overturn a proposed selection: Energy conservation applies only without losses or external excitation; dry friction changes the orbit.
5. **Design trade-off:** Compare two possible interventions, one changing inertia or stiffness and the other changing damping or forcing. Explain which practical requirement each intervention might worsen.
6. **Technical communication:** Write a short decision record separating a model-based prediction, an independent measurement, and a required acceptance condition. Explicitly label any unavailable evidence.

**Self-check:** Explain your result in physical words before looking again at the equation. If its magnitude or trend would surprise an engineer watching the mechanism move, review its coordinate, unit conversions, excitation type and validity limits. Do not use any draft value as an equipment setting without a complete review.


---

# U01-L05 — Nondimensionalization and modeling boundaries

**OpenSTEM Mechanical Engineering / Book 09 / Mechanical Vibrations**  
*Unit 1: Oscillatory Motion and Single-Degree-of-Freedom Models | Unreviewed university-level educational manuscript.*

## Learning objectives

After this lesson, you should be able to (1) construct a defensible simplified model of **nondimensionalization and modeling boundaries**, (2) explain the cause-and-effect relationship between its parameters and the observable output, (3) reproduce the quantitative screening example without losing units, (4) identify a realistic failure of the model, and (5) propose a repeatable experiment or sensor strategy. The lesson is intentionally written around a physical decision, not merely a formula to memorize.

## Physical setting and mechanisms

Scaling time by ω_n and displacement by a reference X separates shape from physical units; x¨+x=0 becomes dimensionless u″+u=0.

**Running example.** Two machines have different masses and springs but similar normalized vibration histories. Start by naming what is *moving*, what imposes the *excitation*, and what establishes the motion reference. A support can be treated as fixed only if its motion is negligible over the frequency range of interest; if a floor, table, shaft or gearbox housing moves, it becomes part of the system. In particular, a displacement reported in millimeters can be either motion in an inertial frame or the difference between two moving points. The two quantities lead to different interpretations of isolation performance and dynamic stress.

A vibration model begins with inertia and a mechanism that transfers forces or energy. Inertia resists acceleration, elastic stiffness supplies a position-dependent restoring force, and mechanical damping removes energy through irreversible processes. A machine may also have forcing from unbalance, pressure pulses, electromagnetic torque, gear contact, road or floor input, or deliberate actuation. Do not include all these effects by default. Begin by isolating the mechanism suggested by the observed response, then test whether omitted effects matter at the operating point. If a linear model cannot reproduce amplitude, phase and frequency dependence together, the disagreement may identify additional physics, rather than an arithmetic problem.

The central interpretive question is not whether an equation has been solved, but whether its dependent variable corresponds to the requested decision. A natural frequency does not alone tell how large the motion will be; frequency of forcing and damping matter as well. Likewise, a reduction in displacement can coincide with a rise in acceleration if the frequency has changed. When comparing candidates, state whether you are minimizing motion, transmitted force, stress, sound, instrument error, fatigue or some weighted combination of those outcomes. These design objectives can conflict.

## Equation and derivation strategy

**Screening calculation:** For m=5 kg and k=2000 N/m, T=2πsqrt(m/k)=0.314 s.

To reproduce this calculation, first sketch a free-body diagram with a positive coordinate direction, then write the force or energy balance. Next substitute numerical inputs with units attached. Convert between frequency in hertz and angular frequency only through ω=2πf; convert rpm to Hz through f=rpm/60 for one event per revolution. Decide whether an amplitude is peak, peak-to-peak or RMS and maintain that convention throughout. Unless the input is a clean harmonic, conversions such as a_peak=ω²X_peak or v_RMS=v_peak/sqrt(2) should not be applied blindly. Where a model assumes a single mode or one-dimensional motion, describe the coordinate that stands in for the true three-dimensional structure.

A useful consistency check is to alter one parameter before making the final decision. Increasing mass at fixed stiffness lowers the natural frequency; increasing stiffness at fixed mass raises it. Damping generally decreases resonant amplification but can increase high-frequency force transmission. Increasing harmonic forcing frequency changes the inertial contribution quadratically. These tendencies apply only within the model that produced them: changes in geometry, preload, temperature, amplitude or joint contact can change mass distribution or stiffness at the same time. A model can be dimensionally correct and still physically wrong because it predicts a quantity no sensor actually measures.

## Worked engineering interpretation

Return to the case: Two machines have different masses and springs but similar normalized vibration histories. The screening result is useful for sizing a measurement range, identifying a suspected mode or testing whether an operating frequency overlaps a predicted response band. It is not a certification result. State the inputs you can actually measure, the ones you have merely assumed, and the likely interval of uncertainty. If two configurations differ by less than measurement variation, choosing the numerically better result is unjustified. For a machine with significant temperature changes, test cold and hot states; for a rotating machine, compare the speed sweep in both directions; for a flexible frame, check whether the fixture and mounting method influence the identified mode.

Introduce a second parameter set, changing one input by 10% while holding the others fixed. Predict the sign of the change before calculating. If the sign differs, identify whether the example crossed a resonance or a stability condition, used the wrong output definition, or violated the small-motion assumption. Record a baseline parameter table with source, unit, uncertainty and date. When the mathematical response is highly sensitive to a small change, refine the test plan before declaring that the first design works.

## Boundaries, failure diagnosis and safety

**Important limitation:** A common dimensionless trace does not imply equal stress, acceleration, fatigue life or allowable clearance. An industrial decision should not replace this qualification with a generic “allow a safety factor.” A factor cannot compensate for an incorrect vibration mode, unseen forcing order, missing contact state, defective sensor mounting or a wrong datum. If a simulation forecasts safe operation but measured vibration increases, stop escalating excitation and investigate the disagreement under controlled conditions. The responsibility to establish safe operating procedures, guards, machine access and acceptance limits belongs to qualified engineering personnel.

One way to diagnose discrepancy is to compare three distinct representations: a time trace, a spectrum or frequency-response curve, and a simple physical sketch of the expected motion. The time trace reveals clipping, impulses, drifting offsets and intermittent contact. The spectrum identifies periodic orders and broadband content but loses much time-localized information. The sketch tests whether the sensor direction can observe the hypothesized mode. A well-fitted numerical peak cannot establish a mechanism if the proposed mode shape is incompatible with the structure.

For measurement, **Report mass, coordinate, frequency, sensor reference and the excluded degrees of freedom.** Measure more than once under a documented load and speed; preserve settings and raw traces. A single amplitude without its frequency band, operating state, transducer orientation and convention is inadequate for comparison. Report model residuals where possible, and identify one datum that could prove the model false. The most useful conclusion may be that a simplified model is insufficient and a more complete test is required.

## Relations to nearby lessons

This lesson builds on **Energy and phase-plane motion** and prepares for **the unit capstone**. These connections matter because the motion predicted in one lesson becomes a forcing input or boundary condition in another. The algebra may look similar while the physical question changes: free response is not forced response, absolute displacement is not relative travel, and a modal natural frequency is not necessarily the frequency of peak operational vibration. Carry definitions of coordinates, units and assumptions forward; do not carry numerical values forward without checking whether the system has changed.

## Guided exercises and assessment

1. **Derivation:** Starting with a labeled free-body diagram or energy balance, derive or explain the screening relationship in this lesson. Show units and confirm at least one limiting case.
2. **Numerical sensitivity:** Recalculate the illustrative case with a 10% change in the parameter most likely to vary in service. Compare the relative change in output with the input change. State whether a linear approximation is justified.
3. **Measurement plan:** For “Two machines have different masses and springs but similar normalized vibration histories.”, choose sensor positions and quantities to measure, and specify a sampling or repeatability requirement. What observation would contradict the simple model?
4. **Model criticism:** Explain exactly why the following warning could overturn a proposed selection: A common dimensionless trace does not imply equal stress, acceleration, fatigue life or allowable clearance.
5. **Design trade-off:** Compare two possible interventions, one changing inertia or stiffness and the other changing damping or forcing. Explain which practical requirement each intervention might worsen.
6. **Technical communication:** Write a short decision record separating a model-based prediction, an independent measurement, and a required acceptance condition. Explicitly label any unavailable evidence.

**Self-check:** Explain your result in physical words before looking again at the equation. If its magnitude or trend would surprise an engineer watching the mechanism move, review its coordinate, unit conversions, excitation type and validity limits. Do not use any draft value as an equipment setting without a complete review.


---

