/* Process Safety Interactive Simulation Suite */
(function(window) {
  'use strict';

  function f(n, d) { d = (d !== undefined) ? d : 2; return Number.isFinite(n) ? n.toFixed(d) : '0.00'; }

  var MODELS = [
    {
      idx: 1, unit: 1,
      html: '<header><span class="eyebrow">Unit 1 Laboratory</span><h3>Toxicity Dose-Response Probit Modeling</h3><p class="lead">Simulate toxic vapor exposure, probit variable Y, and percentage of affected population.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Toxic Concentration C <span><output id="v-conc">150</output> ppm</span></label><input type="range" id="s-conc" min="10" max="1000" step="10" value="150"></div>' +
              '<div class="control-group"><label>Exposure Duration t <span><output id="v-time">30</output> min</span></label><input type="range" id="s-time" min="5" max="120" step="5" value="30"></div>' +
              '<div class="control-group"><label>Chemical Substance <span><output id="v-chem">Chlorine (n=2.0)</output></span></label><input type="range" id="s-chem" min="1" max="2" step="1" value="1"></div>' +
              '<div class="control-group"><label>Population Sample <span><output id="v-pop">1000</output> People</span></label><input type="range" id="s-pop" min="100" max="5000" step="100" value="1000"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Toxic Dose (Cⁿ · t)</span><span class="value" id="r-dose">0</span><span class="subtext">ppmⁿ · min load</span></div>' +
              '<div class="readout-card"><span class="label">Probit Variable Y</span><span class="value" id="r-probit">0.00</span><span class="subtext">normal deviate + 5</span></div>' +
              '<div class="readout-card"><span class="label">Affected Fraction</span><span class="value" id="r-fatality">0.0%</span><span class="subtext">percentage affected</span></div>' +
              '<div class="readout-card"><span class="label">Casualties</span><span class="value" id="r-cas">0 People</span><span class="subtext">estimated count</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-psafe-u1" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-psafe-u1"></div>',
      init: function(card) {
        var sC = card.querySelector('#s-conc'), vC = card.querySelector('#v-conc');
        var sT = card.querySelector('#s-time'), vT = card.querySelector('#v-time');
        var sCh = card.querySelector('#s-chem'), vCh = card.querySelector('#v-chem');
        var sP = card.querySelector('#s-pop'), vP = card.querySelector('#v-pop');
        var rD = card.querySelector('#r-dose'), rY = card.querySelector('#r-probit');
        var rF = card.querySelector('#r-fatality'), rCas = card.querySelector('#r-cas');
        var svg = card.querySelector('#plot-psafe-u1'), diag = card.querySelector('#diag-psafe-u1');

        function update() {
          var C = parseFloat(sC.value); vC.textContent = f(C, 0);
          var t = parseFloat(sT.value); vT.textContent = f(t, 0);
          var isCl2 = parseInt(sCh.value, 10) === 1;
          vCh.textContent = isCl2 ? 'Chlorine (n=2.0)' : 'Ammonia (n=2.0)';
          var pop = parseInt(sP.value, 10); vP.textContent = pop;

          var k1 = isCl2 ? -8.29 : -35.9;
          var k2 = isCl2 ? 0.92 : 1.85;
          var n = 2.0;

          var dose = Math.pow(C, n) * t;
          var Y = k1 + k2 * Math.log(dose);
          Y = Math.max(0.1, Math.min(9.0, Y));

          // Probit to percentage: P = 50 * [1 + erf((Y - 5) / sqrt(2))]
          var z = (Y - 5.0) / 1.4142;
          var t_erf = 1.0 / (1.0 + 0.3275911 * Math.abs(z));
          var erf = 1.0 - (((((1.061405429 * t_erf - 1.453152027) * t_erf + 1.421413741) * t_erf - 0.284496736) * t_erf + 0.254829592) * t_erf) * Math.exp(-z * z);
          if (z < 0) erf = -erf;
          var pct = 50 * (1 + erf);
          pct = Math.max(0, Math.min(100, pct));
          var casualties = Math.round(pop * (pct / 100));

          rD.textContent = f(dose, 0);
          rY.textContent = f(Y, 2);
          rF.textContent = f(pct, 1) + ' %';
          rCas.textContent = casualties + ' People';

          // SVG Sigmoidal Probit Dose-Response Curve
          var dPath = 'M 60 170 ';
          for (var c_i = 10; c_i <= 1000; c_i += 20) {
            var d_i = Math.pow(c_i, n) * t;
            var y_i = k1 + k2 * Math.log(d_i);
            var z_i = (y_i - 5.0) / 1.4142;
            var t_i = 1.0 / (1.0 + 0.3275911 * Math.abs(z_i));
            var e_i = 1.0 - (((((1.061405429 * t_i - 1.453152027) * t_i + 1.421413741) * t_i - 0.284496736) * t_i + 0.254829592) * t_i) * Math.exp(-z_i * z_i);
            if (z_i < 0) e_i = -e_i;
            var p_i = 50 * (1 + e_i);
            p_i = Math.max(0, Math.min(100, p_i));
            var x_px = 60 + ((c_i - 10) / 990) * 480;
            var y_px = 170 - (p_i / 100) * 140;
            dPath += 'L ' + x_px.toFixed(1) + ' ' + y_px.toFixed(1) + ' ';
          }
          var cur_x = 60 + ((C - 10) / 990) * 480;
          var cur_y = 170 - (pct / 100) * 140;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="60" y1="170" x2="540" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<line x1="60" y1="30" x2="60" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<path d="' + dPath + '" fill="none" stroke="#dc2626" stroke-width="3"/>' +
                          '<circle cx="' + cur_x.toFixed(1) + '" cy="' + cur_y.toFixed(1) + '" r="6" fill="#ef4444" stroke="#fff" stroke-width="2"/>' +
                          '<text x="540" y="190" text-anchor="end" font-size="11" fill="#64748b">Concentration C (ppm)</text>' +
                          '<text x="50" y="30" font-size="11" fill="#64748b">Affected Population (%)</text>' +
                          '<text x="300" y="20" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Toxic Dose-Response: Y = ' + f(Y, 2) + ' (' + f(pct, 1) + '% Affected)</text>';
          diag.textContent = 'At ' + f(C, 0) + ' ppm for ' + f(t, 0) + ' minutes, the cumulative toxic dose is ' + f(dose, 0) + ' ppm²·min. Probit equation predicts Y = ' + f(Y, 2) + ', corresponding to ' + f(pct, 1) + '% affected fraction (' + casualties + ' individuals out of ' + pop + ').';
        }
        [sC, sT, sCh, sP].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 2, unit: 2,
      html: '<header><span class="eyebrow">Unit 2 Laboratory</span><h3>Runaway Reaction Thermal Sizing (ARC & DIERS)</h3><p class="lead">Simulate adiabatic exotherm rate dT/dt, self-heat onset, and time-to-maximum rate (TMR).</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Initial Temp T0 <span><output id="v-arcT0">340</output> K</span></label><input type="range" id="s-arcT0" min="300" max="420" step="5" value="340"></div>' +
              '<div class="control-group"><label>Exotherm Heat -ΔHr <span><output id="v-arcdh">90</output> kJ/mol</span></label><input type="range" id="s-arcdh" min="40" max="160" step="10" value="90"></div>' +
              '<div class="control-group"><label>Activation Energy Ea <span><output id="v-arcea">75</output> kJ/mol</span></label><input type="range" id="s-arcea" min="50" max="120" step="5" value="75"></div>' +
              '<div class="control-group"><label>Thermal Inertia Φ <span><output id="v-arcphi">1.25</output></span></label><input type="range" id="s-arcphi" min="1.05" max="2.00" step="0.05" value="1.25"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Self-Heat Rate</span><span class="value" id="r-shrate">0.0 K/min</span><span class="subtext">initial exotherm dT/dt</span></div>' +
              '<div class="readout-card"><span class="label">Adiabatic Rise ΔTad</span><span class="value" id="r-dtad">0 K</span><span class="subtext">maximum thermal surge</span></div>' +
              '<div class="readout-card"><span class="label">Time to Max Rate</span><span class="value" id="r-tmr">0 min</span><span class="subtext">TMR emergency window</span></div>' +
              '<div class="readout-card"><span class="label">Runaway Severity</span><span class="value" id="r-runsev">High</span><span class="subtext">venting urgency</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-psafe-u2" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-psafe-u2"></div>',
      init: function(card) {
        var sT0 = card.querySelector('#s-arcT0'), vT0 = card.querySelector('#v-arcT0');
        var sDh = card.querySelector('#s-arcdh'), vDh = card.querySelector('#v-arcdh');
        var sEa = card.querySelector('#s-arcea'), vEa = card.querySelector('#v-arcea');
        var sPhi = card.querySelector('#s-arcphi'), vPhi = card.querySelector('#v-arcphi');
        var rSh = card.querySelector('#r-shrate'), rDt = card.querySelector('#r-dtad');
        var rTmr = card.querySelector('#r-tmr'), rSev = card.querySelector('#r-runsev');
        var svg = card.querySelector('#plot-psafe-u2'), diag = card.querySelector('#diag-psafe-u2');

        function update() {
          var T0 = parseFloat(sT0.value); vT0.textContent = f(T0, 0);
          var dH = parseFloat(sDh.value); vDh.textContent = f(dH, 0);
          var Ea = parseFloat(sEa.value) * 1e3; vEa.textContent = f(Ea / 1e3, 0);
          var phi = parseFloat(sPhi.value); vPhi.textContent = f(phi, 2);

          var R = 8.314;
          var dTad = (dH * 1000 / (2200 * phi)); // adiabatic temperature rise in K
          var k0 = 1.0e9;
          var rate0 = (k0 * Math.exp(-Ea / (R * T0)) * dTad) * 60; // K/min
          rate0 = Math.max(0.01, rate0);
          var tmr = (R * T0 * T0 / (Ea * (rate0 / 60))) / 60; // min
          tmr = Math.max(0.5, tmr);

          rSh.textContent = f(rate0, 2) + ' K/min';
          rDt.textContent = f(dTad, 0) + ' K';
          rTmr.textContent = tmr < 120 ? f(tmr, 1) + ' min' : '>120 min';
          var sev = tmr < 15 ? 'CRITICAL (Imminent Runaway)' : (tmr < 60 ? 'High (Evacuate/Dump)' : 'Moderate');
          rSev.textContent = sev;
          rSev.style.color = tmr < 15 ? '#dc2626' : (tmr < 60 ? '#d97706' : '#15803d');

          // SVG temperature runaway trajectory
          var dPath = 'M 60 ' + (170 - ((T0 - 280) / 250) * 140).toFixed(1) + ' ';
          for (var t = 0; t <= Math.min(60, tmr * 1.2); t += Math.min(60, tmr * 1.2) / 30) {
            var frac = t / tmr;
            var T_t = T0 + dTad / Math.max(0.01, (1.0 - Math.pow(Math.min(0.99, frac), 2)));
            T_t = Math.min(T0 + dTad, T_t);
            var x_px = 60 + (t / Math.min(60, tmr * 1.2)) * 480;
            var y_px = 170 - ((T_t - 280) / 250) * 140;
            y_px = Math.min(170, Math.max(20, y_px));
            dPath += 'L ' + x_px.toFixed(1) + ' ' + y_px.toFixed(1) + ' ';
          }

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="60" y1="170" x2="540" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<path d="' + dPath + '" fill="none" stroke="#dc2626" stroke-width="3"/>' +
                          '<text x="540" y="190" text-anchor="end" font-size="11" fill="#64748b">Time (min)</text>' +
                          '<text x="50" y="30" font-size="11" fill="#64748b">Core Temperature (K)</text>' +
                          '<text x="300" y="20" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Adiabatic Runaway: TMR = ' + f(tmr, 1) + ' min (ΔTad = ' + f(dTad, 0) + ' K)</text>';
          diag.textContent = 'DIERS runaway kinetic evaluation: Self-heating begins at ' + f(rate0, 2) + ' K/min. Adiabatic temperature rise is ΔTad = ' + f(dTad, 0) + ' K. Time to maximum rate is ' + f(tmr, 1) + ' minutes, defining the emergency window for inhibitor injection or emergency relief venting.';
        }
        [sT0, sDh, sEa, sPhi].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 3, unit: 3,
      html: '<header><span class="eyebrow">Unit 3 Laboratory</span><h3>Gaussian Plume Atmospheric Toxic Dispersion</h3><p class="lead">Simulate wind speed u, Pasquill-Gifford stability class, and downwind toxic footprint.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Release Rate Q <span><output id="v-relq">25</output> kg/s</span></label><input type="range" id="s-relq" min="5" max="100" step="5" value="25"></div>' +
              '<div class="control-group"><label>Wind Speed u <span><output id="v-wind">3.5</output> m/s</span></label><input type="range" id="s-wind" min="1.0" max="12.0" step="0.5" value="3.5"></div>' +
              '<div class="control-group"><label>Stability Class <span><output id="v-pgclass">Class D (Neutral)</output></span></label><input type="range" id="s-pgclass" min="1" max="3" step="1" value="2"></div>' +
              '<div class="control-group"><label>Release Height H <span><output id="v-relh">10</output> m</span></label><input type="range" id="s-relh" min="0" max="40" step="5" value="10"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Ground Peak Cmax</span><span class="value" id="r-cpeak">0 mg/m³</span><span class="subtext">centerline maximum</span></div>' +
              '<div class="readout-card"><span class="label">Distance to Peak xmax</span><span class="value" id="r-dpeak">0 m</span><span class="subtext">downwind touchdown</span></div>' +
              '<div class="readout-card"><span class="label">IDLH Hazard Radius</span><span class="value" id="r-idlh">0 m</span><span class="subtext">lethal boundary</span></div>' +
              '<div class="readout-card"><span class="label">ERPAG-2 Boundary</span><span class="value" id="r-erpg">0 m</span><span class="subtext">evacuation zone</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-psafe-u3" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-psafe-u3"></div>',
      init: function(card) {
        var sQ = card.querySelector('#s-relq'), vQ = card.querySelector('#v-relq');
        var sU = card.querySelector('#s-wind'), vU = card.querySelector('#v-wind');
        var sC = card.querySelector('#s-pgclass'), vC = card.querySelector('#v-pgclass');
        var sH = card.querySelector('#s-relh'), vH = card.querySelector('#v-relh');
        var rPeak = card.querySelector('#r-cpeak'), rDpeak = card.querySelector('#r-dpeak');
        var rIdlh = card.querySelector('#r-idlh'), rErpg = card.querySelector('#r-erpg');
        var svg = card.querySelector('#plot-psafe-u3'), diag = card.querySelector('#diag-psafe-u3');

        function update() {
          var Q = parseFloat(sQ.value); vQ.textContent = f(Q, 0);
          var u = parseFloat(sU.value); vU.textContent = f(u, 1);
          var pg = parseInt(sC.value, 10);
          var pgNames = ['Class B (Unstable)', 'Class D (Neutral)', 'Class F (Stable/Inversion)'];
          vC.textContent = pgNames[pg - 1];
          var H = parseFloat(sH.value); vH.textContent = f(H, 0);

          var sigCoeff = pg === 1 ? 0.16 : (pg === 2 ? 0.08 : 0.04);
          var xmax = H > 0 ? (H / (1.414 * sigCoeff)) * 1.5 : 50;
          var cpeak = (Q * 1e6) / (Math.PI * u * Math.pow(sigCoeff * Math.max(50, xmax), 2));
          cpeak = Math.min(25000, cpeak);
          var idlhR = Math.round(xmax * 1.8 * Math.sqrt(Q / 25));
          var erpgR = Math.round(idlhR * 2.4);

          rPeak.textContent = f(cpeak, 0) + ' mg/m³';
          rDpeak.textContent = f(xmax, 0) + ' m';
          rIdlh.textContent = idlhR + ' m';
          rErpg.textContent = erpgR + ' m';

          // SVG Plume footprint profile
          var dPath = 'M 60 170 ';
          for (var x = 50; x <= 3000; x += 100) {
            var sy = sigCoeff * x;
            var sz = sigCoeff * x * 0.6;
            var c_x = (Q * 1e6) / (2 * Math.PI * u * sy * sz) * Math.exp(-0.5 * Math.pow(H / sz, 2));
            var x_px = 60 + ((x - 50) / 2950) * 480;
            var y_px = 170 - (Math.min(2000, c_x) / 2000) * 140;
            dPath += 'L ' + x_px.toFixed(1) + ' ' + y_px.toFixed(1) + ' ';
          }

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="60" y1="170" x2="540" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<path d="' + dPath + '" fill="none" stroke="#ea580c" stroke-width="3"/>' +
                          '<rect x="60" y="' + (170 - H * 1.5).toFixed(1) + '" width="8" height="' + (H * 1.5).toFixed(1) + '" fill="#475569"/>' +
                          '<text x="540" y="190" text-anchor="end" font-size="11" fill="#64748b">Downwind Distance x (m)</text>' +
                          '<text x="50" y="30" font-size="11" fill="#64748b">Ground Concentration (mg/m³)</text>' +
                          '<text x="300" y="20" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Gaussian Plume Dispersion (' + pgNames[pg-1] + ', u = ' + f(u,1) + ' m/s)</text>';
          diag.textContent = 'Atmospheric dispersion under ' + pgNames[pg - 1] + ' with wind speed ' + f(u, 1) + ' m/s: Plume touches down at maximum ground concentration ' + f(cpeak, 0) + ' mg/m³ at x = ' + f(xmax, 0) + ' m. Lethal IDLH boundary extends to ' + idlhR + ' m downwind.';
        }
        [sQ, sU, sC, sH].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 4, unit: 4,
      html: '<header><span class="eyebrow">Unit 4 Laboratory</span><h3>Structured HAZOP Guide-Word Risk Evaluation</h3><p class="lead">Simulate parameter deviations (More Flow, High Pressure, Reverse Flow) and risk rank reduction.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>HAZOP Guide Word <span><output id="v-gword">MORE FLOW</output></span></label><input type="range" id="s-gword" min="1" max="3" step="1" value="1"></div>' +
              '<div class="control-group"><label>Initial Severity S <span><output id="v-initsev">Catastrophic (4)</output></span></label><input type="range" id="s-initsev" min="1" max="4" step="1" value="4"></div>' +
              '<div class="control-group"><label>Initial Likelihood L <span><output id="v-initlik">Occasional (3)</output></span></label><input type="range" id="s-initlik" min="1" max="4" step="1" value="3"></div>' +
              '<div class="control-group"><label>Safeguard Credit <span><output id="v-safeg">PSV + Interlock (2 Layers)</output></span></label><input type="range" id="s-safeg" min="0" max="3" step="1" value="2"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Initial Risk Rank</span><span class="value" id="r-initrisk">Level 12 (High)</span><span class="subtext">unmitigated score</span></div>' +
              '<div class="readout-card"><span class="label">Residual Likelihood</span><span class="value" id="r-reslik">Improbable (1)</span><span class="subtext">after safeguards</span></div>' +
              '<div class="readout-card"><span class="label">Residual Risk Rank</span><span class="value" id="r-resrisk">Level 4 (Low)</span><span class="subtext">mitigated condition</span></div>' +
              '<div class="readout-card"><span class="label">ALARP Status</span><span class="value" id="r-alarp">Acceptable</span><span class="subtext">risk tolerance check</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-psafe-u4" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-psafe-u4"></div>',
      init: function(card) {
        var sG = card.querySelector('#s-gword'), vG = card.querySelector('#v-gword');
        var sS = card.querySelector('#s-initsev'), vS = card.querySelector('#v-initsev');
        var sL = card.querySelector('#s-initlik'), vL = card.querySelector('#v-initlik');
        var sSaf = card.querySelector('#s-safeg'), vSaf = card.querySelector('#v-safeg');
        var rIR = card.querySelector('#r-initrisk'), rRL = card.querySelector('#r-reslik');
        var rRR = card.querySelector('#r-resrisk'), rAl = card.querySelector('#r-alarp');
        var svg = card.querySelector('#plot-psafe-u4'), diag = card.querySelector('#diag-psafe-u4');

        function update() {
          var g = parseInt(sG.value, 10);
          var gWords = ['MORE FLOW (Pump Runaway)', 'HIGH PRESSURE (Blockage)', 'REVERSE FLOW (Backflow Check)'];
          vG.textContent = gWords[g - 1];
          var S = parseInt(sS.value, 10);
          var sNames = ['Minor (1)', 'Moderate (2)', 'Critical (3)', 'Catastrophic (4)'];
          vS.textContent = sNames[S - 1];
          var L = parseInt(sL.value, 10);
          var lNames = ['Improbable (1)', 'Remote (2)', 'Occasional (3)', 'Frequent (4)'];
          vL.textContent = lNames[L - 1];
          var saf = parseInt(sSaf.value, 10);
          vSaf.textContent = saf === 0 ? 'None (Unmitigated)' : (saf === 1 ? 'Alarm Only (1 Layer)' : (saf === 2 ? 'PSV + Interlock (2 Layers)' : 'SIF SIL-2 Certified (3 Layers)'));

          var initScore = S * L;
          var resL = Math.max(1, L - saf);
          var resScore = S * resL;
          var isAlarp = resScore <= 4;

          rIR.textContent = 'Level ' + initScore + (initScore >= 9 ? ' (High)' : ' (Medium)');
          rIR.style.color = initScore >= 9 ? '#dc2626' : '#d97706';
          rRL.textContent = lNames[resL - 1];
          rRR.textContent = 'Level ' + resScore + (resScore <= 4 ? ' (Low)' : ' (Medium)');
          rRR.style.color = resScore <= 4 ? '#15803d' : '#d97706';
          rAl.textContent = isAlarp ? 'ALARP Acceptable' : 'Unacceptable (Add Layer)';
          rAl.style.color = isAlarp ? '#15803d' : '#dc2626';

          // SVG 4x4 Risk Matrix Grid
          var gridSvg = '';
          for (var r = 0; r < 4; r++) {
            for (var c = 0; c < 4; c++) {
              var score = (4 - r) * (c + 1);
              var col = score >= 9 ? '#fee2e2' : (score >= 6 ? '#fef3c7' : '#dcfce7');
              gridSvg += '<rect x="' + (240 + c * 50) + '" y="' + (35 + r * 35) + '" width="46" height="31" fill="' + col + '" stroke="#cbd5e1" rx="2"/>' +
                         '<text x="' + (263 + c * 50) + '" y="' + (55 + r * 35) + '" text-anchor="middle" font-size="10" font-weight="700" fill="#334155">' + score + '</text>';
            }
          }
          // Highlight initial and residual points
          var initX = 240 + (L - 1) * 50 + 23;
          var initY = 35 + (4 - S) * 35 + 15;
          var resX = 240 + (resL - 1) * 50 + 23;
          var resY = 35 + (4 - S) * 35 + 15;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          gridSvg +
                          '<circle cx="' + initX + '" cy="' + initY + '" r="8" fill="#ef4444" stroke="#fff" stroke-width="2"/>' +
                          '<circle cx="' + resX + '" cy="' + resY + '" r="8" fill="#10b981" stroke="#fff" stroke-width="2"/>' +
                          '<line x1="' + initX + '" y1="' + initY + '" x2="' + resX + '" y2="' + resY + '" stroke="#0f172a" stroke-width="2" stroke-dasharray="3"/>' +
                          '<text x="130" y="70" font-size="11" font-weight="700" fill="#dc2626">Initial: Score ' + initScore + '</text>' +
                          '<text x="130" y="100" font-size="11" font-weight="700" fill="#059669">Residual: Score ' + resScore + '</text>' +
                          '<text x="130" y="130" font-size="11" fill="#475569">Deviation: ' + gWords[g-1].split(' ')[0] + '</text>' +
                          '<text x="340" y="22" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">HAZOP Risk Matrix (Red: Unmitigated, Green: Safeguarded)</text>';
          diag.textContent = 'HAZOP review for deviation [' + gWords[g - 1] + ']: Initial unmitigated risk score is ' + initScore + ' (Severity ' + S + ', Likelihood ' + L + '). Applying ' + saf + ' independent protection layer(s) reduces residual likelihood to ' + resL + ' (Score ' + resScore + '), achieving ' + (isAlarp ? 'ALARP compliance.' : 'further engineering controls mandated.');
        }
        [sG, sS, sL, sSaf].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 5, unit: 5,
      html: '<header><span class="eyebrow">Unit 5 Laboratory</span><h3>Layer of Protection Analysis (LOPA) & SIL Verification</h3><p class="lead">Simulate initiating event frequency (IEF), independent protection layer PFD, and SIL allocation.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Initiating Freq (IEF) <span><output id="v-ief">1.0e-1</output> /yr</span></label><input type="range" id="s-ief" min="1" max="4" step="1" value="2"></div>' +
              '<div class="control-group"><label>Alarm PFD <span><output id="v-alrm">0.10</output></span></label><input type="range" id="s-alrm" min="0.05" max="0.30" step="0.05" value="0.10"></div>' +
              '<div class="control-group"><label>PSV Mechanical PFD <span><output id="v-psvpfd">0.01</output></span></label><input type="range" id="s-psvpfd" min="0.005" max="0.050" step="0.005" value="0.010"></div>' +
              '<div class="control-group"><label>Target Mitigated Freq <span><output id="v-tmf">1.0e-5</output> /yr</span></label><input type="range" id="s-tmf" min="4" max="6" step="1" value="5"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Mitigated Freq (MEF)</span><span class="value" id="r-mef">0 /yr</span><span class="subtext">with base safeguards</span></div>' +
              '<div class="readout-card"><span class="label">Required RRF</span><span class="value" id="r-rrf">0</span><span class="subtext">risk reduction factor</span></div>' +
              '<div class="readout-card"><span class="label">Target SIF SIL</span><span class="value" id="r-sil">SIL 1</span><span class="subtext">IEC 61511 allocation</span></div>' +
              '<div class="readout-card"><span class="label">SIF Achieved PFD</span><span class="value" id="r-sifpfd">1.0e-2</span><span class="subtext">required probability</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-psafe-u5" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-psafe-u5"></div>',
      init: function(card) {
        var sI = card.querySelector('#s-ief'), vI = card.querySelector('#v-ief');
        var sA = card.querySelector('#s-alrm'), vA = card.querySelector('#v-alrm');
        var sP = card.querySelector('#s-psvpfd'), vP = card.querySelector('#v-psvpfd');
        var sT = card.querySelector('#s-tmf'), vT = card.querySelector('#v-tmf');
        var rM = card.querySelector('#r-mef'), rR = card.querySelector('#r-rrf');
        var rS = card.querySelector('#r-sil'), rPfd = card.querySelector('#r-sifpfd');
        var svg = card.querySelector('#plot-psafe-u5'), diag = card.querySelector('#diag-psafe-u5');

        function update() {
          var iefExp = parseInt(sI.value, 10);
          var ief = Math.pow(10, -iefExp); vI.textContent = '1.0e-' + iefExp;
          var pfdAlarm = parseFloat(sA.value); vA.textContent = f(pfdAlarm, 2);
          var pfdPSV = parseFloat(sP.value); vP.textContent = f(pfdPSV, 3);
          var tmfExp = parseInt(sT.value, 10);
          var targetFreq = Math.pow(10, -tmfExp); vT.textContent = '1.0e-' + tmfExp;

          var mef = ief * pfdAlarm * pfdPSV;
          var rrf = mef / targetFreq;
          var sil = rrf <= 1 ? 'None (Base OK)' : (rrf <= 100 ? 'SIL 1 (RRF 10-100)' : (rrf <= 1000 ? 'SIL 2 (RRF 100-1000)' : 'SIL 3 (RRF >1000)'));
          var sifPfd = rrf > 1 ? 1 / rrf : 1.0;

          rM.textContent = mef.toExponential(1) + ' /yr';
          rR.textContent = rrf > 1 ? f(rrf, 0) : '1 (Compliant)';
          rS.textContent = sil;
          rS.style.color = rrf > 1000 ? '#dc2626' : (rrf > 100 ? '#ea580c' : '#15803d');
          rPfd.textContent = sifPfd.toExponential(1);

          // SVG LOPA Onion Barrier Bars
          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="80" y="50" width="80" height="90" fill="#fed7aa" stroke="#ea580c" stroke-width="2" rx="4"/>' +
                          '<text x="120" y="90" text-anchor="middle" font-size="10" font-weight="700" fill="#9a3412">Initiating</text>' +
                          '<text x="120" y="105" text-anchor="middle" font-size="11" font-weight="800" fill="#9a3412">1e-' + iefExp + '</text>' +
                          '<rect x="200" y="50" width="80" height="90" fill="#dbeafe" stroke="#2563eb" stroke-width="2" rx="4"/>' +
                          '<text x="240" y="90" text-anchor="middle" font-size="10" font-weight="700" fill="#1e40af">Alarm BPCS</text>' +
                          '<text x="240" y="105" text-anchor="middle" font-size="11" font-weight="800" fill="#1e40af">PFD ' + f(pfdAlarm,2) + '</text>' +
                          '<rect x="320" y="50" width="80" height="90" fill="#e0e7ff" stroke="#4f46e5" stroke-width="2" rx="4"/>' +
                          '<text x="360" y="90" text-anchor="middle" font-size="10" font-weight="700" fill="#3730a3">Relief PSV</text>' +
                          '<text x="360" y="105" text-anchor="middle" font-size="11" font-weight="800" fill="#3730a3">PFD ' + f(pfdPSV,3) + '</text>' +
                          '<rect x="440" y="50" width="90" height="90" fill="' + (rrf > 1 ? '#fef3c7' : '#dcfce7') + '" stroke="' + (rrf > 1 ? '#d97706' : '#15803d') + '" stroke-width="2" rx="4"/>' +
                          '<text x="485" y="90" text-anchor="middle" font-size="10" font-weight="700" fill="' + (rrf > 1 ? '#92400e' : '#166534') + '">Target SIF</text>' +
                          '<text x="485" y="105" text-anchor="middle" font-size="11" font-weight="800" fill="' + (rrf > 1 ? '#92400e' : '#166534') + '">' + sil.split(' ')[0] + '</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">LOPA Protection Layers (Target Mitigated Freq: 1.0e-' + tmfExp + '/yr)</text>' +
                          '<text x="300" y="175" text-anchor="middle" font-size="11" fill="#475569">Required Risk Reduction Factor RRF = ' + (rrf > 1 ? f(rrf,0) : '1.0') + '</text>';
          diag.textContent = 'LOPA allocation: Initiating event frequency of 1e-' + iefExp + '/yr with base independent protection layers (BPCS alarm PFD ' + f(pfdAlarm, 2) + ', PSV PFD ' + f(pfdPSV, 3) + ') yields an intermediate event frequency of ' + mef.toExponential(1) + '/yr. Meeting corporate target of 1e-' + tmfExp + '/yr requires ' + sil + ' with RRF = ' + (rrf > 1 ? f(rrf, 0) : '1.0') + '.';
        }
        [sI, sA, sP, sT].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 6, unit: 6,
      html: '<header><span class="eyebrow">Unit 6 Laboratory</span><h3>Emergency Relief Valve Orifice Sizing (API 520)</h3><p class="lead">Simulate relief mass flow W, relieving pressure P1, and determine ASME/API standard orifice letter.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Relief Flow W <span><output id="v-relw">12000</output> kg/h</span></label><input type="range" id="s-relw" min="2000" max="50000" step="2000" value="12000"></div>' +
              '<div class="control-group"><label>Relieving Pressure P1 <span><output id="v-relp1">8.0</output> bar-g</span></label><input type="range" id="s-relp1" min="2.0" max="30.0" step="1.0" value="8.0"></div>' +
              '<div class="control-group"><label>Relieving Temp T <span><output id="v-relt">380</output> K</span></label><input type="range" id="s-relt" min="300" max="550" step="10" value="380"></div>' +
              '<div class="control-group"><label>Gas Mol Weight MW <span><output id="v-relmw">44.0</output> g/mol</span></label><input type="range" id="s-relmw" min="16.0" max="100.0" step="2.0" value="44.0"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Required Area A</span><span class="value" id="r-psvarea">0 mm²</span><span class="subtext">API 520 critical flow</span></div>' +
              '<div class="readout-card"><span class="label">Selected Orifice</span><span class="value" id="r-psvletter">Letter G</span><span class="subtext">API standard designation</span></div>' +
              '<div class="readout-card"><span class="label">Standard Area</span><span class="value" id="r-psvstd">324 mm²</span><span class="subtext">actual orifice size</span></div>' +
              '<div class="readout-card"><span class="label">Overpressure Margin</span><span class="value" id="r-psvovr">10%</span><span class="subtext">ASME Code allowance</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-psafe-u6" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-psafe-u6"></div>',
      init: function(card) {
        var sW = card.querySelector('#s-relw'), vW = card.querySelector('#v-relw');
        var sP = card.querySelector('#s-relp1'), vP = card.querySelector('#v-relp1');
        var sT = card.querySelector('#s-relt'), vT = card.querySelector('#v-relt');
        var sM = card.querySelector('#s-relmw'), vM = card.querySelector('#v-relmw');
        var rA = card.querySelector('#r-psvarea'), rLet = card.querySelector('#r-psvletter');
        var rStd = card.querySelector('#r-psvstd'), rOvr = card.querySelector('#r-psvovr');
        var svg = card.querySelector('#plot-psafe-u6'), diag = card.querySelector('#diag-psafe-u6');

        function update() {
          var W = parseFloat(sW.value); vW.textContent = f(W, 0);
          var P1_g = parseFloat(sP.value); vP.textContent = f(P1_g, 1);
          var T = parseFloat(sT.value); vT.textContent = f(T, 0);
          var MW = parseFloat(sM.value); vM.textContent = f(MW, 1);

          var P1_abs = (P1_g + 1.013) * 1.10 * 100; // kPa (with 10% overpressure)
          var k = 1.3;
          var C_gas = 0.03948 * Math.sqrt(k * Math.pow(2 / (k + 1), (k + 1) / (k - 1)));
          var Kd = 0.975;

          // API 520 gas sizing: A = W / (C_gas * Kd * P1 * sqrt(MW / (Z * T))) [mm2]
          var reqArea = (W / (C_gas * Kd * P1_abs * Math.sqrt(MW / T))) * 10;
          reqArea = Math.max(20, reqArea);

          // API Orifice table
          var orifices = [
            { let: 'D', a: 71 }, { let: 'E', a: 126 }, { let: 'F', a: 198 },
            { let: 'G', a: 324 }, { let: 'H', a: 506 }, { let: 'J', a: 830 },
            { let: 'K', a: 1186 }, { let: 'L', a: 1841 }, { let: 'M', a: 2323 },
            { let: 'N', a: 2800 }, { let: 'P', a: 4116 }, { let: 'Q', a: 7129 }
          ];
          var sel = orifices.find(function(o) { return o.a >= reqArea; }) || orifices[orifices.length - 1];

          rA.textContent = f(reqArea, 0) + ' mm²';
          rLet.textContent = 'API Orifice ' + sel.let;
          rStd.textContent = sel.a + ' mm²';
          rOvr.textContent = '10% (ASME VIII)';

          // SVG relief valve diagram
          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<path d="M 270 170 L 270 110 L 230 110 L 230 90 L 370 90 L 370 110 L 330 110 L 330 170 Z" fill="#e2e8f0" stroke="#334155" stroke-width="2"/>' +
                          '<rect x="285" y="40" width="30" height="50" fill="#94a3b8" rx="3"/>' +
                          '<line x1="300" y1="45" x2="300" y2="85" stroke="#ef4444" stroke-width="4"/>' +
                          '<line x1="330" y1="100" x2="440" y2="100" stroke="#0284c7" stroke-width="4"/>' +
                          '<text x="450" y="104" font-size="11" font-weight="700" fill="#0284c7">Vent to Flare</text>' +
                          '<text x="300" y="145" text-anchor="middle" font-size="13" font-weight="800" fill="#1e40af">Orifice ' + sel.let + ' (' + sel.a + ' mm²)</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">API 520 Relief Sizing: Required Area = ' + f(reqArea, 0) + ' mm²</text>';
          diag.textContent = 'For relieving vapor flow W = ' + f(W, 0) + ' kg/h at P1 = ' + f(P1_g, 1) + ' bar-g (accumulated pressure ' + f(P1_abs/100, 2) + ' bar-a), required effective discharge area is ' + f(reqArea, 0) + ' mm². Next standard API size selected: Orifice letter ' + sel.let + ' (' + sel.a + ' mm²).';
        }
        [sW, sP, sT, sM].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 7, unit: 7,
      html: '<header><span class="eyebrow">Unit 7 Laboratory</span><h3>Vapor Cloud Explosion (VCE) Blast Overpressure</h3><p class="lead">Simulate fuel mass M, TNT equivalent efficiency, and blast overpressure ΔP(R) damage zones.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Flammable Mass M <span><output id="v-vmass">5000</output> kg</span></label><input type="range" id="s-vmass" min="500" max="25000" step="500" value="5000"></div>' +
              '<div class="control-group"><label>TNT Yield Equiv η <span><output id="v-tyield">5.0%</output></span></label><input type="range" id="s-tyield" min="1.0" max="15.0" step="0.5" value="5.0"></div>' +
              '<div class="control-group"><label>Target Distance R <span><output id="v-vdist">120</output> m</span></label><input type="range" id="s-vdist" min="20" max="500" step="10" value="120"></div>' +
              '<div class="control-group"><label>Congestion Level <span><output id="v-vcong">Medium Rig</output></span></label><input type="range" id="s-vcong" min="1" max="2" step="1" value="1"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">TNT Equivalent Mass</span><span class="value" id="r-tntm">0 kg TNT</span><span class="subtext">energy yield</span></div>' +
              '<div class="readout-card"><span class="label">Overpressure ΔP</span><span class="value" id="r-ovrp">0 kPa</span><span class="subtext">blast peak side-on</span></div>' +
              '<div class="readout-card"><span class="label">Damage Severity</span><span class="value" id="r-damsev">Moderate</span><span class="subtext">structural impact</span></div>' +
              '<div class="readout-card"><span class="label">Safe Stand-off</span><span class="value" id="r-soff">0 m</span><span class="subtext">threshold < 7 kPa</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-psafe-u7" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-psafe-u7"></div>',
      init: function(card) {
        var sM = card.querySelector('#s-vmass'), vM = card.querySelector('#v-vmass');
        var sY = card.querySelector('#s-tyield'), vY = card.querySelector('#v-tyield');
        var sR = card.querySelector('#s-vdist'), vR = card.querySelector('#v-vdist');
        var sC = card.querySelector('#s-vcong'), vC = card.querySelector('#v-vcong');
        var rTnt = card.querySelector('#r-tntm'), rOvr = card.querySelector('#r-ovrp');
        var rDam = card.querySelector('#r-damsev'), rSoff = card.querySelector('#r-soff');
        var svg = card.querySelector('#plot-psafe-u7'), diag = card.querySelector('#diag-psafe-u7');

        function update() {
          var M = parseFloat(sM.value); vM.textContent = f(M, 0);
          var eta = parseFloat(sY.value) / 100; vY.textContent = f(eta * 100, 1) + '%';
          var R = parseFloat(sR.value); vR.textContent = f(R, 0);
          var isHighCong = parseInt(sC.value, 10) === 2;
          vC.textContent = isHighCong ? 'High Pipe Congestion' : 'Medium Rig / Open Unit';

          var Hc = 46000; // kJ/kg (hydrocarbon heat of combustion)
          var H_TNT = 4686; // kJ/kg TNT
          var W_TNT = (eta * M * Hc) / H_TNT; // kg TNT

          var z = R / Math.pow(W_TNT, 1 / 3); // scaled distance m / kg^(1/3)
          var dP = 100 * (807 / Math.pow(z, 1.3)) * (isHighCong ? 1.4 : 1.0) / 100;
          dP = Math.min(250, Math.max(1.0, dP));
          var safeR = Math.round(Math.pow(807 * 100 / 7.0, 1 / 1.3) * Math.pow(W_TNT, 1 / 3) * (isHighCong ? 1.25 : 1.0));

          var dam = dP > 70 ? 'Total Structural Destruction' : (dP > 35 ? 'Heavy Cladding & Frame Damage' : (dP > 14 ? 'Partial Collapse / Ear Rupture' : 'Window Glass Shatter'));

          rTnt.textContent = f(W_TNT, 0) + ' kg TNT';
          rOvr.textContent = f(dP, 1) + ' kPa';
          rDam.textContent = dam;
          rDam.style.color = dP > 35 ? '#dc2626' : (dP > 14 ? '#ea580c' : '#15803d');
          rSoff.textContent = safeR + ' m';

          // SVG Overpressure vs Distance curve
          var dPath = 'M 60 ';
          for (var r_i = 20; r_i <= 500; r_i += 15) {
            var z_i = r_i / Math.pow(W_TNT, 1 / 3);
            var dp_i = (807 / Math.pow(z_i, 1.3)) * (isHighCong ? 1.4 : 1.0);
            dp_i = Math.min(150, Math.max(1.0, dp_i));
            var x_px = 60 + ((r_i - 20) / 480) * 480;
            var y_px = 170 - (dp_i / 150) * 140;
            if (r_i === 20) dPath += y_px.toFixed(1) + ' ';
            else dPath += 'L ' + x_px.toFixed(1) + ' ' + y_px.toFixed(1) + ' ';
          }
          var cur_x = 60 + ((R - 20) / 480) * 480;
          var cur_y = 170 - (dP / 150) * 140;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="60" y1="170" x2="540" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<line x1="60" y1="' + (170 - (7 / 150) * 140).toFixed(1) + '" x2="540" y2="' + (170 - (7 / 150) * 140).toFixed(1) + '" stroke="#cbd5e1" stroke-dasharray="4"/>' +
                          '<text x="540" y="' + (165 - (7 / 150) * 140).toFixed(1) + '" text-anchor="end" font-size="10" fill="#64748b">7 kPa Safe Window Limit</text>' +
                          '<path d="' + dPath + '" fill="none" stroke="#dc2626" stroke-width="3"/>' +
                          '<circle cx="' + cur_x.toFixed(1) + '" cy="' + cur_y.toFixed(1) + '" r="6" fill="#ef4444" stroke="#fff" stroke-width="2"/>' +
                          '<text x="540" y="190" text-anchor="end" font-size="11" fill="#64748b">Distance R (m)</text>' +
                          '<text x="50" y="30" font-size="11" fill="#64748b">Peak Overpressure ΔP (kPa)</text>' +
                          '<text x="300" y="20" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">VCE Blast Wave: ' + f(W_TNT, 0) + ' kg TNT Equiv (ΔP = ' + f(dP, 1) + ' kPa at ' + f(R,0) + 'm)</text>';
          diag.textContent = 'Vapor cloud explosion consequence: ' + f(M, 0) + ' kg fuel cloud at ' + f(eta * 100, 1) + '% blast yield produces an equivalent explosion energy of ' + f(W_TNT, 0) + ' kg TNT. At stand-off distance R = ' + f(R, 0) + ' m, side-on peak overpressure is ' + f(dP, 1) + ' kPa, causing ' + dam + '. Safe separation distance (<7 kPa) is ' + safeR + ' m.';
        }
        [sM, sY, sR, sC].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 8, unit: 8,
      html: '<header><span class="eyebrow">Unit 8 Laboratory</span><h3>Process Safety Management (PSM) Leading vs Lagging Metrics</h3><p class="lead">Simulate near-miss reporting, mechanical integrity inspection backlogs, and Tier 1 loss of containment.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Near-Miss Reports <span><output id="v-nmis">120</output>/yr</span></label><input type="range" id="s-nmis" min="10" max="300" step="10" value="120"></div>' +
              '<div class="control-group"><label>Inspection Backlog <span><output id="v-iblog">5%</output></span></label><input type="range" id="s-iblog" min="0" max="25" step="1" value="5"></div>' +
              '<div class="control-group"><label>Audit Action Closure <span><output id="v-audclos">95%</output></span></label><input type="range" id="s-audclos" min="70" max="100" step="5" value="95"></div>' +
              '<div class="control-group"><label>Management of Change <span><output id="v-moc">Formal (100%)</output></span></label><input type="range" id="s-moc" min="1" max="2" step="1" value="2"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Leading Health Score</span><span class="value" id="r-leadscore">92%</span><span class="subtext">proactive culture</span></div>' +
              '<div class="readout-card"><span class="label">Predicted Tier 1 PSE</span><span class="value" id="r-tier1">0.02 /yr</span><span class="subtext">major release frequency</span></div>' +
              '<div class="readout-card"><span class="label">PSM Integrity Band</span><span class="value" id="r-psmband">Industry Leader</span><span class="subtext">compliance level</span></div>' +
              '<div class="readout-card"><span class="label">Loss Prevention Cost</span><span class="value" id="r-lpcost">$1.2 M/yr</span><span class="subtext">maintenance & inspection</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-psafe-u8" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-psafe-u8"></div>',
      init: function(card) {
        var sN = card.querySelector('#s-nmis'), vN = card.querySelector('#v-nmis');
        var sB = card.querySelector('#s-iblog'), vB = card.querySelector('#v-iblog');
        var sA = card.querySelector('#s-audclos'), vA = card.querySelector('#v-audclos');
        var sM = card.querySelector('#s-moc'), vM = card.querySelector('#v-moc');
        var rL = card.querySelector('#r-leadscore'), rT1 = card.querySelector('#r-tier1');
        var rB = card.querySelector('#r-psmband'), rC = card.querySelector('#r-lpcost');
        var svg = card.querySelector('#plot-psafe-u8'), diag = card.querySelector('#diag-psafe-u8');

        function update() {
          var nmis = parseFloat(sN.value); vN.textContent = f(nmis, 0);
          var blog = parseFloat(sB.value); vB.textContent = f(blog, 0) + '%';
          var aclos = parseFloat(sA.value); vA.textContent = f(aclos, 0) + '%';
          var isMocFull = parseInt(sM.value, 10) === 2;
          vM.textContent = isMocFull ? 'Formal (100%)' : 'Partial / Informal (60%)';

          var reportingCredit = Math.min(100, (nmis / 150) * 100);
          var leadScore = 0.35 * reportingCredit + 0.35 * aclos + 0.30 * (100 - blog * 3) * (isMocFull ? 1.0 : 0.7);
          leadScore = Math.max(10, Math.min(99, leadScore));

          var tier1 = Math.max(0.01, 1.5 * Math.exp(-0.045 * leadScore));
          var band = leadScore > 85 ? 'Industry Leader (Top Decile)' : (leadScore > 65 ? 'Satisfactory PSM' : 'HIGH RISK (Regulatory Audit Warning)');

          rL.textContent = f(leadScore, 0) + ' %';
          rT1.textContent = f(tier1, 3) + ' /yr';
          rB.textContent = band;
          rB.style.color = leadScore > 85 ? '#15803d' : (leadScore > 65 ? '#d97706' : '#dc2626');
          rC.textContent = '$' + f(0.8 + 0.01 * nmis + (100 - blog) * 0.008, 1) + ' M/yr';

          // SVG Heinrich Safety Triangle
          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<polygon points="300,30 200,165 400,165" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>' +
                          '<polygon points="300,30 230,125 370,125" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>' +
                          '<polygon points="300,30 265,75 335,75" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>' +
                          '<text x="300" y="60" text-anchor="middle" font-size="10" font-weight="700" fill="#dc2626">Tier 1: ' + f(tier1,2) + '</text>' +
                          '<text x="300" y="105" text-anchor="middle" font-size="10" font-weight="700" fill="#92400e">Tier 2 Releases</text>' +
                          '<text x="300" y="150" text-anchor="middle" font-size="10" font-weight="700" fill="#1e293b">Near Misses: ' + f(nmis,0) + '</text>' +
                          '<text x="90" y="70" font-size="11" font-weight="700" fill="#1e40af">Audit Closure: ' + f(aclos,0) + '%</text>' +
                          '<text x="90" y="100" font-size="11" font-weight="700" fill="#b45309">Backlog: ' + f(blog,0) + '%</text>' +
                          '<text x="90" y="130" font-size="11" font-weight="700" fill="#15803d">Score: ' + f(leadScore,0) + '%</text>' +
                          '<text x="300" y="20" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">PSM Pyramid: Leading Culture Score = ' + f(leadScore, 0) + '% (' + band.split(' ')[0] + ')</text>';
          diag.textContent = 'Process Safety Management health: Active near-miss reporting (' + f(nmis, 0) + ' reports/yr) and rigorous audit closure (' + f(aclos, 0) + '%) drive leading indicator health to ' + f(leadScore, 0) + '%. Predicted Tier 1 process safety event frequency is suppressed to ' + f(tier1, 3) + ' incidents/yr.';
        }
        [sN, sB, sA, sM].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    }
  ];

  if (!window.SimulationEngine) window.SimulationEngine = {};
  window.SimulationEngine.initSimulation = function(containerId, simType) {
    var container = document.getElementById(containerId) ||
                    document.getElementById('sim-container') ||
                    document.querySelector('.simulation-slot');
    if (!container) return;
    container.innerHTML = '';
    var unitNum = 1;
    if (simType) {
      var m = simType.match(/(\d+)$/);
      if (m) unitNum = parseInt(m[1], 10);
    } else {
      var bMatch = document.body.dataset.chapterIndex;
      if (bMatch !== undefined && bMatch !== null && bMatch !== '') unitNum = parseInt(bMatch, 10) + 1;
      else {
        var pMatch = window.location.pathname.match(/chapter-(\d+)/);
        if (pMatch) unitNum = parseInt(pMatch[1], 10);
      }
    }
    if (isNaN(unitNum) || unitNum < 1 || unitNum > 8) unitNum = 1;
    var modelsForUnit = MODELS.filter(function(m) { return m.unit === unitNum; });
    if (modelsForUnit.length === 0) modelsForUnit = MODELS.filter(function(m) { return m.unit === 1; });
    modelsForUnit.forEach(function(m) {
      var card = document.createElement('section');
      card.className = 'cpe-sim-card';
      card.setAttribute('aria-label', 'Interactive Simulation ' + m.idx);
      card.id = 'sim-card-' + m.idx;
      card.innerHTML = m.html;
      container.appendChild(card);
      m.init(card);
    });
  };

  if (typeof document !== 'undefined') {
    var autoInit = function() {
      var slot = document.getElementById('sim-container') || document.querySelector('.simulation-slot');
      if (slot && slot.children.length === 0) {
        window.SimulationEngine.initSimulation(slot.id || 'sim-container');
      }
    };
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', autoInit);
    } else {
      autoInit();
    }
  }
})(typeof window === 'undefined' ? globalThis : window);
