# Unit 08: Reliability, Economics and Responsible Plant Design

**Course Code**: PPE 308 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Reliability, Economics and Responsible Plant Design**.

# Unit 08, Lesson 01 — Failure modes and maintenance planning

**Core topic:** repair time and outage exposure. **Representative relation:** `Availability = MTBF/(MTBF+MTTR)`. **Case context:** unit maintenance register.

The central question in this lesson is how to evaluate **repair time and outage exposure** when the engineer is given measurements from **unit maintenance register**. First decide what quantity the result is supposed to describe. A thermodynamic component may have a local performance metric, while the whole plant has different inputs, outputs, auxiliaries and losses. Naming the metric prevents an apparently precise equation from addressing the wrong question. The representative relation is `Availability = MTBF/(MTBF+MTTR)`. This expression is a teaching starting point, not a complete design specification. Before putting values into it, define every term, identify the device boundary, and write its units. Where a symbol can have multiple interpretations, the label on the measurement sheet must be explicit.

### 1. Physical interpretation and scope

The phenomenon in focus is **repair time and outage exposure**. In a utility selecting between refurbishment, capacity expansion and replacement with a different technology mix, a measured value will depend on the actual arrangement of equipment, the time interval over which it is averaged and the physical states entering each component. If an engineer isolates unit maintenance register, the analysis should start by drawing arrows for all relevant energy or material streams and recording their directions. The next question is which measurements are direct and which come from a calculated property, manufacturer map, inferred coefficient or operational assumption. This distinction is more consequential than the number of decimal places in a spreadsheet.

A conservation equation and a constitutive relation serve different roles. Conservation says what the flows must sum to; a heat-transfer coefficient, turbomachinery efficiency, combustion model or empirical performance map helps explain how the flows divide in a specific design. When the calculation requires an unmeasured coefficient, report an explicit assumed range rather than disguising it as an observed constant. A reliable answer reports the sign of work and heat, the unit system and why a steady-state approximation is reasonable—or why it may be inadequate.

### 2. Derivation and use of the central relation

Begin with `Availability = MTBF/(MTBF+MTTR)` and identify the physical quantity on each side. A useful calculation is dimensionally self-consistent: for example MW equals MJ/s, mass flow in kg/s times a specific energy in kJ/kg produces kW, and the ratio of energies or rates is dimensionless only when numerator and denominator use comparable bases. Temperatures added in a balance can be Celsius differences; temperatures divided in ideal-gas or second-law relations must use kelvin. Pressure ratios use absolute pressure; a gauge-pressure reading must be converted before use in a physical ratio.

For repair time and outage exposure, specify whether the result assumes constant properties, negligible kinetic-energy changes, no stored-energy rate, or a fixed device efficiency. Each of these is an engineering hypothesis that can be tested or relaxed. When working from field data, reduce readings in the order: raw instrument value, calibrated engineering unit, time alignment, derived state quantity, physical balance, performance ratio. This audit trail allows a second engineer to repeat the estimate.

A special caution in this lesson is that **scheduled and forced outages have different definitions**. Explain exactly which algebraic term or measurement would be affected by that mistake. For a model with several serial components, a plausible local estimate may still be incompatible with the surrounding plant energy balance. Reconcile the result against the larger system. A model that demands more energy at the outlet than enters without storage, external work or a defined additional source should be rejected rather than patched by an unexplained correction factor.

### 3. Applied worked example — Failure modes and maintenance planning

In a simplified alternating failure-repair model, MTBF is 5000 h and mean repair time is 100 h. Operational availability is 5000/(5000 + 100) = **98.04%**. Planned maintenance, derated operation and common-cause failures are outside this two-number expression.

**Verification and limitations.** Annual capacity factor is not the same quantity as availability. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.

### 7. Exercises and discussion

