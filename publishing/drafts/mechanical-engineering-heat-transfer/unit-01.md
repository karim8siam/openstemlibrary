# Unit 01: Heat Transfer Foundations and Thermal Modeling

**Course Code**: HTR 201 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Heat Transfer Foundations and Thermal Modeling**.

# U01-L01 — Thermal energy and temperature

**Unit 1: Heat Transfer Foundations and Thermal Modeling · Suggested workload 90–130 minutes · Educational draft**

## Learning question and physical setting

**Guiding question:** Why can two objects have the same temperature but store different amounts of energy?

The central task in this lesson is not merely to insert values into a formula. It is to decide whether the formula represents the physical process, whether the thermal boundary is correctly located, and whether the resulting quantity can be compared to a measurement. The setting is concrete: A 1.4 kg aluminum block warms from 293 to 333 K with c=900 J/(kg K), requiring 50.4 kJ. Begin by explaining the physical mechanism in ordinary language before drawing a thermal diagram. Decide which direction energy is expected to move, and identify at least one quantity that changes if the surrounding temperature or operating power changes. This turns a numerical problem into a model that could be revised when new evidence appears.

## Conceptual foundations and governing relationship

**Core relationship:** `ΔU=mcΔT for constant c`.

A thermal balance requires a declaration of what belongs to the system and what crosses its surface. Electrical inputs, shaft work, mass transport and thermal transfer must not be combined casually. A temperature increase is evidence of internal energy storage only when material heat capacity and mass are properly represented. In actual instrumentation, an enclosure can receive heat from a nearby hotter object even if the room air is cool. Conversely, some heat may leave by several paths simultaneously. Describe each path before estimating a coefficient. The equation describes a particular kind of relation: sometimes a constitutive law, sometimes an integral energy balance, a nondimensional definition, a geometry-specific analytical solution, or a correlation validated only in an experimental range. Before using it, define each symbol and its units. State which values are measured, which are assumed, which are looked up, and which are inferred. Unlike an algebraic identity, a model may stop being valid when the shape, temperature distribution, flow regime, surface treatment or boundary conditions change. An answer that violates a conservation balance is unacceptable even if its arithmetic is flawless.

For **thermal energy and temperature**, sketch the physical domain and draw arrows for the relevant energy paths. A first approximation is useful when it makes the dominant mechanism visible. A more detailed approximation is useful only when an observation motivates the additional complexity. In each case, decide whether spatial temperature gradients are physically essential, whether heat is stored, and whether material properties can be treated as uniform. The goal is to preserve both insight and a traceable decision process.

## Guided numerical example: Block heating: ΔU=mcΔT

**Given synthetic inputs.** Mass 1.4 kg; c=900 J/(kg K); T rises from 293 to 333 K.

**Operation.** Use the relationship `Block heating: ΔU=mcΔT` with all inputs converted to compatible units; the result is **5.04e+04 J**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.

**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.

## Derivation map and assumptions

1. Draw a control volume or differential element. Mark every mechanism that carries energy across its boundary and each mechanism that stores or generates it.
2. Choose a coordinate and sign convention, identify a characteristic length, and state whether the requested answer concerns an area, a volume, a point temperature or an integrated rate.
3. Write the governing differential or integral balance. Separate physical conservation from constitutive assumptions, geometric identities and empirical correlations.
4. Simplify only after stating the neglected processes. Common simplifications include negligible contact resistance, uniform fluid properties, quasi-steady conduction or constant wall temperature; each has a plausible failure condition.
5. Substitute values with their dimensions retained. Evaluate a limiting case: zero driving difference, vanishing thickness, extremely low coefficient, large elapsed time or another mathematically relevant limit.
6. Examine whether the dependent quantity could be independently observed and whether the observed conditions would reproduce the assumptions used in the calculation.

For this topic, For this lesson, distinguish measured temperature from inferred energy transfer. Start a data sheet with a time stamp, location and uncertainty for every observation. Identify the heat input or loss path that a single thermometer cannot reveal. If thermal energy and temperature is approached by an electrical-power measurement, determine whether leads, supports or neighboring objects add hidden transfer. State whether the proposed system boundary encloses the source, the surrounding air and the insulation. Then repeat the balance after moving the boundary and check that the physical conclusion is unchanged.

## Engineering experiment and data interpretation

