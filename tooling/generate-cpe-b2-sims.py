import os, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def get_engine_footer(total_units=8):
    return f"""
  if (!window.SimulationEngine) window.SimulationEngine = {{}};
  window.SimulationEngine.initSimulation = function(containerId, simType) {{
    var container = document.getElementById(containerId) ||
                    document.getElementById('sim-container') ||
                    document.querySelector('.simulation-slot');
    if (!container) return;
    container.innerHTML = '';
    var unitNum = 1;
    if (simType) {{
      var m = simType.match(/(\\d+)$/);
      if (m) unitNum = parseInt(m[1], 10);
    }} else {{
      var bMatch = document.body.dataset.chapterIndex;
      if (bMatch !== undefined && bMatch !== null && bMatch !== '') unitNum = parseInt(bMatch, 10) + 1;
      else {{
        var pMatch = window.location.pathname.match(/chapter-(\\d+)/);
        if (pMatch) unitNum = parseInt(pMatch[1], 10);
      }}
    }}
    if (isNaN(unitNum) || unitNum < 1 || unitNum > {total_units}) unitNum = 1;
    var modelsForUnit = MODELS.filter(function(m) {{ return m.unit === unitNum; }});
    if (modelsForUnit.length === 0) modelsForUnit = MODELS.filter(function(m) {{ return m.unit === 1; }});
    modelsForUnit.forEach(function(m) {{
      var card = document.createElement('section');
      card.className = 'cpe-sim-card';
      card.setAttribute('aria-label', 'Interactive Simulation ' + m.idx);
      card.id = 'sim-card-' + m.idx;
      card.innerHTML = m.html;
      container.appendChild(card);
      m.init(card);
    }});
  }};

  if (typeof document !== 'undefined') {{
    var autoInit = function() {{
      var slot = document.getElementById('sim-container') || document.querySelector('.simulation-slot');
      if (slot && slot.children.length === 0) {{
        window.SimulationEngine.initSimulation(slot.id || 'sim-container');
      }}
    }};
    if (document.readyState === 'loading') {{
      document.addEventListener('DOMContentLoaded', autoInit);
    }} else {{
      autoInit();
    }}
  }}
}})(typeof window === 'undefined' ? globalThis : window);
"""

