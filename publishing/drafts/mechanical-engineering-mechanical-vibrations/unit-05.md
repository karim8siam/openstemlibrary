# Unit 05: Multi-Degree-of-Freedom Vibrations and Modal Analysis

**Course Code**: MVB 205 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Multi-Degree-of-Freedom Vibrations and Modal Analysis**.

# U05-L01 — Two-degree-of-freedom model

**OpenSTEM Mechanical Engineering / Book 09 / Mechanical Vibrations**  
*Unit 5: Multi-Degree-of-Freedom Vibrations and Modal Analysis | Unreviewed university-level educational manuscript.*

## Learning objectives

After this lesson, you should be able to (1) construct a defensible simplified model of **two-degree-of-freedom model**, (2) explain the cause-and-effect relationship between its parameters and the observable output, (3) reproduce the quantitative screening example without losing units, (4) identify a realistic failure of the model, and (5) propose a repeatable experiment or sensor strategy. The lesson is intentionally written around a physical decision, not merely a formula to memorize.

## Physical setting and mechanisms

With two masses and linear coupling, Mq¨+Kq=0 yields eigenvalues ω² from det(K-ω²M)=0; each eigenvector describes relative modal motion.

**Running example.** Two equal masses each 2 kg are attached with boundary and coupling springs, both 1000 N/m. Start by naming what is *moving*, what imposes the *excitation*, and what establishes the motion reference. A support can be treated as fixed only if its motion is negligible over the frequency range of interest; if a floor, table, shaft or gearbox housing moves, it becomes part of the system. In particular, a displacement reported in millimeters can be either motion in an inertial frame or the difference between two moving points. The two quantities lead to different interpretations of isolation performance and dynamic stress.

A vibration model begins with inertia and a mechanism that transfers forces or energy. Inertia resists acceleration, elastic stiffness supplies a position-dependent restoring force, and mechanical damping removes energy through irreversible processes. A machine may also have forcing from unbalance, pressure pulses, electromagnetic torque, gear contact, road or floor input, or deliberate actuation. Do not include all these effects by default. Begin by isolating the mechanism suggested by the observed response, then test whether omitted effects matter at the operating point. If a linear model cannot reproduce amplitude, phase and frequency dependence together, the disagreement may identify additional physics, rather than an arithmetic problem.

The central interpretive question is not whether an equation has been solved, but whether its dependent variable corresponds to the requested decision. A natural frequency does not alone tell how large the motion will be; frequency of forcing and damping matter as well. Likewise, a reduction in displacement can coincide with a rise in acceleration if the frequency has changed. When comparing candidates, state whether you are minimizing motion, transmitted force, stress, sound, instrument error, fatigue or some weighted combination of those outcomes. These design objectives can conflict.

## Equation and derivation strategy

**Screening calculation:** For M=2I and K=[[2000,-1000],[-1000,1000]], eigenfrequencies are ≈2.200 and 5.763 Hz.

To reproduce this calculation, first sketch a free-body diagram with a positive coordinate direction, then write the force or energy balance. Next substitute numerical inputs with units attached. Convert between frequency in hertz and angular frequency only through ω=2πf; convert rpm to Hz through f=rpm/60 for one event per revolution. Decide whether an amplitude is peak, peak-to-peak or RMS and maintain that convention throughout. Unless the input is a clean harmonic, conversions such as a_peak=ω²X_peak or v_RMS=v_peak/sqrt(2) should not be applied blindly. Where a model assumes a single mode or one-dimensional motion, describe the coordinate that stands in for the true three-dimensional structure.

A useful consistency check is to alter one parameter before making the final decision. Increasing mass at fixed stiffness lowers the natural frequency; increasing stiffness at fixed mass raises it. Damping generally decreases resonant amplification but can increase high-frequency force transmission. Increasing harmonic forcing frequency changes the inertial contribution quadratically. These tendencies apply only within the model that produced them: changes in geometry, preload, temperature, amplitude or joint contact can change mass distribution or stiffness at the same time. A model can be dimensionally correct and still physically wrong because it predicts a quantity no sensor actually measures.

## Worked engineering interpretation

Return to the case: Two equal masses each 2 kg are attached with boundary and coupling springs, both 1000 N/m. The screening result is useful for sizing a measurement range, identifying a suspected mode or testing whether an operating frequency overlaps a predicted response band. It is not a certification result. State the inputs you can actually measure, the ones you have merely assumed, and the likely interval of uncertainty. If two configurations differ by less than measurement variation, choosing the numerically better result is unjustified. For a machine with significant temperature changes, test cold and hot states; for a rotating machine, compare the speed sweep in both directions; for a flexible frame, check whether the fixture and mounting method influence the identified mode.

Introduce a second parameter set, changing one input by 10% while holding the others fixed. Predict the sign of the change before calculating. If the sign differs, identify whether the example crossed a resonance or a stability condition, used the wrong output definition, or violated the small-motion assumption. Record a baseline parameter table with source, unit, uncertainty and date. When the mathematical response is highly sensitive to a small change, refine the test plan before declaring that the first design works.

