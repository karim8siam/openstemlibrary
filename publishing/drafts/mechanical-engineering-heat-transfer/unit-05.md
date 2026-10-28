# Unit 05: Boiling, Condensation, and Phase-Change Heat Transfer

**Course Code**: HTR 205 · **Level**: Advanced Undergraduate Engineering

## Unit Overview & Physical Foundations

This comprehensive university textbook unit covers the theoretical framework, physical modeling, mathematical governing equations, and engineering applications of **Boiling, Condensation, and Phase-Change Heat Transfer**.

# U05-L01 — Nucleate boiling and boiling curves

**Unit 5: Boiling, Condensation, and Phase-Change Heat Transfer · Suggested workload 90–130 minutes · Educational draft**

## Learning question and physical setting

**Guiding question:** Why is the onset of nucleate boiling desirable in some exchangers but dangerous near critical heat flux?

The central task in this lesson is not merely to insert values into a formula. It is to decide whether the formula represents the physical process, whether the thermal boundary is correctly located, and whether the resulting quantity can be compared to a measurement. The setting is concrete: A heated water surface can undergo natural convection, nucleate boiling, departure from nucleate boiling and film boiling. Begin by explaining the physical mechanism in ordinary language before drawing a thermal diagram. Decide which direction energy is expected to move, and identify at least one quantity that changes if the surrounding temperature or operating power changes. This turns a numerical problem into a model that could be revised when new evidence appears.

## Conceptual foundations and governing relationship

**Core relationship:** `q = hboil(Twall−Tsat) as a local approximation`.

An interface at approximately the saturation temperature may transfer large energy by changing phase rather than changing sensible temperature. Yet surface superheat, local vapor fraction, pressure and wettability affect the regime, and a moving phase boundary introduces geometry and changing resistance. Engineering safety cannot rest on a single simplified boiling or condensation coefficient. The environment may become unstable at abrupt transitions; record which regime is assumed and which observable signs would indicate that the assumption has failed. The equation describes a particular kind of relation: sometimes a constitutive law, sometimes an integral energy balance, a nondimensional definition, a geometry-specific analytical solution, or a correlation validated only in an experimental range. Before using it, define each symbol and its units. State which values are measured, which are assumed, which are looked up, and which are inferred. Unlike an algebraic identity, a model may stop being valid when the shape, temperature distribution, flow regime, surface treatment or boundary conditions change. An answer that violates a conservation balance is unacceptable even if its arithmetic is flawless.

For **nucleate boiling and boiling curves**, sketch the physical domain and draw arrows for the relevant energy paths. A first approximation is useful when it makes the dominant mechanism visible. A more detailed approximation is useful only when an observation motivates the additional complexity. In each case, decide whether spatial temperature gradients are physically essential, whether heat is stored, and whether material properties can be treated as uniform. The goal is to preserve both insight and a traceable decision process.

## Guided numerical example: Local boiling duty: Q=q″A

**Given synthetic inputs.** Hypothetical local heat flux 4500 W/m² over area 0.03 m².

**Operation.** Use the relationship `Local boiling duty: Q=q″A` with all inputs converted to compatible units; the result is **135 W**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.

**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.

## Derivation map and assumptions

1. Draw a control volume or differential element. Mark every mechanism that carries energy across its boundary and each mechanism that stores or generates it.
2. Choose a coordinate and sign convention, identify a characteristic length, and state whether the requested answer concerns an area, a volume, a point temperature or an integrated rate.
3. Write the governing differential or integral balance. Separate physical conservation from constitutive assumptions, geometric identities and empirical correlations.
4. Simplify only after stating the neglected processes. Common simplifications include negligible contact resistance, uniform fluid properties, quasi-steady conduction or constant wall temperature; each has a plausible failure condition.
5. Substitute values with their dimensions retained. Evaluate a limiting case: zero driving difference, vanishing thickness, extremely low coefficient, large elapsed time or another mathematically relevant limit.
6. Examine whether the dependent quantity could be independently observed and whether the observed conditions would reproduce the assumptions used in the calculation.

For this topic, For nucleate boiling and boiling curves, clarify whether mass actually changes phase and what it crosses. Latent heat can dominate a control-volume balance, but phase-front movement can introduce time-dependent conduction resistance. A steady-looking interface temperature does not guarantee steady heat flow. Pressures, nucleation sites, surface conditions, local liquid supply and vapor removal alter behavior. When a hazard involves dryout or unstable boiling, avoid treating a pedagogical fit as evidence for a safe threshold. An independent safety and standards analysis is mandatory for equipment.