**Suggested investigation.** Measure the heating curve of metal and water samples supplied at comparable electrical power. Do not invent real measurements; start with an explicit hypothetical dataset or collect readings under appropriate supervision. Specify the sensor location, thermal settling criterion, and calibration state. Record environmental conditions, because an apparently small change in ambient temperature can alter both boundary gradients and material properties. Identify a control run that removes the driving source or changes only one variable. Repeat at least one operating point to estimate repeatability rather than treating an isolated reading as exact.

A defensible report includes an annotated sketch, a units table, the raw readings, a method for reducing data and a statement of what cannot be inferred. If an inverse calculation uses a model to estimate a coefficient, do not then use the very same data as independent validation. Reserve at least one different condition or instrument for a fair check. The student should be able to explain why a significant discrepancy may indicate an incorrect thermal boundary rather than a mistaken calculator operation.

## Model limits, troubleshooting and safety

**Frequent mistake:** Treating heat as a property stored inside a body rather than energy transferred across a boundary.

Diagnose the underlying reason instead of memorizing a warning. Ask what hidden assumption permits the easy formula to be written and what instrument would reveal its failure. A model may fail by incorrect dimensions, invalid regime, missing heat path, changing fluid property, an inappropriate temperature reference, or a neglected time-dependent term. Separate those failures from numerical mistakes and data-recording problems. Compare the predicted rate against any power or energy known to enter the system; a passive assembly cannot steadily deliver more energy than its stated supply without another source.

If the proposed object is a boiler, pressure vessel, battery pack, electrical appliance, medical device, industrial furnace or fire-safety system, this lesson supplies basic intuition only. Real design requires applicable codes, manufacturer data, validated correlations, abnormal-operation analysis and responsible professional review. The exploratory sliders in the companion models are not design certificates.

## Check your understanding — three problems

1. **Numerical variation.** Rework the example for a 15% increase in its driving thermal difference or equivalent controlling input. State the new units, compare changes as a percentage, and explain whether the relationship is truly linear at this point.
2. **Model selection.** Draw a different physical geometry or flow configuration where this equation might fail. Identify the precise assumption that breaks down, then propose a more suitable balance, correlation or measurement.
3. **Experimental critique.** Design a two-condition laboratory check of the guiding question. Specify a measurable dependent quantity, one plausible confounder, a calibration or repeatability step, and a criterion for recognizing a model–data disagreement.

## Extension: toward real engineering practice

Develop a small calculation sheet or script with named inputs, a units column and explicit warnings about any validity range. Test it at a nominal point and at two extremes, explaining whether the mathematics remains physically credible. Then imagine a colleague changed an input property without documenting temperature or source. Describe exactly how that would affect traceability and how you would reconstruct the decision. Finally propose one material, configuration or instrumentation change that improves thermal performance without adding unacceptable complexity or operating expense.

**Lesson conclusion.** Thermal energy and temperature is useful when the energy pathway, geometry, regime and measurement basis agree. Recalculate when those conditions change; do not use apparent precision to hide uncertainty. Explain the result using a physical picture, not only a number.


---

# U01-L02 — Conduction, convection, and radiation

**Unit 1: Heat Transfer Foundations and Thermal Modeling · Suggested workload 90–130 minutes · Educational draft**

## Learning question and physical setting

**Guiding question:** Which thermal modes cross each boundary of an insulated electronics enclosure?

The central task in this lesson is not merely to insert values into a formula. It is to decide whether the formula represents the physical process, whether the thermal boundary is correctly located, and whether the resulting quantity can be compared to a measurement. The setting is concrete: A 12 W circuit board transfers heat by air convection and longwave radiation, while conducting heat through mounting posts. Begin by explaining the physical mechanism in ordinary language before drawing a thermal diagram. Decide which direction energy is expected to move, and identify at least one quantity that changes if the surrounding temperature or operating power changes. This turns a numerical problem into a model that could be revised when new evidence appears.

## Conceptual foundations and governing relationship

**Core relationship:** `q = −k∇T; q=hA(Ts−T∞); q=εσA(Ts⁴−Tsur⁴)`.

A thermal balance requires a declaration of what belongs to the system and what crosses its surface. Electrical inputs, shaft work, mass transport and thermal transfer must not be combined casually. A temperature increase is evidence of internal energy storage only when material heat capacity and mass are properly represented. In actual instrumentation, an enclosure can receive heat from a nearby hotter object even if the room air is cool. Conversely, some heat may leave by several paths simultaneously. Describe each path before estimating a coefficient. The equation describes a particular kind of relation: sometimes a constitutive law, sometimes an integral energy balance, a nondimensional definition, a geometry-specific analytical solution, or a correlation validated only in an experimental range. Before using it, define each symbol and its units. State which values are measured, which are assumed, which are looked up, and which are inferred. Unlike an algebraic identity, a model may stop being valid when the shape, temperature distribution, flow regime, surface treatment or boundary conditions change. An answer that violates a conservation balance is unacceptable even if its arithmetic is flawless.