1. **Derive.** Start from an explicit control volume for unit maintenance register. Derive `Availability = MTBF/(MTBF+MTTR)` or identify its idealizing assumptions. Label every term and check dimensional homogeneity.
2. **Calculate.** Construct an internally consistent SI example for repair time and outage exposure using values from a standard property table or clearly declared synthetic inputs. Calculate the nominal result and an output range when the dominant uncertain input is perturbed by ±5%.
3. **Diagnose.** A team reports an unexpected improvement while its fuel, electricity or fluid meters are undergoing maintenance. Form two measurement-error hypotheses and one physical-process hypothesis, then identify evidence that would discriminate among them.
4. **Compare.** Evaluate whether overly optimistic repair estimates bias expected energy. Discuss at least one benefit, one new risk and a plant-level quantity that may offset the local benefit.
5. **Communicate.** Write a one-page engineering note distinguishing your numerical result, its assumptions, the source of each input, and the actions that require external professional review.

**Answer-check guidance.** A defensible solution shows its boundary, substitutions and units, not just the final numerical value. For a ±5% sensitivity, recompute the original equation at both input limits rather than automatically declaring the output to have the same percentage uncertainty. For evidence questions, name the actual sensor or log to examine and the expected sign of each competing effect. Qualitative trade-offs need a stated criterion—net export, fuel use, water, safety margin or total cost—rather than a vague ranking.

### 8. Research extension

Design a small, reproducible computational experiment about repair time and outage exposure. Define a physically reasonable input range and record why the range was chosen; collect a baseline output; sweep one independent variable; and export the results with units and assumptions. Explain where the educational calculator in this book is too simple for the proposed study. Contrast its output with published technology characterizations or a documented manufacturer's map *without copying proprietary material*. Include a limitations paragraph on extrapolation, scale effects and evidence quality. A negative finding, such as failure to improve net plant performance despite an attractive component calculation, is a valid outcome when the assumptions are clear.


---

# Unit 08, Lesson 02 — Capacity credit and reserve planning

**Core topic:** reliability versus output statistics. **Representative relation:** `E_expected = P_rated*CF*8760`. **Case context:** high-demand-week planning scenario.

The central question in this lesson is how to evaluate **reliability versus output statistics** when the engineer is given measurements from **high-demand-week planning scenario**. First decide what quantity the result is supposed to describe. A thermodynamic component may have a local performance metric, while the whole plant has different inputs, outputs, auxiliaries and losses. Naming the metric prevents an apparently precise equation from addressing the wrong question. The representative relation is `E_expected = P_rated*CF*8760`. This expression is a teaching starting point, not a complete design specification. Before putting values into it, define every term, identify the device boundary, and write its units. Where a symbol can have multiple interpretations, the label on the measurement sheet must be explicit.

### 1. Physical interpretation and scope

The phenomenon in focus is **reliability versus output statistics**. In a utility selecting between refurbishment, capacity expansion and replacement with a different technology mix, a measured value will depend on the actual arrangement of equipment, the time interval over which it is averaged and the physical states entering each component. If an engineer isolates high-demand-week planning scenario, the analysis should start by drawing arrows for all relevant energy or material streams and recording their directions. The next question is which measurements are direct and which come from a calculated property, manufacturer map, inferred coefficient or operational assumption. This distinction is more consequential than the number of decimal places in a spreadsheet.

A conservation equation and a constitutive relation serve different roles. Conservation says what the flows must sum to; a heat-transfer coefficient, turbomachinery efficiency, combustion model or empirical performance map helps explain how the flows divide in a specific design. When the calculation requires an unmeasured coefficient, report an explicit assumed range rather than disguising it as an observed constant. A reliable answer reports the sign of work and heat, the unit system and why a steady-state approximation is reasonable—or why it may be inadequate.

### 2. Derivation and use of the central relation

Begin with `E_expected = P_rated*CF*8760` and identify the physical quantity on each side. A useful calculation is dimensionally self-consistent: for example MW equals MJ/s, mass flow in kg/s times a specific energy in kJ/kg produces kW, and the ratio of energies or rates is dimensionless only when numerator and denominator use comparable bases. Temperatures added in a balance can be Celsius differences; temperatures divided in ideal-gas or second-law relations must use kelvin. Pressure ratios use absolute pressure; a gauge-pressure reading must be converted before use in a physical ratio.