## Engineering experiment and data interpretation

**Suggested investigation.** Read an experimental boiling curve and identify qualitative regime transitions and hysteresis. Do not invent real measurements; start with an explicit hypothetical dataset or collect readings under appropriate supervision. Specify the sensor location, thermal settling criterion, and calibration state. Record environmental conditions, because an apparently small change in ambient temperature can alter both boundary gradients and material properties. Identify a control run that removes the driving source or changes only one variable. Repeat at least one operating point to estimate repeatability rather than treating an isolated reading as exact.

A defensible report includes an annotated sketch, a units table, the raw readings, a method for reducing data and a statement of what cannot be inferred. If an inverse calculation uses a model to estimate a coefficient, do not then use the very same data as independent validation. Reserve at least one different condition or instrument for a fair check. The student should be able to explain why a significant discrepancy may indicate an incorrect thermal boundary rather than a mistaken calculator operation.

## Model limits, troubleshooting and safety

**Frequent mistake:** Assuming heat flux increases monotonically with surface superheat across the entire boiling curve.

Diagnose the underlying reason instead of memorizing a warning. Ask what hidden assumption permits the easy formula to be written and what instrument would reveal its failure. A model may fail by incorrect dimensions, invalid regime, missing heat path, changing fluid property, an inappropriate temperature reference, or a neglected time-dependent term. Separate those failures from numerical mistakes and data-recording problems. Compare the predicted rate against any power or energy known to enter the system; a passive assembly cannot steadily deliver more energy than its stated supply without another source.

If the proposed object is a boiler, pressure vessel, battery pack, electrical appliance, medical device, industrial furnace or fire-safety system, this lesson supplies basic intuition only. Real design requires applicable codes, manufacturer data, validated correlations, abnormal-operation analysis and responsible professional review. The exploratory sliders in the companion models are not design certificates.

## Check your understanding — three problems

1. **Numerical variation.** Rework the example for a 15% increase in its driving thermal difference or equivalent controlling input. State the new units, compare changes as a percentage, and explain whether the relationship is truly linear at this point.
2. **Model selection.** Draw a different physical geometry or flow configuration where this equation might fail. Identify the precise assumption that breaks down, then propose a more suitable balance, correlation or measurement.
3. **Experimental critique.** Design a two-condition laboratory check of the guiding question. Specify a measurable dependent quantity, one plausible confounder, a calibration or repeatability step, and a criterion for recognizing a model–data disagreement.

## Extension: toward real engineering practice

Develop a small calculation sheet or script with named inputs, a units column and explicit warnings about any validity range. Test it at a nominal point and at two extremes, explaining whether the mathematics remains physically credible. Then imagine a colleague changed an input property without documenting temperature or source. Describe exactly how that would affect traceability and how you would reconstruct the decision. Finally propose one material, configuration or instrumentation change that improves thermal performance without adding unacceptable complexity or operating expense.

**Lesson conclusion.** Nucleate boiling and boiling curves is useful when the energy pathway, geometry, regime and measurement basis agree. Recalculate when those conditions change; do not use apparent precision to hide uncertainty. Explain the result using a physical picture, not only a number.


---

# U05-L02 — Critical heat flux and boiling safety

**Unit 5: Boiling, Condensation, and Phase-Change Heat Transfer · Suggested workload 90–130 minutes · Educational draft**

## Learning question and physical setting

**Guiding question:** What operating uncertainties can unexpectedly cross a critical heat-flux threshold?

The central task in this lesson is not merely to insert values into a formula. It is to decide whether the formula represents the physical process, whether the thermal boundary is correctly located, and whether the resulting quantity can be compared to a measurement. The setting is concrete: A nominally stable evaporator may experience changing pressure, fluid quality, scale formation or local hot spots. Begin by explaining the physical mechanism in ordinary language before drawing a thermal diagram. Decide which direction energy is expected to move, and identify at least one quantity that changes if the surrounding temperature or operating power changes. This turns a numerical problem into a model that could be revised when new evidence appears.

## Conceptual foundations and governing relationship

**Core relationship:** `q < qCHF with verified margin`.

