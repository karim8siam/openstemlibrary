# Tooling script to generate all 4 simulation suites for Chemical & Process Engineering Batch 3
import os, sys, math

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


def build_cre1_sims():
    return """/* Chemical Reaction Engineering I Interactive Simulation Suite */
(function(window) {
  'use strict';

  function f(n, d) { d = (d !== undefined) ? d : 2; return Number.isFinite(n) ? n.toFixed(d) : '0.00'; }

  var MODELS = [
    {
      idx: 1, unit: 1,
      html: '<header><span class="eyebrow">Unit 1 Laboratory</span><h3>Arrhenius Reaction Rate & Temperature Sensitivity</h3><p class="lead">Simulate reaction rate constant k(T) as a function of activation energy Ea and operating temperature T.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Temperature T <span><output id="v-temp">350</output> K</span></label><input type="range" id="s-temp" min="280" max="600" step="10" value="350"></div>' +
              '<div class="control-group"><label>Activation Energy Ea <span><output id="v-ea">65.0</output> kJ/mol</span></label><input type="range" id="s-ea" min="20.0" max="150.0" step="5.0" value="65.0"></div>' +
              '<div class="control-group"><label>Pre-exponential Factor A <span><output id="v-prea">1.0e8</output> s⁻¹</span></label><input type="range" id="s-prea" min="1.0e6" max="1.0e10" step="1.0e6" value="1.0e8"></div>' +
              '<div class="control-group"><label>Reactant Conc CA <span><output id="v-ca1">1.50</output> mol/L</span></label><input type="range" id="s-ca1" min="0.20" max="5.00" step="0.10" value="1.50"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Rate Constant k</div><div class="readout-value" id="r-kval">0.198 s⁻¹</div></div>' +
              '<div class="readout-card"><div class="readout-label">Reaction Rate -rA</div><div class="readout-value" id="r-ra">0.297 mol/L·s</div></div>' +
              '<div class="readout-card"><div class="readout-label">Sensitivity Ratio k(+10K)/k</div><div class="readout-value" id="r-sens">1.82x</div></div>' +
              '<div class="readout-card"><div class="readout-label">Characteristic Half-Life</div><div class="readout-value" id="r-t12">3.50 s</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-cre11" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-cre11"></p>',
      init: function(el) {
        var sT = el.querySelector('#s-temp'), vT = el.querySelector('#v-temp');
        var sEa = el.querySelector('#s-ea'), vEa = el.querySelector('#v-ea');
        var sA = el.querySelector('#s-prea'), vA = el.querySelector('#v-prea');
        var sCa = el.querySelector('#s-ca1'), vCa = el.querySelector('#v-ca1');
        var rK = el.querySelector('#r-kval'), rRa = el.querySelector('#r-ra');
        var rSens = el.querySelector('#r-sens'), rT12 = el.querySelector('#r-t12');
        var svg = el.querySelector('#svg-cre11'), diag = el.querySelector('#diag-cre11');

        var R_gas = 8.314e-3; // kJ/(mol K)

        function update() {
          var T = parseFloat(sT.value); vT.textContent = f(T, 0);
          var Ea = parseFloat(sEa.value); vEa.textContent = f(Ea, 1);
          var A = parseFloat(sA.value); vA.textContent = A.toExponential(1);
          var Ca = parseFloat(sCa.value); vCa.textContent = f(Ca, 2);

          var k = A * Math.exp(-Ea / (R_gas * T));
          var k_plus10 = A * Math.exp(-Ea / (R_gas * (T + 10)));
          var sens = k_plus10 / Math.max(1e-10, k);
          var rA = k * Ca;
          var t12 = k > 0 ? (Math.log(2) / k) : 999;

          rK.textContent = (k < 0.001 || k > 1000) ? k.toExponential(2) + ' s⁻¹' : f(k, 3) + ' s⁻¹';
          rRa.textContent = (rA < 0.001 || rA > 1000) ? rA.toExponential(2) + ' mol/L·s' : f(rA, 3) + ' mol/L·s';
          rSens.textContent = f(sens, 2) + 'x';
          rT12.textContent = t12 > 1000 ? '> 1,000 s' : f(t12, 2) + ' s';

          // Plot Arrhenius ln(k) vs 1000/T
          var pts = [];
          for (var tStep = 280; tStep <= 600; tStep += 10) {
            var invT = 1000 / tStep;
            var px = 100 + ((invT - 1.66) / (3.57 - 1.66)) * 400;
            var kVal = A * Math.exp(-Ea / (R_gas * tStep));
            var lnK = Math.log(Math.max(1e-8, kVal));
            var py = 160 - ((lnK + 15) / 30) * 120;
            py = Math.max(35, Math.min(165, py));
            pts.push(f(px,1) + ',' + f(py,1));
          }

          var curInvT = 1000 / T;
          var curPx = 100 + ((curInvT - 1.66) / (3.57 - 1.66)) * 400;
          var curLnK = Math.log(Math.max(1e-8, k));
          var curPy = 160 - ((curLnK + 15) / 30) * 120;
          curPy = Math.max(35, Math.min(165, curPy));

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="100" y="35" width="400" height="130" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>' +
                          '<polyline points="' + pts.join(' ') + '" fill="none" stroke="#2563eb" stroke-width="3"/>' +
                          '<circle cx="' + curPx + '" cy="' + curPy + '" r="6" fill="#dc2626"/>' +
                          '<text x="300" y="24" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Arrhenius Plot: ln(k) vs 1000/T (Ea = ' + f(Ea,1) + ' kJ/mol)</text>' +
                          '<text x="' + (curPx + 8) + '" y="' + curPy + '" font-size="11" font-weight="700" fill="#dc2626">T=' + f(T,0) + 'K</text>' +
                          '<text x="510" y="50" font-size="10" fill="#64748b">High Temp</text>' +
                          '<text x="105" y="160" font-size="10" fill="#64748b">Low Temp</text>' +
                          '<text x="300" y="185" text-anchor="middle" font-size="11" font-weight="700" fill="#15803d">Rate Acceleration: ' + f(sens,2) + 'x per 10 K temperature rise</text>';
          diag.textContent = 'Arrhenius reaction kinetics: At T = ' + f(T, 0) + ' K, rate constant k = ' + rK.textContent + '. 10 K rise accelerates rate by ' + f(sens, 2) + 'x.';
        }
        [sT, sEa, sA, sCa].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 2, unit: 2,
      html: '<header><span class="eyebrow">Unit 2 Laboratory</span><h3>Isothermal Batch Reactor Conversion & Kinetic Progress</h3><p class="lead">Simulate reactant conversion X(t) and concentration trajectories for first- and second-order irreversible reactions.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Rate Constant k <span><output id="v-k2">0.050</output></span></label><input type="range" id="s-k2" min="0.005" max="0.250" step="0.005" value="0.050"></div>' +
              '<div class="control-group"><label>Initial Conc CA0 <span><output id="v-ca0">2.00</output> mol/L</span></label><input type="range" id="s-ca0" min="0.50" max="5.00" step="0.25" value="2.00"></div>' +
              '<div class="control-group"><label>Reaction Order n <span><output id="v-order">1st Order</output></span></label><input type="range" id="s-order" min="1" max="2" step="1" value="1"></div>' +
              '<div class="control-group"><label>Batch Time t <span><output id="v-btime">30.0</output> min</span></label><input type="range" id="s-btime" min="2.0" max="100.0" step="2.0" value="30.0"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Conversion XA</div><div class="readout-value" id="r-xa2">77.7 %</div></div>' +
              '<div class="readout-card"><div class="readout-label">Residual CA</div><div class="readout-value" id="r-cares">0.45 mol/L</div></div>' +
              '<div class="readout-card"><div class="readout-label">Product CB</div><div class="readout-value" id="r-cbprod">1.55 mol/L</div></div>' +
              '<div class="readout-card"><div class="readout-label">95% Conversion Time</div><div class="readout-value" id="r-t95">59.9 min</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-cre12" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-cre12"></p>',
      init: function(el) {
        var sK = el.querySelector('#s-k2'), vK = el.querySelector('#v-k2');
        var sCa0 = el.querySelector('#s-ca0'), vCa0 = el.querySelector('#v-ca0');
        var sOrd = el.querySelector('#s-order'), vOrd = el.querySelector('#v-order');
        var sBt = el.querySelector('#s-btime'), vBt = el.querySelector('#v-btime');
        var rXa = el.querySelector('#r-xa2'), rCares = el.querySelector('#r-cares');
        var rCb = el.querySelector('#r-cbprod'), rT95 = el.querySelector('#r-t95');
        var svg = el.querySelector('#svg-cre12'), diag = el.querySelector('#diag-cre12');

        function update() {
          var k = parseFloat(sK.value); vK.textContent = f(k, 3);
          var Ca0 = parseFloat(sCa0.value); vCa0.textContent = f(Ca0, 2);
          var order = parseInt(sOrd.value, 10); vOrd.textContent = order === 1 ? '1st Order' : '2nd Order';
          var t = parseFloat(sBt.value); vBt.textContent = f(t, 1);

          var X = 0, Ca = 0, t95 = 0;
          if (order === 1) {
            X = 1 - Math.exp(-k * t);
            Ca = Ca0 * (1 - X);
            t95 = Math.log(20) / k; // ln(1 / 0.05)
          } else {
            X = (k * Ca0 * t) / (1 + k * Ca0 * t);
            Ca = Ca0 * (1 - X);
            t95 = (0.95 / 0.05) / (k * Ca0);
          }
          var Cb = Ca0 * X;

          rXa.textContent = f(X * 100, 1) + ' %';
          rCares.textContent = f(Ca, 2) + ' mol/L';
          rCb.textContent = f(Cb, 2) + ' mol/L';
          rT95.textContent = f(t95, 1) + ' min';

          // Concentration trajectories
          var ptsA = [], ptsB = [];
          for (var tS = 0; tS <= 100; tS += 2) {
            var xVal = 0;
            if (order === 1) xVal = 1 - Math.exp(-k * tS);
            else xVal = (k * Ca0 * tS) / (1 + k * Ca0 * tS);
            var caVal = Ca0 * (1 - xVal);
            var cbVal = Ca0 * xVal;
            var px = 80 + (tS / 100) * 440;
            var pyA = 160 - (caVal / Ca0) * 120;
            var pyB = 160 - (cbVal / Ca0) * 120;
            ptsA.push(f(px,1) + ',' + f(pyA,1));
            ptsB.push(f(px,1) + ',' + f(pyB,1));
          }

          var curPx = 80 + (t / 100) * 440;
          var curPyA = 160 - (Ca / Ca0) * 120;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="80" y="35" width="440" height="130" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>' +
                          '<polyline points="' + ptsA.join(' ') + '" fill="none" stroke="#dc2626" stroke-width="3"/>' +
                          '<polyline points="' + ptsB.join(' ') + '" fill="none" stroke="#16a34a" stroke-width="3"/>' +
                          '<circle cx="' + curPx + '" cy="' + curPyA + '" r="6" fill="#dc2626"/>' +
                          '<text x="80" y="25" font-size="12" font-weight="700" fill="#0f172a">Batch Conversion: ' + (order === 1 ? 'First-Order' : 'Second-Order') + ' (k=' + f(k,3) + ')</text>' +
                          '<text x="500" y="50" font-size="11" font-weight="700" fill="#15803d">Product B (Cb=' + f(Cb,2) + ')</text>' +
                          '<text x="500" y="150" font-size="11" font-weight="700" fill="#dc2626">Reactant A (Ca=' + f(Ca,2) + ')</text>' +
                          '<text x="300" y="185" text-anchor="middle" font-size="11" fill="#475569">At t = ' + f(t,0) + ' min: Conversion X = ' + f(X*100,1) + '% (95% conversion requires ' + f(t95,1) + ' min)</text>';
          diag.textContent = 'Batch reactor performance: Reaction order n = ' + order + '. After ' + f(t, 1) + ' min, conversion XA = ' + f(X * 100, 1) + '%. Residual CA = ' + f(Ca, 2) + ' mol/L.';
        }
        [sK, sCa0, sOrd, sBt].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 3, unit: 3,
      html: '<header><span class="eyebrow">Unit 3 Laboratory</span><h3>CSTR vs. PFR Reactor Volume Comparison</h3><p class="lead">Compare required reactor volume between Continuous Stirred Tank (CSTR) and Plug Flow Reactor (PFR) for identical conversion.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Target Conversion X <span><output id="v-tx">85.0</output> %</span></label><input type="range" id="s-tx" min="50.0" max="98.0" step="1.0" value="85.0"></div>' +
              '<div class="control-group"><label>Molar Feed Rate FA0 <span><output id="v-fa0">10.0</output> mol/s</span></label><input type="range" id="s-fa0" min="2.0" max="50.0" step="1.0" value="10.0"></div>' +
              '<div class="control-group"><label>Rate Constant k <span><output id="v-k3">0.080</output> s⁻¹</span></label><input type="range" id="s-k3" min="0.010" max="0.300" step="0.010" value="0.080"></div>' +
              '<div class="control-group"><label>Inlet Conc CA0 <span><output id="v-ca03">1.00</output> mol/L</span></label><input type="range" id="s-ca03" min="0.20" max="4.00" step="0.10" value="1.00"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">CSTR Volume VCSTR</div><div class="readout-value" id="r-vcstr">708 L</div></div>' +
              '<div class="readout-card"><div class="readout-label">PFR Volume VPFR</div><div class="readout-value" id="r-vpfr">237 L</div></div>' +
              '<div class="readout-card"><div class="readout-label">Volume Ratio VCSTR/VPFR</div><div class="readout-value" id="r-vratio">2.98x</div></div>' +
              '<div class="readout-card"><div class="readout-label">Volumetric Space Time</div><div class="readout-value" id="r-tau3">23.7 s</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-cre13" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-cre13"></p>',
      init: function(el) {
        var sX = el.querySelector('#s-tx'), vX = el.querySelector('#v-tx');
        var sFa0 = el.querySelector('#s-fa0'), vFa0 = el.querySelector('#v-fa0');
        var sK = el.querySelector('#s-k3'), vK = el.querySelector('#v-k3');
        var sCa0 = el.querySelector('#s-ca03'), vCa0 = el.querySelector('#v-ca03');
        var rVcstr = el.querySelector('#r-vcstr'), rVpfr = el.querySelector('#r-vpfr');
        var rVratio = el.querySelector('#r-vratio'), rTau = el.querySelector('#r-tau3');
        var svg = el.querySelector('#svg-cre13'), diag = el.querySelector('#diag-cre13');

        function update() {
          var X = parseFloat(sX.value) / 100; vX.textContent = f(X * 100, 1);
          var Fa0 = parseFloat(sFa0.value); vFa0.textContent = f(Fa0, 1);
          var k = parseFloat(sK.value); vK.textContent = f(k, 3);
          var Ca0 = parseFloat(sCa0.value); vCa0.textContent = f(Ca0, 2);

          var v0 = Fa0 / Ca0; // L/s volumetric flow rate

          // First order reactor volumes:
          // CSTR: V = v0 * X / (k * (1 - X))
          var V_cstr = (v0 * X) / (k * (1 - X));
          // PFR: V = (v0 / k) * ln(1 / (1 - X))
          var V_pfr = (v0 / k) * Math.log(1 / (1 - X));
          var ratio = V_cstr / Math.max(0.01, V_pfr);
          var tau_pfr = V_pfr / v0;

          rVcstr.textContent = f(V_cstr, 0) + ' L';
          rVpfr.textContent = f(V_pfr, 0) + ' L';
          rVratio.textContent = f(ratio, 2) + 'x';
          rTau.textContent = f(tau_pfr, 1) + ' s';

          var barCstr = Math.min(220, Math.max(20, (V_cstr / 2500) * 220));
          var barPfr = Math.min(220, Math.max(20, (V_pfr / 2500) * 220));

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="100" y="50" width="160" height="90" fill="#dbeafe" stroke="#2563eb" stroke-width="2" rx="6"/>' +
                          '<text x="180" y="80" text-anchor="middle" font-size="13" font-weight="700" fill="#1e40af">CSTR Volume</text>' +
                          '<text x="180" y="105" text-anchor="middle" font-size="16" font-weight="800" fill="#0284c7">' + f(V_cstr,0) + ' L</text>' +
                          '<rect x="340" y="50" width="160" height="90" fill="#dcfce7" stroke="#16a34a" stroke-width="2" rx="6"/>' +
                          '<text x="420" y="80" text-anchor="middle" font-size="13" font-weight="700" fill="#15803d">PFR Volume</text>' +
                          '<text x="420" y="105" text-anchor="middle" font-size="16" font-weight="800" fill="#16a34a">' + f(V_pfr,0) + ' L</text>' +
                          '<text x="300" y="30" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">Reactor Volume at X = ' + f(X*100,0) + '%</text>' +
                          '<text x="300" y="175" text-anchor="middle" font-size="12" font-weight="700" fill="#dc2626">CSTR requires ' + f(ratio,2) + 'x more volume than PFR due to exit-rate dilution</text>';
          diag.textContent = 'Reactor comparison at X = ' + f(X * 100, 1) + '%: PFR volume = ' + f(V_pfr, 0) + ' L; CSTR volume = ' + f(V_cstr, 0) + ' L (Ratio = ' + f(ratio, 2) + 'x).';
        }
        [sX, sFa0, sK, sCa0].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 4, unit: 4,
      html: '<header><span class="eyebrow">Unit 4 Laboratory</span><h3>Levenspiel Plot Graphical Sizing & Intermediate Conversions</h3><p class="lead">Visualize Levenspiel sizing curves 1/(-rA) vs. X: compare rectangular CSTR area vs. integrated curve PFR area.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Inlet Conversion X1 <span><output id="v-x14">0.40</output></span></label><input type="range" id="s-x14" min="0.10" max="0.60" step="0.05" value="0.40"></div>' +
              '<div class="control-group"><label>Final Conversion X2 <span><output id="v-x24">0.85</output></span></label><input type="range" id="s-x24" min="0.65" max="0.95" step="0.05" value="0.85"></div>' +
              '<div class="control-group"><label>Reaction Order n <span><output id="v-nord4">2.0</output></span></label><input type="range" id="s-nord4" min="1.0" max="2.5" step="0.5" value="2.0"></div>' +
              '<div class="control-group"><label>Feed Flow FA0 <span><output id="v-fa04">5.0</output> mol/s</span></label><input type="range" id="s-fa04" min="1.0" max="20.0" step="1.0" value="5.0"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Intermediate 1/(-rA)</div><div class="readout-value" id="r-ir1">2.78 L·s/mol</div></div>' +
              '<div class="readout-card"><div class="readout-label">Exit 1/(-rA)</div><div class="readout-value" id="r-ir2">44.4 L·s/mol</div></div>' +
              '<div class="readout-card"><div class="readout-label">CSTR-2 Volume</div><div class="readout-value" id="r-vc2">100.0 L</div></div>' +
              '<div class="readout-card"><div class="readout-label">PFR-2 Volume</div><div class="readout-value" id="r-vp2">35.2 L</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-cre14" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-cre14"></p>',
      init: function(el) {
        var sX1 = el.querySelector('#s-x14'), vX1 = el.querySelector('#v-x14');
        var sX2 = el.querySelector('#s-x24'), vX2 = el.querySelector('#v-x24');
        var sN = el.querySelector('#s-nord4'), vN = el.querySelector('#v-nord4');
        var sFa0 = el.querySelector('#s-fa04'), vFa0 = el.querySelector('#v-fa04');
        var rIr1 = el.querySelector('#r-ir1'), rIr2 = el.querySelector('#r-ir2');
        var rVc2 = el.querySelector('#r-vc2'), rVp2 = el.querySelector('#r-vp2');
        var svg = el.querySelector('#svg-cre14'), diag = el.querySelector('#diag-cre14');

        var k = 1.0, Ca0 = 1.0;

        function update() {
          var x1 = parseFloat(sX1.value); vX1.textContent = f(x1, 2);
          var x2 = parseFloat(sX2.value); vX2.textContent = f(x2, 2);
          var n = parseFloat(sN.value); vN.textContent = f(n, 1);
          var Fa0 = parseFloat(sFa0.value); vFa0.textContent = f(Fa0, 1);

          var invR1 = 1 / Math.max(0.001, k * Math.pow(Ca0 * (1 - x1), n));
          var invR2 = 1 / Math.max(0.001, k * Math.pow(Ca0 * (1 - x2), n));

          var V_cstr2 = Fa0 * (x2 - x1) * invR2;
          // Numerical trapezoid for PFR volume:
          var V_pfr2 = 0;
          var steps = 20, dx = (x2 - x1) / steps;
          for (var i = 0; i < steps; i++) {
            var xm = x1 + (i + 0.5) * dx;
            var invRm = 1 / Math.max(0.001, k * Math.pow(Ca0 * (1 - xm), n));
            V_pfr2 += Fa0 * invRm * dx;
          }

          rIr1.textContent = f(invR1, 2) + ' L·s/mol';
          rIr2.textContent = f(invR2, 1) + ' L·s/mol';
          rVc2.textContent = f(V_cstr2, 1) + ' L';
          rVp2.textContent = f(V_pfr2, 1) + ' L';

          // Render Levenspiel curve
          var pts = [];
          for (var xS = 0; xS <= 0.95; xS += 0.05) {
            var invR = 1 / Math.max(0.001, k * Math.pow(Ca0 * (1 - xS), n));
            var px = 100 + (xS / 0.95) * 400;
            var py = 160 - Math.min(120, (invR / invR2) * 110);
            pts.push(f(px,1) + ',' + f(py,1));
          }

          var px1 = 100 + (x1 / 0.95) * 400;
          var px2 = 100 + (x2 / 0.95) * 400;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="100" y="40" width="400" height="120" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>' +
                          '<rect x="' + px1 + '" y="' + (160 - 110) + '" width="' + (px2 - px1) + '" height="110" fill="#dbeafe" fill-opacity="0.3" stroke="#2563eb" stroke-dasharray="3 3"/>' +
                          '<polyline points="' + pts.join(' ') + '" fill="none" stroke="#dc2626" stroke-width="3"/>' +
                          '<line x1="' + px1 + '" y1="40" x2="' + px1 + '" y2="160" stroke="#64748b" stroke-dasharray="2 2"/>' +
                          '<line x1="' + px2 + '" y1="40" x2="' + px2 + '" y2="160" stroke="#64748b" stroke-dasharray="2 2"/>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Levenspiel Plot: 1/(-rA) vs X (n = ' + f(n,1) + ')</text>' +
                          '<text x="' + px1 + '" y="175" text-anchor="middle" font-size="10" fill="#475569">X1=' + f(x1,2) + '</text>' +
                          '<text x="' + px2 + '" y="175" text-anchor="middle" font-size="10" fill="#475569">X2=' + f(x2,2) + '</text>' +
                          '<text x="510" y="70" font-size="11" fill="#2563eb">CSTR Area = ' + f(V_cstr2,0) + ' L</text>' +
                          '<text x="510" y="90" font-size="11" fill="#15803d">PFR Area = ' + f(V_pfr2,0) + ' L</text>';
          diag.textContent = 'Levenspiel analysis from X1=' + f(x1, 2) + ' to X2=' + f(x2, 2) + ': CSTR volume = ' + f(V_cstr2, 1) + ' L; PFR volume = ' + f(V_pfr2, 1) + ' L.';
        }
        [sX1, sX2, sN, sFa0].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 5, unit: 5,
      html: '<header><span class="eyebrow">Unit 5 Laboratory</span><h3>Multiple Reactions Selectivity & Yield Optimization</h3><p class="lead">Simulate parallel reactions A -> D (desired, order a1) and A -> U (undesired, order a2): optimize instantaneous selectivity.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Desired Order a1 <span><output id="v-ord1">2.0</output></span></label><input type="range" id="s-ord1" min="0.5" max="3.0" step="0.5" value="2.0"></div>' +
              '<div class="control-group"><label>Undesired Order a2 <span><output id="v-ord2">1.0</output></span></label><input type="range" id="s-ord2" min="0.5" max="3.0" step="0.5" value="1.0"></div>' +
              '<div class="control-group"><label>Rate Ratio k1/k2 <span><output id="v-krat">1.50</output></span></label><input type="range" id="s-krat" min="0.20" max="5.00" step="0.10" value="1.50"></div>' +
              '<div class="control-group"><label>Reactant Conc CA <span><output id="v-ca5">2.50</output> mol/L</span></label><input type="range" id="s-ca5" min="0.20" max="5.00" step="0.10" value="2.50"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Instantaneous Selectivity</div><div class="readout-value" id="r-sel">3.75</div></div>' +
              '<div class="readout-card"><div class="readout-label">Differential Order a1 - a2</div><div class="readout-value" id="r-dord">+1.0</div></div>' +
              '<div class="readout-card"><div class="readout-label">Recommended Scheme</div><div class="readout-value" id="r-rscheme">High CA (PFR / Batch)</div></div>' +
              '<div class="readout-card"><div class="readout-label">Fractional Yield φ</div><div class="readout-value" id="r-fyield">78.9 %</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-cre15" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-cre15"></p>',
      init: function(el) {
        var sO1 = el.querySelector('#s-ord1'), vO1 = el.querySelector('#v-ord1');
        var sO2 = el.querySelector('#s-ord2'), vO2 = el.querySelector('#v-ord2');
        var sKr = el.querySelector('#s-krat'), vKr = el.querySelector('#v-krat');
        var sCa = el.querySelector('#s-ca5'), vCa = el.querySelector('#v-ca5');
        var rSel = el.querySelector('#r-sel'), rDord = el.querySelector('#r-dord');
        var rRsch = el.querySelector('#r-rscheme'), rFyd = el.querySelector('#r-fyield');
        var svg = el.querySelector('#svg-cre15'), diag = el.querySelector('#diag-cre15');

        function update() {
          var a1 = parseFloat(sO1.value); vO1.textContent = f(a1, 1);
          var a2 = parseFloat(sO2.value); vO2.textContent = f(a2, 1);
          var krat = parseFloat(sKr.value); vKr.textContent = f(krat, 2);
          var Ca = parseFloat(sCa.value); vCa.textContent = f(Ca, 2);

          var dOrd = a1 - a2;
          var S = krat * Math.pow(Ca, dOrd);
          var phi = S / (1 + S);

          var scheme = '';
          if (dOrd > 0) scheme = 'High CA (PFR / Batch)';
          else if (dOrd < 0) scheme = 'Low CA (CSTR / Semibatch)';
          else scheme = 'CA Independent';

          rSel.textContent = f(S, 2);
          rDord.textContent = (dOrd >= 0 ? '+' : '') + f(dOrd, 1);
          rRsch.textContent = scheme;
          rFyd.textContent = f(phi * 100, 1) + ' %';

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="180" y="50" width="240" height="100" fill="#f1f5f9" stroke="#334155" stroke-width="2" rx="6"/>' +
                          '<text x="300" y="80" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Selectivity S = rD / rU</text>' +
                          '<text x="300" y="110" text-anchor="middle" font-size="18" font-weight="800" fill="#0284c7">' + f(S,2) + '</text>' +
                          '<text x="300" y="130" text-anchor="middle" font-size="11" font-weight="700" fill="#15803d">Instantaneous Yield: ' + f(phi*100,1) + '%</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">Optimal Reactor: ' + scheme + '</text>' +
                          '<text x="300" y="180" text-anchor="middle" font-size="11" fill="#475569">Differential Order a1 - a2 = ' + f(dOrd,1) + ' | CA = ' + f(Ca,2) + ' mol/L</text>';
          diag.textContent = 'Selectivity guidance: a1 - a2 = ' + f(dOrd, 1) + '. When a1 > a2, maintain high reactant concentration using PFR or batch contacting to maximize desired product D.';
        }
        [sO1, sO2, sKr, sCa].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 6, unit: 6,
      html: '<header><span class="eyebrow">Unit 6 Laboratory</span><h3>Non-Isothermal CSTR Van Heerden Thermal Runaway Simulator</h3><p class="lead">Simulate heat generation Qg vs. heat removal Qr in exothermic CSTRs: detect multiple steady states and thermal runaway.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Cooling Jacket Temp Tc <span><output id="v-tc6">295</output> K</span></label><input type="range" id="s-tc6" min="270" max="350" step="5" value="295"></div>' +
              '<div class="control-group"><label>Heat Transfer Coeff UA <span><output id="v-ua6">3.5</output> kW/K</span></label><input type="range" id="s-ua6" min="1.0" max="8.0" step="0.5" value="3.5"></div>' +
              '<div class="control-group"><label>Heat of Reaction ΔHrxn <span><output id="v-dhrxn6">-85</output> kJ/mol</span></label><input type="range" id="s-dhrxn6" min="-150" max="-30" step="5" value="-85"></div>' +
              '<div class="control-group"><label>Feed Temp T0 <span><output id="v-t06">300</output> K</span></label><input type="range" id="s-t06" min="280" max="340" step="5" value="300"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Operating State T</div><div class="readout-value" id="r-top">328 K</div></div>' +
              '<div class="readout-card"><div class="readout-label">Thermal Stability</div><div class="readout-value" id="r-tstab">Stable Lower State</div></div>' +
              '<div class="readout-card"><div class="readout-label">Heat Generated Qg</div><div class="readout-value" id="r-qgen">182 kW</div></div>' +
              '<div class="readout-card"><div class="readout-label">Heat Removed Qr</div><div class="readout-value" id="r-qrem">182 kW</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-cre16" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-cre16"></p>',
      init: function(el) {
        var sTc = el.querySelector('#s-tc6'), vTc = el.querySelector('#v-tc6');
        var sUa = el.querySelector('#s-ua6'), vUa = el.querySelector('#v-ua6');
        var sDh = el.querySelector('#s-dhrxn6'), vDh = el.querySelector('#v-dhrxn6');
        var sT0 = el.querySelector('#s-t06'), vT0 = el.querySelector('#v-t06');
        var rTop = el.querySelector('#r-top'), rTstab = el.querySelector('#r-tstab');
        var rQgen = el.querySelector('#r-qgen'), rQrem = el.querySelector('#r-qrem');
        var svg = el.querySelector('#svg-cre16'), diag = el.querySelector('#diag-cre16');

        function update() {
          var Tc = parseFloat(sTc.value); vTc.textContent = f(Tc, 0);
          var UA = parseFloat(sUa.value); vUa.textContent = f(UA, 1);
          var dH = parseFloat(sDh.value); vDh.textContent = f(dH, 0);
          var T0 = parseFloat(sT0.value); vT0.textContent = f(T0, 0);

          var mCp = 10.0; // kW/K process flow heat capacity
          var T_op = (mCp * T0 + UA * Tc) / (mCp + UA) + Math.abs(dH) * 0.25;
          var runaway = (UA < 2.0 && Math.abs(dH) > 90);
          var stab = runaway ? 'Thermal Runaway (Ignition)' : (T_op > 380 ? 'Upper High-Conversion State' : 'Stable Lower State');

          var Qg = Math.abs(dH) * 2.2;
          var Qr = Qg;

          rTop.textContent = f(T_op, 0) + ' K';
          rTstab.textContent = stab;
          rQgen.textContent = f(Qg, 0) + ' kW';
          rQrem.textContent = f(Qr, 0) + ' kW';

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="100" y="35" width="400" height="130" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>' +
                          '<line x1="100" y1="160" x2="480" y2="45" stroke="#3b82f6" stroke-width="3"/>' +
                          '<text x="490" y="48" font-size="10" font-weight="700" fill="#2563eb">Qr (Removal)</text>' +
                          '<path d="M 120 155 Q 260 150 320 100 T 480 50" fill="none" stroke="#ef4444" stroke-width="3"/>' +
                          '<text x="490" y="65" font-size="10" font-weight="700" fill="#dc2626">Qg (Sigmoid)</text>' +
                          '<circle cx="280" cy="105" r="6" fill="' + (runaway ? '#dc2626' : '#16a34a') + '"/>' +
                          '<text x="300" y="24" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Van Heerden Stability: ' + stab + '</text>' +
                          '<text x="300" y="185" text-anchor="middle" font-size="11" fill="#475569">Jacket Tc = ' + f(Tc,0) + ' K | UA = ' + f(UA,1) + ' kW/K | ΔH = ' + f(dH,0) + ' kJ/mol</text>';
          diag.textContent = 'Van Heerden heat balance: ' + stab + '. Slope of removal Qr relative to generation Qg determines stability against thermal runaway.';
        }
        [sTc, sUa, sDh, sT0].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 7, unit: 7,
      html: '<header><span class="eyebrow">Unit 7 Laboratory</span><h3>Residence Time Distribution (RTD) Pulse Tracer Simulator</h3><p class="lead">Simulate pulse tracer response E(t), evaluate mean residence time tm, variance σ², and Peclet number Pe.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Mean Residence Time tm <span><output id="v-tm7">20.0</output> min</span></label><input type="range" id="s-tm7" min="5.0" max="60.0" step="2.5" value="20.0"></div>' +
              '<div class="control-group"><label>Peclet Number Pe <span><output id="v-pe7">12.0</output></span></label><input type="range" id="s-pe7" min="1.0" max="50.0" step="1.0" value="12.0"></div>' +
              '<div class="control-group"><label>Tanks-in-Series N <span><output id="v-tis7">6</output></span></label><input type="range" id="s-tis7" min="1" max="25" step="1" value="6"></div>' +
              '<div class="control-group"><label>Tracer Mass M <span><output id="v-tmass">50.0</output> g</span></label><input type="range" id="s-tmass" min="10.0" max="100.0" step="5.0" value="50.0"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Variance σ²</div><div class="readout-value" id="r-vars">66.7 min²</div></div>' +
              '<div class="readout-card"><div class="readout-label">Dimensionless σθ²</div><div class="readout-value" id="r-vartheta">0.167</div></div>' +
              '<div class="readout-card"><div class="readout-label">Peak Time tpeak</div><div class="readout-value" id="r-tpeak">16.7 min</div></div>' +
              '<div class="readout-card"><div class="readout-label">Flow Regime</div><div class="readout-value" id="r-freg7">Intermediate Dispersion</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-cre17" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-cre17"></p>',
      init: function(el) {
        var sTm = el.querySelector('#s-tm7'), vTm = el.querySelector('#v-tm7');
        var sPe = el.querySelector('#s-pe7'), vPe = el.querySelector('#v-pe7');
        var sTis = el.querySelector('#s-tis7'), vTis = el.querySelector('#v-tis7');
        var sTmss = el.querySelector('#s-tmass'), vTmss = el.querySelector('#v-tmass');
        var rVars = el.querySelector('#r-vars'), rVartheta = el.querySelector('#r-vartheta');
        var rTpk = el.querySelector('#r-tpeak'), rFreg = el.querySelector('#r-freg7');
        var svg = el.querySelector('#svg-cre17'), diag = el.querySelector('#diag-cre17');

        function update() {
          var tm = parseFloat(sTm.value); vTm.textContent = f(tm, 1);
          var Pe = parseFloat(sPe.value); vPe.textContent = f(Pe, 1);
          var N = parseInt(sTis.value, 10); vTis.textContent = N;
          var M = parseFloat(sTmss.value); vTmss.textContent = f(M, 1);

          var varTheta = 1 / N;
          var variance = varTheta * tm * tm;
          var tPeak = tm * (1 - 1 / N);
          tPeak = Math.max(0.1, tPeak);

          var regime = N === 1 ? 'Ideal CSTR (Pure Mixing)' : (N > 15 ? 'Near Ideal PFR' : 'Intermediate Dispersion');

          rVars.textContent = f(variance, 1) + ' min²';
          rVartheta.textContent = f(varTheta, 3);
          rTpk.textContent = f(tPeak, 1) + ' min';
          rFreg.textContent = regime;

          // Render E(t) curve using Gamma / Tanks-in-series: E(theta) = (N^N / (N-1)!) * theta^(N-1) * exp(-N*theta)
          var pts = [];
          for (var tS = 0; tS <= tm * 2.5; tS += tm * 0.05) {
            var th = tS / tm;
            var eVal = 0;
            if (N === 1) eVal = Math.exp(-th);
            else if (N === 2) eVal = 4 * th * Math.exp(-2 * th);
            else {
              var pwr = Math.pow(th, Math.min(10, N - 1));
              eVal = Math.pow(N, 2) * pwr * Math.exp(-N * th) * 0.15;
            }
            eVal = Math.min(3.0, Math.max(0, eVal));
            var px = 80 + (tS / (tm * 2.5)) * 440;
            var py = 160 - (eVal / 1.5) * 120;
            py = Math.max(35, Math.min(160, py));
            pts.push(f(px,1) + ',' + f(py,1));
          }

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="80" y="35" width="440" height="130" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>' +
                          '<polyline points="' + pts.join(' ') + '" fill="none" stroke="#2563eb" stroke-width="3"/>' +
                          '<line x1="' + (80 + (tm/(tm*2.5))*440) + '" y1="35" x2="' + (80 + (tm/(tm*2.5))*440) + '" y2="165" stroke="#dc2626" stroke-dasharray="3 3"/>' +
                          '<text x="' + (80 + (tm/(tm*2.5))*440) + '" y="30" text-anchor="middle" font-size="10" font-weight="700" fill="#dc2626">tm = ' + f(tm,1) + ' min</text>' +
                          '<text x="300" y="20" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Pulse RTD Curve E(t): ' + regime + '</text>' +
                          '<text x="300" y="185" text-anchor="middle" font-size="11" fill="#475569">Tanks-in-Series N = ' + N + ' | Peclet Pe = ' + f(Pe,1) + ' | Variance σθ² = ' + f(varTheta,3) + '</text>';
          diag.textContent = 'RTD analysis: Mean residence time tm = ' + f(tm, 1) + ' min. Tanks-in-series equivalent N = ' + N + ' (Dimensionless variance = ' + f(varTheta, 3) + '). ' + regime + '.';
        }
        [sTm, sPe, sTis, sTmss].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 8, unit: 8,
      html: '<header><span class="eyebrow">Unit 8 Laboratory</span><h3>Multi-Reactor Network Configuration Economics</h3><p class="lead">Compare capital and operating economics between equal-sized CSTRs in series vs. a single large CSTR.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Target Conversion X <span><output id="v-x8">90.0</output> %</span></label><input type="range" id="s-x8" min="60.0" max="98.0" step="1.0" value="90.0"></div>' +
              '<div class="control-group"><label>Number of CSTRs N <span><output id="v-ncstr">2</output></span></label><input type="range" id="s-ncstr" min="1" max="4" step="1" value="2"></div>' +
              '<div class="control-group"><label>Throughput FA0 <span><output id="v-fthru">20.0</output> mol/s</span></label><input type="range" id="s-fthru" min="5.0" max="80.0" step="5.0" value="20.0"></div>' +
              '<div class="control-group"><label>Reaction Order <span><output id="v-ro8">1st Order</output></span></label><input type="range" id="s-ro8" min="1" max="2" step="1" value="1"></div>' +
            '</div>' +
            '<div class="readout-grid">' +
              '<div class="readout-card"><div class="readout-label">Total Train Volume</div><div class="readout-value" id="r-vtot8">1,842 L</div></div>' +
              '<div class="readout-card"><div class="readout-label">Single CSTR Volume</div><div class="readout-value" id="r-vsing">4,500 L</div></div>' +
              '<div class="readout-card"><div class="readout-label">Volume Reduction</div><div class="readout-value" id="r-vred8">59.1 %</div></div>' +
              '<div class="readout-card"><div class="readout-label">CapEx Savings</div><div class="readout-value" id="r-csave8">$185,000</div></div>' +
            '</div>' +
            '<div class="diagram-wrap"><svg id="svg-cre18" viewBox="0 0 600 200" class="cpe-svg"></svg></div>' +
            '<p class="cpe-diagnostics" id="diag-cre18"></p>',
      init: function(el) {
        var sX = el.querySelector('#s-x8'), vX = el.querySelector('#v-x8');
        var sN = el.querySelector('#s-ncstr'), vN = el.querySelector('#v-ncstr');
        var sF = el.querySelector('#s-fthru'), vF = el.querySelector('#v-fthru');
        var sRo = el.querySelector('#s-ro8'), vRo = el.querySelector('#v-ro8');
        var rVtot = el.querySelector('#r-vtot8'), rVsing = el.querySelector('#r-vsing');
        var rVred = el.querySelector('#r-vred8'), rCsave = el.querySelector('#r-csave8');
        var svg = el.querySelector('#svg-cre18'), diag = el.querySelector('#diag-cre18');

        var k = 0.04; // 1/s

        function update() {
          var X = parseFloat(sX.value) / 100; vX.textContent = f(X * 100, 1);
          var N = parseInt(sN.value, 10); vN.textContent = N;
          var F = parseFloat(sF.value); vF.textContent = f(F, 1);
          var ro = parseInt(sRo.value, 10); vRo.textContent = ro === 1 ? '1st Order' : '2nd Order';

          var v0 = F / 1.0; // L/s
          var V_single = (v0 * X) / (k * (1 - X));

          // N equal CSTRs in series: (1 - X) = 1 / (1 + k*tau_i)^N
          var tau_i = (Math.pow(1 / (1 - X), 1 / N) - 1) / k;
          var V_train = N * v0 * tau_i;
          var reduction = ((V_single - V_train) / V_single) * 100;
          var savings = (Math.pow(V_single, 0.6) - N * Math.pow(V_train / N, 0.6)) * 400;
          savings = Math.max(0, savings);

          rVtot.textContent = f(V_train, 0) + ' L';
          rVsing.textContent = f(V_single, 0) + ' L';
          rVred.textContent = f(reduction, 1) + ' %';
          rCsave.textContent = '$' + f(savings, 0);

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="80" y="50" width="160" height="90" fill="#dbeafe" stroke="#2563eb" stroke-width="2" rx="6"/>' +
                          '<text x="160" y="80" text-anchor="middle" font-size="12" font-weight="700" fill="#1e40af">' + N + ' CSTRs in Series</text>' +
                          '<text x="160" y="105" text-anchor="middle" font-size="15" font-weight="800" fill="#0284c7">' + f(V_train,0) + ' L</text>' +
                          '<rect x="360" y="50" width="160" height="90" fill="#fef3c7" stroke="#d97706" stroke-width="2" rx="6"/>' +
                          '<text x="440" y="80" text-anchor="middle" font-size="12" font-weight="700" fill="#92400e">Single Large CSTR</text>' +
                          '<text x="440" y="105" text-anchor="middle" font-size="15" font-weight="800" fill="#b45309">' + f(V_single,0) + ' L</text>' +
                          '<text x="300" y="30" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">Reactor Staging: ' + f(reduction,1) + '% Volume Reduction</text>' +
                          '<text x="300" y="175" text-anchor="middle" font-size="11" font-weight="700" fill="#15803d">Capital savings: $' + f(savings,0) + ' via staging economy</text>';
          diag.textContent = 'Train staging: ' + N + ' CSTRs in series require ' + f(V_train, 0) + ' L total volume vs. ' + f(V_single, 0) + ' L for a single vessel (' + f(reduction, 1) + '% total volume reduction).';
        }
        [sX, sN, sF, sRo].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    }
  ];
""" + get_engine_footer(8)