## Boundaries, failure diagnosis and safety

**Important limitation:** An eigenvector has arbitrary scale and sign; modes do not directly give actual response amplitudes. An industrial decision should not replace this qualification with a generic “allow a safety factor.” A factor cannot compensate for an incorrect vibration mode, unseen forcing order, missing contact state, defective sensor mounting or a wrong datum. If a simulation forecasts safe operation but measured vibration increases, stop escalating excitation and investigate the disagreement under controlled conditions. The responsibility to establish safe operating procedures, guards, machine access and acceptance limits belongs to qualified engineering personnel.

One way to diagnose discrepancy is to compare three distinct representations: a time trace, a spectrum or frequency-response curve, and a simple physical sketch of the expected motion. The time trace reveals clipping, impulses, drifting offsets and intermittent contact. The spectrum identifies periodic orders and broadband content but loses much time-localized information. The sketch tests whether the sensor direction can observe the hypothesized mode. A well-fitted numerical peak cannot establish a mechanism if the proposed mode shape is incompatible with the structure.

For measurement, **Compare measured operational deflection shapes at identified resonant frequencies.** Measure more than once under a documented load and speed; preserve settings and raw traces. A single amplitude without its frequency band, operating state, transducer orientation and convention is inadequate for comparison. Report model residuals where possible, and identify one datum that could prove the model false. The most useful conclusion may be that a simplified model is insufficient and a more complete test is required.

## Relations to nearby lessons

This lesson builds on **the previous unit foundation** and prepares for **Mass and stiffness matrices**. These connections matter because the motion predicted in one lesson becomes a forcing input or boundary condition in another. The algebra may look similar while the physical question changes: free response is not forced response, absolute displacement is not relative travel, and a modal natural frequency is not necessarily the frequency of peak operational vibration. Carry definitions of coordinates, units and assumptions forward; do not carry numerical values forward without checking whether the system has changed.

## Guided exercises and assessment

1. **Derivation:** Starting with a labeled free-body diagram or energy balance, derive or explain the screening relationship in this lesson. Show units and confirm at least one limiting case.
2. **Numerical sensitivity:** Recalculate the illustrative case with a 10% change in the parameter most likely to vary in service. Compare the relative change in output with the input change. State whether a linear approximation is justified.
3. **Measurement plan:** For “Two equal masses each 2 kg are attached with boundary and coupling springs, both 1000 N/m.”, choose sensor positions and quantities to measure, and specify a sampling or repeatability requirement. What observation would contradict the simple model?
4. **Model criticism:** Explain exactly why the following warning could overturn a proposed selection: An eigenvector has arbitrary scale and sign; modes do not directly give actual response amplitudes.
5. **Design trade-off:** Compare two possible interventions, one changing inertia or stiffness and the other changing damping or forcing. Explain which practical requirement each intervention might worsen.
6. **Technical communication:** Write a short decision record separating a model-based prediction, an independent measurement, and a required acceptance condition. Explicitly label any unavailable evidence.

**Self-check:** Explain your result in physical words before looking again at the equation. If its magnitude or trend would surprise an engineer watching the mechanism move, review its coordinate, unit conversions, excitation type and validity limits. Do not use any draft value as an equipment setting without a complete review.


---

# U05-L02 — Mass and stiffness matrices

**OpenSTEM Mechanical Engineering / Book 09 / Mechanical Vibrations**  
*Unit 5: Multi-Degree-of-Freedom Vibrations and Modal Analysis | Unreviewed university-level educational manuscript.*

## Learning objectives

After this lesson, you should be able to (1) construct a defensible simplified model of **mass and stiffness matrices**, (2) explain the cause-and-effect relationship between its parameters and the observable output, (3) reproduce the quantitative screening example without losing units, (4) identify a realistic failure of the model, and (5) propose a repeatable experiment or sensor strategy. The lesson is intentionally written around a physical decision, not merely a formula to memorize.

## Physical setting and mechanisms

The matrix entries follow kinetic and potential energy, with off-diagonal terms describing coupling; positive mass and stable stiffness give physical modes.

**Running example.** A frame translation couples to rotation because its center of mass is offset from the attachment line. Start by naming what is *moving*, what imposes the *excitation*, and what establishes the motion reference. A support can be treated as fixed only if its motion is negligible over the frequency range of interest; if a floor, table, shaft or gearbox housing moves, it becomes part of the system. In particular, a displacement reported in millimeters can be either motion in an inertial frame or the difference between two moving points. The two quantities lead to different interpretations of isolation performance and dynamic stress.

