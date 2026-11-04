/* Fluid Flow in Processes Interactive Simulation Suite */
(function(window) {
  'use strict';

  function f(n, d) { d = (d !== undefined) ? d : 2; return Number.isFinite(n) ? n.toFixed(d) : '0.00'; }

  var MODELS = [
    {
      idx: 1, unit: 1,
      html: '<header><span class="eyebrow">Unit 1 Laboratory</span><h3>Non-Newtonian Power-Law Apparent Viscosity</h3><p class="lead">Simulate pseudoplastic (shear-thinning) and dilatant fluid viscosity curves.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Shear Rate \u03B3_dot <span><output id="v-gdot">100</output> s⁻¹</span></label><input type="range" id="s-gdot" min="5" max="500" step="5" value="100"></div>' +
              '<div class="control-group"><label>Consistency Index K <span><output id="v-k1">2.0</output> Pa·s^n</span></label><input type="range" id="s-k1" min="0.2" max="10.0" step="0.2" value="2.0"></div>' +
              '<div class="control-group"><label>Flow Index n <span><output id="v-n1">0.60</output></span></label><input type="range" id="s-n1" min="0.20" max="1.50" step="0.05" value="0.60"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Apparent Viscosity</small><output id="out-eta1">0.317</output> Pa·s</div>' +
              '<div class="stat-box"><small>Shear Stress \u03C4</small><output id="out-tau1">31.7</output> Pa</div>' +
              '<div class="stat-box"><small>Rheology Class</small><output id="out-rheoclass">Shear-Thinning</output></div>' +
            '</div>' +
            '<svg id="svg-ffp1" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-ffp1">Ostwald-de Waele power law: \u03C4 = K * (\u03B3_dot)^n; apparent viscosity \u03B7 = K * (\u03B3_dot)^(n-1).</div>',
      init: function(card) {
        var sGdot = card.querySelector('#s-gdot'), sK = card.querySelector('#s-k1'), sN = card.querySelector('#s-n1');
        var vGdot = card.querySelector('#v-gdot'), vK = card.querySelector('#v-k1'), vN = card.querySelector('#v-n1');
        var outEta = card.querySelector('#out-eta1'), outTau = card.querySelector('#out-tau1'), outClass = card.querySelector('#out-rheoclass');
        var svg = card.querySelector('#svg-ffp1'), diag = card.querySelector('#diag-ffp1');

        function update() {
          var gdot = parseFloat(sGdot.value), K = parseFloat(sK.value), n = parseFloat(sN.value);
          vGdot.textContent = f(gdot, 0); vK.textContent = f(K, 1); vN.textContent = f(n, 2);

          var eta = K * Math.pow(gdot, n - 1.0);
          var tau = K * Math.pow(gdot, n);
          var rClass = n < 0.95 ? 'Shear-Thinning (Pseudoplastic)' : (n > 1.05 ? 'Shear-Thickening (Dilatant)' : 'Newtonian');

          outEta.textContent = f(eta, 3); outTau.textContent = f(tau, 1); outClass.textContent = rClass;

          var pts = '';
          for (var g = 10; g <= 500; g += 15) {
            var eta_g = K * Math.pow(g, n - 1.0);
            var xP = 50 + (g / 500.0) * 380;
            var yP = 135 - Math.min(105, (eta_g / 3.0) * 105);
            pts += (pts ? ' ' : '') + xP.toFixed(1) + ',' + yP.toFixed(1);
          }

          svg.innerHTML = '<rect x="35" y="15" width="430" height="130" fill="#f8fafc" stroke="#cbd5e1"/>' +
                          '<polyline points="' + pts + '" fill="none" stroke="#0284c7" stroke-width="2.5"/>' +
                          '<circle cx="' + (50 + (gdot / 500.0) * 380) + '" cy="' + (135 - Math.min(105, (eta / 3.0) * 105)) + '" r="5" fill="#ef4444"/>' +
                          '<text x="60" y="35" font-size="11" fill="#0369a1" font-weight="700">Apparent Viscosity \u03B7 vs Shear Rate (n = ' + f(n,2) + ')</text>' +
                          '<text x="240" y="148" font-size="10" fill="#64748b">Shear Rate \u03B3_dot (s⁻¹)</text>' +
                          '<text x="290" y="65" font-size="11" fill="#b91c1c" font-weight="700">\u03B7 = ' + f(eta, 3) + ' Pa·s</text>';
          diag.textContent = 'Rheological analysis: ' + rClass + ' behavior with consistency index K = ' + f(K, 1) + ' Pa·s^n.';
        }
        [sGdot, sK, sN].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 2, unit: 2,
      html: '<header><span class="eyebrow">Unit 2 Laboratory</span><h3>U-Tube Differential Manometer</h3><p class="lead">Simulate differential pressure measurement across a process line using fluid manometry.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Manometer Deflection h <span><output id="v-mh2">200</output> mm</span></label><input type="range" id="s-mh2" min="20" max="600" step="10" value="200"></div>' +
              '<div class="control-group"><label>Manometer Fluid SG <span><output id="v-sgm">13.6</output></span></label><input type="range" id="s-sgm" min="1.2" max="13.6" step="0.2" value="13.6"></div>' +
              '<div class="control-group"><label>Process Fluid SG <span><output id="v-sgp">1.0</output></span></label><input type="range" id="s-sgp" min="0.7" max="1.4" step="0.05" value="1.0"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Differential \u0394P</small><output id="out-dpman">24.7</output> kPa</div>' +
              '<div class="stat-box"><small>Water Head</small><output id="out-wh">2.52</output> m H2O</div>' +
              '<div class="stat-box"><small>Bar</small><output id="out-barman">0.247</output> bar</div>' +
            '</div>' +
            '<svg id="svg-ffp2" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-ffp2">Manometer equation: \u0394P = (\u03C1_m - \u03C1_p) * g * h.</div>',
      init: function(card) {
        var sMh = card.querySelector('#s-mh2'), sSgm = card.querySelector('#s-sgm'), sSgp = card.querySelector('#s-sgp');
        var vMh = card.querySelector('#v-mh2'), vSgm = card.querySelector('#v-sgm'), vSgp = card.querySelector('#v-sgp');
        var outDp = card.querySelector('#out-dpman'), outWh = card.querySelector('#out-wh'), outBar = card.querySelector('#out-barman');
        var svg = card.querySelector('#svg-ffp2'), diag = card.querySelector('#diag-ffp2');

        function update() {
          var h = parseFloat(sMh.value) / 1000.0, sgM = parseFloat(sSgm.value), sgP = parseFloat(sSgp.value);
          vMh.textContent = f(h * 1000.0, 0); vSgm.textContent = f(sgM, 1); vSgp.textContent = f(sgP, 2);

          var rhoM = sgM * 1000.0, rhoP = sgP * 1000.0;
          var g = 9.80665;
          var dP_kPa = ((rhoM - rhoP) * g * h) / 1000.0;
          var mH2O = dP_kPa / 9.80665;
          var bar = dP_kPa / 100.0;

          outDp.textContent = f(dP_kPa, 2); outWh.textContent = f(mH2O, 2); outBar.textContent = f(bar, 3);

          var defH = Math.min(60, (h / 0.6) * 60);
          svg.innerHTML = '<rect x="40" y="20" width="420" height="120" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>' +
                          '<path d="M 120 30 L 120 110 Q 150 130 180 110 L 180 30" fill="none" stroke="#64748b" stroke-width="8"/>' +
                          '<path d="M 120 ' + (110 - defH) + ' L 120 110 Q 150 130 180 110 L 180 ' + (110 + defH) + '" fill="none" stroke="#ef4444" stroke-width="8"/>' +
                          '<text x="240" y="55" font-size="14" fill="#0284c7" font-weight="700">\u0394P = ' + f(dP_kPa, 2) + ' kPa</text>' +
                          '<text x="240" y="80" font-size="11" fill="#475569">Deflection h = ' + f(h*1000, 0) + ' mm (SG = ' + f(sgM,1) + ')</text>' +
                          '<text x="240" y="105" font-size="11" fill="#475569">Equivalent head = ' + f(mH2O, 2) + ' m H2O</text>';
          diag.textContent = 'Hydrostatic manometer balance: Deflection ' + f(h * 1000, 0) + ' mm registers line pressure drop of ' + f(dP_kPa, 2) + ' kPa.';
        }
        [sMh, sSgm, sSgp].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 3, unit: 3,
      html: '<header><span class="eyebrow">Unit 3 Laboratory</span><h3>Venturi Meter Flow Measurement & Bernoulli Equation</h3><p class="lead">Simulate flow discharge, throat velocity, and head recovery in a standard Venturi meter.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Inlet Pipe D1 <span><output id="v-d1">100</output> mm</span></label><input type="range" id="s-d1" min="50" max="250" step="10" value="100"></div>' +
              '<div class="control-group"><label>Throat Dia D2 <span><output id="v-d2">50</output> mm</span></label><input type="range" id="s-d2" min="20" max="120" step="5" value="50"></div>' +
              '<div class="control-group"><label>Differential Head \u0394h <span><output id="v-dhv">0.80</output> m</span></label><input type="range" id="s-dhv" min="0.10" max="3.00" step="0.10" value="0.80"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Volumetric Flow Q</small><output id="out-qv">7.72</output> L/s</div>' +
              '<div class="stat-box"><small>Throat Velocity v2</small><output id="out-v2">3.93</output> m/s</div>' +
              '<div class="stat-box"><small>Diameter Ratio \u03B2</small><output id="out-beta">0.50</output></div>' +
            '</div>' +
            '<svg id="svg-ffp3" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-ffp3">Bernoulli discharge equation: Q = Cd * A2 * sqrt(2*g*\u0394h / (1 - \u03B2⁴)).</div>',
      init: function(card) {
        var sD1 = card.querySelector('#s-d1'), sD2 = card.querySelector('#s-d2'), sDh = card.querySelector('#s-dhv');
        var vD1 = card.querySelector('#v-d1'), vD2 = card.querySelector('#v-d2'), vDh = card.querySelector('#v-dhv');
        var outQv = card.querySelector('#out-qv'), outV2 = card.querySelector('#out-v2'), outBeta = card.querySelector('#out-beta');
        var svg = card.querySelector('#svg-ffp3'), diag = card.querySelector('#diag-ffp3');

        function update() {
          var d1 = parseFloat(sD1.value) / 1000.0, d2 = Math.min(d1 * 0.85, parseFloat(sD2.value) / 1000.0), dh = parseFloat(sDh.value);
          vD1.textContent = f(d1 * 1000.0, 0); vD2.textContent = f(d2 * 1000.0, 0); vDh.textContent = f(dh, 2);

          var beta = d2 / d1;
          var a2 = (Math.PI / 4.0) * Math.pow(d2, 2);
          var Cd = 0.98; // Venturi coefficient
          var g = 9.80665;
          var Q_m3s = Cd * a2 * Math.sqrt((2.0 * g * dh) / (1.0 - Math.pow(beta, 4)));
          var v2 = Q_m3s / a2;
          var Q_Lps = Q_m3s * 1000.0;

          outQv.textContent = f(Q_Lps, 2); outV2.textContent = f(v2, 2); outBeta.textContent = f(beta, 2);

          svg.innerHTML = '<rect x="40" y="20" width="420" height="120" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>' +
                          '<polygon points="60,40 180,40 220,65 260,65 340,40 400,40 400,120 340,120 260,95 220,95 180,120 60,120" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>' +
                          '<text x="70" y="85" font-size="11" fill="#0369a1">D1 = ' + f(d1*1000, 0) + ' mm</text>' +
                          '<text x="215" y="85" font-size="11" fill="#b91c1c" font-weight="700">D2</text>' +
                          '<text x="290" y="50" font-size="13" fill="#0284c7" font-weight="700">Q = ' + f(Q_Lps, 2) + ' L/s</text>' +
                          '<text x="290" y="75" font-size="11" fill="#475569">Throat velocity = ' + f(v2, 2) + ' m/s</text>' +
                          '<text x="290" y="100" font-size="11" fill="#475569">Diameter ratio \u03B2 = ' + f(beta, 2) + '</text>';
          diag.textContent = 'Venturi discharge calculation: Fluid velocity through throat reaches ' + f(v2, 2) + ' m/s (Q = ' + f(Q_Lps, 2) + ' L/s).';
        }
        [sD1, sD2, sDh].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 4, unit: 4,
      html: '<header><span class="eyebrow">Unit 4 Laboratory</span><h3>Frictional Pipe Loss & Moody Chart Friction Factor</h3><p class="lead">Simulate Darcy-Weisbach friction factor f, Colebrook-White equation, and pressure drop.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Reynolds Number Re <span><output id="v-re4">40000</output></span></label><input type="range" id="s-re4" min="1500" max="500000" step="5000" value="40000"></div>' +
              '<div class="control-group"><label>Relative Roughness \u03B5/D <span><output id="v-ed4">0.0010</output></span></label><input type="range" id="s-ed4" min="0.00005" max="0.010" step="0.0005" value="0.0010"></div>' +
              '<div class="control-group"><label>Pipe Length L <span><output id="v-len4">50</output> m</span></label><input type="range" id="s-len4" min="10" max="200" step="10" value="50"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Darcy Friction f</small><output id="out-f4">0.0248</output></div>' +
              '<div class="stat-box"><small>Head Loss hf</small><output id="out-hf4">3.16</output> m</div>' +
              '<div class="stat-box"><small>Pressure Drop \u0394P</small><output id="out-dp4">31.0</output> kPa</div>' +
            '</div>' +
            '<svg id="svg-ffp4" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-ffp4">Swamee-Jain explicit formula: f = 0.25 / [log10(\u03B5/3.7D + 5.74/Re^0.9)]².</div>',
      init: function(card) {
        var sRe = card.querySelector('#s-re4'), sEd = card.querySelector('#s-ed4'), sLen = card.querySelector('#s-len4');
        var vRe = card.querySelector('#v-re4'), vEd = card.querySelector('#v-ed4'), vLen = card.querySelector('#v-len4');
        var outF = card.querySelector('#out-f4'), outHf = card.querySelector('#out-hf4'), outDp = card.querySelector('#out-dp4');
        var svg = card.querySelector('#svg-ffp4'), diag = card.querySelector('#diag-ffp4');

        function update() {
          var Re = parseFloat(sRe.value), ed = parseFloat(sEd.value), L = parseFloat(sLen.value);
          vRe.textContent = f(Re, 0); vEd.textContent = f(ed, 4); vLen.textContent = f(L, 0);

          var fVal;
          if (Re < 2300) {
            fVal = 64.0 / Re;
          } else {
            fVal = 0.25 / Math.pow(Math.log10(ed / 3.7 + 5.74 / Math.pow(Re, 0.9)), 2);
          }
          var D = 0.10; // 100 mm pipe
          var V = 2.0; // 2 m/s
          var g = 9.80665;
          var hf = fVal * (L / D) * (Math.pow(V, 2) / (2.0 * g));
          var dP_kPa = (1000.0 * g * hf) / 1000.0;

          outF.textContent = f(fVal, 4); outHf.textContent = f(hf, 2); outDp.textContent = f(dP_kPa, 1);

          svg.innerHTML = '<rect x="40" y="20" width="420" height="120" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>' +
                          '<rect x="60" y="55" width="380" height="30" fill="#e2e8f0" rx="4"/>' +
                          '<rect x="60" y="55" width="' + Math.min(380, (fVal / 0.05) * 380) + '" height="30" fill="#0284c7" rx="4"/>' +
                          '<text x="60" y="45" font-size="12" fill="#0369a1" font-weight="700">Darcy Friction Factor f = ' + f(fVal, 4) + '</text>' +
                          '<text x="60" y="115" font-size="11" fill="#475569">Head loss hf = ' + f(hf, 2) + ' m | Pipe \u0394P = ' + f(dP_kPa, 1) + ' kPa across ' + f(L,0) + ' m</text>' +
                          '<text x="320" y="45" font-size="11" fill="#0f172a">Re = ' + f(Re, 0) + '</text>';
          diag.textContent = 'Pipe hydraulics verified: Darcy friction factor f = ' + f(fVal, 4) + ' creates ' + f(dP_kPa, 1) + ' kPa loss.';
        }
        [sRe, sEd, sLen].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 5, unit: 5,
      html: '<header><span class="eyebrow">Unit 5 Laboratory</span><h3>Centrifugal Pump Head Curve & System Operating Point</h3><p class="lead">Simulate pump H-Q curve, system head curve, and operating flow intersection.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Shutoff Head H0 <span><output id="v-h0">45.0</output> m</span></label><input type="range" id="s-h0" min="20" max="80" step="5" value="45"></div>' +
              '<div class="control-group"><label>Static Lift \u0394z <span><output id="v-dz">15.0</output> m</span></label><input type="range" id="s-dz" min="5" max="30" step="1" value="15"></div>' +
              '<div class="control-group"><label>System Resistance K <span><output id="v-ksys">0.008</output></span></label><input type="range" id="s-ksys" min="0.003" max="0.025" step="0.001" value="0.008"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Operating Flow Q_op</small><output id="out-qop">51.2</output> m³/h</div>' +
              '<div class="stat-box"><small>Operating Head H_op</small><output id="out-hop">36.0</output> m</div>' +
              '<div class="stat-box"><small>Hydraulic Power</small><output id="out-pw">5.02</output> kW</div>' +
            '</div>' +
            '<svg id="svg-ffp5" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-ffp5">Pump curve H = H0 - a*Q² intersects system resistance H = \u0394z + K*Q² at operating point.</div>',
      init: function(card) {
        var sH0 = card.querySelector('#s-h0'), sDz = card.querySelector('#s-dz'), sKsys = card.querySelector('#s-ksys');
        var vH0 = card.querySelector('#v-h0'), vDz = card.querySelector('#v-dz'), vKsys = card.querySelector('#v-ksys');
        var outQop = card.querySelector('#out-qop'), outHop = card.querySelector('#out-hop'), outPw = card.querySelector('#out-pw');
        var svg = card.querySelector('#svg-ffp5'), diag = card.querySelector('#diag-ffp5');

        function update() {
          var H0 = parseFloat(sH0.value), dz = parseFloat(sDz.value), Ksys = parseFloat(sKsys.value);
          vH0.textContent = f(H0, 0); vDz.textContent = f(dz, 0); vKsys.textContent = f(Ksys, 3);

          var aPump = 0.0035;
          // Intersection: H0 - a*Q^2 = dz + Ksys*Q^2 => Q = sqrt((H0 - dz)/(a + Ksys))
          var qOp = 0, hOp = H0;
          if (H0 > dz) {
            qOp = Math.sqrt((H0 - dz) / (aPump + Ksys));
            hOp = dz + Ksys * Math.pow(qOp, 2);
          }
          var powerKW = (1000.0 * 9.80665 * (qOp / 3600.0) * hOp) / 1000.0;

          outQop.textContent = f(qOp, 1); outHop.textContent = f(hOp, 1); outPw.textContent = f(powerKW, 2);

          var ptsPump = '', ptsSys = '';
          for (var q = 0; q <= 100; q += 5) {
            var hP = Math.max(0, H0 - aPump * Math.pow(q, 2));
            var hS = dz + Ksys * Math.pow(q, 2);
            var xP = 60 + (q / 100.0) * 360;
            var yPump = 135 - (hP / 90.0) * 110;
            var ySys = 135 - (hS / 90.0) * 110;
            ptsPump += (ptsPump ? ' ' : '') + xP.toFixed(1) + ',' + yPump.toFixed(1);
            ptsSys += (ptsSys ? ' ' : '') + xP.toFixed(1) + ',' + ySys.toFixed(1);
          }
          var curX = 60 + (qOp / 100.0) * 360;
          var curY = 135 - (hOp / 90.0) * 110;

          svg.innerHTML = '<rect x="40" y="20" width="420" height="125" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>' +
                          '<polyline points="' + ptsPump + '" fill="none" stroke="#0284c7" stroke-width="2.5"/>' +
                          '<polyline points="' + ptsSys + '" fill="none" stroke="#ef4444" stroke-width="2.5"/>' +
                          '<circle cx="' + curX + '" cy="' + curY + '" r="5" fill="#10b981"/>' +
                          '<text x="60" y="38" font-size="11" fill="#0369a1" font-weight="700">Pump H-Q Curve</text>' +
                          '<text x="220" y="38" font-size="11" fill="#b91c1c" font-weight="700">System Head Curve</text>' +
                          '<text x="' + Math.min(300, curX + 10) + '" y="' + curY + '" font-size="11" fill="#047857" font-weight="700">Q_op = ' + f(qOp,1) + ' m³/h</text>' +
                          '<text x="210" y="142" font-size="10" fill="#64748b">Flow Rate Q (m³/h)</text>';
          diag.textContent = 'Hydraulic operating match: Pump delivers ' + f(qOp, 1) + ' m³/h against ' + f(hOp, 1) + ' m head (Power = ' + f(powerKW, 2) + ' kW).';
        }
        [sH0, sDz, sKsys].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 6, unit: 6,
      html: '<header><span class="eyebrow">Unit 6 Laboratory</span><h3>Two-Phase Flow Lockhart-Martinelli Multiplier</h3><p class="lead">Simulate gas-liquid co-current flow pressure drop multiplier Phi_L².</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Martinelli Param X <span><output id="v-x6">2.50</output></span></label><input type="range" id="s-x6" min="0.10" max="10.00" step="0.10" value="2.50"></div>' +
              '<div class="control-group"><label>Liquid Alone \u0394P_L <span><output id="v-dpl6">10.0</output> kPa</span></label><input type="range" id="s-dpl6" min="2.0" max="40.0" step="1.0" value="10.0"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Multiplier \u03A6_L²</small><output id="out-phi6">5.16</output></div>' +
              '<div class="stat-box"><small>Two-Phase \u0394P_TP</small><output id="out-dptp">51.6</output> kPa</div>' +
              '<div class="stat-box"><small>Flow Regime</small><output id="out-tpreg">Slug / Wavy</output></div>' +
            '</div>' +
            '<svg id="svg-ffp6" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-ffp6">Chisholm correlation: \u03A6_L² = 1 + C/X + 1/X² with C = 20 for turbulent-turbulent flow.</div>',
      init: function(card) {
        var sX = card.querySelector('#s-x6'), sDpl = card.querySelector('#s-dpl6');
        var vX = card.querySelector('#v-x6'), vDpl = card.querySelector('#v-dpl6');
        var outPhi = card.querySelector('#out-phi6'), outDptp = card.querySelector('#out-dptp'), outReg = card.querySelector('#out-tpreg');
        var svg = card.querySelector('#svg-ffp6'), diag = card.querySelector('#diag-ffp6');

        function update() {
          var X = parseFloat(sX.value), dpL = parseFloat(sDpl.value);
          vX.textContent = f(X, 2); vDpl.textContent = f(dpL, 1);

          var C = 20.0; // turbulent-turbulent
          var phiSq = 1.0 + C / X + 1.0 / Math.pow(X, 2);
          var dpTP = dpL * phiSq;
          var regime = X > 5 ? 'Liquid Dominated' : (X < 0.5 ? 'Mist / Annular' : 'Slug / Wavy');

          outPhi.textContent = f(phiSq, 2); outDptp.textContent = f(dpTP, 1); outReg.textContent = regime;

          svg.innerHTML = '<rect x="40" y="20" width="420" height="120" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>' +
                          '<rect x="60" y="55" width="' + Math.min(380, (phiSq / 25.0) * 380) + '" height="35" rx="4" fill="#0284c7"/>' +
                          '<text x="60" y="45" font-size="12" fill="#0369a1" font-weight="700">Two-Phase Pressure Drop \u0394P_TP = ' + f(dpTP, 1) + ' kPa</text>' +
                          '<text x="60" y="115" font-size="11" fill="#475569">Multiplier \u03A6_L² = ' + f(phiSq, 2) + ' | Regime: ' + regime + '</text>';
          diag.textContent = 'Lockhart-Martinelli two-phase multiplier \u03A6_L² = ' + f(phiSq, 2) + ' amplifies single-phase friction.';
        }
        [sX, sDpl].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 7, unit: 7,
      html: '<header><span class="eyebrow">Unit 7 Laboratory</span><h3>Orifice Plate Meter Discharge Calibration</h3><p class="lead">Simulate flow measurement, orifice beta ratio, and non-recoverable head loss.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Orifice Bore d <span><output id="v-d7">40</output> mm</span></label><input type="range" id="s-d7" min="15" max="75" step="5" value="40"></div>' +
              '<div class="control-group"><label>Differential \u0394P <span><output id="v-dp7">25.0</output> kPa</span></label><input type="range" id="s-dp7" min="5" max="80" step="5" value="25"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Measured Flow Q</small><output id="out-qorf">5.23</output> L/s</div>' +
              '<div class="stat-box"><small>Permanent Loss</small><output id="out-permloss">18.5</output> kPa</div>' +
              '<div class="stat-box"><small>Orifice Beta \u03B2</small><output id="out-beta7">0.40</output></div>' +
            '</div>' +
            '<svg id="svg-ffp7" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-ffp7">Standard concentric orifice: Q = C0 * A0 / sqrt(1 - \u03B2⁴) * sqrt(2*\u0394P/\u03C1).</div>',
      init: function(card) {
        var sD = card.querySelector('#s-d7'), sDp = card.querySelector('#s-dp7');
        var vD = card.querySelector('#v-d7'), vDp = card.querySelector('#v-dp7');
        var outQ = card.querySelector('#out-qorf'), outPerm = card.querySelector('#out-permloss'), outBeta = card.querySelector('#out-beta7');
        var svg = card.querySelector('#svg-ffp7'), diag = card.querySelector('#diag-ffp7');

        function update() {
          var d = parseFloat(sD.value) / 1000.0, dpKpa = parseFloat(sDp.value);
          vD.textContent = f(d * 1000.0, 0); vDp.textContent = f(dpKpa, 1);

          var D_pipe = 0.10; // 100 mm
          var beta = d / D_pipe;
          var a0 = (Math.PI / 4.0) * Math.pow(d, 2);
          var C0 = 0.61; // standard orifice discharge coeff
          var rho = 1000.0;
          var dpPa = dpKpa * 1000.0;
          var Q_m3s = (C0 * a0 / Math.sqrt(1.0 - Math.pow(beta, 4))) * Math.sqrt((2.0 * dpPa) / rho);
          var permLoss = dpKpa * (1.0 - Math.pow(beta, 2));

          outQ.textContent = f(Q_m3s * 1000.0, 2); outPerm.textContent = f(permLoss, 1); outBeta.textContent = f(beta, 2);

          svg.innerHTML = '<rect x="40" y="20" width="420" height="120" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>' +
                          '<line x1="60" y1="50" x2="400" y2="50" stroke="#0f172a" stroke-width="4"/>' +
                          '<line x1="60" y1="110" x2="400" y2="110" stroke="#0f172a" stroke-width="4"/>' +
                          '<rect x="225" y="50" width="8" height="25" fill="#ef4444"/>' +
                          '<rect x="225" y="85" width="8" height="25" fill="#ef4444"/>' +
                          '<text x="245" y="70" font-size="12" fill="#0369a1" font-weight="700">Q = ' + f(Q_m3s * 1000, 2) + ' L/s</text>' +
                          '<text x="245" y="95" font-size="11" fill="#475569">Permanent loss = ' + f(permLoss, 1) + ' kPa</text>';
          diag.textContent = 'Orifice meter flow rate is ' + f(Q_m3s * 1000, 2) + ' L/s with beta ratio ' + f(beta, 2) + '.';
        }
        [sD, sDp].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 8, unit: 8,
      html: '<header><span class="eyebrow">Unit 8 Laboratory</span><h3>Parallel Piping Network Flow Distribution</h3><p class="lead">Simulate flow split between parallel pipe lines sharing common header nodes.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Total Header Flow Q <span><output id="v-qtot8">100</output> m³/h</span></label><input type="range" id="s-qtot8" min="20" max="300" step="10" value="100"></div>' +
              '<div class="control-group"><label>Branch 1 Length L1 <span><output id="v-l1">50</output> m</span></label><input type="range" id="s-l1" min="10" max="200" step="10" value="50"></div>' +
              '<div class="control-group"><label>Branch 2 Length L2 <span><output id="v-l2">100</output> m</span></label><input type="range" id="s-l2" min="20" max="300" step="10" value="100"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Branch 1 Flow Q1</small><output id="out-q1b">58.6</output> m³/h</div>' +
              '<div class="stat-box"><small>Branch 2 Flow Q2</small><output id="out-q2b">41.4</output> m³/h</div>' +
              '<div class="stat-box"><small>Common Head Loss</small><output id="out-hloss">4.22</output> m</div>' +
            '</div>' +
            '<svg id="svg-ffp8" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-ffp8">Hydraulic law: Total flow Q = Q1 + Q2 with equal head loss \u0394h1 = \u0394h2 across parallel paths.</div>',
      init: function(card) {
        var sQ = card.querySelector('#s-qtot8'), sL1 = card.querySelector('#s-l1'), sL2 = card.querySelector('#s-l2');
        var vQ = card.querySelector('#v-qtot8'), vL1 = card.querySelector('#v-l1'), vL2 = card.querySelector('#v-l2');
        var outQ1 = card.querySelector('#out-q1b'), outQ2 = card.querySelector('#out-q2b'), outH = card.querySelector('#out-hloss');
        var svg = card.querySelector('#svg-ffp8'), diag = card.querySelector('#diag-ffp8');

        function update() {
          var Q = parseFloat(sQ.value), l1 = parseFloat(sL1.value), l2 = parseFloat(sL2.value);
          vQ.textContent = f(Q, 0); vL1.textContent = f(l1, 0); vL2.textContent = f(l2, 0);

          // Head loss ~ L * Q^2 => Q1 * sqrt(L1) = Q2 * sqrt(L2)
          // Q1 = Q / (1 + sqrt(L1/L2))
          var rL = Math.sqrt(l1 / l2);
          var q1 = Q / (1.0 + rL);
          var q2 = Q - q1;
          var hLoss = 0.001 * l1 * Math.pow(q1 / 10.0, 2);

          outQ1.textContent = f(q1, 1); outQ2.textContent = f(q2, 1); outH.textContent = f(hLoss, 2);

          svg.innerHTML = '<rect x="40" y="20" width="420" height="120" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>' +
                          '<line x1="60" y1="80" x2="160" y2="80" stroke="#0f172a" stroke-width="4"/>' +
                          '<line x1="160" y1="80" x2="220" y2="50" stroke="#0284c7" stroke-width="3"/>' +
                          '<line x1="220" y1="50" x2="320" y2="50" stroke="#0284c7" stroke-width="3"/>' +
                          '<line x1="320" y1="50" x2="380" y2="80" stroke="#0284c7" stroke-width="3"/>' +
                          '<line x1="160" y1="80" x2="220" y2="110" stroke="#10b981" stroke-width="3"/>' +
                          '<line x1="220" y1="110" x2="320" y2="110" stroke="#10b981" stroke-width="3"/>' +
                          '<line x1="320" y1="110" x2="380" y2="80" stroke="#10b981" stroke-width="3"/>' +
                          '<line x1="380" y1="80" x2="440" y2="80" stroke="#0f172a" stroke-width="4"/>' +
                          '<text x="230" y="42" font-size="11" fill="#0369a1" font-weight="700">Branch 1: ' + f(q1,1) + ' m³/h (' + f(l1,0) + 'm)</text>' +
                          '<text x="230" y="125" font-size="11" fill="#047857" font-weight="700">Branch 2: ' + f(q2,1) + ' m³/h (' + f(l2,0) + 'm)</text>' +
                          '<text x="65" y="70" font-size="11" fill="#0f172a">In: ' + f(Q,0) + '</text>';
          diag.textContent = 'Network balance: Branch 1 takes ' + f(q1, 1) + ' m³/h, Branch 2 takes ' + f(q2, 1) + ' m³/h (Head loss = ' + f(hLoss, 2) + ' m).';
        }
        [sQ, sL1, sL2].forEach(function(el) { el.addEventListener('input', update); });
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
