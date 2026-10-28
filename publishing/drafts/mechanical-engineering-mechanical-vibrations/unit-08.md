# Unit 08: Engineering Design, Testing and Vibration Control

**Course Code**: MVB 208 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Engineering Design, Testing and Vibration Control**.

# U08-L01 — Design against resonance

**OpenSTEM Mechanical Engineering / Book 09 / Mechanical Vibrations**  
*Unit 8: Engineering Design, Testing and Vibration Control | Unreviewed university-level educational manuscript.*

## Learning objectives

After this lesson, you should be able to (1) construct a defensible simplified model of **design against resonance**, (2) explain the cause-and-effect relationship between its parameters and the observable output, (3) reproduce the quantitative screening example without losing units, (4) identify a realistic failure of the model, and (5) propose a repeatable experiment or sensor strategy. The lesson is intentionally written around a physical decision, not merely a formula to memorize.

## Physical setting and mechanisms

Separate critical structural natural frequencies from known excitation orders across the operating envelope; include uncertainty and transient run-up.

**Running example.** A 30–50 Hz variable-speed motor excites a supported enclosure mode near 42 Hz. Start by naming what is *moving*, what imposes the *excitation*, and what establishes the motion reference. A support can be treated as fixed only if its motion is negligible over the frequency range of interest; if a floor, table, shaft or gearbox housing moves, it becomes part of the system. In particular, a displacement reported in millimeters can be either motion in an inertial frame or the difference between two moving points. The two quantities lead to different interpretations of isolation performance and dynamic stress.

A vibration model begins with inertia and a mechanism that transfers forces or energy. Inertia resists acceleration, elastic stiffness supplies a position-dependent restoring force, and mechanical damping removes energy through irreversible processes. A machine may also have forcing from unbalance, pressure pulses, electromagnetic torque, gear contact, road or floor input, or deliberate actuation. Do not include all these effects by default. Begin by isolating the mechanism suggested by the observed response, then test whether omitted effects matter at the operating point. If a linear model cannot reproduce amplitude, phase and frequency dependence together, the disagreement may identify additional physics, rather than an arithmetic problem.

The central interpretive question is not whether an equation has been solved, but whether its dependent variable corresponds to the requested decision. A natural frequency does not alone tell how large the motion will be; frequency of forcing and damping matter as well. Likewise, a reduction in displacement can coincide with a rise in acceleration if the frequency has changed. When comparing candidates, state whether you are minimizing motion, transmitted force, stress, sound, instrument error, fatigue or some weighted combination of those outcomes. These design objectives can conflict.

## Equation and derivation strategy

**Screening calculation:** Mode/excitation separation at 42 Hz and 50 Hz is (50-42)/50=16% relative to 50 Hz.

To reproduce this calculation, first sketch a free-body diagram with a positive coordinate direction, then write the force or energy balance. Next substitute numerical inputs with units attached. Convert between frequency in hertz and angular frequency only through ω=2πf; convert rpm to Hz through f=rpm/60 for one event per revolution. Decide whether an amplitude is peak, peak-to-peak or RMS and maintain that convention throughout. Unless the input is a clean harmonic, conversions such as a_peak=ω²X_peak or v_RMS=v_peak/sqrt(2) should not be applied blindly. Where a model assumes a single mode or one-dimensional motion, describe the coordinate that stands in for the true three-dimensional structure.

A useful consistency check is to alter one parameter before making the final decision. Increasing mass at fixed stiffness lowers the natural frequency; increasing stiffness at fixed mass raises it. Damping generally decreases resonant amplification but can increase high-frequency force transmission. Increasing harmonic forcing frequency changes the inertial contribution quadratically. These tendencies apply only within the model that produced them: changes in geometry, preload, temperature, amplitude or joint contact can change mass distribution or stiffness at the same time. A model can be dimensionally correct and still physically wrong because it predicts a quantity no sensor actually measures.

## Worked engineering interpretation

Return to the case: A 30–50 Hz variable-speed motor excites a supported enclosure mode near 42 Hz. The screening result is useful for sizing a measurement range, identifying a suspected mode or testing whether an operating frequency overlaps a predicted response band. It is not a certification result. State the inputs you can actually measure, the ones you have merely assumed, and the likely interval of uncertainty. If two configurations differ by less than measurement variation, choosing the numerically better result is unjustified. For a machine with significant temperature changes, test cold and hot states; for a rotating machine, compare the speed sweep in both directions; for a flexible frame, check whether the fixture and mounting method influence the identified mode.

Introduce a second parameter set, changing one input by 10% while holding the others fixed. Predict the sign of the change before calculating. If the sign differs, identify whether the example crossed a resonance or a stability condition, used the wrong output definition, or violated the small-motion assumption. Record a baseline parameter table with source, unit, uncertainty and date. When the mathematical response is highly sensitive to a small change, refine the test plan before declaring that the first design works.

## Boundaries, failure diagnosis and safety