A vibration model begins with inertia and a mechanism that transfers forces or energy. Inertia resists acceleration, elastic stiffness supplies a position-dependent restoring force, and mechanical damping removes energy through irreversible processes. A machine may also have forcing from unbalance, pressure pulses, electromagnetic torque, gear contact, road or floor input, or deliberate actuation. Do not include all these effects by default. Begin by isolating the mechanism suggested by the observed response, then test whether omitted effects matter at the operating point. If a linear model cannot reproduce amplitude, phase and frequency dependence together, the disagreement may identify additional physics, rather than an arithmetic problem.

The central interpretive question is not whether an equation has been solved, but whether its dependent variable corresponds to the requested decision. A natural frequency does not alone tell how large the motion will be; frequency of forcing and damping matter as well. Likewise, a reduction in displacement can coincide with a rise in acceleration if the frequency has changed. When comparing candidates, state whether you are minimizing motion, transmitted force, stress, sound, instrument error, fatigue or some weighted combination of those outcomes. These design objectives can conflict.

## Equation and derivation strategy

**Screening calculation:** With K=[[2k,-k],[-k,k]], k=1000 N/m, det(K)=k²>0.

To reproduce this calculation, first sketch a free-body diagram with a positive coordinate direction, then write the force or energy balance. Next substitute numerical inputs with units attached. Convert between frequency in hertz and angular frequency only through ω=2πf; convert rpm to Hz through f=rpm/60 for one event per revolution. Decide whether an amplitude is peak, peak-to-peak or RMS and maintain that convention throughout. Unless the input is a clean harmonic, conversions such as a_peak=ω²X_peak or v_RMS=v_peak/sqrt(2) should not be applied blindly. Where a model assumes a single mode or one-dimensional motion, describe the coordinate that stands in for the true three-dimensional structure.

A useful consistency check is to alter one parameter before making the final decision. Increasing mass at fixed stiffness lowers the natural frequency; increasing stiffness at fixed mass raises it. Damping generally decreases resonant amplification but can increase high-frequency force transmission. Increasing harmonic forcing frequency changes the inertial contribution quadratically. These tendencies apply only within the model that produced them: changes in geometry, preload, temperature, amplitude or joint contact can change mass distribution or stiffness at the same time. A model can be dimensionally correct and still physically wrong because it predicts a quantity no sensor actually measures.

## Worked engineering interpretation

Return to the case: A frame translation couples to rotation because its center of mass is offset from the attachment line. The screening result is useful for sizing a measurement range, identifying a suspected mode or testing whether an operating frequency overlaps a predicted response band. It is not a certification result. State the inputs you can actually measure, the ones you have merely assumed, and the likely interval of uncertainty. If two configurations differ by less than measurement variation, choosing the numerically better result is unjustified. For a machine with significant temperature changes, test cold and hot states; for a rotating machine, compare the speed sweep in both directions; for a flexible frame, check whether the fixture and mounting method influence the identified mode.

Introduce a second parameter set, changing one input by 10% while holding the others fixed. Predict the sign of the change before calculating. If the sign differs, identify whether the example crossed a resonance or a stability condition, used the wrong output definition, or violated the small-motion assumption. Record a baseline parameter table with source, unit, uncertainty and date. When the mathematical response is highly sensitive to a small change, refine the test plan before declaring that the first design works.

## Boundaries, failure diagnosis and safety

**Important limitation:** Assigning diagonal mass without checking coordinate definitions can neglect rotary inertia and coupling. An industrial decision should not replace this qualification with a generic “allow a safety factor.” A factor cannot compensate for an incorrect vibration mode, unseen forcing order, missing contact state, defective sensor mounting or a wrong datum. If a simulation forecasts safe operation but measured vibration increases, stop escalating excitation and investigate the disagreement under controlled conditions. The responsibility to establish safe operating procedures, guards, machine access and acceptance limits belongs to qualified engineering personnel.

One way to diagnose discrepancy is to compare three distinct representations: a time trace, a spectrum or frequency-response curve, and a simple physical sketch of the expected motion. The time trace reveals clipping, impulses, drifting offsets and intermittent contact. The spectrum identifies periodic orders and broadband content but loses much time-localized information. The sketch tests whether the sensor direction can observe the hypothesized mode. A well-fitted numerical peak cannot establish a mechanism if the proposed mode shape is incompatible with the structure.

For measurement, **Derive equations from a free-body diagram and independent energy expressions.** Measure more than once under a documented load and speed; preserve settings and raw traces. A single amplitude without its frequency band, operating state, transducer orientation and convention is inadequate for comparison. Report model residuals where possible, and identify one datum that could prove the model false. The most useful conclusion may be that a simplified model is insufficient and a more complete test is required.

## Relations to nearby lessons

This lesson builds on **Two-degree-of-freedom model** and prepares for **Modal orthogonality and normalization**. These connections matter because the motion predicted in one lesson becomes a forcing input or boundary condition in another. The algebra may look similar while the physical question changes: free response is not forced response, absolute displacement is not relative travel, and a modal natural frequency is not necessarily the frequency of peak operational vibration. Carry definitions of coordinates, units and assumptions forward; do not carry numerical values forward without checking whether the system has changed.