For **conduction, convection, and radiation**, sketch the physical domain and draw arrows for the relevant energy paths. A first approximation is useful when it makes the dominant mechanism visible. A more detailed approximation is useful only when an observation motivates the additional complexity. In each case, decide whether spatial temperature gradients are physically essential, whether heat is stored, and whether material properties can be treated as uniform. The goal is to preserve both insight and a traceable decision process.

## Guided numerical example: Power partition: Qtotal=Qconv+Qrad

**Given synthetic inputs.** Convection 5 W; radiation 7 W; no other assumed paths.

**Operation.** Use the relationship `Power partition: Qtotal=Qconv+Qrad` with all inputs converted to compatible units; the result is **12 W**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.

**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.

## Derivation map and assumptions

1. Draw a control volume or differential element. Mark every mechanism that carries energy across its boundary and each mechanism that stores or generates it.
2. Choose a coordinate and sign convention, identify a characteristic length, and state whether the requested answer concerns an area, a volume, a point temperature or an integrated rate.
3. Write the governing differential or integral balance. Separate physical conservation from constitutive assumptions, geometric identities and empirical correlations.
4. Simplify only after stating the neglected processes. Common simplifications include negligible contact resistance, uniform fluid properties, quasi-steady conduction or constant wall temperature; each has a plausible failure condition.
5. Substitute values with their dimensions retained. Evaluate a limiting case: zero driving difference, vanishing thickness, extremely low coefficient, large elapsed time or another mathematically relevant limit.
6. Examine whether the dependent quantity could be independently observed and whether the observed conditions would reproduce the assumptions used in the calculation.

For this topic, For this lesson, distinguish measured temperature from inferred energy transfer. Start a data sheet with a time stamp, location and uncertainty for every observation. Identify the heat input or loss path that a single thermometer cannot reveal. If conduction, convection, and radiation is approached by an electrical-power measurement, determine whether leads, supports or neighboring objects add hidden transfer. State whether the proposed system boundary encloses the source, the surrounding air and the insulation. Then repeat the balance after moving the boundary and check that the physical conclusion is unchanged.

## Engineering experiment and data interpretation

**Suggested investigation.** Draw a mode-resolved thermal circuit for a powered enclosure and measure surface and ambient temperatures. Do not invent real measurements; start with an explicit hypothetical dataset or collect readings under appropriate supervision. Specify the sensor location, thermal settling criterion, and calibration state. Record environmental conditions, because an apparently small change in ambient temperature can alter both boundary gradients and material properties. Identify a control run that removes the driving source or changes only one variable. Repeat at least one operating point to estimate repeatability rather than treating an isolated reading as exact.

A defensible report includes an annotated sketch, a units table, the raw readings, a method for reducing data and a statement of what cannot be inferred. If an inverse calculation uses a model to estimate a coefficient, do not then use the very same data as independent validation. Reserve at least one different condition or instrument for a fair check. The student should be able to explain why a significant discrepancy may indicate an incorrect thermal boundary rather than a mistaken calculator operation.

## Model limits, troubleshooting and safety

**Frequent mistake:** Applying one heat-transfer coefficient to conduction, moving air, and radiative exchange without separating mechanisms.

Diagnose the underlying reason instead of memorizing a warning. Ask what hidden assumption permits the easy formula to be written and what instrument would reveal its failure. A model may fail by incorrect dimensions, invalid regime, missing heat path, changing fluid property, an inappropriate temperature reference, or a neglected time-dependent term. Separate those failures from numerical mistakes and data-recording problems. Compare the predicted rate against any power or energy known to enter the system; a passive assembly cannot steadily deliver more energy than its stated supply without another source.

If the proposed object is a boiler, pressure vessel, battery pack, electrical appliance, medical device, industrial furnace or fire-safety system, this lesson supplies basic intuition only. Real design requires applicable codes, manufacturer data, validated correlations, abnormal-operation analysis and responsible professional review. The exploratory sliders in the companion models are not design certificates.

## Check your understanding — three problems