An interface at approximately the saturation temperature may transfer large energy by changing phase rather than changing sensible temperature. Yet surface superheat, local vapor fraction, pressure and wettability affect the regime, and a moving phase boundary introduces geometry and changing resistance. Engineering safety cannot rest on a single simplified boiling or condensation coefficient. The environment may become unstable at abrupt transitions; record which regime is assumed and which observable signs would indicate that the assumption has failed. The equation describes a particular kind of relation: sometimes a constitutive law, sometimes an integral energy balance, a nondimensional definition, a geometry-specific analytical solution, or a correlation validated only in an experimental range. Before using it, define each symbol and its units. State which values are measured, which are assumed, which are looked up, and which are inferred. Unlike an algebraic identity, a model may stop being valid when the shape, temperature distribution, flow regime, surface treatment or boundary conditions change. An answer that violates a conservation balance is unacceptable even if its arithmetic is flawless.

For **critical heat flux and boiling safety**, sketch the physical domain and draw arrows for the relevant energy paths. A first approximation is useful when it makes the dominant mechanism visible. A more detailed approximation is useful only when an observation motivates the additional complexity. In each case, decide whether spatial temperature gradients are physically essential, whether heat is stored, and whether material properties can be treated as uniform. The goal is to preserve both insight and a traceable decision process.

## Guided numerical example: CHF threshold comparison: qnominal/qCHF

**Given synthetic inputs.** Nominal 90 kW/m² versus illustrative threshold 120 kW/m²; NOT an operating safety criterion.

**Operation.** Use the relationship `CHF threshold comparison: qnominal/qCHF` with all inputs converted to compatible units; the result is **0.75 fraction**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.

**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.

## Derivation map and assumptions

1. Draw a control volume or differential element. Mark every mechanism that carries energy across its boundary and each mechanism that stores or generates it.
2. Choose a coordinate and sign convention, identify a characteristic length, and state whether the requested answer concerns an area, a volume, a point temperature or an integrated rate.
3. Write the governing differential or integral balance. Separate physical conservation from constitutive assumptions, geometric identities and empirical correlations.
4. Simplify only after stating the neglected processes. Common simplifications include negligible contact resistance, uniform fluid properties, quasi-steady conduction or constant wall temperature; each has a plausible failure condition.
5. Substitute values with their dimensions retained. Evaluate a limiting case: zero driving difference, vanishing thickness, extremely low coefficient, large elapsed time or another mathematically relevant limit.
6. Examine whether the dependent quantity could be independently observed and whether the observed conditions would reproduce the assumptions used in the calculation.

For this topic, For critical heat flux and boiling safety, clarify whether mass actually changes phase and what it crosses. Latent heat can dominate a control-volume balance, but phase-front movement can introduce time-dependent conduction resistance. A steady-looking interface temperature does not guarantee steady heat flow. Pressures, nucleation sites, surface conditions, local liquid supply and vapor removal alter behavior. When a hazard involves dryout or unstable boiling, avoid treating a pedagogical fit as evidence for a safe threshold. An independent safety and standards analysis is mandatory for equipment.

## Engineering experiment and data interpretation

**Suggested investigation.** Create a hazard table for dryout, instrumentation delay and emergency shutoff in a hypothetical loop. Do not invent real measurements; start with an explicit hypothetical dataset or collect readings under appropriate supervision. Specify the sensor location, thermal settling criterion, and calibration state. Record environmental conditions, because an apparently small change in ambient temperature can alter both boundary gradients and material properties. Identify a control run that removes the driving source or changes only one variable. Repeat at least one operating point to estimate repeatability rather than treating an isolated reading as exact.

A defensible report includes an annotated sketch, a units table, the raw readings, a method for reducing data and a statement of what cannot be inferred. If an inverse calculation uses a model to estimate a coefficient, do not then use the very same data as independent validation. Reserve at least one different condition or instrument for a fair check. The student should be able to explain why a significant discrepancy may indicate an incorrect thermal boundary rather than a mistaken calculator operation.

## Model limits, troubleshooting and safety

**Frequent mistake:** Using a classroom CHF estimate as a safe operating limit or ignoring local flux variations.

Diagnose the underlying reason instead of memorizing a warning. Ask what hidden assumption permits the easy formula to be written and what instrument would reveal its failure. A model may fail by incorrect dimensions, invalid regime, missing heat path, changing fluid property, an inappropriate temperature reference, or a neglected time-dependent term. Separate those failures from numerical mistakes and data-recording problems. Compare the predicted rate against any power or energy known to enter the system; a passive assembly cannot steadily deliver more energy than its stated supply without another source.

If the proposed object is a boiler, pressure vessel, battery pack, electrical appliance, medical device, industrial furnace or fire-safety system, this lesson supplies basic intuition only. Real design requires applicable codes, manufacturer data, validated correlations, abnormal-operation analysis and responsible professional review. The exploratory sliders in the companion models are not design certificates.

## Check your understanding — three problems