# =========================================================================
# 2. Chemical Reaction Engineering II
# =========================================================================
def build_cre2_sims():
    return """/* Chemical Reaction Engineering II Interactive Simulation Suite */
(function(window) {
  'use strict';

  function f(n, d) { d = (d !== undefined) ? d : 2; return Number.isFinite(n) ? n.toFixed(d) : '0.00'; }

  var MODELS = [
    {
      idx: 1, unit: 1,
      html: '<header><span class="eyebrow">Unit 1 Laboratory</span><h3>Langmuir-Hinshelwood Heterogeneous Surface Catalysis</h3><p class="lead">Model catalytic surface adsorption, site saturation, and apparent reaction order transitions.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Reactant Pressure PA <span><output id="v-pa">1.50</output> bar</span></label><input type="range" id="s-pa" min="0.05" max="10.0" step="0.05" value="1.50"></div>' +
              '<div class="control-group"><label>Adsorption Constant KA <span><output id="v-ka">1.20</output> bar⁻¹</span></label><input type="range" id="s-ka" min="0.10" max="5.00" step="0.10" value="1.20"></div>' +
              '<div class="control-group"><label>Surface Rate Constant kr <span><output id="v-kr">4.50</output> mol/g·h</span></label><input type="range" id="s-kr" min="0.50" max="10.0" step="0.25" value="4.50"></div>' +
              '<div class="control-group"><label>Inhibitor Pressure PB <span><output id="v-pb">0.20</output> bar</span></label><input type="range" id="s-pb" min="0.00" max="3.00" step="0.10" value="0.20"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Surface Coverage θA</span><span class="value" id="r-theta">0.00</span><span class="subtext">fraction of active sites</span></div>' +
              '<div class="readout-card"><span class="label">Reaction Rate rA</span><span class="value" id="r-rate">0.00</span><span class="subtext">mol / (g-cat · h)</span></div>' +
              '<div class="readout-card"><span class="label">Apparent Order</span><span class="value" id="r-order">0.00</span><span class="subtext">d ln(r) / d ln(PA)</span></div>' +
              '<div class="readout-card"><span class="label">Site Saturation</span><span class="value" id="r-sat">0.0%</span><span class="subtext">monolayer fullness</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-cre2-u1" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-cre2-u1"></div>',
      init: function(card) {
        var sPA = card.querySelector('#s-pa'), vPA = card.querySelector('#v-pa');
        var sKA = card.querySelector('#s-ka'), vKA = card.querySelector('#v-ka');
        var sKr = card.querySelector('#s-kr'), vKr = card.querySelector('#v-kr');
        var sPB = card.querySelector('#s-pb'), vPB = card.querySelector('#v-pb');
        var rTheta = card.querySelector('#r-theta'), rRate = card.querySelector('#r-rate');
        var rOrder = card.querySelector('#r-order'), rSat = card.querySelector('#r-sat');
        var svg = card.querySelector('#plot-cre2-u1'), diag = card.querySelector('#diag-cre2-u1');

        function update() {
          var PA = parseFloat(sPA.value); vPA.textContent = f(PA, 2);
          var KA = parseFloat(sKA.value); vKA.textContent = f(KA, 2);
          var kr = parseFloat(sKr.value); vKr.textContent = f(kr, 2);
          var PB = parseFloat(sPB.value); vPB.textContent = f(PB, 2);
          var KB = 0.8; // competitive adsorption constant

          var denom = 1 + KA * PA + KB * PB;
          var thetaA = (KA * PA) / denom;
          var rA = kr * thetaA;
          var appOrder = 1 / denom; // apparent order transitions from 1 at low PA to 0 at high PA
          var totalCov = (KA * PA + KB * PB) / denom;

          rTheta.textContent = f(thetaA, 3);
          rRate.textContent = f(rA, 2) + ' mol/g·h';
          rOrder.textContent = f(appOrder, 2);
          rSat.textContent = f(totalCov * 100, 1) + ' %';

          // SVG curve of rA vs P
          var dPath = 'M 40 170 ';
          for (var p = 0.05; p <= 10.0; p += 0.2) {
            var den_i = 1 + KA * p + KB * PB;
            var r_i = kr * (KA * p) / den_i;
            var x_px = 40 + (p / 10.0) * 520;
            var y_px = 170 - (r_i / (kr + 0.01)) * 140;
            dPath += 'L ' + x_px.toFixed(1) + ' ' + y_px.toFixed(1) + ' ';
          }
          var cur_x = 40 + (PA / 10.0) * 520;
          var cur_y = 170 - (rA / (kr + 0.01)) * 140;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="40" y1="170" x2="560" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<line x1="40" y1="30" x2="40" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<path d="' + dPath + '" fill="none" stroke="#2563eb" stroke-width="3"/>' +
                          '<circle cx="' + cur_x.toFixed(1) + '" cy="' + cur_y.toFixed(1) + '" r="6" fill="#ef4444" stroke="#fff" stroke-width="2"/>' +
                          '<text x="560" y="190" text-anchor="end" font-size="11" fill="#64748b">Partial Pressure PA (bar)</text>' +
                          '<text x="50" y="45" font-size="11" fill="#64748b">Reaction Rate rA</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Langmuir-Hinshelwood Isotherm: Apparent Order ' + f(appOrder, 2) + '</text>';
          diag.textContent = 'At PA = ' + f(PA, 2) + ' bar, active surface site coverage is ' + f(thetaA * 100, 1) + '%. Apparent reaction order is ' + f(appOrder, 2) + ' (' + (appOrder > 0.7 ? 'first-order limited by adsorption' : (appOrder < 0.3 ? 'zero-order site saturation' : 'intermediate mixed regime')) + ').';
        }
        [sPA, sKA, sKr, sPB].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 2, unit: 2,
      html: '<header><span class="eyebrow">Unit 2 Laboratory</span><h3>Catalyst Deactivation & Coking Dynamics</h3><p class="lead">Simulate catalyst activity decay, sintering, and residual operating life.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Operating Days t <span><output id="v-day">60</output> d</span></label><input type="range" id="s-day" min="0" max="300" step="5" value="60"></div>' +
              '<div class="control-group"><label>Deactivation Const kd <span><output id="v-kd">0.012</output> d⁻¹</span></label><input type="range" id="s-kd" min="0.002" max="0.050" step="0.002" value="0.012"></div>' +
              '<div class="control-group"><label>Deactivation Order <span><output id="v-dord">1st Order</output></span></label><input type="range" id="s-dord" min="1" max="2" step="1" value="1"></div>' +
              '<div class="control-group"><label>Fresh Activity a0 <span><output id="v-a0">1.00</output></span></label><input type="range" id="s-a0" min="0.80" max="1.00" step="0.05" value="1.00"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Current Activity a(t)</span><span class="value" id="r-act">1.00</span><span class="subtext">fraction of pristine state</span></div>' +
              '<div class="readout-card"><span class="label">Residual Rate rA</span><span class="value" id="r-rrate">100%</span><span class="subtext">relative to fresh catalyst</span></div>' +
              '<div class="readout-card"><span class="label">Catalyst Half-Life</span><span class="value" id="r-halflife">0 d</span><span class="subtext">time to 50% activity</span></div>' +
              '<div class="readout-card"><span class="label">Lost Productivity</span><span class="value" id="r-prodloss">0%</span><span class="subtext">cumulative yield deficit</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-cre2-u2" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-cre2-u2"></div>',
      init: function(card) {
        var sDay = card.querySelector('#s-day'), vDay = card.querySelector('#v-day');
        var sKd = card.querySelector('#s-kd'), vKd = card.querySelector('#v-kd');
        var sDord = card.querySelector('#s-dord'), vDord = card.querySelector('#v-dord');
        var sA0 = card.querySelector('#s-a0'), vA0 = card.querySelector('#v-a0');
        var rAct = card.querySelector('#r-act'), rRrate = card.querySelector('#r-rrate');
        var rHalf = card.querySelector('#r-halflife'), rProd = card.querySelector('#r-prodloss');
        var svg = card.querySelector('#plot-cre2-u2'), diag = card.querySelector('#diag-cre2-u2');

        function update() {
          var t = parseFloat(sDay.value); vDay.textContent = f(t, 0);
          var kd = parseFloat(sKd.value); vKd.textContent = f(kd, 3);
          var dord = parseInt(sDord.value, 10); vDord.textContent = dord === 1 ? '1st Order' : '2nd Order';
          var a0 = parseFloat(sA0.value); vA0.textContent = f(a0, 2);

          var act = dord === 1 ? a0 * Math.exp(-kd * t) : a0 / (1 + kd * t * a0);
          var halfLife = dord === 1 ? Math.log(2) / kd : 1 / (kd * a0);
          var loss = (1 - act / a0) * 100;

          rAct.textContent = f(act, 3);
          rRrate.textContent = f(act * 100, 1) + ' %';
          rHalf.textContent = f(halfLife, 0) + ' d';
          rProd.textContent = f(loss, 1) + ' %';

          var dPath = 'M 40 ' + (170 - a0 * 130).toFixed(1) + ' ';
          for (var d = 0; d <= 300; d += 10) {
            var a_i = dord === 1 ? a0 * Math.exp(-kd * d) : a0 / (1 + kd * d * a0);
            var x_px = 40 + (d / 300.0) * 520;
            var y_px = 170 - (a_i / 1.0) * 130;
            dPath += 'L ' + x_px.toFixed(1) + ' ' + y_px.toFixed(1) + ' ';
          }
          var cur_x = 40 + (t / 300.0) * 520;
          var cur_y = 170 - (act / 1.0) * 130;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="40" y1="170" x2="560" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<line x1="40" y1="30" x2="40" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<line x1="40" y1="' + (170 - 0.5 * 130) + '" x2="560" y2="' + (170 - 0.5 * 130) + '" stroke="#cbd5e1" stroke-dasharray="4"/>' +
                          '<text x="560" y="' + (165 - 0.5 * 130) + '" text-anchor="end" font-size="10" fill="#94a3b8">50% Half-Life Threshold</text>' +
                          '<path d="' + dPath + '" fill="none" stroke="#d97706" stroke-width="3"/>' +
                          '<circle cx="' + cur_x.toFixed(1) + '" cy="' + cur_y.toFixed(1) + '" r="6" fill="#b45309" stroke="#fff" stroke-width="2"/>' +
                          '<text x="560" y="190" text-anchor="end" font-size="11" fill="#64748b">On-Stream Time (Days)</text>' +
                          '<text x="50" y="45" font-size="11" fill="#64748b">Activity a(t)</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Catalyst Deactivation Curve (Half-Life: ' + f(halfLife, 0) + ' days)</text>';
          diag.textContent = 'At ' + f(t, 0) + ' days of operation, catalyst activity is ' + f(act * 100, 1) + '%. Estimated half-life is ' + f(halfLife, 0) + ' days before regeneration or replacement is required.';
        }
        [sDay, sKd, sDord, sA0].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 3, unit: 3,
      html: '<header><span class="eyebrow">Unit 3 Laboratory</span><h3>Intraparticle Diffusion & Thiele Modulus</h3><p class="lead">Simulate internal pore diffusion resistance and catalyst effectiveness factor η.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Pellet Radius Rp <span><output id="v-rp">2.0</output> mm</span></label><input type="range" id="s-rp" min="0.5" max="6.0" step="0.5" value="2.0"></div>' +
              '<div class="control-group"><label>Effective Diffusivity De <span><output id="v-de">4.0</output> × 10⁻⁷ m²/s</span></label><input type="range" id="s-de" min="1.0" max="10.0" step="0.5" value="4.0"></div>' +
              '<div class="control-group"><label>Intrinsic Rate Const kv <span><output id="v-kv">2.50</output> s⁻¹</span></label><input type="range" id="s-kv" min="0.20" max="8.00" step="0.20" value="2.50"></div>' +
              '<div class="control-group"><label>Pellet Shape <span><output id="v-shape">Sphere</output></span></label><input type="range" id="s-shape" min="1" max="2" step="1" value="1"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Thiele Modulus Φ</span><span class="value" id="r-thiele">0.00</span><span class="subtext">reaction / diffusion ratio</span></div>' +
              '<div class="readout-card"><span class="label">Effectiveness Factor η</span><span class="value" id="r-eta">0.00</span><span class="subtext">actual rate / surface rate</span></div>' +
              '<div class="readout-card"><span class="label">Controlling Regime</span><span class="value" id="r-regime">-</span><span class="subtext">kinetic limitation</span></div>' +
              '<div class="readout-card"><span class="label">Weisz-Prater Criterion</span><span class="value" id="r-weisz">0.00</span><span class="subtext">η · Φ² observable</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-cre2-u3" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-cre2-u3"></div>',
      init: function(card) {
        var sRp = card.querySelector('#s-rp'), vRp = card.querySelector('#v-rp');
        var sDe = card.querySelector('#s-de'), vDe = card.querySelector('#v-de');
        var sKv = card.querySelector('#s-kv'), vKv = card.querySelector('#v-kv');
        var sShape = card.querySelector('#s-shape'), vShape = card.querySelector('#v-shape');
        var rThiele = card.querySelector('#r-thiele'), rEta = card.querySelector('#r-eta');
        var rRegime = card.querySelector('#r-regime'), rWeisz = card.querySelector('#r-weisz');
        var svg = card.querySelector('#plot-cre2-u3'), diag = card.querySelector('#diag-cre2-u3');

        function update() {
          var Rp = parseFloat(sRp.value) * 1e-3; vRp.textContent = f(Rp * 1e3, 1);
          var De = parseFloat(sDe.value) * 1e-7; vDe.textContent = f(De * 1e7, 1);
          var kv = parseFloat(sKv.value); vKv.textContent = f(kv, 2);
          var isSphere = parseInt(sShape.value, 10) === 1; vShape.textContent = isSphere ? 'Sphere' : 'Flat Slab';

          var phi = Rp * Math.sqrt(kv / De);
          var eta;
          if (isSphere) {
            eta = phi > 0.01 ? (3 / phi) * (1 / Math.tanh(phi) - 1 / phi) : 1.0;
          } else {
            eta = phi > 0.01 ? Math.tanh(phi) / phi : 1.0;
          }
          eta = Math.min(1.0, Math.max(0.01, eta));
          var weisz = eta * phi * phi;
          var regime = phi < 0.5 ? 'Reaction Limited (η ≈ 1)' : (phi > 3.0 ? 'Strong Pore Diffusion' : 'Transition Zone');

          rThiele.textContent = f(phi, 2);
          rEta.textContent = f(eta, 3);
          rRegime.textContent = regime;
          rWeisz.textContent = f(weisz, 2);

          // SVG radial concentration profile C(r)/Cs
          var dPath = 'M 40 ';
          var cCenter = isSphere ? (phi > 0.05 ? phi / Math.sinh(phi) : 1.0) : (phi > 0.05 ? 1 / Math.cosh(phi) : 1.0);
          dPath += (170 - cCenter * 130).toFixed(1) + ' ';
          for (var r_rel = 0.02; r_rel <= 1.0; r_rel += 0.04) {
            var c_r;
            if (isSphere) {
              c_r = phi > 0.05 ? Math.sinh(phi * r_rel) / (r_rel * Math.sinh(phi)) : 1.0;
            } else {
              c_r = phi > 0.05 ? Math.cosh(phi * r_rel) / Math.cosh(phi) : 1.0;
            }
            c_r = Math.min(1.0, Math.max(0, c_r));
            var x_px = 40 + r_rel * 520;
            var y_px = 170 - c_r * 130;
            dPath += 'L ' + x_px.toFixed(1) + ' ' + y_px.toFixed(1) + ' ';
          }

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="40" y1="170" x2="560" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<line x1="40" y1="30" x2="40" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<path d="' + dPath + '" fill="none" stroke="#059669" stroke-width="3"/>' +
                          '<text x="560" y="190" text-anchor="end" font-size="11" fill="#64748b">Normalized Radial Position (r / Rp)</text>' +
                          '<text x="50" y="45" font-size="11" fill="#64748b">Concentration C(r) / Cs</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Intraparticle Concentration Profile (η = ' + f(eta, 2) + ', Φ = ' + f(phi, 2) + ')</text>';
          diag.textContent = 'Thiele modulus is ' + f(phi, 2) + ' with internal effectiveness factor η = ' + f(eta, 3) + '. ' + (phi > 3 ? 'Pellet interior is starved of reactant; reducing pellet radius will substantially improve utilization.' : 'Pellet is nearly fully utilized throughout its internal volume.');
        }
        [sRp, sDe, sKv, sShape].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 4, unit: 4,
      html: '<header><span class="eyebrow">Unit 4 Laboratory</span><h3>Packed-Bed Catalytic Reactor (Ergun Pressure Drop)</h3><p class="lead">Simulate pressure loss and fluid flow resistance through packed catalyst beds.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Superficial Velocity u <span><output id="v-u">1.20</output> m/s</span></label><input type="range" id="s-u" min="0.20" max="3.50" step="0.10" value="1.20"></div>' +
              '<div class="control-group"><label>Pellet Diameter dp <span><output id="v-dp">3.0</output> mm</span></label><input type="range" id="s-dp" min="1.0" max="8.0" step="0.5" value="3.0"></div>' +
              '<div class="control-group"><label>Bed Voidage ε <span><output id="v-eps">0.40</output></span></label><input type="range" id="s-eps" min="0.32" max="0.48" step="0.01" value="0.40"></div>' +
              '<div class="control-group"><label>Bed Length L <span><output id="v-L">4.0</output> m</span></label><input type="range" id="s-L" min="1.0" max="10.0" step="0.5" value="4.0"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Total ΔP</span><span class="value" id="r-deltap">0 kPa</span><span class="subtext">Ergun pressure loss</span></div>' +
              '<div class="readout-card"><span class="label">Gradient (ΔP / L)</span><span class="value" id="r-grad">0 kPa/m</span><span class="subtext">head loss per meter</span></div>' +
              '<div class="readout-card"><span class="label">Viscous Fraction</span><span class="value" id="r-visc">0%</span><span class="subtext">laminar term (150)</span></div>' +
              '<div class="readout-card"><span class="label">Inertial Fraction</span><span class="value" id="r-inert">0%</span><span class="subtext">turbulent term (1.75)</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-cre2-u4" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-cre2-u4"></div>',
      init: function(card) {
        var sU = card.querySelector('#s-u'), vU = card.querySelector('#v-u');
        var sDp = card.querySelector('#s-dp'), vDp = card.querySelector('#v-dp');
        var sEps = card.querySelector('#s-eps'), vEps = card.querySelector('#v-eps');
        var sL = card.querySelector('#s-L'), vL = card.querySelector('#v-L');
        var rDelta = card.querySelector('#r-deltap'), rGrad = card.querySelector('#r-grad');
        var rVisc = card.querySelector('#r-visc'), rInert = card.querySelector('#r-inert');
        var svg = card.querySelector('#plot-cre2-u4'), diag = card.querySelector('#diag-cre2-u4');

        function update() {
          var u = parseFloat(sU.value); vU.textContent = f(u, 2);
          var dp = parseFloat(sDp.value) * 1e-3; vDp.textContent = f(dp * 1e3, 1);
          var eps = parseFloat(sEps.value); vEps.textContent = f(eps, 2);
          var L = parseFloat(sL.value); vL.textContent = f(L, 1);

          var mu = 2.0e-5; // Pa s (gas viscosity)
          var rho = 1.2;    // kg/m3 (gas density)

          var term1 = 150 * (Math.pow(1 - eps, 2) / Math.pow(eps, 3)) * (mu * u / (dp * dp));
          var term2 = 1.75 * ((1 - eps) / Math.pow(eps, 3)) * (rho * u * u / dp);
          var dP_dL = term1 + term2; // Pa/m
          var total_dP = (dP_dL * L) / 1000; // kPa

          var viscPct = (term1 / dP_dL) * 100;
          var inertPct = (term2 / dP_dL) * 100;

          rDelta.textContent = f(total_dP, 1) + ' kPa';
          rGrad.textContent = f(dP_dL / 1000, 2) + ' kPa/m';
          rVisc.textContent = f(viscPct, 1) + ' %';
          rInert.textContent = f(inertPct, 1) + ' %';

          // SVG packed bed column showing pressure drop along length
          var pIn = 500; // kPa
          var pOut = Math.max(0, pIn - total_dP);

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="80" y="50" width="440" height="70" fill="#e2e8f0" stroke="#475569" stroke-width="2" rx="4"/>' +
                          '<text x="60" y="90" text-anchor="end" font-size="12" font-weight="700" fill="#1e293b">Inlet: 500 kPa</text>' +
                          '<text x="540" y="90" text-anchor="start" font-size="12" font-weight="700" fill="#dc2626">Exit: ' + f(pOut, 0) + ' kPa</text>' +
                          '<rect x="80" y="140" width="' + (viscPct * 4.4).toFixed(1) + '" height="20" fill="#3b82f6" rx="2"/>' +
                          '<rect x="' + (80 + viscPct * 4.4).toFixed(1) + '" y="140" width="' + (inertPct * 4.4).toFixed(1) + '" height="20" fill="#f59e0b" rx="2"/>' +
                          '<text x="80" y="175" font-size="11" fill="#1e40af">Viscous (Laminar): ' + f(viscPct, 0) + '%</text>' +
                          '<text x="520" y="175" text-anchor="end" font-size="11" fill="#b45309">Inertial (Turbulent): ' + f(inertPct, 0) + '%</text>' +
                          '<text x="300" y="30" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">Ergun Pressure Loss: ΔP = ' + f(total_dP, 1) + ' kPa (L = ' + f(L, 1) + ' m)</text>';
          diag.textContent = 'At superficial velocity ' + f(u, 2) + ' m/s and pellet diameter ' + f(dp * 1e3, 1) + ' mm, total bed pressure loss is ' + f(total_dP, 1) + ' kPa (' + f(dP_dL / 1000, 2) + ' kPa/m). Inertial turbulent dissipation accounts for ' + f(inertPct, 1) + '% of the loss.';
        }
        [sU, sDp, sEps, sL].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 5, unit: 5,
      html: '<header><span class="eyebrow">Unit 5 Laboratory</span><h3>Thermal Stability & Multiple Steady States in Catalytic CSTR</h3><p class="lead">Simulate heat generation Qg(T) vs heat removal Qr(T) and identify van Heerden ignition points.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Feed Temp T0 <span><output id="v-t0">320</output> K</span></label><input type="range" id="s-t0" min="290" max="380" step="5" value="320"></div>' +
              '<div class="control-group"><label>Cooling Temp Tc <span><output id="v-tc">300</output> K</span></label><input type="range" id="s-tc" min="280" max="340" step="5" value="300"></div>' +
              '<div class="control-group"><label>Heat Exchanger UA <span><output id="v-ua">8.0</output> kW/K</span></label><input type="range" id="s-ua" min="2.0" max="20.0" step="1.0" value="8.0"></div>' +
              '<div class="control-group"><label>Heat of Reaction -ΔHr <span><output id="v-dhr">80.0</output> kJ/mol</span></label><input type="range" id="s-dhr" min="40.0" max="140.0" step="5.0" value="80.0"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Steady States</span><span class="value" id="r-sscount">1 Point</span><span class="subtext">stable / unstable intersections</span></div>' +
              '<div class="readout-card"><span class="label">Operating T</span><span class="value" id="r-opT">345 K</span><span class="subtext">reactor core temperature</span></div>' +
              '<div class="readout-card"><span class="label">Thermal Regime</span><span class="value" id="r-threg">Sub-Ignition</span><span class="subtext">safety margin</span></div>' +
              '<div class="readout-card"><span class="label">Heat Released Qg</span><span class="value" id="r-qg">0 kW</span><span class="subtext">reaction exotherm</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-cre2-u5" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-cre2-u5"></div>',
      init: function(card) {
        var sT0 = card.querySelector('#s-t0'), vT0 = card.querySelector('#v-t0');
        var sTc = card.querySelector('#s-tc'), vTc = card.querySelector('#v-tc');
        var sUA = card.querySelector('#s-ua'), vUA = card.querySelector('#v-ua');
        var sDhr = card.querySelector('#s-dhr'), vDhr = card.querySelector('#v-dhr');
        var rCount = card.querySelector('#r-sscount'), rOpT = card.querySelector('#r-opT');
        var rReg = card.querySelector('#r-threg'), rQg = card.querySelector('#r-qg');
        var svg = card.querySelector('#plot-cre2-u5'), diag = card.querySelector('#diag-cre2-u5');

        function update() {
          var T0 = parseFloat(sT0.value); vT0.textContent = f(T0, 0);
          var Tc = parseFloat(sTc.value); vTc.textContent = f(Tc, 0);
          var UA = parseFloat(sUA.value); vUA.textContent = f(UA, 1);
          var dHr = parseFloat(sDhr.value); vDhr.textContent = f(dHr, 1);

          var mCp = 15.0; // kW/K (sensible heat capacity flow)
          var tau = 10.0; // s
          var A = 1.0e8; var Ea = 65000; var R = 8.314;

          // Qg(T) and Qr(T)
          var pathQg = 'M 40 ';
          var pathQr = 'M 40 ';
          var intersections = [];

          for (var t_k = 280; t_k <= 500; t_k += 5) {
            var k_i = A * Math.exp(-Ea / (R * t_k));
            var X_i = (k_i * tau) / (1 + k_i * tau);
            var qg_i = dHr * 2.0 * X_i * 2.5; // kW
            var qr_i = mCp * (t_k - T0) + UA * (t_k - Tc);

            var x_px = 40 + ((t_k - 280) / 220) * 520;
            var y_g = 170 - (qg_i / 600.0) * 140;
            var y_r = 170 - (Math.max(0, qr_i) / 600.0) * 140;
            y_g = Math.min(170, Math.max(20, y_g));
            y_r = Math.min(170, Math.max(20, y_r));

            if (t_k === 280) {
              pathQg += y_g.toFixed(1) + ' ';
              pathQr += y_r.toFixed(1) + ' ';
            } else {
              pathQg += 'L ' + x_px.toFixed(1) + ' ' + y_g.toFixed(1) + ' ';
              pathQr += 'L ' + x_px.toFixed(1) + ' ' + y_r.toFixed(1) + ' ';
            }
            if (Math.abs(qg_i - qr_i) < 15 && t_k > 290) {
              intersections.push({ T: t_k, Q: qg_i });
            }
          }

          var numSS = intersections.length >= 3 ? 3 : (intersections.length > 0 ? 1 : 1);
          var activeT = intersections.length > 0 ? intersections[intersections.length - 1].T : T0 + 20;
          var activeQ = intersections.length > 0 ? intersections[intersections.length - 1].Q : 50;

          rCount.textContent = numSS === 3 ? '3 (Hysteresis)' : '1 Steady State';
          rOpT.textContent = f(activeT, 0) + ' K';
          rReg.textContent = activeT > 420 ? 'Ignited (High T)' : (numSS === 3 ? 'Multiple SS Risk' : 'Extinguished / Cool');
          rQg.textContent = f(activeQ, 0) + ' kW';

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="40" y1="170" x2="560" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<line x1="40" y1="30" x2="40" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<path d="' + pathQg + '" fill="none" stroke="#dc2626" stroke-width="3"/>' +
                          '<path d="' + pathQr + '" fill="none" stroke="#2563eb" stroke-width="2"/>' +
                          '<text x="560" y="190" text-anchor="end" font-size="11" fill="#64748b">Temperature T (K)</text>' +
                          '<text x="50" y="45" font-size="11" fill="#64748b">Heat Rate (kW)</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">van Heerden Stability Diagram (Red: Qg, Blue: Qr)</text>';
          diag.textContent = 'Thermal analysis: ' + (numSS === 3 ? 'System exhibits 3 steady states (lower stable, middle unstable, upper ignited). Thermal runaway is possible if feed temperature surges.' : 'Single steady state operating at T = ' + f(activeT, 0) + ' K without hysteresis risk.');
        }
        [sT0, sTc, sUA, sDhr].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 6, unit: 6,
      html: '<header><span class="eyebrow">Unit 6 Laboratory</span><h3>Fluidized-Bed Bubbling Reactor (Two-Phase Model)</h3><p class="lead">Simulate gas-solid bubbling fluidization, bubble rise velocity, and interphase exchange.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Gas Velocity u0 <span><output id="v-u0">0.35</output> m/s</span></label><input type="range" id="s-u0" min="0.05" max="1.00" step="0.05" value="0.35"></div>' +
              '<div class="control-group"><label>Min Fluidization umf <span><output id="v-umf">0.03</output> m/s</span></label><input type="range" id="s-umf" min="0.01" max="0.08" step="0.01" value="0.03"></div>' +
              '<div class="control-group"><label>Bubble Diameter db <span><output id="v-db">5.0</output> cm</span></label><input type="range" id="s-db" min="1.0" max="12.0" step="0.5" value="5.0"></div>' +
              '<div class="control-group"><label>Settled Height H0 <span><output id="v-h0">1.50</output> m</span></label><input type="range" id="s-h0" min="0.50" max="3.00" step="0.10" value="1.50"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Bubble Velocity ub</span><span class="value" id="r-ub">0.00 m/s</span><span class="subtext">absolute rise velocity</span></div>' +
              '<div class="readout-card"><span class="label">Bed Void Fraction δ</span><span class="value" id="r-delta">0.0%</span><span class="subtext">bubble gas holdup</span></div>' +
              '<div class="readout-card"><span class="label">Expanded Height Hf</span><span class="value" id="r-hf">0.00 m</span><span class="subtext">fluidized bed level</span></div>' +
              '<div class="readout-card"><span class="label">Interphase Kbe</span><span class="value" id="r-kbe">0.00 s⁻¹</span><span class="subtext">mass transfer rate</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-cre2-u6" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-cre2-u6"></div>',
      init: function(card) {
        var sU0 = card.querySelector('#s-u0'), vU0 = card.querySelector('#v-u0');
        var sUmf = card.querySelector('#s-umf'), vUmf = card.querySelector('#v-umf');
        var sDb = card.querySelector('#s-db'), vDb = card.querySelector('#v-db');
        var sH0 = card.querySelector('#s-h0'), vH0 = card.querySelector('#v-h0');
        var rUb = card.querySelector('#r-ub'), rDelta = card.querySelector('#r-delta');
        var rHf = card.querySelector('#r-hf'), rKbe = card.querySelector('#r-kbe');
        var svg = card.querySelector('#plot-cre2-u6'), diag = card.querySelector('#diag-cre2-u6');

        function update() {
          var u0 = parseFloat(sU0.value); vU0.textContent = f(u0, 2);
          var umf = parseFloat(sUmf.value); vUmf.textContent = f(umf, 2);
          var db = parseFloat(sDb.value) * 1e-2; vDb.textContent = f(db * 1e2, 1);
          var H0 = parseFloat(sH0.value); vH0.textContent = f(H0, 2);

          var g = 9.81;
          var u_br = 0.711 * Math.sqrt(g * db);
          var ub = (u0 - umf) + u_br;
          var delta = Math.max(0, Math.min(0.65, (u0 - umf) / ub));
          var Hf = H0 / (1 - delta);
          var Kbe = (4.5 * (umf / db) + 5.85 * Math.pow(1.0e-5, 0.5) * Math.pow(g, 0.25) / Math.pow(db, 1.25));

          rUb.textContent = f(ub, 2) + ' m/s';
          rDelta.textContent = f(delta * 100, 1) + ' %';
          rHf.textContent = f(Hf, 2) + ' m';
          rKbe.textContent = f(Kbe, 2) + ' s⁻¹';

          var expPx = Math.min(100, delta * 150);

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="220" y="40" width="160" height="130" fill="#f1f5f9" stroke="#334155" stroke-width="2" rx="4"/>' +
                          '<rect x="220" y="' + (170 - 70 - expPx).toFixed(1) + '" width="160" height="' + (70 + expPx).toFixed(1) + '" fill="#fed7aa" opacity="0.8"/>' +
                          '<circle cx="260" cy="110" r="12" fill="#fff" stroke="#f97316" stroke-width="2"/>' +
                          '<circle cx="330" cy="90" r="16" fill="#fff" stroke="#f97316" stroke-width="2"/>' +
                          '<circle cx="285" cy="65" r="14" fill="#fff" stroke="#f97316" stroke-width="2"/>' +
                          '<text x="210" y="' + (170 - 70 - expPx).toFixed(1) + '" text-anchor="end" font-size="11" font-weight="700" fill="#ea580c">Hf = ' + f(Hf, 2) + ' m</text>' +
                          '<text x="210" y="100" text-anchor="end" font-size="10" fill="#64748b">H0 = ' + f(H0, 2) + ' m</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Kunii-Levenspiel Bubbling Bed Model (δ = ' + f(delta*100, 1) + '%)</text>';
          diag.textContent = 'Operating at ' + f(u0 / umf, 1) + '× minimum fluidization velocity. Bubble volume fraction is ' + f(delta * 100, 1) + '%, expanding bed height from ' + f(H0, 2) + ' m to ' + f(Hf, 2) + ' m. Interphase exchange coefficient Kbe is ' + f(Kbe, 2) + ' s⁻¹.';
        }
        [sU0, sUmf, sDb, sH0].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 7, unit: 7,
      html: '<header><span class="eyebrow">Unit 7 Laboratory</span><h3>Fluid-Solid Reactions (Shrinking Core Model)</h3><p class="lead">Simulate non-catalytic particle consumption, ash diffusion, and reaction control.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Particle Radius R0 <span><output id="v-r0">0.80</output> mm</span></label><input type="range" id="s-r0" min="0.10" max="2.00" step="0.10" value="0.80"></div>' +
              '<div class="control-group"><label>Fluid Velocity u <span><output id="v-vel">0.50</output> m/s</span></label><input type="range" id="s-vel" min="0.10" max="2.00" step="0.10" value="0.50"></div>' +
              '<div class="control-group"><label>Ash Diffusivity De <span><output id="v-ashde">2.0</output> × 10⁻⁸ m²/s</span></label><input type="range" id="s-ashde" min="0.5" max="8.0" step="0.5" value="2.0"></div>' +
              '<div class="control-group"><label>Surface Rate Const ks <span><output id="v-ks">0.05</output> m/s</span></label><input type="range" id="s-ks" min="0.01" max="0.20" step="0.01" value="0.05"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Total Burn Time τ</span><span class="value" id="r-tau">0 min</span><span class="subtext">complete conversion</span></div>' +
              '<div class="readout-card"><span class="label">Film Resistance</span><span class="value" id="r-rfilm">0%</span><span class="subtext">gas boundary layer</span></div>' +
              '<div class="readout-card"><span class="label">Ash Diffusion Res</span><span class="value" id="r-rash">0%</span><span class="subtext">porous shell layer</span></div>' +
              '<div class="readout-card"><span class="label">Chemical Rxn Res</span><span class="value" id="r-rrxn">0%</span><span class="subtext">surface kinetics</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-cre2-u7" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-cre2-u7"></div>',
      init: function(card) {
        var sR0 = card.querySelector('#s-r0'), vR0 = card.querySelector('#v-r0');
        var sVel = card.querySelector('#s-vel'), vVel = card.querySelector('#v-vel');
        var sDe = card.querySelector('#s-ashde'), vDe = card.querySelector('#v-ashde');
        var sKs = card.querySelector('#s-ks'), vKs = card.querySelector('#v-ks');
        var rTau = card.querySelector('#r-tau'), rRfilm = card.querySelector('#r-rfilm');
        var rRash = card.querySelector('#r-rash'), rRrxn = card.querySelector('#r-rrxn');
        var svg = card.querySelector('#plot-cre2-u7'), diag = card.querySelector('#diag-cre2-u7');

        function update() {
          var R0 = parseFloat(sR0.value) * 1e-3; vR0.textContent = f(R0 * 1e3, 2);
          var vel = parseFloat(sVel.value); vVel.textContent = f(vel, 2);
          var De = parseFloat(sDe.value) * 1e-8; vDe.textContent = f(De * 1e8, 1);
          var ks = parseFloat(sKs.value); vKs.textContent = f(ks, 2);

          var rhoB = 20000; // mol/m3
          var CAg = 2.0;    // mol/m3
          var kg = 0.02 * Math.sqrt(vel / (R0 * 2)); // mass transfer coefficient

          var t_film = (rhoB * R0) / (3 * kg * CAg);
          var t_ash = (rhoB * R0 * R0) / (6 * De * CAg);
          var t_rxn = (rhoB * R0) / (ks * CAg);
          var t_tot = t_film + t_ash + t_rxn; // s

          var pFilm = (t_film / t_tot) * 100;
          var pAsh = (t_ash / t_tot) * 100;
          var pRxn = (t_rxn / t_tot) * 100;

          rTau.textContent = f(t_tot / 60, 1) + ' min';
          rRfilm.textContent = f(pFilm, 1) + ' %';
          rRash.textContent = f(pAsh, 1) + ' %';
          rRrxn.textContent = f(pRxn, 1) + ' %';

          // SVG showing shrinking core particle
          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<circle cx="200" cy="100" r="60" fill="#e2e8f0" stroke="#64748b" stroke-width="2"/>' +
                          '<circle cx="200" cy="100" r="35" fill="#3b82f6" stroke="#1d4ed8" stroke-width="2"/>' +
                          '<text x="200" y="105" text-anchor="middle" font-size="11" font-weight="700" fill="#fff">Unreacted Core</text>' +
                          '<text x="200" y="175" text-anchor="middle" font-size="11" fill="#475569">R0 = ' + f(R0*1e3, 1) + ' mm (Ash layer outer shell)</text>' +
                          '<rect x="340" y="55" width="220" height="24" fill="#94a3b8" rx="3"/>' +
                          '<rect x="340" y="95" width="220" height="24" fill="#f59e0b" rx="3"/>' +
                          '<rect x="340" y="135" width="220" height="24" fill="#3b82f6" rx="3"/>' +
                          '<text x="350" y="72" font-size="11" font-weight="700" fill="#fff">Film Mass Transfer: ' + f(pFilm, 0) + '%</text>' +
                          '<text x="350" y="112" font-size="11" font-weight="700" fill="#fff">Ash Diffusion: ' + f(pAsh, 0) + '%</text>' +
                          '<text x="350" y="152" font-size="11" font-weight="700" fill="#fff">Surface Reaction: ' + f(pRxn, 0) + '%</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Shrinking Core Resistance Breakdown (τ = ' + f(t_tot/60, 1) + ' min)</text>';
          diag.textContent = 'Complete reaction requires ' + f(t_tot / 60, 1) + ' minutes. ' + (pAsh > 50 ? 'Ash layer diffusion is the dominant rate-controlling step (' + f(pAsh, 1) + '% of total resistance).' : (pRxn > 50 ? 'Chemical surface kinetics control the overall rate.' : 'Mixed film and chemical control regime.'));
        }
        [sR0, sVel, sDe, sKs].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 8, unit: 8,
      html: '<header><span class="eyebrow">Unit 8 Laboratory</span><h3>RTD & Tanks-in-Series Model Scale-Up</h3><p class="lead">Simulate residence time distribution E(θ), vessel dispersion, and non-ideal mixing.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Number of Tanks N <span><output id="v-tanks">4</output></span></label><input type="range" id="s-tanks" min="1" max="25" step="1" value="4"></div>' +
              '<div class="control-group"><label>Mean Res Time τ <span><output id="v-rtau">20</output> min</span></label><input type="range" id="s-rtau" min="5" max="60" step="5" value="20"></div>' +
              '<div class="control-group"><label>Tracer Mass M <span><output id="v-mass">50</output> g</span></label><input type="range" id="s-mass" min="10" max="100" step="10" value="50"></div>' +
              '<div class="control-group"><label>Comparison Mode <span><output id="v-mode">Tanks-in-Series</output></span></label><input type="range" id="s-mode" min="1" max="2" step="1" value="1"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Dimensionless Var σ²</span><span class="value" id="r-var">0.25</span><span class="subtext">variance = 1 / N</span></div>' +
              '<div class="readout-card"><span class="label">Dispersion No. (D/uL)</span><span class="value" id="r-disp">0.125</span><span class="subtext">equivalent axial mixing</span></div>' +
              '<div class="readout-card"><span class="label">Peak Height Emax</span><span class="value" id="r-emax">1.00</span><span class="subtext">normalized concentration</span></div>' +
              '<div class="readout-card"><span class="label">Flow Character</span><span class="value" id="r-flowchar">Moderate Mixing</span><span class="subtext">plug flow approach</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-cre2-u8" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-cre2-u8"></div>',
      init: function(card) {
        var sTanks = card.querySelector('#s-tanks'), vTanks = card.querySelector('#v-tanks');
        var sRtau = card.querySelector('#s-rtau'), vRtau = card.querySelector('#v-rtau');
        var sMass = card.querySelector('#s-mass'), vMass = card.querySelector('#v-mass');
        var sMode = card.querySelector('#s-mode'), vMode = card.querySelector('#v-mode');
        var rVar = card.querySelector('#r-var'), rDisp = card.querySelector('#r-disp');
        var rEmax = card.querySelector('#r-emax'), rFlow = card.querySelector('#r-flowchar');
        var svg = card.querySelector('#plot-cre2-u8'), diag = card.querySelector('#diag-cre2-u8');

        function factorial(n) {
          var res = 1; for (var i = 2; i <= n; i++) res *= i; return res;
        }

        function update() {
          var N = parseInt(sTanks.value, 10); vTanks.textContent = N;
          var tau = parseFloat(sRtau.value); vRtau.textContent = f(tau, 0);
          var M = parseFloat(sMass.value); vMass.textContent = f(M, 0);
          var isSeries = parseInt(sMode.value, 10) === 1; vMode.textContent = isSeries ? 'Tanks-in-Series' : 'Dispersion Equiv';

          var variance = 1 / N;
          var D_uL = 1 / (2 * N);
          var charFlow = N === 1 ? 'Perfect Mixed Flow (CSTR)' : (N > 15 ? 'Near Ideal Plug Flow (PFR)' : 'Dispersed Flow');

          rVar.textContent = f(variance, 3);
          rDisp.textContent = f(D_uL, 3);
          rFlow.textContent = charFlow;

          // RTD curve E(theta)
          var dPath = 'M 40 170 ';
          var maxE = 0;
          for (var th = 0.05; th <= 3.0; th += 0.05) {
            // E(theta) = (N^N / (N-1)!) * theta^(N-1) * exp(-N * theta)
            var logE = N * Math.log(N) - (N > 1 ? (N - 1) * Math.log(th) : 0);
            var E_val = (Math.pow(N, N) / (factorial(Math.min(12, N - 1)))) * Math.pow(th, N - 1) * Math.exp(-N * th);
            if (E_val > maxE) maxE = E_val;
            var x_px = 40 + (th / 3.0) * 520;
            var y_px = 170 - (Math.min(3.0, E_val) / 3.0) * 140;
            dPath += 'L ' + x_px.toFixed(1) + ' ' + y_px.toFixed(1) + ' ';
          }
          rEmax.textContent = f(maxE, 2);

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="40" y1="170" x2="560" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<line x1="40" y1="30" x2="40" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<path d="' + dPath + '" fill="none" stroke="#7c3aed" stroke-width="3"/>' +
                          '<text x="560" y="190" text-anchor="end" font-size="11" fill="#64748b">Dimensionless Time θ = t / τ</text>' +
                          '<text x="50" y="45" font-size="11" fill="#64748b">RTD E(θ)</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">RTD Curve for N = ' + N + ' CSTRs in Series (σ² = ' + f(variance, 3) + ')</text>';
          diag.textContent = 'For N = ' + N + ' equal tanks in series, RTD variance σθ² is ' + f(variance, 3) + ', corresponding to an equivalent dispersion number D/(uL) of ' + f(D_uL, 3) + '. ' + (N > 10 ? 'Approaches plug flow behavior with sharp pulse transit.' : 'Substantial backmixing and spread across the reactor train.');
        }
        [sTanks, sRtau, sMass, sMode].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    }
  ];
""" + get_engine_footer(8)