**Important limitation:** A simple percent separation is not a safety rule; response depends on damping, forcing, mode shape and uncertainty. An industrial decision should not replace this qualification with a generic “allow a safety factor.” A factor cannot compensate for an incorrect vibration mode, unseen forcing order, missing contact state, defective sensor mounting or a wrong datum. If a simulation forecasts safe operation but measured vibration increases, stop escalating excitation and investigate the disagreement under controlled conditions. The responsibility to establish safe operating procedures, guards, machine access and acceptance limits belongs to qualified engineering personnel.

One way to diagnose discrepancy is to compare three distinct representations: a time trace, a spectrum or frequency-response curve, and a simple physical sketch of the expected motion. The time trace reveals clipping, impulses, drifting offsets and intermittent contact. The spectrum identifies periodic orders and broadband content but loses much time-localized information. The sketch tests whether the sensor direction can observe the hypothesized mode. A well-fitted numerical peak cannot establish a mechanism if the proposed mode shape is incompatible with the structure.

For measurement, **Sweep speed under controlled loading and measure the largest response on the actual assembled machine.** Measure more than once under a documented load and speed; preserve settings and raw traces. A single amplitude without its frequency band, operating state, transducer orientation and convention is inadequate for comparison. Report model residuals where possible, and identify one datum that could prove the model false. The most useful conclusion may be that a simplified model is insufficient and a more complete test is required.

## Relations to nearby lessons

This lesson builds on **the previous unit foundation** and prepares for **Tuned mass dampers**. These connections matter because the motion predicted in one lesson becomes a forcing input or boundary condition in another. The algebra may look similar while the physical question changes: free response is not forced response, absolute displacement is not relative travel, and a modal natural frequency is not necessarily the frequency of peak operational vibration. Carry definitions of coordinates, units and assumptions forward; do not carry numerical values forward without checking whether the system has changed.

## Guided exercises and assessment

1. **Derivation:** Starting with a labeled free-body diagram or energy balance, derive or explain the screening relationship in this lesson. Show units and confirm at least one limiting case.
2. **Numerical sensitivity:** Recalculate the illustrative case with a 10% change in the parameter most likely to vary in service. Compare the relative change in output with the input change. State whether a linear approximation is justified.
3. **Measurement plan:** For “A 30–50 Hz variable-speed motor excites a supported enclosure mode near 42 Hz.”, choose sensor positions and quantities to measure, and specify a sampling or repeatability requirement. What observation would contradict the simple model?
4. **Model criticism:** Explain exactly why the following warning could overturn a proposed selection: A simple percent separation is not a safety rule; response depends on damping, forcing, mode shape and uncertainty.
5. **Design trade-off:** Compare two possible interventions, one changing inertia or stiffness and the other changing damping or forcing. Explain which practical requirement each intervention might worsen.
6. **Technical communication:** Write a short decision record separating a model-based prediction, an independent measurement, and a required acceptance condition. Explicitly label any unavailable evidence.

**Self-check:** Explain your result in physical words before looking again at the equation. If its magnitude or trend would surprise an engineer watching the mechanism move, review its coordinate, unit conversions, excitation type and validity limits. Do not use any draft value as an equipment setting without a complete review.


---

# U08-L02 — Tuned mass dampers

**OpenSTEM Mechanical Engineering / Book 09 / Mechanical Vibrations**  
*Unit 8: Engineering Design, Testing and Vibration Control | Unreviewed university-level educational manuscript.*

## Learning objectives

After this lesson, you should be able to (1) construct a defensible simplified model of **tuned mass dampers**, (2) explain the cause-and-effect relationship between its parameters and the observable output, (3) reproduce the quantitative screening example without losing units, (4) identify a realistic failure of the model, and (5) propose a repeatable experiment or sensor strategy. The lesson is intentionally written around a physical decision, not merely a formula to memorize.

## Physical setting and mechanisms

An auxiliary mass–spring–damper can redistribute resonant response over a targeted frequency band, but tuning and added mass are constraints.

**Running example.** A slender platform resonates near 18 Hz; a small auxiliary mass is permitted. Start by naming what is *moving*, what imposes the *excitation*, and what establishes the motion reference. A support can be treated as fixed only if its motion is negligible over the frequency range of interest; if a floor, table, shaft or gearbox housing moves, it becomes part of the system. In particular, a displacement reported in millimeters can be either motion in an inertial frame or the difference between two moving points. The two quantities lead to different interpretations of isolation performance and dynamic stress.

A vibration model begins with inertia and a mechanism that transfers forces or energy. Inertia resists acceleration, elastic stiffness supplies a position-dependent restoring force, and mechanical damping removes energy through irreversible processes. A machine may also have forcing from unbalance, pressure pulses, electromagnetic torque, gear contact, road or floor input, or deliberate actuation. Do not include all these effects by default. Begin by isolating the mechanism suggested by the observed response, then test whether omitted effects matter at the operating point. If a linear model cannot reproduce amplitude, phase and frequency dependence together, the disagreement may identify additional physics, rather than an arithmetic problem.