1. **Numerical variation.** Rework the example for a 15% increase in its driving thermal difference or equivalent controlling input. State the new units, compare changes as a percentage, and explain whether the relationship is truly linear at this point.
2. **Model selection.** Draw a different physical geometry or flow configuration where this equation might fail. Identify the precise assumption that breaks down, then propose a more suitable balance, correlation or measurement.
3. **Experimental critique.** Design a two-condition laboratory check of the guiding question. Specify a measurable dependent quantity, one plausible confounder, a calibration or repeatability step, and a criterion for recognizing a model–data disagreement.

## Extension: toward real engineering practice

Develop a small calculation sheet or script with named inputs, a units column and explicit warnings about any validity range. Test it at a nominal point and at two extremes, explaining whether the mathematics remains physically credible. Then imagine a colleague changed an input property without documenting temperature or source. Describe exactly how that would affect traceability and how you would reconstruct the decision. Finally propose one material, configuration or instrumentation change that improves thermal performance without adding unacceptable complexity or operating expense.

**Lesson conclusion.** Critical heat flux and boiling safety is useful when the energy pathway, geometry, regime and measurement basis agree. Recalculate when those conditions change; do not use apparent precision to hide uncertainty. Explain the result using a physical picture, not only a number.


---

# U05-L03 — Filmwise and dropwise condensation

**Unit 5: Boiling, Condensation, and Phase-Change Heat Transfer · Suggested workload 90–130 minutes · Educational draft**

## Learning question and physical setting

**Guiding question:** Why does condensate drainage strongly influence heat transfer?

The central task in this lesson is not merely to insert values into a formula. It is to decide whether the formula represents the physical process, whether the thermal boundary is correctly located, and whether the resulting quantity can be compared to a measurement. The setting is concrete: A vertical condenser plate accumulates a liquid film whose thickness and resistance vary with height. Begin by explaining the physical mechanism in ordinary language before drawing a thermal diagram. Decide which direction energy is expected to move, and identify at least one quantity that changes if the surrounding temperature or operating power changes. This turns a numerical problem into a model that could be revised when new evidence appears.

## Conceptual foundations and governing relationship

**Core relationship:** `Q=U A ΔT as a system-level approximation`.

An interface at approximately the saturation temperature may transfer large energy by changing phase rather than changing sensible temperature. Yet surface superheat, local vapor fraction, pressure and wettability affect the regime, and a moving phase boundary introduces geometry and changing resistance. Engineering safety cannot rest on a single simplified boiling or condensation coefficient. The environment may become unstable at abrupt transitions; record which regime is assumed and which observable signs would indicate that the assumption has failed. The equation describes a particular kind of relation: sometimes a constitutive law, sometimes an integral energy balance, a nondimensional definition, a geometry-specific analytical solution, or a correlation validated only in an experimental range. Before using it, define each symbol and its units. State which values are measured, which are assumed, which are looked up, and which are inferred. Unlike an algebraic identity, a model may stop being valid when the shape, temperature distribution, flow regime, surface treatment or boundary conditions change. An answer that violates a conservation balance is unacceptable even if its arithmetic is flawless.

For **filmwise and dropwise condensation**, sketch the physical domain and draw arrows for the relevant energy paths. A first approximation is useful when it makes the dominant mechanism visible. A more detailed approximation is useful only when an observation motivates the additional complexity. In each case, decide whether spatial temperature gradients are physically essential, whether heat is stored, and whether material properties can be treated as uniform. The goal is to preserve both insight and a traceable decision process.

## Guided numerical example: Overall condenser: Q=UAΔT

**Given synthetic inputs.** Assumed U=250 W/(m² K), A=2 m² and representative ΔT=20 K.

**Operation.** Use the relationship `Overall condenser: Q=UAΔT` with all inputs converted to compatible units; the result is **1e+04 W**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.

**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.

## Derivation map and assumptions

1. Draw a control volume or differential element. Mark every mechanism that carries energy across its boundary and each mechanism that stores or generates it.
2. Choose a coordinate and sign convention, identify a characteristic length, and state whether the requested answer concerns an area, a volume, a point temperature or an integrated rate.
3. Write the governing differential or integral balance. Separate physical conservation from constitutive assumptions, geometric identities and empirical correlations.
4. Simplify only after stating the neglected processes. Common simplifications include negligible contact resistance, uniform fluid properties, quasi-steady conduction or constant wall temperature; each has a plausible failure condition.
5. Substitute values with their dimensions retained. Evaluate a limiting case: zero driving difference, vanishing thickness, extremely low coefficient, large elapsed time or another mathematically relevant limit.
6. Examine whether the dependent quantity could be independently observed and whether the observed conditions would reproduce the assumptions used in the calculation.