1. **Numerical variation.** Rework the example for a 15% increase in its driving thermal difference or equivalent controlling input. State the new units, compare changes as a percentage, and explain whether the relationship is truly linear at this point.
2. **Model selection.** Draw a different physical geometry or flow configuration where this equation might fail. Identify the precise assumption that breaks down, then propose a more suitable balance, correlation or measurement.
3. **Experimental critique.** Design a two-condition laboratory check of the guiding question. Specify a measurable dependent quantity, one plausible confounder, a calibration or repeatability step, and a criterion for recognizing a model–data disagreement.

## Extension: toward real engineering practice

Develop a small calculation sheet or script with named inputs, a units column and explicit warnings about any validity range. Test it at a nominal point and at two extremes, explaining whether the mathematics remains physically credible. Then imagine a colleague changed an input property without documenting temperature or source. Describe exactly how that would affect traceability and how you would reconstruct the decision. Finally propose one material, configuration or instrumentation change that improves thermal performance without adding unacceptable complexity or operating expense.

**Lesson conclusion.** Conduction, convection, and radiation is useful when the energy pathway, geometry, regime and measurement basis agree. Recalculate when those conditions change; do not use apparent precision to hide uncertainty. Explain the result using a physical picture, not only a number.


---

# U01-L03 — Material properties and temperature dependence

**Unit 1: Heat Transfer Foundations and Thermal Modeling · Suggested workload 90–130 minutes · Educational draft**

## Learning question and physical setting

**Guiding question:** How do conductivity, density, and heat capacity shape transient response differently?

The central task in this lesson is not merely to insert values into a formula. It is to decide whether the formula represents the physical process, whether the thermal boundary is correctly located, and whether the resulting quantity can be compared to a measurement. The setting is concrete: Copper conducts quickly relative to many polymers; a polymer housing may still store significant energy despite low conductivity. Begin by explaining the physical mechanism in ordinary language before drawing a thermal diagram. Decide which direction energy is expected to move, and identify at least one quantity that changes if the surrounding temperature or operating power changes. This turns a numerical problem into a model that could be revised when new evidence appears.

## Conceptual foundations and governing relationship

**Core relationship:** `α=k/(ρcp)`.

A thermal balance requires a declaration of what belongs to the system and what crosses its surface. Electrical inputs, shaft work, mass transport and thermal transfer must not be combined casually. A temperature increase is evidence of internal energy storage only when material heat capacity and mass are properly represented. In actual instrumentation, an enclosure can receive heat from a nearby hotter object even if the room air is cool. Conversely, some heat may leave by several paths simultaneously. Describe each path before estimating a coefficient. The equation describes a particular kind of relation: sometimes a constitutive law, sometimes an integral energy balance, a nondimensional definition, a geometry-specific analytical solution, or a correlation validated only in an experimental range. Before using it, define each symbol and its units. State which values are measured, which are assumed, which are looked up, and which are inferred. Unlike an algebraic identity, a model may stop being valid when the shape, temperature distribution, flow regime, surface treatment or boundary conditions change. An answer that violates a conservation balance is unacceptable even if its arithmetic is flawless.

For **material properties and temperature dependence**, sketch the physical domain and draw arrows for the relevant energy paths. A first approximation is useful when it makes the dominant mechanism visible. A more detailed approximation is useful only when an observation motivates the additional complexity. In each case, decide whether spatial temperature gradients are physically essential, whether heat is stored, and whether material properties can be treated as uniform. The goal is to preserve both insight and a traceable decision process.

## Guided numerical example: Thermal diffusivity: α=k/(ρc)

**Given synthetic inputs.** k=200 W/(m K), ρ=2700 kg/m³, c=900 J/(kg K).

**Operation.** Use the relationship `Thermal diffusivity: α=k/(ρc)` with all inputs converted to compatible units; the result is **8.23e-05 m²/s**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.

**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.

## Derivation map and assumptions

1. Draw a control volume or differential element. Mark every mechanism that carries energy across its boundary and each mechanism that stores or generates it.
2. Choose a coordinate and sign convention, identify a characteristic length, and state whether the requested answer concerns an area, a volume, a point temperature or an integrated rate.
3. Write the governing differential or integral balance. Separate physical conservation from constitutive assumptions, geometric identities and empirical correlations.
4. Simplify only after stating the neglected processes. Common simplifications include negligible contact resistance, uniform fluid properties, quasi-steady conduction or constant wall temperature; each has a plausible failure condition.
5. Substitute values with their dimensions retained. Evaluate a limiting case: zero driving difference, vanishing thickness, extremely low coefficient, large elapsed time or another mathematically relevant limit.
6. Examine whether the dependent quantity could be independently observed and whether the observed conditions would reproduce the assumptions used in the calculation.

