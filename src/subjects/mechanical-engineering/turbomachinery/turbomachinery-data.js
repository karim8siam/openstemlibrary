/* OpenSTEM Course Data: Turbomachinery (TBM) */
var COURSE_DATA = {
  "code": "TBM",
  "title": "Turbomachinery",
  "subtitle": "Euler Turbine Equation, Velocity Triangles, Axial/Radial Pumps, Compressors, Steam & Gas Turbines",
  "units": [
    {
      "number": 1,
      "unitNumber": 1,
      "title": "Foundations of Energy Transfer in Rotating Flow",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Foundations of Energy Transfer in Rotating Flow.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Foundations of Energy Transfer in Rotating Flow.",
      "sections": [
        {
          "id": "sec-1-1",
          "title": "Rotor control volumes and machine classification",
          "leadSummary": "**Outcome.** Use conservation laws and appropriate reference stations to analyze **rotor control volumes and machine classification**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 01, **Foundations of Energy Transfer in Rotating Flow**.",
          "content": "<p>**Outcome.** Use conservation laws and appropriate reference stations to analyze **rotor control volumes and machine classification**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 01, **Foundations of Energy Transfer in Rotating Flow**.</p>"
        },
        {
          "id": "sec-1-2",
          "title": "Angular momentum and Euler specific work",
          "leadSummary": "**Outcome.** Use conservation laws and appropriate reference stations to analyze **angular momentum and euler specific work**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 01, **Foundations of Energy Transfer in Rotating Flow**.",
          "content": "<p>**Outcome.** Use conservation laws and appropriate reference stations to analyze **angular momentum and euler specific work**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 01, **Foundations of Energy Transfer in Rotating Flow**.</p>"
        },
        {
          "id": "sec-1-3",
          "title": "Velocity triangles and blade angles",
          "leadSummary": "**Outcome.** Use conservation laws and appropriate reference stations to analyze **velocity triangles and blade angles**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 01, **Foundations of Energy Transfer in Rotating Flow**.",
          "content": "<p>**Outcome.** Use conservation laws and appropriate reference stations to analyze **velocity triangles and blade angles**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 01, **Foundations of Energy Transfer in Rotating Flow**.</p>"
        },
        {
          "id": "sec-1-4",
          "title": "Flow, head and loading coefficients",
          "leadSummary": "**Outcome.** Use conservation laws and appropriate reference stations to analyze **flow, head and loading coefficients**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 01, **Foundations of Energy Transfer in Rotating Flow**.",
          "content": "<p>**Outcome.** Use conservation laws and appropriate reference stations to analyze **flow, head and loading coefficients**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 01, **Foundations of Energy Transfer in Rotating Flow**.</p>"
        },
        {
          "id": "sec-1-5",
          "title": "Similarity and corrected operating conditions",
          "leadSummary": "**Outcome.** Use conservation laws and appropriate reference stations to analyze **similarity and corrected operating conditions**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 01, **Foundations of Energy Transfer in Rotating Flow**.",
          "content": "<p>**Outcome.** Use conservation laws and appropriate reference stations to analyze **similarity and corrected operating conditions**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 01, **Foundations of Energy Transfer in Rotating Flow**.</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-turbomachinery-1-1",
          "title": "Calculation & Verification: Rotor control volumes and machine classification",
          "unit": 1,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Rotor control volumes and machine classification** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** An air stream of 3.0 kg/s receiving 18 kJ/kg of stagnation enthalpy requires 54 kW of ideal fluid power.\n\n**Explicit substitution:** 3.0 kg/s \u00d7 18 kJ/kg = 54 kJ/s; therefore **54 kW**. A compressor needs fluid energy input, with greater actual shaft input if mechanical losses occur.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
        },
        {
          "id": "prob-turbomachinery-1-2",
          "title": "Calculation & Verification: Angular momentum and Euler specific work",
          "unit": 1,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Angular momentum and Euler specific work** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** With U1=100 m/s, Vtheta1=8 m/s, U2=160 m/s and Vtheta2=48 m/s, ideal specific input is 6880 J/kg.\n\n**Explicit substitution:** 160\u00d748 \u2212 100\u00d78 = 7680 \u2212 800; therefore **6880 J/kg**. Exit whirl is taken positive with the rotor; reversing it changes the sign.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
        },
        {
          "id": "prob-turbomachinery-1-3",
          "title": "Calculation & Verification: Velocity triangles and blade angles",
          "unit": 1,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Velocity triangles and blade angles** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** Air with U=150 m/s, Vtheta=35 m/s and Vax=70 m/s has Wtheta=-115 m/s and beta approximately -58.7 degrees.\n\n**Explicit substitution:** Wtheta = 35 \u2212 150 = \u2212115 m/s; beta = atan2(\u2212115,70); therefore **\u221258.7\u00b0**. Use signed components, not unsigned velocity magnitudes.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
        },
        {
          "id": "prob-turbomachinery-1-4",
          "title": "Calculation & Verification: Flow, head and loading coefficients",
          "unit": 1,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Flow, head and loading coefficients** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** A stage with Vax=90 m/s, U=180 m/s and Delta_h0=19.4 kJ/kg has phi=0.50 and psi=0.599.\n\n**Explicit substitution:** phi = 90/180; psi=19,400/180\u00b2; therefore **phi=0.500; psi=0.5988**. Specific work uses joules per kilogram, not kilojoules per kilogram.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
        },
        {
          "id": "prob-turbomachinery-1-5",
          "title": "Calculation & Verification: Similarity and corrected operating conditions",
          "unit": 1,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Similarity and corrected operating conditions** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** Raising a pump speed from 1200 to 1440 rpm predicts flow multiplication by 1.20 near corresponding operating points.\n\n**Explicit substitution:** N2/N1=1440/1200; therefore **1.20 \u00d7 corresponding flow**. Recompute actual operating point against system curve containing static head.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
        }
      ]
    },
    {
      "number": 2,
      "unitNumber": 2,
      "title": "Centrifugal Pumps, Fans and Hydraulic Systems",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Centrifugal Pumps, Fans and Hydraulic Systems.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Centrifugal Pumps, Fans and Hydraulic Systems.",
      "sections": [
        {
          "id": "sec-2-1",
          "title": "Pump head from pressure and velocity",
          "leadSummary": "**Outcome.** Use conservation laws and appropriate reference stations to analyze **pump head from pressure and velocity**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 02, **Centrifugal Pumps, Fans and Hydraulic Systems**.",
          "content": "<p>**Outcome.** Use conservation laws and appropriate reference stations to analyze **pump head from pressure and velocity**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 02, **Centrifugal Pumps, Fans and Hydraulic Systems**.</p>"
        },
        {
          "id": "sec-2-2",
          "title": "System curves and operating-point intersection",
          "leadSummary": "**Outcome.** Use conservation laws and appropriate reference stations to analyze **system curves and operating-point intersection**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 02, **Centrifugal Pumps, Fans and Hydraulic Systems**.",
          "content": "<p>**Outcome.** Use conservation laws and appropriate reference stations to analyze **system curves and operating-point intersection**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 02, **Centrifugal Pumps, Fans and Hydraulic Systems**.</p>"
        },
        {
          "id": "sec-2-3",
          "title": "Pump efficiency and power",
          "leadSummary": "**Outcome.** Use conservation laws and appropriate reference stations to analyze **pump efficiency and power**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 02, **Centrifugal Pumps, Fans and Hydraulic Systems**.",
          "content": "<p>**Outcome.** Use conservation laws and appropriate reference stations to analyze **pump efficiency and power**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 02, **Centrifugal Pumps, Fans and Hydraulic Systems**.</p>"
        },
        {
          "id": "sec-2-4",
          "title": "Cavitation and NPSH margin",
          "leadSummary": "**Outcome.** Use conservation laws and appropriate reference stations to analyze **cavitation and npsh margin**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 02, **Centrifugal Pumps, Fans and Hydraulic Systems**.",
          "content": "<p>**Outcome.** Use conservation laws and appropriate reference stations to analyze **cavitation and npsh margin**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 02, **Centrifugal Pumps, Fans and Hydraulic Systems**.</p>"
        },
        {
          "id": "sec-2-5",
          "title": "Fans and compressible ventilation flow",
          "leadSummary": "**Outcome.** Use conservation laws and appropriate reference stations to analyze **fans and compressible ventilation flow**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 02, **Centrifugal Pumps, Fans and Hydraulic Systems**.",
          "content": "<p>**Outcome.** Use conservation laws and appropriate reference stations to analyze **fans and compressible ventilation flow**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 02, **Centrifugal Pumps, Fans and Hydraulic Systems**.</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-turbomachinery-2-1",
          "title": "Calculation & Verification: Pump head from pressure and velocity",
          "unit": 2,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Pump head from pressure and velocity** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** For water at 998 kg/m3, 200 kPa pressure rise and negligible elevation or velocity difference give H\u224820.43 m.\n\n**Explicit substitution:** H = 200,000/(998\u00d79.81); therefore **20.43 m**. This is pressure head only; add velocity and elevation terms if nonzero.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
        },
        {
          "id": "prob-turbomachinery-2-2",
          "title": "Calculation & Verification: System curves and operating-point intersection",
          "unit": 2,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **System curves and operating-point intersection** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** A test loop with 12 m static head and K=8000 s2/m5 requires 32 m at Q=0.050 m3/s.\n\n**Explicit substitution:** H=12+8000\u00d7(0.050)\u00b2; therefore **32.0 m**. Square law here assumes the fixed system resistance coefficient remains appropriate.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
        },
        {
          "id": "prob-turbomachinery-2-3",
          "title": "Calculation & Verification: Pump efficiency and power",
          "unit": 2,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Pump efficiency and power** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** Water at 1000 kg/m3 and Q=0.035 m3/s over 25 m, with pump eta=0.76 and motor eta=0.93, uses about 12.13 kW.\n\n**Explicit substitution:** P = 1000\u00d79.81\u00d70.035\u00d725/(0.76\u00d70.93); therefore **12.13 kW**. Fluid power is 8.584 kW, less than electrical input.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
        },
        {
          "id": "prob-turbomachinery-2-4",
          "title": "Calculation & Verification: Cavitation and NPSH margin",
          "unit": 2,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Cavitation and NPSH margin** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** At suction absolute pressure 65 kPa, vapor pressure 3 kPa, rho=1000 kg/m3 and negligible velocity correction, NPSHa\u22486.32 m.\n\n**Explicit substitution:** NPSHa = (65,000\u22123,000)/(1000\u00d79.81); therefore **6.32 m**. Absolute suction and vapor pressures must share the same reference.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
        },
        {
          "id": "prob-turbomachinery-2-5",
          "title": "Calculation & Verification: Fans and compressible ventilation flow",
          "unit": 2,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Fans and compressible ventilation flow** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** A fan delivering 2.5 m3/s against 800 Pa total-pressure rise gives 2.0 kW air power and 3.08 kW input at overall eta=0.65.\n\n**Explicit substitution:** P_air=800\u00d72.5=2000 W; P_input=2000/0.65; therefore **2.00 kW useful; 3.08 kW input**. Static pressure must not be substituted for total pressure without correction.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
        }
      ]
    },
    {
      "number": 3,
      "unitNumber": 3,
      "title": "Axial Compressors and Aerodynamic Stability",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Axial Compressors and Aerodynamic Stability.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Axial Compressors and Aerodynamic Stability.",
      "sections": [
        {
          "id": "sec-3-1",
          "title": "Axial compressor flow passages",
          "leadSummary": "**Outcome.** Use conservation laws and appropriate reference stations to analyze **axial compressor flow passages**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 03, **Axial Compressors and Aerodynamic Stability**.",
          "content": "<p>**Outcome.** Use conservation laws and appropriate reference stations to analyze **axial compressor flow passages**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 03, **Axial Compressors and Aerodynamic Stability**.</p>"
        },
        {
          "id": "sec-3-2",
          "title": "Incidence, turning and cascade losses",
          "leadSummary": "**Outcome.** Use conservation laws and appropriate reference stations to analyze **incidence, turning and cascade losses**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 03, **Axial Compressors and Aerodynamic Stability**.",
          "content": "<p>**Outcome.** Use conservation laws and appropriate reference stations to analyze **incidence, turning and cascade losses**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 03, **Axial Compressors and Aerodynamic Stability**.</p>"
        },
        {
          "id": "sec-3-3",
          "title": "Degree of reaction in an axial stage",
          "leadSummary": "**Outcome.** Use conservation laws and appropriate reference stations to analyze **degree of reaction in an axial stage**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 03, **Axial Compressors and Aerodynamic Stability**.",
          "content": "<p>**Outcome.** Use conservation laws and appropriate reference stations to analyze **degree of reaction in an axial stage**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 03, **Axial Compressors and Aerodynamic Stability**.</p>"
        },
        {
          "id": "sec-3-4",
          "title": "Compressor pressure ratio and isentropic efficiency",
          "leadSummary": "**Outcome.** Use conservation laws and appropriate reference stations to analyze **compressor pressure ratio and isentropic efficiency**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 03, **Axial Compressors and Aerodynamic Stability**.",
          "content": "<p>**Outcome.** Use conservation laws and appropriate reference stations to analyze **compressor pressure ratio and isentropic efficiency**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 03, **Axial Compressors and Aerodynamic Stability**.</p>"
        },
        {
          "id": "sec-3-5",
          "title": "Stall and surge as distinct instabilities",
          "leadSummary": "**Outcome.** Use conservation laws and appropriate reference stations to analyze **stall and surge as distinct instabilities**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 03, **Axial Compressors and Aerodynamic Stability**.",
          "content": "<p>**Outcome.** Use conservation laws and appropriate reference stations to analyze **stall and surge as distinct instabilities**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 03, **Axial Compressors and Aerodynamic Stability**.</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-turbomachinery-3-1",
          "title": "Calculation & Verification: Axial compressor flow passages",
          "unit": 3,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Axial compressor flow passages** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** With density 1.1 kg/m3, annulus area 0.12 m2 and axial velocity 115 m/s, the flow is 15.18 kg/s.\n\n**Explicit substitution:** m_dot = 1.1\u00d70.12\u00d7115; therefore **15.18 kg/s**. The area is the annulus, not the full casing disk.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
        },
        {
          "id": "prob-turbomachinery-3-2",
          "title": "Calculation & Verification: Incidence, turning and cascade losses",
          "unit": 3,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Incidence, turning and cascade losses** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** A relative flow angle of -41 degrees at the leading edge and a metal angle of -45 degrees implies +4 degrees incidence.\n\n**Explicit substitution:** incidence = (\u221241\u00b0)\u2212(\u221245\u00b0); therefore **+4\u00b0**. Opposite sign convention would need a corresponding interpretation change.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
        },
        {
          "id": "prob-turbomachinery-3-3",
          "title": "Calculation & Verification: Degree of reaction in an axial stage",
          "unit": 3,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Degree of reaction in an axial stage** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** If rotor static enthalpy increases 10 kJ/kg and the whole stage increases 22 kJ/kg, the reaction is about 0.455.\n\n**Explicit substitution:** R = 10/22; therefore **0.4545**. Rotor and stage static enthalpy stations must be stated.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
        },
        {
          "id": "prob-turbomachinery-3-4",
          "title": "Calculation & Verification: Compressor pressure ratio and isentropic efficiency",
          "unit": 3,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Compressor pressure ratio and isentropic efficiency** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** Air with pi=2.5, gamma=1.4, T01=300 K and T02=415 K has eta_c\u22480.780.\n\n**Explicit substitution:** eta_c = [2.5^(0.4/1.4)\u22121]/(415/300\u22121); therefore **0.7807**. T temperatures are in kelvin and actual rise exceeds isentropic rise.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
        },
        {
          "id": "prob-turbomachinery-3-5",
          "title": "Calculation & Verification: Stall and surge as distinct instabilities",
          "unit": 3,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Stall and surge as distinct instabilities** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** At common corrected flow, PR_surge=3.1 and PR_operating=2.8 give a nominal 10.7% ratio margin.\n\n**Explicit substitution:** (3.1\u22122.8)/2.8\u00d7100; therefore **10.71% pressure-ratio margin**. A static scalar margin does not resolve transient surge risk.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
        }
      ]
    },
    {
      "number": 4,
      "unitNumber": 4,
      "title": "Centrifugal Compressors and Diffusers",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Centrifugal Compressors and Diffusers.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Centrifugal Compressors and Diffusers.",
      "sections": [
        {
          "id": "sec-4-1",
          "title": "Radial impeller energy rise",
          "leadSummary": "**Outcome.** Use conservation laws and appropriate reference stations to analyze **radial impeller energy rise**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 04, **Centrifugal Compressors and Diffusers**.",
          "content": "<p>**Outcome.** Use conservation laws and appropriate reference stations to analyze **radial impeller energy rise**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 04, **Centrifugal Compressors and Diffusers**.</p>"
        },
        {
          "id": "sec-4-2",
          "title": "Slip factor and backswept blades",
          "leadSummary": "**Outcome.** Use conservation laws and appropriate reference stations to analyze **slip factor and backswept blades**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 04, **Centrifugal Compressors and Diffusers**.",
          "content": "<p>**Outcome.** Use conservation laws and appropriate reference stations to analyze **slip factor and backswept blades**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 04, **Centrifugal Compressors and Diffusers**.</p>"
        },
        {
          "id": "sec-4-3",
          "title": "Diffuser velocity recovery",
          "leadSummary": "**Outcome.** Use conservation laws and appropriate reference stations to analyze **diffuser velocity recovery**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 04, **Centrifugal Compressors and Diffusers**.",
          "content": "<p>**Outcome.** Use conservation laws and appropriate reference stations to analyze **diffuser velocity recovery**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 04, **Centrifugal Compressors and Diffusers**.</p>"
        },
        {
          "id": "sec-4-4",
          "title": "Corrected compressor flow and speed",
          "leadSummary": "**Outcome.** Use conservation laws and appropriate reference stations to analyze **corrected compressor flow and speed**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 04, **Centrifugal Compressors and Diffusers**.",
          "content": "<p>**Outcome.** Use conservation laws and appropriate reference stations to analyze **corrected compressor flow and speed**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 04, **Centrifugal Compressors and Diffusers**.</p>"
        },
        {
          "id": "sec-4-5",
          "title": "Choke and impeller mechanical limits",
          "leadSummary": "**Outcome.** Use conservation laws and appropriate reference stations to analyze **choke and impeller mechanical limits**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 04, **Centrifugal Compressors and Diffusers**.",
          "content": "<p>**Outcome.** Use conservation laws and appropriate reference stations to analyze **choke and impeller mechanical limits**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 04, **Centrifugal Compressors and Diffusers**.</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-turbomachinery-4-1",
          "title": "Calculation & Verification: Radial impeller energy rise",
          "unit": 4,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Radial impeller energy rise** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** At U2=300 m/s, Vtheta2=210 m/s and negligible inlet swirl, the ideal input is 63 kJ/kg.\n\n**Explicit substitution:** Delta h0 =300\u00d7210\u22120; therefore **63,000 J/kg**. Inlet whirl was explicitly assumed negligible.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
        },
        {
          "id": "prob-turbomachinery-4-2",
          "title": "Calculation & Verification: Slip factor and backswept blades",
          "unit": 4,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Slip factor and backswept blades** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** If an ideal exit whirl is 235 m/s and measured or modeled whirl is 205 m/s, sigma\u22480.872.\n\n**Explicit substitution:** sigma =205/235; therefore **0.8723**. Defined slip factor depends on the specified ideal whirl reference.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
        },
        {
          "id": "prob-turbomachinery-4-3",
          "title": "Calculation & Verification: Diffuser velocity recovery",
          "unit": 4,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Diffuser velocity recovery** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** With rho=1.2 kg/m3, V1=160 m/s and V2=100 m/s, the ideal static recovery is 9.36 kPa.\n\n**Explicit substitution:** Delta p\u2248(1.2/2)\u00d7(160\u00b2\u2212100\u00b2); therefore **9360 Pa**. Valid only as a constant-density inviscid recovery idealization.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
        },
        {
          "id": "prob-turbomachinery-4-4",
          "title": "Calculation & Verification: Corrected compressor flow and speed",
          "unit": 4,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Corrected compressor flow and speed** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** At m_dot=8 kg/s, T01=330 K, Tref=288.15 K, p01=95 kPa and pref=101.325 kPa, corrected flow is about 9.12 kg/s.\n\n**Explicit substitution:** m_corr=8\u00d7sqrt(330/288.15)/(95/101.325); therefore **9.12 kg/s corrected**. This is a coordinate for a specified reference state, not physical mass flow.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
        },
        {
          "id": "prob-turbomachinery-4-5",
          "title": "Calculation & Verification: Choke and impeller mechanical limits",
          "unit": 4,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Choke and impeller mechanical limits** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** A local absolute flow speed of 340 m/s at 300 K air gives Mach\u22480.98 using gamma=1.4, R=287 J/(kg K).\n\n**Explicit substitution:** a=sqrt(1.4\u00d7287\u00d7300); M=340/a; therefore **a\u2248347.2 m/s; M\u22480.979**. Relative Mach may exceed the absolute Mach and matters at the blade throat.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
        }
      ]
    },
    {
      "number": 5,
      "unitNumber": 5,
      "title": "Gas and Steam Turbines",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Gas and Steam Turbines.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Gas and Steam Turbines.",
      "sections": [
        {
          "id": "sec-5-1",
          "title": "Gas turbine specific work and power",
          "leadSummary": "**Outcome.** Use conservation laws and appropriate reference stations to analyze **gas turbine specific work and power**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 05, **Gas and Steam Turbines**.",
          "content": "<p>**Outcome.** Use conservation laws and appropriate reference stations to analyze **gas turbine specific work and power**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 05, **Gas and Steam Turbines**.</p>"
        },
        {
          "id": "sec-5-2",
          "title": "Turbine isentropic efficiency",
          "leadSummary": "**Outcome.** Use conservation laws and appropriate reference stations to analyze **turbine isentropic efficiency**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 05, **Gas and Steam Turbines**.",
          "content": "<p>**Outcome.** Use conservation laws and appropriate reference stations to analyze **turbine isentropic efficiency**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 05, **Gas and Steam Turbines**.</p>"
        },
        {
          "id": "sec-5-3",
          "title": "Impulse, reaction and stage velocity triangles",
          "leadSummary": "**Outcome.** Use conservation laws and appropriate reference stations to analyze **impulse, reaction and stage velocity triangles**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 05, **Gas and Steam Turbines**.",
          "content": "<p>**Outcome.** Use conservation laws and appropriate reference stations to analyze **impulse, reaction and stage velocity triangles**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 05, **Gas and Steam Turbines**.</p>"
        },
        {
          "id": "sec-5-4",
          "title": "Steam expansion, quality and moisture",
          "leadSummary": "**Outcome.** Use conservation laws and appropriate reference stations to analyze **steam expansion, quality and moisture**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 05, **Gas and Steam Turbines**.",
          "content": "<p>**Outcome.** Use conservation laws and appropriate reference stations to analyze **steam expansion, quality and moisture**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 05, **Gas and Steam Turbines**.</p>"
        },
        {
          "id": "sec-5-5",
          "title": "Turbine cooling and net cycle balance",
          "leadSummary": "**Outcome.** Use conservation laws and appropriate reference stations to analyze **turbine cooling and net cycle balance**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 05, **Gas and Steam Turbines**.",
          "content": "<p>**Outcome.** Use conservation laws and appropriate reference stations to analyze **turbine cooling and net cycle balance**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 05, **Gas and Steam Turbines**.</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-turbomachinery-5-1",
          "title": "Calculation & Verification: Gas turbine specific work and power",
          "unit": 5,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Gas turbine specific work and power** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** Gas with m_dot=18 kg/s, cp=1.15 kJ/(kg K) and a 210 K total-temperature drop develops about 4.35 MW fluid power.\n\n**Explicit substitution:** P=18\u00d71.15\u00d7210; therefore **4347 kW = 4.347 MW**. The cp is a given mean value over the temperature interval.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
        },
        {
          "id": "prob-turbomachinery-5-2",
          "title": "Calculation & Verification: Turbine isentropic efficiency",
          "unit": 5,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Turbine isentropic efficiency** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** With T01=1100 K, T02=900 K and ideal T02s=865 K, turbine efficiency is about 0.851.\n\n**Explicit substitution:** eta_t=(1100\u2212900)/(1100\u2212865)=200/235; therefore **0.8511**. For a turbine the actual enthalpy drop is less than ideal.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
        },
        {
          "id": "prob-turbomachinery-5-3",
          "title": "Calculation & Verification: Impulse, reaction and stage velocity triangles",
          "unit": 5,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Impulse, reaction and stage velocity triangles** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** At constant U=240 m/s, inlet whirl=160 m/s and exit whirl=-40 m/s, extraction is 48 kJ/kg.\n\n**Explicit substitution:** w=240\u00d7160\u2212240\u00d7(\u221240); therefore **48,000 J/kg**. Rotor extracts power; outlet counter-swirl increases extracted work.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
        },
        {
          "id": "prob-turbomachinery-5-4",
          "title": "Calculation & Verification: Steam expansion, quality and moisture",
          "unit": 5,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Steam expansion, quality and moisture** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** At x=0.90, hg=2600 kJ/kg and hf=200 kJ/kg, mixture enthalpy is 2360 kJ/kg.\n\n**Explicit substitution:** h=0.90\u00d72600+0.10\u00d7200; therefore **2360 kJ/kg**. Saturation quality is mass fraction of vapor.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
        },
        {
          "id": "prob-turbomachinery-5-5",
          "title": "Calculation & Verification: Turbine cooling and net cycle balance",
          "unit": 5,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Turbine cooling and net cycle balance** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** A 12 MW turbine driving a 7.5 MW compressor and 0.4 MW auxiliaries leaves 4.1 MW net before electrical losses.\n\n**Explicit substitution:** P_net=12\u22127.5\u22120.4; therefore **4.1 MW**. Generator and other downstream electrical losses not included.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
        }
      ]
    },
    {
      "number": 6,
      "unitNumber": 6,
      "title": "Hydraulic Turbines and Renewable Power",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Hydraulic Turbines and Renewable Power.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Hydraulic Turbines and Renewable Power.",
      "sections": [
        {
          "id": "sec-6-1",
          "title": "Gross versus net hydraulic head",
          "leadSummary": "**Outcome.** Use conservation laws and appropriate reference stations to analyze **gross versus net hydraulic head**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 06, **Hydraulic Turbines and Renewable Power**.",
          "content": "<p>**Outcome.** Use conservation laws and appropriate reference stations to analyze **gross versus net hydraulic head**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 06, **Hydraulic Turbines and Renewable Power**.</p>"
        },
        {
          "id": "sec-6-2",
          "title": "Hydroelectric turbine power and efficiency",
          "leadSummary": "**Outcome.** Use conservation laws and appropriate reference stations to analyze **hydroelectric turbine power and efficiency**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 06, **Hydraulic Turbines and Renewable Power**.",
          "content": "<p>**Outcome.** Use conservation laws and appropriate reference stations to analyze **hydroelectric turbine power and efficiency**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 06, **Hydraulic Turbines and Renewable Power**.</p>"
        },
        {
          "id": "sec-6-3",
          "title": "Impulse turbine jet and runner speed",
          "leadSummary": "**Outcome.** Use conservation laws and appropriate reference stations to analyze **impulse turbine jet and runner speed**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 06, **Hydraulic Turbines and Renewable Power**.",
          "content": "<p>**Outcome.** Use conservation laws and appropriate reference stations to analyze **impulse turbine jet and runner speed**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 06, **Hydraulic Turbines and Renewable Power**.</p>"
        },
        {
          "id": "sec-6-4",
          "title": "Francis and Kaplan reaction runners",
          "leadSummary": "**Outcome.** Use conservation laws and appropriate reference stations to analyze **francis and kaplan reaction runners**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 06, **Hydraulic Turbines and Renewable Power**.",
          "content": "<p>**Outcome.** Use conservation laws and appropriate reference stations to analyze **francis and kaplan reaction runners**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 06, **Hydraulic Turbines and Renewable Power**.</p>"
        },
        {
          "id": "sec-6-5",
          "title": "Runner specific speed and selection",
          "leadSummary": "**Outcome.** Use conservation laws and appropriate reference stations to analyze **runner specific speed and selection**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 06, **Hydraulic Turbines and Renewable Power**.",
          "content": "<p>**Outcome.** Use conservation laws and appropriate reference stations to analyze **runner specific speed and selection**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 06, **Hydraulic Turbines and Renewable Power**.</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-turbomachinery-6-1",
          "title": "Calculation & Verification: Gross versus net hydraulic head",
          "unit": 6,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Gross versus net hydraulic head** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** A water scheme with 43 m gross head and 5 m penstock losses has 38 m net head at that flow.\n\n**Explicit substitution:** H_net=43\u22125; therefore **38 m**. Penstock friction depends on discharge and must be reassessed off-design.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
        },
        {
          "id": "prob-turbomachinery-6-2",
          "title": "Calculation & Verification: Hydroelectric turbine power and efficiency",
          "unit": 6,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Hydroelectric turbine power and efficiency** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** A plant using Q=2.4 m3/s, H=28 m, rho=1000 kg/m3 and eta_total=0.87 supplies about 573.7 kW.\n\n**Explicit substitution:** P=1000\u00d79.81\u00d72.4\u00d728\u00d70.87/1000; therefore **573.55 kW**. Here total efficiency includes generator loss and is only an assumed value.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
        },
        {
          "id": "prob-turbomachinery-6-3",
          "title": "Calculation & Verification: Impulse turbine jet and runner speed",
          "unit": 6,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Impulse turbine jet and runner speed** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** With H=80 m, ideal water jet speed is about 39.6 m/s before nozzle losses.\n\n**Explicit substitution:** V=sqrt(2\u00d79.81\u00d780); therefore **39.62 m/s ideal**. Actual jet velocity is reduced by nozzle losses.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
        },
        {
          "id": "prob-turbomachinery-6-4",
          "title": "Calculation & Verification: Francis and Kaplan reaction runners",
          "unit": 6,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Francis and Kaplan reaction runners** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** With outlet velocity 6 m/s, recoverable ideal velocity head is 1.84 m before losses.\n\n**Explicit substitution:** V\u00b2/(2g)=6\u00b2/(2\u00d79.81); therefore **1.835 m of velocity head**. Recoverable portion is lower because draft tubes dissipate energy.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
        },
        {
          "id": "prob-turbomachinery-6-5",
          "title": "Calculation & Verification: Runner specific speed and selection",
          "unit": 6,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Runner specific speed and selection** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** Using n=300 rpm, P=500 kW and H=30 m gives a numerical metric about 95.6 in rpm-kW-m convention.\n\n**Explicit substitution:** N_s=300\u00d7sqrt(500)/30^1.25; therefore **95.54 (rpm\u2013kW\u2013m convention)**. Specific-speed values from different numerical conventions must not be compared directly.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
        }
      ]
    },
    {
      "number": 7,
      "unitNumber": 7,
      "title": "Rotor Dynamics, Blades and Mechanical Reliability",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Rotor Dynamics, Blades and Mechanical Reliability.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Rotor Dynamics, Blades and Mechanical Reliability.",
      "sections": [
        {
          "id": "sec-7-1",
          "title": "Centrifugal blade stress scaling",
          "leadSummary": "**Outcome.** Use conservation laws and appropriate reference stations to analyze **centrifugal blade stress scaling**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 07, **Rotor Dynamics, Blades and Mechanical Reliability**.",
          "content": "<p>**Outcome.** Use conservation laws and appropriate reference stations to analyze **centrifugal blade stress scaling**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 07, **Rotor Dynamics, Blades and Mechanical Reliability**.</p>"
        },
        {
          "id": "sec-7-2",
          "title": "Rotor unbalance and bearing load",
          "leadSummary": "**Outcome.** Use conservation laws and appropriate reference stations to analyze **rotor unbalance and bearing load**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 07, **Rotor Dynamics, Blades and Mechanical Reliability**.",
          "content": "<p>**Outcome.** Use conservation laws and appropriate reference stations to analyze **rotor unbalance and bearing load**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 07, **Rotor Dynamics, Blades and Mechanical Reliability**.</p>"
        },
        {
          "id": "sec-7-3",
          "title": "Critical speed and Campbell diagrams",
          "leadSummary": "**Outcome.** Use conservation laws and appropriate reference stations to analyze **critical speed and campbell diagrams**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 07, **Rotor Dynamics, Blades and Mechanical Reliability**.",
          "content": "<p>**Outcome.** Use conservation laws and appropriate reference stations to analyze **critical speed and campbell diagrams**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 07, **Rotor Dynamics, Blades and Mechanical Reliability**.</p>"
        },
        {
          "id": "sec-7-4",
          "title": "Bearing losses, seals and leakage",
          "leadSummary": "**Outcome.** Use conservation laws and appropriate reference stations to analyze **bearing losses, seals and leakage**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 07, **Rotor Dynamics, Blades and Mechanical Reliability**.",
          "content": "<p>**Outcome.** Use conservation laws and appropriate reference stations to analyze **bearing losses, seals and leakage**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 07, **Rotor Dynamics, Blades and Mechanical Reliability**.</p>"
        },
        {
          "id": "sec-7-5",
          "title": "Blade fatigue and thermal transients",
          "leadSummary": "**Outcome.** Use conservation laws and appropriate reference stations to analyze **blade fatigue and thermal transients**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 07, **Rotor Dynamics, Blades and Mechanical Reliability**.",
          "content": "<p>**Outcome.** Use conservation laws and appropriate reference stations to analyze **blade fatigue and thermal transients**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 07, **Rotor Dynamics, Blades and Mechanical Reliability**.</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-turbomachinery-7-1",
          "title": "Calculation & Verification: Centrifugal blade stress scaling",
          "unit": 7,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Centrifugal blade stress scaling** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** For steel-like rho_m=7800 kg/m3 and tip speed 250 m/s, the scaling stress is 487.5 MPa before shape factors.\n\n**Explicit substitution:** sigma_char\u22487800\u00d7250\u00b2; therefore **487.5 MPa**. Characteristic stress scaling is not an allowable stress or burst proof.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
        },
        {
          "id": "prob-turbomachinery-7-2",
          "title": "Calculation & Verification: Rotor unbalance and bearing load",
          "unit": 7,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Rotor unbalance and bearing load** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** An eccentric mass of 0.02 kg at 1 mm radius and 3000 rpm produces about 1.97 N of rotating force.\n\n**Explicit substitution:** F=0.02\u00d70.001\u00d7(2\u03c0\u00d73000/60)\u00b2; therefore **1.974 N**. At twice speed the force becomes four times as large.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
        },
        {
          "id": "prob-turbomachinery-7-3",
          "title": "Calculation & Verification: Critical speed and Campbell diagrams",
          "unit": 7,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Critical speed and Campbell diagrams** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** With stiffness 2.0 MN/m and equivalent mass 50 kg, natural angular frequency is 200 rad/s, about 1910 rpm.\n\n**Explicit substitution:** omega_n=sqrt(2,000,000/50)=200 rad/s; n=omega_n\u00d760/(2\u03c0); therefore **1909.9 rpm**. Real rotors have multiple damped gyroscopic critical speeds.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
        },
        {
          "id": "prob-turbomachinery-7-4",
          "title": "Calculation & Verification: Bearing losses, seals and leakage",
          "unit": 7,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Bearing losses, seals and leakage** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** If bearing torque is 8 N m at 3000 rpm, mechanical dissipation is about 2.51 kW.\n\n**Explicit substitution:** P=8\u00d7(2\u03c0\u00d73000/60); therefore **2513 W = 2.513 kW**. This heat appears in bearings and associated systems, not useful output.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
        },
        {
          "id": "prob-turbomachinery-7-5",
          "title": "Calculation & Verification: Blade fatigue and thermal transients",
          "unit": 7,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Blade fatigue and thermal transients** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** A metal with alpha=12e-6 1/K subjected to a 250 K rise has free strain near 0.003.\n\n**Explicit substitution:** epsilon_free=12\u00d710^(\u22126)\u00d7250; therefore **0.003 or 0.3%**. Restrained expansion and modulus are needed to estimate stress.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
        }
      ]
    },
    {
      "number": 8,
      "unitNumber": 8,
      "title": "Performance Testing, Controls and Sustainable Operations",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Performance Testing, Controls and Sustainable Operations.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Performance Testing, Controls and Sustainable Operations.",
      "sections": [
        {
          "id": "sec-8-1",
          "title": "Design and off-design performance maps",
          "leadSummary": "**Outcome.** Use conservation laws and appropriate reference stations to analyze **design and off-design performance maps**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 08, **Performance Testing, Controls and Sustainable Operations**.",
          "content": "<p>**Outcome.** Use conservation laws and appropriate reference stations to analyze **design and off-design performance maps**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 08, **Performance Testing, Controls and Sustainable Operations**.</p>"
        },
        {
          "id": "sec-8-2",
          "title": "Instrumentation and propagated uncertainty",
          "leadSummary": "**Outcome.** Use conservation laws and appropriate reference stations to analyze **instrumentation and propagated uncertainty**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 08, **Performance Testing, Controls and Sustainable Operations**.",
          "content": "<p>**Outcome.** Use conservation laws and appropriate reference stations to analyze **instrumentation and propagated uncertainty**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 08, **Performance Testing, Controls and Sustainable Operations**.</p>"
        },
        {
          "id": "sec-8-3",
          "title": "Control loops and actuator constraints",
          "leadSummary": "**Outcome.** Use conservation laws and appropriate reference stations to analyze **control loops and actuator constraints**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 08, **Performance Testing, Controls and Sustainable Operations**.",
          "content": "<p>**Outcome.** Use conservation laws and appropriate reference stations to analyze **control loops and actuator constraints**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 08, **Performance Testing, Controls and Sustainable Operations**.</p>"
        },
        {
          "id": "sec-8-4",
          "title": "Condition monitoring and degradation diagnosis",
          "leadSummary": "**Outcome.** Use conservation laws and appropriate reference stations to analyze **condition monitoring and degradation diagnosis**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 08, **Performance Testing, Controls and Sustainable Operations**.",
          "content": "<p>**Outcome.** Use conservation laws and appropriate reference stations to analyze **condition monitoring and degradation diagnosis**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 08, **Performance Testing, Controls and Sustainable Operations**.</p>"
        },
        {
          "id": "sec-8-5",
          "title": "Lifecycle assessment and integrated design review",
          "leadSummary": "**Outcome.** Use conservation laws and appropriate reference stations to analyze **lifecycle assessment and integrated design review**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 08, **Performance Testing, Controls and Sustainable Operations**.",
          "content": "<p>**Outcome.** Use conservation laws and appropriate reference stations to analyze **lifecycle assessment and integrated design review**; solve a traceable numerical example; expose model limitations; and justify a provisional engineering choice. This is Unit 08, **Performance Testing, Controls and Sustainable Operations**.</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-turbomachinery-8-1",
          "title": "Calculation & Verification: Design and off-design performance maps",
          "unit": 8,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Design and off-design performance maps** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** A pump at 32 kW hydraulic and 43 kW shaft power operates at eta\u22480.744.\n\n**Explicit substitution:** eta=32/43; therefore **0.7442**. Hydraulic or aerodynamic power and shaft power must share a time boundary.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
        },
        {
          "id": "prob-turbomachinery-8-2",
          "title": "Calculation & Verification: Instrumentation and propagated uncertainty",
          "unit": 8,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Instrumentation and propagated uncertainty** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** A product with 2% independent flow error and 1% head error has \u22482.24% relative standard uncertainty.\n\n**Explicit substitution:** u_rel=sqrt(2\u00b2+1\u00b2); therefore **2.236%**. The root-sum-square is justified only if the errors are independent.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
        },
        {
          "id": "prob-turbomachinery-8-3",
          "title": "Calculation & Verification: Control loops and actuator constraints",
          "unit": 8,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Control loops and actuator constraints** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** A proportional controller with gain 0.15 per kPa sees 10 kPa error and requests a 1.5 unit actuator correction before saturation.\n\n**Explicit substitution:** Delta u=Kp e=0.15\u00d710; therefore **1.5 actuator units**. Saturation and derivative control are not included in this illustrative P action.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
        },
        {
          "id": "prob-turbomachinery-8-4",
          "title": "Calculation & Verification: Condition monitoring and degradation diagnosis",
          "unit": 8,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Condition monitoring and degradation diagnosis** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** Efficiency falling from 0.84 to 0.80 at matched conditions corresponds to 4 percentage points, not 4% relative.\n\n**Explicit substitution:** eta_ref\u2212eta_now=0.84\u22120.80; therefore **0.04 = 4 percentage points**. Relative decrease is 0.04/0.84\u22484.76%, a different statistic.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
        },
        {
          "id": "prob-turbomachinery-8-5",
          "title": "Calculation & Verification: Lifecycle assessment and integrated design review",
          "unit": 8,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Lifecycle assessment and integrated design review** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** A 12 kW mean auxiliary load running 5000 h/y uses 60 MWh/y; at $0.12/kWh its electricity cost is $7200/y.\n\n**Explicit substitution:** E=12 kW\u00d75000 h=60,000 kWh; cost=60,000\u00d70.12; therefore **60 MWh and USD 7200 per year**. No discounted cash flow or maintenance cost is included.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
        }
      ]
    }
  ],
  "problems": [
    {
      "id": "prob-turbomachinery-1-1",
      "title": "Calculation & Verification: Rotor control volumes and machine classification",
      "unit": 1,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Rotor control volumes and machine classification** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** An air stream of 3.0 kg/s receiving 18 kJ/kg of stagnation enthalpy requires 54 kW of ideal fluid power.\n\n**Explicit substitution:** 3.0 kg/s \u00d7 18 kJ/kg = 54 kJ/s; therefore **54 kW**. A compressor needs fluid energy input, with greater actual shaft input if mechanical losses occur.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
    },
    {
      "id": "prob-turbomachinery-1-2",
      "title": "Calculation & Verification: Angular momentum and Euler specific work",
      "unit": 1,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Angular momentum and Euler specific work** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** With U1=100 m/s, Vtheta1=8 m/s, U2=160 m/s and Vtheta2=48 m/s, ideal specific input is 6880 J/kg.\n\n**Explicit substitution:** 160\u00d748 \u2212 100\u00d78 = 7680 \u2212 800; therefore **6880 J/kg**. Exit whirl is taken positive with the rotor; reversing it changes the sign.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
    },
    {
      "id": "prob-turbomachinery-1-3",
      "title": "Calculation & Verification: Velocity triangles and blade angles",
      "unit": 1,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Velocity triangles and blade angles** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** Air with U=150 m/s, Vtheta=35 m/s and Vax=70 m/s has Wtheta=-115 m/s and beta approximately -58.7 degrees.\n\n**Explicit substitution:** Wtheta = 35 \u2212 150 = \u2212115 m/s; beta = atan2(\u2212115,70); therefore **\u221258.7\u00b0**. Use signed components, not unsigned velocity magnitudes.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
    },
    {
      "id": "prob-turbomachinery-1-4",
      "title": "Calculation & Verification: Flow, head and loading coefficients",
      "unit": 1,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Flow, head and loading coefficients** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** A stage with Vax=90 m/s, U=180 m/s and Delta_h0=19.4 kJ/kg has phi=0.50 and psi=0.599.\n\n**Explicit substitution:** phi = 90/180; psi=19,400/180\u00b2; therefore **phi=0.500; psi=0.5988**. Specific work uses joules per kilogram, not kilojoules per kilogram.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
    },
    {
      "id": "prob-turbomachinery-1-5",
      "title": "Calculation & Verification: Similarity and corrected operating conditions",
      "unit": 1,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Similarity and corrected operating conditions** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** Raising a pump speed from 1200 to 1440 rpm predicts flow multiplication by 1.20 near corresponding operating points.\n\n**Explicit substitution:** N2/N1=1440/1200; therefore **1.20 \u00d7 corresponding flow**. Recompute actual operating point against system curve containing static head.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
    },
    {
      "id": "prob-turbomachinery-2-1",
      "title": "Calculation & Verification: Pump head from pressure and velocity",
      "unit": 2,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Pump head from pressure and velocity** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** For water at 998 kg/m3, 200 kPa pressure rise and negligible elevation or velocity difference give H\u224820.43 m.\n\n**Explicit substitution:** H = 200,000/(998\u00d79.81); therefore **20.43 m**. This is pressure head only; add velocity and elevation terms if nonzero.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
    },
    {
      "id": "prob-turbomachinery-2-2",
      "title": "Calculation & Verification: System curves and operating-point intersection",
      "unit": 2,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **System curves and operating-point intersection** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** A test loop with 12 m static head and K=8000 s2/m5 requires 32 m at Q=0.050 m3/s.\n\n**Explicit substitution:** H=12+8000\u00d7(0.050)\u00b2; therefore **32.0 m**. Square law here assumes the fixed system resistance coefficient remains appropriate.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
    },
    {
      "id": "prob-turbomachinery-2-3",
      "title": "Calculation & Verification: Pump efficiency and power",
      "unit": 2,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Pump efficiency and power** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** Water at 1000 kg/m3 and Q=0.035 m3/s over 25 m, with pump eta=0.76 and motor eta=0.93, uses about 12.13 kW.\n\n**Explicit substitution:** P = 1000\u00d79.81\u00d70.035\u00d725/(0.76\u00d70.93); therefore **12.13 kW**. Fluid power is 8.584 kW, less than electrical input.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
    },
    {
      "id": "prob-turbomachinery-2-4",
      "title": "Calculation & Verification: Cavitation and NPSH margin",
      "unit": 2,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Cavitation and NPSH margin** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** At suction absolute pressure 65 kPa, vapor pressure 3 kPa, rho=1000 kg/m3 and negligible velocity correction, NPSHa\u22486.32 m.\n\n**Explicit substitution:** NPSHa = (65,000\u22123,000)/(1000\u00d79.81); therefore **6.32 m**. Absolute suction and vapor pressures must share the same reference.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
    },
    {
      "id": "prob-turbomachinery-2-5",
      "title": "Calculation & Verification: Fans and compressible ventilation flow",
      "unit": 2,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Fans and compressible ventilation flow** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** A fan delivering 2.5 m3/s against 800 Pa total-pressure rise gives 2.0 kW air power and 3.08 kW input at overall eta=0.65.\n\n**Explicit substitution:** P_air=800\u00d72.5=2000 W; P_input=2000/0.65; therefore **2.00 kW useful; 3.08 kW input**. Static pressure must not be substituted for total pressure without correction.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
    },
    {
      "id": "prob-turbomachinery-3-1",
      "title": "Calculation & Verification: Axial compressor flow passages",
      "unit": 3,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Axial compressor flow passages** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** With density 1.1 kg/m3, annulus area 0.12 m2 and axial velocity 115 m/s, the flow is 15.18 kg/s.\n\n**Explicit substitution:** m_dot = 1.1\u00d70.12\u00d7115; therefore **15.18 kg/s**. The area is the annulus, not the full casing disk.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
    },
    {
      "id": "prob-turbomachinery-3-2",
      "title": "Calculation & Verification: Incidence, turning and cascade losses",
      "unit": 3,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Incidence, turning and cascade losses** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** A relative flow angle of -41 degrees at the leading edge and a metal angle of -45 degrees implies +4 degrees incidence.\n\n**Explicit substitution:** incidence = (\u221241\u00b0)\u2212(\u221245\u00b0); therefore **+4\u00b0**. Opposite sign convention would need a corresponding interpretation change.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
    },
    {
      "id": "prob-turbomachinery-3-3",
      "title": "Calculation & Verification: Degree of reaction in an axial stage",
      "unit": 3,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Degree of reaction in an axial stage** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** If rotor static enthalpy increases 10 kJ/kg and the whole stage increases 22 kJ/kg, the reaction is about 0.455.\n\n**Explicit substitution:** R = 10/22; therefore **0.4545**. Rotor and stage static enthalpy stations must be stated.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
    },
    {
      "id": "prob-turbomachinery-3-4",
      "title": "Calculation & Verification: Compressor pressure ratio and isentropic efficiency",
      "unit": 3,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Compressor pressure ratio and isentropic efficiency** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** Air with pi=2.5, gamma=1.4, T01=300 K and T02=415 K has eta_c\u22480.780.\n\n**Explicit substitution:** eta_c = [2.5^(0.4/1.4)\u22121]/(415/300\u22121); therefore **0.7807**. T temperatures are in kelvin and actual rise exceeds isentropic rise.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
    },
    {
      "id": "prob-turbomachinery-3-5",
      "title": "Calculation & Verification: Stall and surge as distinct instabilities",
      "unit": 3,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Stall and surge as distinct instabilities** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** At common corrected flow, PR_surge=3.1 and PR_operating=2.8 give a nominal 10.7% ratio margin.\n\n**Explicit substitution:** (3.1\u22122.8)/2.8\u00d7100; therefore **10.71% pressure-ratio margin**. A static scalar margin does not resolve transient surge risk.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
    },
    {
      "id": "prob-turbomachinery-4-1",
      "title": "Calculation & Verification: Radial impeller energy rise",
      "unit": 4,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Radial impeller energy rise** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** At U2=300 m/s, Vtheta2=210 m/s and negligible inlet swirl, the ideal input is 63 kJ/kg.\n\n**Explicit substitution:** Delta h0 =300\u00d7210\u22120; therefore **63,000 J/kg**. Inlet whirl was explicitly assumed negligible.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
    },
    {
      "id": "prob-turbomachinery-4-2",
      "title": "Calculation & Verification: Slip factor and backswept blades",
      "unit": 4,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Slip factor and backswept blades** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** If an ideal exit whirl is 235 m/s and measured or modeled whirl is 205 m/s, sigma\u22480.872.\n\n**Explicit substitution:** sigma =205/235; therefore **0.8723**. Defined slip factor depends on the specified ideal whirl reference.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
    },
    {
      "id": "prob-turbomachinery-4-3",
      "title": "Calculation & Verification: Diffuser velocity recovery",
      "unit": 4,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Diffuser velocity recovery** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** With rho=1.2 kg/m3, V1=160 m/s and V2=100 m/s, the ideal static recovery is 9.36 kPa.\n\n**Explicit substitution:** Delta p\u2248(1.2/2)\u00d7(160\u00b2\u2212100\u00b2); therefore **9360 Pa**. Valid only as a constant-density inviscid recovery idealization.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
    },
    {
      "id": "prob-turbomachinery-4-4",
      "title": "Calculation & Verification: Corrected compressor flow and speed",
      "unit": 4,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Corrected compressor flow and speed** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** At m_dot=8 kg/s, T01=330 K, Tref=288.15 K, p01=95 kPa and pref=101.325 kPa, corrected flow is about 9.12 kg/s.\n\n**Explicit substitution:** m_corr=8\u00d7sqrt(330/288.15)/(95/101.325); therefore **9.12 kg/s corrected**. This is a coordinate for a specified reference state, not physical mass flow.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
    },
    {
      "id": "prob-turbomachinery-4-5",
      "title": "Calculation & Verification: Choke and impeller mechanical limits",
      "unit": 4,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Choke and impeller mechanical limits** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** A local absolute flow speed of 340 m/s at 300 K air gives Mach\u22480.98 using gamma=1.4, R=287 J/(kg K).\n\n**Explicit substitution:** a=sqrt(1.4\u00d7287\u00d7300); M=340/a; therefore **a\u2248347.2 m/s; M\u22480.979**. Relative Mach may exceed the absolute Mach and matters at the blade throat.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
    },
    {
      "id": "prob-turbomachinery-5-1",
      "title": "Calculation & Verification: Gas turbine specific work and power",
      "unit": 5,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Gas turbine specific work and power** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** Gas with m_dot=18 kg/s, cp=1.15 kJ/(kg K) and a 210 K total-temperature drop develops about 4.35 MW fluid power.\n\n**Explicit substitution:** P=18\u00d71.15\u00d7210; therefore **4347 kW = 4.347 MW**. The cp is a given mean value over the temperature interval.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
    },
    {
      "id": "prob-turbomachinery-5-2",
      "title": "Calculation & Verification: Turbine isentropic efficiency",
      "unit": 5,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Turbine isentropic efficiency** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** With T01=1100 K, T02=900 K and ideal T02s=865 K, turbine efficiency is about 0.851.\n\n**Explicit substitution:** eta_t=(1100\u2212900)/(1100\u2212865)=200/235; therefore **0.8511**. For a turbine the actual enthalpy drop is less than ideal.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
    },
    {
      "id": "prob-turbomachinery-5-3",
      "title": "Calculation & Verification: Impulse, reaction and stage velocity triangles",
      "unit": 5,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Impulse, reaction and stage velocity triangles** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** At constant U=240 m/s, inlet whirl=160 m/s and exit whirl=-40 m/s, extraction is 48 kJ/kg.\n\n**Explicit substitution:** w=240\u00d7160\u2212240\u00d7(\u221240); therefore **48,000 J/kg**. Rotor extracts power; outlet counter-swirl increases extracted work.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
    },
    {
      "id": "prob-turbomachinery-5-4",
      "title": "Calculation & Verification: Steam expansion, quality and moisture",
      "unit": 5,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Steam expansion, quality and moisture** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** At x=0.90, hg=2600 kJ/kg and hf=200 kJ/kg, mixture enthalpy is 2360 kJ/kg.\n\n**Explicit substitution:** h=0.90\u00d72600+0.10\u00d7200; therefore **2360 kJ/kg**. Saturation quality is mass fraction of vapor.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
    },
    {
      "id": "prob-turbomachinery-5-5",
      "title": "Calculation & Verification: Turbine cooling and net cycle balance",
      "unit": 5,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Turbine cooling and net cycle balance** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** A 12 MW turbine driving a 7.5 MW compressor and 0.4 MW auxiliaries leaves 4.1 MW net before electrical losses.\n\n**Explicit substitution:** P_net=12\u22127.5\u22120.4; therefore **4.1 MW**. Generator and other downstream electrical losses not included.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
    },
    {
      "id": "prob-turbomachinery-6-1",
      "title": "Calculation & Verification: Gross versus net hydraulic head",
      "unit": 6,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Gross versus net hydraulic head** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** A water scheme with 43 m gross head and 5 m penstock losses has 38 m net head at that flow.\n\n**Explicit substitution:** H_net=43\u22125; therefore **38 m**. Penstock friction depends on discharge and must be reassessed off-design.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
    },
    {
      "id": "prob-turbomachinery-6-2",
      "title": "Calculation & Verification: Hydroelectric turbine power and efficiency",
      "unit": 6,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Hydroelectric turbine power and efficiency** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** A plant using Q=2.4 m3/s, H=28 m, rho=1000 kg/m3 and eta_total=0.87 supplies about 573.7 kW.\n\n**Explicit substitution:** P=1000\u00d79.81\u00d72.4\u00d728\u00d70.87/1000; therefore **573.55 kW**. Here total efficiency includes generator loss and is only an assumed value.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
    },
    {
      "id": "prob-turbomachinery-6-3",
      "title": "Calculation & Verification: Impulse turbine jet and runner speed",
      "unit": 6,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Impulse turbine jet and runner speed** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** With H=80 m, ideal water jet speed is about 39.6 m/s before nozzle losses.\n\n**Explicit substitution:** V=sqrt(2\u00d79.81\u00d780); therefore **39.62 m/s ideal**. Actual jet velocity is reduced by nozzle losses.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
    },
    {
      "id": "prob-turbomachinery-6-4",
      "title": "Calculation & Verification: Francis and Kaplan reaction runners",
      "unit": 6,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Francis and Kaplan reaction runners** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** With outlet velocity 6 m/s, recoverable ideal velocity head is 1.84 m before losses.\n\n**Explicit substitution:** V\u00b2/(2g)=6\u00b2/(2\u00d79.81); therefore **1.835 m of velocity head**. Recoverable portion is lower because draft tubes dissipate energy.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
    },
    {
      "id": "prob-turbomachinery-6-5",
      "title": "Calculation & Verification: Runner specific speed and selection",
      "unit": 6,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Runner specific speed and selection** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** Using n=300 rpm, P=500 kW and H=30 m gives a numerical metric about 95.6 in rpm-kW-m convention.\n\n**Explicit substitution:** N_s=300\u00d7sqrt(500)/30^1.25; therefore **95.54 (rpm\u2013kW\u2013m convention)**. Specific-speed values from different numerical conventions must not be compared directly.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
    },
    {
      "id": "prob-turbomachinery-7-1",
      "title": "Calculation & Verification: Centrifugal blade stress scaling",
      "unit": 7,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Centrifugal blade stress scaling** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** For steel-like rho_m=7800 kg/m3 and tip speed 250 m/s, the scaling stress is 487.5 MPa before shape factors.\n\n**Explicit substitution:** sigma_char\u22487800\u00d7250\u00b2; therefore **487.5 MPa**. Characteristic stress scaling is not an allowable stress or burst proof.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
    },
    {
      "id": "prob-turbomachinery-7-2",
      "title": "Calculation & Verification: Rotor unbalance and bearing load",
      "unit": 7,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Rotor unbalance and bearing load** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** An eccentric mass of 0.02 kg at 1 mm radius and 3000 rpm produces about 1.97 N of rotating force.\n\n**Explicit substitution:** F=0.02\u00d70.001\u00d7(2\u03c0\u00d73000/60)\u00b2; therefore **1.974 N**. At twice speed the force becomes four times as large.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
    },
    {
      "id": "prob-turbomachinery-7-3",
      "title": "Calculation & Verification: Critical speed and Campbell diagrams",
      "unit": 7,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Critical speed and Campbell diagrams** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** With stiffness 2.0 MN/m and equivalent mass 50 kg, natural angular frequency is 200 rad/s, about 1910 rpm.\n\n**Explicit substitution:** omega_n=sqrt(2,000,000/50)=200 rad/s; n=omega_n\u00d760/(2\u03c0); therefore **1909.9 rpm**. Real rotors have multiple damped gyroscopic critical speeds.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
    },
    {
      "id": "prob-turbomachinery-7-4",
      "title": "Calculation & Verification: Bearing losses, seals and leakage",
      "unit": 7,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Bearing losses, seals and leakage** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** If bearing torque is 8 N m at 3000 rpm, mechanical dissipation is about 2.51 kW.\n\n**Explicit substitution:** P=8\u00d7(2\u03c0\u00d73000/60); therefore **2513 W = 2.513 kW**. This heat appears in bearings and associated systems, not useful output.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
    },
    {
      "id": "prob-turbomachinery-7-5",
      "title": "Calculation & Verification: Blade fatigue and thermal transients",
      "unit": 7,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Blade fatigue and thermal transients** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** A metal with alpha=12e-6 1/K subjected to a 250 K rise has free strain near 0.003.\n\n**Explicit substitution:** epsilon_free=12\u00d710^(\u22126)\u00d7250; therefore **0.003 or 0.3%**. Restrained expansion and modulus are needed to estimate stress.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
    },
    {
      "id": "prob-turbomachinery-8-1",
      "title": "Calculation & Verification: Design and off-design performance maps",
      "unit": 8,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Design and off-design performance maps** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** A pump at 32 kW hydraulic and 43 kW shaft power operates at eta\u22480.744.\n\n**Explicit substitution:** eta=32/43; therefore **0.7442**. Hydraulic or aerodynamic power and shaft power must share a time boundary.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
    },
    {
      "id": "prob-turbomachinery-8-2",
      "title": "Calculation & Verification: Instrumentation and propagated uncertainty",
      "unit": 8,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Instrumentation and propagated uncertainty** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** A product with 2% independent flow error and 1% head error has \u22482.24% relative standard uncertainty.\n\n**Explicit substitution:** u_rel=sqrt(2\u00b2+1\u00b2); therefore **2.236%**. The root-sum-square is justified only if the errors are independent.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
    },
    {
      "id": "prob-turbomachinery-8-3",
      "title": "Calculation & Verification: Control loops and actuator constraints",
      "unit": 8,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Control loops and actuator constraints** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** A proportional controller with gain 0.15 per kPa sees 10 kPa error and requests a 1.5 unit actuator correction before saturation.\n\n**Explicit substitution:** Delta u=Kp e=0.15\u00d710; therefore **1.5 actuator units**. Saturation and derivative control are not included in this illustrative P action.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
    },
    {
      "id": "prob-turbomachinery-8-4",
      "title": "Calculation & Verification: Condition monitoring and degradation diagnosis",
      "unit": 8,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Condition monitoring and degradation diagnosis** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** Efficiency falling from 0.84 to 0.80 at matched conditions corresponds to 4 percentage points, not 4% relative.\n\n**Explicit substitution:** eta_ref\u2212eta_now=0.84\u22120.80; therefore **0.04 = 4 percentage points**. Relative decrease is 0.04/0.84\u22484.76%, a different statistic.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
    },
    {
      "id": "prob-turbomachinery-8-5",
      "title": "Calculation & Verification: Lifecycle assessment and integrated design review",
      "unit": 8,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Lifecycle assessment and integrated design review** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Teaching case:** A 12 kW mean auxiliary load running 5000 h/y uses 60 MWh/y; at $0.12/kWh its electricity cost is $7200/y.\n\n**Explicit substitution:** E=12 kW\u00d75000 h=60,000 kWh; cost=60,000\u00d70.12; therefore **60 MWh and USD 7200 per year**. No discounted cash flow or maintenance cost is included.\n\nCheck arithmetic independently. Then perturb one input by 10%: linear, quadratic and cubic factors become 1.1, 1.21 and 1.331, respectively. Recompute nonlinear property relationships. An algebraic change is not evidence of a new real-machine operating point.</p></div>"
    }
  ]
};
if (typeof module !== 'undefined') module.exports = COURSE_DATA;
if (typeof window !== 'undefined') window.COURSE_DATA = COURSE_DATA;