The central interpretive question is not whether an equation has been solved, but whether its dependent variable corresponds to the requested decision. A natural frequency does not alone tell how large the motion will be; frequency of forcing and damping matter as well. Likewise, a reduction in displacement can coincide with a rise in acceleration if the frequency has changed. When comparing candidates, state whether you are minimizing motion, transmitted force, stress, sound, instrument error, fatigue or some weighted combination of those outcomes. These design objectives can conflict.

## Equation and derivation strategy

**Screening calculation:** For auxiliary mass 2 kg tuned to 18 Hz, k_t=m_t(2πf)^2≈25,582 N/m.

To reproduce this calculation, first sketch a free-body diagram with a positive coordinate direction, then write the force or energy balance. Next substitute numerical inputs with units attached. Convert between frequency in hertz and angular frequency only through ω=2πf; convert rpm to Hz through f=rpm/60 for one event per revolution. Decide whether an amplitude is peak, peak-to-peak or RMS and maintain that convention throughout. Unless the input is a clean harmonic, conversions such as a_peak=ω²X_peak or v_RMS=v_peak/sqrt(2) should not be applied blindly. Where a model assumes a single mode or one-dimensional motion, describe the coordinate that stands in for the true three-dimensional structure.

A useful consistency check is to alter one parameter before making the final decision. Increasing mass at fixed stiffness lowers the natural frequency; increasing stiffness at fixed mass raises it. Damping generally decreases resonant amplification but can increase high-frequency force transmission. Increasing harmonic forcing frequency changes the inertial contribution quadratically. These tendencies apply only within the model that produced them: changes in geometry, preload, temperature, amplitude or joint contact can change mass distribution or stiffness at the same time. A model can be dimensionally correct and still physically wrong because it predicts a quantity no sensor actually measures.

## Worked engineering interpretation

Return to the case: A slender platform resonates near 18 Hz; a small auxiliary mass is permitted. The screening result is useful for sizing a measurement range, identifying a suspected mode or testing whether an operating frequency overlaps a predicted response band. It is not a certification result. State the inputs you can actually measure, the ones you have merely assumed, and the likely interval of uncertainty. If two configurations differ by less than measurement variation, choosing the numerically better result is unjustified. For a machine with significant temperature changes, test cold and hot states; for a rotating machine, compare the speed sweep in both directions; for a flexible frame, check whether the fixture and mounting method influence the identified mode.

Introduce a second parameter set, changing one input by 10% while holding the others fixed. Predict the sign of the change before calculating. If the sign differs, identify whether the example crossed a resonance or a stability condition, used the wrong output definition, or violated the small-motion assumption. Record a baseline parameter table with source, unit, uncertainty and date. When the mathematical response is highly sensitive to a small change, refine the test plan before declaring that the first design works.

## Boundaries, failure diagnosis and safety

**Important limitation:** The ideal tuned frequency does not determine optimum damping, robust bandwidth or actual support stiffness. An industrial decision should not replace this qualification with a generic “allow a safety factor.” A factor cannot compensate for an incorrect vibration mode, unseen forcing order, missing contact state, defective sensor mounting or a wrong datum. If a simulation forecasts safe operation but measured vibration increases, stop escalating excitation and investigate the disagreement under controlled conditions. The responsibility to establish safe operating procedures, guards, machine access and acceptance limits belongs to qualified engineering personnel.

One way to diagnose discrepancy is to compare three distinct representations: a time trace, a spectrum or frequency-response curve, and a simple physical sketch of the expected motion. The time trace reveals clipping, impulses, drifting offsets and intermittent contact. The spectrum identifies periodic orders and broadband content but loses much time-localized information. The sketch tests whether the sensor direction can observe the hypothesized mode. A well-fitted numerical peak cannot establish a mechanism if the proposed mode shape is incompatible with the structure.

For measurement, **Measure primary response before and after installation across frequencies, not just at one operating speed.** Measure more than once under a documented load and speed; preserve settings and raw traces. A single amplitude without its frequency band, operating state, transducer orientation and convention is inadequate for comparison. Report model residuals where possible, and identify one datum that could prove the model false. The most useful conclusion may be that a simplified model is insufficient and a more complete test is required.

## Relations to nearby lessons

This lesson builds on **Design against resonance** and prepares for **Fatigue and vibratory stress**. These connections matter because the motion predicted in one lesson becomes a forcing input or boundary condition in another. The algebra may look similar while the physical question changes: free response is not forced response, absolute displacement is not relative travel, and a modal natural frequency is not necessarily the frequency of peak operational vibration. Carry definitions of coordinates, units and assumptions forward; do not carry numerical values forward without checking whether the system has changed.

## Guided exercises and assessment