For reliability versus output statistics, specify whether the result assumes constant properties, negligible kinetic-energy changes, no stored-energy rate, or a fixed device efficiency. Each of these is an engineering hypothesis that can be tested or relaxed. When working from field data, reduce readings in the order: raw instrument value, calibrated engineering unit, time alignment, derived state quantity, physical balance, performance ratio. This audit trail allows a second engineer to repeat the estimate.

A special caution in this lesson is that **capacity factor alone does not establish capacity credit**. Explain exactly which algebraic term or measurement would be affected by that mistake. For a model with several serial components, a plausible local estimate may still be incompatible with the surrounding plant energy balance. Reconcile the result against the larger system. A model that demands more energy at the outlet than enters without storage, external work or a defined additional source should be rejected rather than patched by an unexplained correction factor.

### 3. Applied worked example — Capacity credit and reserve planning

A 100 MW net-rated generator serves peaking demand and has annual capacity factor 25%. Its annual energy is 100 × 0.25 × 8760 = **219,000 MWh**. This output alone says nothing about the value of its availability during the 50 highest-price or highest-stress hours.

**Verification and limitations.** Capacity credit depends on system need and the probability of resource availability at critical times. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.

### 7. Exercises and discussion

1. **Derive.** Start from an explicit control volume for high-demand-week planning scenario. Derive `E_expected = P_rated*CF*8760` or identify its idealizing assumptions. Label every term and check dimensional homogeneity.
2. **Calculate.** Construct an internally consistent SI example for reliability versus output statistics using values from a standard property table or clearly declared synthetic inputs. Calculate the nominal result and an output range when the dominant uncertain input is perturbed by ±5%.
3. **Diagnose.** A team reports an unexpected improvement while its fuel, electricity or fluid meters are undergoing maintenance. Form two measurement-error hypotheses and one physical-process hypothesis, then identify evidence that would discriminate among them.
4. **Compare.** Evaluate whether a variable source may produce annual energy but little during a specific critical hour. Discuss at least one benefit, one new risk and a plant-level quantity that may offset the local benefit.
5. **Communicate.** Write a one-page engineering note distinguishing your numerical result, its assumptions, the source of each input, and the actions that require external professional review.

**Answer-check guidance.** A defensible solution shows its boundary, substitutions and units, not just the final numerical value. For a ±5% sensitivity, recompute the original equation at both input limits rather than automatically declaring the output to have the same percentage uncertainty. For evidence questions, name the actual sensor or log to examine and the expected sign of each competing effect. Qualitative trade-offs need a stated criterion—net export, fuel use, water, safety margin or total cost—rather than a vague ranking.

### 8. Research extension

Design a small, reproducible computational experiment about reliability versus output statistics. Define a physically reasonable input range and record why the range was chosen; collect a baseline output; sweep one independent variable; and export the results with units and assumptions. Explain where the educational calculator in this book is too simple for the proposed study. Contrast its output with published technology characterizations or a documented manufacturer's map *without copying proprietary material*. Include a limitations paragraph on extrapolation, scale effects and evidence quality. A negative finding, such as failure to improve net plant performance despite an attractive component calculation, is a valid outcome when the assumptions are clear.


---

# Unit 08, Lesson 03 — Simple levelized energy cost

**Core topic:** cost per delivered MWh. **Representative relation:** `LCOE = annual_total_cost/E_year`. **Case context:** annualized capital and operation-cost worksheet.

The central question in this lesson is how to evaluate **cost per delivered MWh** when the engineer is given measurements from **annualized capital and operation-cost worksheet**. First decide what quantity the result is supposed to describe. A thermodynamic component may have a local performance metric, while the whole plant has different inputs, outputs, auxiliaries and losses. Naming the metric prevents an apparently precise equation from addressing the wrong question. The representative relation is `LCOE = annual_total_cost/E_year`. This expression is a teaching starting point, not a complete design specification. Before putting values into it, define every term, identify the device boundary, and write its units. Where a symbol can have multiple interpretations, the label on the measurement sheet must be explicit.

### 1. Physical interpretation and scope