For this topic, For filmwise and dropwise condensation, clarify whether mass actually changes phase and what it crosses. Latent heat can dominate a control-volume balance, but phase-front movement can introduce time-dependent conduction resistance. A steady-looking interface temperature does not guarantee steady heat flow. Pressures, nucleation sites, surface conditions, local liquid supply and vapor removal alter behavior. When a hazard involves dryout or unstable boiling, avoid treating a pedagogical fit as evidence for a safe threshold. An independent safety and standards analysis is mandatory for equipment.

## Engineering experiment and data interpretation

**Suggested investigation.** Photograph condensate patterns and compare heat flux under clean and contaminated surfaces. Do not invent real measurements; start with an explicit hypothetical dataset or collect readings under appropriate supervision. Specify the sensor location, thermal settling criterion, and calibration state. Record environmental conditions, because an apparently small change in ambient temperature can alter both boundary gradients and material properties. Identify a control run that removes the driving source or changes only one variable. Repeat at least one operating point to estimate repeatability rather than treating an isolated reading as exact.

A defensible report includes an annotated sketch, a units table, the raw readings, a method for reducing data and a statement of what cannot be inferred. If an inverse calculation uses a model to estimate a coefficient, do not then use the very same data as independent validation. Reserve at least one different condition or instrument for a fair check. The student should be able to explain why a significant discrepancy may indicate an incorrect thermal boundary rather than a mistaken calculator operation.

## Model limits, troubleshooting and safety

**Frequent mistake:** Assuming a stable dropwise surface without testing coating durability and contamination.

Diagnose the underlying reason instead of memorizing a warning. Ask what hidden assumption permits the easy formula to be written and what instrument would reveal its failure. A model may fail by incorrect dimensions, invalid regime, missing heat path, changing fluid property, an inappropriate temperature reference, or a neglected time-dependent term. Separate those failures from numerical mistakes and data-recording problems. Compare the predicted rate against any power or energy known to enter the system; a passive assembly cannot steadily deliver more energy than its stated supply without another source.

If the proposed object is a boiler, pressure vessel, battery pack, electrical appliance, medical device, industrial furnace or fire-safety system, this lesson supplies basic intuition only. Real design requires applicable codes, manufacturer data, validated correlations, abnormal-operation analysis and responsible professional review. The exploratory sliders in the companion models are not design certificates.

## Check your understanding — three problems

1. **Numerical variation.** Rework the example for a 15% increase in its driving thermal difference or equivalent controlling input. State the new units, compare changes as a percentage, and explain whether the relationship is truly linear at this point.
2. **Model selection.** Draw a different physical geometry or flow configuration where this equation might fail. Identify the precise assumption that breaks down, then propose a more suitable balance, correlation or measurement.
3. **Experimental critique.** Design a two-condition laboratory check of the guiding question. Specify a measurable dependent quantity, one plausible confounder, a calibration or repeatability step, and a criterion for recognizing a model–data disagreement.

## Extension: toward real engineering practice

Develop a small calculation sheet or script with named inputs, a units column and explicit warnings about any validity range. Test it at a nominal point and at two extremes, explaining whether the mathematics remains physically credible. Then imagine a colleague changed an input property without documenting temperature or source. Describe exactly how that would affect traceability and how you would reconstruct the decision. Finally propose one material, configuration or instrumentation change that improves thermal performance without adding unacceptable complexity or operating expense.

**Lesson conclusion.** Filmwise and dropwise condensation is useful when the energy pathway, geometry, regime and measurement basis agree. Recalculate when those conditions change; do not use apparent precision to hide uncertainty. Explain the result using a physical picture, not only a number.


---

# U05-L04 — Solidification and melting

**Unit 5: Boiling, Condensation, and Phase-Change Heat Transfer · Suggested workload 90–130 minutes · Educational draft**

## Learning question and physical setting

**Guiding question:** How fast does a planar freezing front advance under a fixed temperature difference?

The central task in this lesson is not merely to insert values into a formula. It is to decide whether the formula represents the physical process, whether the thermal boundary is correctly located, and whether the resulting quantity can be compared to a measurement. The setting is concrete: Ice formation on a chilled plate creates an insulating layer that slows growth with time. Begin by explaining the physical mechanism in ordinary language before drawing a thermal diagram. Decide which direction energy is expected to move, and identify at least one quantity that changes if the surrounding temperature or operating power changes. This turns a numerical problem into a model that could be revised when new evidence appears.