1. **Derivation:** Starting with a labeled free-body diagram or energy balance, derive or explain the screening relationship in this lesson. Show units and confirm at least one limiting case.
2. **Numerical sensitivity:** Recalculate the illustrative case with a 10% change in the parameter most likely to vary in service. Compare the relative change in output with the input change. State whether a linear approximation is justified.
3. **Measurement plan:** For “A slender platform resonates near 18 Hz; a small auxiliary mass is permitted.”, choose sensor positions and quantities to measure, and specify a sampling or repeatability requirement. What observation would contradict the simple model?
4. **Model criticism:** Explain exactly why the following warning could overturn a proposed selection: The ideal tuned frequency does not determine optimum damping, robust bandwidth or actual support stiffness.
5. **Design trade-off:** Compare two possible interventions, one changing inertia or stiffness and the other changing damping or forcing. Explain which practical requirement each intervention might worsen.
6. **Technical communication:** Write a short decision record separating a model-based prediction, an independent measurement, and a required acceptance condition. Explicitly label any unavailable evidence.

**Self-check:** Explain your result in physical words before looking again at the equation. If its magnitude or trend would surprise an engineer watching the mechanism move, review its coordinate, unit conversions, excitation type and validity limits. Do not use any draft value as an equipment setting without a complete review.


---

# U08-L03 — Fatigue and vibratory stress

**OpenSTEM Mechanical Engineering / Book 09 / Mechanical Vibrations**  
*Unit 8: Engineering Design, Testing and Vibration Control | Unreviewed university-level educational manuscript.*

## Learning objectives

After this lesson, you should be able to (1) construct a defensible simplified model of **fatigue and vibratory stress**, (2) explain the cause-and-effect relationship between its parameters and the observable output, (3) reproduce the quantitative screening example without losing units, (4) identify a realistic failure of the model, and (5) propose a repeatable experiment or sensor strategy. The lesson is intentionally written around a physical decision, not merely a formula to memorize.

## Physical setting and mechanisms

Cyclic stress can accumulate fatigue damage; converting measured vibration to stress requires validated strain or structural transfer functions.

**Running example.** A cantilever is subject to a sustained narrowband acceleration at its first bending mode. Start by naming what is *moving*, what imposes the *excitation*, and what establishes the motion reference. A support can be treated as fixed only if its motion is negligible over the frequency range of interest; if a floor, table, shaft or gearbox housing moves, it becomes part of the system. In particular, a displacement reported in millimeters can be either motion in an inertial frame or the difference between two moving points. The two quantities lead to different interpretations of isolation performance and dynamic stress.

A vibration model begins with inertia and a mechanism that transfers forces or energy. Inertia resists acceleration, elastic stiffness supplies a position-dependent restoring force, and mechanical damping removes energy through irreversible processes. A machine may also have forcing from unbalance, pressure pulses, electromagnetic torque, gear contact, road or floor input, or deliberate actuation. Do not include all these effects by default. Begin by isolating the mechanism suggested by the observed response, then test whether omitted effects matter at the operating point. If a linear model cannot reproduce amplitude, phase and frequency dependence together, the disagreement may identify additional physics, rather than an arithmetic problem.

The central interpretive question is not whether an equation has been solved, but whether its dependent variable corresponds to the requested decision. A natural frequency does not alone tell how large the motion will be; frequency of forcing and damping matter as well. Likewise, a reduction in displacement can coincide with a rise in acceleration if the frequency has changed. When comparing candidates, state whether you are minimizing motion, transmitted force, stress, sound, instrument error, fatigue or some weighted combination of those outcomes. These design objectives can conflict.

## Equation and derivation strategy

**Screening calculation:** Cycles per day at 20 Hz are 20×86,400=1,728,000.

To reproduce this calculation, first sketch a free-body diagram with a positive coordinate direction, then write the force or energy balance. Next substitute numerical inputs with units attached. Convert between frequency in hertz and angular frequency only through ω=2πf; convert rpm to Hz through f=rpm/60 for one event per revolution. Decide whether an amplitude is peak, peak-to-peak or RMS and maintain that convention throughout. Unless the input is a clean harmonic, conversions such as a_peak=ω²X_peak or v_RMS=v_peak/sqrt(2) should not be applied blindly. Where a model assumes a single mode or one-dimensional motion, describe the coordinate that stands in for the true three-dimensional structure.

A useful consistency check is to alter one parameter before making the final decision. Increasing mass at fixed stiffness lowers the natural frequency; increasing stiffness at fixed mass raises it. Damping generally decreases resonant amplification but can increase high-frequency force transmission. Increasing harmonic forcing frequency changes the inertial contribution quadratically. These tendencies apply only within the model that produced them: changes in geometry, preload, temperature, amplitude or joint contact can change mass distribution or stiffness at the same time. A model can be dimensionally correct and still physically wrong because it predicts a quantity no sensor actually measures.

## Worked engineering interpretation

