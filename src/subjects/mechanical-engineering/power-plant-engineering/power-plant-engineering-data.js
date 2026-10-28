/* OpenSTEM Course Data: Power Plant Engineering (PPE) */
var COURSE_DATA = {
  "code": "PPE",
  "title": "Power Plant Engineering",
  "subtitle": "Supercritical Rankine Cycles, Combined Cycle Gas Turbines, Nuclear, Boilers, Cooling Towers & Economics",
  "units": [
    {
      "number": 1,
      "unitNumber": 1,
      "title": "Power-Plant Architecture and Energy Accounting",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Power-Plant Architecture and Energy Accounting.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Power-Plant Architecture and Energy Accounting.",
      "sections": [
        {
          "id": "sec-1-1",
          "title": "Plant components and boundary definitions",
          "leadSummary": "**Core topic:** gross-to-net station performance. **Representative relation:** `P_net = P_gross - P_aux`. **Case context:** gross export meter versus auxiliary transformers.",
          "content": "<p>**Core topic:** gross-to-net station performance. **Representative relation:** `P_net = P_gross - P_aux`. **Case context:** gross export meter versus auxiliary transformers.</p>"
        },
        {
          "id": "sec-1-2",
          "title": "First-law control-volume balances",
          "leadSummary": "**Core topic:** steady open-system energy conservation. **Representative relation:** `Q_in - W_out = sum(m_out h_out) - sum(m_in h_in)`. **Case context:** fuel heater and steam generator.",
          "content": "<p>**Core topic:** steady open-system energy conservation. **Representative relation:** `Q_in - W_out = sum(m_out h_out) - sum(m_in h_in)`. **Case context:** fuel heater and steam generator.</p>"
        },
        {
          "id": "sec-1-3",
          "title": "Fuel heating values and combustion input",
          "leadSummary": "**Core topic:** mass-flow and heating-value accounting. **Representative relation:** `Q_fuel = m_dot_fuel * LHV`. **Case context:** liquid-fuel and gas custody measurement.",
          "content": "<p>**Core topic:** mass-flow and heating-value accounting. **Representative relation:** `Q_fuel = m_dot_fuel * LHV`. **Case context:** liquid-fuel and gas custody measurement.</p>"
        },
        {
          "id": "sec-1-4",
          "title": "Plant efficiency and heat rate",
          "leadSummary": "**Core topic:** efficiency and inverse heat rate. **Representative relation:** `eta_net = P_net / Q_fuel`. **Case context:** hourly operational performance report.",
          "content": "<p>**Core topic:** efficiency and inverse heat rate. **Representative relation:** `eta_net = P_net / Q_fuel`. **Case context:** hourly operational performance report.</p>"
        },
        {
          "id": "sec-1-5",
          "title": "Capacity factor, utilization, and dispatch",
          "leadSummary": "**Core topic:** annual energy versus rated output. **Representative relation:** `E_year = P_rated * CF * 8760`. **Case context:** annual load curve and forced outage register.",
          "content": "<p>**Core topic:** annual energy versus rated output. **Representative relation:** `E_year = P_rated * CF * 8760`. **Case context:** annual load curve and forced outage register.</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-power-plant-engineering-1-1",
          "title": "Calculation & Verification: Plant components and boundary definitions",
          "unit": 1,
          "question": "<p><strong>Problem Statement:</strong> Gross terminal output is 155 MW(e) and station service is 8 MW(e). Net output is 155 \u2212 8 = **147 MW(e)**. The gross-to-net reduction is 8/155 \u00d7 100 = 5.16%. Compare both values over the same reporting interval; using one hourly gross figure against a daily auxiliary total is invalid.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Even a perfectly unchanged turbine can show lower net efficiency after cooling or emissions controls increase plant auxiliary electricity. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
        },
        {
          "id": "prob-power-plant-engineering-1-2",
          "title": "Calculation & Verification: First-law control-volume balances",
          "unit": 1,
          "question": "<p><strong>Problem Statement:</strong> A hypothetical boiler control volume receives 75 MW of heat. The outgoing enthalpy flow exceeds the incoming enthalpy flow by 61 MW; with negligible changes in kinetic energy and stored energy, net work leaving is 75 \u2212 61 = **14 MW**. The example is only an algebraic control-volume demonstration: an ordinary steam boiler need not export shaft work.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Use a realistic device definition before interpreting the result; a boiler-only balance should include all fluid streams and heat losses. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
        },
        {
          "id": "prob-power-plant-engineering-1-3",
          "title": "Calculation & Verification: Fuel heating values and combustion input",
          "unit": 1,
          "question": "<p><strong>Problem Statement:</strong> A plant burns 3.2 kg/s of fuel whose assumed lower heating value is 43 MJ/kg. Fuel heat input is 3.2 \u00d7 43 = **137.6 MW(th)**. If the report instead uses a higher heating value, the number changes without any change in the physical fuel flow. A gas volume meter alone is insufficient unless gas composition and reference conditions are specified.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Do not multiply a fuel mass flow by an unlabelled calorific value; distinguish LHV from HHV consistently. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
        },
        {
          "id": "prob-power-plant-engineering-1-4",
          "title": "Calculation & Verification: Plant efficiency and heat rate",
          "unit": 1,
          "question": "<p><strong>Problem Statement:</strong> The same hour shows 150 MW(e) net export and 390 MW(th) measured fuel input on an LHV basis. Net thermal efficiency is 150/390 = **38.46%**, and net heat rate is 3600/0.384615 = **9360 kJ/kWh**. A report that substitutes gross output would provide a different performance metric.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Heat rate and efficiency are reciprocal forms of one energy ratio only when their reporting bases match. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
        },
        {
          "id": "prob-power-plant-engineering-1-5",
          "title": "Calculation & Verification: Capacity factor, utilization, and dispatch",
          "unit": 1,
          "question": "<p><strong>Problem Statement:</strong> A net-rated 160 MW station operates at a 65% annual capacity factor. Its annual energy in a 365-day year is 160 \u00d7 0.65 \u00d7 8760 = **911,040 MWh**. This does not mean the facility operated at 65% output every hour: many dispatch and outage profiles can yield the same annual total.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Capacity factor is not a measure of conversion efficiency and does not show plant availability by itself. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
        }
      ]
    },
    {
      "number": 2,
      "unitNumber": 2,
      "title": "Steam-Cycle Power Generation",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Steam-Cycle Power Generation.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Steam-Cycle Power Generation.",
      "sections": [
        {
          "id": "sec-2-1",
          "title": "Rankine states and thermal conversion",
          "leadSummary": "**Core topic:** net cycle work and heat input. **Representative relation:** `eta_R = (w_t - w_p) / q_in`. **Case context:** four-state saturated cycle.",
          "content": "<p>**Core topic:** net cycle work and heat input. **Representative relation:** `eta_R = (w_t - w_p) / q_in`. **Case context:** four-state saturated cycle.</p>"
        },
        {
          "id": "sec-2-2",
          "title": "Steam turbine expansion and extraction",
          "leadSummary": "**Core topic:** enthalpy work and internal efficiency. **Representative relation:** `W_t = m_dot*(h_in-h_out)`. **Case context:** high-pressure turbine with a bleed stream.",
          "content": "<p>**Core topic:** enthalpy work and internal efficiency. **Representative relation:** `W_t = m_dot*(h_in-h_out)`. **Case context:** high-pressure turbine with a bleed stream.</p>"
        },
        {
          "id": "sec-2-3",
          "title": "Condenser duty and backpressure",
          "leadSummary": "**Core topic:** heat rejection from wet exhaust. **Representative relation:** `Q_cond = m_dot*(h_in-h_out)`. **Case context:** surface condenser in a humid climate.",
          "content": "<p>**Core topic:** heat rejection from wet exhaust. **Representative relation:** `Q_cond = m_dot*(h_in-h_out)`. **Case context:** surface condenser in a humid climate.</p>"
        },
        {
          "id": "sec-2-4",
          "title": "Feedwater pumps and boiler input",
          "leadSummary": "**Core topic:** liquid-pump work and steam-generator duty. **Representative relation:** `w_p \u2248 v*(p_out-p_in)`. **Case context:** multistage feedwater train.",
          "content": "<p>**Core topic:** liquid-pump work and steam-generator duty. **Representative relation:** `w_p \u2248 v*(p_out-p_in)`. **Case context:** multistage feedwater train.</p>"
        },
        {
          "id": "sec-2-5",
          "title": "Reheat and regenerative feedwater heating",
          "leadSummary": "**Core topic:** cycle efficiency and moisture management. **Representative relation:** `Q_added = sum(m_dot*delta_h) across heated streams`. **Case context:** one reheat stage with closed feedwater heater.",
          "content": "<p>**Core topic:** cycle efficiency and moisture management. **Representative relation:** `Q_added = sum(m_dot*delta_h) across heated streams`. **Case context:** one reheat stage with closed feedwater heater.</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-power-plant-engineering-2-1",
          "title": "Calculation & Verification: Rankine states and thermal conversion",
          "unit": 2,
          "question": "<p><strong>Problem Statement:</strong> Take idealized cycle enthalpies of 192 kJ/kg at pump inlet, 202 after pumping, 3450 after the boiler, and 2300 at turbine exit. Turbine work is 1150 kJ/kg, pump work is 10 kJ/kg, and heat supplied is 3248 kJ/kg; ideal thermal efficiency is (1150 \u2212 10)/3248 = **35.10%**. These are a synthetic set of enthalpies, not a verified steam-table operating point.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Detailed state selection must satisfy actual pressure and entropy constraints; arbitrary enthalpies cannot validate a real cycle. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
        },
        {
          "id": "prob-power-plant-engineering-2-2",
          "title": "Calculation & Verification: Steam turbine expansion and extraction",
          "unit": 2,
          "question": "<p><strong>Problem Statement:</strong> With steam flow of 30 kg/s and inlet/outlet enthalpies 3410 and 2550 kJ/kg, an ideal steady turbine power estimate is 30(3410 \u2212 2550) = **25,800 kW**, or 25.8 MW. A real extraction turbine must apply this balance separately to every branch rather than using the full inlet flow across all stages.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** The estimate excludes mechanical losses, leakage and the small kinetic-energy terms until their significance is checked. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
        },
        {
          "id": "prob-power-plant-engineering-2-3",
          "title": "Calculation & Verification: Condenser duty and backpressure",
          "unit": 2,
          "question": "<p><strong>Problem Statement:</strong> A condenser receives 42 kg/s of wet exhaust at specific enthalpy 2400 kJ/kg and discharges condensate at 220 kJ/kg. Condenser thermal duty is 42(2400 \u2212 220) = **91,560 kW**. This heat must reach a cooling medium, subject to nonzero temperature approach and finite transfer area.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** A lower condensing temperature may improve ideal cycle output but can increase cooling demand or air-leakage sensitivity. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
        },
        {
          "id": "prob-power-plant-engineering-2-4",
          "title": "Calculation & Verification: Feedwater pumps and boiler input",
          "unit": 2,
          "question": "<p><strong>Problem Statement:</strong> Using near-incompressible liquid specific volume 0.0011 m\u00b3/kg and pressure increase 11 MPa, ideal pump work per kilogram is approximately 0.0011 \u00d7 11,000,000 = **12,100 J/kg**, or 12.1 kJ/kg. A 75%-efficient pump requires approximately 16.1 kJ/kg shaft input, excluding other losses.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Convert pressure to pascals before multiplying by m\u00b3/kg; this dimensional check prevents a thousand-fold error. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
        },
        {
          "id": "prob-power-plant-engineering-2-5",
          "title": "Calculation & Verification: Reheat and regenerative feedwater heating",
          "unit": 2,
          "question": "<p><strong>Problem Statement:</strong> A reheat section raises specific enthalpy of 45 kg/s of steam by 580 kJ/kg. Assuming negligible external heat loss, reheat duty is 45 \u00d7 580 = **26.1 MW(th)**. Whether reheat improves overall cycle efficiency depends on the resulting turbine expansion and heat-supply conditions, not duty alone.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** For regenerative systems, a steam bleed lowers the downstream mass flow; use branch-by-branch energy balances. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
        }
      ]
    },
    {
      "number": 3,
      "unitNumber": 3,
      "title": "Fuels, Combustion and Gas-Turbine Cycles",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Fuels, Combustion and Gas-Turbine Cycles.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Fuels, Combustion and Gas-Turbine Cycles.",
      "sections": [
        {
          "id": "sec-3-1",
          "title": "Fuel characterization and stoichiometry",
          "leadSummary": "**Core topic:** air requirement and excess air. **Representative relation:** `AFR_st = m_air_st / m_fuel`. **Case context:** boiler burner with varying fuel composition.",
          "content": "<p>**Core topic:** air requirement and excess air. **Representative relation:** `AFR_st = m_air_st / m_fuel`. **Case context:** boiler burner with varying fuel composition.</p>"
        },
        {
          "id": "sec-3-2",
          "title": "Steam-generator heat balance",
          "leadSummary": "**Core topic:** boiler efficiency and steam production. **Representative relation:** `Q_to_steam = m_dot_s*(h_out-h_in)`. **Case context:** feedwater-to-superheated steam balance.",
          "content": "<p>**Core topic:** boiler efficiency and steam production. **Representative relation:** `Q_to_steam = m_dot_s*(h_out-h_in)`. **Case context:** feedwater-to-superheated steam balance.</p>"
        },
        {
          "id": "sec-3-3",
          "title": "Ideal Brayton pressure-ratio trends",
          "leadSummary": "**Core topic:** pressure ratio under constant-property ideal assumptions. **Representative relation:** `eta_B = 1-r_p**(-(gamma-1)/gamma)`. **Case context:** gas-turbine performance thought experiment.",
          "content": "<p>**Core topic:** pressure ratio under constant-property ideal assumptions. **Representative relation:** `eta_B = 1-r_p**(-(gamma-1)/gamma)`. **Case context:** gas-turbine performance thought experiment.</p>"
        },
        {
          "id": "sec-3-4",
          "title": "Compressor and turbine specific work",
          "leadSummary": "**Core topic:** gas-path shaft balance. **Representative relation:** `w_net = cp*(T3-T4)-cp*(T2-T1)`. **Case context:** simple open Brayton cycle.",
          "content": "<p>**Core topic:** gas-path shaft balance. **Representative relation:** `w_net = cp*(T3-T4)-cp*(T2-T1)`. **Case context:** simple open Brayton cycle.</p>"
        },
        {
          "id": "sec-3-5",
          "title": "Combustion emissions and operational trade-offs",
          "leadSummary": "**Core topic:** emissions intensity and denominators. **Representative relation:** `e_CO2 = m_CO2 / E_net`. **Case context:** plant output versus fuel-carbon accounting.",
          "content": "<p>**Core topic:** emissions intensity and denominators. **Representative relation:** `e_CO2 = m_CO2 / E_net`. **Case context:** plant output versus fuel-carbon accounting.</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-power-plant-engineering-3-1",
          "title": "Calculation & Verification: Fuel characterization and stoichiometry",
          "unit": 3,
          "question": "<p><strong>Problem Statement:</strong> For ideal pure methane, CH4 + 2 O2 \u2192 CO2 + 2 H2O. One mole of methane has mass about 16 g and needs 64 g oxygen; hence **4 kg O2/kg CH4**. If dry air has 23.2% oxygen by mass, the stoichiometric air requirement is 4/0.232 = **17.24 kg air/kg methane**. This ignores real fuel mixtures and moisture.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Using the wrong oxygen mass fraction or an LHV/HHV basis changes a combustion calculation materially. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
        },
        {
          "id": "prob-power-plant-engineering-3-2",
          "title": "Calculation & Verification: Steam-generator heat balance",
          "unit": 3,
          "question": "<p><strong>Problem Statement:</strong> Feedwater at 850 kJ/kg is heated to steam at 3200 kJ/kg at a mass flow of 20 kg/s. Gross steam-side duty is 20(3200 \u2212 850) = **47 MW(th)**. This is not identical to fuel input, because the boiler has losses, blowdown and possibly attemperation or other mass-flow branches.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** A measured flue-gas stack temperature is not enough to compute complete boiler efficiency without a fuel and mass balance. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
        },
        {
          "id": "prob-power-plant-engineering-3-3",
          "title": "Calculation & Verification: Ideal Brayton pressure-ratio trends",
          "unit": 3,
          "question": "<p><strong>Problem Statement:</strong> Assume an ideal reversible Brayton cycle with a constant heat-capacity ratio \u03b3 = 1.4 and compressor pressure ratio 10. The ideal expression 1 \u2212 10^(\u22120.4/1.4) gives **48.21%**. Real simple-cycle efficiency will generally differ because of compressor/turbine isentropic losses, combustor pressure drop and turbine inlet temperature limits.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Do not interpret the simple air-standard value as a vendor map or predicted guaranteed turbine performance. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
        },
        {
          "id": "prob-power-plant-engineering-3-4",
          "title": "Calculation & Verification: Compressor and turbine specific work",
          "unit": 3,
          "question": "<p><strong>Problem Statement:</strong> With cp = 1.05 kJ/(kg K), compressor inlet/outlet temperatures 300 and 610 K, and turbine inlet/outlet temperatures 1400 and 900 K, net gas-path specific work is 1.05[(1400 \u2212 900) \u2212 (610 \u2212 300)] = **199.5 kJ/kg**. Turbine work alone would be 525 kJ/kg and would badly overstate shaft output.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** The example assumes identical gas and air mass flows and constant cp solely for introductory comparison. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
        },
        {
          "id": "prob-power-plant-engineering-3-5",
          "title": "Calculation & Verification: Combustion emissions and operational trade-offs",
          "unit": 3,
          "question": "<p><strong>Problem Statement:</strong> An illustrative emissions inventory gives 16 tonnes CO2 for 80 MWh(e) net export in the same hour. The intensity is (16,000 kg)/(80 MWh) = **200 kg CO2/MWh**. This is a synthetic arithmetic case, not an emissions factor for a fuel or technology. Boundary choice must state whether the metric covers direct combustion, upstream supply or full lifecycle.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Emissions accounting must not conflate greenhouse-gas intensity with NOx or air-quality compliance. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
        }
      ]
    },
    {
      "number": 4,
      "unitNumber": 4,
      "title": "Combined Cycles and Cogeneration",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Combined Cycles and Cogeneration.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Combined Cycles and Cogeneration.",
      "sections": [
        {
          "id": "sec-4-1",
          "title": "Heat-recovery steam generators",
          "leadSummary": "**Core topic:** gas-to-water energy recovery. **Representative relation:** `Q_HRSG = m_dot_g*cp_g*(T_g,in-T_g,out)`. **Case context:** unfired exhaust heat exchanger.",
          "content": "<p>**Core topic:** gas-to-water energy recovery. **Representative relation:** `Q_HRSG = m_dot_g*cp_g*(T_g,in-T_g,out)`. **Case context:** unfired exhaust heat exchanger.</p>"
        },
        {
          "id": "sec-4-2",
          "title": "Combined-cycle net efficiency",
          "leadSummary": "**Core topic:** system electric performance. **Representative relation:** `eta_CC = (P_GT+P_ST-P_aux)/Q_fuel`. **Case context:** gas and steam generator gross meters.",
          "content": "<p>**Core topic:** system electric performance. **Representative relation:** `eta_CC = (P_GT+P_ST-P_aux)/Q_fuel`. **Case context:** gas and steam generator gross meters.</p>"
        },
        {
          "id": "sec-4-3",
          "title": "CHP total fuel utilization",
          "leadSummary": "**Core topic:** simultaneous heat and electric services. **Representative relation:** `U_CHP = (P_e+Q_useful)/Q_fuel`. **Case context:** industrial process steam demand.",
          "content": "<p>**Core topic:** simultaneous heat and electric services. **Representative relation:** `U_CHP = (P_e+Q_useful)/Q_fuel`. **Case context:** industrial process steam demand.</p>"
        },
        {
          "id": "sec-4-4",
          "title": "Pinch, approach and exhaust constraints",
          "leadSummary": "**Core topic:** thermal contact and exchanger sizing. **Representative relation:** `DeltaT_pinch = T_g,evap_out-T_sat`. **Case context:** single-pressure HRSG temperature sketch.",
          "content": "<p>**Core topic:** thermal contact and exchanger sizing. **Representative relation:** `DeltaT_pinch = T_g,evap_out-T_sat`. **Case context:** single-pressure HRSG temperature sketch.</p>"
        },
        {
          "id": "sec-4-5",
          "title": "Integrated part-load operation",
          "leadSummary": "**Core topic:** coupled equipment at variable demand. **Representative relation:** `P_net = P_GT(load)+P_ST(load)-P_aux(load)`. **Case context:** daily dispatch and ambient-temperature variation.",
          "content": "<p>**Core topic:** coupled equipment at variable demand. **Representative relation:** `P_net = P_GT(load)+P_ST(load)-P_aux(load)`. **Case context:** daily dispatch and ambient-temperature variation.</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-power-plant-engineering-4-1",
          "title": "Calculation & Verification: Heat-recovery steam generators",
          "unit": 4,
          "question": "<p><strong>Problem Statement:</strong> An HRSG receives 220 kg/s of exhaust gas, with assumed cp = 1.1 kJ/(kg K), entering at 560 \u00b0C and leaving at 160 \u00b0C. Sensible heat lost by gas is 220 \u00d7 1.1 \u00d7 400 = **96.8 MW(th)**. Actual heat delivered to steam is lower if there are heat losses or bypass streams.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Finite temperature approach, material limits and stack condensation rules constrain real recovery. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
        },
        {
          "id": "prob-power-plant-engineering-4-2",
          "title": "Calculation & Verification: Combined-cycle net efficiency",
          "unit": 4,
          "question": "<p><strong>Problem Statement:</strong> A gas turbine produces 180 MW(e), a downstream steam turbine 90 MW(e), and auxiliaries consume 12 MW(e), with 450 MW(th) primary fuel input. Net output is 258 MW(e) and overall net efficiency is 258/450 = **57.33%**. The fuel denominator already supplied the gas turbine; recovered exhaust is not counted as a second fuel source.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** This is an illustrative operating point; ambient conditions and part-load behavior change real performance. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
        },
        {
          "id": "prob-power-plant-engineering-4-3",
          "title": "Calculation & Verification: CHP total fuel utilization",
          "unit": 4,
          "question": "<p><strong>Problem Statement:</strong> A CHP plant produces 30 MW(e) and delivers 40 MW(th) of genuinely useful heat while consuming 100 MW(th) primary fuel. Total fuel utilization is (30 + 40)/100 = **70%**. Its electric-only ratio remains 30%; a different customer heat-demand profile could substantially reduce the annual useful-heat credit.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Measure heat at the customer export boundary rather than counting internal steam circulation. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
        },
        {
          "id": "prob-power-plant-engineering-4-4",
          "title": "Calculation & Verification: Pinch, approach and exhaust constraints",
          "unit": 4,
          "question": "<p><strong>Problem Statement:</strong> In a schematic HRSG, the gas temperature leaving the evaporator is 195 \u00b0C and steam saturation temperature is 175 \u00b0C at that section. Pinch temperature difference is **20 K**. Reducing this difference would generally require greater heat-transfer area or different design; it cannot be reduced to zero in a finite exchanger for finite heat transfer.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** A local pinch value does not describe the complete multi-pressure temperature profile or acid-dew-point limits. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
        },
        {
          "id": "prob-power-plant-engineering-4-5",
          "title": "Calculation & Verification: Integrated part-load operation",
          "unit": 4,
          "question": "<p><strong>Problem Statement:</strong> At a particular dispatch point, gas and steam turbines produce 150 and 70 MW(e), and station service consumes 10 MW(e). Net export is **210 MW(e)**. A 10% gas-turbine reduction need not yield an immediate 10% steam-turbine reduction because exhaust temperature, steam storage, controls and time response all matter.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Do not use a fixed rated steam-to-gas power ratio to predict part-load output. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
        }
      ]
    },
    {
      "number": 5,
      "unitNumber": 5,
      "title": "Cooling Systems, Water and Environmental Constraints",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Cooling Systems, Water and Environmental Constraints.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Cooling Systems, Water and Environmental Constraints.",
      "sections": [
        {
          "id": "sec-5-1",
          "title": "Condenser heat-rejection accounting",
          "leadSummary": "**Core topic:** water-side calorimetry. **Representative relation:** `Q_reject = m_dot_cw*cp*DeltaT`. **Case context:** condenser cooling-water loop.",
          "content": "<p>**Core topic:** water-side calorimetry. **Representative relation:** `Q_reject = m_dot_cw*cp*DeltaT`. **Case context:** condenser cooling-water loop.</p>"
        },
        {
          "id": "sec-5-2",
          "title": "Cooling towers and ambient boundaries",
          "leadSummary": "**Core topic:** approach, range and wet-bulb influence. **Representative relation:** `Range = T_hot-T_cold`. **Case context:** forced-draft evaporative cooling tower.",
          "content": "<p>**Core topic:** approach, range and wet-bulb influence. **Representative relation:** `Range = T_hot-T_cold`. **Case context:** forced-draft evaporative cooling tower.</p>"
        },
        {
          "id": "sec-5-3",
          "title": "Water consumption and blowdown",
          "leadSummary": "**Core topic:** cycles of concentration and water budgets. **Representative relation:** `COC = C_circulating/C_makeup`. **Case context:** cooling tower makeup, drift and blowdown records.",
          "content": "<p>**Core topic:** cycles of concentration and water budgets. **Representative relation:** `COC = C_circulating/C_makeup`. **Case context:** cooling tower makeup, drift and blowdown records.</p>"
        },
        {
          "id": "sec-5-4",
          "title": "Dry and hybrid cooling",
          "leadSummary": "**Core topic:** heat-exchanger effectiveness and climate effects. **Representative relation:** `Q = UA*LMTD`. **Case context:** air-cooled condenser under hot weather.",
          "content": "<p>**Core topic:** heat-exchanger effectiveness and climate effects. **Representative relation:** `Q = UA*LMTD`. **Case context:** air-cooled condenser under hot weather.</p>"
        },
        {
          "id": "sec-5-5",
          "title": "Environmental evaluation and monitoring",
          "leadSummary": "**Core topic:** resource intensity across a reporting boundary. **Representative relation:** `I_water = V_consumed/E_net`. **Case context:** monthly plant water balance.",
          "content": "<p>**Core topic:** resource intensity across a reporting boundary. **Representative relation:** `I_water = V_consumed/E_net`. **Case context:** monthly plant water balance.</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-power-plant-engineering-5-1",
          "title": "Calculation & Verification: Condenser heat-rejection accounting",
          "unit": 5,
          "question": "<p><strong>Problem Statement:</strong> A cooling-water loop carries 2600 kg/s with assumed cp = 4.18 kJ/(kg K) and temperature rise 7 K. Heat duty is 2600 \u00d7 4.18 \u00d7 7 = **76,076 kW**, or 76.076 MW(th). A 0.2 K sensor offset would change the inferred duty by about 2.17 MW, so calibration matters.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** This single-phase sensible estimate does not include independent condenser steam-side validation. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
        },
        {
          "id": "prob-power-plant-engineering-5-2",
          "title": "Calculation & Verification: Cooling towers and ambient boundaries",
          "unit": 5,
          "question": "<p><strong>Problem Statement:</strong> A cooling tower returns water at 29 \u00b0C after receiving hot water at 36 \u00b0C. Cooling range is **7 K**. If ambient wet-bulb temperature is 25 \u00b0C, the cold-water approach is **4 K**. Neither number alone specifies evaporation, electrical fan demand or biological treatment requirements.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Cooling-tower performance changes with humidity, air flow and water chemistry. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
        },
        {
          "id": "prob-power-plant-engineering-5-3",
          "title": "Calculation & Verification: Water consumption and blowdown",
          "unit": 5,
          "question": "<p><strong>Problem Statement:</strong> A concentration proxy is 1800 mg/L circulating-water dissolved solids divided by 300 mg/L makeup-water solids, giving **6 cycles of concentration**. This simplified ratio assumes consistent species behavior and mixing; chemical reaction and selective precipitation break the scalar approximation.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** A plant water budget also requires evaporation, blowdown, drift and leak measurements. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
        },
        {
          "id": "prob-power-plant-engineering-5-4",
          "title": "Calculation & Verification: Dry and hybrid cooling",
          "unit": 5,
          "question": "<p><strong>Problem Statement:</strong> A simplified air-cooled exchanger has UA = 250 kW/K and a log-mean temperature difference of 16 K. Its idealized rate is **4.0 MW(th)**. Real UA varies with fouling, air velocity, fin condition and operating temperature, so a hot-day prediction requires actual equipment data.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** An assumed fixed temperature approach can conceal a high-temperature derating risk. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
        },
        {
          "id": "prob-power-plant-engineering-5-5",
          "title": "Calculation & Verification: Environmental evaluation and monitoring",
          "unit": 5,
          "question": "<p><strong>Problem Statement:</strong> A plant consumes 500,000 m\u00b3 of water while exporting 700,000 MWh(e) over the same annual period. Consumptive intensity is 500,000/700,000 = **0.714 m\u00b3/MWh**. Withdrawal volume could be much larger; report the two separately and document where water is returned.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** This accounting value is not a license to withdraw water or discharge heated effluent. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
        }
      ]
    },
    {
      "number": 6,
      "unitNumber": 6,
      "title": "Nonfossil Generation and Hybrid Power Systems",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Nonfossil Generation and Hybrid Power Systems.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Nonfossil Generation and Hybrid Power Systems.",
      "sections": [
        {
          "id": "sec-6-1",
          "title": "Hydroelectric conversion and head",
          "leadSummary": "**Core topic:** hydraulic potential to electric power. **Representative relation:** `P_h = rho*g*Q*H*eta`. **Case context:** reservoir release with known head.",
          "content": "<p>**Core topic:** hydraulic potential to electric power. **Representative relation:** `P_h = rho*g*Q*H*eta`. **Case context:** reservoir release with known head.</p>"
        },
        {
          "id": "sec-6-2",
          "title": "Wind and variable-power capture",
          "leadSummary": "**Core topic:** wind-energy flux and rotor capture. **Representative relation:** `P_w = 0.5*rho_air*A*V**3*Cp`. **Case context:** wind farm performance estimate.",
          "content": "<p>**Core topic:** wind-energy flux and rotor capture. **Representative relation:** `P_w = 0.5*rho_air*A*V**3*Cp`. **Case context:** wind farm performance estimate.</p>"
        },
        {
          "id": "sec-6-3",
          "title": "Solar photovoltaics and solar thermal",
          "leadSummary": "**Core topic:** incident irradiance and AC derating. **Representative relation:** `P_PV = G*A*eta_module*PR`. **Case context:** rooftop module versus utility-scale array.",
          "content": "<p>**Core topic:** incident irradiance and AC derating. **Representative relation:** `P_PV = G*A*eta_module*PR`. **Case context:** rooftop module versus utility-scale array.</p>"
        },
        {
          "id": "sec-6-4",
          "title": "Geothermal and nuclear thermal boundaries",
          "leadSummary": "**Core topic:** thermal-source-to-electric conversion. **Representative relation:** `eta_thermal = P_e/Q_source`. **Case context:** geothermal brine loop and nuclear steam generator comparison.",
          "content": "<p>**Core topic:** thermal-source-to-electric conversion. **Representative relation:** `eta_thermal = P_e/Q_source`. **Case context:** geothermal brine loop and nuclear steam generator comparison.</p>"
        },
        {
          "id": "sec-6-5",
          "title": "Hybrid storage, flexibility and capacity value",
          "leadSummary": "**Core topic:** duration and round-trip losses. **Representative relation:** `E_store = P_discharge*t_discharge`. **Case context:** solar plus battery and dispatchable reserve.",
          "content": "<p>**Core topic:** duration and round-trip losses. **Representative relation:** `E_store = P_discharge*t_discharge`. **Case context:** solar plus battery and dispatchable reserve.</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-power-plant-engineering-6-1",
          "title": "Calculation & Verification: Hydroelectric conversion and head",
          "unit": 6,
          "question": "<p><strong>Problem Statement:</strong> Take water density 1000 kg/m\u00b3, g = 9.81 m/s\u00b2, flow 40 m\u00b3/s, net head 75 m and total efficiency 0.90. Hydropower is 1000 \u00d7 9.81 \u00d7 40 \u00d7 75 \u00d7 0.90 = **26.487 MW(e)**. Actual output also depends on reservoir conditions, permitted releases and seasonal flow.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Using gross rather than net head causes a systematic overestimate of delivered power. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
        },
        {
          "id": "prob-power-plant-engineering-6-2",
          "title": "Calculation & Verification: Wind and variable-power capture",
          "unit": 6,
          "question": "<p><strong>Problem Statement:</strong> For air density 1.2 kg/m\u00b3, swept area 5000 m\u00b2, wind speed 8 m/s and power coefficient 0.42, idealized captured power is 0.5 \u00d7 1.2 \u00d7 5000 \u00d7 8\u00b3 \u00d7 0.42 = **0.645 MW**. Because wind power scales as the cube of speed, using the arithmetic mean wind speed in this formula cannot generally reproduce annual energy.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Do not assume Cp constant across wind speeds or disregard cut-in and cut-out limits. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
        },
        {
          "id": "prob-power-plant-engineering-6-3",
          "title": "Calculation & Verification: Solar photovoltaics and solar thermal",
          "unit": 6,
          "question": "<p><strong>Problem Statement:</strong> A 5000 m\u00b2 PV array receives irradiance 800 W/m\u00b2, has an assumed module efficiency of 20% and an overall performance ratio of 0.85. Net illustrative output is 800 \u00d7 5000 \u00d7 0.20 \u00d7 0.85 = **680 kW**. This is an instantaneous representative condition, not an annual yield estimate.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Shading, inverter clipping, temperature and soiling require more complete modeling. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
        },
        {
          "id": "prob-power-plant-engineering-6-4",
          "title": "Calculation & Verification: Geothermal and nuclear thermal boundaries",
          "unit": 6,
          "question": "<p><strong>Problem Statement:</strong> A thermal system receives 90 MW(th) and exports 25 MW(e). Its thermal-to-electric ratio is 25/90 = **27.78%** under the stated boundary. This value cannot establish whether the heat came from geothermal fluid, nuclear fission, concentrated solar heat or industrial waste heat, nor can it establish any source-specific safety conclusion.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Only source-specific professional studies can establish nuclear safety or geothermal sustainability. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
        },
        {
          "id": "prob-power-plant-engineering-6-5",
          "title": "Calculation & Verification: Hybrid storage, flexibility and capacity value",
          "unit": 6,
          "question": "<p><strong>Problem Statement:</strong> A battery is rated 20 MW discharge power for four hours of its nominal usable energy. The ideal delivered energy is 20 \u00d7 4 = **80 MWh**. An 88% round-trip efficiency means that cycling 80 MWh of delivered energy requires approximately 80/0.88 = **90.9 MWh** charge input under the simplified model.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Energy storage shifts delivery time and has losses; it is not a generator of net energy. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
        }
      ]
    },
    {
      "number": 7,
      "unitNumber": 7,
      "title": "Generators, Electrical Integration and Plant Controls",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Generators, Electrical Integration and Plant Controls.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Generators, Electrical Integration and Plant Controls.",
      "sections": [
        {
          "id": "sec-7-1",
          "title": "Generator mechanical-electric conversion",
          "leadSummary": "**Core topic:** shaft torque and rotational speed. **Representative relation:** `P_shaft = torque*omega`. **Case context:** turbine-generator coupling under rated load.",
          "content": "<p>**Core topic:** shaft torque and rotational speed. **Representative relation:** `P_shaft = torque*omega`. **Case context:** turbine-generator coupling under rated load.</p>"
        },
        {
          "id": "sec-7-2",
          "title": "Three-phase output and power factor",
          "leadSummary": "**Core topic:** electrical real power measurement. **Representative relation:** `P_3ph = sqrt(3)*V_LL*I_L*PF`. **Case context:** synchronous generator terminal measurements.",
          "content": "<p>**Core topic:** electrical real power measurement. **Representative relation:** `P_3ph = sqrt(3)*V_LL*I_L*PF`. **Case context:** synchronous generator terminal measurements.</p>"
        },
        {
          "id": "sec-7-3",
          "title": "Frequency response and ramping",
          "leadSummary": "**Core topic:** power-rate limits and balancing. **Representative relation:** `Ramp = (P2-P1)/(t2-t1)`. **Case context:** automatic generation control response.",
          "content": "<p>**Core topic:** power-rate limits and balancing. **Representative relation:** `Ramp = (P2-P1)/(t2-t1)`. **Case context:** automatic generation control response.</p>"
        },
        {
          "id": "sec-7-4",
          "title": "Auxiliary systems and protection boundary",
          "leadSummary": "**Core topic:** meter alignment and station service. **Representative relation:** `P_net = P_generator-P_station_service`. **Case context:** high-voltage switchyard and feedwater pump loads.",
          "content": "<p>**Core topic:** meter alignment and station service. **Representative relation:** `P_net = P_generator-P_station_service`. **Case context:** high-voltage switchyard and feedwater pump loads.</p>"
        },
        {
          "id": "sec-7-5",
          "title": "Operating data, state estimation and alarm review",
          "leadSummary": "**Core topic:** instrument disagreement and trend interpretation. **Representative relation:** `Residual = measured - predicted`. **Case context:** supervisory historian data quality audit.",
          "content": "<p>**Core topic:** instrument disagreement and trend interpretation. **Representative relation:** `Residual = measured - predicted`. **Case context:** supervisory historian data quality audit.</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-power-plant-engineering-7-1",
          "title": "Calculation & Verification: Generator mechanical-electric conversion",
          "unit": 7,
          "question": "<p><strong>Problem Statement:</strong> At 3000 rpm a generator rotor turns at 3000 \u00d7 2\u03c0/60 = 314.16 rad/s. With shaft torque 250 kN\u00b7m, mechanical shaft power is 250,000 \u00d7 314.16 = **78.54 MW** before losses. A torque estimate based on 3000 rather than 314.16 would be dimensionally incorrect.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Rotor dynamics, overspeed margins and protective systems are outside this basic calculation. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
        },
        {
          "id": "prob-power-plant-engineering-7-2",
          "title": "Calculation & Verification: Three-phase output and power factor",
          "unit": 7,
          "question": "<p><strong>Problem Statement:</strong> A balanced three-phase generator has line voltage 11 kV, line current 5000 A and power factor 0.90. Real power is \u221a3 \u00d7 11,000 \u00d7 5000 \u00d7 0.90 = **85.74 MW**. Apparent power is about 95.26 MVA, a distinct quantity that matters for thermal loading.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** A three-phase formula must use consistent line-to-line voltage and line-current definitions. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
        },
        {
          "id": "prob-power-plant-engineering-7-3",
          "title": "Calculation & Verification: Frequency response and ramping",
          "unit": 7,
          "question": "<p><strong>Problem Statement:</strong> An operator record shows net output rising from 120 MW to 180 MW in 15 minutes. The average ramp rate is (180 \u2212 120)/15 = **4 MW/min**. This scalar does not mean the equipment can repeat the ramp indefinitely or that the grid operator may request it at any condition.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Turbine thermal stress, minimum stable generation and emission limits require independent operating constraints. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
        },
        {
          "id": "prob-power-plant-engineering-7-4",
          "title": "Calculation & Verification: Auxiliary systems and protection boundary",
          "unit": 7,
          "question": "<p><strong>Problem Statement:</strong> A generator terminal meter records 200 MW(e) while feedwater pumps, fans and other station loads consume 12 MW(e). Net export is **188 MW(e)**. A rise in auxiliary use from 12 to 16 MW lowers export to 184 MW even if generator terminal output remains unchanged.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Separate gross generation, contracted station service and net settlement-meter export. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
        },
        {
          "id": "prob-power-plant-engineering-7-5",
          "title": "Calculation & Verification: Operating data, state estimation and alarm review",
          "unit": 7,
          "question": "<p><strong>Problem Statement:</strong> A simple performance model predicts 38.0% net efficiency for a defined state, but a calibrated measurement yields 37.0%. Residual = measured minus predicted = **\u22121.0 percentage point**, approximately \u22122.63% relative to the prediction. Sensor uncertainty, differing fuel heating value and physical degradation are competing explanations.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** The residual is a diagnostic signal, not itself proof of a specific equipment fault. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
        }
      ]
    },
    {
      "number": 8,
      "unitNumber": 8,
      "title": "Reliability, Economics and Responsible Plant Design",
      "leadSummary": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Reliability, Economics and Responsible Plant Design.",
      "description": "Comprehensive university textbook unit covering fundamental principles, governing relationships, and engineering applications of Reliability, Economics and Responsible Plant Design.",
      "sections": [
        {
          "id": "sec-8-1",
          "title": "Failure modes and maintenance planning",
          "leadSummary": "**Core topic:** repair time and outage exposure. **Representative relation:** `Availability = MTBF/(MTBF+MTTR)`. **Case context:** unit maintenance register.",
          "content": "<p>**Core topic:** repair time and outage exposure. **Representative relation:** `Availability = MTBF/(MTBF+MTTR)`. **Case context:** unit maintenance register.</p>"
        },
        {
          "id": "sec-8-2",
          "title": "Capacity credit and reserve planning",
          "leadSummary": "**Core topic:** reliability versus output statistics. **Representative relation:** `E_expected = P_rated*CF*8760`. **Case context:** high-demand-week planning scenario.",
          "content": "<p>**Core topic:** reliability versus output statistics. **Representative relation:** `E_expected = P_rated*CF*8760`. **Case context:** high-demand-week planning scenario.</p>"
        },
        {
          "id": "sec-8-3",
          "title": "Simple levelized energy cost",
          "leadSummary": "**Core topic:** cost per delivered MWh. **Representative relation:** `LCOE = annual_total_cost/E_year`. **Case context:** annualized capital and operation-cost worksheet.",
          "content": "<p>**Core topic:** cost per delivered MWh. **Representative relation:** `LCOE = annual_total_cost/E_year`. **Case context:** annualized capital and operation-cost worksheet.</p>"
        },
        {
          "id": "sec-8-4",
          "title": "Lifecycle impacts and uncertainty",
          "leadSummary": "**Core topic:** consistent lifecycle normalization. **Representative relation:** `I_CO2 = m_CO2_lifecycle/E_lifetime`. **Case context:** replacement versus refurbishment comparison.",
          "content": "<p>**Core topic:** consistent lifecycle normalization. **Representative relation:** `I_CO2 = m_CO2_lifecycle/E_lifetime`. **Case context:** replacement versus refurbishment comparison.</p>"
        },
        {
          "id": "sec-8-5",
          "title": "Capstone integrated plant evaluation",
          "leadSummary": "**Core topic:** closing energy and decision accounts. **Representative relation:** `Residual_energy = Q_in-P_e-Q_reject-Q_other`. **Case context:** conceptual comparison of three plant options.",
          "content": "<p>**Core topic:** closing energy and decision accounts. **Representative relation:** `Residual_energy = Q_in-P_e-Q_reject-Q_other`. **Case context:** conceptual comparison of three plant options.</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-power-plant-engineering-8-1",
          "title": "Calculation & Verification: Failure modes and maintenance planning",
          "unit": 8,
          "question": "<p><strong>Problem Statement:</strong> In a simplified alternating failure-repair model, MTBF is 5000 h and mean repair time is 100 h. Operational availability is 5000/(5000 + 100) = **98.04%**. Planned maintenance, derated operation and common-cause failures are outside this two-number expression.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Annual capacity factor is not the same quantity as availability. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
        },
        {
          "id": "prob-power-plant-engineering-8-2",
          "title": "Calculation & Verification: Capacity credit and reserve planning",
          "unit": 8,
          "question": "<p><strong>Problem Statement:</strong> A 100 MW net-rated generator serves peaking demand and has annual capacity factor 25%. Its annual energy is 100 \u00d7 0.25 \u00d7 8760 = **219,000 MWh**. This output alone says nothing about the value of its availability during the 50 highest-price or highest-stress hours.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Capacity credit depends on system need and the probability of resource availability at critical times. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
        },
        {
          "id": "prob-power-plant-engineering-8-3",
          "title": "Calculation & Verification: Simple levelized energy cost",
          "unit": 8,
          "question": "<p><strong>Problem Statement:</strong> A project reports annualized fixed, fuel and operations cost totaling 40 million dollars and expected delivered annual energy of 800,000 MWh. Its simplified cost is $40,000,000/800,000 = **$50/MWh**. The figure is not a complete financed project LCOE unless the capital annualization, taxes, financing and other assumptions have been specified.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** A cheaper mean $/MWh may still fail to supply capacity, flexibility or the required environmental service. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
        },
        {
          "id": "prob-power-plant-engineering-8-4",
          "title": "Calculation & Verification: Lifecycle impacts and uncertainty",
          "unit": 8,
          "question": "<p><strong>Problem Statement:</strong> A lifecycle inventory attributes 400,000 tonnes of CO2-equivalent to a project, and lifetime net energy delivery is 5,000,000 MWh. The intensity is 400,000/5,000,000 = **0.08 t CO2e/MWh**, or 80 kg/MWh. Changes to the boundary\u2014construction, fuel supply, or end-of-life\u2014change the result.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Uncertainty and allocation choices should be visible rather than hidden in one exact-looking number. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
        },
        {
          "id": "prob-power-plant-engineering-8-5",
          "title": "Calculation & Verification: Capstone integrated plant evaluation",
          "unit": 8,
          "question": "<p><strong>Problem Statement:</strong> A conceptual plant receives 400 MW(th), exports 155 MW(e), rejects 210 MW(th) through cooling, and has 25 MW(th) of other quantified losses. The unclosed energy residual is 400 \u2212 155 \u2212 210 \u2212 25 = **10 MW(th)**. The analyst must investigate this residual as possible unmeasured loss, stored-energy change, or measurement error; it must not silently disappear.</p>",
          "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** A closed spreadsheet is not sufficient evidence of plant safety, emissions compliance or economic viability. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
        }
      ]
    }
  ],
  "problems": [
    {
      "id": "prob-power-plant-engineering-1-1",
      "title": "Calculation & Verification: Plant components and boundary definitions",
      "unit": 1,
      "question": "<p><strong>Problem Statement:</strong> Gross terminal output is 155 MW(e) and station service is 8 MW(e). Net output is 155 \u2212 8 = **147 MW(e)**. The gross-to-net reduction is 8/155 \u00d7 100 = 5.16%. Compare both values over the same reporting interval; using one hourly gross figure against a daily auxiliary total is invalid.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Even a perfectly unchanged turbine can show lower net efficiency after cooling or emissions controls increase plant auxiliary electricity. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
    },
    {
      "id": "prob-power-plant-engineering-1-2",
      "title": "Calculation & Verification: First-law control-volume balances",
      "unit": 1,
      "question": "<p><strong>Problem Statement:</strong> A hypothetical boiler control volume receives 75 MW of heat. The outgoing enthalpy flow exceeds the incoming enthalpy flow by 61 MW; with negligible changes in kinetic energy and stored energy, net work leaving is 75 \u2212 61 = **14 MW**. The example is only an algebraic control-volume demonstration: an ordinary steam boiler need not export shaft work.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Use a realistic device definition before interpreting the result; a boiler-only balance should include all fluid streams and heat losses. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
    },
    {
      "id": "prob-power-plant-engineering-1-3",
      "title": "Calculation & Verification: Fuel heating values and combustion input",
      "unit": 1,
      "question": "<p><strong>Problem Statement:</strong> A plant burns 3.2 kg/s of fuel whose assumed lower heating value is 43 MJ/kg. Fuel heat input is 3.2 \u00d7 43 = **137.6 MW(th)**. If the report instead uses a higher heating value, the number changes without any change in the physical fuel flow. A gas volume meter alone is insufficient unless gas composition and reference conditions are specified.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Do not multiply a fuel mass flow by an unlabelled calorific value; distinguish LHV from HHV consistently. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
    },
    {
      "id": "prob-power-plant-engineering-1-4",
      "title": "Calculation & Verification: Plant efficiency and heat rate",
      "unit": 1,
      "question": "<p><strong>Problem Statement:</strong> The same hour shows 150 MW(e) net export and 390 MW(th) measured fuel input on an LHV basis. Net thermal efficiency is 150/390 = **38.46%**, and net heat rate is 3600/0.384615 = **9360 kJ/kWh**. A report that substitutes gross output would provide a different performance metric.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Heat rate and efficiency are reciprocal forms of one energy ratio only when their reporting bases match. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
    },
    {
      "id": "prob-power-plant-engineering-1-5",
      "title": "Calculation & Verification: Capacity factor, utilization, and dispatch",
      "unit": 1,
      "question": "<p><strong>Problem Statement:</strong> A net-rated 160 MW station operates at a 65% annual capacity factor. Its annual energy in a 365-day year is 160 \u00d7 0.65 \u00d7 8760 = **911,040 MWh**. This does not mean the facility operated at 65% output every hour: many dispatch and outage profiles can yield the same annual total.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Capacity factor is not a measure of conversion efficiency and does not show plant availability by itself. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
    },
    {
      "id": "prob-power-plant-engineering-2-1",
      "title": "Calculation & Verification: Rankine states and thermal conversion",
      "unit": 2,
      "question": "<p><strong>Problem Statement:</strong> Take idealized cycle enthalpies of 192 kJ/kg at pump inlet, 202 after pumping, 3450 after the boiler, and 2300 at turbine exit. Turbine work is 1150 kJ/kg, pump work is 10 kJ/kg, and heat supplied is 3248 kJ/kg; ideal thermal efficiency is (1150 \u2212 10)/3248 = **35.10%**. These are a synthetic set of enthalpies, not a verified steam-table operating point.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Detailed state selection must satisfy actual pressure and entropy constraints; arbitrary enthalpies cannot validate a real cycle. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
    },
    {
      "id": "prob-power-plant-engineering-2-2",
      "title": "Calculation & Verification: Steam turbine expansion and extraction",
      "unit": 2,
      "question": "<p><strong>Problem Statement:</strong> With steam flow of 30 kg/s and inlet/outlet enthalpies 3410 and 2550 kJ/kg, an ideal steady turbine power estimate is 30(3410 \u2212 2550) = **25,800 kW**, or 25.8 MW. A real extraction turbine must apply this balance separately to every branch rather than using the full inlet flow across all stages.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** The estimate excludes mechanical losses, leakage and the small kinetic-energy terms until their significance is checked. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
    },
    {
      "id": "prob-power-plant-engineering-2-3",
      "title": "Calculation & Verification: Condenser duty and backpressure",
      "unit": 2,
      "question": "<p><strong>Problem Statement:</strong> A condenser receives 42 kg/s of wet exhaust at specific enthalpy 2400 kJ/kg and discharges condensate at 220 kJ/kg. Condenser thermal duty is 42(2400 \u2212 220) = **91,560 kW**. This heat must reach a cooling medium, subject to nonzero temperature approach and finite transfer area.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** A lower condensing temperature may improve ideal cycle output but can increase cooling demand or air-leakage sensitivity. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
    },
    {
      "id": "prob-power-plant-engineering-2-4",
      "title": "Calculation & Verification: Feedwater pumps and boiler input",
      "unit": 2,
      "question": "<p><strong>Problem Statement:</strong> Using near-incompressible liquid specific volume 0.0011 m\u00b3/kg and pressure increase 11 MPa, ideal pump work per kilogram is approximately 0.0011 \u00d7 11,000,000 = **12,100 J/kg**, or 12.1 kJ/kg. A 75%-efficient pump requires approximately 16.1 kJ/kg shaft input, excluding other losses.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Convert pressure to pascals before multiplying by m\u00b3/kg; this dimensional check prevents a thousand-fold error. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
    },
    {
      "id": "prob-power-plant-engineering-2-5",
      "title": "Calculation & Verification: Reheat and regenerative feedwater heating",
      "unit": 2,
      "question": "<p><strong>Problem Statement:</strong> A reheat section raises specific enthalpy of 45 kg/s of steam by 580 kJ/kg. Assuming negligible external heat loss, reheat duty is 45 \u00d7 580 = **26.1 MW(th)**. Whether reheat improves overall cycle efficiency depends on the resulting turbine expansion and heat-supply conditions, not duty alone.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** For regenerative systems, a steam bleed lowers the downstream mass flow; use branch-by-branch energy balances. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
    },
    {
      "id": "prob-power-plant-engineering-3-1",
      "title": "Calculation & Verification: Fuel characterization and stoichiometry",
      "unit": 3,
      "question": "<p><strong>Problem Statement:</strong> For ideal pure methane, CH4 + 2 O2 \u2192 CO2 + 2 H2O. One mole of methane has mass about 16 g and needs 64 g oxygen; hence **4 kg O2/kg CH4**. If dry air has 23.2% oxygen by mass, the stoichiometric air requirement is 4/0.232 = **17.24 kg air/kg methane**. This ignores real fuel mixtures and moisture.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Using the wrong oxygen mass fraction or an LHV/HHV basis changes a combustion calculation materially. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
    },
    {
      "id": "prob-power-plant-engineering-3-2",
      "title": "Calculation & Verification: Steam-generator heat balance",
      "unit": 3,
      "question": "<p><strong>Problem Statement:</strong> Feedwater at 850 kJ/kg is heated to steam at 3200 kJ/kg at a mass flow of 20 kg/s. Gross steam-side duty is 20(3200 \u2212 850) = **47 MW(th)**. This is not identical to fuel input, because the boiler has losses, blowdown and possibly attemperation or other mass-flow branches.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** A measured flue-gas stack temperature is not enough to compute complete boiler efficiency without a fuel and mass balance. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
    },
    {
      "id": "prob-power-plant-engineering-3-3",
      "title": "Calculation & Verification: Ideal Brayton pressure-ratio trends",
      "unit": 3,
      "question": "<p><strong>Problem Statement:</strong> Assume an ideal reversible Brayton cycle with a constant heat-capacity ratio \u03b3 = 1.4 and compressor pressure ratio 10. The ideal expression 1 \u2212 10^(\u22120.4/1.4) gives **48.21%**. Real simple-cycle efficiency will generally differ because of compressor/turbine isentropic losses, combustor pressure drop and turbine inlet temperature limits.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Do not interpret the simple air-standard value as a vendor map or predicted guaranteed turbine performance. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
    },
    {
      "id": "prob-power-plant-engineering-3-4",
      "title": "Calculation & Verification: Compressor and turbine specific work",
      "unit": 3,
      "question": "<p><strong>Problem Statement:</strong> With cp = 1.05 kJ/(kg K), compressor inlet/outlet temperatures 300 and 610 K, and turbine inlet/outlet temperatures 1400 and 900 K, net gas-path specific work is 1.05[(1400 \u2212 900) \u2212 (610 \u2212 300)] = **199.5 kJ/kg**. Turbine work alone would be 525 kJ/kg and would badly overstate shaft output.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** The example assumes identical gas and air mass flows and constant cp solely for introductory comparison. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
    },
    {
      "id": "prob-power-plant-engineering-3-5",
      "title": "Calculation & Verification: Combustion emissions and operational trade-offs",
      "unit": 3,
      "question": "<p><strong>Problem Statement:</strong> An illustrative emissions inventory gives 16 tonnes CO2 for 80 MWh(e) net export in the same hour. The intensity is (16,000 kg)/(80 MWh) = **200 kg CO2/MWh**. This is a synthetic arithmetic case, not an emissions factor for a fuel or technology. Boundary choice must state whether the metric covers direct combustion, upstream supply or full lifecycle.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Emissions accounting must not conflate greenhouse-gas intensity with NOx or air-quality compliance. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
    },
    {
      "id": "prob-power-plant-engineering-4-1",
      "title": "Calculation & Verification: Heat-recovery steam generators",
      "unit": 4,
      "question": "<p><strong>Problem Statement:</strong> An HRSG receives 220 kg/s of exhaust gas, with assumed cp = 1.1 kJ/(kg K), entering at 560 \u00b0C and leaving at 160 \u00b0C. Sensible heat lost by gas is 220 \u00d7 1.1 \u00d7 400 = **96.8 MW(th)**. Actual heat delivered to steam is lower if there are heat losses or bypass streams.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Finite temperature approach, material limits and stack condensation rules constrain real recovery. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
    },
    {
      "id": "prob-power-plant-engineering-4-2",
      "title": "Calculation & Verification: Combined-cycle net efficiency",
      "unit": 4,
      "question": "<p><strong>Problem Statement:</strong> A gas turbine produces 180 MW(e), a downstream steam turbine 90 MW(e), and auxiliaries consume 12 MW(e), with 450 MW(th) primary fuel input. Net output is 258 MW(e) and overall net efficiency is 258/450 = **57.33%**. The fuel denominator already supplied the gas turbine; recovered exhaust is not counted as a second fuel source.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** This is an illustrative operating point; ambient conditions and part-load behavior change real performance. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
    },
    {
      "id": "prob-power-plant-engineering-4-3",
      "title": "Calculation & Verification: CHP total fuel utilization",
      "unit": 4,
      "question": "<p><strong>Problem Statement:</strong> A CHP plant produces 30 MW(e) and delivers 40 MW(th) of genuinely useful heat while consuming 100 MW(th) primary fuel. Total fuel utilization is (30 + 40)/100 = **70%**. Its electric-only ratio remains 30%; a different customer heat-demand profile could substantially reduce the annual useful-heat credit.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Measure heat at the customer export boundary rather than counting internal steam circulation. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
    },
    {
      "id": "prob-power-plant-engineering-4-4",
      "title": "Calculation & Verification: Pinch, approach and exhaust constraints",
      "unit": 4,
      "question": "<p><strong>Problem Statement:</strong> In a schematic HRSG, the gas temperature leaving the evaporator is 195 \u00b0C and steam saturation temperature is 175 \u00b0C at that section. Pinch temperature difference is **20 K**. Reducing this difference would generally require greater heat-transfer area or different design; it cannot be reduced to zero in a finite exchanger for finite heat transfer.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** A local pinch value does not describe the complete multi-pressure temperature profile or acid-dew-point limits. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
    },
    {
      "id": "prob-power-plant-engineering-4-5",
      "title": "Calculation & Verification: Integrated part-load operation",
      "unit": 4,
      "question": "<p><strong>Problem Statement:</strong> At a particular dispatch point, gas and steam turbines produce 150 and 70 MW(e), and station service consumes 10 MW(e). Net export is **210 MW(e)**. A 10% gas-turbine reduction need not yield an immediate 10% steam-turbine reduction because exhaust temperature, steam storage, controls and time response all matter.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Do not use a fixed rated steam-to-gas power ratio to predict part-load output. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
    },
    {
      "id": "prob-power-plant-engineering-5-1",
      "title": "Calculation & Verification: Condenser heat-rejection accounting",
      "unit": 5,
      "question": "<p><strong>Problem Statement:</strong> A cooling-water loop carries 2600 kg/s with assumed cp = 4.18 kJ/(kg K) and temperature rise 7 K. Heat duty is 2600 \u00d7 4.18 \u00d7 7 = **76,076 kW**, or 76.076 MW(th). A 0.2 K sensor offset would change the inferred duty by about 2.17 MW, so calibration matters.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** This single-phase sensible estimate does not include independent condenser steam-side validation. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
    },
    {
      "id": "prob-power-plant-engineering-5-2",
      "title": "Calculation & Verification: Cooling towers and ambient boundaries",
      "unit": 5,
      "question": "<p><strong>Problem Statement:</strong> A cooling tower returns water at 29 \u00b0C after receiving hot water at 36 \u00b0C. Cooling range is **7 K**. If ambient wet-bulb temperature is 25 \u00b0C, the cold-water approach is **4 K**. Neither number alone specifies evaporation, electrical fan demand or biological treatment requirements.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Cooling-tower performance changes with humidity, air flow and water chemistry. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
    },
    {
      "id": "prob-power-plant-engineering-5-3",
      "title": "Calculation & Verification: Water consumption and blowdown",
      "unit": 5,
      "question": "<p><strong>Problem Statement:</strong> A concentration proxy is 1800 mg/L circulating-water dissolved solids divided by 300 mg/L makeup-water solids, giving **6 cycles of concentration**. This simplified ratio assumes consistent species behavior and mixing; chemical reaction and selective precipitation break the scalar approximation.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** A plant water budget also requires evaporation, blowdown, drift and leak measurements. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
    },
    {
      "id": "prob-power-plant-engineering-5-4",
      "title": "Calculation & Verification: Dry and hybrid cooling",
      "unit": 5,
      "question": "<p><strong>Problem Statement:</strong> A simplified air-cooled exchanger has UA = 250 kW/K and a log-mean temperature difference of 16 K. Its idealized rate is **4.0 MW(th)**. Real UA varies with fouling, air velocity, fin condition and operating temperature, so a hot-day prediction requires actual equipment data.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** An assumed fixed temperature approach can conceal a high-temperature derating risk. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
    },
    {
      "id": "prob-power-plant-engineering-5-5",
      "title": "Calculation & Verification: Environmental evaluation and monitoring",
      "unit": 5,
      "question": "<p><strong>Problem Statement:</strong> A plant consumes 500,000 m\u00b3 of water while exporting 700,000 MWh(e) over the same annual period. Consumptive intensity is 500,000/700,000 = **0.714 m\u00b3/MWh**. Withdrawal volume could be much larger; report the two separately and document where water is returned.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** This accounting value is not a license to withdraw water or discharge heated effluent. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
    },
    {
      "id": "prob-power-plant-engineering-6-1",
      "title": "Calculation & Verification: Hydroelectric conversion and head",
      "unit": 6,
      "question": "<p><strong>Problem Statement:</strong> Take water density 1000 kg/m\u00b3, g = 9.81 m/s\u00b2, flow 40 m\u00b3/s, net head 75 m and total efficiency 0.90. Hydropower is 1000 \u00d7 9.81 \u00d7 40 \u00d7 75 \u00d7 0.90 = **26.487 MW(e)**. Actual output also depends on reservoir conditions, permitted releases and seasonal flow.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Using gross rather than net head causes a systematic overestimate of delivered power. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
    },
    {
      "id": "prob-power-plant-engineering-6-2",
      "title": "Calculation & Verification: Wind and variable-power capture",
      "unit": 6,
      "question": "<p><strong>Problem Statement:</strong> For air density 1.2 kg/m\u00b3, swept area 5000 m\u00b2, wind speed 8 m/s and power coefficient 0.42, idealized captured power is 0.5 \u00d7 1.2 \u00d7 5000 \u00d7 8\u00b3 \u00d7 0.42 = **0.645 MW**. Because wind power scales as the cube of speed, using the arithmetic mean wind speed in this formula cannot generally reproduce annual energy.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Do not assume Cp constant across wind speeds or disregard cut-in and cut-out limits. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
    },
    {
      "id": "prob-power-plant-engineering-6-3",
      "title": "Calculation & Verification: Solar photovoltaics and solar thermal",
      "unit": 6,
      "question": "<p><strong>Problem Statement:</strong> A 5000 m\u00b2 PV array receives irradiance 800 W/m\u00b2, has an assumed module efficiency of 20% and an overall performance ratio of 0.85. Net illustrative output is 800 \u00d7 5000 \u00d7 0.20 \u00d7 0.85 = **680 kW**. This is an instantaneous representative condition, not an annual yield estimate.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Shading, inverter clipping, temperature and soiling require more complete modeling. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
    },
    {
      "id": "prob-power-plant-engineering-6-4",
      "title": "Calculation & Verification: Geothermal and nuclear thermal boundaries",
      "unit": 6,
      "question": "<p><strong>Problem Statement:</strong> A thermal system receives 90 MW(th) and exports 25 MW(e). Its thermal-to-electric ratio is 25/90 = **27.78%** under the stated boundary. This value cannot establish whether the heat came from geothermal fluid, nuclear fission, concentrated solar heat or industrial waste heat, nor can it establish any source-specific safety conclusion.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Only source-specific professional studies can establish nuclear safety or geothermal sustainability. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
    },
    {
      "id": "prob-power-plant-engineering-6-5",
      "title": "Calculation & Verification: Hybrid storage, flexibility and capacity value",
      "unit": 6,
      "question": "<p><strong>Problem Statement:</strong> A battery is rated 20 MW discharge power for four hours of its nominal usable energy. The ideal delivered energy is 20 \u00d7 4 = **80 MWh**. An 88% round-trip efficiency means that cycling 80 MWh of delivered energy requires approximately 80/0.88 = **90.9 MWh** charge input under the simplified model.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Energy storage shifts delivery time and has losses; it is not a generator of net energy. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
    },
    {
      "id": "prob-power-plant-engineering-7-1",
      "title": "Calculation & Verification: Generator mechanical-electric conversion",
      "unit": 7,
      "question": "<p><strong>Problem Statement:</strong> At 3000 rpm a generator rotor turns at 3000 \u00d7 2\u03c0/60 = 314.16 rad/s. With shaft torque 250 kN\u00b7m, mechanical shaft power is 250,000 \u00d7 314.16 = **78.54 MW** before losses. A torque estimate based on 3000 rather than 314.16 would be dimensionally incorrect.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Rotor dynamics, overspeed margins and protective systems are outside this basic calculation. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
    },
    {
      "id": "prob-power-plant-engineering-7-2",
      "title": "Calculation & Verification: Three-phase output and power factor",
      "unit": 7,
      "question": "<p><strong>Problem Statement:</strong> A balanced three-phase generator has line voltage 11 kV, line current 5000 A and power factor 0.90. Real power is \u221a3 \u00d7 11,000 \u00d7 5000 \u00d7 0.90 = **85.74 MW**. Apparent power is about 95.26 MVA, a distinct quantity that matters for thermal loading.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** A three-phase formula must use consistent line-to-line voltage and line-current definitions. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
    },
    {
      "id": "prob-power-plant-engineering-7-3",
      "title": "Calculation & Verification: Frequency response and ramping",
      "unit": 7,
      "question": "<p><strong>Problem Statement:</strong> An operator record shows net output rising from 120 MW to 180 MW in 15 minutes. The average ramp rate is (180 \u2212 120)/15 = **4 MW/min**. This scalar does not mean the equipment can repeat the ramp indefinitely or that the grid operator may request it at any condition.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Turbine thermal stress, minimum stable generation and emission limits require independent operating constraints. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
    },
    {
      "id": "prob-power-plant-engineering-7-4",
      "title": "Calculation & Verification: Auxiliary systems and protection boundary",
      "unit": 7,
      "question": "<p><strong>Problem Statement:</strong> A generator terminal meter records 200 MW(e) while feedwater pumps, fans and other station loads consume 12 MW(e). Net export is **188 MW(e)**. A rise in auxiliary use from 12 to 16 MW lowers export to 184 MW even if generator terminal output remains unchanged.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Separate gross generation, contracted station service and net settlement-meter export. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
    },
    {
      "id": "prob-power-plant-engineering-7-5",
      "title": "Calculation & Verification: Operating data, state estimation and alarm review",
      "unit": 7,
      "question": "<p><strong>Problem Statement:</strong> A simple performance model predicts 38.0% net efficiency for a defined state, but a calibrated measurement yields 37.0%. Residual = measured minus predicted = **\u22121.0 percentage point**, approximately \u22122.63% relative to the prediction. Sensor uncertainty, differing fuel heating value and physical degradation are competing explanations.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** The residual is a diagnostic signal, not itself proof of a specific equipment fault. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
    },
    {
      "id": "prob-power-plant-engineering-8-1",
      "title": "Calculation & Verification: Failure modes and maintenance planning",
      "unit": 8,
      "question": "<p><strong>Problem Statement:</strong> In a simplified alternating failure-repair model, MTBF is 5000 h and mean repair time is 100 h. Operational availability is 5000/(5000 + 100) = **98.04%**. Planned maintenance, derated operation and common-cause failures are outside this two-number expression.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Annual capacity factor is not the same quantity as availability. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
    },
    {
      "id": "prob-power-plant-engineering-8-2",
      "title": "Calculation & Verification: Capacity credit and reserve planning",
      "unit": 8,
      "question": "<p><strong>Problem Statement:</strong> A 100 MW net-rated generator serves peaking demand and has annual capacity factor 25%. Its annual energy is 100 \u00d7 0.25 \u00d7 8760 = **219,000 MWh**. This output alone says nothing about the value of its availability during the 50 highest-price or highest-stress hours.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Capacity credit depends on system need and the probability of resource availability at critical times. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
    },
    {
      "id": "prob-power-plant-engineering-8-3",
      "title": "Calculation & Verification: Simple levelized energy cost",
      "unit": 8,
      "question": "<p><strong>Problem Statement:</strong> A project reports annualized fixed, fuel and operations cost totaling 40 million dollars and expected delivered annual energy of 800,000 MWh. Its simplified cost is $40,000,000/800,000 = **$50/MWh**. The figure is not a complete financed project LCOE unless the capital annualization, taxes, financing and other assumptions have been specified.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** A cheaper mean $/MWh may still fail to supply capacity, flexibility or the required environmental service. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
    },
    {
      "id": "prob-power-plant-engineering-8-4",
      "title": "Calculation & Verification: Lifecycle impacts and uncertainty",
      "unit": 8,
      "question": "<p><strong>Problem Statement:</strong> A lifecycle inventory attributes 400,000 tonnes of CO2-equivalent to a project, and lifetime net energy delivery is 5,000,000 MWh. The intensity is 400,000/5,000,000 = **0.08 t CO2e/MWh**, or 80 kg/MWh. Changes to the boundary\u2014construction, fuel supply, or end-of-life\u2014change the result.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** Uncertainty and allocation choices should be visible rather than hidden in one exact-looking number. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
    },
    {
      "id": "prob-power-plant-engineering-8-5",
      "title": "Calculation & Verification: Capstone integrated plant evaluation",
      "unit": 8,
      "question": "<p><strong>Problem Statement:</strong> A conceptual plant receives 400 MW(th), exports 155 MW(e), rejects 210 MW(th) through cooling, and has 25 MW(th) of other quantified losses. The unclosed energy residual is 400 \u2212 155 \u2212 210 \u2212 25 = **10 MW(th)**. The analyst must investigate this residual as possible unmeasured loss, stored-energy change, or measurement error; it must not silently disappear.</p>",
      "solution": "<div class=\"step-explanation\"><p><strong>Worked Engineering Derivation:</strong></p><p>**Verification and limitations.** A closed spreadsheet is not sufficient evidence of plant safety, emissions compliance or economic viability. The result is illustrative and does not replace equipment-specific property data, measurements or professional review.</p></div>"
    }
  ]
};
if (typeof module !== 'undefined') module.exports = COURSE_DATA;
if (typeof window !== 'undefined') window.COURSE_DATA = COURSE_DATA;