The phenomenon in focus is **cost per delivered MWh**. In a utility selecting between refurbishment, capacity expansion and replacement with a different technology mix, a measured value will depend on the actual arrangement of equipment, the time interval over which it is averaged and the physical states entering each component. If an engineer isolates annualized capital and operation-cost worksheet, the analysis should start by drawing arrows for all relevant energy or material streams and recording their directions. The next question is which measurements are direct and which come from a calculated property, manufacturer map, inferred coefficient or operational assumption. This distinction is more consequential than the number of decimal places in a spreadsheet.

A conservation equation and a constitutive relation serve different roles. Conservation says what the flows must sum to; a heat-transfer coefficient, turbomachinery efficiency, combustion model or empirical performance map helps explain how the flows divide in a specific design. When the calculation requires an unmeasured coefficient, report an explicit assumed range rather than disguising it as an observed constant. A reliable answer reports the sign of work and heat, the unit system and why a steady-state approximation is reasonable—or why it may be inadequate.

### 2. Derivation and use of the central relation

Begin with `LCOE = annual_total_cost/E_year` and identify the physical quantity on each side. A useful calculation is dimensionally self-consistent: for example MW equals MJ/s, mass flow in kg/s times a specific energy in kJ/kg produces kW, and the ratio of energies or rates is dimensionless only when numerator and denominator use comparable bases. Temperatures added in a balance can be Celsius differences; temperatures divided in ideal-gas or second-law relations must use kelvin. Pressure ratios use absolute pressure; a gauge-pressure reading must be converted before use in a physical ratio.

For cost per delivered MWh, specify whether the result assumes constant properties, negligible kinetic-energy changes, no stored-energy rate, or a fixed device efficiency. Each of these is an engineering hypothesis that can be tested or relaxed. When working from field data, reduce readings in the order: raw instrument value, calibrated engineering unit, time alignment, derived state quantity, physical balance, performance ratio. This audit trail allows a second engineer to repeat the estimate.

A special caution in this lesson is that **financial discounting and real-versus-nominal values require explicit treatment**. Explain exactly which algebraic term or measurement would be affected by that mistake. For a model with several serial components, a plausible local estimate may still be incompatible with the surrounding plant energy balance. Reconcile the result against the larger system. A model that demands more energy at the outlet than enters without storage, external work or a defined additional source should be rejected rather than patched by an unexplained correction factor.

### 3. Applied worked example — Simple levelized energy cost

A project reports annualized fixed, fuel and operations cost totaling 40 million dollars and expected delivered annual energy of 800,000 MWh. Its simplified cost is $40,000,000/800,000 = **$50/MWh**. The figure is not a complete financed project LCOE unless the capital annualization, taxes, financing and other assumptions have been specified.

**Verification and limitations.** A cheaper mean $/MWh may still fail to supply capacity, flexibility or the required environmental service. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.

### 7. Exercises and discussion

1. **Derive.** Start from an explicit control volume for annualized capital and operation-cost worksheet. Derive `LCOE = annual_total_cost/E_year` or identify its idealizing assumptions. Label every term and check dimensional homogeneity.
2. **Calculate.** Construct an internally consistent SI example for cost per delivered MWh using values from a standard property table or clearly declared synthetic inputs. Calculate the nominal result and an output range when the dominant uncertain input is perturbed by ±5%.
3. **Diagnose.** A team reports an unexpected improvement while its fuel, electricity or fluid meters are undergoing maintenance. Form two measurement-error hypotheses and one physical-process hypothesis, then identify evidence that would discriminate among them.
4. **Compare.** Evaluate whether low LCOE does not certify reliability or environmental acceptability. Discuss at least one benefit, one new risk and a plant-level quantity that may offset the local benefit.
5. **Communicate.** Write a one-page engineering note distinguishing your numerical result, its assumptions, the source of each input, and the actions that require external professional review.

**Answer-check guidance.** A defensible solution shows its boundary, substitutions and units, not just the final numerical value. For a ±5% sensitivity, recompute the original equation at both input limits rather than automatically declaring the output to have the same percentage uncertainty. For evidence questions, name the actual sensor or log to examine and the expected sign of each competing effect. Qualitative trade-offs need a stated criterion—net export, fuel use, water, safety margin or total cost—rather than a vague ranking.