For this topic, For this lesson, distinguish measured temperature from inferred energy transfer. Start a data sheet with a time stamp, location and uncertainty for every observation. Identify the heat input or loss path that a single thermometer cannot reveal. If material properties and temperature dependence is approached by an electrical-power measurement, determine whether leads, supports or neighboring objects add hidden transfer. State whether the proposed system boundary encloses the source, the surrounding air and the insulation. Then repeat the balance after moving the boundary and check that the physical conclusion is unchanged.

## Engineering experiment and data interpretation

**Suggested investigation.** Calculate α from property tables, stating measurement temperature, composition, and uncertainty. Do not invent real measurements; start with an explicit hypothetical dataset or collect readings under appropriate supervision. Specify the sensor location, thermal settling criterion, and calibration state. Record environmental conditions, because an apparently small change in ambient temperature can alter both boundary gradients and material properties. Identify a control run that removes the driving source or changes only one variable. Repeat at least one operating point to estimate repeatability rather than treating an isolated reading as exact.

A defensible report includes an annotated sketch, a units table, the raw readings, a method for reducing data and a statement of what cannot be inferred. If an inverse calculation uses a model to estimate a coefficient, do not then use the very same data as independent validation. Reserve at least one different condition or instrument for a fair check. The student should be able to explain why a significant discrepancy may indicate an incorrect thermal boundary rather than a mistaken calculator operation.

## Model limits, troubleshooting and safety

**Frequent mistake:** Using a single room-temperature conductivity at an extreme operating temperature.

Diagnose the underlying reason instead of memorizing a warning. Ask what hidden assumption permits the easy formula to be written and what instrument would reveal its failure. A model may fail by incorrect dimensions, invalid regime, missing heat path, changing fluid property, an inappropriate temperature reference, or a neglected time-dependent term. Separate those failures from numerical mistakes and data-recording problems. Compare the predicted rate against any power or energy known to enter the system; a passive assembly cannot steadily deliver more energy than its stated supply without another source.

If the proposed object is a boiler, pressure vessel, battery pack, electrical appliance, medical device, industrial furnace or fire-safety system, this lesson supplies basic intuition only. Real design requires applicable codes, manufacturer data, validated correlations, abnormal-operation analysis and responsible professional review. The exploratory sliders in the companion models are not design certificates.

## Check your understanding — three problems

1. **Numerical variation.** Rework the example for a 15% increase in its driving thermal difference or equivalent controlling input. State the new units, compare changes as a percentage, and explain whether the relationship is truly linear at this point.
2. **Model selection.** Draw a different physical geometry or flow configuration where this equation might fail. Identify the precise assumption that breaks down, then propose a more suitable balance, correlation or measurement.
3. **Experimental critique.** Design a two-condition laboratory check of the guiding question. Specify a measurable dependent quantity, one plausible confounder, a calibration or repeatability step, and a criterion for recognizing a model–data disagreement.

## Extension: toward real engineering practice

Develop a small calculation sheet or script with named inputs, a units column and explicit warnings about any validity range. Test it at a nominal point and at two extremes, explaining whether the mathematics remains physically credible. Then imagine a colleague changed an input property without documenting temperature or source. Describe exactly how that would affect traceability and how you would reconstruct the decision. Finally propose one material, configuration or instrumentation change that improves thermal performance without adding unacceptable complexity or operating expense.

**Lesson conclusion.** Material properties and temperature dependence is useful when the energy pathway, geometry, regime and measurement basis agree. Recalculate when those conditions change; do not use apparent precision to hide uncertainty. Explain the result using a physical picture, not only a number.


---

# U01-L04 — Conservation of energy for thermal systems

**Unit 1: Heat Transfer Foundations and Thermal Modeling · Suggested workload 90–130 minutes · Educational draft**

## Learning question and physical setting

**Guiding question:** When does an electrical heater reach a stable operating temperature?

The central task in this lesson is not merely to insert values into a formula. It is to decide whether the formula represents the physical process, whether the thermal boundary is correctly located, and whether the resulting quantity can be compared to a measurement. The setting is concrete: An insulated 2 kg part receives 160 W and loses 40 W initially, giving an initial rise of 120/(2cp) K/s. Begin by explaining the physical mechanism in ordinary language before drawing a thermal diagram. Decide which direction energy is expected to move, and identify at least one quantity that changes if the surrounding temperature or operating power changes. This turns a numerical problem into a model that could be revised when new evidence appears.

## Conceptual foundations and governing relationship