Return to the case: A cantilever is subject to a sustained narrowband acceleration at its first bending mode. The screening result is useful for sizing a measurement range, identifying a suspected mode or testing whether an operating frequency overlaps a predicted response band. It is not a certification result. State the inputs you can actually measure, the ones you have merely assumed, and the likely interval of uncertainty. If two configurations differ by less than measurement variation, choosing the numerically better result is unjustified. For a machine with significant temperature changes, test cold and hot states; for a rotating machine, compare the speed sweep in both directions; for a flexible frame, check whether the fixture and mounting method influence the identified mode.

Introduce a second parameter set, changing one input by 10% while holding the others fixed. Predict the sign of the change before calculating. If the sign differs, identify whether the example crossed a resonance or a stability condition, used the wrong output definition, or violated the small-motion assumption. Record a baseline parameter table with source, unit, uncertainty and date. When the mathematical response is highly sensitive to a small change, refine the test plan before declaring that the first design works.

## Boundaries, failure diagnosis and safety

**Important limitation:** Cycle count alone does not determine damage; amplitude, mean stress, environment, geometry and material data are essential. An industrial decision should not replace this qualification with a generic “allow a safety factor.” A factor cannot compensate for an incorrect vibration mode, unseen forcing order, missing contact state, defective sensor mounting or a wrong datum. If a simulation forecasts safe operation but measured vibration increases, stop escalating excitation and investigate the disagreement under controlled conditions. The responsibility to establish safe operating procedures, guards, machine access and acceptance limits belongs to qualified engineering personnel.

One way to diagnose discrepancy is to compare three distinct representations: a time trace, a spectrum or frequency-response curve, and a simple physical sketch of the expected motion. The time trace reveals clipping, impulses, drifting offsets and intermittent contact. The spectrum identifies periodic orders and broadband content but loses much time-localized information. The sketch tests whether the sensor direction can observe the hypothesized mode. A well-fitted numerical peak cannot establish a mechanism if the proposed mode shape is incompatible with the structure.

For measurement, **Use strain gauges at critical locations and qualified fatigue curves when assessing durability.** Measure more than once under a documented load and speed; preserve settings and raw traces. A single amplitude without its frequency band, operating state, transducer orientation and convention is inadequate for comparison. Report model residuals where possible, and identify one datum that could prove the model false. The most useful conclusion may be that a simplified model is insufficient and a more complete test is required.

## Relations to nearby lessons

This lesson builds on **Tuned mass dampers** and prepares for **Uncertainty and robust verification**. These connections matter because the motion predicted in one lesson becomes a forcing input or boundary condition in another. The algebra may look similar while the physical question changes: free response is not forced response, absolute displacement is not relative travel, and a modal natural frequency is not necessarily the frequency of peak operational vibration. Carry definitions of coordinates, units and assumptions forward; do not carry numerical values forward without checking whether the system has changed.

## Guided exercises and assessment

1. **Derivation:** Starting with a labeled free-body diagram or energy balance, derive or explain the screening relationship in this lesson. Show units and confirm at least one limiting case.
2. **Numerical sensitivity:** Recalculate the illustrative case with a 10% change in the parameter most likely to vary in service. Compare the relative change in output with the input change. State whether a linear approximation is justified.
3. **Measurement plan:** For “A cantilever is subject to a sustained narrowband acceleration at its first bending mode.”, choose sensor positions and quantities to measure, and specify a sampling or repeatability requirement. What observation would contradict the simple model?
4. **Model criticism:** Explain exactly why the following warning could overturn a proposed selection: Cycle count alone does not determine damage; amplitude, mean stress, environment, geometry and material data are essential.
5. **Design trade-off:** Compare two possible interventions, one changing inertia or stiffness and the other changing damping or forcing. Explain which practical requirement each intervention might worsen.
6. **Technical communication:** Write a short decision record separating a model-based prediction, an independent measurement, and a required acceptance condition. Explicitly label any unavailable evidence.

**Self-check:** Explain your result in physical words before looking again at the equation. If its magnitude or trend would surprise an engineer watching the mechanism move, review its coordinate, unit conversions, excitation type and validity limits. Do not use any draft value as an equipment setting without a complete review.


---

# U08-L04 — Uncertainty and robust verification

**OpenSTEM Mechanical Engineering / Book 09 / Mechanical Vibrations**  
*Unit 8: Engineering Design, Testing and Vibration Control | Unreviewed university-level educational manuscript.*

## Learning objectives

After this lesson, you should be able to (1) construct a defensible simplified model of **uncertainty and robust verification**, (2) explain the cause-and-effect relationship between its parameters and the observable output, (3) reproduce the quantitative screening example without losing units, (4) identify a realistic failure of the model, and (5) propose a repeatable experiment or sensor strategy. The lesson is intentionally written around a physical decision, not merely a formula to memorize.

## Physical setting and mechanisms

Parameter uncertainty in stiffness, damping, mass and excitation should propagate into resonance and response predictions.