### 8. Research extension

Design a small, reproducible computational experiment about cost per delivered MWh. Define a physically reasonable input range and record why the range was chosen; collect a baseline output; sweep one independent variable; and export the results with units and assumptions. Explain where the educational calculator in this book is too simple for the proposed study. Contrast its output with published technology characterizations or a documented manufacturer's map *without copying proprietary material*. Include a limitations paragraph on extrapolation, scale effects and evidence quality. A negative finding, such as failure to improve net plant performance despite an attractive component calculation, is a valid outcome when the assumptions are clear.


---

# Unit 08, Lesson 04 — Lifecycle impacts and uncertainty

**Core topic:** consistent lifecycle normalization. **Representative relation:** `I_CO2 = m_CO2_lifecycle/E_lifetime`. **Case context:** replacement versus refurbishment comparison.

The central question in this lesson is how to evaluate **consistent lifecycle normalization** when the engineer is given measurements from **replacement versus refurbishment comparison**. First decide what quantity the result is supposed to describe. A thermodynamic component may have a local performance metric, while the whole plant has different inputs, outputs, auxiliaries and losses. Naming the metric prevents an apparently precise equation from addressing the wrong question. The representative relation is `I_CO2 = m_CO2_lifecycle/E_lifetime`. This expression is a teaching starting point, not a complete design specification. Before putting values into it, define every term, identify the device boundary, and write its units. Where a symbol can have multiple interpretations, the label on the measurement sheet must be explicit.

### 1. Physical interpretation and scope

The phenomenon in focus is **consistent lifecycle normalization**. In a utility selecting between refurbishment, capacity expansion and replacement with a different technology mix, a measured value will depend on the actual arrangement of equipment, the time interval over which it is averaged and the physical states entering each component. If an engineer isolates replacement versus refurbishment comparison, the analysis should start by drawing arrows for all relevant energy or material streams and recording their directions. The next question is which measurements are direct and which come from a calculated property, manufacturer map, inferred coefficient or operational assumption. This distinction is more consequential than the number of decimal places in a spreadsheet.

A conservation equation and a constitutive relation serve different roles. Conservation says what the flows must sum to; a heat-transfer coefficient, turbomachinery efficiency, combustion model or empirical performance map helps explain how the flows divide in a specific design. When the calculation requires an unmeasured coefficient, report an explicit assumed range rather than disguising it as an observed constant. A reliable answer reports the sign of work and heat, the unit system and why a steady-state approximation is reasonable—or why it may be inadequate.

### 2. Derivation and use of the central relation

Begin with `I_CO2 = m_CO2_lifecycle/E_lifetime` and identify the physical quantity on each side. A useful calculation is dimensionally self-consistent: for example MW equals MJ/s, mass flow in kg/s times a specific energy in kJ/kg produces kW, and the ratio of energies or rates is dimensionless only when numerator and denominator use comparable bases. Temperatures added in a balance can be Celsius differences; temperatures divided in ideal-gas or second-law relations must use kelvin. Pressure ratios use absolute pressure; a gauge-pressure reading must be converted before use in a physical ratio.

For consistent lifecycle normalization, specify whether the result assumes constant properties, negligible kinetic-energy changes, no stored-energy rate, or a fixed device efficiency. Each of these is an engineering hypothesis that can be tested or relaxed. When working from field data, reduce readings in the order: raw instrument value, calibrated engineering unit, time alignment, derived state quantity, physical balance, performance ratio. This audit trail allows a second engineer to repeat the estimate.

A special caution in this lesson is that **system boundaries and allocation choices affect results**. Explain exactly which algebraic term or measurement would be affected by that mistake. For a model with several serial components, a plausible local estimate may still be incompatible with the surrounding plant energy balance. Reconcile the result against the larger system. A model that demands more energy at the outlet than enters without storage, external work or a defined additional source should be rejected rather than patched by an unexplained correction factor.

### 3. Applied worked example — Lifecycle impacts and uncertainty