## Guided exercises and assessment

1. **Derivation:** Starting with a labeled free-body diagram or energy balance, derive or explain the screening relationship in this lesson. Show units and confirm at least one limiting case.
2. **Numerical sensitivity:** Recalculate the illustrative case with a 10% change in the parameter most likely to vary in service. Compare the relative change in output with the input change. State whether a linear approximation is justified.
3. **Measurement plan:** For “A frame translation couples to rotation because its center of mass is offset from the attachment line.”, choose sensor positions and quantities to measure, and specify a sampling or repeatability requirement. What observation would contradict the simple model?
4. **Model criticism:** Explain exactly why the following warning could overturn a proposed selection: Assigning diagonal mass without checking coordinate definitions can neglect rotary inertia and coupling.
5. **Design trade-off:** Compare two possible interventions, one changing inertia or stiffness and the other changing damping or forcing. Explain which practical requirement each intervention might worsen.
6. **Technical communication:** Write a short decision record separating a model-based prediction, an independent measurement, and a required acceptance condition. Explicitly label any unavailable evidence.

**Self-check:** Explain your result in physical words before looking again at the equation. If its magnitude or trend would surprise an engineer watching the mechanism move, review its coordinate, unit conversions, excitation type and validity limits. Do not use any draft value as an equipment setting without a complete review.


---

# U05-L03 — Modal orthogonality and normalization

**OpenSTEM Mechanical Engineering / Book 09 / Mechanical Vibrations**  
*Unit 5: Multi-Degree-of-Freedom Vibrations and Modal Analysis | Unreviewed university-level educational manuscript.*

## Learning objectives

After this lesson, you should be able to (1) construct a defensible simplified model of **modal orthogonality and normalization**, (2) explain the cause-and-effect relationship between its parameters and the observable output, (3) reproduce the quantitative screening example without losing units, (4) identify a realistic failure of the model, and (5) propose a repeatable experiment or sensor strategy. The lesson is intentionally written around a physical decision, not merely a formula to memorize.

## Physical setting and mechanisms

For symmetric positive definite M and K, distinct undamped modes satisfy φ_i^T M φ_j=0 and φ_i^T K φ_j=0.

**Running example.** A laboratory modal test produces two mode vectors from different sensor locations. Start by naming what is *moving*, what imposes the *excitation*, and what establishes the motion reference. A support can be treated as fixed only if its motion is negligible over the frequency range of interest; if a floor, table, shaft or gearbox housing moves, it becomes part of the system. In particular, a displacement reported in millimeters can be either motion in an inertial frame or the difference between two moving points. The two quantities lead to different interpretations of isolation performance and dynamic stress.

A vibration model begins with inertia and a mechanism that transfers forces or energy. Inertia resists acceleration, elastic stiffness supplies a position-dependent restoring force, and mechanical damping removes energy through irreversible processes. A machine may also have forcing from unbalance, pressure pulses, electromagnetic torque, gear contact, road or floor input, or deliberate actuation. Do not include all these effects by default. Begin by isolating the mechanism suggested by the observed response, then test whether omitted effects matter at the operating point. If a linear model cannot reproduce amplitude, phase and frequency dependence together, the disagreement may identify additional physics, rather than an arithmetic problem.

The central interpretive question is not whether an equation has been solved, but whether its dependent variable corresponds to the requested decision. A natural frequency does not alone tell how large the motion will be; frequency of forcing and damping matter as well. Likewise, a reduction in displacement can coincide with a rise in acceleration if the frequency has changed. When comparing candidates, state whether you are minimizing motion, transmitted force, stress, sound, instrument error, fatigue or some weighted combination of those outcomes. These design objectives can conflict.

## Equation and derivation strategy

**Screening calculation:** Mass-normalization sets φ_i^T M φ_i=1.

To reproduce this calculation, first sketch a free-body diagram with a positive coordinate direction, then write the force or energy balance. Next substitute numerical inputs with units attached. Convert between frequency in hertz and angular frequency only through ω=2πf; convert rpm to Hz through f=rpm/60 for one event per revolution. Decide whether an amplitude is peak, peak-to-peak or RMS and maintain that convention throughout. Unless the input is a clean harmonic, conversions such as a_peak=ω²X_peak or v_RMS=v_peak/sqrt(2) should not be applied blindly. Where a model assumes a single mode or one-dimensional motion, describe the coordinate that stands in for the true three-dimensional structure.

A useful consistency check is to alter one parameter before making the final decision. Increasing mass at fixed stiffness lowers the natural frequency; increasing stiffness at fixed mass raises it. Damping generally decreases resonant amplification but can increase high-frequency force transmission. Increasing harmonic forcing frequency changes the inertial contribution quadratically. These tendencies apply only within the model that produced them: changes in geometry, preload, temperature, amplitude or joint contact can change mass distribution or stiffness at the same time. A model can be dimensionally correct and still physically wrong because it predicts a quantity no sensor actually measures.