# =========================================================================
# 1. Heat Transfer in Processes
# =========================================================================
def build_htp_sims():
    sim_js = """/* Heat Transfer in Processes Interactive Simulation Suite */
(function(window) {
  'use strict';

  function f(n, d) { d = (d !== undefined) ? d : 2; return Number.isFinite(n) ? n.toFixed(d) : '0.00'; }

  var MODELS = [
    {
      idx: 1, unit: 1,
      html: '<header><span class="eyebrow">Unit 1 Laboratory</span><h3>Process Steam Heat Exchanger Duty & Steam Consumption</h3><p class="lead">Simulate sensible heating of process liquid and compute required saturated utility steam consumption rate.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Process Fluid Flow ṁ <span><output id="v-flow">12.0</output> kg/s</span></label><input type="range" id="s-flow" min="1.0" max="50.0" step="0.5" value="12.0"></div>' +
              '<div class="control-group"><label>Inlet Temperature Tin <span><output id="v-tin">20.0</output> °C</span></label><input type="range" id="s-tin" min="5.0" max="60.0" step="1.0" value="20.0"></div>' +
              '<div class="control-group"><label>Outlet Temperature Tout <span><output id="v-tout">85.0</output> °C</span></label><input type="range" id="s-tout" min="40.0" max="140.0" step="1.0" value="85.0"></div>' +
              '<div class="control-group"><label>Steam Pressure Ps <span><output id="v-press">4.0</output> bar</span></label><input type="range" id="s-press" min="1.0" max="15.0" step="0.5" value="4.0"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Thermal Duty Q̇</div><div class="readout-value" id="r-qdot">3,260 kW</div></div>' +
              '<div class="readout-card"><div class="readout-label">Steam Temp Tsat</div><div class="readout-value" id="r-tsat">143.6 °C</div></div>' +
              '<div class="readout-card"><div class="readout-label">Latent Heat λ</div><div class="readout-value" id="r-lambda">2,133 kJ/kg</div></div>' +
              '<div class="readout-card"><div class="readout-label">Steam Flow Required</div><div class="readout-value" id="r-steam">5,502 kg/h</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-htp1" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-htp1"></p>',
      init: function(el) {
        var sFlow = el.querySelector('#s-flow'), vFlow = el.querySelector('#v-flow');
        var sTin = el.querySelector('#s-tin'), vTin = el.querySelector('#v-tin');
        var sTout = el.querySelector('#s-tout'), vTout = el.querySelector('#v-tout');
        var sPress = el.querySelector('#s-press'), vPress = el.querySelector('#v-press');
        var rQdot = el.querySelector('#r-qdot'), rTsat = el.querySelector('#r-tsat');
        var rLambda = el.querySelector('#r-lambda'), rSteam = el.querySelector('#r-steam');
        var svg = el.querySelector('#svg-htp1'), diag = el.querySelector('#diag-htp1');

        var Cp = 4.184; // kJ/(kg·K) water-like liquid

        function update() {
          var m = parseFloat(sFlow.value); vFlow.textContent = f(m, 1);
          var Tin = parseFloat(sTin.value); vTin.textContent = f(Tin, 1);
          var Tout = parseFloat(sTout.value); vTout.textContent = f(Tout, 1);
          var P = parseFloat(sPress.value); vPress.textContent = f(P, 1);

          if (Tout <= Tin) Tout = Tin + 1.0;

          var Q = m * Cp * (Tout - Tin); // kW
          var Tsat = 100 + 28.5 * Math.log(P); // Antoine approximation
          var lambda = 2257 - 40 * (P - 1.0); // latent heat kJ/kg
          var steamRate = (Q / Math.max(100, lambda)) * 3600; // kg/h

          rQdot.textContent = f(Q, 0) + ' kW';
          rTsat.textContent = f(Tsat, 1) + ' °C';
          rLambda.textContent = f(lambda, 0) + ' kJ/kg';
          rSteam.textContent = f(steamRate, 0) + ' kg/h';

          var barW = Math.min(300, Math.max(30, (Q / 10000) * 300));

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="180" y="50" width="240" height="100" fill="#f1f5f9" stroke="#334155" stroke-width="2" rx="6"/>' +
                          '<text x="300" y="85" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">Shell & Tube Heater</text>' +
                          '<text x="300" y="105" text-anchor="middle" font-size="12" fill="#0284c7">Steam at ' + f(P,1) + ' bar (' + f(Tsat,0) + '°C)</text>' +
                          '<text x="300" y="125" text-anchor="middle" font-size="11" font-weight="700" fill="#b91c1c">Duty Q̇ = ' + f(Q,0) + ' kW</text>' +
                          '<line x1="40" y1="100" x2="180" y2="100" stroke="#0284c7" stroke-width="4"/>' +
                          '<text x="110" y="85" text-anchor="middle" font-size="11" font-weight="700" fill="#0369a1">In: ' + f(Tin,0) + '°C</text>' +
                          '<line x1="420" y1="100" x2="560" y2="100" stroke="#dc2626" stroke-width="4"/>' +
                          '<text x="490" y="85" text-anchor="middle" font-size="11" font-weight="700" fill="#b91c1c">Out: ' + f(Tout,0) + '°C</text>' +
                          '<line x1="300" y1="15" x2="300" y2="50" stroke="#ea580c" stroke-width="3"/>' +
                          '<text x="305" y="32" font-size="10" font-weight="700" fill="#c2410c">Steam: ' + f(steamRate,0) + ' kg/h</text>' +
                          '<line x1="300" y1="150" x2="300" y2="185" stroke="#64748b" stroke-width="3"/>' +
                          '<text x="305" y="175" font-size="10" fill="#475569">Condensate</text>';
          diag.textContent = 'Enthalpy balance: Sensible heat addition Q̇ = ṁ·Cp·ΔT = ' + f(Q, 0) + ' kW. Steam flow: ' + f(steamRate, 0) + ' kg/h at ' + f(P, 1) + ' bar.';
        }
        [sFlow, sTin, sTout, sPress].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 2, unit: 2,
      html: '<header><span class="eyebrow">Unit 2 Laboratory</span><h3>Radial Cylindrical Conduction & Insulation Critical Radius</h3><p class="lead">Simulate heat loss through an insulated process pipe, evaluate conduction resistance, and detect critical insulation thickness.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Inner Pipe Radius r1 <span><output id="v-r1">25.0</output> mm</span></label><input type="range" id="s-r1" min="10.0" max="100.0" step="2.5" value="25.0"></div>' +
              '<div class="control-group"><label>Insulation Thickness t <span><output id="v-thick">30.0</output> mm</span></label><input type="range" id="s-thick" min="2.0" max="120.0" step="2.0" value="30.0"></div>' +
              '<div class="control-group"><label>Insulation Conductivity k <span><output id="v-k">0.045</output> W/(m·K)</span></label><input type="range" id="s-k" min="0.020" max="0.250" step="0.005" value="0.045"></div>' +
              '<div class="control-group"><label>Ambient Convection h <span><output id="v-h">10.0</output> W/(m²·K)</span></label><input type="range" id="s-h" min="2.0" max="30.0" step="1.0" value="10.0"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Outer Radius r2</div><div class="readout-value" id="r-r2">55.0 mm</div></div>' +
              '<div class="readout-card"><div class="readout-label">Critical Radius rcrit</div><div class="readout-value" id="r-rcrit">4.5 mm</div></div>' +
              '<div class="readout-card"><div class="readout-label">Heat Loss per Meter q\'</div><div class="readout-value" id="r-qloss">42.8 W/m</div></div>' +
              '<div class="readout-card"><div class="readout-label">Thermal Resistance R\'</div><div class="readout-value" id="r-rtot">3.04 m·K/W</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-htp2" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-htp2"></p>',
      init: function(el) {
        var sR1 = el.querySelector('#s-r1'), vR1 = el.querySelector('#v-r1');
        var sThick = el.querySelector('#s-thick'), vThick = el.querySelector('#v-thick');
        var sK = el.querySelector('#s-k'), vK = el.querySelector('#v-k');
        var sH = el.querySelector('#s-h'), vH = el.querySelector('#v-h');
        var rR2 = el.querySelector('#r-r2'), rRcrit = el.querySelector('#r-rcrit');
        var rQloss = el.querySelector('#r-qloss'), rRtot = el.querySelector('#r-rtot');
        var svg = el.querySelector('#svg-htp2'), diag = el.querySelector('#diag-htp2');

        var deltaT = 130; // Ti = 150 C, T_inf = 20 C

        function update() {
          var r1_mm = parseFloat(sR1.value); vR1.textContent = f(r1_mm, 1);
          var t_mm = parseFloat(sThick.value); vThick.textContent = f(t_mm, 1);
          var k = parseFloat(sK.value); vK.textContent = f(k, 3);
          var h = parseFloat(sH.value); vH.textContent = f(h, 1);

          var r1 = r1_mm / 1000;
          var r2 = (r1_mm + t_mm) / 1000;
          var rcrit = (k / h) * 1000; // mm

          var R_cond = Math.log(r2 / r1) / (2 * Math.PI * k);
          var R_conv = 1 / (2 * Math.PI * r2 * h);
          var R_tot = R_cond + R_conv;
          var qPrime = deltaT / Math.max(0.001, R_tot);

          rR2.textContent = f(r2 * 1000, 1) + ' mm';
          rRcrit.textContent = f(rcrit, 1) + ' mm';
          rQloss.textContent = f(qPrime, 1) + ' W/m';
          rRtot.textContent = f(R_tot, 2) + ' m·K/W';

          var cx = 300, cy = 100;
          var scale = 0.55;
          var rad1 = Math.min(60, r1_mm * scale);
          var rad2 = Math.min(85, (r1_mm + t_mm) * scale);

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<circle cx="' + cx + '" cy="' + cy + '" r="' + rad2 + '" fill="#fef08a" stroke="#ca8a04" stroke-width="2"/>' +
                          '<circle cx="' + cx + '" cy="' + cy + '" r="' + rad1 + '" fill="#cbd5e1" stroke="#475569" stroke-width="2"/>' +
                          '<circle cx="' + cx + '" cy="' + cy + '" r="' + (rad1 * 0.7) + '" fill="#ef4444"/>' +
                          '<text x="80" y="80" font-size="12" font-weight="700" fill="#0f172a">Insulated Pipe Section</text>' +
                          '<text x="80" y="105" font-size="11" fill="#475569">Pipe r1 = ' + f(r1_mm,1) + ' mm</text>' +
                          '<text x="80" y="125" font-size="11" fill="#ca8a04">Outer r2 = ' + f(r2*1000,1) + ' mm</text>' +
                          '<text x="440" y="80" font-size="12" font-weight="700" fill="#0f172a">Thermal Profile</text>' +
                          '<text x="440" y="105" font-size="11" fill="#dc2626">Fluid: 150 °C</text>' +
                          '<text x="440" y="125" font-size="11" fill="#0284c7">Ambient: 20 °C</text>' +
                          '<text x="440" y="145" font-size="11" font-weight="700" fill="#15803d">Loss: ' + f(qPrime,1) + ' W/m</text>';
          diag.textContent = 'Cylindrical resistance: R\'tot = ln(r2/r1)/(2πk) + 1/(2πr2h) = ' + f(R_tot, 2) + ' m·K/W. Critical radius rcrit = k/h = ' + f(rcrit, 1) + ' mm.';
        }
        [sR1, sThick, sK, sH].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 3, unit: 3,
      html: '<header><span class="eyebrow">Unit 3 Laboratory</span><h3>Transient Conduction & Lumped Capacitance Response</h3><p class="lead">Simulate thermal quenching of solid particles: check Biot number validity (Bi < 0.1) and exponential cooling kinetics.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Particle Diameter D <span><output id="v-diam">15.0</output> mm</span></label><input type="range" id="s-diam" min="2.0" max="60.0" step="1.0" value="15.0"></div>' +
              '<div class="control-group"><label>Initial Temp Ti <span><output id="v-ti">350</output> °C</span></label><input type="range" id="s-ti" min="150" max="600" step="10" value="350"></div>' +
              '<div class="control-group"><label>Convection Coeff h <span><output id="v-h3">120</output> W/(m²·K)</span></label><input type="range" id="s-h3" min="20" max="600" step="20" value="120"></div>' +
              '<div class="control-group"><label>Elapsed Time t <span><output id="v-time">25.0</output> s</span></label><input type="range" id="s-time" min="1.0" max="120.0" step="1.0" value="25.0"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Biot Number Bi</div><div class="readout-value" id="r-bi">0.024</div></div>' +
              '<div class="readout-card"><div class="readout-label">Model Validity</div><div class="readout-value" id="r-valid">Lumped Valid (Bi < 0.1)</div></div>' +
              '<div class="readout-card"><div class="readout-label">Time Constant τ</div><div class="readout-value" id="r-tau">32.6 s</div></div>' +
              '<div class="readout-card"><div class="readout-label">Particle Temp T(t)</div><div class="readout-value" id="r-temp">178.5 °C</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-htp3" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-htp3"></p>',
      init: function(el) {
        var sDiam = el.querySelector('#s-diam'), vDiam = el.querySelector('#v-diam');
        var sTi = el.querySelector('#s-ti'), vTi = el.querySelector('#v-ti');
        var sH3 = el.querySelector('#s-h3'), vH3 = el.querySelector('#v-h3');
        var sTime = el.querySelector('#s-time'), vTime = el.querySelector('#v-time');
        var rBi = el.querySelector('#r-bi'), rValid = el.querySelector('#r-valid');
        var rTau = el.querySelector('#r-tau'), rTemp = el.querySelector('#r-temp');
        var svg = el.querySelector('#svg-htp3'), diag = el.querySelector('#diag-htp3');

        var rho = 7800; // kg/m3 steel
        var cp = 500;   // J/(kg K)
        var kSolid = 45; // W/(m K)
        var Tinf = 25;   // C bath

        function update() {
          var D = parseFloat(sDiam.value) / 1000; vDiam.textContent = f(D * 1000, 1);
          var Ti = parseFloat(sTi.value); vTi.textContent = f(Ti, 0);
          var h = parseFloat(sH3.value); vH3.textContent = f(h, 0);
          var t = parseFloat(sTime.value); vTime.textContent = f(t, 1);

          var Lc = D / 6; // Volume / Area for sphere = R/3 = D/6
          var Bi = (h * Lc) / kSolid;
          var tau = (rho * Lc * cp) / Math.max(1, h);
          var theta = Math.exp(-t / Math.max(0.1, tau));
          var T_t = Tinf + (Ti - Tinf) * theta;

          rBi.textContent = f(Bi, 3);
          var isValid = Bi < 0.1;
          rValid.textContent = isValid ? 'Lumped Valid (Bi < 0.1)' : 'Spatial Gradients (Bi >= 0.1)';
          rTau.textContent = f(tau, 1) + ' s';
          rTemp.textContent = f(T_t, 1) + ' °C';

          var pts = [];
          for (var tStep = 0; tStep <= 120; tStep += 2) {
            var x = 80 + (tStep / 120) * 440;
            var th = Math.exp(-tStep / tau);
            var tempAtT = Tinf + (Ti - Tinf) * th;
            var y = 170 - ((tempAtT - Tinf) / (Ti - Tinf + 0.1)) * 130;
            pts.push(f(x,1) + ',' + f(y,1));
          }

          var curX = 80 + (t / 120) * 440;
          var curY = 170 - ((T_t - Tinf) / (Ti - Tinf + 0.1)) * 130;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<polyline points="' + pts.join(' ') + '" fill="none" stroke="#2563eb" stroke-width="3"/>' +
                          '<circle cx="' + curX + '" cy="' + curY + '" r="6" fill="#dc2626"/>' +
                          '<line x1="80" y1="170" x2="520" y2="170" stroke="#94a3b8" stroke-dasharray="4 4"/>' +
                          '<text x="525" y="174" font-size="10" fill="#64748b">T∞=' + Tinf + '°C</text>' +
                          '<text x="80" y="30" font-size="12" font-weight="700" fill="#1e40af">Quenching Cooling Curve: Ti = ' + Ti + '°C</text>' +
                          '<text x="' + (curX + 8) + '" y="' + (curY - 8) + '" font-size="11" font-weight="700" fill="#dc2626">T(' + f(t,0) + 's) = ' + f(T_t,1) + '°C</text>';
          diag.textContent = 'Lumped capacitance kinetics: Biot Bi = ' + f(Bi, 3) + ' (' + (isValid ? 'valid' : 'invalid') + '). Time constant τ = ρ·V·cp/(h·A) = ' + f(tau, 1) + ' s.';
        }
        [sDiam, sTi, sH3, sTime].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 4, unit: 4,
      html: '<header><span class="eyebrow">Unit 4 Laboratory</span><h3>Turbulent Pipe Convection (Dittus-Boelter Correlation)</h3><p class="lead">Calculate turbulent heat transfer coefficient Nu and h in circular process conduits across Reynolds and Prandtl variations.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Reynolds Number Re <span><output id="v-re">45,000</output></span></label><input type="range" id="s-re" min="10000" max="150000" step="5000" value="45000"></div>' +
              '<div class="control-group"><label>Prandtl Number Pr <span><output id="v-pr">4.50</output></span></label><input type="range" id="s-pr" min="0.70" max="12.00" step="0.10" value="4.50"></div>' +
              '<div class="control-group"><label>Pipe Diameter D <span><output id="v-d4">50.0</output> mm</span></label><input type="range" id="s-d4" min="15.0" max="150.0" step="5.0" value="50.0"></div>' +
              '<div class="control-group"><label>Fluid Thermal Cond k <span><output id="v-k4">0.620</output> W/(m·K)</span></label><input type="range" id="s-k4" min="0.100" max="0.800" step="0.020" value="0.620"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Nusselt Number Nu</div><div class="readout-value" id="r-nu">221.4</div></div>' +
              '<div class="readout-card"><div class="readout-label">Heat Transfer Coeff h</div><div class="readout-value" id="r-h4">2,745 W/(m²·K)</div></div>' +
              '<div class="readout-card"><div class="readout-label">Thermal Entry Lth</div><div class="readout-value" id="r-lth">0.50 m</div></div>' +
              '<div class="readout-card"><div class="readout-label">Colburn jH Factor</div><div class="readout-value" id="r-jh">0.0031</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-htp4" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-htp4"></p>',
      init: function(el) {
        var sRe = el.querySelector('#s-re'), vRe = el.querySelector('#v-re');
        var sPr = el.querySelector('#s-pr'), vPr = el.querySelector('#v-pr');
        var sD4 = el.querySelector('#s-d4'), vD4 = el.querySelector('#v-d4');
        var sK4 = el.querySelector('#s-k4'), vK4 = el.querySelector('#v-k4');
        var rNu = el.querySelector('#r-nu'), rH4 = el.querySelector('#r-h4');
        var rLth = el.querySelector('#r-lth'), rJh = el.querySelector('#r-jh');
        var svg = el.querySelector('#svg-htp4'), diag = el.querySelector('#diag-htp4');

        function update() {
          var Re = parseFloat(sRe.value); vRe.textContent = f(Re, 0);
          var Pr = parseFloat(sPr.value); vPr.textContent = f(Pr, 2);
          var D_mm = parseFloat(sD4.value); vD4.textContent = f(D_mm, 1);
          var k = parseFloat(sK4.value); vK4.textContent = f(k, 3);

          var D = D_mm / 1000;
          // Dittus-Boelter heating: Nu = 0.023 * Re^0.8 * Pr^0.4
          var Nu = 0.023 * Math.pow(Re, 0.8) * Math.pow(Pr, 0.4);
          var h = (Nu * k) / D;
          var Lth = 10 * D; // approx 10 diameters entry length
          var jH = (Nu / (Re * Math.pow(Pr, 1/3)));

          rNu.textContent = f(Nu, 1);
          rH4.textContent = f(h, 0) + ' W/(m²·K)';
          rLth.textContent = f(Lth, 2) + ' m';
          rJh.textContent = f(jH, 4);

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="60" y="45" width="480" height="110" fill="#e0f2fe" stroke="#0369a1" stroke-width="2" rx="4"/>' +
                          '<line x1="60" y1="100" x2="540" y2="100" stroke="#0284c7" stroke-dasharray="6 4"/>' +
                          '<path d="M 60 45 Q 220 70 540 70" fill="none" stroke="#ef4444" stroke-width="3"/>' +
                          '<path d="M 60 155 Q 220 130 540 130" fill="none" stroke="#ef4444" stroke-width="3"/>' +
                          '<text x="300" y="30" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Thermal Boundary Layer Growth in Pipe Flow</text>' +
                          '<text x="300" y="105" text-anchor="middle" font-size="12" font-weight="700" fill="#0369a1">h = ' + f(h,0) + ' W/(m²·K) (Nu = ' + f(Nu,1) + ')</text>' +
                          '<text x="300" y="180" text-anchor="middle" font-size="11" fill="#475569">Pipe ID = ' + f(D_mm,0) + ' mm | Re = ' + f(Re,0) + ' | Pr = ' + f(Pr,2) + '</text>';
          diag.textContent = 'Dittus-Boelter calculation: Nu = 0.023·Re^0.8·Pr^0.4 = ' + f(Nu, 1) + '. Convective heat transfer coefficient h = ' + f(h, 0) + ' W/(m²·K).';
        }
        [sRe, sPr, sD4, sK4].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 5, unit: 5,
      html: '<header><span class="eyebrow">Unit 5 Laboratory</span><h3>Radiation Heat Exchange & Radiation Shield Attenuation</h3><p class="lead">Simulate net radiative flux between parallel gray surfaces and calculate thermal radiation reduction with shields.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Hot Surface Temp T1 <span><output id="v-t1">900</output> K</span></label><input type="range" id="s-t1" min="400" max="1500" step="25" value="900"></div>' +
              '<div class="control-group"><label>Cold Surface Temp T2 <span><output id="v-t2">300</output> K</span></label><input type="range" id="s-t2" min="200" max="600" step="25" value="300"></div>' +
              '<div class="control-group"><label>Surface Emissivity ε <span><output id="v-eps">0.70</output></span></label><input type="range" id="s-eps" min="0.10" max="0.95" step="0.05" value="0.70"></div>' +
              '<div class="control-group"><label>Number of Shields N <span><output id="v-shields">1</output></span></label><input type="range" id="s-shields" min="0" max="5" step="1" value="1"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Unshielded Flux q0"</div><div class="readout-value" id="r-q0">20.4 kW/m²</div></div>' +
              '<div class="readout-card"><div class="readout-label">Actual Shielded Flux q"</div><div class="readout-value" id="r-qact">10.2 kW/m²</div></div>' +
              '<div class="readout-card"><div class="readout-label">Radiation Reduction</div><div class="readout-value" id="r-reduc">50.0 %</div></div>' +
              '<div class="readout-card"><div class="readout-label">Equiv hrad</div><div class="readout-value" id="r-hrad">17.0 W/(m²·K)</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-htp5" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-htp5"></p>',
      init: function(el) {
        var sT1 = el.querySelector('#s-t1'), vT1 = el.querySelector('#v-t1');
        var sT2 = el.querySelector('#s-t2'), vT2 = el.querySelector('#v-t2');
        var sEps = el.querySelector('#s-eps'), vEps = el.querySelector('#v-eps');
        var sShields = el.querySelector('#s-shields'), vShields = el.querySelector('#v-shields');
        var rQ0 = el.querySelector('#r-q0'), rQact = el.querySelector('#r-qact');
        var rReduc = el.querySelector('#r-reduc'), rHrad = el.querySelector('#r-hrad');
        var svg = el.querySelector('#svg-htp5'), diag = el.querySelector('#diag-htp5');

        var sigma = 5.670374e-8; // W/(m2 K4)

        function update() {
          var T1 = parseFloat(sT1.value); vT1.textContent = f(T1, 0);
          var T2 = parseFloat(sT2.value); vT2.textContent = f(T2, 0);
          var eps = parseFloat(sEps.value); vEps.textContent = f(eps, 2);
          var N = parseInt(sShields.value, 10); vShields.textContent = N;

          var fEps = 1 / (2 / eps - 1);
          var q0 = fEps * sigma * (Math.pow(T1, 4) - Math.pow(T2, 4)) / 1000; // kW/m2
          var qShield = q0 / (N + 1);
          var reduction = (1 - 1 / (N + 1)) * 100;
          var hRad = (qShield * 1000) / Math.max(1, (T1 - T2));

          rQ0.textContent = f(q0, 1) + ' kW/m²';
          rQact.textContent = f(qShield, 1) + ' kW/m²';
          rReduc.textContent = f(reduction, 1) + ' %';
          rHrad.textContent = f(hRad, 1) + ' W/(m²·K)';

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="80" y="30" width="30" height="140" fill="#ef4444" rx="3"/>' +
                          '<text x="95" y="105" text-anchor="middle" font-size="11" font-weight="700" fill="#ffffff" transform="rotate(-90 95 105)">T1=' + f(T1,0) + 'K</text>' +
                          '<rect x="490" y="30" width="30" height="140" fill="#3b82f6" rx="3"/>' +
                          '<text x="505" y="105" text-anchor="middle" font-size="11" font-weight="700" fill="#ffffff" transform="rotate(-90 505 105)">T2=' + f(T2,0) + 'K</text>';
          
          if (N > 0) {
            var step = (490 - 110) / (N + 1);
            for (var i = 1; i <= N; i++) {
              var sx = 110 + i * step - 5;
              svg.innerHTML += '<rect x="' + sx + '" y="40" width="10" height="120" fill="#94a3b8" rx="2"/>' +
                               '<text x="' + (sx + 5) + '" y="175" text-anchor="middle" font-size="9" fill="#475569">S' + i + '</text>';
            }
          }
          svg.innerHTML += '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Radiative Shield Array (N=' + N + ')</text>' +
                           '<text x="300" y="190" text-anchor="middle" font-size="11" font-weight="700" fill="#15803d">Net Flux q" = ' + f(qShield,1) + ' kW/m² (' + f(reduction,0) + '% attenuated)</text>';
          diag.textContent = 'Radiation exchange: Unshielded flux q0" = ' + f(q0, 1) + ' kW/m². With ' + N + ' radiation shield(s), net flux is reduced to ' + f(qShield, 1) + ' kW/m².';
        }
        [sT1, sT2, sEps, sShields].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 6, unit: 6,
      html: '<header><span class="eyebrow">Unit 6 Laboratory</span><h3>Countercurrent Heat Exchanger Effectiveness-NTU Solver</h3><p class="lead">Simulate heat exchanger rating and sizing using the Effectiveness-NTU method across flow configurations.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Hot Capacity Rate Ch <span><output id="v-ch">25.0</output> kW/K</span></label><input type="range" id="s-ch" min="5.0" max="80.0" step="2.5" value="25.0"></div>' +
              '<div class="control-group"><label>Cold Capacity Rate Cc <span><output id="v-cc">35.0</output> kW/K</span></label><input type="range" id="s-cc" min="5.0" max="80.0" step="2.5" value="35.0"></div>' +
              '<div class="control-group"><label>Heat Exchanger Area A <span><output id="v-area">40.0</output> m²</span></label><input type="range" id="s-area" min="5.0" max="150.0" step="5.0" value="40.0"></div>' +
              '<div class="control-group"><label>Overall Coeff U <span><output id="v-u6">600</output> W/(m²·K)</span></label><input type="range" id="s-u6" min="150" max="1500" step="50" value="600"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Capacity Ratio Cr</div><div class="readout-value" id="r-cr">0.714</div></div>' +
              '<div class="readout-card"><div class="readout-label">Number Transfer Units NTU</div><div class="readout-value" id="r-ntu">0.960</div></div>' +
              '<div class="readout-card"><div class="readout-label">Effectiveness ε</div><div class="readout-value" id="r-eps6">54.8 %</div></div>' +
              '<div class="readout-card"><div class="readout-label">Heat Duty Q̇</div><div class="readout-value" id="r-q6">1,096 kW</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-htp6" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-htp6"></p>',
      init: function(el) {
        var sCh = el.querySelector('#s-ch'), vCh = el.querySelector('#v-ch');
        var sCc = el.querySelector('#s-cc'), vCc = el.querySelector('#v-cc');
        var sArea = el.querySelector('#s-area'), vArea = el.querySelector('#v-area');
        var sU6 = el.querySelector('#s-u6'), vU6 = el.querySelector('#v-u6');
        var rCr = el.querySelector('#r-cr'), rNtu = el.querySelector('#r-ntu');
        var rEps6 = el.querySelector('#r-eps6'), rQ6 = el.querySelector('#r-q6');
        var svg = el.querySelector('#svg-htp6'), diag = el.querySelector('#diag-htp6');

        var Th_in = 120, Tc_in = 40;

        function update() {
          var Ch = parseFloat(sCh.value); vCh.textContent = f(Ch, 1);
          var Cc = parseFloat(sCc.value); vCc.textContent = f(Cc, 1);
          var A = parseFloat(sArea.value); vArea.textContent = f(A, 1);
          var U = parseFloat(sU6.value); vU6.textContent = f(U, 0);

          var Cmin = Math.min(Ch, Cc);
          var Cmax = Math.max(Ch, Cc);
          var Cr = Cmin / Cmax;
          var NTU = (U * A) / (Cmin * 1000);

          // Countercurrent effectiveness:
          var eps = 0;
          if (Cr === 1.0) {
            eps = NTU / (1 + NTU);
          } else {
            var expTerm = Math.exp(-NTU * (1 - Cr));
            eps = (1 - expTerm) / (1 - Cr * expTerm);
          }
          eps = Math.min(0.999, Math.max(0.01, eps));

          var Qmax = Cmin * (Th_in - Tc_in);
          var Q = eps * Qmax;

          rCr.textContent = f(Cr, 3);
          rNtu.textContent = f(NTU, 3);
          rEps6.textContent = f(eps * 100, 1) + ' %';
          rQ6.textContent = f(Q, 0) + ' kW';

          var Th_out = Th_in - Q / Ch;
          var Tc_out = Tc_in + Q / Cc;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="100" y="50" width="400" height="100" fill="#f1f5f9" stroke="#334155" stroke-width="2" rx="6"/>' +
                          '<line x1="80" y1="80" x2="520" y2="80" stroke="#ef4444" stroke-width="4"/>' +
                          '<text x="70" y="85" text-anchor="end" font-size="11" font-weight="700" fill="#dc2626">Th,in ' + Th_in + '°C</text>' +
                          '<text x="530" y="85" text-anchor="start" font-size="11" font-weight="700" fill="#dc2626">Th,out ' + f(Th_out,1) + '°C</text>' +
                          '<line x1="520" y1="120" x2="80" y2="120" stroke="#3b82f6" stroke-width="4"/>' +
                          '<text x="530" y="125" text-anchor="start" font-size="11" font-weight="700" fill="#2563eb">Tc,in ' + Tc_in + '°C</text>' +
                          '<text x="70" y="125" text-anchor="end" font-size="11" font-weight="700" fill="#2563eb">Tc,out ' + f(Tc_out,1) + '°C</text>' +
                          '<text x="300" y="35" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">Countercurrent ε-NTU Rating</text>' +
                          '<text x="300" y="105" text-anchor="middle" font-size="13" font-weight="700" fill="#0369a1">ε = ' + f(eps*100,1) + '% | Q̇ = ' + f(Q,0) + ' kW</text>' +
                          '<text x="300" y="175" text-anchor="middle" font-size="11" fill="#475569">NTU = ' + f(NTU,2) + ' | Cr = ' + f(Cr,2) + ' | Area = ' + f(A,0) + ' m²</text>';
          diag.textContent = 'Effectiveness-NTU method: NTU = UA/Cmin = ' + f(NTU, 3) + '. Heat exchanger thermal effectiveness ε = ' + f(eps * 100, 1) + '%.';
        }
        [sCh, sCc, sArea, sU6].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 7, unit: 7,
      html: '<header><span class="eyebrow">Unit 7 Laboratory</span><h3>Pool Boiling Nukiyama Curve & Critical Heat Flux (CHF)</h3><p class="lead">Simulate boiling regimes from natural convection to nucleate boiling and film boiling under surface superheat.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Surface Superheat ΔTsat <span><output id="v-dtsat">18.0</output> °C</span></label><input type="range" id="s-dtsat" min="2.0" max="150.0" step="1.0" value="18.0"></div>' +
              '<div class="control-group"><label>Operating Pressure <span><output id="v-press7">1.0</output> bar</span></label><input type="range" id="s-press7" min="0.5" max="10.0" step="0.5" value="1.0"></div>' +
              '<div class="control-group"><label>Surface Quality Factor <span><output id="v-csf">1.00</output></span></label><input type="range" id="s-csf" min="0.70" max="1.50" step="0.05" value="1.00"></div>' +
              '<div class="control-group"><label>Liquid Subcooling <span><output id="v-subcool">0.0</output> °C</span></label><input type="range" id="s-subcool" min="0.0" max="25.0" step="1.0" value="0.0"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Boiling Regime</div><div class="readout-value" id="r-regime7">Nucleate Boiling</div></div>' +
              '<div class="readout-card"><div class="readout-label">Boiling Flux q"</div><div class="readout-value" id="r-qflux">452 kW/m²</div></div>' +
              '<div class="readout-card"><div class="readout-label">Critical Heat Flux CHF</div><div class="readout-value" id="r-chf">1,120 kW/m²</div></div>' +
              '<div class="readout-card"><div class="readout-label">CHF Margin</div><div class="readout-value" id="r-chfmar">59.6 %</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-htp7" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-htp7"></p>',
      init: function(el) {
        var sDtsat = el.querySelector('#s-dtsat'), vDtsat = el.querySelector('#v-dtsat');
        var sPress7 = el.querySelector('#s-press7'), vPress7 = el.querySelector('#v-press7');
        var sCsf = el.querySelector('#s-csf'), vCsf = el.querySelector('#v-csf');
        var sSubcool = el.querySelector('#s-subcool'), vSubcool = el.querySelector('#v-subcool');
        var rRegime7 = el.querySelector('#r-regime7'), rQflux = el.querySelector('#r-qflux');
        var rChf = el.querySelector('#r-chf'), rChfmar = el.querySelector('#r-chfmar');
        var svg = el.querySelector('#svg-htp7'), diag = el.querySelector('#diag-htp7');

        function update() {
          var dt = parseFloat(sDtsat.value); vDtsat.textContent = f(dt, 1);
          var P = parseFloat(sPress7.value); vPress7.textContent = f(P, 1);
          var Csf = parseFloat(sCsf.value); vCsf.textContent = f(Csf, 2);
          var sub = parseFloat(sSubcool.value); vSubcool.textContent = f(sub, 1);

          var CHF = 1100 * Math.pow(P, 0.25) * (1 + 0.05 * sub);
          var q = 0;
          var regime = '';

          if (dt < 5) {
            regime = 'Natural Convection';
            q = 1.5 * Math.pow(dt, 1.25);
          } else if (dt <= 30) {
            regime = 'Nucleate Boiling';
            q = (1.5 * Math.pow(5, 1.25)) + 1.2 * Math.pow(dt - 5, 2.7) * Csf;
            q = Math.min(CHF, q);
          } else if (dt <= 80) {
            regime = 'Transition Boiling (Unstable)';
            q = CHF - 15 * (dt - 30);
            q = Math.max(120, q);
          } else {
            regime = 'Stable Film Boiling';
            q = 120 + 2.8 * Math.pow(dt - 80, 1.15);
          }

          var margin = Math.max(0, ((CHF - q) / CHF) * 100);

          rRegime7.textContent = regime;
          rQflux.textContent = f(q, 0) + ' kW/m²';
          rChf.textContent = f(CHF, 0) + ' kW/m²';
          rChfmar.textContent = f(margin, 1) + ' %';

          // Render Nukiyama curve
          var pts = [];
          for (var tStep = 2; tStep <= 150; tStep += 2) {
            var x = 80 + (Math.log10(tStep) / Math.log10(150)) * 440;
            var qVal = 0;
            if (tStep < 5) qVal = 1.5 * Math.pow(tStep, 1.25);
            else if (tStep <= 30) qVal = (1.5 * Math.pow(5, 1.25)) + 1.2 * Math.pow(tStep - 5, 2.7) * Csf;
            else if (tStep <= 80) qVal = CHF - 15 * (tStep - 30);
            else qVal = 120 + 2.8 * Math.pow(tStep - 80, 1.15);
            qVal = Math.min(1400, Math.max(1, qVal));
            var y = 170 - (qVal / 1400) * 130;
            pts.push(f(x,1) + ',' + f(y,1));
          }

          var curX = 80 + (Math.log10(dt) / Math.log10(150)) * 440;
          var curY = 170 - (Math.min(1400, q) / 1400) * 130;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<polyline points="' + pts.join(' ') + '" fill="none" stroke="#2563eb" stroke-width="3"/>' +
                          '<circle cx="' + curX + '" cy="' + curY + '" r="6" fill="#dc2626"/>' +
                          '<line x1="80" y1="' + (170 - (CHF/1400)*130) + '" x2="520" y2="' + (170 - (CHF/1400)*130) + '" stroke="#ef4444" stroke-dasharray="4 4"/>' +
                          '<text x="525" y="' + (174 - (CHF/1400)*130) + '" font-size="10" fill="#dc2626">CHF</text>' +
                          '<text x="80" y="25" font-size="12" font-weight="700" fill="#0f172a">Nukiyama Boiling Curve: ' + regime + '</text>' +
                          '<text x="' + (curX + 8) + '" y="' + (curY - 8) + '" font-size="11" font-weight="700" fill="#dc2626">ΔT=' + f(dt,1) + '°C, q"=' + f(q,0) + 'kW/m²</text>';
          diag.textContent = 'Boiling regime analysis: ΔTsat = ' + f(dt, 1) + ' °C yields ' + regime + '. Flux = ' + f(q, 0) + ' kW/m² (Margin to burnout CHF = ' + f(margin, 1) + '%).';
        }
        [sDtsat, sPress7, sCsf, sSubcool].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 8, unit: 8,
      html: '<header><span class="eyebrow">Unit 8 Laboratory</span><h3>Thermal Pinch Analysis & Minimum Utility Targeting</h3><p class="lead">Optimize plant heat integration: evaluate composite curves, maximum process heat recovery, and minimum hot/cold utility demands.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Min Approach ΔTmin <span><output id="v-dtmin">10.0</output> °C</span></label><input type="range" id="s-dtmin" min="4.0" max="30.0" step="1.0" value="10.0"></div>' +
              '<div class="control-group"><label>Hot Stream Enthalpy <span><output id="v-hoth">8.5</output> MW</span></label><input type="range" id="s-hoth" min="3.0" max="20.0" step="0.5" value="8.5"></div>' +
              '<div class="control-group"><label>Cold Stream Enthalpy <span><output id="v-coldh">10.2</output> MW</span></label><input type="range" id="s-coldh" min="3.0" max="20.0" step="0.5" value="10.2"></div>' +
              '<div class="control-group"><label>Pinch Temperature <span><output id="v-tpinch">95.0</output> °C</span></label><input type="range" id="s-tpinch" min="60.0" max="160.0" step="2.5" value="95.0"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Max Heat Recovery Qrec</div><div class="readout-value" id="r-qrec">7.1 MW</div></div>' +
              '<div class="readout-card"><div class="readout-label">Hot Utility QH,min</div><div class="readout-value" id="r-qhmin">3.1 MW</div></div>' +
              '<div class="readout-card"><div class="readout-label">Cold Utility QC,min</div><div class="readout-value" id="r-qcmin">1.4 MW</div></div>' +
              '<div class="readout-card"><div class="readout-label">Energy Savings</div><div class="readout-value" id="r-esave">69.6 %</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-htp8" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-htp8"></p>',
      init: function(el) {
        var sDtmin = el.querySelector('#s-dtmin'), vDtmin = el.querySelector('#v-dtmin');
        var sHoth = el.querySelector('#s-hoth'), vHoth = el.querySelector('#v-hoth');
        var sColdh = el.querySelector('#s-coldh'), vColdh = el.querySelector('#v-coldh');
        var sTpinch = el.querySelector('#s-tpinch'), vTpinch = el.querySelector('#v-tpinch');
        var rQrec = el.querySelector('#r-qrec'), rQhmin = el.querySelector('#r-qhmin');
        var rQcmin = el.querySelector('#r-qcmin'), rEsave = el.querySelector('#r-esave');
        var svg = el.querySelector('#svg-htp8'), diag = el.querySelector('#diag-htp8');

        function update() {
          var dtMin = parseFloat(sDtmin.value); vDtmin.textContent = f(dtMin, 1);
          var Qh = parseFloat(sHoth.value); vHoth.textContent = f(Qh, 1);
          var Qc = parseFloat(sColdh.value); vColdh.textContent = f(Qc, 1);
          var Tpinch = parseFloat(sTpinch.value); vTpinch.textContent = f(Tpinch, 1);

          // Heat recovery calculation:
          var maxPossible = Math.min(Qh, Qc);
          // Penalty for higher dtMin
          var Qrec = Math.max(1.0, maxPossible - 0.14 * (dtMin - 4));
          var QH_min = Math.max(0.5, Qc - Qrec);
          var QC_min = Math.max(0.5, Qh - Qrec);
          var savings = (Qrec / Math.max(0.1, (Qh + Qc) / 2)) * 100;

          rQrec.textContent = f(Qrec, 1) + ' MW';
          rQhmin.textContent = f(QH_min, 1) + ' MW';
          rQcmin.textContent = f(QC_min, 1) + ' MW';
          rEsave.textContent = f(savings, 1) + ' %';

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="80" y1="50" x2="420" y2="130" stroke="#ef4444" stroke-width="4"/>' +
                          '<text x="75" y="45" font-size="11" font-weight="700" fill="#dc2626">Hot Composite</text>' +
                          '<line x1="160" y1="120" x2="520" y2="175" stroke="#3b82f6" stroke-width="4"/>' +
                          '<text x="525" y="180" font-size="11" font-weight="700" fill="#2563eb">Cold Composite</text>' +
                          '<line x1="280" y1="90" x2="280" y2="140" stroke="#15803d" stroke-dasharray="3 3" stroke-width="2"/>' +
                          '<text x="285" y="115" font-size="11" font-weight="700" fill="#15803d">ΔTmin = ' + f(dtMin,1) + '°C</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">Pinch Analysis: Qrec = ' + f(Qrec,1) + ' MW</text>' +
                          '<text x="300" y="190" text-anchor="middle" font-size="11" fill="#475569">QH,min = ' + f(QH_min,1) + ' MW (Steam) | QC,min = ' + f(QC_min,1) + ' MW (Cooling Water)</text>';
          diag.textContent = 'Pinch analysis targeting: At ΔTmin = ' + f(dtMin, 1) + ' °C, process recovery Qrec = ' + f(Qrec, 1) + ' MW. Minimum hot utility = ' + f(QH_min, 1) + ' MW; cold utility = ' + f(QC_min, 1) + ' MW.';
        }
        [sDtmin, sHoth, sColdh, sTpinch].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    }
  ];
""" + get_engine_footer(8)
    return sim_js

# Generate simulation engines for heat-transfer-in-processes
out_dir = os.path.join(ROOT, 'src', 'subjects', 'chemical-process-engineering', 'heat-transfer-in-processes')
os.makedirs(out_dir, exist_ok=True)
out_file = os.path.join(out_dir, 'heat-transfer-in-processes-sims.js')
with open(out_file, 'w', encoding='utf-8') as f:
    f.write(build_htp_sims())
print(f"Wrote {out_file}")