**Core relationship:** `dE/dt = Qin−Qout+W for a closed control mass`.

A thermal balance requires a declaration of what belongs to the system and what crosses its surface. Electrical inputs, shaft work, mass transport and thermal transfer must not be combined casually. A temperature increase is evidence of internal energy storage only when material heat capacity and mass are properly represented. In actual instrumentation, an enclosure can receive heat from a nearby hotter object even if the room air is cool. Conversely, some heat may leave by several paths simultaneously. Describe each path before estimating a coefficient. The equation describes a particular kind of relation: sometimes a constitutive law, sometimes an integral energy balance, a nondimensional definition, a geometry-specific analytical solution, or a correlation validated only in an experimental range. Before using it, define each symbol and its units. State which values are measured, which are assumed, which are looked up, and which are inferred. Unlike an algebraic identity, a model may stop being valid when the shape, temperature distribution, flow regime, surface treatment or boundary conditions change. An answer that violates a conservation balance is unacceptable even if its arithmetic is flawless.

For **conservation of energy for thermal systems**, sketch the physical domain and draw arrows for the relevant energy paths. A first approximation is useful when it makes the dominant mechanism visible. A more detailed approximation is useful only when an observation motivates the additional complexity. In each case, decide whether spatial temperature gradients are physically essential, whether heat is stored, and whether material properties can be treated as uniform. The goal is to preserve both insight and a traceable decision process.

## Guided numerical example: Instantaneous rise: dT/dt=(Pin−Ploss)/(mc)

**Given synthetic inputs.** Pin=160 W, heat loss 40 W, mass 2 kg, c=900 J/(kg K).

**Operation.** Use the relationship `Instantaneous rise: dT/dt=(Pin−Ploss)/(mc)` with all inputs converted to compatible units; the result is **0.0667 K/s**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.

**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.

## Derivation map and assumptions

1. Draw a control volume or differential element. Mark every mechanism that carries energy across its boundary and each mechanism that stores or generates it.
2. Choose a coordinate and sign convention, identify a characteristic length, and state whether the requested answer concerns an area, a volume, a point temperature or an integrated rate.
3. Write the governing differential or integral balance. Separate physical conservation from constitutive assumptions, geometric identities and empirical correlations.
4. Simplify only after stating the neglected processes. Common simplifications include negligible contact resistance, uniform fluid properties, quasi-steady conduction or constant wall temperature; each has a plausible failure condition.
5. Substitute values with their dimensions retained. Evaluate a limiting case: zero driving difference, vanishing thickness, extremely low coefficient, large elapsed time or another mathematically relevant limit.
6. Examine whether the dependent quantity could be independently observed and whether the observed conditions would reproduce the assumptions used in the calculation.

For this topic, For this lesson, distinguish measured temperature from inferred energy transfer. Start a data sheet with a time stamp, location and uncertainty for every observation. Identify the heat input or loss path that a single thermometer cannot reveal. If conservation of energy for thermal systems is approached by an electrical-power measurement, determine whether leads, supports or neighboring objects add hidden transfer. State whether the proposed system boundary encloses the source, the surrounding air and the insulation. Then repeat the balance after moving the boundary and check that the physical conclusion is unchanged.

## Engineering experiment and data interpretation

**Suggested investigation.** Record supply power and temperature every ten seconds and compare estimated storage with measured losses. Do not invent real measurements; start with an explicit hypothetical dataset or collect readings under appropriate supervision. Specify the sensor location, thermal settling criterion, and calibration state. Record environmental conditions, because an apparently small change in ambient temperature can alter both boundary gradients and material properties. Identify a control run that removes the driving source or changes only one variable. Repeat at least one operating point to estimate repeatability rather than treating an isolated reading as exact.

A defensible report includes an annotated sketch, a units table, the raw readings, a method for reducing data and a statement of what cannot be inferred. If an inverse calculation uses a model to estimate a coefficient, do not then use the very same data as independent validation. Reserve at least one different condition or instrument for a fair check. The student should be able to explain why a significant discrepancy may indicate an incorrect thermal boundary rather than a mistaken calculator operation.

## Model limits, troubleshooting and safety

**Frequent mistake:** Dropping the accumulation term before establishing that conditions are steady.

Diagnose the underlying reason instead of memorizing a warning. Ask what hidden assumption permits the easy formula to be written and what instrument would reveal its failure. A model may fail by incorrect dimensions, invalid regime, missing heat path, changing fluid property, an inappropriate temperature reference, or a neglected time-dependent term. Separate those failures from numerical mistakes and data-recording problems. Compare the predicted rate against any power or energy known to enter the system; a passive assembly cannot steadily deliver more energy than its stated supply without another source.