## Worked engineering interpretation

Return to the case: A laboratory modal test produces two mode vectors from different sensor locations. The screening result is useful for sizing a measurement range, identifying a suspected mode or testing whether an operating frequency overlaps a predicted response band. It is not a certification result. State the inputs you can actually measure, the ones you have merely assumed, and the likely interval of uncertainty. If two configurations differ by less than measurement variation, choosing the numerically better result is unjustified. For a machine with significant temperature changes, test cold and hot states; for a rotating machine, compare the speed sweep in both directions; for a flexible frame, check whether the fixture and mounting method influence the identified mode.

Introduce a second parameter set, changing one input by 10% while holding the others fixed. Predict the sign of the change before calculating. If the sign differs, identify whether the example crossed a resonance or a stability condition, used the wrong output definition, or violated the small-motion assumption. Record a baseline parameter table with source, unit, uncertainty and date. When the mathematical response is highly sensitive to a small change, refine the test plan before declaring that the first design works.

## Boundaries, failure diagnosis and safety

**Important limitation:** Experimental complex modes under general damping may not obey classical real-mode orthogonality. An industrial decision should not replace this qualification with a generic “allow a safety factor.” A factor cannot compensate for an incorrect vibration mode, unseen forcing order, missing contact state, defective sensor mounting or a wrong datum. If a simulation forecasts safe operation but measured vibration increases, stop escalating excitation and investigate the disagreement under controlled conditions. The responsibility to establish safe operating procedures, guards, machine access and acceptance limits belongs to qualified engineering personnel.

One way to diagnose discrepancy is to compare three distinct representations: a time trace, a spectrum or frequency-response curve, and a simple physical sketch of the expected motion. The time trace reveals clipping, impulses, drifting offsets and intermittent contact. The spectrum identifies periodic orders and broadband content but loses much time-localized information. The sketch tests whether the sensor direction can observe the hypothesized mode. A well-fitted numerical peak cannot establish a mechanism if the proposed mode shape is incompatible with the structure.

For measurement, **Compare normalized shape ratios and report the reference degree of freedom.** Measure more than once under a documented load and speed; preserve settings and raw traces. A single amplitude without its frequency band, operating state, transducer orientation and convention is inadequate for comparison. Report model residuals where possible, and identify one datum that could prove the model false. The most useful conclusion may be that a simplified model is insufficient and a more complete test is required.

## Relations to nearby lessons

This lesson builds on **Mass and stiffness matrices** and prepares for **Modal superposition**. These connections matter because the motion predicted in one lesson becomes a forcing input or boundary condition in another. The algebra may look similar while the physical question changes: free response is not forced response, absolute displacement is not relative travel, and a modal natural frequency is not necessarily the frequency of peak operational vibration. Carry definitions of coordinates, units and assumptions forward; do not carry numerical values forward without checking whether the system has changed.

## Guided exercises and assessment

1. **Derivation:** Starting with a labeled free-body diagram or energy balance, derive or explain the screening relationship in this lesson. Show units and confirm at least one limiting case.
2. **Numerical sensitivity:** Recalculate the illustrative case with a 10% change in the parameter most likely to vary in service. Compare the relative change in output with the input change. State whether a linear approximation is justified.
3. **Measurement plan:** For “A laboratory modal test produces two mode vectors from different sensor locations.”, choose sensor positions and quantities to measure, and specify a sampling or repeatability requirement. What observation would contradict the simple model?
4. **Model criticism:** Explain exactly why the following warning could overturn a proposed selection: Experimental complex modes under general damping may not obey classical real-mode orthogonality.
5. **Design trade-off:** Compare two possible interventions, one changing inertia or stiffness and the other changing damping or forcing. Explain which practical requirement each intervention might worsen.
6. **Technical communication:** Write a short decision record separating a model-based prediction, an independent measurement, and a required acceptance condition. Explicitly label any unavailable evidence.

**Self-check:** Explain your result in physical words before looking again at the equation. If its magnitude or trend would surprise an engineer watching the mechanism move, review its coordinate, unit conversions, excitation type and validity limits. Do not use any draft value as an equipment setting without a complete review.


---

# U05-L04 — Modal superposition

**OpenSTEM Mechanical Engineering / Book 09 / Mechanical Vibrations**  
*Unit 5: Multi-Degree-of-Freedom Vibrations and Modal Analysis | Unreviewed university-level educational manuscript.*

## Learning objectives

After this lesson, you should be able to (1) construct a defensible simplified model of **modal superposition**, (2) explain the cause-and-effect relationship between its parameters and the observable output, (3) reproduce the quantitative screening example without losing units, (4) identify a realistic failure of the model, and (5) propose a repeatable experiment or sensor strategy. The lesson is intentionally written around a physical decision, not merely a formula to memorize.

## Physical setting and mechanisms

A linear response can be expressed q(t)=Σφ_j η_j(t); modal coordinates simplify an undamped or classically damped system when modes are complete enough.