## Conceptual foundations and governing relationship

**Core relationship:** `x ≈ sqrt[2kΔT t/(ρLf)] in a simplified one-phase Stefan limit`.

An interface at approximately the saturation temperature may transfer large energy by changing phase rather than changing sensible temperature. Yet surface superheat, local vapor fraction, pressure and wettability affect the regime, and a moving phase boundary introduces geometry and changing resistance. Engineering safety cannot rest on a single simplified boiling or condensation coefficient. The environment may become unstable at abrupt transitions; record which regime is assumed and which observable signs would indicate that the assumption has failed. The equation describes a particular kind of relation: sometimes a constitutive law, sometimes an integral energy balance, a nondimensional definition, a geometry-specific analytical solution, or a correlation validated only in an experimental range. Before using it, define each symbol and its units. State which values are measured, which are assumed, which are looked up, and which are inferred. Unlike an algebraic identity, a model may stop being valid when the shape, temperature distribution, flow regime, surface treatment or boundary conditions change. An answer that violates a conservation balance is unacceptable even if its arithmetic is flawless.

For **solidification and melting**, sketch the physical domain and draw arrows for the relevant energy paths. A first approximation is useful when it makes the dominant mechanism visible. A more detailed approximation is useful only when an observation motivates the additional complexity. In each case, decide whether spatial temperature gradients are physically essential, whether heat is stored, and whether material properties can be treated as uniform. The goal is to preserve both insight and a traceable decision process.

## Guided numerical example: Quasi-steady front location

**Given synthetic inputs.** k=2.2 W/(m K); ΔT=12 K; t=300 s; ρ=920 kg/m³; Lf=334 kJ/kg.

**Operation.** Use the relationship `Quasi-steady front location` with all inputs converted to compatible units; the result is **0.0072 m**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.

**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.

## Derivation map and assumptions

1. Draw a control volume or differential element. Mark every mechanism that carries energy across its boundary and each mechanism that stores or generates it.
2. Choose a coordinate and sign convention, identify a characteristic length, and state whether the requested answer concerns an area, a volume, a point temperature or an integrated rate.
3. Write the governing differential or integral balance. Separate physical conservation from constitutive assumptions, geometric identities and empirical correlations.
4. Simplify only after stating the neglected processes. Common simplifications include negligible contact resistance, uniform fluid properties, quasi-steady conduction or constant wall temperature; each has a plausible failure condition.
5. Substitute values with their dimensions retained. Evaluate a limiting case: zero driving difference, vanishing thickness, extremely low coefficient, large elapsed time or another mathematically relevant limit.
6. Examine whether the dependent quantity could be independently observed and whether the observed conditions would reproduce the assumptions used in the calculation.

For this topic, For solidification and melting, clarify whether mass actually changes phase and what it crosses. Latent heat can dominate a control-volume balance, but phase-front movement can introduce time-dependent conduction resistance. A steady-looking interface temperature does not guarantee steady heat flow. Pressures, nucleation sites, surface conditions, local liquid supply and vapor removal alter behavior. When a hazard involves dryout or unstable boiling, avoid treating a pedagogical fit as evidence for a safe threshold. An independent safety and standards analysis is mandatory for equipment.

## Engineering experiment and data interpretation

**Suggested investigation.** Measure the frozen-layer thickness at regular intervals and examine whether x² is linear in time. Do not invent real measurements; start with an explicit hypothetical dataset or collect readings under appropriate supervision. Specify the sensor location, thermal settling criterion, and calibration state. Record environmental conditions, because an apparently small change in ambient temperature can alter both boundary gradients and material properties. Identify a control run that removes the driving source or changes only one variable. Repeat at least one operating point to estimate repeatability rather than treating an isolated reading as exact.

A defensible report includes an annotated sketch, a units table, the raw readings, a method for reducing data and a statement of what cannot be inferred. If an inverse calculation uses a model to estimate a coefficient, do not then use the very same data as independent validation. Reserve at least one different condition or instrument for a fair check. The student should be able to explain why a significant discrepancy may indicate an incorrect thermal boundary rather than a mistaken calculator operation.

## Model limits, troubleshooting and safety

**Frequent mistake:** Applying a semi-infinite phase-front law when sensible heating or changing boundaries dominate.