A lifecycle inventory attributes 400,000 tonnes of CO2-equivalent to a project, and lifetime net energy delivery is 5,000,000 MWh. The intensity is 400,000/5,000,000 = **0.08 t CO2e/MWh**, or 80 kg/MWh. Changes to the boundary—construction, fuel supply, or end-of-life—change the result.

**Verification and limitations.** Uncertainty and allocation choices should be visible rather than hidden in one exact-looking number. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.

### 7. Exercises and discussion

1. **Derive.** Start from an explicit control volume for replacement versus refurbishment comparison. Derive `I_CO2 = m_CO2_lifecycle/E_lifetime` or identify its idealizing assumptions. Label every term and check dimensional homogeneity.
2. **Calculate.** Construct an internally consistent SI example for consistent lifecycle normalization using values from a standard property table or clearly declared synthetic inputs. Calculate the nominal result and an output range when the dominant uncertain input is perturbed by ±5%.
3. **Diagnose.** A team reports an unexpected improvement while its fuel, electricity or fluid meters are undergoing maintenance. Form two measurement-error hypotheses and one physical-process hypothesis, then identify evidence that would discriminate among them.
4. **Compare.** Evaluate whether a point estimate without sensitivity is weak evidence. Discuss at least one benefit, one new risk and a plant-level quantity that may offset the local benefit.
5. **Communicate.** Write a one-page engineering note distinguishing your numerical result, its assumptions, the source of each input, and the actions that require external professional review.

**Answer-check guidance.** A defensible solution shows its boundary, substitutions and units, not just the final numerical value. For a ±5% sensitivity, recompute the original equation at both input limits rather than automatically declaring the output to have the same percentage uncertainty. For evidence questions, name the actual sensor or log to examine and the expected sign of each competing effect. Qualitative trade-offs need a stated criterion—net export, fuel use, water, safety margin or total cost—rather than a vague ranking.

### 8. Research extension

Design a small, reproducible computational experiment about consistent lifecycle normalization. Define a physically reasonable input range and record why the range was chosen; collect a baseline output; sweep one independent variable; and export the results with units and assumptions. Explain where the educational calculator in this book is too simple for the proposed study. Contrast its output with published technology characterizations or a documented manufacturer's map *without copying proprietary material*. Include a limitations paragraph on extrapolation, scale effects and evidence quality. A negative finding, such as failure to improve net plant performance despite an attractive component calculation, is a valid outcome when the assumptions are clear.


---

# Unit 08, Lesson 05 — Capstone integrated plant evaluation

**Core topic:** closing energy and decision accounts. **Representative relation:** `Residual_energy = Q_in-P_e-Q_reject-Q_other`. **Case context:** conceptual comparison of three plant options.

The central question in this lesson is how to evaluate **closing energy and decision accounts** when the engineer is given measurements from **conceptual comparison of three plant options**. First decide what quantity the result is supposed to describe. A thermodynamic component may have a local performance metric, while the whole plant has different inputs, outputs, auxiliaries and losses. Naming the metric prevents an apparently precise equation from addressing the wrong question. The representative relation is `Residual_energy = Q_in-P_e-Q_reject-Q_other`. This expression is a teaching starting point, not a complete design specification. Before putting values into it, define every term, identify the device boundary, and write its units. Where a symbol can have multiple interpretations, the label on the measurement sheet must be explicit.

### 1. Physical interpretation and scope

The phenomenon in focus is **closing energy and decision accounts**. In a utility selecting between refurbishment, capacity expansion and replacement with a different technology mix, a measured value will depend on the actual arrangement of equipment, the time interval over which it is averaged and the physical states entering each component. If an engineer isolates conceptual comparison of three plant options, the analysis should start by drawing arrows for all relevant energy or material streams and recording their directions. The next question is which measurements are direct and which come from a calculated property, manufacturer map, inferred coefficient or operational assumption. This distinction is more consequential than the number of decimal places in a spreadsheet.

A conservation equation and a constitutive relation serve different roles. Conservation says what the flows must sum to; a heat-transfer coefficient, turbomachinery efficiency, combustion model or empirical performance map helps explain how the flows divide in a specific design. When the calculation requires an unmeasured coefficient, report an explicit assumed range rather than disguising it as an observed constant. A reliable answer reports the sign of work and heat, the unit system and why a steady-state approximation is reasonable—or why it may be inadequate.

