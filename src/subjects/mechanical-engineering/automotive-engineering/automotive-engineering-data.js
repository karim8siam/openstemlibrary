/* OpenSTEM Course Data: Automotive Engineering (AUT) */
var COURSE_DATA = {
  "code": "AUT",
  "title": "Automotive Engineering",
  "subtitle": "Vehicle Dynamics, Aerodynamic Drag, Powertrain Matching, Braking, Steering, Suspension & EV Powertrains",
  "units": [
    {
      "number": 1,
      "unitNumber": 1,
      "title": "Vehicle Architecture, Requirements and Road Loads",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Vehicle Architecture, Requirements and Road Loads.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Vehicle Architecture, Requirements and Road Loads.",
      "sections": [
        {
          "id": "sec-1-1",
          "title": "Subsystem architecture and engineering requirements",
          "leadSummary": "**Learning objective.** Build a reproducible analysis of **interfaces among packaging, loads, safety, service and propulsion**, then evaluate whether trade packaging flexibility against weight and structural margins. The illustrative field case is **comparing two body architectures**. The primary relation is `System mass = sum of component and payload masses`; it is a starting approximation, not a complete calibration or certification method.",
          "content": "<p>**Learning objective.** Build a reproducible analysis of **interfaces among packaging, loads, safety, service and propulsion**, then evaluate whether trade packaging flexibility against weight and structural margins. The illustrative field case is **comparing two body architectures**. The primary relation is `System mass = sum of component and payload masses`; it is a starting approximation, not a complete calibration or certification method.</p>"
        },
        {
          "id": "sec-1-2",
          "title": "Aerodynamic drag and reference area",
          "leadSummary": "**Learning objective.** Build a reproducible analysis of **pressure and skin-friction losses that rise with the square of air-relative speed**, then evaluate whether weigh drag reduction against cooling airflow. The illustrative field case is **a highway coastdown**. The primary relation is `F_drag = 0.5*rho*Cd*A*v_rel^2`; it is a starting approximation, not a complete calibration or certification method.",
          "content": "<p>**Learning objective.** Build a reproducible analysis of **pressure and skin-friction losses that rise with the square of air-relative speed**, then evaluate whether weigh drag reduction against cooling airflow. The illustrative field case is **a highway coastdown**. The primary relation is `F_drag = 0.5*rho*Cd*A*v_rel^2`; it is a starting approximation, not a complete calibration or certification method.</p>"
        },
        {
          "id": "sec-1-3",
          "title": "Tire rolling resistance",
          "leadSummary": "**Learning objective.** Build a reproducible analysis of **energy dissipated by cyclic tire deformation and contact mechanics**, then evaluate whether balance rolling loss against braking and wet grip. The illustrative field case is **comparing tires at equal inflation pressure**. The primary relation is `F_roll = Crr*m*g*cos(theta)`; it is a starting approximation, not a complete calibration or certification method.",
          "content": "<p>**Learning objective.** Build a reproducible analysis of **energy dissipated by cyclic tire deformation and contact mechanics**, then evaluate whether balance rolling loss against braking and wet grip. The illustrative field case is **comparing tires at equal inflation pressure**. The primary relation is `F_roll = Crr*m*g*cos(theta)`; it is a starting approximation, not a complete calibration or certification method.</p>"
        },
        {
          "id": "sec-1-4",
          "title": "Gradient resistance and payload",
          "leadSummary": "**Learning objective.** Build a reproducible analysis of **gravity component parallel to road surface**, then evaluate whether choose the payload and grade design point. The illustrative field case is **a vehicle climbing an 8% road grade**. The primary relation is `F_grade = m*g*sin(theta)`; it is a starting approximation, not a complete calibration or certification method.",
          "content": "<p>**Learning objective.** Build a reproducible analysis of **gravity component parallel to road surface**, then evaluate whether choose the payload and grade design point. The illustrative field case is **a vehicle climbing an 8% road grade**. The primary relation is `F_grade = m*g*sin(theta)`; it is a starting approximation, not a complete calibration or certification method.</p>"
        },
        {
          "id": "sec-1-5",
          "title": "Drive cycles, road-load calibration and reproducible tests",
          "leadSummary": "**Learning objective.** Build a reproducible analysis of **test schedules, environmental controls and boundary definitions**, then evaluate whether pick a valid measurement protocol. The illustrative field case is **laboratory dynamometer versus route trial**. The primary relation is `Distance = integral of vehicle speed over time`; it is a starting approximation, not a complete calibration or certification method.",
          "content": "<p>**Learning objective.** Build a reproducible analysis of **test schedules, environmental controls and boundary definitions**, then evaluate whether pick a valid measurement protocol. The illustrative field case is **laboratory dynamometer versus route trial**. The primary relation is `Distance = integral of vehicle speed over time`; it is a starting approximation, not a complete calibration or certification method.</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-automotive-engineering-1-1",
          "title": "Calculation & Verification: Subsystem architecture and engineering requirements",
          "unit": 1,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Subsystem architecture and engineering requirements** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>An illustrative 1180 kg body and chassis, 240 kg propulsion and 130 kg fluids and accessories produce 1550 kg curb mass; with 250 kg occupants/cargo, test mass becomes 1800 kg. The distinction prevents computing acceleration using curb mass while measuring consumption with full payload.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
        },
        {
          "id": "prob-automotive-engineering-1-2",
          "title": "Calculation & Verification: Aerodynamic drag and reference area",
          "unit": 1,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Aerodynamic drag and reference area** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>At rho = 1.20 kg/m\u00b3, Cd = 0.29, area = 2.3 m\u00b2 and 25 m/s relative flow, F_drag = 0.5\u00d71.20\u00d70.29\u00d72.3\u00d725\u00b2 = 250.1 N. At 30 m/s under otherwise constant assumptions it becomes about 360.2 N, an increase of roughly 44%.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
        },
        {
          "id": "prob-automotive-engineering-1-3",
          "title": "Calculation & Verification: Tire rolling resistance",
          "unit": 1,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Tire rolling resistance** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For 1600 kg, Crr = 0.010 and level ground, F_roll = 0.010\u00d71600\u00d79.81 = 157.0 N. At 20 m/s the simplified rolling power is 3.14 kW, separate from aerodynamic and drivetrain demands.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
        },
        {
          "id": "prob-automotive-engineering-1-4",
          "title": "Calculation & Verification: Gradient resistance and payload",
          "unit": 1,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Gradient resistance and payload** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>An 8% grade has angle arctan(0.08) \u2248 4.57 degrees. A 1800 kg vehicle requires 1800\u00d79.81\u00d7sin(4.57\u00b0) \u2248 1408 N solely to oppose gravity, before tire drag and aero drag.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
        },
        {
          "id": "prob-automotive-engineering-1-5",
          "title": "Calculation & Verification: Drive cycles, road-load calibration and reproducible tests",
          "unit": 1,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Drive cycles, road-load calibration and reproducible tests** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A 900 s route with constant 15 m/s covers 13.5 km. A second route with alternating stops can cover the same distance but require repeated acceleration energy; equal distance and average speed do not establish equal energy consumption.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
        }
      ]
    },
    {
      "number": 2,
      "unitNumber": 2,
      "title": "Longitudinal Vehicle Dynamics and Performance",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Longitudinal Vehicle Dynamics and Performance.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Longitudinal Vehicle Dynamics and Performance.",
      "sections": [
        {
          "id": "sec-2-1",
          "title": "Whole-vehicle free-body analysis",
          "leadSummary": "**Learning objective.** Build a reproducible analysis of **force accounting on a consistent inertial basis**, then evaluate whether identify required tire force. The illustrative field case is **an accelerating delivery van**. The primary relation is `F_wheel - F_drag - F_roll - F_grade = m*a`; it is a starting approximation, not a complete calibration or certification method.",
          "content": "<p>**Learning objective.** Build a reproducible analysis of **force accounting on a consistent inertial basis**, then evaluate whether identify required tire force. The illustrative field case is **an accelerating delivery van**. The primary relation is `F_wheel - F_drag - F_roll - F_grade = m*a`; it is a starting approximation, not a complete calibration or certification method.</p>"
        },
        {
          "id": "sec-2-2",
          "title": "Power-limited acceleration",
          "leadSummary": "**Learning objective.** Build a reproducible analysis of **traction force versus shaft power as vehicle speed changes**, then evaluate whether choose a feasible motor and gearing envelope. The illustrative field case is **a launch that transitions from tire-limited to power-limited**. The primary relation is `P_wheel = F_wheel*v`; it is a starting approximation, not a complete calibration or certification method.",
          "content": "<p>**Learning objective.** Build a reproducible analysis of **traction force versus shaft power as vehicle speed changes**, then evaluate whether choose a feasible motor and gearing envelope. The illustrative field case is **a launch that transitions from tire-limited to power-limited**. The primary relation is `P_wheel = F_wheel*v`; it is a starting approximation, not a complete calibration or certification method.</p>"
        },
        {
          "id": "sec-2-3",
          "title": "Gradeability and tire traction",
          "leadSummary": "**Learning objective.** Build a reproducible analysis of **traction available from the driven axle or wheel**, then evaluate whether assess uphill launch without wheel slip. The illustrative field case is **a rear-wheel-drive vehicle starting on a hill**. The primary relation is `F_max = mu*F_normal`; it is a starting approximation, not a complete calibration or certification method.",
          "content": "<p>**Learning objective.** Build a reproducible analysis of **traction available from the driven axle or wheel**, then evaluate whether assess uphill launch without wheel slip. The illustrative field case is **a rear-wheel-drive vehicle starting on a hill**. The primary relation is `F_max = mu*F_normal`; it is a starting approximation, not a complete calibration or certification method.</p>"
        },
        {
          "id": "sec-2-4",
          "title": "Relative wind and road-load power",
          "leadSummary": "**Learning objective.** Build a reproducible analysis of **air-relative resistance multiplied by road-relative travel speed**, then evaluate whether select a test speed and wind correction. The illustrative field case is **a highway drive into a sustained headwind**. The primary relation is `P_aero = 0.5*rho*Cd*A*v_rel^2*v_vehicle`; it is a starting approximation, not a complete calibration or certification method.",
          "content": "<p>**Learning objective.** Build a reproducible analysis of **air-relative resistance multiplied by road-relative travel speed**, then evaluate whether select a test speed and wind correction. The illustrative field case is **a highway drive into a sustained headwind**. The primary relation is `P_aero = 0.5*rho*Cd*A*v_rel^2*v_vehicle`; it is a starting approximation, not a complete calibration or certification method.</p>"
        },
        {
          "id": "sec-2-5",
          "title": "Energy consumption and duty-cycle decomposition",
          "leadSummary": "**Learning objective.** Build a reproducible analysis of **positive propulsion work and negative braking work**, then evaluate whether quantify effects of mass versus aerodynamics. The illustrative field case is **stop-and-go courier duty cycle**. The primary relation is `E_wheel = integral(F_wheel*v*dt)`; it is a starting approximation, not a complete calibration or certification method.",
          "content": "<p>**Learning objective.** Build a reproducible analysis of **positive propulsion work and negative braking work**, then evaluate whether quantify effects of mass versus aerodynamics. The illustrative field case is **stop-and-go courier duty cycle**. The primary relation is `E_wheel = integral(F_wheel*v*dt)`; it is a starting approximation, not a complete calibration or certification method.</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-automotive-engineering-2-1",
          "title": "Calculation & Verification: Whole-vehicle free-body analysis",
          "unit": 2,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Whole-vehicle free-body analysis** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For mass 1700 kg, acceleration 1.5 m/s\u00b2 and combined resistance 360 N, F_wheel = 1700\u00d71.5 + 360 = 2910 N. This is a demand, not a claim that the vehicle can actually develop that tire force.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
        },
        {
          "id": "prob-automotive-engineering-2-2",
          "title": "Calculation & Verification: Power-limited acceleration",
          "unit": 2,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Power-limited acceleration** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>To maintain 3000 N wheel force at 20 m/s requires 60 kW at the wheels. At 30 m/s, the same force requires 90 kW, before gearbox and motor losses; a 60 kW-limited design cannot maintain that force.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
        },
        {
          "id": "prob-automotive-engineering-2-3",
          "title": "Calculation & Verification: Gradeability and tire traction",
          "unit": 2,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Gradeability and tire traction** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>If a driven axle supports 8000 N normal load and assumed peak friction is 0.7, the illustrative total longitudinal force bound is 5600 N. The simple product is not a guaranteed tire force on an actual road.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
        },
        {
          "id": "prob-automotive-engineering-2-4",
          "title": "Calculation & Verification: Relative wind and road-load power",
          "unit": 2,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Relative wind and road-load power** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>At F_drag = 300 N and ground speed 25 m/s, road-load power is 7.5 kW, even if relative airflow is faster than 25 m/s because of wind.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
        },
        {
          "id": "prob-automotive-engineering-2-5",
          "title": "Calculation & Verification: Energy consumption and duty-cycle decomposition",
          "unit": 2,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Energy consumption and duty-cycle decomposition** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A 1600 kg vehicle accelerated from rest to 15 m/s gains 0.5\u00d71600\u00d715\u00b2 = 180,000 J = 0.050 kWh of translational kinetic energy. Ideal energy recovery cannot exceed that amount for this single acceleration\u2013braking event.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
        }
      ]
    },
    {
      "number": 3,
      "unitNumber": 3,
      "title": "Engines, Transmissions and Driveline Integration",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Engines, Transmissions and Driveline Integration.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Engines, Transmissions and Driveline Integration.",
      "sections": [
        {
          "id": "sec-3-1",
          "title": "Combustion engine speed\u2013torque and fuel maps",
          "leadSummary": "**Learning objective.** Build a reproducible analysis of **brake torque, rotational speed and fuel demand**, then evaluate whether select a powertrain operating range. The illustrative field case is **a naturally aspirated engine operating off its efficiency island**. The primary relation is `P = T*omega`; it is a starting approximation, not a complete calibration or certification method.",
          "content": "<p>**Learning objective.** Build a reproducible analysis of **brake torque, rotational speed and fuel demand**, then evaluate whether select a powertrain operating range. The illustrative field case is **a naturally aspirated engine operating off its efficiency island**. The primary relation is `P = T*omega`; it is a starting approximation, not a complete calibration or certification method.</p>"
        },
        {
          "id": "sec-3-2",
          "title": "Engine fuel energy and efficiency",
          "leadSummary": "**Learning objective.** Build a reproducible analysis of **chemical input versus shaft work**, then evaluate whether evaluate fuel calibration uncertainty. The illustrative field case is **engine dynamometer fuel flow test**. The primary relation is `eta_brake = P_brake/(m_dot_fuel*LHV)`; it is a starting approximation, not a complete calibration or certification method.",
          "content": "<p>**Learning objective.** Build a reproducible analysis of **chemical input versus shaft work**, then evaluate whether evaluate fuel calibration uncertainty. The illustrative field case is **engine dynamometer fuel flow test**. The primary relation is `eta_brake = P_brake/(m_dot_fuel*LHV)`; it is a starting approximation, not a complete calibration or certification method.</p>"
        },
        {
          "id": "sec-3-3",
          "title": "Gear ratio, wheel speed and road speed",
          "leadSummary": "**Learning objective.** Build a reproducible analysis of **kinematic link between crankshaft and tire contact patch**, then evaluate whether trade launch torque and highway engine speed. The illustrative field case is **manual transmission in a steady gear**. The primary relation is `v = omega_engine*r_wheel/(i_gear*i_final)`; it is a starting approximation, not a complete calibration or certification method.",
          "content": "<p>**Learning objective.** Build a reproducible analysis of **kinematic link between crankshaft and tire contact patch**, then evaluate whether trade launch torque and highway engine speed. The illustrative field case is **manual transmission in a steady gear**. The primary relation is `v = omega_engine*r_wheel/(i_gear*i_final)`; it is a starting approximation, not a complete calibration or certification method.</p>"
        },
        {
          "id": "sec-3-4",
          "title": "Transmission losses and driveline efficiency",
          "leadSummary": "**Learning objective.** Build a reproducible analysis of **torque multiplication with mechanical loss**, then evaluate whether evaluate loss against gearing benefits. The illustrative field case is **a high-load low gear during towing**. The primary relation is `T_wheel = T_engine*i_total*eta_driveline`; it is a starting approximation, not a complete calibration or certification method.",
          "content": "<p>**Learning objective.** Build a reproducible analysis of **torque multiplication with mechanical loss**, then evaluate whether evaluate loss against gearing benefits. The illustrative field case is **a high-load low gear during towing**. The primary relation is `T_wheel = T_engine*i_total*eta_driveline`; it is a starting approximation, not a complete calibration or certification method.</p>"
        },
        {
          "id": "sec-3-5",
          "title": "Hybrid power-split and operating modes",
          "leadSummary": "**Learning objective.** Build a reproducible analysis of **parallel, series and power-split strategies**, then evaluate whether choose a control strategy under battery constraints. The illustrative field case is **a hybrid transitioning from electric launch to engine cruising**. The primary relation is `P_wheel = P_engine_path+P_electric_path-losses`; it is a starting approximation, not a complete calibration or certification method.",
          "content": "<p>**Learning objective.** Build a reproducible analysis of **parallel, series and power-split strategies**, then evaluate whether choose a control strategy under battery constraints. The illustrative field case is **a hybrid transitioning from electric launch to engine cruising**. The primary relation is `P_wheel = P_engine_path+P_electric_path-losses`; it is a starting approximation, not a complete calibration or certification method.</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-automotive-engineering-3-1",
          "title": "Calculation & Verification: Combustion engine speed\u2013torque and fuel maps",
          "unit": 3,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Combustion engine speed\u2013torque and fuel maps** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>At 220 N\u00b7m and 3000 rpm, power = 220\u00d72\u03c0\u00d73000/60 = 69.1 kW. Treat the value as shaft brake power, not wheel power after driveline losses.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
        },
        {
          "id": "prob-automotive-engineering-3-2",
          "title": "Calculation & Verification: Engine fuel energy and efficiency",
          "unit": 3,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Engine fuel energy and efficiency** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>If brake power is 60 kW, fuel flow is 0.004 kg/s and LHV is 43,000 kJ/kg, fuel power is 172 kW; brake thermal efficiency = 60/172 = 34.9%.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
        },
        {
          "id": "prob-automotive-engineering-3-3",
          "title": "Calculation & Verification: Gear ratio, wheel speed and road speed",
          "unit": 3,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Gear ratio, wheel speed and road speed** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>At 2400 rpm engine speed, total reduction 8 and rolling radius 0.31 m, wheel speed is 300 rpm. Ground speed is 2\u03c0\u00d70.31\u00d7300/60 = 9.74 m/s \u2248 35.1 km/h, neglecting slip.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
        },
        {
          "id": "prob-automotive-engineering-3-4",
          "title": "Calculation & Verification: Transmission losses and driveline efficiency",
          "unit": 3,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Transmission losses and driveline efficiency** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>Engine torque 180 N\u00b7m, total ratio 10 and assumed transmission efficiency 0.9 give wheel torque 1620 N\u00b7m. With rolling radius 0.30 m, idealized contact force is 5400 N before tire-traction limits.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
        },
        {
          "id": "prob-automotive-engineering-3-5",
          "title": "Calculation & Verification: Hybrid power-split and operating modes",
          "unit": 3,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Hybrid power-split and operating modes** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>At one operating instant the engine path delivers 32 kW and electric path 18 kW, while aggregate losses are 4 kW; the delivered wheel power is 46 kW. This instantaneous balance is not a combined vehicle power rating.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
        }
      ]
    },
    {
      "number": 4,
      "unitNumber": 4,
      "title": "Braking Systems, Tires and Regenerative Braking",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Braking Systems, Tires and Regenerative Braking.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Braking Systems, Tires and Regenerative Braking.",
      "sections": [
        {
          "id": "sec-4-1",
          "title": "Tire slip and force generation",
          "leadSummary": "**Learning objective.** Build a reproducible analysis of **contact-patch mechanics and traction envelope**, then evaluate whether set conservative validation limits. The illustrative field case is **instrumented hard braking on variable-grip pavement**. The primary relation is `Slip_brake = (v-R*omega_wheel)/max(v,epsilon)`; it is a starting approximation, not a complete calibration or certification method.",
          "content": "<p>**Learning objective.** Build a reproducible analysis of **contact-patch mechanics and traction envelope**, then evaluate whether set conservative validation limits. The illustrative field case is **instrumented hard braking on variable-grip pavement**. The primary relation is `Slip_brake = (v-R*omega_wheel)/max(v,epsilon)`; it is a starting approximation, not a complete calibration or certification method.</p>"
        },
        {
          "id": "sec-4-2",
          "title": "Deceleration force and stopping distance",
          "leadSummary": "**Learning objective.** Build a reproducible analysis of **friction-limited constant-deceleration idealization**, then evaluate whether define a safe test envelope. The illustrative field case is **braking on a straight level surface**. The primary relation is `d = v0^2/(2*mu*g)`; it is a starting approximation, not a complete calibration or certification method.",
          "content": "<p>**Learning objective.** Build a reproducible analysis of **friction-limited constant-deceleration idealization**, then evaluate whether define a safe test envelope. The illustrative field case is **braking on a straight level surface**. The primary relation is `d = v0^2/(2*mu*g)`; it is a starting approximation, not a complete calibration or certification method.</p>"
        },
        {
          "id": "sec-4-3",
          "title": "Brake torque, hydraulic systems and thermal energy",
          "leadSummary": "**Learning objective.** Build a reproducible analysis of **friction brake heat and thermal stress**, then evaluate whether size ventilation and thermal test requirements. The illustrative field case is **repeated descents with heavy payload**. The primary relation is `Delta_Ek = 0.5*m*(v1^2-v2^2)`; it is a starting approximation, not a complete calibration or certification method.",
          "content": "<p>**Learning objective.** Build a reproducible analysis of **friction brake heat and thermal stress**, then evaluate whether size ventilation and thermal test requirements. The illustrative field case is **repeated descents with heavy payload**. The primary relation is `Delta_Ek = 0.5*m*(v1^2-v2^2)`; it is a starting approximation, not a complete calibration or certification method.</p>"
        },
        {
          "id": "sec-4-4",
          "title": "Anti-lock braking and wheel-speed estimation",
          "leadSummary": "**Learning objective.** Build a reproducible analysis of **feedback modulation of brake pressure to manage slip**, then evaluate whether validate sensing and fault-handling. The illustrative field case is **emergency stop over a surface transition**. The primary relation is `Wheel angular acceleration = d(omega_wheel)/dt`; it is a starting approximation, not a complete calibration or certification method.",
          "content": "<p>**Learning objective.** Build a reproducible analysis of **feedback modulation of brake pressure to manage slip**, then evaluate whether validate sensing and fault-handling. The illustrative field case is **emergency stop over a surface transition**. The primary relation is `Wheel angular acceleration = d(omega_wheel)/dt`; it is a starting approximation, not a complete calibration or certification method.</p>"
        },
        {
          "id": "sec-4-5",
          "title": "Regenerative and friction brake coordination",
          "leadSummary": "**Learning objective.** Build a reproducible analysis of **recoverable braking energy with power and battery limits**, then evaluate whether design consistent pedal response. The illustrative field case is **hybrid braking with a nearly full battery**. The primary relation is `E_recovered <= eta_regen*Delta_Ek`; it is a starting approximation, not a complete calibration or certification method.",
          "content": "<p>**Learning objective.** Build a reproducible analysis of **recoverable braking energy with power and battery limits**, then evaluate whether design consistent pedal response. The illustrative field case is **hybrid braking with a nearly full battery**. The primary relation is `E_recovered <= eta_regen*Delta_Ek`; it is a starting approximation, not a complete calibration or certification method.</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-automotive-engineering-4-1",
          "title": "Calculation & Verification: Tire slip and force generation",
          "unit": 4,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Tire slip and force generation** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A vehicle travels at 20 m/s while wheel rim equivalent speed is 16 m/s. The idealized braking slip is (20\u221216)/20 = 0.20, or 20%. It is not automatically the optimal slip for that tire or surface.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
        },
        {
          "id": "prob-automotive-engineering-4-2",
          "title": "Calculation & Verification: Deceleration force and stopping distance",
          "unit": 4,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Deceleration force and stopping distance** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>At 20 m/s and mu = 0.7 on level ground, idealized braking distance = 400/(2\u00d70.7\u00d79.81) = 29.1 m. A 1.2 s driver response adds 24 m before braking begins.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
        },
        {
          "id": "prob-automotive-engineering-4-3",
          "title": "Calculation & Verification: Brake torque, hydraulic systems and thermal energy",
          "unit": 4,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Brake torque, hydraulic systems and thermal energy** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>An 1800 kg vehicle decelerated from 25 to 5 m/s loses 0.5\u00d71800\u00d7(625\u221225) = 540 kJ of translational energy, ignoring rotational inertia. If dissipated in four brake assemblies equally, the average is 135 kJ each, but real axle distribution is unequal.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
        },
        {
          "id": "prob-automotive-engineering-4-4",
          "title": "Calculation & Verification: Anti-lock braking and wheel-speed estimation",
          "unit": 4,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Anti-lock braking and wheel-speed estimation** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A wheel-speed signal changes from 65 to 45 rad/s over 0.10 s. The mean angular acceleration is (45\u221265)/0.10 = \u2212200 rad/s\u00b2. The value is a signal-level diagnostic; it does not alone determine road friction.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
        },
        {
          "id": "prob-automotive-engineering-4-5",
          "title": "Calculation & Verification: Regenerative and friction brake coordination",
          "unit": 4,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Regenerative and friction brake coordination** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For 0.15 kWh available wheel braking energy and a hypothetical combined conversion factor of 0.60, recoverable battery energy is at most 0.09 kWh, before any further state-of-charge restrictions.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
        }
      ]
    },
    {
      "number": 5,
      "unitNumber": 5,
      "title": "Steering, Handling and Vehicle Stability",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Steering, Handling and Vehicle Stability.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Steering, Handling and Vehicle Stability.",
      "sections": [
        {
          "id": "sec-5-1",
          "title": "Bicycle model and lateral acceleration",
          "leadSummary": "**Learning objective.** Build a reproducible analysis of **kinematic curvature and tire-force requirement**, then evaluate whether choose speed during tests. The illustrative field case is **a constant-radius corner at moderate speed**. The primary relation is `a_y = v^2/R`; it is a starting approximation, not a complete calibration or certification method.",
          "content": "<p>**Learning objective.** Build a reproducible analysis of **kinematic curvature and tire-force requirement**, then evaluate whether choose speed during tests. The illustrative field case is **a constant-radius corner at moderate speed**. The primary relation is `a_y = v^2/R`; it is a starting approximation, not a complete calibration or certification method.</p>"
        },
        {
          "id": "sec-5-2",
          "title": "Steering geometry and turning radius",
          "leadSummary": "**Learning objective.** Build a reproducible analysis of **low-speed steering kinematics**, then evaluate whether compare geometry and driver effort. The illustrative field case is **vehicle maneuvering through a narrow turn**. The primary relation is `delta = atan(L/R)`; it is a starting approximation, not a complete calibration or certification method.",
          "content": "<p>**Learning objective.** Build a reproducible analysis of **low-speed steering kinematics**, then evaluate whether compare geometry and driver effort. The illustrative field case is **vehicle maneuvering through a narrow turn**. The primary relation is `delta = atan(L/R)`; it is a starting approximation, not a complete calibration or certification method.</p>"
        },
        {
          "id": "sec-5-3",
          "title": "Understeer, oversteer and yaw response",
          "leadSummary": "**Learning objective.** Build a reproducible analysis of **yaw rate and cornering balance**, then evaluate whether set stable handling targets. The illustrative field case is **steering step and constant-radius tests**. The primary relation is `r_ideal = v/R`; it is a starting approximation, not a complete calibration or certification method.",
          "content": "<p>**Learning objective.** Build a reproducible analysis of **yaw rate and cornering balance**, then evaluate whether set stable handling targets. The illustrative field case is **steering step and constant-radius tests**. The primary relation is `r_ideal = v/R`; it is a starting approximation, not a complete calibration or certification method.</p>"
        },
        {
          "id": "sec-5-4",
          "title": "Load transfer, roll and stability margins",
          "leadSummary": "**Learning objective.** Build a reproducible analysis of **simplified lateral axle load transfer**, then evaluate whether set a stability test plan. The illustrative field case is **a tall vehicle entering a sharp bend**. The primary relation is `Delta_Fz_axle \u2248 m*a_y*h/t`; it is a starting approximation, not a complete calibration or certification method.",
          "content": "<p>**Learning objective.** Build a reproducible analysis of **simplified lateral axle load transfer**, then evaluate whether set a stability test plan. The illustrative field case is **a tall vehicle entering a sharp bend**. The primary relation is `Delta_Fz_axle \u2248 m*a_y*h/t`; it is a starting approximation, not a complete calibration or certification method.</p>"
        },
        {
          "id": "sec-5-5",
          "title": "Steering tests and handling model validation",
          "leadSummary": "**Learning objective.** Build a reproducible analysis of **model residuals versus measured yaw and speed**, then evaluate whether qualify operating envelope. The illustrative field case is **double lane-change test with sensor logs**. The primary relation is `Error(t) = r_measured(t) - r_model(t)`; it is a starting approximation, not a complete calibration or certification method.",
          "content": "<p>**Learning objective.** Build a reproducible analysis of **model residuals versus measured yaw and speed**, then evaluate whether qualify operating envelope. The illustrative field case is **double lane-change test with sensor logs**. The primary relation is `Error(t) = r_measured(t) - r_model(t)`; it is a starting approximation, not a complete calibration or certification method.</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-automotive-engineering-5-1",
          "title": "Calculation & Verification: Bicycle model and lateral acceleration",
          "unit": 5,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Bicycle model and lateral acceleration** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>At 15 m/s on a 75 m radius, lateral acceleration = 15\u00b2/75 = 3.0 m/s\u00b2 \u2248 0.306 g. At 20 m/s on the same radius the ideal value rises to 5.33 m/s\u00b2.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
        },
        {
          "id": "prob-automotive-engineering-5-2",
          "title": "Calculation & Verification: Steering geometry and turning radius",
          "unit": 5,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Steering geometry and turning radius** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For wheelbase L = 2.7 m and turn radius R = 9 m, idealized bicycle steer angle = atan(2.7/9) = 16.70 degrees at the road wheel, not necessarily at the steering wheel.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
        },
        {
          "id": "prob-automotive-engineering-5-3",
          "title": "Calculation & Verification: Understeer, oversteer and yaw response",
          "unit": 5,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Understeer, oversteer and yaw response** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>At v = 12 m/s and radius 60 m the ideal yaw rate is r = 0.20 rad/s = 11.46 deg/s. A sensed rate differing from this ideal could arise from path-radius error, slip, or instrumentation.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
        },
        {
          "id": "prob-automotive-engineering-5-4",
          "title": "Calculation & Verification: Load transfer, roll and stability margins",
          "unit": 5,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Load transfer, roll and stability margins** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For 1600 kg, 3 m/s\u00b2 lateral acceleration, 0.55 m CG height and track width 1.6 m, simple transfer is 1650 N side-to-side across an idealized axle representation. The distribution across front and rear requires more data.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
        },
        {
          "id": "prob-automotive-engineering-5-5",
          "title": "Calculation & Verification: Steering tests and handling model validation",
          "unit": 5,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Steering tests and handling model validation** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>At one sample the measured yaw rate is 0.24 rad/s and prediction is 0.20 rad/s; residual = +0.04 rad/s. Determine whether the sign persists over the maneuver before retuning a parameter.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
        }
      ]
    },
    {
      "number": 6,
      "unitNumber": 6,
      "title": "Suspension, Ride Comfort and NVH",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Suspension, Ride Comfort and NVH.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Suspension, Ride Comfort and NVH.",
      "sections": [
        {
          "id": "sec-6-1",
          "title": "Springs, damping and ride response",
          "leadSummary": "**Learning objective.** Build a reproducible analysis of **second-order ride dynamic response**, then evaluate whether find a compromise ride calibration. The illustrative field case is **vehicle body moving over a shallow road bump**. The primary relation is `m*x_ddot + c*x_dot + k*x = F_road(t)`; it is a starting approximation, not a complete calibration or certification method.",
          "content": "<p>**Learning objective.** Build a reproducible analysis of **second-order ride dynamic response**, then evaluate whether find a compromise ride calibration. The illustrative field case is **vehicle body moving over a shallow road bump**. The primary relation is `m*x_ddot + c*x_dot + k*x = F_road(t)`; it is a starting approximation, not a complete calibration or certification method.</p>"
        },
        {
          "id": "sec-6-2",
          "title": "Quarter-car frequency and damping ratio",
          "leadSummary": "**Learning objective.** Build a reproducible analysis of **sprung-mass bounce frequency**, then evaluate whether study frequency shift with payload. The illustrative field case is **loaded versus unloaded suspension tuning**. The primary relation is `f_n = sqrt(k/m)/(2*pi)`; it is a starting approximation, not a complete calibration or certification method.",
          "content": "<p>**Learning objective.** Build a reproducible analysis of **sprung-mass bounce frequency**, then evaluate whether study frequency shift with payload. The illustrative field case is **loaded versus unloaded suspension tuning**. The primary relation is `f_n = sqrt(k/m)/(2*pi)`; it is a starting approximation, not a complete calibration or certification method.</p>"
        },
        {
          "id": "sec-6-3",
          "title": "Unsprung mass and wheel hop",
          "leadSummary": "**Learning objective.** Build a reproducible analysis of **interaction between tire, wheel and suspension**, then evaluate whether balance lightweight wheels against durability. The illustrative field case is **rough-road wheel load fluctuations**. The primary relation is `m_u*z_u_ddot = k_t(z_road-z_u)-k_s(z_u-z_s)-c(z_u_dot-z_s_dot)`; it is a starting approximation, not a complete calibration or certification method.",
          "content": "<p>**Learning objective.** Build a reproducible analysis of **interaction between tire, wheel and suspension**, then evaluate whether balance lightweight wheels against durability. The illustrative field case is **rough-road wheel load fluctuations**. The primary relation is `m_u*z_u_ddot = k_t(z_road-z_u)-k_s(z_u-z_s)-c(z_u_dot-z_s_dot)`; it is a starting approximation, not a complete calibration or certification method.</p>"
        },
        {
          "id": "sec-6-4",
          "title": "Longitudinal load transfer and geometry",
          "leadSummary": "**Learning objective.** Build a reproducible analysis of **pitching moment and axle normal forces**, then evaluate whether tune brake bias and suspension. The illustrative field case is **hard braking with high center of gravity**. The primary relation is `Delta_F_axle = m*a_x*h/L`; it is a starting approximation, not a complete calibration or certification method.",
          "content": "<p>**Learning objective.** Build a reproducible analysis of **pitching moment and axle normal forces**, then evaluate whether tune brake bias and suspension. The illustrative field case is **hard braking with high center of gravity**. The primary relation is `Delta_F_axle = m*a_x*h/L`; it is a starting approximation, not a complete calibration or certification method.</p>"
        },
        {
          "id": "sec-6-5",
          "title": "Noise, vibration and harshness pathways",
          "leadSummary": "**Learning objective.** Build a reproducible analysis of **rotational excitation orders and structural response**, then evaluate whether plan an NVH instrumentation campaign. The illustrative field case is **cabin boom correlated with drivetrain rotational speed**. The primary relation is `f = rpm*order/60`; it is a starting approximation, not a complete calibration or certification method.",
          "content": "<p>**Learning objective.** Build a reproducible analysis of **rotational excitation orders and structural response**, then evaluate whether plan an NVH instrumentation campaign. The illustrative field case is **cabin boom correlated with drivetrain rotational speed**. The primary relation is `f = rpm*order/60`; it is a starting approximation, not a complete calibration or certification method.</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-automotive-engineering-6-1",
          "title": "Calculation & Verification: Springs, damping and ride response",
          "unit": 6,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Springs, damping and ride response** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A spring under 4000 N static load with k = 25,000 N/m deflects x = 4000/25000 = 0.160 m in the linear model. Real mounting geometry changes wheel rate.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
        },
        {
          "id": "prob-automotive-engineering-6-2",
          "title": "Calculation & Verification: Quarter-car frequency and damping ratio",
          "unit": 6,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Quarter-car frequency and damping ratio** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>With k = 20,000 N/m and sprung mass = 300 kg, f_n = sqrt(20000/300)/(2\u03c0) \u2248 1.30 Hz. Increasing sprung mass to 375 kg lowers it to about 1.16 Hz.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
        },
        {
          "id": "prob-automotive-engineering-6-3",
          "title": "Calculation & Verification: Unsprung mass and wheel hop",
          "unit": 6,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Unsprung mass and wheel hop** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>If unsprung mass is 40 kg and tire stiffness is 180,000 N/m, the isolated wheel-hop frequency estimate sqrt(180000/40)/(2\u03c0) \u2248 10.68 Hz; coupling shifts the actual modes.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
        },
        {
          "id": "prob-automotive-engineering-6-4",
          "title": "Calculation & Verification: Longitudinal load transfer and geometry",
          "unit": 6,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Longitudinal load transfer and geometry** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For 1800 kg, longitudinal deceleration 5 m/s\u00b2, center-of-gravity height 0.55 m and wheelbase 2.8 m, frontward load transfer is (1800\u00d75\u00d70.55)/2.8 \u2248 1768 N.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
        },
        {
          "id": "prob-automotive-engineering-6-5",
          "title": "Calculation & Verification: Noise, vibration and harshness pathways",
          "unit": 6,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Noise, vibration and harshness pathways** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A second-order disturbance at shaft speed 1800 rpm has frequency 2\u00d71800/60 = 60 Hz. Reducing the shaft speed to 1500 rpm shifts its second-order excitation to 50 Hz.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
        }
      ]
    },
    {
      "number": 7,
      "unitNumber": 7,
      "title": "Electric and Hybrid Vehicle Energy Systems",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Electric and Hybrid Vehicle Energy Systems.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Electric and Hybrid Vehicle Energy Systems.",
      "sections": [
        {
          "id": "sec-7-1",
          "title": "Electric traction motor torque and inverter limits",
          "leadSummary": "**Learning objective.** Build a reproducible analysis of **motor torque-speed envelope and electrical losses**, then evaluate whether map continuous versus short-duration output. The illustrative field case is **EV acceleration during a battery-limited maneuver**. The primary relation is `P_mech = T*omega`; it is a starting approximation, not a complete calibration or certification method.",
          "content": "<p>**Learning objective.** Build a reproducible analysis of **motor torque-speed envelope and electrical losses**, then evaluate whether map continuous versus short-duration output. The illustrative field case is **EV acceleration during a battery-limited maneuver**. The primary relation is `P_mech = T*omega`; it is a starting approximation, not a complete calibration or certification method.</p>"
        },
        {
          "id": "sec-7-2",
          "title": "Battery capacity, usable window and vehicle range",
          "leadSummary": "**Learning objective.** Build a reproducible analysis of **energy content, auxiliary use and road demand**, then evaluate whether evaluate route-based reserve energy. The illustrative field case is **cold-weather range planning**. The primary relation is `Range_km = usable_kWh/(kWh_per_km)`; it is a starting approximation, not a complete calibration or certification method.",
          "content": "<p>**Learning objective.** Build a reproducible analysis of **energy content, auxiliary use and road demand**, then evaluate whether evaluate route-based reserve energy. The illustrative field case is **cold-weather range planning**. The primary relation is `Range_km = usable_kWh/(kWh_per_km)`; it is a starting approximation, not a complete calibration or certification method.</p>"
        },
        {
          "id": "sec-7-3",
          "title": "Battery internal resistance and thermal management",
          "leadSummary": "**Learning objective.** Build a reproducible analysis of **electrothermal coupling and cell protection**, then evaluate whether design a safe cooling evaluation. The illustrative field case is **high-current acceleration in warm ambient air**. The primary relation is `P_heat = I^2*R`; it is a starting approximation, not a complete calibration or certification method.",
          "content": "<p>**Learning objective.** Build a reproducible analysis of **electrothermal coupling and cell protection**, then evaluate whether design a safe cooling evaluation. The illustrative field case is **high-current acceleration in warm ambient air**. The primary relation is `P_heat = I^2*R`; it is a starting approximation, not a complete calibration or certification method.</p>"
        },
        {
          "id": "sec-7-4",
          "title": "Charging power, efficiency and taper",
          "leadSummary": "**Learning objective.** Build a reproducible analysis of **energy delivery boundary and current limits**, then evaluate whether plan fleet charging turnaround. The illustrative field case is **fast charging near high state of charge**. The primary relation is `t_ideal = Delta_E/(P_charger*eta_charge)`; it is a starting approximation, not a complete calibration or certification method.",
          "content": "<p>**Learning objective.** Build a reproducible analysis of **energy delivery boundary and current limits**, then evaluate whether plan fleet charging turnaround. The illustrative field case is **fast charging near high state of charge**. The primary relation is `t_ideal = Delta_E/(P_charger*eta_charge)`; it is a starting approximation, not a complete calibration or certification method.</p>"
        },
        {
          "id": "sec-7-5",
          "title": "Hybrid and EV system-level comparison",
          "leadSummary": "**Learning objective.** Build a reproducible analysis of **boundaries for efficiency and life-cycle assessment**, then evaluate whether select evidence-based technology for a service. The illustrative field case is **comparing EV and hybrid on a mixed-duty fleet**. The primary relation is `E_wall = E_pack/eta_charging`; it is a starting approximation, not a complete calibration or certification method.",
          "content": "<p>**Learning objective.** Build a reproducible analysis of **boundaries for efficiency and life-cycle assessment**, then evaluate whether select evidence-based technology for a service. The illustrative field case is **comparing EV and hybrid on a mixed-duty fleet**. The primary relation is `E_wall = E_pack/eta_charging`; it is a starting approximation, not a complete calibration or certification method.</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-automotive-engineering-7-1",
          "title": "Calculation & Verification: Electric traction motor torque and inverter limits",
          "unit": 7,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Electric traction motor torque and inverter limits** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>At torque 280 N\u00b7m and 4000 rpm, mechanical shaft power is 280\u00d72\u03c0\u00d74000/60 = 117.3 kW. This says nothing about continuous rating without cooling and duty-cycle information.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
        },
        {
          "id": "prob-automotive-engineering-7-2",
          "title": "Calculation & Verification: Battery capacity, usable window and vehicle range",
          "unit": 7,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Battery capacity, usable window and vehicle range** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For 62 kWh usable energy and assumed average 0.18 kWh/km pack consumption, model range = 62/0.18 = 344 km before reserve and unforeseen conditions. A 10 kWh reserve changes the planned-distance estimate to 52/0.18 = 289 km.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
        },
        {
          "id": "prob-automotive-engineering-7-3",
          "title": "Calculation & Verification: Battery internal resistance and thermal management",
          "unit": 7,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Battery internal resistance and thermal management** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For a hypothetical current of 200 A and effective series resistance 0.05 ohm, ohmic heating is 200\u00b2\u00d70.05 = 2000 W. This is a simplified pack-level resistance example; actual heat generation may differ.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
        },
        {
          "id": "prob-automotive-engineering-7-4",
          "title": "Calculation & Verification: Charging power, efficiency and taper",
          "unit": 7,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Charging power, efficiency and taper** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>Delivering 30 kWh into the pack at constant 50 kW input and 90% overall efficiency would take 30/(50\u00d70.9) = 0.667 h = 40 minutes. Power taper or thermal protection would lengthen the actual session.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
        },
        {
          "id": "prob-automotive-engineering-7-5",
          "title": "Calculation & Verification: Hybrid and EV system-level comparison",
          "unit": 7,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Hybrid and EV system-level comparison** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>At 18 kWh/100 km drawn from the pack and 90% charging efficiency, wall consumption is 20 kWh/100 km; the 2 kWh difference is a conversion loss, not a change in road work.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
        }
      ]
    },
    {
      "number": 8,
      "unitNumber": 8,
      "title": "Automotive Controls, Safety and Validation",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Automotive Controls, Safety and Validation.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Automotive Controls, Safety and Validation.",
      "sections": [
        {
          "id": "sec-8-1",
          "title": "Sensors, embedded software and control loops",
          "leadSummary": "**Learning objective.** Build a reproducible analysis of **observability and actuator constraints**, then evaluate whether set diagnostics and fallback requirements. The illustrative field case is **wheel-speed sensors and steering angle sensors in a controller**. The primary relation is `Measurement = physical signal + bias + noise`; it is a starting approximation, not a complete calibration or certification method.",
          "content": "<p>**Learning objective.** Build a reproducible analysis of **observability and actuator constraints**, then evaluate whether set diagnostics and fallback requirements. The illustrative field case is **wheel-speed sensors and steering angle sensors in a controller**. The primary relation is `Measurement = physical signal + bias + noise`; it is a starting approximation, not a complete calibration or certification method.</p>"
        },
        {
          "id": "sec-8-2",
          "title": "On-board diagnostics and failure analysis",
          "leadSummary": "**Learning objective.** Build a reproducible analysis of **fault signatures and traceable service evidence**, then evaluate whether design tests that distinguish sensor, wiring and physics. The illustrative field case is **intermittent wheel-speed signal dropout**. The primary relation is `Residual = measured - predicted`; it is a starting approximation, not a complete calibration or certification method.",
          "content": "<p>**Learning objective.** Build a reproducible analysis of **fault signatures and traceable service evidence**, then evaluate whether design tests that distinguish sensor, wiring and physics. The illustrative field case is **intermittent wheel-speed signal dropout**. The primary relation is `Residual = measured - predicted`; it is a starting approximation, not a complete calibration or certification method.</p>"
        },
        {
          "id": "sec-8-3",
          "title": "Functional safety, hazards and fault containment",
          "leadSummary": "**Learning objective.** Build a reproducible analysis of **systematic hazard study and safety requirements**, then evaluate whether define safe states and traceability. The illustrative field case is **unintended propulsion torque scenario**. The primary relation is `Risk analysis = severity + exposure + controllability assessment`; it is a starting approximation, not a complete calibration or certification method.",
          "content": "<p>**Learning objective.** Build a reproducible analysis of **systematic hazard study and safety requirements**, then evaluate whether define safe states and traceability. The illustrative field case is **unintended propulsion torque scenario**. The primary relation is `Risk analysis = severity + exposure + controllability assessment`; it is a starting approximation, not a complete calibration or certification method.</p>"
        },
        {
          "id": "sec-8-4",
          "title": "Crashworthiness, occupant protection and restraint systems",
          "leadSummary": "**Learning objective.** Build a reproducible analysis of **collision momentum change and energy management**, then evaluate whether plan independent occupant-protection testing. The illustrative field case is **low-speed sled laboratory exercise with surrogate masses**. The primary relation is `Impulse = integral(force dt) = Delta_p`; it is a starting approximation, not a complete calibration or certification method.",
          "content": "<p>**Learning objective.** Build a reproducible analysis of **collision momentum change and energy management**, then evaluate whether plan independent occupant-protection testing. The illustrative field case is **low-speed sled laboratory exercise with surrogate masses**. The primary relation is `Impulse = integral(force dt) = Delta_p`; it is a starting approximation, not a complete calibration or certification method.</p>"
        },
        {
          "id": "sec-8-5",
          "title": "Vehicle validation, homologation and engineering reports",
          "leadSummary": "**Learning objective.** Build a reproducible analysis of **traceability of requirements, tests and uncertainty**, then evaluate whether create evidence-based release gates. The illustrative field case is **pre-production verification across temperature and payload**. The primary relation is `Metric_error = abs(measurement-prediction)`; it is a starting approximation, not a complete calibration or certification method.",
          "content": "<p>**Learning objective.** Build a reproducible analysis of **traceability of requirements, tests and uncertainty**, then evaluate whether create evidence-based release gates. The illustrative field case is **pre-production verification across temperature and payload**. The primary relation is `Metric_error = abs(measurement-prediction)`; it is a starting approximation, not a complete calibration or certification method.</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-automotive-engineering-8-1",
          "title": "Calculation & Verification: Sensors, embedded software and control loops",
          "unit": 8,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Sensors, embedded software and control loops** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A sensor reports vehicle speed 21.3 m/s while an independent reference is 20.0 m/s. Its instantaneous error is +1.3 m/s or +6.5% relative to reference; repeat measurements are needed to separate calibration bias and noise.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
        },
        {
          "id": "prob-automotive-engineering-8-2",
          "title": "Calculation & Verification: On-board diagnostics and failure analysis",
          "unit": 8,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **On-board diagnostics and failure analysis** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A model predicts 48 km/h while measured speed is 52 km/h; residual = +4 km/h. A repeated +4 km/h bias over multiple speeds suggests a different cause than random \u00b14 km/h noise.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
        },
        {
          "id": "prob-automotive-engineering-8-3",
          "title": "Calculation & Verification: Functional safety, hazards and fault containment",
          "unit": 8,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Functional safety, hazards and fault containment** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>If a controller commands 100 N\u00b7m while a monitor independently estimates 160 N\u00b7m, the discrepancy is 60 N\u00b7m. That signal difference warrants investigation, not an automatic conclusion about a safe tolerance.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
        },
        {
          "id": "prob-automotive-engineering-8-4",
          "title": "Calculation & Verification: Crashworthiness, occupant protection and restraint systems",
          "unit": 8,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Crashworthiness, occupant protection and restraint systems** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>An 80 kg surrogate whose speed changes by 10 m/s has momentum change 800 N\u00b7s. Over an illustrative 0.10 s stopping interval the average net force magnitude is 8000 N, but this is not an injury prediction.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
        },
        {
          "id": "prob-automotive-engineering-8-5",
          "title": "Calculation & Verification: Vehicle validation, homologation and engineering reports",
          "unit": 8,
          "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Vehicle validation, homologation and engineering reports** under steady operational loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For a requirement that test mass be within \u00b120 kg of 1800 kg, a measured 1826 kg fails the specified tolerance by 6 kg, regardless of whether other performance results looked favorable.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
        }
      ]
    }
  ],
  "problems": [
    {
      "id": "prob-automotive-engineering-1-1",
      "title": "Calculation & Verification: Subsystem architecture and engineering requirements",
      "unit": 1,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Subsystem architecture and engineering requirements** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>An illustrative 1180 kg body and chassis, 240 kg propulsion and 130 kg fluids and accessories produce 1550 kg curb mass; with 250 kg occupants/cargo, test mass becomes 1800 kg. The distinction prevents computing acceleration using curb mass while measuring consumption with full payload.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
    },
    {
      "id": "prob-automotive-engineering-1-2",
      "title": "Calculation & Verification: Aerodynamic drag and reference area",
      "unit": 1,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Aerodynamic drag and reference area** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>At rho = 1.20 kg/m\u00b3, Cd = 0.29, area = 2.3 m\u00b2 and 25 m/s relative flow, F_drag = 0.5\u00d71.20\u00d70.29\u00d72.3\u00d725\u00b2 = 250.1 N. At 30 m/s under otherwise constant assumptions it becomes about 360.2 N, an increase of roughly 44%.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
    },
    {
      "id": "prob-automotive-engineering-1-3",
      "title": "Calculation & Verification: Tire rolling resistance",
      "unit": 1,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Tire rolling resistance** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For 1600 kg, Crr = 0.010 and level ground, F_roll = 0.010\u00d71600\u00d79.81 = 157.0 N. At 20 m/s the simplified rolling power is 3.14 kW, separate from aerodynamic and drivetrain demands.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
    },
    {
      "id": "prob-automotive-engineering-1-4",
      "title": "Calculation & Verification: Gradient resistance and payload",
      "unit": 1,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Gradient resistance and payload** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>An 8% grade has angle arctan(0.08) \u2248 4.57 degrees. A 1800 kg vehicle requires 1800\u00d79.81\u00d7sin(4.57\u00b0) \u2248 1408 N solely to oppose gravity, before tire drag and aero drag.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
    },
    {
      "id": "prob-automotive-engineering-1-5",
      "title": "Calculation & Verification: Drive cycles, road-load calibration and reproducible tests",
      "unit": 1,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Drive cycles, road-load calibration and reproducible tests** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A 900 s route with constant 15 m/s covers 13.5 km. A second route with alternating stops can cover the same distance but require repeated acceleration energy; equal distance and average speed do not establish equal energy consumption.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
    },
    {
      "id": "prob-automotive-engineering-2-1",
      "title": "Calculation & Verification: Whole-vehicle free-body analysis",
      "unit": 2,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Whole-vehicle free-body analysis** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For mass 1700 kg, acceleration 1.5 m/s\u00b2 and combined resistance 360 N, F_wheel = 1700\u00d71.5 + 360 = 2910 N. This is a demand, not a claim that the vehicle can actually develop that tire force.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
    },
    {
      "id": "prob-automotive-engineering-2-2",
      "title": "Calculation & Verification: Power-limited acceleration",
      "unit": 2,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Power-limited acceleration** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>To maintain 3000 N wheel force at 20 m/s requires 60 kW at the wheels. At 30 m/s, the same force requires 90 kW, before gearbox and motor losses; a 60 kW-limited design cannot maintain that force.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
    },
    {
      "id": "prob-automotive-engineering-2-3",
      "title": "Calculation & Verification: Gradeability and tire traction",
      "unit": 2,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Gradeability and tire traction** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>If a driven axle supports 8000 N normal load and assumed peak friction is 0.7, the illustrative total longitudinal force bound is 5600 N. The simple product is not a guaranteed tire force on an actual road.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
    },
    {
      "id": "prob-automotive-engineering-2-4",
      "title": "Calculation & Verification: Relative wind and road-load power",
      "unit": 2,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Relative wind and road-load power** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>At F_drag = 300 N and ground speed 25 m/s, road-load power is 7.5 kW, even if relative airflow is faster than 25 m/s because of wind.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
    },
    {
      "id": "prob-automotive-engineering-2-5",
      "title": "Calculation & Verification: Energy consumption and duty-cycle decomposition",
      "unit": 2,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Energy consumption and duty-cycle decomposition** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A 1600 kg vehicle accelerated from rest to 15 m/s gains 0.5\u00d71600\u00d715\u00b2 = 180,000 J = 0.050 kWh of translational kinetic energy. Ideal energy recovery cannot exceed that amount for this single acceleration\u2013braking event.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
    },
    {
      "id": "prob-automotive-engineering-3-1",
      "title": "Calculation & Verification: Combustion engine speed\u2013torque and fuel maps",
      "unit": 3,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Combustion engine speed\u2013torque and fuel maps** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>At 220 N\u00b7m and 3000 rpm, power = 220\u00d72\u03c0\u00d73000/60 = 69.1 kW. Treat the value as shaft brake power, not wheel power after driveline losses.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
    },
    {
      "id": "prob-automotive-engineering-3-2",
      "title": "Calculation & Verification: Engine fuel energy and efficiency",
      "unit": 3,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Engine fuel energy and efficiency** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>If brake power is 60 kW, fuel flow is 0.004 kg/s and LHV is 43,000 kJ/kg, fuel power is 172 kW; brake thermal efficiency = 60/172 = 34.9%.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
    },
    {
      "id": "prob-automotive-engineering-3-3",
      "title": "Calculation & Verification: Gear ratio, wheel speed and road speed",
      "unit": 3,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Gear ratio, wheel speed and road speed** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>At 2400 rpm engine speed, total reduction 8 and rolling radius 0.31 m, wheel speed is 300 rpm. Ground speed is 2\u03c0\u00d70.31\u00d7300/60 = 9.74 m/s \u2248 35.1 km/h, neglecting slip.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
    },
    {
      "id": "prob-automotive-engineering-3-4",
      "title": "Calculation & Verification: Transmission losses and driveline efficiency",
      "unit": 3,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Transmission losses and driveline efficiency** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>Engine torque 180 N\u00b7m, total ratio 10 and assumed transmission efficiency 0.9 give wheel torque 1620 N\u00b7m. With rolling radius 0.30 m, idealized contact force is 5400 N before tire-traction limits.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
    },
    {
      "id": "prob-automotive-engineering-3-5",
      "title": "Calculation & Verification: Hybrid power-split and operating modes",
      "unit": 3,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Hybrid power-split and operating modes** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>At one operating instant the engine path delivers 32 kW and electric path 18 kW, while aggregate losses are 4 kW; the delivered wheel power is 46 kW. This instantaneous balance is not a combined vehicle power rating.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
    },
    {
      "id": "prob-automotive-engineering-4-1",
      "title": "Calculation & Verification: Tire slip and force generation",
      "unit": 4,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Tire slip and force generation** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A vehicle travels at 20 m/s while wheel rim equivalent speed is 16 m/s. The idealized braking slip is (20\u221216)/20 = 0.20, or 20%. It is not automatically the optimal slip for that tire or surface.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
    },
    {
      "id": "prob-automotive-engineering-4-2",
      "title": "Calculation & Verification: Deceleration force and stopping distance",
      "unit": 4,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Deceleration force and stopping distance** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>At 20 m/s and mu = 0.7 on level ground, idealized braking distance = 400/(2\u00d70.7\u00d79.81) = 29.1 m. A 1.2 s driver response adds 24 m before braking begins.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
    },
    {
      "id": "prob-automotive-engineering-4-3",
      "title": "Calculation & Verification: Brake torque, hydraulic systems and thermal energy",
      "unit": 4,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Brake torque, hydraulic systems and thermal energy** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>An 1800 kg vehicle decelerated from 25 to 5 m/s loses 0.5\u00d71800\u00d7(625\u221225) = 540 kJ of translational energy, ignoring rotational inertia. If dissipated in four brake assemblies equally, the average is 135 kJ each, but real axle distribution is unequal.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
    },
    {
      "id": "prob-automotive-engineering-4-4",
      "title": "Calculation & Verification: Anti-lock braking and wheel-speed estimation",
      "unit": 4,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Anti-lock braking and wheel-speed estimation** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A wheel-speed signal changes from 65 to 45 rad/s over 0.10 s. The mean angular acceleration is (45\u221265)/0.10 = \u2212200 rad/s\u00b2. The value is a signal-level diagnostic; it does not alone determine road friction.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
    },
    {
      "id": "prob-automotive-engineering-4-5",
      "title": "Calculation & Verification: Regenerative and friction brake coordination",
      "unit": 4,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Regenerative and friction brake coordination** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For 0.15 kWh available wheel braking energy and a hypothetical combined conversion factor of 0.60, recoverable battery energy is at most 0.09 kWh, before any further state-of-charge restrictions.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
    },
    {
      "id": "prob-automotive-engineering-5-1",
      "title": "Calculation & Verification: Bicycle model and lateral acceleration",
      "unit": 5,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Bicycle model and lateral acceleration** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>At 15 m/s on a 75 m radius, lateral acceleration = 15\u00b2/75 = 3.0 m/s\u00b2 \u2248 0.306 g. At 20 m/s on the same radius the ideal value rises to 5.33 m/s\u00b2.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
    },
    {
      "id": "prob-automotive-engineering-5-2",
      "title": "Calculation & Verification: Steering geometry and turning radius",
      "unit": 5,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Steering geometry and turning radius** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For wheelbase L = 2.7 m and turn radius R = 9 m, idealized bicycle steer angle = atan(2.7/9) = 16.70 degrees at the road wheel, not necessarily at the steering wheel.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
    },
    {
      "id": "prob-automotive-engineering-5-3",
      "title": "Calculation & Verification: Understeer, oversteer and yaw response",
      "unit": 5,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Understeer, oversteer and yaw response** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>At v = 12 m/s and radius 60 m the ideal yaw rate is r = 0.20 rad/s = 11.46 deg/s. A sensed rate differing from this ideal could arise from path-radius error, slip, or instrumentation.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
    },
    {
      "id": "prob-automotive-engineering-5-4",
      "title": "Calculation & Verification: Load transfer, roll and stability margins",
      "unit": 5,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Load transfer, roll and stability margins** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For 1600 kg, 3 m/s\u00b2 lateral acceleration, 0.55 m CG height and track width 1.6 m, simple transfer is 1650 N side-to-side across an idealized axle representation. The distribution across front and rear requires more data.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
    },
    {
      "id": "prob-automotive-engineering-5-5",
      "title": "Calculation & Verification: Steering tests and handling model validation",
      "unit": 5,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Steering tests and handling model validation** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>At one sample the measured yaw rate is 0.24 rad/s and prediction is 0.20 rad/s; residual = +0.04 rad/s. Determine whether the sign persists over the maneuver before retuning a parameter.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
    },
    {
      "id": "prob-automotive-engineering-6-1",
      "title": "Calculation & Verification: Springs, damping and ride response",
      "unit": 6,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Springs, damping and ride response** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A spring under 4000 N static load with k = 25,000 N/m deflects x = 4000/25000 = 0.160 m in the linear model. Real mounting geometry changes wheel rate.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
    },
    {
      "id": "prob-automotive-engineering-6-2",
      "title": "Calculation & Verification: Quarter-car frequency and damping ratio",
      "unit": 6,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Quarter-car frequency and damping ratio** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>With k = 20,000 N/m and sprung mass = 300 kg, f_n = sqrt(20000/300)/(2\u03c0) \u2248 1.30 Hz. Increasing sprung mass to 375 kg lowers it to about 1.16 Hz.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
    },
    {
      "id": "prob-automotive-engineering-6-3",
      "title": "Calculation & Verification: Unsprung mass and wheel hop",
      "unit": 6,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Unsprung mass and wheel hop** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>If unsprung mass is 40 kg and tire stiffness is 180,000 N/m, the isolated wheel-hop frequency estimate sqrt(180000/40)/(2\u03c0) \u2248 10.68 Hz; coupling shifts the actual modes.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
    },
    {
      "id": "prob-automotive-engineering-6-4",
      "title": "Calculation & Verification: Longitudinal load transfer and geometry",
      "unit": 6,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Longitudinal load transfer and geometry** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For 1800 kg, longitudinal deceleration 5 m/s\u00b2, center-of-gravity height 0.55 m and wheelbase 2.8 m, frontward load transfer is (1800\u00d75\u00d70.55)/2.8 \u2248 1768 N.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
    },
    {
      "id": "prob-automotive-engineering-6-5",
      "title": "Calculation & Verification: Noise, vibration and harshness pathways",
      "unit": 6,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Noise, vibration and harshness pathways** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A second-order disturbance at shaft speed 1800 rpm has frequency 2\u00d71800/60 = 60 Hz. Reducing the shaft speed to 1500 rpm shifts its second-order excitation to 50 Hz.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
    },
    {
      "id": "prob-automotive-engineering-7-1",
      "title": "Calculation & Verification: Electric traction motor torque and inverter limits",
      "unit": 7,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Electric traction motor torque and inverter limits** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>At torque 280 N\u00b7m and 4000 rpm, mechanical shaft power is 280\u00d72\u03c0\u00d74000/60 = 117.3 kW. This says nothing about continuous rating without cooling and duty-cycle information.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
    },
    {
      "id": "prob-automotive-engineering-7-2",
      "title": "Calculation & Verification: Battery capacity, usable window and vehicle range",
      "unit": 7,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Battery capacity, usable window and vehicle range** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For 62 kWh usable energy and assumed average 0.18 kWh/km pack consumption, model range = 62/0.18 = 344 km before reserve and unforeseen conditions. A 10 kWh reserve changes the planned-distance estimate to 52/0.18 = 289 km.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
    },
    {
      "id": "prob-automotive-engineering-7-3",
      "title": "Calculation & Verification: Battery internal resistance and thermal management",
      "unit": 7,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Battery internal resistance and thermal management** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For a hypothetical current of 200 A and effective series resistance 0.05 ohm, ohmic heating is 200\u00b2\u00d70.05 = 2000 W. This is a simplified pack-level resistance example; actual heat generation may differ.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
    },
    {
      "id": "prob-automotive-engineering-7-4",
      "title": "Calculation & Verification: Charging power, efficiency and taper",
      "unit": 7,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Charging power, efficiency and taper** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>Delivering 30 kWh into the pack at constant 50 kW input and 90% overall efficiency would take 30/(50\u00d70.9) = 0.667 h = 40 minutes. Power taper or thermal protection would lengthen the actual session.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
    },
    {
      "id": "prob-automotive-engineering-7-5",
      "title": "Calculation & Verification: Hybrid and EV system-level comparison",
      "unit": 7,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Hybrid and EV system-level comparison** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>At 18 kWh/100 km drawn from the pack and 90% charging efficiency, wall consumption is 20 kWh/100 km; the 2 kWh difference is a conversion loss, not a change in road work.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
    },
    {
      "id": "prob-automotive-engineering-8-1",
      "title": "Calculation & Verification: Sensors, embedded software and control loops",
      "unit": 8,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Sensors, embedded software and control loops** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A sensor reports vehicle speed 21.3 m/s while an independent reference is 20.0 m/s. Its instantaneous error is +1.3 m/s or +6.5% relative to reference; repeat measurements are needed to separate calibration bias and noise.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
    },
    {
      "id": "prob-automotive-engineering-8-2",
      "title": "Calculation & Verification: On-board diagnostics and failure analysis",
      "unit": 8,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **On-board diagnostics and failure analysis** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>A model predicts 48 km/h while measured speed is 52 km/h; residual = +4 km/h. A repeated +4 km/h bias over multiple speeds suggests a different cause than random \u00b14 km/h noise.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
    },
    {
      "id": "prob-automotive-engineering-8-3",
      "title": "Calculation & Verification: Functional safety, hazards and fault containment",
      "unit": 8,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Functional safety, hazards and fault containment** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>If a controller commands 100 N\u00b7m while a monitor independently estimates 160 N\u00b7m, the discrepancy is 60 N\u00b7m. That signal difference warrants investigation, not an automatic conclusion about a safe tolerance.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
    },
    {
      "id": "prob-automotive-engineering-8-4",
      "title": "Calculation & Verification: Crashworthiness, occupant protection and restraint systems",
      "unit": 8,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Crashworthiness, occupant protection and restraint systems** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>An 80 kg surrogate whose speed changes by 10 m/s has momentum change 800 N\u00b7s. Over an illustrative 0.10 s stopping interval the average net force magnitude is 8000 N, but this is not an injury prediction.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
    },
    {
      "id": "prob-automotive-engineering-8-5",
      "title": "Calculation & Verification: Vehicle validation, homologation and engineering reports",
      "unit": 8,
      "question": "<p><strong>Problem Statement:</strong> An engineering practitioner analyzes a mechanical system governed by **Vehicle validation, homologation and engineering reports** under steady operational loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>For a requirement that test mass be within \u00b120 kg of 1800 kg, a measured 1826 kg fails the specified tolerance by 6 kg, regardless of whether other performance results looked favorable.\n\n**Cross-check:** Reconstruct the result from the stated inputs without rounding intermediate values prematurely. Describe which term would change if the test were repeated with a new vehicle mass, ambient temperature or tire configuration. At least one check should concern the scale of the result: compare the derived force with vehicle weight, the energy with a known kinetic-energy change, or the speed with a plausible road operating point. A result can satisfy the formula exactly and still be inapplicable because one assumption is not true.</p></div>"
    }
  ]
};
if (typeof module !== 'undefined') module.exports = COURSE_DATA;
if (typeof window !== 'undefined') window.COURSE_DATA = COURSE_DATA;