If the proposed object is a boiler, pressure vessel, battery pack, electrical appliance, medical device, industrial furnace or fire-safety system, this lesson supplies basic intuition only. Real design requires applicable codes, manufacturer data, validated correlations, abnormal-operation analysis and responsible professional review. The exploratory sliders in the companion models are not design certificates.

## Check your understanding — three problems

1. **Numerical variation.** Rework the example for a 15% increase in its driving thermal difference or equivalent controlling input. State the new units, compare changes as a percentage, and explain whether the relationship is truly linear at this point.
2. **Model selection.** Draw a different physical geometry or flow configuration where this equation might fail. Identify the precise assumption that breaks down, then propose a more suitable balance, correlation or measurement.
3. **Experimental critique.** Design a two-condition laboratory check of the guiding question. Specify a measurable dependent quantity, one plausible confounder, a calibration or repeatability step, and a criterion for recognizing a model–data disagreement.

## Extension: toward real engineering practice

Develop a small calculation sheet or script with named inputs, a units column and explicit warnings about any validity range. Test it at a nominal point and at two extremes, explaining whether the mathematics remains physically credible. Then imagine a colleague changed an input property without documenting temperature or source. Describe exactly how that would affect traceability and how you would reconstruct the decision. Finally propose one material, configuration or instrumentation change that improves thermal performance without adding unacceptable complexity or operating expense.

**Lesson conclusion.** Conservation of energy for thermal systems is useful when the energy pathway, geometry, regime and measurement basis agree. Recalculate when those conditions change; do not use apparent precision to hide uncertainty. Explain the result using a physical picture, not only a number.


---

# U01-L05 — Thermal boundaries, units, and modeling scope

**Unit 1: Heat Transfer Foundations and Thermal Modeling · Suggested workload 90–130 minutes · Educational draft**

## Learning question and physical setting

**Guiding question:** What is the difference between a prescribed surface temperature, prescribed flux, and convective boundary?

The central task in this lesson is not merely to insert values into a formula. It is to decide whether the formula represents the physical process, whether the thermal boundary is correctly located, and whether the resulting quantity can be compared to a measurement. The setting is concrete: A steel panel can be held at 350 K by a controller, exposed to 300 W/m², or cooled by air with h=12 W/(m² K). Begin by explaining the physical mechanism in ordinary language before drawing a thermal diagram. Decide which direction energy is expected to move, and identify at least one quantity that changes if the surrounding temperature or operating power changes. This turns a numerical problem into a model that could be revised when new evidence appears.

## Conceptual foundations and governing relationship

**Core relationship:** `−k ∂T/∂n = h(Ts−T∞)`.

A thermal balance requires a declaration of what belongs to the system and what crosses its surface. Electrical inputs, shaft work, mass transport and thermal transfer must not be combined casually. A temperature increase is evidence of internal energy storage only when material heat capacity and mass are properly represented. In actual instrumentation, an enclosure can receive heat from a nearby hotter object even if the room air is cool. Conversely, some heat may leave by several paths simultaneously. Describe each path before estimating a coefficient. The equation describes a particular kind of relation: sometimes a constitutive law, sometimes an integral energy balance, a nondimensional definition, a geometry-specific analytical solution, or a correlation validated only in an experimental range. Before using it, define each symbol and its units. State which values are measured, which are assumed, which are looked up, and which are inferred. Unlike an algebraic identity, a model may stop being valid when the shape, temperature distribution, flow regime, surface treatment or boundary conditions change. An answer that violates a conservation balance is unacceptable even if its arithmetic is flawless.

For **thermal boundaries, units, and modeling scope**, sketch the physical domain and draw arrows for the relevant energy paths. A first approximation is useful when it makes the dominant mechanism visible. A more detailed approximation is useful only when an observation motivates the additional complexity. In each case, decide whether spatial temperature gradients are physically essential, whether heat is stored, and whether material properties can be treated as uniform. The goal is to preserve both insight and a traceable decision process.

## Guided numerical example: Newton-law boundary: q″=h(Ts−T∞)

**Given synthetic inputs.** h=12 W/(m² K), surface 350 K, ambient 300 K.

**Operation.** Use the relationship `Newton-law boundary: q″=h(Ts−T∞)` with all inputs converted to compatible units; the result is **600 W/m²**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.

**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.

## Derivation map and assumptions

