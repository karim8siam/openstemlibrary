/* OpenSTEM Course Data: Robotics and Automation (ROB) */
var COURSE_DATA = {
  "code": "ROB",
  "title": "Robotics and Automation",
  "subtitle": "Spatial Transformations, Forward/Inverse Kinematics, Jacobians, Dynamics, Path Planning & Industrial Cells",
  "units": [
    {
      "number": 1,
      "unitNumber": 1,
      "title": "Robot Architecture, Workcells and Requirements",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Robot Architecture, Workcells and Requirements.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Robot Architecture, Workcells and Requirements.",
      "sections": [
        {
          "id": "sec-1-1",
          "title": "Robot classes and degrees of freedom",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 1: Robot Architecture, Workcells and Requirements.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.",
          "content": "<p>**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 1: Robot Architecture, Workcells and Requirements.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.</p>"
        },
        {
          "id": "sec-1-2",
          "title": "Task specification and measurable throughput",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 1: Robot Architecture, Workcells and Requirements.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.",
          "content": "<p>**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 1: Robot Architecture, Workcells and Requirements.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.</p>"
        },
        {
          "id": "sec-1-3",
          "title": "Coordinate-frame conventions",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 1: Robot Architecture, Workcells and Requirements.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.",
          "content": "<p>**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 1: Robot Architecture, Workcells and Requirements.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.</p>"
        },
        {
          "id": "sec-1-4",
          "title": "Automation cell interfaces",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 1: Robot Architecture, Workcells and Requirements.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.",
          "content": "<p>**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 1: Robot Architecture, Workcells and Requirements.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.</p>"
        },
        {
          "id": "sec-1-5",
          "title": "Hazard identification and protective design",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 1: Robot Architecture, Workcells and Requirements.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.",
          "content": "<p>**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 1: Robot Architecture, Workcells and Requirements.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-robotics-and-automation-1-1",
          "title": "Calculation & Verification: Robot classes and degrees of freedom",
          "unit": 1,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Robot classes and degrees of freedom** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A six-revolute-joint arm normally needs six independent coordinates to state its nominal configuration, although joint limits and singularities constrain useful motion. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Discretization audit.** Choose a simulation step that resolves the fastest physical phenomenon of interest. Check convergence with a smaller step and confirm that numerical artifacts do not explain apparent stability or contact behavior. Sampling rates must exceed the bandwidth of the phenomena they are claimed to detect. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
        },
        {
          "id": "prob-robotics-and-automation-1-2",
          "title": "Calculation & Verification: Task specification and measurable throughput",
          "unit": 1,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Task specification and measurable throughput** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>At a 4.5 s full handling cycle and 0.85 productive fraction, nominal capacity is 680 successful cycles/hour before reject handling. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Uncertainty audit.** Differentiate precision from accuracy: repeated values near one another may share a systematic offset. Use replicated trials and a calibration reference, and consider correlations when combining uncertainties. An error bound must be linked to a defined operating range. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
        },
        {
          "id": "prob-robotics-and-automation-1-3",
          "title": "Calculation & Verification: Coordinate-frame conventions",
          "unit": 1,
          "question": "<p><strong>Problem Statement:</strong> A tool point 0.10 m along a base-aligned axis from a base origin at x=0.70 m has world x=0.80 m; a rotated tool requires the full transform. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Traceable Verification audit.** Record firmware or model version, sensor calibration, test fixture revision and all rejected trials. Set acceptance thresholds before viewing the final traces. If a physical trial cannot be carried out safely, use simulation only and write the missing validation item explicitly. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
        },
        {
          "id": "prob-robotics-and-automation-1-4",
          "title": "Calculation & Verification: Automation cell interfaces",
          "unit": 1,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Automation cell interfaces** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>Segments of 0.10, 1.20, 0.25, 1.05 and 0.40 s yield 3.00 s nominal, excluding overlap and recovery. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Dimensional Balance audit.** Perform a units check by substituting SI base units and showing both sides match. For angles, state that trigonometric functions expect radians unless explicitly converted. For probabilities, check output within [0,1], and for lengths or times reject negative values when the model defines only positive quantities. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
        },
        {
          "id": "prob-robotics-and-automation-1-5",
          "title": "Calculation & Verification: Hazard identification and protective design",
          "unit": 1,
          "question": "<p><strong>Problem Statement:</strong> A 3 kg moving payload at 1.2 m/s has 2.16 J translational kinetic energy, excluding manipulator links. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Boundary Cases audit.** Check a zero-input limit, a typical operating point and a maximum planned input. Where derivatives exist, estimate local sensitivity to a 5% change. If the result changes sharply, prioritize a measurement of the sensitive parameter rather than increasing numerical precision elsewhere. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
        }
      ]
    },
    {
      "number": 2,
      "unitNumber": 2,
      "title": "Manipulators and Robot Kinematics",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Manipulators and Robot Kinematics.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Manipulators and Robot Kinematics.",
      "sections": [
        {
          "id": "sec-2-1",
          "title": "Homogeneous transformations and chains",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 2: Manipulators and Robot Kinematics.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.",
          "content": "<p>**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 2: Manipulators and Robot Kinematics.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.</p>"
        },
        {
          "id": "sec-2-2",
          "title": "Two-link forward kinematics",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 2: Manipulators and Robot Kinematics.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.",
          "content": "<p>**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 2: Manipulators and Robot Kinematics.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.</p>"
        },
        {
          "id": "sec-2-3",
          "title": "Inverse kinematics and reachability",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 2: Manipulators and Robot Kinematics.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.",
          "content": "<p>**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 2: Manipulators and Robot Kinematics.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.</p>"
        },
        {
          "id": "sec-2-4",
          "title": "Jacobians and velocity transmission",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 2: Manipulators and Robot Kinematics.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.",
          "content": "<p>**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 2: Manipulators and Robot Kinematics.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.</p>"
        },
        {
          "id": "sec-2-5",
          "title": "Calibration, payload and workspace uncertainty",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 2: Manipulators and Robot Kinematics.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.",
          "content": "<p>**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 2: Manipulators and Robot Kinematics.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-robotics-and-automation-2-1",
          "title": "Calculation & Verification: Homogeneous transformations and chains",
          "unit": 2,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Homogeneous transformations and chains** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>Two aligned 0.30 m and 0.20 m links at zero joint angle place a planar tip 0.50 m from the first joint center. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Uncertainty audit.** Differentiate precision from accuracy: repeated values near one another may share a systematic offset. Use replicated trials and a calibration reference, and consider correlations when combining uncertainties. An error bound must be linked to a defined operating range. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
        },
        {
          "id": "prob-robotics-and-automation-2-2",
          "title": "Calculation & Verification: Two-link forward kinematics",
          "unit": 2,
          "question": "<p><strong>Problem Statement:</strong> For L1=0.30 m, L2=0.20 m, q1=0\u00b0, q2=90\u00b0, the tip is at (0.30,0.20) m. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Traceable Verification audit.** Record firmware or model version, sensor calibration, test fixture revision and all rejected trials. Set acceptance thresholds before viewing the final traces. If a physical trial cannot be carried out safely, use simulation only and write the missing validation item explicitly. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
        },
        {
          "id": "prob-robotics-and-automation-2-3",
          "title": "Calculation & Verification: Inverse kinematics and reachability",
          "unit": 2,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Inverse kinematics and reachability** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For L1=0.30 m, L2=0.20 m and tip distance 0.40 m, cos(q2)=0.25, giving elbow angles about \u00b175.52\u00b0. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Dimensional Balance audit.** Perform a units check by substituting SI base units and showing both sides match. For angles, state that trigonometric functions expect radians unless explicitly converted. For probabilities, check output within [0,1], and for lengths or times reject negative values when the model defines only positive quantities. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
        },
        {
          "id": "prob-robotics-and-automation-2-4",
          "title": "Calculation & Verification: Jacobians and velocity transmission",
          "unit": 2,
          "question": "<p><strong>Problem Statement:</strong> At L1=0.30 m, L2=0.20 m, q2=90\u00b0, the determinant magnitude is 0.060 m\u00b2, while at q2=0\u00b0 it is zero. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Boundary Cases audit.** Check a zero-input limit, a typical operating point and a maximum planned input. Where derivatives exist, estimate local sensitivity to a 5% change. If the result changes sharply, prioritize a measurement of the sensitive parameter rather than increasing numerical precision elsewhere. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
        },
        {
          "id": "prob-robotics-and-automation-2-5",
          "title": "Calculation & Verification: Calibration, payload and workspace uncertainty",
          "unit": 2,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Calibration, payload and workspace uncertainty** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>With independent contributions 0.4 mm and 0.3 mm to x error, root-sum-square uncertainty is 0.5 mm under the independence approximation. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Discretization audit.** Choose a simulation step that resolves the fastest physical phenomenon of interest. Check convergence with a smaller step and confirm that numerical artifacts do not explain apparent stability or contact behavior. Sampling rates must exceed the bandwidth of the phenomena they are claimed to detect. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
        }
      ]
    },
    {
      "number": 3,
      "unitNumber": 3,
      "title": "Robot Dynamics, Actuation and Contacts",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Robot Dynamics, Actuation and Contacts.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Robot Dynamics, Actuation and Contacts.",
      "sections": [
        {
          "id": "sec-3-1",
          "title": "Newton\u2013Euler balance for links",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 3: Robot Dynamics, Actuation and Contacts.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.",
          "content": "<p>**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 3: Robot Dynamics, Actuation and Contacts.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.</p>"
        },
        {
          "id": "sec-3-2",
          "title": "Lagrange formulation and energy",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 3: Robot Dynamics, Actuation and Contacts.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.",
          "content": "<p>**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 3: Robot Dynamics, Actuation and Contacts.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.</p>"
        },
        {
          "id": "sec-3-3",
          "title": "Motor and gear selection",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 3: Robot Dynamics, Actuation and Contacts.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.",
          "content": "<p>**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 3: Robot Dynamics, Actuation and Contacts.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.</p>"
        },
        {
          "id": "sec-3-4",
          "title": "Grasp force, friction and object variability",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 3: Robot Dynamics, Actuation and Contacts.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.",
          "content": "<p>**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 3: Robot Dynamics, Actuation and Contacts.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.</p>"
        },
        {
          "id": "sec-3-5",
          "title": "Collision impulse and compliant contact",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 3: Robot Dynamics, Actuation and Contacts.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.",
          "content": "<p>**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 3: Robot Dynamics, Actuation and Contacts.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-robotics-and-automation-3-1",
          "title": "Calculation & Verification: Newton\u2013Euler balance for links",
          "unit": 3,
          "question": "<p><strong>Problem Statement:</strong> With I=0.060 kg\u00b7m\u00b2 and angular acceleration 4 rad/s\u00b2, an ideal isolated axis needs 0.24 N\u00b7m acceleration torque before gravity and friction. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Traceable Verification audit.** Record firmware or model version, sensor calibration, test fixture revision and all rejected trials. Set acceptance thresholds before viewing the final traces. If a physical trial cannot be carried out safely, use simulation only and write the missing validation item explicitly. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
        },
        {
          "id": "prob-robotics-and-automation-3-2",
          "title": "Calculation & Verification: Lagrange formulation and energy",
          "unit": 3,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Lagrange formulation and energy** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For a single rigid link with I=0.08 kg\u00b7m\u00b2, angular acceleration 2 rad/s\u00b2 gives 0.16 N\u00b7m inertia torque in the gravity-free idealization. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Dimensional Balance audit.** Perform a units check by substituting SI base units and showing both sides match. For angles, state that trigonometric functions expect radians unless explicitly converted. For probabilities, check output within [0,1], and for lengths or times reject negative values when the model defines only positive quantities. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
        },
        {
          "id": "prob-robotics-and-automation-3-3",
          "title": "Calculation & Verification: Motor and gear selection",
          "unit": 3,
          "question": "<p><strong>Problem Statement:</strong> For gear ratio 12, efficiency 0.80 and motor torque 0.15 N\u00b7m, output torque is 1.44 N\u00b7m under the assumed point-efficiency. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Boundary Cases audit.** Check a zero-input limit, a typical operating point and a maximum planned input. Where derivatives exist, estimate local sensitivity to a 5% change. If the result changes sharply, prioritize a measurement of the sensitive parameter rather than increasing numerical precision elsewhere. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
        },
        {
          "id": "prob-robotics-and-automation-3-4",
          "title": "Calculation & Verification: Grasp force, friction and object variability",
          "unit": 3,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Grasp force, friction and object variability** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For m=1 kg, \u03bc=0.50 and upward acceleration 1 m/s\u00b2, each jaw needs at least 10.81 N in the ideal symmetric model. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Discretization audit.** Choose a simulation step that resolves the fastest physical phenomenon of interest. Check convergence with a smaller step and confirm that numerical artifacts do not explain apparent stability or contact behavior. Sampling rates must exceed the bandwidth of the phenomena they are claimed to detect. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
        },
        {
          "id": "prob-robotics-and-automation-3-5",
          "title": "Calculation & Verification: Collision impulse and compliant contact",
          "unit": 3,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Collision impulse and compliant contact** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A 2 kg object stopped from 0.5 m/s experiences 1 N\u00b7s magnitude impulse regardless of how quickly it is stopped. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Uncertainty audit.** Differentiate precision from accuracy: repeated values near one another may share a systematic offset. Use replicated trials and a calibration reference, and consider correlations when combining uncertainties. An error bound must be linked to a defined operating range. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
        }
      ]
    },
    {
      "number": 4,
      "unitNumber": 4,
      "title": "Motion Planning and Trajectory Generation",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Motion Planning and Trajectory Generation.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Motion Planning and Trajectory Generation.",
      "sections": [
        {
          "id": "sec-4-1",
          "title": "Path versus trajectory",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 4: Motion Planning and Trajectory Generation.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.",
          "content": "<p>**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 4: Motion Planning and Trajectory Generation.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.</p>"
        },
        {
          "id": "sec-4-2",
          "title": "Trapezoidal and triangular velocity profiles",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 4: Motion Planning and Trajectory Generation.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.",
          "content": "<p>**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 4: Motion Planning and Trajectory Generation.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.</p>"
        },
        {
          "id": "sec-4-3",
          "title": "Jerk-limited motion profiles",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 4: Motion Planning and Trajectory Generation.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.",
          "content": "<p>**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 4: Motion Planning and Trajectory Generation.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.</p>"
        },
        {
          "id": "sec-4-4",
          "title": "Joint-space and Cartesian interpolation",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 4: Motion Planning and Trajectory Generation.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.",
          "content": "<p>**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 4: Motion Planning and Trajectory Generation.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.</p>"
        },
        {
          "id": "sec-4-5",
          "title": "Collision checking and replanning",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 4: Motion Planning and Trajectory Generation.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.",
          "content": "<p>**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 4: Motion Planning and Trajectory Generation.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-robotics-and-automation-4-1",
          "title": "Calculation & Verification: Path versus trajectory",
          "unit": 4,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Path versus trajectory** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A 0.60 m path traversed in 1.5 s has average path speed 0.40 m/s, not necessarily constant Cartesian velocity. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Dimensional Balance audit.** Perform a units check by substituting SI base units and showing both sides match. For angles, state that trigonometric functions expect radians unless explicitly converted. For probabilities, check output within [0,1], and for lengths or times reject negative values when the model defines only positive quantities. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
        },
        {
          "id": "prob-robotics-and-automation-4-2",
          "title": "Calculation & Verification: Trapezoidal and triangular velocity profiles",
          "unit": 4,
          "question": "<p><strong>Problem Statement:</strong> For d=0.20 m, a=1 m/s\u00b2 and vmax=1 m/s, the triangular profile takes about 0.894 s. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Boundary Cases audit.** Check a zero-input limit, a typical operating point and a maximum planned input. Where derivatives exist, estimate local sensitivity to a 5% change. If the result changes sharply, prioritize a measurement of the sensitive parameter rather than increasing numerical precision elsewhere. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
        },
        {
          "id": "prob-robotics-and-automation-4-3",
          "title": "Calculation & Verification: Jerk-limited motion profiles",
          "unit": 4,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Jerk-limited motion profiles** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>Changing acceleration from 0 to 2 m/s\u00b2 over 0.20 s gives mean jerk magnitude 10 m/s\u00b3 under a linear ramp. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Discretization audit.** Choose a simulation step that resolves the fastest physical phenomenon of interest. Check convergence with a smaller step and confirm that numerical artifacts do not explain apparent stability or contact behavior. Sampling rates must exceed the bandwidth of the phenomena they are claimed to detect. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
        },
        {
          "id": "prob-robotics-and-automation-4-4",
          "title": "Calculation & Verification: Joint-space and Cartesian interpolation",
          "unit": 4,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Joint-space and Cartesian interpolation** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>At s=0.25 between 20\u00b0 and 60\u00b0, a single interpolated joint is 30\u00b0; intermediate tool positions depend on all other joints. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Uncertainty audit.** Differentiate precision from accuracy: repeated values near one another may share a systematic offset. Use replicated trials and a calibration reference, and consider correlations when combining uncertainties. An error bound must be linked to a defined operating range. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
        },
        {
          "id": "prob-robotics-and-automation-4-5",
          "title": "Calculation & Verification: Collision checking and replanning",
          "unit": 4,
          "question": "<p><strong>Problem Statement:</strong> With predicted clearance 15 mm and combined safety margin 7 mm, the remaining modeled clearance is 8 mm, subject to calibration validity. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Traceable Verification audit.** Record firmware or model version, sensor calibration, test fixture revision and all rejected trials. Set acceptance thresholds before viewing the final traces. If a physical trial cannot be carried out safely, use simulation only and write the missing validation item explicitly. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
        }
      ]
    },
    {
      "number": 5,
      "unitNumber": 5,
      "title": "Mobile Robotics, Localization and Mapping",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Mobile Robotics, Localization and Mapping.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Mobile Robotics, Localization and Mapping.",
      "sections": [
        {
          "id": "sec-5-1",
          "title": "Differential-drive kinematics",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 5: Mobile Robotics, Localization and Mapping.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.",
          "content": "<p>**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 5: Mobile Robotics, Localization and Mapping.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.</p>"
        },
        {
          "id": "sec-5-2",
          "title": "Wheel odometry and pose integration",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 5: Mobile Robotics, Localization and Mapping.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.",
          "content": "<p>**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 5: Mobile Robotics, Localization and Mapping.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.</p>"
        },
        {
          "id": "sec-5-3",
          "title": "Inertial and visual sensor fusion",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 5: Mobile Robotics, Localization and Mapping.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.",
          "content": "<p>**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 5: Mobile Robotics, Localization and Mapping.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.</p>"
        },
        {
          "id": "sec-5-4",
          "title": "Occupancy grids and mapping uncertainty",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 5: Mobile Robotics, Localization and Mapping.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.",
          "content": "<p>**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 5: Mobile Robotics, Localization and Mapping.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.</p>"
        },
        {
          "id": "sec-5-5",
          "title": "Localization failure and recovery",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 5: Mobile Robotics, Localization and Mapping.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.",
          "content": "<p>**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 5: Mobile Robotics, Localization and Mapping.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-robotics-and-automation-5-1",
          "title": "Calculation & Verification: Differential-drive kinematics",
          "unit": 5,
          "question": "<p><strong>Problem Statement:</strong> For vR=0.60 m/s, vL=0.20 m/s and track b=0.50 m, body speed is 0.40 m/s and yaw rate 0.80 rad/s. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Boundary Cases audit.** Check a zero-input limit, a typical operating point and a maximum planned input. Where derivatives exist, estimate local sensitivity to a 5% change. If the result changes sharply, prioritize a measurement of the sensitive parameter rather than increasing numerical precision elsewhere. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
        },
        {
          "id": "prob-robotics-and-automation-5-2",
          "title": "Calculation & Verification: Wheel odometry and pose integration",
          "unit": 5,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Wheel odometry and pose integration** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>Left travel 0.40 m and right travel 0.50 m imply nominal center travel 0.45 m between readings. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Discretization audit.** Choose a simulation step that resolves the fastest physical phenomenon of interest. Check convergence with a smaller step and confirm that numerical artifacts do not explain apparent stability or contact behavior. Sampling rates must exceed the bandwidth of the phenomena they are claimed to detect. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
        },
        {
          "id": "prob-robotics-and-automation-5-3",
          "title": "Calculation & Verification: Inertial and visual sensor fusion",
          "unit": 5,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Inertial and visual sensor fusion** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A residual gyro bias 0.1\u00b0/s accumulates about 6\u00b0 heading error over one minute if uncorrected. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Uncertainty audit.** Differentiate precision from accuracy: repeated values near one another may share a systematic offset. Use replicated trials and a calibration reference, and consider correlations when combining uncertainties. An error bound must be linked to a defined operating range. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
        },
        {
          "id": "prob-robotics-and-automation-5-4",
          "title": "Calculation & Verification: Occupancy grids and mapping uncertainty",
          "unit": 5,
          "question": "<p><strong>Problem Statement:</strong> With prior occupancy 0.50, detection probability 0.80 and false-positive rate 0.20, a positive report yields posterior occupancy 0.80. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Traceable Verification audit.** Record firmware or model version, sensor calibration, test fixture revision and all rejected trials. Set acceptance thresholds before viewing the final traces. If a physical trial cannot be carried out safely, use simulation only and write the missing validation item explicitly. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
        },
        {
          "id": "prob-robotics-and-automation-5-5",
          "title": "Calculation & Verification: Localization failure and recovery",
          "unit": 5,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Localization failure and recovery** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For planar errors 0.12 m and 0.05 m, Euclidean position error is 0.13 m. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Dimensional Balance audit.** Perform a units check by substituting SI base units and showing both sides match. For angles, state that trigonometric functions expect radians unless explicitly converted. For probabilities, check output within [0,1], and for lengths or times reject negative values when the model defines only positive quantities. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
        }
      ]
    },
    {
      "number": 6,
      "unitNumber": 6,
      "title": "Perception, Navigation and Decision-Making",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Perception, Navigation and Decision-Making.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Perception, Navigation and Decision-Making.",
      "sections": [
        {
          "id": "sec-6-1",
          "title": "Cameras, depth sensors and calibration",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 6: Perception, Navigation and Decision-Making.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.",
          "content": "<p>**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 6: Perception, Navigation and Decision-Making.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.</p>"
        },
        {
          "id": "sec-6-2",
          "title": "Detection confidence and classification",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 6: Perception, Navigation and Decision-Making.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.",
          "content": "<p>**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 6: Perception, Navigation and Decision-Making.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.</p>"
        },
        {
          "id": "sec-6-3",
          "title": "Graph and grid path planning",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 6: Perception, Navigation and Decision-Making.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.",
          "content": "<p>**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 6: Perception, Navigation and Decision-Making.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.</p>"
        },
        {
          "id": "sec-6-4",
          "title": "Reactive obstacle avoidance",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 6: Perception, Navigation and Decision-Making.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.",
          "content": "<p>**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 6: Perception, Navigation and Decision-Making.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.</p>"
        },
        {
          "id": "sec-6-5",
          "title": "Task planning and finite-state execution",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 6: Perception, Navigation and Decision-Making.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.",
          "content": "<p>**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 6: Perception, Navigation and Decision-Making.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-robotics-and-automation-6-1",
          "title": "Calculation & Verification: Cameras, depth sensors and calibration",
          "unit": 6,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Cameras, depth sensors and calibration** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For f=500 pixel, baseline=0.10 m and disparity=50 pixel, depth is 1.0 m in the ideal model. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Discretization audit.** Choose a simulation step that resolves the fastest physical phenomenon of interest. Check convergence with a smaller step and confirm that numerical artifacts do not explain apparent stability or contact behavior. Sampling rates must exceed the bandwidth of the phenomena they are claimed to detect. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
        },
        {
          "id": "prob-robotics-and-automation-6-2",
          "title": "Calculation & Verification: Detection confidence and classification",
          "unit": 6,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Detection confidence and classification** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>With 80 true positives and 20 false positives, sample precision is 0.80; this does not measure recall without false negatives. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Uncertainty audit.** Differentiate precision from accuracy: repeated values near one another may share a systematic offset. Use replicated trials and a calibration reference, and consider correlations when combining uncertainties. An error bound must be linked to a defined operating range. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
        },
        {
          "id": "prob-robotics-and-automation-6-3",
          "title": "Calculation & Verification: Graph and grid path planning",
          "unit": 6,
          "question": "<p><strong>Problem Statement:</strong> For relative cell offsets dx=4, dy=3, Manhattan lower bound is seven unit moves when diagonal actions are disallowed. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Traceable Verification audit.** Record firmware or model version, sensor calibration, test fixture revision and all rejected trials. Set acceptance thresholds before viewing the final traces. If a physical trial cannot be carried out safely, use simulation only and write the missing validation item explicitly. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
        },
        {
          "id": "prob-robotics-and-automation-6-4",
          "title": "Calculation & Verification: Reactive obstacle avoidance",
          "unit": 6,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Reactive obstacle avoidance** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>At speed 0.80 m/s, delay 0.10 s and deceleration 1.0 m/s\u00b2, ideal stop distance is 0.40 m before uncertainties. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Dimensional Balance audit.** Perform a units check by substituting SI base units and showing both sides match. For angles, state that trigonometric functions expect radians unless explicitly converted. For probabilities, check output within [0,1], and for lengths or times reject negative values when the model defines only positive quantities. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
        },
        {
          "id": "prob-robotics-and-automation-6-5",
          "title": "Calculation & Verification: Task planning and finite-state execution",
          "unit": 6,
          "question": "<p><strong>Problem Statement:</strong> With per-attempt success probability 0.80, expected attempts are 1.25 only if trials are independent and identical. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Boundary Cases audit.** Check a zero-input limit, a typical operating point and a maximum planned input. Where derivatives exist, estimate local sensitivity to a 5% change. If the result changes sharply, prioritize a measurement of the sensitive parameter rather than increasing numerical precision elsewhere. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
        }
      ]
    },
    {
      "number": 7,
      "unitNumber": 7,
      "title": "Industrial Automation, Integration and Reliability",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Industrial Automation, Integration and Reliability.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Industrial Automation, Integration and Reliability.",
      "sections": [
        {
          "id": "sec-7-1",
          "title": "PLC handshakes and interlocks",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 7: Industrial Automation, Integration and Reliability.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.",
          "content": "<p>**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 7: Industrial Automation, Integration and Reliability.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.</p>"
        },
        {
          "id": "sec-7-2",
          "title": "Cycle-time budgets and bottlenecks",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 7: Industrial Automation, Integration and Reliability.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.",
          "content": "<p>**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 7: Industrial Automation, Integration and Reliability.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.</p>"
        },
        {
          "id": "sec-7-3",
          "title": "Quality inspection and traceability",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 7: Industrial Automation, Integration and Reliability.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.",
          "content": "<p>**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 7: Industrial Automation, Integration and Reliability.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.</p>"
        },
        {
          "id": "sec-7-4",
          "title": "Reliability and preventive maintenance",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 7: Industrial Automation, Integration and Reliability.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.",
          "content": "<p>**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 7: Industrial Automation, Integration and Reliability.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.</p>"
        },
        {
          "id": "sec-7-5",
          "title": "Commissioning, acceptance and change control",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 7: Industrial Automation, Integration and Reliability.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.",
          "content": "<p>**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 7: Industrial Automation, Integration and Reliability.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-robotics-and-automation-7-1",
          "title": "Calculation & Verification: PLC handshakes and interlocks",
          "unit": 7,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **PLC handshakes and interlocks** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>Stages 0.3, 1.0, 0.4 and 0.8 s total 2.5 s if none can overlap. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Uncertainty audit.** Differentiate precision from accuracy: repeated values near one another may share a systematic offset. Use replicated trials and a calibration reference, and consider correlations when combining uncertainties. An error bound must be linked to a defined operating range. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
        },
        {
          "id": "prob-robotics-and-automation-7-2",
          "title": "Calculation & Verification: Cycle-time budgets and bottlenecks",
          "unit": 7,
          "question": "<p><strong>Problem Statement:</strong> For a 5 s bottleneck cycle and 90% uptime, expected steady nominal capacity is 648 units per hour before scrap. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Traceable Verification audit.** Record firmware or model version, sensor calibration, test fixture revision and all rejected trials. Set acceptance thresholds before viewing the final traces. If a physical trial cannot be carried out safely, use simulation only and write the missing validation item explicitly. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
        },
        {
          "id": "prob-robotics-and-automation-7-3",
          "title": "Calculation & Verification: Quality inspection and traceability",
          "unit": 7,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Quality inspection and traceability** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>If 960 of 1,000 inspected units pass, observed sample yield is 96%, without establishing the true defect rate. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Dimensional Balance audit.** Perform a units check by substituting SI base units and showing both sides match. For angles, state that trigonometric functions expect radians unless explicitly converted. For probabilities, check output within [0,1], and for lengths or times reject negative values when the model defines only positive quantities. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
        },
        {
          "id": "prob-robotics-and-automation-7-4",
          "title": "Calculation & Verification: Reliability and preventive maintenance",
          "unit": 7,
          "question": "<p><strong>Problem Statement:</strong> If lambda=0.0002 per hour, illustrative survival after 500 hours is exp(-0.1)\u22480.9048. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Boundary Cases audit.** Check a zero-input limit, a typical operating point and a maximum planned input. Where derivatives exist, estimate local sensitivity to a 5% change. If the result changes sharply, prioritize a measurement of the sensitive parameter rather than increasing numerical precision elsewhere. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
        },
        {
          "id": "prob-robotics-and-automation-7-5",
          "title": "Calculation & Verification: Commissioning, acceptance and change control",
          "unit": 7,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Commissioning, acceptance and change control** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>With 4 pick errors in 2,000 attempted cycles, observed error fraction is 0.002, not proof the true error rate is exactly 0.2%. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Discretization audit.** Choose a simulation step that resolves the fastest physical phenomenon of interest. Check convergence with a smaller step and confirm that numerical artifacts do not explain apparent stability or contact behavior. Sampling rates must exceed the bandwidth of the phenomena they are claimed to detect. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
        }
      ]
    },
    {
      "number": 8,
      "unitNumber": 8,
      "title": "Research Frontiers, Ethics and Capstone Design",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Research Frontiers, Ethics and Capstone Design.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Research Frontiers, Ethics and Capstone Design.",
      "sections": [
        {
          "id": "sec-8-1",
          "title": "Learning-based robot control and distribution shift",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 8: Research Frontiers, Ethics and Capstone Design.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.",
          "content": "<p>**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 8: Research Frontiers, Ethics and Capstone Design.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.</p>"
        },
        {
          "id": "sec-8-2",
          "title": "Digital twins and simulation-to-real transfer",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 8: Research Frontiers, Ethics and Capstone Design.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.",
          "content": "<p>**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 8: Research Frontiers, Ethics and Capstone Design.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.</p>"
        },
        {
          "id": "sec-8-3",
          "title": "Multi-robot coordination and scheduling",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 8: Research Frontiers, Ethics and Capstone Design.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.",
          "content": "<p>**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 8: Research Frontiers, Ethics and Capstone Design.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.</p>"
        },
        {
          "id": "sec-8-4",
          "title": "Automation cost and engineering trade-offs",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 8: Research Frontiers, Ethics and Capstone Design.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.",
          "content": "<p>**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 8: Research Frontiers, Ethics and Capstone Design.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.</p>"
        },
        {
          "id": "sec-8-5",
          "title": "Integrated capstone and reproducible evidence",
          "leadSummary": "**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 8: Research Frontiers, Ethics and Capstone Design.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.",
          "content": "<p>**OpenSTEM Mechanical Engineering \u00b7 Book 12: Robotics and Automation \u00b7 Unit 8: Research Frontiers, Ethics and Capstone Design.** Educational draft. All worked numbers are illustrative unless stated otherwise; do not use the calculations alone to certify a physical robot or protective system.</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-robotics-and-automation-8-1",
          "title": "Calculation & Verification: Learning-based robot control and distribution shift",
          "unit": 8,
          "question": "<p><strong>Problem Statement:</strong> A policy succeeding in 92 of 100 synthetic scenarios has observed simulation success 92%, with wide uncertainty and no hardware proof. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Traceable Verification audit.** Record firmware or model version, sensor calibration, test fixture revision and all rejected trials. Set acceptance thresholds before viewing the final traces. If a physical trial cannot be carried out safely, use simulation only and write the missing validation item explicitly. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
        },
        {
          "id": "prob-robotics-and-automation-8-2",
          "title": "Calculation & Verification: Digital twins and simulation-to-real transfer",
          "unit": 8,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Digital twins and simulation-to-real transfer** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>Predicted travel 0.50 m versus measured 0.47 m gives residual \u22120.03 m under the stated sign convention. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Dimensional Balance audit.** Perform a units check by substituting SI base units and showing both sides match. For angles, state that trigonometric functions expect radians unless explicitly converted. For probabilities, check output within [0,1], and for lengths or times reject negative values when the model defines only positive quantities. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
        },
        {
          "id": "prob-robotics-and-automation-8-3",
          "title": "Calculation & Verification: Multi-robot coordination and scheduling",
          "unit": 8,
          "question": "<p><strong>Problem Statement:</strong> Arrival rate 0.10 tasks/s with 6 s average service time implies nominal utilization 0.60 for one server in the simplified model. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Boundary Cases audit.** Check a zero-input limit, a typical operating point and a maximum planned input. Where derivatives exist, estimate local sensitivity to a 5% change. If the result changes sharply, prioritize a measurement of the sensitive parameter rather than increasing numerical precision elsewhere. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
        },
        {
          "id": "prob-robotics-and-automation-8-4",
          "title": "Calculation & Verification: Automation cost and engineering trade-offs",
          "unit": 8,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Automation cost and engineering trade-offs** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A hypothetical $90,000 installation saving $15,000 per year net has simple payback six years, before discounting and residual value. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Discretization audit.** Choose a simulation step that resolves the fastest physical phenomenon of interest. Check convergence with a smaller step and confirm that numerical artifacts do not explain apparent stability or contact behavior. Sampling rates must exceed the bandwidth of the phenomena they are claimed to detect. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
        },
        {
          "id": "prob-robotics-and-automation-8-5",
          "title": "Calculation & Verification: Integrated capstone and reproducible evidence",
          "unit": 8,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Integrated capstone and reproducible evidence** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A guarded demonstration with 420 successful units in 0.75 h yields 560 accepted units/h over that observed window, not guaranteed monthly capacity. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Uncertainty audit.** Differentiate precision from accuracy: repeated values near one another may share a systematic offset. Use replicated trials and a calibration reference, and consider correlations when combining uncertainties. An error bound must be linked to a defined operating range. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
        }
      ]
    }
  ],
  "problems": [
    {
      "id": "prob-robotics-and-automation-1-1",
      "title": "Calculation & Verification: Robot classes and degrees of freedom",
      "unit": 1,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Robot classes and degrees of freedom** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A six-revolute-joint arm normally needs six independent coordinates to state its nominal configuration, although joint limits and singularities constrain useful motion. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Discretization audit.** Choose a simulation step that resolves the fastest physical phenomenon of interest. Check convergence with a smaller step and confirm that numerical artifacts do not explain apparent stability or contact behavior. Sampling rates must exceed the bandwidth of the phenomena they are claimed to detect. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
    },
    {
      "id": "prob-robotics-and-automation-1-2",
      "title": "Calculation & Verification: Task specification and measurable throughput",
      "unit": 1,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Task specification and measurable throughput** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>At a 4.5 s full handling cycle and 0.85 productive fraction, nominal capacity is 680 successful cycles/hour before reject handling. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Uncertainty audit.** Differentiate precision from accuracy: repeated values near one another may share a systematic offset. Use replicated trials and a calibration reference, and consider correlations when combining uncertainties. An error bound must be linked to a defined operating range. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
    },
    {
      "id": "prob-robotics-and-automation-1-3",
      "title": "Calculation & Verification: Coordinate-frame conventions",
      "unit": 1,
      "question": "<p><strong>Problem Statement:</strong> A tool point 0.10 m along a base-aligned axis from a base origin at x=0.70 m has world x=0.80 m; a rotated tool requires the full transform. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Traceable Verification audit.** Record firmware or model version, sensor calibration, test fixture revision and all rejected trials. Set acceptance thresholds before viewing the final traces. If a physical trial cannot be carried out safely, use simulation only and write the missing validation item explicitly. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
    },
    {
      "id": "prob-robotics-and-automation-1-4",
      "title": "Calculation & Verification: Automation cell interfaces",
      "unit": 1,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Automation cell interfaces** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>Segments of 0.10, 1.20, 0.25, 1.05 and 0.40 s yield 3.00 s nominal, excluding overlap and recovery. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Dimensional Balance audit.** Perform a units check by substituting SI base units and showing both sides match. For angles, state that trigonometric functions expect radians unless explicitly converted. For probabilities, check output within [0,1], and for lengths or times reject negative values when the model defines only positive quantities. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
    },
    {
      "id": "prob-robotics-and-automation-1-5",
      "title": "Calculation & Verification: Hazard identification and protective design",
      "unit": 1,
      "question": "<p><strong>Problem Statement:</strong> A 3 kg moving payload at 1.2 m/s has 2.16 J translational kinetic energy, excluding manipulator links. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Boundary Cases audit.** Check a zero-input limit, a typical operating point and a maximum planned input. Where derivatives exist, estimate local sensitivity to a 5% change. If the result changes sharply, prioritize a measurement of the sensitive parameter rather than increasing numerical precision elsewhere. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
    },
    {
      "id": "prob-robotics-and-automation-2-1",
      "title": "Calculation & Verification: Homogeneous transformations and chains",
      "unit": 2,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Homogeneous transformations and chains** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>Two aligned 0.30 m and 0.20 m links at zero joint angle place a planar tip 0.50 m from the first joint center. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Uncertainty audit.** Differentiate precision from accuracy: repeated values near one another may share a systematic offset. Use replicated trials and a calibration reference, and consider correlations when combining uncertainties. An error bound must be linked to a defined operating range. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
    },
    {
      "id": "prob-robotics-and-automation-2-2",
      "title": "Calculation & Verification: Two-link forward kinematics",
      "unit": 2,
      "question": "<p><strong>Problem Statement:</strong> For L1=0.30 m, L2=0.20 m, q1=0\u00b0, q2=90\u00b0, the tip is at (0.30,0.20) m. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Traceable Verification audit.** Record firmware or model version, sensor calibration, test fixture revision and all rejected trials. Set acceptance thresholds before viewing the final traces. If a physical trial cannot be carried out safely, use simulation only and write the missing validation item explicitly. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
    },
    {
      "id": "prob-robotics-and-automation-2-3",
      "title": "Calculation & Verification: Inverse kinematics and reachability",
      "unit": 2,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Inverse kinematics and reachability** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For L1=0.30 m, L2=0.20 m and tip distance 0.40 m, cos(q2)=0.25, giving elbow angles about \u00b175.52\u00b0. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Dimensional Balance audit.** Perform a units check by substituting SI base units and showing both sides match. For angles, state that trigonometric functions expect radians unless explicitly converted. For probabilities, check output within [0,1], and for lengths or times reject negative values when the model defines only positive quantities. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
    },
    {
      "id": "prob-robotics-and-automation-2-4",
      "title": "Calculation & Verification: Jacobians and velocity transmission",
      "unit": 2,
      "question": "<p><strong>Problem Statement:</strong> At L1=0.30 m, L2=0.20 m, q2=90\u00b0, the determinant magnitude is 0.060 m\u00b2, while at q2=0\u00b0 it is zero. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Boundary Cases audit.** Check a zero-input limit, a typical operating point and a maximum planned input. Where derivatives exist, estimate local sensitivity to a 5% change. If the result changes sharply, prioritize a measurement of the sensitive parameter rather than increasing numerical precision elsewhere. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
    },
    {
      "id": "prob-robotics-and-automation-2-5",
      "title": "Calculation & Verification: Calibration, payload and workspace uncertainty",
      "unit": 2,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Calibration, payload and workspace uncertainty** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>With independent contributions 0.4 mm and 0.3 mm to x error, root-sum-square uncertainty is 0.5 mm under the independence approximation. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Discretization audit.** Choose a simulation step that resolves the fastest physical phenomenon of interest. Check convergence with a smaller step and confirm that numerical artifacts do not explain apparent stability or contact behavior. Sampling rates must exceed the bandwidth of the phenomena they are claimed to detect. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
    },
    {
      "id": "prob-robotics-and-automation-3-1",
      "title": "Calculation & Verification: Newton\u2013Euler balance for links",
      "unit": 3,
      "question": "<p><strong>Problem Statement:</strong> With I=0.060 kg\u00b7m\u00b2 and angular acceleration 4 rad/s\u00b2, an ideal isolated axis needs 0.24 N\u00b7m acceleration torque before gravity and friction. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Traceable Verification audit.** Record firmware or model version, sensor calibration, test fixture revision and all rejected trials. Set acceptance thresholds before viewing the final traces. If a physical trial cannot be carried out safely, use simulation only and write the missing validation item explicitly. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
    },
    {
      "id": "prob-robotics-and-automation-3-2",
      "title": "Calculation & Verification: Lagrange formulation and energy",
      "unit": 3,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Lagrange formulation and energy** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For a single rigid link with I=0.08 kg\u00b7m\u00b2, angular acceleration 2 rad/s\u00b2 gives 0.16 N\u00b7m inertia torque in the gravity-free idealization. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Dimensional Balance audit.** Perform a units check by substituting SI base units and showing both sides match. For angles, state that trigonometric functions expect radians unless explicitly converted. For probabilities, check output within [0,1], and for lengths or times reject negative values when the model defines only positive quantities. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
    },
    {
      "id": "prob-robotics-and-automation-3-3",
      "title": "Calculation & Verification: Motor and gear selection",
      "unit": 3,
      "question": "<p><strong>Problem Statement:</strong> For gear ratio 12, efficiency 0.80 and motor torque 0.15 N\u00b7m, output torque is 1.44 N\u00b7m under the assumed point-efficiency. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Boundary Cases audit.** Check a zero-input limit, a typical operating point and a maximum planned input. Where derivatives exist, estimate local sensitivity to a 5% change. If the result changes sharply, prioritize a measurement of the sensitive parameter rather than increasing numerical precision elsewhere. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
    },
    {
      "id": "prob-robotics-and-automation-3-4",
      "title": "Calculation & Verification: Grasp force, friction and object variability",
      "unit": 3,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Grasp force, friction and object variability** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For m=1 kg, \u03bc=0.50 and upward acceleration 1 m/s\u00b2, each jaw needs at least 10.81 N in the ideal symmetric model. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Discretization audit.** Choose a simulation step that resolves the fastest physical phenomenon of interest. Check convergence with a smaller step and confirm that numerical artifacts do not explain apparent stability or contact behavior. Sampling rates must exceed the bandwidth of the phenomena they are claimed to detect. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
    },
    {
      "id": "prob-robotics-and-automation-3-5",
      "title": "Calculation & Verification: Collision impulse and compliant contact",
      "unit": 3,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Collision impulse and compliant contact** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A 2 kg object stopped from 0.5 m/s experiences 1 N\u00b7s magnitude impulse regardless of how quickly it is stopped. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Uncertainty audit.** Differentiate precision from accuracy: repeated values near one another may share a systematic offset. Use replicated trials and a calibration reference, and consider correlations when combining uncertainties. An error bound must be linked to a defined operating range. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
    },
    {
      "id": "prob-robotics-and-automation-4-1",
      "title": "Calculation & Verification: Path versus trajectory",
      "unit": 4,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Path versus trajectory** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A 0.60 m path traversed in 1.5 s has average path speed 0.40 m/s, not necessarily constant Cartesian velocity. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Dimensional Balance audit.** Perform a units check by substituting SI base units and showing both sides match. For angles, state that trigonometric functions expect radians unless explicitly converted. For probabilities, check output within [0,1], and for lengths or times reject negative values when the model defines only positive quantities. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
    },
    {
      "id": "prob-robotics-and-automation-4-2",
      "title": "Calculation & Verification: Trapezoidal and triangular velocity profiles",
      "unit": 4,
      "question": "<p><strong>Problem Statement:</strong> For d=0.20 m, a=1 m/s\u00b2 and vmax=1 m/s, the triangular profile takes about 0.894 s. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Boundary Cases audit.** Check a zero-input limit, a typical operating point and a maximum planned input. Where derivatives exist, estimate local sensitivity to a 5% change. If the result changes sharply, prioritize a measurement of the sensitive parameter rather than increasing numerical precision elsewhere. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
    },
    {
      "id": "prob-robotics-and-automation-4-3",
      "title": "Calculation & Verification: Jerk-limited motion profiles",
      "unit": 4,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Jerk-limited motion profiles** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>Changing acceleration from 0 to 2 m/s\u00b2 over 0.20 s gives mean jerk magnitude 10 m/s\u00b3 under a linear ramp. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Discretization audit.** Choose a simulation step that resolves the fastest physical phenomenon of interest. Check convergence with a smaller step and confirm that numerical artifacts do not explain apparent stability or contact behavior. Sampling rates must exceed the bandwidth of the phenomena they are claimed to detect. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
    },
    {
      "id": "prob-robotics-and-automation-4-4",
      "title": "Calculation & Verification: Joint-space and Cartesian interpolation",
      "unit": 4,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Joint-space and Cartesian interpolation** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>At s=0.25 between 20\u00b0 and 60\u00b0, a single interpolated joint is 30\u00b0; intermediate tool positions depend on all other joints. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Uncertainty audit.** Differentiate precision from accuracy: repeated values near one another may share a systematic offset. Use replicated trials and a calibration reference, and consider correlations when combining uncertainties. An error bound must be linked to a defined operating range. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
    },
    {
      "id": "prob-robotics-and-automation-4-5",
      "title": "Calculation & Verification: Collision checking and replanning",
      "unit": 4,
      "question": "<p><strong>Problem Statement:</strong> With predicted clearance 15 mm and combined safety margin 7 mm, the remaining modeled clearance is 8 mm, subject to calibration validity. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Traceable Verification audit.** Record firmware or model version, sensor calibration, test fixture revision and all rejected trials. Set acceptance thresholds before viewing the final traces. If a physical trial cannot be carried out safely, use simulation only and write the missing validation item explicitly. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
    },
    {
      "id": "prob-robotics-and-automation-5-1",
      "title": "Calculation & Verification: Differential-drive kinematics",
      "unit": 5,
      "question": "<p><strong>Problem Statement:</strong> For vR=0.60 m/s, vL=0.20 m/s and track b=0.50 m, body speed is 0.40 m/s and yaw rate 0.80 rad/s. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Boundary Cases audit.** Check a zero-input limit, a typical operating point and a maximum planned input. Where derivatives exist, estimate local sensitivity to a 5% change. If the result changes sharply, prioritize a measurement of the sensitive parameter rather than increasing numerical precision elsewhere. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
    },
    {
      "id": "prob-robotics-and-automation-5-2",
      "title": "Calculation & Verification: Wheel odometry and pose integration",
      "unit": 5,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Wheel odometry and pose integration** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>Left travel 0.40 m and right travel 0.50 m imply nominal center travel 0.45 m between readings. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Discretization audit.** Choose a simulation step that resolves the fastest physical phenomenon of interest. Check convergence with a smaller step and confirm that numerical artifacts do not explain apparent stability or contact behavior. Sampling rates must exceed the bandwidth of the phenomena they are claimed to detect. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
    },
    {
      "id": "prob-robotics-and-automation-5-3",
      "title": "Calculation & Verification: Inertial and visual sensor fusion",
      "unit": 5,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Inertial and visual sensor fusion** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A residual gyro bias 0.1\u00b0/s accumulates about 6\u00b0 heading error over one minute if uncorrected. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Uncertainty audit.** Differentiate precision from accuracy: repeated values near one another may share a systematic offset. Use replicated trials and a calibration reference, and consider correlations when combining uncertainties. An error bound must be linked to a defined operating range. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
    },
    {
      "id": "prob-robotics-and-automation-5-4",
      "title": "Calculation & Verification: Occupancy grids and mapping uncertainty",
      "unit": 5,
      "question": "<p><strong>Problem Statement:</strong> With prior occupancy 0.50, detection probability 0.80 and false-positive rate 0.20, a positive report yields posterior occupancy 0.80. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Traceable Verification audit.** Record firmware or model version, sensor calibration, test fixture revision and all rejected trials. Set acceptance thresholds before viewing the final traces. If a physical trial cannot be carried out safely, use simulation only and write the missing validation item explicitly. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
    },
    {
      "id": "prob-robotics-and-automation-5-5",
      "title": "Calculation & Verification: Localization failure and recovery",
      "unit": 5,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Localization failure and recovery** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For planar errors 0.12 m and 0.05 m, Euclidean position error is 0.13 m. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Dimensional Balance audit.** Perform a units check by substituting SI base units and showing both sides match. For angles, state that trigonometric functions expect radians unless explicitly converted. For probabilities, check output within [0,1], and for lengths or times reject negative values when the model defines only positive quantities. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
    },
    {
      "id": "prob-robotics-and-automation-6-1",
      "title": "Calculation & Verification: Cameras, depth sensors and calibration",
      "unit": 6,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Cameras, depth sensors and calibration** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For f=500 pixel, baseline=0.10 m and disparity=50 pixel, depth is 1.0 m in the ideal model. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Discretization audit.** Choose a simulation step that resolves the fastest physical phenomenon of interest. Check convergence with a smaller step and confirm that numerical artifacts do not explain apparent stability or contact behavior. Sampling rates must exceed the bandwidth of the phenomena they are claimed to detect. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
    },
    {
      "id": "prob-robotics-and-automation-6-2",
      "title": "Calculation & Verification: Detection confidence and classification",
      "unit": 6,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Detection confidence and classification** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>With 80 true positives and 20 false positives, sample precision is 0.80; this does not measure recall without false negatives. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Uncertainty audit.** Differentiate precision from accuracy: repeated values near one another may share a systematic offset. Use replicated trials and a calibration reference, and consider correlations when combining uncertainties. An error bound must be linked to a defined operating range. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
    },
    {
      "id": "prob-robotics-and-automation-6-3",
      "title": "Calculation & Verification: Graph and grid path planning",
      "unit": 6,
      "question": "<p><strong>Problem Statement:</strong> For relative cell offsets dx=4, dy=3, Manhattan lower bound is seven unit moves when diagonal actions are disallowed. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Traceable Verification audit.** Record firmware or model version, sensor calibration, test fixture revision and all rejected trials. Set acceptance thresholds before viewing the final traces. If a physical trial cannot be carried out safely, use simulation only and write the missing validation item explicitly. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
    },
    {
      "id": "prob-robotics-and-automation-6-4",
      "title": "Calculation & Verification: Reactive obstacle avoidance",
      "unit": 6,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Reactive obstacle avoidance** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>At speed 0.80 m/s, delay 0.10 s and deceleration 1.0 m/s\u00b2, ideal stop distance is 0.40 m before uncertainties. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Dimensional Balance audit.** Perform a units check by substituting SI base units and showing both sides match. For angles, state that trigonometric functions expect radians unless explicitly converted. For probabilities, check output within [0,1], and for lengths or times reject negative values when the model defines only positive quantities. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
    },
    {
      "id": "prob-robotics-and-automation-6-5",
      "title": "Calculation & Verification: Task planning and finite-state execution",
      "unit": 6,
      "question": "<p><strong>Problem Statement:</strong> With per-attempt success probability 0.80, expected attempts are 1.25 only if trials are independent and identical. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Boundary Cases audit.** Check a zero-input limit, a typical operating point and a maximum planned input. Where derivatives exist, estimate local sensitivity to a 5% change. If the result changes sharply, prioritize a measurement of the sensitive parameter rather than increasing numerical precision elsewhere. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
    },
    {
      "id": "prob-robotics-and-automation-7-1",
      "title": "Calculation & Verification: PLC handshakes and interlocks",
      "unit": 7,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **PLC handshakes and interlocks** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>Stages 0.3, 1.0, 0.4 and 0.8 s total 2.5 s if none can overlap. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Uncertainty audit.** Differentiate precision from accuracy: repeated values near one another may share a systematic offset. Use replicated trials and a calibration reference, and consider correlations when combining uncertainties. An error bound must be linked to a defined operating range. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
    },
    {
      "id": "prob-robotics-and-automation-7-2",
      "title": "Calculation & Verification: Cycle-time budgets and bottlenecks",
      "unit": 7,
      "question": "<p><strong>Problem Statement:</strong> For a 5 s bottleneck cycle and 90% uptime, expected steady nominal capacity is 648 units per hour before scrap. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Traceable Verification audit.** Record firmware or model version, sensor calibration, test fixture revision and all rejected trials. Set acceptance thresholds before viewing the final traces. If a physical trial cannot be carried out safely, use simulation only and write the missing validation item explicitly. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
    },
    {
      "id": "prob-robotics-and-automation-7-3",
      "title": "Calculation & Verification: Quality inspection and traceability",
      "unit": 7,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Quality inspection and traceability** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>If 960 of 1,000 inspected units pass, observed sample yield is 96%, without establishing the true defect rate. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Dimensional Balance audit.** Perform a units check by substituting SI base units and showing both sides match. For angles, state that trigonometric functions expect radians unless explicitly converted. For probabilities, check output within [0,1], and for lengths or times reject negative values when the model defines only positive quantities. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
    },
    {
      "id": "prob-robotics-and-automation-7-4",
      "title": "Calculation & Verification: Reliability and preventive maintenance",
      "unit": 7,
      "question": "<p><strong>Problem Statement:</strong> If lambda=0.0002 per hour, illustrative survival after 500 hours is exp(-0.1)\u22480.9048. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Boundary Cases audit.** Check a zero-input limit, a typical operating point and a maximum planned input. Where derivatives exist, estimate local sensitivity to a 5% change. If the result changes sharply, prioritize a measurement of the sensitive parameter rather than increasing numerical precision elsewhere. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
    },
    {
      "id": "prob-robotics-and-automation-7-5",
      "title": "Calculation & Verification: Commissioning, acceptance and change control",
      "unit": 7,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Commissioning, acceptance and change control** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>With 4 pick errors in 2,000 attempted cycles, observed error fraction is 0.002, not proof the true error rate is exactly 0.2%. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Discretization audit.** Choose a simulation step that resolves the fastest physical phenomenon of interest. Check convergence with a smaller step and confirm that numerical artifacts do not explain apparent stability or contact behavior. Sampling rates must exceed the bandwidth of the phenomena they are claimed to detect. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
    },
    {
      "id": "prob-robotics-and-automation-8-1",
      "title": "Calculation & Verification: Learning-based robot control and distribution shift",
      "unit": 8,
      "question": "<p><strong>Problem Statement:</strong> A policy succeeding in 92 of 100 synthetic scenarios has observed simulation success 92%, with wide uncertainty and no hardware proof. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Traceable Verification audit.** Record firmware or model version, sensor calibration, test fixture revision and all rejected trials. Set acceptance thresholds before viewing the final traces. If a physical trial cannot be carried out safely, use simulation only and write the missing validation item explicitly. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
    },
    {
      "id": "prob-robotics-and-automation-8-2",
      "title": "Calculation & Verification: Digital twins and simulation-to-real transfer",
      "unit": 8,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Digital twins and simulation-to-real transfer** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>Predicted travel 0.50 m versus measured 0.47 m gives residual \u22120.03 m under the stated sign convention. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Dimensional Balance audit.** Perform a units check by substituting SI base units and showing both sides match. For angles, state that trigonometric functions expect radians unless explicitly converted. For probabilities, check output within [0,1], and for lengths or times reject negative values when the model defines only positive quantities. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
    },
    {
      "id": "prob-robotics-and-automation-8-3",
      "title": "Calculation & Verification: Multi-robot coordination and scheduling",
      "unit": 8,
      "question": "<p><strong>Problem Statement:</strong> Arrival rate 0.10 tasks/s with 6 s average service time implies nominal utilization 0.60 for one server in the simplified model. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Boundary Cases audit.** Check a zero-input limit, a typical operating point and a maximum planned input. Where derivatives exist, estimate local sensitivity to a 5% change. If the result changes sharply, prioritize a measurement of the sensitive parameter rather than increasing numerical precision elsewhere. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
    },
    {
      "id": "prob-robotics-and-automation-8-4",
      "title": "Calculation & Verification: Automation cost and engineering trade-offs",
      "unit": 8,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Automation cost and engineering trade-offs** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A hypothetical $90,000 installation saving $15,000 per year net has simple payback six years, before discounting and residual value. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Discretization audit.** Choose a simulation step that resolves the fastest physical phenomenon of interest. Check convergence with a smaller step and confirm that numerical artifacts do not explain apparent stability or contact behavior. Sampling rates must exceed the bandwidth of the phenomena they are claimed to detect. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
    },
    {
      "id": "prob-robotics-and-automation-8-5",
      "title": "Calculation & Verification: Integrated capstone and reproducible evidence",
      "unit": 8,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Integrated capstone and reproducible evidence** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A guarded demonstration with 420 successful units in 0.75 h yields 560 accepted units/h over that observed window, not guaranteed monthly capacity. Reproduce the substitution on paper, carry units through each stage and check the scale with an independent estimate. Precision in displayed decimal places does not demonstrate precise knowledge of link lengths, accelerations, friction coefficients or camera calibration. If inputs are rounded or synthetic, the outputs inherit those limitations; do not label them as measured robot performance.\n\n**Uncertainty audit.** Differentiate precision from accuracy: repeated values near one another may share a systematic offset. Use replicated trials and a calibration reference, and consider correlations when combining uncertainties. An error bound must be linked to a defined operating range. Extend the example by sweeping one independent input through a realistic range. Predict the qualitative trend before computing. Then change another input in a separate run; explain why changing both simultaneously would make causal interpretation weaker. Document any singular, discontinuous or saturating regime instead of hiding it by clipping a plot without explanation.</p></div>"
    }
  ]
};
if (typeof module !== 'undefined') module.exports = COURSE_DATA;
if (typeof window !== 'undefined') window.COURSE_DATA = COURSE_DATA;
