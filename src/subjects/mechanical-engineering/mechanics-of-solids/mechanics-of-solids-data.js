window.COURSE_DATA = {
  "title": "Mechanics of Solids",
  "subtitle": "Stress, Strain, Axial Loading, Torsion, Beam Bending, Deflections, Combined Stresses & Buckling",
  "badge": "Free Interactive Textbook",
  "badgeCredits": "Solid mechanics core",
  "department": "Mechanical Engineering",
  "language": "en",
  "units": [
    {
      "id": "mechanics-of-solids-unit-1",
      "number": 1,
      "title": "Stress, Strain and Elastic Response",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Stress, Strain and Elastic Response.",
      "sections": [
        {
          "secNumber": "1.1",
          "heading": "Traction vectors and cut planes",
          "content": "# Unit 1, Lesson 1 \u2014 Traction vectors and cut planes\n\n**Learning target.** Turn loads and measured dimensional changes into reproducible stress\u2013strain predictions, while distinguishing material behavior from structural geometry. Explain the terms of `sigma_avg=F/A = 24000/(120\u00d710^-6) Pa`, reconstruct the teaching example and identify one condition where the relation must be modified.\n\n## Physical model\n\nCutting an imaginary plane through a loaded solid exposes the force per area transmitted across that plane. Its normal component creates normal stress, and its in-plane component creates shear stress. The traction vector depends on plane orientation even when the underlying stress state is unchanged. Average traction is defensible only over an area for which resultant force and area are both well defined.\n\nThe essential step is to identify what has been idealized. Stress is not directly interchangeable with force; strain is not identical to movement of a distant fixture; and a computed failure index is not an observed failure. Mark the difference between what you assumed, calculated and measured in your notebook.\n\n**Context:** A flat connector plate receives 24 kN normal to a 120 mm\u00b2 net cut section. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.\n\n## Governing relationship and assumptions\n\n**Teaching relation:** `sigma_avg=F/A = 24000/(120\u00d710^-6) Pa`.\n\nA reported modulus, Poisson ratio, or strength is conditional on the tested material condition and specimen history. A laboratory coupon cannot automatically represent a cast surface, welded joint or additively manufactured component. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **traction vectors and cut planes**.\n\nIf the part has a geometric discontinuity, peak local stress may lie far above a cross-sectional average. Document where each area and section property is defined and whether a stress concentration factor is relevant.\n\n## Worked example and interpretation\n\n**Situation:** A flat connector plate receives 24 kN normal to a 120 mm\u00b2 net cut section.\n\n**Equation:** `sigma_avg=F/A = 24000/(120\u00d710^-6) Pa`.\n\n**Reference answer:** **200 MPa**.\n\nReproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.\n\n**Engineering relevance:** Net-section tension checks must be separated from bearing and tear-out checks. Real use requires verified component-specific inputs; this example is not a certified working load.\n\n## Diagnosing a false conclusion\n\n**Common error:** Using gross area when a bolt hole removes part of the net section.\n\nA negative quantity is not by itself a failure: under a defined sign convention, negative axial stress may represent compression and negative strain may represent contraction. What matters is whether the assumed physical constraint can transmit that action. For reliability of material inference, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.\n\n## Exercises and answer criteria\n\n**1. Reconstruct.** Draw the section, mark all inputs and reproduce **200 MPa**, including units.\n\n*Answer guidance:* Use `sigma_avg=F/A = 24000/(120\u00d710^-6) Pa` with correct dimensions. Confirm the sign and the physical meaning of the quantity.\n\n**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.\n\n*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.\n\n**3. Diagnose.** Explain why this error matters: *using gross area when a bolt hole removes part of the net section.* Propose a measurement or alternate equation that exposes it.\n\n*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.\n\n## Transfer to a real engineering study\n\nRecord whether the specimen is isotropic, whether load cycles are present, and whether the stress is a section average or a point value. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.\n",
          "simulations": []
        },
        {
          "secNumber": "1.2",
          "heading": "Engineering and true stress",
          "content": "# Unit 1, Lesson 2 \u2014 Engineering and true stress\n\n**Learning target.** Turn loads and measured dimensional changes into reproducible stress\u2013strain predictions, while distinguishing material behavior from structural geometry. Explain the terms of `sigma_true\u2248sigma_eng(1+e_eng)`, reconstruct the teaching example and identify one condition where the relation must be modified.\n\n## Physical model\n\nEngineering stress uses the original specimen area, while true stress uses instantaneous area. Their difference becomes substantial after plastic deformation and localization. Under uniform volume-preserving plastic deformation before necking, the often-used approximation sigma_true=sigma_eng(1+e_eng) can be useful; it does not extend uncritically past diffuse necking. Data acquisition must specify which quantity was plotted.\n\nUse the structure of the equation to make an advance prediction. Decide which variables the response is proportional to and which enter as powers, reciprocals or geometric factors. This helps expose a unit error before it becomes an engineering conclusion.\n\n**Context:** At 10% engineering strain a specimen carries 300 MPa engineering stress before necking. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.\n\n## Governing relationship and assumptions\n\n**Teaching relation:** `sigma_true\u2248sigma_eng(1+e_eng)`.\n\nA reported modulus, Poisson ratio, or strength is conditional on the tested material condition and specimen history. A laboratory coupon cannot automatically represent a cast surface, welded joint or additively manufactured component. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **engineering and true stress**.\n\nThe model applies over a domain, not to every conceivable physical state. For instance, elastic formulas generally require stresses within an appropriate linear range and strains small enough that deformed geometry does not change the equilibrium appreciably.\n\n## Worked example and interpretation\n\n**Situation:** At 10% engineering strain a specimen carries 300 MPa engineering stress before necking.\n\n**Equation:** `sigma_true\u2248sigma_eng(1+e_eng)`.\n\n**Reference answer:** **330 MPa (uniform-volume approximation)**.\n\nReproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.\n\n**Engineering relevance:** Fitting a plasticity law requires the correct stress and strain measure. Real use requires verified component-specific inputs; this example is not a certified working load.\n\n## Diagnosing a false conclusion\n\n**Common error:** Applying the simple true-stress conversion after necking has made strain highly nonuniform.\n\nLinear elastic predictions cannot be extended beyond yield or into damage without a material law and a method appropriate to those regimes. Temperature and loading rate may change the relevant parameters. For reliability of material inference, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.\n\n## Exercises and answer criteria\n\n**1. Reconstruct.** Draw the section, mark all inputs and reproduce **330 MPa (uniform-volume approximation)**, including units.\n\n*Answer guidance:* Use `sigma_true\u2248sigma_eng(1+e_eng)` with correct dimensions. Confirm the sign and the physical meaning of the quantity.\n\n**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.\n\n*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.\n\n**3. Diagnose.** Explain why this error matters: *applying the simple true-stress conversion after necking has made strain highly nonuniform.* Propose a measurement or alternate equation that exposes it.\n\n*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.\n\n## Transfer to a real engineering study\n\nRecord whether the specimen is isotropic, whether load cycles are present, and whether the stress is a section average or a point value. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.\n",
          "simulations": []
        },
        {
          "secNumber": "1.3",
          "heading": "Axial strain and displacement",
          "content": "# Unit 1, Lesson 3 \u2014 Axial strain and displacement\n\n**Learning target.** Turn loads and measured dimensional changes into reproducible stress\u2013strain predictions, while distinguishing material behavior from structural geometry. Explain the terms of `e=0.125/250`, reconstruct the teaching example and identify one condition where the relation must be modified.\n\n## Physical model\n\nEngineering axial strain e=(L\u2212L0)/L0 is the average extension divided by initial gauge length. A displacement between grips is not necessarily the displacement of a specimen gauge section because the testing machine and fixtures deform. Small strain is a linear approximation to a spatially varying deformation field. State the reference state before comparing two readings.\n\nAn instructive limiting case is one where the load goes to zero, the span approaches zero, the restraint vanishes or the cross-section grows very large. The response should behave consistently with mechanics. A finite nonzero stress with no load may indicate a missing preload or a mathematical mistake.\n\n**Context:** A 250 mm gauge region extends by 0.125 mm. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.\n\n## Governing relationship and assumptions\n\n**Teaching relation:** `e=0.125/250`.\n\nA reported modulus, Poisson ratio, or strength is conditional on the tested material condition and specimen history. A laboratory coupon cannot automatically represent a cast surface, welded joint or additively manufactured component. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **axial strain and displacement**.\n\nAn independent second approach might use a global equilibrium relation, a limiting case, an energy balance or a laboratory reading. It should not merely repeat the same arithmetic with extra decimal places.\n\n## Worked example and interpretation\n\n**Situation:** A 250 mm gauge region extends by 0.125 mm.\n\n**Equation:** `e=0.125/250`.\n\n**Reference answer:** **0.0005 = 500 microstrain**.\n\nReproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.\n\n**Engineering relevance:** Extensometers measure a chosen length, which may exclude grip compliance. Real use requires verified component-specific inputs; this example is not a certified working load.\n\n## Diagnosing a false conclusion\n\n**Common error:** Mixing grip motion with direct gauge-extension measurements.\n\nSafety factors do not cure a mistaken model, incorrectly placed support, unnoticed crack or unrealistic input. Start by verifying the load path and the chosen failure mode. For reliability of material inference, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.\n\n## Exercises and answer criteria\n\n**1. Reconstruct.** Draw the section, mark all inputs and reproduce **0.0005 = 500 microstrain**, including units.\n\n*Answer guidance:* Use `e=0.125/250` with correct dimensions. Confirm the sign and the physical meaning of the quantity.\n\n**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.\n\n*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.\n\n**3. Diagnose.** Explain why this error matters: *mixing grip motion with direct gauge-extension measurements.* Propose a measurement or alternate equation that exposes it.\n\n*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.\n\n## Transfer to a real engineering study\n\nRecord whether the specimen is isotropic, whether load cycles are present, and whether the stress is a section average or a point value. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.\n",
          "simulations": []
        },
        {
          "secNumber": "1.4",
          "heading": "Poisson contraction and elastic constants",
          "content": "# Unit 1, Lesson 4 \u2014 Poisson contraction and elastic constants\n\n**Learning target.** Turn loads and measured dimensional changes into reproducible stress\u2013strain predictions, while distinguishing material behavior from structural geometry. Explain the terms of `e_trans=\u2212nu\u00d7e_axial`, reconstruct the teaching example and identify one condition where the relation must be modified.\n\n## Physical model\n\nFor uniaxial isotropic linear elasticity, lateral strain is approximately minus Poisson ratio times axial strain. This small-strain relation is not a general law for anisotropic composites or nonlinear rubbers. When isotropy is warranted, E, G and Poisson ratio are related by E=2G(1+nu). Admissible elastic constants also respect material stability constraints.\n\nThe word \u201cstrength\u201d is not interchangeable with \u201cstiffness.\u201d Strength concerns exceeding a material or structural limit; stiffness concerns the load-to-deformation relation. Stability and damage mechanisms introduce further limits, which require their own data and assumptions.\n\n**Context:** An isotropic coupon has axial strain 1200 microstrain and nu=0.29. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.\n\n## Governing relationship and assumptions\n\n**Teaching relation:** `e_trans=\u2212nu\u00d7e_axial`.\n\nA reported modulus, Poisson ratio, or strength is conditional on the tested material condition and specimen history. A laboratory coupon cannot automatically represent a cast surface, welded joint or additively manufactured component. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **poisson contraction and elastic constants**.\n\nA true engineering calculation should be independently reproducible from the drawing and a concise input table. Another reader needs to know the sign convention, material assumptions, geometry, force units and exactly which cross-section or point is analyzed.\n\n## Worked example and interpretation\n\n**Situation:** An isotropic coupon has axial strain 1200 microstrain and nu=0.29.\n\n**Equation:** `e_trans=\u2212nu\u00d7e_axial`.\n\n**Reference answer:** **\u2212348 microstrain**.\n\nReproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.\n\n**Engineering relevance:** Lateral gauges provide a cross-check for a reported elastic Poisson ratio. Real use requires verified component-specific inputs; this example is not a certified working load.\n\n## Diagnosing a false conclusion\n\n**Common error:** Assuming transverse strain must always have the same sign as longitudinal strain.\n\nFailure-mode checks are not independent when the same hidden parameter drives all of them. A poor thickness measurement can bias area, area moment and nominal stress together; correlated uncertainties should be handled explicitly. For reliability of material inference, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.\n\n## Exercises and answer criteria\n\n**1. Reconstruct.** Draw the section, mark all inputs and reproduce **\u2212348 microstrain**, including units.\n\n*Answer guidance:* Use `e_trans=\u2212nu\u00d7e_axial` with correct dimensions. Confirm the sign and the physical meaning of the quantity.\n\n**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.\n\n*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.\n\n**3. Diagnose.** Explain why this error matters: *assuming transverse strain must always have the same sign as longitudinal strain.* Propose a measurement or alternate equation that exposes it.\n\n*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.\n\n## Transfer to a real engineering study\n\nRecord whether the specimen is isotropic, whether load cycles are present, and whether the stress is a section average or a point value. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.\n",
          "simulations": []
        },
        {
          "secNumber": "1.5",
          "heading": "Elastic modulus and proportional response",
          "content": "# Unit 1, Lesson 5 \u2014 Elastic modulus and proportional response\n\n**Learning target.** Turn loads and measured dimensional changes into reproducible stress\u2013strain predictions, while distinguishing material behavior from structural geometry. Explain the terms of `E=\u0394sigma/\u0394e`, reconstruct the teaching example and identify one condition where the relation must be modified.\n\n## Physical model\n\nWithin a linear elastic range, E is the slope of stress versus axial strain; it is not yield stress, hardness or ultimate tensile strength. A secant estimate across a nonlinear range can differ from the tangent modulus. Materials with rate or temperature dependence must be characterized at the relevant conditions. Zero-load offsets and fixture displacement can bias an apparent slope.\n\nFor a real joint or machine, the ideal solution is a starting hypothesis. Surface condition, machining tolerances, alignment, residual stress, temperature and spectrum of operating loads can dominate local behavior. Identify a feasible experiment that might falsify the calculation.\n\n**Context:** An elastic specimen increases stress by 80 MPa as strain increases by 0.0004. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.\n\n## Governing relationship and assumptions\n\n**Teaching relation:** `E=\u0394sigma/\u0394e`.\n\nA reported modulus, Poisson ratio, or strength is conditional on the tested material condition and specimen history. A laboratory coupon cannot automatically represent a cast surface, welded joint or additively manufactured component. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **elastic modulus and proportional response**.\n\nChecking the dimensions of each term is necessary but not sufficient. An equation may carry the right SI units while using the wrong load boundary, neutral axis, shear area, material condition, or ideal support type.\n\n## Worked example and interpretation\n\n**Situation:** An elastic specimen increases stress by 80 MPa as strain increases by 0.0004.\n\n**Equation:** `E=\u0394sigma/\u0394e`.\n\n**Reference answer:** **200 GPa**.\n\nReproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.\n\n**Engineering relevance:** A modulus helps predict deformation, but allowable stress requires additional strength data. Real use requires verified component-specific inputs; this example is not a certified working load.\n\n## Diagnosing a false conclusion\n\n**Common error:** Treating elastic stiffness and failure strength as interchangeable material properties.\n\nDo not turn an average calculation into a guarantee of peak stress at holes, shoulders, welds, contact points or cracks. The stress field can be strongly heterogeneous even if force equilibrium is satisfied. For reliability of material inference, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.\n\n## Exercises and answer criteria\n\n**1. Reconstruct.** Draw the section, mark all inputs and reproduce **200 GPa**, including units.\n\n*Answer guidance:* Use `E=\u0394sigma/\u0394e` with correct dimensions. Confirm the sign and the physical meaning of the quantity.\n\n**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.\n\n*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.\n\n**3. Diagnose.** Explain why this error matters: *treating elastic stiffness and failure strength as interchangeable material properties.* Propose a measurement or alternate equation that exposes it.\n\n*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.\n\n## Transfer to a real engineering study\n\nRecord whether the specimen is isotropic, whether load cycles are present, and whether the stress is a section average or a point value. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.\n",
          "simulations": []
        }
      ],
      "problems": [
        {
          "id": "MOS-U1-P1",
          "title": "Traction vectors and cut planes",
          "question": "**Situation:** A flat connector plate receives 24 kN normal to a 120 mm\u00b2 net cut section.",
          "steps": [
            {
              "explanation": "**Equation:** `sigma_avg=F/A = 24000/(120\u00d710^-6) Pa`."
            },
            {
              "explanation": "**Reference answer:** **200 MPa**."
            },
            {
              "explanation": "Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path."
            },
            {
              "explanation": "**Engineering relevance:** Net-section tension checks must be separated from bearing and tear-out checks. Real use requires verified component-specific inputs; this example is not a certified working load."
            }
          ],
          "finalAnswer": "**Engineering relevance:** Net-section tension checks must be separated from bearing and tear-out checks. Real use requires verified component-specific inputs; this example is not a certified working load."
        },
        {
          "id": "MOS-U1-P2",
          "title": "Engineering and true stress",
          "question": "**Situation:** At 10% engineering strain a specimen carries 300 MPa engineering stress before necking.",
          "steps": [
            {
              "explanation": "**Equation:** `sigma_true\u2248sigma_eng(1+e_eng)`."
            },
            {
              "explanation": "**Reference answer:** **330 MPa (uniform-volume approximation)**."
            },
            {
              "explanation": "Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path."
            },
            {
              "explanation": "**Engineering relevance:** Fitting a plasticity law requires the correct stress and strain measure. Real use requires verified component-specific inputs; this example is not a certified working load."
            }
          ],
          "finalAnswer": "**Engineering relevance:** Fitting a plasticity law requires the correct stress and strain measure. Real use requires verified component-specific inputs; this example is not a certified working load."
        },
        {
          "id": "MOS-U1-P3",
          "title": "Axial strain and displacement",
          "question": "**Situation:** A 250 mm gauge region extends by 0.125 mm.",
          "steps": [
            {
              "explanation": "**Equation:** `e=0.125/250`."
            },
            {
              "explanation": "**Reference answer:** **0.0005 = 500 microstrain**."
            },
            {
              "explanation": "Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path."
            },
            {
              "explanation": "**Engineering relevance:** Extensometers measure a chosen length, which may exclude grip compliance. Real use requires verified component-specific inputs; this example is not a certified working load."
            }
          ],
          "finalAnswer": "**Engineering relevance:** Extensometers measure a chosen length, which may exclude grip compliance. Real use requires verified component-specific inputs; this example is not a certified working load."
        },
        {
          "id": "MOS-U1-P4",
          "title": "Poisson contraction and elastic constants",
          "question": "**Situation:** An isotropic coupon has axial strain 1200 microstrain and nu=0.29.",
          "steps": [
            {
              "explanation": "**Equation:** `e_trans=\u2212nu\u00d7e_axial`."
            },
            {
              "explanation": "**Reference answer:** **\u2212348 microstrain**."
            },
            {
              "explanation": "Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path."
            },
            {
              "explanation": "**Engineering relevance:** Lateral gauges provide a cross-check for a reported elastic Poisson ratio. Real use requires verified component-specific inputs; this example is not a certified working load."
            }
          ],
          "finalAnswer": "**Engineering relevance:** Lateral gauges provide a cross-check for a reported elastic Poisson ratio. Real use requires verified component-specific inputs; this example is not a certified working load."
        },
        {
          "id": "MOS-U1-P5",
          "title": "Elastic modulus and proportional response",
          "question": "**Situation:** An elastic specimen increases stress by 80 MPa as strain increases by 0.0004.",
          "steps": [
            {
              "explanation": "**Equation:** `E=\u0394sigma/\u0394e`."
            },
            {
              "explanation": "**Reference answer:** **200 GPa**."
            },
            {
              "explanation": "Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path."
            },
            {
              "explanation": "**Engineering relevance:** A modulus helps predict deformation, but allowable stress requires additional strength data. Real use requires verified component-specific inputs; this example is not a certified working load."
            }
          ],
          "finalAnswer": "**Engineering relevance:** A modulus helps predict deformation, but allowable stress requires additional strength data. Real use requires verified component-specific inputs; this example is not a certified working load."
        }
      ],
      "simulations": [
        "mechanics-of-solids-sim-1"
      ]
    },
    {
      "id": "mechanics-of-solids-unit-2",
      "number": 2,
      "title": "Axial Members and Compatibility",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Axial Members and Compatibility.",
      "sections": [
        {
          "secNumber": "2.1",
          "heading": "Uniform axial bars",
          "content": "# Unit 2, Lesson 1 \u2014 Uniform axial bars\n\n**Learning target.** Calculate elastic axial shortening or extension and resolve load redistribution caused by assembly constraints and temperature. Explain the terms of `\u03b4=PL/(AE)`, reconstruct the teaching example and identify one condition where the relation must be modified.\n\n## Physical model\n\nAxial elongation for a prismatic straight elastic member under uniform force follows \u03b4=PL/(AE). The load P must be the internal axial force; externally applied loads can redistribute when other members participate. The formula assumes small strain and constant E and A throughout the segment. Use a consistent unit system or the dimensions will silently be wrong.\n\nThe essential step is to identify what has been idealized. Stress is not directly interchangeable with force; strain is not identical to movement of a distant fixture; and a computed failure index is not an observed failure. Mark the difference between what you assumed, calculated and measured in your notebook.\n\n**Context:** A steel bar of length 2 m, area 400 mm\u00b2, E=200 GPa, carries 20 kN tension. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.\n\n## Governing relationship and assumptions\n\n**Teaching relation:** `\u03b4=PL/(AE)`.\n\nA correctly balanced set of axial forces can still violate the physical constraint that two fastened points move together. A rigid-plate assumption can be checked by measuring relative displacements. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **uniform axial bars**.\n\nIf the part has a geometric discontinuity, peak local stress may lie far above a cross-sectional average. Document where each area and section property is defined and whether a stress concentration factor is relevant.\n\n## Worked example and interpretation\n\n**Situation:** A steel bar of length 2 m, area 400 mm\u00b2, E=200 GPa, carries 20 kN tension.\n\n**Equation:** `\u03b4=PL/(AE)`.\n\n**Reference answer:** **0.5 mm extension**.\n\nReproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.\n\n**Engineering relevance:** Tie rods require both allowable tensile stress and alignment displacement checks. Real use requires verified component-specific inputs; this example is not a certified working load.\n\n## Diagnosing a false conclusion\n\n**Common error:** Using E=200 as though it were measured in pascals.\n\nA negative quantity is not by itself a failure: under a defined sign convention, negative axial stress may represent compression and negative strain may represent contraction. What matters is whether the assumed physical constraint can transmit that action. For compatibility of connected parts, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.\n\n## Exercises and answer criteria\n\n**1. Reconstruct.** Draw the section, mark all inputs and reproduce **0.5 mm extension**, including units.\n\n*Answer guidance:* Use `\u03b4=PL/(AE)` with correct dimensions. Confirm the sign and the physical meaning of the quantity.\n\n**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.\n\n*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.\n\n**3. Diagnose.** Explain why this error matters: *using e=200 as though it were measured in pascals.* Propose a measurement or alternate equation that exposes it.\n\n*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.\n\n## Transfer to a real engineering study\n\nConfirm whether temperature, preload, and contact slip change the reference length before reusing the formula. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.\n",
          "simulations": []
        },
        {
          "secNumber": "2.2",
          "heading": "Stepped members and internal force variation",
          "content": "# Unit 2, Lesson 2 \u2014 Stepped members and internal force variation\n\n**Learning target.** Calculate elastic axial shortening or extension and resolve load redistribution caused by assembly constraints and temperature. Explain the terms of `\u03b4_total=\u03b41+\u03b42`, reconstruct the teaching example and identify one condition where the relation must be modified.\n\n## Physical model\n\nFor a succession of prismatic elements, sum each segment elongation \u03b4_i=P_i L_i/(A_i E_i). It is unsafe to use one global P when forces enter at intermediate nodes. A cross-section cut finds the force in the segment and the equilibrium of its separated piece. If a bar has varying area, the corresponding limit is an axial integral.\n\nUse the structure of the equation to make an advance prediction. Decide which variables the response is proportional to and which enter as powers, reciprocals or geometric factors. This helps expose a unit error before it becomes an engineering conclusion.\n\n**Context:** Two same-force segments extend 0.3 mm and 0.5 mm respectively. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.\n\n## Governing relationship and assumptions\n\n**Teaching relation:** `\u03b4_total=\u03b41+\u03b42`.\n\nA correctly balanced set of axial forces can still violate the physical constraint that two fastened points move together. A rigid-plate assumption can be checked by measuring relative displacements. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **stepped members and internal force variation**.\n\nThe model applies over a domain, not to every conceivable physical state. For instance, elastic formulas generally require stresses within an appropriate linear range and strains small enough that deformed geometry does not change the equilibrium appreciably.\n\n## Worked example and interpretation\n\n**Situation:** Two same-force segments extend 0.3 mm and 0.5 mm respectively.\n\n**Equation:** `\u03b4_total=\u03b41+\u03b42`.\n\n**Reference answer:** **0.8 mm**.\n\nReproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.\n\n**Engineering relevance:** A transition of cross-section often drives peak stress even when its length is short. Real use requires verified component-specific inputs; this example is not a certified working load.\n\n## Diagnosing a false conclusion\n\n**Common error:** Averaging segment areas before calculating deformation in a variable-area bar.\n\nLinear elastic predictions cannot be extended beyond yield or into damage without a material law and a method appropriate to those regimes. Temperature and loading rate may change the relevant parameters. For compatibility of connected parts, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.\n\n## Exercises and answer criteria\n\n**1. Reconstruct.** Draw the section, mark all inputs and reproduce **0.8 mm**, including units.\n\n*Answer guidance:* Use `\u03b4_total=\u03b41+\u03b42` with correct dimensions. Confirm the sign and the physical meaning of the quantity.\n\n**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.\n\n*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.\n\n**3. Diagnose.** Explain why this error matters: *averaging segment areas before calculating deformation in a variable-area bar.* Propose a measurement or alternate equation that exposes it.\n\n*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.\n\n## Transfer to a real engineering study\n\nConfirm whether temperature, preload, and contact slip change the reference length before reusing the formula. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.\n",
          "simulations": []
        },
        {
          "secNumber": "2.3",
          "heading": "Restricted thermal expansion",
          "content": "# Unit 2, Lesson 3 \u2014 Restricted thermal expansion\n\n**Learning target.** Calculate elastic axial shortening or extension and resolve load redistribution caused by assembly constraints and temperature. Explain the terms of `sigma=\u2212E alpha \u0394T`, reconstruct the teaching example and identify one condition where the relation must be modified.\n\n## Physical model\n\nA free bar can expand by \u03b1L\u0394T without developing mechanical thermal stress. A fully restrained uniform linear elastic bar develops stress of magnitude E\u03b1|\u0394T|, with compression on heating. Compliance of supports or plastic flow reduces or redistributes the stress. Temperature gradients may bend or distort a member even if average temperature is known.\n\nAn instructive limiting case is one where the load goes to zero, the span approaches zero, the restraint vanishes or the cross-section grows very large. The response should behave consistently with mechanics. A finite nonzero stress with no load may indicate a missing preload or a mathematical mistake.\n\n**Context:** A fully fixed steel bar has E=200 GPa, alpha=12e-6/K and temperature rise 40 K. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.\n\n## Governing relationship and assumptions\n\n**Teaching relation:** `sigma=\u2212E alpha \u0394T`.\n\nA correctly balanced set of axial forces can still violate the physical constraint that two fastened points move together. A rigid-plate assumption can be checked by measuring relative displacements. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **restricted thermal expansion**.\n\nAn independent second approach might use a global equilibrium relation, a limiting case, an energy balance or a laboratory reading. It should not merely repeat the same arithmetic with extra decimal places.\n\n## Worked example and interpretation\n\n**Situation:** A fully fixed steel bar has E=200 GPa, alpha=12e-6/K and temperature rise 40 K.\n\n**Equation:** `sigma=\u2212E alpha \u0394T`.\n\n**Reference answer:** **\u221296 MPa compressive**.\n\nReproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.\n\n**Engineering relevance:** Thermal restraints in machine frames need a temperature-dependent stress evaluation. Real use requires verified component-specific inputs; this example is not a certified working load.\n\n## Diagnosing a false conclusion\n\n**Common error:** Assigning thermal stress to an otherwise free, unconstrained bar.\n\nSafety factors do not cure a mistaken model, incorrectly placed support, unnoticed crack or unrealistic input. Start by verifying the load path and the chosen failure mode. For compatibility of connected parts, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.\n\n## Exercises and answer criteria\n\n**1. Reconstruct.** Draw the section, mark all inputs and reproduce **\u221296 MPa compressive**, including units.\n\n*Answer guidance:* Use `sigma=\u2212E alpha \u0394T` with correct dimensions. Confirm the sign and the physical meaning of the quantity.\n\n**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.\n\n*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.\n\n**3. Diagnose.** Explain why this error matters: *assigning thermal stress to an otherwise free, unconstrained bar.* Propose a measurement or alternate equation that exposes it.\n\n*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.\n\n## Transfer to a real engineering study\n\nConfirm whether temperature, preload, and contact slip change the reference length before reusing the formula. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.\n",
          "simulations": []
        },
        {
          "secNumber": "2.4",
          "heading": "Parallel rods and rigid plates",
          "content": "# Unit 2, Lesson 4 \u2014 Parallel rods and rigid plates\n\n**Learning target.** Calculate elastic axial shortening or extension and resolve load redistribution caused by assembly constraints and temperature. Explain the terms of `P1=50\u00d740/(40+60)`, reconstruct the teaching example and identify one condition where the relation must be modified.\n\n## Physical model\n\nWhen rigid end plates force connected rods to experience equal displacement, load shares in proportion to each rod axial stiffness EA/L under small linear response. Force balance alone does not fix the split. For dissimilar materials their thermal strains can also create self-equilibrated forces. Check both the force sum and identical end displacement as independent constraints.\n\nThe word \u201cstrength\u201d is not interchangeable with \u201cstiffness.\u201d Strength concerns exceeding a material or structural limit; stiffness concerns the load-to-deformation relation. Stability and damage mechanisms introduce further limits, which require their own data and assumptions.\n\n**Context:** Two rods have axial stiffness 40 and 60 kN/mm and share 50 kN. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.\n\n## Governing relationship and assumptions\n\n**Teaching relation:** `P1=50\u00d740/(40+60)`.\n\nA correctly balanced set of axial forces can still violate the physical constraint that two fastened points move together. A rigid-plate assumption can be checked by measuring relative displacements. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **parallel rods and rigid plates**.\n\nA true engineering calculation should be independently reproducible from the drawing and a concise input table. Another reader needs to know the sign convention, material assumptions, geometry, force units and exactly which cross-section or point is analyzed.\n\n## Worked example and interpretation\n\n**Situation:** Two rods have axial stiffness 40 and 60 kN/mm and share 50 kN.\n\n**Equation:** `P1=50\u00d740/(40+60)`.\n\n**Reference answer:** **20 kN in the first rod**.\n\nReproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.\n\n**Engineering relevance:** Bolted parallel load paths can become uneven as connections settle. Real use requires verified component-specific inputs; this example is not a certified working load.\n\n## Diagnosing a false conclusion\n\n**Common error:** Dividing the load equally without checking stiffness.\n\nFailure-mode checks are not independent when the same hidden parameter drives all of them. A poor thickness measurement can bias area, area moment and nominal stress together; correlated uncertainties should be handled explicitly. For compatibility of connected parts, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.\n\n## Exercises and answer criteria\n\n**1. Reconstruct.** Draw the section, mark all inputs and reproduce **20 kN in the first rod**, including units.\n\n*Answer guidance:* Use `P1=50\u00d740/(40+60)` with correct dimensions. Confirm the sign and the physical meaning of the quantity.\n\n**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.\n\n*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.\n\n**3. Diagnose.** Explain why this error matters: *dividing the load equally without checking stiffness.* Propose a measurement or alternate equation that exposes it.\n\n*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.\n\n## Transfer to a real engineering study\n\nConfirm whether temperature, preload, and contact slip change the reference length before reusing the formula. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.\n",
          "simulations": []
        },
        {
          "secNumber": "2.5",
          "heading": "Shear pins and joint bearing",
          "content": "# Unit 2, Lesson 5 \u2014 Shear pins and joint bearing\n\n**Learning target.** Calculate elastic axial shortening or extension and resolve load redistribution caused by assembly constraints and temperature. Explain the terms of `tau=F/(2\u03c0d\u00b2/4)`, reconstruct the teaching example and identify one condition where the relation must be modified.\n\n## Physical model\n\nConnections can control strength while the attached bars remain elastic. Average shear in a pin is transmitted force divided by resisting shear area; a double-shear configuration has two effective planes if each plane is engaged as idealized. Bearing pressure on a plate involves projected pin diameter times plate thickness. Neither average stress resolves edge tear-out or bending in a long pin.\n\nFor a real joint or machine, the ideal solution is a starting hypothesis. Surface condition, machining tolerances, alignment, residual stress, temperature and spectrum of operating loads can dominate local behavior. Identify a feasible experiment that might falsify the calculation.\n\n**Context:** A 12 mm diameter pin carries 18 kN in ideal double shear. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.\n\n## Governing relationship and assumptions\n\n**Teaching relation:** `tau=F/(2\u03c0d\u00b2/4)`.\n\nA correctly balanced set of axial forces can still violate the physical constraint that two fastened points move together. A rigid-plate assumption can be checked by measuring relative displacements. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **shear pins and joint bearing**.\n\nChecking the dimensions of each term is necessary but not sufficient. An equation may carry the right SI units while using the wrong load boundary, neutral axis, shear area, material condition, or ideal support type.\n\n## Worked example and interpretation\n\n**Situation:** A 12 mm diameter pin carries 18 kN in ideal double shear.\n\n**Equation:** `tau=F/(2\u03c0d\u00b2/4)`.\n\n**Reference answer:** **79.58 MPa average shear**.\n\nReproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.\n\n**Engineering relevance:** A pin selection also needs bearing, clearance, fatigue and edge-distance assessment. Real use requires verified component-specific inputs; this example is not a certified working load.\n\n## Diagnosing a false conclusion\n\n**Common error:** Using a single shear plane for an ideal double-shear clevis.\n\nDo not turn an average calculation into a guarantee of peak stress at holes, shoulders, welds, contact points or cracks. The stress field can be strongly heterogeneous even if force equilibrium is satisfied. For compatibility of connected parts, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.\n\n## Exercises and answer criteria\n\n**1. Reconstruct.** Draw the section, mark all inputs and reproduce **79.58 MPa average shear**, including units.\n\n*Answer guidance:* Use `tau=F/(2\u03c0d\u00b2/4)` with correct dimensions. Confirm the sign and the physical meaning of the quantity.\n\n**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.\n\n*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.\n\n**3. Diagnose.** Explain why this error matters: *using a single shear plane for an ideal double-shear clevis.* Propose a measurement or alternate equation that exposes it.\n\n*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.\n\n## Transfer to a real engineering study\n\nConfirm whether temperature, preload, and contact slip change the reference length before reusing the formula. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.\n",
          "simulations": []
        }
      ],
      "problems": [
        {
          "id": "MOS-U2-P1",
          "title": "Uniform axial bars",
          "question": "**Situation:** A steel bar of length 2 m, area 400 mm\u00b2, E=200 GPa, carries 20 kN tension.",
          "steps": [
            {
              "explanation": "**Equation:** `\u03b4=PL/(AE)`."
            },
            {
              "explanation": "**Reference answer:** **0.5 mm extension**."
            },
            {
              "explanation": "Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path."
            },
            {
              "explanation": "**Engineering relevance:** Tie rods require both allowable tensile stress and alignment displacement checks. Real use requires verified component-specific inputs; this example is not a certified working load."
            }
          ],
          "finalAnswer": "**Engineering relevance:** Tie rods require both allowable tensile stress and alignment displacement checks. Real use requires verified component-specific inputs; this example is not a certified working load."
        },
        {
          "id": "MOS-U2-P2",
          "title": "Stepped members and internal force variation",
          "question": "**Situation:** Two same-force segments extend 0.3 mm and 0.5 mm respectively.",
          "steps": [
            {
              "explanation": "**Equation:** `\u03b4_total=\u03b41+\u03b42`."
            },
            {
              "explanation": "**Reference answer:** **0.8 mm**."
            },
            {
              "explanation": "Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path."
            },
            {
              "explanation": "**Engineering relevance:** A transition of cross-section often drives peak stress even when its length is short. Real use requires verified component-specific inputs; this example is not a certified working load."
            }
          ],
          "finalAnswer": "**Engineering relevance:** A transition of cross-section often drives peak stress even when its length is short. Real use requires verified component-specific inputs; this example is not a certified working load."
        },
        {
          "id": "MOS-U2-P3",
          "title": "Restricted thermal expansion",
          "question": "**Situation:** A fully fixed steel bar has E=200 GPa, alpha=12e-6/K and temperature rise 40 K.",
          "steps": [
            {
              "explanation": "**Equation:** `sigma=\u2212E alpha \u0394T`."
            },
            {
              "explanation": "**Reference answer:** **\u221296 MPa compressive**."
            },
            {
              "explanation": "Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path."
            },
            {
              "explanation": "**Engineering relevance:** Thermal restraints in machine frames need a temperature-dependent stress evaluation. Real use requires verified component-specific inputs; this example is not a certified working load."
            }
          ],
          "finalAnswer": "**Engineering relevance:** Thermal restraints in machine frames need a temperature-dependent stress evaluation. Real use requires verified component-specific inputs; this example is not a certified working load."
        },
        {
          "id": "MOS-U2-P4",
          "title": "Parallel rods and rigid plates",
          "question": "**Situation:** Two rods have axial stiffness 40 and 60 kN/mm and share 50 kN.",
          "steps": [
            {
              "explanation": "**Equation:** `P1=50\u00d740/(40+60)`."
            },
            {
              "explanation": "**Reference answer:** **20 kN in the first rod**."
            },
            {
              "explanation": "Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path."
            },
            {
              "explanation": "**Engineering relevance:** Bolted parallel load paths can become uneven as connections settle. Real use requires verified component-specific inputs; this example is not a certified working load."
            }
          ],
          "finalAnswer": "**Engineering relevance:** Bolted parallel load paths can become uneven as connections settle. Real use requires verified component-specific inputs; this example is not a certified working load."
        },
        {
          "id": "MOS-U2-P5",
          "title": "Shear pins and joint bearing",
          "question": "**Situation:** A 12 mm diameter pin carries 18 kN in ideal double shear.",
          "steps": [
            {
              "explanation": "**Equation:** `tau=F/(2\u03c0d\u00b2/4)`."
            },
            {
              "explanation": "**Reference answer:** **79.58 MPa average shear**."
            },
            {
              "explanation": "Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path."
            },
            {
              "explanation": "**Engineering relevance:** A pin selection also needs bearing, clearance, fatigue and edge-distance assessment. Real use requires verified component-specific inputs; this example is not a certified working load."
            }
          ],
          "finalAnswer": "**Engineering relevance:** A pin selection also needs bearing, clearance, fatigue and edge-distance assessment. Real use requires verified component-specific inputs; this example is not a certified working load."
        }
      ],
      "simulations": [
        "mechanics-of-solids-sim-2"
      ]
    },
    {
      "id": "mechanics-of-solids-unit-3",
      "number": 3,
      "title": "Shafts, Shear and Torsion",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Shafts, Shear and Torsion.",
      "sections": [
        {
          "secNumber": "3.1",
          "heading": "Shear stress in solid circular shafts",
          "content": "# Unit 3, Lesson 1 \u2014 Shear stress in solid circular shafts\n\n**Learning target.** Connect transmitted torque to shear stress, angle of twist and load transfer through sections and connections. Explain the terms of `tau_max=16T/(\u03c0d\u00b3)`, reconstruct the teaching example and identify one condition where the relation must be modified.\n\n## Physical model\n\nFor a linearly elastic circular shaft under uniform torsion, tau(r)=Tr/J and reaches its maximum at the surface. For a solid round, J=\u03c0d\u2074/32 so tau_max=16T/(\u03c0d\u00b3). This theory assumes Saint-Venant torsion, a sufficient length away from discontinuities and no significant restrained warping. A keyway can dominate actual local stress.\n\nThe essential step is to identify what has been idealized. Stress is not directly interchangeable with force; strain is not identical to movement of a distant fixture; and a computed failure index is not an observed failure. Mark the difference between what you assumed, calculated and measured in your notebook.\n\n**Context:** A solid round shaft of diameter 30 mm carries torque 400 N m. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.\n\n## Governing relationship and assumptions\n\n**Teaching relation:** `tau_max=16T/(\u03c0d\u00b3)`.\n\nStiffness and nominal stress often scale differently with diameter: torsional stiffness varies as d to the fourth power while peak solid-shaft torsional stress varies inversely as d cubed. A transition or keyway destroys the smooth uniform geometry. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **shear stress in solid circular shafts**.\n\nIf the part has a geometric discontinuity, peak local stress may lie far above a cross-sectional average. Document where each area and section property is defined and whether a stress concentration factor is relevant.\n\n## Worked example and interpretation\n\n**Situation:** A solid round shaft of diameter 30 mm carries torque 400 N m.\n\n**Equation:** `tau_max=16T/(\u03c0d\u00b3)`.\n\n**Reference answer:** **75.45 MPa**.\n\nReproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.\n\n**Engineering relevance:** A motor shaft must transmit peak transient torque, not only nominal steady torque. Real use requires verified component-specific inputs; this example is not a certified working load.\n\n## Diagnosing a false conclusion\n\n**Common error:** Using area I=\u03c0d\u2074/64 instead of polar J=\u03c0d\u2074/32.\n\nA negative quantity is not by itself a failure: under a defined sign convention, negative axial stress may represent compression and negative strain may represent contraction. What matters is whether the assumed physical constraint can transmit that action. For geometry at torque transfer interfaces, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.\n\n## Exercises and answer criteria\n\n**1. Reconstruct.** Draw the section, mark all inputs and reproduce **75.45 MPa**, including units.\n\n*Answer guidance:* Use `tau_max=16T/(\u03c0d\u00b3)` with correct dimensions. Confirm the sign and the physical meaning of the quantity.\n\n**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.\n\n*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.\n\n**3. Diagnose.** Explain why this error matters: *using area i=\u03c0d\u2074/64 instead of polar j=\u03c0d\u2074/32.* Propose a measurement or alternate equation that exposes it.\n\n*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.\n\n## Transfer to a real engineering study\n\nConfirm whether a constant torque is present over the entire segment or changes at a pulley, gear, or motor connection. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.\n",
          "simulations": []
        },
        {
          "secNumber": "3.2",
          "heading": "Angle of twist and torsional stiffness",
          "content": "# Unit 3, Lesson 2 \u2014 Angle of twist and torsional stiffness\n\n**Learning target.** Connect transmitted torque to shear stress, angle of twist and load transfer through sections and connections. Explain the terms of `\u03b8=32TL/(\u03c0Gd\u2074)`, reconstruct the teaching example and identify one condition where the relation must be modified.\n\n## Physical model\n\nUniform circular-shaft twist is \u03b8=TL/(GJ), with \u03b8 in radians. A shaft with high nominal strength can still rotate too much for positioning accuracy. In a stepped shaft, integrate local torque divided by GJ along the shaft; a section may reverse torque or have a different stiffness. Angular alignment measurements can test the assumption of elastic behavior.\n\nUse the structure of the equation to make an advance prediction. Decide which variables the response is proportional to and which enter as powers, reciprocals or geometric factors. This helps expose a unit error before it becomes an engineering conclusion.\n\n**Context:** A 25 mm solid shaft, L=1 m, G=80 GPa carries 100 N m. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.\n\n## Governing relationship and assumptions\n\n**Teaching relation:** `\u03b8=32TL/(\u03c0Gd\u2074)`.\n\nStiffness and nominal stress often scale differently with diameter: torsional stiffness varies as d to the fourth power while peak solid-shaft torsional stress varies inversely as d cubed. A transition or keyway destroys the smooth uniform geometry. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **angle of twist and torsional stiffness**.\n\nThe model applies over a domain, not to every conceivable physical state. For instance, elastic formulas generally require stresses within an appropriate linear range and strains small enough that deformed geometry does not change the equilibrium appreciably.\n\n## Worked example and interpretation\n\n**Situation:** A 25 mm solid shaft, L=1 m, G=80 GPa carries 100 N m.\n\n**Equation:** `\u03b8=32TL/(\u03c0Gd\u2074)`.\n\n**Reference answer:** **0.03259 rad \u2248 1.867\u00b0**.\n\nReproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.\n\n**Engineering relevance:** Long drive shafts require angular deflection limits separate from stress limits. Real use requires verified component-specific inputs; this example is not a certified working load.\n\n## Diagnosing a false conclusion\n\n**Common error:** Reporting a radian output as degrees without conversion.\n\nLinear elastic predictions cannot be extended beyond yield or into damage without a material law and a method appropriate to those regimes. Temperature and loading rate may change the relevant parameters. For geometry at torque transfer interfaces, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.\n\n## Exercises and answer criteria\n\n**1. Reconstruct.** Draw the section, mark all inputs and reproduce **0.03259 rad \u2248 1.867\u00b0**, including units.\n\n*Answer guidance:* Use `\u03b8=32TL/(\u03c0Gd\u2074)` with correct dimensions. Confirm the sign and the physical meaning of the quantity.\n\n**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.\n\n*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.\n\n**3. Diagnose.** Explain why this error matters: *reporting a radian output as degrees without conversion.* Propose a measurement or alternate equation that exposes it.\n\n*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.\n\n## Transfer to a real engineering study\n\nConfirm whether a constant torque is present over the entire segment or changes at a pulley, gear, or motor connection. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.\n",
          "simulations": []
        },
        {
          "secNumber": "3.3",
          "heading": "Hollow shafts and weight efficiency",
          "content": "# Unit 3, Lesson 3 \u2014 Hollow shafts and weight efficiency\n\n**Learning target.** Connect transmitted torque to shear stress, angle of twist and load transfer through sections and connections. Explain the terms of `tau_max=T(D/2)/[\u03c0(D\u2074\u2212d\u2074)/32]`, reconstruct the teaching example and identify one condition where the relation must be modified.\n\n## Physical model\n\nMoving material away from the axis can raise torsional stiffness relative to mass, but a tube can face local instability or manufacturing limits. For a circular annulus J=\u03c0(D\u2074\u2212d\u2074)/32 and tau_max=T(D/2)/J. The inner diameter must be smaller than the outer diameter and both must use the same length units. Compare designs at equal torque and material strength, not merely equal outer diameter.\n\nAn instructive limiting case is one where the load goes to zero, the span approaches zero, the restraint vanishes or the cross-section grows very large. The response should behave consistently with mechanics. A finite nonzero stress with no load may indicate a missing preload or a mathematical mistake.\n\n**Context:** A tube has outer D=40 mm, inner d=20 mm and torque 500 N m. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.\n\n## Governing relationship and assumptions\n\n**Teaching relation:** `tau_max=T(D/2)/[\u03c0(D\u2074\u2212d\u2074)/32]`.\n\nStiffness and nominal stress often scale differently with diameter: torsional stiffness varies as d to the fourth power while peak solid-shaft torsional stress varies inversely as d cubed. A transition or keyway destroys the smooth uniform geometry. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **hollow shafts and weight efficiency**.\n\nAn independent second approach might use a global equilibrium relation, a limiting case, an energy balance or a laboratory reading. It should not merely repeat the same arithmetic with extra decimal places.\n\n## Worked example and interpretation\n\n**Situation:** A tube has outer D=40 mm, inner d=20 mm and torque 500 N m.\n\n**Equation:** `tau_max=T(D/2)/[\u03c0(D\u2074\u2212d\u2074)/32]`.\n\n**Reference answer:** **42.44 MPa**.\n\nReproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.\n\n**Engineering relevance:** Transmission tubes balance stiffness, mass, fatigue and connection detailing. Real use requires verified component-specific inputs; this example is not a certified working load.\n\n## Diagnosing a false conclusion\n\n**Common error:** Computing J with (D\u2212d)\u2074 instead of D\u2074\u2212d\u2074.\n\nSafety factors do not cure a mistaken model, incorrectly placed support, unnoticed crack or unrealistic input. Start by verifying the load path and the chosen failure mode. For geometry at torque transfer interfaces, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.\n\n## Exercises and answer criteria\n\n**1. Reconstruct.** Draw the section, mark all inputs and reproduce **42.44 MPa**, including units.\n\n*Answer guidance:* Use `tau_max=T(D/2)/[\u03c0(D\u2074\u2212d\u2074)/32]` with correct dimensions. Confirm the sign and the physical meaning of the quantity.\n\n**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.\n\n*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.\n\n**3. Diagnose.** Explain why this error matters: *computing j with (d\u2212d)\u2074 instead of d\u2074\u2212d\u2074.* Propose a measurement or alternate equation that exposes it.\n\n*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.\n\n## Transfer to a real engineering study\n\nConfirm whether a constant torque is present over the entire segment or changes at a pulley, gear, or motor connection. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.\n",
          "simulations": []
        },
        {
          "secNumber": "3.4",
          "heading": "Transverse shear and load transfer",
          "content": "# Unit 3, Lesson 4 \u2014 Transverse shear and load transfer\n\n**Learning target.** Connect transmitted torque to shear stress, angle of twist and load transfer through sections and connections. Explain the terms of `tau_max=1.5V/(bh)`, reconstruct the teaching example and identify one condition where the relation must be modified.\n\n## Physical model\n\nShear stress in a beam cross-section is not generally uniform. In elementary prismatic beams, the distribution follows tau=VQ/(It), where Q is a first moment of an area subset and t the local section width. For a rectangular section, the maximum is 1.5 times the average V/A. Thin-walled joint design also uses shear flow q=VQ/I, expressed as force per unit length.\n\nThe word \u201cstrength\u201d is not interchangeable with \u201cstiffness.\u201d Strength concerns exceeding a material or structural limit; stiffness concerns the load-to-deformation relation. Stability and damage mechanisms introduce further limits, which require their own data and assumptions.\n\n**Context:** Rectangular beam section b=30 mm, h=60 mm under shear force V=9 kN. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.\n\n## Governing relationship and assumptions\n\n**Teaching relation:** `tau_max=1.5V/(bh)`.\n\nStiffness and nominal stress often scale differently with diameter: torsional stiffness varies as d to the fourth power while peak solid-shaft torsional stress varies inversely as d cubed. A transition or keyway destroys the smooth uniform geometry. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **transverse shear and load transfer**.\n\nA true engineering calculation should be independently reproducible from the drawing and a concise input table. Another reader needs to know the sign convention, material assumptions, geometry, force units and exactly which cross-section or point is analyzed.\n\n## Worked example and interpretation\n\n**Situation:** Rectangular beam section b=30 mm, h=60 mm under shear force V=9 kN.\n\n**Equation:** `tau_max=1.5V/(bh)`.\n\n**Reference answer:** **7.5 MPa**.\n\nReproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.\n\n**Engineering relevance:** Adhesive joints may be governed by interface shear flow rather than beam face bending stress. Real use requires verified component-specific inputs; this example is not a certified working load.\n\n## Diagnosing a false conclusion\n\n**Common error:** Applying the rectangular 1.5 factor to an I-section web without derivation.\n\nFailure-mode checks are not independent when the same hidden parameter drives all of them. A poor thickness measurement can bias area, area moment and nominal stress together; correlated uncertainties should be handled explicitly. For geometry at torque transfer interfaces, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.\n\n## Exercises and answer criteria\n\n**1. Reconstruct.** Draw the section, mark all inputs and reproduce **7.5 MPa**, including units.\n\n*Answer guidance:* Use `tau_max=1.5V/(bh)` with correct dimensions. Confirm the sign and the physical meaning of the quantity.\n\n**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.\n\n*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.\n\n**3. Diagnose.** Explain why this error matters: *applying the rectangular 1.5 factor to an i-section web without derivation.* Propose a measurement or alternate equation that exposes it.\n\n*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.\n\n## Transfer to a real engineering study\n\nConfirm whether a constant torque is present over the entire segment or changes at a pulley, gear, or motor connection. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.\n",
          "simulations": []
        },
        {
          "secNumber": "3.5",
          "heading": "Torque transfer through connections",
          "content": "# Unit 3, Lesson 5 \u2014 Torque transfer through connections\n\n**Learning target.** Connect transmitted torque to shear stress, angle of twist and load transfer through sections and connections. Explain the terms of `F=T/r`, reconstruct the teaching example and identify one condition where the relation must be modified.\n\n## Physical model\n\nAn ideal keyed connection transmits tangential force F=T/r at an effective radius. This relation gives a starting load but cannot predict actual contact distribution at key corners. Contact pressure, fretting, bending and dynamic reversals matter. For a chain of shaft segments in series, transmitted torque is established from equilibrium including any gears or external couples.\n\nFor a real joint or machine, the ideal solution is a starting hypothesis. Surface condition, machining tolerances, alignment, residual stress, temperature and spectrum of operating loads can dominate local behavior. Identify a feasible experiment that might falsify the calculation.\n\n**Context:** A coupling transmits 800 N m at effective radius 40 mm. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.\n\n## Governing relationship and assumptions\n\n**Teaching relation:** `F=T/r`.\n\nStiffness and nominal stress often scale differently with diameter: torsional stiffness varies as d to the fourth power while peak solid-shaft torsional stress varies inversely as d cubed. A transition or keyway destroys the smooth uniform geometry. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **torque transfer through connections**.\n\nChecking the dimensions of each term is necessary but not sufficient. An equation may carry the right SI units while using the wrong load boundary, neutral axis, shear area, material condition, or ideal support type.\n\n## Worked example and interpretation\n\n**Situation:** A coupling transmits 800 N m at effective radius 40 mm.\n\n**Equation:** `F=T/r`.\n\n**Reference answer:** **20 kN tangential force**.\n\nReproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.\n\n**Engineering relevance:** A coupling must be checked for contact pressure and shock loading. Real use requires verified component-specific inputs; this example is not a certified working load.\n\n## Diagnosing a false conclusion\n\n**Common error:** Using diameter rather than radius in T=Fr.\n\nDo not turn an average calculation into a guarantee of peak stress at holes, shoulders, welds, contact points or cracks. The stress field can be strongly heterogeneous even if force equilibrium is satisfied. For geometry at torque transfer interfaces, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.\n\n## Exercises and answer criteria\n\n**1. Reconstruct.** Draw the section, mark all inputs and reproduce **20 kN tangential force**, including units.\n\n*Answer guidance:* Use `F=T/r` with correct dimensions. Confirm the sign and the physical meaning of the quantity.\n\n**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.\n\n*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.\n\n**3. Diagnose.** Explain why this error matters: *using diameter rather than radius in t=fr.* Propose a measurement or alternate equation that exposes it.\n\n*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.\n\n## Transfer to a real engineering study\n\nConfirm whether a constant torque is present over the entire segment or changes at a pulley, gear, or motor connection. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.\n",
          "simulations": []
        }
      ],
      "problems": [
        {
          "id": "MOS-U3-P1",
          "title": "Shear stress in solid circular shafts",
          "question": "**Situation:** A solid round shaft of diameter 30 mm carries torque 400 N m.",
          "steps": [
            {
              "explanation": "**Equation:** `tau_max=16T/(\u03c0d\u00b3)`."
            },
            {
              "explanation": "**Reference answer:** **75.45 MPa**."
            },
            {
              "explanation": "Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path."
            },
            {
              "explanation": "**Engineering relevance:** A motor shaft must transmit peak transient torque, not only nominal steady torque. Real use requires verified component-specific inputs; this example is not a certified working load."
            }
          ],
          "finalAnswer": "**Engineering relevance:** A motor shaft must transmit peak transient torque, not only nominal steady torque. Real use requires verified component-specific inputs; this example is not a certified working load."
        },
        {
          "id": "MOS-U3-P2",
          "title": "Angle of twist and torsional stiffness",
          "question": "**Situation:** A 25 mm solid shaft, L=1 m, G=80 GPa carries 100 N m.",
          "steps": [
            {
              "explanation": "**Equation:** `\u03b8=32TL/(\u03c0Gd\u2074)`."
            },
            {
              "explanation": "**Reference answer:** **0.03259 rad \u2248 1.867\u00b0**."
            },
            {
              "explanation": "Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path."
            },
            {
              "explanation": "**Engineering relevance:** Long drive shafts require angular deflection limits separate from stress limits. Real use requires verified component-specific inputs; this example is not a certified working load."
            }
          ],
          "finalAnswer": "**Engineering relevance:** Long drive shafts require angular deflection limits separate from stress limits. Real use requires verified component-specific inputs; this example is not a certified working load."
        },
        {
          "id": "MOS-U3-P3",
          "title": "Hollow shafts and weight efficiency",
          "question": "**Situation:** A tube has outer D=40 mm, inner d=20 mm and torque 500 N m.",
          "steps": [
            {
              "explanation": "**Equation:** `tau_max=T(D/2)/[\u03c0(D\u2074\u2212d\u2074)/32]`."
            },
            {
              "explanation": "**Reference answer:** **42.44 MPa**."
            },
            {
              "explanation": "Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path."
            },
            {
              "explanation": "**Engineering relevance:** Transmission tubes balance stiffness, mass, fatigue and connection detailing. Real use requires verified component-specific inputs; this example is not a certified working load."
            }
          ],
          "finalAnswer": "**Engineering relevance:** Transmission tubes balance stiffness, mass, fatigue and connection detailing. Real use requires verified component-specific inputs; this example is not a certified working load."
        },
        {
          "id": "MOS-U3-P4",
          "title": "Transverse shear and load transfer",
          "question": "**Situation:** Rectangular beam section b=30 mm, h=60 mm under shear force V=9 kN.",
          "steps": [
            {
              "explanation": "**Equation:** `tau_max=1.5V/(bh)`."
            },
            {
              "explanation": "**Reference answer:** **7.5 MPa**."
            },
            {
              "explanation": "Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path."
            },
            {
              "explanation": "**Engineering relevance:** Adhesive joints may be governed by interface shear flow rather than beam face bending stress. Real use requires verified component-specific inputs; this example is not a certified working load."
            }
          ],
          "finalAnswer": "**Engineering relevance:** Adhesive joints may be governed by interface shear flow rather than beam face bending stress. Real use requires verified component-specific inputs; this example is not a certified working load."
        },
        {
          "id": "MOS-U3-P5",
          "title": "Torque transfer through connections",
          "question": "**Situation:** A coupling transmits 800 N m at effective radius 40 mm.",
          "steps": [
            {
              "explanation": "**Equation:** `F=T/r`."
            },
            {
              "explanation": "**Reference answer:** **20 kN tangential force**."
            },
            {
              "explanation": "Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path."
            },
            {
              "explanation": "**Engineering relevance:** A coupling must be checked for contact pressure and shock loading. Real use requires verified component-specific inputs; this example is not a certified working load."
            }
          ],
          "finalAnswer": "**Engineering relevance:** A coupling must be checked for contact pressure and shock loading. Real use requires verified component-specific inputs; this example is not a certified working load."
        }
      ],
      "simulations": [
        "mechanics-of-solids-sim-3"
      ]
    },
    {
      "id": "mechanics-of-solids-unit-4",
      "number": 4,
      "title": "Beam Stress and Internal Resultants",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Beam Stress and Internal Resultants.",
      "sections": [
        {
          "secNumber": "4.1",
          "heading": "force and moment diagrams",
          "content": "# Unit 4, Lesson 1 \u2014 Shear-force and moment diagrams\n\n**Learning target.** Derive shear-force and bending-moment distributions and convert beam resultants to elastic cross-sectional stresses. Explain the terms of `M_max=PL/4`, reconstruct the teaching example and identify one condition where the relation must be modified.\n\n## Physical model\n\nFor a beam with distributed transverse loading, internal shear and moment are related to load and position through differential equilibrium: dV/dx=\u2212w and dM/dx=V under a consistent sign convention. Concentrated forces jump the shear diagram; applied couples jump the moment diagram. An extremum in M often occurs where V crosses zero. The diagrams must satisfy total load and support reaction balance.\n\nThe essential step is to identify what has been idealized. Stress is not directly interchangeable with force; strain is not identical to movement of a distant fixture; and a computed failure index is not an observed failure. Mark the difference between what you assumed, calculated and measured in your notebook.\n\n**Context:** A 4 m simply supported beam carries a centered 10 kN point load. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.\n\n## Governing relationship and assumptions\n\n**Teaching relation:** `M_max=PL/4`.\n\nA force diagram describes a resultant on a section, not the actual stress field at a support, weld toe, hole or abrupt step. Standard beam expressions are valid only for their associated idealizations and away from singular load introduction. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **shear-force and moment diagrams**.\n\nIf the part has a geometric discontinuity, peak local stress may lie far above a cross-sectional average. Document where each area and section property is defined and whether a stress concentration factor is relevant.\n\n## Worked example and interpretation\n\n**Situation:** A 4 m simply supported beam carries a centered 10 kN point load.\n\n**Equation:** `M_max=PL/4`.\n\n**Reference answer:** **10 kN m**.\n\nReproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.\n\n**Engineering relevance:** Bending stress checks start with the actual critical moment section. Real use requires verified component-specific inputs; this example is not a certified working load.\n\n## Diagnosing a false conclusion\n\n**Common error:** Drawing a triangular shear diagram for a beam with only a point load.\n\nA negative quantity is not by itself a failure: under a defined sign convention, negative axial stress may represent compression and negative strain may represent contraction. What matters is whether the assumed physical constraint can transmit that action. For load-to-stress conversion, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.\n\n## Exercises and answer criteria\n\n**1. Reconstruct.** Draw the section, mark all inputs and reproduce **10 kN m**, including units.\n\n*Answer guidance:* Use `M_max=PL/4` with correct dimensions. Confirm the sign and the physical meaning of the quantity.\n\n**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.\n\n*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.\n\n**3. Diagnose.** Explain why this error matters: *drawing a triangular shear diagram for a beam with only a point load.* Propose a measurement or alternate equation that exposes it.\n\n*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.\n\n## Transfer to a real engineering study\n\nCompare independent moments about two points and verify both section symmetry and material homogeneity. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.\n",
          "simulations": []
        },
        {
          "secNumber": "4.2",
          "heading": "Elastic bending stress",
          "content": "# Unit 4, Lesson 2 \u2014 Elastic bending stress\n\n**Learning target.** Derive shear-force and bending-moment distributions and convert beam resultants to elastic cross-sectional stresses. Explain the terms of `sigma_max=6M/(bh\u00b2)`, reconstruct the teaching example and identify one condition where the relation must be modified.\n\n## Physical model\n\nFor homogeneous linear elastic symmetric beams in pure bending, |sigma|=|M|c/I. The rectangular-section maximum reduces to 6M/(bh\u00b2). This result neglects significant shear deformation, inelasticity and local stress concentrations. Orientation matters because bending stiffness depends on depth cubed. A beam section may yield or buckle locally before an elementary formula remains reliable.\n\nUse the structure of the equation to make an advance prediction. Decide which variables the response is proportional to and which enter as powers, reciprocals or geometric factors. This helps expose a unit error before it becomes an engineering conclusion.\n\n**Context:** A 40 mm by 80 mm rectangle resists bending moment 2 kN m about its strong axis. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.\n\n## Governing relationship and assumptions\n\n**Teaching relation:** `sigma_max=6M/(bh\u00b2)`.\n\nA force diagram describes a resultant on a section, not the actual stress field at a support, weld toe, hole or abrupt step. Standard beam expressions are valid only for their associated idealizations and away from singular load introduction. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **elastic bending stress**.\n\nThe model applies over a domain, not to every conceivable physical state. For instance, elastic formulas generally require stresses within an appropriate linear range and strains small enough that deformed geometry does not change the equilibrium appreciably.\n\n## Worked example and interpretation\n\n**Situation:** A 40 mm by 80 mm rectangle resists bending moment 2 kN m about its strong axis.\n\n**Equation:** `sigma_max=6M/(bh\u00b2)`.\n\n**Reference answer:** **46.875 MPa**.\n\nReproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.\n\n**Engineering relevance:** Section orientation frequently controls both strength and deflection. Real use requires verified component-specific inputs; this example is not a certified working load.\n\n## Diagnosing a false conclusion\n\n**Common error:** Substituting width for depth in the squared denominator.\n\nLinear elastic predictions cannot be extended beyond yield or into damage without a material law and a method appropriate to those regimes. Temperature and loading rate may change the relevant parameters. For load-to-stress conversion, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.\n\n## Exercises and answer criteria\n\n**1. Reconstruct.** Draw the section, mark all inputs and reproduce **46.875 MPa**, including units.\n\n*Answer guidance:* Use `sigma_max=6M/(bh\u00b2)` with correct dimensions. Confirm the sign and the physical meaning of the quantity.\n\n**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.\n\n*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.\n\n**3. Diagnose.** Explain why this error matters: *substituting width for depth in the squared denominator.* Propose a measurement or alternate equation that exposes it.\n\n*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.\n\n## Transfer to a real engineering study\n\nCompare independent moments about two points and verify both section symmetry and material homogeneity. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.\n",
          "simulations": []
        },
        {
          "secNumber": "4.3",
          "heading": "Neutral axis and transformed sections",
          "content": "# Unit 4, Lesson 3 \u2014 Neutral axis and transformed sections\n\n**Learning target.** Derive shear-force and bending-moment distributions and convert beam resultants to elastic cross-sectional stresses. Explain the terms of `|sigma|=E kappa |y|`, reconstruct the teaching example and identify one condition where the relation must be modified.\n\n## Physical model\n\nIn a homogeneous elastic beam under pure bending, the neutral axis passes through the centroid. A composite beam of bonded materials can be handled by a transformed-section approach if strain compatibility and linear elasticity hold. Modulus ratios weight transformed areas; the neutral axis need not coincide with geometric centroid. Connector slip undermines composite action.\n\nAn instructive limiting case is one where the load goes to zero, the span approaches zero, the restraint vanishes or the cross-section grows very large. The response should behave consistently with mechanics. A finite nonzero stress with no load may indicate a missing preload or a mathematical mistake.\n\n**Context:** Two bonded layers experience common curvature kappa=0.001 1/m; a fiber lies 20 mm from the neutral axis, E=70 GPa. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.\n\n## Governing relationship and assumptions\n\n**Teaching relation:** `|sigma|=E kappa |y|`.\n\nA force diagram describes a resultant on a section, not the actual stress field at a support, weld toe, hole or abrupt step. Standard beam expressions are valid only for their associated idealizations and away from singular load introduction. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **neutral axis and transformed sections**.\n\nAn independent second approach might use a global equilibrium relation, a limiting case, an energy balance or a laboratory reading. It should not merely repeat the same arithmetic with extra decimal places.\n\n## Worked example and interpretation\n\n**Situation:** Two bonded layers experience common curvature kappa=0.001 1/m; a fiber lies 20 mm from the neutral axis, E=70 GPa.\n\n**Equation:** `|sigma|=E kappa |y|`.\n\n**Reference answer:** **1.4 MPa at the fiber**.\n\nReproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.\n\n**Engineering relevance:** Layer bonding and interface shear deserve explicit validation. Real use requires verified component-specific inputs; this example is not a certified working load.\n\n## Diagnosing a false conclusion\n\n**Common error:** Assuming the neutral axis of dissimilar bonded materials is always at geometric mid-depth.\n\nSafety factors do not cure a mistaken model, incorrectly placed support, unnoticed crack or unrealistic input. Start by verifying the load path and the chosen failure mode. For load-to-stress conversion, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.\n\n## Exercises and answer criteria\n\n**1. Reconstruct.** Draw the section, mark all inputs and reproduce **1.4 MPa at the fiber**, including units.\n\n*Answer guidance:* Use `|sigma|=E kappa |y|` with correct dimensions. Confirm the sign and the physical meaning of the quantity.\n\n**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.\n\n*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.\n\n**3. Diagnose.** Explain why this error matters: *assuming the neutral axis of dissimilar bonded materials is always at geometric mid-depth.* Propose a measurement or alternate equation that exposes it.\n\n*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.\n\n## Transfer to a real engineering study\n\nCompare independent moments about two points and verify both section symmetry and material homogeneity. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.\n",
          "simulations": []
        },
        {
          "secNumber": "4.4",
          "heading": "Area second moments and beam geometry",
          "content": "# Unit 4, Lesson 4 \u2014 Area second moments and beam geometry\n\n**Learning target.** Derive shear-force and bending-moment distributions and convert beam resultants to elastic cross-sectional stresses. Explain the terms of `I=bh\u00b3/12`, reconstruct the teaching example and identify one condition where the relation must be modified.\n\n## Physical model\n\nThe centroidal I of a solid rectangular area for bending about its horizontal axis is bh\u00b3/12. I is a geometry quantity, not a material property; EI is a bending rigidity. When parts are moved away from the neutral axis, the parallel-axis term Ad\u00b2 increases I. Cutouts subtract their own area moments and shifted contributions. CAD-generated values should still be unit checked.\n\nThe word \u201cstrength\u201d is not interchangeable with \u201cstiffness.\u201d Strength concerns exceeding a material or structural limit; stiffness concerns the load-to-deformation relation. Stability and damage mechanisms introduce further limits, which require their own data and assumptions.\n\n**Context:** A rectangular section has b=50 mm and h=100 mm. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.\n\n## Governing relationship and assumptions\n\n**Teaching relation:** `I=bh\u00b3/12`.\n\nA force diagram describes a resultant on a section, not the actual stress field at a support, weld toe, hole or abrupt step. Standard beam expressions are valid only for their associated idealizations and away from singular load introduction. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **area second moments and beam geometry**.\n\nA true engineering calculation should be independently reproducible from the drawing and a concise input table. Another reader needs to know the sign convention, material assumptions, geometry, force units and exactly which cross-section or point is analyzed.\n\n## Worked example and interpretation\n\n**Situation:** A rectangular section has b=50 mm and h=100 mm.\n\n**Equation:** `I=bh\u00b3/12`.\n\n**Reference answer:** **4.1667e6 mm\u2074**.\n\nReproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.\n\n**Engineering relevance:** An optimized cross-section places material where its bending contribution is greatest. Real use requires verified component-specific inputs; this example is not a certified working load.\n\n## Diagnosing a false conclusion\n\n**Common error:** Entering an area in mm\u00b2 where an I in mm\u2074 is required.\n\nFailure-mode checks are not independent when the same hidden parameter drives all of them. A poor thickness measurement can bias area, area moment and nominal stress together; correlated uncertainties should be handled explicitly. For load-to-stress conversion, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.\n\n## Exercises and answer criteria\n\n**1. Reconstruct.** Draw the section, mark all inputs and reproduce **4.1667e6 mm\u2074**, including units.\n\n*Answer guidance:* Use `I=bh\u00b3/12` with correct dimensions. Confirm the sign and the physical meaning of the quantity.\n\n**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.\n\n*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.\n\n**3. Diagnose.** Explain why this error matters: *entering an area in mm\u00b2 where an i in mm\u2074 is required.* Propose a measurement or alternate equation that exposes it.\n\n*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.\n\n## Transfer to a real engineering study\n\nCompare independent moments about two points and verify both section symmetry and material homogeneity. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.\n",
          "simulations": []
        },
        {
          "secNumber": "4.5",
          "heading": "Beam shear and interface forces",
          "content": "# Unit 4, Lesson 5 \u2014 Beam shear and interface forces\n\n**Learning target.** Derive shear-force and bending-moment distributions and convert beam resultants to elastic cross-sectional stresses. Explain the terms of `q=VQ/I`, reconstruct the teaching example and identify one condition where the relation must be modified.\n\n## Physical model\n\nUnder transverse loading, beam shear stress changes across the depth; thin web geometry often carries most of the vertical shear. Shear flow q=VQ/I can estimate the longitudinal force per unit length that connectors must transfer between built-up components. Fastener spacing follows from allowable fastener shear per pitch only with a defensible joint model. A local concentrated load may cause web crippling outside simple beam theory.\n\nFor a real joint or machine, the ideal solution is a starting hypothesis. Surface condition, machining tolerances, alignment, residual stress, temperature and spectrum of operating loads can dominate local behavior. Identify a feasible experiment that might falsify the calculation.\n\n**Context:** An interface has V=12 kN, Q=2e4 mm\u00b3 and I=8e6 mm\u2074. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.\n\n## Governing relationship and assumptions\n\n**Teaching relation:** `q=VQ/I`.\n\nA force diagram describes a resultant on a section, not the actual stress field at a support, weld toe, hole or abrupt step. Standard beam expressions are valid only for their associated idealizations and away from singular load introduction. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **beam shear and interface forces**.\n\nChecking the dimensions of each term is necessary but not sufficient. An equation may carry the right SI units while using the wrong load boundary, neutral axis, shear area, material condition, or ideal support type.\n\n## Worked example and interpretation\n\n**Situation:** An interface has V=12 kN, Q=2e4 mm\u00b3 and I=8e6 mm\u2074.\n\n**Equation:** `q=VQ/I`.\n\n**Reference answer:** **30 N/mm shear flow**.\n\nReproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.\n\n**Engineering relevance:** A row of connectors must pass the interface force while limiting slip. Real use requires verified component-specific inputs; this example is not a certified working load.\n\n## Diagnosing a false conclusion\n\n**Common error:** Confusing shear flow N/mm with shear stress N/mm\u00b2.\n\nDo not turn an average calculation into a guarantee of peak stress at holes, shoulders, welds, contact points or cracks. The stress field can be strongly heterogeneous even if force equilibrium is satisfied. For load-to-stress conversion, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.\n\n## Exercises and answer criteria\n\n**1. Reconstruct.** Draw the section, mark all inputs and reproduce **30 N/mm shear flow**, including units.\n\n*Answer guidance:* Use `q=VQ/I` with correct dimensions. Confirm the sign and the physical meaning of the quantity.\n\n**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.\n\n*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.\n\n**3. Diagnose.** Explain why this error matters: *confusing shear flow n/mm with shear stress n/mm\u00b2.* Propose a measurement or alternate equation that exposes it.\n\n*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.\n\n## Transfer to a real engineering study\n\nCompare independent moments about two points and verify both section symmetry and material homogeneity. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.\n",
          "simulations": []
        }
      ],
      "problems": [
        {
          "id": "MOS-U4-P1",
          "title": "force and moment diagrams",
          "question": "**Situation:** A 4 m simply supported beam carries a centered 10 kN point load.",
          "steps": [
            {
              "explanation": "**Equation:** `M_max=PL/4`."
            },
            {
              "explanation": "**Reference answer:** **10 kN m**."
            },
            {
              "explanation": "Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path."
            },
            {
              "explanation": "**Engineering relevance:** Bending stress checks start with the actual critical moment section. Real use requires verified component-specific inputs; this example is not a certified working load."
            }
          ],
          "finalAnswer": "**Engineering relevance:** Bending stress checks start with the actual critical moment section. Real use requires verified component-specific inputs; this example is not a certified working load."
        },
        {
          "id": "MOS-U4-P2",
          "title": "Elastic bending stress",
          "question": "**Situation:** A 40 mm by 80 mm rectangle resists bending moment 2 kN m about its strong axis.",
          "steps": [
            {
              "explanation": "**Equation:** `sigma_max=6M/(bh\u00b2)`."
            },
            {
              "explanation": "**Reference answer:** **46.875 MPa**."
            },
            {
              "explanation": "Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path."
            },
            {
              "explanation": "**Engineering relevance:** Section orientation frequently controls both strength and deflection. Real use requires verified component-specific inputs; this example is not a certified working load."
            }
          ],
          "finalAnswer": "**Engineering relevance:** Section orientation frequently controls both strength and deflection. Real use requires verified component-specific inputs; this example is not a certified working load."
        },
        {
          "id": "MOS-U4-P3",
          "title": "Neutral axis and transformed sections",
          "question": "**Situation:** Two bonded layers experience common curvature kappa=0.001 1/m; a fiber lies 20 mm from the neutral axis, E=70 GPa.",
          "steps": [
            {
              "explanation": "**Equation:** `|sigma|=E kappa |y|`."
            },
            {
              "explanation": "**Reference answer:** **1.4 MPa at the fiber**."
            },
            {
              "explanation": "Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path."
            },
            {
              "explanation": "**Engineering relevance:** Layer bonding and interface shear deserve explicit validation. Real use requires verified component-specific inputs; this example is not a certified working load."
            }
          ],
          "finalAnswer": "**Engineering relevance:** Layer bonding and interface shear deserve explicit validation. Real use requires verified component-specific inputs; this example is not a certified working load."
        },
        {
          "id": "MOS-U4-P4",
          "title": "Area second moments and beam geometry",
          "question": "**Situation:** A rectangular section has b=50 mm and h=100 mm.",
          "steps": [
            {
              "explanation": "**Equation:** `I=bh\u00b3/12`."
            },
            {
              "explanation": "**Reference answer:** **4.1667e6 mm\u2074**."
            },
            {
              "explanation": "Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path."
            },
            {
              "explanation": "**Engineering relevance:** An optimized cross-section places material where its bending contribution is greatest. Real use requires verified component-specific inputs; this example is not a certified working load."
            }
          ],
          "finalAnswer": "**Engineering relevance:** An optimized cross-section places material where its bending contribution is greatest. Real use requires verified component-specific inputs; this example is not a certified working load."
        },
        {
          "id": "MOS-U4-P5",
          "title": "Beam shear and interface forces",
          "question": "**Situation:** An interface has V=12 kN, Q=2e4 mm\u00b3 and I=8e6 mm\u2074.",
          "steps": [
            {
              "explanation": "**Equation:** `q=VQ/I`."
            },
            {
              "explanation": "**Reference answer:** **30 N/mm shear flow**."
            },
            {
              "explanation": "Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path."
            },
            {
              "explanation": "**Engineering relevance:** A row of connectors must pass the interface force while limiting slip. Real use requires verified component-specific inputs; this example is not a certified working load."
            }
          ],
          "finalAnswer": "**Engineering relevance:** A row of connectors must pass the interface force while limiting slip. Real use requires verified component-specific inputs; this example is not a certified working load."
        }
      ],
      "simulations": [
        "mechanics-of-solids-sim-4"
      ]
    },
    {
      "id": "mechanics-of-solids-unit-5",
      "number": 5,
      "title": "Beam Deflection and Energy Methods",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Beam Deflection and Energy Methods.",
      "sections": [
        {
          "secNumber": "5.1",
          "heading": "Moment\u2013curvature relation",
          "content": "# Unit 5, Lesson 1 \u2014 Moment\u2013curvature relation\n\n**Learning target.** Predict elastic slopes, deflections and strain energy, including compatibility constraints and load displacement relationships. Explain the terms of `kappa=M/(EI)`, reconstruct the teaching example and identify one condition where the relation must be modified.\n\n## Physical model\n\nEuler\u2013Bernoulli beam theory assumes sections remain plane and normal to a deformed centerline, producing curvature \u03ba=M/(EI) for small slopes. A curvature result cannot be integrated without boundary conditions. In thick short beams, transverse shear deformation can be non-negligible; a Timoshenko model may be better. Deflection and rotation sign conventions should be stated before integration.\n\nThe essential step is to identify what has been idealized. Stress is not directly interchangeable with force; strain is not identical to movement of a distant fixture; and a computed failure index is not an observed failure. Mark the difference between what you assumed, calculated and measured in your notebook.\n\n**Context:** Uniform E=200 GPa, I=500 cm\u2074 and bending moment 2 kN m. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.\n\n## Governing relationship and assumptions\n\n**Teaching relation:** `kappa=M/(EI)`.\n\nChanging boundary constraints can alter a deformation coefficient by a large factor even when E, I and loading remain unchanged. Superposition cannot be used indiscriminately with changing contacts or plastic hinges. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **moment\u2013curvature relation**.\n\nIf the part has a geometric discontinuity, peak local stress may lie far above a cross-sectional average. Document where each area and section property is defined and whether a stress concentration factor is relevant.\n\n## Worked example and interpretation\n\n**Situation:** Uniform E=200 GPa, I=500 cm\u2074 and bending moment 2 kN m.\n\n**Equation:** `kappa=M/(EI)`.\n\n**Reference answer:** **0.002 1/m**.\n\nReproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.\n\n**Engineering relevance:** Curvature is the local change in beam slope per length. Real use requires verified component-specific inputs; this example is not a certified working load.\n\n## Diagnosing a false conclusion\n\n**Common error:** Using I in cm\u2074 as if it were m\u2074.\n\nA negative quantity is not by itself a failure: under a defined sign convention, negative axial stress may represent compression and negative strain may represent contraction. What matters is whether the assumed physical constraint can transmit that action. For boundary-condition dependency, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.\n\n## Exercises and answer criteria\n\n**1. Reconstruct.** Draw the section, mark all inputs and reproduce **0.002 1/m**, including units.\n\n*Answer guidance:* Use `kappa=M/(EI)` with correct dimensions. Confirm the sign and the physical meaning of the quantity.\n\n**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.\n\n*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.\n\n**3. Diagnose.** Explain why this error matters: *using i in cm\u2074 as if it were m\u2074.* Propose a measurement or alternate equation that exposes it.\n\n*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.\n\n## Transfer to a real engineering study\n\nWrite all deflection and slope boundary conditions beside the governing differential equation. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.\n",
          "simulations": []
        },
        {
          "secNumber": "5.2",
          "heading": "Simply supported beam deflection",
          "content": "# Unit 5, Lesson 2 \u2014 Simply supported beam deflection\n\n**Learning target.** Predict elastic slopes, deflections and strain energy, including compatibility constraints and load displacement relationships. Explain the terms of `delta=PL\u00b3/(48EI)`, reconstruct the teaching example and identify one condition where the relation must be modified.\n\n## Physical model\n\nFor a simply supported prismatic beam with a midspan point load and constant EI, the central elastic deflection has magnitude PL\u00b3/(48EI). Its cubic span dependence is a major design sensitivity. Changing the support to a fixed end invalidates the coefficient 48 even if the load and section are unchanged. Account for self-weight separately when it is not negligible.\n\nUse the structure of the equation to make an advance prediction. Decide which variables the response is proportional to and which enter as powers, reciprocals or geometric factors. This helps expose a unit error before it becomes an engineering conclusion.\n\n**Context:** P=8 kN at midspan, L=3 m, E=200 GPa, I=800 cm\u2074. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.\n\n## Governing relationship and assumptions\n\n**Teaching relation:** `delta=PL\u00b3/(48EI)`.\n\nChanging boundary constraints can alter a deformation coefficient by a large factor even when E, I and loading remain unchanged. Superposition cannot be used indiscriminately with changing contacts or plastic hinges. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **simply supported beam deflection**.\n\nThe model applies over a domain, not to every conceivable physical state. For instance, elastic formulas generally require stresses within an appropriate linear range and strains small enough that deformed geometry does not change the equilibrium appreciably.\n\n## Worked example and interpretation\n\n**Situation:** P=8 kN at midspan, L=3 m, E=200 GPa, I=800 cm\u2074.\n\n**Equation:** `delta=PL\u00b3/(48EI)`.\n\n**Reference answer:** **2.8125 mm**.\n\nReproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.\n\n**Engineering relevance:** Long-span design may be governed by deflection before yielding. Real use requires verified component-specific inputs; this example is not a certified working load.\n\n## Diagnosing a false conclusion\n\n**Common error:** Keeping the simply supported coefficient after changing the support type.\n\nLinear elastic predictions cannot be extended beyond yield or into damage without a material law and a method appropriate to those regimes. Temperature and loading rate may change the relevant parameters. For boundary-condition dependency, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.\n\n## Exercises and answer criteria\n\n**1. Reconstruct.** Draw the section, mark all inputs and reproduce **2.8125 mm**, including units.\n\n*Answer guidance:* Use `delta=PL\u00b3/(48EI)` with correct dimensions. Confirm the sign and the physical meaning of the quantity.\n\n**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.\n\n*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.\n\n**3. Diagnose.** Explain why this error matters: *keeping the simply supported coefficient after changing the support type.* Propose a measurement or alternate equation that exposes it.\n\n*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.\n\n## Transfer to a real engineering study\n\nWrite all deflection and slope boundary conditions beside the governing differential equation. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.\n",
          "simulations": []
        },
        {
          "secNumber": "5.3",
          "heading": "Cantilever tip displacement",
          "content": "# Unit 5, Lesson 3 \u2014 Cantilever tip displacement\n\n**Learning target.** Predict elastic slopes, deflections and strain energy, including compatibility constraints and load displacement relationships. Explain the terms of `delta_tip=PL\u00b3/(3EI)`, reconstruct the teaching example and identify one condition where the relation must be modified.\n\n## Physical model\n\nA cantilever with a free-end transverse point load deflects at its tip by PL\u00b3/(3EI) and rotates by PL\u00b2/(2EI) under linear small-deflection theory. The sign reflects load direction, and a rigid support is idealized. Compare deflection prediction to measured motion without including fixture settlement in the same number. For large rotations, geometric nonlinear analysis is required.\n\nAn instructive limiting case is one where the load goes to zero, the span approaches zero, the restraint vanishes or the cross-section grows very large. The response should behave consistently with mechanics. A finite nonzero stress with no load may indicate a missing preload or a mathematical mistake.\n\n**Context:** A cantilever has P=500 N, L=1 m, E=200 GPa, I=400 cm\u2074. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.\n\n## Governing relationship and assumptions\n\n**Teaching relation:** `delta_tip=PL\u00b3/(3EI)`.\n\nChanging boundary constraints can alter a deformation coefficient by a large factor even when E, I and loading remain unchanged. Superposition cannot be used indiscriminately with changing contacts or plastic hinges. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **cantilever tip displacement**.\n\nAn independent second approach might use a global equilibrium relation, a limiting case, an energy balance or a laboratory reading. It should not merely repeat the same arithmetic with extra decimal places.\n\n## Worked example and interpretation\n\n**Situation:** A cantilever has P=500 N, L=1 m, E=200 GPa, I=400 cm\u2074.\n\n**Equation:** `delta_tip=PL\u00b3/(3EI)`.\n\n**Reference answer:** **0.20833 mm**.\n\nReproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.\n\n**Engineering relevance:** A flexible cantilever mechanism can meet strength limits but miss positional tolerances. Real use requires verified component-specific inputs; this example is not a certified working load.\n\n## Diagnosing a false conclusion\n\n**Common error:** Using simply supported beam formulas for a cantilever.\n\nSafety factors do not cure a mistaken model, incorrectly placed support, unnoticed crack or unrealistic input. Start by verifying the load path and the chosen failure mode. For boundary-condition dependency, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.\n\n## Exercises and answer criteria\n\n**1. Reconstruct.** Draw the section, mark all inputs and reproduce **0.20833 mm**, including units.\n\n*Answer guidance:* Use `delta_tip=PL\u00b3/(3EI)` with correct dimensions. Confirm the sign and the physical meaning of the quantity.\n\n**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.\n\n*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.\n\n**3. Diagnose.** Explain why this error matters: *using simply supported beam formulas for a cantilever.* Propose a measurement or alternate equation that exposes it.\n\n*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.\n\n## Transfer to a real engineering study\n\nWrite all deflection and slope boundary conditions beside the governing differential equation. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.\n",
          "simulations": []
        },
        {
          "secNumber": "5.4",
          "heading": "Strain energy and Castigliano",
          "content": "# Unit 5, Lesson 4 \u2014 Strain energy and Castigliano\n\n**Learning target.** Predict elastic slopes, deflections and strain energy, including compatibility constraints and load displacement relationships. Explain the terms of `U=0.5Pdelta`, reconstruct the teaching example and identify one condition where the relation must be modified.\n\n## Physical model\n\nElastic axial energy U=P\u00b2L/(2EA) follows from integrating P d\u03b4 in a linear system. Castigliano\u2019s displacement theorem differentiates total elastic strain energy with respect to a corresponding force for a linear elastic structure, under its conditions of use. The method is particularly useful when several members deform together. A single term is insufficient if bending, shear or torsion also contributes significantly.\n\nThe word \u201cstrength\u201d is not interchangeable with \u201cstiffness.\u201d Strength concerns exceeding a material or structural limit; stiffness concerns the load-to-deformation relation. Stability and damage mechanisms introduce further limits, which require their own data and assumptions.\n\n**Context:** Bar with axial load 12 kN and extension 0.3 mm in a linear test. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.\n\n## Governing relationship and assumptions\n\n**Teaching relation:** `U=0.5Pdelta`.\n\nChanging boundary constraints can alter a deformation coefficient by a large factor even when E, I and loading remain unchanged. Superposition cannot be used indiscriminately with changing contacts or plastic hinges. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **strain energy and castigliano**.\n\nA true engineering calculation should be independently reproducible from the drawing and a concise input table. Another reader needs to know the sign convention, material assumptions, geometry, force units and exactly which cross-section or point is analyzed.\n\n## Worked example and interpretation\n\n**Situation:** Bar with axial load 12 kN and extension 0.3 mm in a linear test.\n\n**Equation:** `U=0.5Pdelta`.\n\n**Reference answer:** **1.8 J**.\n\nReproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.\n\n**Engineering relevance:** Energy methods provide independent displacement checks and stiffness estimates. Real use requires verified component-specific inputs; this example is not a certified working load.\n\n## Diagnosing a false conclusion\n\n**Common error:** Omitting the factor one-half for a load increased quasistatically from zero.\n\nFailure-mode checks are not independent when the same hidden parameter drives all of them. A poor thickness measurement can bias area, area moment and nominal stress together; correlated uncertainties should be handled explicitly. For boundary-condition dependency, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.\n\n## Exercises and answer criteria\n\n**1. Reconstruct.** Draw the section, mark all inputs and reproduce **1.8 J**, including units.\n\n*Answer guidance:* Use `U=0.5Pdelta` with correct dimensions. Confirm the sign and the physical meaning of the quantity.\n\n**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.\n\n*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.\n\n**3. Diagnose.** Explain why this error matters: *omitting the factor one-half for a load increased quasistatically from zero.* Propose a measurement or alternate equation that exposes it.\n\n*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.\n\n## Transfer to a real engineering study\n\nWrite all deflection and slope boundary conditions beside the governing differential equation. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.\n",
          "simulations": []
        },
        {
          "secNumber": "5.5",
          "heading": "Redundant supports and superposition",
          "content": "# Unit 5, Lesson 5 \u2014 Redundant supports and superposition\n\n**Learning target.** Predict elastic slopes, deflections and strain energy, including compatibility constraints and load displacement relationships. Explain the terms of `F=k delta`, reconstruct the teaching example and identify one condition where the relation must be modified.\n\n## Physical model\n\nA statically indeterminate beam or bar requires compatibility as well as equilibrium. One approach removes a redundant restraint, computes displacements from separate loads, and selects the redundant so the required displacement is recovered. Linear superposition fails after yielding, contact change or nonlinear large motion. A zero displacement at a support is a boundary condition, not an arbitrary convenience.\n\nFor a real joint or machine, the ideal solution is a starting hypothesis. Surface condition, machining tolerances, alignment, residual stress, temperature and spectrum of operating loads can dominate local behavior. Identify a feasible experiment that might falsify the calculation.\n\n**Context:** A linear axial spring of stiffness 60 kN/mm is restrained to stretch 0.25 mm. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.\n\n## Governing relationship and assumptions\n\n**Teaching relation:** `F=k delta`.\n\nChanging boundary constraints can alter a deformation coefficient by a large factor even when E, I and loading remain unchanged. Superposition cannot be used indiscriminately with changing contacts or plastic hinges. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **redundant supports and superposition**.\n\nChecking the dimensions of each term is necessary but not sufficient. An equation may carry the right SI units while using the wrong load boundary, neutral axis, shear area, material condition, or ideal support type.\n\n## Worked example and interpretation\n\n**Situation:** A linear axial spring of stiffness 60 kN/mm is restrained to stretch 0.25 mm.\n\n**Equation:** `F=k delta`.\n\n**Reference answer:** **15 kN**.\n\nReproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.\n\n**Engineering relevance:** Support settlement and fit-up can create forces without a new external payload. Real use requires verified component-specific inputs; this example is not a certified working load.\n\n## Diagnosing a false conclusion\n\n**Common error:** Solving a redundant support by force balance alone.\n\nDo not turn an average calculation into a guarantee of peak stress at holes, shoulders, welds, contact points or cracks. The stress field can be strongly heterogeneous even if force equilibrium is satisfied. For boundary-condition dependency, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.\n\n## Exercises and answer criteria\n\n**1. Reconstruct.** Draw the section, mark all inputs and reproduce **15 kN**, including units.\n\n*Answer guidance:* Use `F=k delta` with correct dimensions. Confirm the sign and the physical meaning of the quantity.\n\n**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.\n\n*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.\n\n**3. Diagnose.** Explain why this error matters: *solving a redundant support by force balance alone.* Propose a measurement or alternate equation that exposes it.\n\n*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.\n\n## Transfer to a real engineering study\n\nWrite all deflection and slope boundary conditions beside the governing differential equation. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.\n",
          "simulations": []
        }
      ],
      "problems": [
        {
          "id": "MOS-U5-P1",
          "title": "Moment\u2013curvature relation",
          "question": "**Situation:** Uniform E=200 GPa, I=500 cm\u2074 and bending moment 2 kN m.",
          "steps": [
            {
              "explanation": "**Equation:** `kappa=M/(EI)`."
            },
            {
              "explanation": "**Reference answer:** **0.002 1/m**."
            },
            {
              "explanation": "Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path."
            },
            {
              "explanation": "**Engineering relevance:** Curvature is the local change in beam slope per length. Real use requires verified component-specific inputs; this example is not a certified working load."
            }
          ],
          "finalAnswer": "**Engineering relevance:** Curvature is the local change in beam slope per length. Real use requires verified component-specific inputs; this example is not a certified working load."
        },
        {
          "id": "MOS-U5-P2",
          "title": "Simply supported beam deflection",
          "question": "**Situation:** P=8 kN at midspan, L=3 m, E=200 GPa, I=800 cm\u2074.",
          "steps": [
            {
              "explanation": "**Equation:** `delta=PL\u00b3/(48EI)`."
            },
            {
              "explanation": "**Reference answer:** **2.8125 mm**."
            },
            {
              "explanation": "Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path."
            },
            {
              "explanation": "**Engineering relevance:** Long-span design may be governed by deflection before yielding. Real use requires verified component-specific inputs; this example is not a certified working load."
            }
          ],
          "finalAnswer": "**Engineering relevance:** Long-span design may be governed by deflection before yielding. Real use requires verified component-specific inputs; this example is not a certified working load."
        },
        {
          "id": "MOS-U5-P3",
          "title": "Cantilever tip displacement",
          "question": "**Situation:** A cantilever has P=500 N, L=1 m, E=200 GPa, I=400 cm\u2074.",
          "steps": [
            {
              "explanation": "**Equation:** `delta_tip=PL\u00b3/(3EI)`."
            },
            {
              "explanation": "**Reference answer:** **0.20833 mm**."
            },
            {
              "explanation": "Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path."
            },
            {
              "explanation": "**Engineering relevance:** A flexible cantilever mechanism can meet strength limits but miss positional tolerances. Real use requires verified component-specific inputs; this example is not a certified working load."
            }
          ],
          "finalAnswer": "**Engineering relevance:** A flexible cantilever mechanism can meet strength limits but miss positional tolerances. Real use requires verified component-specific inputs; this example is not a certified working load."
        },
        {
          "id": "MOS-U5-P4",
          "title": "Strain energy and Castigliano",
          "question": "**Situation:** Bar with axial load 12 kN and extension 0.3 mm in a linear test.",
          "steps": [
            {
              "explanation": "**Equation:** `U=0.5Pdelta`."
            },
            {
              "explanation": "**Reference answer:** **1.8 J**."
            },
            {
              "explanation": "Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path."
            },
            {
              "explanation": "**Engineering relevance:** Energy methods provide independent displacement checks and stiffness estimates. Real use requires verified component-specific inputs; this example is not a certified working load."
            }
          ],
          "finalAnswer": "**Engineering relevance:** Energy methods provide independent displacement checks and stiffness estimates. Real use requires verified component-specific inputs; this example is not a certified working load."
        },
        {
          "id": "MOS-U5-P5",
          "title": "Redundant supports and superposition",
          "question": "**Situation:** A linear axial spring of stiffness 60 kN/mm is restrained to stretch 0.25 mm.",
          "steps": [
            {
              "explanation": "**Equation:** `F=k delta`."
            },
            {
              "explanation": "**Reference answer:** **15 kN**."
            },
            {
              "explanation": "Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path."
            },
            {
              "explanation": "**Engineering relevance:** Support settlement and fit-up can create forces without a new external payload. Real use requires verified component-specific inputs; this example is not a certified working load."
            }
          ],
          "finalAnswer": "**Engineering relevance:** Support settlement and fit-up can create forces without a new external payload. Real use requires verified component-specific inputs; this example is not a certified working load."
        }
      ],
      "simulations": [
        "mechanics-of-solids-sim-5"
      ]
    },
    {
      "id": "mechanics-of-solids-unit-6",
      "number": 6,
      "title": "Multiaxial Stress and Yield Criteria",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Multiaxial Stress and Yield Criteria.",
      "sections": [
        {
          "secNumber": "6.1",
          "heading": "Stress components and equilibrium",
          "content": "# Unit 6, Lesson 1 \u2014 Stress components and equilibrium\n\n**Learning target.** Transform stresses, identify principal values and relate multiaxial elastic response to simplified ductile failure estimates. Explain the terms of `mean_normal=(sigma_x+sigma_y)/2`, reconstruct the teaching example and identify one condition where the relation must be modified.\n\n## Physical model\n\nOn a small material element, normal and shear stresses appear on several faces. Moment equilibrium requires the conventional shear components tau_xy=tau_yx in a classical continuum without couple stresses. The Cauchy stress tensor compactly encodes the plane-dependent traction. A plane-stress model assumes stress normal to a thin free surface is negligible; it is not the same as uniform strain.\n\nThe essential step is to identify what has been idealized. Stress is not directly interchangeable with force; strain is not identical to movement of a distant fixture; and a computed failure index is not an observed failure. Mark the difference between what you assumed, calculated and measured in your notebook.\n\n**Context:** In 2D sigma_x=80 MPa, sigma_y=20 MPa, tau_xy=30 MPa. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.\n\n## Governing relationship and assumptions\n\n**Teaching relation:** `mean_normal=(sigma_x+sigma_y)/2`.\n\nA coordinate transform changes stress components but cannot change principal values or trace. Material response in anisotropic solids may depend on direction even if stress invariants remain mathematically defined. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **stress components and equilibrium**.\n\nIf the part has a geometric discontinuity, peak local stress may lie far above a cross-sectional average. Document where each area and section property is defined and whether a stress concentration factor is relevant.\n\n## Worked example and interpretation\n\n**Situation:** In 2D sigma_x=80 MPa, sigma_y=20 MPa, tau_xy=30 MPa.\n\n**Equation:** `mean_normal=(sigma_x+sigma_y)/2`.\n\n**Reference answer:** **50 MPa mean normal stress**.\n\nReproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.\n\n**Engineering relevance:** Component conventions must be documented when importing FE results. Real use requires verified component-specific inputs; this example is not a certified working load.\n\n## Diagnosing a false conclusion\n\n**Common error:** Assuming shear on one element face has no complementary shear on the adjacent face.\n\nA negative quantity is not by itself a failure: under a defined sign convention, negative axial stress may represent compression and negative strain may represent contraction. What matters is whether the assumed physical constraint can transmit that action. For invariance across coordinate rotations, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.\n\n## Exercises and answer criteria\n\n**1. Reconstruct.** Draw the section, mark all inputs and reproduce **50 MPa mean normal stress**, including units.\n\n*Answer guidance:* Use `mean_normal=(sigma_x+sigma_y)/2` with correct dimensions. Confirm the sign and the physical meaning of the quantity.\n\n**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.\n\n*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.\n\n**3. Diagnose.** Explain why this error matters: *assuming shear on one element face has no complementary shear on the adjacent face.* Propose a measurement or alternate equation that exposes it.\n\n*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.\n\n## Transfer to a real engineering study\n\nCheck a limiting rotation and a zero-shear case to catch sign and convention mistakes. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.\n",
          "simulations": []
        },
        {
          "secNumber": "6.2",
          "heading": "stress transformation",
          "content": "# Unit 6, Lesson 2 \u2014 Plane-stress transformation\n\n**Learning target.** Transform stresses, identify principal values and relate multiaxial elastic response to simplified ductile failure estimates. Explain the terms of `sigma_n=80cos\u00b230\u00b0+20sin\u00b230\u00b0`, reconstruct the teaching example and identify one condition where the relation must be modified.\n\n## Physical model\n\nNormal stress acting on a plane rotated by angle theta follows sigma_n=sigma_x cos\u00b2theta+sigma_y sin\u00b2theta+2 tau_xy sin theta cos theta, with appropriate positive-angle and stress convention. The shear transformation uses corresponding sign terms. A principal plane carries no in-plane shear. Test the equation at theta=0 and theta=90\u00b0 as independent boundary checks.\n\nUse the structure of the equation to make an advance prediction. Decide which variables the response is proportional to and which enter as powers, reciprocals or geometric factors. This helps expose a unit error before it becomes an engineering conclusion.\n\n**Context:** Plane stress sigma_x=80, sigma_y=20 and tau_xy=0 MPa, rotated 30\u00b0. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.\n\n## Governing relationship and assumptions\n\n**Teaching relation:** `sigma_n=80cos\u00b230\u00b0+20sin\u00b230\u00b0`.\n\nA coordinate transform changes stress components but cannot change principal values or trace. Material response in anisotropic solids may depend on direction even if stress invariants remain mathematically defined. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **plane-stress transformation**.\n\nThe model applies over a domain, not to every conceivable physical state. For instance, elastic formulas generally require stresses within an appropriate linear range and strains small enough that deformed geometry does not change the equilibrium appreciably.\n\n## Worked example and interpretation\n\n**Situation:** Plane stress sigma_x=80, sigma_y=20 and tau_xy=0 MPa, rotated 30\u00b0.\n\n**Equation:** `sigma_n=80cos\u00b230\u00b0+20sin\u00b230\u00b0`.\n\n**Reference answer:** **65 MPa**.\n\nReproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.\n\n**Engineering relevance:** Stress transformation helps interpret off-axis strain gauges. Real use requires verified component-specific inputs; this example is not a certified working load.\n\n## Diagnosing a false conclusion\n\n**Common error:** Using degrees as radians in a trigonometric library.\n\nLinear elastic predictions cannot be extended beyond yield or into damage without a material law and a method appropriate to those regimes. Temperature and loading rate may change the relevant parameters. For invariance across coordinate rotations, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.\n\n## Exercises and answer criteria\n\n**1. Reconstruct.** Draw the section, mark all inputs and reproduce **65 MPa**, including units.\n\n*Answer guidance:* Use `sigma_n=80cos\u00b230\u00b0+20sin\u00b230\u00b0` with correct dimensions. Confirm the sign and the physical meaning of the quantity.\n\n**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.\n\n*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.\n\n**3. Diagnose.** Explain why this error matters: *using degrees as radians in a trigonometric library.* Propose a measurement or alternate equation that exposes it.\n\n*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.\n\n## Transfer to a real engineering study\n\nCheck a limiting rotation and a zero-shear case to catch sign and convention mistakes. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.\n",
          "simulations": []
        },
        {
          "secNumber": "6.3",
          "heading": "Principal stress and Mohr circle",
          "content": "# Unit 6, Lesson 3 \u2014 Principal stress and Mohr circle\n\n**Learning target.** Transform stresses, identify principal values and relate multiaxial elastic response to simplified ductile failure estimates. Explain the terms of `sigma_1=60+sqrt(40\u00b2+30\u00b2)`, reconstruct the teaching example and identify one condition where the relation must be modified.\n\n## Physical model\n\nIn a plane stress state, principal in-plane values are sigma_avg \u00b1sqrt(((sigma_x\u2212sigma_y)/2)\u00b2+tau_xy\u00b2). Their sum equals sigma_x+sigma_y and principal-plane shear vanishes. The out-of-plane third principal stress equals zero only in the plane stress idealization. Ranking maximum and minimum principal stresses requires including that third value for full three-dimensional comparisons.\n\nAn instructive limiting case is one where the load goes to zero, the span approaches zero, the restraint vanishes or the cross-section grows very large. The response should behave consistently with mechanics. A finite nonzero stress with no load may indicate a missing preload or a mathematical mistake.\n\n**Context:** Plane stress sigma_x=100, sigma_y=20 and tau=30 MPa. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.\n\n## Governing relationship and assumptions\n\n**Teaching relation:** `sigma_1=60+sqrt(40\u00b2+30\u00b2)`.\n\nA coordinate transform changes stress components but cannot change principal values or trace. Material response in anisotropic solids may depend on direction even if stress invariants remain mathematically defined. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **principal stress and mohr circle**.\n\nAn independent second approach might use a global equilibrium relation, a limiting case, an energy balance or a laboratory reading. It should not merely repeat the same arithmetic with extra decimal places.\n\n## Worked example and interpretation\n\n**Situation:** Plane stress sigma_x=100, sigma_y=20 and tau=30 MPa.\n\n**Equation:** `sigma_1=60+sqrt(40\u00b2+30\u00b2)`.\n\n**Reference answer:** **110 MPa**.\n\nReproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.\n\n**Engineering relevance:** Brittle failure checks often consider tensile principal stress. Real use requires verified component-specific inputs; this example is not a certified working load.\n\n## Diagnosing a false conclusion\n\n**Common error:** Ignoring the zero third principal when using a 3D failure criterion.\n\nSafety factors do not cure a mistaken model, incorrectly placed support, unnoticed crack or unrealistic input. Start by verifying the load path and the chosen failure mode. For invariance across coordinate rotations, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.\n\n## Exercises and answer criteria\n\n**1. Reconstruct.** Draw the section, mark all inputs and reproduce **110 MPa**, including units.\n\n*Answer guidance:* Use `sigma_1=60+sqrt(40\u00b2+30\u00b2)` with correct dimensions. Confirm the sign and the physical meaning of the quantity.\n\n**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.\n\n*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.\n\n**3. Diagnose.** Explain why this error matters: *ignoring the zero third principal when using a 3d failure criterion.* Propose a measurement or alternate equation that exposes it.\n\n*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.\n\n## Transfer to a real engineering study\n\nCheck a limiting rotation and a zero-shear case to catch sign and convention mistakes. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.\n",
          "simulations": []
        },
        {
          "secNumber": "6.4",
          "heading": "Generalized Hooke law and plane strain",
          "content": "# Unit 6, Lesson 4 \u2014 Generalized Hooke law and plane strain\n\n**Learning target.** Transform stresses, identify principal values and relate multiaxial elastic response to simplified ductile failure estimates. Explain the terms of `epsilon_x=(sigma_x\u2212nu sigma_y)/E`, reconstruct the teaching example and identify one condition where the relation must be modified.\n\n## Physical model\n\nIsotropic small-strain elasticity relates axial strain to all normal stresses through e_x=[sigma_x\u2212nu(sigma_y+sigma_z)]/E. Thus a uniaxial strain response is not simply sigma_x/E when substantial lateral stresses exist. Under plane strain, out-of-plane strain is constrained to zero and sigma_z is generally nonzero. Plane stress instead sets sigma_z approximately zero.\n\nThe word \u201cstrength\u201d is not interchangeable with \u201cstiffness.\u201d Strength concerns exceeding a material or structural limit; stiffness concerns the load-to-deformation relation. Stability and damage mechanisms introduce further limits, which require their own data and assumptions.\n\n**Context:** E=200 GPa, nu=0.3, sigma_x=120 MPa, sigma_y=40 MPa, sigma_z=0. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.\n\n## Governing relationship and assumptions\n\n**Teaching relation:** `epsilon_x=(sigma_x\u2212nu sigma_y)/E`.\n\nA coordinate transform changes stress components but cannot change principal values or trace. Material response in anisotropic solids may depend on direction even if stress invariants remain mathematically defined. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **generalized hooke law and plane strain**.\n\nA true engineering calculation should be independently reproducible from the drawing and a concise input table. Another reader needs to know the sign convention, material assumptions, geometry, force units and exactly which cross-section or point is analyzed.\n\n## Worked example and interpretation\n\n**Situation:** E=200 GPa, nu=0.3, sigma_x=120 MPa, sigma_y=40 MPa, sigma_z=0.\n\n**Equation:** `epsilon_x=(sigma_x\u2212nu sigma_y)/E`.\n\n**Reference answer:** **540 microstrain**.\n\nReproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.\n\n**Engineering relevance:** Thick constrained components require the right strain boundary model. Real use requires verified component-specific inputs; this example is not a certified working load.\n\n## Diagnosing a false conclusion\n\n**Common error:** Assuming zero out-of-plane strain implies zero out-of-plane stress.\n\nFailure-mode checks are not independent when the same hidden parameter drives all of them. A poor thickness measurement can bias area, area moment and nominal stress together; correlated uncertainties should be handled explicitly. For invariance across coordinate rotations, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.\n\n## Exercises and answer criteria\n\n**1. Reconstruct.** Draw the section, mark all inputs and reproduce **540 microstrain**, including units.\n\n*Answer guidance:* Use `epsilon_x=(sigma_x\u2212nu sigma_y)/E` with correct dimensions. Confirm the sign and the physical meaning of the quantity.\n\n**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.\n\n*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.\n\n**3. Diagnose.** Explain why this error matters: *assuming zero out-of-plane strain implies zero out-of-plane stress.* Propose a measurement or alternate equation that exposes it.\n\n*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.\n\n## Transfer to a real engineering study\n\nCheck a limiting rotation and a zero-shear case to catch sign and convention mistakes. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.\n",
          "simulations": []
        },
        {
          "secNumber": "6.5",
          "heading": "Von Mises and Tresca checks",
          "content": "# Unit 6, Lesson 5 \u2014 Von Mises and Tresca checks\n\n**Learning target.** Transform stresses, identify principal values and relate multiaxial elastic response to simplified ductile failure estimates. Explain the terms of `sigma_vm=sqrt(sigma_x\u00b2\u2212sigma_x sigma_y+sigma_y\u00b2+3tau\u00b2)`, reconstruct the teaching example and identify one condition where the relation must be modified.\n\n## Physical model\n\nFor isotropic ductile metals under a plane stress approximation, von Mises equivalent stress is sqrt(sigma_x\u00b2\u2212sigma_x sigma_y+sigma_y\u00b2+3 tau_xy\u00b2). It compares a multiaxial stress state to a uniaxial yielding characterization, not to ultimate strength automatically. Tresca uses maximum difference of principal stresses and can be more conservative for some states. Neither is a fatigue-life law.\n\nFor a real joint or machine, the ideal solution is a starting hypothesis. Surface condition, machining tolerances, alignment, residual stress, temperature and spectrum of operating loads can dominate local behavior. Identify a feasible experiment that might falsify the calculation.\n\n**Context:** Plane stress sigma_x=100 MPa, sigma_y=0, tau_xy=50 MPa. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.\n\n## Governing relationship and assumptions\n\n**Teaching relation:** `sigma_vm=sqrt(sigma_x\u00b2\u2212sigma_x sigma_y+sigma_y\u00b2+3tau\u00b2)`.\n\nA coordinate transform changes stress components but cannot change principal values or trace. Material response in anisotropic solids may depend on direction even if stress invariants remain mathematically defined. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **von mises and tresca checks**.\n\nChecking the dimensions of each term is necessary but not sufficient. An equation may carry the right SI units while using the wrong load boundary, neutral axis, shear area, material condition, or ideal support type.\n\n## Worked example and interpretation\n\n**Situation:** Plane stress sigma_x=100 MPa, sigma_y=0, tau_xy=50 MPa.\n\n**Equation:** `sigma_vm=sqrt(sigma_x\u00b2\u2212sigma_x sigma_y+sigma_y\u00b2+3tau\u00b2)`.\n\n**Reference answer:** **132.29 MPa**.\n\nReproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.\n\n**Engineering relevance:** Material yield checks need a chosen criterion and a strength value at operating conditions. Real use requires verified component-specific inputs; this example is not a certified working load.\n\n## Diagnosing a false conclusion\n\n**Common error:** Treating equivalent stress as a measured physical stress on one specific face.\n\nDo not turn an average calculation into a guarantee of peak stress at holes, shoulders, welds, contact points or cracks. The stress field can be strongly heterogeneous even if force equilibrium is satisfied. For invariance across coordinate rotations, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.\n\n## Exercises and answer criteria\n\n**1. Reconstruct.** Draw the section, mark all inputs and reproduce **132.29 MPa**, including units.\n\n*Answer guidance:* Use `sigma_vm=sqrt(sigma_x\u00b2\u2212sigma_x sigma_y+sigma_y\u00b2+3tau\u00b2)` with correct dimensions. Confirm the sign and the physical meaning of the quantity.\n\n**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.\n\n*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.\n\n**3. Diagnose.** Explain why this error matters: *treating equivalent stress as a measured physical stress on one specific face.* Propose a measurement or alternate equation that exposes it.\n\n*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.\n\n## Transfer to a real engineering study\n\nCheck a limiting rotation and a zero-shear case to catch sign and convention mistakes. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.\n",
          "simulations": []
        }
      ],
      "problems": [
        {
          "id": "MOS-U6-P1",
          "title": "Stress components and equilibrium",
          "question": "**Situation:** In 2D sigma_x=80 MPa, sigma_y=20 MPa, tau_xy=30 MPa.",
          "steps": [
            {
              "explanation": "**Equation:** `mean_normal=(sigma_x+sigma_y)/2`."
            },
            {
              "explanation": "**Reference answer:** **50 MPa mean normal stress**."
            },
            {
              "explanation": "Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path."
            },
            {
              "explanation": "**Engineering relevance:** Component conventions must be documented when importing FE results. Real use requires verified component-specific inputs; this example is not a certified working load."
            }
          ],
          "finalAnswer": "**Engineering relevance:** Component conventions must be documented when importing FE results. Real use requires verified component-specific inputs; this example is not a certified working load."
        },
        {
          "id": "MOS-U6-P2",
          "title": "stress transformation",
          "question": "**Situation:** Plane stress sigma_x=80, sigma_y=20 and tau_xy=0 MPa, rotated 30\u00b0.",
          "steps": [
            {
              "explanation": "**Equation:** `sigma_n=80cos\u00b230\u00b0+20sin\u00b230\u00b0`."
            },
            {
              "explanation": "**Reference answer:** **65 MPa**."
            },
            {
              "explanation": "Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path."
            },
            {
              "explanation": "**Engineering relevance:** Stress transformation helps interpret off-axis strain gauges. Real use requires verified component-specific inputs; this example is not a certified working load."
            }
          ],
          "finalAnswer": "**Engineering relevance:** Stress transformation helps interpret off-axis strain gauges. Real use requires verified component-specific inputs; this example is not a certified working load."
        },
        {
          "id": "MOS-U6-P3",
          "title": "Principal stress and Mohr circle",
          "question": "**Situation:** Plane stress sigma_x=100, sigma_y=20 and tau=30 MPa.",
          "steps": [
            {
              "explanation": "**Equation:** `sigma_1=60+sqrt(40\u00b2+30\u00b2)`."
            },
            {
              "explanation": "**Reference answer:** **110 MPa**."
            },
            {
              "explanation": "Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path."
            },
            {
              "explanation": "**Engineering relevance:** Brittle failure checks often consider tensile principal stress. Real use requires verified component-specific inputs; this example is not a certified working load."
            }
          ],
          "finalAnswer": "**Engineering relevance:** Brittle failure checks often consider tensile principal stress. Real use requires verified component-specific inputs; this example is not a certified working load."
        },
        {
          "id": "MOS-U6-P4",
          "title": "Generalized Hooke law and plane strain",
          "question": "**Situation:** E=200 GPa, nu=0.3, sigma_x=120 MPa, sigma_y=40 MPa, sigma_z=0.",
          "steps": [
            {
              "explanation": "**Equation:** `epsilon_x=(sigma_x\u2212nu sigma_y)/E`."
            },
            {
              "explanation": "**Reference answer:** **540 microstrain**."
            },
            {
              "explanation": "Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path."
            },
            {
              "explanation": "**Engineering relevance:** Thick constrained components require the right strain boundary model. Real use requires verified component-specific inputs; this example is not a certified working load."
            }
          ],
          "finalAnswer": "**Engineering relevance:** Thick constrained components require the right strain boundary model. Real use requires verified component-specific inputs; this example is not a certified working load."
        },
        {
          "id": "MOS-U6-P5",
          "title": "Von Mises and Tresca checks",
          "question": "**Situation:** Plane stress sigma_x=100 MPa, sigma_y=0, tau_xy=50 MPa.",
          "steps": [
            {
              "explanation": "**Equation:** `sigma_vm=sqrt(sigma_x\u00b2\u2212sigma_x sigma_y+sigma_y\u00b2+3tau\u00b2)`."
            },
            {
              "explanation": "**Reference answer:** **132.29 MPa**."
            },
            {
              "explanation": "Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path."
            },
            {
              "explanation": "**Engineering relevance:** Material yield checks need a chosen criterion and a strength value at operating conditions. Real use requires verified component-specific inputs; this example is not a certified working load."
            }
          ],
          "finalAnswer": "**Engineering relevance:** Material yield checks need a chosen criterion and a strength value at operating conditions. Real use requires verified component-specific inputs; this example is not a certified working load."
        }
      ],
      "simulations": [
        "mechanics-of-solids-sim-6"
      ]
    },
    {
      "id": "mechanics-of-solids-unit-7",
      "number": 7,
      "title": "Stability, Fatigue and Fracture",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Stability, Fatigue and Fracture.",
      "sections": [
        {
          "secNumber": "7.1",
          "heading": "Euler column buckling",
          "content": "# Unit 7, Lesson 1 \u2014 Euler column buckling\n\n**Learning target.** Separate loss of elastic stability from yielding and introduce mechanical damage under repeated and crack-like loading. Explain the terms of `Pcr=\u03c0\u00b2EI/L\u00b2`, reconstruct the teaching example and identify one condition where the relation must be modified.\n\n## Physical model\n\nA sufficiently slender ideal elastic column can lose stability at Euler load Pcr=\u03c0\u00b2EI/(KL)\u00b2. K is the effective-length factor determined by end rotation and translation restraints, not a material property. Yielding and imperfections become important outside the ideal slender elastic regime. An equilibrium-based critical load is not the same as a recommended safe working load.\n\nThe essential step is to identify what has been idealized. Stress is not directly interchangeable with force; strain is not identical to movement of a distant fixture; and a computed failure index is not an observed failure. Mark the difference between what you assumed, calculated and measured in your notebook.\n\n**Context:** Pinned-pinned steel column E=200 GPa, I=400 cm\u2074, L=3 m. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.\n\n## Governing relationship and assumptions\n\n**Teaching relation:** `Pcr=\u03c0\u00b2EI/L\u00b2`.\n\nAn instantaneous elastic calculation says little about growth of a crack under repeated stress. Conversely, a measured fatigue limit cannot prevent buckling of a very slender compression member. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **euler column buckling**.\n\nIf the part has a geometric discontinuity, peak local stress may lie far above a cross-sectional average. Document where each area and section property is defined and whether a stress concentration factor is relevant.\n\n## Worked example and interpretation\n\n**Situation:** Pinned-pinned steel column E=200 GPa, I=400 cm\u2074, L=3 m.\n\n**Equation:** `Pcr=\u03c0\u00b2EI/L\u00b2`.\n\n**Reference answer:** **877.3 kN**.\n\nReproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.\n\n**Engineering relevance:** Column selection requires geometric imperfection and code-based strength checks. Real use requires verified component-specific inputs; this example is not a certified working load.\n\n## Diagnosing a false conclusion\n\n**Common error:** Using an unrestrained length for a column with different end conditions without setting K.\n\nA negative quantity is not by itself a failure: under a defined sign convention, negative axial stress may represent compression and negative strain may represent contraction. What matters is whether the assumed physical constraint can transmit that action. For failure mode and service history, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.\n\n## Exercises and answer criteria\n\n**1. Reconstruct.** Draw the section, mark all inputs and reproduce **877.3 kN**, including units.\n\n*Answer guidance:* Use `Pcr=\u03c0\u00b2EI/L\u00b2` with correct dimensions. Confirm the sign and the physical meaning of the quantity.\n\n**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.\n\n*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.\n\n**3. Diagnose.** Explain why this error matters: *using an unrestrained length for a column with different end conditions without setting k.* Propose a measurement or alternate equation that exposes it.\n\n*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.\n\n## Transfer to a real engineering study\n\nClassify expected response as strength, stability, fracture, environmental degradation or fatigue before selecting a criterion. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.\n",
          "simulations": []
        },
        {
          "secNumber": "7.2",
          "heading": "Eccentric compression and combined bending",
          "content": "# Unit 7, Lesson 2 \u2014 Eccentric compression and combined bending\n\n**Learning target.** Separate loss of elastic stability from yielding and introduce mechanical damage under repeated and crack-like loading. Explain the terms of `M=P e`, reconstruct the teaching example and identify one condition where the relation must be modified.\n\n## Physical model\n\nA compressive force whose line of action misses a section centroid introduces bending moment M=Pe. For an elastic section, compressive axial stress and bending stress superimpose before stability effects. The sign at each fiber depends on moment orientation; opposite edges may face very different stresses. For slender members, second-order P\u2013delta amplification may invalidate a first-order formula.\n\nUse the structure of the equation to make an advance prediction. Decide which variables the response is proportional to and which enter as powers, reciprocals or geometric factors. This helps expose a unit error before it becomes an engineering conclusion.\n\n**Context:** Compression P=30 kN acts with eccentricity e=20 mm. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.\n\n## Governing relationship and assumptions\n\n**Teaching relation:** `M=P e`.\n\nAn instantaneous elastic calculation says little about growth of a crack under repeated stress. Conversely, a measured fatigue limit cannot prevent buckling of a very slender compression member. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **eccentric compression and combined bending**.\n\nThe model applies over a domain, not to every conceivable physical state. For instance, elastic formulas generally require stresses within an appropriate linear range and strains small enough that deformed geometry does not change the equilibrium appreciably.\n\n## Worked example and interpretation\n\n**Situation:** Compression P=30 kN acts with eccentricity e=20 mm.\n\n**Equation:** `M=P e`.\n\n**Reference answer:** **0.6 kN m**.\n\nReproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.\n\n**Engineering relevance:** Alignment tolerances can influence peak stress in brackets and columns. Real use requires verified component-specific inputs; this example is not a certified working load.\n\n## Diagnosing a false conclusion\n\n**Common error:** Using only P/A when the load is eccentric.\n\nLinear elastic predictions cannot be extended beyond yield or into damage without a material law and a method appropriate to those regimes. Temperature and loading rate may change the relevant parameters. For failure mode and service history, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.\n\n## Exercises and answer criteria\n\n**1. Reconstruct.** Draw the section, mark all inputs and reproduce **0.6 kN m**, including units.\n\n*Answer guidance:* Use `M=P e` with correct dimensions. Confirm the sign and the physical meaning of the quantity.\n\n**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.\n\n*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.\n\n**3. Diagnose.** Explain why this error matters: *using only p/a when the load is eccentric.* Propose a measurement or alternate equation that exposes it.\n\n*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.\n\n## Transfer to a real engineering study\n\nClassify expected response as strength, stability, fracture, environmental degradation or fatigue before selecting a criterion. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.\n",
          "simulations": []
        },
        {
          "secNumber": "7.3",
          "heading": "Stress concentration and notch sensitivity",
          "content": "# Unit 7, Lesson 3 \u2014 Stress concentration and notch sensitivity\n\n**Learning target.** Separate loss of elastic stability from yielding and introduce mechanical damage under repeated and crack-like loading. Explain the terms of `sigma_peak=Kt sigma_nom`, reconstruct the teaching example and identify one condition where the relation must be modified.\n\n## Physical model\n\nA hole or fillet changes local elastic stress even when nominal section force is unchanged. The theoretical elastic stress concentration factor Kt relates peak elastic stress to a nominal reference; its definition depends on gross or net nominal stress convention. Fatigue effective concentration Kf may differ from Kt due to material notch sensitivity. Do not use a chart factor without checking its specified geometry.\n\nAn instructive limiting case is one where the load goes to zero, the span approaches zero, the restraint vanishes or the cross-section grows very large. The response should behave consistently with mechanics. A finite nonzero stress with no load may indicate a missing preload or a mathematical mistake.\n\n**Context:** A geometry has nominal tension 60 MPa and Kt=2.5. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.\n\n## Governing relationship and assumptions\n\n**Teaching relation:** `sigma_peak=Kt sigma_nom`.\n\nAn instantaneous elastic calculation says little about growth of a crack under repeated stress. Conversely, a measured fatigue limit cannot prevent buckling of a very slender compression member. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **stress concentration and notch sensitivity**.\n\nAn independent second approach might use a global equilibrium relation, a limiting case, an energy balance or a laboratory reading. It should not merely repeat the same arithmetic with extra decimal places.\n\n## Worked example and interpretation\n\n**Situation:** A geometry has nominal tension 60 MPa and Kt=2.5.\n\n**Equation:** `sigma_peak=Kt sigma_nom`.\n\n**Reference answer:** **150 MPa elastic peak estimate**.\n\nReproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.\n\n**Engineering relevance:** Smooth transitions can lower local elastic stress gradients. Real use requires verified component-specific inputs; this example is not a certified working load.\n\n## Diagnosing a false conclusion\n\n**Common error:** Multiplying fatigue stress by a theoretical Kt without checking the fatigue notch factor.\n\nSafety factors do not cure a mistaken model, incorrectly placed support, unnoticed crack or unrealistic input. Start by verifying the load path and the chosen failure mode. For failure mode and service history, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.\n\n## Exercises and answer criteria\n\n**1. Reconstruct.** Draw the section, mark all inputs and reproduce **150 MPa elastic peak estimate**, including units.\n\n*Answer guidance:* Use `sigma_peak=Kt sigma_nom` with correct dimensions. Confirm the sign and the physical meaning of the quantity.\n\n**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.\n\n*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.\n\n**3. Diagnose.** Explain why this error matters: *multiplying fatigue stress by a theoretical kt without checking the fatigue notch factor.* Propose a measurement or alternate equation that exposes it.\n\n*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.\n\n## Transfer to a real engineering study\n\nClassify expected response as strength, stability, fracture, environmental degradation or fatigue before selecting a criterion. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.\n",
          "simulations": []
        },
        {
          "secNumber": "7.4",
          "heading": "Fatigue under fluctuating stress",
          "content": "# Unit 7, Lesson 4 \u2014 Fatigue under fluctuating stress\n\n**Learning target.** Separate loss of elastic stability from yielding and introduce mechanical damage under repeated and crack-like loading. Explain the terms of `sigma_a=(100\u221220)/2; sigma_m=(100+20)/2`, reconstruct the teaching example and identify one condition where the relation must be modified.\n\n## Physical model\n\nAlternating stress amplitude sigma_a=(sigma_max\u2212sigma_min)/2 and mean stress sigma_m=(sigma_max+sigma_min)/2 describe constant-amplitude uniaxial cycling. A linear Goodman screening relation can compare tensile mean stress with a specified endurance-like strength and ultimate tensile strength. It is not a universal life prediction, especially for nonferrous materials without a clear fatigue limit. Loading spectra and surface finish matter.\n\nThe word \u201cstrength\u201d is not interchangeable with \u201cstiffness.\u201d Strength concerns exceeding a material or structural limit; stiffness concerns the load-to-deformation relation. Stability and damage mechanisms introduce further limits, which require their own data and assumptions.\n\n**Context:** A cycle ranges from 20 to 100 MPa in uniaxial tension. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.\n\n## Governing relationship and assumptions\n\n**Teaching relation:** `sigma_a=(100\u221220)/2; sigma_m=(100+20)/2`.\n\nAn instantaneous elastic calculation says little about growth of a crack under repeated stress. Conversely, a measured fatigue limit cannot prevent buckling of a very slender compression member. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **fatigue under fluctuating stress**.\n\nA true engineering calculation should be independently reproducible from the drawing and a concise input table. Another reader needs to know the sign convention, material assumptions, geometry, force units and exactly which cross-section or point is analyzed.\n\n## Worked example and interpretation\n\n**Situation:** A cycle ranges from 20 to 100 MPa in uniaxial tension.\n\n**Equation:** `sigma_a=(100\u221220)/2; sigma_m=(100+20)/2`.\n\n**Reference answer:** **40 MPa amplitude and 60 MPa mean**.\n\nReproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.\n\n**Engineering relevance:** Motor shafts and fasteners can fail from repeated load variations. Real use requires verified component-specific inputs; this example is not a certified working load.\n\n## Diagnosing a false conclusion\n\n**Common error:** Using maximum stress as fatigue amplitude.\n\nFailure-mode checks are not independent when the same hidden parameter drives all of them. A poor thickness measurement can bias area, area moment and nominal stress together; correlated uncertainties should be handled explicitly. For failure mode and service history, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.\n\n## Exercises and answer criteria\n\n**1. Reconstruct.** Draw the section, mark all inputs and reproduce **40 MPa amplitude and 60 MPa mean**, including units.\n\n*Answer guidance:* Use `sigma_a=(100\u221220)/2; sigma_m=(100+20)/2` with correct dimensions. Confirm the sign and the physical meaning of the quantity.\n\n**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.\n\n*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.\n\n**3. Diagnose.** Explain why this error matters: *using maximum stress as fatigue amplitude.* Propose a measurement or alternate equation that exposes it.\n\n*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.\n\n## Transfer to a real engineering study\n\nClassify expected response as strength, stability, fracture, environmental degradation or fatigue before selecting a criterion. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.\n",
          "simulations": []
        },
        {
          "secNumber": "7.5",
          "heading": "Crack driving force and toughness",
          "content": "# Unit 7, Lesson 5 \u2014 Crack driving force and toughness\n\n**Learning target.** Separate loss of elastic stability from yielding and introduce mechanical damage under repeated and crack-like loading. Explain the terms of `K_I=Y sigma sqrt(\u03c0a)`, reconstruct the teaching example and identify one condition where the relation must be modified.\n\n## Physical model\n\nFor a cracked component in a suitable linear elastic mode I regime, KI=Y sigma sqrt(\u03c0a). Y describes geometry and crack configuration; a is a defined crack size in metres. Comparing KI to toughness KIc is meaningful only when the material state, thickness, environment and fracture regime are appropriate. Crack growth under cyclic loading requires additional data beyond this instantaneous intensity.\n\nFor a real joint or machine, the ideal solution is a starting hypothesis. Surface condition, machining tolerances, alignment, residual stress, temperature and spectrum of operating loads can dominate local behavior. Identify a feasible experiment that might falsify the calculation.\n\n**Context:** For a simplified crack Y=1, sigma=100 MPa, a=1 mm. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.\n\n## Governing relationship and assumptions\n\n**Teaching relation:** `K_I=Y sigma sqrt(\u03c0a)`.\n\nAn instantaneous elastic calculation says little about growth of a crack under repeated stress. Conversely, a measured fatigue limit cannot prevent buckling of a very slender compression member. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **crack driving force and toughness**.\n\nChecking the dimensions of each term is necessary but not sufficient. An equation may carry the right SI units while using the wrong load boundary, neutral axis, shear area, material condition, or ideal support type.\n\n## Worked example and interpretation\n\n**Situation:** For a simplified crack Y=1, sigma=100 MPa, a=1 mm.\n\n**Equation:** `K_I=Y sigma sqrt(\u03c0a)`.\n\n**Reference answer:** **5.605 MPa sqrt(m)**.\n\nReproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.\n\n**Engineering relevance:** Inspection intervals require crack growth and detection-limit evidence. Real use requires verified component-specific inputs; this example is not a certified working load.\n\n## Diagnosing a false conclusion\n\n**Common error:** Using millimetres directly inside sqrt(\u03c0a) when toughness uses sqrt(m).\n\nDo not turn an average calculation into a guarantee of peak stress at holes, shoulders, welds, contact points or cracks. The stress field can be strongly heterogeneous even if force equilibrium is satisfied. For failure mode and service history, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.\n\n## Exercises and answer criteria\n\n**1. Reconstruct.** Draw the section, mark all inputs and reproduce **5.605 MPa sqrt(m)**, including units.\n\n*Answer guidance:* Use `K_I=Y sigma sqrt(\u03c0a)` with correct dimensions. Confirm the sign and the physical meaning of the quantity.\n\n**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.\n\n*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.\n\n**3. Diagnose.** Explain why this error matters: *using millimetres directly inside sqrt(\u03c0a) when toughness uses sqrt(m).* Propose a measurement or alternate equation that exposes it.\n\n*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.\n\n## Transfer to a real engineering study\n\nClassify expected response as strength, stability, fracture, environmental degradation or fatigue before selecting a criterion. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.\n",
          "simulations": []
        }
      ],
      "problems": [
        {
          "id": "MOS-U7-P1",
          "title": "Euler column buckling",
          "question": "**Situation:** Pinned-pinned steel column E=200 GPa, I=400 cm\u2074, L=3 m.",
          "steps": [
            {
              "explanation": "**Equation:** `Pcr=\u03c0\u00b2EI/L\u00b2`."
            },
            {
              "explanation": "**Reference answer:** **877.3 kN**."
            },
            {
              "explanation": "Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path."
            },
            {
              "explanation": "**Engineering relevance:** Column selection requires geometric imperfection and code-based strength checks. Real use requires verified component-specific inputs; this example is not a certified working load."
            }
          ],
          "finalAnswer": "**Engineering relevance:** Column selection requires geometric imperfection and code-based strength checks. Real use requires verified component-specific inputs; this example is not a certified working load."
        },
        {
          "id": "MOS-U7-P2",
          "title": "Eccentric compression and combined bending",
          "question": "**Situation:** Compression P=30 kN acts with eccentricity e=20 mm.",
          "steps": [
            {
              "explanation": "**Equation:** `M=P e`."
            },
            {
              "explanation": "**Reference answer:** **0.6 kN m**."
            },
            {
              "explanation": "Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path."
            },
            {
              "explanation": "**Engineering relevance:** Alignment tolerances can influence peak stress in brackets and columns. Real use requires verified component-specific inputs; this example is not a certified working load."
            }
          ],
          "finalAnswer": "**Engineering relevance:** Alignment tolerances can influence peak stress in brackets and columns. Real use requires verified component-specific inputs; this example is not a certified working load."
        },
        {
          "id": "MOS-U7-P3",
          "title": "Stress concentration and notch sensitivity",
          "question": "**Situation:** A geometry has nominal tension 60 MPa and Kt=2.5.",
          "steps": [
            {
              "explanation": "**Equation:** `sigma_peak=Kt sigma_nom`."
            },
            {
              "explanation": "**Reference answer:** **150 MPa elastic peak estimate**."
            },
            {
              "explanation": "Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path."
            },
            {
              "explanation": "**Engineering relevance:** Smooth transitions can lower local elastic stress gradients. Real use requires verified component-specific inputs; this example is not a certified working load."
            }
          ],
          "finalAnswer": "**Engineering relevance:** Smooth transitions can lower local elastic stress gradients. Real use requires verified component-specific inputs; this example is not a certified working load."
        },
        {
          "id": "MOS-U7-P4",
          "title": "Fatigue under fluctuating stress",
          "question": "**Situation:** A cycle ranges from 20 to 100 MPa in uniaxial tension.",
          "steps": [
            {
              "explanation": "**Equation:** `sigma_a=(100\u221220)/2; sigma_m=(100+20)/2`."
            },
            {
              "explanation": "**Reference answer:** **40 MPa amplitude and 60 MPa mean**."
            },
            {
              "explanation": "Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path."
            },
            {
              "explanation": "**Engineering relevance:** Motor shafts and fasteners can fail from repeated load variations. Real use requires verified component-specific inputs; this example is not a certified working load."
            }
          ],
          "finalAnswer": "**Engineering relevance:** Motor shafts and fasteners can fail from repeated load variations. Real use requires verified component-specific inputs; this example is not a certified working load."
        },
        {
          "id": "MOS-U7-P5",
          "title": "Crack driving force and toughness",
          "question": "**Situation:** For a simplified crack Y=1, sigma=100 MPa, a=1 mm.",
          "steps": [
            {
              "explanation": "**Equation:** `K_I=Y sigma sqrt(\u03c0a)`."
            },
            {
              "explanation": "**Reference answer:** **5.605 MPa sqrt(m)**."
            },
            {
              "explanation": "Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path."
            },
            {
              "explanation": "**Engineering relevance:** Inspection intervals require crack growth and detection-limit evidence. Real use requires verified component-specific inputs; this example is not a certified working load."
            }
          ],
          "finalAnswer": "**Engineering relevance:** Inspection intervals require crack growth and detection-limit evidence. Real use requires verified component-specific inputs; this example is not a certified working load."
        }
      ],
      "simulations": [
        "mechanics-of-solids-sim-7"
      ]
    },
    {
      "id": "mechanics-of-solids-unit-8",
      "number": 8,
      "title": "Testing, Models and Engineering Decisions",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Testing, Models and Engineering Decisions.",
      "sections": [
        {
          "secNumber": "8.1",
          "heading": "Tensile test and offset yield",
          "content": "# Unit 8, Lesson 1 \u2014 Tensile test and offset yield\n\n**Learning target.** Develop experiments, instrumentation and numerical checks; combine strength, stiffness, uncertainty and verification in engineering decisions. Explain the terms of `E=\u0394sigma/\u0394epsilon`, reconstruct the teaching example and identify one condition where the relation must be modified.\n\n## Physical model\n\nThe tensile curve depends on strain measurement, cross-section definition, grip alignment, strain rate and temperature. An offset yield estimate constructs a line parallel to the elastic slope, shifted along the strain axis; it does not identify a unique intrinsic event in every material. Ultimate engineering stress and true stress after necking must not be conflated. Include machine compliance correction when needed.\n\nThe essential step is to identify what has been idealized. Stress is not directly interchangeable with force; strain is not identical to movement of a distant fixture; and a computed failure index is not an observed failure. Mark the difference between what you assumed, calculated and measured in your notebook.\n\n**Context:** An initial linear segment changes stress by 100 MPa over strain change 0.0005. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.\n\n## Governing relationship and assumptions\n\n**Teaching relation:** `E=\u0394sigma/\u0394epsilon`.\n\nAn accurate fit on one loading case may conceal incorrect boundary conditions. Experimental validation asks whether a model predicts untrained measurements, whereas code verification checks numerical implementation. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **tensile test and offset yield**.\n\nIf the part has a geometric discontinuity, peak local stress may lie far above a cross-sectional average. Document where each area and section property is defined and whether a stress concentration factor is relevant.\n\n## Worked example and interpretation\n\n**Situation:** An initial linear segment changes stress by 100 MPa over strain change 0.0005.\n\n**Equation:** `E=\u0394sigma/\u0394epsilon`.\n\n**Reference answer:** **200 GPa initial tangent estimate**.\n\nReproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.\n\n**Engineering relevance:** Test reports should identify specimen standard and uncertainty. Real use requires verified component-specific inputs; this example is not a certified working load.\n\n## Diagnosing a false conclusion\n\n**Common error:** Calling the largest engineering tensile stress the elastic modulus.\n\nA negative quantity is not by itself a failure: under a defined sign convention, negative axial stress may represent compression and negative strain may represent contraction. What matters is whether the assumed physical constraint can transmit that action. For verification, calibration and extrapolation, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.\n\n## Exercises and answer criteria\n\n**1. Reconstruct.** Draw the section, mark all inputs and reproduce **200 GPa initial tangent estimate**, including units.\n\n*Answer guidance:* Use `E=\u0394sigma/\u0394epsilon` with correct dimensions. Confirm the sign and the physical meaning of the quantity.\n\n**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.\n\n*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.\n\n**3. Diagnose.** Explain why this error matters: *calling the largest engineering tensile stress the elastic modulus.* Propose a measurement or alternate equation that exposes it.\n\n*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.\n\n## Transfer to a real engineering study\n\nDesign the validation case before tuning material inputs, and preserve raw measured data separately from synthetic examples. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.\n",
          "simulations": []
        },
        {
          "secNumber": "8.2",
          "heading": "Strain gauge conversion",
          "content": "# Unit 8, Lesson 2 \u2014 Strain gauge conversion\n\n**Learning target.** Develop experiments, instrumentation and numerical checks; combine strength, stiffness, uncertainty and verification in engineering decisions. Explain the terms of `\u0394R/R=GF epsilon`, reconstruct the teaching example and identify one condition where the relation must be modified.\n\n## Physical model\n\nA resistance strain gauge uses gauge factor GF=(\u0394R/R)/epsilon along a specified sensing direction. Wheatstone bridge circuitry turns tiny resistance changes into a measurable voltage; completion and temperature compensation matter. A single gauge reports one local component, not a complete three-dimensional stress tensor. Gauge placement, bonding and lead resistance may dominate experimental error.\n\nUse the structure of the equation to make an advance prediction. Decide which variables the response is proportional to and which enter as powers, reciprocals or geometric factors. This helps expose a unit error before it becomes an engineering conclusion.\n\n**Context:** A gauge of GF=2.1 experiences longitudinal strain 600 microstrain. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.\n\n## Governing relationship and assumptions\n\n**Teaching relation:** `\u0394R/R=GF epsilon`.\n\nAn accurate fit on one loading case may conceal incorrect boundary conditions. Experimental validation asks whether a model predicts untrained measurements, whereas code verification checks numerical implementation. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **strain gauge conversion**.\n\nThe model applies over a domain, not to every conceivable physical state. For instance, elastic formulas generally require stresses within an appropriate linear range and strains small enough that deformed geometry does not change the equilibrium appreciably.\n\n## Worked example and interpretation\n\n**Situation:** A gauge of GF=2.1 experiences longitudinal strain 600 microstrain.\n\n**Equation:** `\u0394R/R=GF epsilon`.\n\n**Reference answer:** **0.00126 = 0.126%**.\n\nReproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.\n\n**Engineering relevance:** Strain gauges validate local model predictions when coordinate alignment is known. Real use requires verified component-specific inputs; this example is not a certified working load.\n\n## Diagnosing a false conclusion\n\n**Common error:** Treating a uniaxial gauge reading as the entire principal stress state.\n\nLinear elastic predictions cannot be extended beyond yield or into damage without a material law and a method appropriate to those regimes. Temperature and loading rate may change the relevant parameters. For verification, calibration and extrapolation, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.\n\n## Exercises and answer criteria\n\n**1. Reconstruct.** Draw the section, mark all inputs and reproduce **0.00126 = 0.126%**, including units.\n\n*Answer guidance:* Use `\u0394R/R=GF epsilon` with correct dimensions. Confirm the sign and the physical meaning of the quantity.\n\n**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.\n\n*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.\n\n**3. Diagnose.** Explain why this error matters: *treating a uniaxial gauge reading as the entire principal stress state.* Propose a measurement or alternate equation that exposes it.\n\n*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.\n\n## Transfer to a real engineering study\n\nDesign the validation case before tuning material inputs, and preserve raw measured data separately from synthetic examples. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.\n",
          "simulations": []
        },
        {
          "secNumber": "8.3",
          "heading": "Uncertainty and sensitivity",
          "content": "# Unit 8, Lesson 3 \u2014 Uncertainty and sensitivity\n\n**Learning target.** Develop experiments, instrumentation and numerical checks; combine strength, stiffness, uncertainty and verification in engineering decisions. Explain the terms of `I_new/I_old=(1.02)^3`, reconstruct the teaching example and identify one condition where the relation must be modified.\n\n## Physical model\n\nA dimension measured with uncertainty contributes nonlinearly to properties such as rectangular beam I\u221dh\u00b3 and shaft stress tau\u221dd^\u22123. First-order relative uncertainty propagation can estimate influence when errors are small and independent; correlation and systematic bias need additional treatment. Report uncertainty and resolution rather than implying unlimited digits from a computer.\n\nAn instructive limiting case is one where the load goes to zero, the span approaches zero, the restraint vanishes or the cross-section grows very large. The response should behave consistently with mechanics. A finite nonzero stress with no load may indicate a missing preload or a mathematical mistake.\n\n**Context:** The height of a rectangular beam has a +2% change, with width fixed. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.\n\n## Governing relationship and assumptions\n\n**Teaching relation:** `I_new/I_old=(1.02)^3`.\n\nAn accurate fit on one loading case may conceal incorrect boundary conditions. Experimental validation asks whether a model predicts untrained measurements, whereas code verification checks numerical implementation. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **uncertainty and sensitivity**.\n\nAn independent second approach might use a global equilibrium relation, a limiting case, an energy balance or a laboratory reading. It should not merely repeat the same arithmetic with extra decimal places.\n\n## Worked example and interpretation\n\n**Situation:** The height of a rectangular beam has a +2% change, with width fixed.\n\n**Equation:** `I_new/I_old=(1.02)^3`.\n\n**Reference answer:** **1.061208, a 6.12% increase**.\n\nReproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.\n\n**Engineering relevance:** Tolerance prioritization can focus on the dimensions with strongest sensitivity. Real use requires verified component-specific inputs; this example is not a certified working load.\n\n## Diagnosing a false conclusion\n\n**Common error:** Assuming a 2% depth change produces only a 2% change in bending stiffness.\n\nSafety factors do not cure a mistaken model, incorrectly placed support, unnoticed crack or unrealistic input. Start by verifying the load path and the chosen failure mode. For verification, calibration and extrapolation, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.\n\n## Exercises and answer criteria\n\n**1. Reconstruct.** Draw the section, mark all inputs and reproduce **1.061208, a 6.12% increase**, including units.\n\n*Answer guidance:* Use `I_new/I_old=(1.02)^3` with correct dimensions. Confirm the sign and the physical meaning of the quantity.\n\n**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.\n\n*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.\n\n**3. Diagnose.** Explain why this error matters: *assuming a 2% depth change produces only a 2% change in bending stiffness.* Propose a measurement or alternate equation that exposes it.\n\n*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.\n\n## Transfer to a real engineering study\n\nDesign the validation case before tuning material inputs, and preserve raw measured data separately from synthetic examples. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.\n",
          "simulations": []
        },
        {
          "secNumber": "8.4",
          "heading": "element mesh convergence",
          "content": "# Unit 8, Lesson 4 \u2014 Finite-element mesh convergence\n\n**Learning target.** Develop experiments, instrumentation and numerical checks; combine strength, stiffness, uncertainty and verification in engineering decisions. Explain the terms of `relative_change=(2.2\u22122.0)/2.2`, reconstruct the teaching example and identify one condition where the relation must be modified.\n\n## Physical model\n\nFinite-element answers are numerical approximations to a specified boundary-value model. Mesh refinement tests whether the discrete approximation stabilizes for a selected quantity, but sharp corners can create mathematical singularities whose peak stresses do not converge. A local displacement and an averaged reaction are often better convergence checks than the single largest nodal stress. Compare to at least one analytical benchmark.\n\nThe word \u201cstrength\u201d is not interchangeable with \u201cstiffness.\u201d Strength concerns exceeding a material or structural limit; stiffness concerns the load-to-deformation relation. Stability and damage mechanisms introduce further limits, which require their own data and assumptions.\n\n**Context:** A scalar displacement estimate changes from 2.0 to 2.2 mm after refinement. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.\n\n## Governing relationship and assumptions\n\n**Teaching relation:** `relative_change=(2.2\u22122.0)/2.2`.\n\nAn accurate fit on one loading case may conceal incorrect boundary conditions. Experimental validation asks whether a model predicts untrained measurements, whereas code verification checks numerical implementation. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **finite-element mesh convergence**.\n\nA true engineering calculation should be independently reproducible from the drawing and a concise input table. Another reader needs to know the sign convention, material assumptions, geometry, force units and exactly which cross-section or point is analyzed.\n\n## Worked example and interpretation\n\n**Situation:** A scalar displacement estimate changes from 2.0 to 2.2 mm after refinement.\n\n**Equation:** `relative_change=(2.2\u22122.0)/2.2`.\n\n**Reference answer:** **9.09% relative coarse-to-fine change**.\n\nReproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.\n\n**Engineering relevance:** Verification and experimental validation must remain separate activities. Real use requires verified component-specific inputs; this example is not a certified working load.\n\n## Diagnosing a false conclusion\n\n**Common error:** Interpreting numerical convergence as proof that physical supports and loads were modeled correctly.\n\nFailure-mode checks are not independent when the same hidden parameter drives all of them. A poor thickness measurement can bias area, area moment and nominal stress together; correlated uncertainties should be handled explicitly. For verification, calibration and extrapolation, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.\n\n## Exercises and answer criteria\n\n**1. Reconstruct.** Draw the section, mark all inputs and reproduce **9.09% relative coarse-to-fine change**, including units.\n\n*Answer guidance:* Use `relative_change=(2.2\u22122.0)/2.2` with correct dimensions. Confirm the sign and the physical meaning of the quantity.\n\n**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.\n\n*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.\n\n**3. Diagnose.** Explain why this error matters: *interpreting numerical convergence as proof that physical supports and loads were modeled correctly.* Propose a measurement or alternate equation that exposes it.\n\n*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.\n\n## Transfer to a real engineering study\n\nDesign the validation case before tuning material inputs, and preserve raw measured data separately from synthetic examples. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.\n",
          "simulations": []
        },
        {
          "secNumber": "8.5",
          "heading": "Integrated member design review",
          "content": "# Unit 8, Lesson 5 \u2014 Integrated member design review\n\n**Learning target.** Develop experiments, instrumentation and numerical checks; combine strength, stiffness, uncertainty and verification in engineering decisions. Explain the terms of `utilization=stress/allowable`, reconstruct the teaching example and identify one condition where the relation must be modified.\n\n## Physical model\n\nA plausible solid-mechanics decision checks loading, internal actions, constitutive law, peak stress, displacement, stability, fatigue and manufacturing tolerances. If an input is based on a specification rather than a measurement, identify it as assumed. Choose a concept that is safe under credible load cases and that can be produced and inspected economically, but do not infer formal compliance from classroom tools.\n\nFor a real joint or machine, the ideal solution is a starting hypothesis. Surface condition, machining tolerances, alignment, residual stress, temperature and spectrum of operating loads can dominate local behavior. Identify a feasible experiment that might falsify the calculation.\n\n**Context:** A member has estimated service stress 60 MPa and stated classroom allowable 120 MPa. Sketch the loaded section and mark any strain, displacement or support conditions. Define the reference state.\n\n## Governing relationship and assumptions\n\n**Teaching relation:** `utilization=stress/allowable`.\n\nAn accurate fit on one loading case may conceal incorrect boundary conditions. Experimental validation asks whether a model predicts untrained measurements, whereas code verification checks numerical implementation. Identify the quantity, units, sign convention and operating domain. Specify what would invalidate the simplified model of **integrated member design review**.\n\nChecking the dimensions of each term is necessary but not sufficient. An equation may carry the right SI units while using the wrong load boundary, neutral axis, shear area, material condition, or ideal support type.\n\n## Worked example and interpretation\n\n**Situation:** A member has estimated service stress 60 MPa and stated classroom allowable 120 MPa.\n\n**Equation:** `utilization=stress/allowable`.\n\n**Reference answer:** **0.50 for this one screening criterion**.\n\nReproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path.\n\n**Engineering relevance:** A design-review matrix records unresolved risks and evidence owners. Real use requires verified component-specific inputs; this example is not a certified working load.\n\n## Diagnosing a false conclusion\n\n**Common error:** Treating a single stress utilization as proof against buckling, fatigue and fracture.\n\nDo not turn an average calculation into a guarantee of peak stress at holes, shoulders, welds, contact points or cracks. The stress field can be strongly heterogeneous even if force equilibrium is satisfied. For verification, calibration and extrapolation, state whether ignoring the nonideal behavior could overpredict capacity or underpredict demand.\n\n## Exercises and answer criteria\n\n**1. Reconstruct.** Draw the section, mark all inputs and reproduce **0.50 for this one screening criterion**, including units.\n\n*Answer guidance:* Use `utilization=stress/allowable` with correct dimensions. Confirm the sign and the physical meaning of the quantity.\n\n**2. Sensitivity.** Change one meaningful input by 10% and recompute the response after predicting its direction.\n\n*Answer guidance:* Use the input exponent or functional dependence. If geometry changes the load path, derive a new model.\n\n**3. Diagnose.** Explain why this error matters: *treating a single stress utilization as proof against buckling, fatigue and fracture.* Propose a measurement or alternate equation that exposes it.\n\n*Answer guidance:* Identify the wrong assumption and a test independent of the original calculation.\n\n## Transfer to a real engineering study\n\nDesign the validation case before tuning material inputs, and preserve raw measured data separately from synthetic examples. Document inputs, response, uncertainty and one falsifiable test. For safety-critical applications, obtain independent professional review and relevant standards.\n",
          "simulations": []
        }
      ],
      "problems": [
        {
          "id": "MOS-U8-P1",
          "title": "Tensile test and offset yield",
          "question": "**Situation:** An initial linear segment changes stress by 100 MPa over strain change 0.0005.",
          "steps": [
            {
              "explanation": "**Equation:** `E=\u0394sigma/\u0394epsilon`."
            },
            {
              "explanation": "**Reference answer:** **200 GPa initial tangent estimate**."
            },
            {
              "explanation": "Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path."
            },
            {
              "explanation": "**Engineering relevance:** Test reports should identify specimen standard and uncertainty. Real use requires verified component-specific inputs; this example is not a certified working load."
            }
          ],
          "finalAnswer": "**Engineering relevance:** Test reports should identify specimen standard and uncertainty. Real use requires verified component-specific inputs; this example is not a certified working load."
        },
        {
          "id": "MOS-U8-P2",
          "title": "Strain gauge conversion",
          "question": "**Situation:** A gauge of GF=2.1 experiences longitudinal strain 600 microstrain.",
          "steps": [
            {
              "explanation": "**Equation:** `\u0394R/R=GF epsilon`."
            },
            {
              "explanation": "**Reference answer:** **0.00126 = 0.126%**."
            },
            {
              "explanation": "Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path."
            },
            {
              "explanation": "**Engineering relevance:** Strain gauges validate local model predictions when coordinate alignment is known. Real use requires verified component-specific inputs; this example is not a certified working load."
            }
          ],
          "finalAnswer": "**Engineering relevance:** Strain gauges validate local model predictions when coordinate alignment is known. Real use requires verified component-specific inputs; this example is not a certified working load."
        },
        {
          "id": "MOS-U8-P3",
          "title": "Uncertainty and sensitivity",
          "question": "**Situation:** The height of a rectangular beam has a +2% change, with width fixed.",
          "steps": [
            {
              "explanation": "**Equation:** `I_new/I_old=(1.02)^3`."
            },
            {
              "explanation": "**Reference answer:** **1.061208, a 6.12% increase**."
            },
            {
              "explanation": "Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path."
            },
            {
              "explanation": "**Engineering relevance:** Tolerance prioritization can focus on the dimensions with strongest sensitivity. Real use requires verified component-specific inputs; this example is not a certified working load."
            }
          ],
          "finalAnswer": "**Engineering relevance:** Tolerance prioritization can focus on the dimensions with strongest sensitivity. Real use requires verified component-specific inputs; this example is not a certified working load."
        },
        {
          "id": "MOS-U8-P4",
          "title": "element mesh convergence",
          "question": "**Situation:** A scalar displacement estimate changes from 2.0 to 2.2 mm after refinement.",
          "steps": [
            {
              "explanation": "**Equation:** `relative_change=(2.2\u22122.0)/2.2`."
            },
            {
              "explanation": "**Reference answer:** **9.09% relative coarse-to-fine change**."
            },
            {
              "explanation": "Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path."
            },
            {
              "explanation": "**Engineering relevance:** Verification and experimental validation must remain separate activities. Real use requires verified component-specific inputs; this example is not a certified working load."
            }
          ],
          "finalAnswer": "**Engineering relevance:** Verification and experimental validation must remain separate activities. Real use requires verified component-specific inputs; this example is not a certified working load."
        },
        {
          "id": "MOS-U8-P5",
          "title": "Integrated member design review",
          "question": "**Situation:** A member has estimated service stress 60 MPa and stated classroom allowable 120 MPa.",
          "steps": [
            {
              "explanation": "**Equation:** `utilization=stress/allowable`."
            },
            {
              "explanation": "**Reference answer:** **0.50 for this one screening criterion**."
            },
            {
              "explanation": "Reproduce the reference with converted SI units and appropriate rounding. First estimate its order of magnitude and check whether it is consistent with the physical load path."
            },
            {
              "explanation": "**Engineering relevance:** A design-review matrix records unresolved risks and evidence owners. Real use requires verified component-specific inputs; this example is not a certified working load."
            }
          ],
          "finalAnswer": "**Engineering relevance:** A design-review matrix records unresolved risks and evidence owners. Real use requires verified component-specific inputs; this example is not a certified working load."
        }
      ],
      "simulations": [
        "mechanics-of-solids-sim-8"
      ]
    }
  ]
};