Diagnose the underlying reason instead of memorizing a warning. Ask what hidden assumption permits the easy formula to be written and what instrument would reveal its failure. A model may fail by incorrect dimensions, invalid regime, missing heat path, changing fluid property, an inappropriate temperature reference, or a neglected time-dependent term. Separate those failures from numerical mistakes and data-recording problems. Compare the predicted rate against any power or energy known to enter the system; a passive assembly cannot steadily deliver more energy than its stated supply without another source.

If the proposed object is a boiler, pressure vessel, battery pack, electrical appliance, medical device, industrial furnace or fire-safety system, this lesson supplies basic intuition only. Real design requires applicable codes, manufacturer data, validated correlations, abnormal-operation analysis and responsible professional review. The exploratory sliders in the companion models are not design certificates.

## Check your understanding — three problems

1. **Numerical variation.** Rework the example for a 15% increase in its driving thermal difference or equivalent controlling input. State the new units, compare changes as a percentage, and explain whether the relationship is truly linear at this point.
2. **Model selection.** Draw a different physical geometry or flow configuration where this equation might fail. Identify the precise assumption that breaks down, then propose a more suitable balance, correlation or measurement.
3. **Experimental critique.** Design a two-condition laboratory check of the guiding question. Specify a measurable dependent quantity, one plausible confounder, a calibration or repeatability step, and a criterion for recognizing a model–data disagreement.

## Extension: toward real engineering practice

Develop a small calculation sheet or script with named inputs, a units column and explicit warnings about any validity range. Test it at a nominal point and at two extremes, explaining whether the mathematics remains physically credible. Then imagine a colleague changed an input property without documenting temperature or source. Describe exactly how that would affect traceability and how you would reconstruct the decision. Finally propose one material, configuration or instrumentation change that improves thermal performance without adding unacceptable complexity or operating expense.

**Lesson conclusion.** Solidification and melting is useful when the energy pathway, geometry, regime and measurement basis agree. Recalculate when those conditions change; do not use apparent precision to hide uncertainty. Explain the result using a physical picture, not only a number.


---

# U05-L05 — Evaporation, latent heat, and moist-air exchange

**Unit 5: Boiling, Condensation, and Phase-Change Heat Transfer · Suggested workload 90–130 minutes · Educational draft**

## Learning question and physical setting

**Guiding question:** Why can a thin evaporating film remove substantial heat at nearly constant temperature?

The central task in this lesson is not merely to insert values into a formula. It is to decide whether the formula represents the physical process, whether the thermal boundary is correctly located, and whether the resulting quantity can be compared to a measurement. The setting is concrete: Evaporating 0.01 kg of water near ambient conditions removes roughly 24 kJ using a representative latent heat. Begin by explaining the physical mechanism in ordinary language before drawing a thermal diagram. Decide which direction energy is expected to move, and identify at least one quantity that changes if the surrounding temperature or operating power changes. This turns a numerical problem into a model that could be revised when new evidence appears.

## Conceptual foundations and governing relationship

**Core relationship:** `Qlatent=m_evap hfg`.

An interface at approximately the saturation temperature may transfer large energy by changing phase rather than changing sensible temperature. Yet surface superheat, local vapor fraction, pressure and wettability affect the regime, and a moving phase boundary introduces geometry and changing resistance. Engineering safety cannot rest on a single simplified boiling or condensation coefficient. The environment may become unstable at abrupt transitions; record which regime is assumed and which observable signs would indicate that the assumption has failed. The equation describes a particular kind of relation: sometimes a constitutive law, sometimes an integral energy balance, a nondimensional definition, a geometry-specific analytical solution, or a correlation validated only in an experimental range. Before using it, define each symbol and its units. State which values are measured, which are assumed, which are looked up, and which are inferred. Unlike an algebraic identity, a model may stop being valid when the shape, temperature distribution, flow regime, surface treatment or boundary conditions change. An answer that violates a conservation balance is unacceptable even if its arithmetic is flawless.

For **evaporation, latent heat, and moist-air exchange**, sketch the physical domain and draw arrows for the relevant energy paths. A first approximation is useful when it makes the dominant mechanism visible. A more detailed approximation is useful only when an observation motivates the additional complexity. In each case, decide whether spatial temperature gradients are physically essential, whether heat is stored, and whether material properties can be treated as uniform. The goal is to preserve both insight and a traceable decision process.

## Guided numerical example: Latent cooling: Q=m hfg

**Given synthetic inputs.** Evaporated water mass 0.01 kg; illustrative hfg=2.4 MJ/kg.

**Operation.** Use the relationship `Latent cooling: Q=m hfg` with all inputs converted to compatible units; the result is **2.4e+04 J**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.

**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.

## Derivation map and assumptions