**Running example.** A tall support frame vibrates in bending and rocking under an eccentric motor. Start by naming what is *moving*, what imposes the *excitation*, and what establishes the motion reference. A support can be treated as fixed only if its motion is negligible over the frequency range of interest; if a floor, table, shaft or gearbox housing moves, it becomes part of the system. In particular, a displacement reported in millimeters can be either motion in an inertial frame or the difference between two moving points. The two quantities lead to different interpretations of isolation performance and dynamic stress.

A vibration model begins with inertia and a mechanism that transfers forces or energy. Inertia resists acceleration, elastic stiffness supplies a position-dependent restoring force, and mechanical damping removes energy through irreversible processes. A machine may also have forcing from unbalance, pressure pulses, electromagnetic torque, gear contact, road or floor input, or deliberate actuation. Do not include all these effects by default. Begin by isolating the mechanism suggested by the observed response, then test whether omitted effects matter at the operating point. If a linear model cannot reproduce amplitude, phase and frequency dependence together, the disagreement may identify additional physics, rather than an arithmetic problem.

The central interpretive question is not whether an equation has been solved, but whether its dependent variable corresponds to the requested decision. A natural frequency does not alone tell how large the motion will be; frequency of forcing and damping matter as well. Likewise, a reduction in displacement can coincide with a rise in acceleration if the frequency has changed. When comparing candidates, state whether you are minimizing motion, transmitted force, stress, sound, instrument error, fatigue or some weighted combination of those outcomes. These design objectives can conflict.

## Equation and derivation strategy

**Screening calculation:** If two modes are retained, q≈φ_1η_1+φ_2η_2.

To reproduce this calculation, first sketch a free-body diagram with a positive coordinate direction, then write the force or energy balance. Next substitute numerical inputs with units attached. Convert between frequency in hertz and angular frequency only through ω=2πf; convert rpm to Hz through f=rpm/60 for one event per revolution. Decide whether an amplitude is peak, peak-to-peak or RMS and maintain that convention throughout. Unless the input is a clean harmonic, conversions such as a_peak=ω²X_peak or v_RMS=v_peak/sqrt(2) should not be applied blindly. Where a model assumes a single mode or one-dimensional motion, describe the coordinate that stands in for the true three-dimensional structure.

A useful consistency check is to alter one parameter before making the final decision. Increasing mass at fixed stiffness lowers the natural frequency; increasing stiffness at fixed mass raises it. Damping generally decreases resonant amplification but can increase high-frequency force transmission. Increasing harmonic forcing frequency changes the inertial contribution quadratically. These tendencies apply only within the model that produced them: changes in geometry, preload, temperature, amplitude or joint contact can change mass distribution or stiffness at the same time. A model can be dimensionally correct and still physically wrong because it predicts a quantity no sensor actually measures.

## Worked engineering interpretation

Return to the case: A tall support frame vibrates in bending and rocking under an eccentric motor. The screening result is useful for sizing a measurement range, identifying a suspected mode or testing whether an operating frequency overlaps a predicted response band. It is not a certification result. State the inputs you can actually measure, the ones you have merely assumed, and the likely interval of uncertainty. If two configurations differ by less than measurement variation, choosing the numerically better result is unjustified. For a machine with significant temperature changes, test cold and hot states; for a rotating machine, compare the speed sweep in both directions; for a flexible frame, check whether the fixture and mounting method influence the identified mode.

Introduce a second parameter set, changing one input by 10% while holding the others fixed. Predict the sign of the change before calculating. If the sign differs, identify whether the example crossed a resonance or a stability condition, used the wrong output definition, or violated the small-motion assumption. Record a baseline parameter table with source, unit, uncertainty and date. When the mathematical response is highly sensitive to a small change, refine the test plan before declaring that the first design works.

## Boundaries, failure diagnosis and safety

**Important limitation:** Truncated models can miss local stress and high-frequency acceleration even if global displacement is accurate. An industrial decision should not replace this qualification with a generic “allow a safety factor.” A factor cannot compensate for an incorrect vibration mode, unseen forcing order, missing contact state, defective sensor mounting or a wrong datum. If a simulation forecasts safe operation but measured vibration increases, stop escalating excitation and investigate the disagreement under controlled conditions. The responsibility to establish safe operating procedures, guards, machine access and acceptance limits belongs to qualified engineering personnel.

One way to diagnose discrepancy is to compare three distinct representations: a time trace, a spectrum or frequency-response curve, and a simple physical sketch of the expected motion. The time trace reveals clipping, impulses, drifting offsets and intermittent contact. The spectrum identifies periodic orders and broadband content but loses much time-localized information. The sketch tests whether the sensor direction can observe the hypothesized mode. A well-fitted numerical peak cannot establish a mechanism if the proposed mode shape is incompatible with the structure.