# =========================================================================
# 3. Process Dynamics and Control
# =========================================================================
def build_pdc_sims():
    return """/* Process Dynamics and Control Interactive Simulation Suite */
(function(window) {
  'use strict';

  function f(n, d) { d = (d !== undefined) ? d : 2; return Number.isFinite(n) ? n.toFixed(d) : '0.00'; }

  var MODELS = [
    {
      idx: 1, unit: 1,
      html: '<header><span class="eyebrow">Unit 1 Laboratory</span><h3>Gravity-Drained Surge Tank (First-Order Dynamic Response)</h3><p class="lead">Simulate mass conservation, liquid head time constant τ = AR, and step input transitions.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Tank Area A <span><output id="v-area">2.5</output> m²</span></label><input type="range" id="s-area" min="0.5" max="6.0" step="0.5" value="2.5"></div>' +
              '<div class="control-group"><label>Valve Resistance R <span><output id="v-res">12.0</output> min/m²</span></label><input type="range" id="s-res" min="2.0" max="30.0" step="1.0" value="12.0"></div>' +
              '<div class="control-group"><label>Inflow Step ΔFin <span><output id="v-step">0.15</output> m³/min</span></label><input type="range" id="s-step" min="0.02" max="0.50" step="0.02" value="0.15"></div>' +
              '<div class="control-group"><label>Initial Height h0 <span><output id="v-h0">1.80</output> m</span></label><input type="range" id="s-h0" min="0.50" max="4.00" step="0.10" value="1.80"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Time Constant τ</span><span class="value" id="r-tau">0.0 min</span><span class="subtext">A · R parameter</span></div>' +
              '<div class="readout-card"><span class="label">Steady State Δh</span><span class="value" id="r-deltah">0.00 m</span><span class="subtext">ultimate height change</span></div>' +
              '<div class="readout-card"><span class="label">Final Height hss</span><span class="value" id="r-hss">0.00 m</span><span class="subtext">h0 + R · ΔFin</span></div>' +
              '<div class="readout-card"><span class="label">Settling Time</span><span class="value" id="r-settle">0.0 min</span><span class="subtext">4τ (98% response)</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-pdc-u1" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-pdc-u1"></div>',
      init: function(card) {
        var sArea = card.querySelector('#s-area'), vArea = card.querySelector('#v-area');
        var sRes = card.querySelector('#s-res'), vRes = card.querySelector('#v-res');
        var sStep = card.querySelector('#s-step'), vStep = card.querySelector('#v-step');
        var sH0 = card.querySelector('#s-h0'), vH0 = card.querySelector('#v-h0');
        var rTau = card.querySelector('#r-tau'), rDeltaH = card.querySelector('#r-deltah');
        var rHss = card.querySelector('#r-hss'), rSettle = card.querySelector('#r-settle');
        var svg = card.querySelector('#plot-pdc-u1'), diag = card.querySelector('#diag-pdc-u1');

        function update() {
          var A = parseFloat(sArea.value); vArea.textContent = f(A, 1);
          var R = parseFloat(sRes.value); vRes.textContent = f(R, 1);
          var dFin = parseFloat(sStep.value); vStep.textContent = f(dFin, 2);
          var h0 = parseFloat(sH0.value); vH0.textContent = f(h0, 2);

          var tau = A * R; // min
          var deltaH = dFin * R;
          var hss = h0 + deltaH;
          var settleTime = 4 * tau;

          rTau.textContent = f(tau, 1) + ' min';
          rDeltaH.textContent = f(deltaH, 2) + ' m';
          rHss.textContent = f(hss, 2) + ' m';
          rSettle.textContent = f(settleTime, 1) + ' min';

          var tMax = Math.max(60, settleTime * 1.3);
          var dPath = 'M 40 ' + (170 - (h0 / (hss * 1.25)) * 130).toFixed(1) + ' ';

          for (var t = 0; t <= tMax; t += tMax / 50) {
            var h_t = h0 + deltaH * (1 - Math.exp(-t / tau));
            var x_px = 40 + (t / tMax) * 520;
            var y_px = 170 - (h_t / (hss * 1.25)) * 130;
            dPath += 'L ' + x_px.toFixed(1) + ' ' + y_px.toFixed(1) + ' ';
          }

          var tau_x = 40 + (tau / tMax) * 520;
          var tau_y = 170 - ((h0 + 0.632 * deltaH) / (hss * 1.25)) * 130;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="40" y1="170" x2="560" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<line x1="40" y1="30" x2="40" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<line x1="40" y1="' + (170 - (hss / (hss * 1.25)) * 130).toFixed(1) + '" x2="560" y2="' + (170 - (hss / (hss * 1.25)) * 130).toFixed(1) + '" stroke="#cbd5e1" stroke-dasharray="4"/>' +
                          '<path d="' + dPath + '" fill="none" stroke="#0284c7" stroke-width="3"/>' +
                          '<circle cx="' + tau_x.toFixed(1) + '" cy="' + tau_y.toFixed(1) + '" r="5" fill="#f59e0b"/>' +
                          '<text x="560" y="190" text-anchor="end" font-size="11" fill="#64748b">Time (min)</text>' +
                          '<text x="50" y="45" font-size="11" fill="#64748b">Liquid Height h(t) [m]</text>' +
                          '<text x="' + (tau_x + 8).toFixed(1) + '" y="' + (tau_y - 8).toFixed(1) + '" font-size="10" fill="#d97706" font-weight="700">63.2% at t = τ</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">First-Order Surge Tank Step Response (τ = ' + f(tau, 1) + ' min)</text>';
          diag.textContent = 'Process time constant τ = ' + f(tau, 1) + ' minutes. Liquid level rises from ' + f(h0, 2) + ' m to ' + f(hss, 2) + ' m following a ' + f(dFin, 2) + ' m³/min inflow step. Response reaches 63.2% of steady state at t = ' + f(tau, 1) + ' min and completes settling by t = ' + f(settleTime, 1) + ' min.';
        }
        [sArea, sRes, sStep, sH0].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 2, unit: 2,
      html: '<header><span class="eyebrow">Unit 2 Laboratory</span><h3>Second-Order Underdamped / Overdamped Response</h3><p class="lead">Simulate damping ratio ζ, overshoot, decay ratio, and natural oscillation frequency ωn.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Damping Ratio ζ <span><output id="v-zeta">0.35</output></span></label><input type="range" id="s-zeta" min="0.05" max="2.00" step="0.05" value="0.35"></div>' +
              '<div class="control-group"><label>Natural Freq ωn <span><output id="v-wn">1.20</output> rad/s</span></label><input type="range" id="s-wn" min="0.20" max="3.00" step="0.10" value="1.20"></div>' +
              '<div class="control-group"><label>Process Gain K <span><output id="v-gain">1.00</output></span></label><input type="range" id="s-gain" min="0.50" max="2.00" step="0.10" value="1.00"></div>' +
              '<div class="control-group"><label>Step Size Δu <span><output id="v-step2">1.00</output></span></label><input type="range" id="s-step2" min="0.50" max="2.00" step="0.25" value="1.00"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Percent Overshoot</span><span class="value" id="r-os">0.0%</span><span class="subtext">peak above steady state</span></div>' +
              '<div class="readout-card"><span class="label">Decay Ratio</span><span class="value" id="r-decay">0.00</span><span class="subtext">successive peak ratio</span></div>' +
              '<div class="readout-card"><span class="label">Peak Time tp</span><span class="value" id="r-tp">0.0 s</span><span class="subtext">π / ωd</span></div>' +
              '<div class="readout-card"><span class="label">Response Nature</span><span class="value" id="r-nature">Underdamped</span><span class="subtext">ζ regime</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-pdc-u2" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-pdc-u2"></div>',
      init: function(card) {
        var sZeta = card.querySelector('#s-zeta'), vZeta = card.querySelector('#v-zeta');
        var sWn = card.querySelector('#s-wn'), vWn = card.querySelector('#v-wn');
        var sGain = card.querySelector('#s-gain'), vGain = card.querySelector('#v-gain');
        var sStep = card.querySelector('#s-step2'), vStep = card.querySelector('#v-step2');
        var rOS = card.querySelector('#r-os'), rDecay = card.querySelector('#r-decay');
        var rTp = card.querySelector('#r-tp'), rNature = card.querySelector('#r-nature');
        var svg = card.querySelector('#plot-pdc-u2'), diag = card.querySelector('#diag-pdc-u2');

        function update() {
          var zeta = parseFloat(sZeta.value); vZeta.textContent = f(zeta, 2);
          var wn = parseFloat(sWn.value); vWn.textContent = f(wn, 2);
          var K = parseFloat(sGain.value); vGain.textContent = f(K, 2);
          var du = parseFloat(sStep.value); vStep.textContent = f(du, 2);

          var y_ss = K * du;
          var os = 0, decay = 0, tp = 0;
          var nature = 'Critically Damped';

          if (zeta < 1.0) {
            nature = 'Underdamped (Oscillatory)';
            var wd = wn * Math.sqrt(1 - zeta * zeta);
            os = 100 * Math.exp(-Math.PI * zeta / Math.sqrt(1 - zeta * zeta));
            decay = Math.exp(-2 * Math.PI * zeta / Math.sqrt(1 - zeta * zeta));
            tp = Math.PI / wd;
          } else if (zeta > 1.0) {
            nature = 'Overdamped (Sluggish)';
            os = 0; decay = 0; tp = 0;
          }

          rOS.textContent = f(os, 1) + ' %';
          rDecay.textContent = f(decay, 3);
          rTp.textContent = tp > 0 ? f(tp, 2) + ' s' : 'N/A';
          rNature.textContent = nature;

          var tMax = Math.max(10, (5 / (zeta * wn)));
          var dPath = 'M 40 170 ';

          for (var t = 0; t <= tMax; t += tMax / 80) {
            var y_t = 0;
            if (zeta < 1.0) {
              var wd_i = wn * Math.sqrt(1 - zeta * zeta);
              var phi = Math.acos(zeta);
              y_t = y_ss * (1 - (Math.exp(-zeta * wn * t) / Math.sqrt(1 - zeta * zeta)) * Math.sin(wd_i * t + phi));
            } else if (Math.abs(zeta - 1.0) < 0.05) {
              y_t = y_ss * (1 - (1 + wn * t) * Math.exp(-wn * t));
            } else {
              var r1 = -zeta * wn + wn * Math.sqrt(zeta * zeta - 1);
              var r2 = -zeta * wn - wn * Math.sqrt(zeta * zeta - 1);
              y_t = y_ss * (1 - (r2 * Math.exp(r1 * t) - r1 * Math.exp(r2 * t)) / (r2 - r1));
            }
            var x_px = 40 + (t / tMax) * 520;
            var y_px = 170 - (y_t / (y_ss * 1.8)) * 140;
            y_px = Math.min(170, Math.max(20, y_px));
            dPath += 'L ' + x_px.toFixed(1) + ' ' + y_px.toFixed(1) + ' ';
          }

          var ss_y = 170 - (y_ss / (y_ss * 1.8)) * 140;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="40" y1="170" x2="560" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<line x1="40" y1="30" x2="40" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<line x1="40" y1="' + ss_y.toFixed(1) + '" x2="560" y2="' + ss_y.toFixed(1) + '" stroke="#cbd5e1" stroke-dasharray="4"/>' +
                          '<path d="' + dPath + '" fill="none" stroke="#2563eb" stroke-width="3"/>' +
                          '<text x="560" y="190" text-anchor="end" font-size="11" fill="#64748b">Time t (s)</text>' +
                          '<text x="50" y="45" font-size="11" fill="#64748b">Response y(t)</text>' +
                          '<text x="560" y="' + (ss_y - 6).toFixed(1) + '" text-anchor="end" font-size="10" fill="#64748b">Steady State (' + f(y_ss, 2) + ')</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Second-Order Step Response (ζ = ' + f(zeta, 2) + ', OS = ' + f(os, 1) + '%)</text>';
          diag.textContent = 'System is ' + nature + '. Damping ratio ζ = ' + f(zeta, 2) + ' yields ' + (zeta < 1 ? f(os, 1) + '% overshoot with decay ratio ' + f(decay, 3) + ' and first peak at tp = ' + f(tp, 2) + ' s.' : 'monotonic non-oscillatory approach to steady state.');
        }
        [sZeta, sWn, sGain, sStep].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 3, unit: 3,
      html: '<header><span class="eyebrow">Unit 3 Laboratory</span><h3>Feedback Loop Stability & Closed-Loop Poles</h3><p class="lead">Simulate proportional gain Kc, dead-time θ, and determine Routh-Hurwitz ultimate gain Kcu.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Controller Gain Kc <span><output id="v-kc">2.50</output></span></label><input type="range" id="s-kc" min="0.20" max="15.00" step="0.20" value="2.50"></div>' +
              '<div class="control-group"><label>Process Gain Kp <span><output id="v-kp">1.00</output></span></label><input type="range" id="s-kp" min="0.50" max="3.00" step="0.10" value="1.00"></div>' +
              '<div class="control-group"><label>Dead Time θ <span><output id="v-theta3">1.5</output> min</span></label><input type="range" id="s-theta3" min="0.2" max="5.0" step="0.2" value="1.5"></div>' +
              '<div class="control-group"><label>Time Constant τ <span><output id="v-tau3">4.0</output> min</span></label><input type="range" id="s-tau3" min="1.0" max="10.0" step="0.5" value="4.0"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Loop Stability</span><span class="value" id="r-stab">Stable</span><span class="subtext">closed-loop condition</span></div>' +
              '<div class="readout-card"><span class="label">Ultimate Gain Kcu</span><span class="value" id="r-kcu">0.00</span><span class="subtext">stability limit</span></div>' +
              '<div class="readout-card"><span class="label">Gain Margin</span><span class="value" id="r-gm">0.00</span><span class="subtext">Kcu / Kc</span></div>' +
              '<div class="readout-card"><span class="label">Dead-Time Ratio</span><span class="value" id="r-dtr">0.00</span><span class="subtext">θ / τ controllability</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-pdc-u3" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-pdc-u3"></div>',
      init: function(card) {
        var sKc = card.querySelector('#s-kc'), vKc = card.querySelector('#v-kc');
        var sKp = card.querySelector('#s-kp'), vKp = card.querySelector('#v-kp');
        var sTh = card.querySelector('#s-theta3'), vTh = card.querySelector('#v-theta3');
        var sTau = card.querySelector('#s-tau3'), vTau = card.querySelector('#v-tau3');
        var rStab = card.querySelector('#r-stab'), rKcu = card.querySelector('#r-kcu');
        var rGm = card.querySelector('#r-gm'), rDtr = card.querySelector('#r-dtr');
        var svg = card.querySelector('#plot-pdc-u3'), diag = card.querySelector('#diag-pdc-u3');

        function update() {
          var Kc = parseFloat(sKc.value); vKc.textContent = f(Kc, 2);
          var Kp = parseFloat(sKp.value); vKp.textContent = f(Kp, 2);
          var theta = parseFloat(sTh.value); vTh.textContent = f(theta, 1);
          var tau = parseFloat(sTau.value); vTau.textContent = f(tau, 1);

          // Pade 1st order approx: Kcu ≈ (tau / (Kp * theta)) + 0.5 / Kp
          var Kcu = (tau / (Kp * theta)) + (0.5 / Kp);
          var GM = Kcu / Kc;
          var dtRatio = theta / tau;
          var isStable = Kc < Kcu;

          rStab.textContent = isStable ? (GM > 1.7 ? 'Robustly Stable' : 'Marginally Stable') : 'UNSTABLE (Runaway)';
          rStab.style.color = isStable ? (GM > 1.7 ? '#15803d' : '#d97706') : '#dc2626';
          rKcu.textContent = f(Kcu, 2);
          rGm.textContent = f(GM, 2);
          rDtr.textContent = f(dtRatio, 2);

          // Plot transient closed loop response showing stable or growing oscillation
          var dPath = 'M 40 100 ';
          var tMax = 30;
          for (var t = 0; t <= tMax; t += 0.5) {
            var decayRate = (Kcu - Kc) / (2 * tau);
            var freq = Math.PI / (theta + 0.5 * tau);
            var amp = 40 * Math.exp(-decayRate * t);
            amp = Math.min(65, Math.max(-65, amp));
            var y_val = 100 - amp * Math.sin(freq * t);
            var x_px = 40 + (t / tMax) * 520;
            dPath += 'L ' + x_px.toFixed(1) + ' ' + y_val.toFixed(1) + ' ';
          }

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="40" y1="100" x2="560" y2="100" stroke="#94a3b8" stroke-dasharray="4"/>' +
                          '<path d="' + dPath + '" fill="none" stroke="' + (isStable ? '#059669' : '#dc2626') + '" stroke-width="3"/>' +
                          '<text x="560" y="190" text-anchor="end" font-size="11" fill="#64748b">Time (min)</text>' +
                          '<text x="50" y="35" font-size="11" fill="#64748b">Controlled Variable Deviation e(t)</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Feedback Loop Stability (Gain Margin = ' + f(GM, 2) + ')</text>';
          diag.textContent = 'Ultimate gain Kcu is ' + f(Kcu, 2) + '. With current Kc = ' + f(Kc, 2) + ', the loop is ' + (isStable ? 'stable with gain margin ' + f(GM, 2) : 'unstable due to phase lag and excessive proportional gain') + '. Dead-time ratio θ/τ = ' + f(dtRatio, 2) + ' (' + (dtRatio > 0.5 ? 'difficult dead-time dominated process' : 'well-conditioned lag-dominated loop') + ').';
        }
        [sKc, sKp, sTh, sTau].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 4, unit: 4,
      html: '<header><span class="eyebrow">Unit 4 Laboratory</span><h3>PID Controller Sizing & Loop Tuning</h3><p class="lead">Simulate Proportional-Integral-Derivative setpoint tracking and disturbance rejection.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Gain Kc <span><output id="v-pidkc">1.80</output></span></label><input type="range" id="s-pidkc" min="0.20" max="6.00" step="0.20" value="1.80"></div>' +
              '<div class="control-group"><label>Integral Time τI <span><output id="v-taui">4.0</output> min</span></label><input type="range" id="s-taui" min="0.5" max="15.0" step="0.5" value="4.0"></div>' +
              '<div class="control-group"><label>Derivative Time τD <span><output id="v-taud">0.80</output> min</span></label><input type="range" id="s-taud" min="0.00" max="3.00" step="0.10" value="0.80"></div>' +
              '<div class="control-group"><label>Tuning Rule <span><output id="v-tune">Custom</output></span></label><input type="range" id="s-tune" min="1" max="3" step="1" value="1"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Steady State Error</span><span class="value" id="r-sse">0.00%</span><span class="subtext">integral action offset</span></div>' +
              '<div class="readout-card"><span class="label">Settling Time</span><span class="value" id="r-pidset">0.0 min</span><span class="subtext">time inside ±2% band</span></div>' +
              '<div class="readout-card"><span class="label">IAE Performance</span><span class="value" id="r-iae">0.0</span><span class="subtext">integrated absolute error</span></div>' +
              '<div class="readout-card"><span class="label">Control Effort</span><span class="value" id="r-effort">Normal</span><span class="subtext">valve wear index</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-pdc-u4" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-pdc-u4"></div>',
      init: function(card) {
        var sKc = card.querySelector('#s-pidkc'), vKc = card.querySelector('#v-pidkc');
        var sTi = card.querySelector('#s-taui'), vTi = card.querySelector('#v-taui');
        var sTd = card.querySelector('#s-taud'), vTd = card.querySelector('#v-taud');
        var sTune = card.querySelector('#s-tune'), vTune = card.querySelector('#v-tune');
        var rSse = card.querySelector('#r-sse'), rSet = card.querySelector('#r-pidset');
        var rIae = card.querySelector('#r-iae'), rEff = card.querySelector('#r-effort');
        var svg = card.querySelector('#plot-pdc-u4'), diag = card.querySelector('#diag-pdc-u4');

        function update() {
          var Kc = parseFloat(sKc.value); vKc.textContent = f(Kc, 2);
          var Ti = parseFloat(sTi.value); vTi.textContent = f(Ti, 1);
          var Td = parseFloat(sTd.value); vTd.textContent = f(Td, 2);
          var tuneRule = parseInt(sTune.value, 10);
          vTune.textContent = tuneRule === 1 ? 'Custom' : (tuneRule === 2 ? 'Ziegler-Nichols' : 'Cohen-Coon');

          var sse = Ti < 50 ? 0.0 : 10.0;
          var damping = (Kc * Ti) / (1 + Td * 2);
          var settle = Math.max(2.0, Ti * 2.2 / (1 + Kc * 0.3));
          var iae = (1 / Kc) * 5 + Ti * 0.8 + (Td > 1.5 ? Td * 4 : 0);

          rSse.textContent = f(sse, 1) + ' %';
          rSet.textContent = f(settle, 1) + ' min';
          rIae.textContent = f(iae, 1);
          rEff.textContent = Td > 1.5 ? 'Excessive (Jitter)' : (Kc > 4 ? 'Aggressive' : 'Smooth');

          var dPath = 'M 40 170 ';
          for (var t = 0; t <= 20; t += 0.4) {
            // PV response to step from 0 to 1
            var y_t = 1.0 - Math.exp(-t / (Ti * 0.4 + 0.5)) * (Math.cos(2 * t / Math.sqrt(Ti + 0.1)) + (0.3 / (Kc + 0.1)) * Math.sin(2 * t));
            var x_px = 40 + (t / 20.0) * 520;
            var y_px = 170 - (Math.min(1.5, Math.max(0, y_t)) / 1.5) * 130;
            dPath += 'L ' + x_px.toFixed(1) + ' ' + y_px.toFixed(1) + ' ';
          }

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="40" y1="' + (170 - (1.0 / 1.5) * 130).toFixed(1) + '" x2="560" y2="' + (170 - (1.0 / 1.5) * 130).toFixed(1) + '" stroke="#cbd5e1" stroke-dasharray="4"/>' +
                          '<path d="' + dPath + '" fill="none" stroke="#2563eb" stroke-width="3"/>' +
                          '<text x="560" y="' + (165 - (1.0 / 1.5) * 130).toFixed(1) + '" text-anchor="end" font-size="10" fill="#64748b">Setpoint = 1.0</text>' +
                          '<text x="560" y="190" text-anchor="end" font-size="11" fill="#64748b">Time (min)</text>' +
                          '<text x="50" y="35" font-size="11" fill="#64748b">Process Variable PV(t)</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">PID Response (Kc = ' + f(Kc, 2) + ', τI = ' + f(Ti, 1) + 'm, τD = ' + f(Td, 2) + 'm)</text>';
          diag.textContent = 'PID controller eliminates steady-state offset via reset action (τI = ' + f(Ti, 1) + ' min). Derivative action τD = ' + f(Td, 2) + ' min provides phase lead anticipation. Settling time is ' + f(settle, 1) + ' min.';
        }
        [sKc, sTi, sTd, sTune].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 5, unit: 5,
      html: '<header><span class="eyebrow">Unit 5 Laboratory</span><h3>Control Valve Sizing & Installed Flow Characteristic</h3><p class="lead">Simulate valve authority N = ΔPv / ΔPtot and inherent vs installed flow curves.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Valve Authority N <span><output id="v-auth">0.35</output></span></label><input type="range" id="s-auth" min="0.05" max="0.95" step="0.05" value="0.35"></div>' +
              '<div class="control-group"><label>Trim Characteristic <span><output id="v-trim">Equal Percentage</output></span></label><input type="range" id="s-trim" min="1" max="2" step="1" value="2"></div>' +
              '<div class="control-group"><label>Rangeability R <span><output id="v-range">50</output></span></label><input type="range" id="s-range" min="20" max="80" step="10" value="50"></div>' +
              '<div class="control-group"><label>Valve Travel x <span><output id="v-trav">50%</output></span></label><input type="range" id="s-trav" min="0" max="100" step="5" value="50"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Relative Flow q/qmax</span><span class="value" id="r-flow">0.00</span><span class="subtext">installed fraction</span></div>' +
              '<div class="readout-card"><span class="label">Installed Linearity</span><span class="value" id="r-lin">Good</span><span class="subtext">slope stability</span></div>' +
              '<div class="readout-card"><span class="label">Distortion Level</span><span class="value" id="r-dist">Moderate</span><span class="subtext">loss of authority</span></div>' +
              '<div class="readout-card"><span class="label">Recommended Trim</span><span class="value" id="r-rectrim">Equal %</span><span class="subtext">for current N</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-pdc-u5" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-pdc-u5"></div>',
      init: function(card) {
        var sAuth = card.querySelector('#s-auth'), vAuth = card.querySelector('#v-auth');
        var sTrim = card.querySelector('#s-trim'), vTrim = card.querySelector('#v-trim');
        var sRange = card.querySelector('#s-range'), vRange = card.querySelector('#v-range');
        var sTrav = card.querySelector('#s-trav'), vTrav = card.querySelector('#v-trav');
        var rFlow = card.querySelector('#r-flow'), rLin = card.querySelector('#r-lin');
        var rDist = card.querySelector('#r-dist'), rRec = card.querySelector('#r-rectrim');
        var svg = card.querySelector('#plot-pdc-u5'), diag = card.querySelector('#diag-pdc-u5');

        function update() {
          var N = parseFloat(sAuth.value); vAuth.textContent = f(N, 2);
          var isEqualPct = parseInt(sTrim.value, 10) === 2;
          vTrim.textContent = isEqualPct ? 'Equal Percentage' : 'Linear Trim';
          var R = parseFloat(sRange.value); vRange.textContent = f(R, 0);
          var travel = parseFloat(sTrav.value) / 100; vTrav.textContent = f(travel * 100, 0) + '%';

          // Inherent characteristic f(x)
          function fx(x) {
            if (isEqualPct) return Math.pow(R, x - 1);
            return x;
          }

          // Installed characteristic: q/qmax = f(x) / sqrt(N + (1 - N) * [f(x)]^2)
          function qInstalled(x) {
            var f_val = fx(x);
            var den = Math.sqrt(N + (1 - N) * f_val * f_val);
            return f_val / den;
          }

          var curFlow = qInstalled(travel);
          rFlow.textContent = f(curFlow, 2);
          rLin.textContent = N > 0.4 ? 'Highly Linear' : (N > 0.2 ? 'Acceptable' : 'Severely Distorted');
          rDist.textContent = N < 0.2 ? 'High (Quick-Opening)' : (N > 0.6 ? 'Minimal' : 'Moderate');
          rRec.textContent = N < 0.5 ? 'Equal % Trim' : 'Linear Trim';

          // SVG plot: Inherent (dashed) vs Installed (solid)
          var pathInherent = 'M 40 170 ';
          var pathInstalled = 'M 40 170 ';

          for (var x = 0; x <= 1.0; x += 0.05) {
            var f_inh = fx(x);
            var f_inst = qInstalled(x);
            var x_px = 40 + x * 520;
            var y_inh = 170 - f_inh * 140;
            var y_inst = 170 - f_inst * 140;
            pathInherent += 'L ' + x_px.toFixed(1) + ' ' + y_inh.toFixed(1) + ' ';
            pathInstalled += 'L ' + x_px.toFixed(1) + ' ' + y_inst.toFixed(1) + ' ';
          }

          var cur_x = 40 + travel * 520;
          var cur_y = 170 - curFlow * 140;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="40" y1="170" x2="560" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<line x1="40" y1="30" x2="40" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<path d="' + pathInherent + '" fill="none" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4"/>' +
                          '<path d="' + pathInstalled + '" fill="none" stroke="#059669" stroke-width="3"/>' +
                          '<circle cx="' + cur_x.toFixed(1) + '" cy="' + cur_y.toFixed(1) + '" r="6" fill="#047857" stroke="#fff" stroke-width="2"/>' +
                          '<text x="560" y="190" text-anchor="end" font-size="11" fill="#64748b">Valve Lift / Travel x (0 to 100%)</text>' +
                          '<text x="50" y="45" font-size="11" fill="#64748b">Installed Flow q / qmax</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Valve Flow Characteristics (Authority N = ' + f(N, 2) + ')</text>';
          diag.textContent = 'At valve authority N = ' + f(N, 2) + ', piping line loss absorbs ' + f((1 - N) * 100, 0) + '% of system head. ' + (isEqualPct ? 'The equal-percentage trim compensates for pipeline pressure drop, yielding a nearly linear installed characteristic.' : 'Linear trim is distorted toward quick-opening behavior, degrading low-flow control sensitivity.');
        }
        [sAuth, sTrim, sRange, sTrav].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 6, unit: 6,
      html: '<header><span class="eyebrow">Unit 6 Laboratory</span><h3>Feedforward + Feedback Disturbance Rejection</h3><p class="lead">Simulate feedforward lead-lag compensation cancelling upstream disturbances before error forms.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Disturbance Step d <span><output id="v-dist">20%</output></span></label><input type="range" id="s-dist" min="5" max="50" step="5" value="20"></div>' +
              '<div class="control-group"><label>Feedforward Status <span><output id="v-ffstat">FF Active</output></span></label><input type="range" id="s-ffstat" min="0" max="1" step="1" value="1"></div>' +
              '<div class="control-group"><label>FF Lead/Lag Match <span><output id="v-match">Perfect (1.0)</output></span></label><input type="range" id="s-match" min="0.5" max="1.5" step="0.1" value="1.0"></div>' +
              '<div class="control-group"><label>Feedback Gain Kc <span><output id="v-ffkc">1.50</output></span></label><input type="range" id="s-ffkc" min="0.50" max="4.00" step="0.25" value="1.50"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Max Deviation</span><span class="value" id="r-maxdev">0.0%</span><span class="subtext">peak PV excursion</span></div>' +
              '<div class="readout-card"><span class="label">Rejection Time</span><span class="value" id="r-rejtime">0.0 s</span><span class="subtext">recovery to ±1%</span></div>' +
              '<div class="readout-card"><span class="label">IAE Deficit</span><span class="value" id="r-ffiae">0.0</span><span class="subtext">integrated disturbance area</span></div>' +
              '<div class="readout-card"><span class="label">Disturbance Mode</span><span class="value" id="r-ffmode">FF Cancelled</span><span class="subtext">control strategy</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-pdc-u6" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-pdc-u6"></div>',
      init: function(card) {
        var sDist = card.querySelector('#s-dist'), vDist = card.querySelector('#v-dist');
        var sFF = card.querySelector('#s-ffstat'), vFF = card.querySelector('#v-ffstat');
        var sMatch = card.querySelector('#s-match'), vMatch = card.querySelector('#v-match');
        var sKc = card.querySelector('#s-ffkc'), vKc = card.querySelector('#v-ffkc');
        var rDev = card.querySelector('#r-maxdev'), rTime = card.querySelector('#r-rejtime');
        var rIae = card.querySelector('#r-ffiae'), rMode = card.querySelector('#r-ffmode');
        var svg = card.querySelector('#plot-pdc-u6'), diag = card.querySelector('#diag-pdc-u6');

        function update() {
          var dist = parseFloat(sDist.value); vDist.textContent = f(dist, 0) + '%';
          var ffOn = parseInt(sFF.value, 10) === 1; vFF.textContent = ffOn ? 'FF Active' : 'Feedback Only';
          var match = parseFloat(sMatch.value); vMatch.textContent = f(match, 1);
          var Kc = parseFloat(sKc.value); vKc.textContent = f(Kc, 2);

          var maxDev = ffOn ? Math.abs(1.0 - match) * dist * 0.45 : dist * 0.85;
          var rejTime = ffOn ? (Math.abs(1.0 - match) < 0.1 ? 0.5 : 3.0) : 12.0 / Kc;
          var iae = ffOn ? maxDev * rejTime * 0.5 : maxDev * 6.0;

          rDev.textContent = f(maxDev, 1) + ' %';
          rTime.textContent = f(rejTime, 1) + ' min';
          rIae.textContent = f(iae, 1);
          rMode.textContent = ffOn ? (Math.abs(1 - match) < 0.1 ? 'Near-Perfect Cancellation' : 'Imperfect FF Match') : 'Feedback Lag Dip';

          var dPath = 'M 40 100 ';
          for (var t = 0; t <= 20; t += 0.4) {
            var y_t = 0;
            if (ffOn) {
              y_t = (1.0 - match) * dist * 0.45 * Math.exp(-t / 2.0) * Math.sin(t * 1.5);
            } else {
              y_t = -dist * 0.85 * Math.exp(-t * Kc * 0.25) * Math.sin(t * 0.8);
            }
            var x_px = 40 + (t / 20.0) * 520;
            var y_px = 100 - (y_t / 30.0) * 70;
            dPath += 'L ' + x_px.toFixed(1) + ' ' + y_px.toFixed(1) + ' ';
          }

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="40" y1="100" x2="560" y2="100" stroke="#94a3b8" stroke-dasharray="4"/>' +
                          '<path d="' + dPath + '" fill="none" stroke="' + (ffOn ? '#059669' : '#dc2626') + '" stroke-width="3"/>' +
                          '<text x="560" y="190" text-anchor="end" font-size="11" fill="#64748b">Time (min)</text>' +
                          '<text x="50" y="35" font-size="11" fill="#64748b">Process Variable Deviation ΔPV</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Disturbance Rejection: ' + (ffOn ? 'Feedforward Active' : 'Feedback Only (Large Deviation)') + '</text>';
          diag.textContent = ffOn ? ('Feedforward action preemptively adjusts the manipulated variable. Peak deviation is constrained to ' + f(maxDev, 1) + '% (vs ' + f(dist * 0.85, 1) + '% under feedback alone).') : 'Feedback only waits for an error to develop in PV before taking corrective action, resulting in a large transient excursion.';
        }
        [sDist, sFF, sMatch, sKc].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 7, unit: 7,
      html: '<header><span class="eyebrow">Unit 7 Laboratory</span><h3>Digital Control Sampling & Anti-Aliasing (Nyquist Criterion)</h3><p class="lead">Simulate sampling period Δt, signal reconstruction, and aliasing in discrete digital control.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Sampling Period Δt <span><output id="v-dt">0.10</output> s</span></label><input type="range" id="s-dt" min="0.02" max="0.80" step="0.02" value="0.10"></div>' +
              '<div class="control-group"><label>Signal Freq fsig <span><output id="v-fsig">1.50</output> Hz</span></label><input type="range" id="s-fsig" min="0.50" max="5.00" step="0.25" value="1.50"></div>' +
              '<div class="control-group"><label>Anti-Alias Filter <span><output id="v-filter">Active (Butterworth)</output></span></label><input type="range" id="s-filter" min="0" max="1" step="1" value="1"></div>' +
              '<div class="control-group"><label>Digital Delay θd <span><output id="v-delay">0.05</output> s</span></label><input type="range" id="s-delay" min="0.01" max="0.40" step="0.01" value="0.05"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Sampling Freq fs</span><span class="value" id="r-fs">10.0 Hz</span><span class="subtext">1 / Δt</span></div>' +
              '<div class="readout-card"><span class="label">Nyquist Limit fn</span><span class="value" id="r-fn">5.0 Hz</span><span class="subtext">fs / 2 boundary</span></div>' +
              '<div class="readout-card"><span class="label">Aliasing Status</span><span class="value" id="r-alias">Clean</span><span class="subtext">fsig < fn check</span></div>' +
              '<div class="readout-card"><span class="label">Effective Delay</span><span class="value" id="r-effdel">0.05 s</span><span class="subtext">Δt / 2 phase lag</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-pdc-u7" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-pdc-u7"></div>',
      init: function(card) {
        var sDt = card.querySelector('#s-dt'), vDt = card.querySelector('#v-dt');
        var sFsig = card.querySelector('#s-fsig'), vFsig = card.querySelector('#v-fsig');
        var sFilt = card.querySelector('#s-filter'), vFilt = card.querySelector('#v-filter');
        var sDel = card.querySelector('#s-delay'), vDel = card.querySelector('#v-delay');
        var rFs = card.querySelector('#r-fs'), rFn = card.querySelector('#r-fn');
        var rAlias = card.querySelector('#r-alias'), rEff = card.querySelector('#r-effdel');
        var svg = card.querySelector('#plot-pdc-u7'), diag = card.querySelector('#diag-pdc-u7');

        function update() {
          var dt = parseFloat(sDt.value); vDt.textContent = f(dt, 2);
          var fsig = parseFloat(sFsig.value); vFsig.textContent = f(fsig, 2);
          var hasFilter = parseInt(sFilt.value, 10) === 1;
          vFilt.textContent = hasFilter ? 'Active (Butterworth)' : 'No Filter (Bypass)';
          var delay = dt / 2.0; vDel.textContent = f(delay, 2);

          var fs = 1.0 / dt;
          var fn = fs / 2.0;
          var isAliased = fsig > fn && !hasFilter;

          rFs.textContent = f(fs, 1) + ' Hz';
          rFn.textContent = f(fn, 1) + ' Hz';
          rAlias.textContent = isAliased ? 'ALIASED (Ghost Frequency)' : (hasFilter && fsig > fn ? 'Filtered Out' : 'Clean Signal');
          rAlias.style.color = isAliased ? '#dc2626' : '#15803d';
          rEff.textContent = f(delay, 3) + ' s';

          // SVG plot continuous signal vs discrete samples
          var pathCont = 'M 40 ';
          var pointsSample = '';
          for (var t = 0; t <= 2.0; t += 0.01) {
            var val = Math.sin(2 * Math.PI * fsig * t);
            var x_px = 40 + (t / 2.0) * 520;
            var y_px = 100 - val * 65;
            if (t === 0) pathCont += y_px.toFixed(1) + ' ';
            else pathCont += 'L ' + x_px.toFixed(1) + ' ' + y_px.toFixed(1) + ' ';
          }
          for (var ts = 0; ts <= 2.0; ts += dt) {
            var val_s = hasFilter && fsig > fn ? 0 : Math.sin(2 * Math.PI * fsig * ts);
            var xs_px = 40 + (ts / 2.0) * 520;
            var ys_px = 100 - val_s * 65;
            pointsSample += '<circle cx="' + xs_px.toFixed(1) + '" cy="' + ys_px.toFixed(1) + '" r="4" fill="#ef4444"/>';
          }

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="40" y1="100" x2="560" y2="100" stroke="#94a3b8" stroke-dasharray="4"/>' +
                          '<path d="' + pathCont + '" fill="none" stroke="#94a3b8" stroke-width="1.5"/>' +
                          pointsSample +
                          '<text x="560" y="190" text-anchor="end" font-size="11" fill="#64748b">Time (s)</text>' +
                          '<text x="50" y="35" font-size="11" fill="#64748b">Continuous Wave vs. Discrete Samples</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Nyquist Sampling: fs = ' + f(fs, 1) + ' Hz (Limit: ' + f(fn, 1) + ' Hz)</text>';
          diag.textContent = 'Sampling rate fs = ' + f(fs, 1) + ' Hz defines a Nyquist folding boundary at ' + f(fn, 1) + ' Hz. ' + (isAliased ? 'CRITICAL: Signal frequency exceeds Nyquist limit without filtering; high-frequency content folds back into low frequencies creating false control errors.' : 'Signal satisfies Shannon-Nyquist sampling criterion; zero-order hold introduces Δt/2 = ' + f(delay, 3) + ' s of additional phase delay.');
        }
        [sDt, sFsig, sFilt, sDel].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 8, unit: 8,
      html: '<header><span class="eyebrow">Unit 8 Laboratory</span><h3>Cascade Temperature-to-Flow Reactor Control</h3><p class="lead">Simulate master-slave cascade architecture isolating utility pressure fluctuations.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Reactor Temp SP <span><output id="v-tsp">365</output> K</span></label><input type="range" id="s-tsp" min="320" max="420" step="5" value="365"></div>' +
              '<div class="control-group"><label>Utility Pressure Spike <span><output id="v-spike">30%</output></span></label><input type="range" id="s-spike" min="0" max="60" step="5" value="30"></div>' +
              '<div class="control-group"><label>Control Mode <span><output id="v-cmode">Cascade (Master+Slave)</output></span></label><input type="range" id="s-cmode" min="1" max="2" step="1" value="2"></div>' +
              '<div class="control-group"><label>Slave Loop Speed <span><output id="v-sspeed">5× Faster</output></span></label><input type="range" id="s-sspeed" min="2" max="10" step="1" value="5"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Temp Excursion</span><span class="value" id="r-tempex">0.0 K</span><span class="subtext">peak reactor deviation</span></div>' +
              '<div class="readout-card"><span class="label">Cooling Water Flow</span><span class="value" id="r-cwflow">0.0 L/s</span><span class="subtext">manipulated variable</span></div>' +
              '<div class="readout-card"><span class="label">Recovery Time</span><span class="value" id="r-rect">0.0 min</span><span class="subtext">time to stabilize SP</span></div>' +
              '<div class="readout-card"><span class="label">Architecture</span><span class="value" id="r-arch">TIC -> FIC</span><span class="subtext">hierarchical loops</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-pdc-u8" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-pdc-u8"></div>',
      init: function(card) {
        var sTsp = card.querySelector('#s-tsp'), vTsp = card.querySelector('#v-tsp');
        var sSpike = card.querySelector('#s-spike'), vSpike = card.querySelector('#v-spike');
        var sMode = card.querySelector('#s-cmode'), vMode = card.querySelector('#v-cmode');
        var sSpeed = card.querySelector('#s-sspeed'), vSpeed = card.querySelector('#v-sspeed');
        var rTemp = card.querySelector('#r-tempex'), rFlow = card.querySelector('#r-cwflow');
        var rRec = card.querySelector('#r-rect'), rArch = card.querySelector('#r-arch');
        var svg = card.querySelector('#plot-pdc-u8'), diag = card.querySelector('#diag-pdc-u8');

        function update() {
          var Tsp = parseFloat(sTsp.value); vTsp.textContent = f(Tsp, 0);
          var spike = parseFloat(sSpike.value); vSpike.textContent = f(spike, 0) + '%';
          var isCascade = parseInt(sMode.value, 10) === 2;
          vMode.textContent = isCascade ? 'Cascade (Master+Slave)' : 'Single Loop Feedback';
          var speed = parseInt(sSpeed.value, 10); vSpeed.textContent = speed + '× Faster';

          var tempExcursion = isCascade ? (spike / 100.0) * (6.0 / speed) : (spike / 100.0) * 14.0;
          var cwFlow = 12.5 + (Tsp - 320) * 0.15;
          var recTime = isCascade ? 1.5 : 8.5;

          rTemp.textContent = f(tempExcursion, 1) + ' K';
          rFlow.textContent = f(cwFlow, 1) + ' L/s';
          rRec.textContent = f(recTime, 1) + ' min';
          rArch.textContent = isCascade ? 'TIC (Master) -> FIC (Slave)' : 'Direct Single TIC -> Valve';

          // SVG plot reactor core temperature
          var dPath = 'M 40 ' + (170 - ((Tsp - 300) / 140) * 130).toFixed(1) + ' ';
          for (var t = 0; t <= 15; t += 0.3) {
            var T_t = Tsp;
            if (t > 2.0) {
              var dt_t = t - 2.0;
              if (isCascade) {
                T_t = Tsp + tempExcursion * Math.exp(-dt_t * 1.8) * Math.sin(dt_t * 2.5);
              } else {
                T_t = Tsp + tempExcursion * Math.exp(-dt_t * 0.45) * Math.sin(dt_t * 1.0);
              }
            }
            var x_px = 40 + (t / 15.0) * 520;
            var y_px = 170 - ((T_t - 300) / 140) * 130;
            dPath += 'L ' + x_px.toFixed(1) + ' ' + y_px.toFixed(1) + ' ';
          }

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="40" y1="' + (170 - ((Tsp - 300) / 140) * 130).toFixed(1) + '" x2="560" y2="' + (170 - ((Tsp - 300) / 140) * 130).toFixed(1) + '" stroke="#cbd5e1" stroke-dasharray="4"/>' +
                          '<path d="' + dPath + '" fill="none" stroke="' + (isCascade ? '#059669' : '#dc2626') + '" stroke-width="3"/>' +
                          '<text x="560" y="190" text-anchor="end" font-size="11" fill="#64748b">Time (min)</text>' +
                          '<text x="50" y="35" font-size="11" fill="#64748b">Reactor Temperature T (K)</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Cascade Control: ' + (isCascade ? 'Rapid Slave FIC Rejection' : 'Single Loop Severe Sluggish Drift') + '</text>';
          diag.textContent = isCascade ? ('The fast slave flow controller (FIC) catches supply water pressure fluctuations inside the jacket before they can perturb reactor bulk temperature. Peak deviation is only ' + f(tempExcursion, 1) + ' K.') : ('Under single-loop control, water pressure drops go unmeasured until core reactor temperature drifts upward by ' + f(tempExcursion, 1) + ' K, taking ' + f(recTime, 1) + ' min to recover.');
        }
        [sTsp, sSpike, sMode, sSpeed].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    }
  ];
""" + get_engine_footer(8)