1. Draw a control volume or differential element. Mark every mechanism that carries energy across its boundary and each mechanism that stores or generates it.
2. Choose a coordinate and sign convention, identify a characteristic length, and state whether the requested answer concerns an area, a volume, a point temperature or an integrated rate.
3. Write the governing differential or integral balance. Separate physical conservation from constitutive assumptions, geometric identities and empirical correlations.
4. Simplify only after stating the neglected processes. Common simplifications include negligible contact resistance, uniform fluid properties, quasi-steady conduction or constant wall temperature; each has a plausible failure condition.
5. Substitute values with their dimensions retained. Evaluate a limiting case: zero driving difference, vanishing thickness, extremely low coefficient, large elapsed time or another mathematically relevant limit.
6. Examine whether the dependent quantity could be independently observed and whether the observed conditions would reproduce the assumptions used in the calculation.

For this topic, For evaporation, latent heat, and moist-air exchange, clarify whether mass actually changes phase and what it crosses. Latent heat can dominate a control-volume balance, but phase-front movement can introduce time-dependent conduction resistance. A steady-looking interface temperature does not guarantee steady heat flow. Pressures, nucleation sites, surface conditions, local liquid supply and vapor removal alter behavior. When a hazard involves dryout or unstable boiling, avoid treating a pedagogical fit as evidence for a safe threshold. An independent safety and standards analysis is mandatory for equipment.

## Engineering experiment and data interpretation

**Suggested investigation.** Compare dry- and wet-bulb measurements and estimate mass-transfer limitations. Do not invent real measurements; start with an explicit hypothetical dataset or collect readings under appropriate supervision. Specify the sensor location, thermal settling criterion, and calibration state. Record environmental conditions, because an apparently small change in ambient temperature can alter both boundary gradients and material properties. Identify a control run that removes the driving source or changes only one variable. Repeat at least one operating point to estimate repeatability rather than treating an isolated reading as exact.

A defensible report includes an annotated sketch, a units table, the raw readings, a method for reducing data and a statement of what cannot be inferred. If an inverse calculation uses a model to estimate a coefficient, do not then use the very same data as independent validation. Reserve at least one different condition or instrument for a fair check. The student should be able to explain why a significant discrepancy may indicate an incorrect thermal boundary rather than a mistaken calculator operation.

## Model limits, troubleshooting and safety

**Frequent mistake:** Assuming an evaporation rate from heat input alone without checking available vapor transport.

Diagnose the underlying reason instead of memorizing a warning. Ask what hidden assumption permits the easy formula to be written and what instrument would reveal its failure. A model may fail by incorrect dimensions, invalid regime, missing heat path, changing fluid property, an inappropriate temperature reference, or a neglected time-dependent term. Separate those failures from numerical mistakes and data-recording problems. Compare the predicted rate against any power or energy known to enter the system; a passive assembly cannot steadily deliver more energy than its stated supply without another source.

If the proposed object is a boiler, pressure vessel, battery pack, electrical appliance, medical device, industrial furnace or fire-safety system, this lesson supplies basic intuition only. Real design requires applicable codes, manufacturer data, validated correlations, abnormal-operation analysis and responsible professional review. The exploratory sliders in the companion models are not design certificates.

## Check your understanding — three problems

1. **Numerical variation.** Rework the example for a 15% increase in its driving thermal difference or equivalent controlling input. State the new units, compare changes as a percentage, and explain whether the relationship is truly linear at this point.
2. **Model selection.** Draw a different physical geometry or flow configuration where this equation might fail. Identify the precise assumption that breaks down, then propose a more suitable balance, correlation or measurement.
3. **Experimental critique.** Design a two-condition laboratory check of the guiding question. Specify a measurable dependent quantity, one plausible confounder, a calibration or repeatability step, and a criterion for recognizing a model–data disagreement.

## Extension: toward real engineering practice

Develop a small calculation sheet or script with named inputs, a units column and explicit warnings about any validity range. Test it at a nominal point and at two extremes, explaining whether the mathematics remains physically credible. Then imagine a colleague changed an input property without documenting temperature or source. Describe exactly how that would affect traceability and how you would reconstruct the decision. Finally propose one material, configuration or instrumentation change that improves thermal performance without adding unacceptable complexity or operating expense.

**Lesson conclusion.** Evaporation, latent heat, and moist-air exchange is useful when the energy pathway, geometry, regime and measurement basis agree. Recalculate when those conditions change; do not use apparent precision to hide uncertainty. Explain the result using a physical picture, not only a number.


---