1. Draw a control volume or differential element. Mark every mechanism that carries energy across its boundary and each mechanism that stores or generates it.
2. Choose a coordinate and sign convention, identify a characteristic length, and state whether the requested answer concerns an area, a volume, a point temperature or an integrated rate.
3. Write the governing differential or integral balance. Separate physical conservation from constitutive assumptions, geometric identities and empirical correlations.
4. Simplify only after stating the neglected processes. Common simplifications include negligible contact resistance, uniform fluid properties, quasi-steady conduction or constant wall temperature; each has a plausible failure condition.
5. Substitute values with their dimensions retained. Evaluate a limiting case: zero driving difference, vanishing thickness, extremely low coefficient, large elapsed time or another mathematically relevant limit.
6. Examine whether the dependent quantity could be independently observed and whether the observed conditions would reproduce the assumptions used in the calculation.

For this topic, For this lesson, distinguish measured temperature from inferred energy transfer. Start a data sheet with a time stamp, location and uncertainty for every observation. Identify the heat input or loss path that a single thermometer cannot reveal. If thermal boundaries, units, and modeling scope is approached by an electrical-power measurement, determine whether leads, supports or neighboring objects add hidden transfer. State whether the proposed system boundary encloses the source, the surrounding air and the insulation. Then repeat the balance after moving the boundary and check that the physical conclusion is unchanged.

## Engineering experiment and data interpretation

**Suggested investigation.** Switch between Dirichlet, Neumann, and Robin boundary conditions in a one-dimensional discretization. Do not invent real measurements; start with an explicit hypothetical dataset or collect readings under appropriate supervision. Specify the sensor location, thermal settling criterion, and calibration state. Record environmental conditions, because an apparently small change in ambient temperature can alter both boundary gradients and material properties. Identify a control run that removes the driving source or changes only one variable. Repeat at least one operating point to estimate repeatability rather than treating an isolated reading as exact.

A defensible report includes an annotated sketch, a units table, the raw readings, a method for reducing data and a statement of what cannot be inferred. If an inverse calculation uses a model to estimate a coefficient, do not then use the very same data as independent validation. Reserve at least one different condition or instrument for a fair check. The student should be able to explain why a significant discrepancy may indicate an incorrect thermal boundary rather than a mistaken calculator operation.

## Model limits, troubleshooting and safety

**Frequent mistake:** Using a fixed-temperature boundary where the actual heater has limited power.

Diagnose the underlying reason instead of memorizing a warning. Ask what hidden assumption permits the easy formula to be written and what instrument would reveal its failure. A model may fail by incorrect dimensions, invalid regime, missing heat path, changing fluid property, an inappropriate temperature reference, or a neglected time-dependent term. Separate those failures from numerical mistakes and data-recording problems. Compare the predicted rate against any power or energy known to enter the system; a passive assembly cannot steadily deliver more energy than its stated supply without another source.

If the proposed object is a boiler, pressure vessel, battery pack, electrical appliance, medical device, industrial furnace or fire-safety system, this lesson supplies basic intuition only. Real design requires applicable codes, manufacturer data, validated correlations, abnormal-operation analysis and responsible professional review. The exploratory sliders in the companion models are not design certificates.

## Check your understanding — three problems

1. **Numerical variation.** Rework the example for a 15% increase in its driving thermal difference or equivalent controlling input. State the new units, compare changes as a percentage, and explain whether the relationship is truly linear at this point.
2. **Model selection.** Draw a different physical geometry or flow configuration where this equation might fail. Identify the precise assumption that breaks down, then propose a more suitable balance, correlation or measurement.
3. **Experimental critique.** Design a two-condition laboratory check of the guiding question. Specify a measurable dependent quantity, one plausible confounder, a calibration or repeatability step, and a criterion for recognizing a model–data disagreement.

## Extension: toward real engineering practice

Develop a small calculation sheet or script with named inputs, a units column and explicit warnings about any validity range. Test it at a nominal point and at two extremes, explaining whether the mathematics remains physically credible. Then imagine a colleague changed an input property without documenting temperature or source. Describe exactly how that would affect traceability and how you would reconstruct the decision. Finally propose one material, configuration or instrumentation change that improves thermal performance without adding unacceptable complexity or operating expense.

**Lesson conclusion.** Thermal boundaries, units, and modeling scope is useful when the energy pathway, geometry, regime and measurement basis agree. Recalculate when those conditions change; do not use apparent precision to hide uncertainty. Explain the result using a physical picture, not only a number.


---