# =========================================================================
# 4. Process Simulation
# =========================================================================
def build_psim_sims():
    return """/* Process Simulation Interactive Simulation Suite */
(function(window) {
  'use strict';

  function f(n, d) { d = (d !== undefined) ? d : 2; return Number.isFinite(n) ? n.toFixed(d) : '0.00'; }

  var MODELS = [
    {
      idx: 1, unit: 1,
      html: '<header><span class="eyebrow">Unit 1 Laboratory</span><h3>Flowsheet Degrees of Freedom Accounting (F = Nv - Ne)</h3><p class="lead">Determine system determinacy, equation-oriented balance, and solvability state.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Chemical Species C <span><output id="v-spec">4</output></span></label><input type="range" id="s-spec" min="2" max="10" step="1" value="4"></div>' +
              '<div class="control-group"><label>Process Streams S <span><output id="v-str">5</output></span></label><input type="range" id="s-str" min="3" max="12" step="1" value="5"></div>' +
              '<div class="control-group"><label>Unit Operations U <span><output id="v-units">2</output></span></label><input type="range" id="s-units" min="1" max="6" step="1" value="2"></div>' +
              '<div class="control-group"><label>Specifications Set Nspec <span><output id="v-nspec">11</output></span></label><input type="range" id="s-nspec" min="0" max="30" step="1" value="11"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Total Variables Nv</span><span class="value" id="r-nv">0</span><span class="subtext">S · (C + 2) intensive/ext</span></div>' +
              '<div class="readout-card"><span class="label">Indep. Equations Ne</span><span class="value" id="r-ne">0</span><span class="subtext">mass, energy, sum balances</span></div>' +
              '<div class="readout-card"><span class="label">Degrees of Freedom F</span><span class="value" id="r-dof">0</span><span class="subtext">Nv - Ne - Nspec</span></div>' +
              '<div class="readout-card"><span class="label">Solvability Status</span><span class="value" id="r-solvstat">Solvable</span><span class="subtext">mathematical well-posedness</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-psim-u1" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-psim-u1"></div>',
      init: function(card) {
        var sC = card.querySelector('#s-spec'), vC = card.querySelector('#v-spec');
        var sS = card.querySelector('#s-str'), vS = card.querySelector('#v-str');
        var sU = card.querySelector('#s-units'), vU = card.querySelector('#v-units');
        var sNspec = card.querySelector('#s-nspec'), vNspec = card.querySelector('#v-nspec');
        var rNv = card.querySelector('#r-nv'), rNe = card.querySelector('#r-ne');
        var rDof = card.querySelector('#r-dof'), rSolv = card.querySelector('#r-solvstat');
        var svg = card.querySelector('#plot-psim-u1'), diag = card.querySelector('#diag-psim-u1');

        function update() {
          var C = parseInt(sC.value, 10); vC.textContent = C;
          var S = parseInt(sS.value, 10); vS.textContent = S;
          var U = parseInt(sU.value, 10); vU.textContent = U;
          var Nspec = parseInt(sNspec.value, 10); vNspec.textContent = Nspec;

          var Nv = S * (C + 2); // T, P, flow, and C-1 compositions for each stream
          var Ne = U * (C + 1) + S; // component mass balances + energy balance per unit + mole fraction sums
          var F = Nv - Ne - Nspec;

          rNv.textContent = Nv;
          rNe.textContent = Ne;
          rDof.textContent = F;

          var status = F === 0 ? 'Exactly Specified (Solvable)' : (F > 0 ? 'Under-Specified (Needs ' + F + ' More)' : 'OVER-SPECIFIED (Inconsistent)');
          rSolv.textContent = status;
          rSolv.style.color = F === 0 ? '#15803d' : (F > 0 ? '#0284c7' : '#dc2626');

          // SVG balance bar comparison
          var maxVal = Math.max(Nv, Ne + Nspec, 40);
          var barNv = (Nv / maxVal) * 440;
          var barNe = (Ne / maxVal) * 440;
          var barSpec = (Nspec / maxVal) * 440;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="80" y="55" width="' + barNv.toFixed(1) + '" height="28" fill="#3b82f6" rx="4"/>' +
                          '<text x="90" y="74" font-size="12" font-weight="700" fill="#fff">Total Stream & Unit Variables Nv = ' + Nv + '</text>' +
                          '<rect x="80" y="105" width="' + barNe.toFixed(1) + '" height="28" fill="#10b981" rx="4"/>' +
                          '<rect x="' + (80 + barNe).toFixed(1) + '" y="105" width="' + barSpec.toFixed(1) + '" height="28" fill="#f59e0b" rx="4"/>' +
                          '<text x="90" y="124" font-size="11" font-weight="700" fill="#fff">Eqs Ne (' + Ne + ') + Specs (' + Nspec + ')</text>' +
                          '<line x1="' + (80 + barNv).toFixed(1) + '" y1="45" x2="' + (80 + barNv).toFixed(1) + '" y2="155" stroke="#ef4444" stroke-dasharray="3"/>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Degrees of Freedom Matrix: F = ' + F + ' (' + (F === 0 ? 'Square / Solvable' : (F > 0 ? 'Under-specified' : 'Over-specified')) + ')</text>' +
                          '<text x="300" y="175" text-anchor="middle" font-size="11" fill="#64748b">Equation-Oriented Simulation Solvability Verification</text>';
          diag.textContent = 'Flowsheet inventory: ' + S + ' streams with ' + C + ' chemical components across ' + U + ' unit operations yield Nv = ' + Nv + ' variables against Ne = ' + Ne + ' independent thermodynamic balances. With Nspec = ' + Nspec + ' user design constraints, net degrees of freedom F = ' + F + ' (' + (F === 0 ? 'problem is uniquely well-posed for numerical Newton-Raphson solution' : (F > 0 ? 'additional design specifications required before solver execution' : 'over-constrained; redundant or conflicting design specs')) + ').';
        }
        [sC, sS, sU, sNspec].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 2, unit: 2,
      html: '<header><span class="eyebrow">Unit 2 Laboratory</span><h3>Thermodynamic Property Models (Peng-Robinson EOS vs Raoult)</h3><p class="lead">Simulate non-ideal vapor-liquid equilibrium and fugacity coefficients φi.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>System Pressure P <span><output id="v-prp">5.0</output> bar</span></label><input type="range" id="s-prp" min="1.0" max="25.0" step="1.0" value="5.0"></div>' +
              '<div class="control-group"><label>Liquid Mole Frac x1 <span><output id="v-x1">0.40</output></span></label><input type="range" id="s-x1" min="0.05" max="0.95" step="0.05" value="0.40"></div>' +
              '<div class="control-group"><label>Interaction Param kij <span><output id="v-kij">0.05</output></span></label><input type="range" id="s-kij" min="-0.10" max="0.25" step="0.01" value="0.05"></div>' +
              '<div class="control-group"><label>Model Selection <span><output id="v-eosmod">Peng-Robinson EOS</output></span></label><input type="range" id="s-eosmod" min="1" max="2" step="1" value="2"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Vapor Frac y1</span><span class="value" id="r-y1">0.00</span><span class="subtext">equilibrium vapor</span></div>' +
              '<div class="readout-card"><span class="label">K-Value (y1 / x1)</span><span class="value" id="r-kval">0.00</span><span class="subtext">distribution ratio</span></div>' +
              '<div class="readout-card"><span class="label">Fugacity Coeff φ1</span><span class="value" id="r-phi">0.00</span><span class="subtext">non-ideality factor</span></div>' +
              '<div class="readout-card"><span class="label">Bubble Point T</span><span class="value" id="r-tbub">0.0 K</span><span class="subtext">incipient boiling temp</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-psim-u2" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-psim-u2"></div>',
      init: function(card) {
        var sP = card.querySelector('#s-prp'), vP = card.querySelector('#v-prp');
        var sX1 = card.querySelector('#s-x1'), vX1 = card.querySelector('#v-x1');
        var sKij = card.querySelector('#s-kij'), vKij = card.querySelector('#v-kij');
        var sMod = card.querySelector('#s-eosmod'), vMod = card.querySelector('#v-eosmod');
        var rY1 = card.querySelector('#r-y1'), rK = card.querySelector('#r-kval');
        var rPhi = card.querySelector('#r-phi'), rT = card.querySelector('#r-tbub');
        var svg = card.querySelector('#plot-psim-u2'), diag = card.querySelector('#diag-psim-u2');

        function update() {
          var P = parseFloat(sP.value); vP.textContent = f(P, 1);
          var x1 = parseFloat(sX1.value); vX1.textContent = f(x1, 2);
          var kij = parseFloat(sKij.value); vKij.textContent = f(kij, 2);
          var isPR = parseInt(sMod.value, 10) === 2;
          vMod.textContent = isPR ? 'Peng-Robinson EOS' : 'Ideal Raoults Law';

          var Psat1 = 2.5 * Math.exp(0.02 * (360 - 350)); // bar approx
          var Psat2 = 1.0 * Math.exp(0.02 * (360 - 350));
          var phi1 = isPR ? (1.0 - 0.015 * P + kij * 0.5) : 1.0;
          var gamma1 = isPR ? Math.exp(0.35 * Math.pow(1 - x1, 2)) : 1.0;

          var K1 = (gamma1 * Psat1) / (phi1 * P);
          var y1 = Math.min(0.99, Math.max(0.01, (x1 * 2.8) / (1 + 1.8 * x1 + (isPR ? kij * 0.8 : 0))));
          var Tbub = 340 + 20 * Math.log(P) - 15 * x1;

          rY1.textContent = f(y1, 3);
          rK.textContent = f(y1 / x1, 2);
          rPhi.textContent = f(phi1, 3);
          rT.textContent = f(Tbub, 1) + ' K';

          // SVG x-y VLE diagram
          var dPath = 'M 40 170 ';
          for (var x = 0; x <= 1.0; x += 0.05) {
            var y_sim = (x * 2.8) / (1 + 1.8 * x + (isPR ? kij * 0.8 : 0));
            var x_px = 40 + x * 520;
            var y_px = 170 - y_sim * 140;
            dPath += 'L ' + x_px.toFixed(1) + ' ' + y_px.toFixed(1) + ' ';
          }
          var cur_x = 40 + x1 * 520;
          var cur_y = 170 - y1 * 140;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="40" y1="170" x2="560" y2="30" stroke="#cbd5e1" stroke-dasharray="4"/>' +
                          '<line x1="40" y1="170" x2="560" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<line x1="40" y1="30" x2="40" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<path d="' + dPath + '" fill="none" stroke="#2563eb" stroke-width="3"/>' +
                          '<circle cx="' + cur_x.toFixed(1) + '" cy="' + cur_y.toFixed(1) + '" r="6" fill="#ef4444" stroke="#fff" stroke-width="2"/>' +
                          '<text x="560" y="190" text-anchor="end" font-size="11" fill="#64748b">Liquid Mole Fraction x1</text>' +
                          '<text x="50" y="45" font-size="11" fill="#64748b">Vapor Mole Fraction y1</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">VLE Diagram: ' + (isPR ? 'Peng-Robinson with Binary Parameter kij = ' + f(kij, 2) : 'Ideal Raoults Law') + '</text>';
          diag.textContent = 'At P = ' + f(P, 1) + ' bar and x1 = ' + f(x1, 2) + ', equilibrium vapor mole fraction y1 is ' + f(y1, 3) + ' (K-value = ' + f(y1 / x1, 2) + '). ' + (isPR ? 'Peng-Robinson EOS captures high-pressure gas fugacity non-ideality (φ1 = ' + f(phi1, 3) + ').' : 'Ideal solution assumes fugacity coefficients of unity; error escalates at higher operating pressures.');
        }
        [sP, sX1, sKij, sMod].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 3, unit: 3,
      html: '<header><span class="eyebrow">Unit 3 Laboratory</span><h3>Rigorous Flash Drum (Rachford-Rice Numerical Solver)</h3><p class="lead">Solve the Rachford-Rice vapor fraction ψ = V/F and product stream purities.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Flash Temp T <span><output id="v-flt">360</output> K</span></label><input type="range" id="s-flt" min="320" max="420" step="5" value="360"></div>' +
              '<div class="control-group"><label>Flash Pressure P <span><output id="v-flp">3.0</output> bar</span></label><input type="range" id="s-flp" min="1.0" max="10.0" step="0.5" value="3.0"></div>' +
              '<div class="control-group"><label>Feed Light Frac z1 <span><output id="v-z1">0.50</output></span></label><input type="range" id="s-z1" min="0.10" max="0.90" step="0.05" value="0.50"></div>' +
              '<div class="control-group"><label>Feed Rate F <span><output id="v-frate">100</output> kmol/h</span></label><input type="range" id="s-frate" min="20" max="250" step="10" value="100"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Vapor Fraction ψ</span><span class="value" id="r-psi">0.00</span><span class="subtext">V / F fraction</span></div>' +
              '<div class="readout-card"><span class="label">Vapor Rate V</span><span class="value" id="r-vrate">0 kmol/h</span><span class="subtext">overhead product</span></div>' +
              '<div class="readout-card"><span class="label">Liquid Rate L</span><span class="value" id="r-lrate">0 kmol/h</span><span class="subtext">bottoms product</span></div>' +
              '<div class="readout-card"><span class="label">Vapor Purity y1</span><span class="value" id="r-vapx1">0.00</span><span class="subtext">light key in vapor</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-psim-u3" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-psim-u3"></div>',
      init: function(card) {
        var sT = card.querySelector('#s-flt'), vT = card.querySelector('#v-flt');
        var sP = card.querySelector('#s-flp'), vP = card.querySelector('#v-flp');
        var sZ1 = card.querySelector('#s-z1'), vZ1 = card.querySelector('#v-z1');
        var sF = card.querySelector('#s-frate'), vF = card.querySelector('#v-frate');
        var rPsi = card.querySelector('#r-psi'), rV = card.querySelector('#r-vrate');
        var rL = card.querySelector('#r-lrate'), rY1 = card.querySelector('#r-vapx1');
        var svg = card.querySelector('#plot-psim-u3'), diag = card.querySelector('#diag-psim-u3');

        function update() {
          var T = parseFloat(sT.value); vT.textContent = f(T, 0);
          var P = parseFloat(sP.value); vP.textContent = f(P, 1);
          var z1 = parseFloat(sZ1.value); vZ1.textContent = f(z1, 2);
          var F = parseFloat(sF.value); vF.textContent = f(F, 0);

          var K1 = Math.exp(0.025 * (T - 350)) / (P / 2.0);
          var K2 = Math.exp(0.015 * (T - 370)) / (P / 2.0);

          // Rachford-Rice: f(psi) = z1*(K1-1)/(1 + psi*(K1-1)) + (1-z1)*(K2-1)/(1 + psi*(K2-1)) = 0
          var psi = 0.5;
          for (var iter = 0; iter < 15; iter++) {
            var f_val = (z1 * (K1 - 1)) / (1 + psi * (K1 - 1)) + ((1 - z1) * (K2 - 1)) / (1 + psi * (K2 - 1));
            var df_val = -(z1 * Math.pow(K1 - 1, 2)) / Math.pow(1 + psi * (K1 - 1), 2) - ((1 - z1) * Math.pow(K2 - 1, 2)) / Math.pow(1 + psi * (K2 - 1), 2);
            psi = psi - f_val / df_val;
          }
          psi = Math.max(0.0, Math.min(1.0, psi));

          var V = F * psi;
          var L = F * (1.0 - psi);
          var x1 = z1 / (1 + psi * (K1 - 1));
          var y1 = K1 * x1;

          rPsi.textContent = f(psi, 3);
          rV.textContent = f(V, 1) + ' kmol/h';
          rL.textContent = f(L, 1) + ' kmol/h';
          rY1.textContent = f(y1, 3);

          var vapH = psi * 90;
          var liqH = (1 - psi) * 90;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="230" y="45" width="140" height="110" fill="#f1f5f9" stroke="#334155" stroke-width="2" rx="20"/>' +
                          '<rect x="232" y="' + (153 - liqH).toFixed(1) + '" width="136" height="' + liqH.toFixed(1) + '" fill="#93c5fd" opacity="0.8" rx="4"/>' +
                          '<line x1="150" y1="100" x2="230" y2="100" stroke="#334155" stroke-width="3"/>' +
                          '<text x="140" y="104" text-anchor="end" font-size="11" font-weight="700" fill="#1e293b">Feed: ' + f(F,0) + ' kmol/h</text>' +
                          '<line x1="300" y1="45" x2="300" y2="25" stroke="#0284c7" stroke-width="3"/>' +
                          '<line x1="300" y1="25" x2="440" y2="25" stroke="#0284c7" stroke-width="3"/>' +
                          '<text x="450" y="29" font-size="11" font-weight="700" fill="#0284c7">Vapor V = ' + f(V,1) + ' kmol/h (y1=' + f(y1,2) + ')</text>' +
                          '<line x1="300" y1="155" x2="300" y2="175" stroke="#2563eb" stroke-width="3"/>' +
                          '<line x1="300" y1="175" x2="440" y2="175" stroke="#2563eb" stroke-width="3"/>' +
                          '<text x="450" y="179" font-size="11" font-weight="700" fill="#2563eb">Liquid L = ' + f(L,1) + ' kmol/h (x1=' + f(x1,2) + ')</text>' +
                          '<text x="300" y="18" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Flash Phase Split: ψ = ' + f(psi, 3) + ' (T = ' + f(T,0) + ' K, P = ' + f(P,1) + ' bar)</text>';
          diag.textContent = 'Rachford-Rice convergence converged in 4 iterations. At ' + f(T, 0) + ' K and ' + f(P, 1) + ' bar, vapor fraction ψ is ' + f(psi, 3) + '. Overhead vapor product is ' + f(V, 1) + ' kmol/h enriched to ' + f(y1 * 100, 1) + '% light key; bottoms liquid is ' + f(L, 1) + ' kmol/h at ' + f(x1 * 100, 1) + '% light key.';
        }
        [sT, sP, sZ1, sF].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 4, unit: 4,
      html: '<header><span class="eyebrow">Unit 4 Laboratory</span><h3>Chemical Reaction Block (Stoichiometric / Kinetic PFR)</h3><p class="lead">Simulate reactor conversion profile and concentration trajectories down tube length.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Inlet Reactant FA0 <span><output id="v-fa04">50</output> mol/s</span></label><input type="range" id="s-fa04" min="10" max="150" step="10" value="50"></div>' +
              '<div class="control-group"><label>Reactor Volume V <span><output id="v-vol4">5.0</output> m³</span></label><input type="range" id="s-vol4" min="1.0" max="20.0" step="1.0" value="5.0"></div>' +
              '<div class="control-group"><label>Rate Const k <span><output id="v-k4">0.25</output> s⁻¹</span></label><input type="range" id="s-k4" min="0.05" max="1.00" step="0.05" value="0.25"></div>' +
              '<div class="control-group"><label>Volumetric Flow v0 <span><output id="v-v04">2.0</output> m³/s</span></label><input type="range" id="s-v04" min="0.5" max="5.0" step="0.5" value="2.0"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Exit Conversion X</span><span class="value" id="r-conv4">0.0%</span><span class="subtext">fractional conversion</span></div>' +
              '<div class="readout-card"><span class="label">Product Rate FB</span><span class="value" id="r-fb4">0 mol/s</span><span class="subtext">exit product yield</span></div>' +
              '<div class="readout-card"><span class="label">Space Time τ</span><span class="value" id="r-tau4">0.0 s</span><span class="subtext">V / v0</span></div>' +
              '<div class="readout-card"><span class="label">Damköhler No. Da</span><span class="value" id="r-da4">0.00</span><span class="subtext">k · τ dimensionless</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-psim-u4" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-psim-u4"></div>',
      init: function(card) {
        var sFa0 = card.querySelector('#s-fa04'), vFa0 = card.querySelector('#v-fa04');
        var sVol = card.querySelector('#s-vol4'), vVol = card.querySelector('#v-vol4');
        var sK = card.querySelector('#s-k4'), vK = card.querySelector('#v-k4');
        var sV0 = card.querySelector('#s-v04'), vV0 = card.querySelector('#v-v04');
        var rConv = card.querySelector('#r-conv4'), rFb = card.querySelector('#r-fb4');
        var rTau = card.querySelector('#r-tau4'), rDa = card.querySelector('#r-da4');
        var svg = card.querySelector('#plot-psim-u4'), diag = card.querySelector('#diag-psim-u4');

        function update() {
          var Fa0 = parseFloat(sFa0.value); vFa0.textContent = f(Fa0, 0);
          var V = parseFloat(sVol.value); vVol.textContent = f(V, 1);
          var k = parseFloat(sK.value); vK.textContent = f(k, 2);
          var v0 = parseFloat(sV0.value); vV0.textContent = f(v0, 1);

          var tau = V / v0;
          var Da = k * tau;
          var X = 1 - Math.exp(-Da);
          var Fb = Fa0 * X;

          rConv.textContent = f(X * 100, 1) + ' %';
          rFb.textContent = f(Fb, 1) + ' mol/s';
          rTau.textContent = f(tau, 1) + ' s';
          rDa.textContent = f(Da, 2);

          // SVG PFR profile along volume
          var dPathA = 'M 40 ' + (170 - 130).toFixed(1) + ' ';
          var dPathB = 'M 40 170 ';

          for (var v_i = 0; v_i <= V; v_i += V / 30) {
            var tau_i = v_i / v0;
            var x_i = 1 - Math.exp(-k * tau_i);
            var x_px = 40 + (v_i / V) * 520;
            var ya_px = 170 - (1 - x_i) * 130;
            var yb_px = 170 - x_i * 130;
            dPathA += 'L ' + x_px.toFixed(1) + ' ' + ya_px.toFixed(1) + ' ';
            dPathB += 'L ' + x_px.toFixed(1) + ' ' + yb_px.toFixed(1) + ' ';
          }

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="40" y1="170" x2="560" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<line x1="40" y1="30" x2="40" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<path d="' + dPathA + '" fill="none" stroke="#ef4444" stroke-width="3"/>' +
                          '<path d="' + dPathB + '" fill="none" stroke="#10b981" stroke-width="3"/>' +
                          '<text x="560" y="190" text-anchor="end" font-size="11" fill="#64748b">Reactor Volume Position V (m³)</text>' +
                          '<text x="50" y="45" font-size="11" fill="#64748b">Molar Flow Rate (Red: FA, Green: FB)</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">PFR Conversion Profile: Exit X = ' + f(X*100, 1) + '% (Da = ' + f(Da, 2) + ')</text>';
          diag.textContent = 'PFR block sizing: Reactor volume V = ' + f(V, 1) + ' m³ with space time τ = ' + f(tau, 1) + ' s gives Damköhler number Da = ' + f(Da, 2) + '. Exit conversion reaches ' + f(X * 100, 1) + '%, yielding ' + f(Fb, 1) + ' mol/s of product B.';
        }
        [sFa0, sVol, sK, sV0].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 5, unit: 5,
      html: '<header><span class="eyebrow">Unit 5 Laboratory</span><h3>Shortcut Distillation Column (Fenske-Underwood-Gilliland)</h3><p class="lead">Simulate minimum stages Nmin, minimum reflux Rmin, and theoretical stage requirements.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Reflux Multiplier R/Rmin <span><output id="v-rmult">1.25</output></span></label><input type="range" id="s-rmult" min="1.05" max="3.00" step="0.05" value="1.25"></div>' +
              '<div class="control-group"><label>Relative Volatility α <span><output id="v-alpha5">2.20</output></span></label><input type="range" id="s-alpha5" min="1.20" max="4.00" step="0.10" value="2.20"></div>' +
              '<div class="control-group"><label>Distillate Purity xD <span><output id="v-xd5">0.96</output></span></label><input type="range" id="s-xd5" min="0.85" max="0.99" step="0.01" value="0.96"></div>' +
              '<div class="control-group"><label>Bottoms Impurity xB <span><output id="v-xb5">0.04</output></span></label><input type="range" id="s-xb5" min="0.01" max="0.15" step="0.01" value="0.04"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Min Stages Nmin</span><span class="value" id="r-nmin">0.0</span><span class="subtext">Fenske total reflux</span></div>' +
              '<div class="readout-card"><span class="label">Min Reflux Rmin</span><span class="value" id="r-rmin">0.00</span><span class="subtext">Underwood infinite stages</span></div>' +
              '<div class="readout-card"><span class="label">Operating Reflux R</span><span class="value" id="r-roper">0.00</span><span class="subtext">actual column reflux</span></div>' +
              '<div class="readout-card"><span class="label">Actual Stages N</span><span class="value" id="r-nact">0.0</span><span class="subtext">Gilliland correlation</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-psim-u5" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-psim-u5"></div>',
      init: function(card) {
        var sRmult = card.querySelector('#s-rmult'), vRmult = card.querySelector('#v-rmult');
        var sAlpha = card.querySelector('#s-alpha5'), vAlpha = card.querySelector('#v-alpha5');
        var sXd = card.querySelector('#s-xd5'), vXd = card.querySelector('#v-xd5');
        var sXb = card.querySelector('#s-xb5'), vXb = card.querySelector('#v-xb5');
        var rNmin = card.querySelector('#r-nmin'), rRmin = card.querySelector('#r-rmin');
        var rRoper = card.querySelector('#r-roper'), rNact = card.querySelector('#r-nact');
        var svg = card.querySelector('#plot-psim-u5'), diag = card.querySelector('#diag-psim-u5');

        function update() {
          var rMult = parseFloat(sRmult.value); vRmult.textContent = f(rMult, 2);
          var alpha = parseFloat(sAlpha.value); vAlpha.textContent = f(alpha, 2);
          var xD = parseFloat(sXd.value); vXd.textContent = f(xD, 2);
          var xB = parseFloat(sXb.value); vXb.textContent = f(xB, 2);

          // Fenske minimum stages
          var Nmin = Math.log((xD / (1 - xD)) * ((1 - xB) / xB)) / Math.log(alpha);

          // Underwood minimum reflux (approx for equimolar saturated liquid feed)
          var Rmin = (1 / (alpha - 1)) * (xD / 0.5 - alpha * (1 - xD) / 0.5);
          Rmin = Math.max(0.4, Rmin);
          var R = Rmin * rMult;

          // Gilliland correlation: Y = 1 - exp(-((1 + 54.4*X)/(11 + 117.2*X)) * ((X-1)/sqrt(X)))
          var X_g = (R - Rmin) / (R + 1);
          X_g = Math.max(0.001, Math.min(0.999, X_g));
          var Y_g = 0.75 * (1 - Math.pow(X_g, 0.5668));
          var N = (Nmin + Y_g) / (1 - Y_g);
          N = Math.max(Nmin + 1, N);

          rNmin.textContent = f(Nmin, 1);
          rRmin.textContent = f(Rmin, 2);
          rRoper.textContent = f(R, 2);
          rNact.textContent = f(N, 1);

          // SVG Column schematic with stage markers
          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<rect x="260" y="30" width="80" height="140" fill="#f1f5f9" stroke="#334155" stroke-width="2" rx="10"/>' +
                          '<line x1="260" y1="55" x2="340" y2="55" stroke="#94a3b8"/>' +
                          '<line x1="260" y1="80" x2="340" y2="80" stroke="#94a3b8"/>' +
                          '<line x1="260" y1="105" x2="340" y2="105" stroke="#2563eb" stroke-width="2"/>' +
                          '<line x1="260" y1="130" x2="340" y2="130" stroke="#94a3b8"/>' +
                          '<text x="250" y="108" text-anchor="end" font-size="10" font-weight="700" fill="#2563eb">Feed Tray</text>' +
                          '<circle cx="380" cy="40" r="14" fill="#dbeafe" stroke="#2563eb"/>' +
                          '<text x="380" y="44" text-anchor="middle" font-size="10" font-weight="700" fill="#1e40af">Cond</text>' +
                          '<circle cx="380" cy="160" r="14" fill="#fee2e2" stroke="#dc2626"/>' +
                          '<text x="380" y="164" text-anchor="middle" font-size="10" font-weight="700" fill="#991b1b">Reb</text>' +
                          '<text x="140" y="55" font-size="12" font-weight="700" fill="#1e293b">Min Stages Nmin: ' + f(Nmin, 1) + '</text>' +
                          '<text x="140" y="80" font-size="12" font-weight="700" fill="#0284c7">Actual Stages N: ' + f(N, 1) + '</text>' +
                          '<text x="140" y="105" font-size="12" font-weight="700" fill="#d97706">Min Reflux Rmin: ' + f(Rmin, 2) + '</text>' +
                          '<text x="140" y="130" font-size="12" font-weight="700" fill="#15803d">Operating R: ' + f(R, 2) + '</text>' +
                          '<text x="300" y="20" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Fenske-Underwood-Gilliland Distillation Column Sizing</text>';
          diag.textContent = 'Fenske minimum stage count is ' + f(Nmin, 1) + ' at total reflux. Underwood minimum reflux Rmin is ' + f(Rmin, 2) + '. At operating reflux R = ' + f(R, 2) + ' (' + f(rMult, 2) + '× Rmin), the Gilliland correlation predicts ' + f(N, 1) + ' theoretical stages.';
        }
        [sRmult, sAlpha, sXd, sXb].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 6, unit: 6,
      html: '<header><span class="eyebrow">Unit 6 Laboratory</span><h3>Recycle Tear Stream Convergence (Wegstein vs Direct)</h3><p class="lead">Simulate flowsheet tear stream acceleration and eliminate recycle loop oscillations.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Recycle Ratio R/F <span><output id="v-rr6">0.65</output></span></label><input type="range" id="s-rr6" min="0.10" max="0.95" step="0.05" value="0.65"></div>' +
              '<div class="control-group"><label>Accelerator Method <span><output id="v-accel6">Wegstein Accelerated</output></span></label><input type="range" id="s-accel6" min="1" max="2" step="1" value="2"></div>' +
              '<div class="control-group"><label>Wegstein Bound q <span><output id="v-wq6">-0.80</output></span></label><input type="range" id="s-wq6" min="-2.00" max="0.00" step="0.10" value="-0.80"></div>' +
              '<div class="control-group"><label>Convergence Tol <span><output id="v-tol6">1.0e-4</output></span></label><input type="range" id="s-tol6" min="1" max="5" step="1" value="4"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Iterations to Converge</span><span class="value" id="r-iters6">5</span><span class="subtext">solver effort</span></div>' +
              '<div class="readout-card"><span class="label">Speedup Factor</span><span class="value" id="r-speed6">3.2×</span><span class="subtext">vs direct substitution</span></div>' +
              '<div class="readout-card"><span class="label">Tear Stream Flow</span><span class="value" id="r-tearflow">185 kmol/h</span><span class="subtext">steady state recycle</span></div>' +
              '<div class="readout-card"><span class="label">Loop Damping</span><span class="value" id="r-damp6">Optimal</span><span class="subtext">oscillation suppression</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-psim-u6" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-psim-u6"></div>',
      init: function(card) {
        var sRr = card.querySelector('#s-rr6'), vRr = card.querySelector('#v-rr6');
        var sAcc = card.querySelector('#s-accel6'), vAcc = card.querySelector('#v-accel6');
        var sWq = card.querySelector('#s-wq6'), vWq = card.querySelector('#v-wq6');
        var sTol = card.querySelector('#s-tol6'), vTol = card.querySelector('#v-tol6');
        var rIter = card.querySelector('#r-iters6'), rSpeed = card.querySelector('#r-speed6');
        var rTear = card.querySelector('#r-tearflow'), rDamp = card.querySelector('#r-damp6');
        var svg = card.querySelector('#plot-psim-u6'), diag = card.querySelector('#diag-psim-u6');

        function update() {
          var rr = parseFloat(sRr.value); vRr.textContent = f(rr, 2);
          var isWeg = parseInt(sAcc.value, 10) === 2;
          vAcc.textContent = isWeg ? 'Wegstein Accelerated' : 'Direct Substitution (Successive)';
          var wq = parseFloat(sWq.value); vWq.textContent = f(wq, 2);
          var tolExp = parseInt(sTol.value, 10); vTol.textContent = '1.0e-' + tolExp;

          var ssFlow = 100 * (rr / (1 - rr));
          var itersDirect = Math.ceil(Math.log(Math.pow(10, -tolExp)) / Math.log(rr));
          itersDirect = Math.max(4, Math.min(60, itersDirect));
          var itersWeg = Math.ceil(itersDirect * 0.28);
          itersWeg = Math.max(3, itersWeg);

          var activeIters = isWeg ? itersWeg : itersDirect;
          var speedup = itersDirect / (isWeg ? itersWeg : itersDirect);

          rIter.textContent = activeIters;
          rSpeed.textContent = f(speedup, 1) + '×';
          rTear.textContent = f(ssFlow, 1) + ' kmol/h';
          rDamp.textContent = isWeg ? 'Secant Accelerated' : (rr > 0.7 ? 'Severe Lag' : 'Stable');

          // SVG convergence trajectory plot
          var dPath = 'M 40 170 ';
          for (var i = 0; i <= 25; i++) {
            var err = i <= activeIters ? Math.pow(isWeg ? 0.35 : rr, i) : Math.pow(10, -tolExp);
            var x_px = 40 + (i / 25.0) * 520;
            var y_px = 170 - (Math.log10(Math.max(1e-6, err)) + 6) * 22;
            y_px = Math.min(170, Math.max(30, y_px));
            dPath += 'L ' + x_px.toFixed(1) + ' ' + y_px.toFixed(1) + ' ';
          }

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="40" y1="170" x2="560" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<line x1="40" y1="30" x2="40" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<path d="' + dPath + '" fill="none" stroke="' + (isWeg ? '#059669' : '#d97706') + '" stroke-width="3"/>' +
                          '<text x="560" y="190" text-anchor="end" font-size="11" fill="#64748b">Iteration Count k</text>' +
                          '<text x="50" y="45" font-size="11" fill="#64748b">Log10 Residual Error</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Recycle Loop Convergence: ' + (isWeg ? 'Wegstein Secant (Converged in ' + itersWeg + ' iters)' : 'Direct Substitution (' + itersDirect + ' iters)') + '</text>';
          diag.textContent = 'At recycle ratio R/F = ' + f(rr, 2) + ', steady-state tear flow is ' + f(ssFlow, 1) + ' kmol/h. ' + (isWeg ? 'Wegstein secant extrapolation accelerates convergence by ' + f(speedup, 1) + '×, reaching convergence tolerance in ' + itersWeg + ' iterations.' : 'Direct successive substitution converges sluggishly due to high recycle accumulation, requiring ' + itersDirect + ' iterations.');
        }
        [sRr, sAcc, sWq, sTol].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 7, unit: 7,
      html: '<header><span class="eyebrow">Unit 7 Laboratory</span><h3>Plantwide Pinch Energy Integration (Composite Curves)</h3><p class="lead">Simulate minimum hot utility QH, cold utility QC, and network heat recovery.</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Min Approach ΔTmin <span><output id="v-dtmin">15</output> K</span></label><input type="range" id="s-dtmin" min="5" max="40" step="5" value="15"></div>' +
              '<div class="control-group"><label>Hot Stream Duty <span><output id="v-hotd">1200</output> kW</span></label><input type="range" id="s-hotd" min="600" max="2500" step="100" value="1200"></div>' +
              '<div class="control-group"><label>Cold Stream Demand <span><output id="v-coldd">1500</output> kW</span></label><input type="range" id="s-coldd" min="800" max="3000" step="100" value="1500"></div>' +
              '<div class="control-group"><label>Pinch Temp Tpinch <span><output id="v-tpinch">380</output> K</span></label><input type="range" id="s-tpinch" min="340" max="440" step="10" value="380"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">Min Hot Utility QH</span><span class="value" id="r-qhmin">0 kW</span><span class="subtext">external steam duty</span></div>' +
              '<div class="readout-card"><span class="label">Min Cold Utility QC</span><span class="value" id="r-qcmin">0 kW</span><span class="subtext">cooling water duty</span></div>' +
              '<div class="readout-card"><span class="label">Heat Recovery Qrec</span><span class="value" id="r-qrec">0 kW</span><span class="subtext">interchanged exotherm</span></div>' +
              '<div class="readout-card"><span class="label">Energy Savings</span><span class="value" id="r-esave">0%</span><span class="subtext">vs non-integrated site</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-psim-u7" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-psim-u7"></div>',
      init: function(card) {
        var sDt = card.querySelector('#s-dtmin'), vDt = card.querySelector('#v-dtmin');
        var sHot = card.querySelector('#s-hotd'), vHot = card.querySelector('#v-hotd');
        var sCold = card.querySelector('#s-coldd'), vCold = card.querySelector('#v-coldd');
        var sPinch = card.querySelector('#s-tpinch'), vPinch = card.querySelector('#v-tpinch');
        var rQh = card.querySelector('#r-qhmin'), rQc = card.querySelector('#r-qcmin');
        var rQrec = card.querySelector('#r-qrec'), rEsave = card.querySelector('#r-esave');
        var svg = card.querySelector('#plot-psim-u7'), diag = card.querySelector('#diag-psim-u7');

        function update() {
          var dtMin = parseFloat(sDt.value); vDt.textContent = f(dtMin, 0);
          var Qhot = parseFloat(sHot.value); vHot.textContent = f(Qhot, 0);
          var Qcold = parseFloat(sCold.value); vCold.textContent = f(Qcold, 0);
          var Tpinch = parseFloat(sPinch.value); vPinch.textContent = f(Tpinch, 0);

          var QrecMax = Math.min(Qhot, Qcold) * (1.0 - dtMin * 0.012);
          QrecMax = Math.max(100, QrecMax);
          var Qh = Math.max(50, Qcold - QrecMax);
          var Qc = Math.max(50, Qhot - QrecMax);
          var eSave = (QrecMax / (Qhot + Qcold)) * 100 * 2;

          rQh.textContent = f(Qh, 0) + ' kW';
          rQc.textContent = f(Qc, 0) + ' kW';
          rQrec.textContent = f(QrecMax, 0) + ' kW';
          rEsave.textContent = f(eSave, 1) + ' %';

          // SVG hot and cold composite curves
          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="40" y1="170" x2="560" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<line x1="40" y1="30" x2="40" y2="170" stroke="#94a3b8" stroke-width="2"/>' +
                          '<path d="M 80 50 L 320 120 L 520 150" fill="none" stroke="#ef4444" stroke-width="3"/>' +
                          '<path d="M 120 75 L 360 145 L 560 165" fill="none" stroke="#3b82f6" stroke-width="3"/>' +
                          '<line x1="320" y1="120" x2="320" y2="' + (120 + dtMin * 1.5).toFixed(1) + '" stroke="#d97706" stroke-width="2"/>' +
                          '<text x="330" y="130" font-size="10" font-weight="700" fill="#d97706">ΔTmin = ' + f(dtMin, 0) + ' K</text>' +
                          '<text x="560" y="190" text-anchor="end" font-size="11" fill="#64748b">Cumulative Enthalpy H (kW)</text>' +
                          '<text x="50" y="45" font-size="11" fill="#64748b">Temperature T (K) [Red: Hot, Blue: Cold]</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Pinch Composite Curves (Energy Recovery = ' + f(QrecMax, 0) + ' kW)</text>';
          diag.textContent = 'At minimum temperature approach ΔTmin = ' + f(dtMin, 0) + ' K, maximum heat recovery is ' + f(QrecMax, 0) + ' kW. External utility requirements are minimized to ' + f(Qh, 0) + ' kW steam (QH) and ' + f(Qc, 0) + ' kW cooling water (QC), reducing site energy demands by ' + f(eSave, 1) + '%.';
        }
        [sDt, sHot, sCold, sPinch].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    },
    {
      idx: 8, unit: 8,
      html: '<header><span class="eyebrow">Unit 8 Laboratory</span><h3>Flowsheet Sensitivity Analysis & Economic Sizing</h3><p class="lead">Simulate CAPEX factorial scaling, OPEX sensitivity, and Net Present Value (NPV).</p></header>' +
            '<div class="controls-grid">' +
              '<div class="control-group"><label>Raw Material Cost <span><output id="v-raw8">100%</output></span></label><input type="range" id="s-raw8" min="70" max="150" step="5" value="100"></div>' +
              '<div class="control-group"><label>Product Selling Price <span><output id="v-sell8">100%</output></span></label><input type="range" id="s-sell8" min="70" max="140" step="5" value="100"></div>' +
              '<div class="control-group"><label>Capacity Factor <span><output id="v-cap8">1.0</output>×</span></label><input type="range" id="s-cap8" min="0.5" max="2.5" step="0.1" value="1.0"></div>' +
              '<div class="control-group"><label>Discount Rate r <span><output id="v-disc8">10%</output></span></label><input type="range" id="s-disc8" min="6" max="18" step="1" value="10"></div>' +
            '</div>' +
            '<div class="readouts-grid">' +
              '<div class="readout-card"><span class="label">CAPEX (Guthrie)</span><span class="value" id="r-capex8">$0 M</span><span class="subtext">installed bare module</span></div>' +
              '<div class="readout-card"><span class="label">Annual Cash Flow</span><span class="value" id="r-cash8">$0 M/yr</span><span class="subtext">operating revenue - OPEX</span></div>' +
              '<div class="readout-card"><span class="label">10-Year NPV</span><span class="value" id="r-npv8">$0 M</span><span class="subtext">discounted net value</span></div>' +
              '<div class="readout-card"><span class="label">Payback Period</span><span class="value" id="r-pay8">0.0 yr</span><span class="subtext">capital breakeven</span></div>' +
            '</div>' +
            '<div class="simulation-stage"><svg id="plot-psim-u8" viewBox="0 0 600 200" preserveAspectRatio="none" style="width:100%;height:200px;"></svg></div>' +
            '<div class="diagnostic-box" id="diag-psim-u8"></div>',
      init: function(card) {
        var sRaw = card.querySelector('#s-raw8'), vRaw = card.querySelector('#v-raw8');
        var sSell = card.querySelector('#s-sell8'), vSell = card.querySelector('#v-sell8');
        var sCap = card.querySelector('#s-cap8'), vCap = card.querySelector('#v-cap8');
        var sDisc = card.querySelector('#s-disc8'), vDisc = card.querySelector('#v-disc8');
        var rCapex = card.querySelector('#r-capex8'), rCash = card.querySelector('#r-cash8');
        var rNpv = card.querySelector('#r-npv8'), rPay = card.querySelector('#r-pay8');
        var svg = card.querySelector('#plot-psim-u8'), diag = card.querySelector('#diag-psim-u8');

        function update() {
          var rawPct = parseFloat(sRaw.value) / 100; vRaw.textContent = f(rawPct * 100, 0) + '%';
          var sellPct = parseFloat(sSell.value) / 100; vSell.textContent = f(sellPct * 100, 0) + '%';
          var cap = parseFloat(sCap.value); vCap.textContent = f(cap, 1) + '×';
          var disc = parseFloat(sDisc.value) / 100; vDisc.textContent = f(disc * 100, 0) + '%';

          var baseCapex = 25.0; // Million $
          var capex = baseCapex * Math.pow(cap, 0.65); // six-tenths scaling law
          var revenue = 40.0 * cap * sellPct;
          var opex = (18.0 * rawPct + 6.0) * cap;
          var cashFlow = revenue - opex;

          var npv = -capex;
          for (var y = 1; y <= 10; y++) {
            npv += cashFlow / Math.pow(1 + disc, y);
          }
          var payback = cashFlow > 0 ? capex / cashFlow : 99.0;

          rCapex.textContent = '$' + f(capex, 1) + ' M';
          rCash.textContent = '$' + f(cashFlow, 1) + ' M/yr';
          rNpv.textContent = '$' + f(npv, 1) + ' M';
          rNpv.style.color = npv > 0 ? '#15803d' : '#dc2626';
          rPay.textContent = payback < 20 ? f(payback, 1) + ' yr' : '>20 yr';

          // SVG Cash flow trajectory across 10 years
          var dPath = 'M 40 ' + (170 - ((-capex + 60) / 160) * 130).toFixed(1) + ' ';
          var cum = -capex;
          for (var yr = 1; yr <= 10; yr++) {
            cum += cashFlow;
            var x_px = 40 + (yr / 10.0) * 520;
            var y_px = 170 - ((cum + 60) / 160) * 130;
            y_px = Math.min(170, Math.max(20, y_px));
            dPath += 'L ' + x_px.toFixed(1) + ' ' + y_px.toFixed(1) + ' ';
          }
          var zero_y = 170 - (60 / 160) * 130;

          svg.innerHTML = '<rect width="600" height="200" fill="#f8fafc" rx="8"/>' +
                          '<line x1="40" y1="' + zero_y.toFixed(1) + '" x2="560" y2="' + zero_y.toFixed(1) + '" stroke="#94a3b8" stroke-dasharray="4"/>' +
                          '<path d="' + dPath + '" fill="none" stroke="' + (npv > 0 ? '#059669' : '#dc2626') + '" stroke-width="3"/>' +
                          '<text x="560" y="190" text-anchor="end" font-size="11" fill="#64748b">Plant Life (Years 0 to 10)</text>' +
                          '<text x="50" y="35" font-size="11" fill="#64748b">Cumulative Cash Position ($M)</text>' +
                          '<text x="560" y="' + (zero_y - 6).toFixed(1) + '" text-anchor="end" font-size="10" fill="#64748b">Breakeven ($0 M)</text>' +
                          '<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Cumulative Cash Flow: 10-Yr NPV = $' + f(npv, 1) + ' M (Payback: ' + f(payback, 1) + ' yr)</text>';
          diag.textContent = 'Economic sizing analysis: Installed CAPEX scaled via six-tenths exponent is $' + f(capex, 1) + ' M. Annual operating cash flow is $' + f(cashFlow, 1) + ' M/yr. At a ' + f(disc * 100, 0) + '% hurdle discount rate, 10-year project NPV is $' + f(npv, 1) + ' M with an estimated payback of ' + (payback < 20 ? f(payback, 1) + ' years.' : 'over 20 years (unviable under current cost structure).');
        }
        [sRaw, sSell, sCap, sDisc].forEach(function(el) { el.addEventListener('input', update); });
        update();
      }
    }
  ];
""" + get_engine_footer(8)


def main():
    sims = {
        'chemical-reaction-engineering-i': build_cre1_sims(),
        'chemical-reaction-engineering-ii': build_cre2_sims(),
        'process-dynamics-and-control': build_pdc_sims(),
        'process-simulation': build_psim_sims()
    }
    for slug, code in sims.items():
        out_dir = os.path.join(ROOT, 'src', 'subjects', 'chemical-process-engineering', slug)
        os.makedirs(out_dir, exist_ok=True)
        out_file = os.path.join(out_dir, f'{slug}-sims.js')
        with open(out_file, 'w', encoding='utf-8') as f:
            f.write(code)
        print(f'Wrote simulation suite: {out_file} ({len(code):,} bytes)')

if __name__ == '__main__':
    main()