**Running example.** A machine mount stiffness is nominally 8000 N/m but varies between batches. Start by naming what is *moving*, what imposes the *excitation*, and what establishes the motion reference. A support can be treated as fixed only if its motion is negligible over the frequency range of interest; if a floor, table, shaft or gearbox housing moves, it becomes part of the system. In particular, a displacement reported in millimeters can be either motion in an inertial frame or the difference between two moving points. The two quantities lead to different interpretations of isolation performance and dynamic stress.

A vibration model begins with inertia and a mechanism that transfers forces or energy. Inertia resists acceleration, elastic stiffness supplies a position-dependent restoring force, and mechanical damping removes energy through irreversible processes. A machine may also have forcing from unbalance, pressure pulses, electromagnetic torque, gear contact, road or floor input, or deliberate actuation. Do not include all these effects by default. Begin by isolating the mechanism suggested by the observed response, then test whether omitted effects matter at the operating point. If a linear model cannot reproduce amplitude, phase and frequency dependence together, the disagreement may identify additional physics, rather than an arithmetic problem.

The central interpretive question is not whether an equation has been solved, but whether its dependent variable corresponds to the requested decision. A natural frequency does not alone tell how large the motion will be; frequency of forcing and damping matter as well. Likewise, a reduction in displacement can coincide with a rise in acceleration if the frequency has changed. When comparing candidates, state whether you are minimizing motion, transmitted force, stress, sound, instrument error, fatigue or some weighted combination of those outcomes. These design objectives can conflict.

## Equation and derivation strategy

**Screening calculation:** For constant mass, +10% stiffness changes natural frequency by sqrt(1.1)-1≈4.88%.

To reproduce this calculation, first sketch a free-body diagram with a positive coordinate direction, then write the force or energy balance. Next substitute numerical inputs with units attached. Convert between frequency in hertz and angular frequency only through ω=2πf; convert rpm to Hz through f=rpm/60 for one event per revolution. Decide whether an amplitude is peak, peak-to-peak or RMS and maintain that convention throughout. Unless the input is a clean harmonic, conversions such as a_peak=ω²X_peak or v_RMS=v_peak/sqrt(2) should not be applied blindly. Where a model assumes a single mode or one-dimensional motion, describe the coordinate that stands in for the true three-dimensional structure.

A useful consistency check is to alter one parameter before making the final decision. Increasing mass at fixed stiffness lowers the natural frequency; increasing stiffness at fixed mass raises it. Damping generally decreases resonant amplification but can increase high-frequency force transmission. Increasing harmonic forcing frequency changes the inertial contribution quadratically. These tendencies apply only within the model that produced them: changes in geometry, preload, temperature, amplitude or joint contact can change mass distribution or stiffness at the same time. A model can be dimensionally correct and still physically wrong because it predicts a quantity no sensor actually measures.

## Worked engineering interpretation

Return to the case: A machine mount stiffness is nominally 8000 N/m but varies between batches. The screening result is useful for sizing a measurement range, identifying a suspected mode or testing whether an operating frequency overlaps a predicted response band. It is not a certification result. State the inputs you can actually measure, the ones you have merely assumed, and the likely interval of uncertainty. If two configurations differ by less than measurement variation, choosing the numerically better result is unjustified. For a machine with significant temperature changes, test cold and hot states; for a rotating machine, compare the speed sweep in both directions; for a flexible frame, check whether the fixture and mounting method influence the identified mode.

Introduce a second parameter set, changing one input by 10% while holding the others fixed. Predict the sign of the change before calculating. If the sign differs, identify whether the example crossed a resonance or a stability condition, used the wrong output definition, or violated the small-motion assumption. Record a baseline parameter table with source, unit, uncertainty and date. When the mathematical response is highly sensitive to a small change, refine the test plan before declaring that the first design works.

## Boundaries, failure diagnosis and safety

**Important limitation:** Treating one nominal frequency as exact can mask resonance coincidence under aging or temperature shifts. An industrial decision should not replace this qualification with a generic “allow a safety factor.” A factor cannot compensate for an incorrect vibration mode, unseen forcing order, missing contact state, defective sensor mounting or a wrong datum. If a simulation forecasts safe operation but measured vibration increases, stop escalating excitation and investigate the disagreement under controlled conditions. The responsibility to establish safe operating procedures, guards, machine access and acceptance limits belongs to qualified engineering personnel.

One way to diagnose discrepancy is to compare three distinct representations: a time trace, a spectrum or frequency-response curve, and a simple physical sketch of the expected motion. The time trace reveals clipping, impulses, drifting offsets and intermittent contact. The spectrum identifies periodic orders and broadband content but loses much time-localized information. The sketch tests whether the sensor direction can observe the hypothesized mode. A well-fitted numerical peak cannot establish a mechanism if the proposed mode shape is incompatible with the structure.

For measurement, **Perform a tolerance or Monte Carlo study and validate the parameter distributions.** Measure more than once under a documented load and speed; preserve settings and raw traces. A single amplitude without its frequency band, operating state, transducer orientation and convention is inadequate for comparison. Report model residuals where possible, and identify one datum that could prove the model false. The most useful conclusion may be that a simplified model is insufficient and a more complete test is required.

