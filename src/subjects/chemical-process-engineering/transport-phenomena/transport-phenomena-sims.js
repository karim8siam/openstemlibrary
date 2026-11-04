/* Transport Phenomena Interactive Simulation Suite */
(function(window) {
  'use strict';

  function f(n, d) { d = (d !== undefined) ? d : 2; return Number.isFinite(n) ? n.toFixed(d) : '0.00'; }

  var MODELS = [
    {
      idx: 1, unit: 1,
      html: '<header><span class="eyebrow">Unit 1 Laboratory</span><h3>Transient Well-Mixed Tank Tracer Response</h3><p class="lead">Simulate macroscopic species accumulation dc/dt = (q/V)*(cin - c) under step change.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Tank Volume V <span><output id="v-vol1">3.0</output> m³</span></label><input type="range" id="s-vol1" min="0.5" max="10.0" step="0.5" value="3.0"></div>' +
              '<div class="control-group"><label>Flow Rate q <span><output id="v-q1">0.10</output> m³/s</span></label><input type="range" id="s-q1" min="0.02" max="0.50" step="0.02" value="0.10"></div>' +
              '<div class="control-group"><label>Inlet Conc cin <span><output id="v-cin1">50.0</output> mol/m³</span></label><input type="range" id="s-cin1" min="10" max="100" step="5" value="50"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Space Time \u03C4</small><output id="out-tau1">30.0</output> s</div>' +
              '<div class="stat-box"><small>95% Response Time</small><output id="out-t95">89.9</output> s</div>' +
              '<div class="stat-box"><small>Steady Outlet c_inf</small><output id="out-cinf">50.0</output> mol/m³</div>' +
            '</div>' +
            '<svg id="svg-tp1" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-tp1">First-order dynamic response: c(t) = cin * (1 - exp(-t/\u03C4)) starting from zero initial holdup.</div>',
      init: function(card) {
        var sVol = card.querySelector('#s-vol1'), sQ = card.querySelector('#s-q1'), sCin = card.querySelector('#s-cin1');
        var vVol = card.querySelector('#v-vol1'), vQ = card.querySelector('#v-q1'), vCin = card.querySelector('#v-cin1');
        var outTau = card.querySelector('#out-tau1'), outT95 = card.querySelector('#out-t95'), outCinf = card.querySelector('#out-cinf');
        var svg = card.querySelector('#svg-tp1'), diag = card.querySelector('#diag-tp1');

        function update() {
          var vol = parseFloat(sVol.value), q = parseFloat(sQ.value), cin = parseFloat(sCin.value);
          vVol.textContent = f(vol, 1); vQ.textContent = f(q, 2); vCin.textContent = f(cin, 0);

          var tau = vol / q;
          var t95 = 2.996 * tau;

          outTau.textContent = f(tau, 1); outT95.textContent = f(t95, 1); outCinf.textContent = f(cin, 1);

          var pts = '';
          for (var t = 0; t <= 120; t += 2) {
            var cVal = cin * (1.0 - Math.exp(-t / tau));
            var xP = 50 + (t / 120.0) * 380;
            var yP = 135 - (cVal / 100.0) * 105;
            pts += (pts ? ' ' : '') + xP.toFixed(1) + ',' + yP.toFixed(1);
          }

          svg.innerHTML = '<rect x="35" y="15" width="430" height="130" fill="#f8fafc" stroke="#cbd5e1"/>' +
                          '<polyline points="' + pts + '" fill="none" stroke="#0284c7" stroke-width="2.5"/>' +
                          '<line x1="50" y1="135" x2="430" y2="135" stroke="#94a3b8" stroke-width="1.5"/>' +
                          '<line x1="50" y1="135" x2="50" y2="25" stroke="#94a3b8" stroke-width="1.5"/>' +
                          '<text x="60" y="35" font-size="11" fill="#0369a1" font-weight="700">Concentration c(t) [mol/m³] vs Time (s)</text>' +
                          '<text x="240" y="148" font-size="10" fill="#64748b">Time (s)</text>' +
                          '<text x="320" y="70" font-size="11" fill="#b91c1c" font-weight="700">\u03C4 = ' + f(tau,1) + ' s</text>';
          diag.textContent = 'Well-mixed reactor dynamic response: Hydraulic space time \u03C4 = ' + f(tau, 1) + ' s.';
        }
        [sVol, sQ, sCin].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 2, unit: 2,
      html: '<header><span class="eyebrow">Unit 2 Laboratory</span><h3>Hagen-Poiseuille Parabolic Laminar Velocity Profile</h3><p class="lead">Evaluate Navier-Stokes shell momentum balance in circular cylindrical coordinates.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Pressure Gradient dP/L <span><output id="v-dpl2">500</output> Pa/m</span></label><input type="range" id="s-dpl2" min="100" max="2000" step="50" value="500"></div>' +
              '<div class="control-group"><label>Pipe Radius R <span><output id="v-rad2">25</output> mm</span></label><input type="range" id="s-rad2" min="10" max="60" step="5" value="25"></div>' +
              '<div class="control-group"><label>Viscosity \u03BC <span><output id="v-mu2">10.0</output> mPa·s</span></label><input type="range" id="s-mu2" min="1.0" max="50.0" step="1.0" value="10.0"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Centerline Velocity vmax</small><output id="out-vmax2">7.81</output> m/s</div>' +
              '<div class="stat-box"><small>Average Velocity v_avg</small><output id="out-vavg2">3.91</output> m/s</div>' +
              '<div class="stat-box"><small>Volumetric Flow Q</small><output id="out-flow2">7.67</output> L/s</div>' +
            '</div>' +
            '<svg id="svg-tp2" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-tp2">Navier-Stokes solution: vz(r) = (dP/L) * (R² - r²) / (4*\u03BC); vmax = 2 * v_avg.</div>',
      init: function(card) {
        var sDpl = card.querySelector('#s-dpl2'), sRad = card.querySelector('#s-rad2'), sMu = card.querySelector('#s-mu2');
        var vDpl = card.querySelector('#v-dpl2'), vRad = card.querySelector('#v-rad2'), vMu = card.querySelector('#v-mu2');
        var outVmax = card.querySelector('#out-vmax2'), outVavg = card.querySelector('#out-vavg2'), outFlow = card.querySelector('#out-flow2');
        var svg = card.querySelector('#svg-tp2'), diag = card.querySelector('#diag-tp2');

        function update() {
          var dpl = parseFloat(sDpl.value), R = parseFloat(sRad.value) / 1000.0, mu = parseFloat(sMu.value) / 1000.0;
          vDpl.textContent = f(dpl, 0); vRad.textContent = f(R * 1000.0, 0); vMu.textContent = f(mu * 1000.0, 1);

          var vmax = (dpl * Math.pow(R, 2)) / (4.0 * mu);
          var vavg = vmax / 2.0;
          var Q_Lps = (vavg * Math.PI * Math.pow(R, 2)) * 1000.0;

          outVmax.textContent = f(vmax, 2); outVavg.textContent = f(vavg, 2); outFlow.textContent = f(Q_Lps, 2);

          var pts = '';
          for (var rNorm = -1.0; rNorm <= 1.0; rNorm += 0.05) {
            var v_r = vmax * (1.0 - Math.pow(rNorm, 2));
            var yPlot = 80 + rNorm * 50;
            var xPlot = 80 + Math.min(300, (v_r / Math.max(1, vmax)) * 260);
            pts += (pts ? ' ' : '') + xPlot.toFixed(1) + ',' + yPlot.toFixed(1);
          }

          svg.innerHTML = '<rect x="40" y="20" width="420" height="120" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>' +
                          '<line x1="80" y1="30" x2="400" y2="30" stroke="#0f172a" stroke-width="3"/>' +
                          '<line x1="80" y1="130" x2="400" y2="130" stroke="#0f172a" stroke-width="3"/>' +
                          '<line x1="80" y1="30" x2="80" y2="130" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="2"/>' +
                          '<polyline points="' + pts + '" fill="none" stroke="#0284c7" stroke-width="2.5"/>' +
                          '<line x1="80" y1="80" x2="' + (80 + 260) + '" y2="80" stroke="#ef4444" stroke-width="1.5"/>' +
                          '<text x="290" y="75" font-size="11" fill="#b91c1c" font-weight="700">vmax = ' + f(vmax, 2) + ' m/s</text>' +
                          '<text x="90" y="25" font-size="10" fill="#475569">Pipe wall r = +R</text>' +
                          '<text x="90" y="145" font-size="10" fill="#475569">Pipe wall r = -R</text>';
          diag.textContent = 'Parabolic profile confirmed: Mean velocity ' + f(vavg, 2) + ' m/s delivers volumetric flow of ' + f(Q_Lps, 2) + ' L/s.';
        }
        [sDpl, sRad, sMu].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 3, unit: 3,
      html: '<header><span class="eyebrow">Unit 3 Laboratory</span><h3>Laminar Boundary Layer Growth over a Flat Plate</h3><p class="lead">Simulate Prandtl boundary layer thickness delta(x) and local skin friction coefficient.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Free Stream Velocity U_inf <span><output id="v-uinf">2.0</output> m/s</span></label><input type="range" id="s-uinf" min="0.5" max="10.0" step="0.5" value="2.0"></div>' +
              '<div class="control-group"><label>Kinematic Viscosity \u03BD <span><output id="v-nu3">1.0</output> mm²/s</span></label><input type="range" id="s-nu3" min="0.5" max="10.0" step="0.5" value="1.0"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Plate End Thickness \u03B4(L)</small><output id="out-del3">3.54</output> mm</div>' +
              '<div class="stat-box"><small>Reynolds Re_L</small><output id="out-rel">2.00e5</output></div>' +
              '<div class="stat-box"><small>Skin Friction Cf</small><output id="out-cf3">0.0015</output></div>' +
            '</div>' +
            '<svg id="svg-tp3" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-tp3">Blasius exact boundary layer solution: \u03B4(x) = 5.0 * sqrt(\u03BD * x / U_inf); Cf = 0.664 / sqrt(Re_x).</div>',
      init: function(card) {
        var sU = card.querySelector('#s-uinf'), sNu = card.querySelector('#s-nu3');
        var vU = card.querySelector('#v-uinf'), vNu = card.querySelector('#v-nu3');
        var outDel = card.querySelector('#out-del3'), outRel = card.querySelector('#out-rel'), outCf = card.querySelector('#out-cf3');
        var svg = card.querySelector('#svg-tp3'), diag = card.querySelector('#diag-tp3');

        function update() {
          var U = parseFloat(sU.value), nu = parseFloat(sNu.value) * 1e-6; // m2/s
          vU.textContent = f(U, 1); vNu.textContent = f(nu * 1e6, 1);

          var L = 1.0; // 1 m plate
          var Re_L = (U * L) / nu;
          var delta_L_mm = (5.0 * Math.sqrt((nu * L) / U)) * 1000.0;
          var cf = 0.664 / Math.sqrt(Math.max(1, Re_L));

          outDel.textContent = f(delta_L_mm, 2); outRel.textContent = Re_L.toExponential(2); outCf.textContent = f(cf, 4);

          var pts = '';
          for (var x = 0.05; x <= 1.0; x += 0.05) {
            var del_x = (5.0 * Math.sqrt((nu * x) / U)) * 1000.0;
            var xP = 60 + x * 340;
            var yP = 130 - Math.min(90, (del_x / 10.0) * 90);
            pts += (pts ? ' ' : '') + xP.toFixed(1) + ',' + yP.toFixed(1);
          }

          svg.innerHTML = '<rect x="40" y="20" width="420" height="120" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>' +
                          '<line x1="60" y1="130" x2="400" y2="130" stroke="#0f172a" stroke-width="4"/>' +
                          '<polyline points="' + pts + '" fill="none" stroke="#0284c7" stroke-width="2.5"/>' +
                          '<text x="65" y="38" font-size="11" fill="#0369a1" font-weight="700">Boundary Layer Thickness \u03B4(x)</text>' +
                          '<text x="260" y="75" font-size="11" fill="#b91c1c" font-weight="700">\u03B4(L) = ' + f(delta_L_mm, 2) + ' mm</text>' +
                          '<text x="60" y="145" font-size="10" fill="#475569">Leading edge x = 0</text>' +
                          '<text x="350" y="145" font-size="10" fill="#475569">Trailing edge x = 1 m</text>';
          diag.textContent = 'Boundary layer growth: Terminal thickness is ' + f(delta_L_mm, 2) + ' mm at trailing edge (Re_L = ' + Re_L.toExponential(2) + ').';
        }
        [sU, sNu].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 4, unit: 4,
      html: '<header><span class="eyebrow">Unit 4 Laboratory</span><h3>Steady 1D Conduction with Internal Heat Generation</h3><p class="lead">Solve Fourier heat conduction across a plane slab: d²T/dx² + q_gen/k = 0.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Heat Generation q_gen <span><output id="v-qgen">50</output> kW/m³</span></label><input type="range" id="s-qgen" min="10" max="200" step="10" value="50"></div>' +
              '<div class="control-group"><label>Thermal Conduct k <span><output id="v-k4">25</output> W/m·K</span></label><input type="range" id="s-k4" min="5" max="100" step="5" value="25"></div>' +
              '<div class="control-group"><label>Half Thickness L <span><output id="v-thk">0.05</output> m</span></label><input type="range" id="s-thk" min="0.02" max="0.15" step="0.01" value="0.05"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Centerline Temp T0</small><output id="out-t0">52.5</output> °C</div>' +
              '<div class="stat-box"><small>Surface Flux q_surf</small><output id="out-qsurf">2.50</output> kW/m²</div>' +
              '<div class="stat-box"><small>Temp Rise \u0394T</small><output id="out-delt4">2.50</output> °C</div>' +
            '</div>' +
            '<svg id="svg-tp4" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-tp4">Parabolic temperature distribution T(x) = T_surf + (q_gen / 2k) * (L² - x²).</div>',
      init: function(card) {
        var sQ = card.querySelector('#s-qgen'), sK = card.querySelector('#s-k4'), sThk = card.querySelector('#s-thk');
        var vQ = card.querySelector('#v-qgen'), vK = card.querySelector('#v-k4'), vThk = card.querySelector('#v-thk');
        var outT0 = card.querySelector('#out-t0'), outQsurf = card.querySelector('#out-qsurf'), outDelt = card.querySelector('#out-delt4');
        var svg = card.querySelector('#svg-tp4'), diag = card.querySelector('#diag-tp4');

        function update() {
          var qgen = parseFloat(sQ.value) * 1000.0, k = parseFloat(sK.value), L = parseFloat(sThk.value);
          vQ.textContent = f(qgen / 1000.0, 0); vK.textContent = f(k, 0); vThk.textContent = f(L, 2);

          var T_surf = 50.0;
          var deltaT = (qgen * Math.pow(L, 2)) / (2.0 * k);
          var T0 = T_surf + deltaT;
          var qSurf_kW = (qgen * L) / 1000.0;

          outT0.textContent = f(T0, 2); outQsurf.textContent = f(qSurf_kW, 2); outDelt.textContent = f(deltaT, 2);

          var pts = '';
          for (var xNorm = -1.0; xNorm <= 1.0; xNorm += 0.05) {
            var T_x = T_surf + deltaT * (1.0 - Math.pow(xNorm, 2));
            var xP = 230 + xNorm * 150;
            var yP = 130 - Math.min(95, ((T_x - 50.0) / Math.max(1, deltaT * 1.3)) * 85);
            pts += (pts ? ' ' : '') + xP.toFixed(1) + ',' + yP.toFixed(1);
          }

          svg.innerHTML = '<rect x="40" y="20" width="420" height="120" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>' +
                          '<polyline points="' + pts + '" fill="none" stroke="#ef4444" stroke-width="2.5"/>' +
                          '<line x1="80" y1="20" x2="80" y2="140" stroke="#64748b" stroke-width="1.5" stroke-dasharray="3"/>' +
                          '<line x1="380" y1="20" x2="380" y2="140" stroke="#64748b" stroke-width="1.5" stroke-dasharray="3"/>' +
                          '<text x="60" y="35" font-size="11" fill="#b91c1c" font-weight="700">Temperature Profile T(x)</text>' +
                          '<text x="210" y="40" font-size="11" fill="#b91c1c" font-weight="700">T0 = ' + f(T0, 2) + ' °C</text>' +
                          '<text x="50" y="150" font-size="10" fill="#475569">x = -L</text>' +
                          '<text x="220" y="150" font-size="10" fill="#475569">x = 0</text>' +
                          '<text x="370" y="150" font-size="10" fill="#475569">x = +L</text>';
          diag.textContent = 'Fourier conduction solved: Internal heat generation elevates slab center to ' + f(T0, 2) + ' °C (\u0394T = ' + f(deltaT, 2) + ' °C).';
        }
        [sQ, sK, sThk].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 5, unit: 5,
      html: '<header><span class="eyebrow">Unit 5 Laboratory</span><h3>Convective Heat Transfer Nusselt Correlation</h3><p class="lead">Simulate Dittus-Boelter turbulent pipe flow heat transfer coefficient.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Reynolds Re <span><output id="v-re5">50000</output></span></label><input type="range" id="s-re5" min="10000" max="200000" step="5000" value="50000"></div>' +
              '<div class="control-group"><label>Prandtl Pr <span><output id="v-pr5">5.0</output></span></label><input type="range" id="s-pr5" min="0.7" max="15.0" step="0.5" value="5.0"></div>' +
              '<div class="control-group"><label>Pipe Diameter D <span><output id="v-d5">50</output> mm</span></label><input type="range" id="s-d5" min="20" max="150" step="5" value="50"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Nusselt Number Nu</small><output id="out-nu5">251.3</output></div>' +
              '<div class="stat-box"><small>Heat Coeff h</small><output id="out-hcoeff">3016</output> W/m²·K</div>' +
              '<div class="stat-box"><small>Thermal Resistance</small><output id="out-rth">0.33</output> m²·K/kW</div>' +
            '</div>' +
            '<svg id="svg-tp5" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-tp5">Dittus-Boelter correlation: Nu = 0.023 * Re^0.8 * Pr^0.4 (turbulent heating).</div>',
      init: function(card) {
        var sRe = card.querySelector('#s-re5'), sPr = card.querySelector('#s-pr5'), sD = card.querySelector('#s-d5');
        var vRe = card.querySelector('#v-re5'), vPr = card.querySelector('#v-pr5'), vD = card.querySelector('#v-d5');
        var outNu = card.querySelector('#out-nu5'), outH = card.querySelector('#out-hcoeff'), outR = card.querySelector('#out-rth');
        var svg = card.querySelector('#svg-tp5'), diag = card.querySelector('#diag-tp5');

        function update() {
          var Re = parseFloat(sRe.value), Pr = parseFloat(sPr.value), D = parseFloat(sD.value) / 1000.0;
          vRe.textContent = f(Re, 0); vPr.textContent = f(Pr, 1); vD.textContent = f(D * 1000.0, 0);

          var kFluid = 0.60; // Water W/m K
          var Nu = 0.023 * Math.pow(Re, 0.8) * Math.pow(Pr, 0.4);
          var h = (Nu * kFluid) / D;
          var Rth = (1000.0 / h);

          outNu.textContent = f(Nu, 1); outH.textContent = f(h, 0); outR.textContent = f(Rth, 2);

          var barW = Math.min(360, (h / 8000.0) * 360);
          svg.innerHTML = '<rect x="40" y="20" width="420" height="120" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>' +
                          '<rect x="60" y="55" width="' + barW + '" height="35" rx="4" fill="#0284c7"/>' +
                          '<text x="60" y="45" font-size="12" fill="#0369a1" font-weight="700">Convective Film Coefficient h = ' + f(h, 0) + ' W/m²·K</text>' +
                          '<text x="60" y="115" font-size="11" fill="#475569">Nusselt Nu = ' + f(Nu, 1) + ' | Thermal resistance: ' + f(Rth, 2) + ' m²·K/kW</text>';
          diag.textContent = 'Turbulent convection: Film coefficient h = ' + f(h, 0) + ' W/m²·K at Re = ' + f(Re, 0) + '.';
        }
        [sRe, sPr, sD].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 6, unit: 6,
      html: '<header><span class="eyebrow">Unit 6 Laboratory</span><h3>Equimolar Counterdiffusion Concentration Gradient</h3><p class="lead">Simulate Fickian 1D steady binary mass diffusion between parallel boundaries.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Boundary Conc cA1 <span><output id="v-ca1">1.00</output> mol/m³</span></label><input type="range" id="s-ca1" min="0.2" max="2.0" step="0.1" value="1.0"></div>' +
              '<div class="control-group"><label>Boundary Conc cA2 <span><output id="v-ca2">0.20</output> mol/m³</span></label><input type="range" id="s-ca2" min="0.0" max="0.8" step="0.05" value="0.2"></div>' +
              '<div class="control-group"><label>Diffusivity DAB <span><output id="v-dab6">2.0</output> ×10⁻⁵ m²/s</span></label><input type="range" id="s-dab6" min="0.5" max="5.0" step="0.5" value="2.0"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Molar Flux JA</small><output id="out-ja6">16.0</output> \u03BCmol/m²·s</div>' +
              '<div class="stat-box"><small>Counter Flux JB</small><output id="out-jb6">-16.0</output> \u03BCmol/m²·s</div>' +
              '<div class="stat-box"><small>Concentration Drop</small><output id="out-dca">0.80</output> mol/m³</div>' +
            '</div>' +
            '<svg id="svg-tp6" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-tp6">Fick first law: JA = -DAB * (dcA/dz); linear profile under equimolar counterdiffusion.</div>',
      init: function(card) {
        var sCa1 = card.querySelector('#s-ca1'), sCa2 = card.querySelector('#s-ca2'), sDab = card.querySelector('#s-dab6');
        var vCa1 = card.querySelector('#v-ca1'), vCa2 = card.querySelector('#v-ca2'), vDab = card.querySelector('#v-dab6');
        var outJa = card.querySelector('#out-ja6'), outJb = card.querySelector('#out-jb6'), outDca = card.querySelector('#out-dca');
        var svg = card.querySelector('#svg-tp6'), diag = card.querySelector('#diag-tp6');

        function update() {
          var ca1 = parseFloat(sCa1.value), ca2 = parseFloat(sCa2.value), dab = parseFloat(sDab.value) * 1e-5;
          vCa1.textContent = f(ca1, 2); vCa2.textContent = f(ca2, 2); vDab.textContent = f(dab * 1e5, 1);

          var deltaZ = 1.0; // 1 m gap
          var JA_umol = (dab * (ca1 - ca2) / deltaZ) * 1e6;
          var JB_umol = -JA_umol;

          outJa.textContent = f(JA_umol, 1); outJb.textContent = f(JB_umol, 1); outDca.textContent = f(ca1 - ca2, 2);

          svg.innerHTML = '<rect x="40" y="20" width="420" height="120" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>' +
                          '<line x1="80" y1="' + (130 - (ca1 / 2.0) * 95) + '" x2="380" y2="' + (130 - (ca2 / 2.0) * 95) + '" stroke="#0284c7" stroke-width="3"/>' +
                          '<circle cx="80" cy="' + (130 - (ca1 / 2.0) * 95) + '" r="5" fill="#10b981"/>' +
                          '<circle cx="380" cy="' + (130 - (ca2 / 2.0) * 95) + '" r="5" fill="#ef4444"/>' +
                          '<text x="60" y="35" font-size="11" fill="#0369a1" font-weight="700">Linear Concentration Gradient cA(z)</text>' +
                          '<text x="80" y="145" font-size="10" fill="#475569">z = 0 (cA1 = ' + f(ca1,2) + ')</text>' +
                          '<text x="320" y="145" font-size="10" fill="#475569">z = L (cA2 = ' + f(ca2,2) + ')</text>' +
                          '<text x="210" y="70" font-size="12" fill="#047857" font-weight="700">JA = ' + f(JA_umol, 1) + ' \u03BCmol/m²·s</text>';
          diag.textContent = 'Fickian diffusion balance: Molar flux JA = ' + f(JA_umol, 1) + ' \u03BCmol/m²·s; equimolar condition JB = -JA holds.';
        }
        [sCa1, sCa2, sDab].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 7, unit: 7,
      html: '<header><span class="eyebrow">Unit 7 Laboratory</span><h3>Two-Film Interphase Mass Transfer Model</h3><p class="lead">Evaluate gas-liquid film resistances and overall mass transfer coefficient K_L.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Liquid Film kL <span><output id="v-kl7">5.0</output> ×10⁻⁵ m/s</span></label><input type="range" id="s-kl7" min="1.0" max="15.0" step="1.0" value="5.0"></div>' +
              '<div class="control-group"><label>Gas Film kG <span><output id="v-kg7">2.0</output> ×10⁻³ mol/m²·s·Pa</span></label><input type="range" id="s-kg7" min="0.5" max="6.0" step="0.5" value="2.0"></div>' +
              '<div class="control-group"><label>Henry Constant H <span><output id="v-h7">2500</output> Pa·m³/mol</span></label><input type="range" id="s-h7" min="500" max="10000" step="500" value="2500"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Overall Coeff KL</small><output id="out-kl7">4.00</output> ×10⁻⁵ m/s</div>' +
              '<div class="stat-box"><small>Liquid Resistance</small><output id="out-resl">80.0</output> %</div>' +
              '<div class="stat-box"><small>Gas Resistance</small><output id="out-resg">20.0</output> %</div>' +
            '</div>' +
            '<svg id="svg-tp7" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-tp7">Two-resistance theory: 1/KL = 1/kL + 1/(H * kG); Henry law governs gas-liquid partition.</div>',
      init: function(card) {
        var sKl = card.querySelector('#s-kl7'), sKg = card.querySelector('#s-kg7'), sH = card.querySelector('#s-h7');
        var vKl = card.querySelector('#v-kl7'), vKg = card.querySelector('#v-kg7'), vH = card.querySelector('#v-h7');
        var outKl = card.querySelector('#out-kl7'), outResl = card.querySelector('#out-resl'), outResg = card.querySelector('#out-resg');
        var svg = card.querySelector('#svg-tp7'), diag = card.querySelector('#diag-tp7');

        function update() {
          var kL = parseFloat(sKl.value) * 1e-5, kG = parseFloat(sKg.value) * 1e-3, H = parseFloat(sH.value);
          vKl.textContent = f(kL * 1e5, 1); vKg.textContent = f(kG * 1e3, 1); vH.textContent = f(H, 0);

          var rL = 1.0 / kL;
          var rG = 1.0 / (H * kG);
          var rTot = rL + rG;
          var KL = 1.0 / rTot;
          var pctL = (rL / rTot) * 100.0;
          var pctG = (rG / rTot) * 100.0;

          outKl.textContent = f(KL * 1e5, 2); outResl.textContent = f(pctL, 1); outResg.textContent = f(pctG, 1);

          svg.innerHTML = '<rect x="40" y="20" width="420" height="120" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>' +
                          '<rect x="60" y="55" width="' + (pctL * 3.4) + '" height="35" fill="#0284c7" rx="4"/>' +
                          '<rect x="' + (60 + pctL * 3.4) + '" y="55" width="' + (pctG * 3.4) + '" height="35" fill="#f59e0b" rx="4"/>' +
                          '<text x="65" y="45" font-size="11" fill="#0369a1" font-weight="700">Liquid Resistance (' + f(pctL,1) + '%)</text>' +
                          '<text x="' + Math.max(220, 60 + pctL * 3.4 + 5) + '" y="45" font-size="11" fill="#b45309" font-weight="700">Gas Resistance (' + f(pctG,1) + '%)</text>' +
                          '<text x="60" y="115" font-size="12" fill="#0f172a" font-weight="700">Overall Mass Transfer Coeff KL = ' + f(KL * 1e5, 2) + ' ×10⁻⁵ m/s</text>';
          diag.textContent = 'Interphase resistance: ' + (pctL > 50 ? 'Liquid-film controlled' : 'Gas-film controlled') + ' (' + f(pctL, 1) + '% liquid resistance).';
        }
        [sKl, sKg, sH].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 8, unit: 8,
      html: '<header><span class="eyebrow">Unit 8 Laboratory</span><h3>Chilton-Colburn Heat & Mass Transfer Analogy</h3><p class="lead">Simulate jH, jD factors, friction factor f/2, and transport analogy equivalence.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Friction Factor f <span><output id="v-f8">0.024</output></span></label><input type="range" id="s-f8" min="0.012" max="0.050" step="0.002" value="0.024"></div>' +
              '<div class="control-group"><label>Schmidt Number Sc <span><output id="v-sc8">1.2</output></span></label><input type="range" id="s-sc8" min="0.5" max="3.0" step="0.1" value="1.2"></div>' +
              '<div class="control-group"><label>Prandtl Number Pr <span><output id="v-pr8">0.7</output></span></label><input type="range" id="s-pr8" min="0.5" max="3.0" step="0.1" value="0.7"></div>' +
            '</div>' +
            '<div class="stats-row">' +
              '<div class="stat-box"><small>Colburn jH Factor</small><output id="out-jh8">0.0120</output></div>' +
              '<div class="stat-box"><small>Colburn jD Factor</small><output id="out-jd8">0.0120</output></div>' +
              '<div class="stat-box"><small>Skin Friction f/2</small><output id="out-fhalf">0.0120</output></div>' +
            '</div>' +
            '<svg id="svg-tp8" viewBox="0 0 500 160" width="100%" height="160"></svg>' +
            '<div class="diagnostic-note" id="diag-tp8">Chilton-Colburn analogy: jH = St * Pr^(2/3) = jD = Sh / (Re * Sc^(1/3)) = f / 2.</div>',
      init: function(card) {
        var sF = card.querySelector('#s-f8'), sSc = card.querySelector('#s-sc8'), sPr = card.querySelector('#s-pr8');
        var vF = card.querySelector('#v-f8'), vSc = card.querySelector('#v-sc8'), vPr = card.querySelector('#v-pr8');
        var outJh = card.querySelector('#out-jh8'), outJd = card.querySelector('#out-jd8'), outFh = card.querySelector('#out-fhalf');
        var svg = card.querySelector('#svg-tp8'), diag = card.querySelector('#diag-tp8');

        function update() {
          var fVal = parseFloat(sF.value), sc = parseFloat(sSc.value), pr = parseFloat(sPr.value);
          vF.textContent = f(fVal, 3); vSc.textContent = f(sc, 1); vPr.textContent = f(pr, 1);

          var fHalf = fVal / 2.0;
          var jH = fHalf;
          var jD = fHalf;

          outJh.textContent = f(jH, 4); outJd.textContent = f(jD, 4); outFh.textContent = f(fHalf, 4);

          svg.innerHTML = '<rect x="40" y="20" width="420" height="120" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>' +
                          '<rect x="60" y="50" width="100" height="40" rx="4" fill="#0284c7"/>' +
                          '<rect x="180" y="50" width="100" height="40" rx="4" fill="#10b981"/>' +
                          '<rect x="300" y="50" width="100" height="40" rx="4" fill="#f59e0b"/>' +
                          '<text x="75" y="75" font-size="12" fill="#fff" font-weight="700">jH = ' + f(jH, 4) + '</text>' +
                          '<text x="195" y="75" font-size="12" fill="#fff" font-weight="700">jD = ' + f(jD, 4) + '</text>' +
                          '<text x="315" y="75" font-size="12" fill="#fff" font-weight="700">f/2 = ' + f(fHalf, 4) + '</text>' +
                          '<text x="60" y="115" font-size="11" fill="#475569">Pr = ' + f(pr,1) + ' | Sc = ' + f(sc,1) + ' | Friction factor f = ' + f(fVal,3) + '</text>';
          diag.textContent = 'Analogy verified: Heat transfer jH, mass transfer jD, and momentum f/2 are unified at ' + f(fHalf, 4) + '.';
        }
        [sF, sSc, sPr].forEach(function(el) { el.addEventListener('input', update); });
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