For measurement, **Converge computed response while adding modes; inspect neglected resonances.** Measure more than once under a documented load and speed; preserve settings and raw traces. A single amplitude without its frequency band, operating state, transducer orientation and convention is inadequate for comparison. Report model residuals where possible, and identify one datum that could prove the model false. The most useful conclusion may be that a simplified model is insufficient and a more complete test is required.

## Relations to nearby lessons

This lesson builds on **Modal orthogonality and normalization** and prepares for **Experimental modal analysis**. These connections matter because the motion predicted in one lesson becomes a forcing input or boundary condition in another. The algebra may look similar while the physical question changes: free response is not forced response, absolute displacement is not relative travel, and a modal natural frequency is not necessarily the frequency of peak operational vibration. Carry definitions of coordinates, units and assumptions forward; do not carry numerical values forward without checking whether the system has changed.

## Guided exercises and assessment

1. **Derivation:** Starting with a labeled free-body diagram or energy balance, derive or explain the screening relationship in this lesson. Show units and confirm at least one limiting case.
2. **Numerical sensitivity:** Recalculate the illustrative case with a 10% change in the parameter most likely to vary in service. Compare the relative change in output with the input change. State whether a linear approximation is justified.
3. **Measurement plan:** For “A tall support frame vibrates in bending and rocking under an eccentric motor.”, choose sensor positions and quantities to measure, and specify a sampling or repeatability requirement. What observation would contradict the simple model?
4. **Model criticism:** Explain exactly why the following warning could overturn a proposed selection: Truncated models can miss local stress and high-frequency acceleration even if global displacement is accurate.
5. **Design trade-off:** Compare two possible interventions, one changing inertia or stiffness and the other changing damping or forcing. Explain which practical requirement each intervention might worsen.
6. **Technical communication:** Write a short decision record separating a model-based prediction, an independent measurement, and a required acceptance condition. Explicitly label any unavailable evidence.

**Self-check:** Explain your result in physical words before looking again at the equation. If its magnitude or trend would surprise an engineer watching the mechanism move, review its coordinate, unit conversions, excitation type and validity limits. Do not use any draft value as an equipment setting without a complete review.


---

# U05-L05 — Experimental modal analysis

**OpenSTEM Mechanical Engineering / Book 09 / Mechanical Vibrations**  
*Unit 5: Multi-Degree-of-Freedom Vibrations and Modal Analysis | Unreviewed university-level educational manuscript.*

## Learning objectives

After this lesson, you should be able to (1) construct a defensible simplified model of **experimental modal analysis**, (2) explain the cause-and-effect relationship between its parameters and the observable output, (3) reproduce the quantitative screening example without losing units, (4) identify a realistic failure of the model, and (5) propose a repeatable experiment or sensor strategy. The lesson is intentionally written around a physical decision, not merely a formula to memorize.

## Physical setting and mechanisms

Impact or shaker testing estimates modal frequencies, damping and shapes with controlled force and response measurements.

**Running example.** An aluminum cantilever with sensor mass produces a measured frequency lower than predicted. Start by naming what is *moving*, what imposes the *excitation*, and what establishes the motion reference. A support can be treated as fixed only if its motion is negligible over the frequency range of interest; if a floor, table, shaft or gearbox housing moves, it becomes part of the system. In particular, a displacement reported in millimeters can be either motion in an inertial frame or the difference between two moving points. The two quantities lead to different interpretations of isolation performance and dynamic stress.

A vibration model begins with inertia and a mechanism that transfers forces or energy. Inertia resists acceleration, elastic stiffness supplies a position-dependent restoring force, and mechanical damping removes energy through irreversible processes. A machine may also have forcing from unbalance, pressure pulses, electromagnetic torque, gear contact, road or floor input, or deliberate actuation. Do not include all these effects by default. Begin by isolating the mechanism suggested by the observed response, then test whether omitted effects matter at the operating point. If a linear model cannot reproduce amplitude, phase and frequency dependence together, the disagreement may identify additional physics, rather than an arithmetic problem.

The central interpretive question is not whether an equation has been solved, but whether its dependent variable corresponds to the requested decision. A natural frequency does not alone tell how large the motion will be; frequency of forcing and damping matter as well. Likewise, a reduction in displacement can coincide with a rise in acceleration if the frequency has changed. When comparing candidates, state whether you are minimizing motion, transmitted force, stress, sound, instrument error, fatigue or some weighted combination of those outcomes. These design objectives can conflict.

## Equation and derivation strategy

**Screening calculation:** Frequency relative error=(f_meas-f_model)/f_model; for 47 Hz vs 50 Hz, error=-6%.

To reproduce this calculation, first sketch a free-body diagram with a positive coordinate direction, then write the force or energy balance. Next substitute numerical inputs with units attached. Convert between frequency in hertz and angular frequency only through ω=2πf; convert rpm to Hz through f=rpm/60 for one event per revolution. Decide whether an amplitude is peak, peak-to-peak or RMS and maintain that convention throughout. Unless the input is a clean harmonic, conversions such as a_peak=ω²X_peak or v_RMS=v_peak/sqrt(2) should not be applied blindly. Where a model assumes a single mode or one-dimensional motion, describe the coordinate that stands in for the true three-dimensional structure.