## Relations to nearby lessons

This lesson builds on **Fatigue and vibratory stress** and prepares for **Acceptance testing and engineering decisions**. These connections matter because the motion predicted in one lesson becomes a forcing input or boundary condition in another. The algebra may look similar while the physical question changes: free response is not forced response, absolute displacement is not relative travel, and a modal natural frequency is not necessarily the frequency of peak operational vibration. Carry definitions of coordinates, units and assumptions forward; do not carry numerical values forward without checking whether the system has changed.

## Guided exercises and assessment

1. **Derivation:** Starting with a labeled free-body diagram or energy balance, derive or explain the screening relationship in this lesson. Show units and confirm at least one limiting case.
2. **Numerical sensitivity:** Recalculate the illustrative case with a 10% change in the parameter most likely to vary in service. Compare the relative change in output with the input change. State whether a linear approximation is justified.
3. **Measurement plan:** For “A machine mount stiffness is nominally 8000 N/m but varies between batches.”, choose sensor positions and quantities to measure, and specify a sampling or repeatability requirement. What observation would contradict the simple model?
4. **Model criticism:** Explain exactly why the following warning could overturn a proposed selection: Treating one nominal frequency as exact can mask resonance coincidence under aging or temperature shifts.
5. **Design trade-off:** Compare two possible interventions, one changing inertia or stiffness and the other changing damping or forcing. Explain which practical requirement each intervention might worsen.
6. **Technical communication:** Write a short decision record separating a model-based prediction, an independent measurement, and a required acceptance condition. Explicitly label any unavailable evidence.

**Self-check:** Explain your result in physical words before looking again at the equation. If its magnitude or trend would surprise an engineer watching the mechanism move, review its coordinate, unit conversions, excitation type and validity limits. Do not use any draft value as an equipment setting without a complete review.


---

# U08-L05 — Acceptance testing and engineering decisions

**OpenSTEM Mechanical Engineering / Book 09 / Mechanical Vibrations**  
*Unit 8: Engineering Design, Testing and Vibration Control | Unreviewed university-level educational manuscript.*

## Learning objectives

After this lesson, you should be able to (1) construct a defensible simplified model of **acceptance testing and engineering decisions**, (2) explain the cause-and-effect relationship between its parameters and the observable output, (3) reproduce the quantitative screening example without losing units, (4) identify a realistic failure of the model, and (5) propose a repeatable experiment or sensor strategy. The lesson is intentionally written around a physical decision, not merely a formula to memorize.

## Physical setting and mechanisms

Verification ties operating conditions, calibrated measurements, repeatability, criteria and corrective actions to a documented design requirement.

**Running example.** A redesigned gearbox support passes one short trial but field duty includes variable speed and temperature. Start by naming what is *moving*, what imposes the *excitation*, and what establishes the motion reference. A support can be treated as fixed only if its motion is negligible over the frequency range of interest; if a floor, table, shaft or gearbox housing moves, it becomes part of the system. In particular, a displacement reported in millimeters can be either motion in an inertial frame or the difference between two moving points. The two quantities lead to different interpretations of isolation performance and dynamic stress.

A vibration model begins with inertia and a mechanism that transfers forces or energy. Inertia resists acceleration, elastic stiffness supplies a position-dependent restoring force, and mechanical damping removes energy through irreversible processes. A machine may also have forcing from unbalance, pressure pulses, electromagnetic torque, gear contact, road or floor input, or deliberate actuation. Do not include all these effects by default. Begin by isolating the mechanism suggested by the observed response, then test whether omitted effects matter at the operating point. If a linear model cannot reproduce amplitude, phase and frequency dependence together, the disagreement may identify additional physics, rather than an arithmetic problem.

The central interpretive question is not whether an equation has been solved, but whether its dependent variable corresponds to the requested decision. A natural frequency does not alone tell how large the motion will be; frequency of forcing and damping matter as well. Likewise, a reduction in displacement can coincide with a rise in acceleration if the frequency has changed. When comparing candidates, state whether you are minimizing motion, transmitted force, stress, sound, instrument error, fatigue or some weighted combination of those outcomes. These design objectives can conflict.

## Equation and derivation strategy

**Screening calculation:** Compute measured change as (A_new-A_old)/A_old; from 5 to 3 mm/s RMS, change=-40%.

To reproduce this calculation, first sketch a free-body diagram with a positive coordinate direction, then write the force or energy balance. Next substitute numerical inputs with units attached. Convert between frequency in hertz and angular frequency only through ω=2πf; convert rpm to Hz through f=rpm/60 for one event per revolution. Decide whether an amplitude is peak, peak-to-peak or RMS and maintain that convention throughout. Unless the input is a clean harmonic, conversions such as a_peak=ω²X_peak or v_RMS=v_peak/sqrt(2) should not be applied blindly. Where a model assumes a single mode or one-dimensional motion, describe the coordinate that stands in for the true three-dimensional structure.

