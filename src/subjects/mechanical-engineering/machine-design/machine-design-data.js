/* OpenSTEM Course Data: Machine Design (MDS) */
var COURSE_DATA = {
  "code": "MDS",
  "title": "Machine Design",
  "subtitle": "Stress Concentrations, Fatigue Failure, Shafts, Bearings, Gears, Fasteners, Springs, Clutches & Brakes",
  "units": [
    {
      "number": 1,
      "unitNumber": 1,
      "title": "Design Requirements, Load Paths and Failure Criteria",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Design Requirements, Load Paths and Failure Criteria.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Design Requirements, Load Paths and Failure Criteria.",
      "sections": [
        {
          "id": "sec-1-1",
          "title": "Requirements and acceptance criteria",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**",
          "content": "<p>**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**</p>"
        },
        {
          "id": "sec-1-2",
          "title": "Load spectra and free-body diagrams",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**",
          "content": "<p>**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**</p>"
        },
        {
          "id": "sec-1-3",
          "title": "Equivalent stress and ductile yielding",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**",
          "content": "<p>**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**</p>"
        },
        {
          "id": "sec-1-4",
          "title": "Brittle failure and crack sensitivity",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**",
          "content": "<p>**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**</p>"
        },
        {
          "id": "sec-1-5",
          "title": "Design uncertainty and reliability",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**",
          "content": "<p>**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-machine-design-1-1",
          "title": "Calculation & Verification: Requirements and acceptance criteria",
          "unit": 1,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Requirements and acceptance criteria** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate requirements capacity screening using demand=6.6 kN, allowable=10 kN. Using the explicit\nrelationship for this simplified case, the arithmetic is `6.6/10`. The computed result is **0.66\ndimensionless**. This is a synthetic, rounded result; it is not a measured or independently certified design\ncapacity. Recalculate with an independent calculator before passing it into a later sizing step. A result\noutside a plausible physical range is evidence that units or assumptions may be wrong, not automatically a new\ndiscovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that treating the customer's nominal power rating as\nthe maximum possible shaft load conceals transients. A responsible notebook records both the numerical output\nand the reason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its\nbase value; check whether the response is linear, quadratic or more sensitive, and explain what happens to the\ncorresponding margin.</p></div>"
        },
        {
          "id": "prob-machine-design-1-2",
          "title": "Calculation & Verification: Load spectra and free-body diagrams",
          "unit": 1,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Load spectra and free-body diagrams** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate support bending from pulley force using F=850 N, overhang=0.12 m. Using the explicit\nrelationship for this simplified case, the arithmetic is `850*0.12`. The computed result is **102 N m**. This is\na synthetic, rounded result; it is not a measured or independently certified design capacity. Recalculate with\nan independent calculator before passing it into a later sizing step. A result outside a plausible physical\nrange is evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that omitting the belt radial reaction when sizing the\ninput bearing makes an apparently adequate assembly unreliable. A responsible notebook records both the\nnumerical output and the reason why the model is incomplete. For a learner, try replacing a primary load with\n80% and 120% of its base value; check whether the response is linear, quadratic or more sensitive, and explain\nwhat happens to the corresponding margin.</p></div>"
        },
        {
          "id": "prob-machine-design-1-3",
          "title": "Calculation & Verification: Equivalent stress and ductile yielding",
          "unit": 1,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Equivalent stress and ductile yielding** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate combined nominal elastic stress using normal=110 MPa, shear=40 MPa. Using the explicit\nrelationship for this simplified case, the arithmetic is `sqrt(110**2+3*40**2)`. The computed result is **130\nMPa**. This is a synthetic, rounded result; it is not a measured or independently certified design capacity.\nRecalculate with an independent calculator before passing it into a later sizing step. A result outside a\nplausible physical range is evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that combining stresses with arithmetic addition\ninstead of a justified failure criterion distorts utilization. A responsible notebook records both the numerical\noutput and the reason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120%\nof its base value; check whether the response is linear, quadratic or more sensitive, and explain what happens\nto the corresponding margin.</p></div>"
        },
        {
          "id": "prob-machine-design-1-4",
          "title": "Calculation & Verification: Brittle failure and crack sensitivity",
          "unit": 1,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Brittle failure and crack sensitivity** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate surface-crack intensity screen using Y=1.12, sigma=95 MPa, a=0.002 m. Using the explicit\nrelationship for this simplified case, the arithmetic is `1.12*95*sqrt(pi*0.002)`. The computed result is\n**8.434 MPa sqrt(m)**. This is a synthetic, rounded result; it is not a measured or independently certified\ndesign capacity. Recalculate with an independent calculator before passing it into a later sizing step. A result\noutside a plausible physical range is evidence that units or assumptions may be wrong, not automatically a new\ndiscovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that substituting yield strength for fracture toughness\nignores crack propagation and temperature dependence. A responsible notebook records both the numerical output\nand the reason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its\nbase value; check whether the response is linear, quadratic or more sensitive, and explain what happens to the\ncorresponding margin.</p></div>"
        },
        {
          "id": "prob-machine-design-1-5",
          "title": "Calculation & Verification: Design uncertainty and reliability",
          "unit": 1,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Design uncertainty and reliability** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate uncertainty margin using allowable=145 MPa, prediction=93 MPa. Using the explicit\nrelationship for this simplified case, the arithmetic is `145/93`. The computed result is **1.559\ndimensionless**. This is a synthetic, rounded result; it is not a measured or independently certified design\ncapacity. Recalculate with an independent calculator before passing it into a later sizing step. A result\noutside a plausible physical range is evidence that units or assumptions may be wrong, not automatically a new\ndiscovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that reporting five decimal places in an estimated\nendurance limit falsely implies precision. A responsible notebook records both the numerical output and the\nreason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base\nvalue; check whether the response is linear, quadratic or more sensitive, and explain what happens to the\ncorresponding margin.</p></div>"
        }
      ]
    },
    {
      "number": 2,
      "unitNumber": 2,
      "title": "Shafts, Fits and Torque Transmission",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Shafts, Fits and Torque Transmission.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Shafts, Fits and Torque Transmission.",
      "sections": [
        {
          "id": "sec-2-1",
          "title": "Torsional shear in solid shafts",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**",
          "content": "<p>**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**</p>"
        },
        {
          "id": "sec-2-2",
          "title": "Combined shaft bending and torsion",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**",
          "content": "<p>**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**</p>"
        },
        {
          "id": "sec-2-3",
          "title": "Deflection and rotor alignment",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**",
          "content": "<p>**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**</p>"
        },
        {
          "id": "sec-2-4",
          "title": "Keys, splines and interference fits",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**",
          "content": "<p>**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**</p>"
        },
        {
          "id": "sec-2-5",
          "title": "Couplings and misalignment",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**",
          "content": "<p>**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-machine-design-2-1",
          "title": "Calculation & Verification: Torsional shear in solid shafts",
          "unit": 2,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Torsional shear in solid shafts** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate nominal torsional shaft stress using T=180 N m, diameter=0.032 m. Using the explicit\nrelationship for this simplified case, the arithmetic is `16*180/(pi*0.032**3)/1e6`. The computed result is\n**27.98 MPa**. This is a synthetic, rounded result; it is not a measured or independently certified design\ncapacity. Recalculate with an independent calculator before passing it into a later sizing step. A result\noutside a plausible physical range is evidence that units or assumptions may be wrong, not automatically a new\ndiscovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that calculating with diameter in millimetres while\nusing N*m without conversion creates a billion-fold scale error. A responsible notebook records both the\nnumerical output and the reason why the model is incomplete. For a learner, try replacing a primary load with\n80% and 120% of its base value; check whether the response is linear, quadratic or more sensitive, and explain\nwhat happens to the corresponding margin.</p></div>"
        },
        {
          "id": "prob-machine-design-2-2",
          "title": "Calculation & Verification: Combined shaft bending and torsion",
          "unit": 2,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Combined shaft bending and torsion** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate shaft combined von Mises stress using M=110 N m, T=180 N m, d=0.04 m. Using the explicit\nrelationship for this simplified case, the arithmetic is\n`sqrt((32*110/(pi*0.04**3))**2+3*(16*180/(pi*0.04**3))**2)/1e6`. The computed result is **30.36 MPa**. This is a\nsynthetic, rounded result; it is not a measured or independently certified design capacity. Recalculate with an\nindependent calculator before passing it into a later sizing step. A result outside a plausible physical range\nis evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that applying pure-torsion sizing to a bent shaft\nunderestimates equivalent stress. A responsible notebook records both the numerical output and the reason why\nthe model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base value; check\nwhether the response is linear, quadratic or more sensitive, and explain what happens to the corresponding\nmargin.</p></div>"
        },
        {
          "id": "prob-machine-design-2-3",
          "title": "Calculation & Verification: Deflection and rotor alignment",
          "unit": 2,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Deflection and rotor alignment** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate beam deflection screen using F=500 N, L=0.4 m, E=210 GPa, d=0.025 m. Using the explicit\nrelationship for this simplified case, the arithmetic is `500*0.4**3/(48*210e9*(pi*0.025**4/64))*1e3`. The\ncomputed result is **0.1656 mm**. This is a synthetic, rounded result; it is not a measured or independently\ncertified design capacity. Recalculate with an independent calculator before passing it into a later sizing\nstep. A result outside a plausible physical range is evidence that units or assumptions may be wrong, not\nautomatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that ignoring bearing compliance and concentrated loads\ngives falsely small predicted deflection. A responsible notebook records both the numerical output and the\nreason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base\nvalue; check whether the response is linear, quadratic or more sensitive, and explain what happens to the\ncorresponding margin.</p></div>"
        },
        {
          "id": "prob-machine-design-2-4",
          "title": "Calculation & Verification: Keys, splines and interference fits",
          "unit": 2,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Keys, splines and interference fits** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate parallel key nominal shear using T=120 N m, d=0.03 m, b=0.008 m, L=0.045 m. Using the\nexplicit relationship for this simplified case, the arithmetic is `2*120/(0.03*0.008*0.045)/1e6`. The computed\nresult is **22.22 MPa**. This is a synthetic, rounded result; it is not a measured or independently certified\ndesign capacity. Recalculate with an independent calculator before passing it into a later sizing step. A result\noutside a plausible physical range is evidence that units or assumptions may be wrong, not automatically a new\ndiscovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that using key length without accounting for the actual\nloaded contact length exaggerates capacity. A responsible notebook records both the numerical output and the\nreason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base\nvalue; check whether the response is linear, quadratic or more sensitive, and explain what happens to the\ncorresponding margin.</p></div>"
        },
        {
          "id": "prob-machine-design-2-5",
          "title": "Calculation & Verification: Couplings and misalignment",
          "unit": 2,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Couplings and misalignment** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate coupling transmitted power using torque=110 N m, speed=900 rpm. Using the explicit\nrelationship for this simplified case, the arithmetic is `110*(900*2*pi/60)/1000`. The computed result is\n**10.37 kW**. This is a synthetic, rounded result; it is not a measured or independently certified design\ncapacity. Recalculate with an independent calculator before passing it into a later sizing step. A result\noutside a plausible physical range is evidence that units or assumptions may be wrong, not automatically a new\ndiscovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that choosing a flexible coupling solely from torque\nrating overlooks shaft reactions and speed limits. A responsible notebook records both the numerical output and\nthe reason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its\nbase value; check whether the response is linear, quadratic or more sensitive, and explain what happens to the\ncorresponding margin.</p></div>"
        }
      ]
    },
    {
      "number": 3,
      "unitNumber": 3,
      "title": "Fatigue, Fracture and Durability",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Fatigue, Fracture and Durability.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Fatigue, Fracture and Durability.",
      "sections": [
        {
          "id": "sec-3-1",
          "title": "Stress cycles and amplitude",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**",
          "content": "<p>**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**</p>"
        },
        {
          "id": "sec-3-2",
          "title": "Mean-stress correction",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**",
          "content": "<p>**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**</p>"
        },
        {
          "id": "sec-3-3",
          "title": "Notch effects and fatigue strength",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**",
          "content": "<p>**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**</p>"
        },
        {
          "id": "sec-3-4",
          "title": "Cumulative damage models",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**",
          "content": "<p>**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**</p>"
        },
        {
          "id": "sec-3-5",
          "title": "Wear, fretting and environmental fatigue",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**",
          "content": "<p>**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-machine-design-3-1",
          "title": "Calculation & Verification: Stress cycles and amplitude",
          "unit": 3,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Stress cycles and amplitude** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate alternating normal stress using max=130 MPa, min=-70 MPa. Using the explicit\nrelationship for this simplified case, the arithmetic is `(130-(-70))/2`. The computed result is **100 MPa**.\nThis is a synthetic, rounded result; it is not a measured or independently certified design capacity.\nRecalculate with an independent calculator before passing it into a later sizing step. A result outside a\nplausible physical range is evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that entering peak-to-peak range as amplitude doubles\nthe cyclic stress in the calculation. A responsible notebook records both the numerical output and the reason\nwhy the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base value;\ncheck whether the response is linear, quadratic or more sensitive, and explain what happens to the corresponding\nmargin.</p></div>"
        },
        {
          "id": "prob-machine-design-3-2",
          "title": "Calculation & Verification: Mean-stress correction",
          "unit": 3,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Mean-stress correction** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate Goodman stress utilization using alternating=76 MPa, mean=38 MPa, Se=180 MPa, Sut=520\nMPa. Using the explicit relationship for this simplified case, the arithmetic is `76/180+38/520`. The computed\nresult is **0.4953 dimensionless**. This is a synthetic, rounded result; it is not a measured or independently\ncertified design capacity. Recalculate with an independent calculator before passing it into a later sizing\nstep. A result outside a plausible physical range is evidence that units or assumptions may be wrong, not\nautomatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that extrapolating a Goodman line to compressive mean\nstress or unconventional materials without evidence is unsound. A responsible notebook records both the\nnumerical output and the reason why the model is incomplete. For a learner, try replacing a primary load with\n80% and 120% of its base value; check whether the response is linear, quadratic or more sensitive, and explain\nwhat happens to the corresponding margin.</p></div>"
        },
        {
          "id": "prob-machine-design-3-3",
          "title": "Calculation & Verification: Notch effects and fatigue strength",
          "unit": 3,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Notch effects and fatigue strength** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate fatigue notch concentration using Kt=2.2, q=0.7. Using the explicit relationship for\nthis simplified case, the arithmetic is `1+0.7*(2.2-1)`. The computed result is **1.84 dimensionless**. This is\na synthetic, rounded result; it is not a measured or independently certified design capacity. Recalculate with\nan independent calculator before passing it into a later sizing step. A result outside a plausible physical\nrange is evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that using Kt for static stress but forgetting Kf in\nalternating stress hides fatigue risk. A responsible notebook records both the numerical output and the reason\nwhy the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base value;\ncheck whether the response is linear, quadratic or more sensitive, and explain what happens to the corresponding\nmargin.</p></div>"
        },
        {
          "id": "prob-machine-design-3-4",
          "title": "Calculation & Verification: Cumulative damage models",
          "unit": 3,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Cumulative damage models** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate Miner sum of two bins using n1=10000,N1=100000,n2=20000,N2=200000. Using the explicit\nrelationship for this simplified case, the arithmetic is `10000/100000+20000/200000`. The computed result is\n**0.2 dimensionless**. This is a synthetic, rounded result; it is not a measured or independently certified\ndesign capacity. Recalculate with an independent calculator before passing it into a later sizing step. A result\noutside a plausible physical range is evidence that units or assumptions may be wrong, not automatically a new\ndiscovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that ignoring load sequence, corrosion or overload\ninteractions can make a Miner estimate nonconservative. A responsible notebook records both the numerical output\nand the reason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its\nbase value; check whether the response is linear, quadratic or more sensitive, and explain what happens to the\ncorresponding margin.</p></div>"
        },
        {
          "id": "prob-machine-design-3-5",
          "title": "Calculation & Verification: Wear, fretting and environmental fatigue",
          "unit": 3,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Wear, fretting and environmental fatigue** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate distance accumulated in micro-slip using v=0.00001 m/s, t=12 h. Using the explicit\nrelationship for this simplified case, the arithmetic is `0.00001*12*3600*1000`. The computed result is **432\nmm**. This is a synthetic, rounded result; it is not a measured or independently certified design capacity.\nRecalculate with an independent calculator before passing it into a later sizing step. A result outside a\nplausible physical range is evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that treating seal wear, corrosion and fatigue as\nunrelated independent hazards misses interactions. A responsible notebook records both the numerical output and\nthe reason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its\nbase value; check whether the response is linear, quadratic or more sensitive, and explain what happens to the\ncorresponding margin.</p></div>"
        }
      ]
    },
    {
      "number": 4,
      "unitNumber": 4,
      "title": "Bolted, Welded and Bonded Joints",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Bolted, Welded and Bonded Joints.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Bolted, Welded and Bonded Joints.",
      "sections": [
        {
          "id": "sec-4-1",
          "title": "Bolt preload and tightening scatter",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**",
          "content": "<p>**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**</p>"
        },
        {
          "id": "sec-4-2",
          "title": "Joint stiffness and separation",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**",
          "content": "<p>**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**</p>"
        },
        {
          "id": "sec-4-3",
          "title": "Bolted joint fatigue",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**",
          "content": "<p>**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**</p>"
        },
        {
          "id": "sec-4-4",
          "title": "Weld throat and load groups",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**",
          "content": "<p>**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**</p>"
        },
        {
          "id": "sec-4-5",
          "title": "Adhesive bonding and hybrid joints",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**",
          "content": "<p>**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-machine-design-4-1",
          "title": "Calculation & Verification: Bolt preload and tightening scatter",
          "unit": 4,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Bolt preload and tightening scatter** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate nut-factor torque estimate using K=0.20, preload=12000 N, bolt dia=0.01 m. Using the\nexplicit relationship for this simplified case, the arithmetic is `0.20*12000*0.01`. The computed result is **24\nN m**. This is a synthetic, rounded result; it is not a measured or independently certified design capacity.\nRecalculate with an independent calculator before passing it into a later sizing step. A result outside a\nplausible physical range is evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that assuming an exact torque-to-tension conversion\ndisregards friction variation and reused threads. A responsible notebook records both the numerical output and\nthe reason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its\nbase value; check whether the response is linear, quadratic or more sensitive, and explain what happens to the\ncorresponding margin.</p></div>"
        },
        {
          "id": "prob-machine-design-4-2",
          "title": "Calculation & Verification: Joint stiffness and separation",
          "unit": 4,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Joint stiffness and separation** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate peak bolt force under load using Fi=12000 N, C=0.22, P=4000 N. Using the explicit\nrelationship for this simplified case, the arithmetic is `12000+0.22*4000`. The computed result is **1.288e+04\nN**. This is a synthetic, rounded result; it is not a measured or independently certified design capacity.\nRecalculate with an independent calculator before passing it into a later sizing step. A result outside a\nplausible physical range is evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that applying the entire external force to the bolt\nwhile also ignoring member unloading misstates both fatigue and gasket integrity. A responsible notebook records\nboth the numerical output and the reason why the model is incomplete. For a learner, try replacing a primary\nload with 80% and 120% of its base value; check whether the response is linear, quadratic or more sensitive, and\nexplain what happens to the corresponding margin.</p></div>"
        },
        {
          "id": "prob-machine-design-4-3",
          "title": "Calculation & Verification: Bolted joint fatigue",
          "unit": 4,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Bolted joint fatigue** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate alternating bolt force using C=0.24, external load range=2000 N. Using the explicit\nrelationship for this simplified case, the arithmetic is `0.24*2000/2`. The computed result is **240 N**. This\nis a synthetic, rounded result; it is not a measured or independently certified design capacity. Recalculate\nwith an independent calculator before passing it into a later sizing step. A result outside a plausible physical\nrange is evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that selecting a bolt solely by ultimate strength does\nnot verify thread-root fatigue. A responsible notebook records both the numerical output and the reason why the\nmodel is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base value; check\nwhether the response is linear, quadratic or more sensitive, and explain what happens to the corresponding\nmargin.</p></div>"
        },
        {
          "id": "prob-machine-design-4-4",
          "title": "Calculation & Verification: Weld throat and load groups",
          "unit": 4,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Weld throat and load groups** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate average fillet weld shear using force=12000 N, leg=0.006 m, length=0.14 m. Using the\nexplicit relationship for this simplified case, the arithmetic is `12000/(0.707*0.006*0.14)/1e6`. The computed\nresult is **20.21 MPa**. This is a synthetic, rounded result; it is not a measured or independently certified\ndesign capacity. Recalculate with an independent calculator before passing it into a later sizing step. A result\noutside a plausible physical range is evidence that units or assumptions may be wrong, not automatically a new\ndiscovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that treating a weld's leg size as identical to its\nthroat thickness overstates effective section. A responsible notebook records both the numerical output and the\nreason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base\nvalue; check whether the response is linear, quadratic or more sensitive, and explain what happens to the\ncorresponding margin.</p></div>"
        },
        {
          "id": "prob-machine-design-4-5",
          "title": "Calculation & Verification: Adhesive bonding and hybrid joints",
          "unit": 4,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Adhesive bonding and hybrid joints** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate average lap adhesive shear using force=3000 N, area=0.003 m2. Using the explicit\nrelationship for this simplified case, the arithmetic is `3000/0.003/1e6`. The computed result is **1 MPa**.\nThis is a synthetic, rounded result; it is not a measured or independently certified design capacity.\nRecalculate with an independent calculator before passing it into a later sizing step. A result outside a\nplausible physical range is evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that assuming uniform shear along a lap joint ignores\npeel and stress peaks at overlap ends. A responsible notebook records both the numerical output and the reason\nwhy the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base value;\ncheck whether the response is linear, quadratic or more sensitive, and explain what happens to the corresponding\nmargin.</p></div>"
        }
      ]
    },
    {
      "number": 5,
      "unitNumber": 5,
      "title": "Bearings, Tribology and Sealing",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Bearings, Tribology and Sealing.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Bearings, Tribology and Sealing.",
      "sections": [
        {
          "id": "sec-5-1",
          "title": "Bearing reaction loads",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**",
          "content": "<p>**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**</p>"
        },
        {
          "id": "sec-5-2",
          "title": "Rolling bearing rating life",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**",
          "content": "<p>**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**</p>"
        },
        {
          "id": "sec-5-3",
          "title": "Lubrication regimes and film formation",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**",
          "content": "<p>**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**</p>"
        },
        {
          "id": "sec-5-4",
          "title": "Journal bearing PV and friction",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**",
          "content": "<p>**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**</p>"
        },
        {
          "id": "sec-5-5",
          "title": "Sealing and contamination control",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**",
          "content": "<p>**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-machine-design-5-1",
          "title": "Calculation & Verification: Bearing reaction loads",
          "unit": 5,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Bearing reaction loads** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate symmetric bearing reaction using radial load=1400 N, centered between supports. Using\nthe explicit relationship for this simplified case, the arithmetic is `1400/2`. The computed result is **700\nN**. This is a synthetic, rounded result; it is not a measured or independently certified design capacity.\nRecalculate with an independent calculator before passing it into a later sizing step. A result outside a\nplausible physical range is evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that putting only tangential torque force into the\nbearing calculation neglects radial belt tension. A responsible notebook records both the numerical output and\nthe reason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its\nbase value; check whether the response is linear, quadratic or more sensitive, and explain what happens to the\ncorresponding margin.</p></div>"
        },
        {
          "id": "prob-machine-design-5-2",
          "title": "Calculation & Verification: Rolling bearing rating life",
          "unit": 5,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Rolling bearing rating life** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate ball bearing basic L10 using C=22000 N, P=4500 N, exponent=3. Using the explicit\nrelationship for this simplified case, the arithmetic is `(22000/4500)**3`. The computed result is **116.9\nmillion revolutions**. This is a synthetic, rounded result; it is not a measured or independently certified\ndesign capacity. Recalculate with an independent calculator before passing it into a later sizing step. A result\noutside a plausible physical range is evidence that units or assumptions may be wrong, not automatically a new\ndiscovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that calling L10 a guarantee of service lifetime\ndisregards contamination, lubrication and probability. A responsible notebook records both the numerical output\nand the reason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its\nbase value; check whether the response is linear, quadratic or more sensitive, and explain what happens to the\ncorresponding margin.</p></div>"
        },
        {
          "id": "prob-machine-design-5-3",
          "title": "Calculation & Verification: Lubrication regimes and film formation",
          "unit": 5,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Lubrication regimes and film formation** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate dynamic viscosity using rho=860 kg/m3, nu=65e-6 m2/s. Using the explicit relationship\nfor this simplified case, the arithmetic is `860*65e-6`. The computed result is **0.0559 Pa s**. This is a\nsynthetic, rounded result; it is not a measured or independently certified design capacity. Recalculate with an\nindependent calculator before passing it into a later sizing step. A result outside a plausible physical range\nis evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that using room-temperature viscosity for hot operation\nmay overestimate film thickness. A responsible notebook records both the numerical output and the reason why the\nmodel is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base value; check\nwhether the response is linear, quadratic or more sensitive, and explain what happens to the corresponding\nmargin.</p></div>"
        },
        {
          "id": "prob-machine-design-5-4",
          "title": "Calculation & Verification: Journal bearing PV and friction",
          "unit": 5,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Journal bearing PV and friction** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate journal bearing PV screen using F=600 N, d=0.025 m, L=0.035 m, n=600 rpm. Using the\nexplicit relationship for this simplified case, the arithmetic is `600/(0.025*0.035)*(pi*0.025*600/60)/1e6`. The\ncomputed result is **0.5386 MPa m/s**. This is a synthetic, rounded result; it is not a measured or\nindependently certified design capacity. Recalculate with an independent calculator before passing it into a\nlater sizing step. A result outside a plausible physical range is evidence that units or assumptions may be\nwrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that a low PV value alone does not prove adequate wear\nlife or heat removal. A responsible notebook records both the numerical output and the reason why the model is\nincomplete. For a learner, try replacing a primary load with 80% and 120% of its base value; check whether the\nresponse is linear, quadratic or more sensitive, and explain what happens to the corresponding margin.</p></div>"
        },
        {
          "id": "prob-machine-design-5-5",
          "title": "Calculation & Verification: Sealing and contamination control",
          "unit": 5,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Sealing and contamination control** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate seal surface speed using shaft diameter=0.03 m, speed=900 rpm. Using the explicit\nrelationship for this simplified case, the arithmetic is `pi*0.03*900/60`. The computed result is **1.414 m/s**.\nThis is a synthetic, rounded result; it is not a measured or independently certified design capacity.\nRecalculate with an independent calculator before passing it into a later sizing step. A result outside a\nplausible physical range is evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that choosing seals from nominal bore diameter alone\nignores wear, temperature and shaft finish. A responsible notebook records both the numerical output and the\nreason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base\nvalue; check whether the response is linear, quadratic or more sensitive, and explain what happens to the\ncorresponding margin.</p></div>"
        }
      ]
    },
    {
      "number": 6,
      "unitNumber": 6,
      "title": "Gears, Belts and Powertrains",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Gears, Belts and Powertrains.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Gears, Belts and Powertrains.",
      "sections": [
        {
          "id": "sec-6-1",
          "title": "Involute gearing fundamentals",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**",
          "content": "<p>**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**</p>"
        },
        {
          "id": "sec-6-2",
          "title": "Tangential gear forces",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**",
          "content": "<p>**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**</p>"
        },
        {
          "id": "sec-6-3",
          "title": "Transmission losses and heat",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**",
          "content": "<p>**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**</p>"
        },
        {
          "id": "sec-6-4",
          "title": "Belts, chains and traction",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**",
          "content": "<p>**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**</p>"
        },
        {
          "id": "sec-6-5",
          "title": "Powertrain layout and transient torque",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**",
          "content": "<p>**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-machine-design-6-1",
          "title": "Calculation & Verification: Involute gearing fundamentals",
          "unit": 6,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Involute gearing fundamentals** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate driven gear ratio using driven=80 teeth, driver=20 teeth. Using the explicit\nrelationship for this simplified case, the arithmetic is `80/20`. The computed result is **4 dimensionless**.\nThis is a synthetic, rounded result; it is not a measured or independently certified design capacity.\nRecalculate with an independent calculator before passing it into a later sizing step. A result outside a\nplausible physical range is evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that selecting equal tooth counts for every gear\nwithout checking center distance and undercut is poor design. A responsible notebook records both the numerical\noutput and the reason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120%\nof its base value; check whether the response is linear, quadratic or more sensitive, and explain what happens\nto the corresponding margin.</p></div>"
        },
        {
          "id": "prob-machine-design-6-2",
          "title": "Calculation & Verification: Tangential gear forces",
          "unit": 6,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Tangential gear forces** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate gear tangential force using T=140 N m, pitch diameter=0.12 m. Using the explicit\nrelationship for this simplified case, the arithmetic is `2*140/0.12`. The computed result is **2,333 N**. This\nis a synthetic, rounded result; it is not a measured or independently certified design capacity. Recalculate\nwith an independent calculator before passing it into a later sizing step. A result outside a plausible physical\nrange is evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that ignoring the mesh pressure angle makes bearing\nreaction calculations incomplete. A responsible notebook records both the numerical output and the reason why\nthe model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base value; check\nwhether the response is linear, quadratic or more sensitive, and explain what happens to the corresponding\nmargin.</p></div>"
        },
        {
          "id": "prob-machine-design-6-3",
          "title": "Calculation & Verification: Transmission losses and heat",
          "unit": 6,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Transmission losses and heat** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate lost power estimate using input=5 kW, efficiency=0.93. Using the explicit relationship\nfor this simplified case, the arithmetic is `5*(1-0.93)`. The computed result is **0.35 kW**. This is a\nsynthetic, rounded result; it is not a measured or independently certified design capacity. Recalculate with an\nindependent calculator before passing it into a later sizing step. A result outside a plausible physical range\nis evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that replacing a thermal calculation with efficiency\nalone fails to predict oil temperature. A responsible notebook records both the numerical output and the reason\nwhy the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base value;\ncheck whether the response is linear, quadratic or more sensitive, and explain what happens to the corresponding\nmargin.</p></div>"
        },
        {
          "id": "prob-machine-design-6-4",
          "title": "Calculation & Verification: Belts, chains and traction",
          "unit": 6,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Belts, chains and traction** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate belt capstan ratio using mu=0.30, contact=2.8 rad. Using the explicit relationship for\nthis simplified case, the arithmetic is `exp(0.30*2.8)`. The computed result is **2.316 dimensionless**. This is\na synthetic, rounded result; it is not a measured or independently certified design capacity. Recalculate with\nan independent calculator before passing it into a later sizing step. A result outside a plausible physical\nrange is evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that a belt that transmits nominal torque may slip\nduring startup acceleration. A responsible notebook records both the numerical output and the reason why the\nmodel is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base value; check\nwhether the response is linear, quadratic or more sensitive, and explain what happens to the corresponding\nmargin.</p></div>"
        },
        {
          "id": "prob-machine-design-6-5",
          "title": "Calculation & Verification: Powertrain layout and transient torque",
          "unit": 6,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Powertrain layout and transient torque** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate acceleration torque using J=0.25 kg m2, angular acceleration=32 rad/s2. Using the\nexplicit relationship for this simplified case, the arithmetic is `0.25*32`. The computed result is **8 N m**.\nThis is a synthetic, rounded result; it is not a measured or independently certified design capacity.\nRecalculate with an independent calculator before passing it into a later sizing step. A result outside a\nplausible physical range is evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that selecting a gear reducer from average power while\nignoring acceleration creates overheating or shock risk. A responsible notebook records both the numerical\noutput and the reason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120%\nof its base value; check whether the response is linear, quadratic or more sensitive, and explain what happens\nto the corresponding margin.</p></div>"
        }
      ]
    },
    {
      "number": 7,
      "unitNumber": 7,
      "title": "Springs, Brakes and Energy Storage",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Springs, Brakes and Energy Storage.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Springs, Brakes and Energy Storage.",
      "sections": [
        {
          "id": "sec-7-1",
          "title": "Helical compression spring stiffness",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**",
          "content": "<p>**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**</p>"
        },
        {
          "id": "sec-7-2",
          "title": "Spring stress and buckling",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**",
          "content": "<p>**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**</p>"
        },
        {
          "id": "sec-7-3",
          "title": "Torsion and leaf spring concepts",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**",
          "content": "<p>**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**</p>"
        },
        {
          "id": "sec-7-4",
          "title": "Brakes and clutches",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**",
          "content": "<p>**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**</p>"
        },
        {
          "id": "sec-7-5",
          "title": "Flywheel energy and speed fluctuations",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**",
          "content": "<p>**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-machine-design-7-1",
          "title": "Calculation & Verification: Helical compression spring stiffness",
          "unit": 7,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Helical compression spring stiffness** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate spring nominal rate using G=79000 N/mm2, wire=3 mm, mean coil=22 mm, active=8. Using the\nexplicit relationship for this simplified case, the arithmetic is `79000*3**4/(8*22**3*8)`. The computed result\nis **9.39 N/mm**. This is a synthetic, rounded result; it is not a measured or independently certified design\ncapacity. Recalculate with an independent calculator before passing it into a later sizing step. A result\noutside a plausible physical range is evidence that units or assumptions may be wrong, not automatically a new\ndiscovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that confusing mean coil diameter with outside diameter\ngives misleading rates. A responsible notebook records both the numerical output and the reason why the model is\nincomplete. For a learner, try replacing a primary load with 80% and 120% of its base value; check whether the\nresponse is linear, quadratic or more sensitive, and explain what happens to the corresponding margin.</p></div>"
        },
        {
          "id": "prob-machine-design-7-2",
          "title": "Calculation & Verification: Spring stress and buckling",
          "unit": 7,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Spring stress and buckling** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate nominal spring wire shear using F=250 N, D=0.022 m, wire=0.003 m. Using the explicit\nrelationship for this simplified case, the arithmetic is `8*250*0.022/(pi*0.003**3)/1e6`. The computed result is\n**518.7 MPa**. This is a synthetic, rounded result; it is not a measured or independently certified design\ncapacity. Recalculate with an independent calculator before passing it into a later sizing step. A result\noutside a plausible physical range is evidence that units or assumptions may be wrong, not automatically a new\ndiscovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that checking maximum load but not lateral instability\npermits sudden buckling and interference. A responsible notebook records both the numerical output and the\nreason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base\nvalue; check whether the response is linear, quadratic or more sensitive, and explain what happens to the\ncorresponding margin.</p></div>"
        },
        {
          "id": "prob-machine-design-7-3",
          "title": "Calculation & Verification: Torsion and leaf spring concepts",
          "unit": 7,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Torsion and leaf spring concepts** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate spring stored energy using k=16 N/mm, compression=0.014 m. Using the explicit\nrelationship for this simplified case, the arithmetic is `0.5*16000*0.014**2`. The computed result is **1.568\nJ**. This is a synthetic, rounded result; it is not a measured or independently certified design capacity.\nRecalculate with an independent calculator before passing it into a later sizing step. A result outside a\nplausible physical range is evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that using a compression-spring formula for a torsion\nspring confuses different deformation modes. A responsible notebook records both the numerical output and the\nreason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base\nvalue; check whether the response is linear, quadratic or more sensitive, and explain what happens to the\ncorresponding margin.</p></div>"
        },
        {
          "id": "prob-machine-design-7-4",
          "title": "Calculation & Verification: Brakes and clutches",
          "unit": 7,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Brakes and clutches** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate friction brake ideal torque using mu=0.35, normal=1800 N, effective radius=0.07 m. Using\nthe explicit relationship for this simplified case, the arithmetic is `0.35*1800*0.07`. The computed result is\n**44.1 N m**. This is a synthetic, rounded result; it is not a measured or independently certified design\ncapacity. Recalculate with an independent calculator before passing it into a later sizing step. A result\noutside a plausible physical range is evidence that units or assumptions may be wrong, not automatically a new\ndiscovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that rating a brake only for static holding torque\nignores emergency-stop heat. A responsible notebook records both the numerical output and the reason why the\nmodel is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base value; check\nwhether the response is linear, quadratic or more sensitive, and explain what happens to the corresponding\nmargin.</p></div>"
        },
        {
          "id": "prob-machine-design-7-5",
          "title": "Calculation & Verification: Flywheel energy and speed fluctuations",
          "unit": 7,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Flywheel energy and speed fluctuations** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate flywheel rotational energy using inertia=0.8 kg m2, speed=50 rad/s. Using the explicit\nrelationship for this simplified case, the arithmetic is `0.5*0.8*50**2`. The computed result is **1,000 J**.\nThis is a synthetic, rounded result; it is not a measured or independently certified design capacity.\nRecalculate with an independent calculator before passing it into a later sizing step. A result outside a\nplausible physical range is evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that a large stored-energy wheel creates overspeed\nhazards even with a small nominal motor. A responsible notebook records both the numerical output and the reason\nwhy the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base value;\ncheck whether the response is linear, quadratic or more sensitive, and explain what happens to the corresponding\nmargin.</p></div>"
        }
      ]
    },
    {
      "number": 8,
      "unitNumber": 8,
      "title": "Tolerances, Simulation, Validation and Lifecycle Design",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Tolerances, Simulation, Validation and Lifecycle Design.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Tolerances, Simulation, Validation and Lifecycle Design.",
      "sections": [
        {
          "id": "sec-8-1",
          "title": "Material selection and procurement",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**",
          "content": "<p>**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**</p>"
        },
        {
          "id": "sec-8-2",
          "title": "Fits and tolerance stack-ups",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**",
          "content": "<p>**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**</p>"
        },
        {
          "id": "sec-8-3",
          "title": "Finite element model credibility",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**",
          "content": "<p>**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**</p>"
        },
        {
          "id": "sec-8-4",
          "title": "Design verification and test planning",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**",
          "content": "<p>**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**</p>"
        },
        {
          "id": "sec-8-5",
          "title": "Multiobjective selection and lifecycle",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**",
          "content": "<p>**OpenSTEM Mechanical Engineering \u2014 Machine Design \u00b7 unreviewed educational draft**</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-machine-design-8-1",
          "title": "Calculation & Verification: Material selection and procurement",
          "unit": 8,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Material selection and procurement** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate component mass using density=7850 kg/m3, volume=0.00042 m3. Using the explicit\nrelationship for this simplified case, the arithmetic is `7850*0.00042`. The computed result is **3.297 kg**.\nThis is a synthetic, rounded result; it is not a measured or independently certified design capacity.\nRecalculate with an independent calculator before passing it into a later sizing step. A result outside a\nplausible physical range is evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that copying a catalogue property without specifying\ntemper, processing or inspection lacks traceability. A responsible notebook records both the numerical output\nand the reason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its\nbase value; check whether the response is linear, quadratic or more sensitive, and explain what happens to the\ncorresponding margin.</p></div>"
        },
        {
          "id": "prob-machine-design-8-2",
          "title": "Calculation & Verification: Fits and tolerance stack-ups",
          "unit": 8,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Fits and tolerance stack-ups** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate worst-case diametral clearance using hole min=30.012 mm, shaft max=30.006 mm. Using the\nexplicit relationship for this simplified case, the arithmetic is `30.012-30.006`. The computed result is\n**0.006 mm**. This is a synthetic, rounded result; it is not a measured or independently certified design\ncapacity. Recalculate with an independent calculator before passing it into a later sizing step. A result\noutside a plausible physical range is evidence that units or assumptions may be wrong, not automatically a new\ndiscovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that designing with only nominal dimensions can lead to\nlooseness or excessive interference at extremes. A responsible notebook records both the numerical output and\nthe reason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its\nbase value; check whether the response is linear, quadratic or more sensitive, and explain what happens to the\ncorresponding margin.</p></div>"
        },
        {
          "id": "prob-machine-design-8-3",
          "title": "Calculation & Verification: Finite element model credibility",
          "unit": 8,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Finite element model credibility** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate finite-element mesh change using fine=118 MPa, coarse=130 MPa. Using the explicit\nrelationship for this simplified case, the arithmetic is `abs(118-130)/118*100`. The computed result is **10.17\npercent**. This is a synthetic, rounded result; it is not a measured or independently certified design capacity.\nRecalculate with an independent calculator before passing it into a later sizing step. A result outside a\nplausible physical range is evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that reporting a singular peak without stress-\nconvergence study leads to arbitrary overdesign. A responsible notebook records both the numerical output and\nthe reason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its\nbase value; check whether the response is linear, quadratic or more sensitive, and explain what happens to the\ncorresponding margin.</p></div>"
        },
        {
          "id": "prob-machine-design-8-4",
          "title": "Calculation & Verification: Design verification and test planning",
          "unit": 8,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Design verification and test planning** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate prediction error using measured=84 C, predicted=79 C. Using the explicit relationship\nfor this simplified case, the arithmetic is `abs(84-79)/79*100`. The computed result is **6.329 percent**. This\nis a synthetic, rounded result; it is not a measured or independently certified design capacity. Recalculate\nwith an independent calculator before passing it into a later sizing step. A result outside a plausible physical\nrange is evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that a single successful bench run does not establish\nreliability or production repeatability. A responsible notebook records both the numerical output and the reason\nwhy the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base value;\ncheck whether the response is linear, quadratic or more sensitive, and explain what happens to the corresponding\nmargin.</p></div>"
        },
        {
          "id": "prob-machine-design-8-5",
          "title": "Calculation & Verification: Multiobjective selection and lifecycle",
          "unit": 8,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Multiobjective selection and lifecycle** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate weighted decision score using three normalized scores=0.8,0.6,0.9; weights=0.5,0.3,0.2.\nUsing the explicit relationship for this simplified case, the arithmetic is `0.5*0.8+0.3*0.6+0.2*0.9`. The\ncomputed result is **0.76 dimensionless**. This is a synthetic, rounded result; it is not a measured or\nindependently certified design capacity. Recalculate with an independent calculator before passing it into a\nlater sizing step. A result outside a plausible physical range is evidence that units or assumptions may be\nwrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that minimizing purchase price while ignoring downtime\nand spare-part lead time shifts rather than removes expense. A responsible notebook records both the numerical\noutput and the reason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120%\nof its base value; check whether the response is linear, quadratic or more sensitive, and explain what happens\nto the corresponding margin.</p></div>"
        }
      ]
    }
  ],
  "problems": [
    {
      "id": "prob-machine-design-1-1",
      "title": "Calculation & Verification: Requirements and acceptance criteria",
      "unit": 1,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Requirements and acceptance criteria** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate requirements capacity screening using demand=6.6 kN, allowable=10 kN. Using the explicit\nrelationship for this simplified case, the arithmetic is `6.6/10`. The computed result is **0.66\ndimensionless**. This is a synthetic, rounded result; it is not a measured or independently certified design\ncapacity. Recalculate with an independent calculator before passing it into a later sizing step. A result\noutside a plausible physical range is evidence that units or assumptions may be wrong, not automatically a new\ndiscovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that treating the customer's nominal power rating as\nthe maximum possible shaft load conceals transients. A responsible notebook records both the numerical output\nand the reason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its\nbase value; check whether the response is linear, quadratic or more sensitive, and explain what happens to the\ncorresponding margin.</p></div>"
    },
    {
      "id": "prob-machine-design-1-2",
      "title": "Calculation & Verification: Load spectra and free-body diagrams",
      "unit": 1,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Load spectra and free-body diagrams** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate support bending from pulley force using F=850 N, overhang=0.12 m. Using the explicit\nrelationship for this simplified case, the arithmetic is `850*0.12`. The computed result is **102 N m**. This is\na synthetic, rounded result; it is not a measured or independently certified design capacity. Recalculate with\nan independent calculator before passing it into a later sizing step. A result outside a plausible physical\nrange is evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that omitting the belt radial reaction when sizing the\ninput bearing makes an apparently adequate assembly unreliable. A responsible notebook records both the\nnumerical output and the reason why the model is incomplete. For a learner, try replacing a primary load with\n80% and 120% of its base value; check whether the response is linear, quadratic or more sensitive, and explain\nwhat happens to the corresponding margin.</p></div>"
    },
    {
      "id": "prob-machine-design-1-3",
      "title": "Calculation & Verification: Equivalent stress and ductile yielding",
      "unit": 1,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Equivalent stress and ductile yielding** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate combined nominal elastic stress using normal=110 MPa, shear=40 MPa. Using the explicit\nrelationship for this simplified case, the arithmetic is `sqrt(110**2+3*40**2)`. The computed result is **130\nMPa**. This is a synthetic, rounded result; it is not a measured or independently certified design capacity.\nRecalculate with an independent calculator before passing it into a later sizing step. A result outside a\nplausible physical range is evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that combining stresses with arithmetic addition\ninstead of a justified failure criterion distorts utilization. A responsible notebook records both the numerical\noutput and the reason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120%\nof its base value; check whether the response is linear, quadratic or more sensitive, and explain what happens\nto the corresponding margin.</p></div>"
    },
    {
      "id": "prob-machine-design-1-4",
      "title": "Calculation & Verification: Brittle failure and crack sensitivity",
      "unit": 1,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Brittle failure and crack sensitivity** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate surface-crack intensity screen using Y=1.12, sigma=95 MPa, a=0.002 m. Using the explicit\nrelationship for this simplified case, the arithmetic is `1.12*95*sqrt(pi*0.002)`. The computed result is\n**8.434 MPa sqrt(m)**. This is a synthetic, rounded result; it is not a measured or independently certified\ndesign capacity. Recalculate with an independent calculator before passing it into a later sizing step. A result\noutside a plausible physical range is evidence that units or assumptions may be wrong, not automatically a new\ndiscovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that substituting yield strength for fracture toughness\nignores crack propagation and temperature dependence. A responsible notebook records both the numerical output\nand the reason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its\nbase value; check whether the response is linear, quadratic or more sensitive, and explain what happens to the\ncorresponding margin.</p></div>"
    },
    {
      "id": "prob-machine-design-1-5",
      "title": "Calculation & Verification: Design uncertainty and reliability",
      "unit": 1,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Design uncertainty and reliability** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate uncertainty margin using allowable=145 MPa, prediction=93 MPa. Using the explicit\nrelationship for this simplified case, the arithmetic is `145/93`. The computed result is **1.559\ndimensionless**. This is a synthetic, rounded result; it is not a measured or independently certified design\ncapacity. Recalculate with an independent calculator before passing it into a later sizing step. A result\noutside a plausible physical range is evidence that units or assumptions may be wrong, not automatically a new\ndiscovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that reporting five decimal places in an estimated\nendurance limit falsely implies precision. A responsible notebook records both the numerical output and the\nreason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base\nvalue; check whether the response is linear, quadratic or more sensitive, and explain what happens to the\ncorresponding margin.</p></div>"
    },
    {
      "id": "prob-machine-design-2-1",
      "title": "Calculation & Verification: Torsional shear in solid shafts",
      "unit": 2,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Torsional shear in solid shafts** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate nominal torsional shaft stress using T=180 N m, diameter=0.032 m. Using the explicit\nrelationship for this simplified case, the arithmetic is `16*180/(pi*0.032**3)/1e6`. The computed result is\n**27.98 MPa**. This is a synthetic, rounded result; it is not a measured or independently certified design\ncapacity. Recalculate with an independent calculator before passing it into a later sizing step. A result\noutside a plausible physical range is evidence that units or assumptions may be wrong, not automatically a new\ndiscovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that calculating with diameter in millimetres while\nusing N*m without conversion creates a billion-fold scale error. A responsible notebook records both the\nnumerical output and the reason why the model is incomplete. For a learner, try replacing a primary load with\n80% and 120% of its base value; check whether the response is linear, quadratic or more sensitive, and explain\nwhat happens to the corresponding margin.</p></div>"
    },
    {
      "id": "prob-machine-design-2-2",
      "title": "Calculation & Verification: Combined shaft bending and torsion",
      "unit": 2,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Combined shaft bending and torsion** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate shaft combined von Mises stress using M=110 N m, T=180 N m, d=0.04 m. Using the explicit\nrelationship for this simplified case, the arithmetic is\n`sqrt((32*110/(pi*0.04**3))**2+3*(16*180/(pi*0.04**3))**2)/1e6`. The computed result is **30.36 MPa**. This is a\nsynthetic, rounded result; it is not a measured or independently certified design capacity. Recalculate with an\nindependent calculator before passing it into a later sizing step. A result outside a plausible physical range\nis evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that applying pure-torsion sizing to a bent shaft\nunderestimates equivalent stress. A responsible notebook records both the numerical output and the reason why\nthe model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base value; check\nwhether the response is linear, quadratic or more sensitive, and explain what happens to the corresponding\nmargin.</p></div>"
    },
    {
      "id": "prob-machine-design-2-3",
      "title": "Calculation & Verification: Deflection and rotor alignment",
      "unit": 2,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Deflection and rotor alignment** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate beam deflection screen using F=500 N, L=0.4 m, E=210 GPa, d=0.025 m. Using the explicit\nrelationship for this simplified case, the arithmetic is `500*0.4**3/(48*210e9*(pi*0.025**4/64))*1e3`. The\ncomputed result is **0.1656 mm**. This is a synthetic, rounded result; it is not a measured or independently\ncertified design capacity. Recalculate with an independent calculator before passing it into a later sizing\nstep. A result outside a plausible physical range is evidence that units or assumptions may be wrong, not\nautomatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that ignoring bearing compliance and concentrated loads\ngives falsely small predicted deflection. A responsible notebook records both the numerical output and the\nreason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base\nvalue; check whether the response is linear, quadratic or more sensitive, and explain what happens to the\ncorresponding margin.</p></div>"
    },
    {
      "id": "prob-machine-design-2-4",
      "title": "Calculation & Verification: Keys, splines and interference fits",
      "unit": 2,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Keys, splines and interference fits** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate parallel key nominal shear using T=120 N m, d=0.03 m, b=0.008 m, L=0.045 m. Using the\nexplicit relationship for this simplified case, the arithmetic is `2*120/(0.03*0.008*0.045)/1e6`. The computed\nresult is **22.22 MPa**. This is a synthetic, rounded result; it is not a measured or independently certified\ndesign capacity. Recalculate with an independent calculator before passing it into a later sizing step. A result\noutside a plausible physical range is evidence that units or assumptions may be wrong, not automatically a new\ndiscovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that using key length without accounting for the actual\nloaded contact length exaggerates capacity. A responsible notebook records both the numerical output and the\nreason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base\nvalue; check whether the response is linear, quadratic or more sensitive, and explain what happens to the\ncorresponding margin.</p></div>"
    },
    {
      "id": "prob-machine-design-2-5",
      "title": "Calculation & Verification: Couplings and misalignment",
      "unit": 2,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Couplings and misalignment** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate coupling transmitted power using torque=110 N m, speed=900 rpm. Using the explicit\nrelationship for this simplified case, the arithmetic is `110*(900*2*pi/60)/1000`. The computed result is\n**10.37 kW**. This is a synthetic, rounded result; it is not a measured or independently certified design\ncapacity. Recalculate with an independent calculator before passing it into a later sizing step. A result\noutside a plausible physical range is evidence that units or assumptions may be wrong, not automatically a new\ndiscovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that choosing a flexible coupling solely from torque\nrating overlooks shaft reactions and speed limits. A responsible notebook records both the numerical output and\nthe reason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its\nbase value; check whether the response is linear, quadratic or more sensitive, and explain what happens to the\ncorresponding margin.</p></div>"
    },
    {
      "id": "prob-machine-design-3-1",
      "title": "Calculation & Verification: Stress cycles and amplitude",
      "unit": 3,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Stress cycles and amplitude** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate alternating normal stress using max=130 MPa, min=-70 MPa. Using the explicit\nrelationship for this simplified case, the arithmetic is `(130-(-70))/2`. The computed result is **100 MPa**.\nThis is a synthetic, rounded result; it is not a measured or independently certified design capacity.\nRecalculate with an independent calculator before passing it into a later sizing step. A result outside a\nplausible physical range is evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that entering peak-to-peak range as amplitude doubles\nthe cyclic stress in the calculation. A responsible notebook records both the numerical output and the reason\nwhy the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base value;\ncheck whether the response is linear, quadratic or more sensitive, and explain what happens to the corresponding\nmargin.</p></div>"
    },
    {
      "id": "prob-machine-design-3-2",
      "title": "Calculation & Verification: Mean-stress correction",
      "unit": 3,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Mean-stress correction** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate Goodman stress utilization using alternating=76 MPa, mean=38 MPa, Se=180 MPa, Sut=520\nMPa. Using the explicit relationship for this simplified case, the arithmetic is `76/180+38/520`. The computed\nresult is **0.4953 dimensionless**. This is a synthetic, rounded result; it is not a measured or independently\ncertified design capacity. Recalculate with an independent calculator before passing it into a later sizing\nstep. A result outside a plausible physical range is evidence that units or assumptions may be wrong, not\nautomatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that extrapolating a Goodman line to compressive mean\nstress or unconventional materials without evidence is unsound. A responsible notebook records both the\nnumerical output and the reason why the model is incomplete. For a learner, try replacing a primary load with\n80% and 120% of its base value; check whether the response is linear, quadratic or more sensitive, and explain\nwhat happens to the corresponding margin.</p></div>"
    },
    {
      "id": "prob-machine-design-3-3",
      "title": "Calculation & Verification: Notch effects and fatigue strength",
      "unit": 3,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Notch effects and fatigue strength** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate fatigue notch concentration using Kt=2.2, q=0.7. Using the explicit relationship for\nthis simplified case, the arithmetic is `1+0.7*(2.2-1)`. The computed result is **1.84 dimensionless**. This is\na synthetic, rounded result; it is not a measured or independently certified design capacity. Recalculate with\nan independent calculator before passing it into a later sizing step. A result outside a plausible physical\nrange is evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that using Kt for static stress but forgetting Kf in\nalternating stress hides fatigue risk. A responsible notebook records both the numerical output and the reason\nwhy the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base value;\ncheck whether the response is linear, quadratic or more sensitive, and explain what happens to the corresponding\nmargin.</p></div>"
    },
    {
      "id": "prob-machine-design-3-4",
      "title": "Calculation & Verification: Cumulative damage models",
      "unit": 3,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Cumulative damage models** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate Miner sum of two bins using n1=10000,N1=100000,n2=20000,N2=200000. Using the explicit\nrelationship for this simplified case, the arithmetic is `10000/100000+20000/200000`. The computed result is\n**0.2 dimensionless**. This is a synthetic, rounded result; it is not a measured or independently certified\ndesign capacity. Recalculate with an independent calculator before passing it into a later sizing step. A result\noutside a plausible physical range is evidence that units or assumptions may be wrong, not automatically a new\ndiscovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that ignoring load sequence, corrosion or overload\ninteractions can make a Miner estimate nonconservative. A responsible notebook records both the numerical output\nand the reason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its\nbase value; check whether the response is linear, quadratic or more sensitive, and explain what happens to the\ncorresponding margin.</p></div>"
    },
    {
      "id": "prob-machine-design-3-5",
      "title": "Calculation & Verification: Wear, fretting and environmental fatigue",
      "unit": 3,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Wear, fretting and environmental fatigue** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate distance accumulated in micro-slip using v=0.00001 m/s, t=12 h. Using the explicit\nrelationship for this simplified case, the arithmetic is `0.00001*12*3600*1000`. The computed result is **432\nmm**. This is a synthetic, rounded result; it is not a measured or independently certified design capacity.\nRecalculate with an independent calculator before passing it into a later sizing step. A result outside a\nplausible physical range is evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that treating seal wear, corrosion and fatigue as\nunrelated independent hazards misses interactions. A responsible notebook records both the numerical output and\nthe reason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its\nbase value; check whether the response is linear, quadratic or more sensitive, and explain what happens to the\ncorresponding margin.</p></div>"
    },
    {
      "id": "prob-machine-design-4-1",
      "title": "Calculation & Verification: Bolt preload and tightening scatter",
      "unit": 4,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Bolt preload and tightening scatter** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate nut-factor torque estimate using K=0.20, preload=12000 N, bolt dia=0.01 m. Using the\nexplicit relationship for this simplified case, the arithmetic is `0.20*12000*0.01`. The computed result is **24\nN m**. This is a synthetic, rounded result; it is not a measured or independently certified design capacity.\nRecalculate with an independent calculator before passing it into a later sizing step. A result outside a\nplausible physical range is evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that assuming an exact torque-to-tension conversion\ndisregards friction variation and reused threads. A responsible notebook records both the numerical output and\nthe reason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its\nbase value; check whether the response is linear, quadratic or more sensitive, and explain what happens to the\ncorresponding margin.</p></div>"
    },
    {
      "id": "prob-machine-design-4-2",
      "title": "Calculation & Verification: Joint stiffness and separation",
      "unit": 4,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Joint stiffness and separation** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate peak bolt force under load using Fi=12000 N, C=0.22, P=4000 N. Using the explicit\nrelationship for this simplified case, the arithmetic is `12000+0.22*4000`. The computed result is **1.288e+04\nN**. This is a synthetic, rounded result; it is not a measured or independently certified design capacity.\nRecalculate with an independent calculator before passing it into a later sizing step. A result outside a\nplausible physical range is evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that applying the entire external force to the bolt\nwhile also ignoring member unloading misstates both fatigue and gasket integrity. A responsible notebook records\nboth the numerical output and the reason why the model is incomplete. For a learner, try replacing a primary\nload with 80% and 120% of its base value; check whether the response is linear, quadratic or more sensitive, and\nexplain what happens to the corresponding margin.</p></div>"
    },
    {
      "id": "prob-machine-design-4-3",
      "title": "Calculation & Verification: Bolted joint fatigue",
      "unit": 4,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Bolted joint fatigue** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate alternating bolt force using C=0.24, external load range=2000 N. Using the explicit\nrelationship for this simplified case, the arithmetic is `0.24*2000/2`. The computed result is **240 N**. This\nis a synthetic, rounded result; it is not a measured or independently certified design capacity. Recalculate\nwith an independent calculator before passing it into a later sizing step. A result outside a plausible physical\nrange is evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that selecting a bolt solely by ultimate strength does\nnot verify thread-root fatigue. A responsible notebook records both the numerical output and the reason why the\nmodel is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base value; check\nwhether the response is linear, quadratic or more sensitive, and explain what happens to the corresponding\nmargin.</p></div>"
    },
    {
      "id": "prob-machine-design-4-4",
      "title": "Calculation & Verification: Weld throat and load groups",
      "unit": 4,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Weld throat and load groups** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate average fillet weld shear using force=12000 N, leg=0.006 m, length=0.14 m. Using the\nexplicit relationship for this simplified case, the arithmetic is `12000/(0.707*0.006*0.14)/1e6`. The computed\nresult is **20.21 MPa**. This is a synthetic, rounded result; it is not a measured or independently certified\ndesign capacity. Recalculate with an independent calculator before passing it into a later sizing step. A result\noutside a plausible physical range is evidence that units or assumptions may be wrong, not automatically a new\ndiscovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that treating a weld's leg size as identical to its\nthroat thickness overstates effective section. A responsible notebook records both the numerical output and the\nreason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base\nvalue; check whether the response is linear, quadratic or more sensitive, and explain what happens to the\ncorresponding margin.</p></div>"
    },
    {
      "id": "prob-machine-design-4-5",
      "title": "Calculation & Verification: Adhesive bonding and hybrid joints",
      "unit": 4,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Adhesive bonding and hybrid joints** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate average lap adhesive shear using force=3000 N, area=0.003 m2. Using the explicit\nrelationship for this simplified case, the arithmetic is `3000/0.003/1e6`. The computed result is **1 MPa**.\nThis is a synthetic, rounded result; it is not a measured or independently certified design capacity.\nRecalculate with an independent calculator before passing it into a later sizing step. A result outside a\nplausible physical range is evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that assuming uniform shear along a lap joint ignores\npeel and stress peaks at overlap ends. A responsible notebook records both the numerical output and the reason\nwhy the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base value;\ncheck whether the response is linear, quadratic or more sensitive, and explain what happens to the corresponding\nmargin.</p></div>"
    },
    {
      "id": "prob-machine-design-5-1",
      "title": "Calculation & Verification: Bearing reaction loads",
      "unit": 5,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Bearing reaction loads** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate symmetric bearing reaction using radial load=1400 N, centered between supports. Using\nthe explicit relationship for this simplified case, the arithmetic is `1400/2`. The computed result is **700\nN**. This is a synthetic, rounded result; it is not a measured or independently certified design capacity.\nRecalculate with an independent calculator before passing it into a later sizing step. A result outside a\nplausible physical range is evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that putting only tangential torque force into the\nbearing calculation neglects radial belt tension. A responsible notebook records both the numerical output and\nthe reason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its\nbase value; check whether the response is linear, quadratic or more sensitive, and explain what happens to the\ncorresponding margin.</p></div>"
    },
    {
      "id": "prob-machine-design-5-2",
      "title": "Calculation & Verification: Rolling bearing rating life",
      "unit": 5,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Rolling bearing rating life** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate ball bearing basic L10 using C=22000 N, P=4500 N, exponent=3. Using the explicit\nrelationship for this simplified case, the arithmetic is `(22000/4500)**3`. The computed result is **116.9\nmillion revolutions**. This is a synthetic, rounded result; it is not a measured or independently certified\ndesign capacity. Recalculate with an independent calculator before passing it into a later sizing step. A result\noutside a plausible physical range is evidence that units or assumptions may be wrong, not automatically a new\ndiscovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that calling L10 a guarantee of service lifetime\ndisregards contamination, lubrication and probability. A responsible notebook records both the numerical output\nand the reason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its\nbase value; check whether the response is linear, quadratic or more sensitive, and explain what happens to the\ncorresponding margin.</p></div>"
    },
    {
      "id": "prob-machine-design-5-3",
      "title": "Calculation & Verification: Lubrication regimes and film formation",
      "unit": 5,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Lubrication regimes and film formation** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate dynamic viscosity using rho=860 kg/m3, nu=65e-6 m2/s. Using the explicit relationship\nfor this simplified case, the arithmetic is `860*65e-6`. The computed result is **0.0559 Pa s**. This is a\nsynthetic, rounded result; it is not a measured or independently certified design capacity. Recalculate with an\nindependent calculator before passing it into a later sizing step. A result outside a plausible physical range\nis evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that using room-temperature viscosity for hot operation\nmay overestimate film thickness. A responsible notebook records both the numerical output and the reason why the\nmodel is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base value; check\nwhether the response is linear, quadratic or more sensitive, and explain what happens to the corresponding\nmargin.</p></div>"
    },
    {
      "id": "prob-machine-design-5-4",
      "title": "Calculation & Verification: Journal bearing PV and friction",
      "unit": 5,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Journal bearing PV and friction** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate journal bearing PV screen using F=600 N, d=0.025 m, L=0.035 m, n=600 rpm. Using the\nexplicit relationship for this simplified case, the arithmetic is `600/(0.025*0.035)*(pi*0.025*600/60)/1e6`. The\ncomputed result is **0.5386 MPa m/s**. This is a synthetic, rounded result; it is not a measured or\nindependently certified design capacity. Recalculate with an independent calculator before passing it into a\nlater sizing step. A result outside a plausible physical range is evidence that units or assumptions may be\nwrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that a low PV value alone does not prove adequate wear\nlife or heat removal. A responsible notebook records both the numerical output and the reason why the model is\nincomplete. For a learner, try replacing a primary load with 80% and 120% of its base value; check whether the\nresponse is linear, quadratic or more sensitive, and explain what happens to the corresponding margin.</p></div>"
    },
    {
      "id": "prob-machine-design-5-5",
      "title": "Calculation & Verification: Sealing and contamination control",
      "unit": 5,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Sealing and contamination control** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate seal surface speed using shaft diameter=0.03 m, speed=900 rpm. Using the explicit\nrelationship for this simplified case, the arithmetic is `pi*0.03*900/60`. The computed result is **1.414 m/s**.\nThis is a synthetic, rounded result; it is not a measured or independently certified design capacity.\nRecalculate with an independent calculator before passing it into a later sizing step. A result outside a\nplausible physical range is evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that choosing seals from nominal bore diameter alone\nignores wear, temperature and shaft finish. A responsible notebook records both the numerical output and the\nreason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base\nvalue; check whether the response is linear, quadratic or more sensitive, and explain what happens to the\ncorresponding margin.</p></div>"
    },
    {
      "id": "prob-machine-design-6-1",
      "title": "Calculation & Verification: Involute gearing fundamentals",
      "unit": 6,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Involute gearing fundamentals** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate driven gear ratio using driven=80 teeth, driver=20 teeth. Using the explicit\nrelationship for this simplified case, the arithmetic is `80/20`. The computed result is **4 dimensionless**.\nThis is a synthetic, rounded result; it is not a measured or independently certified design capacity.\nRecalculate with an independent calculator before passing it into a later sizing step. A result outside a\nplausible physical range is evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that selecting equal tooth counts for every gear\nwithout checking center distance and undercut is poor design. A responsible notebook records both the numerical\noutput and the reason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120%\nof its base value; check whether the response is linear, quadratic or more sensitive, and explain what happens\nto the corresponding margin.</p></div>"
    },
    {
      "id": "prob-machine-design-6-2",
      "title": "Calculation & Verification: Tangential gear forces",
      "unit": 6,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Tangential gear forces** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate gear tangential force using T=140 N m, pitch diameter=0.12 m. Using the explicit\nrelationship for this simplified case, the arithmetic is `2*140/0.12`. The computed result is **2,333 N**. This\nis a synthetic, rounded result; it is not a measured or independently certified design capacity. Recalculate\nwith an independent calculator before passing it into a later sizing step. A result outside a plausible physical\nrange is evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that ignoring the mesh pressure angle makes bearing\nreaction calculations incomplete. A responsible notebook records both the numerical output and the reason why\nthe model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base value; check\nwhether the response is linear, quadratic or more sensitive, and explain what happens to the corresponding\nmargin.</p></div>"
    },
    {
      "id": "prob-machine-design-6-3",
      "title": "Calculation & Verification: Transmission losses and heat",
      "unit": 6,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Transmission losses and heat** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate lost power estimate using input=5 kW, efficiency=0.93. Using the explicit relationship\nfor this simplified case, the arithmetic is `5*(1-0.93)`. The computed result is **0.35 kW**. This is a\nsynthetic, rounded result; it is not a measured or independently certified design capacity. Recalculate with an\nindependent calculator before passing it into a later sizing step. A result outside a plausible physical range\nis evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that replacing a thermal calculation with efficiency\nalone fails to predict oil temperature. A responsible notebook records both the numerical output and the reason\nwhy the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base value;\ncheck whether the response is linear, quadratic or more sensitive, and explain what happens to the corresponding\nmargin.</p></div>"
    },
    {
      "id": "prob-machine-design-6-4",
      "title": "Calculation & Verification: Belts, chains and traction",
      "unit": 6,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Belts, chains and traction** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate belt capstan ratio using mu=0.30, contact=2.8 rad. Using the explicit relationship for\nthis simplified case, the arithmetic is `exp(0.30*2.8)`. The computed result is **2.316 dimensionless**. This is\na synthetic, rounded result; it is not a measured or independently certified design capacity. Recalculate with\nan independent calculator before passing it into a later sizing step. A result outside a plausible physical\nrange is evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that a belt that transmits nominal torque may slip\nduring startup acceleration. A responsible notebook records both the numerical output and the reason why the\nmodel is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base value; check\nwhether the response is linear, quadratic or more sensitive, and explain what happens to the corresponding\nmargin.</p></div>"
    },
    {
      "id": "prob-machine-design-6-5",
      "title": "Calculation & Verification: Powertrain layout and transient torque",
      "unit": 6,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Powertrain layout and transient torque** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate acceleration torque using J=0.25 kg m2, angular acceleration=32 rad/s2. Using the\nexplicit relationship for this simplified case, the arithmetic is `0.25*32`. The computed result is **8 N m**.\nThis is a synthetic, rounded result; it is not a measured or independently certified design capacity.\nRecalculate with an independent calculator before passing it into a later sizing step. A result outside a\nplausible physical range is evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that selecting a gear reducer from average power while\nignoring acceleration creates overheating or shock risk. A responsible notebook records both the numerical\noutput and the reason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120%\nof its base value; check whether the response is linear, quadratic or more sensitive, and explain what happens\nto the corresponding margin.</p></div>"
    },
    {
      "id": "prob-machine-design-7-1",
      "title": "Calculation & Verification: Helical compression spring stiffness",
      "unit": 7,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Helical compression spring stiffness** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate spring nominal rate using G=79000 N/mm2, wire=3 mm, mean coil=22 mm, active=8. Using the\nexplicit relationship for this simplified case, the arithmetic is `79000*3**4/(8*22**3*8)`. The computed result\nis **9.39 N/mm**. This is a synthetic, rounded result; it is not a measured or independently certified design\ncapacity. Recalculate with an independent calculator before passing it into a later sizing step. A result\noutside a plausible physical range is evidence that units or assumptions may be wrong, not automatically a new\ndiscovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that confusing mean coil diameter with outside diameter\ngives misleading rates. A responsible notebook records both the numerical output and the reason why the model is\nincomplete. For a learner, try replacing a primary load with 80% and 120% of its base value; check whether the\nresponse is linear, quadratic or more sensitive, and explain what happens to the corresponding margin.</p></div>"
    },
    {
      "id": "prob-machine-design-7-2",
      "title": "Calculation & Verification: Spring stress and buckling",
      "unit": 7,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Spring stress and buckling** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate nominal spring wire shear using F=250 N, D=0.022 m, wire=0.003 m. Using the explicit\nrelationship for this simplified case, the arithmetic is `8*250*0.022/(pi*0.003**3)/1e6`. The computed result is\n**518.7 MPa**. This is a synthetic, rounded result; it is not a measured or independently certified design\ncapacity. Recalculate with an independent calculator before passing it into a later sizing step. A result\noutside a plausible physical range is evidence that units or assumptions may be wrong, not automatically a new\ndiscovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that checking maximum load but not lateral instability\npermits sudden buckling and interference. A responsible notebook records both the numerical output and the\nreason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base\nvalue; check whether the response is linear, quadratic or more sensitive, and explain what happens to the\ncorresponding margin.</p></div>"
    },
    {
      "id": "prob-machine-design-7-3",
      "title": "Calculation & Verification: Torsion and leaf spring concepts",
      "unit": 7,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Torsion and leaf spring concepts** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate spring stored energy using k=16 N/mm, compression=0.014 m. Using the explicit\nrelationship for this simplified case, the arithmetic is `0.5*16000*0.014**2`. The computed result is **1.568\nJ**. This is a synthetic, rounded result; it is not a measured or independently certified design capacity.\nRecalculate with an independent calculator before passing it into a later sizing step. A result outside a\nplausible physical range is evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that using a compression-spring formula for a torsion\nspring confuses different deformation modes. A responsible notebook records both the numerical output and the\nreason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base\nvalue; check whether the response is linear, quadratic or more sensitive, and explain what happens to the\ncorresponding margin.</p></div>"
    },
    {
      "id": "prob-machine-design-7-4",
      "title": "Calculation & Verification: Brakes and clutches",
      "unit": 7,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Brakes and clutches** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate friction brake ideal torque using mu=0.35, normal=1800 N, effective radius=0.07 m. Using\nthe explicit relationship for this simplified case, the arithmetic is `0.35*1800*0.07`. The computed result is\n**44.1 N m**. This is a synthetic, rounded result; it is not a measured or independently certified design\ncapacity. Recalculate with an independent calculator before passing it into a later sizing step. A result\noutside a plausible physical range is evidence that units or assumptions may be wrong, not automatically a new\ndiscovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that rating a brake only for static holding torque\nignores emergency-stop heat. A responsible notebook records both the numerical output and the reason why the\nmodel is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base value; check\nwhether the response is linear, quadratic or more sensitive, and explain what happens to the corresponding\nmargin.</p></div>"
    },
    {
      "id": "prob-machine-design-7-5",
      "title": "Calculation & Verification: Flywheel energy and speed fluctuations",
      "unit": 7,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Flywheel energy and speed fluctuations** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate flywheel rotational energy using inertia=0.8 kg m2, speed=50 rad/s. Using the explicit\nrelationship for this simplified case, the arithmetic is `0.5*0.8*50**2`. The computed result is **1,000 J**.\nThis is a synthetic, rounded result; it is not a measured or independently certified design capacity.\nRecalculate with an independent calculator before passing it into a later sizing step. A result outside a\nplausible physical range is evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that a large stored-energy wheel creates overspeed\nhazards even with a small nominal motor. A responsible notebook records both the numerical output and the reason\nwhy the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base value;\ncheck whether the response is linear, quadratic or more sensitive, and explain what happens to the corresponding\nmargin.</p></div>"
    },
    {
      "id": "prob-machine-design-8-1",
      "title": "Calculation & Verification: Material selection and procurement",
      "unit": 8,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Material selection and procurement** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate component mass using density=7850 kg/m3, volume=0.00042 m3. Using the explicit\nrelationship for this simplified case, the arithmetic is `7850*0.00042`. The computed result is **3.297 kg**.\nThis is a synthetic, rounded result; it is not a measured or independently certified design capacity.\nRecalculate with an independent calculator before passing it into a later sizing step. A result outside a\nplausible physical range is evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that copying a catalogue property without specifying\ntemper, processing or inspection lacks traceability. A responsible notebook records both the numerical output\nand the reason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its\nbase value; check whether the response is linear, quadratic or more sensitive, and explain what happens to the\ncorresponding margin.</p></div>"
    },
    {
      "id": "prob-machine-design-8-2",
      "title": "Calculation & Verification: Fits and tolerance stack-ups",
      "unit": 8,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Fits and tolerance stack-ups** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate worst-case diametral clearance using hole min=30.012 mm, shaft max=30.006 mm. Using the\nexplicit relationship for this simplified case, the arithmetic is `30.012-30.006`. The computed result is\n**0.006 mm**. This is a synthetic, rounded result; it is not a measured or independently certified design\ncapacity. Recalculate with an independent calculator before passing it into a later sizing step. A result\noutside a plausible physical range is evidence that units or assumptions may be wrong, not automatically a new\ndiscovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that designing with only nominal dimensions can lead to\nlooseness or excessive interference at extremes. A responsible notebook records both the numerical output and\nthe reason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its\nbase value; check whether the response is linear, quadratic or more sensitive, and explain what happens to the\ncorresponding margin.</p></div>"
    },
    {
      "id": "prob-machine-design-8-3",
      "title": "Calculation & Verification: Finite element model credibility",
      "unit": 8,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Finite element model credibility** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate finite-element mesh change using fine=118 MPa, coarse=130 MPa. Using the explicit\nrelationship for this simplified case, the arithmetic is `abs(118-130)/118*100`. The computed result is **10.17\npercent**. This is a synthetic, rounded result; it is not a measured or independently certified design capacity.\nRecalculate with an independent calculator before passing it into a later sizing step. A result outside a\nplausible physical range is evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that reporting a singular peak without stress-\nconvergence study leads to arbitrary overdesign. A responsible notebook records both the numerical output and\nthe reason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its\nbase value; check whether the response is linear, quadratic or more sensitive, and explain what happens to the\ncorresponding margin.</p></div>"
    },
    {
      "id": "prob-machine-design-8-4",
      "title": "Calculation & Verification: Design verification and test planning",
      "unit": 8,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Design verification and test planning** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate prediction error using measured=84 C, predicted=79 C. Using the explicit relationship\nfor this simplified case, the arithmetic is `abs(84-79)/79*100`. The computed result is **6.329 percent**. This\nis a synthetic, rounded result; it is not a measured or independently certified design capacity. Recalculate\nwith an independent calculator before passing it into a later sizing step. A result outside a plausible physical\nrange is evidence that units or assumptions may be wrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that a single successful bench run does not establish\nreliability or production repeatability. A responsible notebook records both the numerical output and the reason\nwhy the model is incomplete. For a learner, try replacing a primary load with 80% and 120% of its base value;\ncheck whether the response is linear, quadratic or more sensitive, and explain what happens to the corresponding\nmargin.</p></div>"
    },
    {
      "id": "prob-machine-design-8-5",
      "title": "Calculation & Verification: Multiobjective selection and lifecycle",
      "unit": 8,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Multiobjective selection and lifecycle** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Question:** Calculate weighted decision score using three normalized scores=0.8,0.6,0.9; weights=0.5,0.3,0.2.\nUsing the explicit relationship for this simplified case, the arithmetic is `0.5*0.8+0.3*0.6+0.2*0.9`. The\ncomputed result is **0.76 dimensionless**. This is a synthetic, rounded result; it is not a measured or\nindependently certified design capacity. Recalculate with an independent calculator before passing it into a\nlater sizing step. A result outside a plausible physical range is evidence that units or assumptions may be\nwrong, not automatically a new discovery.\n\n\n**Interpretation:** The number answers only the posed arithmetic question. A design release would require a\ndefined allowable, actual load spectrum, material condition, geometric tolerances and a standard-appropriate\nassessment. The main danger in this particular lesson is that minimizing purchase price while ignoring downtime\nand spare-part lead time shifts rather than removes expense. A responsible notebook records both the numerical\noutput and the reason why the model is incomplete. For a learner, try replacing a primary load with 80% and 120%\nof its base value; check whether the response is linear, quadratic or more sensitive, and explain what happens\nto the corresponding margin.</p></div>"
    }
  ]
};
if (typeof module !== 'undefined') module.exports = COURSE_DATA;
if (typeof window !== 'undefined') window.COURSE_DATA = COURSE_DATA;