A useful consistency check is to alter one parameter before making the final decision. Increasing mass at fixed stiffness lowers the natural frequency; increasing stiffness at fixed mass raises it. Damping generally decreases resonant amplification but can increase high-frequency force transmission. Increasing harmonic forcing frequency changes the inertial contribution quadratically. These tendencies apply only within the model that produced them: changes in geometry, preload, temperature, amplitude or joint contact can change mass distribution or stiffness at the same time. A model can be dimensionally correct and still physically wrong because it predicts a quantity no sensor actually measures.

## Worked engineering interpretation

Return to the case: An aluminum cantilever with sensor mass produces a measured frequency lower than predicted. The screening result is useful for sizing a measurement range, identifying a suspected mode or testing whether an operating frequency overlaps a predicted response band. It is not a certification result. State the inputs you can actually measure, the ones you have merely assumed, and the likely interval of uncertainty. If two configurations differ by less than measurement variation, choosing the numerically better result is unjustified. For a machine with significant temperature changes, test cold and hot states; for a rotating machine, compare the speed sweep in both directions; for a flexible frame, check whether the fixture and mounting method influence the identified mode.

Introduce a second parameter set, changing one input by 10% while holding the others fixed. Predict the sign of the change before calculating. If the sign differs, identify whether the example crossed a resonance or a stability condition, used the wrong output definition, or violated the small-motion assumption. Record a baseline parameter table with source, unit, uncertainty and date. When the mathematical response is highly sensitive to a small change, refine the test plan before declaring that the first design works.

## Boundaries, failure diagnosis and safety

**Important limitation:** Added sensor mass, fixture flexibility, boundary conditions and signal-processing leakage can explain discrepancies. An industrial decision should not replace this qualification with a generic “allow a safety factor.” A factor cannot compensate for an incorrect vibration mode, unseen forcing order, missing contact state, defective sensor mounting or a wrong datum. If a simulation forecasts safe operation but measured vibration increases, stop escalating excitation and investigate the disagreement under controlled conditions. The responsibility to establish safe operating procedures, guards, machine access and acceptance limits belongs to qualified engineering personnel.

One way to diagnose discrepancy is to compare three distinct representations: a time trace, a spectrum or frequency-response curve, and a simple physical sketch of the expected motion. The time trace reveals clipping, impulses, drifting offsets and intermittent contact. The spectrum identifies periodic orders and broadband content but loses much time-localized information. The sketch tests whether the sensor direction can observe the hypothesized mode. A well-fitted numerical peak cannot establish a mechanism if the proposed mode shape is incompatible with the structure.

For measurement, **Use multiple impact points and document fixtures, sensors and mass loading.** Measure more than once under a documented load and speed; preserve settings and raw traces. A single amplitude without its frequency band, operating state, transducer orientation and convention is inadequate for comparison. Report model residuals where possible, and identify one datum that could prove the model false. The most useful conclusion may be that a simplified model is insufficient and a more complete test is required.

## Relations to nearby lessons

This lesson builds on **Modal superposition** and prepares for **the unit capstone**. These connections matter because the motion predicted in one lesson becomes a forcing input or boundary condition in another. The algebra may look similar while the physical question changes: free response is not forced response, absolute displacement is not relative travel, and a modal natural frequency is not necessarily the frequency of peak operational vibration. Carry definitions of coordinates, units and assumptions forward; do not carry numerical values forward without checking whether the system has changed.

## Guided exercises and assessment

1. **Derivation:** Starting with a labeled free-body diagram or energy balance, derive or explain the screening relationship in this lesson. Show units and confirm at least one limiting case.
2. **Numerical sensitivity:** Recalculate the illustrative case with a 10% change in the parameter most likely to vary in service. Compare the relative change in output with the input change. State whether a linear approximation is justified.
3. **Measurement plan:** For “An aluminum cantilever with sensor mass produces a measured frequency lower than predicted.”, choose sensor positions and quantities to measure, and specify a sampling or repeatability requirement. What observation would contradict the simple model?
4. **Model criticism:** Explain exactly why the following warning could overturn a proposed selection: Added sensor mass, fixture flexibility, boundary conditions and signal-processing leakage can explain discrepancies.
5. **Design trade-off:** Compare two possible interventions, one changing inertia or stiffness and the other changing damping or forcing. Explain which practical requirement each intervention might worsen.
6. **Technical communication:** Write a short decision record separating a model-based prediction, an independent measurement, and a required acceptance condition. Explicitly label any unavailable evidence.

**Self-check:** Explain your result in physical words before looking again at the equation. If its magnitude or trend would surprise an engineer watching the mechanism move, review its coordinate, unit conversions, excitation type and validity limits. Do not use any draft value as an equipment setting without a complete review.


---