A useful consistency check is to alter one parameter before making the final decision. Increasing mass at fixed stiffness lowers the natural frequency; increasing stiffness at fixed mass raises it. Damping generally decreases resonant amplification but can increase high-frequency force transmission. Increasing harmonic forcing frequency changes the inertial contribution quadratically. These tendencies apply only within the model that produced them: changes in geometry, preload, temperature, amplitude or joint contact can change mass distribution or stiffness at the same time. A model can be dimensionally correct and still physically wrong because it predicts a quantity no sensor actually measures.

## Worked engineering interpretation

Return to the case: A redesigned gearbox support passes one short trial but field duty includes variable speed and temperature. The screening result is useful for sizing a measurement range, identifying a suspected mode or testing whether an operating frequency overlaps a predicted response band. It is not a certification result. State the inputs you can actually measure, the ones you have merely assumed, and the likely interval of uncertainty. If two configurations differ by less than measurement variation, choosing the numerically better result is unjustified. For a machine with significant temperature changes, test cold and hot states; for a rotating machine, compare the speed sweep in both directions; for a flexible frame, check whether the fixture and mounting method influence the identified mode.

Introduce a second parameter set, changing one input by 10% while holding the others fixed. Predict the sign of the change before calculating. If the sign differs, identify whether the example crossed a resonance or a stability condition, used the wrong output definition, or violated the small-motion assumption. Record a baseline parameter table with source, unit, uncertainty and date. When the mathematical response is highly sensitive to a small change, refine the test plan before declaring that the first design works.

## Boundaries, failure diagnosis and safety

**Important limitation:** A relative improvement does not automatically demonstrate compliance with application-specific limits or fatigue requirements. An industrial decision should not replace this qualification with a generic “allow a safety factor.” A factor cannot compensate for an incorrect vibration mode, unseen forcing order, missing contact state, defective sensor mounting or a wrong datum. If a simulation forecasts safe operation but measured vibration increases, stop escalating excitation and investigate the disagreement under controlled conditions. The responsibility to establish safe operating procedures, guards, machine access and acceptance limits belongs to qualified engineering personnel.

One way to diagnose discrepancy is to compare three distinct representations: a time trace, a spectrum or frequency-response curve, and a simple physical sketch of the expected motion. The time trace reveals clipping, impulses, drifting offsets and intermittent contact. The spectrum identifies periodic orders and broadband content but loses much time-localized information. The sketch tests whether the sensor direction can observe the hypothesized mode. A well-fitted numerical peak cannot establish a mechanism if the proposed mode shape is incompatible with the structure.

For measurement, **Use a repeatable duty-cycle matrix, record test uncertainty and retain traceable raw data.** Measure more than once under a documented load and speed; preserve settings and raw traces. A single amplitude without its frequency band, operating state, transducer orientation and convention is inadequate for comparison. Report model residuals where possible, and identify one datum that could prove the model false. The most useful conclusion may be that a simplified model is insufficient and a more complete test is required.

## Relations to nearby lessons

This lesson builds on **Uncertainty and robust verification** and prepares for **the unit capstone**. These connections matter because the motion predicted in one lesson becomes a forcing input or boundary condition in another. The algebra may look similar while the physical question changes: free response is not forced response, absolute displacement is not relative travel, and a modal natural frequency is not necessarily the frequency of peak operational vibration. Carry definitions of coordinates, units and assumptions forward; do not carry numerical values forward without checking whether the system has changed.

## Guided exercises and assessment

1. **Derivation:** Starting with a labeled free-body diagram or energy balance, derive or explain the screening relationship in this lesson. Show units and confirm at least one limiting case.
2. **Numerical sensitivity:** Recalculate the illustrative case with a 10% change in the parameter most likely to vary in service. Compare the relative change in output with the input change. State whether a linear approximation is justified.
3. **Measurement plan:** For “A redesigned gearbox support passes one short trial but field duty includes variable speed and temperature.”, choose sensor positions and quantities to measure, and specify a sampling or repeatability requirement. What observation would contradict the simple model?
4. **Model criticism:** Explain exactly why the following warning could overturn a proposed selection: A relative improvement does not automatically demonstrate compliance with application-specific limits or fatigue requirements.
5. **Design trade-off:** Compare two possible interventions, one changing inertia or stiffness and the other changing damping or forcing. Explain which practical requirement each intervention might worsen.
6. **Technical communication:** Write a short decision record separating a model-based prediction, an independent measurement, and a required acceptance condition. Explicitly label any unavailable evidence.

**Self-check:** Explain your result in physical words before looking again at the equation. If its magnitude or trend would surprise an engineer watching the mechanism move, review its coordinate, unit conversions, excitation type and validity limits. Do not use any draft value as an equipment setting without a complete review.


---

