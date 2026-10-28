/* OpenSTEM Course Data: Heat Transfer (HTR) */
var COURSE_DATA = {
  "code": "HTR",
  "title": "Heat Transfer",
  "subtitle": "Conduction, Convection, Radiation, Phase Change, Heat Exchangers & Numerical Thermal Modeling",
  "units": [
    {
      "number": 1,
      "unitNumber": 1,
      "title": "Heat Transfer Foundations and Thermal Modeling",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Heat Transfer Foundations and Thermal Modeling.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Heat Transfer Foundations and Thermal Modeling.",
      "sections": [
        {
          "id": "sec-1-1",
          "title": "Thermal energy and temperature",
          "leadSummary": "**Unit 1: Heat Transfer Foundations and Thermal Modeling \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**",
          "content": "<p>**Unit 1: Heat Transfer Foundations and Thermal Modeling \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**</p>"
        },
        {
          "id": "sec-1-2",
          "title": "Conduction, convection, and radiation",
          "leadSummary": "**Unit 1: Heat Transfer Foundations and Thermal Modeling \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**",
          "content": "<p>**Unit 1: Heat Transfer Foundations and Thermal Modeling \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**</p>"
        },
        {
          "id": "sec-1-3",
          "title": "Material properties and temperature dependence",
          "leadSummary": "**Unit 1: Heat Transfer Foundations and Thermal Modeling \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**",
          "content": "<p>**Unit 1: Heat Transfer Foundations and Thermal Modeling \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**</p>"
        },
        {
          "id": "sec-1-4",
          "title": "Conservation of energy for thermal systems",
          "leadSummary": "**Unit 1: Heat Transfer Foundations and Thermal Modeling \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**",
          "content": "<p>**Unit 1: Heat Transfer Foundations and Thermal Modeling \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**</p>"
        },
        {
          "id": "sec-1-5",
          "title": "Thermal boundaries, units, and modeling scope",
          "leadSummary": "**Unit 1: Heat Transfer Foundations and Thermal Modeling \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**",
          "content": "<p>**Unit 1: Heat Transfer Foundations and Thermal Modeling \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-heat-transfer-1-1",
          "title": "Calculation & Verification: Thermal energy and temperature",
          "unit": 1,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Thermal energy and temperature** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Mass 1.4 kg; c=900 J/(kg K); T rises from 293 to 333 K.\n\n**Operation.** Use the relationship `Block heating: \u0394U=mc\u0394T` with all inputs converted to compatible units; the result is **5.04e+04 J**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
        },
        {
          "id": "prob-heat-transfer-1-2",
          "title": "Calculation & Verification: Conduction, convection, and radiation",
          "unit": 1,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Conduction, convection, and radiation** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Convection 5 W; radiation 7 W; no other assumed paths.\n\n**Operation.** Use the relationship `Power partition: Qtotal=Qconv+Qrad` with all inputs converted to compatible units; the result is **12 W**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
        },
        {
          "id": "prob-heat-transfer-1-3",
          "title": "Calculation & Verification: Material properties and temperature dependence",
          "unit": 1,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Material properties and temperature dependence** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** k=200 W/(m K), \u03c1=2700 kg/m\u00b3, c=900 J/(kg K).\n\n**Operation.** Use the relationship `Thermal diffusivity: \u03b1=k/(\u03c1c)` with all inputs converted to compatible units; the result is **8.23e-05 m\u00b2/s**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
        },
        {
          "id": "prob-heat-transfer-1-4",
          "title": "Calculation & Verification: Conservation of energy for thermal systems",
          "unit": 1,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Conservation of energy for thermal systems** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Pin=160 W, heat loss 40 W, mass 2 kg, c=900 J/(kg K).\n\n**Operation.** Use the relationship `Instantaneous rise: dT/dt=(Pin\u2212Ploss)/(mc)` with all inputs converted to compatible units; the result is **0.0667 K/s**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
        },
        {
          "id": "prob-heat-transfer-1-5",
          "title": "Calculation & Verification: Thermal boundaries, units, and modeling scope",
          "unit": 1,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Thermal boundaries, units, and modeling scope** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** h=12 W/(m\u00b2 K), surface 350 K, ambient 300 K.\n\n**Operation.** Use the relationship `Newton-law boundary: q\u2033=h(Ts\u2212T\u221e)` with all inputs converted to compatible units; the result is **600 W/m\u00b2**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
        }
      ]
    },
    {
      "number": 2,
      "unitNumber": 2,
      "title": "Steady Conduction and Thermal Resistance",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Steady Conduction and Thermal Resistance.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Steady Conduction and Thermal Resistance.",
      "sections": [
        {
          "id": "sec-2-1",
          "title": "Fourier law through a plane wall",
          "leadSummary": "**Unit 2: Steady Conduction and Thermal Resistance \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**",
          "content": "<p>**Unit 2: Steady Conduction and Thermal Resistance \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**</p>"
        },
        {
          "id": "sec-2-2",
          "title": "Thermal resistance and multilayer walls",
          "leadSummary": "**Unit 2: Steady Conduction and Thermal Resistance \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**",
          "content": "<p>**Unit 2: Steady Conduction and Thermal Resistance \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**</p>"
        },
        {
          "id": "sec-2-3",
          "title": "Radial conduction in cylinders and spheres",
          "leadSummary": "**Unit 2: Steady Conduction and Thermal Resistance \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**",
          "content": "<p>**Unit 2: Steady Conduction and Thermal Resistance \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**</p>"
        },
        {
          "id": "sec-2-4",
          "title": "Contact resistance and interfacial engineering",
          "leadSummary": "**Unit 2: Steady Conduction and Thermal Resistance \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**",
          "content": "<p>**Unit 2: Steady Conduction and Thermal Resistance \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**</p>"
        },
        {
          "id": "sec-2-5",
          "title": "Extended surfaces and fin efficiency",
          "leadSummary": "**Unit 2: Steady Conduction and Thermal Resistance \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**",
          "content": "<p>**Unit 2: Steady Conduction and Thermal Resistance \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-heat-transfer-2-1",
          "title": "Calculation & Verification: Fourier law through a plane wall",
          "unit": 2,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Fourier law through a plane wall** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** k=0.04 W/(m K), A=2 m\u00b2, \u0394T=25 K, L=0.08 m.\n\n**Operation.** Use the relationship `Plane-wall conduction: Q=kA\u0394T/L` with all inputs converted to compatible units; the result is **25 W**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
        },
        {
          "id": "prob-heat-transfer-2-2",
          "title": "Calculation & Verification: Thermal resistance and multilayer walls",
          "unit": 2,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Thermal resistance and multilayer walls** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** A=1 m\u00b2; two layers L1=0.02 m, k1=0.8 and L2=1 m, k2=0.04.\n\n**Operation.** Use the relationship `Series-wall rate: Q=\u0394T/R` with all inputs converted to compatible units; the result is **0.999 W**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
        },
        {
          "id": "prob-heat-transfer-2-3",
          "title": "Calculation & Verification: Radial conduction in cylinders and spheres",
          "unit": 2,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Radial conduction in cylinders and spheres** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** k=0.05 W/(m K), \u2113=1 m, radii 0.02 and 0.04 m, \u0394T=45 K.\n\n**Operation.** Use the relationship `Radial conduction: Q=2\u03c0k\u2113\u0394T/ln(ro/ri)` with all inputs converted to compatible units; the result is **20.3956 W**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
        },
        {
          "id": "prob-heat-transfer-2-4",
          "title": "Calculation & Verification: Contact resistance and interfacial engineering",
          "unit": 2,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Contact resistance and interfacial engineering** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Q=30 W and thermal contact resistance R=0.35 K/W.\n\n**Operation.** Use the relationship `Contact temperature drop: \u0394T=QR` with all inputs converted to compatible units; the result is **10.5 K**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
        },
        {
          "id": "prob-heat-transfer-2-5",
          "title": "Calculation & Verification: Extended surfaces and fin efficiency",
          "unit": 2,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Extended surfaces and fin efficiency** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** h=18 W/(m\u00b2 K), P=0.04 m, k=180 W/(m K), Ac=0.0001 m\u00b2, L=0.08 m.\n\n**Operation.** Use the relationship `Fin efficiency: \u03b7=tanh(mL)/(mL)` with all inputs converted to compatible units; the result is **0.9226 fraction**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
        }
      ]
    },
    {
      "number": 3,
      "unitNumber": 3,
      "title": "Transient Heat Diffusion and Numerical Methods",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Transient Heat Diffusion and Numerical Methods.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Transient Heat Diffusion and Numerical Methods.",
      "sections": [
        {
          "id": "sec-3-1",
          "title": "Thermal storage and lumped capacitance",
          "leadSummary": "**Unit 3: Transient Heat Diffusion and Numerical Methods \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**",
          "content": "<p>**Unit 3: Transient Heat Diffusion and Numerical Methods \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**</p>"
        },
        {
          "id": "sec-3-2",
          "title": "Biot and Fourier numbers",
          "leadSummary": "**Unit 3: Transient Heat Diffusion and Numerical Methods \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**",
          "content": "<p>**Unit 3: Transient Heat Diffusion and Numerical Methods \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**</p>"
        },
        {
          "id": "sec-3-3",
          "title": "Transient conduction in plane walls",
          "leadSummary": "**Unit 3: Transient Heat Diffusion and Numerical Methods \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**",
          "content": "<p>**Unit 3: Transient Heat Diffusion and Numerical Methods \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**</p>"
        },
        {
          "id": "sec-3-4",
          "title": "Numerical time marching and stability",
          "leadSummary": "**Unit 3: Transient Heat Diffusion and Numerical Methods \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**",
          "content": "<p>**Unit 3: Transient Heat Diffusion and Numerical Methods \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**</p>"
        },
        {
          "id": "sec-3-5",
          "title": "Thermal transients with internal generation",
          "leadSummary": "**Unit 3: Transient Heat Diffusion and Numerical Methods \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**",
          "content": "<p>**Unit 3: Transient Heat Diffusion and Numerical Methods \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-heat-transfer-3-1",
          "title": "Calculation & Verification: Thermal storage and lumped capacitance",
          "unit": 3,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Thermal storage and lumped capacitance** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** T\u221e=300 K, initial excess 70 K; \u03c4=50 s; evaluate at t=50 s.\n\n**Operation.** Use the relationship `Temperature after one time constant` with all inputs converted to compatible units; the result is **325.7516 K**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
        },
        {
          "id": "prob-heat-transfer-3-2",
          "title": "Calculation & Verification: Biot and Fourier numbers",
          "unit": 3,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Biot and Fourier numbers** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** h=20 W/(m\u00b2 K), Lc=0.012 m, k=16 W/(m K).\n\n**Operation.** Use the relationship `Biot number: Bi=hLc/k` with all inputs converted to compatible units; the result is **0.015 dimensionless**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
        },
        {
          "id": "prob-heat-transfer-3-3",
          "title": "Calculation & Verification: Transient conduction in plane walls",
          "unit": 3,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Transient conduction in plane walls** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** \u03b1=1e\u22125 m\u00b2/s, t=320 s, Lc=0.02 m.\n\n**Operation.** Use the relationship `Fourier number: Fo=\u03b1t/Lc\u00b2` with all inputs converted to compatible units; the result is **8 dimensionless**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
        },
        {
          "id": "prob-heat-transfer-3-4",
          "title": "Calculation & Verification: Numerical time marching and stability",
          "unit": 3,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Numerical time marching and stability** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** 1D uniform grid spacing \u0394x=0.001 m, \u03b1=1e\u22125 m\u00b2/s.\n\n**Operation.** Use the relationship `Explicit stability upper timestep` with all inputs converted to compatible units; the result is **0.05 s**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
        },
        {
          "id": "prob-heat-transfer-3-5",
          "title": "Calculation & Verification: Thermal transients with internal generation",
          "unit": 3,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Thermal transients with internal generation** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Volumetric source 50,000 W/m\u00b3 in volume 0.002 m\u00b3.\n\n**Operation.** Use the relationship `Volumetric heat rate: Q=q\u2034V` with all inputs converted to compatible units; the result is **100 W**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
        }
      ]
    },
    {
      "number": 4,
      "unitNumber": 4,
      "title": "Convection and Boundary-Layer Heat Transfer",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Convection and Boundary-Layer Heat Transfer.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Convection and Boundary-Layer Heat Transfer.",
      "sections": [
        {
          "id": "sec-4-1",
          "title": "Convection and thermal boundary layers",
          "leadSummary": "**Unit 4: Convection and Boundary-Layer Heat Transfer \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**",
          "content": "<p>**Unit 4: Convection and Boundary-Layer Heat Transfer \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**</p>"
        },
        {
          "id": "sec-4-2",
          "title": "Laminar flow over a flat plate",
          "leadSummary": "**Unit 4: Convection and Boundary-Layer Heat Transfer \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**",
          "content": "<p>**Unit 4: Convection and Boundary-Layer Heat Transfer \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**</p>"
        },
        {
          "id": "sec-4-3",
          "title": "External crossflow over cylinders and spheres",
          "leadSummary": "**Unit 4: Convection and Boundary-Layer Heat Transfer \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**",
          "content": "<p>**Unit 4: Convection and Boundary-Layer Heat Transfer \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**</p>"
        },
        {
          "id": "sec-4-4",
          "title": "Fully developed internal laminar convection",
          "leadSummary": "**Unit 4: Convection and Boundary-Layer Heat Transfer \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**",
          "content": "<p>**Unit 4: Convection and Boundary-Layer Heat Transfer \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**</p>"
        },
        {
          "id": "sec-4-5",
          "title": "Turbulent internal convection and hydraulic tradeoffs",
          "leadSummary": "**Unit 4: Convection and Boundary-Layer Heat Transfer \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**",
          "content": "<p>**Unit 4: Convection and Boundary-Layer Heat Transfer \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-heat-transfer-4-1",
          "title": "Calculation & Verification: Convection and thermal boundary layers",
          "unit": 4,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Convection and thermal boundary layers** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** h=12 W/(m\u00b2 K), A=2 m\u00b2, temperature excess 50 K.\n\n**Operation.** Use the relationship `Convective duty: Q=hA\u0394T` with all inputs converted to compatible units; the result is **1200 W**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
        },
        {
          "id": "prob-heat-transfer-4-2",
          "title": "Calculation & Verification: Laminar flow over a flat plate",
          "unit": 4,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Laminar flow over a flat plate** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Air \u03c1=1.2 kg/m\u00b3, \u03bc=1.8e\u22125 Pa\u00b7s; V=3 m/s and L=0.3 m.\n\n**Operation.** Use the relationship `Plate Reynolds number: Re=\u03c1VL/\u03bc` with all inputs converted to compatible units; the result is **6e+04 dimensionless**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
        },
        {
          "id": "prob-heat-transfer-4-3",
          "title": "Calculation & Verification: External crossflow over cylinders and spheres",
          "unit": 4,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **External crossflow over cylinders and spheres** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Measured illustrative h=40 W/(m\u00b2 K); D=0.025 m; kf=0.026 W/(m K).\n\n**Operation.** Use the relationship `Cylinder Nusselt number: Nu=hD/kf` with all inputs converted to compatible units; the result is **38.4615 dimensionless**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
        },
        {
          "id": "prob-heat-transfer-4-4",
          "title": "Calculation & Verification: Fully developed internal laminar convection",
          "unit": 4,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Fully developed internal laminar convection** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Nu=3.66, tube diameter 0.02 m, fluid k=0.6 W/(m K).\n\n**Operation.** Use the relationship `Ideal laminar fully developed h=Nu k/D` with all inputs converted to compatible units; the result is **109.8 W/(m\u00b2 K)**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
        },
        {
          "id": "prob-heat-transfer-4-5",
          "title": "Calculation & Verification: Turbulent internal convection and hydraulic tradeoffs",
          "unit": 4,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Turbulent internal convection and hydraulic tradeoffs** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Re=35,000; Pr=3; fluid k=0.6 W/(m K), D=0.02 m.\n\n**Operation.** Use the relationship `Turbulent-tube h via Dittus\u2013Boelter` with all inputs converted to compatible units; the result is **4,623.2995 W/(m\u00b2 K)**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
        }
      ]
    },
    {
      "number": 5,
      "unitNumber": 5,
      "title": "Boiling, Condensation, and Phase-Change Heat Transfer",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Boiling, Condensation, and Phase-Change Heat Transfer.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Boiling, Condensation, and Phase-Change Heat Transfer.",
      "sections": [
        {
          "id": "sec-5-1",
          "title": "Nucleate boiling and boiling curves",
          "leadSummary": "**Unit 5: Boiling, Condensation, and Phase-Change Heat Transfer \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**",
          "content": "<p>**Unit 5: Boiling, Condensation, and Phase-Change Heat Transfer \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**</p>"
        },
        {
          "id": "sec-5-2",
          "title": "Critical heat flux and boiling safety",
          "leadSummary": "**Unit 5: Boiling, Condensation, and Phase-Change Heat Transfer \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**",
          "content": "<p>**Unit 5: Boiling, Condensation, and Phase-Change Heat Transfer \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**</p>"
        },
        {
          "id": "sec-5-3",
          "title": "Filmwise and dropwise condensation",
          "leadSummary": "**Unit 5: Boiling, Condensation, and Phase-Change Heat Transfer \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**",
          "content": "<p>**Unit 5: Boiling, Condensation, and Phase-Change Heat Transfer \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**</p>"
        },
        {
          "id": "sec-5-4",
          "title": "Solidification and melting",
          "leadSummary": "**Unit 5: Boiling, Condensation, and Phase-Change Heat Transfer \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**",
          "content": "<p>**Unit 5: Boiling, Condensation, and Phase-Change Heat Transfer \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**</p>"
        },
        {
          "id": "sec-5-5",
          "title": "Evaporation, latent heat, and moist-air exchange",
          "leadSummary": "**Unit 5: Boiling, Condensation, and Phase-Change Heat Transfer \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**",
          "content": "<p>**Unit 5: Boiling, Condensation, and Phase-Change Heat Transfer \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-heat-transfer-5-1",
          "title": "Calculation & Verification: Nucleate boiling and boiling curves",
          "unit": 5,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Nucleate boiling and boiling curves** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Hypothetical local heat flux 4500 W/m\u00b2 over area 0.03 m\u00b2.\n\n**Operation.** Use the relationship `Local boiling duty: Q=q\u2033A` with all inputs converted to compatible units; the result is **135 W**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
        },
        {
          "id": "prob-heat-transfer-5-2",
          "title": "Calculation & Verification: Critical heat flux and boiling safety",
          "unit": 5,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Critical heat flux and boiling safety** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Nominal 90 kW/m\u00b2 versus illustrative threshold 120 kW/m\u00b2; NOT an operating safety criterion.\n\n**Operation.** Use the relationship `CHF threshold comparison: qnominal/qCHF` with all inputs converted to compatible units; the result is **0.75 fraction**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
        },
        {
          "id": "prob-heat-transfer-5-3",
          "title": "Calculation & Verification: Filmwise and dropwise condensation",
          "unit": 5,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Filmwise and dropwise condensation** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Assumed U=250 W/(m\u00b2 K), A=2 m\u00b2 and representative \u0394T=20 K.\n\n**Operation.** Use the relationship `Overall condenser: Q=UA\u0394T` with all inputs converted to compatible units; the result is **1e+04 W**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
        },
        {
          "id": "prob-heat-transfer-5-4",
          "title": "Calculation & Verification: Solidification and melting",
          "unit": 5,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Solidification and melting** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** k=2.2 W/(m K); \u0394T=12 K; t=300 s; \u03c1=920 kg/m\u00b3; Lf=334 kJ/kg.\n\n**Operation.** Use the relationship `Quasi-steady front location` with all inputs converted to compatible units; the result is **0.0072 m**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
        },
        {
          "id": "prob-heat-transfer-5-5",
          "title": "Calculation & Verification: Evaporation, latent heat, and moist-air exchange",
          "unit": 5,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Evaporation, latent heat, and moist-air exchange** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Evaporated water mass 0.01 kg; illustrative hfg=2.4 MJ/kg.\n\n**Operation.** Use the relationship `Latent cooling: Q=m hfg` with all inputs converted to compatible units; the result is **2.4e+04 J**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
        }
      ]
    },
    {
      "number": 6,
      "unitNumber": 6,
      "title": "Thermal Radiation and Enclosure Exchange",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Thermal Radiation and Enclosure Exchange.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Thermal Radiation and Enclosure Exchange.",
      "sections": [
        {
          "id": "sec-6-1",
          "title": "Blackbody emission and absolute temperature",
          "leadSummary": "**Unit 6: Thermal Radiation and Enclosure Exchange \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**",
          "content": "<p>**Unit 6: Thermal Radiation and Enclosure Exchange \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**</p>"
        },
        {
          "id": "sec-6-2",
          "title": "Real-surface emissivity and spectral effects",
          "leadSummary": "**Unit 6: Thermal Radiation and Enclosure Exchange \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**",
          "content": "<p>**Unit 6: Thermal Radiation and Enclosure Exchange \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**</p>"
        },
        {
          "id": "sec-6-3",
          "title": "View factors and enclosure exchange",
          "leadSummary": "**Unit 6: Thermal Radiation and Enclosure Exchange \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**",
          "content": "<p>**Unit 6: Thermal Radiation and Enclosure Exchange \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**</p>"
        },
        {
          "id": "sec-6-4",
          "title": "Radiation shields and multilayer insulation",
          "leadSummary": "**Unit 6: Thermal Radiation and Enclosure Exchange \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**",
          "content": "<p>**Unit 6: Thermal Radiation and Enclosure Exchange \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**</p>"
        },
        {
          "id": "sec-6-5",
          "title": "Solar absorption and combined-mode heat loss",
          "leadSummary": "**Unit 6: Thermal Radiation and Enclosure Exchange \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**",
          "content": "<p>**Unit 6: Thermal Radiation and Enclosure Exchange \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-heat-transfer-6-1",
          "title": "Calculation & Verification: Blackbody emission and absolute temperature",
          "unit": 6,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Blackbody emission and absolute temperature** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Hot surface 400 K, large black surroundings 300 K.\n\n**Operation.** Use the relationship `Net blackbody exchange per unit area` with all inputs converted to compatible units; the result is **992.3155 W/m\u00b2**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
        },
        {
          "id": "prob-heat-transfer-6-2",
          "title": "Calculation & Verification: Real-surface emissivity and spectral effects",
          "unit": 6,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Real-surface emissivity and spectral effects** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Emissivity 0.85; blackbody reference 400 K; emitted rather than net power.\n\n**Operation.** Use the relationship `Gray-surface emitted power per area` with all inputs converted to compatible units; the result is **1,233.8735 W/m\u00b2**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
        },
        {
          "id": "prob-heat-transfer-6-3",
          "title": "Calculation & Verification: View factors and enclosure exchange",
          "unit": 6,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **View factors and enclosure exchange** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** A1=2 m\u00b2; A2=5 m\u00b2; F12=0.4.\n\n**Operation.** Use the relationship `View-factor reciprocity: F21=A1F12/A2` with all inputs converted to compatible units; the result is **0.16 dimensionless**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
        },
        {
          "id": "prob-heat-transfer-6-4",
          "title": "Calculation & Verification: Radiation shields and multilayer insulation",
          "unit": 6,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Radiation shields and multilayer insulation** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Large diffuse-gray plates at 500 K and 300 K with emissivities 0.7 and 0.8.\n\n**Operation.** Use the relationship `Two-facing-plate radiative flux` with all inputs converted to compatible units; the result is **1,837.6839 W/m\u00b2**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
        },
        {
          "id": "prob-heat-transfer-6-5",
          "title": "Calculation & Verification: Solar absorption and combined-mode heat loss",
          "unit": 6,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Solar absorption and combined-mode heat loss** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Solar G=800 W/m\u00b2, absorptivity 0.7, \u03b5=0.9, Ts=350 K, Tsur=T\u221e=300 K, h=8.\n\n**Operation.** Use the relationship `Combined surface net gain` with all inputs converted to compatible units; the result is **-192.4492 W/m\u00b2**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
        }
      ]
    },
    {
      "number": 7,
      "unitNumber": 7,
      "title": "Heat Exchangers and Integrated Thermal Systems",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Heat Exchangers and Integrated Thermal Systems.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Heat Exchangers and Integrated Thermal Systems.",
      "sections": [
        {
          "id": "sec-7-1",
          "title": "Heat exchanger architectures and effectiveness",
          "leadSummary": "**Unit 7: Heat Exchangers and Integrated Thermal Systems \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**",
          "content": "<p>**Unit 7: Heat Exchangers and Integrated Thermal Systems \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**</p>"
        },
        {
          "id": "sec-7-2",
          "title": "Log-mean temperature difference",
          "leadSummary": "**Unit 7: Heat Exchangers and Integrated Thermal Systems \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**",
          "content": "<p>**Unit 7: Heat Exchangers and Integrated Thermal Systems \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**</p>"
        },
        {
          "id": "sec-7-3",
          "title": "Effectiveness\u2013NTU analysis",
          "leadSummary": "**Unit 7: Heat Exchangers and Integrated Thermal Systems \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**",
          "content": "<p>**Unit 7: Heat Exchangers and Integrated Thermal Systems \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**</p>"
        },
        {
          "id": "sec-7-4",
          "title": "Fouling and overall thermal resistance",
          "leadSummary": "**Unit 7: Heat Exchangers and Integrated Thermal Systems \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**",
          "content": "<p>**Unit 7: Heat Exchangers and Integrated Thermal Systems \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**</p>"
        },
        {
          "id": "sec-7-5",
          "title": "Thermal systems: heat sinks, heat pumps, and energy efficiency",
          "leadSummary": "**Unit 7: Heat Exchangers and Integrated Thermal Systems \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**",
          "content": "<p>**Unit 7: Heat Exchangers and Integrated Thermal Systems \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-heat-transfer-7-1",
          "title": "Calculation & Verification: Heat exchanger architectures and effectiveness",
          "unit": 7,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Heat exchanger architectures and effectiveness** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Mass flow 0.2 kg/s, cp=4000 J/(kg K), hot-stream drop 15 K.\n\n**Operation.** Use the relationship `Measured hot-stream duty: Q=\u1e41cp\u0394T` with all inputs converted to compatible units; the result is **1.2e+04 W**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
        },
        {
          "id": "prob-heat-transfer-7-2",
          "title": "Calculation & Verification: Log-mean temperature difference",
          "unit": 7,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Log-mean temperature difference** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Positive terminal differences \u0394T1=40 K, \u0394T2=18 K.\n\n**Operation.** Use the relationship `LMTD for two terminal differences` with all inputs converted to compatible units; the result is **27.5514 K**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
        },
        {
          "id": "prob-heat-transfer-7-3",
          "title": "Calculation & Verification: Effectiveness\u2013NTU analysis",
          "unit": 7,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Effectiveness\u2013NTU analysis** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Counterflow single-pass, NTU=1.5, Cr=0.5.\n\n**Operation.** Use the relationship `Counterflow effectiveness at NTU=1.5, Cr=0.5` with all inputs converted to compatible units; the result is **0.6908 fraction**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
        },
        {
          "id": "prob-heat-transfer-7-4",
          "title": "Calculation & Verification: Fouling and overall thermal resistance",
          "unit": 7,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Fouling and overall thermal resistance** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** hi=400, ho=250 W/(m\u00b2 K); wall \u03b4=0.003 m, k=15; total fouling factor 0.0005 m\u00b2K/W.\n\n**Operation.** Use the relationship `Common-area resistance U` with all inputs converted to compatible units; the result is **138.8889 W/(m\u00b2 K)**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
        },
        {
          "id": "prob-heat-transfer-7-5",
          "title": "Calculation & Verification: Thermal systems: heat sinks, heat pumps, and energy efficiency",
          "unit": 7,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Thermal systems: heat sinks, heat pumps, and energy efficiency** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Thermal power 45 W, overall junction-to-ambient resistance 0.6 K/W.\n\n**Operation.** Use the relationship `Heat-sink temperature increase` with all inputs converted to compatible units; the result is **27 K**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
        }
      ]
    },
    {
      "number": 8,
      "unitNumber": 8,
      "title": "Measurement, Computation, and Engineering Design",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Measurement, Computation, and Engineering Design.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Measurement, Computation, and Engineering Design.",
      "sections": [
        {
          "id": "sec-8-1",
          "title": "Temperature sensors and calibration",
          "leadSummary": "**Unit 8: Measurement, Computation, and Engineering Design \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**",
          "content": "<p>**Unit 8: Measurement, Computation, and Engineering Design \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**</p>"
        },
        {
          "id": "sec-8-2",
          "title": "Heat-flux measurement and inverse problems",
          "leadSummary": "**Unit 8: Measurement, Computation, and Engineering Design \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**",
          "content": "<p>**Unit 8: Measurement, Computation, and Engineering Design \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**</p>"
        },
        {
          "id": "sec-8-3",
          "title": "Finite-volume and finite-element thermal models",
          "leadSummary": "**Unit 8: Measurement, Computation, and Engineering Design \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**",
          "content": "<p>**Unit 8: Measurement, Computation, and Engineering Design \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**</p>"
        },
        {
          "id": "sec-8-4",
          "title": "Uncertainty, verification and model validation",
          "leadSummary": "**Unit 8: Measurement, Computation, and Engineering Design \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**",
          "content": "<p>**Unit 8: Measurement, Computation, and Engineering Design \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**</p>"
        },
        {
          "id": "sec-8-5",
          "title": "Integrated design: thermal control of equipment",
          "leadSummary": "**Unit 8: Measurement, Computation, and Engineering Design \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**",
          "content": "<p>**Unit 8: Measurement, Computation, and Engineering Design \u00b7 Suggested workload 90\u2013130 minutes \u00b7 Educational draft**</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-heat-transfer-8-1",
          "title": "Calculation & Verification: Temperature sensors and calibration",
          "unit": 8,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Temperature sensors and calibration** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Sensor reads 49 \u00b0C with linear calibration Tcorrected=1.02 Treading\u22120.5.\n\n**Operation.** Use the relationship `Two-point sensor correction` with all inputs converted to compatible units; the result is **49.48 \u00b0C**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
        },
        {
          "id": "prob-heat-transfer-8-2",
          "title": "Calculation & Verification: Heat-flux measurement and inverse problems",
          "unit": 8,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Heat-flux measurement and inverse problems** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Constant k=1 W/(m K), two temperatures 370 K and 350 K separated by 0.02 m along increasing x.\n\n**Operation.** Use the relationship `Embedded-sensor estimated flux` with all inputs converted to compatible units; the result is **1,000 W/m\u00b2**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
        },
        {
          "id": "prob-heat-transfer-8-3",
          "title": "Calculation & Verification: Finite-volume and finite-element thermal models",
          "unit": 8,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Finite-volume and finite-element thermal models** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Constant k=10 W/(m K), area 1 m\u00b2, total length 0.1 m, \u0394T=20 K.\n\n**Operation.** Use the relationship `Finite-volume linear slab reference` with all inputs converted to compatible units; the result is **2,000 W**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
        },
        {
          "id": "prob-heat-transfer-8-4",
          "title": "Calculation & Verification: Uncertainty, verification and model validation",
          "unit": 8,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Uncertainty, verification and model validation** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Independent k relative error 0.004/0.04, thickness error 0.005/0.1, other uncertainty neglected.\n\n**Operation.** Use the relationship `Relative combined uncertainty` with all inputs converted to compatible units; the result is **0.1118 fraction**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
        },
        {
          "id": "prob-heat-transfer-8-5",
          "title": "Calculation & Verification: Integrated design: thermal control of equipment",
          "unit": 8,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Integrated design: thermal control of equipment** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Allowable temperature rise 32 K for dissipation 80 W.\n\n**Operation.** Use the relationship `Target resistance: R\u03b8,max=\u0394Tallowed/Q` with all inputs converted to compatible units; the result is **0.4 K/W**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
        }
      ]
    }
  ],
  "problems": [
    {
      "id": "prob-heat-transfer-1-1",
      "title": "Calculation & Verification: Thermal energy and temperature",
      "unit": 1,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Thermal energy and temperature** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Mass 1.4 kg; c=900 J/(kg K); T rises from 293 to 333 K.\n\n**Operation.** Use the relationship `Block heating: \u0394U=mc\u0394T` with all inputs converted to compatible units; the result is **5.04e+04 J**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
    },
    {
      "id": "prob-heat-transfer-1-2",
      "title": "Calculation & Verification: Conduction, convection, and radiation",
      "unit": 1,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Conduction, convection, and radiation** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Convection 5 W; radiation 7 W; no other assumed paths.\n\n**Operation.** Use the relationship `Power partition: Qtotal=Qconv+Qrad` with all inputs converted to compatible units; the result is **12 W**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
    },
    {
      "id": "prob-heat-transfer-1-3",
      "title": "Calculation & Verification: Material properties and temperature dependence",
      "unit": 1,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Material properties and temperature dependence** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** k=200 W/(m K), \u03c1=2700 kg/m\u00b3, c=900 J/(kg K).\n\n**Operation.** Use the relationship `Thermal diffusivity: \u03b1=k/(\u03c1c)` with all inputs converted to compatible units; the result is **8.23e-05 m\u00b2/s**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
    },
    {
      "id": "prob-heat-transfer-1-4",
      "title": "Calculation & Verification: Conservation of energy for thermal systems",
      "unit": 1,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Conservation of energy for thermal systems** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Pin=160 W, heat loss 40 W, mass 2 kg, c=900 J/(kg K).\n\n**Operation.** Use the relationship `Instantaneous rise: dT/dt=(Pin\u2212Ploss)/(mc)` with all inputs converted to compatible units; the result is **0.0667 K/s**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
    },
    {
      "id": "prob-heat-transfer-1-5",
      "title": "Calculation & Verification: Thermal boundaries, units, and modeling scope",
      "unit": 1,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Thermal boundaries, units, and modeling scope** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** h=12 W/(m\u00b2 K), surface 350 K, ambient 300 K.\n\n**Operation.** Use the relationship `Newton-law boundary: q\u2033=h(Ts\u2212T\u221e)` with all inputs converted to compatible units; the result is **600 W/m\u00b2**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
    },
    {
      "id": "prob-heat-transfer-2-1",
      "title": "Calculation & Verification: Fourier law through a plane wall",
      "unit": 2,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Fourier law through a plane wall** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** k=0.04 W/(m K), A=2 m\u00b2, \u0394T=25 K, L=0.08 m.\n\n**Operation.** Use the relationship `Plane-wall conduction: Q=kA\u0394T/L` with all inputs converted to compatible units; the result is **25 W**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
    },
    {
      "id": "prob-heat-transfer-2-2",
      "title": "Calculation & Verification: Thermal resistance and multilayer walls",
      "unit": 2,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Thermal resistance and multilayer walls** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** A=1 m\u00b2; two layers L1=0.02 m, k1=0.8 and L2=1 m, k2=0.04.\n\n**Operation.** Use the relationship `Series-wall rate: Q=\u0394T/R` with all inputs converted to compatible units; the result is **0.999 W**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
    },
    {
      "id": "prob-heat-transfer-2-3",
      "title": "Calculation & Verification: Radial conduction in cylinders and spheres",
      "unit": 2,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Radial conduction in cylinders and spheres** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** k=0.05 W/(m K), \u2113=1 m, radii 0.02 and 0.04 m, \u0394T=45 K.\n\n**Operation.** Use the relationship `Radial conduction: Q=2\u03c0k\u2113\u0394T/ln(ro/ri)` with all inputs converted to compatible units; the result is **20.3956 W**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
    },
    {
      "id": "prob-heat-transfer-2-4",
      "title": "Calculation & Verification: Contact resistance and interfacial engineering",
      "unit": 2,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Contact resistance and interfacial engineering** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Q=30 W and thermal contact resistance R=0.35 K/W.\n\n**Operation.** Use the relationship `Contact temperature drop: \u0394T=QR` with all inputs converted to compatible units; the result is **10.5 K**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
    },
    {
      "id": "prob-heat-transfer-2-5",
      "title": "Calculation & Verification: Extended surfaces and fin efficiency",
      "unit": 2,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Extended surfaces and fin efficiency** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** h=18 W/(m\u00b2 K), P=0.04 m, k=180 W/(m K), Ac=0.0001 m\u00b2, L=0.08 m.\n\n**Operation.** Use the relationship `Fin efficiency: \u03b7=tanh(mL)/(mL)` with all inputs converted to compatible units; the result is **0.9226 fraction**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
    },
    {
      "id": "prob-heat-transfer-3-1",
      "title": "Calculation & Verification: Thermal storage and lumped capacitance",
      "unit": 3,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Thermal storage and lumped capacitance** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** T\u221e=300 K, initial excess 70 K; \u03c4=50 s; evaluate at t=50 s.\n\n**Operation.** Use the relationship `Temperature after one time constant` with all inputs converted to compatible units; the result is **325.7516 K**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
    },
    {
      "id": "prob-heat-transfer-3-2",
      "title": "Calculation & Verification: Biot and Fourier numbers",
      "unit": 3,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Biot and Fourier numbers** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** h=20 W/(m\u00b2 K), Lc=0.012 m, k=16 W/(m K).\n\n**Operation.** Use the relationship `Biot number: Bi=hLc/k` with all inputs converted to compatible units; the result is **0.015 dimensionless**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
    },
    {
      "id": "prob-heat-transfer-3-3",
      "title": "Calculation & Verification: Transient conduction in plane walls",
      "unit": 3,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Transient conduction in plane walls** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** \u03b1=1e\u22125 m\u00b2/s, t=320 s, Lc=0.02 m.\n\n**Operation.** Use the relationship `Fourier number: Fo=\u03b1t/Lc\u00b2` with all inputs converted to compatible units; the result is **8 dimensionless**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
    },
    {
      "id": "prob-heat-transfer-3-4",
      "title": "Calculation & Verification: Numerical time marching and stability",
      "unit": 3,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Numerical time marching and stability** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** 1D uniform grid spacing \u0394x=0.001 m, \u03b1=1e\u22125 m\u00b2/s.\n\n**Operation.** Use the relationship `Explicit stability upper timestep` with all inputs converted to compatible units; the result is **0.05 s**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
    },
    {
      "id": "prob-heat-transfer-3-5",
      "title": "Calculation & Verification: Thermal transients with internal generation",
      "unit": 3,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Thermal transients with internal generation** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Volumetric source 50,000 W/m\u00b3 in volume 0.002 m\u00b3.\n\n**Operation.** Use the relationship `Volumetric heat rate: Q=q\u2034V` with all inputs converted to compatible units; the result is **100 W**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
    },
    {
      "id": "prob-heat-transfer-4-1",
      "title": "Calculation & Verification: Convection and thermal boundary layers",
      "unit": 4,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Convection and thermal boundary layers** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** h=12 W/(m\u00b2 K), A=2 m\u00b2, temperature excess 50 K.\n\n**Operation.** Use the relationship `Convective duty: Q=hA\u0394T` with all inputs converted to compatible units; the result is **1200 W**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
    },
    {
      "id": "prob-heat-transfer-4-2",
      "title": "Calculation & Verification: Laminar flow over a flat plate",
      "unit": 4,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Laminar flow over a flat plate** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Air \u03c1=1.2 kg/m\u00b3, \u03bc=1.8e\u22125 Pa\u00b7s; V=3 m/s and L=0.3 m.\n\n**Operation.** Use the relationship `Plate Reynolds number: Re=\u03c1VL/\u03bc` with all inputs converted to compatible units; the result is **6e+04 dimensionless**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
    },
    {
      "id": "prob-heat-transfer-4-3",
      "title": "Calculation & Verification: External crossflow over cylinders and spheres",
      "unit": 4,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **External crossflow over cylinders and spheres** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Measured illustrative h=40 W/(m\u00b2 K); D=0.025 m; kf=0.026 W/(m K).\n\n**Operation.** Use the relationship `Cylinder Nusselt number: Nu=hD/kf` with all inputs converted to compatible units; the result is **38.4615 dimensionless**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
    },
    {
      "id": "prob-heat-transfer-4-4",
      "title": "Calculation & Verification: Fully developed internal laminar convection",
      "unit": 4,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Fully developed internal laminar convection** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Nu=3.66, tube diameter 0.02 m, fluid k=0.6 W/(m K).\n\n**Operation.** Use the relationship `Ideal laminar fully developed h=Nu k/D` with all inputs converted to compatible units; the result is **109.8 W/(m\u00b2 K)**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
    },
    {
      "id": "prob-heat-transfer-4-5",
      "title": "Calculation & Verification: Turbulent internal convection and hydraulic tradeoffs",
      "unit": 4,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Turbulent internal convection and hydraulic tradeoffs** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Re=35,000; Pr=3; fluid k=0.6 W/(m K), D=0.02 m.\n\n**Operation.** Use the relationship `Turbulent-tube h via Dittus\u2013Boelter` with all inputs converted to compatible units; the result is **4,623.2995 W/(m\u00b2 K)**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
    },
    {
      "id": "prob-heat-transfer-5-1",
      "title": "Calculation & Verification: Nucleate boiling and boiling curves",
      "unit": 5,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Nucleate boiling and boiling curves** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Hypothetical local heat flux 4500 W/m\u00b2 over area 0.03 m\u00b2.\n\n**Operation.** Use the relationship `Local boiling duty: Q=q\u2033A` with all inputs converted to compatible units; the result is **135 W**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
    },
    {
      "id": "prob-heat-transfer-5-2",
      "title": "Calculation & Verification: Critical heat flux and boiling safety",
      "unit": 5,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Critical heat flux and boiling safety** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Nominal 90 kW/m\u00b2 versus illustrative threshold 120 kW/m\u00b2; NOT an operating safety criterion.\n\n**Operation.** Use the relationship `CHF threshold comparison: qnominal/qCHF` with all inputs converted to compatible units; the result is **0.75 fraction**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
    },
    {
      "id": "prob-heat-transfer-5-3",
      "title": "Calculation & Verification: Filmwise and dropwise condensation",
      "unit": 5,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Filmwise and dropwise condensation** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Assumed U=250 W/(m\u00b2 K), A=2 m\u00b2 and representative \u0394T=20 K.\n\n**Operation.** Use the relationship `Overall condenser: Q=UA\u0394T` with all inputs converted to compatible units; the result is **1e+04 W**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
    },
    {
      "id": "prob-heat-transfer-5-4",
      "title": "Calculation & Verification: Solidification and melting",
      "unit": 5,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Solidification and melting** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** k=2.2 W/(m K); \u0394T=12 K; t=300 s; \u03c1=920 kg/m\u00b3; Lf=334 kJ/kg.\n\n**Operation.** Use the relationship `Quasi-steady front location` with all inputs converted to compatible units; the result is **0.0072 m**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
    },
    {
      "id": "prob-heat-transfer-5-5",
      "title": "Calculation & Verification: Evaporation, latent heat, and moist-air exchange",
      "unit": 5,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Evaporation, latent heat, and moist-air exchange** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Evaporated water mass 0.01 kg; illustrative hfg=2.4 MJ/kg.\n\n**Operation.** Use the relationship `Latent cooling: Q=m hfg` with all inputs converted to compatible units; the result is **2.4e+04 J**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
    },
    {
      "id": "prob-heat-transfer-6-1",
      "title": "Calculation & Verification: Blackbody emission and absolute temperature",
      "unit": 6,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Blackbody emission and absolute temperature** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Hot surface 400 K, large black surroundings 300 K.\n\n**Operation.** Use the relationship `Net blackbody exchange per unit area` with all inputs converted to compatible units; the result is **992.3155 W/m\u00b2**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
    },
    {
      "id": "prob-heat-transfer-6-2",
      "title": "Calculation & Verification: Real-surface emissivity and spectral effects",
      "unit": 6,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Real-surface emissivity and spectral effects** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Emissivity 0.85; blackbody reference 400 K; emitted rather than net power.\n\n**Operation.** Use the relationship `Gray-surface emitted power per area` with all inputs converted to compatible units; the result is **1,233.8735 W/m\u00b2**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
    },
    {
      "id": "prob-heat-transfer-6-3",
      "title": "Calculation & Verification: View factors and enclosure exchange",
      "unit": 6,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **View factors and enclosure exchange** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** A1=2 m\u00b2; A2=5 m\u00b2; F12=0.4.\n\n**Operation.** Use the relationship `View-factor reciprocity: F21=A1F12/A2` with all inputs converted to compatible units; the result is **0.16 dimensionless**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
    },
    {
      "id": "prob-heat-transfer-6-4",
      "title": "Calculation & Verification: Radiation shields and multilayer insulation",
      "unit": 6,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Radiation shields and multilayer insulation** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Large diffuse-gray plates at 500 K and 300 K with emissivities 0.7 and 0.8.\n\n**Operation.** Use the relationship `Two-facing-plate radiative flux` with all inputs converted to compatible units; the result is **1,837.6839 W/m\u00b2**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
    },
    {
      "id": "prob-heat-transfer-6-5",
      "title": "Calculation & Verification: Solar absorption and combined-mode heat loss",
      "unit": 6,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Solar absorption and combined-mode heat loss** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Solar G=800 W/m\u00b2, absorptivity 0.7, \u03b5=0.9, Ts=350 K, Tsur=T\u221e=300 K, h=8.\n\n**Operation.** Use the relationship `Combined surface net gain` with all inputs converted to compatible units; the result is **-192.4492 W/m\u00b2**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
    },
    {
      "id": "prob-heat-transfer-7-1",
      "title": "Calculation & Verification: Heat exchanger architectures and effectiveness",
      "unit": 7,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Heat exchanger architectures and effectiveness** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Mass flow 0.2 kg/s, cp=4000 J/(kg K), hot-stream drop 15 K.\n\n**Operation.** Use the relationship `Measured hot-stream duty: Q=\u1e41cp\u0394T` with all inputs converted to compatible units; the result is **1.2e+04 W**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
    },
    {
      "id": "prob-heat-transfer-7-2",
      "title": "Calculation & Verification: Log-mean temperature difference",
      "unit": 7,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Log-mean temperature difference** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Positive terminal differences \u0394T1=40 K, \u0394T2=18 K.\n\n**Operation.** Use the relationship `LMTD for two terminal differences` with all inputs converted to compatible units; the result is **27.5514 K**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
    },
    {
      "id": "prob-heat-transfer-7-3",
      "title": "Calculation & Verification: Effectiveness\u2013NTU analysis",
      "unit": 7,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Effectiveness\u2013NTU analysis** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Counterflow single-pass, NTU=1.5, Cr=0.5.\n\n**Operation.** Use the relationship `Counterflow effectiveness at NTU=1.5, Cr=0.5` with all inputs converted to compatible units; the result is **0.6908 fraction**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
    },
    {
      "id": "prob-heat-transfer-7-4",
      "title": "Calculation & Verification: Fouling and overall thermal resistance",
      "unit": 7,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Fouling and overall thermal resistance** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** hi=400, ho=250 W/(m\u00b2 K); wall \u03b4=0.003 m, k=15; total fouling factor 0.0005 m\u00b2K/W.\n\n**Operation.** Use the relationship `Common-area resistance U` with all inputs converted to compatible units; the result is **138.8889 W/(m\u00b2 K)**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
    },
    {
      "id": "prob-heat-transfer-7-5",
      "title": "Calculation & Verification: Thermal systems: heat sinks, heat pumps, and energy efficiency",
      "unit": 7,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Thermal systems: heat sinks, heat pumps, and energy efficiency** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Thermal power 45 W, overall junction-to-ambient resistance 0.6 K/W.\n\n**Operation.** Use the relationship `Heat-sink temperature increase` with all inputs converted to compatible units; the result is **27 K**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
    },
    {
      "id": "prob-heat-transfer-8-1",
      "title": "Calculation & Verification: Temperature sensors and calibration",
      "unit": 8,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Temperature sensors and calibration** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Sensor reads 49 \u00b0C with linear calibration Tcorrected=1.02 Treading\u22120.5.\n\n**Operation.** Use the relationship `Two-point sensor correction` with all inputs converted to compatible units; the result is **49.48 \u00b0C**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
    },
    {
      "id": "prob-heat-transfer-8-2",
      "title": "Calculation & Verification: Heat-flux measurement and inverse problems",
      "unit": 8,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Heat-flux measurement and inverse problems** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Constant k=1 W/(m K), two temperatures 370 K and 350 K separated by 0.02 m along increasing x.\n\n**Operation.** Use the relationship `Embedded-sensor estimated flux` with all inputs converted to compatible units; the result is **1,000 W/m\u00b2**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
    },
    {
      "id": "prob-heat-transfer-8-3",
      "title": "Calculation & Verification: Finite-volume and finite-element thermal models",
      "unit": 8,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Finite-volume and finite-element thermal models** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Constant k=10 W/(m K), area 1 m\u00b2, total length 0.1 m, \u0394T=20 K.\n\n**Operation.** Use the relationship `Finite-volume linear slab reference` with all inputs converted to compatible units; the result is **2,000 W**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
    },
    {
      "id": "prob-heat-transfer-8-4",
      "title": "Calculation & Verification: Uncertainty, verification and model validation",
      "unit": 8,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Uncertainty, verification and model validation** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Independent k relative error 0.004/0.04, thickness error 0.005/0.1, other uncertainty neglected.\n\n**Operation.** Use the relationship `Relative combined uncertainty` with all inputs converted to compatible units; the result is **0.1118 fraction**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
    },
    {
      "id": "prob-heat-transfer-8-5",
      "title": "Calculation & Verification: Integrated design: thermal control of equipment",
      "unit": 8,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Integrated design: thermal control of equipment** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Given synthetic inputs.** Allowable temperature rise 32 K for dissipation 80 W.\n\n**Operation.** Use the relationship `Target resistance: R\u03b8,max=\u0394Tallowed/Q` with all inputs converted to compatible units; the result is **0.4 K/W**. This is an illustrative arithmetic result, not a measured field or equipment rating. Preserve more precision during intermediate calculations than in the reported answer. If the output is a rate, do not confuse it with accumulated energy. If it is a temperature difference, distinguish it from absolute temperature. If it is nondimensional, the absence of units is a useful audit rather than permission to omit definitions.\n\n**Physical interpretation.** Determine how the sign, scale and limiting cases match the original scenario. Recompute the result after raising a physically meaningful driving variable by 10%, but do not automatically assume a proportional change. The formula may contain an exponent, logarithm or regime-dependent coefficient, in which case its sensitivity varies with the operating point. Propose a second measurement that would check the prediction without merely feeding the same data into the same equation. A calibration check tests the measuring instrument, not necessarily the entire heat-transfer model.</p></div>"
    }
  ]
};
if (typeof module !== 'undefined') module.exports = COURSE_DATA;
if (typeof window !== 'undefined') window.COURSE_DATA = COURSE_DATA;