### 2. Derivation and use of the central relation

Begin with `Residual_energy = Q_in-P_e-Q_reject-Q_other` and identify the physical quantity on each side. A useful calculation is dimensionally self-consistent: for example MW equals MJ/s, mass flow in kg/s times a specific energy in kJ/kg produces kW, and the ratio of energies or rates is dimensionless only when numerator and denominator use comparable bases. Temperatures added in a balance can be Celsius differences; temperatures divided in ideal-gas or second-law relations must use kelvin. Pressure ratios use absolute pressure; a gauge-pressure reading must be converted before use in a physical ratio.

For closing energy and decision accounts, specify whether the result assumes constant properties, negligible kinetic-energy changes, no stored-energy rate, or a fixed device efficiency. Each of these is an engineering hypothesis that can be tested or relaxed. When working from field data, reduce readings in the order: raw instrument value, calibrated engineering unit, time alignment, derived state quantity, physical balance, performance ratio. This audit trail allows a second engineer to repeat the estimate.

A special caution in this lesson is that **uncertainty, safety and permitting belong in the final recommendation**. Explain exactly which algebraic term or measurement would be affected by that mistake. For a model with several serial components, a plausible local estimate may still be incompatible with the surrounding plant energy balance. Reconcile the result against the larger system. A model that demands more energy at the outlet than enters without storage, external work or a defined additional source should be rejected rather than patched by an unexplained correction factor.

### 3. Applied worked example — Capstone integrated plant evaluation

A conceptual plant receives 400 MW(th), exports 155 MW(e), rejects 210 MW(th) through cooling, and has 25 MW(th) of other quantified losses. The unclosed energy residual is 400 − 155 − 210 − 25 = **10 MW(th)**. The analyst must investigate this residual as possible unmeasured loss, stored-energy change, or measurement error; it must not silently disappear.

**Verification and limitations.** A closed spreadsheet is not sufficient evidence of plant safety, emissions compliance or economic viability. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.

### 7. Exercises and discussion

1. **Derive.** Start from an explicit control volume for conceptual comparison of three plant options. Derive `Residual_energy = Q_in-P_e-Q_reject-Q_other` or identify its idealizing assumptions. Label every term and check dimensional homogeneity.
2. **Calculate.** Construct an internally consistent SI example for closing energy and decision accounts using values from a standard property table or clearly declared synthetic inputs. Calculate the nominal result and an output range when the dominant uncertain input is perturbed by ±5%.
3. **Diagnose.** A team reports an unexpected improvement while its fuel, electricity or fluid meters are undergoing maintenance. Form two measurement-error hypotheses and one physical-process hypothesis, then identify evidence that would discriminate among them.
4. **Compare.** Evaluate whether reject solutions that achieve apparent efficiency by omitting loss streams. Discuss at least one benefit, one new risk and a plant-level quantity that may offset the local benefit.
5. **Communicate.** Write a one-page engineering note distinguishing your numerical result, its assumptions, the source of each input, and the actions that require external professional review.

**Answer-check guidance.** A defensible solution shows its boundary, substitutions and units, not just the final numerical value. For a ±5% sensitivity, recompute the original equation at both input limits rather than automatically declaring the output to have the same percentage uncertainty. For evidence questions, name the actual sensor or log to examine and the expected sign of each competing effect. Qualitative trade-offs need a stated criterion—net export, fuel use, water, safety margin or total cost—rather than a vague ranking.

### 8. Research extension

Design a small, reproducible computational experiment about closing energy and decision accounts. Define a physically reasonable input range and record why the range was chosen; collect a baseline output; sweep one independent variable; and export the results with units and assumptions. Explain where the educational calculator in this book is too simple for the proposed study. Contrast its output with published technology characterizations or a documented manufacturer's map *without copying proprietary material*. Include a limitations paragraph on extrapolation, scale effects and evidence quality. A negative finding, such as failure to improve net plant performance despite an attractive component calculation, is a valid outcome when the assumptions are clear.


---

