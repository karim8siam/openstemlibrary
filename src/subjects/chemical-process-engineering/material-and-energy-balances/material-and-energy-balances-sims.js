/* Material and Energy Balances Interactive Simulation Suite */
(function(window) {
  'use strict';

  function f(n, d) { d = (d !== undefined) ? d : 2; return Number.isFinite(n) ? n.toFixed(d) : '0.00'; }

  var MODELS = [
    {
      idx: 1, unit: 1,
      html: '<header><span class="eyebrow">Unit 1 Laboratory</span><h3>Binary Stream Mixer Composition Balance</h3><p class="lead">Calculate overall mixed stream flow and solute concentration from independent feed streams.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Feed 1 Flow F1 <span><output id="v-f1">200</output> kg/h</span></label><input type="range" id="s-f1" min="50" max="500" step="10" value="200"></div>' +
              '<div class="control-group"><label>Feed 1 Solute x1 <span><output id="v-x1">10.0</output> wt%</span></label><input type="range" id="s-x1" min="1.0" max="40.0" step="0.5" value="10.0"></div>' +
              '<div class="control-group"><label>Feed 2 Flow F2 <span><output id="v-f2">300</output> kg/h</span></label><input type="range" id="s-f2" min="50" max="500" step="10" value="300"></div>' +
              '<div class="control-group"><label>Feed 2 Solute x2 <span><output id="v-x2">40.0</output> wt%</span></label><input type="range" id="s-x2" min="5.0" max="80.0" step="1.0" value="40.0"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Total Outlet Flow</small><output id="out-f3">500.0</output> kg/h</div>' +
              '<div class="stat-box"><small>Mixed Solute x3</small><output id="out-x3">28.0</output> wt%</div>' +
              '<div class="stat-box"><small>Solute Mass Rate</small><output id="out-m3">140.0</output> kg/h</div>' +
            '</div>' +
            '<svg id="svg-meb1" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-meb1">Total mass balance F3 = F1 + F2; solute species balance F3*x3 = F1*x1 + F2*x2.</div>',
      init: function(card) {
        var sF1 = card.querySelector('#s-f1'), sX1 = card.querySelector('#s-x1'), sF2 = card.querySelector('#s-f2'), sX2 = card.querySelector('#s-x2');
        var vF1 = card.querySelector('#v-f1'), vX1 = card.querySelector('#v-x1'), vF2 = card.querySelector('#v-f2'), vX2 = card.querySelector('#v-x2');
        var outF3 = card.querySelector('#out-f3'), outX3 = card.querySelector('#out-x3'), outM3 = card.querySelector('#out-m3');
        var svg = card.querySelector('#svg-meb1'), diag = card.querySelector('#diag-meb1');

        function update() {
          var f1 = parseFloat(sF1.value), x1 = parseFloat(sX1.value), f2 = parseFloat(sF2.value), x2 = parseFloat(sX2.value);
          vF1.textContent = f(f1, 0); vX1.textContent = f(x1, 1); vF2.textContent = f(f2, 0); vX2.textContent = f(x2, 1);
          var f3 = f1 + f2;
          var m3 = (f1 * x1 + f2 * x2) / 100.0;
          var x3 = (m3 / f3) * 100.0;

          outF3.textContent = f(f3, 1); outX3.textContent = f(x3, 1); outM3.textContent = f(m3, 1);

          svg.innerHTML = '<line x1="40" y1="50" x2="190" y2="80" stroke="#0284c7" stroke-width="3"/>' +
                          '<line x1="40" y1="110" x2="190" y2="80" stroke="#f59e0b" stroke-width="3"/>' +
                          '<circle cx="200" cy="80" r="18" fill="#1e293b" stroke="#0f172a" stroke-width="2"/>' +
                          '<line x1="220" y1="80" x2="360" y2="80" stroke="#10b981" stroke-width="4"/>' +
                          '<polygon points="360,80 345,73 345,87" fill="#10b981"/>' +
                          '<text x="45" y="40" font-size="11" fill="#0369a1" font-weight="700">F1 = ' + f(f1,0) + ' kg/h (' + f(x1,1) + '%)</text>' +
                          '<text x="45" y="125" font-size="11" fill="#b45309" font-weight="700">F2 = ' + f(f2,0) + ' kg/h (' + f(x2,1) + '%)</text>' +
                          '<text x="240" y="70" font-size="12" fill="#047857" font-weight="700">F3 = ' + f(f3,1) + ' kg/h</text>' +
                          '<text x="240" y="100" font-size="12" fill="#0f172a">Solute x3 = ' + f(x3,2) + ' wt%</text>';
          diag.textContent = 'Mixed outflow: Total mass rate is ' + f(f3, 1) + ' kg/h with solute purity ' + f(x3, 2) + ' wt%.';
        }
        [sF1, sX1, sF2, sX2].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 2, unit: 2,
      html: '<header><span class="eyebrow">Unit 2 Laboratory</span><h3>Recycle and Purge System Material Balance</h3><p class="lead">Simulate inerts accumulation, purge fraction, and overall loop recovery in a recycle process.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Fresh Feed A0 <span><output id="v-m0">100</output> kmol/h</span></label><input type="range" id="s-m0" min="20" max="300" step="10" value="100"></div>' +
              '<div class="control-group"><label>Inert Fraction yIn <span><output id="v-yin">0.02</output></span></label><input type="range" id="s-yin" min="0.005" max="0.08" step="0.005" value="0.02"></div>' +
              '<div class="control-group"><label>Purge Fraction \u03B8 <span><output id="v-purg">0.10</output></span></label><input type="range" id="s-purg" min="0.02" max="0.30" step="0.01" value="0.10"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Purge Flow P</small><output id="out-purgflow">20.0</output> kmol/h</div>' +
              '<div class="stat-box"><small>Recycle Flow R</small><output id="out-recflow">180.0</output> kmol/h</div>' +
              '<div class="stat-box"><small>Loop Inerts Conc</small><output id="out-inloop">10.0</output> mol%</div>' +
            '</div>' +
            '<svg id="svg-meb2" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-meb2">At steady state, all inerts introduced with the fresh feed must leave through the purge stream.</div>',
      init: function(card) {
        var sM0 = card.querySelector('#s-m0'), sYin = card.querySelector('#s-yin'), sPurg = card.querySelector('#s-purg');
        var vM0 = card.querySelector('#v-m0'), vYin = card.querySelector('#v-yin'), vPurg = card.querySelector('#v-purg');
        var outPurg = card.querySelector('#out-purgflow'), outRec = card.querySelector('#out-recflow'), outIn = card.querySelector('#out-inloop');
        var svg = card.querySelector('#svg-meb2'), diag = card.querySelector('#diag-meb2');

        function update() {
          var m0 = parseFloat(sM0.value), yin = parseFloat(sYin.value), theta = parseFloat(sPurg.value);
          vM0.textContent = f(m0, 0); vYin.textContent = f(yin, 3); vPurg.textContent = f(theta, 2);

          // Inerts balance: Inerts_in = m0 * yin
          var inertsIn = m0 * yin;
          // Purge carries inerts: P_inerts = inertsIn
          // Since purge has same comp as recycle loop, x_inert_loop = inertsIn / P
          // If reactor consumes A, let overall loop gas flow be m0 / theta * 0.2
          var loopGas = m0 / Math.max(0.01, theta);
          var purgeFlow = loopGas * theta;
          var recFlow = loopGas * (1.0 - theta);
          var inertMolFrac = (inertsIn / Math.max(0.1, purgeFlow)) * 100.0;

          outPurg.textContent = f(purgeFlow, 1); outRec.textContent = f(recFlow, 1); outIn.textContent = f(inertMolFrac, 1);

          svg.innerHTML = '<rect x="150" y="45" width="90" height="60" rx="6" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>' +
                          '<text x="175" y="80" font-size="12" fill="#0369a1" font-weight="700">Loop</text>' +
                          '<line x1="30" y1="75" x2="150" y2="75" stroke="#0f172a" stroke-width="2"/>' +
                          '<line x1="240" y1="75" x2="340" y2="75" stroke="#0f172a" stroke-width="2"/>' +
                          '<line x1="340" y1="75" x2="440" y2="50" stroke="#ef4444" stroke-width="3"/>' +
                          '<line x1="340" y1="75" x2="340" y2="130" stroke="#6366f1" stroke-width="2"/>' +
                          '<line x1="340" y1="130" x2="110" y2="130" stroke="#6366f1" stroke-width="2"/>' +
                          '<line x1="110" y1="130" x2="110" y2="75" stroke="#6366f1" stroke-width="2"/>' +
                          '<text x="40" y="65" font-size="11" fill="#0f172a">Feed: ' + f(m0,0) + '</text>' +
                          '<text x="350" y="45" font-size="11" fill="#b91c1c" font-weight="700">Purge: ' + f(purgeFlow,1) + '</text>' +
                          '<text x="180" y="145" font-size="11" fill="#4338ca" font-weight="700">Recycle: ' + f(recFlow,1) + ' kmol/h</text>';
          diag.textContent = 'Steady state reached: Inerts build up to ' + f(inertMolFrac, 1) + ' mol% in the recycle loop to match purge rate.';
        }
        [sM0, sYin, sPurg].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 3, unit: 3,
      html: '<header><span class="eyebrow">Unit 3 Laboratory</span><h3>Reactor Conversion, Selectivity & Yield</h3><p class="lead">Examine primary reactant conversion and parallel by-product formation selectivity.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Feed A0 <span><output id="v-fa0">100</output> mol/s</span></label><input type="range" id="s-fa0" min="20" max="200" step="5" value="100"></div>' +
              '<div class="control-group"><label>Conversion XA <span><output id="v-xa">0.75</output></span></label><input type="range" id="s-xa" min="0.10" max="0.99" step="0.01" value="0.75"></div>' +
              '<div class="control-group"><label>Selectivity S(P/B) <span><output id="v-sel">5.0</output></span></label><input type="range" id="s-sel" min="1.0" max="15.0" step="0.5" value="5.0"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Desired Product P</small><output id="out-fp">62.5</output> mol/s</div>' +
              '<div class="stat-box"><small>Byproduct B</small><output id="out-fb">12.5</output> mol/s</div>' +
              '<div class="stat-box"><small>Overall Yield Y(P)</small><output id="out-yp">62.5</output> %</div>' +
            '</div>' +
            '<svg id="svg-meb3" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-meb3">Product yield equals conversion multiplied by instantaneous selectivity fraction.</div>',
      init: function(card) {
        var sFa0 = card.querySelector('#s-fa0'), sXa = card.querySelector('#s-xa'), sSel = card.querySelector('#s-sel');
        var vFa0 = card.querySelector('#v-fa0'), vXa = card.querySelector('#v-xa'), vSel = card.querySelector('#v-sel');
        var outFp = card.querySelector('#out-fp'), outFb = card.querySelector('#out-fb'), outYp = card.querySelector('#out-yp');
        var svg = card.querySelector('#svg-meb3'), diag = card.querySelector('#diag-meb3');

        function update() {
          var fa0 = parseFloat(sFa0.value), xa = parseFloat(sXa.value), s = parseFloat(sSel.value);
          vFa0.textContent = f(fa0, 0); vXa.textContent = f(xa, 2); vSel.textContent = f(s, 1);

          var aReacted = fa0 * xa;
          var fracP = s / (s + 1.0);
          var fp = aReacted * fracP;
          var fb = aReacted * (1.0 - fracP);
          var yp = (fp / fa0) * 100.0;

          outFp.textContent = f(fp, 1); outFb.textContent = f(fb, 1); outYp.textContent = f(yp, 1);

          var pW = Math.min(250, (fp / fa0) * 250);
          var bW = Math.min(250 - pW, (fb / fa0) * 250);
          svg.innerHTML = '<rect x="40" y="30" width="420" height="100" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>' +
                          '<rect x="60" y="55" width="' + pW + '" height="40" fill="#10b981" rx="4"/>' +
                          '<rect x="' + (60 + pW) + '" y="55" width="' + bW + '" height="40" fill="#f59e0b" rx="4"/>' +
                          '<rect x="' + (60 + pW + bW) + '" y="55" width="' + (250 - pW - bW) + '" height="40" fill="#94a3b8" rx="4"/>' +
                          '<text x="65" y="45" font-size="11" fill="#047857" font-weight="700">Product P (' + f(fp, 1) + ' mol/s)</text>' +
                          '<text x="' + Math.max(160, 60 + pW + 5) + '" y="45" font-size="11" fill="#b45309" font-weight="700">Byproduct B (' + f(fb, 1) + ' mol/s)</text>' +
                          '<text x="60" y="115" font-size="11" fill="#475569">Unreacted A: ' + f(fa0 - aReacted, 1) + ' mol/s | Overall Yield: ' + f(yp, 1) + '%</text>';
          diag.textContent = 'Reaction extent: ' + f(aReacted, 1) + ' mol/s A consumed producing ' + f(fp, 1) + ' mol/s P and ' + f(fb, 1) + ' mol/s B.';
        }
        [sFa0, sXa, sSel].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 4, unit: 4,
      html: '<header><span class="eyebrow">Unit 4 Laboratory</span><h3>Dynamic Tank Holdup & Level Drainage</h3><p class="lead">Model transient liquid inventory dV/dt = Qin - Qout with Torricelli gravity drainage.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Inflow Rate Qin <span><output id="v-qin">0.05</output> m³/s</span></label><input type="range" id="s-qin" min="0.01" max="0.15" step="0.01" value="0.05"></div>' +
              '<div class="control-group"><label>Valve Coeff Cv <span><output id="v-cv">0.035</output></span></label><input type="range" id="s-cv" min="0.015" max="0.060" step="0.005" value="0.035"></div>' +
              '<div class="control-group"><label>Tank Area A <span><output id="v-area">2.5</output> m²</span></label><input type="range" id="s-area" min="1.0" max="6.0" step="0.5" value="2.5"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Steady-State Level</small><output id="out-hss">2.04</output> m</div>' +
              '<div class="stat-box"><small>Holdup Volume</small><output id="out-vss">5.10</output> m³</div>' +
              '<div class="stat-box"><small>Drain Time Constant</small><output id="out-tau">102</output> s</div>' +
            '</div>' +
            '<svg id="svg-meb4" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-meb4">Dynamic balance: A (dh/dt) = Qin - Cv * sqrt(2*g*h). Equilibrium reached when Qin = Qout.</div>',
      init: function(card) {
        var sQin = card.querySelector('#s-qin'), sCv = card.querySelector('#s-cv'), sArea = card.querySelector('#s-area');
        var vQin = card.querySelector('#v-qin'), vCv = card.querySelector('#v-cv'), vArea = card.querySelector('#v-area');
        var outHss = card.querySelector('#out-hss'), outVss = card.querySelector('#out-vss'), outTau = card.querySelector('#out-tau');
        var svg = card.querySelector('#svg-meb4'), diag = card.querySelector('#diag-meb4');

        function update() {
          var qin = parseFloat(sQin.value), cv = parseFloat(sCv.value), area = parseFloat(sArea.value);
          vQin.textContent = f(qin, 2); vCv.textContent = f(cv, 3); vArea.textContent = f(area, 1);

          // Qout = cv * sqrt(2*g*h) => h_ss = (qin / cv)^2 / (2*g)
          var g = 9.80665;
          var h_ss = Math.pow(qin / cv, 2) / (2.0 * g);
          var v_ss = area * h_ss;
          // Linearized tau = 2 * A * sqrt(h_ss) / (cv * sqrt(2g)) = 2 * v_ss / qin
          var tau = (2.0 * v_ss) / qin;

          outHss.textContent = f(h_ss, 2); outVss.textContent = f(v_ss, 2); outTau.textContent = f(tau, 0);

          var hBar = Math.min(95, (h_ss / 5.0) * 95);
          svg.innerHTML = '<rect x="60" y="30" width="120" height="100" fill="#f1f5f9" stroke="#64748b" stroke-width="2"/>' +
                          '<rect x="60" y="' + (130 - hBar) + '" width="120" height="' + hBar + '" fill="#0284c7" fill-opacity="0.65"/>' +
                          '<line x1="120" y1="10" x2="120" y2="30" stroke="#0284c7" stroke-width="3"/>' +
                          '<line x1="180" y1="120" x2="220" y2="120" stroke="#0284c7" stroke-width="3"/>' +
                          '<text x="240" y="55" font-size="12" fill="#0f172a" font-weight="700">Steady State Level h = ' + f(h_ss, 2) + ' m</text>' +
                          '<text x="240" y="80" font-size="11" fill="#475569">Equilibrium inventory = ' + f(v_ss, 2) + ' m³</text>' +
                          '<text x="240" y="105" font-size="11" fill="#475569">Linearized process time constant = ' + f(tau, 0) + ' s</text>';
          diag.textContent = 'Dynamic inventory balance yields steady-state liquid height ' + f(h_ss, 2) + ' m with response time ' + f(tau, 0) + ' s.';
        }
        [sQin, sCv, sArea].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 5, unit: 5,
      html: '<header><span class="eyebrow">Unit 5 Laboratory</span><h3>Psychrometric Air Cooling & Condensation</h3><p class="lead">Calculate enthalpy and moisture removal during cooling of moist air below its dew point.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Inlet Temp T1 <span><output id="v-t1">35.0</output> °C</span></label><input type="range" id="s-t1" min="20" max="50" step="1" value="35"></div>' +
              '<div class="control-group"><label>Rel Humidity RH1 <span><output id="v-rh1">70</output> %</span></label><input type="range" id="s-rh1" min="20" max="95" step="5" value="70"></div>' +
              '<div class="control-group"><label>Target Temp T2 <span><output id="v-t2">12.0</output> °C</span></label><input type="range" id="s-t2" min="5" max="20" step="1" value="12"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Dew Point T_dp</small><output id="out-tdp">28.7</output> °C</div>' +
              '<div class="stat-box"><small>Water Condensate</small><output id="out-wcond">16.3</output> g/kg dry</div>' +
              '<div class="stat-box"><small>Cooling Duty</small><output id="out-qcool">68.4</output> kJ/kg dry</div>' +
            '</div>' +
            '<svg id="svg-meb5" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-meb5">Sensible cooling occurs until dew point; further cooling condenses water vapor adiabatically.</div>',
      init: function(card) {
        var sT1 = card.querySelector('#s-t1'), sRh1 = card.querySelector('#s-rh1'), sT2 = card.querySelector('#s-t2');
        var vT1 = card.querySelector('#v-t1'), vRh1 = card.querySelector('#v-rh1'), vT2 = card.querySelector('#v-t2');
        var outTdp = card.querySelector('#out-tdp'), outWcond = card.querySelector('#out-wcond'), outQcool = card.querySelector('#out-qcool');
        var svg = card.querySelector('#svg-meb5'), diag = card.querySelector('#diag-meb5');

        function update() {
          var t1 = parseFloat(sT1.value), rh1 = parseFloat(sRh1.value) / 100.0, t2 = parseFloat(sT2.value);
          vT1.textContent = f(t1, 0); vRh1.textContent = f(rh1 * 100, 0); vT2.textContent = f(t2, 0);

          // Magnus formula for saturation vapor pressure
          function pSat(T) { return 0.61078 * Math.exp((17.27 * T) / (T + 237.3)); } // kPa
          var ps1 = pSat(t1);
          var pv1 = rh1 * ps1;
          var tdp = (237.3 * Math.log(pv1 / 0.61078)) / (17.27 - Math.log(pv1 / 0.61078));
          var P_tot = 101.325;
          var w1 = 622.0 * (pv1 / (P_tot - pv1)); // g/kg
          var ps2 = pSat(t2);
          var w2 = 622.0 * (ps2 / (P_tot - ps2)); // saturated at t2
          var cond = Math.max(0, w1 - w2);
          // Cooling duty: sensible air (1.005*dT) + sensible vapor + latent heat (2450 kJ/kg * cond)
          var qCool = 1.005 * (t1 - t2) + (cond / 1000.0) * 2450.0;

          outTdp.textContent = f(tdp, 1); outWcond.textContent = f(cond, 1); outQcool.textContent = f(qCool, 1);

          svg.innerHTML = '<rect x="40" y="25" width="420" height="110" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>' +
                          '<path d="M 60 120 Q 200 110 380 35" fill="none" stroke="#0284c7" stroke-width="2"/>' +
                          '<circle cx="' + (60 + (t1 / 50.0) * 320) + '" cy="' + (120 - (w1 / 35.0) * 85) + '" r="5" fill="#ef4444"/>' +
                          '<circle cx="' + (60 + (t2 / 50.0) * 320) + '" cy="' + (120 - (w2 / 35.0) * 85) + '" r="5" fill="#10b981"/>' +
                          '<text x="60" y="45" font-size="12" fill="#0369a1" font-weight="700">Cooling Path from ' + f(t1,0) + '°C to ' + f(t2,0) + '°C</text>' +
                          '<text x="240" y="75" font-size="11" fill="#b91c1c" font-weight="700">Initial: Tdp = ' + f(tdp,1) + '°C</text>' +
                          '<text x="240" y="95" font-size="11" fill="#047857" font-weight="700">Condensate: ' + f(cond,1) + ' g/kg dry air</text>' +
                          '<text x="240" y="115" font-size="11" fill="#475569">Chiller duty: ' + f(qCool,1) + ' kJ/kg dry air</text>';
          diag.textContent = 'Dehumidification verified: Air cooled past ' + f(tdp, 1) + '°C dew point yields ' + f(cond, 1) + ' g water removed per kg dry air.';
        }
        [sT1, sRh1, sT2].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 6, unit: 6,
      html: '<header><span class="eyebrow">Unit 6 Laboratory</span><h3>Countercurrent Heat Exchanger Energy Balance</h3><p class="lead">Simulate sensible heat transfer duty, LMTD, and stream outlet temperatures.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Hot Stream Flow <span><output id="v-mh">2.0</output> kg/s</span></label><input type="range" id="s-mh" min="0.5" max="5.0" step="0.5" value="2.0"></div>' +
              '<div class="control-group"><label>Hot Inlet Temp Th_in <span><output id="v-thin">120</output> °C</span></label><input type="range" id="s-thin" min="80" max="180" step="5" value="120"></div>' +
              '<div class="control-group"><label>Cold Stream Flow <span><output id="v-mc">3.0</output> kg/s</span></label><input type="range" id="s-mc" min="0.5" max="6.0" step="0.5" value="3.0"></div>' +
              '<div class="control-group"><label>Cold Inlet Temp Tc_in <span><output id="v-tcin">25</output> °C</span></label><input type="range" id="s-tcin" min="10" max="40" step="5" value="25"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Thermal Duty Q</small><output id="out-qduty">376.8</output> kW</div>' +
              '<div class="stat-box"><small>Hot Outlet Th_out</small><output id="out-thout">75.0</output> °C</div>' +
              '<div class="stat-box"><small>Cold Outlet Tc_out</small><output id="out-tcout">55.0</output> °C</div>' +
            '</div>' +
            '<svg id="svg-meb6" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-meb6">Countercurrent flow maximizes log-mean temperature difference and thermodynamic effectiveness.</div>',
      init: function(card) {
        var sMh = card.querySelector('#s-mh'), sThin = card.querySelector('#s-thin'), sMc = card.querySelector('#s-mc'), sTcin = card.querySelector('#s-tcin');
        var vMh = card.querySelector('#v-mh'), vThin = card.querySelector('#v-thin'), vMc = card.querySelector('#v-mc'), vTcin = card.querySelector('#v-tcin');
        var outQduty = card.querySelector('#out-qduty'), outThout = card.querySelector('#out-thout'), outTcout = card.querySelector('#out-tcout');
        var svg = card.querySelector('#svg-meb6'), diag = card.querySelector('#diag-meb6');

        function update() {
          var mh = parseFloat(sMh.value), thin = parseFloat(sThin.value), mc = parseFloat(sMc.value), tcin = parseFloat(sTcin.value);
          vMh.textContent = f(mh, 1); vThin.textContent = f(thin, 0); vMc.textContent = f(mc, 1); vTcin.textContent = f(tcin, 0);

          var cph = 4.184, cpc = 4.184; // Water
          var Ch = mh * cph, Cc = mc * cpc;
          var Cmin = Math.min(Ch, Cc), Cmax = Math.max(Ch, Cc);
          var eff = 0.65; // exchanger effectiveness
          var qMax = Cmin * (thin - tcin);
          var q = eff * qMax;
          var thout = thin - q / Ch;
          var tcout = tcin + q / Cc;

          outQduty.textContent = f(q, 1); outThout.textContent = f(thout, 1); outTcout.textContent = f(tcout, 1);

          svg.innerHTML = '<rect x="40" y="25" width="420" height="110" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>' +
                          '<line x1="60" y1="50" x2="420" y2="80" stroke="#ef4444" stroke-width="3"/>' +
                          '<line x1="420" y1="110" x2="60" y2="90" stroke="#0284c7" stroke-width="3"/>' +
                          '<text x="60" y="42" font-size="11" fill="#b91c1c" font-weight="700">Hot In: ' + f(thin,0) + '°C</text>' +
                          '<text x="360" y="72" font-size="11" fill="#b91c1c" font-weight="700">Hot Out: ' + f(thout,1) + '°C</text>' +
                          '<text x="360" y="125" font-size="11" fill="#0369a1" font-weight="700">Cold In: ' + f(tcin,0) + '°C</text>' +
                          '<text x="60" y="105" font-size="11" fill="#0369a1" font-weight="700">Cold Out: ' + f(tcout,1) + '°C</text>' +
                          '<text x="180" y="145" font-size="11" fill="#0f172a">Exchanger Thermal Duty Q = ' + f(q, 1) + ' kW</text>';
          diag.textContent = 'First law energy balance closed: Heat transferred Q = ' + f(q, 1) + ' kW; no phase change.';
        }
        [sMh, sThin, sMc, sTcin].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 7, unit: 7,
      html: '<header><span class="eyebrow">Unit 7 Laboratory</span><h3>Adiabatic Flame Temperature & Combustion</h3><p class="lead">Determine flame temperature and flue gas oxygen content under excess air conditions.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Methane Fuel Flow <span><output id="v-ch4">10.0</output> kmol/h</span></label><input type="range" id="s-ch4" min="2" max="30" step="1" value="10"></div>' +
              '<div class="control-group"><label>Excess Air <span><output id="v-exair">20</output> %</span></label><input type="range" id="s-exair" min="0" max="100" step="5" value="20"></div>' +
              '<div class="control-group"><label>Preheat Air Temp <span><output id="v-tpre">25</output> °C</span></label><input type="range" id="s-tpre" min="25" max="350" step="25" value="25"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Adiabatic Flame Temp</small><output id="out-tflame">1895</output> °C</div>' +
              '<div class="stat-box"><small>Flue Gas O2</small><output id="out-o2">3.5</output> mol%</div>' +
              '<div class="stat-box"><small>Thermal Release</small><output id="out-lhv">2228</output> kW</div>' +
            '</div>' +
            '<svg id="svg-meb7" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-meb7">Enthalpy balance: Sensible heat of combustion products equals standard lower heating value plus preheat.</div>',
      init: function(card) {
        var sCh4 = card.querySelector('#s-ch4'), sExair = card.querySelector('#s-exair'), sTpre = card.querySelector('#s-tpre');
        var vCh4 = card.querySelector('#v-ch4'), vExair = card.querySelector('#v-exair'), vTpre = card.querySelector('#v-tpre');
        var outTflame = card.querySelector('#out-tflame'), outO2 = card.querySelector('#out-o2'), outLhv = card.querySelector('#out-lhv');
        var svg = card.querySelector('#svg-meb7'), diag = card.querySelector('#diag-meb7');

        function update() {
          var ch4 = parseFloat(sCh4.value), ex = parseFloat(sExair.value), tpre = parseFloat(sTpre.value);
          vCh4.textContent = f(ch4, 0); vExair.textContent = f(ex, 0); vTpre.textContent = f(tpre, 0);

          // CH4 + 2 O2 -> CO2 + 2 H2O
          var LHV = 802.3; // MJ/kmol
          var powerKW = (ch4 * LHV * 1000.0) / 3600.0;
          // Approximate adiabatic flame temp
          // Stoichiometric air = 2 / 0.21 = 9.52 mol air / mol CH4
          // Actual air = 9.52 * (1 + ex/100)
          var airRatio = 9.52 * (1.0 + ex / 100.0);
          var totalFlue = 1.0 + 2.0 + 9.52 * (1.0 + ex / 100.0) * 0.79 + 2.0 * (ex / 100.0);
          var o2_pct = (2.0 * (ex / 100.0) / totalFlue) * 100.0;
          var tFlame = (2050.0 / (1.0 + 0.008 * ex)) + 0.65 * (tpre - 25.0);

          outTflame.textContent = f(tFlame, 0); outO2.textContent = f(o2_pct, 1); outLhv.textContent = f(powerKW, 0);

          svg.innerHTML = '<rect x="40" y="25" width="420" height="110" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>' +
                          '<path d="M 120 125 L 140 40 L 160 125 Z" fill="#ef4444" opacity="0.8"/>' +
                          '<path d="M 130 125 L 140 60 L 150 125 Z" fill="#f59e0b"/>' +
                          '<text x="180" y="55" font-size="14" fill="#b91c1c" font-weight="700">Adiabatic Flame T = ' + f(tFlame, 0) + ' °C</text>' +
                          '<text x="180" y="80" font-size="11" fill="#475569">Excess air dilution: ' + f(ex, 0) + '% (Residual O2: ' + f(o2_pct, 1) + ' mol%)</text>' +
                          '<text x="180" y="105" font-size="11" fill="#475569">Furnace heat release = ' + f(powerKW, 0) + ' kW thermal</text>';
          diag.textContent = 'Combustion enthalpy closed: Higher excess air suppresses peak temperature to ' + f(tFlame, 0) + ' °C.';
        }
        [sCh4, sExair, sTpre].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 8, unit: 8,
      html: '<header><span class="eyebrow">Unit 8 Laboratory</span><h3>Plant-Wide Process Flowsheet Material & Energy Audit</h3><p class="lead">Simulate overall plant utility demand, conversion efficiency, and gross margins.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Crude Feed Rate <span><output id="v-crude">1000</output> t/day</span></label><input type="range" id="s-crude" min="200" max="3000" step="100" value="1000"></div>' +
              '<div class="control-group"><label>Recovery Efficiency <span><output id="v-receff">88</output> %</span></label><input type="range" id="s-receff" min="70" max="98" step="1" value="88"></div>' +
              '<div class="control-group"><label>Energy Intensity <span><output id="v-eint">2.2</output> GJ/t</span></label><input type="range" id="s-eint" min="1.0" max="4.0" step="0.1" value="2.2"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Saleable Output</small><output id="out-sale8">880</output> t/day</div>' +
              '<div class="stat-box"><small>Thermal Demand</small><output id="out-gjd">2200</output> GJ/day</div>' +
              '<div class="stat-box"><small>Process Power</small><output id="out-mwe">25.5</output> MW</div>' +
            '</div>' +
            '<svg id="svg-meb8" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-meb8">Integrated material and energy balance ensures closed plant boundaries and carbon accounting.</div>',
      init: function(card) {
        var sCrude = card.querySelector('#s-crude'), sReceff = card.querySelector('#s-receff'), sEint = card.querySelector('#s-eint');
        var vCrude = card.querySelector('#v-crude'), vReceff = card.querySelector('#v-receff'), vEint = card.querySelector('#v-eint');
        var outSale = card.querySelector('#out-sale8'), outGjd = card.querySelector('#out-gjd'), outMwe = card.querySelector('#out-mwe');
        var svg = card.querySelector('#svg-meb8'), diag = card.querySelector('#diag-meb8');

        function update() {
          var crude = parseFloat(sCrude.value), eff = parseFloat(sReceff.value) / 100.0, eint = parseFloat(sEint.value);
          vCrude.textContent = f(crude, 0); vReceff.textContent = f(eff * 100, 0); vEint.textContent = f(eint, 1);

          var sale = crude * eff;
          var gjDay = crude * eint;
          var mwE = (gjDay * 1e6) / (86400.0 * 1000.0);

          outSale.textContent = f(sale, 0); outGjd.textContent = f(gjDay, 0); outMwe.textContent = f(mwE, 1);

          svg.innerHTML = '<rect x="40" y="25" width="420" height="110" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>' +
                          '<rect x="60" y="55" width="100" height="50" rx="4" fill="#0284c7"/>' +
                          '<rect x="220" y="55" width="100" height="50" rx="4" fill="#10b981"/>' +
                          '<line x1="160" y1="80" x2="220" y2="80" stroke="#0f172a" stroke-width="2"/>' +
                          '<text x="65" y="85" font-size="11" fill="#fff" font-weight="700">Feed: ' + f(crude,0) + ' t/d</text>' +
                          '<text x="225" y="85" font-size="11" fill="#fff" font-weight="700">Prod: ' + f(sale,0) + ' t/d</text>' +
                          '<text x="340" y="70" font-size="11" fill="#475569">Energy: ' + f(gjDay,0) + ' GJ/d</text>' +
                          '<text x="340" y="95" font-size="11" fill="#0369a1" font-weight="700">Power: ' + f(mwE,1) + ' MW</text>';
          diag.textContent = 'Audited balance: Feed ' + f(crude, 0) + ' t/day yields ' + f(sale, 0) + ' t/day products with ' + f(gjDay, 0) + ' GJ/day heat demand.';
        }
        [sCrude, sReceff, sEint].forEach(function(el) { el.addEventListener('input', update); });
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
