/* OpenSTEM Course Data: Control Systems Engineering (CSE) */
var COURSE_DATA = {
  "code": "CSE",
  "title": "Control Systems Engineering",
  "subtitle": "Transfer Functions, Block Diagrams, Routh-Hurwitz, Root Locus, Bode/Nyquist Stability & State-Space",
  "units": [
    {
      "number": 1,
      "unitNumber": 1,
      "title": "Modeling, Feedback, and Control Architecture",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Modeling, Feedback, and Control Architecture.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Modeling, Feedback, and Control Architecture.",
      "sections": [
        {
          "id": "sec-1-1",
          "title": "Control objectives, signals, and feedback",
          "leadSummary": "**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 1: Modeling, Feedback, and Control Architecture.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.",
          "content": "<p>**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 1: Modeling, Feedback, and Control Architecture.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.</p>"
        },
        {
          "id": "sec-1-2",
          "title": "Dynamic models from physical balances",
          "leadSummary": "**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 1: Modeling, Feedback, and Control Architecture.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.",
          "content": "<p>**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 1: Modeling, Feedback, and Control Architecture.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.</p>"
        },
        {
          "id": "sec-1-3",
          "title": "Laplace transforms and transfer functions",
          "leadSummary": "**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 1: Modeling, Feedback, and Control Architecture.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.",
          "content": "<p>**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 1: Modeling, Feedback, and Control Architecture.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.</p>"
        },
        {
          "id": "sec-1-4",
          "title": "Block diagrams, feedback algebra and signal paths",
          "leadSummary": "**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 1: Modeling, Feedback, and Control Architecture.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.",
          "content": "<p>**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 1: Modeling, Feedback, and Control Architecture.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.</p>"
        },
        {
          "id": "sec-1-5",
          "title": "Scaling, assumptions, and baseline experiments",
          "leadSummary": "**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 1: Modeling, Feedback, and Control Architecture.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.",
          "content": "<p>**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 1: Modeling, Feedback, and Control Architecture.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-control-systems-engineering-1-1",
          "title": "Calculation & Verification: Control objectives, signals, and feedback",
          "unit": 1,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Control objectives, signals, and feedback** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>At a 1500 rpm command and 1440 rpm encoder reading the displayed error is 60 rpm. If the encoder has a +20 rpm bias, actual speed is about 1420 rpm and the true tracking difference is about 80 rpm.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
        },
        {
          "id": "prob-control-systems-engineering-1-2",
          "title": "Calculation & Verification: Dynamic models from physical balances",
          "unit": 1,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Dynamic models from physical balances** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For J=0.020 kg\u00b7m\u00b2 and b=0.10 N\u00b7m\u00b7s/rad, the no-load speed-to-torque transfer is \u03a9(s)/T(s)=1/(0.02s+0.1), with a 0.20 s time constant.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
        },
        {
          "id": "prob-control-systems-engineering-1-3",
          "title": "Calculation & Verification: Laplace transforms and transfer functions",
          "unit": 1,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Laplace transforms and transfer functions** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>With K=2 rpm/V and \u03c4=0.5 s, a 3 V command gives a final increment 6 rpm; at t=0.5 s the first-order response is 6(1\u2212e\u207b\u00b9)=3.793 rpm.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
        },
        {
          "id": "prob-control-systems-engineering-1-4",
          "title": "Calculation & Verification: Block diagrams, feedback algebra and signal paths",
          "unit": 1,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Block diagrams, feedback algebra and signal paths** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A first-order plant G=1/(s+1) with proportional gain 4 yields T=4/(s+5); DC closed-loop gain is 0.8, not unity.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
        },
        {
          "id": "prob-control-systems-engineering-1-5",
          "title": "Calculation & Verification: Scaling, assumptions, and baseline experiments",
          "unit": 1,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Scaling, assumptions, and baseline experiments** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A measured change from 20\u00b0C toward 60\u00b0C reaches 45.3\u00b0C at approximately one first-order time constant; a later measurement may indicate a second slower thermal mode.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
        }
      ]
    },
    {
      "number": 2,
      "unitNumber": 2,
      "title": "Time Response and Performance Specifications",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Time Response and Performance Specifications.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Time Response and Performance Specifications.",
      "sections": [
        {
          "id": "sec-2-1",
          "title": "First-order steps and time constants",
          "leadSummary": "**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 2: Time Response and Performance Specifications.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.",
          "content": "<p>**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 2: Time Response and Performance Specifications.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.</p>"
        },
        {
          "id": "sec-2-2",
          "title": "Second-order modes, damping and overshoot",
          "leadSummary": "**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 2: Time Response and Performance Specifications.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.",
          "content": "<p>**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 2: Time Response and Performance Specifications.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.</p>"
        },
        {
          "id": "sec-2-3",
          "title": "Rise time, settling time and specification tradeoffs",
          "leadSummary": "**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 2: Time Response and Performance Specifications.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.",
          "content": "<p>**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 2: Time Response and Performance Specifications.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.</p>"
        },
        {
          "id": "sec-2-4",
          "title": "Pole locations, zeros and transient shape",
          "leadSummary": "**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 2: Time Response and Performance Specifications.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.",
          "content": "<p>**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 2: Time Response and Performance Specifications.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.</p>"
        },
        {
          "id": "sec-2-5",
          "title": "Experimental step tests and system identification",
          "leadSummary": "**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 2: Time Response and Performance Specifications.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.",
          "content": "<p>**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 2: Time Response and Performance Specifications.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-control-systems-engineering-2-1",
          "title": "Calculation & Verification: First-order steps and time constants",
          "unit": 2,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **First-order steps and time constants** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A valve opens and flow increases from 0 to 80 L/min with \u03c4=6 s. At t=12 s, y\u224880(1\u2212e\u207b\u00b2)=69.17 L/min.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
        },
        {
          "id": "prob-control-systems-engineering-2-2",
          "title": "Calculation & Verification: Second-order modes, damping and overshoot",
          "unit": 2,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Second-order modes, damping and overshoot** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>With \u03b6=0.5 and \u03c9_n=8 rad/s, ideal overshoot is \u224816.3%, peak time \u22480.453 s and approximate 2% settling time 1 s.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
        },
        {
          "id": "prob-control-systems-engineering-2-3",
          "title": "Calculation & Verification: Rise time, settling time and specification tradeoffs",
          "unit": 2,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Rise time, settling time and specification tradeoffs** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A servo required to settle within \u00b11\u00b0 after a 20\u00b0 step needs a 5% band relative to the step. It is not the same test as a \u00b12% criterion.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
        },
        {
          "id": "prob-control-systems-engineering-2-4",
          "title": "Calculation & Verification: Pole locations, zeros and transient shape",
          "unit": 2,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Pole locations, zeros and transient shape** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For poles at \u22122\u00b1j6 rad/s, the modal envelope decays as e\u207b\u00b2\u1d57 and the oscillation frequency is 6/(2\u03c0)=0.955 Hz.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
        },
        {
          "id": "prob-control-systems-engineering-2-5",
          "title": "Calculation & Verification: Experimental step tests and system identification",
          "unit": 2,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Experimental step tests and system identification** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>When a 2 V step changes steady temperature by 10\u00b0C, the static gain is 5\u00b0C/V. If the response begins only after 3 s, the delay is approximately 3 s, separate from the thermal time constant.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
        }
      ]
    },
    {
      "number": 3,
      "unitNumber": 3,
      "title": "Stability, Error, and Robustness",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Stability, Error, and Robustness.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Stability, Error, and Robustness.",
      "sections": [
        {
          "id": "sec-3-1",
          "title": "Closed-loop characteristic equations",
          "leadSummary": "**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 3: Stability, Error, and Robustness.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.",
          "content": "<p>**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 3: Stability, Error, and Robustness.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.</p>"
        },
        {
          "id": "sec-3-2",
          "title": "Routh\u2013Hurwitz stability screening",
          "leadSummary": "**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 3: Stability, Error, and Robustness.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.",
          "content": "<p>**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 3: Stability, Error, and Robustness.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.</p>"
        },
        {
          "id": "sec-3-3",
          "title": "Root locus and gain selection",
          "leadSummary": "**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 3: Stability, Error, and Robustness.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.",
          "content": "<p>**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 3: Stability, Error, and Robustness.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.</p>"
        },
        {
          "id": "sec-3-4",
          "title": "Steady-state error and system type",
          "leadSummary": "**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 3: Stability, Error, and Robustness.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.",
          "content": "<p>**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 3: Stability, Error, and Robustness.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.</p>"
        },
        {
          "id": "sec-3-5",
          "title": "Uncertainty, robustness and actuator limits",
          "leadSummary": "**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 3: Stability, Error, and Robustness.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.",
          "content": "<p>**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 3: Stability, Error, and Robustness.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-control-systems-engineering-3-1",
          "title": "Calculation & Verification: Closed-loop characteristic equations",
          "unit": 3,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Closed-loop characteristic equations** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>With G(s)=1/(s(s+2)) and C(s)=K, the characteristic polynomial is s\u00b2+2s+K; K>0 gives stable second-order poles.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
        },
        {
          "id": "prob-control-systems-engineering-3-2",
          "title": "Calculation & Verification: Routh\u2013Hurwitz stability screening",
          "unit": 3,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Routh\u2013Hurwitz stability screening** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For p(s)=s\u00b3+4s\u00b2+5s+K, stable operation for positive K requires 0<K<20. At K=20 the system is marginal and needs further analysis.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
        },
        {
          "id": "prob-control-systems-engineering-3-3",
          "title": "Calculation & Verification: Root locus and gain selection",
          "unit": 3,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Root locus and gain selection** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For 1/(s(s+2)) with gain K, poles solve s\u00b2+2s+K=0. At K=1 the poles coincide at \u22121; for K>1 they are complex with real part \u22121.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
        },
        {
          "id": "prob-control-systems-engineering-3-4",
          "title": "Calculation & Verification: Steady-state error and system type",
          "unit": 3,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Steady-state error and system type** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For G=1/(s+1), C=3 and unity feedback, step reference error tends to 1/(1+3)=0.25. Adding integral action can remove that ideal offset.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
        },
        {
          "id": "prob-control-systems-engineering-3-5",
          "title": "Calculation & Verification: Uncertainty, robustness and actuator limits",
          "unit": 3,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Uncertainty, robustness and actuator limits** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>If a thermal plant gain varies from 1.0 to 1.8\u00b0C/% heater due to airflow, a single nominal controller setting may deliver very different overshoot and settling.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
        }
      ]
    },
    {
      "number": 4,
      "unitNumber": 4,
      "title": "Frequency-Domain Analysis",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Frequency-Domain Analysis.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Frequency-Domain Analysis.",
      "sections": [
        {
          "id": "sec-4-1",
          "title": "Sinusoidal steady-state and frequency response",
          "leadSummary": "**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 4: Frequency-Domain Analysis.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.",
          "content": "<p>**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 4: Frequency-Domain Analysis.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.</p>"
        },
        {
          "id": "sec-4-2",
          "title": "Bode plots, slopes and break frequencies",
          "leadSummary": "**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 4: Frequency-Domain Analysis.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.",
          "content": "<p>**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 4: Frequency-Domain Analysis.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.</p>"
        },
        {
          "id": "sec-4-3",
          "title": "Nyquist criterion and encirclements",
          "leadSummary": "**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 4: Frequency-Domain Analysis.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.",
          "content": "<p>**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 4: Frequency-Domain Analysis.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.</p>"
        },
        {
          "id": "sec-4-4",
          "title": "Gain margin, phase margin and bandwidth",
          "leadSummary": "**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 4: Frequency-Domain Analysis.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.",
          "content": "<p>**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 4: Frequency-Domain Analysis.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.</p>"
        },
        {
          "id": "sec-4-5",
          "title": "Sensitivity, disturbances and sensor noise",
          "leadSummary": "**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 4: Frequency-Domain Analysis.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.",
          "content": "<p>**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 4: Frequency-Domain Analysis.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-control-systems-engineering-4-1",
          "title": "Calculation & Verification: Sinusoidal steady-state and frequency response",
          "unit": 4,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Sinusoidal steady-state and frequency response** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For G=1/(1+0.5s) at \u03c9=4 rad/s, magnitude=1/\u221a5\u22480.447 and phase=\u2212arctan 2\u2248\u221263.4\u00b0.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
        },
        {
          "id": "prob-control-systems-engineering-4-2",
          "title": "Calculation & Verification: Bode plots, slopes and break frequencies",
          "unit": 4,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Bode plots, slopes and break frequencies** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For a pole at 10 rad/s, \u03c9=10 rad/s gives amplitude 1/\u221a2\u22480.707 and phase \u221245\u00b0 relative to low-frequency gain.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
        },
        {
          "id": "prob-control-systems-engineering-4-3",
          "title": "Calculation & Verification: Nyquist criterion and encirclements",
          "unit": 4,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Nyquist criterion and encirclements** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For L(j\u03c9)=K/(1+j\u03c9\u03c4), positive K and \u03c4 produce phase between 0 and \u221290\u00b0, so the simple unity-feedback loop has no crossing of \u2212180\u00b0.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
        },
        {
          "id": "prob-control-systems-engineering-4-4",
          "title": "Calculation & Verification: Gain margin, phase margin and bandwidth",
          "unit": 4,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Gain margin, phase margin and bandwidth** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>At crossover, a measured open-loop phase of \u2212135\u00b0 implies about 45\u00b0 phase margin. If extra delay adds 0.15 rad at crossover, the margin drops by \u22488.6\u00b0.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
        },
        {
          "id": "prob-control-systems-engineering-4-5",
          "title": "Calculation & Verification: Sensitivity, disturbances and sensor noise",
          "unit": 4,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Sensitivity, disturbances and sensor noise** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>With L(j\u03c9)=9 at a very low frequency, S\u22480.1 and T\u22480.9 for this real loop value. Large high-frequency loop gain instead passes measurement noise into the output.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
        }
      ]
    },
    {
      "number": 5,
      "unitNumber": 5,
      "title": "PID, Compensation and Practical Tuning",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of PID, Compensation and Practical Tuning.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of PID, Compensation and Practical Tuning.",
      "sections": [
        {
          "id": "sec-5-1",
          "title": "Proportional control and closed-loop stiffness",
          "leadSummary": "**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 5: PID, Compensation and Practical Tuning.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.",
          "content": "<p>**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 5: PID, Compensation and Practical Tuning.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.</p>"
        },
        {
          "id": "sec-5-2",
          "title": "Integral control and PI design",
          "leadSummary": "**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 5: PID, Compensation and Practical Tuning.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.",
          "content": "<p>**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 5: PID, Compensation and Practical Tuning.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.</p>"
        },
        {
          "id": "sec-5-3",
          "title": "Derivative action and filtered PID",
          "leadSummary": "**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 5: PID, Compensation and Practical Tuning.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.",
          "content": "<p>**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 5: PID, Compensation and Practical Tuning.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.</p>"
        },
        {
          "id": "sec-5-4",
          "title": "Anti-windup, setpoint shaping and bumpless transfer",
          "leadSummary": "**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 5: PID, Compensation and Practical Tuning.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.",
          "content": "<p>**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 5: PID, Compensation and Practical Tuning.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.</p>"
        },
        {
          "id": "sec-5-5",
          "title": "Lead\u2013lag compensation and tuning protocols",
          "leadSummary": "**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 5: PID, Compensation and Practical Tuning.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.",
          "content": "<p>**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 5: PID, Compensation and Practical Tuning.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-control-systems-engineering-5-1",
          "title": "Calculation & Verification: Proportional control and closed-loop stiffness",
          "unit": 5,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Proportional control and closed-loop stiffness** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>With K=2, \u03c4=4 s and K_p=1.5, the ideal closed-loop \u03c4 becomes 1 s, while unit-step output tends to 0.75.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
        },
        {
          "id": "prob-control-systems-engineering-5-2",
          "title": "Calculation & Verification: Integral control and PI design",
          "unit": 5,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Integral control and PI design** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For K_p=2 and K_i=0.5 s\u207b\u00b9 in matching normalized units, the PI zero is at \u22120.25 rad/s and integral time is 4 s.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
        },
        {
          "id": "prob-control-systems-engineering-5-3",
          "title": "Calculation & Verification: Derivative action and filtered PID",
          "unit": 5,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Derivative action and filtered PID** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>If measurement increases at 2\u00b0C/s and K_d=0.8 %heater\u00b7s/\u00b0C, ideal derivative-on-measurement requests a \u22121.6 percentage-point command adjustment before filtering.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
        },
        {
          "id": "prob-control-systems-engineering-5-4",
          "title": "Calculation & Verification: Anti-windup, setpoint shaping and bumpless transfer",
          "unit": 5,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Anti-windup, setpoint shaping and bumpless transfer** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A heater with 0\u2013100% command saturates at 100% during a large temperature change; stopping integral accumulation when the same error direction deepens saturation shortens recovery.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
        },
        {
          "id": "prob-control-systems-engineering-5-5",
          "title": "Calculation & Verification: Lead\u2013lag compensation and tuning protocols",
          "unit": 5,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Lead\u2013lag compensation and tuning protocols** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For \u03b1=0.25, maximum ideal phase lead is asin((1\u2212\u03b1)/(1+\u03b1))\u224836.9\u00b0. It occurs near \u03c9\u22481/(T\u221a\u03b1).\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
        }
      ]
    },
    {
      "number": 6,
      "unitNumber": 6,
      "title": "State-Space and Modern Control",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of State-Space and Modern Control.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of State-Space and Modern Control.",
      "sections": [
        {
          "id": "sec-6-1",
          "title": "State variables and linear state models",
          "leadSummary": "**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 6: State-Space and Modern Control.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.",
          "content": "<p>**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 6: State-Space and Modern Control.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.</p>"
        },
        {
          "id": "sec-6-2",
          "title": "Controllability and reachable states",
          "leadSummary": "**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 6: State-Space and Modern Control.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.",
          "content": "<p>**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 6: State-Space and Modern Control.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.</p>"
        },
        {
          "id": "sec-6-3",
          "title": "Observability and sensor selection",
          "leadSummary": "**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 6: State-Space and Modern Control.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.",
          "content": "<p>**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 6: State-Space and Modern Control.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.</p>"
        },
        {
          "id": "sec-6-4",
          "title": "State feedback and pole placement",
          "leadSummary": "**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 6: State-Space and Modern Control.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.",
          "content": "<p>**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 6: State-Space and Modern Control.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.</p>"
        },
        {
          "id": "sec-6-5",
          "title": "Observers, Kalman filtering and estimation",
          "leadSummary": "**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 6: State-Space and Modern Control.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.",
          "content": "<p>**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 6: State-Space and Modern Control.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-control-systems-engineering-6-1",
          "title": "Calculation & Verification: State variables and linear state models",
          "unit": 6,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **State variables and linear state models** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For m=2 kg, b=4 N\u00b7s/m, k=50 N/m, the state acceleration is \u221225x1\u22122x2+0.5u.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
        },
        {
          "id": "prob-control-systems-engineering-6-2",
          "title": "Calculation & Verification: Controllability and reachable states",
          "unit": 6,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Controllability and reachable states** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For double integrator A=[[0,1],[0,0]] and B=[[0],[1]], controllability matrix [B,AB]=[[0,1],[1,0]], rank 2.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
        },
        {
          "id": "prob-control-systems-engineering-6-3",
          "title": "Calculation & Verification: Observability and sensor selection",
          "unit": 6,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Observability and sensor selection** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For A=[[0,1],[0,0]] and C=[1,0], observability determinant is 1, confirming rank 2.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
        },
        {
          "id": "prob-control-systems-engineering-6-4",
          "title": "Calculation & Verification: State feedback and pole placement",
          "unit": 6,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **State feedback and pole placement** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For double integrator x\u0308=u, u=\u2212k1x\u2212k2x\u0307 produces characteristic s\u00b2+k2s+k1. Desired poles at \u22122 and \u22123 require k2=5 and k1=6.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
        },
        {
          "id": "prob-control-systems-engineering-6-5",
          "title": "Calculation & Verification: Observers, Kalman filtering and estimation",
          "unit": 6,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Observers, Kalman filtering and estimation** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For scalar x\u0307=\u22122x+u, y=x and observer gain L=4, ideal estimation error decays as e\u0307=\u22126e; the error time constant is 1/6 s.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
        }
      ]
    },
    {
      "number": 7,
      "unitNumber": 7,
      "title": "Digital Control and Implementation",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Digital Control and Implementation.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Digital Control and Implementation.",
      "sections": [
        {
          "id": "sec-7-1",
          "title": "Sampling rates and zero-order hold",
          "leadSummary": "**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 7: Digital Control and Implementation.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.",
          "content": "<p>**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 7: Digital Control and Implementation.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.</p>"
        },
        {
          "id": "sec-7-2",
          "title": "Discrete-time models and z-transforms",
          "leadSummary": "**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 7: Digital Control and Implementation.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.",
          "content": "<p>**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 7: Digital Control and Implementation.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.</p>"
        },
        {
          "id": "sec-7-3",
          "title": "Discrete stability and pole mapping",
          "leadSummary": "**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 7: Digital Control and Implementation.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.",
          "content": "<p>**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 7: Digital Control and Implementation.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.</p>"
        },
        {
          "id": "sec-7-4",
          "title": "Digital PI/PID, saturation and computation delay",
          "leadSummary": "**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 7: Digital Control and Implementation.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.",
          "content": "<p>**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 7: Digital Control and Implementation.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.</p>"
        },
        {
          "id": "sec-7-5",
          "title": "Quantization, filtering, latency and deployment",
          "leadSummary": "**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 7: Digital Control and Implementation.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.",
          "content": "<p>**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 7: Digital Control and Implementation.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-control-systems-engineering-7-1",
          "title": "Calculation & Verification: Sampling rates and zero-order hold",
          "unit": 7,
          "question": "<p><strong>Problem Statement:</strong> </p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For a 5 Hz oscillation, a 12 Hz sample rate barely exceeds the Nyquist threshold; 100 Hz yields twenty samples per cycle and better waveform resolution.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
        },
        {
          "id": "prob-control-systems-engineering-7-2",
          "title": "Calculation & Verification: Discrete-time models and z-transforms",
          "unit": 7,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Discrete-time models and z-transforms** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For \u03c4=2 s and h=0.1 s, a=e\u207b\u2070\u00b7\u2070\u2075\u22480.951229 and the input coefficient for K=3 is \u22480.146312.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
        },
        {
          "id": "prob-control-systems-engineering-7-3",
          "title": "Calculation & Verification: Discrete stability and pole mapping",
          "unit": 7,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Discrete stability and pole mapping** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A pole at s=\u22124 s\u207b\u00b9 with h=0.05 s maps to z=e\u207b\u2070\u00b7\u00b2\u22480.81873, strictly inside the unit circle.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
        },
        {
          "id": "prob-control-systems-engineering-7-4",
          "title": "Calculation & Verification: Digital PI/PID, saturation and computation delay",
          "unit": 7,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Digital PI/PID, saturation and computation delay** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>With K_i=0.4 s\u207b\u00b9, h=0.2 s and e[k]=5 units, one rectangular integrator update adds 0.4 actuator units.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
        },
        {
          "id": "prob-control-systems-engineering-7-5",
          "title": "Calculation & Verification: Quantization, filtering, latency and deployment",
          "unit": 7,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Quantization, filtering, latency and deployment** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A 12-bit ADC over 0\u201310 V has step size 10/4096\u22482.44 mV. A plant with 0.05\u00b0C/mV sensor gain therefore has \u22480.122\u00b0C per code in this synthetic illustration.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
        }
      ]
    },
    {
      "number": 8,
      "unitNumber": 8,
      "title": "Engineering Applications and Verification",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Engineering Applications and Verification.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Engineering Applications and Verification.",
      "sections": [
        {
          "id": "sec-8-1",
          "title": "DC motor speed and torque regulation",
          "leadSummary": "**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 8: Engineering Applications and Verification.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.",
          "content": "<p>**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 8: Engineering Applications and Verification.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.</p>"
        },
        {
          "id": "sec-8-2",
          "title": "Thermal chamber temperature regulation",
          "leadSummary": "**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 8: Engineering Applications and Verification.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.",
          "content": "<p>**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 8: Engineering Applications and Verification.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.</p>"
        },
        {
          "id": "sec-8-3",
          "title": "Active damping and vibration isolation",
          "leadSummary": "**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 8: Engineering Applications and Verification.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.",
          "content": "<p>**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 8: Engineering Applications and Verification.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.</p>"
        },
        {
          "id": "sec-8-4",
          "title": "Motion control for a positioning axis",
          "leadSummary": "**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 8: Engineering Applications and Verification.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.",
          "content": "<p>**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 8: Engineering Applications and Verification.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.</p>"
        },
        {
          "id": "sec-8-5",
          "title": "Validation, fault response and responsible deployment",
          "leadSummary": "**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 8: Engineering Applications and Verification.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.",
          "content": "<p>**Mechanical Engineering \u00b7 Control Systems Engineering \u00b7 Unit 8: Engineering Applications and Verification.**  This is an unreviewed instructional chapter; none of its calculations alone justifies commissioning machinery.</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-control-systems-engineering-8-1",
          "title": "Calculation & Verification: DC motor speed and torque regulation",
          "unit": 8,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **DC motor speed and torque regulation** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For steady state R=2 \u03a9, K_e=0.1 V\u00b7s/rad, K_t=0.1 N\u00b7m/A and b=0.01 N\u00b7m\u00b7s/rad, a 10 V supply produces no-load speed \u224833.3 rad/s in the simplified steady model.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
        },
        {
          "id": "prob-control-systems-engineering-8-2",
          "title": "Calculation & Verification: Thermal chamber temperature regulation",
          "unit": 8,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Thermal chamber temperature regulation** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For C_th=1000 J/K and hA=10 W/K, \u03c4=C_th/(hA)=100 s. At 200 W constant input, ideal steady excess temperature is 20 K.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
        },
        {
          "id": "prob-control-systems-engineering-8-3",
          "title": "Calculation & Verification: Active damping and vibration isolation",
          "unit": 8,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Active damping and vibration isolation** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For m=2 kg, b=1 N\u00b7s/m and k_d=5 N\u00b7s/m, effective damping is 6 N\u00b7s/m in the ideal scalar model.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
        },
        {
          "id": "prob-control-systems-engineering-8-4",
          "title": "Calculation & Verification: Motion control for a positioning axis",
          "unit": 8,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Motion control for a positioning axis** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A stage moving 0.2 m in 1 s has average speed 0.2 m/s, but a smooth start-and-stop trajectory must peak above the average speed. The actuator should be sized for peak acceleration and load.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
        },
        {
          "id": "prob-control-systems-engineering-8-5",
          "title": "Calculation & Verification: Validation, fault response and responsible deployment",
          "unit": 8,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Validation, fault response and responsible deployment** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For a safety interlock that must de-energize in 200 ms, a software polling loop running every 250 ms cannot guarantee compliance even before execution and communication delays.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
        }
      ]
    }
  ],
  "problems": [
    {
      "id": "prob-control-systems-engineering-1-1",
      "title": "Calculation & Verification: Control objectives, signals, and feedback",
      "unit": 1,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Control objectives, signals, and feedback** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>At a 1500 rpm command and 1440 rpm encoder reading the displayed error is 60 rpm. If the encoder has a +20 rpm bias, actual speed is about 1420 rpm and the true tracking difference is about 80 rpm.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
    },
    {
      "id": "prob-control-systems-engineering-1-2",
      "title": "Calculation & Verification: Dynamic models from physical balances",
      "unit": 1,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Dynamic models from physical balances** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For J=0.020 kg\u00b7m\u00b2 and b=0.10 N\u00b7m\u00b7s/rad, the no-load speed-to-torque transfer is \u03a9(s)/T(s)=1/(0.02s+0.1), with a 0.20 s time constant.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
    },
    {
      "id": "prob-control-systems-engineering-1-3",
      "title": "Calculation & Verification: Laplace transforms and transfer functions",
      "unit": 1,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Laplace transforms and transfer functions** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>With K=2 rpm/V and \u03c4=0.5 s, a 3 V command gives a final increment 6 rpm; at t=0.5 s the first-order response is 6(1\u2212e\u207b\u00b9)=3.793 rpm.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
    },
    {
      "id": "prob-control-systems-engineering-1-4",
      "title": "Calculation & Verification: Block diagrams, feedback algebra and signal paths",
      "unit": 1,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Block diagrams, feedback algebra and signal paths** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A first-order plant G=1/(s+1) with proportional gain 4 yields T=4/(s+5); DC closed-loop gain is 0.8, not unity.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
    },
    {
      "id": "prob-control-systems-engineering-1-5",
      "title": "Calculation & Verification: Scaling, assumptions, and baseline experiments",
      "unit": 1,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Scaling, assumptions, and baseline experiments** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A measured change from 20\u00b0C toward 60\u00b0C reaches 45.3\u00b0C at approximately one first-order time constant; a later measurement may indicate a second slower thermal mode.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
    },
    {
      "id": "prob-control-systems-engineering-2-1",
      "title": "Calculation & Verification: First-order steps and time constants",
      "unit": 2,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **First-order steps and time constants** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A valve opens and flow increases from 0 to 80 L/min with \u03c4=6 s. At t=12 s, y\u224880(1\u2212e\u207b\u00b2)=69.17 L/min.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
    },
    {
      "id": "prob-control-systems-engineering-2-2",
      "title": "Calculation & Verification: Second-order modes, damping and overshoot",
      "unit": 2,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Second-order modes, damping and overshoot** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>With \u03b6=0.5 and \u03c9_n=8 rad/s, ideal overshoot is \u224816.3%, peak time \u22480.453 s and approximate 2% settling time 1 s.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
    },
    {
      "id": "prob-control-systems-engineering-2-3",
      "title": "Calculation & Verification: Rise time, settling time and specification tradeoffs",
      "unit": 2,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Rise time, settling time and specification tradeoffs** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A servo required to settle within \u00b11\u00b0 after a 20\u00b0 step needs a 5% band relative to the step. It is not the same test as a \u00b12% criterion.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
    },
    {
      "id": "prob-control-systems-engineering-2-4",
      "title": "Calculation & Verification: Pole locations, zeros and transient shape",
      "unit": 2,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Pole locations, zeros and transient shape** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For poles at \u22122\u00b1j6 rad/s, the modal envelope decays as e\u207b\u00b2\u1d57 and the oscillation frequency is 6/(2\u03c0)=0.955 Hz.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
    },
    {
      "id": "prob-control-systems-engineering-2-5",
      "title": "Calculation & Verification: Experimental step tests and system identification",
      "unit": 2,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Experimental step tests and system identification** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>When a 2 V step changes steady temperature by 10\u00b0C, the static gain is 5\u00b0C/V. If the response begins only after 3 s, the delay is approximately 3 s, separate from the thermal time constant.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
    },
    {
      "id": "prob-control-systems-engineering-3-1",
      "title": "Calculation & Verification: Closed-loop characteristic equations",
      "unit": 3,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Closed-loop characteristic equations** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>With G(s)=1/(s(s+2)) and C(s)=K, the characteristic polynomial is s\u00b2+2s+K; K>0 gives stable second-order poles.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
    },
    {
      "id": "prob-control-systems-engineering-3-2",
      "title": "Calculation & Verification: Routh\u2013Hurwitz stability screening",
      "unit": 3,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Routh\u2013Hurwitz stability screening** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For p(s)=s\u00b3+4s\u00b2+5s+K, stable operation for positive K requires 0<K<20. At K=20 the system is marginal and needs further analysis.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
    },
    {
      "id": "prob-control-systems-engineering-3-3",
      "title": "Calculation & Verification: Root locus and gain selection",
      "unit": 3,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Root locus and gain selection** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For 1/(s(s+2)) with gain K, poles solve s\u00b2+2s+K=0. At K=1 the poles coincide at \u22121; for K>1 they are complex with real part \u22121.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
    },
    {
      "id": "prob-control-systems-engineering-3-4",
      "title": "Calculation & Verification: Steady-state error and system type",
      "unit": 3,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Steady-state error and system type** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For G=1/(s+1), C=3 and unity feedback, step reference error tends to 1/(1+3)=0.25. Adding integral action can remove that ideal offset.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
    },
    {
      "id": "prob-control-systems-engineering-3-5",
      "title": "Calculation & Verification: Uncertainty, robustness and actuator limits",
      "unit": 3,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Uncertainty, robustness and actuator limits** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>If a thermal plant gain varies from 1.0 to 1.8\u00b0C/% heater due to airflow, a single nominal controller setting may deliver very different overshoot and settling.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
    },
    {
      "id": "prob-control-systems-engineering-4-1",
      "title": "Calculation & Verification: Sinusoidal steady-state and frequency response",
      "unit": 4,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Sinusoidal steady-state and frequency response** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For G=1/(1+0.5s) at \u03c9=4 rad/s, magnitude=1/\u221a5\u22480.447 and phase=\u2212arctan 2\u2248\u221263.4\u00b0.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
    },
    {
      "id": "prob-control-systems-engineering-4-2",
      "title": "Calculation & Verification: Bode plots, slopes and break frequencies",
      "unit": 4,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Bode plots, slopes and break frequencies** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For a pole at 10 rad/s, \u03c9=10 rad/s gives amplitude 1/\u221a2\u22480.707 and phase \u221245\u00b0 relative to low-frequency gain.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
    },
    {
      "id": "prob-control-systems-engineering-4-3",
      "title": "Calculation & Verification: Nyquist criterion and encirclements",
      "unit": 4,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Nyquist criterion and encirclements** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For L(j\u03c9)=K/(1+j\u03c9\u03c4), positive K and \u03c4 produce phase between 0 and \u221290\u00b0, so the simple unity-feedback loop has no crossing of \u2212180\u00b0.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
    },
    {
      "id": "prob-control-systems-engineering-4-4",
      "title": "Calculation & Verification: Gain margin, phase margin and bandwidth",
      "unit": 4,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Gain margin, phase margin and bandwidth** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>At crossover, a measured open-loop phase of \u2212135\u00b0 implies about 45\u00b0 phase margin. If extra delay adds 0.15 rad at crossover, the margin drops by \u22488.6\u00b0.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
    },
    {
      "id": "prob-control-systems-engineering-4-5",
      "title": "Calculation & Verification: Sensitivity, disturbances and sensor noise",
      "unit": 4,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Sensitivity, disturbances and sensor noise** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>With L(j\u03c9)=9 at a very low frequency, S\u22480.1 and T\u22480.9 for this real loop value. Large high-frequency loop gain instead passes measurement noise into the output.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
    },
    {
      "id": "prob-control-systems-engineering-5-1",
      "title": "Calculation & Verification: Proportional control and closed-loop stiffness",
      "unit": 5,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Proportional control and closed-loop stiffness** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>With K=2, \u03c4=4 s and K_p=1.5, the ideal closed-loop \u03c4 becomes 1 s, while unit-step output tends to 0.75.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
    },
    {
      "id": "prob-control-systems-engineering-5-2",
      "title": "Calculation & Verification: Integral control and PI design",
      "unit": 5,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Integral control and PI design** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For K_p=2 and K_i=0.5 s\u207b\u00b9 in matching normalized units, the PI zero is at \u22120.25 rad/s and integral time is 4 s.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
    },
    {
      "id": "prob-control-systems-engineering-5-3",
      "title": "Calculation & Verification: Derivative action and filtered PID",
      "unit": 5,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Derivative action and filtered PID** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>If measurement increases at 2\u00b0C/s and K_d=0.8 %heater\u00b7s/\u00b0C, ideal derivative-on-measurement requests a \u22121.6 percentage-point command adjustment before filtering.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
    },
    {
      "id": "prob-control-systems-engineering-5-4",
      "title": "Calculation & Verification: Anti-windup, setpoint shaping and bumpless transfer",
      "unit": 5,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Anti-windup, setpoint shaping and bumpless transfer** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A heater with 0\u2013100% command saturates at 100% during a large temperature change; stopping integral accumulation when the same error direction deepens saturation shortens recovery.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
    },
    {
      "id": "prob-control-systems-engineering-5-5",
      "title": "Calculation & Verification: Lead\u2013lag compensation and tuning protocols",
      "unit": 5,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Lead\u2013lag compensation and tuning protocols** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For \u03b1=0.25, maximum ideal phase lead is asin((1\u2212\u03b1)/(1+\u03b1))\u224836.9\u00b0. It occurs near \u03c9\u22481/(T\u221a\u03b1).\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
    },
    {
      "id": "prob-control-systems-engineering-6-1",
      "title": "Calculation & Verification: State variables and linear state models",
      "unit": 6,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **State variables and linear state models** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For m=2 kg, b=4 N\u00b7s/m, k=50 N/m, the state acceleration is \u221225x1\u22122x2+0.5u.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
    },
    {
      "id": "prob-control-systems-engineering-6-2",
      "title": "Calculation & Verification: Controllability and reachable states",
      "unit": 6,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Controllability and reachable states** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For double integrator A=[[0,1],[0,0]] and B=[[0],[1]], controllability matrix [B,AB]=[[0,1],[1,0]], rank 2.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
    },
    {
      "id": "prob-control-systems-engineering-6-3",
      "title": "Calculation & Verification: Observability and sensor selection",
      "unit": 6,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Observability and sensor selection** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For A=[[0,1],[0,0]] and C=[1,0], observability determinant is 1, confirming rank 2.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
    },
    {
      "id": "prob-control-systems-engineering-6-4",
      "title": "Calculation & Verification: State feedback and pole placement",
      "unit": 6,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **State feedback and pole placement** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For double integrator x\u0308=u, u=\u2212k1x\u2212k2x\u0307 produces characteristic s\u00b2+k2s+k1. Desired poles at \u22122 and \u22123 require k2=5 and k1=6.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
    },
    {
      "id": "prob-control-systems-engineering-6-5",
      "title": "Calculation & Verification: Observers, Kalman filtering and estimation",
      "unit": 6,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Observers, Kalman filtering and estimation** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For scalar x\u0307=\u22122x+u, y=x and observer gain L=4, ideal estimation error decays as e\u0307=\u22126e; the error time constant is 1/6 s.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
    },
    {
      "id": "prob-control-systems-engineering-7-1",
      "title": "Calculation & Verification: Sampling rates and zero-order hold",
      "unit": 7,
      "question": "<p><strong>Problem Statement:</strong> </p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For a 5 Hz oscillation, a 12 Hz sample rate barely exceeds the Nyquist threshold; 100 Hz yields twenty samples per cycle and better waveform resolution.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
    },
    {
      "id": "prob-control-systems-engineering-7-2",
      "title": "Calculation & Verification: Discrete-time models and z-transforms",
      "unit": 7,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Discrete-time models and z-transforms** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For \u03c4=2 s and h=0.1 s, a=e\u207b\u2070\u00b7\u2070\u2075\u22480.951229 and the input coefficient for K=3 is \u22480.146312.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
    },
    {
      "id": "prob-control-systems-engineering-7-3",
      "title": "Calculation & Verification: Discrete stability and pole mapping",
      "unit": 7,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Discrete stability and pole mapping** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A pole at s=\u22124 s\u207b\u00b9 with h=0.05 s maps to z=e\u207b\u2070\u00b7\u00b2\u22480.81873, strictly inside the unit circle.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
    },
    {
      "id": "prob-control-systems-engineering-7-4",
      "title": "Calculation & Verification: Digital PI/PID, saturation and computation delay",
      "unit": 7,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Digital PI/PID, saturation and computation delay** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>With K_i=0.4 s\u207b\u00b9, h=0.2 s and e[k]=5 units, one rectangular integrator update adds 0.4 actuator units.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
    },
    {
      "id": "prob-control-systems-engineering-7-5",
      "title": "Calculation & Verification: Quantization, filtering, latency and deployment",
      "unit": 7,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Quantization, filtering, latency and deployment** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A 12-bit ADC over 0\u201310 V has step size 10/4096\u22482.44 mV. A plant with 0.05\u00b0C/mV sensor gain therefore has \u22480.122\u00b0C per code in this synthetic illustration.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
    },
    {
      "id": "prob-control-systems-engineering-8-1",
      "title": "Calculation & Verification: DC motor speed and torque regulation",
      "unit": 8,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **DC motor speed and torque regulation** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For steady state R=2 \u03a9, K_e=0.1 V\u00b7s/rad, K_t=0.1 N\u00b7m/A and b=0.01 N\u00b7m\u00b7s/rad, a 10 V supply produces no-load speed \u224833.3 rad/s in the simplified steady model.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
    },
    {
      "id": "prob-control-systems-engineering-8-2",
      "title": "Calculation & Verification: Thermal chamber temperature regulation",
      "unit": 8,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Thermal chamber temperature regulation** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For C_th=1000 J/K and hA=10 W/K, \u03c4=C_th/(hA)=100 s. At 200 W constant input, ideal steady excess temperature is 20 K.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
    },
    {
      "id": "prob-control-systems-engineering-8-3",
      "title": "Calculation & Verification: Active damping and vibration isolation",
      "unit": 8,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Active damping and vibration isolation** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For m=2 kg, b=1 N\u00b7s/m and k_d=5 N\u00b7s/m, effective damping is 6 N\u00b7s/m in the ideal scalar model.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
    },
    {
      "id": "prob-control-systems-engineering-8-4",
      "title": "Calculation & Verification: Motion control for a positioning axis",
      "unit": 8,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Motion control for a positioning axis** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A stage moving 0.2 m in 1 s has average speed 0.2 m/s, but a smooth start-and-stop trajectory must peak above the average speed. The actuator should be sized for peak acceleration and load.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
    },
    {
      "id": "prob-control-systems-engineering-8-5",
      "title": "Calculation & Verification: Validation, fault response and responsible deployment",
      "unit": 8,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Validation, fault response and responsible deployment** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For a safety interlock that must de-energize in 200 ms, a software polling loop running every 250 ms cannot guarantee compliance even before execution and communication delays.\n\n**Reproduction protocol.** Write the givens and units in a table, compute any derived time scales or gains, substitute into the displayed model and calculate the result with more precision than required for the final reported value. Compare against a limiting case: zero disturbance, zero controller gain, vanishing sample time, or a stationary equilibrium as appropriate. If a calculation predicts infinite control force, negative dissipation, or motion through a hard stop, that is an indication to revisit assumptions, not a valid operating instruction.</p></div>"
    }
  ]
};
if (typeof module !== 'undefined') module.exports = COURSE_DATA;
if (typeof window !== 'undefined') window.COURSE_DATA = COURSE_DATA;
